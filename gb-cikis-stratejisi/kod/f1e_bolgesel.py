"""Faz 1 — Bölgesel yoğunlaşma: AB maruziyeti ve S4 risk istihdamının İBBS-2 bölgelerine dağılımı.

Kaynak: SGK İstatistik Yıllığı 2025, Bölüm 1, Tablo 1.11 (4/1-a zorunlu sigortalılar, faaliyet
bölümü × il). Yıllık zip SGK istatistik sayfasından indirilir (--sgk-xlsx ile yerel dosya da verilebilir).
Bölüm oranları teshis_bolum_maruziyet.csv'den alınır (f1d_maruziyet.py):
  maruz_istihdam_r   = Σ_b sigortalı_rb × ab_ihracat_yogunlugu_b
  s4_risk_istihdam_r = Σ_b sigortalı_rb × s4_kayip_uretim_payi_b
Varsayım: bir bölümün AB ihracat yoğunluğu ve S4 kayıp oranı bütün illerde aynıdır (il düzeyinde
ihracat bileşimi Faz 3'te TİM/Ticaret Bakanlığı il verisiyle düzeltilecek).

Çıktı: veri/teshis_bolgesel_maruziyet.csv
"""

import argparse
import html
import io
import os
import re
import zipfile

import pandas as pd

import nazik_http
import yollar

SGK_SAYFA = "https://www.sgk.gov.tr/Istatistik/Yillik/fcd5e59b-6af9-4d90-a451-ee7500eb1cb4/"
SGK_DOSYA = "YILLIK BÖLÜM 1 Sigortalı ve İş Yeri İstatistikleri_{y}.xlsx"

IBBS2 = {
    "TR10": ("İstanbul", ["İstanbul"]),
    "TR21": ("Tekirdağ, Edirne, Kırklareli", ["Tekirdağ", "Edirne", "Kırklareli"]),
    "TR22": ("Balıkesir, Çanakkale", ["Balıkesir", "Çanakkale"]),
    "TR31": ("İzmir", ["İzmir"]),
    "TR32": ("Aydın, Denizli, Muğla", ["Aydın", "Denizli", "Muğla"]),
    "TR33": ("Manisa, Afyonkarahisar, Kütahya, Uşak", ["Manisa", "Afyonkarahisar", "Kütahya", "Uşak"]),
    "TR41": ("Bursa, Eskişehir, Bilecik", ["Bursa", "Eskişehir", "Bilecik"]),
    "TR42": ("Kocaeli, Sakarya, Düzce, Bolu, Yalova", ["Kocaeli", "Sakarya", "Düzce", "Bolu", "Yalova"]),
    "TR51": ("Ankara", ["Ankara"]),
    "TR52": ("Konya, Karaman", ["Konya", "Karaman"]),
    "TR61": ("Antalya, Isparta, Burdur", ["Antalya", "Isparta", "Burdur"]),
    "TR62": ("Adana, Mersin", ["Adana", "Mersin"]),
    "TR63": ("Hatay, Kahramanmaraş, Osmaniye", ["Hatay", "Kahramanmaraş", "Osmaniye"]),
    "TR71": ("Kırıkkale, Aksaray, Niğde, Nevşehir, Kırşehir", ["Kırıkkale", "Aksaray", "Niğde", "Nevşehir", "Kırşehir"]),
    "TR72": ("Kayseri, Sivas, Yozgat", ["Kayseri", "Sivas", "Yozgat"]),
    "TR81": ("Zonguldak, Karabük, Bartın", ["Zonguldak", "Karabük", "Bartın"]),
    "TR82": ("Kastamonu, Çankırı, Sinop", ["Kastamonu", "Çankırı", "Sinop"]),
    "TR83": ("Samsun, Tokat, Çorum, Amasya", ["Samsun", "Tokat", "Çorum", "Amasya"]),
    "TR90": ("Trabzon, Ordu, Giresun, Rize, Artvin, Gümüşhane",
             ["Trabzon", "Ordu", "Giresun", "Rize", "Artvin", "Gümüşhane"]),
    "TRA1": ("Erzurum, Erzincan, Bayburt", ["Erzurum", "Erzincan", "Bayburt"]),
    "TRA2": ("Ağrı, Kars, Iğdır, Ardahan", ["Ağrı", "Kars", "Iğdır", "Ardahan"]),
    "TRB1": ("Malatya, Elazığ, Bingöl, Tunceli", ["Malatya", "Elazığ", "Bingöl", "Tunceli"]),
    "TRB2": ("Van, Muş, Bitlis, Hakkari", ["Van", "Muş", "Bitlis", "Hakkari"]),
    "TRC1": ("Gaziantep, Adıyaman, Kilis", ["Gaziantep", "Adıyaman", "Kilis"]),
    "TRC2": ("Şanlıurfa, Diyarbakır", ["Şanlıurfa", "Diyarbakır"]),
    "TRC3": ("Mardin, Batman, Şırnak, Siirt", ["Mardin", "Batman", "Şırnak", "Siirt"]),
}


def sgk_tablo(xlsx):
    """Tablo 1.11 → uzun biçim (bölüm, il, ölçü, değer)."""
    ham = pd.read_excel(xlsx, sheet_name="TABLO-1.11", header=None, dtype=str)
    il = ham.iloc[5].ffill()
    olcu = ham.iloc[6].fillna("").str.split("\n").str[0].str.strip()
    satirlar = []
    for i in range(8, len(ham)):
        kod = ham.iat[i, 0]
        if not isinstance(kod, str) or not re.fullmatch(r"\d{2}", kod.strip()):
            continue
        for j in range(2, ham.shape[1]):
            v = pd.to_numeric(str(ham.iat[i, j]).replace(",", ""), errors="coerce")
            if pd.notna(v):
                satirlar.append((kod.strip(), str(il[j]).strip(), olcu[j], float(v)))
    return pd.DataFrame(satirlar, columns=["bolum", "il", "olcu", "deger"])


def sgk_indir(onbellek, yil):
    yol = os.path.join(onbellek, f"sgk_yillik_{yil}.zip")
    if not os.path.exists(yol):
        sayfa = nazik_http.get(SGK_SAYFA, timeout=120).text
        baglanti = None
        for m in re.finditer(r'<a[^>]+href="(/download/downloadfile[^"]+)"[^>]*>(.*?)</a>', sayfa, re.S):
            metin = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(2)))).strip()
            if metin.startswith(f"{yil} yılı istatistik"):
                baglanti = html.unescape(m.group(1))
                break
        r = nazik_http.get("https://www.sgk.gov.tr" + baglanti, timeout=600)
        r.raise_for_status()
        with open(yol, "wb") as f:
            f.write(r.content)
    z = zipfile.ZipFile(yol)
    ad = next(n for n in z.namelist() if n.endswith(SGK_DOSYA.format(y=yil)))
    return io.BytesIO(z.read(ad))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sgk-xlsx", help="SGK yıllığı Bölüm 1 xlsx (verilmezse indirilir)")
    ap.add_argument("--yil", default="2025")
    ap.add_argument("--cache", default=yollar.GIRDI)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    os.makedirs(a.cache, exist_ok=True)

    s = sgk_tablo(a.sgk_xlsx or sgk_indir(a.cache, a.yil))
    s = s[s.olcu.str.startswith("Sigortal") & s.bolum.between("10", "33")]
    il_bolge = {il: k for k, (_ad, iller) in IBBS2.items() for il in iller}
    s["ibbs2"] = s.il.map(il_bolge)
    eksik = sorted(set(s.il[s.ibbs2.isna()]))
    s = s[s.ibbs2.notna()]

    m = pd.read_csv(os.path.join(a.out, "teshis_bolum_maruziyet.csv"), dtype={"bolum": str}).set_index("bolum")
    s["maruz"] = s.deger * s.bolum.map(m.ab_ihracat_yogunlugu.clip(upper=1)).fillna(0)
    s["risk"] = s.deger * s.bolum.map(m.s4_kayip_uretim_payi.clip(lower=0, upper=1)).fillna(0)
    s["risk_14_29"] = s.risk.where(s.bolum.isin(["14", "29"]), 0)
    t = s.groupby("ibbs2").agg(imalat_sigortali=("deger", "sum"), maruz_istihdam=("maruz", "sum"),
                               s4_risk_istihdam=("risk", "sum"), s4_risk_giyim_otomotiv=("risk_14_29", "sum"))
    t.insert(0, "bolge", t.index.map(lambda k: IBBS2[k][0]))
    t["maruz_pay"] = t.maruz_istihdam / t.imalat_sigortali
    t["s4_risk_pay"] = t.s4_risk_istihdam / t.imalat_sigortali
    t["s4_risk_ulusal_pay"] = t.s4_risk_istihdam / t.s4_risk_istihdam.sum()
    t = t.sort_values("s4_risk_istihdam", ascending=False)
    t.round(4).to_csv(os.path.join(a.out, "teshis_bolgesel_maruziyet.csv"))

    print("Eşleşmeyen il adları:", eksik)
    print("İmalat 4/a sigortalı (10–33):", int(t.imalat_sigortali.sum()), "| maruz", int(t.maruz_istihdam.sum()),
          "| S4 risk", int(t.s4_risk_istihdam.sum()))
    pd.set_option("display.width", 220)
    print(t.round(3).to_string())


if __name__ == "__main__":
    main()
