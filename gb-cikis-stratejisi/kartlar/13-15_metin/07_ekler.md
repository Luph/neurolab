## Ek A — Ana matris satırları

Ana matrisin bütün sütunları ve 230 imalat sınıfının tamamı `veri/nace_matris.csv` dosyasında. Aşağıdaki iki tablo çalışma çerçevesinin öngördüğü matris sütunlarını 13–15 sınıfları için veriyor. Skorlar 0–100 arasında, C sınıfları içindeki yüzdelik sıra olarak ifade ediliyor.

{{TABLO:matris_a|A.1}}

{{TABLO:matris_b|A.2}}

## Ek B — Yöntem: bu parçadaki yenilikler

Hesap zinciri ilk parçanın Ek B'sinde anlatıldı ve değişmedi: f3a–f3f bütün 230 sınıfı birlikte hesaplıyor, f3g her parçanın belgesini üretiyor. Bu parçada zincire dört ekleme yapıldı ve parçaya özgü varsayımlar derlendi. Tablo B.1 değişen betikleri özetliyor.

**Tablo B.1 — Bu parçada değişen betikler ve tablolar**

| Betik ya da tablo | Değişiklik | Etiket |
|---|---|---|
| `kod/f3a_ticaret.py` | PEM kümülasyonu maruziyeti: PEM ortaklarına ihracat (`x_pem`) ve ortağın AB payıyla ağırlıklı maruziyet (`x_kum`); `veri/f3_pem_ortak_ab_payi.csv` | `[V]` veri, `[T]` eşleme |
| `kod/f3d_ab_tarife.py` | EUDR kapsamı Tüzük 2026/2102'ye göre güncellendi; 30.12.2027'den eklenen satırlar ayrı bayrakla (`eudr_2027`) | `[V]` |
| `kod/f3e_senaryo.py` | S4'te PEM kümülasyonu kanalı (`dx_kum`, `dl_kum`, `dca_kum`) | `[T]`; parametreler `[H]` |
| `kod/f3f_skor_matris.py` | Arketip düzeltmesinin kaydı ikincil arketipi de gösteriyor | — |
| `kod/f3g_kartlar.py` | Parça numarası ve etiketi YAML'dan; kümülatif defter bütün parçaların kayıtlarından; bölge ve kümülasyon tabloları; "−şok" kaydıyla TÜFE önleminin veriden çözülmesi | — |
| `veri/f3_sinif_varsayim.csv` | 13–15 için menşe kuralları, c_RoO, p_uyum, değer zinciri rolü, DİR bağımlılığı ve κ | `[H]`; kurallar `[V]` |
| `veri/f3_ss_boyutlar.csv` | 13–15 için stratejik önem boyutları gözden geçirildi | `[H]` |

**PEM kümülasyonu kanalı.** Kanal, Türk girdisinin bir PEM ortağında işlenip AB'ye tercihli satıldığı zincirleri yakalıyor. Ortaklar, hem Türkiye hem AB ile yürürlükte tercihli anlaşması olan PEM taraflarıdır: Fas, Tunus, Mısır, Batı Balkan ülkeleri, Gürcistan, Moldova, Ukrayna, EFTA ve Faroe Adaları. İsrail ile ticaret askıda olduğu için, Ürdün, Cezayir ve Lübnan ile de Türkiye'nin yürürlükte bir anlaşması olmadığı için dışarıda bırakıldı. Sınıf i için maruziyet, Türkiye'nin 2024'te her ortağa sınıf i'de yaptığı ihracatın, ortağın aşağı yöndeki ürünlerde AB'ye ihracat payıyla çarpımlarının toplamı. Aşağı yön ürünleri tekstil (13) için Fasıl 61–63, diğer bölümler için ortağın toplam ihracatı. S4'teki kayıp λ · κ_i · maruziyet_i. κ_i, Türk girdisinin ortağın ürününde menşe kazandıran adım olma derecesi: dokuma ve örme kumaşta 1, teknik ve diğer tekstilde 0,3, diğer bütün sınıflarda 0 `[H]`. Kayıp oranı λ, %30–90 arasında tepe değeri %60 olan üçgen bir dağılımdan, ortak bir çekilişle alınıyor `[H]`. Kayıp genel denge toplamının üstüne ekleniyor, çünkü Faz 2B'nin genel denge modeli üçüncü ülkeler üzerinden kurulan menşe zincirlerini içermiyor. S2 ve S3'te kanal yok, çünkü yeni anlaşma PEM'e atıf yaptığı sürece kümülasyon sürüyor. λ çekilişi, önceki çekilişlerden sonra yapıldığı için ilk parçanın sonuçlarını değiştirmiyor.

**Menşe parametreleri.** Tekstil, giyim ve deri sınıflarının menşe kuralı, revize PEM kurallarının ürüne özgü listesinden alındı (Tablo 3.4) `[V]`. Uyum oranı (p_uyum) ve uyumlu ihracatın menşe maliyeti (c_RoO) bu kurallara ve Faz 2C'nin Asya kumaşı tahminine göre belirlendi `[H]`. Kumaş, iplik, halı, deri eşya ve ayakkabıda risk düşük (p_uyum 0,92, c_RoO %1,5). Giyimde risk orta: dış giyimde p_uyum 0,86 ve c_RoO %2,5, iç giyimde 0,88 ve %2,0. Geri ödeme yasağı için ek maliyet eklenmedi (V-42).

**Bölgesel dağılım.** Bölge tablosundaki değerler, her sınıfın S2 ve S4 istihdam etkisinin (P50) o sınıfın İBBS-2 bölge paylarıyla dağıtılmasından geliyor. Bölge payları f3b'de TÜİK sınıf çalışanı ile SGK'nın bölüm × il sigortalı verisinin RAS yöntemiyle uzlaştırılmasından türetildi. Bölgedeki imalat payı aynı yöntemle bütün C sınıfları üzerinden hesaplandı. Değerler sınıf medyanlarının toplamıdır, grup dağılımının medyanı değil.

**Kümülatif defter ve vergi takası.** Defter bu parçadan itibaren kümülatif. f3g, `kartlar/` klasöründeki bütün parça dosyalarını okuyor ve son bölümü bu parçanınkinden büyük olmayan parçaların eylem kayıtlarını topluyor. Senaryo toplamları 10–[son bölüm] grubunun çekiliş dağılımından alınıyor. Vergi takasının TÜFE etkisi sınıf defterlerinde "−şok" olarak kayıtlı. f3g bu kaydı ilgili sınıfın S4 TÜFE şokuyla (P50) değiştiriyor; böylece takas, tasarımına uygun olarak şoku siliyor ve model değiştiğinde kayıt kendiliğinden güncelleniyor. Takasın net mali maliyeti Faz 2A'nın merkez değeri (Laspeyres kuralı, c2 rejimi; giyim 319, ayakkabı 63 milyon dolar; 2026 ortalama kuru {{mk:13.10|usd_try_2026|2}} TL) `[T]`.

## Ek C — Sınıf veri sayfaları

Her veri sayfası sınıf kartının sayısal alanlarını bir arada veriyor. Senaryo tablosu Bölüm 5'te verilen sınıflar için sayfada ilgili tabloya atıf var; diğer sınıfların senaryo tablosu sayfanın hemen altında. Veriler `[V]`; eşleme, bölge payları ve skorlar `[T]`; menşe parametreleri, kümülasyon katsayısı ve stratejik skor `[H]`.

{{VERI_SAYFALARI|C}}

## Ek D — Önceki parçalara ve fazlara düzeltmeler

**D-4. EUDR kapsamı.** AB'nin 2026/2102 sayılı Yetki Devrine Dayanan Tüzüğü 17 Eylül 2026'da Resmî Gazete'de yayımlandı ve ertesi gün yürürlüğe girdi `[V]`. Tüzük, EUDR Ek I'den sığır derisini (ex 4101, ex 4104, ex 4107) ve bazı vulkanize kauçuk eşyayı (ex 4010, ex 4016) çıkardı. Kullanılmış lastiği ve tohumluk soyayı kapsam dışı bıraktı, ahşap oturma yerlerini daralttı. Hazır kahveyi (2101 11 00), dondurulmuş sığır dilini ve on dört palm türevini 30 Aralık 2027'den itibaren kapsama aldı. İlk parçada kullanılan EUDR listesi bu değişikliği içermiyordu. Liste güncellendi. İlk parçanın metnindeki EUDR paragrafları ve EUDR uyum masasının (E-10-03) kapsamı buna göre düzeltildi. Sınıf payları da değişti: tabaklamada (15.11) %62'den sıfıra, kahvede (10.83) hazır kahvenin eklenmesiyle %{{ab:10.83|eudr_payi|0|pct}} düzeyine. Tabaklamanın kural tabanlı arketipi "Yeşil Mutabakat'a maruz" (G) olmaktan çıktı. Bu parçada uzman düzeltmesiyle ikincil arketip olarak korundu, ama gerekçesi artık EUDR değil, alıcıların çevre özen yükümlülükleri (Bölüm 5.13).

**D-5. İlk parçanın S2 sonuçları ve imalat toplamları.** S2'de AB'ye ihracattaki toplam kayıp genel denge sonucuna bağlı ve sınıflara kısmi denge kayıp paylarıyla dağıtılıyor. Bu parçada giyimin menşe parametreleri varsayılan düşük riskten orta riske çekildi; bu, S2 kaybının bir kısmını giyime kaydırdı ve diğer sınıfların S2 kaybını çok az küçülttü. İlk parçanın S2 istihdam etkisi {{g:10-12:S2|dl|p50|0|isaret}} kişi oldu (önceki sürümde −299). S4'te ise PEM kümülasyonu kanalı imalatın toplam istihdam kaybını büyüttü: medyan {{oz:S4|dl_p50|1|bin}} bin kişi (önceki sürümde −41,2 bin), P10 {{oz:S4|dl_p10|1|bin}} bin kişi. İlk parçanın belgesi bu sayılarla yeniden üretildi; metnindeki bütün sayılar veriden geldiği için ayrıca düzeltme gerekmedi.

**D-6. Faz 2'nin giyim istihdam tahmini.** Faz 2A ve 2C, aktif S4'te giyimde yaklaşık 59 bin kişilik net istihdam kaybı raporlamıştı. Bu tahmin tek bir esneklik değeriyle (σ = 5), genel denge kalibrasyonu olmadan, durağan bir yöntemle yapılmıştı. Faz 3'ün genel dengeye kalibre modelinde giyim bölümünün (14) S4 kaybı medyanda {{g:14:S4|dl|p50|0|abs}}, dağılımın alt ucunda {{g:14:S4|dl|p10|0|abs}} kişi. Faz 2'nin tahmini bu dağılımın alt ucundan da büyük bir kayıp gösteriyordu ve Faz 3 kartlarıyla geçersiz. Faz 2'nin vergi takası hesabı (02a, Tablo 1.5a) ise geçerli ve bu parçanın defterinde kullanıldı.

## Ek E — Varsayımlar ve veri boşlukları

Bu parçada varsayım kaydına dört yeni madde eklendi ve beş veri boşluğu açıldı ya da güncellendi. VB-32, yani DTÖ bağlı oranları, bu parçada bağlayıcı olmadı. c2 uygulanan MFN oranlarını değiştirmiyor; giyimde de tarife satırlarının yalnızca %3,7'si bağlı. Bağlı oranlar, MFN artışı önerilen ilk parçada yeniden ele alınacak.

{{TABLO:varsayim|E.1}}

{{TABLO:vb|E.2}}

{{ILERLEME}}
