"""TÜİK Yıllık Sanayi Ürün (PRODCOM/PRODTR) İstatistikleri: ürün düzeyinde üretimden satış ve girişim sayısı.

Kaynak: TÜİK Veri Portalı, "Yıllık Sanayi Ürün (PRODCOM) İstatistikleri, 2025" bülteni (26.6.2026) istatistik
tabloları: "Sanayi Ürünleri Satış Değeri" (TL, 2005–2025), "Sanayi Ürünleri Girişim Sayısı" (2005–2025),
"Yıllık Sanayi Ürün İstatistikleri Kod Listesi" (PRODTR 2025). Kodlar CPA 2.2 (6 hane), PRODCOM (8 hane)
ve PRODTR (10 hane) düzeylerinde; "c" gizli veri demektir (az sayıda girişim).
"""

import json
import os

import pandas as pd

import tuik

BULTEN = 58065
TABLOLAR = {"Sanayi Ürünleri Satış Değeri": "satis_degeri", "Sanayi Ürünleri Girişim Sayısı": "girisim_sayisi",
            "Yıllık Sanayi Ürün İstatistikleri Kod Listesi": "kod_listesi"}


def indir(klasor, bulten=BULTEN):
    os.makedirs(klasor, exist_ok=True)
    d = json.loads(tuik._istek(f"{tuik.PORTAL}/api/tr/press/{bulten}",
                               basliklar={"X-Requested-With": "XMLHttpRequest", "Accept": "application/json"}))
    yollar = {}
    for it in d["data"]["statisticalTables"]:
        ad = TABLOLAR.get(it["title"])
        if ad:
            yol = os.path.join(klasor, ad + ".xls")
            if not os.path.exists(yol):
                tuik.portal_indir(it["url"], yol)
            yollar[ad] = yol
    return yollar


def _uzun(yol):
    t = pd.read_excel(yol, header=None, dtype=str)
    baslik = t.iloc[3].tolist()
    t = t.iloc[4:].copy()
    t.columns = ["kod"] + baslik[1:]
    t["kod"] = t.kod.str.strip()
    return t


def cpa6(klasor, yil="2025"):
    """CPA 6 hane düzeyinde üretimden satış (TL) ve girişim sayısı; gizli satırlar işaretli."""
    y = indir(klasor)
    s, g = _uzun(y["satis_degeri"]), _uzun(y["girisim_sayisi"])
    sy = next(c for c in s.columns if str(c).startswith(yil))
    gy = next(c for c in g.columns if str(c).startswith(yil))
    s = s[s.kod.str.fullmatch(r"\d\d\.\d\d\.\d\d", na=False)][["kod", sy]].rename(columns={sy: "satis"})
    g = g[g.kod.str.fullmatch(r"\d\d\.\d\d\.\d\d", na=False)][["kod", gy]].rename(columns={gy: "girisim"})
    t = s.merge(g, on="kod", how="outer")
    t["gizli"] = t.satis.eq("c") | t.girisim.eq("c")
    t["satis_tl"] = pd.to_numeric(t.satis, errors="coerce")
    t["girisim"] = pd.to_numeric(t.girisim, errors="coerce")
    return t[["kod", "satis_tl", "girisim", "gizli"]].rename(columns={"kod": "cpa22"})
