"""Write model/figure-ledger-case-t.md from model/outputs_case_t.json only (no computation beyond
selecting and formatting values). Run after case_t.py."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
O = json.load(open(os.path.join(HERE, "outputs_case_t.json")))
D = O["derived"]
R = O["runs"]
VER = "Case T model v1.0"


def m(x):
    return f"{x:,.1f}"


def x2(x):
    return f"{x:.2f}x"


def pc(x, n=1):
    return f"{100 * x:.{n}f}%"


rows = []


def add(fid, item, value, unit, scen, asof):
    rows.append((fid, item, value, unit, scen, asof))


# ---------------------------------------------------------------- T-F01
p = O["psc"]
for k, lab in (("raw_capex", "Raw capital cost"), ("om_and_lifecycle", "O&M and lifecycle"),
               ("toll_revenue_retained", "Toll revenue retained by the state"),
               ("construction_risk", "Construction risk"), ("traffic_revenue_risk", "Traffic revenue risk"),
               ("operating_risk", "Operating risk"), ("competitive_neutrality", "Competitive neutrality")):
    add("T-F01", f"PSC: {lab}", m(p["psc_items"][k]), "ARD m, PV at 2012-12-31 (6.85%)", "PSC (inputs)", "2012-11-08")
add("T-F01", "Raw PSC (capital + O&M - retained tolls)", m(p["psc_raw"]), "ARD m, PV 2012", "PSC", "2012-11-08")
add("T-F01", "Risk adjustments plus competitive neutrality", m(p["psc_total"] - p["psc_raw"]), "ARD m, PV 2012", "PSC", "2012-11-08")
add("T-F01", "Risk-adjusted PSC", m(p["psc_total"]), "ARD m, PV 2012", "PSC", "2012-11-08")
add("T-F01", "Discount factor 2019-03-31 to 2012-12-31", f"{p['discount_factor']:.4f}", "factor", "PSC", "2012-11-08")
add("T-F01", "PV of reference contribution (ARD 410.0 m)", m(p["pv_contribution_reference"]), "ARD m, PV 2012", "PSC", "2012-11-08")
add("T-F01", "Retained risks plus contract management", m(p["retained_risks"] + p["contract_management"]), "ARD m, PV 2012", "PSC", "2012-11-08")
add("T-F01", "PPP reference project cost", m(p["ppp_reference_total"]), "ARD m, PV 2012", "PSC", "2012-11-08")
add("T-F01", "Value for money, reference", m(p["vfm_reference"]), "ARD m, PV 2012", "PSC", "2012-11-08")
add("T-F01", "Value for money, reference, share of risk-adjusted PSC", pc(p["vfm_reference_pct"]), "%", "PSC", "2012-11-08")
add("T-F01", "PV of winning contribution (ARD 287.4 m)", m(p["pv_contribution_bid"]), "ARD m, PV 2012", "PSC", "2014-09-23")
add("T-F01", "PPP cost at the winning bid", m(p["ppp_bid_total"]), "ARD m, PV 2012", "PSC", "2014-09-23")
add("T-F01", "Value for money, winning bid", m(p["vfm_bid"]), "ARD m, PV 2012", "PSC", "2014-09-23")
add("T-F01", "Value for money, winning bid, share of risk-adjusted PSC", pc(p["vfm_bid_pct"]), "%", "PSC", "2014-09-23")
# ---------------------------------------------------------------- T-F02
b = D["bid"]
add("T-F02", "Equity IRR, bid base (Pellow), contribution ARD 287.4 m", pc(b["equity_irr_bid_base"], 1), "% nominal post-tax", "Bid base (1)", "2014-08-15")
add("T-F02", "Equity NPV at 11.4% at financial close, bid base", m(b["npv_bid_base_at_11.4"]), "ARD m", "Bid base (1)", "2015-05-27")
add("T-F02", "Equity IRR, banking case at ARD 287.4 m", pc(b["equity_irr_banking"], 1), "%", "Banking (2)", "2015-05-27")
add("T-F02", "Equity NPV at 11.4%, banking case", m(b["npv_banking_at_11.4"]), "ARD m", "Banking (2)", "2015-05-27")
add("T-F02", "Equity IRR, downside at ARD 287.4 m", pc(b["equity_irr_downside"], 1), "%", "Downside (3)", "2015-05-27")
add("T-F02", "Contribution needed for 11.4% on the banking case", m(b["contribution_needed_banking"]), "ARD m (paid at opening)", "Banking (2), contribution solved", "2014-08-15")
add("T-F02", "Contribution needed for 11.4% on the bid base", m(b["contribution_needed_bid_base"]), "ARD m", "Bid base (1), financing re-sized on banking", "2014-08-15")
add("T-F02", "Project IRR post-tax, bid base", pc(b["project_irr_bid_base"], 1), "%", "Bid base (1)", "2015-05-27")
add("T-F02", "Project IRR post-tax, banking", pc(b["project_irr_banking"], 1), "%", "Banking (2)", "2015-05-27")
add("T-F02", "Project IRR pre-tax, bid base", pc(b["project_irr_pretax_bid_base"], 1), "%", "Bid base (1)", "2015-05-27")
# ---------------------------------------------------------------- T-F03
su = D["sources_uses"]
labels = {"dc_contract": "D&C contract (incl. tolling system and 5% retention)", "development": "Development and bid costs",
          "spv_costs": "Project company costs", "insurance": "Insurance during construction", "certifier": "Independent certifier",
          "advisors": "Lenders' advisors and legal", "contingency": "Contingency", "bank_interest": "Bank interest during construction",
          "bank_commitment_fees": "Bank commitment fees", "bond_interest": "Bond interest during construction",
          "escrow_income": "Bond escrow earnings (deducted)", "bridge_interest": "Contribution bridge interest",
          "upfront_fees": "Upfront fees", "dsra_initial": "DSRA initial funding", "ramp_up_interest_account": "Ramp-up interest account"}
for k, v in su["uses"].items():
    add("T-F03", f"Use: {labels[k]}", m(v), "ARD m", "Banking (2) = financing at close", "2015-05-27")
add("T-F03", "Total uses (eligible costs)", m(su["total_uses"]), "ARD m", "Banking (2)", "2015-05-27")
slab = {"equity": "Equity", "senior_bank": "Bank mini-perm", "senior_bonds": "Brannock Infrastructure Revenue Bonds",
        "nilo": "NILO loan", "state_contribution_via_bridge": "State contribution (via the bridge)"}
for k, v in su["sources"].items():
    add("T-F03", f"Source: {slab[k]}", m(v), "ARD m", "Banking (2)", "2015-05-27")
add("T-F03", "Senior debt (bank plus bonds)", m(su["sources"]["senior_bank"] + su["sources"]["senior_bonds"]), "ARD m", "Banking (2)", "2015-05-27")
add("T-F03", "Funding requirement net of the contribution", m(su["funding_requirement_net"]), "ARD m", "Banking (2)", "2015-05-27")
add("T-F03", "Senior share of funding net of contribution", pc(su["senior_pct_net"]), "%", "Banking (2)", "2015-05-27")
add("T-F03", "NILO share of funding net of contribution", pc(su["nilo_pct_net"]), "%", "Banking (2)", "2015-05-27")
add("T-F03", "Equity share of funding net of contribution", pc(su["equity_pct_net"]), "%", "Banking (2)", "2015-05-27")
add("T-F03", "NILO share of eligible costs (cap 33%)", pc(su["nilo_pct_eligible"]), "%", "Banking (2)", "2015-05-27")
add("T-F03", "Equity: share capital", m(su["share_capital"]), "ARD m", "Banking (2)", "2015-05-27")
add("T-F03", "Equity: shareholder loans (10.25%)", m(su["shareholder_loans"]), "ARD m", "Banking (2)", "2015-05-27")
add("T-F03", "IDC: senior interest net of escrow earnings plus bridge interest", m(su["idc_total"]), "ARD m", "Banking (2)", "2019-03-31")
add("T-F03", "Financing costs incl. commitment and upfront fees", m(su["financing_costs_total"]), "ARD m", "Banking (2)", "2019-03-31")
for k, lab in (("bank_upfront", "Bank upfront fee 1.85%"), ("bond_issue", "Bond issue costs 1.20%"),
               ("nilo_application", "NILO application fee 0.10%"), ("bridge_upfront", "Bridge upfront fee 1.00%")):
    add("T-F03", lab, m(su["fees_breakdown"][k]), "ARD m", "Banking (2)", "2015-05-27")
add("T-F03", "NILO interest capitalized during construction", m(su["nilo_capitalized_interest_construction"]), "ARD m", "Banking (2)", "2019-03-31")
add("T-F03", "NILO balance at completion", m(su["nilo_balance_at_completion"]), "ARD m", "Banking (2)", "2019-03-31")
add("T-F03", "NILO balance at 2023-12-31 (banking schedule, before the final capitalized quarter)", m(su["nilo_balance_2024_03_31_start_of_2024H1"]), "ARD m", "Banking (2)", "2023-12-31")
add("T-F03", "Shareholder-loan interest accrued during construction", m(su["shl_interest_capitalized_construction"]), "ARD m", "Banking (2)", "2019-03-31")
add("T-F03", "Contribution Bridge Facility (drawn 2017Q4-2019Q1, repaid at opening)", m(su["sources"]["state_contribution_via_bridge"]), "ARD m", "Banking (2)", "2019-03-31")
# ---------------------------------------------------------------- T-F04 traffic
ta = D["traffic_annual"]
for y in range(2019, 2027):
    ys = str(y)
    vals = "; ".join(f"{n} {ta[k][ys]:.1f}" for k, n in (("pellow", "Pellow"), ("ridgeway", "Ridgeway"), ("downside", "downside"), ("actual", "actual")) if ys in ta[k])
    add("T-F04", f"Average daily trips {y}", vals, "thousand trips/day (2019: average over operating days)", "Inputs via runs 1, 2, 3, 4", f"{y}-12-31")
# ---------------------------------------------------------------- T-F05 tolls
tt = D["tolls"]
for y in range(2015, 2031):
    ys = str(y)
    o, r_ = tt["original"][ys], tt["restructured"][ys]
    add("T-F05", f"Toll per km from July 1, {y}: original car / LCV / HV", f"{o['car']:.4f} / {o['light_commercial']:.4f} / {o['heavy_vehicle']:.4f}", "ARD per km (nominal)", "Inputs plus actual CPI", f"{y}-07-01")
    if y >= 2024:
        add("T-F05", f"Toll per km from July 1, {y}: restructured car / LCV / HV", f"{r_['car']:.4f} / {r_['light_commercial']:.4f} / {r_['heavy_vehicle']:.4f}", "ARD per km (nominal)", "Inputs plus actual CPI", f"{y}-07-01")
# ---------------------------------------------------------------- T-F06 revenue
ra = D["revenue_annual"]
for y in range(2019, 2026):
    ys = str(y)
    add("T-F06", f"Net toll revenue {y}: bid base / banking / actual",
        f"{m(ra['bid_base'][ys])} / {m(ra['banking'][ys])} / {m(ra['actual'][ys])} (actual {pc(ra['actual'][ys] / ra['bid_base'][ys] - 1)} vs bid base)",
        "ARD m (2019 from opening)", "Runs 1, 2, 4", f"{y}-12-31")
# ---------------------------------------------------------------- T-F07 DSCR history
for k, v in D["dscr_history"].items():
    add("T-F07", f"Senior DSCR {k}: actual covenant (historic) / period / banking projection",
        f"{x2(v['actual_hist_12m'])} / {x2(v['actual_period'])} / {x2(v['banking_hist_12m'])}",
        "x", "Actual history (4) vs banking (2)", k.replace("H1", "-06-30").replace("H2", "-12-31"))
    add("T-F07", f"{k}: CFADS / scheduled DS / DSRA / lock-up / event of default",
        f"{m(v['actual_cfads'])} / {m(v['actual_ds_sched'])} / {m(v['dsra_close'])} / {int(v['lockup'])} / {int(v['eod'])}",
        "ARD m; flags", "Actual history (4)", k.replace("H1", "-06-30").replace("H2", "-12-31"))
# ---------------------------------------------------------------- T-F08
t8 = D["termination_2022"]
for k, lab, f in (("senior_principal", "Senior principal outstanding", m), ("senior_arrears", "Senior interest arrears", m),
                  ("senior_claims", "Senior claims", m), ("nilo_outstanding", "NILO outstanding (incl. capitalized interest)", m),
                  ("equity_contributed", "Equity contributed incl. 2021 support", m), ("equity_distributions", "Distributions received", m),
                  ("authority_default_equity_npv", "Authority default: equity compensation (NPV of bid-base distributions at 11.4%)", m),
                  ("authority_default_total", "Authority default or voluntary termination: total (before swap breakage)", m),
                  ("fm_total", "Prolonged force majeure: total", m),
                  ("fair_value", "Concessionaire default: estimated fair value (pre-tax 9.0%)", m),
                  ("retender_costs", "Retendering costs", m),
                  ("concessionaire_default_comp", "Concessionaire default: compensation", m),
                  ("cd_senior_recovery_nilo_pari_passu", "Senior recovery if NILO's springing lien ranks pari passu", pc),
                  ("cd_senior_recovery_nilo_subordinated", "Senior recovery if NILO stays subordinated", pc),
                  ("cd_nilo_recovery_subordinated", "NILO recovery if subordinated", pc)):
    add("T-F08", lab, f(t8[k]), "ARD m" if f is m else "%", "Actual history (4); bid base (1); retender (6)", "2022-06-30")
# ---------------------------------------------------------------- T-F09
r = D["restructuring"]
items = [("bank_principal", "Bank principal", m), ("bond_principal", "Bond principal", m), ("accrued_interest", "Accrued unpaid senior interest", m),
         ("claims_gross", "Senior claims, gross", m), ("swap_mtm", "Swap termination value set off (4.36% vs 3.48%)", m),
         ("claims_net", "Senior claims, net", m), ("bank_claim_net", "Bank claim, net of set-off", m), ("bond_claim_net", "Bondholder claim", m),
         ("cancelled", "Cancelled (14 points)", m), ("conv_eq", "Converted to equity (10 points)", m),
         ("notes_issue", "Restructured Senior Notes (76%)", m), ("notes_market_value", "Notes value at a 7.50% market yield", m),
         ("notes_price_pct", "Notes price", pc), ("equity_value_total", "New equity value at 14.0%", m),
         ("warrant_value", "Warrants (3%, original sponsors)", m), ("equity_value_creditors", "Equity value to senior creditors (85%)", m),
         ("equity_value_state", "Equity value to the state (15%)", m), ("state_capital_grant_implied", "State money above plan value (implied capital grant)", m),
         ("senior_recovery_pct_net_claims", "Senior recovery (notes at market, equity at plan value)", pc),
         ("senior_recovery_pct_at_par", "Senior recovery with notes at par", pc),
         ("bank_recovery_pct", "Bank recovery", pc), ("bond_recovery_pct", "Bondholder recovery", pc),
         ("nilo_claim", "NILO claim (no write-down)", m), ("nilo_pv_at_3.06", "PV of NILO receipts at 3.06%", m),
         ("nilo_recovery_pv_pct", "NILO recovery in PV terms", pc), ("nilo_final_payment", "NILO final payment", str),
         ("original_equity_invested", "Original equity invested incl. support", m), ("shl_written_off", "Shareholder loans written off (incl. accrued interest)", m),
         ("original_equity_warrants", "Value of warrants to original sponsors", m), ("notes_s", "Notes sculpting divisor", lambda v: f"{v:.2f}x"),
         ("dsra_2023", "DSRA balance at 2023-12-31 (before state top-up)", m)]
for k, lab, f in items:
    add("T-F09", lab, f(r[k]), "ARD m" if f is m else ("%" if f is pc else ""), "Restructuring case (5)", "2023-12-31")
add("T-F09", "Pre-restructuring capital structure (bank / bonds / arrears / NILO / shareholder loans)",
    " / ".join(m(r["pre_structure"][k]) for k in ("bank", "bonds", "accrued_senior_interest", "nilo", "shareholder_loans")), "ARD m", "Restructuring case (5)", "2023-12-31")
add("T-F09", "Post-restructuring capital structure (notes / NILO / equity from conversion / state equity money)",
    " / ".join(m(r["post_structure"][k]) for k in ("restructured_notes", "nilo", "new_equity_conversion", "new_equity_state")), "ARD m", "Restructuring case (5)", "2023-12-31")
add("T-F09", "Price per 1% of new equity: plan value / state / creditors' converted claims",
    f"{r['plan_value_per_1pct']:.2f} / {r['state_price_per_1pct']:.2f} / {r['creditor_conversion_per_1pct']:.2f}", "ARD m per 1%", "Restructuring case (5)", "2023-12-31")
# ---------------------------------------------------------------- T-F10
pr = D["post_restructuring"]
add("T-F10", "Minimum notes DSCR (2024-2052)", x2(pr["min_notes_dscr"]), "x", "Ridgeway 2023 case (5)", "2023-12-31")
add("T-F10", "Average notes DSCR", x2(pr["avg_notes_dscr"]), "x", "Ridgeway 2023 case (5)", "2023-12-31")
for k in ("2024H1", "2024H2", "2025H2", "2027H2", "2030H2", "2035H2", "2040H2", "2045H2"):
    if k in pr["notes_dscr_by_period"]:
        add("T-F10", f"Notes DSCR {k}", x2(pr["notes_dscr_by_period"][k]), "x", "Ridgeway 2023 case (5)", "2023-12-31")
for k in ("2024H2", "2026H2", "2028H2", "2030H2", "2035H2", "2040H2", "2045H2"):
    if k in pr["notes_balance"]:
        add("T-F10", f"Notes balance at end {k}", m(pr["notes_balance"][k]), "ARD m", "Ridgeway 2023 case (5)", "2023-12-31")
add("T-F10", "Notes fully repaid (with 50% sweep to 2030)", r["notes_repaid_from"], "date", "Ridgeway 2023 case (5)", "2023-12-31")
add("T-F10", "Cash swept to noteholders 2024-2030", m(pr["sweep_total"]), "ARD m", "Ridgeway 2023 case (5)", "2023-12-31")
add("T-F10", "New equity value at 14.0%", m(pr["equity_value_total"]), "ARD m", "Ridgeway 2023 case (5)", "2023-12-31")
add("T-F10", "First distribution to new equity", pr["first_distribution"], "date", "Ridgeway 2023 case (5)", "2023-12-31")
add("T-F10", "State revenue share paid (whole extended term)", m(pr["revshare_total_nominal"]), "ARD m nominal", "Ridgeway 2023 case (5)", "2023-12-31")
add("T-F10", "2030 toll revenue as share of the revenue-share threshold", pc(pr["revenue_threshold_ratio_2030"]), "%", "Ridgeway 2023 case (5)", "2023-12-31")
add("T-F10", "2058 toll revenue as share of the revenue-share threshold", pc(pr["revenue_threshold_ratio_2058"]), "%", "Ridgeway 2023 case (5)", "2023-12-31")
add("T-F10", "NILO restructured sculpting divisor", f"{r['nilo_r_k']:.2f}x", "x", "Ridgeway 2023 case (5)", "2023-12-31")
# ---------------------------------------------------------------- new figures T-F11 onward
cand = su["sizing_candidates"]
names = {"gearing": "55% gearing cap", "dscr_sculpt": "Sculpted at 1.50x (PV of CFADS / 1.50)", "llcr": "LLCR 1.55x",
         "interest_cover": "Interest cover 1.50x in every repayment period", "downside": "Downside interest cover 1.15x"}
for k, v in cand.items():
    add("T-F11", f"Senior capacity: {names[k]}", m(v), "ARD m", "Banking (2)", "2015-05-27")
add("T-F11", "Binding sizing constraint", names[su["binding_constraint"]], "", "Banking (2)", "2015-05-27")
add("T-F11", "Senior sculpting divisor s (DS = max(interest, CFADS/s))", f"{su['sculpt_s']:.2f}x", "x", "Banking (2)", "2015-05-27")
add("T-F11", "NILO sculpting divisor k", f"{su['nilo_k']:.2f}x", "x", "Banking (2)", "2015-05-27")
for nm, key in (("Bid base", "bid_base_metrics"), ("Banking", "banking_metrics"), ("Downside", "downside_metrics")):
    mt = D[key]
    add("T-F12", f"{nm}: min / average senior DSCR (2021-2048)", f"{x2(mt['min_dscr_rep'])} / {x2(mt['avg_dscr_rep'])}", "x", nm, "2015-05-27")
    add("T-F12", f"{nm}: min ramp-up DSCR (2019-2020, net of ramp-up account)", x2(mt["min_dscr_rampup"]), "x", nm, "2015-05-27")
    add("T-F12", f"{nm}: min senior plus NILO DSCR", x2(mt["min_comb_dscr"]), "x", nm, "2015-05-27")
    add("T-F12", f"{nm}: LLCR at first repayment", x2(mt["llcr_first"]), "x", nm, "2015-05-27")
bm = D["banking_metrics"]
add("T-F12", "Banking: PLCR at first repayment", x2(bm["plcr_first"]), "x", "Banking (2)", "2015-05-27")
add("T-F12", "Downside: lock-up periods after first repayment", str(D["downside_metrics"]["lockup_periods"]), "periods", "Downside (3)", "2015-05-27")
for k, v in D["sensitivities"].items():
    add("T-F13", f"{k}: equity IRR / NPV at 11.4% / min DSCR", f"{pc(v['equity_irr'])} / {m(v['npv_11.4'])} / {x2(v['min_dscr'])}", "% / ARD m / x", "Bid base, financing locked", "2014-08-15")
for y, v in D["balances_banking"].items():
    add("T-F14", f"Scheduled balances at end {y}: senior / NILO", f"{m(v['senior'])} / {m(v['nilo'])}", "ARD m", "Banking (2)", "2015-05-27")
a = D["actual"]
add("T-F15", "Original sponsors: equity invested incl. 2021 support", m(r["original_equity_invested"]), "ARD m", "Actual history (4)", "2023-12-31")
add("T-F15", "Original sponsors: distributions received 2019-2023", m(r["original_equity_distributions"]), "ARD m", "Actual history (4)", "2023-12-31")
add("T-F15", "First event of default (historic DSCR below 1.05x)", a["eod_first"], "period", "Actual history (4)", "2020-12-31")
add("T-F15", "DSRA drawn in total 2019-2023", m(a["dsra_draws"]), "ARD m", "Actual history (4)", "2023-12-31")
add("T-F15", "2019 traffic against the bid base", pc(a["traffic_2019_vs_base_pct"]), "%", "Inputs", "2019-12-31")
add("T-F16", "Tax losses before forgiveness at 2023-12-31", m(r["losses_before_forgiveness"]), "ARD m", "Restructuring case (5)", "2023-12-31")
add("T-F16", "Forgiveness applied to losses / to the asset's cost base", f"{m(r['forgiveness_to_losses'])} / {m(r['forgiveness_to_cost_base'])}", "ARD m", "Restructuring case (5)", "2023-12-31")
u = D["usd"]
add("T-F17", "USD equivalents at close (0.76): total uses / senior / NILO / equity",
    f"{m(u['total_uses_2015'])} / {m(u['senior_2015'])} / {m(u['nilo_2015'])} / {m(u['equity_2015'])}", "USD m (illustrative)", "Banking (2)", "2015-05-27")
add("T-F17", "USD equivalents at 2023 (0.67): net senior claims / notes / state money",
    f"{m(u['claims_net_2023'])} / {m(u['notes_2023'])} / {m(u['state_money_2023'])}", "USD m (illustrative)", "Restructuring case (5)", "2023-12-31")

L = ["# Figure ledger: Case T (Merrick Link)\n",
     f"Source: `model/outputs_case_t.json`, produced by `model/case_t.py` ({VER}, story as of 2026-10-03). Every value below is read "
     "from that file and only formatted here (`model/ledger_t.py`). Amounts in ARD millions, nominal, unless stated. "
     "Scenario numbers refer to the workbook scenario switch: 1 bid base, 2 banking, 3 downside, 4 actual history, "
     "5 restructuring case, 6 retender valuation. Writers cite the ID; when a chapter needs a figure that is not here, "
     "report it to the editor-in-chief.\n",
     "Figure IDs T-F01 to T-F10 are those of the Case Bible figure register; T-F11 to T-F17 are new (added by the modeler).\n",
     "| ID | Figure | Value | Units | Model run (scenario) | As-of story date |", "|---|---|---|---|---|---|"]
for fid, item, val, unit, scen, asof in rows:
    L.append(f"| {fid} | {item} | {val} | {unit} | {scen} | {asof} |")
L += ["", "New figure IDs:", "",
      "- T-F11 Senior sizing: capacity under each constraint, binding constraint, sculpting divisors (Chapters 58, 64).",
      "- T-F12 Ratio summary for the bid base, banking and downside runs (Chapters 47, 58, 64).",
      "- T-F13 Sensitivities on the bid base (Chapters 47, 79).",
      "- T-F14 Scheduled senior and NILO balances on the financing at close (Chapters 29, 58).",
      "- T-F15 Outturn: equity invested and lost, first event of default, DSRA use (Chapters 64, 79).",
      "- T-F16 Tax at the restructuring: losses and forgiveness (Chapter 64).",
      "- T-F17 Illustrative USD equivalents (Chapters 58, 64).", ""]
open(os.path.join(HERE, "figure-ledger-case-t.md"), "w").write("\n".join(L))
print(len(rows), "ledger rows")
