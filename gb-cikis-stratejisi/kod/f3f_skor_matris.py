"""Faz 3 — Bileşik skorlar (KS, SS, AME, EDE, CKE), arketip ve duruş, ağırlık duyarlılığı; ana matris (veri/nace_matris.csv).

Skorlar 0–100; C bölümü sınıfları içinde yüzdelik sıra (ana prompt 2.1). Bileşeni eksik sınıfta ağırlıklar yeniden ölçeklenir.
KS = 0,20 RCA (0,7 × log RCA 2024 + 0,3 × Δlog RCA 2020–24) + 0,20 PCI (TR ihracatı ağırlıklı; yoksa dünya)
   + 0,15 yurt içi KD (0,5 × KD/üretim + 0,5 × (1 − m^X)) + 0,15 Ar-Ge yoğunluğu (OECD sınıflaması: Galindo-Rueda ve
   Verger 2016; yüksek 100, orta-yüksek 75, orta 50, orta-düşük 25) + 0,10 tedarikçi derinliği (I-O yurt içi geri bağlantı)
   + 0,10 AB'ye göre verimlilik + 0,10 firma çeşitliliği (0,5 × log 10+ çalışanlı girişim + 0,5 × (1 − 250+ istihdam payı))
SS = 0,7 × en yüksek boyut + 0,3 × ağırlıklı ortalama (savunma 0,20; ikili kullanım 0,10; enerji 0,15; sağlık 0,15;
   gıda 0,15; dijital 0,10; kritik hammadde 0,15) — boyutlar veri/f3_ss_boyutlar.csv [H]
AME (ham, puan) = AB ihracat payı × (τ_AB,beklenen + q·c_RoO,S2 + q·%1 sınır + %2·CE payı) × değer zinciri çarpanı;
   τ_AB,beklenen = τ_S4 + 0,25 × (τ_S4,1/98 kaybı − τ_S4); q = GB + İTÜ payı
EDE = 1 puan tarifenin (tüm menşeler) TÜFE etkisi, bp (f3e); CKE = 0,5 × yüzdelik(CKE_TÜFE) + 0,5 × yüzdelik(CKE_mali)
Ağırlık duyarlılığı: eşit, ticaret ağırlıklı, yapı ağırlıklı ve Dirichlet (α = 20·w, 1000 çekiliş) ağırlıklarla KS sırası;
   Spearman korelasyonu ve sınıf sırasının P10–P90 aralığı.
Arketip kuralları (başlangıç tipolojisi, ana prompt 2.2) ve duruş: kod içindeki `arketipler` ve `durus`.

Çıktı: veri/nace_matris.csv, veri/f3_ks_duyarlilik.csv
"""

import argparse
import glob
import os

import numpy as np
import pandas as pd
import yaml

import f2a_io_fiyat as io
import yollar

KS_W = {"rca": 0.20, "pci": 0.20, "kd": 0.15, "arge": 0.15, "tedarik": 0.10, "verim": 0.10, "firma": 0.10}
SS_W = {"savunma": 0.20, "ikili": 0.10, "enerji": 0.15, "saglik": 0.15, "gida": 0.15, "dijital": 0.10, "hammadde": 0.15}
SS_AD = {"savunma": "savunma", "ikili": "ikili kullanım", "enerji": "enerji dönüşümü", "saglik": "sağlık", "gida": "gıda güvenliği",
         "dijital": "dijital", "hammadde": "kritik hammadde"}
EDE_ESIK = 0.3        # bp / puan: 10 puanlık tarife ≈ 3 bp (yıllık bütçenin %10'u) [H]
ALT_W = {"esit": {k: 1 / 7 for k in KS_W},
         "ticaret": {"rca": 0.35, "pci": 0.30, "kd": 0.10, "arge": 0.10, "tedarik": 0.05, "verim": 0.05, "firma": 0.05},
         "yapi": {"rca": 0.05, "pci": 0.05, "kd": 0.25, "arge": 0.25, "tedarik": 0.15, "verim": 0.15, "firma": 0.10}}


def arge_duzeyi(kod):
    """OECD Ar-Ge yoğunluğu sınıflaması (ISIC Rev. 4 imalat), 1–4."""
    b, g = kod[:2], kod[:4]
    if b in ("21", "26") or g == "30.3":
        return 4
    if b in ("20", "27", "28", "29") or g in ("25.4", "30.2", "30.4", "30.9", "32.5"):
        return 3
    if b in ("22", "23", "24", "33") or g == "30.1" or (b == "32" and g != "32.5"):
        return 2
    return 1


def yuzdelik(s, ters=False):
    r = s.rank(pct=True, ascending=not ters) * 100
    return r.where(s.notna())


def ks_hesap(b, w):
    agirlik = pd.DataFrame({k: b[k].notna() * w[k] for k in w})
    toplam = sum(b[k].fillna(0) * w[k] for k in w)
    return toplam / agirlik.sum(axis=1)


def arketipler(r):
    """(arketip, güç) listesi; güce göre sıralı. Eşikler yüzdelik skorlara (0–100) ve mutlak EDE'ye göre [H]."""
    a = []
    ks, ame, ss = r.ks, np.nan_to_num(r.ame_puan), r.ss
    ab, imp, rca = r.ab_ihracat_payi, np.nan_to_num(r.ithal_penetrasyon), np.nan_to_num(r.rca_dunya_2024)
    ede_yuksek = r.ede_tum_bp >= EDE_ESIK
    onemli_ab = r.x_ab >= 50 and r.x_ab >= 0.05 * np.nan_to_num(r.q, nan=r.x)
    if onemli_ab and ab >= 0.25 and ((ame >= 60 and ks >= 50) or (ame >= 70 and ks >= 40)
                                     or (ab >= 0.35 and np.nan_to_num(r.rca_ab_2024) >= 1.5 and ks >= 45)):
        a.append(("A", (ame + ks) / 2 + 10))
    if ab < 0.35 and rca >= 1 and ks >= 45 and r.x >= 50 and r.x >= 0.05 * np.nan_to_num(r.q, nan=r.x):
        a.append(("B", (ks + 100 * (1 - ab)) / 2 + 10 * min(np.log(rca), 2)))
    if ks >= 40 and imp >= 0.40 and not ede_yuksek:
        a.append(("C", (ks + 100 * imp) / 2))
    if ss >= 60:
        a.append(("D", ss))
    if ks < 40 and imp >= 0.50 and ede_yuksek:
        a.append(("E", (100 - ks + 100 * imp) / 2))
    if r.emek_puan >= 65 and r.gerileme and r.ticaret_yogunlugu >= 0.10:
        a.append(("F", r.emek_puan))
    yesil = max(r.skdm_payi, r.eudr_payi)
    if yesil * ab >= 0.08:
        a.append(("G", 50 + 50 * yesil * min(1.0, ab / 0.5)))
    a.sort(key=lambda t: -t[1])
    if not a:
        if r.ticaret_yogunlugu >= 0.15 and rca >= 1:
            a = [("B", 0)]
        elif r.ticaret_yogunlugu >= 0.15 and imp >= 0.5:
            a = [("E" if ede_yuksek else "C", 0)]
        else:
            a = [("—", 0)]
    return a


DURUS = {"A": "Koru", "B": "Geliştir", "C": "Geliştir", "D": "Geliştir", "E": "Serbestleştir", "F": "Yönetilen uyum",
         "G": "Dönüştür", "—": "Koru"}
TARIFE = {"A": "AB ile karşılıklı %0 (S2); girdilerde artış yok; S4'te AB'ye MFN (c2)",
          "B": "Girdilerde %0 (P1); nihai üründe MFN korunur",
          "C": "Bağlı oran içinde süreli koruma; T+3'ten azalan, performans koşullu",
          "D": "Tarife ikincil; MFN korunur",
          "E": "MFN → %0, tüm menşeler (T)",
          "F": "MFN korunur; yeni artış yok",
          "G": "MFN; SKDM/EUDR uyum paketi",
          "—": "Değişiklik yok"}
ARAC = {"A": "S2'de %0 ve elverişli menşe kuralı; ACAA; çapa yatırımcı tutma",
        "B": "Yeni STA'lar; ihracat finansmanı; girdi tarifesi indirimi",
        "C": "Yatırım teşviki; süreli koruma; kamu alımı",
        "D": "Kamu alımı/offset; Ar-Ge; stok güvenliği",
        "E": "Tarifeyi sıfırla; tedarik çeşitlendirme; stok",
        "F": "Dönüşüm desteği; bölgesel politika; yeniden beceri",
        "G": "Karbonsuzlaştırma finansmanı; MRV; EUDR izlenebilirlik",
        "—": "İzleme"}
MUZAKERE = {"A": "savunma", "B": "nötr", "C": "savunma", "D": "nötr", "E": "nötr", "F": "savunma", "G": "hücum", "—": "nötr"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=yollar.GIRDI)
    ap.add_argument("--out", default=yollar.VERI)
    a = ap.parse_args()
    v = lambda f: os.path.join(a.out, f)  # noqa: E731

    t = pd.read_csv(v("f3_ticaret_sinif.csv"), dtype={"nace2": str}).set_index("nace2")
    y = pd.read_csv(v("f3_yapi_sinif.csv"), dtype={"kod": str}).set_index("kod")
    p = pd.read_csv(v("f3_pci_sinif.csv"), dtype={"kod": str}).set_index("kod")
    ab = pd.read_csv(v("f3_ab_tarife_sinif.csv"), dtype={"kod": str}).set_index("kod")
    mk = pd.read_csv(v("f3_makro_sinif.csv"), dtype={"kod": str}).set_index("kod")
    sn = pd.read_csv(v("f3_senaryo_sinif.csv"), dtype={"kod": str})
    ss = pd.read_csv(v("f3_ss_boyutlar.csv"), dtype={"kod": str}).set_index("kod")
    k = pd.read_csv(v("nace_kapsam.csv"), dtype={"kod": str}).set_index("kod")

    d = mk[["x", "x_ab", "m", "m_ab", "q", "l", "io", "sigma", "m_x", "yerli_pay", "ithalat_payi", "ithal_penetrasyon",
            "tau_tr_c2",
            "tufe_agirlik_yuzde", "ede_tum_bp", "ede_ab_bp", "ede_sta_disi_bp", "cke_tufe_musd_bp", "cke_mali_musd_mlrtl",
            "risk_s2", "risk_s3", "c_roo_s2", "p_uyum_s2", "c_roo_s3", "p_uyum_s3", "vz_carpani", "mense_kaynak",
            "q_gb_itu"]].copy()
    d.insert(0, "ad", k.ad_tr.reindex(d.index))
    d.insert(1, "gb_statusu", k.gb_statusu.reindex(d.index))
    d["kd_musd"] = y.kd_musd
    d["gizli_tahmin"] = y.gizli_tahmin
    d["ab_ihracat_payi"] = (d.x_ab / d.x).fillna(0)
    d["ab_ithalat_payi"] = (d.m_ab / d.m).fillna(0)
    for c in ("rca_dunya_2024", "rca_dunya_2020", "rca_ab_2024"):
        d[c] = t[c]
    d["pci"] = p.pci_tr.fillna(p.pci_dunya)
    for c in ("tau_ab_s4", "tau_ab_s4_tarim_kaybi", "tepe_satirlar", "eudr_payi", "skdm_payi"):
        d[c] = ab[c]
    d[["eudr_payi", "skdm_payi"]] = d[["eudr_payi", "skdm_payi"]].fillna(0)
    d["ticaret_yogunlugu"] = ((d.x + d.m) / (d.q + d.m)).fillna(0)

    # KS bileşenleri
    C = d.index.str.match(r"^(1\d|2\d|3[0-3])\.")
    b = pd.DataFrame(index=d.index)
    lr = np.log(d.rca_dunya_2024.where(d.rca_dunya_2024 > 0))
    dl = lr - np.log(d.rca_dunya_2020.where(d.rca_dunya_2020 > 0))
    b["rca"] = 0.7 * yuzdelik(lr[C]) + 0.3 * yuzdelik(dl[C]).fillna(50)
    b["pci"] = yuzdelik(d.pci[C])
    b["kd"] = 0.5 * yuzdelik((d.kd_musd / d.q)[C]).fillna(50) + 0.5 * yuzdelik(1 - d.m_x[C])
    b["arge"] = pd.Series({kd: 25 * arge_duzeyi(kd) for kd in d.index})[C]
    yollar_io = io.io_indir(os.path.join(a.cache, "io2023"))
    yd, kod = io.oku(yollar_io["yurtici"])
    Z_d = yd.iloc[io.SATIR, io.SUTUN].astype(float).to_numpy()
    x = yd.iloc[io.P1, io.SUTUN].astype(float).to_numpy()
    A_d = np.divide(Z_d, x, out=np.zeros_like(Z_d), where=x > 0)
    geri = pd.Series(np.linalg.inv(np.eye(len(x)) - A_d).sum(axis=0), index=kod)
    d["geri_baglanti"] = d.io.map(geri)
    b["tedarik"] = yuzdelik(d.geri_baglanti[C])
    b["verim"] = yuzdelik(y.verimlilik_ab_orani.reindex(d.index)[C])
    n10 = y[["girisim_10_49", "girisim_50_249", "girisim_250p"]].sum(axis=1, min_count=1).reindex(d.index)
    b["firma"] = (0.5 * yuzdelik(np.log1p(n10)[C]) + 0.5 * yuzdelik(-y.buyuk_isletme_istihdam_payi.reindex(d.index)[C])
                  .fillna(50))
    b = b.loc[C]
    d["ks"] = ks_hesap(b, KS_W)
    d["ks_bilesen"] = b.notna().sum(axis=1)
    for c in b.columns:
        d[f"ks_{c}"] = b[c]

    # duyarlılık
    rng = np.random.default_rng(7)
    sira = d.loc[C, "ks"].rank(ascending=False)
    dz = []
    for ad, w in ALT_W.items():
        r2 = ks_hesap(b, w).rank(ascending=False)
        dz.append(dict(agirlik=ad, spearman=sira.corr(r2, method="spearman"),
                       ilk30_ortak=len(set(sira.nsmallest(30).index) & set(r2.nsmallest(30).index))))
    w0 = np.array(list(KS_W.values()))
    cek = rng.dirichlet(20 * w0, 1000)
    siralar = np.column_stack([ks_hesap(b, dict(zip(KS_W, cw))).rank(ascending=False).to_numpy() for cw in cek])
    rho = [pd.Series(siralar[:, j]).corr(pd.Series(sira.to_numpy()), method="spearman") for j in range(len(cek))]
    dz.append(dict(agirlik="dirichlet_p10", spearman=float(np.percentile(rho, 10)), ilk30_ortak=np.nan))
    pd.DataFrame(dz).round(4).to_csv(v("f3_ks_duyarlilik.csv"), index=False)
    d.loc[C, "ks_sira"] = sira
    d.loc[C, "ks_sira_p10"] = np.percentile(siralar, 10, axis=1)
    d.loc[C, "ks_sira_p90"] = np.percentile(siralar, 90, axis=1)

    # SS
    s = ss.reindex(d.index)[list(SS_W)].fillna(0)
    d["ss_max"] = s.max(axis=1)
    d["ss_max_boyut"] = s.idxmax(axis=1).map(SS_AD).where(d.ss_max > 0, "—")
    d["ss_ort"] = sum(s[c] * w for c, w in SS_W.items())
    d["ss"] = 0.7 * d.ss_max + 0.3 * d.ss_ort
    d["ss_gerekce"] = ss.gerekce.reindex(d.index)

    # AME
    tau_b = d.tau_ab_s4.fillna(0) + 0.25 * (d.tau_ab_s4_tarim_kaybi.fillna(0) - d.tau_ab_s4.fillna(0))
    d["tau_ab_beklenen"] = tau_b
    d["ame_ham"] = d.ab_ihracat_payi * (tau_b + d.q_gb_itu * d.c_roo_s2 + d.q_gb_itu * 1.0) * d.vz_carpani
    d["ame_puan"] = yuzdelik(d.ame_ham.where(C))
    d["ab_risk_musd"] = d.x_ab * (tau_b + d.q_gb_itu * d.c_roo_s2 + d.q_gb_itu) / 100
    d["ede_puan"] = yuzdelik(d.ede_tum_bp.where(C))
    d["cke_puan"] = pd.concat([yuzdelik(d.cke_tufe_musd_bp.where(C)), yuzdelik(d.cke_mali_musd_mlrtl.where(C))],
                              axis=1).mean(axis=1)

    # emek yoğunluğu ve gerileme
    d["calisan_kd"] = d.l / d.kd_musd
    d["emek_puan"] = yuzdelik(d.calisan_kd.where(C)).fillna(0)
    ab_pay_deg = t.ab_pazar_payi_abdisi_2024 / t.ab_pazar_payi_abdisi_2020 - 1
    d["gerileme"] = (dl < -0.10) | ((ab_pay_deg.reindex(d.index) < -0.15) & (d.x_ab >= 50))

    # senaryo sütunları (P50; S4 için P10 de)
    pv = sn.pivot_table(index="kod", columns=["senaryo", "degisken"], values=["p10", "p50", "p90"])
    for sc in ("S2", "S3", "S4"):
        for dg, ad in (("dca", "ca_musd"), ("dtufe", "tufe_bp"), ("dl", "istihdam"), ("dx_ab", "ab_ihracat_musd"),
                       ("dx", "ihracat_musd"), ("dm", "ithalat_musd"), ("dq", "uretim_musd")):
            for pc in ("p10", "p50", "p90"):
                d[f"{sc.lower()}_{ad}_{pc}"] = pv[(pc, sc, dg)].reindex(d.index)
    d["s4_istihdam_pay_p10"] = d.s4_istihdam_p10 / d.l
    d["istihdam_riski"] = np.select([d.s4_istihdam_pay_p10 <= -0.05, d.s4_istihdam_pay_p10 <= -0.02],
                                    ["Yüksek", "Orta"], "Düşük")

    # arketip ve duruş
    ark = {kd: arketipler(r) for kd, r in d[C].iterrows()}
    d.loc[C, "arketip_birincil"] = [ark[kd][0][0] for kd in d.index[C]]
    d.loc[C, "arketip_ikincil"] = [ark[kd][1][0] if len(ark[kd]) > 1 else "" for kd in d.index[C]]
    d["durus"] = d.arketip_birincil.map(DURUS)
    d.loc[(d.arketip_birincil == "A") & (d.ks < 60), "durus"] = "Geliştir"
    d.loc[(d.arketip_birincil == "A") & (d.arketip_ikincil == "G"), "durus"] = "Dönüştür"
    d["tarife_yolu"] = d.arketip_birincil.map(TARIFE)
    d["ana_araclar"] = d.arketip_birincil.map(ARAC)
    d["ab_muzakere"] = d.arketip_birincil.map(MUZAKERE)
    # uzman düzeltmeleri (kartlar/*.yaml: arketip, durus, tarife_yolu, ana_araclar, ab_muzakere; guven aşağıda)
    d["uzman_duzeltmesi"] = ""
    guven_duz = {}
    for yol in sorted(glob.glob(os.path.join(os.path.dirname(__file__), "..", "kartlar", "*.yaml"))):
        for kd, alan in (yaml.safe_load(open(yol, encoding="utf-8")).get("siniflar") or {}).items():
            if kd not in d.index or not alan:
                continue
            degisen = []
            if "arketip" in alan:
                ark_ = list(alan["arketip"]) + [""]
                if (d.at[kd, "arketip_birincil"], d.at[kd, "arketip_ikincil"] or "") != (ark_[0], ark_[1]):
                    degisen.append(f"arketip {d.at[kd, 'arketip_birincil']}→{ark_[0]}")
                d.at[kd, "arketip_birincil"], d.at[kd, "arketip_ikincil"] = ark_[0], ark_[1]
            for c in ("durus", "tarife_yolu", "ana_araclar", "ab_muzakere"):
                if c in alan:
                    if c == "durus" and d.at[kd, c] != alan[c]:
                        degisen.append(f"duruş {d.at[kd, c]}→{alan[c]}")
                    d.at[kd, c] = alan[c]
            if alan.get("guven") in ("Yüksek", "Orta", "Düşük"):
                guven_duz[kd] = alan["guven"]
            d.at[kd, "uzman_duzeltmesi"] = "; ".join(degisen) if degisen else "metin"
    eksik = d.gizli_tahmin.fillna(True).astype(bool).astype(int) + (d.mense_kaynak != "sınıf").astype(int) + \
        (d.ks_bilesen < 7).astype(int)
    d["guven"] = np.select([eksik == 0, eksik == 1], ["Yüksek", "Orta"], "Düşük")
    # güven: kural veri tamlığını ölçer; kart metnindeki değerlendirme (tutarlılık, [D?] olgular) onu düzeltir
    for kd, g in guven_duz.items():
        if d.at[kd, "guven"] != g:
            not_ = f"güven {d.at[kd, 'guven']}→{g}"
            d.at[kd, "uzman_duzeltmesi"] = not_ if d.at[kd, "uzman_duzeltmesi"] in ("", "metin") else \
                f"{d.at[kd, 'uzman_duzeltmesi']}; {not_}"
            d.at[kd, "guven"] = g
    d["mense_riski"] = d.risk_s2 + "/" + d.risk_s3
    d.index.name = "kod"
    d.round(4).to_csv(v("nace_matris.csv"))

    c = d[C]
    print(f"Ana matris: {len(d)} sınıf ({C.sum()} C). KS duyarlılığı:",
          "; ".join(f"{r['agirlik']} ρ={r['spearman']:.2f}" for r in dz))
    print("Birincil arketip dağılımı:", c.arketip_birincil.value_counts().to_dict())
    print("Duruş dağılımı:", c.durus.value_counts().to_dict())


if __name__ == "__main__":
    main()
