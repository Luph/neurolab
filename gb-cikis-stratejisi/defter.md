# Kümülatif defter

Her NACE grubu tamamlandığında güncellenir. Toplamlar Faz 6'daki makro mutabakatta kullanılır.

**Son güncelleme:** Faz 3 parça 3 (16 Ağaç, 17 Kâğıt, 18 Basım), 22 Kasım 2026. Değerler 10–18'in kümülatif toplamı (72 sınıf). Sınıf düzeyi değerler `veri/nace_matris.csv`'den; parça ayrıntısı [`nace_kartlar_16-18.md`](nace_kartlar_16-18.md), [`nace_kartlar_13-15.md`](nace_kartlar_13-15.md) ve [`nace_kartlar_10-12.md`](nace_kartlar_10-12.md) Bölüm 6. Grup toplamlarının yüzdelikleri çekilişlerin toplamından (V-38). Parça 3'teki model düzeltmesi (V-49) ilk iki parçanın S2 sonuçlarını değiştirdi; aşağıdaki değerler güncel modelle.

| Kalem | Değer | Not |
|---|---|---|
| Tamamlanan / kalan sınıf sayısı | 72 / 158 C sınıfı (10–12, 13–15 ve 16–18 tamam); 0 / 29 ek kapsam satırı (B 15, D 1, E 2, A 3, hizmet 8) | Kapsam listesi: `veri/nace_kapsam.csv` |
| Kullanılan / kalan enflasyon bütçesi (bp) | Birinci tur, 10–18. Çıkış şokları (önlem değil): S2 +2,8, S4 +22,7 (c2; 13–15'in payı 15,6, 16–18'in 0,9). Önlemler: S2 yolu −0,11, S4 yolu −13,76 (13–15'te KDV takası −12,0; 16–18'de ambalaj kâğıdında c2 düzeltmesi −0,2). Net: S2 2,7 / 50; S4 8,9 / 50 (yıllık tavan 30). İkinci tur dahil Faz 6'da | V-05, V-43, V-48; `nace_kartlar_16-18.md` Tablo 6.1 |
| Kümülatif cari denge katkısı (milyar $) | 10–18, T+5, yıllık. Senaryo P50: S2 −0,95, S4 −2,65 (S4 P10 −3,96; 1/98 askısında ortalama −3,36). Önlemler: S2 +0,22, S4 +0,01 `[T]`/`[H]`. 16–18'in katkısı olumlu: S2 +0,04, S4 +0,10 (kâğıtta ithal ikamesi, üst sınır) | `veri/f3_senaryo_grup.csv`, `veri/f3_senaryo_aski.csv` |
| Kümülatif mali maliyet (milyar TL ve GSYH %) | 10–18: S2 yolu 2,04 mlr TL/yıl (%0,003), S4 yolu 23,85 mlr TL/yıl (%0,032); S4'ün 17,5'i KDV takasının net maliyeti | Tavan: GSYH'nin %0,5'i/yıl (2026'da ≈ $9,1 mlr; 2028'de ≈ $10,5 mlr) |
| Riskteki istihdam | 10–18: S2 P50 −15.498; S4 P50 −39.733, P10 −61.720; 1/98 askısında ortalama −42.507. S4 P10'da kaybı %5'i aşan sınıflar: 13.20, 13.91, 13.92, 14.13, 14.14, 14.19, 14.31, 14.39 (trikoda −%19,2). PEM kümülasyonu kanalı S4'te −4.750. 16–18'in katkısı: S2 +163, S4 +471. Faz 3 yöntemiyle imalatın tamamı (geçici): S2 P50 −24,9 bin (P10 −43,9); S3 −28,1 bin; S4 −46,2 bin (P10 −70,3), kaybı %5'i aşan sınıf S4 P50'de 9, P10'da 17. Teşhis tabanı (S4, statik, telafisiz): 207 bin brüt | `veri/f3_senaryo_ozet.csv`; `01_teshis.md` §4.1 |
| Açık kalan veri boşlukları | VB-02, 04, 06, 08–12, 14–17, 21–27, 30–44 (kapanan: VB-01, 03, 05, 07, 13, 18). VB-32 13–18'de bağlayıcı değil | `01_teshis.md` §8; `nace_kartlar_16-18.md` Ek E |
| Varsayım kaydına eklenen yeni maddeler | V-01 … V-49 (Faz 3: V-30–V-39 senaryo kalibrasyonu, 1/98 askı olasılığı, ProTEE σ, sınır sürtünmesi, arketip eşikleri, SS, CKE, KN8 eşlemesi, grup yüzdelikleri, eylem takvimi; parça 2: V-40 PEM kümülasyonu kanalı, V-41 tekstil ve giyim menşe parametreleri, V-42 geri ödeme yasağı, V-43 KDV takası; parça 3: V-44 iç ikame tavanı, V-45 CE payı, V-46 ağaç ve kâğıtta menşe, V-47 EUDR payı üst sınır, V-48 ambalaj kâğıdında c2 düzeltmesi, V-49 S2'de menşe maliyeti yalnız tarifeli üründe) | `00_plan.md` §3 |

## Teşhis tabanı (Faz 1)

Sınıf kartlarının ve makro köprünün karşılaştırılacağı başlangıç değerleri.

| Gösterge | Değer | Kaynak ve etiket |
|---|---|---|
| Cari denge 2025 | −$30,3 mlr (−%1,9 GSYH) | `[V]` EVDS3 |
| Altın ve enerji hariç (çekirdek) cari denge 2025 | +$37,1 mlr (+%2,3) | `[V]` EVDS3 |
| Cari denge, 12 ay (Eyl 2025–Ağu 2026) | −$42,1 mlr; çekirdek +$26,0 mlr | `[V]` EVDS3 |
| OVP cari denge patikası 2027 / 2028 / 2029 | −%1,9 / −%1,8 / −%1,6 | `[V]` OVP Tablo 1.1 |
| T+5 cari denge hedef boşluğu (2033 / 2034) | $28–45 mlr / $25–48 mlr | `[H]` `01_teshis.md` §3.6 |
| TÜFE yıl sonu 2026 / 2027 / 2028 / 2029 | %28,4 / %21,0 / %13,5 / %9,0 | `[V]` OVP |
| İmalat istihdamı | YSHİ 5,03 mn (2024); SGK 4/a 4,03 mn (2025) | `[V]` |
| AB ihracatına doğrudan bağlı imalat istihdamı | 858 bin (YSHİ bazı); 675 bin (SGK bazı) | `[T]` §4 |
| S4 statik ihracat kaybı (σ = 3 / 5 / 8) | −€13,8 / −21,2 / −30,4 mlr | `[T]` Faz 0 S4 hesabı |
| S4 TÜFE birinci tur (pasif): yalnızca MFN / MFN + İGV | 32–42–53 bp / 59–78–98 bp (girdi-çıktı modeli; ilk kaba hesap 21–40 / 46–86 bp) | `[T]` `veri/politika_io_s4_tufe.csv` |
| STA asimetrisi: Türk ihracatının ödediği MFN | $1,2 mlr (yürürlükte) + $0,3 mlr (bekleyen) | `[T]` §2.1 |

## Politika uzayı tabanı (Faz 2A)

Faz 3–6'daki kararların karşılaştırılacağı referans değerler. Ayrıntı: [`02a_politika_uzayi.md`](02a_politika_uzayi.md).

| Gösterge | Değer | Kaynak ve etiket |
|---|---|---|
| S4 TÜFE birinci tur, pasif (MFN + İGV) | 59 / 78 / 98 bp (ρ = 0,6 / 0,8 / 1,0); κ = 0,5 ile ≈182 bp | `[T]` `veri/politika_s4_aktif.csv` |
| Aktif S4 önerilen paket: c2 + P1 + geniş takas | TÜFE 2,5 / 3,3 / 4,1 bp; net mali +%0,05 GSYH (tahsil edilebilir); takas maliyeti $5,7 mlr; koruma kaybı 0 | `[T]` §4.1 |
| Aktif S4 alternatifleri (ρ = 0,8) | c + dar 7,5 bp, −%0,02; a + geniş 4,0 bp, +%0,07; b 1,5 bp, −%0,04 ve $2,9 mlr koruma kaybı | `[T]` §4.1 |
| Vergi takası, on grup (T-A, rejim c2, merkez) | TÜFE 0 bp (pasif +47); net mali −$0,60 mlr (−0,71 ile +0,13); istihdam +31 bin (18–36). Rejim c'de pasif +35 bp, takas −$0,46 mlr | `[T]` `veri/politika_takas_ozet.csv` |
| Otomobil takası | ÖTV %65 → %56,2; AB +%4,1, yerli −%5,4; net mali −$0,15 mlr; T-0 (yalnızca yerli) eşdeğeri −$3,0 mlr ve DTÖ'ye aykırı | `[T]` §1.5 |
| S4 net imalat istihdamı (σ = 5) | Yalnızca MFN −117 bin; c2 −48 bin; c2 + takas ≈ −35 bin; giyim −58,7 bin | `[T]` `veri/politika_s4_net_istihdam_ozet.csv` |
| Gümrük vergisi tahsilat oranı | Toplam %50 (2025: $8,15 mlr gerçekleşme / $16,2 mlr yasal); tüketim ve karma mallarda %100, diğerlerinde %38 | `[V]`/`[T]` §3.4 |
| AB'nin S4 ihracat kaybı (σ = 5) | b $16,4 mlr; c $18,7 mlr; c2 $28,5 mlr; a $31,1 mlr | `[T]` §4.1 |
| İhracat tarafı tam telafi maliyeti | Yılda ≈$38 mlr (2028 GSYH'sinin %1,8'i); telafi edici vergiye açık | `[T]` §5 |
| Zaman kritik DTÖ eylemi | XXVIII:5 çekincesi, son tarih 31.12.2026; DS629 DSB, 27.10.2026 (Faz 2C'de 24.11.2026'ya uzadığı tespit edildi) | `[V]` §7 |

## Seçenekler tabanı (Faz 2B)

S0'a (GB) göre yerleşmiş etkiler. Ayrıntı: [`02b_secenekler_hukuk.md`](02b_secenekler_hukuk.md) §2.

| Gösterge | S2 DCFTA | S3 ITA | S4 | Kaynak |
|---|---|---|---|---|
| TR → AB ihracatı (GE, σ = 7; %90 GA) | −%11 (−27 ile +6) | −%18 (ihtiyatlı) ile +%1 (Türkiye–BK) | −%19 (−32 ile −5) | `[T]` `veri/politika_cekim_senaryolar.csv` |
| Türkiye toplam ihracatı (GE) | −%3,3 | −%5,3 ile +%1,1 | −%6,2 | `[T]` |
| Türkiye reel GSYH, refah vekili (GE) | −%0,22 (−0,56 ile +0,19) | −%0,35 ile +%0,10 | −%0,43 (−0,73 ile −0,10) | `[T]` |
| TÜFE birinci tur (bp) | +2 ile +12 (menşe maliyeti) | +2 ile +12 | 2,5–4,1 (aktif) | `[T]` 02a, f2e |
| Net imalat istihdamı (bin) | ≈ −33 (kaba, GE kanalı) | −54 ile +12 | ≈ −35 (aktif, sınıf düzeyi) | `[T]` |

## Hazırlık tabanı (Faz 2C)

Karar öncesi hamlelerin değer ölçüleri ve zamanlama kısıtları. Ayrıntı: [`02c_hazirlik.md`](02c_hazirlik.md).

| Gösterge | Değer | Kaynak ve etiket |
|---|---|---|
| Hamleler | 51: 11 A, 26 B, 14 C. Hiçbirinin çıkış olmazsa değeri negatif değil | `[H]` `veri/hazirlik_hamleler_oncelik.csv` |
| Sessiz pencere (bugün → K) | T2028 ≈1 ay (K Kasım 2026); T2029 ≈5 ay (K Mart 2027) | `[H]` §13 |
| 33 pazarla STA: S4 GSYH kaybının telafisi (σ = 5 / 7) | Pazar erişimi %14 / %23; karşılıklı %42 / %69. GB içinde GSYH +%0,08–0,30 | `[T]` `veri/hazirlik_sta_ge.csv` |
| STA'ların statik gümrük geliri kaybı | Yılda $1,9 mlr sanayi (GSYH'nin %0,12'si); bütün ürünler $3,2 mlr | `[T]` `veri/hazirlik_sta_tarife.csv` |
| PEM dışı ithal ara girdi payı (AB ihracatı ağırlıklı) | %13,1 (bütünleşik üst sınır ≈%21). Otomobil göstergesi %36 (kural %45) | `[T]` `veri/hazirlik_pem_*.csv` |
| SKDM: AB'ye ödeme, 2028 (merkez fiyat) | Varsayılan €2.593 mn; doğrulanmış €676 mn; yurt içi fiyat AB'ye eşitse AB'ye €81 mn ve Türkiye'de €595 mn | `[T]` `veri/hazirlik_skdm.csv` |
| SKDM: AB'ye ödeme, 2034 | Varsayılan €3.795 mn; doğrulanmış €1.398 mn | `[T]` |
| SKDM aşağı akış önerisi (1.1.2028) | €10,9 mlr ihracat; yük 2028'de €245 mn (varsayılan) / €77 mn (doğrulanmış) | `[T]` `veri/hazirlik_skdm_asagi.csv` |
| Net rezerv (IMF şablonu, Eylül 2026) | $41,6 mlr; brüt $171,6 mlr (9.10.2026) | `[V]`/`[T]` `veri/hazirlik_makro_rezerv.csv` |
| İlan şokunun 12 aylık rezerv etkisi | Kurallı $30–48 mlr; düzensiz $67–90 mlr | `[H]` `veri/hazirlik_makro_tampon.csv` |
| Gerekli net rezerv (makro kapı) | Kurallı ilan $68 mlr; düzensiz $110 mlr. Açık $27 / $69 mlr | `[T]` `veri/hazirlik_makro_kapi.csv` |
| Zaman kritik tarihler | XXVIII:5 31.12.2026; DS629 kabul ya da temyiz 24.11.2026 (WT/DS629/6; 02a'daki 27.10.2026 uzatıldı); ETS izleme planları 27.10.2026; ilk SKDM beyanı 30.9.2027 | `[V]` §1.3 |

## Faz 3 tabanı (parça 1: 10–12)

Sınıf kartlarının toplamları. Faz 3 yöntemi: toplamlar Faz 2B genel dengesine kalibre, dağılım kısmi denge (`kod/f3e_senaryo.py`). Ayrıntı: [`nace_kartlar_10-12.md`](nace_kartlar_10-12.md).

| Gösterge | Değer | Kaynak ve etiket |
|---|---|---|
| 10–12 ağırlığı | İstihdam 636 bin (imalatın %12,6'sı); KD $23,3 mlr; ihracat $24,1 mlr (%9,6); AB'ye ihracat $6,2 mlr (%5,9) | `[V]` YSHİ 2024, BACI 2024 |
| AB'ye ihracatın rejimi (10–12) | Tarım (1/98) %75, İTÜ %24, GB %1 | `[V]`/`[T]` Comext 2025 |
| S4'te AB tarifesi artışı (rota A / 1/98 kaybıyla) | %3,3 / %11,5 (10–12); imalat %5,6 / %6,0 | `[T]` `veri/f3_ab_tarife_sinif.csv` |
| 10–12, bölüm toplamı P50 (P10 / P90), T+5 | S2: AB'ye ihracat −$202 mn (−446 / +125), istihdam −299, cari denge −$44 mn. S4: AB'ye ihracat −$406 mn (−1.840 / −171), istihdam −106 (−3.982 / +258), cari denge +$8 mn (−934 / +104) | `[T]` `veri/f3_senaryo_grup.csv` (V-38) |
| 10–12, S4'te 1/98 askısı (koşullu ortalama; olasılık 0,25) | AB'ye ihracat −$1,72 mlr (askı olmadan −$0,34 mlr), cari denge −$0,86 mlr, istihdam −3,7 bin (P90 / P10: −2,0 / −5,7 bin); askıdan doğan ek kaybın %77'si 10.39'da | `[T]` `veri/f3_senaryo_aski.csv` |
| İmalat (230 sınıf), AB'ye ihracat değişimi P50 (P10 / P90) | S2 −%11,0 (−23,4 / +2,0); S3 −%14,2 (−25,9 / −2,1; parça 3 sonrası); S4 −%19,1 (−29,7 / −7,9) | `[T]` GE kalibrasyonu |
| İmalat, cari denge P50 (P10 / P90), T+5, yıllık | Parça 3 sonrası: S2 −$2,8 mlr (−4,3 / −2,0); S3 −$3,2 mlr; S4 −$4,7 mlr (−6,9 / −3,4); S4'e PEM kümülasyonu kanalı dahil | `[T]` geçici |
| İmalat, birinci tur TÜFE (c2 ve sürtünme), P50 | Parça 3 sonrası: S2 10,7 bp; S3 20,3 bp; S4 69,1 bp (59–79) | `[T]` Faz 2A ile tutarlı (73 bp) |
| Arketip dağılımı (kural + 10–18 düzeltmesi) | A 56, — 55, B 40, C 31, G 22, D 17, F 8, E 1 | `[H]` `veri/nace_matris.csv`; diğer parçalarda düzeltilecek |
| Düzeltmeler | D-1 KN8 → NACE ağırlıkları; D-2 KKTC akımları; D-3 "%5'i aşan 21 sınıf" yerine 9 (P50) / 17 (P10) | `nace_kartlar_10-12.md` Ek D |

## Faz 3 tabanı (parça 2: 13–15)

Ayrıntı: [`nace_kartlar_13-15.md`](nace_kartlar_13-15.md).

| Gösterge | Değer | Kaynak ve etiket |
|---|---|---|
| 13–15 ağırlığı | İstihdam 1.238 bin (imalatın %24,6'sı); KD $22,5 mlr; ihracat $35,9 mlr (%14,3); AB'ye ihracat $17,3 mlr (%16,4) | `[V]` YSHİ 2024, BACI 2024 |
| AB'ye ihracatın rejimi ve S4 tarifesi | GB %100; S4'te AB tarifesi %10,2 (tekstil %7,3, giyim %11,8, deri %7,4); giyimde AB'ye ihracatın %98'i ≥ %10 tarifeli satırlarda | `[V]`/`[T]` Comext 2025, KN 2026 |
| 13–15, grup toplamı P50 (P10 / P90), T+5 | S2: AB'ye ihracat −$1.854 mn (−4.010 / +347), istihdam −14.419 (−30.880 / +1.234), cari denge −$893 mn. S4: AB'ye ihracat −$4.104 mn (−6.394 / −1.698), istihdam −39.397 (−60.851 / −20.019), cari denge −$2.634 mn (−3.841 / −1.473) | `[T]` `veri/f3_senaryo_grup.csv` |
| PEM kümülasyonu (S4) | Ortaklara kumaş ve teknik tekstil ihracatı $1.736 mn; maruziyet $1.131 mn (Fas 613); S4 kaybı −$673 mn (−858 / −483), istihdam −4.750 | `[T]` `veri/f3_pem_ortak_ab_payi.csv`; V-40 `[H]` |
| TÜFE (birinci tur, P50) | S2 1,7 bp; S4 15,6 bp (dış giyim 4,3, ayakkabı 3,9); KDV takasıyla S4 3,6 bp | `[T]` f3e; Faz 2A Tablo 1.5a |
| Bölgeler (S4 P50) | İstanbul −12.209; Mardin–Batman–Şırnak–Siirt −3.388 (13–15 bölge imalatının %78'i); Bursa −2.873; Tekirdağ −2.341; Gaziantep −2.228 | `[T]` f3b bölge payları |
| Duruşlar | Geliştir 11, Dönüştür 2 (14.13, 15.11), Yönetilen uyum 3 (14.14, 14.19, 14.39), Koru 5 | `[H]` |
| Düzeltmeler | D-4 EUDR (Tüzük 2026/2102: sığır derisi kapsam dışı); D-5 10–12'nin S2 sayıları; D-6 Faz 2'nin giyim tahmini (−59 bin) geçersiz | `nace_kartlar_13-15.md` Ek D |

## Faz 3 tabanı (parça 3: 16–18)

Ayrıntı: [`nace_kartlar_16-18.md`](nace_kartlar_16-18.md).

| Gösterge | Değer | Kaynak ve etiket |
|---|---|---|
| 16–18 ağırlığı | İstihdam 245 bin (imalatın %4,9'u); KD $7,3 mlr; ihracat $5,8 mlr (%2,3); AB'ye ihracat $1,4 mlr (%1,3); ithalat $5,0 mlr, %52'si AB'den | `[V]` YSHİ 2024, BACI 2024 |
| AB'ye ihracatın rejimi ve S4 tarifesi | GB %100; S4'te AB tarifesi %1,3 (ağaç %4,6, kâğıt %0,2; ahşap levha %6,9) | `[V]`/`[T]` Comext 2025, KN 2026 |
| 16–18, grup toplamı P50 (P10 / P90), T+5 | S2: AB'ye ihracat −$75 mn (−168 / +28), istihdam +163 (−375 / +815), cari denge +$41 mn. S4: AB'ye ihracat −$134 mn (−219 / −58), istihdam +471 (−8 / +964), cari denge +$101 mn (+3 / +197) | `[T]` `veri/f3_senaryo_grup.csv` |
| İthalat tarafı (S4) | AB'den kâğıt ve karton ithalatı −$239 mn; yerli üretim +$155 mn (c2; üst sınır). TÜFE 0,9 bp; ambalaj kâğıdında c2 düzeltmesiyle 0,7 bp | `[T]` f3e |
| Çıkıştan bağımsız AB araçları | EUDR 30.12.2026 (Türkiye düşük risk; Fasıl 49 kapsam dışı); PPWR 12.8.2026; huş kontrplağında anti-damping genişletmesi (2024/1287), süre sonu gözden geçirmesi 6.11.2026 | `[V]` |
| Türkiye'nin kâğıt korunma önlemleri | Testliner ve fluting: CB Kararı 8651, 28.7.2024–7.2027, $87/86/85 ton; AB menşelisi kapsamda. Kaplamalı kâğıt soruşturması (Tebliğ 2026/3) sürüyor | `[V]` |
| Duruşlar | Geliştir 5 (16.21, 16.22, 17.12, 17.22, 18.13), Koru 13 | `[H]` |
| Düzeltmeler | D-7 kâğıt hamurunda iç ikame (17.11); D-8 S2'de menşe maliyeti yalnız tarifeli üründe: 13–15 S2 istihdamı −14.419 → −15.453, 10–12 −286 → −318; D-9 Faz 2C son tarihleri (DS629 24.11.2026, XXVIII:5 31.12.2026) | `nace_kartlar_16-18.md` Ek D |
