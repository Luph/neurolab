"""TCMB EVDS3 erişimi (API anahtarı gerekmez).

EVDS3 web uygulamasının kullandığı herkese açık arka uç:
  GET  /igmevdsms-dis/serieList/fe/type=json&code=<veri grubu>  -> veri grubundaki seriler
  POST /igmevdsms-dis/fe   (JSON gövde, bkz. govde())             -> gözlemler
Frekans kodları: 1 günlük, 5 aylık, 6 üç aylık, 8 yıllık.
"""

import hashlib
import json
import os
import time

import pandas as pd
import requests

import yollar

B = "https://evds3.tcmb.gov.tr/igmevdsms-dis"
OTURUM = requests.Session()
OTURUM.headers.update({"User-Agent": "gb-cikis-stratejisi/1.0 (kamu politikasi arastirmasi)",
                       "Accept": "application/json", "Origin": "https://evds3.tcmb.gov.tr",
                       "Referer": "https://evds3.tcmb.gov.tr/"})


def _istek(yontem, url, deneme=6, **kw):
    yollar.indirme_izni(url)
    for k in range(deneme):
        try:
            r = OTURUM.request(yontem, url, timeout=120, **kw)
            if r.status_code == 200:
                time.sleep(0.6)
                return r
        except requests.RequestException:
            pass
        time.sleep(2 ** k)
    raise RuntimeError(f"EVDS3 yanıt vermedi: {url}")


def seri_listesi(veri_grubu):
    js = _istek("GET", f"{B}/serieList/fe/type=json&code={veri_grubu}").json()
    return pd.DataFrame([dict(kod=s["SERIE_CODE"], ad=s["SERIE_NAME"], ad_en=s.get("SERIE_NAME_ENG"),
                              toplama=s.get("DEFAULT_AGG_METHOD") or "avg", frekans=s.get("FREQUENCY_STR"),
                              baslangic=s.get("START_DATE"), bitis=s.get("END_DATE")) for s in js])


def govde(kodlar, toplamalar, frekans, bas, son):
    return {"type": "json", "series": "-".join(kodlar), "aggregationTypes": "-".join(toplamalar),
            "formulas": "-".join(["0"] * len(kodlar)), "startDate": bas, "endDate": son,
            "frequency": str(frekans), "decimalSeperator": ".", "decimal": "4", "dateFormat": "0",
            "lang": "tr", "yon": "1", "sira": "1", "ozelFormuller": [], "groupSeperator": False,
            "isRaporSayfasi": False}


def _kayitlar(js):
    if isinstance(js, list):
        return js
    for v in (js.get("items"), js.get("data")) if isinstance(js, dict) else ():
        if isinstance(v, list):
            return v
    return next((v for v in js.values() if isinstance(v, list) and v and isinstance(v[0], dict)), [])


def _yanit(g):
    """POST /fe yanıtı; girdi/evds3/<özet>.json varsa oradan okunur, yoksa indirilip oraya yazılır."""
    anahtar = hashlib.sha1(json.dumps(g, sort_keys=True).encode()).hexdigest()[:16]
    yol = yollar.girdi("evds3", f"fe_{g['frequency']}_{anahtar}.json")
    if os.path.exists(yol):
        with open(yol) as f:
            return json.load(f)
    js = _istek("POST", f"{B}/fe", json=g).json()
    os.makedirs(os.path.dirname(yol), exist_ok=True)
    with open(yol, "w") as f:
        json.dump({"_istek": g, **(js if isinstance(js, dict) else {"items": js})}, f, ensure_ascii=False)
    return js


def veri(kodlar, toplamalar, frekans, bas="01-01-1990", son="31-12-2026"):
    """Seri kodları -> geniş tablo (satır: dönem). Kodlar 30'luk parçalar hâlinde istenir."""
    parcalar = []
    for i in range(0, len(kodlar), 30):
        k, t = kodlar[i:i + 30], toplamalar[i:i + 30]
        x = pd.DataFrame(_kayitlar(_yanit(govde(k, t, frekans, bas, son))))
        if len(x):
            x = x.set_index(x.columns[0])
            x = x[[c for c in x.columns if c.replace("_", ".") in k or c in k]]
            x.columns = [c.replace("_", ".") for c in x.columns]
            parcalar.append(x)
    w = pd.concat(parcalar, axis=1)
    return w.apply(pd.to_numeric, errors="coerce")
