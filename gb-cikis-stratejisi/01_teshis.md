# Faz 1 — Teşhis: GB'nin 30 yıllık bilançosu, asimetriler ve makro tablo

**Durum:** Faz 1 / 9 tamamlandı (17 Ekim 2026); DEVAM bekleniyor. Önceki faz: [`00_plan.md`](00_plan.md). Defter: [`defter.md`](defter.md).

**Kanıt etiketleri** (ana prompt, "Kanıt etiketleri"):
- `[V]`: doğrulanmış veri; kaynak, tablo ve dönem yanında verilir.
- `[T]`: tahmin; yöntemi yazılır, mümkünse P10–P50–P90 aralığıyla.
- `[D?]`: doğrulanması gereken bilgi.
- `[H]`: hipotez veya uzman yargısı; gerekçesi yazılır.

Her çıkarımın yanında **Güven: Yüksek / Orta / Düşük** düzeyi verilir. Tablolarda kaynak ve etiket tablonun altında yer alır.

**Bu fazın veri ve kodu.** Bütün tablolar aşağıdaki betiklerle resmî kaynaklardan yeniden üretilir; sonuçlar `veri/teshis_*.csv` dosyalarındadır.

| Betik | İçerik | Kaynak |
|---|---|---|
| `kod/f1a_ab_ticaret.py` | Ticaret serisi, kompozisyon, sektör tarihçeleri | UN Comtrade (Türkiye beyanı), Eurostat Comext DS-045409 |
| `kod/f1b_odemeler_dengesi.py` | Ödemeler dengesi, GSYH, reel kur, AB27 hizmet ticareti | TCMB EVDS3 (anahtarsız arka uç, `kod/evds3.py`), TÜİK |
| `kod/f1c_sta_asimetrisi.py` | STA asimetrisi | CEPII BACI 2024, WITS/TRAINS |
| `kod/f1d_maruziyet.py` | NACE bölümü maruziyeti | TÜİK YSHİ 2024, Comtrade ve Comext 2025, S4 tarife duvarı |
| `kod/f1e_bolgesel.py` | İBBS-2 bölgeleri | SGK 2025 yıllığı, Tablo 1.11 |

Literatür, sektör ve hukuk bulguları Faz 1 araştırma ajanının birincil kaynak taramasından alındı (kaynakça sonda).

---

## Faz 1'in 12 ana bulgusu

1. **Ticaret on kat büyüdü; AB'nin payı düştü.**
   - Türkiye'nin AB27'ye ihracatı $11,3 mlr'dan (1995) $119,5 mlr'a (2025) çıktı: 10,6 kat, yılda %8,2.
   - Aynı dönemde AB dışı ihracat daha hızlı büyüdü: yılda %9,4.
   - AB27'nin payı ihracatta %52,3'ten %43,7'ye, ithalatta %45,4'ten %31,7'ye indi.
   - GB, Türkiye'yi tek pazara kilitlemedi; çeşitlenme GB içinde de gerçekleşti.
   - `[V]` Comtrade, Türkiye beyanı. Güven: Yüksek.
2. **1996'da ithalat şoku yaşandı.**
   - GB'nin ilk yılında AB27'den ithalat %32,2 arttı, dünya ithalatı %20,2.
   - AB27'ye ihracat yalnızca %1,4 arttı.
   - İkili açık $4,9 mlr'dan $10,0 mlr'a çıktı.
   - GB'nin ilk etkisi Türkiye pazarının açılması oldu; ihracat kazancı sonraki on yıla yayıldı.
   - `[V]` Güven: Yüksek.
3. **Kompozisyon tekstilden taşıtlara kaydı.**
   - AB27'ye ihracattaki paylar (1995 → 2025):
     - Tekstil ve giyim: %46,9 → %12,6.
     - Taşıtlar: %3,9 → %23,8.
     - Makine ve elektrikli cihazlar: %8,1 → %15,4.
     - Ana metaller: %5,5 → %13,2.
   - En çok AB'ye bağımlı hale gelen sektör otomotiv: bölüm 29 ihracatının %79'u AB'ye gidiyor.
   - `[V]` Güven: Yüksek.
4. **Literatür GB'nin etkisini pozitif ama sınırlı ve zamanla azalan buluyor.**
   - Tahminler geniş bir aralıkta: GSYH etkisi sıfırdan (çekim modelleri) +%0,72'ye (BKP 2016 CGE) ve kişi başı GSYH'de +%13'e (sentetik kontrol) kadar uzanıyor.
   - En güncel çekim çalışması etkinin ilk on yılda pozitif olup sonra kaybolduğunu buluyor (Dursun 2023).
   - `[V]` Güven: Orta.
5. **Ölçülebilir statik ticaret kalemlerinde GB'nin bilançosu Türkiye için pozitif.**
   - DTÖ/MFN karşı-olgusuna göre (S4):
     - Türk ihracatçıları yılda ≈€5,5 mlr AB gümrük vergisinden kaçınıyor (alt sınır: spesifik vergiler hariç).
     - Ayrıca menşe kuralı (rules of origin, RoO) maliyeti yok; DTÖ'ye göre gereksiz olduğu için bu kalem sayılmaz.
   - Derin STA karşı-olgusuna göre (S2): kazanç, menşe uyum maliyeti ile tercih kullanılamayan ticaretin vergisidir; yılda €2,4–6,7 mlr.
   - Çıkışın kaldırabileceği ölçülebilir maliyet daha küçük: STA asimetrisi nedeniyle ödenen vergi ≈$1,2 mlr/yıl. Bu da ancak Türkiye kendi STA'larını yaparsa kalkar.
   - Vize ve karayolu kotaları gerçek maliyetler, ancak GB'den bağımsız; çıkışla kalkmıyor.
   - Asıl maliyetler ölçülmesi zor kalemlerde: politika özerkliği ve stratejik dışlanma.
   - Sonuç: **çıkış, pazar erişimini bir anlaşmayla ikame etmeden yapılırsa net negatiftir.**
   - `[T]` Güven: Orta.
6. **STA asimetrisi büyüyor.**
   - Kapsam: AB'nin STA'sı olup Türkiye'nin olmadığı 22 pazar grubu (33 ülke).
   - Türk ihracatı yılda ≈$1,5 mlr MFN vergisi ödüyor; ağırlıklı ortalama %8,6.
   - Aynı pazarlarda AB ihracatçılarının tercih avantajı ≈$24,8 mlr (üst sınır). $6,5 mlr'ı Hindistan, Endonezya ve Avustralya anlaşmaları yürürlüğe girince eklenecek.
   - Bu ortaklardan Türkiye'nin ithalatı $30,2 mlr. Çıkış sonrası Türkiye'nin kendi STA'ları için en büyük kaldıraç bu.
   - `[T]` BACI 2024, WITS. Güven: Orta.
7. **Yönetişim ve dolaşım asimetrileri belgelenmiş durumda.**
   - Türk uzmanlar yalnızca 3 komiteye katılıyor ve oy hakları yok. `[V]` 1/95 Ek 9; 5/95.
   - Bağlayıcı bir uyuşmazlık çözüm mekanizması yok.
   - Vize: 2024'te 1,17 mn başvuru, ret oranı %14,5. `[V]` DG HOME.
   - Karayolu: transit ve ikili kotalar var. `[V]` ATAD C-65/16.
   - SAFE: Türkiye'nin katılımı engellendi (4.2.2026). `[V]`
   - ABD 301: Türkiye'ye %12,5 uygulanıyor, AB'ye uygulanan oran %10'la sınırlı. `[V]`
   - Güven: Yüksek.
8. **Cari açık enerji ve altından kaynaklanıyor.**
   - 2025: cari denge −$30,3 mlr (−%1,9 GSYH); altın ve enerji hariç çekirdek denge +$37,1 mlr (+%2,3).
   - Ağustos 2026'ya kadar 12 aylık birikimli: cari açık −$42,1 mlr, çekirdek +$26,0 mlr, enerji −$51,9 mlr.
   - Birincil gelir açığı (faiz ve doğrudan yatırım geliri) 2021'de $11,5 mlr iken 2025'te $23,4 mlr.
   - `[V]` EVDS3. Güven: Yüksek.
9. **Cari denge hedefinin önünde bir tasarruf-yatırım boşluğu var.**
   - Tasarruf-yatırım açığı kamu kesiminde: 2025'te −%1,9 GSYH, 2029'da −%2,2; özel kesim fazla veriyor. `[V]` OVP Tablo 1.1.
   - OVP'nin 2029 cari denge hedefi −%1,6.
   - T+5'te (2033/2034) cari denge ≥ %0 için ek iyileşme gerekiyor: $25–48 mlr `[H]`.
   - Ticaret önlemleri bu boşluğu ancak tasarruf-yatırım dengesini veya ihracat kapasitesini değiştirdikleri ölçüde kapatır (Lerner simetrisi).
   - Güven: Orta.
10. **Reel kur, emek yoğun ihracatı sıkıştırıyor.**
    - TÜFE bazlı reel efektif kur (2025 = 100) 2022'de 80,1 idi; 2026'nın ilk sekiz ayında 104,8. Reel değerlenme %31.
    - Bu ortamda AB'nin giyime uygulayacağı %11,9'luk MFN çifte darbe olur.
    - `[V]` TCMB. Güven: Yüksek.
11. **S4'ün ilk tur sinyalleri kısıtlarla çatışıyor.**
    - İhracat kaybı: −€21,2 mlr (σ = 5). P10–P90 aralığı −€13,8 ile −€30,4 mlr; 2028 GSYH'sinin ≈%1,1'i. `[T]`
    - İmalatta risk altındaki istihdam: 207 bin (P10–P90: 135–297 bin). En büyük paylar giyimde (87 bin) ve otomotivde (36 bin). `[T]`
    - AB mallarına MFN uygulanırsa TÜFE'ye birinci tur etki 32–53 bp (P50 42), İGV de eklenirse 59–98 bp (P50 78). Faz 2'deki girdi-çıktı modeliyle düzeltildi; ilk kaba hesap 21–40 ve 46–86 bp idi. `[T]`
    - Bölgesel yük orantısız: TRC3'te imalat istihdamının %9,8'i, TRB2'de %8,2'si risk altında.
    - Güven: Orta.
12. **Takvimlerin ikisinde de S4 kısıtlarla bağdaşmıyor.**
    - T2028 şunlarla çakışıyor:
      - 2028 seçimleri,
      - SKDM'nin mansap ürünlere genişlemesi (1.1.2028),
      - çelikte eritme-döküm kuralının kota tahsisinde kullanılmaya başlaması (1.10.2027),
      - TÜFE'nin %21'den %13,5'e indirilmeye çalışılması.
    - T2029 hazırlık için 12 ay daha kazandırıyor; ancak 2029'da tek haneli enflasyon (%9) hedefiyle çakışıyor.
    - Faz 2, S2/S3 ile bir geçiş düzenlemesini birlikte tasarlamak zorunda.
    - `[H]` Güven: Orta.

---

## 1. GB'nin 30 yıllık fayda-maliyet bilançosu (1996–2025)

### 1.1 Ticaret hacmi, AB payı ve ikili denge

| Yıl | TR ihracatı, dünya (mlr $) | AB27'ye ihracat (mlr $) | AB27 payı (%) | TR ithalatı, dünya (mlr $) | AB27'den ithalat (mlr $) | AB27 payı (%) | AB27 ile denge, TR verisi (mlr $) | AB'nin TR'den ithalatı (mlr €) | AB'nin TR'ye ihracatı (mlr €) | Denge, AB ayna verisi (mlr €) | TR'nin AB dışı ithalattaki payı (%) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1991 | 13,6 | 7,2 | 52,8 | 21,0 | 9,4 | 44,5 | -2,2 | — | — | — | — |
| 1995 | 21,6 | 11,3 | 52,3 | 35,7 | 16,2 | 45,4 | -4,9 | — | — | — | — |
| 1996 | 23,0 | 11,5 | 49,7 | 42,9 | 21,4 | 49,9 | -10,0 | — | — | — | — |
| 2000 | 27,8 | 13,9 | 50,1 | 54,5 | 25,8 | 47,4 | -11,9 | 16,3 | 28,8 | -12,5 | 1,7 |
| 2005 | 73,5 | 36,4 | 49,5 | 116,8 | 48,1 | 41,2 | -11,8 | 31,0 | 41,5 | -10,5 | 2,6 |
| 2008 | 132,0 | 56,6 | 42,9 | 202,0 | 69,3 | 34,3 | -12,7 | 40,7 | 51,4 | -10,7 | 2,6 |
| 2010 | 113,9 | 46,7 | 41,0 | 185,5 | 67,8 | 36,5 | -21,1 | 37,7 | 58,3 | -20,6 | 2,6 |
| 2013 | 161,5 | 59,4 | 36,8 | 260,8 | 90,4 | 34,6 | -30,9 | 44,1 | 72,6 | -28,5 | 2,7 |
| 2015 | 151,0 | 57,5 | 38,1 | 213,6 | 76,9 | 36,0 | -19,3 | 52,1 | 74,1 | -22,0 | 3,2 |
| 2018 | 177,2 | 78,7 | 44,4 | 231,2 | 77,1 | 33,4 | 1,5 | 66,9 | 69,2 | -2,3 | 3,5 |
| 2019 | 180,8 | 78,0 | 43,1 | 210,3 | 68,0 | 32,3 | 10,1 | 69,8 | 68,3 | 1,6 | 3,6 |
| 2020 | 169,7 | 70,9 | 41,8 | 219,5 | 73,4 | 33,5 | -2,5 | 62,5 | 70,1 | -7,7 | 3,6 |
| 2022 | 254,2 | 105,2 | 41,4 | 363,7 | 93,4 | 25,7 | 11,8 | 98,8 | 100,2 | -1,4 | 3,3 |
| 2024 | 261,8 | 111,1 | 42,4 | 344,0 | 110,5 | 32,1 | 0,6 | 98,1 | 113,2 | -15,2 | 4,0 |
| 2025 | 273,4 | 119,5 | 43,7 | 365,4 | 115,8 | 31,7 | 3,7 | 103,4 | 114,1 | -10,7 | 4,1 |

*Kaynak ve etiketler:*
- `[V]` UN Comtrade genel önizleme API'si, Türkiye beyanı, AB27 bugünkü üyelik, cari ABD doları. 1991–1992'de Çekoslovakya, 1999–2001'de Lüksemburg yok (küçük).
- `[V]` Eurostat Comext DS-045409, AB27_2020 × TR, avro. Bu seriler 1999'dan başlıyor. Son sütun Türkiye'nin AB27'nin AB dışı ithalatındaki payı.
- Tam yıllık seri `veri/teshis_ab_ticaret_1991_2025.csv` dosyasında.
- Güven: Yüksek.

**Okuma notları**
- **Büyüme dönemleri.** Türkiye'nin AB27'ye ihracatı ile dünya ihracatının yıllık büyümesi:

  | Dönem | AB27 (%/yıl) | Dünya (%/yıl) | Not |
  |---|---|---|---|
  | 1996–2005 | 13,7 | 13,7 | Eşit hız |
  | 2005–2015 | 4,7 | 7,5 | Avro krizi dönemi |
  | 2015–2025 | 7,6 | 6,1 | AB payı geri kazanıldı |

  Son dönemdeki toparlanmanın iki olası açıklaması var: 2018 sonrası reel kur kaybı ve yakın tedarik (nearshoring). `[V]` Hesap Comtrade serisinden; açıklama `[H]`.
- **İkili denge iki farklı ölçüyle iki farklı tablo veriyor.**

  | Ölçü | 2025 dengesi | Kaynak |
  |---|---|---|
  | Türkiye verisi | +$3,7 mlr fazla | İthalat menşe ülkeye göre |
  | AB ayna verisi | €10,7 mlr AB fazlası | AB ihracatı varış ülkesine göre |

  Farkın kaynakları:
  - Menşe ve gönderen ülke farkı: AB'den gönderilen üçüncü ülke menşeli mallar Türkiye verisinde menşe ülkeye yazılıyor.
  - Türkiye ihracatı FOB, AB ithalatı CIF.
  - Zamanlama.

  Müzakerede AB kendi rakamını kullanacak. Faz 7'nin argümanı iki ölçüyü birlikte vermeli. `[V]` Güven: Yüksek.
- **Birikimli açık.** Türkiye verisiyle 1996–2025 birikimli ikili mal açığı ≈$283 mlr. Açık 2011–2013'te yılda ≈$30 mlr ile zirve yaptı. 2018'den bu yana denge çoğunlukla Türkiye lehine. `[V]` Güven: Yüksek.
- **Türkiye'nin AB içindeki önemi arttı.** AB27'nin AB dışı ithalatındaki payı %1,9'dan (1999) %4,1'e (2025) çıktı. Türkiye, AB'nin ihracat pazarları arasında da yükseldi: AB'nin AB dışı ihracatındaki payı %4,3 (2025). Bu karşılıklı bağımlılık AB'nin pazarlık gücünü sınırlıyor, ama asimetrik: AB, Türkiye ihracatının %44'ünü alıyor; Türkiye ise AB'nin AB dışı ihracatının ≈%4'ünü. `[V]` Güven: Yüksek.

### 1.2 Kompozisyon: tekstilden taşıtlara

| HS bölümü | Ad | AB27'ye ihracattaki pay 1995 (%) | 2025 (%) | Fark (puan) | AB27'den ithalattaki pay 1995 (%) | 2025 (%) | AB27'nin bölüm ihracatındaki payı 2025 (%) |
|---|---|---|---|---|---|---|---|
| I | Canlı hayvanlar, hayvansal ürünler | 0,8 | 0,9 | 0,1 | 2,2 | 0,6 | 28,1 |
| II | Bitkisel ürünler | 10,3 | 3,1 | -7,2 | 1,4 | 1,3 | 30,4 |
| III | Hayvansal ve bitkisel yağlar | 0,9 | 0,1 | -0,8 | 1,2 | 0,1 | 5,4 |
| IV | Gıda, içecek, tütün | 5,8 | 3,2 | -2,6 | 1,4 | 3,0 | 27,6 |
| V | Mineral ürünler ve enerji | 4,4 | 8,4 | 4,0 | 1,8 | 2,0 | 48,1 |
| VI | Kimya ve ilaç | 2,8 | 3,7 | 0,9 | 14,6 | 11,1 | 28,3 |
| VII | Plastik ve kauçuk | 2,3 | 6,1 | 3,8 | 7,2 | 6,9 | 47,9 |
| VIII | Deri ve kürk | 3,6 | 0,3 | -3,3 | 1,6 | 0,4 | 43,4 |
| IX | Ağaç ve mantar | 0,2 | 0,3 | 0,1 | 0,4 | 0,2 | 19,2 |
| X | Kâğıt ve basılı ürünler | 0,5 | 0,8 | 0,4 | 2,9 | 2,1 | 32,7 |
| XI | Tekstil ve hazır giyim | 46,9 | 12,6 | -34,4 | 5,2 | 2,2 | 48,7 |
| XII | Ayakkabı ve şapka | 0,5 | 0,4 | -0,1 | 0,1 | 0,3 | 40,4 |
| XIII | Taş, seramik, cam | 2,5 | 1,6 | -0,9 | 1,3 | 0,9 | 37,3 |
| XIV | Kıymetli taşlar ve metaller | 0,4 | 1,6 | 1,2 | 0,1 | 3,0 | 13,9 |
| XV | Ana metaller ve ürünleri | 5,5 | 13,2 | 7,6 | 14,5 | 11,6 | 49,3 |
| XVI | Makine ve elektrikli cihazlar | 8,1 | 15,4 | 7,3 | 30,7 | 23,7 | 42,1 |
| XVII | Taşıtlar | 3,9 | 23,8 | 20,0 | 9,6 | 26,5 | 65,6 |
| XVIII | Optik, ölçü ve tıbbi cihazlar | 0,2 | 0,7 | 0,5 | 2,6 | 2,8 | 38,3 |
| XIX | Silah ve mühimmat | 0,1 | 1,8 | 1,7 | 0,2 | 0,2 | 44,8 |
| XX | Çeşitli mamul eşya | 0,5 | 2,1 | 1,6 | 0,9 | 1,0 | 38,0 |

*Kaynak ve etiketler:*
- `[V]` Comtrade, Türkiye beyanı, HS fasıllarından bölümlere toplandı.
- 1995 verisi HS1992, 2025 verisi HS2022 sınıflamasında; bölüm düzeyinde karşılaştırılabilir.
- Fasıl ayrıntısı ve Comext 1999–2025 serisi `veri/teshis_ab_ticaret_fasil.csv` dosyasında.
- Güven: Yüksek.

**Okuma notları**
- **Değer zinciri dönüşümü.** 30 yılda AB'ye ihracatın ağırlık merkezi değişti:
  - emek yoğun tekstil-giyim ve tarımdan,
  - orta teknolojili taşıtlar, makine, metal ve plastiğe.
  - OVP'ye göre orta ve yüksek teknolojili ürünlerin toplam ihracattaki payı Ağustos 2026'da %44,1 `[V]`.
- **AB'ye bağımlılık sektörden sektöre değişiyor.**
  - Taşıtlarda AB27, Türkiye'nin bölüm ihracatının %65,6'sını alıyor.
  - Ana metaller, tekstil-giyim, plastik ve mineral ürünlerde yaklaşık yarısını.
  - Gıda, ağaç ve kıymetli metallerde %14–31'ini.

  Maruziyet ve dolayısıyla çıkış riski en çok taşıtlarda. `[V]` Güven: Yüksek.
- **İthalatta da taşıtlar öne çıktı.** Taşıtların AB27'den ithalattaki payı %9,6'dan %26,5'e çıktı: otomobil ithalatı ve otomotiv parça ticareti. Bu, iki yönlü bir değer zinciri entegrasyonunu gösteriyor. Tek yönlü bir tarife şoku iki yönü birden keser. `[V]` Güven: Yüksek.

### 1.3 Sektör tarihçeleri

| Sektör | TR→AB 1999 (mn €) | 2005 | 2015 | 2025 | AB→TR 2025 (mn €) | Denge 1999 (mn €) | Denge 2025 (mn €) |
|---|---|---|---|---|---|---|---|
| Motorlu taşıtlar ve parçaları (HS 87) | 985 | 5.629 | 10.858 | 24.539 | 25.469 | -1.036 | -930 |
| Beyaz eşya (HS 8418, 8422, 8450, 8451, 8516) | 192 | 857 | 2.092 | 2.992 | 1.469 | -208 | 1.522 |
| Makine (HS 84) | 612 | 2.424 | 5.804 | 10.881 | 18.839 | -2.984 | -7.958 |
| Elektrikli cihazlar (HS 85) | 1.106 | 2.666 | 3.152 | 6.455 | 9.809 | -2.023 | -3.354 |
| Hazır giyim (HS 61–62) | 4.055 | 6.238 | 7.787 | 8.357 | 1.851 | 3.922 | 6.506 |
| Tekstil (HS 50–60, 63) | 1.723 | 3.062 | 4.318 | 4.613 | 1.711 | 590 | 2.902 |
| Demir-çelik ve ürünleri (HS 72–73) | 689 | 1.969 | 2.658 | 8.280 | 7.107 | -261 | 1.173 |
| Plastik ve kauçuk (HS 39–40) | 379 | 1.140 | 3.158 | 6.715 | 6.992 | -936 | -277 |
| Kimya ve ilaç (HS 28–38) | 286 | 560 | 1.383 | 3.543 | 12.320 | -2.103 | -8.777 |
| Gıda ve tarım (HS 01–24) | 1.942 | 2.903 | 4.844 | 7.569 | 5.702 | 1.352 | 1.867 |

*Kaynak:* `[V]` Comext DS-045409. "TR→AB" AB'nin Türkiye'den ithalatıdır. Güven: Yüksek.

**Otomotiv: GB'nin en büyük başarısı ve en büyük maruziyeti**
- Başlangıç noktası:
  - 1995 binek otomobil üretimi 223.414 adetti; kapasite kullanımı %47.
  - Otomobil ithalat vergileri 1989'da %72–150, 1993'te %39'du.
  - GB'yle AB'den ithalatta gümrük vergisi kalktı; vergi yükü tüketim vergisine kaydırıldı ve ikinci el araç ithalatı beş yıl yasaklandı.
  - `[V]` Duruiz, GERPISA (≈1996).
- 2025:
  - Üretim 1.419.464 araç; kapasite kullanımı %67.
  - İhracat 1.057.920 adet ve $41,5 mlr; Türkiye ihracatının %17,5'i.
  - Otomotiv ihracatının %72,5'i ($30,1 mlr) AB'ye gitti.
  - `[V]` OSD verisi, basın aktarımı; AB payı `[D?]` OİB/AA.
- AB tarafının verisi (ACEA, Temmuz 2026):
  - AB, 2025'te Türkiye'den 797.721 yeni araç (€18,2 mlr, +%18,5) ithal etti. Bu, AB'nin yeni araç ithalatının değer olarak %21,5'i.
  - AB, Türkiye'ye 811.957 araç (€18,8 mlr) ihraç etti. Türkiye, AB'nin üçüncü büyük araç ihracat pazarı.
  - `[V]`
- Sektör, iki yönlü bir AB değer zincirinin parçası; 2025'te HS 87 dengesi −€0,9 mlr.
- Çapa yatırımcılar (anchor investors) AB merkezli veya AB pazarına odaklı: Oyak-Renault, Tofaş (Stellantis), Ford Otosan, Toyota, Hyundai, Mercedes-Benz Türk, MAN.
- Bu yüzden S4'te AB'nin %10–22'lik otomotiv tarifesi, yatırımcıların yeniden konumlanma riskini doğrudan tetikler (kaçınılacak hata 5).

**Beyaz eşya**
- AB'ye ihracat €0,19 mlr'dan (1999) €3,0 mlr'a (2025) çıktı; Türkiye bu sektörde 2005'ten beri fazla veriyor. `[V]`
- 2025 (TÜRKBESD):
  - Üretim −%9.
  - İhracat 20,2 mn adet (−%10, 2017 düzeyi); üretimin ≈%70'i ihraç ediliyor.
  - TÜRKBESD Türkiye'yi "Avrupa'da birinci, dünyada ikinci" üretim merkezi olarak tanımlıyor.
  - `[V]` basın aktarımı.
- AB tarifeleri düşük: buzdolabında %1,5–2,5, çamaşır makinesinde %2,2–3 (Faz 0 H-6). S4'teki tarife şoku küçük kalır; asıl risk menşe ve çapa yatırımcı kararlarında.

**Hazır giyim ve tekstil**
- Kota rejiminin (ÇEA/MFA) 1.1.2005'te kalkmasından sonra Türkiye'nin AB'nin AB dışı giyim ithalatındaki payı:

  | Dönem | Pay | Etiket |
  |---|---|---|
  | 2005 | ≈%14–15 | `[D?]` Eurostat SiF 2007 ve basın |
  | 2024 | %10,8 (€10,4 mlr; Çin %29,6, Bangladeş %19,2) | `[V]` İHKİB, Eurostat verisi |
  | Ocak–Ekim 2025 | %9,2 (−%10,6) | `[V]` |

- 2025'te giyim ihracatı $16,8 mlr (−%6,4); %59,6'sı AB'ye.
- Giyim, GB'nin rekabet avantajını en hızlı kaybeden sektör. AB'nin MFN tarifesi %12, Asya rakipleri ise GSP ve EBA tercihleriyle sıfırda. Bu nedenle sektör S4'e en duyarlı sektör (bkz. §4).

**Demir-çelik**
- Çelik GB değil, 1996 AKÇT STA'sı kapsamında (kaçınılacak hata 16).
- AB'ye ihracat €0,7 mlr'dan €8,3 mlr'a çıktı.
- Asıl kısıt artık AB'nin kota rejimi (Tüzük 2026/1384; TRQ −%47, kota dışı vergi %50) ve SKDM (Faz 0 D-3, D-5). GB'den çıkış AKÇT STA'sını kendiliğinden sona erdirmez.

**Kimya ve makine**
- Kalıcı açık veren alanlar:
  - kimya ve ilaç: −€8,8 mlr,
  - makine: −€8,0 mlr,
  - elektrikli cihazlar: −€3,4 mlr.
- Bu kalemler GB'den çıkışta Türkiye'nin ithalat tarafındaki girdi maliyetinin merkezinde. "Girdide serbest" ilkesinin (temel ilke 6) en büyük uygulama alanı burası.

### 1.4 Doğrudan yatırım

- **Akım.**
  - Doğrudan yatırım yükümlülükleri (net yükümlülük oluşumu) 2025'te $12,9 mlr; bunun $2,3 mlr'ı gayrimenkul.
  - 2010–2025 ortalaması ≈$12,7 mlr/yıl; GSYH'nin ≈%0,8'i.
  - `[V]` EVDS3 TP.ODEAYRSUNUM6.Q108 ve Q113.
- **Stok.** Doğrudan yatırım yükümlülüğü stoku 2025 sonunda $230,1 mlr. Türkiye'nin net uluslararası yatırım pozisyonu −$349,3 mlr. `[V]` EVDS3, Uluslararası Yatırım Pozisyonu.
- **AB'nin payı.**
  - 2003–2024 birikimli girişlerin %58'i AB27'den. 2025'in ilk dokuz ayında %64; bunun %32'si Hollanda, %14'ü Lüksemburg, %7'si Almanya. `[D?]` YASED, TCMB verisi.
  - AB'nin Türkiye'deki doğrudan yatırım stoku €50,4 mlr (2022). `[V]` Eurostat, EEAS aktarımı.
  - Hollanda ve Lüksemburg'un ağırlığı aracı (geçiş) yatırımı da yansıtıyor; nihai yatırımcı ülkeye göre dağılım ayrıca gerekli (VB-14).
- **Yabancı sermayeli firmalar.**
  - 2025'te AB'ye $46,4 mlr ihracat yaptılar: Türkiye'nin AB27'ye ihracatının ≈%39'u. Bu firmalar Türkiye'nin toplam ihracatının ≈%30'unu yapıyor.
  - `[V]` Ticaret Bakanlığı, basın aktarımı. Oran `[T]`.
  - Bu yüzden AB pazarına erişimdeki bir kayıp, doğrudan yatırımın en hareketli kısmını (ihracat platformu yatırımlarını) etkiler.
- **Literatür.** BKP (2016), GB'nin ikili doğrudan yatırıma "güçlü pozitif" etkisini buluyor; ancak verinin zayıf olduğunu ve 2001 reformlarından önce toplam doğrudan yatırım girişine etki görülmediğini not ediyor. `[V]` Güven: Orta.

### 1.5 Mali etki

- **Vazgeçilen gümrük geliri.**
  - 2025 AB ithalatına 2026 MFN oranları uygulansaydı tahsil edilecek vergi:

    | Varyant | Tutar | GSYH'ye oranı |
    |---|---|---|
    | İGV hariç | €4,9 mlr | %0,35 |
    | İGV dahil | €10,7 mlr | %0,75 |

  - Bu bir transferdir: tüketiciler ve AB girdisi kullanan üreticiler vergiyi ödememiş olur. Refah kaybı değil, mali bir kalemdir.
  - `[T]` statik; `veri/s4_tarife_duvari_ozet.csv`. Güven: Orta.
- **1996'daki beklenti.** Gelir kaybının GSYH'nin ≈%1,4'ü, refah kazancının yılda GSYH'nin %1–1,5'i olacağı tahmin ediliyordu. `[D?]` Harrison, Rutherford ve Tarr (1996/97).
- **Bugünkü büyüklük.**
  - 2025 bütçesinde gümrük vergisi hedefi 339,9 mlr TL; vergi gelirlerinin ≈%3,1'i. `[D?]` Bu bütçe hedefidir, gerçekleşme değildir; gerçekleşme rakamı "diğer vergiler" içinde.
  - İthalde alınan KDV 1.724,2 mlr TL; vergi gelirlerinin %15,6'sı. `[V]` HMB Aralık 2025 bütçe raporu.
  - İthalde KDV menşeden bağımsızdır; GB'den çıkış onu değiştirmez.
- **Sonuç.** GB'den çıkış ve AB mallarına MFN uygulanması, gümrük gelirine €4,9–10,7 mlr ekleyebilir. Ancak bu gelir ancak enflasyon bütçesini aşma pahasına elde edilir (§5). "Ek gümrük geliri" mali kısıtı rahatlatan bir kaynak olarak planlanmamalı. `[T]` Güven: Orta.

### 1.6 Teknik uyum, kurumlar ve yönetişim

- **Karar şekillendirme.** 1/95 sayılı Kararın Ek 9'u Türk uzmanların katılabileceği yalnızca üç komiteyi sayıyor: Nomenklatür, Gümrük Kodu ve Dış Ticaret İstatistikleri (md. 60). 5/95 sayılı Karar her komitede oy hakkı olmayan bir Türk hükûmet uzmanı öngörüyor; uzmanın görüşü ayrıca kaydediliyor. `[V]` CELEX 21996D0213(01).
- **Uygulama (BKP 2016).** `[V]`
  - GB Ortak Komitesi'nin ayda bir toplanması öngörülmüştü; yılda 3–4 kez toplanıyor.
  - Türk yetkililer danışmanın "öngörüldüğü gibi işlemediğini" söylüyor ve bir "bildirim açığı"ndan söz ediyor.
  - Komisyon 2014'ten beri yıllık mevzuat listesi veriyor.
- **Teknik mevzuat.**
  - Türkiye, 2/97 sayılı Kararda listelenen teknik engeller (TBT) mevzuatının "çoğunluğunu" iç hukukuna aktardı. `[V]` BKP. Aktarılan mevzuat sayısı doğrulanamadı (VB-18).
  - GB dışında üç konu belirleyici olacak:
    - CE işareti,
    - Türk onaylanmış kuruluşlarının (notified bodies) NANDO bildirimleri,
    - TÜRKAK'ın Avrupa Akreditasyon Birliği (EA) çok taraflı tanıma anlaşmasındaki (MLA) yeri.
  - Bu kurumsal çerçeve yeniden kurulmazsa İngiltere'nin UKCA deneyimine benzer bir uyum maliyeti doğar. Ayrıntılı analiz Faz 2'de (hukuki yol) ve Faz 5'te (yatay araçlar) yapılacak (kaçınılacak hata 11). `[D?]`
- **Menşe ve transit.**
  - GB kapsamındaki mallarda dolaşım A.TR belgesiyle sağlanıyor; menşe ispatı gerekmiyor.
  - Türkiye, revize PEM kurallarını AB ile tarım ve AKÇT ticaretinde 1.1.2026'dan beri uyguluyor (Faz 0 H-2).
  - Ortak Transit Sözleşmesi ve NCTS üyeliği GB'den bağımsız (Faz 0 H-9).
  - Çıkışta A.TR'den PEM menşe ispatına geçiş için altyapı mevcut. Asıl yük KOBİ'lerin menşe hesabı ve tedarikçi beyanları olacak (kaçınılacak hata 3 ve 18).

### 1.7 Ampirik literatür

| Çalışma | Yöntem ve dönem | Bulgu | Etiket |
|---|---|---|---|
| Aytuğ, Mavuş Kütük, Oduncu ve Togan (2017), *JCMS* 55(3) | Sentetik kontrol | GB olmasaydı AB'ye ihracat %38, kişi başı GSYH %13 daha düşük olurdu | `[V]` özet |
| Antonucci ve Manzocchi (2006), *Economic Systems* 30(2) | Çekim modeli, 1967–2001 | Ortaklık Anlaşması'nın ve GB'nin ek ticaret yarattığına dair kanıt yok | `[V]` özet |
| Neyaptı, Taşkın ve Üngör (2007), *Applied Economics* 39(16) | Öncesi-sonrası, makro kontroller | İhracat ve ithalata pozitif etki; esneklikler değişti | `[V]` özet; büyüklük yok |
| Nowak-Lehmann ve diğ. (2007), *JCMS* 45(3) | Genişletilmiş çekim, 16 sektör, 1988–2002 | Tarım ve çeliğin GB'ye eklenmesinin simülasyonu | `[D?]` bulgular alınamadı |
| Adam ve Moutos (2008), *World Economy* 31(5) | Çekim modeli | GB, düşük teknolojili "Güney" AB-15 ihracatını dışladı; "Kuzey" etkilenmedi | `[V]` |
| Yılmaz (2010), Koç-TÜSİAD ERF WP 1023 | Firma ve sektör verimliliği | İthalat rekabeti şokuyla imalat verimliliği arttı; genel etki pozitif | `[V]` |
| Dünya Bankası (2014), Rapor 85830-TR | Çekim modeli, 1990–2010; senaryolar | İkili ticarete anlamlı etki yok, küresel entegrasyona katkı var. GB yerine menşe kurallı STA: Türkiye'nin AB'ye ihracatı %3,0–7,2 daha düşük | `[V]` |
| BKP/Panteia/AESA (2016), DG TRADE için, SWD(2016) 475 Ek 6 | Geçmişe dönük CGE + çekim | Türkiye: GSYH +%0,72, refah +€7,5 mlr. AB: GSYH +%0,008, refah +€1,6 mlr. İkili ihracat GB'siz duruma göre ≈%7, ithalat ≈%9 daha yüksek. Ana kanal menşe maliyetinin olmaması (varsayım %2). Tekstil pay kaybetti, taşıtlar kazandı | `[V]` |
| ifo, Bertelsmann için (2016) | İleriye dönük CGE | GB'nin sona ermesi: Türkiye GSYH −%0,81; AB'nin TTIP benzeri bir anlaşmasıyla ek −%0,96. GB'nin tarım ve hizmetlere genişlemesi: +%1,84 | `[V]` |
| Dursun (2023), *International Economics* 173 | Çekim, toplam ve 69 ürün grubu | Bütün dönemde anlamlı etki yok; ilk on yılda pozitif, sonra kayboluyor. Pozitif ürün grupları çoğunlukla AB ihracatı lehine; GB kararının içselliği (endogeneity) | `[V]` özet |
| Harrison ve diğ. (1996); Francois ve diğ. (2005); Demirci ve Aydın (2011) | İleriye dönük CGE | GSYH +%1,0–1,5; +%1,3; +%4,87 | `[V]` BKP s. 23 aktarımı |

**Sentez.**
- Türkiye için GB'nin GSYH etkisi:
  - geçmişe dönük model tahmini: +%0,7 (BKP),
  - çekim modellerinde anlamsız ile pozitif arasında,
  - tek sentetik kontrol çalışmasında yüksek (+%13).
- Etki büyük ölçüde ilk on yılda gerçekleşmiş ve zamanla azalmış görünüyor.
- Çıkışın maliyetine ilişkin iki doğrudan tahmin:
  - ifo: GSYH −%0,81;
  - Dünya Bankası: STA'ya geçişte AB'ye ihracat −%3,0–7,2.
- Türk ve Avrupa düşünce kuruluşlarında 2017–2026 arasında sayısal bir çıkış çalışması yok (Faz 0 E-6): **kanıt boşluğu**.
- Bu boşluk Faz 2'de kendi yapısal çekim modelimizle doldurulacak (VB-13). Model: PPML, BACI 1996–2024, ihracatçı-yıl, ithalatçı-yıl ve ikili sabit etkiler.
- Güven: Orta.

### 1.8 Bilanço tablosu

İki karşı-olgu ayrı ayrı gösterilir: (a) DTÖ/MFN (S4) ve (b) derin STA (S2). Tutarlar yıllıktır ve 2025 ticareti ile 2026 tarifelerine dayanır.

| No | Kalem | Yön | (a) S4'e göre (yıllık) | (b) S2'ye göre (yıllık) | Etiket ve yöntem | Güven |
|---|---|---|---|---|---|---|
| F-1 | AB pazarına vergisiz erişim (GB + İTÜ, €93,4 mlr ihracat) | Fayda | €5,5 mlr vergi kaçınımı (ortalama %5,85) | Tercih kullanılmayan ticaretin vergisi: €0,5–1,1 mlr (kullanım oranı %80–90 varsayımıyla) | `[T]` statik; spesifik vergiler hariç (alt sınır). Kullanım oranı İngiltere–AB deneyiminden (Faz 0 V-20) | Orta |
| F-2 | Menşe kuralı maliyetinin olmaması (A.TR) | Fayda | — (MFN'de menşe gerekmez) | €1,9–5,6 mlr; P50 €2,8 mlr (%2–6, P50 %3) | `[T]` Dünya Bankası 2014, BKP 2016 aralığı | Orta |
| F-3 | Değer zinciri entegrasyonu ve ihracat hacmi | Fayda | Statik ihracat kaybından kaçınma: €13,8 / 21,2 / 30,4 mlr (σ = 3/5/8) | Sınırlı | `[T]` kısmi denge (Faz 0 S4 hesabı) | Orta |
| F-4 | AB ithalatında düşük maliyet (tüketici ve üretici) | Fayda (transfer) | €4,9 mlr (İGV hariç) – €10,7 mlr (İGV dahil) vergi ödenmiyor | Aynı (STA'da da sıfır) | `[T]` statik | Orta |
| F-5 | Kurumsal ve teknik yükseltme (TBT, standartlar, rekabet hukuku) | Fayda | Ölçülmedi | Kısmen korunur | `[H]` literatür (Yılmaz 2010) | Düşük |
| M-1 | Vazgeçilen gümrük geliri | Maliyet (mali) | €4,9–10,7 mlr (GSYH'nin %0,35–0,75'i) | Aynı | `[T]`; F-4'ün mali karşılığı | Orta |
| M-2 | STA asimetrisi: AB'nin STA ortaklarında Türk ihracatının ödediği MFN | Maliyet | $1,2 mlr; tamamlanan anlaşmalarla $1,5 mlr | Aynı (yalnızca Türkiye kendi STA'larını yaparsa kalkar) | `[T]` §2.1 | Orta |
| M-3 | STA asimetrisi: AB rakiplerinin tercih avantajı (pazar payı kaybı) | Maliyet (potansiyel) | $18,2 mlr AB ihracatına uygulanmayan vergi; Türkiye'nin kaybettiği pay ölçülmedi | Aynı | `[T]` üst sınır | Düşük |
| M-4 | Ticaret politikası özerkliği: girdi tarifelerini OGT'nin altına indirememe, kendi STA'larını yapamama | Maliyet (opsiyon değeri) | Faz 5'te ölçülecek ("özerklik temettüsü") | Aynı | `[H]` | Düşük |
| M-5 | Karar alma dışlanması ve bildirim açığı | Maliyet | Ölçülmedi | Aynı | `[V]` nitel (§1.6) | Yüksek (nitel) |
| M-6 | Vize | Maliyet | ≈€114 mn konsolosluk ücreti (1,27 mn başvuru × €90); aracı kurum ücretleri ve zaman maliyeti hariç | Aynı | `[T]`; başvuru sayısı `[D?]` (2025, basın) | Orta |
| M-7 | Karayolu kotaları ve transit | Maliyet | 2005–2012'de karayoluyla taşınan ihracatta ≈$10,6 mlr birikimli kayıp | Aynı | `[D?]` çekim çalışması (2014) | Düşük |
| M-8 | AB'nin yeni araçlarından dışlanma (SAFE, IAA karşılıklılığı, SKDM'de muafiyet yok) | Maliyet (artıyor) | Faz 3–4'te sınıf bazında | Aynı | `[V]` nitel (Faz 0 D-3, D-7) | Orta |

**Net değerlendirme.**
- *S4'e göre:* ölçülebilir fayda (F-1 ve F-3) yılda €5,5 mlr vergi ile €14–30 mlr statik ihracat hacmi.
  - Çıkışın kaldırabileceği ölçülebilir maliyet yalnızca M-2: $1,2–1,5 mlr/yıl, o da ancak Türkiye kendi STA'larını yaparsa.
  - M-6 (vize, ≈€0,1 mlr) ve M-7 (karayolu kotaları, ≈$1,3 mlr/yıl ihracat kaybı) GB'den bağımsız; çıkışla kalkmıyor.
  - **GB, anlaşmasız çıkışa göre açık ara üstün.** `[T]` Güven: Yüksek.
- *S2'ye göre:* GB'nin üstünlüğü menşe maliyeti ve tercih kullanım açığıyla sınırlı, yılda €2,4–6,7 mlr. Buna karşılık çıkış şu kazanımları sağlayabilir:
  - özerklik temettüsü: girdi tarifelerini düşürme, kendi STA'ları;
  - STA asimetrisinin giderilmesi: $1,2–1,5 mlr doğrudan vergi ve pazar payı;
  - AB'nin yeni araçlarına karşı esneklik.
- Bu kazanımlar menşe maliyetini karşılayabilir; ancak ölçümü Faz 2 ve Faz 5'e kaldı. Bu nedenle **S0 ile S2 karşılaştırması bugünkü veriyle başa baş ile hafif negatif arasında** (−€6,7 mlr ile +€2 mlr). `[T]` Güven: Düşük.

### 1.9 Teşhis sonucu

1. GB'nin ölçülebilir statik bilançosu Türkiye için pozitif. Bu pozitiflik büyük ölçüde AB pazarına menşe kuralsız ve vergisiz erişimden kaynaklanıyor.
2. Çıkışın kendisi bir fayda üretmez. Fayda ancak üç koşulla mümkün:
   - pazar erişimi derin bir STA ile korunur (S2/S3);
   - menşe maliyeti tam kümülasyon, PEM ve tolerans tasarımıyla düşürülür;
   - özerklik temettüsü (girdi tarifelerinde indirim, kendi STA ağı) fiilen elde edilir.
3. Kullanıcı kararıyla çıkış yönü veri (V-28). Bu durumda strateji S4'ten kaçınmak üzerine kurulmalı. S4 bütün kısıtları zorluyor (§5).
4. AB hasmane olduğu için (V-11) S4'ün olasılığı yüksek (Faz 0: T2028'de %45–70, T2029'da %25–45). Dolayısıyla Faz 2'nin ana görevi, AB'yi S2/S3'e çekecek pazarlık paketini ve S4'e düşülürse zararı sınırlayacak tek taraflı tampon paketini birlikte tasarlamak.
5. Bu bulgu stratejinin yönünü değiştirmiyor; tasarım koşullarını belirliyor. `[H]` Güven: Orta.

---

## 2. Mevcut asimetriler

### 2.1 STA asimetrisi

AB'nin STA'sı olup Türkiye'nin STA'sı olmayan pazarlar aşağıda. Türkiye–Ukrayna STA'sının 1.10.2026'da yürürlüğe girdiği bildiriliyor (Faz 0 §6.7, `[D?]`); Ukrayna bu yüzden tabloda yok.

| Ortak | AB anlaşması (yürürlük) | Durum | TR ihracatı 2024 (mn $) | TR'nin ödediği MFN vergisi (mn $) | Ağırlıklı MFN (%) | TR pazar payı (%) | AB27 ihracatı (mn $) | AB27 pazar payı (%) | AB'nin tercih avantajı, üst sınır (mn $) | TR'nin bu ortaktan ithalatı (mn $) |
|---|---|---|---|---|---|---|---|---|---|---|
| Meksika | Küresel Anlaşma (STA) (2000) | yürürlükte | 1.391 | 100 | 7,2 | 0,25 | 54.913 | 9,8 | 3.053 | 1.185 |
| Kanada | CETA (2017) | geçici uygulamada | 1.944 | 69 | 3,5 | 0,37 | 57.026 | 10,7 | 936 | 1.251 |
| Japonya | EPA (2019) | yürürlükte | 746 | 30 | 4,0 | 0,10 | 75.516 | 10,5 | 1.332 | 4.489 |
| Vietnam | EVFTA (2020) | yürürlükte (geçiş takvimi 2030'a kadar) | 407 | 31 | 7,6 | 0,11 | 12.141 | 3,2 | 651 | 2.976 |
| Cezayir | Ortaklık Anlaşması (2005) | yürürlükte (Cezayir'in kısıtlamaları var) | 2.871 | 389 | 13,5 | 6,58 | 16.027 | 36,7 | 1.972 | 1.472 |
| GAGB (SACU) | SADC EPA (2016) | yürürlükte | 749 | 61 | 8,2 | 0,74 | 21.517 | 21,3 | 1.237 | 963 |
| Mozambik | SADC EPA (2018) | yürürlükte (asimetrik) | 99 | 14 | 14,2 | 0,60 | 1.245 | 7,6 | 72 | 56 |
| Kolombiya | Ticaret Anlaşması (2013) | yürürlükte | 302 | 25 | 8,4 | 0,48 | 8.598 | 13,7 | 509 | 821 |
| Peru | Ticaret Anlaşması (2013) | yürürlükte | 332 | 5 | 1,4 | 0,62 | 4.949 | 9,2 | 78 | 319 |
| Ekvador | Ticaret Anlaşması (2017) | yürürlükte | 121 | 6 | 4,7 | 0,41 | 3.545 | 12,0 | 179 | 167 |
| Orta Amerika | Ortaklık Anlaşması (2013) | yürürlükte | 657 | 43 | 6,6 | 0,46 | 11.723 | 8,2 | 426 | 330 |
| Yeni Zelanda | STA (2024) | yürürlükte | 192 | 6 | 3,4 | 0,41 | 6.561 | 14,0 | 166 | 56 |
| Kenya | EPA (2024) | yürürlükte (25 yıllık asimetrik takvim) | 282 | 40 | 14,1 | 1,19 | 2.093 | 8,9 | 124 | 17 |
| CARIFORUM | EPA (2008) | geçici uygulamada (asimetrik) | 462 | 46 | 10,0 | 0,99 | 5.178 | 11,1 | 488 | 105 |
| Fildişi Sahili | Ara EPA (2016) | yürürlükte (asimetrik) | 309 | 32 | 10,4 | 1,66 | 4.383 | 23,5 | 352 | 505 |
| Gana | Ara EPA (2016) | yürürlükte (asimetrik) | 399 | 57 | 14,3 | 1,96 | 3.497 | 17,1 | 272 | 173 |
| Kamerun | Ara EPA (2014) | yürürlükte (asimetrik) | 195 | 34 | 17,6 | 2,36 | 1.915 | 23,2 | 240 | 95 |
| Doğu ve Güney Afrika (ESA) | Ara EPA (2012) | yürürlükte (asimetrik) | 94 | 7 | 8,0 | 0,64 | 1.165 | 7,9 | 74 | 43 |
| Mercosur | Geçici Ticaret Anlaşması (2026) | geçici uygulamada (1.5.2026'dan) | 1.634 | 198 | 12,1 | 0,45 | 59.495 | 16,3 | 6.086 | 5.014 |
| Hindistan | STA (—) | müzakere tamamlandı (27.1.2026); imza önerisi 11.9.2026 | 2.667 | 240 | 9,0 | 0,39 | 50.480 | 7,3 | 4.625 | 6.780 |
| Endonezya | CEPA (—) | sonuçlandı (2025); Konsey'e sunuldu 29.6.2026 | 482 | 27 | 5,5 | 0,21 | 12.192 | 5,3 | 794 | 2.363 |
| Avustralya | STA (—) | müzakere tamamlandı (24.3.2026) | 1.251 | 49 | 3,9 | 0,44 | 42.727 | 14,9 | 1.124 | 1.058 |
| **Toplam: yürürlükte veya geçici uygulamada** | | | 13.187 | 1.195 | 9,1 | | 351.487 | | 18.245 | 20.037 |
| **Toplam: tamamlanmış, yürürlük bekleyen** | | | 4.400 | 315 | 7,2 | | 105.399 | | 6.543 | 10.202 |
| **Genel toplam** | | | 17.587 | 1.510 | 8,6 | | 456.886 | | 24.788 | 30.239 |

*Kaynak ve etiketler:*
- `[V]` CEPII BACI HS17 V202601, 2024.
- `[V]` WITS/TRAINS, ortağın en son MFN yılı (çoğunlukla 2023), HS6 basit ortalama.
- `[T]` Ağırlıklandırma: Türkiye'nin veya AB'nin o pazara ihracat bileşimi.
- "AB'nin tercih avantajı" tam liberalizasyon varsayımıyla bir üst sınırdır. Ekonomik ortaklık anlaşmalarında (EPA), Vietnam ve Mercosur'un geçiş takvimlerinde ve Cezayir'in kısıtlamalarında gerçek değer daha düşüktür.
- Anlaşma durumu Faz 0 D-8'den (DG TRADE müzakere sayfası, 17.10.2026). Türkiye'nin STA ağı 24 anlaşma `[V]` (Ticaret Bakanlığı); DG TRADE sayfası 22 sayıyor.
- Güven: Orta.

**Okuma notları**
1. **Asimetrinin bugünkü maliyeti küçük, yönü büyüyor.**
   - Türkiye'nin bu pazarlara ihracatı toplam ihracatın %6,7'si ($17,6 mlr, 2024).
   - Ödenen vergi ≈$1,5 mlr: ihracat değerinin %8,6'sı.
   - Türkiye'nin bu pazarlardaki payı çoğunlukla %0,1–0,6. Tek istisna Cezayir (%6,6).
   - Tamamlanan Hindistan, Endonezya ve Avustralya anlaşmaları ile Mercosur'un kademeli tarife indirimleri, AB rakiplerinin avantajını önümüzdeki 5–10 yılda $18 mlr'dan ≈$25 mlr'a çıkaracak.
   - Asimetri en çok yüksek MFN'li pazarlarda pahalı: Kamerun %17,6, Gana %14,3, Mozambik %14,2, Kenya %14,1, Cezayir %13,5, Mercosur %12,1.
2. **Neden STA yapılamadı?**
   - BKP (2016) gerekçeyi açıkça yazıyor: Cezayir, Meksika ve Güney Afrika, malları Türkiye'ye AB üzerinden zaten ulaştığı için paralel bir STA'dan kaçınıyor. `[V]`
   - Ticaret Bakanlığı'na göre (2.8.2024) aktif müzakereler yalnızca Japonya, Endonezya ve Körfez İşbirliği Konseyi ile yürüyor; İngiltere STA'sı da güncelleniyor. `[V]`
   - 2016'da "devam ediyor" listesindeki Meksika, Mercosur, Kolombiya, Ekvador ve Peru müzakereleri fiilen uykuda. `[D?]`
3. **Çıkışın kaldıracı.**
   - Bu ortakların Türkiye'ye ihracatı $30,2 mlr. En büyükleri:
     - Hindistan $6,8 mlr,
     - Mercosur $5,0 mlr,
     - Japonya $4,5 mlr,
     - Vietnam $3,0 mlr,
     - Endonezya $2,4 mlr.
   - GB'den çıkışla A.TR üzerinden dolaylı erişim ortadan kalkar. Türkiye'nin kendi tarifesini belirleyebilmesi de bu ortakları Türkiye ile STA'ya yöneltir.
   - Bu, "azami fayda" hedefinin (yeni STA ağı) somut tabanı. Ancak kaldıracın iki yüzü var: GB sonrası Türkiye'nin bu ortaklara uygulayacağı tarife, kendi girdi maliyetini de belirler (Faz 5).
   - `[T]` Güven: Orta.

### 2.2 Serbest dolaşım, İGV ve ticaret sapması

- **Dolaylı erişim ve Türkiye'nin karşı önlemi.**
  - AB'de serbest dolaşıma girmiş üçüncü ülke menşeli mallar A.TR ile Türkiye'ye gelebiliyor.
  - Türkiye, STA'sı olmayan ülkelerin menşeli mallarına İGV uyguluyor; bu mallar AB üzerinden gelse de vergi alınıyor (1/95 md. 58(2) uyarınca tek taraflı önlem gerekçesi; örneğin Meksika menşeli otomobiller).
  - Komisyon'un Türkiye Raporu (2025) bu ek vergileri, muafiyetleri, serbest bölge uygulamalarını ve kıymete dayalı gözetimi "GB kurallarına aykırı" sayıyor.
  - 2026'da İGV'nin ≈4.344 satırda %48'e kadar uygulandığı bildiriliyor.
  - `[V]` SWD(2025) 756; satır sayısı `[D?]`.
- **Çıkış sonrası.**
  - İGV düzeni Türkiye'nin kendi MFN tarifesine dönüşür. AB menşeli mallar için ayrıca bir karar gerekir.
  - Mevcut İGV Kararı değişmezse AB menşeli mallar da İGV'ye tabi olur. Bu durumda AB mallarına uygulanan ağırlıklı oran %4,7'den %10,2'ye çıkar (Faz 0 S4 hesabı; §5'teki enflasyon etkisi).
  - `[T]` Güven: Orta.

### 2.3 Karar alma asimetrisi

- Türkiye AB'nin ticaret politikası, OGT, STA'lar ve ticaret savunması kararlarına oy hakkıyla katılmıyor. Danışma kanalları dar: Ek 9'daki üç komite ve md. 54–60'taki bilgi verme ve danışma hükümleri. `[V]`
- Ortaklık Konseyi 2019'dan beri toplanmıyor; kararlar yazılı usulle alınıyor (ör. 1/2025). `[V]` Faz 0 B-3.
- Konsey'in 2016 modernizasyon yetkisi hâlâ kabul edilmedi. Üst düzey ticaret diyalogları 8.7.2024'te ve 1.7.2025'te yapıldı. `[V]` DG TRADE Türkiye sayfası, 17.10.2026.
- Pratik sonuç: AB'nin yeni STA'ları, SKDM ve IAA Türkiye'ye danışılmadan tasarlanıyor ve Türkiye bunlara uymak zorunda kalıyor. Bu asimetri çıkışın siyasi gerekçesinin merkezinde. Faz 2'deki S1 karşı-olgusunda yalnızca "kısmen" giderilebilecek bir kalem. `[H]` Güven: Yüksek.

### 2.4 Kişilerin ve taşımacılığın dolaşımı

- **Vize**
  - 2024'te Türkiye vatandaşları 1.173.917 Schengen vizesi başvurusu yaptı; Çin'den sonra ikinci sırada. Ret oranı %14,5 (2023'te %16,1). `[V]` DG HOME, 20.5.2025.
  - 2025: 1.268.376 başvuru, ret oranı %14,6. Ret oranı en yüksek ülkeler Malta (%34,8) ve Almanya (%21,1). `[D?]` AB verisinin basın aktarımı.
  - 15.7.2025 tarihli Komisyon kararıyla kademeli çok girişli vize kuralları getirildi; tır şoförleri kapsam dışı. `[V]` EEAS; karar numarası `[D?]`.
  - Doğrudan konsolosluk ücreti ≈€114 mn/yıl `[T]`.
- **Hukuki sınır**
  - Demirkan (C-221/11, 2013): Katma Protokol md. 41 standstill hükmü hizmet *almak* için seyahat edenleri kapsamıyor.
  - Soysal çizgisi (C-228/06): hizmet sunucularına yeni vize şartı konamaz.
  - `[V]`
  - Bu haklar GB'den değil Ankara Anlaşması'ndan doğduğu için çıkıştan etkilenmez (Faz 0 A-8).
- **Karayolu**
  - GB mal ticaretini kapsıyor, taşıma hizmetlerini kapsamıyor.
  - Çekya'nın transit kotası yılda 10.000; seferlerde 800 km'ye kadar dolanma gerektiriyor. `[V]` Ekonomi Gazetesi, 16.1.2025.
  - Avusturya'nın toplam izin sayısı ≈21.000. `[D?]`
  - ATAD, Macaristan'ın transit Türk tırlarından aldığı araç vergisini 1/95 md. 4'e aykırı "eş etkili vergi" saydı. `[V]` C-65/16 *Istanbul Lojistik*, 19.10.2017.
  - Kayıp tahmini: karayoluyla taşınan ihracatta 2005–2012'de ≈$10,6 mlr birikimli. Kayıpları ağırlıkla transit değil ikili kotalar yaratıyor. `[D?]`
  - AB'ye ihracatın değer olarak ≈%31'i karayoluyla taşınıyor. `[D?]` VB-16.
  - Ro-Ro hatları (Trieste ve Patras hatları; 28.9.2025'ten beri Haydarpaşa–Marsilya) kotaya karşı bir uyum mekanizması. `[D?]`
- **Hizmet ticaretindeki iz**
  - 2025'te AB27'ye karayolu yük taşımacılığı ihracatı $3,8 mlr; Türkiye'nin karayolu yük hizmetleri ihracatının %56,7'si.
  - AB27 ile taşımacılık dengesi +$9,9 mlr. `[V]` TÜİK, §3.5.
- **Çıkışın etkisi.** Kotalar ve vize zaten GB dışında. Çıkış bu asimetrileri kendiliğinden düzeltmez, kötüleştirmez de. Ancak yeni çerçeve müzakeresinde (S2) taşımacılık, transit ve iş vizesi başlıkları ilk kez masaya konabilir. Bu, çıkışın "GB'nin kapsamadığı alanlarda daha iyi çerçeve" hedefinin en somut alanı. `[H]` Güven: Orta.

### 2.5 Uyuşmazlık çözümü ve tek taraflı önlemler

- 1/95 md. 61–62'deki uyuşmazlık çözümü sınırlı:
  - anlaşmazlık Ortaklık Konseyi'ne götürülür;
  - tahkim yalnızca belirli konularda ve tarafların rızasıyla mümkün.
- Md. 63–64 korunma önlemlerini ve dengeyi yeniden kurma (yeniden dengeleme) önlemlerini düzenliyor.
- Ankara Anlaşması md. 25 zorunlu bir yargı yetkisi içermiyor.
- `[V]` Faz 0 A-1, A-6.
- AB'nin Türkiye'ye karşı ticaret savunması (anti-damping ve korunma) GB içinde de uygulanıyor; Türkiye de üçüncü ülkelere kendi önlemlerini alıyor (md. 44–47).
- Sonuç: GB, ihtilaf halinde Türkiye'ye bağlayıcı bir hukuki koruma sağlamıyor. Bu, çıkış senaryolarında kaybedilen bir güvence değil. S2'de bağlayıcı bir uyuşmazlık mekanizması bir kazanım olur. `[H]` Güven: Yüksek.

### 2.6 AB'nin yeni araçları

Ayrıntılı doğrulama Faz 0 §6.4'te.

| Araç | Türkiye'ye etkisi | GB içinde mi? | Çıkışta |
|---|---|---|---|
| SKDM (Tüzük 2025/2083; COM(2025) 989: ≈180 mansap ürün, 1.1.2028) | Demir-çelik, alüminyum, çimento, gübre; 2028'den mansap ürünler | GB'den bağımsız | Değişmez. Belirleyici olan TR-ETS'nin mahsup edilebilir bir fiyat üretmesi |
| Çelik rejimi (Tüzük 2026/1384) | Ülke kotaları, kota dışı %50, eritme-döküm kuralı | AKÇT STA'sı | Değişmez; AKÇT STA'sının korunması gerekir |
| Endüstriyel Hızlandırıcı Yasası (IAA, COM(2026) 100) | STA ve gümrük birliği ortakları kamu desteğinde ve açık artırmada "AB menşeine eşdeğer". Karşılıklılık sağlamayanlar dışlanabilir | Gümrük birliği ortağı olarak eşdeğerlik talep edilebilir | **Kırmızı çizgi:** yeni anlaşmada eşdeğerlik açıkça yazılmalı |
| SAFE (Tüzük 2025/1106) ve EDIP | Yunanistan Türkiye'nin katılımını engelledi (4.2.2026); EDIP'te AB dışı bileşen tavanı %35 | GB, savunma programlarına katılım sağlamıyor | Değişmez |
| Yatırım taraması (17.1.2028'den) ve ekonomik güvenlik (JOIN(2025) 977) | Türk yatırımlarına tarama | GB ilgisiz | Değişmez |
| Rusya yaptırımları (18. ve 20. paket) | Rus ham petrolünden rafine ürün yasağı; Türk kuruluşlar Ek IV'te | GB ilgisiz | Değişmez |

`[V]` Faz 0 D-3–D-11. Güven: Yüksek.

**Sonuç.** AB'nin yeni araçlarının çoğu GB'den bağımsız işliyor. GB üyeliği Türkiye'yi bunlardan korumuyor: SKDM muafiyeti yok, SAFE dışlaması var. Tek istisna IAA: gümrük birliği ortağı statüsü IAA'da avantaj sağlayabilir. **Çıkış bu avantajı kaybettirebilir.** Bu, çıkışın olumsuz bir bulgusudur. S2 metnine "AB menşeine eşdeğerlik" hükmü konması zorunlu hale gelir. `[H]` Güven: Orta.

### 2.7 Üçüncü ülkelerin ayrımcılığı

- **ABD.**
  - Bölüm 301 kapsamında Türkiye'ye %12,5 uygulanıyor (24.7.2026'dan); AB'ye toplam oran %10'la sınırlı. `[V]` USTR.
  - Bölüm 232 kapsamında Türkiye'ye indirim yok.
  - GB, Türkiye'yi AB'nin pazarlıkla elde ettiği koşullardan yararlandırmıyor. Türkiye ABD ile müzakereyi tek başına yapmak zorunda.
  - Bu, GB içindeyken de var olan bir asimetri. Çıkış Türkiye'ye ABD ile tarife indirimi müzakere etme özerkliği verir. GB içinde Türkiye'nin ABD'ye tek taraflı tarife indirimi OGT'ye aykırı olur.
  - `[H]` Güven: Orta.
- **Çin.**
  - Türkiye'nin Çin menşeli otomobillere ek vergileri DS629'da bağlı oranları aşmakla mahkûm edildi (panel raporu 28.7.2026). `[V]`
  - Çıkış sonrası tarife cetvelinde politika alanı bağsız satırlarla sınırlı. Sanayi satırlarının %57'si bağsız (Faz 0 C-7, §6.7).

### 2.8 Asimetrilerin özeti

| No | Asimetri | Bugünkü maliyet (yıllık) | 2026–2030 eğilimi | Çıkışla değişim | Etiket ve güven |
|---|---|---|---|---|---|
| A-1 | STA asimetrisi | $1,2 mlr vergi; AB rakiplerine $18,2 mlr avantaj (üst sınır) | Artıyor: Mercosur, Hindistan, Endonezya, Avustralya ile $25 mlr | Türkiye kendi STA'larını yaparsa kalkar (kaldıraç $30 mlr ithalat) | `[T]` Orta |
| A-2 | Karar alma | Ölçülmedi | Artıyor (SKDM, IAA, ekonomik güvenlik) | Kalkar; ancak Türkiye AB kurallarından etkilenmeye devam eder | `[V]` nitel, Yüksek |
| A-3 | İGV ve serbest dolaşım sürtünmesi | Ölçülmedi | Durağan | İGV'nin AB mallarına yayılması riski (enflasyon) | `[V]` Orta |
| A-4 | Vize | ≈€114 mn ücret + zaman maliyeti | Hafif iyileşme (kademeli vize kuralı) | Değişmez (Ankara hakları korunur); S2'de iş vizesi başlığı açılabilir | `[T]` Orta |
| A-5 | Karayolu kotaları ve transit | ≈$1,3 mlr/yıl ihracat kaybı (2005–12 ortalaması) | Belirsiz | Değişmez; S2'de karayolu taşımacılığı başlığı açılabilir | `[D?]` Düşük |
| A-6 | Uyuşmazlık çözümü | Ölçülmedi | Durağan | S2'de bağlayıcı mekanizma kazanım olur | `[V]` Yüksek |
| A-7 | AB'nin yeni araçları (SKDM, çelik, SAFE) | Faz 3–4'te | Artıyor | Çoğu değişmez; IAA eşdeğerliği kaybedilebilir | `[V]` Orta |
| A-8 | ABD'nin ayrımcı tarifesi (301) | 2,5 puan fark | Belirsiz | Çıkış müzakere özerkliği verir | `[V]` Orta |

---

## 3. Makro tablo ve cari denge ayrıştırması

### 3.1 Cari denge bileşenleri, 2010–2026

Tutarlar milyar $; son üç sütun yüzde ve endeks.

| Yıl | Cari denge | Dış ticaret dengesi (ÖD tanımlı) | Hizmetler | Seyahat (net) | Taşımacılık (net) | Birincil gelir | İkincil gelir | Enerji (net) | Parasal olmayan altın (net) | Altın ve enerji hariç (çekirdek) | GSYH (mlr $) | Cari denge/GSYH (%) | Çekirdek/GSYH (%) | Reel kur, TÜFE bazlı (2025=100) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2010 | -44,6 | -56,3 | 16,7 | 17,4 | 1,3 | -6,5 | 1,5 | -34,0 | -0,5 | -10,1 | 784 | -5,7 | -1,3 | 169,7 |
| 2012 | -41,8 | -65,4 | 28,7 | 27,4 | 3,7 | -6,6 | 1,5 | -52,4 | 5,7 | 4,9 | 887 | -4,7 | 0,6 | 155,1 |
| 2014 | -32,1 | -66,6 | 41,1 | 31,2 | 16,6 | -8,2 | 1,5 | -48,7 | -3,9 | 20,5 | 943 | -3,4 | 2,2 | 143,8 |
| 2016 | -22,2 | -39,9 | 25,4 | 18,8 | 12,7 | -9,2 | 1,6 | -24,1 | 1,8 | 0,1 | 871 | -2,5 | 0,0 | 140,6 |
| 2018 | -14,6 | -40,7 | 36,4 | 26,9 | 14,9 | -11,1 | 0,8 | -37,8 | -8,7 | 31,9 | 792 | -1,8 | 4,0 | 109,4 |
| 2019 | 15,0 | -16,8 | 42,8 | 34,4 | 13,8 | -11,8 | 0,9 | -33,3 | -9,3 | 57,6 | 776 | 1,9 | 7,4 | 107,7 |
| 2020 | -31,0 | -37,9 | 15,3 | 13,2 | 8,1 | -8,6 | 0,2 | -24,2 | -22,4 | 15,6 | 734 | -4,2 | 2,1 | 97,7 |
| 2021 | -7,1 | -29,3 | 32,8 | 26,2 | 13,1 | -11,5 | 0,9 | -42,2 | -2,0 | 37,1 | 837 | -0,8 | 4,4 | 88,4 |
| 2022 | -46,7 | -89,6 | 52,5 | 41,0 | 18,2 | -9,2 | -0,4 | -80,1 | -19,4 | 52,8 | 925 | -5,0 | 5,7 | 80,1 |
| 2023 | -41,8 | -86,3 | 55,7 | 42,2 | 19,9 | -11,8 | 0,6 | -52,7 | -25,6 | 36,6 | 1.141 | -3,7 | 3,2 | 83,1 |
| 2024 | -13,6 | -56,0 | 60,8 | 48,9 | 19,6 | -18,5 | 0,1 | -49,0 | -13,7 | 49,1 | 1.362 | -1,0 | 3,6 | 93,0 |
| 2025 | -30,3 | -69,3 | 63,0 | 51,1 | 22,8 | -23,4 | -0,5 | -47,3 | -20,1 | 37,1 | 1.602 | -1,9 | 2,3 | 100,0 |
| 2026 Oca–Ağu | -31,5 | -53,3 | 41,5 | 32,4 | 16,9 | -17,8 | -1,9 | -36,0 | -7,1 | 11,6 | — | — | — | 104,8 |

*Kaynak ve etiketler:*
- `[V]` TCMB EVDS3:
  - ödemeler dengesi ayrıntılı sunum (BPM6), TP.ODEAYRSUNUM6.*;
  - altın ve enerji hariç cari denge, TP.HARICCARIACIK.* (enerji = fasıl 27);
  - reel kur TP.RK.T1.Y.
- GSYH: TP.GSYIH20.BY.B1GQ (cari fiyatlar, TL) yıllık ortalama TP.DK.USD.A.YTL kuruna bölündü. 2025 değeri ($1.602 mlr) OVP Tablo 1.1 ile aynı `[V]`.
- 2026 yalnızca sekiz ay.
- Tam seri ve finans hesabı `veri/teshis_odemeler_dengesi.csv` dosyasında.
- Güven: Yüksek.

**Okuma notları**
1. **2025 revizyonu (VB-07 kapandı).**
   - EVDS3'teki güncel 2025 cari açığı −$30,276 mn. Bu, OVP'nin −$30,3 mlr'ı ile aynı.
   - Şubat 2026'daki ilk açıklama (−$25,2 mlr) sonradan revize edildi. Farkın ana kaynağı birincil gelir giderindeki +$4,8 mlr'lık yukarı revizyon (Faz 0 VB-07). TCMB revizyon duyuruları: 12.3.2026 portföy faizi, 13.5.2026 yatırım fonu, 13.8.2026 finans hesabı.
   - `[V]` Güven: Yüksek.
2. **Çekirdek denge yapısal olarak fazla veriyor.**
   - Altın ve enerji hariç denge 2014'ten bu yana her yıl pozitif:
     - 2019'da +$57,6 mlr ile zirve;
     - 2025'te +$37,1 mlr (GSYH'nin %2,3'ü);
     - Ağustos 2026 itibarıyla 12 ayda +$26,0 mlr.
   - Cari açığın kaynakları:
     - enerji: 2025'te −$47,3 mlr; 12 ayda −$51,9 mlr;
     - altın: −$20,1 mlr;
     - birincil gelir: −$23,4 mlr.
   - GB'nin doğrudan etkilediği mal ve hizmet ticareti çekirdek dengenin içinde. **Bir GB şoku, cari açığın en sağlıklı bileşenini bozar.** `[V]` Güven: Yüksek.
3. **Birincil gelir açığı büyüyor.**
   - Faiz gideri $5,6 mlr'dan (2021) $14,9 mlr'a (2025) çıktı.
   - Doğrudan yatırım geliri gideri $7,9 mlr (2025).
   - T+5 hedefinde bu kalem hızla daralmayacak; dış borç stoku ve faiz düzeyi belirleyici.
   - `[V]` Güven: Yüksek.
4. **Hizmet fazlası turizm ve taşımacılığa dayanıyor.**
   - 2025'te seyahat geliri $60,0 mlr; OVP'de turizm geliri $65,2 mlr.
   - Seyahat ve taşımacılık birlikte $73,9 mlr net fazla veriyor; diğer hizmetler −$10,9 mlr açık.
   - `[V]` Güven: Yüksek.

### 3.2 Finansman ve dış yükümlülükler

| Kalem (milyar $) | 2023 | 2024 | 2025 | Kaynak |
|---|---|---|---|---|
| Doğrudan yatırım, net yükümlülük oluşumu | 10,6 | 11,7 | 12,9 | `[V]` EVDS3 Q108 |
| bunun gayrimenkul kısmı | 3,6 | 2,8 | 2,3 | `[V]` Q113 |
| Portföy yatırımları, net yükümlülük oluşumu | 8,4 | 23,4 | 17,5 | `[V]` Q119 |
| Diğer yatırımlar, net | −24,8 | −4,3 | −12,5 | `[V]` Q136 |
| Rezerv varlıklar | −2,0 | 0,6 | −22,0 | `[V]` Q204 |
| Net hata ve noksan | 4,6 | −7,2 | −5,9 | `[V]` Q210 |
| Uluslararası yatırım pozisyonu, net (yıl sonu) | −307,0 | −351,2 | −349,3 | `[V]` TP.UYPUCAY.K1 |
| Doğrudan yatırım yükümlülük stoku (yıl sonu) | 194,4 | 231,9 | 230,1 | `[V]` TP.UYPUCAY.K41 |

*Not:* EVDS3 rezerv varlık serisinin işareti finans hesabı sunumuna göredir. Brüt rezervler 28.8.2026'da $188,2 mlr `[V]` OVP. Güven: Yüksek.

**Kırılganlık.**
- Cari açık 2024–2025'te büyük ölçüde portföy girişleriyle finanse edildi.
- Çıkış kararının duyurusu ve müzakere belirsizliği risk primini ve portföy akımlarını doğrudan etkiler. Bu kanal enflasyon bütçesinde ayrı blok olarak gösterilecek (V-05).
- Faz 0 bulgusu bunu destekliyor: kamuoyu önündeki resmî Türk tutumu "modernizasyon"du (B-3). Bu yüzden çıkış kararı piyasa için bir tutum değişikliği olur.
- `[H]` Güven: Orta.

### 3.3 Tasarruf-yatırım dengesi

| GSYH'ye oran (%) | 2025 | 2026 (GT) | 2027 (P) | 2028 (P) | 2029 (P) |
|---|---|---|---|---|---|
| Toplam yurt içi tasarruf | 29,9 | 30,2 | 30,3 | 30,5 | 30,7 |
| kamu tasarrufu | 1,4 | 1,0 | 0,6 | 0,5 | 1,0 |
| özel tasarruf | 28,5 | 29,2 | 29,7 | 29,9 | 29,8 |
| Toplam tasarruf-yatırım farkı | −1,8 | −2,5 | −1,9 | −1,8 | −1,6 |
| kamu tasarruf-yatırım farkı | −1,9 | −2,8 | −2,6 | −2,7 | −2,2 |
| özel tasarruf-yatırım farkı | 0,2 | 0,3 | 0,7 | 0,9 | 0,6 |

*Kaynak:* `[V]` OVP (2027–2029), Tablo 1.1, RG 6.9.2026. Toplam tasarruf-yatırım farkı ile cari açık arasındaki küçük fark, milli gelir hesaplarındaki kur ağırlığından kaynaklanıyor (OVP dipnot 3). Güven: Yüksek.

**Çıkarım (kaçınılacak hata 1).**
- Cari denge = tasarruf − yatırım.
- OVP'nin 2029 patikasında açığın tamamı kamu kesiminde (−%2,2); özel kesim fazla veriyor (+%0,6).
- T+5'te cari denge ≥ %0 için ya kamu tasarruf-yatırım açığının ≈1,6–2,2 puan kapanması gerekir, ya da özel tasarrufun artması veya yatırımın düşmesi.
- Tarife ve sanayi politikası önlemleri ancak bu kalemleri değiştirdikleri ölçüde kalıcı katkı yapar:
  - enerji ithalatını kalıcı olarak azaltan yerli üretim,
  - ihracat kapasitesi yaratan yatırım,
  - verimlilik.
- Lerner simetrisi gereği genel bir ithalat tarifesi ihracatı da vergiler; reel kur tepkisiyle cari dengeye net katkısı sıfıra yakın olur.
- `[V]` kimlik; uygulama `[H]`. Güven: Yüksek.

### 3.4 Reel kur

- TÜFE bazlı reel efektif kur (2025 = 100; artış TL'nin reel değer kazancı):
  - 2010: 169,7;
  - 2018: 109,4;
  - 2022: 80,1 (dip);
  - 2025: 100,0;
  - 2026 ilk sekiz ay ortalaması: 104,8.
- 2022–2026 arasında reel değerlenme %31. `[V]` EVDS3 TP.RK.T1.Y.
- Dezenflasyon programının bir parçası olarak TL'nin reel değerlenmesi emek yoğun ve düşük marjlı ihracatçıları sıkıştırıyor. Giyimde AB pazar payı kaybı (§1.3) bununla uyumlu.
- S4'te AB'nin giyime %11,9, otomotive %9,8 ortalama MFN uygulaması aynı sektörlere ikinci bir şok olur.
- Telafi için kur kanalı kullanılamaz: dezenflasyonla çatışır (temel ilke 4). Telafi hedefli, süreli ve DTÖ uyumlu araçlarla yapılmalı (Faz 5).
- `[V]`/`[H]` Güven: Orta.

### 3.5 AB ile ikili cari denge: mal ve hizmet

| Hizmet türü | AB27'ye ihracat 2019 (mn $) | 2025 (mn $) | AB27'nin payı 2025 (%) | AB27'den ithalat 2025 (mn $) | AB27'nin payı 2025 (%) | AB27 ile denge 2025 (mn $) |
|---|---|---|---|---|---|---|
| Toplam (seyahat hariç) | 12.466 | 23.419 | 36,1 | 23.098 | 43,7 | 321 |
| Taşımacılık | 9.003 | 16.166 | 38,0 | 6.248 | 31,6 | 9.918 |
| Karayolu yük taşımacılığı | 2.161 | 3.787 | 56,7 | 282 | 21,6 | 3.505 |
| Diğer iş hizmetleri | 1.299 | 3.049 | 38,7 | 5.886 | 56,2 | -2.837 |
| Telekomünikasyon, bilgisayar ve bilgi | 537 | 1.363 | 20,3 | 4.326 | 61,4 | -2.964 |
| Fikri mülkiyet kullanım ücretleri | 41 | 184 | 26,4 | 2.479 | 50,3 | -2.295 |
| Bakım ve onarım | 339 | 599 | 24,0 | 318 | 18,8 | 281 |
| Başkasına ait girdilerle imalat (fason) | 153 | 164 | 45,5 | 0 | — | 164 |
| İnşaat | 20 | 60 | 12,7 | 0 | — | 60 |

*Kaynak ve etiketler:*
- `[V]` TÜİK DF_UHTI_HIZMET_COGRAFI_C (Uluslararası Hizmet Ticareti İstatistikleri, ortak ülke × EBOPS). AB27 = 27 üye ülkenin toplamı; dünya toplamı "W1" kodu. W1'in 2025 dengesi, ödemeler dengesindeki hizmet dengesiyle (+$63,0 mlr) aynı.
- Ülke dağılımında seyahat kalemi yok. "Toplam" satırındaki paylar seyahat hariç dünya toplamına göre hesaplandı `[T]`.
- Güven: Yüksek.

**Okuma notları**
- **Hizmetlerde (seyahat hariç) AB27 ile denge dengede: +$0,3 mlr.**
  - Türkiye taşımacılıkta fazla veriyor: +$9,9 mlr; bunun $3,5 mlr'ı karayolu yük taşımacılığı.
  - Bilgi-iletişim (−$3,0 mlr), diğer iş hizmetleri (−$2,8 mlr) ve fikri mülkiyet ücretlerinde (−$2,3 mlr) açık veriyor.
- **Mal dengesi.** 2025'te AB ayna verisiyle −€10,7 mlr, Türkiye verisiyle +$3,7 mlr (§1.1).
- **Seyahat.** AB ülkeleri vatandaşlarının seyahat gelirindeki payı bu veri setinde yok (VB-12). Almanya Türkiye'nin en büyük ikinci kaynak pazarı; AB27'nin yabancı ziyaretçilerdeki payının ≈%30 olduğu tahmin ediliyor. `[D?]`
- **Sonuç.** AB ile ikili cari denge, mal ve hizmet birlikte, ayna veriye göre Türkiye aleyhine ≈$10–12 mlr; Türkiye verisine göre ise Türkiye lehine. Seyahat de eklenince Türkiye lehine döner. `[T]` Güven: Düşük; seyahat payı doğrulanmalı.

### 3.6 OVP 2027–2029 taban patikası ve T+5 uzantısı

| Gösterge | 2025 | 2026 (GT) | 2027 (P) | 2028 (P) | 2029 (P) | 2033 (T2028'de T+5) | 2034 (T2029'da T+5) |
|---|---|---|---|---|---|---|---|
| GSYH (mlr $) | 1.602 | 1.821 | 1.984 | 2.091 | 2.225 | ≈2.810 `[H]` | ≈2.980 `[H]` |
| GSYH büyümesi (%) | 3,7 | 3,3 | 4,2 | 4,6 | 5,0 | — | — |
| TÜFE, yıl sonu (%) | 30,9 | 28,4 | 21,0 | 13,5 | 9,0 | — | — |
| Mal ihracatı, GTS (mlr $) | 273,2 | 282,0 | 292,0 | 302,5 | 316,0 | — | — |
| Mal ithalatı, GTS (mlr $) | 365,4 | 387,0 | 397,0 | 411,0 | 426,0 | — | — |
| Enerji ithalatı (mlr $); Brent ($/varil) | 62,5; 69,1 | 71,0; 88,0 | 66,0; 76,0 | 63,5; 72,0 | 61,0; 67,0 | — | — |
| Turizm geliri (mlr $) | 65,2 | 65,0 | 70,0 | 73,5 | 78,5 | — | — |
| Cari denge (mlr $) | −30,3 | −47,5 | −38,5 | −37,0 | −35,5 | −28 ile −45 arası `[H]` | −25 ile −48 arası `[H]` |
| Cari denge/GSYH (%) | −1,9 | −2,6 | −1,9 | −1,8 | −1,6 | −1,0 ile −1,6 arası `[H]` | −0,85 ile −1,6 arası `[H]` |
| Altın hariç cari denge/GSYH (%) | −0,6 | −1,9 | −1,2 | −1,0 | −0,8 | — | — |
| Altın ve enerji hariç cari denge (mlr $) | 37,1 `[V]` | ≈21 | — | — | — | — | — |
| İşsizlik (%) | 8,3 | 8,1 | 8,0 | 7,8 | 7,6 | — | — |

*Kaynak ve etiketler:*
- `[V]` OVP (2027–2029), Tablo 1.1. 2026 çekirdek denge OVP metninden.
- `[H]` 2033 ve 2034 uzantısı. GSYH yılda %6 nominal dolar büyümesiyle uzatıldı (OVP'de 2028→2029 %6,4).
- Cari denge iki uç varsayımla verildi:
  - sabit: −%1,6 (OVP'nin son yılı);
  - iyileşen: OVP'nin eğimiyle yılda 0,15 puan.
- Güven: Düşük.

**Hedef boşluğu (`[H]`).**
- T+5'te cari denge ≥ %0 hedefi, GB kararından bağımsız olarak taban patikaya göre ek bir iyileşme gerektiriyor:
  - 2033: $28–45 mlr;
  - 2034: $25–48 mlr;
  - GSYH'nin 0,85–1,6 puanı.
- Faz 6'daki cari denge köprüsü bu boşluğu üç bileşene ayıracak:
  - GB paketinin katkısı,
  - tamamlayıcı politikalar (enerji dönüşümü, kamu tasarrufu, altın),
  - kalan açık.
- Bu fazın teşhisi: **GB paketi bu boşluğu tek başına kapatamaz.** Enerji (−$47–52 mlr) ve kamu tasarruf açığı belirleyici. Güven: Orta.

### 3.7 S4'ün ilk tur makro sinyalleri (Faz 6'da kalibre edilecek)

| Kanal | Büyüklük | Yöntem | Etiket ve güven |
|---|---|---|---|
| Türk ihracatına AB vergisi | €5,5 mlr/yıl (ortalama %5,85) | 2025 ticareti × CN 2026 MFN, CN8 | `[T]` Orta |
| İhracat hacmi kaybı | P10–P50–P90: −€13,8 / −21,2 / −30,4 mlr (σ = 3/5/8); 2028 GSYH'sinin %0,7–1,6'sı | Kısmi denge, tek σ | `[T]` Orta |
| AB mallarına Türkiye vergisi | €4,9 mlr (İGV hariç) / €10,7 mlr (İGV dahil) | 2025 ticareti × 2026 Türk tarifesi | `[T]` Orta |
| TÜFE'ye birinci tur etki: yalnızca MFN | **Faz 2 düzeltmesi (girdi-çıktı modeli):** P10–P50–P90: 32 / 42 / 53 bp. İlk kaba hesap 21 / 28 / 40 bp idi | Leontief fiyat modeli, TÜİK 2023 yurt içi ve ithal girdi-çıktı tabloları; geçişkenlik ρ = 0,6 / 0,8 / 1,0 (`kod/f2a_io_fiyat.py`, `veri/politika_io_s4_tufe.csv`). En büyük kalem otomobil (C29): 24 bp | `[T]` Orta |
| TÜFE'ye birinci tur etki: MFN + İGV | **Faz 2 düzeltmesi:** 59 / 78 / 98 bp. İlk kaba hesap 46 / 62 / 86 bp idi. Yurt içi rakipler fiyatlarını ithal fiyatına yarı yarıya uydurursa (κ = 0,5) 182 bp | Aynı | `[T]` Orta |
| Cari dengeye ilk etki | Faz 6'da (ihracat kaybı ile ithalatın sapma ve daralma payı birlikte). İlk iki yılda GSYH'nin −0,5 ile −1,1 puanı aralığında olası | Kısmi denge; reel kur tepkisi yok | `[H]` Düşük |

**Okuma.**
- **İGV dahil senaryo enflasyon kısıtını aşıyor.** Birinci turda kümülatif tavan 50 bp, yıllık tavan 30 bp. Girdi-çıktı modeline göre (Faz 2) MFN'nin tek başına etkisi de (P50 42 bp) yıllık tavanı aşıyor. Bu tablo S4'ü pasif kabul eder; vergi takası, girdi tarifeleri ve İGV tasarımıyla nasıl değiştiği [`02a_politika_uzayi.md`](02a_politika_uzayi.md) belgesinde.
- Dolayısıyla AB mallarına İGV'nin yayılmasını önleyen ve girdi tarifelerini düşüren bir tarife cetveli T'den önce kabul edilmeli.
- Ancak DTÖ'nün en çok kayrılan ulus (MFN) ilkesi, STA olmadan yalnızca AB'ye indirim yapılmasına izin vermez (GATT md. I ve XXIV). İndirim herkese uygulanmak zorunda; bu da Çin ve diğer kaynaklara karşı korumayı azaltır. Bu, kabiliyet hedefiyle bir çatışmadır (§5).
- Güven: Orta.

---

## 4. Maruziyet haritası

### 4.1 NACE bölümleri (imalat)

| NACE | Bölüm | Çalışan 2024 (bin) | Üretim değeri 2024 (mlr $) | AB'ye ihracat 2025 (mlr $) | AB'nin bölüm ihracatındaki payı (%) | AB ihracat yoğunluğu (% üretim) | S4: AB MFN, ağırlıklı (%) | S4: ihracat kaybı σ=5 (mn $) | Kayıp / üretim (%) | Doğrudan maruz istihdam (bin) | S4 risk istihdamı σ=5 (bin) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 14 | Giyim eşyası | 668,7 | 31,2 | 9,5 | 57,0 | 30,6 | 11,9 | 4.079 | 13,1 | 204,3 | 87,5 |
| 29 | Motorlu kara taşıtları ve parçaları | 255,3 | 57,5 | 22,4 | 79,0 | 38,9 | 9,8 | 8.103 | 14,1 | 99,4 | 36,0 |
| 13 | Tekstil ürünleri | 493,4 | 42,1 | 4,8 | 37,2 | 11,5 | 7,2 | 1.374 | 3,3 | 56,5 | 16,1 |
| 28 | Makine ve ekipman (bys) | 319,0 | 36,1 | 11,8 | 50,7 | 32,5 | 2,6 | 1.383 | 3,8 | 103,7 | 12,2 |
| 27 | Elektrikli teçhizat | 231,6 | 37,4 | 10,8 | 52,3 | 28,7 | 4,2 | 1.901 | 5,1 | 66,6 | 11,8 |
| 22 | Kauçuk ve plastik ürünler | 283,5 | 33,5 | 6,0 | 51,8 | 17,9 | 5,3 | 1.357 | 4,1 | 50,8 | 11,5 |
| 25 | Fabrikasyon metal ürünleri | 474,7 | 46,4 | 7,1 | 56,0 | 15,4 | 2,7 | 860 | 1,8 | 72,9 | 8,8 |
| 23 | Metalik olmayan mineral ürünler | 287,5 | 35,9 | 3,5 | 35,8 | 9,6 | 3,8 | 570 | 1,6 | 27,7 | 4,6 |
| 20 | Kimyasallar ve kimyasal ürünler | 128,0 | 34,5 | 5,3 | 36,5 | 15,5 | 4,3 | 982 | 2,8 | 19,8 | 3,6 |
| 24 | Ana metal sanayii | 195,6 | 69,9 | 9,7 | 41,5 | 13,9 | 4,4 | 1.106 | 1,6 | 27,1 | 3,1 |
| 10 | Gıda ürünleri | 610,3 | 99,2 | 5,8 | 25,8 | 5,9 | 9,6 | 447 | 0,4 | 35,7 | 2,7 |
| 15 | Deri ve ilgili ürünler | 75,8 | 4,7 | 0,6 | 36,4 | 12,3 | 7,5 | 161 | 3,5 | 9,3 | 2,6 |
| 32 | Diğer imalat | 104,9 | 10,0 | 1,7 | 15,3 | 17,4 | 2,0 | 157 | 1,6 | 18,3 | 1,7 |
| 30 | Diğer ulaşım araçları | 86,9 | 17,0 | 3,1 | 58,4 | 18,2 | 2,0 | 274 | 1,6 | 15,8 | 1,4 |
| 26 | Bilgisayar, elektronik ve optik ürünler | 64,6 | 10,7 | 1,0 | 30,0 | 9,2 | 6,1 | 209 | 2,0 | 5,9 | 1,3 |
| 31 | Mobilya | 252,8 | 12,9 | 1,4 | 38,9 | 11,0 | 0,8 | 53 | 0,4 | 27,8 | 1,0 |
| 16 | Ağaç ve mantar ürünleri (mobilya hariç) | 91,9 | 9,1 | 0,4 | 18,3 | 4,0 | 4,6 | 70 | 0,8 | 3,7 | 0,7 |
| 12 | Tütün ürünleri | 5,8 | 2,8 | 0,2 | 19,0 | 5,4 | 54,0 | 123 | 4,4 | 0,3 | 0,3 |
| 19 | Kok ve rafine petrol ürünleri | 9,9 | 29,0 | 3,4 | 25,5 | 11,8 | 3,5 | 531 | 1,8 | 1,2 | 0,2 |
| 11 | İçecekler | 19,5 | 5,3 | 0,2 | 26,9 | 2,9 | 4,8 | 28 | 0,5 | 0,6 | 0,1 |
| 17 | Kâğıt ve kâğıt ürünleri | 98,8 | 17,4 | 1,1 | 29,2 | 6,3 | 0,2 | 9 | 0,1 | 6,2 | 0,1 |
| 21 | Temel eczacılık ürünleri | 50,2 | 7,9 | 0,6 | 25,2 | 8,0 | 0,2 | 5 | 0,1 | 4,0 | 0,0 |
| 18 | Basım ve kayıtlı medyanın çoğaltılması | 54,7 | 4,3 | 0,0 | 65,9 | 0,2 | 0,0 | 0 | 0,0 | 0,1 | 0,0 |
| 33 | Makine ve ekipman kurulumu ve onarımı | 169,6 | 12,0 | — | — | — | — | — | — | — | — |
| **10–33** | **İmalat toplamı** | 5.033,0 | 666,8 | 110,3 | 44,3 | 16,5 | — | 23.781 | 3,6 | 857,8 | 207,2 |

*Kaynak ve etiketler:*
- `[V]` TÜİK YSHİ 2024 (çalışan, üretim değeri).
- `[V]` Comext 2025 (AB'ye ihracat; CIF, ayna veri) ve Comtrade 2025 (dünyaya ihracat). HS6 → NACE eşleştirmesi Türkiye ihracat değerinin %96,4'ünü kapsıyor.
- `[T]` S4 sütunları: Faz 0 S4 tarife duvarı, AB'nin 2026 MFN'si, σ = 5. Yalnızca GB ve İTÜ kapsamı; tarım (1/98) ve AKÇT hariç.
- "Doğrudan maruz istihdam" = çalışan × AB ihracat yoğunluğu; girdi bağlantıları hariç, Faz 6'da Leontief miktar modeliyle genişletilecek.
- "S4 risk istihdamı" = çalışan × kayıp/üretim; telafi, yeniden yönlendirme ve kur tepkisi içermeyen statik bir üst sınır.
- Güven: Orta.

**Okuma notları**
- **Toplam risk.**
  - İmalat istihdamının %17'si (≈858 bin) doğrudan AB ihracatına bağlı.
  - S4'te statik risk 207 bin kişi (%4,1). P10–P90 aralığı σ = 3 ile 135 bin, σ = 8 ile 297 bin.
  - Mal ve hizmet girdisi bağlantılarıyla rakam büyür (Faz 6). `[T]`
- **Yoğunlaşma.**
  - Riskin %60'ı iki bölümde: giyim (87 bin; üretimin %13,1'i) ve otomotiv (36 bin; %14,1).
  - İstihdam kısıtına göre bir sınıfta %5'i aşan kayıp destek tetikler. Bölüm düzeyinde 14, 29 ve 27 bu eşiği aşıyor (27'de üretim kaybı %5,1).
  - Sınıf düzeyindeki dağılım Faz 3'te çıkacak. `[T]` Güven: Orta.
- **Tarifenin kaba göstergesi.**
  - Tütünde (12) AB MFN'si %54. Ticaret küçük, ama İTÜ ve tarım bileşeni rejimi ayrıca incelenecek (kaçınılacak hata 15).
  - Gıdada (10) ortalama %9,6. Ancak AB'ye gıda ihracatının çoğu 1/98 tarım rejiminde ve S4 varyant (i)'de kapsam dışı.

### 4.2 Bölgesel yoğunlaşma

| İBBS-2 | Bölge | İmalat 4/a sigortalı 2025 (bin) | Doğrudan maruz (bin) | Maruz payı (%) | S4 risk σ=5 (bin) | S4 risk payı (%) | Ulusal S4 riskindeki pay (%) | Bunun giyim + otomotiv kısmı (bin) |
|---|---|---|---|---|---|---|---|---|
| TR10 | İstanbul | 848,2 | 145,5 | 17,2 | 38,0 | 4,5 | 23,2 | 25,5 |
| TR41 | Bursa, Eskişehir, Bilecik | 395,4 | 75,4 | 19,1 | 19,2 | 4,9 | 11,8 | 13,0 |
| TR42 | Kocaeli, Sakarya, Düzce, Bolu, Yalova | 410,1 | 78,7 | 19,2 | 18,2 | 4,5 | 11,1 | 11,5 |
| TR31 | İzmir | 248,6 | 41,0 | 16,5 | 9,3 | 3,7 | 5,7 | 5,4 |
| TRC3 | Mardin, Batman, Şırnak, Siirt | 85,5 | 21,0 | 24,6 | 8,4 | 9,8 | 5,1 | 8,0 |
| TR51 | Ankara | 256,3 | 42,2 | 16,5 | 7,0 | 2,7 | 4,3 | 2,3 |
| TR21 | Tekirdağ, Edirne, Kırklareli | 178,8 | 29,5 | 16,5 | 6,9 | 3,9 | 4,2 | 3,1 |
| TR33 | Manisa, Afyonkarahisar, Kütahya, Uşak | 188,0 | 28,6 | 15,2 | 6,1 | 3,2 | 3,7 | 2,6 |
| TRC1 | Gaziantep, Adıyaman, Kilis | 165,3 | 22,7 | 13,7 | 5,9 | 3,6 | 3,6 | 2,3 |
| TR62 | Adana, Mersin | 145,7 | 21,6 | 14,8 | 5,0 | 3,4 | 3,1 | 2,7 |
| TR52 | Konya, Karaman | 136,4 | 24,7 | 18,1 | 4,8 | 3,5 | 2,9 | 2,5 |
| TR83 | Samsun, Tokat, Çorum, Amasya | 96,1 | 16,2 | 16,9 | 4,5 | 4,7 | 2,8 | 3,4 |
| TRC2 | Şanlıurfa, Diyarbakır | 67,2 | 12,3 | 18,4 | 3,8 | 5,7 | 2,3 | 3,0 |
| TR32 | Aydın, Denizli, Muğla | 131,1 | 17,0 | 13,0 | 3,8 | 2,9 | 2,3 | 1,5 |
| TR63 | Hatay, Kahramanmaraş, Osmaniye | 109,2 | 14,5 | 13,2 | 2,9 | 2,6 | 1,8 | 0,8 |
| TR72 | Kayseri, Sivas, Yozgat | 112,3 | 15,8 | 14,1 | 2,6 | 2,3 | 1,6 | 0,8 |
| TRB1 | Malatya, Elazığ, Bingöl, Tunceli | 49,7 | 8,4 | 16,8 | 2,6 | 5,2 | 1,6 | 2,0 |
| TR90 | Trabzon, Ordu, Giresun, Rize, Artvin, Gümüşhane | 63,0 | 9,1 | 14,4 | 2,5 | 4,0 | 1,5 | 1,9 |
| TRB2 | Van, Muş, Bitlis, Hakkari | 28,8 | 6,2 | 21,5 | 2,4 | 8,2 | 1,4 | 2,2 |
| TR81 | Zonguldak, Karabük, Bartın | 49,6 | 8,1 | 16,3 | 1,9 | 3,9 | 1,2 | 1,2 |
| TR71 | Kırıkkale, Aksaray, Niğde, Nevşehir, Kırşehir | 54,4 | 8,2 | 15,0 | 1,9 | 3,4 | 1,1 | 1,0 |
| TR82 | Kastamonu, Çankırı, Sinop | 35,7 | 6,2 | 17,4 | 1,8 | 5,1 | 1,1 | 1,3 |
| TR61 | Antalya, Isparta, Burdur | 85,2 | 10,6 | 12,5 | 1,7 | 2,0 | 1,0 | 0,4 |
| TR22 | Balıkesir, Çanakkale | 73,6 | 8,8 | 11,9 | 1,5 | 2,0 | 0,9 | 0,4 |
| TRA1 | Erzurum, Erzincan, Bayburt | 13,0 | 1,7 | 13,0 | 0,4 | 3,4 | 0,3 | 0,3 |
| TRA2 | Ağrı, Kars, Iğdır, Ardahan | 7,8 | 1,1 | 14,7 | 0,3 | 4,5 | 0,2 | 0,3 |
| | **Toplam** | 4.034,8 | 675,2 | 16,7 | 163,7 | 4,1 | 100,0 | 99,7 |

*Kaynak ve etiketler:*
- `[V]` SGK İstatistik Yıllığı 2025, Tablo 1.11 (4/1-a zorunlu sigortalılar, il × NACE bölümü).
- `[T]` Bölüm oranları §4.1'den; her bölümün AB yoğunluğunun bütün illerde aynı olduğu varsayıldı. İl düzeyindeki ihracat bileşimi Faz 3'te TİM ve Ticaret Bakanlığı verisiyle düzeltilecek (VB-17).
- SGK 4/a toplamı (4,03 mn) YSHİ çalışan sayısından (5,03 mn) düşük; SGK yalnızca zorunlu sigortalı ücretlileri sayıyor.
- Güven: Orta.

**Okuma (kaçınılacak hata 19).**
- Mutlak riskin %46'sı üç sanayi bölgesinde: İstanbul (TR10), Bursa (TR41), Kocaeli (TR42).
- Bölge imalatına oranla risk en yüksek Güneydoğu ve Doğu'da:
  - Mardin, Batman, Şırnak, Siirt (TRC3): %9,8;
  - Van, Muş, Bitlis, Hakkari (TRB2): %8,2;
  - Şanlıurfa, Diyarbakır (TRC2): %5,7;
  - Malatya, Elazığ, Bingöl, Tunceli (TRB1): %5,2;
  - Kastamonu, Çankırı, Sinop (TR82): %5,1.
- Bu bölgelerdeki risk neredeyse tamamen giyimden kaynaklanıyor. Giyim üretimi, son on yılın bölgesel teşviklerle bu bölgelere kaydı.
- Bu bölgelerin alternatif istihdam seçenekleri sınırlı. Telafi tasarımı bölgesel olmalı: İBBS-2 bazında tetik ve kademeli destek (Faz 5, Faz 8).
- `[T]` Güven: Orta.

---

## 5. Kısıt çatışmaları: olumsuz bulgular ve onları değiştirecek koşullar

Ana prompt olumsuz bulguların açıkça yazılmasını ve onları pozitife çevirecek koşulların belirtilmesini istiyor. Aşağıdaki tablo S4'e göre ilk sinyalleri özetliyor.

| Kısıt (varsayım kaydı) | S4'teki ilk sinyal | Değerlendirme | Pozitife çevirme koşulu | Gerçekçilik `[H]` |
|---|---|---|---|---|
| Enflasyon: birinci tur ≤50 bp, ≤30 bp/yıl (V-05) | Pasif S4'te AB mallarına MFN: 32–53 bp; MFN + İGV: 59–98 bp (girdi-çıktı modeli, Faz 2) | Pasif tasarımda MFN de yıllık tavanı aşıyor. Aktif tasarım (vergi takası, İGV) `02a_politika_uzayi.md` belgesinde | (1) AB menşeli mallara İGV'nin yayılmaması (İGV Kararı değişikliği, T−6). (2) Yurt içinde üretilmeyen girdilerde MFN'nin herkese sıfırlanması (dezenflasyonist, bütçeye alan açar). (3) AB ile STA (S2/S3) veya geçiş düzenlemesiyle karşılıklı sıfır tarifenin korunması | (1) ve (2) Türkiye'nin elinde: yüksek. (3) AB'nin tutumuna bağlı: T2028'de düşük, T2029'da orta |
| Cari denge: T+5'te ≥ %0 (V-06) | Taban patikada 2029'da −%1,6; S4'te ilk yıllarda ek −0,5 ile −1,1 puan | GB paketi boşluğu tek başına kapatamaz; S4 boşluğu büyütür | Enerji ithalatında yapısal düşüş, kamu tasarrufu ve S4'ten kaçınma. Özerklik temettüsü ve STA ağı ihracat kapasitesini artırırsa katkı | Orta; tamamlayıcı politikalara bağlı |
| İstihdam: T+3'te net imalat kaybı sıfır; sınıfta %5 tetiği (V-07) | 207 bin (P10–P90: 135–297 bin) statik risk; 14, 29 ve 27 bölümleri %5 eşiğinin üstünde | S4'te kısıt telafisiz sağlanamaz | Anlaşmalı çıkış (S2/S3) veya geçiş süresi; giyim ve otomotivde hedefli ihracat ve istihdam desteği (DTÖ uyumlu: ASCM yasaklı sübvansiyon değil); yeni pazar (STA) | S2 ile yüksek; S4'te düşük |
| Kabiliyet: hiçbir sınıfta kabiliyet kaybı yok (V-08) | Otomotivde çapa yatırımcıların yeniden konumlanma riski; giyimde firma çıkışı | S4'te risk yüksek | Çapa yatırımcılarla T öncesi bağlayıcı yatırım ve tutma sözleşmeleri; AB pazarına erişimin STA ile güvence altına alınması | Orta |
| Mali: ≤ GSYH'nin %0,5'i/yıl (V-09) | Telafi ihtiyacı büyük; ek gümrük geliri enflasyon nedeniyle kullanılamaz | 2028'de kamu tasarruf-yatırım açığı −%2,7 (seçim yılı) | Destekler süreli ve azalan olmalı; girdi tarifesi indirimlerinin gelir kaybı hesaba katılmalı | Orta |
| Hukuk: DTÖ uyumu (V-10) | MFN ilkesi AB'ye özel indirimi yasaklıyor (STA olmadan); bağlı oranlar artışı sınırlıyor (DS629) | Tek taraflı tampon araçlar dar | GATT md. XXIV uyumlu geçici anlaşma (interim agreement) veya STA; bağsız satırlarda politika alanı | Orta |

**Sentez.** S4, altı kısıtın en az dördünü (enflasyon, istihdam, kabiliyet, cari denge) ihlal ediyor. Kullanıcı kararıyla çıkış yönü veri olduğundan, Faz 2'nin tasarım hedefi şu:

> T'de AB ile karşılıklı sıfır tarife korunmalı: STA, geçici anlaşma veya geçiş düzenlemesi; mümkünse menşe maliyeti düşük bir yapıyla. Buna ulaşılamazsa tek taraflı bir tampon paketi devreye girmeli: İGV düzeltmesi, girdide sıfır MFN, hedefli destek ve AKÇT STA'sının korunması.

Güven: Orta.

---

## 6. İki takvim için çıkarımlar: T2028 ve T2029

| Boyut | T2028 (T = 1.1.2028) | T2029 (T = 1.1.2029) | Teşhis |
|---|---|---|---|
| Makro başlangıç noktası (OVP) | TÜFE 2027 sonu %21,0; 2028 hedefi %13,5. Cari denge 2027'de −%1,9 | TÜFE 2028 sonu %13,5; 2029 hedefi %9,0 (tek hane). Cari denge 2028'de −%1,8 | T2028'de fiyat şoku dezenflasyonun en hızlı yılına denk geliyor. T2029'da tek haneli enflasyon hedefini tehdit ediyor. İkisinde de enflasyon bütçesi bağlayıcı |
| Mali alan | Kamu tasarruf-yatırım farkı 2028'de −%2,7; seçim yılı | 2029'da −%2,2 | T2029'da telafi için alan biraz daha geniş |
| T+5 | 2033; cari açık boşluğu $28–45 mlr | 2034; boşluk $25–48 mlr | T2029 uyum için bir yıl daha veriyor |
| AB takvimi | SKDM mansap genişlemesi (1.1.2028) T ile çakışıyor; çelikte eritme-döküm kuralı 1.10.2027'den tahsiste kullanılıyor; yatırım tarama tüzüğü 17.1.2028 | Bu yükler T'den önce soğurulmuş olur | T2028'de şoklar üst üste biniyor |
| AB'nin yeni STA'ları | Mercosur geçici uygulamada; Hindistan imza süreci; Endonezya Konsey'de | Hindistan ve Endonezya muhtemelen yürürlükte `[D?]` | Asimetrinin maliyeti 2028–2029'da yükseliyor. Bu, çıkış için bir gerekçe; ama Türkiye'nin kendi STA'larını müzakere süresi de kısa |
| Müzakere penceresi | ≈6 ay; yalnızca ince STA veya geçiş düzenlemesi | ≈18 ay; S3 (temel STA) gerçekçi, S2 zor | Faz 0 §2A ile uyumlu |
| Siyasi takvim | 2028 genel seçimleri | Seçim sonrası | T2028'de "takvim baskısı" riski yüksek |

**Teşhis sonucu.**
- İki takvimde de S4 kısıtlarla bağdaşmıyor.
- T2028, hazırlık süresi ve şokların üst üste binmesi bakımından belirgin şekilde daha riskli.
- Faz 2'de T2028 için bir **geçiş düzenlemesi** (mevcut tarife tercihlerinin geçici olarak sürdürülmesi; standstill), T2029 için **temel STA (S3) + menşe kolaylıkları** ana seçenek olarak değerlendirilecek.
- `[H]` Güven: Orta.

---

## 7. Faz 2'ye girdiler

| No | Hipotez | Faz 2'de nasıl sınanacak |
|---|---|---|
| H1-1 | S4 kısıtlarla bağdaşmaz; bitiş durumu olamaz, yalnızca geri dönüş planı (fallback) olur | S0–S5 karşılaştırma matrisi; çekim modeliyle S4 ticaret etkisi |
| H1-2 | S2'nin S0'a göre net etkisi: menşe maliyeti (−€1,9–5,6 mlr) ile özerklik temettüsü ve STA kazancının karşılaştırması | Faz 2'de ön hesap, Faz 5'te tarife cetveliyle kesinleştirme |
| H1-3 | Menşe maliyetini düşürmenin anahtarı tam kümülasyon (PEM), toleranslar ve tedarikçi beyanı dijitalleşmesi | Revize PEM ürüne özgü kuralları; İngiltere'deki tercih kullanım oranları |
| H1-4 | AB'nin pazarlık tutumu: hasmane AB'nin bile Türkiye ile karşılıklı sıfır tarifeye çıkarı var (AB'nin AB dışı ihracatının %4,3'ü; otomotivde üçüncü pazar) | Veto oyuncuları ve oylama (md. 207 NÇ), AB'nin karşı talepleri |
| H1-5 | STA ağı programı: önce Hindistan, Mercosur, Japonya, Meksika ve Kanada (Türkiye'nin $30 mlr ithalat kaldıracı) | Ortak bazında ilgi ve kaldıraç tablosu |
| H1-6 | IAA eşdeğerliği ve AKÇT STA'sının korunması müzakerenin kırmızı çizgileri | Hukuki yol haritası |

**Çekim modeli (VB-13).** Faz 2'de kendi tahminimiz yapılacak:
- Model: PPML; ihracatçı-yıl, ithalatçı-yıl ve ikili sabit etkiler (Yotov ve diğ., 2016).
- Veri: BACI 1996–2024.
- Amaç: GB'nin geçmiş etkisini ve DCFTA / temel STA / DTÖ senaryolarının ticaret etkisini tahmin etmek; literatürdeki aralığı (bkz. §1.7) çapraz kontrol etmek.

---

## 8. Veri boşlukları (güncel)

| No | Boşluk | Durum (17.10.2026) | Kapatma yolu (veri, kurum, süre) |
|---|---|---|---|
| VB-01 | NACE 4 haneli üretim, istihdam, katma değer | **Kapandı** | TÜİK YSHİ 2009–2024 sınıf düzeyi; 2025 Rev. 2.1 grup düzeyi |
| VB-02 | GTİP12 × ülke × rejim dış ticareti (DİR, serbest bölge) | Kısmen | TÜİK dış ticaret Qlik arayüzü tarayıcıyla okunuyor; DİR rejim alanı yok. Ticaret Bakanlığı'ndan DİR kullanım verisi talebi, 4–6 hafta; Faz 3 |
| VB-03 | 2023 girdi-çıktı tabloları | **Kapandı** | TÜİK 2023 arz, kullanım ve simetrik tablolar (8 dosya) indirildi; Faz 6 |
| VB-04 | TÜFE madde ağırlıkları (428 madde) | Kısmen | COICOP 2018 2–5. düzey ağırlıkları var; madde ağırlıkları TÜİK'ten veya HICP'den; Faz 6 |
| VB-05 | 2026 uygulanan tarife ve İGV listesi | **Kapandı** | Ticaret Bakanlığı ekleri (`kod/tarife_tr.py`) |
| VB-06 | 1/95 Ek 1 satır içeriği (İTÜ) | Açık | TARIC'teki Türkiye tercih satırları; Faz 3 |
| VB-07 | 2025 cari denge tutarsızlığı | **Kapandı** | EVDS3: −$30,276 mn; birincil gelir revizyonu (§3.1) |
| VB-08 | Türkiye'nin AB çelik kotası toplam tahsisi | Açık | DG TAXUD kota tablosu; Faz 3 |
| VB-09 | Çapa yatırımcı ve tedarikçi ağı | Açık | OSD, TAYSAD, TÜRKBESD, Sanayi Sicil; Faz 4 |
| VB-10 | DTÖ bağlı oranları, HS2022 satır düzeyi | Kısmen | HS2002 sertifikalı ve UR94 cetvelleri indirildi (WTO e-Kütüphane); HS2022 aktarımı için WTO TTD (e-posta ve captcha) veya ücretsiz WTO API anahtarı; Faz 5 |
| VB-11 | OECD ICIO / TiVA | Açık | Betikle erişimde 403; elle indirme, 1 gün; Faz 6 (yedek: TÜİK 2023 girdi-çıktı) |
| VB-12 | Seyahat gelirinin ülkelere dağılımı (AB27 payı) | Açık | TÜİK Turizm İstatistikleri (çıkış yapan ziyaretçi anketi) Veri Portalı tabloları; 1 hafta; Faz 6 |
| VB-13 | Kendi çekim modeli tahminimiz (GB etkisi, senaryolar) | **Kapandı (Faz 2)** | `kod/f2f_cekim_modeli.py`: CEPII Gravity 1988–2020 + BACI 2024, PPML ve genel denge ([`02b_secenekler_hukuk.md`](02b_secenekler_hukuk.md) §2) |
| VB-14 | Doğrudan yatırımın nihai yatırımcı ülkeye göre dağılımı | Açık | TCMB doğrudan yatırım ülke tabloları; Faz 4 |
| VB-15 | AB'nin spesifik ve bileşik vergileri için ad valorem eşdeğerleri | Açık | WITS "aveestimated" (AB, 918) veya TARIC; Faz 3 |
| VB-16 | AB'ye ihracatın taşıma şekline göre dağılımı (karayolu payı) | Açık | TÜİK dış ticaret Qlik "taşıma şekli" boyutu; 1 hafta |
| VB-17 | İl düzeyinde ihracat bileşimi | Açık | TİM ve Ticaret Bakanlığı il bazında ihracat; Faz 3 |
| VB-18 | Aktarılan AB teknik mevzuatı, Türk onaylanmış kuruluşları (NANDO), TÜRKAK'ın EA MLA statüsü | **Kapandı (Faz 2)** | NANDO: 95 Türk kaydı, ≈81'i yürürlükte; TÜRKAK dokuz alanda EA MLA imzacısı ([`02a_politika_uzayi.md`](02a_politika_uzayi.md) §2 H2) |

---

## 9. Faz 1 kalite kontrol listesi

| No | Kontrol | Sonuç |
|---|---|---|
| 1 | Her sayının etiketi, birimi ve dönemi var mı? | Evet. Tablolarda kaynak ve etiket tablo altında; metinde satır içinde. `[T]` tahminler yöntem ve P10–P50–P90 ile verildi |
| 2 | NACE toplamları makro toplamlarla tutarlı mı; çift sayım var mı? | S4 ihracat kaybı bölüm toplamı ($23,8 mlr) ile Faz 0 makro toplamı (€21,2 mlr ≈ $24,0 mlr) tutarlı; fark eşleşmeyen sınıflardan. İstihdam iki kaynakla (YSHİ, SGK) ayrı ayrı verildi, toplanmadı |
| 3 | Kısıtlar sağlanıyor mu; sağlanmıyorsa yazıldı mı? | S4'te enflasyon, istihdam, kabiliyet ve cari denge kısıtlarının ihlal sinyali açıkça yazıldı (§5) |
| 4 | Tarife önerisinde bağlı oran, ITA, STA kontrolü | Bu fazda tarife önerisi yok. DS629 ve bağsız satır kısıtı not edildi (Faz 5) |
| 5 | DTÖ uyumu | MFN ilkesinin AB'ye özel indirimi engellediği yazıldı (§3.7, §5) |
| 6 | "Pazartesi sabahı testi" | Teşhis fazı; eylem yok. Kısıt tablosundaki koşullar Faz 2 ve Faz 5'te eyleme dönüştürülecek |
| 7 | AB'nin tepkisi | Hasmane AB varsayımı (V-11) S4 olasılığına yansıtıldı. AB'nin pazarlık çıkarı H1-4'te |
| 8 | Zaman yolu | İki takvim için ayrı tablo (§6); T+5 uzantısı (§3.6) |
| 9 | Kaçınılacak 20 hatadan biri yapıldı mı? | Hata 1 (Lerner) §3.3'te; hata 3 (menşe) F-2 ve H1-3'te; hata 5 (çapa yatırımcı) §1.3'te; hata 9 (2021–25 şokları) §3.4 reel kur ve 2025 bazında ele alındı; hata 11 (CE, NANDO, TÜRKAK) VB-18'de; hata 12 (kota, vize, transit) §2.4'te; hata 16 (AKÇT) §1.3 ve §2.6'da; hata 19 (bölgesel) §4.2'de. Hata 2, 4, 6, 7, 10 ve 13–15 ilgili fazlarda ele alınacak |
| 10 | Kaçamak ifade | Kontrol edildi; öneriler bu fazda koşul düzeyinde, eylemler Faz 2'den itibaren |
| 11 | Olumsuz bulgular dürüstçe raporlandı mı? | Evet. GB'nin ölçülebilir bilançosunun pozitif olduğu (§1.8–1.9), çıkışın IAA avantajını kaybettirebileceği (§2.6) ve S4'ün kısıtları ihlal ettiği (§5) açıkça yazıldı |

---

## 10. Durum özeti

[`DURUM_OZETI.md`](DURUM_OZETI.md) dosyasında (Faz 1 sonu).

---

## Kaynaklar (Faz 1)

**Veri**
- UN Comtrade genel önizleme API'si (comtradeapi.un.org/public/v1/preview), Türkiye (792) beyanı, 1991–2025.
- Eurostat Comext DS-045409 (SDMX 2.1), AB27_2020 × TR ve AB27 × AB dışı, 1999–2025.
- CEPII BACI HS17 V202601 (22.1.2026), 2024.
- WITS/TRAINS SDMX API, ortak MFN tarifeleri (2022–2023).
- TCMB EVDS3 (evds3.tcmb.gov.tr): ödemeler dengesi ayrıntılı sunum (bie_odeayrsunum6), altın ve enerji hariç cari denge (bie_hariccariacik), GSYH harcama yöntemi (bie_gsyhhrccar), döviz kurları (bie_dkdovytl), reel efektif kur (bie_rktufey), uluslararası yatırım pozisyonu (bie_uypucay).
- TÜİK Dağıtım Yönetim Sistemi: DF_UHTI_HIZMET_COGRAFI_C, YSHİ (DF_YAPISAL_EFGTG).
- SGK İstatistik Yıllığı 2025, Tablo 1.11.
- OVP (2027–2029), RG 6.9.2026 (mükerrer), Tablo 1.1; SBB basın duyurusu 6.9.2026: https://www.sbb.gov.tr/wp-content/uploads/2026/09/Orta-Vadeli-Program_2027-2029-Basin-Duyurusu_06092026.pdf

**Literatür ve belgeler** (Faz 1 araştırma taraması)
- Aytuğ ve diğ. (2017): https://repository.bilkent.edu.tr/items/0f043d7d-4d3d-4099-9a41-74761e120b41/full
- Antonucci ve Manzocchi (2006): https://iris.luiss.it/handle/11385/3245
- Neyaptı, Taşkın ve Üngör (2007): https://ecomod.net/sites/default/files/document-conference/ecomod2003/Neyapti.pdf
- Nowak-Lehmann ve diğ. (2007): https://ideas.repec.org/p/diw/diwwpp/dp483.html
- Adam ve Moutos (2008): https://ideas.repec.org/a/bla/worlde/v31y2008i5p685-700.html
- Yılmaz (2010): https://econpapers.repec.org/paper/kocwpaper/1023.htm
- Dünya Bankası (2014): https://documents1.worldbank.org/curated/en/298151468308967367/pdf/858300ESW0P1440disclosed090260140TR.pdf
- BKP/Panteia/AESA (2016), SWD(2016) 475 Ek 6: https://ec.europa.eu/smart-regulation/impact/ia_carried_out/docs/ia_2016/turkey_anx6_en.pdf
- ifo/Bertelsmann (2016): https://www.bertelsmann-stiftung.de/en/topics/latest-news/2016/juli/turkey-and-the-eu-have-to-expand-their-trade
- Dursun (2023): https://ideas.repec.org/a/eee/inteco/v173y2023icp143-163.html
- 1/95 sayılı Karar: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:21996D0213(01)
- ACEA (Temmuz 2026): https://www.acea.auto/files/ACEA_fact_sheet_EU_Turkiye_vehicle_trade-July_2026.pdf
- Otomotiv ihracatı 2025: https://www.capital.com.tr/sektorler/otomotiv/otomotiv-ihracati-2025te-415-milyar-dolara-cikti ; https://www.aa.com.tr/en/turkiye/turkiye-seeks-full-inclusion-in-eu-s-made-in-eu-automotive-policy/4000478
- Duruiz, GERPISA: https://gerpisa.org/ancien-gerpisa/actes/20/article1.html
- TÜRKBESD 2025: https://www.cnbce.com/is-dunyasi/beyaz-esya-sektoru-2025te-daraldi-h23808
- İHKİB 2025 hazır giyim ihracat raporu: https://www.ihkib.org.tr/content/files/uploads/289/2025-annual-apparel-export-report.pdf
- Eurostat SiF KS-SF-07-063: https://edz.bib.uni-mannheim.de/edz/pdf/statinf/07/KS-SF-07-063-EN.pdf
- DG HOME vize istatistikleri: https://home-affairs.ec.europa.eu/news/visa-applications-reach-117-million-eu-and-schengen-associated-countries-2025-05-20_en ; 2025: https://www.hurriyetdailynews.com/turkiye-takes-2nd-place-in-global-schengen-visa-applications-222665
- EEAS, kademeli vize kuralları: https://www.eeas.europa.eu/delegations/t%C3%BCrkiye/more-favourable-visa-rules-turkish-citizens-applying-schengen-visas_en
- ATAD C-65/16 *Istanbul Lojistik*: https://op.europa.eu/fi/publication-detail/-/publication/dd7712f7-de44-11e7-a506-01aa75ed71a1/language-en
- Karayolu kotaları: https://www.ekonomigazetesi.com/sektor-haberleri/nakliyeciler-vize-ve-transite-cozum-ariyor-51114 ; https://avesis.iuc.edu.tr/yayin/caee4b9d-513a-4e7a-99ad-9ed0f52aef27/effects-of-quotas-on-turkish-foreign-trade-a-gravity-model
- Doğrudan yatırım: https://www.milliyet.com.tr/7555931 ; YASED: https://turob.com/assets/Istatistikler-Dosyalari-image/2025/YASED_Rakamlarla-UDY_2025-Eylul.pdf ; EEAS bilgi notu (Mayıs 2024)
- HMB Aralık 2025 bütçe gerçekleşme raporu: https://ms.hmb.gov.tr/uploads/sites/23/2026/01/2025-Aralik-Aylik-Butce-Gerceklesme-Raporu_V2_14.01.2026-e6324968422ea9d9.pdf
- DG TRADE Türkiye sayfası: https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/turkiye_en
- Ticaret Bakanlığı, müzakeresi süren STA'lar: https://ticaret.gov.tr/dis-iliskiler/serbest-ticaret-anlasmalari/muzakere-sureci-devam-eden-stalar

---

İLERLEME: Faz 0–1 tamamlandı / Faz 2–9 kaldı — SONRAKİ ADIM: Faz 2, S0–S5 seçenek karşılaştırması, önerilen bitiş durumu ve hukuki yol haritası (AB, DTÖ, iç hukuk); iki takvim için ayrı ayrı. **DEVAM bekleniyor.**
