"""Paket içi yollar ve çevrimdışı kip.

Bütün betikler ham girdileri varsayılan olarak paketteki girdi/ klasöründen okur (önbellek düzeni:
girdi/f1/..., girdi/f2_cekim/..., girdi/io2023/... vb.). Bir girdi orada yoksa betik onu resmî kaynağından
indirip girdi/'ye yazar. GB_CEVRIMDISI=1 ortam değişkeniyle indirme yasaklanır: eksik bir girdi varsa
betik ağa çıkmak yerine hata verir (yeniden üretim testi: kod/hepsini_uret.sh --cevrimdisi).

Ortam değişkenleri:
  GB_GIRDI       girdi klasörü (varsayılan: <paket>/girdi)
  GB_CEVRIMDISI  "1" ise ağ erişimi yok
"""

import os

PAKET = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
GIRDI = os.environ.get("GB_GIRDI", os.path.join(PAKET, "girdi"))
VERI = os.path.join(PAKET, "veri")


def girdi(*parcalar):
    """girdi/ altındaki bir yol."""
    return os.path.join(GIRDI, *parcalar)


def cevrimdisi():
    return os.environ.get("GB_CEVRIMDISI", "") == "1"


def indirme_izni(neyi):
    """İndirmeden hemen önce çağrılır; çevrimdışı kipte eksik girdiyi açıkça bildirir."""
    if cevrimdisi():
        raise RuntimeError(f"GB_CEVRIMDISI=1: girdi pakette yok ve indirilemez → {neyi}")


def bul(yol):
    """Dosya varsa yolunu, yoksa sıkıştırılmış (.gz) kopyasının yolunu, o da yoksa None döndürür."""
    for aday in (yol, yol + ".gz"):
        if os.path.exists(aday) and os.path.getsize(aday) > 0:
            return aday
    return None
