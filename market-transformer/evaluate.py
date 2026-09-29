"""Out-of-sample evaluation, relationship discovery, and current mispricing screen.

Run after `run.py predict`, `run.py fair`, `run.py linear`.  Writes CSVs + PNGs to outputs/.
"""
import os
import pickle

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
from scipy.stats import spearmanr

from mt.data import cost_native
from mt.model import CrossAssetTransformer
from mt.train import N_GROUPS, _ridge_fit, _ridge_path, fair_batch, fixed_groups, folds

OUT = os.environ.get("MT_OUT", "outputs")
u, A = pickle.load(open(os.environ["MT_CACHE"], "rb"))
T, N = A["z"].shape
tick = np.array(u.tickers)
short = np.array([t.replace(" Index", "").replace(" Comdty", "").replace(" Curncy", "").replace(" US Equity", "")
                  .replace(" CDSI GEN 5Y Corp", "").replace(" CDSI GEN 5Y PRC Corp", " (px)").strip() for t in tick])
classes = sorted(set(u.cls))
cls_ids = np.array([classes.index(c) for c in u.cls])
groups = fixed_groups(N)
A["groups"] = groups
F = folds(u.dates)
dates = u.dates

BLUE, ORANGE, AQUA, GRAY, RED = "#2a78d6", "#eb6834", "#1baf7a", "#8a8984", "#e34948"
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": "#b5b4ae", "axes.grid": True, "grid.color": "#ecebe7",
                     "grid.linewidth": 0.6, "figure.facecolor": "#fcfcfb", "axes.facecolor": "#fcfcfb",
                     "lines.linewidth": 1.6})


def assemble(kind, key="pred"):
    out = np.full((T,) + ((N, 3) if kind == "predict" or (kind == "linear" and key == "pred") else (N,)), np.nan,
                  np.float32)
    for k in range(len(F)):
        d = np.load(f"{OUT}/{kind}_fold{k}.npz")
        out[d["idx"]] = d[key]
    return out


P_tf, P_lin = assemble("predict"), assemble("linear", "pred")
Fa_tf, Fa_lin = assemble("fair"), assemble("linear", "fair")
test = np.where(~np.isnan(Fa_tf).all(1))[0]
t0, t1 = test[0], test[-1]
z = A["z"]
sig = A["sig"]
avail = A["avail"]
cost_z = np.array([cost_native(t, c, k) for t, c, k in zip(tick, u.cls, u.kind)])[None] / sig  # cost in vol units
# P&L universe: tradable instruments whose typical one-way cost is below 0.25 daily sigma
med_cost = np.nanmedian(cost_z[dates.searchsorted(pd.Timestamp("2010-01-01")):], 0)
trad = u.tradable & ~np.array([("OAS" in t) or t == "SPBDAL Index" for t in tick]) & (med_cost < 0.25)

lines = []


def say(s=""):
    print(s)
    lines.append(s)


# ----------------------------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------------------------
def r2(y, p, m):
    ok = m & ~np.isnan(y) & ~np.isnan(p)
    return 1 - ((y - p) ** 2)[ok].sum() / (y ** 2)[ok].sum()


def daily_ic(sig_, y, m, step=1):
    ics = []
    for t in range(t0, t1 + 1, step):
        ok = m[t] & ~np.isnan(sig_[t]) & ~np.isnan(y[t])
        if ok.sum() > 20:
            ics.append(spearmanr(sig_[t, ok], y[t, ok])[0])
    ics = np.array(ics)
    return ics.mean(), ics.mean() / ics.std() * np.sqrt(len(ics))


def class_neutral_weights(s, m):
    """Within each class: demeaned cross-sectional rank; each class gets equal gross; total gross = 1."""
    W = np.zeros_like(s)
    for t in range(T):
        st = s[t]
        ok0 = m[t] & ~np.isnan(st)
        live = []
        for c in classes:
            ok = ok0 & (u.cls == c)
            if ok.sum() >= 4:
                r = pd.Series(st[ok]).rank().values
                r = r - r.mean()
                W[t, ok] = r / np.abs(r).sum()
                live.append(c)
        if live:
            W[t] /= len(live)
    return W


def backtest(W, lag):
    """W decided at close t; with lag=1 it earns the t+1 move (close-to-close, no execution delay),
    with lag=2 it is traded at the close of t+1 and earns the t+2 move.  Returns daily pnl series (vol units)."""
    zf = np.nan_to_num(np.clip(z, -6, 6))
    gross = np.zeros(T)
    tc = np.zeros(T)
    for t in range(t0, min(t1, T - 1 - lag) + 1):
        gross[t + lag] = (W[t] * zf[t + lag]).sum()
        tc[t + lag] = (np.abs(W[t] - W[t - 1]) * np.nan_to_num(cost_z[t])).sum()
    idx = dates[t0 + lag: min(t1, T - 1 - lag) + lag + 1]
    return pd.Series(gross[t0 + lag: min(t1, T - 1 - lag) + lag + 1], idx), pd.Series(tc[t0 + lag: min(t1, T - 1 - lag) + lag + 1], idx)


def stats(g, c):
    n = g - c
    sh = lambda x: x.mean() / x.std() * np.sqrt(252)
    return dict(sharpe_gross=sh(g), sharpe_net=sh(n), breakeven_cost_mult=g.sum() / max(c.sum(), 1e-9), ann_ret_net_volunits=n.mean() * 252,
                maxdd=(n.cumsum() - n.cumsum().cummax()).min(), cost_share=c.sum() / max(g.sum(), 1e-9))


def smooth(S, h):
    return pd.DataFrame(S).rolling(h, min_periods=1).mean().values


def ewm_w(W, hl):
    return pd.DataFrame(W).ewm(halflife=hl).mean().values


def turnover(W):
    return np.abs(np.diff(W[t0:t1], axis=0)).sum(1).mean()


mask_all = avail.copy()
mask_all[:t0] = False
mask_tr = mask_all & trad[None]

# ----------------------------------------------------------------------------------------------
# 1. Forward-return prediction
# ----------------------------------------------------------------------------------------------
say(f"OOS period: {dates[t0].date()} .. {dates[t1].date()}  ({t1 - t0 + 1} days, {N} series, {trad.sum()} tradable)")
say("\n## 1. Forward-return forecasts (walk-forward OOS)")
rows = []
for h, key in enumerate(("y1", "y2", "y5")):
    y = A[key]
    for name, P in (("transformer", P_tf), ("linear ridge", P_lin)):
        p = P[..., h]
        ic, ict = daily_ic(p, y, mask_tr, step=5 if key == "y5" else 1)
        rows.append(dict(target=key, model=name, oos_r2_pct=100 * r2(y, p, mask_all), ic=ic, ic_t=ict))
pred_tab = pd.DataFrame(rows)
say(pred_tab.round(4).to_string(index=False))

bt = {}
for name, P in (("transformer", P_tf), ("linear ridge", P_lin)):
    W1 = class_neutral_weights(P[..., 0], mask_tr)
    bt[(name, "t+1 close-to-close (NOT executable across time zones)")] = backtest(W1, 1)
    W2 = class_neutral_weights(P[..., 1], mask_tr)
    bt[(name, "t+2 one-day execution lag")] = backtest(W2, 2)
    W5 = ewm_w(class_neutral_weights(P[..., 2], mask_tr), 5)
    bt[(name, "5d horizon, 1-day lag, 5d smoothing")] = backtest(W5, 2)
    W20 = ewm_w(class_neutral_weights(P[..., 2], mask_tr), 20)
    bt[(name, "5d horizon, 1-day lag, slow (hl=20d)")] = backtest(W20, 2)
    if name == "transformer":
        W_pred_last = W5[t1]
rows = [dict(model=k[0], strategy=k[1], **stats(*v)) for k, v in bt.items()]
bt_tab = pd.DataFrame(rows)
say("\nClass-neutral long/short on tradable assets (P&L in vol-units, costs = rough per-asset bid/ask):")
say(bt_tab.round(3).to_string(index=False))

# ----------------------------------------------------------------------------------------------
# 2. Fair-value model and mispricing reversion
# ----------------------------------------------------------------------------------------------
say("\n## 2. Cross-asset fair-value (masked) model")
r2_tf = np.array([r2(z[:, i], Fa_tf[:, i], mask_all[:, i]) for i in range(N)])
r2_lin = np.array([r2(z[:, i], Fa_lin[:, i], mask_all[:, i]) for i in range(N)])
say(f"Same-day move explained OOS: transformer pooled R2 = {100 * r2(z, Fa_tf, mask_all):.1f}%  | "
    f"linear ridge = {100 * r2(z, Fa_lin, mask_all):.1f}%")
say(f"Transformer beats linear on {np.mean(r2_tf > r2_lin) * 100:.0f}% of series; median gain "
    f"{100 * np.median(r2_tf - r2_lin):.1f} pts")
fv = pd.DataFrame(dict(ticker=tick, cls=u.cls, r2_transformer=r2_tf, r2_linear=r2_lin, gain=r2_tf - r2_lin))
fv.to_csv(f"{OUT}/fair_value_r2_by_asset.csv", index=False)
cls_gain = fv.groupby("cls")[["r2_transformer", "r2_linear", "gain"]].median().sort_values("gain", ascending=False)
say("\nMedian OOS R2 by asset class:")
say((100 * cls_gain).round(1).to_string())
say("\nLargest non-linear gains (R2 points):")
say((fv.sort_values("gain", ascending=False).head(15).assign(
    r2_transformer=lambda d: 100 * d.r2_transformer, r2_linear=lambda d: 100 * d.r2_linear,
    gain=lambda d: 100 * d.gain)).round(1).to_string(index=False))


def resid_signal(Fa, hl=5):
    e = z - Fa
    e[~mask_all] = np.nan
    s = pd.DataFrame(e).rolling(hl, min_periods=hl).sum()
    scale = pd.DataFrame(e).rolling(250, min_periods=60).std().shift(1) * np.sqrt(hl)
    return e, (s / scale).values


rev_rows = []
sig_store = {}
for name, Fa in (("transformer", Fa_tf), ("linear ridge", Fa_lin)):
    e, S = resid_signal(Fa)
    sig_store[name] = (e, S)
    fwd_e = pd.DataFrame(e).rolling(5).sum().shift(-6).values  # residual over t+2..t+6
    ic_r, ict_r = daily_ic(-S, fwd_e, mask_tr, step=5)
    ic_p, ict_p = daily_ic(-S, A["y5"], mask_tr, step=5)
    W = class_neutral_weights(-S, mask_tr)
    g, c = backtest(W, 2)
    Wsm = ewm_w(W, 5)
    g2, c2 = backtest(Wsm, 2)
    bt[(name, "mispricing reversion, 1-day lag, hl=5d")] = (g2, c2)
    bt[(name, "mispricing reversion, 1-day lag")] = (g, c)
    rev_rows.append(dict(model=name, ic_vs_future_residual=ic_r, t1=ict_r, ic_vs_future_return=ic_p, t2=ict_p,
                         **{k + "_lag1": v for k, v in stats(g, c).items() if k.startswith("sharpe")},
                         **{k + "_lag1_smoothed": v for k, v in stats(g2, c2).items() if k.startswith("sharpe")}))
    if name == "transformer":
        W_rev_last = W[t1]
rev_tab = pd.DataFrame(rev_rows)
say("\nDo residuals (actual - fair) mean-revert?  Signal = -(5d cumulated residual z-score).")
say(rev_tab.round(3).to_string(index=False))

# reversion IC by class (transformer)
e, S = sig_store["transformer"]
fwd_e = pd.DataFrame(e).rolling(5).sum().shift(-6).values
cls_rev = {}
for c in classes:
    m = mask_tr & (u.cls == c)[None]
    if m[t0:].sum() > 5000:
        cls_rev[c] = daily_ic(-S, A["y5"], m, step=5)
say("\nReversion IC vs next-week return, by class (transformer residuals):")
say(pd.DataFrame(cls_rev, index=["ic", "t"]).T.sort_values("ic", ascending=False).round(3).to_string())

# per-asset reversion hit rate (OOS)
per_asset = []
for i in range(N):
    ok = mask_all[:, i] & ~np.isnan(S[:, i]) & ~np.isnan(A["y5"][:, i])
    ok[::1] &= (np.arange(T) % 5 == 0)
    if ok.sum() > 100:
        c_ = np.corrcoef(-S[ok, i], A["y5"][ok, i])[0, 1]
        big = ok & (np.abs(np.nan_to_num(S[:, i])) > 2)
        hit = np.mean(np.sign(-S[big, i]) == np.sign(A["y5"][big, i])) if big.sum() > 10 else np.nan
        per_asset.append((tick[i], c_, hit, big.sum()))
pa = pd.DataFrame(per_asset, columns=["ticker", "rev_corr", "hit_rate_when_|z|>2", "n_signals"]).set_index("ticker")

# ----------------------------------------------------------------------------------------------
# 3. Charts: cumulative P&L
# ----------------------------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(11, 3.8), sharey=False)
for ax, strat, title in ((axes[0], "5d horizon, 1-day lag, 5d smoothing", "Forward-return model (5d, executed with 1-day lag)"),
                         (axes[1], "mispricing reversion, 1-day lag", "Fair-value residual reversion (1-day lag)")):
    for name, col in (("transformer", BLUE), ("linear ridge", ORANGE)):
        g, c = bt[(name, strat)]
        n = (g - c).cumsum()
        ax.plot(n.index, n.values, color=col, label=f"{name}  (net SR {stats(g, c)['sharpe_net']:.2f})")
    ax.axhline(0, color=GRAY, lw=0.8)
    ax.set_title(title, loc="left", fontsize=10)
    ax.set_ylabel("cumulative P&L, vol-units (net of costs)")
    ax.legend(frameon=False, loc="upper left")
fig.tight_layout()
fig.savefig(f"{OUT}/pnl.png", dpi=140)

fig, ax = plt.subplots(figsize=(7, 3.4))
cg = cls_gain.sort_values("gain")
ax.barh(cg.index, 100 * cg["r2_linear"], color=ORANGE, height=0.38, align="edge", label="linear ridge")
ax.barh(cg.index, 100 * cg["r2_transformer"], color=BLUE, height=-0.38, align="edge", label="transformer")
ax.set_xlabel("median OOS R² of same-day move, %")
ax.set_title("How much of each asset's daily move is explained by all the others", loc="left", fontsize=10)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(f"{OUT}/fair_value_r2.png", dpi=140)

# ----------------------------------------------------------------------------------------------
# 4. Non-linear relationship discovery with the latest fair-value model (2022-2026 OOS days)
# ----------------------------------------------------------------------------------------------
say("\n## 3. Non-linear relationships (latest model, perturbation analysis on its OOS days)")
lastk = len(F) - 1
model = CrossAssetTransformer(N, len(classes), A["feat"].shape[2] + 3, 1)
model.load_state_dict(torch.load(f"{OUT}/fair_fold{lastk}_seed0.pt"))
model.eval()
b = np.load(f"{OUT}/base_fold{lastk}.npz")
A["base_fair"] = b["bf"]
aid, cid = torch.arange(N), torch.as_tensor(cls_ids)
rng = np.random.default_rng(0)
days = np.sort(rng.choice(F[lastk]["test"], 60, replace=False))
torch.set_num_threads(4)

# linear part of the hybrid for the last fold (same fit that produced its test-period base)
zz = np.nan_to_num(z)
LW = {}
fl = F[lastk]
for g in range(N_GROUPS):
    gm = groups == g
    Xf = lambda idx, gm=gm: np.concatenate([zz[idx][:, ~gm], zz[idx - 1]], 1)
    _, _, a = _ridge_path(Xf(fl["train"]), z[fl["train"]][:, gm], Xf(fl["val"]), z[fl["val"]][:, gm])
    I = np.concatenate([fl["train"], fl["val"]])
    LW[g] = _ridge_fit(Xf(I), z[I][:, gm], a)[1]   # (n_visible + N, n_group)


@torch.no_grad()
def fair_with(idx, g, j=None, v=0.0, nonlinear_only=False):
    """Hybrid fair move of the hidden group g, optionally forcing driver j's same-day move to v (sigma)."""
    gm = groups == g
    m = np.broadcast_to(gm, (len(idx), N))
    x, _, pad = fair_batch(A, idx, m)
    base = x[:, :, -1].copy()
    if j is not None:
        col = np.searchsorted(np.where(~gm)[0], j)
        dz = v - x[:, j, -3]
        base[:, gm] += dz[:, None] * LW[g][col][None]
        x[:, j, -3] = v
        x[:, j, -2] = 1.0
        x[:, :, -1] = base
    corr = model(torch.from_numpy(x), aid, cid, torch.from_numpy(pad)).numpy()[..., 0]
    return corr if nonlinear_only else corr + base


# slope (+-1 sigma) and convexity of every hidden target to every visible driver
slope = np.zeros((N, N))       # [driver j, target i]
convex = np.zeros((N, N))
state_sd = np.zeros((N, N))
nl_slope = np.zeros((N, N))
base = {g: fair_with(days, g) for g in range(N_GROUPS)}
for j in range(N):
    for g in range(N_GROUPS):
        if groups[j] == g:
            continue
        tg = groups == g
        up = fair_with(days, g, j, 1.5)
        dn = fair_with(days, g, j, -1.5)
        ok = avail[days][:, j]
        if ok.sum() < 30:
            continue
        s_ = (up - dn)[ok][:, tg] / 3.0
        # non-linear share: the transformer correction's own slope
        up_n = fair_with(days, g, j, 1.5, True)
        dn_n = fair_with(days, g, j, -1.5, True)
        nl_slope[j, tg] = ((up_n - dn_n)[ok][:, tg] / 3.0).mean(0)
        slope[j, tg] = s_.mean(0)
        state_sd[j, tg] = s_.std(0)
        convex[j, tg] = ((up + dn - 2 * base[g]) / 2)[ok][:, tg].mean(0) / 1.5 ** 2

rows = []
for j in range(N):
    for i in range(N):
        if i == j or groups[i] == groups[j] or slope[j, i] == 0:
            continue
        rows.append((short[j], u.cls[j], short[i], u.cls[i], slope[j, i], nl_slope[j, i], state_sd[j, i], convex[j, i]))
rel = pd.DataFrame(rows, columns=["driver", "driver_cls", "target", "target_cls", "slope", "nonlinear_part", "slope_sd_across_days", "convexity"])
rel["abs_slope"] = rel.slope.abs()
rel["state_dependence"] = rel.slope_sd_across_days / (rel.abs_slope + 0.02)
rel.to_csv(f"{OUT}/relationships_all.csv", index=False)
cross = rel[rel.driver_cls != rel.target_cls]
say("\nStrongest cross-asset-class links (d fair move / d driver move, both in vol units):")
say(cross.sort_values("abs_slope", ascending=False).head(20)[["driver", "target", "slope", "nonlinear_part", "slope_sd_across_days", "convexity"]].round(3).to_string(index=False))
strong = cross[cross.abs_slope > 0.05]
say("\nMost regime-dependent cross-class links (sensitivity varies most across days, |slope|>0.05):")
say(strong.sort_values("slope_sd_across_days", ascending=False).head(15)[["driver", "target", "slope", "nonlinear_part", "slope_sd_across_days", "convexity"]].round(3).to_string(index=False))
say("\nMost asymmetric / convex cross-class links (response to a 1.5σ up vs down move differs):")
say(strong.assign(ac=strong.convexity.abs()).sort_values("ac", ascending=False).head(15)[["driver", "target", "slope", "convexity"]].round(3).to_string(index=False))

# response curves for a few interpretable pairs
pairs = [("SPX Index", "USGG10YR Index"), ("USDJPY Curncy", "USGG10YR Index"), ("AUDJPY Curncy", "SPX Index"),
         ("XLE US Equity", "CL1 Comdty"), ("GC1 Comdty", "USGGT10Y Index"), ("CDX HY CDSI GEN 5Y PRC Corp", "SPX Index"),
         ("UX1 Index", "SPX Index"), ("USDMXN Curncy", "SPX Index"), ("KRE US Equity", "USGG2YR Index")]
grid = np.linspace(-3, 3, 13)
fig, axes = plt.subplots(3, 3, figsize=(10.5, 8.2))
tix = list(tick)
say("\nResponse curves (target fair move vs driver move, others as observed); linear-ridge slope for reference:")
for ax, (tgt, drv) in zip(axes.flat, pairs):
    i, j = tix.index(tgt), tix.index(drv)
    g = groups[i]
    if groups[j] == g:
        ax.set_visible(False)
        continue
    ok = days[avail[days, j] & avail[days, i]]
    curves = np.stack([fair_with(ok, g, j, v)[:, i] for v in grid])  # (grid, days)
    # split days by stress regime: driver-independent state = VIX 1y z-score
    vz = A["feat"][ok, tix.index("VIX Index"), -2]
    hi = vz > np.median(vz)
    mean = curves.mean(1)
    ax.plot(grid, curves[:, hi].mean(1) - mean[6], color=RED, label="high-VIX days")
    ax.plot(grid, curves[:, ~hi].mean(1) - mean[6], color=BLUE, label="low-VIX days")
    # linear reference: OLS beta on test-period data
    m_ = mask_all[:, i] & mask_all[:, j] & (np.arange(T) >= F[lastk]["test"][0])
    b = np.polyfit(z[m_, j], z[m_, i], 1)[0]
    ax.plot(grid, b * grid, color=GRAY, lw=1, ls="--", label="linear OLS")
    ax.set_title(f"{short[i]}  vs  {short[j]}", loc="left", fontsize=9)
    ax.axhline(0, color="#d8d7d2", lw=0.6)
    ax.axvline(0, color="#d8d7d2", lw=0.6)
    say(f"  {short[i]:>12} <- {short[j]:<12} slope lowVIX {np.polyfit(grid, curves[:, ~hi].mean(1), 1)[0]:+.3f} "
        f"highVIX {np.polyfit(grid, curves[:, hi].mean(1), 1)[0]:+.3f}  OLS {b:+.3f}")
axes[0, 0].legend(frameon=False, fontsize=7)
for ax in axes[-1]:
    ax.set_xlabel("driver same-day move (σ)")
for ax in axes[:, 0]:
    ax.set_ylabel("fair move of target (σ)")
fig.suptitle("Transformer response curves, split by volatility regime (2022–2026 OOS days)", x=0.01, ha="left", fontsize=10)
fig.tight_layout()
fig.savefig(f"{OUT}/response_curves.png", dpi=140)

# ----------------------------------------------------------------------------------------------
# 5. Current mispricing screen (as of last date)
# ----------------------------------------------------------------------------------------------
say(f"\n## 4. Current mispricing screen as of {dates[t1].date()}")
e, S = sig_store["transformer"]
last = t1
act5 = pd.DataFrame(np.where(avail, z, np.nan)).rolling(5).sum().values[last]
fair5 = pd.DataFrame(Fa_tf).rolling(5).sum().values[last]
lvl = A["feat"][last, :, -2]
scr = pd.DataFrame(dict(ticker=tick, cls=u.cls, transform=u.kind, tradable=trad, resid_z=S[last],
                        actual_5d_sigma=act5, fair_5d_sigma=fair5, level_z_1y=lvl,
                        fwd5d_forecast=P_tf[last, :, 2], lin_resid_z=sig_store["linear ridge"][1][last]))
scr = scr.join(pa, on="ticker")
scr["view"] = np.where(scr.resid_z > 0, "rich vs cross-asset fair value -> expect underperformance",
                       "cheap vs cross-asset fair value -> expect outperformance")
scr = scr[scr.tradable & scr.resid_z.notna()].copy()
scr["abs_z"] = scr.resid_z.abs()
scr = scr.sort_values("abs_z", ascending=False)
scr.drop(columns="abs_z").to_csv(f"{OUT}/mispricing_screen_latest.csv", index=False)
cols = ["ticker", "cls", "resid_z", "actual_5d_sigma", "fair_5d_sigma", "lin_resid_z", "fwd5d_forecast", "rev_corr", "hit_rate_when_|z|>2"]
say(scr[cols].head(25).round(2).to_string(index=False))

pd.concat([pred_tab]).to_csv(f"{OUT}/forecast_metrics.csv", index=False)
pd.DataFrame([dict(model=k[0], strategy=k[1], **stats(*v)) for k, v in bt.items()]).to_csv(f"{OUT}/backtests.csv", index=False)
rev_tab.to_csv(f"{OUT}/reversion_metrics.csv", index=False)
pa.to_csv(f"{OUT}/reversion_by_asset.csv")
# monthly net pnl of the reversion strategy by year
g, c = bt[("transformer", "mispricing reversion, 1-day lag")]
say("\nTransformer residual-reversion strategy, net Sharpe by calendar year:")
yr = (g - c).groupby((g - c).index.year).apply(lambda x: x.mean() / x.std() * np.sqrt(252))
say(yr.round(2).to_string())
g, c = bt[("transformer", "5d horizon, 1-day lag, 5d smoothing")]
say("\nTransformer 5d forecast strategy, net Sharpe by calendar year:")
say((g - c).groupby((g - c).index.year).apply(lambda x: x.mean() / x.std() * np.sqrt(252)).round(2).to_string())
open(f"{OUT}/summary.txt", "w").write("\n".join(lines))
