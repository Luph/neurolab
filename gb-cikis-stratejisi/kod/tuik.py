"""TÜİK verilerine kimlik doğrulamasız erişim.

İki kanal kullanılır:
  1. Dağıtım Yönetim Sistemi (databrowser2.tuik.gov.tr) arka ucu, /api/core/:
     SDMX veri akışlarının kataloğu, yapısı, kod listeleri ve tam CSV indirmesi.
     (nsiws.tuik.gov.tr SDMX servisi API anahtarı ister; bu arka uç anonim çalışır.)
  2. Veri Portalı (veriportali.tuik.gov.tr) arama API'si: bülten tabloları (xls) ve
     indirme bağlantıları. 'X-Requested-With: XMLHttpRequest' başlığı zorunludur.

Sunucu bağlantıları zaman zaman TLS aşamasında düşüyor; her istek geri çekilmeli
yeniden denenir.
"""

import json
import time
import urllib.parse
import urllib.request

import yollar

DB = "https://databrowser2.tuik.gov.tr/api/core"
PORTAL = "https://veriportali.tuik.gov.tr"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0 Safari/537.36")
NODE = 1  # TÜİK düğümü


def _istek(url, veri=None, basliklar=None, deneme=6, zaman_asimi=900):
    yollar.indirme_izni(url)
    h = {"User-Agent": UA, "Accept": "*/*", "Accept-Language": "tr"}
    h.update(basliklar or {})
    govde = None
    if veri is not None:
        govde = json.dumps(veri).encode()
        h["Content-Type"] = "application/json"
    son_hata = None
    for i in range(deneme):
        try:
            req = urllib.request.Request(url, data=govde, headers=h,
                                         method="POST" if govde is not None else "GET")
            with urllib.request.urlopen(req, timeout=zaman_asimi) as r:
                return r.read()
        except Exception as e:  # TLS kopması, 5xx, zaman aşımı
            son_hata = e
            time.sleep(min(60, 3 * 2 ** i))
    raise RuntimeError(f"{url}: {son_hata}")


def _ds(veri_akisi, surum="1.0"):
    return f"TR,{veri_akisi},{surum}"


def katalog():
    """{veri_akisi_id: başlık} sözlüğü (510 civarı veri akışı)."""
    d = json.loads(_istek(f"{DB}/nodes/{NODE}/catalog", basliklar={"Accept": "application/json"}))
    return {k.split(",")[1]: v.get("title") for k, v in d["datasetMap"].items()}


def yapi(veri_akisi, surum="1.0"):
    return json.loads(_istek(f"{DB}/nodes/{NODE}/datasets/{_ds(veri_akisi, surum)}/structure",
                             basliklar={"Accept": "application/json"}))


def kod_listesi(veri_akisi, boyut, surum="1.0"):
    """Bir boyutun {kod: etiket} sözlüğü (etiket dili Accept-Language ile belirlenir)."""
    url = f"{DB}/nodes/{NODE}/datasets/{_ds(veri_akisi, surum)}/column/{boyut}/full/values"
    d = json.loads(_istek(url, basliklar={"Accept": "application/json"}))
    return {v["id"]: v["name"] for v in d["criteria"][0]["values"]}


def indir_csv(veri_akisi, hedef, surum="1.0", kriter=None):
    """Veri akışının tamamını (veya kritere uyan kısmını) SDMX-CSV olarak indirir.

    kriter: [{"id": "REF_AREA", "filterValues": ["TR"], "type": "CodeValues"}, ...]
    """
    bulunan = yollar.bul(hedef)  # pakette sıkıştırılmış (.gz) olarak da durabilir
    if bulunan:
        return bulunan
    url = f"{DB}/nodes/{NODE}/datasets/{_ds(veri_akisi, surum)}/download/csv"
    icerik = _istek(url, veri=kriter or [])
    with open(hedef, "wb") as f:
        f.write(icerik)
    return hedef


def portal_ara(metin, dil="tr", sayfa=1):
    """Veri Portalı araması: bültenler (type 1), veri akışları ve tablolar (type 2)."""
    govde = {"text": metin[:200], "page": sayfa, "typeIds": [], "categoryIds": [],
             "subCategoryIds": [], "years": [], "levels": [], "archive": False, "autoFilter": True}
    d = json.loads(_istek(f"{PORTAL}/api/{dil}/data/search", veri=govde,
                          basliklar={"X-Requested-With": "XMLHttpRequest",
                                     "Accept": "application/json"}))
    return d.get("data", {}).get("data", [])


def portal_indir(url, hedef):
    """Arama sonucundaki '/api/{dil}/data/downloads?...' tablo bağlantısını indirir."""
    if url.startswith("/"):
        url = PORTAL + url
    icerik = _istek(url, basliklar={"X-Requested-With": "XMLHttpRequest"})
    with open(hedef, "wb") as f:
        f.write(icerik)
    return hedef


def databrowser_kimligi(url):
    """'https://databrowser2.tuik.gov.tr/#/tr/tuik/TR,DF_X,1.0' -> ('DF_X', '1.0')."""
    parca = urllib.parse.unquote(url.rsplit("/", 1)[-1]).split(",")
    return parca[1], parca[2]
