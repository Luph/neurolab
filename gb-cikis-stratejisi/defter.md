# Kümülatif defter

Her NACE grubu tamamlandığında güncellenir. Toplamlar Faz 6'daki makro mutabakatta kullanılır.

**Son güncelleme:** Faz 2A, 18 Ekim 2026. Faz 3 başlamadığı için sınıf düzeyinde katkı yok.

| Kalem | Değer | Not |
|---|---|---|
| Tamamlanan / kalan sınıf sayısı | 0 / 230 C sınıfı; 0 / 29 ek kapsam satırı (B 15, D 1, E 2, A 3, hizmet 8) | Kapsam listesi: `veri/nace_kapsam.csv` |
| Kullanılan / kalan enflasyon bütçesi (bp) | Birinci tur: 0 / 50 (yıllık tavan 30). İkinci tur dahil: 0 / 100 | V-05 |
| Kümülatif cari denge katkısı (milyar $) | 0 | P10–P50–P90, Faz 3'ten itibaren |
| Kümülatif mali maliyet (milyar TL ve GSYH %) | 0 | Tavan: GSYH'nin %0,5'i/yıl (2026'da ≈ $9,1 mlr; 2028'de ≈ $10,5 mlr) |
| Riskteki istihdam | Teşhis tabanı (S4, statik, telafisiz): 207 bin brüt (P10–P90: 135–297 bin). Net (ithal ikamesi dahil): −117 bin (−77 ile −165 bin); %5 eşiğini aşan 22 sınıf (σ = 5). Sınıf düzeyinde karar Faz 3'te | `01_teshis.md` §4.1; `02a_politika_uzayi.md` §4.2 |
| Açık kalan veri boşlukları | VB-02, 04, 06, 08–17, 21–27 (kapanan: VB-01, 03, 05, 07, 18) | `01_teshis.md` §8; `02a_politika_uzayi.md` §9 |
| Varsayım kaydına eklenen yeni maddeler | V-01 … V-29; Faz 1'de V-06 ve V-07 baz değerleri güncellendi | `00_plan.md` §3 |

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
| Vergi takası, on grup (T-A, merkez) | TÜFE −2 bp (pasif +35); net mali −$0,46 mlr (−0,56 ile +0,10); istihdam +20 bin (12–22) | `[T]` `veri/politika_takas_ozet.csv` |
| Otomobil takası | ÖTV %65 → %56,2; AB +%4,1, yerli −%5,4; net mali −$0,15 mlr; T-0 (yalnızca yerli) eşdeğeri −$3,0 mlr ve DTÖ'ye aykırı | `[T]` §1.5 |
| Gümrük vergisi tahsilat oranı | Toplam %50 (2025: $8,15 mlr gerçekleşme / $16,2 mlr yasal); tüketim ve karma mallarda %100, diğerlerinde %38 | `[V]`/`[T]` §3.4 |
| AB'nin S4 ihracat kaybı (σ = 5) | b $16,4 mlr; c $18,7 mlr; c2 $28,5 mlr; a $31,1 mlr | `[T]` §4.1 |
| İhracat tarafı tam telafi maliyeti | Yılda ≈$38 mlr (2028 GSYH'sinin %1,8'i); telafi edici vergiye açık | `[T]` §5 |
| Zaman kritik DTÖ eylemi | XXVIII:5 çekincesi, son tarih 31.12.2026; DS629 DSB, 27.10.2026 | `[V]` §7 |

