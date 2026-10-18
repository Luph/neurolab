"""Faz 2 — Tarife–iç vergi takası: AB mallarına tarife + menşeden bağımsız ÖTV/KDV indirimi.

Soru: GB'den çıkışta AB mallarına gümrük vergisi uygulanırken, enflasyonu önlemek için yalnızca yerli
ürünlerde ÖTV indirimi yapılabilir mi? Yalnızca yerli ürüne indirim GATT md. III:2'ye aykırıdır
(Endonezya–Otomobil, Brezilya–Vergilendirme; DS583 dersi, temel ilke 8). Hukuken temiz eşdeğeri:
tarife (bağlı oran içinde, MFN) + aynı ürün grubunda bütün menşelere eşit ÖTV/KDV indirimi. Bu betik o
takası ürün grubu düzeyinde sayısallaştırır.

Model (her ürün grubu g; kaynaklar o ∈ {yerli, ab, sta, diger}):
  Tüketici fiyatı      P_o = c_o (1 + ρ τ_o)(1 + ö)(1 + k)
  Armington CES        q_o = a_o Q (P_o / P)^(−σ),  P = (Σ a_o P_o^(1−σ))^(1/(1−σ)),  Q = Q0 (P / P0)^(−η)
  Takas kuralı         ö1 (veya KDV'de k1): grubun fiyat endeksi değişmez (P1 = P0; Laspeyres ve CES ayrı
                       raporlanır). Oran sıfıra inse de yetmiyorsa kısmi telafi (kalan fiyat artışı raporlanır)
  Gelir                tarife = Σ τ_o × CIF_o; ÖTV = ö × Σ matrah_o; KDV = k × Σ (matrah_o + ÖTV_o)
                       (matrah = CIF + gümrük vergisi + yurt içi marj; yerli üründe üretici fiyatı + marj)
  İstihdam             Δ yerli satış × (çalışan / üretim değeri), NACE sınıfı oranı (TÜİK YSHİ)
Tasarımlar (senaryo): yok (pasif); T-A takas (bütün menşelere eşit ÖTV/KDV indirimi); T-0 yalnızca yerli
ürüne ÖTV/KDV indirimi (kullanıcının önerisinin ilk biçimi; GATT III:2'ye aykırı, yalnızca karşılaştırma);
T-B tek tip vergi + yerli üreticiye III:8(b) birim ödemesi. Hepsi aynı kurala göre grubun fiyat endeksini
sabitler; fark, sabitlemenin maliyeti ve yerli ürüne sağladığı fiyat avantajıdır.
Belirsizlik: σ ∈ {2, 4, 6}, η ∈ {0,5; 1,0; 1,5}, ρ ∈ {0,8; 1,0} (P10–P50–P90 olarak raporlanır).

Girdi: veri/politika_takas_parametre.csv (ürün grubu başına pazar bileşimi, ÖTV/KDV, tarifeler, kaynaklar)
Çıktı: veri/politika_takas_sonuc.csv
"""

import argparse
import itertools
import os

import numpy as np
import pandas as pd

KAYNAKLAR = ("yerli", "ab", "sta", "diger")
SIGMA, ETA, RHO = (2.0, 4.0, 6.0), (0.5, 1.0, 1.5), (0.8, 1.0)


def ikiye_bol(f, lo, hi, tol=1e-10):
    """f(lo) < 0 < f(hi) aralığında kök (ikiye bölme)."""
    for _ in range(200):
        orta = (lo + hi) / 2
        if f(orta) > 0:
            hi = orta
        else:
            lo = orta
        if hi - lo < tol:
            break
    return (lo + hi) / 2


def fiyatlar(tau, rho, ö, k, s=None):
    """ö, k: kaynak başına ÖTV ve KDV oranı; s: yerli üreticiye birim destek (üretici fiyatına oran)."""
    s = s or {}
    return {o: (1 + rho * tau[o]) * (1 + ö[o]) * (1 + k[o]) * (1 - s.get(o, 0.0)) for o in KAYNAKLAR}


def ces_endeks(a, P, sigma):
    return sum(a[o] * P[o] ** (1 - sigma) for o in KAYNAKLAR if a[o] > 0) ** (1 / (1 - sigma))


def coz(r, sigma, eta, rho, kural="ces"):
    """Tek parametre seti için tasarımı çözer. r: parametre satırı (pay ve oranlar oran olarak).

    r.takas: "otv"/"kdv" (T-A, bütün menşelere eşit indirim), "otv_yerli"/"kdv_yerli" (T-0, yalnızca
    yerli ürüne indirim; GATT III:2'ye aykırı, karşılaştırma için), "destek_yerli" (T-B, yerli üreticiye
    III:8(b) birim ödemesi), "yok". Çözülen araç grubun fiyat endeksini (kural: "laspeyres" veya "ces")
    baz düzeyde tutar; araç sınırına (oran 0, destek %90) ulaşılırsa kısmi telafi raporlanır.
    """
    pay = {o: r[f"pay_{o}"] for o in KAYNAKLAR}
    tau0 = {o: r[f"tau0_{o}"] for o in KAYNAKLAR}
    tau1 = {o: r[f"tau1_{o}"] for o in KAYNAKLAR}
    ö0 = {o: r.otv0 for o in KAYNAKLAR}
    k0 = {o: r.kdv for o in KAYNAKLAR}
    P0 = fiyatlar(tau0, rho, ö0, k0)
    # CES ağırlıkları baz paylara kalibre edilir (harcama payı = a_o P_o^(1−σ) / Σ)
    a = {o: pay[o] * P0[o] ** (sigma - 1) for o in KAYNAKLAR}
    I0 = ces_endeks(a, P0, sigma)

    def arac(x):
        if r.takas == "otv":
            return {o: x for o in KAYNAKLAR}, k0, {}
        if r.takas == "kdv":
            return ö0, {o: x for o in KAYNAKLAR}, {}
        if r.takas == "otv_yerli":
            return {**ö0, "yerli": x}, k0, {}
        if r.takas == "kdv_yerli":
            return ö0, {**k0, "yerli": x}, {}
        if r.takas == "destek_yerli":
            return ö0, k0, {"yerli": x}
        return ö0, k0, {}

    def endeks(x):
        P = fiyatlar(tau1, rho, *arac(x))
        if kural == "ces":
            return ces_endeks(a, P, sigma) / I0 - 1
        return sum(pay[o] * P[o] / P0[o] for o in KAYNAKLAR) - 1

    if r.takas in ("otv", "kdv", "otv_yerli", "kdv_yerli"):
        ust = r.otv0 if r.takas.startswith("otv") else r.kdv
        # [0, baz oran] aralığında endeksi sabitleyen oran; sıfıra inmek yetmiyorsa 0 (kısmi telafi)
        if endeks(0.0) >= 0:
            x = 0.0
        else:
            x = ikiye_bol(endeks, 0.0, ust) if endeks(ust) > 0 else ust
    elif r.takas == "destek_yerli":
        # destek arttıkça endeks düşer: [0, 0,9] aralığında kök
        if endeks(0.0) <= 0:
            x = 0.0
        else:
            x = ikiye_bol(lambda d: -endeks(d), 0.0, 0.9) if endeks(0.9) < 0 else 0.9
    else:
        x = 0.0
    ö1, k1, s1 = arac(x)
    P1 = fiyatlar(tau1, rho, ö1, k1, s1)
    I1 = ces_endeks(a, P1, sigma)
    Q1 = (I1 / I0) ** (-eta)
    harc0 = {o: pay[o] for o in KAYNAKLAR}                                     # baz harcama (oran)
    harc1 = {o: (a[o] * P1[o] ** (1 - sigma) / I1 ** (1 - sigma)) * Q1 * I1 / I0 for o in KAYNAKLAR}
    hacim = {o: (harc1[o] / P1[o]) / (harc0[o] / P0[o]) - 1 if harc0[o] > 0 else 0.0 for o in KAYNAKLAR}

    def gelirler(harc, tau, ö, kk, s):
        # tüketici harcaması → matrah (KDV ve ÖTV hariç) → CIF (ithalatta gümrük vergisi hariç).
        # ρ < 1 ise CIF fiyatı sabit kalır, vergi farkını yurt içi dağıtıcı üstlenir; vergi tam CIF üzerinden.
        # Yerli destek: üretici fiyatı sabit, tüketiciye yansıyan matrah (1 − s) ile düşer; ödeme = s / (1 − s) × matrah
        matrah = {o: harc[o] / ((1 + ö[o]) * (1 + kk[o])) for o in KAYNAKLAR}
        cif = {o: matrah[o] / (1 + rho * tau[o]) if o != "yerli" else 0.0 for o in KAYNAKLAR}
        g = sum(tau[o] * cif[o] for o in KAYNAKLAR)
        otv = sum(ö[o] * matrah[o] for o in KAYNAKLAR)
        kdv = sum(kk[o] * matrah[o] * (1 + ö[o]) for o in KAYNAKLAR)
        sy = s.get("yerli", 0.0)
        return g, otv, kdv, matrah["yerli"] * sy / (1 - sy)

    g0, o0, kd0, _ = gelirler(harc0, tau0, ö0, k0, {})
    g1, o1, kd1, d1 = gelirler(harc1, tau1, ö1, k1, s1)
    las = sum(pay[o] * P1[o] / P0[o] for o in KAYNAKLAR) - 1
    return dict(otv1=ö1["ab"], otv1_yerli=ö1["yerli"], kdv1=k1["ab"], kdv1_yerli=k1["yerli"],
                destek_orani=s1.get("yerli", 0.0), fiyat_degisimi_laspeyres=las, fiyat_degisimi_ces=I1 / I0 - 1,
                **{f"hacim_{o}": hacim[o] for o in KAYNAKLAR},
                **{f"fiyat_{o}": P1[o] / P0[o] - 1 for o in KAYNAKLAR},
                yerli_fiyat_avantaji=(P1["ab"] / P0["ab"]) / (P1["yerli"] / P0["yerli"]) - 1,
                d_gumruk=g1 - g0, d_otv=o1 - o0, d_kdv=kd1 - kd0, d_destek=-d1,
                d_mali=(g1 - g0) + (o1 - o0) + (kd1 - kd0) - d1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    par = pd.read_csv(os.path.join(a.out, "politika_takas_parametre.csv"))
    satirlar = []
    for _, r in par.iterrows():
        for sigma, eta, rho in itertools.product(SIGMA, ETA, RHO):
            for kural in ("ces", "laspeyres"):
                s = coz(r, sigma, eta, rho, kural)
                pazar = r.pazar_musd
                satirlar.append(dict(grup=r.grup, senaryo=r.senaryo, sigma=sigma, eta=eta, rho=rho, kural=kural,
                                     pazar_musd=pazar, **{k: v for k, v in s.items() if not k.startswith("d_")},
                                     **{k + "_musd": v * pazar for k, v in s.items() if k.startswith("d_")},
                                     # yerli üreticinin satış geliri: üretici fiyatı sabit, değişim = hacim
                                     yerli_satis_degisimi_musd=s["hacim_yerli"] * r.pay_yerli * pazar
                                     / ((1 + r.otv0) * (1 + r.kdv)),
                                     istihdam_degisimi=s["hacim_yerli"] * r.pay_yerli * pazar
                                     / ((1 + r.otv0) * (1 + r.kdv)) * r.calisan_per_musd))
    t = pd.DataFrame(satirlar)
    t.round(5).to_csv(os.path.join(a.out, "politika_takas_sonuc.csv"), index=False)

    # Özet: TÜFE kısıtı ölçülen (Laspeyres) endeksle bağlandığı için başlık kural "laspeyres"; CES refah
    # kontrolüdür. Merkez σ=4, η=1, ρ=1; aralık parametre ızgarasının P10–P90'ı
    agirlik = par.drop_duplicates("grup").set_index("grup").tufe_agirlik_yuzde
    t["tufe_katki_bp"] = t.grup.map(agirlik) * t.fiyat_degisimi_laspeyres * 100
    olcu = ["otv1", "otv1_yerli", "kdv1", "kdv1_yerli", "destek_orani", "fiyat_degisimi_laspeyres",
            "fiyat_degisimi_ces", "fiyat_ab", "fiyat_yerli", "yerli_fiyat_avantaji", "hacim_yerli", "hacim_ab",
            "hacim_sta", "hacim_diger", "d_gumruk_musd", "d_otv_musd", "d_kdv_musd", "d_destek_musd", "d_mali_musd",
            "yerli_satis_degisimi_musd", "istihdam_degisimi", "tufe_katki_bp"]
    ozet = []
    for (grup, senaryo, kural), x in t.groupby(["grup", "senaryo", "kural"], sort=False):
        m = x[(x.sigma == 4.0) & (x.eta == 1.0) & (x.rho == 1.0)].iloc[0]
        for o in olcu:
            ozet.append(dict(grup=grup, senaryo=senaryo, kural=kural, olcu=o, merkez=m[o],
                             p10=x[o].quantile(0.1), p90=x[o].quantile(0.9)))
    oz = pd.DataFrame(ozet)
    toplam = (t.groupby(["senaryo", "kural", "sigma", "eta", "rho"])
              [["d_gumruk_musd", "d_otv_musd", "d_kdv_musd", "d_destek_musd", "d_mali_musd",
                "yerli_satis_degisimi_musd", "istihdam_degisimi", "tufe_katki_bp"]].sum().reset_index())
    for (senaryo, kural), x in toplam.groupby(["senaryo", "kural"], sort=False):
        m = x[(x.sigma == 4.0) & (x.eta == 1.0) & (x.rho == 1.0)].iloc[0]
        for o in ("d_gumruk_musd", "d_otv_musd", "d_kdv_musd", "d_destek_musd", "d_mali_musd",
                  "yerli_satis_degisimi_musd", "istihdam_degisimi", "tufe_katki_bp"):
            ozet.append(dict(grup="TOPLAM", senaryo=senaryo, kural=kural, olcu=o, merkez=m[o],
                             p10=x[o].quantile(0.1), p90=x[o].quantile(0.9)))
    oz = pd.DataFrame(ozet)
    oz.round(5).to_csv(os.path.join(a.out, "politika_takas_ozet.csv"), index=False)
    m = t[(t.sigma == 4.0) & (t.eta == 1.0) & (t.rho == 1.0) & (t.kural == "laspeyres")]
    pd.set_option("display.width", 250)
    sut = ["grup", "senaryo", "otv1", "otv1_yerli", "kdv1", "kdv1_yerli", "destek_orani", "fiyat_degisimi_laspeyres",
           "fiyat_ab", "fiyat_yerli", "yerli_fiyat_avantaji", "hacim_yerli", "hacim_ab", "d_gumruk_musd", "d_otv_musd",
           "d_kdv_musd", "d_destek_musd", "d_mali_musd", "yerli_satis_degisimi_musd", "istihdam_degisimi",
           "tufe_katki_bp"]
    print(m[sut].round(3).to_string(index=False))
    print(oz[oz.grup == "TOPLAM"].round(1).to_string(index=False))


if __name__ == "__main__":
    main()
