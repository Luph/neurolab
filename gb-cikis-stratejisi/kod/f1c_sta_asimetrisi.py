"""Faz 1 — STA asimetrisi: AB'nin serbest ticaret anlaşması olup Türkiye'nin olmadığı pazarlar.

GB, Türkiye'yi AB'nin ortak gümrük tarifesine uymakla yükümlü kılar; AB'nin üçüncü ülkelerle
imzaladığı STA'lar ise Türk ihracatına karşılıklı erişim sağlamaz. Bu betik, AB'nin STA ortağı
olup Türkiye ile STA'sı yürürlükte olmayan pazarlarda:
  - Türkiye'nin ihracatını (BACI 2024, HS6),
  - Türk ihracatının karşılaştığı MFN tarifesini (WITS/TRAINS, ortağın en son yılı, HS6 basit
    ortalama; Türkiye'nin ihracat bileşimiyle ağırlıklı),
  - aynı pazarda AB ihracatını ve AB'nin tercih marjını (AB ihracatı × MFN; liberalizasyonu
    tamamlanmış satırlarda AB'nin ödemediği vergi; EPA ve geçiş takvimi süren anlaşmalarda üst sınır)
hesaplar.

Kaynaklar (kimlik doğrulamasız):
  - CEPII BACI HS17 V202601 (yıl 2024; parquet dosyası --baci ile verilir)
  - WITS TRAINS SDMX API: /datasource/TRN/reporter/{ortak}/partner/000/product/all/year/{yıl}/datatype/reported
Notlar:
  - BACI HS2017; WITS tarifeleri ortağın kendi HS sürümündedir (çoğunlukla HS2022). HS6 eşleşmeyen
    satırlar (HS2022 değişiklikleri) ağırlıktan düşülür; kapsama oranı çıktıda verilir.
  - Anlaşma durumu ve yürürlük yılları 17.10.2026 itibarıyla; [D?] işaretliler Faz 2'de doğrulanacak.

Çıktı: veri/teshis_sta_asimetrisi.csv
"""

import argparse
import os
import xml.etree.ElementTree as ET

import pandas as pd

import nazik_http

WITS = ("https://wits.worldbank.org/API/V1/SDMX/V21/datasource/TRN/reporter/{r}/partner/000/product/all/"
        "year/{y}/datatype/reported")

AB27_ISO3 = ["AUT", "BEL", "BGR", "HRV", "CYP", "CZE", "DNK", "EST", "FIN", "FRA", "DEU", "GRC", "HUN", "IRL",
             "ITA", "LVA", "LTU", "LUX", "MLT", "NLD", "POL", "PRT", "ROU", "SVK", "SVN", "ESP", "SWE"]

# iso3, WITS kodu, grup, AB anlaşması, AB yürürlük yılı, durum, not
ORTAKLAR = [
    ("MEX", "484", "Meksika", "Küresel Anlaşma (STA)", 2000, "yürürlükte", "modernize anlaşma imza sürecinde [D?]"),
    ("CAN", "124", "Kanada", "CETA", 2017, "geçici uygulamada", ""),
    ("JPN", "392", "Japonya", "EPA", 2019, "yürürlükte", "TR–Japonya EPA müzakeresi 2014'ten beri sürüyor"),
    ("VNM", "704", "Vietnam", "EVFTA", 2020, "yürürlükte (geçiş takvimi 2030'a kadar)", ""),
    ("DZA", "012", "Cezayir", "Ortaklık Anlaşması", 2005, "yürürlükte (Cezayir'in kısıtlamaları var)", ""),
    ("ZAF", "710", "GAGB (SACU)", "SADC EPA", 2016, "yürürlükte", "GAGB ortak tarifesi"),
    ("MOZ", "508", "Mozambik", "SADC EPA", 2018, "yürürlükte (asimetrik)", ""),
    ("COL", "170", "Kolombiya", "Ticaret Anlaşması", 2013, "yürürlükte", ""),
    ("PER", "604", "Peru", "Ticaret Anlaşması", 2013, "yürürlükte", ""),
    ("ECU", "218", "Ekvador", "Ticaret Anlaşması", 2017, "yürürlükte", "TR–Ekvador STA müzakeresi askıda [D?]"),
    ("CRI", "188", "Orta Amerika", "Ortaklık Anlaşması", 2013, "yürürlükte", ""),
    ("SLV", "222", "Orta Amerika", "Ortaklık Anlaşması", 2013, "yürürlükte", ""),
    ("GTM", "320", "Orta Amerika", "Ortaklık Anlaşması", 2013, "yürürlükte", ""),
    ("HND", "340", "Orta Amerika", "Ortaklık Anlaşması", 2013, "yürürlükte", ""),
    ("NIC", "558", "Orta Amerika", "Ortaklık Anlaşması", 2013, "yürürlükte", ""),
    ("PAN", "591", "Orta Amerika", "Ortaklık Anlaşması", 2013, "yürürlükte", ""),
    ("NZL", "554", "Yeni Zelanda", "STA", 2024, "yürürlükte", ""),
    ("KEN", "404", "Kenya", "EPA", 2024, "yürürlükte (25 yıllık asimetrik takvim)", ""),
    ("DOM", "214", "CARIFORUM", "EPA", 2008, "geçici uygulamada (asimetrik)", ""),
    ("JAM", "388", "CARIFORUM", "EPA", 2008, "geçici uygulamada (asimetrik)", ""),
    ("TTO", "780", "CARIFORUM", "EPA", 2008, "geçici uygulamada (asimetrik)", ""),
    ("CIV", "384", "Fildişi Sahili", "Ara EPA", 2016, "yürürlükte (asimetrik)", ""),
    ("GHA", "288", "Gana", "Ara EPA", 2016, "yürürlükte (asimetrik)", ""),
    ("CMR", "120", "Kamerun", "Ara EPA", 2014, "yürürlükte (asimetrik)", ""),
    ("MDG", "450", "Doğu ve Güney Afrika (ESA)", "Ara EPA", 2012, "yürürlükte (asimetrik)", "TR–Morityus STA var"),
    ("ZWE", "716", "Doğu ve Güney Afrika (ESA)", "Ara EPA", 2012, "yürürlükte (asimetrik)", ""),
    ("BRA", "076", "Mercosur", "Ortaklık Anlaşması", None, "imzalı, yürürlük bekliyor [D?]", ""),
    ("ARG", "032", "Mercosur", "Ortaklık Anlaşması", None, "imzalı, yürürlük bekliyor [D?]", ""),
    ("URY", "858", "Mercosur", "Ortaklık Anlaşması", None, "imzalı, yürürlük bekliyor [D?]", ""),
    ("PRY", "600", "Mercosur", "Ortaklık Anlaşması", None, "imzalı, yürürlük bekliyor [D?]", ""),
    ("IND", "356", "Hindistan", "STA", None, "müzakere sonuçlandı, yürürlük bekliyor [D?]", ""),
    ("IDN", "360", "Endonezya", "CEPA", None, "müzakere sonuçlandı, yürürlük bekliyor [D?]",
     "TR–Endonezya müzakeresi sürüyor"),
    ("AUS", "036", "Avustralya", "STA", None, "müzakere sürüyor [D?]", ""),
]
YILLAR = (2025, 2024, 2023, 2022, 2021)


def wits_mfn(kod, onbellek):
    """Ortağın en son yıl MFN tarifesi (HS6 basit ortalama). Bulunamazsa boş tablo."""
    for y in YILLAR:
        yol = os.path.join(onbellek, f"wits_{kod}_{y}.xml")
        if not os.path.exists(yol):
            r = nazik_http.get(WITS.format(r=kod, y=y), timeout=600)
            if r.status_code != 200:
                continue
            with open(yol, "wb") as f:
                f.write(r.content)
        satirlar = []
        for s in ET.parse(yol).getroot().iter():
            if s.tag.endswith("Series"):
                for o in s:
                    if o.tag.endswith("Obs"):
                        satirlar.append((s.attrib.get("PRODUCTCODE"), o.attrib.get("OBS_VALUE")))
        if satirlar:
            x = pd.DataFrame(satirlar, columns=["hs6", "mfn"])
            x["mfn"] = pd.to_numeric(x.mfn, errors="coerce")
            return x.groupby("hs6").mfn.mean(), y
    return pd.Series(dtype=float), None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baci", required=True, help="BACI_HS17_Y2024_V202601.parquet")
    ap.add_argument("--ulke-kodlari", required=True, help="BACI country_codes_V202601.csv")
    ap.add_argument("--cache", default=os.path.expanduser("~/.cache/gb_cikis"))
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    c = os.path.join(a.cache, "f1", "wits")
    os.makedirs(c, exist_ok=True)

    uk = pd.read_csv(a.ulke_kodlari, dtype={"country_code": int})
    iso = uk[~uk.country_name.str.contains(r"\.\.\.", regex=True)].drop_duplicates("country_iso3").set_index(
        "country_iso3").country_code
    tr, ab = iso["TUR"], set(iso[AB27_ISO3])
    b = pd.read_parquet(a.baci, columns=["i", "j", "k", "v"])
    hedef = {iso[o[0]] for o in ORTAKLAR}
    b = b[b.j.isin(hedef)]
    b["hs6"] = b.k.astype(str).str.zfill(6)
    b["kaynak"] = b.i.map(lambda i: "TR" if i == tr else ("AB27" if i in ab else "diger"))

    satirlar = []
    for kod3, wits, grup, anlasma, yil, durum, notu in ORTAKLAR:
        j = iso[kod3]
        x = b[b.j == j].groupby(["hs6", "kaynak"]).v.sum().unstack(fill_value=0)
        for s in ("TR", "AB27", "diger"):
            if s not in x:
                x[s] = 0.0
        mfn, tyil = wits_mfn(wits, c)
        x["mfn"] = x.index.map(mfn)
        k = x[x.mfn.notna()]
        tr_top, ab_top, top = x.TR.sum(), x.AB27.sum(), x[["TR", "AB27", "diger"]].sum().sum()
        satirlar.append(dict(
            iso3=kod3, ortak_grubu=grup, ab_anlasmasi=anlasma, ab_yururluk=yil, durum=durum, not_=notu,
            tarife_yili=tyil,
            ithalat_toplam_musd=top / 1e3, tr_ihracati_musd=tr_top / 1e3, ab27_ihracati_musd=ab_top / 1e3,
            tr_pazar_payi=tr_top / top if top else None, ab27_pazar_payi=ab_top / top if top else None,
            tarife_kapsama_tr=k.TR.sum() / tr_top if tr_top else None,
            tr_agirlikli_mfn=(k.TR * k.mfn).sum() / k.TR.sum() if k.TR.sum() else None,
            tr_mfn_pozitif_pay=k.TR[k.mfn > 0].sum() / k.TR.sum() if k.TR.sum() else None,
            tr_odenen_vergi_musd=(k.TR * k.mfn / 100).sum() / 1e3,
            ab27_agirlikli_mfn=(k.AB27 * k.mfn).sum() / k.AB27.sum() if k.AB27.sum() else None,
            ab27_tercih_avantaji_musd=(k.AB27 * k.mfn / 100).sum() / 1e3,
            basit_ortalama_mfn=mfn.mean() if len(mfn) else None,
        ))
        print(kod3, tyil, round(tr_top / 1e3, 1), flush=True)
    t = pd.DataFrame(satirlar).rename(columns={"not_": "not"})
    t.round(4).to_csv(os.path.join(a.out, "teshis_sta_asimetrisi.csv"), index=False)

    t["yururlukte"] = t.ab_yururluk.notna()
    for etiket, g in t.groupby("yururlukte"):
        print("AB STA'sı yürürlükte" if etiket else "Bekleyen", "| TR ihracatı", round(g.tr_ihracati_musd.sum()),
              "mn $ | TR'nin ödediği MFN vergisi", round(g.tr_odenen_vergi_musd.sum()),
              "mn $ | AB27 ihracatı", round(g.ab27_ihracati_musd.sum()),
              "mn $ | AB tercih avantajı (üst sınır)", round(g.ab27_tercih_avantaji_musd.sum()), "mn $")
    pd.set_option("display.width", 250)
    print(t.drop(columns=["not", "durum", "ab_anlasmasi"]).round(3).to_string(index=False))


if __name__ == "__main__":
    main()
