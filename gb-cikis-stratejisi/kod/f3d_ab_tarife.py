"""Faz 3 — AB tarafı tarife maruziyeti, KN8 düzeyinde (kart alan 4; ana matris τ_AB).

Faz 0'daki S4 tarife duvarı (f0d) yalnız ad valorem kısmı alıyordu. Burada spesifik ve bileşik vergiler ad valorem
eşdeğerine (AVE) çevrilir ve artış rejime göre ayrıştırılır:
  AVE_spesifik = spesifik vergi (€/100 kg) / birim değer (€/100 kg)
  Birim değer: AB'nin Türkiye'den 2025 ithalatı (Comext, KN8; değer / 100 kg). KN8'de miktar yoksa aynı HS6'nın
  TR→AB birim değeri, o da yoksa AB27'nin dünyadan HS6 ithalatı (BACI 2024, $ → €).
  Birimler: €/100 kg, €/t, €/kg, €/hl (1 hl ≈ 100 kg), €/% vol/hl (alkol derecesi varsayımı: 2204 %12, 2205 %15,
  2206 %8, 2207 %95, 2208 %40), MIN/MAX hükümleri; € p/st ve €/m³ çevrilmez (yalnız ad valorem kısım). AVE ≤ %200.
S4 artışı (rota A, P50; AB'nin 2026 MFN'si, 2025 TR→AB ticaret ağırlığı):
  GB satırı           → tam MFN (ad valorem + spesifik AVE)
  İTÜ satırı          → yalnız sanayi bileşeni (ad valorem kısım); tarım bileşeni (EA / spesifik) bugün de ödeniyor
  TARIM (1/98) satırı → 0 (1/98 sürer); "1/98 kaybı" varyantında tam MFN (bugünkü tercih 0 sayılır: üst sınır, VB-06)
  AKÇT satırı         → 0 (1996 AKÇT Anlaşması sürer)
S2/S3: sanayi ve İTÜ sanayi bileşeni 0; menşe uyumsuz pay S4 artışını öder (f3e).
Ek bayraklar: EUDR (Tüzük 2023/1115 Ek I, 2026/2102 ile değişik; 30.12.2027'den eklenen satırlar ayrıca eudr_2027),
SKDM (veri/skdm_ek1_kn.csv).

Çıktı: veri/f3_ab_tarife_kn8.csv, veri/f3_ab_tarife_sinif.csv
"""

import argparse
import os
import re

import numpy as np
import pandas as pd

import yollar

USD_EUR_2024 = 1.0824                     # ECB yıllık ortalama referans kur ($/€), 2024 [V]
ALKOL = {"2204": 12, "2205": 15, "2206": 8, "2207": 95, "2208": 40}
AVE_TAVAN = 200.0
# EUDR Ek I (Tüzük 2023/1115), Yetki Devrine Dayanan Tüzük (AB) 2026/2102 ile değişik hâli (RG L 17.9.2026; 18.9.2026'dan),
# HS/KN önekleri [V]. 2026/2102 sığır derisini (ex 4101, ex 4104, ex 4107) ve ex 4010, ex 4016 kauçuk eşyayı çıkardı; 4012'yi
# 4012 90 30'a, 1201'i 1201 90 00'a, 9401'i ahşap oturma yerlerine daralttı. "ex" kayıtların istisnaları (ambalaj,
# geri kazanılmış kâğıt, kullanılmış eşya) öneklerle ayrılamaz: pay üst sınırdır.
EUDR = ("010221", "010229", "0201", "0202", "020610", "020622", "020629", "160250",
        "1801", "1802", "1803", "1804", "1805", "1806", "0901",
        "120710", "1511", "151321", "151329", "230660", "290545", "291570", "291590",
        "382311", "382312", "382319", "382370",
        "4001", "4005", "4006", "4007", "4008", "4011", "40129030", "4013", "4015", "4017",
        "12019000", "120810", "1507", "2304",
        "44", "47", "48", "49", "940131", "940141", "940161", "940169", "940180", "940191",
        "940330", "940340", "940350", "940360", "940391", "940610")
# 2026/2102'nin eklediği satırlar 30.12.2027'den uygulanır (T2028 ve T2029'da yürürlükte) [V]: dondurulmuş sığır dili, hazır
# kahve (2101 11 00) ve palm türevleri. Palm türevleri "ex" (yalnız palm kökenli) olduğundan pay üst sınırdır; kalıntı
# başlıklar ex 3824 99 ve ex 3907 29 hesaba katılmadı [H].
EUDR_2027 = ("02062100", "21011100", "151620", "151800", "152000", "290516", "29051700", "29051900", "291539", "291615",
             "29161910", "292119", "29239000", "29241900", "34011100", "340120")
SAYI = r"(\d+(?:[.,]\d+)?)"


def sayi(s):
    return float(s.replace(",", "."))


def ozgul_100kg(parca, hs4):
    """Metin parçasındaki spesifik vergilerin toplamı (€/100 kg net); çevrilemeyen birim varsa None."""
    toplam, bulundu = 0.0, False
    for m in re.finditer(SAYI + r"\s*€\s*(/\s*%\s*vol\s*/\s*hl|/\s*100\s*kg[^+)A-Z]*|/\s*t\b|/\s*kg/tot\. alc\.|"
                                r"/\s*kg[^+)A-Z]*|/\s*hl|p/st|/\s*m3|/\s*m²|/\s*\d+\s*p/st)", parca):
        deger, birim = sayi(m.group(1)), re.sub(r"\s+", "", m.group(2))
        bulundu = True
        if "%vol/hl" in birim:
            toplam += deger * ALKOL.get(hs4, 40)
        elif birim.startswith("/100kg"):
            toplam += deger
        elif birim == "/t":
            toplam += deger / 10
        elif birim.startswith("/kg/tot"):
            toplam += deger * 100 * 0.32 * ALKOL.get(hs4, 40) / 40
        elif birim.startswith("/kg"):
            toplam += deger * 100
        elif birim == "/hl":
            toplam += deger
        else:
            return None
    return toplam if bulundu else 0.0


def ave(metin, adval, tur, uv, hs4):
    """(ad valorem %, toplam MFN AVE %, spesifik AVE %). uv: €/100 kg."""
    a = float(adval) if pd.notna(adval) else 0.0
    if not isinstance(metin, str) or tur in ("footnote_only", "empty", "other"):
        return a, np.nan, np.nan
    if tur == "adval":
        return a, a, 0.0
    if tur == "compound_EA":
        return a, np.nan, np.nan                      # EA bileşimine bağlı; sanayi bileşeni = a
    gecerli = pd.notna(uv) and uv > 0
    sp = lambda p: (ozgul_100kg(p, hs4) / uv * 100 if gecerli and ozgul_100kg(p, hs4) is not None else np.nan)  # noqa
    if "MIN" in metin or "MAX" in metin:
        bas, *kalan = re.split(r"\b(MIN|MAX)\b", metin)
        taban = a + (sp(bas) if not re.fullmatch(r"\s*" + SAYI + r"\s*", bas) else 0.0)
        toplam = taban
        for i in range(0, len(kalan), 2):
            op, deger = kalan[i], kalan[i + 1]
            yuzde = re.fullmatch(r"\s*\(?\s*" + SAYI + r"\s*\)?\s*", deger)
            d = sayi(yuzde.group(1)) if yuzde else (sp(deger) + (sayi(re.match(r"\s*\(?\s*" + SAYI, deger).group(1))
                                                                  if re.match(r"\s*\(?\s*" + SAYI + r"\s*\+", deger) else 0.0))
            if pd.isna(d):
                continue
            toplam = max(toplam, d) if op == "MIN" else min(toplam, d)
        return a, min(toplam, AVE_TAVAN), min(max(toplam - a, 0.0), AVE_TAVAN)
    s = sp(metin)
    if pd.isna(s):
        return a, np.nan, np.nan
    return a, min(a + s, AVE_TAVAN), min(s, AVE_TAVAN)


def comext(yol, gosterge):
    x = pd.read_csv(yol, dtype=str)
    x = x[(x["product"].str.len() == 8) & x.indicators.eq(gosterge) & x.flow.eq("1")]
    return x.assign(v=pd.to_numeric(x.OBS_VALUE, errors="coerce")).groupby("product").v.sum()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=yollar.GIRDI)
    ap.add_argument("--out", default=yollar.VERI)
    a = ap.parse_args()
    v = lambda f: os.path.join(a.out, f)  # noqa: E731
    g = lambda f: yollar.bul(os.path.join(a.cache, f)) or os.path.join(a.cache, f)  # noqa: E731

    deger = comext(g("comext_eu_tr_2025_f1.csv"), "VALUE_IN_EUROS")
    miktar = comext(g("comext_eu_tr_2025_f1_miktar.csv"), "QUANTITY_IN_100KG")
    t = pd.DataFrame({"x_ab_eur": deger, "q_100kg": miktar.reindex(deger.index)})
    t.index.name = "cn8"
    t = t.reset_index()
    t = t[t.cn8.str.fullmatch(r"\d{8}")]
    t["hs6"] = t.cn8.str[:6]
    t["uv"] = t.x_ab_eur / t.q_100kg.where(t.q_100kg > 0)
    uv6 = t.groupby("hs6").apply(lambda d: d.x_ab_eur.sum() / d.q_100kg[d.q_100kg > 0].sum()
                                 if (d.q_100kg > 0).any() else np.nan, include_groups=False)
    b = pd.read_parquet(g(os.path.join("baci", "baci_hs17_ab27_ithalat_ihracatci_hs6_2020_2024.parquet")))
    b = b[b.t == b.t.max()]
    bu = b.groupby("k")[["v", "q"]].sum()
    uv_baci = (bu.v * 1e3 / USD_EUR_2024) / (bu.q * 10).where(bu.q > 0)       # € / 100 kg
    uv_baci.index = uv_baci.index.astype(str).str.zfill(6)
    t["uv_kaynak"] = np.where(t.uv.notna(), "KN8", np.where(t.hs6.map(uv6).notna(), "HS6-TR", "HS6-BACI"))
    t["uv"] = t.uv.fillna(t.hs6.map(uv6)).fillna(t.hs6.map(uv_baci))

    tar = pd.read_csv(v("tarife_ab_cn2026_cn8.csv"), dtype={"cn8": str, "hs6": str})
    t = t.merge(tar[["cn8", "duty_text", "adval_rate", "duty_type"]], on="cn8", how="left")
    # KN 2026'da bulunmayan satırlar: aynı HS6'nın ilk satırının vergisi [T]
    ilk6 = tar.drop_duplicates("hs6").set_index("hs6")
    eks = t.duty_type.isna()
    for c in ("duty_text", "adval_rate", "duty_type"):
        t.loc[eks, c] = t.loc[eks, "hs6"].map(ilk6[c])
    t["tarife_kaynak"] = np.where(eks, "HS6", "KN8")
    sonuc = [ave(r.duty_text, r.adval_rate, r.duty_type, r.uv, r.cn8[:4]) for r in t.itertuples()]
    t["adval"], t["mfn_ave"], t["ozgul_ave"] = zip(*sonuc)

    m = pd.read_csv(v("cn2025_nace_rejim.csv"), dtype={"cn8": str, "nace2": str})
    m = m[m.agirlik_f3 > 0][["cn8", "nace2", "agirlik_f3", "rejim"]]
    t = t.merge(m, on="cn8", how="left")
    t["agirlik_f3"] = t.agirlik_f3.fillna(1.0)
    t["rejim"] = t.rejim.fillna("GB")
    t["x_ab_meur"] = t.x_ab_eur * t.agirlik_f3 / 1e6
    mfn = t.mfn_ave.fillna(t.adval)                    # AVE çevrilemeyen satırda ad valorem kısım (alt sınır)
    t["artis_s4"] = np.select([t.rejim.eq("GB"), t.rejim.eq("ITU")], [mfn, t.adval], 0.0)
    t["artis_s4_tarim_kaybi"] = np.where(t.rejim.eq("TARIM"), mfn, t.artis_s4)
    t["eudr_2027"] = t.cn8.apply(lambda k: any(k.startswith(p) for p in EUDR_2027))
    t["eudr"] = t.cn8.apply(lambda k: any(k.startswith(p) for p in EUDR)) | t.eudr_2027
    sk = pd.read_csv(v("skdm_ek1_kn.csv"), dtype={"kn": str})
    t["skdm"] = t.cn8.apply(lambda k: any(k.startswith(p) for p in sk.kn))
    t["ave_eksik"] = t.mfn_ave.isna() & ~t.duty_type.isin(["compound_EA"]) & t.duty_type.ne("adval")

    sut = ["cn8", "nace2", "rejim", "agirlik_f3", "x_ab_meur", "q_100kg", "uv", "uv_kaynak", "duty_type", "duty_text",
           "tarife_kaynak", "adval", "ozgul_ave", "mfn_ave", "artis_s4", "artis_s4_tarim_kaybi", "eudr", "eudr_2027", "skdm"]
    t[sut].round(4).to_csv(v("f3_ab_tarife_kn8.csv"), index=False)

    satirlar = []
    for kod, d in t[t.nace2.notna()].groupby("nace2"):
        x = d.x_ab_meur
        w = x.sum()
        r = dict(kod=kod, x_ab_meur_2025=w, kn8_satir=len(d))
        if w > 0:
            r["tau_ab_s4"] = (x * d.artis_s4).sum() / w
            r["tau_ab_s4_tarim_kaybi"] = (x * d.artis_s4_tarim_kaybi).sum() / w
            r["tau_ab_mfn"] = (x * mfn.loc[d.index]).sum() / w
            r["tau_ab_s4_advalorem"] = (x * np.select([d.rejim.isin(["GB", "ITU"])], [d.adval], 0.0)).sum() / w
            for rj in ("GB", "ITU", "TARIM", "AKCT"):
                r[f"pay_{rj}"] = x[d.rejim.eq(rj)].sum() / w
            r["ozgul_vergi_payi"] = x[d.duty_type.isin(["specific", "compound", "mixed_minmax"])].sum() / w
            r["ea_payi"] = x[d.duty_type.eq("compound_EA")].sum() / w
            r["ave_eksik_payi"] = x[d.ave_eksik].sum() / w
            tepe = d[d.artis_s4 >= 10]
            r["tepe_satir_sayisi"] = len(tepe)
            r["tepe_ihracat_payi"] = tepe.x_ab_meur.sum() / w
            ust = d.sort_values("x_ab_meur", ascending=False)
            ust = ust[ust.artis_s4 >= 10].head(3)
            r["tepe_satirlar"] = "; ".join(f"{s.cn8} %{s.artis_s4:.1f} (€{s.x_ab_meur:.1f} mn)" for s in ust.itertuples())
            r["eudr_payi"] = x[d.eudr].sum() / w
            r["eudr_2027_payi"] = x[d.eudr_2027].sum() / w
            r["skdm_payi"] = x[d.skdm].sum() / w
        satirlar.append(r)
    s = pd.DataFrame(satirlar).set_index("kod")
    s.round(5).to_csv(v("f3_ab_tarife_sinif.csv"))

    c = s[s.index.str.match(r"^(1\d|2\d|3[0-3])\.")]
    w = c.x_ab_meur_2025
    print(f"KN8 satırı {len(t)}; AVE çevrilemeyen özgül satırların ihracat payı "
          f"%{100 * t.loc[t.ave_eksik, 'x_ab_meur'].sum() / t.x_ab_meur.sum():.2f}; "
          f"birim değer kaynağı: {t.uv_kaynak.value_counts().to_dict()}")
    print(f"C bölümü S4 τ_AB (ağırlıklı): %{(w * c.tau_ab_s4).sum() / w.sum():.2f} "
          f"(yalnız ad valorem %{(w * c.tau_ab_s4_advalorem).sum() / w.sum():.2f}); "
          f"1/98 kaybıyla %{(w * c.tau_ab_s4_tarim_kaybi).sum() / w.sum():.2f}")
    print(f"Tüm ürünler S4 τ_AB: %{(t.x_ab_meur * t.artis_s4).sum() / t.x_ab_meur.sum():.2f}; "
          f"1/98 kaybıyla %{(t.x_ab_meur * t.artis_s4_tarim_kaybi).sum() / t.x_ab_meur.sum():.2f}")


if __name__ == "__main__":
    main()
