"""Lists numeric literals inside calculation formulas of Case_P_Model.xlsx (FAST check).
Allowed: 0, 1, 12 and unit conversions 100, 1000, 1000000. Usage: python3 scan_hardcodes_p.py [workbook]"""
import re, sys, collections
from openpyxl import load_workbook
path = sys.argv[1] if len(sys.argv) > 1 else 'Case_P_Model.xlsx'
wb = load_workbook(path)
ALLOWED = {'0', '1', '12', '100', '1000', '1000000'}
hits = collections.Counter(); ex = {}
for ws in wb:
    if ws.title in ('Inputs', 'Cover', 'AuditKey'): continue
    for row in ws.iter_rows():
        for c in row:
            v = c.value
            if not (isinstance(v, str) and v.startswith('=')): continue
            if '{' in v: hits[('BRACE', ws.title)] += 1; ex[('BRACE', ws.title)] = (c.coordinate, v[:120])
            f = re.sub(r'"[^"]*"', '', v)
            f = re.sub(r"(\$?[A-Z]{1,3}\$?\d+)", ' ', f)        # cell references
            f = re.sub(r"[A-Za-z_]+[A-Za-z_.0-9]*!", ' ', f)
            for n in re.findall(r'(?<![A-Za-z_\d.])(\d+\.?\d*(?:[eE]-?\d+)?)', f):
                if n.rstrip('0').rstrip('.') in ALLOWED or n in ALLOWED: continue
                hits[(ws.title, n)] += 1; ex[(ws.title, n)] = (c.coordinate, v[:160])
for k, n in sorted(hits.items()):
    print(k, n, ex[k])
print('TOTAL', sum(hits.values()))
