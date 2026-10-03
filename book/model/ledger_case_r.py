"""Writes model/figure-ledger-case-r.md from outputs_case_r.json (every value is read from the JSON)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
O = json.load(open(os.path.join(HERE, "outputs_case_r.json")))
INP = json.load(open(os.path.join(HERE, "inputs_case_r.json")))
VER = "%s (inputs v%s)" % (O["meta"]["model_version"], O["meta"]["inputs_file_version"])


def g(path):
    v = O
    for p in path:
        v = v[p] if not isinstance(v, list) else v[p]
    return v


def yr(y):
    return y - 2022


def fmt(v, unit):
    if v is None:
        return "n.m."
    if unit in ("x",):
        return "%.2fx" % v
    if unit == "%":
        return "%.2f%%" % v
    if unit in ("USD/MWh",):
        return "%.2f" % v
    if unit == "share":
        return "%.1f%%" % (100 * v)
    if unit in ("ratio", "fraction"):
        return "%.3f" % v
    if unit == "years":
        return "%d" % v
    if unit == "MWh":
        return "{:,.0f}".format(v)
    return "{:,.1f}".format(v)


L = []
w = L.append
w("# Figure ledger, Case R (Mesa Corta Renewables)\n")
w("Every value below is read by `model/ledger_case_r.py` from `model/outputs_case_r.json` (model %s, generated %s). "
  "The JSON path is given for each figure so a reviewer can trace it. Display rounding follows the style sheet: USD m to one decimal, "
  "ratios to two decimals with x, rates to two decimals, returns to one decimal in prose. Scenario names: base, low, high (price and capture cases), "
  "p90_1yr, p90_10yr, p99_1yr (volume cases applied in every year), status_quo (no 2025 refinancing), sens_* (sensitivities). "
  "Debt is sized once on the base case and held fixed in every other scenario. Every Case R price is Illustrative. "
  "Figures R-F11 to R-F17 are new IDs added by the modeler; R-F18 and R-F19 come from Case Bible Annex TR (R.4, R.5). "
  "Terminal value rule (Annex TR R.7): cash flows after 2040 and within each asset's useful life are discounted at the 10.50%% unlevered tail rate from the valuation date; "
  "no terminal value beyond any useful life; no post-2040 levered rate (NAV uses bucket-weighted levered rates in every year). "
  "Battery convention (Annex TR R.5): usable energy is tracked at each period start and end; revenue scales by min(1, average usable / nameplate).\n" % (VER, O["meta"]["generated"]))
w("| ID | Figure | Value | Units | Scenario | Story date | JSON path |")
w("|---|---|---|---|---|---|---|")


def row(fid, label, path, unit, sc, date, value=None):
    v = g(path) if value is None else value
    src = ".".join(str(p) for p in path) if path else "computed in ledger_case_r.py from the JSON paths named in the label's components"
    w("| %s | %s | %s | %s | %s | %s | `%s` |" % (fid, label, fmt(v, unit) if not isinstance(v, str) else v, unit, sc, date, src))


# R-F01 yield
for a in INP["assets"]:
    aid = a["id"]
    if aid not in O["diversification"]["assets"]:
        continue
    ys = ["diversification", "assets", aid]
    w("| R-F01 | %s P50 (input) | %.1f | GWh/yr | inputs | 2021-12 | inputs_case_r.json assets |" % (aid, a["p50_gwh"]))
    for k, lab in (("p90_1yr", "P90 one-year"), ("p90_10yr", "P90 ten-year"), ("p99_1yr", "P99 one-year (recomputed, R-C09)"), ("p99_10yr", "P99 ten-year")):
        row("R-F01", "%s %s" % (aid, lab), ys + [k], "%", "yield model", "2021-12")
    for k, lab in (("sigma_lt", "long-term sigma"), ("sigma_iav", "inter-annual sigma"), ("sigma_1yr", "one-year sigma"), ("sigma_10yr", "ten-year sigma")):
        row("R-F01", "%s %s (fraction of P50)" % (aid, lab), ys + [k], "ratio", "yield model", "2021-12")
for grp, lab in (("A1", "A1 portfolio (R1-R5)"), ("all_generation", "All generation (R1-R5, R8)")):
    for k, l2, u in (("p50_gwh", "P50", "GWh"), ("p90_1yr_gwh", "P90 one-year", "GWh"), ("p90_1yr_pct", "P90 one-year", "%"), ("p99_1yr_gwh", "P99 one-year", "GWh"),
                     ("p99_1yr_pct", "P99 one-year", "%"), ("p90_10yr_gwh", "P90 ten-year", "GWh"), ("p90_10yr_pct", "P90 ten-year", "%"), ("p99_10yr_gwh", "P99 ten-year", "GWh"),
                     ("p99_10yr_pct", "P99 ten-year", "%"), ("p90_1yr_correlated_pct", "P90 one-year if fully correlated", "%"), ("p90_1yr_independent_pct", "P90 one-year if independent", "%")):
        row("R-F01", "%s %s" % (lab, l2), ["diversification", grp, k], u, "yield model (correlated)", "2021-12")
for k, v in O["diversification"]["correlations"].items():
    w("| R-F01 | Yield correlation %s | %.2f | rho | assumption (R-C10) | 2021-12 | `diversification.correlations.%s` |" % (k, v, k))

# R-F02 hedge book
B = ["scenarios", "base", "series"]
for y in range(2022, 2035):
    i = yr(y)
    for aid, lab, unit in (("R1", "R1 swap volume", "GWh"), ("R4", "R4 shape hedge volume", "GWh"), ("R8", "R8 shape hedge volume", "GWh"), ("R2", "R2 PPA volume", "GWh"), ("R5", "R5 vPPA volume", "GWh")):
        v = g(B + [aid + ".con_vol"])[i]
        if abs(v) > 1e-9:
            row("R-F02", "%s %d" % (lab, y), B + [aid + ".con_vol", i], unit, "base", "2022-10 to 2023")
    for aid, lab in (("R1", "R1 swap settlement"), ("R2", "R2 PPA revenue"), ("R3", "R3 PRS net settlement"), ("R4", "R4 shape hedge settlement"), ("R5", "R5 vPPA settlement"),
                     ("R6", "R6 toll revenue"), ("R7", "R7 revenue under floor contract"), ("R8", "R8 shape hedge settlement")):
        v = g(B + [aid + ".settle"])[i]
        if abs(v) > 1e-9:
            row("R-F02", "%s %d" % (lab, y), B + [aid + ".settle", i], "USD m", "base", "2022-10 to 2023")
    for bk in ("contracted", "hedged", "merchant"):
        row("R-F02", "Share of Mesa revenue %s %d" % (bk, y), B + ["portfolio.share_%s_all" % bk, i], "share", "base", "2022-10 to 2023")
for sc in ("low", "high"):
    for y in (2026, 2028, 2030):
        for aid in ("R1", "R4", "R5", "R8"):
            row("R-F02", "%s settlement %d (%s)" % (aid, y, sc), ["scenarios", sc, "series", aid + ".settle", yr(y)], "USD m", sc, "2022-10 to 2023")

# R-F03 Uri
for k, lab, u in (("swap_mwh", "Swap volume over the event", "MWh"), ("gen_mwh", "R1 generation over the event", "MWh"), ("shortfall_mwh", "Volume shortfall", "MWh"),
                  ("swap_payment", "Swap settlement paid", "USD m"), ("physical_revenue", "Physical revenue", "USD m"), ("net_cash", "Net cash over the event", "USD m"),
                  ("net_vs_fully_covered", "Net cash versus normal hedged revenue for the same hours", "USD m")):
    row("R-F03", lab, ["uri_stress", k], u, "sensitivity (72 h at USD 5,000/MWh, 15% availability)", "2022-10")

# R-F04 A1 valuation
for sc in ("base", "low", "high"):
    V = ["valuations", sc, "A1"]
    for aid in ("R1", "R2", "R3", "R4", "R5", "Platform costs"):
        for bk in ("contracted", "hedged", "merchant", "total"):
            if sc != "base" and bk != "total":
                continue
            row("R-F04", "A1 value %s %s" % (aid, bk), V + ["by_asset", aid, bk], "USD m", sc, "2021-12-09 (bid), valued at 2022-03-22")
    for bk in ("contracted", "hedged", "merchant"):
        row("R-F04", "A1 value by bucket %s" % bk, V + ["by_bucket", bk], "USD m", sc, "2021-12-09")
    for k, lab, u in (("pre_shield", "A1 value before purchase-price tax shield", "USD m"), ("shield_at_price", "Tax shield at the price paid", "USD m"), ("ev", "A1 enterprise value", "USD m"),
                      ("price", "A1 price paid (calibrated, R-C04)", "USD m"), ("npv_vs_price", "Value less price", "USD m"), ("breakeven_price", "Breakeven price", "USD m")):
        row("R-F04", lab, V + [k], u, sc, "2021-12-09")

# R-F05 A1 financing
S = ["sizing"]
SU = ["scenarios", "base", "sources_uses", "A1"]
for k, lab in (("price", "Uses: purchase price"), ("costs", "Uses: transaction costs"), ("opco_fee", "Uses: opco upfront fee"), ("holdco_oid", "Uses: holdco OID"), ("uses", "Uses: total"),
               ("opco_tl", "Sources: opco term loan"), ("holdco_tlb", "Sources: holdco TLB (face)"), ("equity", "Sources: fund equity")):
    row("R-F05", lab, SU + [k], "USD m", "base", "2022-03-22")
for k, lab, u in (("tl_pv_cap_contracted", "Opco TL capacity from contracted CFADS (PV)", "USD m"), ("tl_pv_cap_hedged", "Opco TL capacity from hedged CFADS (PV)", "USD m"),
                  ("tl_pv_cap_merchant", "Opco TL capacity from merchant CFADS (PV)", "USD m"), ("tl_debt", "Opco term loan", "USD m"), ("tl_p99_binds_years", "Years the P99 test binds", "years"),
                  ("hc_face_cov", "Holdco TLB supported by 1.75x coverage", "USD m"), ("opco_eq_val_2022", "Opco equity value (levered rates)", "USD m"), ("hc_face_cap", "Holdco cap at 45% of opco equity value", "USD m"),
                  ("hc_face", "Holdco TLB face", "USD m"), ("hc_binding", "Holdco binding constraint", "text")):
    row("R-F05", lab, S + [k], u, "base; P99 test", "2022-03-22")
for y in range(2022, 2026):
    row("R-F05", "Opco TL sizing rate %d" % y, S + ["tl_rate", yr(y)], "%", "base", "2022-03-22")
row("R-F05", "Gearing at A1 (opco TL / price)", ["derived", "a1_opco_gearing_pct"], "%", "base", "2022-03-22")
row("R-F05", "Total leverage at A1 ((opco TL + holdco) / price)", ["derived", "a1_total_leverage_pct"], "%", "base", "2022-03-22")

# R-F06 capture and revenue build
for sc in ("base", "low"):
    for aid in ("R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"):
        for y in range(2022, 2031):
            i = yr(y)
            if aid in ("R1", "R2", "R3", "R4", "R5", "R8"):
                row("R-F06", "%s generation %d" % (aid, y), ["scenarios", sc, "series", aid + ".gen", i], "GWh", sc, "2022 to 2030")
                row("R-F06", "%s node capture ratio %d" % (aid, y), ["scenarios", sc, "series", aid + ".cap_node", i], "ratio", sc, "2022 to 2030")
                row("R-F06", "%s realized node price %d" % (aid, y), ["scenarios", sc, "series", aid + ".node_price", i], "USD/MWh", sc, "2022 to 2030")
            row("R-F06", "%s revenue %d" % (aid, y), ["scenarios", sc, "series", aid + ".revenue", i], "USD m", sc, "2022 to 2030")
        for y in range(2022, 2031):
            pass
    for y in range(2022, 2031):
        row("R-F06", "West Hub ATC %d" % y, ["scenarios", sc, "series", "portfolio.west_atc", yr(y)], "USD/MWh", sc, "2022 to 2030")
        row("R-F06", "Portfolio CFADS (Mesa share) %d" % y, ["scenarios", sc, "series", "portfolio.cfads_all", yr(y)], "USD m", sc, "2022 to 2030")

# R-F07 A2/A3
V2 = ["valuations", "base", "A2"]; V3 = ["valuations", "base", "A3"]
for k, lab in (("pre_shield", "A2 R6 value before shield"), ("shield_at_price", "A2 tax shield"), ("ev", "A2 value"), ("price", "A2 price (calibrated, R-C05)"), ("npv_vs_price", "A2 value less price"), ("breakeven_price", "A2 breakeven price")):
    row("R-F07", lab, V2 + [k], "USD m", "base", "2023-08-31")
for bk in ("contracted", "merchant"):
    row("R-F07", "A2 R6 value %s" % bk, V2 + ["R6", bk], "USD m", "base", "2023-08-31")
for k, lab in (("price", "A2 uses: price"), ("costs", "A2 uses: costs"), ("fee", "A2 uses: Redfern fee"), ("loan", "A2 sources: Redfern loan"), ("equity", "A2 sources: fund equity")):
    row("R-F07", lab, ["scenarios", "base", "sources_uses", "A2", k], "USD m", "base", "2023-08-31")
row("R-F07", "Redfern loan minimum DSCR 2024-2029", ["scenarios", "base", "scalars", "rf_dscr_min"], "x", "base", "2023-08-31")
for aid in ("R7", "R8"):
    for bk in ("contracted", "hedged", "merchant", "total"):
        row("R-F07", "A3 %s value %s" % (aid, bk), V3 + [aid, bk], "USD m", "base", "2024-02-15")
for k, lab in (("itc7", "R7 ITC"), ("itc8", "R8 ITC"), ("itc_proceeds", "ITC transfer proceeds (nominal)"), ("itc_pv", "ITC transfer proceeds (PV at signing)"), ("shield", "A3 tax shield"),
               ("ev", "A3 value"), ("price_nominal", "A3 prices (calibrated, R-C06)"), ("price_pv", "A3 price payments (PV at signing)"), ("npv_vs_price", "A3 value less PV of price")):
    row("R-F07", lab, V3 + [k], "USD m", "base", "2024-02-15")
for k, lab in (("r8_deposit", "A3 R8 deposit"), ("costs", "A3 costs"), ("oid", "A3 holdco incremental OID"), ("holdco_incr", "Holdco incremental term loan"), ("itc7_proceeds", "R7 ITC proceeds"),
               ("itc8_proceeds", "R8 ITC proceeds"), ("eq_signing", "A3 equity at signing"), ("eq_r7", "A3 equity at R7 COD"), ("eq_r8", "A3 equity at R8 COD"), ("equity", "A3 fund equity")):
    row("R-F07", lab, ["scenarios", "base", "sources_uses", "A3", k], "USD m", "base", "2024-02-15 to 2024-12-19")

# R-F08 refinancing
for k in ("A", "B", "C"):
    row("R-F08", "USPP Series %s size" % k, S + ["u_series_size", k], "USD m", "base", "2025-10-21 (priced)")
    row("R-F08", "USPP Series %s share" % k, S + ["u_series_share", k], "%", "base", "2025-10-21")
for k, lab, u in (("u_size", "USPP notes total", "USD m"), ("u_coupon", "Blended coupon (issue-weighted)", "%"), ("u_pv_cap_contracted", "USPP capacity from contracted CFADS (PV at blended coupon)", "USD m"),
                  ("u_pv_cap_hedged", "USPP capacity from hedged CFADS (PV)", "USD m"), ("u_pv_cap_merchant", "USPP capacity from merchant CFADS (PV)", "USD m"),
                  ("u_p99_binds_years", "Years the USPP P99 test binds", "years"), ("hn_face", "Repriced holdco TLB face", "USD m")):
    row("R-F08", lab, S + [k], u, "base", "2025-12-16 (modeled 2025-12-31)")
RC = ["scenarios", "base", "refinancing_cash"]
for k, lab in (("tl_repay", "Opco term loan repaid"), ("rf_repay", "Redfern loan repaid"), ("mtm_opco_receivable", "Opco swap unwind receivable"), ("mtm_redfern_payable", "Redfern swap unwind payable"),
               ("costs", "USPP transaction costs"), ("opco_net", "Net opco proceeds to holdco")):
    row("R-F08", lab, RC + [k], "USD m", "base", "2025-12-16")
row("R-F08", "Holdco tranches repaid at repricing", ["derived", "holdco_repaid_at_repricing"], "USD m", "base", "2025-12-16")
row("R-F08", "Holdco repricing net proceeds", B + ["finance.recap_hold", 3], "USD m", "base", "2025-12-16")
row("R-F08", "Recapitalization distribution to the fund", ["scenarios", "base", "scalars", "recap_distribution_2025"], "USD m", "base", "2025-12-16")
row("R-F08", "Minimum USPP DSCR 2026-2043", ["scenarios", "base", "scalars", "uspp_dscr_min_2026_2043"], "x", "base", "2025-12-31")
row("R-F08", "Average USPP DSCR 2026-2043", ["scenarios", "base", "scalars", "uspp_dscr_avg_2026_2043"], "x", "base", "2025-12-31")
row("R-F08", "Repriced holdco balance at 2031 maturity (refinancing requirement)", ["scenarios", "base", "scalars", "holdco_balance_end_2031"], "USD m", "base", "2031-12-31 (projected)")
for sc in ("base", "status_quo"):
    row("R-F08", "Fund gross IRR, life (%s)" % sc, ["scenarios", sc, "scalars", "fund_irr_life_pct"], "%", sc, "2025-12-31")
    row("R-F08", "Fund gross IRR to 2025 incl. NAV (%s)" % sc, ["scenarios", sc, "scalars", "fund_irr_2025_pct"], "%", sc, "2025-12-31")
row("R-F08", "IRR impact of the refinancing, life (percentage points)", ["derived", "irr_impact_life_pts"], "%", "base less status_quo", "2025-12-31")
row("R-F08", "IRR impact of the refinancing, to 2025 incl. NAV (percentage points)", ["derived", "irr_impact_2025_pts"], "%", "base less status_quo", "2025-12-31")

# R-F09 fund returns
for sc in ("base", "status_quo"):
    SC = ["scenarios", sc, "scalars"]
    for k, lab, u in (("fund_contributions", "Fund equity contributed (A1+A2+A3)", "USD m"), ("fund_distributions_to_2025", "Distributions to December 31, 2025", "USD m"),
                      ("fund_nav_2025", "NAV at December 31, 2025", "USD m"), ("fund_irr_2025_pct", "Gross IRR to December 31, 2025 incl. NAV", "%"),
                      ("fund_moic_2025_x", "Multiple to December 31, 2025 incl. NAV", "x"), ("fund_irr_life_pct", "Gross IRR, life", "%"), ("fund_moic_life_x", "Multiple, life", "x")):
        row("R-F09", lab + " (%s)" % sc, SC + [k], u, sc, "2025-12-31")
for y in range(2022, 2026):
    row("R-F09", "Fund distribution %d" % y, B + ["finance.fund_dist", yr(y)], "USD m", "base", "%d-12-31" % y)

# R-F10 decommissioning
for aid, dct in O["decommissioning"].items():
    for k, lab in (("cost_2022_prices", "cost in 2022 prices"), ("bonded_amount_2026", "bonded amount 2026"), ("bond_cost_2026", "surety cost 2026"), ("cost_nominal_at_retirement", "nominal cost at retirement")):
        w("| R-F10 | %s decommissioning %s (retires %s) | %s | USD m | base | 2026-03 | `decommissioning.%s.%s` |" % (aid, lab, dct["retirement"], ("%.3f" % dct[k]) if k == "bond_cost_2026" else "%.1f" % dct[k], aid, k))

# New figures
for k, lab in (("rf_debt", "Redfern term loan"), ("hi_face", "Holdco incremental term loan")):
    row("R-F11", lab, S + [k], "USD m", "base", "2023-08-31 / 2024-02-15")
row("R-F11", "Holdco coverage 2024 (incremental interest before R8 COD)", B + ["finance.hc_cov", 2], "x", "base", "2024-12-31")
row("R-F11", "Minimum opco TL DSCR 2022-2025", ["scenarios", "base", "scalars", "tl_dscr_min_2022_2025"], "x", "base", "2022 to 2025")
for y in range(2022, 2026):
    row("R-F11", "Opco TL DSCR %d" % y, B + ["finance.dscr_tl", yr(y)], "x", "base", "%d" % y)
for f, lab in (("opco_tl_2022", "Opco TL allocated"), ("uspp_2025", "USPP allocated")):
    for aid, v in O["debt_by_asset"][f].items():
        row("R-F12", "%s to %s" % (lab, aid), ["debt_by_asset", f, aid], "USD m", "base", "2022-03-22" if f.startswith("opco") else "2025-12-31")
for sc in O["scenarios"]:
    SC = ["scenarios", sc, "scalars"]
    for k, lab, u in (("cfads_2026", "Portfolio CFADS 2026", "USD m"), ("uspp_dscr_min_2026_2043", "Minimum USPP DSCR", "x"), ("holdco_cov_min_2023_2031", "Minimum holdco coverage 2023-2031", "x"),
                      ("fund_irr_life_pct", "Fund gross IRR, life", "%"), ("fund_irr_2025_pct", "Fund gross IRR to 2025 incl. NAV", "%"), ("years_holdco_shortfall", "Years with holdco shortfall", "years")):
        row("R-F13", "%s (%s)" % (lab, sc), SC + [k], u, sc, "2025-12-31 view")
for y in range(2022, 2036):
    row("R-F14", "Cash tax %d" % y, B + ["finance.tax", yr(y)], "USD m", "base", "%d" % y)
    row("R-F14", "NOL closing %d" % y, B + ["finance.nol_close", yr(y)], "USD m", "base", "%d" % y)
for y in range(2026, 2044):
    row("R-F15", "USPP debt service %d" % y, B + ["finance.u_ds", yr(y)], "USD m", "base", "%d" % y)
    row("R-F15", "USPP DSCR %d" % y, B + ["finance.dscr_u", yr(y)], "x", "base", "%d" % y)
    row("R-F15", "USPP opening balance %d" % y, B + ["finance.u_open", yr(y)], "USD m", "base", "%d" % y)
for y in range(2022, 2041):
    row("R-F16", "Opco TL sculpted debt service %d" % y, S + ["tl_ds", yr(y)], "USD m", "base", "2022-03-22")
    row("R-F16", "Opco TL scheduled opening balance %d" % y, S + ["tl_sched_open", yr(y)], "USD m", "base", "2022-03-22")
for y in range(2026, 2032):
    row("R-F17", "Repriced holdco opening balance %d" % y, B + ["finance.hc3_open", yr(y)], "USD m", "base", "%d" % y)
    row("R-F17", "Holdco coverage %d" % y, B + ["finance.hc_cov", yr(y)], "x", "base", "%d" % y)

# R-F18 R7 revenue floor (Annex TR R.4)
for sc in ("base", "low", "high"):
    for y in range(2024, 2033):
        i = yr(y)
        Ssc = ["scenarios", sc, "series"]
        row("R-F18", "R7 reference revenue %d" % y, Ssc + ["R7.floor_ref", i], "USD/MWh", sc, "%d (calendar year; contract years pro rata)" % y)
        for f, lab in (("floor_payment", "floor payment from Galloway"), ("floor_premium", "premium"), ("floor_upside", "upside share to Galloway"), ("floor_net", "net floor settlement")):
            row("R-F18", "R7 %s %d" % (lab, y), Ssc + ["R7." + f, i], "USD m", sc, "%d" % y)
# R-F19 battery capacity (Annex TR R.5)
for aid in ("R6", "R7"):
    for y in range(2023 if aid == "R6" else 2024, 2045):
        i = yr(y)
        for f, lab, u in (("bat_usable_start", "usable energy, start of year", "MWh"), ("bat_usable_end", "usable energy, end of year", "MWh"),
                          ("bat_aug_mwh", "augmentation installed", "MWh"), ("aug", "augmentation cost", "USD m"), ("bat_scale", "revenue scaling factor", "ratio")):
            v = g(B + ["%s.%s" % (aid, f), i])
            if f in ("bat_aug_mwh", "aug") and abs(v) < 1e-9:
                continue
            row("R-F19", "%s %s %d" % (aid, lab, y), B + ["%s.%s" % (aid, f), i], u, "base", "%d" % y)
row("R-F19", "R6 lowest usable energy in the toll term (requirement 200 MWh)", ["battery_check", "r6_min_usable_in_toll_term_mwh"], "MWh", "base", "2023-07-14 to 2030-07-13")

w("\nNew IDs: R-F11 A2 and A3 debt and early ratios (Chapters 31, 73); R-F12 opco debt by asset; R-F13 scenario and sensitivity results; "
  "R-F14 cash tax and NOL profile; R-F15 USPP debt service and DSCR profile; R-F16 opco term loan sculpted schedule; R-F17 repriced holdco profile.\n")
open(os.path.join(HERE, "figure-ledger-case-r.md"), "w").write("\n".join(L) + "\n")
print(len(L))
