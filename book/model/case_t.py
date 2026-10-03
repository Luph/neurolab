"""Case T reference model: the Merrick Link toll road PPP (Brannock, Ardmore).

Python mirror and computational source of truth for Case T. Pure Python plus numpy.

Reads  model/inputs_case_t.json
Writes model/outputs_case_t.json   (period series and scalars, keyed by scenario and name)
       model/case_t_report.md      (human-readable summary tables)

Timeline (one column per period, mirrored by the Excel workbook from column J):
  t = 0        2015-05-27 to 2015-06-30 (construction stub, financial close 2015-05-27)
  t = 1..15    calendar quarters 2015Q3 to 2019Q1 (construction)
  t = 16       2019-03-31 to 2019-06-30 (first operating period; contains the actual opening)
  t = 17..96   semiannual periods 2019H2 to 2059H1 (operations; concession ends 2053-05-26,
               or 2059-05-26 after the 2023 restructuring)

Scenarios (Inputs!Scenario in the workbook):
  1 Bid base (Pellow traffic), financing locked from scenario 2
  2 Banking case (Ridgeway traffic): LIVE debt sizing; the financing used by every other run
  3 Downside, locked financing
  4 Actual history: actual traffic and events to 2026H1, Ridgeway 2023 case after; locked
    original financing and locked restructured profiles from scenario 5
  5 Restructuring case: actual history to 2023H2, Ridgeway 2023 case from 2024; LIVE sculpting
    of the Restructured Senior Notes and the restructured NILO loan
  6 Retender valuation: actual history to 2022H1, retender traffic case after (fair value at
    June 30, 2022, original concession terms)
  7-13 Sensitivities on the bid base: traffic -10%, ramp-up one year slower, toll escalation
    CPI only, opex +10%, lifecycle +20%, interest +100 bp on refinancing, heavy vehicles -2 pts

Circularities and how they are resolved
  * Construction funding: IDC, commitment fees, upfront fees, bond negative carry, bridge
    interest, the DSRA and the ramp-up interest account all depend on the debt amounts, which
    depend on the funding requirement (gearing cap, equity share, NILO remainder).
  * Debt sizing: CFADS depends on tax, tax on interest, interest on the debt sized from CFADS.
  * Sculpting: the sculpting divisor s (senior), k (NILO) and s_n (restructured notes) are
    fixed points: s = PV(CFADS in amortizing periods) / (D - PV(interest in interest-only periods)).
  All are solved by Gauss-Seidel iteration of the whole model until the largest change in any
  tracked value is below TOL (ARD 1e-9 million). The workbook uses Excel/LibreOffice
  iterative calculation with a circuit-breaker switch (Inputs!Circ) and converges to the same
  fixed point.
"""
import json
import math
import os
import datetime as dt

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
INP = json.load(open(os.path.join(HERE, "inputs_case_t.json")))
TOL = 1e-9
MAX_PASSES = 400

# ----------------------------------------------------------------------------------------
# Constants from the inputs file (names mirror the Inputs sheet)
# ----------------------------------------------------------------------------------------
D_ = dt.date
FC_DATE = D_(2015, 5, 27)
CON_END = D_(2019, 3, 31)
OPEN_SCHED = D_(2019, 3, 31)
OPEN_ACT = D_(2019, 5, 6)
CONC_ORIG = D_(2053, 5, 26)
CONC_EXT = D_(2059, 5, 26)
RESTR_DATE = D_(2023, 12, 31)
FIRST_REP = D_(2021, 6, 30)
FINAL_REP = D_(2048, 12, 31)
MARGIN_STEP = D_(2020, 5, 27)
MINIPERM_MAT = D_(2022, 5, 27)
HEDGE_END = D_(2035, 6, 30)
NILO_CAP_END = D_(2024, 3, 31)
NILO_FIRST = D_(2024, 6, 30)
NILO_FINAL = D_(2052, 12, 31)
NILO_R_FIRST = D_(2031, 6, 30)
NILO_R_FINAL = D_(2058, 12, 31)
NILO_PIK_END = D_(2030, 12, 31)
NOTES_FINAL = D_(2052, 12, 31)
NOTES_SWEEP_END = D_(2030, 12, 31)
DEFAULT_TEST_START = D_(2020, 12, 31)
FV_DATE = D_(2022, 6, 30)
AUTH_DATE = D_(2022, 6, 30)

cap = INP["capex_ard_m"]
fin = INP["financing_at_close"]
ops_in = INP["opex_ard_m_2015_prices"]
tolls = INP["tolls"]
traf = INP["traffic_k_trips_per_day"]
ev = INP["events"]["restructuring"]
MA = INP["modeler_assumptions"]

DC_PRICE = cap["dc_contract_price"]
DC_PROFILE = [v / 100.0 for v in cap["dc_payment_profile_pct_by_quarter"].values()]  # sums to 95%
RET_AT_COMPLETION = cap["dc_retention_release"]["at_completion_pct"] / 100.0
RET_DEFECTS = cap["dc_retention_release"]["end_of_defects_period_24_months_pct"] / 100.0
DEV = cap["development_and_bid_costs_reimbursed"]
SPVC = cap["spv_costs_during_construction"]
INS_C = cap["insurance_during_construction"]
CERT = cap["independent_certifier_spv_share"]
ADV = cap["lenders_advisors_and_legal"]
CONT = cap["spv_contingency"]
CONTRIB_BID = INP["state_contribution"]["amount_ard_m"]
BRIDGE_MARGIN = INP["state_contribution"]["bridge"]["margin_pct"] / 100.0
BRIDGE_FEE = INP["state_contribution"]["bridge"]["upfront_fee_pct"] / 100.0

EQ_SHARE = fin["equity"]["target_share_of_funding_net_of_state_contribution_pct"] / 100.0
SHARE_CAP = fin["equity"]["form"]["share_capital_pct"] / 100.0
SHL_RATE = INP["tax"]["shareholder_loan_rate_pct"] / 100.0
TARGET_IRR = fin["equity"]["bid_target_equity_irr_nominal_post_tax_pct"] / 100.0
SZ = fin["senior_sizing"]
DSCR_TARGET = SZ["min_dscr_banking_x"]
DSCR_DOWN = SZ["min_dscr_downside_x"]
LLCR_TARGET = SZ["min_llcr_banking_x"]
GEAR_CAP = SZ["gearing_cap_senior_pct_of_funding_net_of_contribution"] / 100.0
BANK_SPLIT = fin["senior_split_pct"]["bank_mini_perm"] / 100.0
BOND_SPLIT = fin["senior_split_pct"]["bonds"] / 100.0
BK = fin["bank_mini_perm"]
M1 = BK["margin_pct"]["to_2020-05-27"]
M2 = BK["margin_pct"]["2020-05-27_to_maturity"]
M3_REFI = 2.25          # base-case refinancing margin (inputs: ABBR + 2.25%)
REFI_FEE = 0.0125       # base-case refinancing fee (inputs: 1.25%)
AE_MARGIN = 3.25        # amend and extend margin (events.standstill_terms)
AE_FEE = 0.0050
BANK_UPFRONT = BK["upfront_fee_pct"] / 100.0
BANK_COMMIT = BK["commitment_fee_pct_pa"] / 100.0
SWAP = INP["macro"]["swap_rates_pct"]["2015-05-27_20y_amortizing"]
SWAP_MKT = INP["macro"]["swap_rates_pct"]["2023-12-31_market_for_mtm"]
BOND_CPN = fin["bonds"]["coupon_pct"] / 100.0
ESCROW_RATE = 0.021
BOND_COST = fin["bonds"]["issue_costs_pct"] / 100.0
NILO_RATE = fin["nilo_loan"]["rate_pct"] / 100.0
NILO_MAX = fin["nilo_loan"]["max_pct_of_eligible_costs"] / 100.0
NILO_FEE = fin["nilo_loan"]["application_fee_pct"] / 100.0
NILO_COMB_MIN = 1.25
NILO_PIK = ev["nilo"]["interest_pik_pct_to_2030-12-31"] / 100.0
LOCKUP = fin["covenants"]["lock_up_dscr_x"]
DEFAULT_DSCR = fin["covenants"]["default_dscr_x"]
TAX_RATE = INP["tax"]["corporate_tax_rate_pct"] / 100.0
TRIP_KM = tolls["average_trip_length_km"]
TOLL_2014 = tolls["car_toll_ard_per_km_2014"]
LEAK = tolls["revenue_leakage_pct"] / 100.0
MULT_O = tolls["class_multipliers_original"]
MULT_N = tolls["class_multipliers_after_2024-01-01"]
MIX_O = tolls["vehicle_mix_pct_original"]
MIX_N = tolls["vehicle_mix_pct_from_2024"]
ESC_FLOOR = 0.03
ESC_FLOOR_LAST_YEAR = 2029   # floor applies to escalations up to July 1, 2029
OM = ops_in["om_fixed_corvus_pa"]
OM_CUT = -ops_in["om_fee_change_after_restructuring_pct"] / 100.0
BO_PCT = ops_in["tolling_back_office_pct_of_toll_revenue"] / 100.0
BO_FIX = ops_in["tolling_back_office_fixed_pa"]
INS = ops_in["insurance_pa"]
SPV = ops_in["spv_costs_pa"]
LC = ops_in["lifecycle"]
LC_PAV, LC_TUN, LC_ITS = LC["pavement_resurfacing_oy12_oy24_oy36"], LC["tunnel_m_and_e_oy15_oy30"], LC["tolling_its_replacement_every_8_years_from_oy8"]
CYC_PAV, CYC_TUN, CYC_ITS = 12, 15, 8
HB_EST = MA["handback_works_estimate_ard_m_2015"]
HB_N = MA["handback_funding_periods"]
REC_DAYS = INP["working_capital"]["toll_receivable_days"]
PAY_DAYS = INP["working_capital"]["payable_days"]
LD_ACT = cap["dc_terms"]["actual_delay_lds_ard_m"]
SUPPORT = INP["events"]["sponsor_support_2021_ard_m"]
RESTR_COST_TOTAL = ops_in["restructuring_costs_2022_2023"]
WRITE_DOWN = ev["write_down_pct"] / 100.0
CANCEL = ev["cancelled_pct_points"] / 100.0
CONVERT = ev["converted_to_equity_pct_points"] / 100.0
NOTES_SHARE = ev["restructured_senior_notes"]["share_of_claims_pct"] / 100.0
NOTES_CPN = ev["restructured_senior_notes"]["coupon_pct"] / 100.0
NOTES_DSCR = 1.30
NOTES_SWEEP = 0.50
CRED_EQ = ev["senior_creditor_share_of_new_equity_pct"] / 100.0
STATE_EQ = ev["state_share_of_new_equity_pct"] / 100.0
STATE_MONEY = ev["state_new_money_ard_m"]
UPGRADE = ev["state_new_money_use"]["holloway_junction_interchange_upgrade_2024_2025"]
STATE_RES = ev["state_new_money_use"]["reserve_top_up"]
WARRANT = 0.03
REV_SHARE = 0.30
REV_SHARE_THRESH = 260.0
RIA_DSCR = MA["ramp_up_interest_account"]["target_dscr_x"]
EQV_RATE = MA["equity_valuation_rate_pct"] / 100.0
FV_RATE = MA["fair_value_2022"]["pre_tax_discount_rate_pct"] / 100.0
RETENDER_COST = MA["fair_value_2022"]["retendering_costs_ard_m"]
BID_CPI = MA["bid_date_cpi_pct"]["value"]
PSC = INP["psc_and_vfm_ard_m_pv_2012"]

# ----------------------------------------------------------------------------------------
# Scenario table (mirrors the scenario table on the Inputs sheet)
# columns: name, traffic case, history end, extended, cpi path (1 bid, 2 actual),
#          traffic factor, ramp lag, CPI-only escalation, opex factor, lifecycle factor,
#          refinancing margin add (%), heavy-vehicle share delta (points), live senior,
#          live restructuring
# ----------------------------------------------------------------------------------------
SCENARIOS = {
    1: ("Bid base (Pellow)", 1, None, 0, 1, 1.0, 0, 0, 1.0, 1.0, 0.0, 0.0, 0, 0),
    2: ("Banking case (Ridgeway)", 2, None, 0, 1, 1.0, 0, 0, 1.0, 1.0, 0.0, 0.0, 1, 0),
    3: ("Downside", 3, None, 0, 1, 1.0, 0, 0, 1.0, 1.0, 0.0, 0.0, 0, 0),
    4: ("Actual history", 4, D_(2026, 6, 30), 1, 2, 1.0, 0, 0, 1.0, 1.0, 0.0, 0.0, 0, 0),
    5: ("Restructuring case (Ridgeway 2023)", 4, D_(2023, 12, 31), 1, 2, 1.0, 0, 0, 1.0, 1.0, 0.0, 0.0, 0, 1),
    6: ("Retender valuation 2022", 5, D_(2022, 6, 30), 0, 2, 1.0, 0, 0, 1.0, 1.0, 0.0, 0.0, 0, 0),
    7: ("Sensitivity: traffic -10%", 1, None, 0, 1, 0.9, 0, 0, 1.0, 1.0, 0.0, 0.0, 0, 0),
    8: ("Sensitivity: ramp-up one year slower", 1, None, 0, 1, 1.0, 1, 0, 1.0, 1.0, 0.0, 0.0, 0, 0),
    9: ("Sensitivity: toll escalation CPI only", 1, None, 0, 1, 1.0, 0, 1, 1.0, 1.0, 0.0, 0.0, 0, 0),
    10: ("Sensitivity: opex +10%", 1, None, 0, 1, 1.0, 0, 0, 1.1, 1.0, 0.0, 0.0, 0, 0),
    11: ("Sensitivity: lifecycle +20%", 1, None, 0, 1, 1.0, 0, 0, 1.0, 1.2, 0.0, 0.0, 0, 0),
    12: ("Sensitivity: interest +100 bp on refinancing", 1, None, 0, 1, 1.0, 0, 0, 1.0, 1.0, 1.0, 0.0, 0, 0),
    13: ("Sensitivity: heavy-vehicle share -2 points", 1, None, 0, 1, 1.0, 0, 0, 1.0, 1.0, 0.0, -2.0, 0, 0),
}
HISTORY_SCEN = (4, 5, 6)

# Traffic cases: base level, base year, growth bands (to 2030, to 2040, after), ramp 2019..2023, uplift
_pel, _rid, _dn = traf["sponsor_base_pellow"], traf["banking_ridgeway"], traf["downside"]
_r23 = traf["restructuring_case_ridgeway_2023"]
TRAFFIC_CASES = {
    1: (_pel["mature_level_2019"], 2019, [_pel["growth_pct"][k] for k in ("2020-2030", "2031-2040", "2041_onward")],
        [0.80, 0.90, 0.96, 1.00, 1.00], 0.0),
    2: (_rid["mature_level_2019"], 2019, [_rid["growth_pct"][k] for k in ("2020-2030", "2031-2040", "2041_onward")],
        [0.72, 0.84, 0.93, 0.98, 1.00], 0.0),
    3: (_dn["mature_level_2019"], 2019, [_dn["growth_pct"][k] for k in ("2020-2030", "2031-2040", "2041_onward")],
        [0.65, 0.78, 0.88, 0.95, 1.00], 0.0),
    4: (_r23["base_2023"], 2023, [_r23["growth_pct"][k] for k in ("2024-2030", "2031-2040", "2041_onward")],
        [1.0] * 5, _r23["heavy_vehicle_uplift_total_trips_pct_from_2024"]),
    5: (_r23["base_2023"], 2023, [_r23["growth_pct"][k] for k in ("2024-2030", "2031-2040", "2041_onward")],
        [1.0] * 5, 0.0),
}
ACT_TRAFFIC = {}
for k, v in traf["actual_semiannual"].items():
    ACT_TRAFFIC[(int(k[:4]), int(k[5]))] = v

CPI_ACT = {}
for k, v in INP["macro"]["ardmore_cpi_annual_avg_change_pct"].items():
    if k.isdigit():
        CPI_ACT[int(k)] = v
CPI_LONG = INP["macro"]["ardmore_cpi_annual_avg_change_pct"]["2027_onward"]
ABBR = {}
for k, v in INP["macro"]["abbr_6m_pct_semiannual_fixing"].items():
    if k[:4].isdigit() and "H" in k:
        ABBR[(int(k[:4]), int(k[5]))] = v
ABBR_LONG = INP["macro"]["abbr_6m_pct_semiannual_fixing"]["2027_onward"]


def cpi_pct(year, path):
    """Annual average CPI change (%) for a calendar year on the bid (1) or actual (2) path."""
    if path == 1:
        return BID_CPI
    return CPI_ACT.get(year, CPI_LONG)


def abbr_pct(year, half):
    return ABBR.get((year, half), ABBR_LONG)


def rnd(x, n=0):
    """Excel ROUND (half away from zero)."""
    f = 10.0 ** n
    return math.floor(abs(x) * f + 0.5) / f * (1 if x >= 0 else -1)


def xl(d):
    """Excel serial number of a date (both Excel and LibreOffice use the 1899-12-30 epoch)."""
    return d.toordinal() - 693594


def d360(a, b):
    """30/360 day count used for bonds and notes: 360(Y2-Y1)+30(M2-M1)+min(D2,30)-min(D1,30)."""
    return 360 * (b.year - a.year) + 30 * (b.month - a.month) + min(b.day, 30) - min(a.day, 30)


def frac_before(start, end, x):
    """Share of the period (start, end] that falls on or before date x."""
    days = (end - start).days
    return min(1.0, max(0.0, (min(end, x) - start).days / days))


def xnpv(rate, cfs, dates, base):
    return sum(cf / (1.0 + rate) ** ((d - base).days / 365.0) for cf, d in zip(cfs, dates))


def xirr(cfs, dates):
    """Excel XIRR: rate r with sum CF_i/(1+r)^((d_i-d_0)/365) = 0. Bisection plus Newton polish."""
    cfs = list(cfs)
    if not any(c > 0 for c in cfs) or not any(c < 0 for c in cfs):
        return None
    base = dates[0]

    def f(r):
        return sum(c / (1.0 + r) ** ((d - base).days / 365.0) for c, d in zip(cfs, dates))
    lo, hi = -0.99, 1.0
    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
        if hi - lo < 1e-14:
            break
    return 0.5 * (lo + hi)


# ----------------------------------------------------------------------------------------
# Timeline
# ----------------------------------------------------------------------------------------
def build_ends():
    ends = [D_(2015, 6, 30)]
    y, q = 2015, 3
    while True:
        m = 3 * q
        last = D_(y, m, 30 if m in (6, 9) else 31)
        ends.append(last)
        if last == CON_END:
            break
        q += 1
        if q == 5:
            y, q = y + 1, 1
    ends.append(D_(2019, 6, 30))
    y, h = 2019, 2
    while True:
        ends.append(D_(y, 12, 31) if h == 2 else D_(y, 6, 30))
        if (y, h) == (2059, 1):
            break
        h += 1
        if h == 3:
            y, h = y + 1, 1
    return ends


ENDS = build_ends()
T = len(ENDS)
STARTS = [FC_DATE] + ENDS[:-1]
assert T == 97 and ENDS[15] == CON_END and ENDS[16] == D_(2019, 6, 30)
T_RESTR = ENDS.index(RESTR_DATE)          # 25
T_FV = ENDS.index(FV_DATE)                # 22
LAST6 = list(range(10, 16))              # last six construction quarters (bridge draws)


def scen_params(scn):
    p = SCENARIOS[scn]
    keys = ("name", "tcase", "hist_end", "ext", "cpi_path", "tfac", "lag", "cpi_only", "opexf",
            "lcf", "refi_add", "hvd", "live", "live_r")
    return dict(zip(keys, p))


# ----------------------------------------------------------------------------------------
# Operations (independent of financing)
# ----------------------------------------------------------------------------------------
def time_and_ops(scn):
    P = scen_params(scn)
    H = scn in HISTORY_SCEN
    ext = P["ext"]
    opening = OPEN_ACT if H else OPEN_SCHED
    conc_final = CONC_EXT if ext else CONC_ORIG
    R = {}
    z = lambda: np.zeros(T)
    for k in ("days", "d360", "year", "half", "months", "con", "opsdays", "ops", "openper", "final",
              "remdays", "rep", "rampup", "prefirst", "standstill", "restr", "post", "notesrep",
              "notessweep", "hist", "f1", "f2", "hedge", "abbr", "cpif", "toll", "esc", "level",
              "ramp", "uplift", "traffic_fc", "traffic_act", "traffic", "wmult", "gross", "leak",
              "netrev", "ld", "om", "bofix", "bovar", "ins", "spv", "opex", "revshare", "restrcost",
              "ebitda", "oy", "lc2015", "lc", "mmra_c", "hbflag", "hb_c", "rec", "pay", "nwc", "dwc",
              "upgrade", "nilorep", "nrate", "ncash", "mpm", "firstrep", "testdate", "lcspend_hb",
              "eodtest", "retention_rel", "end_xl", "start_xl", "contrib_flag", "firstpost",
              "notesfirst", "nilofirst", "postprev", "conc_t"):
        R[k] = z()
    # cpi factor on the period timeline (2015 = 1.0)
    cpif2023 = 1.0
    for y in range(2016, 2024):
        cpif2023 *= 1 + cpi_pct(y, P["cpi_path"]) / 100.0
    L0, BY, G, RAMP, UPL = TRAFFIC_CASES[P["tcase"]]
    mix_car_o = MIX_O["car"] - P["hvd"]
    mix_hv_o = MIX_O["heavy_vehicle"] + P["hvd"]
    w_orig = (mix_car_o * MULT_O["car"] + MIX_O["light_commercial"] * MULT_O["light_commercial"]
              + mix_hv_o * MULT_O["heavy_vehicle"]) / 100.0
    w_new = (MIX_N["car"] * MULT_N["car"] + MIX_N["light_commercial"] * MULT_N["light_commercial"]
             + MIX_N["heavy_vehicle"] * MULT_N["heavy_vehicle"]) / 100.0
    con_days = (CON_END - FC_DATE).days
    for t in range(T):
        s, e = STARTS[t], ENDS[t]
        R["start_xl"][t], R["end_xl"][t] = xl(s), xl(e)
        R["days"][t] = (e - s).days
        R["d360"][t] = d360(s, e)
        R["year"][t] = e.year
        R["half"][t] = 1 if e.month <= 6 else 2
        R["months"][t] = rnd(R["days"][t] / 30.4)
        R["con"][t] = 1 if e <= CON_END else 0
        R["opsdays"][t] = max(0, (min(e, conc_final) - max(s, opening)).days)
        R["ops"][t] = 1 if R["opsdays"][t] > 0 else 0
        R["openper"][t] = 1 if (s < opening <= e) else 0
        R["final"][t] = 1 if (s < conc_final <= e) else 0
        post = 1 if (ext and e > RESTR_DATE) else 0
        conc_t = CONC_EXT if post else CONC_ORIG
        R["conc_t"][t] = xl(conc_t)
        R["remdays"][t] = max(0, (conc_t - max(s, opening)).days)
        R["rep"][t] = 1 if FIRST_REP <= e <= FINAL_REP else 0
        R["rampup"][t] = 1 if (R["ops"][t] and e < FIRST_REP) else 0
        R["prefirst"][t] = 1 if e < FIRST_REP else 0
        R["firstrep"][t] = 1 if e == FIRST_REP else 0
        R["standstill"][t] = 1 if (H and FIRST_REP <= e <= RESTR_DATE) else 0
        R["restr"][t] = 1 if (ext and e == RESTR_DATE) else 0
        R["post"][t] = post
        R["postprev"][t] = 1 if (ext and t > 0 and ENDS[t - 1] > RESTR_DATE) else 0
        R["notesrep"][t] = 1 if (post and e <= NOTES_FINAL) else 0
        R["notessweep"][t] = 1 if (post and e <= NOTES_SWEEP_END) else 0
        R["notesfirst"][t] = 1 if (post and t > 0 and ENDS[t - 1] == RESTR_DATE) else 0
        R["firstpost"][t] = 1 if t == 16 else 0
        R["hist"][t] = 1 if (H and R["ops"][t] and e <= P["hist_end"]) else 0
        R["f1"][t] = frac_before(s, e, MARGIN_STEP)
        R["f2"][t] = frac_before(s, e, MINIPERM_MAT)
        R["mpm"][t] = 1 if (s < MINIPERM_MAT <= e) else 0
        R["hedge"][t] = 1 if e <= HEDGE_END else 0
        R["abbr"][t] = abbr_pct(e.year, int(R["half"][t]))
        R["testdate"][t] = 1 if (R["ops"][t] and e >= D_(2019, 12, 31)) else 0
        R["eodtest"][t] = 1 if e >= DEFAULT_TEST_START else 0
        R["contrib_flag"][t] = R["openper"][t]
        R["retention_rel"][t] = 1 if (s < D_(opening.year + 2, opening.month, opening.day) <= e) else 0
        # NILO regime
        if ext:
            R["nilorep"][t] = 1 if NILO_R_FIRST <= e <= NILO_R_FINAL else 0
            R["nilofirst"][t] = 1 if e == NILO_R_FIRST else 0
        else:
            R["nilorep"][t] = 1 if NILO_FIRST <= e <= NILO_FINAL else 0
            R["nilofirst"][t] = 1 if e == NILO_FIRST else 0
        if post and e <= NILO_PIK_END:
            R["nrate"][t], R["ncash"][t] = NILO_PIK, 0.0
        else:
            R["nrate"][t] = NILO_RATE
            R["ncash"][t] = 1.0 - frac_before(s, e, NILO_CAP_END)
        # CPI factor
        if t == 0:
            R["cpif"][t] = 1.0
        else:
            R["cpif"][t] = R["cpif"][t - 1] * ((1 + cpi_pct(e.year, P["cpi_path"]) / 100.0)
                                               if e.year > ENDS[t - 1].year else 1.0)
        # toll per km (escalated each July 1)
        y = e.year
        if P["cpi_only"] or (ext and y >= 2024) or y > ESC_FLOOR_LAST_YEAR:
            esc = 1 + cpi_pct(y, P["cpi_path"]) / 100.0
        else:
            esc = max(1 + cpi_pct(y, P["cpi_path"]) / 100.0, 1 + ESC_FLOOR)
        R["esc"][t] = esc
        july = 1 if (s < D_(y, 7, 1) <= e) else 0
        prev_toll = TOLL_2014 if t == 0 else R["toll"][t - 1]
        R["toll"][t] = rnd(prev_toll * esc, 4) if july else prev_toll
        # traffic
        g = G[0] if y <= 2030 else (G[1] if y <= 2040 else G[2])
        if y <= BY:
            R["level"][t] = L0 / (1 + G[0] / 100.0) ** (BY - y)
        else:
            R["level"][t] = R["level"][t - 1] * ((1 + g / 100.0) if y > ENDS[t - 1].year else 1.0)
        ry = max(2019, min(2023, y - P["lag"]))
        R["ramp"][t] = RAMP[ry - 2019]
        R["uplift"][t] = 1 + UPL / 100.0 if y >= 2024 else 1.0
        R["traffic_fc"][t] = R["level"][t] * R["ramp"][t] * R["uplift"][t] * P["tfac"]
        R["traffic_act"][t] = ACT_TRAFFIC.get((y, int(R["half"][t])), 0.0)
        R["traffic"][t] = (R["traffic_act"][t] if R["hist"][t] else R["traffic_fc"][t]) * R["ops"][t]
        R["wmult"][t] = w_new if post else w_orig
        od = R["opsdays"][t]
        R["gross"][t] = R["traffic"][t] * 1000 * od * TRIP_KM * R["toll"][t] * R["wmult"][t] / 1e6
        R["leak"][t] = R["gross"][t] * LEAK
        R["netrev"][t] = R["gross"][t] - R["leak"][t]
        R["ld"][t] = LD_ACT if (H and R["openper"][t]) else 0.0
        cf = R["cpif"][t] * od / 365.0 * P["opexf"]
        R["om"][t] = OM * cf * (1 - OM_CUT if post else 1.0)
        R["bofix"][t] = BO_FIX * cf
        R["bovar"][t] = BO_PCT * R["netrev"][t] * P["opexf"]
        R["ins"][t] = INS * cf
        R["spv"][t] = SPV * cf
        R["opex"][t] = R["om"][t] + R["bofix"][t] + R["bovar"][t] + R["ins"][t] + R["spv"][t]
        if post:
            thr = REV_SHARE_THRESH * R["cpif"][t] / cpif2023 * od / 365.0
            R["revshare"][t] = REV_SHARE * max(0.0, R["netrev"][t] - thr)
        R["restrcost"][t] = RESTR_COST_TOTAL / 4.0 if (R["hist"][t] and D_(2022, 6, 30) <= e <= RESTR_DATE) else 0.0
        R["ebitda"][t] = R["netrev"][t] + R["ld"][t] - R["opex"][t] - R["revshare"][t] - R["restrcost"][t]
        # lifecycle (operating year counted from the scheduled opening; items in H2 periods)
        oy = y - 2018 if (R["half"][t] == 2 and R["ops"][t] and e <= conc_final) else 0
        R["oy"][t] = oy
        if oy > 0:
            R["lc2015"][t] = (LC_PAV * (oy % CYC_PAV == 0) + LC_TUN * (oy % CYC_TUN == 0)
                              + LC_ITS * (oy % CYC_ITS == 0))
        R["lc"][t] = R["lc2015"][t] * R["cpif"][t] * P["lcf"]
        hb_start = D_(conc_final.year - 5, conc_final.month, conc_final.day)
        R["hbflag"][t] = 1 if (R["ops"][t] and s >= hb_start) else 0
        R["hb_c"][t] = HB_EST * R["cpif"][t] * P["lcf"] / HB_N * R["hbflag"][t]
        if R["ops"][t] and not R["final"][t]:
            R["rec"][t] = R["netrev"][t] / od * REC_DAYS
            R["pay"][t] = R["opex"][t] / od * PAY_DAYS
        R["nwc"][t] = R["rec"][t] - R["pay"][t]
        R["dwc"][t] = R["nwc"][t] - (R["nwc"][t - 1] if t > 0 else 0.0)
        R["upgrade"][t] = UPGRADE / 4.0 if (ext and D_(2024, 6, 30) <= e <= D_(2025, 12, 31)) else 0.0
    for t in range(T):
        R["mmra_c"][t] = sum(R["lc"][t + 1:t + 7]) / 6.0
    R["cpif2023"] = cpif2023
    R["w_orig"], R["w_new"] = w_orig, w_new
    # construction costs
    capex = {k: np.zeros(T) for k in ("dc", "dev", "spvc", "ins", "cert", "adv", "cont")}
    for t in range(16):
        capex["dc"][t] = DC_PRICE * DC_PROFILE[t] + (DC_PRICE * (RET_AT_COMPLETION + RET_DEFECTS) if t == 15 else 0.0)
        capex["dev"][t] = DEV if t == 0 else 0.0
        capex["spvc"][t] = SPVC * R["days"][t] / con_days
        capex["cert"][t] = CERT * R["days"][t] / con_days
        capex["adv"][t] = ADV * R["days"][t] / con_days
        capex["ins"][t] = INS_C * (0.8 if t == 0 else (0.2 if t == 8 else 0.0))
        capex["cont"][t] = CONT * DC_PROFILE[t] / sum(DC_PROFILE)
    R["capex_items"] = capex
    R["capex"] = sum(capex.values())
    R["retention_dep"] = np.array([DC_PRICE * RET_DEFECTS if t == 15 else 0.0 for t in range(T)])
    R["P"] = P
    R["opening"] = opening
    R["conc_final"] = conc_final
    return R


# ----------------------------------------------------------------------------------------
# Full run with financing
# ----------------------------------------------------------------------------------------
def run(scn, contribution=CONTRIB_BID, locked=None, locked_r=None, down_cfads=None, verbose=False):
    """Run one scenario. locked: financing from the banking run (None => live sizing, scn 2).
    locked_r: restructured profiles from scenario 5 (used by scenario 4)."""
    R = time_and_ops(scn)
    P = R["P"]
    H = scn in HISTORY_SCEN
    ext = P["ext"]
    live = locked is None
    live_r = bool(P["live_r"])
    C = contribution
    z = lambda: np.zeros(T)

    # bank rate and sizing rate
    m3 = AE_MARGIN if H else M3_REFI + P["refi_add"]
    R["margin"] = M1 * R["f1"] + M2 * (R["f2"] - R["f1"]) + m3 * (1 - R["f2"])
    R["bankrate"] = (np.where(R["hedge"] == 1, SWAP, R["abbr"]) + R["margin"]) / 100.0
    R["rr"] = BANK_SPLIT * R["bankrate"] * R["days"] / 365.0 + BOND_SPLIT * BOND_CPN * R["d360"] / 360.0
    R["rrn"] = NOTES_CPN * R["d360"] / 360.0
    R["bridgerate"] = (R["abbr"] / 100.0 + BRIDGE_MARGIN)

    # state of the iteration (initial guesses)
    st = dict(Fnet=1850.0, D=950.0, N=450.0, E=400.0, s=2.0, k=5.0, sn=2.0, kr=5.0,
              tax=z(), R6=500.0, ria=z(), P=z(), nP=z(), notesP=z(), nPr=z(), cfads=z(),
              notesface=0.0)
    if not live:
        st.update(D=locked["D"], N=locked["N"], E=locked["E"], ria=locked["ria"].copy(),
                  P=locked["P"].copy(), nP=locked["nP"].copy())
    if ext and not live_r:
        st.update(notesP=locked_r["notesP"].copy(), nPr=locked_r["nPr"].copy())

    prev_track = None
    for it in range(MAX_PASSES):
        X = one_pass(R, st, C, H, ext, scn)
        # live sizing of the original financing (banking case)
        if live:
            size_senior(R, X, st, C, down_cfads)
            sculpt_nilo(R, X, st, restructured=False)
        if live_r:
            sculpt_notes(R, X, st)
            sculpt_nilo(R, X, st, restructured=True)
        track = np.concatenate([X["cfads"], X["uses"], [st["D"], st["N"], st["E"], st["s"], st["k"],
                                st["sn"], st["kr"], st["notesface"]], st["P"], st["nP"], st["notesP"],
                                st["nPr"], st["ria"], X["tax"]])
        if prev_track is not None and np.max(np.abs(track - prev_track)) < TOL:
            X["passes"] = it + 1
            break
        prev_track = track
    else:
        raise RuntimeError(f"scenario {scn} did not converge")
    X.update({k: v for k, v in R.items() if k not in X})
    X["st"] = dict(st)
    X["scn"] = scn
    X["C"] = C
    finish(X, scn)
    return X


def one_pass(R, st, C, H, ext, scn):
    """One Gauss-Seidel pass over the timeline, using st for the circular quantities."""
    z = lambda: np.zeros(T)
    X = {}
    names = ("uses", "eqdraw", "need", "bridgedraw", "debtdraw", "sendraw", "bankdraw", "bonddraw", "nilodraw",
             "bank_open", "bank_close", "bond_open", "bond_close", "escrow_open", "escrow_close", "escrow_int",
             "bank_int", "commit_fee", "bond_int", "bridge_open", "bridge_close", "bridge_int", "bridge_int_ops",
             "bridge_repay", "contrib", "fees", "dsra_init", "ria_init", "nilo_open", "nilo_close", "nilo_accr",
             "nilo_cashdue", "nilo_Pdue", "nilo_due", "nilo_paid", "nilo_short", "shl_open", "shl_close",
             "shl_int", "shl_draw", "sharecap_draw", "support", "cash_open", "cash_close", "A1", "A2", "A3",
             "A4", "A5", "A6", "fees_due", "int_due", "bank_int_due", "bond_int_due", "notes_int_due",
             "arr_bank_open", "arr_bank_close", "arr_bond_open", "arr_bond_close", "P_due", "P_due_bank",
             "P_due_bond", "notes_P_due", "sen_due", "sen_paid", "fees_paid", "int_paid", "P_paid",
             "P_paid_bank", "P_paid_bond", "dsra_open", "dsra_close", "dsra_draw", "dsra_topup",
             "dsra_release", "dsra_target", "sweep1", "sweep1_bank", "sweep1_bond", "sweep2", "notes_open",
             "notes_close", "notes_P_paid", "ria_open", "ria_close", "mmra_open", "mmra_close", "hb_open",
             "hb_close", "hb_spend", "ret_open", "ret_close", "ret_paid", "upg_open", "upg_close", "lockup",
             "distr", "shl_paid", "div", "eq_cf", "neweq_cf", "state_cf", "ds_sched", "dscr", "dscr_hist",
             "eod", "tax", "cfads", "wdv_open", "wdv_close", "wdv_add", "amort", "ti", "loss_open",
             "loss_close", "loss_used", "loss_added", "forg_loss", "forg_wdv", "taxable", "capcost",
             "extinguish_bank", "extinguish_bond", "statecash", "claims_gross", "swap_mtm", "claims_net",
             "notes_issue", "conv_eq", "cancelled", "shl_wo", "nilo_int_exp", "ria_rel", "dscr_den")
    for n in names:
        X[n] = z()
    D, N, E = st["D"], st["N"], st["E"]
    bankC, bondF = BANK_SPLIT * D, BOND_SPLIT * D
    sen_share = D / (D + N) if (D + N) > 0 else 0.0
    cum_eq = 0.0
    ria_total = float(np.sum(st["ria"]))
    claims = {}
    for t in range(T):
        con = R["con"][t]
        days, days360 = R["days"][t], R["d360"][t]
        prev = (lambda k: X[k][t - 1]) if t > 0 else (lambda k: 0.0)
        # ---------------- balances brought forward
        X["bank_open"][t] = prev("bank_close")
        X["bond_open"][t] = bondF if t == 0 else prev("bond_close")
        X["escrow_open"][t] = bondF if t == 0 else prev("escrow_close")
        X["bridge_open"][t] = prev("bridge_close")
        X["nilo_open"][t] = prev("nilo_close")
        X["shl_open"][t] = prev("shl_close")
        X["notes_open"][t] = prev("notes_close")
        X["cash_open"][t] = prev("cash_close")
        X["dsra_open"][t] = prev("dsra_close")
        X["ria_open"][t] = prev("ria_close")
        X["mmra_open"][t] = prev("mmra_close")
        X["hb_open"][t] = prev("hb_close")
        X["ret_open"][t] = prev("ret_close")
        X["upg_open"][t] = prev("upg_close")
        X["arr_bank_open"][t] = prev("arr_bank_close")
        X["arr_bond_open"][t] = prev("arr_bond_close")
        X["loss_open"][t] = prev("loss_close")
        X["wdv_open"][t] = prev("wdv_close")
        X["nilo_short"][t] = 0.0
        # ---------------- interest accruals on opening balances
        X["bank_int"][t] = X["bank_open"][t] * R["bankrate"][t] * days / 365.0
        X["bond_int"][t] = X["bond_open"][t] * BOND_CPN * days360 / 360.0
        X["notes_int_due"][t] = X["notes_open"][t] * NOTES_CPN * days360 / 360.0
        X["escrow_int"][t] = X["escrow_open"][t] * ESCROW_RATE * days / 365.0 * con
        X["commit_fee"][t] = BANK_COMMIT * (bankC - X["bank_open"][t]) * days / 365.0 * con
        bridge_days = max(0.0, (min(ENDS[t], R["opening"]) - STARTS[t]).days)
        X["bridge_int"][t] = X["bridge_open"][t] * R["bridgerate"][t] * bridge_days / 365.0
        X["nilo_accr"][t] = X["nilo_open"][t] * R["nrate"][t] * days / 365.0
        X["shl_int"][t] = X["shl_open"][t] * SHL_RATE * days / 365.0
        # ---------------- construction funding
        if con:
            fees = (BANK_UPFRONT * bankC + BOND_COST * bondF + NILO_FEE * N + BRIDGE_FEE * C) if t == 0 else 0.0
            X["fees"][t] = fees
            X["dsra_init"][t] = st.get("dsra_init_guess", 0.0) if t == 15 else 0.0
            X["ria_init"][t] = ria_total if t == 15 else 0.0
            X["uses"][t] = (R["capex"][t] + fees + X["bank_int"][t] + X["commit_fee"][t] + X["bond_int"][t]
                            - X["escrow_int"][t] + X["bridge_int"][t] + X["dsra_init"][t] + X["ria_init"][t])
            X["eqdraw"][t] = min(X["uses"][t], max(0.0, E - cum_eq))
            cum_eq += X["eqdraw"][t]
            X["need"][t] = X["uses"][t] - X["eqdraw"][t]
            X["bridgedraw"][t] = C * X["need"][t] / st["R6"] if t in LAST6 else 0.0
            X["debtdraw"][t] = X["need"][t] - X["bridgedraw"][t]
            X["sendraw"][t] = X["debtdraw"][t] * sen_share
            X["nilodraw"][t] = X["debtdraw"][t] - X["sendraw"][t]
            X["bankdraw"][t] = BANK_SPLIT * X["sendraw"][t]
            X["bonddraw"][t] = BOND_SPLIT * X["sendraw"][t]
            X["sharecap_draw"][t] = SHARE_CAP * X["eqdraw"][t]
            X["shl_draw"][t] = X["eqdraw"][t] - X["sharecap_draw"][t]
            X["capcost"][t] = X["uses"][t] - X["dsra_init"][t] - X["ria_init"][t] + X["nilo_accr"][t] + X["shl_int"][t]
        X["contrib"][t] = C * R["contrib_flag"][t]
        X["bridge_repay"][t] = X["contrib"][t]
        X["bridge_int_ops"][t] = 0.0 if con else X["bridge_int"][t]
        X["escrow_close"][t] = X["escrow_open"][t] - X["bonddraw"][t]
        X["bridge_close"][t] = X["bridge_open"][t] + X["bridgedraw"][t] - X["bridge_repay"][t]
        # ---------------- reserves not in the waterfall
        X["ria_rel"][t] = st["ria"][t]
        X["ria_close"][t] = X["ria_open"][t] + X["ria_init"][t] - X["ria_rel"][t]
        X["mmra_close"][t] = X["mmra_open"][t] + R["mmra_c"][t] - R["lc"][t]
        X["hb_spend"][t] = (X["hb_open"][t] + R["hb_c"][t]) * R["final"][t]
        X["hb_close"][t] = X["hb_open"][t] + R["hb_c"][t] - X["hb_spend"][t]
        X["ret_paid"][t] = X["ret_open"][t] * R["retention_rel"][t]
        X["ret_close"][t] = X["ret_open"][t] + R["retention_dep"][t] - X["ret_paid"][t]
        X["support"][t] = (SUPPORT.get(f"{ENDS[t].year}H{int(R['half'][t])}", 0.0) if H else 0.0)
        # ---------------- senior debt service due
        X["bank_int_due"][t] = 0.0 if con else X["bank_int"][t]
        X["bond_int_due"][t] = 0.0 if con else X["bond_int"][t]
        X["int_due"][t] = X["bank_int_due"][t] + X["bond_int_due"][t] + X["notes_int_due"][t]
        refi = REFI_FEE if not H else AE_FEE
        X["fees_due"][t] = refi * X["bank_open"][t] * R["mpm"][t] + X["bridge_int_ops"][t]
        if con or R["standstill"][t]:
            pdb = pdo = 0.0
        else:
            pdb = min(BANK_SPLIT * st["P"][t], X["bank_open"][t])
            pdo = min(BOND_SPLIT * st["P"][t], X["bond_open"][t])
        X["P_due_bank"][t], X["P_due_bond"][t] = pdb, pdo
        X["notes_P_due"][t] = min(st["notesP"][t], X["notes_open"][t]) if R["post"][t] else 0.0
        X["P_due"][t] = pdb + pdo + X["notes_P_due"][t]
        # scheduled debt service (covenant basis, ignores the standstill deferral)
        sched_p = (BANK_SPLIT * st["P"][t] + BOND_SPLIT * st["P"][t]) * (1 - R["post"][t]) * (1 - con) \
            + X["notes_P_due"][t]
        X["ds_sched"][t] = X["int_due"][t] + sched_p - X["ria_rel"][t]
        # ---------------- NILO
        X["nilo_cashdue"][t] = X["nilo_accr"][t] * R["ncash"][t] * (1 - con)
        X["nilo_Pdue"][t] = min(st["nPr"][t] if ext else st["nP"][t],
                                X["nilo_open"][t] + X["nilo_accr"][t] - X["nilo_cashdue"][t]) * (1 - con)
        # ---------------- tax
        X["wdv_add"][t] = X["capcost"][t] - X["contrib"][t] + R["upgrade"][t]
        X["amort"][t] = X["wdv_open"][t] * R["opsdays"][t] / R["remdays"][t] if R["remdays"][t] > 0 else 0.0
        X["nilo_int_exp"][t] = 0.0 if con else X["nilo_accr"][t]
        shl_exp = 0.0 if con else X["shl_int"][t]
        X["ti"][t] = (R["ebitda"][t] - R["lc"][t] - X["hb_spend"][t] - X["amort"][t] - X["int_due"][t]
                      - X["nilo_int_exp"][t] - shl_exp - X["fees_due"][t]) * (1 - con)
        X["loss_used"][t] = min(X["loss_open"][t], max(0.0, X["ti"][t]))
        X["loss_added"][t] = max(0.0, -X["ti"][t])
        X["taxable"][t] = max(0.0, X["ti"][t]) - X["loss_used"][t]
        X["tax"][t] = TAX_RATE * X["taxable"][t]
        # ---------------- CFADS
        X["cfads"][t] = (R["ebitda"][t] - R["dwc"][t] - X["tax"][t] - R["mmra_c"][t] - R["hb_c"][t]) * (1 - con)
        if con:
            X["dsra_close"][t] = X["dsra_open"][t] + X["dsra_init"][t]
            X["bank_close"][t] = X["bank_open"][t] + X["bankdraw"][t]
            X["bond_close"][t] = X["bond_open"][t]
            X["nilo_close"][t] = X["nilo_open"][t] + X["nilodraw"][t] + X["nilo_accr"][t]
            X["shl_close"][t] = X["shl_open"][t] + X["shl_draw"][t] + X["shl_int"][t]
            X["cash_close"][t] = 0.0
            X["arr_bank_close"][t] = X["arr_bond_close"][t] = 0.0
            X["loss_close"][t] = 0.0
            X["wdv_close"][t] = X["wdv_open"][t] + X["wdv_add"][t]
            X["eq_cf"][t] = -X["eqdraw"][t]
            X["dscr"][t] = X["dscr_hist"][t] = 0.0
            if t == 15:
                # DSRA initial funding target: next period scheduled cash debt service scaled to 6 months
                X["dsra_target"][t] = next_ds(R, X, st, t) * 6.0 / R["months"][t + 1]
            continue
        # ---------------- waterfall
        A1 = X["cash_open"][t] + X["cfads"][t] + X["ria_rel"][t] + X["support"][t]
        X["A1"][t] = A1
        X["arr_bank_open"][t] = X["arr_bank_open"][t]
        arrears = X["arr_bank_open"][t] + X["arr_bond_open"][t]
        due = X["fees_due"][t] + X["int_due"][t] + arrears + X["P_due"][t]
        X["sen_due"][t] = due
        funds = max(0.0, A1) + X["dsra_open"][t]
        paid = min(due, funds)
        X["sen_paid"][t] = paid
        X["fees_paid"][t] = min(X["fees_due"][t], paid)
        X["int_paid"][t] = min(X["int_due"][t] + arrears, paid - X["fees_paid"][t])
        X["P_paid"][t] = paid - X["fees_paid"][t] - X["int_paid"][t]
        int_tot = X["int_due"][t] + arrears
        shb = (X["bank_int_due"][t] + X["arr_bank_open"][t]) / int_tot if int_tot > 0 else 0.0
        sho = (X["bond_int_due"][t] + X["arr_bond_open"][t]) / int_tot if int_tot > 0 else 0.0
        X["arr_bank_close"][t] = X["arr_bank_open"][t] + X["bank_int_due"][t] - X["int_paid"][t] * shb
        X["arr_bond_close"][t] = X["arr_bond_open"][t] + X["bond_int_due"][t] - X["int_paid"][t] * sho
        if X["P_due"][t] > 0:
            X["P_paid_bank"][t] = X["P_paid"][t] * X["P_due_bank"][t] / X["P_due"][t]
            X["P_paid_bond"][t] = X["P_paid"][t] * X["P_due_bond"][t] / X["P_due"][t]
            X["notes_P_paid"][t] = X["P_paid"][t] * X["notes_P_due"][t] / X["P_due"][t]
        X["dsra_draw"][t] = max(0.0, paid - max(0.0, A1))
        A2 = A1 - paid + X["dsra_draw"][t]
        X["A2"][t] = A2
        # DSRA
        target = next_ds(R, X, st, t, pre_close=True) * 6.0 / R["months"][t + 1] if t + 1 < T else 0.0
        X["dsra_target"][t] = target
        avail = X["dsra_open"][t] - X["dsra_draw"][t]
        gap = target - avail
        X["dsra_topup"][t] = min(max(0.0, A2), max(0.0, gap))
        X["dsra_release"][t] = max(0.0, -gap)
        A3 = A2 - X["dsra_topup"][t] + X["dsra_release"][t]
        X["A3"][t] = A3
        X["dsra_close"][t] = avail + X["dsra_topup"][t] - X["dsra_release"][t]
        # standstill sweep (100% of excess cash to senior principal)
        bank_after = X["bank_open"][t] - X["P_paid_bank"][t]
        bond_after = X["bond_open"][t] - X["P_paid_bond"][t]
        X["sweep1"][t] = R["standstill"][t] * min(max(0.0, A3), bank_after + bond_after)
        if X["sweep1"][t] > 0:
            X["sweep1_bank"][t] = X["sweep1"][t] * bank_after / (bank_after + bond_after)
            X["sweep1_bond"][t] = X["sweep1"][t] - X["sweep1_bank"][t]
        A4 = A3 - X["sweep1"][t]
        X["A4"][t] = A4
        # NILO
        X["nilo_due"][t] = X["nilo_cashdue"][t] + X["nilo_Pdue"][t] + (X["nilo_short"][t - 1] if t > 0 else 0.0)
        X["nilo_paid"][t] = min(X["nilo_due"][t], max(0.0, A4))
        X["nilo_short"][t] = X["nilo_due"][t] - X["nilo_paid"][t]
        A5 = A4 - X["nilo_paid"][t]
        X["A5"][t] = A5
        X["nilo_close"][t] = X["nilo_open"][t] + X["nilo_accr"][t] - X["nilo_paid"][t]
        # notes sweep
        notes_after = X["notes_open"][t] - X["notes_P_paid"][t]
        X["sweep2"][t] = R["notessweep"][t] * min(NOTES_SWEEP * max(0.0, A5), notes_after)
        A6 = A5 - X["sweep2"][t]
        X["A6"][t] = A6
        # covenant ratios
        X["dscr_den"][t] = X["ds_sched"][t]
        X["dscr"][t] = X["cfads"][t] / X["ds_sched"][t] if X["ds_sched"][t] > 1e-9 else 0.0
        if R["notesfirst"][t]:
            num, den = X["cfads"][t], X["ds_sched"][t]
        else:
            num, den = X["cfads"][t] + X["cfads"][t - 1], X["ds_sched"][t] + X["ds_sched"][t - 1]
        X["dscr_hist"][t] = num / den if (R["testdate"][t] and den > 1e-9) else 0.0
        test_fail_lock = R["testdate"][t] and den > 1e-9 and X["dscr_hist"][t] < LOCKUP
        test_fail_def = R["eodtest"][t] and den > 1e-9 and X["dscr_hist"][t] < DEFAULT_DSCR
        X["eod"][t] = 1.0 if ((not R["post"][t]) and (X["eod"][t - 1] > 0 or test_fail_def)) else 0.0
        lock = (R["prefirst"][t] or test_fail_lock or X["dsra_close"][t] < target - 1e-6 or X["eod"][t] > 0
                or R["standstill"][t] or X["nilo_short"][t] > 1e-6
                or X["arr_bank_close"][t] + X["arr_bond_close"][t] > 1e-6)
        X["lockup"][t] = 0.0 if R["final"][t] else (1.0 if lock else 0.0)
        X["distr"][t] = 0.0 if X["lockup"][t] else max(0.0, A6)
        X["statecash"][t] = STATE_RES * R["restr"][t]
        X["cash_close"][t] = A6 - X["distr"][t] + X["statecash"][t]
        # closing balances
        X["bank_close"][t] = X["bank_open"][t] - X["P_paid_bank"][t] - X["sweep1_bank"][t]
        X["bond_close"][t] = X["bond_open"][t] - X["P_paid_bond"][t] - X["sweep1_bond"][t]
        X["notes_close"][t] = X["notes_open"][t] - X["notes_P_paid"][t] - X["sweep2"][t]
        # shareholder loans and dividends
        shl_avail = X["shl_open"][t] + X["shl_int"][t] + X["support"][t]
        X["shl_paid"][t] = min(X["distr"][t], shl_avail)
        X["div"][t] = X["distr"][t] - X["shl_paid"][t]
        X["shl_close"][t] = shl_avail - X["shl_paid"][t]
        # equity cash flows
        if R["post"][t]:
            X["neweq_cf"][t] = X["distr"][t]
        else:
            X["eq_cf"][t] = X["distr"][t] - X["support"][t]
        # upgrade account
        X["upg_close"][t] = X["upg_open"][t] - R["upgrade"][t]
        # ---------------- restructuring at 2023-12-31 (after the period's waterfall)
        if R["restr"][t]:
            gross = X["bank_close"][t] + X["bond_close"][t] + X["arr_bank_close"][t] + X["arr_bond_close"][t]
            mtm = swap_mtm(R, st)
            net = gross - mtm
            X["claims_gross"][t], X["swap_mtm"][t], X["claims_net"][t] = gross, mtm, net
            X["notes_issue"][t] = NOTES_SHARE * net
            X["conv_eq"][t] = CONVERT * net
            X["cancelled"][t] = CANCEL * net
            X["shl_wo"][t] = X["shl_close"][t]
            claims = dict(bank=X["bank_close"][t] + X["arr_bank_close"][t],
                          bond=X["bond_close"][t] + X["arr_bond_close"][t])
            X["extinguish_bank"][t] = X["bank_close"][t]
            X["extinguish_bond"][t] = X["bond_close"][t]
            X["bank_close"][t] = X["bond_close"][t] = 0.0
            X["arr_bank_close"][t] = X["arr_bond_close"][t] = 0.0
            X["notes_close"][t] = X["notes_issue"][t]
            X["shl_close"][t] = 0.0
            X["upg_close"][t] += UPGRADE
            X["state_cf"][t] = -STATE_MONEY
            X["neweq_cf"][t] = -STATE_MONEY
            st["notesface"] = X["notes_issue"][t]
            # DSRA target re-based on the notes (next period)
            X["dsra_target"][t] = next_ds(R, X, st, t) * 6.0 / R["months"][t + 1]
        # ---------------- tax losses and cost base (forgiveness applied at restructuring)
        forg = (X["cancelled"][t] + X["shl_wo"][t]) if R["restr"][t] else 0.0
        lpool = X["loss_open"][t] - X["loss_used"][t] + X["loss_added"][t]
        X["forg_loss"][t] = min(forg, lpool)
        X["loss_close"][t] = lpool - X["forg_loss"][t]
        wpool = X["wdv_open"][t] + X["wdv_add"][t] - X["amort"][t]
        X["forg_wdv"][t] = min(forg - X["forg_loss"][t], wpool)
        X["wdv_close"][t] = wpool - X["forg_wdv"][t]
    # bridge sum over the last six quarters, funding requirement, DSRA initial funding
    st["R6"] = float(sum(X["need"][t] for t in LAST6))
    X["total_uses"] = float(np.sum(X["uses"]))
    X["Fnet"] = X["total_uses"] - C
    st["Fnet"] = X["Fnet"]
    st["dsra_init_guess"] = X["dsra_target"][15]
    X["claims"] = claims
    return X


def next_ds(R, X, st, t, pre_close=False):
    """Scheduled cash debt service of period t+1 (interest on period-t closing balances,
    scheduled principal, less the ramp-up account release). Used for the DSRA target."""
    if t + 1 >= T:
        return 0.0
    u = t + 1
    if pre_close:
        bank_c = X["bank_open"][t] - X["P_paid_bank"][t] - X["sweep1_bank"][t]
        bond_c = X["bond_open"][t] - X["P_paid_bond"][t] - X["sweep1_bond"][t]
        notes_c = X["notes_open"][t] - X["notes_P_paid"][t] - X["sweep2"][t]
        if R["restr"][t]:
            bank_c = bond_c = 0.0
    else:
        bank_c, bond_c, notes_c = X["bank_close"][t], X["bond_close"][t], X["notes_close"][t]
    intr = (bank_c * R["bankrate"][u] * R["days"][u] / 365.0 + bond_c * BOND_CPN * R["d360"][u] / 360.0
            + notes_c * NOTES_CPN * R["d360"][u] / 360.0)
    if R["standstill"][u]:
        p = 0.0
    elif R["post"][u]:
        p = min(st["notesP"][u], notes_c)
    else:
        p = min(BANK_SPLIT * st["P"][u], bank_c) + min(BOND_SPLIT * st["P"][u], bond_c)
    return intr + p - st["ria"][u]


def swap_mtm(R, st):
    """Mark-to-market of the bank swap at 2023-12-31 (positive = owed to the concessionaire):
    remaining notional = original scheduled bank balance; receive market 4.36%, pay 3.48%."""
    bal = BANK_SPLIT * st["D"]
    sched_open = np.zeros(T)
    for t in range(16, T):
        sched_open[t] = bal
        bal -= BANK_SPLIT * st["P"][t]
    v, df = 0.0, 1.0
    for t in range(T_RESTR + 1, T):
        if not R["hedge"][t]:
            break
        df /= (1 + SWAP_MKT / 100.0 * R["days"][t] / 365.0)
        v += (SWAP_MKT - SWAP) / 100.0 * sched_open[t] * R["days"][t] / 365.0 * df
    return v


def solve_sculpt(cf, intr_fn, flags, D0, df, s0=2.0):
    """Fixed point for the sculpting divisor s: DS_t = max(I_t, CF_t/s) over the flagged periods,
    s = sum_{not A} CF*DF / (D0 - sum_{A} I*DF). intr_fn(s) returns the interest row for s."""
    s = s0
    for _ in range(500):
        I = intr_fn(s)
        A = flags * (I > cf / s)
        num = np.sum(cf * df * flags * (1 - A))
        den = D0 - np.sum(I * df * A)
        s_new = num / den if den > 0 else s
        if abs(s_new - s) < 1e-13:
            return s_new
        s = s_new
    raise RuntimeError("sculpting did not converge")


def sched_profile(cf, rate, flags, D0, start_t, s, cashfrac=None):
    """Roll a balance from D0 at start_t with DS = max(cash interest, cf/s) in flagged periods."""
    bal = np.zeros(T)
    intr = np.zeros(T)
    cashi = np.zeros(T)
    P = np.zeros(T)
    DS = np.zeros(T)
    b = D0
    for t in range(start_t, T):
        bal[t] = b
        intr[t] = b * rate[t]
        cashi[t] = intr[t] * (1.0 if cashfrac is None else cashfrac[t])
        if flags[t]:
            DS[t] = max(cashi[t], cf[t] / s)
            P[t] = DS[t] - cashi[t]
        b = b + intr[t] - cashi[t] - P[t]
    return bal, intr, cashi, P, DS


def df_chain(rate, flags):
    df = np.zeros(T)
    d = 1.0
    for t in range(T):
        if flags[t]:
            d = d / (1 + rate[t])
            df[t] = d
    return df


def size_senior(R, X, st, C, down_cfads):
    """Banking-case senior sizing (live): lesser of gearing cap, sculpted amount at 1.50x,
    LLCR 1.55x, interest-only cover 1.50x and downside interest-only cover 1.15x."""
    cf = X["cfads"]
    rep = R["rep"]
    rr = R["rr"]
    df = df_chain(rr, rep)
    pv = float(np.sum(cf * df * rep))
    cand = {
        "gearing": GEAR_CAP * X["Fnet"],
        "dscr_sculpt": pv / DSCR_TARGET,
        "llcr": pv / LLCR_TARGET,
        "interest_cover": float(np.min(np.where(rep == 1, cf / (DSCR_TARGET * rr), 1e12))),
    }
    if down_cfads is not None:
        cand["downside"] = float(np.min(np.where(rep == 1, down_cfads / (DSCR_DOWN * rr), 1e12)))
    D = min(cand.values())
    st["cand"] = cand
    st["binding"] = min(cand, key=cand.get)
    st["D"] = D
    st["E"] = EQ_SHARE * X["Fnet"]
    st["N"] = X["Fnet"] - st["E"] - D
    st["pv_cfads"] = pv
    st["df"] = df
    first = 16

    def intr_fn(s):
        return sched_profile(cf, rr, rep, D, first, s)[1]
    s = solve_sculpt(cf, intr_fn, rep, D, df, st["s"])
    st["s"] = s
    bal, intr, cashi, P, DS = sched_profile(cf, rr, rep, D, first, s)
    st["P"] = P
    st["sched_bal"], st["sched_int"], st["sched_ds"] = bal, intr, DS
    ria = np.where(R["rampup"] == 1, np.maximum(0.0, intr - cf / RIA_DSCR), 0.0)
    st["ria"] = ria
    st["sculpt_residual"] = float(bal[np.where(rep == 1)[0][-1]] - P[np.where(rep == 1)[0][-1]])


def sculpt_notes(R, X, st):
    cf = X["cfads"]
    flags = R["notesrep"]
    rate = R["rrn"]
    D0 = st["notesface"]
    if D0 <= 0:
        return
    df = df_chain(rate, flags)
    first = T_RESTR + 1

    def intr_fn(s):
        return sched_profile(cf, rate, flags, D0, first, s)[1]
    s = solve_sculpt(cf, intr_fn, flags, D0, df, st["sn"])
    st["sn"] = s
    bal, intr, cashi, P, DS = sched_profile(cf, rate, flags, D0, first, s)
    st["notesP"] = P
    st["notes_sched_bal"], st["notes_sched_ds"], st["notes_df"] = bal, DS, df


def sculpt_nilo(R, X, st, restructured):
    """NILO profile sculpted on CFADS after scheduled senior (or notes) cash debt service."""
    cf = X["cfads"]
    if restructured:
        start = T_RESTR + 1
        B0 = X["nilo_close"][T_RESTR]
        resid = cf - st.get("notes_sched_ds", np.zeros(T))
    else:
        start = 16
        B0 = X["nilo_close"][15]
        resid = cf - (st.get("sched_ds", np.zeros(T)) - st["ria"])
    flags = R["nilorep"]
    rate = R["nrate"] * R["days"] / 365.0
    cash = R["ncash"]
    # DF over the flagged periods; balances roll from B0 at `start` with capitalization before
    df = df_chain(rate, flags)
    first_flag = int(np.where(flags == 1)[0][0])
    # balance at the start of the first flagged period (capitalized from `start`)
    Bs = B0
    for t in range(start, first_flag):
        Bs = Bs * (1 + rate[t]) - 0.0
    key = "kr" if restructured else "k"

    def intr_fn(k):
        return sched_profile(resid, rate, flags, B0, start, k, cashfrac=cash)[2]
    k = solve_sculpt(resid, intr_fn, flags, Bs, df, st[key])
    st[key] = k
    bal, intr, cashi, P, DS = sched_profile(resid, rate, flags, B0, start, k, cashfrac=cash)
    if restructured:
        st["nPr"] = P
        st["nilo_r_ds"] = DS
    else:
        st["nP"] = P
        st["nilo_sched_ds"] = DS
        st["nilo_B0"] = Bs


# ----------------------------------------------------------------------------------------
# Results per run
# ----------------------------------------------------------------------------------------
def finish(X, scn):
    R = X
    ends = ENDS
    # equity returns (original sponsors)
    eq_dates = [FC_DATE] + ends
    eq_cfs = [0.0] + list(X["eq_cf"])
    X["equity_irr"] = xirr(eq_cfs, eq_dates)
    X["equity_npv_target"] = xnpv(TARGET_IRR, eq_cfs, eq_dates, FC_DATE)
    X["equity_invested"] = float(np.sum(X["eqdraw"]) + np.sum(X["support"]))
    X["equity_distributions"] = float(np.sum(np.where(X["post"] == 1, 0.0, X["distr"])))
    # project cash flows (post-tax, unlevered by financing flows; tax as computed)
    proj = -X["capex"] + X["contrib"] + X["cfads"] * (1 - X["con"]) - X["upgrade"]
    X["project_cf"] = proj
    X["project_irr"] = xirr([0.0] + list(proj), eq_dates)
    X["project_irr_pretax"] = xirr([0.0] + list(proj + X["tax"]), eq_dates)
    # ratios on the original senior debt
    rep = X["rep"]
    ds = X["ds_sched"]
    with np.errstate(divide="ignore", invalid="ignore"):
        dscr = np.where((rep == 1) & (ds > 1e-9), X["cfads"] / ds, np.nan)
    X["min_dscr_rep"] = float(np.nanmin(dscr)) if np.any(~np.isnan(dscr)) else None
    X["avg_dscr_rep"] = float(np.nanmean(dscr)) if np.any(~np.isnan(dscr)) else None
    ramp = X["rampup"] == 1
    X["min_dscr_rampup"] = float(np.min(X["cfads"][ramp] / ds[ramp]))
    # combined senior plus NILO cover where NILO is paying
    nds = X["nilo_cashdue"] + X["nilo_Pdue"]
    comb = (rep == 1) & (X["nilorep"] == 1)
    X["min_comb_dscr"] = float(np.min(X["cfads"][comb] / (ds[comb] + nds[comb]))) if np.any(comb) else None
    # LLCR and PLCR at the first repayment period (start of 2021H1)
    rr = X["rr"]
    t0 = int(np.where(rep == 1)[0][0])
    df_all = np.zeros(T)
    d = 1.0
    for t in range(t0, T):
        d /= (1 + rr[t])
        df_all[t] = d
    bal0 = X["bank_open"][t0] + X["bond_open"][t0]
    X["llcr_first"] = float(np.sum(X["cfads"] * df_all * rep) / bal0) if bal0 > 0 else None
    X["plcr_first"] = float(np.sum(X["cfads"] * df_all * X["ops"]) / bal0) if bal0 > 0 else None
    llcr = np.full(T, np.nan)
    for t in range(t0, T):
        b = X["bank_open"][t] + X["bond_open"][t]
        if rep[t] and b > 1e-6:
            llcr[t] = np.sum(X["cfads"][t:] * df_all[t:] * rep[t:]) / (df_all[t] * (1 + rr[t])) / b
    X["llcr"] = llcr
    X["min_llcr"] = float(np.nanmin(llcr)) if np.any(~np.isnan(llcr)) else None
    X["lockup_periods"] = int(np.sum(X["lockup"] * X["ops"] * (1 - X["prefirst"])))
    X["dsra_draws_total"] = float(np.sum(X["dsra_draw"]))
    # NPV of the scenario's distributions after the authority-default test date at the base IRR
    after = [i for i, e in enumerate(ends) if e > AUTH_DATE]
    X["npv_distr_after_2022H1"] = xnpv(TARGET_IRR, [X["distr"][i] for i in after], [ends[i] for i in after], AUTH_DATE)
    # pre-tax unlevered cash flows after the fair-value date (retender valuation)
    fv_cf = X["ebitda"] - X["dwc"] - X["lc"] - X["hb_spend"] + X["restrcost"]
    X["fv_cf"] = fv_cf
    X["fair_value_2022"] = xnpv(FV_RATE, [fv_cf[i] for i in after], [ends[i] for i in after], FV_DATE)


# ----------------------------------------------------------------------------------------
# Public sector comparator and value for money (2012 present values)
# ----------------------------------------------------------------------------------------
def psc_vfm():
    r = PSC["discount_rate_nominal_pct"] / 100.0
    p = PSC["psc"]
    psc_total = sum(p.values())
    days = (D_(2019, 3, 31) - D_(2012, 12, 31)).days
    dfac = (1 + r) ** (-days / 365.0)
    ref = 410.0 * dfac
    bid = CONTRIB_BID * dfac
    pp = PSC["ppp_shadow_bid"]
    ppp_ref = ref + pp["retained_risks"] + pp["contract_management"]
    ppp_bid = bid + pp["retained_risks"] + pp["contract_management"]
    return dict(psc_items=p, psc_total=psc_total, discount_days=days, discount_factor=dfac,
                pv_contribution_reference=ref, pv_contribution_bid=bid,
                retained_risks=pp["retained_risks"], contract_management=pp["contract_management"],
                ppp_reference_total=ppp_ref, ppp_bid_total=ppp_bid,
                vfm_reference=psc_total - ppp_ref, vfm_bid=psc_total - ppp_bid,
                vfm_reference_pct=(psc_total - ppp_ref) / psc_total,
                vfm_bid_pct=(psc_total - ppp_bid) / psc_total,
                psc_risk_total=p["construction_risk"] + p["traffic_revenue_risk"] + p["operating_risk"],
                psc_raw=p["raw_capex"] + p["om_and_lifecycle"] + p["toll_revenue_retained"])


# ----------------------------------------------------------------------------------------
# Orchestration
# ----------------------------------------------------------------------------------------
def lock_from(Xb):
    st = Xb["st"]
    return dict(D=st["D"], N=st["N"], E=st["E"], ria=st["ria"].copy(), P=st["P"].copy(), nP=st["nP"].copy())


def size_banking(C=CONTRIB_BID, down=None):
    """Banking run with live sizing; the downside interest-cover constraint uses the downside
    CFADS row from a downside run on the resulting financing (iterated to a fixed point)."""
    down_cf = down
    for _ in range(20):
        Xb = run(2, C, down_cfads=down_cf)
        Xd = run(3, C, locked=lock_from(Xb))
        if down_cf is not None and np.max(np.abs(Xd["cfads"] - down_cf)) < 1e-10:
            return Xb, Xd
        down_cf = Xd["cfads"].copy()
    raise RuntimeError("downside loop did not converge")


def solve_contribution(target, which):
    """Contribution giving the target equity IRR: which='banking' (IRR on the banking case
    with live sizing) or 'base' (bid base IRR with financing sized on the banking case)."""
    def irr_at(C):
        Xb, _ = size_banking(C)
        if which == "banking":
            return Xb["equity_irr"]
        return run(1, C, locked=lock_from(Xb))["equity_irr"]
    lo, hi = 150.0, 700.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if irr_at(mid) < target:
            lo = mid
        else:
            hi = mid
        if hi - lo < 1e-9:
            break
    return 0.5 * (lo + hi)


def main():
    out = {"meta": {"model": "Case T reference model (Python mirror)", "version": "1.0",
                    "as_of_story": "2026-10-03", "inputs": "inputs_case_t.json", "tolerance": TOL,
                    "currency": "ARD millions unless stated"}}
    Xb, Xd = size_banking()
    L = lock_from(Xb)
    runs = {2: Xb, 3: Xd}
    runs[1] = run(1, locked=L)
    X5 = run(5, locked=L)
    LR = dict(notesP=X5["st"]["notesP"].copy(), nPr=X5["st"]["nPr"].copy())
    runs[5] = X5
    runs[4] = run(4, locked=L, locked_r=LR)
    runs[6] = run(6, locked=L)
    for s in range(7, 14):
        runs[s] = run(s, locked=L)
    C_bank = solve_contribution(TARGET_IRR, "banking")
    C_base = solve_contribution(TARGET_IRR, "base")
    Xc, _ = size_banking(C_bank)
    out["runs"] = {}
    for s, X in runs.items():
        out["runs"][str(s)] = export_run(X)
    out["contribution_solved"] = {"banking_case_at_11.4pct": C_bank, "bid_base_at_11.4pct": C_base,
                                  "banking_run_at_solved": export_run(Xc, series=False)}
    out["locked"] = {"D": L["D"], "N": L["N"], "E": L["E"], "ria": list(L["ria"]), "P": list(L["P"]),
                     "nP": list(L["nP"]), "notesP": list(LR["notesP"]), "nPr": list(LR["nPr"]),
                     "down_cfads": list(Xd["cfads"])}
    out["psc"] = psc_vfm()
    out["timeline"] = {"start": [d.isoformat() for d in STARTS], "end": [d.isoformat() for d in ENDS]}
    out["derived"] = derived(runs, out)
    json.dump(out, open(os.path.join(HERE, "outputs_case_t.json"), "w"), indent=1, default=float)
    write_report(runs, out)
    return runs, out


SERIES = ("traffic", "toll", "wmult", "gross", "netrev", "ld", "opex", "revshare", "restrcost", "ebitda", "lc",
          "mmra_c", "hb_c", "dwc", "tax", "cfads", "uses", "capex", "eqdraw", "bridgedraw", "sendraw", "nilodraw",
          "bank_int", "commit_fee", "bond_int", "escrow_int", "bridge_int", "fees", "bank_open", "bank_close",
          "bond_open", "bond_close", "notes_open", "notes_close", "nilo_open", "nilo_close", "nilo_accr",
          "nilo_cashdue", "nilo_Pdue", "nilo_paid", "shl_open", "shl_close", "shl_int", "int_due", "P_due",
          "sen_paid", "int_paid", "P_paid", "arr_bank_close", "arr_bond_close", "ds_sched", "dscr", "dscr_hist",
          "dsra_target", "dsra_close", "dsra_draw", "ria_rel", "ria_close", "mmra_close", "hb_close",
          "cash_close", "lockup", "eod", "distr", "shl_paid", "div", "eq_cf", "neweq_cf", "wdv_close", "amort",
          "loss_close", "ti", "sweep1", "sweep2", "fees_due", "cpif", "level", "opsdays", "llcr", "fv_cf",
          "project_cf", "A1", "upgrade", "upg_close", "ret_close", "support", "hb_spend", "rec", "pay")


def export_run(X, series=True):
    st = X["st"]
    sc = {k: st[k] for k in ("D", "N", "E", "s", "k", "sn", "kr", "notesface") if k in st}
    for k in ("cand", "binding", "pv_cfads"):
        if k in st:
            sc[k] = st[k]
    for k in ("equity_irr", "equity_npv_target", "equity_invested", "equity_distributions", "project_irr",
              "project_irr_pretax", "min_dscr_rep", "avg_dscr_rep", "min_dscr_rampup", "min_comb_dscr",
              "llcr_first", "plcr_first", "min_llcr", "lockup_periods", "dsra_draws_total",
              "npv_distr_after_2022H1", "fair_value_2022", "total_uses", "Fnet", "passes", "cpif2023",
              "w_orig", "w_new"):
        sc[k] = X.get(k)
    sc["claims"] = X.get("claims")
    sc["name"] = X["P"]["name"]
    sc["contribution"] = X["C"]
    if "sculpt_residual" in st:
        sc["sculpt_residual"] = st["sculpt_residual"]
    r = {"scalars": sc}
    if series:
        r["series"] = {k: [float(v) for v in X[k]] for k in SERIES}
        for k, v in X["capex_items"].items():
            r["series"]["capex_" + k] = [float(a) for a in v]
        r["series"]["restr"] = {k: float(X[k][T_RESTR]) for k in ("claims_gross", "swap_mtm", "claims_net",
                                                                     "notes_issue", "conv_eq", "cancelled",
                                                                     "shl_wo")}
    return r


def annual(X, key, y0=2019, y1=2026, mode="sum"):
    out = {}
    for y in range(y0, y1 + 1):
        idx = [t for t in range(T) if ENDS[t].year == y and X["ops"][t]]
        if not idx:
            continue
        if mode == "sum":
            out[y] = float(sum(X[key][t] for t in idx))
        else:  # day-weighted average (traffic)
            dsum = sum(X["opsdays"][t] for t in idx)
            out[y] = float(sum(X[key][t] * X["opsdays"][t] for t in idx) / dsum)
    return out


def derived(runs, out):
    """Figures assembled from several runs (ledger items T-F01 to T-F10 and extras)."""
    d = {}
    X1, X2, X3, X4, X5, X6 = (runs[i] for i in (1, 2, 3, 4, 5, 6))
    # sources and uses at close (banking = bid base financing)
    capex = X2["capex_items"]
    su = {
        "uses": {
            "dc_contract": float(np.sum(capex["dc"])),
            "development": float(np.sum(capex["dev"])),
            "spv_costs": float(np.sum(capex["spvc"])),
            "insurance": float(np.sum(capex["ins"])),
            "certifier": float(np.sum(capex["cert"])),
            "advisors": float(np.sum(capex["adv"])),
            "contingency": float(np.sum(capex["cont"])),
            "bank_interest": float(np.sum(X2["bank_int"][:16])),
            "bank_commitment_fees": float(np.sum(X2["commit_fee"][:16])),
            "bond_interest": float(np.sum(X2["bond_int"][:16])),
            "escrow_income": -float(np.sum(X2["escrow_int"][:16])),
            "bridge_interest": float(np.sum(X2["bridge_int"][:16])),
            "upfront_fees": float(np.sum(X2["fees"])),
            "dsra_initial": float(X2["dsra_target"][15]),
            "ramp_up_interest_account": float(np.sum(X2["st"]["ria"])),
        },
        "sources": {
            "equity": float(np.sum(X2["eqdraw"])),
            "senior_bank": BANK_SPLIT * X2["st"]["D"],
            "senior_bonds": BOND_SPLIT * X2["st"]["D"],
            "nilo": X2["st"]["N"],
            "state_contribution_via_bridge": X2["C"],
        },
    }
    su["total_uses"] = sum(su["uses"].values())
    su["total_sources"] = sum(su["sources"].values())
    st = X2["st"]
    fnet = X2["Fnet"]
    su["fees_breakdown"] = {"bank_upfront": BANK_UPFRONT * BANK_SPLIT * st["D"], "bond_issue": BOND_COST * BOND_SPLIT * st["D"],
                            "nilo_application": NILO_FEE * st["N"], "bridge_upfront": BRIDGE_FEE * X2["C"]}
    su["idc_total"] = su["uses"]["bank_interest"] + su["uses"]["bond_interest"] + su["uses"]["escrow_income"] + su["uses"]["bridge_interest"]
    su["financing_costs_total"] = su["idc_total"] + su["uses"]["bank_commitment_fees"] + su["uses"]["upfront_fees"]
    su["funding_requirement_net"] = fnet
    su["senior_pct_net"] = st["D"] / fnet
    su["nilo_pct_net"] = st["N"] / fnet
    su["equity_pct_net"] = st["E"] / fnet
    su["nilo_pct_eligible"] = st["N"] / X2["total_uses"]
    su["nilo_capitalized_interest_construction"] = float(np.sum(X2["nilo_accr"][:16]))
    su["nilo_balance_at_completion"] = float(X2["nilo_close"][15])
    su["nilo_balance_2024_03_31_start_of_2024H1"] = float(X2["nilo_open"][ENDS.index(D_(2024, 6, 30))])
    su["shl_interest_capitalized_construction"] = float(np.sum(X2["shl_int"][:16]))
    su["binding_constraint"] = st["binding"]
    su["sizing_candidates"] = st["cand"]
    su["sculpt_s"] = st["s"]
    su["nilo_k"] = st["k"]
    su["share_capital"] = SHARE_CAP * st["E"]
    su["shareholder_loans"] = (1 - SHARE_CAP) * st["E"]
    d["sources_uses"] = su
    # T-F02
    d["bid"] = {"equity_irr_bid_base": X1["equity_irr"], "equity_irr_banking": X2["equity_irr"],
                "equity_irr_downside": X3["equity_irr"], "npv_bid_base_at_11.4": X1["equity_npv_target"],
                "npv_banking_at_11.4": X2["equity_npv_target"],
                "contribution_needed_banking": out["contribution_solved"]["banking_case_at_11.4pct"],
                "contribution_needed_bid_base": out["contribution_solved"]["bid_base_at_11.4pct"],
                "project_irr_bid_base": X1["project_irr"], "project_irr_banking": X2["project_irr"],
                "project_irr_pretax_bid_base": X1["project_irr_pretax"]}
    # T-F04 traffic, T-F06 revenue
    d["traffic_annual"] = {"pellow": annual(X1, "traffic", mode="avg"), "ridgeway": annual(X2, "traffic", mode="avg"),
                           "downside": annual(X3, "traffic", mode="avg"),
                           "actual": annual(X4, "traffic", 2019, 2026, mode="avg")}
    d["revenue_annual"] = {"bid_base": annual(X1, "netrev", 2019, 2025), "banking": annual(X2, "netrev", 2019, 2025),
                           "actual": annual(X4, "netrev", 2019, 2025)}
    # T-F05 toll per km by class 2015-2030 (actual CPI path), original and restructured regimes
    d["tolls"] = toll_table()
    # T-F07 DSCR history vs banking
    hist = {}
    for t in range(17, T_RESTR + 1):
        lab = f"{ENDS[t].year}H{1 if ENDS[t].month <= 6 else 2}"
        hist[lab] = {"actual_hist_12m": float(X4["dscr_hist"][t]), "actual_period": float(X4["dscr"][t]),
                     "banking_hist_12m": float(X2["dscr_hist"][t]), "banking_period": float(X2["dscr"][t]),
                     "actual_cfads": float(X4["cfads"][t]), "actual_ds_sched": float(X4["ds_sched"][t]),
                     "lockup": float(X4["lockup"][t]), "eod": float(X4["eod"][t]),
                     "dsra_close": float(X4["dsra_close"][t]), "arrears": float(X4["arr_bank_close"][t] + X4["arr_bond_close"][t])}
    d["dscr_history"] = hist
    # T-F08 termination comparison at 2022-06-30
    t = T_FV
    sen = X4["bank_close"][t] + X4["bond_close"][t] + X4["arr_bank_close"][t] + X4["arr_bond_close"][t]
    nilo = X4["nilo_close"][t]
    eq_contrib = float(np.sum(X4["eqdraw"]) + np.sum(X4["support"][:t + 1]))
    eq_distr = float(np.sum(X4["distr"][:t + 1]))
    fv = X6["fair_value_2022"]
    comp_cd = fv - RETENDER_COST
    d["termination_2022"] = {
        "senior_principal": float(X4["bank_close"][t] + X4["bond_close"][t]),
        "senior_arrears": float(X4["arr_bank_close"][t] + X4["arr_bond_close"][t]),
        "senior_claims": float(sen), "nilo_outstanding": float(nilo),
        "equity_contributed": eq_contrib, "equity_distributions": eq_distr,
        "authority_default_equity_npv": X1["npv_distr_after_2022H1"],
        "authority_default_total": float(sen + nilo + X1["npv_distr_after_2022H1"]),
        "fm_total": float(sen + nilo + eq_contrib - eq_distr),
        "fair_value": fv, "retender_costs": RETENDER_COST, "concessionaire_default_comp": comp_cd,
        "cd_senior_recovery_nilo_subordinated": min(1.0, comp_cd / sen),
        "cd_senior_recovery_nilo_pari_passu": min(1.0, comp_cd / (sen + nilo)),
        "cd_nilo_recovery_pari_passu": min(1.0, comp_cd / (sen + nilo)),
        "cd_nilo_recovery_subordinated": max(0.0, min(1.0, (comp_cd - sen) / nilo)),
        "cd_shortfall_to_senior": float(sen - comp_cd),
    }
    # T-F09 restructuring
    r = {k: float(X5[k][T_RESTR]) for k in ("claims_gross", "swap_mtm", "claims_net", "notes_issue",
                                            "conv_eq", "cancelled", "shl_wo")}
    cl = X5["claims"]
    r["bank_claim_gross"], r["bond_claim_gross"] = cl["bank"], cl["bond"]
    r["bank_principal"] = float(X5["bank_open"][T_RESTR] - X5["P_paid_bank"][T_RESTR] - X5["sweep1_bank"][T_RESTR])
    r["bond_principal"] = float(X5["bond_open"][T_RESTR] - X5["P_paid_bond"][T_RESTR] - X5["sweep1_bond"][T_RESTR])
    r["accrued_interest"] = r["claims_gross"] - r["bank_principal"] - r["bond_principal"]
    r["bank_claim_net"] = cl["bank"] - r["swap_mtm"]
    r["bond_claim_net"] = cl["bond"]
    after = [i for i in range(T_RESTR + 1, T)]
    dates = [ENDS[i] for i in after]
    distr = [X5["distr"][i] for i in after]
    eqv = xnpv(EQV_RATE, distr, dates, RESTR_DATE)
    notes_repaid = [i for i in after if X5["notes_open"][i] <= 1e-9 and X5["notes_close"][i - 1] <= 1e-9]
    w = WARRANT * xnpv(EQV_RATE, [X5["distr"][i] for i in notes_repaid], [ENDS[i] for i in notes_repaid], RESTR_DATE) if notes_repaid else 0.0
    r["equity_value_total"] = eqv
    r["warrant_value"] = w
    r["equity_value_creditors"] = CRED_EQ * (eqv - w)
    r["equity_value_state"] = STATE_EQ * (eqv - w)
    r["state_new_money"] = STATE_MONEY
    r["state_npv_at_11.4"] = r["equity_value_state"] - STATE_MONEY
    r["notes_repaid_from"] = ENDS[notes_repaid[0]].isoformat() if notes_repaid else None
    r["senior_value_received"] = r["notes_issue"] + r["equity_value_creditors"]
    r["senior_recovery_pct_net_claims"] = r["senior_value_received"] / r["claims_net"]
    r["senior_recovery_pct_gross_claims_incl_setoff"] = (r["senior_value_received"] + r["swap_mtm"]) / r["claims_gross"]
    for cls, gross in (("bank", cl["bank"]), ("bond", cl["bond"])):
        netc = gross - (r["swap_mtm"] if cls == "bank" else 0.0)
        share = netc / r["claims_net"]
        r[f"{cls}_notes"] = r["notes_issue"] * share
        r[f"{cls}_equity_value"] = r["equity_value_creditors"] * share
        r[f"{cls}_cancelled"] = r["cancelled"] * share
        r[f"{cls}_recovery_pct"] = (r[f"{cls}_notes"] + r[f"{cls}_equity_value"]) / netc
    nilo_claim = float(X5["nilo_close"][T_RESTR])
    nilo_cf = [X5["nilo_paid"][i] for i in after]
    r["nilo_claim"] = nilo_claim
    r["nilo_pv_at_3.06"] = xnpv(NILO_RATE, nilo_cf, dates, RESTR_DATE)
    r["nilo_recovery_pv_pct"] = r["nilo_pv_at_3.06"] / nilo_claim
    r["nilo_nominal_receipts"] = float(sum(nilo_cf))
    r["nilo_final_payment"] = ENDS[max(i for i in after if X5["nilo_paid"][i] > 1e-9)].isoformat()
    r["original_equity_invested"] = X5["equity_invested"]
    r["original_equity_distributions"] = float(np.sum(X5["distr"][:T_RESTR + 1]))
    r["original_equity_warrants"] = w
    r["shl_written_off"] = r["shl_wo"]
    r["forgiveness_to_losses"] = float(X5["forg_loss"][T_RESTR])
    r["forgiveness_to_cost_base"] = float(X5["forg_wdv"][T_RESTR])
    r["losses_before_forgiveness"] = float(X5["loss_open"][T_RESTR] - X5["loss_used"][T_RESTR] + X5["loss_added"][T_RESTR])
    r["notes_s"] = X5["st"]["sn"]
    r["nilo_r_k"] = X5["st"]["kr"]
    r["nilo_balance_2023"] = nilo_claim
    r["dsra_2023"] = float(X5["dsra_close"][T_RESTR])
    r["cash_2023_incl_state"] = float(X5["cash_close"][T_RESTR])
    pre = {"bank": r["bank_principal"], "bonds": r["bond_principal"], "accrued_senior_interest": r["accrued_interest"],
           "nilo": nilo_claim, "shareholder_loans": r["shl_wo"]}
    post = {"restructured_notes": r["notes_issue"], "nilo": nilo_claim, "new_equity_conversion": r["conv_eq"],
            "new_equity_state": STATE_MONEY}
    r["pre_structure"], r["post_structure"] = pre, post
    d["restructuring"] = r
    # T-F10 post-restructuring projections
    nrep = X5["notesrep"] == 1
    nds = X5["ds_sched"]
    p = {"min_notes_dscr": float(np.min(X5["cfads"][nrep] / nds[nrep])),
         "avg_notes_dscr": float(np.mean(X5["cfads"][nrep] / nds[nrep])),
         "notes_dscr_by_period": {f"{ENDS[i].year}H{1 if ENDS[i].month <= 6 else 2}": float(X5["cfads"][i] / nds[i])
                                  for i in range(T) if nrep[i]},
         "notes_balance": {f"{ENDS[i].year}H{1 if ENDS[i].month <= 6 else 2}": float(X5["notes_close"][i])
                           for i in range(T_RESTR, T) if X5["notes_close"][i - 1] > 1e-9},
         "revshare_total_nominal": float(np.sum(X5["revshare"])),
         "revshare_npv_6.85": xnpv(0.0685, [X5["revshare"][i] for i in after], dates, RESTR_DATE),
         "equity_value_total": eqv,
         "sweep_total": float(np.sum(X5["sweep2"])),
         "first_distribution": next((ENDS[i].isoformat() for i in after if X5["distr"][i] > 1e-6), None),
         "revenue_threshold_ratio_2030": None}
    t30 = ENDS.index(D_(2030, 12, 31))
    rev30 = X5["netrev"][t30 - 1] + X5["netrev"][t30]
    thr30 = REV_SHARE_THRESH * X5["cpif"][t30] / X5["cpif2023"]
    p["revenue_2030"] = float(rev30)
    p["threshold_2030"] = float(thr30)
    p["revenue_threshold_ratio_2030"] = float(rev30 / thr30)
    tlast = max(i for i in range(T) if X5["ops"][i] and X5["half"][i] == 2)
    revL = X5["netrev"][tlast - 1] + X5["netrev"][tlast]
    p["revenue_threshold_ratio_2058"] = float(revL / (REV_SHARE_THRESH * X5["cpif"][tlast] / X5["cpif2023"]))
    d["post_restructuring"] = p
    # sensitivities
    sens = {}
    for s in [1] + list(range(7, 14)):
        X = runs[s]
        sens[X["P"]["name"]] = {"equity_irr": X["equity_irr"], "npv_11.4": X["equity_npv_target"],
                                "min_dscr": X["min_dscr_rep"], "avg_dscr": X["avg_dscr_rep"],
                                "min_comb_dscr": X["min_comb_dscr"], "lockup_periods": X["lockup_periods"],
                                "dsra_draws": X["dsra_draws_total"]}
    d["sensitivities"] = sens
    # banking metrics
    d["banking_metrics"] = {k: X2[k] for k in ("min_dscr_rep", "avg_dscr_rep", "min_dscr_rampup", "min_comb_dscr",
                                               "llcr_first", "plcr_first", "min_llcr")}
    d["downside_metrics"] = {k: X3[k] for k in ("min_dscr_rep", "avg_dscr_rep", "min_dscr_rampup", "min_comb_dscr",
                                                "llcr_first", "equity_irr", "lockup_periods")}
    d["bid_base_metrics"] = {k: X1[k] for k in ("min_dscr_rep", "avg_dscr_rep", "min_dscr_rampup", "min_comb_dscr",
                                                "llcr_first", "equity_irr", "lockup_periods")}
    # actual outturn
    d["actual"] = {"equity_invested": X4["equity_invested"], "dsra_draws": X4["dsra_draws_total"],
                   "first_lockup": "2019H2", "eod_first": next((f"{ENDS[i].year}H{1 if ENDS[i].month <= 6 else 2}"
                                                                for i in range(T) if X4["eod"][i] > 0), None),
                   "senior_arrears_2023": float(X4["arr_bank_close"][T_RESTR - 0] if False else r["accrued_interest"]),
                   "traffic_2019_vs_base_pct": d["traffic_annual"]["actual"][2019] / d["traffic_annual"]["pellow"][2019] - 1,
                   "covid_2020H1_traffic": ACT_TRAFFIC[(2020, 1)]}
    return d


def toll_table():
    rows = {}
    for regime in ("original", "restructured"):
        toll = TOLL_2014
        yr = {}
        for y in range(2015, 2031):
            if regime == "restructured" and y >= 2024:
                esc = 1 + cpi_pct(y, 2) / 100.0
            elif y <= ESC_FLOOR_LAST_YEAR:
                esc = max(1 + cpi_pct(y, 2) / 100.0, 1 + ESC_FLOOR)
            else:
                esc = 1 + cpi_pct(y, 2) / 100.0
            toll = rnd(toll * esc, 4)
            hv = MULT_N["heavy_vehicle"] if (regime == "restructured" and y >= 2024) else MULT_O["heavy_vehicle"]
            yr[y] = {"car": toll, "light_commercial": rnd(toll * MULT_O["light_commercial"], 4),
                     "heavy_vehicle": rnd(toll * hv, 4), "car_trip_23.8km": toll * TRIP_KM}
        rows[regime] = yr
    return rows


def f1(x, n=1):
    return "n/a" if x is None else f"{x:,.{n}f}"


def pct(x, n=1):
    return "n/a" if x is None else f"{100 * x:.{n}f}%"


def write_report(runs, out):
    d = out["derived"]
    su = d["sources_uses"]
    L = []
    w = L.append
    w("# Case T reference model: report\n")
    w("Merrick Link toll road PPP (Brannock, Commonwealth of Ardmore). Model version 1.0, story as of October 3, 2026. "
      "All amounts ARD millions (nominal) unless stated. Generated by `model/case_t.py`; every number below is computed, "
      "none is typed by hand.\n")
    w("## 1. Model structure and conventions\n")
    w("- Timeline: 16 construction columns (stub 2015-05-27 to 2015-06-30, then quarters to 2019-03-31), then a "
      "2019-03-31 to 2019-06-30 column and semiannual periods to 2059-06-30 (97 columns; first model period in "
      "Excel column J).")
    w("- Scenarios: 1 bid base (Pellow), 2 banking (Ridgeway, live sizing), 3 downside, 4 actual history, "
      "5 restructuring case (Ridgeway 2023), 6 retender valuation at June 30, 2022, 7 to 13 sensitivities on the bid base.")
    w("- Financing is sized live on the banking case (scenario 2) and locked for all other runs; the Restructured "
      "Senior Notes and restructured NILO profile are sculpted live in scenario 5 and locked for scenario 4.")
    w(f"- Circularity: Gauss-Seidel iteration of the whole model to a tolerance of {TOL:g} (ARD million) on every "
      f"tracked series and scalar. Banking run converged in {runs[2]['passes']} passes. The workbook uses iterative "
      "calculation (100 iterations, 0.000001 maximum change) with a circuit breaker `Circ` on the Inputs sheet: "
      "Circ = 0 cuts the financing-cost and sizing feedback so errors flush out; set it back to 1 to recalculate.")
    w("- Day counts: bank, bridge, NILO, escrow and shareholder loans ACT/365; bonds and notes 30/360.")
    w("- Sign convention: costs stored positive and subtracted; equity cash flows negative for contributions.\n")
    w("## 2. Public sector comparator and value for money (T-F01)\n")
    p = out["psc"]
    w("| Item | ARD m, PV 2012 at 6.85% |\n|---|---|")
    for k, v in p["psc_items"].items():
        w(f"| PSC: {k.replace('_', ' ')} | {f1(v)} |")
    w(f"| **PSC total** | {f1(p['psc_total'])} |")
    w(f"| PPP reference: contribution ARD 410.0 m at 2019-03-31 (DF {p['discount_factor']:.6f}) | {f1(p['pv_contribution_reference'])} |")
    w(f"| PPP reference: retained risks plus contract management | {f1(p['retained_risks'] + p['contract_management'])} |")
    w(f"| **PPP reference total** | {f1(p['ppp_reference_total'])} |")
    w(f"| **Value for money, reference** | {f1(p['vfm_reference'])} ({pct(p['vfm_reference_pct'])}) |")
    w(f"| PPP winning bid: contribution ARD 287.4 m PV | {f1(p['pv_contribution_bid'])} |")
    w(f"| **PPP bid total** | {f1(p['ppp_bid_total'])} |")
    w(f"| **Value for money, winning bid** | {f1(p['vfm_bid'])} ({pct(p['vfm_bid_pct'])}) |\n")
    w("## 3. Financing at close (T-F03)\n")
    w("| Uses | ARD m |\n|---|---|")
    for k, v in su["uses"].items():
        w(f"| {k.replace('_', ' ')} | {f1(v)} |")
    w(f"| **Total uses** | {f1(su['total_uses'])} |")
    w("\n| Sources | ARD m | % of funding net of contribution |\n|---|---|---|")
    for k, v in su["sources"].items():
        w(f"| {k.replace('_', ' ')} | {f1(v)} | {pct(v / su['funding_requirement_net']) if 'contribution' not in k else '-'} |")
    w(f"| **Total sources** | {f1(su['total_sources'])} | |\n")
    w(f"Funding requirement net of the contribution: {f1(su['funding_requirement_net'])}. IDC (net of escrow income): "
      f"{f1(su['idc_total'])}; financing costs including fees: {f1(su['financing_costs_total'])}. NILO capitalized "
      f"construction interest {f1(su['nilo_capitalized_interest_construction'])}; NILO balance at completion "
      f"{f1(su['nilo_balance_at_completion'])}; NILO as share of eligible costs {pct(su['nilo_pct_eligible'])} (cap 33%).\n")
    w("Senior sizing candidates (ARD m):\n")
    w("| Constraint | Debt capacity |\n|---|---|")
    for k, v in su["sizing_candidates"].items():
        w(f"| {k.replace('_', ' ')} | {f1(v)} |")
    w(f"\nBinding constraint: **{su['binding_constraint']}**. Sculpting divisor s = {su['sculpt_s']:.4f}x; NILO divisor "
      f"k = {su['nilo_k']:.4f}x.\n")
    w("## 4. Bid returns (T-F02)\n")
    b = d["bid"]
    w("| Item | Value |\n|---|---|")
    w(f"| Equity IRR, bid base at ARD 287.4 m | {pct(b['equity_irr_bid_base'], 2)} |")
    w(f"| Equity NPV at 11.4%, bid base (at close) | {f1(b['npv_bid_base_at_11.4'])} |")
    w(f"| Equity IRR, banking case | {pct(b['equity_irr_banking'], 2)} |")
    w(f"| Equity IRR, downside | {pct(b['equity_irr_downside'], 2)} |")
    w(f"| Contribution for 11.4% on the banking case | {f1(b['contribution_needed_banking'])} |")
    w(f"| Contribution for 11.4% on the bid base | {f1(b['contribution_needed_bid_base'])} |")
    w(f"| Project IRR post-tax, bid base | {pct(b['project_irr_bid_base'], 2)} |")
    w(f"| Project IRR post-tax, banking | {pct(b['project_irr_banking'], 2)} |\n")
    w("Ratios (senior, repayment periods 2021H1 to 2048H2):\n")
    w("| Run | Min DSCR | Avg DSCR | Min ramp-up DSCR | Min senior+NILO DSCR | LLCR 2021H1 | Equity IRR | Lock-up periods |\n|---|---|---|---|---|---|---|---|")
    for s in (1, 2, 3):
        X = runs[s]
        w(f"| {X['P']['name']} | {f1(X['min_dscr_rep'], 2)}x | {f1(X['avg_dscr_rep'], 2)}x | {f1(X['min_dscr_rampup'], 2)}x | "
          f"{f1(X['min_comb_dscr'], 2)}x | {f1(X['llcr_first'], 2)}x | {pct(X['equity_irr'], 2)} | {X['lockup_periods']} |")
    w("\n## 5. Sensitivities on the bid base (financing locked)\n")
    w("| Case | Equity IRR | NPV at 11.4% | Min DSCR | Avg DSCR | Lock-up periods |\n|---|---|---|---|---|---|")
    for k, v in d["sensitivities"].items():
        w(f"| {k} | {pct(v['equity_irr'], 2)} | {f1(v['npv_11.4'])} | {f1(v['min_dscr'], 2)}x | {f1(v['avg_dscr'], 2)}x | {v['lockup_periods']} |")
    w("\n## 6. Traffic and revenue (T-F04, T-F06)\n")
    w("| Year | Pellow | Ridgeway | Downside | Actual | Revenue bid base | Revenue banking | Revenue actual |\n|---|---|---|---|---|---|---|---|")
    ta, ra = d["traffic_annual"], d["revenue_annual"]
    for y in range(2019, 2027):
        w(f"| {y} | {f1(ta['pellow'].get(y))} | {f1(ta['ridgeway'].get(y))} | {f1(ta['downside'].get(y))} | {f1(ta['actual'].get(y))} | "
          f"{f1(ra['bid_base'].get(y))} | {f1(ra['banking'].get(y))} | {f1(ra['actual'].get(y))} |")
    w("\nTraffic in thousand trips per day (2019 averaged over operating days); revenue = net toll revenue, ARD m.\n")
    w("## 7. Toll per km by class (T-F05, actual CPI path)\n")
    w("| Year from July 1 | Car orig | LCV orig | HV orig | Car restr | HV restr |\n|---|---|---|---|---|---|")
    tt = d["tolls"]
    for y in range(2015, 2031):
        o, r_ = tt["original"][y], tt["restructured"][y]
        w(f"| {y} | {o['car']:.4f} | {o['light_commercial']:.4f} | {o['heavy_vehicle']:.4f} | {r_['car']:.4f} | {r_['heavy_vehicle']:.4f} |")
    w("\n## 8. Outturn and distress (T-F07)\n")
    w("| Period | CFADS actual | Sched. DS | DSCR period | DSCR 12m | Banking DSCR 12m | Lock-up | EoD | DSRA | Arrears |\n|---|---|---|---|---|---|---|---|---|---|")
    for k, v in d["dscr_history"].items():
        w(f"| {k} | {f1(v['actual_cfads'])} | {f1(v['actual_ds_sched'])} | {f1(v['actual_period'], 2)}x | {f1(v['actual_hist_12m'], 2)}x | "
          f"{f1(v['banking_hist_12m'], 2)}x | {int(v['lockup'])} | {int(v['eod'])} | {f1(v['dsra_close'])} | {f1(v['arrears'])} |")
    w("\n## 9. Termination compensation at June 30, 2022 (T-F08)\n")
    tc = d["termination_2022"]
    w("| Item | ARD m |\n|---|---|")
    for k, v in tc.items():
        w(f"| {k.replace('_', ' ')} | {pct(v) if 'recovery' in k else f1(v)} |")
    w("\n## 10. Restructuring at December 31, 2023 (T-F09)\n")
    r = d["restructuring"]
    w("| Item | Value |\n|---|---|")
    for k, v in r.items():
        if isinstance(v, dict):
            continue
        w(f"| {k.replace('_', ' ')} | {pct(v) if ('pct' in k) else (v if isinstance(v, str) or v is None else f1(v, 2 if k.endswith('_s') or k.endswith('_k') else 1))} |")
    w("\n## 11. Post-restructuring projections (T-F10)\n")
    pr = d["post_restructuring"]
    w(f"Minimum notes DSCR {f1(pr['min_notes_dscr'], 2)}x; average {f1(pr['avg_notes_dscr'], 2)}x; cash sweep total {f1(pr['sweep_total'])}; "
      f"first distribution {pr['first_distribution']}; equity value at 11.4% {f1(pr['equity_value_total'])}; state revenue share total "
      f"{f1(pr['revshare_total_nominal'])} (2030 revenue is {pct(pr['revenue_threshold_ratio_2030'])} of the threshold; final full year "
      f"{pct(pr['revenue_threshold_ratio_2058'])}).\n")
    w("## 12. Assumption changes\n")
    for line in ASSUMPTION_CHANGES:
        w(f"- {line}")
    w("")
    open(os.path.join(HERE, "case_t_report.md"), "w").write("\n".join(L))


ASSUMPTION_CHANGES = []

if __name__ == "__main__":
    runs, out = main()
    d = out["derived"]
    print(json.dumps(d["sources_uses"], indent=1, default=float)[:3000])
    print(json.dumps(d["bid"], indent=1, default=float))
