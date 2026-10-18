"""Faz 2C — Makro-finansal tampon: çıkış ilanı şokuna karşı rezerv ihtiyacı ve zamanlama kapısı.

Veri: TCMB EVDS3 (evds3.py; anlık görüntü girdi/evds3/):
  TP.AB.TOPLAM      resmî rezerv varlıkları, haftalık (milyon $)
  TP.REZVARPD.K1    IMF rezerv şablonu I.A: resmî rezerv varlıkları, aylık
  TP.DOVVARNC.K1    II.1: 12 ay içinde vadesi gelen döviz kredi, menkul kıymet ve mevduat çıkışları
  TP.DOVVARNC.K14   II.2: döviz swapları ve vadeli işlemler, kısa pozisyon
  TP.DOVVARNC.K23   II.3: diğer (altın swapları dahil)
  TP.DOVVARSB.K1    III.1: şarta bağlı döviz yükümlülükleri (bankaların TCMB'deki zorunlu karşılıkları)
  Şablon neti = I.A + II.1 + II.2 + II.3 + III.1: 12 ay içindeki bütün döviz çıkışları, swaplar ve zorunlu
  karşılıklar düşülmüş en sıkı ölçü. Piyasanın "swap hariç net rezerv"i (9.10.2026'da ≈$44 mlr) buna yakındır.
Şok: ilanı izleyen 12 ayda rezervden çıkış, iki senaryo (kurallı ilan: ITA yolu güvenilir, dondurma kararı;
  düzensiz: anlaşmasız çıkış beklentisi). Kalem bazında varsayımlar SOK'ta, kaynakları yorumda `[H]`. Kalibrasyon:
  Mart–Mayıs 2025 ve Şubat–Nisan 2026 stres dönemlerinde TCMB 4–8 haftada $45–65 mlr harcadı; net döviz talebinin
  %70'i yurt dışı yerleşiklerden geldi (TCMB Enflasyon Raporu 2026-II, Kutu 2.1).
Gerekli tampon = 12 aylık çıkışın üst ucu + taban (TCMB'nin net rezervi sıfıra yaklaşmadan müdahale edebilmesi).
Çıktı: veri/hazirlik_makro_rezerv.csv (zaman serisi), veri/hazirlik_makro_tampon.csv (kalemler, ihtiyaç, açık, süre).
"""

import argparse
import os

import pandas as pd

import evds3
import yollar

SABLON = {"TP.REZVARPD.K1": "brut", "TP.DOVVARNC.K1": "cikis_12ay", "TP.DOVVARNC.K14": "swap_vadeli",
          "TP.DOVVARNC.K23": "diger_altin_swap", "TP.DOVVARSB.K1": "sarta_bagli"}
# Şok kalemleri: (taban büyüklük $ mlr, kurallı alt–üst oran, düzensiz alt–üst oran, açıklama)
SOK = [
    ("Yurt dışı yerleşiklerin TL varlık ve taşıma pozisyonu satışı", 80, (0.20, 0.30), (0.45, 0.55),
     "Taban ≈$80 mlr TL varlık ve taşıma pozisyonu (piyasa tahmini) `[T]`; satış oranı `[H]`"),
    ("Yerleşiklerin dolarizasyonu (rezerve yansıyan yarısı)", 350 * 0.5, (0.02, 0.04), (0.05, 0.08),
     "TL mevduatı ≈$350 mlr; dönüşüm oranı `[H]`; rezerve yansıyan pay 0,5 `[H]`"),
    ("Dış borç çevirme oranında düşüş", 248.1, (0.02, 0.03), (0.05, 0.07),
     "Kalan vadeye göre kısa vadeli dış borç $248,1 mlr (Temmuz 2026) `[V]`; kayıp oranı `[H]`"),
    ("Geçiş yılında cari açığın genişlemesi", 1.0, (5, 10), (10, 15),
     "$ mlr; anlaşmasız çıkışta ihracat kaybı ve belirsizlik `[H]`"),
]
TABAN = 20          # $ mlr: müdahale kapasitesi için korunacak asgari net rezerv `[H]`
K_TARIHLERI = {"T2028": "2026-11-30", "T2029": "2027-03-31"}   # 02b §5.8: iç karar ve AB'ye resmî bildirim
BUGUN = "2026-10-18"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=yollar.VERI)
    a = ap.parse_args()

    s = evds3.veri(list(SABLON), ["last"] * len(SABLON), 5, bas="01-01-2023", son="31-12-2026").rename(columns=SABLON)
    s.index = pd.PeriodIndex(s.index, freq="M").to_timestamp(how="end").normalize()
    s = s.dropna() / 1e3
    s["sablon_neti"] = s[list(SABLON.values())].sum(axis=1)
    h = evds3.veri(["TP.AB.TOPLAM"], ["last"], 3, bas="01-01-2024", son="31-12-2026")
    h.index = pd.to_datetime(h.index, format="%d-%m-%Y")
    h = (h["TP.AB.TOPLAM"] / 1e3).rename("brut_haftalik").dropna()
    rezerv = pd.concat([h, s[["brut", "sablon_neti"]].rename(columns={"brut": "brut_aylik"})], axis=1, sort=True)
    rezerv.index.name = "tarih"
    rezerv.round(2).to_csv(os.path.join(a.out, "hazirlik_makro_rezerv.csv"))

    son_net = s.sablon_neti.iloc[-1]
    son_ay = s.index[-1]
    # birikim hızı: (i) güçlü giriş dönemi Mart→Ağustos 2026; (ii) Ocak 2023'ten bu yana ortalama
    guclu = (s.sablon_neti.loc["2026-08"].iloc[0] - s.sablon_neti.loc["2026-03"].iloc[0]) / 5
    ortalama = (son_net - s.sablon_neti.iloc[0]) / ((son_ay.year - s.index[0].year) * 12 + son_ay.month - s.index[0].month)
    satirlar = []
    for ad, taban, kur, duz, aciklama in SOK:
        satirlar.append(dict(kalem=ad, kurallı_alt=taban * kur[0], kurallı_ust=taban * kur[1],
                             duzensiz_alt=taban * duz[0], duzensiz_ust=taban * duz[1], aciklama=aciklama))
    t = pd.DataFrame(satirlar)
    toplam = t[["kurallı_alt", "kurallı_ust", "duzensiz_alt", "duzensiz_ust"]].sum()
    t = pd.concat([t, pd.DataFrame([dict(kalem="Toplam 12 aylık çıkış", **toplam, aciklama="")])], ignore_index=True)
    ek = []
    for sen, ust in (("kurallı", toplam["kurallı_ust"]), ("duzensiz", toplam["duzensiz_ust"])):
        gerekli = ust + TABAN
        acik = max(0.0, gerekli - son_net)
        satir = dict(kalem=f"Gerekli net rezerv ({sen})", deger=gerekli, mevcut=son_net, acik=acik,
                     ay_guclu_giris=acik / guclu, ay_ortalama=acik / ortalama)
        for takvim, k in K_TARIHLERI.items():
            ay_k = (pd.Timestamp(k).year - pd.Timestamp(BUGUN).year) * 12 + pd.Timestamp(k).month - pd.Timestamp(BUGUN).month
            satir[f"{takvim}_K_ay"] = ay_k
            satir[f"{takvim}_guclu_girisle_kapanir"] = acik <= guclu * ay_k
        ek.append(satir)
    e = pd.DataFrame(ek)
    t.round(1).to_csv(os.path.join(a.out, "hazirlik_makro_tampon.csv"), index=False)
    e.round(2).to_csv(os.path.join(a.out, "hazirlik_makro_kapi.csv"), index=False)
    print(t.round(1).to_string(index=False))
    print(e.round(1).to_string(index=False))
    print(f"Son şablon neti {son_ay:%Y-%m}: {son_net:.1f}; birikim hızı güçlü {guclu:.1f}, ortalama {ortalama:.1f} $ mlr/ay")


if __name__ == "__main__":
    main()
