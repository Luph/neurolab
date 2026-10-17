"""Türkiye'nin 2026 uygulanan ithalat tarifesi, 12 haneli GTİP satırları; Ticaret Bakanlığı'nın konsolide Excel ekleri.
Kimlik doğrulama gerekmez; ticaret.gov.tr bağlantıyı sık düşürdüğü için istekler yeniden denenir.

Türkiye applied import tariff 2026, national 12-digit GTİP lines, from official Ministry of Trade (ticaret.gov.tr) files. Keyless.
 MFN applied = 'DÜ' (Diğer Ülkeler / other countries) column of the consolidated İthalat Rejimi Kararı (Karar 3350) lists I-IV
 İGV         = 'DÜ' column (col '7' in Ek-1) of the consolidated İGV Kararı (Karar 3351) Ek-1, Ek-2, Ek-3
 Universe/desc/Law-474 statutory rate = TGTC 2026 (Karar 10781)."""
import re, io, os, sys, zipfile, unicodedata, urllib.parse
import pandas as pd, openpyxl, xlrd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nazik_http import get
P = 'https://ticaret.gov.tr/ithalat/ithalat-mevzuati/ithalat-rejimi-karari-igv-karari-ve-ithalat-tebligleri/'
PAGES = {'irk': (P + '1-ithalat-rejimi-kararikarar-sayisi3350karar-metni-ve-tablolar-konsolide-edilmis-olup-gunceldir', r'rejim[^"]*\.zip'),
         'igv': (P + '2-ithalatta-ilave-gumruk-vergisi-uygulanmasina-iliskin-karar-karar-sayisi-3351-karar-metni-ve-tablolar-konsolide-edilmis-olup-gunceldir', r'GV\.zip'),
         'tgtc': ('https://ticaret.gov.tr/gumruk-islemleri/mevzuat/cumhurbaskanligi-karari-bkk', r'TGTC\.zip')}
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'}
N = lambda s: unicodedata.normalize('NFKC', str(s)).replace('\n', ' ').strip() if s is not None else ''

def download_zips(outdir):
    """Discover the current zip links on the 3 ministry pages (first match = current year) and download them."""
    os.makedirs(outdir, exist_ok=True); paths = {}
    for k, (page, pat) in PAGES.items():
        html = get(page, headers=UA, timeout=120).text
        href = next(h for h in re.findall(r'href="([^"]+)"', html) if re.search(pat, h))
        href = urllib.parse.quote(href, safe=':/%()')
        r = get(href, headers=UA, timeout=600); r.raise_for_status()
        paths[k] = os.path.join(outdir, k + '.zip'); open(paths[k], 'wb').write(r.content)
        print(k, href, len(r.content))
    return paths

def sheets(zf, name):
    b = zf.read(name)
    if name.lower().endswith('.xlsx'):
        for ws in openpyxl.load_workbook(io.BytesIO(b), read_only=True, data_only=True).worksheets:
            yield ws.title, [list(r) for r in ws.iter_rows(values_only=True)]
    else:
        for s in xlrd.open_workbook(file_contents=b).sheets():
            yield s.name, [s.row_values(i) for i in range(s.nrows)]

def code12(v):
    if v is None or v == '': return None
    if isinstance(v, float): v = int(v) if v == int(v) else v
    s = re.sub(r'[\s.]', '', str(v))
    if not s.isdigit(): return None
    return s.zfill(12) if len(s) in (11, 12) else None

def rate(v):
    """-> (float ad valorem or None, raw text). Leading number of e.g. '27,6 (H)' is kept as value."""
    if v is None or v == '': return None, ''
    if isinstance(v, (int, float)): return float(v), str(v)
    t = N(v); m = re.match(r'^(\d+(?:[.,]\d+)?)', t)
    return (float(m.group(1).replace(',', '.')) if m else None), t

def du_cols(rows):
    """Find header row ('GTİP' in col 0) and the 'DÜ' (or '7') columns of the group-label rows below it."""
    for h, r in enumerate(rows[:12]):
        if r and re.search(r'G\.?T\.?İ?\.?P', N(r[0]).upper()):
            labs = {}
            for rr in rows[max(0, h - 3):h + 4]:
                if not rr or code12(rr[0]): continue        # label rows only (never data rows)
                for j, v in enumerate(rr):
                    if j >= 2 and N(v).replace(' ', '').upper() in ('DÜ', 'D.Ü.', 'D.Ü', '7', '7.0'): labs.setdefault(j, N(v))
            return h, sorted(labs)
    return None, []

def parse_lists(zf, members, kind):
    out = []
    for m in members:
        for title, rows in sheets(zf, m):
            if 'alışma' in N(title): continue            # skip 'Çalışma' (working) sheets
            h, cols = du_cols(rows)
            if h is None or not cols: continue
            for r in rows[h + 1:]:
                c = code12(r[0] if r else None)
                if not c: continue
                v, t = rate(r[cols[0]] if len(r) > cols[0] else None)
                rec = dict(gtip12=c, src=f'{kind}:{os.path.basename(m)}', footnote=N(r[1]) if len(r) > 1 else '', rate=v, rate_text=t)
                if len(cols) > 1:   # III: tarım payı DÜ ; IV: ek mali yükümlülük DÜ
                    rec['extra_text'] = N(r[cols[1]]) if len(r) > cols[1] else ''
                out.append(rec)
    return pd.DataFrame(out)

def parse_tgtc(zf):
    out = []
    for m in zf.namelist():
        if re.search(r'fas[ıi]l \d{4}\.xls$', m, re.I) and 'NOTLARI' not in m:
            title, rows = next(sheets(zf, m))
            for r in rows:
                c = code12(r[0] if r else None)
                if c and len(r) >= 4: out.append(dict(gtip12=c, desc_tr=N(r[1]), unit=N(r[2]), law474_rate=rate(r[3])[0]))
    return pd.DataFrame(out).drop_duplicates('gtip12')

def build(paths, out_csv):
    irk = zipfile.ZipFile(paths['irk']); igv = zipfile.ZipFile(paths['igv']); tg = zipfile.ZipFile(paths['tgtc'])
    lists = [n for n in irk.namelist() if re.search(r'(^|/)(I|II|III|IV) say', N(n), re.I)]
    mfn = parse_lists(irk, lists, 'IRK')
    mfn['list'] = mfn.src.str.extract(r'IRK:(I{1,3}V?|IV)\s', expand=False)
    ig = parse_lists(igv, [n for n in igv.namelist() if n.lower().endswith(('.xlsx', '.xls'))], 'IGV')
    ig = ig.sort_values('rate', ascending=False).groupby('gtip12').agg(igv_rate=('rate', 'first'), igv_text=('rate_text', 'first'), igv_src=('src', lambda s: ';'.join(sorted(set(s))))).reset_index()
    dup = mfn.gtip12.duplicated(keep=False).sum()
    mfn = mfn.drop_duplicates('gtip12', keep='first').rename(columns={'rate': 'mfn_rate', 'rate_text': 'mfn_text', 'src': 'mfn_src', 'extra_text': 'specific_or_emy_DU'})
    tg = parse_tgtc(tg)
    df = tg.merge(mfn, on='gtip12', how='outer', indicator=True).merge(ig, on='gtip12', how='left')
    df['in_tgtc_only'] = df._merge.eq('left_only'); df['in_irk_only'] = df._merge.eq('right_only'); df = df.drop(columns='_merge')
    df['igv_rate'] = df.igv_rate.fillna(0.0)
    df['mfn_plus_igv'] = df.mfn_rate + df.igv_rate
    df['emy_rate_IV'] = pd.to_numeric(df.specific_or_emy_DU.where(df.list.eq('IV')), errors='coerce')   # Ek Mali Yükümlülük (fish), ad valorem
    df['mfn_igv_emy'] = df.mfn_plus_igv + df.emy_rate_IV.fillna(0)
    df.insert(1, 'hs6', df.gtip12.str[:6]); df['year'] = 2026
    df.to_csv(out_csv, index=False)
    print('irk duplicate rows across lists:', dup)
    return df

if __name__ == '__main__':
    outdir = sys.argv[1]
    paths = {k: os.path.join(outdir, k + '.zip') for k in PAGES} if '--offline' in sys.argv else download_zips(outdir)
    df = build(paths, sys.argv[2]); print(df.shape)
