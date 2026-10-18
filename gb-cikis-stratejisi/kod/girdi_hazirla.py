"""Paketteki ham girdileri (girdi/) hazırlar ve belgeler.

Betikler ham verilerini girdi/ klasöründen okur; bir dosya yoksa resmî kaynağından indirip oraya yazar
(kod/yollar.py). Bu betik üç iş yapar:

  baci-ozet   CEPII BACI HS17 V202601 tam dosyalarından (her yıl ≈95 MB) paketin taşıyabileceği özetleri üretir:
                girdi/baci/baci_hs17_2024_f1c_ozet.parquet      f1c'nin kullandığı satırlar: ithalatçı = AB'nin STA
                                                                ortağı olup Türkiye'nin olmadığı 33 pazar (bütün
                                                                ihracatçılar) + Türkiye'nin bu pazarlardan ithalatı
                girdi/baci/baci_hs17_ikili_toplam_{2020,2024}.parquet   f2f'nin kullandığı ikili toplamlar (i, j, v)
              Türkiye'nin ikili HS6 akışları ve dünya ihracatı özetleri baci_ozet.py ile üretilir.
  sikistir    1 MB'tan büyük CSV, TSV ve XML dosyalarını gzip'ler (betikler .gz kopyayı kendiliğinden okur).
  manifest    girdi/MANIFEST.csv: her dosyanın boyutu, SHA-256 özeti, kaynağı, adresi ve onu okuyan betik.

Kullanım:
  python3 girdi_hazirla.py baci-ozet --baci-dizin <BACI klasörü: all_countries/*.parquet, country_codes_V202601.csv>
  python3 girdi_hazirla.py sikistir
  python3 girdi_hazirla.py manifest
"""

import argparse
import fnmatch
import gzip
import hashlib
import os
import shutil

import pandas as pd

import yollar

ERISIM = "2026-10-17/18"
ARA_URUNLER = {"tarife_tr_2026_tam.csv"}  # f0e'nin girdi/'ye yazdığı ara ürün (girdi/.gitignore)

# (desen, kaynak kurum, açıklama, adres, okuyan betik); ilk eşleşen desen kullanılır
KAYNAKLAR = [
    ("nace_r2_en.tsv", "Eurostat", "NACE Rev. 2 kod listesi (İngilizce adlar)",
     "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/codelist/ESTAT/NACE_R2", "f0_nace_kapsam"),
    ("nace_r21_en.tsv", "Eurostat", "NACE Rev. 2.1 kod listesi",
     "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/codelist/ESTAT/NACE_R2_1", "f0_nace_kapsam"),
    ("nace21_nace2.xlsx", "AB Yayın Ofisi (EU Vocabularies, ShowVoc)", "NACE Rev. 2.1 – Rev. 2 karşılık tablosu",
     "https://showvoc.op.europa.eu", "f0_nace_kapsam"),
    ("cpa22_cpa21.xlsx", "AB Yayın Ofisi (ShowVoc)", "CPA 2.2 – CPA 2.1 karşılık tablosu",
     "https://showvoc.op.europa.eu", "f0_nace_kapsam"),
    ("cpa22_cn2025.tsv*", "AB Yayın Ofisi (ShowVoc)", "CPA 2.2 – CN 2025 karşılık tablosu",
     "https://showvoc.op.europa.eu", "f0_nace_kapsam"),
    ("comext_eu_tr_*", "Eurostat Comext", "AB27–Türkiye ticareti, CN8, 2025 (DS-045409, akış 1/2)",
     "https://ec.europa.eu/eurostat/api/comext/dissemination/sdmx/2.1/data/DS-045409", "f0_nace_kapsam"),
    ("gib_sinif4.xls", "Gelir İdaresi Başkanlığı", "NACE Rev. 2.1 dört haneli sınıf listesi (Türkçe adlar)",
     "https://www.gib.gov.tr", "f0_nace_kapsam"),
    ("tuik_DF_YAPISAL_EFGTG*", "TÜİK Dağıtım Yönetim Sistemi", "Yıllık Sanayi ve Hizmet İstatistikleri (NACE Rev. 2 / 2.1)",
     "https://databrowser2.tuik.gov.tr", "f0b_tuik_yshi"),
    ("ecb/*", "Avrupa Merkez Bankası", "Yıllık ortalama döviz kurları (EXR)", "https://data-api.ecb.europa.eu",
     "f0b_tuik_yshi"),
    ("tuik_DF_BR_FAALIYET*", "TÜİK Dağıtım Yönetim Sistemi", "İş kayıtları: İBBS × NACE × büyüklük girişim sayıları",
     "https://databrowser2.tuik.gov.tr", "f0c_tuik_bolge_tufe"),
    ("tuik_DF_TUFE_SDMX_TT04*", "TÜİK Dağıtım Yönetim Sistemi", "TÜFE ağırlıkları (COICOP 2018)",
     "https://databrowser2.tuik.gov.tr", "f0c_tuik_bolge_tufe"),
    ("tuik_DF_SANAYI_URETIM_ENDEKS_ALT_C*", "TÜİK Dağıtım Yönetim Sistemi", "Sanayi üretim endeksi, sınıf düzeyi, aylık",
     "https://databrowser2.tuik.gov.tr", "f0c_tuik_bolge_tufe"),
    ("tarife_tr/*", "T.C. Ticaret Bakanlığı", "İthalat Rejimi Kararı (3350), İGV Kararı (3351), TGTC 2026 konsolide ekleri",
     "https://ticaret.gov.tr/ithalat/ithalat-mevzuati", "f0e_tarifeler (tarife_tr.py)"),
    ("cn2026_fmx4.zip", "AB Yayın Ofisi", "Uyg. Tüzüğü (AB) 2025/1926 (KN 2026), Formex 4",
     "https://publications.europa.eu/resource/celex/32025R1926", "f0e_tarifeler (tarife_ab.py)"),
    ("f1/ct_*", "BM Comtrade", "Türkiye beyanı, toplam ve AG2 ticaret (genel önizleme API'si)",
     "https://comtradeapi.un.org/public/v1/preview/C/A/HS", "f1a_ab_ticaret"),
    ("f1/cx_*", "Eurostat Comext", "AB27–Türkiye ve AB27 dışı ticaret, 1999–2025 (DS-045409)",
     "https://ec.europa.eu/eurostat/api/comext/dissemination/sdmx/2.1/data/DS-045409", "f1a_ab_ticaret"),
    ("f1/wits/*", "Dünya Bankası WITS (TRAINS)", "Ortak ülkelerin MFN tarifeleri, HS6",
     "https://wits.worldbank.org/API/V1/SDMX/V21/datasource/TRN", "f1c_sta_asimetrisi"),
    ("evds3/*", "TCMB EVDS3", "Ödemeler dengesi, GSYH, kurlar, reel kur, UYP (anlık görüntü, 18.10.2026)",
     "https://evds3.tcmb.gov.tr", "f1b_odemeler_dengesi (evds3.py)"),
    ("tuik_DF_UHTI_HIZMET_COGRAFI_C*", "TÜİK Dağıtım Yönetim Sistemi", "Uluslararası hizmet ticareti, ortak ülke × hizmet türü",
     "https://databrowser2.tuik.gov.tr", "f1b_odemeler_dengesi"),
    ("sgk_yillik_*", "SGK", "SGK istatistik yıllığı 2025 (il × NACE sigortalı)", "https://www.sgk.gov.tr",
     "f1e_bolgesel"),
    ("io2023/*", "TÜİK Veri Portalı", "Girdi-çıktı tabloları 2023 (yurt içi, ithal, alıcı fiyatlarıyla kullanım)",
     "https://veriportali.tuik.gov.tr", "f2a_io_fiyat, f2b, f2c0, f2e"),
    ("prodtr/*", "TÜİK Veri Portalı", "Yıllık Sanayi Ürün İstatistikleri (PRODTR) bülten tabloları",
     "https://veriportali.tuik.gov.tr", "f2b_tarife_politikasi, f2c0 (prodtr.py)"),
    ("bec/*", "Dünya Bankası WITS", "HS 2017 → BEC 5 karşılık tablosu", "https://wits.worldbank.org", "f2b_tarife_politikasi"),
    ("baci/baci_hs17_2024_f1c_ozet.parquet", "CEPII BACI HS17 V202601 (özet: girdi_hazirla.py)",
     "2024; 33 STA asimetrisi pazarının ithalatı ve Türkiye'nin bu pazarlardan ithalatı",
     "https://www.cepii.fr/DATA_DOWNLOAD/baci/data/BACI_HS17_V202601.zip", "f1c_sta_asimetrisi"),
    ("baci/baci_hs17_ikili_toplam_*", "CEPII BACI HS17 V202601 (özet: girdi_hazirla.py)", "İkili toplam ticaret (bin $)",
     "https://www.cepii.fr/DATA_DOWNLOAD/baci/data/BACI_HS17_V202601.zip", "f2f_cekim_modeli"),
    ("baci/baci_hs17_tur_bilateral_*", "CEPII BACI HS17 V202601 (özet: baci_ozet.py)",
     "Türkiye'nin ihracatı ve ithalatı, HS6 × ortak, 2020–2024",
     "https://www.cepii.fr/DATA_DOWNLOAD/baci/data/BACI_HS17_V202601.zip", "f2a, f2b, f2c0, f2d"),
    ("baci/baci_hs17_world_exports_*", "CEPII BACI HS17 V202601 (özet: baci_ozet.py)",
     "İhracatçı × HS6 dünya ihracatı ve RCA, 2024",
     "https://www.cepii.fr/DATA_DOWNLOAD/baci/data/BACI_HS17_V202601.zip", "f2b_tarife_politikasi"),
    ("baci/*", "CEPII BACI HS17 V202601", "Ülke ve ürün kodları", "https://www.cepii.fr", "f1c, f2f"),
    ("comtrade/*", "BM Comtrade (comtrade_tr_hs6.py)", "Türkiye'nin dünyaya ihracatı ve ithalatı, HS6, 2025",
     "https://comtradeapi.un.org/public/v1/preview/C/A/HS", "f1d_maruziyet"),
    ("f2_cekim/gravity_V202211_1980_v4.parquet", "CEPII Gravity V202211 (özet: f2f_cekim_modeli.gravity_oku)",
     "1980–2021, f2f'nin kullandığı sütunlar", "https://www.cepii.fr/DATA_DOWNLOAD/gravity/data/Gravity_csv_V202211.zip",
     "f2f_cekim_modeli"),
    ("f2_cekim/gravity_ulkeler.csv", "CEPII Gravity V202211", "Countries_V202211.csv",
     "https://www.cepii.fr/DATA_DOWNLOAD/gravity/data/Gravity_csv_V202211.zip", "f2f_cekim_modeli"),
    ("f2_cekim/desta/*", "DESTA v2.3 (Dür, Baccini ve Elsig)", "Ticaret anlaşmaları, ikili liste ve derinlik endeksleri",
     "https://www.designoftradeagreements.org", "f2f_cekim_modeli"),
    ("f2_cekim/unama/*", "BM İstatistik Bölümü", "Ulusal Hesaplar Ana Toplamları (cari $)",
     "https://unstats.un.org/unsd/amaapi/api/file/2", "f2f_cekim_modeli"),
]


def baci_ozet(baci_dizin):
    import f1c_sta_asimetrisi as f1c
    hedef_dizin = yollar.girdi("baci")
    os.makedirs(hedef_dizin, exist_ok=True)
    uk = pd.read_csv(os.path.join(baci_dizin, "country_codes_V202601.csv"), dtype={"country_code": int})
    iso = uk[~uk.country_name.str.contains(r"\.\.\.", regex=True)].drop_duplicates("country_iso3").set_index(
        "country_iso3").country_code
    tr, hedef = iso["TUR"], {iso[o[0]] for o in f1c.ORTAKLAR}
    tam = lambda y: os.path.join(baci_dizin, "all_countries", f"BACI_HS17_Y{y}_V202601.parquet")  # noqa: E731
    b = pd.read_parquet(tam(2024), columns=["i", "j", "k", "v"])
    x = b[b.j.isin(hedef) | ((b.j == tr) & b.i.isin(hedef))]
    x.to_parquet(os.path.join(hedef_dizin, "baci_hs17_2024_f1c_ozet.parquet"), compression="zstd", index=False)
    print("f1c özeti:", len(x), "satır /", len(b))
    for y in (2020, 2024):
        t = pd.read_parquet(tam(y), columns=["i", "j", "v"]).groupby(["i", "j"], as_index=False).v.sum()
        t.to_parquet(os.path.join(hedef_dizin, f"baci_hs17_ikili_toplam_{y}.parquet"), compression="zstd", index=False)
        print(f"ikili toplam {y}:", len(t), "çift")
    for ad in ("country_codes_V202601.csv", "product_codes_HS17_V202601.csv"):
        shutil.copy2(os.path.join(baci_dizin, ad), os.path.join(hedef_dizin, ad))


def sikistir(esik=1 << 20):
    for kok, _, dosyalar in os.walk(yollar.GIRDI):
        for ad in dosyalar:
            yol = os.path.join(kok, ad)
            if ad.lower().endswith((".csv", ".tsv", ".xml")) and os.path.getsize(yol) > esik:
                with open(yol, "rb") as g, gzip.GzipFile(yol + ".gz", "wb", mtime=0) as c:
                    shutil.copyfileobj(g, c)
                os.remove(yol)
                print("gzip:", os.path.relpath(yol, yollar.GIRDI))


def manifest():
    satirlar = []
    for kok, _, dosyalar in os.walk(yollar.GIRDI):
        for ad in sorted(dosyalar):
            yol = os.path.join(kok, ad)
            goreli = os.path.relpath(yol, yollar.GIRDI).replace(os.sep, "/")
            if goreli in ("MANIFEST.csv", "README.md", ".gitignore") or ad in ARA_URUNLER or ad.endswith(".part"):
                continue
            h = hashlib.sha256()
            with open(yol, "rb") as f:
                for parca in iter(lambda: f.read(1 << 20), b""):
                    h.update(parca)
            kaynak = next((k for k in KAYNAKLAR if fnmatch.fnmatch(goreli, k[0]) or fnmatch.fnmatch(ad, k[0])),
                          ("", "?", "", "", ""))
            satirlar.append(dict(dosya=goreli, bayt=os.path.getsize(yol), sha256=h.hexdigest(), kaynak=kaynak[1],
                                 aciklama=kaynak[2], adres=kaynak[3], okuyan=kaynak[4], erisim=ERISIM))
    m = pd.DataFrame(satirlar).sort_values("dosya")
    m.to_csv(yollar.girdi("MANIFEST.csv"), index=False)
    bilinmeyen = m[m.kaynak == "?"]
    print(len(m), "dosya,", round(m.bayt.sum() / 1e6, 1), "MB; kaynağı tanımsız:", list(bilinmeyen.dosya))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("is_", choices=["baci-ozet", "sikistir", "manifest"])
    ap.add_argument("--baci-dizin")
    a = ap.parse_args()
    if a.is_ == "baci-ozet":
        baci_ozet(a.baci_dizin)
    elif a.is_ == "sikistir":
        sikistir()
    else:
        manifest()


if __name__ == "__main__":
    main()
