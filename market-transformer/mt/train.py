"""Walk-forward training of the transformer and linear baselines.

Expanding window.  For each test block the model is trained only on data that ends 10 business
days before the block starts (embargo covers the 6-day forward target), with the last 15% of the
training window held out for early stopping.  Nothing from a test block is ever seen in training.
"""
from __future__ import annotations

import time

import numpy as np
import pandas as pd
import torch

from .model import CrossAssetTransformer

TEST_STARTS = ["2010-01-01", "2014-01-01", "2018-01-01", "2022-01-01"]
TRAIN_START = "2002-01-01"
EMBARGO = 10
N_GROUPS = 8


def folds(dates: pd.DatetimeIndex):
    t0 = dates.searchsorted(pd.Timestamp(TRAIN_START))
    out = []
    for k, s in enumerate(TEST_STARTS):
        a = dates.searchsorted(pd.Timestamp(s))
        b = dates.searchsorted(pd.Timestamp(TEST_STARTS[k + 1])) if k + 1 < len(TEST_STARTS) else len(dates)
        end_train = a - EMBARGO
        n = end_train - t0
        v0 = t0 + int(n * 0.85)
        out.append(dict(train=np.arange(t0, v0 - EMBARGO), val=np.arange(v0, end_train), test=np.arange(a, b)))
    return out


def fixed_groups(n_assets, seed=0):
    rng = np.random.default_rng(seed)
    return rng.permutation(n_assets) % N_GROUPS


# ----------------------------------------------------------------------------------------------
# batch builders
# ----------------------------------------------------------------------------------------------
def predict_batch(A, idx):
    x = A["feat"][idx]
    y = np.stack([A["y1"][idx], A["y2"][idx], A["y5"][idx]], -1)
    pad = ~A["avail"][idx]
    return x, y, pad


def fair_batch(A, idx, mask):
    """mask: (B, N) bool -> which assets' same-day move is hidden."""
    hist = A["feat"][idx - 1]                           # history known before t
    zt = np.nan_to_num(A["z"][idx])
    vis = (~mask) & A["avail"][idx]
    x = np.concatenate([hist, (zt * vis)[..., None], vis[..., None].astype(np.float32)], -1)
    y = np.where(mask, A["z"][idx], np.nan)[..., None]
    pad = ~A["avail"][idx]
    return x.astype(np.float32), y.astype(np.float32), pad


def masked_mse(pred, y):
    ok = ~torch.isnan(y)
    d = torch.where(ok, pred - torch.nan_to_num(y), torch.zeros_like(pred))
    return (d ** 2).sum() / ok.sum().clamp(min=1)


def train_model(kind, A, cls_ids, fold, seed, log, max_steps=2000, eval_every=100, patience=4, bs=16, lr=5e-4):
    torch.manual_seed(seed)
    rng = np.random.default_rng(seed)
    N = A["z"].shape[1]
    nf = A["feat"].shape[2] + (2 if kind == "fair" else 0)
    nout = 3 if kind == "predict" else 1
    model = CrossAssetTransformer(N, int(cls_ids.max()) + 1, nf, nout)
    opt = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-2)
    sched = torch.optim.lr_scheduler.OneCycleLR(opt, lr, total_steps=max_steps, pct_start=0.1)
    aid = torch.arange(N)
    cid = torch.as_tensor(cls_ids)

    def make(idx, r):
        if kind == "predict":
            return predict_batch(A, idx)
        return fair_batch(A, idx, r.random((len(idx), N)) < 1 / N_GROUPS)

    val_rng = np.random.default_rng(1234)
    vidx = fold["val"][:: max(1, len(fold["val"]) // 300)]
    val_batches = [make(vidx[i:i + 64], val_rng) for i in range(0, len(vidx), 64)]

    def val_loss():
        model.eval()
        tot, cnt = 0.0, 0
        with torch.no_grad():
            for x, y, pad in val_batches:
                p = model(torch.from_numpy(x), aid, cid, torch.from_numpy(pad))
                yt = torch.from_numpy(y)
                ok = ~torch.isnan(yt)
                tot += float(((p - torch.nan_to_num(yt)) ** 2)[ok].sum())
                cnt += int(ok.sum())
        model.train()
        return tot / cnt

    best, best_state, bad = val_loss(), None, 0
    log(f"  [{kind} seed{seed}] init val_mse={best:.5f}")
    best_state = {k: v.clone() for k, v in model.state_dict().items()}
    model.train()
    t0 = time.time()
    for step in range(1, max_steps + 1):
        x, y, pad = make(rng.choice(fold["train"], bs, replace=False), rng)
        p = model(torch.from_numpy(x), aid, cid, torch.from_numpy(pad))
        loss = masked_mse(p, torch.from_numpy(y))
        opt.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()
        sched.step()
        if step % eval_every == 0:
            vl = val_loss()
            log(f"  [{kind} seed{seed}] step{step} val_mse={vl:.5f} {time.time() - t0:.0f}s")
            if vl < best - 1e-5:
                best, bad = vl, 0
                best_state = {k: v.clone() for k, v in model.state_dict().items()}
            else:
                bad += 1
                if bad >= patience:
                    break
    model.load_state_dict(best_state)
    model.eval()
    return model


@torch.no_grad()
def infer_predict(model, A, cls_ids, idx, bs=64):
    N = A["z"].shape[1]
    aid, cid = torch.arange(N), torch.as_tensor(cls_ids)
    out = []
    for i in range(0, len(idx), bs):
        x, _, pad = predict_batch(A, idx[i:i + bs])
        out.append(model(torch.from_numpy(x), aid, cid, torch.from_numpy(pad)).numpy())
    return np.concatenate(out)


@torch.no_grad()
def infer_fair(model, A, cls_ids, idx, groups, bs=64):
    """Each asset hidden exactly once (with the other members of its fixed group)."""
    N = A["z"].shape[1]
    aid, cid = torch.arange(N), torch.as_tensor(cls_ids)
    out = np.zeros((len(idx), N), np.float32)
    for g in range(N_GROUPS):
        gm = groups == g
        for i in range(0, len(idx), bs):
            sl = idx[i:i + bs]
            m = np.broadcast_to(gm, (len(sl), N))
            x, _, pad = fair_batch(A, sl, m)
            p = model(torch.from_numpy(x), aid, cid, torch.from_numpy(pad)).numpy()[..., 0]
            out[i:i + len(sl), gm] = p[:, gm]
    return out


# ----------------------------------------------------------------------------------------------
# Linear baselines (same information sets, no non-linearity)
# ----------------------------------------------------------------------------------------------
ALPHAS = [1e1, 1e2, 1e3, 1e4, 1e5, 1e6]


def _ridge_path(X, Y, Xv, Yv):
    """Fit ridge for all alphas via SVD; choose alpha on validation MSE (NaN targets ignored -> 0-filled)."""
    mu = X.mean(0)
    Xc = X - mu
    U, s, Vt = np.linalg.svd(Xc, full_matrices=False)
    Ym = np.nan_to_num(Y)
    UtY = U.T @ Ym
    best = None
    for a in ALPHAS:
        W = Vt.T @ ((s / (s ** 2 + a))[:, None] * UtY)
        pv = (Xv - mu) @ W
        ok = ~np.isnan(Yv)
        mse = ((pv - np.nan_to_num(Yv)) ** 2)[ok].mean()
        if best is None or mse < best[0]:
            best = (mse, a, W)
    return mu, best[2], best[1]


def linear_predict(A, fold):
    """Cross-asset linear model: every asset's last 1d / 5d / 20d moves -> every asset's forward move."""
    f = A["feat"]

    def X(idx):
        return np.concatenate([f[idx, :, 0], f[idx, :, :5].sum(-1) / np.sqrt(5), f[idx, :, :20].sum(-1) / np.sqrt(20)], 1)

    out = []
    alphas = []
    for key in ("y1", "y2", "y5"):
        mu, W, a = _ridge_path(X(fold["train"]), A[key][fold["train"]], X(fold["val"]), A[key][fold["val"]])
        out.append((X(fold["test"]) - mu) @ W)
        alphas.append(a)
    return np.stack(out, -1), alphas


def linear_fair(A, fold, groups):
    """Linear 'fair value': same-day moves of the other groups + everyone's previous-day move."""
    z = np.nan_to_num(A["z"])
    N = z.shape[1]
    out = np.zeros((len(fold["test"]), N), np.float32)
    for g in range(N_GROUPS):
        gm = groups == g

        def X(idx):
            return np.concatenate([z[idx][:, ~gm], z[idx - 1]], 1)

        Y = A["z"][:, gm]
        mu, W, _ = _ridge_path(X(fold["train"]), Y[fold["train"]], X(fold["val"]), Y[fold["val"]])
        out[:, gm] = (X(fold["test"]) - mu) @ W
    return out
