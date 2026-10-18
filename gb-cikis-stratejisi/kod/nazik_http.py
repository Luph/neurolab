"""Nazik HTTP yardımcısı: en fazla ~2 istek/sn, 429/5xx ve bağlantı hatalarında üstel geri çekilmeyle yeniden deneme.
TLS doğrulaması her zaman açık."""
import time, requests
import yollar
_last = [0.0]
SESSION = requests.Session()
SESSION.headers["User-Agent"] = "gb-cikis-stratejisi/1.0 (kamu politikasi arastirmasi)"
def get(url, params=None, min_interval=0.6, retries=6, timeout=300, **kw):
    yollar.indirme_izni(url)
    for attempt in range(retries):
        wait = min_interval - (time.time() - _last[0])
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time()
        try:
            r = SESSION.get(url, params=params, timeout=timeout, **kw)
        except (requests.ConnectionError, requests.Timeout) as e:
            time.sleep(2 ** attempt); continue
        if r.status_code == 429 or r.status_code >= 500:
            ra = r.headers.get("Retry-After")
            time.sleep(float(ra) if ra and ra.isdigit() else 2 ** attempt)
            continue
        return r
    raise RuntimeError(f"giving up on {url}")
