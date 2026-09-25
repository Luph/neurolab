# FonAlfa · Google Ads görsel öğeleri

fonalfa.com'un tasarım dilinden türetilmiş reklam öğeleri: krem kâğıt zemin (`#F4F1EA`),
başlığın altındaki çift çizgi, Fraunces logo, yeşil/kırmızı net akış çubukları
(`#1A6B36` / `#B42318`), fon büyüklüğü haritası, zaman serisi ve KPI kartları.
Renkler sitenin `:root` tokenlarından alındı; logo ve favicon sitedeki SVG'lerin kendisi.

## İçerik

| Klasör | Kullanım | Ölçüler | Sınır |
|---|---|---|---|
| `out/duyarli-goruntulu/` | Duyarlı Görüntülü Reklam (RDA), Performance Max, Demand Gen görselleri | 1200×628 (1.91:1), 1200×1200 (1:1), 960×1200 (4:5) | ≤5 MB |
| `out/logolar/` | Logo öğeleri: α işareti (kare), "Fonα" yazılı kare (açık ve koyu), yatay | 1200×1200 (1:1), 1200×300 (4:1) | ≤5 MB |
| `out/banner/` | Yüklenen görüntülü reklamlar (HTML5 değil, statik PNG) | 300×250, 336×280, 250×250, 200×200, 728×90, 970×90, 468×60, 320×50, 970×250, 320×100, 300×600, 160×600 | ≤150 KB |
| `metinler.json` | RDA / PMax metin öğeleri | başlık ≤30, uzun başlık ≤90, açıklama ≤90 (ilki ≤60), işletme adı ≤25 | — |

Duyarlı görsellerde dört sahne var, her biri üç oranda:

- `net-akis` — "Net akış · kırılım" çubuk grafiği (ortadan ayrışan giriş/çıkış)
- `harita` — "Fon büyüklüğü haritası" (alan = varlık, renk = akış oranı)
- `zaman-serisi` — günlük net akış sütunları + kümülatif çizgi
- `ozet-kartlari` — üst bölümdeki KPI kartları, yön okları ve sparkline ile

## Google kurallarına uyum

**Duyarlı / PMax görselleri (`duyarli-goruntulu`)**
- Google'ın önerdiği gibi görselin üzerinde **metin, logo veya düğme yok**; metin ve logo,
  Google tarafından reklam öğeleri olarak ayrıca eklenir.
- Görsel kadrajı tamamen dolduruyor, kolaj yok, bulanık/ters değil, aşırı boş alan yok.
- Veriler stilize ve temsilidir: belirli bir fon, getiri veya rakam gösterilmez.

**Logolar**
- Kare logonun etrafında güvenli boşluk bırakıldı (Google logoyu daire olarak kırpabilir).
- Yatay logo 4:1, düz zemin üzerinde.

**Bannerlar**
- Açık renkli zeminde görünür 1 px kenarlık var (açık zeminli görüntülü reklamlar
  için Google kuralı).
- CTA gerçek bir sistem uyarısı ya da sahte arayüz öğesi gibi görünmüyor; "Buraya tıklayın"
  gibi ifadeler kullanılmadı.
- Tüm dosyalar 150 KB sınırının çok altında (`node render.js` her çalıştırmada denetler).

**Metinler**
- Ünlem işareti, gereksiz büyük harf, getiri vaadi ya da "en iyi / garantili" gibi
  kanıtlanamayan üstünlük ifadeleri yok.
- `node metin-kontrol.js` karakter sınırlarını denetler.

**Finansal hizmetler politikası — yayından önce kontrol edin**
FonAlfa yatırım ürünü satmayan bir bilgi/analiz sitesi olsa da Google, finansal içerikli
reklamları "Finansal hizmetler" politikası kapsamında inceleyebilir. Türkiye için
finansal hizmetler doğrulaması gerekip gerekmediğini Google Ads Politika Merkezi'nden
kontrol edin. Açılış sayfasında veri kaynağı (TEFAS) ve "yatırım tavsiyesi değildir"
notunun görünür olması onay sürecini kolaylaştırır.

## Yeniden üretme

```bash
npm install
node render.js        # tüm PNG'leri out/ altına yazar ve boyutları denetler
node metin-kontrol.js # metin öğelerini denetler
```

Chromium yolu varsayılan olarak `/opt/pw-browsers/chromium`; farklıysa
`CHROMIUM_PATH=/yol/chromium node render.js` ile verin. Metinleri (`COPY`), sahneleri
ve ölçüleri `render.js` içinden değiştirebilirsiniz.
