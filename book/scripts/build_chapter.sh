#!/usr/bin/env bash
# Usage: scripts/build_chapter.sh chapters/07-accounting-for-the-project-company.tex
# Compiles one chapter standalone (two passes) into book/build/<name>.pdf and prints errors and warnings summary.
set -u
BOOK="$(cd "$(dirname "$0")/.." && pwd)"
f="$1"; base="$(basename "$f" .tex)"; num="$((10#${base%%-*}))"
mkdir -p "$BOOK/build/$base"
cd "$BOOK/latex"
for pass in 1 2; do
  lualatex -interaction=nonstopmode -halt-on-error -output-directory="$BOOK/build/$base" -jobname="$base" \
    "\def\CHAPFILE{$BOOK/${f%.tex}}\def\CHAPNUM{$num}\input{chapter-test}" > "$BOOK/build/$base/build.log" 2>&1
  rc=$?
  [ $rc -ne 0 ] && break
done
log="$BOOK/build/$base/$base.log"
if [ $rc -ne 0 ]; then echo "BUILD FAILED (rc=$rc). First errors:"; grep -n -A4 '^!' "$log" | head -40; exit 1; fi
echo "BUILD OK: $BOOK/build/$base/$base.pdf ($(grep -c . /dev/null) )"
echo "Pages: $(grep -o 'Output written.*' "$log")"
echo "Overfull boxes: $(grep -c 'Overfull' "$log")"
echo "Undefined references (cross-chapter refs are expected in standalone builds):"
grep -o "Reference \`[^']*' on page" "$log" | sort -u | head -50
