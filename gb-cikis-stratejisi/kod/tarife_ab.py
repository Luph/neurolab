"""AB Kombine Nomenklatürü 2026: CN8 satırları ve konvansiyonel (MFN) vergiler, resmî Formex 4 XML'den.

EU Combined Nomenclature 2026 (Annex I of Commission Implementing Regulation (EU) 2025/1926, OJ L 31.10.2025) -> CSV of CN8 lines
with conventional (MFN) duty, parsed from the official Formex 4 XML served keyless by the Publications Office (Cellar):
  GET https://publications.europa.eu/resource/celex/{CELEX}   headers: Accept: application/zip;mtype=fmx4 , Accept-Language: eng"""
import io, re, os, sys, zipfile, xml.etree.ElementTree as ET
import pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nazik_http import get
def _text(el):
    """text of an element, skipping footnotes (<NOTE>)."""
    parts = [el.text or '']
    for c in el:
        if c.tag != 'NOTE': parts.append(_text(c))
        parts.append(c.tail or '')
    return re.sub(r'\s+', ' ', ''.join(parts)).strip()
def classify(d):
    """-> (ad valorem part in %, type). EU column 3 is in % unless a specific unit follows the number."""
    t = d.replace('\u00a0', ' ').strip(); u = t.upper()
    if not t: return None, 'empty'
    if u.startswith('FREE'): return 0.0, 'adval'
    m = re.fullmatch(r'(\d+(?:,\d+)?)\s*%?', t)
    if m: return float(m.group(1).replace(',', '.')), 'adval'
    m = re.match(r'^\(?\s*(\d+(?:,\d+)?)\s*%?\s*(.*)$', t)
    if m:
        if m.group(2).startswith(('€', 'EUR')): return None, 'specific'
        typ = 'compound_EA' if re.search(r'\bEA\b|AD ?S/Z|AD ?F/M', u) else ('mixed_minmax' if re.search(r'MIN|MAX', u) else 'compound')
        return float(m.group(1).replace(',', '.')), typ
    return None, 'other'
def fetch_cn(celex='32025R1926', out_csv=None, zip_path=None):
    if zip_path and os.path.exists(zip_path): b = open(zip_path, 'rb').read()
    else:
        r = get(f'https://publications.europa.eu/resource/celex/{celex}', headers={'Accept': 'application/zip;mtype=fmx4', 'Accept-Language': 'eng'}, timeout=600)
        r.raise_for_status(); b = r.content
        if zip_path: open(zip_path, 'wb').write(b)
    z = zipfile.ZipFile(io.BytesIO(b))
    annex = max((i for i in z.infolist() if i.filename.endswith('.fmx.xml')), key=lambda i: i.file_size)
    root = ET.fromstring(z.read(annex)); rows, seen, last = [], set(), None
    for row in root.iter('ROW'):
        cells = {c.get('COL'): c for c in row.findall('CELL')}
        if '1' not in cells or '3' not in cells: continue
        code = re.sub(r'\s', '', _text(cells['1']))
        if not code and last is not None and last['duty_type'] in ('empty', 'conditional'):
            # duty split over un-coded sub-rows (seasonal / alcoholic-strength dependent): collect them
            sub = _text(cells['3'])
            if sub:
                last['duty_text'] = (last['duty_text'] + ' | ' if last['duty_text'] else '') + f"{_text(cells['2'])}: {sub}"
                av = [classify(x.split(': ')[-1]) for x in last['duty_text'].split(' | ')]
                last['duty_type'] = 'conditional'
                last['adval_rate'] = max(a for a, k in av if k == 'adval') if all(k == 'adval' for a, k in av) else None
            continue
        if not re.fullmatch(r'\d{8}', code) or code in seen:
            last = None; continue                                         # first occurrence = Part Two schedule
        seen.add(code); duty = _text(cells['3']); av, kind = classify(duty)
        last = dict(cn8=code, hs6=code[:6], desc=_text(cells['2']) if '2' in cells else '', duty_text=duty, adval_rate=av, duty_type=kind,
                    has_note=bool(cells['3'].findall('.//NOTE')), supp_unit=_text(cells['4']) if '4' in cells else '', year=2026)
        rows.append(last)
    df = pd.DataFrame(rows)
    df.loc[df.duty_type.eq('empty') & df.has_note, 'duty_type'] = 'footnote_only'   # e.g. seasonal duties defined in a footnote
    if out_csv: df.to_csv(out_csv, index=False)
    return df
if __name__ == '__main__':
    df = fetch_cn(out_csv=sys.argv[1], zip_path=sys.argv[2] if len(sys.argv) > 2 else None); print(df.shape)
