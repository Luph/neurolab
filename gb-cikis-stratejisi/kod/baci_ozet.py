# Faz 1 yardımcı betiği (ticaret veri ajanının gözden geçirilmiş betiği): CEPII BACI zip dosyasından parquet alt kümeleri.
"""CEPII BACI (HS17, V202601) -> compact subsets for the Türkiye-EU Customs Union study.

Download (reproducible):
  curl -L -C - -o BACI_HS17_V202601.zip https://www.cepii.fr/DATA_DOWNLOAD/baci/data/BACI_HS17_V202601.zip
Then:
  python3 -I baci_extract.py ZIP OUTDIR [--years 2020-2024] [--delete-zip]

Outputs (OUTDIR):
  all_countries/BACI_HS17_Y{yyyy}_V202601.parquet  full bilateral HS6 data, last 5 years (zstd parquet;
                                                   cols t,i,j,k(int, HS6 without leading zero),v(kUSD),q(t))
  baci_hs17_world_exports_exporter_hs6_{last}.csv.gz   exporter x HS6 world exports + Balassa RCA
  baci_hs17_tur_bilateral_hs6_{first}_{last}.csv.gz    Türkiye exports (X) and imports (M) by HS6 x partner
  country_codes_V202601.csv, product_codes_HS17_V202601.csv, Readme.txt, baci_validation.csv
CSV members are streamed from the zip (never fully extracted to disk).
"""
import sys, os, zipfile, argparse
import pandas as pd

TUR = 792
EU27_ISO3 = {"AUT", "BEL", "BGR", "HRV", "CYP", "CZE", "DNK", "EST", "FIN", "FRA", "DEU", "GRC", "HUN", "IRL",
             "ITA", "LVA", "LTU", "LUX", "MLT", "NLD", "POL", "PRT", "ROU", "SVK", "SVN", "ESP", "SWE"}
DT = {"t": "int16", "i": "int16", "j": "int16", "k": "int32", "v": "float64", "q": "float64"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("zip")
    ap.add_argument("outdir")
    ap.add_argument("--years", default=None, help="e.g. 2020-2024 (default: last 5 in zip)")
    ap.add_argument("--delete-zip", action="store_true")
    a = ap.parse_args()
    os.makedirs(os.path.join(a.outdir, "all_countries"), exist_ok=True)
    z = zipfile.ZipFile(a.zip)
    names = z.namelist()
    ver = os.path.basename(a.zip).split("_")[-1].replace(".zip", "")
    yfiles = {int(n.split("_Y")[1][:4]): n for n in names if "_Y" in n and n.endswith(".csv")}
    if a.years:
        y0, y1 = map(int, a.years.split("-"))
    else:
        y1 = max(yfiles)
        y0 = y1 - 4
    years = [y for y in sorted(yfiles) if y0 <= y <= y1]
    print("version", ver, "years in zip", sorted(yfiles), "-> using", years, flush=True)
    for n in names:  # small metadata files
        if not n.endswith(".csv") or "_Y" not in n:
            with z.open(n) as src, open(os.path.join(a.outdir, os.path.basename(n)), "wb") as dst:
                dst.write(src.read())
    cc = pd.read_csv(os.path.join(a.outdir, [os.path.basename(n) for n in names if "country_codes" in n][0]),
                     dtype=str, keep_default_na=False)
    cc["country_code"] = cc["country_code"].astype(int)
    iso3 = dict(zip(cc.country_code, cc.country_iso3))
    cname = dict(zip(cc.country_code, cc.country_name))
    eu_codes = {c for c, s in iso3.items() if s in EU27_ISO3}
    print("EU27 codes found:", len(eu_codes), sorted(eu_codes), flush=True)

    tur_parts, val = [], []
    last = None
    for y in years:
        with z.open(yfiles[y]) as f:
            df = pd.read_csv(f, dtype=DT, na_values=["NA", ""], skipinitialspace=True)
        df.to_parquet(os.path.join(a.outdir, "all_countries", f"BACI_HS17_Y{y}_{ver}.parquet"),
                      compression="zstd", index=False)
        x = df[df.i == TUR].rename(columns={"j": "partner"}).assign(flow="X")
        m = df[df.j == TUR].rename(columns={"i": "partner"}).assign(flow="M")
        tp = pd.concat([x.drop(columns="i"), m.drop(columns="j")], ignore_index=True)
        tur_parts.append(tp)
        val.append(dict(year=y, rows=len(df), world_kusd=df.v.sum(),
                        tur_X_kusd=x.v.sum(), tur_M_kusd=m.v.sum(),
                        tur_X_EU27_kusd=x[x.partner.isin(eu_codes)].v.sum(),
                        tur_M_EU27_kusd=m[m.partner.isin(eu_codes)].v.sum(),
                        tur_X_hs6=x.k.nunique(), tur_M_hs6=m.k.nunique()))
        print(val[-1], flush=True)
        if y == years[-1]:
            last = df
        else:
            del df

    # (b) Türkiye bilateral, HS6 x partner, all years
    t = pd.concat(tur_parts, ignore_index=True)
    t["hs6"] = t.k.astype(str).str.zfill(6)
    t["partner_iso3"] = t.partner.map(iso3)
    t["partner_name"] = t.partner.map(cname)
    t["eu27"] = t.partner.isin(eu_codes).astype(int)
    t = t.rename(columns={"t": "year", "partner": "partner_code", "v": "value_kusd", "q": "qty_tonnes"})
    t = t[["year", "flow", "partner_code", "partner_iso3", "partner_name", "eu27", "hs6", "value_kusd",
           "qty_tonnes"]].sort_values(["year", "flow", "partner_code", "hs6"])
    fb = os.path.join(a.outdir, f"baci_hs17_tur_bilateral_hs6_{years[0]}_{years[-1]}.csv.gz")
    t.to_csv(fb, index=False)
    print("wrote", fb, len(t), "rows", flush=True)

    # (a) world exports by exporter x HS6, last year, + Balassa RCA
    w = last.groupby(["i", "k"], as_index=False).agg(value_kusd=("v", "sum"), qty_tonnes=("q", "sum"))
    xi = w.groupby("i").value_kusd.transform("sum")
    xk = w.groupby("k").value_kusd.transform("sum")
    w["rca"] = (w.value_kusd / xi) / (xk / w.value_kusd.sum())
    w.insert(0, "year", years[-1])
    w["exporter_iso3"] = w.i.map(iso3)
    w["hs6"] = w.k.astype(str).str.zfill(6)
    w = w.rename(columns={"i": "exporter_code"})[["year", "exporter_code", "exporter_iso3", "hs6", "value_kusd",
                                                  "qty_tonnes", "rca"]]
    fa = os.path.join(a.outdir, f"baci_hs17_world_exports_exporter_hs6_{years[-1]}.csv.gz")
    w.to_csv(fa, index=False, float_format="%.6g")
    print("wrote", fa, len(w), "rows; TUR RCA>1 products:",
          int(((w.exporter_iso3 == "TUR") & (w.rca > 1)).sum()), flush=True)
    v = pd.DataFrame(val)
    v.to_csv(os.path.join(a.outdir, "baci_validation.csv"), index=False)
    pd.set_option("display.width", 250)
    print(v.to_string(), flush=True)
    if a.delete_zip:
        os.remove(a.zip)
        print("deleted", a.zip, flush=True)


if __name__ == "__main__":
    main()
