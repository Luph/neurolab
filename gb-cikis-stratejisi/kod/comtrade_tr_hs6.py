# Faz 1 yardımcı betiği (ticaret veri ajanının gözden geçirilmiş betiği): Türkiye HS6 dış ticareti, UN Comtrade önizleme API.
"""UN Comtrade keyless public *preview* API -> Türkiye (reporter 792) annual HS6 trade.

What it downloads (per year):
  1. HS6 x {X,M} with partner World (0): all 5,613 H6 (HS2022) subheadings, paged by
     passing comma-separated lists of <=240 HS6 codes per call (240 codes x 2 flows < 500-record cap).
  2. TOTAL and AG2 (chapter) aggregates x {X,M} for validation.
  3. Bonus: HS2 chapter x 27 EU member states x {X,M} (Comtrade has no EU-27 partner aggregate),
     summed to an EU27 total.
Politeness: >=1.2 s between calls, exponential backoff on 429/5xx, chunks split automatically if a
response hits the 500-record cap.

Usage: python3 -I comtrade_tur_hs6.py OUTDIR [YEAR ...]   (default years: 2024 2025)
"""
import sys, os, json, time
import requests
import pandas as pd

BASE = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"
REF = "https://comtradeapi.un.org/files/v1/app/reference/"
CAP = 500
MIN_INTERVAL = 1.2
REPORTER = 792
EU27_ISO3 = ["AUT", "BEL", "BGR", "HRV", "CYP", "CZE", "DNK", "EST", "FIN", "FRA", "DEU", "GRC", "HUN",
             "IRL", "ITA", "LVA", "LTU", "LUX", "MLT", "NLD", "POL", "PRT", "ROU", "SVK", "SVN", "ESP", "SWE"]
KEEP = ["refYear", "period", "reporterCode", "flowCode", "partnerCode", "classificationCode", "cmdCode",
        "qtyUnitCode", "qty", "altQtyUnitCode", "altQty", "netWgt", "grossWgt", "cifvalue", "fobvalue",
        "primaryValue", "isReported", "isAggregate"]

S = requests.Session()
S.headers["User-Agent"] = "academic-trade-research/1.0 (polite: 1 req/s)"
_last = [0.0]
NCALLS = [0]


def get(url, params=None, tries=8):
    global MIN_INTERVAL
    for i in range(tries):
        wait = MIN_INTERVAL - (time.time() - _last[0])
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time()
        try:
            r = S.get(url, params=params, timeout=180)
            NCALLS[0] += 1
        except requests.RequestException as e:
            d = 3 * 2 ** i
            print(f"  network error {e!r}; retry in {d}s", flush=True)
            time.sleep(d)
            continue
        if r.status_code == 200:
            return r
        if r.status_code == 429 or r.status_code >= 500:
            ra = r.headers.get("Retry-After", "")
            d = max(float(ra) if ra.replace(".", "").isdigit() else 0, 3 * 2 ** i)
            if r.status_code == 429:  # adaptive politeness: slow down permanently
                MIN_INTERVAL = min(MIN_INTERVAL * 1.3 + 0.2, 8.0)
            print(f"  HTTP {r.status_code}; backoff {d}s; interval now {MIN_INTERVAL:.1f}s", flush=True)
            time.sleep(d)
            continue
        raise RuntimeError(f"HTTP {r.status_code} {r.url[:200]}: {r.text[:300]}")
    raise RuntimeError(f"giving up after {tries} tries: {url}")


def ref(name, outdir):
    p = os.path.join(outdir, f"ref_{name}.json")
    if not os.path.exists(p):
        open(p, "wb").write(get(REF + f"{name}.json").content)
    return json.load(open(p, encoding="utf-8-sig"))["results"]


def preview(period, cmds, partners="0", flows="X,M"):
    p = dict(reporterCode=REPORTER, period=period, partnerCode=partners, flowCode=flows,
             cmdCode=",".join(cmds))
    d = get(BASE, p).json()
    if d.get("error"):
        raise RuntimeError(d["error"])
    return d.get("data") or []


def fetch(period, cmds, partners="0", flows="X,M"):
    """Fetch, splitting the code list recursively if the 500-record cap is hit."""
    rows = preview(period, cmds, partners, flows)
    if len(rows) >= CAP:
        if len(cmds) == 1:
            raise RuntimeError(f"single code {cmds} still hits the cap")
        h = len(cmds) // 2
        return fetch(period, cmds[:h], partners, flows) + fetch(period, cmds[h:], partners, flows)
    return rows


def chunks(xs, n):
    return [xs[i:i + n] for i in range(0, len(xs), n)]


def main():
    outdir = sys.argv[1]
    eu_only = "--eu-only" in sys.argv  # re-run only the EU27 x HS2 part
    years = [int(y) for y in sys.argv[2:] if y.isdigit()] or [2024, 2025]
    os.makedirs(outdir, exist_ok=True)
    h6 = ref("H6", outdir)
    desc = {r["id"]: r["text"] for r in h6}
    hs6 = sorted(r["id"] for r in h6 if len(r["id"]) == 6 and r["id"].isdigit())
    hs2 = sorted(r["id"] for r in h6 if len(r["id"]) == 2 and r["id"].isdigit())
    parts = ref("partnerAreas", outdir)
    # all live (non-expired, non-group) codes of EU27 members; FRA has 251 'France' and 250 'Metropolitan France'
    eu = sorted(r["PartnerCode"] for r in parts if r.get("PartnerCodeIsoAlpha3") in EU27_ISO3
                and not r.get("isGroup") and not r.get("entryExpiredDate"))
    pname = {r["PartnerCode"]: r["text"] for r in parts}
    print(f"{len(hs6)} HS6 codes, {len(hs2)} chapters, EU27 codes ({len(eu)}) {eu}", flush=True)
    vpath = os.path.join(outdir, "comtrade_validation.csv")
    summary = [] if not (eu_only and os.path.exists(vpath)) else pd.read_csv(vpath).to_dict("records")
    for y in years:
        tot = pd.DataFrame(fetch(y, ["TOTAL"]))
        if tot.empty:
            print(f"{y}: no data (not yet available)", flush=True)
            continue
        if not eu_only:
            ag2 = pd.DataFrame(fetch(y, ["AG2"]))[KEEP]
            ag2["cmdDesc"] = ag2["cmdCode"].map(desc)
            ag2.to_csv(os.path.join(outdir, f"comtrade_tur_hs2_world_{y}.csv"), index=False)
            rows = []
            for i, c in enumerate(chunks(hs6, 240)):
                rows += fetch(y, c)
                print(f"{y}: chunk {i + 1}/{-(-len(hs6) // 240)} -> {len(rows)} rows (calls {NCALLS[0]})", flush=True)
            df = pd.DataFrame(rows)[KEEP]
            df["cmdDesc"] = df["cmdCode"].map(desc)
            df = df.sort_values(["flowCode", "cmdCode"])
            df.to_csv(os.path.join(outdir, f"comtrade_tur_hs6_world_{y}.csv.gz"), index=False)
            for fl in ("X", "M"):  # validation: HS6 sum vs TOTAL vs AG2
                t = float(tot.loc[tot.flowCode == fl, "primaryValue"].sum())
                s6 = float(df.loc[df.flowCode == fl, "primaryValue"].sum())
                s2 = float(ag2.loc[ag2.flowCode == fl, "primaryValue"].sum())
                summary.append(dict(year=y, flow=fl, total=t, sum_hs6=s6, sum_hs2=s2,
                                    n_hs6=int((df.flowCode == fl).sum()), hs6_cover=s6 / t if t else None))
            d6 = df.assign(ch=df.cmdCode.str[:2]).groupby(["flowCode", "ch"]).primaryValue.sum()
            d2 = ag2.set_index(["flowCode", "cmdCode"]).primaryValue
            idx = d2.index.union(d6.index)
            gap = d2.reindex(idx).fillna(0) - d6.reindex(idx).fillna(0)
            gap = gap[gap.abs() > 1e8].sort_values()
            print(f"{y}: AG2 minus sum(HS6) by chapter, |gap| > $100m (confidential trade booked in ch.99 at HS6):",
                  flush=True)
            print((gap / 1e9).round(2).to_string(), flush=True)
        # EU27 member states x HS2 chapter (8 chapters x 28 codes x 2 flows = 448 < 500)
        er = []
        for c in chunks(hs2, 8):
            er += fetch(y, c, partners=",".join(map(str, eu)))
        e = pd.DataFrame(er)[KEEP]
        e["partnerDesc"] = e["partnerCode"].map(pname)
        e["cmdDesc"] = e["cmdCode"].map(desc)
        e.to_csv(os.path.join(outdir, f"comtrade_tur_hs2_eu27members_{y}.csv"), index=False)
        es = e.groupby("flowCode").primaryValue.sum()
        print(f"{y}: EU27 rows {len(e)}, partners present {sorted(e.partnerCode.unique())}; "
              f"EU27 X {es.get('X', 0) / 1e9:.2f} bn, M {es.get('M', 0) / 1e9:.2f} bn", flush=True)
        for srow in summary:
            if srow["year"] == y:
                srow["eu27_hs2_sum"] = float(es.get(srow["flow"], 0))
    sm = pd.DataFrame(summary)
    sm.to_csv(vpath, index=False)
    pd.set_option("display.width", 200)
    print(sm.to_string(), flush=True)
    print(f"total API calls: {NCALLS[0]}", flush=True)


if __name__ == "__main__":
    main()
