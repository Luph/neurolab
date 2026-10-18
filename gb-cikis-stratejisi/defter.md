# Kümülatif defter

Her NACE grubu tamamlandığında güncellenir. Toplamlar Faz 6'daki makro mutabakatta kullanılır.

**Son güncelleme:** Faz 1, 17 Ekim 2026. Faz 3 başlamadığı için sınıf düzeyinde katkı yok.

| Kalem | Değer | Not |
|---|---|---|
| Tamamlanan / kalan sınıf sayısı | 0 / 230 C sınıfı; 0 / 29 ek kapsam satırı (B 15, D 1, E 2, A 3, hizmet 8) | Kapsam listesi: `veri/nace_kapsam.csv` |
| Kullanılan / kalan enflasyon bütçesi (bp) | Birinci tur: 0 / 50 (yıllık tavan 30). İkinci tur dahil: 0 / 100 | V-05 |
| Kümülatif cari denge katkısı (milyar $) | 0 | P10–P50–P90, Faz 3'ten itibaren |
| Kümülatif mali maliyet (milyar TL ve GSYH %) | 0 | Tavan: GSYH'nin %0,5'i/yıl (2026'da ≈ $9,1 mlr; 2028'de ≈ $10,5 mlr) |
| Riskteki istihdam | Teşhis tabanı (S4, statik, telafisiz): 207 bin (P10–P90: 135–297 bin). Sınıf düzeyinde dağılım Faz 3'te | `01_teshis.md` §4.1; YSHİ 2024 bazı |
| Açık kalan veri boşlukları | VB-02, 04, 06, 08–18 (kapanan: VB-01, 03, 05, 07) | `01_teshis.md` §8 |
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
