"""Faz 2C — Karar öncesi STA ağının değeri: Türkiye'nin AB'nin STA ortaklarıyla kendi STA'larını yapması.

Soru: Türkiye, AB'nin STA ortağı olup kendisinin STA'sı olmayan 33 pazarla (Faz 1 §2.1) çıkıştan önce STA yaparsa
(i) GB içinde kalınırsa (S0) ne kazanır, (ii) anlaşmasız çıkışın (S4) kaybının ne kadarını telafi eder?

Yöntem: f2f_cekim_modeli.py'nin genel denge modülü (2019 kesiti, kesin şapka cebiri, Armington-CES, σ = 5 ve 7).
  - S4: TR↔AB27 ticaret maliyeti GB etkisi kadar artar, τ̂ = exp(−β_GB); β_GB, M1 (PPML) tahmininden
    N(β̂, V̂) çekilişleriyle (1.000; %90 GA).
  - STA: ortak k'nin Türk ihracatına uyguladığı MFN (WITS, ortağın son yılı, HS6 basit ortalama, BACI 2024 Türk
    ihracatıyla ağırlıklı) ve Türkiye'nin k menşeli ithalata uyguladığı MFN + İGV (2026, GTİP12 → HS6 ortalama;
    HS6 bulunamazsa HS4 ortalaması; BACI 2024 ithalatıyla ağırlıklı) sıfırlanır: τ̂_TR,k = (1 + t_k)^θ,
    τ̂_k,TR = (1 + t_TR,k)^θ, θ = σ − 1.
  - Kapsam: sanayi (HS 25–97) tam serbest, tarım değişmez (temel); bütün ürünler (üst sınır).
  - Gümrük geliri GE'de yok (buzdağı maliyeti varsayımı); STA'ların statik gelir kaybı ayrıca verilir.
  - Tarifeler dışındaki STA etkisi (kural, hizmet, yatırım) dahil değil; AB'nin derin STA'larında ek etki +%10
    (Faz 2B, M1), TR'nin diğer STA'larında ≈0 (RTA_DIGER). Bu yüzden sonuçlar tarife kanalıyla sınırlı.

Çıktılar:
  veri/hazirlik_sta_tarife.csv   ortak: ağırlıklı tarifeler (iki yön, sanayi/tümü), ticaret 2024, GE örneğinde mi
  veri/hazirlik_sta_ge.csv       senaryo × σ × ölçü: merkez ve %90 GA

Kullanım: python3 f2g_hazirlik_sta_ge.py [--cekilis 1000]
"""

import argparse
import os

import numpy as np
import pandas as pd

import f1c_sta_asimetrisi as f1c
import f2f_cekim_modeli as cm
import yollar

GRUPLAR = {
    "ileri": ["JPN", "CAN", "AUS", "NZL"],
    "yukselen": ["IND", "MEX", "BRA", "ARG", "URY", "PRY", "IDN", "ZAF", "VNM"],
}
GRUP_ADI = {"ileri": "İleri ekonomiler (Japonya, Kanada, Avustralya, Yeni Zelanda)",
            "yukselen": "Büyük yükselen pazarlar (Hindistan, Meksika, Mercosur, Endonezya, GAGB, Vietnam)",
            "diger": "Diğer (Afrika, Orta ve Güney Amerika, Karayipler)", "hepsi": "33 pazarın tamamı"}


def sanayi_mi(hs6):
    return hs6.str[:2].astype(int).between(25, 97)


def tarifeler(veri, girdi):
    """Ortak bazında iki yönlü ağırlıklı tarife (%), BACI 2024."""
    b = pd.read_csv(os.path.join(girdi, "baci", "baci_hs17_tur_bilateral_hs6_2020_2024.csv.gz"),
                    dtype={"hs6": str, "partner_iso3": str})
    b = b[b.year == 2024]
    b["hs6"] = b.hs6.str.zfill(6)
    tr = pd.read_csv(os.path.join(veri, "tarife_tr_2026_gtip12.csv"), dtype={"hs6": str, "gtip12": str})
    tr = tr[~tr.in_tgtc_only]
    t6 = tr.groupby("hs6").mfn_igv_emy.mean()
    t4 = tr.groupby(tr.hs6.str[:4]).mfn_igv_emy.mean()
    satirlar = []
    for kod3, wits, *_ in f1c.ORTAKLAR:
        mfn, yil = f1c.wits_mfn(wits, os.path.join(girdi, "f1", "wits"))
        x = b[(b.partner_iso3 == kod3) & (b.flow == "X")].groupby("hs6").value_kusd.sum()
        m = b[(b.partner_iso3 == kod3) & (b.flow == "M")].groupby("hs6").value_kusd.sum()
        sat = dict(iso3=kod3, wits_yili=yil, ihracat_2024_musd=x.sum() / 1e3, ithalat_2024_musd=m.sum() / 1e3)
        xm = pd.DataFrame({"x": x, "t": x.index.map(mfn)})
        xm = xm[xm.t.notna()]
        mm = pd.DataFrame({"m": m, "t": m.index.map(t6)})
        mm["t"] = mm.t.fillna(pd.Series(m.index.str[:4].map(t4), index=m.index))
        mm = mm[mm.t.notna()]
        for ad, d, w in (("ortak_mfn", xm, "x"), ("tr_tarife", mm, "m")):
            for kapsam, maske in (("tumu", np.ones(len(d), bool)), ("sanayi", sanayi_mi(d.index.to_series()).to_numpy())):
                dd = d[maske]
                sat[f"{ad}_{kapsam}"] = (dd[w] * dd.t).sum() / dd[w].sum() if dd[w].sum() > 0 else 0.0
                sat[f"{ad}_{kapsam}_kapsama"] = dd[w].sum() / d[w].sum() if d[w].sum() > 0 else np.nan
        sat["tr_gelir_kaybi_sanayi_musd"] = (mm.m * mm.t / 100)[sanayi_mi(mm.index.to_series()).to_numpy()].sum() / 1e3
        sat["tr_gelir_kaybi_tumu_musd"] = (mm.m * mm.t / 100).sum() / 1e3
        sat["tr_ihracat_vergisi_sanayi_musd"] = (xm.x * xm.t / 100)[sanayi_mi(xm.index.to_series()).to_numpy()].sum() / 1e3
        satirlar.append(sat)
    return pd.DataFrame(satirlar)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=yollar.GIRDI)
    ap.add_argument("--out", default=yollar.VERI)
    ap.add_argument("--cekilis", type=int, default=1000)
    a = ap.parse_args()
    c = os.path.join(a.cache, "f2_cekim")

    tt = tarifeler(a.out, a.cache)

    # M1 ve GE tabanı (f2f ile aynı veri ve örnek)
    g, ulke_bilgi = cm.gravity_oku(c)
    t = cm.uyumlastir(g)
    gsyh = cm.gsyh_tablosu(g)
    del g
    sec, _ = cm.ulke_sec(t, ulke_bilgi, 150)
    rs = cm.rta_suresi(t)
    etiket, _, kaynak, yillar, tur, sinif, _, kume = cm.SPEC[0]
    assert etiket == "M1_ana"
    p = cm.kuklalar(cm.panel(t, sec, kaynak, yillar), rs, sinif)
    r = cm.tahmin(p, cm.degiskenler(p, tur), kume=kume)
    X, ulke, _ = cm.ge_matrisi(c, t, sec, ulke_bilgi, gsyh)
    idx = {u: k for k, u in enumerate(ulke)}
    tr = idx[cm.TR]
    ab_i = np.array([idx[u] for u in ulke if u in cm.AB_UYELIK and u != "GBR"])
    tt["ge_orneginde"] = tt.iso3.isin(idx)
    hepsi = tt[tt.ge_orneginde].iso3.tolist()
    gruplar = {**GRUPLAR, "diger": [u for u in hepsi if u not in GRUPLAR["ileri"] + GRUPLAR["yukselen"]], "hepsi": hepsi}
    tt["grup"] = tt.iso3.map({u: k for k, L in GRUPLAR.items() for u in L}).fillna("diger")
    tt.round(4).to_csv(os.path.join(a.out, "hazirlik_sta_tarife.csv"), index=False)

    adlar = ["GB_TR_AB", "GB_AB_TR"]
    b = r["b"][adlar].to_numpy()
    V = r["V"].loc[adlar, adlar].to_numpy()
    rng = np.random.default_rng(20261018)
    cek = np.vstack([b, rng.multivariate_normal(b, V, size=a.cekilis)])
    t_ort = tt.set_index("iso3")

    # (senaryo, ortak grubu, ürün kapsamı, yön): "iki" = karşılıklı STA; "pazar" = yalnız Türk ihracatının
    # karşılaştığı tarife sıfırlanır (ithalat serbestleşmesinin buzdağı varsayımıyla şişen refah etkisini ayırmak için)
    senaryolar = [("S4", None, None, None), ("S0+STA_hepsi", "hepsi", "sanayi", "iki"),
                  ("S0+STA_hepsi_pazar", "hepsi", "sanayi", "pazar")]
    senaryolar += [(f"S4+STA_{k}", k, "sanayi", "iki") for k in ("ileri", "yukselen", "diger", "hepsi")]
    senaryolar += [("S4+STA_hepsi_pazar", "hepsi", "sanayi", "pazar"), ("S4+STA_hepsi_tumu", "hepsi", "tumu", "iki")]
    ihr0 = X[tr].sum() - X[tr, tr]
    ith0 = X[:, tr].sum() - X[tr, tr]
    k_hepsi = np.array([idx[u] for u in hepsi])
    satirlar = []
    for theta in (4.0, 6.0):
        for sen, grup, kapsam, yon in senaryolar:
            sta = np.ones_like(X)
            if grup:
                for u in gruplar[grup]:
                    k = idx[u]
                    sta[tr, k] = (1 + t_ort.loc[u, f"ortak_mfn_{kapsam}"] / 100) ** theta
                    if yon == "iki":
                        sta[k, tr] = (1 + t_ort.loc[u, f"tr_tarife_{kapsam}"] / 100) ** theta
            cikis = sen.startswith("S4")
            sonuc = []
            p0 = None
            for j, bb in enumerate(cek if cikis else cek[:1]):
                tau = sta.copy()
                if cikis:
                    tau[tr, ab_i] *= np.exp(-bb[0])
                    tau[ab_i, tr] *= np.exp(-bb[1])
                Xn, pp, P = cm.ge_coz(X, tau, theta, p0=p0)
                p0 = pp
                reel = pp / P
                sonuc.append({"cekilis": j,
                              "TR reel GSYH (refah vekili)": reel[tr] - 1,
                              "TR toplam ihracat": (Xn[tr].sum() - Xn[tr, tr]) / ihr0 - 1,
                              "TR toplam ithalat": (Xn[:, tr].sum() - Xn[tr, tr]) / ith0 - 1,
                              "TR→AB": Xn[tr, ab_i].sum() / X[tr, ab_i].sum() - 1,
                              "TR→33 pazar": Xn[tr, k_hepsi].sum() / X[tr, k_hepsi].sum() - 1})
            d = pd.DataFrame(sonuc)
            for olcu in [c_ for c_ in d.columns if c_ != "cekilis"]:
                nokta = d.loc[d.cekilis == 0, olcu].iloc[0]
                q = d.loc[d.cekilis > 0, olcu].quantile([0.05, 0.95]) if cikis else pd.Series([np.nan, np.nan])
                satirlar.append(dict(senaryo=sen, grup=grup or "", kapsam=kapsam or "", yon=yon or "", sigma=int(theta + 1),
                                     olcu=olcu, degisim_yuzde=100 * nokta, ci90_alt_yuzde=100 * q.iloc[0],
                                     ci90_ust_yuzde=100 * q.iloc[1],
                                     ortak_sayisi=len(gruplar[grup]) if grup else 0))
            print(f"σ={theta + 1:.0f} {sen:20s} GSYH {100 * d.loc[0, 'TR reel GSYH (refah vekili)']:+.3f}%  "
                  f"ihracat {100 * d.loc[0, 'TR toplam ihracat']:+.2f}%  TR→AB {100 * d.loc[0, 'TR→AB']:+.2f}%",
                  flush=True)
    s = pd.DataFrame(satirlar)
    # telafi oranı: STA'nın S4 kaybının ne kadarını kapattığı (merkez)
    s4 = s[s.senaryo == "S4"].set_index(["sigma", "olcu"]).degisim_yuzde
    s["s4_kaybini_telafi_orani"] = [
        (r_.degisim_yuzde - s4[(r_.sigma, r_.olcu)]) / -s4[(r_.sigma, r_.olcu)]
        if r_.senaryo.startswith("S4+") and s4[(r_.sigma, r_.olcu)] < 0 else np.nan for r_ in s.itertuples()]
    s.round(5).to_csv(os.path.join(a.out, "hazirlik_sta_ge.csv"), index=False)
    print("GE örneğindeki pazarlar:", len(hepsi), "/", len(tt), "; 2024 Türk ihracatındaki payları:",
          round(tt[tt.ge_orneginde].ihracat_2024_musd.sum() / tt.ihracat_2024_musd.sum(), 3))


if __name__ == "__main__":
    main()
