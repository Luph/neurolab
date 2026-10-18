"""Faz 2 — Girdi-çıktı fiyat modeli: tarife değişikliklerinin TÜFE'ye birinci tur etkisi ve EDE.

Kaynak: TÜİK 2023 girdi-çıktı tabloları (CPA Rev. 2.1, 64 ürün, bin TL), Veri Portalı'ndan:
  - Yurtiçi Üretim Girdi-Çıktı Tablosu, temel fiyatlarla       → Z_d, x (P.1), h_d (hanehalkı)
  - İthalat Girdi-Çıktı Tablosu, cif, temel fiyatlarla          → Z_m, h_m
  - Kullanım Tablosu, alıcı fiyatlarıyla                        → w (hanehalkı tüketim ağırlıkları)
Model (ana prompt, Bölüm 1.1 "Enflasyon etkisi"):
  Δp_d   = (I − A_d')⁻¹ A_m' (ρ Δτ_m)                       yurt içi üretim fiyatları (maliyet itişi)
  ΔP_c   = [h_d,c (Δp_d,c + κ ρ Δτ_m,c) + h_m,c ρ Δτ_m,c] / (h_d,c + h_m,c)
  ΔTÜFE  = Σ_c w_c ΔP_c                                      w: alıcı fiyatlarıyla hanehalkı payı, L68A hariç
  κ: yurt içi rakiplerin ithal fiyat artışına uyma payı ("tarife şemsiyesi"); ana promptun formülünde
  κ = 0, duyarlılıkta κ = 0,5.
Tarife şoku: AB menşeli ithalata uygulanacak oran t_c × ürünün ithalatında AB payı s_c:
  Δτ_m,c = s_c × t_c. s_c ve t_c BACI 2024 (HS6, Türkiye ithalatı) ve 2026 Türk tarifesiyle (GTİP12 → HS6
  ortalaması), AB ithalatı ağırlıklı. Varyant (i): GB + İTÜ satırları; (ii): + tarım (1/98). AKÇT satırları
  iki varyantta da hariç (1996 AKÇT Anlaşması sürer).
Varsayımlar: ad valorem ÖTV ve KDV oransal olduğundan temel fiyattaki % değişim alıcı fiyatına aynen
geçer (ticaret marjları oransal); hacim ve kaynak değişimi yok (statik, birinci tur üst sınır).

Çıktılar:
  veri/politika_io_ede.csv      ürün başına ağırlık, ithal payı, AB payı, tarifeler, EDE ve S4 TÜFE katkısı
  veri/politika_io_s4_tufe.csv  S4 birinci tur TÜFE etkisi (bp): varyant × tarife ölçüsü × ρ × κ
"""

import argparse
import glob
import os

import numpy as np
import pandas as pd

import tuik

IO_TABLOLAR = {"yurtici": "Yurtiçi Üretim Girdi-Çıktı Tablosu 2023",
               "ithalat": "İthalat Girdi-Çıktı Tablosu 2023",
               "kullanim_alici": "Kullanım Tablosu 2023 Alıcı Fiyatlarıyla"}
SATIR, SUTUN, HH = slice(9, 73), slice(3, 67), 68   # 64 ürün satırı/sütunu; hanehalkı tüketimi sütunu
P1 = 85                                              # yurt içi tablo: toplam üretim (P.1) satırı
RHO = (0.6, 0.8, 1.0)                                # ithal fiyatına geçişkenlik, P10–P50–P90 [T]
KAPPA = (0.0, 0.5)


def io_indir(klasor):
    """TÜİK Veri Portalı aramasıyla 2023 tablolarını indirir (yoksa)."""
    os.makedirs(klasor, exist_ok=True)
    yollar = {}
    for anahtar, baslik in IO_TABLOLAR.items():
        yol = os.path.join(klasor, anahtar + ".xls")
        if not os.path.exists(yol):
            sonuc = [s for s in tuik.portal_ara(baslik) if s.get("icon") == "tablo"
                     and "2023" in s.get("title", "") and baslik.split(" 2023")[0].lower() in s["title"].lower()]
            tuik.portal_indir(sonuc[0]["url"], yol)
        yollar[anahtar] = yol
    return yollar


def oku(yol):
    t = pd.read_excel(yol, sheet_name=0, header=None)
    kod = t.iloc[SATIR, 1].astype(str).str.strip().tolist()
    return t, kod


def hs6_esleme(rejim_dosyasi):
    """HS6 → (I-O ürün kodu, rejim). CN8 satırlarının AB ithalatı ağırlıklı çoğunluğu."""
    m = pd.read_csv(rejim_dosyasi, dtype={"cn8": str, "cpa21": str})
    m = m[m.cn8.str.fullmatch(r"\d{8}") & m.cpa21.notna()].copy()
    m["hs6"] = m.cn8.str[:6]
    m["io"] = m.cpa21.str[:2].map(io_kodu)
    m["w"] = m.tr_ith_ab.fillna(0) + 1.0
    io = m.groupby(["hs6", "io"]).w.sum().reset_index().sort_values(["hs6", "w"]).drop_duplicates("hs6", keep="last")
    rj = m.groupby(["hs6", "rejim"]).w.sum().reset_index().sort_values(["hs6", "w"]).drop_duplicates("hs6", keep="last")
    return io.set_index("hs6").io, rj.set_index("hs6").rejim


def io_kodu(bolum):
    """CPA 2.1 bölümü (2 hane) → TÜİK 64 ürünlük girdi-çıktı kodu (mal ürünleri)."""
    b = int(bolum)
    if b in (1, 2, 3):
        return f"A0{b}"
    if 5 <= b <= 9:
        return "B"
    if 10 <= b <= 12:
        return "C10-C12"
    if 13 <= b <= 15:
        return "C13-C15"
    if b in (31, 32):
        return "C31_C32"
    if 16 <= b <= 33:
        return f"C{b}"
    if b == 35:
        return "D35"
    if b == 36:
        return "E36"
    if 37 <= b <= 39:
        return "E37-E39"
    if b == 58:
        return "J58"
    if b in (59, 60):
        return "J59_J60"
    return None


def model(A_d, A_m, h_d, h_m, w, dtau, rho, kappa):
    """Ürün başına tüketici fiyat değişimi (oran) ve TÜFE etkisi (oran)."""
    n = len(h_d)
    dp_d = np.linalg.solve(np.eye(n) - A_d.T, A_m.T @ (rho * dtau))
    pay_d = np.divide(h_d, h_d + h_m, out=np.zeros(n), where=(h_d + h_m) > 0)
    dP = pay_d * (dp_d + kappa * rho * dtau) + (1 - pay_d) * rho * dtau
    return dP, float(w @ dP), dp_d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baci-tr", required=True, help="baci_hs17_tur_bilateral_hs6_2020_2024.csv.gz (baci_ozet.py)")
    ap.add_argument("--cache", default=os.path.expanduser("~/.cache/gb_cikis"))
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    v = lambda f: os.path.join(a.out, f)  # noqa: E731
    yollar = io_indir(os.path.join(a.cache, "io2023"))

    yd, kod = oku(yollar["yurtici"])
    it, kod_m = oku(yollar["ithalat"])
    ka, kod_k = oku(yollar["kullanim_alici"])
    assert kod == kod_m == kod_k, "ürün sıraları farklı"
    Z_d = yd.iloc[SATIR, SUTUN].astype(float).to_numpy()
    Z_m = it.iloc[SATIR, SUTUN].astype(float).to_numpy()
    x = yd.iloc[P1, SUTUN].astype(float).to_numpy()
    h_d = yd.iloc[SATIR, HH].astype(float).to_numpy()
    h_m = it.iloc[SATIR, HH].astype(float).to_numpy()
    h_alici = ka.iloc[SATIR, HH].astype(float).to_numpy()
    A_d = np.divide(Z_d, x, out=np.zeros_like(Z_d), where=x > 0)
    A_m = np.divide(Z_m, x, out=np.zeros_like(Z_m), where=x > 0)
    w = np.where(np.array(kod) == "L68A", 0.0, np.clip(h_alici, 0, None))
    w = w / w.sum()

    # AB payı ve AB ithalatına uygulanacak oran (HS6 → I-O ürünü)
    hs6_io, hs6_rejim = hs6_esleme(v("cn2025_nace_rejim.csv"))
    b = pd.read_csv(a.baci_tr, dtype={"hs6": str})
    b = b[(b.year == b.year.max()) & (b.flow == "M")]
    b["hs6"] = b.hs6.str.zfill(6)
    imp = b.groupby("hs6").value_kusd.sum().rename("m_dunya").to_frame()
    imp["m_ab"] = b[b.eu27 == 1].groupby("hs6").value_kusd.sum()
    imp = imp.fillna(0)
    tr = pd.read_csv(v("tarife_tr_2026_gtip12.csv"), dtype={"gtip12": str, "hs6": str})
    tr = tr[~tr.in_tgtc_only]
    imp["t_mfn"] = tr.groupby("hs6").mfn_rate.mean()
    imp["t_igv"] = tr.groupby("hs6").mfn_igv_emy.mean()
    imp["io"] = imp.index.map(hs6_io)
    imp["rejim"] = imp.index.map(hs6_rejim)
    eslesen = imp.loc[imp.io.notna(), "m_dunya"].sum() / imp.m_dunya.sum()
    imp = imp[imp.io.notna()]

    satirlar = []
    for c in kod:
        g = imp[imp.io == c]
        r = dict(io=c, m_dunya_musd=g.m_dunya.sum() / 1e3, m_ab_musd=g.m_ab.sum() / 1e3)
        r["s_ab"] = r["m_ab_musd"] / r["m_dunya_musd"] if r["m_dunya_musd"] else 0.0
        for var, kapsam in (("i", ["GB", "ITU"]), ("ii", ["GB", "ITU", "TARIM"])):
            k = g[g.rejim.isin(kapsam)]
            for olcu in ("mfn", "igv"):
                t = k[f"t_{olcu}"].fillna(0)
                r[f"t_{olcu}_{var}"] = (k.m_ab * t).sum() / g.m_ab.sum() if g.m_ab.sum() else 0.0
        satirlar.append(r)
    t = pd.DataFrame(satirlar).set_index("io")
    t.insert(0, "ad", yd.iloc[SATIR, 2].astype(str).str.strip().tolist())
    t["agirlik_tufe"] = w
    t["ithal_payi_hh"] = np.divide(h_m, h_d + h_m, out=np.zeros(len(h_d)), where=(h_d + h_m) > 0)
    t["ithal_girdi_payi"] = A_m.sum(axis=0)

    # EDE: 1 puanlık tarifenin TÜFE etkisi (bp); tüm ithalata ve yalnızca AB ithalatına
    n = len(kod)
    for i, c in enumerate(kod):
        e = np.zeros(n)
        e[i] = 0.01
        t.loc[c, "ede_tum_bp"] = model(A_d, A_m, h_d, h_m, w, e, 1.0, 0.0)[1] * 1e4
        e[i] = 0.01 * t.loc[c, "s_ab"]
        t.loc[c, "ede_ab_bp"] = model(A_d, A_m, h_d, h_m, w, e, 1.0, 0.0)[1] * 1e4

    ozet = []
    for var in ("i", "ii"):
        for olcu in ("mfn", "igv"):
            dtau = (t.s_ab * t[f"t_{olcu}_{var}"] / 100).to_numpy()
            for rho in RHO:
                for kappa in KAPPA:
                    dP, toplam, dp_d = model(A_d, A_m, h_d, h_m, w, dtau, rho, kappa)
                    dogrudan = float(w @ ((1 - np.divide(h_d, h_d + h_m, out=np.zeros(n), where=(h_d + h_m) > 0))
                                          * rho * dtau))
                    ozet.append(dict(varyant=var, tarife=olcu, rho=rho, kappa=kappa, tufe_bp=toplam * 1e4,
                                     dogrudan_bp=dogrudan * 1e4, dolayli_bp=(toplam - dogrudan) * 1e4))
                    if rho == 0.8 and kappa == 0.0:
                        t[f"s4_katki_bp_{olcu}_{var}"] = w * dP * 1e4
                        t[f"s4_uretici_fiyat_yuzde_{olcu}_{var}"] = dp_d * 100
    oz = pd.DataFrame(ozet)
    oz.round(2).to_csv(v("politika_io_s4_tufe.csv"), index=False)
    t.round(5).to_csv(v("politika_io_ede.csv"))

    print(f"HS6 → I-O eşleşmesi Türkiye ithalatının %{100 * eslesen:.1f}'i")
    pd.set_option("display.width", 250)
    print(oz[(oz.kappa == 0.0)].round(1).to_string(index=False))
    print(oz[(oz.kappa == 0.5) & (oz.rho == 0.8)].round(1).to_string(index=False))
    sut = ["ad", "agirlik_tufe", "ithal_payi_hh", "s_ab", "t_mfn_i", "t_igv_i", "ede_tum_bp", "ede_ab_bp",
           "s4_katki_bp_mfn_i", "s4_katki_bp_igv_i"]
    print(t[sut].sort_values("s4_katki_bp_igv_i", ascending=False).head(25).round(3).to_string())


if __name__ == "__main__":
    main()
