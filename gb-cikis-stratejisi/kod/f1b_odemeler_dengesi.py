"""Faz 1 — Makro tablo ve cari denge ayrıştırması.

Kaynaklar (kimlik doğrulamasız):
  - TCMB EVDS3 (evds3.py): ödemeler dengesi ayrıntılı sunum (BPM6), altın ve enerji hariç cari
    denge, GSYH (harcama yöntemi, cari fiyatlar), döviz kurları, TÜFE bazlı reel efektif kur,
    uluslararası yatırım pozisyonu
  - TÜİK DF_UHTI_HIZMET_COGRAFI_C: hizmet ticareti, ortak ülke × hizmet türü, 2016–2025 (milyon $);
    "W1" kodu (etiketi "Rest of the World") dünya toplamıdır: 2025 dengesi ödemeler dengesindeki
    hizmet dengesine eşittir

Çıktılar:
  veri/teshis_odemeler_dengesi.csv       yıllık: cari denge bileşenleri, altın/enerji hariç denge,
                                         finansman, GSYH (ABD doları) ve GSYH'ye oranlar, reel kur
  veri/teshis_cari_denge_12ay.csv        aylık yıllıklandırılmış (12 aylık birikimli) cari denge
  veri/teshis_hizmet_ticareti_ab27.csv   hizmet ihracatı/ithalatı: AB27 ve toplam, türlere göre
Not: son yıl (2026) kısmi yıldır; yıllık tabloda "ay_sayisi" sütunu kaç ayın dahil olduğunu gösterir.
"""

import argparse
import os

import pandas as pd

import evds3
import tuik
import yollar

ODEME = {  # EVDS3 kodu -> sütun adı (milyon ABD doları)
    "TP.ODEAYRSUNUM6.Q1": "cari_denge",
    "TP.ODEAYRSUNUM6.Q4": "dis_ticaret_dengesi",
    "TP.ODEAYRSUNUM6.Q5": "mal_ihracati",
    "TP.ODEAYRSUNUM6.Q6": "mal_ithalati",
    "TP.ODEAYRSUNUM6.Q17": "parasal_olmayan_altin_net",
    "TP.ODEAYRSUNUM6.Q20": "hizmet_dengesi",
    "TP.ODEAYRSUNUM6.Q21": "hizmet_geliri",
    "TP.ODEAYRSUNUM6.Q29": "tasimacilik_net",
    "TP.ODEAYRSUNUM6.Q30": "tasimacilik_geliri",
    "TP.ODEAYRSUNUM6.Q41": "seyahat_net",
    "TP.ODEAYRSUNUM6.Q42": "seyahat_geliri",
    "TP.ODEAYRSUNUM6.Q68": "birincil_gelir_dengesi",
    "TP.ODEAYRSUNUM6.Q79": "dogrudan_yatirim_geliri_gideri",
    "TP.ODEAYRSUNUM6.Q85": "faiz_gideri",
    "TP.ODEAYRSUNUM6.Q92": "ikincil_gelir_dengesi",
    "TP.ODEAYRSUNUM6.Q101": "finans_hesabi",
    "TP.ODEAYRSUNUM6.Q108": "dyy_yukumluluk",
    "TP.ODEAYRSUNUM6.Q110": "dyy_sermaye_girisi",
    "TP.ODEAYRSUNUM6.Q113": "dyy_gayrimenkul",
    "TP.ODEAYRSUNUM6.Q103": "dyy_yurt_disi",
    "TP.ODEAYRSUNUM6.Q119": "portfoy_yukumluluk",
    "TP.ODEAYRSUNUM6.Q136": "diger_yatirimlar",
    "TP.ODEAYRSUNUM6.Q204": "rezerv_varliklar",
    "TP.ODEAYRSUNUM6.Q210": "net_hata_noksan",
    "TP.HARICCARIACIK.K7": "enerji_net",
    "TP.HARICCARIACIK.K8": "cari_denge_altin_haric",
    "TP.HARICCARIACIK.K9": "cari_denge_enerji_haric",
    "TP.HARICCARIACIK.K10": "cari_denge_altin_enerji_haric",
}
GSYH = {"TP.GSYIH20.BY.B1GQ": "gsyh", "TP.GSYIH20.BY.P51G": "gsso", "TP.GSYIH20.BY.P6": "ihracat_ua",
        "TP.GSYIH20.BY.P7": "ithalat_ua"}
KUR = {"TP.DK.USD.A.YTL": "usd_try", "TP.DK.EUR.A.YTL": "eur_try"}
REEL_KUR = {"TP.RK.T1.Y": "reel_kur_tufe", "TP.RK.T3.Y": "reel_kur_tufe_gelismis"}
UYP = {"TP.UYPUCAY.K1": "uyp_net", "TP.UYPUCAY.K41": "uyp_dyy_yukumluluk"}

AB27_ISO2 = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IE", "IT", "LV",
             "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE"]
HIZMET = {"S": "toplam", "SC": "tasimacilik", "SC3C2": "karayolu_yuk", "SD": "seyahat", "SE": "insaat",
          "SH": "fikri_mulkiyet", "SI": "bilgisayar_iletisim", "SJ": "diger_is_hizmetleri", "SA": "fason_imalat",
          "SB": "bakim_onarim"}


def yillik(kodlar, frekans=8, toplama=None, bas="01-01-1990"):
    t = [toplama or "sum"] * len(kodlar)
    w = evds3.veri(list(kodlar), t, frekans, bas=bas)
    w.index = w.index.astype(str).str[:4].astype(int)
    return w.rename(columns=kodlar)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=yollar.GIRDI)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    os.makedirs(a.cache, exist_ok=True)

    od = yillik(ODEME)
    aylik = evds3.veri(list(ODEME), ["sum"] * len(ODEME), 5, bas="01-01-2023").rename(columns=ODEME)
    son_yil = od.index.max()
    od["ay_sayisi"] = 12
    od.loc[son_yil, "ay_sayisi"] = int(aylik.index.astype(str).str.startswith(str(son_yil)).sum())

    g = yillik(GSYH)
    kur = yillik(KUR, toplama="avg")
    rk = yillik(REEL_KUR, frekans=8, toplama="avg")
    uyp = yillik(UYP, frekans=8, toplama="last")
    t = od.join([g, kur, rk, uyp], how="left")
    t = t[t.index >= 2002]
    # GSYH serisi bin TL; ABD doları karşılığı yıllık ortalama kurla
    t["gsyh_musd"] = t.gsyh / t.usd_try / 1e3
    t.loc[t.ay_sayisi < 12, "gsyh_musd"] = float("nan")
    for s in ["cari_denge", "cari_denge_altin_haric", "cari_denge_enerji_haric", "cari_denge_altin_enerji_haric",
              "dis_ticaret_dengesi", "hizmet_dengesi", "birincil_gelir_dengesi", "enerji_net",
              "parasal_olmayan_altin_net", "dyy_yukumluluk", "uyp_net"]:
        t[f"{s}_gsyh"] = 100 * t[s] / t.gsyh_musd
    t["gsso_gsyh"] = 100 * t.gsso / t.gsyh
    t.index.name = "yil"
    t.round(3).to_csv(os.path.join(a.out, "teshis_odemeler_dengesi.csv"))

    a12 = aylik[["cari_denge", "cari_denge_altin_haric", "cari_denge_enerji_haric", "cari_denge_altin_enerji_haric",
                 "enerji_net", "parasal_olmayan_altin_net"]].rolling(12).sum().dropna()
    a12.index.name = "ay"
    a12.round(0).to_csv(os.path.join(a.out, "teshis_cari_denge_12ay.csv"))

    h = pd.read_csv(tuik.indir_csv("DF_UHTI_HIZMET_COGRAFI_C",
                                   os.path.join(a.cache, "tuik_DF_UHTI_HIZMET_COGRAFI_C.csv")), dtype=str)
    h = h[h.HIZMET_TUR.isin(HIZMET) & h.EKONOMIK_GOSTERGE.isin(["13", "14"])]
    h["deger"] = pd.to_numeric(h.OBS_VALUE, errors="coerce")
    h["grup"] = h.TICARET_ORTAGI.map(lambda k: "ab27" if k in AB27_ISO2 else ("toplam" if k == "W1" else None))
    h = h[h.grup.notna()]
    hz = h.pivot_table(index=["TIME_PERIOD", "HIZMET_TUR"], columns=["EKONOMIK_GOSTERGE", "grup"],
                       values="deger", aggfunc="sum")
    hz.columns = [f"{'ihracat' if e == '13' else 'ithalat'}_{g}_musd" for e, g in hz.columns]
    hz = hz.reset_index().rename(columns={"TIME_PERIOD": "yil", "HIZMET_TUR": "kod"})
    hz.insert(2, "hizmet", hz.kod.map(HIZMET))
    for ak in ("ihracat", "ithalat"):
        hz[f"{ak}_ab27_payi"] = hz[f"{ak}_ab27_musd"] / hz[f"{ak}_toplam_musd"]
    hz["denge_ab27_musd"] = hz.ihracat_ab27_musd - hz.ithalat_ab27_musd
    hz.round(3).to_csv(os.path.join(a.out, "teshis_hizmet_ticareti_ab27.csv"), index=False)

    pd.set_option("display.width", 250)
    print(t[["ay_sayisi", "cari_denge", "dis_ticaret_dengesi", "hizmet_dengesi", "birincil_gelir_dengesi",
             "enerji_net", "parasal_olmayan_altin_net", "cari_denge_altin_enerji_haric", "gsyh_musd",
             "cari_denge_gsyh", "cari_denge_altin_enerji_haric_gsyh", "reel_kur_tufe", "gsso_gsyh"]]
          .round(1).to_string())
    print(a12.tail(4).to_string())
    print(hz[hz.yil.isin(["2019", "2024", "2025"])].round(2).to_string(index=False))


if __name__ == "__main__":
    main()
