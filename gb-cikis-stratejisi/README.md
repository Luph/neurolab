# Türkiye–AB Gümrük Birliği'nden kontrollü çıkış: NACE sınıfı düzeyinde ulusal strateji

Bu klasör, "GB Çıkış Stratejisi" ana promptuna göre fazlar halinde üretilen çalışma
belgelerini, verileri ve kodu içerir. Her faz sonunda çalışma durur ve **DEVAM** komutu beklenir.
**HEPSİNİ OTOMATİK** komutu verilirse fazlar durmadan dosyalara yazılır.

## Durum

| Faz | İçerik | Durum | Dosya |
|---|---|---|---|
| 0 | Plan, varsayımlar, veri envanteri, NACE kapsamı, `[D?]` doğrulaması | Tamamlandı (17.10.2026) | [`00_plan.md`](00_plan.md) |
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
| `kod/f0_nace_kapsam.py` | Yukarıdaki veri dosyalarını resmî kaynaklardan yeniden üreten betik |

## Yeniden üretme

```bash
pip install -r kod/requirements.txt
python3 kod/f0_nace_kapsam.py --cache ~/.cache/gb_cikis --out veri
```

Betik Eurostat (SDMX ve Comext), EU Vocabularies (ShowVoc) ve GİB'den herkese açık dosyaları
indirir; kimlik doğrulama gerekmez. İndirilen ham dosyalar depoya eklenmez.
