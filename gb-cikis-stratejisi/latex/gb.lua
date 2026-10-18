--[[
gb.lua — GB çıkış stratejisi belgeleri için pandoc (Markdown → LaTeX) filtresi.

Ne yapar:
  1. Tablolar: sütun genişliklerini içerikten hesaplar (CSS otomatik tablo düzeni gibi: en uzun sözcük
     alt sınır, en uzun hücre üst sınır), yazı boyutunu sütun sayısına göre küçültür, 10+ sütunlu ya da
     sığmayan tabloları yatay sayfaya alır, sayısal sütunları sağa yaslar, başlık satırını kalın yapar.
  2. Kanıt etiketleri: `[V]`, `[T]`, `[D?]`, `[H]` → \etiketV … \etiketH (renkli kutu).
  3. Satır içi kod: kırılabilir \kod{…} (/, _, ., - vb. sonrasında satır kırılabilir).
  4. Bağlantılar: başka bir belgeye (x.md) → \belgebag{x}{}{…}; ciltte bölüme, tek belgede x.pdf'ye gider.
     Belge içi (#…) bağlantılara ve başlık kimliklerine belge öneki eklenir (ciltte çakışma olmasın diye).
     Paket içi göreli dosya bağlantıları pdf/ klasörüne göre (../) yeniden yazılır.
  5. Şekiller: sekiller/x.png → sekiller/x.pdf (vektör), tam satır genişliği. Şeklin hemen altındaki,
     GitHub için yazılmış italik "Şekil …" satırı LaTeX'te atılır (başlık zaten şeklin altyazısı).
  6. "İLERLEME:" satırı çerçeveli kutuya, kod blokları satır kıran Verbatim ortamına alınır.

Kullanım: pandoc -f markdown-... --lua-filter gb.lua -M kimlik=<dosya kökü> ...
]]

local stringify = pandoc.utils.stringify
local KIMLIK = "belge"

-- Yardımcılar -------------------------------------------------------------------------------------

local function uzunluk(s)
  return utf8.len(s) or #s
end

-- Yazı genişliği, ortalama küçük harf genişliği biriminde: büyük harf ve rakam daha geniş, boşluk dar.
local BUYUK = "ÇĞİÖŞÜÂÎÛ"
local GENIS = { ["%"] = 1.5, ["—"] = 1.9, ["–"] = 1.1, ["−"] = 1.3, ["≈"] = 1.3, ["×"] = 1.2, ["→"] = 1.9,
                ["$"] = 1.1, ["€"] = 1.2, ["m"] = 1.6, ["w"] = 1.4, ["M"] = 1.9, ["W"] = 2.0 }
local function genislik(s)
  local g = 0
  for _, c in utf8.codes(s) do
    local ch = utf8.char(c)
    if GENIS[ch] then
      g = g + GENIS[ch]
    elseif ch == " " then
      g = g + 0.55
    elseif ch:match("^%u$") or BUYUK:find(ch, 1, true) then
      g = g + 1.45
    elseif ch:match("^%d$") then
      g = g + 1.1
    elseif ch:match("^[%.,;:'!|il]$") then
      g = g + 0.6
    else
      g = g + 1.0
    end
  end
  return g
end

local function en_uzun_sozcuk(s)
  local m = 0
  for w in s:gmatch("%S+") do
    local L = genislik(w)
    if L > m then m = L end
  end
  return m
end

local KACIS = {
  ["\\"] = "\\textbackslash{}", ["{"] = "\\{", ["}"] = "\\}", ["#"] = "\\#", ["$"] = "\\$",
  ["%"] = "\\%", ["&"] = "\\&", ["_"] = "\\_", ["^"] = "\\textasciicircum{}", ["~"] = "\\textasciitilde{}",
}
local KIRILMA = { ["/"] = true, ["_"] = true, ["."] = true, ["-"] = true, ["="] = true, [","] = true,
                  [":"] = true, ["|"] = true, ["("] = true, ["+"] = true }

-- Satır içi kodu LaTeX'e çevirir; kırılma karakterlerinden sonra \allowbreak ekler.
local function kod_tex(s)
  local out = {}
  for _, c in utf8.codes(s) do
    local ch = utf8.char(c)
    out[#out + 1] = KACIS[ch] or ch
    if KIRILMA[ch] then out[#out + 1] = "\\allowbreak{}" end
  end
  return table.concat(out)
end

-- Tablo hücresinin metni; kod ve bağlantılar kırılabildiği için en uzun sözcük hesabında kısaltılır.
local function hucre_olcu(hucre)
  local tam = stringify(hucre.contents)
  local kisa = pandoc.walk_block(pandoc.Div(hucre.contents), {
    Code = function(e) return pandoc.Str(e.text:sub(1, 10)) end,
    Link = function(e)
      if e.target:match("^%a[%w+.-]*:") and stringify(e.content):match("^%a[%w+.-]*:") then
        return pandoc.Str("bağlantı")
      end
    end,
  })
  return genislik(tam), en_uzun_sozcuk(stringify(kisa)), tam
end

local function sayisal_mi(s)
  s = s:gsub("^%s+", ""):gsub("%s+$", "")
  if s == "" or uzunluk(s) > 24 then return false end
  local rakam = select(2, s:gsub("%d", ""))
  if rakam == 0 then return false end
  local diger = s:gsub("[%d%s%.,%%%(%)%+/]", ""):gsub("−", ""):gsub("–", ""):gsub("≈", ""):gsub("±", "")
                 :gsub("%$", ""):gsub("€", ""):gsub("%-", "")
  local harf = uzunluk(diger)
  return harf <= 4 and harf <= rakam
end

-- 1. Meta: belge kimliği ------------------------------------------------------------------------

local BASLIK = nil -- verilirse ilk düzey 1 başlığın metni bununla değiştirilir (ekler için)

local function meta_oku(m)
  if m.kimlik then KIMLIK = stringify(m.kimlik) end
  if m.baslik then BASLIK = stringify(m.baslik) end
end

-- 2. Tablolar ve blok düzeyi düzenlemeler -------------------------------------------------------

-- Yazı boyutu → ortalama karakter genişliği (pt, TeX Gyre Pagella; kaba ölçü)
local KARAKTER = { small = 4.2, footnotesize = 3.75, scriptsize = 3.3 }
local PAY = 1.2 -- her sütuna eklenen güvenlik payı (birim): kalın başlık ve ölçü hatası için
local SIRA = { "small", "footnotesize", "scriptsize" }
local GENISLIK = { dikey = 470, yatay = 690 } -- metin genişliği (pt); latex/gbstil.sty ile uyumlu
local TABCOLSEP = 4

local function tablo(t)
  local ncol = #t.colspecs
  local maxL, minW, sayisal, dolu = {}, {}, {}, {}
  for j = 1, ncol do maxL[j], minW[j], sayisal[j], dolu[j] = 0, 1, 0, 0 end

  local function satir_isle(r, govde)
    local j = 1
    for _, c in ipairs(r.cells) do
      local span = c.col_span or 1
      if span == 1 and j <= ncol then
        local L, W, tam = hucre_olcu(c)
        if not govde then L, W = L * 1.08, W * 1.08 end -- başlık kalın
        L, W = L + PAY, W + PAY
        if L > maxL[j] then maxL[j] = L end
        if W > minW[j] then minW[j] = W end
        if govde and tam:match("%S") then
          dolu[j] = dolu[j] + 1
          if sayisal_mi(tam) then sayisal[j] = sayisal[j] + 1 end
        end
      end
      j = j + span
    end
  end
  for _, r in ipairs(t.head.rows) do satir_isle(r, false) end
  for _, b in ipairs(t.bodies) do
    for _, r in ipairs(b.head) do satir_isle(r, false) end
    for _, r in ipairs(b.body) do satir_isle(r, true) end
  end
  for _, r in ipairs(t.foot.rows) do satir_isle(r, true) end

  -- Boyut ve yön seçimi
  local yon = (ncol >= 10) and "yatay" or "dikey"
  local bas = (ncol <= 4) and 1 or 2 -- small ya da footnotesize ile başla
  local son = (ncol >= 8) and 3 or 2
  local function kapasite(boyut, y)
    return (GENISLIK[y] - ncol * 2 * TABCOLSEP) / KARAKTER[boyut]
  end
  local function alt_sinir(esik)
    local s, m = 0, {}
    for j = 1, ncol do
      m[j] = math.max(minW[j], math.min(maxL[j], esik))
      s = s + m[j]
    end
    return s, m
  end
  local boyut = SIRA[bas]
  local esik = (ncol >= 8) and 8 or 12
  local smin, mins = alt_sinir(esik)
  for k = bas, son do
    boyut = SIRA[k]
    if smin <= kapasite(boyut, yon) then break end
  end
  if smin > kapasite(boyut, yon) and yon == "dikey" and ncol >= 6 then
    yon, boyut = "yatay", "footnotesize"
  end

  -- Genişlikler
  local C = kapasite(boyut, yon)
  local smax = 0
  for j = 1, ncol do smax = smax + maxL[j] end
  if smax <= 0.85 * C then
    for j = 1, ncol do t.colspecs[j] = { t.colspecs[j][1], nil } end
  else
    local w = {}
    if smin >= C then
      for j = 1, ncol do w[j] = mins[j] end
    else
      local f = (C - smin) / math.max(smax - smin, 1)
      for j = 1, ncol do w[j] = mins[j] + (math.max(maxL[j], mins[j]) - mins[j]) * f end
    end
    local toplam = 0
    for j = 1, ncol do toplam = toplam + w[j] end
    for j = 1, ncol do t.colspecs[j] = { t.colspecs[j][1], w[j] / toplam } end
  end

  -- Sayısal sütunları sağa yasla (ilk sütun hariç)
  for j = 2, ncol do
    if dolu[j] >= 2 and sayisal[j] / dolu[j] >= 0.7 and t.colspecs[j][1] == "AlignDefault" then
      t.colspecs[j] = { "AlignRight", t.colspecs[j][2] }
    end
  end

  -- Başlık satırı kalın
  for _, r in ipairs(t.head.rows) do
    for _, c in ipairs(r.cells) do
      c.contents = pandoc.walk_block(pandoc.Div(c.contents), {
        Plain = function(p) return pandoc.Plain({ pandoc.Strong(p.content) }) end,
      }).content
    end
  end

  local once, sonra = {}, {}
  if yon == "yatay" then
    once[#once + 1] = pandoc.RawBlock("latex", "\\begin{landscape}")
  end
  once[#once + 1] = pandoc.RawBlock("latex", "\\begingroup\\gbtablo\\" .. boyut)
  sonra[#sonra + 1] = pandoc.RawBlock("latex", "\\endgroup")
  if yon == "yatay" then
    sonra[#sonra + 1] = pandoc.RawBlock("latex", "\\end{landscape}")
  end
  local sonuc = {}
  for _, b in ipairs(once) do sonuc[#sonuc + 1] = b end
  sonuc[#sonuc + 1] = t
  for _, b in ipairs(sonra) do sonuc[#sonuc + 1] = b end
  return sonuc
end

local function ilerleme_mi(b)
  return b.t == "Para" and stringify(b.content):match("^İLERLEME:") ~= nil
end

local function tablo_basligi_mi(b)
  return b.t == "Para" and #b.content >= 1 and b.content[1].t == "Strong"
    and stringify(b.content[1]):match("^Tablo ") ~= nil
end

local function sekil_alti_mi(b)
  return b.t == "Para" and #b.content >= 1 and b.content[1].t == "Emph"
    and stringify(b.content[1]):match("^Şekil ") ~= nil
end

local function bloklar(blocks)
  local out = pandoc.List()
  local i = 1
  while i <= #blocks do
    local b = blocks[i]
    if b.t == "Figure" and blocks[i + 1] and sekil_alti_mi(blocks[i + 1]) then
      out:insert(b)
      i = i + 1 -- GitHub için yazılmış altyazı satırını atla
    elseif tablo_basligi_mi(b) and blocks[i + 1] and blocks[i + 1].t == "Table" then
      out:insert(pandoc.RawBlock("latex", "\\Needspace{7\\baselineskip}")) -- başlık tablosuz sayfa sonunda kalmasın (\\needspace longtable ile çakışır)
      out:insert(b)
      out:insert(pandoc.RawBlock("latex", "\\nopagebreak[4]"))
    elseif ilerleme_mi(b) then
      out:insert(pandoc.RawBlock("latex", "\\begin{gbilerleme}"))
      out:insert(b)
      out:insert(pandoc.RawBlock("latex", "\\end{gbilerleme}"))
    else
      out:insert(b)
    end
    i = i + 1
  end
  return out
end

local function kod_blogu(cb)
  return pandoc.RawBlock("latex", "\\begin{gbkod}\n" .. cb.text .. "\n\\end{gbkod}")
end

local ilk_baslik = true
local function baslik(h)
  if h.level == 1 and ilk_baslik then
    h.identifier = KIMLIK
    ilk_baslik = false
    if BASLIK then h.content = pandoc.Inlines(BASLIK) end
  elseif h.identifier ~= "" then
    h.identifier = KIMLIK .. "-" .. h.identifier
  end
  return h
end

-- 3. Satır içi öğeler -----------------------------------------------------------------------------

local ETIKET = { ["[V]"] = "V", ["[T]"] = "T", ["[D?]"] = "D", ["[H]"] = "H" }

local function kod(el)
  local e = ETIKET[el.text]
  if e then
    return pandoc.RawInline("latex", "\\etiket" .. e .. "{}")
  end
  return pandoc.RawInline("latex", "\\kod{" .. kod_tex(el.text) .. "}")
end

local function baglanti(el)
  local t = el.target
  if t:match("^%a[%w+.-]*:") then
    return el -- http(s), mailto vb.
  end
  if t:sub(1, 1) == "#" then
    el.target = "#" .. KIMLIK .. "-" .. t:sub(2)
    return el
  end
  local dosya, parca = t:match("^([^#]*)#?(.*)$")
  local ad = dosya:match("([^/]+)%.md$")
  if ad then
    local icerik = pandoc.List({ pandoc.RawInline("latex", "\\belgebag{" .. ad .. "}{" .. parca .. "}{") })
    icerik:extend(el.content)
    icerik:insert(pandoc.RawInline("latex", "}"))
    return icerik
  end
  el.target = "../" .. dosya
  return el
end

local function resim(el)
  local src = el.src
  if src:match("%.png$") then
    local pdf = src:gsub("%.png$", ".pdf")
    local f = io.open(pdf, "r")
    if f then
      f:close()
      el.src = pdf
    end
  end
  el.attributes.width = "100%"
  return el
end

-- Tablo hücrelerindeki HTML satır sonu ve madde listeleri (GitHub'da da aynı görünür)
local function ham_html(el)
  if el.format ~= "html" then return nil end
  local t = el.text:lower():gsub("%s", "")
  if t == "<br>" or t == "<br/>" then
    return pandoc.RawInline("latex", "\\newline{}")
  elseif t == "<li>" then
    return pandoc.RawInline("latex", "\\gbli{}")
  elseif t == "<ul>" or t == "</ul>" or t == "</li>" then
    return {}
  end
  return nil
end

-- Yatay tablolarda başlık paragrafı landscape ortamının içine alınır; yoksa başlık bir önceki sayfada kalır.
local function yatay_baslik(blocks)
  local out = pandoc.List()
  local i = 1
  while i <= #blocks do
    local b, n1, n2, n3 = blocks[i], blocks[i + 1], blocks[i + 2], blocks[i + 3]
    if b.t == "RawBlock" and b.text:match("Needspace") and n1 and tablo_basligi_mi(n1) and n2 and n2.t == "RawBlock"
        and n2.text:match("nopagebreak") and n3 and n3.t == "RawBlock" and n3.text == "\\begin{landscape}" then
      out:insert(n3)
      out:insert(n1)
      out:insert(n2)
      i = i + 4
    else
      out:insert(b)
      i = i + 1
    end
  end
  return out
end

return {
  { Meta = meta_oku },
  { Blocks = bloklar },
  { Table = tablo, CodeBlock = kod_blogu, Header = baslik },
  { Code = kod, Link = baglanti, Image = resim, RawInline = ham_html },
  { Blocks = yatay_baslik },
}
