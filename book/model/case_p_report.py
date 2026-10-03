"""Writes model/case_p_report.md from the outputs dictionary produced by case_p.main()."""

def f1(x): return f"{x:,.1f}"
def f2(x): return f"{x:,.2f}"
def fx(x): return f"{x:.2f}x"
def pc(x): return f"{x * 100:.1f}%"

def table(rows, head):
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)]
    out += ['| ' + ' | '.join(str(c) for c in r) + ' |' for r in rows]
    return '\n'.join(out)

def write(o, path):
    P = o['figures']; S = o['summary']; Z = o['sizing']
    L = []
    a = L.append
    a('# Case P reference model: report')
    a('')
    a('Model: `model/case_p.py` (Python mirror, source of truth) and `model/Case_P_Model.xlsx` (live-formula workbook built by '
      '`model/build_excel_p.py`). Run date October 3, 2026. All amounts USD million unless stated. Figures for the book are '
      'cited from `model/figure-ledger-case-p.md` by ID; this report is the modeler\'s summary.')
    a('')
    a('## 1. Scenarios run')
    a('')
    rows = []
    for i, n in o['meta']['scenarios'].items():
        s = S[i] if i in S else S[str(i)]
        rows.append([i, n, f1(s['T']), f1(s['D']), fx(s['min_dscr']), fx(s['avg_dscr']), fx(s['llcr_first']),
                     pc(s['equity_irr']), pc(s['project_irr']), s['lockups']])
    a(table(rows, ['#', 'Scenario', 'Total funding', 'Senior debt', 'Min DSCR', 'Avg DSCR', 'LLCR (1st DS period)', 'Equity IRR', 'Project IRR', 'Lock-ups']))
    a('')
    a('Senior debt is the committed amount of the four tranches. Scenarios 2 to 6 and 9 to 13 keep the FC base construction and the '
      'contractual debt (amount, repayment profile, swap notional); scenarios 7 and 8 re-gross the funding pro rata at the contract '
      'debt share. Scenario 14 is the lenders\' COD re-forecast (actual construction, no crisis); scenario 15 is the actual history.')
    a('')
    a('## 2. Financial close sizing (FC base)')
    a('')
    u = P['P-F07']['uses']; sres = P['P-F07']['sources']
    a(table([[k.replace('_', ' '), f2(v)] for k, v in u.items()], ['Use of funds', 'USD m']))
    a('')
    a(table([[k.replace('_', ' '), f2(v)] for k, v in sres.items()], ['Source of funds', 'USD m']))
    a('')
    a(f"Binding constraint: **{Z['binding']}**. Candidates: gearing cap (75% of the total funding requirement at full gearing, "
      f"closed form) {f2(Z['gearing_cap_debt_closed_form'])}; DSCR 1.35x capacity {f2(Z['dscr_capacity_at_1_35'])}; downside "
      f"1.20x constraint {f2(Z['candidates']['downside'])} (downside minimum DSCR at the sized debt {Z['downside_min_dscr']:.4f}x). "
      f"Gearing achieved {pc(Z['gearing'])}. LLCR at close (incl. DSRA) {Z['llcr_at_close_incl_dsra']:.4f}x, so the 1.40x LLCR "
      f"test does not bind (excluding the DSRA it would be {Z['llcr_at_close_ex_dsra']:.4f}x).")
    a('')
    e = P['P-F09']['eca_tests']
    a(f"ECA tests (OECD project finance terms in force in 2018): repayment term from COD {e['tenor_years']:.2f} years (max 14); WAL "
      f"{e['wal_years']:.2f} years (max 7.25); largest installment {pc(e['largest_installment_share'])} (max 25%); first repayment "
      f"{e['first_repayment_months_after_cod']} months after COD (max 24). All pass. The Case Bible's \"first repayment within six "
      "months of COD\" is not an Arrangement rule (fact sheet t-oecd-pf-2018); it is dropped and the base first repayment stays "
      "December 31, 2021.")
    a('')
    a('## 3. Circularity resolution (for Chapters 40 and 42)')
    a('')
    it = o['iterations']
    a(f"* Construction gross-up (IDC, commitment and upfront fees, ECA premium, DSRA): Python iterates the total funding requirement "
      f"to a tolerance of USD 1,000 ({it['fc_construction_fixed_point']} passes on the FC base). The workbook solves the same fixed "
      "point in closed form on the Funding sheet: each month's balance is carried as alpha_m + beta_m x T, and "
      "T = alpha_end / (g - beta_end). The ECA premium inside each month is removed algebraically: draw = g X / (1 - 10.85% x 30% x g). "
      f"At the 75% gearing cap the closed form gives T = {f2(Z['total_funding_at_75pct_closed_form'])}.")
    a(f"* Sculpting with tax: CFADS depends on tax, which depends on interest and the shareholder-loan path. Python iterates profile -> "
      f"model -> CFADS -> constant-DSCR re-sculpt to USD 1,000 on every installment: {it['fc_sizing_passes']} passes at financial close, "
      f"{it['cod_resculpt_passes']} for the COD re-sculpting, {it['bond_sculpt_passes']} for the 2025 bond. The workbook carries the "
      "converged profiles on the Inputs sheet as contractual schedules (after financial close they are contract terms) and recomputes the "
      "sculpted profile live on the Debt sheet; the Checks sheet reports live minus contract (0.000).")
    a('* The workbook contains no circular reference and needs no iterative calculation or macro. A pasted-value Converge macro is the '
      'alternative the book may teach; it is not needed to run this workbook.')
    a('')
    a('## 4. Actual history (scenario 15)')
    a('')
    p18 = P['P-F18']
    a(f"Construction: hard-cost overrun {f2(p18['uses']['hard_cost_overrun_total'])} ({f2(p18['uses']['of_which_bible_items'])} Case Bible items plus {f2(p18['uses']['of_which_delay_related_added'])} delay-related costs in seven named categories, P-C43); FX forward settlements (gain) {f2(P['P-F66']['settlements_total'])}. "
      f"Total funding {f2(p18['uses']['total'])} against {f2(p18['fc_base_comparison']['total_funding_fc'])} at FC. "
      f"Hard-cost overrun 39.27 against contingency 38.40; KCR depreciation reduced the onshore EPC cost by {f2(p18['uses']['epc_fx_gain_on_onshore'])}; "
      f"loan interest, swap and PRI in construction {f2(p18['fc_base_comparison']['idc_actual'])} against {f2(p18['fc_base_comparison']['idc_fc'])} at FC. "
      f"Undrawn senior commitment cancelled {f2(p18['sources']['undrawn_commitment_cancelled'])}; standby drawn {f2(p18['sources']['standby_drawn'])}; "
      f"contingent equity {f2(p18['sources']['contingent_equity_drawn'])}; delay LDs and DSU ({f2(10.1393 + 7.0804)}) applied to construction before the standby facility.")
    a('')
    p21 = P['P-F21']
    a(f"Crisis: historic DSCR {p21['historic_dscr_2022_12_31']:.2f}x at December 31, 2022 (lock-up), {p21['historic_dscr_2023_06_30']:.2f}x at "
      f"June 30, 2023 (event of default; DSRA drawn {f2(p21['dsra_draw_2023_06_30'])}), waiver fee {f2(p21['waiver_fee'])}, margin uplift cost "
      f"{f2(p21['margin_uplift_cost_total'])}, deferred principal {f2(p21['deferred_principal_2023_12_31'])}, lock-up released {p21['release_period']}.")
    p23 = P['P-F23']
    a(f"Refinancing June 30, 2025: prepaid {f2(p23['prepaid_principal'])}; swap unwind receipt {f2(p23['swap_unwind_receipt'])}; bond face "
      f"{f2(p23['bond_face'])}; transaction costs incl. OID {f2(p23['transaction_costs_total'])}; combined sculpted DSCR {p23['combined_dscr_sculpted']:.2f}x.")
    p24 = P['P-F24']
    a(f"Sale: equity value at December 31, 2025 {f2(p24['equity_value_100pct_at_13_75'])} at 13.75% and {f2(p24['equity_value_100pct_at_12_50'])} at 12.50%; "
      f"price for 24% at completion {f2(p24['price_at_completion'])}; indirect transfer tax {f2(p24['indirect_transfer_tax'])}; Kilnworth IRR on the sold stake "
      f"{pc(p24['kilnworth_irr_on_sold_stake'])}.")
    a('')
    a('## 5. Returns, sensitivities and breakevens (FC base)')
    a('')
    p16 = P['P-F16']
    a(f"Equity IRR {pc(p16['equity_irr'])} (project-company level from the LNTP date, before shareholder withholding; "
      f"{pc(p16['equity_irr_incl_development'])} including development spend and its reimbursement); project IRR {pc(p16['project_irr_post_tax'])} post-tax, "
      f"{pc(p16['project_irr_pre_tax'])} pre-tax; equity NPV at 16.0% {f2(p16['equity_npv_at_16pct_at_fc'])}; payback {p16['payback_date']}.")
    a('')
    a(table([[k, fx(v['min_dscr']), fx(v['avg_dscr']), pc(v['equity_irr'])] for k, v in p16['sensitivities'].items()],
            ['Case', 'Min DSCR', 'Avg DSCR', 'Equity IRR']))
    a('')
    a(f"Breakevens (debt locked): availability {p16['breakeven_availability_shift_points']:.1f} points below profile for a 1.00x minimum DSCR; "
      f"capacity charge cut {p16['breakeven_capacity_charge_cut_pct']:.1f}%; DSRA plus LC cover {p16['months_zero_payment_covered_paying_gas']:.1f} months of zero "
      f"SEKA payment if gas is paid, {p16['months_zero_payment_covered_gas_deferred']:.1f} months if gas payments are deferred.")
    a('')
    a('## 6. Assumption changes and interpretations')
    a('')
    a(table([
        ['A1', 'Cash effect of SEKA arrears (actual history)', 'Not specified (read literally, the full overdue increase hits cash)',
         '80% of overdue amounts are energy-charge arrears matched by deferred payments to SNHK and GCK (state gas chain), formalized by the June 2023 netting agreement; 20% hits cash',
         'Read literally the path gives a June 2023 historic DSCR near 0.0x and an event of default at December 2022, against the Bible design range of 0.80x to 1.00x for June 2023. With A1: 1.14x at December 2022 (lock-up), 0.97x at June 2023 (default), DSRA pays the June 2023 shortfall, as the storyline requires. Modeler calibration, pre-publication.'],
        ['A12', 'Construction overrun (actual, P-C43, modeler assumption)', 'USD 39.27m hard-cost overrun; standby and contingent equity not drawn',
         f"Plus USD {P['P-F18']['uses']['of_which_delay_related_added']:.2f}m delay-related costs in seven named categories (Section 8b), Months 34-40", 'Editor ruling: Chapters 31 and 61 teach the standby facility; drawn about USD 10.0m with contingent equity about 3.3m after contingency, delay LDs, DSU and FX gains.'],
        ['A13', 'Construction FX hedge (D-114)', 'None', 'Forwards with Castellan buying KCR for 75% of onshore EPC payments at covered-parity rates (13.5% vs FC LIBOR); actual run only (FC base budgets onshore at the FC spot)', 'Standards require currency hedging; P-F65, P-F66. The forwards gained (forward points about 10% a year against about 5% actual depreciation).'],
        ['A14', 'SEKA LC amount (P-C44)', 'USD 33.8m in 2022; drawing USD 33.8m', 'USD 36.2m (2022 reset on the annex 1.1.5 formula); drawing February 2023 USD 36.6m (2023 reset)', 'Editor ruling: model value wins; the overdue path stays as given (already net of the drawing).'],
        ['A15', 'Halbeck RBL logic (P-F59, Illustrative)', 'Field sold 150 MMscfd; NPV after remaining capex', 'Sales capped at contracted demand (about 106 MMscfd); 40% reserve tail; completion-basis NPV excluding capex funded by the facility', 'Editor ruling: logic check; inputs unchanged.'],
        ['A10', 'Actual 2022 dispatch (annex 4.11, P-C32)', '76.5%', '84.0% (2022H1), 81.5% (2022H2); 76.5% from 2023', 'Annex; changes actual-history 2022 energy, fuel and VOM revenue, gas volumes, LTSA EOH.'],
        ['A11', 'LTSA EOH scaling', 'Hours scale with availability only', 'Hours scale with availability and with dispatch relative to 76.5% (starts fixed); 8,439 EOH a year per unit at base', 'Annex 1.5 and P-F48; no change in the FC base; FC banking and the dispatch sensitivity change slightly.'],
        ['A2', 'FC downside dispatch', 'Plant input lists 58.0% downside dispatch; the 1.10 definition omits dispatch',
         'Downside uses base dispatch 76.5% with availability -6.5 points, heat rate +1.5%, fixed opex +10%',
         'Confirmed by annex 3.7 (P-C25): 58.0% is the low-dispatch gas case only.'],
        ['A3', 'Thin capitalization 3:1', 'Rule application undefined', 'Shareholder loans count as related-party debt; equity = share capital + positive retained earnings; deductible share = min(1, 3 x equity / SHL)',
         'Adopted as Kessaran law in annex 4.15; excess interest permanently non-deductible.'],
        ['A4', 'ECA first-repayment test', '6 months after COD', '24 months after the starting point (OECD project finance terms in force in 2018)',
         'Annex 3.6 (P-C23): within 24 months with at least 2% repaid; FC base and actual both pass.'],
        ['A5', '6M USD LIBOR, July 2016 (P-F03 only)', 'Not in inputs', '0.95% (approximate)', 'Annex 4.7 with 2016 margins and fees; fact-check before printing.'],
        ['A6', 'Sensitivity timing', 'Not specified', 'Devaluation, conversion lag, SEKA payment delay and base-rate shift start 2022H1; payment delay and lag apply to capacity and VOM charges (pass-through energy charges matched by deferred gas payables, as A1); capex +10% excludes development costs and fee; COD delay re-grossed pro rata', 'Modeler definitions.'],
        ['A7', 'COD re-forecast macro', 'Not specified', 'Actual history to 2021H2, FC assumptions after (US CPI 2.2%, Kessara CPI 7.5%, FC forward LIBOR, FX at the inflation differential)', 'Lenders\' view at COD.'],
        ['A8', 'Overrun item timing', 'Amounts only', 'Timing per month in `case_p.OVERRUN_TIMING`', 'Amounts unchanged (39.27).'],
        ['A9', 'Onshore EPC price', 'Fixed in KCR at 519.4', 'FC base budgets it at USD 82.67; the actual run converts the KCR price at actual FX', 'Gives a KCR-depreciation saving in the actual run.'],
    ], ['#', 'Item', 'Old', 'New', 'Reason']))
    a('')
    a('Editor rulings applied in v1.2: standby drawn in range (P-C43); equity IRR gap explained by P-F64; LC model value adopted (P-C44); Halbeck RBL logic corrected (P-F59; signing about 281 and 2023 about 363; the annex expectation is revised to these values in v1.3, P-C46); IFRIC 12 loss against lenders\' basis gain kept; COD re-sculpt 1.31x rising to 1.35x after the LD prepayment kept (P-F19).')
    a('')
    a('## 7. Modeling conventions (stated once; adopt centrally)')
    a('')
    for t_ in [
        'Accounting basis (P-F04, P-F45, proposed for central adoption): IFRS, USD functional currency (revenue and debt are USD-denominated). For simplicity the model presents the plant as property, plant and equipment. A BOOT PPA with a state utility that fixes the tariff and takes the plant for USD 1 at expiry may fall within IFRIC 12 (financial-asset model, given the availability-based capacity payments) or contain a lease under IFRS 16; either treatment changes the balance-sheet presentation and revenue recognition, not the cash flows, CFADS, ratios or returns. Book depreciation: straight line over the 25-year PPA term to nil at transfer. Capitalized cost = all construction uses (incl. IDC, fees, ECA premium, development fee, capitalized SHL interest) less DSRA funding and initial working capital, less delay LDs, DSU proceeds and performance LDs received. Receivables at amortized cost; no expected-credit-loss provision is modeled.',
        'Deferred tax: 30% of (book value of plant - tax written-down value - deferred depreciation pool).',
        'Tax: paid in the period computed; holiday by operating-month bands (OY1-OY5 exempt, OY6-OY8 15%, then 30%); depreciation of holiday months deemed deferred and used against later positive results; minimum turnover tax 0.5% of non-fuel revenue from OY6; tax = max(CIT, MTT); losses carried forward (none arise in any scenario); interest limitation 30% of tax EBITDA not binding because all loans and the 2025 bond are grandfathered.',
        'CFADS = revenue - operating costs - tax paid - increase in working capital - MMRA contributions + MMRA releases (MMRA inside CFADS); DSRA flows excluded; late payment interest received is revenue.',
        'Debt service = interest (incl. WHT gross-up) + swap net settlement + PRI premium + PCG fee + scheduled principal; one-off waiver fee excluded from DSCR.',
        'LLCR = (PV of CFADS to final maturity at the period all-in senior cost + DSRA balance) / senior debt outstanding. Average DSCR = sum of CFADS / sum of debt service over the loan life. Gearing = senior debt / total funding requirement.',
        'Waterfall order: CFADS (+ lock-up and trapped cash brought forward) -> senior interest, swap, premiums and fees -> scheduled principal -> DSRA drawing if short -> DSRA top-up or release -> handback reserve (from OY20) -> distribution test -> soft mini-perm sweep (50% from 2027, commercial tranche) or lock-up account -> SHL interest -> SHL principal -> dividends within distributable reserves -> trapped cash.',
        'Distribution test in the waterfall: first repayment made, historic 12-month DSCR >= 1.20x, DSRA at target, no uncured default, and (actual history) the waiver release condition. Projected DSCR and LLCR are reported on the Ratios sheet but not wired into the waterfall (they would close a loop through tax). Check: with the LLCR defined incl. the DSRA (book convention) no scenario breaches the 1.25x LLCR lock-up in a period where distributions are made; the projected 12-month DSCR (perfect foresight) would have locked up the actual-history distribution of June 30, 2022, one period before the historic test did.',
        'Prepayments (LDs, sweeps) reduce remaining installments pro rata (scheduled principal = balance x installment share of the remaining profile); the swap notional is not reduced by prepayments.',
        'Interest on reserve, lock-up and trapped cash balances: nil.',
        'Major maintenance outside the LTSA is spent in the period containing month 7 of OY4, 8, 12, 16, 20, 24; the MMRA collects one sixth in each of the six periods before.',
        'DSRA target: next period scheduled debt service on balances after this period\'s scheduled payment and non-cash-dependent prepayments.',
        'Swap floating leg equal to the loan base rate (LIBOR to 2022, Term SOFR + 0.42826% from 2023); LIBOR/SOFR basis in H1 2023 ignored.',
    ]:
        a('* ' + t_)
    a('')
    a('## 8b. Version 1.3 (editor fixes, October 3, 2026)')
    a('')
    p64 = P['P-F64']
    a(f"P-F64 is now a sequential attribution from the reconstructed bid model ({p64['bid_irr'] * 100:.2f}%) to the FC base ({p64['fc_irr'] * 100:.2f}%), in the order shown; each step re-sizes the debt; the steps sum to {p64['sum_of_steps_pp']:+.2f} pp, the full gap, with no residual and no interaction line. The bid model's swapped base rate is the one undocumented bid input; it is solved at {p64['reconstructed_bid_swapped_rate_pct']:.2f}% flat so that the reconstruction returns 16.0% (modeler reconstruction, a conservative bid-stage rate). The 2016 indicative terms are annex 4.7 (margins 1.50/3.90/3.75/4.50, upfront fees ECA 1.25 and commercial 2.50, ECA premium 11.5%; A- and B-loan upfront fees as at FC).")
    a('')
    a(table([[s_['step'], f"{s_['cumulative_irr'] * 100:.2f}%", f"{s_['change_pp']:+.2f}", f"{s_['gearing'] * 100:.1f}%"] for s_ in p64['steps']], ['Step', 'Equity IRR', 'Change (pp)', 'Gearing']))
    a('')
    cats = P['P-F18']['uses']['delay_related_added_by_category']
    a(f"P-C43 is no longer a single calibration line: the USD {P['P-F18']['uses']['of_which_delay_related_added']:.2f}m is split into named cost categories (modeler assumptions consistent with Chapter 61), each incurred evenly over Months 34 to 40, so every downstream figure is unchanged.")
    a('')
    a(table([[c['name'], f2(c['usd_m'])] for c in cats.values()] + [['Total', f2(sum(c['usd_m'] for c in cats.values()))]], ['Category', 'USD m']))
    a('')
    a('Halbeck RBL (P-F59): the model result is accepted (signing about USD 281m, 2023 redetermination about USD 363m); case-bible-annex-p.md 4.13 is updated (P-C46).')
    a('')
    a('## 8a. Version 1.2 (editor rulings, October 3, 2026)')
    a('')
    a('P-C43 delay-related overrun (named categories from v1.3); D-114 construction FX hedge (P-F65, P-F66); P-F64 bid-to-close IRR bridge; P-C44 LC; RBL logic (P-F59); all hard-coded constants moved to Inputs and Time (scan_hardcodes_p.py: 0 literals); deferred-principal repayment now dfo / remaining repayment dates (same values); bond face carried as a row (no column-specific formulas). Ledger values that changed: every actual-history figure (P-F04, P-F18 to P-F26, P-F29, P-F31, P-F37 to P-F40, P-F46, P-F51 to P-F54, P-F56, P-F58, P-F63) through the larger overrun, the standby drawing and the FX hedge; FC figures unchanged except P-F16 months covered (annex LC formula).')
    a('')
    a('## 8. Annex P absorption (case-bible-annex-p.md and case-p-input-requests.md)')
    a('')
    a('Model version 1.1. Priority A items: 2 ECA test (absorbed; P-F09 adds the 2% test, values unchanged); 6 actual 2022 dispatch (absorbed, key `case_p.ACT_DISPATCH`, workbook row Operations disp; changes P-F04, P-F18 to P-F25, P-F40, P-F46, P-F58 and every actual-history ledger value slightly); 13 termination definitions (absorbed: the model already used them; P-F25 changes only through item 6); 19 and 20 development fee and premium split (absorbed in P-F49; project-company figures unchanged); 39 IFRIC 12 (absorbed as P-F56; lenders\' basis unchanged); 42 retained 36% fair value at the sale price per point and hedge-reserve recycling (absorbed; P-F26 recomputed). Priority B items absorbed as new figures P-F46 to P-F63 (rules stated in each ledger row); item 16 PRI premium accrues with each period rather than semiannually in advance (different timing rule, same amounts by period); item 37 equity cure computed on the 12-month historic test; item 43 Pillar Two on the simplified basis (top-up nil in 2024 and 2025 because GloBE income is below the substance carve-out). Priority C items confirmed: 1 (policy rates; 2016 and 2017 not used by the model), 3, 4, 5, 7 (GSA and GTA charges continue after 2043 as pass-through), 10, 11, 17, 18, 22 (no receivable booked for the grid claim), 23 to 26.')
    a('')
    a('## 9. Python-only figures')
    a('')
    a('Computed in `case_p.py` only (not in the workbook): P-F01 (inputs), P-F03, P-F05, P-F06, P-F17 (sizing runs; the seeded errors are also in '
      '`Case_P_Model_AuditExercise.xlsx`), P-F19 variants, P-F23 equity PV gain, P-F24, P-F25, P-F26, P-F27, P-F29, P-F31, P-F32, P-F33, '
      'P-F36, P-F42 (Monte Carlo), P-F43 equity-first variant, breakevens in P-F16, P-F64 bridge, P-F66 MTM, and P-F46 to P-F63 (annex figures, derived from the verified runs or from annex inputs). All other figures are reproduced by the workbook '
      '(scenario switch) and verified in `case_p_verification.md`.')
    open(path, 'w').write('\n'.join(L) + '\n')
