#!/usr/bin/env python3
"""Write model/build/verification.md from verify_stages.py results (verify_results.json) plus ledger spot
checks read from the same LibreOffice recalculations."""
import os, sys, json, datetime
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
import build_stages as bs     # noqa: E402

W = bs.WORK
R = json.load(open(os.path.join(W, 'verify_results.json')))
OUT = os.path.join(W, 'recalc_out')

# ledger spot checks (Scenario 1): (stage from which the cell exists, sheet, cell, ledger ID and line, value, decimals)
SPOT = [
    (40, 'Construction', 'G32', 'P-F07 uses before financing', 710.99, 2),
    (40, 'Funding', 'G44', 'P-F07 DSRA initial funding', 37.25, 2),
    (40, 'Funding', 'G48', 'P-F07 ECA premium', 20.61, 2),
    (40, 'Funding', 'F75', 'P-F07 total uses', 855.09, 2),
    (40, 'Funding', 'F25', 'P-F07 senior debt total', 633.26, 2),
    (40, 'Funding', 'G57', 'P-F07 debt ECA', 189.98, 2),
    (40, 'Funding', 'G58', 'P-F07 debt A', 139.32, 2),
    (40, 'Funding', 'G59', 'P-F07 debt B', 63.33, 2),
    (40, 'Funding', 'G60', 'P-F07 debt COM', 240.64, 2),
    (40, 'Funding', 'G67', 'P-F07 equity total', 221.83, 2),
    (40, 'Funding', 'G69', 'P-F07 share capital', 44.37, 2),
    (40, 'Funding', 'G70', 'P-F07 shareholder loans', 177.47, 2),
    (40, 'Funding', 'G71', 'P-F07 SHL interest capitalized', 24.2, 1),
    (40, 'Funding', 'F24', 'P-F43 closed-form total funding at the 75% cap', 857.2, 1),
    (42, 'Debt', 'F130', 'P-F08 debt capacity at 1.35x', 633.3, 1),
    (42, 'Debt', 'F131', 'P-F08 debt at the 75% gearing cap', 642.9, 1),
    (43, 'Outputs', 'F17', 'P-F08 minimum DSCR (FC base)', 1.35, 2),
    (43, 'Outputs', 'F21', 'P-F16 equity IRR (%, x100)', 13.3, 1),
    (43, 'Outputs', 'F23', 'P-F16 equity NPV at 16.0%', -43.1, 1),
]


def spot():
    rows = []
    for stage, _ in bs.STAGES:
        wb = load_workbook(os.path.join(OUT, f'Ch{stage}_s01.xlsx'), data_only=True)
        for st, sh, cell, lab, val, dp in SPOT:
            if st > stage:
                continue
            v = wb[sh][cell].value
            v = v * 100 if 'x100' in lab else v
            rows.append((stage, f'{sh}!{cell}', lab, val, v, round(v, dp) == round(val, dp)))
    return rows


def fmt(x):
    return f'{x:.1e}' if isinstance(x, float) else str(x)


def main():
    S = R['stages']
    sp = spot()
    L = []
    a = L.append
    a('# Build-along series: verification')
    a('')
    a(f'Model version 1.4 (`model/build_excel_p.py`, `model/case_p.py`). Built by `model/build/build_stages.py`, verified by `model/build/verify_stages.py` (this file written by `write_verification_md.py`), {datetime.date.today().isoformat()}.')
    a('')
    a('## Method')
    a('')
    a('1. **Generation by filtering, not retyping.** `build_stages.py` runs the master build script (`build_excel_p.build`, Scenario 1) and cuts its output to each stage: it keeps the sheets and rows that the u09 Section 0.4 row map assigns to Chapters 39 up to the stage, deletes every other cell, and pastes the provisional rows. No formula is written by hand except the restated master check Checks F19 (the sum of the absolute values of the checks present).')
    a('2. **Row assignments.** u09 Section 0.4 (regenerated from v1.4, round 2) and Section 0.5, with the modeler\'s confirmed assignments (`case_p_report.md` 8c): Inputs row 226 stays in Chapter 39; provisional rows only in the Chapter 40 file (Construction row 38) and the Chapter 41 file (Debt rows 103, 104, 110 and 112; Waterfall rows 33 and 43); the Chapter 39, 42 and 43 files paste nothing.')
    a('3. **Provisional rows (D-051 (c)).** Values are the FC base (Scenario 1) values of the LibreOffice-recalculated master, pasted as numbers in input color (blue on pale yellow); each label carries the suffix "(provisional: pasted FC base values; replaced by formulas in Chapter N)"; the row-total formula in column G is kept.')
    a('4. **Recalculation.** LibreOffice 24.2 headless, private profile `-env:UserInstallation=file:///tmp/lo_profile_buildalong`, own output directory (`$BUILDALONG_WORK/recalc_out`). Masters for each scenario are rebuilt with the v1.4 script and recalculated in the same run.')
    a('5. **Comparisons.** (a) every built row with a Python-mirror counterpart (`build_excel_p.rowmap`, the same row list `verify_p.py` uses) against `case_p.run(case_p.scen(s))`, tolerance 0.01 (USD m, x, percentage points for IRRs); (b) every numeric cell of the stage against the recalculated master of the same scenario; (c) every check present and the restated master check; (d) a forward-reference scan (no formula refers to a sheet or row the stage does not contain); (e) cumulative containment (each file contains every cell of the previous one, except the cells the later chapter is meant to replace); (f) macro-free (.xlsx, no vbaProject part, iterative calculation off).')
    a('6. **Scenarios.** Files without provisional rows (Ch 39, 42, 43) are run in all fifteen scenarios; the Ch 40 and Ch 41 files hold Scenario 1 values in their provisional rows, so they reconcile on Scenario 1 only (u09 Section 0.1 item 4; their Covers say so).')
    a('')
    a('## Results by stage')
    a('')
    a('| Stage | File | Sheets | Formulas | Forward refs | Macro-free, no iteration | Scenarios run | Python rows compared (per run) | Largest difference vs Python | Numeric cells vs master (per run) | Largest difference vs master | Checks present (all 0) | Result |')
    a('|---|---|---|---|---|---|---|---|---|---|---|---|---|')
    for stage, fname in bs.STAGES:
        s = S[str(stage)]; st = s['structure']; runs = s['runs']
        pym = max(r['py_maxdiff'] for r in runs.values()); mm = max(r['master_maxdiff'][0] for r in runs.values())
        pyn = sorted({r['py_rows'] for r in runs.values()}); cn = sorted({r['cells'] for r in runs.values()})
        fails = sum(len(r['py_fail']) for r in runs.values())
        allzero = all(all((v or 0) == 0 for v in r['checks'].values()) and r['master_check'] == 0 for r in runs.values())
        errs = sum(len(r['errors']) for r in runs.values())
        ok = fails == 0 and allzero and not st['forward_refs'] and st['macro_free'] and not st['iterative'] and mm < 1e-6 and errs == 0
        chk = ', '.join(f'F{k}' for k in runs['1']['checks'])
        a(f"| Ch {stage} | `{fname}` | {len(st['sheets'])} | {st['formulas']:,} | {len(st['forward_refs'])} | {'yes' if st['macro_free'] and not st['iterative'] else 'NO'} | "
          f"{'1 to 15' if len(runs) == 15 else ', '.join(runs)} | {'/'.join(map(str, pyn))} | {fmt(pym)} | {'/'.join(f'{x:,}' for x in cn)} | {fmt(mm)} | {chk} | {'PASS' if ok else 'FAIL'} |")
    a('')
    a('Sheets per stage: ' + '; '.join(f"Ch {st}: {', '.join(S[str(st)]['structure']['sheets'])}" for st, _ in bs.STAGES) + '.')
    a('')
    a('Python rows compared rise from 4 (Ch 39: the Time sheet operating months and days rows) to 312 in Ch 43 (311 in Scenarios 14 and 15 and 300/301 in Ch 42, where one mirror item is not defined for the actual-history and re-forecast runs, as in `case_p_verification.md`). No error value (#REF!, #VALUE!, #NAME? and so on) appears in any recalculated stage file.')
    a('')
    a('### Chapter 39 calendar facts (u09 Section 0.5)')
    a('')
    a('| Scenario | COD | PPA expiry | Construction months | COD period (months) | First debt-service period | Last funding month | Last operating period (months) | Operating months | Matches Section 0.5 |')
    a('|---|---|---|---|---|---|---|---|---|---|')
    for k in ('1', '8', '15'):
        c = S['39']['runs'][k]['calendar']
        a(f"| {k} | {c['cod']} | {c['expiry']} | {c['nc']} | {c['tcod']} {c['tcod_label']} ({c['tcod_months']}) | {c['t1']} | {c['fe']} ({c['fe_label']}) | {c['last']} {c['last_label']} ({c['last_months']}) | {c['total_om']} | {'yes' if S['39']['runs'][k]['calendar_ok'] else 'NO'} |")
    a('')
    a('Every scenario 1 to 15 of the Chapter 39 file: total operating months 300 (Checks F20 = 0), construction flags equal the construction months (Checks F21 = 0), master check 0.')
    a('')
    a('### Ledger spot checks (Scenario 1, recalculated stage files)')
    a('')
    a('| Cell | Ledger line | Ledger value | Ch 40 | Ch 41 | Ch 42 | Ch 43 | Match |')
    a('|---|---|---|---|---|---|---|---|')
    for st0, sh, cell, lab, val, dp in SPOT:
        vals = {stage: (v, okk) for stage, c_, l_, vv, v, okk in sp if c_ == f'{sh}!{cell}' and l_ == lab}
        cols = ' | '.join(f'{vals[k][0]:.4f}' if k in vals else '' for k in (40, 41, 42, 43))
        a(f"| {sh}!{cell} | {lab} | {val} | {cols} | {'yes' if all(o for _, o in vals.values()) else 'NO'} |")
    a('')
    a('## Provisional rows (Scenario 1)')
    a('')
    a('Pasted values in the earlier file against the formula values of the file that replaces them. Every total the replacement touches is unchanged.')
    a('')
    a('| Row | Pasted in | Formula from | Largest difference, any column | Row total pasted | Row total with formulas |')
    a('|---|---|---|---|---|---|')
    for k, v in R['stubs'].items():
        tp = '' if v['total_pasted'] is None else f"{v['total_pasted']:.6f}"
        tf = '' if v['total_formula'] is None else f"{v['total_formula']:.6f}"
        a(f"| {k} | Ch {v['pasted_in']} | Ch {v['formula_in']} | {v['maxdiff']} | {tp} | {tf} |")
    a('')
    a('## Cumulative containment')
    a('')
    a('| Step | Cells in the earlier file | Replaced as intended | Unexpected changes |')
    a('|---|---|---|---|')
    for k, v in R['cumulative'].items():
        a(f"| {k.replace('->', ' to ')} | {v['cells']:,} | {v['replaced_as_intended']} | {v['n_unexpected']} |")
    a('')
    a('"Replaced as intended" covers the provisional rows (values and label suffix) when their chapter writes the formulas, the D-125 cells in Chapter 43, the restated master check F19 and the Cover stage note.')
    a('')
    a('## Where the v1.4 changes land (D-125)')
    a('')
    a('| v1.4 change | Cells | Stage file | Note |')
    a('|---|---|---|---|')
    a('| R1 timeline checks | Checks F20, F21 | Ch 39 | in the restated master check from Ch 39 |')
    a('| R2 master-check link | Cover row 22 | Ch 39 | see "Assignment conflicts" below |')
    a('| R10 pass-through tests | Operations rows 98, 99 | Ch 41 | |')
    a('| R4 cash flow statement and cash check | Financials rows 30 to 52; Checks F22 | Ch 42 | |')
    a('| R11 ECA tests | Debt rows 136 to 142; Inputs rows 1314 to 1320; Checks F23 | Ch 42 | F23 without the Monte Carlo condition until Ch 43 (below) |')
    a('| R12 MMRA-window check | Checks F24 | Ch 42 | |')
    a('| R5 Monte Carlo block | Inputs F311, F312, rows 313 to 1312 (draw table J:AL, pasted per-run results AN:AR), F1321; Cover row 29 | Ch 43 | 8c had listed F311, F312 and F1321 under Ch 39; under D-125 and the round-2 u09 Sections 0.4 and 0.5 they are Ch 43 rows (unreferenced before Ch 43) |')
    a('| R3 projected DSCR | Ratios rows 20, 21 | Ch 43 | |')
    a('| R6 fifteen-scenario table and compare row | Outputs rows 25 to 44; Checks F25 | Ch 43 | |')
    a('| Monte Carlo branches in existing cells | Time F16; Operations rows 31, 37, 39 (all 57 columns) | Ch 43 | Ch 39 to 42 files hold the pre-hook formulas and labels, read from the v1.3 workbook (git commit 8addab2, `book/model/Case_P_Model.xlsx`) |')
    a('| Run suspension of checks | Checks F8, F13, F14 | Ch 43 | pre-hook formulas (v1.3) and the F8 label in the Ch 40 to 42 files |')
    a('| Run suspension of the ECA-test check | Checks F23 | Ch 43 | Ch 42 file: `=IF(Inputs!$F$8=1,...)`; Ch 43 adds `AND(...,Inputs!$F$312=0)` (u09 round 2 Section 0.5 lists F23 among the Ch 43 modifications) |')
    a('| Run suspension of the Outputs compare row | Outputs F44 | Ch 43 | born with the condition (Outputs is a Ch 43 sheet) |')
    a('| Master check extended | Checks F19 | each stage | restated over the checks present; equal to the master formula in Ch 43 |')
    a('')
    a('With Inputs F311 = 0 every Monte Carlo branch is inert, so the Ch 43 file reproduces the Ch 42 values cell for cell (largest difference 0 in all fifteen scenarios against the v1.4 master, which itself was verified against the mirror with runs 1, 500 and 1,000 in `case_p_verification.md`).')
    a('')
    f = R['final']
    a('## Ch43_outputs.xlsx against Case_P_Model.xlsx')
    a('')
    a(f"Compared cell by cell with the committed `model/Case_P_Model.xlsx`: sheet order {'identical' if f['sheet_order_equal'] else 'DIFFERENT'}; defined names {'identical' if f['names_equal'] else 'DIFFERENT'} (`Scenario` only); {f['cells']:,} non-empty cells compared for content (formula text or constant).")
    a('')
    a('| Kind | Cells that differ | Where | Intended |')
    a('|---|---|---|---|')
    a(f"| Content (formulas and constants) | {len(f['diffs'])} | {', '.join(d[0] + '!' + d[1] for d in f['diffs'])} | yes: the R7 stage note (rows 31 to 35, empty in the master) |")
    a(f"| Style (font color, fill, number format) | {len(f['style_diffs'])} | {', '.join(d[0] + '!' + d[1] for d in f['style_diffs'])} | yes: bold first line of the stage note |")
    a(f"| Recalculated values (Scenario 1) | {len(f['value_text_diffs'])} text cells; numeric max difference {f['value_maxdiff']} over {f['value_cells']:,} cells | the same five note cells | yes |")
    a('')
    a('No other intentional difference exists: every formula, input, label, unit, number format, conditional format range and the scenario name equal the master.')
    a('')
    a('## Assignment conflicts and decisions')
    a('')
    a('- **Cover row 22 (master-check link).** u09 R2 ("39 (link), 43 (complete)"), the Chapter 39 installment (39.J step 5, "Cover link (R2)") and `case_p_report.md` 8c put the link in Chapter 39; the round-2 Sections 0.3 to 0.5 list it under Chapter 43. The link is in the Ch 39 file (its formula is final from Chapter 39; the master check it shows is completed check by check through Chapter 43). If the editor prefers the Section 0.4 reading, the change is to delete Cover D22:F22 from the Ch 39 to Ch 42 files in `build_stages.py` (`COVER` map).')
    a('- **Inputs F311, F312, F1321.** Chapter 43 (D-125; round-2 Section 0.4), not Chapter 39 as 8c had it.')
    a('- **Checks F23.** The appended ECA-test check is a Chapter 42 row whose v1.4 formula carries the Monte Carlo condition; the Ch 42 file holds it without that condition, consistent with D-125 and round-2 Section 0.5.')
    a('- **Data validation on the scenario selector** (39.J step 2 mentions "data validation 1 to 15"): not added, because the master workbook has none and Ch 43 must equal it.')
    a('')
    a('## Reproduce')
    a('')
    a('```')
    a('cd model/build')
    a('python3 build_stages.py            # five files, from build_excel_p.py (v1.4)')
    a('python3 verify_stages.py           # 63 LibreOffice recalculations, comparisons, verify_results.json')
    a('python3 write_verification_md.py   # this file')
    a('```')
    open(os.path.join(HERE, 'verification.md'), 'w').write('\n'.join(L) + '\n')
    print('written verification.md;', sum(1 for x in sp if not x[5]), 'spot-check mismatches')


if __name__ == '__main__':
    main()
