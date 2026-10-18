#!/usr/bin/env bash
# hepsini_uret.sh — Faz 0–2'nin bütün hesaplarını paketteki ham girdilerden (girdi/) yeniden üretir.
#
# Kullanım (paket kökünden ya da herhangi bir yerden):
#   kod/hepsini_uret.sh                          çıktılar veri/ klasörüne yazılır
#   kod/hepsini_uret.sh --cikti /tmp/gb_veri     çıktılar başka klasöre yazılır, sonra veri/ ile karşılaştırılır
#   kod/hepsini_uret.sh --cevrimdisi ...         ağ erişimi yok: eksik girdi varsa betik hata verir
#
# Adımlar betiklerin bağımlılık sırasıyla çalışır (Faz 0 → 1 → 2A → 2B → şekiller). Süre: ≈15–25 dk;
# çoğu çekim modelinde (f2f: 19 PPML spesifikasyonu ve 1.000 çekilişli genel denge).
set -euo pipefail
KOD="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PAKET="$(dirname "$KOD")"
CIKTI="$PAKET/veri"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --cevrimdisi) export GB_CEVRIMDISI=1; shift ;;
    --cikti) CIKTI="$(mkdir -p "$2" && cd "$2" && pwd)"; shift 2 ;;
    *) echo "bilinmeyen seçenek: $1"; exit 2 ;;
  esac
done
cd "$KOD"
if [[ "$CIKTI" != "$PAKET/veri" ]]; then
  # Elle derlenmiş girdiler (kaynakları satır içinde): betikler bunları çıktı klasöründen okur
  cp "$PAKET/veri/vergi_oranlari_2026.csv" "$PAKET/veri/vergi_gelirleri_2024_2026.csv" "$CIKTI/"
fi

adim() {
  local betik="$1"; shift
  local bas=$SECONDS
  printf '%-28s ' "$betik"
  python3 "$betik" --out "$CIKTI" "$@" >"$CIKTI/.$betik.log" 2>&1 \
    || { echo "HATA (ayrıntı: $CIKTI/.$betik.log)"; tail -20 "$CIKTI/.$betik.log"; exit 1; }
  echo "tamam ($((SECONDS - bas)) sn)"
}

echo "Faz 0"
adim f0_nace_kapsam.py
adim f0b_tuik_yshi.py
adim f0c_tuik_bolge_tufe.py
adim f0e_tarifeler.py
adim f0d_s4_tarife_duvari.py
echo "Faz 1"
adim f1a_ab_ticaret.py
adim f1b_odemeler_dengesi.py
adim f1c_sta_asimetrisi.py
adim f1d_maruziyet.py
adim f1e_bolgesel.py
echo "Faz 2A"
adim f2a_io_fiyat.py
adim f2b_tarife_politikasi.py
adim f2c0_takas_parametre.py
adim f2c_vergi_takasi.py
adim f2d_s4_net_istihdam.py
adim f2e_s4_aktif.py
echo "Faz 2B"
adim f2f_cekim_modeli.py
echo "Şekiller"
python3 sekiller.py --veri "$CIKTI" --cikti "$CIKTI/sekiller" >/dev/null && echo "sekiller.py                  tamam"

if [[ "$CIKTI" != "$PAKET/veri" ]]; then
  echo "Karşılaştırma: $CIKTI ↔ veri/"
  python3 dogrula.py "$CIKTI" "$PAKET/veri"
fi
