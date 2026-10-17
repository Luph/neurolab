"""Faz 0 (revizyon) — Anlaşmasız çıkışın (S4) statik tarife duvarı.

T'de yeni bir anlaşma yoksa GB kapsamındaki ticaret DTÖ en çok kayrılan ulus (MFN)
tarifelerine geçer. Bu betik, 2025 ticaret akımlarına MFN oranlarını uygulayarak
iki yönde ödenecek gümrük vergisini hesaplar:
  - TR → AB: AB'nin MFN oranları × AB'nin Türkiye'den ithalatı (Comext 2025)
  - AB → TR: Türkiye'nin MFN oranları (İGV dahil) × AB'nin Türkiye'ye ihracatı

Statik ilk tur tutardır: ticaret hacmi, fiyat ve kaynak değişimi tepkisi içermez;
gerçek refah maliyeti değildir. Kapsam varyantları:
  (i)  yalnızca 1/95 kapsamı (GB + İTÜ); tarım (1/98) ve AKÇT anlaşmaları sürer
  (ii) (i) + 1/98 tarım tercihleri de kaybedilir
AKÇT ürünleri iki varyantta da kapsam dışıdır: 1996 AKÇT Anlaşması GB'den bağımsız
olarak sürer ve çelikte belirleyici olan AB kota rejimidir (Tüzük 2026/1384).

Tarife kaynağı: WITS TRAINS, HS6 basit ortalama (EU = 918, TUR = 792). AB'de ad valorem
olmayan satırlar için WITS AVE tahmini yoksa satır kapsam dışı kalır ve kapsam oranı
raporlanır. Türkiye'nin MFN oranları İGV'yi içerir; "İGV hariç" varyantında Türkiye'nin
temel oranları OGT'ye eşit olduğundan AB'nin MFN oranları kullanılır.

Kısmi denge hacim etkisi (statik, sınıf kartlarındaki sektörel σ yerine tek σ):
  ΔX = X × [(1 + τ)^(−σ) − 1],  σ ∈ {3, 5, 8} (P10 / P50 / P90 aralığı için) [T]
"""

SIGMALAR = (3, 5, 8)

import argparse
import os

import pandas as pd


def tarife(dosya):
    x = pd.read_csv(dosya, dtype={"PRODUCTCODE": str})
    return x.set_index("PRODUCTCODE").OBS_VALUE.rename("oran")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ab-tarife", required=True, help="WITS AB MFN HS6 CSV")
    ap.add_argument("--tr-tarife", required=True, help="WITS Türkiye MFN (İGV dahil) HS6 CSV")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()

    m = pd.read_csv(os.path.join(a.out, "cn2025_nace_rejim.csv"), dtype={"cn8": str, "nace2": str})
    m = m[m.cn8.str.fullmatch(r"\d{8}") & m.rejim.isin(["GB", "ITU", "TARIM", "AKCT"])]
    m["hs6"] = m.cn8.str[:6]
    m["bolum"] = m.nace2.str[:2]
    ab, tr = tarife(a.ab_tarife), tarife(a.tr_tarife)
    m["oran_ab"] = m.hs6.map(ab)
    m["oran_tr"] = m.hs6.map(tr)

    satirlar = []
    for varyant, kapsam in (("i_GB_ITU", ["GB", "ITU"]), ("ii_GB_ITU_TARIM", ["GB", "ITU", "TARIM"])):
        k = m[m.rejim.isin(kapsam)]
        for yon, deger, oran in (("TR->AB", "tr_ihr_ab", "oran_ab"),
                                 ("AB->TR (İGV dahil)", "tr_ith_ab", "oran_tr"),
                                 ("AB->TR (İGV hariç)", "tr_ith_ab", "oran_ab")):
            g = k[k[oran].notna()]
            rec = dict(varyant=varyant, yon=yon,
                       ticaret_meur=k[deger].sum() / 1e6,
                       kapsanan_ticaret_meur=g[deger].sum() / 1e6,
                       vergi_meur=(g[deger] * g[oran] / 100).sum() / 1e6)
            for s in SIGMALAR:
                rec[f"hacim_degisimi_meur_sigma{s}"] = (g[deger] * ((1 + g[oran] / 100) ** (-s) - 1)).sum() / 1e6
            satirlar.append(rec)
    ozet = pd.DataFrame(satirlar)
    ozet["kapsama_orani"] = ozet.kapsanan_ticaret_meur / ozet.ticaret_meur
    ozet["agirlikli_oran_yuzde"] = 100 * ozet.vergi_meur / ozet.kapsanan_ticaret_meur
    ozet.round(3).to_csv(os.path.join(a.out, "s4_tarife_duvari_ozet.csv"), index=False)

    k = m[m.rejim.isin(["GB", "ITU"])]
    k = k.assign(v_ab=k.tr_ihr_ab * k.oran_ab / 100, v_tr=k.tr_ith_ab * k.oran_tr / 100,
                 dx5=k.tr_ihr_ab * ((1 + k.oran_ab / 100) ** -5 - 1))

    def topla(anahtar):
        t = k.groupby(anahtar).agg(
            tr_ab_ihracat_meur=("tr_ihr_ab", lambda s: s.sum() / 1e6),
            ab_vergisi_meur=("v_ab", lambda s: s.sum() / 1e6),
            ihracat_degisimi_sigma5_meur=("dx5", lambda s: s.sum() / 1e6),
            ab_tr_ihracat_meur=("tr_ith_ab", lambda s: s.sum() / 1e6),
            tr_vergisi_igv_dahil_meur=("v_tr", lambda s: s.sum() / 1e6),
        )
        t["ab_oran_yuzde"] = 100 * t.ab_vergisi_meur / t.tr_ab_ihracat_meur
        t["tr_oran_igv_dahil_yuzde"] = 100 * t.tr_vergisi_igv_dahil_meur / t.ab_tr_ihracat_meur
        return t.reset_index().sort_values("ab_vergisi_meur", ascending=False)

    bol = topla("bolum")
    bol.round(2).to_csv(os.path.join(a.out, "s4_tarife_duvari_bolum.csv"), index=False)
    sinif = topla("nace2")
    sinif = sinif[sinif.nace2.str.fullmatch(r"\d\d\.\d\d")]
    sinif.round(2).to_csv(os.path.join(a.out, "s4_tarife_duvari_sinif.csv"), index=False)

    print(ozet.round(2).to_string(index=False))
    print(bol.head(12).round(1).to_string(index=False))
    print(sinif.head(15).round(1).to_string(index=False))


if __name__ == "__main__":
    main()
