"""Faz 3 — NACE sınıfı düzeyinde üretim yapısı, ölçek, bölgesel yoğunlaşma ve AB'ye göre verimlilik (kart alan 2).

Kaynak:
  - TÜİK Yıllık Sanayi ve Hizmet İstatistikleri (veri/tuik_yshi_nace2.csv; 2015–2024): girişim, çalışan, üretim değeri,
    faktör maliyetiyle katma değer, personel gideri ($, yıllık ortalama kurla)
  - TÜİK İş Kayıtları (veri/tuik_girisim_ibbs2_nace2.csv; 2024): İBBS-2 × sınıf × büyüklük grubu girişim sayısı
  - Eurostat SBS (sbs_ovw_act; AB27; 2022–2023): kişi başı katma değer (LABPRY_TEUR), istihdam, katma değer
  - TCMB ödemeler dengesi tablosundaki GSYH ($; veri/teshis_odemeler_dengesi.csv)
  - SGK İstatistik Yıllığı 2025, Tablo 1.11 (4/1-a sigortalı, bölüm × il; f1e_bolgesel.py ile aynı dosya)
Bölgesel istihdam tahmini `[T]`: iş kayıtlarındaki girişim sayısı × büyüklük grubu orta değeri (0: 1, 1–9: 3, 10–49: 22,
  50–249: 105; 250+ sınıf çalışanına kalibre) tohum matrisi verir; gizli hücreler TR kenar değerinden doldurulur. Tohum,
  her bölümde satırı YSHİ sınıf çalışanı, sütunu SGK bölüm × İBBS-2 sigortalısı olan RAS ile uyarlanır.
AB'ye göre verimlilik: TR kişi başı KD (2024, $) / AB27 kişi başı KD (son yıl, € × yıllık ortalama $/€) `[T]`;
  nominal kur, fiyat düzeyi farkı düzeltilmedi.
Çıktı: veri/f3_yapi_sinif.csv, veri/f3_bolge_sinif.csv (sınıf × ilk 3 İBBS-2 bölgesi).
"""

import argparse
import json
import os

import numpy as np
import pandas as pd
from scipy.optimize import nnls

import f1e_bolgesel as f1e
import nazik_http
import yollar

SBS_URL = ("https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sbs_ovw_act?format=JSON&geo=EU27_2020"
           "&time=2022&time=2023&indic_sbs=LABPRY_TEUR&indic_sbs=EMP_NR&indic_sbs=AV_MEUR&indic_sbs=ENT_NR")
USD_EUR = {2022: 1.0530, 2023: 1.0813}          # ECB yıllık ortalama referans kur ($/€) [V]
BUYUK = ["g_0", "g_1_9", "g_10_49", "g_50_249", "g_250p"]
ORTA = {"g_0": 1, "g_1_9": 3, "g_10_49": 22, "g_50_249": 105}
IBBS2_AD = {"TR10": "İstanbul", "TR21": "Tekirdağ, Edirne, Kırklareli", "TR22": "Balıkesir, Çanakkale",
            "TR31": "İzmir", "TR32": "Aydın, Denizli, Muğla", "TR33": "Manisa, Afyon, Kütahya, Uşak",
            "TR41": "Bursa, Eskişehir, Bilecik", "TR42": "Kocaeli, Sakarya, Düzce, Bolu, Yalova", "TR51": "Ankara",
            "TR52": "Konya, Karaman", "TR61": "Antalya, Isparta, Burdur", "TR62": "Adana, Mersin",
            "TR63": "Hatay, Kahramanmaraş, Osmaniye", "TR71": "Kırıkkale, Aksaray, Niğde, Nevşehir, Kırşehir",
            "TR72": "Kayseri, Sivas, Yozgat", "TR81": "Zonguldak, Karabük, Bartın", "TR82": "Kastamonu, Çankırı, Sinop",
            "TR83": "Samsun, Tokat, Çorum, Amasya", "TR90": "Trabzon, Ordu, Giresun, Rize, Artvin, Gümüşhane",
            "TRA1": "Erzurum, Erzincan, Bayburt", "TRA2": "Ağrı, Kars, Iğdır, Ardahan", "TRB1": "Malatya, Elazığ, Bingöl, Tunceli",
            "TRB2": "Van, Muş, Bitlis, Hakkari", "TRC1": "Gaziantep, Adıyaman, Kilis", "TRC2": "Şanlıurfa, Diyarbakır",
            "TRC3": "Mardin, Batman, Şırnak, Siirt"}


def sbs(cache):
    yol = os.path.join(cache, "eurostat", "sbs_ovw_act_eu27_2022_2023.json")
    if not os.path.exists(yol):
        r = nazik_http.get(SBS_URL, timeout=600)
        r.raise_for_status()
        os.makedirs(os.path.dirname(yol), exist_ok=True)
        with open(yol, "w", encoding="utf-8") as f:
            f.write(r.text)
    d = json.load(open(yol, encoding="utf-8"))
    boyut, sira = d["id"], d["size"]
    kat = {k: {v: i for v, i in d["dimension"][k]["category"]["index"].items()} for k in boyut}
    ters = {k: {i: v for v, i in kat[k].items()} for k in boyut}
    satirlar = []
    carpan = np.cumprod([1] + sira[::-1])[::-1][1:]
    for anahtar, deger in d["value"].items():
        n, kalan = int(anahtar), {}
        for k, c in zip(boyut, carpan):
            kalan[k], n = ters[k][n // c], n % c
        satirlar.append(dict(nace=kalan["nace_r2"], gosterge=kalan["indic_sbs"], yil=int(kalan["time"]), deger=deger))
    s = pd.DataFrame(satirlar)
    s = s[s.nace.str.fullmatch(r"C\d{4}")].copy()
    s["kod"] = s.nace.str[1:3] + "." + s.nace.str[3:5]
    son = s.sort_values("yil").groupby(["kod", "gosterge"]).last().reset_index()
    p = son.pivot(index="kod", columns="gosterge", values="deger")
    p["ab_yil"] = son[son.gosterge == "LABPRY_TEUR"].set_index("kod").yil
    return p


def ulusal_kenar(tr, girisim, calisan):
    """TR düzeyinde gizli büyüklük grubu sayıları. Kayıt/YSHİ girişim oranı tam sınıfların medyanından alınır; kalan girişim
    sayısı gizli gruplara, (i) sayı ve (ii) çalışan kalanını birlikte tutturan, imalat geneli grup paylarına çekilmiş
    negatif olmayan en küçük kareler çözümüyle dağıtılır [T]. 250+ grubunun tipik büyüklüğü 500 alınır."""
    tr = tr.copy()
    tam = tr[BUYUK].notna().all(axis=1) & girisim.reindex(tr.index).gt(0)
    oran = float((tr.loc[tam, BUYUK].sum(axis=1) / girisim.reindex(tr.index)[tam]).median())
    c = tr[tr.index.str.match(r"^(1\d|2\d|3[0-3])\.")]
    onsel = c[BUYUK].sum() / c[BUYUK].sum().sum()
    orta = pd.Series({**ORTA, "g_250p": 500})
    for kod in tr.index[tr[BUYUK].isna().any(axis=1)]:
        g = [k for k in BUYUK if pd.isna(tr.at[kod, k])]
        bilinen = [k for k in BUYUK if k not in g]
        n_kalan = oran * girisim.get(kod, np.nan) - tr.loc[kod, bilinen].sum()
        if not n_kalan > 0:
            tr.loc[kod, g] = np.nan
            continue
        p = onsel[g] / onsel[g].sum() * n_kalan
        satirlar, hedef = [np.ones(len(g))], [n_kalan]
        e_kalan = calisan.get(kod, np.nan) - (tr.loc[kod, bilinen] * orta[bilinen]).sum()
        if e_kalan > 0:
            satirlar.append(orta[g].values / 100)
            hedef.append(e_kalan / 100)
        A = np.vstack(satirlar + [np.sqrt(0.1) * np.eye(len(g))])
        y = np.concatenate([hedef, np.sqrt(0.1) * p.values])
        tr.loc[kod, g] = nnls(A, y)[0]
    return tr


def kayit_tohum(r, girisim, calisan):
    """İş kayıtlarından İBBS-2 × sınıf istihdam tohumu. Bölgesel gizli hücrelere TR kenar değerinden (gerekirse
    ulusal_kenar tahmini) açıklanan bölgeler düşülüp kalan eşit dağıtılır; kenar yoksa hücre başına 1,5 girişim [T].
    250+ grubunun ortalama büyüklüğü sınıfın YSHİ çalışan sayısına kalibre edilir (alt sınır 250, veri yoksa 500)."""
    tr = ulusal_kenar(r[r.ibbs2.eq("TR")].set_index("kod"), girisim, calisan)
    b = r[r.ibbs2.ne("TR")].copy()
    for k in BUYUK:
        bilinen = b.groupby("kod")[k].sum()
        gizli = b[k].isna().groupby(b.kod).sum()
        kalan = (tr[k].reindex(bilinen.index) - bilinen).clip(lower=0)
        b[k] = b[k].fillna(b.kod.map(kalan / gizli.replace(0, np.nan)).fillna(1.5))
    kucuk = sum(b[k] * w for k, w in ORTA.items())
    n250 = b.groupby("kod").g_250p.sum()
    kucuk_top = kucuk.groupby(b.kod).sum()
    buyuk_ort = ((calisan.reindex(n250.index) - kucuk_top) / n250.replace(0, np.nan)).clip(lower=250).fillna(500)
    b["tohum"] = kucuk + b.g_250p * b.kod.map(buyuk_ort)
    return b[["kod", "ibbs2", "tohum"]], buyuk_ort, n250, tr


def ras(t, satir, sutun, tekrar=1000):
    """İki yönlü orantılı uyarlama: satır = YSHİ sınıf çalışanı, sütun = SGK bölüm × bölge sigortalısı (ölçekli)."""
    m = t.copy()
    for _ in range(tekrar):
        m = m.mul(sutun / m.sum(axis=0).replace(0, np.nan), axis=1).fillna(0)
        m = m.mul(satir / m.sum(axis=1).replace(0, np.nan), axis=0).fillna(0)
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=yollar.GIRDI)
    ap.add_argument("--out", default=yollar.VERI)
    a = ap.parse_args()
    v = lambda f: os.path.join(a.out, f)  # noqa: E731

    y = pd.read_csv(v("tuik_yshi_nace2.csv"), dtype={"kod": str})
    bolum = y[y.kod.str.fullmatch(r"\d{2}") & (y.yil == 2024)].set_index("kod")
    y = y[y.kod.str.fullmatch(r"\d{2}\.\d{2}")]
    son = y[y.yil == 2024].set_index("kod")
    ilk = y[y.yil == 2015].set_index("kod")
    d = pd.DataFrame({
        "girisim": son.girisim, "calisan": son.calisan, "uretim_musd": son.uretim_degeri_musd,
        "kd_musd": son.faktor_maliyetiyle_kd_musd, "personel_gideri_musd": son.personel_gideri_musd,
        "calisan_2015": ilk.calisan, "uretim_musd_2015": ilk.uretim_degeri_musd})
    # Gizli sınıflar: bölüm toplamından açıklanan sınıflar düşülür, kalan iş kayıtlarındaki büyüklük gruplarından
    # tahmin edilen istihdamla (orta değerler; 250+ = 500), o da yoksa girişim sayısıyla dağıtılır [T]
    kt = pd.read_csv(v("tuik_girisim_ibbs2_nace2.csv"), dtype={"kod": str})
    kt = kt[kt.ibbs2.eq("TR")].set_index("kod")
    kayit_ist = (kt[BUYUK].fillna(0) * pd.Series({**ORTA, "g_250p": 500})).sum(axis=1)
    d["gizli_tahmin"] = False
    for sutun, kaynak in (("calisan", "calisan"), ("uretim_musd", "uretim_degeri_musd"),
                          ("kd_musd", "faktor_maliyetiyle_kd_musd"), ("personel_gideri_musd", "personel_gideri_musd")):
        for bl, grup in d.groupby(d.index.str[:2]):
            eksik = grup[grup[sutun].isna()]
            if eksik.empty or bl not in bolum.index or pd.isna(bolum.loc[bl, kaynak]):
                continue
            kalan = bolum.loc[bl, kaynak] - grup[sutun].sum()
            w = kayit_ist.reindex(eksik.index).fillna(0)
            if w.sum() <= 0:
                w = eksik.girisim.fillna(0)
            if kalan > 0 and w.sum() > 0:
                d.loc[eksik.index, sutun] = kalan * w / w.sum()
                d.loc[eksik.index, "gizli_tahmin"] = True
    d["kd_uretim_orani"] = d.kd_musd / d.uretim_musd
    d["kisi_basi_kd_bin_usd"] = 1e3 * d.kd_musd / d.calisan
    d["kisi_basi_ucret_bin_usd"] = 1e3 * d.personel_gideri_musd / d.calisan
    d["istihdam_degisimi_2015_2024_yuzde"] = 100 * (d.calisan / d.calisan_2015 - 1)
    od = pd.read_csv(v("teshis_odemeler_dengesi.csv"))
    gsyh = float(od.loc[od.yil == 2024, "gsyh_musd"].iloc[0])
    d["kd_gsyh_payi_yuzde"] = 100 * d.kd_musd / gsyh

    # ölçek ve bölge
    r = pd.read_csv(v("tuik_girisim_ibbs2_nace2.csv"), dtype={"kod": str})
    r = r[r.kod.str.fullmatch(r"\d{2}\.\d{2}")]
    tohum, buyuk_ort, n250, tr = kayit_tohum(r, d.girisim, d.calisan)
    for k in BUYUK:
        d[f"girisim_{k[2:]}"] = tr[k]
    d["buyuk_isletme_istihdam_payi"] = (n250 * buyuk_ort / d.calisan).clip(upper=1)
    sgk = f1e.sgk_tablo(f1e.sgk_indir(a.cache, "2025"))
    sgk = sgk[sgk.olcu.str.startswith("Sigortal") & sgk.bolum.between("10", "33")].copy()
    il_bolge = {il: k for k, (_ad, iller) in f1e.IBBS2.items() for il in iller}
    sgk["ibbs2"] = sgk.il.map(il_bolge)
    sgk = sgk[sgk.ibbs2.notna()].groupby(["bolum", "ibbs2"]).deger.sum().unstack(fill_value=0)
    parcalar = []
    for bl, grup in d[d.calisan.notna() & d.index.str[:2].isin(sgk.index)].groupby(lambda k: k[:2]):
        t = (tohum[tohum.kod.isin(grup.index)].pivot_table(index="kod", columns="ibbs2", values="tohum", aggfunc="sum")
             .reindex(index=grup.index, columns=sgk.columns).fillna(0))
        sutun = sgk.loc[bl] * grup.calisan.sum() / sgk.loc[bl].sum()
        # %1 bölüm dağılımı karışımı: kayıtta görünmeyen hücreler sıfıra kilitlenmesin [T]
        t = 0.99 * t.div(t.sum(axis=1).replace(0, np.nan), axis=0).fillna(0).mul(grup.calisan, axis=0) \
            + 0.01 * np.outer(grup.calisan, sutun / sutun.sum())
        m = ras(t, grup.calisan, sutun)
        parcalar.append(m.stack().rename("istihdam_tahmini").reset_index())
    b = pd.concat(parcalar)
    b["pay"] = b.istihdam_tahmini / b.groupby("kod").istihdam_tahmini.transform("sum")
    b = b[b.istihdam_tahmini >= 0.5].sort_values(["kod", "pay"], ascending=[True, False])
    b["bolge"] = b.ibbs2.map(IBBS2_AD)
    b["sira"] = b.groupby("kod").cumcount() + 1
    b[["kod", "sira", "ibbs2", "bolge", "istihdam_tahmini", "pay"]].round(4).to_csv(v("f3_bolge_sinif.csv"), index=False)
    d["ilk_bolge"] = b[b.sira == 1].set_index("kod").bolge
    d["ilk3_bolge_payi"] = b[b.sira <= 3].groupby("kod").pay.sum()
    d["bolge_hhi"] = (b.pay ** 2).groupby(b.kod).sum()

    # AB'ye göre verimlilik
    p = sbs(a.cache)
    d["ab_kisi_basi_kd_bin_eur"] = p.LABPRY_TEUR
    d["ab_yil"] = p.ab_yil
    d["ab_kisi_basi_kd_bin_usd"] = p.LABPRY_TEUR * p.ab_yil.map(USD_EUR)
    d["verimlilik_ab_orani"] = d.kisi_basi_kd_bin_usd / d.ab_kisi_basi_kd_bin_usd
    d["ab_istihdam"] = p.EMP_NR
    d.index.name = "kod"
    d.round(4).to_csv(v("f3_yapi_sinif.csv"))
    c = d[d.index.str.match(r"^(1[0-9]|2[0-9]|3[0-3])\.")]
    print(f"C sınıfı: {len(c)}; çalışan {c.calisan.sum():,.0f}; KD {c.kd_musd.sum():,.0f} mn $ "
          f"(GSYH'nin %{100 * c.kd_musd.sum() / gsyh:.1f}); AB verimlilik verisi olan {c.verimlilik_ab_orani.notna().sum()}")


if __name__ == "__main__":
    main()
