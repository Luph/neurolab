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


def fiyatlar(tau, rho, ö, k):
    return {o: (1 + rho * tau[o]) * (1 + ö) * (1 + k) for o in KAYNAKLAR}


def ces_endeks(a, P, sigma):
    return sum(a[o] * P[o] ** (1 - sigma) for o in KAYNAKLAR if a[o] > 0) ** (1 / (1 - sigma))


def coz(r, sigma, eta, rho, kural="ces"):
    """Tek parametre seti için takası çözer. r: parametre satırı (pay ve oranlar oran olarak)."""
    pay = {o: r[f"pay_{o}"] for o in KAYNAKLAR}
    tau0 = {o: r[f"tau0_{o}"] for o in KAYNAKLAR}
    tau1 = {o: r[f"tau1_{o}"] for o in KAYNAKLAR}
    ö0, k = r.otv0, r.kdv
    P0 = fiyatlar(tau0, rho, ö0, k)
    # CES ağırlıkları baz paylara kalibre edilir (harcama payı = a_o P_o^(1−σ) / Σ)
    a = {o: pay[o] * P0[o] ** (sigma - 1) for o in KAYNAKLAR}
    I0 = ces_endeks(a, P0, sigma)

    def endeks(ö, kk):
        P = fiyatlar(tau1, rho, ö, kk)
        if kural == "ces":
            return ces_endeks(a, P, sigma) / I0 - 1
        return sum(pay[o] * P[o] / P0[o] for o in KAYNAKLAR) - 1

    def kok(f, ust):
        # [0, üst] aralığında fiyat endeksini sabitleyen oran; sıfıra inmek yetmiyorsa 0 (kısmi telafi)
        if f(0.0) >= 0:
            return 0.0
        return ikiye_bol(f, 0.0, ust) if f(ust) > 0 else ust

    ö1, k1 = ö0, k
    if r.takas == "otv":
        ö1 = kok(lambda x: endeks(x, k), ö0)
    elif r.takas == "kdv":
        k1 = kok(lambda x: endeks(ö0, x), k)
    P1 = fiyatlar(tau1, rho, ö1, k1)
    I1 = ces_endeks(a, P1, sigma)
    Q1 = (I1 / I0) ** (-eta)
    harc0 = {o: pay[o] for o in KAYNAKLAR}                                     # baz harcama (oran)
    harc1 = {o: (a[o] * P1[o] ** (1 - sigma) / I1 ** (1 - sigma)) * Q1 * I1 / I0 for o in KAYNAKLAR}
    hacim = {o: (harc1[o] / P1[o]) / (harc0[o] / P0[o]) - 1 if harc0[o] > 0 else 0.0 for o in KAYNAKLAR}

    def gelirler(harc, tau, ö, kk):
        # tüketici harcaması → matrah (KDV ve ÖTV hariç) → CIF (ithalatta gümrük vergisi hariç).
        # ρ < 1 ise CIF fiyatı sabit kalır, vergi farkını yurt içi dağıtıcı üstlenir; vergi tam CIF üzerinden
        matrah = {o: harc[o] / ((1 + ö) * (1 + kk)) for o in KAYNAKLAR}
        cif = {o: matrah[o] / (1 + rho * tau[o]) if o != "yerli" else 0.0 for o in KAYNAKLAR}
        g = sum(tau[o] * cif[o] for o in KAYNAKLAR)
        otv = ö * sum(matrah.values())
        kdv = kk * sum(matrah[o] * (1 + ö) for o in KAYNAKLAR)
        return g, otv, kdv, matrah

    g0, o0, kd0, m0 = gelirler(harc0, tau0, ö0, k)
    g1, o1, kd1, m1 = gelirler(harc1, tau1, ö1, k1)
    las = sum(pay[o] * P1[o] / P0[o] for o in KAYNAKLAR) - 1
    return dict(otv1=ö1, kdv1=k1, fiyat_degisimi_laspeyres=las, fiyat_degisimi_ces=I1 / I0 - 1,
                **{f"hacim_{o}": hacim[o] for o in KAYNAKLAR},
                **{f"fiyat_{o}": P1[o] / P0[o] - 1 for o in KAYNAKLAR},
                yerli_matrah_degisimi=m1["yerli"] / m0["yerli"] - 1 if m0["yerli"] else 0.0,
                d_gumruk=g1 - g0, d_otv=o1 - o0, d_kdv=kd1 - kd0, d_mali=(g1 - g0) + (o1 - o0) + (kd1 - kd0))


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
                                     yerli_satis_degisimi_musd=s["yerli_matrah_degisimi"] * r.pay_yerli * pazar
                                     / ((1 + r.otv0) * (1 + r.kdv)),
                                     istihdam_degisimi=s["yerli_matrah_degisimi"] * r.pay_yerli * pazar
                                     / ((1 + r.otv0) * (1 + r.kdv)) * r.calisan_per_musd))
    t = pd.DataFrame(satirlar)
    t.round(5).to_csv(os.path.join(a.out, "politika_takas_sonuc.csv"), index=False)
    m = t[(t.sigma == 4.0) & (t.eta == 1.0) & (t.rho == 1.0) & (t.kural == "ces")]
    pd.set_option("display.width", 250)
    sut = ["grup", "senaryo", "otv1", "kdv1", "fiyat_degisimi_laspeyres", "fiyat_ab", "fiyat_yerli", "hacim_yerli", "hacim_ab",
           "hacim_diger", "d_gumruk_musd", "d_otv_musd", "d_kdv_musd", "d_mali_musd", "yerli_satis_degisimi_musd",
           "istihdam_degisimi"]
    print(m[sut].round(3).to_string(index=False))


if __name__ == "__main__":
    main()
