#!/usr/bin/env python3
"""Recalculate Case_P_Model.xlsx with LibreOffice for every scenario and compare every
mapped row and scalar with the Python mirror. Writes recalc/verify_results.json."""
import os, sys, json, subprocess, shutil
import numpy as np
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_excel_p as bx
import case_p as cp

RC = os.path.join(HERE, 'recalc')
os.makedirs(RC, exist_ok=True)
TOL = 0.01

def pyval(R, key):
    src, k = key.split('.', 1)
    if src == 'S': return R['S'][k]
    if src == 'f': return R['f'][k]
    if src == 'u': return R['u'][k]
    if src == 'R': return R[k]

def recalc(scn):
    p = os.path.join(RC, f'scn{scn:02d}.xlsx')
    bx.build(p, scn)
    out = os.path.join(RC, 'out')
    os.makedirs(out, exist_ok=True)
    subprocess.run(['soffice', '--headless', '--calc', '--convert-to', 'xlsx', '--outdir', out, p],
                   check=True, capture_output=True, timeout=600)
    return load_workbook(os.path.join(out, f'scn{scn:02d}.xlsx'), data_only=True)

def compare(scn, wb):
    R = cp.run(cp.scen(scn))
    rows = bx.rowmap(); res = []
    for key, (sh, r, n, py) in rows.items():
        if not py: continue
        ws = wb[sh]
        try:
            pv = pyval(R, py)
        except KeyError:
            continue
        if n == 0:
            xv = ws.cell(r, 6).value
            pv_ = float(pv)
            if py.startswith('R.') and 'irr' in py:
                d = abs((xv or 0) - pv_) * 100   # compare IRRs in percentage points
            else:
                d = abs((xv or 0) - pv_)
            res.append((key, 'scalar', d, xv, pv_))
        else:
            pv = np.asarray(pv, dtype=float)
            xv = np.array([ws.cell(r, 10 + i).value or 0 for i in range(n)], dtype=float)
            m = min(len(pv), n)
            d = np.abs(xv[:m] - pv[:m])
            j = int(d.argmax())
            res.append((key, 'row', float(d.max()), float(xv[j]), float(pv[j]), j))
    chk = wb['Checks']['F' + str(bx.SHEETS['Checks'].key['total'])].value
    return R, res, chk

if __name__ == '__main__':
    scns = [int(a) for a in sys.argv[1:]] or list(range(1, 16))
    allres = {}
    for s in scns:
        wb = recalc(s)
        R, res, chk = compare(s, wb)
        bad = [x for x in res if not (x[2] <= TOL)]
        print(f"scenario {s}: {len(res)} compared, {len(bad)} fail, max diff {max(x[2] for x in res):.2e}, checks {chk}")
        for x in sorted(bad, key=lambda x: -x[2])[:12]:
            print('   ', x)
        allres[s] = dict(n=len(res), fails=len(bad), maxdiff=max(x[2] for x in res), checks=chk,
                         rows=[[x[0], x[1], x[2], x[3], x[4]] for x in res])
    json.dump(allres, open(os.path.join(RC, 'verify_results_%s.json' % '_'.join(map(str, scns))), 'w'), default=float)
