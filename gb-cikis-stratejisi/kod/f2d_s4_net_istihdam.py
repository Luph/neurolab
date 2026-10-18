"""Faz 2 — S4'te NACE sınıfı düzeyinde net istihdam: ihracat kaybı ile ithal ikamesinin karşılaştırılması.

Faz 1'deki S4 risk istihdamı (207 bin) yalnızca ihracat tarafıydı. GB'den çıkışta Türkiye de AB mallarına
MFN uygular; AB'den ithalatın bir kısmı yurt içi üretime kayar. Bu betik iki tarafı sınıf düzeyinde netler.

  İhracat kaybı      ΔX_c = AB'ye ihracat_c × [(1 + τ_AB,c)^(−σ) − 1]          (Faz 0 S4 hesabı, CN8)
  AB ithalatı kaybı  ΔM_c = AB'den ithalat_c × [(1 + τ_TR,c)^(−σ) − 1]         (τ_TR: 2026 MFN, İGV hariç)
  İthal ikamesi      ΔD_c = −ΔM_c × D_c / (D_c + M_AB-dışı,c)                  (Armington payları) [H]
                     D_c: yurt içi üretimin iç satışı = max(PRODTR 2025 satış, YSHİ 2024 üretim değeri)
                     − ihracat (BACI 2024), ≥ 0 (PRODTR gizli satırları ve küçük girişimleri kapsamaz)
  İstihdam           ΔL_c = (ΔX_c + ΔD_c) × çalışan_c / üretim değeri_c (TÜİK YSHİ 2024)
σ ∈ {3, 5, 8}. Statik, telafisiz; çapa yatırımcı kararları, girdi bağlantıları ve kur tepkisi yok.
İki ithalat rejimi: "mfn" (AB'ye yalnızca MFN) ve "c2" (02a §4.1: İGV, AB'nin baskın ve yurt içi kabiliyetin
zayıf olduğu satırlarda herkes için kalkar, diğer satırlarda AB'ye de uygulanır; τ_TR,c HS6 satırlarının AB
ithalatı ağırlıklı ortalaması, f2b'nin politika_tarife_hs6.csv'si).
İthalat tarafında enflasyonu önleyen vergi takası (f2c) yerli satışları ayrıca artırır; burada yok.

Girdiler: veri/s4_tarife_duvari_sinif.csv, veri/prodtr_cpa6_2025.csv (f2b), veri/tuik_yshi_nace2.csv,
          veri/cn2025_nace_rejim.csv, veri/teshis_odemeler_dengesi.csv, BACI 2024 Türkiye ikili ticareti
Çıktı:    veri/politika_s4_net_istihdam_sinif.csv, veri/politika_s4_net_istihdam_ozet.csv
"""

import argparse
import os

import numpy as np
import pandas as pd
import yollar

SIGMALAR = (3, 5, 8)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baci-tr", default=yollar.girdi("baci", "baci_hs17_tur_bilateral_hs6_2020_2024.csv.gz"))
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    v = lambda f: os.path.join(a.out, f)  # noqa: E731

    od = pd.read_csv(v("teshis_odemeler_dengesi.csv"), index_col=0)
    eurusd = od.loc[2025, "eur_try"] / od.loc[2025, "usd_try"]
    s4 = pd.read_csv(v("s4_tarife_duvari_sinif.csv"), dtype={"nace2": str}).set_index("nace2")

    m = pd.read_csv(v("cn2025_nace_rejim.csv"), dtype={"cn8": str, "nace2": str, "cpa22": str})
    m = m[m.cn8.str.fullmatch(r"\d{8}") & m.nace2.str.fullmatch(r"\d\d\.\d\d")].copy()
    m["hs6"] = m.cn8.str[:6]
    m["w"] = m.tr_ith_ab.fillna(0) + m.tr_ihr_ab.fillna(0) + 1.0
    hs = m.groupby(["hs6", "nace2"]).w.sum().reset_index().sort_values(["hs6", "w"]).drop_duplicates("hs6", keep="last")
    hs6_sinif = hs.set_index("hs6").nace2

    b = pd.read_csv(a.baci_tr, dtype={"hs6": str})
    b = b[b.year == b.year.max()].copy()
    b["hs6"] = b.hs6.str.zfill(6)
    b["sinif"] = b.hs6.map(hs6_sinif)
    x = b[b.flow == "X"].groupby("sinif").value_kusd.sum() / 1e3
    mn = b[(b.flow == "M") & (b.eu27 == 0)].groupby("sinif").value_kusd.sum() / 1e3

    pr = pd.read_csv(v("prodtr_cpa6_2025.csv"), dtype={"cpa22": str})
    pr["sinif"] = pr.cpa22.str[:5]
    uretim = pr.groupby("sinif").uretim_musd.sum(min_count=1)
    gizli = pr.groupby("sinif").gizli.any()

    y = pd.read_csv(v("tuik_yshi_nace2.csv"), dtype={"kod": str})
    y = y[(y.yil == 2024) & (y.kod.str.len() == 5)].set_index("kod")

    t = pd.DataFrame(index=sorted(set(s4.index) | set(y.index)))
    t.index.name = "sinif"
    t = t[t.index.str.fullmatch(r"(1\d|2\d|3[0-3])\.\d\d")]
    t["calisan"] = y.calisan
    t["uretim_degeri_musd"] = y.uretim_degeri_musd
    t["l_per_musd"] = t.calisan / t.uretim_degeri_musd
    t["ab_ihracat_musd"] = s4.tr_ab_ihracat_meur * eurusd
    t["ab_ithalat_musd"] = s4.ab_tr_ihracat_meur * eurusd
    t["tau_ab"] = s4.ab_oran_yuzde / 100
    t["tau_tr"] = s4.tr_oran_igv_haric_yuzde / 100
    # c2 rejimi: HS6 düzeyinde oran → sınıf (AB ithalatı ağırlıklı); GB ve İTÜ dışı satırlar 0
    h = pd.read_csv(v("politika_tarife_hs6.csv"), dtype={"hs6": str})
    baskin = (h.m_ab_musd / (h.m_ab_musd + h.m_diger_musd).replace(0, np.nan)).fillna(0) >= 0.5
    guclu = h.gizli.astype(bool) | (h.uretim_ithalat_orani >= 1.0)
    h["oran_c2"] = np.where(baskin & ~guclu, h.t_mfn, h.t_tam) * h.rejim.isin(["GB", "ITU"]) / 100
    h["sinif"] = h.hs6.map(hs6_sinif)
    g = h.groupby("sinif")
    t["tau_tr_c2"] = (g.apply(lambda d: (d.m_ab_musd * d.oran_c2).sum() / d.m_ab_musd.sum()
                              if d.m_ab_musd.sum() > 0 else np.nan, include_groups=False))
    t["prodtr_satis_musd"] = uretim
    t["prodtr_gizli"] = gizli
    t["ihracat_dunya_musd"] = x
    t["ab_disi_ithalat_musd"] = mn
    # PRODTR gizli satırları ve küçük girişimleri kapsamadığından iç satış YSHİ üretim değeriyle tamamlanır
    t["ic_satis_musd"] = np.fmax((t.prodtr_satis_musd - t.ihracat_dunya_musd).clip(lower=0),
                                 (t.uretim_degeri_musd - t.ihracat_dunya_musd).clip(lower=0))
    pay_d = t.ic_satis_musd / (t.ic_satis_musd + t.ab_disi_ithalat_musd.fillna(0))
    t["yerli_pay_ikame"] = pay_d.fillna(0)
    for s in SIGMALAR:
        dx = t.ab_ihracat_musd * ((1 + t.tau_ab.fillna(0)) ** (-s) - 1)
        for rejim, tau in (("", t.tau_tr), ("_c2", t.tau_tr_c2.fillna(t.tau_tr))):
            dm = t.ab_ithalat_musd * ((1 + tau.fillna(0)) ** (-s) - 1)
            dd = -dm * t.yerli_pay_ikame
            t[f"ithal_ikamesi{rejim}_s{s}_musd"] = dd
            t[f"istihdam_ikame{rejim}_s{s}"] = dd * t.l_per_musd
            t[f"istihdam_net{rejim}_s{s}"] = (dx + dd) * t.l_per_musd
            t[f"net_pay{rejim}_s{s}"] = t[f"istihdam_net{rejim}_s{s}"] / t.calisan
        t[f"ihracat_kaybi_s{s}_musd"] = dx
        t[f"istihdam_ihracat_s{s}"] = dx * t.l_per_musd
    t = t.replace([np.inf, -np.inf], np.nan)
    t.round(4).to_csv(v("politika_s4_net_istihdam_sinif.csv"))

    ozet = []
    for rejim, ad in (("", "mfn"), ("_c2", "c2")):
        for s in SIGMALAR:
            k = t[t.calisan.notna()]
            ozet.append(dict(rejim=ad, sigma=s, ihracat_kaybi_musd=k[f"ihracat_kaybi_s{s}_musd"].sum(),
                             ithal_ikamesi_musd=k[f"ithal_ikamesi{rejim}_s{s}_musd"].sum(),
                             istihdam_ihracat=k[f"istihdam_ihracat_s{s}"].sum(),
                             istihdam_ikame=k[f"istihdam_ikame{rejim}_s{s}"].sum(),
                             istihdam_net=k[f"istihdam_net{rejim}_s{s}"].sum(),
                             sinif_5yuzde_ustu_kayip=int((k[f"net_pay{rejim}_s{s}"] < -0.05).sum()),
                             sinif_net_kazanc=int((k[f"net_pay{rejim}_s{s}"] > 0).sum())))
    oz = pd.DataFrame(ozet)
    oz.round(1).to_csv(v("politika_s4_net_istihdam_ozet.csv"), index=False)
    pd.set_option("display.width", 220)
    print(oz.round(0).to_string(index=False))
    sut = ["calisan", "ab_ihracat_musd", "ab_ithalat_musd", "tau_ab", "tau_tr", "yerli_pay_ikame", "istihdam_ihracat_s5",
           "istihdam_ikame_s5", "istihdam_net_s5", "net_pay_s5"]
    print(t.sort_values("istihdam_net_s5")[sut].head(20).round(3).to_string())
    print(t.sort_values("istihdam_net_s5", ascending=False)[sut].head(12).round(3).to_string())


if __name__ == "__main__":
    main()
