#!/usr/bin/env bash
# derle.sh — Markdown belgelerinden LaTeX gövdelerini (latex/govde/) ve PDF'leri (pdf/) üretir.
#
# Gerekenler: pandoc ≥ 3.1, LuaLaTeX ve latexmk (TeX Live 2023), TeX Gyre ve DejaVu yazı tipleri.
#   Ubuntu: apt-get install pandoc texlive-luatex texlive-latex-extra texlive-fonts-extra \
#           texlive-lang-european latexmk fonts-dejavu
# Kullanım (paket kökünden ya da herhangi bir yerden):
#   latex/derle.sh              şekiller + gövdeler + bütün PDF'ler
#   latex/derle.sh --tex        yalnızca şekiller ve LaTeX gövdeleri (PDF yok)
#   latex/derle.sh --cilt       yalnızca birleşik cilt
set -euo pipefail
export LC_ALL=C.UTF-8   # pandoc komut satırındaki Türkçe başlıkları (-M baslik=…) UTF-8 okusun
PAKET="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PAKET"
KIP="${1:-hepsi}"

# Markdown okuyucusu: GitHub'daki görünümle birebir uyum için gfm (CommonMark); akıllı tırnak ve tek
# başına duran resimden şekil açık; TeX matematiği ($ tutarlar için), YAML ve emoji kısa kodları kapalı.
OKU="gfm+smart+implicit_figures-tex_math_dollars-yaml_metadata_block-emoji"

# kök | kapak alt başlığı | kapak açıklaması | (isteğe bağlı) bölüm başlığı
BELGELER=(
  "DURUM_OZETI|Durum özeti|Faz 3 parça 1 sonu itibarıyla bulgular, öneri ve açık konular.|"
  "00_plan|Faz 0 — Plan|Çalışma planı, varsayım kaydı, veri envanteri ve NACE kapsamı.|"
  "01_teshis|Faz 1 — Teşhis|Gümrük Birliği'nin 30 yıllık bilançosu, asimetriler ve makro tablo.|"
  "02a_politika_uzayi|Faz 2A — Politika uzayı|Tek taraflı araçlar, iç vergiler ve dış rejim seçenekleri.|"
  "02b_secenekler_hukuk|Faz 2B — Seçenekler ve hukuk|Seçenekler matrisi, bitiş durumu, çekim modeli ve hukuki yol haritası.|"
  "02c_hazirlik|Faz 2C — Karar öncesi hazırlık|Sessiz, pişmanlıksız hamleler: hukuk, STA, menşe, kalite, SKDM, makro-finans, diplomasi.|"
  "nace_kartlar_10-12|Faz 3 — NACE kartları: 10–12|Gıda, içecek ve tütün: genel görünüm, ana matris satırları, 33 sınıf kartı ve kümülatif defter.|"
  "defter|Ek A — Kümülatif defter|Fazlar boyunca taşınan referans değerler ve bütçeler.|Ek A — Kümülatif defter"
  "README|Ek B — Çalışma paketi|Paketin yapısı, kod, veri ve yeniden üretim adımları.|Ek B — Çalışma paketi: kod, veri ve yeniden üretim"
)

echo "1/3 Şekiller (kod/sekiller.py)"
python3 kod/sekiller.py >/dev/null

echo "2/3 LaTeX gövdeleri (pandoc + latex/gb.lua)"
mkdir -p latex/govde latex/_derle pdf
for satir in "${BELGELER[@]}"; do
  IFS='|' read -r kok altbaslik aciklama bolum <<<"$satir"
  ek=()
  [[ -n "$bolum" ]] && ek=(-M "baslik=$bolum")
  pandoc -f "$OKU" "$kok.md" -t latex --top-level-division=chapter --wrap=none \
    --lua-filter latex/gb.lua -M "kimlik=$kok" "${ek[@]}" -o "latex/govde/$kok.tex"
  cat > "latex/tek_$kok.tex" <<TEX
% Otomatik üretildi (latex/derle.sh); elle düzenlemeyin.
\\documentclass[fontsize=10pt, paper=a4, oneside, open=any]{scrreprt}
\\usepackage{gbstil}
\\gbciltfalse
\\setcounter{tocdepth}{2}
\\hypersetup{pdftitle={Gümrük Birliği'nden kontrollü çıkış — $altbaslik}, pdfsubject={$aciklama}}
\\begin{document}
\\gbkapak{$altbaslik}{$aciklama}
\\tableofcontents
\\input{govde/$kok}
\\end{document}
TEX
done
[[ "$KIP" == "--tex" ]] && exit 0

echo "3/3 PDF (LuaLaTeX, latexmk)"
cd latex
derle() {
  latexmk -lualatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=_derle "$1.tex" \
    >"_derle/$1.konsol" 2>&1 || { echo "HATA: $1 (latex/_derle/$1.log)"; tail -30 "_derle/$1.konsol"; exit 1; }
}
derle cilt
cp _derle/cilt.pdf ../pdf/GB_Cikis_Stratejisi_Faz0-3.pdf
if [[ "$KIP" != "--cilt" ]]; then
  for satir in "${BELGELER[@]}"; do
    IFS='|' read -r kok _ <<<"$satir"
    derle "tek_$kok"
    cp "_derle/tek_$kok.pdf" "../pdf/$kok.pdf"
  done
fi
echo "Tamam: pdf/"
ls -la ../pdf
