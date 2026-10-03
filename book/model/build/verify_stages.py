#!/usr/bin/env python3
"""Verify the build-along series (u09 Section 0.5) and write model/build/verification.md.

For each stage file:
  1. structure: sheets present, macro-free (.xlsx, no vbaProject part, iterative calculation off),
     no formula refers to a sheet or row the stage does not contain (forward-reference scan);
  2. recalculation with LibreOffice headless under a PRIVATE profile
     (-env:UserInstallation=file:///tmp/lo_profile_buildalong) into this script's own output directory;
  3. every built row that has a Python-mirror counterpart (build_excel_p.rowmap 'py' key) equals
     case_p.py within 0.01 (USD m, x, percentage points for IRRs);
  4. every numeric cell equals the recalculated master workbook (same scenario);
  5. the checks present in the stage are 0 and the restated master check Checks F19 is 0;
  6. Chapter 39: the calendar facts of u09 Section 0.5 under Scenarios 1, 8 and 15.
Stages 39, 42 and 43 (no provisional rows) are run in all fifteen scenarios; stages 40 and 41
(provisional rows hold Scenario 1 values) on Scenario 1 only.
Finally Ch43_outputs.xlsx is compared with model/Case_P_Model.xlsx cell by cell (formulas, constants,
styles of input cells, and recalculated values).
"""
import os, sys, re, json, zipfile, datetime, shutil
import numpy as np
from openpyxl import load_workbook
from openpyxl.formula.tokenizer import Tokenizer
from openpyxl.utils import column_index_from_string as CI

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.dirname(HERE)
sys.path.insert(0, MODEL); sys.path.insert(0, HERE)
import build_excel_p as bx          # noqa: E402
import case_p as cp                 # noqa: E402
import build_stages as bs           # noqa: E402

WORK = bs.WORK
TOL = 0.01
REF_RE = re.compile(r"^(?:'?([^'!]+)'?!)?\$?([A-Z]{1,3})\$?(\d+)(?::\$?([A-Z]{1,3})\$?(\d+))?$")
NAMES = {'Scenario': ('Inputs', 'F', 8, 'F', 8)}


def refs(formula, home):
    out = []
    try:
        tok = Tokenizer(formula)
    except Exception:
        return out
    for t in tok.items:
        if t.type == 'OPERAND' and t.subtype == 'RANGE':
            v = t.value
            if v in NAMES:
                sh, c1, r1, c2, r2 = NAMES[v]
                out.append((sh, r1, r2)); continue
            m = REF_RE.match(v)
            if not m:
                out.append(('?', v, v)); continue
            sh = m.group(1) or home
            r1 = int(m.group(3)); r2 = int(m.group(5) or r1)
            out.append((sh, r1, r2))
    return out


def structure(stage, path):
    wb = load_workbook(path)
    z = zipfile.ZipFile(path)
    names = z.namelist()
    wbxml = z.read('xl/workbook.xml').decode()
    macro_free = not any('vbaProject' in n for n in names) and path.endswith('.xlsx')
    iterate = 'iterate="1"' in wbxml or "iterate='1'" in wbxml
    sheets = wb.sheetnames
    bad = []
    nform = 0
    for sh in sheets:
        ws = wb[sh]
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith('='):
                    nform += 1
                    for (tsh, r1, r2) in refs(c.value, sh):
                        if tsh == '?':
                            bad.append((sh, c.coordinate, 'unparsed ' + str(r1))); continue
                        if tsh not in sheets:
                            bad.append((sh, c.coordinate, f'sheet {tsh} absent')); continue
                        if r2 - r1 > 2000:
                            continue
                        miss = [r for r in range(r1, r2 + 1) if r >= 5 and not bs.present(tsh, r, stage)]
                        if miss:
                            bad.append((sh, c.coordinate, f'{tsh} rows {miss[:3]} not built'))
    return dict(sheets=sheets, macro_free=macro_free, iterative=iterate, formulas=nform, forward_refs=bad,
                defined_names=list(wb.defined_names.keys()))


def set_scenario(src, dst, s):
    wb = load_workbook(src)
    wb['Inputs']['F8'].value = s
    wb.save(dst)


def num(v):
    if isinstance(v, bool):
        return float(v)
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, datetime.datetime):
        return float((v - datetime.datetime(1899, 12, 30)).days + (v - datetime.datetime(1899, 12, 30)).seconds / 86400)
    if isinstance(v, datetime.date):
        return float((v - datetime.date(1899, 12, 30)).days)
    return None


def compare_master(stage_wb, master_wb):
    n = 0; worst = (0.0, None); nonnum = []
    for sh in stage_wb.sheetnames:
        ws, wm = stage_wb[sh], master_wb[sh]
        for row in ws.iter_rows():
            for c in row:
                x = num(c.value)
                if x is None:
                    continue
                if sh == 'Cover' and c.row >= bs.STAGE_NOTE_ROW:
                    continue
                y = num(wm[c.coordinate].value)
                if y is None:
                    nonnum.append((sh, c.coordinate, c.value, wm[c.coordinate].value)); continue
                n += 1
                d = abs(x - y)
                if d > worst[0]:
                    worst = (d, f'{sh}!{c.coordinate}')
    # error values in stage
    errs = []
    for sh in stage_wb.sheetnames:
        for row in stage_wb[sh].iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith('#') and c.value[1:4].isupper():
                    errs.append(f'{sh}!{c.coordinate}={c.value}')
    return n, worst, nonnum[:10], errs[:10]


def pyval(R, key):
    src, k = key.split('.', 1)
    return R[src][k] if src in ('S', 'f', 'u') else R[k]


def compare_python(stage, wb, scn):
    R = cp.run(cp.scen(scn))
    res = []
    for key, (sh, r, n, py) in bx.rowmap().items():
        if not py or sh not in wb.sheetnames or not bs.present(sh, r, stage):
            continue
        try:
            pv = pyval(R, py)
        except KeyError:
            continue
        ws = wb[sh]
        if n == 0:
            xv = num(ws.cell(r, 6).value)
            d = abs((xv or 0.0) - float(pv)) * (100 if (py.startswith('R.') and 'irr' in py) else 1)
            res.append((key, d))
        else:
            pv = np.asarray(pv, dtype=float)
            xv = np.array([(num(ws.cell(r, 10 + i).value) or 0.0) for i in range(n)], dtype=float)
            m = min(len(pv), n)
            d = np.abs(xv[:m] - pv[:m])
            res.append((key, float(np.nanmax(np.where(np.isnan(d), 1e9, d)))))
    bad = [x for x in res if not x[1] <= TOL]
    return len(res), (max(x[1] for x in res) if res else 0.0), bad


def checks(stage, wb):
    ck = wb['Checks']
    out = {}
    for r in list(range(7, 26)):
        if bs.present('Checks', r, stage):
            out[r] = ck.cell(r, 6).value
    return out


def calendar_facts(wb):
    t = wb['Time']; c = wb['Construction']
    f = lambda r: t.cell(r, 6).value
    om = [t.cell(30, 10 + i).value for i in range(bx.NS)]
    tcod = int(f(12)); last = int(f(15))
    return dict(cod=f(8).date().isoformat(), expiry=f(10).date().isoformat(), nc=int(f(11)), tcod=tcod,
                tcod_label=t.cell(5, 9 + tcod).value, tcod_months=int(om[tcod - 1]), t1=int(f(13)), fe=int(f(14)),
                last=last, last_label=t.cell(5, 9 + last).value, last_months=int(om[last - 1]), total_om=int(sum(om)),
                fe_label=c.cell(5, 9 + int(f(14))).value)


EXPECT39 = {1: dict(cod='2021-05-01', expiry='2046-04-30', nc=33, tcod=6, tcod_months=2, t1=7, fe=35, last=56, last_months=4, total_om=300),
            8: dict(cod='2021-11-01', expiry='2046-10-31', nc=39, tcod=7, tcod_months=2, t1=8, fe=41, last=57, last_months=4, total_om=300),
            15: dict(cod='2021-12-01', expiry='2046-11-30', nc=40, tcod=7, tcod_months=1, t1=8, fe=41, last=57, last_months=5, total_om=300)}


def compare_final(ch43, master_repo, ch43_vals, master_vals):
    a, b = load_workbook(ch43), load_workbook(master_repo)
    out = dict(sheet_order_equal=a.sheetnames == b.sheetnames, names_equal=sorted(a.defined_names.keys()) == sorted(b.defined_names.keys()))
    diffs = []; ncells = 0; style_diffs = []
    for sh in b.sheetnames:
        wa, wb_ = a[sh], b[sh]
        keys = set((c.row, c.column) for row in wa.iter_rows() for c in row if c.value is not None) | \
               set((c.row, c.column) for row in wb_.iter_rows() for c in row if c.value is not None)
        for (r, cc) in sorted(keys):
            ncells += 1
            va, vb = wa.cell(r, cc).value, wb_.cell(r, cc).value
            if va != vb:
                diffs.append((sh, wa.cell(r, cc).coordinate, va, vb))
            ca, cb = wa.cell(r, cc), wb_.cell(r, cc)
            if (ca.font.color and ca.font.color.rgb) != (cb.font.color and cb.font.color.rgb) or ca.fill.fgColor.rgb != cb.fill.fgColor.rgb or ca.number_format != cb.number_format:
                style_diffs.append((sh, ca.coordinate))
    out.update(cells=ncells, diffs=diffs, style_diffs=style_diffs)
    # values after recalculation
    va, vb = load_workbook(ch43_vals, data_only=True), load_workbook(master_vals, data_only=True)
    worst = 0.0; nv = 0; vdiff = []
    for sh in vb.sheetnames:
        wa, wb_ = va[sh], vb[sh]
        keys = set((c.row, c.column) for row in wa.iter_rows() for c in row if c.value is not None) | \
               set((c.row, c.column) for row in wb_.iter_rows() for c in row if c.value is not None)
        for (r, cc) in keys:
            x, y = wa.cell(r, cc).value, wb_.cell(r, cc).value
            nx, ny = num(x), num(y)
            nv += 1
            if nx is not None and ny is not None:
                worst = max(worst, abs(nx - ny))
            elif x != y:
                vdiff.append((sh, wa.cell(r, cc).coordinate, x, y))
    out.update(value_cells=nv, value_maxdiff=worst, value_text_diffs=vdiff)
    return out


def cumulative():
    """Every cell of stage N appears unchanged in stage N+1, except the cells the later chapter is meant
    to replace: provisional rows (values -> formulas, label suffix dropped), the D-125 pre-hook cells
    (Chapter 43), Checks F19 (restated each stage) and the Cover stage note."""
    out = {}
    for (a, fa), (b, fb) in zip(bs.STAGES[:-1], bs.STAGES[1:]):
        wa, wb_ = load_workbook(os.path.join(HERE, fa)), load_workbook(os.path.join(HERE, fb))
        allowed = 0; bad = []; n = 0
        hooks = {(sh, r) for sh, r, _ in bs.V13_ROWS} | {('Checks', 23), ('Checks', 19)}
        for sh in wa.sheetnames:
            if sh not in wb_.sheetnames:
                bad.append((sh, 'sheet dropped')); continue
            for row in wa[sh].iter_rows():
                for c in row:
                    if c.value is None:
                        continue
                    n += 1
                    v2 = wb_[sh][c.coordinate].value
                    if v2 == c.value:
                        continue
                    if (sh, c.row) in bs.STUBS and bs.STUBS[(sh, c.row)][1] == b:
                        allowed += 1; continue
                    if (sh, c.row) in hooks and (b == 43 or c.row == 19):
                        allowed += 1; continue
                    if sh == 'Cover' and c.row >= bs.STAGE_NOTE_ROW:
                        allowed += 1; continue
                    bad.append((sh, c.coordinate, str(c.value)[:60], str(v2)[:60]))
        out[f'{a}->{b}'] = dict(cells=n, replaced_as_intended=allowed, unexpected=bad[:10], n_unexpected=len(bad))
    return out


def main():
    info = json.load(open(os.path.join(WORK, 'stages.json')))
    mdir = os.path.join(WORK, 'masters'); sdir = os.path.join(WORK, 'stage_in'); odir = os.path.join(WORK, 'recalc_out')
    for d in (mdir, sdir, odir):
        os.makedirs(d, exist_ok=True)
    plan = {39: range(1, 16), 40: [1], 41: [1], 42: range(1, 16), 43: range(1, 16)}
    # masters by scenario (v1.4 build script)
    todo = []
    for s in range(1, 16):
        p = os.path.join(mdir, f'm{s:02d}.xlsx')
        bx.build(p, s); todo.append(p)
    # repo master (as committed) for the final comparison
    shutil.copy(os.path.join(MODEL, 'Case_P_Model.xlsx'), os.path.join(mdir, 'repo_master.xlsx')); todo.append(os.path.join(mdir, 'repo_master.xlsx'))
    for stage, fname in bs.STAGES:
        for s in plan[stage]:
            p = os.path.join(sdir, f'Ch{stage}_s{s:02d}.xlsx')
            set_scenario(os.path.join(HERE, fname), p, s); todo.append(p)
    print('recalculating', len(todo), 'files'); sys.stdout.flush()
    bs.soffice_recalc(todo, odir)
    results = {'stages': {}}
    for stage, fname in bs.STAGES:
        st = structure(stage, os.path.join(HERE, fname))
        runs = {}
        for s in plan[stage]:
            wb = load_workbook(os.path.join(odir, f'Ch{stage}_s{s:02d}.xlsx'), data_only=True)
            wm = load_workbook(os.path.join(odir, f'm{s:02d}.xlsx'), data_only=True)
            n, worst, nonnum, errs = compare_master(wb, wm)
            npy, pymax, pybad = compare_python(stage, wb, s)
            ck = checks(stage, wb)
            r = dict(cells=n, master_maxdiff=worst, nonnum=nonnum, errors=errs, py_rows=npy, py_maxdiff=pymax,
                     py_fail=pybad[:10], checks=ck, master_check=wb['Checks']['F19'].value)
            if stage == 39 and s in (1, 8, 15):
                cf = calendar_facts(wb); r['calendar'] = cf
                r['calendar_ok'] = all(cf[k] == v for k, v in EXPECT39[s].items())
            runs[s] = r
            print(stage, s, n, worst, npy, pymax, len(pybad), r['master_check'], errs[:2]); sys.stdout.flush()
        # provisional rows of the previous stage against this stage's formulas (Scenario 1)
        results['stages'][stage] = dict(file=fname, structure=st, runs=runs)
    # stub reconciliation: pasted values (stage N) vs formula values (stage N+1), Scenario 1
    stub = {}
    for (sh, r), (a, b) in bs.STUBS.items():
        wa = load_workbook(os.path.join(odir, f'Ch{a}_s01.xlsx'), data_only=True)[sh]
        wb_ = load_workbook(os.path.join(odir, f'Ch{b}_s01.xlsx'), data_only=True)[sh]
        n = bx.SHEETS[sh].n
        d = max(abs((num(wa.cell(r, 10 + i).value) or 0) - (num(wb_.cell(r, 10 + i).value) or 0)) for i in range(n))
        tot = (num(wa.cell(r, 7).value), num(wb_.cell(r, 7).value))
        stub[f'{sh} {r}'] = dict(pasted_in=a, formula_in=b, maxdiff=d, total_pasted=tot[0], total_formula=tot[1])
    results['stubs'] = stub
    results['final'] = compare_final(os.path.join(HERE, 'Ch43_outputs.xlsx'), os.path.join(MODEL, 'Case_P_Model.xlsx'),
                                     os.path.join(odir, 'Ch43_s01.xlsx'), os.path.join(odir, 'repo_master.xlsx'))
    results['cumulative'] = cumulative()
    json.dump(results, open(os.path.join(WORK, 'verify_results.json'), 'w'), indent=1, default=str)
    print('final:', {k: (v if not isinstance(v, list) else len(v)) for k, v in results['final'].items()})


if __name__ == '__main__':
    main()
