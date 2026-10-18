"""Faz 2C — Karar öncesi hamlelerin puanlanması ve öncelik sırası.

Girdi: veri/hazirlik_hamleler.csv (elle derlendi; her satırın gerekçesi ve kaynağı 02c_hazirlik.md'de).
Puan (şeffaf, toplamsal; en fazla 10):
  çıkış değeri × 2     Yüksek 3, Orta 2, Düşük 1
  pişmanlıksızlık      (çıkış olmazsa değeri) Yüksek 2, Orta 1, Düşük 0, Negatif −2
  görünürlük           Düşük +1, Orta 0, Yüksek −1
  hukuki durum         Uygun 0, Gri −1 (aykırı hamleler tabloda yok; kırmızı listede)
  aciliyet             +1: hazırlık süresinin üst sınırı T2029'a kalan süreyi (26 ay) aşıyor ya da kesin son tarih
                       Haziran 2027'den önce
Öncelik: A ≥ 9 (hemen başlat), B 7–8 (karar öncesi başlat), C ≤ 6 (fırsat oldukça).
Duyarlılık: çıkış değeri ×1 (×2 yerine) ve görünürlük ×2 ağırlıklarıyla puanlar; sıra korelasyonu ve en iyi 11'in örtüşmesi.
Çıktı: veri/hazirlik_hamleler_oncelik.csv; standart çıktıya Markdown tablosu ve duyarlılık özeti.
"""

import argparse
import os

import pandas as pd

import yollar

PUAN = {
    "cikis_degeri": {"Yüksek": 6, "Orta": 4, "Düşük": 2},
    "pismanliksiz": {"Yüksek": 2, "Orta": 1, "Düşük": 0, "Negatif": -2},
    "gorunurluk": {"Düşük": 1, "Orta": 0, "Yüksek": -1},
    "hukuk": {"Uygun": 0, "Gri": -1},
}
KALAN_T2029 = 26


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=yollar.VERI)
    a = ap.parse_args()
    h = pd.read_csv(os.path.join(a.out, "hazirlik_hamleler.csv"))
    for k, eslem in PUAN.items():
        bilinmeyen = set(h[k]) - set(eslem)
        assert not bilinmeyen, (k, bilinmeyen)
    h["aciliyet"] = ((h.sure_ay_ust >= KALAN_T2029) |
                     (h.kesin_son_tarih.fillna("").astype(str).between("2026-01-01", "2027-06-30"))).astype(int)
    h["puan"] = sum(h[k].map(e) for k, e in PUAN.items()) + h.aciliyet
    h["oncelik"] = pd.cut(h.puan, [-99, 6, 8, 99], labels=["C", "B", "A"]).astype(str)
    ortak = h.pismanliksiz.map(PUAN["pismanliksiz"]) + h.hukuk.map(PUAN["hukuk"]) + h.aciliyet
    h["puan_cikis_x1"] = ortak + h.cikis_degeri.map(PUAN["cikis_degeri"]) / 2 + h.gorunurluk.map(PUAN["gorunurluk"])
    h["puan_gorunurluk_x2"] = ortak + h.cikis_degeri.map(PUAN["cikis_degeri"]) + 2 * h.gorunurluk.map(PUAN["gorunurluk"])
    h = h.sort_values(["oncelik", "puan", "no"], ascending=[True, False, True])
    h.to_csv(os.path.join(a.out, "hazirlik_hamleler_oncelik.csv"), index=False)
    hukuk_sutunu = h.hukuk.nunique() > 1          # hepsi "Uygun" ise sütun basılmaz
    print("| No | Çerçeve | Hamle | Görünürlük |" + (" Hukuk |" if hukuk_sutunu else "") +
          " Çıkış olmasa | Çıkışta | Süre (ay) | Puan | Öncelik |")
    print("|---" * (9 + hukuk_sutunu) + "|")
    for r in h.itertuples():
        print(f"| {r.no} | {r.cerceve} | {r.hamle} | {r.gorunurluk} |" + (f" {r.hukuk} |" if hukuk_sutunu else "") +
              f" {r.pismanliksiz} | {r.cikis_degeri} | {r.sure_ay_alt}–{r.sure_ay_ust} | {r.puan} | **{r.oncelik}** |")
    print(h.groupby("oncelik").size().to_dict())
    n_a = (h.oncelik == "A").sum()
    a_kume = set(h.no[h.oncelik == "A"])
    for k in ("puan_cikis_x1", "puan_gorunurluk_x2"):
        ilk = set(h.sort_values([k, "puan"], ascending=False).no.head(n_a))
        print(f"duyarlılık {k}: Spearman {h.puan.corr(h[k], method='spearman'):.2f}; "
              f"en iyi {n_a} örtüşme {len(ilk & a_kume)}/{n_a}")


if __name__ == "__main__":
    main()
