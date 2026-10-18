"""Faz 3 — Ürün karmaşıklığı (PCI), ürün uzayı yakınlığı ve Türkiye için yoğunluk / karmaşıklık kazancı (kart alan 6).

Kaynak: CEPII BACI HS17 (V202601), 2024, ihracatçı × HS6 (girdi/baci/baci_hs17_world_exports_exporter_hs6_2024.csv.gz).
Yöntem (Hidalgo ve Hausmann 2009; Hausmann ve diğ. 2014, "The Atlas of Economic Complexity"):
  RCA_cp = (X_cp / X_c) / (X_p / X)            M_cp = 1[RCA_cp ≥ 1]
  M̃_pp' = Σ_c M_cp M_cp' / (k_c k_p)          PCI = M̃'nin ikinci özvektörü (standartlaştırılmış)
  ECI_c  = Σ_p M_cp PCI_p / k_c (standartlaştırılmış; sınama için)
  φ_pp'  = Σ_c M_cp M_cp' / max(k_p, k_p')    (yakınlık)
  yoğunluk_p = Σ_p' φ_pp' M_TR,p' / Σ_p' φ_pp'
  COG_p  = Σ_p' (φ_pp' / Σ_p'' φ_p''p') (1 − M_TR,p') PCI_p'   (karmaşıklık kazancı)
Süzgeç: toplam ihracatı ≥ 1 mlr $ olan ülkeler; dünya ihracatı ≥ 50 mn $ ve en az bir ülkede RCA ≥ 1 olan ürünler.
Özvektör, simetrik biçim S = D_p^(−½) M' D_c^(−1) M D_p^(−½) üzerinden hesaplanır (M̃ ile aynı özdeğerler).
İşaret: PCI ile ürün yaygınlığı (k_p) arasındaki ilişki negatif olacak şekilde seçilir.
Sınıf düzeyi: HS6 → NACE ağırlıkları (f3a_ticaret.hs6_nace_agirlik); dünya ihracatı ve Türkiye ihracatı ağırlıklı PCI.
"Atlanabilir ürün": sınıf içinde TR RCA < 1, yoğunluk sınıf içi üst çeyrekte ve PCI sınıfın TR ağırlıklı PCI'sından yüksek.

Çıktı: veri/f3_pci_hs6.csv, veri/f3_pci_sinif.csv, veri/f3_eci_ulke.csv
"""

import argparse
import os

import numpy as np
import pandas as pd

import f3a_ticaret as f3a
import yollar


def karmasiklik(x, min_ulke=1e6, min_urun=5e4):
    """x: ülke × HS6 ihracat (bin $). Döndürür: (pci, eci, M, phi, urunler, ulkeler)."""
    x = x.loc[x.sum(axis=1) >= min_ulke]
    x = x.loc[:, x.sum(axis=0) >= min_urun]
    rca = (x.div(x.sum(axis=1), axis=0)).div(x.sum(axis=0) / x.values.sum(), axis=1)
    M = (rca >= 1).astype(float)
    M = M.loc[M.sum(axis=1) > 0, M.sum(axis=0) > 0]
    kc, kp = M.sum(axis=1).values, M.sum(axis=0).values
    Mv = M.values
    S = (Mv / np.sqrt(kp)).T @ (Mv / kc[:, None]) / np.sqrt(kp)
    w, v = np.linalg.eigh(S)
    pci = v[:, -2] / np.sqrt(kp)
    pci = (pci - pci.mean()) / pci.std()
    if np.corrcoef(pci, kp)[0, 1] > 0:
        pci = -pci
    eci = (Mv @ pci) / kc
    eci = (eci - eci.mean()) / eci.std()
    ortak = Mv.T @ Mv
    phi = ortak / np.maximum.outer(kp, kp)
    np.fill_diagonal(phi, 0.0)
    return (pd.Series(pci, index=M.columns), pd.Series(eci, index=M.index), M, phi,
            pd.Series(kp, index=M.columns), rca)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baci", default=yollar.girdi("baci", "baci_hs17_world_exports_exporter_hs6_2024.csv.gz"))
    ap.add_argument("--ulkeler", default=yollar.girdi("baci", "country_codes_V202601.csv"))
    ap.add_argument("--out", default=yollar.VERI)
    a = ap.parse_args()
    v = lambda f: os.path.join(a.out, f)  # noqa: E731

    b = pd.read_csv(a.baci, dtype={"hs6": str})
    b["hs6"] = b.hs6.str.zfill(6)
    x = b.pivot_table(index="exporter_iso3", columns="hs6", values="value_kusd", aggfunc="sum", fill_value=0.0)
    pci, eci, M, phi, kp, rca = karmasiklik(x)

    tr = M.loc["TUR"].values
    yogunluk = (phi @ tr) / phi.sum(axis=1)
    cog = phi @ ((1 - tr) * pci.values / phi.sum(axis=0))
    h = pd.DataFrame({"pci": pci, "yayginlik": kp, "tr_rca": rca.loc["TUR", pci.index], "tr_m": tr.astype(int),
                      "yogunluk": yogunluk, "cog": cog,
                      "dunya_ihracat_musd": x[pci.index].sum(axis=0) / 1e3,
                      "tr_ihracat_musd": x.loc["TUR", pci.index] / 1e3})
    h.index.name = "hs6"

    adlar = pd.read_csv(a.ulkeler, dtype=str)
    e = pd.DataFrame({"eci": eci})
    e["ulke"] = e.index.map(adlar.drop_duplicates("country_iso3").set_index("country_iso3").country_name)
    e["cesitlilik"] = M.sum(axis=1)
    e = e.sort_values("eci", ascending=False)
    e["sira"] = range(1, len(e) + 1)
    e.round(4).to_csv(v("f3_eci_ulke.csv"))

    # sınıf düzeyi
    ag = f3a.hs6_nace_agirlik(v("cn2025_nace_rejim.csv"))
    h6 = h.reset_index()
    d6 = h6.merge(ag["hs6"], on="hs6", how="inner")
    k = h6[~h6.hs6.isin(ag["hs6"].hs6)].assign(hs4=lambda t: t.hs6.str[:4])
    d = pd.concat([d6, k.merge(ag["hs4"], on="hs4", how="inner").drop(columns="hs4")], ignore_index=True)
    d["w_dunya"] = d.dunya_ihracat_musd * d.pay
    d["w_tr"] = d.tr_ihracat_musd * d.pay
    satirlar = []
    for kod, g in d.groupby("nace2"):
        r = dict(kod=kod, urun_sayisi=len(g),
                 pci_dunya=np.average(g.pci, weights=g.w_dunya) if g.w_dunya.sum() > 0 else np.nan,
                 pci_tr=np.average(g.pci, weights=g.w_tr) if g.w_tr.sum() > 0 else np.nan,
                 tr_rca_urun_payi=(g.tr_m * g.w_dunya).sum() / g.w_dunya.sum() if g.w_dunya.sum() > 0 else np.nan,
                 yogunluk_ort=np.average(g.yogunluk, weights=g.w_dunya) if g.w_dunya.sum() > 0 else np.nan,
                 cog_ort=np.average(g.cog, weights=g.w_dunya) if g.w_dunya.sum() > 0 else np.nan)
        esik = g.yogunluk.quantile(0.75)
        ref = r["pci_tr"] if pd.notna(r["pci_tr"]) else r["pci_dunya"]
        aday = g[(g.tr_rca < 1) & (g.yogunluk >= esik) & (g.pci > ref) & (g.dunya_ihracat_musd >= 100)]
        aday = aday.sort_values(["cog", "pci"], ascending=False).head(3)
        r["atlanabilir_urunler"] = "; ".join(f"{s.hs6} (PCI {s.pci:+.2f}, RCA {s.tr_rca:.2f})" for s in aday.itertuples())
        satirlar.append(r)
    s = pd.DataFrame(satirlar).set_index("kod")
    s.round(4).to_csv(v("f3_pci_sinif.csv"))
    h.round(5).to_csv(v("f3_pci_hs6.csv"))

    tur = e.loc["TUR"]
    print(f"PCI: {len(pci)} ürün, {len(eci)} ülke; Türkiye ECI {tur.eci:+.2f} (sıra {int(tur.sira)}/{len(e)}), "
          f"RCA≥1 ürün {int(tur.cesitlilik)}")
    print("ECI ilk 8:", ", ".join(e.ulke.head(8)))
    c = s[s.index.str.match(r"^(1\d|2\d|3[0-3])\.")]
    print("En karmaşık 5 C sınıfı (dünya ağırlıklı):", ", ".join(f"{k} {p:+.2f}" for k, p in c.pci_dunya.nlargest(5).items()))
    print("En basit 5 C sınıfı:", ", ".join(f"{k} {p:+.2f}" for k, p in c.pci_dunya.nsmallest(5).items()))


if __name__ == "__main__":
    main()
