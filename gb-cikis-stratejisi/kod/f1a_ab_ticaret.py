"""Faz 1 — GB'nin 30 yıllık ticaret bilançosu: AB–Türkiye mal ticareti 1991–2025.

Kaynaklar (kimlik doğrulamasız):
  - UN Comtrade genel önizleme API'si: Türkiye'nin bildirdiği ihracat/ithalat, Dünya ve AB27
    üyeleri (bugünkü üyelik), TOTAL 1991–2025 ve HS fasılları (1995 ve 2025), ABD doları
  - Eurostat Comext DS-045409: AB27_2020 × TR ve AB27 × AB dışı, 1999–2025, HS fasılları ve
    seçilmiş HS4 pozisyonları, avro (ayna veri: AB'nin Türkiye'den ithalatı = TR ihracatı)

Notlar:
  - Comtrade'de Belçika-Lüksemburg 1998'e kadar 58 koduyla, 1999'dan sonra Belçika 56 ve
    Lüksemburg 442 (2002'den) ile raporlanır; çakışma yoktur. Almanya 1990 verisi 280 kodlu
    olduğundan seri 1991'de başlar. Çekoslovakya (1991–92) dahil değildir (küçük).
  - 1995 (GB öncesi son yıl) ile 2025 karşılaştırması Comtrade HS fasıllarıyla yapılır;
    1995 verisi HS1992, 2025 verisi HS2022 sınıflamasıdır (fasıl düzeyinde karşılaştırılabilir).

Çıktılar:
  veri/teshis_ab_ticaret_1991_2025.csv   yıllık toplamlar, AB payları, ikili denge
  veri/teshis_ab_ticaret_fasil.csv        HS fasılları: Comtrade 1995/2025 ve Comext 1999–2025
  veri/teshis_ab_ticaret_bolum.csv        HS bölümleri (I–XXI), 1995 ve 2025 payları
  veri/teshis_sektor_tarihceleri.csv      seçilmiş sektörler, Comext 1999–2025 (TR→AB, AB→TR)
"""

import argparse
import json
import os

import pandas as pd

import nazik_http
import yollar

COMTRADE = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"
COMEXT = ("https://ec.europa.eu/eurostat/api/comext/dissemination/sdmx/2.1/data/DS-045409/"
          "A.{bildiren}.{ortak}.{urun}.{akis}.VALUE_IN_EUROS?startPeriod={bas}&endPeriod={son}")
SDMX_CSV = {"Accept": "application/vnd.sdmx.data+csv;version=1.0.0"}
FASILLAR = [f"{i:02d}" for i in range(1, 100) if i not in (77, 98)]  # Comext'te 77 ve 98 tanımlı değil

# UN M49 kodları; Belçika-Lüksemburg (58) 1998'e kadar
AB27 = {40: "AT", 56: "BE", 58: "BE-LU", 100: "BG", 191: "HR", 196: "CY", 203: "CZ", 208: "DK", 233: "EE",
        246: "FI", 251: "FR", 276: "DE", 300: "GR", 348: "HU", 372: "IE", 380: "IT", 428: "LV", 440: "LT",
        442: "LU", 470: "MT", 528: "NL", 616: "PL", 620: "PT", 642: "RO", 703: "SK", 705: "SI", 724: "ES",
        752: "SE"}

HS_BOLUM = [  # (bölüm, ilk fasıl, son fasıl, ad)
    ("I", 1, 5, "Canlı hayvanlar, hayvansal ürünler"), ("II", 6, 14, "Bitkisel ürünler"),
    ("III", 15, 15, "Hayvansal ve bitkisel yağlar"), ("IV", 16, 24, "Gıda, içecek, tütün"),
    ("V", 25, 27, "Mineral ürünler ve enerji"), ("VI", 28, 38, "Kimya ve ilaç"),
    ("VII", 39, 40, "Plastik ve kauçuk"), ("VIII", 41, 43, "Deri ve kürk"), ("IX", 44, 46, "Ağaç ve mantar"),
    ("X", 47, 49, "Kâğıt ve basılı ürünler"), ("XI", 50, 63, "Tekstil ve hazır giyim"),
    ("XII", 64, 67, "Ayakkabı ve şapka"), ("XIII", 68, 70, "Taş, seramik, cam"),
    ("XIV", 71, 71, "Kıymetli taşlar ve metaller"), ("XV", 72, 83, "Ana metaller ve ürünleri"),
    ("XVI", 84, 85, "Makine ve elektrikli cihazlar"), ("XVII", 86, 89, "Taşıtlar"),
    ("XVIII", 90, 92, "Optik, ölçü ve tıbbi cihazlar"), ("XIX", 93, 93, "Silah ve mühimmat"),
    ("XX", 94, 96, "Çeşitli mamul eşya"), ("XXI", 97, 97, "Sanat eserleri"), ("—", 98, 99, "Özel kodlar"),
]

# Sektör tarihçeleri: (ad, Comext ürün kodları)
SEKTORLER = {
    "Motorlu taşıtlar ve parçaları (HS 87)": ["87"],
    "Beyaz eşya (HS 8418, 8422, 8450, 8451, 8516)": ["8418", "8422", "8450", "8451", "8516"],
    "Makine (HS 84)": ["84"],
    "Elektrikli cihazlar (HS 85)": ["85"],
    "Hazır giyim (HS 61–62)": ["61", "62"],
    "Tekstil (HS 50–60, 63)": [f"{f:02d}" for f in range(50, 61)] + ["63"],
    "Demir-çelik ve ürünleri (HS 72–73)": ["72", "73"],
    "Plastik ve kauçuk (HS 39–40)": ["39", "40"],
    "Kimya ve ilaç (HS 28–38)": [f"{f:02d}" for f in range(28, 39)],
    "Gıda ve tarım (HS 01–24)": [f"{f:02d}" for f in range(1, 25)],
}


def indir(url, yol, basliklar=None, min_aralik=0.6):
    if not os.path.exists(yol):
        r = nazik_http.get(url, headers=basliklar or {}, min_interval=min_aralik, timeout=600)
        r.raise_for_status()
        with open(yol, "wb") as f:
            f.write(r.content)
    return yol


def comtrade(yol, yil, ortaklar, urun="TOTAL"):
    url = (f"{COMTRADE}?reporterCode=792&period={yil}&partnerCode={','.join(map(str, ortaklar))}"
           f"&flowCode=X,M&cmdCode={urun}")
    with open(indir(url, yol, min_aralik=3.5)) as f:
        js = json.load(f)
    return pd.DataFrame([(yil, d["flowCode"], d["partnerCode"], d["cmdCode"], d["primaryValue"])
                         for d in js.get("data", [])],
                        columns=["yil", "akis", "ortak", "urun", "deger_usd"])


def comext(yol, urunler, ortak="TR", bildiren="EU27_2020", bas=1999, son=2025):
    url = COMEXT.format(bildiren=bildiren, ortak=ortak, urun="+".join(urunler), akis="1+2", bas=bas, son=son)
    x = pd.read_csv(indir(url, yol, SDMX_CSV), dtype={"product": str})
    x = x.rename(columns={"product": "urun", "flow": "akis", "TIME_PERIOD": "yil", "OBS_VALUE": "deger_eur"})
    return x[["urun", "akis", "yil", "deger_eur"]]


def bolum(fasil):
    f = int(fasil)
    for kod, ilk, son, ad in HS_BOLUM:
        if ilk <= f <= son:
            return kod, ad
    return "—", "Özel kodlar"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=yollar.GIRDI)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    c = os.path.join(a.cache, "f1")
    os.makedirs(c, exist_ok=True)

    # 1) Comtrade: Türkiye'nin bildirdiği toplamlar, Dünya + AB27, 1991–2025
    t = pd.concat([comtrade(os.path.join(c, f"ct_toplam_{y}.json"), y, [0] + list(AB27)) for y in range(1991, 2026)])
    t["grup"] = t.ortak.map(lambda o: "dunya" if o == 0 else "ab27")
    y = t.pivot_table(index="yil", columns=["akis", "grup"], values="deger_usd", aggfunc="sum") / 1e6
    seri = pd.DataFrame({
        "tr_ihracat_dunya_musd": y[("X", "dunya")], "tr_ihracat_ab27_musd": y[("X", "ab27")],
        "tr_ithalat_dunya_musd": y[("M", "dunya")], "tr_ithalat_ab27_musd": y[("M", "ab27")],
    })
    seri["ab27_ihracat_payi"] = seri.tr_ihracat_ab27_musd / seri.tr_ihracat_dunya_musd
    seri["ab27_ithalat_payi"] = seri.tr_ithalat_ab27_musd / seri.tr_ithalat_dunya_musd
    seri["ab27_denge_musd"] = seri.tr_ihracat_ab27_musd - seri.tr_ithalat_ab27_musd
    seri["ab27_disi_denge_musd"] = ((seri.tr_ihracat_dunya_musd - seri.tr_ihracat_ab27_musd)
                                    - (seri.tr_ithalat_dunya_musd - seri.tr_ithalat_ab27_musd))

    # 2) Comext: AB27 ayna verisi (avro) ve Türkiye'nin AB dışı ticaretteki payı, 1999–2025
    tr = comext(os.path.join(c, "cx_ab27_tr_toplam.csv"), ["TOTAL"])
    dis = comext(os.path.join(c, "cx_ab27_extra_toplam.csv"), ["TOTAL"], ortak="EXT_EU27_2020")
    tr = tr.pivot_table(index="yil", columns="akis", values="deger_eur") / 1e6
    dis = dis.pivot_table(index="yil", columns="akis", values="deger_eur") / 1e6
    seri["ab_tr_ithalati_meur"] = tr[1]
    seri["ab_tr_ihracati_meur"] = tr[2]
    seri["tr_payi_ab_disi_ithalat"] = tr[1] / dis[1]
    seri["tr_payi_ab_disi_ihracat"] = tr[2] / dis[2]
    seri.index.name = "yil"
    seri.round(4).to_csv(os.path.join(a.out, "teshis_ab_ticaret_1991_2025.csv"))

    # 3) Fasıl kompozisyonu: Comtrade 1995 ve 2025 (her ortak için ayrı çağrı; 500 kayıt sınırı)
    parcalar = []
    for yil in (1995, 2025):
        ortaklar = [0] + [o for o in AB27 if (o != 58 or yil < 1999) and (o not in (56, 442) or yil >= 1999)]
        for o in ortaklar:
            parcalar.append(comtrade(os.path.join(c, f"ct_ag2_{yil}_{o}.json"), yil, [o], urun="AG2"))
    f = pd.concat(parcalar)
    f["grup"] = f.ortak.map(lambda o: "dunya" if o == 0 else "ab27")
    ct = f.pivot_table(index="urun", columns=["yil", "akis", "grup"], values="deger_usd", aggfunc="sum") / 1e6
    ct.columns = [f"ct_{yil}_{'ihr' if ak == 'X' else 'ith'}_{g}_musd" for yil, ak, g in ct.columns]

    cx = comext(os.path.join(c, "cx_ab27_tr_fasil.csv"), FASILLAR)
    cx = cx[cx.yil.isin([1999, 2005, 2010, 2015, 2020, 2025])]
    cx = cx.pivot_table(index="urun", columns=["yil", "akis"], values="deger_eur", aggfunc="sum") / 1e6
    cx.columns = [f"cx_{yil}_{'tr_ihr' if ak == 1 else 'tr_ith'}_meur" for yil, ak in cx.columns]
    fasil = ct.join(cx, how="outer").fillna(0)
    fasil.index.name = "fasil"
    fasil.insert(0, "bolum", [bolum(i)[0] for i in fasil.index])
    fasil.round(2).to_csv(os.path.join(a.out, "teshis_ab_ticaret_fasil.csv"))

    b = fasil.copy()
    b["ad"] = [bolum(i)[1] for i in b.index]
    b = b.groupby(["bolum", "ad"], sort=False).sum(numeric_only=True)
    sira = {k: i for i, (k, *_r) in enumerate(HS_BOLUM)}
    b = b.sort_index(key=lambda s: s.map(sira) if s.name == "bolum" else s)
    out = pd.DataFrame(index=b.index)
    for yil in (1995, 2025):
        for ak in ("ihr", "ith"):
            sut = f"ct_{yil}_{ak}_ab27_musd"
            out[f"{ak}_ab27_{yil}_musd"] = b[sut]
            out[f"{ak}_ab27_{yil}_pay"] = b[sut] / b[sut].sum()
            out[f"{ak}_ab27_payi_dunya_{yil}"] = b[sut] / b[f"ct_{yil}_{ak}_dunya_musd"]
    out.round(4).to_csv(os.path.join(a.out, "teshis_ab_ticaret_bolum.csv"))

    # 4) Sektör tarihçeleri: Comext 1999–2025
    kodlar = sorted({k for v in SEKTORLER.values() for k in v if len(k) == 4})
    s4 = comext(os.path.join(c, "cx_ab27_tr_hs4_secili.csv"), kodlar)
    hs2 = comext(os.path.join(c, "cx_ab27_tr_fasil.csv"), FASILLAR)
    hepsi = pd.concat([hs2, s4])
    satirlar = []
    for ad, urunler in SEKTORLER.items():
        g = hepsi[hepsi.urun.isin(urunler)].groupby(["yil", "akis"]).deger_eur.sum().unstack() / 1e6
        for yil, r in g.iterrows():
            satirlar.append(dict(sektor=ad, yil=yil, tr_ab_ihracat_meur=r.get(1), ab_tr_ihracat_meur=r.get(2)))
    st = pd.DataFrame(satirlar)
    st["denge_meur"] = st.tr_ab_ihracat_meur - st.ab_tr_ihracat_meur
    st.round(1).to_csv(os.path.join(a.out, "teshis_sektor_tarihceleri.csv"), index=False)

    pd.set_option("display.width", 200)
    print(seri.loc[[1991, 1995, 1996, 2000, 2005, 2010, 2015, 2020, 2024, 2025]].round(3).to_string())
    print(out.round(3).to_string())
    print(st[st.yil.isin([1999, 2025])].round(0).to_string(index=False))


if __name__ == "__main__":
    main()
