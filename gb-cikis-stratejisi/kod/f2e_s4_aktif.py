"""Faz 2 — "Aktif S4": anlaşmasız çıkışta Türkiye'nin kendi araçlarıyla enflasyon ve mali bilanço.

Paket bileşenleri (her biri ayrı raporlanır):
  P1  Girdide sıfır: yurt içinde üretimi olmayan/zayıf sanayi girdilerinde MFN ve İGV = 0 (f2b)
  P2  İGV AB menşeli mallara yayılmaz: AB mallarına yalnızca MFN (İGV Kararı değişikliği; MFN ilkesi
      gereği İGV'nin STA dışı bütün ülkeler için yeniden tasarlanması gerekir, bkz. 02a §3)
  P3  Vergi takası: tüketici fiyatı, menşeden bağımsız ÖTV/KDV indirimiyle nötrlenen ürünler
      (I-O ürünleri; varsayılan: C29 otomobil [ÖTV II], C26 ve C27 elektronik ve beyaz eşya [ÖTV IV],
      C13-C15 giyim ve tekstil [KDV], C20 kozmetik ve temizlik [ÖTV IV/KDV])
Yöntem: f2a'daki Leontief fiyat modeli. P3 ürünlerinde hanehalkının ödediği fiyat değişimi vergi
indirimiyle sıfırlanır; bu ürünlerin girdi olarak kullanımından doğan maliyet etkisi diğer ürünlere
geçmeye devam eder. Takasın mali maliyeti = nötrlenen fiyat artışı × alıcı fiyatlarıyla hanehalkı
tüketimi (2023, GSYH'ye oranla, 2025 GSYH'ye uygulanır). Gümrük geliri: f2b (2024 ithalatı × 2026 oranları;
yasal tutar; DİR, teşvik ve GSP muafiyetleri nedeniyle gerçek tahsilat daha düşük).
Çıktı: veri/politika_s4_aktif.csv
"""

import argparse
import os

import numpy as np
import pandas as pd

import f2a_io_fiyat as io

TAKAS_URUNLERI = {"C29": "ÖTV (II)", "C26": "ÖTV (IV)", "C27": "ÖTV (IV)", "C13-C15": "KDV", "C20": "ÖTV (IV)/KDV"}


def vektor(t, kod, deger):
    g = t.groupby("io").m_toplam_musd.sum()
    d = deger.groupby(t.io).sum()
    return (d / g).reindex(kod).fillna(0.0).to_numpy()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=os.path.expanduser("~/.cache/gb_cikis"))
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    v = lambda f: os.path.join(a.out, f)  # noqa: E731

    yollar = io.io_indir(os.path.join(a.cache, "io2023"))
    yd, kod = io.oku(yollar["yurtici"])
    it, _ = io.oku(yollar["ithalat"])
    ka, _ = io.oku(yollar["kullanim_alici"])
    Z_d = yd.iloc[io.SATIR, io.SUTUN].astype(float).to_numpy()
    Z_m = it.iloc[io.SATIR, io.SUTUN].astype(float).to_numpy()
    x = yd.iloc[io.P1, io.SUTUN].astype(float).to_numpy()
    h_d = yd.iloc[io.SATIR, io.HH].astype(float).to_numpy()
    h_m = it.iloc[io.SATIR, io.HH].astype(float).to_numpy()
    h_alici = np.clip(ka.iloc[io.SATIR, io.HH].astype(float).to_numpy(), 0, None)
    w = np.where(np.array(kod) == "L68A", 0.0, h_alici)
    w = w / w.sum()
    A_d = np.divide(Z_d, x, out=np.zeros_like(Z_d), where=x > 0)
    A_m = np.divide(Z_m, x, out=np.zeros_like(Z_m), where=x > 0)
    od = pd.read_csv(v("teshis_odemeler_dengesi.csv"), index_col=0)
    gsyh_2023_bintl, gsyh_2025_musd = float(od.loc[2023, "gsyh"]), float(od.loc[2025, "gsyh_musd"])  # bin TL; mn $

    t = pd.read_csv(v("politika_tarife_hs6.csv"), dtype={"hs6": str})
    t = t[t.io.notna()]
    gb = t.rejim.isin(["GB", "ITU"])
    p1 = t.p1.astype(bool)
    vek = {
        "S4_pasif_mfn_igv": vektor(t, kod, (t.m_ab_musd * t.t_tam / 100).where(gb, 0.0)),
        "S4_P2_mfn": vektor(t, kod, (t.m_ab_musd * t.t_mfn / 100).where(gb, 0.0)),
        "S4_P1_P2": vektor(t, kod, (t.m_ab_musd * t.t_mfn / 100).where(gb & ~p1, 0.0))
                    - vektor(t, kod, t.gelir_mevcut_musd.where(p1, 0.0)),
    }
    takas = np.isin(np.array(kod), list(TAKAS_URUNLERI))
    gelir = {"S4_pasif_mfn_igv": t.s4_gelir_tam_musd.sum(), "S4_P2_mfn": t.s4_gelir_mfn_musd.sum(),
             "S4_P1_P2": t.s4_gelir_mfn_musd.where(~p1, 0).sum() - t.gelir_mevcut_musd.where(p1, 0).sum()}
    satirlar, urun = [], {}
    for ad, dtau in vek.items():
        for rho in io.RHO:
            dP, toplam, dp_d = io.model(A_d, A_m, h_d, h_m, w, dtau, rho, 0.0)
            satirlar.append(dict(paket=ad, rho=rho, tufe_bp=toplam * 1e4, gumruk_geliri_musd=gelir[ad],
                                 takas_mali_maliyet_musd=0.0))
            if ad == "S4_P1_P2":
                # P3: takas ürünlerinde hanehalkı fiyatı vergi indirimiyle sıfırlanır
                kalan = float(w @ np.where(takas, 0.0, dP))
                maliyet_gsyh = float((np.where(takas, dP, 0.0) * h_alici).sum() / gsyh_2023_bintl)
                satirlar.append(dict(paket="S4_P1_P2_P3", rho=rho, tufe_bp=kalan * 1e4,
                                     gumruk_geliri_musd=gelir[ad],
                                     takas_mali_maliyet_musd=maliyet_gsyh * gsyh_2025_musd))
                if rho == 0.8:
                    urun["tuketici_fiyat_yuzde"] = dP * 100
                    urun["tufe_katki_bp"] = w * dP * 1e4
                    urun["takas"] = [TAKAS_URUNLERI.get(k, "") for k in kod]
                    urun["takas_maliyeti_musd"] = np.where(takas, dP, 0.0) * h_alici / gsyh_2023_bintl * gsyh_2025_musd
    oz = pd.DataFrame(satirlar)
    oz["net_mali_musd"] = oz.gumruk_geliri_musd - oz.takas_mali_maliyet_musd
    oz["net_mali_gsyh_yuzde"] = 100 * oz.net_mali_musd / gsyh_2025_musd
    oz.round(3).to_csv(v("politika_s4_aktif.csv"), index=False)
    u = pd.DataFrame(urun, index=kod)
    u.insert(0, "ad", yd.iloc[io.SATIR, 2].astype(str).str.split("\n").str[0].str.strip().tolist())
    u.round(4).to_csv(v("politika_s4_aktif_urun.csv"))
    pd.set_option("display.width", 220)
    print(oz.round(2).to_string(index=False))
    print(u[u.takas != ""].round(3).to_string())
    print(u.sort_values("tufe_katki_bp", ascending=False).head(12).round(3).to_string())


if __name__ == "__main__":
    main()
