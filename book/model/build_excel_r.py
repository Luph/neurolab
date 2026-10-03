"""Builds model/Case_R_Model.xlsx: the Case R workbook with live formulas (FAST-consistent layout).

Layout (book/bible/style-sheet.md 5.4): time across columns, first period (2022) in column J, last (2059) in AU;
column D label, E unit, F constants, G row total. Inputs: blue font on pale yellow fill; links from other sheets:
green font; calculations: black. Checks show 0 when passing and turn red otherwise.
The only range name is `Scenario` (the price-scenario selector).

Every number in the workbook is either an input copied from inputs_case_r.json (plus the supplementary assumptions
in case_r.SUPP) or a formula. Nothing is pasted from the Python mirror. `case_r_excel_map.json` records which
row/cell holds each Python series and scalar, for verify_case_r.py.

Usage: python3 build_excel_r.py [--scenario base|low|high|...] [--out path]
"""
import json, os, sys, datetime as dt
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import CellIsRule
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import case_r as M

INP = M.INP
NT = M.NT
COLS = [get_column_letter(10 + i) for i in range(NT)]          # J..AU
PREV = {c: get_column_letter(9 + i) for i, c in enumerate(COLS)}   # I..AT
NEXT = {c: get_column_letter(11 + i) for i, c in enumerate(COLS)}  # K..AV
FC, LC = COLS[0], COLS[-1]

BLUE = Font(color="0000FF")
GREEN = Font(color="008000")
BOLD = Font(bold=True)
TITLE = Font(bold=True, size=14)
INFILL = PatternFill("solid", fgColor="FFF2CC")
HEADFILL = PatternFill("solid", fgColor="DDEBF7")
REDFILL = PatternFill("solid", fgColor="FF9999")
FMT = {"m": '#,##0.000;(#,##0.000);"–"', "x": '0.000"x"', "pct": '0.0000', "date": "yyyy-mm-dd", "f": "0.000000",
       "int": "0", "gwh": '#,##0.000;(#,##0.000);"–"', "p": '#,##0.00;(#,##0.00);"–"'}


class Book:
    def __init__(self):
        self.wb = Workbook()
        self.wb.remove(self.wb.active)
        self.rows = {}     # key -> (sheet, row)
        self.cells = {}    # key -> "Sheet!$F$r"
        self.sheets = {}
        self.map = {"series": {}, "scalars": {}}

    def sheet(self, name, title):
        ws = self.wb.create_sheet(name)
        w = Sheet(self, ws, name, title)
        self.sheets[name] = w
        return w

    def R(self, key, c, absrow=False):
        sh, r = self.rows[key]
        return "%s!%s%s%d" % (sh, c, "$" if absrow else "", r)

    def RR(self, key):
        """Whole time row range, absolute."""
        sh, r = self.rows[key]
        return "%s!$%s$%d:$%s$%d" % (sh, FC, r, LC, r)

    def C(self, key):
        return self.cells[key]


class Sheet:
    def __init__(self, book, ws, name, title):
        self.b, self.ws, self.name = book, ws, name
        ws["A1"] = title
        ws["A1"].font = TITLE
        ws["A2"] = "Case R, Mesa Corta Renewables. USD m nominal unless stated. Illustrative prices: not ERCOT settlement data and not a forecast."
        for col, wd in (("A", 2), ("B", 2), ("C", 2), ("D", 52), ("E", 12), ("F", 14), ("G", 14), ("H", 2), ("I", 2)):
            ws.column_dimensions[col].width = wd
        for c in COLS:
            ws.column_dimensions[c].width = 11
        self.r = 6

    def header_time(self):
        ws = self.ws
        ws["D4"] = "Year"
        ws["D5"] = "Period end"
        for c in COLS:
            if self.name == "Time":
                continue
            ws["%s4" % c] = "=Time!%s$4" % c
            ws["%s4" % c].font = Font(color="008000", bold=True)
            ws["%s5" % c] = "=Time!%s$6" % c
            ws["%s5" % c].font = GREEN
            ws["%s5" % c].number_format = FMT["date"]
        ws.freeze_panes = "J6"

    def section(self, text):
        self.r += 1
        c = self.ws.cell(row=self.r, column=1, value=text)
        c.font = BOLD
        for col in range(1, 48):
            self.ws.cell(row=self.r, column=col).fill = HEADFILL
        self.r += 1

    def note(self, text):
        self.ws.cell(row=self.r, column=4, value=text).font = Font(italic=True, color="666666")
        self.r += 1

    def series(self, key, label, unit, fn, style="calc", fmt="m", total=None, pykey=None):
        r = self.r
        ws = self.ws
        ws.cell(row=r, column=4, value=label)
        ws.cell(row=r, column=5, value=unit)
        for c in COLS:
            v = fn(c)
            cell = ws["%s%d" % (c, r)]
            cell.value = v if not isinstance(v, str) or v.startswith("=") else "=" + v
            cell.number_format = FMT[fmt]
            if style == "input":
                cell.font = BLUE
                cell.fill = INFILL
            elif style == "link":
                cell.font = GREEN
        if total:
            g = ws.cell(row=r, column=7, value="=%s(%s%d:%s%d)" % (total, FC, r, LC, r))
            g.number_format = FMT[fmt]
        self.b.rows[key] = (self.name, r)
        if pykey:
            self.b.map["series"][pykey] = [self.name, r]
        self.r += 1
        return r

    def scalar(self, key, label, unit, value, style="calc", fmt="m", pykey=None, note=None):
        r = self.r
        ws = self.ws
        ws.cell(row=r, column=4, value=label)
        ws.cell(row=r, column=5, value=unit)
        cell = ws.cell(row=r, column=6)
        if isinstance(value, str) and not value.startswith("="):
            value = "=" + value
        cell.value = value
        cell.number_format = FMT[fmt]
        if style == "input":
            cell.font = BLUE
            cell.fill = INFILL
        elif style == "link":
            cell.font = GREEN
        if note:
            ws.cell(row=r, column=7, value=note).font = Font(italic=True, color="666666")
        self.b.cells[key] = "%s!$F$%d" % (self.name, r)
        if pykey:
            self.b.map["scalars"][pykey] = [self.name, "F%d" % r]
        self.r += 1
        return r


def d(s):
    return dt.datetime.fromisoformat(s)


# ============================================================================================
def build(scenario="base", out=None):
    B = Book()
    case = M.SCENARIOS[scenario]
    SUPP = M.SUPP
    P, H, D, TX, OX, VAL = M.P, M.H, M.D, M.TX, M.OX, M.VAL
    A = M.ASSETS
    I = B.C

    # ---------------------------------------------------------------- Cover
    cv = B.sheet("Cover", "Case R reference model: Mesa Corta Renewables portfolio (ERCOT)")
    for i, t in enumerate([
        "Owner: Lattimer Energy Transition Fund II (Lattimer Infrastructure Partners). Platform: Mesa Corta Renewables LLC; HoldCo: Mesa Corta HoldCo LLC; OpCo: Mesa Corta OpCo LLC.",
        "Assets R1-R8 (603.0 MW wind, 401.1 MWac solar, 250.0 MW / 500 MWh storage). Annual periods 2022-2059, first period in column J.",
        "Python mirror: model/case_r.py (computational source of truth). Verification: model/case_r_verification.md.",
        "Model version R-1.1; inputs_case_r.json version %s. Workbook saved with scenario '%s'." % (INP["meta"]["file_version"], scenario),
        "Switches on the Inputs sheet: Scenario (1 base, 2 low, 3 high prices and captures), volume case (1 P50, 2 P90 one-year, 3 P90 ten-year, 4 P99 one-year),",
        "refinancing switch (1 = 2025 USPP refinancing and holdco repricing, 0 = status quo), and sensitivity cells. Debt is always sized on the Operations sizing blocks (base, P50 and P99).",
        "Colors: blue on pale yellow = input; green = link from another sheet; black = calculation; Checks sheet shows 0 when passing, red when failing.",
        "Sign convention: costs and outflows stored positive on calculation sheets and subtracted explicitly.",
        "No circular references: debt sculpting uses forward discount-factor products; USPP series are solved backward from 2043; iterative calculation is off.",
        "Every Case R price is Illustrative: Case Bible illustrative price paths; not ERCOT settlement data and not a forecast.",
    ]):
        cv.ws.cell(row=4 + i, column=2, value=t)
    cv.ws.column_dimensions["B"].width = 160

    # ---------------------------------------------------------------- Inputs
    ip = B.sheet("Inputs", "Inputs")
    ip.header_time()
    ws = ip.ws

    def inp(key, label, unit, value, fmt=None, note=None):
        if fmt is None:
            fmt = "date" if isinstance(value, dt.datetime) else ("int" if isinstance(value, int) and not isinstance(value, bool) else "f")
        ip.scalar(key, label, unit, value, style="input", fmt=fmt, note=note)

    ip.section("Switches")
    sc_idx = M.PRICE_IDX[case["price"]]
    inp("scen", "Scenario (1 base, 2 low, 3 high prices and captures)", "index", sc_idx)
    B.wb.defined_names["Scenario"] = DefinedName("Scenario", attr_text=I("scen"))
    vol_idx = {"p50": 1, "p90_1yr": 2, "p90_10yr": 3, "p99_1yr": 4}[case["volume"]]
    inp("volcase", "Volume case (1 P50, 2 P90 one-year, 3 P90 ten-year, 4 P99 one-year)", "index", vol_idx)
    inp("refi", "Refinancing switch (1 = 2025 refinancing, 0 = status quo)", "flag", 1 if case["refi"] else 0)
    inp("s_wsc", "Sensitivity: West solar capture shift", "points", float(case["wsc"]))
    inp("s_batt", "Sensitivity: battery revenue low case (1 = on)", "flag", 1 if case["battery"] == "low" else 0)
    inp("s_curt", "Sensitivity: curtailment added", "% points", float(case["curt_add"]))
    inp("s_opex", "Sensitivity: opex factor", "factor", float(case["opex_f"]))
    inp("s_sofr", "Sensitivity: SOFR shift on unhedged debt", "% points", float(case["sofr_add"]))
    inp("sz_price", "Sizing case price scenario (base)", "index", 1)
    inp("sz_vol", "Sizing case volume case (P50)", "index", 1)
    inp("sz_vol99", "P99 sizing test volume case", "index", 4)
    inp("zero", "Sensitivity value in sizing cases", "number", 0.0)
    inp("one", "Opex factor in sizing cases", "factor", 1.0)

    ip.section("General")
    inp("y0", "First model year", "year", 2022)
    inp("ybase", "Price base year for escalation", "year", 2022)
    inp("infl", "Opex inflation", "% pa", SUPP["inflation_pct"])
    inp("model_end", "Model end date", "date", d("2059-12-31"))
    inp("dpy", "Days per year for discounting (unit conversion)", "days", 365)
    inp("big", "Large number for MIN tests", "number", SUPP["large_number"])
    inp("thr", "Debt service below which ratios are not shown", "USD m", SUPP["ratio_threshold_usd_m"])
    inp("z90", "Standard normal z for P90", "number", M.Z90)
    inp("z99", "Standard normal z for P99", "number", M.Z99)
    inp("n10", "Years in the long-horizon P-value", "years", 10)

    ip.section("Prices and capture (Illustrative)")
    for h, v in P["hub_ratio_to_north"].items():
        inp("hub_" + h.split()[0].lower(), "Hub ratio to North Hub: " + h, "ratio", v)
    inp("lowmult", "Low case: capture decline multiplier", "x", 1.5)
    inp("lowfloor", "Low case: floor adjustment", "ratio", -0.04)
    inp("highmult", "High case: capture decline multiplier", "x", 0.5)
    for b, basis in M.BASIS.items():
        cp = P["capture_ratio_to_own_hub_atc"][b]
        inp("cap0_" + b, "Hub capture ratio 2022: " + b, "ratio", cp["2022"])
        inp("capd_" + b, "Hub capture decline: " + b, "points pa", cp["decline_pts_pa"])
        inp("capf_" + b, "Hub capture floor: " + b, "ratio", cp["floor"])
        inp("basis_" + b, "Hub-to-node basis: " + b, "ratio", basis)
    inp("curt_full_year", "Curtailment reaches its long-run value in", "year", 2025)
    for b in M.BASIS:
        cs = P["curtailment_pct"][b]
        v0 = cs.get("2022", cs.get("all"))
        v1 = cs.get("2025_onward", cs.get("all"))
        inp("curt0_" + b, "Curtailment 2022: " + b, "%", float(v0))
        inp("curt1_" + b, "Curtailment from 2025: " + b, "%", float(v1))
    ip.section("Price paths (Illustrative)")
    for k, nm in (("north_base", "north_hub_atc_base"), ("north_low", "north_hub_atc_low"), ("north_high", "north_hub_atc_high")):
        ip.series("in_" + k, "North Hub ATC, " + k.split("_")[1] + " (Illustrative)", "USD/MWh",
                  lambda c, nm=nm: float(P[nm][str(2022 + COLS.index(c))]), style="input", fmt="p")
    for k in ("base", "low", "high"):
        ip.series("in_batt_" + k, "Battery merchant revenue, " + k + " (Illustrative)", "USD/kW-yr",
                  lambda c, k=k: float(P["battery_merchant_revenue_usd_per_kw_yr"][k].get(str(2022 + COLS.index(c)), 0.0)), style="input", fmt="p")
    ip.series("in_sofr", "Term SOFR 3M, annual average (approximate)", "%", lambda c: float(M.SOFR[COLS.index(c)]), style="input", fmt="pct")
    ip.series("in_ptc", "R3 PTC rate (2026+ held at 2025 value)", "USD/MWh",
              lambda c: float(TX["ptc_r3_usd_per_mwh"].get(str(2022 + COLS.index(c)), SUPP["ptc_after_2025_usd_per_mwh"])), style="input", fmt="p")
    ip.series("in_macrs5", "MACRS 5-year rates by recovery year (column J = year 1)", "factor",
              lambda c: SUPP["macrs_5"][COLS.index(c)] if COLS.index(c) < len(SUPP["macrs_5"]) else 0.0, style="input", fmt="f")
    ip.series("in_macrs15", "MACRS 15-year rates by recovery year (column J = year 1)", "factor",
              lambda c: SUPP["macrs_15"][COLS.index(c)] if COLS.index(c) < len(SUPP["macrs_15"]) else 0.0, style="input", fmt="f")
    inp("n_macrs5", "MACRS 5-year recovery years", "years", len(SUPP["macrs_5"]))
    inp("n_macrs15", "MACRS 15-year recovery years", "years", len(SUPP["macrs_15"]))

    ip.section("Assets")
    for aid in M.AIDS:
        a = A[aid]
        inp(aid + "_mw", aid + " capacity", "MWac", a["mw_ac"])
        inp(aid + "_cod", aid + " COD", "date", d(a["cod"]))
        inp(aid + "_life", aid + " useful life end", "date", d(a["useful_life_end"]))
        inp(aid + "_own", aid + " ownership start", "date", d(M.OWN_START[aid]))
        inp(aid + "_opex", aid + " opex (2022 prices)", "USD/kW-yr", OX[M.OPEX_KEY[aid]])
        inp(aid + "_decom", aid + " decommissioning net of salvage (2022)", "USD/kW", OX["decommissioning_net_of_salvage_usd_per_kw_2022"][M.DECOM_KEY[aid]])
        if aid in M.GEN:
            inp(aid + "_p50", aid + " P50", "GWh/yr", a["p50_gwh"])
            inp(aid + "_p901", aid + " P90 one-year", "% of P50", a["p90_1yr_pct_of_p50"])
            inp(aid + "_p9010", aid + " P90 ten-year", "% of P50", a["p90_10yr_pct_of_p50"])
            inp(aid + "_deg", aid + " degradation", "% pa", a["degradation_pct_pa"])
            inp(aid + "_ref", aid + " P50 reference year", "year", SUPP["p50_reference_year"][aid])
        else:
            inp(aid + "_mwh", aid + " energy capacity", "MWh", a["mwh"])
            inp(aid + "_avail", aid + " availability", "%", a["availability_pct"])
            inp(aid + "_aug1", aid + " augmentation year 1 after COD year", "years", a["augmentation"]["years_after_cod"][0])
            inp(aid + "_aug2", aid + " augmentation year 2 after COD year", "years", a["augmentation"]["years_after_cod"][1])
            inp(aid + "_augpct", aid + " augmentation share of MWh", "%", a["augmentation"]["pct_of_mwh"])
            inp(aid + "_augcost", aid + " augmentation cost (2025 prices)", "USD/kWh", a["augmentation"]["cost_usd_per_kwh_2025"])
    for ck_, cv_ in M.CORR.items():
        inp("rho_" + ck_, "Yield correlation: " + ck_, "rho", cv_)
    inp("avail_gen", "Wind and solar availability relative to P50 basis", "%", SUPP["availability_factor_vs_p50_pct"])
    inp("aug_y0", "Augmentation cost base year", "year", 2025)
    inp("aug_esc", "Augmentation cost escalation", "% pa", SUPP["augmentation_escalation_from_2025_pct"])

    ip.section("Contracts and hedges")
    h = H["R1_fixed_volume_swap"]
    inp("R1_hv", "R1 swap volume (7x24)", "MW", h["volume_mw_atc"]); inp("R1_hk", "R1 swap price (West Hub)", "USD/MWh", h["price_usd_per_mwh"])
    inp("R1_hs", "R1 swap start", "date", d(h["start"])); inp("R1_he", "R1 swap end", "date", d(h["end"]))
    inp("hpd", "Hours per day (unit conversion)", "hours", 24)
    h = H["R2_physical_ppa"]
    inp("R2_hk", "R2 PPA price", "USD/MWh", h["price_usd_per_mwh"]); inp("R2_he", "R2 PPA end", "date", d(h["end"]))
    h = H["R3_proxy_revenue_swap"]
    inp("R3_hfix", "R3 PRS fixed payment", "USD m pa", h["fixed_payment_usd_m_pa"])
    inp("R3_hs", "R3 PRS start", "date", d(h["start"])); inp("R3_he", "R3 PRS end", "date", d(h["end"]))
    h = H["R4_fixed_shape_hedge"]
    inp("R4_hv", "R4 shape hedge volume", "GWh pa", h["annual_volume_gwh"]); inp("R4_hk", "R4 shape hedge price", "USD/MWh", h["price_usd_per_mwh"])
    inp("R4_hs", "R4 hedge start", "date", d(h["start"])); inp("R4_he", "R4 hedge end", "date", d(h["end"]))
    h = H["R5_virtual_ppa"]
    inp("R5_hk", "R5 vPPA strike", "USD/MWh", h["strike_usd_per_mwh"]); inp("R5_he", "R5 vPPA end", "date", d(h["end"]))
    h = H["R6_toll"]
    inp("R6_hk", "R6 toll", "USD/kW-month", h["toll_usd_per_kw_month"]); inp("mpy", "Months per year", "months", 12)
    inp("R6_hs", "R6 toll start", "date", d(h["start"])); inp("R6_he", "R6 toll end", "date", d(h["end"]))
    inp("R6_hg", "R6 availability guarantee", "%", h["availability_guarantee_pct"])
    h = H["R7_revenue_floor"]
    inp("R7_hf", "R7 revenue floor", "USD/kW-yr", h["floor_usd_per_kw_yr"]); inp("R7_hp", "R7 floor premium", "USD/kW-yr", h["premium_usd_per_kw_yr"])
    inp("R7_hsh", "R7 upside share to Galloway", "%", h["upside_share_pct_above_140_usd_per_kw_yr"]); inp("R7_hth", "R7 upside share threshold", "USD/kW-yr", 140.0)
    inp("R7_hs", "R7 floor start", "date", d(h["start"])); inp("R7_he", "R7 floor end", "date", d(h["end"]))
    h = H["R8_fixed_shape_hedge"]
    inp("R8_hv", "R8 shape hedge volume", "GWh pa", h["annual_volume_gwh"]); inp("R8_hk", "R8 shape hedge price (South Hub)", "USD/MWh", h["price_usd_per_mwh"])
    inp("R8_hs", "R8 hedge start", "date", d(h["start"])); inp("R8_he", "R8 hedge end", "date", d(h["end"]))
    for aid in ("R3", "R5"):
        te = A[aid]["tax_equity"]
        inp(aid + "_tec", aid + " tax equity cash share before flip", "%", te["pre_flip_cash_to_te_pct"])
        inp(aid + "_tet", aid + " tax equity tax share before flip", "%", te["pre_flip_tax_to_te_pct"])
        inp(aid + "_tep", aid + " tax equity share after flip", "%", te["post_flip_cash_and_tax_to_te_pct"])
        inp(aid + "_flip", aid + " expected flip date", "date", d(te["expected_flip"]))
    inp("ptc_years", "PTC term", "years", SUPP["ptc_term_years"])

    ip.section("Operating costs and tax")
    inp("land", "Wind land lease", "% of revenue", OX["land_lease_wind_pct_of_revenue"])
    inp("ins_step", "Insurance step-up", "%", OX["insurance_step_up_2023_pct"])
    inp("ins_share", "Insurance share of opex", "%", SUPP["insurance_share_of_opex_pct"])
    inp("ins_year", "Insurance step-up year", "year", 2023)
    inp("bondpct", "Decommissioning surety cost", "% of bond pa", 0.6)
    inp("mt_rate", "Texas margin tax rate", "%", 0.75)
    inp("mt_base", "Texas margin tax deemed margin", "% of revenue", 70.0)
    inp("am", "Asset management cost (2022 prices)", "USD m pa", INP["owner"]["asset_management_cost_usd_m_pa_2022"])
    inp("am_start", "Asset management cost start", "date", d("2022-03-22"))
    inp("tax", "Federal income tax rate", "%", TX["federal_rate_pct"])
    inp("nol", "NOL use limit", "% of taxable income", 80.0)
    inp("alloc5", "Purchase price allocated to 5-year MACRS", "%", 85.0)
    inp("alloc15", "Purchase price allocated to 15-year MACRS", "%", 10.0)
    bonus = TX["bonus_depreciation_pct_by_placed_in_service_or_acquired_year"]
    inp("bonus22", "Bonus depreciation, 2022 acquisitions", "%", float(bonus["2022"]))
    inp("bonus23", "Bonus depreciation, 2023 acquisitions", "%", float(bonus["2023"]))
    inp("bonus24", "Bonus depreciation, 2024 acquisitions", "%", float(bonus["2024"]))
    inp("itc7", "R7 ITC rate", "%", TX["itc_r7_pct"]); inp("itc7e", "R7 ITC eligible basis", "% of price", TX["itc_r7_eligible_basis_pct_of_price"])
    inp("itc8", "R8 ITC rate", "%", TX["itc_r8_pct"]); inp("itc8e", "R8 ITC eligible basis", "% of price", TX["itc_r8_eligible_basis_pct_of_price"])
    inp("itcpx", "ITC transfer price", "USD per USD of credit", TX["itc_transfer_price_per_usd_of_credit"])
    inp("itcbr", "ITC basis reduction", "share of credit", SUPP["itc_basis_reduction_share"])

    ip.section("Acquisitions")
    acq = INP["acquisitions"]
    inp("a1_date", "A1 closing", "date", d("2022-03-22")); inp("a1_price", "A1 enterprise value (bid price)", "USD m", acq["A1"]["enterprise_value_usd_m"])
    inp("a1_costs", "A1 transaction costs", "USD m", acq["A1"]["transaction_costs_usd_m"])
    inp("a2_date", "A2 closing", "date", d("2023-08-31")); inp("a2_price", "A2 price", "USD m", acq["A2"]["enterprise_value_usd_m"])
    inp("a2_costs", "A2 transaction costs", "USD m", acq["A2"]["transaction_costs_usd_m"])
    inp("a3_date", "A3 signing and deposit", "date", d("2024-02-15")); inp("a3_r7", "A3 R7 price", "USD m", acq["A3"]["kerrigan_price_usd_m"])
    inp("a3_r8", "A3 R8 price", "USD m", acq["A3"]["barlow_price_usd_m"]); inp("a3_dep", "R8 deposit", "% of price", acq["A3"]["barlow_deposit_pct"])
    inp("a3_costs", "A3 transaction costs", "USD m", acq["A3"]["transaction_costs_usd_m"])

    ip.section("Debt")
    t = D["opco_term_loan_2022"]
    inp("tl_date", "Opco TL date", "date", d(t["date"])); inp("tl_end", "Opco TL notional amortization to", "date", d(t["notional_amortization_to"]))
    inp("tl_m1", "Opco TL margin to step date", "%", t["margin_pct"]["to_2026-03-22"]); inp("tl_m2", "Opco TL margin after step date", "%", t["margin_pct"]["after"])
    inp("tl_step", "Opco TL margin step date", "date", d("2026-03-22")); inp("tl_fee", "Opco TL upfront fee", "%", t["upfront_fee_pct"])
    for bk in M.BUCKETS:
        inp("tl_d_" + bk, "Opco TL sizing DSCR, " + bk, "x", t["sizing_dscr_x_by_revenue_bucket"][bk], fmt="x")
    inp("tl_d99", "Opco TL P99 one-year minimum DSCR", "x", t["p99_1yr_dscr_min_x"], fmt="x")
    inp("tl_hr", "Opco TL hedge ratio", "%", t["hedge"]["ratio_pct"]); inp("tl_hf", "Opco TL swap fixed rate", "%", t["hedge"]["fixed_pct"])
    inp("tl_hto", "Opco TL swap end", "date", d(t["hedge"]["to"]))
    hc = D["holdco_term_loan_2022"]
    inp("hc_date", "Holdco TLB date", "date", d(hc["date"])); inp("hc_mat", "Holdco TLB maturity", "date", d(hc["maturity"]))
    inp("hc_m", "Holdco TLB margin", "%", hc["margin_pct"]); inp("hc_floor", "Holdco SOFR floor", "%", hc["sofr_floor_pct"])
    inp("hc_oid", "Holdco TLB OID", "% of face", hc["oid_pct"]); inp("hc_am", "Holdco TLB amortization", "% pa", hc["amortization_pct_pa"])
    inp("hc_sw", "Holdco excess cash sweep", "%", hc["excess_cash_sweep_pct"]); inp("hc_cov", "Holdco sizing coverage", "x", 1.75, fmt="x")
    inp("hc_cap", "Holdco debt cap", "% of opco equity value", 45.0)
    inp("hc_t0", "Holdco TLB test years from", "year", SUPP["holdco_test_years_2022"][0]); inp("hc_t1", "Holdco TLB test years to", "year", SUPP["holdco_test_years_2022"][1])
    rf = D["redfern_loan_2023"]
    inp("rf_date", "Redfern loan date", "date", d(rf["date"])); inp("rf_mat", "Redfern loan maturity", "date", d(rf["maturity"]))
    inp("rf_m", "Redfern margin", "%", rf["margin_pct"]); inp("rf_fee", "Redfern upfront fee", "%", rf["upfront_fee_pct"])
    inp("rf_d", "Redfern sizing DSCR on toll cash flow", "x", 1.35, fmt="x")
    inp("rf_hr", "Redfern hedge ratio", "%", rf["hedge"]["ratio_pct"]); inp("rf_hf", "Redfern swap fixed rate", "%", rf["hedge"]["fixed_pct"])
    hi = D["holdco_incremental_2024"]
    inp("hi_date", "Holdco incremental date", "date", d(hi["date"])); inp("hi_mat", "Holdco incremental maturity", "date", d(hi["maturity"]))
    inp("hi_m", "Holdco incremental margin", "%", hi["margin_pct"]); inp("hi_oid", "Holdco incremental OID", "% of face", hi["oid_pct"])
    inp("hi_am", "Holdco incremental amortization", "% pa", SUPP["holdco_amort_pct_pa_incremental"])
    inp("hi_t0", "Incremental test years from", "year", SUPP["holdco_test_years_2024"][0]); inp("hi_t1", "Incremental test years to", "year", SUPP["holdco_test_years_2024"][1])
    u = D["refinancing_2025"]["uspp_notes"]
    inp("ref_year", "Refinancing year (modeled at December 31)", "year", 2025); inp("ref_date", "Refinancing date (modeled)", "date", d("2025-12-31"))
    inp("u_y0", "USPP first debt service year", "year", SUPP["uspp_first_year"])
    for k in ("A", "B", "C"):
        inp("u_ten" + k, "USPP Series %s tenor" % k, "years", u["series"][k]["tenor_years"])
        inp("u_cpn" + k, "USPP Series %s coupon" % k, "%", u["series"][k]["coupon_pct"])
    for bk in M.BUCKETS:
        inp("u_d_" + bk, "USPP sizing DSCR, " + bk, "x", u["sizing_dscr_x_by_revenue_bucket"][bk], fmt="x")
    inp("u_d99", "USPP P99 one-year minimum DSCR", "x", u["p99_1yr_dscr_min_x"], fmt="x")
    inp("u_cost", "USPP transaction costs", "% of notes", u["transaction_costs_pct"])
    inp("swr", "SOFR swap rate for unwinds", "%", 3.55)
    hr = D["refinancing_2025"]["holdco_repricing"]
    inp("hn_m", "Repriced holdco margin", "%", hr["new_margin_pct"]); inp("hn_mat", "Repriced holdco maturity", "date", d(hr["new_maturity"]))
    inp("hn_oid", "Repriced holdco OID", "% of face", hr["oid_pct"]); inp("hn_am", "Repriced holdco amortization", "% pa", SUPP["holdco_amort_pct_pa_repriced"])
    inp("hn_t0", "Repricing test years from", "year", SUPP["holdco_test_years_2025"][0]); inp("hn_t1", "Repricing test years to", "year", SUPP["holdco_test_years_2025"][1])

    ip.section("Valuation")
    un = VAL["discount_rates_nominal_post_tax_pct"]["unlevered"]; lv = VAL["discount_rates_nominal_post_tax_pct"]["levered_equity"]
    for k in ("contracted", "hedged", "merchant", "storage_merchant", "terminal_post_2040"):
        inp("u_" + k, "Unlevered discount rate, " + k, "%", un[k])
    inp("term_after", "Terminal rate applies to cash flows after", "year", 2040)
    for k in ("contracted", "hedged", "merchant", "storage_merchant"):
        inp("l_" + k, "Levered equity discount rate, " + k, "%", lv[k])
    inp("nav_date", "NAV date", "date", d("2025-12-31"))

    ip.section("Uri-type stress (R1)")
    inp("uri_h", "Event duration", "hours", 72.0); inp("uri_p", "Price during event", "USD/MWh", 5000.0); inp("uri_a", "R1 availability during event", "%", 15.0)

    # ---------------------------------------------------------------- Time
    tm = B.sheet("Time", "Time")
    tm.ws["D4"] = "Year"
    tm.r = 4
    tm.series("year", "Year", "year", lambda c: "=%s" % I("y0") if c == FC else "=%s4+1" % PREV[c], fmt="int")
    tm.series("ys", "Period start (prior December 31)", "date", lambda c: "=DATE(%s4,1,1)-1" % c, fmt="date")
    tm.series("ye", "Period end (December 31)", "date", lambda c: "=DATE(%s4+1,1,1)-1" % c, fmt="date")
    tm.series("days", "Days in period", "days", lambda c: "=%s6-%s5" % (c, c), fmt="int")
    tm.series("ysb", "Years since price base year", "years", lambda c: "=%s4-%s" % (c, I("ybase")), fmt="int")
    tm.series("esc", "Opex escalation factor", "factor", lambda c: "=(1+%s/100)^%s8" % (I("infl"), c), fmt="f")
    tm.series("insf", "Insurance step-up factor", "factor", lambda c: "=1+%s/100*%s/100*(%s4>=%s)" % (I("ins_share"), I("ins_step"), c, I("ins_year")), fmt="f")
    tm.ws.freeze_panes = "J5"
    T = lambda k, c: "Time!%s$%d" % (c, B.rows[k][1])

    def FR(c, start, end):
        """Day-count fraction of period c between two date expressions."""
        return "MAX(0,MIN(%s,%s)-MAX(%s,%s))/%s" % (end, T("ye", c), start, T("ys", c), T("days", c))

    def PRE(c, date):
        """Fraction of period c before a date."""
        return "MAX(0,MIN(%s,%s)-%s)/%s" % (date, T("ye", c), T("ys", c), T("days", c))

    def WIN(c, y0, y1):
        return "(%s>=%s)*(%s<=%s)" % (T("year", c), y0, T("year", c), y1)

    # ---------------------------------------------------------------- Operations
    op = B.sheet("Operations", "Operations: asset yield, hedges, revenue buckets, opex and cash flow")
    op.header_time()

    def block(tag, pidx, vidx, wsc, curt, opexf, battsw, live):
        PK = (lambda k: k) if live else (lambda k: None)
        op.section("Block %s: %s" % (tag, {"L": "LIVE case (Inputs switches)", "B": "Sizing case: base prices, P50 volumes",
                                           "Q": "Sizing test: base prices, P99 one-year volumes"}[tag]))
        op.scalar(tag + ".pidx", "Price scenario index", "index", "=" + pidx, style="link", fmt="int")
        op.scalar(tag + ".vidx", "Volume case index", "index", "=" + vidx, style="link", fmt="int")
        op.scalar(tag + ".wsc", "West solar capture shift", "points", "=" + wsc, style="link", fmt="f")
        op.scalar(tag + ".curt", "Curtailment added", "% points", "=" + curt, style="link", fmt="f")
        op.scalar(tag + ".opexf", "Opex factor", "factor", "=" + opexf, style="link", fmt="f")
        op.scalar(tag + ".bidx", "Battery revenue curve index", "index", "=IF(%s=1,2,%s)" % (battsw, I(tag + ".pidx")) if False else
                  "=IF(%s=1,2,%s)" % (battsw, B.C(tag + ".pidx")), fmt="int")
        px, bx = B.C(tag + ".pidx"), B.C(tag + ".bidx")
        pre = tag + "."
        op.series(pre + "north", "North Hub ATC", "USD/MWh", lambda c: "=CHOOSE(%s,%s,%s,%s)" % (px, B.R("in_north_base", c), B.R("in_north_low", c), B.R("in_north_high", c)), fmt="p", pykey=PK("portfolio.north_atc"))
        hubs = {"West Hub": "west", "South Hub": "south", "Houston Hub": "houston"}
        for hname, hk in hubs.items():
            op.series(pre + hk, hname + " ATC", "USD/MWh", lambda c, hk=hk: "=%s*%s" % (B.R(pre + "north", c), I("hub_" + hk)), fmt="p", pykey=PK("portfolio.%s_atc" % hk))
        op.series(pre + "batt", "Battery merchant revenue", "USD/kW-yr", lambda c: "=CHOOSE(%s,%s,%s,%s)" % (bx, B.R("in_batt_base", c), B.R("in_batt_low", c), B.R("in_batt_high", c)), fmt="p", pykey=PK("portfolio.batt_rate"))
        for bk in M.BASIS:
            adj = "+%s/100" % B.C(tag + ".wsc") if bk == "west_solar" else ""
            op.series(pre + "cap_" + bk, "Hub capture ratio: " + bk, "ratio",
                      lambda c, bk=bk, adj=adj: "=MAX(%s+CHOOSE(%s,0,%s,0),%s-%s/100*CHOOSE(%s,1,%s,%s)*%s)%s" % (
                          I("capf_" + bk), px, I("lowfloor"), I("cap0_" + bk), I("capd_" + bk), px, I("lowmult"), I("highmult"), T("ysb", c), adj),
                      fmt="f", pykey=PK("portfolio.cap_hub_" + bk))
        HUBROW = {"R1": "west", "R2": "south", "R3": "west", "R4": "west", "R5": "west", "R6": "north", "R7": "houston", "R8": "south"}
        for aid in M.AIDS:
            a = A[aid]
            k = lambda f: "%s%s.%s" % (pre, aid, f)
            pk = lambda f: PK("%s.%s" % (aid, f))
            R = lambda f, c: B.R(k(f), c)
            op.note("%s %s (%s)" % (aid, a["name"], a["technology"]))
            op.series(k("op_frac"), aid + " operating fraction", "fraction", lambda c: "=" + FR(c, I(aid + "_cod"), I(aid + "_life")), fmt="f", pykey=pk("op_frac"))
            op.series(k("own_frac"), aid + " owned fraction", "fraction", lambda c: "=" + FR(c, "MAX(%s,%s)" % (I(aid + "_own"), I(aid + "_cod")), I(aid + "_life")), fmt="f")
            op.series(k("own_share"), aid + " owned share of operating period", "fraction", lambda c: "=IF(%s>0,%s/%s,0)" % (R("op_frac", c), R("own_frac", c), R("op_frac", c)), fmt="f", pykey=pk("own_share"))
            hubref = (lambda c: B.R(pre + "north", c)) if HUBROW[aid] == "north" else (lambda c: B.R(pre + HUBROW[aid], c))
            op.series(k("hub_atc"), aid + " own hub ATC", "USD/MWh", lambda c: "=" + hubref(c), fmt="p", pykey=pk("hub_atc"))
            if aid in M.GEN:
                bk = a["capture_bucket"]
                op.series(k("vf"), aid + " volume factor", "factor", lambda c: "=CHOOSE(%s,1,%s/100,%s/100,%s/100)" % (B.C(tag + ".vidx"), I(aid + "_p901"), I(aid + "_p9010"), B.C("ys_%s_p99_1yr" % aid)), fmt="f")
                op.series(k("deg"), aid + " degradation factor", "factor", lambda c: "=(1-%s/100)^MAX(0,%s-%s)" % (I(aid + "_deg"), T("year", c), I(aid + "_ref")), fmt="f", pykey=pk("deg"))
                op.series(k("curt"), aid + " curtailment", "fraction", lambda c: "=(IF(%s>=%s,%s,%s+(%s-%s)*(%s-%s)/(%s-%s))+%s)/100" % (
                    T("year", c), I("curt_full_year"), I("curt1_" + bk), I("curt0_" + bk), I("curt1_" + bk), I("curt0_" + bk), T("year", c), I("y0"), I("curt_full_year"), I("y0"), B.C(tag + ".curt")), fmt="f", pykey=pk("curt"))
                op.series(k("gen_full"), aid + " net generation, full year", "GWh", lambda c: "=%s*%s*%s/100*%s*(1-%s)" % (I(aid + "_p50"), R("vf", c), I("avail_gen"), R("deg", c), R("curt", c)), fmt="gwh", pykey=pk("gen_full"))
                op.series(k("gen"), aid + " net generation", "GWh", lambda c: "=%s*%s" % (R("gen_full", c), R("op_frac", c)), fmt="gwh", total="SUM", pykey=pk("gen"))
                op.series(k("cap_hub"), aid + " hub capture ratio", "ratio", lambda c: "=" + B.R(pre + "cap_" + bk, c), fmt="f", pykey=pk("cap_hub"))
                op.series(k("cap_node"), aid + " node capture ratio", "ratio", lambda c: "=%s-%s" % (R("cap_hub", c), I("basis_" + bk)), fmt="f", pykey=pk("cap_node"))
                op.series(k("node_price"), aid + " realized node price", "USD/MWh", lambda c: "=%s*%s" % (R("hub_atc", c), R("cap_node", c)), fmt="p", pykey=pk("node_price"))
            # contract rows
            if aid == "R1":
                op.series(k("con_frac"), "R1 swap term fraction", "fraction", lambda c: "=" + FR(c, I("R1_hs") + "-1", I("R1_he")), fmt="f", pykey=pk("con_frac"))
                op.series(k("con_vol"), "R1 swap volume", "GWh", lambda c: "=%s*%s*%s/1000*%s" % (I("R1_hv"), T("days", c), I("hpd"), R("con_frac", c)), fmt="gwh", pykey=pk("con_vol"))
                op.series(k("settle"), "R1 swap settlement (receive fixed, pay West Hub)", "USD m", lambda c: "=%s*(%s-%s)/1000" % (R("con_vol", c), I("R1_hk"), R("hub_atc", c)), total="SUM", pykey=pk("settle"))
                op.series(k("mkt_gen"), "R1 generation sold at node", "GWh", lambda c: "=" + R("gen", c), fmt="gwh", pykey=pk("mkt_gen"))
                op.series(k("rev_contracted"), "R1 contracted revenue", "USD m", lambda c: "=0", pykey=pk("rev_contracted"))
                op.series(k("rev_hedged"), "R1 hedged revenue (swap volume x price)", "USD m", lambda c: "=%s*%s/1000" % (R("con_vol", c), I("R1_hk")), pykey=pk("rev_hedged"))
            elif aid == "R2":
                op.series(k("con_frac"), "R2 PPA term fraction", "fraction", lambda c: "=" + FR(c, I("R2_cod"), I("R2_he")), fmt="f", pykey=pk("con_frac"))
                op.series(k("con_vol"), "R2 PPA volume (as generated)", "GWh", lambda c: "=%s*%s" % (R("gen_full", c), R("con_frac", c)), fmt="gwh", pykey=pk("con_vol"))
                op.series(k("settle"), "R2 PPA revenue", "USD m", lambda c: "=%s*%s/1000" % (R("con_vol", c), I("R2_hk")), total="SUM", pykey=pk("settle"))
                op.series(k("mkt_gen"), "R2 generation sold at node", "GWh", lambda c: "=%s-%s" % (R("gen", c), R("con_vol", c)), fmt="gwh", pykey=pk("mkt_gen"))
                op.series(k("rev_contracted"), "R2 contracted revenue", "USD m", lambda c: "=" + R("settle", c), pykey=pk("rev_contracted"))
                op.series(k("rev_hedged"), "R2 hedged revenue", "USD m", lambda c: "=0", pykey=pk("rev_hedged"))
            elif aid == "R3":
                op.series(k("con_frac"), "R3 PRS term fraction", "fraction", lambda c: "=" + FR(c, I("R3_hs") + "-1", I("R3_he")), fmt="f", pykey=pk("con_frac"))
                op.series(k("con_vol"), "R3 proxy generation", "GWh", lambda c: "=%s*%s" % (R("gen_full", c), R("con_frac", c)), fmt="gwh", pykey=pk("con_vol"))
                op.series(k("settle"), "R3 PRS net (fixed received less proxy revenue paid)", "USD m", lambda c: "=%s*%s-%s*%s*%s/1000" % (I("R3_hfix"), R("con_frac", c), R("con_vol", c), R("cap_hub", c), R("hub_atc", c)), total="SUM", pykey=pk("settle"))
                op.series(k("mkt_gen"), "R3 generation sold at node", "GWh", lambda c: "=" + R("gen", c), fmt="gwh", pykey=pk("mkt_gen"))
                op.series(k("rev_contracted"), "R3 contracted revenue (PRS fixed payment)", "USD m", lambda c: "=%s*%s" % (I("R3_hfix"), R("con_frac", c)), pykey=pk("rev_contracted"))
                op.series(k("rev_hedged"), "R3 hedged revenue", "USD m", lambda c: "=0", pykey=pk("rev_hedged"))
            elif aid in ("R4", "R8"):
                op.series(k("con_frac"), aid + " shape hedge term fraction", "fraction", lambda c: "=" + FR(c, I(aid + "_hs") + "-1", I(aid + "_he")), fmt="f", pykey=pk("con_frac"))
                op.series(k("con_vol"), aid + " shape hedge volume", "GWh", lambda c: "=%s*%s" % (I(aid + "_hv"), R("con_frac", c)), fmt="gwh", pykey=pk("con_vol"))
                op.series(k("settle"), aid + " shape hedge settlement (strike less hub x shape factor)", "USD m", lambda c: "=%s*(%s-%s*%s)/1000" % (R("con_vol", c), I(aid + "_hk"), R("hub_atc", c), R("cap_hub", c)), total="SUM", pykey=pk("settle"))
                op.series(k("mkt_gen"), aid + " generation sold at node", "GWh", lambda c: "=" + R("gen", c), fmt="gwh", pykey=pk("mkt_gen"))
                op.series(k("rev_contracted"), aid + " contracted revenue", "USD m", lambda c: "=0", pykey=pk("rev_contracted"))
                op.series(k("rev_hedged"), aid + " hedged revenue (volume x strike)", "USD m", lambda c: "=%s*%s/1000" % (R("con_vol", c), I(aid + "_hk")), pykey=pk("rev_hedged"))
            elif aid == "R5":
                op.series(k("con_frac"), "R5 vPPA term fraction", "fraction", lambda c: "=" + FR(c, I("R5_cod"), I("R5_he")), fmt="f", pykey=pk("con_frac"))
                op.series(k("con_vol"), "R5 vPPA volume (as generated)", "GWh", lambda c: "=%s*%s" % (R("gen_full", c), R("con_frac", c)), fmt="gwh", pykey=pk("con_vol"))
                op.series(k("settle"), "R5 vPPA settlement (strike less hub capture price)", "USD m", lambda c: "=%s*(%s-%s*%s)/1000" % (R("con_vol", c), I("R5_hk"), R("hub_atc", c), R("cap_hub", c)), total="SUM", pykey=pk("settle"))
                op.series(k("mkt_gen"), "R5 generation sold at node", "GWh", lambda c: "=" + R("gen", c), fmt="gwh", pykey=pk("mkt_gen"))
                op.series(k("rev_contracted"), "R5 contracted revenue (strike x volume)", "USD m", lambda c: "=%s*%s/1000" % (R("con_vol", c), I("R5_hk")), pykey=pk("rev_contracted"))
                op.series(k("rev_hedged"), "R5 hedged revenue", "USD m", lambda c: "=0", pykey=pk("rev_hedged"))
            elif aid == "R6":
                op.series(k("con_frac"), "R6 toll term fraction", "fraction", lambda c: "=" + FR(c, I("R6_hs"), I("R6_he")), fmt="f", pykey=pk("con_frac"))
                op.series(k("settle"), "R6 toll revenue", "USD m", lambda c: "=%s*%s*%s/1000*%s*(1-MAX(0,%s-%s)/100)" % (I("R6_hk"), I("mpy"), I("R6_mw"), R("con_frac", c), I("R6_hg"), I("R6_avail")), total="SUM", pykey=pk("settle"))
                op.series(k("stor_rev"), "R6 merchant revenue after toll", "USD m", lambda c: "=%s*%s/1000*%s/100*(%s-%s)" % (B.R(pre + "batt", c), I("R6_mw"), I("R6_avail"), R("op_frac", c), R("con_frac", c)), total="SUM", pykey=pk("stor_rev"))
                op.series(k("rev_contracted"), "R6 contracted revenue (toll)", "USD m", lambda c: "=" + R("settle", c), pykey=pk("rev_contracted"))
                op.series(k("rev_hedged"), "R6 hedged revenue", "USD m", lambda c: "=0", pykey=pk("rev_hedged"))
            elif aid == "R7":
                op.series(k("con_frac"), "R7 floor term fraction", "fraction", lambda c: "=" + FR(c, I("R7_hs"), I("R7_he")), fmt="f", pykey=pk("con_frac"))
                op.series(k("m"), "R7 merchant revenue, availability-adjusted", "USD/kW-yr", lambda c: "=%s*%s/100" % (B.R(pre + "batt", c), I("R7_avail")), fmt="p")
                op.series(k("settle"), "R7 revenue under floor contract (max of floor, less premium and upside share)", "USD m",
                          lambda c: "=(MAX(%s,%s)-%s-%s/100*MAX(0,%s-%s))*%s/1000*%s" % (R("m", c), I("R7_hf"), I("R7_hp"), I("R7_hsh"), R("m", c), I("R7_hth"), I("R7_mw"), R("con_frac", c)), total="SUM", pykey=pk("settle"))
                op.series(k("stor_rev"), "R7 merchant revenue outside floor term", "USD m", lambda c: "=%s*%s/1000*(%s-%s)" % (R("m", c), I("R7_mw"), R("op_frac", c), R("con_frac", c)), total="SUM", pykey=pk("stor_rev"))
                op.series(k("rev_contracted"), "R7 contracted revenue (floor less premium)", "USD m", lambda c: "=(%s-%s)*%s/1000*%s" % (I("R7_hf"), I("R7_hp"), I("R7_mw"), R("con_frac", c)), pykey=pk("rev_contracted"))
                op.series(k("rev_hedged"), "R7 hedged revenue", "USD m", lambda c: "=0", pykey=pk("rev_hedged"))
            if aid in M.GEN:
                op.series(k("mkt_rev"), aid + " market revenue at node", "USD m", lambda c: "=%s*%s/1000" % (R("mkt_gen", c), R("node_price", c)), total="SUM", pykey=pk("mkt_rev"))
                op.series(k("revenue"), aid + " total revenue", "USD m", lambda c: "=%s+%s" % (R("mkt_rev", c), R("settle", c)), total="SUM", pykey=pk("revenue"))
            else:
                op.series(k("revenue"), aid + " total revenue", "USD m", lambda c: "=%s+%s" % (R("settle", c), R("stor_rev", c)), total="SUM", pykey=pk("revenue"))
            op.series(k("rev_merchant"), aid + " merchant revenue (total less contracted and hedged)", "USD m", lambda c: "=%s-%s-%s" % (R("revenue", c), R("rev_contracted", c), R("rev_hedged", c)), pykey=pk("rev_merchant"))
            op.series(k("opex"), aid + " opex (O&M, land, insurance, property tax, site)", "USD m", lambda c: "=%s*%s/1000*%s*%s*%s*%s" % (I(aid + "_opex"), I(aid + "_mw"), T("esc", c), T("insf", c), R("op_frac", c), B.C(tag + ".opexf")), pykey=pk("opex"))
            if aid in ("R1", "R2", "R3"):
                op.series(k("land"), aid + " wind land lease", "USD m", lambda c: "=%s/100*%s" % (I("land"), R("revenue", c)), pykey=pk("land"))
            else:
                op.series(k("land"), aid + " land lease (in opex)", "USD m", lambda c: "=0", pykey=pk("land"))
            op.series(k("bond"), aid + " decommissioning surety cost", "USD m", lambda c: "=%s/100*%s*%s/1000*%s*%s" % (I("bondpct"), I(aid + "_decom"), I(aid + "_mw"), T("esc", c), R("op_frac", c)), pykey=pk("bond"))
            op.series(k("margin_tax"), aid + " Texas margin tax", "USD m", lambda c: "=%s/100*%s/100*%s" % (I("mt_rate"), I("mt_base"), R("revenue", c)), pykey=pk("margin_tax"))
            op.series(k("ebitda"), aid + " EBITDA", "USD m", lambda c: "=%s-%s-%s-%s-%s" % (R("revenue", c), R("opex", c), R("land", c), R("bond", c), R("margin_tax", c)), total="SUM", pykey=pk("ebitda"))
            if aid in M.STOR:
                op.series(k("aug"), aid + " augmentation capex", "USD m", lambda c: "=IF(OR(%s=YEAR(%s)+%s,%s=YEAR(%s)+%s),%s/100*%s*%s/1000*(1+%s/100)^(%s-%s),0)" % (
                    T("year", c), I(aid + "_cod"), I(aid + "_aug1"), T("year", c), I(aid + "_cod"), I(aid + "_aug2"), I(aid + "_augpct"), I(aid + "_mwh"), I(aid + "_augcost"), I("aug_esc"), T("year", c), I("aug_y0")), pykey=pk("aug"))
            else:
                op.series(k("aug"), aid + " capex", "USD m", lambda c: "=0", pykey=pk("aug"))
            op.series(k("decom"), aid + " decommissioning at end of life", "USD m", lambda c: "=IF(%s=YEAR(%s),%s*%s/1000*%s,0)" % (T("year", c), I(aid + "_life"), I(aid + "_decom"), I(aid + "_mw"), T("esc", c)), pykey=pk("decom"))
            op.series(k("cf"), aid + " pre-tax cash flow, 100% of asset", "USD m", lambda c: "=%s-%s-%s" % (R("ebitda", c), R("aug", c), R("decom", c)), total="SUM", pykey=pk("cf"))
            if aid in ("R3", "R5"):
                op.series(k("pre"), aid + " fraction of year before flip", "fraction", lambda c: "=" + PRE(c, I(aid + "_flip")), fmt="f")
                op.series(k("te_cash"), aid + " tax equity cash share", "fraction", lambda c: "=%s/100*%s+%s/100*(1-%s)" % (I(aid + "_tec"), R("pre", c), I(aid + "_tep"), R("pre", c)), fmt="f", pykey=pk("te_cash"))
                op.series(k("mesa_tax_share"), aid + " Mesa share of taxable income", "fraction", lambda c: "=(1-%s/100)*%s+(1-%s/100)*(1-%s)" % (I(aid + "_tet"), R("pre", c), I(aid + "_tep"), R("pre", c)), fmt="f", pykey=pk("mesa_tax_share"))
            else:
                op.series(k("te_cash"), aid + " tax equity cash share", "fraction", lambda c: "=0", fmt="f", pykey=pk("te_cash"))
                op.series(k("mesa_tax_share"), aid + " Mesa share of taxable income", "fraction", lambda c: "=1", fmt="f", pykey=pk("mesa_tax_share"))
            op.series(k("mesa_cf"), aid + " Mesa share of cash flow", "USD m", lambda c: "=%s*(1-%s)*%s" % (R("cf", c), R("te_cash", c), R("own_share", c)), total="SUM", pykey=pk("mesa_cf"))
            op.series(k("mesa_taxable"), aid + " Mesa taxable operating income", "USD m", lambda c: "=%s*%s*%s" % (R("cf", c), R("mesa_tax_share", c), R("own_share", c)), pykey=pk("mesa_taxable"))
            op.series(k("posttax"), aid + " Mesa unlevered post-tax cash flow (before price shield)", "USD m", lambda c: "=%s-%s/100*%s" % (R("mesa_cf", c), I("tax"), R("mesa_taxable", c)))
            for bk in M.BUCKETS:
                if bk == "merchant":
                    op.series(k("s_merchant"), aid + " merchant share of revenue", "fraction", lambda c: "=1-%s-%s" % (R("s_contracted", c), R("s_hedged", c)), fmt="f", pykey=pk("s_merchant"))
                else:
                    op.series(k("s_" + bk), aid + " %s share of revenue" % bk, "fraction", lambda c, bk=bk: "=IF(%s=0,0,%s/%s)" % (R("revenue", c), R("rev_" + bk, c), R("revenue", c)), fmt="f", pykey=pk("s_" + bk))
            for bk in M.BUCKETS:
                op.series(k("mrev_" + bk), aid + " Mesa-share %s revenue" % bk, "USD m", lambda c, bk=bk: "=%s*%s*(1-%s)" % (R("rev_" + bk, c), R("own_share", c), R("te_cash", c)))
            op.series(k("mesa_rev"), aid + " Mesa-share revenue", "USD m", lambda c: "=%s*%s*(1-%s)" % (R("revenue", c), R("own_share", c), R("te_cash", c)), pykey=pk("mesa_rev"))
            if aid == "R3":
                op.series(k("ptc"), "R3 PTC generated (99% to tax equity before flip)", "USD m", lambda c: "=%s*%s*%s/1000" % (R("gen_full", c), FR(c, I("R3_cod"), "DATE(YEAR(%s)+%s,MONTH(%s),DAY(%s))" % (I("R3_cod"), I("ptc_years"), I("R3_cod"), I("R3_cod"))), B.R("in_ptc", c)), pykey=PK("R3.ptc_total"))
        op.section("Block %s: portfolio" % tag)
        op.series(pre + "am", "Asset management cost", "USD m", lambda c: "=%s*%s*%s" % (I("am"), T("esc", c), FR(c, I("am_start"), I("model_end"))), pykey=PK("portfolio.am_cost"))
        for grp, ids in (("a1", M.A1), ("all", M.AIDS), ("a3", ["R7", "R8"])):
            op.series(pre + "mesa_cf_" + grp, "Mesa cash flow, %s assets" % grp, "USD m", lambda c, ids=ids: "=" + "+".join(B.R("%s%s.mesa_cf" % (pre, a), c) for a in ids))
            for bk in M.BUCKETS:
                op.series(pre + "mrev_%s_%s" % (bk, grp), "Mesa-share %s revenue, %s" % (bk, grp), "USD m", lambda c, ids=ids, bk=bk: "=" + "+".join(B.R("%s%s.mrev_%s" % (pre, a, bk), c) for a in ids),
                          pykey=PK("portfolio.mesa_rev_%s_%s" % (bk, grp)) if grp != "a3" else None)
            op.series(pre + "mrev_" + grp, "Mesa-share revenue, " + grp, "USD m", lambda c, grp=grp: "=" + "+".join(B.R(pre + "mrev_%s_%s" % (bk, grp), c) for bk in M.BUCKETS),
                      pykey=PK("portfolio.mesa_rev_" + grp) if grp != "a3" else None)
        op.series(pre + "cfads_a1", "CFADS, A1 group (opco term loan borrower group)", "USD m", lambda c: "=%s-%s" % (B.R(pre + "mesa_cf_a1", c), B.R(pre + "am", c)), total="SUM", pykey=PK("portfolio.cfads_a1"))
        op.series(pre + "cfads_all", "CFADS, portfolio (all assets)", "USD m", lambda c: "=%s-%s" % (B.R(pre + "mesa_cf_all", c), B.R(pre + "am", c)), total="SUM", pykey=PK("portfolio.cfads_all"))
        op.series(pre + "cfads_a3", "CFADS, R7 and R8", "USD m", lambda c: "=" + B.R(pre + "mesa_cf_a3", c), pykey=PK("portfolio.cfads_a3"))
        for grp in ("a1", "all"):
            for bk in M.BUCKETS:
                if bk == "merchant":
                    op.series(pre + "sh_merchant_" + grp, "Merchant share of Mesa revenue, " + grp, "fraction", lambda c, grp=grp: "=1-%s-%s" % (B.R(pre + "sh_contracted_" + grp, c), B.R(pre + "sh_hedged_" + grp, c)), fmt="f", pykey=PK("portfolio.share_merchant_" + grp))
                else:
                    op.series(pre + "sh_%s_%s" % (bk, grp), "%s share of Mesa revenue, %s" % (bk.capitalize(), grp), "fraction",
                              lambda c, grp=grp, bk=bk: "=IF(%s=0,0,%s/%s)" % (B.R(pre + "mrev_" + grp, c), B.R(pre + "mrev_%s_%s" % (bk, grp), c), B.R(pre + "mrev_" + grp, c)), fmt="f", pykey=PK("portfolio.share_%s_%s" % (bk, grp)))
            for bk in M.BUCKETS:
                op.series(pre + "cfads_%s_%s" % (grp, bk), "CFADS allocated to %s, %s" % (bk, grp), "USD m", lambda c, grp=grp, bk=bk: "=%s*%s" % (B.R(pre + "cfads_" + grp, c), B.R(pre + "sh_%s_%s" % (bk, grp), c)))

    op.section("Yield statistics (normal; sigma_1^2 = sigma_LT^2 + sigma_IAV^2; sigma_10^2 = sigma_LT^2 + sigma_IAV^2/10)")
    for aid in M.GEN:
        yk = lambda f: "ys_%s_%s" % (aid, f)
        op.scalar(yk("s1"), aid + " sigma one-year", "fraction of P50", "=(1-%s/100)/%s" % (I(aid + "_p901"), I("z90")), fmt="f", pykey="ys.%s.sigma_1yr" % aid)
        op.scalar(yk("s10"), aid + " sigma ten-year", "fraction of P50", "=(1-%s/100)/%s" % (I(aid + "_p9010"), I("z90")), fmt="f", pykey="ys.%s.sigma_10yr" % aid)
        op.scalar(yk("iav"), aid + " sigma inter-annual variability", "fraction of P50", "=SQRT((%s^2-%s^2)*%s/(%s-1))" % (B.C(yk("s1")), B.C(yk("s10")), I("n10"), I("n10")), fmt="f", pykey="ys.%s.sigma_iav" % aid)
        op.scalar(yk("lt"), aid + " sigma long-term", "fraction of P50", "=SQRT(%s^2-%s^2/%s)" % (B.C(yk("s10")), B.C(yk("iav")), I("n10")), fmt="f", pykey="ys.%s.sigma_lt" % aid)
        op.scalar(yk("p99_1yr"), aid + " P99 one-year", "% of P50", "=100*(1-%s*%s)" % (I("z99"), B.C(yk("s1"))), fmt="pct", pykey="ys.%s.p99_1yr" % aid)
        op.scalar(yk("p99_10yr"), aid + " P99 ten-year", "% of P50", "=100*(1-%s*%s)" % (I("z99"), B.C(yk("s10"))), fmt="pct", pykey="ys.%s.p99_10yr" % aid)

    block("L", I("scen"), I("volcase"), I("s_wsc"), I("s_curt"), I("s_opex"), I("s_batt"), True)
    block("B", I("sz_price"), I("sz_vol"), I("zero"), I("zero"), I("one"), I("zero"), False)
    block("Q", I("sz_price"), I("sz_vol99"), I("zero"), I("zero"), I("one"), I("zero"), False)

    # Uri stress and diversification (operations analytics)
    op.section("Uri-type stress on R1's fixed-volume swap (R-F03)")
    op.scalar("uri_gen", "R1 generation during event", "MWh", "=%s*%s/100*%s" % (I("R1_mw"), I("uri_a"), I("uri_h")), pykey="uri.gen_mwh")
    op.scalar("uri_swap", "Swap volume during event", "MWh", "=%s*%s" % (I("R1_hv"), I("uri_h")), pykey="uri.swap_mwh")
    op.scalar("uri_short", "Volume shortfall", "MWh", "=%s-%s" % (B.C("uri_swap"), B.C("uri_gen")), pykey="uri.shortfall_mwh")
    op.scalar("uri_pay", "Swap settlement paid", "USD m", "=%s*(%s-%s)/1000000" % (B.C("uri_swap"), I("uri_p"), I("R1_hk")), pykey="uri.swap_payment")
    op.scalar("uri_phys", "Physical revenue", "USD m", "=%s*%s/1000000" % (B.C("uri_gen"), I("uri_p")), pykey="uri.physical_revenue")
    op.scalar("uri_net", "Net cash over the event", "USD m", "=%s-%s" % (B.C("uri_phys"), B.C("uri_pay")), pykey="uri.net_cash")
    op.scalar("uri_vs", "Net cash versus normal hedged revenue for the same hours", "USD m", "=%s-%s*%s/1000000" % (B.C("uri_net"), B.C("uri_swap"), I("R1_hk")), pykey="uri.net_vs_fully_covered")
    op.section("Portfolio yield with inter-asset correlations (R-F01)")
    wind = {"R1", "R2", "R3"}

    def rho(i, j, comp):
        if i == j:
            return "1"
        ti, tj = i in wind, j in wind
        if comp == "lt":
            return I("rho_lt_same_technology") if ti == tj else I("rho_lt_cross_technology")
        if ti != tj:
            return I("rho_iav_wind_solar")
        if ti:
            return I("rho_iav_wind_west_coastal") if "R2" in (i, j) else I("rho_iav_wind_west_west")
        return I("rho_iav_solar_west_south") if "R8" in (i, j) else I("rho_iav_solar_west_west")
    for grp, ids in (("A1", M.A1), ("all_generation", M.GEN)):
        p50 = "+".join(I(a + "_p50") for a in ids)
        op.scalar("dv_%s_p50" % grp, "P50, %s" % grp, "GWh", "=" + p50, pykey="div.%s.p50_gwh" % grp)
        for comp in ("lt", "iav"):
            terms = "+".join("%s*%s*%s*%s*%s" % (I(i + "_p50"), B.C("ys_%s_%s" % (i, comp)), I(j + "_p50"), B.C("ys_%s_%s" % (j, comp)), rho(i, j, comp)) for i in ids for j in ids)
            op.scalar("dv_%s_v%s" % (grp, comp), "Variance, %s component, %s" % (comp, grp), "GWh^2", "=" + terms, fmt="m")
        for kk, nexp in (("1yr", "1"), ("10yr", I("n10"))):
            op.scalar("dv_%s_s%s" % (grp, kk), "Portfolio sigma %s, %s" % (kk, grp), "GWh", "=SQRT(%s+%s/%s)" % (B.C("dv_%s_vlt" % grp), B.C("dv_%s_viav" % grp), nexp), pykey="div.%s.sigma_%s_gwh" % (grp, kk))
            for pk, z in (("p90", "z90"), ("p99", "z99")):
                op.scalar("dv_%s_%s_%s" % (grp, pk, kk), "Portfolio %s %s, %s" % (pk.upper(), kk, grp), "GWh", "=%s-%s*%s" % (B.C("dv_%s_p50" % grp), I(z), B.C("dv_%s_s%s" % (grp, kk))), pykey="div.%s.%s_%s_gwh" % (grp, pk, kk))
            sk = "s1" if kk == "1yr" else "s10"
            corr = "+".join("%s*%s" % (I(a + "_p50"), B.C("ys_%s_%s" % (a, sk))) for a in ids)
            ind = "+".join("(%s*%s)^2" % (I(a + "_p50"), B.C("ys_%s_%s" % (a, sk))) for a in ids)
            op.scalar("dv_%s_%s_c" % (grp, kk), "P90 %s if fully correlated, %s" % (kk, grp), "GWh", "=%s-%s*(%s)" % (B.C("dv_%s_p50" % grp), I("z90"), corr), pykey="div.%s.p90_%s_correlated_gwh" % (grp, kk))
            op.scalar("dv_%s_%s_i" % (grp, kk), "P90 %s if independent, %s" % (kk, grp), "GWh", "=%s-%s*SQRT(%s)" % (B.C("dv_%s_p50" % grp), I("z90"), ind), pykey="div.%s.p90_%s_independent_gwh" % (grp, kk))

    # ---------------------------------------------------------------- Tax (depreciation part first; income tax rows added after Debt)
    tx = B.sheet("Tax", "Tax: depreciation of purchase prices, taxable income, NOL and cash tax")
    tx.header_time()
    tx.section("ITC on R7 and R8 (claimed by the fund and transferred)")
    tx.scalar("itc7_amt", "R7 ITC", "USD m", "=%s/100*%s/100*%s" % (I("itc7"), I("itc7e"), I("a3_r7")), pykey="val.A3.itc7")
    tx.scalar("itc8_amt", "R8 ITC", "USD m", "=%s/100*%s/100*%s" % (I("itc8"), I("itc8e"), I("a3_r8")), pykey="val.A3.itc8")
    tx.section("Tax depreciation (bonus in acquisition year, MACRS half-year on the remainder)")
    lots = [("A1", "=" + I("a1_price"), "a1_date", "bonus22"), ("A2", "=" + I("a2_price"), "a2_date", "bonus23"),
            ("R7", "=%s-%s*%s" % (I("a3_r7"), I("itcbr"), B.C("itc7_amt")), "a3_date", "bonus24"),
            ("R8", "=%s-%s*%s" % (I("a3_r8"), I("itcbr"), B.C("itc8_amt")), "a3_date", "bonus24")]
    for nm, basis, dk, bk in lots:
        tx.scalar("basis_" + nm, "Depreciable basis, " + nm, "USD m", basis)
        tx.series("n_" + nm, "Recovery year index, " + nm, "years", lambda c, dk=dk: "=%s-YEAR(%s)" % (T("year", c), I(dk)), fmt="int")
        tx.series("dep_" + nm, "Tax depreciation, " + nm, "USD m", lambda c, nm=nm, bk=bk: (
            "=%s*((%s+%s)/100*IF(%s=0,%s/100,0)+(1-%s/100)*(%s/100*IF(AND(%s>=0,%s<%s),INDEX(%s,%s+1),0)+%s/100*IF(AND(%s>=0,%s<%s),INDEX(%s,%s+1),0)))" % (
                B.C("basis_" + nm), I("alloc5"), I("alloc15"), B.R("n_" + nm, c), I(bk), I(bk),
                I("alloc5"), B.R("n_" + nm, c), B.R("n_" + nm, c), I("n_macrs5"), B.RR("in_macrs5"), B.R("n_" + nm, c),
                I("alloc15"), B.R("n_" + nm, c), B.R("n_" + nm, c), I("n_macrs15"), B.RR("in_macrs15"), B.R("n_" + nm, c))), total="SUM")
    tx.series("dep", "Tax depreciation, total", "USD m", lambda c: "=" + "+".join(B.R("dep_" + nm, c) for nm, _, _, _ in lots), total="SUM", pykey="finance.dep")
    tx.series("taxable_ops", "Taxable operating income (Mesa shares) less asset management", "USD m",
              lambda c: "=" + "+".join(B.R("L.%s.mesa_taxable" % a, c) for a in M.AIDS) + "-" + B.R("L.am", c), pykey="finance.taxable_ops")

    # ---------------------------------------------------------------- Funding: sizing, sources and uses, refinancing
    fd = B.sheet("Funding", "Funding: debt sizing (base P50 and P99 sizing blocks), sources and uses, 2025 refinancing")
    fd.header_time()
    # Opco TL
    fd.section("Opco term loan, March 22, 2022 (A1 group, sculpted to December 31, 2040)")
    fd.series("tl_f", "Interest period fraction (loan date to notional end)", "fraction", lambda c: "=" + FR(c, I("tl_date"), I("tl_end")), fmt="f", pykey="sz.tl_f")
    fd.series("tl_pre26", "Fraction of year before margin step", "fraction", lambda c: "=" + PRE(c, I("tl_step")), fmt="f")
    fd.series("tl_margin", "Margin", "%", lambda c: "=%s-(%s-%s)*%s" % (I("tl_m2"), I("tl_m2"), I("tl_m1"), B.R("tl_pre26", c)), fmt="pct")
    fd.series("tl_h", "Hedged share (hedge ratio x fraction of year before swap end)", "fraction", lambda c: "=%s/100*%s" % (I("tl_hr"), PRE(c, I("tl_hto"))), fmt="f")
    fd.series("tl_rate", "All-in sizing rate", "%", lambda c: "=%s*%s+(1-%s)*%s+%s" % (B.R("tl_h", c), I("tl_hf"), B.R("tl_h", c), B.R("in_sofr", c), B.R("tl_margin", c)), fmt="pct", pykey="sz.tl_rate")
    fd.series("tl_capb", "Debt-service capacity by bucket (CFADS / bucket DSCR)", "USD m", lambda c: "=" + "+".join("%s/%s" % (B.R("B.cfads_a1_" + bk, c), I("tl_d_" + bk)) for bk in M.BUCKETS), pykey="sz.tl_cap_bucket")
    fd.series("tl_cap99", "Debt-service capacity at P99 (P99 CFADS / 1.00x)", "USD m", lambda c: "=%s/%s" % (B.R("Q.cfads_a1", c), I("tl_d99")), pykey="sz.tl_cap_p99")
    fd.series("tl_ds", "Sculpted debt service", "USD m", lambda c: "=IF(%s>0,MAX(0,MIN(%s,%s)),0)" % (B.R("tl_f", c), B.R("tl_capb", c), B.R("tl_cap99", c)), total="SUM", pykey="sz.tl_ds")
    fd.series("tl_df", "Discount factor to loan date", "factor", lambda c: "=IF(%s=%s,1,%s)/(1+%s/100*%s)" % (T("year", c), I("y0"), "%s%d" % (PREV[c], B.rows["tl_df"][1]) if "tl_df" in B.rows else "0", B.R("tl_rate", c), B.R("tl_f", c)), fmt="f")
    # fix self reference for tl_df (row known now)
    rdf = B.rows["tl_df"][1]
    for cc in COLS:
        fd.ws["%s%d" % (cc, rdf)] = "=IF(%s=%s,1,%s%d)/(1+%s/100*%s)" % (T("year", cc), I("y0"), PREV[cc], rdf, B.R("tl_rate", cc), B.R("tl_f", cc))
    B.map["series"]["sz.tl_df"] = ["Funding", rdf]
    fd.scalar("tl_debt", "Opco term loan amount (PV of sculpted debt service)", "USD m", "=SUMPRODUCT(%s,%s)" % (B.RR("tl_ds"), B.RR("tl_df")), pykey="sz.tl_debt")
    for bk in M.BUCKETS:
        fd.scalar("tl_pv_" + bk, "PV of %s debt-service capacity" % bk, "USD m", "=SUMPRODUCT(%s/%s,%s,--(%s>0))" % (B.RR("B.cfads_a1_" + bk), I("tl_d_" + bk), B.RR("tl_df"), B.RR("tl_f")), pykey="sz.tl_pv_cap_" + bk)
    fd.scalar("tl_p99yrs", "Years in which the P99 test binds", "years", "=SUMPRODUCT(--(%s<%s),--(%s>0))" % (B.RR("tl_cap99"), B.RR("tl_capb"), B.RR("tl_f")), fmt="int", pykey="sz.tl_p99_binds_years")
    fd.series("tl_sopen", "Sculpted schedule: opening balance", "USD m", lambda c: "=IF(%s=YEAR(%s),%s,%s%d)" % (T("year", c), I("tl_date"), B.C("tl_debt"), PREV[c], fd.r + 3), pykey="sz.tl_sched_open")
    fd.series("tl_sint", "Sculpted schedule: interest", "USD m", lambda c: "=%s*%s/100*%s" % (B.R("tl_sopen", c), B.R("tl_rate", c), B.R("tl_f", c)), pykey="sz.tl_sched_int")
    fd.series("tl_sprin", "Sculpted schedule: principal", "USD m", lambda c: "=IF(%s>0,%s-%s,0)" % (B.R("tl_f", c), B.R("tl_ds", c), B.R("tl_sint", c)), total="SUM", pykey="sz.tl_sched_prin")
    fd.series("tl_sclose", "Sculpted schedule: closing balance", "USD m", lambda c: "=%s-%s" % (B.R("tl_sopen", c), B.R("tl_sprin", c)))
    fd.series("dist_a1", "Base P50 distributions from A1 group (CFADS less sculpted debt service)", "USD m", lambda c: "=%s-%s" % (B.R("B.cfads_a1", c), B.R("tl_ds", c)), pykey="sz.dist_a1_base")
    # Holdco TLB
    fd.section("Holdco term loan B, March 22, 2022")
    fd.series("hc_f", "Interest period fraction to maturity", "fraction", lambda c: "=" + FR(c, I("hc_date"), I("hc_mat")), fmt="f")
    fd.series("hc_rate", "Rate (SOFR floored + margin)", "%", lambda c: "=MAX(%s,%s)+%s" % (B.R("in_sofr", c), I("hc_floor"), I("hc_m")), fmt="pct")
    fd.series("hc_amf", "Scheduled amortization per unit of face", "factor", lambda c: "=%s/100*%s" % (I("hc_am"), B.R("hc_f", c)), fmt="f")
    fd.series("hc_bf", "Scheduled balance per unit of face", "factor", lambda c: "=IF(%s=%s,1,%s%d-%s%d)" % (T("year", c), I("y0"), PREV[c], fd.r, PREV[c], fd.r - 1), fmt="f")
    fd.series("hc_k", "Debt service per unit of face", "factor", lambda c: "=%s*%s/100*%s+%s" % (B.R("hc_bf", c), B.R("hc_rate", c), B.R("hc_f", c), B.R("hc_amf", c)), fmt="f", pykey="sz.hc_k")
    fd.series("hc_test", "Coverage test year flag", "flag", lambda c: "=" + WIN(c, I("hc_t0"), I("hc_t1")), fmt="int")
    fd.series("hc_capv", "Face supported at 1.75x coverage", "USD m", lambda c: "=IF(%s>0,%s/(%s*IF(%s>0,%s,1)),%s)" % (B.R("hc_test", c), B.R("dist_a1", c), I("hc_cov"), B.R("hc_k", c), B.R("hc_k", c), I("big")), pykey="sz.hc_cap_vec")
    fd.scalar("hc_face_cov", "Face supported by coverage (minimum over test years)", "USD m", "=MIN(%s)" % B.RR("hc_capv"), pykey="sz.hc_face_cov")

    def levdf(key, label, v0, grp):
        fd.series(key + "_tau", label + ": years from valuation date", "years", lambda c: "=MAX(0,(%s-%s)/%s)" % (T("ye", c), v0, I("dpy")), fmt="f")
        fd.series(key, label + ": levered discount factor weighted by revenue bucket", "factor", lambda c: "=(%s>=%s)*(%s)" % (
            T("ye", c), v0, "+".join("%s*(1+%s/100)^(-%s)" % (B.R(grp % bk, c), I("l_" + bk), B.R(key + "_tau", c)) for bk in M.BUCKETS)), fmt="f")
    levdf("hc_eqdf", "Opco equity value at March 22, 2022", I("a1_date"), "B.sh_%s_a1")
    fd.scalar("eq_val22", "Opco equity value at levered equity rates", "USD m", "=SUMPRODUCT(%s,%s)" % (B.RR("dist_a1"), B.RR("hc_eqdf")), pykey="sz.opco_eq_val_2022")
    fd.scalar("hc_face_cap", "Cap: 45% of opco equity value", "USD m", "=%s/100*%s" % (I("hc_cap"), B.C("eq_val22")), pykey="sz.hc_face_cap")
    fd.scalar("hc_face", "Holdco TLB face", "USD m", "=MIN(%s,%s)" % (B.C("hc_face_cov"), B.C("hc_face_cap")), pykey="sz.hc_face")
    # Redfern
    fd.section("Redfern term loan, August 31, 2023 (toll cash flow only)")
    fd.series("rf_f", "Interest period fraction", "fraction", lambda c: "=" + FR(c, I("rf_date"), I("rf_mat")), fmt="f", pykey="sz.rf_f")
    fd.series("rf_cost", "R6 annualized cash costs (opex, surety, margin tax)", "USD m", lambda c: "=IF(%s>0,(%s+%s+%s)/%s,0)" % (B.R("B.R6.op_frac", c), B.R("B.R6.opex", c), B.R("B.R6.bond", c), B.R("B.R6.margin_tax", c), B.R("B.R6.op_frac", c)))
    fd.series("rf_cf", "Toll cash flow for sizing", "USD m", lambda c: "=(%s*%s*%s/1000-%s)*%s-%s*(%s>0)" % (I("R6_hk"), I("mpy"), I("R6_mw"), B.R("rf_cost", c), B.R("rf_f", c), B.R("B.R6.aug", c), B.R("rf_f", c)), pykey="sz.rf_cf")
    fd.series("rf_ds", "Sculpted debt service (toll CF / 1.35x)", "USD m", lambda c: "=IF(%s>0,%s/%s,0)" % (B.R("rf_f", c), B.R("rf_cf", c), I("rf_d")), pykey="sz.rf_ds")
    fd.series("rf_rate", "All-in rate", "%", lambda c: "=%s/100*%s+(1-%s/100)*%s+%s" % (I("rf_hr"), I("rf_hf"), I("rf_hr"), B.R("in_sofr", c), I("rf_m")), fmt="pct", pykey="sz.rf_rate")
    r_ = fd.r
    fd.series("rf_df", "Discount factor", "factor", lambda c: "=IF(%s=%s,1,%s%d)/(1+%s/100*%s)" % (T("year", c), I("y0"), PREV[c], r_, B.R("rf_rate", c), B.R("rf_f", c)), fmt="f")
    fd.scalar("rf_debt", "Redfern loan amount", "USD m", "=SUMPRODUCT(%s,%s)" % (B.RR("rf_ds"), B.RR("rf_df")), pykey="sz.rf_debt")
    r_ = fd.r
    fd.series("rf_sopen", "Sculpted schedule: opening balance", "USD m", lambda c: "=IF(%s=YEAR(%s),%s,%s%d)" % (T("year", c), I("rf_date"), B.C("rf_debt"), PREV[c], r_ + 2), pykey="sz.rf_sched_open")
    fd.series("rf_sprin", "Sculpted schedule: principal", "USD m", lambda c: "=IF(%s>0,%s-%s*%s/100*%s,0)" % (B.R("rf_f", c), B.R("rf_ds", c), B.R("rf_sopen", c), B.R("rf_rate", c), B.R("rf_f", c)), total="SUM", pykey="sz.rf_sched_prin")
    fd.series("rf_sclose", "Sculpted schedule: closing balance", "USD m", lambda c: "=%s-%s" % (B.R("rf_sopen", c), B.R("rf_sprin", c)))
    # Incremental
    fd.section("Holdco incremental term loan, February 15, 2024 (R7 and R8)")
    fd.series("hi_f", "Interest period fraction to maturity", "fraction", lambda c: "=" + FR(c, I("hi_date"), I("hi_mat")), fmt="f")
    fd.series("hi_rate", "Rate (SOFR floored + margin)", "%", lambda c: "=MAX(%s,%s)+%s" % (B.R("in_sofr", c), I("hc_floor"), I("hi_m")), fmt="pct")
    fd.series("hi_amf", "Scheduled amortization per unit of face", "factor", lambda c: "=%s/100*%s" % (I("hi_am"), B.R("hi_f", c)), fmt="f")
    fd.series("hi_bf", "Scheduled balance per unit of face", "factor", lambda c: "=IF(%s=%s,1,%s%d-%s%d)" % (T("year", c), I("y0"), PREV[c], fd.r, PREV[c], fd.r - 1), fmt="f")
    fd.series("hi_k", "Debt service per unit of face", "factor", lambda c: "=%s*%s/100*%s+%s" % (B.R("hi_bf", c), B.R("hi_rate", c), B.R("hi_f", c), B.R("hi_amf", c)), fmt="f", pykey="sz.hi_k")
    fd.series("hi_test", "Coverage test year flag", "flag", lambda c: "=" + WIN(c, I("hi_t0"), I("hi_t1")), fmt="int")
    fd.series("hi_capv", "Face supported at 1.75x on R7 and R8 distributions", "USD m", lambda c: "=IF(%s>0,%s/(%s*IF(%s>0,%s,1)),%s)" % (B.R("hi_test", c), B.R("B.cfads_a3", c), I("hc_cov"), B.R("hi_k", c), B.R("hi_k", c), I("big")), pykey="sz.hi_cap_vec")
    fd.scalar("hi_face", "Holdco incremental face", "USD m", "=MIN(%s)" % B.RR("hi_capv"), pykey="sz.hi_face")
    # USPP
    fd.section("2025 refinancing: USPP senior secured notes (sized on base P50 and P99 blocks)")
    fd.series("u_flA", "Series A amortization years", "flag", lambda c: "=" + WIN(c, I("u_y0"), "%s+%s-1" % (I("u_y0"), I("u_tenA"))), fmt="int")
    fd.series("u_flB", "Series B amortization years", "flag", lambda c: "=" + WIN(c, "%s+%s" % (I("u_y0"), I("u_tenA")), "%s+%s-1" % (I("u_y0"), I("u_tenB"))), fmt="int")
    fd.series("u_flC", "Series C amortization years", "flag", lambda c: "=" + WIN(c, "%s+%s" % (I("u_y0"), I("u_tenB")), "%s+%s-1" % (I("u_y0"), I("u_tenC"))), fmt="int")
    fd.series("u_f", "Notes outstanding flag", "flag", lambda c: "=%s+%s+%s" % (B.R("u_flA", c), B.R("u_flB", c), B.R("u_flC", c)), fmt="int", pykey="sz.u_f")
    fd.series("u_ct", "Coupon of the series amortizing in the year", "%", lambda c: "=%s*%s+%s*%s+%s*%s" % (B.R("u_flA", c), I("u_cpnA"), B.R("u_flB", c), I("u_cpnB"), B.R("u_flC", c), I("u_cpnC")), fmt="pct")
    fd.series("u_capb", "Debt-service capacity by bucket", "USD m", lambda c: "=" + "+".join("%s/%s" % (B.R("B.cfads_all_" + bk, c), I("u_d_" + bk)) for bk in M.BUCKETS), pykey="sz.u_cap_bucket")
    fd.series("u_cap99", "Debt-service capacity at P99 (1.05x)", "USD m", lambda c: "=%s/%s" % (B.R("Q.cfads_all", c), I("u_d99")), pykey="sz.u_cap_p99")
    fd.series("u_ds", "Sculpted debt service", "USD m", lambda c: "=IF(%s>0,MAX(0,MIN(%s,%s)),0)" % (B.R("u_f", c), B.R("u_capb", c), B.R("u_cap99", c)), total="SUM", pykey="sz.u_ds")
    rP = fd.r
    rA, rB_, rC = rP + 1, rP + 2, rP + 3
    fd.series("u_prin", "Principal, solved backward: (DS - sum of coupons x next-year opening balances) / (1 + coupon of amortizing series)", "USD m",
              lambda c: "=IF(%s>0,(%s-%s/100*%s%d-%s/100*%s%d-%s/100*%s%d)/(1+%s/100),0)" % (B.R("u_f", c), B.R("u_ds", c), I("u_cpnA"), NEXT[c], rA, I("u_cpnB"), NEXT[c], rB_, I("u_cpnC"), NEXT[c], rC, B.R("u_ct", c)), total="SUM", pykey="sz.u_prin")
    fd.series("u_oA", "Series A opening balance", "USD m", lambda c: "=%s%d+%s*%s" % (NEXT[c], rA, B.R("u_prin", c), B.R("u_flA", c)))
    fd.series("u_oB", "Series B opening balance", "USD m", lambda c: "=%s%d+%s*%s" % (NEXT[c], rB_, B.R("u_prin", c), B.R("u_flB", c)))
    fd.series("u_oC", "Series C opening balance", "USD m", lambda c: "=%s%d+%s*%s" % (NEXT[c], rC, B.R("u_prin", c), B.R("u_flC", c)))
    fd.series("u_open", "Notes opening balance", "USD m", lambda c: "=(%s+%s+%s)*%s" % (B.R("u_oA", c), B.R("u_oB", c), B.R("u_oC", c), B.R("u_f", c)), pykey="sz.u_open")
    fd.series("u_int", "Notes interest", "USD m", lambda c: "=(%s/100*%s+%s/100*%s+%s/100*%s)*%s" % (I("u_cpnA"), B.R("u_oA", c), I("u_cpnB"), B.R("u_oB", c), I("u_cpnC"), B.R("u_oC", c), B.R("u_f", c)), total="SUM", pykey="sz.u_int")
    for k_ in ("A", "B", "C"):
        fd.scalar("u_size" + k_, "Series %s size" % k_, "USD m", "=SUMIF(%s,%s,%s)" % ("Time!$%s$4:$%s$4" % (FC, LC), I("u_y0"), B.RR("u_o" + k_)), pykey="sz.u_series_size." + k_)
    fd.scalar("u_size", "USPP notes total", "USD m", "=%s+%s+%s" % (B.C("u_sizeA"), B.C("u_sizeB"), B.C("u_sizeC")), pykey="sz.u_size")
    for k_ in ("A", "B", "C"):
        fd.scalar("u_sh" + k_, "Series %s share" % k_, "%", "=100*%s/%s" % (B.C("u_size" + k_), B.C("u_size")), fmt="pct", pykey="sz.u_series_share." + k_)
    fd.scalar("u_cpn", "Issue-weighted blended coupon", "%", "=(%s*%s+%s*%s+%s*%s)/%s" % (B.C("u_sizeA"), I("u_cpnA"), B.C("u_sizeB"), I("u_cpnB"), B.C("u_sizeC"), I("u_cpnC"), B.C("u_size")), fmt="pct", pykey="sz.u_coupon")
    fd.series("u_dfb", "Discount factor at blended coupon (bucket exhibit)", "factor", lambda c: "=(1+%s/100)^(-(%s-%s))*%s" % (B.C("u_cpn"), T("year", c), I("ref_year"), B.R("u_f", c)), fmt="f")
    for bk in M.BUCKETS:
        fd.scalar("u_pv_" + bk, "PV of %s capacity at blended coupon" % bk, "USD m", "=SUMPRODUCT(%s/%s,%s)" % (B.RR("B.cfads_all_" + bk), I("u_d_" + bk), B.RR("u_dfb")), pykey="sz.u_pv_cap_" + bk)
    fd.scalar("u_p99yrs", "Years in which the P99 test binds", "years", "=SUMPRODUCT(--(%s<%s),--(%s>0))" % (B.RR("u_cap99"), B.RR("u_capb"), B.RR("u_f")), fmt="int", pykey="sz.u_p99_binds_years")
    # Repricing
    fd.section("2025 holdco repricing (sized on post-refinancing base distributions)")
    fd.series("hn_f", "Interest period fraction", "fraction", lambda c: "=" + FR(c, I("ref_date"), I("hn_mat")), fmt="f")
    fd.series("hn_rate", "Rate (SOFR floored + margin)", "%", lambda c: "=MAX(%s,%s)+%s" % (B.R("in_sofr", c), I("hc_floor"), I("hn_m")), fmt="pct")
    fd.series("hn_amf", "Scheduled amortization per unit of face", "factor", lambda c: "=%s/100*%s" % (I("hn_am"), B.R("hn_f", c)), fmt="f")
    fd.series("hn_bf", "Scheduled balance per unit of face", "factor", lambda c: "=IF(%s=%s,1,%s%d-%s%d)" % (T("year", c), I("y0"), PREV[c], fd.r, PREV[c], fd.r - 1), fmt="f")
    fd.series("hn_k", "Debt service per unit of face", "factor", lambda c: "=%s*%s/100*%s+%s" % (B.R("hn_bf", c), B.R("hn_rate", c), B.R("hn_f", c), B.R("hn_amf", c)), fmt="f", pykey="sz.hn_k")
    fd.series("hn_test", "Coverage test year flag", "flag", lambda c: "=" + WIN(c, I("hn_t0"), I("hn_t1")), fmt="int")
    fd.series("dist_post", "Base distributions after USPP debt service", "USD m", lambda c: "=%s-%s" % (B.R("B.cfads_all", c), B.R("u_ds", c)), pykey="sz.dist_post_base")
    fd.series("hn_capv", "Face supported at 1.75x", "USD m", lambda c: "=IF(%s>0,%s/(%s*IF(%s>0,%s,1)),%s)" % (B.R("hn_test", c), B.R("dist_post", c), I("hc_cov"), B.R("hn_k", c), B.R("hn_k", c), I("big")), pykey="sz.hn_cap_vec")
    fd.scalar("hn_face", "Repriced holdco face", "USD m", "=MIN(%s)" % B.RR("hn_capv"), pykey="sz.hn_face")
    # Debt by asset
    fd.section("Opco debt by asset (pro rata to PV of each asset's own debt-service capacity)")
    for fac, ids, dpref, dfk, fk, tot in (("tl", M.A1, "tl_d_", "tl_df", "tl_f", "tl_debt"), ("u", M.AIDS, "u_d_", "u_dfb", "u_f", "u_size")):
        for aid in ids:
            fd.series("%s_acap_%s" % (fac, aid), "%s capacity, %s" % (aid, fac), "USD m", lambda c, aid=aid, dpref=dpref: "=" + "+".join(
                "%s*%s/%s" % (B.R("B.%s.mesa_cf" % aid, c), B.R("B.%s.s_%s" % (aid, bk), c), I(dpref + bk)) for bk in M.BUCKETS))
            fd.scalar("%s_apv_%s" % (fac, aid), "PV of capacity, %s" % aid, "USD m", "=SUMPRODUCT(%s,%s,--(%s>0))" % (B.RR("%s_acap_%s" % (fac, aid)), B.RR(dfk), B.RR(fk)))
        tot_pv = "+".join(B.C("%s_apv_%s" % (fac, a)) for a in ids)
        for aid in ids:
            fd.scalar("%s_debt_%s" % (fac, aid), "Allocated debt, %s" % aid, "USD m", "=%s*%s/(%s)" % (B.C(tot), B.C("%s_apv_%s" % (fac, aid)), tot_pv),
                      pykey="dba.%s.%s" % ({"tl": "opco_tl_2022", "u": "uspp_2025"}[fac], aid))
    # Sources and uses
    fd.section("Sources and uses")
    fd.scalar("su1_fee", "A1 opco upfront fee", "USD m", "=%s/100*%s" % (I("tl_fee"), B.C("tl_debt")), pykey="su.A1.opco_fee")
    fd.scalar("su1_oid", "A1 holdco OID", "USD m", "=(1-%s/100)*%s" % (I("hc_oid"), B.C("hc_face")), pykey="su.A1.holdco_oid")
    fd.scalar("su1_uses", "A1 uses (price, costs, fee, OID)", "USD m", "=%s+%s+%s+%s" % (I("a1_price"), I("a1_costs"), B.C("su1_fee"), B.C("su1_oid")), pykey="su.A1.uses")
    fd.scalar("su1_eq", "A1 fund equity", "USD m", "=%s-%s-%s" % (B.C("su1_uses"), B.C("tl_debt"), B.C("hc_face")), pykey="su.A1.equity")
    fd.scalar("su2_fee", "A2 Redfern upfront fee", "USD m", "=%s/100*%s" % (I("rf_fee"), B.C("rf_debt")), pykey="su.A2.fee")
    fd.scalar("su2_uses", "A2 uses", "USD m", "=%s+%s+%s" % (I("a2_price"), I("a2_costs"), B.C("su2_fee")), pykey="su.A2.uses")
    fd.scalar("su2_eq", "A2 fund equity", "USD m", "=%s-%s" % (B.C("su2_uses"), B.C("rf_debt")), pykey="su.A2.equity")
    fd.scalar("su3_dep", "R8 deposit at signing", "USD m", "=%s/100*%s" % (I("a3_dep"), I("a3_r8")), pykey="su.A3.r8_deposit")
    fd.scalar("su3_oid", "Holdco incremental OID", "USD m", "=(1-%s/100)*%s" % (I("hi_oid"), B.C("hi_face")), pykey="su.A3.oid")
    fd.scalar("su3_itc7", "R7 ITC transfer proceeds", "USD m", "=%s*%s" % (B.C("itc7_amt"), I("itcpx")), pykey="su.A3.itc7_proceeds")
    fd.scalar("su3_itc8", "R8 ITC transfer proceeds", "USD m", "=%s*%s" % (B.C("itc8_amt"), I("itcpx")), pykey="su.A3.itc8_proceeds")
    fd.scalar("su3_u1", "A3 uses at signing (deposit, costs, OID)", "USD m", "=%s+%s+%s" % (B.C("su3_dep"), I("a3_costs"), B.C("su3_oid")))
    fd.scalar("su3_eq1", "A3 equity at signing", "USD m", "=MAX(0,%s-%s)" % (B.C("su3_u1"), B.C("hi_face")), pykey="su.A3.eq_signing")
    fd.scalar("su3_c1", "Cash carried to R7 COD", "USD m", "=MAX(0,%s-%s)" % (B.C("hi_face"), B.C("su3_u1")), pykey="su.A3.carry")
    fd.scalar("su3_n2", "Funding need at R7 COD", "USD m", "=%s-%s-%s" % (I("a3_r7"), B.C("su3_c1"), B.C("su3_itc7")))
    fd.scalar("su3_eq2", "A3 equity at R7 COD", "USD m", "=MAX(0,%s)" % B.C("su3_n2"), pykey="su.A3.eq_r7")
    fd.scalar("su3_c2", "Cash carried to R8 COD", "USD m", "=MAX(0,-%s)" % B.C("su3_n2"), pykey="su.A3.carry2")
    fd.scalar("su3_n3", "Funding need at R8 COD", "USD m", "=%s-%s-%s-%s" % (I("a3_r8"), B.C("su3_dep"), B.C("su3_c2"), B.C("su3_itc8")))
    fd.scalar("su3_eq3", "A3 equity at R8 COD", "USD m", "=MAX(0,%s)" % B.C("su3_n3"), pykey="su.A3.eq_r8")
    fd.scalar("su3_c3", "Cash left after R8 COD (returned)", "USD m", "=MAX(0,-%s)" % B.C("su3_n3"), pykey="su.A3.cash_left_after_r8")
    fd.scalar("su3_uses", "A3 uses (prices, costs, OID)", "USD m", "=%s+%s+%s+%s" % (I("a3_r7"), I("a3_r8"), I("a3_costs"), B.C("su3_oid")), pykey="su.A3.uses")
    fd.scalar("su3_eq", "A3 fund equity, net", "USD m", "=%s+%s+%s-%s" % (B.C("su3_eq1"), B.C("su3_eq2"), B.C("su3_eq3"), B.C("su3_c3")), pykey="su.A3.equity")
    # Refinancing uses
    fd.section("2025 refinancing: uses and proceeds at December 31, 2025")
    fd.series("sw_df", "Discount factor at the SOFR swap rate", "factor", lambda c: "=(1+%s/100)^(-(%s-%s))" % (I("swr"), T("year", c), I("ref_year")), fmt="f")
    fd.series("sw_tl", "Opco swap: remaining hedged period fraction", "fraction", lambda c: "=" + FR(c, I("ref_date"), I("tl_hto")), fmt="f")
    fd.series("sw_rf", "Redfern swap: remaining period fraction", "fraction", lambda c: "=" + FR(c, I("ref_date"), I("rf_mat")), fmt="f")
    fd.scalar("mtm_tl", "Opco swap unwind (receivable to opco)", "USD m", "=SUMPRODUCT(%s/100*%s*(%s-%s)/100*%s,%s)" % (I("tl_hr"), B.RR("tl_sopen"), I("swr"), I("tl_hf"), B.RR("sw_tl"), B.RR("sw_df")), pykey="refi.mtm_opco_receivable")
    fd.scalar("mtm_rf", "Redfern swap unwind (payable by Redfern)", "USD m", "=SUMPRODUCT(%s/100*%s*(%s-%s)/100*%s,%s)" % (I("rf_hr"), B.RR("rf_sopen"), I("rf_hf"), I("swr"), B.RR("sw_rf"), B.RR("sw_df")), pykey="refi.mtm_redfern_payable")
    fd.scalar("refi_cost", "USPP transaction costs", "USD m", "=%s/100*%s" % (I("u_cost"), B.C("u_size")), pykey="refi.costs")
    fd.scalar("refi_tl", "Opco term loan repaid", "USD m", "=SUMIF(Time!$%s$4:$%s$4,%s,%s)" % (FC, LC, I("ref_year"), B.RR("tl_sclose")), pykey="refi.tl_repay")
    fd.scalar("refi_rf", "Redfern loan repaid", "USD m", "=SUMIF(Time!$%s$4:$%s$4,%s,%s)" % (FC, LC, I("ref_year"), B.RR("rf_sclose")), pykey="refi.rf_repay")
    fd.scalar("refi_net", "Net opco proceeds distributed to holdco", "USD m", "=%s-%s-%s-%s+%s-%s" % (B.C("u_size"), B.C("refi_cost"), B.C("refi_tl"), B.C("refi_rf"), B.C("mtm_tl"), B.C("mtm_rf")), pykey="refi.opco_net")

    # ---------------------------------------------------------------- Debt (live schedules)
    db = B.sheet("Debt", "Debt: live schedules (sized amounts held fixed)")
    db.header_time()
    db.section("Flags")
    db.series("post", "Post-refinancing flag", "flag", lambda c: "=(%s=1)*(%s>%s)" % (I("refi"), T("year", c), I("ref_year")), fmt="int")
    db.series("refy", "Refinancing year flag", "flag", lambda c: "=(%s=1)*(%s=%s)" % (I("refi"), T("year", c), I("ref_year")), fmt="int")
    db.series("sofr", "SOFR including sensitivity", "%", lambda c: "=%s+%s" % (B.R("in_sofr", c), I("s_sofr")), fmt="pct")
    db.section("Opco term loan")
    db.series("tl_rate", "All-in rate (unhedged share at live SOFR)", "%", lambda c: "=%s*%s+(1-%s)*%s+%s" % (B.R("tl_h", c), I("tl_hf"), B.R("tl_h", c), B.R("sofr", c), B.R("tl_margin", c)), fmt="pct")
    r0 = db.r
    db.series("tl_open", "Opening balance", "USD m", lambda c: "=IF(%s=YEAR(%s),%s,%s%d)" % (T("year", c), I("tl_date"), B.C("tl_debt"), PREV[c], r0 + 5), pykey="finance.tl_open")
    db.series("tl_int", "Interest", "USD m", lambda c: "=%s*%s/100*%s" % (B.R("tl_open", c), B.R("tl_rate", c), B.R("tl_f", c)), total="SUM", pykey="finance.tl_int")
    db.series("tl_prin", "Scheduled principal", "USD m", lambda c: "=MIN(%s,%s)*(1-%s)" % (B.R("tl_open", c), B.R("tl_sprin", c), B.R("post", c)), total="SUM", pykey="finance.tl_prin")
    db.series("tl_prep", "Prepayment from refinancing", "USD m", lambda c: "=%s*(%s-%s)" % (B.R("refy", c), B.R("tl_open", c), B.R("tl_prin", c)), total="SUM", pykey="finance.tl_prepay")
    db.series("tl_ds", "Debt service (interest and scheduled principal)", "USD m", lambda c: "=%s+%s" % (B.R("tl_int", c), B.R("tl_prin", c)), total="SUM", pykey="finance.tl_ds")
    db.series("tl_close", "Closing balance", "USD m", lambda c: "=%s-%s-%s" % (B.R("tl_open", c), B.R("tl_prin", c), B.R("tl_prep", c)))
    db.section("Redfern term loan")
    db.series("rf_rate", "All-in rate", "%", lambda c: "=%s/100*%s+(1-%s/100)*%s+%s" % (I("rf_hr"), I("rf_hf"), I("rf_hr"), B.R("sofr", c), I("rf_m")), fmt="pct")
    r0 = db.r
    db.series("rf_open", "Opening balance", "USD m", lambda c: "=IF(%s=YEAR(%s),%s,%s%d)" % (T("year", c), I("rf_date"), B.C("rf_debt"), PREV[c], r0 + 5), pykey="finance.rf_open")
    db.series("rf_int", "Interest", "USD m", lambda c: "=%s*%s/100*%s" % (B.R("rf_open", c), B.R("rf_rate", c), B.R("rf_f", c)), total="SUM", pykey="finance.rf_int")
    db.series("rf_prin", "Scheduled principal", "USD m", lambda c: "=MIN(%s,%s)*(1-%s)" % (B.R("rf_open", c), B.R("rf_sprin", c), B.R("post", c)), total="SUM", pykey="finance.rf_prin")
    db.series("rf_prep", "Prepayment from refinancing", "USD m", lambda c: "=%s*(%s-%s)" % (B.R("refy", c), B.R("rf_open", c), B.R("rf_prin", c)), pykey="finance.rf_prepay")
    db.series("rf_ds", "Debt service", "USD m", lambda c: "=%s+%s" % (B.R("rf_int", c), B.R("rf_prin", c)), total="SUM", pykey="finance.rf_ds")
    db.series("rf_close", "Closing balance", "USD m", lambda c: "=%s-%s-%s" % (B.R("rf_open", c), B.R("rf_prin", c), B.R("rf_prep", c)))
    db.section("USPP notes (fixed coupons; schedule as sized)")
    db.series("u_open", "Opening balance", "USD m", lambda c: "=%s*%s" % (B.R("u_open", c), I("refi")), pykey="finance.u_open")
    db.series("u_int", "Interest", "USD m", lambda c: "=%s*%s" % (B.R("u_int", c), I("refi")), total="SUM", pykey="finance.u_int")
    db.series("u_prin", "Principal", "USD m", lambda c: "=%s*%s" % (B.R("u_prin", c), I("refi")), total="SUM", pykey="finance.u_prin")
    db.series("u_ds", "Debt service", "USD m", lambda c: "=%s+%s" % (B.R("u_int", c), B.R("u_prin", c)), total="SUM", pykey="finance.u_ds")
    db.section("Holdco tranches (sweep from the Waterfall sheet)")
    tr = [("1", "hc_date", "hc_m", "hc_am", "hc_face", "Holdco TLB 2022"), ("2", "hi_date", "hi_m", "hi_am", "hi_face", "Holdco incremental 2024"),
          ("3", "ref_date", "hn_m", "hn_am", "hn_face", "Repriced holdco TLB 2025")]
    for n, dk, mk, ak, fk, nm in tr:
        db.series("h%s_f" % n, nm + ": interest period fraction", "fraction", lambda c, dk=dk: "=" + FR(c, I(dk), I("model_end")), fmt="f")
        db.series("h%s_rate" % n, nm + ": rate", "%", lambda c, mk=mk: "=MAX(%s,%s)+%s" % (B.R("sofr", c), I("hc_floor"), I(mk)), fmt="pct")
        db.scalar("h%s_F" % n, nm + ": face", "USD m", ("=%s*%s" % (B.C(fk), I("refi"))) if n == "3" else "=" + B.C(fk), style="link")
    for n, dk, mk, ak, fk, nm in tr:
        r0 = db.r
        if n == "3":
            opf = lambda c, r0=r0: "=IF(AND(%s=1,%s=%s+1),%s,%s%d)" % (I("refi"), T("year", c), I("ref_year"), B.C("h3_F"), PREV[c], r0 + 6)
        else:
            opf = lambda c, r0=r0, dk=dk, n=n: "=IF(%s=YEAR(%s),%s,%s%d)" % (T("year", c), I(dk), B.C("h%s_F" % n), PREV[c], r0 + 6)
        db.series("hc%s_open" % n, nm + ": opening balance", "USD m", opf, pykey="finance.hc%s_open" % n)
        db.series("hc%s_int" % n, nm + ": interest", "USD m", lambda c, n=n: "=%s*%s/100*%s" % (B.R("hc%s_open" % n, c), B.R("h%s_rate" % n, c), B.R("h%s_f" % n, c)), total="SUM", pykey="finance.hc%s_int" % n)
        db.series("hc%s_amort" % n, nm + ": scheduled amortization", "USD m", lambda c, n=n, ak=ak: "=MIN(%s,%s/100*%s*%s)" % (B.R("hc%s_open" % n, c), I(ak), B.C("h%s_F" % n), B.R("h%s_f" % n, c)), total="SUM", pykey="finance.hc%s_amort" % n)
        db.series("hc%s_sweep" % n, nm + ": excess cash sweep", "USD m", lambda c: "=0", pykey="finance.hc%s_sweep" % n)  # filled after Waterfall
        db.series("hc%s_rem" % n, nm + ": balance after amortization", "USD m", lambda c, n=n: "=%s-%s" % (B.R("hc%s_open" % n, c), B.R("hc%s_amort" % n, c)))
        if n in ("1", "2"):
            db.series("hc%s_repay" % n, nm + ": repaid at refinancing", "USD m", lambda c, n=n: "=%s*(%s-%s)" % (B.R("refy", c), B.R("hc%s_rem" % n, c), B.R("hc%s_sweep" % n, c)), pykey="finance.hc%s_repay" % n)
        else:
            db.series("hc%s_repay" % n, nm + ": repaid at refinancing", "USD m", lambda c: "=0")
        db.series("hc%s_close" % n, nm + ": closing balance", "USD m", lambda c, n=n: "=%s-%s-%s" % (B.R("hc%s_rem" % n, c), B.R("hc%s_sweep" % n, c), B.R("hc%s_repay" % n, c)))
        assert B.rows["hc%s_close" % n][1] == r0 + 6
    db.series("hc_ds", "Holdco debt service (interest and scheduled amortization)", "USD m", lambda c: "=" + "+".join("%s+%s" % (B.R("hc%s_int" % n, c), B.R("hc%s_amort" % n, c)) for n in "123"), total="SUM", pykey="finance.hc_ds")

    # ---------------------------------------------------------------- Tax (income tax)
    tx.section("Taxable income, NOL and cash tax (Mesa Corta modeled as a taxable blocker)")
    tx.series("int_ded", "Interest deducted (opco TL, Redfern, USPP, holdco)", "USD m", lambda c: "=%s+%s+%s+%s+%s+%s" % (B.R("tl_int", c), B.R("rf_int", c), B.R("u_int", c), B.R("hc1_int", c), B.R("hc2_int", c), B.R("hc3_int", c)))
    tx.series("ti", "Taxable income before NOL", "USD m", lambda c: "=%s-%s-%s" % (B.R("taxable_ops", c), B.R("dep", c), B.R("int_ded", c)), pykey="finance.taxable_income")
    r0 = tx.r
    tx.series("nol_o", "NOL opening", "USD m", lambda c: "=%s%d" % (PREV[c], r0 + 3), pykey="finance.nol_open")
    tx.series("nol_u", "NOL used (limited to 80% of taxable income)", "USD m", lambda c: "=MIN(%s,%s/100*MAX(%s,0))" % (B.R("nol_o", c), I("nol"), B.R("ti", c)), total="SUM", pykey="finance.nol_used")
    tx.series("tax", "Cash tax", "USD m", lambda c: "=%s/100*(MAX(%s,0)-%s)" % (I("tax"), B.R("ti", c), B.R("nol_u", c)), total="SUM", pykey="finance.tax")
    tx.series("nol_c", "NOL closing", "USD m", lambda c: "=%s-%s+MAX(-%s,0)" % (B.R("nol_o", c), B.R("nol_u", c), B.R("ti", c)), pykey="finance.nol_close")
    assert B.rows["nol_c"][1] == r0 + 3

    # ---------------------------------------------------------------- Waterfall
    wf = B.sheet("Waterfall", "Waterfall: opco to holdco to fund")
    wf.header_time()
    wf.section("Opco")
    wf.series("cfads", "CFADS (portfolio, Mesa share)", "USD m", lambda c: "=" + B.R("L.cfads_all", c), style="link", total="SUM")
    wf.series("opco_ds", "Opco debt service (term loan, Redfern, USPP)", "USD m", lambda c: "=%s+%s+%s" % (B.R("tl_ds", c), B.R("rf_ds", c), B.R("u_ds", c)), total="SUM", pykey="finance.opco_ds")
    wf.series("opco_dist", "Opco distributions to holdco", "USD m", lambda c: "=%s-%s" % (B.R("cfads", c), B.R("opco_ds", c)), total="SUM", pykey="finance.opco_dist")
    wf.series("recap_opco", "Refinancing proceeds distributed by opco", "USD m", lambda c: "=%s*%s" % (B.R("refy", c), B.C("refi_net")), total="SUM", pykey="finance.recap_opco")
    wf.section("Holdco")
    wf.series("w_tax", "Cash tax", "USD m", lambda c: "=" + B.R("tax", c), style="link")
    wf.series("w_hcds", "Holdco debt service", "USD m", lambda c: "=" + B.R("hc_ds", c), style="link")
    wf.series("excess", "Excess cash after tax and holdco debt service", "USD m", lambda c: "=%s-%s-%s" % (B.R("opco_dist", c), B.R("w_tax", c), B.R("w_hcds", c)), total="SUM", pykey="finance.hc_excess")
    wf.series("rem", "Holdco balances after scheduled amortization", "USD m", lambda c: "=%s+%s+%s" % (B.R("hc1_rem", c), B.R("hc2_rem", c), B.R("hc3_rem", c)))
    wf.series("sweep", "Excess cash sweep (50%, capped at balances)", "USD m", lambda c: "=MIN(%s/100*MAX(%s,0),%s)" % (I("hc_sw"), B.R("excess", c), B.R("rem", c)), total="SUM")
    wf.series("fund_ops", "Distribution to the fund from operations (floored at zero)", "USD m", lambda c: "=MAX(0,%s-%s)" % (B.R("excess", c), B.R("sweep", c)), total="SUM", pykey="finance.fund_dist_ops")
    wf.series("recap_hold", "Holdco repricing net proceeds (new face x OID less tranches repaid)", "USD m", lambda c: "=%s*(%s*%s/100-%s-%s)" % (B.R("refy", c), B.C("hn_face"), I("hn_oid"), B.R("hc1_repay", c), B.R("hc2_repay", c)), total="SUM", pykey="finance.recap_hold")
    wf.series("recap", "Recapitalization distribution", "USD m", lambda c: "=%s+%s" % (B.R("recap_opco", c), B.R("recap_hold", c)), total="SUM", pykey="finance.recap_total")
    wf.series("fund_dist", "Total distribution to the fund", "USD m", lambda c: "=%s+%s" % (B.R("fund_ops", c), B.R("recap", c)), total="SUM", pykey="finance.fund_dist")
    # fill sweep allocation rows on Debt
    for n in "123":
        rr = B.rows["hc%s_sweep" % n][1]
        for c in COLS:
            db.ws["%s%d" % (c, rr)] = "=IF(%s>0,%s*%s/%s,0)" % (B.R("rem", c), B.R("sweep", c), B.R("hc%s_rem" % n, c), B.R("rem", c))

    # ---------------------------------------------------------------- Ratios
    ra = B.sheet("Ratios", "Ratios")
    ra.header_time()
    ra.section("Cover ratios (shown where debt service exceeds the threshold)")
    for key, label, num, den, pk in (("dscr_tl", "Opco term loan DSCR (A1 group CFADS)", "L.cfads_a1", "tl_ds", "finance.dscr_tl"),
                                      ("dscr_rf", "Redfern DSCR (R6 Mesa cash flow)", "L.R6.mesa_cf", "rf_ds", "finance.dscr_rf"),
                                      ("dscr_u", "USPP DSCR (portfolio CFADS)", "L.cfads_all", "u_ds", "finance.dscr_u"),
                                      ("dscr_opco", "Opco aggregate DSCR", "L.cfads_all", "opco_ds", "finance.dscr_opco"),
                                      ("hc_cov", "Holdco coverage (opco distributions / holdco debt service)", "opco_dist", "hc_ds", "finance.hc_cov")):
        ra.series(key, label, "x", lambda c, num=num, den=den: '=IF(%s>%s,%s/%s,"")' % (B.R(den, c), I("thr"), B.R(num, c), B.R(den, c)), fmt="x", pykey=pk)
    ra.section("Summary")
    yr = "Time!$%s$4:$%s$4" % (FC, LC)
    for key, row, y0, y1, pk in (("tl", "dscr_tl", 2022, 2025, "tl_dscr_%s_2022_2025"), ("u", "dscr_u", 2026, 2043, "uspp_dscr_%s_2026_2043"),
                                 ("rf", "dscr_rf", 2024, 2029, "rf_dscr_%s"), ("hc", "hc_cov", 2023, 2031, "holdco_cov_%s_2023_2031")):
        ra.scalar("min_" + key, "Minimum %s, %d-%d" % (row, y0, y1), "x", '=IF(SUMPRODUCT(ISNUMBER(%s)*(%s>=%d)*(%s<=%d))=0,"",_xlfn.MINIFS(%s,%s,">="&%d,%s,"<="&%d))' % (B.RR(row), yr, y0, yr, y1, B.RR(row), yr, y0, yr, y1), fmt="x", pykey="sc." + pk % "min")
        ra.scalar("avg_" + key, "Average %s, %d-%d" % (row, y0, y1), "x", '=IFERROR(AVERAGEIFS(%s,%s,">="&%d,%s,"<="&%d),"")' % (B.RR(row), yr, y0, yr, y1), fmt="x", pykey="sc." + pk % "avg")

    # ---------------------------------------------------------------- Returns: valuations and fund returns
    rt = B.sheet("Returns", "Returns: bid valuations by risk bucket and fund returns")
    rt.header_time()
    rt.section("Unlevered discount factors (bucket rates to 2040, terminal rate after)")
    for vk, vd in (("v1", "a1_date"), ("v2", "a2_date"), ("v3", "a3_date")):
        rt.series(vk + "_tau", "Years from valuation date (%s)" % vd, "years", lambda c, vd=vd: "=MAX(0,(%s-%s)/%s)" % (T("ye", c), I(vd), I("dpy")), fmt="f")
        rt.series(vk + "_m", "Cash flow on or after valuation date", "flag", lambda c, vd=vd: "=--(%s>=%s)" % (T("ye", c), I(vd)), fmt="int")
        for bk in ("contracted", "hedged", "merchant", "storage_merchant"):
            rt.series("%s_df_%s" % (vk, bk), "DF %s (%s)" % (bk, vk), "factor", lambda c, vk=vk, bk=bk: "=IF(%s>%s,(1+%s/100)^(-%s),(1+%s/100)^(-%s))*%s" % (
                T("year", c), I("term_after"), I("u_terminal_post_2040"), B.R(vk + "_tau", c), I("u_" + bk), B.R(vk + "_tau", c), B.R(vk + "_m", c)), fmt="f")
        rt.series(vk + "_df_shield", "DF tax shield at contracted rate (%s)" % vk, "factor", lambda c, vk=vk: "=(1+%s/100)^(-%s)*%s" % (I("u_contracted"), B.R(vk + "_tau", c), B.R(vk + "_m", c)), fmt="f")

    def pv_asset(vk, aid, pyprefix):
        out = {}
        for bk in M.BUCKETS:
            dfk = "%s_df_%s" % (vk, "storage_merchant" if (bk == "merchant" and aid in M.STOR) else bk)
            out[bk] = rt.scalar("%s_%s_%s" % (vk, aid, bk), "%s value: %s" % (aid, bk), "USD m", "=SUMPRODUCT(%s,%s,%s)" % (B.RR("L.%s.posttax" % aid), B.RR("L.%s.s_%s" % (aid, bk)), B.RR(dfk)),
                                pykey="%s.%s" % (pyprefix, bk))
        rt.scalar("%s_%s_total" % (vk, aid), "%s value: total" % aid, "USD m", "=" + "+".join(B.C("%s_%s_%s" % (vk, aid, bk)) for bk in M.BUCKETS), pykey="%s.total" % pyprefix)

    rt.section("A1 valuation at March 22, 2022 (R-F04)")
    for aid in M.A1:
        pv_asset("v1", aid, "val.A1.by_asset.%s" % aid)
    rt.series("am_cf", "Platform cost after tax", "USD m", lambda c: "=-%s*(1-%s/100)" % (B.R("L.am", c), I("tax")))
    for bk in M.BUCKETS:
        rt.scalar("v1_pc_" + bk, "Platform costs value: " + bk, "USD m", "=SUMPRODUCT(%s,%s,%s)" % (B.RR("am_cf"), B.RR("L.sh_%s_a1" % bk), B.RR("v1_df_" + bk)), pykey="val.A1.by_asset.Platform costs.%s" % bk)
    rt.scalar("v1_pc_total", "Platform costs value: total", "USD m", "=" + "+".join(B.C("v1_pc_" + bk) for bk in M.BUCKETS), pykey="val.A1.by_asset.Platform costs.total")
    for bk in M.BUCKETS:
        rt.scalar("v1_b_" + bk, "A1 value by bucket: " + bk, "USD m", "=" + "+".join(B.C("v1_%s_%s" % (a, bk)) for a in M.A1) + "+" + B.C("v1_pc_" + bk), pykey="val.A1.by_bucket.%s" % bk)
    rt.scalar("v1_pre", "A1 value before purchase-price tax shield", "USD m", "=" + "+".join(B.C("v1_%s_total" % a) for a in M.A1) + "+" + B.C("v1_pc_total"), pykey="val.A1.pre_shield")
    rt.scalar("v1_pvdep", "PV of A1 tax depreciation per USD of price", "factor", "=SUMPRODUCT(%s,%s)/%s" % (B.RR("dep_A1"), B.RR("v1_df_shield"), I("a1_price")), fmt="f", pykey="val.A1.pv_dep_per_usd")
    rt.scalar("v1_shield", "Tax shield at the price paid", "USD m", "=%s/100*%s*%s" % (I("tax"), B.C("v1_pvdep"), I("a1_price")), pykey="val.A1.shield_at_price")
    rt.scalar("v1_ev", "A1 enterprise value", "USD m", "=%s+%s" % (B.C("v1_pre"), B.C("v1_shield")), pykey="val.A1.ev")
    rt.scalar("v1_npv", "Value less price", "USD m", "=%s-%s" % (B.C("v1_ev"), I("a1_price")), pykey="val.A1.npv_vs_price")
    rt.scalar("v1_be", "Breakeven price (closed form)", "USD m", "=%s/(1-%s/100*%s)" % (B.C("v1_pre"), I("tax"), B.C("v1_pvdep")), pykey="val.A1.breakeven_price")
    rt.section("A2 valuation at August 31, 2023 (R-F07)")
    pv_asset("v2", "R6", "val.A2.R6")
    rt.scalar("v2_pvdep", "PV of A2 tax depreciation per USD of price", "factor", "=SUMPRODUCT(%s,%s)/%s" % (B.RR("dep_A2"), B.RR("v2_df_shield"), I("a2_price")), fmt="f")
    rt.scalar("v2_shield", "Tax shield at the price paid", "USD m", "=%s/100*%s*%s" % (I("tax"), B.C("v2_pvdep"), I("a2_price")), pykey="val.A2.shield_at_price")
    rt.scalar("v2_ev", "A2 value", "USD m", "=%s+%s" % (B.C("v2_R6_total"), B.C("v2_shield")), pykey="val.A2.ev")
    rt.scalar("v2_npv", "Value less price", "USD m", "=%s-%s" % (B.C("v2_ev"), I("a2_price")), pykey="val.A2.npv_vs_price")
    rt.scalar("v2_be", "Breakeven price", "USD m", "=%s/(1-%s/100*%s)" % (B.C("v2_R6_total"), I("tax"), B.C("v2_pvdep")), pykey="val.A2.breakeven_price")
    rt.section("A3 valuation at February 15, 2024 (R-F07)")
    pv_asset("v3", "R7", "val.A3.R7")
    pv_asset("v3", "R8", "val.A3.R8")
    rt.scalar("v3_t7", "Years from signing to R7 COD", "years", "=(%s-%s)/%s" % (I("R7_cod"), I("a3_date"), I("dpy")), fmt="f")
    rt.scalar("v3_t8", "Years from signing to R8 COD", "years", "=(%s-%s)/%s" % (I("R8_cod"), I("a3_date"), I("dpy")), fmt="f")
    rt.scalar("v3_itc", "PV of ITC transfer proceeds", "USD m", "=%s*(1+%s/100)^(-%s)+%s*(1+%s/100)^(-%s)" % (B.C("su3_itc7"), I("u_contracted"), B.C("v3_t7"), B.C("su3_itc8"), I("u_contracted"), B.C("v3_t8")), pykey="val.A3.itc_pv")
    rt.scalar("v3_shield", "Tax shield on R7 and R8 basis", "USD m", "=%s/100*SUMPRODUCT(%s+%s,%s)" % (I("tax"), B.RR("dep_R7"), B.RR("dep_R8"), B.RR("v3_df_shield")), pykey="val.A3.shield")
    rt.scalar("v3_ev", "A3 value", "USD m", "=%s+%s+%s+%s" % (B.C("v3_R7_total"), B.C("v3_R8_total"), B.C("v3_itc"), B.C("v3_shield")), pykey="val.A3.ev")
    rt.scalar("v3_ppv", "PV of A3 price payments", "USD m", "=%s+%s*(1+%s/100)^(-%s)+(%s-%s)*(1+%s/100)^(-%s)" % (B.C("su3_dep"), I("a3_r7"), I("u_contracted"), B.C("v3_t7"), I("a3_r8"), B.C("su3_dep"), I("u_contracted"), B.C("v3_t8")), pykey="val.A3.price_pv")
    rt.scalar("v3_npv", "Value less PV of price", "USD m", "=%s-%s" % (B.C("v3_ev"), B.C("v3_ppv")), pykey="val.A3.npv_vs_price")

    rt.section("Fund cash flows (gross of fund fees and carry)")
    rt.series("nav_tau", "Years from NAV date", "years", lambda c: "=MAX(0,(%s-%s)/%s)" % (T("ye", c), I("nav_date"), I("dpy")), fmt="f")
    rt.series("nav_df", "NAV discount factor (levered rates by portfolio bucket, after NAV date)", "factor", lambda c: "=(%s>%s)*(%s)" % (
        T("ye", c), I("nav_date"), "+".join("%s*(1+%s/100)^(-%s)" % (B.R("L.sh_%s_all" % bk, c), I("l_" + bk), B.R("nav_tau", c)) for bk in M.BUCKETS)), fmt="f", pykey="finance.nav_df")
    rt.scalar("nav_unf", "NAV before floor", "USD m", "=SUMPRODUCT(%s,%s)" % (B.RR("fund_dist"), B.RR("nav_df")))
    rt.scalar("nav", "NAV at December 31, 2025 (floored at zero)", "USD m", "=MAX(0,%s)" % B.C("nav_unf"), pykey="sc.fund_nav_2025")
    rt.scalar("contrib", "Fund equity contributed", "USD m", "=%s+%s+%s" % (B.C("su1_eq"), B.C("su2_eq"), B.C("su3_eq")), pykey="sc.fund_contributions")
    rt.scalar("dist_life", "Fund distributions, life", "USD m", "=SUM(%s)" % B.RR("fund_dist"), pykey="sc.fund_distributions_life")
    rt.scalar("dist25", "Fund distributions to 2025", "USD m", "=SUMIF(%s,\"<=\"&%s,%s)" % (yr, I("ref_year"), B.RR("fund_dist")), pykey="sc.fund_distributions_to_2025")
    rt.scalar("moic", "Lifetime multiple", "x", "=%s/%s" % (B.C("dist_life"), B.C("contrib")), fmt="x", pykey="sc.fund_moic_life_x")
    rt.scalar("moic25", "Multiple to 2025 including NAV", "x", "=(%s+%s)/%s" % (B.C("dist25"), B.C("nav"), B.C("contrib")), fmt="x", pykey="sc.fund_moic_2025_x")
    # vertical flow table
    ws = rt.ws
    r0 = rt.r + 1
    ws.cell(row=r0, column=4, value="Dated fund cash flows (life)").font = BOLD
    ws.cell(row=r0, column=5, value="Date")
    ws.cell(row=r0, column=6, value="USD m")
    ws.cell(row=r0, column=7, value="To 2025 incl. NAV")
    eq_rows = [("A1 equity", I("a1_date"), "=-" + B.C("su1_eq")), ("A2 equity", I("a2_date"), "=-" + B.C("su2_eq")),
               ("A3 equity at signing", I("a3_date"), "=-" + B.C("su3_eq1")), ("A3 equity at R7 COD", I("R7_cod"), "=-" + B.C("su3_eq2")),
               ("A3 equity at R8 COD (net of cash returned)", I("R8_cod"), "=-%s+%s" % (B.C("su3_eq3"), B.C("su3_c3")))]
    rr = r0 + 1
    for lab, dref, val in eq_rows:
        ws.cell(row=rr, column=4, value=lab)
        ws.cell(row=rr, column=5, value="=" + dref).number_format = FMT["date"]
        ws.cell(row=rr, column=6, value=val).number_format = FMT["m"]
        ws.cell(row=rr, column=7, value="=F%d" % rr).number_format = FMT["m"]
        rr += 1
    for i in range(NT):
        ws.cell(row=rr, column=3, value=i + 1)
        ws.cell(row=rr, column=4, value="Distribution, year %d" % (2022 + i))
        ws.cell(row=rr, column=5, value="=INDEX(Time!$%s$6:$%s$6,C%d)" % (FC, LC, rr)).number_format = FMT["date"]
        ws.cell(row=rr, column=6, value="=INDEX(%s,C%d)" % (B.RR("fund_dist"), rr)).number_format = FMT["m"]
        ws.cell(row=rr, column=7, value="=IF(YEAR(E%d)<%s,F%d,IF(YEAR(E%d)=%s,F%d+%s,0))" % (rr, I("ref_year"), rr, rr, I("ref_year"), rr, B.C("nav"))).number_format = FMT["m"]
        rr += 1
    first, last = r0 + 1, rr - 1
    rt.r = rr + 1
    rt.scalar("irr_life", "Fund gross IRR, life", "%", "=100*XIRR(F%d:F%d,E%d:E%d)" % (first, last, first, last), fmt="pct", pykey="sc.fund_irr_life_pct")
    rt.scalar("irr25", "Fund gross IRR to December 31, 2025 including NAV", "%", "=100*XIRR(G%d:G%d,E%d:E%d)" % (first, last, first, last), fmt="pct", pykey="sc.fund_irr_2025_pct")

    # ---------------------------------------------------------------- Checks
    ck = B.sheet("Checks", "Checks (0 = pass)")
    ck.header_time()
    checks = [
        ("Opco TL sculpted balance repaid by 2040", "=ROUND(INDEX(%s,%d),6)" % (B.RR("tl_sclose"), NT)),
        ("Redfern sculpted balance repaid by 2030", "=ROUND(INDEX(%s,%d),6)" % (B.RR("rf_sclose"), NT)),
        ("USPP principal equals notes issued", "=ROUND(%s-SUM(%s),6)" % (B.C("u_size"), B.RR("u_prin"))),
        ("USPP interest plus principal equals sculpted debt service", "=ROUND(SUMPRODUCT(ABS(%s+%s-%s)),6)" % (B.RR("u_int"), B.RR("u_prin"), B.RR("u_ds"))),
        ("A1 sources equal uses", "=ROUND(%s+%s+%s-%s,6)" % (B.C("tl_debt"), B.C("hc_face"), B.C("su1_eq"), B.C("su1_uses"))),
        ("A3 sources equal uses", "=ROUND(%s+%s+%s+%s-%s,6)" % (B.C("hi_face"), B.C("su3_itc7"), B.C("su3_itc8"), B.C("su3_eq"), B.C("su3_uses"))),
        ("NOL never negative", "=ROUND(MIN(0,MIN(%s)),6)" % B.RR("nol_c")),
        ("Debt balances never negative", "=ROUND(MIN(0,MIN(%s),MIN(%s),MIN(%s),MIN(%s),MIN(%s)),6)" % (B.RR("tl_open"), B.RR("rf_open"), B.RR("hc1_open"), B.RR("hc2_open"), B.RR("hc3_open"))),
        ("Opco TL repaid when refinanced", "=ROUND(%s*INDEX(%s,%d),6)" % (I("refi"), B.RR("tl_close"), NT)),
    ]
    for aid in M.AIDS:
        checks.append(("%s revenue buckets sum to revenue" % aid, "=ROUND(SUMPRODUCT(ABS(%s+%s+%s-%s)),6)" % (B.RR("L.%s.rev_contracted" % aid), B.RR("L.%s.rev_hedged" % aid), B.RR("L.%s.rev_merchant" % aid), B.RR("L.%s.revenue" % aid))))
    ck.r = 8
    ck_rows = []
    for lab, f in checks:
        r = ck.scalar("chk%d" % len(ck_rows), lab, "USD m", f, fmt="f")
        ck_rows.append(r)
    ck.scalar("chk_total", "Total of absolute check values (0 = all pass)", "USD m", "=SUMPRODUCT(ABS(F%d:F%d))" % (ck_rows[0], ck_rows[-1]), fmt="f")
    ck.ws.conditional_formatting.add("F%d:F%d" % (ck_rows[0], ck_rows[-1] + 1), CellIsRule(operator="notEqual", formula=["0"], fill=REDFILL))

    # ---------------------------------------------------------------- Outputs
    ou = B.sheet("Outputs", "Outputs dashboard")
    ou.header_time()
    ou.section("Selected case")
    ou.scalar("o_scen", "Scenario (1 base, 2 low, 3 high)", "index", "=Scenario", style="link", fmt="int")
    ou.scalar("o_vol", "Volume case", "index", "=" + I("volcase"), style="link", fmt="int")
    ou.scalar("o_refi", "Refinancing switch", "flag", "=" + I("refi"), style="link", fmt="int")
    ou.section("Debt sized at each transaction (base, P50, P99 test)")
    for key, lab in (("tl_debt", "Opco term loan 2022"), ("hc_face", "Holdco TLB 2022"), ("rf_debt", "Redfern loan 2023"), ("hi_face", "Holdco incremental 2024"),
                     ("u_size", "USPP notes 2025"), ("u_sizeA", "Series A"), ("u_sizeB", "Series B"), ("u_sizeC", "Series C"), ("u_cpn", "Blended coupon (%)"), ("hn_face", "Repriced holdco TLB 2025"),
                     ("refi_net", "Net opco refinancing proceeds"), ("su1_eq", "A1 fund equity"), ("su2_eq", "A2 fund equity"), ("su3_eq", "A3 fund equity")):
        ou.scalar("o_" + key, lab, "USD m" if key != "u_cpn" else "%", "=" + B.C(key), style="link", fmt="m" if key != "u_cpn" else "pct")
    ou.section("Returns and valuation (selected case)")
    for key, lab, fm in (("irr_life", "Fund gross IRR, life (%)", "pct"), ("irr25", "Fund gross IRR to 2025 incl. NAV (%)", "pct"), ("nav", "NAV at December 31, 2025", "m"),
                         ("moic", "Lifetime multiple", "x"), ("v1_ev", "A1 enterprise value", "m"), ("v1_be", "A1 breakeven price", "m"), ("min_u", "Minimum USPP DSCR 2026-2043", "x"),
                         ("avg_u", "Average USPP DSCR 2026-2043", "x"), ("min_tl", "Minimum opco TL DSCR 2022-2025", "x"), ("chk_total", "Checks total (0 = pass)", "f")):
        ou.scalar("o_" + key, lab, "", "=" + B.C(key), style="link", fmt=fm)
    ou.section("Key series")
    for key, lab in (("L.cfads_all", "Portfolio CFADS"), ("opco_ds", "Opco debt service"), ("hc_ds", "Holdco debt service"), ("tax", "Cash tax"), ("fund_dist", "Fund distributions"),
                     ("dscr_u", "USPP DSCR"), ("hc_cov", "Holdco coverage")):
        ou.series("o_" + key, lab, "x" if key in ("dscr_u", "hc_cov") else "USD m", lambda c, key=key: "=" + B.R(key, c), style="link", fmt="x" if key in ("dscr_u", "hc_cov") else "m")

    # order sheets as per style sheet
    order = ["Cover", "Inputs", "Time", "Operations", "Tax", "Funding", "Debt", "Waterfall", "Ratios", "Returns", "Checks", "Outputs"]
    B.wb._sheets = [B.wb[n] for n in order]
    B.wb.calculation.fullCalcOnLoad = True
    out = out or os.path.join(HERE, "Case_R_Model.xlsx")
    B.wb.save(out)
    # scalar map for decommissioning/diversification etc. are Python-only report items
    json.dump(B.map, open(os.path.join(HERE, "case_r_excel_map.json"), "w"), indent=0)
    return out


if __name__ == "__main__":
    sc = "base"
    out = None
    args = sys.argv[1:]
    if "--scenario" in args:
        sc = args[args.index("--scenario") + 1]
    if "--out" in args:
        out = args[args.index("--out") + 1]
    print(build(sc, out))
