"""Faz 0 (revizyon) — Uygulanan tarifeler: Türkiye 2026 (GTİP12, İGV dahil) ve AB CN 2026 (CN8).

Kaynaklar (kimlik doğrulamasız):
  Türkiye: Ticaret Bakanlığı konsolide ekleri — İthalat Rejimi Kararı (3350) listeleri I–IV,
           İGV Kararı (3351) ekleri ve 2026 Türk Gümrük Tarife Cetveli (tarife_tr.py)
  AB:      Uyg. Tüzüğü (AB) 2025/1926 Ek I, Yayın Ofisi Formex 4 XML (tarife_ab.py)

Çıktılar:
  veri/tarife_tr_2026_gtip12.csv  MFN ("DÜ" sütunu), İGV, balık ek mali yükümlülüğü ve toplam
  veri/tarife_ab_cn2026_cn8.csv   konvansiyonel vergi metni, ad valorem kısım ve vergi türü
"""

import argparse
import os

import tarife_ab
import tarife_tr

TR_SUTUN = ["gtip12", "hs6", "list", "law474_rate", "mfn_rate", "mfn_text", "igv_rate", "emy_rate_IV",
            "mfn_igv_emy", "in_tgtc_only", "in_irk_only"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=os.path.expanduser("~/.cache/gb_cikis"))
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    zipler = os.path.join(a.cache, "tarife_tr")
    os.makedirs(zipler, exist_ok=True)

    yollar = {k: os.path.join(zipler, k + ".zip") for k in tarife_tr.PAGES}
    if not all(os.path.exists(p) for p in yollar.values()):
        yollar = tarife_tr.download_zips(zipler)
    tr = tarife_tr.build(yollar, os.path.join(a.cache, "tarife_tr_2026_tam.csv"))
    tr[TR_SUTUN].to_csv(os.path.join(a.out, "tarife_tr_2026_gtip12.csv"), index=False)

    ab = tarife_ab.fetch_cn(zip_path=os.path.join(a.cache, "cn2026_fmx4.zip"))
    ab[["cn8", "hs6", "duty_text", "adval_rate", "duty_type"]].to_csv(
        os.path.join(a.out, "tarife_ab_cn2026_cn8.csv"), index=False)

    d = tr[~tr.in_tgtc_only]
    print("Türkiye 2026:", len(d), "GTİP12 satırı; İGV'li satır:", int((d.igv_rate > 0).sum()),
          "| satır ortalaması MFN", round(d.mfn_rate.mean(), 2), "MFN+İGV+EMY", round(d.mfn_igv_emy.mean(), 2))
    print("AB CN 2026:", len(ab), "CN8 satırı;", ab.duty_type.value_counts().to_dict())


if __name__ == "__main__":
    main()
