"""Faz 0 (revizyon) — TÜİK Yıllık Sanayi ve Hizmet İstatistikleri, NACE Rev. 2 sınıf düzeyi.

Kaynak: TÜİK Dağıtım Yönetim Sistemi, veri akışları
  DF_YAPISAL_EFGTG          (NACE Rev. 2, 2009–2024, sınıf düzeyi)
  DF_YAPISAL_EFGTG_NACEREV21 (NACE Rev. 2.1, 2025 ön sonuç, grup düzeyi)
TL tutarlar ECB yıllık ortalama kurlarıyla (TRY/EUR ÷ USD/EUR) ABD dolarına çevrilir.

Kullanım:
  python3 f0b_tuik_yshi.py --out ../veri
"""

import argparse
import os
import urllib.request

import pandas as pd

import tuik
import yollar

GOSTERGE = {"1": "girisim", "2": "calisan", "3": "ucretli_calisan", "4": "personel_gideri_tl",
            "5": "ciro_tl", "6": "mal_hizmet_alimi_tl", "7": "stok_degisimi_tl",
            "8": "uretim_degeri_tl", "9": "faktor_maliyetiyle_kd_tl", "10": "yeniden_satis_alimi_tl"}
TL_SUTUNLAR = [v for v in GOSTERGE.values() if v.endswith("_tl")]
ECB = "https://data-api.ecb.europa.eu/service/data/EXR/A.{c}.EUR.SP00.A?startPeriod=2009&format=csvdata"


def usd_try(onbellek):
    def seri(c):
        yol = os.path.join(onbellek, "ecb", f"EXR_A_{c}_EUR.csv")
        if not os.path.exists(yol):
            yollar.indirme_izni(ECB.format(c=c))
            os.makedirs(os.path.dirname(yol), exist_ok=True)
            with urllib.request.urlopen(ECB.format(c=c), timeout=120) as r, open(yol, "wb") as f:
                f.write(r.read())
        x = pd.read_csv(yol)
        return x.set_index(x.TIME_PERIOD.astype(str)).OBS_VALUE
    return (seri("TRY") / seri("USD")).rename("usd_try")


def duzenle(ham, nace_sutun, yil_min):
    x = ham[ham.FREQ.eq("A") & ham.REF_AREA.eq("TR")].copy()
    x["kod"] = x[nace_sutun].str.replace(r"^([A-U])(\d\d)(\d)?(\d)?$",
                                         lambda m: m.group(2) + ("." + m.group(3) + (m.group(4) or "")
                                                                 if m.group(3) else ""), regex=True)
    x = x[x.TIME_PERIOD.astype(int) >= yil_min]
    x["gosterge"] = x.TEMEL_GOSTERGE_YILLIK_SANAYI_VE_HIZMET.map(GOSTERGE)
    x["deger"] = pd.to_numeric(x.OBS_VALUE, errors="coerce")
    gizli = x.filter(like="CONF").iloc[:, 0].eq("C")
    x.loc[gizli, "deger"] = float("nan")  # gizli hücreler
    t = x.pivot_table(index=["kod", "TIME_PERIOD"], columns="gosterge", values="deger", aggfunc="first")
    t.columns.name = None
    t = t.reset_index().rename(columns={"TIME_PERIOD": "yil"})
    return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=yollar.GIRDI)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    os.makedirs(a.cache, exist_ok=True)

    r2 = pd.read_csv(tuik.indir_csv("DF_YAPISAL_EFGTG", os.path.join(a.cache, "tuik_DF_YAPISAL_EFGTG.csv")),
                     dtype=str)
    r21 = pd.read_csv(tuik.indir_csv("DF_YAPISAL_EFGTG_NACEREV21",
                                     os.path.join(a.cache, "tuik_DF_YAPISAL_EFGTG_NACEREV21.csv")), dtype=str)
    kur = usd_try(a.cache)

    t2 = duzenle(r2, "ACTIVITY_NACE_REV2", 2015)
    sec = t2.kod.str.fullmatch(r"(0[5-9]|[1-2]\d|3[0-3])(\.\d\d)?|35(\.\d\d?)?|38(\.\d\d?)?")
    t2 = t2[sec]
    t2["usd_try"] = t2.yil.map(kur)
    for s in TL_SUTUNLAR:
        if s in t2:
            t2[s.replace("_tl", "_musd")] = (t2[s] / t2.usd_try / 1e6).round(2)
    sira = ["kod", "yil", "girisim", "calisan", "ucretli_calisan"] + \
           [s.replace("_tl", "_musd") for s in TL_SUTUNLAR] + TL_SUTUNLAR + ["usd_try"]
    t2 = t2.reindex(columns=sira).sort_values(["kod", "yil"])
    t2.to_csv(os.path.join(a.out, "tuik_yshi_nace2.csv"), index=False, float_format="%.6g")

    t21 = duzenle(r21, "EKONOMIK_FAALIYET_NACE_REV_2_1", 2025)
    t21["usd_try"] = t21.yil.map(kur)
    for s in TL_SUTUNLAR:
        if s in t21:
            t21[s.replace("_tl", "_musd")] = (t21[s] / t21.usd_try / 1e6).round(2)
    t21.reindex(columns=sira).sort_values(["kod", "yil"]).to_csv(
        os.path.join(a.out, "tuik_yshi_nace21_2025.csv"), index=False, float_format="%.6g")

    # Doğrulama özeti
    c = t2[(t2.kod == "C") | (t2.kod.str.fullmatch(r"\d\d") & t2.kod.between("10", "33"))]
    imalat = t2[t2.kod.str.fullmatch(r"(1\d|2\d|3[0-3])")].groupby("yil")[
        ["girisim", "calisan", "faktor_maliyetiyle_kd_musd", "uretim_degeri_musd"]].sum()
    print("İmalat (NACE 10–33 bölümleri toplamı):")
    print(imalat.tail(4).round(0).to_string())
    sinif = t2[t2.kod.str.fullmatch(r"(1\d|2\d|3[0-3])\.\d\d") & (t2.yil == "2024")]
    print("2024'te verisi olan C sınıfı:", sinif.kod.nunique(), "| gizli KD:",
          sinif.faktor_maliyetiyle_kd_tl.isna().sum())
    print("USD/TRY:", kur.tail(3).round(3).to_dict())
    del c


if __name__ == "__main__":
    main()
