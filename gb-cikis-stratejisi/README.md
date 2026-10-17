# Türkiye–AB Gümrük Birliği'nden kontrollü çıkış: NACE sınıfı düzeyinde ulusal strateji

Bu klasör, "GB Çıkış Stratejisi" ana promptuna göre fazlar halinde üretilen çalışma
belgelerini, verileri ve kodu içerir. Her faz sonunda çalışma durur ve **DEVAM** komutu beklenir.
**HEPSİNİ OTOMATİK** komutu verilirse fazlar durmadan dosyalara yazılır.

## Durum

| Faz | İçerik | Durum | Dosya |
|---|---|---|---|
| 0 | Plan, varsayımlar, veri envanteri, NACE kapsamı, `[D?]` doğrulaması; Revizyon 1: kullanıcı yanıtları, T2028/T2029 takvimleri, çevrim içi veri erişimi | Tamamlandı (17.10.2026) | [`00_plan.md`](00_plan.md) |
| 1 | Teşhis | Sırada | `01_teshis.md` |
| 2–9 | Seçenekler ve hukuk → NACE kartları → derin analizler → araçlar ve tarife cetveli → makro → müzakere → uygulama → risk ve yönetici özeti | Planlandı | bkz. `00_plan.md` §2 |

Yeni bir sohbette devam etmek için: ana prompt + [`DURUM_OZETI.md`](DURUM_OZETI.md).

## Dosyalar

| Dosya | İçerik |
|---|---|
| `00_plan.md` | Faz 0 çıktısı: araçlar, çalışma planı, varsayım kaydı (V-01…), veri envanteri, NACE kapsamı, doğrulama kaydı, netleştirme soruları |
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
| `veri/s4_tarife_duvari_ozet.csv`, `veri/s4_tarife_duvari_bolum.csv` | Anlaşmasız çıkışta (S4) iki yönlü statik gümrük vergisi ve kısmi denge hacim etkisi (ön hesap) |
| `kod/f0_nace_kapsam.py` | NACE kapsam ve eşleştirme dosyalarını resmî kaynaklardan yeniden üreten betik |
| `kod/tuik.py` | TÜİK'e anonim erişim: Dağıtım Yönetim Sistemi (SDMX-CSV indirme, kod listeleri) ve Veri Portalı arama API'si |
| `kod/f0b_tuik_yshi.py`, `kod/f0c_tuik_bolge_tufe.py` | TÜİK tablolarını üreten betikler |
| `kod/f0d_s4_tarife_duvari.py` | S4 tarife duvarı hesabı |

## Yeniden üretme

```bash
pip install -r kod/requirements.txt
cd kod
python3 f0_nace_kapsam.py --cache ~/.cache/gb_cikis --out ../veri
python3 f0b_tuik_yshi.py --cache ~/.cache/gb_cikis --out ../veri
python3 f0c_tuik_bolge_tufe.py --cache ~/.cache/gb_cikis --out ../veri
```

Betikler Eurostat (SDMX ve Comext), EU Vocabularies (ShowVoc), GİB, TÜİK ve ECB'den herkese
açık dosyaları indirir; kimlik doğrulama gerekmez. İndirilen ham dosyalar depoya eklenmez.
