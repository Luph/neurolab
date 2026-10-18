# Kümülatif defter

Her NACE grubu tamamlandığında güncellenir. Toplamlar Faz 6'daki makro mutabakatta kullanılır.

**Son güncelleme:** Faz 3 parça 1 (10 Gıda, 11 İçecekler, 12 Tütün), 18 Ekim 2026. Sınıf düzeyi değerler `veri/nace_matris.csv`'den; parça ayrıntısı [`nace_kartlar_10-12.md`](nace_kartlar_10-12.md) §5.

| Kalem | Değer | Not |
|---|---|---|
| Tamamlanan / kalan sınıf sayısı | 33 / 197 C sınıfı (10–12 tamam); 0 / 29 ek kapsam satırı (B 15, D 1, E 2, A 3, hizmet 8) | Kapsam listesi: `veri/nace_kapsam.csv` |
| Kullanılan / kalan enflasyon bütçesi (bp) | Birinci tur, 10–12. Önlemler: S2 yolu −0,11, S4 yolu −1,55. Çıkış şokları (önlem değil): S2 +0,9, S4 +6,2 (c2). Net: S2 0,8 / 50; S4 4,7 / 50 (yıllık tavan 30). İkinci tur dahil Faz 6'da | V-05; `nace_kartlar_10-12.md` Tablo 5.1 |
| Kümülatif cari denge katkısı (milyar $) | 10–12, T+5, yıllık. Senaryo P50: S2 −0,044, S4 +0,030 (S4 P10 −1,06; 1/98 askısı). Önlemler: S2 +0,071, S4 +0,010 `[T]`/`[H]` | P10–P50–P90 kartlarda |
| Kümülatif mali maliyet (milyar TL ve GSYH %) | 10–12: S2 yolu 0,83 mlr TL/yıl, S4 yolu 1,69 mlr TL/yıl (GSYH'nin %0,001–0,002'si) | Tavan: GSYH'nin %0,5'i/yıl (2026'da ≈ $9,1 mlr; 2028'de ≈ $10,5 mlr) |
| Riskteki istihdam | 10–12: S2 P50 −284; S4 P50 −15, P10 −4.698 (10.39 −3.215; P10'da −%4,9). Faz 3 yöntemiyle imalatın tamamı (geçici, diğer parçalarda kartlarla gözden geçirilecek): S2 P50 −22,5 bin (P10 −38,7); S3 −30,4 bin; S4 −41,2 bin (P10 −64,6), kaybı %5'i aşan sınıf S4 P50'de 9, P10'da 15. Teşhis tabanı (S4, statik, telafisiz): 207 bin brüt | `veri/f3_senaryo_ozet.csv`; `01_teshis.md` §4.1 |
| Açık kalan veri boşlukları | VB-02, 04, 06, 08–12, 14–17, 21–27, 30–35 (kapanan: VB-01, 03, 05, 07, 13, 18) | `01_teshis.md` §8; `nace_kartlar_10-12.md` Tablo 5.1 |
| Varsayım kaydına eklenen yeni maddeler | V-01 … V-37 (Faz 3: V-30–V-37 senaryo kalibrasyonu, 1/98 askı olasılığı, ProTEE σ, sınır sürtünmesi, arketip eşikleri, SS, CKE, KN8 eşlemesi) | `00_plan.md` §3 |

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
| Zaman kritik DTÖ eylemi | XXVIII:5 çekincesi, son tarih 31.12.2026; DS629 DSB, 27.10.2026 | `[V]` §7 |

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
| 10–12 S4 kuyruk riski (1/98 askısı, P10) | AB'ye ihracat −$2,0 mlr, cari denge −$1,06 mlr, istihdam −4,7 bin; yarıdan fazlası 10.39 | `[T]` |
| İmalat (230 sınıf), AB'ye ihracat değişimi P50 (P10 / P90) | S2 −%11,0 (−23,4 / +2,0); S3 −%14,9 (−26,4 / −2,9); S4 −%19,1 (−29,7 / −7,9) | `[T]` GE kalibrasyonu |
| İmalat, cari denge P50 (P10 / P90), T+5, yıllık | S2 −$2,7 mlr (−4,2 / −2,0); S3 −$3,5 mlr; S4 −$4,2 mlr (−6,3 / −2,9) | `[T]` geçici |
| İmalat, birinci tur TÜFE (c2 ve sürtünme), P50 | S2 10,9 bp; S3 20,7 bp; S4 69,1 bp (59–79) | `[T]` Faz 2A ile tutarlı (73 bp) |
| Arketip dağılımı (kural + 10–12 düzeltmesi) | A 53, — 49, B 39, G 33, C 30, D 17, F 8, E 1 | `[H]` `veri/nace_matris.csv`; diğer parçalarda düzeltilecek |
| Düzeltmeler | D-1 KN8 → NACE ağırlıkları; D-2 KKTC akımları; D-3 "%5'i aşan 21 sınıf" yerine 9 (P50) / 15 (P10) | `nace_kartlar_10-12.md` §0 |

