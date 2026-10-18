"""Faz 3 — NACE sınıfı düzeyinde dış ticaret göstergeleri (kart alan 3 ve 4; ana matris sütunları).

Kaynak: CEPII BACI HS17 V202601 (girdi/baci/; özetler girdi_hazirla.py baci-ozet ve baci-ozet-f3 ile):
  - Türkiye'nin ortak × HS6 ihracatı ve ithalatı, 2020 ve 2024 (bin $, ton)
  - AB27'nin ihracatçı × HS6 ithalatı, 2020 ve 2024 (AB içi dahil; AB dışı ayrıca)
  - dünya ihracatı, HS6, 2020 ve 2024
HS6 → NACE Rev. 2: veri/cn2025_nace_rejim.csv'deki KN8 → NACE ağırlıkları HS6'ya toplanır (KN8 satırının bölünme
  ağırlığı × 2025 AB–TR ticareti; ticaret yoksa eşit). BACI HS2017 kodudur; HS2022'de değişen kodlar HS4 düzeyindeki
  ağırlıklarla dağıtılır `[T]`.
Göstergeler (sınıf × yıl):
  RCA_dünya = (X_TR,i / X_TR) / (X_W,i / X_W)
  RCA_AB    = (X_TR→AB,i / X_TR→AB) / (M_AB←AB dışı,i / M_AB←AB dışı)    (AB pazarında, AB dışı tedarikçilere göre)
  AB pazar payı = X_TR→AB,i / M_AB←AB dışı,i   ve   X_TR→AB,i / M_AB,i (AB içi dahil)
  Birim değer oranı = Σ_k w_k × (UV_TR→AB,k / UV_AB dışı→AB,k); w_k sınıf içindeki TR→AB payı; oranlar [0,2; 5]'e kırpılır
AB pazarındaki tercihli rakipler: AB dışı ilk 5 tedarikçi ve AB'deki tercih durumları (f2f.AB_ANLASMA; GSP+ ve EBA ayrı).
PEM çapraz kümülasyonu maruziyeti (PEM_KUM): x_pem (TR→PEM ortağı ihracatı) ve x_kum (ortağın AB'ye ihracat payıyla ağırlıklı).
Çıktı: veri/f3_ticaret_sinif.csv, veri/f3_ortaklar_sinif.csv (ilk 5: AB pazarı, AB dışı pazar, ithalat kaynağı, AB'deki rakip),
       veri/f3_pem_ortak_ab_payi.csv (PEM ortaklarının AB'ye ihracat payı: giyim Fasıl 61–63 ve toplam).
"""

import argparse
import os

import numpy as np
import pandas as pd

import yollar

AB27 = {"AUT", "BEL", "BGR", "HRV", "CYP", "CZE", "DNK", "EST", "FIN", "FRA", "DEU", "GRC", "HUN", "IRL", "ITA", "LVA",
        "LTU", "LUX", "MLT", "NLD", "POL", "PRT", "ROU", "SVK", "SVN", "ESP", "SWE"}
# AB'nin tek taraflı tercihleri (2024): GSP+ ve Silah Dışında Her Şey (EBA) yararlanıcılarının başlıcaları `[T]`
GSP_ARTI = {"PAK", "LKA", "PHL", "BOL", "CPV", "KGZ", "MNG", "UZB", "TJK"}
EBA = {"BGD", "KHM", "MMR", "ETH", "TZA", "UGA", "SEN", "MLI", "BFA", "NPL", "LAO", "HTI", "YEM", "AFG", "SOM", "SDN"}
YILLAR = (2020, 2024)
# PEM çapraz kümülasyonu: hem Türkiye hem AB ile tercihli anlaşması olan PEM tarafları (2026; İsrail ticareti askıda,
# Ürdün STA'sı 2018'de sona erdi, Cezayir ve Lübnan'la TR anlaşması yürürlükte değil) `[V]`. Türk girdisi bu ülkelerde
# işlenip AB'ye tercihli satıldığında kümülasyon, Türkiye ile AB arasında GATT XXIV anlaşması ister (PEM Ek I md. 8(1)(a)):
# S4'te Türk girdisi menşesiz sayılır. Maruziyet = Σ TR→ortak ihracatı × ortağın aşağı yön ürünlerinde AB'ye ihracat payı
# (13. bölüm için Fasıl 61–63, diğerlerinde ortağın toplam ihracatı); Türk girdisinin ortağın AB'ye giden üretiminde
# orantılı kullanıldığı varsayımıyla üst sınır `[T]`
PEM_KUM = {"MAR", "TUN", "EGY", "ALB", "BIH", "MNE", "MKD", "SRB", "XKX", "GEO", "MDA", "UKR", "CHE", "NOR", "ISL", "LIE",
           "FRO"}
ASAGI_GIYIM = ("61", "62", "63")
ASAGI_GIYIM_BOLUM = ("13",)


def hs6_nace_agirlik(eslem_yolu):
    """HS6 (HS2022) ve HS4 → NACE sınıfı ağırlıkları (her HS6/HS4 için toplam 1)."""
    m = pd.read_csv(eslem_yolu, dtype={"cn8": str, "nace2": str})
    m = m[m.cn8.str.fullmatch(r"\d{8}") & m.nace2.notna()].copy()
    deger = (m.tr_ihr_ab.fillna(0) + m.tr_ith_ab.fillna(0)).groupby(m.cn8).transform("sum")   # satırın tüm değeri
    m = m[m.agirlik_f3 > 0].copy()
    m["hs6"], m["hs4"] = m.cn8.str[:6], m.cn8.str[:4]
    m["w"] = m.agirlik_f3 * np.maximum(deger.reindex(m.index), 1.0)
    cikti = {}
    for duzey in ("hs6", "hs4"):
        g = m.groupby([duzey, "nace2"]).w.sum()
        cikti[duzey] = (g / g.groupby(level=0).transform("sum")).rename("pay").reset_index()
    return cikti


def nace_dagit(df, agirlik, deger_sutunlari, anahtarlar):
    """HS6 düzeyindeki değerleri NACE sınıflarına dağıtır (önce HS6, yoksa HS4 ağırlığı)."""
    df = df.copy()
    df["hs6"] = df.hs6.astype(str).str.zfill(6)
    a6 = df.merge(agirlik["hs6"], on="hs6", how="inner")
    kalan = df[~df.hs6.isin(agirlik["hs6"].hs6)].copy()
    kalan["hs4"] = kalan.hs6.str[:4]
    a4 = kalan.merge(agirlik["hs4"], on="hs4", how="inner")
    a = pd.concat([a6, a4], ignore_index=True)
    for s in deger_sutunlari:
        a[s] = a[s] * a.pay
    eslesmeyen = df[~df.hs6.isin(a.hs6)][deger_sutunlari[0]].sum() / max(df[deger_sutunlari[0]].sum(), 1e-9)
    return a.groupby(anahtarlar + ["nace2"], as_index=False)[deger_sutunlari].sum(), eslesmeyen


def tercih_durumu(iso3):
    import f2f_cekim_modeli as f2f
    sta = {u: kat for u, kat, *_ in f2f.AB_ANLASMA if kat not in ("KATILIM",)}
    if iso3 in sta:
        return {"EFTA": "AEA/STA", "AB_BK_TCA": "TCA"}.get(sta[iso3], "STA/EPA")
    if iso3 in GSP_ARTI:
        return "GSP+"
    if iso3 in EBA:
        return "EBA"
    return "MFN/GSP"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=yollar.VERI)
    a = ap.parse_args()
    v = lambda f: os.path.join(a.out, f)  # noqa: E731
    g = lambda *p: yollar.bul(yollar.girdi(*p)) or yollar.girdi(*p)  # noqa: E731

    agirlik = hs6_nace_agirlik(v("cn2025_nace_rejim.csv"))
    uk = pd.read_csv(g("baci", "country_codes_V202601.csv"), dtype={"country_code": int})
    iso = uk.drop_duplicates("country_code").set_index("country_code").country_iso3
    ad = uk.drop_duplicates("country_iso3").set_index("country_iso3").country_name

    # --- Türkiye: ortak × HS6, 2020 ve 2024
    tr = pd.read_csv(g("baci", "baci_hs17_tur_bilateral_hs6_2020_2024.csv.gz"), dtype={"hs6": str})
    tr = tr[tr.year.isin(YILLAR)].copy()
    # BACI'deki Kıbrıs akımları (2024'te TR→CYP $1,6 mlr; %31'i akaryakıt) büyük ölçüde KKTC ticaretidir ve AB gümrük
    # bölgesi dışında kalır (Protokol 10): AB maruziyetinde AB dışı sayılır; AB27 pazarı verisinden de düşülür [T]
    tr.loc[tr.partner_iso3.eq("CYP"), "eu27"] = 0
    kktc = tr[(tr.flow == "X") & tr.partner_iso3.eq("CYP")].assign(k=lambda d: d.hs6.astype(int)) \
        .groupby(["year", "k"])[["value_kusd", "qty_tonnes"]].sum()
    tr_n, kayip_tr = nace_dagit(tr, agirlik, ["value_kusd", "qty_tonnes"], ["year", "flow", "partner_iso3", "eu27"])
    tr_n["value_musd"] = tr_n.value_kusd / 1e3
    tr_n["cin"] = (tr_n.partner_iso3 == "CHN").astype(int)
    toplam_tr = tr.groupby(["year", "flow"]).value_kusd.sum() / 1e3          # dağıtım öncesi toplam (RCA paydası)
    tr_ab_toplam = tr[(tr.flow == "X") & (tr.eu27 == 1)].groupby("year").value_kusd.sum() / 1e3

    # --- AB27'nin ithalatı (ihracatçı × HS6) ve dünya ihracatı
    ab = pd.read_parquet(g("baci", "baci_hs17_ab27_ithalat_ihracatci_hs6_2020_2024.parquet"))
    ab = ab.rename(columns={"t": "year", "k": "hs6", "v": "value_kusd", "q": "qty_tonnes"})
    ab["iso3"] = ab.i.map(iso)
    tur = ab.iso3.eq("TUR")
    dus = ab.loc[tur, ["year", "hs6"]].merge(kktc.reset_index().rename(columns={"k": "hs6"}), on=["year", "hs6"],
                                             how="left").fillna(0)
    ab.loc[tur, "value_kusd"] = (ab.loc[tur, "value_kusd"].to_numpy() - dus.value_kusd.to_numpy()).clip(min=0)
    ab.loc[tur, "qty_tonnes"] = (ab.loc[tur, "qty_tonnes"].to_numpy() - dus.qty_tonnes.to_numpy()).clip(min=0)
    ab["ab_ici"] = ab.iso3.isin(AB27).astype(int)
    ab_n, _ = nace_dagit(ab, agirlik, ["value_kusd", "qty_tonnes"], ["year", "iso3", "ab_ici"])
    dunya = pd.read_parquet(g("baci", "baci_hs17_dunya_ihracat_hs6_2020_2024.parquet"))
    dunya = dunya.rename(columns={"t": "year", "k": "hs6", "v": "value_kusd"})
    dunya_n, _ = nace_dagit(dunya, agirlik, ["value_kusd"], ["year"])
    dunya_toplam = dunya.groupby("year").value_kusd.sum() / 1e3
    ab_disi_toplam = ab[ab.ab_ici == 0].groupby("year").value_kusd.sum() / 1e3

    satirlar = []
    for y in YILLAR:
        t = tr_n[tr_n.year == y]
        x = t[t.flow == "X"].groupby("nace2").value_musd.sum()
        x_ab = t[(t.flow == "X") & (t.eu27 == 1)].groupby("nace2").value_musd.sum()
        m = t[t.flow == "M"].groupby("nace2").value_musd.sum()
        m_ab = t[(t.flow == "M") & (t.eu27 == 1)].groupby("nace2").value_musd.sum()
        m_cin = t[(t.flow == "M") & (t.cin == 1)].groupby("nace2").value_musd.sum()
        w = dunya_n[dunya_n.year == y].set_index("nace2").value_kusd / 1e3
        b = ab_n[ab_n.year == y]
        ab_disi = b[b.ab_ici == 0].groupby("nace2").value_kusd.sum() / 1e3
        ab_tum = b.groupby("nace2").value_kusd.sum() / 1e3
        d = pd.DataFrame({"x_musd": x, "x_ab_musd": x_ab, "m_musd": m, "m_ab_musd": m_ab, "m_cin_musd": m_cin,
                          "x_dunya_musd": w, "m_ab_abdisi_musd": ab_disi, "m_ab_tum_musd": ab_tum}).fillna(0.0)
        d["rca_dunya"] = (d.x_musd / toplam_tr[(y, "X")]) / (d.x_dunya_musd / dunya_toplam[y])
        d["rca_ab"] = (d.x_ab_musd / tr_ab_toplam[y]) / (d.m_ab_abdisi_musd / ab_disi_toplam[y])
        d["ab_pazar_payi_abdisi"] = d.x_ab_musd / d.m_ab_abdisi_musd
        d["ab_pazar_payi_tum"] = d.x_ab_musd / d.m_ab_tum_musd
        d["year"] = y
        satirlar.append(d.reset_index().rename(columns={"index": "nace2"}))
    s = pd.concat(satirlar, ignore_index=True).replace([np.inf, -np.inf], np.nan)
    gen = s.pivot(index="nace2", columns="year")
    gen.columns = [f"{c}_{y}" for c, y in gen.columns]
    gen = gen.reset_index()
    for c in ("x", "x_ab", "m", "m_ab", "m_cin"):
        gen[f"{c}_musd_degisim_yuzde"] = 100 * (gen[f"{c}_musd_2024"] / gen[f"{c}_musd_2020"] - 1)
    gen["ab_ihracat_payi_2024"] = gen.x_ab_musd_2024 / gen.x_musd_2024
    gen["ab_ithalat_payi_2024"] = gen.m_ab_musd_2024 / gen.m_musd_2024
    gen["cin_ithalat_payi_2024"] = gen.m_cin_musd_2024 / gen.m_musd_2024
    gen["denge_musd_2024"] = gen.x_musd_2024 - gen.m_musd_2024

    # --- Birim değer oranı (2024): TR→AB / AB dışı→AB, HS6 düzeyinde, sonra sınıf ağırlıklı
    ab24 = ab[(ab.year == 2024) & (ab.ab_ici == 0)].copy()
    ab24["hs6"] = ab24.hs6.astype(str).str.zfill(6)
    uv_all = ab24.groupby("hs6")[["value_kusd", "qty_tonnes"]].sum()
    uv_tr = ab24[ab24.iso3 == "TUR"].groupby("hs6")[["value_kusd", "qty_tonnes"]].sum()
    oran = ((uv_tr.value_kusd / uv_tr.qty_tonnes) / (uv_all.value_kusd / uv_all.qty_tonnes)).replace([np.inf, -np.inf], np.nan)
    uv = pd.DataFrame({"hs6": oran.index, "oran": oran.clip(0.2, 5).values, "w": uv_tr.value_kusd.reindex(oran.index).values})
    uv = uv[uv.oran.notna() & (uv.w > 0)]
    uv_n, _ = nace_dagit(uv.assign(ow=uv.oran * uv.w), agirlik, ["ow", "w"], [])
    gen["birim_deger_orani_2024"] = gen.nace2.map(uv_n.set_index("nace2").eval("ow / w"))

    # --- İlk 5 listeleri (2024)
    liste = []
    t24 = tr_n[tr_n.year == 2024]
    for tur, kosul in (("AB pazarı", (t24.flow == "X") & (t24.eu27 == 1)), ("AB dışı pazar", (t24.flow == "X") & (t24.eu27 == 0)),
                       ("İthalat kaynağı", t24.flow == "M")):
        p = t24[kosul].groupby(["nace2", "partner_iso3"]).value_musd.sum().reset_index()
        p["pay"] = p.value_musd / p.groupby("nace2").value_musd.transform("sum")
        p = p.sort_values(["nace2", "value_musd"], ascending=[True, False]).groupby("nace2").head(5)
        p["tur"] = tur
        liste.append(p)
    b24 = ab_n[(ab_n.year == 2024) & (ab_n.ab_ici == 0)].copy()
    b24["value_musd"] = b24.value_kusd / 1e3
    b24["pay"] = b24.value_musd / b24.groupby("nace2").value_musd.transform("sum")
    tr_sira = b24.assign(sira=b24.groupby("nace2").value_musd.rank(ascending=False))
    gen["ab_pazari_tr_sirasi_2024"] = gen.nace2.map(tr_sira[tr_sira.iso3 == "TUR"].set_index("nace2").sira)
    r = b24[b24.iso3 != "TUR"].sort_values(["nace2", "value_musd"], ascending=[True, False]).groupby("nace2").head(5)
    r = r.rename(columns={"iso3": "partner_iso3"})[["nace2", "partner_iso3", "value_musd", "pay"]]
    r["tur"] = "AB pazarında rakip (AB dışı)"
    liste.append(r)
    o = pd.concat(liste, ignore_index=True)
    o["ortak_adi"] = o.partner_iso3.map(ad)
    o["ab_tercihi"] = np.where(o.tur.str.startswith("AB pazarında"), o.partner_iso3.map(tercih_durumu), "")
    o["sira"] = o.groupby(["nace2", "tur"]).value_musd.rank(ascending=False, method="first").astype(int)
    o = o.sort_values(["nace2", "tur", "sira"])
    o.round(4).to_csv(v("f3_ortaklar_sinif.csv"), index=False)
    gen["tercihli_rakip_payi_2024"] = gen.nace2.map(
        b24.assign(tercihli=b24.iso3.map(tercih_durumu).isin(["STA/EPA", "AEA/STA", "TCA", "GSP+", "EBA"]))
        .query("tercihli and iso3 != 'TUR'").groupby("nace2").value_musd.sum() / b24.groupby("nace2").value_musd.sum())

    # --- PEM çapraz kümülasyonu maruziyeti (2024): ortağın AB'ye ihracatı ağırlıklı TR→ortak ihracatı
    dw = pd.read_csv(g("baci", "baci_hs17_world_exports_exporter_hs6_2024.csv.gz"), dtype={"hs6": str})
    dw["fasil"] = dw.hs6.str.zfill(6).str[:2]
    ab24k = ab[ab.year == 2024].assign(fasil=lambda x: x.hs6.astype(str).str.zfill(6).str[:2])
    oran_ab = {}
    for ad_, fasillar in (("giyim", ASAGI_GIYIM), ("toplam", None)):
        sw = dw if fasillar is None else dw[dw.fasil.isin(fasillar)]
        sa = ab24k if fasillar is None else ab24k[ab24k.fasil.isin(fasillar)]
        oran_ab[ad_] = (sa.groupby("iso3").value_kusd.sum() / sw.groupby("exporter_iso3").value_kusd.sum()) \
            .reindex(sorted(PEM_KUM)).fillna(0).clip(upper=1)
    k24 = t24[(t24.flow == "X") & t24.partner_iso3.isin(PEM_KUM)]
    gen["x_pem_musd_2024"] = gen.nace2.map(k24.groupby("nace2").value_musd.sum()).fillna(0)
    for ad_ in ("giyim", "toplam"):
        gen[f"x_kum_{ad_}_musd_2024"] = gen.nace2.map(
            k24.assign(w=k24.value_musd * k24.partner_iso3.map(oran_ab[ad_])).groupby("nace2").w.sum()).fillna(0)
    gen["x_kum_musd_2024"] = np.where(gen.nace2.str[:2].isin(ASAGI_GIYIM_BOLUM), gen.x_kum_giyim_musd_2024,
                                      gen.x_kum_toplam_musd_2024)
    pd.DataFrame({"ortak": oran_ab["giyim"].index, "ortak_adi": oran_ab["giyim"].index.map(ad),
                  "ab_payi_giyim_2024": oran_ab["giyim"].values, "ab_payi_toplam_2024": oran_ab["toplam"].values}) \
        .round(4).to_csv(v("f3_pem_ortak_ab_payi.csv"), index=False)
    gen.round(5).to_csv(v("f3_ticaret_sinif.csv"), index=False)
    print(f"Eşleşmeyen TR ticaret payı: %{100 * kayip_tr:.2f}; sınıf sayısı {gen.nace2.nunique()}")
    c = gen[gen.nace2.str.match(r"^(1[0-9]|2[0-9]|3[0-3])\.")]
    print(f"C bölümü: ihracat {c.x_musd_2024.sum():,.0f} / {toplam_tr[(2024, 'X')]:,.0f} mn $; "
          f"ithalat {c.m_musd_2024.sum():,.0f} / {toplam_tr[(2024, 'M')]:,.0f} mn $")


if __name__ == "__main__":
    main()
