"""Load the Bloomberg sheet, classify each series, and build model tensors.

Transform rule (per the brief):
  * yields, rates, spreads, OAS, and other level series that can go negative -> first differences
  * everything else (prices, FX, indices, vol levels)                        -> log returns
"""
from __future__ import annotations

import re
from dataclasses import dataclass

import numpy as np
import pandas as pd

# ----------------------------------------------------------------------------------------------
# Classification
# ----------------------------------------------------------------------------------------------
YIELD_PREFIXES = (
    "USGG", "H15T", "GDBR", "GBTP", "GFRN", "GSPG", "GUKG", "GJGB", "GACGB", "GCAN", "GSWISS",
    "GCNY", "GIND", "GEBR", "GMXN", "GSAB", "BVMB", "FWIS", "USSWIT", "MTGEFNCL",
)
RATE_TICKERS = {"FEDL01 Index", "IRRBIOER Index"}
# STIR futures are quoted 100 - rate: economically a rate, so they are differenced like one.
STIR_FUTURES = {"FF3 Comdty", "FF6 Comdty", "FF12 Comdty", "ER4 Comdty"}
SPREAD_TICKERS = {
    "CDX IG CDSI GEN 5Y Corp", "ITRX EUR CDSI GEN 5Y Corp", "ITRX XOVER CDSI GEN 5Y Corp",
    "SNRFIN CDSI GEN 5Y Corp", "SUBFIN CDSI GEN 5Y Corp", "JPEIDISP Index",
    "USDJPY25R1M Curncy",  # risk reversal (vol spread)
    "SAR12M Curncy",       # forward points
}
LEVEL_DIFF_TICKERS = {"CESIUSD Index", "CESIEUR Index", "CESICNY Index", "CESIJPY Index", "BFCIUS Index"}

# Series used as model inputs only: not directly tradable, so excluded from P&L tests.
NON_TRADABLE = {
    "FEDL01 Index", "IRRBIOER Index", "MOVE Index", "VIX Index", "VVIX Index", "V2X Index",
    "VXN Index", "RVX Index", "OVX Index", "GVZ Index", "SKEW Index", "JPMVXYGL Index",
    "JPMVXYEM Index", "BENCH Index", "SAR12M Curncy", "BDIY Index", "BIDY Index", "BITY Index",
    "CESIUSD Index", "CESIEUR Index", "CESICNY Index", "CESIJPY Index", "BFCIUS Index",
    "MTGEFNCL Index", "FXJPEMCI Index", "H15T20Y Index", "LMCADY Comdty", "LMAHDY Comdty",
    "LMNIDY Comdty", "LMZSDY Comdty", "LMSNDY Comdty", "LMPBDY Comdty", "JPEIDISP Index",
}


def is_oas(t: str) -> bool:
    return "OAS" in t and t.endswith("Index")


def transform_kind(t: str) -> str:
    if t.startswith(YIELD_PREFIXES) or t in RATE_TICKERS:
        return "diff"
    if t in STIR_FUTURES or t in SPREAD_TICKERS or t in LEVEL_DIFF_TICKERS or is_oas(t):
        return "diff"
    return "log"


def asset_class(t: str) -> str:
    if t.startswith(("USGGT", "USGGBE", "FWIS", "USSWIT", "GUKGIN")) or t == "TIP US Equity":
        return "inflation"
    if t.startswith(YIELD_PREFIXES) or t in RATE_TICKERS or t in STIR_FUTURES or t == "BVMB10Y Index":
        return "rates"
    if "CDSI" in t or is_oas(t) or t in {"JPEIDISP Index", "SPBDAL Index", "BKLN US Equity", "LQD US Equity",
                                          "HYG US Equity", "EMB US Equity", "MUB US Equity", "MBB US Equity",
                                          "CWB US Equity", "ARCC US Equity", "MAIN US Equity", "HTGC US Equity",
                                          "PSEC US Equity"}:
        return "credit"
    if t in {"MOVE Index", "VIX Index", "UX1 Index", "UX2 Index", "VVIX Index", "V2X Index", "VXN Index",
             "RVX Index", "OVX Index", "GVZ Index", "SKEW Index", "EURUSDV1M Curncy", "USDJPYV1M Curncy",
             "JPMVXYGL Index", "JPMVXYEM Index", "USDJPY25R1M Curncy"}:
        return "vol"
    if t.endswith("Curncy") or t in {"BBDXY Index", "FXJPEMCI Index", "FXCTG10 Index", "FXCTEM8 Index"}:
        return "crypto" if t.startswith("XBT") else "fx"
    if t.startswith(("CESI", "BFCI")) or t == "BENCH Index":
        return "macro"
    if re.match(r"^(CL|CO|NG|XB|HO|QS|MO)\d", t) or t.startswith(("TTFG", "JGL", "XW", "BCOMEN")) or t in {
            "URA US Equity", "CCJ US Equity", "XOP US Equity"}:
        return "energy"
    if re.match(r"^(GC|SI|PL|PA|HG|SCO|RBT)\d", t) or t.startswith("LM") or t in {
            "LIT US Equity", "REMX US Equity", "ALB US Equity", "SQM US Equity", "BCOMIN Index", "BCOMPR Index"}:
        return "metals"
    if re.match(r"^(C |S |W |KW|BO|SM|KO|RS|SB|KC|DF|CC|QC|CT|LC|FC|LH)\s?\d", t) or t == "BCOMAG Index":
        return "ags"
    if t in {"BDIY Index", "BIDY Index", "BITY Index", "MAERSKB DC Equity", "1919 HK Equity", "2603 TT Equity"}:
        return "shipping"
    if t in {"BCOM Index", "SPGSCI Index"}:
        return "commodity_idx"
    return "equity"


# Rough one-way transaction cost, in the series' own units (log-return units for prices,
# yield/spread points for differenced series).  Deliberately conservative-ish round numbers.
def cost_native(t: str, cls: str, kind: str) -> float:
    if kind == "diff":
        if cls == "credit":                  # CDS spread in bp, OAS in % points
            return 0.25 if "CDSI" in t else 0.005
        if t in STIR_FUTURES:
            return 0.005
        if t.startswith(("USGG", "H15T")):
            return 0.0025                    # 0.25bp in % yield
        if t.startswith(("GEBR", "GMXN", "GSAB", "GIND", "GCNY", "BVMB")):
            return 0.02
        if t == "USDJPY25R1M Curncy":
            return 0.1
        return 0.005
    if cls == "fx":
        em = any(c in t for c in ("MXN", "BRL", "ZAR", "TRY", "COP", "CLP", "IDR", "INR", "KRW", "TWD",
                                  "PLN", "HUF", "CZK", "CNH", "CNY"))
        return 0.0005 if em else 0.0001
    if cls == "vol":
        return 0.005
    if cls == "crypto":
        return 0.001
    if t.endswith("Index") and cls == "equity":
        return 0.0001                        # index futures
    return 0.0004 if t.endswith("Comdty") else 0.0005


@dataclass
class Universe:
    dates: pd.DatetimeIndex
    tickers: list
    kind: np.ndarray        # "log" / "diff"
    cls: np.ndarray
    tradable: np.ndarray
    levels: pd.DataFrame
    ret: pd.DataFrame       # raw log returns / first differences


def load(path: str) -> Universe:
    raw = pd.read_excel(path, header=None)
    tickers = [str(x).strip() for x in raw.iloc[6, 1:].tolist()]
    body = raw.iloc[9:].copy()
    body.index = pd.to_datetime(body.iloc[:, 0])
    body = body.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")
    body.columns = tickers
    body = body.sort_index()
    body = body[~body.index.duplicated(keep="last")]
    # carry prices over holidays but never before a series starts
    levels = body.ffill(limit=10)

    kind = np.array([transform_kind(t) for t in tickers])
    cls = np.array([asset_class(t) for t in tickers])
    ret = pd.DataFrame(index=levels.index, columns=tickers, dtype=float)
    for j, t in enumerate(tickers):
        x = levels[t]
        if kind[j] == "log":
            lx = np.log(x.where(x > 0))      # CL1 went negative in Apr-2020: those days are masked
            ret[t] = lx.diff()
        else:
            ret[t] = x.diff()
    tradable = np.array([t not in NON_TRADABLE for t in tickers])
    return Universe(levels.index, tickers, kind, cls, tradable, levels, ret)


# ----------------------------------------------------------------------------------------------
# Features
# ----------------------------------------------------------------------------------------------
N_LAGS = 20
FEATURE_NAMES = [f"r_lag{k}" for k in range(N_LAGS)] + ["cum60", "cum120", "cum250", "volratio", "level_z", "present"]


def build_arrays(u: Universe, clip: float = 6.0):
    """Returns dict of float32 arrays.

    z[t, i]      = ret[t, i] / sigma[t-1, i]  (vol-normalised using only information before t)
    sigma[t, i]  = EWMA vol (halflife 40d) through t
    feat[t,i,:]  = history features known at close of t
    y1, y2, y5   = forward targets normalised by sigma[t]:  r[t+1], r[t+2], sum r[t+2..t+6] / sqrt5
    """
    R = u.ret.values.astype(np.float64)
    T, N = R.shape
    present = ~np.isnan(R)
    # EWMA variance
    lam = 0.5 ** (1 / 40)
    var = np.full((T, N), np.nan)
    v = np.full(N, np.nan)
    cnt = np.zeros(N)
    for t in range(T):
        r = R[t]
        ok = ~np.isnan(r)
        init = ok & np.isnan(v)
        v[init] = r[init] ** 2
        upd = ok & ~init
        v[upd] = lam * v[upd] + (1 - lam) * r[upd] ** 2
        cnt[ok] += 1
        var[t] = np.where(cnt >= 40, v, np.nan)
    sig = np.sqrt(var)
    # floor: 10% of the series' median vol, avoids blow-ups on stale/pegged series (HKD, CNY...)
    med = np.nanmedian(sig, axis=0)
    sig = np.maximum(sig, 0.1 * med)
    sig_lag = np.vstack([np.full((1, N), np.nan), sig[:-1]])
    z = np.clip(R / sig_lag, -clip, clip)
    zf = np.nan_to_num(z)

    feat = np.zeros((T, N, len(FEATURE_NAMES)), dtype=np.float32)
    for k in range(N_LAGS):
        feat[k:, :, k] = zf[: T - k]
    cs = np.cumsum(zf, axis=0)
    for c, w in zip(range(N_LAGS, N_LAGS + 3), (60, 120, 250)):
        s = cs.copy()
        s[w:] -= cs[:-w]
        feat[:, :, c] = np.clip(s / np.sqrt(w), -clip, clip)
    # vol regime
    long_sig = pd.DataFrame(sig).rolling(250, min_periods=120).mean().values
    feat[:, :, N_LAGS + 3] = np.nan_to_num(np.clip(np.log(sig / long_sig), -3, 3))
    # level z-score vs 1y: log level for prices, raw level for yields/spreads
    L = u.levels.values.astype(np.float64).copy()
    for j in range(N):
        if u.kind[j] == "log":
            L[:, j] = np.log(np.where(L[:, j] > 0, L[:, j], np.nan))
    Ld = pd.DataFrame(L)
    m = Ld.rolling(250, min_periods=120).mean().values
    s = Ld.rolling(250, min_periods=120).std().values
    feat[:, :, N_LAGS + 4] = np.nan_to_num(np.clip((L - m) / s, -4, 4))
    avail = ~np.isnan(sig_lag) & present
    feat[:, :, N_LAGS + 5] = avail

    def fwd(k0, k1):
        acc = np.zeros((T, N))
        ok = np.ones((T, N), bool)
        for k in range(k0, k1 + 1):
            sh = np.full((T, N), np.nan)
            sh[: T - k] = R[k:]
            ok &= ~np.isnan(sh)
            acc += np.nan_to_num(sh)
        out = acc / sig / np.sqrt(k1 - k0 + 1)
        out[~ok] = np.nan
        return np.clip(out, -clip, clip)

    y1, y2, y5 = fwd(1, 1), fwd(2, 2), fwd(2, 6)
    avail_now = ~np.isnan(sig) & present
    for y in (y1, y2, y5):
        y[~avail_now] = np.nan
    z[~avail] = np.nan
    return dict(z=z.astype(np.float32), sig=sig.astype(np.float32), feat=feat,
                y1=y1.astype(np.float32), y2=y2.astype(np.float32), y5=y5.astype(np.float32),
                avail=avail)
