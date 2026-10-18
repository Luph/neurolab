# Faz 3 — NACE sınıf kartları, parça 1: 10 Gıda, 11 İçecekler, 12 Tütün ürünleri

**Durum:** Faz 3 / 9, parça 1 / 16 tamamlandı (18 Ekim 2026); DEVAM bekleniyor. Önceki fazlar: [`01_teshis.md`](01_teshis.md), [`02a_politika_uzayi.md`](02a_politika_uzayi.md), [`02b_secenekler_hukuk.md`](02b_secenekler_hukuk.md), [`02c_hazirlik.md`](02c_hazirlik.md). Defter: [`defter.md`](defter.md). Ana matris (230 sınıfın tamamı): [`veri/nace_matris.csv`](veri/nace_matris.csv).

**Bu belge ne yapıyor?**
- 10–12 bölümlerinin 33 sınıfı için ana promptun 15 alanlı kartını dolduruyor.
- Bölümlerin kısa genel görünümünü ve ana matris satırlarını veriyor.
- Kartlara temel olan Faz 3 hesap altyapısını, bütün 230 C sınıfı için bir kez kuruyor. Bu altyapı ticaret, yapı, karmaşıklık, AB tarifesi, senaryolar ve skorları kapsıyor. Sonraki parçalar aynı tabloları kullanacak.
- Kümülatif defteri güncelliyor.

**Takvim gösterimi.** Eylem tablolarında tarihler `T`'ye göre yazılıyor. T2028'de `T` = 1.1.2028, T2029'da `T` = 1.1.2029; örneğin `T−12` T2028'de Ocak 2027'ye, T2029'da Ocak 2028'e denk geliyor. Kanıt etiketleri (`[V]`, `[T]`, `[D?]`, `[H]`) ve güven düzeyleri önceki fazlardaki gibi.

**Ana bulgu: 10–12 GB çıkışından en az etkilenen büyük sanayi grubu, ama üç ince nokta var.**
1. **AB'ye ihracatın dörtte üçü tarım rejiminde (1/98).** Bu ihracat zaten menşe kuralına tabi ve GB'ye bağlı değil.
   - Rota A'da (1/98 sürer) S4'ün getirdiği ortalama AB tarifesi %3,3. Bu oran yalnızca işlenmiş tarım ürünlerinin sanayi bileşeninden ve sigaradan geliyor.
   - 1/98 da kaybedilirse oran %11,5'e çıkıyor.
   - Riskin asıl kaynağı GB değil, hasmane bir AB'nin 1/98'i askıya alması. Bu durumda S4'ün P10 değerlerinde AB'ye ihracat −$2.018 mn, istihdam −4.698 kişi oluyor. Kaybın yarıdan fazlası 10.39'da (kuru meyve, fındık, işlenmiş sebze).
2. **İşlenmiş tarım ürünlerinde (İTÜ) S4'ün maliyeti sanayi bileşeni kadar.** Tarım bileşeni bugün de ödeniyor.
   - Sanayi bileşeni: bisküvi ve ekmek %9; çikolata %8,4; makarna %7,7; glikoz %14; gıda müstahzarları %12,8; sigara %57,6.
   - En büyük mutlak kayıplar: bisküvi, gıda müstahzarları, glikoz ve sigara.
3. **S2'de menşe kuralı tarifeden daha bağlayıcı olabilir.** Bisküvi ve ekmek ihracatçıları Dahilde İşleme Rejimi (DİR) ile ithal (çoğunlukla Rus) buğday kullanıyor. PEM'in Fasıl 11–19 kuralları ise unun menşeli olmasını istiyor.
   - Bisküvide S2'nin kaybı (−$35 mn AB ihracatı) S4'ünkinin (−$51 mn) üçte ikisinden fazla.
   - Çözüm tarifede değil, DİR'deki "eşdeğer eşya" mekanizmasında ve ürüne özgü menşe kuralı (PSR) müzakeresinde (E-10-02).

**Olumsuz bulgular (dürüst rapor).**
- Sigarada (12.00) S2'de bile kayıp büyük. Kural "tütünün %70'i menşeli" diyor ve Amerikan harmanı bunu karşılamıyor. AB'ye yönelik üretim büyük olasılıkla AB fabrikalarına kayar.
- Fındık ve kuru meyvede Türkiye dünya ihracatının %30–75'ini yapıyor. Bu, AB'ye karşı bir müzakere kaldıracı. Ama 1/98 kaybında bile fındık içinin AB MFN'si yalnızca %3,2. Kaldıraç tarife tehdidinden değil, arz güvenliğinden geliyor.

## 0. Faz 3 yöntemi (bütün parçalar için)

**Tablo 0.1 — Faz 3 hesap zinciri**

| Betik | Ne üretiyor | Ana kaynak | Etiket |
|---|---|---|---|
| `kod/f3a_ticaret.py` | Sınıf düzeyi ihracat, ithalat, AB ve Çin payları, RCA (dünya ve AB pazarı), AB pazar payı, birim değer, ilk 5 pazar/kaynak/rakip | BACI HS17 2020 ve 2024 (TR ikili; AB27 ithalatı; dünya ihracatı) | `[V]` veri, `[T]` eşleme |
| `kod/f3b_yapi.py` | Üretim, KD, istihdam, ölçek dağılımı, İBBS-2 bölge payları, AB'ye göre verimlilik | TÜİK YSHİ 2024, İş Kayıtları 2024, SGK 2025, Eurostat SBS 2023 | `[V]`; bölge ve gizli hücre `[T]` |
| `kod/f3c_karmasiklik.py` | PCI, ECI, ürün uzayı yoğunluğu, karmaşıklık kazancı, atlanabilir ürünler | BACI 2024 ihracatçı × HS6 (157 ülke, 4.858 ürün) | `[T]` |
| `kod/f3d_ab_tarife.py` | KN8 düzeyinde AB MFN'si, spesifik vergilerin ad valorem eşdeğeri, rejime göre S4 artışı, tepe satırlar, EUDR/SKDM payları | AB KN 2026, Comext 2025 (değer ve miktar) | `[V]`; AVE `[T]` |
| `kod/f3e_senaryo.py` | S2/S3/S4 sınıf etkileri (P10–P50–P90), EDE, CKE | f3a–f3d, I-O 2023, ProTEE esneklikleri, Faz 2B GE | `[T]` |
| `kod/f3f_skor_matris.py` | KS, SS, AME, EDE ve CKE puanları, arketip, duruş, ağırlık duyarlılığı, `veri/nace_matris.csv` | f3a–f3e, `veri/f3_ss_boyutlar.csv` | `[T]`; SS `[H]` |
| `kod/f3g_kartlar.py` | Bu belge (kartların sayısal alanları; nitel alanlar `kartlar/10-12*.yaml`) | — | — |

**Ölçümün beş kuralı.**
1. **Senaryolar genel dengeye bağlı.** Her Monte Carlo çekilişinde (N = 2.000) AB'ye toplam ihracat ve ithalat değişimi Faz 2B'nin genel denge dağılımından alınıyor. S4: −%18,9 (GA90 −32/−5); S2: −%11,1 (−27/+6). Kısmi denge modeli (`ΔX = X[(1+τ_etkin)^(−σ) − 1]`) yalnızca bu toplamı sınıflara dağıtıyor; S3 iki senaryonun kısmi denge yapısıyla ara değer alıyor. Kalibrasyon ölçeği S2'de 0,65, S4'te 0,54: ürün düzeyi esnekliklerle kısmi denge, genel dengenin yaklaşık iki katı kayıp üretiyor (`V-30`).
2. **Esneklikler ürün düzeyinde.** CEPII ProTEE (Fontagné, Guimbard ve Orefice 2022) HS6 esneklikleri sınıf içinde AB ihracatıyla ağırlıklandırılıp [2, 15] aralığına kırpıldı; medyan 7,8 (`V-32`).
3. **Tarife rejime göre ayrıştırılıyor.** S4'te GB satırına tam MFN, İTÜ satırına yalnızca sanayi bileşeni ekleniyor; tarım satırı (1/98) değişmiyor. Hasmane AB varsayımıyla (`V-11`) S4'te 1/98'in askıya alınma olasılığı 0,25 (`V-31`). 1/98 kaybı genel denge toplamına ekleniyor, yeniden dağıtılmıyor.
4. **Sürtünme ve menşe ayrı kalemler.** Sınır sürtünmesi %0,5–2 ve yalnızca GB ve İTÜ satırlarına uygulanıyor; S2'de AEO karşılıklı tanıma ve tek pencereyle yarıya iniyor (`V-33`). Menşe maliyeti `c_RoO` ve uyum olasılığı `p_uyum` sınıf varsayım tablosundan geliyor (`veri/f3_sinif_varsayim.csv`, `[H]`). Tarım satırları 1/98'de bugün de menşe kuralına tabi olduğundan onlara ek menşe maliyeti eklenmiyor.
5. **TÜFE etkisi birinci tur ve I-O ile tutarlı.** Doğrudan kanal: COICOP 2018 sepetinden sınıfa eşlenen ağırlık × tüketimdeki ithal pay. Dolaylı kanal: I-O 2023 Leontief fiyat modeli (`kod/f2a_io_fiyat.py`). 230 sınıfın EDE toplamı 22,0 bp; I-O ürün toplamı 23,5 bp. S4'te AB'ye uygulanacak c2 tarifesinin imalat toplamı birinci turda 69 bp (Faz 2A'daki 73 bp ile tutarlı).

**Skorlar.**
- KS'nin yedi bileşeni, ağırlıkları ana prompttaki gibi, C sınıfları içinde yüzdelik sıraya çevrildi. Ar-Ge bileşeni OECD sınıflamasından geliyor (Türkiye'ye özgü sınıf düzeyi Ar-Ge verisi yok: VB-31).
- Ağırlık duyarlılığı: varsayılan sıranın Spearman korelasyonu eşit ağırlıkta 0,93, ticaret ağırlıklı setle 0,92, yapı ağırlıklı setle 0,75; Dirichlet çekilişlerinin P10'unda 0,71. Sıralama ticaret ağırlıklarına karşı sağlam, yapısal ağırlıklara karşı orta derecede sağlam. Kartlarda her sınıfın sıra aralığı (P10–P90) veriliyor.
- SS yedi boyutta, elle ve gerekçeli puanlandı `[H]`. SS = 0,7 × en yüksek boyut + 0,3 × ağırlıklı ortalama.
- AME = AB ihracat payı × (beklenen `τ_AB` + `c_RoO` + sınır sürtünmesi) × değer zinciri çarpanı. Beklenen τ, 1/98 kaybını 0,25 olasılıkla içeriyor.
- CKE: STA dışı ithalata 1 puanlık tarifenin ya da iç satışa %1 üretim desteğinin 5 yıllık net cari denge getirisi. Getiri, sırasıyla TÜFE baz puanına ve mali maliyete bölünüyor; kapasite yatırımının ithalatı ve ithal girdi düşülüyor (`V-36`).
- Arketip ve duruş önce kurala göre atanıyor (`V-34`), sonra kartta uzman muhakemesiyle düzeltiliyor. Düzeltmeler `veri/nace_matris.csv`'nin `uzman_duzeltmesi` sütununda.

**Düzeltme notu (Faz 0–2 sınıf tabloları).** Faz 3 hesapları iki veri hatası buldu.
- **D-1. KN8 → NACE ağırlıkları.** `veri/cn2025_nace_rejim.csv` yazılırken birden çok sınıfa düşen 1.251 KN8 satırının ağırlığı tam sayıya yuvarlanmış ve sıfır görünüyordu. Bu satırlar TR→AB ihracatının %12,8'ini oluşturuyor.
  - Faz 0–2'nin toplamları doğru: değerler eşit paylaştırılmış olarak zaten yazılıydı.
  - Sınıf dağılımı ise bazı sınıflarda yanlış. Örnek: hibrit otomobil satırları (CPA 2.2 29.10.23) 29.10 ile 27.11 arasında eşit bölünmüştü. Faz 3 eşlemesiyle 29.32'nin AB ihracatı €2,1 mlr'dan €5,6 mlr'a, 29.10'unki €16,6 mlr'dan €18,7 mlr'a çıkıyor; 27.11 (€3,3 → €1,3 mlr) ve 28.25 (€2,9 → €1,3 mlr) düşüyor.
  - Faz 3'te CPA 2.2 kodunun CPA 2.1'de aynen sürdüğü bağlantıya öncelik veriliyor (`agirlik_f3`, `V-37`); eşleşmeyen ticaret %6,0'dan %0,3'e iniyor.
  - Faz 0–2'deki sınıf düzeyi tablolar (`nace_kapsam.csv` ihracat sütunu, `s4_tarife_duvari_sinif.csv`, `politika_s4_net_istihdam_sinif.csv`) bu sınıflar için Faz 3 kartlarıyla geçersiz kalıyor. Sınıf düzeyi Faz 2 sayılarının Faz 3 yöntemiyle yeniden hesaplanmış hâli matriste.
- **D-2. Kıbrıs akımları.** BACI'deki TR→Kıbrıs ihracatı ($1,6 mlr, 2024; %31'i akaryakıt) büyük ölçüde KKTC ticareti ve AB gümrük bölgesi dışında (Protokol 10).
  - Faz 3'te bu akımlar AB dışı sayılıyor ve AB pazarı verisinden düşülüyor. Etki: imalatın AB'ye ihracatının %1,4'ü; bazı küçük gıda sınıflarında AB payı belirgin düşüyor.
  - Faz 1–2'de AB tarafı maruziyet Comext'ten hesaplandığı için etkilenmiyor. Yalnız BACI'ye dayanan Türkiye ithalatı AB payları (EDE) çok az yüksek kalmış.
- **D-3. Faz 2'deki "kaybı %5'i aşan 21 sınıf"** σ = 5 ile, kalibrasyonsuz kısmi dengeden geliyordu. Faz 3'te genel denge kalibrasyonu ve iç ikameyle S4'te kaybı %5'i aşan sınıf sayısı P50'de 9, P10'da 15 (`veri/f3_senaryo_ozet.csv`).

**Tablo 1.1 — Bölümlerin genel görünümü (2024; senaryolar T+5)**

| Bölüm | Sınıf | Çalışan | KD ($ mn) | İhracat ($ mn) | AB payı | İthalat ($ mn) | Denge | S2 cari P50 | S4 cari P50 | S4 istihdam P50 | S4 istihdam P10 | S4 TÜFE P50 (bp) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10 Gıda ürünleri | 25 | 610.282 | 21.311 | 22.655 | %26 | 11.186 | +11.469 | −32 | +3 | −89 | −4.693 | 2,6 |
| 11 İçecekler | 7 | 19.525 | 1.331 | 539 | %30 | 1.242 | −704 | +3 | +16 | +54 | 0 | 0,9 |
| 12 Tütün ürünleri | 1 | 5.769 | 656 | 876 | %13 | 958 | −81 | −15 | +11 | +20 | −5 | 2,7 |

*Kaynak:* `[V]` TÜİK YSHİ, BACI; senaryolar `[T]` (f3e). Cari denge ve TÜFE etkileri sınıf toplamıdır; makro kanallar (kur, talep) Faz 6'da.


## 1. Genel görünüm

**10 Gıda ürünleri (25 sınıf).**
- İmalat istihdamının %12'si (610 bin), AB'ye imalat ihracatının yalnızca %5,6'sı. AB'ye ihracatın büyük kısmı tarım rejiminde (1/98): kuru meyve ve fındık, su ürünleri, meyve suyu, bitkisel yağ.
- Türkiye birçok üründe dünya ihracatında ilk sırada (BACI 2024) `[V]`:
  - buğday unu (%19,6), fındık içi (%62), kuru kayısı (%75), kuru incir (%50), kuru üzüm (%30);
  - levrek (%32), rafine ayçiçek yağı (%19), bulgur (%75), fruktoz (%35);
  - makarna ve çipurada ikinci.
- Bu ihracatın çoğu AB dışına gidiyor: un ve makarnada Irak, Somali, Gana; kanatlıda Irak.
- Bölümün GB'ye bağlı tek parçası İTÜ: bisküvi, çikolata ve şekerleme, glikoz, gıda müstahzarları. AB'ye €1,1 mlr civarında ihracat ve S4'te %7–16 sanayi bileşeni.

**11 İçecekler (7 sınıf).**
- AB'nin alkollü içki ve birada MFN'si sıfır ya da çok düşük, bu yüzden çıkışın AB tarafı etkisi küçük.
- Alkolsüz içeceklerde (11.07) AB ihracatı $111 mn ve S4 tarifesi %6,6. İthalatta enerji içecekleri öne çıkıyor (Avusturya %42).
- 11.05'in ithalatı ($348 mn) aslında bira değil, ABD'den damıtma artığı yem (KN 2303 30): sınıflandırma CPA 11.05.20'ye bağlı.
- ÖTV ile gümrük etkileşimi: alkollü içki ve kolada ÖTV maktu ya da yüksek oranlı. S4'te AB'ye MFN, ithal ürünün ÖTV öncesi fiyatına eklenir, ama TÜFE etkisi küçük (11 için 0,9 bp).

**12 Tütün ürünleri (1 sınıf).**
- Çok uluslu üretim üssü (PMI ve JTI İzmir; PMI Torbalı 2024'te üretiminin %11'inden fazlasını ihraç etti) `[V]`.
- AB'ye ihracat $116 mn ve sigarada AB MFN'si %57,6: S4'te AB pazarı fiilen kapanır.
- S2'de menşe kuralı (%70 menşeli yaprak) Amerikan harmanını dışarıda bırakıyor.
- İthalatın %48'i AB'den. Isıtılmış tütün ve sigara Almanya, Hollanda ve Belçika'dan geliyor. S4'te c2 tarifesi TÜFE'ye 2,7 bp ekliyor; bölümün S4 TÜFE etkisinin %44'ü bu.

## 2. Ana matris satırları

Matrisin bütün sütunları ve 230 sınıfın tamamı `veri/nace_matris.csv`'de. Aşağıdaki iki tablo ana promptun matris sütunlarını 10–12 için gösteriyor.

**Tablo 2.1a — Ana matris: kimlik, ticaret, maruziyet**

| Kod | Ad | GB | KD | İstihdam | İhracat | AB payı | İthalat | AB ith. payı | τ_AB (S4) | Menşe S2/S3 | İthal girdi | RCA | PCI |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10.11 | Etin işlenmesi ve saklanması (kümes ha | KARMA | 804 | 10.835 | 146 | %46 | 1.011 | %64 | %0,0 | D/D | %20 | 0,09 | −0,89 |
| 10.12 | Kümes hayvanları etlerinin işlenmesi v | TARIM-1/98 | 2.136 | 35.710 | 643 | %0 | 86 | %9 | %0,0 | D/D | %20 | 1,45 | −0,89 |
| 10.13 | Et ve kümes hayvanları etlerinden üret | TARIM-1/98 | 379 | 11.726 | 214 | %2 | 64 | %56 | %0,0 | D/D | %20 | 0,49 | 0,17 |
| 10.20 | Balık, kabuklu deniz hayvanları ve yum | TARIM-1/98 | 722 | 14.445 | 1.237 | %40 | 514 | %7 | %0,0 | D/D | %20 | 0,75 | −0,97 |
| 10.31 | Patatesin işlenmesi ve saklanması | KARMA | 107 | 2.152 | 110 | %3 | 22 | %85 | %0,0 | D/D | %20 | 0,49 | 0,42 |
| 10.32 | Sebze ve meyve suyu imalatı | TARIM-1/98 | 415 | 7.460 | 770 | %27 | 144 | %6 | %0,0 | D/D | %20 | 3,21 | −0,84 |
| 10.39 | Meyve ve sebzelerin diğer şekillerde i | TARIM-1/98 | 2.174 | 66.354 | 6.472 | %56 | 1.177 | %8 | %0,0 | D/D | %20 | 5,05 | −1,03 |
| 10.41 | Sıvı ve katı yağ imalatı | TARIM-1/98 | 910 | 17.859 | 3.183 | %9 | 3.711 | %2 | %0,0 | D/O | %20 | 1,53 | −1,10 |
| 10.42 | Margarin ve benzeri yenilebilir katı y | TARIM-1/98 | 71 | 773 | 165 | %7 | 79 | %39 | %0,0 | O/O | %20 | 1,62 | −0,58 |
| 10.51 | Süthane işletmelerinin faaliyetleri ve | TARIM-1/98 | 1.987 | 48.749 | 440 | %6 | 112 | %46 | %0,2 | D/D | %20 | 0,35 | 0,15 |
| 10.52 | Dondurma imalatı | İTÜ | 489 | 7.589 | 72 | %1 | 5 | %54 | %8,4 | D/O | %20 | 0,99 | −0,13 |
| 10.61 | Öğütülmüş hububat ve sebze ürünleri im | KARMA | 1.245 | 26.004 | 1.870 | %7 | 739 | %17 | %4,9 | O/O | %20 | 2,40 | −1,18 |
| 10.62 | Nişasta ve nişastalı ürünlerin imalatı | KARMA | 357 | 3.117 | 528 | %18 | 206 | %68 | %14,2 | D/O | %20 | 1,84 | 0,05 |
| 10.71 | Ekmek, taze pastane ürünleri ve taze k | İTÜ | 2.097 | 189.869 | 264 | %19 | 29 | %61 | %9,0 | O/O | %20 | 1,45 | −0,18 |
| 10.72 | Peksimet ve bisküvi imalatı; dayanıklı | İTÜ | 1.548 | 42.160 | 1.174 | %14 | 89 | %75 | %9,0 | O/O | %20 | 3,10 | −0,49 |
| 10.73 | Makarna, şehriye, kuskus ve benzeri un | İTÜ | 409 | 7.040 | 852 | %2 | 17 | %86 | %7,7 | D/D | %20 | 9,09 | −1,59 |
| 10.81 | Şeker imalatı | TARIM-1/98 | 803 | 15.900 | 143 | %10 | 458 | %10 | %0,0 | D/D | %20 | 0,27 | −0,94 |
| 10.82 | Kakao, çikolata ve şekerleme imalatı | İTÜ | 1.645 | 36.835 | 2.032 | %14 | 963 | %73 | %8,4 | O/O | %20 | 1,97 | −0,27 |
| 10.83 | Kahve ve çayın işlenmesi | KARMA | 1.042 | 19.999 | 170 | %23 | 364 | %60 | %3,2 | D/D | %20 | 0,44 | −0,76 |
| 10.84 | Baharat, sos, sirke ve diğer çeşni mad | KARMA | 296 | 7.151 | 242 | %34 | 90 | %40 | %4,9 | D/D | %20 | 0,78 | −0,92 |
| 10.85 | Hazır yemeklerin imalatı | İTÜ | 221 | 10.010 | 100 | %10 | 2 | %65 | %7,0 | O/O | %20 | 1,00 | −1,08 |
| 10.86 | Homojenize gıda müstahzarları ve diyet | KARMA | 61 | 1.321 | 214 | %20 | 173 | %91 | %7,7 | O/O | %20 | 0,80 | −0,17 |
| 10.89 | Başka yerde sınıflandırılmamış diğer g | İTÜ | 467 | 10.858 | 1.114 | %24 | 639 | %62 | %11,8 | D/O | %20 | 0,99 | −0,13 |
| 10.91 | Çiftlik hayvanları için hazır yem imal | TARIM-1/98 | 846 | 14.598 | 352 | %1 | 279 | %50 | %0,0 | D/D | %20 | 1,40 | −0,76 |
| 10.92 | Ev hayvanları için hazır gıda imalatı | TARIM-1/98 | 81 | 1.768 | 147 | %14 | 214 | %87 | %0,0 | D/D | %20 | 0,49 | 0,03 |
| 11.01 | Alkollü içeceklerin damıtılması, arıtı | İTÜ | 393 | 2.398 | 68 | %48 | 425 | %25 | %0,0 | D/D | %20 | 0,14 | −0,36 |
| 11.02 | Üzümden şarap imalatı | TARIM-1/98 | 109 | 1.968 | 24 | %61 | 53 | %86 | %0,0 | D/D | %20 | 0,05 | −0,56 |
| 11.03 | Elma şarabı ve diğer meyve şaraplarını | TARIM-1/98 | — | — | 0 | %10 | 1 | %47 | %0,0 | D/D | %20 | 0,01 | 0,07 |
| 11.04 | Diğer damıtılmamış fermente içecekleri | İTÜ | — | — | 0 | %15 | 2 | %100 | %0,0 | D/D | %20 | 0,01 | −0,42 |
| 11.05 | Bira imalatı | İTÜ | 65 | 394 | 61 | %8 | 348 | %10 | %0,0 | D/D | %20 | 0,23 | −0,64 |
| 11.06 | Malt imalatı | TARIM-1/98 | — | — | 0 | %2 | 83 | %86 | %0,0 | D/D | %20 | 0,01 | 0,16 |
| 11.07 | Alkolsüz içeceklerin imalatı; maden su | KARMA | 764 | 14.765 | 385 | %29 | 330 | %78 | %6,6 | D/O | %20 | 0,93 | −0,64 |
| 12.00 | Tütün ürünleri imalatı | KARMA | 656 | 5.769 | 876 | %13 | 958 | %48 | %51,3 | Y/Y | %20 | 1,52 | −1,08 |

*Kaynak:* `veri/nace_matris.csv`. KD, ihracat, ithalat $ mn (2024). τ_AB: S4'te eklenen AB tarifesi (rota A).


**Tablo 2.1b — Ana matris: skorlar, strateji, senaryo**

| Kod | KS | SS | AME | EDE | CKE | Arketip | Duruş | Tarife yolu | Ana araçlar | AB müz. | S2 cari P50 | S2 TÜFE P50 | İstihdam riski | Güven |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10.11 | 41 | 53 | 17 | 0,46 | 34 | — | Koru | Değişiklik yok (tarım ürünü; 1/98) | ESK ithalat kaynağı çeşitlendirme; SPS; EUDR (sığır izlenebilirliği) | nötr | +0,2 | 0,01 | Düşük | Yüksek |
| 10.12 | 46 | 60 | 11 | 0,05 | 25 | B/D | Geliştir | Değişiklik yok (tarım); yem girdilerinde mevcut rejim | Pazar çeşitlendirme; AB SPS listelenme talebi; yem arz güvenliği | hücum | +0,1 | 0,00 | Düşük | Yüksek |
| 10.13 | 54 | 30 | 18 | 0,05 | 16 | — | Koru | Değişiklik yok (tarım) | İzleme | nötr | 0,0 | 0,00 | Düşük | Yüksek |
| 10.20 | 47 | 38 | 62 | 0,05 | 42 | A | Koru | 1/98 balıkçılık tavizleri korunur; S2'de kota yerine %0 | 1/98 sürekliliği (E-10-01); ticaret savunması hazırlığı (E-10-04); yem ve yavru arzı | hücum | 0,0 | 0,00 | Orta | Yüksek |
| 10.31 | 50 | 22 | 13 | 0,01 | 33 | — | Koru | Değişiklik yok | İzleme | nötr | 0,0 | 0,00 | Düşük | Yüksek |
| 10.32 | 52 | 15 | 62 | 0,02 | 32 | B/A | Geliştir | Değişiklik yok (tarım; 1/98) | 1/98 sürekliliği (E-10-01); AB dışı pazar; giriş fiyatı istisnası (E-10-06) | hücum | 0,0 | 0,00 | Orta | Yüksek |
| 10.39 | 50 | 37 | 54 | 0,12 | 51 | A | Koru | 1/98 korunur; S2'de tavizler ve giriş fiyatı istisnası; TR tarifesi değişmez | 1/98 sürekliliği (E-10-01); arz güvenliği kaldıracı (fındık); SPS kontrol sıklığının azaltılması | hücum | −0,4 | 0,00 | Orta | Yüksek |
| 10.41 | 46 | 63 | 18 | 0,39 | 63 | D/B | Geliştir | Tarım tarifeleri değişmez; DİR sürer | Yağlı tohum üretimi; stratejik ham yağ stoku; kaynak çeşitlendirme | nötr | −0,1 | 0,00 | Düşük | Orta |
| 10.42 | 42 | 30 | 17 | 0,01 | 26 | B | Geliştir | Değişiklik yok | Pazar çeşitlendirme | nötr | 0,0 | 0,00 | Düşük | Orta |
| 10.51 | 46 | 57 | 19 | 0,14 | 12 | — | Koru | Değişiklik yok (tarım) | İzleme; S2'de süt ürünleri SPS listelenmesi | nötr | 0,0 | 0,00 | Düşük | Orta |
| 10.52 | 52 | 4 | 15 | 0,00 | 15 | — | Koru | Değişiklik yok | İzleme | nötr | 0,0 | 0,00 | Düşük | Orta |
| 10.61 | 48 | 71 | 27 | 0,11 | 37 | B/D | Geliştir | Tarım tarifeleri değişmez; İTÜ satırlarında (bulgur, karışımlar) AB'de S4'te %4,9 | Buğday arz güvenliği (TMO stoku, kaynak çeşitlendirme); DİR eşdeğer eşya (E-10-02); Afrika ve Körfez STA'ları | nötr | −6,5 | 0,00 | Düşük | Yüksek |
| 10.62 | 53 | 30 | 84 | 0,02 | 50 | B | Geliştir | Değişiklik yok; S2'de AB'ye %0 (İTÜ sanayi bileşeni) | S2'de İTÜ sanayi bileşeninin sıfırı; nişasta bazlı şeker kotası; mısır arzı | savunma | −4,2 | 0,01 | Düşük | Yüksek |
| 10.71 | 56 | 67 | 72 | 0,05 | 13 | —/D | Koru | Değişiklik yok | Buğday ve un arz güvenliği; menşe uyumlu DİR (E-10-02) | savunma | −5,2 | 0,04 | Düşük | Orta |
| 10.72 | 55 | 22 | 63 | 0,03 | 25 | B | Geliştir | Değişiklik yok; S2'de AB'ye %0 | Menşe uyumlu DİR (E-10-02); Fasıl 19 PSR toleransı; S4 tamponu (E-10-05) | savunma | −16,3 | 0,03 | Düşük | Yüksek |
| 10.73 | 42 | 52 | 16 | 0,01 | 20 | B/D | Geliştir | Değişiklik yok | Afrika, Latin Amerika ve Japonya STA'ları; makarnalık buğday arzı | nötr | −0,4 | 0,01 | Düşük | Orta |
| 10.81 | 34 | 53 | 10 | 0,09 | 20 | — | Koru | Değişiklik yok (tarım; kota rejimi) | İzleme; S2'de şeker hassas listesi | savunma | 0,0 | 0,00 | Düşük | Yüksek |
| 10.82 | 56 | 7 | 57 | 0,11 | 57 | B/G | Geliştir | Kakao ara ürünlerinde (1803–1805) MFN %0, tüm menşeler; nihai üründe MFN korunur | Girdide sıfır (kakao); EUDR uyumu (E-10-03); menşe uyumlu DİR (şeker) | savunma | +2,7 | 0,11 | Düşük | Yüksek |
| 10.83 | 44 | 22 | 39 | 0,18 | 25 | — | Koru | Değişiklik yok | EUDR (kahve; E-10-03); izleme | nötr | +2,8 | 0,08 | Düşük | Yüksek |
| 10.84 | 42 | 22 | 73 | 0,02 | 30 | A | Geliştir | S2'de AB'ye %0 (İTÜ); baharatta 1/98 | S2'de İTÜ sıfırı; SPS kontrol sıklığı (2019/1793); izleme | savunma | −2,1 | 0,01 | Düşük | Yüksek |
| 10.85 | 38 | 24 | 41 | 0,01 | 8 | — | Koru | Değişiklik yok | İzleme; afet ve askerî tayın tedariki | nötr | −0,3 | 0,01 | Düşük | Yüksek |
| 10.86 | 50 | 55 | 69 | 0,02 | 72 | D/C | Geliştir | S4'te bebek mamasında (1901 10) MFN %0, tüm menşeler; diğerlerinde MFN | S4'te 1901 10 MFN %0; yatırım teşviki (bebek maması tesisi); stok izleme | nötr | +1,0 | 0,03 | Düşük | Yüksek |
| 10.89 | 53 | 38 | 86 | 0,05 | 36 | A/C | Geliştir | S2'de AB'ye %0; S4'te 2106 90'da AB'ye MFN (c2), TÜFE izlenir | S2'de İTÜ sıfırı; maya ihracatında pazar çeşitlendirme; S4 tamponu (E-10-05) | savunma | −3,6 | 0,08 | Düşük | Yüksek |
| 10.91 | 49 | 63 | 12 | 0,02 | 30 | D/B | Geliştir | Tarım tarifeleri değişmez | Soya küspesi ve mısır kaynak çeşitlendirme; EUDR (soya); stok | nötr | 0,0 | 0,00 | Düşük | Yüksek |
| 10.92 | 48 | 4 | 15 | 0,04 | 41 | C | Geliştir | Değişiklik yok (tarım) | Yatırım teşviki (yerlileştirme); izleme | nötr | 0,0 | 0,00 | Düşük | Yüksek |
| 11.01 | 41 | 0 | 45 | 0,08 | 23 | — | Koru | Değişiklik yok (AB MFN ≈ %0) | Coğrafi işaret (Türk Rakısı) korunması; izleme | hücum | +0,1 | 0,02 | Düşük | Düşük |
| 11.02 | 50 | 0 | 13 | 0,01 | 33 | — | Koru | Değişiklik yok | İzleme | nötr | 0,0 | 0,00 | Düşük | Yüksek |
| 11.03 | 42 | 0 | 11 | 0,00 | 3 | — | Koru | Değişiklik yok | İzleme | nötr | 0,0 | 0,00 | Düşük | Düşük |
| 11.04 | 43 | 0 | 20 | 0,00 | — | — | Koru | Değişiklik yok | İzleme | nötr | 0,0 | 0,00 | Düşük | Düşük |
| 11.05 | 42 | 0 | 16 | 0,08 | 33 | — | Koru | Değişiklik yok (AB MFN %0) | İzleme | nötr | 0,0 | 0,01 | Düşük | Orta |
| 11.06 | 44 | 15 | 12 | 0,01 | 3 | — | Koru | Değişiklik yok (tarım) | İzleme | nötr | 0,0 | 0,00 | Düşük | Düşük |
| 11.07 | 41 | 30 | 74 | 0,13 | 29 | — | Koru | S2'de AB'ye %0; S4'te AB'ye c2 (%8,6) | İzleme; S4'te enerji içeceklerinde TÜFE izleme | savunma | +2,9 | 0,14 | Düşük | Düşük |
| 12.00 | 40 | 0 | 98 | 0,31 | 26 | B | Koru | Tütün ürünlerinde MFN korunur; S4'te ısıtılmış tütünde MFN %0 | AB dışı pazar; S2'de PSR talebi (%50 menşeli yaprak); S4'te ısıtılmış tütünde MFN %0 | savunma | −14,7 | 0,29 | Düşük | Yüksek |

*Kaynak:* Skorlar 0–100 (C sınıfları içinde yüzdelik); EDE bp/puan; S2 cari $ mn; TÜFE bp. Arketip ve duruş kural tabanlı öneri, uzman düzeltmesiyle (kartlar).


## 3. Sınıf kartları

Her kartta sayısal alanlar veriden, nitel alanlar `kartlar/10-12_siniflar.yaml`'dan geliyor. Bölümler arası ortak eylemler (E-10-01 … E-10-06) §4'te; kartlar bunlara atıf yapıyor. Senaryo tablolarındaki değerler T+5'teki yıllık etki (P50, parantez içinde P10 / P90).

### 3.1 10.11 Etin işlenmesi ve saklanması (kümes hayvanları eti hariç) — GB statüsü: KARMA | Birincil/ikincil arketip: — | Duruş: Koru

*İç pazar ve tarım politikası sınıfı; GB çıkışı doğrudan etkilemiyor. AB'den et ithalatı (%64) 1/98'e bağlı.*

**1. Kimlik.** Rev. 2.1: 10.11 (1:1); CPA 10.11. Başlıca HS4 (TR ihracatı 2024): 0504 %48, 0202 %13, 0511 %12, 4102 %9. BEC payları (ticaret ağırlıklı): ara %28 / sermaye %0 / tüketim %72.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $4.069 mn; $804 mn (GSYH'nin %0,06) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 10.835; 608 (57 / 410 / 144 / 37 / 5) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %23; 1,41 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | Kocaeli, Sakarya, Düzce, Bolu, Yalova %34; Balıkesir, Çanakkale %6; Konya, Karaman %6 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Namet, Pınar Et, Bonfilet ve ESK (Et ve Süt Kurumu; kamu ithalatı). Yabancı çapa yok | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $146 mn; %26 |
| AB payı; ilk 5 AB pazarı | %46; ITA %21; DEU %19; FRA %16; NLD %10; DNK %6 |
| İlk 5 AB dışı pazar | VNM %36; HKG %10; USA %10; LBR %4; CIV %4 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $1.011 mn; AB %64, Çin %0; POL %30; BRA %24; FRA %15; BGR %8; ITA %7 |
| Dış ticaret dengesi | $−865 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %20 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,09 → 0,09 / 0,28 |
| Birim değer ÷ AB pazarı ortalaması | 2,03 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,8 → %1,1; 14. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %0,3; tam MFN ortalaması %0,3. Rejim: GB %20, İTÜ %0, tarım %80 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): GBR %27; NZL %13; ARG %11; BRA %10; CHN %9. Tercihli rakip payı %51.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: Fasıl 2: Fasıl 1–2 malzemeleri tamamen elde edilmiş; ithal canlı hayvandan et menşe kazanmaz (1/98 rejiminde bugün de geçerli).
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.
- AB'ye ihracat ($68 mn) bağırsak, tuzlanmış deri artıkları ve yağ gibi yan ürünler; et ihracatı SPS izni olmadığı için sınırlı `[H]`.
- AB'den ithalat ($651 mn; Polonya, Fransa) ESK'nın fiyat istikrarı alımları. 1/98'deki Türk tavizleri kalkarsa bu ithalat MFN'ye (et %40–225) döner; bu da TÜFE riski (E-10-01).

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %96,7, İGV dahil %96,7 `[V]`. S4'te AB menşeline (c2): %0,0.
- Kritik girdiler (HS4 0102, 0201, 0202), Türkiye'nin toplam ithalatı 2024: $1.745 mn (AB %58; BRA %28, POL %18, BGR %13) `[V]`.
- Canlı hayvan ve et ithalatı TARIM rejiminde. GB çıkışı Türkiye'nin et tarifesini değiştirmiyor.

**6. Kabiliyet**

- KS 40,7 (sıra 202/230; ağırlık duyarlılığında P10–P90 130–220). Bileşenler: RCA 12, PCI 13 (PCI −0,89), yurt içi KD 52, Ar-Ge 25, tedarikçi 84, verimlilik 98, firma 59 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): 020120 (PCI +0.14, RCA 0.00); 020110 (PCI -0.07, RCA 0.00); 410210 (PCI -0.88, RCA 0.35) `[T]`.
- **Kırmızı çizgi yetkinlikleri:** Kesimhane ve soğuk zincir hijyen sertifikasyonu (AB'ye bağırsak ve yan ürün ihracatının şartı).
- **Geliştirme hedefi:** T+5: AB'ye ısıl işlem görmüş et ürünleri için SPS listelenmesi (E-10-06); 2035: hayvan hastalıklarından ari bölge (Trakya) üzerinden AB ihracatı.

**7. Stratejik önem.** SS 52,6 (en yüksek boyut: gıda güvenliği 70; ağırlıklı ortalama 12,0) `[H]`. Kırmızı et arzı; canlı hayvan ithalatına bağımlı

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %2,10; %18 |
| ÜFE vekili (imalat üretimindeki pay) | %0,61 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,464 / 0,299 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %23 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 415,0 ve 15,42; 34 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −1 (−2 / +1) | −1 (−2 / 0) | −1 (−1 / 0) |
| Toplam ihracat ($ mn) | −1 (−2 / +1) | −1 (−2 / 0) | 0 (−1 / 0) |
| Nihai mal ithalatı ($ mn) | −1 (−3 / +43) | −1 (−4 / +25) | −1 (−2 / 0) |
| Cari denge ($ mn) | 0 (−34 / +1) | 0 (−20 / +2) | 0 (0 / +1) |
| Üretim ($ mn) | 0 (−42 / +2) | +1 (−26 / +2) | 0 (0 / +1) |
| İstihdam (kişi) | 0 (−78 / +3) | +1 (−47 / +4) | 0 (0 / +1) |
| TÜFE (bp, birinci tur) | +0,01 (+0,01 / +0,02) | +0,03 (+0,02 / +0,04) | +0,02 (+0,01 / +0,02) |
| Yatırım ve DYY (bütün senaryolar) | Etkisi yok; ESK alımları kamu kararı |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**10. Politika paketi**

| Eylem ID | Araç | Parametre | Sorumlu | Hukuki araç | Bütçe | Başlangıç–bitiş; sunset | Performans koşulu | KPI |
|---|---|---|---|---|---|---|---|---|
| E-10.11-01 | ESK ithalat kaynağı çeşitlendirme | AB payı %64 → ≤ %40; Brezilya, Uruguay ve Avustralya ile ihale çerçevesi | TOB, ESK | ESK yönetim kurulu kararı | İdari | T−12 → T+12; sunset: T+24 | Fiyat ≤ AB teklifi + %5 | Kırmızı et TÜFE alt endeksi yıllık artışı ≤ genel TÜFE + 5 puan |

**12. Erken uyarı ve tetikler**

| Gösterge | Eşik | Tetiklenecek önlem |
|---|---|---|
| Kırmızı et TÜFE alt endeksi (aylık) | 3 ay üst üste genel TÜFE'nin 5 puan üstünde | ESK'nın ek ithalat ve stok satışı |

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Etkilenen kesim yok. 1/98 askıya alınırsa et ithalatçıları ve tüketiciler kaybeder; telafi ESK'nın kaynak çeşitlendirmesi.

**14. Riskler ve azaltım**

- AB'nin 1/98'i askıya alması ithalat maliyetini artırır → E-10-01 ve E-10.11-01.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Yüksek (veri); ihracatın bileşimi `[H]`. `[D?]`: AB'ye et ürünü ihracatındaki SPS listelenme durumu.


### 3.2 10.12 Kümes hayvanları etlerinin işlenmesi ve saklanması — GB statüsü: TARIM-1/98 | Birincil/ikincil arketip: B/D | Duruş: Geliştir

*Güçlü ihracatçı ($643 mn), ama ihracatın %70'i Irak'a gidiyor; AB'ye ihracat yok denecek kadar az. GB çıkışının etkisi sıfıra yakın, asıl risk pazar yoğunlaşması.*

**1. Kimlik.** Rev. 2.1: 10.12 (1:1); CPA 10.12. Başlıca HS4 (TR ihracatı 2024): 0207 %100, 0505 %0, 6701 %0, 0209 %0. BEC payları (ticaret ağırlıklı): ara %2 / sermaye %0 / tüketim %98.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $7.057 mn; $2.136 mn (GSYH'nin %0,16) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 35.710; 130 (12 / 77 / 24 / 0 / 68) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %98; 0,96 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | Manisa, Afyon, Kütahya, Uşak %16; Kocaeli, Sakarya, Düzce, Bolu, Yalova %15; Balıkesir, Çanakkale %13 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Banvit (BRF ve Katar Yatırım Otoritesi), Beypi, Şenpiliç, Erpiliç, Keskinoğlu, Gedik Piliç, Abalıoğlu `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $643 mn; %18 |
| AB payı; ilk 5 AB pazarı | %0; DEU %45; AUT %28; MLT %9; HUN %4; ITA %4 |
| İlk 5 AB dışı pazar | IRQ %69; UZB %4; MRT %3; COG %2; BLR %2 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $86 mn; AB %9, Çin %1; UKR %38; BRA %33; USA %12; ITA %4; IRQ %4 |
| Dış ticaret dengesi | $+557 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %30 |
| RCA dünya (2020 → 2024) / AB pazarında | 1,94 → 1,45 / 0,07 |
| Birim değer ÷ AB pazarı ortalaması | 1,95 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,1 → %0,3; 14. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %0,0; tam MFN ortalaması %0,0. Rejim: GB %100, İTÜ %0, tarım %0 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): UKR %39; BRA %22; GBR %15; CHN %9; THA %4. Tercihli rakip payı %57.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: Fasıl 2 (0207): tamamen elde edilmiş.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.
- AB pazarına taze kanatlı eti ihracatı SPS listelenmesine bağlı; bugün yok denecek kadar az ($3 mn) `[D?]`.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %56,1, İGV dahil %56,1 `[V]`. S4'te AB menşeline (c2): %0,4.
- Kritik girdiler (HS4 1005, 1201, 2304), Türkiye'nin toplam ithalatı 2024: $3.393 mn (AB %4; BRA %35, UKR %25, ARG %13) `[V]`.
- Yem maliyetinin ana kalemleri mısır ve soya küspesi. Bunlar ithal (Ukrayna, Brezilya, ABD) ve tarım rejiminde, GB'den bağımsız. DİR ile ihracata yönelik kullanılıyor.

**6. Kabiliyet**

- KS 46,0 (sıra 158/230; ağırlık duyarlılığında P10–P90 83–199). Bileşenler: RCA 42, PCI 13 (PCI −0,89), yurt içi KD 73, Ar-Ge 25, tedarikçi 84, verimlilik 95, firma 24 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): 050510 (PCI +0.13, RCA 0.08); 020711 (PCI +0.15, RCA 0.21) `[T]`.
- **Kırmızı çizgi yetkinlikleri:** Entegre üretim (damızlık–kuluçka–kesim) ve helal sertifikasyonu; Irak dışı pazarlara giriş için kalıntı izleme.
- **Geliştirme hedefi:** T+5: Irak payı %70 → ≤ %50 (Körfez, Orta Asya, Afrika); 2035: AB'ye pişmiş kanatlı ürünü listelenmesi.

**7. Stratejik önem.** SS 60,0 (en yüksek boyut: gıda güvenliği 80; ağırlıklı ortalama 13,5) `[H]`. En ucuz hayvansal protein; yem (mısır/soya) ithalatına bağımlı

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %1,65; %2 |
| ÜFE vekili (imalat üretimindeki pay) | %1,06 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,048 / 0,004 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %98 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 873,9 ve 2,45; 25 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (−1 / 0) | −1 (−1 / 0) | 0 (0 / 0) |
| Toplam ihracat ($ mn) | 0 (−1 / 0) | 0 (−1 / 0) | 0 (0 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (−2 / +1) | −1 (−2 / 0) | 0 (−1 / 0) |
| Cari denge ($ mn) | 0 (0 / +1) | 0 (0 / +1) | 0 (0 / 0) |
| Üretim ($ mn) | 0 (−1 / +1) | 0 (0 / +1) | 0 (0 / +1) |
| İstihdam (kişi) | 0 (−2 / +3) | +1 (−1 / +4) | +1 (0 / +2) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | +0,01 (+0,01 / +0,01) | +0,01 (0,00 / +0,01) |
| Yatırım ve DYY (bütün senaryolar) | GB'den bağımsız; Irak riskine bağlı |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**10. Politika paketi**

| Eylem ID | Araç | Parametre | Sorumlu | Hukuki araç | Bütçe | Başlangıç–bitiş; sunset | Performans koşulu | KPI |
|---|---|---|---|---|---|---|---|---|
| E-10.12-01 | Pazar çeşitlendirme | Körfez İşbirliği Konseyi, Orta Asya ve Batı Afrika'da helal kanatlı tescili ve kota | Ticaret Bakanlığı (İhracat GM), TOB | STA müzakereleri; SPS ikili protokolleri | 0,05 mlr TL/yıl `[T]` | T−12 → T+36; sunset: T+36 | Yeni pazarlarda tescil | Irak payı ≤ %50 |
| E-10.12-02 | AB SPS listelenme talebi | Isıl işlem görmüş kanatlı ürünleri için AB üçüncü ülke listesi (S2 SPS bölümü) | TOB, Ticaret Bakanlığı | S2 anlaşma metni (SPS) | İdari | T−18 → T+24; sunset: — | AB denetimi (DG SANTE) | Liste kararı |

**12. Erken uyarı ve tetikler**

| Gösterge | Eşik | Tetiklenecek önlem |
|---|---|---|
| Irak'a kanatlı ihracatı (aylık) | Yıllık −%20 | Eximbank kredi sigortası limitinin artırılması; pazar çeşitlendirme hızlandırılır |

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** GB çıkışından etkilenen yok. Bölgeler: Manisa–Afyon (%16), Kocaeli–Sakarya–Bolu (%15), Balıkesir–Çanakkale (%13); risk Irak'a bağlı.

**14. Riskler ve azaltım**

- Irak'ın ithalat yasağı ya da kotası (2024 öncesinde de görüldü) → pazar çeşitlendirme.
- Kuş gribi → bölgeselleştirme protokolleri.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Yüksek. `[D?]`: AB'ye kanatlı ürünü listelenme durumu (DG SANTE üçüncü ülke listeleri).


### 3.3 10.13 Et ve kümes hayvanları etlerinden üretilen ürünlerin imalatı — GB statüsü: TARIM-1/98 | Birincil/ikincil arketip: — | Duruş: Koru

*Küçük ve iç pazara dönük. AB ihracatı Kıbrıs düzeltmesinden sonra $5 mn. GB çıkışının etkisi yok; S4'te 1/98 kaybında AB MFN'si %53, ama hacim küçük.*

**1. Kimlik.** Rev. 2.1: 10.13 (1:1); CPA 10.13. Başlıca HS4 (TR ihracatı 2024): 1602 %64, 1601 %32, 2301 %2, 0210 %2. BEC payları (ticaret ağırlıklı): ara %23 / sermaye %0 / tüketim %77.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $2.240 mn; $379 mn (GSYH'nin %0,03) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 11.726; 945 (62 / 778 / 135 / 31 / 7) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %26; 0,64 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İzmir %16; İstanbul %16; Manisa, Afyon, Kütahya, Uşak %8 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Pınar, Namet, Polonez, Apikoğlu `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $214 mn; %152 |
| AB payı; ilk 5 AB pazarı | %2; AUT %55; FRA %20; BGR %11; MLT %5; NLD %2 |
| İlk 5 AB dışı pazar | IRQ %21; VEN %15; SYR %7; CYP %5; KWT %4 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $64 mn; AB %56, Çin %0; POL %23; GBR %16; DNK %11; IRN %9; TUN %8 |
| Dış ticaret dengesi | $+150 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %17 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,28 → 0,49 / 0,06 |
| Birim değer ÷ AB pazarı ortalaması | 0,83 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,1 → %0,2; 14. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %53,0; tam MFN ortalaması %53,0. Rejim: GB %0, İTÜ %0, tarım %100 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): BRA %33; THA %31; GBR %14; CHN %13; CHE %3. Tercihli rakip payı %20.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 1601–1602: Fasıl 1, 2 ve 16 malzemeleri tamamen elde edilmiş.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %11,6, İGV dahil %11,6 `[V]`. S4'te AB menşeline (c2): %0,0.
- Kritik girdiler (HS4 0201, 0202, 0207), Türkiye'nin toplam ithalatı 2024: $923 mn (AB %65; POL %33, BRA %28, FRA %16) `[V]`.

**6. Kabiliyet**

- KS 54,1 (sıra 69/230; ağırlık duyarlılığında P10–P90 41–118). Bileşenler: RCA 45, PCI 60 (PCI 0,17), yurt içi KD 50, Ar-Ge 25, tedarikçi 84, verimlilik 81, firma 55 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): 160231 (PCI +0.43, RCA 0.38) `[T]`.

**7. Stratejik önem.** SS 29,8 (en yüksek boyut: gıda güvenliği 40; ağırlıklı ortalama 6,0) `[H]`. İşlenmiş et; temel tüketim

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,85; %5 |
| ÜFE vekili (imalat üretimindeki pay) | %0,34 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,046 / 0,026 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %26 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 257,0 ve 2,09; 16 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (−2 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (−2 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (0 / +3) | 0 (0 / +2) | 0 (0 / 0) |
| Cari denge ($ mn) | 0 (−2 / 0) | 0 (−1 / 0) | 0 (−2 / 0) |
| Üretim ($ mn) | 0 (−2 / 0) | 0 (−2 / 0) | 0 (−2 / 0) |
| İstihdam (kişi) | 0 (−9 / 0) | 0 (−5 / 0) | 0 (−7 / 0) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Etkilenen kesim yok.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Yüksek.


### 3.4 10.20 Balık, kabuklu deniz hayvanları ve yumuşakçaların işlenmesi ve saklanması — GB statüsü: TARIM-1/98 | Birincil/ikincil arketip: A | Duruş: Koru

*AB'ye entegre bir tarım ihracatçısı: levrekte dünya birincisi (%32), çipurada ikinci (%31); AB'ye $491 mn ihracat. GB'ye bağlı değil, 1/98'in balıkçılık tavizlerine bağlı. AB ticaret savunmasının tarihi var.*

**1. Kimlik.** Rev. 2.1: 10.20 (1:1); CPA 10.20. Başlıca HS4 (TR ihracatı 2024): 0304 %42, 0303 %39, 1604 %8, 0305 %4. BEC payları (ticaret ağırlıklı): ara %16 / sermaye %0 / tüketim %79.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $2.685 mn; $722 mn (GSYH'nin %0,05) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 14.445; 380 (42 / 296 / 51 / 23 / 9) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %69; 0,85 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İzmir %19; Aydın, Denizli, Muğla %18; Trabzon, Ordu, Giresun, Rize, Artvin, Gümüşhane %16 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Kılıç Deniz, Gümüşdoğa, Agromey, Özpekler, Fjord Marin (Norveç sermayesi) `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $1.237 mn; %102 |
| AB payı; ilk 5 AB pazarı | %40; ITA %29; NLD %22; DEU %15; GRC %10; FRA %5 |
| İlk 5 AB dışı pazar | RUS %41; GBR %14; JPN %8; USA %7; KOR %5 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $514 mn; AB %7, Çin %4; MAR %31; NOR %8; MYS %7; RUS %6; GIN %5 |
| Dış ticaret dengesi | $+723 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %27 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,48 → 0,75 / 0,53 |
| Birim değer ÷ AB pazarı ortalaması | 1,18 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %1,5 → %2,1; 14. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %16,3; tam MFN ortalaması %16,3. Rejim: GB %0, İTÜ %0, tarım %100 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): NOR %15; ECU %9; MAR %8; CHN %7; IND %4. Tercihli rakip payı %64.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: Fasıl 3 ve 1604–1605: tamamen elde edilmiş (yetiştiricilikte yumurta/yavru TR'de).
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.
- AB ticaret savunması: AB Türk gökkuşağı alabalığına 2015'te telafi edici vergi koydu (2015/309), vergiyi 2021'de beş yıl uzattı (2021/823), vergi 26.5.2026'da sona erdi. Levrek ve çipurada sübvansiyon soruşturması 2016'da önlemsiz kapandı `[V]`. Yunan ve İspanyol üreticiler hassas; hasmane AB'de yeni soruşturma olasılığı yüksek `[H]`.
- Taze balıkta AB MFN'si %15. 1/98 kaybında (P10) AB'ye ihracat −$137 mn ve −417 kişi.
- Değer zinciri: AB perakende zincirlerine taze ürün (çabuk bozulan, tam zamanında). Sınır gecikmesi maliyeti yüksek.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %14,7, İGV dahil %19,5 `[V]`. S4'te AB menşeline (c2): %0,0.
- Kritik girdiler (HS4 0303, 2301), Türkiye'nin toplam ithalatı 2024: $432 mn (AB %13; MAR %31, NOR %7, RUS %7) `[V]`.
- Balık yemi girdisi balık unu (Moritanya, Peru) ve soya. Yavru üretimi yurt içinde.

**6. Kabiliyet**

- KS 46,7 (sıra 153/230; ağırlık duyarlılığında P10–P90 79–192). Bileşenler: RCA 51, PCI 10 (PCI −0,97), yurt içi KD 65, Ar-Ge 25, tedarikçi 84, verimlilik 94, firma 31 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): 030539 (PCI -0.91, RCA 0.30); 030619 (PCI -0.96, RCA 0.08) `[T]`.
- **Kırmızı çizgi yetkinlikleri:** Kuluçkahane ve genetik (yavru) kapasitesi; AB sağlık sertifikası ve izlenebilirlik (ASC/GlobalG.A.P.).
- **Geliştirme hedefi:** T+5: AB payını koruyup ABD ve Körfez'e işlenmiş fileto; 2035: açık deniz yetiştiriciliği ve yeni türler (kuzey Ege).

**7. Stratejik önem.** SS 37,7 (en yüksek boyut: gıda güvenliği 50; ağırlıklı ortalama 9,0) `[H]`. Su ürünleri; yetiştiricilik ihracatı

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,14; %6 |
| ÜFE vekili (imalat üretimindeki pay) | %0,40 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,048 / 0,003 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %69 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 1.287,1 ve 14,92; 42 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / +10) | 0 (0 / 0) | 0 (−137 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / +7) | 0 (0 / 0) | 0 (−112 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (0 / +2) | 0 (0 / +1) | 0 (0 / 0) |
| Cari denge ($ mn) | 0 (0 / +4) | 0 (0 / 0) | 0 (−89 / 0) |
| Üretim ($ mn) | 0 (−1 / +5) | 0 (−1 / 0) | 0 (−112 / 0) |
| İstihdam (kişi) | 0 (−2 / +19) | 0 (−2 / 0) | 0 (−417 / 0) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) |
| Yatırım ve DYY (bütün senaryolar) | Norveç sermayeli yatırımlar 1/98 belirsizliğine duyarlı `[H]` |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**10. Politika paketi**

| Eylem ID | Araç | Parametre | Sorumlu | Hukuki araç | Bütçe | Başlangıç–bitiş; sunset | Performans koşulu | KPI |
|---|---|---|---|---|---|---|---|---|
| E-10.20-01 | Destek programlarının ASCM uyum dosyası | Yetiştiricilik desteklerinin (yem, yavru) ihracata bağlı olmadığının belgelenmesi; destek tasarımında ihracat koşulu yok | TOB, Ticaret Bakanlığı (İthalat GM) | Destek tebliğleri | İdari | T−12 → T; sunset: — | Dosya hazır | AB soruşturması açılırsa ilk yanıt 30 gün |
| E-10.20-02 | S2'de balıkçılık tavizi | Levrek, çipura ve alabalıkta kota/tavan yerine %0; menşe: yetiştiricilikte yavru TR'de | Ticaret Bakanlığı, TOB | S2 anlaşma metni (tarım eki) | İdari | T−18 → T; sunset: — | — | Tavizli satırların AB ihracatı ≥ T−12 düzeyi |

**11. Müzakere pozisyonu**

- AB ile hücum: 1/98 balıkçılık tavizlerinin tam liberalizasyona dönüştürülmesi; karşılığında AB'ye işlenmiş ürün kotası (E-10-06).
- Üçüncü ülke STA'ları: Körfez (taze levrek/çipura), Japonya (alabalık).

**12. Erken uyarı ve tetikler**

| Gösterge | Eşik | Tetiklenecek önlem |
|---|---|---|
| AB'nin soruşturma başlatma ilanı (OJ C) | İlan | E-10-04: yanıt ekibi; AB ithalatçılarıyla ortak savunma |
| AB'ye taze balık ihracatı (aylık, ton) | Yıllık −%15 | 1/98 ihlali iddiasıyla Ortaklık Konseyi ve DTÖ başvurusu |

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Kaybeden (yalnız 1/98 kaybında): Muğla (Milas, Bodrum) ve İzmir kıyı işletmeleri; 14 bin çalışan. Telafi: E-10-05 benzeri ihracat sigortası ve AB dışı pazar.

**14. Riskler ve azaltım**

- Yeni AB telafi edici vergi soruşturması → E-10-04.
- 1/98'in askıya alınması → E-10-01.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Orta (1/98 tavizlerinin satır içeriği: VB-06). `[D?]`: levrek ve çipurada bugünkü AB tercih oranı ve kota.


### 3.5 10.31 Patatesin işlenmesi ve saklanması — GB statüsü: KARMA | Birincil/ikincil arketip: — | Duruş: Koru

*Küçük sınıf (patates ürünleri). AB ihracatı Kıbrıs düzeltmesinden sonra $4 mn; GB etkisi yok.*

**1. Kimlik.** Rev. 2.1: 10.31 (1:1); CPA 10.31. Başlıca HS4 (TR ihracatı 2024): 2004 %85, 2005 %13, 0710 %2, 1105 %1. BEC payları (ticaret ağırlıklı): ara %12 / sermaye %0 / tüketim %88.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $385 mn; $107 mn (GSYH'nin %0,01) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 2.152; 145 (10 / 125 / 13 / 6 / 2) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %38; 0,37 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İstanbul %46; Konya, Karaman %16; Kırıkkale, Aksaray, Niğde, Nevşehir, Kırşehir %12 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Pepsico (Lay's; Tarsus ve Kocaeli `[D?]`), Ülker `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $110 mn; %140 |
| AB payı; ilk 5 AB pazarı | %3; DEU %37; GRC %23; BGR %15; FRA %9; NLD %5 |
| İlk 5 AB dışı pazar | RUS %54; IRQ %15; CHN %10; CYP %6; GEO %4 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $22 mn; AB %85, Çin %0; NLD %38; DEU %32; BEL %7; RUS %7; LBN %5 |
| Dış ticaret dengesi | $+88 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %28 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,40 → 0,49 / 0,40 |
| Birim değer ÷ AB pazarı ortalaması | 0,76 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %1,3 → %1,6; 11. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %15,1; tam MFN ortalaması %15,1. Rejim: GB %0, İTÜ %0, tarım %100 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): GBR %49; SRB %13; EGY %5; NOR %4; CHE %4. Tercihli rakip payı %67.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 2004–2005: Fasıl 7 malzemesi tamamen elde edilmiş.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %25,7, İGV dahil %25,7 `[V]`. S4'te AB menşeline (c2): %0,0.

**6. Kabiliyet**

- KS 50,3 (sıra 111/230; ağırlık duyarlılığında P10–P90 61–169). Bileşenler: RCA 38, PCI 73 (PCI 0,42), yurt içi KD 68, Ar-Ge 25, tedarikçi 84, verimlilik 29, firma 29 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.

**7. Stratejik önem.** SS 22,4 (en yüksek boyut: gıda güvenliği 30; ağırlıklı ortalama 4,5) `[H]`. 

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,22; %4 |
| ÜFE vekili (imalat üretimindeki pay) | %0,06 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,009 / 0,008 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %38 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 835,3 ve 9,83; 33 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (−2 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (−1 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (0 / +1) | 0 (0 / +1) | 0 (0 / 0) |
| Cari denge ($ mn) | 0 (−1 / 0) | 0 (−1 / 0) | 0 (−1 / 0) |
| Üretim ($ mn) | 0 (−1 / 0) | 0 (−1 / 0) | 0 (−1 / 0) |
| İstihdam (kişi) | 0 (−5 / +1) | 0 (−3 / +1) | 0 (−5 / 0) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Etkilenen kesim yok.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Yüksek.


### 3.6 10.32 Sebze ve meyve suyu imalatı — GB statüsü: TARIM-1/98 | Birincil/ikincil arketip: B/A | Duruş: Geliştir

*Elma suyu konsantresinde dünya ikincisi (%16). ABD ana pazar (%67); AB'ye ihracatın büyük kısmı Hollanda'daki karıştırıcılara gidiyor. Tarım rejiminde; risk 1/98 kaybı ve ABD'nin ticaret savunması.*

**1. Kimlik.** Rev. 2.1: 10.32 (1:1); CPA 10.32. Başlıca HS4 (TR ihracatı 2024): 2009 %100. BEC payları (ticaret ağırlıklı): ara %0 / sermaye %0 / tüketim %100.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $1.980 mn; $415 mn (GSYH'nin %0,03) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 7.460; 322 (19 / 264 / 42 / 13 / 9) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %58; 0,66 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | Adana, Mersin %16; İstanbul %14; Bursa, Eskişehir, Bilecik %13 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Döhler, Konfrut, Elmasu, Aroma, Dimes, Tat `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $770 mn; %96 |
| AB payı; ilk 5 AB pazarı | %27; NLD %40; DEU %12; ITA %12; POL %7; ESP %7 |
| İlk 5 AB dışı pazar | USA %67; GBR %5; SAU %4; JPN %4; RUS %3 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $144 mn; AB %6, Çin %47; CHN %47; IRN %24; CYP %11; IRL %2; PAK %2 |
| Dış ticaret dengesi | $+625 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %21 |
| RCA dünya (2020 → 2024) / AB pazarında | 2,55 → 3,21 / 1,43 |
| Birim değer ÷ AB pazarı ortalaması | 1,19 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %4,8 → %5,7; 2. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %24,0; tam MFN ortalaması %24,0. Rejim: GB %0, İTÜ %0, tarım %100 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): BRA %48; UKR %5; ZAF %4; EGY %4; CRI %3. Tercihli rakip payı %35.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 2009: aynı başlık dışı; meyve tamamen elde edilmiş.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.
- 1/98 kaybında (P10) meyve sularında AB MFN'si %24'e çıkar (giriş fiyatı sistemi dahil değil): AB'ye ihracat −$74 mn.
- Değer zinciri: AB içecek sanayisine ara girdi (konsantre).

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %58,5, İGV dahil %58,5 `[V]`. S4'te AB menşeline (c2): %0,0.
- Kritik girdiler (HS4 2009), Türkiye'nin toplam ithalatı 2024: $144 mn (AB %18; CHN %47, IRN %24, CYP %11) `[V]`.

**6. Kabiliyet**

- KS 51,6 (sıra 95/230; ağırlık duyarlılığında P10–P90 35–160). Bileşenler: RCA 84, PCI 16 (PCI −0,84), yurt içi KD 54, Ar-Ge 25, tedarikçi 84, verimlilik 83, firma 31 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.
- **Kırmızı çizgi yetkinlikleri:** Konsantre üretiminde patulin ve kalıntı kontrolü (ABD ve AB eşikleri).
- **Geliştirme hedefi:** T+5: konsantre yerine aseptik nihai ürün (NFC) payını artırmak.

**7. Stratejik önem.** SS 14,9 (en yüksek boyut: gıda güvenliği 20; ağırlıklı ortalama 3,0) `[H]`. 

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,18; %3 |
| ÜFE vekili (imalat üretimindeki pay) | %0,30 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,017 / 0,001 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %58 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 1.256,0 ve 6,32; 32 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / +4) | 0 (0 / 0) | 0 (−74 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / +3) | 0 (0 / 0) | 0 (−60 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (0 / +1) | 0 (0 / 0) | 0 (0 / 0) |
| Cari denge ($ mn) | 0 (0 / +2) | 0 (0 / 0) | 0 (−48 / 0) |
| Üretim ($ mn) | 0 (0 / +2) | 0 (0 / 0) | 0 (−60 / 0) |
| İstihdam (kişi) | 0 (0 / +6) | 0 (0 / 0) | 0 (−156 / 0) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) |
| Yatırım ve DYY (bütün senaryolar) | Döhler (Almanya) yatırımları 1/98'e duyarlı `[H]` |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**12. Erken uyarı ve tetikler**

| Gösterge | Eşik | Tetiklenecek önlem |
|---|---|---|
| AB'ye ve ABD'ye konsantre ihracatı (aylık) | Yıllık −%20 | E-10-05 benzeri kredi sigortası; ABD'de damping soruşturması hazırlığı |

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Kaybeden (yalnız 1/98 kaybında): Isparta, Karaman, Niğde elma bölgeleri.

**14. Riskler ve azaltım**

- 1/98 askısı → E-10-01.
- ABD'nin elma suyu ticaret savunması (geçmişte Çin'e uyguladı) `[H]`.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Orta.


### 3.7 10.39 Meyve ve sebzelerin diğer şekillerde işlenmesi ve korunması — GB statüsü: TARIM-1/98 | Birincil/ikincil arketip: A | Duruş: Koru

*10–12'nin en büyük AB ihracatçısı: AB'ye $3,6 mlr, AB payı %56. Dünya birincisi olduğu ürünler: fındık içi (%62), kuru kayısı (%75), kuru incir (%50), kuru üzüm (%30). Tamamı 1/98'de. S4'ün P50 etkisi yok; P10'da (1/98 askısı) −$1.141 mn ve −3.215 kişi.*

**1. Kimlik.** Rev. 2.1: 10.39 (1:1); CPA 10.39. Başlıca HS4 (TR ihracatı 2024): 0802 %29, 2008 %19, 0806 %9, 0813 %8. BEC payları (ticaret ağırlıklı): ara %1 / sermaye %0 / tüketim %99. Kabuklu fındık ve kuru meyvenin bir kısmı A bölümünde (01.25); burada işlenmiş, kavrulmuş, ezme ve kuru meyve hazırlıkları var.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $13.264 mn; $2.174 mn (GSYH'nin %0,16) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 66.354; 3.961 (426 / 3.333 / 426 / 221 / 49) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %35; 0,51 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | Manisa, Afyon, Kütahya, Uşak %16; İzmir %14; Bursa, Eskişehir, Bilecik %10 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Ferrero (Oltan dahil), ofi (Olam), Balsu, Durak, Gürsoy; kuru meyvede Malatya ve Ege ihracatçıları `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $6.472 mn; %36 |
| AB payı; ilk 5 AB pazarı | %56; DEU %37; ITA %17; FRA %10; NLD %8; POL %7 |
| İlk 5 AB dışı pazar | GBR %14; USA %14; IRQ %9; RUS %5; CHE %5 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $1.177 mn; AB %8, Çin %4; USA %24; VNM %12; IRN %12; ECU %8; CHN %4 |
| Dış ticaret dengesi | $+5.296 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %16 |
| RCA dünya (2020 → 2024) / AB pazarında | 4,86 → 5,05 / 4,68 |
| Birim değer ÷ AB pazarı ortalaması | 1,23 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %15,8 → %18,6; 1. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %9,5; tam MFN ortalaması %9,5. Rejim: GB %0, İTÜ %0, tarım %100 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): 1 satır, AB ihracatının %0'i: KN 2008 11 10 %12,8 (€1,0 mn).
- AB pazarında AB dışı rakipler (tercih durumu): USA %12; CHN %9; ECU %5; VNM %5; ARG %5. Tercihli rakip payı %44.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: Fasıl 8 ve 20: meyve/fındık tamamen elde edilmiş; şeker ağırlık sınırı (2008).
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.
- 1/98 kaybında tarife satıra göre değişiyor: fındık içinde %3,2, kuru kayısıda %5,6, kuru incirde %7,7, işlenmiş meyve ve sebzede (2001–2008) %12–20. Ağırlıklı ortalama %9,5.
- Sınır dışı engel (bugün de): AB'nin artırılmış resmî kontroller listesinde (Uygulama Tüzüğü 2019/1793) Türk kuru incir, fındık ve antep fıstığı aflatoksin nedeniyle yer alıyor `[V]` (güncel satırlar `[D?]`).
- Değer zinciri: fındıkta AB şekerleme sanayisine (Ferrero, Lindt, Nestlé) ara girdi. Alıcı çok yoğunlaşmış, ama bağımlılık karşılıklı: Türkiye'nin dünya ihracatındaki payı %62.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %25,2, İGV dahil %25,2 `[V]`. S4'te AB menşeline (c2): %0,3.
- Kritik girdiler (HS4 0801, 0802, 0813), Türkiye'nin toplam ithalatı 2024: $1.161 mn (AB %3; USA %44, VNM %12, IRN %12) `[V]`.
- İthalat ($1,2 mlr) badem, ceviz, kaju ve antep fıstığı: ABD, Vietnam, İran. Tarım rejiminde; GB'den bağımsız.

**6. Kabiliyet**

- KS 49,8 (sıra 119/230; ağırlık duyarlılığında P10–P90 48–170). Bileşenler: RCA 79, PCI 9 (PCI −1,03), yurt içi KD 49, Ar-Ge 25, tedarikçi 84, verimlilik 61, firma 67 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.
- **Kırmızı çizgi yetkinlikleri:** Aflatoksin kontrolü ve izlenebilirlik (bahçe → depo → fabrika); fındık kırma ve kavurma kapasitesi; Malatya kayısı kurutma standardı.
- **Geliştirme hedefi:** T+5: ham fındık içi yerine fındık ezmesi ve kavrulmuş üründe payı +10 puan (atlanabilir ürünler: 2008 19); 2035: AB'nin yanında Asya şekerleme sanayisi (Çin, Hindistan) pazarı.

**7. Stratejik önem.** SS 37,2 (en yüksek boyut: gıda güvenliği 50; ağırlıklı ortalama 7,5) `[H]`. Gıda güvenliğinden çok tarımsal gelir ve ihracat: 400 binden fazla fındık üreticisi hane `[D?]`.

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,88; %3 |
| ÜFE vekili (imalat üretimindeki pay) | %1,99 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,118 / 0,010 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %35 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 2.626,2 ve 16,51; 51 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −1 (−2 / +72) | −1 (−2 / 0) | −3 (−1.141 / −1) |
| Toplam ihracat ($ mn) | −1 (−2 / +49) | −1 (−2 / 0) | −2 (−940 / −1) |
| Nihai mal ithalatı ($ mn) | 0 (−1 / +6) | 0 (−1 / +4) | −1 (−2 / 0) |
| Cari denge ($ mn) | 0 (−1 / +34) | 0 (−1 / 0) | −1 (−748 / −1) |
| Üretim ($ mn) | 0 (−2 / +43) | 0 (−2 / 0) | −1 (−939 / −1) |
| İstihdam (kişi) | −2 (−6 / +160) | −2 (−6 / −1) | −4 (−3.215 / −2) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) |
| Yatırım ve DYY (bütün senaryolar) | Ferrero'nun Türkiye'deki işleme yatırımı 1/98'e değil fındık arzına bağlı `[H]` |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**10. Politika paketi**

| Eylem ID | Araç | Parametre | Sorumlu | Hukuki araç | Bütçe | Başlangıç–bitiş; sunset | Performans koşulu | KPI |
|---|---|---|---|---|---|---|---|---|
| E-10.39-01 | Fındık arz güvenliği diyaloğu | AB şekerleme sanayisi ve Komisyonla çok yıllı arz ve fiyat şeffaflığı çerçevesi; 1/98'in sürmesiyle bağlantılı | Ticaret Bakanlığı, TOB, Karadeniz Fındık İhracatçıları Birliği | İdari mutabakat | İdari | T−18 → T; sunset: — | AB'nin 1/98'i sürdürmesi | 1/98 kesintisiz |
| E-10.39-02 | SPS kontrol sıklığını azaltma | 2019/1793 listesindeki Türk ürünlerinde kontrol oranının düşürülmesi; ön ihracat kontrolü (PEC) ve laboratuvar akreditasyonu | TOB, TÜRKAK | AB ile SPS teknik protokolü | 0,03 mlr TL/yıl `[T]` | T−12 → T+24; sunset: T+24 | RASFF bildirimleri −%30 | Kontrol oranı ≤ %10 |

**11. Müzakere pozisyonu**

- AB ile hücum: S2'de 1/98'in tam aktarımı; işlenmiş meyve ve sebzede giriş fiyatı sistemi istisnası ve kotaların genişletilmesi (E-10-06).
- Üçüncü ülke: Çin ve Hindistan'da fındık ve kuru meyve tarifesi (Çin'de fındık MFN %10 `[D?]`); Körfez STA'sı.

**12. Erken uyarı ve tetikler**

| Gösterge | Eşik | Tetiklenecek önlem |
|---|---|---|
| AB'nin 1/98 tavizlerini askıya alma girişimi | Komisyon önerisi ya da Uygulama Tüzüğü 654/2014 bildirimi | E-10-01: Ortaklık Konseyi toplantı talebi ve DTÖ istişaresi; fındık arz diyaloğu devreye girer |
| AB'ye fındık ve kuru meyve ihracatı (aylık, ton) | Yıllık −%10 | E-10-05 genişletilir; Asya pazarı hızlandırılır |

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Kaybeden (yalnız 1/98 askısında): Karadeniz (Ordu, Giresun, Trabzon; fındık) ve Malatya, Manisa, Aydın (kuru meyve). En büyük üç bölgenin istihdam payı %40. Telafi: tarımsal gelir desteği değil ihracat sigortası ve pazar çeşitlendirme; fındıkta TMO alımı son çare.

**14. Riskler ve azaltım**

- 1/98 askısı (olasılık 0,25 varsayıldı) → E-10-01 ve fındık arz diyaloğu.
- Aflatoksin kaynaklı AB kontrol artışı (çıkıştan bağımsız) → SPS eylemi.
- Ferrero'nun alım payı (yaklaşık üçte bir `[D?]`): fiyat gücü yoğunlaşması.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Orta (1/98 satır içeriği VB-06; 1/98 askı olasılığı `[H]`). `[D?]`: Ferrero'nun Türkiye fındık alım payı; 2019/1793'ün güncel Türkiye satırları.


### 3.8 10.41 Sıvı ve katı yağ imalatı — GB statüsü: TARIM-1/98 | Birincil/ikincil arketip: D/B | Duruş: Geliştir

*Rafine ayçiçek yağında dünya birincisi (%19), ama ithal ham yağa ve tohuma bağımlı: Rusya ve Ukrayna %42, palm yağında Malezya %21. AB'ye ihracat %9. Gıda güvenliği sınıfı; GB çıkışının etkisi sıfıra yakın.*

**1. Kimlik.** Rev. 2.1: 10.41 (1:1); CPA 10.41. Başlıca HS4 (TR ihracatı 2024): 1512 %41, 1509 %21, 2304 %17, 1507 %11. BEC payları (ticaret ağırlıklı): ara %71 / sermaye %0 / tüketim %29.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $7.265 mn; $910 mn (GSYH'nin %0,07) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 17.859; 1.938 (107 / 1.664 / 264 / 43 / 5) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %14; 0,44 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | Manisa, Afyon, Kütahya, Uşak %13; İzmir %11; Balıkesir, Çanakkale %10 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Küçükbay, Yonca, Zade, Oruçoğlu, Savola (Suudi), Cargill ve Bunge `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $3.183 mn; %110 |
| AB payı; ilk 5 AB pazarı | %9; ESP %44; ITA %23; EST %10; DEU %6; ROU %4 |
| İlk 5 AB dışı pazar | IRQ %15; USA %11; IRN %11; DJI %8; DZA %7 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $3.711 mn; AB %2, Çin %0; RUS %30; MYS %21; UKR %12; ARG %11; SYR %6 |
| Dış ticaret dengesi | $−527 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %13 |
| RCA dünya (2020 → 2024) / AB pazarında | 1,10 → 1,53 / 0,29 |
| Birim değer ÷ AB pazarı ortalaması | 1,07 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,3 → %1,2; 15. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %12,4; tam MFN ortalaması %12,4. Rejim: GB %0, İTÜ %0, tarım %100 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): BRA %18; UKR %17; IDN %13; ARG %12; MYS %8. Tercihli rakip payı %37.
- Menşe (S2 / S3): risk D/O; `c_RoO` %1,5 / %3,0; `p_uyum` 0,90 / 0,80 `[H]`. Kural: 1507–1515: aynı alt başlık dışı malzemeden; ham yağ ithalatından rafine yağ menşe kazanır.
- EUDR kapsamındaki AB ihracatı payı: %43; SKDM: %0.
- AB'ye ihracat ($283 mn) ağırlıkla zeytinyağı (İspanya %40, İtalya %21). 1/98 kaybında spesifik vergi AVE'si %12'ye çıkar (zeytinyağında €124,5/100 kg).
- EUDR: AB ihracatının %43'ü palm ve soya türevi satırlarda; ham yağın kökenine ilişkin coğrafi konum verisi gerekiyor (E-10-03).

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %18,9, İGV dahil %18,9 `[V]`. S4'te AB menşeline (c2): %0,0.
- Kritik girdiler (HS4 1206, 1512, 1511, 1507, 1201), Türkiye'nin toplam ithalatı 2024: $3.755 mn (AB %2; BRA %27, RUS %20, MYS %17) `[V]`.
- 2022 şoku: Ukrayna savaşında ham ayçiçek yağı fiyatı iki katına çıktı. Yerli tohum üretimi tüketimin yaklaşık yarısını karşılıyor `[D?]`.

**6. Kabiliyet**

- KS 45,7 (sıra 162/230; ağırlık duyarlılığında P10–P90 91–193). Bileşenler: RCA 67, PCI 7 (PCI −1,10), yurt içi KD 47, Ar-Ge 25, tedarikçi 84, verimlilik 45, firma 71 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.
- **Kırmızı çizgi yetkinlikleri:** Rafineri ve ekstraksiyon kapasitesi; DİR'deki ihracat ağı (Irak, Körfez).
- **Geliştirme hedefi:** T+5: yağlı tohum (ayçiçek, kanola) ekim alanı +%15; 2035: ham yağ ithalatında tek kaynak payı ≤ %30.

**7. Stratejik önem.** SS 63,3 (en yüksek boyut: gıda güvenliği 85; ağırlıklı ortalama 12,8) `[H]`. Bitkisel yağ temel tüketim ürünü. Ham yağ ve tohumda ithalat bağımlılığı yüksek, 2022'de fiyat şoku yaşandı.

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %1,00; %11 |
| ÜFE vekili (imalat üretimindeki pay) | %1,09 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,395 / 0,009 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %14 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 1.502,4 ve 52,71; 63 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / +6) | 0 (0 / 0) | 0 (−102 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / +4) | 0 (0 / 0) | 0 (−82 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (0 / +3) | 0 (0 / +2) | 0 (0 / 0) |
| Cari denge ($ mn) | 0 (−1 / +1) | 0 (−1 / 0) | 0 (−65 / 0) |
| Üretim ($ mn) | 0 (−1 / +1) | 0 (−1 / 0) | 0 (−82 / 0) |
| İstihdam (kişi) | 0 (−2 / +1) | 0 (−2 / 0) | 0 (−137 / 0) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) |
| Yatırım ve DYY (bütün senaryolar) | Etkisi yok |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**10. Politika paketi**

| Eylem ID | Araç | Parametre | Sorumlu | Hukuki araç | Bütçe | Başlangıç–bitiş; sunset | Performans koşulu | KPI |
|---|---|---|---|---|---|---|---|---|
| E-10.41-01 | Stratejik ham yağ stoku | 60 günlük tüketim; TMO ve özel lisanslı depo | TOB, TMO | Cumhurbaşkanı kararı (stok programı) | 0,15 mlr TL/yıl `[T]` (taşıma maliyeti) | T−12 → T+36; sunset: T+36 (gözden geçirme) | Stok ≥ 60 gün | Fiyat şokunda TÜFE yağ alt endeksi oynaklığı −%30 |

**12. Erken uyarı ve tetikler**

| Gösterge | Eşik | Tetiklenecek önlem |
|---|---|---|
| Ham ayçiçek yağı ithalat fiyatı (aylık) | 3 ayda +%25 | Stoktan satış; kaynak çeşitlendirme ihaleleri |

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** GB çıkışından etkilenen yok.

**14. Riskler ve azaltım**

- Karadeniz arz kesintisi (GB'den bağımsız) → stok.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Yüksek (veri), Orta (stok bütçesi).


### 3.9 10.42 Margarin ve benzeri yenilebilir katı yağların imalatı — GB statüsü: TARIM-1/98 | Birincil/ikincil arketip: B | Duruş: Geliştir

*Küçük sınıf (margarin): ihracat $165 mn, Irak ve Suriye ağırlıklı. GB etkisi yok; palm yağına bağımlı (Endonezya, Malezya).*

**1. Kimlik.** Rev. 2.1: 10.42 (1:1); CPA 10.42. Başlıca HS4 (TR ihracatı 2024): 1517 %100. BEC payları (ticaret ağırlıklı): ara %0 / sermaye %0 / tüketim %100.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $380 mn; $71 mn (GSYH'nin %0,01) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 773; 13 (1 / 7 / 2 / 3 / 1) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %49; 0,43 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İstanbul %55; İzmir %19; Adana, Mersin %16 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Unilever (Sana), Yonca, Bunge `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $165 mn; %69 |
| AB payı; ilk 5 AB pazarı | %7; ROU %62; DEU %15; BGR %8; NLD %3; GRC %3 |
| İlk 5 AB dışı pazar | IRQ %46; SYR %20; GEO %6; IRN %4; LBY %2 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $79 mn; AB %39, Çin %0; IDN %35; MYS %16; NLD %15; SWE %14; IND %6 |
| Dış ticaret dengesi | $+87 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %19 |
| RCA dünya (2020 → 2024) / AB pazarında | 1,61 → 1,62 / 0,78 |
| Birim değer ÷ AB pazarı ortalaması | 0,72 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %2,7 → %3,1; 10. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %14,9; tam MFN ortalaması %14,9. Rejim: GB %0, İTÜ %0, tarım %100 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): USA %21; GBR %20; IDN %14; CHE %10; NOR %8. Tercihli rakip payı %48.
- Menşe (S2 / S3): risk O/O; `c_RoO` %2,5 / %3,5; `p_uyum` 0,85 / 0,75 `[H]`. Kural: 1517: Fasıl 15 ve 4 malzemeleri ağırlık sınırı.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %22,5, İGV dahil %22,5 `[V]`. S4'te AB menşeline (c2): %0,0.
- Kritik girdiler (HS4 1511, 1513), Türkiye'nin toplam ithalatı 2024: $825 mn (AB %1; MYS %87, IDN %10, PHL %2) `[V]`.

**6. Kabiliyet**

- KS 41,8 (sıra 196/230; ağırlık duyarlılığında P10–P90 145–209). Bileşenler: RCA 57, PCI 22 (PCI −0,58), yurt içi KD 51, Ar-Ge 25, tedarikçi 84, verimlilik 42, firma 18 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.

**7. Stratejik önem.** SS 29,8 (en yüksek boyut: gıda güvenliği 40; ağırlıklı ortalama 6,0) `[H]`. 

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,07; %7 |
| ÜFE vekili (imalat üretimindeki pay) | %0,06 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,011 / 0,004 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %49 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 419,2 ve 6,76; 26 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (−2 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (−1 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (0 / +2) | 0 (0 / +1) | 0 (0 / 0) |
| Cari denge ($ mn) | 0 (−1 / 0) | 0 (−1 / 0) | 0 (−1 / 0) |
| Üretim ($ mn) | 0 (−2 / 0) | 0 (−1 / 0) | 0 (−1 / 0) |
| İstihdam (kişi) | 0 (−2 / 0) | 0 (−1 / 0) | 0 (−2 / 0) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Etkilenen kesim yok.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Yüksek.


### 3.10 10.51 Süthane işletmelerinin faaliyetleri ve peynir imalatı — GB statüsü: TARIM-1/98 | Birincil/ikincil arketip: — | Duruş: Koru

*İç pazara dönük büyük işveren (49 bin kişi). AB ihracatı $26 mn, Almanya'daki diaspora pazarı. Tarım rejiminde; GB etkisi yok.*

**1. Kimlik.** Rev. 2.1: 10.51 (1:1); CPA 10.51. Başlıca HS4 (TR ihracatı 2024): 0406 %52, 0402 %16, 0404 %15, 0403 %7. BEC payları (ticaret ağırlıklı): ara %28 / sermaye %0 / tüketim %72.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $10.843 mn; $1.987 mn (GSYH'nin %0,15) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 48.749; 2.293 (180 / 1.802 / 374 / 89 / 37) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %52; 0,48 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | Kocaeli, Sakarya, Düzce, Bolu, Yalova %15; İzmir %14; Bursa, Eskişehir, Bilecik %13 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Sütaş, Pınar, Danone, Ak Gıda (İçim), SEK, Torku `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $440 mn; %21 |
| AB payı; ilk 5 AB pazarı | %6; DEU %46; FRA %18; BGR %9; NLD %6; CZE %4 |
| İlk 5 AB dışı pazar | IRQ %20; EGY %8; DZA %7; SAU %6; ARE %5 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $112 mn; AB %46, Çin %0; CYP %24; NLD %10; DEU %7; IRL %7; ITA %6 |
| Dış ticaret dengesi | $+328 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %18 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,40 → 0,35 / 0,25 |
| Birim değer ÷ AB pazarı ortalaması | 1,22 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,3 → %1,0; 7. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,2; 1/98 kaybıyla %22,5; tam MFN ortalaması %22,6. Rejim: GB %0, İTÜ %2, tarım %98 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): GBR %55; CHE %24; NZL %7; UKR %4; USA %2. Tercihli rakip payı %93.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: Fasıl 4: Fasıl 4 malzemeleri tamamen elde edilmiş.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %137,9, İGV dahil %137,9 `[V]`. S4'te AB menşeline (c2): %0,0.
- Kritik girdiler (HS4 0402, 0404, 0405, 0406), Türkiye'nin toplam ithalatı 2024: $90 mn (AB %64; CYP %24, IRL %9, NLD %8) `[V]`.
- AB'den ithalat süt tozu, peynir altı suyu tozu ve tereyağı. Tarım rejiminde; 1/98'deki Türk tavizleri kalkarsa maliyet artar, ama ithalat küçük ($52 mn).

**6. Kabiliyet**

- KS 45,7 (sıra 161/230; ağırlık duyarlılığında P10–P90 105–196). Bileşenler: RCA 17, PCI 58 (PCI 0,15), yurt içi KD 51, Ar-Ge 25, tedarikçi 84, verimlilik 54, firma 56 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): 040520 (PCI +0.16, RCA 0.07) `[T]`.

**7. Stratejik önem.** SS 56,8 (en yüksek boyut: gıda güvenliği 75; ağırlıklı ortalama 14,2) `[H]`. Süt ve süt ürünleri; çiğ süt üreticisi geliri

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %3,01; %4 |
| ÜFE vekili (imalat üretimindeki pay) | %1,63 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,137 / 0,063 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %52 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 135,1 ve 0,64; 12 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / +1) | 0 (0 / 0) | 0 (−9 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (−7 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (0 / +4) | 0 (0 / +2) | 0 (0 / 0) |
| Cari denge ($ mn) | 0 (−3 / 0) | 0 (−2 / 0) | 0 (−6 / 0) |
| Üretim ($ mn) | 0 (−3 / 0) | 0 (−2 / 0) | 0 (−7 / 0) |
| İstihdam (kişi) | 0 (−10 / 0) | 0 (−7 / 0) | 0 (−23 / 0) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Etkilenen kesim yok.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Yüksek.


### 3.11 10.52 Dondurma imalatı — GB statüsü: İTÜ | Birincil/ikincil arketip: — | Duruş: Koru

*İç pazara dönük (dondurma). Kıbrıs düzeltmesinden sonra AB ihracatı $1 mn; GB etkisi yok.*

**1. Kimlik.** Rev. 2.1: 10.52 (1:1); CPA 10.52. Başlıca HS4 (TR ihracatı 2024): 2105 %100. BEC payları (ticaret ağırlıklı): ara %0 / sermaye %0 / tüketim %100.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $2.017 mn; $489 mn (GSYH'nin %0,04) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 7.589; 878 (22 / 841 / 42 / 10 / 4) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %40; 1,35 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İstanbul %26; Hatay, Kahramanmaraş, Osmaniye %23; Konya, Karaman %5 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Unilever (Algida; Konya), Ülker (Golf), Panda `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $72 mn; %56 |
| AB payı; ilk 5 AB pazarı | %1; DEU %32; BEL %28; NLD %23; FRA %5; MLT %3 |
| İlk 5 AB dışı pazar | USA %16; IRQ %16; CYP %10; ARE %7; SRB %7 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $5 mn; AB %54, Çin %2; CHE %30; FRA %30; MDA %10; POL %7; NLD %5 |
| Dış ticaret dengesi | $+67 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %24 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,96 → 0,99 / 0,10 |
| Birim değer ÷ AB pazarı ortalaması | 1,10 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,1 → %0,4; 12. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %8,5; 1/98 kaybıyla %8,5; tam MFN ortalaması %15,7. Rejim: GB %0, İTÜ %100, tarım %0 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): GBR %45; SRB %30; UKR %10; CHE %4; MKD %3. Tercihli rakip payı %63.
- Menşe (S2 / S3): risk D/O; `c_RoO` %1,5 / %2,5; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 2105: başlık değişikliği; Fasıl 4 ve şeker ağırlık sınırları.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %8,2, İGV dahil %8,2 `[V]`. S4'te AB menşeline (c2): %8,2.

**6. Kabiliyet**

- KS 51,8 (sıra 91/230; ağırlık duyarlılığında P10–P90 48–149). Bileşenler: RCA 43, PCI 43 (PCI −0,13), yurt içi KD 60, Ar-Ge 25, tedarikçi 84, verimlilik 97, firma 38 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.

**7. Stratejik önem.** SS 3,7 (en yüksek boyut: gıda güvenliği 5; ağırlıklı ortalama 0,8) `[H]`. 

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,21; %2 |
| ÜFE vekili (imalat üretimindeki pay) | %0,30 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,004 / 0,002 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %40 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 376,6 ve 0,31; 15 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (−1 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (−1 / 0) | 0 (−1 / 0) | 0 (−1 / 0) |
| Cari denge ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Üretim ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| İstihdam (kişi) | 0 (0 / +1) | 0 (0 / +1) | +1 (0 / +1) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | +0,01 (+0,01 / +0,01) | +0,02 (+0,02 / +0,02) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Etkilenen kesim yok.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Yüksek.


### 3.12 10.61 Öğütülmüş hububat ve sebze ürünleri imalatı — GB statüsü: KARMA | Birincil/ikincil arketip: B/D | Duruş: Geliştir

*Dünya un ihracatında birinci (%19,6), bulgurda %75. İhracatın %92'si AB dışına (Irak, Suriye, Somali) ve DİR'de Rus buğdayıyla. GB etkisi küçük; asıl kırılganlık buğday arzı.*

**1. Kimlik.** Rev. 2.1: 10.61 (n:1); CPA 10.61. Başlıca HS4 (TR ihracatı 2024): 1101 %62, 1904 %12, 1006 %11, 1103 %5. BEC payları (ticaret ağırlıklı): ara %68 / sermaye %0 / tüketim %32.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $7.803 mn; $1.245 mn (GSYH'nin %0,09) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 26.004; 2.657 (172 / 2.271 / 383 / 75 / 8) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %10; 0,60 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | Konya, Karaman %10; Tekirdağ, Edirne, Kırklareli %8; Balıkesir, Çanakkale %7 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Yüzlerce orta ölçekli değirmen (Gaziantep, Konya, Mersin, Tekirdağ); yabancı çapa yok `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $1.870 mn; %25 |
| AB payı; ilk 5 AB pazarı | %7; DEU %41; BEL %16; AUT %7; NLD %7; FRA %6 |
| İlk 5 AB dışı pazar | IRQ %31; SYR %11; SOM %3; USA %3; DJI %3 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $739 mn; AB %17, Çin %11; RUS %43; CHN %11; IND %7; ITA %6; BRA %5 |
| Dış ticaret dengesi | $+1.131 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %16 |
| RCA dünya (2020 → 2024) / AB pazarında | 2,85 → 2,40 / 0,95 |
| Birim değer ÷ AB pazarı ortalaması | 1,11 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %3,0 → %3,8; 9. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %4,9; 1/98 kaybıyla %10,3; tam MFN ortalaması %24,5. Rejim: GB %0, İTÜ %64, tarım %36 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): GBR %22; PAK %13; IND %9; MMR %9; THA %8. Tercihli rakip payı %65.
- Menşe (S2 / S3): risk O/O; `c_RoO` %2,5 / %3,5; `p_uyum` 0,85 / 0,75 `[H]`. Kural: Fasıl 11 ve 1904: tahıl tamamen elde edilmiş (makarnalık buğday istisnası 1904'te).
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.
- AB'ye ihracat ($139 mn) un, bulgur ve kahvaltılık tahıl. İTÜ payının (%64) S4 sanayi bileşeni %4,9; AB'ye ihracatta S4'te −$24 mn.
- Menşe (S2/S3): Fasıl 11'de tahılın tamamen elde edilmiş olması isteniyor. DİR'de Rus buğdayından üretilen un menşe kazanmıyor (O).

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %19,2, İGV dahil %19,2 `[V]`. S4'te AB menşeline (c2): %0,9.
- Kritik girdiler (HS4 1001, 1003, 1005), Türkiye'nin toplam ithalatı 2024: $2.438 mn (AB %5; RUS %60, UKR %30, BRA %2) `[V]`.
- Buğday ithalatının %43'ü Rusya'dan. Karadeniz koridoru ve Rusya'nın ihracat kotası en büyük risk (2022, 2023) `[V]`.

**6. Kabiliyet**

- KS 48,1 (sıra 135/230; ağırlık duyarlılığında P10–P90 63–180). Bileşenler: RCA 60, PCI 7 (PCI −1,18), yurt içi KD 49, Ar-Ge 25, tedarikçi 84, verimlilik 75, firma 77 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.
- **Kırmızı çizgi yetkinlikleri:** Değirmencilik ve paketleme kapasitesi; DİR ağıyla kurulan Afrika–Orta Doğu dağıtım ilişkileri.
- **Geliştirme hedefi:** T+5: Batı Afrika ve Körfez'de pazar payı; 2035: Rusya payı ≤ %35.

**7. Stratejik önem.** SS 70,8 (en yüksek boyut: gıda güvenliği 95; ağırlıklı ortalama 14,2) `[H]`. Ekmek zincirinin başı: un ve buğday arzı gıda güvenliğinin çekirdeği.

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,86; %6 |
| ÜFE vekili (imalat üretimindeki pay) | %1,17 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,107 / 0,018 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %10 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 1.403,9 ve 9,03; 37 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −12 (−29 / +3) | −16 (−30 / −3) | −24 (−43 / −10) |
| Toplam ihracat ($ mn) | −9 (−20 / +2) | −11 (−21 / −2) | −19 (−34 / −8) |
| Nihai mal ithalatı ($ mn) | −1 (−2 / +8) | −1 (−3 / +5) | −2 (−4 / −1) |
| Cari denge ($ mn) | −6 (−15 / −4) | −8 (−15 / −5) | −13 (−24 / −6) |
| Üretim ($ mn) | −8 (−18 / −5) | −10 (−19 / −6) | −17 (−30 / −8) |
| İstihdam (kişi) | −19 (−43 / −11) | −23 (−44 / −14) | −39 (−71 / −18) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | +0,01 (0,00 / +0,01) | +0,01 (+0,01 / +0,02) |
| Yatırım ve DYY (bütün senaryolar) | Etkisi yok |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**10. Politika paketi**

| Eylem ID | Araç | Parametre | Sorumlu | Hukuki araç | Bütçe | Başlangıç–bitiş; sunset | Performans koşulu | KPI |
|---|---|---|---|---|---|---|---|---|
| E-10.61-01 | Buğday kaynak çeşitlendirme | Kazakistan, Romanya, Bulgaristan ve Kanada'dan TMO alım çerçeveleri; Rusya payı ≤ %35 | TMO, Ticaret Bakanlığı | TMO yönetim kurulu kararı; ikili mutabakatlar | İdari | T−18 → T+36; sunset: — | Alım fiyatı ≤ Rus teklifi + %3 | Tek kaynak payı ≤ %35 |

**12. Erken uyarı ve tetikler**

| Gösterge | Eşik | Tetiklenecek önlem |
|---|---|---|
| Rusya'nın buğday ihracat vergisi/kotası ya da Karadeniz kesintisi | Duyuru | TMO stok satışı; DİR'de alternatif kaynak izni hızlandırılır |

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** GB çıkışından küçük kayıp (S4 P50: −39 kişi); bölgeler Konya–Karaman, Trakya, Balıkesir.

**14. Riskler ve azaltım**

- Karadeniz arz şoku (GB'den bağımsız) → kaynak çeşitlendirme.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Yüksek.


### 3.13 10.62 Nişasta ve nişastalı ürünlerin imalatı — GB statüsü: KARMA | Birincil/ikincil arketip: B | Duruş: Geliştir

*Fruktozda dünya birincisi (%35). AB'ye $96 mn ihracat; AB MFN'si yüksek (glikozda %16), S4'te AB'ye ihracat −$31 mn. S2'de menşe sorunu yok, çünkü ithal mısırdan glikoz başlık değişikliğiyle menşe kazanıyor.*

**1. Kimlik.** Rev. 2.1: 10.62 (n:1); CPA 10.62. Başlıca HS4 (TR ihracatı 2024): 1702 %47, 1108 %25, 1515 %20, 3505 %7. BEC payları (ticaret ağırlıklı): ara %89 / sermaye %0 / tüketim %11.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $1.638 mn; $357 mn (GSYH'nin %0,03) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 3.117; 33 (3 / 18 / 4 / 6 / 5) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %75; 0,58 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | Adana, Mersin %45; İstanbul %35; Kocaeli, Sakarya, Düzce, Bolu, Yalova %6 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Cargill (Orhangazi), Tat Nişasta, Sunar Mısır, Pendik Nişasta `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $528 mn; %66 |
| AB payı; ilk 5 AB pazarı | %18; NLD %36; ITA %15; DEU %14; ESP %9; FRA %4 |
| İlk 5 AB dışı pazar | LBY %12; NGA %11; IRQ %9; USA %6; EGY %4 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $206 mn; AB %68, Çin %7; NLD %17; DEU %15; CHN %7; BEL %6; FRA %6 |
| Dış ticaret dengesi | $+322 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %22 |
| RCA dünya (2020 → 2024) / AB pazarında | 1,70 → 1,84 / 3,34 |
| Birim değer ÷ AB pazarı ortalaması | 0,85 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %7,2 → %13,3; 2. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %14,2; 1/98 kaybıyla %15,4; tam MFN ortalaması %54,3. Rejim: GB %0, İTÜ %95, tarım %5 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): 1 satır, AB ihracatının %83'i: KN 1702 50 00 %16,0 (€67,0 mn).
- AB pazarında AB dışı rakipler (tercih durumu): USA %20; CHN %11; GBR %11; THA %8; MEX %7. Tercihli rakip payı %34.
- Menşe (S2 / S3): risk D/O; `c_RoO` %1,5 / %2,5; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 1108: tahıl tamamen elde edilmiş; 1702 glikoz: başlık değişikliği (ithal mısırdan nişasta → glikoz menşe kazanır).
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.
- Değer zinciri: AB gıda ve içecek sanayisine ara girdi (glikoz ve fruktoz şurubu).
- AB'ye ihracat kaybı S2'de −$11 mn, S4'te −$31 mn; çapa yatırımcının (Cargill) AB'ye arzı AB'deki tesislerinden karşılayabilir `[H]`.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %26,4, İGV dahil %26,4 `[V]`. S4'te AB menşeline (c2): %5,3.
- Kritik girdiler (HS4 1005), Türkiye'nin toplam ithalatı 2024: $1.114 mn (AB %10; UKR %54, RUS %28, BRA %5) `[V]`.
- Nişasta bazlı şekerin (NBŞ) yurt içi satışı Şeker Kanunu'ndaki kotayla sınırlı; ihracat kotasız `[V]`.

**6. Kabiliyet**

- KS 52,6 (sıra 83/230; ağırlık duyarlılığında P10–P90 47–144). Bileşenler: RCA 65, PCI 52 (PCI 0,05), yurt içi KD 55, Ar-Ge 25, tedarikçi 84, verimlilik 74, firma 13 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.
- **Kırmızı çizgi yetkinlikleri:** Mısır ıslak öğütme kapasitesi; fruktozda ihracat sertifikasyonu.
- **Geliştirme hedefi:** T+5: AB dışı (Kuzey Afrika, Körfez) payı +10 puan.

**7. Stratejik önem.** SS 30,2 (en yüksek boyut: gıda güvenliği 40; ağırlıklı ortalama 7,5) `[H]`. Nişasta ve glikoz: gıda ve ilaç sanayisine ara girdi

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,00; %6 |
| ÜFE vekili (imalat üretimindeki pay) | %0,25 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,016 / 0,011 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %75 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 2.899,1 ve 13,27; 50 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −11 (−26 / +2) | −15 (−28 / −3) | −31 (−49 / −13) |
| Toplam ihracat ($ mn) | −8 (−19 / +1) | −11 (−20 / −2) | −25 (−39 / −10) |
| Nihai mal ithalatı ($ mn) | −4 (−13 / +10) | −6 (−15 / +6) | −14 (−25 / −3) |
| Cari denge ($ mn) | −4 (−8 / −1) | −4 (−7 / −2) | −9 (−13 / −6) |
| Üretim ($ mn) | −5 (−10 / −2) | −5 (−9 / −2) | −11 (−17 / −7) |
| İstihdam (kişi) | −7 (−13 / −2) | −7 (−12 / −3) | −14 (−23 / −9) |
| TÜFE (bp, birinci tur) | +0,01 (+0,01 / +0,01) | +0,02 (+0,01 / +0,02) | +0,05 (+0,04 / +0,06) |
| Yatırım ve DYY (bütün senaryolar) | S4'te çapa yatırımcının AB'ye yönelik kapasite kararı riski `[H]` |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**11. Müzakere pozisyonu**

- AB ile savunma: S2'de İTÜ'de sanayi bileşeninin sıfırı (bugünkü durumun sürmesi); 1702 için başlık değişikliği kuralı.

**12. Erken uyarı ve tetikler**

| Gösterge | Eşik | Tetiklenecek önlem |
|---|---|---|
| AB'ye glikoz ve fruktoz ihracatı (aylık) | Yıllık −%20 | E-10-05 tamponu |

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Kaybeden (S4): Bursa (Orhangazi), Adana; P50'de −14 kişi (sermaye yoğun).

**14. Riskler ve azaltım**

- Çapa yatırımcının S4'te AB arzını kaydırması → S2 önceliği.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Orta (çapa yatırımcı davranışı `[H]`).


### 3.14 10.71 Ekmek, taze pastane ürünleri ve taze kek imalatı — GB statüsü: İTÜ | Birincil/ikincil arketip: —/D | Duruş: Koru

*İç pazara dönük en büyük gıda işvereni (190 bin kişi, çoğu küçük fırın). Dondurulmuş hamur ürünü ihracatı AB'ye $50 mn; S4'te %9 sanayi bileşeni, S2'de menşe (un) sorunu.*

**1. Kimlik.** Rev. 2.1: 10.71 (n:1); CPA 10.71. Başlıca HS4 (TR ihracatı 2024): 1905 %100. BEC payları (ticaret ağırlıklı): ara %0 / sermaye %0 / tüketim %100.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $6.566 mn; $2.097 mn (GSYH'nin %0,15) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 189.869; 33.744 (524 / 31.889 / 3.178 / 304 / 40) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %5; — | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İstanbul %11; İzmir %8; Kocaeli, Sakarya, Düzce, Bolu, Yalova %7 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Uno, Simit Sarayı, Ülker (Bizim), dondurulmuş hamurda Hacıbaba, Yuvam `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $264 mn; %62 |
| AB payı; ilk 5 AB pazarı | %19; DEU %40; NLD %11; BEL %10; ROU %9; BGR %8 |
| İlk 5 AB dışı pazar | IRQ %32; USA %8; AZE %5; YEM %5; LBY %4 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $29 mn; AB %61, Çin %1; MYS %30; POL %21; CZE %8; BEL %7; DEU %6 |
| Dış ticaret dengesi | $+235 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %32 |
| RCA dünya (2020 → 2024) / AB pazarında | 1,54 → 1,45 / 2,06 |
| Birim değer ÷ AB pazarı ortalaması | 0,89 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %6,0 → %8,2; 2. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %9,0; 1/98 kaybıyla %9,0; tam MFN ortalaması %9,0. Rejim: GB %0, İTÜ %100, tarım %0 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): GBR %43; CHN %6; CHE %5; SRB %4; THA %3. Tercihli rakip payı %66.
- Menşe (S2 / S3): risk O/O; `c_RoO` %3,0 / %3,5; `p_uyum` 0,80 / 0,75 `[H]`. Kural: 1905: Fasıl 11 malzemesi kullanılamaz (un menşeli olmalı; DİR'deki Rus buğdayı unu menşesiz).
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.
- S2'de menşe: Fasıl 11 malzemesi kullanılamıyor; DİR'deki Rus buğdayı unu menşesiz. S2'nin kaybı (−$11 mn AB ihracatı) S4'ünkinin (−$16 mn) üçte ikisinden fazla.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %7,1, İGV dahil %7,1 `[V]`. S4'te AB menşeline (c2): %7,1.
- Kritik girdiler (HS4 1001, 1101), Türkiye'nin toplam ithalatı 2024: $1.302 mn (AB %1; RUS %87, UKR %10, SYR %1) `[V]`.

**6. Kabiliyet**

- KS 55,5 (sıra 57/230; ağırlık duyarlılığında P10–P90 19–122). Bileşenler: RCA 47, PCI 38 (PCI −0,18), yurt içi KD 79, Ar-Ge 25, tedarikçi 84, verimlilik —, firma 90 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.
- **Kırmızı çizgi yetkinlikleri:** Ekmeklik buğday unu arzı ve fiyat istikrarı (Halk Ekmek ve belediye fırınları).

**7. Stratejik önem.** SS 67,0 (en yüksek boyut: gıda güvenliği 90; ağırlıklı ortalama 13,5) `[H]`. Ekmek en geniş tabanlı temel gıda; fiyatı belediye düzenlemesine tabi.

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %2,37; %2 |
| ÜFE vekili (imalat üretimindeki pay) | %0,98 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,052 / 0,032 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %5 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 184,8 ve 0,56; 13 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −11 (−25 / +1) | −12 (−22 / −2) | −16 (−25 / −7) |
| Toplam ihracat ($ mn) | −8 (−18 / +1) | −8 (−16 / −2) | −12 (−20 / −5) |
| Nihai mal ithalatı ($ mn) | −1 (−4 / +1) | −2 (−4 / +1) | −3 (−5 / −1) |
| Cari denge ($ mn) | −5 (−11 / 0) | −5 (−9 / −2) | −8 (−12 / −4) |
| Üretim ($ mn) | −7 (−14 / −1) | −6 (−12 / −2) | −9 (−15 / −5) |
| İstihdam (kişi) | −131 (−294 / −12) | −130 (−237 / −47) | −189 (−310 / −92) |
| TÜFE (bp, birinci tur) | +0,04 (+0,03 / +0,05) | +0,08 (+0,06 / +0,09) | +0,21 (+0,18 / +0,24) |
| Yatırım ve DYY (bütün senaryolar) | Etkisi yok |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**12. Erken uyarı ve tetikler**

| Gösterge | Eşik | Tetiklenecek önlem |
|---|---|---|
| Ekmek ve tahıl TÜFE alt endeksi | 3 ay üst üste genel TÜFE + 5 puan | TMO'dan değirmenlere satış fiyatı ayarı |

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** S4'te küçük kayıp (P50 −189 kişi; emek yoğun, kişi başı üretim düşük). Bölge: İstanbul (%11), İzmir.

**14. Riskler ve azaltım**

- Menşe uyumlu DİR uygulanmazsa S2'de dondurulmuş ürün ihracatı kaybı → E-10-02.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Orta (sınıf üretimi YSHİ'de geniş: küçük fırınlar).


### 3.15 10.72 Peksimet ve bisküvi imalatı; dayanıklı pastane ürünleri ve dayanıklı kek imalatı — GB statüsü: İTÜ | Birincil/ikincil arketip: B | Duruş: Geliştir

*Küresel rekabetçi (bisküvide dünya sekizincisi), AB payı %14. S4'te %9 sanayi bileşeniyle AB'ye ihracat −$51 mn. S2'de menşe kuralı (yerli un) kaybın üçte ikisinden fazlasını bırakıyor; çözüm DİR'de eşdeğer eşya ve PSR.*

**1. Kimlik.** Rev. 2.1: 10.72 (n:1); CPA 10.72. Başlıca HS4 (TR ihracatı 2024): 1905 %100. BEC payları (ticaret ağırlıklı): ara %0 / sermaye %0 / tüketim %100.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $5.738 mn; $1.548 mn (GSYH'nin %0,11) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 42.160; 5.211 (70 / 5.139 / 242 / 32 / 11) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %43; 0,78 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İstanbul %16; Konya, Karaman %15; Bursa, Eskişehir, Bilecik %15 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Ülker (Yıldız Holding/pladis), Eti, Şölen, Tayaş, Elvan, Bifa, Torku `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $1.174 mn; %45 |
| AB payı; ilk 5 AB pazarı | %14; DEU %32; BEL %19; ROU %11; NLD %9; POL %7 |
| İlk 5 AB dışı pazar | IRQ %33; SAU %6; USA %5; LBY %4; GBR %4 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $89 mn; AB %75, Çin %0; ITA %19; DEU %15; POL %13; UKR %8; MYS %7 |
| Dış ticaret dengesi | $+1.085 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %27 |
| RCA dünya (2020 → 2024) / AB pazarında | 3,52 → 3,10 / 3,15 |
| Birim değer ÷ AB pazarı ortalaması | 0,95 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %9,4 → %12,6; 2. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %9,0; 1/98 kaybıyla %9,0; tam MFN ortalaması %9,0. Rejim: GB %0, İTÜ %100, tarım %0 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok (AB ihracatının %1'inden az).
- AB pazarında AB dışı rakipler (tercih durumu): GBR %40; UKR %10; SRB %5; CHE %4; THA %4. Tercihli rakip payı %65.
- Menşe (S2 / S3): risk O/O; `c_RoO` %3,0 / %3,5; `p_uyum` 0,80 / 0,75 `[H]`. Kural: 1905: Fasıl 11 malzemesi kullanılamaz (un menşeli olmalı); şeker ağırlık sınırı.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.
- Menşe kuralı: 1905'te Fasıl 11 malzemesi kullanılamaz ve şeker ağırlık sınırı var. İhracatçıların DİR'de ithal buğday ve şeker kullanması bugün sorun değil, çünkü GB'de serbest dolaşım için A.TR yeterli.
- AB pazarındaki AB dışı rakiplerin hepsi tercihli: İngiltere (TCA), Ukrayna (DCFTA), Sırbistan (İOA). S4'te Türkiye bu grupta MFN ödeyen tek büyük tedarikçi olur.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %8,5, İGV dahil %9,7 `[V]`. S4'te AB menşeline (c2): %9,8.
- Kritik girdiler (HS4 1001, 1101, 1701, 1804), Türkiye'nin toplam ithalatı 2024: $2.015 mn (AB %15; RUS %56, MAR %11, BGR %9) `[V]`.
- Girdiler: buğday (DİR'de Rusya), şeker (DİR'de ham kamış şekeri), kakao yağı ve tozu (AB'den; S4'te %7,7–9,6). S4'te kakao ara ürünlerinde MFN %0 (E-10.82-01) bu sınıfa da yarıyor.

**6. Kabiliyet**

- KS 54,9 (sıra 64/230; ağırlık duyarlılığında P10–P90 23–121). Bileşenler: RCA 67, PCI 25 (PCI −0,49), yurt içi KD 66, Ar-Ge 25, tedarikçi 84, verimlilik 89, firma 55 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.
- **Kırmızı çizgi yetkinlikleri:** Marka ve ambalaj tasarımı, raf ömrü teknolojisi, Irak ve Körfez'deki dağıtım ağları.
- **Geliştirme hedefi:** T+5: AB ihracatı ≥ T−12 düzeyi (menşe çözümüyle); 2035: Kuzey Amerika'da marka payı.

**7. Stratejik önem.** SS 22,4 (en yüksek boyut: gıda güvenliği 30; ağırlıklı ortalama 4,5) `[H]`. 

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %1,02; %2 |
| ÜFE vekili (imalat üretimindeki pay) | %0,86 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,026 / 0,019 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %43 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 1.103,7 ve 2,27; 25 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −35 (−78 / +3) | −37 (−69 / −7) | −51 (−81 / −21) |
| Toplam ihracat ($ mn) | −25 (−58 / +2) | −26 (−50 / −5) | −40 (−66 / −17) |
| Nihai mal ithalatı ($ mn) | −5 (−15 / +5) | −7 (−17 / +3) | −13 (−24 / −3) |
| Cari denge ($ mn) | −16 (−34 / −2) | −16 (−27 / −6) | −21 (−34 / −11) |
| Üretim ($ mn) | −20 (−43 / −3) | −20 (−34 / −8) | −27 (−43 / −14) |
| İstihdam (kişi) | −104 (−218 / −13) | −99 (−174 / −40) | −135 (−221 / −70) |
| TÜFE (bp, birinci tur) | +0,03 (+0,02 / +0,03) | +0,05 (+0,05 / +0,06) | +0,17 (+0,15 / +0,19) |
| Yatırım ve DYY (bütün senaryolar) | Yıldız Holding'in yurt dışı (pladis) tesisleri AB arzını karşılayabilir: S4'te üretim kayması riski `[H]` |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**10. Politika paketi**

| Eylem ID | Araç | Parametre | Sorumlu | Hukuki araç | Bütçe | Başlangıç–bitiş; sunset | Performans koşulu | KPI |
|---|---|---|---|---|---|---|---|---|
| E-10.72-01 | Fasıl 19 PSR talebi | 1905: 'başlık değişikliği; menşesiz tahıl ve un fabrika çıkış fiyatının %15'ine kadar' (genel toleransla uyumlu) | Ticaret Bakanlığı (Uluslararası Anlaşmalar ve AB GM) | S2 menşe protokolü | İdari | T−18 → T; sunset: — | — | Kabul edilen PSR |

**11. Müzakere pozisyonu**

- AB ile savunma: İTÜ'de sanayi bileşeninin sıfırı sürsün; Fasıl 19 PSR toleransı ya da eşdeğer eşya kabulü.
- Üçüncü ülke: Körfez STA'sında bisküvi ve şekerlemede sıfır.

**12. Erken uyarı ve tetikler**

| Gösterge | Eşik | Tetiklenecek önlem |
|---|---|---|
| AB'ye bisküvi ihracatında menşe ispatlı pay (S2'den sonra) | < %80 | E-10-02 kapsamı genişletilir; TMO yerli buğday arzı |
| AB'ye bisküvi ihracatı (aylık; S4) | Yıllık −%20 | E-10-05 |

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Kaybeden (S4 P50): −135 kişi; bölgeler İstanbul, Konya–Karaman (Torku, Eti Karaman `[H]`), Bursa–Eskişehir (Eti). Telafi: E-10-05.

**14. Riskler ve azaltım**

- Üretimin pladis'in AB içindeki tesislerine kayması → S2 önceliği ve E-10-02.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Orta (c_RoO ve yerli buğday fiyat farkı `[T]`; VB-33).


### 3.16 10.73 Makarna, şehriye, kuskus ve benzeri unlu mamullerin imalatı — GB statüsü: İTÜ | Birincil/ikincil arketip: B/D | Duruş: Geliştir

*Makarnada dünya ikincisi (%12,3; tonajda dörtte bir). İhracatın %98'i AB dışına (Afrika, Venezuela, Japonya). GB etkisi küçük; menşe kuralı ithal makarnalık buğdaya izin veriyor (D).*

**1. Kimlik.** Rev. 2.1: 10.73 (n:1); CPA 10.73. Başlıca HS4 (TR ihracatı 2024): 1902 %100. BEC payları (ticaret ağırlıklı): ara %0 / sermaye %0 / tüketim %100.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $1.959 mn; $409 mn (GSYH'nin %0,03) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 7.040; 429 (40 / 391 / 28 / 11 / 7) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %58; — | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | Konya, Karaman %23; Adana, Mersin %16; Gaziantep, Adıyaman, Kilis %15 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Filiz, Nuh'un Ankara, Oba, Selva, Barilla (Bursa), Pastavilla, Durum Gıda `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $852 mn; %20 |
| AB payı; ilk 5 AB pazarı | %2; DEU %35; NLD %14; FRA %9; AUT %8; POL %6 |
| İlk 5 AB dışı pazar | SOM %15; GHA %9; VEN %9; JPN %8; TGO %6 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $17 mn; AB %86, Çin %7; ITA %82; CHN %7; ROU %3; EGY %2; LBN %1 |
| Dış ticaret dengesi | $+835 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %21 |
| RCA dünya (2020 → 2024) / AB pazarında | 10,68 → 9,09 / 2,63 |
| Birim değer ÷ AB pazarı ortalaması | 0,55 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %9,4 → %10,5; 3. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %7,7; 1/98 kaybıyla %7,7; tam MFN ortalaması %34,2. Rejim: GB %0, İTÜ %100, tarım %0 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): MAR %19; VNM %11; THA %10; CHN %10; GBR %6. Tercihli rakip payı %58.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 1902: tahıl tamamen elde edilmiş, makarnalık buğday ve türevleri hariç (ithal durum serbest).
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %7,7, İGV dahil %15,0 `[V]`. S4'te AB menşeline (c2): %14,8.
- Kritik girdiler (HS4 1001), Türkiye'nin toplam ithalatı 2024: $1.293 mn (AB %1; RUS %87, UKR %10, SYR %1) `[V]`.
- Makarnalık buğday ithalatı (Kanada, Rusya, Kazakistan) DİR'de. GB'den bağımsız.

**6. Kabiliyet**

- KS 42,5 (sıra 187/230; ağırlık duyarlılığında P10–P90 110–216). Bileşenler: RCA 73, PCI 3 (PCI −1,59), yurt içi KD 53, Ar-Ge 25, tedarikçi 84, verimlilik —, firma 28 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.
- **Kırmızı çizgi yetkinlikleri:** Durum işleme ve kurutma teknolojisi; Afrika dağıtım ağları.
- **Geliştirme hedefi:** T+5: Afrika Kıtasal Serbest Ticaret Bölgesi üyeleriyle STA'lar; 2035: makarnada dünya birinciliği (tonaj).

**7. Stratejik önem.** SS 52,1 (en yüksek boyut: gıda güvenliği 70; ağırlıklı ortalama 10,5) `[H]`. Makarna: temel ve ucuz karbonhidrat

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,21; %2 |
| ÜFE vekili (imalat üretimindeki pay) | %0,29 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,005 / 0,004 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %58 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 594,7 ve 0,99; 20 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −2 (−4 / 0) | −2 (−4 / 0) | −4 (−6 / −2) |
| Toplam ihracat ($ mn) | −1 (−3 / 0) | −1 (−3 / 0) | −3 (−5 / −1) |
| Nihai mal ithalatı ($ mn) | −1 (−2 / +1) | −1 (−3 / +1) | −2 (−4 / −1) |
| Cari denge ($ mn) | 0 (−1 / 0) | 0 (−1 / 0) | 0 (−1 / 0) |
| Üretim ($ mn) | −1 (−1 / 0) | 0 (−1 / 0) | −1 (−1 / 0) |
| İstihdam (kişi) | −1 (−2 / 0) | −1 (−2 / 0) | −1 (−2 / 0) |
| TÜFE (bp, birinci tur) | +0,01 (+0,01 / +0,01) | +0,01 (+0,01 / +0,02) | +0,06 (+0,05 / +0,06) |
| Yatırım ve DYY (bütün senaryolar) | Etkisi yok |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** GB'den etkilenen yok.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Yüksek.


### 3.17 10.81 Şeker imalatı — GB statüsü: TARIM-1/98 | Birincil/ikincil arketip: — | Duruş: Koru

*Kotalı iç pazar (Şeker Kanunu); ihracat küçük. GB etkisi yok; ham şeker ithalatı (Fas, Brezilya) DİR'de.*

**1. Kimlik.** Rev. 2.1: 10.81 (1:1); CPA 10.81. Başlıca HS4 (TR ihracatı 2024): 1701 %86, 2303 %13, 1703 %0, 1702 %0. BEC payları (ticaret ağırlıklı): ara %15 / sermaye %0 / tüketim %85.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $3.202 mn; $803 mn (GSYH'nin %0,06) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 15.900; 24 (0 / 8 / 0 / 3 / 30) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %98; 0,26 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | Manisa, Afyon, Kütahya, Uşak %21; Konya, Karaman %18; Samsun, Tokat, Çorum, Amasya %13 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Türkiye Şeker Fabrikaları (özelleştirilmiş tesisler), Konya Şeker (Torku), Kayseri Şeker `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $143 mn; %426 |
| AB payı; ilk 5 AB pazarı | %10; ESP %44; GRC %30; ITA %15; IRL %7; BGR %2 |
| İlk 5 AB dışı pazar | SYR %50; IRQ %35; GEO %5; MAR %4; CYP %2 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $458 mn; AB %10, Çin %0; MAR %50; BRA %15; RUS %12; UKR %8; POL %3 |
| Dış ticaret dengesi | $−315 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %25 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,09 → 0,27 / 0,23 |
| Birim değer ÷ AB pazarı ortalaması | 1,00 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,0 → %0,9; 21. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %0,3; tam MFN ortalaması %0,3. Rejim: GB %0, İTÜ %0, tarım %100 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): BRA %19; UKR %14; GBR %7; EGY %7; CAN %6. Tercihli rakip payı %68.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 1701: Fasıl 17 malzemesi menşeli.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %116,8, İGV dahil %116,8 `[V]`. S4'te AB menşeline (c2): %0,0.
- Kritik girdiler (HS4 1701), Türkiye'nin toplam ithalatı 2024: $389 mn (AB %12; MAR %59, BRA %18, UKR %9) `[V]`.
- Şeker fiyatı İTÜ ihracatçıları için menşe maliyeti: yerli pancar şekeri dünya fiyatının üzerinde. Bu yüzden 10.72 ve 10.82 DİR'de ham kamış şekeri kullanıyor.

**6. Kabiliyet**

- KS 33,5 (sıra 223/230; ağırlık duyarlılığında P10–P90 195–228). Bileşenler: RCA 39, PCI 11 (PCI −0,94), yurt içi KD 62, Ar-Ge 25, tedarikçi 84, verimlilik 8, firma 12 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.

**7. Stratejik önem.** SS 52,6 (en yüksek boyut: gıda güvenliği 70; ağırlıklı ortalama 12,0) `[H]`. Şeker; pancar üreticisi; melastan biyoetanol

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,35; %16 |
| ÜFE vekili (imalat üretimindeki pay) | %0,48 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,092 / 0,009 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %98 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 306,3 ve 3,21; 20 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (0 / +3) | 0 (0 / +2) | 0 (0 / 0) |
| Cari denge ($ mn) | 0 (−2 / 0) | 0 (−1 / 0) | 0 (0 / 0) |
| Üretim ($ mn) | 0 (−3 / 0) | 0 (−2 / 0) | 0 (0 / 0) |
| İstihdam (kişi) | 0 (−9 / 0) | 0 (−6 / 0) | 0 (0 / 0) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Etkilenen kesim yok.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Yüksek.


### 3.18 10.82 Kakao, çikolata ve şekerleme imalatı — GB statüsü: İTÜ | Birincil/ikincil arketip: B/G | Duruş: Geliştir

*Küresel rekabetçi ihracatçı ($2,0 mlr; AB payı %14). S4'te AB'ye ihracat −$84 mn, ama AB'den kakao ara ürünü ithalatı ($474 mn) %8 tarifeye girdiği için iç ikame artı yazıyor. Doğru politika girdide sıfır: kakao yağı, tozu ve hamurunda MFN %0.*

**1. Kimlik.** Rev. 2.1: 10.82 (1:1); CPA 10.82. Başlıca HS4 (TR ihracatı 2024): 1806 %46, 1704 %45, 1805 %5, 1804 %3. BEC payları (ticaret ağırlıklı): ara %33 / sermaye %0 / tüketim %67.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $6.016 mn; $1.645 mn (GSYH'nin %0,12) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 36.835; 2.055 (111 / 1.700 / 283 / 64 / 32) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %51; 0,69 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İstanbul %36; Konya, Karaman %8; Manisa, Afyon, Kütahya, Uşak %8 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Ülker (Yıldız), Eti, Şölen, Kervan, Elvan, Tayaş, Nestlé (Bursa), Mondelez (Bursa `[D?]`) `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $2.032 mn; %78 |
| AB payı; ilk 5 AB pazarı | %14; DEU %25; NLD %11; ROU %11; BGR %8; GRC %6 |
| İlk 5 AB dışı pazar | IRQ %14; USA %13; GBR %7; SAU %5; RUS %5 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $963 mn; AB %73, Çin %1; BGR %26; NLD %16; DEU %11; BEL %9; GHA %6 |
| Dış ticaret dengesi | $+1.069 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %27 |
| RCA dünya (2020 → 2024) / AB pazarında | 2,03 → 1,97 / 0,79 |
| Birim değer ÷ AB pazarı ortalaması | 0,94 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %2,8 → %3,1; 8. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %8,4; 1/98 kaybıyla %8,4; tam MFN ortalaması %8,8. Rejim: GB %0, İTÜ %100, tarım %0 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok (AB ihracatının %1'inden az).
- AB pazarında AB dışı rakipler (tercih durumu): CIV %29; GBR %14; CHE %11; GHA %9; CMR %6. Tercihli rakip payı %79.
- Menşe (S2 / S3): risk O/O; `c_RoO` %2,5 / %3,5; `p_uyum` 0,85 / 0,75 `[H]`. Kural: 1704 ve 1806: başlık değişikliği; menşesiz şeker ve Fasıl 4 malzemesi ağırlıkça %40 (birlikte %60) sınırı.
- EUDR kapsamındaki AB ihracatı payı: %62; SKDM: %0.
- EUDR: AB ihracatının %62'si EUDR kapsamında (1806, 1803–1805). 30.12.2026'dan itibaren orta ve büyük AB operatörleri, kakaonun yetiştirildiği parselin coğrafi konumunu istiyor `[V]` (Tüzük 2025/2650). GB çıkışından bağımsız, ama hasmane AB'de uygulama sıkılığı artabilir `[H]`.
- AB pazarında rakipler Fildişi Sahili ve Gana (EPA; kakao ürünleri), İngiltere ve İsviçre (çikolata). Hepsi tercihli; tercihli rakip payı %79.
- Menşe: başlık değişikliği, menşesiz şeker ve Fasıl 4 ağırlık sınırı %40. DİR'deki ham şekerle yapılan şekerlemelerde sınır aşılıyor (O).

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %8,5, İGV dahil %8,6 `[V]`. S4'te AB menşeline (c2): %8,5.
- Kritik girdiler (HS4 1801, 1803, 1804, 1805, 1701), Türkiye'nin toplam ithalatı 2024: $1.539 mn (AB %34; CIV %21, BGR %16, MAR %15) `[V]`.
- S4'te AB'den kakao yağı (1804; $254 mn), kakao tozu (1805; $149 mn) ve kakao hamurunun (1803; $70 mn) tarifesi %7,7–9,6. Bunlar ihracatçının girdisi. Yerli öğütme kapasitesi bu talebin tamamını karşılayamaz `[D?]`. Matristeki üretim artışı (S4 P50 +56 $ mn) bu yüzden üst sınır.
- Fildişi Sahili ve Gana'dan doğrudan kakao ürünü ithalatı bugün %7,7–9,6 MFN ödüyor (AB'nin EPA'sı var, Türkiye'nin yok). Çıkış girdide sıfırı mümkün kılıyor: özerklik temettüsü.

**6. Kabiliyet**

- KS 55,5 (sıra 56/230; ağırlık duyarlılığında P10–P90 24–109). Bileşenler: RCA 62, PCI 34 (PCI −0,27), yurt içi KD 67, Ar-Ge 25, tedarikçi 84, verimlilik 86, firma 54 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.
- **Kırmızı çizgi yetkinlikleri:** Fındık–kakao harman bilgisi ve marka; çikolata kalıplama ve kaplama hatları; helal ve Körfez dağıtımı.
- **Geliştirme hedefi:** T+5: kakaoyu doğrudan kaynaktan (Batı Afrika) alarak maliyette −%3; 2035: premium segmentte AB dışı (ABD, Körfez) marka payı.

**7. Stratejik önem.** SS 7,5 (en yüksek boyut: gıda güvenliği 10; ağırlıklı ortalama 1,5) `[H]`. 

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,61; %7 |
| ÜFE vekili (imalat üretimindeki pay) | %0,90 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,114 / 0,084 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %51 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 2.661,9 ve 24,12; 57 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −52 (−123 / +5) | −64 (−121 / −13) | −84 (−137 / −36) |
| Toplam ihracat ($ mn) | −38 (−90 / +4) | −45 (−86 / −9) | −67 (−110 / −28) |
| Nihai mal ithalatı ($ mn) | −44 (−147 / +48) | −63 (−164 / +28) | −123 (−225 / −26) |
| Cari denge ($ mn) | +3 (−35 / +50) | +13 (−30 / +64) | +44 (−2 / +94) |
| Üretim ($ mn) | +3 (−44 / +63) | +16 (−37 / +80) | +56 (−2 / +117) |
| İstihdam (kişi) | +15 (−185 / +266) | +71 (−159 / +341) | +233 (−11 / +494) |
| TÜFE (bp, birinci tur) | +0,11 (+0,10 / +0,14) | +0,22 (+0,18 / +0,26) | +0,64 (+0,55 / +0,73) |
| Yatırım ve DYY (bütün senaryolar) | Nestlé ve Mondelez'in AB'ye yönelik üretim kararı S2'ye duyarlı `[H]` |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**10. Politika paketi**

| Eylem ID | Araç | Parametre | Sorumlu | Hukuki araç | Bütçe | Başlangıç–bitiş; sunset | Performans koşulu | KPI |
|---|---|---|---|---|---|---|---|---|
| E-10.82-01 | Girdide sıfır: kakao ara ürünleri | KN 1803–1805'te MFN %7,7–9,6 → %0, tüm menşeler (T'den itibaren; S2'de de) | Ticaret Bakanlığı | İthalat Rejimi Kararı eki (Cumhurbaşkanı kararı) | Gelir kaybı ≈ 0,55 mlr TL/yıl (AB dışı kakao ürünü ithalatı × %8) `[T]` | T → kalıcı; sunset: Yok | Yurt içi çikolata fiyatında geçiş (izleme) | TÜFE çikolata alt endeksi; S4'te −0,36 bp |
| E-10.82-02 | Menşe uyumlu şeker | AB'ye yönelik şekerlemede yerli pancar şekerinin DİR'de eşdeğer eşya olarak kullanımı (E-10-02) | Ticaret Bakanlığı, Şeker Kurumu | DİR Tebliği | ≈ 0 | T−12 → T+60; sunset: T+60 | — | AB'ye şekerleme ihracatında menşe ispatlı pay ≥ %85 |

**11. Müzakere pozisyonu**

- AB ile savunma: İTÜ sanayi bileşeninin sıfırı; 1704 ve 1806'da şeker ağırlık sınırına %15 tolerans.
- Üçüncü ülke: Fildişi Sahili ve Gana ile kakao ürünlerinde sıfır tarifeli STA ya da tek taraflı sıfır; Körfez STA'sında çikolata.

**12. Erken uyarı ve tetikler**

| Gösterge | Eşik | Tetiklenecek önlem |
|---|---|---|
| AB'ye çikolata ve şekerleme ihracatı (aylık) | Yıllık −%15 | E-10-05 |
| EUDR nedeniyle AB'de bekletilen sevkiyat | ≥ 3 vaka | E-10-03: tedarikçi veri havuzu |

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Kazanan (S4): kakao öğütücüleri ve iç pazara satan üreticiler (P50 +233 kişi). Kaybeden: AB'ye ihracatçılar. Bölgeler: İstanbul (%36), Konya–Karaman, Manisa.

**14. Riskler ve azaltım**

- Girdide sıfırın yerli kakao öğütücülerine etkisi → kademeli geçiş (T+12'ye kadar %4).
- EUDR uyumsuzluğu → E-10-03.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Orta (iç ikamenin kapasite sınırı `[D?]`; EUDR uygulama sıkılığı `[H]`).


### 3.19 10.83 Kahve ve çayın işlenmesi — GB statüsü: KARMA | Birincil/ikincil arketip: — | Duruş: Koru

*Çay (yerli; Çaykur) ve kahve (ithal). AB'den hazır kahve ithalatı ($93 mn) S4'te %9; TÜFE 0,4 bp. GB'nin ihracat etkisi küçük.*

**1. Kimlik.** Rev. 2.1: 10.83 (1:1); CPA 10.83. Başlıca HS4 (TR ihracatı 2024): 2101 %51, 0901 %31, 0902 %18. BEC payları (ticaret ağırlıklı): ara %0 / sermaye %0 / tüketim %100.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $3.787 mn; $1.042 mn (GSYH'nin %0,08) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 19.999; 1.018 (99 / 850 / 129 / 18 / 9) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %63; 0,57 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İstanbul %40; Trabzon, Ordu, Giresun, Rize, Artvin, Gümüşhane %19; Adana, Mersin %11 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Çaykur (kamu), Doğuş Çay, Lipton Teas and Infusions, Kurukahveci Mehmet Efendi, Nestlé, JDE `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $170 mn; %109 |
| AB payı; ilk 5 AB pazarı | %23; DEU %50; BEL %19; NLD %13; FRA %5; ROU %3 |
| İlk 5 AB dışı pazar | IRQ %17; BLR %10; SYR %8; IRN %6; GBR %6 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $364 mn; AB %60, Çin %0; ESP %15; DEU %12; CHE %10; NLD %9; IND %8 |
| Dış ticaret dengesi | $−194 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %28 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,32 → 0,44 / 0,29 |
| Birim değer ÷ AB pazarı ortalaması | 0,74 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,8 → %1,1; 11. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %3,2; 1/98 kaybıyla %4,8; tam MFN ortalaması %4,8. Rejim: GB %0, İTÜ %41, tarım %59 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): 4 satır, AB ihracatının %13'i: KN 2101 12 92 %11,5 (€4,2 mn); KN 2101 30 11 %11,5 (€0,1 mn); KN 2101 30 91 %14,1 (€0,1 mn).
- AB pazarında AB dışı rakipler (tercih durumu): CHE %47; GBR %14; VNM %9; BRA %5; IND %4. Tercihli rakip payı %82.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 0901 ve 2101: başlık değişikliği; ithal kahve çekirdeğinden kavrulmuş/hazır kahve menşe kazanır.
- EUDR kapsamındaki AB ihracatı payı: %20; SKDM: %0.
- EUDR: AB ihracatının %20'si (kavrulmuş kahve) kapsamda.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %11,2, İGV dahil %11,2 `[V]`. S4'te AB menşeline (c2): %4,6.
- Kritik girdiler (HS4 0901, 0902), Türkiye'nin toplam ithalatı 2024: $578 mn (AB %18; BRA %58, LKA %8, NLD %5) `[V]`.

**6. Kabiliyet**

- KS 44,4 (sıra 172/230; ağırlık duyarlılığında P10–P90 115–197). Bileşenler: RCA 39, PCI 17 (PCI −0,76), yurt içi KD 68, Ar-Ge 25, tedarikçi 84, verimlilik 72, firma 37 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.

**7. Stratejik önem.** SS 22,4 (en yüksek boyut: gıda güvenliği 30; ağırlıklı ortalama 4,5) `[H]`. Çay (yerli) ve kahve (ithal)

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %1,04; %14 |
| ÜFE vekili (imalat üretimindeki pay) | %0,57 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,178 / 0,106 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %63 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 388,1 ve 6,50; 25 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −1 (−3 / +1) | −2 (−4 / 0) | −4 (−7 / −2) |
| Toplam ihracat ($ mn) | −1 (−3 / +1) | −1 (−3 / 0) | −3 (−6 / −1) |
| Nihai mal ithalatı ($ mn) | −5 (−15 / +15) | −7 (−18 / +9) | −17 (−31 / −4) |
| Cari denge ($ mn) | +3 (−12 / +10) | +5 (−7 / +12) | +11 (+2 / +20) |
| Üretim ($ mn) | +4 (−15 / +13) | +6 (−9 / +16) | +13 (+2 / +25) |
| İstihdam (kişi) | +13 (−54 / +47) | +21 (−33 / +56) | +49 (+8 / +93) |
| TÜFE (bp, birinci tur) | +0,08 (+0,07 / +0,09) | +0,15 (+0,13 / +0,18) | +0,44 (+0,38 / +0,50) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** S4'te iç ikame kazancı küçük (+49 kişi).

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Yüksek.


### 3.20 10.84 Baharat, sos, sirke ve diğer çeşni maddelerinin imalatı — GB statüsü: KARMA | Birincil/ikincil arketip: A | Duruş: Geliştir

*Baharat, sos ve sirke: AB payı %34. AB'ye $83 mn ihracat, S4'te %4,9 (ketçapta %10,2). SPS kontrolleri (kalıntı) GB'den bağımsız risk.*

**1. Kimlik.** Rev. 2.1: 10.84 (1:1); CPA 10.84. Başlıca HS4 (TR ihracatı 2024): 2103 %54, 0910 %20, 2501 %9, 0904 %9. BEC payları (ticaret ağırlıklı): ara %7 / sermaye %0 / tüketim %93.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $1.244 mn; $296 mn (GSYH'nin %0,02) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 7.151; 659 (29 / 558 / 96 / 24 / 2) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %11; 0,55 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İstanbul %14; İzmir %13; Gaziantep, Adıyaman, Kilis %8 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Tat (ketçap ve sos), Kühne (Almanya; sos), Bağdat Baharat; defne ve kekikte Ege ihracatçıları `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $242 mn; %38 |
| AB payı; ilk 5 AB pazarı | %34; DEU %34; BEL %16; NLD %9; FRA %8; ROU %5 |
| İlk 5 AB dışı pazar | USA %17; GBR %13; IRQ %11; SYR %3; CAN %3 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $90 mn; AB %40, Çin %5; IDN %16; GBR %11; ITA %8; NLD %7; HUN %7 |
| Dış ticaret dengesi | $+153 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %24 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,85 → 0,78 / 1,01 |
| Birim değer ÷ AB pazarı ortalaması | 0,98 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %3,0 → %4,0; 7. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %4,9; 1/98 kaybıyla %7,4; tam MFN ortalaması %7,4. Rejim: GB %11, İTÜ %56, tarım %33 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): 1 satır, AB ihracatının %23'i: KN 2103 20 00 %10,2 (€13,6 mn).
- AB pazarında AB dışı rakipler (tercih durumu): GBR %23; CHN %14; THA %11; USA %6; VNM %5. Tercihli rakip payı %49.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,5; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 2103 ve 2209: başlık değişikliği (hardal unu istisnası).
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.
- Kekik, defne ve kimyonda kalıntı ve aflatoksin kaynaklı RASFF bildirimleri GB'den bağımsız bir engel `[D?]`.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %12,4, İGV dahil %12,4 `[V]`. S4'te AB menşeline (c2): %5,0.
- Kritik girdiler (HS4 0904, 0909, 0910), Türkiye'nin toplam ithalatı 2024: $108 mn (AB %6; SYR %31, VNM %16, CHN %14) `[V]`.

**6. Kabiliyet**

- KS 42,3 (sıra 192/230; ağırlık duyarlılığında P10–P90 133–208). Bileşenler: RCA 30, PCI 12 (PCI −0,92), yurt içi KD 59, Ar-Ge 25, tedarikçi 84, verimlilik 69, firma 60 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.

**7. Stratejik önem.** SS 22,4 (en yüksek boyut: gıda güvenliği 30; ağırlıklı ortalama 4,5) `[H]`. 

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,28; %6 |
| ÜFE vekili (imalat üretimindeki pay) | %0,19 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,023 / 0,009 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %11 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 861,7 ve 6,88; 30 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −6 (−14 / +2) | −8 (−16 / −2) | −14 (−24 / −6) |
| Toplam ihracat ($ mn) | −4 (−10 / +1) | −6 (−11 / −1) | −11 (−19 / −5) |
| Nihai mal ithalatı ($ mn) | −1 (−4 / +2) | −2 (−5 / +1) | −3 (−6 / −1) |
| Cari denge ($ mn) | −2 (−5 / −1) | −3 (−5 / −2) | −6 (−10 / −3) |
| Üretim ($ mn) | −3 (−6 / −1) | −4 (−7 / −2) | −8 (−13 / −4) |
| İstihdam (kişi) | −10 (−24 / −5) | −14 (−26 / −9) | −31 (−54 / −16) |
| TÜFE (bp, birinci tur) | +0,01 (+0,01 / +0,01) | +0,02 (+0,02 / +0,02) | +0,04 (+0,04 / +0,05) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Kaybeden (S4 P50): −31 kişi; İzmir ve İstanbul.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Orta.


### 3.21 10.85 Hazır yemeklerin imalatı — GB statüsü: İTÜ | Birincil/ikincil arketip: — | Duruş: Koru

*Küçük sınıf (hazır yemek): ihracat $100 mn, AB payı %10. Kurallar emek yoğun ve gerileyen (F) dedi; GB'nin etkisi küçük olduğu için duruş Koru.*

**1. Kimlik.** Rev. 2.1: 10.85 (1:1); CPA 10.85. Başlıca HS4 (TR ihracatı 2024): 1902 %100. BEC payları (ticaret ağırlıklı): ara %0 / sermaye %0 / tüketim %100.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $815 mn; $221 mn (GSYH'nin %0,02) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 10.010; 932 (67 / 857 / 105 / 12 / 8) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %38; 0,35 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İstanbul %15; İzmir %15; Tekirdağ, Edirne, Kırklareli %11 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Yerli orta ölçekli üreticiler `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $100 mn; %26 |
| AB payı; ilk 5 AB pazarı | %10; DEU %23; DNK %15; FRA %11; NLD %8; ROU %7 |
| İlk 5 AB dışı pazar | IRQ %21; SYR %19; MYS %14; NER %11; PSE %2 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $2 mn; AB %65, Çin %18; ITA %46; CHN %18; DEU %10; HUN %5; VNM %4 |
| Dış ticaret dengesi | $+98 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %27 |
| RCA dünya (2020 → 2024) / AB pazarında | 1,30 → 1,00 / 0,25 |
| Birim değer ÷ AB pazarı ortalaması | 0,62 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,4 → %1,0; 12. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %7,0; 1/98 kaybıyla %7,0; tam MFN ortalaması %17,7. Rejim: GB %0, İTÜ %100, tarım %0 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): CHN %19; KOR %17; THA %15; CHE %13; VNM %13. Tercihli rakip payı %57.
- Menşe (S2 / S3): risk O/O; `c_RoO` %3,0 / %4,0; `p_uyum` 0,80 / 0,70 `[H]`. Kural: 1902 20 ve 2104: Fasıl 2, 3 ve 16 malzemeleri tamamen elde edilmiş; tahıl kuralı.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %15,9, İGV dahil %20,9 `[V]`. S4'te AB menşeline (c2): %23,3.

**6. Kabiliyet**

- KS 37,5 (sıra 216/230; ağırlık duyarlılığında P10–P90 170–222). Bileşenler: RCA 34, PCI 8 (PCI −1,08), yurt içi KD 66, Ar-Ge 25, tedarikçi 84, verimlilik 25, firma 46 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.

**7. Stratejik önem.** SS 23,6 (en yüksek boyut: gıda güvenliği 30; ağırlıklı ortalama 8,5) `[H]`. Hazır yemek; askerî ve afet tayınları

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,26; %2 |
| ÜFE vekili (imalat üretimindeki pay) | %0,12 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,005 / 0,003 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %38 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 35,3 ve 0,09; 8 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −1 (−1 / 0) | −1 (−1 / 0) | −1 (−1 / 0) |
| Toplam ihracat ($ mn) | 0 (−1 / 0) | −1 (−1 / 0) | −1 (−1 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Cari denge ($ mn) | 0 (−1 / 0) | 0 (−1 / 0) | 0 (−1 / 0) |
| Üretim ($ mn) | 0 (−1 / 0) | 0 (−1 / 0) | −1 (−1 / 0) |
| İstihdam (kişi) | −3 (−8 / 0) | −4 (−7 / −1) | −5 (−8 / −2) |
| TÜFE (bp, birinci tur) | +0,01 (+0,01 / +0,01) | +0,01 (+0,01 / +0,02) | +0,07 (+0,06 / +0,07) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Etkilenen kesim küçük (S4 P50 −5 kişi).

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Orta.


### 3.22 10.86 Homojenize gıda müstahzarları ve diyetetik gıdaların imalatı — GB statüsü: KARMA | Birincil/ikincil arketip: D/C | Duruş: Geliştir

*Bebek maması ve diyet gıdaları: ithalatın %91'i AB'den (Polonya, Almanya, İrlanda). S4'te AB'ye c2 (%7,6) fiyatı artırır. Sağlık açısından hassas; tarife yanlış araç, yerlileştirme için yatırım teşviki gerekiyor.*

**1. Kimlik.** Rev. 2.1: 10.61, 10.62, 10.71, 10.72, 10.73, 10.86 (1:6); CPA 10.86. Başlıca HS4 (TR ihracatı 2024): 1905 %85, 1901 %7, 2007 %5, 2104 %3. BEC payları (ticaret ağırlıklı): ara %0 / sermaye %0 / tüketim %100.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $172 mn; $61 mn (GSYH'nin %0,00) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 1.321; 124 (16 / 102 / 11 / 4 / 1) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %26; 0,45 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İstanbul %41; Ankara %15; Mardin, Batman, Şırnak, Siirt %9 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Nutricia (Danone), Nestlé, Abbott ve HiPP ithalatçıları; yerli üretimde Hero Baby (Ülker–Hero) `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $214 mn; %62 |
| AB payı; ilk 5 AB pazarı | %20; DEU %46; NLD %10; BEL %8; ROU %7; BGR %7 |
| İlk 5 AB dışı pazar | IRQ %29; USA %7; AZE %5; YEM %4; SYR %4 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $173 mn; AB %91, Çin %0; POL %32; DEU %25; FRA %12; IRL %10; NLD %5 |
| Dış ticaret dengesi | $+41 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %35 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,64 → 0,80 / 2,14 |
| Birim değer ÷ AB pazarı ortalaması | 1,26 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %4,5 → %8,5; 3. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %7,7; 1/98 kaybıyla %11,0; tam MFN ortalaması %11,2. Rejim: GB %0, İTÜ %86, tarım %14 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok (AB ihracatının %1'inden az).
- AB pazarında AB dışı rakipler (tercih durumu): GBR %39; CHE %9; CHN %6; SRB %5; USA %3. Tercihli rakip payı %67.
- Menşe (S2 / S3): risk O/O; `c_RoO` %2,5 / %3,5; `p_uyum` 0,85 / 0,75 `[H]`. Kural: 1901 10 ve 2104 20: Fasıl 4 ve tahıl malzemeleri ağırlık/menşe sınırları.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %8,4, İGV dahil %8,4 `[V]`. S4'te AB menşeline (c2): %7,5.
- Kritik girdiler (HS4 0402, 0404), Türkiye'nin toplam ithalatı 2024: $15 mn (AB %12; BLR %32, NZL %17, USA %13) `[V]`.
- Tüketimde ithal pay matristeki I-O tahmininden (%9) çok daha yüksek; bebek mamasında yerli üretim sınırlı `[D?]`. YSHİ üretimi ($172 mn) ihracatın ($214 mn) altında: sınıflama farkı var (VB-35).

**6. Kabiliyet**

- KS 50,1 (sıra 117/230; ağırlık duyarlılığında P10–P90 59–160). Bileşenler: RCA 46, PCI 40 (PCI −0,17), yurt içi KD 85, Ar-Ge 25, tedarikçi 84, verimlilik 46, firma 34 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.
- **Kırmızı çizgi yetkinlikleri:** Bebek maması formülasyonu ve gıda güvenliği laboratuvarları.
- **Geliştirme hedefi:** T+5: yerli bebek maması kapasitesi iç talebin %30'u; 2035: %50.

**7. Stratejik önem.** SS 54,9 (en yüksek boyut: sağlık 70; ağırlıklı ortalama 19,5) `[H]`. Bebek maması ve tıbbi gıdalar sağlık için kritik; ithalat bağımlılığı yüksek.

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,09; %9 |
| ÜFE vekili (imalat üretimindeki pay) | %0,03 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,021 / 0,019 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %26 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 1.850,8 ve 101,62; 72 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −7 (−17 / +1) | −9 (−17 / −2) | −13 (−21 / −5) |
| Toplam ihracat ($ mn) | −5 (−12 / +1) | −6 (−12 / −1) | −10 (−17 / −4) |
| Nihai mal ithalatı ($ mn) | −7 (−23 / +8) | −10 (−26 / +5) | −19 (−34 / −4) |
| Cari denge ($ mn) | +1 (−6 / +9) | +3 (−5 / +11) | +7 (0 / +14) |
| Üretim ($ mn) | +1 (−7 / +11) | +3 (−6 / +14) | +9 (0 / +18) |
| İstihdam (kişi) | +7 (−39 / +60) | +18 (−31 / +76) | +45 (−2 / +96) |
| TÜFE (bp, birinci tur) | +0,03 (+0,02 / +0,03) | +0,05 (+0,04 / +0,06) | +0,13 (+0,12 / +0,15) |
| Yatırım ve DYY (bütün senaryolar) | Yatırım teşviki (öncelikli yatırım) ile bir çok uluslu üretim tesisi hedefi `[H]` |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**10. Politika paketi**

| Eylem ID | Araç | Parametre | Sorumlu | Hukuki araç | Bütçe | Başlangıç–bitiş; sunset | Performans koşulu | KPI |
|---|---|---|---|---|---|---|---|---|
| E-10.86-01 | S4'te bebek mamasında MFN %0 | KN 1901 10: %7,6 → %0, tüm menşeler (yalnız S4'te; S2'de AB'ye zaten %0) | Ticaret Bakanlığı | İthalat Rejimi Kararı eki | Gelir kaybı ≈ 0,06 mlr TL/yıl (AB dışı ithalat) `[T]` | T → T+36; sunset: T+36 (yerli kapasite devreye girince) | — | Bebek maması TÜFE alt kalemi; −0,12 bp |
| E-10.86-02 | Bebek maması yatırım teşviki | Öncelikli yatırım statüsü; en az 30 bin ton/yıl kapasite | Sanayi ve Teknoloji Bakanlığı | Yatırımlarda Devlet Yardımları Kararı | 0,2 mlr TL (bir kez, vergi indirimi) `[T]` | T−12 → T+36; sunset: T+60 | Üretim başlangıcı T+36 | Yerli pay ≥ %30 |

**12. Erken uyarı ve tetikler**

| Gösterge | Eşik | Tetiklenecek önlem |
|---|---|---|
| Bebek maması perakende fiyatı (aylık) | 3 ayda +%10 | Stok ve ithalat izni hızlandırma |

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Kazanan (S4): yerli üretici; tüketici MFN %0 ile korunur.

**14. Riskler ve azaltım**

- Tek tedarikçi kesintisi → stok izleme.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Düşük (sınıf verisi tutarsız; VB-35).


### 3.23 10.89 Başka yerde sınıflandırılmamış diğer gıda maddelerinin imalatı — GB statüsü: İTÜ | Birincil/ikincil arketip: A/C | Duruş: Geliştir

*İki yönlü maruziyet. AB'ye ihracat $267 mn, en büyük satır 2106 90 92 (%12,8): S4'te −$30 mn. AB'den ithalat $396 mn, gıda takviyesi ve müstahzarı: S4'te c2 %30, TÜFE 0,7 bp. Mayada dünya ikincisi (%10,6).*

**1. Kimlik.** Rev. 2.1: 10.89, 11.07 (1:2); CPA 10.89. Başlıca HS4 (TR ihracatı 2024): 2106 %70, 2102 %23, 2104 %3, 1302 %2. BEC payları (ticaret ağırlıklı): ara %25 / sermaye %0 / tüketim %75.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $1.372 mn; $467 mn (GSYH'nin %0,03) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 10.858; 1.167 (174 / 988 / 93 / 31 / 8) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %22; 0,46 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İstanbul %34; Kocaeli, Sakarya, Düzce, Bolu, Yalova %10; İzmir %10 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Pakmaya (maya), Dr. Oetker, Unilever (Knorr), Nestlé `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $1.114 mn; %59 |
| AB payı; ilk 5 AB pazarı | %24; CZE %26; DEU %19; NLD %14; ITA %9; ESP %7 |
| İlk 5 AB dışı pazar | IRQ %15; USA %7; DZA %4; SAU %4; AZE %3 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $639 mn; AB %62, Çin %6; DEU %15; ITA %12; USA %8; NLD %8; FRA %6 |
| Dış ticaret dengesi | $+475 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %34 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,89 → 0,99 / 1,10 |
| Birim değer ÷ AB pazarı ortalaması | 1,14 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %3,3 → %4,4; 5. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %11,8; 1/98 kaybıyla %12,0; tam MFN ortalaması %13,0. Rejim: GB %1, İTÜ %98, tarım %1 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): 10 satır, AB ihracatının %83'i: KN 2106 90 92 %12,8 (€174,7 mn); KN 2102 10 31 %12,0 (€9,4 mn); KN 2104 10 00 %11,5 (€5,6 mn).
- AB pazarında AB dışı rakipler (tercih durumu): GBR %22; CHN %15; USA %14; CHE %10; IND %4. Tercihli rakip payı %50.
- Menşe (S2 / S3): risk D/O; `c_RoO` %2,0 / %3,0; `p_uyum` 0,85 / 0,80 `[H]`. Kural: 2106 ve 2102: başlık değişikliği; şeker ve Fasıl 4 ağırlık sınırları.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.
- AB'ye ihracatta en büyük satır KN 2106 90 92 (€175 mn; süt yağı ve şeker içermeyen müstahzarlar). İçerik `[D?]`: aroma ve tatlandırıcı karışımları olabilir.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %25,7, İGV dahil %25,9 `[V]`. S4'te AB menşeline (c2): %25,4.
- 2106 90'da Türkiye'nin MFN'si yüksek (satırlarda %17–58,5). S4'te AB'den gelen takviye ve müstahzarlara c2 olarak yansıyor. İGV kaldırma ölçütü (AB baskın, yerli zayıf) bazı satırlarda karşılanıyor.

**6. Kabiliyet**

- KS 53,1 (sıra 76/230; ağırlık duyarlılığında P10–P90 39–130). Bileşenler: RCA 48, PCI 43 (PCI −0,13), yurt içi KD 83, Ar-Ge 25, tedarikçi 84, verimlilik 49, firma 56 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.
- **Geliştirme hedefi:** T+5: maya ve maya ekstraktında Afrika ve Asya payı.

**7. Stratejik önem.** SS 38,1 (en yüksek boyut: gıda güvenliği 50; ağırlıklı ortalama 10,5) `[H]`. Maya (ekmek zinciri) ve gıda müstahzarları

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,07; %8 |
| ÜFE vekili (imalat üretimindeki pay) | %0,21 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,054 / 0,033 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %22 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 438,5 ve 17,26; 36 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −12 (−28 / +5) | −15 (−30 / −3) | −30 (−49 / −13) |
| Toplam ihracat ($ mn) | −9 (−21 / +4) | −11 (−22 / −2) | −24 (−40 / −10) |
| Nihai mal ithalatı ($ mn) | −5 (−17 / +15) | −8 (−20 / +9) | −25 (−45 / −5) |
| Cari denge ($ mn) | −4 (−9 / 0) | −3 (−9 / +1) | 0 (−4 / +5) |
| Üretim ($ mn) | −5 (−11 / 0) | −4 (−11 / +1) | 0 (−5 / +7) |
| İstihdam (kişi) | −25 (−63 / 0) | −21 (−63 / +6) | +2 (−28 / +37) |
| TÜFE (bp, birinci tur) | +0,08 (+0,07 / +0,09) | +0,15 (+0,13 / +0,18) | +0,71 (+0,61 / +0,80) |
| Yatırım ve DYY (bütün senaryolar) | Etkisi küçük |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**12. Erken uyarı ve tetikler**

| Gösterge | Eşik | Tetiklenecek önlem |
|---|---|---|
| 2106 90 ithalat fiyatı (S4) | Yıllık +%15 | İGV'nin bu satırlarda kaldırılması (c2 kuralının gözden geçirilmesi) |

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** S4'te iç ikame AB ihracat kaybını dengeliyor (P50 +2 kişi).

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Orta (en büyük satırın içeriği `[D?]`).


### 3.24 10.91 Çiftlik hayvanları için hazır yem imalatı — GB statüsü: TARIM-1/98 | Birincil/ikincil arketip: D/B | Duruş: Geliştir

*Karma yem: hayvancılığın ana girdisi. İhracat AB dışına (Irak, Suriye). GB etkisi yok; soya küspesi, mısır ve DDGS ithalatına bağımlı.*

**1. Kimlik.** Rev. 2.1: 10.91 (1:1); CPA 10.91. Başlıca HS4 (TR ihracatı 2024): 2309 %100, 1214 %0. BEC payları (ticaret ağırlıklı): ara %100 / sermaye %0 / tüketim %0.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $6.390 mn; $846 mn (GSYH'nin %0,06) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 14.598; 757 (82 / 512 / 162 / 49 / 9) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %29; 0,60 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | Manisa, Afyon, Kütahya, Uşak %13; Balıkesir, Çanakkale %11; İzmir %10 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Bolca orta ölçekli üretici; Cargill, Kocatepe Yem, Abalıoğlu `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $352 mn; %128 |
| AB payı; ilk 5 AB pazarı | %1; NLD %27; ESP %10; ROU %9; GRC %9; BEL %8 |
| İlk 5 AB dışı pazar | IRQ %36; SYR %25; RUS %6; TUN %4; URY %4 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $279 mn; AB %50, Çin %9; FRA %13; RUS %10; CHN %9; ITA %7; USA %6 |
| Dış ticaret dengesi | $+73 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %13 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,82 → 1,40 / 0,10 |
| Birim değer ÷ AB pazarı ortalaması | 2,59 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,4 → %0,4; 13. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %9,3; tam MFN ortalaması %9,3. Rejim: GB %0, İTÜ %0, tarım %100 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): CHN %31; GBR %25; USA %12; NOR %9; RUS %4. Tercihli rakip payı %42.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 2309: tahıl, şeker pancarı ve Fasıl 2–4 malzemeleri tamamen elde edilmiş; ağırlık sınırı.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %6,8, İGV dahil %6,8 `[V]`. S4'te AB menşeline (c2): %0,0.
- Kritik girdiler (HS4 2304, 1005, 1201, 2303), Türkiye'nin toplam ithalatı 2024: $3.768 mn (AB %4; BRA %33, UKR %23, USA %13) `[V]`.

**6. Kabiliyet**

- KS 49,3 (sıra 125/230; ağırlık duyarlılığında P10–P90 65–165). Bileşenler: RCA 66, PCI 18 (PCI −0,76), yurt içi KD 48, Ar-Ge 25, tedarikçi 84, verimlilik 76, firma 58 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.

**7. Stratejik önem.** SS 63,3 (en yüksek boyut: gıda güvenliği 85; ağırlıklı ortalama 12,8) `[H]`. Yem, kanatlı ve süt zincirinin maliyet tabanı.

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,00; %9 |
| ÜFE vekili (imalat üretimindeki pay) | %0,96 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,021 / 0,011 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %29 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 1.600,7 ve 1,96; 30 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (−1 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (−1 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (0 / +10) | 0 (0 / +6) | 0 (0 / 0) |
| Cari denge ($ mn) | 0 (−8 / 0) | 0 (−5 / 0) | 0 (−1 / 0) |
| Üretim ($ mn) | 0 (−10 / 0) | 0 (−6 / 0) | 0 (−1 / 0) |
| İstihdam (kişi) | 0 (−16 / 0) | 0 (−9 / 0) | 0 (−1 / 0) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Etkilenen kesim yok.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Yüksek.


### 3.25 10.92 Ev hayvanları için hazır gıda imalatı — GB statüsü: TARIM-1/98 | Birincil/ikincil arketip: C | Duruş: Geliştir

*Evcil hayvan maması: ithalatın %87'si AB'den (Fransa, Polonya). Yerli üretim hızla büyüyor (RCA 0,17 → 0,49). Tarım rejiminde; GB çıkışı tarifeyi değiştirmiyor.*

**1. Kimlik.** Rev. 2.1: 10.92 (1:1); CPA 10.92. Başlıca HS4 (TR ihracatı 2024): 2309 %100. BEC payları (ticaret ağırlıklı): ara %0 / sermaye %0 / tüketim %100.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $347 mn; $81 mn (GSYH'nin %0,01) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 1.768; 140 (21 / 117 / 18 / — / —) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %21; 0,44 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İzmir %38; Manisa, Afyon, Kütahya, Uşak %16; Adana, Mersin %11 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Mars (Royal Canin) ve Nestlé Purina ithalatı; yerli üreticiler `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $147 mn; %382 |
| AB payı; ilk 5 AB pazarı | %14; GRC %32; BGR %20; DEU %13; ROU %12; ITA %6 |
| İlk 5 AB dışı pazar | MYS %15; IRQ %12; SAU %6; USA %5; ISR %5 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $214 mn; AB %87, Çin %4; FRA %39; POL %14; HUN %10; ITA %6; NLD %5 |
| Dış ticaret dengesi | $−67 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %23 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,17 → 0,49 / 0,25 |
| Birim değer ÷ AB pazarı ortalaması | 0,50 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,4 → %1,0; 10. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %5,7; tam MFN ortalaması %5,7. Rejim: GB %0, İTÜ %0, tarım %100 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): CHN %26; THA %18; CHE %18; GBR %17; CAN %5. Tercihli rakip payı %44.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 2309 10: aynı.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %8,5, İGV dahil %8,5 `[V]`. S4'te AB menşeline (c2): %0,0.

**6. Kabiliyet**

- KS 48,3 (sıra 133/230; ağırlık duyarlılığında P10–P90 95–167). Bileşenler: RCA 46, PCI 51 (PCI 0,03), yurt içi KD 58, Ar-Ge 25, tedarikçi 84, verimlilik 43, firma 38 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.

**7. Stratejik önem.** SS 3,7 (en yüksek boyut: gıda güvenliği 5; ağırlıklı ortalama 0,8) `[H]`. 

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,19; %12 |
| ÜFE vekili (imalat üretimindeki pay) | %0,05 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,040 / 0,035 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %21 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 585,6 ve 22,92; 41 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (−2 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (−2 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (0 / +12) | 0 (0 / +7) | 0 (0 / 0) |
| Cari denge ($ mn) | 0 (−9 / 0) | 0 (−6 / 0) | 0 (−2 / 0) |
| Üretim ($ mn) | 0 (−11 / 0) | 0 (−7 / 0) | 0 (−2 / 0) |
| İstihdam (kişi) | 0 (−41 / 0) | 0 (−24 / 0) | 0 (−7 / 0) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Etkilenen kesim yok.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Orta.


### 3.26 11.01 Alkollü içeceklerin damıtılması, arıtılması ve harmanlanması — GB statüsü: İTÜ | Birincil/ikincil arketip: — | Duruş: Koru

*Rakı (Mey|Diageo) ve diğer alkollü içkiler. AB'nin MFN'si sıfıra yakın; GB etkisi yok. İthalatın %63'ü İngiltere'den (viski; TR–BK STA'sı).*

**1. Kimlik.** Rev. 2.1: 11.01 (1:1); CPA 11.01. Başlıca HS4 (TR ihracatı 2024): 2208 %100. BEC payları (ticaret ağırlıklı): ara %0 / sermaye %0 / tüketim %100.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $1.210 mn; $393 mn (GSYH'nin %0,03) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 2.398; 21 (1 / 7 / 9 / 1 / 4) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %85; — | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İstanbul %50; Manisa, Afyon, Kütahya, Uşak %26; Antalya, Isparta, Burdur %11 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Mey/Diageo (2011'den beri Diageo) `[V]`, Efe Rakı, Tekirdağ (Mey) `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $68 mn; %92 |
| AB payı; ilk 5 AB pazarı | %48; DEU %69; BGR %7; NLD %7; AUT %5; FRA %3 |
| İlk 5 AB dışı pazar | CYP %62; BLR %13; USA %6; IRQ %4; GBR %4 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $425 mn; AB %25, Çin %0; GBR %63; DEU %7; MEX %5; IRL %4; USA %4 |
| Dış ticaret dengesi | $−358 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %33 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,11 → 0,14 / 0,17 |
| Birim değer ÷ AB pazarı ortalaması | 1,20 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,7 → %0,7; 11. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %0,4; tam MFN ortalaması %0,4. Rejim: GB %0, İTÜ %100, tarım %0 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): GBR %54; USA %23; MEX %4; JPN %2; CHN %2. Tercihli rakip payı %70.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 2208: başlık değişikliği (2207–2208 hariç); üzüm türevleri tamamen elde edilmiş (rakı: yerli suma).
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %0,6, İGV dahil %0,6 `[V]`. S4'te AB menşeline (c2): %0,7.
- ÖTV ile gümrük etkileşimi: alkollü içkide ÖTV maktu (litre başına) ve fiyatın çoğunu oluşturuyor. Gümrük vergisinin perakende fiyata oransal etkisi düşük.

**6. Kabiliyet**

- KS 41,0 (sıra 201/230; ağırlık duyarlılığında P10–P90 131–218). Bileşenler: RCA 29, PCI 29 (PCI −0,36), yurt içi KD 81, Ar-Ge 25, tedarikçi 84, verimlilik —, firma 11 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.

**7. Stratejik önem.** SS 0,0 (en yüksek boyut: — 0; ağırlıklı ortalama 0,0) `[H]`. 

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,28; %18 |
| ÜFE vekili (imalat üretimindeki pay) | %0,18 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,083 / 0,021 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %85 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 279,0 ve 6,69; 23 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −1 (−2 / +1) | −1 (−2 / 0) | 0 (−1 / 0) |
| Toplam ihracat ($ mn) | −1 (−1 / 0) | −1 (−1 / 0) | 0 (−1 / 0) |
| Nihai mal ithalatı ($ mn) | −1 (−3 / +6) | −1 (−3 / +4) | −1 (−2 / 0) |
| Cari denge ($ mn) | 0 (−4 / +1) | 0 (−3 / +1) | 0 (0 / +1) |
| Üretim ($ mn) | 0 (−5 / +1) | 0 (−4 / +2) | +1 (0 / +1) |
| İstihdam (kişi) | 0 (−7 / +2) | +1 (−5 / +2) | +1 (0 / +2) |
| TÜFE (bp, birinci tur) | +0,02 (+0,01 / +0,02) | +0,03 (+0,03 / +0,04) | +0,03 (+0,02 / +0,04) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**11. Müzakere pozisyonu**

- AB ile hücum: S2'de 'Türk Rakısı' coğrafi işaretinin karşılıklı korunması `[D?]` (AB'deki tescil durumu).

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Etkilenen kesim yok.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Orta (YSHİ gizli; bölüm kalanından tahmin).


### 3.27 11.02 Üzümden şarap imalatı — GB statüsü: TARIM-1/98 | Birincil/ikincil arketip: — | Duruş: Koru

*Küçük şarap sınıfı (ihracat $24 mn). Tarım rejiminde; GB etkisi yok.*

**1. Kimlik.** Rev. 2.1: 11.02 (1:1); CPA 11.02. Başlıca HS4 (TR ihracatı 2024): 2204 %100. BEC payları (ticaret ağırlıklı): ara %0 / sermaye %0 / tüketim %100.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $278 mn; $109 mn (GSYH'nin %0,01) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 1.968; 196 (21 / 145 / 35 / 8 / 0) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %0; 0,59 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | Aydın, Denizli, Muğla %16; Ankara %14; Tekirdağ, Edirne, Kırklareli %14 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Kavaklıdere, Doluca, Kayra `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $24 mn; %213 |
| AB payı; ilk 5 AB pazarı | %61; GRC %23; DEU %21; NLD %15; BEL %12; FRA %12 |
| İlk 5 AB dışı pazar | BLR %34; GBR %21; CYP %14; USA %11; RUS %9 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $53 mn; AB %86, Çin %0; FRA %43; ITA %24; GRC %7; ESP %5; MDA %4 |
| Dış ticaret dengesi | $−29 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %39 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,02 → 0,05 / 0,23 |
| Birim değer ÷ AB pazarı ortalaması | 1,72 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,2 → %0,9; 12. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %0,3; tam MFN ortalaması %0,3. Rejim: GB %0, İTÜ %0, tarım %100 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): CHL %21; USA %19; ZAF %14; AUS %12; NZL %8. Tercihli rakip payı %60.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 2204: üzüm ve türevleri tamamen elde edilmiş.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %69,9, İGV dahil %69,9 `[V]`. S4'te AB menşeline (c2): %0,0.

**6. Kabiliyet**

- KS 50,3 (sıra 110/230; ağırlık duyarlılığında P10–P90 45–168). Bileşenler: RCA 32, PCI 23 (PCI −0,56), yurt içi KD 90, Ar-Ge 25, tedarikçi 84, verimlilik 74, firma 62 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): 220422 (PCI -0.15, RCA 0.00) `[T]`.

**7. Stratejik önem.** SS 0,0 (en yüksek boyut: — 0; ağırlıklı ortalama 0,0) `[H]`. 

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,05; %15 |
| ÜFE vekili (imalat üretimindeki pay) | %0,04 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,011 / 0,009 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %0 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 773,8 ve 10,18; 33 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (0 / +3) | 0 (0 / +2) | 0 (0 / 0) |
| Cari denge ($ mn) | 0 (−2 / 0) | 0 (−1 / 0) | 0 (0 / 0) |
| Üretim ($ mn) | 0 (−3 / 0) | 0 (−2 / 0) | 0 (0 / 0) |
| İstihdam (kişi) | 0 (−15 / 0) | 0 (−9 / 0) | 0 (−1 / 0) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Etkilenen kesim yok.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Yüksek.


### 3.28 11.03 Elma şarabı ve diğer meyve şaraplarının imalatı — GB statüsü: TARIM-1/98 | Birincil/ikincil arketip: — | Duruş: Koru

*İhmal edilebilir ticaret (elma şarabı); YSHİ verisi yok.*

**1. Kimlik.** Rev. 2.1: 11.03 (1:1); CPA 11.03. Başlıca HS4 (TR ihracatı 2024): 2206 %100. BEC payları (ticaret ağırlıklı): ara %0 / sermaye %0 / tüketim %100.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $— mn; $— mn (GSYH'nin —) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | —; — (— / — / — / — / —) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | —; — | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | — | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | — | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $0 mn; %−61 |
| AB payı; ilk 5 AB pazarı | %10; DEU %66; BEL %25; CZE %10; IRL %0 |
| İlk 5 AB dışı pazar | CYP %60; AUS %34; CHE %3; GBR %1; ZAF %1 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $1 mn; AB %47, Çin %0; JPN %30; SWE %23; BEL %11; CAN %6; USA %6 |
| Dış ticaret dengesi | $−1 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / — |
| RCA dünya (2020 → 2024) / AB pazarında | 0,02 → 0,01 / 0,01 |
| Birim değer ÷ AB pazarı ortalaması | 1,07 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,0 → %0,0; 33. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %1,1; tam MFN ortalaması %1,1. Rejim: GB %0, İTÜ %0, tarım %100 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): GBR %38; JPN %23; USA %11; CHN %10; ARM %3. Tercihli rakip payı %73.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 2206: başlık değişikliği; meyve tamamen elde edilmiş.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %70,0, İGV dahil %70,0 `[V]`. S4'te AB menşeline (c2): %0,0.

**6. Kabiliyet**

- KS 42,5 (sıra 186/230; ağırlık duyarlılığında P10–P90 104–221). Bileşenler: RCA 2, PCI 54 (PCI 0,07), yurt içi KD 72, Ar-Ge 25, tedarikçi 84, verimlilik —, firma — `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.

**7. Stratejik önem.** SS 0,0 (en yüksek boyut: — 0; ağırlıklı ortalama 0,0) `[H]`. 

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,00; %19 |
| ÜFE vekili (imalat üretimindeki pay) | — |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,000 / 0,000 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | — |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 0,0 ve —; 3 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Cari denge ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Üretim ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| İstihdam (kişi) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Düşük (YSHİ verisi yok).


### 3.29 11.04 Diğer damıtılmamış fermente içeceklerin imalatı — GB statüsü: İTÜ | Birincil/ikincil arketip: — | Duruş: Koru

*İhmal edilebilir ticaret (vermut ve benzeri); YSHİ verisi yok.*

**1. Kimlik.** Rev. 2.1: 11.04 (1:1); CPA 11.04. Başlıca HS4 (TR ihracatı 2024): 2205 %100. BEC payları (ticaret ağırlıklı): ara %0 / sermaye %0 / tüketim %100.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $— mn; $— mn (GSYH'nin —) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | —; — (— / — / — / — / —) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | —; — | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | — | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | — | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $0 mn; %696 |
| AB payı; ilk 5 AB pazarı | %15; DEU %100 |
| İlk 5 AB dışı pazar | NGA %93; GBR %5; OMN %1; GEO %1 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $2 mn; AB %100, Çin %0; ITA %71; DEU %12; ESP %6; ROU %5; NLD %2 |
| Dış ticaret dengesi | $−2 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / — |
| RCA dünya (2020 → 2024) / AB pazarında | 0,00 → 0,01 / 0,02 |
| Birim değer ÷ AB pazarı ortalaması | 1,74 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,0 → %0,1; 28. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %0,0; tam MFN ortalaması %0,7. Rejim: GB %0, İTÜ %100, tarım %0 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): ARG %48; USA %20; CHL %10; GEO %6; GBR %5. Tercihli rakip payı %30.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 2205: başlık değişikliği; üzüm türevleri tamamen elde edilmiş.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %4,2, İGV dahil %4,2 `[V]`. S4'te AB menşeline (c2): %4,2.

**6. Kabiliyet**

- KS 43,1 (sıra 180/230; ağırlık duyarlılığında P10–P90 114–207). Bileşenler: RCA 31, PCI 27 (PCI −0,42), yurt içi KD 72, Ar-Ge 25, tedarikçi 84, verimlilik —, firma — `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.

**7. Stratejik önem.** SS 0,0 (en yüksek boyut: — 0; ağırlıklı ortalama 0,0) `[H]`. 

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,00; %20 |
| ÜFE vekili (imalat üretimindeki pay) | — |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,000 / 0,000 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | — |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | — ve —; — |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Cari denge ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Üretim ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| İstihdam (kişi) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Düşük (YSHİ verisi yok).


### 3.30 11.05 Bira imalatı — GB statüsü: İTÜ | Birincil/ikincil arketip: — | Duruş: Koru

*Bira (Anadolu Efes, Türk Tuborg). AB'nin bira MFN'si sıfır; GB etkisi yok. İthalatın ($348 mn) %92'si bira değil, ABD'den damıtma artığı yem (KN 2303 30, DDGS).*

**1. Kimlik.** Rev. 2.1: 11.05 (1:1); CPA 11.05. Başlıca HS4 (TR ihracatı 2024): 2203 %90, 2202 %7, 2303 %3. BEC payları (ticaret ağırlıklı): ara %78 / sermaye %0 / tüketim %22. CPA 11.05.20 (bira ve damıtma artığı) DDGS'yi bu sınıfa koyuyor; ekonomik olarak bir yem girdisi (10.91).

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $199 mn; $65 mn (GSYH'nin %0,00) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 394; 15 (3 / 12 / 0 / 0 / 1) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %90; 1,50 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İzmir %59; İstanbul %15; Adana, Mersin %9 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Anadolu Efes (AB InBev ortaklığı `[D?]`), Türk Tuborg `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $61 mn; %29 |
| AB payı; ilk 5 AB pazarı | %8; BGR %32; ROU %22; FRA %11; SVK %8; NLD %6 |
| İlk 5 AB dışı pazar | IRQ %39; CYP %29; GBR %8; CHN %7; AZE %3 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $348 mn; AB %10, Çin %0; USA %64; BRA %12; RUS %8; BGR %3; MEX %3 |
| Dış ticaret dengesi | $−287 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %33 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,23 → 0,23 / 0,15 |
| Birim değer ÷ AB pazarı ortalaması | 0,79 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,7 → %0,6; 11. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %0,0; tam MFN ortalaması %0,0. Rejim: GB %0, İTÜ %100, tarım %0 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): GBR %43; USA %23; MEX %16; BRA %3; CAN %3. Tercihli rakip payı %67.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 2203: başlık değişikliği (ithal malttan bira menşe kazanır).
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %0,1, İGV dahil %1,6 `[V]`. S4'te AB menşeline (c2): %8,5.
- İthalatın asıl kalemi DDGS ($319 mn, ABD). Tarım rejiminde (Fasıl 23) ve GB'den bağımsız; yem maliyeti için önemli.

**6. Kabiliyet**

- KS 42,4 (sıra 189/230; ağırlık duyarlılığında P10–P90 105–220). Bileşenler: RCA 19, PCI 20 (PCI −0,64), yurt içi KD 80, Ar-Ge 25, tedarikçi 84, verimlilik 98, firma 4 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.

**7. Stratejik önem.** SS 0,0 (en yüksek boyut: — 0; ağırlıklı ortalama 0,0) `[H]`. 

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,27; %18 |
| ÜFE vekili (imalat üretimindeki pay) | %0,03 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,075 / 0,008 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %90 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 121,4 ve 21,81; 33 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (−1 / +1) | 0 (−1 / 0) | −1 (−1 / 0) |
| Cari denge ($ mn) | 0 (−1 / 0) | 0 (0 / 0) | 0 (0 / +1) |
| Üretim ($ mn) | 0 (−1 / 0) | 0 (0 / 0) | +1 (0 / +1) |
| İstihdam (kişi) | 0 (−1 / 0) | 0 (−1 / 0) | +1 (0 / +2) |
| TÜFE (bp, birinci tur) | +0,01 (+0,01 / +0,01) | +0,02 (+0,01 / +0,02) | +0,06 (+0,05 / +0,06) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Etkilenen kesim yok.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Orta (YSHİ gizli; sınıflama notu).


### 3.31 11.06 Malt imalatı — GB statüsü: TARIM-1/98 | Birincil/ikincil arketip: — | Duruş: Koru

*Malt: ithalat $72 mn (Almanya, Danimarka, Fransa). YSHİ verisi yok. Tarım rejiminde; GB etkisi yok.*

**1. Kimlik.** Rev. 2.1: 11.06 (1:1); CPA 11.06. Başlıca HS4 (TR ihracatı 2024): 1107 %100. BEC payları (ticaret ağırlıklı): ara %100 / sermaye %0 / tüketim %0.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $— mn; $— mn (GSYH'nin —) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | —; — (— / — / — / — / —) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | —; — | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | — | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Efes Malt (Afyon, Konya) `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $0 mn; %−66 |
| AB payı; ilk 5 AB pazarı | %2; NLD %90; DEU %6; BEL %4; ITA %0; POL %0 |
| İlk 5 AB dışı pazar | CAF %86; CYP %5; UKR %3; IRQ %2; CAN %1 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $83 mn; AB %86, Çin %0; DEU %29; DNK %23; FRA %23; RUS %10; ROU %7 |
| Dış ticaret dengesi | $−83 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / — |
| RCA dünya (2020 → 2024) / AB pazarında | 0,03 → 0,01 / 0,01 |
| Birim değer ÷ AB pazarı ortalaması | 2,98 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %0,0 → %0,0; 20. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %0,0; 1/98 kaybıyla %8,2; tam MFN ortalaması %8,2. Rejim: GB %0, İTÜ %0, tarım %100 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): GBR %71; UKR %23; COD %2; TGO %1; SRB %1. Tercihli rakip payı %95.
- Menşe (S2 / S3): risk D/D; `c_RoO` %1,5 / %2,0; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 1107: tahıl tamamen elde edilmiş.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %18,7, İGV dahil %18,7 `[V]`. S4'te AB menşeline (c2): %0,0.

**6. Kabiliyet**

- KS 43,7 (sıra 176/230; ağırlık duyarlılığında P10–P90 92–218). Bileşenler: RCA 1, PCI 59 (PCI 0,16), yurt içi KD 72, Ar-Ge 25, tedarikçi 84, verimlilik —, firma — `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.

**7. Stratejik önem.** SS 14,9 (en yüksek boyut: gıda güvenliği 20; ağırlıklı ortalama 3,0) `[H]`. Malt; bira ve gıda girdisi

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %0,00; %21 |
| ÜFE vekili (imalat üretimindeki pay) | — |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,006 / 0,005 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | — |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 0,0 ve —; 3 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Toplam ihracat ($ mn) | 0 (0 / 0) | 0 (0 / 0) | 0 (0 / 0) |
| Nihai mal ithalatı ($ mn) | 0 (0 / +5) | 0 (0 / +3) | 0 (0 / 0) |
| Cari denge ($ mn) | 0 (−4 / 0) | 0 (−2 / 0) | 0 (0 / 0) |
| Üretim ($ mn) | 0 (−5 / 0) | 0 (−3 / 0) | 0 (0 / 0) |
| İstihdam (kişi) | 0 (−10 / 0) | 0 (−6 / 0) | 0 (0 / 0) |
| TÜFE (bp, birinci tur) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) | 0,00 (0,00 / 0,00) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Düşük (YSHİ verisi yok).


### 3.32 11.07 Alkolsüz içeceklerin imalatı; maden sularının ve diğer şişelenmiş suların üretimi — GB statüsü: KARMA | Birincil/ikincil arketip: — | Duruş: Koru

*Alkolsüz içecek ve su. AB'ye ihracat $111 mn, S4'te %6,6. AB'den ithalat $258 mn, enerji içecekleri (Avusturya %42): S4'te c2 %8,6, TÜFE 0,8 bp. Etki küçük.*

**1. Kimlik.** Rev. 2.1: 11.07 (n:1); CPA 11.07. Başlıca HS4 (TR ihracatı 2024): 2202 %79, 2201 %21. BEC payları (ticaret ağırlıklı): ara %0 / sermaye %0 / tüketim %100.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $3.641 mn; $764 mn (GSYH'nin %0,06) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 14.765; 537 (72 / 343 / 105 / 44 / 13) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %45; — | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | Bursa, Eskişehir, Bilecik %17; Kocaeli, Sakarya, Düzce, Bolu, Yalova %14; Adana, Mersin %12 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Coca-Cola İçecek (Anadolu Grubu), PepsiCo şişeleyicisi, Uludağ, Erikli ve Hayat Su `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $385 mn; %61 |
| AB payı; ilk 5 AB pazarı | %29; DEU %42; NLD %14; AUT %7; FRA %7; BEL %7 |
| İlk 5 AB dışı pazar | GBR %17; SYR %13; LBY %8; ARE %7; CYP %7 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $330 mn; AB %78, Çin %0; AUT %42; NLD %19; CHE %16; DEU %4; ITA %4 |
| Dış ticaret dengesi | $+55 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %21 |
| RCA dünya (2020 → 2024) / AB pazarında | 0,89 → 0,93 / 1,41 |
| Birim değer ÷ AB pazarı ortalaması | 1,29 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %5,7 → %5,6; 4. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %6,6; 1/98 kaybıyla %6,6; tam MFN ortalaması %7,0. Rejim: GB %28, İTÜ %72, tarım %0 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): yok.
- AB pazarında AB dışı rakipler (tercih durumu): CHE %33; GBR %23; SRB %7; USA %3; KOR %3. Tercihli rakip payı %73.
- Menşe (S2 / S3): risk D/O; `c_RoO` %1,5 / %2,5; `p_uyum` 0,90 / 0,85 `[H]`. Kural: 2201–2202: başlık değişikliği; şeker %40 ağırlık sınırı; meyve suyu menşeli.
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %8,6, İGV dahil %8,6 `[V]`. S4'te AB menşeline (c2): %8,6.
- ÖTV ile gümrük etkileşimi: kolalı içeceklerde ÖTV (III) oransal. S4'te AB'den gelen enerji içeceğindeki gümrük vergisi ÖTV matrahına giriyor, ama etki küçük (0,8 bp).

**6. Kabiliyet**

- KS 41,3 (sıra 200/230; ağırlık duyarlılığında P10–P90 150–207). Bileşenler: RCA 42, PCI 20 (PCI −0,64), yurt içi KD 54, Ar-Ge 25, tedarikçi 84, verimlilik —, firma 45 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.

**7. Stratejik önem.** SS 30,2 (en yüksek boyut: gıda güvenliği 40; ağırlıklı ortalama 7,5) `[H]`. İçme suyu arzı (afet ve kriz)

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %1,11; %10 |
| ÜFE vekili (imalat üretimindeki pay) | %0,55 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,134 / 0,104 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %45 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 567,9 ve 7,85; 29 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −10 (−25 / +2) | −15 (−28 / −3) | −23 (−38 / −10) |
| Toplam ihracat ($ mn) | −7 (−18 / +2) | −10 (−20 / −2) | −18 (−30 / −8) |
| Nihai mal ithalatı ($ mn) | −12 (−39 / +18) | −18 (−44 / +11) | −37 (−67 / −8) |
| Cari denge ($ mn) | +3 (−13 / +17) | +5 (−10 / +20) | +15 (0 / +30) |
| Üretim ($ mn) | +4 (−17 / +22) | +7 (−13 / +26) | +18 (0 / +38) |
| İstihdam (kişi) | +10 (−46 / +62) | +19 (−37 / +73) | +52 (0 / +106) |
| TÜFE (bp, birinci tur) | +0,14 (+0,12 / +0,17) | +0,27 (+0,23 / +0,33) | +0,81 (+0,70 / +0,93) |
| Yatırım ve DYY (bütün senaryolar) | — |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** S4'te iç ikame kazancı (+52 kişi); AB ihracatçısı küçük kayıp.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Düşük (AB verimlilik verisi yok; YSHİ gizli).


### 3.33 12.00 Tütün ürünleri imalatı — GB statüsü: KARMA | Birincil/ikincil arketip: B | Duruş: Koru

*Çok uluslu üretim üssü. AB'ye $116 mn ihracat; sigarada AB MFN'si %57,6, S4'te AB pazarı kapanır. S2'de de %70 menşeli yaprak kuralı Amerikan harmanını dışarıda bırakıyor. İthalatın %48'i AB'den, ısıtılmış tütün ve sigara: S4 TÜFE etkisi 2,7 bp.*

**1. Kimlik.** Rev. 2.1: 12.00 (1:1); CPA 12.00. Başlıca HS4 (TR ihracatı 2024): 2402 %62, 2403 %27, 2401 %11. BEC payları (ticaret ağırlıklı): ara %45 / sermaye %0 / tüketim %55. NACE 12.00 yaprak tütün işlemeyi de (sapından ayırma, kurutma) içeriyor; AB pazarındaki rakip listesi (Brezilya, Hindistan, Malavi) bu yüzden yaprak tütün ihracatçıları.

**2. Ölçek**

| Gösterge | Değer | Etiket ve kaynak |
|---|---|---|
| Üretim değeri; katma değer | $2.816 mn; $656 mn (GSYH'nin %0,05) | TÜİK YSHİ 2024 `[V]` |
| Çalışan; girişim (0 / 1–9 / 10–49 / 50–249 / 250+) | 5.769; 80 (8 / 43 / 21 / 8 / 5) | TÜİK YSHİ ve İş Kayıtları 2024 `[V]`; gizli büyüklük hücreleri `[T]` |
| 250+ girişimlerin istihdam payı; AB'ye göre kişi başı KD | %75; 0,48 | `[T]` (AB27 SBS 2023, nominal kur) |
| İlk 3 İBBS-2 bölgesi | İzmir %59; Samsun, Tokat, Çorum, Amasya %11; Adana, Mersin %6 | `[T]` iş kayıtları + SGK 2025, RAS |
| Yabancı sermaye; çapa yatırımcılar | Philip Morris (Torbalı; 2024'te üretiminin %11'inden fazlasını ihraç etti) `[V]`, JTI (Torbalı), BAT `[D?]`, KT&G `[H]` | `[H]` (firma bilgisi; pay verisi yok: VB-30) |

**3. Dış ticaret**

| Gösterge | Değer (BACI 2024, $; `[V]`, eşleme `[T]`) |
|---|---|
| İhracat (2024); 2020–24 değişimi | $876 mn; %19 |
| AB payı; ilk 5 AB pazarı | %13; ROU %36; NLD %15; DEU %12; BEL %10; MLT %7 |
| İlk 5 AB dışı pazar | IRQ %20; IRN %11; AZE %7; KWT %7; USA %7 |
| İthalat; AB ve Çin payı; ilk kaynaklar | $958 mn; AB %48, Çin %1; DEU %14; NLD %11; BEL %9; IND %6; BRA %6 |
| Dış ticaret dengesi | $−81 mn |
| İthal girdi içeriği (I-O, toplam) / KD÷üretim | %20 / %23 |
| RCA dünya (2020 → 2024) / AB pazarında | 1,64 → 1,52 / 0,71 |
| Birim değer ÷ AB pazarı ortalaması | 0,88 |
| AB pazar payı (AB dışı tedarik içinde, 2020 → 2024); TR'nin sırası | %3,9 → %2,8; 12. |

**4. AB tarafı maruziyet**

- `τ_AB` (S4 artışı, rota A, TR→AB 2025 ağırlıklı): %51,3; 1/98 kaybıyla %51,8; tam MFN ortalaması %51,8. Rejim: GB %0, İTÜ %95, tarım %5 `[V]`/`[T]`.
- Tepe satırlar (S4 artışı ≥ %10; en büyük 3): 8 satır, AB ihracatının %95'i: KN 2402 20 90 %57,6 (€98,8 mn); KN 2403 99 90 %16,6 (€15,6 mn); KN 2403 11 00 %74,9 (€9,0 mn).
- AB pazarında AB dışı rakipler (tercih durumu): BRA %21; IND %12; USA %7; MWI %6; CHN %5. Tercihli rakip payı %29.
- Menşe (S2 / S3): risk Y/Y; `c_RoO` %5,0 / %6,0; `p_uyum` 0,40 / 0,30 `[H]`. Kural: 2402: başlık 2401 tütününün ağırlıkça en az %70'i menşeli (Amerikan harmanı ithal Virginia/Burley içerir).
- EUDR kapsamındaki AB ihracatı payı: %0; SKDM: %0.
- Menşe: 2402 için 'başlık 2401 tütününün ağırlıkça en az %70'i menşeli'. Türk sigaralarında Virginia ve Burley ithal; şark tütünü yerli. Uyum olasılığı S2'de 0,40 `[H]`.
- Çok uluslu şirket AB pazarını AB fabrikalarından besleyebilir. PMI'ın Yunanistan'daki Papastratos fabrikası 2018'de ısıtılmış tütüne döndü `[V]`.

**5. Türkiye tarafı maruziyet**

- Uygulanan tarife (2026, ithalat ağırlıklı): MFN %29,1, İGV dahil %29,1 `[V]`. S4'te AB menşeline (c2): %22,3.
- Kritik girdiler (HS4 2401), Türkiye'nin toplam ithalatı 2024: $519 mn (AB %29; BEL %13, IND %11, DEU %11) `[V]`.
- ÖTV ile gümrük etkileşimi: sigarada ÖTV oransal + asgari maktu. S4'te AB'den gelen ürüne MFN (sigarada %41,7, ısıtılmış tütün ve diğer mamul tütünde %29,1) perakende fiyatın vergi öncesi kısmını artırıyor. Isıtılmış tütünde (KN 2404 11; HS2017'de 2403 99) MFN %0, S4 etkisinin %39'unu kaldırır.
- Isıtılmış tütünün Türkiye'de üretilip üretilmediği `[D?]` (PMI Torbalı'da ısıtılmış tütün hattı doğrulanmadı).

**6. Kabiliyet**

- KS 39,8 (sıra 206/230; ağırlık duyarlılığında P10–P90 157–219). Bileşenler: RCA 49, PCI 8 (PCI −1,08), yurt içi KD 58, Ar-Ge 25, tedarikçi 84, verimlilik 57, firma 17 `[T]`.
- Ürün uzayında atlanabilir ürünler (sınıf içi; yoğunluk üst çeyrek, PCI > sınıf): yok `[T]`.
- **Kırmızı çizgi yetkinlikleri:** Şark tütünü harman bilgisi ve yaprak işleme (Ege, Karadeniz); fabrikaların bölgesel ihracat merkezi rolü.
- **Geliştirme hedefi:** T+5: AB'ye kaybın AB dışı (Irak, Körfez, Kafkasya) ihracatla telafisi.

**7. Stratejik önem.** SS 0,0 (en yüksek boyut: — 0; ağırlıklı ortalama 0,0) `[H]`. Stratejik değil; kamu sağlığı ve vergi geliri açısından izlenir.

**8. Makro duyarlılık**

| Gösterge | Değer (`[T]`) |
|---|---|
| TÜFE ağırlığı (doğrudan, COICOP 2018 eşlemesi); tüketimde ithal pay | %2,16; %11 |
| ÜFE vekili (imalat üretimindeki pay) | %0,42 |
| EDE: 1 puan tarife, tüm menşe / yalnız AB (bp; ρ = 1) | 0,310 / 0,148 |
| Geçişkenlik ρ (senaryolarda) | 0,6–1,0 (P50 0,8) |
| Piyasa yoğunlaşması (250+ istihdam payı) | %75 |
| CKE: tarife ($ mn / bp) ve mali ($ mn / mlr TL); 0–100 puan | 215,2 ve 10,30; 26 |

**9. Senaryo etkileri, T+5, P50 (P10 / P90)**

| Değişken | S2 | S3 | S4 |
|---|---|---|---|
| AB'ye ihracat ($ mn) | −35 (−78 / +2) | −34 (−63 / −7) | −39 (−62 / −16) |
| Toplam ihracat ($ mn) | −25 (−57 / +2) | −24 (−46 / −5) | −31 (−50 / −13) |
| Nihai mal ithalatı ($ mn) | −9 (−30 / +26) | −14 (−36 / +15) | −46 (−84 / −10) |
| Cari denge ($ mn) | −15 (−26 / −10) | −9 (−17 / −5) | +11 (−3 / +28) |
| Üretim ($ mn) | −19 (−33 / −13) | −11 (−21 / −6) | +14 (−3 / +35) |
| İstihdam (kişi) | −27 (−48 / −17) | −16 (−30 / −9) | +20 (−5 / +49) |
| TÜFE (bp, birinci tur) | +0,29 (+0,25 / +0,33) | +0,55 (+0,47 / +0,63) | +2,73 (+2,34 / +3,09) |
| Yatırım ve DYY (bütün senaryolar) | AB'ye yönelik üretim hattının AB'ye kayması olası (S4 ve S2) `[H]` |  |  |

*Kaynak:* `[T]` f3e: kısmi denge, toplamlar Faz 2B GE dağılımına kalibre; S4'te 1/98 kaybı olasılığı 0,25.

**10. Politika paketi**

| Eylem ID | Araç | Parametre | Sorumlu | Hukuki araç | Bütçe | Başlangıç–bitiş; sunset | Performans koşulu | KPI |
|---|---|---|---|---|---|---|---|---|
| E-12.00-01 | S2'de PSR talebi | 2402: 'başlık değişikliği; menşesiz 2401 tütünü ağırlıkça ≤ %50' | Ticaret Bakanlığı | S2 menşe protokolü | İdari | T−18 → T; sunset: — | — | Kabul (olasılık düşük `[H]`) |
| E-12.00-02 | S4'te ısıtılmış tütünde MFN %0 | KN 2404 11 ve 2403 99: %29,1 → %0, tüm menşeler; ÖTV yapısı değişmez | Ticaret Bakanlığı, Hazine ve Maliye Bakanlığı | İthalat Rejimi Kararı eki | Gelir kaybı ≈ 0,5 mlr TL/yıl (AB dışı ithalat) `[T]` | T → T+36; sunset: T+36 | — | TÜFE tütün alt endeksi; −1,07 bp |

**11. Müzakere pozisyonu**

- AB ile savunma: PSR talebi; kabul görmezse AB'ye ihracat kaybını kabul et, karşılığında başka bir başlıkta taviz iste.

**12. Erken uyarı ve tetikler**

| Gösterge | Eşik | Tetiklenecek önlem |
|---|---|---|
| AB'ye sigara ihracatı (aylık) | Yıllık −%30 | Çok uluslu şirketlerle üretim hattı kararı görüşmesi; AB dışı pazar desteği |
| Kayıt dışı sigara payı (S4) | +2 puan | Gümrük ve Muhafaza denetimi |

**13. Kazanan ve kaybedenler; bölgesel ve sosyal etki; telafi.** Kaybeden: AB'ye ihracat yapan hat (P50'de istihdam etkisi küçük; iç ikame dengeliyor). Bölge: İzmir (%59).

**14. Riskler ve azaltım**

- AB'ye yönelik üretimin AB'ye kayması → kabullenilen kayıp; AB dışı pazar.
- Kaçakçılık (fiyat artışı) → MFN %0 (ısıtılmış tütün) ve denetim.

**15. Güven düzeyi; veri boşlukları; `[D?]`.** Orta. `[D?]`: ısıtılmış tütün üretiminin yeri; BAT'ın Türkiye'deki üretim durumu.


## 4. Ortak eylemler (10–12)

**Tablo 4.1 — Bölüm düzeyi eylemler**

| Eylem ID | Araç | Parametre | Sorumlu | Hukuki araç | Bütçe | Başlangıç–bitiş | Performans koşulu | Sunset | KPI |
|---|---|---|---|---|---|---|---|---|---|
| E-10-01 | 1/98 sürekliliği ve S2'ye aktarımı | (i) 1/98'in Ankara Anlaşması'na dayanan bağımsız hukuki dosyası; (ii) S2 metninde 1/98 tavizlerinin ve İTÜ rejiminin aktarımı; (iii) S4'te 1/98'i askıya alma girişimine karşı DTÖ ve Ortaklık Konseyi yolu | Ticaret Bakanlığı (Uluslararası Anlaşmalar ve AB GM), Dışişleri (AB Başkanlığı), Tarım ve Orman Bakanlığı (TOB) | Ortaklık Konseyi kararı; S2 anlaşma metni (Ek: tarım tavizleri) | İdari | T−18 → T | S2 metninde 1/98 tavizleri en az bugünkü kapsamda | Yok (anlaşmayla kalıcı) | 1/98 kapsamındaki AB ihracatı (€4,0 mlr civarı) T+1'de ≥ %95 |
| E-10-02 | Menşe uyumlu DİR: yerli eşdeğer eşya | AB'ye yönelik İTÜ ihracatında (Fasıl 17–21) DİR izin belgesiyle yerli (menşeli) buğday ve şeker kullanımı; ithal eşya serbest dolaşıma vergisiz girer (eşdeğer eşya). S2'de PSR talebi: Fasıl 19'da menşesiz tahıla fabrika çıkış fiyatının %15'ine kadar tolerans | Ticaret Bakanlığı (İhracat GM), TMO, Gümrükler GM | DİR Kararı ve Tebliği değişikliği; S2 menşe protokolü | Gelir etkisi ≈ 0 (vergi zaten alınmıyor) `[T]` | T−12 → T+60 | Belge sahibinin AB ihracatı ≥ yerli eşdeğer miktar | T+60 (PSR yürürlüğe girince gözden geçirilir) | Bisküvi/ekmek AB ihracatında menşe ispatlı pay ≥ %85 |
| E-10-03 | EUDR uyum masası | Kakao (10.82), kahve (10.83), soya/palm (10.41, 10.91) ve sığır (10.11, 15.11) için coğrafi konum verisi ve özen beyanı desteği; ithalatçı birlikleriyle ortak veri havuzu | TOB, Ticaret Bakanlığı, TİM (ilgili ihracatçı birlikleri) | Bakanlık genelgesi; TİM yönetim kurulu kararı | ≈ 0,05 mlr TL/yıl `[T]` | T−18 → T+24 | Kullanan firma sayısı | T+24 | EUDR nedeniyle AB'de reddedilen sevkiyat = 0 |
| E-10-04 | Ticaret savunması erken uyarı | Su ürünleri (10.20) ve işlenmiş meyve-sebzede (10.39) AB anti-damping ve sübvansiyon soruşturmalarına hazırlık: destek programlarının ASCM uyum dosyası, maliyet verisi | Ticaret Bakanlığı (İthalat GM ve İhracat GM), TOB, ilgili ihracatçı birlikleri | İç talimat | İdari | T−12 → T+36 | — | T+36 | Soruşturma açılırsa 30 gün içinde tam yanıt |
| E-10-05 | S4 geçiş tamponu (yalnız S4) | AB'ye İTÜ ihracatçılarına (10.62, 10.72, 10.82, 10.89, 11.07) ihracat kredi sigortası ve pazar çeşitlendirme desteği; yıllık tavan | Türk Eximbank, Ticaret Bakanlığı | Eximbank programı; İhracat Destekleri Kararı | 0,3 mlr TL/yıl × 3 yıl `[T]` | T → T+36 | AB dışı ihracat artışı | T+36 | Tampon kapsamındaki firmaların toplam ihracatı ≥ T−12 düzeyi |
| E-10-06 | Tarımda hücum gündemi (S2) | Meyve-sebzede giriş fiyatı sistemi istisnası, domates ve işlenmiş ürün kotalarının genişletilmesi, su ürünlerinde kota yerine sıfır tarife, kanatlı ve süt ürünlerinde SPS listelenme | Ticaret Bakanlığı, TOB | S2 anlaşma metni (tarım ve SPS bölümleri) | İdari | T−18 → T | AB'nin tarım hassas listesine karşılıklı taviz | — | Tavizli satırların AB ihracatı T+5'te +%10 |

*Kaynak:* Bütçeler `[T]`, kurumsal sorumluluk `[V]` (mevcut görev dağılımı), tutarlar 2026 fiyatlarıyla; mali yükler defterde toplanıyor.

## 5. Kümülatif defter

**Tablo 5.1 — Kümülatif defter (Faz 3, parça 1 sonrası)**

| Kalem | Değer |
|---|---|
| Tamamlanan / kalan sınıf | 33 / 197 C sınıfı; ek kapsam (B, D, E, hizmet) 0 / 29 |
| Kullanılan / kalan enflasyon bütçesi (bp; birinci tur, P50) | S2 yolu: şok 0,9 + önlem −0,11 = 0,8 bp; S4 yolu: şok 6,2 + önlem −1,55 = 4,7 bp. Kümülatif 50 bp bütçeden kalan: S2 49,2, S4 45,3 bp |
| Kümülatif cari denge katkısı ($ mlr/yıl, T+5) | Senaryo P50: S2 −0,044, S4 +0,030 (S4 P10 −1,06); önlemler: S2 +0,071, S4 +0,010 `[T]`/`[H]` |
| Kümülatif mali maliyet (mlr TL/yıl; GSYH %) | S2 yolu 0,83 (%0,001); S4 yolu 1,69 (%0,002) |
| Riskteki istihdam (kişi, T+5) | S2 P50 −284; S4 P50 −15, P10 −4.698. S4 P10'da kaybı %5'i aşan sınıf: yok |
| Açık kalan veri boşlukları | VB-30: sınıf düzeyinde yabancı sermaye payı (TÜİK yabancı kontrollü girişim istatistikleri yalnız bölüm düzeyinde); VB-31: Türkiye'ye özgü sınıf düzeyi Ar-Ge yoğunluğu (OECD sınıflaması vekil); VB-32: DTÖ bağlı oranları, satır düzeyi (WTO CTS); 10–12'de tarife artışı önerilmediği için bağlayıcı değil, sonraki parçalarda gerekli; VB-33: TMO yerli buğday fiyatı ile ithal paritesi farkı (menşe maliyeti c_RoO'nun kalibrasyonu); VB-34: EUDR kapsamındaki ihracatçıların tedarik zinciri verisi; VB-35: YSHİ ile BACI sınıf eşlemesindeki tutarsızlık (10.86; 11.03, 11.04, 11.06'da YSHİ verisi yok); VB-06 (sürüyor): 1/98 tercih oranları satır düzeyinde; 1/98 kaybı varyantı bu yüzden üst sınır |
| Varsayım kaydına eklenen yeni maddeler | V-30: Faz 3 senaryoları — toplam GE'den, dağılım kısmi dengeden (ortak z, N = 2.000); V-31: S4'te 1/98'in askıya alınma olasılığı 0,25 (hasmane AB) `[H]`; V-32: ticaret esnekliği σ — ProTEE HS6, sınıf içi AB ihracatı ağırlıklı medyan, [2, 15]; V-33: sınır sürtünmesi %0,5–2 (yalnız GB ve İTÜ), S2'de × 0,5; AB ihracatçısının menşe maliyeti S2 %0,5, S3 %1; V-34: arketip eşikleri (KS, AME, ithalat penetrasyonu, EDE ≥ 0,3 bp/puan, SS ≥ 60) `[H]`; V-35: SS boyut puanları ve ağırlıkları `[H]` (veri/f3_ss_boyutlar.csv; 10–12 gözden geçirildi, diğerleri ilk tahmin); V-36: CKE tanımı — 1 puan tarife / %1 üretim desteği, 5 yıl, kapasite yatırımının ithalatı (sermaye/hasıla 1, ithal payı 0,6) düşülü; V-37: KN8 → NACE eşlemesinde CPA 2.2 → 2.1 kimlik bağlantısı önceliği (D-1) |

*Kaynak:* Bu tablo `kod/f3g_kartlar.py` ile matristen ve kartlardaki önlem kayıtlarından üretildi. Senaryo şokları politika seçimi değil, çıkışın kendisi; önlemler kartların eylem tablolarından. Makro mutabakat Faz 6'da.


**Kontrol listesi (parça 1).**
1. Etiketler: her sayının etiketi, birimi ve dönemi var. Sınıf değerleri 2024, AB tarifeleri 2026, senaryolar T+5.
2. Toplam ve çift sayım: bölüm toplamları matristen (230 sınıf); EDE toplamı I-O ile tutarlı (22,0 / 23,5 bp). KKTC ve KN8 düzeltmeleri yapıldı (D-1, D-2).
3. Kısıtlar:
   - S2 yolunda 10–12'nin birinci tur TÜFE etkisi 0,9 bp (önlem değil, sürtünme şoku).
   - S4 yolunda 6,2 bp; önlemler (E-10.82-01, E-10.86-01, E-12.00-02) bunu 1,55 bp düşürüyor (Tablo 5.1).
   - Mali kısıt: önlemler S2 yolunda 0,8, S4 yolunda 1,7 mlr TL/yıl (GSYH'nin %0,002'si; Tablo 5.1).
   - İstihdam: S4'ün P10 değerinde 10.39 −%4,9 ile %5 eşiğine yakın; tetik tanımlandı.
4. Tarife önerileri: 10–12'de bağlı oranı aşan öneri yok. Öneriler ya MFN'yi koruyor ya indiriyor; ITA bu bölümleri kapsamıyor; STA kontrolü kartlarda.
5. DTÖ: E-10-02, DİR'in mevcut eşdeğer eşya rejimi içinde. Tarım ürünlerinde ihracat sübvansiyonu yasağına (Nairobi 2015) takılmamak için TMO satışı ihracat koşullu indirimle yapılmıyor.
6. "Pazartesi sabahı": eylemlerde kurum, hukuki araç, bütçe, tarih ve KPI var. Bütçe ve tarih kalibrasyonu Faz 5–8'de.
7. AB tepkisi: 1/98'in askıya alınması (0,25) ve ticaret savunması (10.20, 10.39) fiyatlandı.
8. Zaman yolu: eylemler T−18 → T+60.
9. Kaçınılacak hatalar: tarım satırlarına GB tarifesi eklenmedi (hata 15); spesifik vergiler AVE'ye çevrildi.
10. Kaçamak ifade bırakılmadı. Belirsiz olgular `[D?]` olarak işaretli.
11. Olumsuz bulgular girişte (sigara, fındık kaldıracının sınırı).

İLERLEME: Faz 3 parça 1 / 16 tamamlandı (33 / 230 C sınıfı kartı) — SONRAKİ ADIM: Faz 3 parça 2 (13–15: tekstil, giyim, deri); DEVAM bekleniyor.
