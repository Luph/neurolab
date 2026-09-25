// metinler.json'daki metin öğelerini Google Ads karakter sınırlarına göre denetler.
const t = require('./metinler.json');
let bad = 0;
const chk = (k, a, max) => a.forEach((s) => {
  const n = [...s].length;
  // Google, başlıklarda ünlem işaretine izin vermez.
  const ok = n <= max && !s.includes('!');
  if (!ok) bad++;
  console.log(`${ok ? 'OK  ' : 'HATA'} ${k.padEnd(12)} ${String(n).padStart(2)}/${max}  ${s}`);
});
chk('işletme adı', [t.isletme_adi], 25);
chk('kısa başlık', t.kisa_basliklar, 30);
chk('uzun başlık', t.uzun_basliklar, 90);
chk('açıklama', t.aciklamalar.slice(0, 1), 60); // ilk açıklama "kısa açıklama" (≤60)
chk('açıklama', t.aciklamalar.slice(1), 90);
process.exit(bad ? 1 : 0);
