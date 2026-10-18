## Ek A — Ana matris satırları

Ana matrisin bütün sütunları ve 230 imalat sınıfının tamamı `veri/nace_matris.csv` dosyasında. Aşağıdaki iki tablo, çalışma çerçevesinin öngördüğü matris sütunlarını 10–12 sınıfları için veriyor. Skorlar 0–100 arasında, C sınıfları içindeki yüzdelik sıra olarak ifade ediliyor.

{{TABLO:matris_a|A.1}}

{{TABLO:matris_b|A.2}}

## Ek B — Yöntem

Faz 3'ün hesap altyapısı bütün 230 imalat sınıfı için bir kez kuruldu; sonraki parçalar aynı tabloları kullanacak. Zincir yedi betikten oluşuyor ve Tablo B.1'de özetleniyor. Bütün betikler `kod/` klasöründe, girdileri `girdi/` klasöründe, çıktıları `veri/` klasöründe; paket çevrimdışı olarak baştan üretilebiliyor (`kod/hepsini_uret.sh`).

**Tablo B.1 — Faz 3 hesap zinciri**

| Betik | Ne üretiyor | Ana kaynak | Etiket |
|---|---|---|---|
| `kod/f3a_ticaret.py` | Sınıf düzeyinde ihracat, ithalat, AB ve Çin payları, RCA (dünya ve AB pazarı), AB pazar payı, birim değer, ilk beş pazar, kaynak ve rakip | BACI HS17 2020 ve 2024 (Türkiye'nin ikili ticareti; AB27 ithalatı; dünya ihracatı) | `[V]` veri, `[T]` eşleme |
| `kod/f3b_yapi.py` | Üretim, katma değer, istihdam, ölçek dağılımı, İBBS-2 bölge payları, AB'ye göre verimlilik | TÜİK YSHİ 2024, İş Kayıtları 2024, SGK 2025, Eurostat SBS 2023 | `[V]`; bölge ve gizli hücre `[T]` |
| `kod/f3c_karmasiklik.py` | Ürün karmaşıklığı (PCI), ülke karmaşıklığı (ECI), ürün uzayı yoğunluğu, atlanabilir ürünler | BACI 2024 ihracatçı × HS6 (157 ülke, 4.858 ürün) | `[T]` |
| `kod/f3d_ab_tarife.py` | KN8 düzeyinde AB MFN tarifesi, spesifik vergilerin ad valorem eşdeğeri, rejime göre S4 artışı, tepe satırlar, EUDR ve SKDM payları | AB Kombine Nomenklatürü 2026, Comext 2025 (değer ve miktar) | `[V]`; eşdeğer `[T]` |
| `kod/f3e_senaryo.py` | S2, S3 ve S4'te sınıf etkileri (P10–P50–P90), bölüm ve parça toplamlarının dağılımı, 1/98 askısına koşullu sonuçlar, EDE, CKE | f3a–f3d, I-O 2023, ProTEE esneklikleri, Faz 2B genel denge sonuçları | `[T]` |
| `kod/f3f_skor_matris.py` | KS, SS, AME, EDE ve CKE puanları, arketip, duruş, ağırlık duyarlılığı, ana matris | f3a–f3e, `veri/f3_ss_boyutlar.csv`, kartların uzman düzeltmeleri | `[T]`; SS `[H]` |
| `kod/f3g_kartlar.py` | Bu belge: `kartlar/10-12_metin/` şablonları, yer tutucular veriden doldurularak | f3a–f3f, `kartlar/10-12*.yaml` | — |

**Senaryo modeli.** Modelin toplamları Faz 2B'nin genel denge (GE) sonuçlarından geliyor. Her Monte Carlo çekilişinde (N = 2.000; tohum 20261018) AB'ye toplam ihracat ve ithalattaki değişim, GE dağılımından ortak bir standart normal çekilişle alınıyor. S4'te AB'ye ihracat −%18,9 (%90 güven aralığı −32,4 ile −4,6), S2'de −%11,1 (−26,7 ile +6,1). Bu toplam, sınıflara kısmi denge yapısıyla dağıtılıyor: her sınıfın AB'ye ihracatındaki kısmi denge değişimi X[(1 + τ)^(−σ) − 1] ile hesaplanıyor. Burada τ, sınıfın etkin ticaret maliyeti artışı (tarife, sınır sürtünmesi ve menşe maliyeti), σ ise ürün düzeyindeki ikame esnekliği. Toplam kayıp kısmi denge kayıp paylarıyla dağıtılıyor. S3, iki senaryonun kısmi denge yapısıyla ara değer alıyor. Kalibrasyon ölçeği, yani genel denge toplamının kısmi denge toplamına oranı, S2'de {{oz:S2|olcek_ihracat|2}}, S3'te {{oz:S3|olcek_ihracat|2}}, S4'te {{oz:S4|olcek_ihracat|2}}. Ürün düzeyindeki esnekliklerle kısmi denge, genel dengenin yaklaşık iki katı kayıp üretiyor; ölçek bu farkı düzeltiyor.

S4'te 1/98'in askıya alınması her çekilişte 0,25 olasılıkla gerçekleşiyor ve tarım satırlarına AB'nin tam MFN tarifesi ekleniyor. Bu ek kayıp genel denge toplamının üstüne konuyor, yeniden dağıtılmıyor. Sınır sürtünmesi %0,5–2 arasında üçgen dağılımla çekiliyor ve yalnızca Gümrük Birliği'ne bağlı (GB ve İTÜ) satırlara uygulanıyor; S2'de yetkilendirilmiş yükümlü statüsünün karşılıklı tanınması ve tek pencereyle yarıya iniyor. Menşe maliyeti ve uyum olasılığı her sınıf için varsayım tablosundan (`veri/f3_sinif_varsayim.csv`) geliyor `[H]`; tarım satırları bugün de menşe kuralına tabi olduğu için onlara ek menşe maliyeti eklenmiyor. İthalat tarafında AB ihracatçısının menşe maliyeti S2'de %0,5, S3'te %1; uyum olasılığı 0,92 ve 0,85. Ticaretin yön değiştirmesiyle AB dışı pazarlara kayan ihracat payı (δ) S2'de {{oz:S2|delta|2}}, S4'te {{oz:S4|delta|2}}. Üretim değişimi, ihracat değişimi ile iç pazarda yerli ürünün AB ithalatından kazandığı payın toplamı. İstihdam etkisi, üretim değişiminin sınıfın çalışan/üretim oranıyla çarpılmasından ve istihdama yansımayan payın (θ; 0,1–0,5 arasında üçgen dağılım, tepe değeri 0,3) düşülmesinden; cari denge etkisi ise üretim değişiminden ithal girdi içeriğinin düşülmesinden geliyor. Bölüm ve parça toplamlarının yüzdelikleri, sınıf yüzdeliklerinin toplanmasıyla değil, her çekilişteki toplamın dağılımından alınıyor (V-38).

**Esneklikler ve tarifeler.** İkame esneklikleri CEPII'nin ProTEE veritabanından (Fontagné, Guimbard ve Orefice 2022) HS6 düzeyinde alındı, sınıf içinde AB'ye ihracatla ağırlıklandırılıp medyanı hesaplandı ve [2, 15] aralığına kırpıldı; 230 sınıfın medyanı 7,75. AB tarifeleri 2026 Kombine Nomenklatürü'nden KN8 düzeyinde alındı. Spesifik vergiler (100 kilogram, ton, kilogram, hektolitre ve alkol derecesi başına) Comext 2025'in birim değerleriyle ad valorem eşdeğerine çevrildi; asgari ve azami vergiler hesaba katıldı. İşlenmiş tarım ürünlerinde tarım bileşeni (EA) çevrilemediği için ad valorem kısım alt sınır olarak kullanıldı. S4'teki artış rejime göre belirlendi: GB satırına tam MFN, İTÜ satırına yalnızca sanayi bileşeni, tarım satırına (1/98 sürdükçe) sıfır.

**Enflasyon ve cari denge duyarlılığı.** Enflasyon duyarlılık endeksi (EDE), bir puanlık tarifenin TÜFE'ye birinci tur etkisini baz puan olarak veriyor. Doğrudan kanal, sınıfın COICOP 2018 sepetinden eşlenen TÜFE ağırlığı ile tüketimdeki ithal payının çarpımı. Dolaylı kanal, girdi-çıktı tablosundaki (2023) Leontief fiyat modelinden. 230 sınıfın EDE toplamı 22,0 baz puan ve girdi-çıktı tablosunun imalat ürünleri toplamıyla (23,5 baz puan) tutarlı. Cari denge kaldıraç endeksi (CKE), STA dışı ithalata bir puanlık tarifenin ya da iç satışlara %1'lik üretim desteğinin beş yıllık net cari denge getirisini, sırasıyla TÜFE maliyetine ve mali maliyete bölüyor; kapasite yatırımının ithalatı ve ithal girdi düşülüyor (V-36).

**Skorlar ve arketipler.** Kabiliyet skoru (KS) yedi bileşenden oluşuyor: dünya pazarında RCA (ağırlık 0,2), ürün karmaşıklığı (0,2), yurt içi katma değer (0,15), Ar-Ge yoğunluğu (0,15; OECD sınıflaması, VB-31), yurt içi tedarikçi bağlantıları (0,1), AB'ye göre verimlilik (0,1) ve firma çeşitliliği (0,1). Ağırlık seçimine duyarlılık sınandı: varsayılan sıralamanın Spearman korelasyonu eşit ağırlıklarla {{ksd:esit|spearman|2}}, ticaret ağırlıklı setle {{ksd:ticaret|spearman|2}}, yapı ağırlıklı setle {{ksd:yapi|spearman|2}}; rastgele ağırlık çekilişlerinin alt %10'unda {{ksd:dirichlet_p10|spearman|2}}. Sıralama ticaret ağırlıklarına karşı sağlam, yapısal ağırlıklara karşı orta derecede sağlam; her sınıfın sıra aralığı veri sayfasında veriliyor. Stratejik skor (SS) yedi boyutta elle ve gerekçeli puanlandı `[H]`; skor, en yüksek boyutun 0,7 ve ağırlıklı ortalamanın 0,3 ağırlıklı toplamı. AB maruziyet endeksi (AME), AB'ye ihracat payı ile beklenen tarife, menşe ve sınır maliyetinin toplamının değer zinciri çarpanıyla çarpımı. Arketip ve duruş önce kurallarla atandı (V-34), sonra her sınıf için gözden geçirilip gerekirse düzeltildi; düzeltmeler matrisin `uzman_duzeltmesi` sütununda.

## Ek C — Sınıf veri sayfaları

Her veri sayfası, çalışma çerçevesinin sınıf kartındaki sayısal alanları (kimlik, ölçek, dış ticaret, AB ve Türkiye tarafındaki maruziyet, kabiliyet, stratejik önem ve makro duyarlılık) bir arada veriyor. Senaryo tablosu Bölüm 5'te verilen sınıflar için sayfada ilgili tabloya atıf var; diğer sınıfların senaryo tablosu sayfanın hemen altında. Veriler `[V]`; eşleme, bölge payları, gizli hücre tahminleri ve skorlar `[T]`; menşe parametreleri ve stratejik skor `[H]`.

{{VERI_SAYFALARI|C}}

## Ek D — Önceki fazlara düzeltmeler

Faz 3'ün sınıf düzeyindeki hesapları, önceki fazlarda kullanılan verilerde iki hata ve bir yöntem farkı ortaya çıkardı.

**D-1. KN8 → NACE eşleme ağırlıkları.** `veri/cn2025_nace_rejim.csv` yazılırken birden çok sınıfa düşen 1.251 KN8 satırının eşleme ağırlığı tam sayıya yuvarlanmış ve sıfır görünüyordu. Bu satırlar Türkiye'nin AB'ye ihracatının %12,8'ini oluşturuyor. Faz 0–2'nin toplamları doğru, çünkü değerler eşit paylaştırılmış olarak zaten yazılıydı; ancak bazı sınıflarda sınıf dağılımı yanlış. Örneğin hibrit otomobil satırları (CPA 2.2 29.10.23) 29.10 ile 27.11 arasında eşit bölünmüştü. Faz 3 eşlemesiyle 29.32'nin AB'ye ihracatı €2,1 milyardan €5,6 milyara, 29.10'unki €16,6 milyardan €18,7 milyara çıkıyor; 27.11 (€3,3 milyardan €1,3 milyara) ve 28.25 (€2,9 milyardan €1,3 milyara) ise düşüyor. Faz 3'te CPA 2.2 kodunun CPA 2.1'de aynen sürdüğü bağlantıya öncelik veriliyor (V-37) ve eşleşmeyen ticaretin payı %6,0'dan %0,3'e iniyor. Faz 0–2'deki sınıf düzeyi tabloların bu sınıflardaki değerleri Faz 3 kartlarıyla geçersiz kalıyor; Faz 2'nin sınıf düzeyindeki sayılarının Faz 3 yöntemiyle yeniden hesaplanmış hâli ana matriste.

**D-2. Kıbrıs akımları.** BACI'deki Türkiye–Kıbrıs ticareti (2024'te 1,6 milyar dolarlık ihracat; %31'i akaryakıt) büyük ölçüde Kuzey Kıbrıs ile yapılan ticaret ve AB gümrük bölgesinin dışında. Faz 3'te bu akımlar AB dışı sayılıyor ve AB pazarı verilerinden düşülüyor. Etki, imalatın AB'ye ihracatının %1,4'ü; bazı küçük gıda sınıflarında (et ürünleri, patates ürünleri, dondurma) AB payı belirgin biçimde düşüyor ve süt ürünlerinde Kuzey Kıbrıs'tan gelen hellim ithalatı AB dışı sayılıyor. Faz 1–2'de AB tarafındaki maruziyet Comext'ten hesaplandığı için etkilenmiyor; yalnızca BACI'ye dayanan Türkiye ithalatı AB payları çok az yüksek kalmıştı.

**D-3. Kaybı %5'i aşan sınıf sayısı.** Faz 2'de anlaşmasız çıkışta istihdam kaybı %5'i aşan 21 sınıf raporlanmıştı. Bu sayı tek bir esneklik değeriyle (σ = 5) ve genel denge kalibrasyonu olmadan, kısmi dengeden geliyordu. Faz 3'te genel denge kalibrasyonu ve iç ikameyle bu sayı medyanda {{oz:S4|kayip_5yuzde_ustu_sinif_p50|0}}, dağılımın alt ucunda (P10) {{oz:S4|kayip_5yuzde_ustu_sinif_p10|0}} (`veri/f3_senaryo_ozet.csv`).

## Ek E — Varsayımlar ve veri boşlukları

Bu parçada varsayım kaydına on yeni madde eklendi ve yedi veri boşluğu açık kaldı. Varsayımların çoğu Faz 3'ün bütün parçaları için geçerli ve sonraki parçalarda yeniden kullanılacak.

{{TABLO:varsayim|E.1}}

{{TABLO:vb|E.2}}

{{ILERLEME}}
