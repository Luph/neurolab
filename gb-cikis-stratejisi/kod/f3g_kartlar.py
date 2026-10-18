"""Faz 3 — NACE sınıf kartları (ana prompt <nace_karti>) ve bölüm belgesi: nace_kartlar_[bölüm].md.

Sayısal alanlar veriden üretilir (veri/nace_matris.csv ve f3_* tabloları); nitel alanlar (çapa yatırımcılar, menşe
kuralı, kırmızı çizgiler, eylem tablosu, müzakere, tetikler, riskler) kartlar/[bölüm].yaml dosyasından okunur. YAML'daki
arketip/duruş/tarife yolu/araç/müzakere alanları matristeki kural tabanlı ilk öneriyi uzman muhakemesiyle düzeltir
(f3f bu düzeltmeleri matrise de yazar).

Kullanım: python3 f3g_kartlar.py --yaml ../kartlar/10-12.yaml --cikti ../nace_kartlar_10-12.md
"""

import argparse
import os
import re

import numpy as np
import pandas as pd
import yaml

import f3a_ticaret as f3a
import yollar

SEN = ("S2", "S3", "S4")


def tr(x, nd=0, isaret=False):
    """Türkçe sayı biçimi: binlik nokta, ondalık virgül, eksi işareti U+2212."""
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "—"
    if round(x, nd) == 0:
        x, isaret = 0.0, False            # "−0" ve "+0" yerine "0"
    s = f"{x:+,.{nd}f}" if isaret else f"{x:,.{nd}f}"
    s = s.replace(",", "§").replace(".", ",").replace("§", ".")
    return s.replace("-", "−")


YER = re.compile(r"\{\{(\d\d\.\d\d|C|10|11|12|10-12)\|([a-z0-9_]+)\|(\d)(?:\|(abs|pct|pctabs|isaret))?\}\}")


def doldur(metin, m):
    """Metindeki {{kod|sütun|ondalık|biçim}} yer tutucularını nace_matris değerleriyle doldurur.
    kod: sınıf kodu, bölüm (10, 11, 12), 10-12 ya da C (230 sınıf toplamı); bölüm ve C için sütun toplamı."""
    def bir(mt):
        kod, sut, nd, bic = mt.group(1), mt.group(2), int(mt.group(3)), mt.group(4)
        if kod in m.index:
            x = float(m.at[kod, sut])
        else:
            sec = {"C": m.index, "10-12": m.index[m.index.str[:2].isin(["10", "11", "12"])]}.get(kod, m.index[m.index.str[:2] == kod])
            x = float(m.loc[sec, sut].sum())
        if bic == "abs":
            x = abs(x)
        if bic in ("pct", "pctabs"):
            x = 100 * (abs(x) if bic == "pctabs" else x)
        return tr(x, nd, bic == "isaret")
    return YER.sub(bir, metin)


def doldur_hepsi(o, m):
    if isinstance(o, str):
        return doldur(o, m)
    if isinstance(o, list):
        return [doldur_hepsi(x, m) for x in o]
    if isinstance(o, dict):
        return {k: doldur_hepsi(x, m) for k, x in o.items()}
    return o


def yuzde(x, nd=0):
    return "—" if x is None or (isinstance(x, float) and np.isnan(x)) else f"%{tr(100 * x, nd)}"


def hucre(s):
    return str(s).replace("|", "/").replace("\n", " ")


def tablo(baslik, sutunlar, satirlar, kaynak=None):
    out = [f"**{baslik}**", "", "| " + " | ".join(sutunlar) + " |", "|" + "---|" * len(sutunlar)]
    out += ["| " + " | ".join(hucre(c) for c in r) + " |" for r in satirlar]
    if kaynak:
        out += ["", f"*Kaynak:* {kaynak}"]
    return "\n".join(out) + "\n"


class Veri:
    def __init__(self, v, cache):
        self.veri = v
        oku = lambda f, **k: pd.read_csv(os.path.join(v, f), **k)  # noqa: E731
        self.m = oku("nace_matris.csv", dtype={"kod": str}).set_index("kod")
        self.t = oku("f3_ticaret_sinif.csv", dtype={"nace2": str}).set_index("nace2")
        self.y = oku("f3_yapi_sinif.csv", dtype={"kod": str}).set_index("kod")
        self.p = oku("f3_pci_sinif.csv", dtype={"kod": str}).set_index("kod")
        self.ab = oku("f3_ab_tarife_sinif.csv", dtype={"kod": str}).set_index("kod")
        self.mk = oku("f3_makro_sinif.csv", dtype={"kod": str}).set_index("kod")
        self.o = oku("f3_ortaklar_sinif.csv", dtype={"nace2": str})
        self.b = oku("f3_bolge_sinif.csv", dtype={"kod": str})
        self.sn = oku("f3_senaryo_sinif.csv", dtype={"kod": str})
        self.k = oku("nace_kapsam.csv", dtype={"kod": str}).set_index("kod")
        self.va = oku("f3_sinif_varsayim.csv", dtype={"kod": str}).set_index("kod")
        self.kn8 = oku("f3_ab_tarife_kn8.csv", dtype={"cn8": str, "nace2": str})
        h = oku("politika_tarife_hs6.csv", dtype={"hs6": str})
        ag = f3a.hs6_nace_agirlik(os.path.join(v, "cn2025_nace_rejim.csv"))
        h["w_mfn"], h["w_tam"] = h.m_toplam_musd * h.t_mfn.fillna(0), h.m_toplam_musd * h.t_tam.fillna(0)
        h["tic"] = h.m_toplam_musd + h.x_musd
        for k in ("ara", "sermaye", "tuketim"):
            h[f"bec_{k}"] = h.tic * h.kullanim.eq(k)
        sut = ["m_toplam_musd", "w_mfn", "w_tam", "tic", "bec_ara", "bec_sermaye", "bec_tuketim"]
        self.h, _ = f3a.nace_dagit(h[["hs6"] + sut], ag, sut, [])
        self.h = self.h.set_index("nace2")
        bt = pd.read_csv(yollar.girdi("baci", "baci_hs17_tur_bilateral_hs6_2020_2024.csv.gz"), dtype={"hs6": str})
        bt = bt[bt.year == bt.year.max()].copy()
        bt["hs6"] = bt.hs6.str.zfill(6)
        self.bt = bt
        x = bt[bt.flow == "X"].groupby("hs6", as_index=False).value_kusd.sum()
        xn, _ = f3a.nace_dagit(x.assign(hs4=x.hs6.str[:4]).rename(columns={"value_kusd": "v"}), ag, ["v"], ["hs4"])
        self.hs4 = xn
        self.ag = ag

    def tepe(self, kod):
        k = self.kn8[(self.kn8.nace2 == kod) & (self.kn8.artis_s4 >= 10)].sort_values("x_ab_meur", ascending=False)
        pay = k.x_ab_meur.sum() / max(self.kn8[self.kn8.nace2 == kod].x_ab_meur.sum(), 1e-9)
        if k.empty or (pay < 0.01 and k.x_ab_meur.sum() < 1):
            return "yok (AB ihracatının %1'inden az)" if not k.empty else "yok"
        ilk = "; ".join(f"KN {r.cn8[:4]} {r.cn8[4:6]} {r.cn8[6:]} %{tr(r.artis_s4, 1)} (€{tr(r.x_ab_meur, 1)} mn)"
                        for r in k.head(3).itertuples())
        return f"{len(k)} satır, AB ihracatının {yuzde(pay)}'i: {ilk}"

    def senaryo(self, kod, dg, sc):
        r = self.sn[(self.sn.kod == kod) & (self.sn.degisken == dg) & (self.sn.senaryo == sc)]
        return r.iloc[0] if len(r) else None

    def girdi(self, kodlar):
        """Kritik girdi HS4 listesi: 2024 ithalatı, ilk 3 kaynak."""
        m = self.bt[(self.bt.flow == "M") & self.bt.hs6.str[:4].isin(kodlar)]
        if m.empty:
            return "—"
        top = m.value_kusd.sum() / 1e3
        k = m.groupby("partner_iso3").value_kusd.sum().sort_values(ascending=False) / 1e3
        ab = m[m.eu27 == 1].value_kusd.sum() / 1e3
        ilk = ", ".join(f"{a} {yuzde(v / top)}" for a, v in k.head(3).items())
        return f"${tr(top)} mn (AB {yuzde(ab / top)}; {ilk})"


def kart(V, kod, y, sira):
    m, t, yy = V.m.loc[kod], V.t.reindex([kod]).iloc[0], V.y.reindex([kod]).iloc[0]
    k, mk = V.k.loc[kod], V.mk.loc[kod]
    ab = V.ab.reindex([kod]).iloc[0]
    y = y or {}
    ark = "/".join(a for a in [m.arketip_birincil, m.arketip_ikincil] if isinstance(a, str) and a)
    out = [f"### {sira} {kod} {k.ad_tr} — GB statüsü: {k.gb_statusu} | Birincil/ikincil arketip: {ark} | "
           f"Duruş: {m.durus}", ""]
    if y.get("ozet"):
        out += [f"*{y['ozet']}*", ""]

    # 1 Kimlik
    hs = V.hs4[V.hs4.nace2 == kod].sort_values("v", ascending=False)
    hs_top = hs.v.sum()
    fasil = ", ".join(f"{r.hs4} {yuzde(r.v / hs_top)}" for r in hs.head(4).itertuples()) if hs_top > 0 else "—"
    hb = V.h.reindex([kod]).iloc[0]
    bec = "—"
    if hb.notna().any() and hb.tic > 0:
        bec = f"ara {yuzde(hb.bec_ara / hb.tic)} / sermaye {yuzde(hb.bec_sermaye / hb.tic)} / tüketim {yuzde(hb.bec_tuketim / hb.tic)}"
    rev = f"{k.rev21} ({k.kopru_tipi})" if isinstance(k.rev21, str) else "—"
    out += [f"**1. Kimlik.** Rev. 2.1: {rev}; CPA {kod}. Başlıca HS4 (TR ihracatı 2024): {fasil}. BEC payları (ticaret "
            f"ağırlıklı): {bec}. {y.get('kimlik', '')}".rstrip(), ""]

    # 2 Ölçek
    bol = V.b[(V.b.kod == kod) & (V.b.sira <= 3)]
    bolge = "; ".join(f"{r.bolge} {yuzde(r.pay)}" for r in bol.itertuples()) or "—"
    olc = " / ".join(tr(yy.get(f"girisim_{g}")) for g in ("0", "1_9", "10_49", "50_249", "250p"))
    gizli = " `[T]` (gizli; bölüm kalanından)" if yy.get("gizli_tahmin") is True else " `[V]`"
    satir = [["Üretim değeri; katma değer", f"${tr(yy.get('uretim_musd'))} mn; ${tr(yy.get('kd_musd'))} mn "
              f"(GSYH'nin {yuzde(yy.get('kd_gsyh_payi_yuzde', np.nan) / 100, 2)})", f"TÜİK YSHİ 2024{gizli}"],
             ["Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+)", f"{tr(yy.get('calisan'))}; {tr(yy.get('girisim'))} ({olc})",
              "TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]`"],
             ["250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD", f"{yuzde(yy.get('buyuk_isletme_istihdam_payi'))}; "
              f"{tr(yy.get('verimlilik_ab_orani'), 2)}", "`[T]` (AB27 SBS 2023, nominal kur)"],
             ["İlk 3 İBBS-2 bölgesi", bolge, "`[T]` iş kayıtları + SGK 2025, RAS"],
             ["Yabancı sermaye; çapa yatırımcılar", y.get("capa", "—"), "`[H]` (firma bilgisi; pay verisi yok: VB-30)"]]
    out += [tablo("2. Ölçek", ["Gösterge", "Değer", "Etiket ve kaynak"], satir)]

    # 3 Dış ticaret
    o = V.o[V.o.nace2 == kod]
    par = lambda tur: "; ".join(f"{r.partner_iso3} {yuzde(r.pay)}" for r in o[o.tur == tur].itertuples()) or "—"  # noqa
    satir = [["İhracat (2024); 2020–24 değişimi", f"${tr(t.x_musd_2024)} mn; {yuzde(t.x_musd_degisim_yuzde / 100)}"],
             ["AB payı; ilk 5 AB pazarı", f"{yuzde(t.ab_ihracat_payi_2024)}; {par('AB pazarı')}"],
             ["İlk 5 AB dışı pazar", par("AB dışı pazar")],
             ["İthalat; AB ve Çin payı; ilk kaynaklar", f"${tr(t.m_musd_2024)} mn; AB {yuzde(t.ab_ithalat_payi_2024)}, Çin "
              f"{yuzde(t.cin_ithalat_payi_2024)}; {par('İthalat kaynağı')}"],
             ["Dış ticaret dengesi", f"${tr(t.denge_musd_2024, isaret=True)} mn"],
             ["İthal girdi içeriği (I-O, toplam) / KD÷üretim", f"{yuzde(mk.m_x)} / {yuzde(yy.get('kd_uretim_orani'))}"],
             ["RCA dünya (2020 → 2024) / AB pazarında", f"{tr(t.rca_dunya_2020, 2)} → {tr(t.rca_dunya_2024, 2)} / "
              f"{tr(t.rca_ab_2024, 2)}"],
             ["Birim değer ÷ AB pazarı ortalaması", tr(t.birim_deger_orani_2024, 2)],
             ["AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası",
              f"{yuzde(t.ab_pazar_payi_abdisi_2020, 1)} → {yuzde(t.ab_pazar_payi_abdisi_2024, 1)}; {tr(t.ab_pazari_tr_sirasi_2024)}."]]
    out += [tablo("3. Dış ticaret", ["Gösterge", "Değer (BACI 2024, $; `[V]`, eşleme `[T]`)"], satir)]

    # 4 AB tarafı
    rakip = par("AB pazarında rakip (AB dışı)")
    satir4 = [f"- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): {yuzde(ab.get('tau_ab_s4', np.nan) / 100, 1)}; 1/98 "
              f"kaybıyla {yuzde(ab.get('tau_ab_s4_tarim_kaybi', np.nan) / 100, 1)}; tam MFN ortalaması "
              f"{yuzde(ab.get('tau_ab_mfn', np.nan) / 100, 1)}. Rejim: GB {yuzde(ab.get('pay_GB', np.nan))}, İTÜ "
              f"{yuzde(ab.get('pay_ITU', np.nan))}, tarım {yuzde(ab.get('pay_TARIM', np.nan))} `[V]`/`[T]`.",
              f"- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): {V.tepe(kod)}.",
              f"- AB pazarında AB dışı rakipler (tercih durumu): {rakip}. Tercihli rakip payı "
              f"{yuzde(t.tercihli_rakip_payi_2024)}.",
              f"- Menşe (S2 / S3): risk {m.mense_riski}; `c_RoO` %{tr(m.c_roo_s2, 1)} / %{tr(m.c_roo_s3, 1)}; `p_uyum` "
              f"{tr(m.p_uyum_s2, 2)} / {tr(m.p_uyum_s3, 2)} `[H]`. Kural: {V.va.mense_kurali.get(kod, '—')}.",
              f"- EUDR kapsamındaki AB ihracatı payı: {yuzde(ab.get('eudr_payi', 0))}; SKDM: {yuzde(ab.get('skdm_payi', 0))}."]
    satir4 += [f"- {s}" for s in y.get("ab", [])]
    out += ["**4. AB tarafı maruziyet**", ""] + satir4 + [""]

    # 5 Türkiye tarafı
    tm = hb.w_mfn / hb.m_toplam_musd if hb.notna().any() and hb.m_toplam_musd > 0 else np.nan
    tt = hb.w_tam / hb.m_toplam_musd if hb.notna().any() and hb.m_toplam_musd > 0 else np.nan
    satir5 = [f"- Uygulanan tarife (2026, ithalat ağırlıklı): MFN {yuzde(tm / 100, 1)}, İGV dahil {yuzde(tt / 100, 1)} `[V]`. "
              f"S4'te AB menşeline (c2): {yuzde(m.tau_tr_c2 / 100, 1)}."]
    if y.get("girdi_hs4"):
        satir5.append(f"- Kritik girdiler (HS4 {', '.join(y['girdi_hs4'])}), Türkiye'nin toplam ithalatı 2024: "
                      f"{V.girdi(y['girdi_hs4'])} `[V]`.")
    satir5 += [f"- {s}" for s in y.get("tr", [])]
    out += ["**5. Türkiye tarafı maruziyet**", ""] + satir5 + [""]

    # 6 Kabiliyet
    atl = V.p.atlanabilir_urunler.get(kod)
    satir6 = [f"- KS {tr(m.ks, 1)} (sıra {tr(m.ks_sira)}/230; ağırlık duyarlılığında P10–P90 {tr(m.ks_sira_p10)}–"
              f"{tr(m.ks_sira_p90)}). Bileşenler: RCA {tr(m.ks_rca)}, PCI {tr(m.ks_pci)} (PCI {tr(m.pci, 2)}), yurt içi KD "
              f"{tr(m.ks_kd)}, Ar-Ge {tr(m.ks_arge)}, tedarikçi {tr(m.ks_tedarik)}, verimlilik {tr(m.ks_verim)}, firma "
              f"{tr(m.ks_firma)} `[T]`.",
              f"- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): "
              f"{atl if isinstance(atl, str) and atl else 'yok'} `[T]`."]
    satir6 += [f"- **Kırmızı çizgi yetkinlikleri:** {y['kirmizi']}" if y.get("kirmizi") else None,
               f"- **Geliştirme hedefi:** {y['hedef']}" if y.get("hedef") else None]
    out += ["**6. Kabiliyet**", ""] + [s for s in satir6 if s] + [""]

    # 7 Stratejik önem
    out += [f"**7. Stratejik önem.** SS {tr(m.ss, 1)} (en yüksek boyut: {m.ss_max_boyut} {tr(m.ss_max)}; ağırlıklı ortalama "
            f"{tr(m.ss_ort, 1)}) `[H]`. {y.get('ss', m.ss_gerekce if isinstance(m.ss_gerekce, str) else '')}", ""]

    # 8 Makro
    satir = [["TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay",
              f"%{tr(m.tufe_agirlik_yuzde, 2)}; {yuzde(m.ithalat_payi)}"],
             ["ÜFE vekili (imalat üretimindeki pay)", yuzde(yy.get("uretim_musd", np.nan) / V.y.uretim_musd[
                 V.y.index.str.match(r"^(1\d|2\d|3[0-3])\.")].sum(), 2)],
             ["EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1)", f"{tr(m.ede_tum_bp, 3)} / {tr(m.ede_ab_bp, 3)}"],
             ["Geçişkenlik ρ (senaryolarda)", y.get("rho", "0,6–1,0 (P50 0,8)")],
             ["Piyasa yoğunlaşması (250+ istihdam payı)", yuzde(yy.get("buyuk_isletme_istihdam_payi"))],
             ["CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan",
              f"{tr(m.cke_tufe_musd_bp, 1)} ve {tr(m.cke_mali_musd_mlrtl, 2)}; {tr(m.cke_puan)}"]]
    out += [tablo("8. Makro duyarlılık", ["Gösterge", "Değer (`[T]`)"], satir)]

    # 9 Senaryolar
    satir = []
    for dg, ad, nd in (("dx_ab", "AB'ye ihracat ($ mn)", 0), ("dx", "Toplam ihracat ($ mn)", 0),
                       ("dm", "Nihai mal ithalatı ($ mn)", 0), ("dca", "Cari denge ($ mn)", 0),
                       ("dq", "Üretim ($ mn)", 0), ("dl", "İstihdam (kişi)", 0), ("dtufe", "TÜFE (bp, birinci tur)", 2)):
        h_ = [ad]
        for sc in SEN:
            r = V.senaryo(kod, dg, sc)
            h_.append("—" if r is None else f"{tr(r.p50, nd, True)} ({tr(r.p10, nd, True)} / {tr(r.p90, nd, True)})")
        satir.append(h_)
    satir.append(["Yatırım ve DYY (bütün senaryolar)", y.get("yatirim", "—"), "", ""])
    out += [tablo("9. Senaryo etkileri, T+5, P50 (P10 / P90)", ["Değişken", "S2", "S3", "S4"], satir,
                  "`[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.")]

    # 10 Politika paketi
    ey = y.get("eylemler", [])
    if ey:
        satir = [[f"E-{kod}-{i + 1:02d}", e[0], e[1], e[2], e[3], e[4], f"{e[5]}; sunset: {e[7]}", e[6], e[8]]
                 for i, e in enumerate(ey)]
        out += [tablo("10. Politika paketi", ["Eylem ID", "Araç", "Parametre", "Sorumlu", "Hukuki araç", "Bütçe",
                                              "Başlangıç–bitiş; sunset", "Performans koşulu", "KPI"], satir)]
    # 11–15
    for no, an, ad in ((11, "muzakere", "Müzakere pozisyonu"), (12, None, None), (13, "kazanan", "Kazanan ve kaybedenler; "
                                                                                     "bölgesel ve sosyal etki; telafi"),
                       (14, "riskler", "Riskler ve azaltım"), (15, "guven", "Güven düzeyi; veri boşlukları; `[D?]`")):
        if no == 12:
            tt_ = y.get("tetikler", [])
            if tt_:
                out += [tablo("12. Erken uyarı ve tetikler", ["Gösterge", "Eşik", "Tetiklenecek önlem"], tt_)]
            continue
        deg = y.get(an)
        if not deg:
            continue
        if isinstance(deg, list):
            out += [f"**{no}. {ad}**", ""] + [f"- {s}" for s in deg] + [""]
        else:
            out += [f"**{no}. {ad}.** {deg}", ""]
    if not y.get("guven"):
        out += [f"**15. Güven düzeyi.** {m.guven}.", ""]
    return "\n".join(out)


def matris_satirlari(V, kodlar):
    m = V.m.loc[kodlar]
    a = [[kd, V.k.ad_tr[kd][:38], r.gb_statusu, tr(r.kd_musd), tr(r.l), tr(r.x), yuzde(r.ab_ihracat_payi), tr(r.m),
          yuzde(r.ab_ithalat_payi), f"%{tr(r.tau_ab_s4, 1)}", r.mense_riski, yuzde(r.m_x), tr(r.rca_dunya_2024, 2),
          tr(r.pci, 2)] for kd, r in m.iterrows()]
    b = [[kd, tr(r.ks), tr(r.ss), tr(r.ame_puan), tr(r.ede_tum_bp, 2), tr(r.cke_puan),
          "/".join(x for x in [r.arketip_birincil, r.arketip_ikincil] if isinstance(x, str) and x), r.durus, r.tarife_yolu,
          r.ana_araclar, r.ab_muzakere, tr(r.s2_ca_musd_p50, 1, True), tr(r.s2_tufe_bp_p50, 2), r.istihdam_riski, r.guven]
         for kd, r in m.iterrows()]
    return a, b


def toplamlar(Y):
    t = {k: 0.0 for k in ("tufe_s2", "tufe_s4", "mali_s2", "mali_s4", "ca_s2", "ca_s4")}
    for kayit in list((Y.get("siniflar") or {}).values()) + list((Y["belge"].get("defter_ortak") or {}).values()):
        for k in t:
            t[k] += float(((kayit or {}).get("defter", kayit) or {}).get(k, 0) or 0)
    return t


def defter(V, kodlar, Y):
    """Kümülatif defter (ana prompt 2.6): tamamlanan kartların toplamı."""
    m, k = V.m.loc[kodlar], V.k
    t = toplamlar(Y)
    usd_try = float(V.mk.usd_try_2026.iloc[0])
    gsyh = float(pd.read_csv(os.path.join(V.veri, "teshis_odemeler_dengesi.csv"), index_col=0).loc[2025, "gsyh_musd"])
    gs = lambda mlr_tl: 100 * mlr_tl * 1e3 / usd_try / gsyh  # noqa: E731
    sok = {sc: m[f"{sc}_tufe_bp_p50"].sum() for sc in ("s2", "s4")}
    c_toplam, diger = int((k.kapsam_grubu == "C").sum()), int((k.kapsam_grubu != "C").sum())
    asan = m[m.s4_istihdam_pay_p10 <= -0.05]
    satir = [
        ["Tamamlanan / kalan sınıf", f"{len(kodlar)} / {c_toplam - len(kodlar)} C sınıfı; ek kapsam (B, D, E, hizmet) 0 / {diger}"],
        ["Kullanılan / kalan enflasyon bütçesi (bp; birinci tur, P50)",
         f"S2 yolu: şok {tr(sok['s2'], 1)} + önlem {tr(t['tufe_s2'], 2, True)} = {tr(sok['s2'] + t['tufe_s2'], 1)} bp; "
         f"S4 yolu: şok {tr(sok['s4'], 1)} + önlem {tr(t['tufe_s4'], 2, True)} = {tr(sok['s4'] + t['tufe_s4'], 1)} bp. "
         f"Kümülatif 50 bp bütçeden kalan: S2 {tr(50 - sok['s2'] - t['tufe_s2'], 1)}, S4 {tr(50 - sok['s4'] - t['tufe_s4'], 1)} bp"],
        ["Kümülatif cari denge katkısı ($ mlr/yıl, T+5)",
         f"Senaryo P50: S2 {tr(m.s2_ca_musd_p50.sum() / 1e3, 3, True)}, S4 {tr(m.s4_ca_musd_p50.sum() / 1e3, 3, True)} "
         f"(S4 P10 {tr(m.s4_ca_musd_p10.sum() / 1e3, 2, True)}); önlemler: S2 {tr(t['ca_s2'] / 1e3, 3, True)}, "
         f"S4 {tr(t['ca_s4'] / 1e3, 3, True)} `[T]`/`[H]`"],
        ["Kümülatif mali maliyet (mlr TL/yıl; GSYH %)",
         f"S2 yolu {tr(t['mali_s2'], 2)} (%{tr(gs(t['mali_s2']), 3)}); S4 yolu {tr(t['mali_s4'], 2)} (%{tr(gs(t['mali_s4']), 3)})"],
        ["Riskteki istihdam (kişi, T+5)",
         f"S2 P50 {tr(m.s2_istihdam_p50.sum(), 0, True)}; S4 P50 {tr(m.s4_istihdam_p50.sum(), 0, True)}, P10 "
         f"{tr(m.s4_istihdam_p10.sum(), 0, True)}. S4 P10'da kaybı %5'i aşan sınıf: "
         + (", ".join(f"{kd} ({yuzde(r.s4_istihdam_pay_p10, 1)})" for kd, r in asan.iterrows()) or "yok")],
        ["Açık kalan veri boşlukları", "; ".join(Y["belge"].get("veri_bosluklari", []))],
        ["Varsayım kaydına eklenen yeni maddeler", "; ".join(Y["belge"].get("varsayimlar", []))],
    ]
    return tablo("Tablo 5.1 — Kümülatif defter (Faz 3, parça 1 sonrası)", ["Kalem", "Değer"], satir,
                 "Bu tablo `kod/f3g_kartlar.py` ile matristen ve kartlardaki önlem kayıtlarından üretildi. Senaryo şokları "
                 "politika seçimi değil, çıkışın kendisi; önlemler kartların eylem tablolarından. Makro mutabakat Faz 6'da.")


def ilerleme(V, kodlar, Y):
    c_toplam = int((V.k.kapsam_grubu == "C").sum())
    return (f"İLERLEME: Faz 3 parça 1 / 16 tamamlandı ({len(kodlar)} / {c_toplam} C sınıfı kartı) — SONRAKİ ADIM: "
            f"{Y['belge'].get('sonraki', 'Faz 3 parça 2 (13–15: tekstil, giyim, deri)')}; DEVAM bekleniyor.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--yaml", required=True, action="append", help="birden çok verilebilir; sırayla birleştirilir")
    ap.add_argument("--cikti", required=True)
    ap.add_argument("--cache", default=yollar.GIRDI)
    ap.add_argument("--out", default=yollar.VERI)
    a = ap.parse_args()
    Y = {"belge": {}, "siniflar": {}, "bolumler": {}}
    for yol in a.yaml:
        y_ = yaml.safe_load(open(yol, encoding="utf-8")) or {}
        for anahtar in Y:
            Y[anahtar].update(y_.get(anahtar) or {})
    V = Veri(a.out, a.cache)
    Y = doldur_hepsi(Y, V.m)
    kodlar = [k for k in V.m.index if k[:2] in Y["bolumler"]]
    parca = [Y["belge"]["baslik"], "", Y["belge"]["giris"].strip(), ""]
    for blok in Y["belge"].get("on_bolumler", []):
        parca += [blok.strip(), ""]
    # bölüm özeti
    satir = []
    for bl, ad in Y["bolumler"].items():
        g = V.m[V.m.index.str[:2] == bl]
        s4 = lambda c: g[c].sum()  # noqa: E731
        satir.append([f"{bl} {ad}", len(g), tr(g.l.sum()), tr(g.kd_musd.sum()), tr(g.x.sum()), yuzde(g.x_ab.sum() / g.x.sum()),
                      tr(g.m.sum()), tr(g.x.sum() - g.m.sum(), isaret=True), tr(s4("s2_ca_musd_p50"), 0, True),
                      tr(s4("s4_ca_musd_p50"), 0, True), tr(s4("s4_istihdam_p50"), 0, True), tr(s4("s4_istihdam_p10"), 0, True),
                      tr(s4("s4_tufe_bp_p50"), 1)])
    parca += [tablo("Tablo 1.1 — Bölümlerin genel görünümü (2024; senaryolar T+5)",
                    ["Bölüm", "Sınıf", "Çalışan", "KD ($ mn)", "İhracat ($ mn)", "AB payı", "İthalat ($ mn)", "Denge",
                     "S2 cari P50", "S4 cari P50", "S4 istihdam P50", "S4 istihdam P10", "S4 TÜFE P50 (bp)"], satir,
                    "`[V]` TÜİK YSHİ, BACI; senaryolar `[T]` (f3e). Cari denge ve TÜFE etkileri sınıf toplamıdır; makro "
                    "kanallar (kur, talep) Faz 6'da."), ""]
    for blok in Y["belge"].get("genel", []):
        parca += [blok.strip(), ""]
    ma, mb = matris_satirlari(V, kodlar)
    parca += [Y["belge"].get("matris_giris", "## 2. Ana matris satırları").strip(), "",
              tablo("Tablo 2.1a — Ana matris: kimlik, ticaret, maruziyet",
                    ["Kod", "Ad", "GB", "KD", "İstihdam", "İhracat", "AB payı", "İthalat", "AB ith. payı", "τ_AB (S4)",
                     "Menşe S2/S3", "İthal girdi", "RCA", "PCI"], ma,
                    "`veri/nace_matris.csv`. KD, ihracat, ithalat $ mn (2024). τ_AB: S4'te eklenen AB tarifesi (rota A)."), "",
              tablo("Tablo 2.1b — Ana matris: skorlar, strateji, senaryo",
                    ["Kod", "KS", "SS", "AME", "EDE", "CKE", "Arketip", "Duruş", "Tarife yolu", "Ana araçlar", "AB müz.",
                     "S2 cari P50", "S2 TÜFE P50", "İstihdam riski", "Güven"], mb,
                    "Skorlar 0–100 (C sınıfları içinde yüzdelik); EDE bp/puan; S2 cari $ mn; TÜFE bp. Arketip ve duruş "
                    "kural tabanlı öneri, uzman düzeltmesiyle (kartlar)."), ""]
    parca += [Y["belge"].get("kart_giris", "## 3. Sınıf kartları").strip(), ""]
    for i, kd in enumerate(kodlar):
        parca += [kart(V, kd, Y["siniflar"].get(kd), f"3.{i + 1}"), ""]
    for blok in Y["belge"].get("son_bolumler", []):
        blok = blok.replace("{{DEFTER}}", defter(V, kodlar, Y)).replace("{{ILERLEME}}", ilerleme(V, kodlar, Y))
        parca += [blok.strip(), ""]
    open(a.cikti, "w", encoding="utf-8").write("\n".join(parca).rstrip() + "\n")
    print(f"{a.cikti}: {len(kodlar)} kart; {sum(1 for k in kodlar if Y['siniflar'].get(k))} sınıfta nitel içerik")


if __name__ == "__main__":
    main()
