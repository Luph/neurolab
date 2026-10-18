"""Faz 3 — NACE bölüm belgesi (nace_kartlar_[bölüm].md): elle yazılmış metin, veriden doldurulan sayılar ve tablolar.

Belgenin metni kartlar/[bölüm]_metin/ altındaki Markdown şablonlarından gelir (dosya adı sırasıyla birleştirilir). Şablondaki
sayılar ve tablolar bu betikle veri/ tablolarından doldurulur; veri değişirse metindeki sayılar da değişir. Yapısal içerik
(eylem tabloları, tetikler, çapa yatırımcılar, kritik girdiler, uzman düzeltmeleri, defter kayıtları) kartlar/*.yaml'dan okunur.

Satır içi yer tutucular ({{...}}; bayraklar: abs, pct (×100), pctabs, isaret (+/−), bin (÷1.000)):
  {{kod|sütun|ondalık|bayrak...}}               veri/nace_matris.csv. kod: sınıf (10.39), bölüm (10), aralık (10-12), C
                                                 ya da virgüllü liste; grupta sütun toplamı
  {{t:kod|...}} {{y:..}} {{ab:..}} {{mk:..}} {{p:..}}   f3_ticaret_sinif, f3_yapi_sinif, f3_ab_tarife_sinif,
                                                 f3_makro_sinif, f3_pci_sinif (aynı söz dizimi)
  {{ort:tablo:kod|sütun|ağırlık|ondalık}}        ağırlıklı ortalama (tablo: m, t, y, ab, mk, p)
  {{oran:tablo:kod|pay_sütunu|payda_sütunu|ondalık}}   100 × Σpay ÷ Σpayda
  {{pay:tablo:kod|sütun|payda_kod|ondalık}}      100 × Σ(kod) ÷ Σ(payda_kod)
  {{g:grup:senaryo|değişken|p10/p50/p90|ondalık}}  f3_senaryo_grup (çekiliş toplamlarının yüzdeliği)
  {{aski:birim|değişken|sütun|ondalık}}          f3_senaryo_aski (S4, 1/98 askısına koşullu); sütun: aski_ort, aski_p10,
                                                 aski_p50, aski_p90, askisiz_ort, askisiz_p50, fark (aski_ort − askisiz_ort)
  {{askipay:birim|payda_birim|değişken|ondalık}}   askı farkındaki pay (%; ortalamalar toplanabilir)
  {{dunya:HS[+HS]|pay/sira/deger/ton_pay|ondalık}}  Türkiye'nin dünya ihracatındaki payı ve sırası (BACI 2024)
  {{ith:HS[+HS]|grup|ondalık}} {{ihr:...}}       Türkiye'nin 2024 ithalatı/ihracatı ($ mn); grup: top, ab, abpay, ISO3, ISO3pay
  {{kn8:önek|sütun|ondalık}}                     AB tarifesi, KN8 (TR→AB 2025 ağırlıklı ortalama; x_ab_meur için toplam)
  {{oz:senaryo|sütun|ondalık}}                   f3_senaryo_ozet (imalat geneli)
  {{ksd:ağırlık|sütun|ondalık}}                  f3_ks_duyarlilik (KS ağırlık duyarlılığı)
  {{say:kod[|sütun=değer]}}                      sınıf sayısı (isteğe bağlı koşulla, ör. durus=Koru)
  {{defter:[kod:]anahtar|ondalık}}              eylem kayıtlarının toplamı ya da tek sınıfın kaydı (tufe_s2, tufe_s4, mali_s2,
                                                 mali_s4, ca_s2, ca_s4); aski: için pay=sütun bayrağı: 100 × değer ÷ Σ sütun
  {{tufe_net:senaryo|ondalık}}                   parçanın TÜFE şoku (grup P50) + önlemler
  {{eylem:ortak}} {{eylem:sinif}} {{eylem:sinifsayisi}}   eylem sayıları (YAML)
Blok işaretleri (tek başına bir satır): {{TABLO:ad[:kodlar]|no[|n]}}, {{KUNYE:kod}}, {{VERI_SAYFALARI|harf}},
  {{DEFTER|no}}, {{ILERLEME}}. Tablo adları: ozet, bolum, rejim, aski, itu, tufe, durus, eylem_ortak, eylem_sinif, tetik,
  senaryo:kod, kucuk:kodlar, matris_a, matris_b, varsayim, vb.

Kullanım: python3 f3g_kartlar.py --yaml ../kartlar/10-12.yaml --yaml ../kartlar/10-12_siniflar.yaml \\
            --metin ../kartlar/10-12_metin --cikti ../nace_kartlar_10-12.md
"""

import argparse
import glob
import os
import re

import numpy as np
import pandas as pd
import yaml

import f3a_ticaret as f3a
import yollar

SEN = ("S2", "S3", "S4")
ARKETIP = {"A": "AB'ye entegre ihracat şampiyonu", "B": "küresel rekabetçi, AB bağımlılığı düşük",
           "C": "ithalata bağımlı, yerlileştirme potansiyeli", "D": "stratejik / güvenlik kritik",
           "E": "kabiliyet düşük, ithalat zorunlu", "F": "emek yoğun, rekabet gücü zayıflayan",
           "G": "SKDM ve Yeşil Mutabakat maruz", "H": "hizmet ve lojistik bağlantılı", "—": "belirgin arketip yok"}
SATIR_ICI = re.compile(r"\{\{([^{}]+?)\}\}")
BLOK = re.compile(r"^\{\{(TABLO:[^{}]+|KUNYE:[^{}]+|VERI_SAYFALARI[^{}]*|DEFTER[^{}]*|ILERLEME)\}\}$", re.M)


def tr(x, nd=0, isaret=False):
    """Türkçe sayı biçimi: binlik nokta, ondalık virgül, eksi işareti U+2212."""
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "—"
    if round(x, nd) == 0:
        x, isaret = 0.0, False            # "−0" ve "+0" yerine "0"
    s = f"{x:+,.{nd}f}" if isaret else f"{x:,.{nd}f}"
    s = s.replace(",", "§").replace(".", ",").replace("§", ".")
    return s.replace("-", "−")


def bicim(x, nd, bayrak=()):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "—"
    x = float(x)
    if "abs" in bayrak or "pctabs" in bayrak:
        x = abs(x)
    if "pct" in bayrak or "pctabs" in bayrak:
        x = 100 * x
    if "bin" in bayrak:
        x = x / 1000
    return tr(x, nd, "isaret" in bayrak)


def yuzde(x, nd=0):
    """Yüzde biçimi; eksi işareti yüzde imgesinin önünde (−%4,5)."""
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "—"
    v = 100 * float(x)
    return f"−%{tr(-v, nd)}" if round(v, nd) < 0 else f"%{tr(abs(v) if round(v, nd) == 0 else v, nd)}"


def hucre(s):
    return str(s).replace("|", "/").replace("\n", " ")


def tablo(baslik, sutunlar, satirlar, kaynak=None):
    out = [f"**{baslik}**", "", "| " + " | ".join(sutunlar) + " |", "|" + "---|" * len(sutunlar)]
    out += ["| " + " | ".join(hucre(c) for c in r) + " |" for r in satirlar]
    if kaynak:
        out += ["", f"*Kaynak:* {kaynak}"]
    return "\n".join(out)


def kalin(r):
    return [f"**{c}**" if c not in ("", "—") else c for c in r]


class Veri:
    def __init__(self, v):
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
        self.sn = oku("f3_senaryo_sinif.csv", dtype={"kod": str}).set_index(["kod", "senaryo", "degisken"])
        self.g = oku("f3_senaryo_grup.csv", dtype={"grup": str}).set_index(["grup", "senaryo", "degisken"])
        self.aski = oku("f3_senaryo_aski.csv", dtype={"birim": str}).set_index(["birim", "degisken"])
        self.oz = oku("f3_senaryo_ozet.csv").set_index("senaryo")
        self.ksd = oku("f3_ks_duyarlilik.csv").set_index("agirlik")
        self.k = oku("nace_kapsam.csv", dtype={"kod": str}).set_index("kod")
        self.va = oku("f3_sinif_varsayim.csv", dtype={"kod": str}).set_index("kod")
        self.kn8 = oku("f3_ab_tarife_kn8.csv", dtype={"cn8": str, "nace2": str})
        self.ulke = oku("ulke_adlari_tr.csv").set_index("iso3").ad_tr.to_dict()
        self.tab = {"m": self.m, "t": self.t, "y": self.y, "ab": self.ab, "mk": self.mk, "p": self.p}
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
        bt.loc[bt.partner_iso3.eq("CYP"), "eu27"] = 0          # KKTC ticareti AB dışı (D-2; f3a ile aynı)
        self.bt = bt
        x = bt[bt.flow == "X"].groupby("hs6", as_index=False).value_kusd.sum()
        xn, _ = f3a.nace_dagit(x.assign(hs4=x.hs6.str[:4]).rename(columns={"value_kusd": "v"}), ag, ["v"], ["hs4"])
        self.hs4 = xn
        d = pd.read_csv(yollar.girdi("baci", "baci_hs17_world_exports_exporter_hs6_2024.csv.gz"), dtype={"hs6": str})
        d["hs6"] = d.hs6.str.zfill(6)
        self.d = d

    # --- seçim ve yer tutucular ---------------------------------------------------------------------------------------
    def c_kodlari(self, idx):
        return [k for k in idx if self.k.kapsam_grubu.get(k) == "C"]

    def secim(self, df, grup):
        if grup in df.index:
            return [grup]
        if re.fullmatch(r"\d\d\.\d\d", grup):
            return []
        c = self.c_kodlari(df.index)
        if grup == "C":
            return c
        if re.fullmatch(r"\d\d-\d\d", grup):
            a, b = grup.split("-")
            return [k for k in c if a <= k[:2] <= b]
        if re.fullmatch(r"\d\d", grup):
            return [k for k in c if k[:2] == grup]
        if "," in grup:
            return [k for k in grup.split(",") if k in df.index]
        raise KeyError(f"tanımsız grup: {grup}")

    def hs_sec(self, df, kodlar):
        kod = kodlar.split("+")
        return df[df.hs6.isin([k for k in kod if len(k) == 6]) | df.hs6.str[:4].isin([k for k in kod if len(k) == 4])]

    def dunya(self, kodlar, ne):
        s = self.hs_sec(self.d, kodlar)
        g = s.groupby("exporter_iso3")["qty_tonnes" if ne == "ton_pay" else "value_kusd"].sum().sort_values(ascending=False)
        t = float(g.get("TUR", 0.0))
        if ne in ("pay", "ton_pay"):
            return 100 * t / g.sum()
        if ne == "sira":
            return float(list(g.index).index("TUR") + 1) if "TUR" in g.index else np.nan
        if ne == "deger":
            return t / 1e3
        raise KeyError(ne)

    def ticaret(self, akim, kodlar, grup):
        b = self.hs_sec(self.bt[self.bt.flow.eq("M" if akim == "ith" else "X")], kodlar)
        top = b.value_kusd.sum() / 1e3
        if grup == "top":
            return top
        v = (b[b.eu27 == 1] if grup.startswith("ab") else b[b.partner_iso3 == grup[:3]]).value_kusd.sum() / 1e3
        return 100 * v / top if grup.endswith("pay") else v

    def kn8_deger(self, onek, sut):
        k = self.kn8[self.kn8.cn8.str.startswith(onek)]
        if sut in ("x_ab_meur", "q_100kg"):
            return k[sut].sum()
        x = k.mfn_ave.fillna(k.adval) if sut == "mfn_ave" else k[sut]
        w = k.x_ab_meur.where(x.notna(), 0)
        return (x.fillna(0) * w).sum() / w.sum() if w.sum() > 0 else (x.mean() if len(x) else np.nan)

    def aski_deger(self, birim, dg, sut):
        r = self.aski.loc[(birim, dg)]
        return r.aski_ort - r.askisiz_ort if sut == "fark" else r[sut]

    def deger(self, govde):
        p = govde.split("|")
        bas = p[0]
        if bas.startswith("ort:"):
            _, tab, grup = bas.split(":", 2)
            df = self.tab[tab]
            s = self.secim(df, grup)
            x, w = df.loc[s, p[1]].astype(float), df.loc[s, p[2]].astype(float)
            ok = x.notna() & w.notna()
            return bicim((x[ok] * w[ok]).sum() / w[ok].sum() if w[ok].sum() else np.nan, int(p[3]), p[4:])
        if bas.startswith("oran:"):
            _, tab, grup = bas.split(":", 2)
            df = self.tab[tab]
            s = self.secim(df, grup)
            return bicim(100 * df.loc[s, p[1]].sum() / df.loc[s, p[2]].sum(), int(p[3]), p[4:])
        if bas.startswith("pay:"):
            _, tab, grup = bas.split(":", 2)
            df = self.tab[tab]
            v = 100 * df.loc[self.secim(df, grup), p[1]].sum() / df.loc[self.secim(df, p[2]), p[1]].sum()
            return bicim(v, int(p[3]), p[4:])
        if bas.startswith("g:"):
            _, grup, sc = bas.split(":")
            return bicim(self.g.loc[(grup, sc, p[1]), p[2]], int(p[3]), p[4:])
        if bas.startswith("aski:"):
            v, bay = self.aski_deger(bas[5:], p[1], p[2]), [b for b in p[4:] if not b.startswith("pay=")]
            for b in p[4:]:
                if b.startswith("pay="):          # 100 × değer ÷ Σ matris sütunu (ör. pay=l: istihdamdaki pay)
                    v = 100 * v / self.m.loc[self.secim(self.m, bas[5:]), b[4:]].sum()
            return bicim(v, int(p[3]), bay)
        if bas.startswith("askipay:"):
            v = 100 * self.aski_deger(bas[8:], p[2], "fark") / self.aski_deger(p[1], p[2], "fark")
            return bicim(v, int(p[3]), p[4:])
        if bas.startswith("dunya:"):
            return bicim(self.dunya(bas[6:], p[1]), int(p[2]), p[3:])
        if bas.startswith(("ith:", "ihr:")):
            return bicim(self.ticaret(bas[:3], bas[4:], p[1]), int(p[2]), p[3:])
        if bas.startswith("kn8:"):
            return bicim(self.kn8_deger(bas[4:], p[1]), int(p[2]), p[3:])
        if bas.startswith("oz:"):
            return bicim(self.oz.at[bas[3:], p[1]], int(p[2]), p[3:])
        if bas.startswith("ksd:"):               # KS ağırlık duyarlılığı (f3_ks_duyarlilik.csv)
            return bicim(self.ksd.at[bas[4:], p[1]], int(p[2]), p[3:])
        if bas.startswith("say:"):
            s = self.secim(self.m, bas[4:])
            if len(p) > 1:
                sut, deg = p[1].split("=", 1)
                s = [k for k in s if str(self.m.at[k, sut]) == deg]
            return str(len(s))
        if bas.startswith("defter:"):
            a = bas[7:].split(":")
            if len(a) == 2:                       # defter:kod:anahtar — tek sınıfın eylem kaydı
                return bicim(float(((self.Y["siniflar"].get(a[0]) or {}).get("defter") or {}).get(a[1], 0) or 0), int(p[1]), p[2:])
            return bicim(toplamlar(self.Y)[a[0]], int(p[1]), p[2:])
        if bas.startswith("eylem:"):              # eylem:ortak, eylem:sinif, eylem:sinifsayisi
            e = {k: (v or {}).get("eylemler", []) for k, v in self.Y["siniflar"].items()}
            return str({"ortak": len(self.Y["belge"].get("ortak_eylemler", [])), "sinif": sum(len(x) for x in e.values()),
                        "sinifsayisi": sum(1 for x in e.values() if x)}[bas[6:]])
        if bas.startswith("tufe_net:"):
            sc = bas[9:]
            v = self.g.loc[(self.grup, sc, "dtufe")].p50 + toplamlar(self.Y)[f"tufe_{sc.lower()}"]
            return bicim(v, int(p[1]), p[2:])
        tab, grup = bas.split(":", 1) if ":" in bas else ("m", bas)
        df = self.tab[tab]
        if re.fullmatch(r"\d\d\.\d\d", grup):
            v = df[p[1]].get(grup, np.nan)
            if isinstance(v, str):
                return v
        else:
            v = df.loc[self.secim(df, grup), p[1]].sum()
        return bicim(v, int(p[2]), p[3:])

    def doldur(self, metin):
        def bir(mt):
            try:
                return self.deger(mt.group(1))
            except Exception as e:  # noqa: BLE001 — şablon hatası açıkça bildirilsin
                raise ValueError(f"yer tutucu çözülemedi: {{{{{mt.group(1)}}}}} ({e!r})") from e
        return SATIR_ICI.sub(bir, metin)

    # --- yardımcılar ---------------------------------------------------------------------------------------------------
    def ad(self, kod, Y=None):
        kisa = ((Y or {}).get("siniflar", {}).get(kod) or {}).get("kisa")
        return f"{kod} {kisa or self.k.ad_tr[kod]}"

    def ulke_adi(self, iso):
        return self.ulke.get(iso, iso)

    def sn_deger(self, kod, sc, dg):
        try:
            return self.sn.loc[(kod, sc, dg)]
        except KeyError:
            return None

    def tepe(self, kod):
        k = self.kn8[(self.kn8.nace2 == kod) & (self.kn8.artis_s4 >= 10)].sort_values("x_ab_meur", ascending=False)
        pay = k.x_ab_meur.sum() / max(self.kn8[self.kn8.nace2 == kod].x_ab_meur.sum(), 1e-9)
        if k.empty or (pay < 0.01 and k.x_ab_meur.sum() < 1):
            return "yok (AB'ye ihracatın %1'inden az)" if not k.empty else "yok"
        ilk = "; ".join(f"KN {r.cn8[:4]} {r.cn8[4:6]} {r.cn8[6:]} %{tr(r.artis_s4, 1)} (€{tr(r.x_ab_meur, 1)} mn)"
                        for r in k.head(3).itertuples())
        return f"{len(k)} satır, AB'ye ihracatın {yuzde(pay)}'i: {ilk}"

    def girdi(self, kodlar):
        """Kritik girdi HS4 listesi: Türkiye'nin 2024 ithalatı, AB payı ve ilk üç kaynak."""
        m = self.bt[(self.bt.flow == "M") & self.bt.hs6.str[:4].isin(kodlar)]
        if m.empty:
            return "—"
        top = m.value_kusd.sum() / 1e3
        k = m.groupby("partner_iso3").value_kusd.sum().sort_values(ascending=False) / 1e3
        ab = m[m.eu27 == 1].value_kusd.sum() / 1e3
        ilk = ", ".join(f"{self.ulke_adi(a)} {yuzde(v / top)}" for a, v in k.head(3).items())
        return f"${tr(top)} mn (AB {yuzde(ab / top)}; {ilk})"

    def ortaklar(self, kod, tur, tercih=False):
        o = self.o[(self.o.nace2 == kod) & (self.o.tur == tur)]
        return "; ".join(f"{self.ulke_adi(r.partner_iso3)} {yuzde(r.pay)}"
                         + (f" ({r.ab_tercihi})" if tercih and isinstance(r.ab_tercihi, str) else "")
                         for r in o.itertuples()) or "—"


# --- tablolar ----------------------------------------------------------------------------------------------------------
def senaryo_hucre(r, nd=0, olcek=1.0):
    if r is None:
        return "—"
    return f"{tr(r.p50 * olcek, nd, True)} ({tr(r.p10 * olcek, nd, True)} / {tr(r.p90 * olcek, nd, True)})"


def t_ozet(V, Y, kodlar, no, grup):
    t = toplamlar(Y)
    g = lambda sc, dg: V.g.loc[(grup, sc, dg)]  # noqa: E731
    satir = []
    for dg, ad_, nd in (("dx_ab", "AB'ye ihracat ($ mn)", 0), ("dl", "İstihdam (kişi)", 0),
                        ("dca", "Cari denge ($ mn)", 0), ("dtufe", "TÜFE, birinci tur (bp)", 1)):
        r2, r4 = g("S2", dg), g("S4", dg)
        isr = dg != "dtufe"
        ak = tr(V.aski.loc[(grup, dg)].aski_ort, nd, True) if isr else tr(r4.p50, nd)
        satir.append([ad_, tr(r2.p50, nd, isr), f"{tr(r2.p10, nd, isr)} / {tr(r2.p90, nd, isr)}", tr(r4.p50, nd, isr),
                      f"{tr(r4.p10, nd, isr)} / {tr(r4.p90, nd, isr)}", ak])
    s2, s4 = g("S2", "dtufe").p50, g("S4", "dtufe").p50
    satir.append(["TÜFE, önerilen önlemlerle (bp)", tr(s2 + t["tufe_s2"], 1), "—", tr(s4 + t["tufe_s4"], 1), "—",
                  tr(s4 + t["tufe_s4"], 1)])
    satir.append(["Önlemlerin mali maliyeti (mlr TL/yıl)", tr(t["mali_s2"], 2), "—", tr(t["mali_s4"], 2), "—",
                  tr(t["mali_s4"], 2)])
    return tablo(f"Tablo {no} — Çıkışın 10–12'ye etkisi (T+5'te yıllık; bugüne göre fark)",
                 ["Gösterge", "S2: P50", "S2: P10 / P90", "S4: P50", "S4: P10 / P90", "S4, 1/98 askıya alınırsa (ortalama)"],
                 satir, "`[T]` f3e Monte Carlo (N = 2.000; yüzdelikler bölüm toplamının dağılımından). S2: derin ve kapsamlı "
                        "STA; S4: anlaşmasız çıkış ve tek taraflı paket. Son sütun, AB'nin 1/98'i askıya aldığı çekilişlerin "
                        "ortalaması (olasılık 0,25 varsayıldı). Önlemler ve mali maliyet Bölüm 4'teki eylemlerden.")


def t_bolum(V, Y, kodlar, no):
    m, y = V.m, V.y
    c = V.c_kodlari(m.index)
    cy = V.c_kodlari(y.index)
    satir = []
    for bl, ad_ in list(Y["bolumler"].items()) + [("hepsi", "10–12 toplamı")]:
        s = [k for k in kodlar if bl == "hepsi" or k[:2] == bl]
        ys = [k for k in s if k in y.index]
        r = [f"{bl} {ad_}" if bl != "hepsi" else ad_, str(len(s)), tr(y.calisan[ys].sum() / 1e3, 1),
             tr(y.kd_musd[ys].sum() / 1e3, 2), tr(m.x[s].sum() / 1e3, 2), tr(m.x_ab[s].sum() / 1e3, 2),
             yuzde(m.x_ab[s].sum() / m.x[s].sum()), tr(m.m[s].sum() / 1e3, 2), tr((m.x[s].sum() - m.m[s].sum()) / 1e3, 2, True)]
        satir.append(kalin(r) if bl == "hepsi" else r)
    s = kodlar
    ys = [k for k in s if k in y.index]
    satir.append(["İmalat (C) içindeki payı", f"{len(s)} / {len(c)}", yuzde(y.calisan[ys].sum() / y.calisan[cy].sum(), 1),
                  yuzde(y.kd_musd[ys].sum() / y.kd_musd[cy].sum(), 1), yuzde(m.x[s].sum() / m.x[c].sum(), 1),
                  yuzde(m.x_ab[s].sum() / m.x_ab[c].sum(), 1), "—", yuzde(m.m[s].sum() / m.m[c].sum(), 1), "—"])
    return tablo(f"Tablo {no} — Bölümlerin büyüklüğü ve dış ticareti (2024)",
                 ["Bölüm", "Sınıf", "Çalışan (bin)", "Katma değer ($ mlr)", "İhracat ($ mlr)", "AB'ye ihracat ($ mlr)",
                  "AB payı", "İthalat ($ mlr)", "Denge ($ mlr)"], satir,
                 "TÜİK Yıllık Sanayi ve Hizmet İstatistikleri 2024 (çalışan, katma değer); BACI HS17 2024 (dış ticaret; "
                 "Kıbrıs akımları AB dışı, Ek D). `[V]`; HS6 → NACE eşlemesi `[T]`.")


def t_rejim(V, Y, kodlar, no):
    ab = V.ab
    satir = []
    gruplar = [(bl, f"{bl} {ad_}") for bl, ad_ in Y["bolumler"].items()] + [("hepsi", "10–12 toplamı"), ("C", "İmalat (C)")]
    for bl, ad_ in gruplar:
        s = V.c_kodlari(ab.index) if bl == "C" else [k for k in kodlar if (bl == "hepsi" or k[:2] == bl) and k in ab.index]
        w = ab.x_ab_meur_2025[s].fillna(0)
        o = lambda c: (ab[c][s].fillna(0) * w).sum() / w.sum()  # noqa: E731
        r = [ad_, tr(w.sum()), yuzde(o("pay_GB")), yuzde(o("pay_ITU")), yuzde(o("pay_TARIM")), f"%{tr(o('tau_ab_s4'), 1)}",
             f"%{tr(o('tau_ab_s4_tarim_kaybi'), 1)}"]
        satir.append(kalin(r) if bl == "hepsi" else r)
    return tablo(f"Tablo {no} — AB'ye ihracatın rejimlere dağılımı ve S4'te eklenecek AB tarifesi (2025)",
                 ["Bölüm", "AB'ye ihracat (€ mn)", "GB (sanayi)", "İTÜ", "Tarım (1/98)", "S4 tarifesi: 1/98 sürerse",
                  "S4 tarifesi: 1/98 askıdaysa"], satir,
                 "Eurostat Comext 2025 (TR→AB27, KN8), AB Kombine Nomenklatürü 2026; `kod/f3d_ab_tarife.py`. Tarifeler TR→AB "
                 "ihracatı ağırlıklı; spesifik vergiler ad valorem eşdeğerine çevrildi `[T]`. İTÜ satırında S4 artışı yalnız "
                 "sanayi bileşeni; tarım satırında 1/98 sürerse artış yok.")


def t_aski(V, Y, kodlar, no, grup, n=8):
    a, ab = V.aski, V.ab
    fark = {k: a.loc[(k, "dx_ab")].aski_ort - a.loc[(k, "dx_ab")].askisiz_ort for k in kodlar}
    sira = sorted(kodlar, key=lambda k: fark[k])[:n]
    satir = []
    for k in sira:
        x, l_ = a.loc[(k, "dx_ab")], a.loc[(k, "dl")]
        satir.append([V.ad(k, Y), tr(ab.x_ab_meur_2025.get(k, np.nan)), yuzde(ab.pay_TARIM.get(k, np.nan)),
                      f"%{tr(ab.tau_ab_s4_tarim_kaybi.get(k, np.nan), 1)}", tr(x.askisiz_ort, 0, True), tr(x.aski_ort, 0, True),
                      tr(l_.aski_ort, 0, True), yuzde(l_.aski_ort / V.m.l[k], 1) if V.m.l[k] > 0 else "—"])
    diger = [k for k in kodlar if k not in sira]
    ds = lambda dg, c: sum(a.loc[(k, dg)][c] for k in diger)  # noqa: E731
    satir.append([f"Diğer {len(diger)} sınıf", tr(ab.x_ab_meur_2025.reindex(diger).sum()), "—", "—",
                  tr(ds("dx_ab", "askisiz_ort"), 0, True), tr(ds("dx_ab", "aski_ort"), 0, True), tr(ds("dl", "aski_ort"), 0, True),
                  "—"])
    x, l_ = a.loc[(grup, "dx_ab")], a.loc[(grup, "dl")]
    satir.append(kalin(["10–12 toplamı", tr(ab.x_ab_meur_2025.reindex(kodlar).sum()), "—", "—", tr(x.askisiz_ort, 0, True),
                        tr(x.aski_ort, 0, True), tr(l_.aski_ort, 0, True), yuzde(l_.aski_ort / V.m.l[kodlar].sum(), 1)]))
    return tablo(f"Tablo {no} — S4'te 1/98'in askıya alınması: en çok etkilenen sınıflar (T+5)",
                 ["Sınıf", "AB'ye ihracat (€ mn, 2025)", "Tarım payı", "Askıda AB tarifesi", "AB'ye ihracat: askı yok ($ mn)",
                  "AB'ye ihracat: askıda ($ mn)", "İstihdam: askıda (kişi)", "İstihdamdaki pay"], satir,
                 "`[T]` f3e; S4 çekilişlerinin 1/98 askısına göre koşullu ortalaması (`veri/f3_senaryo_aski.csv`). Askıda AB "
                 "tarifesi: tarım satırlarına tam MFN (1/98 tercihleri satır düzeyinde bilinmediği için üst sınır, VB-06).")


def t_itu(V, Y, kodlar, no):
    m, ab = V.m, V.ab
    s = [k for k in kodlar if k in ab.index and (ab.pay_ITU.get(k, 0) + ab.pay_GB.get(k, 0)) >= 0.5
         and ab.x_ab_meur_2025.get(k, 0) >= 10 and ab.tau_ab_s4.get(k, 0) >= 1]
    s = sorted(s, key=lambda k: m.s4_ab_ihracat_musd_p50[k])
    satir = []
    for k in s:
        r2, r4 = m.s2_ab_ihracat_musd_p50[k], m.s4_ab_ihracat_musd_p50[k]
        satir.append([V.ad(k, Y), tr(ab.x_ab_meur_2025[k]), yuzde(ab.pay_ITU[k] + ab.pay_GB[k]), f"%{tr(ab.tau_ab_s4[k], 1)}",
                      m.mense_riski[k], tr(r2, 0, True), tr(r4, 0, True), yuzde(r2 / r4) if r4 < 0 else "—",
                      tr(m.s4_istihdam_p50[k], 0, True)])
    t2, t4 = m.s2_ab_ihracat_musd_p50[s].sum(), m.s4_ab_ihracat_musd_p50[s].sum()
    satir.append(kalin(["Toplam", tr(ab.x_ab_meur_2025[s].sum()), "—", "—", "—", tr(t2, 0, True), tr(t4, 0, True), yuzde(t2 / t4),
                        tr(m.s4_istihdam_p50[s].sum(), 0, True)]))
    return tablo(f"Tablo {no} — GB'ye bağlı sınıflar: S4'te sanayi bileşeni ve S2'de menşe (T+5, P50)",
                 ["Sınıf", "AB'ye ihracat (€ mn, 2025)", "GB ve İTÜ payı", "S4'te AB tarifesi", "Menşe riski S2/S3",
                  "AB'ye ihracat S2 ($ mn)", "AB'ye ihracat S4 ($ mn)", "S2 ÷ S4", "İstihdam S4 (kişi)"], satir,
                 "`[T]` f3d, f3e. Menşe riski D/O/Y: düşük, orta, yüksek (`veri/f3_sinif_varsayim.csv`, `[H]`). Seçim: AB'ye "
                 "ihracatının en az yarısı GB veya İTÜ rejiminde, €10 mn üzerinde ve S4'te AB tarifesi en az %1 olan sınıflar.")


def t_tufe(V, Y, kodlar, no, grup, n=8):
    m = V.m
    sira = sorted(kodlar, key=lambda k: -m.s4_tufe_bp_p50[k])[:n]
    onlem = {k: float(((Y["siniflar"].get(k) or {}).get("defter") or {}).get("tufe_s4", 0) or 0) for k in kodlar}
    satir = []
    for k in sira:
        satir.append([V.ad(k, Y), f"%{tr(m.tufe_agirlik_yuzde[k], 2)}", yuzde(m.ithalat_payi[k]), yuzde(m.ab_ithalat_payi[k]),
                      f"%{tr(m.tau_tr_c2[k], 1)}", tr(m.s2_tufe_bp_p50[k], 2), tr(m.s4_tufe_bp_p50[k], 2),
                      tr(onlem[k], 2, True) if onlem[k] else "—", tr(m.s4_tufe_bp_p50[k] + onlem[k], 2)])
    diger = [k for k in kodlar if k not in sira]
    od = sum(onlem[k] for k in diger)
    satir.append([f"Diğer {len(diger)} sınıf", f"%{tr(m.tufe_agirlik_yuzde[diger].sum(), 2)}", "—", "—", "—",
                  tr(m.s2_tufe_bp_p50[diger].sum(), 2), tr(m.s4_tufe_bp_p50[diger].sum(), 2), tr(od, 2, True) if od else "—",
                  tr(m.s4_tufe_bp_p50[diger].sum() + od, 2)])
    g2, g4 = V.g.loc[(grup, "S2", "dtufe")].p50, V.g.loc[(grup, "S4", "dtufe")].p50
    ot = sum(onlem.values())
    satir.append(kalin(["10–12 toplamı", f"%{tr(m.tufe_agirlik_yuzde[kodlar].sum(), 2)}", "—", "—", "—", tr(g2, 2), tr(g4, 2),
                        tr(ot, 2, True), tr(g4 + ot, 2)]))
    return tablo(f"Tablo {no} — İthalat tarafı: TÜFE'ye birinci tur etkisi en büyük sınıflar (bp, P50)",
                 ["Sınıf", "TÜFE ağırlığı", "Tüketimde ithal pay", "İthalatta AB payı", "S4'te AB'ye tarife (c2)", "S2",
                  "S4", "Önlem (S4)", "S4, önlemle"], satir,
                 "`[T]` f3e (doğrudan kanal COICOP 2018 sepeti, dolaylı kanal I-O 2023 Leontief fiyat modeli). c2: S4'te AB "
                 "menşeli mala uygulanacak MFN + İGV (İGV, AB'nin baskın, yerli üretimin zayıf olduğu satırlarda herkes için "
                 "kalkar; Faz 2A). Önlemler Tablo 4.3'te.")


def t_durus(V, Y, kodlar, no):
    m = V.m
    satir = []
    for d_ in ("Koru", "Geliştir", "Dönüştür", "Yönetilen uyum", "Serbestleştir"):
        s = [k for k in kodlar if m.durus[k] == d_]
        if not s:
            continue
        satir.append([d_, str(len(s)), ", ".join(s), tr(m.l[s].sum() / 1e3, 1), tr(m.x_ab[s].sum())])
    return tablo(f"Tablo {no} — Sınıfların duruşa göre dağılımı",
                 ["Duruş", "Sınıf", "Sınıflar", "Çalışan (bin)", "AB'ye ihracat ($ mn, 2024)"], satir,
                 "`veri/nace_matris.csv` (`durus`; kural tabanlı öneri ve uzman düzeltmesi, `uzman_duzeltmesi` sütunu).")


EYLEM_SUTUN = ["Eylem", "Araç", "Parametre", "Sorumlu", "Hukuki araç", "Bütçe", "Başlangıç → bitiş", "Performans koşulu",
               "Sunset", "KPI"]


def t_eylem_ortak(V, Y, kodlar, no):
    satir = [list(e) for e in Y["belge"].get("ortak_eylemler", [])]
    return tablo(f"Tablo {no} — Bölüm düzeyi ortak eylemler (10–12)", EYLEM_SUTUN, satir,
                 "Bütçeler `[T]`, 2026 fiyatlarıyla; kurumsal sorumluluk mevcut görev dağılımına göre. Mali yükler ve cari "
                 "denge katkıları defterde (Tablo 6.1) toplanıyor.")


def t_eylem_sinif(V, Y, kodlar, no):
    satir = []
    for k in kodlar:
        for i, e in enumerate((Y["siniflar"].get(k) or {}).get("eylemler", [])):
            satir.append([f"E-{k}-{i + 1:02d}"] + list(e))
    return tablo(f"Tablo {no} — Sınıf eylemleri", EYLEM_SUTUN, satir,
                 "Bütçeler `[T]`, 2026 fiyatlarıyla. Tarihler T'ye göre (T2028'de T = 1.1.2028, T2029'da 1.1.2029).")


def t_tetik(V, Y, kodlar, no):
    satir = [list(e) for e in Y["belge"].get("ortak_tetikler", [])]
    for k in kodlar:
        for e in (Y["siniflar"].get(k) or {}).get("tetikler", []):
            satir.append([k] + list(e))
    return tablo(f"Tablo {no} — Erken uyarı göstergeleri ve tetikler", ["Sınıf", "Gösterge", "Eşik", "Tetiklenecek önlem"],
                 satir, "Göstergeler aylık izlenir: TÜİK dış ticaret ve TÜFE alt endeksleri, Eurostat Comext, AB Resmî Gazetesi.")


def t_senaryo(V, Y, kod, no):
    m = V.m
    x_ab, l_ = m.x_ab[kod], m.l[kod]
    aski = (V.ab.pay_TARIM.get(kod, 0) or 0) >= 0.2
    satir = []
    for dg, ad_, nd, olc in (("dx_ab", "AB'ye ihracat ($ mn)", 0, 1.0),
                             ("dx_ab", "AB'ye ihracat (%)", 1, 100 / x_ab if x_ab else np.nan),
                             ("dx", "Toplam ihracat ($ mn)", 0, 1.0), ("dm", "Nihai mal ithalatı ($ mn)", 0, 1.0),
                             ("dq", "Üretim ($ mn)", 0, 1.0), ("dl", "İstihdam (kişi)", 0, 1.0),
                             ("dl", "İstihdam (%)", 1, 100 / l_ if l_ else np.nan), ("dca", "Cari denge ($ mn)", 0, 1.0),
                             ("dtufe", "TÜFE (bp)", 2, 1.0)):
        r = [ad_] + [senaryo_hucre(V.sn_deger(kod, sc, dg), nd, olc) if not np.isnan(olc) else "—" for sc in SEN]
        if aski:
            a = V.aski.loc[(kod, dg)].aski_ort if (kod, dg) in V.aski.index else np.nan
            r.append(tr(a * olc, nd, True) if not np.isnan(olc) and not np.isnan(a) else "—")
        satir.append(r)
    sut = ["Değişken", "S2", "S3", "S4"] + (["S4, 1/98 askıda (ort.)"] if aski else [])
    return tablo(f"Tablo {no} — {V.ad(kod, Y)}: senaryo etkileri (T+5'te yıllık; P50, parantez içinde P10 / P90)", sut, satir,
                 "`[T]` f3e; toplamlar Faz 2B genel denge dağılımına kalibre. Yüzdeler 2024 düzeyine göre.")


def t_kucuk(V, Y, kodlar, no):
    m, ab = V.m, V.ab
    satir = []
    for k in kodlar:
        aski = V.aski.loc[(k, "dx_ab")].aski_ort if (k, "dx_ab") in V.aski.index else np.nan
        satir.append([V.ad(k, Y), tr(m.l[k]), tr(m.x[k]), yuzde(m.ab_ihracat_payi[k]), m.gb_statusu[k],
                      f"%{tr(ab.tau_ab_s4.get(k, np.nan), 1)} / %{tr(ab.tau_ab_s4_tarim_kaybi.get(k, np.nan), 1)}",
                      tr(m.s4_ab_ihracat_musd_p50[k], 1, True), tr(aski, 1, True), tr(m.s4_tufe_bp_p50[k], 2)])
    return tablo(f"Tablo {no} — Etkisi sınırlı sınıflar: temel göstergeler",
                 ["Sınıf", "Çalışan", "İhracat ($ mn)", "AB payı", "GB statüsü", "S4 AB tarifesi: 1/98 sürer / askıda",
                  "AB'ye ihracat S4 P50 ($ mn)", "1/98 askıda (ort., $ mn)", "TÜFE S4 (bp)"], satir,
                 "TÜİK YSHİ 2024, BACI 2024 `[V]`; senaryolar `[T]` f3e. Veri sayfaları Ek C'de.")


def t_matris(V, Y, kodlar, no, parca):
    m = V.m.loc[kodlar]
    ark = lambda r: "/".join(x for x in [r.arketip_birincil, r.arketip_ikincil] if isinstance(x, str) and x)  # noqa: E731
    if parca == "a":
        satir = [[kd, (Y["siniflar"].get(kd) or {}).get("kisa", V.k.ad_tr[kd][:38]), r.gb_statusu, tr(r.kd_musd), tr(r.l),
                  tr(r.x), yuzde(r.ab_ihracat_payi), tr(r.m), yuzde(r.ab_ithalat_payi), f"%{tr(r.tau_ab_s4, 1)}", r.mense_riski,
                  yuzde(r.m_x), tr(r.rca_dunya_2024, 2), tr(r.pci, 2)] for kd, r in m.iterrows()]
        return tablo(f"Tablo {no} — Ana matris: kimlik, ticaret ve maruziyet",
                     ["Kod", "Ad", "GB statüsü", "KD", "İstihdam", "İhracat", "AB payı", "İthalat", "AB ithalat payı",
                      "τ_AB (S4)", "Menşe S2/S3", "İthal girdi", "RCA", "PCI"], satir,
                     "`veri/nace_matris.csv`. KD, ihracat ve ithalat $ mn (2024). τ_AB: S4'te eklenecek AB tarifesi (1/98 "
                     "sürer varsayımı).")
    satir = [[kd, tr(r.ks), tr(r.ss), tr(r.ame_puan), tr(r.ede_tum_bp, 2), tr(r.cke_puan), ark(r), r.durus, r.tarife_yolu,
              r.ana_araclar, r.ab_muzakere, tr(r.s2_ca_musd_p50, 1, True), tr(r.s2_tufe_bp_p50, 2), r.istihdam_riski, r.guven]
             for kd, r in m.iterrows()]
    return tablo(f"Tablo {no} — Ana matris: skorlar, strateji ve senaryo",
                 ["Kod", "KS", "SS", "AME", "EDE", "CKE", "Arketip", "Duruş", "Tarife yolu", "Ana araçlar", "AB müzakere",
                  "S2 cari P50", "S2 TÜFE P50", "İstihdam riski", "Güven"], satir,
                 "Skorlar 0–100 (C sınıfları içinde yüzdelik); EDE bp/puan; S2 cari denge $ mn; TÜFE bp. Arketip ve duruş "
                 "kural tabanlı öneri ve uzman düzeltmesi.")


def t_liste(baslik, sutunlar, ogeler):
    satir = [list(s.split(": ", 1)) if ": " in s else [s, ""] for s in ogeler]
    return tablo(baslik, sutunlar, satir)


def kunye(V, Y, kod, ek_no):
    m = V.m.loc[kod]
    ark = [a for a in [m.arketip_birincil, m.arketip_ikincil] if isinstance(a, str) and a]
    ark_s = " / ".join(f"{a} ({ARKETIP.get(a, '')})" for a in ark)
    return (f"*GB statüsü: {m.gb_statusu} · Arketip: {ark_s} · Duruş: {m.durus} · AB ile müzakere: {m.ab_muzakere} · "
            f"Güven: {m.guven} · Veri sayfası: Ek {ek_no}*")


def veri_sayfasi(V, Y, kod, no, senaryo_no=None):
    m, t, yy = V.m.loc[kod], V.t.reindex([kod]).iloc[0], V.y.reindex([kod]).iloc[0]
    k, mk = V.k.loc[kod], V.mk.loc[kod]
    ab = V.ab.reindex([kod]).iloc[0]
    va = V.va.reindex([kod]).iloc[0]
    y = Y["siniflar"].get(kod) or {}
    hs = V.hs4[V.hs4.nace2 == kod].sort_values("v", ascending=False)
    hs_top = hs.v.sum()
    fasil = ", ".join(f"{r.hs4} {yuzde(r.v / hs_top)}" for r in hs.head(4).itertuples()) if hs_top > 0 else "—"
    hb = V.h.reindex([kod]).iloc[0]
    bec = "—"
    if hb.notna().any() and hb.tic > 0:
        bec = f"{yuzde(hb.bec_ara / hb.tic)} / {yuzde(hb.bec_sermaye / hb.tic)} / {yuzde(hb.bec_tuketim / hb.tic)}"
    rev = f"{k.rev21} ({k.kopru_tipi})" if isinstance(k.rev21, str) else "—"
    bol = V.b[(V.b.kod == kod) & (V.b.sira <= 3)]
    bolge = "; ".join(f"{r.bolge} {yuzde(r.pay)}" for r in bol.itertuples()) or "—"
    olc = " / ".join(tr(yy.get(f"girisim_{g}")) for g in ("0", "1_9", "10_49", "50_249", "250p"))
    gizli = " (gizli hücre; bölüm kalanından tahmin `[T]`)" if yy.get("gizli_tahmin") is True else ""
    tm = hb.w_mfn / hb.m_toplam_musd if hb.notna().any() and hb.m_toplam_musd > 0 else np.nan
    tt = hb.w_tam / hb.m_toplam_musd if hb.notna().any() and hb.m_toplam_musd > 0 else np.nan
    atl = V.p.atlanabilir_urunler.get(kod)
    uretim_c = V.y.uretim_musd[V.c_kodlari(V.y.index)].sum()
    yn = lambda x: x if isinstance(x, str) and x else "—"  # noqa: E731
    satir = [
        ["1 Kimlik", "Rev. 2.1 karşılığı; CPA", f"{rev}; CPA {kod}"],
        ["", "Başlıca HS4 (ihracat, 2024)", fasil],
        ["", "BEC payları: ara / sermaye / tüketim", bec],
        ["2 Ölçek", "Üretim; katma değer (GSYH payı)", f"${tr(yy.get('uretim_musd'))} mn; ${tr(yy.get('kd_musd'))} mn "
                                                         f"({yuzde(yy.get('kd_gsyh_payi_yuzde', np.nan) / 100, 2)}){gizli}"],
        ["", "Çalışan; girişim", f"{tr(yy.get('calisan'))}; {tr(yy.get('girisim'))}"],
        ["", "Girişim ölçeği: 0 / 1–9 / 10–49 / 50–249 / 250+ çalışan", olc],
        ["", "250+ girişimlerin istihdam payı; kişi başı KD (AB27 = 1)",
         f"{yuzde(yy.get('buyuk_isletme_istihdam_payi'))}; {tr(yy.get('verimlilik_ab_orani'), 2)}"],
        ["", "İstihdam değişimi, 2015–2024", yuzde(yy.get("istihdam_degisimi_2015_2024_yuzde", np.nan) / 100)],
        ["", "İlk üç bölge (İBBS-2)", bolge],
        ["", "Çapa yatırımcılar", y.get("capa", "—")],
        ["3 Dış ticaret", "İhracat 2024; 2020–2024 değişimi", f"${tr(t.x_musd_2024)} mn; {yuzde(t.x_musd_degisim_yuzde / 100)}"],
        ["", "AB payı; ilk beş AB pazarı", f"{yuzde(t.ab_ihracat_payi_2024)}; {V.ortaklar(kod, 'AB pazarı')}"],
        ["", "İlk beş AB dışı pazar", V.ortaklar(kod, "AB dışı pazar")],
        ["", "İthalat 2024; AB ve Çin payı", f"${tr(t.m_musd_2024)} mn; AB {yuzde(t.ab_ithalat_payi_2024)}, Çin "
                                             f"{yuzde(t.cin_ithalat_payi_2024)}"],
        ["", "İlk beş ithalat kaynağı", V.ortaklar(kod, "İthalat kaynağı")],
        ["", "Dış ticaret dengesi", f"{'−' if t.denge_musd_2024 < 0 else '+'}${tr(abs(t.denge_musd_2024))} mn"],
        ["", "İthal girdi içeriği (I-O); KD ÷ üretim", f"{yuzde(mk.m_x)}; {yuzde(yy.get('kd_uretim_orani'))}"],
        ["", "RCA: dünya 2020 → 2024; AB pazarı 2024", f"{tr(t.rca_dunya_2020, 2)} → {tr(t.rca_dunya_2024, 2)}; "
                                                      f"{tr(t.rca_ab_2024, 2)}"],
        ["", "Birim değer ÷ AB pazarı ortalaması", tr(t.birim_deger_orani_2024, 2)],
        ["", "AB pazarındaki pay (AB dışı tedarik içinde) 2020 → 2024; Türkiye'nin sırası",
         f"{yuzde(t.ab_pazar_payi_abdisi_2020, 1)} → {yuzde(t.ab_pazar_payi_abdisi_2024, 1)}; {tr(t.ab_pazari_tr_sirasi_2024)}."],
        ["4 AB tarafı", "AB'ye ihracat 2025; rejim payları (GB / İTÜ / tarım)",
         f"€{tr(ab.get('x_ab_meur_2025', np.nan), 1)} mn; {yuzde(ab.get('pay_GB', np.nan))} / {yuzde(ab.get('pay_ITU', np.nan))} / "
         f"{yuzde(ab.get('pay_TARIM', np.nan))}"],
        ["", "S4'te AB tarifesi: 1/98 sürerse / askıda / tam MFN ortalaması",
         f"{yuzde(ab.get('tau_ab_s4', np.nan) / 100, 1)} / {yuzde(ab.get('tau_ab_s4_tarim_kaybi', np.nan) / 100, 1)} / "
         f"{yuzde(ab.get('tau_ab_mfn', np.nan) / 100, 1)}"],
        ["", "Tepe satırlar (S4 artışı ≥ %10)", V.tepe(kod)],
        ["", "AB pazarında AB dışı rakipler (AB tercihi)", V.ortaklar(kod, "AB pazarında rakip (AB dışı)", tercih=True)],
        ["", "Tercihli rakiplerin payı; AME (puan; ham)", f"{yuzde(t.tercihli_rakip_payi_2024)}; {tr(m.ame_puan)} "
                                                          f"({tr(m.ame_ham, 2)})"],
        ["", "Menşe kuralı (PEM)", yn(va.get("mense_kurali"))],
        ["", "Menşe riski S2 / S3; c_RoO (%); p_uyum", f"{m.mense_riski}; {tr(m.c_roo_s2, 1)} / {tr(m.c_roo_s3, 1)}; "
                                                       f"{tr(m.p_uyum_s2, 2)} / {tr(m.p_uyum_s3, 2)} `[H]`"],
        ["", "Değer zincirindeki rol; DİR bağımlılığı", f"{yn(va.get('deger_zinciri'))}; {yn(va.get('dir_bagimliligi'))}"],
        ["", "EUDR ve SKDM kapsamındaki AB'ye ihracat payı", f"{yuzde(ab.get('eudr_payi', 0))}; {yuzde(ab.get('skdm_payi', 0))}"],
        ["5 Türkiye tarafı", "Uygulanan tarife 2026 (ithalat ağırlıklı): MFN; İGV dahil",
         f"{yuzde(tm / 100, 1)}; {yuzde(tt / 100, 1)}"],
        ["", "S4'te AB menşeline tarife (c2)", yuzde(m.tau_tr_c2 / 100, 1)],
        ["", "Kritik girdiler: 2024 ithalatı, AB payı, ilk kaynaklar",
         f"HS4 {', '.join(y['girdi_hs4'])}: {V.girdi(y['girdi_hs4'])}" if y.get("girdi_hs4") else "—"],
        ["6 Kabiliyet", "KS; sıra (ağırlık duyarlılığında P10–P90)", f"{tr(m.ks, 1)}; {tr(m.ks_sira)} / 230 "
                                                                    f"({tr(m.ks_sira_p10)}–{tr(m.ks_sira_p90)})"],
        ["", "KS bileşenleri (yüzdelik): RCA, PCI, yurt içi KD, Ar-Ge, tedarikçi, verimlilik, firma",
         ", ".join(tr(m[c]) for c in ("ks_rca", "ks_pci", "ks_kd", "ks_arge", "ks_tedarik", "ks_verim", "ks_firma"))],
        ["", "PCI (sınıf)", tr(m.pci, 2)],
        ["", "Atlanabilir ürünler (yoğunluk üst çeyrek, PCI > sınıf)",
         re.sub(r"(\d)\.(\d)", r"\1,\2", atl).replace("-", "−") if isinstance(atl, str) and atl else "yok"],
        ["7 Stratejik önem", "SS; en yüksek boyut; ağırlıklı ortalama", f"{tr(m.ss, 1)}; {m.ss_max_boyut} {tr(m.ss_max)}; "
                                                                       f"{tr(m.ss_ort, 1)} `[H]`"],
        ["8 Makro duyarlılık", "TÜFE ağırlığı (doğrudan); tüketimde ithal pay", f"%{tr(m.tufe_agirlik_yuzde, 2)}; "
                                                                              f"{yuzde(m.ithalat_payi)}"],
        ["", "ÜFE vekili (imalat üretimindeki pay)", yuzde(yy.get("uretim_musd", np.nan) / uretim_c, 2)],
        ["", "EDE, 1 puan tarife: tüm menşeler / yalnız AB (bp; ρ = 1)", f"{tr(m.ede_tum_bp, 3)} / {tr(m.ede_ab_bp, 3)}"],
        ["", "CKE: tarife ($ mn / bp); mali ($ mn / mlr TL); puan", f"{tr(m.cke_tufe_musd_bp, 1)}; {tr(m.cke_mali_musd_mlrtl, 2)}; "
                                                                   f"{tr(m.cke_puan)}"],
        ["9 Senaryolar", "Senaryo tablosu", f"Tablo {senaryo_no}" if senaryo_no else f"Tablo {no}b (aşağıda)"],
    ]
    out = [f"### {no} {V.ad(kod)}", "", tablo(f"Tablo {no} — {kod}: veri sayfası", ["Alan", "Gösterge", "Değer"], satir)]
    if not senaryo_no:
        out += ["", t_senaryo(V, Y, kod, f"{no}b")]
    return "\n".join(out)


def toplamlar(Y):
    t = {k: 0.0 for k in ("tufe_s2", "tufe_s4", "mali_s2", "mali_s4", "ca_s2", "ca_s4")}
    for kayit in list((Y.get("siniflar") or {}).values()) + list((Y["belge"].get("defter_ortak") or {}).values()):
        for k in t:
            t[k] += float(((kayit or {}).get("defter", kayit) or {}).get(k, 0) or 0)
    return t


def defter(V, kodlar, Y, no, grup):
    """Kümülatif defter (ana prompt 2.6): tamamlanan sınıfların toplamı; yüzdelikler grup toplamının dağılımından."""
    m, k = V.m.loc[kodlar], V.k
    t = toplamlar(Y)
    g = lambda sc, dg: V.g.loc[(grup, sc, dg)]  # noqa: E731
    usd_try = float(V.mk.usd_try_2026.iloc[0])
    gsyh = float(pd.read_csv(os.path.join(V.veri, "teshis_odemeler_dengesi.csv"), index_col=0).loc[2025, "gsyh_musd"])
    gs = lambda mlr_tl: 100 * mlr_tl * 1e3 / usd_try / gsyh  # noqa: E731
    sok = {sc: g(sc.upper(), "dtufe").p50 for sc in ("s2", "s4")}
    c_toplam, diger = int((k.kapsam_grubu == "C").sum()), int((k.kapsam_grubu != "C").sum())
    asan = m[m.s4_istihdam_pay_p10 <= -0.05]
    satir = [
        ["Tamamlanan / kalan sınıf", f"{len(kodlar)} / {c_toplam - len(kodlar)} C sınıfı; ek kapsam (B, D, E, hizmet) 0 / {diger}"],
        ["Kullanılan / kalan enflasyon bütçesi (bp; birinci tur, P50)",
         f"S2 yolu: şok {tr(sok['s2'], 1)} + önlem {tr(t['tufe_s2'], 2, True)} = {tr(sok['s2'] + t['tufe_s2'], 1)} bp; "
         f"S4 yolu: şok {tr(sok['s4'], 1)} + önlem {tr(t['tufe_s4'], 2, True)} = {tr(sok['s4'] + t['tufe_s4'], 1)} bp. "
         f"Kümülatif 50 bp bütçeden kalan: S2 {tr(50 - sok['s2'] - t['tufe_s2'], 1)}, S4 {tr(50 - sok['s4'] - t['tufe_s4'], 1)} bp"],
        ["Kümülatif cari denge katkısı ($ mlr/yıl, T+5)",
         f"Senaryo P50: S2 {tr(g('S2', 'dca').p50 / 1e3, 3, True)}, S4 {tr(g('S4', 'dca').p50 / 1e3, 3, True)} "
         f"(S4 P10 {tr(g('S4', 'dca').p10 / 1e3, 2, True)}; 1/98 askısında ortalama "
         f"{tr(V.aski.loc[(grup, 'dca')].aski_ort / 1e3, 2, True)}); önlemler: S2 {tr(t['ca_s2'] / 1e3, 3, True)}, "
         f"S4 {tr(t['ca_s4'] / 1e3, 3, True)} `[T]`/`[H]`"],
        ["Kümülatif mali maliyet (mlr TL/yıl; GSYH %)",
         f"S2 yolu {tr(t['mali_s2'], 2)} (%{tr(gs(t['mali_s2']), 3)}); S4 yolu {tr(t['mali_s4'], 2)} (%{tr(gs(t['mali_s4']), 3)})"],
        ["Riskteki istihdam (kişi, T+5)",
         f"S2 P50 {tr(g('S2', 'dl').p50, 0, True)}; S4 P50 {tr(g('S4', 'dl').p50, 0, True)}, P10 {tr(g('S4', 'dl').p10, 0, True)}; "
         f"1/98 askısında ortalama {tr(V.aski.loc[(grup, 'dl')].aski_ort, 0, True)}. S4 P10'da kaybı %5'i aşan sınıf: "
         + (", ".join(f"{kd} ({yuzde(r.s4_istihdam_pay_p10, 1)})" for kd, r in asan.iterrows()) or "yok")],
        ["Açık kalan veri boşlukları", "; ".join(Y["belge"].get("veri_bosluklari", []))],
        ["Varsayım kaydına eklenen yeni maddeler", "; ".join(Y["belge"].get("varsayimlar", []))],
    ]
    return tablo(f"Tablo {no} — Kümülatif defter (Faz 3, parça 1 sonrası)", ["Kalem", "Değer"], satir,
                 "`kod/f3g_kartlar.py`; matris, grup senaryoları (`veri/f3_senaryo_grup.csv`) ve eylem kayıtlarından. Senaryo "
                 "şokları politika seçimi değil, çıkışın kendisi; önlemler Bölüm 4'teki eylemlerden. Makro mutabakat Faz 6'da.")


def ilerleme(V, kodlar, Y):
    c_toplam = int((V.k.kapsam_grubu == "C").sum())
    return (f"İLERLEME: Faz 3 parça 1 / 16 tamamlandı ({len(kodlar)} / {c_toplam} C sınıfı kartı) — SONRAKİ ADIM: "
            f"{Y['belge'].get('sonraki', 'Faz 3 parça 2 (13–15: tekstil, giyim, deri)')}; DEVAM bekleniyor.")


def bloklar(metin, V, Y, kodlar, grup):
    senaryo_no = {}
    for mt in BLOK.finditer(metin):
        g = mt.group(1).split("|")
        if g[0].startswith("TABLO:senaryo:"):
            senaryo_no[g[0].split(":")[2]] = g[1]

    def bir(mt):
        g = mt.group(1).split("|")
        bas, no = g[0], (g[1] if len(g) > 1 else "")
        n = int(g[2]) if len(g) > 2 else 8
        if bas == "ILERLEME":
            return ilerleme(V, kodlar, Y)
        if bas == "DEFTER":
            return defter(V, kodlar, Y, no, grup)
        if bas.startswith("KUNYE:"):
            kod = bas[6:]
            return kunye(V, Y, kod, f"C.{kodlar.index(kod) + 1}")
        if bas == "VERI_SAYFALARI":
            return "\n\n".join(veri_sayfasi(V, Y, kd, f"{no}.{i + 1}", senaryo_no.get(kd)) for i, kd in enumerate(kodlar))
        ad_ = bas[6:]
        if ad_.startswith("senaryo:"):
            return t_senaryo(V, Y, ad_.split(":")[1], no)
        if ad_.startswith("kucuk:"):
            return t_kucuk(V, Y, ad_.split(":")[1].split(","), no)
        if ad_ == "varsayim":
            return t_liste(f"Tablo {no} — Varsayım kaydına eklenen maddeler", ["Kimlik", "Varsayım"],
                           Y["belge"].get("varsayimlar", []))
        if ad_ == "vb":
            return t_liste(f"Tablo {no} — Açık veri boşlukları", ["Kimlik", "Veri boşluğu"], Y["belge"].get("veri_bosluklari", []))
        f = {"ozet": lambda: t_ozet(V, Y, kodlar, no, grup), "bolum": lambda: t_bolum(V, Y, kodlar, no),
             "rejim": lambda: t_rejim(V, Y, kodlar, no), "aski": lambda: t_aski(V, Y, kodlar, no, grup, n),
             "itu": lambda: t_itu(V, Y, kodlar, no), "tufe": lambda: t_tufe(V, Y, kodlar, no, grup, n),
             "durus": lambda: t_durus(V, Y, kodlar, no), "eylem_ortak": lambda: t_eylem_ortak(V, Y, kodlar, no),
             "eylem_sinif": lambda: t_eylem_sinif(V, Y, kodlar, no), "tetik": lambda: t_tetik(V, Y, kodlar, no),
             "matris_a": lambda: t_matris(V, Y, kodlar, no, "a"), "matris_b": lambda: t_matris(V, Y, kodlar, no, "b")}
        if ad_ not in f:
            raise ValueError(f"tanımsız tablo: {ad_}")
        return f[ad_]()
    return BLOK.sub(bir, metin)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--yaml", required=True, action="append", help="birden çok verilebilir; sırayla birleştirilir")
    ap.add_argument("--metin", required=True, help="şablon klasörü (*.md, ad sırasıyla) ya da tek dosya")
    ap.add_argument("--cikti", required=True)
    ap.add_argument("--out", default=yollar.VERI)
    a = ap.parse_args()
    Y = {"belge": {}, "siniflar": {}, "bolumler": {}}
    for yol in a.yaml:
        y_ = yaml.safe_load(open(yol, encoding="utf-8")) or {}
        for anahtar in Y:
            Y[anahtar].update(y_.get(anahtar) or {})
    V = Veri(a.out)
    kodlar = [k for k in V.m.index if k[:2] in Y["bolumler"]]
    bl = sorted(Y["bolumler"])
    grup = bl[0] if len(bl) == 1 else f"{bl[0]}-{bl[-1]}"
    V.Y, V.grup = Y, grup
    dosyalar = sorted(glob.glob(os.path.join(a.metin, "*.md"))) if os.path.isdir(a.metin) else [a.metin]
    metin = "\n\n".join(open(f, encoding="utf-8").read().strip() for f in dosyalar)
    metin = bloklar(metin, V, Y, kodlar, grup)
    metin = V.doldur(metin)
    kalan = re.findall(r"\{\{[^{}]*\}\}", metin)
    if kalan:
        raise ValueError(f"doldurulmamış yer tutucu: {kalan[:5]}")
    metin = re.sub(r"\n{3,}", "\n\n", metin)
    open(a.cikti, "w", encoding="utf-8").write(metin.rstrip() + "\n")
    print(f"{a.cikti}: {len(dosyalar)} şablon, {len(kodlar)} sınıf, {len(metin.split())} sözcük")


if __name__ == "__main__":
    main()
