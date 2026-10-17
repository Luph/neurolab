"""Faz 0 (revizyon) — TÜİK bölgesel girişim sayıları, TÜFE ağırlıkları ve sanayi üretim endeksi.

Kaynak: TÜİK Dağıtım Yönetim Sistemi
  DF_BR_FAALIYET_BUYUKLUK_GIRISIM_TR_IBBS1_2_V1: İş kayıtları, NACE Rev. 2 × büyüklük × İBBS-1/2, 2009–2024
  DF_TUFE_SDMX_TT04: TÜFE sepeti ve ağırlıkları (2025=100, COICOP 2018)
  DF_SANAYI_URETIM_ENDEKS_ALT_C: Sanayi üretim endeksi (2021=100), NACE Rev. 2 sınıf düzeyi, aylık

Çıktılar:
  veri/tuik_girisim_ibbs2_nace2.csv  (son yıl; İBBS-2 × NACE sınıfı × büyüklük grubu)
  veri/tuik_tufe_agirlik_2026.csv    (COICOP 2018 düzeylerine göre 2026 ağırlıkları)
  veri/tuik_sue_sinif_aylik.csv      (2023'ten bu yana; mevsim ve takvim etkisinden arındırılmış
                                      endeks ve takvim etkisinden arındırılmış yıllık değişim)
"""

import argparse
import os

import pandas as pd

import tuik

BUYUKLUK = {"0": "toplam", "1T9": "g_1_9", "10T49": "g_10_49", "50T249": "g_50_249", "GE250": "g_250p"}


def nace_kodu(s):
    return s.str.replace(r"^([A-U])(\d\d)(\d)?(\d)?$",
                         lambda m: m.group(2) + ("." + m.group(3) + (m.group(4) or "") if m.group(3) else ""),
                         regex=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=os.path.expanduser("~/.cache/gb_cikis"))
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    os.makedirs(a.cache, exist_ok=True)

    f = tuik.indir_csv("DF_BR_FAALIYET_BUYUKLUK_GIRISIM_TR_IBBS1_2_V1",
                       os.path.join(a.cache, "tuik_DF_BR_FAALIYET_BUYUKLUK_GIRISIM_TR_IBBS1_2_V1.csv"))
    sut = ["REF_AREA", "ACTIVITY_NACE_REV2", "BUYUKLUK_GRUP", "IBBS_DUZEY", "TIME_PERIOD", "OBS_VALUE",
           "CONF_STATUS"]
    parcalar = []
    for p in pd.read_csv(f, dtype=str, usecols=sut, chunksize=400_000):
        p = p[p.IBBS_DUZEY.eq("2")]
        parcalar.append(p)
    b = pd.concat(parcalar)
    son = b.TIME_PERIOD.astype(int).max()
    b = b[b.TIME_PERIOD.astype(int).eq(son)].copy()
    b["kod"] = nace_kodu(b.ACTIVITY_NACE_REV2)
    b = b[b.kod.str.fullmatch(r"(0[5-9]|[1-2]\d|3[0-3]|35|38)\.\d\d")]
    b["deger"] = pd.to_numeric(b.OBS_VALUE, errors="coerce").where(b.CONF_STATUS.ne("C"))
    t = b.pivot_table(index=["REF_AREA", "kod"], columns="BUYUKLUK_GRUP", values="deger", aggfunc="first")
    t = t.rename(columns=BUYUKLUK).reset_index().rename(columns={"REF_AREA": "ibbs2"})
    t.insert(2, "yil", son)
    t.to_csv(os.path.join(a.out, "tuik_girisim_ibbs2_nace2.csv"), index=False, float_format="%.0f")
    print(f"İBBS-2 × NACE sınıfı girişim sayıları ({son}):", len(t), "satır;",
          t.ibbs2.nunique(), "bölge;", t.kod.nunique(), "sınıf")

    w = pd.read_csv(tuik.indir_csv("DF_TUFE_SDMX_TT04", os.path.join(a.cache, "tuik_DF_TUFE_SDMX_TT04.csv")),
                    dtype=str)
    yil = w.TIME_PERIOD.astype(int).max()
    w = w[w.TIME_PERIOD.astype(int).eq(yil) & w.SINIFLAMA_DUZEYI.isin(["2", "3", "4", "5"])]
    w = w.assign(agirlik=pd.to_numeric(w.OBS_VALUE, errors="coerce"))[["SINIFLAMA_DUZEYI", "COICOP_2018", "agirlik"]]
    w.columns = ["duzey", "coicop_2018", "agirlik_yuzde"]
    w.insert(0, "yil", yil)
    w.to_csv(os.path.join(a.out, "tuik_tufe_agirlik_2026.csv"), index=False)
    print(f"TÜFE ağırlıkları ({yil}):", w.groupby("duzey").agirlik_yuzde.agg(["count", "sum"]).round(2).to_dict())

    sut = ["ACTIVITY_NACE_REV2", "SEASONAL_ADJUST", "DEGISIM_TUR", "TIME_PERIOD", "OBS_VALUE"]
    s = pd.read_csv(tuik.indir_csv("DF_SANAYI_URETIM_ENDEKS_ALT_C",
                                   os.path.join(a.cache, "tuik_DF_SANAYI_URETIM_ENDEKS_ALT_C.csv")),
                    dtype=str, usecols=sut)
    s = s[s.ACTIVITY_NACE_REV2.str.fullmatch(r"[B-E]\d{4}") & (s.TIME_PERIOD >= "2023-01")]
    s["kod"] = nace_kodu(s.ACTIVITY_NACE_REV2)
    s["seri"] = s.SEASONAL_ADJUST + s.DEGISIM_TUR
    s = s[s.seri.isin(["Y1", "W4"])]  # Y1: arındırılmış endeks; W4: takvim etkisinden arındırılmış yıllık %
    s["deger"] = pd.to_numeric(s.OBS_VALUE, errors="coerce")
    t = s.pivot_table(index=["kod", "TIME_PERIOD"], columns="seri", values="deger", aggfunc="first")
    t = t.rename(columns={"Y1": "endeks_mta", "W4": "yillik_degisim_ta_yuzde"}).reset_index()
    t = t.rename(columns={"TIME_PERIOD": "ay"})
    t.to_csv(os.path.join(a.out, "tuik_sue_sinif_aylik.csv"), index=False, float_format="%.2f")
    print("Sanayi üretim endeksi:", t.kod.nunique(), "sınıf;", t.ay.min(), "–", t.ay.max())


if __name__ == "__main__":
    main()
