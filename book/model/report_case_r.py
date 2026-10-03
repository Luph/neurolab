"""Writes model/case_r_report.md from the outputs dictionary produced by case_r.py."""
import json

YEARS = list(range(2022, 2060))


def yi(y):
    return y - 2022


def f1(x):
    if x is None:
        return "n.m."
    return "(%.1f)" % -x if x < -0.05 else "%.1f" % (0.0 if abs(x) < 0.05 else x)


def f2(x):
    return "n.m." if x is None else "%.2f" % x


def pct(x, d=1):
    return "n.m." if x is None else ("%." + str(d) + "f%%") % x


def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "|".join(["---"] * len(head)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out) + "\n"


def write_report(O, path):
    B = O["scenarios"]["base"]
    Sb = B["series"]
    S = O["sizing"]
    inp = json.load(open(path.replace("case_r_report.md", "inputs_case_r.json")))
    L = []
    w = L.append
    w("# Case R reference model report: Mesa Corta Renewables (ERCOT)\n")
    w("Model version %s, inputs file version %s, generated %s. All money USD millions nominal unless stated. "
      "Every Case R price is Illustrative (Case Bible illustrative price paths; not ERCOT settlement data and not a forecast). "
      "Source of every number: `model/outputs_case_r.json`, produced by `python3 model/case_r.py`.\n"
      % (O["meta"]["model_version"], O["meta"]["inputs_file_version"], O["meta"]["generated"]))

    w("## 1. Assumption changes (modeler calibration, pre-publication)\n")
    w("The v1.0 inputs produce a base-case unlevered value for A1 of about USD 438 million against a USD 1,184.6 million price "
      "(high case about USD 611 million), a fund IRR below zero and opco debt of about USD 328 million against a 520 to 600 "
      "design range. Revenue per MW is realistic for ERCOT (West Texas wind about USD 100,000 per MW-year in 2025); the prices "
      "were not. The fix keeps every market, contract, asset and financing term and recalibrates the four acquisition prices (R-C04 to R-C08; R-C09 and R-C10 follow the editor-in-chief's yield note) "
      "to just above the model's base-case breakeven values, so the bids read as full auction prices. These are larger than "
      "'small' changes and need editor-in-chief sign-off.\n")
    rows = [[c["id"], c["item"], c["old"], c["new"], c["reason"]] for c in inp["calibration_log"]]
    w(table(["ID", "Item", "Old", "New", "Reason"], rows))
    w("\nSupplementary assumptions where the Case Bible is silent (also on the workbook Inputs sheet):\n")
    sp = O["meta"]["supplementary_assumptions"]
    w(table(["Item", "Value", "Use"], [
        ["Insurance share of base opex", "%.1f%%" % sp["insurance_share_of_opex_pct"], "the 22% 2023 insurance step-up applies to this share"],
        ["R3 PTC rate 2026 to November 2029", "USD %.2f/MWh" % sp["ptc_after_2025_usd_per_mwh"], "held at the 2025 value; 99% to tax equity"],
        ["Curtailment 2023 and 2024", "linear between 2022 and 2025 values", "West wind 5.0%, 5.5%; Panhandle 5.8%, 6.4%; West solar 2.5%, 3.0%"],
        ["Availability of wind and solar", "P50 is net of long-term availability (factor 100%)", "batteries: 97.5% applied to merchant revenue; toll paid in full above 97.0%"],
        ["Yield distribution", "normal; sigma split into long-term and inter-annual components", "P99s recomputed from P90s (R-C09); correlations added (R-C10)"],
        ["P50 reference year for degradation", "2022 (A1 assets), 2025 (R8)", "degradation compounds from the reference year"],
        ["Battery augmentation cost", "USD 41/kWh in 2025 prices, +2.5% a year", "6% of MWh in calendar year COD+5 and COD+9"],
        ["Holdco coverage test years", "2023-2027 (2022 TLB); 2025-2027 (2024 incremental); 2026-2031 (2025 repricing)", "full years before maturity"],
        ["Holdco amortization", "1% a year of original face on every tranche, 50% excess cash sweep", "repriced tranche keeps the sweep"],
        ["Tax", "Mesa Corta is modeled as a taxable blocker (21%); bonus and MACRS on purchase prices (85% 5-year, 10% 15-year, 5% land); ITC basis reduction 50% of credit; NOL 80% limit", "fees, OID and swap unwind gains are not deducted; interest limitation not modeled; Mesa's 1% PTC share ignored"],
    ]))
    w("\nModel conventions:\n")
    for t in [
        "Annual periods 2022 to 2059, first period in column J; day-count fractions for every partial year (acquisitions, COD, contract end, loan dates).",
        "Asset rows are 100% of each asset for its operating fraction; Mesa's share applies the owned share (from the acquisition date) and deducts tax-equity cash (R3 40% to December 31, 2029 then 5%; R5 20% to June 30, 2027 then 5%).",
        "Hub capture ratio follows the bucket path (low: 1.5x decline, floor 0.04 lower; high: 0.5x decline). Node capture = hub capture minus the basis. Physical sales settle at node capture; hedges and the vPPA settle at hub (R4 and R8 shape factor = solar hub capture ratio).",
        "Revenue buckets: contracted = R2 PPA revenue, R3 PRS fixed payment, R5 vPPA strike x volume, R6 toll, R7 floor less premium; hedged = swap and shape-hedge volume x strike; merchant = the rest (can be negative where basis is paid). CFADS is split across buckets in proportion to Mesa-share revenue.",
        "Debt is sized once, on the base price case at P50 with the P99 one-year test, and held fixed in every other scenario. Sculpted debt service = min(sum of bucket CFADS / bucket DSCR, P99 CFADS / P99 minimum DSCR).",
        "Status quo (no refinancing) case: the opco term loan continues on its sculpted notional profile to 2040 at the stepped margin (unhedged after March 22, 2029), the Redfern loan runs to 2030, holdco tranches keep 1% amortization and the 50% sweep; maturities are assumed extended like-for-like (balances at maturity are reported as refinancing requirements). Cash sweeps at opco are not applied in either case.",
        "Fund cash flows are gross of fund fees and carry; acquisition equity on the deal dates, distributions at December 31. Negative holdco cash is treated as an equity cure (fund contribution). NAV at December 31, 2025 = PV of later fund distributions at the levered equity rates weighted by portfolio revenue bucket shares, floored at zero.",
        "Bid valuations: Mesa's unlevered post-tax cash flow by asset, split by revenue bucket and discounted at the bucket rate (storage merchant rate for battery merchant revenue); all cash flows after 2040 at the 10.50% terminal rate; tax computed stand-alone (losses valued when generated); the purchase-price depreciation shield is a separate portfolio line discounted at the contracted rate. Breakeven price solves V = P in closed form because the shield is linear in price.",
    ]:
        w("- " + t)
    w("\n## 2. Circularity\n")
    w("There is no circular reference in the Case R model, so no iteration is needed and the workbook runs with iterative calculation off. "
      "The four places where circularity usually appears are handled as follows: (1) sculpted debt is the sum of debt-service capacity times "
      "forward discount-factor products at each year's all-in rate, DF_t = DF_{t-1} / (1 + r_t x f_t), so the debt amount follows directly; "
      "(2) USPP series sizes are solved backward from 2043, P_t = (DS_t - sum of coupons x next-year opening balances) / (1 + coupon of the series amortizing in t), "
      "which needs only later columns; (3) upfront fees, OID and transaction costs are funded by equity as the plug, so debt size does not depend on them; "
      "(4) the bid valuation's tax shield is linear in price, so the breakeven price is closed form, P* = V_pre / (1 - tax rate x PV of depreciation per dollar). "
      "Interest is charged on opening balances, so cash sweeps and taxes do not feed back into interest.\n")

    w("## 3. Asset yield (R-F01, R-F06)\n")
    w("Distribution: annual net energy is normal. One-year sigma^2 = sigma_LT^2 + sigma_IAV^2 and ten-year sigma^2 = sigma_LT^2 + sigma_IAV^2/10, "
      "where sigma_LT is long-term (measurement, model, long-term resource) uncertainty and sigma_IAV inter-annual variability. "
      "The Bible's P90 one-year and ten-year values are the anchors; P99 values follow (z = 1.2816 for P90, 2.3263 for P99). "
      "Wind and solar P50s are net of long-term availability and gross of curtailment; degradation and curtailment apply on top.\n")
    dv = O["diversification"]
    ys = dv["assets"]
    rows = []
    for a in inp["assets"]:
        aid = a["id"]
        if aid in ys:
            y = ys[aid]
            rows.append([aid, a["name"], "%.1f" % a["mw_ac"], "%.1f" % a["p50_gwh"], pct(100 * y["sigma_lt"]), pct(100 * y["sigma_iav"]), pct(100 * y["sigma_1yr"]), pct(100 * y["sigma_10yr"]),
                         pct(y["p90_1yr"]), pct(y["p90_10yr"]), pct(y["p99_1yr"]), pct(y["p99_10yr"]), f1(Sb[aid + ".gen"][yi(2026)]),
                         f2(Sb[aid + ".cap_node"][yi(2026)]), f2(Sb[aid + ".node_price"][yi(2026)])])
    w(table(["Asset", "Name", "MWac", "P50 GWh", "sigma LT", "sigma IAV", "sigma 1-yr", "sigma 10-yr", "P90 1-yr", "P90 10-yr", "P99 1-yr", "P99 10-yr",
             "Net gen 2026 base (GWh)", "Node capture 2026", "Node price 2026 (USD/MWh)"], rows))
    w("\nCorrelations: " + ", ".join("%s %.2f" % (k, v) for k, v in dv["correlations"].items()) + ".\n")
    rows = []
    for grp in ("A1", "all_generation"):
        g = dv[grp]
        for k in ("1yr", "10yr"):
            rows.append([grp, k, f1(g["p50_gwh"]), f1(g["sigma_%s_gwh" % k]), f1(g["p90_%s_gwh" % k]), pct(g["p90_%s_pct" % k]), f1(g["p99_%s_gwh" % k]), pct(g["p99_%s_pct" % k]),
                         pct(g["p90_%s_correlated_pct" % k]), pct(g["p90_%s_independent_pct" % k])])
    w("\nPortfolio yield (correlated):\n")
    w(table(["Group", "Horizon", "P50 GWh", "sigma GWh", "P90 GWh", "P90 % of P50", "P99 GWh", "P99 % of P50", "P90 if fully correlated", "P90 if independent"], rows))
    for sc in ("base", "low"):
        Ss = O["scenarios"][sc]["series"]
        w("\nRevenue build by asset, %s case (USD m, 100%% of asset):\n" % sc)
        rows = []
        for aid in ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]:
            rows.append([aid] + [f1(Ss[aid + ".revenue"][yi(y)]) for y in range(2022, 2031)])
        rows.append(["Portfolio CFADS (Mesa share)"] + [f1(Ss["portfolio.cfads_all"][yi(y)]) for y in range(2022, 2031)])
        w(table(["Asset"] + [str(y) for y in range(2022, 2031)], rows))

    w("\n## 4. Hedge book (R-F02, base)\n")
    rows = []
    for y in range(2022, 2035):
        i = yi(y)
        tot = Sb["portfolio.mesa_rev_all"][i]
        sh = [Sb["portfolio.share_%s_all" % b][i] * 100 for b in ("contracted", "hedged", "merchant")]
        rows.append([y, f1(Sb["R1.settle"][i]), f1(Sb["R3.settle"][i]), f1(Sb["R4.settle"][i]), f1(Sb["R5.settle"][i]),
                     f1(Sb["R6.settle"][i]), f1(Sb["R7.settle"][i]), f1(Sb["R8.settle"][i]), f1(tot)] + ["%.1f%%" % x for x in sh])
    w(table(["Year", "R1 swap settlement", "R3 PRS net", "R4 shape settlement", "R5 vPPA settlement", "R6 toll", "R7 floor contract", "R8 shape settlement",
             "Mesa revenue", "Contracted", "Hedged", "Merchant"], rows))

    w("\n## 5. A1 financing (R-F05)\n")
    su = B["sources_uses"]["A1"]
    w(table(["Uses", "USD m", "Sources", "USD m"], [
        ["Purchase price", f1(su["price"]), "Opco term loan", f1(su["opco_tl"])],
        ["Transaction costs", f1(su["costs"]), "Holdco TLB (face)", f1(su["holdco_tlb"])],
        ["Opco upfront fee", f1(su["opco_fee"]), "Fund equity", f1(su["equity"])],
        ["Holdco OID", f1(su["holdco_oid"]), "", ""],
        ["Total", f1(su["uses"]), "Total", f1(su["opco_tl"] + su["holdco_tlb"] + su["equity"])]]))
    w("\nOpco term loan sizing: PV of debt-service capacity by bucket at the sizing rates: contracted %s, hedged %s, merchant %s; total %s. "
      "The P99 one-year test (1.00x) binds in %d years. Debt %s. Holdco TLB: coverage test %s, cap at 45%% of opco equity value %s (opco equity value %s); "
      "binding: %s; face %s.\n" % (f1(S["tl_pv_cap_contracted"]), f1(S["tl_pv_cap_hedged"]), f1(S["tl_pv_cap_merchant"]), f1(S["tl_pv_cap_bucket_total"]),
                                   S["tl_p99_binds_years"], f1(S["tl_debt"]), f1(S["hc_face_cov"]), f1(S["hc_face_cap"]), f1(S["opco_eq_val_2022"]),
                                   S["hc_binding"], f1(S["hc_face"])))
    rows = [[y, f1(S["tl_cap_bucket"][yi(y)]), f1(S["tl_cap_p99"][yi(y)]), f1(S["tl_ds"][yi(y)]), pct(S["tl_rate"][yi(y)], 3), f1(S["tl_sched_open"][yi(y)])] for y in range(2022, 2041)]
    w(table(["Year", "Bucket capacity", "P99 capacity", "Sculpted DS", "All-in rate", "Opening balance"], rows))
    da = O["debt_by_asset"]
    w("\nOpco debt by asset (pro rata to PV of each asset's own debt-service capacity):\n")
    w(table(["Asset", "Opco TL 2022", "USPP 2025", "Redfern 2023"], [[a, f1(da["opco_tl_2022"].get(a)) if a in da["opco_tl_2022"] else "--",
                                                                      f1(da["uspp_2025"][a]), f1(da["redfern_2023"].get(a)) if a == "R6" else "--"] for a in ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]]))

    w("\n## 6. Valuations (R-F04, R-F07)\n")
    rows = []
    for sc in ("base", "low", "high"):
        v = O["valuations"][sc]["A1"]
        rows.append([sc, f1(v["by_bucket"]["contracted"]), f1(v["by_bucket"]["hedged"]), f1(v["by_bucket"]["merchant"]), f1(v["pre_shield"]),
                     f1(v["shield_at_price"]), f1(v["ev"]), f1(v["price"]), f1(v["npv_vs_price"]), f1(v["breakeven_price"])])
    w(table(["Case", "Contracted", "Hedged", "Merchant", "Value before shield", "Tax shield at price", "Enterprise value", "Price", "Value less price", "Breakeven price"], rows))
    rows = []
    for aid, v in O["valuations"]["base"]["A1"]["by_asset"].items():
        rows.append([aid, f1(v["contracted"]), f1(v["hedged"]), f1(v["merchant"]), f1(v["total"])] +
                    [f1(O["valuations"][sc]["A1"]["by_asset"][aid]["total"]) for sc in ("low", "high")])
    w("\nA1 by asset (base by bucket; totals in low and high):\n")
    w(table(["Asset", "Contracted", "Hedged", "Merchant", "Base total", "Low total", "High total"], rows))
    v2 = O["valuations"]["base"]["A2"]; v3 = O["valuations"]["base"]["A3"]
    w("\nA2 (R6, at 2023-08-31): contracted %s, merchant %s, shield %s, value %s against price %s (breakeven %s). "
      "A3 (at 2024-02-15): R7 %s, R8 %s, ITC transfer proceeds PV %s (nominal %s on credits of %s and %s), shield %s, value %s against price PV %s (nominal %s).\n"
      % (f1(v2["R6"]["contracted"]), f1(v2["R6"]["merchant"]), f1(v2["shield_at_price"]), f1(v2["ev"]), f1(v2["price"]), f1(v2["breakeven_price"]),
         f1(v3["R7"]["total"]), f1(v3["R8"]["total"]), f1(v3["itc_pv"]), f1(v3["itc_proceeds"]), f1(v3["itc7"]), f1(v3["itc8"]),
         f1(v3["shield"]), f1(v3["ev"]), f1(v3["price_pv"]), f1(v3["price_nominal"])))
    for k in ("A2", "A3"):
        s = B["sources_uses"][k]
        w("\n%s sources and uses: %s\n" % (k, ", ".join("%s %s" % (kk, f1(vv)) for kk, vv in s.items())))

    w("\n## 7. 2025 refinancing (R-F08)\n")
    rc = B["refinancing_cash"]
    sz = S["u_series_size"]; sh = S["u_series_share"]
    ser = inp["debt"]["refinancing_2025"]["uspp_notes"]["series"]
    w(table(["Series", "Tenor (years)", "Coupon", "Size", "Share"], [[k, ser[k]["tenor_years"], pct(ser[k]["coupon_pct"], 2), f1(sz[k]), pct(sh[k])] for k in ("A", "B", "C")]
            + [["Total", "", pct(S["u_coupon"], 2) + " (issue-weighted)", f1(S["u_size"]), "100.0%"]]))
    w("\nUSPP P99 test binds in %d years. Uses and proceeds at December 31, 2025:\n" % S["u_p99_binds_years"])
    w(table(["Item", "USD m"], [["USPP proceeds", f1(rc["uspp"])], ["Repay opco term loan", f1(-rc["tl_repay"])], ["Repay Redfern loan", f1(-rc["rf_repay"])],
                                ["Opco swap unwind (receivable)", f1(rc["mtm_opco_receivable"])], ["Redfern swap unwind (payable)", f1(-rc["mtm_redfern_payable"])],
                                ["Transaction costs (1.10%)", f1(-rc["costs"])], ["Net opco proceeds to holdco", f1(rc["opco_net"])],
                                ["Repriced holdco TLB (face)", f1(S["hn_face"])], ["Repay holdco TLB and incremental", f1(-(Sb["finance.hc1_repay"][3] + Sb["finance.hc2_repay"][3]))],
                                ["Holdco OID (0.5%)", f1(-S["hn_face"] * 0.005)],
                                ["Recapitalization distribution to the fund", f1(Sb["finance.recap_total"][3])]]))
    Q = O["scenarios"]["status_quo"]["scalars"]; Bs = B["scalars"]
    w("\nIRR impact (gross, fund level): lifetime IRR %s with the refinancing against %s without (%+.2f points); IRR to December 31, 2025 including NAV %s against %s; "
      "NAV %s against %s; multiple to 2025 %sx against %sx.\n" % (pct(Bs["fund_irr_life_pct"], 2), pct(Q["fund_irr_life_pct"], 2), Bs["fund_irr_life_pct"] - Q["fund_irr_life_pct"],
                                                                  pct(Bs["fund_irr_2025_pct"], 2), pct(Q["fund_irr_2025_pct"], 2), f1(Bs["fund_nav_2025"]), f1(Q["fund_nav_2025"]),
                                                                  f2(Bs["fund_moic_2025_x"]), f2(Q["fund_moic_2025_x"])))
    rows = [[y, f1(Sb["portfolio.cfads_all"][yi(y)]), f1(Sb["finance.u_ds"][yi(y)]), f2(Sb["finance.dscr_u"][yi(y)]), f1(Sb["finance.u_open"][yi(y)]),
             f1(Sb["finance.hc3_open"][yi(y)]), f2(Sb["finance.hc_cov"][yi(y)]), f1(Sb["finance.tax"][yi(y)]), f1(Sb["finance.fund_dist"][yi(y)])] for y in range(2022, 2044)]
    w(table(["Year", "CFADS", "USPP DS", "USPP DSCR", "USPP opening", "Repriced holdco opening", "Holdco coverage", "Cash tax", "Fund distribution"], rows))

    w("\n## 8. Fund returns (R-F09) and scenarios\n")
    rows = []
    for k, sc in O["scenarios"].items():
        s = sc["scalars"]
        rows.append([k, f1(s["cfads_2026"]), f2(s["tl_dscr_min_2022_2025"]), f2(s["uspp_dscr_min_2026_2043"]), f2(s["uspp_dscr_avg_2026_2043"]),
                     f2(s["holdco_cov_min_2023_2031"]), f1(s["fund_contributions"]), f1(s["recap_distribution_2025"]), f1(s["fund_nav_2025"]),
                     pct(s["fund_irr_2025_pct"]), pct(s["fund_irr_life_pct"]), f2(s["fund_moic_life_x"]), s["years_holdco_shortfall"]])
    w(table(["Scenario", "CFADS 2026", "Min TL DSCR 2022-25", "Min USPP DSCR", "Avg USPP DSCR", "Min holdco cover", "Equity in", "Recap 2025", "NAV 2025",
             "IRR to 2025", "Lifetime IRR", "Lifetime multiple", "Years with holdco shortfall"], rows))
    w("\nFund distributions are floored at zero (limited liability); a holdco shortfall year is one in which opco distributions do not cover tax and holdco debt service, which in practice means a default or a negotiated cure. IRR 'n.m.' means the fund does not recover its equity.\n")

    w("\n## 9. Uri-type stress on R1 (R-F03)\n")
    u = O["uri_stress"]
    w(table(["Item", "Value"], [["Event", "72 hours at USD 5,000/MWh; R1 at 15% availability"], ["Swap volume (MWh)", "%.0f" % u["swap_mwh"]],
                                ["R1 generation (MWh)", "%.0f" % u["gen_mwh"]], ["Volume shortfall (MWh)", "%.0f" % u["shortfall_mwh"]],
                                ["Swap settlement paid (USD m)", f1(u["swap_payment"])], ["Physical revenue (USD m)", f1(u["physical_revenue"])],
                                ["Net cash over the event (USD m)", f1(u["net_cash"])],
                                ["Versus normal hedged revenue for the same hours (USD m)", f1(u["net_vs_fully_covered"])]]))

    w("\n## 9a. Batteries and the R7 floor (R-F18, R-F19; Annex TR R.4, R.5)\n")
    w("Overbuild 8%% of nameplate at COD; fade 2.0 points of beginning-of-life energy in year 1, 1.5 a year in years 2 to 10, 1.0 a year after; each augmentation tranche (6%% of nameplate at the start of calendar years COD+5 and COD+9) fades from its own installation. "
      "Usable energy is computed at each period start and end; merchant revenue and the R7 floor reference revenue scale by min(1, average usable energy / nameplate). "
      "R6 lowest usable energy in the toll term: %s MWh (requirement 200 MWh; condition holds).\n" % f1(O["battery_check"]["r6_min_usable_in_toll_term_mwh"]))
    rows = []
    for y in range(2023, 2036):
        i = yi(y)
        rows.append([y] + [f1(Sb["%s.%s" % (a, f)][i]) for a in ("R6", "R7") for f in ("bat_usable_end", "bat_aug_mwh", "aug")] + [f2(Sb["R6.bat_scale"][i]), f2(Sb["R7.bat_scale"][i])])
    w(table(["Year", "R6 usable end (MWh)", "R6 augmentation (MWh)", "R6 augmentation cost", "R7 usable end (MWh)", "R7 augmentation (MWh)", "R7 augmentation cost", "R6 scale", "R7 scale"], rows))
    rows = []
    for sc in ("base", "low", "high"):
        Ss = O["scenarios"][sc]["series"]
        for y in range(2024, 2033):
            i = yi(y)
            rows.append([sc, y, f2(Ss["R7.floor_ref"][i]), f1(Ss["R7.floor_payment"][i]), f1(Ss["R7.floor_premium"][i]), f1(Ss["R7.floor_upside"][i]), f1(Ss["R7.floor_net"][i])])
    w("\nR7 revenue floor by calendar year (contract years April to April, pro rata):\n")
    w(table(["Case", "Year", "Reference revenue (USD/kW-yr)", "Floor payment", "Premium", "Upside share", "Net"], rows))
    va2 = O["valuations"]["base"]["A2"]; va3 = O["valuations"]["base"]["A3"]
    w("\nMateriality against D-014 prices (threshold USD 1.0 million): A2 breakeven %s against price %s (%s below); A3 value %s against price PV %s (%s short). Prices unchanged per D-014.\n"
      % (f1(va2["breakeven_price"]), f1(va2["price"]), f1(va2["price"] - va2["breakeven_price"]), f1(va3["ev"]), f1(va3["price_pv"]), f1(va3["price_pv"] - va3["ev"])))

    w("\n## 10. Decommissioning (R-F10)\n")
    rows = [[a, d["retirement"], "%.0f" % d["usd_per_kw_2022"], f1(d["cost_2022_prices"]), f1(d["bonded_amount_2026"]), "%.3f" % d["bond_cost_2026"],
             f1(d["cost_nominal_at_retirement"])] for a, d in O["decommissioning"].items()]
    w(table(["Asset", "Retirement", "USD/kW (2022)", "Cost, 2022 prices", "Bonded amount 2026", "Bond cost 2026", "Nominal cost at retirement"], rows))

    w("\n## 11. Design ranges against outputs\n")
    w(table(["Item", "v1.0 design range", "Model"], [["Opco term loan 2022", "520-600", f1(S["tl_debt"])], ["Holdco TLB 2022", "160-210", f1(S["hc_face"])],
                                                    ["USPP 2025", "750-860", f1(S["u_size"])], ["Fund net IRR target", "11-13% (net)", "gross lifetime " + pct(Bs["fund_irr_life_pct"])]]))
    w("\nRanges were superseded with the price calibration (R-C08); the debt amounts follow from the Bible's revenue inputs and are reported to the editor-in-chief.\n")

    w("\n## 12. Checks\n")
    fails = [c for c in O["checks"] if not c["pass"]]
    w("%d checks run, %d failed.\n" % (len(O["checks"]), len(fails)))
    w(table(["Check", "Value", "Pass"], [[c["check"], "%.2e" % c["value"], "yes" if c["pass"] else "NO"] for c in O["checks"] if "[" not in c["check"] or c["check"].startswith("[base]")]))
    open(path, "w").write("\n".join(L))
