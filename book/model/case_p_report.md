# Case P reference model: report

Model: `model/case_p.py` (Python mirror, source of truth) and `model/Case_P_Model.xlsx` (live-formula workbook built by `model/build_excel_p.py`). Run date October 3, 2026. All amounts USD million unless stated. Figures for the book are cited from `model/figure-ledger-case-p.md` by ID; this report is the modeler's summary.

## 1. Scenarios run

| # | Scenario | Total funding | Senior debt | Min DSCR | Avg DSCR | LLCR (1st DS period) | Equity IRR | Project IRR | Lock-ups |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FC base | 855.1 | 633.3 | 1.35x | 1.54x | 1.42x | 13.3% | 11.0% | 0 |
| 2 | FC banking | 855.1 | 633.3 | 1.34x | 1.53x | 1.41x | 13.1% | 10.9% | 0 |
| 3 | FC downside | 855.1 | 633.3 | 1.20x | 1.38x | 1.31x | 11.4% | 10.1% | 0 |
| 4 | Sens: availability -3 points | 855.1 | 633.3 | 1.32x | 1.53x | 1.42x | 13.2% | 10.9% | 0 |
| 5 | Sens: heat rate +2% | 855.1 | 633.3 | 1.30x | 1.49x | 1.38x | 12.5% | 10.6% | 0 |
| 6 | Sens: fixed opex +10% | 855.1 | 633.3 | 1.32x | 1.51x | 1.40x | 12.8% | 10.7% | 0 |
| 7 | Sens: capex +10% funded pro rata | 936.4 | 693.5 | 1.23x | 1.38x | 1.31x | 11.4% | 10.1% | 0 |
| 8 | Sens: COD delay 6 months, no LDs | 888.2 | 657.7 | 1.25x | 1.45x | 1.35x | 12.1% | 10.4% | 0 |
| 9 | Sens: base rate +200 bps (unhedged) | 855.1 | 633.3 | 1.30x | 1.51x | 1.40x | 12.9% | 11.0% | 0 |
| 10 | Sens: KCR devaluation 40%, 90-day lag | 855.1 | 633.3 | 0.45x | 1.52x | 1.40x | 12.9% | 10.8% | 2 |
| 11 | Sens: SEKA pays 120 days late for 12 months | 855.1 | 633.3 | 0.13x | 1.54x | 1.42x | 13.2% | 10.9% | 2 |
| 12 | Sens: dispatch 50% | 855.1 | 633.3 | 1.29x | 1.48x | 1.37x | 12.4% | 10.5% | 0 |
| 13 | Sens: gas price +30% | 855.1 | 633.3 | 1.35x | 1.54x | 1.42x | 13.3% | 11.0% | 0 |
| 14 | COD re-forecast (2021 lenders case) | 848.4 | 633.3 | 1.31x | 1.54x | 1.38x | 13.3% | 10.5% | 0 |
| 15 | Actual history | 846.5 | 633.3 | 0.94x | 1.53x | 1.50x | 13.4% | 10.5% | 4 |

Senior debt is the committed amount of the four tranches. Scenarios 2 to 6 and 9 to 13 keep the FC base construction and the contractual debt (amount, repayment profile, swap notional); scenarios 7 and 8 re-gross the funding pro rata at the contract debt share. Scenario 14 is the lenders' COD re-forecast (actual construction, no crisis); scenario 15 is the actual history.

## 2. Financial close sizing (FC base)

| Use of funds | USD m |
|---|---|
| epc | 571.84 |
| of which lntp paid before close | 14.20 |
| owners costs | 46.18 |
| insurance during construction | 7.62 |
| development costs and fee | 32.63 |
| lenders advisors | 8.97 |
| contingency | 38.40 |
| initial working capital | 5.35 |
| subtotal before financing | 710.99 |
| idc loans | 60.99 |
| swap net during construction | -0.78 |
| pri premium | 3.69 |
| commitment fees | 10.12 |
| upfront fees | 9.95 |
| eca premium | 20.61 |
| agency fees | 0.74 |
| vat facility interest | 1.52 |
| dsra initial | 37.25 |
| total | 855.09 |

| Source of funds | USD m |
|---|---|
| debt ECA | 189.98 |
| debt A | 139.32 |
| debt B | 63.33 |
| debt COM | 240.64 |
| debt total | 633.26 |
| share capital | 44.37 |
| shareholder loans | 177.47 |
| equity total | 221.83 |
| of which lntp credit | 14.20 |
| total | 855.09 |

Binding constraint: **DSCR**. Candidates: gearing cap (75% of the total funding requirement at full gearing, closed form) 642.91; DSCR 1.35x capacity 633.26; downside 1.20x constraint 633.45 (downside minimum DSCR at the sized debt 1.2004x). Gearing achieved 74.1%. LLCR at close (incl. DSRA) 1.4191x, so the 1.40x LLCR test does not bind (excluding the DSRA it would be 1.3603x).

ECA tests (OECD project finance terms in force in 2018): repayment term from COD 13.16 years (max 14); WAL 7.18 years (max 7.25); largest installment 4.6% (max 25%); first repayment 8 months after COD (max 24). All pass. The Case Bible's "first repayment within six months of COD" is not an Arrangement rule (fact sheet t-oecd-pf-2018); it is dropped and the base first repayment stays December 31, 2021.

## 3. Circularity resolution (for Chapters 40 and 42)

* Construction gross-up (IDC, commitment and upfront fees, ECA premium, DSRA): Python iterates the total funding requirement to a tolerance of USD 1,000 (12 passes on the FC base). The workbook solves the same fixed point in closed form on the Funding sheet: each month's balance is carried as alpha_m + beta_m x T, and T = alpha_end / (g - beta_end). The ECA premium inside each month is removed algebraically: draw = g X / (1 - 10.85% x 30% x g). At the 75% gearing cap the closed form gives T = 857.21.
* Sculpting with tax: CFADS depends on tax, which depends on interest and the shareholder-loan path. Python iterates profile -> model -> CFADS -> constant-DSCR re-sculpt to USD 1,000 on every installment: 11 passes at financial close, 5 for the COD re-sculpting, 5 for the 2025 bond. The workbook carries the converged profiles on the Inputs sheet as contractual schedules (after financial close they are contract terms) and recomputes the sculpted profile live on the Debt sheet; the Checks sheet reports live minus contract (0.000).
* The workbook contains no circular reference and needs no iterative calculation or macro. A pasted-value Converge macro is the alternative the book may teach; it is not needed to run this workbook.

## 4. Actual history (scenario 15)

Construction: total funding 846.53 against 855.09 at FC. Hard-cost overrun 39.27 against contingency 38.40; KCR depreciation reduced the onshore EPC cost by 6.72; loan interest, swap and PRI in construction 62.52 against 63.90 at FC. Undrawn senior commitment cancelled 6.34; standby drawn 0.00; contingent equity 0.00; delay LDs and DSU (17.22) passed to operating cash.

Crisis: historic DSCR 1.14x at December 31, 2022 (lock-up), 0.97x at June 30, 2023 (event of default; DSRA drawn 2.46), waiver fee 1.40, margin uplift cost 4.35, deferred principal 10.77, lock-up released 2024H2.
Refinancing June 30, 2025: prepaid 233.00; swap unwind receipt 6.30; bond face 233.99; transaction costs incl. OID 7.29; combined sculpted DSCR 1.62x.
Sale: equity value at December 31, 2025 327.37 at 13.75% and 358.72 at 12.50%; price for 24% at completion 78.00; indirect transfer tax 6.62; Kilnworth IRR on the sold stake 11.5%.

## 5. Returns, sensitivities and breakevens (FC base)

Equity IRR 13.3% (project-company level from the LNTP date, before shareholder withholding; 13.6% including development spend and its reimbursement); project IRR 11.0% post-tax, 11.6% pre-tax; equity NPV at 16.0% -43.07; payback 2031-06-30.

| Case | Min DSCR | Avg DSCR | Equity IRR |
|---|---|---|---|
| FC base | 1.35x | 1.54x | 13.3% |
| FC banking | 1.34x | 1.53x | 13.1% |
| FC downside | 1.20x | 1.38x | 11.4% |
| Sens: availability -3 points | 1.32x | 1.53x | 13.2% |
| Sens: heat rate +2% | 1.30x | 1.49x | 12.5% |
| Sens: fixed opex +10% | 1.32x | 1.51x | 12.8% |
| Sens: capex +10% funded pro rata | 1.23x | 1.38x | 11.4% |
| Sens: COD delay 6 months, no LDs | 1.25x | 1.45x | 12.1% |
| Sens: base rate +200 bps (unhedged) | 1.30x | 1.51x | 12.9% |
| Sens: KCR devaluation 40%, 90-day lag | 0.45x | 1.52x | 12.9% |
| Sens: SEKA pays 120 days late for 12 months | 0.13x | 1.54x | 13.2% |
| Sens: dispatch 50% | 1.29x | 1.48x | 12.4% |
| Sens: gas price +30% | 1.35x | 1.54x | 13.3% |

Breakevens (debt locked): availability -21.4 points below profile for a 1.00x minimum DSCR; capacity charge cut 25.0%; DSRA plus LC cover 3.0 months of zero SEKA payment if gas is paid, 8.2 months if gas payments are deferred.

## 6. Assumption changes and interpretations

| # | Item | Old | New | Reason |
|---|---|---|---|---|
| A1 | Cash effect of SEKA arrears (actual history) | Not specified (read literally, the full overdue increase hits cash) | 80% of overdue amounts are energy-charge arrears matched by deferred payments to SNHK and GCK (state gas chain), formalized by the June 2023 netting agreement; 20% hits cash | Read literally the path gives a June 2023 historic DSCR near 0.0x and an event of default at December 2022, against the Bible design range of 0.80x to 1.00x for June 2023. With A1: 1.14x at December 2022 (lock-up), 0.97x at June 2023 (default), DSRA pays the June 2023 shortfall, as the storyline requires. Modeler calibration, pre-publication. |
| A2 | FC downside dispatch | Plant input lists 58.0% downside dispatch; the 1.10 definition omits dispatch | Downside uses base dispatch 76.5% with availability -6.5 points, heat rate +1.5%, fixed opex +10% | Follows Case Bible 1.10 and the JSON debt.sizing definition; the 58.0% figure is not used (a 50% dispatch sensitivity exists). |
| A3 | Thin capitalization 3:1 | Rule application undefined | Shareholder loans count as related-party debt; equity = share capital + positive retained earnings; deductible share = min(1, 3 x equity / SHL) | Editor request; share capital alone gives 4:1 at subscription, so a part of SHL interest is disallowed until retained earnings build. |
| A4 | ECA first-repayment test | 6 months after COD | 24 months after the starting point (OECD project finance terms in force in 2018) | Fact sheet t-oecd-pf-2018; the base first repayment (December 31, 2021, 8 months after COD) passes. |
| A5 | 6M USD LIBOR, July 2016 (P-F03 only) | Not in inputs | 0.95% (approximate) | Needed for the 2016 indicative pricing; fact-check before printing. |
| A6 | Sensitivity timing | Not specified | Devaluation, conversion lag, SEKA payment delay and base-rate shift start 2022H1; payment delay and lag apply to capacity and VOM charges (pass-through energy charges matched by deferred gas payables, as A1); capex +10% excludes development costs and fee; COD delay re-grossed pro rata | Modeler definitions. |
| A7 | COD re-forecast macro | Not specified | Actual history to 2021H2, FC assumptions after (US CPI 2.2%, Kessara CPI 7.5%, FC forward LIBOR, FX at the inflation differential) | Lenders' view at COD. |
| A8 | Overrun item timing | Amounts only | Timing per month in `case_p.OVERRUN_TIMING` | Amounts unchanged (39.27). |
| A9 | Onshore EPC price | Fixed in KCR at 519.4 | FC base budgets it at USD 82.67; the actual run converts the KCR price at actual FX | Gives a KCR-depreciation saving in the actual run. |

Outputs outside Case Bible design ranges (reported to the editor-in-chief): standby plus contingent equity drawing 0.0 (range 5 to 15); FC base equity IRR 13.3% against the 16.0% bid target (NPV at 16% negative); COD re-sculpted DSCR 1.31x before the LD prepayment (1.35x minimum after it); LC size 36.6 on the PPA formula against USD 33.8 million stated for 2022.

## 7. Modeling conventions (stated once; adopt centrally)

* Accounting basis (P-F04, P-F45, proposed for central adoption): IFRS, USD functional currency (revenue and debt are USD-denominated). For simplicity the model presents the plant as property, plant and equipment. A BOOT PPA with a state utility that fixes the tariff and takes the plant for USD 1 at expiry may fall within IFRIC 12 (financial-asset model, given the availability-based capacity payments) or contain a lease under IFRS 16; either treatment changes the balance-sheet presentation and revenue recognition, not the cash flows, CFADS, ratios or returns. Book depreciation: straight line over the 25-year PPA term to nil at transfer. Capitalized cost = all construction uses (incl. IDC, fees, ECA premium, development fee, capitalized SHL interest) less DSRA funding and initial working capital, less delay LDs, DSU proceeds and performance LDs received. Receivables at amortized cost; no expected-credit-loss provision is modeled.
* Deferred tax: 30% of (book value of plant - tax written-down value - deferred depreciation pool).
* Tax: paid in the period computed; holiday by operating-month bands (OY1-OY5 exempt, OY6-OY8 15%, then 30%); depreciation of holiday months deemed deferred and used against later positive results; minimum turnover tax 0.5% of non-fuel revenue from OY6; tax = max(CIT, MTT); losses carried forward (none arise in any scenario); interest limitation 30% of tax EBITDA not binding because all loans and the 2025 bond are grandfathered.
* CFADS = revenue - operating costs - tax paid - increase in working capital - MMRA contributions + MMRA releases (MMRA inside CFADS); DSRA flows excluded; late payment interest received is revenue.
* Debt service = interest (incl. WHT gross-up) + swap net settlement + PRI premium + PCG fee + scheduled principal; one-off waiver fee excluded from DSCR.
* LLCR = (PV of CFADS to final maturity at the period all-in senior cost + DSRA balance) / senior debt outstanding. Average DSCR = sum of CFADS / sum of debt service over the loan life. Gearing = senior debt / total funding requirement.
* Waterfall order: CFADS (+ lock-up and trapped cash brought forward) -> senior interest, swap, premiums and fees -> scheduled principal -> DSRA drawing if short -> DSRA top-up or release -> handback reserve (from OY20) -> distribution test -> soft mini-perm sweep (50% from 2027, commercial tranche) or lock-up account -> SHL interest -> SHL principal -> dividends within distributable reserves -> trapped cash.
* Distribution test in the waterfall: first repayment made, historic 12-month DSCR >= 1.20x, DSRA at target, no uncured default, and (actual history) the waiver release condition. Projected DSCR and LLCR are reported on the Ratios sheet but not wired into the waterfall (they would close a loop through tax); none would have triggered a lock-up that the historic test did not.
* Prepayments (LDs, sweeps) reduce remaining installments pro rata (scheduled principal = balance x installment share of the remaining profile); the swap notional is not reduced by prepayments.
* Interest on reserve, lock-up and trapped cash balances: nil.
* Major maintenance outside the LTSA is spent in the period containing month 7 of OY4, 8, 12, 16, 20, 24; the MMRA collects one sixth in each of the six periods before.
* DSRA target: next period scheduled debt service on balances after this period's scheduled payment and non-cash-dependent prepayments.
* Swap floating leg equal to the loan base rate (LIBOR to 2022, Term SOFR + 0.42826% from 2023); LIBOR/SOFR basis in H1 2023 ignored.

## 8. Python-only figures

Computed in `case_p.py` only (not in the workbook): P-F01 (inputs), P-F03, P-F05, P-F06, P-F17 (sizing runs; the seeded errors are also in `Case_P_Model_AuditExercise.xlsx`), P-F19 variants, P-F23 equity PV gain, P-F24, P-F25, P-F26, P-F27, P-F29, P-F31, P-F32, P-F33, P-F36, P-F42 (Monte Carlo), P-F43 equity-first variant, breakevens in P-F16. All other figures are reproduced by the workbook (scenario switch) and verified in `case_p_verification.md`.
