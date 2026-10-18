# Türkiye–AB Gümrük Birliği'nden kontrollü çıkış: NACE sınıfı düzeyinde ulusal strateji

Bu klasör, "GB Çıkış Stratejisi" ana promptuna göre fazlar halinde üretilen çalışma
belgelerini, verileri ve kodu içerir. Her faz sonunda çalışma durur ve **DEVAM** komutu beklenir.
**HEPSİNİ OTOMATİK** komutu verilirse fazlar durmadan dosyalara yazılır.

## Durum

| Faz | İçerik | Durum | Dosya |
|---|---|---|---|
| 0 | Plan, varsayımlar, veri envanteri, NACE kapsamı, `[D?]` doğrulaması; Revizyon 1: kullanıcı yanıtları, T2028/T2029 takvimleri, çevrim içi veri erişimi | Tamamlandı (17.10.2026) | [`00_plan.md`](00_plan.md) |
| 1 | Teşhis: GB'nin 30 yıllık bilançosu, asimetriler, makro tablo ve cari denge ayrıştırması, maruziyet haritası | Tamamlandı (17.10.2026) | [`01_teshis.md`](01_teshis.md) |
| 2A | Politika uzayı: kullanıcının önerisi (tarife + ÖTV takası), araç evreni, bağlı oranlar, aktif S4, dış rejim evreni | Tamamlandı (18.10.2026) | [`02a_politika_uzayi.md`](02a_politika_uzayi.md) |
| 2B | Seçenekler (S0–S5), bitiş durumu ve hukuki yol haritası | Sürüyor | `02b_secenekler_hukuk.md` |
| 3–9 | NACE kartları → derin analizler → araçlar ve tarife cetveli → makro → müzakere → uygulama → risk ve yönetici özeti | Planlandı | bkz. `00_plan.md` §2 |

Yeni bir sohbette devam etmek için: ana prompt + [`DURUM_OZETI.md`](DURUM_OZETI.md).

## Dosyalar

| Dosya | İçerik |
|---|---|
| `00_plan.md` | Faz 0 çıktısı: araçlar, çalışma planı, varsayım kaydı (V-01…), veri envanteri, NACE kapsamı, doğrulama kaydı, netleştirme soruları |
| `02a_politika_uzayi.md` | Faz 2A çıktısı: tarife + ÖTV/KDV takası (dört tasarım, on ürün grubu), DTÖ hukuku ve emsaller, araç evreni A–K, bağlı oranlar, tahsilat oranı, aktif S4 paket sınırı (İGV rejimi × P1 × takas), net istihdam, AB'nin maliyeti, zaman kritik eylemler |
| `01_teshis.md` | Faz 1 çıktısı: ticaret ve kompozisyon (1991–2025), sektör tarihçeleri, literatür, bilanço tablosu, STA ve diğer asimetriler, ödemeler dengesi, OVP tabanı ve T+5 boşluğu, NACE bölümü ve İBBS-2 maruziyeti, kısıt çatışmaları, veri boşlukları |
| `DURUM_OZETI.md` | Son fazın durum özeti (≤500 kelime) |
| `defter.md` | Kümülatif defter (enflasyon bütçesi, cari denge, mali maliyet, istihdam) |
| `veri/nace_kapsam.csv` | 230 C sınıfı + B, D, E, A ve hizmet kapsamı; GB statü etiketi, rejim payları, AB–TR ticareti (2025), Rev. 2.1 karşılığı |
| `veri/nace_kapsam_bolum_ozeti.csv` | NACE bölümü (2 hane) özeti |
| `veri/nace_r2_r21_kopru.csv` | Resmî Eurostat NACE Rev. 2 ↔ Rev. 2.1 köprüsü (C bölümü ve ek kapsam) |
| `veri/cn2025_nace_rejim.csv` | CN2025 (8 hane) → CPA 2.2 → CPA 2.1 → NACE Rev. 2 eşleştirmesi, satır bazında ticaret rejimi ve 2025 AB–TR ticareti |
| `veri/akct_1996_cn8.txt` | 1996 AKÇT–Türkiye Anlaşması Ek I ürün listesi (CN 1996, 280 satır) |
| `veri/tuik_yshi_nace2.csv` | TÜİK Yıllık Sanayi ve Hizmet İstatistikleri, NACE Rev. 2 bölüm ve sınıf düzeyi, 2015–2024 (girişim, çalışan, ciro, üretim değeri, faktör maliyetiyle katma değer; TL ve milyon $) |
| `veri/tuik_yshi_nace21_2025.csv` | Aynı istatistiklerin 2025 ön sonuçları, NACE Rev. 2.1 grup düzeyi |
| `veri/tuik_girisim_ibbs2_nace2.csv` | İBBS-2 bölgesi × NACE sınıfı × büyüklük grubu girişim sayıları (2024) |
| `veri/tuik_tufe_agirlik_2026.csv` | TÜFE ağırlıkları, 2026 (COICOP 2018, 2–5. düzeyler) |
| `veri/tuik_sue_sinif_aylik.csv` | Sanayi üretim endeksi, sınıf düzeyi, aylık (2023–) |
| `veri/tarife_tr_2026_gtip12.csv`, `veri/tarife_ab_cn2026_cn8.csv` | Türkiye 2026 uygulanan tarifesi (MFN, İGV, EMY; GTİP12) ve AB CN 2026 konvansiyonel vergileri (CN8) |
| `veri/s4_tarife_duvari_ozet.csv`, `veri/s4_tarife_duvari_bolum.csv`, `veri/s4_tarife_duvari_sinif.csv` | Anlaşmasız çıkışta (S4) iki yönlü statik gümrük vergisi ve kısmi denge hacim etkisi (ön hesap) |
| `veri/teshis_ab_ticaret_1991_2025.csv` | AB27–Türkiye ticareti: Türkiye beyanı (Comtrade, $) ve AB ayna verisi (Comext, €); AB payları, ikili denge |
| `veri/teshis_ab_ticaret_fasil.csv`, `veri/teshis_ab_ticaret_bolum.csv` | HS fasıl ve bölüm kompozisyonu (1995, 2025; Comext 1999–2025) |
| `veri/teshis_sektor_tarihceleri.csv` | Seçilmiş sektörlerin AB ticareti, 1999–2025 |
| `veri/teshis_sta_asimetrisi.csv` | AB'nin STA'sı olup Türkiye'nin olmadığı 33 pazar: Türk ihracatı, ödenen MFN, AB'nin tercih avantajı |
| `veri/teshis_odemeler_dengesi.csv`, `veri/teshis_cari_denge_12ay.csv` | Ödemeler dengesi bileşenleri, GSYH, reel kur, UYP (2002–2026); 12 aylık birikimli cari denge |
| `veri/teshis_hizmet_ticareti_ab27.csv` | AB27 ile hizmet ticareti, hizmet türüne göre (2016–2025) |
| `veri/teshis_bolum_maruziyet.csv`, `veri/teshis_bolgesel_maruziyet.csv` | NACE bölümü ve İBBS-2 düzeyinde AB maruziyeti ve S4 risk istihdamı |
| `kod/f0_nace_kapsam.py` | NACE kapsam ve eşleştirme dosyalarını resmî kaynaklardan yeniden üreten betik |
| `kod/tuik.py` | TÜİK'e anonim erişim: Dağıtım Yönetim Sistemi (SDMX-CSV indirme, kod listeleri) ve Veri Portalı arama API'si |
| `kod/f0b_tuik_yshi.py`, `kod/f0c_tuik_bolge_tufe.py` | TÜİK tablolarını üreten betikler |
| `kod/f0d_s4_tarife_duvari.py`, `kod/f0e_tarifeler.py` | S4 tarife duvarı; 2026 tarifelerinin indirilmesi (`kod/tarife_tr.py`, `kod/tarife_ab.py`, `kod/nazik_http.py`) |
| `kod/evds3.py` | TCMB EVDS3'e anahtarsız erişim |
| `kod/f1a_ab_ticaret.py` … `kod/f1e_bolgesel.py` | Faz 1 tabloları (ticaret, ödemeler dengesi, STA asimetrisi, bölüm ve bölge maruziyeti) |
| `kod/comtrade_tr_hs6.py`, `kod/baci_ozet.py` | Comtrade HS6 ve CEPII BACI yardımcı betikleri |
| `kod/f2a_io_fiyat.py` | Leontief fiyat modeli (TÜİK 2023 girdi-çıktı): tarife şokunun TÜFE'ye birinci tur etkisi → `veri/politika_io_ede.csv`, `veri/politika_io_s4_tufe.csv` |
| `kod/prodtr.py`, `kod/f2b_tarife_politikasi.py` | PRODTR (CPA 6 hane) ve tarife yapısı, BEC kullanımı, yurt içi kabiliyet, "girdide sıfır" → `veri/politika_tarife_*.csv`, `veri/prodtr_cpa6_2025.csv` |
| `kod/f2c0_takas_parametre.py`, `kod/f2c_vergi_takasi.py` | Vergi takası modeli: on ürün grubu, dört tasarım (pasif, T-A, T-0, T-B), Armington CES → `veri/politika_takas_parametre.csv`, `veri/politika_takas_sonuc.csv`, `veri/politika_takas_ozet.csv` |
| `kod/f2d_s4_net_istihdam.py` | S4 net istihdam, NACE sınıfı; iki ithalat rejimi (yalnızca MFN, c2) → `veri/politika_s4_net_istihdam_*.csv` |
| `kod/f2e_s4_aktif.py` | Aktif S4 paketleri: İGV rejimi (a, b, c, c2, d) × P1 × takas kapsamı, ayrıca S3 menşe maliyeti senaryoları; yasal ve tahsil edilebilir mali bilanço → `veri/politika_s4_aktif.csv`, `veri/politika_s4_aktif_urun.csv` |
| `veri/vergi_oranlari_2026.csv`, `veri/vergi_gelirleri_2024_2026.csv` | Ürün grubu ÖTV/KDV oranları ve yerli pay (kaynaklı); ÖTV, KDV ve gümrük vergisi tahsilatı (GİB, 2024–2026) |

## Yeniden üretme

```bash
pip install -r kod/requirements.txt
cd kod
python3 f0_nace_kapsam.py --cache ~/.cache/gb_cikis --out ../veri
python3 f0b_tuik_yshi.py --cache ~/.cache/gb_cikis --out ../veri
python3 f0c_tuik_bolge_tufe.py --cache ~/.cache/gb_cikis --out ../veri
python3 f0e_tarifeler.py --cache ~/.cache/gb_cikis --out ../veri
python3 f0d_s4_tarife_duvari.py --out ../veri
# Faz 1
python3 f1a_ab_ticaret.py --cache ~/.cache/gb_cikis --out ../veri
python3 f1b_odemeler_dengesi.py --cache ~/.cache/gb_cikis --out ../veri
python3 -I comtrade_tr_hs6.py ~/.cache/gb_cikis/comtrade 2025          # Türkiye HS6 dış ticareti
curl -L -C - -o ~/.cache/gb_cikis/BACI_HS17_V202601.zip https://www.cepii.fr/DATA_DOWNLOAD/baci/data/BACI_HS17_V202601.zip
python3 -I baci_ozet.py ~/.cache/gb_cikis/BACI_HS17_V202601.zip ~/.cache/gb_cikis/baci
python3 f1c_sta_asimetrisi.py --baci ~/.cache/gb_cikis/baci/all_countries/BACI_HS17_Y2024_V202601.parquet \
        --ulke-kodlari ~/.cache/gb_cikis/baci/country_codes_V202601.csv --cache ~/.cache/gb_cikis --out ../veri
python3 f1d_maruziyet.py --comtrade-hs6 ~/.cache/gb_cikis/comtrade/comtrade_tur_hs6_world_2025.csv.gz --out ../veri
python3 f1e_bolgesel.py --cache ~/.cache/gb_cikis --out ../veri
# Faz 2A (BACI_TR: Türkiye ikili HS6 akışları, 2020–2024; baci_ozet.py çıktısı)
python3 f2a_io_fiyat.py --cache ~/.cache/gb_cikis --out ../veri
python3 f2b_tarife_politikasi.py --baci-tr $BACI_TR --baci-dunya $BACI_DUNYA --bec $BEC --cache ~/.cache/gb_cikis --out ../veri
python3 f2c0_takas_parametre.py --baci-tr $BACI_TR --cache ~/.cache/gb_cikis --out ../veri
python3 f2c_vergi_takasi.py --out ../veri
python3 f2d_s4_net_istihdam.py --baci-tr $BACI_TR --out ../veri
python3 f2e_s4_aktif.py --cache ~/.cache/gb_cikis --out ../veri
```

Betikler Eurostat (SDMX ve Comext), EU Vocabularies (ShowVoc), GİB, TÜİK, TCMB EVDS3, UN Comtrade,
WITS, CEPII, SGK, Ticaret Bakanlığı, AB Yayın Ofisi ve ECB'den herkese açık dosyaları indirir;
kimlik doğrulama gerekmez. İndirilen ham dosyalar depoya eklenmez.
