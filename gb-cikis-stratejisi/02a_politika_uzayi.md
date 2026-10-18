# Faz 2A — Politika uzayı: tek taraflı araçlar, iç vergiler ve dış rejim seçenekleri

**Durum:** Faz 2 / 9, birinci kısım (2A), 18 Ekim 2026. İkinci kısım: [`02b_secenekler_hukuk.md`](02b_secenekler_hukuk.md). Önceki faz: [`01_teshis.md`](01_teshis.md). Defter: [`defter.md`](defter.md).

**Bu belge neden var?** Faz 1'e kullanıcının itirazı şuydu: yapılabileceklerin evreni keşfedilmedi. Örneğin GB'den çıkıp AB mallarına gümrük vergisi uygulamak ve yurt içinde üretilen mallarda ÖTV indirimi yapmak mümkün değil mi? İtiraz haklı. Faz 1, anlaşmasız çıkışı (S4) pasif bir senaryo olarak ele aldı: Türkiye AB mallarına MFN uygular, başka hiçbir şey yapmaz. Bu belge politika evrenini sistematik olarak tarıyor. Kapsam:
- kullanıcının önerisi: hukuki analiz, ekonomik eşdeğerlik, ürün grubu düzeyinde sayısallaştırma (§1);
- tarife, iç vergi, sübvansiyon, kamu alımı, ticaret savunması, gümrük rejimleri, teknik mevzuat, dış anlaşmalar ve makro araçlardan oluşan araç evreni (§2);
- Türkiye'nin kendi politika alanının sınırları: bağlı oranlar, yurt içi kabiliyet, koruma yapısı, gelir tabanı (§3);
- anlaşmasız çıkışın Türkiye'nin kendi araçlarıyla yeniden hesaplanması, yani "aktif S4" (§4);
- ihracat cephesinin sınırları (§5);
- dış rejim seçenekleri (§6) ve zaman kritik eylemler (§7).

**Kanıt etiketleri:**
- `[V]`: doğrulanmış veri.
- `[T]`: tahmin; yöntem ve P10–P50–P90 aralığı verilir.
- `[D?]`: doğrulanmalı.
- `[H]`: hipotez veya uzman yargısı.

Her çıkarımın yanında Güven: Yüksek / Orta / Düşük düzeyi verilir. Tutarlar aksi belirtilmedikçe ABD doları ve cari fiyatlarla; "mlr" milyar, "mn" milyon, "bp" baz puandır (0,01 puan).

**Bu kısmın veri ve kodu.** Bütün sayılar aşağıdaki betiklerle yeniden üretilir; çıktılar `veri/politika_*.csv` dosyalarındadır.

| Betik | İçerik | Ana kaynak |
|---|---|---|
| `kod/f2a_io_fiyat.py` | Leontief fiyat modeli: tarife şokunun TÜFE'ye birinci tur etkisi | TÜİK 2023 girdi-çıktı tabloları (64 ürün) |
| `kod/f2b_tarife_politikasi.py` | Tarife yapısı, BEC kullanım sınıfı, yurt içi kabiliyet ve "girdide sıfır" (P1) | BACI 2024, 2026 İthalat Rejimi Kararı, TÜİK PRODTR 2025, WITS BEC |
| `kod/prodtr.py` | TÜİK Yıllık Sanayi Ürün İstatistikleri (CPA 2.2, 6 hane) | TÜİK Veri Portalı, bülten 58065 |
| `kod/f2c0_takas_parametre.py`, `kod/f2c_vergi_takasi.py` | Tarife + ÖTV/KDV takası, ürün grubu düzeyinde; dört tasarım | BACI 2024, PRODTR 2024, YSHİ 2024, ODMD 2025, GİB ÖTV listeleri, 2026 TÜFE ağırlıkları |
| `kod/f2d_s4_net_istihdam.py` | S4'te NACE sınıfı düzeyinde net istihdam: ihracat kaybı − ithal ikamesi | Faz 0 tarife duvarı, PRODTR, YSHİ |
| `kod/f2e_s4_aktif.py` | Aktif S4 paketleri: İGV rejimi × P1 × vergi takası kapsamı | f2a, f2b; GİB 2025 gümrük vergisi tahsilatı |

Hukuk, emsal ve AB tarafı bulguları Faz 2'nin dört araştırma ajanının birincil kaynak taramasından alındı:
- DTÖ hukuku;
- Türkiye'nin ÖTV/KDV yapısı ve pazar verisi;
- emsaller ve fiyat geçişkenliği;
- AB hukuku ve çıkış mekaniği.

Kaynaklar sondadır; ham metinler ve çıkarılmış tablolar araştırma notlarında, `[V]` etiketli olanlar birincil metinden okunmuştur.

---

## Faz 2A'nın 12 ana bulgusu

1. **Gümrük birliğinden (GB) çıkınca AB mallarına gümrük vergisi konabilir; ÖTV indirimi ise yalnızca yerli ürüne yapılamaz.**
   - Tarife: MFN ilkesiyle ve bağlı oran içinde. Otomobilde Türkiye'nin cetvelindeki 18 satır %19 ve %20 ile bağlı; elektrikli otomobil %20. Diğer içten yanmalı motorlu otomobil satırlarında bağlama yok (DS629 panel raporu, 28.7.2026).
   - Yalnızca yerli ürüne ÖTV indirimi GATT md. III:2'nin "kendiliğinden" (per se) ihlalidir. III:8(b) bunu kurtarmaz; çünkü vergi indirimi "sübvansiyon ödemesi" sayılmaz (Brezilya–Vergilendirme, Temyiz Organı 2018, para. 5.92).
   - Türkiye çok taraflı geçici temyiz düzenlemesine (MPIA) taraf değil. AB, "boşluğa temyiz" edilen bir panel raporuna dayanarak kendi Uygulama Tüzüğüyle misilleme yapabilir.
   - `[V]` Güven: Yüksek.
2. **Aynı amaç hukuken temiz bir biçimle elde edilebiliyor: tarife ile menşeden bağımsız ÖTV/KDV indiriminin takası (T-A).**
   - AB malına MFN tarifesi konur; aynı ürün grubunda bütün menşelere eşit ÖTV/KDV indirimi yapılır.
   - Grubun fiyat endeksi sabit kalır; yerli ürün AB ürününe göre tarife kadar ucuzlar.
   - Otomobilde (merkez tahmin):
     - ÖTV %65'ten %56,2'ye iner;
     - AB otomobili %4,1 pahalanır, yerli %5,4 ucuzlar;
     - yerli satış +%23 (+$1,2 mlr); istihdam +2,3 bin;
     - net mali etki yılda −$0,15 mlr.
   - Takas yapılmazsa otomobil tek başına TÜFE'ye +26 bp ekler.
   - `[T]` Güven: Orta.
3. **Önerinin ilk biçimi (T-0) yalnızca hukuka aykırı değil, pahalı da.**
   - Otomobil pazarının ancak %22'si yerli. TÜFE'yi sabit tutmak için yerli otomobilde ÖTV'nin %65'ten %22,5'e inmesi gerekir. Bunun maliyeti yılda ≈$3,0 mlr; on grupta ≈$3,4 mlr. Takasta (T-A) maliyet ≈$0,46 mlr.
   - T-A'daki 8,8 puanlık indirim yalnızca yerliye uygulanırsa ucuz kalır, ama otomobilin TÜFE etkisinin ≈%80'i yerinde durur.
   - Yerli üreticiye doğrudan ödeme (T-B, III:8(b)) ekonomik olarak T-0 ile aynıdır. GATT md. III'e uygundur, ama Sübvansiyonlar ve Telafi Edici Önlemler Anlaşması (ASCM) kapsamında dava edilebilir.
   - `[T]` Güven: Orta.
4. **On ürün grubunda takasın bilançosu.**
   - Kapsam: otomobil, hafif ticari, beyaz eşya, küçük ev aletleri, TV, klima, kozmetik, giyim, ayakkabı, mobilya; TÜFE'nin %17,4'ü.
   - Pasif S4: +35 bp TÜFE, +$1,45 mlr mali, +11 bin istihdam.
   - Takas (T-A): −2 bp, −$0,46 mlr (P10–P90: −0,56 ile +0,10), +20 bin istihdam (12–22 bin).
   - `[T]` Güven: Orta.
5. **Anlaşmasız çıkışın enflasyon sorunu Türkiye'nin kendi araçlarıyla çözülebiliyor.**
   - Pasif S4'te birinci tur TÜFE etkisi 78 bp (P10–P90: 59–98). Bunu ilk yılda 30 bp altına indiren dört paket bulundu.
   - Önerilen paket (c2 + P1 + geniş takas):
     - İGV yalnızca yurt içi üretimi zayıf satırlarda kaldırılır;
     - üretilmeyen girdilerde tarife sıfırlanır;
     - imalat ürünlerinde menşeden bağımsız ÖTV/KDV takası yapılır.
   - Sonuç: TÜFE 3,3 bp (2,5–4,1). Tahsil edilebilir net mali etki GSYH'nin +%0,05'i. Çin ve diğer kaynaklara karşı mevcut koruma korunuyor.
   - `[T]` Güven: Orta.
6. **İstihdam ve kabiliyet kısıtları ise Türkiye'nin kontrolünde değil.**
   - S4'te imalatta net istihdam etkisi: −117 bin (P10–P90: −77 ile −165 bin).
   - Kaybın çekirdeği giyim: −72,6 bin, bölümün %10,9'u.
   - Kayıp AB pazarında oluşuyor. İç pazardaki hiçbir araç, AB'nin Türk ürünlerine uygulayacağı MFN'yi telafi etmiyor.
   - `[T]` Güven: Orta.
7. **İhracat tarafında yasal ve etkili bir tek taraflı araç yok.**
   - İhracat sübvansiyonu yasak.
   - AB vergisini üretim desteğiyle telafi etmek yılda ≈$38 mlr gerektirir (2028 GSYH'sinin %1,8'i); AB bunu telafi edici vergiyle geri alır.
   - Çıkışın ihracat cephesi bir anlaşmaya bağlı.
   - `[T]` Güven: Orta.
8. **Aktif S4, Türkiye'nin pazarlık gücünü artırıyor.**
   - AB'nin Türkiye'ye ihracatındaki kayıp (σ = 5, kısmi denge) rejime göre değişiyor:
     - yalnızca MFN uygulanırsa $16,4 mlr;
     - seçici rejimde (c) $18,7 mlr;
     - İGV kabiliyete duyarlı biçimde AB'ye de uygulanırsa (c2) $28,5 mlr.
   - Türkiye, AB'nin üçüncü büyük yeni araç ihracat pazarı: 2025'te €18,8 mlr.
   - Enflasyonu kendi araçlarıyla nötrleyebilen bir Türkiye için anlaşmasızlık daha az korkutucudur. Bu, anlaşmasız alternatifini (BATNA) güçlendirir.
   - `[T]`/`[H]` Güven: Orta.
9. **Çıkış hukuken AB'nin katılımını gerektiriyor.**
   - Ankara Anlaşması ve 1/95 sayılı Ortaklık Konseyi Kararı'nda fesih hükmü yok.
   - En temiz teknik iki adımlıdır:
     - Ortaklık Konseyi'nin bir "dondurma" (standstill) kararı. AB tarafında nitelikli çoğunlukla alınabilir (ABİDA md. 207(4) ve 218(9)).
     - AB'nin tek başına yetkili olduğu bir md. 207 anlaşması. Bu anlaşma GB hükümlerini "etkisiz kılar" (AB–Şili Geçici Ticaret Anlaşması md. 33.11 emsali).
   - Hasmane AB bu anlaşmayı önermeyebilir. Pazarlık, kozun kimde olduğuna bağlı.
   - `[V]`/`[H]` Güven: Orta.
10. **İki takvim için gerçekçilik.**
    - 1.1.2028 için gerçekçi olan yalnızca dondurma veya mevcut rejimin uzatılması.
    - 1.1.2029 için en fazla mal ağırlıklı bir serbest ticaret anlaşması (STA). Bunun için AB müzakere yetkisinin en geç 2027'nin üçüncü çeyreğinde verilmesi gerekir.
    - Derin ve kapsamlı STA (DCFTA) 2030 sonrası bir projedir.
    - `[H]` Güven: Orta.
11. **Zaman kritik bir DTÖ adımı var: GATT md. XXVIII:5 çekincesi.**
    - Bağlı oranları 2027–2029'da yeniden müzakere edebilmek için Türkiye bu çekinceyi **31.12.2026'dan önce** bildirmeli.
    - Bildirilmezse bu dönemde değişiklik ancak DTÖ'nün özel izniyle (XXVIII:4) yapılabilir. Olağan bir sonraki fırsat 1.1.2030.
    - Bedeli: diğer üyeler de aynı dönemde Türkiye ile ilk müzakere ettikleri tavizleri değiştirebilir.
    - DS629 panel raporu 27.10.2026'da DSB gündeminde.
    - `[V]` Güven: Yüksek.
12. **Türkiye'nin mevcut iç vergi düzenlemelerinde, çıkıştan önce temizlenmesi gereken DTÖ riskleri var.** Bunlar çıkıştan sonra AB'nin ilk hedefleri olur:
    - Engelli araç alımındaki ÖTV istisnasının %40 yerli katkı şartı.
    - İhracat kazancına kurumlar vergisi indirimi (md. 32/7). Bu, ihracata bağlı sübvansiyon sayılabilir.
    - Rakı ile diğer alkollü içkiler arasındaki maktu vergi farkı.
    - Elektrikli araç ÖTV dilimlerinin 160 kW eşiği ve bununla ilgili açık "yerli üretimi koruma" beyanları.
    - `[V]` Güven: Yüksek.

---

## 1. Öneri: "AB mallarına gümrük vergisi + yurt içinde üretilen mallarda ÖTV indirimi"

### 1.1 Kısa cevap

1. **Tarife kısmı mümkün.**
   - GB'den çıkınca Türkiye'nin AB'nin ortak gümrük tarifesine (OGT) bağlılığı biter. AB malları, STA'sı olmayan herkes gibi MFN oranını öder.
   - Oran bağlı oranı aşamaz.
   - AB'ye özel bir oran ancak bir STA veya GATT md. XXIV:5 kapsamında bir geçici anlaşmayla mümkündür.
2. **ÖTV kısmı önerildiği biçimde mümkün değil.**
   - Yalnızca yurt içinde üretilen mallara ÖTV indirimi, ithal benzer ürünü yerliden daha ağır vergilemek demektir. Bu GATT md. III:2 birinci cümlenin doğrudan ihlalidir:
     - en küçük fark bile ihlaldir (Japonya–Alkollü İçkiler II, 1996);
     - menşeye dayalı bir ayrım tek başına ihlal için yeter (Endonezya–Otomobil 1998, para. 14.113);
     - ticaret etkisi veya asgari eşik savunması yoktur (Arjantin–Deri, 2001).
   - AB böyle bir uygulamayı dava eder ve kazanır.
3. **Önerinin amacı ise hukuken temiz biçimde elde edilebilir.** Kullanıcının iki amacı var:
   - AB ürününe karşı yerli üreticiyi korumak;
   - tarifenin enflasyonist etkisini nötrlemek.

   Bu iki amaç, tarife + aynı ürün grubunda **bütün menşelere eşit** ÖTV/KDV indirimi takasıyla (T-A) birlikte sağlanır:
   - yerli ürün AB ürününe göre tarife kadar ucuzlar;
   - grubun ortalama fiyatı değişmez;
   - mali maliyet küçüktür, çünkü tarife geliri indirimi büyük ölçüde finanse eder.
4. **Takas bir enflasyon kalkanıdır; ihracat çözümü değildir.** Yerli üreticiye iç pazarda avantaj verir. AB'nin Türk mallarına uygulayacağı MFN'yi ise değiştirmez. Otomotiv ihracatının %79'u AB'ye gidiyor (Faz 1).

### 1.2 Hukuki çerçeve

| Kural | Özü | Öneriye uygulanışı |
|---|---|---|
| GATT III:2, birinci cümle | İthal ürün, benzer yerli üründen "daha fazla" iç vergiye tabi tutulamaz. Asgari eşik yok: "en küçük fazlalık bile fazladır" (Japonya–Alkollü İçkiler II, s. 23) | Yalnızca yerli araca ÖTV indirimi: **kendiliğinden ihlal** |
| GATT III:2, ikinci cümle ve Ek Not | Doğrudan rakip veya ikame ürünler "korumaya yol açacak şekilde" farklı vergilenemez. Ölçütler: tasarım, mimari ve "açığa vuran yapı" (revealing structure). Yalnızca nesnel olarak görünür amaç sayılır (Şili–Alkollü İçkiler, para. 71–72). Korumacı beyanlar delil olabilir (Meksika–Meşrubat, panel para. 8.91) | Görünüşte menşeden bağımsız ama yerli modelin özelliğine göre kesilmiş dilimler (ör. 160 kW eşiği): **fiilî ayrımcılık riski** |
| GATT III:4 | Satışı etkileyen düzenlemelerde ithal ürüne daha az elverişli muamele yasak; biçimsel eşitlik yetmez (Dominik Cumhuriyeti–Sigara) | İndirim yerli katkı, yerli tesiste üretim veya akreditasyon şartına bağlanırsa ihlal (Brezilya–Vergilendirme; Türkiye–Pirinç DS334) |
| GATT III:8(b) | Md. III, yalnızca yerli üreticilere sübvansiyon **ödenmesini** engellemez; iç vergi gelirinden finanse edilen ödemeler dahil | Kapsamı yalnızca kamu harcamasıdır; vergi muafiyeti veya indirimi kapsam dışı (Kanada–Süreli Yayınlar 1997, s. 33–34; Brezilya–Vergilendirme, para. 5.84, 5.92). Uygunluk ölçütü üretim faaliyeti olabilir, yerli girdi kullanımı olamaz (para. 5.93–5.95) |
| ASCM md. 1–3, 5–6, Kısım V | Vazgeçilen vergi geliri bir mali katkıdır. İhracata bağlı (3.1(a)) ve yerli girdiye bağlı (3.1(b)) sübvansiyonlar yasak. Sektöre özgü sübvansiyon dava edilebilir; sübvansiyonlu ülke pazarında ithalatın yerinden edilmesi ciddi zarardır (6.3(a)). İhracat pazarında telafi edici vergiye açık | III:8(b) ödemesi ASCM'den kaçamaz. AB hem Türkiye pazarındaki kaybı için dava açabilir (Endonezya–Otomobil'de ciddi zarar bulundu) hem de AB'ye giden Türk ürünlerine telafi edici vergi koyabilir |
| TRIMs md. 2 ve örnek liste | Yerli ürün satın alma veya kullanma (1(a)) ve ticaret dengeleme (1(b), 2(a)) şartları yasak; bir "avantaj" elde etmek için gerekiyorsa kapsam içinde (Endonezya–Otomobil, para. 14.88–14.91) | Takas ve III:8(b) desteği **koşulsuz** olmalı: yatırım, istihdam, Ar-Ge veya Türkiye'de üretim şartı olabilir; girdinin menşesi şartı olamaz |
| GATT I ve II:1 | MFN ve bağlı oran | AB'ye özel tarife STA olmadan mümkün değil. Bağlı oran aşılamaz (DS629: elektrikli araçlardaki ek vergiler II:1(b)'yi ihlal etti) |
| DTÖ uyuşmazlık çözümü (2026) | Temyiz Organı işlemiyor; 25.9.2026'da atama önerisi 100. kez engellendi. Türkiye MPIA'ya taraf değil | AB, Uygulama Tüzüğü 654/2014 md. 3(aa) ile, temyizi tamamlanamayan bir panel raporu sonrasında karşı önlem alabilir. Şikâyetten karşı önleme ≈2,5–3,5 yıl `[H]` |

*Kaynak ve etiketler:*
- `[V]` Antlaşma metinleri; DTÖ Analitik Endeksi (GATT md. III, ASCM md. 1–3, TRIMs md. 2).
- DTÖ uyuşmazlık sayfaları: DS8/10/11, DS31, DS54/55/59/64, DS87/110, DS155, DS302, DS308, DS334, DS472/497, DS583, DS629.
- DSB toplantısı, 25.9.2026; AB Tüzüğü 654/2014, 2021/167 ile değişik.
- Güven: Yüksek.

### 1.3 Emsaller: dünyada kim ne yaptı, ne oldu?

| Ülke ve önlem | Tasarım | Hukuki sonuç | Ölçülen etki | Ders |
|---|---|---|---|---|
| **Endonezya**, "Millî Otomobil" (1996) | Yerli içeriğe bağlı lüks satış vergisi ve gümrük muafiyeti | DS54/55/59/64 (1998): III:2, I, TRIMs 2.1 ihlali; ASCM'de ciddi zarar. 1999'da yeni politika | — | Menşeye bağlı vergi ayrıcalığı ders kitabı ihlalidir |
| Endonezya, düşük maliyetli yeşil otomobil (LCGC) programı (2013–) ve 2021 indirimi | Motor hacmi, yakıt verimliliği ve fiyat ölçütü; yerli alım oranı %60–70 şartı | Dava yok `[D?]` | LCGC 2016'dan beri pazarın >%20'si. 2021 indirimi: maliyet Rp4,6 trilyon, satış +%67 (COVID tabanından) | Kısa süreli kriz önlemleri dava edilmedi, ama risk taşır |
| **Brezilya**, Inovar-Auto (2012–17) | Akredite yerli üreticiye 30 puanlık IPI (sanayi ürünleri vergisi) indirimi; ithalatçıya yılda 4.800 adetlik kota | DS472/497 (2019): III:2, III:4, I:1 ve TRIMs ihlali; III:8(b) savunması reddedildi | İthalatçıların satışı 199 binden (2011) ≈35 bine (2016) düştü. Brezilya'nın dünya üretimindeki payı kalıcı artmadı | Vergi indirimi "sübvansiyon ödemesi" sayılmaz |
| Brezilya, Rota 2030 (2018) ve MOVER (2024) | Aynı şartlar ve aynı IPI indirimleri "Brezilya'da üretilen veya ithal edilen" araçlara; MOVER'de itici güce, verimliliğe ve geri dönüştürülebilirliğe dayalı "yeşil IPI" | Rota 2030 DTÖ'ye uygun şablon. MOVER'in tam IPI muafiyeti Brezilya'da üretim şartı taşıyor: risk | MOVER Ar-Ge kredileri ≈R$19 mlr | Menşeden bağımsız, teknolojiye dayalı vergi tasarımı mümkün |
| **Rusya**, geri dönüşüm harcı (2012–) | DTÖ üyeliğiyle tarife inerken ithal araçlara harç. Yerli üretici önce muaf; 2014'ten sonra yerli üretici de ödüyor ama federal sübvansiyonlarla telafi ediliyor | AB (DS462) ve Japonya (DS463): panel kuruldu ama hiç oluşturulmadı. USTR'ye göre fiilî ayrımcılık iddiası sürüyor | İthalat payı 2009'da %48'den 2019'da %15'e indi (rubledeki çöküş de etkili). Harç 2024–2025'te %10–20 fiyat payına çıktı. Yerel montaj 2026'da satışların %64'ü, ama yerli içerik sığ. 2026 bütçesinde gelir ≈RUB1,65 trilyon | "Tek tip harç + yerli üreticiye telafi" pratikte tarife gibi çalışır ve gelir getirir. Bedeli yüksek tüketici fiyatı ve gümrük birliği ortakları üzerinden sızıntı (Avrasya Ekonomik Birliği) |
| **Hindistan**, üretime bağlı teşvik (PLI, 2020–) | Artan satışın %13–18'i oranında ödeme (otomotiv); en az %50 yurt içi katma değer şartı | Çin'in açtığı DS642: panel 28.5.2026'da oluştu; sonuç bekleniyor | Haziran 2026'ya kadar ödeme ₹36.754 crore (bütçenin beşte birinden az). Telefon üretimi FY25'te +%146; ithalat −%77 | Üretime bağlı ödeme yaygın. Risk yurt içi katma değer şartında ve eşlik eden tarife artışlarında |
| **Çin**, yeni enerjili araç alım vergisi muafiyeti (2014–2027) | %10 alım vergisinden muafiyet; kataloğa giren ithal modeller de yararlanıyor; 2026–27'de yarıya iniyor ve önceden ilan edildi | Menşeden bağımsız; dava yok | 2024–27 vergi harcaması ≈¥520 mlr | **Teknolojiye dayalı, menşeden bağımsız vergi indirimi hukuken sağlam.** Kademeli ve önceden ilan edilmiş çıkış |
| **Tayland**, elektrikli araç programları EV 3.0/3.5 (2022–27) | Alım sübvansiyonu ve ÖTV indirimi; ithalat vergisi indirimi karşılığında yerli üretim taahhüdü (1:1, sonra 1:2 ve 1:3); ithal batarya hücresi tavanı | Dava yok. Hücre tavanı ve ticaret dengeleme benzeri taahhüt III:4 ve TRIMs riski | 2025'e kadar 238 bin elektrikli araç; 43 üreticiden THB140 mlr yatırım; arz fazlası ve fiyat savaşı nedeniyle 2025'te şartlar gevşetildi | "Şimdi ithal et, sonra üret" hızlı yatırım çekti, ama tekrar tekrar gevşetme gerektirdi |
| **Arjantin**, Tierra del Fuego (2009–) | İthal elektroniğe yerli üretime göre çok daha yüksek iç vergi; bölge üretimi KDV'den muaf | Dava yok; menşeye dayalı iç vergi açık III:2 sorunu. Arjantin ticaret dengeleme şartlarından DS438'i kaybetti | Telefon pazarının >%90'ı bölgeden; maliyet yılda ≈$1,07 mlr | Menşeye göre değişen ÖTV gizli bir tarifedir; mali maliyeti yüksek ve kalıcı bir lobi yaratır |
| **ABD**, IRA temiz araç kredisi (30D, 2022–2025) | Kuzey Amerika'da son montaj ve kritik mineral oranı şartlı $7.500 kredi | AB, Japonya ve Kore itiraz etti; Çin'in açtığı DS623'te kredi iddiaları, 30D kaldırıldıktan sonra (30.9.2025) düştü | — | Üretim yerine bağlı tüketici kredisi müttefikleri kızdırdı; önce sulandırıldı, sonra kaldırıldı |
| **Türkiye**, ilaç yerelleştirmesi (2016–2024) | SGK geri ödemesinin yerelleştirmeye bağlanması | DS583 (DSU md. 25 tahkim kararı, 2022): III:4 ihlali; III:8(a) ve XX savunmaları reddedildi | — | Türkiye'nin kendi dersi (temel ilke 8) |
| **Türkiye**, geçmiş ÖTV indirimleri (2009, 2017, 2018–19) | Otomobil, beyaz eşya ve mobilyada geçici indirimler | Hiçbirinde menşe şartı yok (CK 287 metni) | Kasım 2018: aylık TÜFE −%1,44; otomobil fiyatı −%13,6, mobilya −%8,5, beyaz eşya −%5,2. Geçişkenlik mobilyada ≈%100, beyaz eşyada ≈%83 | Menşeden bağımsız indirim Türkiye'de defalarca uygulandı; bu, takasın kurumsal altyapısıdır |

*Kaynak ve etiketler:*
- `[V]` DTÖ uyuşmazlık sayfaları: DS54, DS462/463, DS472/497, DS438, DS583, DS623, DS642.
- USTR 2022 ve 2025 Rusya raporları; TCMB Kasım 2018 fiyat gelişmeleri raporu; CK 287 (RG 31.10.2018 mük.).
- `[D?]` Rusya, Endonezya, Tayland, Arjantin ve Hindistan'ın ölçülen etkilerinde basın ve ikincil kaynaklar kullanıldı.
- Güven: Orta.

### 1.4 Ekonomik eşdeğerlik ve tasarım seçenekleri

Bir ithalat tarifesi ekonomik olarak iki aracın toplamıdır: yerli üreticiye **üretim sübvansiyonu** ve tüketiciye **tüketim vergisi** (Bhagwati–Ramaswami 1963).
- Tarife ile aynı ürün grubundaki menşeden bağımsız ÖTV indirimi birlikte uygulanırsa tüketim vergisi kısmı nötrlenir.
- Geriye tarife geliriyle finanse edilen bir üretim sübvansiyonu kalır. Yerli üretici AB ürününe göre tarife kadar fiyat avantajı kazanır; tüketici ortalamada aynı fiyatı öder.
- Hedefleme ilkesine göre amaç yerli üretimse en verimli araç doğrudan üretim sübvansiyonudur. Ancak bu araç bütçeden finanse edilir ve ASCM'ye tabidir. Takas, tarife gelirini kullandığı için mali olarak neredeyse kendi kendini finanse eder.

| Tasarım | Yerli ürünün AB ürününe göre fiyat avantajı | STA ortağının (Kore, İngiltere, Fas) ürününe göre | Grubun TÜFE'si | Mali | DTÖ riski | AB'nin misilleme riski |
|---|---|---|---|---|---|---|
| **T-0** Tarife + yalnızca yerli ürüne ÖTV indirimi (önerinin ilk biçimi) | Tarife + ÖTV farkı (otomobilde %48) | ÖTV farkı | Sabitlenirse çok pahalı; ucuz tutulursa artar | Yüksek negatif (TÜFE sabitlenirse) | **Yüksek**: III:2 kendiliğinden ihlal; şarta bağlanırsa III:4, TRIMs ve ASCM 3.1(b) | Yüksek (md. 3(aa); MPIA yok) |
| **T-A** Tarife + menşeden bağımsız ÖTV/KDV indirimi (takas) | Tarife kadar (otomobilde %10) | Yok | Sabit (tasarım gereği) | ≈ Nötr | **Düşük** | Düşük–orta (bağlı oran aşılırsa XXVIII dengelemesi) |
| **T-B** Tek tip ÖTV + yerli üreticiye III:8(b) birim ödemesi | Ödeme kadar | Ödeme kadar | Sabitlenebilir | Yüksek negatif (bütçeden) | Düşük (GATT); orta (ASCM: ciddi zarar davası) | Düşük–orta; telafi edici vergi riski orta–yüksek |
| **T-C** ÖTV'nin nesnel ölçütlerle yeniden yapılandırılması (CO₂, verimlilik, boyut) | Ölçütün yerli modelle örtüşmesine bağlı | Aynı | ± | ± | Düşük–orta; eşikler yerli modele göre kesilirse orta | Düşük |
| **T-D** Kamu alımında yerli malı fiyat avantajı | %15'e kadar (yalnızca gerçek kamu alımında) | Aynı | Etkisiz | Hafif negatif | Düşük (Türkiye Hükûmet Alımları Anlaşması'na taraf değil, gözlemci) | Orta (AB'nin Uluslararası Kamu Alımı Aracı) |
| **T-E** Ticaret savunması (anti-damping, telafi edici vergi) | Dampingli/sübvansiyonlu ithalata karşı | — | Hafif + | + | Düşük (kanıta dayalıysa) | Düşük–orta |
| **T-F** Korunma önlemi | Herkese karşı | Herkese karşı | + | + | Orta–yüksek (çıkışta AB ithalatı artmaz, azalır; "ithalat artışı" koşulu sağlanamaz) | Orta–yüksek (md. 8.2 karşı önlem) |

*Kaynak ve etiketler:* `[V]` hukuki değerlendirme DTÖ araştırma notunun sıralı tasarım tablosuna dayanıyor. `[T]` sayılar §1.5'ten. Güven: Orta–Yüksek.

**T-0 ile T-A arasındaki fark, sanıldığı gibi yalnızca hukuki değil.**
- T-0'da yerli ürüne yapılan ÖTV indirimi küçük bir tabana uygulanır: otomobil pazarının %22'si.
- Pazarın geri kalanında, yani AB ve diğer ithal ürünlerde fiyat tarife kadar artar.
- Bu nedenle T-0 grubun fiyatını ya sabitleyemez ya da sabitlemek için yerli üründe çok derin bir indirim gerektirir. Derin indirim yerliye %48'lik bir fiyat avantajı verir; bu, hukuka aykırılığın büyüklüğünün de ölçüsüdür.
- T-A ise indirimi bütün pazara yayar. Gereken indirim küçüktür ve tarife geliri onu finanse eder.

### 1.5 Ürün grubu düzeyinde sonuçlar

**Model** (`kod/f2c_vergi_takasi.py`):
- On ürün grubu; kaynaklar yerli, AB, STA ortakları ve diğerleri.
- Armington CES talep sistemi:
  - ikame esnekliği σ ∈ {2, 4, 6};
  - grup talebinin fiyat esnekliği η ∈ {0,5; 1; 1,5};
  - tarifenin fiyata geçişkenliği ρ ∈ {0,8; 1}.
- S4 tarife rejimi "c": AB'nin baskın olduğu satırlarda İGV herkes için kalkar (§4.1).
- Takas kuralı: grubun **ölçülen** fiyat endeksi (Laspeyres; TÜFE ağırlıkları yıl içinde sabit) değişmez. Refah açısından tam fiyat endeksi (CES) ayrıca raporlandı.
- Merkez tahmin σ = 4, η = 1, ρ = 1. Aralık, 18 parametre bileşiminin P10–P90'ı.

**Veri:**
- İthalat ve ihracat: BACI 2024.
- Yerli iç satış: PRODTR 2024 (az sayıda üreticili gruplarda), YSHİ 2024 (parçalı sektörlerde), 2023 girdi-çıktı tablosu (giyimde) ve ODMD 2025 (otomobil ve hafif ticari).
- ÖTV ve KDV: GİB listeleri, 2026.
- TÜFE ağırlıkları: 2026, COICOP 2018.

**Tablo 1.5a — Takas (T-A) ve pasif S4, ürün grubu başına (merkez)**

| Grup | TÜFE ağırlığı (%) | Yerli pay | ÖTV/KDV: bugün → takasla | Pasif S4: grup fiyatı | Pasif S4: TÜFE katkısı (bp) | Takasla AB ürünü / yerli ürün fiyatı | Takasla yerli satış ($ mn) | Takasla istihdam | Takasla net mali ($ mn) |
|---|---|---|---|---|---|---|---|---|---|
| Binek otomobil | 4,59 | %22 | ÖTV %65 → %56,2 | +%5,7 | 26,0 | +%4,1 / −%5,4 | +1.189 | +2.300 | −153 |
| Hafif ticari | 0 | %22 | ÖTV %6 → %0 (yetmiyor; kalan +%1,5) | +%7,6 | 0 | +%7,1 / −%5,7 | +161 | +312 | +7 |
| Beyaz eşya | 1,06 | %86 | ÖTV %6,7 → %6,6 | +%0,1 | 0,1 | +%3,1 / −%0,1 | +4 | +18 | +2 |
| Küçük ev aletleri | 0,19 | %33 | ÖTV %6,7 → %5,6 | +%1,1 | 0,2 | +%11,5 / −%1,1 | +16 | +81 | +10 |
| TV | 0,26 | %74 | ÖTV %6,7 → %6,0 | +%0,7 | 0,2 | +%13,2 / −%0,7 | +15 | +80 | −2 |
| Klima | 0,16 | %77 | ÖTV değişmez | +%0,0 | 0,0 | +%2,0 / 0 | +2 | +17 | 0 |
| Kozmetik | 0,92 | %39 | Değişmez (fiyat düşüyor) | −%1,4 | −1,2 | +%0,4 / 0 | −49 | −419 | −26 |
| Giyim | 6,51 | %87 | KDV %10 → %8,9 | +%1,0 | 6,5 | +%42,0 / −%1,0 | +797 | +17.102 | −241 |
| Ayakkabı | 1,11 | %45 | KDV %10 → %6,3 | +%3,5 | 3,9 | +%37,8 / −%3,4 | +177 | +2.958 | −44 |
| Mobilya | 2,62 | %91 | Değişmez (fiyat düşüyor) | −%0,3 | −0,8 | +%2,9 / 0 | −117 | −2.384 | −15 |
| **Toplam** | **17,41** | | | | **34,7 (27,6–34,7)** | | **+2.195 (1.112–2.694)** | **+20.066 (12.417–21.841)** | **−462 (−555 ile +99)** |

*Kaynak ve etiketler:*
- `[T]` `veri/politika_takas_ozet.csv`, `veri/politika_takas_parametre.csv`.
- Yerli payın kaynağı: otomobil ve hafif ticaride ODMD 2025 adet payı × OSD ihracat birim değeri; beyaz eşya, küçük ev aletleri, TV, klima ve kozmetikte PRODTR 2024; ayakkabı ve mobilyada YSHİ 2024; giyimde 2023 girdi-çıktı tablosundaki hanehalkı yurt içi payı.
- Üç yöntem arasındaki fark parametre dosyasında raporlandı. Otomobilde I-O payı %39, YSHİ payı %54; ikisi de hafif ticari ve parça üretimini karıştırıyor.
- Güven: Orta.

**Okuma.**
- Kozmetik ve mobilyada fiyat düşüyor. Bunun nedeni rejim "c": AB'nin baskın olduğu satırlarda İGV herkes için kalkıyor. Bu iki grupta yerli üretici kaybediyor: mobilyada −2,4 bin istihdam.
- Rejim "c"nin bu yan etkisini, İGV'yi yalnızca kabiliyeti zayıf satırlarda kaldıran rejim "c2" önlüyor (§4.1).
- Giyim ve ayakkabıda AB ürününün fiyatı %38–42 artıyor. Bu satırlarda AB tedarikçi olarak baskın değil, bu yüzden İGV AB'ye de uygulanıyor. Ama iç pazardaki payı küçük (%2–8); TÜFE etkisini KDV indirimi küçük bir maliyetle siliyor.

**Tablo 1.5b — Otomobilde dört tasarım (merkez; aralık P10–P90)**

| | Pasif S4 | T-A takas | T-0 yalnızca yerliye indirim | T-B III:8(b) ödemesi |
|---|---|---|---|---|
| ÖTV (ithal / yerli) | %65 / %65 | %56,2 / %56,2 | %65 / **%22,5** | %65 / %65 |
| Yerli üreticiye birim ödeme | — | — | — | Üretici fiyatının %25,8'i |
| AB otomobilinin fiyatı | +%10,0 | +%4,1 | +%10,0 | +%10,0 |
| Yerli otomobilin fiyatı | 0 | −%5,4 | −%25,8 | −%25,8 |
| Yerlinin AB'ye göre fiyat avantajı | %10 | %10 | **%48** | **%48** |
| Yerli satış hacmi | +%16 | +%23 (+9 ile +34) | +%180 (+57 ile +276) | +%180 |
| Otomobilin TÜFE katkısı | +26,0 bp | 0 | 0 | 0 |
| Net mali etki ($ mn/yıl) | +1.102 | **−153** (−212 ile +193) | **−2.992** (−4.194 ile −664) | **−2.992** |
| İstihdam | +1.641 | +2.300 | +17.977 | +17.977 |
| DTÖ | Uyumlu | Uyumlu | **Aykırı** | Uyumlu (GATT); ASCM'de dava edilebilir |

*Kaynak:* `[T]` aynı model. T-0 ve T-B'de yerli satıştaki +%180 bir kapasite sınırına çarpar: yerli üretimin iç satışı 323 bin adetten ≈900 bin adede çıkmak zorunda kalır. Bu, ihracattan iç pazara kaydırma olmadan mümkün değildir. Sayı bir üst sınır olarak okunmalı. Güven: Orta.

**Otomobilde bir ara yol: T-0'da indirim T-A ile aynı tutulursa.** ÖTV yalnızca yerli otomobilde 8,8 puan indirilir.
- Yerli fiyat −%5,4, AB fiyatı +%10 olur.
- Grup fiyatı +%4,5 artar; TÜFE katkısı ≈+20,5 bp, yani pasif S4'ün ≈%80'i.
- Mali maliyet küçük kalır (≈+$0,7 mlr net), ama hukuka aykırılık aynıdır.
- Kısacası T-0 ya pahalıdır ya da enflasyonu durdurmaz. `[T]`

**Tablo 1.5c — On grubun toplamı, dört tasarım (merkez; aralık P10–P90)**

| | Pasif S4 | T-A takas | T-0 | T-B |
|---|---|---|---|---|
| TÜFE katkısı (bp) | +34,7 (27,6–34,7) | −2,1 | −2,1 | −2,1 |
| Gümrük geliri ($ mn) | +1.446 | +1.576 | +937 | +871 |
| ÖTV + KDV ($ mn) | 0 | −2.039 | −4.383 | 0 |
| Yerli üreticiye ödeme ($ mn) | — | — | — | −5.089 |
| **Net mali ($ mn)** | **+1.446** (874–2.154) | **−462** (−555 ile +99) | **−3.447** (−4.781 ile −739) | **−4.217** (−5.870 ile −1.019) |
| Yerli satış ($ mn) | +1.398 | +2.195 | +11.036 | +12.405 |
| İstihdam | +11.000 | +20.066 (12.417–21.841) | +46.662 | +49.309 |

*Kaynak:* `[T]` `veri/politika_takas_ozet.csv`. Güven: Orta.

**Okuma.**
1. TÜFE'yi sabitleyen üç tasarımdan en ucuzu takas (T-A). Maliyeti T-0'ın yedide biri, T-B'nin dokuzda biri.
2. T-0 ve T-B istihdamı daha çok artırıyor (+47–49 bin), çünkü yerliye çok daha büyük bir fiyat avantajı veriyorlar.
   - Bu avantaj iç pazarda AB ürününün yerinden edilmesidir. ASCM md. 6.3(a)'nın tanımladığı "ciddi zarar" tam olarak budur.
   - T-0 zaten III:2 ihlali. T-B, GATT'a uygun olsa da ASCM davasına ve telafi edici vergiye açık.
   - Ayrıca ek istihdamın büyük kısmı otomobilde kapasite sınırına takılır.
3. Takasın getirdiği +20 bin istihdam, S4'ün net istihdam kaybını (−117 bin) kapatmaya yetmez (§4.2). Ama takas, enflasyon kısıtını istihdam kısıtıyla takas etmeden çözer.

### 1.6 Fiyat geçişkenliği: model varsayımları kanıtla uyumlu mu?

| Kanal | Kanıt | Modelde |
|---|---|---|
| Tarife → sınır fiyatı (vergi dahil) | ABD 2018–19: ≈%95–100 geçişkenlik (Amiti–Redding–Weinstein 2019; Fajgelbaum vd. 2020; Cavallo vd. 2021). Türkiye 2020 İGV'leri: sınır fiyatı düşmedi, yükü Türk alıcı taşıdı; her puan ithalatı %1,24 azalttı (TCMB WP 21/13) | ρ ∈ {0,8; 1} |
| Tarife → perakende fiyat | ABD'de daha yavaş ve düşük: %20 tarife iki büyük perakendecide göreli fiyatı yalnızca %0,7 artırdı, çünkü marjlar daraldı. Çamaşır makinesi istisnaydı. Türkiye'de enflasyon beklentisi yüksekken geçişkenlik daha yüksek (TCMB 2023) | ρ = 0,6 (P10) |
| ÖTV/KDV indirimi → perakende fiyat | Kasım 2018: TCMB'ye göre "büyük ölçüde" yansıdı. Mobilyada ≈%100, beyaz eşyada ≈%83; otomobilde mekanik etkiden fazla (−%13,6). 2017'de kur değer kaybederken "görece sınırlı" | Tam geçişkenlik |
| Tarife kaldırma → fiyat | İsviçre, 1.1.2024'te bütün sanayi tarifelerini tek taraflı kaldırdı: sanayi tüketim mallarında fiyat 12 ayda −%1,15, giyimde −%1,95. Sınır fiyatları yükselmedi (SECO 2026) | P1 ve rejim "b" yönünde |
| Kur geçişkenliği | Türkiye'de bir yıllık: potansiyel çıktıda ≈%15, genişlemede ≈%25 (TCMB). 2018'den beri arttı, 2020'den beri hızlandı | Faz 6 |
| Geçici indirimlerin bitişi | Temmuz 2019'da indirim bitişi enflasyonu artırdı (TCMB Enflasyon Raporu 2019-III); Rusya'da ilan edilen artışlar öncesi alım dalgası | Takas **kalıcı** veya önceden ilan edilmiş kademeli bir patikayla tasarlanmalı |

*Kaynak ve etiketler:* `[V]` emsal araştırma notu S50, S54–S57, S60, S62, S64–S66, S69–S70. Güven: Orta–Yüksek.

**Sonuç.** Modelin merkez varsayımı (ρ = 1) Türkiye için temkinlidir; TÜFE etkisi bu varsayımla bir üst sınır olarak okunmalı. Vergi indiriminin fiyata tam yansıması varsayımı ise 2018 deneyimiyle uyumlu. Ancak kur değer kaybederken yansıma zayıflar. Takas, dezenflasyon programıyla eş zamanlı ve kur istikrarı içinde uygulanmalı.

### 1.7 Takasın sınırları ve tasarım kuralları

1. **Ticaret sapması.**
   - STA ortaklarının ürünleri de ÖTV indiriminden yararlanır; tarife ödemedikleri için fiyatları düşer.
   - Otomobilde AB'nin kaybettiği payı yerli üretici kadar Kore, İngiltere ve Fas da alır: STA hacmi +%23.
   - Fas'tan gelen Dacia için belirleyici, Fas–Türkiye STA'sının menşe kuralıdır. AB girdisi çapraz kümülasyonla ancak AB–Türkiye arasında bir menşe düzenlemesi varsa sayılır. S4'te bu düzenleme yok.
2. **Bağlı oran tavanı.**
   - Otomobilde bağlı satırlarda en fazla %19–20, elektrikli otomobilde %20.
   - Bilgi Teknolojisi Anlaşması (ITA) ürünlerinde (bilgisayar, telefon) sıfır.
   - Bağsız satırlarda hukuki alan geniş, ama itibar ve STA müzakeresi maliyeti var (§3.1).
3. **ÖTV dilimlerinde sıçrama tuzağı.**
   - İthalatta ÖTV matrahı KDV matrahıdır (4760 sayılı Kanun md. 11/3). Gümrük vergisi muhtemelen bu matrahın içinde `[D?]`.
   - Dilimli otomobil ÖTV'sinde (%70 / 75 / 80 / 90) %10'luk tarife, eşiğe yakın bir AB otomobilini üst dilime iter. Bu durumda fiyat %10 değil, %15–17 artar.
   - Çözüm: dilim eşiklerini gümrük vergisi hariç bir tabana veya teknik ölçütlere bağlamak; ya da eşikleri çıkış günü tarifenin ortalama matrah etkisi kadar (≈%7) yükseltmek.
4. **Fiilî ayrımcılık riski (T-C).**
   - İndirim bütün dilimlerde aynı oranda yapılmalı.
   - 2022'de elektrikli otomobil dilimlerinin 160 kW'a göre yeniden kesildiği belgelendi. Togg T10X'in arkadan itişli sürümü 160 kW. TBMM'de "yerli üretimi korumak" amacı açıkça söylendi (AK Parti Grup Başkanvekili, Temmuz 2022).
   - Şili–Alkol ve Meksika–Meşrubat içtihadına göre bu bir risk işaretidir.
   - Hafifletici unsur: Tesla, BMW ve VW yazılımla 160 kW'a sınırlanmış sürümler çıkardı. 2025'te 160 kW altı elektrikli otomobiller pazarın %13,9'uydu.
   - Takas yeni bir eşik yaratmamalı, mevcut eşikleri genişletmemeli.
5. **Mali taban aşınması.**
   - Tüketici AB ürününden yerli ve STA ürününe kaydıkça gümrük geliri azalır. Düşük ÖTV ise bütün satışlara uygulanır.
   - Bu yüzden takasın net maliyeti zamanla artar. σ yükseldikçe maliyet de artıyor: P10–P90 aralığının alt ucu.
   - Ayrıca gümrük vergisinin bir kısmı Dahilde İşleme Rejimi (DİR) ve teşvik muafiyetleriyle zaten tahsil edilmiyor (§3.4). Tüketim mallarında bu sorun yok; otomobil ithalatı tam vergilenir.
6. **Geçici değil kalıcı.**
   - Geçici indirimlerin sonu fiyat uçurumu yaratır (2019). İndirim ilan edilirse alımlar öne çekilir.
   - Takas, GB'den çıkış günü yürürlüğe giren **kalıcı** bir oran değişikliği olmalı.
   - Varsa sonraki değişiklikler önceden ilan edilmiş bir patikayla yapılmalı. Çin'in yeni enerjili araç muafiyeti bunu iyi yaptı: 2026–27'de yarıya inme önceden açıklandı.
7. **AB'nin tepkisi.**
   - MFN tarifesi bağlı oran içindeyse DTÖ'ye uygundur; AB'nin DTÖ temelli misilleme hakkı doğmaz.
   - AB'nin elindeki diğer araçlar §4.4'te: ticaret savunması, çelik tüzüğü, SKDM, onaylanmış kuruluşlar, menşe kuralları ve siyasi araçlar.
8. **Lerner simetrisi ve reel kur.**
   - Takas, ithal ürünlere karşı göreli fiyatı değiştirir; tasarruf-yatırım dengesini değiştirmez.
   - Tarifelerin cari dengeye etkisi uluslararası kanıtta "küçük ve anlamsız" (Furceri, Hannan, Ostry ve Rose 2019; 151 ülke, 1963–2014). Türkiye'nin 2020 İGV'leri toplam ithalatı yalnızca %0,9 azalttı.
   - Takas **bir enflasyon kalkanıdır, cari açık çözümü değildir.**

### 1.8 Çıkıştan önce temizlenmesi gereken mevcut riskler

Türkiye'nin mevcut iç vergi ve teşvik düzenlemelerinde, GB içinde AB'nin dava etmediği ama çıkıştan sonra ilk hedefi olacak unsurlar var.

| Düzenleme | Sorun | Risk | Öneri |
|---|---|---|---|
| Engelli araç alımında ÖTV istisnası: %40 yerli katkı şartı (4760 md. 7/2; CK 9321, 27.12.2024) | Menşeye bağlı vergi avantajı: III:2, III:4, TRIMs | Yüksek | Şartı kaldırmak; istisnayı menşeden bağımsız yapmak |
| Kurumlar vergisinde ihracat kazancına 5 puan indirim (5520 md. 32/7) | Hukuken ihracata bağlı sübvansiyon (ASCM 3.1(a)). ABD, ihracat gelirine bağlı benzer bir indirimi (ihracat hasılatından götürü gider indirimi) 2015'te telafi edilebilir buldu (inşaat demiri) | Yüksek (yasak sübvansiyon; telafi edici vergi) | İndirimi bütün imalat kazancına genellemek. 2026'da imalat kazancına %12,5 oran getirildi (7582 sayılı Kanun); ihracat ayrımı bunun içinde eritilmeli |
| Rakı ile diğer alkollü içkiler arasında maktu ÖTV farkı (1.980 TL'ye karşı 2.228 TL) | Fiilî ayrımcılık (III:2 ikinci cümle; Japonya–Alkol, Kore–Alkol) | Orta (AB'nin engeller veri tabanında açık kayıt, no. 17082) | Farkı kaldırmak |
| Elektrikli otomobil ÖTV'sinde 160 kW eşiği ve "yerli üretimi koruma" beyanları | Fiilî ayrımcılık işaretleri (§1.7.4) | Orta | Eşiği nesnel bir verimlilik veya CO₂ ölçütüne bağlamak; gerekçeyi belgelemek |
| 2025 hurda teşviki tasarısı: "Türkiye'de üretilmiş" yeni araç şartı | III:4 ve TRIMs | Yüksek (yasalaşırsa) | Yasalaştırmamak veya menşe şartını çıkarmak |
| Elektrikli araç ithalatında yetkili servis ağı şartı (AB ve STA menşelileri muaf) | DS629: III:4 ihlali, XX(d) savunması reddedildi | Yüksek (karar alındı) | DSB kararına uyum; GB sonrası AB menşelilere de aynı kural |
| Çin menşeli elektrikli araçlara ek gümrük vergileri | DS629: bağlı oranı (%20) aşan kısım II:1(b) ihlali | Yüksek (karar alındı) | Oranı bağlı oran içine çekmek; gerekiyorsa anti-damping veya telafi edici vergi soruşturmasıyla değiştirmek |
| IMEI kayıt harcı (2026: 54.258 TL; yolcu beraberi telefon) | Yalnızca kişisel ithalata uygulanan ve ithalata özgü bir yük | Düşük–orta | Ticari ithalatla yükü eşitlemek; TRT bandrolü ve ÖTV ile tutarlı hale getirmek |

*Kaynak ve etiketler:*
- `[V]` 4760 ve 5520 sayılı Kanunların konsolide metinleri; DS629 panel raporu (WT/DS629/R, 28.7.2026).
- AB engeller veri tabanı (Access2Markets, 18.10.2026); Avrupa Komisyonu Türkiye 2025 Raporu; ABD Federal Register telafi edici vergi kararları; Türkiye vergi notu.
- Güven: Yüksek.

---

## 2. Araç evreni

Ana promptun araç seti (A–G) iç vergileri, kamu alımlarını ve dış rejim seçeneklerini içermiyordu. Aşağıdaki evren bu boşlukları kapatıyor. Her araç için şunlar verildi:
- ne yaptığı;
- hukuki sınırı;
- etkisinin yönü: TÜFE / mali / cari denge (CA) / kabiliyet (+ olumlu, − olumsuz, 0 etkisiz, ± koşula bağlı);
- uygulayıcı kurum, hukuki araç ve hazırlık süresi.

Sayısal etkiler §1, §3 ve §4'te.

### A. Tarife düzeyi ve yapısı (Türkiye'nin kendi gümrük tarife cetveli)

| No | Araç | Ne yapar | Hukuki sınır | TÜFE / mali / CA / kabiliyet | Kurum ve araç; süre |
|---|---|---|---|---|---|
| A1 | Ürün bazında MFN düzeyi | GB'den çıkınca OGT'ye bağlılık biter; her satır 0 ile bağlı oran arasında serbest | GATT II:1. Türkiye'nin satırlarının ≈%50'si bağlı; sanayide %43. Ortalama bağlı oran %28,5. ITA ürünleri sıfıra bağlı. MFN: STA'sı olmayan herkese aynı oran | Artış: − / + / ≈0 (Lerner) / ± | Ticaret Bakanlığı; Cumhurbaşkanı kararıyla İthalat Rejimi Kararı; 3–6 ay |
| A2 | Tarife merdiveni | Hammaddede %0, ara malda %0–5, nihai malda seçici | A1 ile aynı | − (girdide) / − / + / + (efektif koruma) | Aynı |
| A3 | Otomatik tarife askıya alma | Yurt içi üretimi olmayan girdide başvuruyla sıfır (AB'nin otonom askıya alma sistemi gibi) | MFN uyumlu; şeffaf ölçüt şart | + / − (küçük) / ≈0 / + | Ticaret, Sanayi ve Teknoloji Bakanlıkları; yönetmelik; 6 ay |
| A4 | Tarife kontenjanı | Kontenjan içinde sıfır veya düşük oran | GATT XIII (ayrımsız dağıtım); kontenjan dışı oran bağlı oranı aşamaz | + / − / 0 / ± | Ticaret Bakanlığı; 3 ay |
| A5 | **Bağlı oranın yeniden müzakeresi: XXVIII:5 çekincesi** | 2027–2029 boyunca bağlı oranı değiştirme hakkını saklı tutar | **Bildirim 31.12.2026'dan önce yapılmalı.** Sonra XXVIII:1–3 prosedürü: ilk müzakere hakkı ve başlıca tedarikçi çıkarı olan üyelerle müzakere ve tazminat; anlaşma olmazsa karşı tarafın eşdeğer tavizleri geri çekme hakkı | − / + / 0 / + | Dışişleri ve Ticaret Bakanlıkları; Cenevre Daimi Temsilciliği notası; **bu hafta** |
| A6 | Son kullanım ve özel kullanım muafiyeti | Belirli kullanıcıya girdi muafiyeti | Gümrük mevzuatı; MFN uyumlu | + / − / + / + | Ticaret Bakanlığı (Gümrükler); 3 ay |

### B. İGV ve ek vergiler

| No | Araç | Ne yapar | Hukuki sınır | TÜFE / mali / CA / kabiliyet | Kurum ve araç; süre |
|---|---|---|---|---|---|
| B1 | İGV'nin MFN'ye entegrasyonu ve sadeleştirme | İGV'li HS6 satırları tek orana dönüşür | GB sonrası İGV de bir MFN vergisidir: STA dışı herkese uygulanır, AB dahil | Yönüne bağlı | Ticaret Bakanlığı; İGV Kararı; 3–6 ay |
| B2 | **İGV rejim seçimi: a / b / c / c2** | AB mallarına İGV'nin uygulanıp uygulanmayacağı satır satır seçilir (§4.1) | STA olmadan AB'ye özel muafiyet mümkün değil (GATT I). Seçim yalnızca satırın oranı üzerinden, bütün STA dışı kaynaklar için yapılır | Rejime göre: c2 → + / + / 0 / + | Aynı; T−6 |
| B3 | Süreli ve kademeli İGV | Koruma süreli, azalan ve performansa bağlı | Temel ilke 7; MFN | ± | Aynı |
| B4 | Ülkeye özgü ek vergiler (ör. Çin'in elektrikli araçları) | — | DS629: bağlı oranı aşan kısım ihlal. Yerine anti-damping, telafi edici vergi ya da korunma önlemi | Bağlı oran içine çekilmeli | Ticaret Bakanlığı |

### C. İç vergiler (ÖTV, KDV, harçlar)

| No | Araç | Ne yapar | Hukuki sınır | TÜFE / mali / CA / kabiliyet | Kurum ve araç; süre |
|---|---|---|---|---|---|
| C1 | **Tarife + menşeden bağımsız ÖTV takası (T-A)** | AB malına tarife; aynı üründe bütün menşelere eşit ÖTV indirimi. Grup fiyat endeksi sabit, yerli ürün AB ürününe göre tarife kadar ucuzlar | Tarife bağlı oran içinde ve MFN; ÖTV indirimi bütün benzer ürünlere aynı oranda; yeni eşik yaratmadan. Risk düşük (§1) | 0 / ≈0 / ≈0 / + | HMB ve GİB; ÖTV oranları Cumhurbaşkanı kararıyla (4760 md. 12); çıkış günü |
| C2 | Tarife + menşeden bağımsız KDV takası | ÖTV'si olmayan tüketim mallarında (giyim, ayakkabı, mobilya, gıda) aynı mantık | KDV oranları Cumhurbaşkanı kararıyla (3065 md. 28); ayrımsız | 0 / ≈0 / ≈0 / + | HMB; çıkış günü |
| C3 | ÖTV'nin nesnel ölçütlerle yeniden tasarımı (CO₂, verimlilik, boyut) | Vergi yükünü ürün özelliklerine göre dağıtır | Görünüşte menşeden bağımsız olsa da yerli modelin özelliğine göre kesilmiş eşikler fiilî ayrımcılık riski taşır (III:2 ikinci cümle) | ± | HMB; risk düşük–orta |
| C4 | **Yalnızca yerli ürüne ÖTV/KDV indirimi (T-0)** | Önerinin ilk biçimi | **GATT III:2 kendiliğinden ihlal.** Şarta bağlanırsa III:4, TRIMs 2.1 ve ASCM 3.1(b). AB dava açar, misilleme hakkı kazanır | Kullanılmamalı; ayrıca pahalı (§1.5) | — |
| C5 | TRT bandrolü (TV %16, telefon %12) | Menşeden bağımsız bir iç ödeme | Takas için ek alan; ayrımsız kullanılmalı | 0 / ± / 0 / 0 | HMB, Kültür ve Turizm Bakanlığı |
| C6 | Harçlar ve kayıt ücretleri (ör. IMEI) | İthal ürüne fiilen ek yük | İthalata özgü ise "diğer vergi ve harçlar" (II:1(b)) veya III:2 kapsamında risk | Gözden geçirilmeli | — |
| C7 | ÖTV dilim eşiklerinin gümrük vergisinden arındırılması | Tarifenin ithal aracı üst dilime itmesini önler | Menşeden bağımsız teknik bir düzeltme | + / − (küçük) / 0 / 0 | HMB; çıkış günü |

### D. Sübvansiyonlar ve teşvikler

| No | Araç | Ne yapar | Hukuki sınır | TÜFE / mali / CA / kabiliyet | Kurum ve araç; süre |
|---|---|---|---|---|---|
| D1 | Yerli üreticiye III:8(b) üretim ödemesi (T-B) | Vergi tek tip kalır, yerli üretici birim başına ödeme alır | GATT md. III'ten muaf. ASCM: sektöre özgü, dava edilebilir (6.3(a) ithal ikamesi yoluyla ciddi zarar) ve ihracat pazarında telafi edici vergiye açık | 0 / −− / ± / + | STB; kanun veya Cumhurbaşkanı kararı; risk orta |
| D2 | Yatırım teşvikleri (CK 9903 ve sonrası) | KDV istisnası, gümrük muafiyeti, faiz ve SGK prim desteği | Dava edilebilir. ABD'nin Türk çeliğine telafi edici vergi kararlarında bölgesel teşvik (RIIS) vergi indirimi, Eximbank kredileri, arazi tahsisi ve enerji fiyatlaması inceleme konusu oldu | 0 / − / + (orta vade) / + | STB |
| D3 | Ar-Ge, tasarım ve beceri destekleri | 5746 sayılı Kanun, TÜBİTAK, teknoloji geliştirme bölgeleri | Düşük risk (genel nitelikli) | 0 / − / + / + | TÜBİTAK, STB |
| D4 | Bölgesel istihdam desteği | Yüksek riskli bölgelerde SGK prim desteği (giyim kümeleri) | Bölgesel spesifiklik; ihracata bağlı değilse dava edilebilir ama düşük öncelikli | 0 / − / 0 / + | SGK, İŞKUR, Çalışma Bakanlığı |
| D5 | İhracat sübvansiyonu | — | **Yasak** (ASCM 3.1(a)). Eximbank kredileri yalnızca OECD Uzlaşması faiz kurallarına uygunsa güvenli liman içinde (Ek I (k)) | Kullanılmamalı. Mevcut **kurumlar vergisi md. 32/7 indirimi** bu kapsamda (§1.8) | — |
| D6 | Yerli girdi şartlı destek | — | **Yasak** (ASCM 3.1(b), TRIMs) | Kullanılmamalı | — |
| D7 | İmalat kazancına indirimli kurumlar vergisi (%12,5; 7582 sayılı Kanun) | Bütün imalatçıya | Menşeden bağımsız ama sektöre özgü olabilir (ASCM 2.1); ihracat ayrımı içermemeli | 0 / − / + / + | HMB |

### E. Kamu alımları

| No | Araç | Ne yapar | Hukuki sınır | TÜFE / mali / CA / kabiliyet | Kurum ve araç; süre |
|---|---|---|---|---|---|
| E1 | Yerli malı fiyat avantajı (%15'e kadar) | 4734 md. 63. 2024'te uluslararası ihalelerin değer olarak %54'ünde uygulandı | Türkiye Hükûmet Alımları Anlaşması'na (GPA) taraf değil: serbest. III:8(a) yalnızca devletin kendi kullanımı için alımı kapsar; tüketiciye sübvansiyonlu satış kapsam dışı | − (küçük) / − / + / + | KİK, HMB |
| E2 | Kamu alımında karşılıklılık | Cumhurbaşkanı, yerli istekli ve yerli mal avantajını karşılıklılık esasıyla AB istekli ve mallarına genişletebilir (7590 sayılı Kanun md. 13, 2026) | Müzakerede koz; AB'nin Uluslararası Kamu Alımı Aracı karşısında simetri | 0 / 0 / + / ± | Cumhurbaşkanlığı, KİK |
| E3 | Offset ve sanayi katılımı | Savunma, raylı sistem, enerji, sağlık | GPA dışında serbest | 0 / − / + / + | SSB, ilgili bakanlıklar |
| E4 | Geri ödeme ve ruhsat üzerinden yerelleştirme (ilaç) | — | **DS583**: SGK geri ödemesi kamu alımı sayılmadı; III:4 ihlali | Kullanılmamalı | — |

### F. Ticaret savunması

| No | Araç | Ne yapar | Hukuki sınır | TÜFE / mali / CA / kabiliyet | Kurum ve araç; süre |
|---|---|---|---|---|---|
| F1 | Anti-damping | Dampingli ithalata ek vergi | Anti-Damping Anlaşması; kanıt ve soruşturma (12–18 ay); kamu yararı testi | − / + / ≈0 / + | Ticaret Bakanlığı İthalat GM |
| F2 | Telafi edici vergi | Sübvansiyonlu ithalata vergi | ASCM Kısım V | − / + / ≈0 / + | Aynı |
| F3 | Korunma önlemi | İthalat artışına karşı geçici tarife veya kota | Korunma Anlaşması: kaynağı ne olursa olsun uygulanır; en fazla 4 + 4 yıl, gelişmekte olan ülkeye +2. Tazminat aranır; mutlak artışa dayanıyorsa 3 yıl karşı önlem yok. GB'den çıkışta AB ithalatı azalır, artmaz; bu yüzden AB'ye karşı bir araç değildir | − / + / ≈0 / + | Aynı |
| F4 | Gözetim (kıymete dayalı) | İthalat fiyat tabanı | AB eleştirisi; Gümrük Kıymeti Anlaşması riski | Sınırlı kullanılmalı | Aynı |

### G. Gümrük rejimleri

| No | Araç | Ne yapar | Hukuki sınır | TÜFE / mali / CA / kabiliyet | Kurum ve araç; süre |
|---|---|---|---|---|---|
| G1 | Dahilde işleme rejimi (DİR) | İhracatçının ithal girdisi vergisiz; S4'te AB girdileri de kapsanır | ASCM Ek I(i), II, III: yalnızca fiilen kullanılan girdi; girdi-çıktı normları ve doğrulama. ABD 2015'te DİR'de telafi edilebilir fayda bulmadı. S2/S3'te revize PEM'in geri ödeme kuralları geçerli (yasak yalnızca 50–63. fasıllar) | + / − / + / + | Ticaret Bakanlığı |
| G2 | Serbest bölgeler, hariçte işleme | 3218 sayılı Kanun | AB eleştirisi (Türkiye Raporu 2025); S2'de pazarlık konusu | ± | Ticaret Bakanlığı |
| G3 | Yetkilendirilmiş yükümlü (AEO), tek pencere, NCTS ve Ortak Transit | Menşe ve gümrük maliyetini düşürür | Ortak Transit GB'den bağımsız (Faz 0 H-9) | + / 0 / + / + | Ticaret Bakanlığı |
| G4 | Yoldaki mal hükmü | Çıkış günü yolda olan malın eski rejimle girişi | AB–Birleşik Krallık Ticaret ve İşbirliği Anlaşması (TCA) md. 67 emsali: 12 ay | + / 0 / + / + | Ticaret Bakanlığı; anlaşma veya tek taraflı geçiş hükmü |

### H. Teknik mevzuat ve kalite altyapısı

| No | Araç | Ne yapar | Hukuki sınır | TÜFE / mali / CA / kabiliyet | Kurum ve araç; süre |
|---|---|---|---|---|---|
| H1 | CE işaretini tek taraflı kabul | Türkiye pazarında CE'li ürün ek belge istemeden satılır | Ticarette Teknik Engeller Anlaşması (TBT) ile uyumlu; ithalatı kolaylaştırır (dezenflasyonist), ama karşılıklılık kozunu azaltır. İngiltere 21 tüzük için CE'yi süresiz kabul ediyor | + / 0 / − / 0 | Ticaret ve STB; 7223 sayılı Kanun ikincil mevzuatı |
| H2 | Türk onaylanmış kuruluşlarının statüsü | AB pazarına giden Türk ürünü için AB'de geçerli sertifika | NANDO'da 95 Türk kaydı (≈81'i yürürlükte), 16+ mevzuat alanında. Uyum değerlendirme anlaşması (ACAA) veya karşılıklı tanıma anlaşması (MRA) yoksa çıkışta AB geçerliliği biter (İngiltere 2020 ve İsviçre tıbbi cihaz 2021 dersleri) | 0 / 0 / − (yoksa) / − (yoksa) | STB, TÜRKAK |
| H3 | Piyasa gözetimi ve denetimi | Standart altı ithalata karşı; enflasyonist değil | TBT 2.1 (ayrımsız) ve 2.2 (gereklilik) | 0 / − / + / + | Ticaret Bakanlığı, TSE |

### I. Dış anlaşmalar

| No | Araç | Ne yapar | Hukuki sınır | TÜFE / mali / CA / kabiliyet | Kurum ve araç; süre |
|---|---|---|---|---|---|
| I1 | AB ile yeni çerçeve | S2 (DCFTA), S3 (temel STA), geçici anlaşma ve dondurma (§6) | GATT XXIV:8(b) ("ticaretin esasının tamamı"), XXIV:5(c) geçici anlaşma (makul süre en fazla 10 yıl). AB tarafında md. 207 (nitelikli çoğunluk) veya md. 217 (oybirliği) | + / ± / + / + | Dışişleri, Ticaret; Faz 2B |
| I2 | Kendi STA ağı | Hindistan, Mercosur, Japonya, Meksika, Kanada, Körfez İşbirliği Konseyi (KİK), ASEAN; ABD ile sektörel anlaşma | XXIV. GB sonrası paralel STA zorunluluğu kalkar. Kaldıraç: bu ortakların Türkiye'ye ihracatı $30,2 mlr (Faz 1 §2.1) | + / − / + / ± | Ticaret Bakanlığı; 1–4 yıl |
| I3 | Pan-Avrupa-Akdeniz (PEM) kümülasyonu | AB, EFTA, Batı Balkanlar ve Akdeniz ortaklarıyla çapraz kümülasyon | Türkiye PEM Sözleşmesi tarafı (2014'ten beri). Çapraz kümülasyon için AB–Türkiye STA'sının menşe protokolü PEM'e atıf yapmalı. Revize PEM kuralları 1.1.2025'ten beri geçerli | + / 0 / + / + | Ticaret Bakanlığı |

### J. Makro ve tamamlayıcı araçlar

| No | Araç | Ne yapar | Hukuki sınır | TÜFE / mali / CA / kabiliyet | Kurum ve araç; süre |
|---|---|---|---|---|---|
| J1 | Kur politikası | — | Dezenflasyonla çatışır (temel ilke 4); araç değil | — | TCMB |
| J2 | Kamu tasarrufu | Cari denge ≥ %0 için kamu tasarruf-yatırım açığının kapanması (Faz 1 §3.3) | Bütçe | + (orta vade) / + / + / 0 | HMB, SBB |
| J3 | Enerji dönüşümü ve verimlilik | Enerji ithalatı (2025: $62,5 mlr) cari açığın ana kaynağı | — | ± / − / + / + | ETKB |
| J4 | Altın ithalatı yönetimi | 2023 kotası emsal | Miktar kısıtlaması GATT XI riski; fiyat temelli araçlar tercih edilmeli | 0 / + / + / 0 | Ticaret Bakanlığı, TCMB |
| J5 | Türkiye emisyon ticaret sistemi (TR-ETS) ve SKDM mahsubu | Karbon fiyatı Türkiye'de kalır | İklim Kanunu 7552 | ± / + / + / + | ÇŞİDB |
| J6 | Ödemeler dengesi önlemi (GATT XII/XVIII:B) | Genel ithalat düzeyine fiyat temelli ek vergi | Rezervler yeterliyse savunulamaz (Hindistan–Miktar Kısıtlamaları); AB'yi hedefleyemez. Brüt rezerv $185 mlr (Ağustos 2026) | Kullanılmamalı | — |
| J7 | Güvenlik istisnası (GATT XXI) | — | Paneller "uluslararası ilişkilerde olağanüstü durum" şartını nesnel olarak inceliyor (Rusya–Transit, DS512); ekonomik bir çıkış için inandırıcı değil | Kullanılmamalı | — |

### K. Hizmetler ve hareketlilik

| No | Araç | Ne yapar | Hukuki sınır | TÜFE / mali / CA / kabiliyet | Kurum ve araç; süre |
|---|---|---|---|---|---|
| K1 | Karayolu taşıma kotaları ve transit | Kota maliyeti ≈$1,3 mlr/yıl ihracat (2005–12 ortalaması, `[D?]`) | GB'nin dışında; yeni anlaşmada ilk kez masaya konabilir | + / 0 / + / + | UAB |
| K2 | İş vizesi ve hizmet sunucularının dolaşımı | Ankara Anlaşması ve Katma Protokol md. 41 "standstill" hükmü, üye devlet yetkisi olarak sürer (Soysal, Demirkan) | Yeni anlaşmada hizmetler ve geçici hareket (Mod 4) | + / 0 / + / + | Dışişleri |
| K3 | Hizmet ticareti faslı | Bilgi teknolojileri, mühendislik, müteahhitlik | GATS md. V | + / 0 / + / + | Ticaret Bakanlığı |

---

## 3. Politika alanı haritası

### 3.1 Bağlı oranlar: tarifeyi nereye kadar yükseltebiliriz?

GB'den çıkınca Türkiye'nin AB mallarına uygulayabileceği tarifenin üst sınırı DTÖ bağlı oranıdır. MFN ilkesi gereği bu oran STA'sı olmayan herkese uygulanır.

| Ürün | 2026 uygulanan MFN (%) | MFN + İGV + EMY, STA dışı (%) | Bağlı oran (%) | Boşluk | Not |
|---|---|---|---|---|---|
| Binek otomobil (8703) | 5–10 (çoğu 10) | 5–20 | **Kısmen bağlı:** HS2002 cetvelinde 18 satır bağlı (17'si %19, elektrikli araç satırı 8703.90.10 %20). Diğer içten yanmalı motorlu otomobil satırları bağsız | Bağlı satırlarda 9–10 puan; bağsızlarda hukuken sınırsız | DS629 panel raporu, para. 7.30, 7.41, 7.73. Satır listesi Faz 5'te (VB-10) |
| Hafif ticari ve kamyon (8704) | 0–22 | 0–22 | 17,4–22 | 0–10 | Bazı satırlarda boşluk yok |
| Otobüs (8702) | 10–16 | 10–20 | 19,4–20 | 4–10 | |
| TV (8528.72) | 14 | 14 | 35,6 | ≈21 | |
| Bulaşık makinesi (8422.11) | 2,7 | 12,7 | 17 | ≈14 | |
| Klima (8415) | 0–2,7 | 0–9,7 | 9–11,1 | 6–9 | |
| Lastik (4011) | 0–4,5 | 0–26,3 | 26,3 | MFN'de 22; İGV ile 0 | İGV tam bağlı orana ayarlanmış |
| Mobilya (9403) | 0–5,6 | 17,7–32,7 | 62,2 | >55 | |
| Kozmetik (3303, 3304) | 0 | 25 | 62,6 | >60 | |
| Buzdolabı, çamaşır makinesi (8418, 8450) | 1,5–3 | 2,2–22,2 | Cetvelde bulunamadı | — | Büyük olasılıkla bağsız `[D?]` |
| Bilgisayar, cep telefonu (8471, 8517.13) | 0 | 0 | 0 (ITA-I) | 0 | **Artırılamaz** |
| Giyim (61–62), ayakkabı (64) | 6,3–12; 3–17 | 16–51; 13–57 | Çoğunlukla bağsız | Serbest | DTÖ profili: giyimde bağlama oranı %3,7 |

*Kaynak ve etiketler:*
- `[V]` Uygulanan oranlar: 2026 İthalat Rejimi Kararı ve İGV kararları (GTİP12, `veri/tarife_tr_2026_gtip12.csv`).
- Bağlı oranlar: Türkiye Cetvel XXXVII, UR94 ve HS2002 aktarımı; DS629 panel raporu; DTÖ tarife profili.
- Cetvel dosyaları eksik: sanayide HS6 satırlarının %29'unu, tarımda %40'ını kapsıyor. Kesin satır listesi için WTO TTD veya API anahtarı gerekiyor (VB-10).
- Güven: Orta.

**Okuma.**
- Otomobilde AB mallarına uygulanacak %10'luk MFN'yi bağlı satırlarda %19–20'ye çıkarma alanı var. Bağsız satırlarda alan hukuken sınırsız. Ancak üç fren var:
  - itibar;
  - STA müzakerelerinde bağlı oranların karşı tarafça referans alınması;
  - otomobilin TÜFE ağırlığı: her 1 puanlık ek tarife ≈+2,6 bp (takassız).
- ITA ürünlerinde alan sıfır.
- Bağsız satırlarda (giyim, ayakkabı, beyaz eşyanın bir kısmı) hukuki alan geniş.
- **XXVIII:5 çekincesi** (§2 A5), 2027–2029'da bağlı satırların da yeniden müzakere edilebilmesini sağlar. Çıkış tarihi T2028 veya T2029 olduğu için bu dönem tam olarak kritik dönemdir.

### 3.2 Yurt içi kabiliyet ve "girdide sıfır" (P1)

**Veri.** TÜİK'in Yıllık Sanayi Ürün (PRODCOM/PRODTR) İstatistikleri (26.6.2026), 2005–2025 için CPA 2.2'nin 6 hanesi düzeyinde üretimden satış değerini ve girişim sayısını veriyor (`kod/prodtr.py`, `veri/prodtr_cpa6_2025.csv`).
- 2025'te 1.518 CPA ürün grubunun 461'inde veri gizli; bu, az sayıda üretici olduğu anlamına gelir.
- Bu veri Faz 3'te kabiliyet kısıtının (b) bendi için, yani girişim sayısının kritik eşiği için doğrudan kullanılacak.

**"Girdide sıfır" (P1).** Sanayi fasıllarında (25–97) iki koşulu birlikte sağlayan satırlar seçildi:
- BEC sınıflamasına göre ara malı veya sermaye malı;
- yurt içi üretimi, aynı CPA grubunun ithalatının %10'undan az.

| | HS6 satırı | İthalat 2024 ($ mlr) | Bunun AB'den kısmı ($ mlr) | Yasal gümrük geliri ($ mn) | İthalat ağırlıklı oran (%) |
|---|---|---|---|---|---|
| Üretilmeyen ara malları | 451 | 30,8 | 10,3 | 242 | MFN 1,2; İGV dahil 1,5 |
| Üretilmeyen sermaye malları | 90 | 14,8 | 6,8 | 117 | |
| **P1 toplamı** | **541** | **45,6** | **17,2** | **360** | |
| Karşılaştırma: yurt içinde üretilen sanayi girdileri | ≈3.000 | ≈187 | ≈59 | ≈5.000 | MFN 3,5; İGV dahil 6,6 |

*Kaynak:* `[T]` `kod/f2b_tarife_politikasi.py`; BACI 2024; PRODTR 2025; WITS HS2017 → BEC Rev. 4; 2026 tarifesi. Güven: Orta.

**Olumsuz bulgu.**
- Üretilmeyen girdilerde tarifeyi sıfırlamanın getirisi küçük: yasal gelir kaybı ≈$0,36 mlr (tahsil edilebilir ≈$0,14 mlr), TÜFE etkisi −4 ile −5 bp. Çünkü AB'nin OGT'si bu girdilerde zaten düşük.
- "Özerklik temettüsünün" asıl büyüklüğü başka yerde:
  - yurt içinde üretilen girdilerdeki koruma: ≈$5 mlr yasal gelir, İGV dahil %6,6;
  - tüketim mallarındaki İGV.
- Bu alanlarda indirim üretici kabiliyetiyle doğrudan çatışır. Karar ürün ürün verilmeli: sınıf kartları Faz 3'te, tarife cetveli Faz 5'te.

### 3.3 Koruma yapısı: MFN ve İGV

| Kullanım (BEC) | Yurt içi üretim | HS6 | STA dışı ithalat ($ mlr) | MFN geliri ($ mlr) | İGV geliri ($ mlr) |
|---|---|---|---|---|---|
| Ara malı (sanayi) | var | 2.435 | 63,9 | 2,49 | 1,72 |
| Ara malı (sanayi) | yok/zayıf | 451 | 17,3 | 0,19 | 0,06 |
| Sermaye malı | var | 577 | 16,7 | 0,28 | 0,48 |
| Tüketim malı (sanayi) | var | 651 | 9,2 | 0,66 | 2,29 |
| Tarım ürünleri (fasıl 1–24) | — | ≈800 | 14,3 | ≈7,6 | ≈0 |
| **Toplam** | | 5.612 | | **11,6** | **4,6** |

*Kaynak:* `[T]` 2026 oranları × BACI 2024 ithalatı. GSP tercihleri ve DİR, teşvik ve serbest bölge muafiyetleri yok sayıldı; yasal üst sınırdır. Güven: Orta.

**Okuma.**
- İGV ağırlıkla yurt içinde üretilen tüketim mallarında ($2,3 mlr) ve ara mallarda ($1,7 mlr) yoğunlaşıyor. Tüketim mallarının başında giyim, ayakkabı ve ev eşyası geliyor.
- Bu yapı GB'nin kuralı değil, Türkiye'nin 2011 sonrası tercihi.
- GB sonrası İGV'nin kaderi §4.1'deki rejim seçimiyle belirlenir.

### 3.4 Gelir tabanı ve tahsilat oranı

| | $ mlr | Kaynak |
|---|---|---|
| Yasal gümrük geliri: 2026 oranları × 2024 ithalatı | 16,2 | `[T]` f2b |
| 2025 gerçekleşen gümrük vergileri (İGV dahil varsayıldı) | 8,15 (321,8 mlr TL) | `[V]` GİB Tablo 28; `[D?]` İGV'nin bu kalemde olup olmadığı |
| **Toplam tahsilat oranı** | **%50** | `[T]` |
| Sanayi tüketim ve karma kullanım malları (otomobil dahil): muafiyet yok | %100 varsayım (yasal 3,3) | `[H]` |
| Ara malı, sermaye malı ve tarım: DİR, teşvik belgesi ve GSP | **%38** (kalan) | `[T]` |
| Karşılaştırma: ÖTV (II) motorlu taşıtlar, 2025 | 20,2 (796,1 mlr TL) | `[V]` GİB |
| KDV (ithalde), 2025 | 43,7 (1.726,8 mlr TL) | `[V]` GİB |

**Okuma.**
- S4'te AB mallarından alınacak yasal gümrük geliri (MFN, $4,3 mlr; MFN + İGV, $10,8 mlr) aynı oranlarla düşer.
- Rejim "a"nın tahsil edilebilir geliri ≈$7,6 mlr, rejim "c"ninki ≈$2,7–3,0 mlr.
- Mali bilançolar §4.1'de hem yasal hem tahsil edilebilir olarak verildi. Karar için ikincisi esas alınmalı.
- Takasın maliyeti, yani ÖTV ve KDV indirimi, ise tam gerçekleşir. Bu yüzden tahsilat düzeltmesi takaslı paketlerin mali bilançosunu yasal hesaba göre 0,1–0,2 puan kötüleştirir.

---

## 4. Aktif S4: anlaşmasız çıkışta Türkiye'nin kendi paketiyle neler değişiyor?

Faz 1, S4'ü pasif bir senaryo olarak ele aldı. Aşağıda aynı şok, Türkiye'nin kendi araçlarından kurulan paketlerle yeniden hesaplanıyor. Bir paketin üç boyutu var.

**İGV rejimi.** GB sonrası İGV bir MFN vergisidir; STA olmadan AB'yi muaf tutmak mümkün değil. Seçenekler:
- (a) İGV AB'ye de uygulanır;
- (b) İGV, STA dışı bütün kaynaklar için kaldırılır;
- (c) seçici: AB'nin baskın olduğu satırlarda (AB / (AB + diğer) ≥ %50) İGV herkes için kaldırılır, diğer satırlarda AB'ye de uygulanır;
- (c2) kabiliyete duyarlı seçici: c'de İGV yalnızca yurt içi üretimi zayıf satırlarda (PRODTR üretimi < ithalat) kaldırılır, güçlü satırlarda AB'ye de uygulanır;
- (d) AB ile XXIV:5 kapsamında geçici anlaşma: tercihler sürer. Bu artık S4 değildir, karşılaştırma için verildi.

**P1, girdide sıfır.** Üretilmeyen 541 sanayi girdisinde MFN ve İGV sıfırlanır.

**P3, vergi takası.** İki kapsam:
- dar: otomobil (ÖTV II), beyaz eşya ve elektronik (ÖTV IV), kozmetik ve temizlik (ÖTV IV/KDV), giyim ve tekstil (KDV);
- geniş: bütün imalat ürünlerinde hanehalkı fiyatı ÖTV/KDV ile nötrlenir. Tarım, enerji ve hizmetlere geçen maliyet etkisi nötrlenmez.

### 4.1 Enflasyon, mali bilanço ve koruma: paket sınırı

**Tablo 4.1 — Rejim × takas kapsamı (P1 dahil; TÜFE: ρ = 0,6 / 0,8 / 1,0; mali: ρ = 0,8, 2025 GSYH'sine oranla)**

| Rejim | Takas | TÜFE, birinci tur (bp) P10 / P50 / P90 | Net mali, yasal (GSYH %) | **Net mali, tahsil edilebilir (GSYH %)** | Takas maliyeti ($ mlr) | Güçlü yerli üretimli satırlarda kaldırılan İGV ($ mlr) | AB'nin Türkiye'ye ihracat kaybı, σ = 5 ($ mlr) |
|---|---|---|---|---|---|---|---|
| Pasif S4 (a, P1 yok) | yok | 59 / **78** / 98 | +0,68 | +0,47 | — | 0 | −32,2 |
| a: İGV AB'ye de | yok | 55 / 73 / 92 | +0,64 | +0,46 | — | 0 | −31,1 |
| a | dar | 20 / 27 / 33 | +0,38 | +0,20 | 4,1 | 0 | −31,1 |
| a | geniş | 3 / **4,0** / 5 | +0,25 | +0,07 | 6,2 | 0 | −31,1 |
| b: İGV herkes için kalkar | yok | 1 / **1,5** / 2 | −0,05 | −0,04 | — | **2,9** | −16,4 |
| b | dar | −16 / −21 / −26 | −0,18 | −0,17 | 2,0 | 2,9 | −16,4 |
| c: seçici | yok | 32 / 42 / 53 | +0,23 | +0,17 | — | 0,7 | −18,7 |
| c | dar | 6 / **7,5** / 9 | +0,04 | −0,02 | 3,1 | 0,7 | −18,7 |
| c | geniş | 1,0 / 1,3 / 1,6 | 0,00 | −0,06 | 3,7 | 0,7 | −18,7 |
| c2: kabiliyete duyarlı seçici | yok | 51 / 68 / 85 | +0,55 | +0,41 | — | 0 | −28,5 |
| c2 | dar | 18 / 24 / 30 | +0,31 | +0,17 | 3,9 | 0 | −28,5 |
| **c2** | **geniş** | **2,5 / 3,3 / 4,1** | +0,19 | **+0,05** | 5,7 | **0** | **−28,5** |
| d: geçici anlaşma (S4 değil) | — | −3 / −3,5 / −4 | −0,02 | −0,01 | — | 0 | 0 |

*Kaynak ve etiketler:*
- `[T]` `kod/f2e_s4_aktif.py`, `veri/politika_s4_aktif.csv`. Leontief fiyat modeli; TÜİK 2023 yurt içi ve ithal girdi-çıktı tabloları; BACI 2024 ithalatı; 2026 Türk tarifesi.
- Yurt içi rakiplerin fiyat uydurması (κ) 0. κ = 0,5 duyarlılığında pasif S4 ≈182 bp (Faz 1).
- Tahsil edilebilir gelir §3.4'teki oranlarla hesaplandı.
- AB'nin kaybı kısmi denge: ΔM = M_AB × ((1 + t)^−σ − 1), BACI 2024 tabanı.
- Takas maliyeti, nötrlenen fiyat artışı × alıcı fiyatlarıyla hanehalkı tüketimi.
- Güven: Orta.

**Okuma.**
1. **Enflasyon kısıtı aktif tasarımla karşılanabiliyor.** İlk yıl 30 bp altında kalan dört paket:
   - c + dar: 7,5 bp;
   - c2 + geniş: 3,3 bp;
   - a + geniş: 4,0 bp;
   - b + yok: 1,5 bp.

   c2 + dar (24 bp) ve a + dar (27 bp) yıllık tavanın altında kalıyor, ama kümülatif 50 bp bütçesinin yarısını tüketiyor.
2. **Paketler arasında gerçek bir seçim var.** Bedel üç yerden ödeniyor: bütçe, koruma ve AB'ye verilen sinyal.
   - **b** en ucuz enflasyon çözümü. Ama Çin ve diğer kaynaklara karşı $2,9 mlr'lık İGV korumasını yurt içi üretimi güçlü satırlarda kaldırır. Bu, Faz 3'teki kabiliyet kısıtıyla çatışır.
   - **c** (Faz 2 ara raporundaki öneri) korumanın $0,7 mlr'ını kaldırır ve mobilya ile kozmetikte yerli üreticiye zarar verir (§1.5). Mali olarak hafif negatif.
   - **c2 + geniş** korumayı tamamen korur, TÜFE'yi 3,3 bp'de tutar ve tahsil edilebilir gelirle bile hafif pozitif kalır. Bedeli daha geniş bir vergi takası ($5,7 mlr ÖTV/KDV indirimi) ve daha karmaşık bir uygulama.
   - **a + geniş**: c2'den farkı, İGV'nin kabiliyeti zayıf satırlarda da AB'ye uygulanması. Mali olarak biraz daha iyi, ama AB'den gelen ve yurt içinde üretilmeyen girdileri gereksiz yere pahalılaştırır.
3. **Öneri: c2 + P1 + geniş takas.**
   - "Geniş" kapsamın pratik karşılığı şöyle: dar kapsama mobilya (KDV), gıda ve içecek (KDV) ve plastik ürünler eklenir.
   - Bu üç ürün, c2'de dar takastan sonra kalan TÜFE etkisinin ≈%80'ini oluşturuyor: mobilya 11,5 bp, gıda 5,9 bp, plastik 1,9 bp.
   - Bu paket aynı zamanda AB'nin anlaşmasızlık maliyetini $28,5 mlr'a çıkarıyor; c'de $18,7 mlr. Müzakere kaldıracı açısından da en güçlüsü.
4. **Takas bütçeyi değil, vergi yapısını değiştirir.**
   - Geniş takas, ÖTV ve KDV'de yılda ≈$5,7 mlr indirim demek: 2025 ÖTV + KDV tahsilatının ≈%3'ü.
   - Bu indirim, AB mallarından alınan gümrük geliriyle finanse edilir.
   - Net etki küçüktür. Ama vergi bileşimi tüketimden dış ticarete kayar. Bu tercihin orta vadede gözden geçirilmesi gerekir (Faz 6).

### 4.2 Net istihdam: ihracat kaybı ve ithal ikamesi

Faz 1'deki S4 risk istihdamı (207 bin) yalnızca ihracat tarafıydı. Türkiye de AB mallarına MFN uyguladığında AB'den ithalatın bir kısmı yurt içi üretime kayar.

| | σ = 3 | σ = 5 | σ = 8 |
|---|---|---|---|
| İhracat kaybı ($ mlr) | −15,2 | −23,5 | −33,7 |
| İthal ikamesiyle yurt içi satış artışı ($ mlr) | +8,0 | +12,4 | +18,0 |
| İstihdam: ihracat tarafı | −123 bin | −190 bin | −272 bin |
| İstihdam: ithal ikamesi | +47 bin | +73 bin | +106 bin |
| **Net imalat istihdamı** | **−77 bin** | **−117 bin** | **−165 bin** |
| Net kaybı %5'i aşan sınıf sayısı | 14 | 22 | 32 |
| Net kazanan sınıf sayısı | 61 | 61 | 61 |

*Kaynak ve etiketler:*
- `[T]` `kod/f2d_s4_net_istihdam.py`, NACE sınıfı düzeyinde.
- İhracat kaybı: Faz 0 S4 tarife duvarı (CN8).
- İthal ikamesi: AB'den ithalatın kaybı (2026 MFN, İGV hariç), yerli ürünün iç pazardaki Armington payıyla yurt içine dağıtıldı. İç satış = max(PRODTR 2025, YSHİ 2024) − ihracat (BACI 2024).
- İstihdam: YSHİ 2024 sınıf düzeyi çalışan/üretim oranı.
- Statik ve telafisiz bir hesap; çapa yatırımcı kararları ve girdi bağlantıları yok.
- İGV'nin AB'ye uygulandığı rejimlerde (a, c2) ve vergi takasıyla ithal ikamesi daha büyük. On grupta takas +9 bin ek istihdam getiriyor (§1.5), ama net tablo değişmiyor.
- Güven: Orta.

**Bölüm düzeyinde net etki (σ = 5)**

| NACE | Bölüm | Çalışan (bin) | İhracat tarafı (bin) | İthal ikamesi (bin) | Net (bin) | Net (% bölüm) |
|---|---|---|---|---|---|---|
| 14 | Giyim | 668,7 | −86,2 | +13,6 | **−72,6** | **−10,9** |
| 13 | Tekstil | 493,4 | −16,7 | +3,4 | −13,3 | −2,7 |
| 29 | Motorlu taşıtlar | 255,3 | −19,9 | +12,5 | −7,4 | −2,9 |
| 27 | Elektrikli teçhizat | 231,6 | −11,2 | +5,1 | −6,1 | −2,6 |
| 25 | Fabrikasyon metal | 474,7 | −8,5 | +2,7 | −5,8 | −1,2 |
| 22 | Kauçuk ve plastik | 283,5 | −10,8 | +5,9 | −4,9 | −1,7 |
| 28 | Makine | 319,0 | −11,8 | +7,3 | −4,6 | −1,4 |
| 24 | Ana metal | 194,1 | −4,2 | +0,8 | −3,5 | −1,8 |
| 15 | Deri ve ayakkabı | 75,8 | −2,8 | +5,2 | **+2,4** | +3,1 |
| 30 | Diğer ulaşım araçları | 86,9 | −1,2 | +2,0 | +0,8 | +0,9 |
| 10 | Gıda | 610,3 | −3,1 | +3,7 | +0,6 | +0,1 |
| 20 | Kimya | 128,0 | −3,3 | +3,6 | +0,3 | +0,2 |

*Kaynak:* `[T]` `veri/politika_s4_net_istihdam_sinif.csv`.

Net kaybı %5'i aşan 22 sınıf (σ = 5):
- 10.86; 13.92;
- giyim: 14.13, 14.14, 14.19, 14.31, 14.39;
- 20.14, 23.42, 24.42, 25.99;
- 26.52, 26.70, 27.11, 27.90;
- 28.11, 28.15, 28.24;
- 29.10, 30.92, 32.13, 32.20.

Bu sınıflar ana promptun destek tetikleyicisini (>%5 kayıp) çalıştırır ve Faz 3'te ayrı ayrı ele alınacak.

**Okuma.**
- İthal ikamesi, ihracat kaybının yaklaşık %38'ini istihdam olarak geri kazandırıyor.
- Ama kaybın yapısı farklı:
  - Otomotiv (29.10) iç pazarda AB ithalatının yerini alabiliyor: −14,8 bin ihracat tarafı, +10,0 bin ikame. Takasla bu +12,3 bine çıkıyor.
  - Giyim (14) bunu yapamıyor. İç pazarda AB'nin payı küçük (≈%2–5); kayıp AB pazarında.
- **Giyim, S4'te istihdam kısıtının çözülemeyen çekirdeği.**
  - AB'nin %12'lik MFN'sine karşı Bangladeş ("Silah Hariç Her Şey" rejimi, EBA), Fas, Tunus ve Vietnam sıfır tarifeyle giriyor; Fas, Tunus ve Vietnam'ın AB ile STA'sı var.
  - Türkiye'nin AB giyim ithalatındaki payı zaten düşüşte (Faz 1).
  - Bu sınıflar S4'te F arketipine (yönetilen uyum) girer. S2/S3'te ise menşe kuralı belirleyici olur (giyimde çift dönüşüm).

### 4.3 Cari denge ve reel kur

- **İlk yıl, kısmi denge.**
  - AB'ye ihracat kaybı −€21,5 mlr (σ = 5).
  - AB'den ithalat kaybı −€19,9 mlr (yalnızca MFN; Faz 0, Comext tabanı) ile ≈−$28,5 mlr (c2; BACI tabanı) arasında. Bunun ≈%40'ı yurt içi üretime, kalanı diğer kaynaklara kayar.
  - Doğrudan cari denge etkisi ≈ −$12 ile −$16 mlr: 2028 GSYH'sinin −0,6 ile −0,8 puanı. `[T]` Güven: Düşük.
- **Genel denge.** Lerner simetrisi ve reel kur tepkisi devreye girer:
  - TL'nin reel değer kaybı ihracat kaybını kısmen telafi eder, ama dezenflasyonu zorlar.
  - Tasarruf-yatırım dengesi değişmedikçe kalıcı cari denge etkisi sıfıra yakın olur (Furceri vd. 2019; temel ilke 5).
  - S4 cari denge hedefine katkı vermez. Hedef, Faz 1 §3.6'daki tamamlayıcı politikalara bağlı.

### 4.4 AB'nin maliyeti ve pazarlık gücü

| | Değer | Kaynak |
|---|---|---|
| AB–Türkiye mal ticareti, 2025 | €217,6 mlr; AB ihracatı €114,3 mlr, ithalatı €103,3 mlr (AB fazlası ≈€11 mlr) | `[V]` Komisyon |
| Türkiye'nin AB için sırası | 5. ticaret ortağı; hizmet ticareti €42,1 mlr (2024) | `[V]` |
| Otomotiv | Türkiye, AB yeni araç ihracatının 3. büyük pazarı: 811.957 araç, €18,8 mlr, değerin %11,1'i. Türkiye'nin AB'ye arzı 797.721 araç, €18,2 mlr; AB yeni araç ithalatının %21,5'i (230.833'ü ticari araç ve otobüs, €8,2 mlr). Türk pazarında AB üretimi araçların payı %49, Çin'in %8 | `[V]` ACEA, Temmuz 2026 |
| AB'nin anlaşmasızlık kaybı (σ = 5) | Yalnızca MFN (b) $16,4 mlr; c $18,7 mlr; c2 $28,5 mlr; a $31,1 mlr. Karşılaştırma: Türkiye'nin AB'ye ihracat kaybı €21,5 mlr | `[T]` §4.1 |
| Göreli yük | AB'de GSYH'nin ≈%0,1–0,2'si; Türkiye'de ≈%1,5'i | `[T]` |

**Okuma.**
- Kayıplar değer olarak benzer, ekonomilerin büyüklüğüne göre değil. Asimetri Türkiye aleyhine.
- Ama AB'nin kaybı otomotivde ve birkaç üye devlette yoğunlaşıyor. Almanya, İspanya, Fransa, Çekya, Slovakya ve Romanya Türkiye'ye en çok otomobil satan ülkeler.
- Renault, Stellantis, Ford, Toyota, Hyundai ve Mercedes'in Türkiye'deki fabrikaları AB pazarına üretiyor. AB tedarik zincirleri iki yönlü.
- AB'nin md. 207 kapsamındaki kararları nitelikli çoğunlukla alınıyor. Almanya ve İtalya'nın pozisyonu belirleyici; Yunanistan ve GKRY'nin nüfus payı ≈%2,5 (§6).
- Aktif S4, Türkiye'nin anlaşmasızlık maliyetini enflasyon tarafında düşürür. AB'nin otomotiv maliyetini ise artırır. **Bu, Türkiye'nin anlaşmasız alternatifini (BATNA) güçlendirir** ve Faz 7'deki müzakere stratejisinin temel kozlarından biridir.
- `[T]`/`[H]` Güven: Orta.

**AB'nin karşı araçları.** Hasmane AB varsayımında bunlar zaten kullanılıyor veya kullanılabilir:

| Araç | Tetikleyici | Türkiye için anlamı |
|---|---|---|
| Uygulama Tüzüğü 654/2014 (2021/167 ile değişik) | DTÖ kararı, temyizi engellenmiş panel raporu (md. 3(aa)), ikili anlaşmada işbirliği reddi (md. 3(ba)), XXVIII dengelemesi (md. 3(d)) | Tek taraflı GB değişikliğine karşı ana araç |
| Zorlamaya Karşı Araç (2023/2675) | AB veya üye devletin egemen tercihine yönelik ekonomik baskı | Yalnızca ticari baskı GKRY veya Yunanistan meselesine bağlanırsa |
| Çelik tüzüğü 2026/1384 (17.6.2026) | Küresel kapasite fazlası; md. 207(2); DTÖ korunma anlaşması dışında | 18,35 Mt kota; kota dışı %50 vergi; 1.10.2026'dan itibaren "eritildiği ve döküldüğü yer" kuralı. Türkiye'nin payı en büyük: ≈2,86 Mt. Çelik GB dışında olduğu için çıkıştan bağımsız olarak geçerli |
| Ticaret savunması | 2024–26'da Türkiye'ye karşı: sıcak haddelenmiş yassı çelik, seramik karo, balık (alabalık), dolanma önleme kararları; soğuk haddelenmiş çelik, kaynaklı çelik hasır ve tel halat soruşturmaları | Çıkıştan sonra artabilir |
| Onaylanmış kuruluşlar, SKDM, menşe kuralları | ACAA/MRA yokluğunda Türk sertifikalarının AB geçerliliği biter; SKDM karbon maliyeti | İhracatçının uyum maliyeti |
| Siyasi araçlar | SAFE savunma fonu (oybirliği; Yunanistan ve GKRY şartı), vize, göç ve enerji dosyaları | Hasmane AB varsayımında (V-11) zaten kullanılıyor |

*Kaynak:* `[V]` AB hukuku araştırma notu S12, S18, S20–S23; `[D?]` basında geçen Türk lastiğine anti-damping iddiası Resmî Gazete'de bulunamadı.

### 4.5 Sonuç: aktif tasarım Faz 1 teşhisini nasıl değiştiriyor?

| Kısıt | Pasif S4 (Faz 1) | Aktif S4 (c2 + P1 + geniş takas) | Değerlendirme |
|---|---|---|---|
| Enflasyon (≤30 bp/yıl, ≤50 bp kümülatif) | 59–98 bp: ihlal | 2,5–4,1 bp: **sağlanıyor** | Takas ve İGV tasarımı yeterli |
| Mali (≤ GSYH %0,5/yıl) | Gelir artışı | +%0,05 (tahsil edilebilir) | Sağlanıyor |
| İstihdam (T+3'te net sıfır) | −207 bin (brüt) | ≈ −105 ile −110 bin (net; takas dahil; P10–P90 ≈ −65 ile −155 bin) | **İhlal**; giyimde çekirdek kayıp |
| Kabiliyet | Otomotiv, giyim ve beyaz eşya ihracat platformlarında risk | İç pazarda koruma korunuyor; ihracat platformu riski değişmiyor | **İhlal riski** |
| Cari denge | İlk yıllarda −0,6 ile −0,8 puan | Değişmiyor | Tamamlayıcı politikalar şart |
| DTÖ uyumu | — | Uyumlu: MFN, bağlı oran içinde, menşeden bağımsız vergi; XXVIII:5 çekincesiyle esneklik | Sağlanıyor |

*Not:* Aktif S4'ün istihdam sütunu yaklaşıktır `[T]`. f2d'nin MFN hesabına takasın on gruptaki ek etkisi (+9 bin) eklendi. İGV'nin AB'ye de uygulanmasından gelen ek ithal ikamesi hesaplanmadı; bu, kaybı birkaç bin azaltabilir.

**Teşhisin yeni hali.**
- S4'ün enflasyon sorunu, Türkiye'nin kendi araçlarıyla çözülebilen bir tasarım sorunudur.
- S4'ün istihdam, kabiliyet ve ihracat sorunları ise Türkiye'nin kontrolü dışında. Belirleyici olan AB'nin tarifeleri ve menşe kurallarıdır.
- Bu yüzden S4 hâlâ bitiş durumu olamaz. Ama geri dönüş planı olarak çok daha az maliyetli ve müzakerede caydırıcı bir alternatif.

---

## 5. İhracat tarafı: Türkiye'nin elinde ne var, ne yok?

| Seçenek | Hukuki durum | Ekonomik etkinlik | Değerlendirme |
|---|---|---|---|
| İhracat sübvansiyonu (AB tarifesini telafi) | **Yasak** (ASCM 3.1(a)) | — | Kullanılamaz |
| Üretim sübvansiyonu (ihracata bağlı değil) | Dava edilebilir (ASCM 5–6); AB'de telafi edici vergiye açık | AB'nin S4'te alacağı ≈$6,1 mlr vergiyi telafi etmek için bütün üretime ödeme gerekir: yılda ≈$38 mlr (2028 GSYH'sinin %1,8'i). Otomotivde $2,2 mlr vergi için $5,6 mlr. AB bu desteği telafi edici vergiyle geri alır | Mali tavanın çok üstünde ve etkisiz. **Kullanılmamalı** |
| Kur | DTÖ'de sorun yok (2026'da ABD'nin telafi edici vergi soruşturmalarında "kur düşüklüğü" iddiası gündemde) | Dezenflasyonla çatışır | Kullanılmamalı |
| Pazar çeşitlendirmesi (STA ağı) | Uyumlu | Orta vadede. AB pazarının yerini 5 yılda alamaz: Türkiye'nin asimetrik pazarlara ihracatı $17,6 mlr, AB'ye $119,5 mlr | Gerekli ama yetersiz |
| Menşe ve uyum kolaylığı (S2/S3) | Anlaşmaya bağlı | En etkili: sıfır tarifeyi korur | **Ana yol** |
| Çapa yatırımcıyla tutma sözleşmesi | Uyumlu; performans koşulları ihracata bağlı sübvansiyon içermemeli | Kararı AB pazarına erişim belirler | Tamamlayıcı |
| Geçiş dönemi ve dondurma | Anlaşmaya bağlı (XXIV:5; Ortaklık Konseyi kararı) | Uçurumu önler | T2028 için şart |
| Eximbank kredileri ve DİR | OECD Uzlaşması içindeyse ve DİR normlara bağlıysa düşük risk | Finansman maliyetini düşürür, tarife farkını kapatmaz | Tamamlayıcı |

*Kaynak:* `[T]` tam telafi maliyeti = AB'nin ağırlıklı MFN'si × bölüm üretim değeri (YSHİ 2024), `veri/teshis_bolum_maruziyet.csv`. Güven: Orta.

**Sonuç.** İhracat tarafında AB'nin tarifesi iç politikayla telafi edilemez. Telafi girişimi ya yasaktır, ya mali tavanı aşar, ya da AB'nin telafi edici vergisiyle boşa çıkar. Bu yüzden çıkışın ihracat cephesi bir anlaşmaya bağlıdır: S2, S3 veya en azından geçiş anlaşması.

---

## 6. Dış rejim seçenekleri evreni

S0–S5 ana promptun senaryolarıdır. Aşağıda bunların yanında melez ve geçiş modelleri de var. Hukuki mekanik, şablonlar, menşe ve uyum değerlendirmesi, takvim ve sayısal karşılaştırma [`02b_secenekler_hukuk.md`](02b_secenekler_hukuk.md)'de.

| No | Model | İçerik | DTÖ dayanağı | AB tarafında hukuki yol ve oy kuralı | Hasmane AB'de gerçekçilik `[H]` | Not |
|---|---|---|---|---|---|---|
| R1 | Statüko GB (S0) | Mevcut 1/95 | XXIV:8(a) | — | — | Referans |
| R2 | Modernize GB (S1) | Hizmetler, kamu alımı, tarım, uyuşmazlık çözümü | XXIV | Konsey müzakere yönergesi hiç kabul edilmedi (Komisyon önerisi Aralık 2016) | Düşük | Karşı-olgu |
| R3 | Derin ve kapsamlı STA, DCFTA (S2) | Sanayide sıfır tarife, PEM menşei ve tam kümülasyon, ACAA, hizmetler, kamu alımı, karayolu ve vize | XXIV:8(b) | Md. 207 (nitelikli çoğunluk; hizmet ve fikrî mülkiyette md. 207(4) gereği oybirliği olabilir) veya md. 217 (oybirliği) | Orta–düşük | 2030 sonrası |
| R4 | Temel STA (S3) | Sıfır tarife, PEM menşei, ACAA yok | XXIV:8(b) | Md. 207 (nitelikli çoğunluk) + Avrupa Parlamentosu onayı | Orta | T2029 için en fazla bu |
| R5 | İsviçre modeli | 1972 tipi sanayi STA'sı + sektörel anlaşmalar (MRA, taşımacılık) | XXIV | Birden çok anlaşma; 2026 kurumsal paketi dinamik uyum ve AB Adalet Divanı rolü içeriyor | Düşük (zaman) | Parçalı ilerleme imkânı |
| R6 | Birleşik Krallık TCA modeli | Sıfır tarife ve kota; yalnızca ikili kümülasyon; eşit rekabet koşulları ve md. 411 yeniden dengeleme; 12 ay ihbarla fesih | XXIV | Md. 217 (oybirliği) | Orta | ≈10 aylık müzakere emsali; hazır yetki ve varoluşsal son tarih gerektirdi |
| R7 | **Geçici anlaşma ve dondurma** | GB tercihleri sabit bir tarihe kadar korunur (ör. 31.12.2029); STA'ya geçiş takvimi | XXIV:5(c); makul süre en fazla 10 yıl | Ortaklık Konseyi kararı (AB pozisyonu md. 207(4) + 218(9), nitelikli çoğunluk; C-81/13). Kurumsal çerçeveyi değiştiremez; GB'yi kaldıramaz, dondurabilir ve aşamalandırabilir | Orta (AB'nin otomotiv çıkarı var) | **T2028 için tek gerçekçi yol** |
| R8 | Geçici Ticaret Anlaşması (ITA) ayrımı | AB'nin tek başına yetkili olduğu bir md. 207 anlaşması GB hükümlerini "etkisiz kılar"; karma ortaklık anlaşması sonra gelir | XXIV:5–8 | AB–Şili ITA md. 33.11 ("Ortaklık Anlaşmasının IV. Kısmı ... etkisiz kalır"); Mercosur: Konsey Kararı 2026/183, nitelikli çoğunlukla. AB Adalet Divanı'nın 1/26 sayılı görüşü bekleniyor: ayrım tekniğini daraltabilir | Orta–düşük | T2029'un hukuki aracı |
| R9 | Asimetrik geçiş | AB sıfır, Türkiye AB mallarına kademeli tarife indirimi (veya tersi) | XXIV (asimetri kabul edilir) | Md. 207 | Düşük | Hasmane AB kabul etmez |
| R10 | Sektörel GB (ör. yalnızca otomotiv) | — | **XXIV'e aykırı**: "ticaretin esasının tamamı" şartı "ticaretin yalnızca bir kısmından çok daha fazlası" demek (Türkiye–Tekstil, DS34, para. 48) | — | Yok | Kullanılamaz |
| R11 | GB'de kalıp STA özerkliği | Ortak dış tarifesiz GB | GB tanımına aykırı | — | Yok | Kullanılamaz |
| R12 | EFTA üyeliği | EFTA Sözleşmesi md. 56 | — | AB pazarına erişim sağlamaz (AEA dışı) | Düşük fayda | Türkiye–EFTA STA'sı zaten var |
| R13 | **Aktif S4** | Anlaşmasız çıkış + tek taraflı paket (§4: c2 + P1 + geniş takas) | DTÖ | — | Yüksek olasılıklı geri dönüş planı | Enflasyon kısıtını çözer; ihracat ve istihdam kısıtlarını çözmez; BATNA'yı güçlendirir |
| R14 | S5 (gerilim) | S4 + AB ticaret savunmasında sertleşme, kritik girdi kısıtı, risk primi | DTÖ | Uygulama Tüzüğü, çelik tüzüğü, Zorlamaya Karşı Araç | Stres testi | |
| R15 | Tek taraflı fesih | Ankara Anlaşması ve 1/95'te fesih hükmü yok; teamül hukuku (Viyana Sözleşmesi md. 56 ve 62'nin karşılığı) feshi ancak niyet veya köklü değişiklik varsa kabul eder. Türkiye Viyana Sözleşmesi'ne taraf değil | — | AB, md. 58(2) koruma önlemleri, md. 64 yeniden dengeleme ve Uygulama Tüzüğü md. 3(ba) ile karşılık verebilir | Yüksek riskli | Hukuken açık; yalnızca son çare |
| R16 | Kademeli çıkış | Önce STA ağı ve tarife cetveli hazırlanır; GB'den çıkış anlaşmayla eş zamanlı | — | — | Yüksek (iç hazırlık) | Temel ilke 1 ve 10 |
| R17 | Çok taraflı açılım | ABD ile sektörel tarife anlaşması; Hindistan, Mercosur, Japonya STA'ları; KİK | XXIV | — | Orta | Çıkışla aynı anda başlar |

*Kaynak ve etiketler:*
- `[V]` Ankara Anlaşması (md. 23, 25, 31–33); 1/95 sayılı Karar (md. 13, 58, 61–64); ABİDA md. 207, 217, 218.
- C-81/13 İngiltere/Konsey; AB–Şili ITA (L_202402953); Konsey Kararı 2026/183; COM(2026) 477; DS34 Temyiz Organı raporu.
- `[H]` gerçekçilik yargısı. Güven: Orta.

**Kısa liste.** Faz 2B'de karşılaştırılacaklar:
- S0, S1, S2, S3;
- R7 (dondurma ve geçici anlaşma), R8 (ITA ayrımı);
- aktif S4 (R13) ve S5;
- bunların T2028 ve T2029 takvimlerine göre sıralanmış bileşimleri (ör. "R7 → S3 → S2").

---

## 7. Zaman kritik eylemler ("Pazartesi sabahı" listesi, Faz 2A)

| # | Eylem | Sorumlu | Hukuki araç | Son tarih | Neden şimdi |
|---|---|---|---|---|---|
| 1 | **GATT XXVIII:5 çekincesi**: 1.1.2027'de başlayan dönem için Cetvel XXXVII'yi değiştirme hakkının saklı tutulması | Dışişleri Bakanlığı (Cenevre Daimi Temsilciliği) ve Ticaret Bakanlığı | DTÖ Mal Ticareti Konseyi'ne nota | **31.12.2026** | Çıkış 2028 veya 2029'da; bağlı oranlarda esneklik ancak bu dönem için şimdi saklı tutulabilir. Bedeli: diğer üyelerin de Türkiye ile ilk müzakere ettikleri tavizleri değiştirebilmesi |
| 2 | DS629 kararına uyum planı: temyize gitmemek, elektrikli araç ek vergilerini bağlı oran (%20) içine çekmek, servis ağı şartını düzeltmek | Ticaret Bakanlığı, Dışişleri | DSB toplantısı; Cumhurbaşkanı kararı | **27.10.2026** (DSB) | Türkiye MPIA'da değil; boşluğa temyiz Türkiye'nin kural temelli aktör itibarını zayıflatır. GB sonrası Türkiye AB'ye karşı DTÖ kurallarına dayanacak |
| 3 | Mevcut DTÖ risklerinin temizlenmesi (§1.8): engelli ÖTV istisnasındaki %40 yerli katkı şartı, kurumlar vergisi md. 32/7, rakı farkı, 160 kW eşiğinin gerekçesi; hurda teşviki tasarısından menşe şartının çıkarılması | HMB, Ticaret Bakanlığı | Kanun değişikliği (md. 7/2, md. 32/7); Cumhurbaşkanı kararı (ÖTV III ve II listeleri) | 2027 bütçe kanunu dönemi (Aralık 2026) | Çıkıştan sonra AB'nin ilk hedefleri; GB içinde dava edilmeden temizlenmesi ucuz |
| 4 | Takasın hukuki taslakları: ÖTV (II) ve (IV) listelerinde oran değişiklikleri; KDV (II) listesinde değişiklik; ÖTV dilim eşiklerinin gümrük vergisinden arındırılması | HMB, GİB | Cumhurbaşkanı kararı taslakları (4760 md. 12; 3065 md. 28) | T−6 ay | Çıkış günü yürürlüğe girecek kalıcı oranlar; geçici indirim uçurumundan kaçınmak |
| 5 | Takas kalibrasyon verisi: ÖTV (II) tahsilatının menşeye (yerli/ithal) ve matrah dilimine göre dağılımı; gümrük vergisinin rejime göre (DİR, teşvik, GSP) ve İGV'nin ayrı raporlanması | GİB, Ticaret Bakanlığı (Gümrükler) | İdari veri talebi | 3 ay | Takas maliyetinin ve tahsilat oranının belirsizliği (§1.5, §3.4) |
| 6 | Rejim c2 satır listesi: AB'nin baskın, yurt içi kabiliyetin zayıf olduğu satırlar (PRODTR + BACI); sektör istişaresi | Ticaret ve Sanayi ve Teknoloji Bakanlıkları | Faz 5 tarife cetveli | T−12 ay | İGV rejimi, paketin en büyük tek kararı |
| 7 | AB ile yürüyen teknik süreçleri kullanmak: A.TR kurallarının PEM ile uyumu (COM(2026) 477, 1.1.2026'dan geriye dönük); 13.10.2026 Üst Düzey Ticaret Diyaloğu'nun açık maddeleri (deri, tekstil, alkol, kozmetik ürün bildirimi, ilaç seri serbest bırakma) | Ticaret Bakanlığı, Dışişleri | Gümrük Birliği Ortak Komitesi | Sürekli | Hasmane ortamda bile işleyen teknik kanallar; çıkış sonrası menşe ve uyum altyapısının temeli |

---

## 8. Faz 2B'ye girdiler

1. Kısa listedeki rejimlerin (S0–S3, R7, R8, aktif S4, S5) sayısal karşılaştırması. Eklenecek bileşenler:
   - çekim modeli (PPML) ile GB ve STA etkileri (`kod/f2f_cekim_modeli.py`);
   - menşe uyum maliyeti ve tercih kullanım oranları (Faz 0 ve Faz 1);
   - bu belgedeki TÜFE, mali ve istihdam sonuçları.
2. T2028 ve T2029 takvimleri için önerilen son durum ve geçiş sırası.
3. Hukuki yol haritası:
   - AB tarafı: Ortaklık Konseyi kararı, md. 207 ITA, md. 218 süreçleri ve Mercosur ile Şili emsalleri;
   - DTÖ: XXIV:7(a) bildirimi, şeffaflık mekanizması, XXVIII;
   - Türk iç hukuku: Anayasa md. 90; ÖTV, KDV ve gümrük tarife araçları.
4. Kısıt testleri (temel ilke 9): her seçenek için enflasyon, cari denge, mali, istihdam, kabiliyet ve DTÖ.

---

## 9. Veri boşlukları (Faz 2A)

| No | Boşluk | Etki | Kapatma yolu |
|---|---|---|---|
| VB-10 | DTÖ bağlı oranlarının HS2022 satır listesi (cetvel dosyaları sanayi satırlarının %29'unu kapsıyor) | Bağlı oran boşluğu (§3.1) | WTO TTD veya API anahtarı; DS629 panel raporu eki (otomobil) |
| VB-21 | ÖTV (II) tahsilatının yerli/ithal ve dilim dağılımı | Takasın maliyeti ve etkin ÖTV oranı (%58–66, merkez %65) | GİB idari verisi |
| VB-22 | İGV'nin gümrük vergileri kalemindeki payı; gümrük vergisinin rejime göre dağılımı | Tahsilat oranı (§3.4) | Ticaret Bakanlığı, GİB |
| VB-23 | Beyaz eşya ve TV'de ürün düzeyinde iç satış ve ithalat payı (TÜRKBESD ve Ticaret Bakanlığı sitelerine erişilemedi) | Yerli pay (PRODTR'den hesaplandı) | TÜRKBESD; Ticaret Bakanlığı sektör raporu |
| VB-24 | Giyim ve ayakkabıda kayıt dışı ve fason üretimin iç pazar payı | Yerli pay (I-O ve YSHİ'den) | TÜİK, sektör dernekleri |
| VB-25 | Otomobil ÖTV matrahına gümrük vergisinin dahil olup olmadığı (4760 md. 11/3 → KDV matrahı) | Dilim sıçraması (§1.7.3) | GİB özelgesi; mevzuat |
| VB-26 | DS629'un 27.10.2026 DSB kararı | §7 eylem 2 | DSB toplantısı |
| VB-27 | ABD telafi edici vergi soruşturmalarında Türk programları hakkındaki son kararlar (arazi, YEKDEM, bölgesel teşvik, imalatçı vergi indirimi, kur) | D2 riskinin büyüklüğü | ABD Ticaret Bakanlığı karar memorandumları |

Faz 1'den süren boşluklar [`01_teshis.md`](01_teshis.md) §8'de.

---

## 10. Faz 2A kalite kontrol listesi

| Kontrol | Durum |
|---|---|
| Kullanıcının önerisi (tarife + yerli ürüne ÖTV indirimi) hukuken, ekonomik olarak ve sayısal olarak incelendi; hukuka uygun eşdeğerleri karşılaştırıldı | ✓ §1 |
| Araç evreni A–K; her araç için hukuki sınır, yön ve uygulayıcı | ✓ §2 |
| Her sayının etiketi `[V]`/`[T]`/`[D?]`/`[H]`, güven düzeyi, birimi ve dönemi var | ✓ |
| `[T]` tahminleri P10–P50–P90 aralığıyla | ✓ σ, η, ρ ızgarası; ρ aralığı |
| Olumsuz bulgular açıkça yazıldı ve değiştirecek koşullar belirtildi | ✓ T-0 yasadışı ve pahalı; P1 küçük; istihdam kısıtı aktif S4'te de ihlal; ihracat tarafında tek taraflı çözüm yok |
| DTÖ uyumu (temel ilke 8, DS583 dersi) her araçta kontrol edildi | ✓ §1.2, §1.8, §2 |
| Enflasyon kısıtı: birinci tur ≤30 bp/yıl, ≤50 bp kümülatif | ✓ Aktif S4'ün dört paketi sağlıyor |
| Mali kısıt (≤ GSYH %0,5/yıl): yasal ve tahsil edilebilir gelirle | ✓ §3.4, §4.1 |
| İstihdam kısıtı ve %5 tetikleyicisi | ✓ §4.2: 22 sınıf (σ = 5); kısıt ihlal |
| Eylemler Pazartesi sabahı testinden geçiyor (kurum, araç, son tarih) | ✓ §7 |
| İki takvim (T2028, T2029) | Kısmen: §6; ayrıntı Faz 2B |
| Kod ve veri yeniden üretilebilir | ✓ `kod/f2*.py`, `veri/politika_*.csv`, `veri/vergi_*.csv` |

---

## Kaynaklar (Faz 2A)

**Hukuk metinleri ve DTÖ**
- GATT 1994, ASCM, TRIMs, Korunma Anlaşması, 1994 Ödemeler Dengesi Mutabakatı, XXIV Mutabakatı; WTO Analytical Index (GATT md. II, III, XII, XVIII, XIX, XXI, XXIV, XXVIII; ASCM md. 1–3 ve Ek I; TRIMs md. 2): https://www.wto.org/english/res_e/publications_e/ai17_e/
- Uyuşmazlıklar: DS8/10/11, DS31, DS34, DS54/55/59/64, DS87/110, DS90, DS155, DS302, DS308, DS334, DS339, DS371, DS396/403, DS412/426, DS438, DS462/463, DS472/497, DS512, DS544, DS583, DS592, DS600, DS623, DS629 (WT/DS629/R, 28.7.2026), DS642, DS644: https://www.wto.org/english/tratop_e/dispu_e/
- DSB, 25.9.2026: https://www.wto.org/english/news_e/news26_e/dsb_25sep26_496_e.htm; MPIA: https://www.wto.org/english/tratop_e/dispu_e/mpia_e.htm; GPA gözlemcileri; Türkiye tarife profili: https://www.wto.org/english/res_e/statis_e/daily_update_e/tariff_profiles/TR_E.pdf

**AB hukuku**
- Ankara Anlaşması: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:21964A1229(01)
- 1/95 sayılı Karar: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:21996D0213(01)
- COM(2026) 477: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026PC0477
- C-81/13: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62013CJ0081
- AB–Şili ITA ve Konsey Kararı 2023/2761: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202402953
- Konsey Kararı 2026/183 (Mercosur): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202600183
- TCA: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:22021A0430(01)
- Uygulama Tüzüğü 654/2014 (konsolide): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014R0654-20210213
- Zorlamaya Karşı Araç 2023/2675: https://eur-lex.europa.eu/eli/reg/2023/2675/oj
- Çelik uygulama tüzüğü 2026/1457: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R1457
- Revize PEM: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202400390
- Türkiye 2025 Raporu, SWD(2025) 756; ACEA, AB–Türkiye araç ticareti, Temmuz 2026: https://www.acea.auto/files/ACEA_fact_sheet_EU_Turkiye_vehicle_trade-July_2026.pdf
- AB engeller veri tabanı (Access2Markets), Türkiye kayıtları, 18.10.2026.

**Türk mevzuatı ve vergi verisi**
- 4760 sayılı ÖTV Kanunu (konsolide), 3065 sayılı KDV Kanunu, 5520 sayılı Kurumlar Vergisi Kanunu, 4734 sayılı Kamu İhale Kanunu: https://www.mevzuat.gov.tr
- CK 10115 (RG 24.7.2025): https://www.resmigazete.gov.tr/eskiler/2025/07/20250724-5.pdf
- 7590 sayılı Kanun (RG 31.7.2026): https://www.resmigazete.gov.tr/eskiler/2026/07/20260731-2.htm
- 7417 ve 7521 sayılı Kanunlar; CK 287 (RG 31.10.2018 mük.).
- GİB ÖTV (II), (III), (IV) listeleri (31.7.2026, 3.7.2026, 24.10.2025); GİB KDV oranları; GİB Tablo 28 (gelir tahsilatı): https://cdn.gib.gov.tr/
- SBB, 2026 yılı gelir tahminleri.
- ODMD Aralık 2025 bülteni; OSD 19.1.2026 basın bülteni: https://www.osd.org.tr/haberler/231
- UN Comtrade (Türkiye beyanı, 2025); Eurostat prc_hicp_iw (Türkiye, COICOP 2018 ağırlıkları).

**İstatistik**
- TÜİK 2023 girdi-çıktı tabloları; TÜİK PRODTR 2025 (bülten 58065); TÜİK YSHİ 2024; TÜİK 2026 TÜFE ağırlıkları.
- CEPII BACI 2024 (HS 2017); 2026 İthalat Rejimi Kararı ve İGV kararları; WITS HS2017–BEC Rev. 4 eşleştirmesi.
- OVP 2027–2029.

**Emsaller ve geçişkenlik**
- Amiti, Redding ve Weinstein (2019), *Journal of Economic Perspectives*; Fajgelbaum vd. (2020), *QJE*; Cavallo vd. (2021), *AER: Insights*.
- Furceri, Hannan, Ostry ve Rose (2019), NBER 25402; Barattieri, Cacciatore ve Ghironi (2021), *JIE*; Lindé ve Pescatori (2019), Riksbank WP 363.
- TCMB WP 21/13 (2020 İGV'leri); TCMB Enflasyon Raporları 2009-II, 2017-II, 2019-I, 2019-III; TCMB Kasım 2018 fiyat gelişmeleri.
- SECO (2026), sanayi tarifelerinin kaldırılmasının tüketici fiyatlarına etkisi, WP 65.
- UKTPO (2019, 2020) Birleşik Krallık tarife analizleri; Breinlich vd. (2022), *IER*; Bakker vd., CEP DP1888.
- USTR Rusya DTÖ uyum raporları (2015, 2022, 2025); ICCT MOVER notu (2025).
