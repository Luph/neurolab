"""Faz 2 — Yapısal çekim modeli: AB–Türkiye Gümrük Birliği'nin (GB) ticaret etkisi, AB STA'larının derinliğe
göre etkisi ve GB'nin derin STA (S2), temel STA (S3) ya da anlaşmasızlıkla (S4, DTÖ) ikamesinin ticaret etkisi.

Kaynaklar (kimlik doğrulamasız):
  - CEPII Gravity V202211 (Conte, Cotterlaz ve Mayer 2022; en güncel sürüm): ikili mal ticareti 1980–2020, bin $
    (IMF DOTS, UN Comtrade, BACI toplam ve imalat), WTO RTA kuklası (fta_wto), uzaklık, sömürge bağı, ülke listesi
  - DESTA v2.3 (Dür, Baccini ve Elsig 2014; Eylül 2025): AB anlaşmalarının derinlik endeksi (0–7) ve Rasch ölçeği
  - İsteğe bağlı (--baci-dizin): CEPII BACI HS17 V202601 parquet (2020 sürüm denetimi ve 2024 gözlemi)
  - GE: BM Ulusal Hesaplar Ana Toplamları (UN AMA, cari $): ISIC A–B, C–E ve D katma değeri, GSYH
Yöntem (Yotov, Piermartini, Monteiro ve Larch 2016, bölüm 1–2):
  X_ijt = exp(π_it + χ_jt + μ_ij + β'D_ijt)·ε_ijt; PPML (pyfixest.fepois); ihracatçı-yıl, ithalatçı-yıl, yönlü ikili
  sabit etkiler; SH yönsüz ülke çiftine göre kümelenmiş (CRV1). Ana örnek (M1): IMF DOTS (ithalatçı beyanı, yoksa
  ihracatçı aynası; iki taraf o yıl veri veriyorsa eksik = 0), 1988–2020, 4 yıllık aralık; 2000–2020 ortalama
  ticaretine göre ilk 150 egemen ekonomi (+ Tayvan, Hong Kong, Makao) ve AB28 + TR. Toplam mal ticareti
  (imalat ayrımı CEPII'de yalnız BACI ile, 1996'dan). Ülke içi ticaret yok: β'lar üçüncü ülkelerle ticarete göre
  görecelidir (yaratma ve saptırma birlikte); AB/TR dışı küresel değişimler sabit etkilerde.
  Kuklalar (her çift-yıl tek kategoride): GB_TR_AB (TR→AB üyesi; 1996'dan ya da üyelikten), GB_AB_TR; AB_STA_DERIN,
  AB_STA_TEMEL; kontroller AB_KATILIM (Avrupa Anlaşmaları, İOA, Kıbrıs/Malta OA), AB_EFTA (1973 STA'ları, AEA),
  AB_EPA (EPA'lar, Andorra/San Marino GB'leri), AB_UYELIK (AB içi), RTA_DIGER (diğer RTA'lar).
  Sınıflama (AB_ANLASMA, DESTA derinliği konsola yazılır): DERIN = Kore 2011, Kolombiya/Peru 2013, Ekvador 2017,
  Orta Amerika 2013, Gürcistan ve Moldova 2014, Ukrayna 2016 (DCFTA'lar), CETA 2017, Japonya 2019, Singapur 2019,
  Vietnam 2020 (DESTA 6–7; Rasch 1,6–2,1); TEMEL = Avrupa-Akdeniz OA'ları (Tunus 1998, Fas 2000, Ürdün 2002, Lübnan
  2003, Mısır 2004, Cezayir 2005), İsrail 1975/2000, Meksika 2000, Güney Afrika 2000, Şili 2003, Faroe (DESTA 1–5,
  Şili 7). R4: DESTA Rasch ≥ 1,5 (Şili ve CARIFORUM derin); R5: dar derin tanımı. AB–BK TCA (2021) ayrı kukla.
  Veri düzeltmeleri: BEL+LUX = BLX (IMF'de 1997 öncesi yok → Comtrade BLX); DEU.1/DEU.2 vb. birleşik; SCG → SRB;
  1993 öncesi dağılan birimler (SSCB, Yugoslavya, ÇSFC, DAC) örnek dışı. AB'li ve TR'li çiftlerde anlaşma tarihleri
  elle kodlanır (CEPII fta_wto'da gecikme ve hatalar: Romanya'nın bütün çiftleri 0, TR–Çekya/Malezya/Moldova 0,
  AB–Orta Amerika 2016); Romanya'nın 2007 öncesi STA'ları ROU_STA ile düzeltilir; diğer çiftlerde fta_wto.
  Yürürlük kuralı: anlaşma t yılının 1 Temmuz'unda yürürlükteyse t "yürürlükte" (ör. Vietnam 8/2020 → 2021).
  Sağlamlık: (i) 2020 hariç; (ii) Comtrade, IMF/BACI/BACI-imalat 1996–2020 aynı pencere, BACI 2024 uzatması
  (2024: BACI HS17 V202601; 2021'den sonra fta_wto 2021 değeriyle taşınır; Ukrayna 2022+ ve Rusya yaptırımları
  kontrol); (iii) 3 ve 5 yıllık aralık, yıllık veri; ayrıca öncüler, gecikmeler, GB olay çalışması, genişleme
  ayrımı, uzaklık×yıl, sömürge×yıl, AB içi×yıl, tüm ülkeler, yönlü kümeleme.
  Senaryolar (kısmi denge, ÇDT ve gelirler sabit): S0'a göre % değişim = exp(β_X − β_GB,yön) − 1, β_S4 = 0.
  %90 GA log uzayında delta yöntemiyle (doğrusal bileşim; normal varsayımı altında parametrik bootstrap ile aynı).
  Türkiye'ye özgü S3: S3_TR = TR–aday STA'sından GB'ye geçiş (M5), S3_BK = TR–BK GB→STA geçişi (R2e, 2024).
  GE: 2019 kesiti (IMF), ülke içi satış = mal brüt üretimi (UN AMA KD / KD-üretim oranı: tarım 0,55, imalat 0,33,
  madencilik-enerji 0,40; TÜİK YSHİ ve OECD oranlarıyla uyumlu) − toplam mal ihracatı (alt sınır %20 brüt üretim);
  Armington-CES, sabit donanım, E_j/Y_j sabit; kesin şapka cebiri (GEPPML koşullu ve tam donanım eşdeğeri),
  σ ∈ {5, 7}; karşı-olgu yalnız TR–AB27 ticaret maliyetini değiştirir (BK 2021'den beri GB dışında).

Çıktılar:
  veri/politika_cekim_katsayilar.csv  spesifikasyon × değişken: katsayı, küme-sağlam SH, z, p, %90 GA, % etki, N,
                                      çift ve küme sayısı; türetilmiş satırlar (kümülatif gecikme etkileri, farklar)
  veri/politika_cekim_senaryolar.csv  S2/S3/S4 (ve S3_TR, S3_BK) × yön: S0'a göre % değişim ve %90 GA, formül, etkinin
                                      zirve yılı ve kümülatif yolu (M2), değerlendirme; GE satırları (TR→AB, AB→TR,
                                      TR toplam ihracat/ithalat, TR ve AB reel GSYH vekili)
"""

import argparse
import datetime as dt
import io
import os
import warnings
import zipfile

import numpy as np
import pandas as pd
import pyfixest as pf

import nazik_http
import yollar

GRAVITY_URL = "https://www.cepii.fr/DATA_DOWNLOAD/gravity/data/Gravity_csv_V202211.zip"
DESTA = "https://www.designoftradeagreements.org/media/filer_public/"
DESTA_DOSYALAR = {
    "desta_indices_version_02_03.csv": DESTA + "0c/64/0c64ec71-5728-409f-91d8-64c324bf4400/desta_indices_version_02_03.csv",
    "desta_list_of_treaties_02_03.csv": DESTA + "5e/11/5e11943b-8871-4e8b-bcb2-8188aa83969c/desta_list_of_treaties_02_03.csv",
}
UN_AMA_URL = "https://unstats.un.org/unsd/amaapi/api/file/2"   # GDP/breakdown at current prices in US Dollars
GRAVITY_SUTUN = ["year", "iso3_o", "iso3_d", "country_exists_o", "country_exists_d", "fta_wto", "dist", "col_dep_ever", "gdp_o",
                 "tradeflow_comtrade_o", "tradeflow_comtrade_d", "tradeflow_baci", "manuf_tradeflow_baci",
                 "tradeflow_imf_o", "tradeflow_imf_d"]
ESKI = {"DDR", "SUN", "YUG", "CSK", "YMD", "ANT"}   # dağılan birimler örnek dışı (Hollanda Antilleri 2010)
ESLE = {"BEL": "BLX", "LUX": "BLX", "SCG": "SRB"}  # IMF'de BEL/LUX 1997 öncesi birleşik (CEPII'de yok)
TOPRAK_ISTISNA = {"TWN", "HKG", "MAC"}             # bağımlı toprak sayılmayan büyük ticaret ekonomileri
TR = "TUR"
GB_YIL = 1996                                      # 1/95 OKK, 1.1.1996

# AB üyeliği (ticaret açısından): giriş, çıkış (GB'nin geçiş dönemi 2020 sonuna kadar üye sayılır)
AB_UYELIK = {**{u: ("1958-01-01", None) for u in ("BLX", "DEU", "FRA", "ITA", "NLD")},
             **{u: ("1973-01-01", None) for u in ("DNK", "IRL")}, "GBR": ("1973-01-01", "2021-01-01"),
             "GRC": ("1981-01-01", None), "ESP": ("1986-01-01", None), "PRT": ("1986-01-01", None),
             **{u: ("1995-01-01", None) for u in ("AUT", "FIN", "SWE")},
             **{u: ("2004-05-01", None) for u in ("CYP", "CZE", "EST", "HUN", "LVA", "LTU", "MLT", "POL", "SVK", "SVN")},
             **{u: ("2007-01-01", None) for u in ("BGR", "ROU")}, "HRV": ("2013-07-01", None)}

# AB'nin üçüncü ülkelerle anlaşmaları: (ortak, kategori, ticaret hükümlerinin yürürlüğü, DESTA no, ad).
# DERIN: yeni nesil kapsamlı STA ve DCFTA (hizmet, yatırım, kamu alımı, rekabet, FMH, düzenleyici uyum);
# TEMEL: eski nesil, mal ağırlıklı STA ve Avrupa-Akdeniz OA. Tarihler: geçici uygulama dahil ilk yürürlük.
AB_ANLASMA = [
    ("KOR", "DERIN", "2011-07-01", "815", "AB–Kore STA"),
    ("PER", "DERIN", "2013-03-01", "810", "AB–Kolombiya/Peru/Ekvador TA"),
    ("COL", "DERIN", "2013-08-01", "810", "AB–Kolombiya/Peru/Ekvador TA"),
    ("ECU", "DERIN", "2017-01-01", "810", "AB–Kolombiya/Peru/Ekvador TA (Ekvador katılımı)"),
    *[(u, "DERIN", "2013-08-01", "799", "AB–Orta Amerika OA (ticaret ayağı)") for u in ("HND", "NIC", "PAN")],
    *[(u, "DERIN", "2013-10-01", "799", "AB–Orta Amerika OA (ticaret ayağı)") for u in ("CRI", "SLV")],
    ("GTM", "DERIN", "2013-12-01", "799", "AB–Orta Amerika OA (ticaret ayağı)"),
    ("GEO", "DERIN", "2014-09-01", "866", "AB–Gürcistan OA/DCFTA"),
    ("MDA", "DERIN", "2014-09-01", "872", "AB–Moldova OA/DCFTA"),
    ("UKR", "DERIN", "2016-01-01", "876", "AB–Ukrayna OA/DCFTA"),
    ("CAN", "DERIN", "2017-09-21", "848", "CETA"),
    ("JPN", "DERIN", "2019-02-01", "869", "AB–Japonya EPA"),
    ("SGP", "DERIN", "2019-11-21", "874", "AB–Singapur STA"),
    ("VNM", "DERIN", "2020-08-01", "877", "AB–Vietnam STA"),
    ("NZL", "DERIN", "2024-05-01", "966", "AB–Yeni Zelanda STA"),
    ("GBR", "AB_BK_TCA", "2021-01-01", "1046", "AB–BK Ticaret ve İşbirliği Anlaşması"),
    ("TUN", "TEMEL", "1998-03-01", "354", "AB–Tunus Avrupa-Akdeniz OA"),
    ("ISR", "TEMEL", "1975-07-01", "315", "AB–İsrail STA (1975), OA (2000)"),
    ("MAR", "TEMEL", "2000-03-01", "334", "AB–Fas Avrupa-Akdeniz OA"),
    ("JOR", "TEMEL", "2002-05-01", "318", "AB–Ürdün Avrupa-Akdeniz OA"),
    ("LBN", "TEMEL", "2003-03-01", "323", "AB–Lübnan geçici anlaşma (2003), OA (2006)"),
    ("EGY", "TEMEL", "2004-06-01", "304", "AB–Mısır Avrupa-Akdeniz OA"),
    ("DZA", "TEMEL", "2005-09-01", "17", "AB–Cezayir Avrupa-Akdeniz OA"),
    ("PSE", "TEMEL", "1997-07-01", "", "AB–Filistin geçici OA"),
    ("MEX", "TEMEL", "2000-07-01", "330", "AB–Meksika Küresel Anlaşma (STA)"),
    ("ZAF", "TEMEL", "2000-01-01", "347", "AB–Güney Afrika TDCA (2016'dan SADC EPA)"),
    ("CHL", "TEMEL", "2003-02-01", "202", "AB–Şili OA (2003)"),
    ("FRO", "TEMEL", "1997-01-01", "307", "AB–Faroe STA"),
    ("POL", "KATILIM", "1992-03-01", "337", "Avrupa Anlaşması (geçici anlaşma)"),
    ("HUN", "KATILIM", "1992-03-01", "312", "Avrupa Anlaşması (geçici anlaşma)"),
    ("CZE", "KATILIM", "1992-03-01", "280", "Avrupa Anlaşması (ÇSFC geçici anlaşması)"),
    ("SVK", "KATILIM", "1992-03-01", "344", "Avrupa Anlaşması (ÇSFC geçici anlaşması)"),
    ("ROU", "KATILIM", "1993-05-01", "340", "Avrupa Anlaşması (geçici anlaşma)"),
    ("BGR", "KATILIM", "1993-12-31", "148", "Avrupa Anlaşması (geçici anlaşma)"),
    *[(u, "KATILIM", "1995-01-01", n, "STA (1995), Avrupa Anlaşması (1998)") for u, n in
      (("EST", "306"), ("LVA", "320"), ("LTU", "326"))],
    ("SVN", "KATILIM", "1997-01-01", "346", "Avrupa Anlaşması (geçici anlaşma)"),
    ("CYP", "KATILIM", "1973-06-01", "278", "AET–Kıbrıs OA"),
    ("MLT", "KATILIM", "1971-04-01", "329", "AET–Malta OA"),
    ("MKD", "KATILIM", "2001-06-01", "328", "İstikrar ve Ortaklık Anlaşması (geçici)"),
    ("HRV", "KATILIM", "2002-03-01", "254", "İstikrar ve Ortaklık Anlaşması (geçici)"),
    ("ALB", "KATILIM", "2006-12-01", "8", "İstikrar ve Ortaklık Anlaşması (geçici)"),
    ("MNE", "KATILIM", "2008-01-01", "331", "İstikrar ve Ortaklık Anlaşması (geçici)"),
    ("BIH", "KATILIM", "2008-07-01", "130", "İstikrar ve Ortaklık Anlaşması (geçici)"),
    ("SRB", "KATILIM", "2010-02-01", "342", "İstikrar ve Ortaklık Anlaşması (geçici)"),
    ("XKX", "KATILIM", "2016-04-01", "975", "İstikrar ve Ortaklık Anlaşması"),
    *[(u, "EFTA", "1973-01-01", "350", "AET–İsviçre/Lihtenştayn STA (1973); AEA (LIE 1995)") for u in ("CHE", "LIE")],
    ("NOR", "EFTA", "1973-07-01", "336", "AET–Norveç STA (1973); AEA (1994)"),
    ("ISL", "EFTA", "1973-04-01", "313", "AET–İzlanda STA (1973); AEA (1994)"),
    ("AUT", "EFTA", "1973-01-01", "85", "AET–Avusturya STA (1995'te üyelik)"),
    ("FIN", "EFTA", "1974-01-01", "309", "AET–Finlandiya STA (1995'te üyelik)"),
    ("SWE", "EFTA", "1973-01-01", "349", "AET–İsveç STA (1995'te üyelik)"),
    *[(u, "EPA", "2008-12-29", "181", "CARIFORUM EPA") for u in
      ("ATG", "BHS", "BRB", "BLZ", "DMA", "DOM", "GRD", "GUY", "JAM", "KNA", "LCA", "VCT", "SUR", "TTO")],
    *[(u, "EPA", "2012-05-14", "1062", "Doğu ve Güney Afrika geçici EPA") for u in ("MDG", "MUS", "SYC", "ZWE")],
    ("COM", "EPA", "2019-02-07", "1062", "Doğu ve Güney Afrika geçici EPA"),
    ("PNG", "EPA", "2009-12-20", "979", "Pasifik geçici EPA"), ("FJI", "EPA", "2014-07-28", "979", "Pasifik geçici EPA"),
    ("WSM", "EPA", "2018-12-31", "979", "Pasifik geçici EPA"), ("SLB", "EPA", "2020-05-17", "979", "Pasifik geçici EPA"),
    ("CMR", "EPA", "2014-08-04", "", "AB–Kamerun geçici EPA"),
    ("CIV", "EPA", "2016-09-03", "252", "AB–Fildişi Sahili geçici EPA"),
    ("GHA", "EPA", "2016-12-15", "1113", "AB–Gana geçici EPA"),
    *[(u, "EPA", "2016-10-10", "978", "AB–SADC EPA") for u in ("BWA", "LSO", "NAM", "SWZ")],
    ("MOZ", "EPA", "2018-02-04", "978", "AB–SADC EPA"),
    ("KEN", "EPA", "2024-07-01", "1103", "AB–Kenya EPA"),
    ("AND", "EPA", "1991-07-01", "28", "AB–Andorra GB"), ("SMR", "EPA", "2002-04-01", "341", "AB–San Marino GB"),
]

# Türkiye'nin AB dışı ortaklarla STA'ları (ortak, yürürlük, sona erme). AB'ye katılan ülkelerle STA'lar üyelikle
# GB'ye dönüşür (otomatik). [D?]: tarih kaynağı Ticaret Bakanlığı STA listesi; yıl düzeyinde doğrulandı.
TR_STA = [
    *[(u, "1992-04-01", None) for u in ("CHE", "NOR", "ISL", "LIE")],
    *[(u, "1992-04-01", "1995-01-01") for u in ("AUT", "FIN", "SWE")],
    ("ISR", "1997-05-01", None), ("ROU", "1998-02-01", None), ("LTU", "1998-03-01", None),
    ("HUN", "1998-04-01", None), ("EST", "1998-07-01", None), ("CZE", "1998-09-01", None),
    ("SVK", "1998-09-01", None), ("BGR", "1999-01-01", None), ("POL", "2000-05-01", None),
    ("SVN", "2000-06-01", None), ("LVA", "2000-07-01", None), ("MKD", "2000-09-01", None),
    ("BIH", "2003-07-01", None), ("HRV", "2003-07-01", None), ("PSE", "2005-06-01", None),
    ("TUN", "2005-07-01", None), ("MAR", "2006-01-01", None), ("SYR", "2007-01-01", "2011-12-06"),
    ("EGY", "2007-03-01", None), ("ALB", "2008-05-01", None), ("GEO", "2008-11-01", None),
    ("MNE", "2010-03-01", None), ("SRB", "2010-09-01", None), ("CHL", "2011-03-01", None),
    ("JOR", "2011-03-01", "2018-11-22"), ("KOR", "2013-05-01", None), ("MUS", "2013-06-01", None),
    ("MYS", "2015-08-01", None), ("MDA", "2016-11-01", None), ("FRO", "2017-10-01", None),
    ("SGP", "2017-10-01", None), ("XKX", "2019-09-01", None), ("GBR", "2021-01-01", None),
    ("ARE", "2023-09-01", None),
]
# Romanya'nın 2007 öncesi AB dışı STA'ları (CEPII fta_wto'da Romanya'nın bütün çiftleri 0): EFTA, CEFTA, Moldova, İsrail
ROU_STA = [*[(u, "1993-05-01") for u in ("CHE", "NOR", "ISL", "LIE")],
           *[(u, "1997-07-01") for u in ("POL", "HUN", "CZE", "SVK", "SVN")], ("BGR", "1999-01-01"),
           ("HRV", "2003-03-01"), ("MDA", "1995-01-01"), ("ISR", "2001-07-01")]

KAT_DEGISKEN = {"DERIN": "AB_STA_DERIN", "TEMEL": "AB_STA_TEMEL", "KATILIM": "AB_KATILIM", "EFTA": "AB_EFTA",
                "EPA": "AB_EPA", "AB_BK_TCA": "AB_BK_TCA"}
TEMEL_DEG = ["GB_TR_AB", "GB_AB_TR", "AB_STA_DERIN", "AB_STA_TEMEL", "AB_KATILIM", "AB_EFTA", "AB_EPA",
             "AB_UYELIK", "RTA_DIGER"]
Z90 = 1.6448536269514722


# ----------------------------------------------------------------------------------------------- indirme
def indir(url, yol, akis=False):
    """Önbellekte yoksa indirir; büyük dosyalar parça parça (yarım kalan .part dosyası sürdürülür)."""
    bulunan = yollar.bul(yol)  # pakette .gz olarak da durabilir
    if bulunan:
        return bulunan
    yollar.indirme_izni(url)
    os.makedirs(os.path.dirname(yol), exist_ok=True)
    if not akis:
        r = nazik_http.get(url, timeout=600)
        r.raise_for_status()
        with open(yol, "wb") as f:
            f.write(r.content)
        return yol
    gecici = yol + ".part"
    for _ in range(6):
        bas = os.path.getsize(gecici) if os.path.exists(gecici) else 0
        try:
            with nazik_http.SESSION.get(url, stream=True, timeout=600,
                                        headers={"Range": f"bytes={bas}-"} if bas else {}) as r:
                if r.status_code not in (200, 206):
                    raise RuntimeError(f"{url}: HTTP {r.status_code}")
                with open(gecici, "ab" if r.status_code == 206 else "wb") as f:
                    for parca in r.iter_content(1 << 20):
                        f.write(parca)
            os.replace(gecici, yol)
            return yol
        except (OSError, RuntimeError, nazik_http.requests.RequestException):
            continue
    raise RuntimeError(f"indirilemedi: {url}")


def gravity_oku(c):
    """CEPII Gravity'den 1980 sonrası ve gerekli sütunları parquet önbelleğine alır."""
    pq = os.path.join(c, "gravity_V202211_1980_v4.parquet")
    if not os.path.exists(pq):
        z = zipfile.ZipFile(indir(GRAVITY_URL, os.path.join(c, "cepii", "Gravity_csv_V202211.zip"), akis=True))
        parcalar = []
        with z.open("Gravity_V202211.csv") as f:
            for ch in pd.read_csv(f, usecols=GRAVITY_SUTUN, chunksize=1_000_000, encoding="latin-1",
                                  dtype={"iso3_o": str, "iso3_d": str}):
                parcalar.append(ch[ch.year >= 1980])
        pd.concat(parcalar, ignore_index=True).to_parquet(pq, index=False)
        ulkeler = pd.read_csv(io.BytesIO(z.read("Countries_V202211.csv")), encoding="latin-1", keep_default_na=False)
        ulkeler.to_csv(os.path.join(c, "gravity_ulkeler.csv"), index=False)
    return pd.read_parquet(pq), pd.read_csv(os.path.join(c, "gravity_ulkeler.csv"), keep_default_na=False)


def desta_oku(c):
    """DESTA derinlik endeksleri (anlaşma no → depth_index, depth_rasch)."""
    for ad, url in DESTA_DOSYALAR.items():
        indir(url, os.path.join(c, "desta", ad))
    ix = pd.read_csv(os.path.join(c, "desta", "desta_indices_version_02_03.csv"), encoding="latin-1", dtype={"number": str})
    return ix.set_index("number")[["name", "depth_index", "depth_rasch"]]


# ------------------------------------------------------------------------------------------ panel kurma
def yuruluk_yili(tarih):
    """1 Temmuz kuralı: anlaşma t yılının 1 Temmuz'unda yürürlükteyse t ilk etkin yıldır."""
    d = dt.date.fromisoformat(tarih)
    return d.year if (d.month, d.day) <= (7, 1) else d.year + 1


def akim(g, kaynak):
    """Kaynağa göre ikili akım (bin $): ithalatçı beyanı, yoksa ihracatçı aynası (BACI zaten uzlaştırılmış)."""
    if kaynak in ("baci", "baci_imalat"):
        x = g.tradeflow_baci if kaynak == "baci" else g.manuf_tradeflow_baci
        return x.where(x > 0)
    d, o = (g.tradeflow_imf_d, g.tradeflow_imf_o) if kaynak == "imf" else (g.tradeflow_comtrade_d, g.tradeflow_comtrade_o)
    return d.where(d > 0, o.where(o > 0))


def uyumlastir(g):
    """Var olan birimler; DEU.1/DEU.2 vb. ISO3'te birleşir, BEL+LUX → BLX, SCG → SRB; eski birimler düşer."""
    g = g[(g.country_exists_o == 1) & (g.country_exists_d == 1) & ~g.iso3_o.isin(ESKI) & ~g.iso3_d.isin(ESKI)].copy()
    g["o"] = g.iso3_o.replace(ESLE)
    g["d"] = g.iso3_d.replace(ESLE)
    g = g[g.o != g.d]
    for k in ("imf", "comtrade", "baci", "baci_imalat"):
        g["x_" + k] = akim(g, k)
    # IMF'de Belçika-Lüksemburg 1997 öncesi boş: Comtrade (BLX olarak bildirilmiş) ile doldurulur
    blx = (g.year <= 1996) & (g.iso3_o.isin(["BEL", "LUX"]) | g.iso3_d.isin(["BEL", "LUX"]))
    g.loc[blx, "x_imf"] = g.loc[blx, "x_comtrade"]
    anahtar = ["year", "o", "d"]
    tablo = g.groupby(anahtar)[["x_imf", "x_comtrade", "x_baci", "x_baci_imalat"]].sum(min_count=1)
    tablo["fta_wto"] = g.groupby(anahtar).fta_wto.max()
    tablo["dist"] = g.groupby(anahtar).dist.mean()
    tablo["kolonyal"] = g.groupby(anahtar).col_dep_ever.max()
    return tablo.reset_index()


def gsyh_tablosu(g):
    """CEPII GSYH (milyon $, cari) ülke-yıl; BEL+LUX toplanır (GE'de UN AMA'da olmayan ülkeler için yedek)."""
    x = g[g.country_exists_o == 1].groupby(["year", "iso3_o"]).gdp_o.first().reset_index()
    x["u"] = x.iso3_o.replace(ESLE)
    return x.groupby(["year", "u"]).gdp_o.sum(min_count=1) / 1e3


def ulke_sec(t, ulkeler, n):
    """2000–2020 ortalama toplam ticarete (IMF) göre ilk n egemen ekonomi + AB (tarihsel) + TR."""
    bagimli = set(ulkeler.loc[ulkeler.heg_iso3_2020.astype(str).str.len() > 0, "iso3"]) - TOPRAK_ISTISNA
    s = t[(t.year >= 2000) & (t.year <= 2020)]
    hacim = (s.groupby(["o", "year"]).x_imf.sum().add(s.groupby(["d", "year"]).x_imf.sum(), fill_value=0)
             .groupby(level=0).mean().sort_values(ascending=False))
    hacim = hacim[~hacim.index.isin(bagimli)]
    secilen = list(hacim.index[:n])
    for u in list(AB_UYELIK) + [TR]:
        if u not in secilen:
            secilen.append(u)
    return secilen, hacim


def panel(t, ulkeler_secili, kaynak, yillar):
    """Seçili ülke ve yıllar için kare panel; iki taraf da o yıl veri veriyorsa eksik akım = 0."""
    p = t[t.year.isin(yillar) & t.o.isin(ulkeler_secili) & t.d.isin(ulkeler_secili)].copy()
    p["X"] = p["x_" + kaynak]
    poz = p[p.X > 0]
    p = (p.merge(poz[["year", "o"]].drop_duplicates().assign(_ao=1), on=["year", "o"], how="left")
          .merge(poz[["year", "d"]].drop_duplicates().assign(_ad=1), on=["year", "d"], how="left"))
    p = p[p._ao.notna() & p._ad.notna()].drop(columns=["_ao", "_ad"])
    p["X"] = p.X.fillna(0.0) / 1e3          # milyon $
    return p.reset_index(drop=True)


# ------------------------------------------------------------------------------------------ kuklalar
def uyelik_tablosu(yillar):
    s = []
    for u, (bas, bit) in AB_UYELIK.items():
        y0 = yuruluk_yili(bas)
        y1 = yuruluk_yili(bit) if bit else 9999
        s += [(u, y, y0) for y in yillar if y0 <= y < y1]
    return pd.DataFrame(s, columns=["u", "year", "ab_bas"])


def anlasma_tablosu(yillar, liste, kat=None):
    s = []
    for r in liste:
        u, bas, bit = (r[0], r[2], None) if kat else (r[0], r[1], r[2] if len(r) > 2 else None)
        y0 = yuruluk_yili(bas)
        y1 = yuruluk_yili(bit) if bit else 9999
        s += [(u, y, y0, r[1] if kat else "RTA") for y in yillar if y0 <= y < y1]
    return pd.DataFrame(s, columns=["u", "year", "bas", "kat"])


def rta_suresi(t):
    """CEPII fta_wto için kesintisiz dönemin başlangıç yılı (1980'de başlayanlar 1960 sayılır)."""
    a = t[["year", "o", "d", "fta_wto"]].sort_values(["o", "d", "year"]).copy()
    a["f"] = a.fta_wto.fillna(0).astype(int)
    yeni = (a.f != a.groupby(["o", "d"]).f.shift().fillna(-1)).astype(int)
    a["blok"] = yeni.groupby([a.o, a.d]).cumsum()
    a["rta_bas"] = a.groupby(["o", "d", "blok"]).year.transform("min")
    a.loc[a.rta_bas == a.year.min(), "rta_bas"] = 1960
    return a[["year", "o", "d", "rta_bas"]]


def ab_listesi(siniflama):
    """AB anlaşma listesi; sınıflama varyantları: ana, desta (Rasch ≥ 1,5: Şili ve CARIFORUM derin),
    dar (derin = yalnız DCFTA'lar, Kore, Japonya, CETA, Singapur, Vietnam; diğer yeni nesil ayrı kukla)."""
    if siniflama == "desta":
        return [(r[0], "DERIN" if r[3] in ("202", "181") else r[1], *r[2:]) for r in AB_ANLASMA]
    if siniflama == "dar":
        dar = {"KOR", "GEO", "MDA", "UKR", "CAN", "JPN", "SGP", "VNM", "NZL"}
        return [(r[0], "DERIN_DIGER" if (r[1] == "DERIN" and r[0] not in dar) else r[1], *r[2:]) for r in AB_ANLASMA]
    return AB_ANLASMA


def kuklalar(p, rs, siniflama="ana"):
    """Her çift-yıla tek bir anlaşma kategorisi ve o kategorinin başlangıç yılı atanır (öncelik sırası:
    AB içi > TR–AB GB > AB–üçüncü ülke tablosu > TR STA tablosu > ROU düzeltmesi > CEPII fta_wto)."""
    yillar = range(1950, 2030)
    uy = uyelik_tablosu(yillar)
    ab = anlasma_tablosu(yillar, ab_listesi(siniflama), kat=True)
    tr = anlasma_tablosu(yillar, TR_STA)
    ro = anlasma_tablosu(yillar, [(u, b, "2007-01-01") for u, b in ROU_STA])
    for tablo in (uy, ab, tr, ro):
        assert not tablo.duplicated(["u", "year"]).any()
    p = p.merge(uy.rename(columns={"u": "o", "ab_bas": "ab_o"}), on=["o", "year"], how="left")
    p = p.merge(uy.rename(columns={"u": "d", "ab_bas": "ab_d"}), on=["d", "year"], how="left")
    p["ab_ortak"] = np.where(p.ab_o.notna(), p.d, p.o)
    p["tr_ortak"] = np.where(p.o == TR, p.d, p.o)
    p["ro_ortak"] = np.where(p.o == "ROU", p.d, p.o)
    p = p.merge(ab.rename(columns={"u": "ab_ortak", "bas": "ab_anl_bas", "kat": "ab_kat"}), on=["ab_ortak", "year"], how="left")
    p = p.merge(tr.rename(columns={"u": "tr_ortak", "bas": "tr_bas"})[["tr_ortak", "year", "tr_bas"]], on=["tr_ortak", "year"], how="left")
    p = p.merge(ro.rename(columns={"u": "ro_ortak", "bas": "ro_bas"})[["ro_ortak", "year", "ro_bas"]], on=["ro_ortak", "year"], how="left")
    p = p.merge(rs, on=["year", "o", "d"], how="left")
    o_ab, d_ab = p.ab_o.notna().to_numpy(), p.ab_d.notna().to_numpy()
    o_tr, d_tr = (p.o == TR).to_numpy(), (p.d == TR).to_numpy()
    tr_cift, tek_ab = o_tr | d_tr, o_ab ^ d_ab
    ro_cift = ((p.o == "ROU") | (p.d == "ROU")).to_numpy()
    eu_bas = np.where(o_ab, p.ab_o, p.ab_d)
    yil = p.year.to_numpy()
    kat = np.full(len(p), "YOK", dtype=object)
    bas = np.full(len(p), np.nan)
    kosullar = [  # (maske, kategori, başlangıç)
        (o_ab & d_ab, "AB_UYELIK", np.fmax(p.ab_o, p.ab_d)),
        (tek_ab & o_tr & (yil >= GB_YIL), "GB_TR_AB", np.fmax(GB_YIL, eu_bas)),
        (tek_ab & d_tr & (yil >= GB_YIL), "GB_AB_TR", np.fmax(GB_YIL, eu_bas)),
        (tek_ab & ~tr_cift & p.ab_kat.notna().to_numpy(), None, np.fmax(p.ab_anl_bas, eu_bas)),
        (~o_ab & ~d_ab & tr_cift & (p.tr_ortak == "GBR").to_numpy() & (yil >= 2021), "TR_BK_STA", p.tr_bas),
        (~o_ab & ~d_ab & tr_cift & p.tr_bas.notna().to_numpy(), "RTA_DIGER", p.tr_bas),
        (~o_ab & ~d_ab & ~tr_cift & ro_cift & p.ro_bas.notna().to_numpy(), "RTA_DIGER", p.ro_bas),
        (~o_ab & ~d_ab & ~tr_cift & ~ro_cift & (p.fta_wto == 1).to_numpy(), "RTA_DIGER", p.rta_bas),
    ]
    atanmis = np.zeros(len(p), dtype=bool)
    for m, k, b in kosullar:
        m = m & ~atanmis
        kat[m] = p.ab_kat.map(lambda x: KAT_DEGISKEN.get(x, "AB_" + str(x))).to_numpy()[m] if k is None else k
        bas[m] = np.asarray(b, dtype=float)[m]
        atanmis |= m
    p["kat"], p["kat_bas"] = kat, bas
    p["sure"] = p.year - p.kat_bas
    for k in ["GB_TR_AB", "GB_AB_TR", "AB_UYELIK", "RTA_DIGER", "TR_BK_STA", "AB_DERIN_DIGER",
              *KAT_DEGISKEN.values()]:
        p[k] = (p.kat == k).astype(float)
    for k in ("AB_STA_DERIN", "AB_STA_TEMEL"):       # yönlü STA kuklaları
        p[k + "_AB_ORT"] = p[k] * o_ab
        p[k + "_ORT_AB"] = p[k] * d_ab
    # GB öncüsü: önümüzdeki 1–4 yıl içinde GB'ye girecek TR–ülke çiftleri (beklenti/ters nedensellik sınaması)
    gb_bas = np.fmax(GB_YIL, p.tr_ortak.map(uy.groupby("u").ab_bas.min()).to_numpy(dtype=float))
    on = tr_cift & ~np.isin(kat, ["GB_TR_AB", "GB_AB_TR"]) & (gb_bas - yil > 0) & (gb_bas - yil <= 4)
    p["GB_TR_AB_ONCU4"] = (on & o_tr).astype(float)
    p["GB_AB_TR_ONCU4"] = (on & d_tr).astype(float)
    # GB'nin 1996 girişi (AB15) ile genişleme girişlerini ayırmak için
    ab15 = p.tr_ortak.isin(["BLX", "DEU", "FRA", "ITA", "NLD", "DNK", "IRL", "GBR", "GRC", "ESP", "PRT", "AUT",
                            "FIN", "SWE"]).to_numpy()
    for k in ("GB_TR_AB", "GB_AB_TR"):
        p[k + "_AB15"] = p[k] * ab15
        p[k + "_YENI"] = p[k] * ~ab15
    return p.drop(columns=["ab_ortak", "ro_ortak", "ab_anl_bas", "tr_bas", "ro_bas"])


def gecikme_ekle(p, degiskenler, gecikmeler):
    """Aşamalı etki: D_Lk = D × 1[yürürlükten bu yana geçen yıl ≥ k] (kümülatif artış katsayıları)."""
    yeni = []
    for v in degiskenler:
        for k in gecikmeler:
            ad = f"{v}_L{k}"
            p[ad] = p[v] * (p.sure >= k)
            yeni.append(ad)
    return yeni


# ------------------------------------------------------------------------------------------- tahmin
def tahmin(p, degiskenler, kume="cift_yonsuz"):
    """PPML, ihracatçı-yıl + ithalatçı-yıl + yönlü çift sabit etkileri; yönsüz çift kümeli SH."""
    p = p.copy()
    p["it"] = pd.factorize(p.o + "_" + p.year.astype(str))[0]
    p["jt"] = pd.factorize(p.d + "_" + p.year.astype(str))[0]
    p["ij"] = pd.factorize(p.o + "_" + p.d)[0]
    p["cift_yonsuz"] = pd.factorize(np.minimum(p.o, p.d) + "_" + np.maximum(p.o, p.d))[0]
    # tek bir çift-yıl dışında değişmeyen ya da hep sıfır olan kuklalar çıkarılır (tanımlanamaz)
    deg = [v for v in degiskenler if p[v].abs().sum() > 0]
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        m = pf.fepois(f"X ~ {' + '.join(deg)} | it + jt + ij", data=p, vcov={"CRV1": kume},
                      iwls_tol=1e-10, iwls_maxiter=100, fixef_tol=1e-10)
    adlar = [str(a) for a in m._coefnames]
    b = pd.Series(np.asarray(m.coef()), index=adlar)
    V = pd.DataFrame(np.asarray(m._vcov), index=adlar, columns=adlar)
    # tahminde kullanılan örnek: çift FE'si tanımlı (bütünü sıfır olmayan) çiftler
    return dict(b=b, V=V, N=int(m._N), G=int(np.max(m._G)) if np.ndim(m._G) else int(m._G),
                n_cift=int(p.loc[p.groupby("ij").X.transform("sum") > 0, "ij"].nunique()))


def bilesim(sonuc, agirlik):
    """Doğrusal bileşim w'b ve SH'si (delta yöntemi)."""
    w = pd.Series(agirlik, dtype=float)
    w = w[w.index.isin(sonuc["b"].index)]
    deger = float((w * sonuc["b"][w.index]).sum())
    se = float(np.sqrt(w.values @ sonuc["V"].loc[w.index, w.index].values @ w.values))
    return deger, se


# ------------------------------------------------------------------------------- 2024 uzatması (BACI)
def baci_oku(dizin, yil):
    """Yerel BACI HS17 V202601 parquet → ikili toplam (bin $), ISO3 (S19 = Tayvan, BEL+LUX = BLX)."""
    import pyarrow.parquet as pq
    kod = pd.read_csv(os.path.join(dizin, "country_codes_V202601.csv"), dtype=str, keep_default_na=False)
    iso = dict(zip(kod.country_code.astype(int), kod.country_iso3.replace({"S19": "TWN"}).replace(ESLE)))
    ozet = os.path.join(dizin, f"baci_hs17_ikili_toplam_{yil}.parquet")  # pakette: kod/girdi_hazirla.py
    if os.path.exists(ozet):
        b = pd.read_parquet(ozet)
    else:
        b = pq.read_table(os.path.join(dizin, "all_countries", f"BACI_HS17_Y{yil}_V202601.parquet"),
                          columns=["i", "j", "v"]).to_pandas()
    b = b.groupby(["i", "j"], as_index=False).v.sum()
    b["o"], b["d"] = b.i.map(iso), b.j.map(iso)
    b = b[b.o != b.d].groupby(["o", "d"], as_index=False).v.sum()
    b["year"] = yil
    return b


def tabloyu_uzat(t, baci_dizin):
    """2022–2024 satırları: fta_wto, uzaklık ve sömürge bağı 2021'den taşınır; 2024 akımı BACI HS17'den."""
    son = t[t.year == 2021].copy()
    ek = []
    for y in (2022, 2023, 2024):
        s = son.copy()
        s["year"] = y
        s[["x_imf", "x_comtrade", "x_baci", "x_baci_imalat"]] = np.nan
        ek.append(s)
    u = pd.concat([t] + ek, ignore_index=True)
    b24 = baci_oku(baci_dizin, 2024).rename(columns={"v": "x_b24"})
    u = u.merge(b24, on=["year", "o", "d"], how="left")
    u.loc[u.year == 2024, "x_baci"] = u.loc[u.year == 2024, "x_b24"]
    kontrol = None
    if os.path.exists(os.path.join(baci_dizin, "all_countries", "BACI_HS17_Y2020_V202601.parquet")):
        b20 = baci_oku(baci_dizin, 2020).merge(t[t.year == 2020][["o", "d", "x_baci"]], on=["o", "d"])
        b20 = b20[(b20.v > 0) & (b20.x_baci > 0)]
        w = b20.x_baci / b20.x_baci.sum()
        r = np.log(b20.v / b20.x_baci)
        kontrol = dict(agirlikli_log_fark=float((w * r).sum()), agirlikli_mutlak_sapma=float((w * r.abs()).sum()),
                       korelasyon=float(np.corrcoef(np.log(b20.v), np.log(b20.x_baci))[0, 1]))
    return u.drop(columns=["x_b24"]), kontrol


# ------------------------------------------------------------------------------------ spesifikasyonlar
YIL4 = list(range(1988, 2021, 4))
YIL4_B = list(range(1996, 2021, 4))
CEEC = ["ROU", "LTU", "HUN", "EST", "CZE", "SVK", "BGR", "POL", "SVN", "LVA", "HRV"]
YAPTIRIM = ["BLX", "DEU", "FRA", "ITA", "NLD", "DNK", "IRL", "GRC", "ESP", "PRT", "AUT", "FIN", "SWE", "CYP", "CZE",
            "EST", "HUN", "LVA", "LTU", "MLT", "POL", "SVK", "SVN", "BGR", "ROU", "HRV", "GBR", "USA", "CAN", "JPN",
            "AUS", "NZL", "NOR", "CHE", "KOR", "ISL"]


def yil_etkilesimi(p, sutun, onek, yillar):
    """sütun × yıl kuklaları (ilk yıl taban)."""
    adlar = []
    for y in yillar[1:]:
        p[f"{onek}_{y}"] = p[sutun].fillna(0) * (p.year == y)
        adlar.append(f"{onek}_{y}")
    return adlar


def ek_sta_oncu(p):
    """AB STA öncüleri: önümüzdeki 1–4 yıl içinde yürürlüğe girecek AB–ortak anlaşmaları."""
    ab = anlasma_tablosu(range(1950, 2030), AB_ANLASMA, kat=True)
    ortak = np.where(p.ab_o.notna(), p.d, p.o)
    bas = pd.Series(ortak).map(ab.groupby("u").bas.min()).to_numpy(dtype=float)
    kat = pd.Series(ortak).map(ab.groupby("u").kat.first()).to_numpy()
    tek = (p.ab_o.notna() ^ p.ab_d.notna()).to_numpy() & (p.o != TR).to_numpy() & (p.d != TR).to_numpy()
    fark = bas - p.year.to_numpy()
    for k, ad in (("TEMEL", "AB_STA_TEMEL_ONCU4"), ("DERIN", "AB_STA_DERIN_ONCU4")):
        p[ad] = (tek & (kat == k) & (fark > 0) & (fark <= 4)).astype(float)
    return ["AB_STA_TEMEL_ONCU4", "AB_STA_DERIN_ONCU4"]


def ek_genisleme(p):
    """TR–(sonradan AB üyesi) STA'ları ayrı; GB etkisi AB15 (1996) ve genişleme girişi olarak ayrı."""
    trc = (((p.o == TR) & p.d.isin(CEEC)) | ((p.d == TR) & p.o.isin(CEEC))).to_numpy()
    p["TR_STA_ADAY_TR_X"] = p.RTA_DIGER * trc * (p.o == TR)
    p["TR_STA_ADAY_X_TR"] = p.RTA_DIGER * trc * (p.d == TR)
    p["RTA_DIGER_X"] = p.RTA_DIGER * ~trc
    return ["GB_TR_AB_AB15", "GB_TR_AB_YENI", "GB_AB_TR_AB15", "GB_AB_TR_YENI", "AB_STA_DERIN", "AB_STA_TEMEL",
            "AB_KATILIM", "AB_EFTA", "AB_EPA", "AB_UYELIK", "RTA_DIGER_X", "TR_STA_ADAY_TR_X", "TR_STA_ADAY_X_TR"]


def ek_uzatma(p):
    """2024 uzatması: AB–BK TCA, TR–BK STA (yönlü), Ukrayna savaşı/ATM ve Rusya yaptırımları kontrolleri."""
    p["TR_BK_STA_TR_GBR"] = p.TR_BK_STA * (p.o == TR)
    p["TR_BK_STA_GBR_TR"] = p.TR_BK_STA * (p.d == TR)
    ukr = ((p.o == "UKR") & p.ab_d.notna()) | ((p.d == "UKR") & p.ab_o.notna())
    p["AB_UKR_2022SONRASI"] = (ukr & (p.year >= 2022)).astype(float)
    rus = ((p.o.isin(["RUS", "BLR"]) & p.d.isin(YAPTIRIM)) | (p.d.isin(["RUS", "BLR"]) & p.o.isin(YAPTIRIM)))
    p["RUS_YAPTIRIM_2022SONRASI"] = (rus & (p.year >= 2022)).astype(float)
    return ["AB_BK_TCA", "TR_BK_STA_TR_GBR", "TR_BK_STA_GBR_TR", "AB_UKR_2022SONRASI", "RUS_YAPTIRIM_2022SONRASI"]


STA_GRUP = {  # anlaşma grubu → (kaynak kukla, ortaklar)
    "H_KORE": ("AB_STA_DERIN", ["KOR"]), "H_ORTA_AMERIKA": ("AB_STA_DERIN", ["HND", "NIC", "PAN", "CRI", "SLV", "GTM"]),
    "H_AND": ("AB_STA_DERIN", ["COL", "PER", "ECU"]), "H_DCFTA": ("AB_STA_DERIN", ["GEO", "MDA", "UKR"]),
    "H_KANADA": ("AB_STA_DERIN", ["CAN"]), "H_JAPONYA": ("AB_STA_DERIN", ["JPN"]),
    "H_SINGAPUR_VIETNAM": ("AB_STA_DERIN", ["SGP", "VNM"]), "H_YENI_ZELANDA": ("AB_STA_DERIN", ["NZL"]),
    "H_AVRUPA_AKDENIZ": ("AB_STA_TEMEL", ["TUN", "MAR", "JOR", "LBN", "EGY", "DZA", "PSE"]),
    "H_MEKSIKA": ("AB_STA_TEMEL", ["MEX"]), "H_GUNEY_AFRIKA": ("AB_STA_TEMEL", ["ZAF"]),
    "H_SILI": ("AB_STA_TEMEL", ["CHL"]), "H_ISRAIL_FAROE": ("AB_STA_TEMEL", ["ISR", "FRO"]),
}


def degiskenler(p, tur):
    """Spesifikasyon türüne göre açıklayıcılar (gerekli sütunları da ekler)."""
    v = list(TEMEL_DEG)
    if tur == "yonlu_sta":
        return [x for x in v if x not in ("AB_STA_DERIN", "AB_STA_TEMEL")] + \
               ["AB_STA_DERIN_AB_ORT", "AB_STA_DERIN_ORT_AB", "AB_STA_TEMEL_AB_ORT", "AB_STA_TEMEL_ORT_AB"]
    if tur == "gecikmeli":
        return v + gecikme_ekle(p, ["GB_TR_AB", "GB_AB_TR", "AB_STA_DERIN", "AB_STA_TEMEL"], [4, 8, 12])
    if tur == "gb_olay":
        return v + gecikme_ekle(p, ["GB_TR_AB", "GB_AB_TR"], [4, 8, 12, 16, 20, 24]) + \
               gecikme_ekle(p, ["AB_STA_DERIN", "AB_STA_TEMEL"], [4, 8, 12])
    if tur == "oncu":
        return v + ["GB_TR_AB_ONCU4", "GB_AB_TR_ONCU4"] + ek_sta_oncu(p)
    if tur == "genisleme":
        return ek_genisleme(p)
    if tur == "uzaklik_yil":
        p["lndist"] = np.log(p.dist)
        return v + yil_etkilesimi(p, "lndist", "LNDIST", sorted(p.year.unique()))
    if tur == "kolonyal_yil":
        return v + yil_etkilesimi(p, "kolonyal", "KOLONYAL", sorted(p.year.unique()))
    if tur == "ab_yil":
        return v + yil_etkilesimi(p, "AB_UYELIK", "AB_UYELIK", sorted(p.year.unique()))
    if tur == "dar":
        return v + ["AB_DERIN_DIGER"]
    if tur == "uzatma":
        return v + ek_uzatma(p)
    if tur == "heterojen":   # anlaşma grubuna göre ayrı AB STA etkileri
        ortak = np.where(p.ab_o.notna(), p.d, p.o)
        for ad, (k, L) in STA_GRUP.items():
            p[ad] = p[k] * np.isin(ortak, L)
        # Rusya'nın komşularla ticaret kopuşları (UKR 2014+, GEO 2006+ ambargo/savaş, MDA 2014+): DCFTA etkisini
        # yeniden yönelimden ayırmak için çift-yıl kontrolü
        ru = {"UKR": 2014, "GEO": 2006, "MDA": 2014}
        kom = np.where(p.o == "RUS", p.d, np.where(p.d == "RUS", p.o, ""))
        p["RUS_KOMSU_KOPUS"] = (pd.Series(kom).map(ru).to_numpy(dtype=float) <= p.year.to_numpy()).astype(float)
        return [x for x in v if x not in ("AB_STA_DERIN", "AB_STA_TEMEL")] + list(STA_GRUP) + ["RUS_KOMSU_KOPUS"]
    return v


SPEC = [  # etiket, açıklama, kaynak, yıllar, değişken türü, sınıflama, ülke kümesi, küme, uzatma
    ("M1_ana", "Ana model: IMF DOTS, 1988–2020, 4 yıllık aralık, statik kuklalar", "imf", YIL4, "ana", "ana", "ilk150", "cift_yonsuz"),
    ("M1b_yonlu_sta", "M1 + AB STA etkileri yöne göre (AB→ortak, ortak→AB)", "imf", YIL4, "yonlu_sta", "ana", "ilk150", "cift_yonsuz"),
    ("M2_gecikmeli", "M1 + aşamalı etki: GB ve AB STA'ları için 4, 8, 12 yıl gecikmeler (kümülatif artış)", "imf", YIL4, "gecikmeli", "ana", "ilk150", "cift_yonsuz"),
    ("M3_gb_olay", "M1 + GB olay çalışması (0–24 yıl) ve STA gecikmeleri (4, 8, 12)", "imf", YIL4, "gb_olay", "ana", "ilk150", "cift_yonsuz"),
    ("M4_oncu", "M1 + öncü kuklalar (yürürlükten önceki 1–4 yıl): beklenti/ön-eğilim sınaması", "imf", YIL4, "oncu", "ana", "ilk150", "cift_yonsuz"),
    ("M5_genisleme", "GB etkisi AB15 (1996) ve genişleme (2004/2007/2013) girişlerine göre; TR–aday STA'ları ayrı", "imf", YIL4, "genisleme", "ana", "ilk150", "cift_yonsuz"),
    ("M6_heterojen", "M1 + AB STA etkileri anlaşma grubuna göre (Kore, Orta Amerika, And, DCFTA, Kanada, Japonya, ...)", "imf", YIL4, "heterojen", "ana", "ilk150", "cift_yonsuz"),
    ("R1_2020_haric", "Sağlamlık (i): 2020 (COVID) hariç, 1988–2016", "imf", YIL4[:-1], "ana", "ana", "ilk150", "cift_yonsuz"),
    ("R2_comtrade", "Sağlamlık (ii): UN Comtrade akımları, 1988–2020", "comtrade", YIL4, "ana", "ana", "ilk150", "cift_yonsuz"),
    ("R2b_imf_1996", "Sağlamlık (ii): IMF, 1996–2020 (BACI ile aynı pencere; GB yalnız genişlemeyle tanımlı)", "imf", YIL4_B, "ana", "ana", "ilk150", "cift_yonsuz"),
    ("R2c_baci_1996", "Sağlamlık (ii): BACI toplam mal, 1996–2020", "baci", YIL4_B, "ana", "ana", "ilk150", "cift_yonsuz"),
    ("R2d_baci_imalat_1996", "Sağlamlık (ii): BACI imalat (CEPII manuf_tradeflow_baci), 1996–2020", "baci_imalat", YIL4_B, "ana", "ana", "ilk150", "cift_yonsuz"),
    ("R2e_baci_2024", "Uzatma: BACI 1996–2020 + BACI HS17 V202601 2024; AB–BK TCA, TR–BK STA, Ukrayna/Rusya kontrolleri", "baci", YIL4_B + [2024], "uzatma", "ana", "ilk150", "cift_yonsuz"),
    ("R3a_3yil", "Sağlamlık (iii): 3 yıllık aralık, 1987–2020", "imf", list(range(1987, 2021, 3)), "ana", "ana", "ilk150", "cift_yonsuz"),
    ("R3b_5yil", "Sağlamlık (iii): 5 yıllık aralık, 1990–2020", "imf", list(range(1990, 2021, 5)), "ana", "ana", "ilk150", "cift_yonsuz"),
    ("R3c_yillik", "Sağlamlık (iii): yıllık veri, 1988–2020", "imf", list(range(1988, 2021)), "ana", "ana", "ilk150", "cift_yonsuz"),
    ("R4_desta", "Sınıflama: DESTA Rasch derinliği ≥ 1,5 (Şili ve CARIFORUM derin sayılır)", "imf", YIL4, "ana", "desta", "ilk150", "cift_yonsuz"),
    ("R5_dar_derin", "Sınıflama: derin = DCFTA'lar, Kore, Japonya, CETA, Singapur, Vietnam; diğer yeni nesil ayrı", "imf", YIL4, "dar", "dar", "ilk150", "cift_yonsuz"),
    ("R6_uzaklik_yil", "Kontrol: ln(uzaklık) × yıl (küreselleşme/uzaklık esnekliği değişimi)", "imf", YIL4, "uzaklik_yil", "ana", "ilk150", "cift_yonsuz"),
    ("R7_kolonyal_yil", "Kontrol: sömürge bağı × yıl (sömürge ticaretinin aşınması)", "imf", YIL4, "kolonyal_yil", "ana", "ilk150", "cift_yonsuz"),
    ("R8_ab_yil", "Kontrol: AB içi etki yıla göre değişken (tek pazar, avro, genişleme)", "imf", YIL4, "ab_yil", "ana", "ilk150", "cift_yonsuz"),
    ("R9_tum_ulkeler", "Örnek: verisi olan tüm egemen ekonomiler (ilk 150 kısıtı yok)", "imf", YIL4, "ana", "ana", "tum", "cift_yonsuz"),
    ("R10_yonlu_kume", "SH: yönlü çift kümelemesi (M1 ile aynı nokta tahmini)", "imf", YIL4, "ana", "ana", "ilk150", "ij"),
]


# ---------------------------------------------------------------------------------- senaryo eşlemesi
SENARYO = {"S2": "Derin STA (AB yeni nesil STA/DCFTA ortalaması)", "S3": "Temel STA (AB eski nesil STA/OA ortalaması)",
           "S4": "Anlaşma yok (DTÖ/MFN)", "S3_TR": "Temel STA: TR'nin kendi STA→GB geçişi (AB'ye katılan 11 ülke)",
           "S3_BK": "Temel STA: TR–BK'nin GB→STA geçişi (2021)", "S4_TR": "Anlaşma yok: genişleme ülkelerinde tam GB etkisi",
           "S2_DCFTA": "Derin STA: AB'nin komşu DCFTA'ları (Gürcistan, Moldova, Ukrayna)",
           "S3_AVRUPA_AKDENIZ": "Temel STA: Avrupa-Akdeniz OA'ları (Tunus, Fas, Ürdün, Lübnan, Mısır, Cezayir)"}
YONLER = {"TR→AB": ("GB_TR_AB", "ORT_AB"), "AB→TR": ("GB_AB_TR", "AB_ORT")}


def var_olan(r, adlar):
    return {a: 1.0 for a in adlar if a in r["b"].index}


def senaryo_agirliklari(tur, r):
    """(senaryo, yön, vade) → (β_X ağırlıkları, β_GB ağırlıkları). β_S4 = 0."""
    out = []
    for yon, (gb, sonek) in YONLER.items():
        if tur in ("ana", "dar", "uzaklik_yil", "kolonyal_yil", "ab_yil", "uzatma", "oncu"):
            out += [(s, yon, "statik", {k: 1.0} if k else {}, {gb: 1.0})
                    for s, k in (("S2", "AB_STA_DERIN"), ("S3", "AB_STA_TEMEL"), ("S4", None))]
        if tur == "yonlu_sta":
            out += [(s, yon, "statik", {k: 1.0} if k else {}, {gb: 1.0})
                    for s, k in (("S2", f"AB_STA_DERIN_{sonek}"), ("S3", f"AB_STA_TEMEL_{sonek}"), ("S4", None))]
        if tur in ("gecikmeli", "gb_olay"):
            gb_uzun = var_olan(r, [gb] + [f"{gb}_L{k}" for k in (4, 8, 12, 16, 20, 24)])
            derin = var_olan(r, ["AB_STA_DERIN"] + [f"AB_STA_DERIN_L{k}" for k in (4, 8, 12)])
            temel = var_olan(r, ["AB_STA_TEMEL"] + [f"AB_STA_TEMEL_L{k}" for k in (4, 8, 12)])
            vade = "uzun (GB güncel, STA tam yerleşmiş)" if tur == "gb_olay" else "uzun (12+ yıl)"
            out += [("S2", yon, vade, derin, gb_uzun), ("S3", yon, vade, temel, gb_uzun), ("S4", yon, vade, {}, gb_uzun),
                    ("S2", yon, "kısa (ilk 0–3 yıl)", {"AB_STA_DERIN": 1.0}, gb_uzun),
                    ("S3", yon, "kısa (ilk 0–3 yıl)", {"AB_STA_TEMEL": 1.0}, gb_uzun)]
        if tur == "genisleme":
            x = "TR_STA_ADAY_TR_X" if yon == "TR→AB" else "TR_STA_ADAY_X_TR"
            out += [("S3_TR", yon, "statik", {x: 1.0}, {gb + "_YENI": 1.0}),
                    ("S4_TR", yon, "statik", {}, {gb + "_YENI": 1.0})]
        if tur == "heterojen":
            out += [("S2_DCFTA", yon, "statik", {"H_DCFTA": 1.0}, {gb: 1.0}),
                    ("S3_AVRUPA_AKDENIZ", yon, "statik", {"H_AVRUPA_AKDENIZ": 1.0}, {gb: 1.0})]
        if tur == "uzatma":
            x = "TR_BK_STA_TR_GBR" if yon == "TR→AB" else "TR_BK_STA_GBR_TR"
            out.append(("S3_BK", yon, "statik (2024)", {x: 1.0}, {gb: 1.0}))
    return out


def yerlesme(r, ad, gecikmeler=(4, 8, 12)):
    """Aşamalı etki: kümülatif etki yolu [(yıl, etki, SH)] ve etkinin zirve yaptığı gecikme (yıl).
    4 yıllık aralıkta 'k yıl' = yürürlükten sonraki k ile k+3. yıllar arası."""
    yol = []
    for k in (0,) + tuple(gecikmeler):
        a = ad if k == 0 else f"{ad}_L{k}"
        if a not in r["b"].index:
            break
        kum, kse = bilesim(r, {x: 1.0 for x in [ad] + [f"{ad}_L{j}" for j in gecikmeler if j <= k]})
        yol.append((k, kum, kse))
    zirve = max(yol, key=lambda x: x[1])[0] if yol and max(x[1] for x in yol) > 0 else np.nan
    return yol, zirve


# ----------------------------------------------------------------------------------------- genel denge
def ge_coz(X, tau, theta, kosullu=False, p0=None, tol=1e-11, maxit=20000):
    """Kesin şapka cebiri, Armington-CES, sabit donanım; E_j = φ_j Y_j (φ sabit; Yotov vd. 2016 böl. 2).
    tau: (t'_ij/t_ij)^(−θ) = exp(Δβ'D). Dönüş: X', p̂ (fabrika çıkış fiyatı = nominal gelir), P̂ (iç ÇDT)."""
    Y, E = X.sum(1), X.sum(0)
    phi = E / Y
    lam = X / E[None, :]
    if kosullu:          # Y ve E sabit; yalnız çok taraflı direnç terimleri uyarlanır
        Pi, P = np.ones(len(Y)), np.ones(len(Y))
        for _ in range(maxit):
            P_yeni = (lam * tau / Pi[:, None]).sum(0)
            Pi_yeni = (X / Y[:, None] * tau / P_yeni[None, :]).sum(1)
            if np.max(np.abs(Pi_yeni - Pi)) + np.max(np.abs(P_yeni - P)) < tol:
                break
            Pi, P = Pi_yeni, P_yeni
        return X * tau / (Pi[:, None] * P[None, :]), np.ones(len(Y)), P ** (-1 / theta)
    p = np.ones(len(Y)) if p0 is None else p0.copy()
    for _ in range(maxit):
        Pt = (lam * (p ** -theta)[:, None] * tau).sum(0)                       # P̂_j^(−θ)
        talep = (lam * (p ** -theta)[:, None] * tau / Pt[None, :] * (phi * Y * p)[None, :]).sum(1)
        p_yeni = p * (talep / (p * Y)) ** (1 / (1 + theta))
        p_yeni /= (p_yeni * Y).sum() / Y.sum()                                    # dünya nominal üretimi sabit
        if np.max(np.abs(p_yeni - p)) < tol:
            p = p_yeni
            break
        p = p_yeni
    Pt = (lam * (p ** -theta)[:, None] * tau).sum(0)
    Xn = lam * (p ** -theta)[:, None] * tau / Pt[None, :] * (phi * Y * p)[None, :]
    return Xn, p, Pt ** (-1 / theta)


KD_URETIM_ORANI = {"A-B": 0.55, "D": 0.33, "C-E_D_haric": 0.40}   # katma değer / brüt üretim varsayımları [V]


def ic_ticaret(c, t, ulkeler_secili, ulke_bilgi, yil, gsyh_cepii):
    """Ülke içi mal satışları ≈ mal brüt üretimi (UN AMA KD / KD-üretim oranı) − toplam mal ihracatı (IMF).
    Eksik ya da makul olmayan (≤ %20 brüt üretim) değerler: brüt üretimin %20'si alt sınırı; AMA'da olmayanlar
    için diğer ülkelerin medyan iç satış/GSYH oranı (CEPII GSYH yok → UN AMA GSYH)."""
    yol = indir(UN_AMA_URL, os.path.join(c, "unama", "ama_usd.xlsx"))
    a = pd.read_excel(yol, header=2)
    a = a[["CountryID", "IndicatorName", yil]].rename(columns={yil: "deger"})
    m49 = {int(float(k)): v for k, v in zip(ulke_bilgi.iso3num, ulke_bilgi.iso3) if str(k) not in ("", "nan")}
    a["u"] = a.CountryID.map(m49).replace(ESLE)
    p = a.pivot_table(index="u", columns="IndicatorName", values="deger", aggfunc="sum")
    ab = p["Agriculture, hunting, forestry, fishing (ISIC A-B)"]
    ce = p["Mining, Manufacturing, Utilities (ISIC C-E)"]
    d = p["Manufacturing (ISIC D)"]
    bu = (ab / KD_URETIM_ORANI["A-B"] + d / KD_URETIM_ORANI["D"] + (ce - d) / KD_URETIM_ORANI["C-E_D_haric"]) / 1e6
    ihr = t[(t.year == yil)].groupby("o").x_imf.sum() / 1e3                   # milyon $, bütün ortaklara
    gsyh = p["Gross Domestic Product (GDP)"] / 1e6
    ic = (bu - ihr.reindex(bu.index)).clip(lower=0.2 * bu)
    oran = (ic / gsyh).median()
    sonuc = pd.Series({u: ic.get(u, np.nan) for u in ulkeler_secili})
    eksik = sonuc[sonuc.isna()].index.tolist()
    for u in eksik:
        sonuc[u] = oran * (gsyh.get(u) if pd.notna(gsyh.get(u, np.nan)) else gsyh_cepii.get((yil, u), np.nan))
    return sonuc, eksik, bu


def ge_modulu(c, t, sec, ulke_bilgi, sonuclar, gsyh_cepii, yil=2019, cekilis=1000, tohum=20261018):
    """2019 kesitinde S2/S3/S4 için koşullu ve tam GE; parametrik bootstrap ile %90 aralık."""
    ulke = [u for u in sec]
    ic, eksik, _ = ic_ticaret(c, t, ulke, ulke_bilgi, yil, gsyh_cepii)
    ic = ic.dropna()
    ulke = [u for u in ulke if u in ic.index]
    s = t[(t.year == yil) & t.o.isin(ulke) & t.d.isin(ulke)]
    X = s.pivot_table(index="o", columns="d", values="x_imf", aggfunc="sum").reindex(index=ulke, columns=ulke)
    X = X.fillna(0.0).to_numpy() / 1e3
    np.fill_diagonal(X, ic[ulke].to_numpy())
    idx = {u: k for k, u in enumerate(ulke)}
    ab = [u for u in ulke if u in AB_UYELIK and u != "GBR"]   # karşı-olgu AB27 ile; BK 2021'den beri GB dışında
    tr = idx[TR]
    ab_i = np.array([idx[u] for u in ab])
    rng = np.random.default_rng(tohum)
    tanim = {  # senaryo: (model, TR→AB ağırlık farkı, AB→TR ağırlık farkı)
        "S2": ("M1_ana", {"AB_STA_DERIN": 1, "GB_TR_AB": -1}, {"AB_STA_DERIN": 1, "GB_AB_TR": -1}),
        "S3_TR": ("M5_genisleme", {"TR_STA_ADAY_TR_X": 1, "GB_TR_AB_YENI": -1}, {"TR_STA_ADAY_X_TR": 1, "GB_AB_TR_YENI": -1}),
        "S4": ("M1_ana", {"GB_TR_AB": -1}, {"GB_AB_TR": -1}),
    }
    if "R2e_baci_2024" in sonuclar:
        tanim["S3_BK"] = ("R2e_baci_2024", {"TR_BK_STA_TR_GBR": 1, "GB_TR_AB": -1}, {"TR_BK_STA_GBR_TR": 1, "GB_AB_TR": -1})
    satirlar = []
    for theta in (4.0, 6.0):
        for sen, (model, w1, w2) in tanim.items():
            r = sonuclar[model]
            adlar = sorted(set(w1) | set(w2))
            b = r["b"][adlar].to_numpy()
            V = r["V"].loc[adlar, adlar].to_numpy()
            a1 = np.array([w1.get(a, 0) for a in adlar])
            a2 = np.array([w2.get(a, 0) for a in adlar])
            cek = np.vstack([b, rng.multivariate_normal(b, V, size=cekilis)])
            sonuc = []
            p0 = None
            for k, bb in enumerate(cek):
                tau = np.ones_like(X)
                tau[tr, ab_i] = np.exp(a1 @ bb)
                tau[ab_i, tr] = np.exp(a2 @ bb)
                for kosullu in (True, False):
                    Xn, p, P = ge_coz(X, tau, theta, kosullu=kosullu, p0=p0 if not kosullu else None)
                    if not kosullu:
                        p0 = p
                    ihr0 = X[tr].sum() - X[tr, tr]
                    ith0 = X[:, tr].sum() - X[tr, tr]
                    w_ab = X[ab_i].sum(1)
                    reel = p / P
                    sonuc.append(dict(cekilis=k, kosullu=kosullu,
                                      **{"TR→AB": Xn[tr, ab_i].sum() / X[tr, ab_i].sum() - 1,
                                         "AB→TR": Xn[ab_i, tr].sum() / X[ab_i, tr].sum() - 1,
                                         "TR toplam ihracat": (Xn[tr].sum() - Xn[tr, tr]) / ihr0 - 1,
                                         "TR toplam ithalat": (Xn[:, tr].sum() - Xn[tr, tr]) / ith0 - 1,
                                         "TR reel GSYH (refah vekili)": reel[tr] - 1,
                                         "AB reel GSYH (üretim ağırlıklı)": (w_ab * reel[ab_i]).sum() / w_ab.sum() - 1}))
            d = pd.DataFrame(sonuc)
            for kosullu, g in d.groupby("kosullu"):
                for olcu in ["TR→AB", "AB→TR", "TR toplam ihracat", "TR toplam ithalat", "TR reel GSYH (refah vekili)",
                             "AB reel GSYH (üretim ağırlıklı)"]:
                    if kosullu and "reel" in olcu:
                        continue
                    nokta = g.loc[g.cekilis == 0, olcu].iloc[0]
                    q = g.loc[g.cekilis > 0, olcu].quantile([0.05, 0.95])
                    satirlar.append(dict(spesifikasyon=f"GE_{'kosullu' if kosullu else 'tam'}_sigma{int(theta + 1)}",
                                         yontem=f"GE ({'koşullu: yalnız ÇDT' if kosullu else 'tam donanım'}), σ = {theta + 1:.0f}, {yil} kesiti, {len(ulke)} ülke",
                                         senaryo=sen, senaryo_tanim=SENARYO[sen], yon=olcu, vade="uzun (yeni denge)",
                                         kaynak_model=model, degisim_yuzde=100 * nokta, ci90_alt_yuzde=100 * q.iloc[0],
                                         ci90_ust_yuzde=100 * q.iloc[1],
                                         formul="τ̂(TR→AB27) = exp(fark_TR→AB), τ̂(AB27→TR) = exp(fark_AB→TR); kesin şapka cebiri",
                                         degerlendirme=("GA: %90 parametrik bootstrap (β ~ N(β̂, V̂), "
                                                        f"{cekilis} çekiliş). Ülke içi satışlar UN AMA katma değerinden "
                                                        "türetildi (KD/üretim oranı varsayımı); BK karşı-olguda GB dışı.")))
    bilgi = dict(ulke_sayisi=len(ulke), eksik_ama=eksik,
                 tr_ic_pay=float(X[tr, tr] / X[:, tr].sum()), tr_ic_satis_musd=float(X[tr, tr]))
    return pd.DataFrame(satirlar), bilgi


# ------------------------------------------------------------------------------------------------ ana
def degerlendir(spes, sen, yon):
    """Senaryo satırları için kısa yorum (kullanım önerisi)."""
    if spes == "M1_ana" and sen == "S4":
        return ("Tercih edilen. GB katsayısı 1996 öncesi ortaklık rejimine göre artıştır (ikili sabit etki, 1971'den beri "
                "TR sanayi ürünlerine AB tercihi ve 1993–95 TR tarife indirimlerini taban alır) → S4 kaybı alt sınır. "
                "Çapraz kontrol, tarife duvarı (veri/s4_tarife_duvari_ozet.csv, KD, σ=3–8): " +
                ("TR→AB −15/−33%." if yon == "TR→AB" else "AB→TR −12/−27% (İGV hariç), −22/−42% (İGV dahil)."))
    if spes == "M1_ana":
        return {"S2": "Tercih edilen (görev eşlemesi). Derin STA katsayısı 2020'ye ve uzaklık×yıl kontrolüne duyarlı "
                      "(R1, R6'da ≈ 0 → S2 ≈ S4); yönlü modelde (M1b) ortak→AB etkisi ≈ 0.",
                "S3": "Kullanılamaz: AB temel STA katsayısı negatif (S3, S4'ten kötü çıkıyor; ekonomik olarak tutarsız) ve "
                      "öncü sınaması anlamlı (M4: −0,19, p<0,01) → ön-eğilim yanlılığı. Yerine S3_TR (M5) ve S3_BK (R2e).",
                }[sen]
    if spes == "M5_genisleme":
        return {"S3_TR": "Tercih edilen S3 (ihtiyatlı): TR–aday STA'sından GB'ye geçiş (2004/2007/2013). Katılımın kendisiyle "
                         "(tek pazar, değer zincirleri) karışabilir → kayıp için üst sınır niteliğinde.",
                "S4_TR": "Bilgi amaçlı: genişleme ülkelerinde GB'nin anlaşmasız duruma göre tam etkisi; 1990'ların geçiş "
                         "dönemi yeniden yönelimi nedeniyle büyük olasılıkla abartılı."}.get(sen, "")
    if spes == "R2e_baci_2024" and sen == "S3_BK":
        return ("İyimser S3: TR–BK'nin GB'den STA'ya geçişi (2021). Tek çift, 3 yıl; sıfır tarife korundu, menşe "
                "kurallarında AB girdisiyle kümülasyon; BK'nin genel Brexit şoku sabit etkilerde.")
    if spes in ("M2_gecikmeli", "M3_gb_olay"):
        return "Dinamik: GB etkisi zamanla aşınmış (olay çalışması); güncel GB etkisi küçük ve belirsiz, GA'lar geniş."
    if spes == "M1b_yonlu_sta":
        return "Yönlü STA etkileri: TR→AB için ortak→AB, AB→TR için AB→ortak katsayısı."
    if spes == "M6_heterojen":
        return {"S2_DCFTA": "Türkiye'ye en yakın emsal (komşu, düzenleyici uyum); 3 ortak, yalnız 2016–2020 gözlemleri; "
                            "Rusya kopuşu kontrol edilse de yeniden yönelim nedeniyle yukarı yanlı olabilir → kesinlik düşük.",
                "S3_AVRUPA_AKDENIZ": "Avrupa-Akdeniz OA'ları; ön-eğilim nedeniyle aşağı yanlı (M4)."}.get(sen, "")
    return "Sağlamlık."


def yil_etiketi(yillar):
    y = sorted(yillar)
    adim = sorted(set(np.diff(y)))
    return f"{y[0]}–{y[-1]}, {'/'.join(map(str, adim))} yıl" + (" (+2024)" if 2024 in y and len(adim) > 1 else "")


def katsayi_satirlari(etiket, aciklama, kaynak, yillar, n_ulke, kume, r):
    from scipy.stats import norm
    s = []
    for a in r["b"].index:
        b, se = r["b"][a], float(np.sqrt(r["V"].loc[a, a]))
        s.append(dict(spesifikasyon=etiket, aciklama=aciklama, veri=kaynak, yillar=yil_etiketi(yillar),
                      ulke_sayisi=n_ulke, degisken=a, tur="tahmin", katsayi=b, se_kume=se, z=b / se,
                      p=2 * (1 - norm.cdf(abs(b / se))), ci90_alt=b - Z90 * se, ci90_ust=b + Z90 * se,
                      etki_yuzde=100 * (np.exp(b) - 1), N=r["N"], n_cift=r["n_cift"], n_kume=r["G"],
                      kume="yönsüz ülke çifti" if kume == "cift_yonsuz" else "yönlü ülke çifti"))
    return s


def turetilmis(satir0, ad, deger, se):
    from scipy.stats import norm
    s = dict(satir0)
    s.update(degisken=ad, tur="türetilmiş (doğrusal bileşim, delta yöntemi)", katsayi=deger, se_kume=se, z=deger / se,
             p=2 * (1 - norm.cdf(abs(deger / se))), ci90_alt=deger - Z90 * se, ci90_ust=deger + Z90 * se,
             etki_yuzde=100 * (np.exp(deger) - 1))
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=yollar.GIRDI)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    ap.add_argument("--baci-dizin", default=None,
                    help="BACI HS17 V202601 klasörü (all_countries/*.parquet ve country_codes_V202601.csv; "
                         "varsayılan <cache>/baci, baci_ozet.py çıktısı); yoksa 2024 uzatması (R2e, S3_BK) atlanır")
    ap.add_argument("--ulke-sayisi", type=int, default=150)
    ap.add_argument("--ge-cekilis", type=int, default=1000)
    a = ap.parse_args()
    c = os.path.join(a.cache, "f2_cekim")
    os.makedirs(c, exist_ok=True)
    pd.set_option("display.width", 220)
    import time
    t0 = time.time()

    g, ulke_bilgi = gravity_oku(c)
    desta = desta_oku(c)
    t = uyumlastir(g)
    gsyh = gsyh_tablosu(g)
    del g
    sec, hacim = ulke_sec(t, ulke_bilgi, a.ulke_sayisi)
    tum = list(dict.fromkeys(list(hacim.index) + sec))
    rs = rta_suresi(t)
    uz, kontrol, rs_uz = None, None, None
    a.baci_dizin = a.baci_dizin or os.path.join(a.cache, "baci")   # README: baci_ozet.py çıktısı
    if any(os.path.exists(os.path.join(a.baci_dizin, *p)) for p in
           (("baci_hs17_ikili_toplam_2024.parquet",), ("all_countries", "BACI_HS17_Y2024_V202601.parquet"))):
        uz, kontrol = tabloyu_uzat(t, a.baci_dizin)
        rs_uz = rta_suresi(uz)
        print("BACI 2020 sürüm tutarlılığı (HS17 V202601 / CEPII Gravity BACI):", kontrol)

    katsayilar, senaryolar, sonuclar, paneller = [], [], {}, {}
    for etiket, aciklama, kaynak, yillar, tur, sinif, ulkeler, kume in SPEC:
        if tur == "uzatma" and uz is None:
            print("atlandı (BACI 2024 yok):", etiket)
            continue
        tablo, rs_t = (uz, rs_uz) if tur == "uzatma" else (t, rs)
        anahtar = (kaynak, tuple(yillar), sinif, ulkeler, tur == "uzatma")
        if anahtar not in paneller:
            paneller[anahtar] = kuklalar(panel(tablo, sec if ulkeler == "ilk150" else tum, kaynak, yillar), rs_t, sinif)
        p = paneller[anahtar].copy()
        v = degiskenler(p, tur)
        r = tahmin(p, v, kume=kume)
        sonuclar[etiket] = r
        n_ulke = int(pd.concat([p.o, p.d]).nunique())
        ks = katsayi_satirlari(etiket, aciklama, kaynak, yillar, n_ulke, kume, r)
        katsayilar += ks
        # türetilmiş: aşamalı etkinin kümülatif yolu, genişleme ve BK farkları
        for ad in ("GB_TR_AB", "GB_AB_TR", "AB_STA_DERIN", "AB_STA_TEMEL"):
            if f"{ad}_L4" in r["b"].index:
                yol, _ = yerlesme(r, ad, (4, 8, 12, 16, 20, 24))
                for k, kum, kse in yol[1:]:
                    katsayilar.append(turetilmis(ks[0], f"{ad}_kumulatif_{k}yil", kum, kse))
        if tur == "genisleme":
            for x, gb in (("TR_STA_ADAY_TR_X", "GB_TR_AB_YENI"), ("TR_STA_ADAY_X_TR", "GB_AB_TR_YENI")):
                katsayilar.append(turetilmis(ks[0], f"{gb}_eksi_{x}", *bilesim(r, {gb: 1, x: -1})))
        if tur == "uzatma":
            for x, gb in (("TR_BK_STA_TR_GBR", "GB_TR_AB"), ("TR_BK_STA_GBR_TR", "GB_AB_TR"), ("AB_BK_TCA", "AB_UYELIK")):
                katsayilar.append(turetilmis(ks[0], f"{x}_eksi_{gb}", *bilesim(r, {x: 1, gb: -1})))
        # senaryolar
        for sen, yon, vade, wX, wGB in senaryo_agirliklari(tur, r):
            w = dict(wX)
            for k, x in wGB.items():
                w[k] = w.get(k, 0.0) - x
            eksik = [k for k in list(wX) + list(wGB) if k not in r["b"].index]
            if eksik:
                continue
            d, se = bilesim(r, w)
            bX = bilesim(r, wX)[0] if wX else 0.0
            bGB = bilesim(r, wGB)[0]
            senaryolar.append(dict(spesifikasyon=etiket, yontem="Kısmi denge (ÇDT ve gelirler sabit)", senaryo=sen,
                                   senaryo_tanim=SENARYO[sen], yon=yon, vade=vade,
                                   beta_senaryo=bX, beta_gb=bGB, fark=d, se_fark=se, degisim_yuzde=100 * (np.exp(d) - 1),
                                   ci90_alt_yuzde=100 * (np.exp(d - Z90 * se) - 1), ci90_ust_yuzde=100 * (np.exp(d + Z90 * se) - 1),
                                   N=r["N"], veri=kaynak, yillar=yil_etiketi(yillar), _wX=list(wX), _wGB=list(wGB)))
        print(f"{etiket:22s} N={r['N']:7d}  " + "  ".join(
            f"{k}={r['b'][k]:+.3f}({np.sqrt(r['V'].loc[k, k]):.3f})" for k in
            ["GB_TR_AB", "GB_AB_TR", "AB_STA_DERIN", "AB_STA_TEMEL"] if k in r["b"].index), flush=True)

    # aşamalı etki özeti (M2): kümülatif yol ve zirve gecikmesi (k yıl = yürürlükten k ile k+3 yıl sonra)
    r2 = sonuclar["M2_gecikmeli"]
    adlar = ("GB_TR_AB", "GB_AB_TR", "AB_STA_DERIN", "AB_STA_TEMEL")
    zirve = {ad: yerlesme(r2, ad)[1] for ad in adlar}
    yol_metin = {ad: "; ".join(f"{k}–{k + 3} yıl: {100 * (np.exp(kum) - 1):+.1f}% (SH {kse:.3f})"
                               for k, kum, kse in yerlesme(r2, ad)[0]) for ad in adlar}
    sen = pd.DataFrame(senaryolar)
    x_ad = {"S2": "AB_STA_DERIN", "S3": "AB_STA_TEMEL"}
    sen["etki_zirve_yil_senaryo"] = sen.senaryo.map(lambda s_: zirve.get(x_ad.get(s_, ""), np.nan))
    sen["etki_zirve_yil_gb"] = sen.yon.map(lambda y_: zirve[YONLER[y_][0]])
    sen["kumulatif_yol_senaryo_M2"] = sen.senaryo.map(lambda s_: yol_metin.get(x_ad.get(s_, ""), ""))
    sen["kumulatif_yol_gb_M2"] = sen.yon.map(lambda y_: yol_metin[YONLER[y_][0]])
    sen["formul"] = [f"exp({' + '.join(k for k in wx) or '0'} − ({' + '.join(wg)})) − 1"
                     for wx, wg in zip(sen.pop("_wX"), sen.pop("_wGB"))]
    tercih = ((sen.spesifikasyon == "M1_ana") & sen.senaryo.isin(["S2", "S4"])) | \
             ((sen.spesifikasyon == "M5_genisleme") & (sen.senaryo == "S3_TR"))
    sen["tercih_edilen"] = tercih.astype(int)
    sen["degerlendirme"] = [degerlendir(sp, sn, yn) for sp, sn, yn in zip(sen.spesifikasyon, sen.senaryo, sen.yon)]

    # genel denge
    ge, bilgi = ge_modulu(c, t, sec, ulke_bilgi, sonuclar, gsyh, cekilis=a.ge_cekilis)
    print("GE bilgi:", bilgi)
    ge["tercih_edilen"] = (ge.spesifikasyon == "GE_tam_sigma7").astype(int)
    sen = pd.concat([sen, ge], ignore_index=True)
    sira = ["spesifikasyon", "yontem", "senaryo", "senaryo_tanim", "yon", "vade", "degisim_yuzde", "ci90_alt_yuzde",
            "ci90_ust_yuzde", "beta_senaryo", "beta_gb", "fark", "se_fark", "formul", "etki_zirve_yil_senaryo",
            "etki_zirve_yil_gb", "kumulatif_yol_senaryo_M2", "kumulatif_yol_gb_M2", "tercih_edilen", "degerlendirme",
            "N", "veri", "yillar", "kaynak_model"]
    sen = sen[sira]

    # DESTA derinliği: sınıflama tablosu (konsola) — CSV'de değil, betik başlığında belgelendi
    sinif = pd.DataFrame(AB_ANLASMA, columns=["ortak", "kategori", "yururluk", "desta_no", "ad"])
    sinif = sinif.join(desta[["depth_index", "depth_rasch"]], on="desta_no")
    print(sinif.groupby(["kategori", "ad"]).agg(ortaklar=("ortak", lambda s_: ",".join(s_)), yururluk=("yururluk", "min"),
                                                 depth_index=("depth_index", "first"), depth_rasch=("depth_rasch", "first"))
          .round(2).to_string())

    ks = pd.DataFrame(katsayilar)
    ks.round(6).to_csv(os.path.join(a.out, "politika_cekim_katsayilar.csv"), index=False)
    sen.round(6).to_csv(os.path.join(a.out, "politika_cekim_senaryolar.csv"), index=False)
    print(sen[sen.tercih_edilen == 1][["spesifikasyon", "senaryo", "yon", "degisim_yuzde", "ci90_alt_yuzde",
                                       "ci90_ust_yuzde"]].round(1).to_string(index=False))
    print(ge[ge.spesifikasyon == "GE_tam_sigma7"][["senaryo", "yon", "degisim_yuzde", "ci90_alt_yuzde",
                                                  "ci90_ust_yuzde"]].round(2).to_string(index=False))
    print(f"süre: {time.time() - t0:.0f} sn")


if __name__ == "__main__":
    main()
