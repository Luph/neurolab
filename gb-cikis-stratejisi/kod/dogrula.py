"""Yeniden üretilen CSV dosyalarını paketteki veri/ ile karşılaştırır.

Her dosya için: bayt bayt aynı mı; değilse aynı satır/sütun yapısında mı ve sayısal sütunlarda en büyük
göreli fark ne (eşik: 1e-6). Metin sütunlarında farklı hücre sayısı raporlanır.

Kullanım: python3 dogrula.py <yeni klasör> <referans klasör: ../veri>
Çıkış kodu: bütün dosyalar eşikte aynıysa 0, değilse 1.
"""

import filecmp
import os
import sys

import numpy as np
import pandas as pd

ESIK = 1e-6


def karsilastir(yeni, ref):
    if filecmp.cmp(yeni, ref, shallow=False):
        return "aynı (bayt bayt)", True
    a, b = pd.read_csv(yeni, dtype=str, keep_default_na=False), pd.read_csv(ref, dtype=str, keep_default_na=False)
    if list(a.columns) != list(b.columns) or a.shape != b.shape:
        return f"yapı farklı: {a.shape} ↔ {b.shape}; sütun farkı {sorted(set(a.columns) ^ set(b.columns))[:6]}", False
    en_buyuk, metin_farki = 0.0, 0
    for s in a.columns:
        x, y = pd.to_numeric(a[s], errors="coerce"), pd.to_numeric(b[s], errors="coerce")
        sayisal = x.notna() & y.notna()
        if sayisal.any():
            fark = (x[sayisal] - y[sayisal]).abs() / np.maximum(y[sayisal].abs(), 1e-12)
            en_buyuk = max(en_buyuk, float(fark.max()))
        metin_farki += int(((a[s] != b[s]) & ~sayisal).sum())
    tamam = en_buyuk <= ESIK and metin_farki == 0
    return f"en büyük göreli fark {en_buyuk:.2e}; sayısal olmayan farklı hücre {metin_farki}", tamam


def main():
    yeni_dizin, ref_dizin = sys.argv[1], sys.argv[2]
    hepsi = True
    for ad in sorted(os.listdir(ref_dizin)):
        if not ad.endswith(".csv"):
            continue
        yeni = os.path.join(yeni_dizin, ad)
        if not os.path.exists(yeni):
            print(f"  YOK     {ad}")
            hepsi = False
            continue
        mesaj, tamam = karsilastir(yeni, os.path.join(ref_dizin, ad))
        hepsi &= tamam
        print(f"  {'TAMAM ' if tamam else 'FARKLI'}  {ad}: {mesaj}")
    print("Sonuç:", "bütün dosyalar aynı" if hepsi else "farklar var (yukarıda)")
    sys.exit(0 if hepsi else 1)


if __name__ == "__main__":
    main()
