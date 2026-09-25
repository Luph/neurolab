// FonAlfa Google Ads görsel üreticisi.
// Sitenin (fonalfa.com) tasarım dilini — krem kâğıt zemin, çift çizgili başlık,
// yeşil/kırmızı net akış çubukları, fon büyüklüğü haritası, KPI kartları — stilize
// ederek Google Ads ölçülerinde PNG üretir.
//
//   npm install && node render.js
//
// Çıktı: out/duyarli-goruntulu (Responsive Display / Performance Max, yazısız),
//        out/logolar, out/banner (yüklenen görüntülü reklam, ≤150 KB).

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright-core');

const ROOT = __dirname;
const OUT = path.join(ROOT, 'out');
const SRC = path.join(ROOT, 'src');

// Site tokenları (:root, açık tema)
const C = {
  bg: '#F4F1EA', surface: '#FAF8F2', surface2: '#ECE7DC', card: '#EDE9E0',
  border: '#D6CFC0', rule: '#B8AF9C', text: '#17150F', muted: '#6B655A',
  accent: '#7A1F1A', accent2: '#1F3A5F', pos: '#1A6B36', neg: '#B42318', c4: '#B8741A',
};

// Deterministik rastgele: her çalıştırmada aynı görseller.
function rng(seed) {
  let s = seed >>> 0;
  return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296);
}

function mix(a, b, t) {
  const p = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16));
  const [x, y] = [p(a), p(b)];
  return '#' + x.map((v, i) => Math.round(v + (y[i] - v) * t).toString(16).padStart(2, '0')).join('');
}

const fontCss = `
@font-face{font-family:'Fraunces';font-style:normal;font-weight:400 700;src:url(src/fonts/fraunces-normal-400_700-latin.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212}
@font-face{font-family:'Fraunces';font-style:normal;font-weight:400 700;src:url(src/fonts/fraunces-normal-400_700-latin-ext.woff2) format('woff2');unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F}
@font-face{font-family:'Fraunces';font-style:italic;font-weight:400 700;src:url(src/fonts/fraunces-italic-400_700-latin.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212}
@font-face{font-family:'Fraunces';font-style:italic;font-weight:400 700;src:url(src/fonts/fraunces-italic-400_700-latin-ext.woff2) format('woff2');unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F}
@font-face{font-family:'IBM Plex Sans';font-weight:400 600;src:url(src/fonts/plexsans-normal-400-latin.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+2000-206F,U+2191,U+2193,U+2212}
@font-face{font-family:'IBM Plex Sans';font-weight:400 600;src:url(src/fonts/plexsans-normal-400-latin-ext.woff2) format('woff2');unicode-range:U+0100-02BA,U+1E00-1E9F}
@font-face{font-family:'IBM Plex Mono';font-weight:400;src:url(src/fonts/plexmono-normal-400-latin.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+2000-206F,U+2212}
@font-face{font-family:'IBM Plex Mono';font-weight:400;src:url(src/fonts/plexmono-normal-400-latin-ext.woff2) format('woff2');unicode-range:U+0100-02BA}
@font-face{font-family:'IBM Plex Mono';font-weight:500;src:url(src/fonts/plexmono-normal-500-latin.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+2000-206F,U+2212}
@font-face{font-family:'IBM Plex Mono';font-weight:500;src:url(src/fonts/plexmono-normal-500-latin-ext.woff2) format('woff2');unicode-range:U+0100-02BA}
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:${C.bg};color:${C.text};font-family:'IBM Plex Sans',sans-serif;-webkit-font-smoothing:antialiased}
`;

// ---------------------------------------------------------------------------
// Sahneler (yazısız SVG). Her biri (W, H) alır, tam kadrajı doldurur.
// ---------------------------------------------------------------------------

// Sitedeki başlık altı çift çizgi.
function doubleRule(x, y, w, s) {
  return `<rect x="${x}" y="${y}" width="${w}" height="${Math.max(2, 3 * s)}" fill="${C.text}"/>
  <rect x="${x}" y="${y + 9 * s}" width="${w}" height="${Math.max(1, 1.4 * s)}" fill="${C.text}"/>`;
}

function paper(W, H, inner) {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
  <rect width="${W}" height="${H}" fill="${C.bg}"/>${inner}</svg>`;
}

// 1) "Net akış · kırılım": ortadan ayrışan yatay çubuklar.
function sceneFlows(W, H) {
  const s = Math.min(W, H) / 628;
  const m = Math.round(Math.min(W, H) * 0.085);
  const r = rng(7);
  const top = m + 22 * s;
  const n = H / W > 1.1 ? 14 : H / W > 0.9 ? 11 : 8;
  const rowH = (H - top - m) / n;
  const cx = W * 0.5;
  const half = W / 2 - m;
  const vals = Array.from({ length: n }, (_, i) => {
    const t = i / (n - 1);
    const d = 1 - 2 * t;
    // Sıfıra yakın çubuk bırakma: boş alan Google'da "aşırı boşluk" sayılabilir.
    return Math.sign(d || 1) * (0.3 + 0.7 * Math.pow(Math.abs(d), 0.8) + r() * 0.08);
  }).sort((a, b) => b - a);
  const maxAbs = Math.max(...vals.map(Math.abs));
  let bars = '';
  vals.forEach((v, i) => {
    const y = top + i * rowH;
    const w = (Math.abs(v) / maxAbs) * half * 0.94;
    const bh = rowH * 0.56;
    const col = v >= 0 ? C.pos : C.neg;
    bars += `<rect x="${m}" y="${y + rowH - 0.5}" width="${W - 2 * m}" height="1" fill="${C.border}"/>`;
    bars += `<rect x="${v >= 0 ? cx : cx - w}" y="${y + (rowH - bh) / 2}" width="${w}" height="${bh}" rx="${2 * s}" fill="${col}" opacity="${0.55 + 0.45 * Math.abs(v) / maxAbs}"/>`;
  });
  return paper(W, H, `${doubleRule(m, m, W - 2 * m, s)}
    <rect x="${cx - s}" y="${top - 6 * s}" width="${Math.max(2, 2 * s)}" height="${H - top - m + 12 * s}" fill="${C.text}"/>${bars}`);
}

// 2) "Fon büyüklüğü haritası": alan = varlık, renk = akış oranı.
function squarify(items, x, y, w, h) {
  const out = [];
  const total = items.reduce((a, b) => a + b.v, 0);
  const scale = (w * h) / total;
  let rest = items.map((d) => ({ ...d, a: d.v * scale }));
  const worst = (row, len) => {
    const sum = row.reduce((a, b) => a + b.a, 0);
    const mx = Math.max(...row.map((d) => d.a)), mn = Math.min(...row.map((d) => d.a));
    return Math.max((len * len * mx) / (sum * sum), (sum * sum) / (len * len * mn));
  };
  while (rest.length) {
    const len = Math.min(w, h);
    let row = [rest[0]];
    let i = 1;
    while (i < rest.length && worst([...row, rest[i]], len) <= worst(row, len)) row.push(rest[i++]);
    rest = rest.slice(i);
    const sum = row.reduce((a, b) => a + b.a, 0);
    const thick = sum / len;
    let off = 0;
    for (const d of row) {
      const l = d.a / thick;
      if (w >= h) out.push({ ...d, x, y: y + off, w: thick, h: l });
      else out.push({ ...d, x: x + off, y, w: l, h: thick });
      off += l;
    }
    if (w >= h) { x += thick; w -= thick; } else { y += thick; h -= thick; }
  }
  return out;
}

function sceneTreemap(W, H) {
  const s = Math.min(W, H) / 628;
  const m = Math.round(Math.min(W, H) * 0.085);
  const r = rng(11);
  const items = Array.from({ length: 22 }, (_, i) => ({
    v: Math.pow(0.84, i) * (0.8 + r() * 0.4),
    f: (r() - 0.42) * 2,
  })).sort((a, b) => b.v - a.v);
  const top = m + 22 * s;
  const gap = Math.max(3, 5 * s);
  const cells = squarify(items, m, top, W - 2 * m, H - top - m);
  const rects = cells.map((c) => {
    const t = Math.min(1, Math.abs(c.f));
    const fill = mix(C.card, c.f >= 0 ? C.pos : C.neg, 0.25 + 0.75 * t);
    return `<rect x="${c.x + gap / 2}" y="${c.y + gap / 2}" width="${Math.max(0, c.w - gap)}" height="${Math.max(0, c.h - gap)}" rx="${3 * s}" fill="${fill}"/>`;
  }).join('');
  return paper(W, H, `${doubleRule(m, m, W - 2 * m, s)}${rects}`);
}

// 3) "Zaman serisi": günlük net akış sütunları + kümülatif çizgi.
function sceneSeries(W, H) {
  const s = Math.min(W, H) / 628;
  const m = Math.round(Math.min(W, H) * 0.085);
  const r = rng(23);
  const n = W > H ? 42 : 28;
  const top = m + 22 * s;
  const plotH = H - top - m;
  const vals = [];
  for (let i = 0; i < n; i++) vals.push(Math.sin(i / 5) * 0.45 + (i / n) * 0.55 + (r() - 0.5) * 0.9);
  const maxAbs = Math.max(...vals.map(Math.abs));
  const zero = top + plotH * (W > H ? 0.66 : 0.72);
  const upH = zero - top - 10 * s, dnH = top + plotH - zero - 10 * s;
  const step = (W - 2 * m) / n;
  let grid = '';
  for (let k = 1; k <= 4; k++) {
    const gy = top + (plotH * k) / 5;
    grid += `<rect x="${m}" y="${gy}" width="${W - 2 * m}" height="1" fill="${C.border}"/>`;
  }
  let cols = '';
  let cum = 0;
  const cumPts = [];
  vals.forEach((v, i) => {
    const x = m + i * step + step * 0.16;
    const bw = step * 0.68;
    const h = (Math.abs(v) / maxAbs) * (v >= 0 ? upH : dnH);
    cols += `<rect x="${x}" y="${v >= 0 ? zero - h : zero}" width="${bw}" height="${h}" fill="${v >= 0 ? C.pos : C.neg}"/>`;
    cum += v;
    cumPts.push([x + bw / 2, cum]);
  });
  const cMin = Math.min(...cumPts.map((p) => p[1])), cMax = Math.max(...cumPts.map((p) => p[1]));
  const line = cumPts.map(([x, c], i) => `${i ? 'L' : 'M'}${x.toFixed(1)},${(top + 14 * s + (1 - (c - cMin) / (cMax - cMin)) * (upH * 0.9)).toFixed(1)}`).join('');
  const last = cumPts[cumPts.length - 1];
  const ly = top + 14 * s + (1 - (last[1] - cMin) / (cMax - cMin)) * (upH * 0.9);
  return paper(W, H, `${doubleRule(m, m, W - 2 * m, s)}${grid}${cols}
    <rect x="${m}" y="${zero}" width="${W - 2 * m}" height="${Math.max(1.5, 2 * s)}" fill="${C.text}"/>
    <path d="${line}" fill="none" stroke="${C.accent2}" stroke-width="${Math.max(2.5, 4 * s)}" stroke-linejoin="round" stroke-linecap="round"/>
    <circle cx="${last[0]}" cy="${ly}" r="${8 * s}" fill="${C.accent2}"/><circle cx="${last[0]}" cy="${ly}" r="${3.5 * s}" fill="${C.bg}"/>`);
}

// 4) "Özet kartları": KPI döşemeleri, rakam yerine yön okları ve sparkline.
function sceneCards(W, H) {
  const s = Math.min(W, H) / 628;
  const m = Math.round(Math.min(W, H) * 0.085);
  const top = m + 22 * s;
  const cols = W / H > 1.4 ? 3 : 2;
  const rows = W / H > 1.4 ? 1 : H / W > 1.1 ? 3 : 2;
  const g = 18 * s;
  const cw = (W - 2 * m - g * (cols - 1)) / cols;
  const ch = (H - top - m - g * (rows - 1)) / rows;
  const specs = [
    { up: true, seed: 3, color: C.pos }, { up: false, seed: 5, color: C.neg },
    { up: true, seed: 9, color: C.accent2 }, { up: true, seed: 13, color: C.c4 },
    { up: false, seed: 17, color: C.neg }, { up: true, seed: 19, color: C.pos },
  ];
  let out = '';
  let k = 0;
  for (let rr = 0; rr < rows; rr++) for (let cc = 0; cc < cols; cc++) {
    const sp = specs[k++ % specs.length];
    const x = m + cc * (cw + g), y = top + rr * (ch + g);
    const p = 24 * s;
    const r = rng(sp.seed);
    // Kart: site kartları gibi ince kenarlık + üst vurgu çizgisi
    out += `<rect x="${x}" y="${y}" width="${cw}" height="${ch}" rx="${3 * s}" fill="${C.surface}" stroke="${C.border}" stroke-width="${Math.max(1, 1.5 * s)}"/>`;
    out += `<rect x="${x}" y="${y}" width="${cw}" height="${4 * s}" fill="${sp.color}"/>`;
    // Yön üçgeni (▲/▼)
    const tri = 34 * s, tx = x + p, ty = y + p + 14 * s;
    out += sp.up
      ? `<path d="M${tx},${ty + tri} L${tx + tri / 2},${ty} L${tx + tri},${ty + tri}Z" fill="${sp.color === C.neg ? C.pos : sp.color}"/>`
      : `<path d="M${tx},${ty} L${tx + tri / 2},${ty + tri} L${tx + tri},${ty}Z" fill="${C.neg}"/>`;
    // Sparkline + alan
    const n = 24, sx = x + p, sw = cw - 2 * p;
    const sTop = ty + tri + 26 * s, sBot = y + ch - p;
    const pts = [];
    let v = 0.5;
    for (let i = 0; i < n; i++) { v += (r() - 0.5) * 0.22 + (sp.up ? 0.02 : -0.02); v = Math.max(0.05, Math.min(0.95, v)); pts.push(v); }
    const P = pts.map((q, i) => [sx + (i / (n - 1)) * sw, sBot - q * (sBot - sTop)]);
    const d = P.map(([a, b], i) => `${i ? 'L' : 'M'}${a.toFixed(1)},${b.toFixed(1)}`).join('');
    const lc = sp.up ? (sp.color === C.neg ? C.pos : sp.color) : C.neg;
    out += `<path d="${d}L${sx + sw},${sBot}L${sx},${sBot}Z" fill="${lc}" opacity="0.12"/>`;
    out += `<path d="${d}" fill="none" stroke="${lc}" stroke-width="${Math.max(2, 3 * s)}" stroke-linejoin="round"/>`;
  }
  return paper(W, H, `${doubleRule(m, m, W - 2 * m, s)}${out}`);
}

const SCENES = { 'net-akis': sceneFlows, 'harita': sceneTreemap, 'zaman-serisi': sceneSeries, 'ozet-kartlari': sceneCards };

// Responsive Display / Performance Max ölçüleri (Google önerilen boyutlar)
const RDA = [
  { tag: 'yatay-1200x628', W: 1200, H: 628 },   // 1.91:1 (zorunlu)
  { tag: 'kare-1200x1200', W: 1200, H: 1200 },  // 1:1 (zorunlu)
  { tag: 'dikey-960x1200', W: 960, H: 1200 },   // 4:5 (isteğe bağlı)
];

// ---------------------------------------------------------------------------
// Logolar
// ---------------------------------------------------------------------------
const logoSvg = fs.readFileSync(path.join(SRC, 'logo.svg'), 'utf8');
const favSvg = fs.readFileSync(path.join(SRC, 'favicon.svg'), 'utf8');
const dataUri = (svg) => 'data:image/svg+xml;base64,' + Buffer.from(svg).toString('base64');

function logoSquare() {
  // Favicon'daki α işareti; Google kare logo 1:1, logonun etrafında boşluk olmalı.
  return `<html><head><style>${fontCss}</style></head><body style="width:1200px;height:1200px;padding:180px;background:${C.accent}">
    <img src="${dataUri(favSvg)}" style="width:840px;height:840px;display:block"></body></html>`;
}
function logoSquareWordmark(dark) {
  // "Fonα" kelime işaretinin kare sürümü. 900 px genişlik, Google'ın daire kırpmasında
  // da tamamen görünür kalır (köşegen yarısı < 600 px).
  const svg = fs.readFileSync(path.join(SRC, dark ? 'logo-dark.svg' : 'logo.svg'), 'utf8');
  return `<html><head><style>${fontCss}</style></head><body style="width:1200px;height:1200px;display:flex;align-items:center;justify-content:center;background:${dark ? C.text : C.bg}">
    <img src="${dataUri(svg)}" style="width:900px;display:block"></body></html>`;
}
function logoWide() {
  // 4:1 yatay logo, kelime işareti ortada, krem zemin.
  return `<html><head><style>${fontCss}</style></head><body style="width:1200px;height:300px;display:flex;align-items:center;justify-content:center;background:${C.bg}">
    <img src="${dataUri(logoSvg)}" style="height:188px;display:block"></body></html>`;
}

// ---------------------------------------------------------------------------
// Yüklenen görüntülü reklam bannerları (metinli, CTA'lı, kenarlıklı)
// ---------------------------------------------------------------------------
const COPY = {
  h: 'Hangi fonlara para giriyor?',
  sub: 'TEFAS fon akışları · her iş günü',
  cta: 'Akışları incele',
};

function miniBars(w, h, n, seed) {
  const r = rng(seed);
  const vals = Array.from({ length: n }, (_, i) => (1 - 2 * (i / (n - 1))) + (r() - 0.5) * 0.25).sort((a, b) => b - a);
  const mx = Math.max(...vals.map(Math.abs));
  const rh = h / n, cx = w / 2;
  const bars = vals.map((v, i) => {
    const bw = (Math.abs(v) / mx) * (w / 2) * 0.95;
    return `<rect x="${v >= 0 ? cx : cx - bw}" y="${i * rh + rh * 0.2}" width="${bw}" height="${rh * 0.6}" rx="1" fill="${v >= 0 ? C.pos : C.neg}"/>`;
  }).join('');
  return `<svg width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" style="display:block"><rect x="${cx - 0.75}" y="0" width="1.5" height="${h}" fill="${C.text}"/>${bars}</svg>`;
}

function miniCols(w, h, n, seed) {
  const r = rng(seed);
  const vals = Array.from({ length: n }, (_, i) => Math.sin(i / 3) * 0.4 + i / n * 0.6 + (r() - 0.5) * 0.9);
  const mx = Math.max(...vals.map(Math.abs));
  const zero = h * 0.62, st = w / n;
  const cols = vals.map((v, i) => {
    const bh = (Math.abs(v) / mx) * (v >= 0 ? zero - 2 : h - zero - 2);
    return `<rect x="${i * st + st * 0.15}" y="${v >= 0 ? zero - bh : zero}" width="${st * 0.7}" height="${bh}" fill="${v >= 0 ? C.pos : C.neg}"/>`;
  }).join('');
  return `<svg width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" style="display:block">${cols}<rect x="0" y="${zero}" width="${w}" height="1.5" fill="${C.text}"/></svg>`;
}

function bannerHtml(W, H) {
  const base = `${fontCss}
    body{width:${W}px;height:${H}px;overflow:hidden}
    .ad{position:relative;width:${W}px;height:${H}px;background:${C.bg};border:1px solid ${C.rule};overflow:hidden}
    .logo{display:block}
    .rule{border-top:2px solid ${C.text};border-bottom:1px solid ${C.text};height:5px}
    .h{font-family:'Fraunces',serif;font-weight:600;letter-spacing:-0.01em;line-height:1.08;color:${C.text}}
    .sub{color:${C.muted};line-height:1.25}
    .cta{display:inline-flex;align-items:center;gap:.35em;background:${C.accent};color:${C.bg};font-weight:600;border-radius:3px;white-space:nowrap;line-height:1}
    .url{font-family:'IBM Plex Mono',monospace;color:${C.muted}}`;
  const logo = (h) => `<img class="logo" src="${dataUri(logoSvg)}" style="height:${h}px">`;
  const ratio = W / H;
  let body;
  if (ratio >= 4) {
    // Yatay şeritler: 728x90, 970x90, 468x60, 320x50
    const small = H <= 60;
    const lh = small ? Math.round(H * 0.46) : Math.round(H * 0.4);
    const showSub = W >= 700;
    const showChart = W >= 700;
    const hs = small ? (W < 400 ? 13 : 16) : 24;
    body = `<div style="display:flex;align-items:center;height:100%;padding:0 ${small ? 10 : 18}px;gap:${small ? 10 : 18}px">
      ${logo(lh)}
      <div style="width:1px;align-self:stretch;margin:${small ? 8 : 14}px 0;background:${C.rule}"></div>
      <div style="flex:1;min-width:0">
        <div class="h" style="font-size:${hs}px;white-space:nowrap">${COPY.h}</div>
        ${showSub ? `<div class="sub" style="font-size:13px;margin-top:4px">${COPY.sub}</div>` : ''}
      </div>
      ${showChart ? `<div>${miniBars(small ? 70 : 110, H - (small ? 18 : 30), small ? 5 : 7, 5)}</div>` : ''}
      ${W >= 460 ? `<span class="cta" style="font-size:${small ? 12 : 14}px;padding:${small ? '8px 10px' : '11px 14px'}">${COPY.cta} →</span>` : `<span class="cta" style="font-size:12px;padding:7px 8px">→</span>`}
    </div>`;
  } else if (ratio >= 2.5) {
    // 970x250, 320x100
    const big = W >= 900;
    body = `<div style="display:flex;height:100%;padding:${big ? 26 : 10}px ${big ? 30 : 12}px;gap:${big ? 30 : 10}px;align-items:stretch">
      <div style="flex:1;display:flex;flex-direction:column;justify-content:space-between;min-width:0">
        <div>${logo(big ? 34 : 18)}<div class="rule" style="margin-top:${big ? 10 : 5}px"></div></div>
        <div class="h" style="font-size:${big ? 40 : 16}px">${COPY.h}</div>
        ${big ? `<div style="display:flex;align-items:center;gap:16px"><span class="cta" style="font-size:16px;padding:12px 16px">${COPY.cta} →</span><span class="sub" style="font-size:14px">${COPY.sub}</span></div>` : ''}
      </div>
      <div style="display:flex;align-items:center">${big ? miniCols(320, 190, 22, 3) : miniBars(78, 76, 6, 5)}</div>
    </div>`;
  } else if (ratio <= 0.4) {
    // Gökdelen: 160x600, 300x600 (0.5 aşağıda)
    body = skyscraper(W, H, logo);
  } else if (ratio <= 0.6) {
    body = skyscraper(W, H, logo);
  } else {
    // Kare/dikdörtgen: 300x250, 336x280, 250x250, 200x200
    const tiny = W <= 210;
    const hs = tiny ? 18 : W >= 330 ? 25 : 22;
    const pad = tiny ? 12 : 16;
    body = `<div style="display:flex;flex-direction:column;height:100%;padding:${pad}px">
      ${logo(tiny ? 20 : 24)}<div class="rule" style="margin-top:6px"></div>
      <div class="h" style="font-size:${hs}px;margin-top:${tiny ? 8 : 12}px">${COPY.h}</div>
      <div style="flex:1;display:flex;align-items:center;justify-content:center;padding:${tiny ? 6 : 10}px 0">${miniBars(W - 2 * pad, tiny ? 40 : Math.round(H * 0.26), tiny ? 5 : 7, 9)}</div>
      <div style="display:flex;align-items:center;justify-content:space-between;gap:8px">
        <span class="cta" style="font-size:${tiny ? 12 : 14}px;padding:${tiny ? '8px 10px' : '10px 13px'}">${COPY.cta} →</span>
        ${tiny ? '' : `<span class="url" style="font-size:11px">fonalfa.com</span>`}
      </div>
    </div>`;
  }
  return `<html><head><style>${base}</style></head><body><div class="ad">${body}</div></body></html>`;
}

function skyscraper(W, H, logo) {
  const narrow = W < 200;
  const pad = narrow ? 12 : 20;
  const inner = W - 2 * pad;
  return `<div style="display:flex;flex-direction:column;height:100%;padding:${pad}px">
    ${logo(narrow ? 26 : 34)}<div class="rule" style="margin-top:8px"></div>
    <div class="h" style="font-size:${narrow ? 24 : 34}px;margin-top:16px">${COPY.h}</div>
    <div class="sub" style="font-size:${narrow ? 13 : 15}px;margin-top:10px">${COPY.sub}</div>
    <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:18px;padding:16px 0">
      ${miniBars(inner, narrow ? 130 : 150, 8, 21)}
      ${miniCols(inner, narrow ? 70 : 90, narrow ? 14 : 20, 3)}
    </div>
    <span class="cta" style="font-size:${narrow ? 13 : 16}px;padding:12px ${narrow ? 10 : 16}px;justify-content:center">${COPY.cta} →</span>
    <div class="url" style="font-size:11px;margin-top:10px;text-align:center">fonalfa.com</div>
  </div>`;
}

// Google Ads "yüklenen görüntülü reklam" ölçüleri
const BANNERS = [
  [300, 250], [336, 280], [250, 250], [200, 200],
  [728, 90], [970, 90], [468, 60], [320, 50],
  [970, 250], [320, 100],
  [300, 600], [160, 600],
];

// ---------------------------------------------------------------------------
async function shoot(browser, html, W, H, file) {
  const tmp = path.join(ROOT, `.tmp-${W}x${H}.html`);
  fs.writeFileSync(tmp, html);
  const page = await browser.newPage({ viewport: { width: W, height: H } });
  await page.goto('file://' + tmp);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(150);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  await page.screenshot({ path: file, clip: { x: 0, y: 0, width: W, height: H } });
  await page.close();
  fs.unlinkSync(tmp);
  return fs.statSync(file).size;
}

(async () => {
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium' });
  const report = [];
  const wrap = (svg) => `<html><head><style>${fontCss}</style></head><body>${svg}</body></html>`;

  for (const [name, fn] of Object.entries(SCENES)) {
    for (const { tag, W, H } of RDA) {
      const f = path.join(OUT, 'duyarli-goruntulu', `${name}_${tag}.png`);
      report.push([path.relative(ROOT, f), W, H, await shoot(browser, wrap(fn(W, H)), W, H, f)]);
    }
  }
  const lk = path.join(OUT, 'logolar', 'logo-kare_1200x1200.png');
  report.push([path.relative(ROOT, lk), 1200, 1200, await shoot(browser, logoSquare(), 1200, 1200, lk)]);
  const lkw = path.join(OUT, 'logolar', 'logo-kare-yazili_1200x1200.png');
  report.push([path.relative(ROOT, lkw), 1200, 1200, await shoot(browser, logoSquareWordmark(false), 1200, 1200, lkw)]);
  const lkd = path.join(OUT, 'logolar', 'logo-kare-yazili-koyu_1200x1200.png');
  report.push([path.relative(ROOT, lkd), 1200, 1200, await shoot(browser, logoSquareWordmark(true), 1200, 1200, lkd)]);
  const lw = path.join(OUT, 'logolar', 'logo-yatay_1200x300.png');
  report.push([path.relative(ROOT, lw), 1200, 300, await shoot(browser, logoWide(), 1200, 300, lw)]);

  for (const [W, H] of BANNERS) {
    const f = path.join(OUT, 'banner', `banner_${W}x${H}.png`);
    report.push([path.relative(ROOT, f), W, H, await shoot(browser, bannerHtml(W, H), W, H, f)]);
  }
  await browser.close();

  let bad = 0;
  for (const [f, W, H, size] of report) {
    const limit = f.includes('/banner/') ? 150 * 1024 : 5 * 1024 * 1024;
    const ok = size <= limit;
    if (!ok) bad++;
    console.log(`${ok ? 'OK ' : 'BÜYÜK'} ${f}  ${W}x${H}  ${(size / 1024).toFixed(1)} KB`);
  }
  if (bad) { console.error(`${bad} dosya boyut sınırını aşıyor`); process.exit(1); }
})();
