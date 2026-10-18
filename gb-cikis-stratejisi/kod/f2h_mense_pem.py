"""Faz 2C — Menşe hazırlığı: AB ile bir STA'da (S2/S3) Türk sanayisinin menşe kurallarını karşılama riski.

GB'de sanayi malları menşe kuralı olmadan serbest dolaşır (A.TR). Çıkıştan sonra AB'ye tercihli girişin şartı menşedir:
pan-Avrupa-Akdeniz (PEM) kurallarında AB ve PEM bölgesi girdileri "menşeli" sayılır (ikili ve çapraz kümülasyon),
diğer girdiler menşe dışı malzemedir (NOM). Bu betik her sanayi kolu için menşe dışı ithal ara girdinin üretim değerine
oranını hesaplar. Bu oran, PEM'in değer kurallarındaki (MaxNOM, fabrika çıkış fiyatının %'si) tavanla karşılaştırılır.

Yöntem:
  - TÜİK 2023 ithalat girdi-çıktı tablosu (64 ürün × 64 kol, cif, temel fiyat): Z_m[i, j] = j kolunun kullandığı ithal i.
  - Ürün i'nin ithalatında menşe payları: BACI 2024, Türkiye ithalatı, yalnız ara malları (BEC, f2b sınıflaması; ürünün
    ara malı satırı yoksa bütün satırlar). HS6 → I-O ürünü: CN2025–CPA eşlemesi (f2a).
  - İki kümülasyon tanımı: (a) yalnız AB27 (AB–TR STA'sında ikili kümülasyon); (b) PEM bölgesi (çapraz kümülasyon;
    ortakların birbirleriyle de aynı kuralları uygulaması şartıyla).
  - Doğrudan oran: NOM_j = Σ_i Z_m[i, j] × s_i / x_j. "Bütünleşik" oran Leontief ile yurt içi girdilerin ithal içeriğini de
    ekler: m (I − A_d)⁻¹; menşeli yurt içi girdiler PEM'de tamamen menşeli sayıldığı için (emme kuralı) üst sınırdır.
  - Sektör ortalamasıdır; firma ve ürün dağılımı geniştir. Tekstil ve giyimde kural değer değil işlem esaslıdır
    (kumaş/iplik menşei), bu yüzden oran yalnızca gösterge.
Ürün mercek altında: sektör ortalaması ürün düzeyindeki riski gizleyebilir. Beş kilit üründe ürüne özgü ana bileşenlerin
PEM dışı ithalatı (BACI 2024) üretim değerine (PRODTR 2025) oranlanır. Bileşen ithalatı başka kullanımları da içerir
(yedek parça, başka araçlar), genel amaçlı ve diğer menşe dışı malzemeler dahil değildir; gösterge kabadır. Kesin sonuç
için firma ürün ağaçları (malzeme listesi ve menşe) gerekir.

Çıktılar: veri/hazirlik_pem_mense.csv (sektör), veri/hazirlik_pem_urun.csv (ürün)
"""

import argparse
import os

import numpy as np
import pandas as pd

import yollar
from f2a_io_fiyat import P1, SATIR, SUTUN, hs6_esleme, io_indir, io_kodu, oku

AB27 = {"AUT", "BEL", "BGR", "HRV", "CYP", "CZE", "DNK", "EST", "FIN", "FRA", "DEU", "GRC", "HUN", "IRL", "ITA",
        "LVA", "LTU", "LUX", "MLT", "NLD", "POL", "PRT", "ROU", "SVK", "SVN", "ESP", "SWE"}
# PEM Sözleşmesi'ni uygulayan taraflar (Suriye ve Cezayir hariç tutuldu: kümülasyon fiilen işlemiyor) [D?]
PEM_DIGER = {"CHE", "LIE", "NOR", "ISL", "FRO", "ISR", "PSE", "JOR", "LBN", "EGY", "MAR", "TUN", "ALB", "BIH",
             "MKD", "MNE", "SRB", "XKX", "GEO", "MDA", "UKR"}
ONE_CIKAN = ["CHN", "RUS", "USA", "KOR", "JPN", "IND", "TWN", "VNM", "GBR"]
KUMAS = ["5208", "5209", "5210", "5211", "5212", "5407", "5408", "5512", "5513", "5514", "5515", "5516",
         "6001", "6002", "6003", "6004", "6005", "6006"]
# ürün: (ihracat HS önekleri, PRODTR CPA önekleri, ana bileşen HS önekleri)
URUNLER = {  # yalnız ürüne özgü bileşen fasılları (genel amaçlı çip, motor, kablo, lastik hariç)
    "Otomobil (8703)": (["8703"], ["29.10.21", "29.10.22", "29.10.23"], ["8708", "8407", "8408", "8409", "8706", "8707"]),
    "Televizyon (852872)": (["852872"], ["26.40.20"], ["852990"]),
    "Buzdolabı (841810, 841821)": (["841810", "841821"], ["27.51.11"], ["841430", "841899"]),
    "Çamaşır makinesi (845011, 845020)": (["845011", "845020"], ["27.51.13"], ["845090"]),
    "Giyim (61, 62)": (["61", "62"], ["14.1"], KUMAS),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=yollar.GIRDI)
    ap.add_argument("--out", default=yollar.VERI)
    ap.add_argument("--baci-tr", default=yollar.girdi("baci", "baci_hs17_tur_bilateral_hs6_2020_2024.csv.gz"))
    a = ap.parse_args()
    v = lambda f: os.path.join(a.out, f)  # noqa: E731

    io_yollari = io_indir(os.path.join(a.cache, "io2023"))
    yd, kod = oku(io_yollari["yurtici"])
    it, kod_m = oku(io_yollari["ithalat"])
    assert kod == kod_m
    Z_d = yd.iloc[SATIR, SUTUN].astype(float).to_numpy()
    Z_m = it.iloc[SATIR, SUTUN].astype(float).to_numpy()
    x = yd.iloc[P1, SUTUN].astype(float).to_numpy()
    A_d = np.divide(Z_d, x, out=np.zeros_like(Z_d), where=x > 0)
    ad = [a.split("\n")[0].strip() for a in yd.iloc[SATIR, 2].astype(str)]

    # Ürün başına ara malı ithalatının menşe payları (BACI 2024)
    hs6_io, _ = hs6_esleme(v("cn2025_nace_rejim.csv"))
    kul = pd.read_csv(v("politika_tarife_hs6.csv"), dtype={"hs6": str}).set_index("hs6").kullanim
    b = pd.read_csv(a.baci_tr, dtype={"hs6": str, "partner_iso3": str})
    b = b[(b.year == 2024) & (b.flow == "M")].copy()
    b["hs6"] = b.hs6.str.zfill(6)
    b["io"] = b.hs6.map(hs6_io)
    b["ara"] = b.hs6.map(kul).isin(["ara"])
    b = b[b.io.notna()]
    b["bolge"] = np.where(b.partner_iso3.isin(AB27), "ab", np.where(b.partner_iso3.isin(PEM_DIGER), "pem", "disi"))
    payl = {}
    for c in kod:
        g = b[b.io == c]
        g = g[g.ara] if g.ara.any() else g
        top = g.value_kusd.sum()
        if top <= 0:
            payl[c] = dict(ab=0.0, pem=0.0, disi=0.0, **{u: 0.0 for u in ONE_CIKAN}, ara_ithalat_musd=0.0)
            continue
        s = g.groupby("bolge").value_kusd.sum() / top
        u = g.groupby("partner_iso3").value_kusd.sum() / top
        payl[c] = dict(ab=s.get("ab", 0.0), pem=s.get("pem", 0.0), disi=s.get("disi", 0.0),
                       **{k: u.get(k, 0.0) for k in ONE_CIKAN}, ara_ithalat_musd=top / 1e3)
    P = pd.DataFrame(payl).T.reindex(kod)

    s_ab_disi = (1 - P.ab).to_numpy(dtype=float)            # (a) yalnız AB kümülasyonu
    s_pem_disi = P.disi.to_numpy(dtype=float)               # (b) PEM bölgesi
    with np.errstate(invalid="ignore", divide="ignore"):
        nom_a = np.where(x > 0, (Z_m * s_ab_disi[:, None]).sum(0) / x, np.nan)
        nom_b = np.where(x > 0, (Z_m * s_pem_disi[:, None]).sum(0) / x, np.nan)
        m_b = np.nan_to_num(nom_b)
        L = np.linalg.inv(np.eye(len(kod)) - A_d)
        nom_b_top = m_b @ L
        ithal_ara = np.where(x > 0, Z_m.sum(0) / x, np.nan)
    t = pd.DataFrame({"io": kod, "ad": ad, "uretim_mtl": x / 1e3, "ithal_ara_orani": ithal_ara,
                      "nom_ab_disi_dogrudan": nom_a, "nom_pem_disi_dogrudan": nom_b, "nom_pem_disi_butunlesik": nom_b_top})
    # kolun kullandığı ithal girdilerde öne çıkan menşe dışı tedarikçiler (üretime oran)
    for u in ONE_CIKAN:
        su = P[u].to_numpy(dtype=float)
        t[f"nom_{u.lower()}"] = np.where(x > 0, (Z_m * su[:, None]).sum(0) / x, np.nan)
    # AB'ye ihracat (2025, NACE bölümü → I-O kolu)
    bm = pd.read_csv(v("teshis_bolum_maruziyet.csv"), dtype={"bolum": str})
    bm = bm[bm.bolum.str.fullmatch(r"\d\d")]
    bm["io"] = bm.bolum.astype(int).map(io_kodu)
    t = t.merge(bm.groupby("io")[["tr_ihr_ab_2025_musd", "calisan_2024"]].sum().reset_index(), on="io", how="left")
    t["risk"] = pd.cut(t.nom_pem_disi_dogrudan, [-np.inf, 0.25, 0.40, np.inf], labels=["düşük", "orta", "yüksek"])
    t["kural_turu_notu"] = np.select(
        [t.io.eq("C13-C15"), t.io.eq("C19")],
        ["işlem esaslı (kumaş/iplik menşei); oran yalnız gösterge",
         "rafinaj özel işlem kuralıyla menşe kazandırır; ham petrol ithalatı değer tavanına girmez"], "")
    imalat = t.io.str.startswith("C")
    t = t[imalat].copy()
    t.round(5).to_csv(v("hazirlik_pem_mense.csv"), index=False)
    pd.set_option("display.width", 250)
    print(t[["io", "ithal_ara_orani", "nom_ab_disi_dogrudan", "nom_pem_disi_dogrudan", "nom_pem_disi_butunlesik",
             "nom_chn", "nom_rus", "tr_ihr_ab_2025_musd", "risk"]].round(3).to_string(index=False))
    w = t.tr_ihr_ab_2025_musd.fillna(0)
    print("AB'ye ihracat ağırlıklı ortalama NOM (PEM dışı, doğrudan):", round((w * t.nom_pem_disi_dogrudan).sum() / w.sum(), 3))
    for r in ("orta", "yüksek"):
        print(f"risk={r}: AB ihracatı", round(w[t.risk == r].sum() / 1e3, 1), "mlr $ /", round(w.sum() / 1e3, 1))

    # Ürün mercek altında
    tum = pd.read_csv(a.baci_tr, dtype={"hs6": str, "partner_iso3": str})
    tum = tum[tum.year == 2024].copy()
    tum["hs6"] = tum.hs6.str.zfill(6)
    pem = AB27 | PEM_DIGER
    pr = pd.read_csv(v("prodtr_cpa6_2025.csv"), dtype={"cpa22": str})
    urunler = []
    for ad_, (ihr, cpa, bil) in URUNLER.items():
        x_ = tum[(tum.flow == "X") & tum.hs6.str.startswith(tuple(ihr))]
        m_ = tum[(tum.flow == "M") & tum.hs6.str.startswith(tuple(bil))]
        disi = m_[~m_.partner_iso3.isin(pem)]
        uretim = pr[pr.cpa22.str.startswith(tuple(cpa))].uretim_musd.sum()
        bas = (disi.groupby("partner_iso3").value_kusd.sum() / 1e3).nlargest(3)
        urunler.append(dict(urun=ad_, ihracat_2024_musd=x_.value_kusd.sum() / 1e3,
                            ihracat_ab_2024_musd=x_[x_.partner_iso3.isin(AB27)].value_kusd.sum() / 1e3,
                            uretim_2025_musd=uretim, bilesen_ithalat_musd=m_.value_kusd.sum() / 1e3,
                            bilesen_pem_disi_musd=disi.value_kusd.sum() / 1e3,
                            nom_vekili=disi.value_kusd.sum() / 1e3 / uretim if uretim else np.nan,
                            bas_tedarikciler="; ".join(f"{k} {val:,.0f}" for k, val in bas.items()),
                            bilesenler=" ".join(bil)))
    u = pd.DataFrame(urunler)
    u.round(4).to_csv(v("hazirlik_pem_urun.csv"), index=False)
    print(u.drop(columns=["bilesenler"]).round(3).to_string(index=False))


if __name__ == "__main__":
    main()
