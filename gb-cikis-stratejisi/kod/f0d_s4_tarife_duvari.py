"""Faz 0 (revizyon) — Anlaşmasız çıkışın (S4) statik tarife duvarı.

T'de yeni bir anlaşma yoksa GB kapsamındaki ticaret DTÖ en çok kayrılan ulus (MFN)
tarifelerine geçer. Bu betik, 2025 ticaret akımlarına 2026 MFN oranlarını uygulayarak
iki yönde ödenecek gümrük vergisini hesaplar:
  - TR → AB: AB'nin CN 2026 konvansiyonel oranları × AB'nin Türkiye'den ithalatı (Comext 2025)
  - AB → TR: Türkiye'nin 2026 "Diğer Ülkeler" oranları × AB'nin Türkiye'ye ihracatı.
    İGV dahil varyant: mevcut İGV Kararı değişmezse AB menşeli mallar da İGV'ye tabi olur.
    İGV hariç varyant: yalnızca İthalat Rejimi Kararı MFN oranı (OGT ile uyumlu).

Oran eşleştirmesi CN8 düzeyindedir. GTİP'in ilk 8 hanesi CN8'e karşılık gelir; 12 haneli
satırların basit ortalaması alınır. CN8 eşleşmesi yoksa HS6 ortalaması kullanılır.
AB'nin spesifik ve bileşik vergilerinde yalnızca ad valorem kısım alınır (spesifik kısım
ve tarım bileşeni dahil edilmez; tarım ve İTÜ'de vergi eksik tahmin edilir).

Statik ilk tur tutardır: ticaret hacmi, fiyat ve kaynak değişimi tepkisi içermez; refah
maliyeti değildir. Kapsam varyantları:
  (i)  yalnızca 1/95 kapsamı (GB + İTÜ); tarım (1/98) ve AKÇT anlaşmaları sürer
  (ii) (i) + 1/98 tarım tercihleri de kaybedilir
AKÇT ürünleri iki varyantta da kapsam dışıdır: 1996 AKÇT Anlaşması GB'den bağımsız olarak
sürer ve çelikte belirleyici olan AB kota rejimidir (Tüzük 2026/1384).

Kısmi denge hacim etkisi (statik, sınıf kartlarındaki sektörel σ yerine tek σ):
  ΔX = X × [(1 + τ)^(−σ) − 1],  σ ∈ {3, 5, 8} (P10 / P50 / P90 aralığı için) [T]
"""

import argparse
import os

import pandas as pd

SIGMALAR = (3, 5, 8)


def ab_oranlari(dosya):
    x = pd.read_csv(dosya, dtype={"cn8": str, "hs6": str})
    x = x[x.adval_rate.notna()]
    return x.set_index("cn8").adval_rate, x.groupby("hs6").adval_rate.mean()


def tr_oranlari(dosya, sutun):
    x = pd.read_csv(dosya, dtype={"gtip12": str, "hs6": str})
    x = x[~x.in_tgtc_only & x[sutun].notna()]
    x["cn8"] = x.gtip12.str[:8]
    return x.groupby("cn8")[sutun].mean(), x.groupby("hs6")[sutun].mean()


def eslestir(kodlar, cn8_oran, hs6_oran):
    oran = kodlar.map(cn8_oran)
    kaynak = pd.Series("CN8", index=kodlar.index).where(oran.notna())
    eksik = oran.isna()
    oran[eksik] = kodlar[eksik].str[:6].map(hs6_oran)
    kaynak[eksik & oran.notna()] = "HS6"
    return oran, kaynak


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()

    m = pd.read_csv(os.path.join(a.out, "cn2025_nace_rejim.csv"), dtype={"cn8": str, "nace2": str})
    m = m[m.cn8.str.fullmatch(r"\d{8}") & m.rejim.isin(["GB", "ITU", "TARIM", "AKCT"])].copy()
    m["bolum"] = m.nace2.str[:2]

    ab8, ab6 = ab_oranlari(os.path.join(a.out, "tarife_ab_cn2026_cn8.csv"))
    tr_dosya = os.path.join(a.out, "tarife_tr_2026_gtip12.csv")
    tri8, tri6 = tr_oranlari(tr_dosya, "mfn_igv_emy")
    trm8, trm6 = tr_oranlari(tr_dosya, "mfn_rate")
    m["oran_ab"], m["kaynak_ab"] = eslestir(m.cn8, ab8, ab6)
    m["oran_tr_igv"], m["kaynak_tr"] = eslestir(m.cn8, tri8, tri6)
    m["oran_tr_mfn"], _ = eslestir(m.cn8, trm8, trm6)

    satirlar = []
    for varyant, kapsam in (("i_GB_ITU", ["GB", "ITU"]), ("ii_GB_ITU_TARIM", ["GB", "ITU", "TARIM"])):
        k = m[m.rejim.isin(kapsam)]
        for yon, deger, oran in (("TR->AB", "tr_ihr_ab", "oran_ab"),
                                 ("AB->TR (İGV dahil)", "tr_ith_ab", "oran_tr_igv"),
                                 ("AB->TR (İGV hariç)", "tr_ith_ab", "oran_tr_mfn")):
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

    k = m[m.rejim.isin(["GB", "ITU"])].copy()
    k = k.assign(v_ab=k.tr_ihr_ab * k.oran_ab.fillna(0) / 100,
                 v_tr=k.tr_ith_ab * k.oran_tr_igv.fillna(0) / 100,
                 v_tr_mfn=k.tr_ith_ab * k.oran_tr_mfn.fillna(0) / 100,
                 dx5=k.tr_ihr_ab * ((1 + k.oran_ab.fillna(0) / 100) ** -5 - 1))

    def topla(anahtar):
        t = k.groupby(anahtar).agg(
            tr_ab_ihracat_meur=("tr_ihr_ab", lambda s: s.sum() / 1e6),
            ab_vergisi_meur=("v_ab", lambda s: s.sum() / 1e6),
            ihracat_degisimi_sigma5_meur=("dx5", lambda s: s.sum() / 1e6),
            ab_tr_ihracat_meur=("tr_ith_ab", lambda s: s.sum() / 1e6),
            tr_vergisi_igv_dahil_meur=("v_tr", lambda s: s.sum() / 1e6),
            tr_vergisi_igv_haric_meur=("v_tr_mfn", lambda s: s.sum() / 1e6),
        )
        t["ab_oran_yuzde"] = 100 * t.ab_vergisi_meur / t.tr_ab_ihracat_meur
        t["tr_oran_igv_dahil_yuzde"] = 100 * t.tr_vergisi_igv_dahil_meur / t.ab_tr_ihracat_meur
        t["tr_oran_igv_haric_yuzde"] = 100 * t.tr_vergisi_igv_haric_meur / t.ab_tr_ihracat_meur
        return t.reset_index().sort_values("ab_vergisi_meur", ascending=False)

    bol = topla("bolum")
    bol.round(2).to_csv(os.path.join(a.out, "s4_tarife_duvari_bolum.csv"), index=False)
    sinif = topla("nace2")
    sinif = sinif[sinif.nace2.str.fullmatch(r"\d\d\.\d\d")]
    sinif.round(2).to_csv(os.path.join(a.out, "s4_tarife_duvari_sinif.csv"), index=False)

    agirlik = lambda s, d: (m.loc[m[s] == "CN8", d].sum() / m[d].sum())  # noqa: E731
    print(f"Oran eşleşmesi CN8 düzeyinde: TR→AB değerinin %{100 * agirlik('kaynak_ab', 'tr_ihr_ab'):.1f}'i, "
          f"AB→TR değerinin %{100 * agirlik('kaynak_tr', 'tr_ith_ab'):.1f}'i")
    print(ozet.round(2).to_string(index=False))
    print(bol.head(10).round(1).to_string(index=False))
    print(sinif.head(12).round(1).to_string(index=False))


if __name__ == "__main__":
    main()
