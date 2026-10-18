# girdi/ — ham girdiler

Bu klasör, Faz 0–2C hesaplarının okuduğu bütün ham verileri içerir. Betikler (`kod/`) girdilerini varsayılan olarak buradan okur (`kod/yollar.py`). Bir dosya burada yoksa betik onu resmî kaynağından indirip buraya yazar.

`GB_CEVRIMDISI=1` ile indirme yasaklanır. Bu kipte eksik bir girdi varsa betik ağa çıkmaz, hata verir. Paketin kendi kendine yettiğini bu kip gösterir:

```bash
kod/hepsini_uret.sh --cevrimdisi --cikti /tmp/gb_veri    # bütün hesaplar, sonra veri/ ile karşılaştırma
```

Her dosyanın boyutu, SHA-256 özeti, kaynak kurumu, adresi ve onu okuyan betik [`MANIFEST.csv`](MANIFEST.csv) dosyasında. Erişim tarihi 17–18 Ekim 2026.

## Düzen

| Klasör / dosya | Kaynak | Okuyan betik | Not |
|---|---|---|---|
| `nace_*.tsv`, `nace21_nace2.xlsx`, `cpa22_*.xlsx/.tsv.gz`, `gib_sinif4.xls` | Eurostat, AB Yayın Ofisi (ShowVoc), GİB | `f0_nace_kapsam.py` | Sınıflama ve karşılık tabloları |
| `comext_eu_tr_2025_f{1,2}.csv.gz`, `comext_eu_tr_2025_f1_{miktar,elektrik_mwh}.csv.gz` | Eurostat Comext DS-045409 | `f0_nace_kapsam.py`, `f2i_skdm.py`, `f3d_ab_tarife.py` | CN8 × akış, 2025; AB ithalatında değer, 100 kg ve elektrikte MWh |
| `skdm/` | Avrupa Komisyonu (DG TAXUD) | `f2i_skdm.py` | SKDM varsayılan değerleri (Uygulama Tüzüğü 2026/1740) ve kıyas değerleri (2025/2620); Komisyonun bilgi dosyaları |
| `tuik_DF_*.csv(.gz)` | TÜİK Dağıtım Yönetim Sistemi | `f0b`, `f0c`, `f1b` | SDMX-CSV, tam veri akışları |
| `ecb/` | Avrupa Merkez Bankası | `f0b_tuik_yshi.py` | Yıllık ortalama kurlar; anlık görüntü |
| `tarife_tr/`, `cn2026_fmx4.zip` | Ticaret Bakanlığı; AB Yayın Ofisi | `f0e_tarifeler.py` | 2026 tarifeleri |
| `f1/ct_*.json`, `f1/cx_*.csv` | BM Comtrade; Eurostat Comext | `f1a_ab_ticaret.py` | 1991–2025 |
| `f1/wits/*.xml.gz` | Dünya Bankası WITS (TRAINS) | `f1c_sta_asimetrisi.py` | 33 pazarın MFN tarifeleri; WITS'in yanıt verdiği en son yıl |
| `evds3/` | TCMB EVDS3 | `f1b_odemeler_dengesi.py`, `f2k_makro_tampon.py` | API yanıtları; anlık görüntü (18.10.2026) |
| `sgk_yillik_2025.zip` | SGK | `f1e_bolgesel.py`, `f3b_yapi.py` | İl × NACE sigortalı |
| `io2023/` | TÜİK | `f2a`, `f2b`, `f2c0`, `f2e`, `f3e`, `f3f` | Girdi-çıktı tabloları 2023 |
| `prodtr/` | TÜİK | `f2b`, `f2c0` (`prodtr.py`) | PRODTR bülten tabloları |
| `bec/` | Dünya Bankası WITS | `f2b_tarife_politikasi.py` | HS 2017 → BEC 5 |
| `baci/` | CEPII BACI HS17 V202601 | `f1c`, `f2a`, `f2b`, `f2c0`, `f2d`, `f2f`, `f3a`, `f3c`, `f3d`, `f3g` | Özetler (aşağıda) |
| `cepii/ProTEE_0_1.csv` | CEPII ProTEE 0.1 (Fontagné, Guimbard ve Orefice 2022; Etalab 2.0) | `f3e_senaryo.py` | HS6 ticaret esneklikleri (5.050 ürün) |
| `eurostat/sbs_ovw_act_eu27_2022_2023.json` | Eurostat SBS (`sbs_ovw_act`) | `f3b_yapi.py` | AB27 sınıf düzeyi kişi başı KD, istihdam, KD, girişim; JSON-stat |
| `comtrade/` | BM Comtrade | `f1d_maruziyet.py` | Türkiye HS6 dış ticareti, 2025 (`comtrade_tr_hs6.py`) |
| `f2_cekim/` | CEPII Gravity V202211; DESTA v2.3; BM AMA | `f2f_cekim_modeli.py` | Çekim modeli paneli ve GSYH |

## Özetler: büyük dosyalar yerine ne var?

Üç kaynak pakete sığmayacak kadar büyük. Bunların yerine, betiklerin okuduğu satır ve sütunlar konuldu. Özetleri üreten kod pakette.

- **CEPII BACI HS17 V202601.** Yıl başına ≈95 MB, beş yıl.
  - `baci_hs17_tur_bilateral_hs6_2020_2024.csv.gz`: Türkiye'nin ikili HS6 akışları.
  - `baci_hs17_world_exports_exporter_hs6_2024.csv.gz`: ihracatçı × HS6 dünya ihracatı.
  - Bu iki özeti `kod/baci_ozet.py` üretir.
  - `baci_hs17_2024_f1c_ozet.parquet`: f1c'nin okuduğu satırlar. 2,2 milyon satır; tam dosyada 11,2 milyon.
  - `baci_hs17_ikili_toplam_{2020,2024}.parquet`: f2f'nin okuduğu ikili toplamlar.
  - Son iki özeti `kod/girdi_hazirla.py baci-ozet` üretir.
  - `baci_hs17_ab27_ithalat_ihracatci_hs6_2020_2024.parquet`: AB27'nin ihracatçı × HS6 ithalatı (AB üyeleri toplanmış; AB içi akımlar dahil), değer ve miktar; `baci_hs17_dunya_ihracat_hs6_2020_2024.parquet`: dünya ihracatı, HS6. İkisini `kod/girdi_hazirla.py baci-ozet-f3` üretir (Faz 3).
  - Betikler tam dosyayı da okuyabilir: `--baci` ve `--baci-dizin` seçenekleri.
- **CEPII Gravity V202211.** Zip dosyası 197 MB. Yerine `f2_cekim/gravity_V202211_1980_v4.parquet` var: f2f'nin `gravity_oku()` işlevinin zip'ten çıkardığı 1980 sonrası satırlar ve kullanılan sütunlar. Zip indirilip bu dosya silinirse f2f onu yeniden üretir.
- **TÜİK iş kayıtları** (189 MB CSV) ve diğer büyük metin dosyaları gzip'li. Betikler `.gz` kopyayı kendiliğinden okur (`yollar.bul`).

## Anlık görüntüler ve revizyonlar

EVDS3, ECB ve TÜİK serileri kaynakta revize edilebilir. Buradaki dosyalar 17–18 Ekim 2026'da indirildi. `veri/` klasöründeki sonuçlar bu dosyalarla birebir yeniden üretiliyor.

Güncel verilerle yeniden hesaplamak için:
1. İlgili dosyayı silin; betik dosyayı yeniden indirir.
2. `python3 kod/girdi_hazirla.py sikistir` ve `python3 kod/girdi_hazirla.py manifest` komutlarını çalıştırın.

## Kullanım koşulları

Veriler, kaynak kurumların kullanım koşullarına tabidir. Atıf için MANIFEST'teki adresler ve belgelerin "Kaynaklar" bölümleri kullanılmalıdır. CEPII veri tabanları (BACI, Gravity) için CEPII'nin atıf şartları geçerlidir.
