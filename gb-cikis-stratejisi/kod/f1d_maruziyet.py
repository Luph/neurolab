"""Faz 1 — Bölüm düzeyinde AB maruziyet haritası (NACE Rev. 2, 2 hane).

Her bölüm için:
  - Türkiye'nin dünyaya ihracatı (UN Comtrade 2025, HS6 → NACE eşleştirmesi) ve AB'ye ihracatı
    (Comext 2025 ayna veri, CN8 → NACE; cn2025_nace_rejim.csv)
  - üretim değeri, çalışan ve faktör maliyetiyle katma değer (TÜİK YSHİ 2024; tuik_yshi_nace2.csv)
  - S4 tarife duvarı (s4_tarife_duvari_bolum.csv): AB'nin uygulayacağı ağırlıklı MFN ve σ=5 ile
    statik ihracat kaybı
Türetilen göstergeler:
  ab_payi_ihracat       = AB'ye ihracat / dünyaya ihracat (ikisi de aynı HS6 → bölüm eşleştirmesiyle;
                          kaynak farkı nedeniyle 1'i aşan değerler boş bırakılır)
  ab_ihracat_yogunlugu  = AB'ye ihracat / üretim değeri (2025 ihracatı / 2024 üretimi; yıl farkı
                          nedeniyle yaklaşık)
  maruz_istihdam        = çalışan × ab_ihracat_yogunlugu (doğrudan; girdi bağlantıları hariç)
  s4_risk_istihdam      = çalışan × (σ=5 statik ihracat kaybı / üretim değeri); telafi, yeniden
                          yönlendirme ve kur tepkisi içermeyen kaba üst sınır
Para birimi: milyon ABD doları; avro tutarları 2025 ortalama EUR/USD paritesiyle çevrilir
(teshis_odemeler_dengesi.csv, TCMB kurları).

Çıktı: veri/teshis_bolum_maruziyet.csv
"""

import argparse
import os

import pandas as pd

BOLUM_AD = {
    "05": "Kömür ve linyit çıkartılması", "06": "Ham petrol ve doğal gaz çıkarımı",
    "07": "Metal cevherleri madenciliği", "08": "Diğer madencilik ve taş ocakçılığı",
    "09": "Madenciliği destekleyici hizmetler", "10": "Gıda ürünleri", "11": "İçecekler",
    "12": "Tütün ürünleri", "13": "Tekstil ürünleri", "14": "Giyim eşyası", "15": "Deri ve ilgili ürünler",
    "16": "Ağaç ve mantar ürünleri (mobilya hariç)", "17": "Kâğıt ve kâğıt ürünleri",
    "18": "Basım ve kayıtlı medyanın çoğaltılması", "19": "Kok ve rafine petrol ürünleri",
    "20": "Kimyasallar ve kimyasal ürünler", "21": "Temel eczacılık ürünleri", "22": "Kauçuk ve plastik ürünler",
    "23": "Metalik olmayan mineral ürünler", "24": "Ana metal sanayii", "25": "Fabrikasyon metal ürünleri",
    "26": "Bilgisayar, elektronik ve optik ürünler", "27": "Elektrikli teçhizat", "28": "Makine ve ekipman (bys)",
    "29": "Motorlu kara taşıtları ve parçaları", "30": "Diğer ulaşım araçları", "31": "Mobilya",
    "32": "Diğer imalat", "33": "Makine ve ekipman kurulumu ve onarımı",
    "35": "Elektrik, gaz, buhar ve iklimlendirme", "38": "Atık toplama, ıslah; geri kazanım",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--comtrade-hs6", required=True, help="comtrade_tur_hs6_world_2025.csv.gz (comtrade_tr_hs6.py)")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    v = lambda f: os.path.join(a.out, f)  # noqa: E731

    od = pd.read_csv(v("teshis_odemeler_dengesi.csv"), index_col=0)
    eurusd = od.loc[2025, "eur_try"] / od.loc[2025, "usd_try"]

    m = pd.read_csv(v("cn2025_nace_rejim.csv"), dtype={"cn8": str, "nace2": str})
    m = m[m.cn8.str.fullmatch(r"\d{8}") & m.nace2.str.fullmatch(r"\d\d\.\d\d")].copy()
    m["bolum"] = m.nace2.str[:2]
    m["hs6"] = m.cn8.str[:6]
    ab = m.groupby("bolum").tr_ihr_ab.sum() / 1e6 * eurusd
    ab_gb = m[m.rejim.isin(["GB", "ITU"])].groupby("bolum").tr_ihr_ab.sum() / 1e6 * eurusd

    # HS6 → bölüm: AB'ye ihracatı en büyük CN8 satırının bölümü; ticaret yoksa en çok satırı olan bölüm
    e = m.groupby(["hs6", "bolum"]).agg(deger=("tr_ihr_ab", "sum"), satir=("cn8", "size")).reset_index()
    e = e.sort_values(["hs6", "deger", "satir"], ascending=[True, False, False]).drop_duplicates("hs6")
    hs6_bolum = e.set_index("hs6").bolum

    c = pd.read_csv(a.comtrade_hs6, dtype={"cmdCode": str})
    c = c[(c.flowCode == "X") & (c.partnerCode == 0) & c.cmdCode.str.fullmatch(r"\d{6}")]
    c["bolum"] = c.cmdCode.map(hs6_bolum)
    eslesme = c.loc[c.bolum.notna(), "primaryValue"].sum() / c.primaryValue.sum()
    dunya = c.groupby("bolum").primaryValue.sum() / 1e6
    # AB payı için pay ve payda aynı HS6 → bölüm eşleştirmesiyle toplanır
    ab_hs6 = (m.groupby("hs6").tr_ihr_ab.sum() / 1e6 * eurusd).rename("ab").to_frame()
    ab_hs6["bolum"] = ab_hs6.index.map(hs6_bolum)
    ab_ayni = ab_hs6.groupby("bolum").ab.sum()

    y = pd.read_csv(v("tuik_yshi_nace2.csv"), dtype={"kod": str})
    y = y[(y.yil == 2024) & (y.kod.str.len() == 2)].set_index("kod")

    s4 = pd.read_csv(v("s4_tarife_duvari_bolum.csv"), dtype={"bolum": str}).set_index("bolum")

    t = pd.DataFrame(index=sorted(set(BOLUM_AD) & (set(y.index) | set(ab.index))))
    t.index.name = "bolum"
    t["ad"] = t.index.map(BOLUM_AD)
    t["calisan_2024"] = y.calisan
    t["uretim_degeri_2024_musd"] = y.uretim_degeri_musd
    t["katma_deger_2024_musd"] = y.faktor_maliyetiyle_kd_musd
    t["tr_ihr_dunya_2025_musd"] = dunya
    t["tr_ihr_ab_2025_musd"] = ab
    t["tr_ihr_ab_gb_itu_2025_musd"] = ab_gb
    # Comext (AB ithalatı, CIF) ile Comtrade (TR ihracatı, FOB) farklı kaynaklar; pay > 1 ise tutarsız
    t["ab_payi_ihracat"] = (ab_ayni / t.tr_ihr_dunya_2025_musd).where(lambda x: x <= 1)
    t["ab_ihracat_yogunlugu"] = t.tr_ihr_ab_2025_musd / t.uretim_degeri_2024_musd
    t["s4_ab_oran_yuzde"] = s4.ab_oran_yuzde
    t["s4_ab_vergisi_musd"] = s4.ab_vergisi_meur * eurusd
    t["s4_ihracat_kaybi_sigma5_musd"] = -s4.ihracat_degisimi_sigma5_meur * eurusd
    t["s4_kayip_uretim_payi"] = t.s4_ihracat_kaybi_sigma5_musd / t.uretim_degeri_2024_musd
    t["maruz_istihdam"] = t.calisan_2024 * t.ab_ihracat_yogunlugu.clip(upper=1)
    t["s4_risk_istihdam"] = t.calisan_2024 * t.s4_kayip_uretim_payi.clip(upper=1)
    t.round(4).to_csv(v("teshis_bolum_maruziyet.csv"))

    imalat = t.loc[[b for b in t.index if "10" <= b <= "33"]]
    print(f"EUR/USD 2025 = {eurusd:.4f}; HS6→bölüm eşleşmesi TR ihracat değerinin %{100 * eslesme:.1f}'i")
    print("İmalat (10–33): çalışan", int(imalat.calisan_2024.sum()), "| AB'ye ihracat", round(imalat.tr_ihr_ab_2025_musd.sum()),
          "| dünyaya ihracat", round(imalat.tr_ihr_dunya_2025_musd.sum()), "| maruz istihdam",
          int(imalat.maruz_istihdam.sum()), "| S4 risk istihdamı (σ=5)", int(imalat.s4_risk_istihdam.sum()))
    pd.set_option("display.width", 250)
    print(t.drop(columns=["ad"]).sort_values("s4_risk_istihdam", ascending=False).round(3).to_string())


if __name__ == "__main__":
    main()
