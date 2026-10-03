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
    a(f"Construction: total funding {f2(p18['uses']['total'])} against {f2(p18['fc_base_comparison']['total_funding_fc'])} at FC. "
      f"Hard-cost overrun 39.27 against contingency 38.40; KCR depreciation reduced the onshore EPC cost by {f2(p18['uses']['epc_fx_gain_on_onshore'])}; "
      f"loan interest, swap and PRI in construction {f2(p18['fc_base_comparison']['idc_actual'])} against {f2(p18['fc_base_comparison']['idc_fc'])} at FC. "
      f"Undrawn senior commitment cancelled {f2(p18['sources']['undrawn_commitment_cancelled'])}; standby drawn {f2(p18['sources']['standby_drawn'])}; "
      f"contingent equity {f2(p18['sources']['contingent_equity_drawn'])}; delay LDs and DSU ({f2(10.1393 + 7.0804)}) passed to operating cash.")
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
        ['A2', 'FC downside dispatch', 'Plant input lists 58.0% downside dispatch; the 1.10 definition omits dispatch',
         'Downside uses base dispatch 76.5% with availability -6.5 points, heat rate +1.5%, fixed opex +10%',
         'Follows Case Bible 1.10 and the JSON debt.sizing definition; the 58.0% figure is not used (a 50% dispatch sensitivity exists).'],
        ['A3', 'Thin capitalization 3:1', 'Rule application undefined', 'Shareholder loans count as related-party debt; equity = share capital + positive retained earnings; deductible share = min(1, 3 x equity / SHL)',
         'Editor request; share capital alone gives 4:1 at subscription, so a part of SHL interest is disallowed until retained earnings build.'],
        ['A4', 'ECA first-repayment test', '6 months after COD', '24 months after the starting point (OECD project finance terms in force in 2018)',
         'Fact sheet t-oecd-pf-2018; the base first repayment (December 31, 2021, 8 months after COD) passes.'],
        ['A5', '6M USD LIBOR, July 2016 (P-F03 only)', 'Not in inputs', '0.95% (approximate)', 'Needed for the 2016 indicative pricing; fact-check before printing.'],
        ['A6', 'Sensitivity timing', 'Not specified', 'Devaluation, conversion lag, SEKA payment delay and base-rate shift start 2022H1; payment delay and lag apply to capacity and VOM charges (pass-through energy charges matched by deferred gas payables, as A1); capex +10% excludes development costs and fee; COD delay re-grossed pro rata', 'Modeler definitions.'],
        ['A7', 'COD re-forecast macro', 'Not specified', 'Actual history to 2021H2, FC assumptions after (US CPI 2.2%, Kessara CPI 7.5%, FC forward LIBOR, FX at the inflation differential)', 'Lenders\' view at COD.'],
        ['A8', 'Overrun item timing', 'Amounts only', 'Timing per month in `case_p.OVERRUN_TIMING`', 'Amounts unchanged (39.27).'],
        ['A9', 'Onshore EPC price', 'Fixed in KCR at 519.4', 'FC base budgets it at USD 82.67; the actual run converts the KCR price at actual FX', 'Gives a KCR-depreciation saving in the actual run.'],
    ], ['#', 'Item', 'Old', 'New', 'Reason']))
    a('')
    a('Outputs outside Case Bible design ranges (reported to the editor-in-chief): standby plus contingent equity drawing 0.0 (range 5 to 15); '
      f"FC base equity IRR {pc(p16['equity_irr'])} against the 16.0% bid target (NPV at 16% negative); COD re-sculpted DSCR "
      f"{P['P-F19']['cod_resculpted_dscr']:.2f}x before the LD prepayment ({P['P-F19']['projected_min_dscr_after_prepayment']:.2f}x minimum after it); "
      f"LC size {f1(P['P-F39']['actual_2022H1'])} on the PPA formula against USD 33.8 million stated for 2022.")
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
    a('## 8. Python-only figures')
    a('')
    a('Computed in `case_p.py` only (not in the workbook): P-F01 (inputs), P-F03, P-F05, P-F06, P-F17 (sizing runs; the seeded errors are also in '
      '`Case_P_Model_AuditExercise.xlsx`), P-F19 variants, P-F23 equity PV gain, P-F24, P-F25, P-F26, P-F27, P-F29, P-F31, P-F32, P-F33, '
      'P-F36, P-F42 (Monte Carlo), P-F43 equity-first variant, breakevens in P-F16. All other figures are reproduced by the workbook '
      '(scenario switch) and verified in `case_p_verification.md`.')
    open(path, 'w').write('\n'.join(L) + '\n')
