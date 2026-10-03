#!/usr/bin/env python3
"""Writes model/inputs_case_p.xlsx: the Case P input file as a workbook, one sheet per Case Bible block,
each value with its JSON key path and unit, so that no reader needs to read JSON (u17 fm:model-builds)."""
import json, os, re
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
H = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(H, 'inputs_case_p.json')))
UNITS = [('_usd_m', 'USD m'), ('_kcr_m', 'KCR m'), ('_usd_per_kw_month', 'USD/kW-month'), ('_usd_per_mwh', 'USD/MWh'),
         ('_usd_per_mmbtu', 'USD/MMBtu'), ('_pct', '%'), ('_bps', 'bps'), ('_mw', 'MW'), ('_days', 'days'), ('_months', 'months'),
         ('_years', 'years'), ('_kj_per_kwh', 'kJ/kWh'), ('_mmscfd', 'MMscfd'), ('_mmbtu', 'MMBtu'), ('_date', 'date'), ('_x', 'x')]
def unit(k):
    for suf, u in UNITS:
        if suf in k: return u
    return ''
def rows(x, path):
    if isinstance(x, dict):
        for k, v in x.items(): yield from rows(v, path + [str(k)])
    elif isinstance(x, list) and x and isinstance(x[0], (dict, list)):
        for i, v in enumerate(x): yield from rows(v, path + [f'[{i}]'])
    else:
        yield path, x
wb = Workbook(); wb.remove(wb.active)
B = Font(bold=True); BLUE = Font(color='0000FF'); YEL = PatternFill('solid', fgColor='FFF2CC')
for blk, val in D.items():
    ws = wb.create_sheet(blk[:31])
    ws['A1'] = f'Case P inputs: {blk}'; ws['A1'].font = Font(bold=True, size=13)
    ws['A2'] = 'Source: model/inputs_case_p.json (Case Bible Part 1 as amended by Annex P and the change log). Lists are written across from column D.'
    for j, h in enumerate(['JSON key path', 'Unit', 'Value']): ws.cell(4, 1 + j, h).font = B
    r = 5
    for path, v in rows(val, [blk]):
        key = '.'.join(path); ws.cell(r, 1, key); ws.cell(r, 2, unit(path[-1] if not path[-1].startswith('[') else path[-2]))
        vals = v if isinstance(v, list) else [v]
        for j, x in enumerate(vals):
            c = ws.cell(r, 3 + j, x if isinstance(x, (int, float, str)) or x is None else json.dumps(x)); c.font = BLUE; c.fill = YEL
        r += 1
    ws.column_dimensions['A'].width = 70; ws.column_dimensions['B'].width = 14; ws.column_dimensions['C'].width = 18
wb.save(os.path.join(H, 'inputs_case_p.xlsx')); print('written inputs_case_p.xlsx', len(wb.sheetnames), 'sheets')
