"""Case R reference model: Mesa Corta Renewables portfolio (ERCOT), owned by Lattimer.

Python mirror and computational source of truth for Case R (book/bible/case-bible.md Part 3).
Pure Python + numpy. Reads inputs_case_r.json, runs every scenario the Case Bible needs and
writes outputs_case_r.json (series + scalars) and case_r_report.md.

Periodicity: annual, calendar years 2022-2059 (38 periods). Every period is the year ending
December 31. Partial years use day-count fractions:
    frac(start, end)_t = max(0, min(end, YE_t) - max(start, YE_{t-1})) / (YE_t - YE_{t-1})
with dates held as Excel serial numbers so the workbook reproduces the same arithmetic.

All money in USD millions (nominal). Prices USD/MWh. Energy GWh.
Sign convention: costs and outflows stored positive and subtracted explicitly.

Model conventions that the Case Bible leaves open are listed in MODEL_CONVENTIONS (written to the
report). Circularities: none. Debt sculpting uses forward discount-factor products (no iteration);
the bid valuation's depreciation tax shield is linear in price and solved in closed form.
"""
import json, os, datetime as dt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
INP = json.load(open(os.path.join(HERE, "inputs_case_r.json")))

# --------------------------------------------------------------------------------------------
# Model-level conventions and supplementary assumptions (documented in the report).
# These are additions where the Case Bible is silent; the workbook carries the same values on
# its Inputs sheet.
# --------------------------------------------------------------------------------------------
SUPP = {
    "inflation_pct": 2.5,                 # opex escalation (Case Bible 3.8)
    "insurance_share_of_opex_pct": 15.0,  # share of opex the 22% 2023 step-up applies to (new)
    "ptc_after_2025_usd_per_mwh": 30.0,   # R3 PTC held flat at the 2025 value to Nov 2029 (new)
    "ptc_term_years": 10,
    "availability_factor_vs_p50_pct": 100.0,  # P50 is net of long-term availability
    "p50_reference_year": {"R1": 2022, "R2": 2022, "R3": 2022, "R4": 2022, "R5": 2022, "R8": 2025},
    "augmentation_escalation_from_2025_pct": 2.5,
    "holdco_test_years_2022": [2023, 2027],
    "holdco_test_years_2024": [2025, 2027],
    "holdco_test_years_2025": [2026, 2031],
    "holdco_amort_pct_pa_incremental": 1.0,
    "holdco_amort_pct_pa_repriced": 1.0,
    "uspp_first_year": 2026,
    "am_cost_end": "2059-12-31",
    "macrs_5": [0.20, 0.32, 0.192, 0.1152, 0.1152, 0.0576],
    "macrs_15": [0.05, 0.095, 0.0855, 0.077, 0.0693, 0.0623, 0.059, 0.059, 0.0591, 0.059,
                 0.0591, 0.059, 0.0591, 0.059, 0.0591, 0.0295],
    "itc_basis_reduction_share": 0.5,
    "large_number": 1.0e9,
    "ratio_threshold_usd_m": 0.001,
}

YEARS = np.arange(2022, 2060)
NT = len(YEARS)
EPOCH = dt.date(1899, 12, 30)


def ser(s):
    """ISO date string -> Excel serial number."""
    if isinstance(s, str):
        s = dt.date.fromisoformat(s)
    return (s - EPOCH).days


YE = np.array([ser(dt.date(int(y), 12, 31)) for y in YEARS], dtype=float)
YS = np.array([ser(dt.date(int(y) - 1, 12, 31)) for y in YEARS], dtype=float)
DAYS = YE - YS
EARLY = ser("2000-01-01")


def frac(start, end):
    s = ser(start) if isinstance(start, str) else start
    e = ser(end) if isinstance(end, str) else end
    return np.clip(np.minimum(e, YE) - np.maximum(s, YS), 0, None) / DAYS


def yidx(y):
    return int(y) - 2022


def yr_flag(a, b):
    return ((YEARS >= a) & (YEARS <= b)).astype(float)


ASSETS = {a["id"]: a for a in INP["assets"]}
AIDS = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]
GEN = ["R1", "R2", "R3", "R4", "R5", "R8"]
STOR = ["R6", "R7"]
A1 = ["R1", "R2", "R3", "R4", "R5"]
HUB_OF = {"R1": "West Hub", "R2": "South Hub", "R3": "West Hub", "R4": "West Hub",
          "R5": "West Hub", "R6": "North Hub", "R7": "Houston Hub", "R8": "South Hub"}
BASIS = {"west_wind": 0.04, "panhandle_wind": 0.07, "west_solar": 0.03, "south_solar": 0.02,
         "coastal_wind": 0.01}
OPEX_KEY = {"R1": "wind_pre_2018", "R2": "wind_pre_2018", "R3": "wind_post_2018", "R4": "solar",
            "R5": "solar", "R8": "solar", "R6": "storage", "R7": "storage"}
DECOM_KEY = {"R1": "wind", "R2": "wind", "R3": "wind", "R4": "solar", "R5": "solar",
             "R8": "solar", "R6": "storage", "R7": "storage"}
OWN_START = {"R1": "2022-03-22", "R2": "2022-03-22", "R3": "2022-03-22", "R4": "2022-03-22",
             "R5": "2022-03-22", "R6": "2023-08-31", "R7": "2024-04-02", "R8": "2024-12-19"}
BUCKETS = ["contracted", "hedged", "merchant"]

P = INP["prices"]
H = INP["hedges"]
D = INP["debt"]
TX = INP["tax"]
OX = INP["opex"]
VAL = INP["valuation"]


def series_from_dict(d):
    return np.array([float(d[str(y)]) for y in YEARS])


def sofr_series():
    s = D["sofr_3m_annual_avg_pct"]
    out = []
    for y in YEARS:
        out.append(float(s[str(y)]) if str(y) in s else float(s["2028_onward"]))
    return np.array(out)


SOFR = sofr_series()
ESC = (1 + SUPP["inflation_pct"] / 100) ** (YEARS - 2022)


def curtail_path(spec):
    if "all" in spec:
        return np.full(NT, spec["all"])
    a, b = spec["2022"], spec["2025_onward"]
    # linear interpolation 2022 -> 2025 (convention)
    return np.where(YEARS >= 2025, b, a + (b - a) * (YEARS - 2022) / 3.0)


# --------------------------------------------------------------------------------------------
# Case definition
# --------------------------------------------------------------------------------------------
def make_case(price="base", volume="p50", west_solar_capture_pts=0.0, battery="same",
              curtail_add_pts=0.0, opex_factor=1.0, sofr_add_unhedged_pct=0.0, refi=True):
    return dict(price=price, volume=volume, wsc=west_solar_capture_pts, battery=battery,
                curt_add=curtail_add_pts, opex_f=opex_factor, sofr_add=sofr_add_unhedged_pct,
                refi=refi)


PRICE_IDX = {"base": 1, "low": 2, "high": 3}
VOL_KEY = {"p50": None, "p90_1yr": "p90_1yr", "p90_10yr": "p90_10yr", "p99_1yr": "p99_1yr"}


def capture_hub(bucket, price):
    c = P["capture_ratio_to_own_hub_atc"][bucket]
    dec = c["decline_pts_pa"] / 100.0
    floor = c["floor"]
    if price == "low":
        dec *= 1.5
        floor -= 0.04
    elif price == "high":
        dec *= 0.5
    return np.maximum(floor, c["2022"] - dec * (YEARS - 2022))


# --------------------------------------------------------------------------------------------
# Yield statistics (editor-in-chief note, R-C09): normal distribution of annual net energy.
# One-year sigma^2 = sigma_LT^2 + sigma_IAV^2; N-year sigma^2 = sigma_LT^2 + sigma_IAV^2 / N.
# The Bible's P90 one-year and ten-year values (percent of P50) are the anchors; they imply
# sigma_1 and sigma_10, from which sigma_IAV^2 = (sigma_1^2 - sigma_10^2) * 10/9 and
# sigma_LT^2 = sigma_10^2 - sigma_IAV^2/10. P99 values are recomputed from these.
# --------------------------------------------------------------------------------------------
Z90, Z99 = 1.2816, 2.3263
CORR = {  # inter-asset correlations (ERCOT sites, illustrative), applied as stated below
    "iav_wind_west_west": 0.60,    # R1-R3 (West and Panhandle)
    "iav_wind_west_coastal": 0.30,  # R1/R3-R2
    "iav_solar_west_west": 0.85,   # R4-R5 (adjacent West sites)
    "iav_solar_west_south": 0.50,  # R4/R5-R8
    "iav_wind_solar": -0.10,       # any wind-solar pair
    "lt_same_technology": 0.50,    # long-term (model and measurement) uncertainty
    "lt_cross_technology": 0.00,
}


def yield_stats():
    out = {}
    for aid in GEN:
        a = ASSETS[aid]
        s1 = (1 - a["p90_1yr_pct_of_p50"] / 100.0) / Z90
        s10 = (1 - a["p90_10yr_pct_of_p50"] / 100.0) / Z90
        iav2 = (s1 ** 2 - s10 ** 2) * 10.0 / 9.0
        lt2 = s10 ** 2 - iav2 / 10.0
        out[aid] = dict(sigma_1yr=s1, sigma_10yr=s10, sigma_iav=iav2 ** 0.5, sigma_lt=lt2 ** 0.5,
                        p90_1yr=100 * (1 - Z90 * s1), p90_10yr=100 * (1 - Z90 * s10),
                        p99_1yr=100 * (1 - Z99 * s1), p99_10yr=100 * (1 - Z99 * s10))
    return out


def corr_pair(i, j, comp):
    if i == j:
        return 1.0
    wind = {"R1", "R2", "R3"}
    ti, tj = i in wind, j in wind
    if comp == "lt":
        return CORR["lt_same_technology"] if ti == tj else CORR["lt_cross_technology"]
    if ti != tj:
        return CORR["iav_wind_solar"]
    if ti:
        return CORR["iav_wind_west_coastal"] if "R2" in (i, j) else CORR["iav_wind_west_west"]
    return CORR["iav_solar_west_south"] if "R8" in (i, j) else CORR["iav_solar_west_west"]


YSTAT = yield_stats()


# --------------------------------------------------------------------------------------------
# Operations block: asset yield, hedge settlement, revenue buckets, opex, CF, tax shares
# --------------------------------------------------------------------------------------------
def operations(case):
    price = case["price"]
    north = series_from_dict(P["north_hub_atc_" + price])
    hub = {h: north * r for h, r in P["hub_ratio_to_north"].items()}
    hub["North Hub"] = north.copy()
    batt_key = price if case["battery"] == "same" else case["battery"]
    batt = np.array([float(P["battery_merchant_revenue_usd_per_kw_yr"][batt_key].get(str(y), 0.0))
                     for y in YEARS])
    ins_factor = 1 + SUPP["insurance_share_of_opex_pct"] / 100 * OX["insurance_step_up_2023_pct"] / 100 * (YEARS >= 2023)
    out = {"north_atc": north, "west_atc": hub["West Hub"], "south_atc": hub["South Hub"],
           "houston_atc": hub["Houston Hub"], "batt_rate": batt, "esc": ESC, "ins_factor": ins_factor}
    caps = {}
    for b in BASIS:
        cap = capture_hub(b, price)
        if b == "west_solar":
            cap = cap + case["wsc"] / 100.0  # sensitivity: West solar capture shift (points)
        caps[b] = cap
        out["cap_hub_" + b] = cap
    A = {}
    for aid in AIDS:
        a = ASSETS[aid]
        r = {}
        cod = a["cod"]
        life = a["useful_life_end"]
        r["op_frac"] = frac(cod, life)
        own_start = max(ser(OWN_START[aid]), ser(cod))
        r["own_frac"] = frac(own_start, life)
        r["own_share"] = np.where(r["op_frac"] > 0, r["own_frac"] / np.where(r["op_frac"] > 0, r["op_frac"], 1), 0.0)
        hubp = hub[HUB_OF[aid]]
        r["hub_atc"] = hubp
        mw = a["mw_ac"]
        if aid in GEN:
            bk = a["capture_bucket"]
            vf = 1.0 if VOL_KEY[case["volume"]] is None else YSTAT[aid][VOL_KEY[case["volume"]]] / 100.0
            r["vol_factor"] = np.full(NT, vf)
            ref = SUPP["p50_reference_year"][aid]
            r["deg"] = (1 - a["degradation_pct_pa"] / 100.0) ** np.maximum(0, YEARS - ref)
            r["curt"] = (curtail_path(P["curtailment_pct"][bk]) + case["curt_add"]) / 100.0
            r["gen_full"] = a["p50_gwh"] * vf * SUPP["availability_factor_vs_p50_pct"] / 100 * r["deg"] * (1 - r["curt"])
            r["gen"] = r["gen_full"] * r["op_frac"]
            r["cap_hub"] = caps[bk]
            r["cap_node"] = caps[bk] - BASIS[bk]
            r["node_price"] = hubp * r["cap_node"]
        else:
            z = np.zeros(NT)
            r.update(vol_factor=z, deg=z + 1, curt=z, gen_full=z, gen=z, cap_hub=z, cap_node=z, node_price=z)
        z = np.zeros(NT)
        con_frac, con_vol, settle, contracted, hedged, stor = z.copy(), z.copy(), z.copy(), z.copy(), z.copy(), z.copy()
        mkt_gen = r["gen"].copy()
        if aid == "R1":
            h = H["R1_fixed_volume_swap"]
            con_frac = frac(ser(h["start"]) - 1, h["end"])
            con_vol = h["volume_mw_atc"] * DAYS * 24 / 1000.0 * con_frac
            settle = con_vol * (h["price_usd_per_mwh"] - hubp) / 1000.0
            hedged = con_vol * h["price_usd_per_mwh"] / 1000.0
        elif aid == "R2":
            h = H["R2_physical_ppa"]
            con_frac = frac(cod, h["end"])
            con_vol = r["gen_full"] * con_frac
            mkt_gen = r["gen"] - con_vol
            settle = con_vol * h["price_usd_per_mwh"] / 1000.0
            contracted = settle.copy()
        elif aid == "R3":
            h = H["R3_proxy_revenue_swap"]
            con_frac = frac(ser(h["start"]) - 1, h["end"])
            con_vol = r["gen_full"] * con_frac  # proxy generation (model approximation)
            fixed = h["fixed_payment_usd_m_pa"] * con_frac
            settle = fixed - con_vol * r["cap_hub"] * hubp / 1000.0
            contracted = fixed
        elif aid == "R4":
            h = H["R4_fixed_shape_hedge"]
            con_frac = frac(ser(h["start"]) - 1, h["end"])
            con_vol = h["annual_volume_gwh"] * con_frac
            settle = con_vol * (h["price_usd_per_mwh"] - hubp * r["cap_hub"]) / 1000.0
            hedged = con_vol * h["price_usd_per_mwh"] / 1000.0
        elif aid == "R5":
            h = H["R5_virtual_ppa"]
            con_frac = frac(cod, h["end"])
            con_vol = r["gen_full"] * con_frac
            settle = con_vol * (h["strike_usd_per_mwh"] - hubp * r["cap_hub"]) / 1000.0
            contracted = con_vol * h["strike_usd_per_mwh"] / 1000.0
        elif aid == "R8":
            h = H["R8_fixed_shape_hedge"]
            con_frac = frac(ser(h["start"]) - 1, h["end"])
            con_vol = h["annual_volume_gwh"] * con_frac
            settle = con_vol * (h["price_usd_per_mwh"] - hubp * r["cap_hub"]) / 1000.0
            hedged = con_vol * h["price_usd_per_mwh"] / 1000.0
        elif aid == "R6":
            h = H["R6_toll"]
            con_frac = frac(h["start"], h["end"])
            avail = a["availability_pct"]
            short = max(0.0, h["availability_guarantee_pct"] - avail) / 100.0
            settle = h["toll_usd_per_kw_month"] * 12 * mw / 1000.0 * con_frac * (1 - short)
            contracted = settle.copy()
            stor = batt * mw / 1000.0 * avail / 100.0 * (r["op_frac"] - con_frac)
        elif aid == "R7":
            h = H["R7_revenue_floor"]
            con_frac = frac(h["start"], h["end"])
            avail = a["availability_pct"]
            m = batt * avail / 100.0
            under = np.maximum(m, h["floor_usd_per_kw_yr"]) - h["premium_usd_per_kw_yr"] - \
                h["upside_share_pct_above_140_usd_per_kw_yr"] / 100.0 * np.maximum(0, m - 140.0)
            settle = under * mw / 1000.0 * con_frac
            stor = m * mw / 1000.0 * (r["op_frac"] - con_frac)
            contracted = (h["floor_usd_per_kw_yr"] - h["premium_usd_per_kw_yr"]) * mw / 1000.0 * con_frac
        r["mkt_gen"] = mkt_gen
        r["mkt_rev"] = mkt_gen * r["node_price"] / 1000.0
        r["con_frac"], r["con_vol"], r["settle"], r["stor_rev"] = con_frac, con_vol, settle, stor
        r["revenue"] = r["mkt_rev"] + settle + stor
        r["rev_contracted"] = contracted
        r["rev_hedged"] = hedged
        r["rev_merchant"] = r["revenue"] - contracted - hedged
        # opex
        unit = OX[OPEX_KEY[aid]]
        r["opex"] = unit * mw / 1000.0 * ESC * ins_factor * r["op_frac"] * case["opex_f"]
        r["land"] = (OX["land_lease_wind_pct_of_revenue"] / 100.0 * r["revenue"]) if aid in ("R1", "R2", "R3") else z.copy()
        dk = OX["decommissioning_net_of_salvage_usd_per_kw_2022"][DECOM_KEY[aid]]
        r["bond"] = 0.006 * dk * mw / 1000.0 * ESC * r["op_frac"]
        mt = 0.0075 * 0.70
        r["margin_tax"] = mt * r["revenue"]
        r["ebitda"] = r["revenue"] - r["opex"] - r["land"] - r["bond"] - r["margin_tax"]
        aug = z.copy()
        if aid in STOR:
            ag = a["augmentation"]
            cy = int(cod[:4])
            for k in ag["years_after_cod"]:
                yy = cy + k
                if 2022 <= yy <= 2059:
                    aug[yidx(yy)] = ag["pct_of_mwh"] / 100.0 * a["mwh"] * ag["cost_usd_per_kwh_2025"] / 1000.0 * \
                        (1 + SUPP["augmentation_escalation_from_2025_pct"] / 100) ** (yy - 2025)
        r["aug"] = aug
        dec = z.copy()
        ly = int(life[:4])
        dec[yidx(ly)] = dk * mw / 1000.0 * ESC[yidx(ly)]
        r["decom"] = dec
        r["cf"] = r["ebitda"] - aug - dec
        # tax equity
        te = a.get("tax_equity")
        if te:
            pre = frac(EARLY, te["expected_flip"])
            r["te_cash"] = te["pre_flip_cash_to_te_pct"] / 100 * pre + te["post_flip_cash_and_tax_to_te_pct"] / 100 * (1 - pre)
            r["mesa_tax_share"] = (1 - te["pre_flip_tax_to_te_pct"] / 100) * pre + (1 - te["post_flip_cash_and_tax_to_te_pct"] / 100) * (1 - pre)
        else:
            r["te_cash"] = z.copy()
            r["mesa_tax_share"] = z + 1.0
        r["mesa_cf"] = r["cf"] * (1 - r["te_cash"]) * r["own_share"]
        r["te_cf"] = r["cf"] * r["te_cash"] * r["own_share"]
        r["mesa_taxable"] = r["cf"] * r["mesa_tax_share"] * r["own_share"]
        rv = r["revenue"]
        safe = np.where(rv != 0, rv, 1.0)
        r["s_contracted"] = np.where(rv != 0, contracted / safe, 0.0)
        r["s_hedged"] = np.where(rv != 0, hedged / safe, 0.0)
        r["s_merchant"] = 1 - r["s_contracted"] - r["s_hedged"]
        mult = r["own_share"] * (1 - r["te_cash"])
        for b in BUCKETS:
            r["mesa_rev_" + b] = r["rev_" + b] * mult
        r["mesa_rev"] = rv * mult
        if aid == "R3":
            ptc = np.array([TX["ptc_r3_usd_per_mwh"].get(str(y), SUPP["ptc_after_2025_usd_per_mwh"]) for y in YEARS], dtype=float)
            ptc_frac = frac(cod, dt.date(int(cod[:4]) + SUPP["ptc_term_years"], int(cod[5:7]), int(cod[8:10])).isoformat())
            r["ptc_total"] = r["gen_full"] * ptc_frac * ptc / 1000.0
        A[aid] = r
    out["assets"] = A
    am = INP["owner"]["asset_management_cost_usd_m_pa_2022"] * ESC * frac("2022-03-22", SUPP["am_cost_end"])
    out["am_cost"] = am
    for grp, ids in (("a1", A1), ("all", AIDS), ("a3", ["R7", "R8"])):
        out["mesa_cf_" + grp] = sum(A[i]["mesa_cf"] for i in ids)
        for b in BUCKETS:
            out["mesa_rev_%s_%s" % (b, grp)] = sum(A[i]["mesa_rev_" + b] for i in ids)
        out["mesa_rev_" + grp] = sum(A[i]["mesa_rev"] for i in ids)
    out["cfads_a1"] = out["mesa_cf_a1"] - am
    out["cfads_all"] = out["mesa_cf_all"] - am
    out["cfads_a3"] = out["mesa_cf_a3"]
    for grp in ("a1", "all", "a3"):
        tot = out["mesa_rev_" + grp]
        safe = np.where(tot != 0, tot, 1.0)
        for b in BUCKETS:
            sh = np.where(tot != 0, out["mesa_rev_%s_%s" % (b, grp)] / safe, 1.0 if b == "merchant" else 0.0)
            out["share_%s_%s" % (b, grp)] = sh
            out["cfads_%s_%s" % (grp, b)] = out["cfads_" + grp] * sh
    return out


# --------------------------------------------------------------------------------------------
# Debt sizing (always on base-case P50 and P99 operations)
# --------------------------------------------------------------------------------------------
def dscr_caps(ops, grp, dscr):
    return sum(ops["cfads_%s_%s" % (grp, b)] / dscr[b] for b in BUCKETS)


def disc_factors(rate_pct, f):
    """Forward product of 1/(1 + r*f): discount factor to the loan's start date."""
    return np.cumprod(1.0 / (1.0 + rate_pct / 100.0 * f))


def opco_tl_rates(sofr_add=0.0):
    t = D["opco_term_loan_2022"]
    pre26 = frac(EARLY, "2026-03-22")
    margin = t["margin_pct"]["after"] - (t["margin_pct"]["after"] - t["margin_pct"]["to_2026-03-22"]) * pre26
    h = t["hedge"]["ratio_pct"] / 100.0 * frac(EARLY, t["hedge"]["to"])
    return h * t["hedge"]["fixed_pct"] + (1 - h) * (SOFR + sofr_add) + margin, h, margin


def redfern_rates(sofr_add=0.0):
    t = D["redfern_loan_2023"]
    h = t["hedge"]["ratio_pct"] / 100.0
    return h * t["hedge"]["fixed_pct"] + (1 - h) * (SOFR + sofr_add) + t["margin_pct"]


def holdco_rate(margin, sofr_add=0.0):
    return np.maximum(SOFR + sofr_add, D["holdco_term_loan_2022"]["sofr_floor_pct"]) + margin


def levered_dfs(v0, grp_shares):
    lev = VAL["discount_rates_nominal_post_tax_pct"]["levered_equity"]
    tau = np.maximum(0, (YE - ser(v0)) / 365.0)
    mask = (YE >= ser(v0)).astype(float)
    w = 0
    for b in BUCKETS:
        w = w + grp_shares[b] * (1 + lev[b] / 100.0) ** (-tau)
    return w * mask


def holdco_k(rate, f, amort_pct):
    """Debt-service factor per unit face: interest on scheduled balance + scheduled amortization."""
    am = amort_pct / 100.0 * f
    bf = 1 - np.concatenate([[0.0], np.cumsum(am)[:-1]])
    return bf * rate / 100.0 * f + am, bf


def size_all(base, p99):
    S = {}
    # ---- Opco term loan 2022 (A1 group, sculpted to 2040-12-31) ----
    t = D["opco_term_loan_2022"]
    f = frac(t["date"], t["notional_amortization_to"])
    cap_b = dscr_caps(base, "a1", t["sizing_dscr_x_by_revenue_bucket"])
    cap_99 = p99["cfads_a1"] / t["p99_1yr_dscr_min_x"]
    ds = np.where(f > 0, np.maximum(0, np.minimum(cap_b, cap_99)), 0.0)
    r, h, m = opco_tl_rates()
    df = disc_factors(r, f)
    debt = float(np.sum(ds * df))
    S["tl_f"], S["tl_rate"], S["tl_hedge_share"], S["tl_margin"] = f, r, h, m
    S["tl_cap_bucket"], S["tl_cap_p99"], S["tl_ds"], S["tl_df"] = cap_b, cap_99, ds, df
    S["tl_p99_binds_years"] = int(np.sum((cap_99 < cap_b) & (f > 0)))
    for b in BUCKETS:
        S["tl_pv_cap_" + b] = float(np.sum(base["cfads_a1_" + b] / t["sizing_dscr_x_by_revenue_bucket"][b] * df * (f > 0)))
    S["tl_pv_cap_bucket_total"] = float(np.sum(cap_b * df * (f > 0)))
    S["tl_debt"] = debt
    op = np.zeros(NT); prin = np.zeros(NT); intr = np.zeros(NT)
    bal = debt
    for i in range(NT):
        op[i] = bal
        intr[i] = bal * r[i] / 100.0 * f[i]
        prin[i] = ds[i] - intr[i] if f[i] > 0 else 0.0
        bal = bal - prin[i]
    S["tl_sched_open"], S["tl_sched_prin"], S["tl_sched_int"] = op, prin, intr
    S["tl_sched_close_end"] = bal
    dist_a1 = base["cfads_a1"] - ds
    S["dist_a1_base"] = dist_a1
    # ---- Holdco TLB 2022 ----
    hc = D["holdco_term_loan_2022"]
    fh = frac(hc["date"], hc["maturity"])
    rh = holdco_rate(hc["margin_pct"])
    k, bf = holdco_k(rh, fh, hc["amortization_pct_pa"])
    test = yr_flag(*SUPP["holdco_test_years_2022"])
    cov_req = 1.75
    capv = np.where(test > 0, dist_a1 / (cov_req * np.where(k > 0, k, 1)), SUPP["large_number"])
    face_cov = float(np.min(capv))
    lev_sh = {b: base["share_%s_a1" % b] for b in BUCKETS}
    eq_df = levered_dfs(hc["date"], lev_sh)
    eq_val = float(np.sum(dist_a1 * eq_df))
    face_cap = 0.45 * eq_val
    S.update(hc_f=fh, hc_rate=rh, hc_k=k, hc_test=test, hc_cap_vec=capv, hc_face_cov=face_cov,
             opco_eq_val_2022=eq_val, hc_face_cap=face_cap, hc_face=min(face_cov, face_cap),
             hc_binding="coverage" if face_cov <= face_cap else "45% of opco equity value", hc_eq_df=eq_df)
    # ---- Redfern loan 2023 (toll cash flow only) ----
    rf = D["redfern_loan_2023"]
    fr = frac(rf["date"], rf["maturity"])
    r6 = base["assets"]["R6"]
    toll_rate = H["R6_toll"]["toll_usd_per_kw_month"] * 12 * ASSETS["R6"]["mw_ac"] / 1000.0
    opf = r6["op_frac"]
    costrate = np.where(opf > 0, (r6["opex"] + r6["bond"] + r6["margin_tax"]) / np.where(opf > 0, opf, 1), 0.0)
    cfr = (toll_rate - costrate) * fr - r6["aug"] * (fr > 0)
    dsr = np.where(fr > 0, cfr / 1.35, 0.0)
    rr = redfern_rates()
    dfr = disc_factors(rr, fr)
    red = float(np.sum(dsr * dfr))
    op = np.zeros(NT); prin = np.zeros(NT); bal = 0.0
    draw = int(rf["date"][:4])
    for i in range(NT):
        if YEARS[i] == draw:
            bal = red
        op[i] = bal
        prin[i] = dsr[i] - bal * rr[i] / 100.0 * fr[i] if fr[i] > 0 else 0.0
        bal -= prin[i]
    S.update(rf_f=fr, rf_cf=cfr, rf_ds=dsr, rf_rate=rr, rf_df=dfr, rf_debt=red, rf_sched_open=op,
             rf_sched_prin=prin, rf_close_end=bal)
    # ---- Holdco incremental 2024 ----
    hi = D["holdco_incremental_2024"]
    fi = frac(hi["date"], hi["maturity"])
    ri = holdco_rate(hi["margin_pct"])
    ki, _ = holdco_k(ri, fi, SUPP["holdco_amort_pct_pa_incremental"])
    testi = yr_flag(*SUPP["holdco_test_years_2024"])
    capi = np.where(testi > 0, base["cfads_a3"] / (cov_req * np.where(ki > 0, ki, 1)), SUPP["large_number"])
    S.update(hi_f=fi, hi_rate=ri, hi_k=ki, hi_test=testi, hi_cap_vec=capi, hi_face=float(np.min(capi)))
    # ---- 2025 refinancing: USPP notes ----
    # Aggregate debt service is sculpted to min(bucket DSCR capacity, P99 capacity). Principal is
    # applied sequentially by tenor: years 2026-2032 retire Series A, 2033-2037 Series B,
    # 2038-2043 Series C. Each series accrues its own coupon. Working backward from 2043:
    #   P_t = (DS_t - sum_s c_s * Open_s,t+1) / (1 + c_s(t)),  Open_s,t = Open_s,t+1 + P_t*[s = s(t)]
    # so the series sizes (and the issue-weighted blended coupon) are outputs of the sculpting.
    u = D["refinancing_2025"]["uspp_notes"]
    ser_ = u["series"]
    y0 = SUPP["uspp_first_year"]
    endA = y0 + ser_["A"]["tenor_years"] - 1
    endB = y0 + ser_["B"]["tenor_years"] - 1
    endC = y0 + ser_["C"]["tenor_years"] - 1
    flA, flB, flC = yr_flag(y0, endA), yr_flag(endA + 1, endB), yr_flag(endB + 1, endC)
    fu = flA + flB + flC
    cA, cB, cC = ser_["A"]["coupon_pct"] / 100, ser_["B"]["coupon_pct"] / 100, ser_["C"]["coupon_pct"] / 100
    c_t = flA * cA + flB * cB + flC * cC
    capu = dscr_caps(base, "all", u["sizing_dscr_x_by_revenue_bucket"])
    capu99 = p99["cfads_all"] / u["p99_1yr_dscr_min_x"]
    dsu = np.where(fu > 0, np.maximum(0, np.minimum(capu, capu99)), 0.0)
    oA = np.zeros(NT + 1); oB = np.zeros(NT + 1); oC = np.zeros(NT + 1); prin = np.zeros(NT)
    for i in range(NT - 1, -1, -1):
        if fu[i] > 0:
            prin[i] = (dsu[i] - cA * oA[i + 1] - cB * oB[i + 1] - cC * oC[i + 1]) / (1 + c_t[i])
        oA[i] = oA[i + 1] + prin[i] * flA[i]
        oB[i] = oB[i + 1] + prin[i] * flB[i]
        oC[i] = oC[i + 1] + prin[i] * flC[i]
    oA, oB, oC = oA[:NT], oB[:NT], oC[:NT]
    i0 = yidx(y0)
    sizes = {"A": float(oA[i0]), "B": float(oB[i0]), "C": float(oC[i0])}
    uspp = sum(sizes.values())
    op = (oA + oB + oC) * fu
    intr = (cA * oA + cB * oB + cC * oC) * fu
    cpn = 100 * (sizes["A"] * cA + sizes["B"] * cB + sizes["C"] * cC) / uspp
    S.update(u_f=fu, u_flA=flA, u_flB=flB, u_flC=flC, u_coupon_t=c_t, u_coupon=cpn, u_cap_bucket=capu,
             u_cap_p99=capu99, u_ds=dsu, u_size=uspp, u_open=op, u_openA=oA, u_openB=oB, u_openC=oC,
             u_prin=prin, u_int=intr, u_series_size=sizes,
             u_series_share={k: 100 * v / uspp for k, v in sizes.items()},
             u_p99_binds_years=int(np.sum((capu99 < capu) & (fu > 0))))
    # PV of bucket capacities at the blended coupon (for the sizing-by-bucket exhibit)
    dfu = (1 + cpn / 100) ** (-(YEARS - 2025).astype(float)) * fu
    S["u_df_blended"] = dfu
    for b in BUCKETS:
        S["u_pv_cap_" + b] = float(np.sum(base["cfads_all_" + b] / u["sizing_dscr_x_by_revenue_bucket"][b] * dfu))
    S["u_pv_ds_blended"] = float(np.sum(dsu * dfu))
    # ---- Holdco repricing: sized on post-refinancing distributions ----
    hr = D["refinancing_2025"]["holdco_repricing"]
    fn = frac("2025-12-31", hr["new_maturity"])
    rn = holdco_rate(hr["new_margin_pct"])
    kn, _ = holdco_k(rn, fn, SUPP["holdco_amort_pct_pa_repriced"])
    testn = yr_flag(*SUPP["holdco_test_years_2025"])
    dist_post = base["cfads_all"] - dsu
    capn = np.where(testn > 0, dist_post / (cov_req * np.where(kn > 0, kn, 1)), SUPP["large_number"])
    S.update(hn_f=fn, hn_rate=rn, hn_k=kn, hn_test=testn, hn_cap_vec=capn, hn_face=float(np.min(capn)),
             dist_post_base=dist_post)
    return S


# --------------------------------------------------------------------------------------------
# Live run: actual debt schedules, tax, holdco, fund cash flows
# --------------------------------------------------------------------------------------------
def tax_depreciation():
    """Mesa Corta's tax depreciation from purchase prices (bonus + MACRS)."""
    m5, m15 = SUPP["macrs_5"], SUPP["macrs_15"]
    bonus = TX["bonus_depreciation_pct_by_placed_in_service_or_acquired_year"]
    acq = INP["acquisitions"]
    itc7 = TX["itc_r7_pct"] / 100 * TX["itc_r7_eligible_basis_pct_of_price"] / 100 * acq["A3"]["kerrigan_price_usd_m"]
    itc8 = TX["itc_r8_pct"] / 100 * TX["itc_r8_eligible_basis_pct_of_price"] / 100 * acq["A3"]["barlow_price_usd_m"]
    red = SUPP["itc_basis_reduction_share"]
    lots = [("A1", acq["A1"]["enterprise_value_usd_m"], 2022, bonus["2022"]),
            ("A2", acq["A2"]["enterprise_value_usd_m"], 2023, bonus["2023"]),
            ("R7", acq["A3"]["kerrigan_price_usd_m"] - red * itc7, 2024, bonus["2024"]),
            ("R8", acq["A3"]["barlow_price_usd_m"] - red * itc8, 2024, bonus["2024"])]
    dep = np.zeros(NT); per = {}
    for name, basis, y0, bp in lots:
        d = np.zeros(NT)
        b5, b15 = basis * 0.85, basis * 0.10
        for i, y in enumerate(YEARS):
            n = y - y0
            if n < 0:
                continue
            v = 0.0
            if n == 0:
                v += (b5 + b15) * bp / 100.0
            if n < len(m5):
                v += b5 * (1 - bp / 100.0) * m5[n]
            if n < len(m15):
                v += b15 * (1 - bp / 100.0) * m15[n]
            d[i] = v
        per[name] = d
        dep += d
    return dep, per, itc7, itc8


def run(case, base=None, p99=None, S=None):
    if base is None:
        base = operations(make_case())
        p99 = operations(make_case(volume="p99_1yr"))
    if S is None:
        S = size_all(base, p99)
    L = operations(case)
    R = {"ops": L}
    refi = case["refi"]
    ref_i = yidx(2025)
    post = (YEARS > 2025).astype(float) if refi else np.zeros(NT)
    # ---- Opco term loan actual ----
    t = D["opco_term_loan_2022"]
    r_tl, _, _ = opco_tl_rates(case["sofr_add"])
    f = S["tl_f"]
    op = np.zeros(NT); intr = np.zeros(NT); prin = np.zeros(NT); prep = np.zeros(NT)
    bal = S["tl_debt"]
    for i in range(NT):
        op[i] = bal
        intr[i] = bal * r_tl[i] / 100.0 * f[i]
        prin[i] = min(bal, S["tl_sched_prin"][i]) * (1 - post[i])
        prep[i] = (bal - prin[i]) if (refi and i == ref_i) else 0.0
        bal = bal - prin[i] - prep[i]
    R.update(tl_open=op, tl_int=intr, tl_prin=prin, tl_prepay=prep, tl_ds=intr + prin)
    # ---- Redfern actual ----
    rr = redfern_rates(case["sofr_add"])
    fr = S["rf_f"]
    op = np.zeros(NT); intr = np.zeros(NT); prin = np.zeros(NT); prep = np.zeros(NT); bal = 0.0
    draw = int(D["redfern_loan_2023"]["date"][:4])
    for i in range(NT):
        if YEARS[i] == draw:
            bal = S["rf_debt"]
        op[i] = bal
        intr[i] = bal * rr[i] / 100.0 * fr[i]
        prin[i] = min(bal, S["rf_sched_prin"][i]) * (1 - post[i])
        prep[i] = (bal - prin[i]) if (refi and i == ref_i) else 0.0
        bal = bal - prin[i] - prep[i]
    R.update(rf_open=op, rf_int=intr, rf_prin=prin, rf_prepay=prep, rf_ds=intr + prin)
    # ---- USPP actual (fixed coupon; schedule as sized) ----
    if refi:
        R.update(u_open=S["u_open"].copy(), u_int=S["u_int"].copy(), u_prin=S["u_prin"].copy())
    else:
        z = np.zeros(NT)
        R.update(u_open=z.copy(), u_int=z.copy(), u_prin=z.copy())
    R["u_ds"] = R["u_int"] + R["u_prin"]
    u_issue = S["u_size"] if refi else 0.0
    # ---- Refinancing cash at 2025-12-31 ----
    u = D["refinancing_2025"]["uspp_notes"]
    swr = 3.55
    dfsw = (1 + swr / 100.0) ** (-(YEARS - 2025).astype(float))
    hfr = frac("2025-12-31", t["hedge"]["to"])
    mtm_opco = float(np.sum(t["hedge"]["ratio_pct"] / 100.0 * S["tl_sched_open"] * (swr - t["hedge"]["fixed_pct"]) / 100.0 * hfr * dfsw))
    rfh = D["redfern_loan_2023"]["hedge"]
    rfr = frac("2025-12-31", D["redfern_loan_2023"]["maturity"])
    mtm_red = float(np.sum(rfh["ratio_pct"] / 100.0 * S["rf_sched_open"] * (rfh["fixed_pct"] - swr) / 100.0 * rfr * dfsw))
    costs_u = u["transaction_costs_pct"] / 100.0 * S["u_size"]
    refi_cash = dict(uspp=S["u_size"], costs=costs_u, tl_repay=float(R["tl_prepay"][ref_i]) if refi else float(S["tl_sched_open"][ref_i] - S["tl_sched_prin"][ref_i]),
                     rf_repay=float(R["rf_prepay"][ref_i]) if refi else float(S["rf_sched_open"][ref_i] - S["rf_sched_prin"][ref_i]),
                     mtm_opco_receivable=mtm_opco, mtm_redfern_payable=mtm_red)
    refi_cash["opco_net"] = refi_cash["uspp"] - costs_u - refi_cash["tl_repay"] - refi_cash["rf_repay"] + mtm_opco - mtm_red
    R["refi_cash"] = refi_cash
    # ---- Opco distributions ----
    cfads = L["cfads_all"]
    opco_ds = R["tl_ds"] + R["rf_ds"] + R["u_ds"]
    opco_dist = cfads - opco_ds
    recap_opco = np.zeros(NT)
    if refi:
        recap_opco[ref_i] = refi_cash["opco_net"]
    R.update(cfads=cfads, opco_ds=opco_ds, opco_dist=opco_dist, recap_opco=recap_opco)
    # ---- Tax (Mesa Corta tax group, modeled as a taxable blocker) ----
    dep, dep_per, itc7, itc8 = tax_depreciation()
    taxable_ops = sum(L["assets"][a]["mesa_taxable"] for a in AIDS) - L["am_cost"]
    # ---- Holdco ----
    hc = D["holdco_term_loan_2022"]; hi = D["holdco_incremental_2024"]; hr = D["refinancing_2025"]["holdco_repricing"]
    r1 = holdco_rate(hc["margin_pct"], case["sofr_add"]); r2 = holdco_rate(hi["margin_pct"], case["sofr_add"])
    r3 = holdco_rate(hr["new_margin_pct"], case["sofr_add"])
    f1 = frac(hc["date"], "2059-12-31"); f2 = frac(hi["date"], "2059-12-31"); f3 = frac("2025-12-31", "2059-12-31")
    F1, F2, F3 = S["hc_face"], S["hi_face"], (S["hn_face"] if refi else 0.0)
    b1 = np.zeros(NT); b2 = np.zeros(NT); b3 = np.zeros(NT)
    i1 = np.zeros(NT); i2 = np.zeros(NT); i3 = np.zeros(NT)
    a1 = np.zeros(NT); a2 = np.zeros(NT); a3 = np.zeros(NT)
    s1 = np.zeros(NT); s2 = np.zeros(NT); s3 = np.zeros(NT)
    rep1 = np.zeros(NT); rep2 = np.zeros(NT)
    nol_o = np.zeros(NT); nol_u = np.zeros(NT); nol_c = np.zeros(NT); ti = np.zeros(NT); tax = np.zeros(NT)
    excess = np.zeros(NT); fund_dist = np.zeros(NT); hc_ds = np.zeros(NT); recap_hold = np.zeros(NT)
    tl_int = R["tl_int"]; rf_int = R["rf_int"]; u_int = R["u_int"]
    c1 = 0.0; c2 = 0.0; c3 = 0.0; nol = 0.0
    sw = hc["excess_cash_sweep_pct"] / 100.0
    for i, y in enumerate(YEARS):
        o1 = F1 if y == 2022 else c1
        o2 = F2 if y == 2024 else c2
        o3 = F3 if (y == 2026 and refi) else c3
        b1[i], b2[i], b3[i] = o1, o2, o3
        i1[i] = o1 * r1[i] / 100 * f1[i]; i2[i] = o2 * r2[i] / 100 * f2[i]; i3[i] = o3 * r3[i] / 100 * f3[i]
        a1[i] = min(o1, hc["amortization_pct_pa"] / 100 * F1 * f1[i])
        a2[i] = min(o2, SUPP["holdco_amort_pct_pa_incremental"] / 100 * F2 * f2[i])
        a3[i] = min(o3, SUPP["holdco_amort_pct_pa_repriced"] / 100 * F3 * f3[i])
        # tax
        ti[i] = taxable_ops[i] - dep[i] - tl_int[i] - rf_int[i] - u_int[i] - i1[i] - i2[i] - i3[i]
        nol_o[i] = nol
        nol_u[i] = min(nol, TX_NOL_LIMIT * max(ti[i], 0.0))
        tax[i] = TX_RATE * (max(ti[i], 0.0) - nol_u[i])
        nol = nol - nol_u[i] + max(-ti[i], 0.0)
        nol_c[i] = nol
        hc_ds[i] = i1[i] + i2[i] + i3[i] + a1[i] + a2[i] + a3[i]
        excess[i] = opco_dist[i] - tax[i] - hc_ds[i]
        sweep = sw * max(excess[i], 0.0)
        rem1 = o1 - a1[i]; rem2 = o2 - a2[i]; rem3 = o3 - a3[i]
        tot = rem1 + rem2 + rem3
        if tot > 0:
            sweep = min(sweep, tot)
            s1[i] = sweep * rem1 / tot; s2[i] = sweep * rem2 / tot; s3[i] = sweep * rem3 / tot
        c1 = rem1 - s1[i]; c2 = rem2 - s2[i]; c3 = rem3 - s3[i]
        if refi and y == 2025:
            rep1[i] = c1; rep2[i] = c2
            c1 = 0.0; c2 = 0.0
            recap_hold[i] = F3 * hr["oid_pct"] / 100.0 - rep1[i] - rep2[i]
        # limited liability: the fund does not cure holdco shortfalls; a shortfall is reported
        fund_dist[i] = max(0.0, excess[i] - s1[i] - s2[i] - s3[i])
    R.update(hc1_open=b1, hc1_int=i1, hc1_amort=a1, hc1_sweep=s1, hc1_repay=rep1,
             hc2_open=b2, hc2_int=i2, hc2_amort=a2, hc2_sweep=s2, hc2_repay=rep2,
             hc3_open=b3, hc3_int=i3, hc3_amort=a3, hc3_sweep=s3,
             hc_ds=hc_ds, taxable_ops=taxable_ops, dep=dep, taxable_income=ti, nol_open=nol_o,
             nol_used=nol_u, nol_close=nol_c, tax=tax, hc_excess=excess, fund_dist_ops=fund_dist,
             recap_hold=recap_hold)
    recap = recap_opco + recap_hold
    R["recap_total"] = recap
    R["fund_dist"] = fund_dist + recap
    # ---- Acquisition funding and fund cash flows ----
    acq = INP["acquisitions"]
    tlf = S["tl_debt"]
    su_a1 = dict(price=acq["A1"]["enterprise_value_usd_m"], costs=acq["A1"]["transaction_costs_usd_m"],
                 opco_fee=t["upfront_fee_pct"] / 100 * tlf, holdco_oid=(1 - hc["oid_pct"] / 100) * S["hc_face"],
                 opco_tl=tlf, holdco_tlb=S["hc_face"])
    su_a1["uses"] = su_a1["price"] + su_a1["costs"] + su_a1["opco_fee"] + su_a1["holdco_oid"]
    su_a1["equity"] = su_a1["uses"] - tlf - S["hc_face"]
    rf = D["redfern_loan_2023"]
    su_a2 = dict(price=acq["A2"]["enterprise_value_usd_m"], costs=acq["A2"]["transaction_costs_usd_m"],
                 fee=rf["upfront_fee_pct"] / 100 * S["rf_debt"], loan=S["rf_debt"])
    su_a2["uses"] = su_a2["price"] + su_a2["costs"] + su_a2["fee"]
    su_a2["equity"] = su_a2["uses"] - S["rf_debt"]
    itc_px = TX["itc_transfer_price_per_usd_of_credit"]
    dep_amt = acq["A3"]["barlow_deposit_pct"] / 100 * acq["A3"]["barlow_price_usd_m"]
    oid_i = (1 - hi["oid_pct"] / 100) * S["hi_face"]
    uses1 = dep_amt + acq["A3"]["transaction_costs_usd_m"] + oid_i
    # cash is carried from one A3 payment date to the next; equity funds any shortfall on each date
    carry = max(0.0, S["hi_face"] - uses1)
    eq1 = max(0.0, uses1 - S["hi_face"])
    need2 = acq["A3"]["kerrigan_price_usd_m"] - carry - itc7 * itc_px
    eq2 = max(0.0, need2)
    carry2 = max(0.0, -need2)
    need3 = acq["A3"]["barlow_price_usd_m"] - dep_amt - carry2 - itc8 * itc_px
    eq3 = max(0.0, need3)
    carry3 = max(0.0, -need3)
    su_a3 = dict(r7_price=acq["A3"]["kerrigan_price_usd_m"], r8_price=acq["A3"]["barlow_price_usd_m"],
                 r8_deposit=dep_amt, costs=acq["A3"]["transaction_costs_usd_m"], oid=oid_i,
                 holdco_incr=S["hi_face"], itc7=itc7, itc8=itc8, itc7_proceeds=itc7 * itc_px,
                 itc8_proceeds=itc8 * itc_px, eq_signing=eq1, eq_r7=eq2, eq_r8=eq3, carry=carry, carry2=carry2,
                 cash_left_after_r8=carry3)
    su_a3["uses"] = su_a3["r7_price"] + su_a3["r8_price"] + su_a3["costs"] + su_a3["oid"]
    su_a3["equity"] = eq1 + eq2 + eq3 - carry3
    R.update(su_a1=su_a1, su_a2=su_a2, su_a3=su_a3)
    flows = [(ser("2022-03-22"), -su_a1["equity"]), (ser("2023-08-31"), -su_a2["equity"]),
             (ser("2024-02-15"), -eq1), (ser("2024-04-02"), -eq2), (ser("2024-12-19"), -eq3)]
    flows += [(YE[i], R["fund_dist"][i]) for i in range(NT)]
    R["fund_flows"] = flows
    R["fund_irr_life"] = xirr(flows)
    contrib = su_a1["equity"] + su_a2["equity"] + eq1 + eq2 + eq3
    R["fund_contrib"] = contrib
    R["fund_moic_life"] = float(np.sum(R["fund_dist"])) / contrib
    # NAV at 2025-12-31 (levered equity rates by portfolio revenue bucket)
    lev_sh = {b: L["share_%s_all" % b] for b in BUCKETS}
    nav_df = levered_dfs("2025-12-31", lev_sh) * (YEARS > 2025)
    R["nav_df"] = nav_df
    R["nav_2025_unfloored"] = float(np.sum(R["fund_dist"] * nav_df))
    nav = max(0.0, R["nav_2025_unfloored"])  # limited liability: NAV is never negative
    R["nav_2025"] = nav
    fl25 = flows[:5] + [(YE[i], R["fund_dist"][i]) for i in range(NT) if YEARS[i] <= 2025]
    fl25[-1] = (fl25[-1][0], fl25[-1][1] + nav)
    R["fund_irr_2025"] = xirr(fl25)
    dist25 = float(np.sum(R["fund_dist"][YEARS <= 2025]))
    R["fund_dist_to_2025"] = dist25
    R["fund_moic_2025"] = (dist25 + nav) / contrib
    # ---- Ratios ----
    thr = SUPP["ratio_threshold_usd_m"]

    def ratio(n, d):
        return np.where(d > thr, n / np.where(d > thr, d, 1), np.nan)
    R["dscr_tl"] = ratio(L["cfads_a1"], R["tl_ds"])
    R["dscr_rf"] = ratio(L["assets"]["R6"]["mesa_cf"], R["rf_ds"])
    R["dscr_u"] = ratio(cfads, R["u_ds"])
    R["dscr_opco"] = ratio(cfads, opco_ds)
    R["hc_cov"] = ratio(opco_dist, hc_ds)
    return R


TX_RATE = TX["federal_rate_pct"] / 100.0
TX_NOL_LIMIT = 0.80


def xirr(flows):
    """IRR on dated flows (Actual/365, as Excel XIRR). Bisection on the root nearest zero:
    [0, 2] when the undiscounted sum is positive, otherwise [-0.5, 0]."""
    d0 = flows[0][0]

    def npv(r):
        return sum(cf / (1 + r) ** ((d - d0) / 365.0) for d, cf in flows)
    if npv(0.0) >= 0:
        lo, hi = 0.0, 2.0
    else:
        lo, hi = -0.5, 0.0
    flo, fhi = npv(lo), npv(hi)
    if flo * fhi > 0:
        return float("nan")
    for _ in range(200):
        mid = (lo + hi) / 2
        fm = npv(mid)
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


# --------------------------------------------------------------------------------------------
# Valuations by risk bucket
# --------------------------------------------------------------------------------------------
def unlev_dfs(v0):
    u = VAL["discount_rates_nominal_post_tax_pct"]["unlevered"]
    tau = np.maximum(0, (YE - ser(v0)) / 365.0)
    mask = (YE >= ser(v0)).astype(float)
    term = (1 + u["terminal_post_2040"] / 100.0) ** (-tau)
    out = {}
    for b in BUCKETS:
        df = (1 + u[b] / 100.0) ** (-tau)
        out[b] = np.where(YEARS > 2040, term, df) * mask
    out["storage_merchant"] = np.where(YEARS > 2040, term, (1 + u["storage_merchant"] / 100.0) ** (-tau)) * mask
    out["contracted_shield"] = (1 + u["contracted"] / 100.0) ** (-tau) * mask
    return out


def asset_value(L, aid, dfs):
    """PV by bucket of Mesa's unlevered post-tax cash flow (before purchase-price tax shield)."""
    r = L["assets"][aid]
    cf = r["mesa_cf"] - TX_RATE * r["mesa_taxable"]
    merch_df = dfs["storage_merchant"] if aid in STOR else dfs["merchant"]
    pv = {"contracted": float(np.sum(cf * r["s_contracted"] * dfs["contracted"])),
          "hedged": float(np.sum(cf * r["s_hedged"] * dfs["hedged"])),
          "merchant": float(np.sum(cf * r["s_merchant"] * merch_df))}
    pv["total"] = sum(pv.values())
    return pv, cf


def valuations(L):
    V = {}
    acq = INP["acquisitions"]
    dep, per, itc7, itc8 = tax_depreciation()
    # A1 at 2022-03-22
    dfs = unlev_dfs("2022-03-22")
    a1 = {}
    for aid in A1:
        a1[aid], _ = asset_value(L, aid, dfs)
    am_cf = -(L["am_cost"]) * (1 - TX_RATE)
    sh = {b: L["share_%s_a1" % b] for b in BUCKETS}
    am_pv = {b: float(np.sum(am_cf * sh[b] * dfs[b])) for b in BUCKETS}
    am_pv["total"] = sum(am_pv.values())
    a1["Platform costs"] = am_pv
    pre = sum(v["total"] for v in a1.values())
    price = acq["A1"]["enterprise_value_usd_m"]
    unit_dep = per["A1"] / price
    pv_dep = float(np.sum(unit_dep * dfs["contracted_shield"]))
    shield = TX_RATE * pv_dep * price
    V["A1"] = dict(by_asset=a1, pre_shield=pre, pv_dep_per_usd=pv_dep, shield_at_price=shield,
                   ev=pre + shield, price=price, npv_vs_price=pre + shield - price,
                   breakeven_price=pre / (1 - TX_RATE * pv_dep),
                   by_bucket={b: sum(v[b] for v in a1.values()) for b in BUCKETS})
    # A2 at 2023-08-31
    dfs = unlev_dfs("2023-08-31")
    r6, _ = asset_value(L, "R6", dfs)
    p2 = acq["A2"]["enterprise_value_usd_m"]
    pv_dep2 = float(np.sum(per["A2"] / p2 * dfs["contracted_shield"]))
    sh2 = TX_RATE * pv_dep2 * p2
    V["A2"] = dict(R6=r6, pre_shield=r6["total"], shield_at_price=sh2, ev=r6["total"] + sh2, price=p2,
                   npv_vs_price=r6["total"] + sh2 - p2, breakeven_price=r6["total"] / (1 - TX_RATE * pv_dep2))
    # A3 at 2024-02-15
    dfs = unlev_dfs("2024-02-15")
    r7, _ = asset_value(L, "R7", dfs)
    r8, _ = asset_value(L, "R8", dfs)
    tau7 = (ser("2024-04-02") - ser("2024-02-15")) / 365.0
    tau8 = (ser("2024-12-19") - ser("2024-02-15")) / 365.0
    uc = VAL["discount_rates_nominal_post_tax_pct"]["unlevered"]["contracted"] / 100.0
    itcpx = TX["itc_transfer_price_per_usd_of_credit"]
    itc_pv = itc7 * itcpx * (1 + uc) ** (-tau7) + itc8 * itcpx * (1 + uc) ** (-tau8)
    sh3 = TX_RATE * float(np.sum((per["R7"] + per["R8"]) * dfs["contracted_shield"]))
    pr = acq["A3"]["kerrigan_price_usd_m"] + acq["A3"]["barlow_price_usd_m"]
    dep_amt = acq["A3"]["barlow_deposit_pct"] / 100 * acq["A3"]["barlow_price_usd_m"]
    price_pv = dep_amt + acq["A3"]["kerrigan_price_usd_m"] * (1 + uc) ** (-tau7) + \
        (acq["A3"]["barlow_price_usd_m"] - dep_amt) * (1 + uc) ** (-tau8)
    ev3 = r7["total"] + r8["total"] + itc_pv + sh3
    V["A3"] = dict(R7=r7, R8=r8, itc_pv=itc_pv, shield=sh3, ev=ev3, price_nominal=pr, price_pv=price_pv,
                   npv_vs_price=ev3 - price_pv, itc7=itc7, itc8=itc8,
                   itc_proceeds=(itc7 + itc8) * itcpx)
    return V


# --------------------------------------------------------------------------------------------
# Opco debt by asset and portfolio diversification of yield
# --------------------------------------------------------------------------------------------
def debt_by_asset(base, S):
    """Allocate each opco-level facility to assets pro rata to the PV of each asset's own
    debt-service capacity (asset cash flow by bucket / bucket DSCR), using the facility's discount
    factors. Platform costs are absorbed pro rata."""
    out = {}
    t = D["opco_term_loan_2022"]["sizing_dscr_x_by_revenue_bucket"]
    u = D["refinancing_2025"]["uspp_notes"]["sizing_dscr_x_by_revenue_bucket"]
    for name, ids, dscr, df, mask, total in (
            ("opco_tl_2022", A1, t, S["tl_df"], S["tl_f"] > 0, S["tl_debt"]),
            ("uspp_2025", AIDS, u, S["u_df_blended"], S["u_f"] > 0, S["u_size"])):
        pv = {}
        for aid in ids:
            r = base["assets"][aid]
            cap = sum(r["mesa_cf"] * r["s_" + b] / dscr[b] for b in BUCKETS)
            pv[aid] = float(np.sum(cap * df * mask))
        tot = sum(pv.values())
        out[name] = {aid: total * v / tot for aid, v in pv.items()}
        out[name + "_pv_capacity"] = pv
    out["redfern_2023"] = {"R6": S["rf_debt"]}
    return out


def diversification():
    """Portfolio P50/P90/P99 (one-year and ten-year) with inter-asset correlations, plus the
    fully correlated and independent bounds for comparison."""
    out = {"assets": YSTAT, "correlations": CORR}
    for grp, ids in (("A1", A1), ("all_generation", GEN)):
        p50 = sum(ASSETS[a]["p50_gwh"] for a in ids)
        res = {"p50_gwh": p50}
        vlt = sum(ASSETS[i]["p50_gwh"] * YSTAT[i]["sigma_lt"] * ASSETS[j]["p50_gwh"] * YSTAT[j]["sigma_lt"] * corr_pair(i, j, "lt") for i in ids for j in ids)
        viav = sum(ASSETS[i]["p50_gwh"] * YSTAT[i]["sigma_iav"] * ASSETS[j]["p50_gwh"] * YSTAT[j]["sigma_iav"] * corr_pair(i, j, "iav") for i in ids for j in ids)
        for k, n in (("1yr", 1.0), ("10yr", 10.0)):
            sig = (vlt + viav / n) ** 0.5
            res["sigma_%s_gwh" % k] = sig
            for pk, z in (("p90", Z90), ("p99", Z99)):
                res["%s_%s_gwh" % (pk, k)] = p50 - z * sig
                res["%s_%s_pct" % (pk, k)] = 100 * (p50 - z * sig) / p50
            sig_c = sum(ASSETS[a]["p50_gwh"] * YSTAT[a]["sigma_%s" % k] for a in ids)
            sig_i = sum((ASSETS[a]["p50_gwh"] * YSTAT[a]["sigma_%s" % k]) ** 2 for a in ids) ** 0.5
            res["p90_%s_correlated_gwh" % k] = p50 - Z90 * sig_c
            res["p90_%s_independent_gwh" % k] = p50 - Z90 * sig_i
            res["p90_%s_correlated_pct" % k] = 100 * (p50 - Z90 * sig_c) / p50
            res["p90_%s_independent_pct" % k] = 100 * (p50 - Z90 * sig_i) / p50
        out[grp] = res
    return out


# --------------------------------------------------------------------------------------------
# Uri-type stress on R1's fixed-volume swap
# --------------------------------------------------------------------------------------------
def uri_stress():
    sc = INP["scenarios"]["sensitivities"][5]
    hours, price, avail = 72.0, 5000.0, 0.15
    h = H["R1_fixed_volume_swap"]
    mw = ASSETS["R1"]["mw_ac"]
    gen_mwh = mw * avail * hours
    swap_mwh = h["volume_mw_atc"] * hours
    swap_pay = swap_mwh * (price - h["price_usd_per_mwh"]) / 1e6
    phys = gen_mwh * price / 1e6
    net = phys - swap_pay
    short_mwh = swap_mwh - gen_mwh
    normal_hedged = swap_mwh * h["price_usd_per_mwh"] / 1e6
    return dict(hours=hours, price=price, availability=avail, gen_mwh=gen_mwh, swap_mwh=swap_mwh,
                shortfall_mwh=short_mwh, swap_payment=swap_pay, physical_revenue=phys, net_cash=net,
                net_vs_fully_covered=net - normal_hedged, label=sc)


# --------------------------------------------------------------------------------------------
# Runner
# --------------------------------------------------------------------------------------------
SCENARIOS = {
    "base": make_case(),
    "low": make_case(price="low"),
    "high": make_case(price="high"),
    "p90_1yr": make_case(volume="p90_1yr"),
    "p90_10yr": make_case(volume="p90_10yr"),
    "p99_1yr": make_case(volume="p99_1yr"),
    "status_quo": make_case(refi=False),
    "sens_west_solar_capture_m5": make_case(west_solar_capture_pts=-5.0),
    "sens_battery_low": make_case(battery="low"),
    "sens_curtailment_p3": make_case(curtail_add_pts=3.0),
    "sens_opex_p10": make_case(opex_factor=1.10),
    "sens_sofr_p100_unhedged": make_case(sofr_add_unhedged_pct=1.0),
}


def tolist(x):
    if isinstance(x, np.ndarray):
        return [None if not np.isfinite(v) else round(float(v), 10) for v in x]
    if isinstance(x, dict):
        return {str(k): tolist(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [tolist(v) for v in x]
    if isinstance(x, (np.floating, float)):
        return None if not np.isfinite(x) else float(x)
    if isinstance(x, (np.integer,)):
        return int(x)
    return x


def window_stats(arr, y0, y1):
    m = (YEARS >= y0) & (YEARS <= y1) & np.isfinite(arr)
    v = arr[m]
    return (float(np.min(v)) if v.size else float("nan"), float(np.mean(v)) if v.size else float("nan"))


def scenario_scalars(R, S):
    L = R["ops"]
    sc = {}
    sc["tl_dscr_min_2022_2025"], sc["tl_dscr_avg_2022_2025"] = window_stats(R["dscr_tl"], 2022, 2025)
    sc["tl_dscr_min_2022_2040"], sc["tl_dscr_avg_2022_2040"] = window_stats(R["dscr_tl"], 2022, 2040)
    sc["rf_dscr_min"], sc["rf_dscr_avg"] = window_stats(R["dscr_rf"], 2024, 2029)
    sc["uspp_dscr_min_2026_2043"], sc["uspp_dscr_avg_2026_2043"] = window_stats(R["dscr_u"], 2026, 2043)
    sc["opco_dscr_min_2026_2040"], sc["opco_dscr_avg_2026_2040"] = window_stats(R["dscr_opco"], 2026, 2040)
    sc["holdco_cov_min_2023_2031"], sc["holdco_cov_avg_2023_2031"] = window_stats(R["hc_cov"], 2023, 2031)
    sc["cfads_2026"] = float(L["cfads_all"][yidx(2026)])
    sc["cfads_avg_2026_2030"] = float(np.mean(L["cfads_all"][yidx(2026):yidx(2030) + 1]))
    sc["revenue_portfolio_2026"] = float(sum(L["assets"][a]["revenue"][yidx(2026)] for a in AIDS))
    sc["fund_irr_life_pct"] = 100 * R["fund_irr_life"]
    sc["fund_irr_2025_pct"] = 100 * R["fund_irr_2025"]
    sc["fund_moic_life_x"] = R["fund_moic_life"]
    sc["fund_moic_2025_x"] = R["fund_moic_2025"]
    sc["fund_nav_2025"] = R["nav_2025"]
    sc["fund_contributions"] = R["fund_contrib"]
    sc["fund_distributions_to_2025"] = R["fund_dist_to_2025"]
    sc["fund_distributions_life"] = float(np.sum(R["fund_dist"]))
    sc["recap_distribution_2025"] = float(R["recap_total"][yidx(2025)])
    sc["years_holdco_shortfall"] = int(np.sum(R["hc_excess"] < -1e-9))
    sc["holdco_shortfall_total"] = float(-np.sum(np.minimum(R["hc_excess"], 0.0)))
    sc["tax_paid_life"] = float(np.sum(R["tax"]))
    sc["holdco_balance_end_2031"] = float(R["hc1_open"][yidx(2032)] + R["hc2_open"][yidx(2032)] + R["hc3_open"][yidx(2032)])
    return sc


def checks(base, S, runs):
    C = []
    def add(name, val, tol=1e-6):
        C.append({"check": name, "value": float(val), "pass": bool(abs(val) <= tol)})
    add("Opco TL sculpted balance after 2040 (USD m)", S["tl_sched_close_end"])
    add("Redfern sculpted balance after 2030 (USD m)", S["rf_close_end"])
    add("USPP balance after 2043: opening 2026 minus total principal (USD m)", S["u_size"] - float(np.sum(S["u_prin"])))
    add("USPP DS = interest + principal vs sculpted target, max abs diff", float(np.max(np.abs(S["u_int"] + S["u_prin"] - S["u_ds"]))))
    for k, R in runs.items():
        L = R["ops"]
        add("[%s] revenue buckets sum to revenue, max abs diff" % k, float(max(np.max(np.abs(L["assets"][a]["rev_contracted"] + L["assets"][a]["rev_hedged"] + L["assets"][a]["rev_merchant"] - L["assets"][a]["revenue"])) for a in AIDS)))
        add("[%s] NOL never negative (min NOL, if <0)" % k, min(0.0, float(np.min(R["nol_close"]))))
        add("[%s] debt balances never negative (min, if <0)" % k, min(0.0, float(np.min(R["tl_open"])), float(np.min(R["rf_open"])), float(np.min(R["hc1_open"])), float(np.min(R["hc2_open"])), float(np.min(R["hc3_open"]))))
        a1 = R["su_a1"]
        add("[%s] A1 sources = uses" % k, a1["opco_tl"] + a1["holdco_tlb"] + a1["equity"] - a1["uses"])
        a3 = R["su_a3"]
        add("[%s] A3 sources = uses" % k, a3["holdco_incr"] + a3["itc7_proceeds"] + a3["itc8_proceeds"] + a3["equity"] - a3["uses"])
    return C


def main():
    base_ops = operations(make_case())
    p99_ops = operations(make_case(volume="p99_1yr"))
    S = size_all(base_ops, p99_ops)
    runs = {k: run(c, base_ops, p99_ops, S) for k, c in SCENARIOS.items()}
    vals = {k: valuations(runs[k]["ops"]) for k in ("base", "low", "high")}
    uri = uri_stress()
    return base_ops, p99_ops, S, runs, vals, uri


ASSET_SERIES = ["op_frac", "own_share", "deg", "curt", "gen_full", "gen", "hub_atc", "cap_hub", "cap_node",
                "node_price", "mkt_gen", "mkt_rev", "con_frac", "con_vol", "settle", "stor_rev", "revenue",
                "rev_contracted", "rev_hedged", "rev_merchant", "opex", "land", "bond", "margin_tax", "ebitda",
                "aug", "decom", "cf", "te_cash", "mesa_tax_share", "mesa_cf", "te_cf", "mesa_taxable",
                "s_contracted", "s_hedged", "s_merchant", "mesa_rev"]


def build_outputs(base_ops, p99_ops, S, runs, vals, uri):
    O = {"meta": {"case": "R", "model": "case_r.py", "model_version": "R-1.1", "inputs_file_version": INP["meta"]["file_version"],
                  "generated": "2026-10-03", "currency": "USD m nominal", "years": [int(y) for y in YEARS],
                  "supplementary_assumptions": SUPP}}
    O["sizing"] = {k: v for k, v in S.items()}
    O["sizing_cases"] = {"base_p50": {"cfads_a1": base_ops["cfads_a1"], "cfads_all": base_ops["cfads_all"], "cfads_a3": base_ops["cfads_a3"],
                                      **{"cfads_%s_%s" % (g, b): base_ops["cfads_%s_%s" % (g, b)] for g in ("a1", "all") for b in BUCKETS}},
                         "base_p99": {"cfads_a1": p99_ops["cfads_a1"], "cfads_all": p99_ops["cfads_all"]}}
    sc_out = {}
    for k, R in runs.items():
        L = R["ops"]
        ser_ = {}
        for a in AIDS:
            for f in ASSET_SERIES:
                ser_["%s.%s" % (a, f)] = L["assets"][a][f]
        ser_["R3.ptc_total"] = L["assets"]["R3"]["ptc_total"]
        for f in ("north_atc", "west_atc", "south_atc", "houston_atc", "batt_rate", "am_cost", "cfads_a1", "cfads_all", "cfads_a3",
                  "mesa_rev_all", "mesa_rev_a1") + tuple("share_%s_%s" % (b, g) for b in BUCKETS for g in ("a1", "all")) + \
                tuple("mesa_rev_%s_%s" % (b, g) for b in BUCKETS for g in ("a1", "all")) + tuple("cap_hub_" + b for b in BASIS):
            ser_["portfolio." + f] = L[f]
        for f in ("tl_open", "tl_int", "tl_prin", "tl_prepay", "tl_ds", "rf_open", "rf_int", "rf_prin", "rf_prepay", "rf_ds",
                  "u_open", "u_int", "u_prin", "u_ds", "opco_ds", "opco_dist", "recap_opco", "hc1_open", "hc1_int", "hc1_amort",
                  "hc1_sweep", "hc1_repay", "hc2_open", "hc2_int", "hc2_amort", "hc2_sweep", "hc2_repay", "hc3_open", "hc3_int",
                  "hc3_amort", "hc3_sweep", "hc_ds", "taxable_ops", "dep", "taxable_income", "nol_open", "nol_used", "nol_close",
                  "tax", "hc_excess", "fund_dist_ops", "recap_hold", "recap_total", "fund_dist", "nav_df", "dscr_tl", "dscr_rf",
                  "dscr_u", "dscr_opco", "hc_cov"):
            ser_["finance." + f] = R[f]
        sc_out[k] = {"case": SCENARIOS[k], "scalars": scenario_scalars(R, S), "series": ser_,
                     "sources_uses": {"A1": R["su_a1"], "A2": R["su_a2"], "A3": R["su_a3"]},
                     "refinancing_cash": R["refi_cash"],
                     "fund_flows": [{"date": (EPOCH + dt.timedelta(days=int(d))).isoformat(), "usd_m": float(v)} for d, v in R["fund_flows"]]}
    O["scenarios"] = sc_out
    O["valuations"] = vals
    O["uri_stress"] = uri
    O["debt_by_asset"] = debt_by_asset(base_ops, S)
    O["diversification"] = diversification()
    dec = {}
    for a in AIDS:
        r = base_ops["assets"][a]
        ly = int(ASSETS[a]["useful_life_end"][:4])
        dk = OX["decommissioning_net_of_salvage_usd_per_kw_2022"][DECOM_KEY[a]]
        dec[a] = {"retirement": ASSETS[a]["useful_life_end"], "usd_per_kw_2022": dk,
                  "cost_2022_prices": dk * ASSETS[a]["mw_ac"] / 1000.0,
                  "bonded_amount_2026": dk * ASSETS[a]["mw_ac"] / 1000.0 * ESC[yidx(2026)],
                  "bond_cost_2026": float(r["bond"][yidx(2026)]),
                  "cost_nominal_at_retirement": float(r["decom"][yidx(ly)]),
                  "pv_2025_at_unlevered_terminal_rate": float(r["decom"][yidx(ly)] * (1 + VAL["discount_rates_nominal_post_tax_pct"]["unlevered"]["terminal_post_2040"] / 100) ** (-(ly - 2025)))}
    O["decommissioning"] = dec
    O["checks"] = checks(base_ops, S, runs)
    return tolist(O)


def write_all(base_ops, p99_ops, S, runs, vals, uri):
    O = build_outputs(base_ops, p99_ops, S, runs, vals, uri)
    json.dump(O, open(os.path.join(HERE, "outputs_case_r.json"), "w"), indent=0)
    import report_case_r
    report_case_r.write_report(O, os.path.join(HERE, "case_r_report.md"))
    return O


if __name__ == "__main__":
    write_all(*main())
