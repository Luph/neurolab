"""Lower-turnover implementations of the fair-value residual reversion signal (post-hoc check)."""
import os
import pickle

import numpy as np
import pandas as pd

from mt.data import cost_native
from mt.train import folds

OUT = os.environ.get("MT_OUT", "outputs")
u, A = pickle.load(open(os.environ["MT_CACHE"], "rb"))
T, N = A["z"].shape
F = folds(u.dates)
tick = np.array(u.tickers)


def assemble(kind, key):
    out = np.full((T, N), np.nan, np.float32)
    for k in range(len(F)):
        d = np.load(f"{OUT}/{kind}_fold{k}.npz")
        out[d["idx"]] = d[key]
    return out


z, sig, avail = A["z"], A["sig"], A["avail"]
cost_z = np.array([cost_native(t, c, k) for t, c, k in zip(tick, u.cls, u.kind)])[None] / sig
t0 = F[0]["test"][0]
t1 = T - 1
med_cost = np.nanmedian(cost_z[t0:], 0)
trad = u.tradable & ~np.array([("OAS" in t) or t == "SPBDAL Index" for t in tick]) & (med_cost < 0.25)
m = avail.copy()
m[:t0] = False
m &= trad[None]
zf = np.nan_to_num(np.clip(z, -6, 6))
cz = np.nan_to_num(cost_z)


def resid_S(Fa, hl=5):
    e = z - Fa
    e[~avail] = np.nan
    s = pd.DataFrame(e).rolling(hl, min_periods=hl).sum()
    sc = pd.DataFrame(e).rolling(250, min_periods=60).std().shift(1) * np.sqrt(hl)
    return (s / sc).values


def run(S, thr, hold, classes=None):
    """Enter against residuals with |z|>thr, equal risk per position, hold `hold` days; trade at close t+1."""
    mm = m if classes is None else m & np.isin(u.cls, classes)[None]
    sig_ = np.where(mm & (np.abs(np.nan_to_num(S)) > thr), -np.sign(np.nan_to_num(S)), 0.0)
    pos = pd.DataFrame(sig_).rolling(hold, min_periods=1).sum().values / hold
    gross_n = np.abs(pos).sum(1, keepdims=True)
    W = np.where(gross_n > 0, pos / np.maximum(gross_n, 1), 0)  # cap gross at 1
    g = np.zeros(T)
    c = np.zeros(T)
    for t in range(t0, t1 - 2):
        g[t + 2] = (W[t] * zf[t + 2]).sum()
        c[t + 2] = (np.abs(W[t] - W[t - 1]) * cz[t]).sum()
    g, c = g[t0 + 2:t1], c[t0 + 2:t1]
    sh = lambda x: x.mean() / x.std() * np.sqrt(252)
    run.last = (pd.Series(g, u.dates[t0 + 2:t1]), pd.Series(c, u.dates[t0 + 2:t1]))
    return sh(g), sh(g - c), np.abs(np.diff(W[t0:t1], axis=0)).sum(1).mean()


rows = []
curves = {}
for name, key in (("transformer hybrid", "fair"), ("linear ridge", "linear")):
    Fa = assemble(key, "pred" if key == "fair" else "fair")
    S = resid_S(Fa)
    for thr in (2.0, 3.0):
        for hold in (5, 10):
            for cl_name, cl in (("all", None), ("rates+ags+energy+metals", ["rates", "ags", "energy", "metals"])):
                gs, ns, to = run(S, thr, hold, cl)
                if thr == 3.0 and hold == 5 and cl is None:
                    curves[name] = run.last
                rows.append(dict(model=name, threshold=thr, hold_days=hold, universe=cl_name,
                                 sharpe_gross=gs, sharpe_net=ns, daily_turnover=to))
df = pd.DataFrame(rows)
print(df.round(3).to_string(index=False))
df.to_csv(f"{OUT}/reversion_low_turnover.csv", index=False)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True,
                     "grid.color": "#ecebe7", "figure.facecolor": "#fcfcfb", "axes.facecolor": "#fcfcfb"})
fig, ax = plt.subplots(figsize=(7.5, 3.6))
for (name, (g, c)), col in zip(curves.items(), ("#2a78d6", "#eb6834")):
    sh = lambda x: x.mean() / x.std() * np.sqrt(252)
    ax.plot(g.cumsum(), color=col, lw=1.6, label=f"{name}: gross (SR {sh(g):.2f})")
    ax.plot((g - c).cumsum(), color=col, lw=1.2, ls="--", label=f"{name}: net of costs (SR {sh(g - c):.2f})")
ax.axhline(0, color="#8a8984", lw=0.8)
ax.set_ylabel("cumulative P&L, vol-units")
ax.set_title("Fade |residual z| > 3 vs cross-asset fair value, hold 5d, 1-day execution lag (OOS 2010-2026)",
             loc="left", fontsize=9.5)
ax.legend(frameon=False, fontsize=8)
fig.tight_layout()
fig.savefig(f"{OUT}/reversion_pnl.png", dpi=140)
