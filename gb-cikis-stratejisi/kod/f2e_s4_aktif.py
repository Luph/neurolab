"""Faz 2 — "Aktif S4": anlaşmasız çıkışta Türkiye'nin kendi araçlarıyla enflasyon ve mali bilanço.

Paket bileşenleri (her biri ayrı raporlanır):
  P1  Girdide sıfır: yurt içinde üretimi olmayan/zayıf sanayi girdilerinde MFN ve İGV = 0 (f2b)
  P2  İGV AB menşeli mallara yayılmaz: AB mallarına yalnızca MFN. MFN ilkesi gereği bu, STA olmadan ancak
      İGV'nin STA dışı herkes için yeniden tasarlanmasıyla mümkündür. Üç varyant:
        P2   yalnızca AB'nin İGV'den muaf tutulduğu varsayımı (geçici anlaşma, XXIV:5) — üst sınır
        P2b  İGV herkes için kaldırılır (dezenflasyonist; gelir ve koruma kaybı)
        P2c  seçici: AB'nin STA dışı ithalattaki payı ≥ %50 olan satırlarda İGV herkes için kaldırılır,
             diğer satırlarda AB'ye de uygulanır
        P2c2 kabiliyete duyarlı seçici: P2c'de İGV yalnızca yurt içi üretimi zayıf satırlarda (PRODTR
             üretimi < ithalat; gizli satırlar güçlü sayılır) kaldırılır; güçlü satırlarda AB'ye de uygulanır
  P3  Vergi takası: tüketici fiyatı, menşeden bağımsız ÖTV/KDV indirimiyle nötrlenen ürünler. İki kapsam:
        dar   I-O ürünleri C29 otomobil [ÖTV II], C26 ve C27 elektronik ve beyaz eşya [ÖTV IV], C13-C15 giyim
              ve tekstil [KDV], C20 kozmetik ve temizlik [ÖTV IV/KDV]
        genis bütün imalat ürünleri (C10–C33; KDV veya ÖTV ile). Tarım, enerji ve hizmetlere geçen maliyet
              etkisi nötrlenmez
Yöntem: f2a'daki Leontief fiyat modeli. P3 ürünlerinde hanehalkının ödediği fiyat değişimi vergi
indirimiyle sıfırlanır; bu ürünlerin girdi olarak kullanımından doğan maliyet etkisi diğer ürünlere
geçmeye devam eder. Takasın mali maliyeti = nötrlenen fiyat artışı × alıcı fiyatlarıyla hanehalkı
tüketimi (2023, GSYH'ye oranla, 2025 GSYH'ye uygulanır). Gümrük geliri: f2b (2024 ithalatı × 2026 oranları;
yasal tutar). Tahsil edilebilir gelir: DİR, teşvik belgesi ve GSP muafiyetleri nedeniyle yasal tutarın bir
kısmı tahsil edilmez. 2025 gerçekleşmesi (321,8 mlr TL = $8,15 mlr; GİB Tablo 28) yasal tutarın %50'si.
Sanayi tüketim ve karma kullanım mallarında (otomobil dahil) muafiyet yok sayılır (%100); ara ve sermaye
mallarında ve tarımda oran, toplam 2025 gerçekleşmesini tutturacak biçimde hesaplanır (≈%38).
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
    # tahsilat oranı: sanayi tüketim/karma malları %100, diğerleri 2025 gerçekleşmesinden
    vg = pd.read_csv(v("vergi_gelirleri_2024_2026.csv")).set_index("kalem")
    gercek = vg.loc["gumruk_vergileri", "y2025_mlr_tl"] * 1e3 / float(od.loc[2025, "usd_try"])   # mn $
    tam_tahsil = (t.hs6.str[:2].astype(int) > 24) & t.kullanim.isin(["tuketim", "karma"])
    oran_diger = (gercek - t.gelir_mevcut_musd[tam_tahsil].sum()) / t.gelir_mevcut_musd[~tam_tahsil].sum()
    t["tahsilat"] = np.where(tam_tahsil, 1.0, oran_diger)
    t = t[t.io.notna()]
    gb = t.rejim.isin(["GB", "ITU"])
    p1 = t.p1.astype(bool)
    igv_diger = t.m_diger_musd * (t.t_tam - t.t_mfn) / 100            # STA dışı ithalattan İGV geliri (yasal)
    ab_baskin = (t.m_ab_musd / (t.m_ab_musd + t.m_diger_musd).replace(0, np.nan)).fillna(0) >= 0.5
    guclu = t.gizli.astype(bool) | (t.uretim_ithalat_orani >= 1.0)
    kaldir_c2 = ab_baskin & ~guclu
    # AB mallarına uygulanacak oran ve STA dışı İGV değişimi: rejim × P1
    rejimler = {
        "a_igv_ab_dahil": (t.t_tam, 0.0 * igv_diger),                                     # İGV herkese, AB dahil
        "b_igv_kaldirilir": (t.t_mfn, -igv_diger),                                        # İGV herkes için kalkar
        "c_igv_secici": (np.where(ab_baskin, t.t_mfn, t.t_tam), -igv_diger.where(ab_baskin, 0.0)),
        "c2_igv_secici_kabiliyet": (np.where(kaldir_c2, t.t_mfn, t.t_tam), -igv_diger.where(kaldir_c2, 0.0)),
        "d_gecici_anlasma": (0.0 * t.t_mfn, 0.0 * igv_diger),                             # XXIV:5; S4 değil
    }
    kodlar = np.array(kod)
    imalat = np.array([k.startswith("C") for k in kod])
    kapsamlar = {"yok": np.zeros(len(kod), bool), "dar": np.isin(kodlar, list(TAKAS_URUNLERI)), "genis": imalat}
    adlar = yd.iloc[io.SATIR, 2].astype(str).str.split("\n").str[0].str.strip().tolist()
    satirlar, urun = [], []
    for rejim, (oran_ab, d_igv) in rejimler.items():
        for P1 in (False, True):
            maske = gb & ~p1 if P1 else gb
            ab_vergi = (t.m_ab_musd * pd.Series(oran_ab, index=t.index) / 100).where(maske, 0.0)
            p1_kayip = t.gelir_mevcut_musd.where(p1, 0.0) if P1 else 0.0 * t.gelir_mevcut_musd
            d_igv_p = pd.Series(d_igv, index=t.index).where(~p1, 0.0) if P1 else pd.Series(d_igv, index=t.index)
            dtau = vektor(t, kod, ab_vergi) + vektor(t, kod, d_igv_p) - vektor(t, kod, p1_kayip)
            gelir = ab_vergi.sum() + d_igv_p.sum() - p1_kayip.sum()
            gelir_tahsil = ((ab_vergi + d_igv_p - p1_kayip) * t.tahsilat).sum()
            # koruma göstergesi: güçlü yerli üretimli satırlarda kaldırılan İGV (STA dışı ithalattan, yasal)
            koruma_kaybi = -d_igv_p.where(guclu, 0.0).sum()
            # AB'nin Türkiye'ye ihracat kaybı (kısmi denge, σ = 5): ΔM = M_AB × ((1 + t)^−σ − 1)
            oran_s = pd.Series(oran_ab, index=t.index).where(maske, 0.0) / 100
            ab_kayip = (t.m_ab_musd * ((1 + oran_s) ** -5.0 - 1)).sum()
            for rho in io.RHO:
                dP, toplam, dp_d = io.model(A_d, A_m, h_d, h_m, w, dtau, rho, 0.0)
                for P3, takas in kapsamlar.items():
                    artis = np.where(takas, np.clip(dP, 0, None), 0.0)
                    kalan = float(w @ (dP - artis))
                    maliyet = float((artis * h_alici).sum() / gsyh_2023_bintl) * gsyh_2025_musd
                    satirlar.append(dict(rejim=rejim, P1=P1, P3=P3, rho=rho, tufe_bp=kalan * 1e4,
                                         gumruk_geliri_degisimi_musd=gelir, tahsil_edilebilir_gumruk_musd=gelir_tahsil,
                                         takas_mali_maliyet_musd=maliyet,
                                         ab_mallarina_vergi_musd=ab_vergi.sum(), ab_disi_igv_degisimi_musd=d_igv_p.sum(),
                                         guclu_satirda_kaldirilan_igv_musd=koruma_kaybi,
                                         ab_ihracat_kaybi_s5_musd=ab_kayip))
                if P1 and rho == 0.8:
                    urun.append(pd.DataFrame(dict(
                        rejim=rejim, io=kod, ad=adlar, tuketici_fiyat_yuzde=dP * 100, tufe_katki_bp=w * dP * 1e4,
                        takas_dar=[TAKAS_URUNLERI.get(k, "") for k in kod], imalat=imalat,
                        takas_maliyeti_dar_musd=np.where(kapsamlar["dar"], np.clip(dP, 0, None), 0.0) * h_alici
                        / gsyh_2023_bintl * gsyh_2025_musd,
                        takas_maliyeti_genis_musd=np.where(imalat, np.clip(dP, 0, None), 0.0) * h_alici
                        / gsyh_2023_bintl * gsyh_2025_musd)))
    oz = pd.DataFrame(satirlar)
    oz["net_mali_musd"] = oz.gumruk_geliri_degisimi_musd - oz.takas_mali_maliyet_musd
    oz["net_mali_gsyh_yuzde"] = 100 * oz.net_mali_musd / gsyh_2025_musd
    oz["net_mali_tahsil_musd"] = oz.tahsil_edilebilir_gumruk_musd - oz.takas_mali_maliyet_musd
    oz["net_mali_tahsil_gsyh_yuzde"] = 100 * oz.net_mali_tahsil_musd / gsyh_2025_musd
    oz.round(3).to_csv(v("politika_s4_aktif.csv"), index=False)
    u = pd.concat(urun)
    u.round(4).to_csv(v("politika_s4_aktif_urun.csv"), index=False)
    pd.set_option("display.width", 220)
    print(f"tahsilat oranı (ara/sermaye/tarım): {oran_diger:.3f}")
    print(oz[oz.rho == 0.8].drop(columns=["ab_mallarina_vergi_musd", "ab_disi_igv_degisimi_musd"]).round(2).to_string(index=False))
    print(oz.pivot_table(index=["rejim", "P1", "P3"], columns="rho", values="tufe_bp").round(1).to_string())
    for r in ("c_igv_secici", "c2_igv_secici_kabiliyet"):
        x = u[u.rejim == r].sort_values("tufe_katki_bp", ascending=False)
        print(r)
        print(x.head(12)[["io", "tuketici_fiyat_yuzde", "tufe_katki_bp", "takas_dar", "imalat"]].round(3).to_string(index=False))


if __name__ == "__main__":
    main()
