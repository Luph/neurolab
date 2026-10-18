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
| 2B | Seçenekler (S0–S5, R7, ITA, aktif S4), çekim modeli, bitiş durumu ve hukuki yol haritası (AB, DTÖ, Türk iç hukuku), iki takvim | Tamamlandı (18.10.2026) | [`02b_secenekler_hukuk.md`](02b_secenekler_hukuk.md) |
| 2C | Karar öncesi hazırlık: dokuz çerçevede 51 sessiz, pişmanlıksız hamle; STA ağının genel dengesi, menşe riski, SKDM yükü, makro tampon; kırmızı liste ve devreye alma sırası | Tamamlandı (18.10.2026) | [`02c_hazirlik.md`](02c_hazirlik.md) |
| 3 | NACE sınıf analizi (16 parça). Parça 1: 10 Gıda, 11 İçecekler, 12 Tütün; 33 sınıfın düzyazı incelemesi ve veri sayfası; ana matris 230 sınıfın tamamı için | Parça 1 / 16 tamamlandı (18.10.2026) | [`nace_kartlar_10-12.md`](nace_kartlar_10-12.md), [`veri/nace_matris.csv`](veri/nace_matris.csv) |
| 4–9 | Derin analizler → araçlar ve tarife cetveli → makro → müzakere → uygulama → risk ve yönetici özeti | Planlandı | bkz. `00_plan.md` §2 |

Yeni bir sohbette devam etmek için: ana prompt + [`DURUM_OZETI.md`](DURUM_OZETI.md).

## Nihai çıktı: PDF

Belgeler LaTeX'te dizilir ve PDF olarak üretilir (LuaLaTeX; Markdown → pandoc + `latex/gb.lua` → `latex/govde/*.tex`).

| PDF | İçerik |
|---|---|
| [`pdf/GB_Cikis_Stratejisi_Faz0-3.pdf`](pdf/GB_Cikis_Stratejisi_Faz0-3.pdf) | **Birleşik cilt:** durum özeti, Faz 0, 1, 2A, 2B, 2C, Faz 3 kartları (şimdilik 10–12); Ek A defter; Ek B çalışma paketi. İçindekiler ve şekil listesi |
| `pdf/00_plan.pdf`, `pdf/01_teshis.pdf`, `pdf/02a_politika_uzayi.pdf`, `pdf/02b_secenekler_hukuk.pdf`, `pdf/02c_hazirlik.pdf`, `pdf/nace_kartlar_10-12.pdf` | Faz belgeleri tek tek |
| `pdf/DURUM_OZETI.pdf`, `pdf/defter.pdf`, `pdf/README.pdf` | Durum özeti, defter, paket açıklaması |

Kanıt etiketleri PDF'te renkli kutudur: V doğrulanmış veri, T tahmin (P10–P90), D? doğrulanacak, H hipotez/yargı.

## Paket yapısı

Bütün kod, ham veri, ara ve nihai hesaplar pakettedir. Hesaplar ağ erişimi olmadan baştan üretilebilir (aşağıda).

| Klasör | İçerik |
|---|---|
| kök (`*.md`) | Faz belgeleri (Markdown kaynak) |
| [`pdf/`](pdf/) | Dizilmiş PDF'ler |
| [`latex/`](latex/) | Stil (`gbstil.sty`), pandoc filtresi (`gb.lua`), cilt ve belge sarmalayıcıları, üretilmiş LaTeX gövdeleri, derleme betiği (`derle.sh`) |
| [`kod/`](kod/) | Bütün betikler; `hepsini_uret.sh` hepsini sırayla çalıştırır, `dogrula.py` sonuçları karşılaştırır |
| [`kartlar/`](kartlar/) | Faz 3 belgelerinin kaynağı. `[bölüm]_metin/*.md`: elle yazılmış Türkçe metin; içindeki `{{…}}` yer tutucuları ve tablo işaretleri `kod/f3g_kartlar.py` ile veriden doldurulur. `[bölüm].yaml` ve `[bölüm]_siniflar.yaml`: yapısal alanlar (eylem ve tetik tabloları, çapa yatırımcılar, kritik girdiler, arketip/duruş/güven düzeltmeleri, defter kayıtları) |
| [`girdi/`](girdi/) | Ham girdiler (184 dosya, ≈132 MB): TÜİK, TCMB, Eurostat, Comtrade, WITS, CEPII, Ticaret Bakanlığı, SGK, DESTA, BM, Avrupa Komisyonu (SKDM). Kaynak, adres ve SHA-256: [`girdi/MANIFEST.csv`](girdi/MANIFEST.csv); açıklama: [`girdi/README.md`](girdi/README.md) |
| [`veri/`](veri/) | Hesap sonuçları (CSV) ve elle derlenmiş girdiler (`vergi_oranlari_2026.csv`, `vergi_gelirleri_2024_2026.csv`, `akct_1996_cn8.txt`, `skdm_ek1_kn.csv`, `skdm_asagi_kn.csv`, `skdm_parametre.csv`, `hazirlik_hamleler.csv`, `f3_sinif_varsayim.csv`, `f3_ss_boyutlar.csv`, `f3_coicop_nace.csv`, `ulke_adlari_tr.csv`; kaynakları ve gerekçeleri satır içinde) |
| [`sekiller/`](sekiller/) | Şekiller (PNG ve PDF), `kod/sekiller.py` ile `veri/`den |
| [`kaynaklar/`](kaynaklar/) | Hukuki ve kurumsal bulguların araştırma notları |

## Dosyalar

| Dosya | İçerik |
|---|---|
| `00_plan.md` | Faz 0 çıktısı: araçlar, çalışma planı, varsayım kaydı (V-01…), veri envanteri, NACE kapsamı, doğrulama kaydı, netleştirme soruları |
| `02a_politika_uzayi.md` | Faz 2A çıktısı: tarife + ÖTV/KDV takası (dört tasarım, on ürün grubu), DTÖ hukuku ve emsaller, araç evreni A–K, bağlı oranlar, tahsilat oranı, aktif S4 paket sınırı (İGV rejimi × P1 × takas), net istihdam, AB'nin maliyeti, zaman kritik eylemler |
| `02b_secenekler_hukuk.md` | Faz 2B çıktısı: seçeneklerin tanımı, çekim modeli sonuçları (PPML ve genel denge), karşılaştırma matrisi, kısıt testleri, önerilen bitiş durumu ve geçiş sırası (T2028, T2029), hukuki yol haritası, olasılıklar, riskler |
| `01_teshis.md` | Faz 1 çıktısı: ticaret ve kompozisyon (1991–2025), sektör tarihçeleri, literatür, bilanço tablosu, STA ve diğer asimetriler, ödemeler dengesi, OVP tabanı ve T+5 boşluğu, NACE bölümü ve İBBS-2 maruziyeti, kısıt çatışmaları, veri boşlukları |
| `02c_hazirlik.md` | Faz 2C çıktısı: karar öncesi sessiz hamleler (hukuk, DTÖ, iç hukuk, STA, menşe ve gümrük, kalite altyapısı, sanayi ve yatırım, SKDM, makro-finans, diplomasi, firma düzeyi), kırmızı liste, öncelik tablosu, iki takvim için sıra |
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
| `kod/f2f_cekim_modeli.py` | Yapısal çekim modeli (PPML; ihracatçı-yıl, ithalatçı-yıl, ikili sabit etkiler): GB ve AB STA etkileri, S2/S3/S4 senaryoları, 19 sağlamlık spesifikasyonu, genel denge (kesin şapka cebiri) → `veri/politika_cekim_katsayilar.csv`, `veri/politika_cekim_senaryolar.csv` |
| `kod/f2g_hazirlik_sta_ge.py` | AB'nin STA ortaklarıyla Türkiye'nin kendi STA'ları: S0 ve S4 üzerine genel denge (f2f modülü), WITS ve 2026 Türk tarifesi → `veri/hazirlik_sta_ge.csv`, `veri/hazirlik_sta_tarife.csv` |
| `kod/f2h_mense_pem.py` | Sanayi kollarında ve kilit ürünlerde PEM dışı girdi payı (TÜİK G-Ç 2023, BACI 2024, PRODTR) → `veri/hazirlik_pem_mense.csv`, `veri/hazirlik_pem_urun.csv` |
| `kod/f2i_skdm.py` | SKDM yükü: Komisyonun varsayılan değer ve kıyas dosyaları, Comext 2025; varsayılan ve doğrulanmış değer, yurt içi karbon fiyatı, aşağı akış önerisi → `veri/hazirlik_skdm*.csv` |
| `kod/f2k_makro_tampon.py` | TCMB rezervleri (IMF şablonu), ilan şoku senaryoları, gerekli tampon ve zamanlama kapısı → `veri/hazirlik_makro_*.csv` |
| `kod/f2j_hamle_tablosu.py` | 51 hamlenin puanı, öncelik sırası ve duyarlılık → `veri/hazirlik_hamleler_oncelik.csv` |
| `veri/skdm_*.csv`, `veri/hazirlik_hamleler.csv` | SKDM Ek I ve aşağı akış KN listeleri, SKDM parametreleri (kaynaklı); hamle tablosu (gerekçe, hukuki dayanak, süre, sorumlu, Pazartesi sabahı) |
| `veri/vergi_oranlari_2026.csv`, `veri/vergi_gelirleri_2024_2026.csv` | Ürün grubu ÖTV/KDV oranları ve yerli pay (kaynaklı); ÖTV, KDV ve gümrük vergisi tahsilatı (GİB, 2024–2026) |
| `kod/yollar.py` | Paket içi yollar (`girdi/`, `veri/`) ve çevrimdışı kip (`GB_CEVRIMDISI=1`) |
| `kod/hepsini_uret.sh`, `kod/dogrula.py` | Bütün hesapları sırayla yeniden üretir; sonuçları `veri/` ile karşılaştırır |
| `kod/girdi_hazirla.py` | BACI özetleri, büyük dosyaların sıkıştırılması, `girdi/MANIFEST.csv` |
| `nace_kartlar_10-12.md` | Faz 3 parça 1: yönetici özeti, çıkışın beş kanalı, strateji ve eylem paketi, 33 sınıfın incelemesi (15 alanlı kart: metin + Ek C veri sayfası + Bölüm 4 eylem ve tetik tabloları), kümülatif defter, ekler |
| `kod/f3a_ticaret.py` | Sınıf düzeyi ticaret: ihracat/ithalat, AB ve Çin payları, RCA (dünya, AB pazarı), AB pazar payı, birim değer, ilk 5 pazar/kaynak/rakip ve AB tercih durumu (BACI 2020, 2024; KKTC akımları AB dışı) → `veri/f3_ticaret_sinif.csv`, `veri/f3_ortaklar_sinif.csv` |
| `kod/f3b_yapi.py` | Üretim, KD, istihdam, ölçek, İBBS-2 bölge payları (iş kayıtları + SGK, RAS), AB'ye göre verimlilik (Eurostat SBS) → `veri/f3_yapi_sinif.csv`, `veri/f3_bolge_sinif.csv` |
| `kod/f3c_karmasiklik.py` | PCI ve ECI (yansımalar yöntemi, özvektör), ürün uzayı yoğunluğu, karmaşıklık kazancı, atlanabilir ürünler → `veri/f3_pci_*.csv`, `veri/f3_eci_ulke.csv` |
| `kod/f3d_ab_tarife.py` | AB MFN'si KN8 düzeyinde: spesifik vergilerin AVE'si, rejime göre S4 artışı (GB, İTÜ, 1/98), tepe satırlar, EUDR ve SKDM payları → `veri/f3_ab_tarife_kn8.csv`, `veri/f3_ab_tarife_sinif.csv` |
| `kod/f3e_senaryo.py` | S2/S3/S4 sınıf etkileri, P10–P50–P90 (Monte Carlo; toplamlar Faz 2B genel dengesine kalibre), bölüm ve parça toplamlarının dağılımı, S4'te 1/98 askısına koşullu sonuçlar, EDE, CKE → `veri/f3_senaryo_sinif.csv`, `veri/f3_senaryo_ozet.csv`, `veri/f3_senaryo_grup.csv`, `veri/f3_senaryo_aski.csv`, `veri/f3_makro_sinif.csv` |
| `kod/f3f_skor_matris.py` | KS, SS, AME, EDE, CKE puanları, arketip ve duruş (kural + `kartlar/` düzeltmeleri), ağırlık duyarlılığı → `veri/nace_matris.csv`, `veri/f3_ks_duyarlilik.csv` |
| `kod/f3g_kartlar.py` | Bölüm belgesi `nace_kartlar_[bölüm].md`: `kartlar/[bölüm]_metin/` şablonlarındaki yer tutucuları (matris ve f3 tabloları, grup yüzdelikleri, 1/98 askısı, dünya ihracat payları, ithalat kalemleri, KN8 tarifeleri) ve tablo işaretlerini doldurur; Türkçe ülke adları `veri/ulke_adlari_tr.csv` |
| `kod/sekiller.py` | On üç şekil (`sekiller/`) |
| `latex/derle.sh`, `latex/gb.lua`, `latex/gbstil.sty`, `latex/cilt.tex` | PDF üretimi |

## Yeniden üretme

```bash
pip install -r kod/requirements.txt
kod/hepsini_uret.sh                                     # bütün hesaplar → veri/ (girdi/'deki ham verilerden)
kod/hepsini_uret.sh --cevrimdisi --cikti /tmp/gb_veri   # ağsız sınama: başka klasöre üret, veri/ ile karşılaştır
latex/derle.sh                                          # şekiller, LaTeX gövdeleri ve bütün PDF'ler → pdf/
```

- **Süre.** Hesaplar ≈20–30 dakika sürer; çoğu çekim modelinde (19 PPML spesifikasyonu, 1.000 çekilişli genel denge) ve STA ağı genel dengesinde. PDF'ler ≈4 dakika.
- **Sınama sonucu (18.10.2026).** Çevrimdışı kipte Faz 0–3'ün bütün betikleri (31 adım) paketteki girdilerle çalıştı. `veri/` klasöründeki 77 dosya (Faz 3'ün grup yüzdelikleri ve 1/98 askısı çıktıları dahil) ve düzyazı belgesi `nace_kartlar_10-12.md` bayt bayt aynı üretildi (`kod/dogrula.py`). Faz 3 hesapları ≈1,5 dakika sürüyor.
- **Tek tek çalıştırma.** Betikler `kod/` içinden argümansız çalışır. Varsayılan girdi `girdi/`, çıktı `veri/`. Örnek: `python3 f2e_s4_aktif.py`. Sıra `hepsini_uret.sh` içinde.
- **PDF için gerekenler.** pandoc ≥ 3.1, TeX Live 2023 (LuaLaTeX, latexmk, KOMA-Script, polyglossia), TeX Gyre ve DejaVu yazı tipleri. Ubuntu'da: `apt-get install pandoc texlive-luatex texlive-latex-extra texlive-fonts-extra texlive-lang-european latexmk fonts-dejavu`.

**Ham verinin kaynakları.** Betikler Eurostat (SDMX ve Comext), EU Vocabularies (ShowVoc), GİB, TÜİK, TCMB EVDS3, UN Comtrade, WITS, CEPII, SGK, Ticaret Bakanlığı, AB Yayın Ofisi, ECB, DESTA ve BM'den herkese açık dosyaları kullanır; kimlik doğrulama gerekmez.
- Bu dosyalar `girdi/` klasöründedir.
- Bir dosya silinirse betik onu kaynağından yeniden indirir.
- Pakete sığmayan üç kaynak (BACI tam dosyaları, CEPII Gravity zip'i, TÜİK iş kayıtlarının ham CSV'si) için betiklerin okuduğu özetler konuldu. Ayrıntı: [`girdi/README.md`](girdi/README.md).
