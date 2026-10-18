"""Faz 3 — Sınıf düzeyi senaryo etkileri (S2, S3, S4; P10–P50–P90), EDE ve CKE (kart alanları 8–9; ana matris).

Kısmi denge (ana prompt 1.1), sınıf i ve senaryo s için (değerler $ mn, BACI 2024):
  AB'ye ihracat    ΔX_AB = k_s · X_AB · [(1 + τ_etkin)^(−σ_i) − 1]
     S4:    τ_etkin = τ_AB,S4 + NTM_sınır + CE
     S2/S3: τ_etkin = (1 − p_uyum)·τ_AB,S4 + q·p_uyum·c_RoO + NTM_sınır + CE_s
            q = GB + İTÜ payı (tarım satırları 1/98'de bugün de menşe kuralına tabi; ek maliyet yok)
  Saptırma         ΔX_diğer = −δ_s · ΔX_AB
  AB'den ithalat   ΔM_AB = k^M_s · M_AB · [(1 + τ_m)^(−σ_i) − 1]
     S4:    τ_m = τ_TR,c2 + NTM_sınır          (c2: 02a §4.1, AB baskın ve yurt içi kabiliyet zayıfsa İGV kalkar)
     S2/S3: τ_m = (1 − p_AB)·τ_TR,c2 + p_AB·c_AB + NTM_sınır
  İç ikame         ΔD = −ΔM_AB · D/(D + M_AB-dışı),  D = max(YSHİ üretim − ihracat, 0)
  Üretim, istihdam ΔQ = ΔX_AB + ΔX_diğer + ΔD;   ΔL = ΔQ · L/Q · (1 − θ)
  Cari denge       ΔCA = ΔQ · (1 − m^X)        m^X: I-O 2023 toplam (doğrudan + dolaylı) ithal girdi içeriği
  TÜFE (bp)        ΔTÜFE = EDE_AB,i · τ_m(puan) · ρ
σ_i: CEPII ProTEE (Fontagné, Guimbard ve Orefice 2022) HS6 ticaret esneklikleri; sınıf içinde TR→AB ihracatı ağırlıklı
  medyan (anlamsız/pozitif HS6 → HS4 ortalaması → HS2), [2, 15] aralığına kırpılır.
k_s, k^M_s: merkez parametrelerle toplam AB ihracatı (ithalatı) değişimini Faz 2B GE (σ = 7, uzun dönem) medyanına
  eşitleyen ölçek; S3 için S2 ve S4 ölçeklerinin ortalaması (S3 GE aralığı −%18 / +%1 çok geniş).
δ_s: GE'de toplam ihracat ile AB ihracatı değişiminin oranından (2024 AB payıyla).
Monte Carlo (N = 2000), ortak çarpanlar + sınıf gürültüsü [T]:
  σ: ortak lognormal(0; 0,25) × sınıf lognormal(0; 0,15);  NTM_sınır: üçgen(0,5; 1; 2)% (+ çabuk bozulan pay × üçgen(0,5; 1; 2)%);
  CE: CE payı × üçgen(1; 2; 4)% (S2'de ACAA ile × 0,25);  p_uyum: ±0,10 sınıf + ±0,05 ortak;  c_RoO: × lognormal(0; 0,3);
  S2'de sınır sürtünmesi × 0,5 (AEO karşılıklı tanıma, tek pencere); AB ihracatçısının TR'ye menşe maliyeti c_AB:
  S2 %0,5, S3 %1, uyum p_AB 0,92 / 0,85;  δ: ±0,10;  ρ: üçgen(0,6; 0,8; 1,0);  θ: üçgen(0,1; 0,3; 0,5);  S4'te 1/98 kaybı olasılığı 0,25 (AB hasmane, V-11) [H];
  1/98 kaybının kısmi denge etkisi GE toplamına eklenir (GE ölçeğiyle), yeniden dağıtılmaz.
Toplam belirsizlik: her çekilişte AB ihracatı (ithalatı) toplam değişimi GE dağılımından (ortak z; SH = GA90 / 3,29) alınır;
  toplam negatifse sınıflara kısmi denge kayıp paylarıyla, pozitifse ihracat (ithalat) payıyla dağıtılır.
EDE (1 puan tarife → TÜFE bp, ρ = 1): doğrudan = TÜFE ağırlığı (COICOP 2018 → sınıf, veri/f3_coicop_nace.csv) × ithalat
  payı × 100; dolaylı = I-O ürününün (f2a) dolaylı etkisi × sınıfın I-O ithalatındaki payı. EDE_AB = EDE × AB payı.
CKE (5 yıl, birikimli; yatırım ithalatı ve ithal girdi düşülmüş) [T]:
  tarife: STA dışı ithalata +1 puan → ΔM = M_STA-dışı[(1,01)^(−σ) − 1], ΔD = −ΔM · yerli pay (≤ %3 Q);
          CA_5 = 4,3 · ΔD · (1 − m^X) − 0,6 · ΔD (kapasite yatırımı: sermaye/hasıla 1, ithal payı 0,6);
          CKE_TÜFE = CA_5 / (EDE_STA-dışı · ρ = 0,8)   [$ mn / bp]
  mali:   iç satışa %1 üretim desteği → ΔD = σ · 0,01 · M · D/(D + M) (≤ %3 Q); maliyet 5 · 0,01 · D;
          CKE_mali = CA_5 / maliyet (mlr TL, 2026 ort. kur)   [$ mn / mlr TL]

Çıktı: veri/f3_senaryo_sinif.csv (sınıf × senaryo × değişken, P10/P50/P90), veri/f3_senaryo_ozet.csv,
       veri/f3_makro_sinif.csv (σ, m^X, EDE, TÜFE ağırlığı, CKE)
"""

import argparse
import os

import numpy as np
import pandas as pd

import f2a_io_fiyat as io
import f3a_ticaret as f3a
import yollar

N = 2000
TOHUM = 20261018
PAYLAR = {"S2": dict(p_ab=0.92, c_ab=0.5, ntm=0.5), "S3": dict(p_ab=0.85, c_ab=1.0, ntm=1.0), "S4": dict(ntm=1.0)}
VARSAYILAN_MENSE = {"düşük": ("D", 1.5, 0.90, 2.5, 0.80), "orta": ("O", 3.0, 0.80, 4.0, 0.70),
                    "yüksek": ("Y", 5.0, 0.65, 6.0, 0.55)}
CABUK = ("0201", "0203", "0204", "0207", "0302", "0304", "0401", "0402", "0403", "0406", "0603", "07", "0801", "0802",
         "0803", "0804", "0805", "0806", "0807", "0808", "0809", "0810")
CABUK_HARIC = ("0710", "0711", "0712", "0713", "0714")


def ucgen(rng, a, m, b, n):
    return rng.triangular(a, m, b, n)


def ithal_icerik(cache):
    """I-O 2023: ürün başına toplam ithal girdi içeriği 1' A_m (I − A_d)^-1."""
    yollar_io = io.io_indir(os.path.join(cache, "io2023"))
    yd, kod = io.oku(yollar_io["yurtici"])
    it, _ = io.oku(yollar_io["ithalat"])
    Z_d = yd.iloc[io.SATIR, io.SUTUN].astype(float).to_numpy()
    Z_m = it.iloc[io.SATIR, io.SUTUN].astype(float).to_numpy()
    x = yd.iloc[io.P1, io.SUTUN].astype(float).to_numpy()
    A_d = np.divide(Z_d, x, out=np.zeros_like(Z_d), where=x > 0)
    A_m = np.divide(Z_m, x, out=np.zeros_like(Z_m), where=x > 0)
    L = np.linalg.inv(np.eye(len(x)) - A_d)
    return pd.Series(A_m.sum(axis=0) @ L, index=kod), pd.Series(A_m.sum(axis=0), index=kod)


def sigma_sinif(protee, kn8):
    """ProTEE HS6 esneklikleri → sınıf (TR→AB ihracatı ağırlıklı medyan, mutlak değer)."""
    p = pd.read_csv(protee, dtype={"HS6": str})
    p["hs6"] = p.HS6.str.zfill(6)
    p["s"] = -pd.to_numeric(p.sigma, errors="coerce")
    p.loc[(p.s <= 0) | (p.positive == 1), "s"] = np.nan
    p["hs4"], p["hs2"] = p.hs6.str[:4], p.hs6.str[:2]
    for d in ("hs4", "hs2"):
        p["s"] = p.s.fillna(p.groupby(d).s.transform("mean"))
    s6, s4, s2 = p.set_index("hs6").s, p.groupby("hs4").s.mean(), p.groupby("hs2").s.mean()
    k = kn8.copy()
    k["hs6"] = k.cn8.str[:6]
    k["s"] = k.hs6.map(s6).fillna(k.cn8.str[:4].map(s4)).fillna(k.cn8.str[:2].map(s2))

    def wmed(d):
        d = d[d.s.notna()]
        if d.empty:
            return np.nan
        w = d.x_ab_meur.clip(lower=1e-6)
        o = np.argsort(d.s.values)
        c = np.cumsum(w.values[o]) / w.sum()
        return float(d.s.values[o][np.searchsorted(c, 0.5)])
    return k.groupby("nace2").apply(wmed, include_groups=False), float(p.s.median())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=yollar.GIRDI)
    ap.add_argument("--out", default=yollar.VERI)
    ap.add_argument("--n", type=int, default=N)
    a = ap.parse_args()
    v = lambda f: os.path.join(a.out, f)  # noqa: E731
    rng = np.random.default_rng(TOHUM)

    t = pd.read_csv(v("f3_ticaret_sinif.csv"), dtype={"nace2": str}).set_index("nace2")
    y = pd.read_csv(v("f3_yapi_sinif.csv"), dtype={"kod": str}).set_index("kod")
    ab = pd.read_csv(v("f3_ab_tarife_sinif.csv"), dtype={"kod": str}).set_index("kod")
    kn8 = pd.read_csv(v("f3_ab_tarife_kn8.csv"), dtype={"cn8": str, "nace2": str})
    od = pd.read_csv(v("teshis_odemeler_dengesi.csv"), index_col=0)
    usd_try_2026 = float(od.loc[2026, "usd_try"])

    kap = pd.read_csv(v("nace_kapsam.csv"), dtype={"kod": str})
    siniflar = sorted(kap.kod[kap.kapsam_grubu.eq("C")])          # 230 C sınıfı; ticareti olmayanlar 0
    d = pd.DataFrame(index=pd.Index(siniflar, name="kod"))
    d["x"] = t.x_musd_2024.reindex(d.index).fillna(0)
    d["x_ab"] = t.x_ab_musd_2024.reindex(d.index).fillna(0)
    d["m"] = t.m_musd_2024.reindex(d.index).fillna(0)
    d["m_ab"] = t.m_ab_musd_2024.reindex(d.index).fillna(0)
    d["q"] = y.uretim_musd
    d["l"] = y.calisan
    bolum = d.index.str[:2]
    lq = (d.l / d.q).replace([np.inf, -np.inf], np.nan)
    d["l_q"] = lq.fillna(lq.groupby(bolum).transform("median")).fillna(lq.median())
    d["ic_satis"] = (d.q - d.x).clip(lower=0).fillna(0)

    # TR tarifesi (AB menşeli ithalata, c2) ve STA dışı ithalat payı: HS6 → sınıf ağırlıkları
    h = pd.read_csv(v("politika_tarife_hs6.csv"), dtype={"hs6": str})
    baskin = (h.m_ab_musd / (h.m_ab_musd + h.m_diger_musd).replace(0, np.nan)).fillna(0) >= 0.5
    guclu = h.gizli.astype(bool) | (h.uretim_ithalat_orani >= 1.0)
    h["oran_c2"] = np.where(baskin & ~guclu, h.t_mfn, h.t_tam) * h.rejim.isin(["GB", "ITU"])
    h["w_c2"] = h.m_ab_musd * h.oran_c2
    ag = f3a.hs6_nace_agirlik(v("cn2025_nace_rejim.csv"))
    hn, _ = f3a.nace_dagit(h[["hs6", "m_ab_musd", "m_sta_musd", "m_diger_musd", "m_toplam_musd", "w_c2"]], ag,
                           ["m_ab_musd", "m_sta_musd", "m_diger_musd", "m_toplam_musd", "w_c2"], [])
    hn = hn.set_index("nace2")
    d["tau_tr_c2"] = (hn.w_c2 / hn.m_ab_musd.replace(0, np.nan)).reindex(d.index).fillna(0)
    d["sta_disi_pay"] = (hn.m_diger_musd / hn.m_toplam_musd.replace(0, np.nan)).reindex(d.index).fillna(0.5)
    # iç satış güvenilir değilse (ihracat ≥ üretimin %80'i ya da üretim yok) I-O ürününün hanehalkı ithal payına düşülür
    d["io"] = [io.io_kodu(int(k[:2])) for k in d.index]
    e = pd.read_csv(v("politika_io_ede.csv")).set_index("io")
    # iç satış en az üretimin %20'si sayılır (ihracat, YSHİ üretimini aşıyorsa sınıflama farkı); üretim yoksa I-O payı
    d["ic_satis_guvenilir"] = d.ic_satis > 0.2 * d.q.fillna(0)
    d["ic_satis"] = np.fmax(d.ic_satis, 0.2 * d.q.fillna(0))
    yedek = 1 - d.io.map(e.ithal_payi_hh).fillna(0.3)
    d["yerli_pay"] = np.where(d.q.fillna(0) > 0,
                              d.ic_satis / (d.ic_satis + (d.m - d.m_ab).clip(lower=0)).replace(0, np.nan), yedek)
    d["yerli_pay"] = d.yerli_pay.fillna(yedek)
    rj = pd.read_csv(v("cn2025_nace_rejim.csv"), dtype={"cn8": str, "nace2": str})
    rj = rj[rj.agirlik > 0]
    rj["m_f3"] = rj.tr_ith_ab / rj.agirlik * rj.agirlik_f3
    pm = rj.groupby("nace2").apply(lambda g: g.m_f3[g.rejim.isin(["GB", "ITU"])].sum() / max(g.m_f3.sum(), 1e-9),
                                   include_groups=False)
    d["q_gb_itu_m"] = pm.reindex(d.index).fillna(1.0)

    # AB tarafı tarife, rejim payları, çabuk bozulan pay
    for c in ("tau_ab_s4", "tau_ab_s4_tarim_kaybi", "pay_GB", "pay_ITU", "pay_TARIM"):
        d[c] = ab[c].reindex(d.index).fillna(0)
    kn8["cabuk"] = kn8.cn8.apply(lambda k: k.startswith(CABUK) and not k.startswith(CABUK_HARIC)) & \
        kn8.rejim.isin(["GB", "ITU"])
    cb = kn8.groupby("nace2").apply(lambda g: (g.x_ab_meur * g.cabuk).sum() / max(g.x_ab_meur.sum(), 1e-9),
                                    include_groups=False)
    d["cabuk_pay"] = cb.reindex(d.index).fillna(0)
    d["ce_pay"] = 0.0          # CE/onaylanmış kuruluş bağımlılığı: 10–12'de yok; diğer bölümler kendi parçalarında
    d["q_gb_itu"] = d.pay_GB + d.pay_ITU

    # σ
    sig, sig_med = sigma_sinif(yollar.girdi("cepii", "ProTEE_0_1.csv"), kn8)
    d["sigma"] = sig.reindex(d.index).fillna(sig_med).clip(2, 15)

    # menşe varsayımları: sınıf tablosu, yoksa I-O sektörü PEM riski (Faz 2C)
    pem = pd.read_csv(v("hazirlik_pem_mense.csv")).set_index("io").risk
    va = pd.read_csv(v("f3_sinif_varsayim.csv"), dtype={"kod": str}).set_index("kod")
    for c in ("risk_s2", "c_roo_s2", "p_uyum_s2", "risk_s3", "c_roo_s3", "p_uyum_s3", "vz_carpani"):
        d[c] = va[c].reindex(d.index)
    vars_ = d.io.map(pem).fillna("düşük").map(VARSAYILAN_MENSE)
    d["mense_kaynak"] = np.where(d.c_roo_s2.notna(), "sınıf", "varsayılan (I-O PEM riski)")
    for j, c in enumerate(("risk_s2", "c_roo_s2", "p_uyum_s2", "c_roo_s3", "p_uyum_s3")):
        d[c] = d[c].fillna(vars_.str[j])
    d["risk_s3"] = d.risk_s3.fillna(d.risk_s2)
    d["vz_carpani"] = d.vz_carpani.fillna(1.0)

    # I-O: ithal girdi içeriği ve EDE
    m_tot, m_dog = ithal_icerik(a.cache)
    d["m_x"] = d.io.map(m_tot)
    d["m_x_dogrudan"] = d.io.map(m_dog)
    dolayli_io = (e.ede_tum_bp - e.agirlik_tufe * e.ithal_payi_hh * 100).clip(lower=0)
    m_io = d.groupby("io").m.transform("sum")
    tufe = pd.read_csv(v("tuik_tufe_agirlik_2026.csv"), dtype={"coicop_2018": str})
    tufe = tufe[tufe.duzey == 5].set_index("coicop_2018").agirlik_yuzde
    cn = pd.read_csv(v("f3_coicop_nace.csv"), dtype={"coicop": str, "kod": str})
    cn["w"] = cn.coicop.map(tufe) * cn.pay
    d["tufe_agirlik_yuzde"] = cn.groupby("kod").w.sum().reindex(d.index).fillna(0)
    # tüketimde ithal pay: I-O ürününün hanehalkı ithal payı × sınıfın göreli ithalat yoğunluğu (M/(M+X), I-O ortalamasına
    # göre; 0,25–3 aralığı). Sınıf üretimi (YSHİ) ile ihracat (BACI) sınıflama farkından bağımsızdır [T].
    mx = (d.m / (d.m + d.x)).replace([np.inf, -np.inf], np.nan)
    mx_io = d.groupby("io").m.transform("sum") / (d.groupby("io").m.transform("sum") + d.groupby("io").x.transform("sum"))
    d["ithalat_payi"] = (d.io.map(e.ithal_payi_hh) * (mx / mx_io).clip(0.25, 3)).clip(upper=0.95).fillna(0)
    d.loc[d.m <= 0, "ithalat_payi"] = 0.0
    d["ithal_penetrasyon"] = (d.m / (d.m + d.ic_satis)).where(d.q.fillna(0) > 0)   # arketip için (ara/sermaye dahil)
    d["ede_dogrudan_bp"] = d.tufe_agirlik_yuzde / 100 * d.ithalat_payi * 100
    d["ede_dolayli_bp"] = d.io.map(dolayli_io).fillna(0) * (d.m / m_io).fillna(0)
    d["ede_tum_bp"] = d.ede_dogrudan_bp + d.ede_dolayli_bp
    d["ab_ithalat_payi"] = (d.m_ab / d.m).fillna(0)
    d["ede_ab_bp"] = d.ede_tum_bp * d.ab_ithalat_payi
    d["ede_sta_disi_bp"] = d.ede_tum_bp * d.sta_disi_pay

    # GE hedefleri
    c = pd.read_csv(v("politika_cekim_senaryolar.csv"))
    c = c[c.spesifikasyon.eq("GE_tam_sigma7")]
    ge = {(s, yon): c[(c.senaryo == s) & (c.yon == yon)].iloc[0]
          for s in ("S2", "S3_TR", "S4") for yon in ("TR→AB", "AB→TR", "TR toplam ihracat")}
    ab_payi = t.x_ab_musd_2024.sum() / t.x_musd_2024.sum()
    delta = {s: 1 - ge[(g, "TR toplam ihracat")].degisim_yuzde / (ge[(g, "TR→AB")].degisim_yuzde * ab_payi)
             for s, g in (("S2", "S2"), ("S3", "S3_TR"), ("S4", "S4"))}

    n = a.n
    K = len(d)
    ortak = dict(sig=rng.lognormal(0, 0.25, n), ntm=ucgen(rng, 0.5, 1.0, 2.0, n), ntm_c=ucgen(rng, 0.5, 1.0, 2.0, n),
                 ce=ucgen(rng, 1.0, 2.0, 4.0, n), pu=rng.uniform(-0.05, 0.05, n), dl=rng.uniform(-0.10, 0.10, n),
                 rho=ucgen(rng, 0.6, 0.8, 1.0, n), theta=ucgen(rng, 0.1, 0.3, 0.5, n),
                 tarim=rng.uniform(0, 1, n) < 0.25)
    sinif_sig = rng.lognormal(0, 0.15, (n, K))
    sinif_pu = rng.uniform(-0.10, 0.10, (n, K))
    sinif_c = rng.lognormal(0, 0.30, (n, K))
    V = {c_: d[c_].to_numpy(float) for c_ in ("x_ab", "m_ab", "sigma", "tau_ab_s4", "tau_ab_s4_tarim_kaybi", "q_gb_itu",
                                              "cabuk_pay", "ce_pay", "tau_tr_c2", "q_gb_itu_m", "yerli_pay", "l_q", "m_x", "ede_ab_bp",
                                              "c_roo_s2", "p_uyum_s2", "c_roo_s3", "p_uyum_s3")}
    for k_ in ("x_ab", "m_ab"):
        V[k_] = np.nan_to_num(V[k_])

    def pe(s, merkez=False):
        """Ölçeksiz kısmi denge: AB ihracatı ve ithalatı değişimi, fiyat kamaları ve ortak parametreler."""
        if merkez:
            o = dict(sig=np.ones(1), ntm=np.ones(1), ntm_c=np.ones(1), ce=np.full(1, 2.0), pu=np.zeros(1), dl=np.zeros(1),
                     rho=np.full(1, 0.8), theta=np.full(1, 0.3), tarim=np.zeros(1, bool))
            ss, sp, sc = np.ones((1, K)), np.zeros((1, K)), np.ones((1, K))
        else:
            o, ss, sp, sc = ortak, sinif_sig, sinif_pu, sinif_c
        sg = V["sigma"] * o["sig"][:, None] * ss
        f = PAYLAR[s]["ntm"]          # S2: AEO karşılıklı tanıma ve tek pencereyle sınır sürtünmesi yarıya iner [H]
        ntm = f * (V["q_gb_itu"] * o["ntm"][:, None] + V["cabuk_pay"] * o["ntm_c"][:, None]) / 100
        ntm_m = f * V["q_gb_itu_m"] * o["ntm"][:, None] / 100
        ek = np.zeros((len(o["sig"]), K))
        if s == "S4":
            ce = V["ce_pay"] * o["ce"][:, None] / 100
            te = V["tau_ab_s4"] / 100 + ntm + ce
            te_t = np.where(o["tarim"][:, None], V["tau_ab_s4_tarim_kaybi"] / 100 + ntm + ce, te)
            ek = V["x_ab"] * ((1 + te_t) ** (-sg) - (1 + te) ** (-sg))     # 1/98 kaybının ek kısmi denge kaybı
            tm = V["tau_tr_c2"] / 100 + ntm_m
        else:
            j = s[-1]
            pu = np.clip(V[f"p_uyum_s{j}"] + o["pu"][:, None] + sp, 0.05, 0.98)
            cr = V[f"c_roo_s{j}"] * sc / 100
            ce = V["ce_pay"] * o["ce"][:, None] / 100 * (0.25 if s == "S2" else 1.0)
            te = (1 - pu) * V["tau_ab_s4"] / 100 + V["q_gb_itu"] * pu * cr + ntm + ce
            p_ab, c_ab = PAYLAR[s]["p_ab"], PAYLAR[s]["c_ab"] / 100
            tm = (1 - p_ab) * V["tau_tr_c2"] / 100 + V["q_gb_itu_m"] * p_ab * c_ab + ntm_m
        return dict(px=V["x_ab"] * ((1 + te) ** (-sg) - 1), pm=V["m_ab"] * ((1 + tm) ** (-sg) - 1), ek=ek,
                    dlt=np.clip(delta[s] + o["dl"][:, None], 0, 0.6), rho=o["rho"][:, None], theta=o["theta"][:, None],
                    te=te, tm=tm)

    def dagit(deger, hedef, taban):
        """Çekiliş başına toplam = hedef oran × Σ taban. Hedef < 0: kısmi denge kaybı paylarıyla; ≥ 0: tabanla orantılı."""
        top = deger.sum(axis=1, keepdims=True)
        kayip = hedef[:, None] * taban.sum() * deger / np.where(top < 0, top, -1e-9)
        return np.where(hedef[:, None] < 0, kayip, hedef[:, None] * taban[None, :])

    def sonuc(p, gx, gm, k_merkez):
        # 1/98 kaybı GE toplamına eklenir (yeniden dağıtılmaz): aynı çekilişin ölçeğiyle
        top = p["px"].sum(axis=1)
        kj = np.where(gx < 0, gx * V["x_ab"].sum() / np.where(top < 0, top, -1e-9), k_merkez)
        dx_ab = dagit(p["px"], gx, V["x_ab"]) + kj[:, None] * p["ek"]
        dm_ab = dagit(p["pm"], gm, V["m_ab"])
        dx = dx_ab * (1 - p["dlt"])
        dd = -dm_ab * V["yerli_pay"]
        dq = dx + dd
        return dict(dx_ab=dx_ab, dx=dx, dm_ab=dm_ab, dm=dm_ab * V["yerli_pay"], dd=dd, dq=dq,
                    dl=dq * V["l_q"] * (1 - p["theta"]), dca=dq * (1 - V["m_x"]),
                    dtufe=V["ede_ab_bp"] * p["tm"] * 100 * p["rho"], te=p["te"] + 0 * dq, tm=p["tm"] + 0 * dq)

    # GE çekilişleri: ortak z (S2, S4; ihracat ve ithalat), SH = (üst − alt) / (2 × 1,645); S3 kısmi denge yapısıyla ara değer
    z = rng.standard_normal(n)
    hedef, merkez_hedef = {}, {}
    for s_ in ("S2", "S4"):
        for yon, ad in (("TR→AB", "x"), ("AB→TR", "m")):
            g = ge[(s_, yon)]
            se = (g.ci90_ust_yuzde - g.ci90_alt_yuzde) / (2 * 1.645)
            hedef[(s_, ad)] = (g.degisim_yuzde + z * se) / 100
            merkez_hedef[(s_, ad)] = np.array([g.degisim_yuzde / 100])
    pm_ = {s_: pe(s_, merkez=True) for s_ in ("S2", "S3", "S4")}
    agirlik_s3 = {}
    for ad, anahtar, taban in (("x", "px", V["x_ab"]), ("m", "pm", V["m_ab"])):
        oran = {s_: pm_[s_][anahtar].sum() / taban.sum() for s_ in pm_}
        agirlik_s3[ad] = (oran["S3"] - oran["S2"]) / (oran["S4"] - oran["S2"])
        for hd in (hedef, merkez_hedef):
            hd[("S3", ad)] = hd[("S2", ad)] + agirlik_s3[ad] * (hd[("S4", ad)] - hd[("S2", ad)])
    olcek = {s_: (merkez_hedef[(s_, "x")][0] * V["x_ab"].sum() / pm_[s_]["px"].sum(),
                  merkez_hedef[(s_, "m")][0] * V["m_ab"].sum() / pm_[s_]["pm"].sum()) for s_ in pm_}

    satirlar, ozet = [], []
    deg = ["dx_ab", "dx", "dm_ab", "dm", "dd", "dq", "dl", "dca", "dtufe", "te", "tm"]
    for s in ("S2", "S3", "S4"):
        r = sonuc(pe(s), hedef[(s, "x")], hedef[(s, "m")], olcek[s][0])
        rm = sonuc(pm_[s], merkez_hedef[(s, "x")], merkez_hedef[(s, "m")], olcek[s][0])
        for dg in deg:
            q = np.percentile(r[dg], [10, 50, 90], axis=0)
            for i, kod in enumerate(d.index):
                satirlar.append(dict(kod=kod, senaryo=s, degisken=dg, p10=q[0, i], p50=q[1, i], p90=q[2, i],
                                     merkez=rm[dg][0, i]))
        istihdam_pay = r["dl"] / d.l.to_numpy(float)
        toplam = {dg: np.percentile(r[dg].sum(axis=1), [10, 50, 90]) for dg in ("dx_ab", "dx", "dm_ab", "dq", "dl", "dca",
                                                                                "dtufe")}
        ozet.append(dict(senaryo=s, olcek_ihracat=olcek[s][0], olcek_ithalat=olcek[s][1], delta=delta[s],
                         s3_agirlik_ihracat=agirlik_s3["x"], s3_agirlik_ithalat=agirlik_s3["m"],
                         ab_ihracat_degisim_yuzde_p50=100 * toplam["dx_ab"][1] / V["x_ab"].sum(),
                         ab_ihracat_degisim_yuzde_p10=100 * toplam["dx_ab"][0] / V["x_ab"].sum(),
                         ab_ihracat_degisim_yuzde_p90=100 * toplam["dx_ab"][2] / V["x_ab"].sum(),
                         **{f"{dg}_{p}": toplam[dg][j] for dg in toplam for j, p in enumerate(("p10", "p50", "p90"))},
                         kayip_5yuzde_ustu_sinif_p50=int((np.nanmedian(istihdam_pay, axis=0) < -0.05).sum()),
                         kayip_5yuzde_ustu_sinif_p10=int((np.nanpercentile(istihdam_pay, 10, axis=0) < -0.05).sum())))
    sn = pd.DataFrame(satirlar)
    sn.round(4).to_csv(v("f3_senaryo_sinif.csv"), index=False)
    oz = pd.DataFrame(ozet)
    oz.round(4).to_csv(v("f3_senaryo_ozet.csv"), index=False)

    # CKE
    sgm = d.sigma
    m_sd = (d.m * d.sta_disi_pay).fillna(0)
    dd_t = (-(m_sd * ((1.01) ** (-sgm) - 1)) * d.yerli_pay).clip(upper=0.03 * d.q.fillna(0))
    ca_t = 4.3 * dd_t * (1 - d.m_x) - 0.6 * dd_t
    d["cke_tufe_musd_bp"] = ca_t / (d.ede_sta_disi_bp * 0.8).replace(0, np.nan)
    dd_m = (sgm * 0.01 * d.m * d.ic_satis / (d.ic_satis + d.m)).clip(upper=0.03 * d.q.fillna(0)).fillna(0)
    ca_m = 4.3 * dd_m * (1 - d.m_x) - 0.6 * dd_m
    maliyet = 5 * 0.01 * d.ic_satis * usd_try_2026 / 1e3          # mlr TL
    d["cke_mali_musd_mlrtl"] = ca_m / maliyet.replace(0, np.nan)
    d["cke_ca5_tarife_musd"] = ca_t
    d["cke_ca5_mali_musd"] = ca_m
    d["usd_try_2026"] = usd_try_2026
    d.round(5).to_csv(v("f3_makro_sinif.csv"))

    pd.set_option("display.width", 250)
    print("δ:", {s: round(x, 3) for s, x in delta.items()}, "| ölçek (ihracat, ithalat):",
          {s: tuple(round(x, 3) for x in o) for s, o in olcek.items()})
    print(oz[["senaryo", "ab_ihracat_degisim_yuzde_p10", "ab_ihracat_degisim_yuzde_p50", "ab_ihracat_degisim_yuzde_p90",
              "dq_p50", "dl_p10", "dl_p50", "dl_p90", "dca_p50", "dtufe_p50", "kayip_5yuzde_ustu_sinif_p50"]]
          .round(1).to_string(index=False))
    print(f"Σ EDE_tüm (C sınıfları) {d.ede_tum_bp.sum():.2f} bp; I-O C ürünleri toplamı "
          f"{e.loc[e.index.str.startswith('C'), 'ede_tum_bp'].sum():.2f} bp; σ medyan {d.sigma.median():.2f}")


if __name__ == "__main__":
    main()
