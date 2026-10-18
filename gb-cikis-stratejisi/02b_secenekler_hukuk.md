# Faz 2B — Seçenekler, bitiş durumu ve hukuki yol haritası

**Durum:** Faz 2 / 9 tamamlandı (18 Ekim 2026); DEVAM bekleniyor. Birinci kısım: [`02a_politika_uzayi.md`](02a_politika_uzayi.md). Önceki faz: [`01_teshis.md`](01_teshis.md). Defter: [`defter.md`](defter.md).

**Bu belge ne yapıyor?** Faz 2A, Türkiye'nin kendi araçlarının sınırlarını çizdi. Bu belge dört şey yapıyor:
- dış rejim seçeneklerini sayısal olarak karşılaştırıyor (§1–§3);
- iki takvim için bitiş durumunu ve geçiş sırasını öneriyor (§4);
- AB, DTÖ ve Türk iç hukuku açısından adım adım yol haritasını çiziyor (§5);
- olasılıkları, kapıları ve riskleri güncelliyor (§6–§7).

Kanıt etiketleri ve güven düzeyleri 02a'daki gibi.

**Veri ve kod.**

| Betik | İçerik | Ana kaynak |
|---|---|---|
| `kod/f2f_cekim_modeli.py` | Yapısal çekim modeli (PPML): GB'nin ve AB STA'larının (derin, temel) ticaret etkisi; S2, S3 ve S4 senaryoları; genel denge modülü | CEPII Gravity V202211, BACI 2024, DESTA v2.3, UN AMA |
| `kod/f2e_s4_aktif.py` | Aktif S4 paketleri ve S3'te menşe maliyetinin TÜFE etkisi | 02a |
| `kod/f2c_vergi_takasi.py`, `kod/f2d_s4_net_istihdam.py` | Vergi takası; net istihdam | 02a |

Hukuki bulgular Faz 2'nin AB hukuku ve DTÖ hukuku araştırma notlarından alındı. `[V]` etiketli olanlar birincil metinden okundu: Ankara Anlaşması, Katma Protokol, 1/95, ABİDA md. 207/217/218, Mercosur, Şili ve Meksika kararları, TCA, revize PEM, NANDO, DTÖ Analitik Endeksi.

---
## Faz 2B'nin 10 ana bulgusu

1. **Anlaşmasız çıkışın (S4) ticaret kaybı sağlam ve büyük.**
   - Türkiye'nin AB'ye ihracatı −%19 (GE; %90 GA −%32 ile −%5). Kısmi denge −%22; Faz 0 tarife duvarı hesabı −%15 ile −%33.
   - Toplam ihracat −%6,2; reel GSYH −%0,43 (GA −%0,73 ile −%0,10).
   - Bu bir alt sınır, çünkü 1971'den beri süren sanayi tercihleri modelde ikili sabit etkiye düşüyor.
   - `[T]` Güven: Orta.
2. **Derin STA'nın (S2) maliyeti belirsiz ve muhtemelen küçük.**
   - Merkez tahmin: AB'ye ihracatta −%11, GSYH'de −%0,22. İkisinin de GA'sı sıfırı içeriyor.
   - Dünya Bankası (2014): −%3 ile −%7.
   - `[T]` Güven: Düşük–Orta.
3. **Temel STA'nın (S3) sonucu tasarıma bağlı.**
   - Aralık −%18 ile +%1.
   - Türkiye–BK STA'sı (2021) sıfır tarifeyi ve AB girdisiyle kümülasyonu korudu. GB'den STA'ya geçişte ticaret kaybı istatistiksel olarak sıfır çıktı.
   - Ders: menşe protokolü müzakerenin en kritik başlığıdır.
   - `[T]` Güven: Düşük–Orta.
4. **Hiçbir çıkış seçeneği bütün kısıtları kendiliğinden sağlamıyor.**
   - TÜFE ve mali kısıtlar her seçenekte tasarımla karşılanabiliyor.
   - İstihdam kısıtı S2'de bile risk altında: ≈ −33 bin, GA sıfırı içeriyor. Sınıf düzeyinde uyum ve destek paketi (Faz 3–5) her seçenekte gerekli.
   - `[T]` Güven: Düşük–Orta.
5. **Önerilen bitiş durumu S2 (DCFTA), 2030–2031.**
   - İçerik: sanayide sıfır tarife, PEM ve tam kümülasyon, öncelikli sektörlerde ACAA, hizmetler, kamu alımı, karayolu, eşit rekabet koşulları; Türkiye'nin tarife özerkliği ve kendi STA ağı.
   - Ara durum S3 (md. 207 ITA). Geçiş R7 (dondurma). Geri dönüş planı aktif S4.
   - `[H]` Güven: Orta.
6. **İki takvim.**
   - **T2029:** ITA 1.1.2029'da geçici uygulamada. Bunun için AB müzakere yetkisinin Eylül 2027'ye kadar verilmesi gerekiyor.
   - **T2028:** yalnızca çıkış kararı ve dondurma (geçiş dönemi); ITA 2029–2030'da.
   - Ortaklık Konseyi kararı GB'yi kaldıramaz. GB'nin hukuken sona ermesi ITA'nın "GB hükümleri etkisiz kalır" maddesiyle olur (AB–Şili md. 33.11 emsali).
   - Öneri: ekonomik ve hukuki çıkış T2029; T2028 gerekiyorsa çıkış kararı ve geçiş başlangıcı.
   - `[V]`/`[H]` Güven: Orta.
7. **AB tarafında yol var: nitelikli çoğunluk.**
   - Dondurma kararında AB pozisyonu (md. 218(9) + 207(4); C-81/13), ITA yetkisi ve imzası nitelikli çoğunlukla alınıyor. Bu, Faz 0'daki oybirliği varsayımının düzeltmesi.
   - Yunanistan ve GKRY'nin hukuki vetosu yok; siyasi vetoları var.
   - Belirleyici başkentler Berlin ve Roma. Mercosur'da beş üye devletin karşı oyuna rağmen karar çıktı.
   - Risk: Divan'ın Görüş 1/26'sı ITA ayrımını daraltabilir.
   - `[V]` Güven: Orta–Yüksek.
8. **Onaylanmış kuruluş uçurumu gerçek.**
   - NANDO'da 95 Türk kaydı var; ≈81'i yürürlükte.
   - Süreklilik hükmü olmadan Türk sertifikaları çıkış günü AB'de geçersiz olur (İngiltere 2020, İsviçre 2021 dersleri).
   - Dondurma kararına ve ITA'ya "büyükbaba" hükmü konmalı.
   - `[V]` Güven: Yüksek.
9. **Olasılıklar güncellendi (hasmane AB, kapılar işletilmeden).**
   - T2028'de anlaşmasız çıkış %55–68; T2029'da %30–50.
   - Kapılar işletilirse bu olasılığın çoğu erteleme anlamına gelir; çıkış yönü değişmez, tarih değişir.
   - `[H]` Güven: Düşük.
10. **En büyük risk tarife değil, kur.**
    - %10'luk bir değer kaybı TÜFE'ye ≈+250 bp ekler; bu, aktif S4'ün tarife kanalının 30–80 katı.
    - Çıkışın kurallı, önceden ilan edilmiş ve anlaşmaya dayalı olması tarife tasarımından daha önemli.
    - Makro çerçeve Faz 6'da.
    - `[V]`/`[H]` Güven: Orta.

---

## 1. Seçeneklerin tanımı

| Seçenek | TR → AB tarife | AB → TR tarife | Türkiye'nin üçüncü ülkelere tarifesi ve STA'ları | Menşe | Uyum değerlendirmesi | Hizmet, kamu alımı, hareketlilik | Eşit rekabet koşulları ve uyuşmazlık | AB'de hukuki yol | Müzakere süresi (emsal) |
|---|---|---|---|---|---|---|---|---|---|
| **S0** Statüko GB | 0 (sanayi, İTÜ) | 0 | OGT'ye bağlı; paralel STA | Gerekmiyor (A.TR) | 1/95 md. 8–10; Türk onaylanmış kuruluşları geçerli | GB dışında | Ortaklık Konseyi; zayıf | — | — |
| **S1** Modernize GB | 0; tarım ve hizmetler genişler | 0 | OGT; Türkiye'nin STA sürecine katılımı ("Türkiye maddesi") | A.TR | Aynı | Hizmet ve kamu alımı açılır | Güçlü uyuşmazlık çözümü | Ortaklık Konseyi kararı + karma anlaşma; Konsey yetkisi 10 yıldır yok | 3–5 yıl |
| **S2** DCFTA | 0 (menşe şartıyla) | 0 (menşe şartıyla) | **Özerk**; kendi STA ağı | Revize PEM; tam kümülasyon | ACAA veya MRA | Hizmet, kamu alımı, karayolu ve vize faslı | Sübvansiyon denetimi, yeniden dengeleme, tahkim | Md. 207 veya 217 | 3–6 yıl; 2030 sonrası |
| **S3** Temel STA (md. 207 ITA) | 0 (menşe şartıyla) | 0 (menşe şartıyla) | Özerk | Revize PEM ve çapraz kümülasyon | ACAA yok; **onaylanmış kuruluş geçiş hükmü şart** | Sınırlı | Hafif; tahkim | Md. 207 (nitelikli çoğunluk) + AP onayı; geçici uygulama mümkün | ≈12 ay (TCA 10 ay) |
| **R7** Dondurma (geçici anlaşma) | 0 | 0 | OGT dondurma süresince sürer | A.TR | Statü sürer | — | Ortaklık Konseyi | Ortaklık Konseyi kararı; AB pozisyonu md. 218(9), nitelikli çoğunluk | 6–9 ay |
| **S4-aktif** Anlaşmasız çıkış + tek taraflı paket | AB MFN (%5,85; €5,5 mlr) | MFN; İGV rejimi c2; girdide sıfır; vergi takası | Özerk | Gerekmiyor (MFN) | Türk sertifikaları AB'de geçersiz | — | DTÖ | — | — |
| **S5** Gerilim | AB MFN + ticaret savunmasında sertleşme | Aynı | Özerk | — | Geçersiz | — | AB karşı önlemleri | — | — |

*Not:* S3'ün hukuki aracı R8'dir: AB'nin tek başına yetkili olduğu md. 207 Geçici Ticaret Anlaşması. Bu anlaşma GB hükümlerini "etkisiz kılar" (§5.1). S2, S3'ün üzerine kurulan karma bir anlaşma olarak sonra gelebilir.

---

## 2. Karşılaştırma matrisi

### 2.1 Ticaret etkisi: çekim modeli

**Yöntem** (`kod/f2f_cekim_modeli.py`):
- Model: yapısal çekim modeli, PPML (Yotov vd. 2016).
- Sabit etkiler: ihracatçı-yıl, ithalatçı-yıl ve yönlü ikili.
- Örnek: CEPII Gravity, 1988–2020, 4 yıllık aralık, ilk 150 ekonomi; 2024'e BACI ile uzatma.
- Kuklalar:
  - GB'nin iki yönü: Türkiye → AB ve AB → Türkiye;
  - AB'nin derin STA'ları (Kore, CETA, Japonya, Vietnam, DCFTA'lar);
  - AB'nin temel STA'ları (Avrupa-Akdeniz anlaşmaları, Meksika 2000, Şili 2003);
  - kontroller.
- Senaryo etkisi: S0'a göre % değişim = exp(β_senaryo − β_GB) − 1; S4'te β = 0.
- Kısmi denge: çok taraflı direnç terimleri sabit. Genel denge modülü ayrıca raporlandı.

**Tablo 2.1 — Ana katsayılar (M1, PPML; parantez içinde küme-sağlam standart hata)**

| Değişken | Katsayı | Yüzde etki | Sağlamlık aralığı (19 spesifikasyon) |
|---|---|---|---|
| GB: Türkiye → AB | +0,246 (0,130) | +%28 | +0,04 ile +0,36. 1996 öncesi ortaklık rejimine göre artış: AB sanayide 1971'den beri Türk mallarına tarife uygulamıyordu |
| GB: AB → Türkiye | +0,142 (0,120) | +%15 | −0,08 ile +0,44 |
| AB'nin derin STA'ları | +0,100 (0,039) | +%11 | +0,01 ile +0,13; 2020'ye ve uzaklık × yıl kontrolüne duyarlı |
| AB'nin temel STA'ları | −0,167 (0,056) | −%15 | −0,21 ile −0,07. **Kullanılamaz:** anlaşma öncesinde anlamlı bir eğilim var (4 yıl önceki öncül katsayı −0,19, p < 0,01). Avrupa-Akdeniz ortaklarının anlaşmadan önce de tercihli erişimi vardı. Bu yüzden S3 için Türkiye'nin kendi GB ↔ STA geçişleri kullanıldı |

**Tablo 2.1b — Senaryolar: S0'a (GB) göre Türkiye'nin AB'ye ihracatı ve diğer göstergeler**

| | Kısmi denge (M1; %90 GA) | Genel denge (σ = 7; %90 GA) | Türkiye toplam ihracatı (GE) | Türkiye reel GSYH, refah vekili (GE) | AB reel GSYH (GE) |
|---|---|---|---|---|---|
| **S2** DCFTA | −%13,6 (−30,5 ile +7,4) | −%11,1 (−26,7 ile +6,1) | −%3,3 (−8,3 ile +2,1) | −%0,22 (−0,56 ile +0,19) | −%0,01 |
| **S3, ihtiyatlı** (Türkiye'nin aday ülkelerle STA'sından GB'ye geçiş, 2004/2007/2013) | −%22,0 (−35,1 ile −6,4) | −%18,2 (−31,1 ile −3,4) | −%5,3 (−10,6 ile +1,3) | −%0,35 (−0,75 ile +0,15) | −%0,02 |
| **S3, iyimser** (Türkiye–BK'nin GB'den STA'ya geçişi, 2021) | +%0,3 (−9,2 ile +10,9) | +%1,4 (−6,7 ile +10,5) | +%1,1 (−1,7 ile +4,5) | +%0,10 (−0,11 ile +0,35) | 0 |
| **S4** | −%21,8 (−36,9 ile −3,2) | −%18,9 (−32,4 ile −4,6) | −%6,2 (−10,6 ile −1,5) | −%0,43 (−0,73 ile −0,10); σ = 5'te −%0,63 | −%0,03 |
| Karşılaştırma: Faz 0 tarife duvarı (S4, kısmi denge, σ = 3 / 5 / 8) | −%15 / −%23 / −%33 | | | | |
| Karşılaştırma: Dünya Bankası (2014), GB yerine menşe kurallı STA | −%3,0 ile −%7,2 | | | | |

*Kaynak ve etiketler:*
- `[T]` `veri/politika_cekim_katsayilar.csv`, `veri/politika_cekim_senaryolar.csv`.
- Örnek: 150 ekonomi; 1988–2020, 4 yıllık aralık. N = 185.003, 21.480 çift.
- Tahminde ülke içi ticaret yok (USITC ITPD-E erişilemedi). Etkiler üçüncü ülkelerle ticarete göredir; yaratma ve saptırmayı birlikte içerir.
- GE: 2019 kesiti; ülke içi satışlar UN AMA katma değerinden türetildi; kesin şapka cebiri; %90 GA 1.000 çekilişli parametrik bootstrap.
- **Etkinin zaman yolu (M2).** GB etkisi hemen ortaya çıkıyor, sonra sönümleniyor:
  - Türkiye → AB: 0–3 yılda +%44, 4–7 yılda +%25, 8–11 yılda +%34, 12+ yılda +%21 (anlamsız).
  - AB → Türkiye: +%55, +%40, +%16, −%3.

  Derin STA etkisi ilk 8 yılda ≈+%9.
- **Kırılganlık.** Derin STA katsayısı 2020'ye (2020 hariç 0,012; BACI 2024 uzatmasıyla yine 0,099) ve uzaklık × yıl kontrolüne (0,014) duyarlı.
  - Yalnızca DCFTA'lar alındığında (M6; Rusya ile ticaret kırılması kontrol edilerek) S2: Türkiye → AB −%9,8 (−31 ile +18).
  - GB katsayısı veri kaynağına ve aralığa duyarlı: 5 yıllık aralıkta 1995 taban yılı zaten "tedavi edilmiş", çünkü Türkiye 1993–95'te tarifelerini önceden indirdi.
- **Literatürle uyum.** Aytuğ vd. (2017) +%38 buluyor; bizim ilk on yıl tahminimiz +%34–44. Dünya Bankası (2014) ikili etkiyi anlamsız buluyor; bu, AB → Türkiye sonucumuzla ve 5 yıllık ve BACI varyantlarıyla uyumlu. Dursun (2023) sönümlenmeyi buluyor; bizde de var.
- Güven: Orta (S4), Düşük–Orta (S2, S3).

**Okuma.**
1. **S4'ün ticaret kaybı sağlam.**
   - Kısmi denge, genel denge ve tarife duvarı hesabı aynı bölgeye düşüyor: Türkiye'nin AB'ye ihracatında −%19 ile −%23.
   - Bu bir alt sınır, çünkü 1971'den beri süren tercihler ve Türkiye'nin 1993–95 tarife indirimleri ikili sabit etkide kalıyor.
   - Reel GSYH kaybının GA'sı sıfırı dışlıyor.
   - AB → Türkiye için tarife duvarı çapraz kontrolü: İGV hariç −%12 ile −%27, İGV dahil −%22 ile −%42.
2. **S2'nin kaybı belirsiz.** Merkez tahmin −%11, ama GA sıfırı içeriyor.
   - GB katsayısı muhtemelen 1996'da kalkan tekstil kotalarının etkisini de içeriyor `[H]`. Bir STA bu kotaları geri getirmez; bu yüzden S2'nin kaybı muhtemelen merkez tahminden küçük.
   - GB etkisi zamanla sönümleniyor. Uzun vadede (12+ yıl, M2) S2'nin S0'a göre etkisi ≈0 (+%0,1; GA −28 ile +40).
   - Dünya Bankası'nın −%3 ile −%7 aralığı bu okumayla uyumlu.
3. **S3'ün sonucu tasarıma bağlı.**
   - İhtiyatlı tahmin S4'e yakın: −%18. Bu tahmin AB katılımının kendi etkisiyle karışıyor; kayıp için üst sınır.
   - İyimser tahmin sıfır. Türkiye–BK STA'sı (2021) sıfır tarifeyi korudu ve menşede AB girdisiyle kümülasyona izin verdi. GB'den STA'ya geçişte ticaret kaybı istatistiksel olarak sıfır çıktı. Yalnızca tek çift ve üç yıl var.
   - Ders: **menşe tasarımı (PEM, çapraz kümülasyon, tolerans) S3'ü S0'a yaklaştırır; kötü tasarım S4'e yaklaştırır.**
4. **AB'nin kaybı her senaryoda küçük ama gerçek:** AB GSYH'sinin %0,01–0,03'ü. AB'nin Türkiye'ye ihracatı S4'te −%14 (GE). Kayıp otomotivde yoğunlaşıyor (02a §4.4).

### 2.2 Bütün göstergeler

**Tablo 2.2 — Seçeneklerin S0'a göre yerleşmiş yıllık etkileri**

| Seçenek | TR → AB ihracat (GE, σ = 7) | Türkiye toplam ihracatı | Reel GSYH (refah vekili) | İhracatçının AB'de vergi ve menşe maliyeti (€ mlr/yıl) | TÜFE birinci tur (bp) | Net mali (GSYH %, tahsil edilebilir) | Net imalat istihdamı (bin) | Cari denge, ilk yıl (GSYH puanı) |
|---|---|---|---|---|---|---|---|---|
| **S0** Statüko | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **S1** Modernize GB | Ölçülmedi (+; hizmet ve kamu alımı) | + | + | 0 | 0 | 0 | + | ≈0 |
| **S2** DCFTA | −%11 (−27 ile +6); Dünya Bankası −%3 ile −%7 | −%3,3 | −%0,22 (−0,56 ile +0,19) | 2,4–6,7 (menşe uyumu ve kullanılmayan tercih; Faz 1) | +2 ile +12 (menşe maliyeti %1–3; P1 dahil) | ≈0 | ≈ −33 (GA sıfırı içeriyor) | −0,1 ile −0,3 `[H]` |
| **S3** ITA | −%18 ile +%1 (tasarıma göre) | −%5,3 ile +%1,1 | −%0,35 ile +%0,10 | 2,4–6,7 + uyum değerlendirmesi 0,1–0,3 `[H]` | +2 ile +12 | ≈0 | −54 ile +12 | −0,1 ile −0,5 `[H]` |
| **R7** Dondurma | 0 (süresince) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **S4-aktif** | −%19 (−32 ile −5); kısmi denge −%15 ile −%33 | −%6,2 | −%0,43 (−0,73 ile −0,10) | 5,5 (vergi) | 2,5–4,1 (c2 + P1 + geniş takas) | +0,05 | ≈ −35 (c2 + takas, sınıf düzeyi; ≈ −11 ile −72) | −0,6 ile −0,8 |
| **S5** Gerilim | S4'ten kötü (ticaret savunması) | S4'ten kötü | S4'ten kötü | 5,5 + ticaret savunması | S4 + kur şoku (%10 değer kaybı ≈ +250) | Negatif (faiz) | S4'ten kötü | S4'ten kötü |

*Kaynak ve etiketler:*
- `[T]` Ticaret ve GSYH: §2.1 (GE, σ = 7). TÜFE, mali ve S4 istihdamı: 02a ve `veri/politika_s4_aktif.csv` (S3 satırları: `s3_sta_mense_*`).
- S2 ve S3 istihdamı kaba bir hesap: GE'deki toplam ihracat ve ithalat değişimi × istihdam yoğunluğu. İhracat tarafında 7,9 bin kişi/$ mlr; ithal ikamesinde 0,58 × 5,8 bin kişi/$ mlr (f2d'nin ortalamaları). S4-aktif ise f2d'nin sınıf düzeyi kısmi denge hesabı.
- Aynı GE kanalıyla pasif S4 (yalnızca MFN) ≈ −63 bin; aktif S4'ün daha az kaybı, AB mallarına uygulanan İGV'nin yarattığı ithal ikamesinden geliyor.
- Cari denge: S4 Faz 1 hesabı; S2 ve S3 için ilk yıllarda ticaret kaybının yavaş yerleşmesi (derin STA etkisi 8. yılda zirve) varsayıldı.
- Güven: Orta (S4), Düşük (S2 ve S3 istihdamı ve cari denge).

**Okuma.**

1. **Refah sıralaması:** S0 > S3 iyimser ≈ S2 > S3 ihtiyatlı > S4 > S5.
   - Farklar GSYH'nin onda biri ile yarım puanı arasında. Ama S4'ün kaybı istatistiksel olarak sağlam.
   - S2 ve S3'ün GA'sı sıfırı içeriyor.
2. **İstihdam kısıtını hiçbir çıkış seçeneği kendiliğinden sağlamıyor.**
   - S2'de ihracat kaybı ithal ikamesiyle telafi edilmiyor, çünkü AB malları vergisiz kalıyor.
   - S4-aktif'in daha düşük net kaybı (≈ −35 bin), AB mallarına uygulanan İGV'nin yarattığı ithal ikamesinden geliyor. Bunun üç bedeli var:
     - tüketiciye: takasla bütçeye aktarılan $5,7 mlr;
     - refaha: GSYH −%0,43;
     - kabiliyete: ihracat platformu ve çapa yatırımcı riski, hesaba dahil değil.

   Sonuç: istihdam metriği tek başına korumacılığı ödüllendiriyor. Kısıt testi GSYH ve kabiliyetle birlikte okunmalı.
3. **TÜFE kısıtı bütün çıkış seçeneklerinde sağlanabiliyor.**
   - S2 ve S3'te AB ithalatındaki menşe maliyeti 2–12 bp ekliyor.
   - S4'te tarife şoku takasla nötrleniyor.
   - Asıl risk kur (S5).
4. **S3'ün kalitesi belirleyici.** Türkiye–BK deneyimi doğru tasarlanmış bir STA'nın GB'ye çok yakın sonuç verebildiğini gösteriyor:
   - sıfır tarife;
   - AB girdisiyle kümülasyon;
   - yoldaki mal hükmü.

   Bu yüzden ITA'nın menşe protokolü (PEM'e dinamik atıf, çapraz kümülasyon, %15 tolerans) en yüksek öncelikli müzakere başlığıdır.

---

## 3. Kısıt testleri (temel ilke 9)

| Kısıt | S2 DCFTA | S3 ITA | R7 Dondurma | S4-aktif | S5 |
|---|---|---|---|---|---|
| Enflasyon: birinci tur ≤30 bp/yıl ve ≤50 bp kümülatif; ikinci tur dahil ≤100 bp | ✓ 2–12 bp (menşe maliyeti %1–3; P1 dahil) | ✓ 2–12 bp | ✓ 0 | ✓ 2,5–4,1 bp | ✗ kur şoku: %10 değer kaybında ≈+250 bp |
| Cari denge: T+5'te ≥ %0, çekirdek fazla | ≈ ilk yıllarda −0,1 ile −0,3 puan; kalıcı etki tasarruf-yatırıma bağlı | ≈ −0,1 ile −0,5 puan | ✓ değişmez | ✗ ilk yıllar −0,6 ile −0,8 puan | ✗ |
| Mali: ≤ GSYH %0,5/yıl | ✓ ≈0 | ✓ ≈0 | ✓ 0 | ✓ +%0,05 | ? faiz ve risk primi |
| İstihdam: T+3'te net sıfır; >%5 kayıpta destek | ✗ riski: ≈ −33 bin (GA sıfırı içeriyor); sınıf düzeyi uyum gerekli | ✗ riski: −54 ile +12 bin; menşe tasarımına bağlı | ✓ 0 | ✗ ≈ −35 bin; giyim −59 bin | ✗ |
| Kabiliyet (ölçek, ihracat platformu, çapa yatırımcı) | ✓ ACAA ile | ≈ onaylanmış kuruluş geçiş hükmü şart; giyimde çift dönüşüm | ✓ | ✗ otomotiv, beyaz eşya ve giyim ihracat platformu riski | ✗ |
| DTÖ uyumu | ✓ XXIV:8(b) | ✓ XXIV:8(b) | ✓ XXIV:5(c) (plan ve takvim) | ✓ MFN, bağlı oran içinde | ✓ / ? |
| Hasmane AB'de uygulanabilirlik | Düşük (2030 sonrası) | Orta (T2029) | Orta (T2028) | Yüksek | — |
| **Sonuç** | **Bitiş durumu** | **Ara durum** | **Geçiş** | **Geri dönüş planı** | **Kaçınılacak** |

*Etiket:* `[T]` §2 ve 02a; `[H]` uygulanabilirlik. Güven: Orta.

**Olumsuz bulgu.**
- Hiçbir çıkış seçeneği S0'ı (GB'de kalmayı) bütün kısıtlarda geçmiyor.
- S2'nin S0'a göre net bilançosu başa baş ile hafif negatif arasında (Faz 1: −€6,7 mlr ile +€2 mlr).
- Bunu olumluya çevirecek koşullar şunlar:
  1. **Menşe maliyetinin düşük tutulması:** tam kümülasyon, %15 tolerans, ihracatçının beyanı ve dijital tedarikçi beyanı.
  2. **Özerklik temettüsünün gerçekleşmesi:**
     - girdide sıfır;
     - İGV'nin yeniden tasarımı;
     - kendi STA'ları: Hindistan, Mercosur, Endonezya, Avustralya ve Meksika ile yeni ve modernize anlaşmalar. AB'nin bu ortaklarla anlaşmaları 2026'da sonuçlandı, imzalandı veya geçici olarak uygulanmaya başladı (Faz 1 §2.1).
  3. **STA asimetrisinin kapanması:** $1,2–1,5 mlr/yıl.
  4. **ACAA'nın öncelikli sektörlerde zamanında yapılması.**

---

## 4. Önerilen bitiş durumu ve geçiş sırası

### 4.1 Bitiş durumu: S2 (DCFTA), 2030–2031

**Gerekçe.** S2, çıkışla birlikte kısıt testlerinden geçebilen tek kalıcı rejim (§3). S0 ve S1 çıkışı dışladığı için değerlendirme dışında. Temel ilkelerle uyumu:
- AB pazarına sıfır tarifeli erişimi korur.
- Menşe maliyetini revize PEM ve tam kümülasyonla sınırlar.
- Onaylanmış kuruluş uçurumunu ACAA ile kapatır.
- Türkiye'ye tarife özerkliği ve kendi STA ağını verir:
  - "girdide sıfır" (P1);
  - STA asimetrisinin giderilmesi ($1,2–1,5 mlr);
  - İGV'nin yeniden tasarımı.

**İçerik (asgari).**
1. **Mal ticareti.**
   - Sanayide AB ile karşılıklı %0 tarife ve kota.
   - 1/98 sayılı Karar'daki tarım tavizleri ve işlenmiş tarım ürünlerinin aktarılması.
   - 1996 AKÇT STA'sının anlaşmaya taşınması. Çelik kotası AB'nin 2026/1384 sayılı tüzüğünden ayrı müzakere edilir.
2. **Menşe.**
   - Revize PEM'e dinamik atıf ve çapraz kümülasyon.
   - Fabrika çıkış fiyatının %15'i tolerans.
   - Geri ödeme yasağı yalnızca 50–63. fasıllarda.
   - İhracatçının menşe beyanı; 12 aylık yoldaki mal hükmü.
3. **Uyum değerlendirmesi.**
   - Öncelikli sektörlerde ACAA: makine, elektrikli teçhizat, tıbbi cihaz, inşaat ürünleri, basınçlı ekipman, telsiz ekipmanı.
   - ACAA yürürlüğe girene kadar Türk onaylanmış kuruluşlarının statüsü sürer ("büyükbaba" hükmü).
4. **Gümrük işbirliği.** AEO karşılıklı tanıma (uygulamada), Ortak Transit (GB'den bağımsız), idari işbirliği ve menşe doğrulaması.
5. **Hizmetler ve kamu alımı.**
   - GATS-artı hizmet taahhütleri; geçici hareket ve iş vizesi kolaylığı (Mod 4).
   - Karayolu taşımacılığı kotaları.
   - Karşılıklılık temelinde kamu alımı (7590 sayılı Kanun md. 13 kozu).
6. **Eşit rekabet koşulları.**
   - Sübvansiyon şeffaflığı ve yasak sübvansiyon listesi (ihracata bağlı destekler).
   - İşleyen bir devlet yardımları denetimi. AB'nin talebi bu; Türkiye'de uygulama "süresiz ertelenmiş".
   - TCA md. 411 tipi yeniden dengeleme.
7. **Ticaret savunması ve korunma.** Anti-damping ve telafi edici vergi kuralları; ikili korunma maddesi.
8. **Uyuşmazlık çözümü.** Hakem paneli (TCA modeli). AB hukuku kavramlarında Divan'a başvuru yalnızca uyum bölümleri için.

### 4.2 Geçiş sırası: iki takvim

| | **T2028 yolu** | **T2029 yolu** |
|---|---|---|
| T'de ne olur? | **Çıkış kararı + geçiş dönemi (R7).** Ortaklık Konseyi kararıyla dondurma ve sona erme takvimi kabul edilir; 1/95'in uygulaması 31.12.2029'a kadar veya ITA yürürlüğe girene kadar sürer. Ekonomik rejim değişmez. GB'nin hukuken sona ermesi ITA'nın yürürlüğüyle olur | **ITA (S3) geçici uygulamada.** GB hükümleri etkisiz kalır (Şili md. 33.11 tipi madde). Sanayide %0 tarife ve PEM menşei; Türkiye'nin tarife özerkliği başlar |
| T'den sonra | ITA (S3): 2029 sonu veya 2030 başı | DCFTA (S2): 2030–2031 |
| Bitiş durumu | DCFTA (S2): 2031 | DCFTA (S2): 2030–2031 |
| Kritik koşul | Haziran 2027'ye kadar dondurma kararı için AB pozisyonu (nitelikli çoğunluk) | **Eylül 2027'ye kadar** ITA müzakere yetkisi |
| Yedek | Dondurma yoksa T ertelenir. Erteleme yoksa aktif S4 | Yetki gecikirse T2029'da dondurma (R7), ITA 2030'da |
| Avantaj | Erken hukuki kesinlik; pazarlık baskısı tarihi | Tek adımlı ekonomik geçiş; seçim sonrası; TÜFE hedefi %9 (OVP) |
| Dezavantaj | 2028 genel seçimleriyle çakışma; dezenflasyonun kritik yılı (TÜFE hedefi %13,5); ekonomik özerklik 2030'a kayar | Yetki takvimi dar; AP onayı 2029 AP seçimlerinden önce veya geçici uygulamayla |

**Öneri `[H]`.**
- Ekonomik ve hukuki çıkış tarihi T2029 olsun.
- T2028 siyasi olarak gerekiyorsa **çıkış kararı ve geçiş dönemi başlangıcı** olarak kullanılsın. Geçiş 31.12.2029'a veya ITA'nın yürürlüğüne kadar sürer.
- Bu, İngiltere'nin hukuki çıkışı (31.1.2020) ile geçiş dönemi sonu (31.12.2020) ayrımına benzer, ama bir farkla:
  - Ortaklık Konseyi kararı GB'yi dondurabilir, değiştirebilir ve aşamalandırabilir; kaldıramaz. GB, Ankara Anlaşması'nın hedefidir.
  - Bu yüzden GB'nin hukuken sona ermesi ancak ITA'nın yürürlüğüyle olur.
  - 1.1.2028'de "hukuki çıkış" yalnızca tek taraflı fesihle (R15) mümkün; bu yol hukuken açık ve AB'nin karşı önlemlerine kapı aralar.
- Güven: Orta.

### 4.3 Geri dönüş planı: aktif S4, ama bir koşulla

- **Ne zaman devreye girer?** AB hem dondurmayı hem ITA'yı reddederse ve T ertelenmezse.
- **İçerik (02a §4):**
  - İGV rejimi c2;
  - girdide sıfır (P1);
  - geniş vergi takası;
  - giyim ve %5 eşiğini aşan 21 sınıf için hedefli destek;
  - XXVIII:5 çekincesiyle tarife esnekliği.
- **Kısıt bilançosu.**
  - TÜFE ≈3 bp; mali +%0,05 GSYH.
  - Net imalat istihdamı ≈ −35 bin, çekirdeği giyim.
  - İhracat −€21 mlr (σ = 5); cari denge ilk yıl −0,6 ile −0,8 puan.
- **Koşul.** Aktif S4'ün hazırlığı, T2028 için 1.7.2027'de, T2029 için 1.7.2028'de ilan edilmiş olmalı. Hazırlık müzakerede caydırıcılık işlevi görür: AB'nin anlaşmasızlık maliyeti c2'de $28,5 mlr.
- **Dürüst uyarı.** Aktif S4 bir bitiş durumu değil, bir pazarlık aracı ve son çare. Giyimdeki istihdam kaybı ve ihracat platformu riski yalnızca bir anlaşmayla çözülür.

### 4.4 Müzakere paketi: kim neyi ister, kimin kozu var?

| Taraf | Talepler | Kozlar |
|---|---|---|
| AB | İşleyen devlet yardımları denetimi; kamu alımında açılım; ilaçta "yapay kur" fiyatlaması ve iyi üretim uygulaması sertifikalarının kabulü; serbest dolaşımdaki mallara ek vergilerin, ithalat gözetiminin ve ham deri ihracat vergilerinin kaldırılması; yaptırımların dolanılmasına karşı taahhüt; SKDM/ETS uyumu; GKRY'ye ayrımsız uygulama | Çelik kotaları; ticaret savunması; SKDM; onaylanmış kuruluş statüsü; menşe kuralları; SAFE; vize |
| Türkiye | AB pazarına sıfır tarife ve kota; PEM'de çapraz kümülasyon; onaylanmış kuruluş sürekliliği; karayolu kotaları; iş vizesi; STA asimetrisinin sona ermesi | Pazar büyüklüğü (AB'nin 5. ortağı; otomotivde 3. pazar, €18,8 mlr); iki yönlü otomotiv tedarik zinciri; aktif S4'ün AB'ye maliyeti ($28,5 mlr); enerji transiti (2027'den itibaren Rus boru gazı yasağı); göç; kamu alımında karşılıklılık |

*Kaynak:* `[V]` Türkiye 2025 Raporu; Ortak Açıklama, 13.10.2026; ACEA; Tüzük 2026/261. `[T]` 02a §4. Güven: Orta.

**Çıkarım.**
- Nitelikli çoğunluk yolunda belirleyici olan Berlin ve Roma.
- Türkiye'nin en güçlü kozu otomotiv ve sanayi tedarik zinciri.
- En pahalı tavizi ise devlet yardımları denetimi ve kamu alımları. Bunlar Faz 7'de fiyatlandırılacak.

**Otomotiv "erken hasat" önerisi `[H]`.**
- Anlaşmasızlıkta iki tarafın en çok kaybettiği tek sektör otomotiv:
  - AB'nin Türkiye'ye otomobil ihracatı €15,6 mlr;
  - Türkiye'nin AB'ye ihracatı €18,2 mlr (araç); 29.10'da AB'nin kaybı σ = 5'te €7,4 mlr.
- Bu yüzden ITA müzakeresinin ilk ve ayrı bir bölümü olarak üç unsur önerilmeli:
  - sıfır tarife;
  - parçalarda PEM çapraz kümülasyonu;
  - tip onayının (BM/ECE 1958 Anlaşması, iki taraf da üye) ve otomotiv uyum değerlendirmesinin sürekliliği.
- Çapa yatırımcılar (Renault, Stellantis, Ford, Toyota, Hyundai ve AB'deki tedarikçileri) bu bölümün en güçlü savunucusu olur.

---

## 5. Hukuki yol haritası

### 5.1 Çıkışın hukuki temeli: neden AB'nin katılımı gerekiyor?

| Metin | Hüküm | Sonuç |
|---|---|---|
| Ankara Anlaşması (1963) | Md. 22: Ortaklık Konseyi kararları tarafları bağlar. Md. 23: Konsey "oybirliğiyle karar alır" (bir yanda üye devletler, AB Konseyi ve Komisyon, öte yanda Türkiye). Md. 25: uyuşmazlıklar Ortaklık Konseyi'ne; Konsey karara bağlayabilir veya AB Adalet Divanı'na ya da başka bir yargı merciine gönderebilir. Md. 31–33: **fesih, çekilme veya süre hükmü yok** | Tek taraflı fesih metinde öngörülmemiş |
| Katma Protokol (1970) | Md. 47: anti-damping; md. 60: korunma önlemleri; md. 41: yerleşme ve hizmetlerde "standstill" | Çıkıştan sonra da yürürlükte kalabilecek üye devlet yetkisi alanları |
| 1/95 sayılı Ortaklık Konseyi Kararı | Md. 13: OGT'ye uyum. Md. 14(2): Gümrük Birliği Ortak Komitesi, Türkiye'nin OGT'nin altında tarife uygulamasına hiçbir zaman izin veremez. Md. 58(2): mevzuat farkında zarar gören taraf "gerekli koruma önlemlerini" alabilir. Md. 61–62: tahkim yalnızca md. 58(2), 63 ve 64 önlemleri için; hakem listesini Ortaklık Konseyi belirler (listenin oluşturulduğuna dair kanıt yok `[D?]`). Md. 64: dengesizlik halinde "yeniden dengeleme önlemleri". Md. 65: yürürlük 31.12.1995; süre veya fesih hükmü yok | OGT'den tek taraflı sapma tahkime götürülemez; Ortaklık Konseyi'nde oybirliği gerekir. AB'nin elinde md. 58(2) ve md. 64 var |
| Antlaşmalar hukuku | Türkiye 1969 Viyana Sözleşmesi'ne taraf değil. Teamül hukuku (Sözleşme md. 56 ve 62'nin karşılığı): fesih hükmü olmayan bir antlaşmadan çekilme, ancak tarafların bunu öngördüğü kanıtlanırsa veya antlaşmanın niteliğinden çıkıyorsa mümkün. Köklü değişiklik ilkesi dar yorumlanır | **Tek taraflı çıkış hukuken açık** (R15). AB, Uygulama Tüzüğü md. 3(ba) ile karşı önlem alabilir |

*Kaynak:* `[V]` Ankara Anlaşması (CELEX 21964A1229(01)), Katma Protokol (21970A1123(01)), 1/95 (21996D0213(01)); BM Antlaşmalar Koleksiyonu; Tüzük 654/2014. Güven: Yüksek.

**Sonuç.** Hukuken temiz çıkış ancak AB ile birlikte mümkün. Bunun iki aracı var:
- **Ortaklık Konseyi kararı.**
  - 1/95'in uygulama hükümlerini dondurabilir, değiştirebilir ve aşamalandırabilir.
  - Ankara Anlaşması'nın hedefi olan gümrük birliğini kendi başına kaldıramaz; kurumsal çerçeveyi değiştiremez (ABİDA md. 218(9)).
- **AB'nin tek başına yetkili olduğu bir ticaret anlaşması (md. 207).**
  - GB hükümlerinin "etkisiz kalacağını" hükme bağlayabilir.
  - Emsal: AB–Şili Geçici Ticaret Anlaşması (ITA) md. 33.11. Bu anlaşmayla, karma bir ortaklık anlaşmasının ticaret kısmı, ona dayanan Ortaklık Konseyi kararlarıyla birlikte yürürlükten kalktı.
  - Türkiye'ye uygulanınca: Katma Protokol'ün GB hükümleri, 1/95, 1/98 sayılı Karar ve 1996 AKÇT anlaşması etkisiz kalır.
  - Üye devlet yetkisindeki kısımlar sürer: işçilere ilişkin 1/80 sayılı Karar ve md. 41 standstill hükmü.

### 5.2 AB tarafında karar kuralları ve veto oyuncuları

| Adım | Hukuki dayanak | Oy | Not |
|---|---|---|---|
| Müzakere yetkisi ve yönergeleri | ABİDA md. 218(2)–(4); md. 207(3)–(4) | Nitelikli çoğunluk. Hizmet ticareti, fikrî mülkiyetin ticari yönleri ve doğrudan yatırımda iç kurallar oybirliği gerektiriyorsa oybirliği; kültürel, görsel-işitsel, sosyal, eğitim ve sağlık hizmetlerinde özel kurallar | 2016 modernizasyon tavsiyesine hiç yetki verilmedi |
| Ortaklık Konseyi'nde AB pozisyonu (dondurma kararı) | Md. 218(9), maddi dayanak md. 207(4) | Nitelikli çoğunluk (C-81/13: oy kuralı maddi hukuki dayanağı izler). Komisyon'un Eylül 2026'daki önerisi bu dayanağı kullanıyor (COM(2026) 477). Öneri, A.TR kurallarını düzenleyen Gümrük İşbirliği Komitesi'nin 1/2006 sayılı Kararı'nın yerine geçecek kararla ilgili | **Faz 0'daki "oybirliği" varsayımı düzeltildi** |
| İmza ve geçici uygulama | Md. 218(5) | Nitelikli çoğunluk | Mercosur ITA: Konsey Kararı 2026/183 (9.1.2026). Fransa, Polonya, Avusturya, Macaristan ve İrlanda karşı oy verdi, Belçika çekimser kaldı; karar yine de çıktı |
| Avrupa Parlamentosu onayı | Md. 218(6)(a)(v) | Salt çoğunluk | Mercosur'da AP 21.1.2026'da 334–324–11 oyla Divan'dan görüş istedi (md. 218(11); Görüş 1/26). Onay bekliyor; geçici uygulama 1.5.2026'da başladı |
| Akdetme | Md. 218(6) | Nitelikli çoğunluk | — |
| Md. 217 ortaklık anlaşması veya karma anlaşma | Md. 217, 218(8) | Oybirliği ve 27 ulusal onay (karma) | Yunanistan ve GKRY'nin hukuki vetosu |

**Engelleme azınlığı.** Nitelikli çoğunlukta bir kararı engellemek için en az dört üye devletin ve AB nüfusunun %35'inden fazlasının birleşmesi gerekir.
- Yunanistan ve GKRY'nin nüfus payı ≈%2,5. Md. 207 yolunda hukuki vetoları yok.
- Siyasi vetoları ise var:
  - Konsey 10 yıldır yetki vermiyor. Ticaret Bakanı Ekim 2026'da bunu "bazı üye devletlerin tutumuna" bağladı.
  - Her anlaşma GKRY'ye de uygulanacak. Bu, 2005 Ek Protokolü'nün uygulanmaması meselesini yeniden açar.
  - Oybirliği gerektiren başka dosyalar pazarlık için birbirine bağlanabilir: SAFE savunma fonu, Doğu Akdeniz yaptırımları.
- Mercosur'da karşı çıkanların nüfus payı ≈%31'di ve kararı engelleyemedi.
- Türkiye için belirleyici başkentler Berlin ve Roma. İkisi de otomotiv ve sanayi tedarik zinciri üzerinden en çok kaybedecek olanlar arasında (§4.4, 02a).

**Görüş 1/26 riski.** AB Adalet Divanı'nın Mercosur görüşü, karma anlaşmayı "ticaret" ve "ortaklık" diye ikiye ayırma tekniğini daraltabilir. Türkiye ITA'sı için hafifletici unsurlar:
- Yalnızca mal ticareti, gümrük, menşe ve teknik kurallar içerir. Bunlar AB'nin münhasır yetkisinde.
- Yatırım korumasını dışarıda tutar. Bu alan paylaşılan yetkidedir (Görüş 2/15).

Bu tasarım ITA'yı AB'nin tek başına yetkili olduğu bir anlaşma olarak tutar. `[H]` Güven: Orta.

### 5.3 Şablonlar: yeni çerçevenin yapı taşları

| Şablon | Tarifeler | Menşe kuralları | Uyum değerlendirmesi | Eşit rekabet koşulları ve uyuşmazlık | Süre | Türkiye için alınacak |
|---|---|---|---|---|---|---|
| AB–Birleşik Krallık TCA (2020) | %0 tarife, %0 kota | Yalnızca ikili kümülasyon; tolerans değerin %10'u; ihracatçının kendi beyanı; PEM değil | MRA yok; sektör ekleri (ilaçta iyi üretim uygulamaları denetimi) | Sübvansiyon denetimi ilkeleri; md. 411 yeniden dengeleme (14 gün istişare, 30 gün tahkim); tahkim; 12 ay ihbarla fesih | ≈10 ay; 1.1.2021'de geçici uygulama | Hız ve geçici uygulama tekniği; yoldaki mal hükmü (md. 67) |
| AB–Ukrayna, Moldova, Gürcistan DCFTA'ları | Neredeyse tam; Ukrayna'da 2025'te AB üretim standartlarına bağlı kota artışları | PEM | Ukrayna'da ACAA 2025–26 | Mevzuat yakınlaştırması; AB hukuku kavramlarında Divan'a başvuru | 2008–2012; 2014–2016 | Kapsam, ama yakınlaştırma yükümlülüğü ağır |
| AB–İsviçre (1972 STA + sektörel) | Sanayide sıfır | PEM | 1999 MRA. Tıbbi cihaz bölümü 26.5.2021'den beri dondurulmuş: İsviçre sertifikaları AB'de geçersiz kaldı | 2026 paketi: dinamik uyum, Divan rolü | 2024'te müzakere; 2.3.2026'da imza | **MRA güncellenmezse sertifika uçurumu**: Türkiye için ana uyarı |
| AB–Andorra ve San Marino | Gümrük birliği | PEM'de AB menşeli sayılır | AB müktesebatı | — | — | GB'nin PEM'deki "eşdeğerlik" muamelesi; Türkiye'de bu hüküm yok |
| AB–İsrail (ACAA, 2013) | — | — | İlaç iyi üretim uygulamaları protokolü | — | — | İlaç seri serbest bırakma sorununun çözüm şablonu |
| AB–Meksika (2026) ve AB–Şili (2025) ITA'ları | Neredeyse tam | İkili kümülasyon; %10 tolerans | TBT bölümü | Sürdürülebilir kalkınma; devletten devlete uyuşmazlık | 2016–2025; 2017–2022 | **ITA ayrımı ve "GB hükümleri etkisiz" maddesi** (Şili md. 33.11, 33.15, 33.16) |

*Kaynak:* `[V]` TCA (CELEX 22021A0430(01)) md. 40, 42, 54, 67, 411, 779, 783; AB–Şili ITA md. 3.3, 3.5, 33.11, 33.15–33.16; Konsey Kararları 2014/492, 2014/494; MDCG 2021 notu. Güven: Orta–Yüksek.

### 5.4 Menşe kuralları ve PEM: çıkışın sessiz maliyeti

- **Durum.**
  - Türkiye 1.2.2014'ten beri PEM Sözleşmesi tarafı.
  - Revize kurallar 1.1.2025'ten beri geçerli; eski kurallar 31.12.2025'e kadar paralel uygulandı.
  - Sanayi mallarında AB–Türkiye ticaretinde menşe ispatı gerekmiyor; A.TR serbest dolaşımı belgeliyor. Tarım (Ortaklık Konseyi Kararı 1/2025) ve AKÇT çeliği (Ortak Komite Kararı 1/2025) için PEM'e dinamik atıf 22.12.2025'te kabul edildi.
- **Çıkışta A.TR düşer.** Yerine EUR.1 veya EUR-MED dolaşım belgeleri ya da menşe beyanı gelir (PEM Başlık V).
- **Çapraz kümülasyonun üç şartı** var:
  - AB–Türkiye STA'sının menşe protokolü PEM'e atıf yapmalı;
  - kümüle edilecek girdinin geldiği her ülkeyle PEM'e dayalı STA olmalı;
  - ilgili bildirimler yayımlanmalı.

  Türkiye'nin PEM'deki STA ağı: EFTA, Batı Balkanlar, Gürcistan, Moldova, Faroe, Fas, Tunus, Mısır, Filistin. Ukrayna STA'sının yürürlüğü `[D?]`. İsrail ile ticaret 2024'te durduruldu; Ürdün STA'sı 2018'de feshedildi.
- **Revize PEM'in Türkiye için önemli kuralları.**
  - Tolerans: fabrika çıkış fiyatının %15'i.
  - Geri ödeme yasağı yalnızca 50–63. fasıllarda.
  - Tam kümülasyon 50–63. fasıllar hariç serbest.

  Sonuç: giyimde (61–62) çift dönüşüm kuralı ve geri ödeme yasağı belirleyici. Faz 4'te giyim derin analizi.
- **Eşdeğerlik yok.** Revize Sözleşme, GB mallarını AB menşeli saymıyor. Andorra ve San Marino'daki eşdeğerlik muamelesi Türkiye'ye uygulanmıyor.
- **Yoldaki mallar.** TCA md. 67'deki gibi 12 aylık bir geçiş hükmü gerekir.

*Kaynak:* `[V]` revize PEM (L_202400390), Ortaklık Konseyi Kararı 1/2025, COM(2026) 477. Güven: Yüksek.

### 5.5 Uyum değerlendirmesi: onaylanmış kuruluş uçurumu

- **Hukuki dayanak.** 1/95 md. 8–10: Türkiye AB teknik mevzuatını iç hukukuna aktarır; ticaret o mevzuata göre yürür. 2/97 sayılı Karar aktarılan mevzuatı listeler. Ortaklık Konseyi'nin 15.5.2006 tarihli 1/2006 sayılı Kararı md. 9'u uygular ve Türk onaylanmış kuruluşlarının bildirimini düzenler. Bu karar, A.TR'ye ilişkin aynı numaralı Gümrük İşbirliği Komitesi kararından farklıdır.
- **Bugünkü stok.** NANDO'da 95 Türk kaydı var; ≈81'inin bildirimi yürürlükte. Ayrıca basınçlı ekipmanda 8 tanınmış üçüncü taraf kuruluş ve inşaat ürünlerinde 2 teknik değerlendirme kuruluşu bulunuyor. Bildirimler Eylül 2026'ya kadar sürdü.
- **Kapsanan alanlar:**
  - inşaat ürünleri, makine, asansörler, kişisel koruyucu donanım;
  - basınçlı ekipman ve basit basınçlı kaplar, gaz yakan cihazlar;
  - tıbbi cihazlar, elektromanyetik uyumluluk, telsiz ekipmanı;
  - patlayıcı ortam ekipmanı (ATEX), ölçü aletleri, eğlence amaçlı tekneler;
  - piroteknik ürünler, kablolu taşıma tesisleri, dış mekân gürültüsü, kazanlar.
- **TÜRKAK** dokuz alanda Avrupa Akreditasyon (EA) çok taraflı anlaşması imzacısı; bir sonraki değerlendirme Mart 2028. Bu statü çıkıştan sonra da sürer, ama onaylanmış kuruluş statüsü vermez.
- **Uyarılar.**
  - İngiltere: onaylanmış kuruluşlar 2020 sonunda AB statüsünü kaybetti.
  - İsviçre: MRA'nın tıbbi cihaz bölümü güncellenmediği için 2021'de sertifikalar geçersiz kaldı.
- **Sonuç.**
  - Bir ACAA, bir MRA veya bir geçiş ("büyükbaba") hükmü olmadan Türk sertifikaları çıkış günü AB'de geçersiz olur.
  - AB'nin bunun karşılığında isteyeceği belli: dinamik uyum, piyasa gözetimi ve Divan'a bağlı uyuşmazlık çözümü.
  - T2028 ve T2029'un ikisinde de dondurma kararına "onaylanmış kuruluşların statüsü sürer" hükmü konmalı.
- `[V]` NANDO (18.10.2026), EA MAC kararları. Güven: Yüksek.

### 5.6 DTÖ tarafı

| Adım | Dayanak | Zamanlama |
|---|---|---|
| XXVIII:5 çekincesi: Cetvel XXXVII'yi 2027–2029'da değiştirme hakkı | GATT XXVIII:5 | **31.12.2026'dan önce** (02a §7) |
| DS629 kararına uyum | DSU md. 21 | DSB 27.10.2026; makul süre içinde |
| Geçici anlaşma (dondurma) bildirimi: "plan ve takvim" ile | GATT XXIV:5(c), XXIV:7(a); XXIV Mutabakatı para. 3 (makul süre en fazla 10 yıl) | İmzayı izleyen ilk fırsatta |
| STA (ITA) bildirimi | XXIV:7(a); Şeffaflık Mekanizması (WT/L/671): müzakere başlarken erken duyuru, onay veya uygulamadan hemen sonra ve tercihler uygulanmadan önce bildirim; Bölgesel Ticaret Anlaşmaları Komitesi bir yıl içinde Sekretarya'nın olgusal sunumu üzerinden görüşür | Uygulamadan önce |
| GB'nin sona erdiğinin ve Türk uygulanan tarifesinin bildirimi | XXIV:7; Entegre Veri Tabanı bildirimleri | Çıkış günü |
| Türkiye'nin kendi cetveli | Türkiye GB içinde de kendi bağlı oranlarını korudu; çıkış XXIV:6 tazminatı gerektirmez. Uygulanan MFN bağlı oran içinde serbest | — |

*Kaynak:* `[V]` GATT 1994; XXIV Mutabakatı; WT/L/671; DS629. Güven: Yüksek.

**Ek not: anlaşmasız çıkışta GB'nin XXIV dayanağı.** Bugün AB mallarına İGV uygulanmaması GATT XXIV ile haklı gösteriliyor. DS629 panelinin ifadesiyle, bölgesel ticaret anlaşması ortaklarını muaf tutmak I:1'i ihlal etti, ama XXIV ile haklı görüldü. Anlaşmasız çıkışta bu dayanak düşer. AB malları İGV'ye ve elektrikli araç ek vergilerine (bağlı oran içinde) tabi olur. 02a §4'teki rejim seçimi bu yüzden zorunludur.

### 5.7 Türk iç hukuku

| İşlem | Dayanak | Not |
|---|---|---|
| ITA veya STA'nın onayı | Anayasa md. 90/1: onay, TBMM'nin bir kanunla uygun bulmasına bağlı. Md. 90/5: usulüne göre yürürlüğe konmuş antlaşmalar kanun hükmünde | TBMM uygun bulma kanunu + Cumhurbaşkanı onay kararı; 1–2 ay `[D?]` |
| Ortaklık Konseyi kararları (dondurma, geçiş) | Md. 90/3: milletlerarası bir antlaşmaya dayanan uygulama antlaşmaları TBMM onayı gerektirmez, ama ekonomik ve ticari olanlar yayımlanmadan yürürlüğe giremez. 244 sayılı Kanun | Cumhurbaşkanı kararı ve Resmî Gazete'de yayım `[D?]` |
| Kısa süreli ekonomik antlaşmalar | Md. 90/2: süresi bir yılı aşmayan, maliyeye yük getirmeyen ekonomik, ticari veya teknik antlaşmalar yayımla yürürlüğe girebilir | Kısa bir köprü düzenlemesi için seçenek |
| Uygulanan tarife ve İGV | İthalat Rejimi Kararı ve İGV kararları (Cumhurbaşkanı kararı); 474 sayılı Gümrük Tarife Kanunu, 2976 sayılı Dış Ticaretin Düzenlenmesi Hakkında Kanun `[D?]` | T−6'da ilan (02a §7) |
| ÖTV ve KDV oranları (takas) | 4760 sayılı Kanun md. 12 (Cumhurbaşkanı oran ve dilim yetkisi); 3065 sayılı Kanun md. 28 | Çıkış günü yürürlük; matrah tanımı (md. 11) kanunla değişir |
| Kamu alımında karşılıklılık | 4734 sayılı Kanun ek md. 13 (7590 sayılı Kanun md. 13, 2026) | Müzakere kozu |
| Ticaret savunması | 3577 sayılı İthalatta Haksız Rekabetin Önlenmesi Hakkında Kanun; korunma önlemleri mevzuatı `[D?]` | Ticaret Bakanlığı |
| Mevcut DTÖ risklerinin temizlenmesi | 4760 md. 7/2 ve 5520 md. 32/7 (kanun değişikliği); ÖTV (III) listesi (Cumhurbaşkanı kararı) | 02a §1.8 |

*Kaynak:* `[V]` Anayasa md. 90; 4760, 3065, 4734, 5520 sayılı Kanunlar; 7590 sayılı Kanun. `[D?]` 244, 474, 2976 ve 3577 sayılı Kanunların ilgili maddeleri bu oturumda metinden doğrulanmadı. Güven: Orta.

### 5.8 İki takvim için adım adım yol haritası

Bugün 18.10.2026. T2028'e 14,5 ay, T2029'a 26,5 ay var.

| # | Adım | T2028 son tarih | T2029 son tarih | Kurum | Not |
|---|---|---|---|---|---|
| 1 | XXVIII:5 çekincesi | 31.12.2026 | 31.12.2026 | Dışişleri, Ticaret | Takvimden bağımsız |
| 2 | İç karar ve AB'ye resmî bildirim: çıkış niyeti, dondurma ve ITA talebi; Ortaklık Konseyi toplantı talebi | Kasım 2026 | Mart 2027 | Cumhurbaşkanlığı, Dışişleri | "Önce anlaşma, sonra çıkış" ilkesinin ilanı |
| 3 | Konsey'de dondurma kararı için AB pozisyonu (md. 218(9), nitelikli çoğunluk) | Haziran 2027 | Haziran 2028 | Komisyon önerisi, Konsey | Kapı K1 |
| 4 | Konsey'in ITA müzakere yetkisi (md. 207, nitelikli çoğunluk) | Mart 2027 | **Eylül 2027 (2027'nin 3. çeyreği)** | Konsey | T2029 için kritik eşik |
| 5 | Ortaklık Konseyi dondurma kararı: 1/95'in uygulaması, A.TR, onaylanmış kuruluşlar, ticaret savunması ve uyuşmazlık hükümleri sabit bir tarihe kadar (ör. 31.12.2029) veya ITA yürürlüğe girene kadar sürer | Eylül 2027 | Eylül 2028 (yedek) | Ortaklık Konseyi | T2028'in tek gerçekçi yolu |
| 6 | Yeni Türk tarife cetveli ve İGV rejimi ilanı (aktif S4 hazırlığı dahil) | 1.7.2027 | 1.7.2028 | Ticaret Bakanlığı | Kapı K2; S4'e hazır olmak pazarlık kozudur |
| 7 | ITA müzakeresi: sanayide sıfır tarife; tarım ve AKÇT rejimlerinin aktarılması; PEM'e atıf; gümrük ve AEO işbirliği; onaylanmış kuruluş geçiş hükmü; ticaret savunması; uyuşmazlık çözümü; hafif eşit rekabet hükümleri | — (T2028'de yetişmez) | Eylül 2027–Eylül 2028 | Ticaret Bakanlığı heyeti | ≈12 ay |
| 8 | İmza ve geçici uygulama (md. 218(5)); Avrupa Parlamentosu onayı | — | Kasım–Aralık 2028; AP onayı 2029 AP seçimlerinden önce veya geçici uygulamayla | Konsey, AP | Mercosur emsali: AP onayı öncesi geçici uygulama |
| 9 | TBMM uygun bulma kanunu ve yayım | Ortaklık Konseyi kararı için yayım (Eylül–Aralık 2027) | Aralık 2028 | TBMM, Cumhurbaşkanlığı | Anayasa md. 90 |
| 10 | DTÖ bildirimleri: XXIV:7(a) ve Şeffaflık Mekanizması | Dondurma kararı imzalanınca | ITA uygulanmadan önce | Cenevre Daimi Temsilciliği | |
| 11 | Uygulama hazırlığı: menşe ispatı (onaylı ihracatçı, tedarikçi beyanı), BİLGE, KOBİ eğitimi, yoldaki mallar | Kasım 2026'dan itibaren | Ocak 2028'e kadar başlamalı | Ticaret Bakanlığı | İngiltere'nin ilk aylardaki kullanım oranı %59–70 |
| 12 | Mevcut 24 STA'daki GB atıfları ve PEM kümülasyon ilişkileri | Paralel | Paralel | Ticaret Bakanlığı | |

**Faz 0'a göre iki düzeltme.**
- Ortaklık Konseyi kararında AB pozisyonu nitelikli çoğunlukla belirleniyor, oybirliğiyle değil (C-81/13; COM(2026) 477). Bu, T2028'in dondurma yolunu Yunanistan ve GKRY'nin hukuki vetosundan kurtarıyor; siyasi vetodan değil.
- T2028'de ince STA'nın (S3) yetişme olasılığı Faz 0'da sanılandan düşük. Kritik darboğaz müzakere yetkisi. Bu yüzden T2028'in gerçekçi içeriği "hukuki çıkış kararı + dondurma + T2029–2030'da ITA" olarak tanımlanmalı.

---

## 6. Olasılıklar ve kapılar (güncellenmiş)

Faz 0'daki öznel olasılıklar (V-11, hasmane AB) üç yeni bilgiyle güncellendi:
- **Müzakere yetkisi darboğazı.** Konsey 10 yıldır yetki vermiyor. Ticaret Bakanı Ekim 2026'da "bazı üye devletleri" işaret etti.
- **Nitelikli çoğunluk yolu var.** Mercosur'da yetki ve imza, beş üye devletin karşı oyuna rağmen çıktı. Dondurma kararı için de AB pozisyonu nitelikli çoğunlukla belirleniyor.
- **ITA tekniği mevcut.** Şili ve Meksika örnekleri var. Ama Görüş 1/26 bunu daraltabilir.

| T'deki sonuç | T2028: Faz 0 | **T2028: Faz 2** | T2029: Faz 0 | **T2029: Faz 2** | Gerekçe |
|---|---|---|---|---|---|
| S2: DCFTA yürürlükte | < %5 | **< %2** | %5–15 | **%3–8** | DCFTA 2030 sonrası projesi (müzakere 3–6 yıl) |
| S3: ITA, geçici uygulamada | %10–25 | **%5–10** | %30–45 | **%25–40** | T2028'de müzakere için zaman yok; T2029'da yetki 2027'nin 3. çeyreğinde verilmeli |
| R7: dondurma veya geçiş düzenlemesi | %15–30 | **%25–35** | %15–25 | **%15–25** | Nitelikli çoğunluk yolu, AB'nin otomotiv çıkarı |
| S4/S5: anlaşmasız çıkış | %45–70 | **%55–68** | %25–45 | **%30–50** | Hasmane AB; siyasi veto |

*Etiket:* `[H]` uzman yargısı; kapılar işletilmeden önceki durum. Güven: Düşük.

**Kapılarla birlikte okuma.** "Önce anlaşma, sonra çıkış" ilkesi gereği:
- K1'de (T2028 için 1.4.2027; T2029 için 1.1.2028) dondurma veya ITA yetkisi yoksa T ertelenir.
- Bu durumda S4/S5 olasılığının büyük kısmı **erteleme**ye dönüşür. Çıkış yönü veri kalır; değişen tarihtir.
- Kapıların asgari koşulları Faz 0 §2A'daki gibi. K1'e bir koşul eklendi: dondurma kararında **onaylanmış kuruluşların statüsünün sürmesi** hükmü.

---

## 7. Riskler ve geri dönüş planı

| Risk | Olasılık | Etki | Önlem | Tetikleyici |
|---|---|---|---|---|
| AB yetki vermez (siyasi veto) | Yüksek | T ertelenir veya S4 | Berlin ve Roma ile otomotiv ve tedarik zinciri gündemi; aktif S4'ün inandırıcı hazırlığı (BATNA) | K1 |
| Görüş 1/26 ITA ayrımını daraltır | Orta | ITA yolu kapanır, karma anlaşma (oybirliği) gerekir | ITA'yı yalnızca mal ticareti, gümrük ve menşe ile sınırlamak; yatırım korumasını dışarıda bırakmak | Divan görüşü |
| Onaylanmış kuruluş uçurumu | Yüksek (anlaşmasız) | Makine, tıbbi cihaz, inşaat ürünleri ve telsiz ekipmanında AB'ye ihracat durur | Dondurma kararında süreklilik hükmü; Türk üreticilerinin AB onaylanmış kuruluşlarıyla yedek sözleşmeleri | T−6 |
| Menşe uyumunda düşük tercih kullanımı (ilk yıl %59–70) | Yüksek (S3) | İhracatçıya ek maliyet | Onaylı ihracatçı ve tedarikçi beyanı sistemi; KOBİ eğitimi; T−12'den başlamak | T−12 |
| AB ticaret savunmasında sertleşme (S5) | Orta | Çelik, kimya, tekstilde ek vergiler | Çelik kotası müzakeresi; anti-damping savunma kapasitesi | Sürekli |
| Risk primi ve kur | Orta | **%10 değer kaybı ≈ +250 bp TÜFE** (kur geçişkenliği ≈%25; TCMB 2023). Bu, tarife kanalının 30–80 katı | Çıkışın piyasaya önceden ve kurallı biçimde duyurulması; makro çerçeve (Faz 6) | CDS, kur |
| Seçim takvimi (2028) | Yüksek (T2028) | Siyasi ekonomi riski | T2029'un tercih edilmesi; T2028'de yalnızca hukuki çıkış ve dondurma | — |
| Mevcut DTÖ riskleri (02a §1.8) | Orta | AB'nin ilk davaları | Çıkıştan önce temizlemek | Aralık 2026 |

*Etiket:* `[H]`; kur geçişkenliği `[V]` (TCMB). Güven: Orta.

**En büyük risk tarife değil, kur.**
- Aktif S4'ün tarife kanalındaki TÜFE etkisi 3–8 bp.
- Çıkışın kötü yönetilmesinden doğacak %10'luk bir risk primi şoku ise ≈250 bp.
- Bu yüzden çıkışın "nasıl" yapıldığı, "ne" yapıldığından daha önemli. Kurallı, önceden ilan edilmiş, anlaşmaya dayalı ve geri dönüş planı hazır bir süreç gerekiyor.
- Ayrıntı Faz 6'da.

---

## 8. Faz 2 kalite kontrol listesi

| Kontrol | Durum |
|---|---|
| S0–S5 ve melez seçenekler (R7, R8) tanımlandı ve karşılaştırıldı | ✓ §1–§2 |
| Karşılaştırma sayısal; her sayı etiketli ve aralıklı | ✓ §2 (çekim modeli, 02a modelleri, menşe maliyeti senaryoları) |
| Kısıt testleri (temel ilke 9) her seçenek için | ✓ §3 |
| İki takvim için ayrı bitiş durumu ve sıra | ✓ §4 |
| Hukuki yol haritası: AB (md. 207, 217, 218; Mercosur ve Şili emsalleri; C-81/13), Ankara Anlaşması ve 1/95, DTÖ (XXIV, XXVIII), Türk iç hukuku (Anayasa md. 90) | ✓ §5 |
| Olumsuz bulgular ve onları değiştirecek koşullar | ✓ §3, §4, §7 |
| Faz 0 ve Faz 1 varsayımlarında düzeltmeler açıkça yazıldı | ✓ §5.8 (oy kuralı), §6 (olasılıklar), 02a §3.1 (otomobilde bağlı oran) |
| Pazartesi sabahı testi | ✓ 02a §7, §5.8 |
| Kod ve veri yeniden üretilebilir | ✓ `kod/f2*.py`, `veri/politika_*.csv` |

---

## 9. Durum özeti (Faz 2)

**Çerçeve (değişmedi).** Çıkış yönü veri; AB hasmane; üyelik perspektifi yok. İki takvim: T2028 ve T2029.

**Faz 2A — politika uzayı**
- **Öneri: AB'ye tarife + yerli ürüne ÖTV indirimi.**
  - Tarife MFN ve bağlı oran içinde mümkün.
  - Yerli ürüne özgü ÖTV indirimi GATT III:2 ihlali.
  - Hukuka uygun eşdeğer: bütün menşelere eşit ÖTV/KDV indirimi (takas).
- **On ürün grubunda takas (rejim c2).**
  - TÜFE 0 (pasif +47 bp); net mali −$0,60 mlr; +31 bin istihdam.
  - Yerliye özgü indirim −$3,75 mlr; üretim desteği −$4,6 mlr.
- **Aktif S4 (c2 + girdide sıfır + geniş takas).**
  - TÜFE 3,3 bp (pasif: 78); mali +%0,05 GSYH.
  - Net imalat istihdamı ≈ −35 bin (yalnızca MFN'de −117 bin); çekirdek giyim −59 bin.
- **Zaman kritik.** XXVIII:5 çekincesi 31.12.2026'dan önce. DS629 DSB toplantısı 27.10.2026. Mevcut DTÖ risklerinin temizlenmesi (%40 yerli katkı şartı, md. 32/7, rakı, 160 kW).

**Faz 2B — seçenekler (çekim modeli, PPML + GE)**
- **S4:**
  - AB'ye ihracat −%19 (GA −%32 ile −%5);
  - toplam ihracat −%6,2;
  - GSYH −%0,43. Sağlam ve alt sınır.
- **S2 (DCFTA):**
  - AB'ye ihracat −%11;
  - GSYH −%0,22;
  - GA sıfırı içeriyor. Dünya Bankası: −%3 ile −%7.
- **S3 (ITA):** −%18 ile +%1. Türkiye–BK geçişinde (2021) kayıp sıfır. Menşe tasarımı belirleyici.
- **Kısıtlar.** TÜFE ve mali kısıtlar her seçenekte tasarımla sağlanıyor. İstihdam kısıtı hiçbir çıkış seçeneğinde kendiliğinden sağlanmıyor.

**Öneri `[H]`**
- **Bitiş durumu:** S2, 2030–2031.
- **T2029:** ITA 1.1.2029'da geçici uygulamada. AB yetkisi Eylül 2027'ye kadar gerekli.
- **T2028:** çıkış kararı + Ortaklık Konseyi dondurma kararı; ITA 2029–2030'da. Ortaklık Konseyi GB'yi kaldıramaz; hukuki sona eriş ITA'yla olur (Şili md. 33.11).
- **Geri dönüş:** aktif S4. Pazarlık aracı; bitiş durumu değil.
- **Kapılar:** K1'de dondurma veya yetki yoksa T ertelenir.

**Hukuk**
- AB pozisyonu nitelikli çoğunlukla belirleniyor (md. 207, 218(9); C-81/13). Faz 0'daki oybirliği varsayımı düzeltildi.
- Yunanistan ve GKRY'nin hukuki vetosu yok; siyasi vetoları var. Belirleyici başkentler Berlin ve Roma.
- Risk: Görüş 1/26.
- Onaylanmış kuruluş sürekliliği (95 kayıt) dondurma kararına ve ITA'ya yazılmalı.

**Olasılıklar (kapılar işletilmeden)**
- T2028'de anlaşmasız çıkış %55–68.
- T2029'da %30–50.

**En büyük risk.** Kur: %10 değer kaybı ≈ +250 bp TÜFE.

**Defter.** 0/230 sınıf kartı; enflasyon bütçesi 0/50 bp. Faz 2 referans değerleri `defter.md`'de.

**Açık konular**
- Veri boşlukları: VB-02, 04, 06, 08–12, 14–17, 21–27.
- Faz 3: NACE sınıfı kartları. Öncelik: S4'te kaybı %5'i aşan 21 sınıf ve otomotiv, giyim, beyaz eşya platformları.

**Sonraki adım.** Faz 3: 230 C sınıfı ve ek kapsam için sınıf kartları. İki takvimde S3/S2 ve aktif S4 altında sınıf etkileri; destek tetikleyicileri.

---

## Kaynaklar (Faz 2B)

**AB–Türkiye hukuku**
- Ankara Anlaşması (CELEX 21964A1229(01)); Katma Protokol (21970A1123(01)); 1/95 sayılı Ortaklık Konseyi Kararı (21996D0213(01)); 1/98 ve 2/97 sayılı Kararlar; 1/2006 sayılı Ortaklık Konseyi Kararı.
- COM(2026) 477 (A.TR kurallarının PEM ile uyumu): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026PC0477
- C-81/13 İngiltere/Konsey: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62013CJ0081
- ABİDA md. 207, 212, 217, 218: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12016E218
- Türkiye–AB Üst Düzey Ticaret Diyaloğu Ortak Açıklaması, 13.10.2026 (STATEMENT/26/2135).
- DG TRADE Türkiye sayfası: https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/turkiye_en
- Avrupa Komisyonu, Türkiye 2025 Raporu, SWD(2025) 756.

**Emsal anlaşmalar**
- AB–Şili ITA ve Konsey Kararı 2023/2761: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202402953
- AB–Mercosur: Konsey Kararı 2026/183, https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202600183; Komisyon Mercosur sayfası; AP'nin görüş talebi (Görüş 1/26).
- AB–Meksika MGA ve iTA (22.5.2026).
- AB–Birleşik Krallık TCA: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:22021A0430(01); Karar 2021/689.
- AB–Ukrayna, Moldova, Gürcistan: Konsey Kararları 2014/492 ve 2014/494; Ortaklık Komitesi Kararı 3/2025.
- AB–İsviçre paketi (Konsey, 24.2.2026); MDCG AB–İsviçre MRA notu (2021).
- AB–İsrail ACAA (Karar 2013/1/AB).

**Menşe ve uyum değerlendirmesi**
- Revize PEM Sözleşmesi: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202400390; DG TAXUD PEM sayfası.
- Ortaklık Konseyi Kararı 1/2025 (tarım, PEM'e dinamik atıf): https://eur-lex.europa.eu/eli/dec/2026/1903/oj
- NANDO (Single Market Compliance Space), 18.10.2026; EA MAC kararları (TÜRKAK).
- Birleşik Krallık hükümeti, Büyük Britanya'da imal ürünlerin piyasaya arzı rehberi (CE/UKCA).

**AB'nin ticaret araçları**
- Uygulama Tüzüğü 654/2014 (2021/167 ile değişik); Zorlamaya Karşı Araç 2023/2675; Ticaret Engelleri Tüzüğü 2015/1843; Korunma Tüzüğü 2015/478.
- Çelik Tüzüğü 2026/1384 ve Uygulama Tüzüğü 2026/1457; SAFE Tüzüğü 2025/1106; Tüzük 2026/261 (Rus gazı).
- ACEA, AB–Türkiye araç ticareti, Temmuz 2026.

**DTÖ**
- GATT 1994 md. XXIV ve XXIV Mutabakatı: https://www.wto.org/english/docs_e/legal_e/10-24_e.htm
- Şeffaflık Mekanizması (WT/L/671); Analitik Endeks md. XXIV ve XXVIII.
- DS34 (Türkiye–Tekstil), DS629 (WT/DS629/R).

**Çekim modeli**
- Conte, Cotterlaz ve Mayer (2022), CEPII Gravity veri tabanı V202211.
- CEPII BACI HS17 V202601.
- Dür, Baccini ve Elsig (2014), DESTA v2.3 (2025).
- UN Ulusal Hesaplar Ana Toplamları.
- Yotov, Piermartini, Monteiro ve Larch (2016), *An Advanced Guide to Trade Policy Analysis: The Structural Gravity Model*, WTO/UNCTAD.
- Dünya Bankası (2014), *Evaluation of the EU–Turkey Customs Union*, Rapor 85830-TR.

**Türk mevzuatı**
- Anayasa md. 90; 4760, 3065, 4734, 5520 ve 7590 sayılı Kanunlar (https://www.mevzuat.gov.tr).
- 244, 474, 2976 ve 3577 sayılı Kanunlar `[D?]`.

---

İLERLEME: Faz 2 / 9 tamamlandı (02a + 02b) — SONRAKİ ADIM: Faz 3 (NACE sınıfı kartları); DEVAM bekleniyor.
