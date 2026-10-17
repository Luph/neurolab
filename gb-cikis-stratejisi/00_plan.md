# Faz 0 — Çalışma Planı, Varsayım Kaydı, Veri Envanteri ve NACE Kapsamı

**Türkiye–AB Gümrük Birliği'nden Kontrollü Çıkış: NACE Sınıfı Düzeyinde Ulusal Strateji**

| | |
|---|---|
| Tarih | 17 Ekim 2026 (çalışma ortamının tarihi) |
| Faz | 0 / 9: tamamlandı; Revizyon 1 ile kullanıcı yanıtları işlendi; **DEVAM** bekleniyor |
| Bu fazın çıktıları | `00_plan.md` (bu belge); `veri/nace_kapsam.csv`, `veri/nace_kapsam_bolum_ozeti.csv`, `veri/nace_r2_r21_kopru.csv`, `veri/cn2025_nace_rejim.csv`, `veri/akct_1996_cn8.txt`; `kod/f0_nace_kapsam.py`; `defter.md`; `DURUM_OZETI.md` |
| Kanıt etiketleri | `[V]` doğrulanmış veri (kaynak, dönem) · `[T]` tahmin (yöntem, P10–P50–P90) · `[D?]` doğrulanması gereken · `[H]` hipotez veya uzman yargısı. Güven: **Y**üksek / **O**rta / **D**üşük |
| Para birimi | Aksi belirtilmedikçe cari ABD doları; AB kaynaklı veriler avro olarak verilir. 2025 ortalama kuru: 1 € = 1,1300 $ `[V]` (ECB, EXR.A.USD.EUR) |

---

## Revizyon 1 (17.10.2026): kullanıcı yanıtları

| Soru | Kullanıcının yanıtı | Çalışmaya etkisi |
|---|---|---|
| S-1 Görev çerçevesi | Her şey AB'nin hasmane tutumundan kaynaklanıyor | **Çıkış yönü veri kabul edildi.** Görev en az zararlı ve en yüksek faydalı çıkışın tasarımıdır. S1 (modernize GB) yalnızca maliyet karşılaştırma ölçütü olarak fiyatlanır. Çıkışın net negatif kaldığı tasarım, sınıf ve dönemler yine açıkça yazılır (`<gorev>`) |
| S-2 T tarihi | 1.1.2028 de hesaplanacak | İki takvim birlikte yürütülür: **T2028** (hızlandırılmış, T = 1.1.2028) ve **T2029** (nominal, T = 1.1.2029). Kritik yol ve fizibilite §2A'da; bütün fazlarda iki takvim ayrı sütun olarak raporlanır |
| S-3 Veri | Bütün verilere API'lerden veya kazıma ile çevrim içi erişilebilir | Kullanıcı yüklemesi beklenmez. TÜİK için anonim erişim yolu kuruldu, TÜİK verileri indirildi; diğer kaynaklar yeniden test edildi (§4) |
| S-4 Üyelik perspektifi | Üyelik perspektifi yok | Diplomatik çerçeve "üyelikten bağımsız, çıkar temelli ekonomik ortaklık" (V-27). Ankara Anlaşması, 1/80 ve standstill hakları üyelik için değil, vatandaş hakları ve ekonomik çıkar için korunur (temel ilke 2) |
| S-5 Enflasyon bütçesi kapsamı | Yanıt yok | Varsayılan geçerli: bütçe GB paketini ve kur/risk primi kanalını kapsar |
| V-11 AB ile ilişki | AB'nin tutumu hasmane | Temel durum "gerginlik"; iş birliği yukarı yönlü duyarlılık. S5 bileşenlerinin olasılığı yükseltildi (V-11, V-28) |

---

## Faz 0'da öne çıkan 10 bulgu

Bu bulgular strateji tasarımını daha ilk fazda etkiliyor; ayrıntıları ve kaynakları §5 ve §6'da.

1. **Çıkışın asıl etki alanı sanayi malları.** Türkiye'nin AB'ye 2025 ihracatı (AB'nin Türkiye'den ithalatı) €103,4 mlr ($116,9 mlr) `[V]` (Eurostat Comext DS-045409). Bu değerin %89,3'ü GB kapsamındaki sanayi ürünleri, %6,0'ı tarım ve balıkçılık (1/98 sayılı Karar), %3,3'ü AKÇT kapsamındaki çelik ve kömür, %1,3'ü işlenmiş tarım ürünleri (İTÜ) `[V]` (CN8 düzeyinde eşleştirme; Güven: GB/tarım ayrımı Y, çelik ve İTÜ sınırları O). Menşe kuralları sorunu yaklaşık €92 mlr'lık ihracatta ortaya çıkar.
2. **Kamuya açık resmî pozisyon bugüne kadar modernizasyondu; çıkış kararı bir pozisyon değişikliği olacak.** Faz 0 taramasında GB'den çıkışı öneren resmî bir Türk açıklaması bulunamadı: Bakan Bolat (Ekim 2026) modernizasyonu "seçenek değil zorunluluk" olarak tanımlıyor; Fidan–Kos ortak açıklaması (6.2.2026) modernizasyonun "yolunu açma" taahhüdü içeriyor `[V]`. AB Konseyi 2018'den beri müzakere yetkisi vermedi; Ortaklık Konseyi 2019'dan beri toplanmıyor `[V]`. Revizyon 1 ile çıkış yönü veri kabul edildi. Bu değişikliğin piyasalara, yatırımcılara ve AB'ye nasıl duyurulacağı kur ve risk primi bakımından başlı başına bir risk kalemidir (Faz 8 iletişim planı).
3. **Hukuki çıkış kapısı dar ve oybirliğine bağlı.** Ankara Anlaşması'nda ve 1/95 sayılı Kararda süre, fesih veya çekilme hükmü yok. Ortaklık Konseyi oybirliğiyle karar alır (Ankara md. 23) `[V]`. Türkiye Viyana Antlaşmalar Hukuku Sözleşmesi'ne (VCLT) taraf değil `[V]` (BM Antlaşmalar Kayıtları, 17.10.2026); tek taraflı çıkış ancak teamül hukukuna (md. 56 mantığı, en az 12 ay bildirim) dayanabilir ve tartışmalıdır. AB tarafında veto riskini azaltan tek yol ABİHA md. 207'ye dayanan, portföy yatırımı ve yatırımcı-devlet uyuşmazlık çözümü (ISDS) içermeyen "yalnızca AB" (EU-only) ticaret anlaşmasıdır: nitelikli çoğunlukla (NÇ) kabul edilir. Ortaklık yolu (md. 217) oybirliği ve karma onay gerektirir `[V]`.
4. **Mevcut sayısal literatür GB'den STA'ya geçişi Türkiye için olumsuz buluyor.** BKP (2016): GB yerine DCFTA → Türkiye refahı −€144 mn, AB'ye ihracat −€4,34 mlr; modernize GB → refah +€12,5 mlr, GSYH +%1,44 `[V]`. Dünya Bankası (2014): GB yerine STA olsaydı AB'ye ihracat %3,0–7,2 daha düşük olurdu `[V]`. ifo (2016): GB'nin sona ermesi GSYH'yi %0,81 düşürür `[V]`. Bu sonuçlar 2016 öncesi veriye dayanıyor; özerklik temettüsünü, ABD ve Çin kaynaklı yeni ortamı ve AB'nin 2024–2026 STA dalgasını içermiyor. Dürüstlük ilkesi gereği başlangıç hipotezi şudur `[H]`: **S2, S0'ı ancak elverişli menşe kuralları, ACAA, SKDM düzenlemesi ve büyük bir özerklik temettüsü birlikte sağlanırsa geçebilir.** Faz 1–2 bu hipotezi sınayacak.
5. **Asimetri baskısı 2026'da sıçradı.** AB–Mercosur geçici ticaret anlaşması 1.5.2026'dan beri uygulanıyor; AB–Meksika 22.5.2026'da imzalandı; AB–Hindistan (27.1.2026) ve AB–Avustralya (24.3.2026) müzakereleri sonuçlandı; AB–Endonezya imza aşamasında `[V]`. Türkiye'nin bu ortaklarla STA'sı yok. Bu durum, GB içinde kalmanın maliyetini artıran ve özerklik argümanını güçlendiren en somut gelişme.
6. **ABD pazarında Türkiye AB'den daha kötü muamele görüyor.** Bölüm 301 kapsamında Türkiye'ye 24.7.2026'dan itibaren %12,5 uygulanıyor; AB için MFN dahil toplam %10 tavanı var. Bölüm 232'de (çelik, alüminyum, bakır %50; otomobil ve parça %25) Türkiye'ye indirim yok `[V]`. GB içindeyken Türkiye OGT'ye bağlı olduğundan ABD'ye tek taraflı tarife tavizi veremez. Çıkış pazarlık alanı açar; ABD ile STA'nın gerçekçiliği ise orta-düşük `[H]`.
7. **AB'nin yeni sanayi politikası GB ortaklığını ödüllendiriyor.** Sanayi Hızlandırıcı Yasası (Industrial Accelerator Act, IAA) önerisi COM(2026) 100 (4.3.2026), STA ve gümrük birliği ortaklarını kamu desteği ve açık artırma ölçütlerinde AB menşeine eşdeğer sayıyor `[V]`. Türkiye savunma programı SAFE'ye ise Yunanistan engeli nedeniyle katılamadı `[V]`. Yeni anlaşma bu eşdeğerliği açıkça içermezse GB'den çıkış "Made in Europe" statüsünü kaybettirebilir. Bu bir **kırmızı çizgi müzakere maddesidir**.
8. **Çelik zaten GB dışında ve 1.7.2026'dan beri kalıcı AB kota rejimine tabi.** Tüzük (AB) 2026/1384: yıllık tarife kontenjanı 18,35 Mt (−%47), kota dışı %50 vergi, eritme ve döküm (melt and pour) kuralı 1.10.2027'den itibaren tahsiste kullanılacak. Türkiye STA ortağı muamelesi görüyor ve ülke kotaları aldı `[V]`. SKDM (CBAM) kesin dönemi 1.1.2026'da başladı; 2026 sertifika fiyatı tCO₂ başına €75–82 `[V]`. TR-ETS pilot dönemi %100 ücretsiz tahsisle işliyor ve 2026 yalnızca raporlama yılı; dolayısıyla 2026–27'de SKDM'de mahsup edilebilecek bir Türk karbon fiyatı yok `[V]`. 24.10, 24.42, 23.51 ve 20.15 sınıfları GB kararından bağımsız olarak ağır maruziyette.
9. **DTÖ politika alanı geniş, ama bağlı satırlarda dar.** Sanayi ürünlerinde bağlama oranı %43,0: giyim %3,7, tekstil %23,4, mineral-metal %24,3, taşıt %57,8, elektriksiz makine %68,6 `[V]` (WTO World Tariff Profiles 2026). DS629 panel raporu (28.7.2026), Türkiye'nin elektrikli araçlara uyguladığı ek vergileri bağlı oranı aştığı için GATT II:1'e aykırı buldu. DS583 tahkim kararı (2022) da yerlileştirme şartlarını III:4'e aykırı bulmuştu `[V]`. Tarife merdiveni bu nedenle satır satır bağlı oran kontrolüyle kurulacak. Bağsız satırlarda geniş alan var; itibar ve STA riski ise fiyatlanacak.
10. **Makro çerçeve sıkı.** OVP 2027–2029: 2026 cari açığı −$47,5 mlr (GSYH'nin −%2,6'sı), 2029'da −%1,6 `[V]`. TÜFE Eylül 2026'da yıllık %29,73; TCMB ara hedefleri 2026 için %24, 2027 için %15, 2028 için %9; politika faizi %37 `[V]`. Cari dengeyi T+5'te (T2028'de 2033, T2029'da 2034) sıfıra çekmek, OVP'nin 2029 patikasına göre yaklaşık 1,6 puan GSYH ek iyileşme gerektirir. GB paketi bunun ancak bir bölümünü sağlayabilir; büyüklüğü Faz 6'da hesaplanacak `[H]`.

---

## 1. Ortam ve araç tespiti; çalışma modu

| Araç | Durum | Bu çalışmadaki kullanımı |
|---|---|---|
| Web arama ve sayfa getirme | Var | `[D?]` doğrulaması; bilgi kesim tarihinden (Haziran 2026) sonraki gelişmeler |
| Kod çalıştırma | Var: Python 3.13, pandas 3.0, numpy 2.5, openpyxl, xlrd. PyPI erişimi var, statsmodels, pyfixest, scipy ve pulp kurulabilir | Eşleştirme, kısmi denge, çekim (PPML), girdi-çıktı, optimizasyon |
| Dosya oluşturma ve git | Var: `luph/neurolab` deposu, `claude/new-session-sz4axk` dalı | Her faz `gb-cikis-stratejisi/` altına yazılır, commit edilir ve push edilir |
| Paralel araştırma ajanları | Var | Faz 0'da 4 doğrulama ajanı: hukuk; DTÖ, tarife ve STA; SKDM, çelik ve yaptırımlar; literatür, makro ve veri |

**Veri kaynaklarına erişim testi (17.10.2026):**

| Kaynak | Durum | Not |
|---|---|---|
| Eurostat SDMX API ve Comext | ✓ | AB–TR 2025 CN8 ticareti indirildi (aylık veri Ağustos 2026'ya kadar mevcut) |
| EU Vocabularies (ShowVoc) | ✓ | NACE 2.1↔2, CPA 2.2↔2.1 ve CPA 2.2↔CN 2025 tabloları indirildi |
| GİB | ✓ | NACE Rev. 2.1 Türkçe sınıf adları (2026) |
| Eurostat'ta Türkiye: sanayi üretimi (STS), HICP ağırlıkları, ÜFE | ✓ | Ağustos–Eylül 2026'ya kadar; erken uyarı ve fiyat izleme için yedek |
| Eurostat'ta Türkiye: yapısal işletme istatistikleri (SBS) | ✗ (veri yok) | NACE 4 haneli ölçek verisi için TÜİK şart |
| OECD SDMX (ICIO/TiVA), Dünya Bankası API, WITS, CEPII (BACI), ECB | ✓ | |
| UN Comtrade | ✓ (genel önizleme API'si, kısıtlı) | Tam erişim için ücretsiz API anahtarı gerekir |
| TCMB EVDS | ✓ | API anahtarı gerekir |
| SBB, HMB, Sanayi ve Teknoloji Bakanlığı, SGK, İSO | ✓ | |
| WTO web sitesi | ✓; ttd.wto.org ✗ (403) | Satır düzeyinde bağlı oranlar için WITS ve WTO TDF yolu denenecek |
| TÜİK veri portalı, Resmî Gazete, mevzuat.gov.tr | ✗ (zaman aşımı) | TÜİK verileri için kullanıcı yüklemesi veya yedek kaynaklar (§4) |
| ticaret.gov.tr | ✗ (502) | Ajanlar içeriği arama motoru önbelleği ve basın üzerinden doğruladı |

**Seçilen mod: araçlı mod** (web + kod + dosya). Hesaplamalar kodla yapılır, kod ve ara çıktılar depoda saklanır, web kaynakları künyesiyle verilir. **HEPSİNİ OTOMATİK** komutu verilirse fazlar durmadan dosyalara yazılır; her faz sonunda yine DURUM ÖZETİ üretilir.

---

## 2. Ayrıntılı çalışma planı

| Faz | İçerik | Tahmini yanıt | Ana çıktılar | Kritik veri ve araçlar |
|---|---|---|---|---|
| 0 | Plan, araçlar, varsayımlar, veri envanteri, NACE kapsamı, `[D?]` doğrulaması | 1 | bu belge; `veri/nace_kapsam.csv`; köprü ve eşleştirme tabloları | Eurostat, ShowVoc, GİB |
| 1 | Teşhis: GB'nin 30 yıllık fayda-maliyet bilançosu, asimetriler, makro tablo, cari denge ayrıştırması | 2 | `01_teshis.md`, `veri/teshis_*.csv` | Comext 1995–2025, UN Comtrade/BACI, TCMB ödemeler dengesi, OVP 2027–29 |
| 2 | S0–S5 karşılaştırması, önerilen bitiş durumu, hukuki yol haritası (AB, DTÖ, iç hukuk) | 2 | `02_secenekler_hukuk.md` | Faz 0 hukuk doğrulaması, literatür |
| 3 | NACE analizi: bölüm bölüm ana matris satırları, 230 sınıf kartı, B/D/E ve hizmetler; her yanıtın sonunda kümülatif defter | 22–26 | `nace_matris.csv`, `nace_kartlar_[bölüm].md`, `defter.md` | Comext CN8, CN 2026 tarifesi, bağlı oranlar, BACI, OECD ICIO |
| 4 | Segmentasyon (KS×AME, EDE×CKE); 30–40 derin analiz (her yanıtta 2–4 sınıf) | 1 + 12 | `04_segmentasyon.md`, `04_derin_[kod].md` | Firma ve çapa yatırımcı verileri, ürün ağacı (BOM) menşe simülasyonları |
| 5 | Yatay araçlar; GB sonrası tarife cetveli taslağı | 3 | `05_araclar.md`, `tarife_cetveli_taslak.csv` | CN 2026 / GTİP, bağlı oranlar, ITA listesi |
| 6 | Makro entegrasyon: cari denge köprüsü, enflasyon yolu, bütçe optimizasyonu, tutarlılık testleri | 3 | `06_makro.md`, `kod/f6_*.py` | Girdi-çıktı (TÜİK 2023 veya OECD ICIO 2022), TCMB |
| 7 | Müzakere stratejisi: AB, üçüncü ülkeler, DTÖ; metin önerileri | 2 | `07_muzakere.md` | — |
| 8 | Uygulama planı, iletişim, izleme ve değerlendirme | 2 | `08_uygulama.md` | — |
| 9 | Risk kaydı, kırmızı takım, etki boyutları tablosu, yönetici özeti ve karar notu | 2 | `09_risk.md`, `00_yonetici_ozeti.md` | — |
| | **Toplam** | **≈ 50–56** | | |

**Faz 3'ün parçaları** (sınıf sayısı ve tahmini yanıt): 10–12 (33 sınıf; 3) → 13–15 (21; 2) → 16–18 (18; 2) → 19–21 (20; 2) → 22–23 (30; 3) → 24 (16; 2) → 25 (17; 2) → 26 (10; 1) → 27 (10; 1) → 28 (21; 2) → 29 (4; 1) → 30 (8; 1) → 31–33 (22; 2) → B (15; 1) → D/E (3; 1) → hizmetler (8; 1).

**Analitik omurga.** Yöntemler `<analitik_cerceve>` tanımlarıyla birebir uygulanır; farklı yöntem seçilen yerde neden yazılır.

| Katman | Uygulama | Fark ve gerekçe |
|---|---|---|
| Eşleştirme | CN2025 → CPA 2.2 → CPA 2.1 → NACE Rev. 2 (Faz 0'da tamamlandı). GTİP'in ilk 8 hanesi CN ile aynı `[H→V Faz 1]`; BEC Rev. 5 ve COICOP 2018 bağlantıları Faz 3'te eklenecek | Birden çok NACE sınıfına düşen CN satırları eşit paylaştırılır (ağırlık sütunu dosyada) |
| Kısmi denge | 230 sınıfın tamamı; CN8 düzeyinde `τ_AB`, `c_RoO`, `p_uyum` ve sınıfa toplama | — |
| Yapısal çekim | PPML, ihracatçı-yıl, ithalatçı-yıl ve ikili sabit etkilerle (pyfixest); BACI 2000–2024 | Geriye dönük sınama: 1996 GB girişi, Brexit |
| Genel denge | GTAP veritabanı lisanslı olduğundan **GE-PPML** karşı-olgusu (Anderson, Larch ve Yotov 2018) ve literatürdeki CGE sonuçları (BKP 2016, ifo 2016) ile çapraz kontrol | GTAP-benzeri tam CGE ancak lisans sağlanırsa |
| Girdi-çıktı | Leontief fiyat ve miktar modeli; tercihen TÜİK 2023 simetrik tablosu (64 sektör), yedek OECD ICIO 2025 baskısı (Türkiye, 2022) | 4 haneye geçiş TÜFE madde ağırlıkları ve ithalat paylarıyla köprülenir |
| Makro blok | Ödemeler dengesi, tasarruf-yatırım, reel kur, TÜFE, mali denge için yarı yapısal tutarlılık çerçevesi | — |
| Belirsizlik | σ, ρ, φ, `p_uyum`, çapa yatırımcı davranışı ve reel kur için Monte Carlo ile P10/P50/P90; tornado duyarlılığı | — |

---

## 2A. İki takvim: T2028 ve T2029

Bugün (17.10.2026) itibarıyla T2028'e 14,5 ay, T2029'a 26,5 ay var. T2028'de prompttaki T−24 başlangıcı (1.1.2026) geride kaldı; hazırlık penceresi T−14,5'ten başlıyor. "Önce anlaşma, sonra çıkış" ilkesi gereği T, yeni çerçevenin yürürlüğe girdiği gündür.

### Kritik yol

Süreler emsallere dayanır: AB–İngiltere Ticaret ve İşbirliği Anlaşması'nda (TCA) Komisyon tavsiyesi 3.2.2020, Konsey yetkisi 25.2.2020, anlaşma 24.12.2020, geçici uygulama 1.1.2021 oldu `[V]`. AB–Japonya EPA'sı 2013–2019, AB–Yeni Zelanda 2018–2024, AB–Ukrayna DCFTA'sı 2008–2016 (geçici uygulama) sürdü `[V]`. Türkiye'ye ilişkin 2016 modernizasyon tavsiyesi ise 10 yıldır Konsey'de bekliyor `[V]`.

| No | Adım | Asgari süre (emsal) | T2028'de son tarih | T2029'da son tarih |
|---|---|---|---|---|
| 1 | İç karar, müzakere heyeti, AB'ye resmî başvuru, piyasa iletişimi | 1–2 ay | Aralık 2026 | Mart 2027 |
| 2 | AB Konseyi müzakere yetkisi (md. 207, NÇ) | 3 hafta (TCA) ile süresiz (2016 tavsiyesi) arası | Mart 2027 | Haziran 2027 |
| 3 | Müzakere | İnce STA: ≈10 ay (TCA, sabit son tarih baskısıyla). DCFTA: 3–6 yıl | Nisan–Ekim 2027 (≈6 ay) | Temmuz 2027–Temmuz 2028 (≈12 ay) |
| 4 | Hukuki gözden geçirme ve çeviri | 2–4 ay; geçici uygulamayla sıkıştırılabilir | Kasım 2027 | Eylül 2028 |
| 5 | AB imza kararı ve geçici uygulama; Avrupa Parlamentosu onayı sonra gelebilir | 1–2 ay | Aralık 2027 | Kasım 2028 |
| 6 | TBMM onayı (Anayasa md. 90) veya geçici uygulama kararı | 1–2 ay `[D?]` | Aralık 2027 | Aralık 2028 |
| 7 | Ortaklık Konseyi kararı: 1/95'in yerine geçiş, AB tutumu md. 218(9) ile (oybirliği) | 1–3 ay; yazılı usul mümkün | Aralık 2027 | Aralık 2028 |
| 8 | Uygulama hazırlığı: menşe ispatı (onaylı ihracatçı, REX benzeri sistem), BİLGE, tedarikçi beyanları, KOBİ eğitimi | 9–12 ay (İngiltere 2019–2020) | **Kasım 2026'da başlamalı**, menşe kuralları bilinmeden | Ocak 2028'e kadar başlamalı |
| 9 | Yeni Türk tarife cetveli ve İGV'nin yeniden tasarımı; T−6'da ilan | 6 ay önceden ilan | 1.7.2027 | 1.7.2028 |
| 10 | CE ve onaylanmış kuruluş sürekliliği (ACAA veya geçiş düzenlemesi) | ACAA müzakeresi yıllar sürer; geçiş için karşılıklı tanıma kararı gerekir | AB'nin geçiş kararına bağlı | AB'nin geçiş kararına bağlı |
| 11 | Mevcut 24 STA'daki GB atıfları ve PEM kümülasyon ilişkileri | 6–18 ay | Paralel yürütülmeli | Paralel yürütülmeli |

### Değerlendirme

- **T2028'de tam DCFTA (S2) mümkün değil.** Müzakere için en fazla 6 ay kalıyor. Ulaşılabilecek en iyi sonuç geçici uygulamalı ince bir STA (S3: sanayi mallarında sıfır tarife ve revize PEM kuralları). Hizmetler, kamu alımları, ACAA, SKDM, karayolu taşımacılığı ve vize "yerleşik müzakere gündemi" olarak T'den sonraya kalır. Uygulama hazırlığı menşe kuralları kesinleşmeden başlamak zorunda. İngiltere'nin ilk aylardaki %59–70'lik tercih kullanım oranı `[V]` 2028'in ilk yarısında Türkiye için de beklenmelidir `[H]`.
- **T2029'da 12–15 aylık müzakere penceresi var.** Bu süre ince STA'ya ek olarak öncelikli sektörlerde ACAA ve SKDM düzenlemesi gibi DCFTA bölümlerine yeter (S3+). Tam S2 büyük olasılıkla 2030–2031'i gerektirir `[H]`.
- **AB'nin hasmane tutumu (V-11) iki takvimi farklı etkiler.** Yetki ve müzakere AB'nin iş birliğine bağlı. AB oyalarsa T2028'de "önce anlaşma" ilkesi karşılanamaz ve sonuç ya erteleme ya da anlaşmasız çıkıştır (S4/S5).
- **T2028 üç takvimle çakışıyor:**
  - **SKDM:** Mansap ürünlere genişleme önerisi 1.1.2028'de başlıyor; 2027 ithalatı için ilk sertifika teslimi Eylül 2028'de.
  - **Çelik:** Eritme-döküm kuralı 1.10.2027'den itibaren kota tahsisinde kullanılıyor.
  - **Seçim:** Olağan genel seçimler 2028'de; beş yıllık dönem Mayıs 2023'te başladı `[V]`.

  Seçimden aylar önce bir ticaret şoku, siyasi ekonomi riskini (etki boyutu 21) en üst düzeye çıkarır.
- **Enflasyon ve kur:** TCMB'nin ara hedefleri 2027 için %15, 2028 için %9 `[V]`. T2028'de olası bir şok tam dezenflasyonun son yılına denk gelir. Anlaşmasız çıkışta mevcut İGV rejimi AB menşeli mallara da uygulanmaya başlar, çünkü İGV STA'sı olmayan ülkelerin mallarına uygulanıyor `[V]`. Tarife ve İGV T'den önce yeniden tasarlanmazsa bu kendi başına büyük bir TÜFE şoku demektir. Bu nedenle 9. adım (tarife cetveli ve İGV) iki takvimde de kritik yoldadır.

### T'de gerçekleşebilecek sonuçların öznel olasılıkları

Bu olasılıklar V-11 (hasmane AB) varsayımı altında ve gitme/gitmeme kapıları işletilmeden önceki durumu gösterir `[H]`, Güven: D. Faz 2 ve 7'de güncellenecek.

| T'deki sonuç | T2028 | T2029 |
|---|---|---|
| S2: tam DCFTA yürürlükte | < %5 | %5–15 |
| S3/S3+: ince STA, geçici uygulamada | %10–25 | %30–45 |
| Geçiş düzenlemesi: hukuki çıkış, yeni anlaşma yürürlüğe girene kadar GB kurallarının sürmesi | %15–30 | %15–25 |
| S4/S5: anlaşmasız çıkış | %45–70 | %25–45 |

### Kapılar

Kapıların takvimi iki seçenekte farklıdır:

| Kapı | T2028 | T2029 | Asgari koşul (sağlanmazsa T ertelenir) |
|---|---|---|---|
| K1 | 1.4.2027 (T−9) | 1.1.2028 (T−12) | AB müzakere yetkisi verilmiş; geçiş/statüko ilkesi üzerinde yazılı mutabakat |
| K2 | 1.7.2027 (T−6) | 1.7.2028 (T−6) | Sanayi mallarında sıfır tarife ve menşe kuralları metni üzerinde uzlaşı; yeni tarife cetveli ilan edilmiş |
| K3 | 1.11.2027 (T−2) | 1.10.2028 (T−3) | Geçici uygulama kararı veya geçiş düzenlemesi imzalanmış; gümrük ve menşe sistemleri test edilmiş |

**Sonuç:** T2028 ancak AB geçiş düzenlemesini veya ince STA'yı kabul ederse "boşluksuz geçiş" ilkesiyle bağdaşır. Aksi halde T2028 fiilen bir **baskı tarihi** işlevi görür: Türkiye anlaşmasız çıkışa inandırıcı biçimde hazırsa pazarlık kaldıracı olur, hazır değilse maliyetlidir. Anlaşmasız çıkışın maliyeti Faz 3 ve 6'da her iki takvim için ayrı ayrı hesaplanacak.

---

## 3. Varsayım kaydı (son hal)

| ID | Parametre | Değer | Kaynak / gerekçe |
|---|---|---|---|
| V-01 | Bugünün tarihi | 17 Ekim 2026. Bilgi kesimi Haziran 2026; sonrası web aramasıyla kontrol edildi | Ortam tarihi |
| V-02 | Baz yıl ve veri dönemi | 2025 tam yıl. Son 12 ay: cari denge Eyl 2025–Ağu 2026; dış ticaret ve fiyatlar mevcut son ay | Prompt varsayılanı |
| V-03 | Zaman çizelgesi | **İki takvim birlikte hesaplanır.** T2028: hazırlık 17.10.2026 → **T = 1 Ocak 2028** → T+60 = 1 Ocak 2033. T2029: hazırlık T−24 = 1 Ocak 2027 → **T = 1 Ocak 2029** → T+60 = 1 Ocak 2034. Vizyon 2035. T koşulludur: yeni çerçevenin yürürlük tarihidir. Kapılar §2A'da (T2028: T−9, T−6, T−2; T2029: T−12, T−6, T−3). Duyarlılık: T = 1 Ocak 2030 | Kullanıcı yanıtı (Revizyon 1) + `<temel_ilkeler>` 1 |
| V-04 | Tercih edilen bitiş durumu | Faz 2'de S0–S5 karşılaştırmasıyla önerilecek; S2 ana tasarım hipotezi, S1 zorunlu karşı-olgu | Prompt varsayılanı |
| V-05 | Enflasyon bütçesi (TÜFE) | Birinci tur kümülatif ≤ 50 baz puan (bp), herhangi bir yılda ≤ 30 bp; ikinci tur dahil kümülatif ≤ 100 bp. Hedef: net dezenflasyonist paket. Ölçüt: TÜFE genel (2025=100, COICOP 2018). Kur ve risk primi kanalı ayrı blok olarak gösterilir ve bütçeye sayılır | Prompt varsayılanı; kapsam için soru 5 |
| V-06 | Cari denge hedefi | T+5'te (T2028'de 2033, T2029'da 2034) cari denge/GSYH ≥ %0; enerji ve altın hariç çekirdek dengede kalıcı fazla. GB paketinin katkısı ile tamamlayıcı politikaların katkısı ayrı gösterilir. Baz: 2025 −$30,3 mlr (−%1,9) `[V]` (OVP 2027–29); TCMB'nin Şubat 2026 ilk açıklaması −$25,2 mlr; fark Faz 1'de EVDS'den çözülecek `[D?]`. 2026 tahmini −$47,5 mlr (−%2,6) | OVP 2027–2029 (6.9.2026) |
| V-07 | İstihdam kısıtı | T+3'te toplam imalat istihdamında net kayıp sıfır. Herhangi bir NACE sınıfında %5'i aşan kayıp otomatik destek tetikler. Ölçüm: SGK 4/a sigortalı (NACE 4 hane, aylık) ve TÜİK. Baz: imalatta ücretli çalışan 4,46 mn (2025 sonu) `[D?]` | Prompt varsayılanı |
| V-08 | Kabiliyet kısıtı | `<temel_ilkeler>` 3 (a)–(d). (a) "kalıcı %30 düşüş" = 3 yıllık hareketli ortalamanın 2023–25 ortalamasına göre %30'dan fazla düşmesi. (b) Kritik eşik varsayılanı = etkin girişim sayısının 2025 düzeyinin %70'i veya en az 3 bağımsız üretici (hangisi yüksekse); sınıf kartında özelleştirilir | `[H]`; Faz 3'te sınıf bazında |
| V-09 | Mali kısıt | Net mali maliyet (ek gümrük gelirleri düşülmüş) ≤ GSYH'nin %0,5'i/yıl. 2026'da ≈ $9,1 mlr, 2029'da ≈ $11,1 mlr (OVP GSYH patikası) | Prompt varsayılanı; OVP 2027–29 |
| V-10 | Hukuki kısıt | DTÖ uyumu zorunlu. İstisna önerilirse dava ve misilleme riski fiyatlanır (DS583 ve DS629 emsalleri) | Prompt varsayılanı |
| V-11 | AB ile siyasi ilişki | **Hasmane.** Temel durum "gerginlik": AB'nin ticaret savunması, SKDM varsayılan değerleri, IAA karşılıklılık hükmü ve savunma programlarından dışlama gibi araçları kullanma olasılığı yüksek. İş birliği yukarı yönlü duyarlılık | Kullanıcı yanıtı (Revizyon 1) |
| V-12 | Risk iştahı | Orta: geri dönüşü olmayan kayıplara karşı düşük, geri alınabilir denemelere karşı orta | Prompt varsayılanı |
| V-13 | Çıktı dili | Türkçe; teknik terimlerin İngilizcesi ilk geçtiği yerde parantez içinde | Prompt varsayılanı |
| V-14 | Analiz birimi | NACE Rev. 2, C bölümünde 230 sınıf. TÜİK ulusal sınıflamada 2026'da NACE Rev. 2.1'e geçtiği için (GİB 2026 listeleri 651 sınıf) 2025 sonrası veriler resmî Eurostat köprüsüyle Rev. 2'ye çevrilir | `[V]` Eurostat NACE_R2 kod listesi; GİB 2026 |
| V-15 | GB statü etiketi kuralı | CN2025→CPA→NACE zinciri; rejim payı Türkiye'nin AB'ye ihracatıyla (Comext 2025) ağırlıklı. Tek rejimin payı ≥ %97,5 ise o etiket, değilse KARMA. İkili ticaret €25 mn altındaysa CN satır sayısıyla ağırlıklandırılır (eşik %90). CPA'da "hizmet" olarak tanımlanan fason sınıflar GB (dolaylı) | Faz 0 yöntemi (§5.1) |
| V-16 | Kur | Faz 1'de OVP 2027–29 USD/TL patikası ve TCMB Piyasa Katılımcıları Anketi; EUR/USD 2025 ortalaması 1,1300 `[V]` (ECB) | — |
| V-17 | Ticaret esneklikleri σ | Sektörel değerler literatürden (Fontagné, Guimbard ve Orefice 2022 ürün düzeyi esneklikleri; Caliendo ve Parro 2015). Kaynak bulunamazsa varsayılan σ = 5 (P10 3, P90 8) | `[H]`; Faz 3'te sınıf bazında |
| V-18 | İkinci tur çarpanı φ | Başlangıç aralığı 0,5–1,5 (P50 1,0). Faz 6'da geçmişe endeksleme, beklenti ve ücret kanallarından tahmin | `[H]` |
| V-19 | Geçişkenlik ρ | Piyasa yapısına göre 0,3–1,0. TCMB kur geçişkenliği çalışmaları ve 2011 sonrası İGV deneyimiyle kalibre edilecek | `[H]` |
| V-20 | Menşe uyum maliyeti c_RoO ve uyum olasılığı p_uyum | c_RoO başlangıç aralığı %2–6 ad valorem (Dünya Bankası 2014; BKP 2016 %2). p_uyum referansları: İngiltere'nin AB'ye ihracatında tercih kullanım oranı %77,7 (2021), %82,8 (2022), %80,8 (2023) `[V]` (DBT/HMRC); revize PEM ürüne özgü kuralları | — |
| V-21 | Senaryo tanımları | S0–S5 prompttaki gibi. S2'ye "IAA/Made in Europe eşdeğerliği" ve "AKÇT çelik kotası/eritme-döküm" düzenlemesi eklendi | Faz 0 bulguları 7–8 |
| V-22 | Küresel bindirmeler | G1–G5 prompttaki gibi. G1 tabanı: ABD 301'de Türkiye %12,5, AB %10 tavanı; 232'de Türkiye'ye indirim yok | `[V]` USTR, Temmuz 2026 |
| V-23 | KOBİ tanımı | KOBİ Yönetmeliği eşikleri: 250 çalışan ve güncel ciro/bilanço eşiği | `[D?]`: güncel TL eşiği Faz 3'te doğrulanacak |
| V-24 | Bölge birimi | İBBS Düzey 2 (26 bölge) | Prompt |
| V-25 | Tarih gösterimi | Eylem takvimleri T'ye göre ve her iki takvim için nominal tarihle (T2028 ve T2029) verilir | — |
| V-26 | Dış ticaret ölçüsü | AB tarafı maruziyeti için Comext (AB ithalatı, CIF, menşe ülke). Türkiye tarafı için TÜİK genel ticaret sistemi (FOB). Ayna veri farkları Faz 1'de mutabakata bağlanır | — |
| V-27 | Üyelik perspektifi | **Yok.** Diplomatik çerçeve: "üyelikten bağımsız, çıkar temelli ekonomik ortaklık". Ankara Anlaşması feshedilmez: 1/80 ve Katma Protokol md. 41 hakları AB'deki Türk vatandaşları için korunur, 1/95'in sona ermesi bu hakları etkilemez (A-8). Sonuçlar: (a) AB katılım öncesi mali yardımları (IPA) sona erer; (b) müktesebata uyum hedefi kalkar, teknik mevzuat uyumu yalnızca pazar erişimi için yapılır (temel ilke 9); (c) md. 218(8)'deki aday ülke hükmü gündemden çıkar, md. 207 yolu tercih edilir | Kullanıcı yanıtı (Revizyon 1); temel ilke 2 |
| V-28 | Görev çerçevesi | Çıkış yönü veri. S1 (modernize GB) öneri seçeneği değil, maliyet karşılaştırma ölçütü. Çıkışın net negatif kaldığı yerlerde bunu pozitife çevirecek tasarım koşulları ve gerçekçilikleri yazılır | Kullanıcı yanıtı (Revizyon 1); `<gorev>` |
| V-29 | Veri erişimi | Bütün veriler çevrim içi kaynaklardan (API ve kazıma) alınır. TÜİK için Dağıtım Yönetim Sistemi arka ucu (anonim) ve Veri Portalı arama API'si kullanılır; erişim kodu `kod/tuik.py` | Kullanıcı yanıtı (Revizyon 1) |

---

## 4. Veri envanteri ve erişim planı

| # | Veri seti | Kaynak | Son dönem | Erişim (17.10.2026) | Kullanıldığı analiz | Yedek kaynak |
|---|---|---|---|---|---|---|
| 1 | AB–TR ticareti, CN8 × akış | Eurostat Comext DS-045409 | 2025 yıllık; Ağu 2026 aylık | ✓ API (2025 indirildi) | AB maruziyeti, rejim payları, `τ_AB` ağırlıkları, AME | UN Comtrade (AB beyanı) |
| 2 | TR dış ticareti, GTİP12 × ülke × rejim (DİR, serbest bölge) | TÜİK | 2025; aylık 2026 | ✗ portal; **kullanıcı yüklemesi** | Bütün sınıf kartları, ithalat yapısı, DİR etkisi | UN Comtrade (TR beyanı, HS6), BACI |
| 3 | Dünya ticareti, HS6 | CEPII BACI | 2023–2024 (HS22/HS17) | ✓ | RCA, rakip payları, PPML | UN Comtrade |
| 4 | Yıllık Sanayi ve Hizmet İstatistikleri (NACE 4 hane: üretim, katma değer, istihdam, girişim, ölçek) | TÜİK | 2024 `[D?]` | ✗; **kullanıcı yüklemesi** | Ölçek, verimlilik, KS | Eurostat SBS'de TR yok → yedek yok; İSO 500 ve Sanayi Sicil kısmi |
| 5 | PRODTR (ürün düzeyi üretim) | TÜİK | 2024 `[D?]` | ✗ | Kabiliyet, ürün çeşitliliği | Sanayi Sicil |
| 6 | Sanayi üretim endeksi | TÜİK; Eurostat `sts_inpr_m` | Ağu 2026 | ✓ Eurostat | Erken uyarı | — |
| 7 | Girdi-çıktı (2023 arz-kullanım ve simetrik tablo, 64 sektör) | TÜİK (Ağustos 2025 revizyonu) `[D?]` | 2023 | ✗; **kullanıcı yüklemesi** | Leontief fiyat ve miktar, EDE, ERP | OECD ICIO 2025 baskısı (TR, 2022), Eurostat FIGARO |
| 8 | TÜFE ağırlıkları ve alt endeksler (2025=100, COICOP 2018, 428 madde) | TÜİK | Eyl 2026 | ✗ | EDE, enflasyon yolu | Eurostat HICP ağırlıkları (TR, 2025) ✓ |
| 9 | Yİ-ÜFE (CPA/NACE) | TÜİK; Eurostat `sts_inppd_m` | Eyl 2026 | ✓ Eurostat (toplam düzey) | Maliyet geçişkenliği | — |
| 10 | Bölgesel istihdam ve ihracat (İBBS-2, il) | SGK, TİM, Ticaret Bakanlığı | 2025 | Kısmen (SGK ✓) | Bölgesel etki | SGK istatistik yıllığı |
| 11 | Ödemeler dengesi (BPM6) | TCMB EVDS | Ağu 2026 | ✓ (anahtar gerekir) | Cari denge köprüsü | IMF BOP |
| 12 | Sektör bilançoları (NACE) | TCMB | 2024 | ✓ web | Finansal kırılganlık, KOBİ finansmanı | KAP |
| 13 | KKO (NACE 2 hane), iktisadi yönelim anketi | TCMB | Eyl–Eki 2026 | ✓ | Erken uyarı | — |
| 14 | Doğrudan yatırım (stok, akım, gelir) | TCMB | 2025 | ✓ | Çapa yatırımcı, birincil gelir | OECD FDI |
| 15 | Kur geçişkenliği ve endeksleme çalışmaları | TCMB çalışma tebliğleri, Enflasyon Raporları | 2018–2026 | ✓ | ρ, φ | Akademik literatür |
| 16 | Uygulanan tarife cetveli (GTİP12, OGT + İGV) ve 2026 İthalat Rejimi Kararı | Ticaret Bakanlığı, Resmî Gazete (31.12.2025, No. 33124) | 2026 | ✗; **kullanıcı yüklemesi** | Tarife cetveli taslağı, ERP | WTO IDB/TDF (uygulanan), WITS TRAINS, ITC MAcMap |
| 17 | Türkiye'nin ticaret savunma önlemleri | Ticaret Bakanlığı | 2026 | ✗ (502) | Kamu yararı testi, EDE | WTO I-TIP, Global Trade Alert |
| 18 | AB tarifesi (CN 2026, Uyg. Tüzüğü (AB) 2025/1926) ve TARIC | AB | 2026 | ✓ EUR-Lex | `τ_AB`, tepe tarifeler, AVE | WITS, MAcMap |
| 19 | Menşe kuralları (revize PEM, Karar 1/2023) | PEM Ortak Komitesi, DG TAXUD, Access2Markets | 2025– | ✓ | c_RoO, p_uyum, ürün ağacı simülasyonu | — |
| 20 | AB'nin Türkiye'ye karşı ticaret savunması | DG TRADE, TARIC | 2026 | ✓ | Risk, S5 | — |
| 21 | SKDM varsayılan değerleri (Uyg. Tüzüğü 2025/2621), sertifika fiyatları | DG TAXUD | 2026 | ✓ | G arketipi, AB pazarında karbon maliyeti | — |
| 22 | AB çelik rejimi (Tüzük 2026/1384) ve kota tahsisleri | DG TRADE, TAXUD | 2026 | ✓ | 24.xx sınıfları | Sektör basını (GMK, SteelOrbis) |
| 23 | DTÖ bağlı ve uygulanan oranlar (satır düzeyi) | WTO TDF/IDB | 2025 | Kısmen (ttd ✗) | Bağlı oran kontrolü, politika alanı haritası | WITS ✓ |
| 24 | ITA-I kapsamı (WT/LET/173) | WTO | — | ✓ | 26.xx, 27.xx kontrolü | — |
| 25 | OECD ICIO / TiVA | OECD | 1995–2022 (2025 baskısı) | ✓ | İthal girdi içeriği, yurt içi katma değer, ERP katsayıları | Eurostat FIGARO |
| 26 | GTAP 12 | Purdue GTAP | 2017/2019/2023 referans yılları | Lisanslı | CGE | GE-PPML + literatür |
| 27 | Ürün karmaşıklığı (PCI), ürün uzayı | Harvard Growth Lab Atlas | 2023–2024 | ✓ | KS | OEC |
| 28 | UNIDO INDSTAT (ISIC 4 hane) | UNIDO | 2023 | ✓ | AB'ye göre verimlilik | Eurostat SBS (AB tarafı) |
| 29 | Patent ve tasarım | WIPO, EPO PATSTAT | 2024 | WIPO ✓; PATSTAT lisanslı | KS Ar-Ge bileşeni | Türk Patent ve Marka Kurumu |
| 30 | Ticaret müdahaleleri | Global Trade Alert | 2026 | ✓ | Ortam, misilleme riski | WTO TMDB |
| 31 | Literatür: Dünya Bankası 2014, BKP 2016, SWD(2016) 475/476, Türkiye Raporu 2025 | DB, Komisyon | — | ✓ indirildi | Teşhis, karşı-olgu | — |
| 32 | OVP 2027–2029, 12. Kalkınma Planı, 2030 Sanayi ve Teknoloji Stratejisi, CK 9903 teşvik kararı | SBB, Sanayi ve Teknoloji Bak. | 2023–2026 | ✓ | Makro baz, hedefler | — |
| 33 | Sanayi Sicil, Girişimci Bilgi Sistemi, teşvik belgeleri | Sanayi ve Teknoloji Bakanlığı | 2025 | Kısmen | Firma sayısı, yatırım | İSO 500 |
| 34 | Çapa yatırımcı ve sektör verileri (İSO 500 ve İkinci 500, OSD, TAYSAD, TÇÜD, TÜRKBESD, İTKİB) | Sanayi kuruluşları | 2025 | ✓ (web) | Çapa yatırımcı analizi | Şirket raporları |
| 35 | Brexit ampirik kanıtı (tercih kullanım oranları, firma çıkışı) | DBT/HMRC, CEP/LSE, OBR | 2021–2026 | ✓ | p_uyum, KOBİ etkisi, S3 kalibrasyonu | — |
| 36 | NACE, CPA, CN yazışma tabloları | Eurostat / EU Vocabularies, GİB | 2025–2026 | ✓ indirildi | Eşleştirme | UN/WITS |

**İlk veri boşlukları ve kapatma planı.** Bu liste her fazda güncellenir; Faz 9'da ek olarak verilir.

| No | Boşluk | Etkilediği analiz | Kapatma yolu (veri, kurum, süre) |
|---|---|---|---|
| VB-01 | NACE 4 haneli üretim, katma değer, istihdam ve girişim sayısı | Ölçek, KS, istihdam, kabiliyet eşiği | TÜİK YSHİ 2019–2024 tabloları veya mikro veri (TÜİK Mikro Veri Merkezi); kullanıcı yüklerse hemen; resmî başvuruyla 4–8 hafta |
| VB-02 | GTİP12 × ülke × rejim dış ticareti | DİR etkisi, ithal girdi, menşe | TÜİK dış ticaret veri tabanı veya Ticaret Bakanlığı; 1–2 hafta. Yedek: UN Comtrade HS6 (anahtar ücretsiz) |
| VB-03 | 2023 girdi-çıktı tabloları (64 sektör) | Enflasyon (EDE), ERP | TÜİK; kullanıcı yüklemesi. Yedek: OECD ICIO 2022 (hemen) |
| VB-04 | TÜFE madde ağırlıkları (428 madde) ve COICOP–CPA köprüsü | EDE, ρ | TÜİK; yedek: Eurostat HICP (ECOICOP) ağırlıkları |
| VB-05 | Uygulanan tarife ve İGV listesi (GTİP12, 2026) | Tarife cetveli, ERP | Ticaret Bakanlığı veya Resmî Gazete ekleri (CK 31.12.2025 ve 11.7.2026 değişikliği); kullanıcı yüklemesi |
| VB-06 | 1/95 Ek 1 (İTÜ listesi, 1/2007 değişikliğiyle) satır içeriği | İTÜ/GB ayrımı (tütün, içecekler) | EUR-Lex'te tablo görüntü olarak; Ticaret Bakanlığı İTÜ mevzuatı veya TARIC'teki Türkiye tercih satırları; Faz 3 |
| VB-07 | 2025 cari denge tutarsızlığı (−$25,2 mlr ilk açıklama / −$30,3 mlr OVP) | Cari denge köprüsü bazı | TCMB EVDS revize seri; Faz 1 |
| VB-08 | Türkiye'nin AB çelik kotası toplam tahsisi (basında 2,86 Mt) | 24.xx | DG TAXUD kota tablosu; Faz 3 |
| VB-09 | Sektör bazında çapa yatırımcı ve tedarikçi ağı verisi | Çapa yatırımcı tutma planı, tedarikçi çarpanı | OSD, TAYSAD, TÜRKBESD ve Sanayi Sicil; Faz 4 |

---

## 5. NACE kapsam listesi

### 5.1 Yöntem

1. **Sınıf listesi:** C bölümünde 24 bölüm, 95 grup, **230 sınıf** `[V]` (Eurostat NACE_R2 kod listesi; NACE Rev. 2 toplamı 615 sınıf). Rev. 2.1'de C bölümü 232 sınıftır `[V]`.
2. **Ürün eşleştirmesi:** CN2025 (9.778 satır) → CPA 2.2 → CPA 2.1 → NACE Rev. 2 sınıfı (CPA 2.1 kodunun ilk 4 hanesi). Kaynak: EU Vocabularies'teki resmî tablolar `[V]`. NACE'de karşılığı olmayan CPA 31.00 (oturmalık ve mobilya parçaları) 31.09'a atandı `[H]`.
3. **Rejim kuralları (CN8):**
   - **AKÇT-STA:** 1996 AKÇT–Türkiye Anlaşması Ek I'deki 280 CN 1996 satırı (resmî metinden çıkarıldı; `veri/akct_1996_cn8.txt`). HS6 düzeyinde aktarıldı; artık alt başlıklarda ('90', '99'), 7202 ferro alaşımlarda ve 2619'da satır düzeyinde eşleşme arandı.
   - **TARIM-1/98:** ABİHA Ek I tarım ürünleri (fasıl 1–24'ün büyük bölümü ile 4501, 5301, 5302); balıkçılık ürünleri dahil.
   - **İTÜ:** AB'nin Ek I dışı işlenmiş tarım ürünleri listesi esas alındı: fasıl 19 ve 21; 1704, 1803–1806; 2202, 2203, 2205, 2208 (tağyir edilmemiş etil alkol hariç); 2402–2404; sorbitol ve mannitol; 3501, 3502, 3505, 3809 10, 3823 vb. 1/95 Ek 1'in satır içeriği doğrulanamadı (VB-06).
   - **GB:** geri kalan sanayi ürünleri (fasıl 25–97) ve fasıl 1–24 içindeki Ek I dışı sanayi ürünleri (ör. tüy, kıl, su).
4. **Ağırlık:** Türkiye'nin AB'ye ihracatı (Comext 2025). İhracat €1 mn'un altındaysa AB'nin Türkiye'ye ihracatı; ikili ticaret €25 mn'un altındaysa CN satır sayısı kullanıldı. Bu son kural 10.12'yi düzeltiyor: AB–TR kanatlı eti ticareti SPS kısıtları nedeniyle sıfır, ticaret yalnızca tüyden ibaret.
5. **Etiket:** tek rejimin payı ≥ %97,5 ise o rejim; aksi halde KARMA, paylarıyla birlikte (satır ağırlığında eşik %90). CPA'da çıktısı "hizmet" olarak tanımlanan fason sınıflar **GB (dolaylı)** olarak işaretlendi. Bunların fiziksel çıktısı (dökme parça, kaplanmış veya işlenmiş parça, bitmiş kumaş, basılı ürün) GB kapsamındaki mal satırlarında sınıflanır. Onarım, bakım ve kurulum sınıfları KAPSAM DIŞI.
6. **Mutabakat:** C sınıfları toplamı €97,55 mlr, C dışı ürünler €5,74 mlr; toplam €103,29 mlr, Comext toplamıyla (€103,31 mlr) uyumlu `[V]`. Fark yuvarlama ve fasıl 99 gizli kodlarından kaynaklanıyor.
7. **Sınırlamalar:** AB ithalat verisi (ayna veri) kullanıldı; Türkiye'nin dünyaya ihracatıyla ağırlıklandırma Faz 1'de eklenecek. Çelik ve İTÜ sınırları CN satırında doğrulanacak (Güven: O).

### 5.2 C bölümü: NACE bölümü bazında sıkıştırılmış tablo

"GB dışı sınıflar" sütununda adı geçmeyen bütün sınıflar **GB** statüsündedir. Sınıf düzeyindeki tüm satırlar `veri/nace_kapsam.csv` dosyasındadır.

| Bölüm | Ad | Sınıf | GB | GB dışı sınıflar (etiket) | TR→AB 2025 (mn €) | AB→TR 2025 (mn €) | Rev. 2.1 değişikliği |
|---|---|---|---|---|---|---|---|
| 10 | Gıda ürünleri | 25 | 0 | TARIM-1/98: 10.12, 10.13, 10.20, 10.32, 10.39, 10.41, 10.42, 10.51, 10.81, 10.91, 10.92 · İTÜ: 10.52, 10.71, 10.72, 10.73, 10.82, 10.85, 10.89 · KARMA: 10.11, 10.31, 10.61, 10.62, 10.83, 10.84, 10.86 | 5.129,5 | 3.546,6 | 10.86 altı sınıfa bölünüyor; 10.89'un bir kısmı 11.07'ye |
| 11 | İçecekler | 7 | 0 | İTÜ: 11.01, 11.04, 11.05 · TARIM-1/98: 11.02, 11.03, 11.06 · KARMA: 11.07 | 137,4 | 513,9 | 11.07, 10.89'dan pay alıyor |
| 12 | Tütün ürünleri | 1 | 0 | KARMA: 12.00 | 133,4 | 519,4 | — |
| 13 | Tekstil | 10 | 10 (13.30 dolaylı) | — | 4.267,5 | 1.341,1 | 13.20 → 13.20/13.96/23.99; 13.92 → 13.92/13.96 |
| 14 | Giyim | 8 | 8 | — | 8.472,3 | 1.916,3 | Yeniden yapılandırma: 8 sınıf → 6 (14.10, 14.21–14.24, 14.29) |
| 15 | Deri ve ayakkabı | 3 | 3 | — | 520,0 | 1.256,0 | 15.20, 16.29/22.19/22.29'dan pay alıyor |
| 16 | Ağaç ürünleri | 6 | 6 | — | 324,8 | 276,3 | 16.10 → 16.11/16.12; 16.21–16.24 ve 16.29 kısmen 16.25–16.28'e |
| 17 | Kağıt | 7 | 7 | — | 968,4 | 2.019,2 | 17.29 → 17.25 |
| 18 | Basım ve kayıt ortamı | 5 | 4 (18.11, 18.12, 18.20 dolaylı) | KAPSAM DIŞI: 18.14 | 8,9 | 7,7 | 18.12'nin bir kısmı 13.30'a |
| 19 | Kok ve rafine petrol | 2 | 1 | AKÇT-STA: 19.10 | 3.071,2 | 1.546,3 | 19.20 adı "ve fosil yakıt ürünleri" oldu |
| 20 | Kimya | 16 | 14 | KARMA: 20.14, 20.53 | 4.719,4 | 10.535,9 | 20.51 (patlayıcı) → 20.59; yeni 20.51 sıvı biyoyakıt; 20.52/20.53 → 20.59 |
| 21 | İlaç | 2 | 2 | — | 553,6 | 3.866,9 | — |
| 22 | Kauçuk ve plastik | 6 | 6 | — | 5.291,9 | 3.498,7 | 22.19 → 22.12; 22.2x yeniden düzenleniyor (22.23–22.26) |
| 23 | Metalik olmayan mineraller | 24 | 24 | — | 3.048,6 | 2.094,7 | 23.19→23.15; 23.49→23.45; 23.69→23.66; 23.12'nin bir kısmı 29.32'ye; 23.42/23.69/23.70'in bir kısmı 31.00'a |
| 24 | Ana metal | 16 | 12 (24.53, 24.54 dolaylı) | KARMA: 24.10, 24.31, 24.33 · AKÇT-STA: 24.32 | 8.549,5 | 5.825,5 | 24.53 → 24.53/24.54 |
| 25 | Metal ürünler | 17 | 17 (25.50, 25.61, 25.62 dolaylı) | — | 6.299,4 | 3.041,3 | Yeniden numaralama: 25.29→25.22, 25.30→25.21, 25.40→25.30, 25.50→25.40, 25.61→25.51–25.53, 25.62→25.53, 25.71–25.73→25.61–25.63 |
| 26 | Elektronik ve optik | 10 | 10 | — | 862,2 | 6.215,3 | 26.20→26.20/26.40; 26.30→26.30/26.51; 26.80→26.70 |
| 27 | Elektrikli teçhizat | 10 | 10 | — | 9.507,7 | 8.359,3 | 27.11/27.12/27.90 arasında kayma; 27.11'in bir kısmı 29.10'a, 27.90'ın bir kısmı 29.31 ve 32.99'a |
| 28 | Makine | 21 | 21 | — | 10.381,1 | 17.723,0 | 28.49→27.90/28.41/28.42; yeni 28.97 (eklemeli imalat makineleri); 28.11'in bir kısmı 29.32/30.91'e |
| 29 | Motorlu kara taşıtları | 4 | 4 | — | 19.763,6 | 21.306,7 | 27.11, 23.12, 28.11 ve 28.25'ten pay alıyor |
| 30 | Diğer ulaşım araçları | 8 | 8 | — | 2.756,1 | 5.635,2 | 30.11→30.11/30.13 (askerî gemi); 30.30→30.31/30.32 (sivil/askerî hava ve uzay); 30.40'ın bir kısmı 33.18'e |
| 31 | Mobilya | 4 | 4 | — | 1.248,4 | 366,5 | 31.01–31.09 tek sınıfta (31.00) birleşiyor |
| 32 | Diğer imalat | 9 | 9 | — | 1.537,9 | 4.293,2 | 32.50 → 20.59/26.60/32.50; 32.30'un bir kısmı 32.99'a |
| 33 | Onarım ve kurulum | 9 | 0 | KAPSAM DIŞI: 33.11–33.17, 33.19, 33.20 | — | — | 33.12/33.15/33.16'nın askerî kısımları yeni 33.18'e |
| **C** | **Toplam** | **230** | **180** (9'u dolaylı) | TARIM-1/98 14 · KARMA 14 · İTÜ 10 · AKÇT-STA 2 · KAPSAM DIŞI 10 | **97.552,8** | **105.705,0** | 137 sınıf 1:1; 38 sınıf daha geniş bir Rev. 2.1 sınıfına birleşiyor; 55 sınıf 2–6 sınıfa bölünüyor |

**Yoğunlaşma:** Türkiye'nin AB'ye C bölümü ihracatının %17,1'i tek sınıfta, 29.10'da (€16,6 mlr). İlk 10 sınıf (29.10, 14.13, 27.11, 24.10, 10.39, 19.20, 28.25, 28.11, 27.51, 24.42) toplamın %44,5'ini, ilk 25 sınıf %65,4'ünü oluşturuyor `[V]` (Comext 2025, CPA eşleştirmesine göre).

### 5.3 KARMA sınıflar ve rejim payları

Paylar (%) Türkiye'nin AB'ye ihracatıyla ağırlıklıdır; son sütunlar AB'nin Türkiye'ye ihracatıyla (Türkiye'nin AB'den ithalatı) ağırlıklı paylardır.

| Kod | Ad | GB | AKÇT | İTÜ | Tarım | İthalatta GB/AKÇT/İTÜ/Tarım | Karma olmasının nedeni |
|---|---|---|---|---|---|---|---|
| 10.11 | Et (kümes hayvanı hariç) | 19,8 | 0 | 0 | 80,2 | 5,9 / 0 / 0 / 94,1 | Ham deri (HS 41) GB; et Ek I |
| 10.31 | Patates işleme | 0 | 0 | 18,2 | 81,8 | 0 / 0 / 7,1 / 92,9 | Patates unu ve pulu İTÜ (satır ağırlığı) |
| 10.61 | Öğütülmüş tahıl | 0 | 0 | 51,3 | 48,7 | 0 / 0 / 13,1 / 86,9 | Bulgur ve kahvaltılık tahıllar (HS 1904) İTÜ; un Ek I |
| 10.62 | Nişasta | 0 | 0 | 95,0 | 5,0 | 0 / 0 / 60,8 / 39,2 | Dekstrin ve modifiye nişasta İTÜ; glikoz Ek I |
| 10.83 | Kahve ve çay | 0 | 0 | 40,9 | 59,1 | 0 / 0 / 54,0 / 46,0 | Kahve ve çay özleri (HS 2101) İTÜ |
| 10.84 | Baharat, sos, sirke | 10,9 | 0 | 56,4 | 32,7 | 1,3 / 0 / 88,9 / 9,8 | Soslar İTÜ; sirke ve baharat Ek I; tuz GB |
| 10.86 | Homojenize ve diyet gıdalar | 0 | 0 | 96,0 | 4,0 | 0 / 0 / 91,4 / 8,6 | Bebek mamaları İTÜ |
| 11.07 | Alkolsüz içecek ve su | 28,0 | 0 | 72,0 | 0 | 4,2 / 0 / 95,8 / 0 | Su GB; alkolsüz içecekler İTÜ |
| 12.00 | Tütün ürünleri | 0 | 0 | 95,1 | 4,9 | 0 / 0 / 66,3 / 33,7 | Sigara İTÜ `[D?]` (VB-06); işlenmiş yaprak tütün Ek I |
| 20.14 | Organik temel kimyasallar | 96,1 | 0 | 3,8 | 0,1 | 97,7 / 0 / 1,4 / 0,9 | Sorbitol ve mannitol İTÜ; etil alkol Ek I |
| 20.53 | Uçucu yağlar | 85,5 | 0 | 14,5 | 0 | 39,4 / 0 / 60,6 / 0 | Gıda sanayii aroma karışımları (3302 10) İTÜ |
| 24.10 | Ana demir-çelik ve ferro alaşımlar | 6,3 | 93,7 | 0 | 0 | 8,0 / 92,0 / 0 / 0 | Ferro alaşımların çoğu (ferrokrom dahil) GB; AKÇT listesinde yalnızca yüksek karbonlu ferromangan ve 7202 99 11 var |
| 24.31 | Barların soğuk çekilmesi | 93,2 | 6,8 | 0 | 0 | 78,7 / 21,3 / 0 / 0 | Bazı soğuk şekillendirilmiş çubuklar AKÇT listesinde |
| 24.33 | Soğuk şekillendirme | 94,3 | 5,7 | 0 | 0 | 85,2 / 14,8 / 0 / 0 | Soğuk şekillendirilmiş profillerin bir kısmı AKÇT |
| 38.32 | Geri kazanım (E) | 90,4 | 9,6 | 0 | 0 | 40,1 / 59,9 / 0 / 0 | **Demir hurdası (HS 7204) AKÇT ürünü**; AB→TR hurda €3,05 mlr |
| A01 | Bitkisel ve hayvansal üretim | 3,8 | 0 | 0 | 96,2 | 12,4 / 0 / 0 / 87,6 | Ham pamuk ve yapağı Ek I dışı (GB) |
| A02 | Ormancılık | 72,7 | 0 | 0 | 27,3 | satır ağırlığı | Tomruk GB; doğal mantar Ek I |

**Dolaylı GB (9 sınıf):** 13.30 (boya-terbiye), 18.11 ve 18.12 (basım), 18.20 (kayıt ortamı çoğaltma), 24.53 ve 24.54 (hafif ve diğer demir dışı metal dökümü), 25.50 (dövme ve presleme), 25.61 (kaplama ve ısıl işlem), 25.62 (talaşlı imalat). Bu sınıflar GB'nin doğrudan değil, müşteri sektörler üzerinden etkileyeceği tier-2 tedarikçilerdir; menşe kuralı maliyetini en çok taşıyacak KOBİ yoğun halkalar bunlardır `[H]`.

**KAPSAM DIŞI (10 sınıf):** 18.14 ve 33.11–33.20 hizmettir. 33.15 (gemi onarımı) ve 33.16 (uçak bakımı, MRO) hizmet ihracatıdır; GB'den bağımsız olarak EASA Part-145 ve hizmet müzakeresine bağlıdır.

### 5.4 B, D, E, A ve hizmet kapsamı

| Grup | Kod | Ad | GB statüsü | Pay GB/AKÇT/İTÜ/Tarım (%) | TR→AB 2025 (mn €) | AB→TR 2025 (mn €) | Not |
|---|---|---|---|---|---|---|---|
| B | 05.10 | Taş kömürü | AKÇT-STA | 0/100/0/0 | 6,1 | 19,4 | |
| B | 05.20 | Linyit | AKÇT-STA | 0/100/0/0 | 0,9 | 0,0 | |
| B | 06.10 | Ham petrol | GB | 100/0/0/0 | 313,4 | 268,6 | |
| B | 06.20 | Doğal gaz | GB | 100/0/0/0 | 138,3 | 16,2 | Sakarya sahası enerji köprüsüne bağlanır |
| B | 07.10 | Demir cevherleri | AKÇT-STA | 0/100/0/0 | 8,9 | 119,7 | |
| B | 07.21 | Uranyum ve toryum | GB `[D?]` | — | 0 | 0 | Euratom ürünlerinin GB kapsamı doğrulanacak |
| B | 07.29 | Diğer demir dışı metal cevherleri | GB | 99,9/0,1/0/0 | 584,7 | 10,2 | Krom, bakır, çinko, nadir toprak elementleri; kritik hammadde |
| B | 08.11 | Süs ve yapı taşı ocakçılığı | GB | 100/0/0/0 | 36,0 | 8,1 | Ham mermer blok; işlenmiş mermer 23.70'te |
| B | 08.12 | Kum, çakıl, kil, kaolin | GB | 100/0/0/0 | 154,1 | 76,5 | |
| B | 08.91 | Kimyasal ve gübre mineralleri | GB | 100/0/0/0 | 73,0 | 71,6 | Ham bor mineralleri |
| B | 08.92 | Turba | GB | satır | 0,0 | 17,0 | |
| B | 08.93 | Tuz | GB | satır | 14,0 | 1,7 | |
| B | 08.99 | B.y.s. diğer madencilik | GB | 100/0/0/0 | 368,2 | 34,7 | Feldspat, perlit, barit |
| B | 09.10, 09.90 | Madencilik destek hizmetleri | KAPSAM DIŞI | — | — | — | Hizmet |
| D | 35.11 | Elektrik üretimi | GB | 100/0/0/0 | 154,5 | 12,2 | SKDM kapsamında; ENTSO-E bağlantısı |
| E | 38.31 | Hurdaların sökülmesi | KAPSAM DIŞI | — | — | — | Gemi söküm (Aliağa); çıktı 38.32 ve 38.11'de |
| E | 38.32 | Geri kazanım | KARMA | 90,4/9,6/0/0 | 1.327,4 | 5.095,9 | Hurdanın serbest dolaşımı **GB değil 1996 AKÇT STA'sı** (md. 3–4: ihracat vergisi ve miktar kısıtlaması yasağı) ile korunuyor |
| A | A01 | Bitkisel ve hayvansal üretim | KARMA | 3,8/0/0/96,2 | 1.848,0 | 1.319,6 | Yalnızca İTÜ bağlantısı ve DCFTA tarım müzakeresi için |
| A | A02 | Ormancılık | KARMA | 72,7/0/0/27,3 | 8,4 | 15,6 | EUDR (30.12.2026'dan itibaren) |
| A | A03 | Balıkçılık ve su ürünleri | TARIM-1/98 | 1,0/0/0/99,0 | 388,6 | 7,2 | Levrek ve çipura; 1/98 (2/2006 ile değişik) |
| Hizmet | 46 | Toptan ticaret | KAPSAM DIŞI | — | — | — | İthalat dağıtımı; 46.77 hurda toptancılığı |
| Hizmet | 49.41 | Karayolu yük taşımacılığı | KAPSAM DIŞI | — | — | — | Kota, geçiş belgesi, vize; S2'de hücum hedefi |
| Hizmet | 50.20 | Deniz yük taşımacılığı | KAPSAM DIŞI | — | — | — | Ro-Ro hatları |
| Hizmet | 52.10 | Depolama ve ambarlama | KAPSAM DIŞI | — | — | — | |
| Hizmet | 52.29 | Taşımacılığı destekleyici diğer faaliyetler | KAPSAM DIŞI | — | — | — | Gümrük müşavirliği; menşe ispatına geçişte kapasite |
| Hizmet | 62 | Yazılım ve BT hizmetleri | KAPSAM DIŞI | — | — | — | Dijital ticaret |
| Hizmet | 71.20 | Teknik test ve analiz | KAPSAM DIŞI | — | — | — | Onaylanmış kuruluşlar, ACAA |
| Hizmet | F | İnşaat | KAPSAM DIŞI | — | — | — | AB kamu alımlarına erişim; hücum hedefi |

---

## 6. `[D?]` bağlam maddelerinin doğrulama durumu

Durum: **Doğrulandı** / **Güncellendi** (düzeltme veya yeni gelişme) / **Kısmen** / **Doğrulanamadı**. Kaynaklar resmî metinlerdir (EUR-Lex, Konsey belgeleri, WTO, UNTC, mevzuat.gov.tr); basın kaynaklı maddeler ayrıca belirtilmiştir.

### 6.1 Hukuki mimari (bağlam A)

| No | Madde | Durum | Bulgu | Kaynak |
|---|---|---|---|---|
| A-1 | Ankara Anlaşması imza ve yürürlük | Doğrulandı | İmza 12.9.1963, yürürlük 1.12.1964 (md. 32). **Yeni:** süre, fesih veya çekilme hükmü yok (son hükümler md. 28–33); Ortaklık Konseyi oybirliğiyle karar alır (md. 23); uyuşmazlık çözümü zorunlu yargı yetkisi içermez (md. 25) | CELEX 21964A1229(01) |
| A-2 | Katma Protokol imza ve yürürlük | Doğrulandı | İmza 23.11.1970, yürürlük 1.1.1973 (Tüzük (AET) 2760/72; OJ L 293, 29.12.1972) | CELEX 21970A1123(01) |
| A-3 | 1/95 sayılı Karar, OJ referansı ve yürürlük | Güncellendi | OJ L 35, 13.2.1996, s. 1–47 doğru. Yürürlük hükmü **md. 65(1)**: "31 Aralık 1995'te yürürlüğe girer"; md. 66 yorum hükmüdür. Karar 22.12.1995 tarihli; esasları 6.3.1995 Ortaklık Konseyi'nde kararlaştırıldı | CELEX 21996D0213(01) |
| A-4 | AKÇT ürünleri GB dışında, ayrı 1996 STA | Doğrulandı, ayrıntı güncellendi | 1/95'te açık bir AKÇT istisnası yok; Ankara çerçevesi AET'ye ilişkin olduğu için kömür ve çelik dışarıda kalıyor. AKÇT–Türkiye Anlaşması 25.7.1996'da imzalandı (OJ L 227, 7.9.1996). Ek I: demir ve manganez cevheri, kömür, linyit, kok, pik demir, yalnızca belirli ferro alaşımlar, sünger demir, **hurdanın tamamı (7204)**, fasıl 72 çeliği, palplanş, demiryolu malzemesi; **borular (7304–7306) kapsam dışı**. Md. 3–4: ithalat ve ihracatta gümrük vergisi ve miktar kısıtlaması yasağı; md. 12: korunma. AKÇT Antlaşması'nın sona ermesinden sonra haklar ve yükümlülükler AT'ye, ardından AB'ye geçti (Konsey Kararı 2002/596/AT). Fiilî yürürlük tarihi doğrulanamadı | CELEX 21996A0907(01); 32002D0596 |
| A-5 | Temel tarım ürünleri 1/98 rejiminde | Doğrulandı, güncellendi | 1/98 sayılı Karar 25.2.1998 (OJ L 86, 20.3.1998). Değişiklikler: 2/2006, 3/2006 (menşe), 1/2018 ve **1/2025 (22.12.2025; OJ L 2026/1903, 31.7.2026: Protokol 3'ü revize PEM kurallarına dinamik atıfla değiştiriyor)**. Balıkçılık ürünleri bu rejimde (BKP 2016: "tarım ve balıkçılık ticaret rejimi") | CELEX 21998D0320(01), 22026D1903 |
| A-6 | Türkiye'nin yükümlülüklerine ilişkin madde numaraları | Doğrulandı | Teknik mevzuat md. 8–11; ticaret politikası md. 12; OGT md. 13 (uyum kuralları md. 14–15); tercihli rejimler md. 16 ve Ek 10; İTÜ md. 17–23 ve Ek 1; tarım md. 24–27; gümrük md. 28–30; fikri mülkiyet md. 31 ve Ek 8; rekabet ve devlet yardımları md. 32–43; ticaret savunması md. 44–47; kamu alımları md. 48 (yalnızca müzakere taahhüdü); GB Ortak Komitesi md. 52–53; karar şekillendirme md. 54–60 (md. 58(2) tek taraflı koruma önlemi); uyuşmazlık md. 61–62 (sınırlı kapsamlı tahkim); korunma ve yeniden dengeleme md. 63–64 | CELEX 21996D0213(01) |
| A-7 | Katma Protokol md. 41 standstill ve ATAD içtihadı | Doğrulandı | Md. 41(1) metni doğrulandı. Savaş C-37/98 (2000): doğrudan etki. Tum ve Darı C-16/05 (2007): ilk kabul koşulları. Soysal C-228/06 (2009): hizmet sunucularına yeni vize şartı konamaz. Demirkan C-221/11 (2013): pasif hizmet alımı kapsam dışı. 1/80 md. 13 standstill: Doğan C-138/13 (2014), Genc C-561/14 (2016), A C-89/18 (2019) | CELEX 62011CJ0221 vd. |
| A-8 | "GB'den çık, Ortaklıktan değil" ayrımının hukuki dayanağı | Doğrulandı (analiz) | 1/80 ve Katma Protokol md. 41 hakları 1/95'ten bağımsızdır; 1/95 açıkça Ankara Anlaşması'na "halel getirmeksizin" kabul edilmiştir (md. 1). 1/95'in sona ermesi veya yerine başka bir çerçeve konması bu hakları kaldırmaz; Ankara Anlaşması'nın feshi kaldırır | 1/95 md. 1; Ankara md. 12 ve 22 |

### 6.2 Asimetriler ve modernizasyon (bağlam B)

| No | Madde | Durum | Bulgu | Kaynak |
|---|---|---|---|---|
| B-1 | Komisyon 2016 modernizasyon önerisi | Doğrulandı | COM(2016) 830 final ve etki analizi SWD(2016) 475 final, 21.12.2016 | SWD(2016) 476 başlığı |
| B-2 | Konsey 2018'de süreci dondurdu | Doğrulandı | Genel İşler Konseyi, 26.6.2018, para. 35: "no further work towards the modernisation of the EU-Turkey Customs Union is foreseen" | Konsey belgesi 10555/18 |
| B-3 | Güncel durum (Ekim 2026) | Güncellendi | **Konsey müzakere yetkisi yok** (Bolat, 14.10.2026; Komisyon konu konu çalışıyor). JOIN(2023) 50 (29.11.2023) yeniden başlamayı yaptırımların dolanılmasının önlenmesine ve sorunların çözümüne bağladı. AB Zirvesi 17–18.4.2024: "aşamalı, orantılı ve geri döndürülebilir" ilerleme. Üst düzey ticaret diyalogları 8.7.2024 ve Temmuz 2025; üçüncüsü ≈14.10.2026'da yapıldı, yetkilendirilmiş yükümlü (AEO) programlarının karşılıklı tanınması kararlaştırıldı (basın) `[D?]`. Fidan–Kos ortak açıklaması (6.2.2026). Ortaklık Konseyi 2019'dan beri toplanmıyor; kararlar yazılı usulle alınıyor (ör. 1/2025). Bolat: GB sorunları listesi 29'dan 14'e indi; Türkiye IAA'da "eşit ortak" statüsü istiyor. **GB'den çıkışı öneren resmî bir Türk açıklaması bulunamadı** | EEAS, Konsey, AA (Ekim 2026) |
| B-4 | Bilinen sürtünmeler | Güncellendi | Türkiye Raporu 2025, GB faslı: "iyi düzeyde hazırlık, ilerleme yok"; muafiyetler, serbest bölgeler ve gözetim rejimi "GB kurallarına aykırı"; AB'de serbest dolaşımdaki üçüncü ülke menşeli mallara ek vergiler; kıymete dayalı gözetim; ham deri ihracat vergileri; ilaçta yapay kur; GMP sertifikalarının tanınmaması; YEKA ve tütünde yerli katkı şartları. 2026'da İGV'nin ≈4.344 satırda %48'e kadar uygulandığı bildiriliyor (basın) `[D?]` | SWD(2025) 756 |

### 6.3 Çıkış ve dönüşüm hukuku (bağlam C)

| No | Madde | Durum | Bulgu | Kaynak |
|---|---|---|---|---|
| C-1 | VCLT md. 56 ve 65–67 | Doğrulandı | Md. 56: çekilme hükmü olmayan antlaşmadan ancak tarafların niyeti veya antlaşmanın niteliği izin veriyorsa çekilinebilir; en az 12 ay bildirim. Md. 65: yazılı bildirim ve 3 aylık itiraz süresi; md. 66: 12 ayda çözüm çıkmazsa uzlaştırma; md. 67: belge biçimi | BM Uluslararası Hukuk Komisyonu metni |
| C-2 | VCLT'nin taraflar bakımından uygulanabilirliği | Güncellendi (kritik) | **Türkiye VCLT'ye taraf da imzacı da değil** (17.10.2026: 45 imzacı, 119 taraf). AB de taraf değil; ATAD VCLT kurallarını teamül hukuku olarak uyguluyor (Racke C-162/96; Brita C-386/08). 1986 Sözleşmesi (uluslararası örgütler) yürürlükte değil. Sonuç: tek taraflı çıkış yalnızca teamül hukukuna dayanır | UNTC XXIII-1, XXIII-3 |
| C-3 | ABİHA md. 207, 217, 218(6), (8), (9) | Doğrulandı | Md. 207(4): NÇ; hizmetler, fikri mülkiyet ve doğrudan yabancı yatırım gibi belirli hallerde oybirliği. Md. 218(8): ortaklık anlaşmaları ve aday ülkelerle md. 212 anlaşmaları için oybirliği. Md. 218(9): anlaşma organlarında AB tutumu, kurumsal çerçeveyi değiştiren işlemler hariç. Md. 218(6): Avrupa Parlamentosu onayı | CELEX 12016E207, 12016E218 |
| C-4 | ATAD Görüş 2/15 | Doğrulandı | 16.5.2017: AB–Singapur STA'sı, portföy yatırımı ve ISDS dışında AB'nin münhasır yetkisinde | ATAD basın bülteni 52/17 |
| C-5 | Veto riski ve yasal dayanak | Doğrulandı (analiz) | Portföy yatırımı ve ISDS içermeyen bağımsız bir md. 207 ticaret anlaşması "yalnızca AB" niteliğinde olur; yetki ve onay NÇ ile, Avrupa Parlamentosu onayıyla verilir. Ortaklık anlaşması veya Ankara Protokolü (md. 217) olarak kurulursa oybirliği ve muhtemelen karma onay gerekir. C-81/13 (18.12.2014) para. 66: ortaklık anlaşmasını uygulayan kararlarda AB tutumu NÇ ile belirlenir. Ancak Ortaklık Konseyi oybirliğiyle karar alır ve Konsey pratikte uzlaşıyla çalışır; 2016 yetkisi hâlâ kabul edilmedi | CELEX 62013CJ0081; COM(2024) 559 |
| C-6 | Türkiye iç hukuku | Doğrulandı, güncellendi | Anayasa md. 90 (TBMM onayı ve istisnaları) doğrulandı. 4458 sayılı Gümrük Kanunu (RG 4.11.1999); Birlik Gümrük Kodu'na uyumlu taslak bekliyor. 2026 İthalat Rejimi Kararı RG 31.12.2025 (No. 33124); yıl içinde CK ile değişiyor. 7223 sayılı Kanun (RG 12.3.2020). 4734 md. 63: %15'e kadar yerli malı fiyat avantajı; 2024'te uluslararası ihalelerin değer bazında %54,39'unda uygulandı. **6015 sayılı Devlet Yardımları Kanunu fiilen işlemiyor** (uygulama 7061 sayılı Kanunla Cumhurbaşkanı kararına bağlandı). Antlaşmadan çekilmede Cumhurbaşkanlığı Kararnamesi No. 9 yetkisi `[D?]` | mevzuat.gov.tr; SWD(2025) 756 |
| C-7 | Türkiye'nin bağlı tarife cetveli: sanayide bağlama kısmi | Güncellendi | WTO World Tariff Profiles 2026: bağlama oranı toplam %50,5; tarım %100; sanayi %43,0. Ortalama bağlı oran %28,9 (tarım 61,8; sanayi 17,2). Uygulanan basit ortalama (2025) %17,3; tarım 39,9, sanayi 13,6; İGV dahil görünüyor (giyimde ortalama %49,4). Sektörel bağlama: giyim %3,7, tekstil %23,4, mineral-metal %24,3, petrol %20, kauçuk-deri-ayakkabı %47,8, taşıt %57,8, elektrikli makine %58,3, elektriksiz makine %68,6, kimya %66 | WTO TR profili, 2026 |
| C-8 | ITA kapsamında sıfır bağlı tarifeler | Doğrulandı | Türkiye ITA-I katılımcısı (WT/LET/173); **2015 genişlemesine (ITA-II) katılmadı** | WTO ITA sayfaları |
| C-9 | Türkiye GPA'da gözlemci | Doğrulandı | 4.6.1996'dan beri gözlemci; taraf değil, katılım müzakeresi yok | WTO GPA gözlemciler sayfası |

### 6.4 Küresel ve bölgesel ortam (bağlam D)

| No | Madde | Durum | Bulgu | Kaynak |
|---|---|---|---|---|
| D-1 | SKDM kesin dönem ve kapsam | Doğrulandı | 1.1.2026'da başladı; demir-çelik, alüminyum, çimento, gübre, hidrojen, elektrik | DG TAXUD |
| D-2 | SKDM 2025 sadeleştirme paketi | Doğrulandı | Tüzük (AB) 2025/2083: ithalatçı başına yıllık 50 ton eşiği (elektrik ve hidrojen hariç; emisyonların ≥%99'u kapsamda kalacak); sertifika satışı Şubat 2027'de (2026 ithalatı için); ilk beyan ve teslim 30.9.2027; çeyreklik tutma şartı %50 | Tüzük 2025/2083; DG TAXUD |
| D-3 | SKDM güncel gelişmeler | Güncellendi | COM(2025) 989 (17.12.2025): ≈180 çelik veya alüminyum yoğun mansap ürüne genişleme (1.1.2028) ve dolanım önleme. COM(2025) 990: Geçici Karbonsuzlaştırma Fonu. Konsey genel yaklaşımı 12.6.2026; Avrupa Parlamentosu pozisyonu 15.9.2026 (≈450 ürün; yüksek riskli menşeler için ülke bazlı varsayılan değerler; ETS bağlantısı olmayan STA ortaklarına muafiyet yok); üçlü görüşmeler 20.10.2026'da başlıyor. Varsayılan değerler: Uyg. Tüzüğü 2025/2621 (Türkiye'ye özgü değerler var). 2026 sertifika fiyatı: Ç1 €75,36, Ç2 €75,28, Ç3 €82,32/tCO₂. Üçüncü ülke karbon fiyatı mahsubu (md. 9): taslak 13.5.2026, kabul edilmedi | Mayer Brown (7.10.2026); DG TAXUD; GMK |
| D-4 | Türkiye ETS ve İklim Kanunu | Doğrulandı, güncellendi | 7552 sayılı İklim Kanunu: TBMM 2.7.2025, RG 9.7.2025 (No. 32951); 2053 net sıfır. TR-ETS Yönetmeliği RG 27.8.2026 (No. 33353). Pilot dönem 2026–2027: elektrik, çimento, demir-çelik, alüminyum, gübre; %100 ücretsiz tahsis; 2026 yalnızca raporlama. Ulusal Tahsis Planı yayımlanmadı | ICAP (Eylül 2026) |
| D-5 | AB çelik rejimi | Güncellendi | Korunma önlemi 30.6.2026'da sona erdi; **Tüzük (AB) 2026/1384** (17.6.2026) 1.7.2026'dan beri uygulanıyor: TRQ 18.345.922 t/yıl (−%47), kota dışı %50 (anti-damping ve telafi edici vergilere ek olarak), çeyreklik kotalar, eritme-döküm beyanı 1.10.2026'dan, tahsiste kullanımı 1.10.2027'den. Türkiye STA ortağı muamelesi görüyor: ülke kotaları (ör. sıcak haddelenmiş yassı 642.295 t/yıl) ve ≈9,15 Mt ortak STA havuzu. Toplam Türkiye tahsisi (basında 2,86 Mt) doğrulanamadı (VB-08) | tradecomplianceresourcehub (26.6.2026); DG TRADE |
| D-6 | AB hurda politikası | Güncellendi | AB'de hurda ihracat kısıtlaması kabul edilmedi; Temmuz 2025'ten beri gözetim var. Atık Taşımaları Tüzüğü (AB) 2024/1157: OECD dışı ülkelere ihracat 21.5.2027'den onaylı listeye bağlanıyor; Türkiye OECD üyesi olduğundan bu listeye tabi değil, md. 45 izlemesine tabi. 2025: AB hurda ihracatı 16,31 Mt, Türkiye'nin payı 10,78 Mt (%66). Türkiye ham çelik üretimi 38,1 Mt, %72,2 ark ocağı. **Hurda GB değil AKÇT STA ürünü; serbest dolaşımı 1996 Anlaşması md. 3–4 ile korunuyor** (A-4) | KPMG (7/2025); IndexBox (9/2026); TÇÜD |
| D-7 | "Made in Europe", ekonomik güvenlik, yatırım taraması | Güncellendi | IAA önerisi COM(2026) 100 (4.3.2026): kamu alımı, açık artırma ve destek programlarında AB menşei ve düşük karbon şartları; **STA ve gümrük birliği ortakları açık artırma ve kamu desteğinde AB menşeine eşdeğer**; karşılıklılık sağlamayan ortaklar Komisyonun devredilmiş tasarrufuyla (delegated act) dışlanabilir; STA'sı veya gümrük birliği olmayan ülke yatırımcılarına yeni yabancı yatırım şartları (%49 sahiplik tavanı, teknoloji transferi). SAFE (Tüzük 2025/1106): Yunanistan Türkiye'nin katılımını engelledi (4.2.2026). EDIP: AB ve ilişkili ülkeler dışından bileşen tavanı %35. Ekonomik güvenlik: JOIN(2025) 977 (3.12.2025). Revize yatırım tarama tüzüğü RG 26.6.2026, 17.1.2028'den uygulanır | Mayer Brown (3/2026); BCLP (6/2026) |
| D-8 | AB'nin yeni STA'ları | Güncellendi | Mercosur: imza 17.1.2026, geçici ticaret anlaşması 1.5.2026'dan beri geçici uygulamada (AP 21.1.2026'da ATAD görüşü istedi). Hindistan: müzakereler 27.1.2026'da tamamlandı, imza önerisi 11.9.2026. Endonezya: 2025'te sonuçlandı, Konsey'e 29.6.2026'da sunuldu. Meksika: imza 22.5.2026. Avustralya: 24.3.2026'da sonuçlandı. Şili geçici anlaşması 1.2.2025'ten beri yürürlükte. BAE, Tayland, Filipinler, Malezya müzakerede; KİK blok müzakeresi askıda | DG TRADE müzakere sayfası (17.10.2026) |
| D-9 | ABD tarife politikası | Güncellendi | ABD Yüksek Mahkemesi 20.2.2026 (Learning Resources v. Trump): IEEPA tarife yetkisi vermiyor. Bölüm 122 kapsamında %10 (24.2–24.7.2026) sona erdi. Bölüm 301 (zorla çalıştırma): **Türkiye %12,5 (24.7.2026'dan)**; AB toplam %10 tavanlı. Bölüm 232: çelik, alüminyum ve bakır %50, türevler %25, otomobil ve parça %25, ağır kamyon %25; **Türkiye'ye indirim yok**. ABD–Türkiye anlaşması yok; hedef 2028'e kadar $50 mlr ticaret (2025 mal ticareti ≈$36,8 mlr) | USTR FRN (23.7.2026); Beyaz Saray; Atlantic Council (6.10.2026) |
| D-10 | Çin: Türkiye'nin ek vergileri ve Çin yatırımları | Doğrulandı, güncellendi | CK 8639 (RG 8.6.2024): Çin menşeli benzinli ve hibrit binek otomobillere %40 veya en az $7.000 ek vergi; elektrikli araçlara 2023'ten beri %40; teşvik belgeli ithalata muafiyet. **DS629 (Çin–Türkiye) panel raporu 28.7.2026: EV ek vergileri bağlı oranları aşıyor (GATT II:1), XX(b) ve XX(g) ile haklı değil; ithalat izni şartı III:4'e aykırı.** BYD Manisa ($1 mlr) yatırımı askıda (Haziran 2026), teşviklerin askıya alındığı bildiriliyor (basın) | WTO DS629; electrive (6/2026) |
| D-11 | Rusya yaptırımları | Güncellendi | 18. paket (18.7.2025) md. 3ma: üçüncü ülkelerde Rus ham petrolünden rafine edilen ürünlerin AB'ye ithalat yasağı 21.1.2026'dan; Türkiye, Hindistan ve Çin ürünleri için güçlendirilmiş durum tespiti. KSE (11.6.2026): bu rafinerilerden AB ithalatı −%69; Tüpraş İzmit'in Rus ham petrol alımını artırdığı bildiriliyor. 20. paket (23.4.2026): Türkiye dahil ülkelerden 60'tan fazla kuruluş Ek IV'e (çift kullanımlı ürün kısıtı) eklendi; Türk bankası listelenmedi | Baker McKenzie (1/2026); KSE; DLA Piper (5/2026) |
| D-12 | DS583 (Türkiye — İlaç) | Doğrulandı, güncellendi | Md. 25 tahkim kararı taraflara 21.7.2022'de verildi, DSB'ye 25.7.2022'de bildirildi (ilk md. 25 temyiz tahkimi). Yerlileştirme şartı III:4'e aykırı; III:8(a) kamu alımı savunması ve XX(b)/(d) reddedildi. Türkiye 25.4.2023'te uyum bildirdi; uyum paneli yok | WTO DS583 |

### 6.5 Literatür ve belgeler (bağlam E)

| No | Madde | Durum | Bulgu | Kaynak |
|---|---|---|---|---|
| E-1 | Dünya Bankası (2014) | Doğrulandı | "Evaluation of the EU–Turkey Customs Union", Rapor No. 85830-TR, 28.3.2014. GB yerine STA olsaydı Türkiye'nin AB'ye ihracatı %3,0–7,2 daha düşük olurdu (menşe maliyeti %2–6); STA asimetrisi "potansiyel olarak çok maliyetli" | documents1.worldbank.org |
| E-2 | BKP Development (2016) | Doğrulandı | "Study of the EU-Turkey Bilateral Preferential Trade Framework, Including the Customs Union, and an Assessment of Its Possible Enhancement", 26.10.2016. Mevcut GB: Türkiye GSYH +%0,72. Modernize GB: Türkiye refahı +€12,5 mlr, GSYH +%1,44. GB yerine DCFTA: Türkiye refahı −€144 mn, AB'ye ihracat −€4,34 mlr, GSYH +%0,26 | SWD(2016) 475, Ek 6 |
| E-3 | Komisyon etki analizi SWD(2016) 475 | Doğrulandı | Yürütme özeti SWD(2016) 476 üzerinden. B seçeneği (modernizasyon ve kapsam genişletme) tercih edildi. C seçeneği (GB yerine sanayi STA'sı) menşe maliyeti ve siyasi geri adım görüntüsü nedeniyle reddedildi | SWD(2016) 476 |
| E-4 | Komisyon Türkiye Raporları | Güncellendi | 2025 Raporu: SWD(2025) 756, 4.11.2025. 2026 Raporu henüz yayımlanmadı (genişleme paketi ≈4.11.2026'ya kaydı) | Komisyon |
| E-5 | Brexit sonrası İngiltere–AB TCA'nın ampirik etkileri | Doğrulandı, kısmen | OBR: uzun vadede ihracat ve ithalat −%15, verimlilik −%4. Freeman ve diğ. (2024–25): kısa vadede İngiltere'nin dünya ihracatı −%6,4; kayıplar küçük firmalarda yoğun; AB'ye ihracat yapan firmaların ≈%14'ü çıktı. Du ve diğ. (2024): 2021–23'te AB'ye ihracat −%27, ihraç ürün çeşitliliği −%33,5. Tercih kullanım oranı: İngiltere'den AB'ye %77,7 / %82,8 / %80,8 (2021/22/23); AB'den İngiltere'ye %90,3 / %91,0 (2022/23). Brexit'e özgü menşe uyum maliyeti tahmini doğrulanamadı | OBR (20.7.2026); DBT/HMRC; CEP; Productivity Institute |
| E-6 | GB çıkışını modelleyen 2017–2026 çalışmaları | Kısmen | ifo/Bertelsmann (2016): GB'nin sona ermesi Türkiye GSYH −%0,81, AB'nin yeni STA'larıyla ek −%0,96. 2017–2026 döneminde TEPAV, EDAM, İKV, CEPS, SWP, Kiel veya Bruegel'den sayısal bir çıkış çalışması bulunamadı: **kanıt boşluğu** | ifo proje sayfası |
| E-7 | Türkiye resmî belgeleri | Güncellendi | **OVP 2027–2029 (6.9.2026)**: büyüme 2026 %3,3, 2027 %4,2; TÜFE 2026 %28,4, 2027 %21,0, 2029 %9,0; cari açık/GSYH 2026 −%2,6, 2029 −%1,6; ihracat 2026 $282 mlr, 2029 $316 mlr; enerji ithalatı 2026 $71 mlr. 12. Kalkınma Planı 2024–2028 (RG 1.11.2023). 2030 Sanayi ve Teknoloji Stratejisi (Genelge 2025/6, RG 10.5.2025; yüksek teknoloji ihracatında $30 mlr hedefi; HIT-30). Ayrı bir "ihracat ana planı" bulunamadı; hedefler OVP'de. Yeşil Mutabakat Eylem Planı (Genelge 2021/15, RG 16.7.2021). **Yeni teşvik kararı: CK 9903 (RG 30.5.2025)**, 2012/3305 sayılı kararın yerine geçti | SBB; RG |

### 6.6 Başlangıç hipotezleri ve araç setindeki `[D?]` maddeleri

| No | Madde | Durum | Bulgu |
|---|---|---|---|
| H-1 | Giyimde AB EÇM ≈%12 | Doğrulandı | CN 2026: fasıl 61–62'deki 333 satırın 295'i %12, diğerleri %6,3–10,5 |
| H-2 | Revize PEM tekstil kuralları ve toleranslar | Doğrulandı, güncellendi | Karar 1/2023, 1.1.2025'ten beri uygulanıyor. Genel tolerans %10'dan %15'e çıktı (fasıl 50–63 hariç; tekstilde ayrı tolerans). Geri ödemeye (drawback) izin var (50–63 hariç). Tam kümülasyon genelleşti (50–63'te yalnızca ikili). Fasıl 61: örme + konfeksiyon (çift dönüşüm); fasıl 62: dokuma + konfeksiyon **veya** baskıyla öncelenmiş konfeksiyon; düz tek dönüşüm genellikle yok. Fasıl 87: ithal girdi tavanı (MaxNOM) %45; 8708: tarife pozisyonu değişikliği veya MaxNOM %50; fasıl 84–85: pozisyon değişikliği veya MaxNOM %50. **Türkiye revize kuralları AB ile tarım ve AKÇT ticaretinde 1.1.2026'dan beri uyguluyor**. GB kapsamındaki mallarda menşe değil A.TR dolaşım belgesi kullanılıyor |
| H-3 | 15.20'de AB tarifeleri yüksek | Doğrulandı | 6402: %16,8–17; 6403: çoğunlukla %8; 6404: %16,9–17 |
| H-4 | Rus ham petrolünden ürünlere AB kısıtı (19.20) | Güncellendi | D-11'e bakınız |
| H-5 | 26.11–26.12'de ITA kısıtı | Doğrulandı | ITA-I bağlı sıfır oranlar (C-8) |
| H-6 | Otomotivde AB EÇM | Doğrulandı | 8703 %10 (elektrikli dahil). 8704: ≤5 t ve büyük motorlu veya >5 t olanlar %22; küçük motorlu ve elektrikli %10. 8702: %16, elektrikli %10. Ayrıca: lastik 4011 %4,5; buzdolabı 8418 %1,5–2,5; çamaşır makinesi 8450 %2,2–3; TV 8528 72 %14; seramik karo 6907 %5 |
| H-7 | Türkiye GPA'ya taraf değil | Doğrulandı | C-9 |
| H-8 | OECD İhracat Kredileri Uzlaşması'na uyum | Doğrulandı | Türkiye Uzlaşma katılımcısı (Gemi Sektörü Anlaşması hariç) |
| H-9 | Ortak Transit Sözleşmesi ve NCTS üyeliğinin korunması | Doğrulandı | Türkiye 1.12.2012'den beri taraf; Sözleşme GB'den bağımsız (İngiltere de taraf); 39 taraf (Gürcistan 2025, Moldova ve Karadağ 1.11.2025). GB'den çıkış transit rejimini kendiliğinden sona erdirmez |

**Özet:** Toplam 49 madde: doğrulandı 25; güncellendi 15 (çoğu bilgi kesim tarihinden sonraki gelişme); karma (doğrulandı ve güncellendi veya kısmen) 9. Tamamen doğrulanamayan maddeler yok. Doğrulanamayan alt ayrıntılar şunlar: AKÇT Anlaşması'nın fiilî yürürlük tarihi, 1/95 Ek 1'in satır içeriği (VB-06), Türkiye'nin AB çelik kotasının toplamı (VB-08), Brexit'e özgü menşe uyum maliyeti tahmini ve Cumhurbaşkanlığı Kararnamesi No. 9'un antlaşmadan çekilme yetkisi. Basın kaynaklı ayrıntılar ayrıca `[D?]` olarak işaretli.

### 6.7 Faz 0'da ortaya çıkan, strateji için önemli yeni bilgiler

1. **Hurda koruması AKÇT STA'sında.** AB'nin olası hurda kısıtlarına karşı hukuki kalkan GB değil, 1996 AKÇT Anlaşması'nın md. 3–4'üdür. GB'den çıkış bu kalkanı kendiliğinden kaldırmaz; ama AKÇT Anlaşması'na da fesih hükmü yok ve yeni çerçevede bu güvencenin korunması gerekir (müzakere hedefi xii).
2. **Bağlı oranlar bağlayıcı.** DS629 (Temmuz 2026), bağlı satırlarda tarife artışı yapılamayacağını gösteren güncel ve doğrudan bir emsaldir. GB sonrası tarife cetvelinde politika alanı ağırlıkla bağsız satırlarda (sanayide satırların %57'si) olacak.
3. **TR-ETS 2026–27'de SKDM mahsubu üretmiyor.** Pilot dönemde fiyat sinyali yok; AB'nin md. 9 mahsup kuralları da henüz kabul edilmedi. G arketipi için en hızlı kazanım ölçüm-raporlama-doğrulama (MRV) tanınması ve gerçek bir karbon fiyatı takvimi.
4. **ABD 301 ayrımcılığı.** Türkiye'nin AB'ye göre 2,5 puan dezavantajı, GB içindeyken düzeltilemeyen bir asimetri; G1 bindirmesinde temel durum olarak alınacak.
5. **Türkiye–Ukrayna STA'sı 1.10.2026'da yürürlüğe girdi** (tarife hükümleri 1.1.2027'den), İngiltere STA modernizasyonu sürüyor (basın) `[D?]`. Türkiye'nin STA ağı 24 anlaşma `[V]` (Ticaret Bakanlığı).

---

## 7. Netleştirme soruları ve sonuçları

Revizyon 1 ile S-1–S-4 yanıtlandı; S-5 için varsayılan geçerli.

| No | Soru | Sonuç |
|---|---|---|
| S-1 | Siyasi karar "GB'den çıkılacak" olarak mı verildi, yoksa karar açık mı? | **Çıkış yönü veri** (AB'nin hasmane tutumu). S2 ana tasarım; S1 yalnızca maliyet karşılaştırma ölçütü (V-28) |
| S-2 | T tarihi | **İki takvim:** T2028 (1.1.2028) ve T2029 (1.1.2029); duyarlılık T = 1.1.2030 (V-03, §2A) |
| S-3 | Veriler nereden gelecek? | **Çevrim içi kaynaklar** (API ve kazıma); kullanıcı yüklemesi yok (V-29, §4) |
| S-4 | AB üyelik perspektifi | **Yok.** Diplomatik çerçeve "üyelikten bağımsız ekonomik ortaklık"; Ankara Anlaşması ve 1/80 hakları vatandaş hakları olarak korunur (V-27) |
| S-5 | Enflasyon bütçesinin kapsamı | **Varsayılan:** GB paketi + kur ve risk primi kanalı (ayrı blok). Ölçüt TÜFE genel (2025=100). Tamamlayıcı politikalar ayrı raporlanır, bütçeye sayılmaz |

---

## 8. Faz 0 kalite kontrol listesi

| No | Kontrol | Sonuç |
|---|---|---|
| 1 | Her sayıda etiket, birim ve dönem | ✓ Faz 0 sayıları etiketli. Basın kaynaklı rakamlar `[D?]` |
| 2 | NACE toplamlarının makro toplamlarla mutabakatı, çift sayım | ✓ C (€97,55 mlr) + C dışı (€5,74 mlr) = €103,29 mlr ≈ Comext toplamı (€103,31 mlr). Birden çok sınıfa düşen CN satırları eşit paylaştırıldı, çift sayım yok |
| 3 | Enflasyon, mali, istihdam ve kabiliyet kısıtları | Faz 0'da parametre olarak kayda alındı (V-05…V-09); sınama Faz 3 ve 6'da |
| 4 | Tarife önerilerinde bağlı oran, ITA ve STA kontrolü; negatif ERP | Faz 0'da tarife önerisi yok. Bağlama oranları ve ITA statüsü doğrulandı (C-7, C-8) |
| 5 | DTÖ uyumu | Faz 0'da önlem önerisi yok. DS583 ve DS629 emsalleri kayda alındı |
| 6 | "Pazartesi sabahı testi" | Faz 0'da eylem yok. Veri boşlukları için kurum ve süre yazıldı (§4) |
| 7 | AB'nin olası tepkisi ve karşı talepleri | Kayda alındı: IAA karşılıklılık hükmü, md. 58(2) ve 64 yeniden dengeleme araçları, Avrupa Parlamentosu'nun SKDM'de STA muafiyetine karşı tutumu. Modellemesi Faz 2 ve 7'de |
| 8 | Zaman yolu | T ve kapılar tanımlandı (V-03); zaman yolları Faz 3'ten itibaren |
| 9 | `<kacinilacak_hatalar>` | Faz 0'da ilgili olanlar gözetildi: #9 (2025 verisi kullanıldı), #12 (transit ve NCTS doğrulandı), #14 (yasal dayanak ve veto), #15 (İTÜ rejimi ayrıştırıldı), #16 (çelik AKÇT olarak ayrıştırıldı), #17 (ITA ve bağlı oranlar) |
| 10 | Kaçamak ifade | Kontrol edildi; Faz 0'da genel geçer tavsiye yok |
| 11 | Olumsuz bulguların dürüstçe raporlanması | ✓ Literatürün GB→STA için olumsuz sonuçları ve resmî modernizasyon pozisyonu en başta yazıldı (bulgu 2 ve 4) |

---

## 9. Durum özeti

Ayrıca `DURUM_OZETI.md` dosyasında.

**Alınan kararlar.** Araçlı mod seçildi. Analiz birimi NACE Rev. 2 (230 C sınıfı); Rev. 2.1 köprüsü resmî Eurostat tablosundan üretildi. Varsayım kaydı V-01–V-26 olarak kuruldu; nominal T = 1.1.2029 (koşullu), T+60 = 1.1.2034. GB statü etiketleri CN8 düzeyinde, Türkiye'nin AB'ye 2025 ihracatıyla ağırlıklandırılarak atandı: GB 180 (9'u dolaylı), TARIM-1/98 14, KARMA 14, İTÜ 10, AKÇT-STA 2, KAPSAM DIŞI 10. B, D, E, A ve hizmet kapsamı eklendi.

**Temel bulgular.** Türkiye'nin AB'ye ihracatı (€103,4 mlr) %89,3 oranında GB'ye bağlı. Resmî Türk pozisyonu modernizasyon; AB'de yetki yok; Ortaklık Konseyi 2019'dan beri toplanmıyor. Hukuki çıkış kapısı dar: Ankara Anlaşması'nda ve 1/95'te fesih hükmü yok; Türkiye VCLT'ye taraf değil. Veto riskini azaltan yol md. 207 "yalnızca AB" anlaşması. Literatür GB→STA'yı Türkiye için olumsuz buluyor (BKP 2016: −€144 mn refah). Buna karşılık asimetri 2026'da sert biçimde arttı (Mercosur, Hindistan, Meksika, Avustralya) ve ABD 301'de Türkiye AB'den kötü konumda. IAA'daki GB/STA ortağı eşdeğerliği kırmızı çizgi müzakere maddesi. Çelik GB dışında ve 1.7.2026'dan beri kalıcı AB kota rejiminde; hurda koruması AKÇT STA'sında. DS629 bağlı satırlarda tarife artışı alanını kapatıyor; sanayide bağlama oranı %43.

**Kümülatif defter.** Tamamlanan sınıf kartı 0 / 230 (+29 ek kapsam satırı). Kullanılan enflasyon bütçesi 0 / 50 bp birinci tur, 0 / 100 bp toplam. Cari denge katkısı 0. Mali maliyet 0. Riskteki istihdam: hesaplanmadı.

**Açık konular.** Netleştirme soruları S-1–S-5; veri boşlukları VB-01–VB-09 (en kritikleri TÜİK YSHİ, GTİP12 ticareti, 2023 girdi-çıktı tabloları, uygulanan tarife ve İGV cetveli); 1/95 Ek 1 satır içeriği; 2025 cari denge revizyonu.

---

`İLERLEME: Faz 0 tamamlandı (1/10 faz; 0/230 sınıf kartı) — SONRAKİ ADIM: Faz 1 Teşhis: GB'nin 30 yıllık fayda-maliyet bilançosu (Comext 1995–2025, çekim modeliyle 1996 etkisi), mevcut asimetriler, makro tablo ve cari denge ayrıştırması (OVP 2027–29, TCMB ödemeler dengesi)`

**DEVAM** komutunu bekliyorum.

---

## Kaynaklar (Faz 0)

- Eurostat Comext DS-045409 (AB27 × TR, CN8, 2025): https://ec.europa.eu/eurostat/api/comext/dissemination/sdmx/2.1/
- Eurostat NACE_R2 ve NACE_R2_1 kod listeleri: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/codelist/ESTAT/
- EU Vocabularies (ShowVoc): NACE Rev. 2.1–Rev. 2; CPA 2.2–CPA 2.1; CPA 2.2–CN 2025: https://showvoc.op.europa.eu/
- GİB NACE sınıf kodları (2026): https://cdn.gib.gov.tr/
- ECB döviz kurları (EXR): https://data-api.ecb.europa.eu/
- 1/95 sayılı Karar: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:21996D0213(01)
- AKÇT–Türkiye Anlaşması (1996): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:21996A0907(01)
- 1/98 sayılı Karar: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:21998D0320(01); 1/2025: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:22026D1903
- Ankara Anlaşması: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:21964A1229(01)
- VCLT statüsü (UNTC): https://treaties.un.org/Pages/ViewDetailsIII.aspx?src=TREATY&mtdsg_no=XXIII-1&chapter=23&Temp=mtdsg3&clang=_en
- C-81/13: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62013CJ0081; Görüş 2/15: https://curia.europa.eu/jcms/upload/docs/application/pdf/2017-05/cp170052en.pdf
- Genel İşler Konseyi sonuçları, 26.6.2018: https://data.consilium.europa.eu/doc/document/ST-10555-2018-INIT/en/pdf
- Fidan–Kos ortak açıklaması (6.2.2026): https://www.eeas.europa.eu/delegations/t%C3%BCrkiye/joint-statement-turkish-foreign-minister-he-hakan-fidan-and-eu-commissioner-enlargement-he-marta-kos-0_en
- Türkiye Raporu 2025, SWD(2025) 756: https://enlargement.ec.europa.eu/document/download/4bb4ddd1-4f20-4ee0-92db-926996ec8dd1_en
- WTO Tariff Profile Türkiye (2026): https://www.wto.org/english/res_e/statis_e/daily_update_e/tariff_profiles/TR_e.pdf
- WTO DS583: https://www.wto.org/english/tratop_e/dispu_e/cases_e/ds583_e.htm; DS629: https://www.wto.org/english/tratop_e/dispu_e/cases_e/ds629_e.htm
- WTO ITA: https://www.wto.org/english/tratop_e/inftec_e/itscheds_e.htm; GPA gözlemciler: https://www.wto.org/english/tratop_e/gproc_e/memobs_e.htm
- CN 2026, Uyg. Tüzüğü (AB) 2025/1926: https://eur-lex.europa.eu/eli/reg_impl/2025/1926/oj
- PEM menşe ve kümülasyon (DG TAXUD): https://taxation-customs.ec.europa.eu/customs-4/international-affairs/pan-euro-mediterranean-cumulation-and-pem-convention_en
- SKDM mevzuatı (DG TAXUD): https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en
- SKDM mansap genişlemesi ve üçlü görüşmeler (Mayer Brown, 7.10.2026): https://www.mayerbrown.com/en/insights/publications/2026/10/eus-cbam-downstream-extension-and-anti-circumvention-amendments-the-road-to-trilogue
- TR-ETS pilot dönemi (ICAP): https://icapcarbonaction.com/en/node/1238
- AB çelik tüzüğü 2026/1384: https://www.tradecomplianceresourcehub.com/2026/06/26/eu-steel-regulation-published-key-features-application-dates-and-what-to-do-next/
- IAA önerisi (Mayer Brown, 3/2026): https://www.mayerbrown.com/en/insights/publications/2026/03/european-commission-proposes-industrial-accelerator-act
- DG TRADE müzakereler ve anlaşmalar: https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/negotiations-and-agreements_en
- OVP 2027–2029: https://www.sbb.gov.tr/wp-content/uploads/2026/09/Orta-Vadeli-Program-2027-2029.pdf
- Dünya Bankası (2014): https://documents1.worldbank.org/curated/en/298151468308967367/pdf/858300ESW0P1440disclosed090260140TR.pdf
- BKP (2016): https://ec.europa.eu/smart-regulation/impact/ia_carried_out/docs/ia_2016/turkey_anx6_en.pdf
- SWD(2016) 476: https://ec.europa.eu/smart-regulation/impact/ia_carried_out/docs/ia_2016/swd_2016_0476_en.pdf
- OBR Brexit analizi: https://obr.uk/brexit-analysis/
- Ortak Transit Sistemi (Ticaret Bakanlığı): https://trade.gov.tr/multinational-relations/common-transit-system
- OECD İhracat Kredileri Uzlaşması (TAD/PG(2026)2): https://one.oecd.org/document/TAD/PG(2026)2/en/pdf
