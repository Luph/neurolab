"""Faz 0 — NACE kapsam listesi ve GB statü etiketleri.

Zincir: CN2025 (8 hane) -> CPA 2.2 -> CPA 2.1 -> NACE Rev. 2 sınıfı (CPA 2.1 kodunun ilk 4 hanesi).
Her CN8 satırına bir ticaret rejimi atanır (GB / AKCT / ITU / TARIM), ardından NACE Rev. 2
sınıfı düzeyinde rejim payları Türkiye'nin AB'ye ihracatıyla (Eurostat Comext, AB'nin
Türkiye'den ithalatı, 2025, avro) ağırlıklandırılır.

Kaynaklar (hepsi herkese açık, kimlik doğrulama gerektirmez):
  - Eurostat SDMX kod listeleri NACE_R2 ve NACE_R2_1
  - EU Vocabularies (ShowVoc): NACE Rev. 2.1–NACE Rev. 2, CPA 2.2–CPA 2.1, CPA 2.2–CN 2025
  - Eurostat Comext DS-045409 (AB27 × TR, CN8, 2025, akış 1 = AB ithalatı, 2 = AB ihracatı)
  - GİB NACE Rev. 2.1 sınıf adları (Türkçe, 2026)

Kullanım:
  python3 f0_nace_kapsam.py --cache ~/.cache/gb_cikis --out ../veri

Rejim kuralları HS fasıl/pozisyon düzeyinde yaklaşık kurallardır; kesin liste için
1/95 sayılı Karar Ek 1 (işlenmiş tarım ürünleri) ve 1996 AKÇT Anlaşması ürün listesi
ile satır satır doğrulama Faz 3'te yapılacaktır (bkz. veri boşlukları).
"""

import argparse
import os
import re
import urllib.parse
import urllib.request

import pandas as pd

ESTAT_CL = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/codelist/ESTAT/{cl}/latest?format=TSV&lang=en"
SHOWVOC = ("https://showvoc.op.europa.eu/semanticturkey/it.uniroma2.art.semanticturkey/"
           "st-core-services/Download/getFile?fileName={f}&ctx_project={p}")
P_CPA22 = "ESTAT_Statistical_classification_of_products_by_activity,_2.2_(CPA_2.2)"
P_NACE21 = ("ESTAT_Statistical_Classification_of_Economic_Activities_in_the_European_Community_"
            "Rev._2.1._(NACE_2.1)")
COMEXT = ("https://ec.europa.eu/eurostat/api/comext/dissemination/sdmx/2.1/data/DS-045409/"
          "A.EU27_2020.TR..{flow}.VALUE_IN_EUROS?startPeriod={y}&endPeriod={y}")
GIB_SINIF = ("https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey="
             "arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2F4_FAALIYETSINIFKODLARI.xls")

YIL = 2025
# Bir rejimin payı >= %97,5 ise sınıf o rejimle etiketlenir; başka bir rejimin payı %2,5'i
# aşıyorsa KARMA (önemlilik eşiği; varsayım kaydında V-15)
ESIK_TEK_REJIM = 0.975
ESIK_SATIR = 0.90  # değer ağırlığı yerine CN satır sayısı kullanıldığında (düşük ticaretli sınıflar)

# CPA 2.1'de çıktısı "hizmet" olarak tanımlanan ama fiziksel çıktısı GB kapsamındaki mal
# satırlarında (parça, kumaş, basılı ürün) sınıflanan fason/işleme sınıfları
DOLAYLI_GB = {
    "13.30": "Fason boya-terbiye; bitmiş kumaş GB kapsamında (HS 50–60).",
    "18.11": "Basım hizmeti; basılı ürünler (HS 49) GB kapsamında.",
    "18.12": "Basım hizmeti; basılı ürünler (HS 49) GB kapsamında.",
    "18.20": "Çoğaltma hizmeti; kayıt ortamı (HS 8523) GB kapsamında.",
    "24.53": "Döküm hizmeti; dökme parçalar müşteri ürün satırlarında (ör. HS 8708) GB kapsamında.",
    "24.54": "Döküm hizmeti; dökme parçalar müşteri ürün satırlarında GB kapsamında.",
    "25.50": "Dövme/presleme hizmeti; parçalar müşteri ürün satırlarında GB kapsamında.",
    "25.61": "Kaplama/ısıl işlem hizmeti; işlenen mal GB veya AKÇT kapsamında.",
    "25.62": "Talaşlı imalat hizmeti; işlenen parçalar GB kapsamında.",
}


def indir(url, yol, headers=None):
    if os.path.exists(yol) and os.path.getsize(yol) > 0:
        return yol
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=600) as r, open(yol, "wb") as f:
        f.write(r.read())
    return yol


def showvoc(proje, dosya, yol):
    url = SHOWVOC.format(f=urllib.parse.quote(dosya), p=urllib.parse.quote(proje))
    return indir(url, yol)


# ---------------------------------------------------------------------------
# Türkçe büyük/küçük harf dönüşümü (I/ı, İ/i)
# ---------------------------------------------------------------------------
def tr_cumle(s):
    s = str(s).strip().replace("I", "ı").replace("İ", "i").lower()
    s = re.sub(r"\s+", " ", s)
    bas = {"i": "İ", "ı": "I"}.get(s[:1], s[:1].upper())
    return bas + s[1:]


# Rev. 2 sınıfının içeriği Rev. 2.1'de aynı kodla değiştiyse veya kod kaldırıldıysa
# GİB (Rev. 2.1) adı kullanılamaz; TÜİK Rev. 2 adlandırmasına dayalı çalışma adları:
AD_R2 = {
    "10.11": "Etin işlenmesi ve saklanması (kümes hayvanları eti hariç)",
    "10.51": "Süthane işletmelerinin faaliyetleri ve peynir imalatı",
    "10.52": "Dondurma imalatı",
    "10.72": "Peksimet ve bisküvi imalatı; dayanıklı pastane ürünleri ve dayanıklı kek imalatı",
    "11.03": "Elma şarabı ve diğer meyve şaraplarının imalatı",
    "11.07": "Alkolsüz içeceklerin imalatı; maden sularının ve diğer şişelenmiş suların üretimi",
    "13.92": "Giyim eşyası dışındaki tamamlanmış tekstil ürünlerinin imalatı",
    "13.95": "Dokusuz kumaşların ve dokusuz kumaştan ürünlerin imalatı (giyim eşyası hariç)",
    "14.11": "Deri giyim eşyası imalatı",
    "14.12": "İş giysisi imalatı",
    "14.13": "Diğer dış giyim eşyası imalatı",
    "14.14": "İç giyim eşyası imalatı",
    "14.19": "Diğer giyim eşyası ve aksesuarlarının imalatı",
    "14.20": "Kürkten eşya imalatı",
    "14.31": "Örme (trikotaj) ve tığ işi (kroşe) çorap imalatı",
    "14.39": "Örme (trikotaj) ve tığ işi (kroşe) diğer giyim eşyası imalatı",
    "15.11": "Derinin tabaklanması ve işlenmesi; kürkün işlenmesi ve boyanması",
    "15.12": "Bavul, el çantası ve benzerleri ile saraçlık ve koşum takımı imalatı",
    "16.10": "Ağaçların biçilmesi ve planyalanması",
    "16.29": "Ağaçtan diğer ürünlerin imalatı; mantar, saz, saman ve benzeri örme "
             "malzemelerinden ürünlerin imalatı",
    "17.21": "Oluklu kağıt ve mukavva ile kağıt ve mukavvadan muhafazaların imalatı",
    "17.29": "Kağıt ve mukavvadan diğer ürünlerin imalatı",
    "19.20": "Rafine edilmiş petrol ürünleri imalatı",
    "20.20": "Haşere ilaçları ve diğer zirai-kimyasal ürünlerin imalatı",
    "20.51": "Patlayıcı madde imalatı",
    "20.52": "Tutkal imalatı",
    "20.53": "Uçucu yağların imalatı",
    "22.11": "Kauçuk dış ve iç lastik imalatı; lastiğe sırt geçirilmesi ve yeniden işlenmesi",
    "22.19": "Diğer kauçuk ürünlerin imalatı",
    "22.23": "Plastikten inşaat malzemeleri imalatı",
    "22.29": "Diğer plastik ürünlerin imalatı",
    "23.19": "Diğer camların imalatı ve işlenmesi (teknik amaçlı cam eşyalar dahil)",
    "23.49": "Diğer seramik ürünlerin imalatı",
    "23.69": "Beton, alçı ve çimentodan diğer ürünlerin imalatı",
    "23.91": "Aşındırıcı ürünlerin imalatı",
    "25.21": "Merkezi ısıtma radyatörleri ve kazanları imalatı",
    "25.29": "Metalden diğer tank, rezervuar ve konteynerlerin imalatı",
    "25.30": "Buhar jeneratörü imalatı (merkezi ısıtma sıcak su kazanları hariç)",
    "25.40": "Silah ve mühimmat (cephane) imalatı",
    "25.50": "Metallerin dövülmesi, preslenmesi, baskılanması ve yuvarlanması; toz metalurjisi",
    "25.61": "Metallerin işlenmesi ve kaplanması",
    "25.62": "Metallerin makinede işlenmesi",
    "25.71": "Çatal-bıçak takımı ve diğer kesici aletlerin imalatı",
    "25.72": "Kilit ve menteşe imalatı",
    "25.73": "Alet imalatı",
    "26.70": "Optik aletlerin ve fotoğrafik ekipmanların imalatı",
    "26.80": "Manyetik ve optik kayıt ortamlarının imalatı",
    "27.40": "Elektrikli aydınlatma ekipmanları imalatı",
    "28.21": "Fırınlar, ocaklar ve ocak brülörleri imalatı",
    "28.23": "Büro makineleri ve ekipmanları imalatı (bilgisayarlar ve çevre birimleri hariç)",
    "28.25": "Soğutma ve havalandırma donanımlarının imalatı (evde kullanılanlar hariç)",
    "28.41": "Metal şekillendirme makinelerinin imalatı",
    "28.49": "Diğer takım tezgâhlarının imalatı",
    "29.20": "Motorlu kara taşıtları için karoser (kaporta) imalatı; treyler (römork) ve "
             "yarı treyler imalatı",
    "30.11": "Gemilerin ve yüzen yapıların inşası",
    "30.30": "Hava taşıtları ve uzay araçları ile bunlarla ilgili makinelerin imalatı",
    "31.01": "Büro ve mağaza mobilyaları imalatı",
    "31.02": "Mutfak mobilyalarının imalatı",
    "31.03": "Yatak imalatı",
    "31.09": "Diğer mobilyaların imalatı",
    "33.11": "Fabrikasyon metal ürünlerin onarımı",
    "33.12": "Makinelerin onarımı",
    "33.13": "Elektronik ve optik ekipmanların onarımı",
    "33.14": "Elektrikli ekipmanların onarımı",
    "33.15": "Gemilerin ve teknelerin bakım ve onarımı",
    "33.16": "Hava taşıtlarının ve uzay araçlarının bakım ve onarımı",
    "33.17": "Diğer ulaşım ekipmanlarının bakım ve onarımı",
    "33.19": "Diğer ekipmanların onarımı",
    # C dışı kapsam (Rev. 2.1'de aynı kodun anlamı değişen sınıflar dahil)
    "05.10": "Taş kömürü madenciliği",
    "05.20": "Linyit madenciliği",
    "06.10": "Ham petrol çıkarımı",
    "06.20": "Doğal gaz çıkarımı",
    "07.10": "Demir cevherleri madenciliği",
    "07.21": "Uranyum ve toryum cevherleri madenciliği",
    "07.29": "Diğer demir dışı metal cevherleri madenciliği",
    "08.11": "Süs ve yapı taşı, kireç taşı, alçı taşı, tebeşir ve arduvaz ocakçılığı",
    "08.12": "Çakıl ve kum ocaklarının işletilmesi; kil ve kaolin madenciliği",
    "08.91": "Kimyasal ve gübre mineralleri madenciliği",
    "08.92": "Turba çıkarımı",
    "08.93": "Tuz çıkarımı",
    "08.99": "Başka yerde sınıflandırılmamış diğer madencilik ve taş ocakçılığı",
    "09.10": "Petrol ve doğal gaz çıkarımını destekleyici faaliyetler",
    "09.90": "Madencilik ve taş ocakçılığını destekleyici diğer faaliyetler",
    "35.11": "Elektrik enerjisi üretimi",
    "38.31": "Hurdaların (gemi, araç vb.) parçalara ayrılması",
    "38.32": "Tasnif edilmiş materyallerin geri kazanımı",
}

# C dışındaki ek kapsam: (kod, kapsam grubu, sabit etiket veya None = CN'den hesapla, not)
EK_KAPSAM = [
    ("05.10", "B", None, "Kömür AKÇT ürünüdür."),
    ("05.20", "B", None, "Linyit AKÇT ürünüdür."),
    ("06.10", "B", None, ""),
    ("06.20", "B", None, ""),
    ("07.10", "B", None, "Demir cevheri AKÇT listesinde [D?]."),
    ("07.21", "B", None, "Euratom ürünleri; GB kapsamı [D?]."),
    ("07.29", "B", None, "Krom, bakır, çinko, nadir toprak cevherleri; kritik hammadde."),
    ("08.11", "B", None, "Mermer ve doğal taş."),
    ("08.12", "B", None, "Kaolin, kil, feldspat değil (08.99)."),
    ("08.91", "B", None, "Bor mineralleri (ham), fosfat, potas."),
    ("08.92", "B", None, ""),
    ("08.93", "B", None, ""),
    ("08.99", "B", None, "Feldspat, perlit, barit vb."),
    ("09.10", "B", "KAPSAM DIŞI", "Hizmet."),
    ("09.90", "B", "KAPSAM DIŞI", "Hizmet."),
    ("35.11", "D", None, "Elektrik HS 2716; SKDM kapsamında."),
    ("38.31", "E", None, "Gemi söküm (Aliağa) ve araç hurdası."),
    ("38.32", "E", None, "Hurda HS 7204 çoğunlukla CPA 38.11'e eşlenir; bkz. not."),
]
A_KAPSAM = [
    ("A01", "01.", "Bitkisel ve hayvansal üretim; yalnızca İTÜ bağlantısı ve DCFTA tarım "
     "müzakeresi için. Ham pamuk ve yapağı Ek I dışı (GB)."),
    ("A02", "02.", "Ormancılık: tomruk (HS 44) GB; doğal mantar (HS 4501) Ek I tarım."),
    ("A03", "03.", "Balıkçılık ve su ürünleri (CPA 03.00); tercihli rejim [D?]."),
]
HIZMET_KAPSAM = [
    ("46", "Hizmet", "KAPSAM DIŞI", "Toptan ticaret (46.77 hurda toptancılığı dahil); ithalat dağıtımı."),
    ("49.41", "Hizmet", "KAPSAM DIŞI", "Karayolu yük taşımacılığı; kota ve geçiş belgeleri."),
    ("50.20", "Hizmet", "KAPSAM DIŞI", "Deniz yük taşımacılığı; Ro-Ro hatları."),
    ("52.10", "Hizmet", "KAPSAM DIŞI", "Depolama ve ambarlama."),
    ("52.29", "Hizmet", "KAPSAM DIŞI", "Gümrük müşavirliği, nakliye organizasyonu."),
    ("62", "Hizmet", "KAPSAM DIŞI", "Yazılım ve BT hizmetleri; dijital ticaret."),
    ("71.20", "Hizmet", "KAPSAM DIŞI", "Uygunluk değerlendirme ve test; CE / onaylanmış kuruluş."),
    ("F", "Hizmet", "KAPSAM DIŞI", "İnşaat ve müteahhitlik; AB kamu alımlarına erişim."),
]
AD_HIZMET = {
    "A01": "Bitkisel ve hayvansal üretim ile avcılık ve ilgili hizmet faaliyetleri",
    "A02": "Ormancılık ve tomrukçuluk",
    "A03": "Balıkçılık ve su ürünleri yetiştiriciliği",
    "46": "Toptan ticaret (motorlu kara taşıtları ve motosikletler hariç)",
    "49.41": "Kara yolu ile yük taşımacılığı",
    "50.20": "Deniz ve kıyı sularında yük taşımacılığı",
    "52.10": "Depolama ve ambarlama",
    "52.29": "Taşımacılığı destekleyici diğer faaliyetler",
    "62": "Bilgisayar programlama, danışmanlık ve ilgili faaliyetler",
    "71.20": "Teknik test ve analiz faaliyetleri",
    "F": "İnşaat",
}


# ---------------------------------------------------------------------------
# Rejim kuralları (CN8 -> GB / AKCT / ITU / TARIM)
# ---------------------------------------------------------------------------
def _bas(cn, onekler):
    return any(cn.startswith(o) for o in onekler)


# 1996 AKÇT Anlaşması Ek I (CN 1996, 280 satır). CN 2025'e aktarım: HS6 eşleşmesi yeterli
# sayılır; yalnızca '90'/'99' ile biten artık alt başlıklarda ve 7202 (ferro alaşımlar) ile
# 2619'da (cüruf) satır düzeyinde (CN8) eşleşme aranır. CN8 kodu 1996'dan beri değişmiş artık
# alt başlıklar (hiçbir CN2025 satırı eşleşmiyorsa) bütünüyle AKÇT sayılır.
_AKCT_DOSYA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "veri", "akct_1996_cn8.txt")
with open(_AKCT_DOSYA, encoding="utf-8") as _f:
    AKCT_CN8 = {s.strip() for s in _f if re.fullmatch(r"\d{8}", s.strip())}
AKCT_HS6 = {c[:6] for c in AKCT_CN8}
AKCT_SATIR_DUZEYI = {h for h in AKCT_HS6 if h[-2:] in ("90", "99") or h[:4] in ("7202", "2619")}
AKCT_HS6_KODSUZ = set()  # main() içinde CN2025 listesine göre doldurulur


def akct_mi(cn):
    h6 = cn[:6]
    if h6 not in AKCT_HS6:
        return False
    if h6 in AKCT_SATIR_DUZEYI and h6 not in AKCT_HS6_KODSUZ:
        return cn[:8] in AKCT_CN8
    return True
# ABİHA Ek I dışındaki işlenmiş tarım ürünleri (AB'nin Ek I dışı mallar listesine dayalı; [D?])
ITU = (
    "040320", "040390", "040520", "170250", "17029010", "1704", "1803", "1804", "1805", "1806",
    "19", "21", "2202", "2203", "2205", "2208", "2402", "2403", "2404", "290543", "290544",
    "330210", "3501", "3502", "3505", "380910", "3823", "382460",
    "15171010", "15179010", "20019030", "20019040", "20041091", "20049010", "20052010",
    "200580", "20081110", "20089985", "20089991",
)
# Süt ürünlerinde yalnızca aromalı/katkılı alt pozisyonlar İTÜ'dür
ITU_SUT = ("04032051", "04032053", "04032059", "04032091", "04032093", "04032099",
           "04039071", "04039073", "04039079", "04039091", "04039093", "04039099",
           "04052010", "04052030")
# Fasıl 25–97 içindeki ABİHA Ek I tarım ürünleri
TARIM_SANAYI_FASLI = ("4501", "5301", "5302")
# Fasıl 1–24 içinde Ek I dışında kalan sanayi ürünleri
GB_TARIM_FASLI = ("0501", "0502", "0505", "0506", "0507", "0508", "0510", "0903", "1301",
                  "1302", "14", "1505", "1506", "1518", "1520", "1521", "2201")


def rejim(cn):
    """CN8 kodu için (rejim, kural) döndürür. Gizli 'XX' kodlarında sayısal önek kullanılır."""
    cn = re.sub(r"[^0-9]", "", str(cn))
    if not cn:
        return "BILINMIYOR", "kod yok"
    fasil = int(cn[:2])
    if fasil in (98, 99):
        return "GIZLI", "fasıl 98–99 özel/gizli ticaret kodları"
    if akct_mi(cn):
        return "AKCT", "1996 AKÇT Anlaşması Ek I (CN 1996 → CN 2025 aktarımı)"
    if fasil <= 24:
        if cn.startswith("0403") or cn.startswith("0405"):
            return ("ITU", "aromalı süt ürünü / süt bazlı sürülebilir") if _bas(cn, ITU_SUT) \
                else ("TARIM", "Ek I süt ürünü")
        if cn.startswith("1302") and cn.startswith("130220"):
            return "TARIM", "pektin (Ek I)"
        if cn.startswith("2208") and cn[:8] in ("22089091", "22089099"):
            return "TARIM", "tağyir edilmemiş etil alkol (Ek I)"
        if _bas(cn, ITU):
            return "ITU", "Ek I dışı işlenmiş tarım ürünü"
        if _bas(cn, GB_TARIM_FASLI):
            return "GB", "Fasıl 1–24'te Ek I dışı sanayi ürünü"
        return "TARIM", "ABİHA Ek I tarım ürünü (1/98 rejimi; balıkçılık dahil)"
    if _bas(cn, TARIM_SANAYI_FASLI):
        return "TARIM", "Ek I: doğal mantar / ham keten / ham kenevir"
    if _bas(cn, ITU):
        return "ITU", "Ek I dışı işlenmiş tarım ürünü (kimyasal fasıllar)"
    return "GB", "sanayi ürünü (fasıl 25–97)"


# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=os.path.expanduser("~/.cache/gb_cikis"))
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    os.makedirs(a.cache, exist_ok=True)
    os.makedirs(a.out, exist_ok=True)
    c = lambda f: os.path.join(a.cache, f)  # noqa: E731

    # --- İndirmeler
    indir(ESTAT_CL.format(cl="NACE_R2"), c("nace_r2_en.tsv"))
    indir(ESTAT_CL.format(cl="NACE_R2_1"), c("nace_r21_en.tsv"))
    showvoc(P_NACE21, "NACE_Rev.2.1_NACE_Rev.2_ CorrespondenceTable.xlsx", c("nace21_nace2.xlsx"))
    showvoc(P_CPA22, "Correspondence Table CPA Ver. 2.2 - CPA Ver. 2.1.xlsx", c("cpa22_cpa21.xlsx"))
    showvoc(P_CPA22, "Correspondence table CPA Ver. 2.2 - CN 2025.tsv", c("cpa22_cn2025.tsv"))
    csv_hdr = {"Accept": "application/vnd.sdmx.data+csv;version=1.0.0"}
    for fl in (1, 2):
        indir(COMEXT.format(flow=fl, y=YIL), c(f"comext_eu_tr_{YIL}_f{fl}.csv"), csv_hdr)
    indir(GIB_SINIF, c("gib_sinif4.xls"))

    # --- NACE adları
    def kodlist(f):
        r = pd.read_csv(f, sep="\t", header=None, names=["k", "ad"], dtype=str)
        r = r[r.k.str.fullmatch(r"[A-V]\d{4}")]
        return dict(zip(r.k.str[1:3] + "." + r.k.str[3:5], r.ad))

    en2 = kodlist(c("nace_r2_en.tsv"))
    en21 = kodlist(c("nace_r21_en.tsv"))
    gib = pd.read_excel(c("gib_sinif4.xls"), header=None, dtype=str, skiprows=1, names=["k", "ad"])
    tr21 = dict(zip(gib.k.str[:2] + "." + gib.k.str[2:4], gib.ad.map(tr_cumle)))

    # --- Rev. 2 -> Rev. 2.1 köprüsü (resmî tablo)
    kk = pd.read_excel(c("nace21_nace2.xlsx"), dtype=str)
    kk = kk[kk.LEVEL == "4"][["NACE2_Code", "NACE21_Code", "TypeOfCorrespondence"]]
    kopru = (kk.groupby("NACE2_Code")
               .agg(rev21=("NACE21_Code", lambda s: ", ".join(sorted(set(s)))),
                    n21=("NACE21_Code", "nunique"))
               .reset_index())
    ters = kk.groupby("NACE21_Code").NACE2_Code.nunique()
    kopru["tip"] = kopru.apply(
        lambda r: ("1:1" if ters.get(r.rev21, 1) == 1 else "n:1") if r.n21 == 1 else f"1:{r.n21}",
        axis=1)
    kopru = kopru.set_index("NACE2_Code")

    # --- CN8 -> CPA 2.2 -> CPA 2.1 -> NACE Rev. 2
    cn = pd.read_csv(c("cpa22_cn2025.tsv"), sep="\t", dtype=str)
    cn["cn8"] = cn.CN2025_Code.str.replace(" ", "", regex=False)
    # Satır düzeyinde aranan AKÇT alt başlıklarından hiçbir CN2025 satırı 1996 koduyla
    # eşleşmiyorsa (kod değişmiş), o alt başlık bütünüyle AKÇT sayılır
    for h6 in AKCT_SATIR_DUZEYI:
        if not cn.cn8[cn.cn8.str.startswith(h6)].isin(AKCT_CN8).any():
            AKCT_HS6_KODSUZ.add(h6)
    cp = pd.read_excel(c("cpa22_cpa21.xlsx"), dtype=str)
    cp = cp[cp.LEVEL == "6"][["CPA_Ver_22_Code", "CPA_Ver_21_Code"]]
    m = cn.merge(cp, on="CPA_Ver_22_Code", how="left")
    m["nace2"] = m.CPA_Ver_21_Code.str[:5]
    # CPA 2.1 karşılığı olmayan birkaç CPA 2.2 kodu: Rev. 2.1 sınıfı tek bir Rev. 2 sınıfından
    # geliyorsa onu kullan (ör. 16.11 -> 16.10, 06.10 -> 06.10)
    tek_kaynak = kk.groupby("NACE21_Code").NACE2_Code.agg(lambda s: s.iat[0] if s.nunique() == 1 else None)
    eksik = m.nace2.isna()
    m.loc[eksik, "nace2"] = m.loc[eksik, "CPA_Ver_22_Code"].str[:5].map(tek_kaynak)
    m.loc[m.CPA_Ver_22_Code == "00.00.00", "nace2"] = "00.00"  # kullanılmış eşya
    # NACE'de karşılığı olmayan CPA sınıfı: 31.00 (oturmalık ve mobilya parçaları) -> 31.09 [H]
    m.loc[m.nace2 == "31.00", "nace2"] = "31.09"
    # CN8 birden çok NACE sınıfına düşüyorsa eşit paylaştır
    m = m.drop_duplicates(["cn8", "nace2"])
    m["agirlik"] = 1 / m.groupby("cn8").nace2.transform("count")

    # --- Comext: AB'nin Türkiye'den ithalatı (=TR'nin AB'ye ihracatı) ve AB'nin TR'ye ihracatı
    def comext(fl):
        x = pd.read_csv(c(f"comext_eu_tr_{YIL}_f{fl}.csv"), dtype=str)
        x = x[x["product"].str.len() == 8]
        return x.assign(v=x.OBS_VALUE.astype(float)).groupby("product").v.sum()

    ihr, ith = comext(1), comext(2)

    # Gizli kodlar (ör. '040120XX'): önekle eşleşen CN8'lerin en sık NACE sınıfına ata
    def gizli_nace(kod):
        on = re.sub(r"X+$", "", kod)
        aday = m[m.cn8.str.startswith(on)].nace2.dropna()
        aday = aday[aday != "00.00"]
        return aday.mode().iat[0] if len(aday) else "??.??"

    satirlar = []
    tum_kodlar = sorted(set(ihr.index) | set(ith.index) | set(m.cn8))
    mi = m.groupby("cn8")
    for kod in tum_kodlar:
        rj, kural = rejim(kod)
        if kod in mi.groups:
            g = mi.get_group(kod)
            hedefler = list(zip(g.nace2, g.agirlik, g.CPA_Ver_22_Code, g.CPA_Ver_21_Code))
        else:
            hedefler = [(gizli_nace(kod), 1.0, "", "")]
        for n2, w, c22, c21 in hedefler:
            satirlar.append(dict(cn8=kod, cpa22=c22, cpa21=c21, nace2=n2, agirlik=w, rejim=rj,
                                 kural=kural, tr_ihr_ab=ihr.get(kod, 0.0) * w,
                                 tr_ith_ab=ith.get(kod, 0.0) * w))
    cnm = pd.DataFrame(satirlar)
    aciklama = cn.drop_duplicates("cn8").set_index("cn8").CN2025_Self_Text
    cnm["cn_aciklama_en"] = cnm.cn8.map(aciklama).fillna("(gizli / CN2025 dışı kod)")
    cnm.to_csv(os.path.join(a.out, "cn2025_nace_rejim.csv"), index=False, float_format="%.0f")

    # --- NACE sınıfı düzeyinde rejim payları
    REJ = ["GB", "AKCT", "ITU", "TARIM"]
    ETIKET = {"GB": "GB", "AKCT": "AKÇT-STA", "ITU": "İTÜ", "TARIM": "TARIM-1/98"}

    def pay(grup, kolon):
        t = grup[grup.rejim.isin(REJ)].groupby("rejim")[kolon].sum()
        return (t / t.sum()).reindex(REJ, fill_value=0.0) if t.sum() > 0 else None

    def paylar(grup):
        # İkili ticaret 25 milyon avronun altındaysa değer ağırlığı sınıfın ürün yapısını temsil
        # etmez (ör. 10.12'de AB–TR kanatlı eti ticareti SPS nedeniyle sıfır, yalnızca tüy
        # ticareti var); bu durumda CN satır sayısı kullanılır.
        if grup.tr_ihr_ab.sum() + grup.tr_ith_ab.sum() >= 25e6:
            for kolon in ("tr_ihr_ab", "tr_ith_ab"):
                if grup[kolon].sum() >= 1e6:
                    return pay(grup, kolon), kolon
        return pay(grup, "agirlik"), "satir"

    def etiketle(p, taban):
        esik = ESIK_TEK_REJIM if taban != "satir" else ESIK_SATIR
        if p.max() >= esik:
            return ETIKET[p.idxmax()]
        return "KARMA"

    def kayit(kod, grup_adi, sabit, notu, ad_tr, ad_en, onek=None):
        g = cnm[cnm.nace2.str.startswith(onek)] if onek else cnm[cnm.nace2 == kod]
        rec = dict(kapsam_grubu=grup_adi, kod=kod, ad_tr=ad_tr, ad_en=ad_en,
                   tr_ihr_ab_2025_meur=round(g.tr_ihr_ab.sum() / 1e6, 1),
                   tr_ith_ab_2025_meur=round(g.tr_ith_ab.sum() / 1e6, 1),
                   cn8_satir=int(round(g.agirlik.sum())))
        if sabit:
            rec.update(gb_statusu=sabit, agirlik_tabani="kural")
        elif len(g) == 0:
            dolayli = DOLAYLI_GB.get(kod)
            rec.update(gb_statusu="GB" if dolayli else "KAPSAM DIŞI",
                       agirlik_tabani="dolaylı (CPA'da hizmet)" if dolayli else
                       "CN eşleşmesi yok (hizmet)")
            notu = dolayli or notu
        else:
            p, taban = paylar(g)
            rec.update(gb_statusu=etiketle(p, taban), agirlik_tabani=taban,
                       **{f"pay_{r}": round(p[r] * 100, 1) for r in REJ})
            pi = pay(g, "tr_ith_ab")
            if pi is not None and g.tr_ith_ab.sum() >= 1e6:
                rec.update({f"ith_pay_{r}": round(pi[r] * 100, 1) for r in REJ})
        b = kopru.loc[kod] if kod in kopru.index else None
        rec.update(rev21=b.rev21 if b is not None else "", kopru_tipi=b.tip if b is not None else "",
                   notlar=notu)
        return rec

    kayitlar = []
    for kod in sorted(k for k in en2 if re.fullmatch(r"(1\d|2\d|3[0-3])\.\d\d", k)):
        ad = AD_R2.get(kod) or tr21.get(kod) or ""
        kayitlar.append(kayit(kod, "C", None, "", ad, en2[kod]))
    for kod, grp, sabit, notu in EK_KAPSAM:
        kayitlar.append(kayit(kod, grp, sabit, notu, AD_R2[kod], en2.get(kod, "")))
    for kod, onek, notu in A_KAPSAM:
        kayitlar.append(kayit(kod, "A", None, notu, AD_HIZMET[kod], "", onek=onek))
    for kod, grp, sabit, notu in HIZMET_KAPSAM:
        kayitlar.append(dict(kapsam_grubu=grp, kod=kod, ad_tr=AD_HIZMET[kod], ad_en="",
                             gb_statusu=sabit, agirlik_tabani="kural", notlar=notu))
    ks = pd.DataFrame(kayitlar)
    hizmet_C = ks.kapsam_grubu.eq("C") & ks.gb_statusu.eq("KAPSAM DIŞI")
    ks.loc[hizmet_C, "notlar"] = "Onarım/bakım/kurulum hizmeti; GB kapsamı dışında, mal ticaretine bağlı."
    celik = ks.kod.isin(["24.10", "24.31", "24.32", "24.33", "24.34", "19.10", "07.10"])
    ks.loc[celik, "notlar"] = (ks.loc[celik, "notlar"].fillna("") +
                               " AKÇT/GB ayrımı CN satırında 1996 Anlaşması ürün listesiyle doğrulanacak [D?].").str.strip()
    sira = ["kapsam_grubu", "kod", "ad_tr", "ad_en", "gb_statusu", "pay_GB", "pay_AKCT", "pay_ITU",
            "pay_TARIM", "agirlik_tabani", "ith_pay_GB", "ith_pay_AKCT", "ith_pay_ITU", "ith_pay_TARIM",
            "tr_ihr_ab_2025_meur", "tr_ith_ab_2025_meur", "cn8_satir", "rev21", "kopru_tipi", "notlar"]
    ks = ks.reindex(columns=sira)
    ks.to_csv(os.path.join(a.out, "nace_kapsam.csv"), index=False)

    # --- NACE bölümü (2 hane) özeti: C bölümü
    C = ks[ks.kapsam_grubu == "C"].copy()
    C["bolum"] = C.kod.str[:2]
    oz = C.groupby("bolum").agg(
        sinif=("kod", "count"),
        GB=("gb_statusu", lambda s: (s == "GB").sum()),
        AKCT_STA=("gb_statusu", lambda s: (s == "AKÇT-STA").sum()),
        ITU=("gb_statusu", lambda s: (s == "İTÜ").sum()),
        TARIM=("gb_statusu", lambda s: (s == "TARIM-1/98").sum()),
        KARMA=("gb_statusu", lambda s: (s == "KARMA").sum()),
        KAPSAM_DISI=("gb_statusu", lambda s: (s == "KAPSAM DIŞI").sum()),
        tr_ihr_ab_2025_meur=("tr_ihr_ab_2025_meur", "sum"),
        tr_ith_ab_2025_meur=("tr_ith_ab_2025_meur", "sum"),
        gb_disi_siniflar=("kod", lambda s: ", ".join(
            f"{k} ({v})" for k, v in zip(s, C.loc[s.index, "gb_statusu"]) if v != "GB")),
    ).reset_index()
    bolum_rejim = (cnm.assign(bolum=cnm.nace2.str[:2])
                      .pivot_table(index="bolum", columns="rejim", values="tr_ihr_ab", aggfunc="sum")
                      .reindex(columns=REJ, fill_value=0.0).fillna(0.0))
    bolum_rejim = (bolum_rejim.div(bolum_rejim.sum(axis=1), axis=0) * 100).round(1)
    bolum_rejim.columns = [f"ihr_pay_{r}" for r in REJ]
    oz = oz.merge(bolum_rejim, left_on="bolum", right_index=True, how="left")
    oz.to_csv(os.path.join(a.out, "nace_kapsam_bolum_ozeti.csv"), index=False)

    # --- Köprü tablosu (C bölümü + ek kapsam)
    kk2 = kk.copy()
    kk2["nace2_ad_en"] = kk2.NACE2_Code.map(en2)
    kk2["nace21_ad_en"] = kk2.NACE21_Code.map(en21)
    kk2["nace21_ad_tr"] = kk2.NACE21_Code.map(tr21)
    ek = {k for k, *_ in EK_KAPSAM}
    kk2 = kk2[kk2.NACE2_Code.str.match(r"^(1\d|2\d|3[0-3])\.") | kk2.NACE2_Code.isin(ek)]
    kk2.rename(columns={"NACE2_Code": "nace2", "NACE21_Code": "nace21",
                        "TypeOfCorrespondence": "esleme_tipi_resmi"}) \
       .sort_values(["nace2", "nace21"]) \
       .to_csv(os.path.join(a.out, "nace_r2_r21_kopru.csv"), index=False)

    # --- Konsol özeti
    print("C sınıf sayısı:", len(C))
    print(C.gb_statusu.value_counts().to_string())
    tot = cnm.groupby("rejim")[["tr_ihr_ab", "tr_ith_ab"]].sum() / 1e9
    print("\nRejim bazında TR->AB ihracatı ve AB->TR ihracatı (2025, milyar avro):")
    print(tot.round(2).to_string())


if __name__ == "__main__":
    main()
