"""Faz 2 — Türkiye'nin kendi tarife politikası: gelir tabanı, "girdide sıfır" paketi (özerklik temettüsü)
ve S4'te AB mallarına uygulanacak tarifenin aktif tasarımı.

Girdiler:
  - BACI 2024: Türkiye ithalatı (HS6 × ortak; baci_ozet.py) ve dünya ihracatı + RCA (Türkiye satırları)
  - WITS HS2017 → BEC Rev. 4 eşleştirmesi (Concordance_H5_to_BE)
  - 2026 Türk tarifesi (veri/tarife_tr_2026_gtip12.csv), cn2025_nace_rejim.csv (HS6 → I-O ürünü, rejim)
  - TÜİK 2023 girdi-çıktı tabloları (f2a_io_fiyat.py ile aynı model)
Tanımlar:
  - Ortak grupları: AB27; STA ortakları (yürürlükteki STA'lar, sanayi ürünlerinde sıfır; tarımda MFN
    varsayıldı); diğer (MFN + İGV + EMY). GSP tercihleri yok sayıldı (gelir üst sınırı).
  - Kullanım amacı (BEC Rev. 4): sermaye malı 41, 521; ara malı 111, 121, 21, 22, 31, 322, 42, 53;
    tüketim malı 112, 122, 522, 61, 62, 63; karma 321, 51 (binek otomobil), 7.
  - Yurt içi kabiliyet: TÜİK PRODTR 2025 üretimden satış değeri (CPA 2.2, 6 hane; prodtr.py). Ürünün
    CPA grubunda yurt içi üretim, aynı grubun ithalatının en az %10'u ise veya veri gizliyse (az
    girişimli üretim var) "üretim var" [H: eşik]. İkincil vekil: HS6 ihracatı/ithalatı ≥ 0,25 veya RCA ≥ 0,5.
Paketler:
  - S4-pasif: AB menşeli GB ve İTÜ ithalatına 2026 MFN (İGV hariç ve İGV dahil iki ölçü)
  - P1 "girdide sıfır": sanayi fasıllarında (25–97) üretimi olmayan veya zayıf ara ve sermaye
    mallarında MFN, İGV ve EMY = 0 (bütün kaynaklar; MFN ilkesi gereği). Tarım girdileri tarım
    politikasıyla birlikte ele alınır (Faz 3, bölüm 10–12)
  - S4+P1: S4-pasif; P1 satırlarında AB'ye de sıfır
Çıktılar:
  veri/politika_tarife_hs6.csv    HS6 satırları: ithalat (kaynağa göre), oranlar, BEC, kabiliyet, P1 bayrağı
  veri/politika_tarife_ozet.csv   paket özeti: TÜFE (bp; ρ = 0,6/0,8/1,0); politika_tarife_gelir.csv: gelir
  veri/politika_tarife_io_urun.csv I-O ürünleri: üretici fiyatı ve TÜFE katkısı
  veri/prodtr_cpa6_2025.csv       CPA 6 hane: üretimden satış (2025), girişim sayısı, ithalat, üretim/ithalat
"""

import argparse
import os

import numpy as np
import pandas as pd

import f2a_io_fiyat as io
import prodtr

STA = {"CHE", "NOR", "ISL", "LIE", "ISR", "MKD", "BIH", "PSE", "TUN", "MAR", "EGY", "ALB", "GEO", "MNE", "SRB",
       "CHL", "MUS", "KOR", "MYS", "MDA", "FRO", "SGP", "GBR", "ARE"}
BEC = {"41": "sermaye", "521": "sermaye", "111": "ara", "121": "ara", "21": "ara", "22": "ara", "31": "ara",
       "322": "ara", "42": "ara", "53": "ara", "112": "tuketim", "122": "tuketim", "522": "tuketim",
       "61": "tuketim", "62": "tuketim", "63": "tuketim", "321": "karma", "51": "karma", "7": "karma"}
IHRACAT_ESIGI, RCA_ESIGI = 0.25, 0.5
URETIM_ESIGI = 0.10   # yurt içi üretim / ithalat (CPA 6 hane)


def veri_kur(a):
    v = lambda f: os.path.join(a.out, f)  # noqa: E731
    b = pd.read_csv(a.baci_tr, dtype={"hs6": str})
    b = b[b.year == b.year.max()].copy()
    b["hs6"] = b.hs6.str.zfill(6)
    m = b[b.flow == "M"].copy()
    m["grup"] = np.where(m.eu27 == 1, "ab", np.where(m.partner_iso3.isin(STA), "sta", "diger"))
    t = m.pivot_table(index="hs6", columns="grup", values="value_kusd", aggfunc="sum").fillna(0) / 1e3
    t.columns = [f"m_{c}_musd" for c in t.columns]
    t["m_toplam_musd"] = t.sum(axis=1)
    t["x_musd"] = b[b.flow == "X"].groupby("hs6").value_kusd.sum() / 1e3
    w = pd.read_csv(a.baci_dunya, dtype={"hs6": str})
    w = w[w.exporter_iso3 == "TUR"]
    w["hs6"] = w.hs6.str.zfill(6)
    t["rca"] = w.set_index("hs6").rca
    t = t.fillna({"x_musd": 0.0})

    bec = pd.read_csv(a.bec, dtype=str)
    bec.columns = ["hs6", "hs_ad", "bec", "bec_ad"]
    bec["hs6"] = bec.hs6.str.strip().str.zfill(6)
    bec["bec"] = bec.bec.str.strip()
    t["bec"] = bec.drop_duplicates("hs6").set_index("hs6").bec
    t["kullanim"] = t.bec.map(BEC).fillna("karma")

    tr = pd.read_csv(v("tarife_tr_2026_gtip12.csv"), dtype={"gtip12": str, "hs6": str})
    tr = tr[~tr.in_tgtc_only]
    t["t_mfn"] = tr.groupby("hs6").mfn_rate.mean()
    t["t_tam"] = tr.groupby("hs6").mfn_igv_emy.mean()
    t[["t_mfn", "t_tam"]] = t[["t_mfn", "t_tam"]].fillna(0)

    hs6_io, hs6_rejim = io.hs6_esleme(v("cn2025_nace_rejim.csv"))
    t["io"] = t.index.map(hs6_io)
    t["rejim"] = t.index.map(hs6_rejim)
    t["tarim"] = t.index.str[:2].astype(int) <= 24
    oran = t.x_musd / t.m_toplam_musd.replace(0, np.nan)
    t["ihracat_vekili"] = (oran >= IHRACAT_ESIGI) | (t.rca >= RCA_ESIGI)

    # PRODTR: CPA 6 hane üretim ve girişim sayısı (2025, TL → $ 2025 ortalama kuru)
    usd_try = pd.read_csv(v("teshis_odemeler_dengesi.csv"), index_col=0).loc[2025, "usd_try"]
    pr = prodtr.cpa6(os.path.join(a.cache, "prodtr")).set_index("cpa22")
    pr["uretim_musd"] = pr.satis_tl / usd_try / 1e6
    m = pd.read_csv(v("cn2025_nace_rejim.csv"), dtype={"cn8": str, "cpa22": str})
    m = m[m.cn8.str.fullmatch(r"\d{8}") & m.cpa22.notna()].copy()
    m["hs6"] = m.cn8.str[:6]
    m["w"] = m.tr_ith_ab.fillna(0) + 1.0
    hc = m.groupby(["hs6", "cpa22"]).w.sum().reset_index().sort_values(["hs6", "w"]).drop_duplicates("hs6", keep="last")
    t["cpa22"] = t.index.map(hc.set_index("hs6").cpa22)
    ith_cpa = t.groupby("cpa22").m_toplam_musd.sum()
    t["uretim_musd"] = t.cpa22.map(pr.uretim_musd)
    t["girisim"] = t.cpa22.map(pr.girisim)
    t["gizli"] = t.cpa22.map(pr.gizli).fillna(False).astype(bool)
    t["uretim_ithalat_orani"] = t.uretim_musd / t.cpa22.map(ith_cpa)
    t["uretim_var"] = t.gizli | (t.uretim_ithalat_orani >= URETIM_ESIGI)
    cpa_tablo = pr.join(ith_cpa.rename("ithalat_2024_musd"), how="outer")
    cpa_tablo["uretim_ithalat_orani"] = cpa_tablo.uretim_musd / cpa_tablo.ithalat_2024_musd
    cpa_tablo.round(3).to_csv(v("prodtr_cpa6_2025.csv"))
    # P1 yalnızca sanayi fasıllarında (25–97): tarımda ihracat vekili yurt içi üretimi göstermez
    t["p1"] = t.kullanim.isin(["ara", "sermaye"]) & ~t.uretim_var & ~t.tarim
    for c in ("m_ab_musd", "m_sta_musd", "m_diger_musd"):
        if c not in t:
            t[c] = 0.0
    # mevcut gelir (2026 oranları × 2024 ithalatı)
    t["gelir_mevcut_musd"] = (t.m_diger_musd * t.t_tam / 100
                              + np.where(t.tarim, (t.m_sta_musd + t.m_ab_musd) * t.t_mfn / 100, 0.0))
    t["p1_gelir_kaybi_musd"] = np.where(t.p1, t.gelir_mevcut_musd, 0.0)
    gb = t.rejim.isin(["GB", "ITU"])
    for olcu, sut in (("mfn", "t_mfn"), ("tam", "t_tam")):
        t[f"s4_gelir_{olcu}_musd"] = np.where(gb, t.m_ab_musd * t[sut] / 100, 0.0)
    return t


def vektor(t, kod, deger):
    """HS6 düzeyindeki maliyet değişimini (milyon $) I-O ürünlerine, ürün ithalatına oranla dağıtır."""
    g = t.groupby("io").agg(m=("m_toplam_musd", "sum"))
    g["d"] = deger.groupby(t.io).sum()
    oranlar = (g.d / g.m).reindex(kod).fillna(0.0)
    return oranlar.to_numpy()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baci-tr", required=True)
    ap.add_argument("--baci-dunya", required=True, help="baci_hs17_world_exports_exporter_hs6_2024.csv.gz")
    ap.add_argument("--bec", required=True, help="WITS JobID-86_Concordance_H5_to_BE.CSV")
    ap.add_argument("--cache", default=os.path.expanduser("~/.cache/gb_cikis"))
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    t = veri_kur(a)

    yollar = io.io_indir(os.path.join(a.cache, "io2023"))
    yd, kod = io.oku(yollar["yurtici"])
    it, _ = io.oku(yollar["ithalat"])
    ka, _ = io.oku(yollar["kullanim_alici"])
    Z_d = yd.iloc[io.SATIR, io.SUTUN].astype(float).to_numpy()
    Z_m = it.iloc[io.SATIR, io.SUTUN].astype(float).to_numpy()
    x = yd.iloc[io.P1, io.SUTUN].astype(float).to_numpy()
    h_d = yd.iloc[io.SATIR, io.HH].astype(float).to_numpy()
    h_m = it.iloc[io.SATIR, io.HH].astype(float).to_numpy()
    w = np.where(np.array(kod) == "L68A", 0.0, np.clip(ka.iloc[io.SATIR, io.HH].astype(float).to_numpy(), 0, None))
    w = w / w.sum()
    A_d = np.divide(Z_d, x, out=np.zeros_like(Z_d), where=x > 0)
    A_m = np.divide(Z_m, x, out=np.zeros_like(Z_m), where=x > 0)

    tt = t[t.io.notna()]
    gb = tt.rejim.isin(["GB", "ITU"])
    p1 = tt.p1
    senaryolar = {
        "S4_pasif_mfn": vektor(tt, kod, (tt.m_ab_musd * tt.t_mfn / 100).where(gb, 0.0)),
        "S4_pasif_tam": vektor(tt, kod, (tt.m_ab_musd * tt.t_tam / 100).where(gb, 0.0)),
        "P1": -vektor(tt, kod, tt.p1_gelir_kaybi_musd),
    }
    senaryolar["S4_P1_mfn"] = vektor(tt, kod, (tt.m_ab_musd * tt.t_mfn / 100).where(gb & ~p1, 0.0)) + senaryolar["P1"]
    senaryolar["S4_P1_tam"] = vektor(tt, kod, (tt.m_ab_musd * tt.t_tam / 100).where(gb & ~p1, 0.0)) + senaryolar["P1"]

    ozet, urun = [], {}
    for ad, dtau in senaryolar.items():
        for rho in io.RHO:
            dP, toplam, dp_d = io.model(A_d, A_m, h_d, h_m, w, dtau, rho, 0.0)
            ozet.append(dict(paket=ad, rho=rho, tufe_bp=toplam * 1e4))
            if rho == 0.8:
                urun[ad + "_uretici_fiyat_yuzde"] = dp_d * 100
                urun[ad + "_tufe_katki_bp"] = w * dP * 1e4
    oz = pd.DataFrame(ozet)
    gelir = {
        "gelir_mevcut_musd": t.gelir_mevcut_musd.sum(),
        "p1_gelir_kaybi_musd": t.p1_gelir_kaybi_musd.sum(),
        "s4_gelir_mfn_musd": t.s4_gelir_mfn_musd.sum(),
        "s4_gelir_tam_musd": t.s4_gelir_tam_musd.sum(),
        "s4_p1_gelir_mfn_musd": t.s4_gelir_mfn_musd.where(~t.p1, 0).sum(),
        "s4_p1_gelir_tam_musd": t.s4_gelir_tam_musd.where(~t.p1, 0).sum(),
        "p1_hs6_sayisi": int(t.p1.sum()),
        "p1_ithalat_musd": t.loc[t.p1, "m_toplam_musd"].sum(),
        "ithalat_toplam_musd": t.m_toplam_musd.sum(),
    }
    pd.DataFrame([gelir]).round(1).to_csv(os.path.join(a.out, "politika_tarife_gelir.csv"), index=False)
    oz.round(2).to_csv(os.path.join(a.out, "politika_tarife_ozet.csv"), index=False)
    u = pd.DataFrame(urun, index=kod)
    u.insert(0, "ad", yd.iloc[io.SATIR, 2].astype(str).str.split("\n").str[0].str.strip().tolist())
    u.round(4).to_csv(os.path.join(a.out, "politika_tarife_io_urun.csv"))
    sut = ["m_ab_musd", "m_sta_musd", "m_diger_musd", "m_toplam_musd", "x_musd", "rca", "bec", "kullanim",
           "cpa22", "uretim_musd", "girisim", "gizli", "uretim_ithalat_orani", "uretim_var", "ihracat_vekili",
           "p1", "t_mfn", "t_tam", "io", "rejim", "gelir_mevcut_musd", "s4_gelir_mfn_musd", "s4_gelir_tam_musd"]
    t[sut].round(4).to_csv(os.path.join(a.out, "politika_tarife_hs6.csv"))

    pd.set_option("display.width", 220)
    print(pd.Series(gelir).round(1).to_string())
    print(t.groupby(["kullanim", "uretim_var"]).agg(hs6=("t_mfn", "size"), ithalat=("m_toplam_musd", "sum"),
                                                     ab=("m_ab_musd", "sum"),
                                                     gelir=("gelir_mevcut_musd", "sum")).round(0).to_string())
    print(oz.pivot_table(index="paket", columns="rho", values="tufe_bp").round(1).to_string())
    secili = ["C29", "C13-C15", "C27", "C28", "C24", "C22", "C25", "C20", "C10-C12", "C26"]
    print(u.loc[secili, [c for c in u.columns if "uretici" in c]].round(3).to_string())


if __name__ == "__main__":
    main()
