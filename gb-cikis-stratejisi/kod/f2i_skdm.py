"""Faz 2C — Sınırda Karbon Düzenleme Mekanizması (SKDM, AB CBAM): Türk ihracatının yükü ve yurt içinde tutulabilecek kısmı.

SKDM, GB'den bağımsızdır. Türkiye GB içinde de dışında da AB'ye çelik, alüminyum, çimento, gübre, elektrik ve hidrojen
satarken AB'deki ithalatçı gömülü emisyon için SKDM sertifikası teslim eder. Bu yüzden buradaki hamleler pişmanlıksızdır.

Yükümlülük (Tüzük 2023/956 md. 6(2)(c), 31; Uygulama Tüzüğü 2025/2620):
  sertifika/ton = gömülü emisyon − AB ücretsiz tahsis düzeltmesi − md. 9 mahsubu
  AB ücretsiz tahsis düzeltmesi = SKDM faktörü(yıl) × sektörler arası düzeltme × kıyas değeri
  Varsayılan değer yolunda: gömülü emisyon = Türkiye varsayılan değeri × (1 + işaret(yıl)); kıyas = B sütunu,
  Türkiye'ye atanan üretim rotası (çelikte (C) yüksek fırın, alüminyumda (K) birincil). Varsayılan değer kullanan
  ihracatçı md. 9 mahsubundan yararlanamaz (Komisyon varsayılan karbon fiyatı yayımlamadıkça).
  Gerçek (doğrulanmış) değer yolunda: rota bazında gerçek yoğunluk; kıyas, gerçek rotanın B sütunu değeri (çelikte
  (E) hurda-EAF ya da (C); alüminyumda (L) ikincil ya da (K)). Bu, Uygulama Tüzüğü'nün öncüllerle özyinelemeli
  hesabının yaklaşığıdır `[H]`. Yurt içi karbon fiyatı p_TR, ücretsiz tahsisi AB'ninkini aşmayan bir ETS'de
  fiilen ödenirse mahsup edilir: Türkiye'de kalan = min(p_TR, P) × yükümlülük; AB'ye ödenen = (P − p_TR)+ × yükümlülük.
Kapsam: Ek I KN listesi (veri/skdm_ek1_kn.csv; en uzun önek eşleşmesi, istisnalar dahil). Ticaret: Comext DS-045409,
  AB27'nin Türkiye'den ithalatı, 2025; değer (€), miktar (100 kg → ton), elektrikte MWh (tamamlayıcı birim).
Aşağı akış (COM(2025) 989; 1.1.2028'den, kabul edilmedi): kapsama girecek KN satırlarında ihracat değeri, kütle ve
  kaba yük: kütle × metal payı × yassı çelik yükümlülüğü/ton `[H]`.
2025 ticaret hacmi sabittir (davranış tepkisi yok); bu yüzden yük bir üst sınırdır.
Çıktı: veri/hazirlik_skdm_kapsam.csv (grup), veri/hazirlik_skdm.csv (grup × yıl × senaryo × fiyat × faktör),
       veri/hazirlik_skdm_asagi.csv (aşağı akış ürün grubu × senaryo × yıl).
"""

import argparse
import gzip
import os
import re

import numpy as np
import pandas as pd

import nazik_http
import yollar

COMEXT = ("https://ec.europa.eu/eurostat/api/comext/dissemination/sdmx/2.1/data/DS-045409/"
          "A.EU27_2020.TR.{urun}.1.{gosterge}?startPeriod=2025&endPeriod=2025")
SDMX_CSV = {"Accept": "application/vnd.sdmx.data+csv;version=1.0.0"}
YILLAR = list(range(2026, 2035))
VARSAYILAN_XLSX = os.path.join("skdm", "varsayilan_degerler_IR2026_1740.xlsx")  # Komisyon bilgi dosyası, 6.8.2026
KIYAS_XLSX = os.path.join("skdm", "kiyas_degerleri_IR2025_2620.xlsx")
SEKTOR = {"Cement": "Çimento", "Fertilisers": "Gübre", "Iron and steel": "Demir-çelik", "Iron & Steel": "Demir-çelik",
          "Aluminium": "Alüminyum", "Hydrogen": "Hidrojen", "Electricity": "Elektrik"}
# Çelik ürün grupları (KN4 önekleri); gerçek değer yolunda EAF payı ve verim bu gruplara göre. "diger": pelet,
# pik demir, ferroalyaj, DRI, paslanmaz (öncülü ithal sıcak bant) ve paslanmaz borular; gerçek = işaretsiz varsayılan.
CELIK_GRUP = {"diger": ("2601", "7201", "7202", "7203", "7205", "7218", "7219", "7220", "7221", "7222", "7223"),
              "uzun": ("7206", "7207", "7213", "7214", "7215", "7216", "7217", "7224", "7227", "7228", "7229",
                       "7301", "7302"),
              "yassi": ("7208", "7209", "7210", "7211", "7212", "7225", "7226"),
              "boru_esya": ("7303", "7304", "7305", "7306", "7307", "7308", "7309", "7310", "7311", "7318", "7326")}
PASLANMAZ_BORU = 5.0   # 7304/7306'da varsayılan değeri bunun üstündekiler paslanmaz: "diger"
ASAGI_GRUP = [("87", "Taşıtlar ve parçaları"), ("8418", "Beyaz eşya"), ("8450", "Beyaz eşya"), ("8451", "Beyaz eşya"),
              ("84", "Makine ve motorlar"), ("85", "Elektrik makineleri ve kablolar"), ("94", "Mobilya ve prefabrik"),
              ("90", "Tıbbi ve ölçü cihazları"), ("7", "Metal eşya"), ("8", "Metal eşya")]
SENARYOLAR = [("V", "Varsayılan değerler"), ("D", "Doğrulanmış gerçek değerler"),
              ("D+TR20", "Doğrulanmış + yurt içi 20 €/t"), ("D+TR50", "Doğrulanmış + yurt içi 50 €/t"),
              ("D+TRAB", "Doğrulanmış + yurt içi fiyat = AB")]
TR_FIYAT = {"V": "yok", "D": "yok", "D+TR20": "tr20", "D+TR50": "tr50", "D+TRAB": "trab"}


def comext(yol, urun, gosterge):
    """Comext CSV'si (gzip'li) girdi/'de yoksa indirilip yazılır; KN8 düzeyi."""
    if not os.path.exists(yol):
        url = COMEXT.format(urun=urun, gosterge=gosterge)
        yollar.indirme_izni(url)
        r = nazik_http.get(url, headers=SDMX_CSV, timeout=600)
        r.raise_for_status()
        with gzip.GzipFile(yol, "wb", mtime=0) as f:
            f.write(r.content)
    x = pd.read_csv(yol, dtype=str)
    x = x[x["product"].str.fullmatch(r"\d{8}")]
    return x.set_index("product").OBS_VALUE.astype(float)


def sayi(s):
    """'1,700' → 1.7; '–', 'N/A', 'see below' gibi hücreler → NaN."""
    try:
        return float(str(s).strip().replace(",", "."))
    except ValueError:
        return np.nan


def varsayilan_tablosu(yol):
    """Türkiye tablosu; '–' hücreleri 'Other countries and territories' tablosundan (IR 2026/1740 Ek I)."""
    sayfalar = pd.read_excel(yol, sheet_name=None, header=None, dtype=str)

    def oku(d):
        satirlar, sektor = [], None
        for r in d.itertuples(index=False):
            ilk = str(r[0]).strip()
            if ilk in SEKTOR:
                sektor = SEKTOR[ilk]
                continue
            kod = re.sub(r"\s", "", ilk)
            if kod.isdigit() and sektor:
                satirlar.append(dict(kod=kod, sektor=sektor, aciklama=r[1], dv=sayi(r[4]),
                                     rota=("" if pd.isna(r[5]) else str(r[5]).strip())))
        return pd.DataFrame(satirlar).drop_duplicates("kod").set_index("kod")

    tr = oku(sayfalar["Türkiye"])
    diger = oku(sayfalar[next(k for k in sayfalar if k.startswith("_Other"))])
    tr["yedek"] = tr.dv.isna()
    tr.loc[tr.yedek, "dv"] = diger.dv.reindex(tr.index[tr.yedek]).values
    tr.loc[tr.yedek & (tr.rota == ""), "rota"] = diger.rota.reindex(tr.index[tr.yedek & (tr.rota == "")]).fillna("").values
    return tr


def kiyas_tablosu(yol):
    """B sütunu kıyas değerleri (varsayılan değer yolu) ve rota göstergeleri; KN8 × rota."""
    d = pd.read_excel(yol, sheet_name="Benchmarks", header=None, dtype=str, skiprows=1)
    d.columns = ["kn", "aciklama", "bmA", "rA", "bmB", "rB"]
    d["kn"] = d.kn.where(d.kn.fillna("").str.replace(" ", "").str.isdigit()).ffill().str.replace(" ", "")
    d = d[d.bmB.notna()].copy()
    d["bm"] = d.bmB.map(sayi)
    d["rota"] = d.rB.fillna("").str.strip()
    return d[["kn", "rota", "bm"]].dropna(subset=["kn"])


def onek_esle(kodlar, tablo):
    """Her KN8 için tablo kodu: önce KN8'in altındaki TARIC kodları (ortalama), sonra en uzun önek."""
    t = sorted(tablo, key=len, reverse=True)
    sonuc = {}
    for k in kodlar:
        alt = [x for x in t if len(x) > 8 and x.startswith(k)]
        if alt:                      # TARIC alt kırılımı: "diğer" (…90) kodu, yoksa ortalama (ör. gri klinker)
            sonuc[k] = [x for x in alt if x.endswith("90")] or alt
            continue
        ust = next((x for x in t if k.startswith(x)), None)
        sonuc[k] = [ust] if ust else []
    return sonuc


def kapsam(kodlar, ek1):
    """Ek I: en uzun önek eşleşmesi; 'haric' ve 'kapsam_disi' satırları dışarıda bırakır."""
    e = ek1.assign(n=ek1.kn.str.len()).sort_values("n", ascending=False)
    sektor = {}
    for k in kodlar:
        r = next((r for r in e.itertuples() if k.startswith(r.kn)), None)
        if r is not None and r.kapsam == "dahil":
            sektor[k] = r.sektor
    return pd.Series(sektor, dtype=object)


def kiyas_degeri(kb, kn, rotalar):
    """KN8 ve rota(lar) için B sütunu kıyası; rota yoksa ya da eşleşmezse en düşük değer (temkinli)."""
    s = kb[kb.kn == kn]
    if s.empty:
        s = kb[kb.kn.str.startswith(kn[:6])]
    if s.empty:
        return np.nan
    istenen = [r for r in re.findall(r"\([A-Z0-9]+\)", rotalar or "")]
    eslesen = s[s.rota.isin(istenen)]
    return (eslesen if not eslesen.empty else s).bm.min()


def celik_grubu(kn):
    return next((g for g, onekler in CELIK_GRUP.items() if kn.startswith(onekler)), "diger")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=yollar.GIRDI)
    ap.add_argument("--out", default=yollar.VERI)
    a = ap.parse_args()
    v = lambda f: os.path.join(a.out, f)  # noqa: E731
    g = lambda f: os.path.join(a.cache, f)  # noqa: E731

    deger = comext(g("comext_eu_tr_2025_f1.csv.gz"), "", "VALUE_IN_EUROS")
    ton = comext(g("comext_eu_tr_2025_f1_miktar.csv.gz"), "", "QUANTITY_IN_100KG") / 10
    mwh = comext(g("comext_eu_tr_2025_f1_elektrik_mwh.csv.gz"), "27160000", "SUPPLEMENTARY_QUANTITY")
    ek1 = pd.read_csv(v("skdm_ek1_kn.csv"), dtype={"kn": str})
    asagi = pd.read_csv(v("skdm_asagi_kn.csv"), dtype={"kn": str})
    par = pd.read_csv(v("skdm_parametre.csv"), dtype={"anahtar": str})
    dv = varsayilan_tablosu(yollar.bul(g(VARSAYILAN_XLSX)) or g(VARSAYILAN_XLSX))
    kb = kiyas_tablosu(yollar.bul(g(KIYAS_XLSX)) or g(KIYAS_XLSX))

    assert not par.duplicated(["tur", "anahtar", "senaryo"]).any()
    parametre = {(r.tur, r.anahtar, r.senaryo): float(r.deger) for r in par.itertuples()}

    def p(tur, anahtar, senaryo="hepsi"):
        return parametre[(tur, anahtar, senaryo)]

    faktor = {(int(r.anahtar), r.senaryo): r.deger for r in par[par.tur == "skdm_faktoru"].itertuples()}
    cscf = p("sektorler_arasi_duzeltme", "hepsi", "merkez")
    isaret = lambda yil, sektor: (p("isaret", "2026", "gubre") if sektor == "Gübre"  # noqa: E731
                                  else p("isaret", str(min(yil, 2028)), "genel"))
    fiyat = lambda yil, fs: p("ets_fiyati", "2026") if yil == 2026 else p("ets_fiyati", "2027", fs)  # noqa: E731

    # ---- KN8 tablosu: kapsam, varsayılan değer, kıyaslar
    d = pd.DataFrame({"eur": deger, "ton": ton}).fillna(0.0)
    d["sektor"] = kapsam(d.index, ek1)
    d = d[d.sektor.notna() & (d.eur > 0)].copy()
    if "27160000" in d.index:
        d.loc["27160000", "ton"] = mwh.get("27160000", np.nan)      # elektrik: MWh
    esle = onek_esle(d.index, dv.index)
    d["dv"] = [dv.loc[esle[k], "dv"].mean() if esle[k] else np.nan for k in d.index]
    d["rota"] = [dv.loc[esle[k][0], "rota"] if esle[k] else "" for k in d.index]
    d["yedek"] = [bool(dv.loc[esle[k], "yedek"].any()) if esle[k] else False for k in d.index]
    d.loc[d.sektor == "Elektrik", ["dv", "rota"]] = [p("elektrik", "varsayilan"), ""]
    d["bm_v"] = [kiyas_degeri(kb, k, r) for k, r in zip(d.index, d.rota)]
    d["bm_e"] = [kiyas_degeri(kb, k, "(E)") for k in d.index]
    d["bm_c"] = [kiyas_degeri(kb, k, "(C)") for k in d.index]
    d["bm_k"] = [kiyas_degeri(kb, k, "(K)") for k in d.index]
    d["bm_l"] = [kiyas_degeri(kb, k, "(L)") for k in d.index]
    d.loc[d.sektor == "Elektrik", ["bm_v", "bm_e", "bm_c", "bm_k", "bm_l"]] = 0.0
    eksik = d[d.dv.isna() | d.bm_v.isna()]
    if len(eksik):
        print("Varsayılan değer ya da kıyası bulunamayan satırlar (yükten düşüldü):",
              eksik[["sektor", "eur"]].to_dict("index"))
    d = d[d.dv.notna() & d.bm_v.notna()].copy()
    d["grup"] = d.sektor
    celik = d.sektor == "Demir-çelik"
    d.loc[celik, "grup"] = ["Demir-çelik: " + ("diger" if k.startswith(("7304", "7306")) and dvi > PASLANMAZ_BORU
                                              else celik_grubu(k))
                            for k, dvi in zip(d.index[celik], d.dv[celik])]

    # ---- ton başına yükümlülük
    def gercek(r, ys, cf):
        """Gerçek değer yolunda (emisyon/ton, sertifika/ton)."""
        if r.grup.startswith("Demir-çelik") and not r.grup.endswith("diger"):
            grup = r.grup.split(": ")[1]
            s, verim = p("eaf_payi", grup, "merkez"), p("celik_verim", grup)
            e_eaf = verim * p("gercek_yogunluk", "celik_eaf", ys)
            e_yf = verim * p("gercek_yogunluk", "celik_yf", ys)
            bm_e = r.bm_e if not np.isnan(r.bm_e) else r.bm_v
            bm_c = r.bm_c if not np.isnan(r.bm_c) else r.bm_v
            return (s * e_eaf + (1 - s) * e_yf,
                    s * max(0.0, e_eaf - cf * bm_e) + (1 - s) * max(0.0, e_yf - cf * bm_c))
        if r.sektor == "Alüminyum":
            s = p("aluminyum", "ikincil_payi", ys)
            e_pri, e_sec = p("aluminyum", "birincil_dogrudan", ys), p("aluminyum", "ikincil_dogrudan")
            islem = 0.0 if r.Index.startswith("7601") else p("aluminyum", "isleme_dogrudan")
            bm_k = r.bm_k if not np.isnan(r.bm_k) else r.bm_v
            bm_l = r.bm_l if not np.isnan(r.bm_l) else r.bm_v
            return (s * (e_sec + islem) + (1 - s) * (e_pri + islem),
                    s * max(0.0, e_sec + islem - cf * bm_l) + (1 - s) * max(0.0, e_pri + islem - cf * bm_k))
        if r.sektor == "Çimento":
            if r.Index.startswith("252310"):
                e, klinker = p("gercek_yogunluk", "klinker", ys), 1.0
            elif r.Index.startswith("252329"):
                e, klinker = p("gercek_yogunluk", "cimento_gri", ys), p("cimento_klinker_orani", "hepsi", "merkez")
            else:
                e, klinker = r.dv * p("oran", "cimento_diger", ys), p("cimento_klinker_orani", "hepsi", "merkez")
            return e, max(0.0, e - cf * klinker * r.bm_v)
        if r.sektor in ("Gübre", "Hidrojen"):
            e = r.dv * p("oran", "gubre" if r.sektor == "Gübre" else "hidrojen",
                         ys if r.sektor == "Gübre" else "hepsi")
            return e, max(0.0, e - cf * r.bm_v)
        return r.dv, max(0.0, r.dv - cf * r.bm_v)        # elektrik ve özel çelik: gerçek = işaretsiz varsayılan

    satirlar = []
    for r in d.itertuples():
        for fk in ("yasa", "oneri"):
            for yil in YILLAR:
                cf = faktor[(yil, fk)] * cscf
                mk = 0.0 if r.sektor == "Elektrik" else isaret(yil, r.sektor)
                e_v = r.dv * (1 + mk)
                n_v = max(0.0, e_v - cf * r.bm_v)
                for ys in ("dusuk", "merkez", "yuksek"):
                    e_d, n_d = gercek(r, ys, cf)
                    for fs in ("dusuk", "merkez", "yuksek"):
                        P = fiyat(yil, fs)
                        for sk, _ in SENARYOLAR:
                            if sk == "V" and ys != "merkez":
                                continue
                            pt = p("tr_karbon_fiyati", TR_FIYAT[sk])
                            pt = P if pt < 0 else min(pt, P)
                            if r.sektor == "Elektrik":
                                pt = 0.0                     # elektrikte md. 9 mahsubu modellenmedi
                            e, n = (e_v, n_v) if sk == "V" else (e_d, n_d)
                            satirlar.append(dict(kn=r.Index, grup=r.grup, sektor=r.sektor, faktor=fk, yil=yil,
                                                 senaryo=sk, yogunluk=("—" if sk == "V" else ys), fiyat=fs,
                                                 ets_fiyati=P, tr_fiyati=pt, eur=r.eur, miktar=r.ton,
                                                 emisyon=e * r.ton, sertifika=n * r.ton,
                                                 ab_odeme=(P - pt) * n * r.ton, tr_kalan=pt * n * r.ton))
    s = pd.DataFrame(satirlar)
    anahtar = ["grup", "sektor", "faktor", "yil", "senaryo", "yogunluk", "fiyat"]
    t = s.groupby(anahtar, as_index=False).agg(
        ets_fiyati=("ets_fiyati", "first"), tr_fiyati=("tr_fiyati", "max"),
        ihracat_meur=("eur", lambda x: x.sum() / 1e6), emisyon_mt=("emisyon", lambda x: x.sum() / 1e6),
        sertifika_mt=("sertifika", lambda x: x.sum() / 1e6), ab_odeme_meur=("ab_odeme", lambda x: x.sum() / 1e6),
        tr_kalan_meur=("tr_kalan", lambda x: x.sum() / 1e6))
    t["toplam_maliyet_meur"] = t.ab_odeme_meur + t.tr_kalan_meur
    t["maliyet_ihracat_orani_yuzde"] = 100 * t.toplam_maliyet_meur / t.ihracat_meur
    t.round(4).to_csv(v("hazirlik_skdm.csv"), index=False)

    # ---- kapsam özeti (grup)
    o = s[(s.faktor == "yasa") & (s.fiyat == "merkez") & (s.yogunluk.isin(["—", "merkez"]))]
    k = d.groupby("grup").agg(sektor=("sektor", "first"), kn_satiri=("eur", "size"),
                              ihracat_meur=("eur", lambda x: x.sum() / 1e6), miktar_kt=("ton", lambda x: x.sum() / 1e3),
                              yedek_deger_payi=("yedek", "mean")).reset_index()
    for etiket, sk, yil in [("emisyon_varsayilan_2028_mt", "V", 2028), ("emisyon_gercek_mt", "D", 2028)]:
        k[etiket] = k.grup.map(o[(o.senaryo == sk) & (o.yil == yil)].groupby("grup").emisyon.sum() / 1e6)
    k["varsayilan_yogunluk"] = k.grup.map(d.assign(w=d.dv * d.ton).groupby("grup").w.sum() /
                                          d.groupby("grup").ton.sum())
    k["gercek_yogunluk"] = 1e3 * k.emisyon_gercek_mt / k.miktar_kt
    k.round(3).to_csv(v("hazirlik_skdm_kapsam.csv"), index=False)

    # ---- aşağı akış (COM(2025) 989)
    tum = pd.DataFrame({"eur": deger, "ton": ton}).fillna(0.0)
    liste = asagi.assign(n=asagi.kn.str.len()).sort_values("n", ascending=False)
    eslesme = {kn: next((r for r in liste.itertuples() if kn.startswith(r.kn)), None) for kn in tum.index}
    tum["ex"] = [e.ex if e is not None else np.nan for e in eslesme.values()]
    x = tum[tum.ex.notna()].copy()
    x["grup"] = [next(ad for onek, ad in ASAGI_GRUP if kn.startswith(onek)) for kn in x.index]
    yassi = t[(t.grup == "Demir-çelik: yassi") & (t.faktor == "yasa") & (t.fiyat == "merkez") &
              (t.yogunluk.isin(["—", "merkez"]))].set_index(["senaryo", "yil"])
    metal = p("asagi", "metal_payi", "merkez")
    yassi_ton = d[d.grup == "Demir-çelik: yassi"].ton.sum()
    a_sat = []
    for grup, gx in x.groupby("grup"):
        for sk in ("V", "D"):
            for yil in (2028, 2029, 2030, 2034):
                ton_basi = yassi.loc[(sk, yil)].toplam_maliyet_meur * 1e6 / yassi_ton   # €/t yassı çelik
                a_sat.append(dict(grup=grup, senaryo=sk, yil=yil, ihracat_meur=gx.eur.sum() / 1e6,
                                  ex_payi=(gx.eur * gx.ex).sum() / gx.eur.sum(), kutle_kt=gx.ton.sum() / 1e3,
                                  metal_kt=metal * gx.ton.sum() / 1e3, celik_maliyeti_eur_t=ton_basi,
                                  yuk_meur=metal * gx.ton.sum() * ton_basi / 1e6))
    a_df = pd.DataFrame(a_sat)
    a_df["yuk_ihracat_orani_yuzde"] = 100 * a_df.yuk_meur / a_df.ihracat_meur
    a_df.round(3).to_csv(v("hazirlik_skdm_asagi.csv"), index=False)

    # ---- özet
    pd.set_option("display.width", 200)
    print(k.round(2).to_string(index=False))
    m = t[(t.faktor == "yasa") & (t.fiyat == "merkez") & (t.yogunluk.isin(["—", "merkez"]))]
    print(m.pivot_table(index="yil", columns="senaryo", values="ab_odeme_meur", aggfunc="sum").round(0).to_string())
    print(m.pivot_table(index="yil", columns="senaryo", values="tr_kalan_meur", aggfunc="sum").round(0).to_string())
    print(a_df[a_df.yil == 2028].round(1).to_string(index=False))


if __name__ == "__main__":
    main()
