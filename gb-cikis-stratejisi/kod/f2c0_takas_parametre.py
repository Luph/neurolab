"""Faz 2 — Vergi takası modelinin (f2c) parametre tablosu: ürün grubu başına pazar bileşimi ve oranlar.

Her ürün grubu için:
  - İthalat ve ihracat: BACI 2024 (HS 2017, HS6; ithalat CIF yerine FOB, küçük fark). Kaynaklar: AB27,
    STA ortakları, diğer
  - Yerli pay (yurt içi üretimin iç satışı) üç yoldan hesaplanır, grubun birincil yöntemi seçilir:
      prodtr  PRODTR 2024 üretimden satış (grubun CPA 6 hane kodları, TL → $ 2024 ortalama kuru) − ihracat.
              Az sayıda büyük üreticili gruplarda (beyaz eşya, TV, klima, kozmetik) en isabetli ölçü.
              Gizli ("c") kod varsa toplam eksik kalır; işaretlenir
      yshi    YSHİ 2024 üretim değeri (NACE sınıfı) − ihracat. Küçük işletmeleri de kapsar; parçalı
              sektörlerde (ayakkabı, mobilya) PRODTR'den daha iyi. Fason işlerde mükerrer sayım riski var
      io      2023 girdi-çıktı tablosu: hanehalkı tüketiminde yurt içi ürünün payı (temel fiyatlarla).
              Giyimde PRODTR ve YSHİ işe yaramaz: PRODTR üretimi ≈ ihracat (kayıt dışı ve fason üretim
              kapsanmıyor), YSHİ ise fason zincirini mükerrer sayıyor
      dis     dış kaynak (veri/vergi_oranlari_2026.csv "yerli_pay_dis"; otomobilde ODMD adet payları)
  - Tarifeler: τ0 (bugün): AB ve STA 0, diğer = 2026 MFN + İGV + EMY (STA dışı ithalat ağırlıklı).
    τ1, iki S4 İGV rejimi (02a §4.1):
      c   AB'nin baskın olduğu satırlarda (AB / (AB + diğer) ≥ %50) AB ve diğerlerine yalnızca MFN; öteki
          satırlarda AB'ye de MFN + İGV + EMY
      c2  c'de İGV yalnızca yurt içi üretimi zayıf satırlarda kalkar (PRODTR üretimi < ithalat; gizli satırlar
          güçlü sayılır; f2b'nin politika_tarife_hs6.csv'si); güçlü satırlarda AB'ye de uygulanır
  - ÖTV ve KDV: veri/vergi_oranlari_2026.csv (grup, otv, kdv, takas türü, kaynak)
  - İstihdam: grubun NACE sınıflarında çalışan / üretim değeri (YSHİ 2024)
  - TÜFE ağırlığı: 2026 TÜFE (COICOP 2018) kalemleri. Beyaz eşya 05.3.1.1 (büyük mutfak aletleri; fırın
    ve ocak dahil) + 05.3.1.2 (çamaşır); küçük ev aletleri 05.3.2; klima 05.3.1.3'ün (ısıtıcı ve klima)
    yarısı [H]; TV 08.1.4; kozmetik 13.1.2'nin %75'i [H] (kalem sabun, diş macunu ve kâğıt ürünlerini de
    içeriyor). Hafif ticari araç hanehalkı sepetinde yok (0)
  - HS 2017 kodu 2026 tarifesinde (HS 2022) bulunamazsa aynı HS4 başlığının ortalama oranı kullanılır
Çıktı: veri/politika_takas_parametre.csv (f2c_vergi_takasi.py girdisi). Senaryolar: rejim (c, c2) × tasarım
(TA_takas, yok, T0_yalniz_yerli, TB_uretim_destegi), ör. S4_c2_TA_takas
"""

import argparse
import os

import numpy as np
import pandas as pd

import f2a_io_fiyat as io
import prodtr
import yollar

STA = {"CHE", "NOR", "ISL", "LIE", "ISR", "MKD", "BIH", "PSE", "TUN", "MAR", "EGY", "ALB", "GEO", "MNE", "SRB",
       "CHL", "MUS", "KOR", "MYS", "MDA", "FRO", "SGP", "GBR", "ARE"}
# grup: HS6 önekleri, hariç tutulan HS6 önekleri, PRODTR CPA önekleri, YSHİ NACE sınıfları, I-O ürünü,
#       birincil yöntem, TÜFE kalemleri (COICOP 2018) ve kalemden gruba düşen pay
GRUPLAR = {
    "binek_otomobil": dict(hs=("8703",), haric=("870310",), cpa=("29.10.2",), nace=("29.10",), io="C29",
                           yontem="dis", tufe=("0711",), tufe_pay=1.0),
    "hafif_ticari": dict(hs=("870421", "870431"), haric=(), cpa=("29.10.4",), nace=("29.10",), io="C29",
                         yontem="dis", tufe=(), tufe_pay=0.0),
    "beyaz_esya": dict(hs=("841810", "841821", "841829", "841830", "841840", "845011", "845012", "845019",
                           "845121", "842211"), haric=(), cpa=("27.51.11", "27.51.12", "27.51.13"),
                       nace=("27.51",), io="C27", yontem="prodtr", tufe=("05311", "05312"), tufe_pay=1.0),
    "kucuk_ev_aletleri": dict(hs=("8509", "8516"), haric=(), cpa=("27.51.2",), nace=("27.51",), io="C27",
                              yontem="prodtr", tufe=("0532",), tufe_pay=1.0),
    "tv": dict(hs=("852872", "852873"), haric=(), cpa=("26.40.20",), nace=("26.40",), io="C26", yontem="prodtr",
               tufe=("0814",), tufe_pay=1.0),
    "klima": dict(hs=("841510", "841581", "841582", "841583"), haric=(), cpa=("28.25.12",), nace=("28.25",),
                  io="C28", yontem="prodtr", tufe=("05313",), tufe_pay=0.5),
    "kozmetik": dict(hs=("3303", "3304", "3305", "3307"), haric=(), cpa=("20.42.1",), nace=("20.42",), io="C20",
                     yontem="prodtr", tufe=("1312",), tufe_pay=0.75),
    "giyim": dict(hs=("61", "62"), haric=(), cpa=("14.10", "14.21", "14.22", "14.23", "14.29"), nace=("14",),
                  io="C13-C15", yontem="io", tufe=("0312",), tufe_pay=1.0),
    "ayakkabi": dict(hs=("6401", "6402", "6403", "6404", "6405"), haric=(), cpa=("15.20.1", "15.20.2", "15.20.3"),
                     nace=("15.20",), io="C13-C15", yontem="yshi", tufe=("0321",), tufe_pay=1.0),
    "mobilya": dict(hs=("9401", "9403"), haric=("940110", "940120"),
                    cpa=("31.00.1", "31.00.20", "31.00.4", "31.00.61", "31.00.62", "31.00.63"),
                    nace=("31.01", "31.02", "31.09"), io="C31_C32", yontem="yshi", tufe=("05111",), tufe_pay=1.0),
}


def io_yerli_paylari(cache):
    """2023 I-O: hanehalkı tüketiminde yurt içi ürün payı, ürün başına."""
    y = io.io_indir(os.path.join(cache, "io2023"))
    yd, kod = io.oku(y["yurtici"])
    ym, _ = io.oku(y["ithalat"])
    hd = yd.iloc[io.SATIR, io.HH].astype(float).to_numpy()
    hm = ym.iloc[io.SATIR, io.HH].astype(float).to_numpy()
    return pd.Series(np.divide(hd, hd + hm, out=np.full_like(hd, np.nan), where=(hd + hm) > 0), index=kod)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baci-tr", default=yollar.girdi("baci", "baci_hs17_tur_bilateral_hs6_2020_2024.csv.gz"))
    ap.add_argument("--cache", default=yollar.GIRDI)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    v = lambda f: os.path.join(a.out, f)  # noqa: E731

    b = pd.read_csv(a.baci_tr, dtype={"hs6": str})
    b = b[b.year == 2024].copy()
    b["hs6"] = b.hs6.str.zfill(6)
    b["grp"] = np.where(b.eu27 == 1, "ab", np.where(b.partner_iso3.isin(STA), "sta", "diger"))
    tr = pd.read_csv(v("tarife_tr_2026_gtip12.csv"), dtype={"gtip12": str, "hs6": str})
    tr = tr[~tr.in_tgtc_only]
    mfn = tr.groupby("hs6").mfn_rate.mean() / 100
    tam = tr.groupby("hs6").mfn_igv_emy.mean() / 100
    mfn4 = tr.groupby(tr.hs6.str[:4]).mfn_rate.mean() / 100
    tam4 = tr.groupby(tr.hs6.str[:4]).mfn_igv_emy.mean() / 100
    tufe = pd.read_csv(v("tuik_tufe_agirlik_2026.csv"), dtype={"coicop_2018": str}).set_index("coicop_2018")
    h = pd.read_csv(v("politika_tarife_hs6.csv"), dtype={"hs6": str}).set_index("hs6")
    guclu_hs6 = h.gizli.astype(bool) | (h.uretim_ithalat_orani >= 1.0)
    y = pd.read_csv(v("tuik_yshi_nace2.csv"), dtype={"kod": str})
    y = y[y.yil == 2024].set_index("kod")
    usd_try = pd.read_csv(v("teshis_odemeler_dengesi.csv"), index_col=0).loc[2024, "usd_try"]
    pr = prodtr.cpa6(os.path.join(a.cache, "prodtr"), yil="2024")
    pr["uretim_musd"] = pr.satis_tl / usd_try / 1e6
    io_pay = io_yerli_paylari(a.cache)
    vo = pd.read_csv(v("vergi_oranlari_2026.csv"))

    satirlar = []
    for grup, g in GRUPLAR.items():
        x = b[b.hs6.str.startswith(g["hs"]) & ~b.hs6.str.startswith(g["haric"] or ("@",))]
        M = x[x.flow == "M"].pivot_table(index="hs6", columns="grp", values="value_kusd", aggfunc="sum").fillna(0) / 1e3
        for c in ("ab", "sta", "diger"):
            if c not in M:
                M[c] = 0.0
        X = x[x.flow == "X"].value_kusd.sum() / 1e3
        M["mfn"], M["tam"] = M.index.map(mfn), M.index.map(tam)
        eslesmeyen = float(M.loc[M.mfn.isna(), ["ab", "sta", "diger"]].sum().sum())
        M["mfn"] = M.mfn.fillna(pd.Series(M.index.str[:4].map(mfn4), index=M.index)).fillna(0)
        M["tam"] = M.tam.fillna(pd.Series(M.index.str[:4].map(tam4), index=M.index)).fillna(0)
        baskin = M.ab / (M.ab + M.diger).replace(0, np.nan) >= 0.5
        guclu = pd.Series(M.index.map(guclu_hs6), index=M.index).fillna(False).astype(bool)
        tau0_diger = (M.diger * M.tam).sum() / M.diger.sum() if M.diger.sum() else 0.0
        tau1 = {}
        for rejim, kaldir in (("c", baskin), ("c2", baskin & ~guclu)):
            oran = np.where(kaldir, M.mfn, M.tam)
            tau1[rejim] = ((M.ab * oran).sum() / M.ab.sum() if M.ab.sum() else 0.0,
                           (M.diger * oran).sum() / M.diger.sum() if M.diger.sum() else 0.0)
        r = vo[vo.grup == grup].iloc[0]

        # yerli pay: üç yöntem (iç satış, $ mn) ve dış kaynak
        p = pr[pr.cpa22.str.startswith(g["cpa"])]
        uretim_prodtr, gizli_kod = p.uretim_musd.sum(), int(p.gizli.fillna(False).sum())
        uretim_yshi = sum(y.loc[n, "uretim_degeri_musd"] for n in g["nace"])
        calisan = sum(y.loc[n, "calisan"] for n in g["nace"])
        ithal = {"ab": M.ab.sum(), "sta": M.sta.sum(), "diger": M.diger.sum()}
        tau0 = {"yerli": 0.0, "ab": 0.0, "sta": 0.0, "diger": tau0_diger}
        harcama = {o: ithal[o] * (1 + tau0[o]) for o in ithal}
        ithal_harcama = sum(harcama.values())
        s_io = float(io_pay[g["io"]])
        yerli = {"prodtr": max(uretim_prodtr - X, 0.0), "yshi": max(uretim_yshi - X, 0.0),
                 "io": s_io / (1 - s_io) * ithal_harcama}
        s_dis = r.get("yerli_pay_dis", np.nan)
        if not pd.isna(s_dis):
            yerli["dis"] = s_dis / (1 - s_dis) * ithal_harcama
        yontem = g["yontem"] if g["yontem"] in yerli else "io"
        harcama["yerli"] = yerli[yontem]
        toplam = sum(harcama.values())
        for rejim, (tau1_ab, tau1_diger) in tau1.items():
            satirlar.append(dict(
                grup=grup, rejim=rejim, senaryo=f"S4_{rejim}_TA_takas", pazar_musd=toplam * (1 + r.otv) * (1 + r.kdv),
                **{f"pay_{o}": harcama[o] / toplam for o in ("yerli", "ab", "sta", "diger")},
                tau0_yerli=0.0, tau0_ab=0.0, tau0_sta=0.0, tau0_diger=tau0_diger,
                tau1_yerli=0.0, tau1_ab=tau1_ab, tau1_sta=0.0, tau1_diger=tau1_diger,
                otv0=r.otv, kdv=r.kdv, takas=r.takas, calisan_per_musd=calisan / uretim_yshi,
                tufe_agirlik_yuzde=g["tufe_pay"] * sum(tufe.loc[c, "agirlik_yuzde"] for c in g["tufe"]),
                yerli_yontem=yontem, **{f"yerli_pay_{k}": yerli[k] / (yerli[k] + ithal_harcama) for k in yerli},
                uretim_prodtr_musd=uretim_prodtr, prodtr_gizli_kod=gizli_kod, uretim_yshi_musd=uretim_yshi,
                ihracat_musd=X, ithalat_ab_musd=ithal["ab"], ithalat_sta_musd=ithal["sta"],
                ithalat_diger_musd=ithal["diger"], hs4_ortalamasi_kullanilan_ithalat_musd=eslesmeyen,
                ab_baskin_ithalat_payi=float(M.ab[baskin].sum() / M.ab.sum()) if M.ab.sum() else 0.0,
                kaynak=r.kaynak))
    t = pd.DataFrame(satirlar)
    # karşılaştırma tasarımları: pasif (yok), T-0 (yalnızca yerli ürüne indirim), T-B (III:8(b) yerli desteği)
    turevler = [t.assign(senaryo="S4_" + t.rejim + "_yok", takas="yok"),
                t.assign(senaryo="S4_" + t.rejim + "_T0_yalniz_yerli", takas=t.takas + "_yerli"),
                t.assign(senaryo="S4_" + t.rejim + "_TB_uretim_destegi", takas="destek_yerli")]
    pd.concat([t] + turevler).round(5).to_csv(v("politika_takas_parametre.csv"), index=False)
    pd.set_option("display.width", 250)
    sut = ["grup", "pazar_musd", "pay_yerli", "pay_ab", "pay_sta", "pay_diger", "tau0_diger", "tau1_ab", "tau1_diger",
           "otv0", "kdv", "yerli_yontem", "yerli_pay_prodtr", "yerli_pay_yshi", "yerli_pay_io", "prodtr_gizli_kod",
           "ihracat_musd", "hs4_ortalamasi_kullanilan_ithalat_musd", "tufe_agirlik_yuzde"]
    print(t[["rejim"] + [c for c in sut if c in t]].round(3).to_string(index=False))


if __name__ == "__main__":
    main()
