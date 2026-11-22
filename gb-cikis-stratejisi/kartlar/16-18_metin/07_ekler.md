## Ek A — Ana matris satırları

Ana matrisin bütün sütunları ve 230 imalat sınıfının tamamı `veri/nace_matris.csv` dosyasında. Aşağıdaki iki tablo çalışma çerçevesinin öngördüğü matris sütunlarını 16–18 sınıfları için veriyor. Skorlar 0–100 arasında, C sınıfları içindeki yüzdelik sıra olarak ifade ediliyor.

{{TABLO:matris_a|A.1}}

{{TABLO:matris_b|A.2}}

## Ek B — Yöntem: bu parçadaki yenilikler

Hesap zinciri ilk parçanın Ek B'sinde anlatıldı ve değişmedi: f3a–f3f bütün 230 sınıfı birlikte hesaplıyor, f3g her parçanın belgesini üretiyor. Bu parçada zincire iki ekleme ve bir düzeltme yapıldı, parçaya özgü varsayımlar derlendi. Tablo B.1 değişen betikleri ve tabloları özetliyor.

**Tablo B.1 — Bu parçada değişen betikler ve tablolar**

| Betik ya da tablo | Değişiklik | Etiket |
|---|---|---|
| `kod/f3e_senaryo.py` | İç ikame tavanı (`ikame_tavani`) ve CE ve onaylanmış kuruluş bağımlılığı (`ce_payi`) sınıf tablosundan okunuyor; S2 ve S3'te menşe maliyeti yalnız tercihin kurtardığı tarife kadar sayılıyor (ihracatta ve ithalatta) | `[T]`; parametreler `[H]` |
| `kod/f3g_kartlar.py` | Bölge tablosunun çalışana göre sıralanan biçimi (`bolge_l`) | — |
| `kod/requirements.txt` | pyfixest 0.60.0'a sabitlendi (0.70, f2f'nin kullandığı bir parametreyi kaldırdı); PyYAML ve matplotlib eklendi | — |
| `veri/f3_sinif_varsayim.csv` | 16–18 için menşe kuralları, c_RoO, p_uyum, değer zinciri rolü ve DİR bağımlılığı; iki yeni sütun | `[H]`; kurallar `[V]` |
| `veri/f3_ss_boyutlar.csv` | 16–18 için stratejik önem boyutları gözden geçirildi | `[H]` |

**İç ikame tavanı.** Kısmi denge modelinde AB'den ithalattaki düşüşün bir kısmını yerli üretim karşılıyor: ΔD = −ΔM_AB · D/(D + M_AB-dışı), D sınıfın iç satışı. Bu formül, yerli üretimin aynı ürünü üretebildiğini varsayıyor. Kâğıt hamurunda bu varsayım geçerli değil: yurt içi üretim yok denecek kadar az ve sınıfın verisi gizli olduğu için formül, ithal paylarına dayanan bir yedek değer kullanıyordu. Sınıf tablosuna eklenen `ikame_tavani` sütunu, iç ikame payını bir üst sınırla kısıtlıyor; boş bırakılan sınıflarda bir değişiklik yok. Bu parçada yalnızca kâğıt hamurunda tavan tanımlandı ve değeri sıfır (V-44). Kâğıt ve kartonda tavan gerekmedi. AB'den ithalattaki düşüş, c2'nin İGV koyduğu ve yerli üretimin güçlü olduğu satırlarda yoğunlaşıyor; sınıfın ortalama iç ikame payı (%{{17.12|yerli_pay|0|pct}}) bu yoğunlaşmayla tutarlı. Yanlış sınıflanan satırlar (VB-43) E-17.12-01 ile ele alınıyor.

**CE ve onaylanmış kuruluş bağımlılığı.** Model, AB'ye satışında AB'nin tanıdığı bir kuruluşun deneyini ya da belgesini gerektiren ihracat payına, S4'te değerin %1–4'ü, S2'de bunun dörtte biri kadar bir maliyet ekliyor. Bu kanal ilk parçadan beri modeldeydi, ama bütün sınıflarda pay sıfırdı. Bu parçada pay, sınıf tablosundaki `ce_payi` sütunundan okunuyor ve yapı ürünleri için tanımlandı: ahşap levhada 0,15 (taşıyıcı levha ve yangın tepkisi deneyi gereken ürünler), ahşap döşemede 0,5, doğramada 0,3 (pencere ve dış kapı) (V-45). Elektrikli ekipman, makine, otomotiv, tıbbi cihaz ve oyuncakta bu pay sonraki parçalarda belirlenecek ve orada çok daha belirleyici olacak.

**S2 ve S3'te menşe maliyeti.** Serbest ticaret anlaşmasında ihracatçı, tercihli tarifeden yararlanmak için menşe ispatlamak zorunda; bunun maliyeti modelde c_RoO. Ama tercihin bir değeri ancak MFN tarifesi pozitifse var. AB'nin MFN tarifesi sıfır olan bir üründe ihracatçı tercih istemez, menşe ispatına da katlanmaz; MFN'yi öder ve bu sıfırdır. Model şimdiye kadar menşe maliyetini tarifeden bağımsız olarak, menşe kuralına uyan bütün ihracata ekliyordu. Bu parçada fiyat kaması τ_etkin = (1 − p_uyum)·τ + q·p_uyum·min(c_RoO, τ) + NTM + CE biçimine getirildi: uyumlu ihracatçı, menşe maliyeti ile tarifenin küçüğünü öder. Aynı düzeltme ithalat tarafında AB'li ihracatçının menşe maliyetine de uygulandı. Düzeltme sınıf ortalaması düzeyinde yaklaşık, çünkü bir sınıfın içinde tarifeli ve tarifesiz satırlar bir arada olabilir (V-49). S2'nin toplam AB ihracatı kaybı genel denge modelinden geldiği için düzeltme bu toplamı değiştirmiyor; kaybın sınıflara dağılımını değiştiriyor. Tarifesi sıfır ya da çok düşük sınıfların (kâğıt, bazı makine, mobilya, gemi ve tıbbi cihaz sınıfları) S2 kaybı küçülüyor, tarifeli ve emek yoğun sınıflarınki büyüyor (Ek D).

**Menşe parametreleri.** Ağaç, kâğıt ve basım sınıflarının menşe kuralı revize PEM kurallarından alındı; Fasıl 44, 47 ve 48'in ürünlerinin büyük çoğunluğunda kural başlık değişikliği `[V]`. Bu yüzden bütün sınıflarda S2 menşe riski düşük: uyum oranı (p_uyum) 0,95, uyumlu ihracatın menşe maliyeti (c_RoO) %1; S3'te 0,92 ve %1,5 (V-46). Geri ödeme yasağı bu fasıllarda uygulanmıyor.

**EUDR payı.** Sınıfların EUDR payı (f3d), AB'ye ihracatın EUDR kapsamındaki KN kodlarına giren kısmı. Tüzük 2025/2650 ile basılı ürünlerin (Fasıl 49) kapsamdan çıkarılması bu parçanın sınıflarını etkilemedi, çünkü Fasıl 49 yayıncılık sınıflarına sayılıyor. Tamamen geri dönüştürülmüş liften yapılan ürünlerin ve yalnızca taşıma amaçlı kullanılan ambalajın kapsam dışı olması ise KN koduyla ayrılamıyor; bu yüzden pay bir üst sınır (V-47, VB-41).

**Yeni ortamda yeniden üretim.** Bu parça yeni bir çalışma ortamında hazırlandı. Paketin bütün betikleri çevrimdışı kipte, yalnızca paketteki girdilerle yeniden çalıştırıldı. Model değişikliklerinden önce, ikinci parçanın çıktılarının tamamı bayt bayt aynı üretildi; tek fark, pyfixest'in yeni sürümünün f2f'nin kullandığı bir parametreyi kaldırmasıydı ve sürüm sabitlendi. Bu parçanın sonundaki yeniden üretim sınaması README'de.

## Ek C — Sınıf veri sayfaları

Her veri sayfası sınıf kartının sayısal alanlarını bir arada veriyor. Senaryo tablosu Bölüm 5'te verilen sınıflar için sayfada ilgili tabloya atıf var; diğer sınıfların senaryo tablosu sayfanın hemen altında. Veriler `[V]`; eşleme, bölge payları ve skorlar `[T]`; menşe parametreleri, CE payı, iç ikame tavanı ve stratejik skor `[H]`.

{{VERI_SAYFALARI|C}}

## Ek D — Önceki parçalara ve fazlara düzeltmeler

**D-7. Kâğıt hamurunda iç ikame ve imalat toplamları.** Kâğıt hamurunda (17.11) iç ikame tavanının sıfırlanması, sınıfın S2'deki 129 ve S4'teki 98 kişilik anlamsız istihdam artışını kaldırdı. Bu artış önceki parçaların imalat geneli toplamlarına giriyordu. İmalatın S4 istihdam etkisi medyanda −46,2 bin kişi oldu (ikinci parçada −46,1 bin).

**D-8. İlk iki parçanın S2 ve S3 sonuçları.** S2'de AB'ye ihracattaki toplam kayıp genel denge sonucuna bağlı ve sınıflara kısmi denge kayıp paylarıyla dağıtılıyor. Bu parçadaki iki değişiklik bu dağılımı kaydırdı. Birincisi ve büyüğü, S2'de menşe maliyetinin yalnız tercihin kurtardığı tarife kadar sayılması (Ek B, V-49). İkincisi, ağaç, kâğıt ve basımın menşe parametrelerinin varsayılan değerlerden (c_RoO %1,5, p_uyum 0,90) sınıfa özgü değerlere (%1, 0,95) çekilmesi. İkisi de tarifesi düşük sınıfların S2 kaybını küçültüp tarifeli sınıflarınkini büyüttü. İkinci parçanın S2 istihdam etkisi −15.453 kişi oldu (önceki sürümde −14.419; P10 −32.928), ilk parçanınki −318 (önceki sürümde −286). İmalatın S2 istihdam etkisi −24,9 bin kişi (önceki sürümde −24,3 bin). S3'ün genel denge toplamı, S2 ile S4'ün kısmi denge toplamları arasındaki konumuyla belirlendiği için S3 sonuçları da değişti. S4 sonuçları yalnız CE kanalının ahşap sınıflarına eklenmesiyle çok az değişti. İkinci parçanın temel bulgusu değişmiyor, hatta güçleniyor: giyimde iyi bir anlaşmanın değeri büyük ve S2'de bile kayıp kalıcı. İlk iki parçanın belgeleri bu sayılarla yeniden üretildi; metinlerindeki bütün sayılar veriden geldiği için ayrıca düzeltme gerekmedi.

**D-9. Faz 2C'nin son tarihleri.** Faz 2C'nin listelediği iki son tarih bu belgenin tarihine çok yaklaştı. DS629'da (Çin–Türkiye) panel raporunun kabulü ya da temyizi için son gün 24 Kasım 2026, yani bu belgenin tarihinden iki gün sonra; bir temyiz başvurusuna ilişkin kayıt bulunamadı `[D?]`. 2027–2029 dönemi için GATT XXVIII:5 çekincesinin son günü 31 Aralık 2026; Türkiye'nin bir bildirimine ilişkin kayıt da bulunamadı `[D?]`. İki hamlenin (H-D1, H-D2) önceliği Faz 2C'de belirlendi ve değişmedi; durumları `DURUM_OZETI.md`'de açık konular arasında izleniyor.

## Ek E — Varsayımlar ve veri boşlukları

Bu parçada varsayım kaydına altı yeni madde eklendi, bir madde güncellendi, beş veri boşluğu açıldı ve biri güncellendi. VB-32, yani DTÖ bağlı oranları, bu parçada da bağlayıcı olmadı: c2 uygulanan MFN oranlarını değiştirmiyor ve önerilen tek tarife değişikliği (E-17.12-01) bir indirim.

{{TABLO:varsayim|E.1}}

{{TABLO:vb|E.2}}

{{ILERLEME}}
