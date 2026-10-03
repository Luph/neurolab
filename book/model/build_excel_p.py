#!/usr/bin/env python3
"""
Builds model/Case_P_Model.xlsx: the Case P companion workbook with live formulas.

Layout follows the style sheet (Section 5.4): sheets Cover, Inputs, Time, Construction,
Operations, Tax, Funding, Debt, Reserves, Waterfall, Financials, Ratios, Returns, Checks,
Outputs; time across columns; column D label, E unit, F constant, G row total/check,
first period in column J.  Construction and Funding run monthly (August 2018 to December 2022);
all other calculation sheets run semiannually (2018H2 to 2046H2).

Inputs: blue font on pale yellow.  Calculations: black.  Links from other sheets: green.
Checks: 0 when passing, red fill when failing (conditional format).

Circularity: none in the workbook.
  * IDC / fee / ECA premium / DSRA gross-up: closed form (Funding sheet, "affine gross-up"):
    each month's debt balance is carried as alpha + beta x T, so T = alpha / (g - beta).
  * Sculpting with tax: the converged contractual repayment profile is an input (it is a
    contract term after financial close); the live sculpting rows on the Debt sheet recompute
    it from CFADS and the Checks sheet shows the difference.
Requires case_p.py (contract values and input data).
"""
import os, sys, json
import numpy as np
from datetime import date
from openpyxl import Workbook
from openpyxl.utils import get_column_letter as L
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.formatting.rule import CellIsRule
from openpyxl.workbook.defined_name import DefinedName

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import case_p as cp

NS, NM = cp.NS, cp.NM
FC0 = 10                     # column J
BLUE = Font(color='0000FF'); GREEN = Font(color='008000'); BOLD = Font(bold=True)
YEL = PatternFill('solid', fgColor='FFF2CC'); RED = PatternFill('solid', fgColor='FF9999')
HEAD = PatternFill('solid', fgColor='DDEBF7')

def C(i): return L(FC0 + i)

# ----------------------------------------------------------------------------------------
# Row registry: two passes (layout, then formulas) so formulas may reference later rows
# ----------------------------------------------------------------------------------------
SHEETS = {}      # name -> Sheet
CUR = {'sheet': None}

class Sheet:
    def __init__(self, name, tl, title):
        self.name, self.tl, self.title = name, tl, title
        self.n = {'M': NM, 'S': NS, None: 0, 'X': 111}[tl]
        self.rows = []; self.key = {}; self.r = 7
        SHEETS[name] = self
    def sec(self, text):
        self.rows.append(('sec', text, self.r)); self.r += 1
    def gap(self):
        self.r += 1
    def row(self, key, label, unit, fn, total=None, fmt='#,##0.000;(#,##0.000);"-"', py=None,
            first=None, inp=False, const=None):
        self.key[key] = self.r
        self.rows.append(('row', dict(key=key, label=label, unit=unit, fn=fn, total=total, fmt=fmt,
                                      py=py, first=first, inp=inp, const=const), self.r))
        self.r += 1
    def scalar(self, key, label, unit, value, fmt='#,##0.0000', inp=False, py=None):
        self.key[key] = self.r
        self.rows.append(('scalar', dict(key=key, label=label, unit=unit, value=value, fmt=fmt,
                                         inp=inp, py=py), self.r))
        self.r += 1

def ref(key, i=None, off=0, absolute=False):
    """Reference to row `key` ('Sheet.key'); i = column index (0-based), None = column F."""
    sh, k = key.split('.', 1)
    S = SHEETS[sh]; r = S.key[k]
    pre = '' if CUR['sheet'] == sh else f"{sh}!"
    if i is None:
        return f"{pre}$F${r}"
    j = i + off
    if absolute:
        return f"{pre}${C(j)}${r}"
    return f"{pre}{C(j)}{r}"

def rng(key, i0=0, i1=None):
    sh, k = key.split('.', 1); S = SHEETS[sh]; r = S.key[k]
    pre = '' if CUR['sheet'] == sh else f"{sh}!"
    i1 = S.n - 1 if i1 is None else i1
    return f"{pre}${C(i0)}${r}:${C(i1)}${r}"

def rngrel(key, i0, i1):
    sh, k = key.split('.', 1); S = SHEETS[sh]; r = S.key[k]
    pre = '' if CUR['sheet'] == sh else f"{sh}!"
    return f"{pre}{C(i0)}{r}:{C(i1)}{r}"

def V(name):
    """Absolute reference to a named scalar on Inputs or a scalar row elsewhere."""
    return ref(name)

# ----------------------------------------------------------------------------------------
# Build contract and reference run
# ----------------------------------------------------------------------------------------
R1, R14, R15 = cp.build_contract()
K = cp.CONTRACT
ERR = set()    # seeded audit errors for the Chapter 44 exercise copy (empty for the reference workbook)
SG = lambda: '-1*' if 'E10' in ERR else ''

# ========================================================================================
# INPUTS
# ========================================================================================
I = Sheet('Inputs', 'S', 'Inputs: scenario selector, assumptions, contract terms')
I.sec('Scenario control')
I.scalar('Scenario', 'Scenario selector (1-15, see table below)', 'index', 1, '0', inp=True)
I.sec('Live scenario parameters (selected from the scenario table)')
SCN_PARAMS = [  # key, label, unit, function of scenario dict
    ('s_macro', 'Macro path (1 FC forward, 2 actual history, 3 COD re-forecast)', 'code',
     lambda p: {'FC': 1, 'ACT': 2, 'CODRF': 3}[p['macro']]),
    ('s_constr', 'Construction case (1 FC budget, 2 actual)', 'code', lambda p: 1 if p['constr'] == 'FC' else 2),
    ('s_cod_delay', 'COD delay (sensitivity)', 'months', lambda p: p['cod_delay']),
    ('s_capex', 'Capex factor', 'factor', lambda p: p['capex']),
    ('s_avail_d', 'Availability adjustment', 'points', lambda p: p['avail_d']),
    ('s_dispatch', 'Dispatch factor when available', '%', lambda p: p['dispatch']),
    ('s_hr_f', 'Plant heat rate factor', 'factor', lambda p: p['hr_f']),
    ('s_fo_f', 'Fixed opex factor', 'factor', lambda p: p['fo_f']),
    ('s_gas_f', 'Gas price factor', 'factor', lambda p: p['gas_f']),
    ('s_rate_shift', 'Base rate shift from 2022H1', '%', lambda p: p['rate_shift']),
    ('s_deval', 'KCR devaluation from 2022H1', 'fraction', lambda p: p['deval']),
    ('s_xdays', 'Extra days on SEKA capacity/VOM payments, 2022H1-2022H2', 'days',
     lambda p: p['delay_days'] + p['lag_days']),
    ('s_crisis', 'Offtaker crisis events (1 = on)', 'flag', lambda p: p['crisis']),
    ('s_ins_step', 'Insurance market step-up from 2022H2 (1 = on)', 'flag', lambda p: p['ins_step']),
    ('s_profile', 'Repayment profile (1 FC contract, 2 COD re-sculpted)', 'code', lambda p: 1 if p['profile'] == 'FC' else 2),
    ('s_ld_prep', 'Performance LD prepayment June 2022 (1 = on)', 'flag', lambda p: p['ld_prep']),
    ('s_waiver', 'Waiver and amendment 2023 (1 = on)', 'flag', lambda p: p['waiver']),
    ('s_refi', '2025 bond refinancing (1 = on)', 'flag', lambda p: p['refi']),
    ('s_mode', 'Funding mode (1 committed amounts, 2 re-grossed pro rata)', 'code',
     lambda p: 2 if (p['capex'] != 1.0 or p['cod_delay']) else 1),
    ('s_miniperm', 'Soft mini-perm sweep (1 = on)', 'flag', lambda p: p['miniperm']),
    ('s_shl', 'Shareholder loan share of equity', 'fraction', lambda p: p['shl_share']),
    ('s_capf', 'Capital charge factor', 'factor', lambda p: p['cap_charge_f']),
    ('s_disp_path', 'Actual 2022 dispatch path (1 = on)', 'flag', lambda p: p['disp_path']),
]
for k, lab, un, fn in SCN_PARAMS:
    I.row(k + '_tbl', lab + ' [table]', un, None, inp=True)
for k, lab, un, fn in SCN_PARAMS:
    I.scalar(k, lab, un, None, '0.0000')

SC = {}
def add_scalars(section, items):
    I.sec(section)
    for k, lab, un, v in items:
        I.scalar(k, lab, un, v, '#,##0.00000', inp=True)
        SC[k] = v

add_scalars('Capital cost (USD m unless stated)', [
    ('epc_price', 'EPC contract price', 'USD m', 571.84),
    ('epc_off', 'of which offshore portion', 'USD m', 489.17),
    ('epc_on', 'of which onshore portion', 'USD m', 82.67),
    ('on_rate', 'Onshore portion fixed in KCR at', 'KCR/USD', 519.4),
    ('owners', "Owner's costs", 'USD m', 46.18),
    ('ins_c', 'Insurance during construction', 'USD m', 7.62),
    ('dev_c', 'Development costs reimbursed at FC', 'USD m', 21.43),
    ('dev_fee', 'Development fee at FC', 'USD m', 11.20),
    ('adv', "Lenders' advisors and legal", 'USD m', 8.97),
    ('cont', 'Contingency', 'USD m', 38.40),
    ('init_wc', 'Initial working capital (spares, fuel)', 'USD m', 5.35),
    ('lntp', 'LNTP paid February 2018 (equity credit at FC)', 'USD m', 14.20),
    ('ext_own', "Extended owner's costs (actual, months 34-40)", 'USD m', cp.EXT_OWNERS),
    ('vat_rate', 'VAT on onshore EPC', '%', 18.0),
    ('vat_spread', 'VAT facility margin over policy rate', '%', 2.5),
    ('vat_limit', 'VAT facility limit', 'KCR m', 7900.0),
    ('fc_policy', 'Policy rate, FC expectation', '%', 13.5),
])
add_scalars('Senior debt terms', [
    ('sh_E', 'ECA-covered tranche share', 'fraction', 0.30), ('sh_A', 'ABDB A-loan share', 'fraction', 0.22),
    ('sh_B', 'ABDB B-loan share', 'fraction', 0.10), ('sh_C', 'Commercial tranche share', 'fraction', 0.38),
    ('m_E', 'ECA margin', '%', 1.35), ('m_A', 'A-loan margin', '%', 3.65), ('m_B', 'B-loan margin', '%', 3.40),
    ('m_C1', 'Commercial margin to 2025', '%', 4.10), ('m_C2', 'Commercial margin 2026-2029', '%', 4.60),
    ('m_C3', 'Commercial margin from 2030', '%', 5.10),
    ('cf_E', 'ECA commitment fee', '% pa', 0.45), ('cf_A', 'A-loan commitment fee', '% pa', 0.75),
    ('cf_B', 'B-loan commitment fee', '% pa', 0.85), ('cf_Cpct', 'Commercial commitment fee (% of margin)', '%', 40.0),
    ('uf_E', 'ECA arrangement fee', '%', 1.10), ('uf_A', 'A-loan front-end fee', '%', 1.25),
    ('uf_B', 'B-loan upfront fee', '%', 1.50), ('uf_C', 'Commercial upfront fee', '%', 2.15),
    ('wht', 'Withholding tax on commercial interest (grossed up)', '%', 10.0),
    ('eca_prem', 'ECA premium (% of ECA drawdowns, financed)', '%', 10.85),
    ('pri_rate', 'PRI premium', '% pa', 1.15), ('pri_cover', 'PRI cover of commercial tranche', '%', 90.0),
    ('swap_fix', 'Swap fixed rate', '%', 2.947), ('cas', 'ISDA 6M spread adjustment', '%', 0.42826),
    ('sb_commit', 'Standby facility', 'USD m', 46.0), ('sb_cf', 'Standby commitment fee', '% pa', 0.60),
    ('sb_add', 'Standby margin over tranche margin', '%', 0.25), ('sb_com', 'Standby commercial share', 'fraction', 0.60),
    ('ce', 'Contingent equity', 'USD m', 15.4),
    ('shl_rate', 'Shareholder loan rate', '% pa', 9.5),
    ('gear', 'Gearing cap', 'fraction', 0.75), ('dscr_t', 'Sizing DSCR target', 'x', 1.35),
    ('agency', 'Agency and account fees', 'USD m pa', 0.255),
    ('lu_dscr', 'Lock-up historic DSCR', 'x', 1.20), ('eod_dscr', 'Event of default DSCR', 'x', 1.10),
    ('rel_dscr', 'Waiver release DSCR (two consecutive tests)', 'x', 1.25),
    ('mp_share', 'Soft mini-perm sweep share (from 2027)', 'fraction', 0.50),
])
add_scalars('Contract terms fixed at financial close (from the FC base sizing run)', [
    ('D_c', 'Senior debt commitment (total, 4 tranches)', 'USD m', K['D']),
    ('E_c', 'Equity commitment (base, incl. LNTP)', 'USD m', K['E']),
])
add_scalars('Plant and PPA', [
    ('C_fc', 'Contracted capacity (FC)', 'MW', 588.4), ('C_act', 'Contracted capacity after tests', 'MW', 581.9),
    ('HR_g', 'Guaranteed net heat rate', 'kJ/kWh', 6261), ('HR_t', 'Tested net heat rate', 'kJ/kWh', 6286),
    ('HR_c', 'PPA contracted heat rate', 'kJ/kWh', 6323), ('HR_cdeg', 'Contracted HR degradation allowance', '% pa', 0.10),
    ('pl', 'Average part-load penalty', '%', 2.3), ('hhv', 'HHV/LHV ratio', 'factor', 1.108),
    ('kj', 'kJ per MMBtu', 'kJ', 1055056), ('o_nr', 'Output degradation, non-recoverable', '% pa', 0.15),
    ('o_rec', 'Output degradation, recoverable average', '%', 1.0), ('h_nr', 'Heat-rate degradation, non-recoverable', '% pa', 0.12),
    ('h_rec', 'Heat-rate degradation, recoverable average', '%', 0.8), ('gt_hours', 'GT operating hours per year', 'h', 8059),
    ('gt_starts', 'GT starts per year', 'starts', 38), ('disp_base', 'Base dispatch for GT hours', '%', 76.5), ('eoh_start', 'EOH per start', 'h', 10),
    ('a_target', 'PPA availability target', '%', 90.0),
    ('cap_chg', 'Capital charge (Nov 2016 prices)', 'USD/kW-month', 14.36), ('cap_idx', 'Capital charge indexed share', 'fraction', 0.20),
    ('fom_chg', 'Fixed O&M charge', 'USD/kW-month', 2.31), ('fom_us', 'Fixed O&M US CPI share', 'fraction', 0.62),
    ('bid_fx', 'Bid base FX rate', 'KCR/USD', 462.35), ('vom_chg', 'Variable O&M charge', 'USD/MWh', 3.86),
    ('vom_us', 'VOM US CPI share', 'fraction', 0.70),
])
add_scalars('Fuel and transport', [
    ('gas_p', 'GSA gas price 2018', 'USD/MMBtu', 5.86), ('gas_esc', 'GSA escalation', '% pa', 2.0),
    ('dcq', 'Daily contract quantity', 'MMBtu/d', 72400), ('top', 'Take-or-pay level', 'fraction', 0.80),
    ('gta_cap', 'GTA reserved capacity', 'MMBtu/d', 96500), ('gta_r', 'GTA reservation charge 2018', 'USD/MMBtu', 0.62),
    ('gta_c', 'GTA commodity charge 2018', 'USD/MMBtu', 0.19), ('gta_esc', 'GTA escalation', '% pa', 1.5),
])
add_scalars('Operating costs (2018 prices)', [
    ('om_fee', 'O&M fixed fee', 'USD m pa', 7.92), ('om_usd', 'O&M USD share', 'fraction', 0.65),
    ('fx18', 'KCR conversion rate for 2018-price local costs', 'KCR/USD', 516.8),
    ('om_inc', 'O&M availability incentive (max)', 'USD m pa', 0.60),
    ('ltsa_fix', 'LTSA fixed fee', 'USD m pa', 2.64), ('ltsa_var', 'LTSA variable fee', 'USD/EOH/GT', 486.0),
    ('ins_o', 'Operational insurance', 'USD m pa', 4.37), ('ins_step', 'Insurance market step-up (actual, from 2022H2)', 'fraction', 0.18),
    ('ga', 'Project company G&A', 'USD m pa', 3.18), ('land', 'Land lease and permits', 'KCR m pa', 368.0),
    ('comm', 'Community fund + OREK levy', '% of non-fuel revenue', 0.55),
    ('consum', 'Variable consumables', 'USD/MWh', 1.08), ('prg', 'ABDB PRG fee (0.75% x USD 41.5m)', 'USD m pa', 0.0075 * 41.5),
    ('mm_maj', 'Major maintenance outside LTSA (OY8, 16, 24)', 'USD m', 9.47),
    ('mm_min', 'HRSG/BOP works outside LTSA (OY4, 12, 20)', 'USD m', 2.18),
    ('hb', 'Handback reserve from OY20', 'USD m pa', 1.85),
])
add_scalars('Working capital', [
    ('rec_d', 'Receivable days', 'days', 45), ('gas_d', 'Gas payable days', 'days', 45),
    ('gta_d', 'GTA payable days', 'days', 30), ('om_d', 'O&M/LTSA payable days', 'days', 30), ('oth_d', 'Other payable days', 'days', 30),
])
add_scalars('Tax', [
    ('cit', 'Corporate income tax', '%', 30.0), ('cit_red', 'Reduced rate OY6-OY8', '%', 15.0),
    ('mtt', 'Minimum turnover tax (non-fuel revenue, from OY6)', '%', 0.5),
    ('dep_pl', 'Plant share of capitalized cost', 'fraction', 0.92), ('life_pl', 'Plant life', 'months', 240),
    ('dep_bl', 'Buildings share', 'fraction', 0.05), ('life_bl', 'Buildings life', 'months', 300),
    ('dep_in', 'Intangibles share', 'fraction', 0.03), ('life_in', 'Intangibles life', 'months', 60),
    ('thin', 'Thin capitalization ratio (SHL to equity)', 'x', 3.0), ('dt_rate', 'Deferred tax rate', '%', 30.0),
])
from datetime import date as _d
I.sec('Timing and event dates (all dates are inputs; flags on the Time sheet read them)')
DATES = [
    ('d_lntp', 'LNTP payment date', _d(2018, 2, 5)), ('d_fc', 'Financial close', _d(2018, 7, 17)),
    ('d_ntp', 'Notice to proceed (Month 1 start)', _d(2018, 8, 1)), ('d_s1', 'First semiannual period start', _d(2018, 7, 1)),
    ('d_cod_fc', 'COD, FC base', _d(2021, 5, 1)), ('d_cod_act', 'COD, actual', _d(2021, 12, 1)),
    ('d_maturity', 'Final maturity, bank debt', _d(2034, 6, 30)), ('d_shock', 'Start of devaluation, payment-delay and base-rate sensitivities', _d(2022, 1, 1)),
    ('d_rf_cut', 'COD re-forecast: first projected period', _d(2022, 1, 1)), ('d_ins_step', 'Insurance step-up from', _d(2022, 7, 1)),
    ('d_sofr', 'Loans switch to Term SOFR + CAS', _d(2023, 1, 1)), ('d_settle', 'Arrears settlement agreement', _d(2024, 3, 21)),
    ('d_ldprep', 'Performance LD prepayment date', _d(2022, 6, 30)), ('d_test1', 'First waived test date', _d(2023, 6, 30)),
    ('d_test2', 'Second waived test date (principal deferral)', _d(2023, 12, 31)), ('d_up1', 'Margin uplift from', _d(2023, 7, 1)),
    ('d_up2', 'Margin uplift to', _d(2024, 12, 31)), ('d_drep1', 'First deferred repayment', _d(2024, 6, 30)),
    ('d_drep2', 'Last deferred repayment', _d(2025, 12, 31)), ('d_refi', 'Refinancing settlement', _d(2025, 6, 30)),
    ('d_mp', 'Soft mini-perm sweep from', _d(2027, 1, 1)), ('d_mC2', 'Commercial margin step 1 from', _d(2026, 1, 1)),
    ('d_mC3', 'Commercial margin step 2 from', _d(2030, 1, 1)),
]
for k, lab, v in DATES:
    I.scalar(k, lab, 'date', v, 'yyyy-mm-dd', inp=True); SC[k] = v
add_scalars('Structural constants (FAST: no numbers inside calculation formulas)', [
    ('ppa_years', 'PPA term', 'years', 25), ('shock_months', 'Length of the shock sensitivities', 'months', 12),
    ('mid', 'Mid-period offset for FC FX drift', 'periods', 0.5), ('fc_k', 'FC Kessara CPI expectation', '%', 7.5), ('fc_u', 'FC US CPI expectation', '%', 2.2),
    ('hrs_m', 'Hours per month (8,760 / 12)', 'h', 730), ('om_pivot', 'O&M incentive zero point', '%', 92.0), ('om_band', 'O&M incentive band (points to full incentive)', 'points', 3.0),
    ('ga_us', 'G&A US CPI share', 'fraction', 0.5), ('cons_us', 'Consumables US CPI share', 'fraction', 0.7),
    ('av_cycle', 'Availability profile cycle', 'years', 8), ('mm_month', 'Month of the operating year when out-of-LTSA maintenance is spent', 'month', 7),
    ('mm_last', 'Last operating year with out-of-LTSA maintenance', 'OY', 24), ('mm_maj_c', 'Major overhaul cycle', 'years', 8), ('mm_min_c', 'HRSG/BOP works cycle', 'years', 4),
    ('mmra_n', 'MMRA accumulation periods (window fixed at six columns)', 'periods', 6), ('mpp', 'Months per operating period', 'months', 6),
    ('hb_oy', 'Handback reserve from operating year', 'OY', 20), ('hol_y', 'Full tax exemption', 'years', 5), ('red_y', 'Reduced rate to end of operating year', 'OY', 8),
    ('idx_by', 'Index base year (index = 100 at November)', 'year', 2016), ('idx_bm', 'Index base month', 'month', 11), ('idx_100', 'Index base value', 'index', 100),
    ('rd_cost1', 'First cost reading month (September 2018)', 'month', 9), ('rd_tar1', 'First tariff reading month (March 2018)', 'month', 3),
    ('rd_b18', '2018 price base month (June 2018)', 'month', 6), ('rd_lag', 'Reading months in the prior year for a January reset', 'months', 3),
    ('epc_fc_m', 'FC EPC payment months', 'months', 33), ('to_pct', 'Taking-over payment', '% of EPC price', 7.5), ('own_ext', "Owner's cost rate per extra month (FC delay sensitivity)", '%', 2.75),
    ('ext1', 'Actual extension window: first month', 'month', 34), ('ext2', 'Actual extension window: last month', 'month', 40), ('ins_m2', 'Second insurance installment month', 'month', 18),
    ('ins_sh1', 'Insurance paid at FC', 'fraction', 0.85), ('adv_sh1', "Lenders' advisors paid at FC", 'fraction', 0.70), ('ld_month', 'Month delay LDs and DSU are received', 'month', 40),
    ('vat_lag', 'VAT refund lag', 'months', 9), ('day_usd', 'Day basis, USD loans', 'days', 360), ('day_kcr', 'Day basis, KCR items, SHL, premiums', 'days', 365),
    ('sb_split', 'Standby share of overrun funding (rest contingent equity)', 'fraction', 0.75), ('def_n', 'Number of deferred repayments', 'count', 4),
    ('eca_cap', 'ECA-covered tranche cap', 'USD m', 224.1), ('npv_r', 'Equity NPV rate', '%', 16.0), ('eps', 'Numerical zero (balances and debt service)', 'USD m', 0.000000001),
    ('eps_r', 'Reserve tolerance', 'USD m', 0.000001), ('irr_g', 'XIRR starting guess, project IRR', 'fraction', 0.1),
    ('price_yr', 'Price base year for GSA and GTA escalation', 'year', 2018), ('lu_n', 'Consecutive lock-ups before the lock-up cash sweep', 'count', 2),
    ('n_gt', 'Number of gas turbines', 'count', 2), ('fxh_share', 'Share of onshore KCR EPC payments hedged forward', 'fraction', cp.FXH_SHARE), ('tol_sc', 'Sculpting convergence tolerance (USD 1,000)', 'USD m', 0.001),
])
add_scalars('Events (actual history)', [
    ('gas_arr', 'Share of SEKA arrears matched by deferred SNHK/GCK payables (calibration)', 'fraction', cp.GAS_ARREARS_SHARE),
    ('lpi_sp', 'Late payment interest spread', '%', 2.0), ('lpi_paid', 'Late payment interest received (1 - waived)', 'fraction', 0.60),
    ('ld_delay', 'EPC delay LDs received Nov 2021', 'USD m', cp.OVR['epc_delay_lds_usd_m']),
    ('dsu', 'DSU insurance proceeds Nov 2021', 'USD m', cp.OVR['dsu_proceeds_usd_m']),
    ('ld_perf', 'Performance LDs (prepay June 2022)', 'USD m', 18.485),
    ('w_fee', 'Waiver fee', '% of senior debt', 0.25), ('w_up', 'Margin uplift 2023H2-2024H2', '%', 0.50),
    ('w_def', 'Deferred share of 2023-12-31 principal', 'fraction', 0.60),
    ('b_cpn', 'Bond coupon', '%', 7.875), ('b_px', 'Bond issue price', 'fraction', 0.99512),
    ('b_uw', 'Underwriting fee', 'fraction', 0.01), ('b_oth', 'Other transaction costs', 'USD m', 3.10),
    ('pcg', 'ABDB partial credit guarantee', 'USD m', 95.0), ('pcg_fee', 'PCG fee', '% pa', 1.10),
    ('pcg_up', 'PCG upfront fee', '%', 0.75), ('unw_r', 'Flat swap rate for unwind', '%', 3.68),
    ('unw_sh', 'Share of swap terminated', 'fraction', 0.48), ('sw_rem', 'Share of swap remaining after refi', 'fraction', 0.52),
])

# annual CPI table (rows 2015..2049) placed as rows with years across? -> vertical block in cols J..
I.sec('Annual tables (columns J = 2015 ... ): CPI annual average change (%), policy rate (%)')
YEARS = list(range(2015, 2050))
for k, lab in [('yr', 'Calendar year'), ('us_fc', 'US CPI, FC expectation'), ('kc_fc', 'Kessara CPI, FC expectation'),
               ('us_act', 'US CPI, actual history + assumptions'), ('kc_act', 'Kessara CPI, actual history + assumptions'),
               ('us_rf', 'US CPI, COD re-forecast'), ('kc_rf', 'Kessara CPI, COD re-forecast'),
               ('pol_act', 'Kessara policy rate (actual)')]:
    I.row('A_' + k, lab, 'year' if k == 'yr' else '%', None, inp=True)

I.sec('Semiannual inputs (column J = 2018H2 ... BN = 2046H2)')
for k, lab, un in [('base_fc', '6M LIBOR forward curve at FC', '%'),
                   ('base_act', '6M LIBOR to 2022H2; 6M Term SOFR + CAS from 2023H1 (actual)', '%'),
                   ('base_rf', 'Base rate, COD re-forecast', '%'),
                   ('fx_act', 'KCR per USD, semiannual average (actual to 2026H2)', 'KCR/USD'),
                   ('overdue', 'SEKA overdue receivables at period end (actual)', 'USD m'),
                   ('fxloss', 'FX conversion losses (actual)', 'USD m'),
                   ('lpi_sh', 'Settlement installment share of late payment interest', 'fraction'),
                   ('prof_fc', 'Contract repayment profile at FC, A-loan, B-loan, commercial and standby (share of their amount; ECA in equal installments)', 'fraction'),
                   ('prof_cod', 'COD re-sculpted repayment profile, tranches other than ECA (share of their amount at COD)', 'fraction'),
                   ('prof_bond', 'Bond amortization profile (share of face)', 'fraction'),
                   ('N_s', 'Swap notional schedule, semiannual (contract)', 'USD m'),
                   ('av8', 'Availability profile by OY (8-year cycle, cols J-Q)', '%'),
                   ('disp_act', 'Actual dispatch when available, 2022 drought (annex 4.11)', '%')]:
    I.row('S_' + k, lab, un, None, inp=True)
I.sec('Monthly inputs (column J = Aug 2018 ... BJ = Dec 2022)')
for k, lab, un in [('epc_fc', 'EPC payment profile, FC (33 months)', '%'), ('epc_act', 'EPC payment profile, actual (40 months)', '%'),
                   ('own_fc', "Owner's cost profile, FC", '%'), ('ovr', 'Overrun items, actual (excl. extended owners)', 'USD m'),
                   ('N_m', 'Swap notional schedule, monthly (contract)', 'USD m')]:
    I.row('M_' + k, lab, un, None, inp=True)

# ---- v1.4 appended blocks (u09 Section 0.7 R5 and R11): below the last used row, so no address moves
I.gap()
I.scalar('mc_run', 'Monte Carlo run number (0 = off; 1 to 1,000 reads that row of the draw table, Scenario 1 only)', 'index', 0, '0', inp=True)
I.scalar('mc_on', 'Monte Carlo active (run number above 0 and Scenario 1)', 'flag', f"=IF(AND({V('Inputs.mc_run')}>0,{V('Inputs.Scenario')}=1),1,0)", '0')
MC_R0 = I.r; MC_N = cp.MC_RUNS; MC_NY = cp.MC_NY
I.r += MC_N            # draw table rows (written in build(): runs by 26 availability shocks, dispatch, heat-rate degradation, FX drift)
I.gap()
add_scalars('ECA test limits (OECD Arrangement, 2018 commitments) and constants for the appended rows', [
    ('eca_tenor', 'ECA limit: repayment term from COD', 'years', 14.0),
    ('eca_wal', 'ECA limit: weighted average life from COD', 'years', 7.25),
    ('eca_max', 'ECA limit: largest installment', '% of principal', 25.0),
    ('eca_m', 'ECA limit: months from COD to first repayment (and window for the minimum share)', 'months', 24.0),
    ('eca_min', 'ECA limit: minimum share repaid within the window', '% of principal', 2.0),
    ('day_yr', 'Days per year for life measures', 'days', 365.25),
    ('mc_ny', 'Monte Carlo: operating years with an availability shock', 'years', float(cp.MC_NY)),
])
def _mcr(c0, c1):
    return f"Inputs!${L(FC0 + c0)}${MC_R0}:${L(FC0 + c1)}${MC_R0 + MC_N - 1}"
MC_SHK = _mcr(0, MC_NY - 1); MC_DISP = _mcr(MC_NY, MC_NY); MC_HNR = _mcr(MC_NY + 1, MC_NY + 1); MC_FXD = _mcr(MC_NY + 2, MC_NY + 2)
MCON = lambda: V('Inputs.mc_on'); MCRUN = lambda: V('Inputs.mc_run')

# ========================================================================================
# TIME
# ========================================================================================
T = Sheet('Time', 'S', 'Time: semiannual operating timeline (monthly timeline on the Construction sheet)')
T.sec('Key dates (scenario-dependent)')
def tsc(k, lab, un, f, fmt='0'):
    T.scalar(k, lab, un, f, fmt)
tsc('cod', 'Commercial operation date', 'date',
    f"=IF({V('Inputs.s_constr')}<>1,{V('Inputs.d_cod_act')},EDATE({V('Inputs.d_cod_fc')},{V('Inputs.s_cod_delay')}))", 'yyyy-mm-dd')
tsc('ppam', 'PPA term', 'months', f"={V('Inputs.ppa_years')}*12")
tsc('expiry', 'PPA expiry', 'date', f"=EDATE({V('Time.cod')},{V('Time.ppam')})-1", 'yyyy-mm-dd')
tsc('nc', 'Construction months (NTP to COD)', 'months', f"=(YEAR({V('Time.cod')})-YEAR({V('Inputs.d_ntp')}))*12+MONTH({V('Time.cod')})-MONTH({V('Inputs.d_ntp')})")
tsc('tcod', 'Period containing COD (period number)', 'index', lambda: f"=MATCH({V('Time.cod')},{rng('Time.start')},1)")
tsc('t1', 'First debt service period', 'index', f"={V('Time.tcod')}+1")
tsc('fe', 'Last month of the funding period (month number)', 'index', lambda: f"=MATCH(INDEX({rng('Time.end')},1,{V('Time.tcod')}),{rng('Construction.end')},0)")
tsc('lastop', 'Last operating period (period number)', 'index', None)
tsc('fx_d', 'FC FX drift per year (Kessara / US CPI expectations; Monte Carlo draw when active)', 'factor', f"=IF({MCON()}=1,INDEX({MC_FXD},{MCRUN()}),(1+{V('Inputs.fc_k')}/100)/(1+{V('Inputs.fc_u')}/100))", '0.000000')
tsc('tR', 'Refinancing period (period number)', 'index', lambda: f"=MATCH({V('Inputs.d_refi')},{rng('Time.end')},0)")
tsc('t23', 'Deferral period (period number)', 'index', lambda: f"=MATCH({V('Inputs.d_test2')},{rng('Time.end')},0)")
T.sec('Semiannual timeline')
T.row('t', 'Period number', 'index', lambda i: f"={ref('Time.t', i, -1)}+1", fmt='0')
T.row('mper', 'Months per period', 'months', lambda i: f"={V('Inputs.mpp')}", fmt='0')
T.row('start', 'Period start', 'date', lambda i: f"=IF({ref('Time.t', i)}=1,{V('Inputs.d_s1')},EDATE({ref('Time.start', i, -1)},{ref('Time.mper', i)}))", fmt='yyyy-mm-dd')
T.row('end', 'Period end', 'date', lambda i: f"=EOMONTH({ref('Time.start', i)},{ref('Time.mper', i)}-1)", fmt='yyyy-mm-dd')
T.row('yf30', 'Year fraction 30/360 (months / 12)', 'factor', lambda i: f"={ref('Time.mper', i)}/12", fmt='0.0000')
T.row('days', 'Days in period', 'days', lambda i: f"={ref('Time.end', i)}-{ref('Time.start', i)}+1", fmt='0')
T.row('year', 'Calendar year', 'year', lambda i: f"=YEAR({ref('Time.start', i)})", fmt='0')
T.row('half', 'Flag_FirstHalf (Jan-Jun)', 'flag', lambda i: f"=IF(MONTH({ref('Time.start', i)})=1,1,0)", fmt='0')
T.row('os', 'Operations start in period', 'date', lambda i: f"=MAX({ref('Time.start', i)},{V('Time.cod')})", fmt='yyyy-mm-dd')
T.row('oe', 'Operations end in period', 'date', lambda i: f"=MIN({ref('Time.end', i)},{V('Time.expiry')})", fmt='yyyy-mm-dd')
T.row('om', 'Operating months in period', 'months',
      lambda i: f"=IF({ref('Time.oe', i)}>={ref('Time.os', i)},(YEAR({ref('Time.oe', i)})-YEAR({ref('Time.os', i)}))*12+MONTH({ref('Time.oe', i)})-MONTH({ref('Time.os', i)})+1,0)",
      fmt='0', py='S.om')
T.row('opdays', 'Operating days in period', 'days',
      lambda i: f"=IF({ref('Time.oe', i)}>={ref('Time.os', i)},{ref('Time.oe', i)}-{ref('Time.os', i)}+1,0)", fmt='0', py='S.opdays')
T.row('oms', 'Operating months elapsed at period start', 'months',
      lambda i: f"=MIN(MAX((YEAR({ref('Time.start', i)})-YEAR({V('Time.cod')}))*12+MONTH({ref('Time.start', i)})-MONTH({V('Time.cod')}),0),{V('Time.ppam')})", fmt='0', py='S.oms')
T.row('ome', 'Operating months elapsed at period end', 'months', lambda i: f"={ref('Time.oms', i)}+{ref('Time.om', i)}", fmt='0', py='S.ome')
T.row('f_cod', 'Flag_CODPeriod', 'flag', lambda i: f"=IF({ref('Time.t', i)}={V('Time.tcod')},1,0)", fmt='0')
T.row('f_ds', 'Flag_DebtService (after COD period)', 'flag', lambda i: f"=IF({ref('Time.t', i)}>{V('Time.tcod')},1,0)", fmt='0')
T.row('f_ops', 'Flag_Operations', 'flag', lambda i: f"=IF({ref('Time.om', i)}>0,1,0)", fmt='0')
T.row('f_last', 'Flag_LastOperatingPeriod', 'flag',
      lambda i: f"=IF(AND({ref('Time.om', i)}>0,{ref('Time.om', i, 1)}=0),1,0)", fmt='0')
T.row('f_shock', 'Flag_ShockPeriods', 'flag', lambda i: f"=IF(AND({ref('Time.start', i)}>={V('Inputs.d_shock')},{ref('Time.start', i)}<EDATE({V('Inputs.d_shock')},{V('Inputs.shock_months')})),1,0)", fmt='0')
T.row('f_ge8', 'Flag_FromShockStart', 'flag', lambda i: f"=IF({ref('Time.start', i)}>={V('Inputs.d_shock')},1,0)", fmt='0')
T.row('f_sofr', 'Flag_TermSOFR', 'flag', lambda i: f"=IF({ref('Time.start', i)}>={V('Inputs.d_sofr')},1,0)", fmt='0')
T.row('f_ins', 'Flag_InsuranceStepUp', 'flag', lambda i: f"=IF({ref('Time.start', i)}>={V('Inputs.d_ins_step')},1,0)", fmt='0')
T.row('f_ld', 'Flag_LDPrepayment', 'flag', lambda i: f"={V('Inputs.s_ld_prep')}*IF({ref('Time.end', i)}={V('Inputs.d_ldprep')},1,0)", fmt='0')
T.row('f_t23', 'Flag_WaiverDeferral', 'flag', lambda i: f"={V('Inputs.s_waiver')}*IF({ref('Time.end', i)}={V('Inputs.d_test2')},1,0)", fmt='0')
T.row('f_up', 'Flag_MarginUplift', 'flag', lambda i: f"={V('Inputs.s_waiver')}*IF(AND({ref('Time.start', i)}>={V('Inputs.d_up1')},{ref('Time.end', i)}<={V('Inputs.d_up2')}),1,0)", fmt='0')
T.row('f_drep', 'Flag_DeferredRepayment', 'flag', lambda i: f"={V('Inputs.s_waiver')}*IF(AND({ref('Time.end', i)}>={V('Inputs.d_drep1')},{ref('Time.end', i)}<={V('Inputs.d_drep2')}),1,0)", fmt='0')
T.row('n_drep', 'Deferred repayments remaining (this and later periods)', 'count', lambda i: f"=SUM({rngrel('Time.f_drep', i, NS - 1)})", fmt='0')
T.row('f_tR', 'Flag_Refinancing', 'flag', lambda i: f"={V('Inputs.s_refi')}*IF({ref('Time.end', i)}={V('Inputs.d_refi')},1,0)", fmt='0')
T.row('f_postR', 'Flag_AfterRefinancing', 'flag', lambda i: f"={V('Inputs.s_refi')}*IF({ref('Time.end', i)}>{V('Inputs.d_refi')},1,0)", fmt='0')
T.row('f_waived', 'Flag_TestWaived', 'flag', lambda i: f"={V('Inputs.s_waiver')}*IF(AND({ref('Time.end', i)}>={V('Inputs.d_test1')},{ref('Time.end', i)}<={V('Inputs.d_test2')}),1,0)", fmt='0')
T.row('f_inw', 'Flag_WaiverRegime', 'flag', lambda i: f"={V('Inputs.s_waiver')}*IF({ref('Time.end', i)}>={V('Inputs.d_test1')},1,0)", fmt='0')
T.row('f_postw', 'Flag_AfterWaivedTests', 'flag', lambda i: f"={V('Inputs.s_waiver')}*IF({ref('Time.end', i)}>{V('Inputs.d_test2')},1,0)", fmt='0')
T.row('f_mp', 'Flag_MiniPermSweep', 'flag', lambda i: f"=IF({ref('Time.start', i)}>={V('Inputs.d_mp')},1,0)", fmt='0')
T.row('f_sc', 'Flag_SculptingPeriod (first repayment to final maturity)', 'flag', lambda i: f"=IF(AND({ref('Time.t', i)}>={V('Time.t1')},{ref('Time.end', i)}<={V('Inputs.d_maturity')}),1,0)", fmt='0')
T.row('f_rfp', 'Flag_ReforecastProjection', 'flag', lambda i: f"=IF({ref('Time.start', i)}>={V('Inputs.d_rf_cut')},1,0)", fmt='0')
T.row('f_lpi', 'Days of late-payment interest accrual to settlement', 'days', lambda i: f"=MAX(0,MIN({ref('Time.days', i)},{V('Inputs.d_settle')}-{ref('Time.start', i)}))", fmt='0')

# ========================================================================================
# OPERATIONS (macro, plant, revenue, opex, working capital, MMRA)
# ========================================================================================
O = Sheet('Operations', 'S', 'Operations: macro paths, plant, revenue, operating costs, working capital')
O.sec('Macro paths')
mac = V('Inputs.s_macro')
O.row('base0', 'Base rate before sensitivity shift', '%',
      lambda i: f"=CHOOSE({mac},{ref('Inputs.S_base_fc', i)},{ref('Inputs.S_base_act', i)},{ref('Inputs.S_base_rf', i)})")
O.row('base', 'Base rate (6M LIBOR / Term SOFR + CAS)', '%',
      lambda i: f"={ref('Operations.base0', i)}+{V('Inputs.s_rate_shift')}*{ref('Time.f_ge8', i)}", py='S.base')
def fx_raw(i):
    fc = f"{V('Inputs.on_rate')}*{V('Time.fx_d')}^(({ref('Time.t', i)}-{V('Inputs.mid')})*{ref('Time.yf30', i)})"
    proj = f"{ref('Operations.fx_raw', i, -1)}*((1+{ref('Operations.gkc', i)}/100)/(1+{ref('Operations.gus', i)}/100))^{ref('Time.yf30', i)}"
    act = f"IF({ref('Inputs.S_fx_act', i)}>0,{ref('Inputs.S_fx_act', i)},{proj})"
    rf = f"IF({ref('Time.f_rfp', i)}=0,{ref('Inputs.S_fx_act', i)},{ref('Operations.fx_raw', i, -1)}*{V('Time.fx_d')}^{ref('Time.yf30', i)})"
    return f"=CHOOSE({mac},{fc},{act},{rf})"
O.row('fx_raw', 'KCR per USD before devaluation sensitivity', 'KCR/USD', fx_raw)
O.row('fx', 'KCR per USD, period average', 'KCR/USD',
      lambda i: f"={ref('Operations.fx_raw', i)}/(1-{V('Inputs.s_deval')}*{ref('Time.f_ge8', i)})", py='S.fx')
def ann(tbl_key, yexpr):
    return f"INDEX({rng('Inputs.A_' + tbl_key, 0, len(YEARS) - 1)},1,MATCH({yexpr},{rng('Inputs.A_yr', 0, len(YEARS) - 1)},0))"
def g_of(cur, i, lag):
    y = f"({ref('Time.year', i)}-{lag})"
    return f"=CHOOSE({mac},{ann(cur + '_fc', y)},{ann(cur + '_act', y)},{ann(cur + '_rf', y)})"
O.row('gus', 'US CPI change, current year', '%', lambda i: g_of('us', i, 0))
O.row('gkc', 'Kessara CPI change, current year', '%', lambda i: g_of('kc', i, 0))
O.row('gus1', 'US CPI change, prior year', '%', lambda i: g_of('us', i, 1))
O.row('gkc1', 'Kessara CPI change, prior year', '%', lambda i: g_of('kc', i, 1))
def gy(cur, yexpr):
    return f"(1+CHOOSE({mac},{ann(cur + '_fc', yexpr)},{ann(cur + '_act', yexpr)},{ann(cur + '_rf', yexpr)})/100)"
def idx_closed(cur, mo_key):
    by = V('Inputs.idx_by'); y1 = f"YEAR({V('Inputs.d_s1')})"
    return (f"{V('Inputs.idx_100')}*{gy(cur, by)}^((12-{V('Inputs.idx_bm')})/12)*{gy(cur, by + '+1')}"
            f"*{gy(cur, y1)}^({V('Inputs.' + mo_key)}/12)")
for cur in ('us', 'kc'):
    O.scalar(cur + '_b18', f"{cur.upper()} index, 2018 price base month", 'index', "=" + idx_closed(cur, 'rd_b18'), '0.0000')
    O.scalar(cur + '_c1', f"{cur.upper()} index, first cost reading", 'index', "=" + idx_closed(cur, 'rd_cost1'), '0.0000')
    O.scalar(cur + '_t1', f"{cur.upper()} index, first tariff reading", 'index', "=" + idx_closed(cur, 'rd_tar1'), '0.0000')
    O.row(cur + '_cost', f"{'US' if cur == 'us' else 'Kessara'} CPI index, cost reading (Mar/Sep), Nov 2016 = 100", 'index',
          (lambda cur: lambda i: f"=IF({ref('Time.t', i)}=1,{V('Operations.' + cur + '_c1')},{ref('Operations.' + cur + '_cost', i, -1)}*IF({ref('Time.half', i)}=1,(1+{ref('Operations.g' + cur + '1', i)}/100)^({V('Inputs.rd_lag')}/12)*(1+{ref('Operations.g' + cur, i)}/100)^(({ref('Time.mper', i)}-{V('Inputs.rd_lag')})/12),(1+{ref('Operations.g' + cur, i)}/100)^{ref('Time.yf30', i)}))")(cur))
    O.row(cur + '_tar', f"{'US' if cur == 'us' else 'Kessara'} CPI index, tariff reading (3-month lag)", 'index',
          (lambda cur: lambda i: (f"={ref('Operations.' + cur + '_cost', i)}*(1+{ref('Operations.g' + cur, i)}/100)^({V('Inputs.rd_lag')}/12)" if 'E3' in ERR else
                                  f"=IF({ref('Time.t', i)}=1,{V('Operations.' + cur + '_t1')},{ref('Operations.' + cur + '_cost', i, -1)})"))(cur),
          py='S.' + cur + '_tar')
    O.row(cur + '_cf', f"{'US' if cur == 'us' else 'Kessara'} cost indexation factor vs 2018 prices", 'factor',
          (lambda cur: lambda i: f"={ref('Operations.' + cur + '_cost', i)}/{V('Operations.' + cur + '_b18')}")(cur), py='S.' + cur + '_cf')
O.sec('Plant')
O.row('oya', 'Operating year at period start', 'OY', lambda i: f"=INT({ref('Time.oms', i)}/12)+1", fmt='0')
O.row('ma', 'Months in that operating year', 'months', lambda i: f"=MIN({ref('Time.ome', i)},{ref('Operations.oya', i)}*12)-{ref('Time.oms', i)}", fmt='0')
av8 = rng('Inputs.S_av8', 0, 7)
O.row('avail_prof', 'Availability, profile (month-weighted; plus the Monte Carlo shock for the operating year when active)', '%',
      lambda i: (f"=IF({ref('Time.om', i)}>0,({ref('Operations.ma', i)}*INDEX({av8},1,MOD({ref('Operations.oya', i)}-1,{V('Inputs.av_cycle')})+1)+({ref('Time.om', i)}-{ref('Operations.ma', i)})*INDEX({av8},1,MOD({ref('Operations.oya', i)},{V('Inputs.av_cycle')})+1))/{ref('Time.om', i)}"
                 f"+IF({MCON()}=1,({ref('Operations.ma', i)}*INDEX({MC_SHK},{MCRUN()},{ref('Operations.oya', i)})+({ref('Time.om', i)}-{ref('Operations.ma', i)})"
                 f"*IF({ref('Operations.oya', i)}+1<={V('Inputs.mc_ny')},INDEX({MC_SHK},{MCRUN()},{ref('Operations.oya', i)}+1),0))/{ref('Time.om', i)},0),0)"),
      py='S.avail_prof')
O.row('avail', 'Availability', '%', lambda i: f"=IF({ref('Time.om', i)}>0,{ref('Operations.avail_prof', i)}+{V('Inputs.s_avail_d')},0)", py='S.avail')
O.row('yrs', 'Years since COD (period mid-point)', 'years', lambda i: f"=IF({ref('Time.om', i)}>0,AVERAGE({ref('Time.oms', i)},{ref('Time.ome', i)})/12,0)", py='S.yrs')
O.scalar('C', 'Contracted capacity', 'MW', f"=IF({V('Inputs.s_constr')}<>1,{V('Inputs.C_act')},{V('Inputs.C_fc')})", '0.0')
O.scalar('HRg', 'Plant net heat rate, new and clean', 'kJ/kWh', f"=IF({V('Inputs.s_constr')}<>1,{V('Inputs.HR_t')},{V('Inputs.HR_g')})", '0')
O.row('of', 'Output degradation factor', 'factor',
      lambda i: f"=(1-{V('Inputs.o_nr')}/100*{ref('Operations.yrs', i)})*(1-{V('Inputs.o_rec')}/100)", py='S.out_factor')
O.row('disp', 'Dispatch factor when available', '%',
      lambda i: f"=IF({MCON()}=1,INDEX({MC_DISP},{MCRUN()}),IF(AND({V('Inputs.s_disp_path')}=1,{ref('Inputs.S_disp_act', i)}>0),{ref('Inputs.S_disp_act', i)},{V('Inputs.s_dispatch')}))", py='S.dispatch')
O.row('energy', 'Net energy delivered', 'MWh',
      lambda i: f"={V('Operations.C')}*{V('Inputs.hrs_m')}*{ref('Time.om', i)}*{ref('Operations.avail', i)}/100*{ref('Operations.disp', i)}/100*{ref('Operations.of', i)}",
      fmt='#,##0', py='S.energy')
O.row('hr_act', 'Plant net heat rate', 'kJ/kWh',
      lambda i: f"={V('Operations.HRg')}*(1+IF({MCON()}=1,INDEX({MC_HNR},{MCRUN()}),{V('Inputs.h_nr')})/100*{ref('Operations.yrs', i)})*(1+{V('Inputs.h_rec')}/100)*(1+{V('Inputs.pl')}/100)*{V('Inputs.s_hr_f')}", py='S.hr_act')
O.row('hr_con', 'Contracted heat rate at dispatched load', 'kJ/kWh',
      lambda i: f"={V('Inputs.HR_c')}*(1+{V('Inputs.HR_cdeg')}/100*{ref('Operations.yrs', i)})*(1+{V('Inputs.pl')}/100)", py='S.hr_con')
KG = f"(1000*{V('Inputs.hhv')}/{V('Inputs.kj')})"
O.row('gas_p', 'Gas price (GCV)', 'USD/MMBtu',
      lambda i: f"={V('Inputs.gas_p')}*(1+{V('Inputs.gas_esc')}/100)^({ref('Time.year', i)}-{V('Inputs.price_yr')})*{V('Inputs.s_gas_f')}", py='S.gas_price')
O.row('gas', 'Gas burned', 'MMBtu', lambda i: f"={ref('Operations.energy', i)}*{ref('Operations.hr_act', i)}*{KG}", fmt='#,##0', py='S.gas_mmbtu')
O.row('top_vol', 'Take-or-pay quantity', 'MMBtu', lambda i: f"={V('Inputs.top')}*{V('Inputs.dcq')}*{ref('Time.opdays', i)}", fmt='#,##0', py='S.top_vol')
O.sec('Revenue (USD m)')
O.row('cap_chg', 'Capital charge, indexed', 'USD/kW-month',
      lambda i: f"={V('Inputs.cap_chg')}*{V('Inputs.s_capf')}*(1-{V('Inputs.cap_idx')}+{V('Inputs.cap_idx')}*{ref('Operations.us_tar', i)}/100)", py='S.cap_charge')
O.row('fom_chg', 'Fixed O&M charge, indexed', 'USD/kW-month',
      lambda i: f"={V('Inputs.fom_chg')}*({V('Inputs.fom_us')}*{ref('Operations.us_tar', i)}/100+(1-{V('Inputs.fom_us')})*{ref('Operations.kc_tar', i)}/100*{V('Inputs.bid_fx')}/{ref('Operations.fx', i)})", py='S.fom_charge')
O.row('avf', 'Availability factor min(1, A/90%)', 'factor', lambda i: (f"={ref('Operations.avail', i)}/{V('Inputs.a_target')}" if 'E1' in ERR else f"=MIN(1,{ref('Operations.avail', i)}/{V('Inputs.a_target')})"), py='S.avail_factor')
O.row('cap_pay', 'Capacity payment', 'USD m',
      lambda i: f"={V('Operations.C')}*1000*{ref('Time.om', i)}*({ref('Operations.cap_chg', i)}+{ref('Operations.fom_chg', i)})*{ref('Operations.avf', i)}/1000000", total=True, py='S.cap_pay')
O.row('vom_rate', 'VOM charge, indexed', 'USD/MWh',
      lambda i: f"={V('Inputs.vom_chg')}*({V('Inputs.vom_us')}*{ref('Operations.us_tar', i)}/100+(1-{V('Inputs.vom_us')})*{ref('Operations.kc_tar', i)}/100*{V('Inputs.bid_fx')}/{ref('Operations.fx', i)})", py='S.vom_rate')
O.row('vom', 'Variable O&M payment', 'USD m', lambda i: f"={ref('Operations.energy', i)}*{ref('Operations.vom_rate', i)}/1000000", total=True, py='S.vom')
O.row('fuel_rev', 'Fuel charge (pass-through)', 'USD m',
      lambda i: f"={ref('Operations.energy', i)}*{ref('Operations.hr_con', i)}*{KG}*{ref('Operations.gas_p', i)}/1000000" + (f"*0.765/({V('Inputs.s_dispatch')}/100)" if 'E9' in ERR else ''), total=True, py='S.fuel_rev')
O.row('gta_res', 'GTA reservation charge (pass-through)', 'USD m',
      lambda i: f"={V('Inputs.gta_cap')}*{ref('Time.opdays', i)}*{V('Inputs.gta_r')}*(1+{V('Inputs.gta_esc')}/100)^({ref('Time.year', i)}-{V('Inputs.price_yr')})/1000000", total=True, py='S.gta_res')
O.row('gta_com', 'GTA commodity charge (pass-through)', 'USD m',
      lambda i: f"={ref('Operations.gas', i)}*{V('Inputs.gta_c')}*(1+{V('Inputs.gta_esc')}/100)^({ref('Time.year', i)}-{V('Inputs.price_yr')})/1000000", total=True, py='S.gta_com')
O.row('top_pay', 'Take-or-pay payment (pass-through)', 'USD m',
      lambda i: f"=MAX(0,{ref('Operations.top_vol', i)}-{ref('Operations.gas', i)})*{ref('Operations.gas_p', i)}/1000000", total=True, py='S.top_pay')
O.row('nonfuel', 'Non-fuel revenue', 'USD m', lambda i: f"={ref('Operations.cap_pay', i)}+{ref('Operations.vom', i)}", total=True, py='S.nonfuel_rev')
O.row('rev', 'Total revenue', 'USD m',
      lambda i: f"={ref('Operations.nonfuel', i)}+{ref('Operations.fuel_rev', i)}+{ref('Operations.gta_res', i)}+{ref('Operations.gta_com', i)}+{ref('Operations.top_pay', i)}", total=True, py='S.revenue')
O.row('lpi_acc', 'Late payment interest accrued (to settlement 2024-03-21)', 'USD m',
      lambda i: (f"=IF({V('Inputs.s_crisis')}=1,AVERAGE({ref('Operations.over', i, -1)},{ref('Operations.over', i)})*({ref('Operations.base', i)}-{ref('Time.f_sofr', i)}*{V('Inputs.cas')}+{V('Inputs.lpi_sp')})/100"
                 f"*{ref('Time.f_lpi', i)}/{V('Inputs.day_usd')},0)"), total=True, py='S.lpi_accrued')
O.row('lpi', 'Late payment interest received (60%, with settlement installments)', 'USD m',
      lambda i: f"={V('Inputs.lpi_paid')}*SUM({rng('Operations.lpi_acc')})*{ref('Inputs.S_lpi_sh', i)}", total=True, py='S.lpi_received')
O.sec('Operating costs (USD m)')
fo = V('Inputs.s_fo_f'); mf = lambda i: f"{ref('Time.om', i)}/12"
O.row('om_fix', 'O&M fixed fee', 'USD m',
      lambda i: f"={V('Inputs.om_fee')}*({V('Inputs.om_usd')}*{ref('Operations.us_cf', i)}+(1-{V('Inputs.om_usd')})*{ref('Operations.kc_cf', i)}*{V('Inputs.fx18')}/{ref('Operations.fx', i)})*{mf(i)}*{fo}", total=True, py='S.om_fixed')
O.row('om_inc', 'O&M availability incentive', 'USD m',
      lambda i: f"=IF({ref('Time.om', i)}>0,{V('Inputs.om_inc')}*MAX(-1,MIN(1,({ref('Operations.avail', i)}-{V('Inputs.om_pivot')})/{V('Inputs.om_band')}))*{ref('Operations.us_cf', i)}*{mf(i)},0)", total=True, py='S.om_incentive')
O.row('ltsa_fix', 'LTSA fixed fee', 'USD m', lambda i: f"={V('Inputs.ltsa_fix')}*{ref('Operations.us_cf', i)}*{mf(i)}*{fo}", total=True, py='S.ltsa_fixed')
O.row('eoh', 'Equivalent operating hours (2 GTs)', 'EOH',
      lambda i: f"=IF({ref('Operations.avail_prof', i)}>0,{'1' if 'E2' in ERR else V('Inputs.n_gt')}*({V('Inputs.gt_hours')}*{ref('Operations.avail', i)}/{ref('Operations.avail_prof', i)}*{ref('Operations.disp', i)}/{V('Inputs.disp_base')}+{V('Inputs.gt_starts')}*{V('Inputs.eoh_start')})*{mf(i)},0)", fmt='#,##0', py='S.eoh')
O.row('ltsa_var', 'LTSA variable fee', 'USD m', lambda i: f"={ref('Operations.eoh', i)}*{V('Inputs.ltsa_var')}*{ref('Operations.us_cf', i)}/1000000", total=True, py='S.ltsa_var')
O.row('insur', 'Operational insurance', 'USD m',
      lambda i: f"={V('Inputs.ins_o')}*{ref('Operations.us_cf', i)}*{mf(i)}*(1+{V('Inputs.ins_step')}*{V('Inputs.s_ins_step')}*{ref('Time.f_ins', i)})*{fo}", total=True, py='S.insurance')
O.row('ga', 'G&A', 'USD m',
      lambda i: f"={V('Inputs.ga')}*({V('Inputs.ga_us')}*{ref('Operations.us_cf', i)}+(1-{V('Inputs.ga_us')})*{ref('Operations.kc_cf', i)}*{V('Inputs.fx18')}/{ref('Operations.fx', i)})*{mf(i)}*{fo}", total=True, py='S.ga')
O.row('land', 'Land lease and permits', 'USD m', lambda i: f"={V('Inputs.land')}*{ref('Operations.kc_cf', i)}/{ref('Operations.fx', i)}*{mf(i)}*{fo}", total=True, py='S.land')
O.row('comm', 'Community fund and OREK levy', 'USD m', lambda i: f"={V('Inputs.comm')}/100*{ref('Operations.nonfuel', i)}", total=True, py='S.community_levy')
O.row('consum', 'Variable consumables', 'USD m',
      lambda i: f"={V('Inputs.consum')}*({V('Inputs.cons_us')}*{ref('Operations.us_cf', i)}+(1-{V('Inputs.cons_us')})*{ref('Operations.kc_cf', i)}*{V('Inputs.fx18')}/{ref('Operations.fx', i)})*{ref('Operations.energy', i)}/1000000", total=True, py='S.consumables')
O.row('agency', 'Agency and account fees', 'USD m', lambda i: f"={V('Inputs.agency')}*{mf(i)}", total=True, py='S.agency')
O.row('prg', 'ABDB PRG fee', 'USD m', lambda i: f"={V('Inputs.prg')}*{mf(i)}", total=True, py='S.prg_fee')
O.row('opex_om', 'Operating costs before pass-through items', 'USD m',
      lambda i: "=" + "+".join(ref('Operations.' + k, i) for k in ['om_fix', 'om_inc', 'ltsa_fix', 'ltsa_var', 'insur', 'ga', 'land', 'comm', 'consum', 'agency', 'prg']), total=True, py='S.opex_om')
O.row('fuel_cost', 'Gas purchases', 'USD m', lambda i: f"={ref('Operations.gas', i)}*{ref('Operations.gas_p', i)}/1000000", total=True, py='S.fuel_cost')
O.row('pass', 'Pass-through costs (gas, GTA, take-or-pay)', 'USD m',
      lambda i: f"={ref('Operations.fuel_cost', i)}+{ref('Operations.gta_res', i)}+{ref('Operations.gta_com', i)}+{ref('Operations.top_pay', i)}", total=True, py='S.pass_cost')
O.row('vat_ops', 'VAT facility interest after the funding period', 'USD m',
      lambda i: f"=SUMIFS({rng('Construction.vat_int')},{rng('Construction.per')},{ref('Time.t', i)},{rng('Construction.m')},\">\"&{V('Time.fe')})", total=True, py='S.vat_int_ops')
O.row('fxl', 'FX conversion losses', 'USD m', lambda i: f"={V('Inputs.s_crisis')}*{ref('Inputs.S_fxloss', i)}", total=True, py='S.fx_loss')
O.row('mmk', 'OY whose maintenance month could fall in the period', 'OY', lambda i: f"=INT(({ref('Time.ome', i)}-{V('Inputs.mm_month')})/12)+1", fmt='0')
O.row('mm18', 'Major maintenance outside LTSA (2018 prices)', 'USD m',
      lambda i: (f"=IF(AND({ref('Time.om', i)}>0,{ref('Operations.mmk', i)}>=1,{ref('Operations.mmk', i)}<={V('Inputs.mm_last')},{ref('Time.oms', i)}<({ref('Operations.mmk', i)}-1)*12+{V('Inputs.mm_month')},({ref('Operations.mmk', i)}-1)*12+{V('Inputs.mm_month')}<={ref('Time.ome', i)}),"
                 f"IF(MOD({ref('Operations.mmk', i)},{V('Inputs.mm_maj_c')})=0,{V('Inputs.mm_maj')},IF(MOD({ref('Operations.mmk', i)},{V('Inputs.mm_min_c')})=0,{V('Inputs.mm_min')},0)),0)"), py='S.mm_2018')
O.row('mm', 'Major maintenance spend', 'USD m', lambda i: f"={ref('Operations.mm18', i)}*{ref('Operations.us_cf', i)}", total=True, py='S.mm_spend')
O.row('hb_m', 'Months in period from the handback reserve year', 'months', lambda i: f"=MAX(0,MIN({ref('Time.ome', i)},{V('Time.ppam')})-MAX({ref('Time.oms', i)},({V('Inputs.hb_oy')}-1)*12))", fmt='0')
O.row('hb_req', 'Handback reserve contribution required', 'USD m', lambda i: f"={V('Inputs.hb')}*{ref('Operations.us_cf', i)}*{ref('Operations.hb_m', i)}/12", total=True, py='S.hb_contr_req')
O.row('hb_works', 'Handback works at PPA expiry', 'USD m', lambda i: f"={ref('Time.f_last', i)}*SUM({rng('Operations.hb_req')})", total=True, py='S.hb_works')
O.row('opex', 'Total operating costs', 'USD m',
      lambda i: "=" + "+".join(ref('Operations.' + k, i) for k in ['opex_om', 'pass', 'vat_ops', 'fxl', 'mm', 'hb_works']), total=True, py='S.opex')
O.row('ebitda', 'EBITDA', 'USD m', lambda i: f"={ref('Operations.rev', i)}-{ref('Operations.opex', i)}+{ref('Operations.lpi', i)}", total=True, py='S.ebitda')
O.sec('Working capital (USD m, period-end balances)')
od = lambda i: f"MAX({ref('Time.opdays', i)},1)"
nf = lambda i: f"(1-{ref('Operations.fin', i)})"
O.row('fin', 'Flag: final operating period or later (working capital unwinds)', 'flag',
      lambda i: f"=IF({ref('Time.t', i)}>={V('Time.lastop')},1,0)", fmt='0')
O.row('xdays', 'Extra receivable days on capacity and VOM (sensitivities)', 'days', lambda i: f"={V('Inputs.s_xdays')}*{ref('Time.f_shock', i)}", fmt='0')
O.row('ar', 'Trade receivables (normal terms)', 'USD m',
      lambda i: f"={nf(i)}*({ref('Operations.rev', i)}/{od(i)}*{V('Inputs.rec_d')}+{ref('Operations.nonfuel', i)}/{od(i)}*{ref('Operations.xdays', i)})", py='S.ar')
O.row('over', 'SEKA overdue receivables', 'USD m', lambda i: f"={V('Inputs.s_crisis')}*{ref('Inputs.S_overdue', i)}", py='S.overdue')
O.row('pay_gas', 'Gas payables', 'USD m', lambda i: f"={nf(i)}*({ref('Operations.fuel_cost', i)}+{ref('Operations.top_pay', i)})/{od(i)}*{V('Inputs.gas_d')}", py='S.pay_gas')
O.row('pay_gta', 'GTA payables', 'USD m', lambda i: f"={nf(i)}*({ref('Operations.gta_res', i)}+{ref('Operations.gta_com', i)})/{od(i)}*{V('Inputs.gta_d')}", py='S.pay_gta')
O.row('pay_om', 'O&M and LTSA payables', 'USD m',
      lambda i: f"={nf(i)}*({ref('Operations.om_fix', i)}+{ref('Operations.om_inc', i)}+{ref('Operations.ltsa_fix', i)}+{ref('Operations.ltsa_var', i)})/{od(i)}*{V('Inputs.om_d')}", py='S.pay_om')
O.row('pay_oth', 'Other payables', 'USD m',
      lambda i: f"={nf(i)}*(" + "+".join(ref('Operations.' + k, i) for k in ['insur', 'ga', 'land', 'comm', 'consum', 'agency', 'prg']) + f")/{od(i)}*{V('Inputs.oth_d')}", py='S.pay_oth')
O.row('gas_arr', 'Deferred SNHK/GCK payables matching SEKA energy-charge arrears', 'USD m',
      lambda i: f"={V('Inputs.gas_arr')}*{ref('Operations.over', i)}", py='S.gas_arrears')
O.row('nwc', 'Net working capital (excl. spares inventory)', 'USD m',
      lambda i: f"={ref('Operations.ar', i)}+{ref('Operations.over', i)}-{ref('Operations.pay_gas', i)}-{ref('Operations.pay_gta', i)}-{ref('Operations.pay_om', i)}-{ref('Operations.pay_oth', i)}-{ref('Operations.gas_arr', i)}", py='S.nwc')
O.row('dnwc', 'Increase in net working capital', 'USD m', lambda i: f"={ref('Operations.nwc', i)}-{ref('Operations.nwc', i, -1)}", total=True, py='S.dnwc')
O.row('inv_rel', 'Release of spares inventory at expiry', 'USD m', lambda i: f"={ref('Time.f_last', i)}*{V('Inputs.init_wc')}*{V('Inputs.s_capex')}", total=True, py='S.inv_release')
# v1.4 appended pass-through tests (u09 R10)
O.row('pt_fuel', 'Fuel pass-through test: fuel charge less gas purchases (= heat-rate headroom margin)', 'USD m',
      lambda i: f"={ref('Operations.fuel_rev', i)}-{ref('Operations.fuel_cost', i)}", total=True, py='S.pt_fuel')
O.row('pt_gta', 'GTA pass-through test (0 in every period)', 'USD m',
      lambda i: f"={ref('Operations.gta_res', i)}+{ref('Operations.gta_com', i)}-({ref('Operations.pass', i)}-{ref('Operations.fuel_cost', i)}-{ref('Operations.top_pay', i)})", total=True, py='S.pt_gta')

# ========================================================================================
# CONSTRUCTION (monthly uses)
# ========================================================================================
CS = Sheet('Construction', 'M', 'Construction: monthly uses of funds before financing costs, VAT')
CS.sec('Monthly timeline (column J = August 2018)')
CS.row('m', 'Month number', 'index', lambda i: f"={ref('Construction.m', i, -1)}+1", fmt='0')
CS.row('start', 'Month start', 'date', lambda i: f"=IF({ref('Construction.m', i)}=1,{V('Inputs.d_ntp')},EDATE({ref('Construction.start', i, -1)},1))", fmt='yyyy-mm-dd')
CS.row('end', 'Month end', 'date', lambda i: f"=EOMONTH({ref('Construction.start', i)},0)", fmt='yyyy-mm-dd')
CS.row('days', 'Days', 'days', lambda i: f"={ref('Construction.end', i)}-{ref('Construction.start', i)}+1", fmt='0')
CS.row('per', 'Semiannual period number', 'index', lambda i: f"=MATCH({ref('Construction.start', i)},{rng('Time.start')},1)", fmt='0')
CS.row('f_con', 'Flag_Construction (before COD)', 'flag', lambda i: f"=IF({ref('Construction.m', i)}<={V('Time.nc')},1,0)", fmt='0')
CS.row('f_fund', 'Flag_FundingPeriod (to end of COD period)', 'flag', lambda i: f"=IF({ref('Construction.m', i)}<={V('Time.fe')},1,0)", fmt='0')
CS.row('f_codm', 'Flag_CODMonth', 'flag', lambda i: f"=IF({ref('Construction.m', i)}={V('Time.nc')}+1,1,0)", fmt='0')
CS.row('fx', 'KCR per USD', 'KCR/USD',
      lambda i: f"=IF({mac}=1,{V('Inputs.on_rate')}*{V('Time.fx_d')}^(({ref('Construction.m', i)}-{V('Inputs.mid')})/12),INDEX({rng('Operations.fx')},1,{ref('Construction.per', i)}))")
CS.row('base', 'Base rate (6M fixing for the half-year)', '%', lambda i: f"=INDEX({rng('Operations.base0')},1,{ref('Construction.per', i)})")
CS.row('pol', 'Kessara policy rate', '%', lambda i: f"=IF({mac}=1,{V('Inputs.fc_policy')},{ann('pol_act', 'YEAR(' + ref('Construction.start', i) + ')')})")
CS.sec('Uses before financing costs (USD m)')
cx = V('Inputs.s_capex'); nc = V('Time.nc'); m_ = lambda i: ref('Construction.m', i)
CS.row('pct', 'EPC payment profile, selected', '%',
      lambda i: f"=IF({V('Inputs.s_constr')}<>1,{ref('Inputs.M_epc_act', i)},{ref('Inputs.M_epc_fc', i)}+IF({V('Inputs.s_cod_delay')}>0,IF({m_(i)}={V('Inputs.epc_fc_m')},-{V('Inputs.to_pct')},0)+IF({m_(i)}={V('Inputs.epc_fc_m')}+{V('Inputs.s_cod_delay')},{V('Inputs.to_pct')},0),0))")
CS.row('prog', 'EPC progress payments for contingency (FC)', '%',
      lambda i: f"=IF({m_(i)}=1,0,{ref('Construction.pct', i)})-IF({m_(i)}={nc},{V('Inputs.to_pct')},0)")
CS.row('epc', 'EPC payments', 'USD m',
      lambda i: f"=IF({V('Inputs.s_constr')}<>1,{ref('Construction.pct', i)}/100*{V('Inputs.epc_off')}+{ref('Construction.pct', i)}/100*{V('Inputs.epc_on')}*{V('Inputs.on_rate')}/{ref('Construction.fx', i)},{V('Inputs.epc_price')}*{cx}*{ref('Construction.pct', i)}/100)",
      total=True, py='u.epc')
CS.row('owners', "Owner's costs", 'USD m',
      lambda i: (f"={V('Inputs.owners')}*IF({V('Inputs.s_constr')}=1,{cx},1)*({ref('Inputs.M_own_fc', i)}+IF(AND({V('Inputs.s_constr')}=1,{m_(i)}>{V('Inputs.epc_fc_m')},{m_(i)}<={nc}),{V('Inputs.own_ext')},0))/100"
                 f"+IF(AND({V('Inputs.s_constr')}<>1,{m_(i)}>={V('Inputs.ext1')},{m_(i)}<={V('Inputs.ext2')}),{V('Inputs.ext_own')}/({V('Inputs.ext2')}-{V('Inputs.ext1')}+1),0)"), total=True, py='u.owners')
CS.row('ins', 'Insurance during construction', 'USD m',
      lambda i: f"={V('Inputs.ins_c')}*{cx}*({V('Inputs.ins_sh1')}*IF({m_(i)}=1,1,0)+(1-{V('Inputs.ins_sh1')})*IF({m_(i)}={V('Inputs.ins_m2')},1,0))", total=True, py='u.insurance')
CS.row('dev', 'Development costs and fee', 'USD m', lambda i: f"=IF({m_(i)}=1,{V('Inputs.dev_c')}+{V('Inputs.dev_fee')},0)", total=True, py='u.dev')
CS.row('adv', "Lenders' advisors and legal", 'USD m',
      lambda i: f"={V('Inputs.adv')}*{cx}*({V('Inputs.adv_sh1')}*IF({m_(i)}=1,1,0)+(1-{V('Inputs.adv_sh1')})/({nc}-1)*IF(AND({m_(i)}>1,{m_(i)}<={nc}),1,0))", total=True, py='u.advisors')
CS.row('cont', 'Contingency (FC: pro rata with EPC progress payments)', 'USD m',
      lambda i: f"=IF({V('Inputs.s_constr')}=1,{V('Inputs.cont')}*{cx}*{ref('Construction.prog', i)}/SUM({rng('Construction.prog')}),0)", total=True, py='u.contingency')
CS.row('wc', 'Initial working capital', 'USD m', lambda i: f"=IF({m_(i)}={nc},{V('Inputs.init_wc')}*{cx},0)", total=True, py='u.wc')
CS.row('ovr', 'Overrun items (actual)', 'USD m', lambda i: f"=IF({V('Inputs.s_constr')}<>1,{ref('Inputs.M_ovr', i)},0)", total=True, py='u.overrun')
CS.row('fwd', 'KCR forward rate traded at financial close (covered interest parity)', 'KCR/USD',
      lambda i: f"={V('Inputs.on_rate')}*((1+{V('Inputs.fc_policy')}/100)/(1+INDEX({rng('Inputs.S_base_fc')},1,{ref('Construction.per', i)})/100))^(({ref('Construction.end', i)}-{V('Inputs.d_fc')})/{V('Inputs.day_kcr')})", py='u.fx_fwd')
CS.row('fxh', 'FX forward settlement on onshore EPC payments (gain to the project)', 'USD m',
      lambda i: f"=IF({V('Inputs.s_constr')}<>1,{V('Inputs.fxh_share')}*{ref('Construction.on_kcr', i)}*(1/{ref('Construction.fx', i)}-1/{ref('Construction.fwd', i)}),0)", total=True, py='u.fx_hedge')
CS.row('base_total', 'Uses before financing costs (net of FX hedge settlements)', 'USD m',
      lambda i: "=" + "+".join(ref('Construction.' + k, i) for k in ['epc', 'owners', 'ins', 'dev', 'adv', 'cont', 'wc', 'ovr']) + f"-{ref('Construction.fxh', i)}", total=True, py='u.base_total')
CS.sec('VAT on onshore EPC (KCR m) and UBK VAT facility')
CS.row('on_kcr', 'Onshore EPC payments', 'KCR m', lambda i: f"={ref('Construction.pct', i)}/100*{V('Inputs.epc_on')}*{V('Inputs.on_rate')}*{cx}", total=True, py='u.onshore_kcr')
CS.row('vat', 'VAT paid (drawn on the VAT facility)', 'KCR m', lambda i: f"={V('Inputs.vat_rate')}/100*{ref('Construction.on_kcr', i)}", total=True, py='u.vat_kcr')
CS.row('vat_ref', 'VAT refunds (9-month lag) repaying the facility', 'KCR m',
      lambda i: f"=SUMIFS({rng('Construction.vat')},{rng('Construction.m')},{m_(i)}-{V('Inputs.vat_lag')})", total=True, py='u.vat_refund_kcr')
CS.row('vat_bal', 'VAT facility balance', 'KCR m', lambda i: f"={ref('Construction.vat_bal', i, -1)}+{ref('Construction.vat', i)}-{ref('Construction.vat_ref', i)}", py='u.vat_bal_kcr')
CS.row('vat_int', 'VAT facility interest', 'USD m',
      lambda i: f"={ref('Construction.vat_bal', i, -1)}*({ref('Construction.pol', i)}+{V('Inputs.vat_spread')})/100*{ref('Construction.days', i)}/{V('Inputs.day_kcr')}/{ref('Construction.fx', i)}", total=True, py='u.vat_int')

# ========================================================================================
# FUNDING (monthly)
# ========================================================================================
F = Sheet('Funding', 'M', 'Funding: closed-form gross-up, drawdowns by tranche, IDC, fees, equity')
TRK = [('E', 'ECA-covered tranche'), ('A', 'ABDB A-loan'), ('B', 'ABDB B-loan'), ('C', 'Commercial tranche')]
F.sec('Constants')
F.scalar('gc', 'Contract debt share of funding g = D/(D+E)', 'fraction', f"={V('Inputs.D_c')}/({V('Inputs.D_c')}+{V('Inputs.E_c')})", '0.000000')
F.scalar('gaff', 'Gearing used in the closed-form gross-up', 'fraction', f"=IF({V('Inputs.s_mode')}<>1,{V('Funding.gc')},{V('Inputs.gear')})", '0.000000')
F.scalar('den', 'ECA premium gross-up denominator 1 - prem x share x g', 'factor', f"=1-{V('Inputs.eca_prem')}/100*{V('Inputs.sh_E')}*{V('Funding.gaff')}", '0.000000')
gu = {'E': '1', 'A': '1', 'B': '1', 'C': f"(1/(1-{V('Inputs.wht')}/100))"}
cfk = {'E': V('Inputs.cf_E'), 'A': V('Inputs.cf_A'), 'B': V('Inputs.cf_B'), 'C': f"({V('Inputs.cf_Cpct')}/100*{V('Inputs.m_C1')})"}
ufk = {k: V('Inputs.uf_' + k) for k in 'EABC'}
mk = {'E': V('Inputs.m_E'), 'A': V('Inputs.m_A'), 'B': V('Inputs.m_B'), 'C': V('Inputs.m_C1')}
shk = {k: V('Inputs.sh_' + k) for k in 'EABC'}
PRIR = f"({V('Inputs.pri_rate')}/100*{V('Inputs.pri_cover')}/100)"
# DSRA coefficients from the first debt service period (semiannual sheet references)
t1i = V('Time.t1')
def at_t1(key): return f"INDEX({rng(key)},1,{t1i})"
F.scalar('pshare1', 'First installment share of remaining profile (A, B, commercial, standby)', 'fraction', lambda: f"={at_t1('Debt.prof')}/{at_t1('Debt.rem')}", '0.000000')
for k, _ in TRK:
    extra = f"+{PRIR}*{at_t1('Time.days')}/{V('Inputs.day_kcr')}" if k == 'C' else ''
    F.scalar('d1_' + k, f'DSRA coefficient per USD of {k} balance', 'factor',
             lambda k=k, extra=extra: f"={at_t1('Debt.pshe') if k == 'E' else V('Funding.pshare1')}+({at_t1('Operations.base')}+{mk[k] if k != 'C' else at_t1('Debt.mC')})/100*{'0.5' if 'E4' in ERR else at_t1('Time.days') + '/' + V('Inputs.day_usd')}*{gu[k]}{extra}", '0.000000')
F.scalar('d1_SB', 'DSRA coefficient per USD of standby balance', 'factor', lambda: f"={V('Funding.pshare1')}+{at_t1('Debt.r_SB')}", '0.000000')
F.scalar('d0', 'DSRA constant (swap net payment)', 'USD m',
         lambda: f"={SG()}{at_t1('Inputs.S_N_s')}*({V('Inputs.swap_fix')}/100*{at_t1('Time.yf30')}-{at_t1('Operations.base')}/100*{at_t1('Time.days')}/{V('Inputs.day_usd')})", '0.000000')
F.sec('Closed-form gross-up: debt balance = alpha + beta x T (FC-type cases)')
fl = lambda i: ref('Construction.f_fund', i)
dcf = lambda i: f"{ref('Construction.days', i)}/{V('Inputs.day_usd')}"
dcfL = lambda i: '(1/12)' if 'E4' in ERR else dcf(i)
F.row('rr', 'Blended loan rate per month (rho)', 'factor',
      lambda i: "=" + "+".join(f"{shk[k]}*({ref('Construction.base', i)}+{mk[k]})/100*{dcfL(i)}*{gu[k]}" for k in 'EABC') + f"+{shk['C']}*{PRIR}*{ref('Construction.days', i)}/{V('Inputs.day_kcr')}", fmt='0.0000000')
F.row('kk', 'Blended commitment fee per month (kappa)', 'factor',
      lambda i: "=" + "+".join(f"{shk[k]}*{cfk[k]}/100*{dcf(i)}" for k in 'EABC'), fmt='0.0000000')
F.row('const', 'Costs independent of facility size', 'USD m',
      lambda i: (f"={ref('Funding.codw', i)}+{fl(i)}*({ref('Construction.base_total', i)}+{ref('Construction.vat_int', i)}+{V('Inputs.agency')}/12"
                 f"+{SG()}{ref('Inputs.M_N_m', i)}*({V('Inputs.swap_fix')}/100/12-{ref('Construction.base', i)}/100*{dcf(i)})"
                 f"+{V('Inputs.sb_commit')}*{V('Inputs.sb_cf')}/100*{dcf(i)}+{ref('Construction.f_codm', i)}*{V('Funding.d0')})"))
F.row('alpha', 'Balance, constant part (alpha)', 'USD m',
      lambda i: (f"={ref('Funding.alpha', i, -1)}+{fl(i)}*{V('Funding.gaff')}/{V('Funding.den')}*({ref('Funding.const', i)}+({ref('Funding.rr', i)}-{ref('Funding.kk', i)})*{ref('Funding.alpha', i, -1)})"), py='f.alpha')
F.row('beta', 'Balance per USD of total funding (beta)', 'factor',
      lambda i: (f"={ref('Funding.beta', i, -1)}+{fl(i)}*{V('Funding.gaff')}/{V('Funding.den')}*({ref('Funding.rr', i)}*{ref('Funding.beta', i, -1)}"
                 f"+{ref('Funding.kk', i)}*({V('Funding.gaff')}-{ref('Funding.beta', i, -1)})"
                 f"+IF({m_(i)}=1,{V('Funding.gaff')}*(" + "+".join(f"{shk[k]}*{ufk[k]}/100" for k in 'EABC') + "),0)"
                 f"+{ref('Construction.f_codm', i)}*{V('Funding.gaff')}*(" + "+".join(f"{shk[k]}*{V('Funding.d1_' + k)}" for k in 'EABC') + "))"), fmt='0.0000000', py='f.beta')
F.scalar('T_aff', 'Total funding requirement at this gearing, closed form T = alpha/(g - beta)', 'USD m',
         f"=INDEX({rng('Funding.alpha')},1,{V('Time.fe')})/({V('Funding.gaff')}-INDEX({rng('Funding.beta')},1,{V('Time.fe')}))", '#,##0.000000', py='f.T_closed_form')
F.scalar('D', 'Senior debt (committed tranches)', 'USD m',
         f"=IF({V('Inputs.s_mode')}<>1,{V('Funding.gc')}*{V('Funding.T_aff')},{V('Inputs.D_c')})", '#,##0.000000', py='f.D')
F.scalar('g', 'Debt share of monthly funding', 'fraction', lambda: (f"=({V('Inputs.D_c')}-SUM({rng('Funding.dsra')}))/({V('Inputs.D_c')}+{V('Inputs.E_c')}-SUM({rng('Funding.dsra')}))" if 'E7' in ERR else f"={V('Funding.gc')}"), '0.000000')
F.sec('Monthly funding schedule (USD m)')
for k, lab in TRK:
    F.row('bo_' + k, f'{lab}: opening balance', 'USD m', lambda i, k=k: f"={ref('Funding.bc_' + k, i, -1)}")
F.row('bo_SB', 'Standby facility: opening balance', 'USD m', lambda i: f"={ref('Funding.bc_SB', i, -1)}")
for k, lab in TRK:
    F.row('idc_' + k, f'{lab}: interest', 'USD m',
          lambda i, k=k: f"={fl(i)}*{ref('Funding.bo_' + k, i)}*({ref('Construction.base', i)}+{mk[k]})/100*{dcfL(i)}*{gu[k]}", total=True, py='f.idc_' + {'E': 'ECA', 'A': 'A', 'B': 'B', 'C': 'COM'}[k])
SBR = lambda i: (f"({V('Inputs.sb_com')}*({ref('Construction.base', i)}+{V('Inputs.m_C1')}+{V('Inputs.sb_add')})/(1-{V('Inputs.wht')}/100)"
                 f"+(1-{V('Inputs.sb_com')})*({ref('Construction.base', i)}+{V('Inputs.m_A')}+{V('Inputs.sb_add')}))/100")
F.row('sbi', 'Standby facility: interest', 'USD m', lambda i: f"={fl(i)}*{ref('Funding.bo_SB', i)}*{SBR(i)}*{dcf(i)}", total=True, py='f.sb_int')
F.row('pri', 'PRI premium on commercial tranche', 'USD m', lambda i: f"={fl(i)}*{PRIR}*{ref('Funding.bo_C', i)}*{ref('Construction.days', i)}/{V('Inputs.day_kcr')}", total=True, py='f.pri')
F.row('swap', 'Swap net payment', 'USD m',
      lambda i: f"={SG()}{fl(i)}*{ref('Inputs.M_N_m', i)}*({V('Inputs.swap_fix')}/100/12-{ref('Construction.base', i)}/100*{dcf(i)})", total=True, py='f.swap')
F.row('cfee', 'Commitment fees, senior tranches', 'USD m',
      lambda i: f"={fl(i)}*(" + "+".join(f"({shk[k]}*{V('Funding.D')}-{ref('Funding.bo_' + k, i)})*{cfk[k]}/100" for k in 'EABC') + f")*{dcf(i)}", total=True, py='f.cfee')
F.row('sbf', 'Commitment fee, standby facility', 'USD m',
      lambda i: f"={fl(i)}*({V('Inputs.sb_commit')}-{ref('Funding.bo_SB', i)})*{V('Inputs.sb_cf')}/100*{dcf(i)}", total=True, py='f.sb_cfee')
F.row('upf', 'Upfront and arrangement fees', 'USD m',
      lambda i: f"=IF({m_(i)}=1," + "+".join(f"{shk[k]}*{V('Funding.D')}*{ufk[k]}/100" for k in 'EABC') + ",0)", total=True, py='f.upfront')
F.row('agy', 'Agency fees during construction', 'USD m', lambda i: f"={fl(i)}*{V('Inputs.agency')}/12", total=True, py='f.agency')
F.row('dsra', 'DSRA initial funding (COD month)', 'USD m',
      lambda i: (f"={ref('Construction.f_codm', i)}*IF({V('Inputs.s_constr')}=1," + "+".join(f"{V('Funding.d1_' + k)}*{shk[k]}*{V('Funding.D')}" for k in 'EABC')
                 + f"+{V('Funding.d0')}," + "+".join(f"{V('Funding.d1_' + k)}*{ref('Funding.bo_' + k, i)}" for k in 'EABC')
                 + f"+{V('Funding.d1_SB')}*{ref('Funding.bo_SB', i)}+{V('Funding.d0')})"), total=True, py='f.dsra')
F.row('X', 'Uses before ECA premium', 'USD m',
      lambda i: f"={fl(i)}*({ref('Construction.base_total', i)}+{ref('Construction.vat_int', i)})+" + "+".join(ref('Funding.' + k, i) for k in ['idc_E', 'idc_A', 'idc_B', 'idc_C', 'sbi', 'pri', 'swap', 'cfee', 'sbf', 'upf', 'agy', 'dsra', 'codw']))
F.row('hd', 'Headroom on committed senior tranches', 'USD m',
      lambda i: f"={V('Funding.D')}-" + "-".join(ref('Funding.bo_' + k, i) for k in 'EABC'))
F.row('bdebt', 'Senior tranche drawdown (pro rata)', 'USD m',
      lambda i: (f"=MIN(({V('Funding.g')}*({ref('Funding.X', i)}-{ref('Funding.dsra', i)})+{ref('Funding.dsra', i)})/(1-{V('Inputs.eca_prem')}/100*{V('Inputs.sh_E')}*{V('Funding.g')}),{ref('Funding.hd', i)})" if 'E7' in ERR else
                 f"=MIN({V('Funding.g')}*{ref('Funding.X', i)}/(1-{V('Inputs.eca_prem')}/100*{V('Inputs.sh_E')}*{V('Funding.g')}),{ref('Funding.hd', i)})"), total=True)
F.row('prem', 'ECA premium (financed)', 'USD m', lambda i: f"={V('Inputs.eca_prem')}/100*{V('Inputs.sh_E')}*{ref('Funding.bdebt', i)}", total=True, py='f.eca_prem')
F.row('uses', 'Total uses of funds', 'USD m', lambda i: f"={ref('Funding.X', i)}+{ref('Funding.prem', i)}", total=True, py='f.uses')
F.row('bfund', 'Funded pro rata from committed debt and equity', 'USD m', lambda i: (f"={ref('Funding.uses', i)}" if 'E7' in ERR else f"={ref('Funding.bdebt', i)}/{V('Funding.g')}"), total=True, py='f.base_fund')
F.row('r1', 'Remaining uses after committed facilities', 'USD m', lambda i: f"={ref('Funding.uses', i)}-{ref('Funding.bfund', i)}")
F.row('ldrec', 'Delay LDs and DSU proceeds received', 'USD m',
      lambda i: f"=IF(AND({V('Inputs.s_constr')}<>1,{m_(i)}={V('Inputs.ld_month')}),{V('Inputs.ld_delay')}+{V('Inputs.dsu')},0)", total=True, py='f.ld_received')
F.row('ldu', 'LD and DSU proceeds applied', 'USD m',
      lambda i: f"=MIN({ref('Funding.r1', i)},{ref('Funding.ldpool', i, -1)}+{ref('Funding.ldrec', i)})", total=True, py='f.ld_used')
F.row('ldpool', 'LD and DSU proceeds held (Proceeds Account)', 'USD m',
      lambda i: f"={ref('Funding.ldpool', i, -1)}+{ref('Funding.ldrec', i)}-{ref('Funding.ldu', i)}", py='f.ld_pool')
F.row('sbd', 'Standby facility drawdown (75%)', 'USD m', lambda i: f"={V('Inputs.sb_split')}*({ref('Funding.r1', i)}-{ref('Funding.ldu', i)})", total=True, py='f.sb_draw')
F.row('ced', 'Contingent equity (25%)', 'USD m', lambda i: f"=(1-{V('Inputs.sb_split')})*({ref('Funding.r1', i)}-{ref('Funding.ldu', i)})", total=True, py='f.ce_draw')
for k, lab in TRK:
    F.row('dr_' + k, f'{lab}: drawdown', 'USD m', lambda i, k=k: f"={shk[k]}*{ref('Funding.bdebt', i)}", total=True,
          py='f.draw_' + {'E': 'ECA', 'A': 'A', 'B': 'B', 'C': 'COM'}[k])
for k, lab in TRK:
    F.row('bc_' + k, f'{lab}: closing balance', 'USD m', lambda i, k=k: f"={ref('Funding.bo_' + k, i)}+{ref('Funding.dr_' + k, i)}",
          py='f.bal_' + {'E': 'ECA', 'A': 'A', 'B': 'B', 'C': 'COM'}[k])
F.row('bc_SB', 'Standby facility: closing balance', 'USD m', lambda i: f"={ref('Funding.bo_SB', i)}+{ref('Funding.sbd', i)}", py='f.bal_SB')
F.sec('Equity (USD m)')
F.row('eq', 'Equity contributions (incl. LNTP credit in month 1)', 'USD m',
      lambda i: f"={ref('Funding.bfund', i)}-{ref('Funding.bdebt', i)}+{ref('Funding.ced', i)}", total=True, py='f.equity')
F.row('eq_cash', 'Equity contributed in cash', 'USD m', lambda i: f"={ref('Funding.eq', i)}-IF({m_(i)}=1,{V('Inputs.lntp')},0)", total=True, py='f.equity_cash')
F.row('sc', 'Share capital', 'USD m', lambda i: f"=(1-{V('Inputs.s_shl')})*{ref('Funding.eq', i)}", total=True, py='f.sc_contrib')
F.row('shl_c', 'Shareholder loans advanced', 'USD m', lambda i: f"={V('Inputs.s_shl')}*{ref('Funding.eq', i)}", total=True, py='f.shl_contrib')
F.row('shl_i', 'Shareholder loan interest capitalized (to COD)', 'USD m',
      lambda i: f"=IF({m_(i)}<={nc},{ref('Funding.shl_b', i, -1)}*{V('Inputs.shl_rate')}/100*{ref('Construction.days', i)}/{V('Inputs.day_kcr')},0)", total=True, py='f.shl_capint')
F.row('shl_b', 'Shareholder loan balance', 'USD m',
      lambda i: f"={ref('Funding.shl_b', i, -1)}+{ref('Funding.shl_i', i)}+{ref('Funding.shl_c', i)}", py='f.shl_bal')
F.row('debt_draw', 'Total debt drawdowns (incl. standby)', 'USD m', lambda i: f"={ref('Funding.bdebt', i)}+{ref('Funding.sbd', i)}", total=True, py='f.debt_draw')
F.row('fin_costs', 'Financing costs (IDC, fees, premium, VAT interest)', 'USD m',
      lambda i: "=" + "+".join(ref('Funding.' + k, i) for k in ['idc_E', 'idc_A', 'idc_B', 'idc_C', 'sbi', 'pri', 'swap', 'cfee', 'sbf', 'upf', 'agy', 'prem']) + f"+{fl(i)}*{ref('Construction.vat_int', i)}", total=True, py='f.fin_costs')
F.scalar('T', 'Total funding requirement (sum of uses)', 'USD m', f"=SUM({rng('Funding.uses')})", '#,##0.000000', py='f.T')
F.scalar('cap', 'Capitalized cost (book and tax)', 'USD m',
         lambda: f"=SUM({rng('Funding.uses')})-SUM({rng('Funding.dsra')})-SUM({rng('Construction.wc')})-SUM({rng('Funding.codw')})+SUM({rng('Funding.shl_i')})-SUM({rng('Funding.ldrec')})-{V('Inputs.s_ld_prep')}*{V('Inputs.ld_perf')}",
         '#,##0.000000', py='R.capcost')
# v1.6 appended (D-143): COD-period working capital funded through the construction cascade, held to COD
F.gap()
F.scalar('codneed', 'COD-period operating cash shortfall before tax (working capital built in the COD period)', 'USD m',
         lambda: (f"=MAX(0,-(INDEX({rng('Operations.ebitda')},1,{V('Time.tcod')})-INDEX({rng('Operations.dnwc')},1,{V('Time.tcod')})+INDEX({rng('Operations.inv_rel')},1,{V('Time.tcod')})"
                  f"-INDEX({rng('Reserves.mmc')},1,{V('Time.tcod')})+INDEX({rng('Operations.mm')},1,{V('Time.tcod')})))"), '#,##0.000000', py='R.cod_wc')
F.row('codw', 'COD working-capital funding (a use in the last funding month; held in the project accounts to COD)', 'USD m',
      lambda i: f"=IF({m_(i)}={V('Time.fe')},{V('Funding.codneed')},0)", total=True, py='f.cod_wc')

# ========================================================================================
# DEBT (semiannual)
# ========================================================================================
D_ = Sheet('Debt', 'S', 'Debt: tranches, scheduled repayment, waiver, refinancing, swap, sculpting')
TR6 = [('E', 'ECA', 'ECA-covered tranche'), ('A', 'A', 'ABDB A-loan'), ('B', 'B', 'ABDB B-loan'),
       ('C', 'COM', 'Commercial tranche'), ('SB', 'SB', 'Standby facility'), ('BD', 'BOND', '2025 project bond')]
tt = lambda i: ref('Time.t', i)
EPS = V('Inputs.eps')
yf = lambda i: ref('Time.yf30', i)
D_.sec('Rates')
D_.row('mC', 'Commercial margin (step-ups)', '%',
       lambda i: f"=IF({ref('Time.start', i)}<{V('Inputs.d_mC2')},{V('Inputs.m_C1')},IF({ref('Time.start', i)}<{V('Inputs.d_mC3')},{V('Inputs.m_C2')},{V('Inputs.m_C3')}))")
D_.row('up', 'Waiver margin uplift', '%', lambda i: f"={ref('Time.f_up', i)}*{V('Inputs.w_up')}")
dsc = lambda i: f"{ref('Time.days', i)}/{V('Inputs.day_usd')}"
dscL = lambda i: '0.5' if 'E4' in ERR else dsc(i)
MK6 = {'E': V('Inputs.m_E'), 'A': V('Inputs.m_A'), 'B': V('Inputs.m_B')}
for k, pk, lab in TR6:
    if k in ('E', 'A', 'B'):
        fn = lambda i, k=k: f"=({ref('Operations.base', i)}+{MK6[k]}+{ref('Debt.up', i)})/100*{dscL(i)}"
    elif k == 'C':
        fn = lambda i: f"=({ref('Operations.base', i)}+{ref('Debt.mC', i)}+{ref('Debt.up', i)})/100*{dscL(i)}/(1-{V('Inputs.wht')}/100)"
    elif k == 'SB':
        fn = lambda i: (f"=({V('Inputs.sb_com')}*({ref('Operations.base', i)}+{ref('Debt.mC', i)}+{V('Inputs.sb_add')}+{ref('Debt.up', i)})/(1-{V('Inputs.wht')}/100)"
                        f"+(1-{V('Inputs.sb_com')})*({ref('Operations.base', i)}+{V('Inputs.m_A')}+{V('Inputs.sb_add')}+{ref('Debt.up', i)}))/100*{dsc(i)}")
    else:
        fn = lambda i: f"={V('Inputs.b_cpn')}/100*{yf(i)}"
    D_.row('r_' + k, f'{lab}: rate per period', 'factor', fn, fmt='0.0000000')
D_.sec('Contract repayment profile')
D_.row('prof', 'Repayment profile, selected', 'fraction',
       lambda i: f"=IF({V('Inputs.s_profile')}=1,{ref('Inputs.S_prof_fc', i)},{ref('Inputs.S_prof_cod', i)})", fmt='0.000000', py='S.prof')
D_.row('rem', 'Remaining profile (this and later installments)', 'fraction', lambda i: f"=SUM({rngrel('Debt.prof', i, NS - 1)})", fmt='0.000000')
D_.row('psh', 'Installment share of remaining balance', 'fraction', lambda i: f"=IF({ref('Debt.rem', i)}>{EPS},{ref('Debt.prof', i)}/{ref('Debt.rem', i)},0)", fmt='0.000000')
fds = lambda i: ref('Time.f_ds', i)
def bal_cod(k):
    if k == 'SB':
        return f"INDEX({rng('Funding.bc_SB')},1,{V('Time.fe')})"
    return f"INDEX({rng('Funding.bc_' + k)},1,{V('Time.fe')})"
for k, pk, lab in TR6:
    D_.sec(lab)
    D_.row('bo_' + k, 'Opening balance', 'USD m', lambda i, k=k: f"={fds(i)}*{ref('Debt.bc_' + k, i, -1)}", py='S.bal_open_' + pk)
    if k != 'BD':
        D_.row('dfo_' + k, 'Deferred principal, opening', 'USD m', lambda i, k=k: f"={ref('Debt.dfc_' + k, i, -1)}")
    D_.row('int_' + k, 'Interest (incl. WHT gross-up where applicable)', 'USD m', lambda i, k=k: f"={ref('Debt.bo_' + k, i)}*{ref('Debt.r_' + k, i)}", total=True, py='S.interest_' + pk)
    if k != 'BD':
        D_.row('sch_' + k, 'Scheduled principal per profile', 'USD m',
               lambda i, k=k: f"={fds(i)}*({ref('Debt.bo_' + k, i)}-{ref('Debt.dfo_' + k, i)})*{ref('Debt.pshe' if k == 'E' else 'Debt.psh', i)}", total=True, py='S.sched_' + pk)
        D_.row('dfn_' + k, 'Principal deferred under the waiver', 'USD m',
               lambda i, k=k: f"={ref('Time.f_t23', i)}*{V('Inputs.w_def')}*{ref('Debt.sch_' + k, i)}", total=True, py='S.deferred_new_' + pk)
        D_.row('dfr_' + k, 'Deferred principal repaid (equal parts over the remaining repayment dates)', 'USD m',
               lambda i, k=k: f"=IF({ref('Time.n_drep', i)}>0,{ref('Time.f_drep', i)}*{ref('Debt.dfo_' + k, i)}/{ref('Time.n_drep', i)},0)", total=True, py='S.deferred_repay_' + pk)
        D_.row('p_' + k, 'Principal paid', 'USD m',
               lambda i, k=k: f"={ref('Debt.sch_' + k, i)}-{ref('Debt.dfn_' + k, i)}+{ref('Debt.dfr_' + k, i)}", total=True, py='S.principal_' + pk)
        D_.row('ld_' + k, 'Performance LD prepayment', 'USD m',
               lambda i, k=k: (f"={ref('Time.f_ld', i)}*{V('Inputs.ld_perf')}*({ref('Debt.bo_' + k, i)}-{ref('Debt.p_' + k, i)})/("
                               + "+".join(f"{ref('Debt.bo_' + j, i)}-{ref('Debt.p_' + j, i)}" for j, _, _ in TR6[:5]) + f"+{EPS})"), total=True, py='S.ld_prepay_' + pk)
        if k in ('B', 'C', 'SB'):
            D_.row('rf_' + k, 'Refinanced (prepaid from bond proceeds)', 'USD m',
                   lambda i, k=k: f"={ref('Time.f_tR', i)}*({ref('Debt.bo_' + k, i)}-{ref('Debt.p_' + k, i)}-{ref('Debt.ld_' + k, i)})", total=True, py='S.refi_prepay_' + pk)
        else:
            D_.row('rf_' + k, 'Refinanced (not refinanced: stays in place)', 'USD m', lambda i: f"={ref('Time.f_tR', i)}*0", total=True)
        D_.row('dfc_' + k, 'Deferred principal, closing', 'USD m',
               lambda i, k=k: (f"=(1-{ref('Time.f_tR', i)})*({ref('Debt.dfo_' + k, i)}+{ref('Debt.dfn_' + k, i)}-{ref('Debt.dfr_' + k, i)})"
                               if k in ('B', 'C', 'SB') else f"={ref('Debt.dfo_' + k, i)}+{ref('Debt.dfn_' + k, i)}-{ref('Debt.dfr_' + k, i)}"), py='S.deferred_' + pk)
        D_.row('after_' + k, 'Balance after scheduled payment, LDs and refinancing', 'USD m',
               lambda i, k=k: f"={ref('Debt.bo_' + k, i)}-{ref('Debt.p_' + k, i)}-{ref('Debt.ld_' + k, i)}-{ref('Debt.rf_' + k, i)}")
        D_.row('sw_' + k, 'Cash sweep prepayment', 'USD m',
               lambda i, k=k: (f"={ref('Waterfall.lusw', i)}*{ref('Debt.after_' + k, i)}/(" + "+".join(ref('Debt.after_' + j, i) for j, _, _ in TR6[:5]) + f"+{EPS})"
                               + (f"+{ref('Waterfall.mpsw', i)}" if k == 'C' else '')), total=True, py='S.sweep_' + pk)
        D_.row('bc_' + k, 'Closing balance', 'USD m',
               lambda i, k=k: f"=IF({ref('Time.f_cod', i)}=1,{bal_cod(k)},{fds(i)}*({ref('Debt.after_' + k, i)}-{ref('Debt.sw_' + k, i)}))", py='S.bal_close_' + pk)
    else:
        D_.row('p_BD', 'Principal paid', 'USD m',
               lambda i: f"=IF({ref('Debt.bo_BD', i)}>0,MIN({ref('Debt.Fc', i, -1)}*{ref('Inputs.S_prof_bond', i)},{ref('Debt.bo_BD', i)}),0)", total=True, py='S.principal_BOND')
        D_.row('after_BD', 'Balance after scheduled payment', 'USD m', lambda i: f"={ref('Debt.bo_BD', i)}-{ref('Debt.p_BD', i)}")
        D_.row('bc_BD', 'Closing balance (incl. bond issued)', 'USD m', lambda i: f"={ref('Debt.after_BD', i)}+{ref('Debt.Fn', i)}", py='S.bal_close_BOND')
D_.sec('Refinancing 2025 (USD m)')
D_.row('udf', 'Swap unwind discount factor at the flat swap rate', 'factor',
       lambda i: f"=IF({ref('Time.end', i)}>{V('Inputs.d_refi')},(1+{V('Inputs.unw_r')}/100*{yf(i)})^-({tt(i)}-{V('Time.tR')}),0)", fmt='0.000000')
D_.scalar('mtm', 'Swap unwind receipt (terminated share, MTM at the flat swap rate)', 'USD m',
          lambda: f"={V('Inputs.s_refi')}*{V('Inputs.unw_sh')}*({V('Inputs.unw_r')}-{V('Inputs.swap_fix')})/100*SUMPRODUCT({rng('Inputs.S_N_s')},{rng('Debt.udf')},{rng('Time.yf30')})", '#,##0.000000')
D_.row('prep', 'Principal prepaid from bond proceeds (B-loan, commercial, standby)', 'USD m',
       lambda i: f"={ref('Debt.rf_B', i)}+{ref('Debt.rf_C', i)}+{ref('Debt.rf_SB', i)}", total=True)
D_.row('Fn', 'Bond issued (face)', 'USD m',
       lambda i: f"={ref('Time.f_tR', i)}*({ref('Debt.prep', i)}+{V('Inputs.b_oth')}+{V('Inputs.pcg_up')}/100*{V('Inputs.pcg')}-{V('Debt.mtm')})/({V('Inputs.b_px')}-{V('Inputs.b_uw')})", total=True)
D_.row('Fc', 'Bond face, cumulative', 'USD m', lambda i: f"={ref('Debt.Fc', i, -1)}+{ref('Debt.Fn', i)}")
D_.scalar('F', 'Bond face amount', 'USD m', lambda: f"=SUM({rng('Debt.Fn')})", '#,##0.000000', py='R.bond_F')
D_.row('unwind', 'Swap unwind receipt', 'USD m', lambda i: f"={ref('Time.f_tR', i)}*{V('Debt.mtm')}", total=True, py='S.unwind')
D_.row('refi_c', 'Refinancing costs (OID, underwriting, other, PCG upfront)', 'USD m',
       lambda i: f"={ref('Debt.Fn', i)}*(1-{V('Inputs.b_px')})+{V('Inputs.b_uw')}*{ref('Debt.Fn', i)}+{ref('Time.f_tR', i)}*({V('Inputs.b_oth')}+{V('Inputs.pcg_up')}/100*{V('Inputs.pcg')})", total=True, py='S.refi_costs')
D_.sec('Swap, premiums and fees (USD m)')
D_.row('swsh', 'Swap share outstanding', 'fraction', lambda i: f"=IF({ref('Time.f_postR', i)}=1,{V('Inputs.sw_rem')},1)")
D_.row('swap', 'Swap net payment (fixed 30/360 less floating ACT/360)', 'USD m',
       lambda i: f"={SG()}{fds(i)}*{ref('Inputs.S_N_s', i)}*{ref('Debt.swsh', i)}*({V('Inputs.swap_fix')}/100*{yf(i)}-{ref('Operations.base', i)}/100*{dsc(i)})", total=True, py='S.swap')
D_.row('pri', 'PRI premium (commercial tranche)', 'USD m', lambda i: f"={PRIR}*{ref('Debt.bo_C', i)}*{ref('Time.days', i)}/{V('Inputs.day_kcr')}", total=True, py='S.pri')
D_.row('pcg', 'ABDB PCG fee (bond)', 'USD m',
       lambda i: f"=IF({ref('Debt.Fc', i, -1)}>0,{V('Inputs.pcg_fee')}/100*{yf(i)}*{ref('Debt.bo_BD', i)}*{V('Inputs.pcg')}/{ref('Debt.Fc', i, -1)},0)", total=True, py='S.pcg')
D_.row('wfee', 'Waiver fee', 'USD m', lambda i: f"={ref('Time.f_t23', i)}*{V('Inputs.w_fee')}/100*(" + "+".join(ref('Debt.bo_' + k, i) for k in ['E', 'A', 'B', 'C', 'SB']) + ")", total=True, py='S.waiver_fee')
D_.row('int', 'Interest, all tranches', 'USD m', lambda i: "=" + "+".join(ref('Debt.int_' + k, i) for k, _, _ in TR6), total=True, py='S.interest_total')
D_.row('sc', 'Senior financing costs (interest, swap, PRI, PCG)', 'USD m',
       lambda i: f"={ref('Debt.int', i)}+{ref('Debt.swap', i)}+{ref('Debt.pri', i)}+{ref('Debt.pcg', i)}", total=True, py='S.senior_costs')
D_.row('prin', 'Principal paid, all tranches', 'USD m', lambda i: "=" + "+".join(ref('Debt.p_' + k, i) for k, _, _ in TR6), total=True, py='S.principal_total')
D_.row('ds', 'Senior debt service', 'USD m', lambda i: f"={ref('Debt.sc', i)}+{ref('Debt.prin', i)}", total=True, py='S.ds')
D_.row('bo', 'Senior debt outstanding, opening', 'USD m', lambda i: "=" + "+".join(ref('Debt.bo_' + k, i) for k, _, _ in TR6), py='S.debt_open')
D_.row('bc', 'Senior debt outstanding, closing', 'USD m', lambda i: "=" + "+".join(ref('Debt.bc_' + k, i) for k, _, _ in TR6), py='S.debt_close')
D_.sec('DSRA target: next period scheduled debt service (USD m)')
def nxt(key, i):
    return ref(key, i, 1)
LIVE = lambda i: f"AND({tt(i)}>={V('Time.tcod')},{nxt('Time.t', i)}>0)"
D_.row('bn_C', 'Commercial balance carried to next period', 'USD m', lambda i: f"=IF({ref('Time.f_cod', i)}=1,{ref('Debt.bc_C', i)},{ref('Debt.after_C', i)})")
for k, pk, lab in TR6[:5]:
    BN = lambda i, k=k: f"IF({ref('Time.f_cod', i)}=1,{ref('Debt.bc_' + k, i)},{ref('Debt.after_' + k, i)})"
    D_.row('tn_' + k, f'{lab}: next period debt service', 'USD m',
           lambda i, k=k, BN=BN: (f"=IF({LIVE(i)},({BN(i)}-{ref('Debt.dfc_' + k, i)})*{nxt('Debt.pshe' if k == 'E' else 'Debt.psh', i)}"
                                  f"+IF({nxt('Time.n_drep', i)}>0,{nxt('Time.f_drep', i)}*{ref('Debt.dfc_' + k, i)}/{nxt('Time.n_drep', i)},0)"
                                  f"+{BN(i)}*{nxt('Debt.r_' + k, i)},0)"))
BNB = lambda i: f"({ref('Debt.after_BD', i)}+{ref('Debt.Fn', i)})"
D_.row('tn_BD', 'Bond: next period debt service', 'USD m',
       lambda i: (f"=IF(AND({LIVE(i)},{BNB(i)}>{EPS}),MIN({ref('Debt.Fc', i)}*{nxt('Inputs.S_prof_bond', i)},{BNB(i)})"
                  f"+{BNB(i)}*({nxt('Debt.r_BD', i)}+{V('Inputs.pcg_fee')}/100*{nxt('Time.yf30', i)}*{V('Inputs.pcg')}/{ref('Debt.Fc', i)}),0)"))
D_.row('tgt', 'DSRA target (six months of next debt service)', 'USD m',
       lambda i: (f"=IF({LIVE(i)}," + "+".join(ref('Debt.tn_' + k, i) for k, _, _ in TR6)
                  + f"+{SG()}{nxt('Inputs.S_N_s', i)}*{nxt('Debt.swsh', i)}*({V('Inputs.swap_fix')}/100*{nxt('Time.yf30', i)}-{nxt('Operations.base', i)}/100*{nxt('Time.days', i)}/{V('Inputs.day_usd')})"
                  + f"+{PRIR}*{ref('Debt.bn_C', i)}*{nxt('Time.days', i)}/{V('Inputs.day_kcr')},0)"), py='S.dsra_target')
D_.sec('Live sculpting check (FC base: constant-DSCR total debt service; ECA equal installments, other tranches sculpted)')
fsc = lambda i: ref('Time.f_sc', i)
DO = lambda: f"{V('Funding.D')}*(1-{V('Inputs.sh_E')})"
SHO = lambda: f"(1-{V('Inputs.sh_E')})"
D_.row('wrate', 'Sculpting rate on the other tranches\' scheduled balance (A, B, commercial incl. PRI; plus swap)', 'factor',
       lambda i: (f"=IF({fsc(i)}=1,({V('Inputs.sh_A')}*{ref('Debt.r_A', i)}+{V('Inputs.sh_B')}*{ref('Debt.r_B', i)}"
                  f"+{V('Inputs.sh_C')}*({ref('Debt.r_C', i)}+{PRIR}*{ref('Time.days', i)}/{V('Inputs.day_kcr')}))/{SHO()}+{ref('Debt.ssw', i)},0)"), fmt='0.0000000')
D_.row('pvc', 'PV of CFADS to final maturity at the sculpting rate', 'USD m',
       lambda i: f"=IF({fsc(i)}=1,({ref('Waterfall.cfads', i)}{('+' + ref('Tax.tax', i)) if 'E8' in ERR else ''}+{nxt('Debt.pvc', i)})/(1+{ref('Debt.wrate', i)}),0)")
D_.scalar('dscr_eff', 'Sculpted DSCR = PV(CFADS) / (other tranches + PV of ECA debt service), at the sculpting rate', 'x',
          lambda: f"=INDEX({rng('Debt.pvc')},1,{V('Time.t1')})/({DO()}+INDEX({rng('Debt.pvE')},1,{V('Time.t1')}))", '0.000000', py='R.sculpt_dscr_live')
D_.scalar('capacity', 'Debt capacity at the target DSCR (debt x sculpted DSCR / target)', 'USD m', lambda: f"={V('Funding.D')}*{V('Debt.dscr_eff')}/{V('Inputs.dscr_t')}", '#,##0.000000', py='R.capacity_live')
D_.scalar('gearcap', 'Debt at the gearing cap (closed form)', 'USD m', lambda: f"={V('Inputs.gear')}*{V('Funding.T_aff')}", '#,##0.000000')
D_.row('sds', 'Sculpted debt service (all tranches)', 'USD m', lambda i: f"=IF({fsc(i)}=1,({ref('Waterfall.cfads', i)}{('+' + ref('Tax.tax', i)) if 'E8' in ERR else ''})/{V('Debt.dscr_eff')},0)")
D_.row('sbal', 'Sculpted balance of the other tranches, opening', 'USD m',
       lambda i: f"=IF({fsc(i)}=1,IF({tt(i)}={V('Time.t1')},{DO()},{ref('Debt.sbal', i, -1)}-{ref('Debt.sprin', i, -1)}),0)")
D_.row('sprin', 'Sculpted principal of the other tranches', 'USD m', lambda i: f"={ref('Debt.sds', i)}-{ref('Debt.sE', i)}-{ref('Debt.sbal', i)}*{ref('Debt.wrate', i)}")
D_.row('sdiff', 'Sculpted principal less contract principal, other tranches (FC base)', 'USD m',
       lambda i: f"=IF({V('Inputs.Scenario')}=1,{ref('Debt.sprin', i)}-{fsc(i)}*{ref('Inputs.S_prof_fc', i)}*{DO()},0)")
# v1.4 appended ECA tests on the selected profile (u09 R11; values as P-F09)
D_.gap()
D_.row('eca_y', 'ECA tests (ECA-covered tranche, contractual schedule): years from COD to period end', 'years', lambda i: f"=({ref('Time.end', i)}-{V('Time.cod')})/{V('Inputs.day_yr')}", fmt='0.0000', py='S.eca_yrs')
D_.scalar('eca_wal', 'ECA test: weighted average life from COD', 'years', lambda: f"=SUMPRODUCT({rng('Debt.pe')},{rng('Debt.eca_y')})/SUM({rng('Debt.pe')})", '0.0000', py='R.eca_wal')
D_.scalar('eca_max', 'ECA test: largest installment as a share of principal', 'fraction', lambda: f"=MAX({rng('Debt.pe')})/SUM({rng('Debt.pe')})", '0.0000', py='R.eca_max_share')
D_.scalar('eca_ten', 'ECA test: repayment term from COD (to the last installment)', 'years',
          lambda: f"=INDEX({rng('Debt.eca_y')},1,SUMPRODUCT(MAX(({rng('Debt.pe')}>{V('Inputs.eps')})*{rng('Time.t')})))", '0.0000', py='R.eca_tenor')
D_.scalar('eca_fm', 'ECA test: months from COD to the first repayment', 'months',
          lambda: (f"=(YEAR(INDEX({rng('Time.end')},1,_xlfn.MINIFS({rng('Time.t')},{rng('Debt.pe')},\">\"&{V('Inputs.eps')}))+1)-YEAR({V('Time.cod')}))*12"
                   f"+MONTH(INDEX({rng('Time.end')},1,_xlfn.MINIFS({rng('Time.t')},{rng('Debt.pe')},\">\"&{V('Inputs.eps')}))+1)-MONTH({V('Time.cod')})"), '0', py='R.eca_first_m')
D_.scalar('eca_24', 'ECA test: share of principal repaid within the window from COD', 'fraction',
          lambda: f"=SUMIFS({rng('Debt.pe')},{rng('Time.end')},\"<=\"&(EDATE({V('Time.cod')},{V('Inputs.eca_m')})-1))/SUM({rng('Debt.pe')})", '0.0000', py='R.eca_24m_share')
# v1.5 appended (D-128): ECA-covered tranche in equal installments; sculpting helpers
D_.gap()
D_.sec('ECA-covered tranche: contractual schedule (equal semiannual installments, first repayment period to final maturity)')
D_.row('pe', 'ECA installment, share of the ECA amount', 'fraction', lambda i: f"=IF({fsc(i)}=1,1/SUM({rng('Time.f_sc')}),0)", fmt='0.000000', py='S.prof_eca')
D_.row('reme', 'ECA remaining profile (this and later installments)', 'fraction', lambda i: f"=SUM({rngrel('Debt.pe', i, NS - 1)})", fmt='0.000000')
D_.row('pshe', 'ECA installment share of remaining balance', 'fraction', lambda i: f"=IF({ref('Debt.reme', i)}>{EPS},{ref('Debt.pe', i)}/{ref('Debt.reme', i)},0)", fmt='0.000000')
D_.row('ssw', 'Swap net cost per USD of total scheduled balance (sculpting)', 'factor',
       lambda i: (f"=IF({fsc(i)}=1,{SG()}{ref('Inputs.S_N_s', i)}/({V('Funding.D')}*({V('Inputs.sh_E')}*{ref('Debt.reme', i)}+{SHO()}*{ref('Debt.rem', i)}))"
                  f"*({V('Inputs.swap_fix')}/100*{yf(i)}-{ref('Operations.base', i)}/100*{dsc(i)}),0)"), fmt='0.0000000')
D_.row('sE', 'ECA scheduled debt service in the sculpting (installment, interest, swap share)', 'USD m',
       lambda i: f"=IF({fsc(i)}=1,{V('Funding.D')}*{V('Inputs.sh_E')}*({ref('Debt.pe', i)}+{ref('Debt.reme', i)}*({ref('Debt.r_E', i)}+{ref('Debt.ssw', i)})),0)")
D_.row('pvE', 'PV of ECA scheduled debt service at the sculpting rate', 'USD m',
       lambda i: f"=IF({fsc(i)}=1,({ref('Debt.sE', i)}+{nxt('Debt.pvE', i)})/(1+{ref('Debt.wrate', i)}),0)")

# ========================================================================================
# TAX
# ========================================================================================
TX = Sheet('Tax', 'S', 'Tax: holiday, deferred depreciation, thin capitalization, minimum turnover tax')
om = lambda i: ref('Time.om', i); oms_ = lambda i: ref('Time.oms', i); ome_ = lambda i: ref('Time.ome', i)
seg = lambda i, a, b: f"MAX(0,MIN({ome_(i)},{b})-MIN(MAX({oms_(i)},{a}),{b}))"
HE = lambda: (f"{V('Inputs.red_y')}*12" if 'E5' in ERR else f"{V('Inputs.hol_y')}*12")
TX.row('hol', 'Holiday months (OY1-OY5)', 'months', lambda i: f"=MAX(0,MIN({ome_(i)},{HE()})-MIN({oms_(i)},{HE()}))", fmt='0')
TX.row('red', 'Reduced-rate months (OY6-OY8)', 'months', lambda i: f"={seg(i, HE(), V('Inputs.red_y') + '*12')}", fmt='0')
TX.row('full', 'Full-rate months (OY9+)', 'months', lambda i: f"={om(i)}-{ref('Tax.hol', i)}-{ref('Tax.red', i)}", fmt='0')
cap_ = V('Funding.cap')
DM = f"({V('Inputs.dep_pl')}*{cap_}/{V('Inputs.life_pl')}+{V('Inputs.dep_bl')}*{cap_}/{V('Inputs.life_bl')}+{V('Inputs.dep_in')}*{cap_}/{V('Inputs.life_in')})"
TX.row('dep_full', 'Tax depreciation (straight line from COD)', 'USD m',
       lambda i: (f"={V('Inputs.dep_pl')}*{cap_}/{V('Inputs.life_pl')}*MAX(0,MIN({ome_(i)},{V('Inputs.life_pl')})-MIN({oms_(i)},{V('Inputs.life_pl')}))"
                  f"+{V('Inputs.dep_bl')}*{cap_}/{V('Inputs.life_bl')}*MAX(0,MIN({ome_(i)},{V('Inputs.life_bl')})-MIN({oms_(i)},{V('Inputs.life_bl')}))"
                  f"+{V('Inputs.dep_in')}*{cap_}/{V('Inputs.life_in')}*MAX(0,MIN({ome_(i)},{V('Inputs.life_in')})-MIN({oms_(i)},{V('Inputs.life_in')}))"), total=True, py='S.dep_full')
TX.row('dep_hol', 'Depreciation of holiday months (deemed deferred)', 'USD m',
       lambda i: (f"=({V('Inputs.dep_pl')}*{cap_}/{V('Inputs.life_pl')}+{V('Inputs.dep_bl')}*{cap_}/{V('Inputs.life_bl')})*{ref('Tax.hol', i)}"
                  f"+{V('Inputs.dep_in')}*{cap_}/{V('Inputs.life_in')}*MAX(0,MIN({ome_(i)},MIN({V('Inputs.life_in')},{HE()}))-MIN({oms_(i)},MIN({V('Inputs.life_in')},{HE()})))"), total=True, py='S.dep_hol')
TX.row('dep_cur', 'Depreciation deducted currently', 'USD m', lambda i: f"={ref('Tax.dep_full', i)}-{ref('Tax.dep_hol', i)}", total=True, py='S.dep_cur')
TX.row('shl_int', 'Shareholder loan interest accrued', 'USD m',
       lambda i: f"=IF({tt(i)}>={V('Time.tcod')},{ref('Waterfall.shl_o', i)}*{V('Inputs.shl_rate')}/100*{ref('Time.opdays', i)}/{V('Inputs.day_kcr')},0)", total=True, py='S.shl_int')
TX.row('thin', 'Thin cap: deductible share = min(1, 3 x equity / SHL)', 'fraction',
       lambda i: f"=IF({ref('Waterfall.shl_o', i)}>0,MIN(1,{V('Inputs.thin')}*({V('Waterfall.sc_tot')}+MAX(0,{ref('Waterfall.re', i, -1)}))/{ref('Waterfall.shl_o', i)}),1)", fmt='0.0000', py='S.thin_frac')
TX.row('shl_ded', 'Shareholder loan interest deductible', 'USD m', lambda i: f"={ref('Tax.shl_int', i)}*{ref('Tax.thin', i)}", total=True, py='S.shl_ded')
TX.row('int_ded', 'Senior financing costs deductible (all grandfathered)', 'USD m',
       lambda i: f"={ref('Debt.sc', i)}+{ref('Debt.wfee', i)}+{ref('Debt.refi_c', i)}-{ref('Debt.unwind', i)}", total=True, py='S.int_ded')
TX.row('nh', 'Non-holiday share of operating months', 'fraction', lambda i: f"=IF({om(i)}>0,({om(i)}-{ref('Tax.hol', i)})/{om(i)},0)", py='S.nonhol_frac')
TX.row('ti_pre', 'Taxable income before losses and deferred depreciation', 'USD m',
       lambda i: f"=({ref('Operations.ebitda', i)}-{ref('Tax.int_ded', i)}-{ref('Tax.shl_ded', i)})*{ref('Tax.nh', i)}-{ref('Tax.dep_cur', i)}", total=True, py='S.ti_pre')
TX.row('luse', 'Tax losses used', 'USD m', lambda i: f"=MIN({ref('Tax.loss', i, -1)},MAX(0,{ref('Tax.ti_pre', i)}))", total=True, py='S.loss_use')
TX.row('puse', 'Deferred depreciation used', 'USD m',
       lambda i: f"=MIN({ref('Tax.pool', i, -1)},MAX(0,{ref('Tax.ti_pre', i)}-{ref('Tax.luse', i)}))", total=True, py='S.pool_use')
TX.row('pool', 'Deferred depreciation pool, closing', 'USD m',
       lambda i: f"={ref('Tax.pool', i, -1)}+{'0' if 'E6' in ERR else ref('Tax.dep_hol', i)}-{ref('Tax.puse', i)}", py='S.pool_close')
TX.row('loss', 'Tax losses carried forward, closing', 'USD m',
       lambda i: f"={ref('Tax.loss', i, -1)}-{ref('Tax.luse', i)}+MAX(0,-{ref('Tax.ti_pre', i)})", py='S.loss_close')
TX.row('taxable', 'Taxable income', 'USD m', lambda i: f"=MAX(0,{ref('Tax.ti_pre', i)}-{ref('Tax.luse', i)}-{ref('Tax.puse', i)})", total=True, py='S.taxable')
TX.row('rate', 'Applicable CIT rate (month-weighted)', '%',
       lambda i: f"=IF({ref('Tax.red', i)}+{ref('Tax.full', i)}>0,({ref('Tax.red', i)}*{V('Inputs.cit_red')}+{ref('Tax.full', i)}*{V('Inputs.cit')})/({ref('Tax.red', i)}+{ref('Tax.full', i)})/100,0)", fmt='0.0000', py='S.hold_rate')
TX.row('cit', 'Corporate income tax', 'USD m', lambda i: f"={ref('Tax.taxable', i)}*{ref('Tax.rate', i)}", total=True, py='S.cit')
TX.row('mtt', 'Minimum turnover tax', 'USD m',
       lambda i: f"=IF({om(i)}>0,{V('Inputs.mtt')}/100*{ref('Operations.nonfuel', i)}*({ref('Tax.red', i)}+{ref('Tax.full', i)})/{om(i)},0)", total=True, py='S.mtt')
TX.row('tax', 'Tax paid = max(CIT, MTT)', 'USD m', lambda i: f"=MAX({ref('Tax.cit', i)},{ref('Tax.mtt', i)})", total=True, py='S.tax')
TX.row('thin_dis', 'Thin-cap disallowance', 'USD m', lambda i: f"={ref('Tax.shl_int', i)}-{ref('Tax.shl_ded', i)}", total=True)

# ========================================================================================
# RESERVES and WATERFALL
# ========================================================================================
RS = Sheet('Reserves', 'S', 'Reserves: MMRA, DSRA, handback reserve, Compensation Account')
RS.row('mmc', 'MMRA contribution (1/6 of next outlay)', 'USD m',
       lambda i: f"=SUM({rngrel('Operations.mm', i + 1, i + 6)})/{V('Inputs.mmra_n')}", total=True, py='S.mm_contr')
RS.row('mmb', 'MMRA balance', 'USD m', lambda i: f"={ref('Reserves.mmb', i, -1)}+{ref('Reserves.mmc', i)}-{ref('Operations.mm', i)}", py='S.mmra_bal')
RS.row('dsra_o', 'DSRA opening', 'USD m',
       lambda i: f"=IF({ref('Time.f_cod', i)}=1,SUM({rng('Funding.dsra')}),{ref('Reserves.dsra_c', i, -1)})", py='S.dsra_open')
RS.row('dsra_d', 'DSRA drawing', 'USD m', lambda i: f"=MIN({ref('Reserves.dsra_o', i)},{ref('Waterfall.short', i)})", total=True, py='S.dsra_draw')
RS.row('dsra_t', 'DSRA top-up', 'USD m',
       lambda i: f"=MIN({ref('Waterfall.cad', i)},MAX(0,{ref('Debt.tgt', i)}-({ref('Reserves.dsra_o', i)}-{ref('Reserves.dsra_d', i)})))", total=True, py='S.dsra_topup')
RS.row('dsra_r', 'DSRA release of excess', 'USD m',
       lambda i: f"=MAX(0,{ref('Reserves.dsra_o', i)}-{ref('Reserves.dsra_d', i)}-{ref('Debt.tgt', i)})", total=True, py='S.dsra_release')
RS.row('dsra_c', 'DSRA closing', 'USD m',
       lambda i: f"=(1-{ref('Time.f_last', i)})*({ref('Reserves.dsra_o', i)}-{ref('Reserves.dsra_d', i)}+{ref('Reserves.dsra_t', i)}-{ref('Reserves.dsra_r', i)})", py='S.dsra_close')
RS.row('hb_c', 'Handback reserve contribution', 'USD m', lambda i: f"=MIN({ref('Waterfall.cash1', i)},{ref('Operations.hb_req', i)})", total=True, py='S.hb_contr')
RS.row('hb_r', 'Handback reserve release at expiry', 'USD m', lambda i: f"={ref('Time.f_last', i)}*({ref('Reserves.hb_b', i, -1)}+{ref('Reserves.hb_c', i)})", total=True, py='S.hb_release')
RS.row('hb_b', 'Handback reserve balance', 'USD m', lambda i: f"={ref('Reserves.hb_b', i, -1)}+{ref('Reserves.hb_c', i)}-{ref('Reserves.hb_r', i)}", py='S.hb_bal')
RS.row('comp', 'Compensation Account (performance LDs held)', 'USD m',
       lambda i: f"={V('Inputs.s_ld_prep')}*IF(AND({tt(i)}>={V('Time.tcod')},{ref('Time.end', i)}<{V('Inputs.d_ldprep')}),{V('Inputs.ld_perf')},0)", py='S.comp_acct')

W = Sheet('Waterfall', 'S', 'Waterfall: CFADS, debt service, reserves, tests, sweeps, distributions')
W.row('cfads', 'CFADS', 'USD m',
      lambda i: f"={ref('Operations.ebitda', i)}-{ref('Tax.tax', i)}-{ref('Operations.dnwc', i)}-{ref('Reserves.mmc', i)}+{ref('Operations.mm', i)}+{ref('Operations.inv_rel', i)}", total=True, py='S.cfads')
W.row('copen', 'Cash brought forward (lock-up and trapped cash)', 'USD m',
      lambda i: (f"=IF({ref('Time.f_cod', i)}=1,INDEX({rng('Funding.ldpool')},1,{V('Time.fe')})+SUM({rng('Funding.codw')}),0)+{ref('Waterfall.lu', i, -1)}+{ref('Waterfall.trap', i, -1)}"), py='S.cash_open')
W.row('avail', 'Cash available for debt service', 'USD m', lambda i: f"={ref('Waterfall.cfads', i)}+{ref('Waterfall.copen', i)}", py='S.avail_cash')
W.row('need', 'Senior debt service and fees due', 'USD m', lambda i: f"={ref('Debt.ds', i)}+{ref('Debt.wfee', i)}", total=True)
W.row('short', 'Debt-service shortfall before DSRA (the DSRA covers debt service only)', 'USD m', lambda i: f"=MIN({ref('Waterfall.need', i)},MAX(0,{ref('Waterfall.need', i)}-{ref('Waterfall.avail', i)}))", total=True)
W.row('unpaid', 'Shortfall after DSRA (must be zero)', 'USD m', lambda i: f"={ref('Waterfall.short', i)}-{ref('Reserves.dsra_d', i)}", total=True, py='S.shortfall')
W.row('cad', 'Cash after debt service', 'USD m', lambda i: f"=MAX(0,{ref('Waterfall.avail', i)}-{ref('Waterfall.need', i)})", py='S.cash_after_ds')
W.row('cash1', 'Cash after DSRA movements', 'USD m', lambda i: f"={ref('Waterfall.cad', i)}-{ref('Reserves.dsra_t', i)}+{ref('Reserves.dsra_r', i)}")
W.row('cash', 'Cash available for distribution tests', 'USD m', lambda i: f"={ref('Waterfall.cash1', i)}-{ref('Reserves.hb_c', i)}+{ref('Reserves.hb_r', i)}")
W.sec('Ratios and tests')
W.row('dscr', 'DSCR, period', 'x', lambda i: f"=IF({ref('Debt.ds', i)}>{V('Inputs.eps')},{ref('Waterfall.cfads', i)}/{ref('Debt.ds', i)},0)", fmt='0.0000', py='S.dscr')
W.row('dh', 'DSCR, historic 12 months (cash basis)', 'x',
      lambda i: (f"=IF({ref('Debt.ds', i)}>{V('Inputs.eps')},IF({ref('Debt.ds', i, -1)}>{V('Inputs.eps')},({ref('Waterfall.cfads', i)}+{ref('Waterfall.cfads', i, -1)})/({ref('Debt.ds', i)}+{ref('Debt.ds', i, -1)}),{ref('Waterfall.dscr', i)}),0)"), fmt='0.0000', py='S.dscr_hist')
W.row('frep', 'First repayment made', 'flag', lambda i: f"=IF(SUM({rng('Debt.prin', 0, i).replace('$' + C(i), C(i))})>{V('Inputs.eps')},1,0)", fmt='0')
W.row('eod', 'Event of default (historic DSCR < 1.10x)', 'flag',
      lambda i: f"=IF(AND({ref('Debt.ds', i)}>{V('Inputs.eps')},{ref('Waterfall.dh', i)}<{V('Inputs.eod_dscr')}),1,0)", fmt='0', py='S.eod')
W.row('waived', 'Tests waived', 'flag', lambda i: f"={ref('Time.f_waived', i)}", fmt='0')
W.row('inw', 'Waiver regime', 'flag', lambda i: f"={ref('Time.f_inw', i)}", fmt='0')
W.row('rel', 'Lock-up released under the waiver', 'flag',
      lambda i: (f"=MAX({ref('Waterfall.rel', i, -1)},IF(AND({ref('Waterfall.inw', i)}=1,{ref('Time.f_postw', i)}=1,{ref('Waterfall.dh', i)}>={V('Inputs.rel_dscr')},"
                 f"{ref('Time.f_postw', i, -1)}=1,{ref('Waterfall.dh', i, -1)}>={V('Inputs.rel_dscr')},{ref('Reserves.dsra_c', i)}>={ref('Debt.tgt', i)}-{V('Inputs.eps_r')}),1,0))"), fmt='0', py='S.released')
W.row('ok', 'Distributions permitted', 'flag',
      lambda i: (f"=IF(OR(AND({ref('Waterfall.frep', i)}=1,{ref('Waterfall.dh', i)}>={V('Inputs.lu_dscr')},{ref('Reserves.dsra_c', i)}>={ref('Debt.tgt', i)}-{V('Inputs.eps_r')},"
                 f"OR({ref('Waterfall.eod', i)}=0,{ref('Waterfall.waived', i)}=1),{ref('Debt.ds', i)}>{V('Inputs.eps')},OR({ref('Waterfall.inw', i)}=0,{ref('Waterfall.rel', i)}=1)),"
                 f"AND({ref('Time.f_last', i)}=1,{ref('Debt.ds', i)}<={V('Inputs.eps')}),AND({ref('Debt.ds', i)}<={V('Inputs.eps')},{ref('Time.f_ds', i)}=1,{ref('Debt.bo', i)}<{V('Inputs.eps')})),1,0)"), fmt='0', py='S.dist_ok')
W.row('lock', 'Lock-up', 'flag', lambda i: f"=IF(AND({ref('Waterfall.ok', i)}=0,{ref('Waterfall.frep', i)}=1,{ref('Debt.ds', i)}>{V('Inputs.eps')}),1,0)", fmt='0', py='S.lockup')
W.row('cnt', 'Consecutive lock-ups', 'count', lambda i: f"=IF({ref('Waterfall.lock', i)}=1,{ref('Waterfall.cnt', i, -1)}+1,0)", fmt='0', py='S.lu_count')
W.sec('Sweeps and distributions (USD m)')
W.row('lusw', 'Lock-up cash sweep (after two consecutive lock-ups)', 'USD m',
      lambda i: (f"=IF(AND({ref('Waterfall.ok', i)}=0,{ref('Waterfall.cnt', i)}>={V('Inputs.lu_n')},{ref('Waterfall.inw', i)}=0),MIN({ref('Waterfall.cash', i)},"
                 + "+".join(ref('Debt.after_' + k, i) for k in ['E', 'A', 'B', 'C', 'SB']) + "),0)"), total=True, py='S.lu_sweep')
W.row('mpsw', 'Soft mini-perm sweep (50%, commercial tranche, from 2027)', 'USD m',
      lambda i: f"=IF(AND({ref('Waterfall.ok', i)}=1,{ref('Time.f_mp', i)}=1,{V('Inputs.s_miniperm')}=1),MIN({V('Inputs.mp_share')}*{ref('Waterfall.cash', i)},{ref('Debt.after_C', i)}),0)", total=True, py='S.mp_sweep')
W.row('lu', 'Lock-up account, closing', 'USD m',
      lambda i: f"=IF({ref('Waterfall.ok', i)}=0,{ref('Waterfall.cash', i)}-{ref('Waterfall.lusw', i)},0)", py='S.lu_close')
W.row('dist', 'Cash available for distribution', 'USD m', lambda i: f"=IF({ref('Waterfall.ok', i)}=1,{ref('Waterfall.cash', i)}-{ref('Waterfall.mpsw', i)},0)", total=True, py='S.cash_dist')
W.scalar('sc_tot', 'Share capital contributed', 'USD m', f"=SUM({rng('Funding.sc')})", '#,##0.000000')
W.row('shl_o', 'Shareholder loan balance, opening', 'USD m',
      lambda i: f"=IF({tt(i)}<{V('Time.tcod')},0,IF({ref('Time.f_cod', i)}=1,INDEX({rng('Funding.shl_b')},1,{V('Time.fe')}),{ref('Waterfall.shl_c', i, -1)}))", py='S.shl_open')
W.row('sip', 'Shareholder loan interest paid', 'USD m', lambda i: f"={ref('Waterfall.ok', i)}*MIN({ref('Waterfall.dist', i)},{ref('Tax.shl_int', i)})", total=True, py='S.shl_int_paid')
W.row('spr', 'Shareholder loan principal repaid', 'USD m',
      lambda i: f"={ref('Waterfall.ok', i)}*MIN({ref('Waterfall.dist', i)}-{ref('Waterfall.sip', i)},{ref('Waterfall.shl_o', i)}+{ref('Tax.shl_int', i)}-{ref('Waterfall.sip', i)})", total=True, py='S.shl_prin')
W.row('shl_c', 'Shareholder loan balance, closing', 'USD m',
      lambda i: f"={ref('Waterfall.shl_o', i)}+{ref('Tax.shl_int', i)}-{ref('Waterfall.sip', i)}-{ref('Waterfall.spr', i)}", py='S.shl_close')
W.row('dcap', 'Distributable reserves (retained earnings + current profit)', 'USD m',
      lambda i: f"=MAX(0,{ref('Waterfall.re', i, -1)}+{ref('Financials.ni', i)})")
W.row('div0', 'Dividends within distributable reserves', 'USD m',
      lambda i: f"={ref('Waterfall.ok', i)}*MIN({ref('Waterfall.dist', i)}-{ref('Waterfall.sip', i)}-{ref('Waterfall.spr', i)},{ref('Waterfall.dcap', i)})")
W.row('trap0', 'Cash trapped by the dividend restriction', 'USD m',
      lambda i: f"={ref('Waterfall.ok', i)}*({ref('Waterfall.dist', i)}-{ref('Waterfall.sip', i)}-{ref('Waterfall.spr', i)}-{ref('Waterfall.div0', i)})")
W.row('fdist', 'Liquidation distribution at PPA expiry', 'USD m',
      lambda i: f"={ref('Time.f_last', i)}*({ref('Waterfall.trap0', i)}+{ref('Waterfall.lu', i)}+{ref('Reserves.dsra_o', i)}-{ref('Reserves.dsra_d', i)}+{ref('Reserves.dsra_t', i)}-{ref('Reserves.dsra_r', i)})", total=True, py='S.final_dist')
W.row('div', 'Dividends', 'USD m', lambda i: f"={ref('Waterfall.div0', i)}+{ref('Waterfall.fdist', i)}", total=True, py='S.div')
W.row('trap', 'Trapped cash, closing', 'USD m', lambda i: f"=(1-{ref('Time.f_last', i)})*{ref('Waterfall.trap0', i)}", py='S.trap_close')
W.row('re', 'Retained earnings, closing', 'USD m', lambda i: f"=IF({tt(i)}<{V('Time.tcod')},0,{ref('Waterfall.re', i, -1)}+{ref('Financials.ni', i)}-{ref('Waterfall.div', i)})", py='S.re')
W.row('edist', 'Distributions to shareholders (SHL interest + principal + dividends)', 'USD m',
      lambda i: f"={ref('Waterfall.sip', i)}+{ref('Waterfall.spr', i)}+{ref('Waterfall.div', i)}", total=True, py='S.equity_dist')

# ========================================================================================
# FINANCIALS
# ========================================================================================
FN = Sheet('Financials', 'S', 'Financials: income statement and balance sheet (IFRS basis, USD functional currency)')
FN.sec('Income statement (USD m)')
FN.row('dep', 'Book depreciation (straight line over the 25-year PPA term)', 'USD m', lambda i: f"={cap_}/{V('Time.ppam')}*{om(i)}", total=True, py='S.book_dep')
FN.row('intx', 'Finance costs (senior, swap, PRI, PCG, fees, SHL interest)', 'USD m',
       lambda i: f"={ref('Debt.sc', i)}+{ref('Debt.wfee', i)}+{ref('Debt.refi_c', i)}-{ref('Debt.unwind', i)}+{ref('Tax.shl_int', i)}", total=True, py='S.int_exp')
FN.row('tnbv', 'Tax written-down value', 'USD m', lambda i: f"={cap_}-SUM({rng('Tax.dep_full', 0, i).replace('$' + C(i), C(i))})", py='S.tax_nbv')
FN.row('bnbv', 'Book value of plant (from COD)', 'USD m', lambda i: f"={cap_}-SUM({rng('Financials.dep', 0, i).replace('$' + C(i), C(i))})", py='S.book_nbv')
FN.row('dt', 'Deferred tax liability (asset if negative)', 'USD m',
       lambda i: f"=IF({tt(i)}>={V('Time.tcod')},{V('Inputs.dt_rate')}/100*({ref('Financials.bnbv', i)}-{ref('Financials.tnbv', i)}-{ref('Tax.pool', i)}),0)", py='S.dt')
FN.row('dtx', 'Deferred tax expense', 'USD m', lambda i: f"={ref('Financials.dt', i)}-{ref('Financials.dt', i, -1)}", total=True, py='S.dt_exp')
FN.row('ni', 'Net income', 'USD m',
       lambda i: f"={ref('Operations.ebitda', i)}-{ref('Financials.dep', i)}-{ref('Financials.intx', i)}-{ref('Tax.tax', i)}-{ref('Financials.dtx', i)}", total=True, py='S.ni')
FN.sec('Balance sheet (USD m, period end)')
cum_m = lambda key, i: f"SUMIFS({rng(key)},{rng('Construction.per')},\"<=\"&{tt(i)})"
FN.row('ppe', 'Plant (construction in progress before COD)', 'USD m',
       lambda i: (f"=IF({tt(i)}>={V('Time.tcod')},{ref('Financials.bnbv', i)},{cum_m('Funding.uses', i)}-{cum_m('Funding.dsra', i)}-{cum_m('Construction.wc', i)}+{cum_m('Funding.shl_i', i)}-{cum_m('Funding.ldrec', i)})"), py='S.ppe')
FN.row('cash', 'Cash in project accounts (DSRA, MMRA, handback, lock-up, trapped, compensation)', 'USD m',
       lambda i: (f"={ref('Reserves.dsra_c', i)}+{ref('Reserves.mmb', i)}+{ref('Reserves.hb_b', i)}+{ref('Waterfall.lu', i)}+{ref('Waterfall.trap', i)}+{ref('Reserves.comp', i)}"
                  f"+IF({tt(i)}<{V('Time.tcod')},{cum_m('Funding.ldrec', i)}-{cum_m('Funding.ldu', i)},0)"), py='S.bs_cash')
FN.row('ar', 'Receivables (incl. overdue)', 'USD m', lambda i: f"={ref('Operations.ar', i)}+{ref('Operations.over', i)}", py='S.bs_ar')
FN.row('inv', 'Spares inventory', 'USD m',
       lambda i: f"=IF({tt(i)}<{V('Time.tcod')},{cum_m('Construction.wc', i)},IF({tt(i)}<{V('Time.lastop')},{V('Inputs.init_wc')}*{V('Inputs.s_capex')},0))", py='S.bs_inv')
FN.row('dta', 'Deferred tax asset', 'USD m', lambda i: f"=MAX(0,-{ref('Financials.dt', i)})", py='S.bs_dta')
FN.row('ta', 'Total assets', 'USD m', lambda i: "=" + "+".join(ref('Financials.' + k, i) for k in ['ppe', 'cash', 'ar', 'inv', 'dta']), py='S.bs_assets')
FN.row('debt', 'Senior debt', 'USD m', lambda i: f"=IF({tt(i)}<{V('Time.tcod')},{cum_m('Funding.debt_draw', i)},{ref('Debt.bc', i)})", py='S.bs_debt')
FN.row('shl', 'Shareholder loans (incl. capitalized interest)', 'USD m',
       lambda i: f"=IF({tt(i)}<{V('Time.tcod')},{cum_m('Funding.shl_c', i)}+{cum_m('Funding.shl_i', i)},{ref('Waterfall.shl_c', i)})", py='S.bs_shl')
FN.row('pay', 'Payables (incl. deferred SNHK/GCK payables)', 'USD m',
       lambda i: "=" + "+".join(ref('Operations.' + k, i) for k in ['pay_gas', 'pay_gta', 'pay_om', 'pay_oth', 'gas_arr']), py='S.bs_pay')
FN.row('dtl', 'Deferred tax liability', 'USD m', lambda i: f"=MAX(0,{ref('Financials.dt', i)})", py='S.bs_dtl')
FN.row('scap', 'Share capital', 'USD m', lambda i: f"={cum_m('Funding.sc', i)}", py='S.bs_sc')
FN.row('reb', 'Retained earnings', 'USD m', lambda i: f"={ref('Waterfall.re', i)}", py='S.bs_re')
FN.row('tle', 'Total liabilities and equity', 'USD m', lambda i: "=" + "+".join(ref('Financials.' + k, i) for k in ['debt', 'shl', 'pay', 'dtl', 'scap', 'reb']), py='S.bs_liab_eq')
FN.row('chk', 'Balance check (assets less liabilities and equity)', 'USD m', lambda i: f"={ref('Financials.ta', i)}-{ref('Financials.tle', i)}", py='S.bs_check')
# v1.4 appended cash flow statement (u09 R4): project accounts = row 'cash' above
FN.gap()
FN.sec('Cash flow statement (USD m; project accounts as in the cash row above)')
FN.row('cf_ebitda', 'EBITDA', 'USD m', lambda i: f"={ref('Operations.ebitda', i)}", total=True, py='S.cf_ebitda')
FN.row('cf_tax', 'Tax paid', 'USD m', lambda i: f"=-{ref('Tax.tax', i)}", total=True, py='S.cf_tax')
FN.row('cf_wc', 'Working capital: increase (negative) and spares release', 'USD m', lambda i: f"=-{ref('Operations.dnwc', i)}+{ref('Operations.inv_rel', i)}", total=True, py='S.cf_wc')
FN.row('cf_mm', 'MMRA net: releases for outlays less contributions', 'USD m', lambda i: f"={ref('Operations.mm', i)}-{ref('Reserves.mmc', i)}", total=True, py='S.cf_mm')
FN.row('cf_cfads', 'CFADS', 'USD m', lambda i: "=" + "+".join(ref('Financials.' + k, i) for k in ['cf_ebitda', 'cf_tax', 'cf_wc', 'cf_mm']), total=True, py='S.cf_cfads')
FN.row('cf_ds', 'Senior debt service and fees', 'USD m', lambda i: f"=-({ref('Debt.ds', i)}+{ref('Debt.wfee', i)})", total=True, py='S.cf_ds')
FN.row('cf_ldin', 'Performance LDs received (Compensation Account)', 'USD m',
       lambda i: f"={ref('Reserves.comp', i)}-{ref('Reserves.comp', i, -1)}+" + "+".join(ref('Debt.ld_' + k, i) for k in ['E', 'A', 'B', 'C', 'SB']), total=True, py='S.cf_ldin')
FN.row('cf_ldp', 'Performance LD prepayment of senior debt', 'USD m', lambda i: "=-(" + "+".join(ref('Debt.ld_' + k, i) for k in ['E', 'A', 'B', 'C', 'SB']) + ")", total=True, py='S.cf_ldp')
FN.row('cf_bond', 'Bond issued, net of refinancing costs', 'USD m', lambda i: f"={ref('Debt.Fn', i)}-{ref('Debt.refi_c', i)}", total=True, py='S.cf_bond')
FN.row('cf_prep', 'Senior debt prepaid from bond proceeds', 'USD m', lambda i: f"=-{ref('Debt.prep', i)}", total=True, py='S.cf_prep')
FN.row('cf_unw', 'Swap unwind receipt', 'USD m', lambda i: f"={ref('Debt.unwind', i)}", total=True, py='S.cf_unw')
FN.row('cf_sw', 'Cash sweeps (lock-up and soft mini-perm)', 'USD m', lambda i: f"=-({ref('Waterfall.lusw', i)}+{ref('Waterfall.mpsw', i)})", total=True, py='S.cf_sw')
FN.row('cf_shl', 'Shareholder loan interest and principal paid', 'USD m', lambda i: f"=-({ref('Waterfall.sip', i)}+{ref('Waterfall.spr', i)})", total=True, py='S.cf_shl')
FN.row('cf_div', 'Dividends', 'USD m', lambda i: f"=-{ref('Waterfall.div', i)}", total=True, py='S.cf_div')
FN.row('cf_dsra', 'DSRA initial funding from the construction budget (COD period)', 'USD m', lambda i: f"={ref('Time.f_cod', i)}*SUM({rng('Funding.dsra')})", total=True, py='S.cf_dsra')
FN.row('cf_cld', 'Construction: delay LDs and DSU received less applied to uses', 'USD m',
       lambda i: f"=SUMIFS({rng('Funding.ldrec')},{rng('Construction.per')},{tt(i)})-SUMIFS({rng('Funding.ldu')},{rng('Construction.per')},{tt(i)})", total=True, py='S.cf_cld')
FN.row('cf_mmr', 'MMRA contributions less releases (held in the project accounts)', 'USD m', lambda i: f"={ref('Reserves.mmc', i)}-{ref('Operations.mm', i)}", total=True, py='S.cf_mmr')
FN.row('cf_net', 'Net cash flow', 'USD m',
       lambda i: "=" + "+".join(ref('Financials.' + k, i) for k in ['cf_cfads', 'cf_ds', 'cf_ldin', 'cf_ldp', 'cf_bond', 'cf_prep', 'cf_unw', 'cf_sw', 'cf_shl', 'cf_div', 'cf_dsra', 'cf_cld', 'cf_mmr', 'cf_codw']), total=True, py='S.cf_net')
FN.row('cf_dsra_memo', 'Memo: DSRA top-ups less drawings and releases (transfers within the project accounts)', 'USD m',
       lambda i: f"={ref('Reserves.dsra_t', i)}-{ref('Reserves.dsra_d', i)}-{ref('Reserves.dsra_r', i)}", total=True, py='S.cf_dsra_memo')
FN.row('cf_dc', 'Change in project-account cash', 'USD m', lambda i: f"={ref('Financials.cash', i)}-{ref('Financials.cash', i, -1)}", total=True, py='S.cf_dc')
FN.row('cf_chk', 'Cash check: change in cash less net cash flow (0)', 'USD m', lambda i: f"={ref('Financials.cf_dc', i)}-{ref('Financials.cf_net', i)}", py='S.cf_chk')
FN.row('cf_codw', 'COD working-capital funding brought into the COD period (standby facility and contingent equity)', 'USD m',
       lambda i: f"={ref('Time.f_cod', i)}*SUM({rng('Funding.codw')})", total=True, py='S.cf_codw')

# ========================================================================================
# RATIOS
# ========================================================================================
RT = Sheet('Ratios', 'S', 'Ratios: DSCR, LLCR, PLCR')
RT.row('rate', 'All-in senior cost per period (financing costs / opening debt)', 'factor',
       lambda i: f"=IF({ref('Debt.bo', i)}>{V('Inputs.eps')},{ref('Debt.sc', i)}/{ref('Debt.bo', i)},0)", fmt='0.0000000', py='S.allin_rate')
RT.scalar('fm', 'Final maturity period', 'index', f"=SUMPRODUCT(MAX(({rng('Debt.bo')}>{V('Inputs.eps')})*{rng('Time.t')}))", '0')
RT.scalar('rfm', 'Rate in final maturity period', 'factor', f"=INDEX({rng('Ratios.rate')},1,{V('Ratios.fm')})", '0.0000000')
RT.row('r2', 'Discount rate used', 'factor', lambda i: f"=IF({ref('Ratios.rate', i)}>0,{ref('Ratios.rate', i)},{V('Ratios.rfm')})", fmt='0.0000000')
RT.row('pvl', 'PV of CFADS to final maturity', 'USD m',
       lambda i: f"=IF({tt(i)}<={V('Ratios.fm')},({ref('Waterfall.cfads', i)}+{nxt('Ratios.pvl', i)})/(1+{ref('Ratios.r2', i)}),0)", py='S.pv_cfads_loan')
RT.row('pvp', 'PV of CFADS to PPA expiry', 'USD m',
       lambda i: f"=IF({tt(i)}<={V('Time.lastop')},({ref('Waterfall.cfads', i)}+{nxt('Ratios.pvp', i)})/(1+{ref('Ratios.r2', i)}),0)")
RT.row('llcr', 'LLCR = (PV CFADS + DSRA) / debt', 'x',
       lambda i: f"=IF({ref('Debt.bo', i)}>{V('Inputs.eps')},({ref('Ratios.pvl', i)}+{ref('Reserves.dsra_o', i)})/{ref('Debt.bo', i)},0)", fmt='0.0000', py='S.llcr_dsra')
RT.row('llcr0', 'LLCR excluding DSRA', 'x', lambda i: f"=IF({ref('Debt.bo', i)}>{V('Inputs.eps')},{ref('Ratios.pvl', i)}/{ref('Debt.bo', i)},0)", fmt='0.0000', py='S.llcr')
RT.row('plcr', 'PLCR = PV CFADS to expiry / debt', 'x', lambda i: f"=IF({ref('Debt.bo', i)}>{V('Inputs.eps')},{ref('Ratios.pvp', i)}/{ref('Debt.bo', i)},0)", fmt='0.0000', py='S.plcr')
RT.scalar('min_dscr', 'Minimum DSCR', 'x', f"=_xlfn.MINIFS({rng('Waterfall.dscr')},{rng('Debt.ds')},\">\"&{V('Inputs.eps')})", '0.0000')
RT.scalar('avg_dscr', 'Average DSCR (debt-service weighted)', 'x', f"=SUMIFS({rng('Waterfall.cfads')},{rng('Debt.ds')},\">\"&{V('Inputs.eps')})/SUM({rng('Debt.ds')})", '0.0000')
RT.scalar('llcr_1', 'LLCR at first debt service period', 'x', f"=INDEX({rng('Ratios.llcr')},1,{V('Time.t1')})", '0.0000')
RT.scalar('plcr_1', 'PLCR at first debt service period', 'x', f"=INDEX({rng('Ratios.plcr')},1,{V('Time.t1')})", '0.0000')
# v1.4 appended (u09 R3): report only, not wired into the waterfall
RT.row('pdscr', 'Projected 12-month DSCR, next two periods (report only)', 'x',
       lambda i: (f"=IF({ref('Debt.ds', i, 1)}>{V('Inputs.eps')},({ref('Waterfall.cfads', i, 1)}+IF({ref('Debt.ds', i, 2)}>{V('Inputs.eps')},{ref('Waterfall.cfads', i, 2)},0))"
                  f"/({ref('Debt.ds', i, 1)}+{ref('Debt.ds', i, 2)}),0)"), fmt='0.0000', py='S.proj_dscr')
RT.row('pflag', 'Projected 12-month DSCR below the lock-up level (flag)', 'flag',
       lambda i: f"=IF(AND({ref('Ratios.pdscr', i)}>0,{ref('Ratios.pdscr', i)}<{V('Inputs.lu_dscr')}),1,0)", fmt='0', py='S.proj_flag')

# ========================================================================================
# RETURNS (combined dated strip: LNTP, 53 months, 57 half-years)
# ========================================================================================
RET = Sheet('Returns', 'X', 'Returns: dated cash flows for XIRR (column J = LNTP 2018-02-05, then months, then half-years)')
def strip(i, mfn, sfn, first):
    if i == 0: return first
    if i <= NM: return mfn(i - 1)
    return sfn(i - 1 - NM)
RET.row('date', 'Cash flow date', 'date', lambda i: strip(i, lambda m: f"={ref('Construction.start', m)}", lambda t: f"={ref('Time.end', t)}", f"={V('Inputs.d_lntp')}"), fmt='yyyy-mm-dd')
RET.row('eq', 'Equity cash flow (contributions negative)', 'USD m',
        lambda i: strip(i, lambda m: f"=-{ref('Funding.eq_cash', m)}", lambda t: f"={ref('Waterfall.edist', t)}", f"=-{V('Inputs.lntp')}"), total=True)
RET.row('pr', 'Project cash flow, post-tax (uses before financing; CFADS)', 'USD m',
        lambda i: strip(i, lambda m: f"=-{ref('Construction.base_total', m)}", lambda t: f"={ref('Waterfall.cfads', t)}", "=0"), total=True)
RET.row('prt', 'Project cash flow, pre-tax', 'USD m',
        lambda i: strip(i, lambda m: f"=-{ref('Construction.base_total', m)}", lambda t: f"={ref('Waterfall.cfads', t)}+{ref('Tax.tax', t)}", "=0"), total=True)
RET.row('cum', 'Cumulative equity cash flow', 'USD m', lambda i: f"={ref('Returns.cum', i, -1) + '+' if i else '='}{ref('Returns.eq', i)}")
RET.scalar('eirr', 'Equity IRR (XIRR)', '%', f"=XIRR({rng('Returns.eq')},{rng('Returns.date')})", '0.0000%', py='R.equity_irr')
RET.scalar('pirr', 'Project IRR, post-tax (XIRR)', '%', f"=XIRR({rng('Returns.pr')},{rng('Returns.date')},{V('Inputs.irr_g')})", '0.0000%', py='R.project_irr')
RET.scalar('pirrt', 'Project IRR, pre-tax (XIRR)', '%', f"=XIRR({rng('Returns.prt')},{rng('Returns.date')},{V('Inputs.irr_g')})", '0.0000%', py='R.project_irr_pretax')
RET.scalar('npv16', 'Equity NPV at 16.0%, at financial close (2018-07-17)', 'USD m',
           f"=XNPV({V('Inputs.npv_r')}/100,{rng('Returns.eq')},{rng('Returns.date')})*(1+{V('Inputs.npv_r')}/100)^(({V('Inputs.d_fc')}-{V('Inputs.d_lntp')})/{V('Inputs.day_kcr')})", '#,##0.000', py='R.equity_npv16_at_fc')

# ========================================================================================
# CHECKS and OUTPUTS
# ========================================================================================
CK = Sheet('Checks', None, 'Checks: every check shows 0 when passing')
CHK = [
    ('c_su', 'Sources less uses (construction)', f"=IF(ABS(SUM({rng('Funding.debt_draw')})+SUM({rng('Funding.eq')})+SUM({rng('Funding.ldu')})-SUM({rng('Funding.uses')}))<={V('Inputs.eps_r')},0,SUM({rng('Funding.debt_draw')})+SUM({rng('Funding.eq')})+SUM({rng('Funding.ldu')})-SUM({rng('Funding.uses')}))"),
    ('c_dc', 'Committed debt drawn in full (FC-type, Monte Carlo off), USD m', f"=IF(AND({V('Inputs.s_constr')}=1,{MCON()}=0),IF(ABS(SUM({rng('Funding.bdebt')})-{V('Funding.D')})<={V('Inputs.eps_r')},0,SUM({rng('Funding.bdebt')})-{V('Funding.D')}),0)"),
    ('c_cf', 'Closed-form T less live T (re-grossed cases), USD m', f"=IF({V('Inputs.s_mode')}<>1,IF(ABS({V('Funding.T_aff')}-{V('Funding.T')})<={V('Inputs.eps_r')},0,{V('Funding.T_aff')}-{V('Funding.T')}),0)"),
    ('c_bs', 'Balance sheet balances (max abs difference)', f"=IF(MAX(MAX({rng('Financials.chk')}),-MIN({rng('Financials.chk')}))<={V('Inputs.eps_r')},0,MAX(MAX({rng('Financials.chk')}),-MIN({rng('Financials.chk')})))"),
    ('c_sf', 'No unpaid debt service after DSRA', f"=IF(ABS(SUM({rng('Waterfall.unpaid')}))<={V('Inputs.eps_r')},0,SUM({rng('Waterfall.unpaid')}))"),
    ('c_dr', 'Debt repaid by final maturity', f"=IF(ABS(INDEX({rng('Debt.bc')},1,COLUMNS({rng('Debt.bc')})))<={V('Inputs.eps_r')},0,INDEX({rng('Debt.bc')},1,COLUMNS({rng('Debt.bc')})))"),
    ('c_sc', 'FC base: live sculpting equals contract profile (max abs, USD m)', f"=IF({MCON()}=1,0,IF(MAX(MAX({rng('Debt.sdiff')}),-MIN({rng('Debt.sdiff')}))<={V('Inputs.tol_sc')},0,MAX(MAX({rng('Debt.sdiff')}),-MIN({rng('Debt.sdiff')}))))"),
    ('c_ds', 'FC base: debt not above DSCR capacity or gearing cap', f"=IF(AND({V('Inputs.Scenario')}=1,{MCON()}=0),IF({V('Funding.D')}<=MIN({V('Debt.capacity')},{V('Debt.gearcap')})+{V('Inputs.eps_r')},0,1),0)"),
    ('c_vat', 'VAT facility within limit', f"=IF(MAX({rng('Construction.vat_bal')})<={V('Inputs.vat_limit')},0,1)"),
    ('c_sb', 'Standby and contingent equity within commitments', f"=IF(AND(SUM({rng('Funding.sbd')})<={V('Inputs.sb_commit')}+{V('Inputs.eps_r')},SUM({rng('Funding.ced')})<={V('Inputs.ce')}+{V('Inputs.eps_r')}),0,1)"),
    ('c_eca', 'ECA tranche within cap', f"=IF({V('Inputs.sh_E')}*{V('Funding.D')}<={V('Inputs.eca_cap')},0,1)"),
    ('c_mm', 'MMRA never negative', f"=IF(MIN({rng('Reserves.mmb')})>=-{V('Inputs.eps_r')},0,1)"),
]
for k, lab, f_ in CHK:
    CK.scalar(k, lab, 'check', f_, '0.0000')
CHK2 = [   # v1.4 appended checks (u09 R1, R4, R11, R12, R6), rows 20 to 25
    ('c_tom', 'Time: operating months sum to the PPA term', lambda: f"=SUM({rng('Time.om')})-{V('Time.ppam')}"),
    ('c_tcm', 'Construction flags sum to construction months', lambda: f"=SUM({rng('Construction.f_con')})-{V('Time.nc')}"),
    ('c_cash', 'Cash flow statement reconciles to project-account cash (max abs, USD m)',
     lambda: f"=IF(MAX(MAX({rng('Financials.cf_chk')}),-MIN({rng('Financials.cf_chk')}))<={V('Inputs.eps_r')},0,MAX(MAX({rng('Financials.cf_chk')}),-MIN({rng('Financials.cf_chk')})))"),
    ('c_ecat', 'ECA tests pass on the ECA-covered tranche\'s contractual schedule (number of failed tests)',
     lambda: (f"=({V('Debt.eca_ten')}>{V('Inputs.eca_tenor')})+({V('Debt.eca_wal')}>{V('Inputs.eca_wal')})+({V('Debt.eca_max')}>{V('Inputs.eca_max')}/100)"
              f"+({V('Debt.eca_fm')}>{V('Inputs.eca_m')})+({V('Debt.eca_24')}<{V('Inputs.eca_min')}/100)")),
    ('c_mmw', 'MMRA window equals the input number of periods', lambda: f"=COLUMNS(Operations!$K${SHEETS['Operations'].key['mm']}:$P${SHEETS['Operations'].key['mm']})-{V('Inputs.mmra_n')}"),
    ('c_out', 'Outputs: live dashboard equals the pasted row of the selected scenario', lambda: f"={V('Outputs.o_cmp')}"),
]
CK.scalar('total', 'Sum of checks (0 = all pass)', 'check', lambda: "=" + "+".join(f"ABS({V('Checks.' + k)})" for k, _, _ in CHK + CHK2), '0.0000')
for k, lab, f_ in CHK2:
    CK.scalar(k, lab, 'check', f_, '0.0000')

OUT = Sheet('Outputs', None, 'Outputs: dashboard for the selected scenario')
OUTS = [
    ('o_T', 'Total funding requirement', 'USD m', f"={V('Funding.T')}"),
    ('o_D', 'Senior debt (four tranches)', 'USD m', f"={V('Funding.D')}"),
    ('o_E', 'Equity (incl. LNTP)', 'USD m', f"=SUM({rng('Funding.eq')})"),
    ('o_G', 'Gearing (debt incl. standby / total funding)', '%', f"=SUM({rng('Funding.debt_draw')})/{V('Funding.T')}"),
    ('o_idc', 'Interest during construction incl. swap and PRI', 'USD m', f"=SUM({rng('Funding.idc_E')})+SUM({rng('Funding.idc_A')})+SUM({rng('Funding.idc_B')})+SUM({rng('Funding.idc_C')})+SUM({rng('Funding.sbi')})+SUM({rng('Funding.swap')})+SUM({rng('Funding.pri')})"),
    ('o_fees', 'Commitment, upfront and agency fees', 'USD m', f"=SUM({rng('Funding.cfee')})+SUM({rng('Funding.sbf')})+SUM({rng('Funding.upf')})+SUM({rng('Funding.agy')})"),
    ('o_prem', 'ECA premium', 'USD m', f"=SUM({rng('Funding.prem')})"),
    ('o_dsra', 'DSRA initial funding', 'USD m', f"=SUM({rng('Funding.dsra')})"),
    ('o_sb', 'Standby drawn', 'USD m', f"=SUM({rng('Funding.sbd')})"),
    ('o_ce', 'Contingent equity drawn', 'USD m', f"=SUM({rng('Funding.ced')})"),
    ('o_min', 'Minimum DSCR', 'x', f"={V('Ratios.min_dscr')}"),
    ('o_avg', 'Average DSCR', 'x', f"={V('Ratios.avg_dscr')}"),
    ('o_llcr', 'LLCR at first debt service period (incl. DSRA)', 'x', f"={V('Ratios.llcr_1')}"),
    ('o_plcr', 'PLCR at first debt service period', 'x', f"={V('Ratios.plcr_1')}"),
    ('o_eirr', 'Equity IRR', '%', f"={V('Returns.eirr')}"),
    ('o_pirr', 'Project IRR, post-tax', '%', f"={V('Returns.pirr')}"),
    ('o_npv', 'Equity NPV at 16.0% (at FC)', 'USD m', f"={V('Returns.npv16')}"),
    ('o_chk', 'All checks', 'check', f"={V('Checks.total')}"),
]
for k, lab, un, f_ in OUTS:
    OUT.scalar(k, lab, un, f_, '0.0000%' if un == '%' else '#,##0.0000')
# v1.4 appended (u09 R6): fifteen-scenario results pasted from the mirror, and a compare row
OUT.gap()
OUT_STAMP = OUT.r; OUT.r += 1          # stamp line
OUT_HDR = OUT.r; OUT.r += 1            # column headings
OUT_T0 = OUT.r; OUT.r += 15            # scenarios 1 to 15
OUT.gap()
def _cmp():
    terms = []
    for j, (k, _, _, _) in enumerate(OUTS[:-1]):
        col = L(FC0 + j)
        terms.append(f"ABS({V('Outputs.' + k)}-INDEX(${col}${OUT_T0}:${col}${OUT_T0 + 14},{V('Inputs.Scenario')}))")
    x = "MAX(" + ",".join(terms) + ")"
    return f"=IF({MCON()}=1,0,IF({x}<={V('Inputs.eps_r')},0,{x}))"
OUT.scalar('o_cmp', 'Live dashboard (rows above) less the pasted row of the selected scenario (max abs; 0 = match)', 'check', _cmp, '0.000000')

def pasted_results():
    out = []
    for i in range(1, 16):
        p = cp.scen(i, errs=set(ERR)) if ERR else cp.scen(i)
        try:
            R = cp.run(p)
        except RuntimeError:
            out.append([None] * (len(OUTS) - 1)); continue
        f = R['f']; S = R['S']; st = cp.dscr_stats(R); sm = lambda k: float(np.sum(f[k])) if k in f else 0.0
        out.append([float(f['T']), float(f['D']), sm('equity'), sm('debt_draw') / float(f['T']),
                    sm('idc_ECA') + sm('idc_A') + sm('idc_B') + sm('idc_COM') + sm('sb_int') + sm('swap') + sm('pri'),
                    sm('cfee') + sm('sb_cfee') + sm('upfront') + sm('agency'), sm('eca_prem'), sm('dsra'), sm('sb_draw'), sm('ce_draw'),
                    st['min_dscr'], st['avg_dscr'], float(S['llcr_dsra'][R['t1']]), float(S['plcr'][R['t1']]),
                    float(R['equity_irr']), float(R['project_irr']), float(R['equity_npv16_at_fc'])])
    return out

COVER = Sheet('Cover', None, 'Case P companion model')

# ========================================================================================
# WRITE
# ========================================================================================
ORDER = ['Cover', 'Inputs', 'Time', 'Construction', 'Operations', 'Tax', 'Funding', 'Debt', 'Reserves',
         'Waterfall', 'Financials', 'Ratios', 'Returns', 'Checks', 'Outputs']

def input_values():
    """Values for the input rows."""
    v = {}
    sc = {i: cp.scen(i) for i in range(1, 16)}
    for k, lab, un, fn in SCN_PARAMS:
        v[k + '_tbl'] = [fn(sc[i]) for i in range(1, 16)]
    us_a, kc_a = cp.CPI['ACT']; us_f, kc_f = cp.CPI['FC']; us_r, kc_r = cp.CPI['CODRF']
    v['A_yr'] = YEARS
    v['A_us_fc'] = [us_f[y] for y in YEARS]; v['A_kc_fc'] = [kc_f[y] for y in YEARS]
    v['A_us_act'] = [us_a[y] for y in YEARS]; v['A_kc_act'] = [kc_a[y] for y in YEARS]
    v['A_us_rf'] = [us_r[y] for y in YEARS]; v['A_kc_rf'] = [kc_r[y] for y in YEARS]
    v['A_pol_act'] = [cp.POLICY_ACT.get(y, 15.5) for y in YEARS]
    v['S_base_fc'] = cp.FC_FWD; v['S_base_act'] = cp.ACT_BASE; v['S_base_rf'] = cp.RF_BASE
    v['S_fx_act'] = cp.FX_ACT_GIVEN
    ov = [0.0] * NS
    for k_, val in cp.INP['events']['offtaker_crisis']['overdue_receivables_usd_m_period_end'].items():
        ov[[t for t in range(NS) if cp.S_END[t] == date.fromisoformat(k_)][0]] = val
    v['S_overdue'] = ov
    fl_ = [0.0] * NS
    for k_, val in cp.INP['events']['offtaker_crisis']['fx_conversion_losses_usd_m'].items():
        fl_[cp.tix(k_)] = val
    v['S_fxloss'] = fl_
    ls = [0.0] * NS; ls[cp.tix('2024H1')] = 3 / 15; ls[cp.tix('2024H2')] = 6 / 15; ls[cp.tix('2025H1')] = 6 / 15
    v['S_lpi_sh'] = ls
    v['S_prof_fc'] = K['prof_FC']; v['S_prof_cod'] = K['prof_COD']; v['S_prof_bond'] = K['prof_BOND']
    v['S_N_s'] = K['N_s']
    v['S_disp_act'] = [cp.ACT_DISPATCH.get(cp.S_LABEL[t], 0.0) for t in range(NS)]
    v['S_av8'] = cp.INP['plant']['availability_profile_pct_by_operating_year_cycle']['values']
    v['M_epc_fc'] = cp.EPC_FC; v['M_epc_act'] = cp.EPC_ACT; v['M_own_fc'] = cp.OWN_FC
    ovr = np.zeros(NM)
    for _, amt, m0, n in cp.OVERRUN_TIMING:
        ovr[m0:m0 + n] += amt / n
    v['M_ovr'] = list(ovr); v['M_N_m'] = K['N_m']
    return v

def build(path, scenario=1, mc_run=0):
    wb = Workbook(); wb.remove(wb.active)
    vals = input_values()
    for name in ORDER:
        S = SHEETS[name]; ws = wb.create_sheet(name); CUR['sheet'] = name
        ws['A1'] = 'Case P: Belanou Combined Cycle Power Project, Republic of Kessara'; ws['A1'].font = Font(bold=True, size=13)
        ws['A2'] = S.title
        ws['A3'] = 'Units in column E; constants in column F; row totals in column G; first period in column J. Inputs: blue on yellow. Links from other sheets: green.'
        for col, w in zip('ABCDEFGHI', [2, 2, 2, 58, 12, 14, 14, 2, 2]):
            ws.column_dimensions[col].width = w
        hdr = 5
        ws.cell(4, 4, 'Label').font = BOLD; ws.cell(4, 5, 'Unit').font = BOLD; ws.cell(4, 6, 'Constant').font = BOLD; ws.cell(4, 7, 'Total').font = BOLD
        if S.tl in ('S', 'M', 'X'):
            ws.cell(hdr, 4, {'S': 'Period ending', 'M': 'Month', 'X': 'Flow'}[S.tl]).font = BOLD
            for i in range(S.n):
                c = ws.cell(hdr, FC0 + i)
                if S.tl == 'S': c.value = cp.S_LABEL[i]
                elif S.tl == 'M': c.value = cp.M_START[i].strftime('%Y-%m')
                else: c.value = 'LNTP' if i == 0 else (cp.M_START[i - 1].strftime('%Y-%m') if i <= NM else cp.S_LABEL[i - 1 - NM])
                c.font = BOLD; c.fill = HEAD
                ws.column_dimensions[L(FC0 + i)].width = 11
        if name == 'Inputs':
            ws.cell(hdr, 4, 'Scenario table: columns J-X = scenarios 1-15; semiannual rows: columns = periods; annual rows: columns = years 2015+').font = BOLD
        if name == 'Cover':
            lines = [
                'Companion model for Chapters 39-45. Python mirror: model/case_p.py (source of truth).',
                'Select the scenario on the Inputs sheet (cell named Scenario):',
            ] + [f"  {i}: {cp.SCENARIOS[i]['name']}" for i in range(1, 16)] + [
                '',
                'Circularity: none. IDC/fee/premium/DSRA gross-up is solved in closed form on the Funding sheet',
                '(balance = alpha + beta x T; T = alpha/(g - beta)). Sculpting with tax uses the contractual',
                'repayment profile on Inputs; the Debt sheet recomputes the sculpted profile live and the',
                'Checks sheet reports the difference (Python iterates the profile to convergence, tolerance USD 1,000).',
                'Sheets: ' + ', '.join(ORDER),
                'Sign convention: costs stored positive and subtracted explicitly.',
                'Monte Carlo (Inputs F311): the draw table is pasted from case_p.py (seed 20180717, P-F42 parameters); the per-run results beside it are pasted from the mirror with a stamp (no native data table: one could not be generated and verified without macros).',
            ]
            for j, t_ in enumerate(lines):
                ws.cell(5 + j, 4, t_)
            # v1.4 (u09 R2): master check link in row 22
            ws.cell(22, 4, 'Master check (0 = all pass)').font = BOLD
            c = ws.cell(22, 6, f"=Checks!$F${SHEETS['Checks'].key['total']}"); c.number_format = '0.0000'
            ws.conditional_formatting.add('F22', CellIsRule(operator='notEqual', formula=['0'], fill=RED))
        if name == 'Inputs':
            DR = cp.mc_draws()
            ws.cell(MC_R0 - 1, FC0, 'Draw table: availability shocks OY1-OY26 (points), dispatch (%), heat-rate degradation (% a year), FX drift (factor)').font = BOLD
            for rr in range(MC_N):
                ws.cell(MC_R0 + rr, 4, f'Run {rr + 1}')
                for j in range(MC_NY + 3):
                    c = ws.cell(MC_R0 + rr, FC0 + j, float(DR[rr, j])); c.font = BLUE; c.fill = YEL
            if cp.MC_RESULTS is None or len(cp.MC_RESULTS) != MC_N:
                cp.monte_carlo()
            c0 = FC0 + MC_NY + 4
            ws.cell(MC_R0 - 2, c0, 'Per-run results pasted from case_p.py v1.4 (2026-10-03; P-F42), not live: min DSCR, min historic DSCR, equity IRR, historic DSCR < 1.20x, < 1.10x').font = BOLD
            for j, h in enumerate(['Min DSCR', 'Min hist DSCR', 'Equity IRR', 'Lock-up (<1.20x)', 'Default (<1.10x)']):
                ws.cell(MC_R0 - 1, c0 + j, h).font = BOLD
            for rr in range(MC_N):
                for j in range(5):
                    c = ws.cell(MC_R0 + rr, c0 + j, float(cp.MC_RESULTS[rr, j])); c.font = BLUE; c.fill = YEL
        if name == 'Outputs':
            ws.cell(OUT_STAMP, 4, 'Fifteen-scenario results pasted from case_p.py (model version 1.4, run 2026-10-03); compare row below and Checks row 25').font = BOLD
            for j, (k, lab, un, _) in enumerate(OUTS[:-1]):
                ws.cell(OUT_HDR, FC0 + j, lab).font = BOLD
            ws.cell(OUT_HDR, 4, 'Scenario').font = BOLD
            for rr, vals_ in enumerate(pasted_results()):
                ws.cell(OUT_T0 + rr, 4, f"{rr + 1}: {cp.SCENARIOS[rr + 1]['name']}")
                for j, x in enumerate(vals_):
                    if x is None: continue
                    c = ws.cell(OUT_T0 + rr, FC0 + j, x); c.font = BLUE; c.fill = YEL
                    c.number_format = '0.0000%' if OUTS[j][2] == '%' else '#,##0.0000'
        for kind, d, r in S.rows:
            if kind == 'sec':
                ws.cell(r, 2, d).font = BOLD
                continue
            ws.cell(r, 4, d['label']); ws.cell(r, 5, d['unit'])
            if kind == 'scalar':
                c = ws.cell(r, 6)
                if d['inp']:
                    val = d['value'] if d['key'] != 'Scenario' else scenario
                    if d['key'] == 'D_c': val = K['D']
                    if d['key'] == 'E_c': val = K['E']
                    if d['key'] == 'mc_run': val = mc_run
                    c.value = val; c.font = BLUE; c.fill = YEL
                elif d['value'] is None and d['key'].startswith('s_'):
                    tr = S.key[d['key'] + '_tbl']
                    c.value = f"=INDEX($J${tr}:$X${tr},1,Scenario)"
                elif d['key'] == 'lastop':
                    c.value = f"=SUMPRODUCT({rng('Time.f_last')},{rng('Time.t')})"
                else:
                    c.value = d['value']() if callable(d['value']) else d['value']
                c.number_format = d['fmt']
                continue
            # row
            if d['inp']:
                arr = vals.get(d['key'])
                if arr is not None:
                    for i, x in enumerate(arr):
                        c = ws.cell(r, FC0 + i, float(x) if not isinstance(x, (int,)) else x)
                        c.font = BLUE; c.fill = YEL
                continue
            for i in range(S.n):
                f_ = d['fn'](i)
                c = ws.cell(r, FC0 + i, f_)
                c.number_format = d['fmt']
                if f_.startswith('=') and '!' in f_ and f_.count('!') == 1 and not any(op in f_[1:] for op in '+-*/(,'):
                    c.font = GREEN
            if d['total']:
                ws.cell(r, 7, f"=SUM({C(0)}{r}:{C(S.n - 1)}{r})").number_format = d['fmt']
        ws.freeze_panes = 'J6' if S.tl else 'A5'
    # defined name for scenario
    wb.defined_names['Scenario'] = DefinedName('Scenario', attr_text=f"Inputs!$F${SHEETS['Inputs'].key['Scenario']}")
    # conditional format on Checks
    ws = wb['Checks']
    ws.conditional_formatting.add(f"F7:F{SHEETS['Checks'].r}", CellIsRule(operator='notEqual', formula=['0'], fill=RED))
    wb.calculation.fullCalcOnLoad = True
    wb.save(path)

def rowmap():
    """key -> (sheet, row, ncols, py) for verification."""
    out = {}
    for name in ORDER:
        S = SHEETS[name]
        for kind, d, r in S.rows:
            if kind == 'sec': continue
            out[f"{name}.{d['key']}"] = (name, r, S.n if kind == 'row' else 0, d.get('py'))
    return out

ERR_ROWS = {
    'E1': ['Operations.avf'], 'E2': ['Operations.eoh'], 'E3': ['Operations.us_tar', 'Operations.kc_tar'],
    'E4': ['Funding.rr', 'Funding.idc_E', 'Funding.idc_A', 'Funding.idc_B', 'Funding.idc_C', 'Funding.d1_E', 'Funding.d1_A', 'Funding.d1_B', 'Funding.d1_C', 'Debt.r_E', 'Debt.r_A', 'Debt.r_B', 'Debt.r_C'],
    'E5': ['Tax.hol', 'Tax.red', 'Tax.dep_hol'], 'E6': ['Tax.pool'], 'E7': ['Funding.g', 'Funding.bdebt', 'Funding.bfund'],
    'E8': ['Debt.pvc', 'Debt.sds'], 'E9': ['Operations.fuel_rev'],
    'E10': ['Funding.const', 'Funding.swap', 'Funding.d0', 'Debt.swap', 'Debt.tgt', 'Debt.wrate'],
}

def build_audit(path):
    """Chapter 44 exercise copy: the ten seeded errors E1-E10, contract terms from the erroneous sizing."""
    from openpyxl import load_workbook
    _, c, res = cp.audit_case(cp.ERR_LIST)
    old = dict(cp.CONTRACT)
    cp.CONTRACT.update(c); ERR.clear(); ERR.update(cp.ERR_LIST)
    try:
        build(path, 1)
        rm = rowmap()
    finally:
        ERR.clear(); cp.CONTRACT.clear(); cp.CONTRACT.update(old)
    wb = load_workbook(path)
    ws = wb.create_sheet('AuditKey')
    ws['A1'] = 'Audit exercise key (Chapter 44): sponsor model version 0.9 with ten seeded errors. Do not distribute with the exercise.'
    ws['A1'].font = Font(bold=True)
    ws['A2'] = 'Contract terms on the Inputs sheet come from sizing this erroneous model. Effects (P-F17) are from case_p.py: each error alone, re-sized.'
    hdr = ['ID', 'Seeded error', 'Cells (sheet, row)', 'Senior debt (USD m)', 'Change vs correct', 'Min DSCR base', 'Min DSCR downside', 'Equity IRR', 'Binding']
    for j, h in enumerate(hdr): ws.cell(4, 1 + j, h).font = BOLD
    import json as _j
    o = _j.load(open(os.path.join(HERE, 'outputs_case_p.json')))
    R = o['figures']['P-F17']['results']
    for r_, e in enumerate(['correct'] + cp.ERR_LIST + ['ALL']):
        x = R[e]
        cells = '; '.join(f"{k.split('.')[0]} row {rm[k][1]}" + (' (col F)' if rm[k][2] == 0 else '') for k in ERR_ROWS.get(e, [])) if e in ERR_ROWS else ('all of the above' if e == 'ALL' else '')
        vals = [e, x.get('description', 'correct model'), cells, round(x['senior_debt'], 2), round(x.get('delta_senior_debt', 0.0), 2),
                round(x['min_dscr_base'], 3), round(x['min_dscr_downside'], 3), round(x['equity_irr'] * 100, 2), x['binding']]
        for j, v in enumerate(vals): ws.cell(5 + r_, 1 + j, v)
    ws.column_dimensions['B'].width = 70; ws.column_dimensions['C'].width = 60
    wb.save(path)
    # reader copy without the key (u09 R8, Chapter 44)
    wb.remove(wb['AuditKey'])
    os.makedirs(os.path.join(HERE, 'exercises'), exist_ok=True)
    wb.save(os.path.join(HERE, 'exercises', 'Case_P_Model_AuditExercise_reader.xlsx'))
    return c

if __name__ == '__main__':
    p = os.path.join(HERE, 'Case_P_Model.xlsx')
    build(p, 1)
    print('written', p)
    if os.path.exists(os.path.join(HERE, 'outputs_case_p.json')):
        build_audit(os.path.join(HERE, 'Case_P_Model_AuditExercise.xlsx'))
        print('written audit exercise copy')
