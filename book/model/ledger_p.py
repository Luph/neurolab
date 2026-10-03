#!/usr/bin/env python3
"""Formats model/figure-ledger-case-p.md from model/outputs_case_p.json (no computation here)."""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
o = json.load(open(os.path.join(H, 'outputs_case_p.json')))
P = o['figures']; S = o['summary']; Z = o['sizing']
rows = []
def m(x): return f"{x:,.1f}"
def m2(x): return f"{x:,.2f}"
def r(x): return f"{x:.2f}x"
def p1(x): return f"{x * 100:.1f}%"
def add(i, fig, val, unit, run, d):
    rows.append((i, fig, val, unit, run, d))

FCB, FCK, FCD, ACT, RF = 'FC base (1)', 'FC banking (2)', 'FC downside (3)', 'Actual history (15)', 'COD re-forecast (14)'
FC = '2018-07-17'

# P-F01
f = P['P-F01']
add('P-F01', 'Development budget approved 2015', m2(f['budget_2015']), 'USD m', 'Inputs', '2015-09')
for y, v in f['actual_by_year'].items(): add('P-F01', f'Development costs incurred {y}', m2(v), 'USD m', 'Inputs', FC)
add('P-F01', 'Development costs to financial close', m2(f['actual_total']), 'USD m', 'Inputs', FC)
add('P-F01', 'Overrun against the 2015 budget', m2(f['overrun_vs_budget']), 'USD m', 'Inputs', FC)
# P-F02
f = P['P-F02']
add('P-F02', 'US CPI index reading for the January 2022 reset (September 2021; Nov 2016 = 100)', f"{f['us_cpi_index']:.2f}", 'index', ACT, '2022-01-01')
add('P-F02', 'Kessara CPI index reading (September 2021; Nov 2016 = 100)', f"{f['kessara_cpi_index']:.2f}", 'index', ACT, '2022-01-01')
add('P-F02', 'FX used to reconvert local shares (2022H1 average)', f"{f['fx_for_reconversion_kcr_per_usd']:.1f}", 'KCR/USD', ACT, '2022-01-01')
add('P-F02', 'Contracted capacity applying in January 2022 (reset at completion tests)', '581.9', 'MW', ACT, '2022-01-01')
add('P-F02', 'Capital charge, indexed (base 14.36)', f"{f['capital_charge_indexed']:.2f}", 'USD/kW-month', ACT, '2022-01-01')
add('P-F02', 'Fixed O&M charge, indexed (base 2.31)', f"{f['fixed_om_charge_indexed']:.2f}", 'USD/kW-month', ACT, '2022-01-01')
add('P-F02', 'Total capacity charge, nominal', f"{f['capacity_charge_total_indexed']:.2f}", 'USD/kW-month', ACT, '2022-01-01')
add('P-F02', 'Total capacity charge in November 2016 dollars (real)', f"{f['capacity_charge_real_nov2016_usd']:.2f}", 'USD/kW-month', ACT, '2022-01-01')
add('P-F02', 'VOM charge, indexed (base 3.86)', f"{f['vom_charge_indexed']:.2f}", 'USD/MWh', ACT, '2022-01-01')
add('P-F02', 'VOM charge in November 2016 dollars (real)', f"{f['vom_real_nov2016_usd']:.2f}", 'USD/MWh', ACT, '2022-01-01')
# P-F03
f = P['P-F03']
add('P-F03', '6M USD LIBOR, July 2016 (approximate; fact-check)', f"{f['libor_6m_july_2016_pct']:.2f}%", '%', 'Annex 4.7 inputs', '2016-07')
for k, v in f['margins_2016_pct'].items(): add('P-F03', f'Indicative 2016 margin, {k}', f"{v:.2f}%", '%', 'Annex 4.7 inputs', '2016-07')
for k, v in f['all_in_pct'].items(): add('P-F03', f'Indicative all-in floating cost, {k} (LIBOR + margin + upfront fee over 7.0 years' + (' + ECA premium 11.5% over 7.0 years' if k == 'ECA' else '') + ')', f"{v:.2f}%", '% pa', 'Annex 4.7 inputs plus calculation', '2016-07')
add('P-F03', 'Commercial tranche incl. PRI premium and WHT gross-up', f"{f['commercial_all_in_with_pri_and_grossup_pct']:.2f}%", '% pa', 'Annex 4.7 inputs plus calculation', '2016-07')
add('P-F03', 'Indicative weighted all-in floating cost (30/22/10/38)', f"{f['weighted_pct']:.2f}%", '% pa', 'Annex 4.7 inputs plus calculation', '2016-07')
# P-F04
f = P['P-F04']
for k, v in f['income_statement'].items(): add('P-F04', 'FY2022 income statement: ' + k.replace('_', ' '), m(v), 'USD m', ACT, '2022-12-31')
for k, v in f['cash_flow'].items(): add('P-F04', 'FY2022 cash flow: ' + k.replace('_', ' '), m(v), 'USD m', ACT, '2022-12-31')
for k, v in f['balance_sheet'].items():
    if k != 'date': add('P-F04', 'Balance sheet at 2022-12-31: ' + k.replace('_', ' '), m(v), 'USD m', ACT, '2022-12-31')
add('P-F04', 'Financing costs capitalized during construction (IDC, fees, ECA premium, VAT interest)', m(f['capitalized_idc_and_financing_costs']), 'USD m', ACT, '2021-12-01')
add('P-F04', 'Shareholder-loan interest capitalized to COD', m(f['capitalized_shl_interest']), 'USD m', ACT, '2021-12-01')
# P-F05
for g, v in P['P-F05']['by_gearing'].items():
    add('P-F05', f'Equity IRR at {g} gearing', p1(v['equity_irr']), '% nominal post-tax', FCB + ', debt set at gearing', '2017')
    add('P-F05', f'Senior debt at {g} gearing', m(v['senior_debt']), 'USD m', FCB, '2017')
    add('P-F05', f'Minimum DSCR at {g} gearing', r(v['min_dscr']), 'x', FCB, '2017')
# P-F06
f = P['P-F06']
add('P-F06', 'Levelized tariff of the winning bid (RFP formula)', m2(f['levelized_tariff_usd_per_mwh']), 'USD/MWh (2016 prices)', 'FC base inputs', '2016-09-27')
add('P-F06', 'of which capacity', m2(f['capacity_component']), 'USD/MWh', 'FC base inputs', '2016-09-27')
add('P-F06', 'of which VOM', m2(f['vom_component']), 'USD/MWh', 'FC base inputs', '2016-09-27')
add('P-F06', 'of which fuel', m2(f['fuel_component']), 'USD/MWh', 'FC base inputs', '2016-09-27')
add('P-F06', 'Runner-up levelized tariff (4.6% higher)', m2(f['runner_up_usd_per_mwh']), 'USD/MWh', 'FC base inputs', '2016-09-27')
# P-F07
f = P['P-F07']
for k, v in f['uses'].items(): add('P-F07', 'Use: ' + k.replace('_', ' '), m2(v), 'USD m', FCB, FC)
for k, v in f['sources'].items(): add('P-F07', 'Source: ' + k.replace('_', ' '), m2(v), 'USD m', FCB, FC)
add('P-F07', 'Gearing (senior debt / total funding requirement)', p1(f['gearing']), '%', FCB, FC)
add('P-F07', 'Shareholder-loan interest capitalized to COD (non-cash)', m(f['shl_interest_capitalized_to_cod']), 'USD m', FCB, FC)
add('P-F07', 'Shareholder-loan balance at COD', m(f['shl_balance_at_cod']), 'USD m', FCB, FC)
# P-F08
f = P['P-F08']
for k, v in f['senior_debt_by_tranche'].items(): add('P-F08', f'Senior debt, {k} tranche', m(v), 'USD m', FCB, FC)
add('P-F08', 'Senior debt, total', m(f['senior_debt']), 'USD m', FCB, FC)
add('P-F08', 'Binding constraint', f['binding_constraint'] + ' (1.35x)', 'text', FCB, FC)
add('P-F08', 'Debt at the 75% gearing cap', m(f['gearing_cap_debt']), 'USD m', FCB, FC)
add('P-F08', 'Debt capacity at 1.35x', m(f['candidates']['DSCR']), 'USD m', FCB, FC)
add('P-F08', 'Debt meeting the 1.20x downside', m(f['candidates']['downside']), 'USD m', FCD, FC)
for nm, key, run in (('base', 'base', FCB), ('banking', 'banking', FCK), ('downside', 'downside', FCD)):
    add('P-F08', f'Minimum DSCR, {nm}', r(f[key]['min_dscr']), 'x', run, FC)
    add('P-F08', f'Average DSCR (debt-service weighted), {nm}', r(f[key]['avg_dscr']), 'x', run, FC)
add('P-F08', 'LLCR at close (PV CFADS + DSRA over debt; first repayment period)', r(f['llcr_at_close_incl_dsra']), 'x', FCB, FC)
add('P-F08', 'LLCR at close excluding DSRA', r(f['base']['llcr_first_ex_dsra']), 'x', FCB, FC)
add('P-F08', 'Does the 1.40x LLCR test bind?', 'No' if not f['llcr_test_1_40_binds'] else 'Yes', 'text', FCB, FC)
# P-F09
f = P['P-F09']; e = f['eca_tests']
for k, v in f['principal_usd_m'].items(): add('P-F09', f'Scheduled principal {k}', m(v), 'USD m', FCB, FC)
add('P-F09', 'Weighted average life of repayment from COD', f"{e['wal_years']:.2f}", 'years (limit 7.25)', FCB, FC)
add('P-F09', 'Largest installment', p1(e['largest_installment_share']), '% of principal (limit 25%)', FCB, FC)
add('P-F09', 'Repayment term from COD', f"{e['tenor_years']:.2f}", 'years (limit 14)', FCB, FC)
add('P-F09', 'First repayment after COD', str(e['first_repayment_months_after_cod']), 'months (limit 24)', FCB, FC)
# P-F10
for case, run in (('fc_base', FCB), ('actual', ACT)):
    d = P['P-F10'][case]
    for k, v in d['build'].items(): add('P-F10', f"{'FC base' if case == 'fc_base' else 'Actual'} first full operating year ({d['period']}): {k.replace('_', ' ')}", r(v) if k == 'dscr' else m(v), 'x' if k == 'dscr' else 'USD m', run, d['period'])
# P-F11
f = P['P-F11']
add('P-F11a', 'DSRA initial balance (funded at COD; next period debt service)', m(f['dsra_initial']), 'USD m', FCB, '2021-05-01')
for k, v in list(P['P-F11a']['dsra_balance_by_period'].items())[:8]: add('P-F11a', f'DSRA balance {k}', m(v), 'USD m', FCB, k)
for k, v in f['mmra_contributions'].items():
    if int(k[:4]) <= 2030: add('P-F11b', f'MMRA contribution {k}', m2(v), 'USD m', FCB, k)
for k, v in f['mm_spend'].items(): add('P-F11b', f'Out-of-LTSA major maintenance spend {k}', m2(v), 'USD m', FCB, k)
# P-F12
f = P['P-F12']
add('P-F12', 'Swap fixed rate', f"{f['swap_fixed_pct']:.3f}%", '%', FCB, FC)
add('P-F12', 'Swap notional peak during construction', m(f['notional_monthly_peak']), 'USD m', FCB, FC)
for k, v in list(f['notional_semiannual'].items())[::4]: add('P-F12', f'Swap notional {k}', m(v), 'USD m', FCB, FC)
add('P-F12', 'Blended base rate on 80% hedged / 20% unhedged (2022)', f"{f['blended_base_pct']:.2f}%", '%', FCB, FC)
for k in ['ECA', 'A', 'B', 'COM']:
    add('P-F12', f'All-in cost {k}: full (base, margin, fees, ECA premium, PRI, gross-up)', f"{f['all_in_pct_full'][k]:.2f}%", '% pa', FCB, FC)
    add('P-F12', f'All-in cost {k}: excluding PRI premium', f"{f['all_in_pct_ex_pri'][k]:.2f}%", '% pa', FCB, FC)
    add('P-F12', f'All-in cost {k}: excluding WHT gross-up', f"{f['all_in_pct_ex_grossup'][k]:.2f}%", '% pa', FCB, FC)
    add('P-F12', f'All-in cost {k}: excluding financed ECA premium', f"{f['all_in_pct_ex_eca_premium'][k]:.2f}%", '% pa', FCB, FC)
    add('P-F12', f'All-in cost {k}: base and margin only', f"{f['all_in_pct_margin_and_base_only'][k]:.2f}%", '% pa', FCB, FC)
add('P-F12', 'Weighted all-in cost of senior debt', f"{f['weighted_all_in_pct']:.2f}%", '% pa', FCB, FC)
add('P-F12', 'Model all-in senior cost in 2022 (financing costs / opening debt)', f"{f['model_allin_rate_2022_pct_pa']:.2f}%", '% pa', FCB, '2022')
# P-F13
f = P['P-F13']
for k, v in f['totals'].items(): add('P-F13', 'Construction total: ' + k.replace('_', ' '), m(v), 'USD m', FCB, '2021-06-30')
for i_ in (0, 5, 11, 17, 23, 29, 32, 33):
    add('P-F13', f"Month {f['month'][i_]}: uses / debt / equity / IDC", f"{f['uses'][i_]:.1f} / {f['debt_draw'][i_]:.1f} / {f['equity'][i_]:.1f} / {f['idc_incl_swap_pri'][i_]:.2f}", 'USD m', FCB, f['month'][i_])
# P-F14
f = P['P-F14']
for oy, d in f['by_operating_year'].items():
    for k in ('ebitda', 'depreciation_deferred', 'depreciation_current', 'deferred_used', 'taxable_income', 'cit', 'minimum_turnover_tax', 'tax_paid'):
        add('P-F14', f'{oy} {k.replace("_", " ")}', m(d[k]), 'USD m', FCB, oy)
add('P-F14', 'First period with corporate income tax above the minimum tax', str(f['first_period_with_cit']), 'period', FCB, FC)
# P-F15
f = P['P-F15']
for oy, d in f['waterfall_by_oy'].items():
    for k, v in d.items():
        if v is not None: add('P-F15', f'{oy} {k.replace("_", " ")}', m(v), 'USD m', FCB, oy)
add('P-F15', 'Maximum trapped cash with 80% shareholder loans', m(f['max_trapped_with_shl']), 'USD m', FCB, FC)
add('P-F15', 'Maximum trapped cash with 100% share capital', m(f['max_trapped_without_shl']), 'USD m', FCB + ', no SHL variant', FC)
add('P-F15', 'Equity IRR with 100% share capital', p1(f['equity_irr_without_shl']), '%', FCB + ', no SHL variant', FC)
# P-F16
f = P['P-F16']
add('P-F16', 'Equity IRR (project-company level, from LNTP date, before WHT)', p1(f['equity_irr']), '% nominal post-tax', FCB, FC)
add('P-F16', 'Equity IRR including development spend and reimbursement', p1(f['equity_irr_incl_development']), '%', FCB, FC)
add('P-F16', 'Project IRR, post-tax', p1(f['project_irr_post_tax']), '%', FCB, FC)
add('P-F16', 'Project IRR, pre-tax', p1(f['project_irr_pre_tax']), '%', FCB, FC)
add('P-F16', 'Equity NPV at 16.0% at financial close', m(f['equity_npv_at_16pct_at_fc']), 'USD m', FCB, FC)
add('P-F16', 'Equity payback (cumulative equity cash flow turns positive)', f['payback_date'], 'date', FCB, FC)
for k, v in f['sensitivities'].items():
    add('P-F16', f'{k}: minimum DSCR / average DSCR / equity IRR', f"{v['min_dscr']:.2f}x / {v['avg_dscr']:.2f}x / {v['equity_irr'] * 100:.1f}%", 'x, x, %', 'Sensitivity (debt locked)', FC)
add('P-F16', 'Breakeven availability shift for 1.00x minimum DSCR', f"{f['breakeven_availability_shift_points']:.1f}", 'points below profile', FCB, FC)
add('P-F16', 'Breakeven capacity charge cut for 1.00x minimum DSCR', f"{f['breakeven_capacity_charge_cut_pct']:.1f}%", '%', FCB, FC)
add('P-F16', 'Months of zero SEKA payment covered by DSRA plus LC (gas paid)', f"{f['months_zero_payment_covered_paying_gas']:.1f}", 'months', FCB, '2022H1')
add('P-F16', 'Months covered if gas payments are deferred', f"{f['months_zero_payment_covered_gas_deferred']:.1f}", 'months', FCB, '2022H1')
# P-F17
for k, v in P['P-F17']['results'].items():
    add('P-F17', f'{k}: {v.get("description", "correct model")}', f"debt {v['senior_debt']:.1f} ({v.get('delta_senior_debt', 0):+.1f}), {v['binding']}; min DSCR {v['min_dscr_base']:.2f}x; avg {v['avg_dscr_base']:.2f}x; downside {v['min_dscr_downside']:.2f}x; banking {v['min_dscr_banking']:.2f}x; LLCR {v['llcr_at_close']:.2f}x; equity IRR {v['equity_irr'] * 100:.1f}%", 'USD m, x, %', 'FC base, sponsor model v0.9', '2018-06')
# P-F18
f = P['P-F18']
for k, v in f['uses'].items():
    if isinstance(v, dict):
        for kk, vv in v.items(): add('P-F18', 'Actual use: delay-related cost added (P-C43): ' + vv['name'], m2(vv['usd_m']), 'USD m', 'Modeler assumption (P-C43), Months 34-40', '2021-05 to 2021-11')
        continue
    add('P-F18', 'Actual use: ' + k.replace('_', ' '), m2(v), 'USD m', ACT, '2021-12-01')
for k, v in f['sources'].items(): add('P-F18', 'Actual source: ' + k.replace('_', ' '), m2(v), 'USD m', ACT, '2021-12-01')
for k, v in f['fc_base_comparison'].items(): add('P-F18', k.replace('_', ' '), m2(v), 'USD m', ACT + ' vs ' + FCB, '2021-12-01')
# P-F19
f = P['P-F19']
add('P-F19', 'Tested net output / heat rate', '581.9 MW / 6,286 kJ/kWh', 'inputs', 'Inputs', '2021-11-30')
add('P-F19', 'Output LDs / heat-rate LDs / total', '13.975 / 4.510 / 18.485', 'USD m', 'Inputs', '2021-11-30')
add('P-F19', 'COD re-sculpted constant DSCR (before the LD prepayment)', r(f['cod_resculpted_dscr']), 'x', RF, '2021-12-01')
add('P-F19', 'Same, had capacity and heat rate stayed at 588.4 MW / 6,261', r(f['cod_resculpted_dscr_if_no_reset']), 'x', RF + ' variant', '2021-12-01')
add('P-F19', 'Projected minimum DSCR after the June 2022 LD prepayment', r(f['projected_min_dscr_after_prepayment']), 'x', RF, '2022-06-30')
add('P-F19', 'Projected average DSCR after the prepayment', r(f['projected_avg_dscr_after_prepayment']), 'x', RF, '2022-06-30')
add('P-F19', 'Projected minimum DSCR without the prepayment', r(f['projected_min_dscr_without_prepayment']), 'x', RF + ' variant', '2022-06-30')
# P-F20
f = P['P-F20']
for k in f['overdue']:
    add('P-F20', f'{k}: overdue / deferred SNHK-GCK payables / CFADS / debt service / DSCR / DSRA draw / DSRA balance',
        f"{f['overdue'][k]:.1f} / {f['deferred_snhk_gck_payables'][k]:.1f} / {f['cfads'][k]:.1f} / {f['debt_service'][k]:.1f} / {f['cash_dscr'][k]:.2f}x / {f['dsra_draw'][k]:.1f} / {f['dsra_balance'][k]:.1f}", 'USD m, x', ACT, k)
add('P-F20', 'FX conversion losses, total 2022H2-2024H1', m2(f['fx_losses_total']), 'USD m', 'Inputs', '2024-06-30')
add('P-F20', 'Late payment interest accrued / received (60%)', f"{f['lpi_accrued_total']:.1f} / {f['lpi_received_total']:.1f}", 'USD m', ACT, '2025-06-30')
add('P-F20', 'Lock-up periods (distribution test failed)', ', '.join(f['lockup_periods']), 'periods', ACT, '2024-12-31')
# P-F21
f = P['P-F21']
add('P-F21', 'Historic DSCR at December 31, 2022', r(f['historic_dscr_2022_12_31']), 'x', ACT, '2022-12-31')
add('P-F21', 'Historic DSCR at June 30, 2023 (event of default below 1.10x)', r(f['historic_dscr_2023_06_30']), 'x', ACT, '2023-06-30')
add('P-F21', 'Period DSCR 2023H1', r(f['period_dscr_2023H1']), 'x', ACT, '2023-06-30')
add('P-F21', 'DSRA drawing at June 30, 2023', m2(f['dsra_draw_2023_06_30']), 'USD m', ACT, '2023-06-30')
add('P-F21', 'Waiver fee (0.25% of senior debt)', m2(f['waiver_fee']), 'USD m', ACT, '2023-10-26')
add('P-F21', 'Margin uplift cost, 2023H2-2024H2', m2(f['margin_uplift_cost_total']), 'USD m', ACT, '2024-12-31')
add('P-F21', 'Principal deferred from December 31, 2023 (60%)', m2(f['deferred_principal_2023_12_31']), 'USD m', ACT, '2023-12-31')
add('P-F21', 'Each of four deferred repayments (2024H1-2025H2)', m2(f['deferred_repayment_each_installment']), 'USD m', ACT, '2024-06-30')
add('P-F21', 'Historic DSCR at December 31, 2023 (waived test)', r(f['historic_dscr_2023_12_31']), 'x', ACT, '2023-12-31')
add('P-F21', 'Lock-up released (two tests >= 1.25x and DSRA full)', f['release_period'], 'period', ACT, '2024-12-31')
# P-F22
f = P['P-F22']
add('P-F22', 'Base rate 2022H2 (6M LIBOR)', f"{f['base_2022H2_libor_pct']:.2f}%", '%', ACT, '2022-07')
add('P-F22', 'Base rate 2023H1 (6M Term SOFR 4.86% + 0.42826%)', f"{f['base_2023H1_sofr_plus_cas_pct']:.2f}%", '%', ACT, '2023-01')
add('P-F22', 'Senior financing cost 2022H2 / 2023H1', f"{f['interest_cost_2022H2']:.1f} / {f['interest_cost_2023H1']:.1f}", 'USD m', ACT, '2023-06-30')
add('P-F22', 'All-in senior cost 2022H2 / 2023H1', f"{f['allin_rate_2022H2_pct_pa']:.2f}% / {f['allin_rate_2023H1_pct_pa']:.2f}%", '% pa', ACT, '2023-06-30')
add('P-F22', 'Unhedged balance 2023H1 (debt less swap notional)', m(f['unhedged_balance_2023H1']), 'USD m', ACT, '2023-01')
add('P-F22', 'Cost of the 0.42826% spread adjustment, 2023H1 / calendar 2023', f"{f['cas_cost_2023H1_unhedged']:.2f} / {f['cas_cost_per_year_2023']:.2f}", 'USD m', ACT, '2023-12-31')
# P-F23
f = P['P-F23']
for k in ('prepaid_principal', 'swap_unwind_receipt', 'bond_face', 'bond_proceeds', 'oid', 'underwriting', 'other_costs', 'pcg_upfront', 'transaction_costs_total', 'remaining_eca', 'remaining_a_loan', 'equity_pv_gain_at_13_75pct', 'equity_pv_gain_at_12_50pct'):
    add('P-F23', k.replace('_', ' '), m2(f[k]), 'USD m', ACT, '2025-06-30')
for k, v in f['prepaid_by_tranche'].items(): add('P-F23', f'prepaid {k}', m2(v), 'USD m', ACT, '2025-06-30')
add('P-F23', 'Combined sculpted DSCR (ECA + A-loan + bond, constant)', r(f['combined_dscr_sculpted']), 'x', ACT, '2025-06-30')
add('P-F23', 'Minimum DSCR after refinancing', r(f['min_dscr_after_refi']), 'x', ACT, '2025-06-30')
add('P-F23', 'Equity IRR with / without the refinancing', f"{f['equity_irr_with_refi'] * 100:.1f}% / {f['equity_irr_without_refi'] * 100:.1f}%", '%', ACT, '2025-06-30')
for k, v in list(f['bond_amortization'].items())[::2]: add('P-F23', f'Bond amortization {k}', m2(v), 'USD m', ACT, '2025-06-30')
# P-F24
f = P['P-F24']
for k in ('equity_value_100pct_at_13_75', 'equity_value_100pct_at_12_50', 'value_24pct_at_13_75', 'value_24pct_at_12_50', 'leakage_h1_2026_distribution_24pct', 'price_at_completion', 'kilnworth_reserve_price_24pct', 'deferred_consideration', 'cost_basis_24pct', 'seller_gain', 'indirect_transfer_tax'):
    add('P-F24', k.replace('_', ' '), m2(f[k]), 'USD m', ACT, '2025-12-31 (locked box); 2026-09-30 (completion)')
add('P-F24', 'Locked-box ticker factor (6.5% simple, 273 days)', f"{f['ticker_factor']:.4f}", 'factor', ACT, '2026-09-30')
add('P-F24', "Kilnworth's IRR on the sold 24% (after transfer tax)", p1(f['kilnworth_irr_on_sold_stake']), '%', ACT, '2026-09-30')
add('P-F24', 'Same including the USD 4.0 million deferred consideration (taxed)', p1(f['kilnworth_irr_incl_deferred']), '%', ACT, '2027-06-30')
# P-F25
f = P['P-F25']
for k in ('senior_debt_outstanding', 'swap_mtm_to_project', 'equity_npv_distributions_14_5', 'equity_contributed_compounded_less_distributions', 'equity_amount', 'seka_default_compensation', 'project_default_compensation', 'natural_fm_compensation', 'equity_contributed', 'distributions_received'):
    add('P-F25', k.replace('_', ' '), m(f[k]), 'USD m', ACT, '2023-06-30')
# P-F26
f = P['P-F26']
for k in ('book_equity_lenders_basis', 'ifrs12_equity_adjustment_pretax', 'shl_at_completion', 'consideration', 'fv_retained_36pct', 'carrying_amount_60pct_lenders_basis', 'carrying_amount_60pct_ifrs', 'gain_on_loss_of_control_lenders_basis', 'gain_on_loss_of_control_ifrs', 'hedge_reserve_parent_share_recycled', 'equity_method_carrying_value_36pct', 'indirect_transfer_tax'):
    add('P-F26', k.replace('_', ' '), m(f[k]), 'USD m', ACT, '2026-09-30')
# P-F27
for case, run in (('fc_base', FCB), ('actual', ACT)):
    for k, v in P['P-F27'][case].items(): add('P-F27', f'{case.replace("_", " ")}: {k.replace("_", " ")} (life total)', m(v), 'USD m', run, '2018-2046')
# P-F28
f = P['P-F28']
add('P-F28', 'Senior debt / total funding / gearing', f"{f['senior_debt']:.1f} / {f['total_funding']:.1f} / {f['gearing'] * 100:.1f}%", 'USD m, %', FCB, '2018-05')
add('P-F28', 'Tenor from COD / WAL', f"{f['tenor_from_cod_years']:.1f} / {f['wal_years']:.2f}", 'years', FCB, '2018-05')
for nm, run in (('base', FCB), ('banking', FCK), ('downside', FCD)):
    add('P-F28', f'{nm}: min DSCR / avg DSCR / LLCR', f"{f[nm]['min_dscr']:.2f}x / {f[nm]['avg_dscr']:.2f}x / {f[nm]['llcr_first']:.2f}x", 'x', run, '2018-05')
add('P-F28', 'Equity IRR / project IRR (base)', f"{f['equity_irr_base'] * 100:.1f}% / {f['project_irr_base'] * 100:.1f}%", '%', FCB, '2018-05')
# P-F29
f = P['P-F29']
for k, v in f['contributions_by_year'].items(): add('P-F29', f'Handback reserve contribution {k}', m2(v), 'USD m', ACT, k)
add('P-F29', 'Handback reserve at PPA expiry', m(f['balance_at_expiry']), 'USD m', ACT, '2046-11-30')
# P-F30
f = P['P-F30']
add('P-F30', 'EAR loss / deductible / paid to EPC contractor', '6.84 / 1.00 / 5.84', 'USD m', 'Inputs', '2021-06-09')
add('P-F30', 'DSU: 76 days delay less 45-day deductible = 31 days x USD 228,400', m2(f['dsu_paid']), 'USD m', 'Inputs', '2021-11')
# P-F31
f = P['P-F31']
for k in f['actual']:
    add('P-F31', f'OY1 {k.replace("_", " ")}: actual (Dec 2021-Nov 2022) / FC base (May 2021-Apr 2022)',
        f"{f['actual'][k]:.1f} / {f['fc_base'][k]:.1f}", '% or USD m', ACT + ' / ' + FCB, '2022-11-30')
# P-F32
f = P['P-F32']
for k in ('energy_mwh', 'capacity_payment', 'vom_payment', 'fuel_charge', 'gta_pass_through', 'take_or_pay', 'invoice_total'):
    add('P-F32', 'January 2022 invoice: ' + k.replace('_', ' '), f"{f[k]:,.0f}" if k == 'energy_mwh' else m2(f[k]), 'MWh' if k == 'energy_mwh' else 'USD m', ACT + ' formulas', '2022-01-31')
add('P-F32', 'Gas price 2022', m2(f['gas_price']), 'USD/MMBtu', ACT, '2022-01')
# P-F33
f = P['P-F33']
for k in ('daily_interest', 'daily_fixed_costs', 'ppa_delay_ld', 'total', 'epc_delay_ld', 'daily_capacity_revenue'):
    add('P-F33', k.replace('_', ' ') + ' per day', f"{f[k]:,.0f}", 'USD', FCB, '2021-05-01')
# P-F34
for oy, d in P['P-F34']['by_operating_year'].items():
    for k in ('om_fixed', 'ltsa_fixed', 'ltsa_var', 'insurance', 'ga', 'consumables', 'mm_contr', 'opex_om'):
        add('P-F34', f'{oy} {k.replace("_", " ")}', m2(d[k]), 'USD m', FCB, oy)
# P-F35
f = P['P-F35']
for nm in ('base', 'banking', 'downside', 'dispatch_50'):
    add('P-F35', f'2022 gas burned, {nm}', f"{f[nm]['gas_mmbtu'] / 1e6:.2f}", 'million MMBtu', nm, '2022')
    add('P-F35', f'2022 take-or-pay payment, {nm}', m2(f[nm]['take_or_pay_payment']), 'USD m', nm, '2022')
add('P-F35', 'Annual contract quantity / take-or-pay level', f"{f['base']['acq'] / 1e6:.2f} / {f['base']['top_level'] / 1e6:.2f}", 'million MMBtu', 'Inputs', '2022')
# P-F36
for k, v in P['P-F36']['grid'].items():
    add('P-F36', k, f"debt {v['senior_debt']:.1f} ({v['binding']}); downside min {v['downside_min_dscr']:.2f}x; equity IRR {v['equity_irr'] * 100:.1f}%", 'USD m, x, %', FCB, '2017-10')
# P-F37 to P-F45
f = P['P-F37']
for case in ('fc_base', 'actual'):
    for k, v in f[case].items():
        add('P-F37', f'VAT {case.replace("_", " ")}: {k.replace("_", " ")}', (f"{v:,.1f}" if isinstance(v, float) else v), 'KCR m' if 'kcr' in k else ('USD m' if isinstance(v, float) else 'month'), FCB if case == 'fc_base' else ACT, '2018-2022')
f = P['P-F38']
for case in ('fc_base', 'actual'):
    d = f[case]
    add('P-F38', f'Thin cap {case.replace("_", " ")}: SHL interest total / deductible / disallowed', f"{d['shl_interest_total']:.1f} / {d['deductible']:.1f} / {d['disallowed']:.1f}", 'USD m', FCB if case == 'fc_base' else ACT, 'life')
    add('P-F38', f'Thin cap {case.replace("_", " ")}: deductible share in the COD period', p1(d['first_period_fraction']), '%', FCB if case == 'fc_base' else ACT, 'COD')
f = P['P-F39']
for nm, d in (('FC base at COD (588.4 MW)', f['fc_base_at_cod']), ('Actual at COD (581.9 MW)', f['actual_at_cod'])):
    add('P-F39', f'LC {nm}: two-plus-one / three-month', f"{d['two_plus_one']:.1f} / {d['three_month']:.1f}", 'USD m', FCB if 'FC' in nm else ACT, '2021-05-01' if 'FC' in nm else '2021-12-01')
for y, d in f['actual_resets'].items(): add('P-F39', f'LC reset January 1, {y}: two-plus-one / three-month', f"{d['two_plus_one']:.1f} / {d['three_month']:.1f}", 'USD m', ACT, f'{y}-01-01')
f = P['P-F40']
add('P-F40', 'FX conversion losses total (2022H2-2024H1)', m2(f['fx_losses_total']), 'USD m', 'Inputs', '2024-03-29')
add('P-F40', 'Energy-charge arrears matched by deferred SNHK/GCK payables, peak (2023-06-30)', m(max(f['energy_charge_arrears_matched_by_snhk_gck_deferral'].values())), 'USD m', ACT, '2023-06-30')
add('P-F40', 'Overdue reduction 2024H1 / 2024H2 / 2025H1', f"{f['overdue_reduction_2024H1']:.1f} / {f['overdue_reduction_2024H2']:.1f} / {f['overdue_reduction_2025H1']:.1f}", 'USD m', 'Inputs', '2025-06-30')
add('P-F40', 'Implied monthly settlement installment 2024H2 / 2025H1', f"{f['settlement_installment_implied_monthly_2024H2']:.2f} / {f['settlement_installment_implied_monthly_2025H1']:.2f}", 'USD m', 'Inputs', '2025-06-30')
add('P-F40', 'Late payment interest received / waived', f"{f['lpi_received']:.2f} / {f['lpi_waived']:.2f}", 'USD m', ACT, '2025-06-30')
f = P['P-F41']
for k in ('base', 'banking', 'downside'):
    add('P-F41', f'PLCR at close, {k}', r(f['plcr_at_close'][k]), 'x', {'base': FCB, 'banking': FCK, 'downside': FCD}[k], FC)
    add('P-F41', f'LLCR at close (incl. DSRA), {k}', r(f['llcr_at_close'][k]), 'x', {'base': FCB, 'banking': FCK, 'downside': FCD}[k], FC)
for case in ('base', 'banking', 'downside'):
    for k, v in f['profiles'][case].items(): add('P-F41', f'FC {case} {k}: CFADS / DS / DSCR', f"{v['cfads']:.1f} / {v['ds']:.1f} / {v['dscr']:.2f}x", 'USD m, x', {'base': FCB, 'banking': FCK, 'downside': FCD}[case], k)
for k, v in f['actual_profile'].items():
    if k <= '2026H2': add('P-F41', f'Actual {k}: CFADS / DS / DSCR', f"{v['cfads']:.1f} / {v['ds']:.1f} / {v['dscr']:.2f}x", 'USD m, x', ACT, k)
f = P['P-F42']
add('P-F42', 'Monte Carlo inputs', '; '.join(f'{k}: {v}' for k, v in f['inputs'].items()) + f"; {f['runs']} runs, seed {f['seed']}", 'text', FCB + ', debt locked', FC)
add('P-F42', 'Minimum DSCR P10 / P50 / P90', f"{f['min_dscr_p10']:.2f}x / {f['min_dscr_p50']:.2f}x / {f['min_dscr_p90']:.2f}x", 'x', FCB, FC)
add('P-F42', 'Equity IRR P10 / P50 / P90', f"{f['equity_irr_p10'] * 100:.1f}% / {f['equity_irr_p50'] * 100:.1f}% / {f['equity_irr_p90'] * 100:.1f}%", '%', FCB, FC)
add('P-F42', 'Probability of a historic DSCR below 1.20x / 1.10x in any test', f"{f['prob_hist_below_1_20'] * 100:.1f}% / {f['prob_hist_below_1_10'] * 100:.1f}%", '%', FCB, FC)
add('P-F42', 'Minimum DSCR histogram (bins 1.0,1.1,1.2,1.25,1.3,1.35,1.4,1.5,+)', ', '.join(map(str, f['min_dscr_histogram']['counts'])), 'runs', FCB, FC)
f = P['P-F43']
add('P-F43', 'Sizing passes to USD 1,000 tolerance (profile, debt, notional)', str(f['sizing_passes']), 'passes', FCB, FC)
add('P-F43', 'Sizing residuals by pass', ', '.join(f"{x:.4g}" for x in f['sizing_residuals_usd_m']), 'USD m', FCB, FC)
add('P-F43', 'Construction fixed-point passes (Python)', str(f['construction_fixed_point_iterations']), 'passes', FCB, FC)
add('P-F43', 'Closed-form total funding at the 75% gearing cap', m(f['closed_form_T_at_75pct']), 'USD m', FCB, FC)
add('P-F43', 'Pro rata: total funding / debt / IDC incl. swap and PRI', f"{f['pro_rata']['T']:.1f} / {f['pro_rata']['D']:.1f} / {f['pro_rata']['idc']:.1f}", 'USD m', FCB, FC)
ef = f['equity_first']
add('P-F43', 'Equity first: total funding / debt / equity / IDC / commitment fees', f"{ef['T']:.1f} / {ef['D']:.1f} / {ef['E']:.1f} / {ef['idc']:.1f} / {ef['commitment_fees']:.1f}", 'USD m', FCB + ' variant', FC)
f = P['P-F44']
for oy, d in f['by_operating_year'].items():
    add('P-F44', f'{oy} revenue: capacity / VOM / fuel / GTA / take-or-pay / total', f"{d['cap_pay']:.1f} / {d['vom']:.1f} / {d['fuel_rev']:.1f} / {d['gta_res'] + d['gta_com']:.1f} / {d['top_pay']:.1f} / {d['revenue']:.1f}", 'USD m', FCB, oy)
for k, v in f['sample_2022H1'].items():
    if k != 'period': add('P-F44', f'2022H1 revenue build: {k}', f"{v:,.2f}", 'see model row', FCB, '2022H1')
f = P['P-F45']
for oy, d in f['by_operating_year'].items():
    for k, v in d.items(): add('P-F45', f'{oy} {k.replace("_", " ")} (lenders basis)', m(v), 'USD m', FCB, oy)
for per, bs in f['balance_sheets'].items():
    for k, v in bs.items():
        if k != 'date': add('P-F45', f'Balance sheet {bs["date"]}: {k.replace("_", " ")}', m(v), 'USD m', FCB, bs['date'])
# P-F37 working capital extension
for per, d in P['P-F37']['working_capital_fc_base'].items():
    add('P-F37', f'Working capital {per}: receivables / gas / GTA / O&M-LTSA / other payables / net', f"{d['receivables']:.1f} / {d['gas_payables']:.1f} / {d['gta_payables']:.1f} / {d['om_ltsa_payables']:.1f} / {d['other_payables']:.1f} / {d['net_working_capital']:.1f}", 'USD m', FCB, per)
# P-F40 extension
f = P['P-F40']
add('P-F40', 'Netting set-off per month 2023H2 / 2024H1 (fall in deferred SNHK/GCK payables)', f"{f['netting_setoff_monthly_2023H2']:.2f} / {f['netting_setoff_monthly_2024H1']:.2f}", 'USD m', ACT, '2024-03-31')
for g in f['guarantee_demands']: add('P-F40', f"Guarantee demand {g['date']} (USD {g['amount']} m): paid {g['paid']}", str(g['days']), 'days', 'Inputs', g['date'])
add('P-F40', 'FX queue duration (2022-11-07 to 2024-03-29)', str(f['fx_queue_days']), 'days', 'Inputs', '2024-03-29')
# P-F09 extension
e = P['P-F09']['eca_tests']; ea = P['P-F09']['eca_tests_actual']
add('P-F09', 'Share of principal repaid within 24 months of COD (FC base; minimum 2%)', p1(e['repaid_within_24_months_share']), '%', FCB, FC)
add('P-F09', 'Actual: WAL / tenor / first repayment / repaid within 24 months', f"{ea['wal_years']:.2f} y / {ea['tenor_years']:.2f} y / {ea['first_repayment_months_after_cod']} months / {ea['repaid_within_24_months_share'] * 100:.1f}%", 'years, months, %', ACT, '2021-12-01')
# P-F07 extension
for nm, d in P['P-F07']['equity_by_sponsor'].items():
    add('P-F07', f'Equity at close by sponsor: {nm} ({d["share_pct"]}%): share capital / SHL / total', f"{d['share_capital']:.2f} / {d['shareholder_loans']:.2f} / {d['total']:.2f}", 'USD m', FCB, FC)
# P-F46 to P-F63
f = P['P-F46']
add('P-F46', 'GTA 2022: reservation / commodity / total passed to SEKA (= GCK revenue from Belanou)', f"{f['reservation']:.1f} / {f['commodity']:.1f} / {f['total_passed_to_seka']:.1f}", 'USD m', ACT, '2022-12-31')
add('P-F46', 'Gas burned 2022', f"{f['gas_mmbtu'] / 1e6:.2f}", 'million MMBtu', ACT, '2022-12-31')
f = P['P-F47']
for k, v in f['by_oy'].items(): add('P-F47', f'Fuel margin from heat-rate headroom, {k}', m2(v), 'USD m', FCB, k)
add('P-F47', 'Contracted / plant heat rate, 2021H2 (incl. part-load 2.3%)', f"{f['contracted_hr_oy1']:,.0f} / {f['plant_hr_oy1']:,.0f}", 'kJ/kWh', FCB, '2021H2')
f = P['P-F48']
for k in ('base', 'banking', 'low_dispatch_58', 'actual'):
    add('P-F48', f'LTSA 128,000 EOH run-out, {k}', f"{f[k]['date']} ({f[k]['eoh_per_gt_year']:,.0f} EOH/yr; {f[k]['years_from_cod']:.1f} years)", 'date', k, f[k]['date'])
add('P-F48', '16-year LTSA date (FC base / actual)', f"{f['sixteen_year_date_fc']} / {f['sixteen_year_date_actual']}", 'date', 'Inputs', '2037')
f = P['P-F49']
for k, v in f['first_utilization'].items(): add('P-F49', f'First utilization, {k}', m2(v), 'USD m', FCB, '2018-07-17')
for k in ('first_utilization_total', 'equity_at_close', 'of_which_lntp_credit', 'equity_cash_at_close', 'epc_advance_gross', 'epc_advance_cash_net_of_lntp', 'upfront_fees', 'first_eca_premium', 'advisers_at_close', 'insurance_at_close', 'idc_month1', 'total_uses_month1'):
    add('P-F49', k.replace('_', ' '), m2(f[k]), 'USD m', FCB, '2018-07-17')
for grp in ('development_cost_reimbursement', 'development_fee', 'abdb_fund_premium_paid_by_fund'):
    for k, v in f[grp].items(): add('P-F49', f'{grp.replace("_", " ")}: {k}', f"{v:.4f}" if grp.startswith('abdb') else m2(v), 'USD m', 'Annex 1.14', '2018-07-17')
for k, v in f['sponsor_development_receipts'].items(): add('P-F49', f'Total development receipts at close, {k}', m2(v), 'USD m', 'Annex 1.14', '2018-07-17')
f = P['P-F50']
add('P-F50', 'PV of the 7.5 bps swap charge / at 10 bps / difference', f"{f['pv_7_5bps']:.2f} / {f['pv_10bps']:.2f} / {f['saving']:.2f}", 'USD m', FCB, '2018-07-17')
f = P['P-F51']
for k, v in f['actual'].items(): add('P-F51', f'PRI premium {k} (insured amount {v["insured_amount"]:.1f})', m2(v['premium']), 'USD m', ACT, k)
add('P-F51', 'PRI premium total to cancellation (actual)', m2(f['actual_total']), 'USD m', ACT, '2025-06-30')
f = P['P-F52']
for k in f['actual_cum_pct']:
    add('P-F52', f'EPC cumulative progress {k}: planned / actual', f"{f['planned_cum_pct'].get(k, 100.0):.1f}% / {f['actual_cum_pct'][k]:.1f}%", '% of contract price', 'FC base / actual', k)
f = P['P-F53']
for k, v in f['ecl'].items(): add('P-F53', f'ECL allowance {k} (normal / 1-90 / 91-180 / >180 days aged)', f"{v['ecl']:.2f} ({v['normal_receivables']:.1f} / {v['overdue_1_90']:.1f} / {v['overdue_91_180']:.1f} / {v['overdue_over_180']:.1f})", 'USD m', ACT, k)
for k, v in f['swap_mtm'].items(): add('P-F53', f'Swap MTM to project (= hedge reserve, pre-tax), {k}', m2(v), 'USD m', ACT, k[:10])
f = P['P-F54']
for y, d in f['estimate'].items(): add('P-F54', f'{y} estimate: GloBE income / covered taxes / SBIE / UK top-up on Kilnworth share', f"{d['globe_income']:.1f} / {d['covered_taxes']:.2f} / {d['sbie']:.1f} / {d['uk_top_up_estimate']:.2f}", 'USD m', ACT, f'{y}-12-31')
f = P['P-F55']
add('P-F55', 'Underwritten at mandate (ECA-covered + commercial) / final holds commercial / ECA-covered', f"{f['underwritten_at_mandate']:.1f} / {f['final_hold_commercial']:.1f} / {f['final_hold_eca']:.1f}", 'USD m', FCB, '2018-07-17')
for ph in ('construction_2020H1', 'operations_2022H1'):
    d = f[ph]; add('P-F55', f'Castellan {ph}: RWA / capital / net income (annual) / RORAC', f"{d['rwa']:.1f} / {d['capital']:.2f} / {d['net_income']:.2f} / {d['rorac'] * 100:.1f}%", 'USD m, %', FCB, ph[-6:])
f = P['P-F56']
add('P-F56', 'IFRIC 12 financial asset at COD / effective interest rate', f"{f['asset_at_cod']:.1f} / {f['effective_interest_rate_annual'] * 100:.2f}% a year", 'USD m, %', ACT, '2021-12-01')
for y, d in f['by_year'].items():
    add('P-F56', f'{y}: financial asset / PP&E (lenders) / finance income / capital charge collected / PBT difference / cumulative equity difference', f"{d['financial_asset']:.1f} / {d['ppe_lenders_basis']:.1f} / {d['finance_income']:.1f} / {d['capital_charge_collected']:.1f} / {d['pbt_difference']:.1f} / {d['cumulative_equity_difference_pretax']:.1f}", 'USD m', ACT, f'{y}-12-31')
f = P['P-F57']
for k, d in f['technologies'].items():
    add('P-F57', f'{k}: annualized fixed cost / fuel cost / cost at 30%, 50%, 70%, 90% CF', f"{d['annualized_usd_per_kw_year']:.1f} USD/kW-yr / {d['fuel_usd_per_mwh']:.1f} / {d['usd_per_mwh_by_cf']['30%']:.1f}, {d['usd_per_mwh_by_cf']['50%']:.1f}, {d['usd_per_mwh_by_cf']['70%']:.1f}, {d['usd_per_mwh_by_cf']['90%']:.1f}", 'USD/MWh (2015)', 'Annex 4.12 inputs', '2015')
f = P['P-F58']
for k in f['gas_burn_actual']:
    add('P-F58', f'{k}: dispatch / gas burn actual / at 76.5% / fuel charge actual / at 76.5%', f"{f['dispatch'][k]:.1f}% / {f['gas_burn_actual'][k] / 1e6:.2f} / {f['gas_burn_at_76_5'][k] / 1e6:.2f} million MMBtu / {f['fuel_charge_actual'][k]:.1f} / {f['fuel_charge_at_76_5'][k]:.1f}", '%, MMBtu, USD m', ACT + ' vs ' + RF, k)
f = P['P-F59']
for k in ('at_signing_2017', 'at_2023_redetermination'):
    d = f[k]; add('P-F59', f'Halbeck RBL {k}: NPV10 of operating cash flows to the reserve tail (65% share) / borrowing base (NPV / 1.30, max 600)', f"{d['npv10_p50_net']:.1f} / {d['borrowing_base']:.1f}", 'USD m', 'Illustrative (annex 4.13)', k[-4:])
add('P-F59', 'Gas price to SNHK that would give a USD 420m base at signing', f"{f['gas_price_needed_for_420_at_signing']:.2f}", 'USD/MMBtu (2018)', 'Illustrative', '2017-10')
f = P['P-F60']
add('P-F60', 'Bid screen: cost / capacity + FOM revenue / fixed costs / CFADS proxy', f"{f['project_cost']:.1f} / {f['capacity_and_fom_revenue']:.1f} / {f['fixed_costs_2018_prices']:.1f} / {f['cfads_proxy']:.1f}", 'USD m', 'Annex 4.7 inputs', '2016-09')
add('P-F60', 'Bid screen: debt capacity at 1.35x over 13 years / debt at 75% gearing / capacity payments share of SEKA revenue', f"{f['debt_capacity_dscr_1_35']:.1f} / {f['debt_at_75pct_gearing']:.1f} / {f['capacity_share_of_seka_revenue_2016'] * 100:.1f}%", 'USD m, %', 'Annex 4.7 inputs', '2016-09')
f = P['P-F61']
add('P-F61', '2P reserves / Belanou GSA / SEKA contract / coverage', f"{f['reserves_2p_bcf']:.0f} / {f['belanou_bcf']:.0f} / {f['seka_existing_bcf']:.0f} bcf / {f['coverage_ratio']:.2f}x", 'bcf, x', 'Annex 1.7.4 inputs', '2017')
f = P['P-F62']
add('P-F62', 'Levelized tariffs: winner / runner-up / third / fourth', f"{f['winner']:.2f} / {f['runner_up']:.2f} / {f['third']:.2f} / {f['fourth']:.2f}", 'USD/MWh (2016)', 'Bid inputs', '2016-09-27')
add('P-F62', 'Pricing committee tariff at USD 15.05/kW-month (bid-model IRR 17.6%) vs submitted (16.0%)', f"{f['pricing_committee_tariff_at_15_05']:.2f} vs {f['winner']:.2f}", 'USD/MWh', 'Bid inputs', '2016-09-19')
f = P['P-F63']
add('P-F63', 'June 30, 2023: 12-month CFADS / debt service / historic DSCR', f"{f['cfads_12m']:.1f} / {f['debt_service_12m']:.1f} / {f['historic_dscr']:.2f}x", 'USD m, x', ACT, '2023-06-30')
add('P-F63', 'Equity cure needed for 1.10x / 1.20x', f"{f['cure_to_1_10']:.1f} / {f['cure_to_1_20']:.1f}", 'USD m', ACT, '2023-06-30')

# P-F64 to P-F66 (v1.2)
for st in P['P-F64']['steps']:
    add('P-F64', 'Bid-to-close IRR bridge (sequential, in this order): ' + st['step'], f"{st['cumulative_irr'] * 100:.2f}% ({st['change_pp']:+.2f} pp)", '% (cumulative)', FCB + ' re-sized at each step', '2016-09 to 2018-07')
add('P-F64', 'Bridge total: bid model to FC base / sum of steps (no residual)', f"{P['P-F64']['total_change_pp']:+.2f} pp / {P['P-F64']['sum_of_steps_pp']:+.2f} pp", 'pp', FCB, '2016-09 to 2018-07')
add('P-F64', 'Reconstructed bid-model swapped base rate (modeler reconstruction, solved to the 16.0% bid IRR)', f"{P['P-F64']['reconstructed_bid_swapped_rate_pct']:.2f}%", '% flat', 'Modeler reconstruction', '2016-09')
f = P['P-F65']
add('P-F65', 'FX forwards (Castellan, traded 2018-07-17): share hedged / KCR notional / USD at forward / USD at FC spot / average forward', f"{f['hedge_share'] * 100:.0f}% / {f['total_kcr_m']:,.0f} / {f['total_usd_at_forward']:.1f} / {f['total_usd_at_fc_spot']:.1f} / {f['average_forward']:.1f}", '%, KCR m, USD m, KCR/USD', 'Contract (FC)', '2018-07-17')
for k, v in list(f['schedule'].items())[::6]: add('P-F65', f'Forward {k}: KCR notional / forward rate / USD', f"{v['kcr_m']:,.1f} / {v['forward']:.1f} / {v['usd_at_forward']:.2f}", 'KCR m, KCR/USD, USD m', 'Contract (FC)', k)
f = P['P-F66']
for k, v in f['settlements_by_half'].items(): add('P-F66', f'FX forward settlement {k} (gain to project)', m2(v), 'USD m', ACT, k)
add('P-F66', 'FX forward settlements, total', m2(f['settlements_total']), 'USD m', ACT, '2021-11-30')
for k, v in f['mtm_to_project'].items(): add('P-F66', f'FX forward MTM to project at {k}', m2(v), 'USD m', ACT, k)
add('P-F66', 'Unhedged KCR depreciation saving on the onshore EPC (for comparison)', m2(f['unhedged_fx_gain_on_onshore_epc']), 'USD m', ACT, '2021-11-30')
add('P-F40', 'SEKA LC drawing, February 14, 2023 (2023 reset value; P-C44)', m(P['P-F40']['lc_drawing']), 'USD m', ACT, '2023-02-14')

L = ['# Figure ledger: Case P (Bélanou Combined Cycle Power Project)', '',
     'Source: `model/outputs_case_p.json`, produced by `model/case_p.py` (Case P model v1.3; story as of October 3, 2026); formatted by '
     '`model/ledger_p.py` (no computation). Amounts in USD million, nominal, unless stated. Scenario numbers are the workbook scenario switch '
     '(1 FC base, 2 FC banking, 3 FC downside, 4-13 sensitivities, 14 COD re-forecast, 15 actual history). P-F01 to P-F36 are the Case Bible '
     'register; P-F37 to P-F45 are editor assignments and P-F46 to P-F63 come from case-bible-annex-p.md (P-F11 is split into P-F11a DSRA and P-F11b MMRA). Model version 1.3 (annex absorbed; editor rulings of October 3, 2026: delay-related overrun categories P-C43, FX hedge D-114, P-F64 to P-F66, sequential P-F64 bridge, RBL expectation revised P-C46). Writers cite the ID; print values in the style-sheet format.', '',
     'Definitions used throughout: DSCR = CFADS / (interest incl. WHT gross-up + swap net + PRI premium + PCG fee + scheduled principal); '
     'average DSCR = sum of CFADS / sum of debt service over the loan life; LLCR = (PV of CFADS to final maturity at the period all-in senior '
     'cost + DSRA balance) / senior debt, at the start of the first repayment period; gearing = senior debt / total funding requirement; '
     'CFADS = revenue - operating costs - tax paid - increase in working capital - MMRA contributions + MMRA releases. Equity IRR is at '
     'project-company level from the LNTP date (February 5, 2018), before shareholder withholding tax.', '',
     '| ID | Figure | Value | Units | Model run (scenario) | As-of story date |', '|---|---|---|---|---|---|']
for row in rows:
    L.append('| ' + ' | '.join(str(c) for c in row) + ' |')
L += ['', 'FC base equity IRR is below the 16.0% bid-model target; P-F64 bridges the gap sequentially with no residual (steps printed to 0.01 pp may sum to the total within 0.01 by rounding). See `model/case_p_report.md` Section 8b.']
open(os.path.join(H, 'figure-ledger-case-p.md'), 'w').write('\n'.join(L) + '\n')
print(len(rows), 'rows')
