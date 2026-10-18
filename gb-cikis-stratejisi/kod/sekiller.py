"""Belgelerdeki şekiller: veri/ klasöründeki çıktılardan PNG (Markdown) ve PDF (LaTeX) üretir.

Şekiller (sekiller/):
  f1_ab_ticaret        Türkiye–AB27 ticareti ve AB27'nin payı, 1991–2025 (teshis_ab_ticaret_1991_2025.csv)
  f1_cari_denge        Cari denge, enerji ve altın hariç çekirdek denge, 2010–2025 (teshis_odemeler_dengesi.csv)
  f1_bolum_maruziyet   NACE bölümü: AB'ye ihracat payı ve S4 risk istihdamı (teshis_bolum_maruziyet.csv)
  f2_takas_tasarim     Vergi takası: dört tasarımın net mali maliyeti ve istihdamı (politika_takas_ozet.csv)
  f2_s4_paket_siniri   Aktif S4: TÜFE etkisi ve tahsil edilebilir net mali etki, rejim × takas (politika_s4_aktif.csv)
  f2_net_istihdam      S4 net istihdam, NACE bölümü: yalnızca MFN ve rejim c2 (politika_s4_net_istihdam_sinif.csv)
  f2_cekim_senaryo     Çekim modeli: S2, S3, S4'ün Türkiye'nin AB'ye ihracatına etkisi, %90 GA (politika_cekim_senaryolar.csv)
  f2_cekim_zaman_yolu  GB ve derin STA etkisinin zaman yolu, M2 (politika_cekim_katsayilar.csv)
Kullanım: python3 sekiller.py [--veri ../veri] [--cikti ../sekiller]
"""

import argparse
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

RENK = {"ab": "#1f4e79", "dunya": "#7f7f7f", "vurgu": "#c00000", "yesil": "#2e7d32", "turuncu": "#e07b00",
        "mor": "#6a3d9a", "acik": "#9dc3e6"}
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.grid": True, "grid.alpha": 0.25, "figure.dpi": 100,
                     "axes.formatter.use_locale": False})


def kaydet(fig, cikti, ad):
    fig.tight_layout()
    for uzanti in ("png", "pdf"):
        fig.savefig(os.path.join(cikti, f"{ad}.{uzanti}"), dpi=200 if uzanti == "png" else None, bbox_inches="tight")
    plt.close(fig)


def virgul(x, ondalik=0):
    return f"{x:,.{ondalik}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def f1_ab_ticaret(v, c):
    t = pd.read_csv(os.path.join(v, "teshis_ab_ticaret_1991_2025.csv"))
    fig, ax = plt.subplots(1, 2, figsize=(8.6, 3.2))
    ax[0].plot(t.yil, t.tr_ihracat_ab27_musd / 1e3, color=RENK["ab"], lw=2, label="İhracat, AB27")
    ax[0].plot(t.yil, t.tr_ithalat_ab27_musd / 1e3, color=RENK["ab"], lw=2, ls="--", label="İthalat, AB27")
    ax[0].plot(t.yil, (t.tr_ihracat_dunya_musd - t.tr_ihracat_ab27_musd) / 1e3, color=RENK["dunya"], lw=1.5,
               label="İhracat, AB27 dışı")
    ax[0].axvline(1996, color=RENK["vurgu"], lw=1, ls=":")
    ax[0].text(1996.5, ax[0].get_ylim()[1] * 0.92, "GB (1996)", color=RENK["vurgu"], fontsize=8)
    ax[0].set_title("Türkiye'nin ticareti (milyar $)", fontsize=9)
    ax[0].legend(frameon=False, fontsize=7.5)
    ax[1].plot(t.yil, 100 * t.ab27_ihracat_payi, color=RENK["ab"], lw=2, label="İhracatta AB27 payı")
    ax[1].plot(t.yil, 100 * t.ab27_ithalat_payi, color=RENK["ab"], lw=2, ls="--", label="İthalatta AB27 payı")
    ax[1].axvline(1996, color=RENK["vurgu"], lw=1, ls=":")
    ax[1].set_title("AB27'nin payı (%)", fontsize=9)
    ax[1].legend(frameon=False, fontsize=7.5)
    for a in ax:
        a.set_xlim(1991, 2025)
    fig.text(0.01, -0.02, "Kaynak: UN Comtrade (Türkiye beyanı); veri/teshis_ab_ticaret_1991_2025.csv", fontsize=7,
             color="#555555")
    kaydet(fig, c, "f1_ab_ticaret")


def f1_cari_denge(v, c):
    t = pd.read_csv(os.path.join(v, "teshis_odemeler_dengesi.csv"))
    t = t[(t.yil >= 2010) & (t.yil <= 2025)]
    fig, ax = plt.subplots(figsize=(8.6, 3.4))
    ax.bar(t.yil - 0.3, t.cari_denge_gsyh, width=0.3, color=RENK["ab"], label="Cari denge")
    ax.bar(t.yil, t.enerji_net_gsyh, width=0.3, color=RENK["turuncu"], label="Enerji (net)")
    ax.bar(t.yil + 0.3, t.parasal_olmayan_altin_net_gsyh, width=0.3, color="#c9a227", label="Parasal olmayan altın (net)")
    ax.plot(t.yil, t.cari_denge_altin_enerji_haric_gsyh, color=RENK["yesil"], lw=2, marker="o", ms=3,
            label="Altın ve enerji hariç çekirdek denge")
    ax.axhline(0, color="black", lw=0.6)
    ax.set_xlim(2009.4, 2025.6)
    ax.set_ylim(-10.5, 10.5)
    ax.set_xticks(range(2010, 2026, 2))
    ax.set_title("Cari denge bileşenleri (GSYH'nin %'si)", fontsize=9)
    ax.legend(frameon=False, fontsize=7.5, ncol=2, loc="upper left")
    fig.text(0.01, -0.03, "Kaynak: TCMB EVDS (ödemeler dengesi, BPM6); veri/teshis_odemeler_dengesi.csv", fontsize=7,
             color="#555555")
    kaydet(fig, c, "f1_cari_denge")


def f1_bolum_maruziyet(v, c):
    t = pd.read_csv(os.path.join(v, "teshis_bolum_maruziyet.csv"), dtype={"bolum": str})
    t = t[t.bolum.str.fullmatch(r"(1\d|2\d|3[0-3])") & t.s4_risk_istihdam.notna()]
    t = t.sort_values("s4_risk_istihdam", ascending=True).tail(15)
    fig, ax = plt.subplots(1, 2, figsize=(8.6, 3.8), sharey=True)
    etiket = t.bolum + " " + t.ad.map(lambda a: a if len(a) <= 30 else a[:30].rsplit(" ", 1)[0] + "…")
    ax[0].barh(etiket, 100 * t.ab_payi_ihracat, color=RENK["ab"])
    ax[0].set_title("İhracatta AB27 payı (%)", fontsize=9)
    ax[1].barh(etiket, t.s4_risk_istihdam / 1e3, color=RENK["vurgu"])
    ax[1].set_title("S4 risk istihdamı (bin kişi, σ = 5)", fontsize=9)
    ax[0].tick_params(axis="y", labelsize=7)
    fig.text(0.01, -0.02, "Kaynak: TÜİK YSHİ 2024, Comtrade 2025, Faz 0 tarife duvarı; veri/teshis_bolum_maruziyet.csv",
             fontsize=7, color="#555555")
    kaydet(fig, c, "f1_bolum_maruziyet")


def f2_takas_tasarim(v, c):
    o = pd.read_csv(os.path.join(v, "politika_takas_ozet.csv"))
    o = o[(o.grup == "TOPLAM") & (o.kural == "laspeyres") & o.senaryo.str.startswith("S4_c2_")]
    ad = {"S4_c2_yok": "Pasif\nS4", "S4_c2_TA_takas": "T-A\ntakas", "S4_c2_T0_yalniz_yerli": "T-0\nyalnız\nyerli*",
          "S4_c2_TB_uretim_destegi": "T-B\nüretim\ndesteği"}
    sira = list(ad)
    m = o.pivot_table(index="senaryo", columns="olcu", values=["merkez", "p10", "p90"]).reindex(sira)
    fig, ax = plt.subplots(1, 3, figsize=(8.6, 3.0))
    x = np.arange(len(sira))
    for i, (olcu, baslik, olc, renk) in enumerate([
            ("tufe_katki_bp", "TÜFE katkısı (bp)", 1, RENK["turuncu"]),
            ("d_mali_musd", "Net mali etki (milyar $)", 1e-3, RENK["ab"]),
            ("istihdam_degisimi", "İstihdam (bin kişi)", 1e-3, RENK["yesil"])]):
        merkez = m[("merkez", olcu)] * olc
        hata = np.vstack([merkez - m[("p10", olcu)] * olc, m[("p90", olcu)] * olc - merkez]).clip(min=0)
        ax[i].bar(x, merkez, color=renk, yerr=hata, capsize=3, error_kw={"lw": 0.8})
        ax[i].set_xticks(x, [ad[s] for s in sira], fontsize=7.5)
        ax[i].set_title(baslik, fontsize=9)
        ax[i].axhline(0, color="black", lw=0.6)
    fig.text(0.01, -0.06, "On ürün grubu, rejim c2; merkez σ = 4, η = 1, ρ = 1; hata çubukları P10–P90. *T-0 GATT III:2'ye aykırı; "
             "yalnızca karşılaştırma için.\nKaynak: kod/f2c_vergi_takasi.py; veri/politika_takas_ozet.csv", fontsize=7,
             color="#555555")
    kaydet(fig, c, "f2_takas_tasarim")


def f2_s4_paket_siniri(v, c):
    o = pd.read_csv(os.path.join(v, "politika_s4_aktif.csv"))
    o = o[(o.P1 == True) & o.rejim.isin(["a_igv_ab_dahil", "b_igv_kaldirilir", "c_igv_secici",  # noqa: E712
                                           "c2_igv_secici_kabiliyet"])]
    ad = {"a_igv_ab_dahil": "a: İGV AB'ye de", "b_igv_kaldirilir": "b: İGV herkes için kalkar",
          "c_igv_secici": "c: seçici", "c2_igv_secici_kabiliyet": "c2: kabiliyete duyarlı"}
    isaret = {"yok": "o", "dar": "s", "genis": "^"}
    renk = {"a_igv_ab_dahil": RENK["vurgu"], "b_igv_kaldirilir": RENK["dunya"], "c_igv_secici": RENK["turuncu"],
            "c2_igv_secici_kabiliyet": RENK["ab"]}
    fig, ax = plt.subplots(figsize=(8.6, 3.8))
    for (r, p3), g in o.groupby(["rejim", "P3"]):
        g = g.set_index("rho")
        y, x = g.loc[0.8, "tufe_bp"], g.loc[0.8, "net_mali_tahsil_gsyh_yuzde"]
        ax.errorbar(x, y, yerr=[[y - g.tufe_bp.min()], [g.tufe_bp.max() - y]], fmt=isaret[p3],
                    color=renk[r], ms=6, capsize=2, lw=0.8)
    ax.axhspan(-40, 30, color=RENK["yesil"], alpha=0.06)
    ax.axhline(30, color=RENK["yesil"], lw=0.8, ls="--")
    ax.text(0.99, 31.5, "Yıllık TÜFE tavanı: 30 bp", color=RENK["yesil"], fontsize=7.5, ha="right",
            transform=ax.get_yaxis_transform())
    ax.axvline(0, color="black", lw=0.6)
    for r in ad:
        ax.plot([], [], "o", color=renk[r], label=ad[r])
    for p3, ms in isaret.items():
        ax.plot([], [], ms, color="black", mfc="none", label={"yok": "takas yok", "dar": "dar takas", "genis": "geniş takas"}[p3])
    ax.legend(frameon=False, fontsize=7, ncol=2, loc="upper left")
    ax.set_xlabel("Net mali etki, tahsil edilebilir (GSYH %)")
    ax.set_ylabel("TÜFE, birinci tur (bp)")
    ax.set_title("Aktif S4 paket sınırı (girdide sıfır dahil; dikey çubuk ρ = 0,6–1,0)", fontsize=9)
    fig.text(0.01, -0.02, "Kaynak: kod/f2e_s4_aktif.py; veri/politika_s4_aktif.csv", fontsize=7, color="#555555")
    kaydet(fig, c, "f2_s4_paket_siniri")


def f2_net_istihdam(v, c):
    t = pd.read_csv(os.path.join(v, "politika_s4_net_istihdam_sinif.csv"), dtype={"sinif": str})
    t["bolum"] = t.sinif.str[:2]
    g = t.groupby("bolum")[["istihdam_ihracat_s5", "istihdam_ikame_s5", "istihdam_ikame_c2_s5",
                            "istihdam_net_s5", "istihdam_net_c2_s5"]].sum() / 1e3
    toplam_mfn, toplam_c2 = g.istihdam_net_s5.sum(), g.istihdam_net_c2_s5.sum()
    g = g[(g.istihdam_ihracat_s5.abs() > 0.9) | (g.istihdam_ikame_c2_s5.abs() > 0.9)].sort_values("istihdam_net_c2_s5")
    fig, ax = plt.subplots(figsize=(8.6, 3.6))
    x = np.arange(len(g))
    ax.bar(x - 0.2, g.istihdam_net_s5, width=0.4, color=RENK["dunya"], label="Net, yalnızca MFN")
    ax.bar(x + 0.2, g.istihdam_net_c2_s5, width=0.4, color=RENK["ab"], label="Net, rejim c2")
    ax.scatter(x, g.istihdam_ihracat_s5, marker="_", s=120, color=RENK["vurgu"], label="İhracat tarafı kaybı")
    ax.axhline(0, color="black", lw=0.6)
    ax.set_xticks(x, g.index, fontsize=8)
    ax.set_xlabel("NACE bölümü")
    ax.set_ylabel("bin kişi")
    ax.set_title(f"Anlaşmasız çıkışta net imalat istihdamı (σ = 5): toplam MFN {virgul(toplam_mfn)} bin, "
                 f"c2 {virgul(toplam_c2)} bin".replace("-", "−"), fontsize=9)
    ax.legend(frameon=False, fontsize=7.5)
    fig.text(0.01, -0.02, "Kaynak: kod/f2d_s4_net_istihdam.py; veri/politika_s4_net_istihdam_sinif.csv", fontsize=7,
             color="#555555")
    kaydet(fig, c, "f2_net_istihdam")


def f2_cekim_senaryo(v, c):
    s = pd.read_csv(os.path.join(v, "politika_cekim_senaryolar.csv"))
    satir = [("S2", "M1_ana", "GE_tam_sigma7", "S2 derin STA"),
             ("S3_TR", "M5_genisleme", "GE_tam_sigma7", "S3 ihtiyatlı\n(aday ülke STA → GB)"),
             ("S3_BK", "R2e_baci_2024", "GE_tam_sigma7", "S3 iyimser\n(TR–BK 2021)"),
             ("S4", "M1_ana", "GE_tam_sigma7", "S4 anlaşmasız")]
    fig, ax = plt.subplots(figsize=(8.6, 3.3))
    for i, (sen, ke, ge, ad) in enumerate(satir):
        for j, (spec, renk, et) in enumerate([(ke, RENK["acik"], "Kısmi denge"), (ge, RENK["ab"], "Genel denge (σ = 7)")]):
            r = s[(s.spesifikasyon == spec) & (s.senaryo == sen) & (s.yon == "TR→AB")]
            if r.empty:
                continue
            r = r.iloc[0]
            y = i + (j - 0.5) * 0.3
            ax.errorbar(r.degisim_yuzde, y, xerr=[[r.degisim_yuzde - r.ci90_alt_yuzde], [r.ci90_ust_yuzde - r.degisim_yuzde]],
                        fmt="o", color=renk, capsize=3, lw=1.2, label=et if i == 0 else None)
    ax.axvline(0, color="black", lw=0.6)
    ax.set_yticks(range(len(satir)), [x[3] for x in satir], fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("Türkiye'nin AB'ye ihracatı, S0'a (GB) göre % değişim; %90 GA")
    ax.set_title("Çekim modeli senaryoları (PPML, 150 ekonomi, 1988–2020; BK için 2024)", fontsize=9)
    ax.legend(frameon=False, fontsize=7.5, loc="lower right")
    fig.text(0.01, -0.03, "Kaynak: kod/f2f_cekim_modeli.py; veri/politika_cekim_senaryolar.csv", fontsize=7, color="#555555")
    kaydet(fig, c, "f2_cekim_senaryo")


def f2_cekim_zaman_yolu(v, c):
    k = pd.read_csv(os.path.join(v, "politika_cekim_katsayilar.csv"))
    k = k[k.spesifikasyon == "M2_gecikmeli"]
    fig, ax = plt.subplots(figsize=(8.6, 3.0))
    for ad, et, renk, kay in [("GB_TR_AB", "GB: Türkiye → AB", RENK["ab"], -0.6), ("GB_AB_TR", "GB: AB → Türkiye", RENK["turuncu"], 0),
                              ("AB_STA_DERIN", "AB'nin derin STA'ları", RENK["yesil"], 0.6)]:
        noktalar = []
        for gec, deg in [(0, ad), (4, f"{ad}_kumulatif_4yil"), (8, f"{ad}_kumulatif_8yil"), (12, f"{ad}_kumulatif_12yil")]:
            r = k[k.degisken == deg]
            if not r.empty:
                r = r.iloc[0]
                noktalar.append((gec, r.katsayi, r.ci90_alt, r.ci90_ust))
        if not noktalar:
            continue
        n = np.array(noktalar)
        y = 100 * (np.exp(n[:, 1]) - 1)
        hata = np.vstack([y - 100 * (np.exp(n[:, 2]) - 1), 100 * (np.exp(n[:, 3]) - 1) - y])
        ax.errorbar(n[:, 0] + kay, y, yerr=hata, fmt="-o", color=renk, capsize=3, lw=1.3, ms=4, label=et)
    ax.axhline(0, color="black", lw=0.6)
    ax.set_xticks([0, 4, 8, 12], ["0–3 yıl", "4–7 yıl", "8–11 yıl", "12+ yıl"])
    ax.set_ylabel("% etki (kümülatif)")
    ax.set_title("Etkinin zaman yolu (M2): GB etkisi hemen ortaya çıkıyor, sonra sönümleniyor; %90 GA", fontsize=9)
    ax.legend(frameon=False, fontsize=7.5)
    fig.text(0.01, -0.04, "Kaynak: kod/f2f_cekim_modeli.py; veri/politika_cekim_katsayilar.csv", fontsize=7, color="#555555")
    kaydet(fig, c, "f2_cekim_zaman_yolu")


def main():
    kok = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    ap = argparse.ArgumentParser()
    ap.add_argument("--veri", default=os.path.join(kok, "veri"))
    ap.add_argument("--cikti", default=os.path.join(kok, "sekiller"))
    a = ap.parse_args()
    os.makedirs(a.cikti, exist_ok=True)
    for f in (f1_ab_ticaret, f1_cari_denge, f1_bolum_maruziyet, f2_takas_tasarim, f2_s4_paket_siniri, f2_net_istihdam,
              f2_cekim_senaryo, f2_cekim_zaman_yolu):
        f(a.veri, a.cikti)
        print("şekil:", f.__name__)


if __name__ == "__main__":
    main()
