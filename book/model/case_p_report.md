# Case P reference model: report

Model: `model/case_p.py` (Python mirror, source of truth) and `model/Case_P_Model.xlsx` (live-formula workbook built by `model/build_excel_p.py`). Run date October 3, 2026. All amounts USD million unless stated. Figures for the book are cited from `model/figure-ledger-case-p.md` by ID; this report is the modeler's summary.

## 1. Scenarios run

| # | Scenario | Total funding | Senior debt | Min DSCR | Avg DSCR | LLCR (1st DS period) | Equity IRR | Project IRR | Lock-ups |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FC base | 854.6 | 629.9 | 1.35x | 1.55x | 1.42x | 13.2% | 11.0% | 0 |
| 2 | FC banking | 854.6 | 629.9 | 1.35x | 1.55x | 1.42x | 13.1% | 11.0% | 0 |
| 3 | FC downside | 854.6 | 629.9 | 1.20x | 1.38x | 1.30x | 11.3% | 10.1% | 0 |
| 4 | Sens: availability -3 points | 854.6 | 629.9 | 1.32x | 1.54x | 1.42x | 13.1% | 11.0% | 0 |
| 5 | Sens: heat rate +2% | 854.6 | 629.9 | 1.30x | 1.50x | 1.38x | 12.4% | 10.6% | 0 |
| 6 | Sens: fixed opex +10% | 854.6 | 629.9 | 1.32x | 1.52x | 1.40x | 12.7% | 10.7% | 0 |
| 7 | Sens: capex +10% funded pro rata | 935.8 | 689.9 | 1.23x | 1.39x | 1.31x | 11.3% | 10.1% | 0 |
| 8 | Sens: COD delay 6 months, no LDs | 887.5 | 654.2 | 1.25x | 1.45x | 1.35x | 12.0% | 10.4% | 0 |
| 9 | Sens: base rate +200 bps (unhedged) | 854.6 | 629.9 | 1.30x | 1.52x | 1.40x | 12.8% | 11.0% | 0 |
| 10 | Sens: KCR devaluation 40%, 90-day lag | 854.6 | 629.9 | 0.45x | 1.53x | 1.40x | 12.7% | 10.8% | 2 |
| 11 | Sens: SEKA pays 120 days late for 12 months | 854.6 | 629.9 | 0.13x | 1.55x | 1.42x | 13.1% | 10.9% | 2 |
| 12 | Sens: dispatch 50% | 854.6 | 629.9 | 1.34x | 1.54x | 1.41x | 13.0% | 10.9% | 0 |
| 13 | Sens: gas price +30% | 854.6 | 629.9 | 1.35x | 1.55x | 1.42x | 13.2% | 11.0% | 0 |
| 14 | COD re-forecast (2021 lenders case) | 887.4 | 629.9 | 1.28x | 1.51x | 1.34x | 12.3% | 10.1% | 0 |
| 15 | Actual history | 885.2 | 629.9 | 0.91x | 1.50x | 1.47x | 12.4% | 10.1% | 4 |

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
| idc loans | 60.68 |
| swap net during construction | -0.78 |
| pri premium | 3.67 |
| commitment fees | 10.07 |
| upfront fees | 9.90 |
| eca premium | 20.50 |
| agency fees | 0.74 |
| vat facility interest | 1.52 |
| dsra initial | 37.25 |
| total | 854.55 |

| Source of funds | USD m |
|---|---|
| debt ECA | 188.98 |
| debt A | 138.59 |
| debt B | 62.99 |
| debt COM | 239.38 |
| debt total | 629.95 |
| share capital | 44.92 |
| shareholder loans | 179.68 |
| equity total | 224.60 |
| of which lntp credit | 14.20 |
| total | 854.55 |

Binding constraint: **DSCR**. Candidates: gearing cap (75% of the total funding requirement at full gearing, closed form) 643.08; DSCR 1.35x capacity 629.95; downside 1.20x constraint 630.14 (downside minimum DSCR at the sized debt 1.2004x). Gearing achieved 73.7%. LLCR at close (incl. DSRA) 1.4189x, so the 1.40x LLCR test does not bind (excluding the DSRA it would be 1.3598x).

ECA tests (OECD project finance terms in force in 2018): repayment term from COD 13.16 years (max 14); WAL 6.92 years (max 7.25); largest installment 3.8% (max 25%); first repayment 8 months after COD (max 24). All pass. The Case Bible's "first repayment within six months of COD" is not an Arrangement rule (fact sheet t-oecd-pf-2018); it is dropped and the base first repayment stays December 31, 2021.

## 3. Circularity resolution (for Chapters 40 and 42)

* Construction gross-up (IDC, commitment and upfront fees, ECA premium, DSRA): Python iterates the total funding requirement to a tolerance of USD 1,000 (12 passes on the FC base). The workbook solves the same fixed point in closed form on the Funding sheet: each month's balance is carried as alpha_m + beta_m x T, and T = alpha_end / (g - beta_end). The ECA premium inside each month is removed algebraically: draw = g X / (1 - 10.85% x 30% x g). At the 75% gearing cap the closed form gives T = 857.44.
* Sculpting with tax: CFADS depends on tax, which depends on interest and the shareholder-loan path. Python iterates profile -> model -> CFADS -> constant-DSCR re-sculpt to USD 1,000 on every installment: 11 passes at financial close, 4 for the COD re-sculpting, 5 for the 2025 bond. The workbook carries the converged profiles on the Inputs sheet as contractual schedules (after financial close they are contract terms) and recomputes the sculpted profile live on the Debt sheet; the Checks sheet reports live minus contract (0.000).
* The workbook contains no circular reference and needs no iterative calculation or macro. A pasted-value Converge macro is the alternative the book may teach; it is not needed to run this workbook.

## 4. Actual history (scenario 15)

Construction: hard-cost overrun 81.44 (39.27 Case Bible items plus 42.17 delay-related costs in seven named categories, P-C43); FX forward settlements (gain) 4.40. Total funding 885.21 against 854.55 at FC. Hard-cost overrun 39.27 against contingency 38.40; KCR depreciation reduced the onshore EPC cost by 6.72; loan interest, swap and PRI in construction 62.42 against 63.57 at FC. Undrawn senior commitment cancelled 0.00; standby drawn 10.08; contingent equity 3.36; delay LDs and DSU (17.22) applied to construction before the standby facility.

Crisis: historic DSCR 1.12x at December 31, 2022 (lock-up), 0.95x at June 30, 2023 (event of default; DSRA drawn 3.33), waiver fee 1.43, margin uplift cost 4.46, deferred principal 10.85, lock-up released 2024H2.
Refinancing June 30, 2025: prepaid 252.44; swap unwind receipt 6.28; bond face 253.75; transaction costs incl. OID 7.59; combined sculpted DSCR 1.59x.
Sale: equity value at December 31, 2025 325.02 at 13.75% and 356.46 at 12.50%; price for 24% at completion 77.52; indirect transfer tax 5.49; Kilnworth IRR on the sold stake 9.6%.

## 5. Returns, sensitivities and breakevens (FC base)

Equity IRR 13.2% (project-company level from the LNTP date, before shareholder withholding; 13.5% including development spend and its reimbursement); project IRR 11.0% post-tax, 11.6% pre-tax; equity NPV at 16.0% -45.31; payback 2031-06-30.

| Case | Min DSCR | Avg DSCR | Equity IRR |
|---|---|---|---|
| FC base | 1.35x | 1.55x | 13.2% |
| FC banking | 1.35x | 1.55x | 13.1% |
| FC downside | 1.20x | 1.38x | 11.3% |
| Sens: availability -3 points | 1.32x | 1.54x | 13.1% |
| Sens: heat rate +2% | 1.30x | 1.50x | 12.4% |
| Sens: fixed opex +10% | 1.32x | 1.52x | 12.7% |
| Sens: capex +10% funded pro rata | 1.23x | 1.39x | 11.3% |
| Sens: COD delay 6 months, no LDs | 1.25x | 1.45x | 12.0% |
| Sens: base rate +200 bps (unhedged) | 1.30x | 1.52x | 12.8% |
| Sens: KCR devaluation 40%, 90-day lag | 0.45x | 1.53x | 12.7% |
| Sens: SEKA pays 120 days late for 12 months | 0.13x | 1.55x | 13.1% |
| Sens: dispatch 50% | 1.34x | 1.54x | 13.0% |
| Sens: gas price +30% | 1.35x | 1.55x | 13.2% |

Breakevens (debt locked): availability -21.4 points below profile for a 1.00x minimum DSCR; capacity charge cut 25.0%; DSRA plus LC cover 3.0 months of zero SEKA payment if gas is paid, 8.1 months if gas payments are deferred.

## 6. Assumption changes and interpretations

| # | Item | Old | New | Reason |
|---|---|---|---|---|
| A1 | Cash effect of SEKA arrears (actual history) | Not specified (read literally, the full overdue increase hits cash) | 80% of overdue amounts are energy-charge arrears matched by deferred payments to SNHK and GCK (state gas chain), formalized by the June 2023 netting agreement; 20% hits cash | Read literally the path gives a June 2023 historic DSCR near 0.0x and an event of default at December 2022, against the Bible design range of 0.80x to 1.00x for June 2023. With A1: 1.12x at December 2022 (lock-up), 0.95x at June 2023 (default), DSRA pays the June 2023 shortfall, as the storyline requires. Modeler calibration, pre-publication. |
| A12 | Construction overrun (actual, P-C43, modeler assumption) | USD 39.27m hard-cost overrun; standby and contingent equity not drawn | Plus USD 42.17m delay-related costs in seven named categories (Section 8b), Months 34-40 | Editor ruling: Chapters 31 and 61 teach the standby facility; drawn about USD 10.0m with contingent equity about 3.3m after contingency, delay LDs, DSU and FX gains. |
| A13 | Construction FX hedge (D-114) | None | Forwards with Castellan buying KCR for 75% of onshore EPC payments at covered-parity rates (13.5% vs FC LIBOR); actual run only (FC base budgets onshore at the FC spot) | Standards require currency hedging; P-F65, P-F66. The forwards gained (forward points about 10% a year against about 5% actual depreciation). |
| A14 | SEKA LC amount (P-C44) | USD 33.8m in 2022; drawing USD 33.8m | USD 36.2m (2022 reset on the annex 1.1.5 formula); drawing February 2023 USD 36.6m (2023 reset) | Editor ruling: model value wins; the overdue path stays as given (already net of the drawing). |
| A15 | Halbeck RBL logic (P-F59, Illustrative) | Field sold 150 MMscfd; NPV after remaining capex | Sales capped at contracted demand (about 106 MMscfd); 40% reserve tail; completion-basis NPV excluding capex funded by the facility | Editor ruling: logic check; inputs unchanged. |
| A10 | Actual 2022 dispatch (annex 4.11, P-C32) | 76.5% | 84.0% (2022H1), 81.5% (2022H2); 76.5% from 2023 | Annex; changes actual-history 2022 energy, fuel and VOM revenue, gas volumes, LTSA EOH. |
| A11 | LTSA EOH scaling | Hours scale with availability only | Hours scale with availability and with dispatch relative to 76.5% (starts fixed); 8,439 EOH a year per unit at base | Annex 1.5 and P-F48; no change in the FC base; FC banking and the dispatch sensitivity change slightly. |
| A2 | FC downside dispatch | Plant input lists 58.0% downside dispatch; the 1.10 definition omits dispatch | Downside uses base dispatch 76.5% with availability -6.5 points, heat rate +1.5%, fixed opex +10% | Confirmed by annex 3.7 (P-C25): 58.0% is the low-dispatch gas case only. |
| A3 | Thin capitalization 3:1 | Rule application undefined | Shareholder loans count as related-party debt; equity = share capital + positive retained earnings; deductible share = min(1, 3 x equity / SHL) | Adopted as Kessaran law in annex 4.15; excess interest permanently non-deductible. |
| A4 | ECA first-repayment test | 6 months after COD | 24 months after the starting point (OECD project finance terms in force in 2018) | Annex 3.6 (P-C23): within 24 months with at least 2% repaid; FC base and actual both pass. |
| A5 | 6M USD LIBOR, July 2016 (P-F03 only) | Not in inputs | 0.95% (approximate) | Annex 4.7 with 2016 margins and fees; fact-check before printing. |
| A6 | Sensitivity timing | Not specified | Devaluation, conversion lag, SEKA payment delay and base-rate shift start 2022H1; payment delay and lag apply to capacity and VOM charges (pass-through energy charges matched by deferred gas payables, as A1); capex +10% excludes development costs and fee; COD delay re-grossed pro rata | Modeler definitions. |
| A7 | COD re-forecast macro | Not specified | Actual history to 2021H2, FC assumptions after (US CPI 2.2%, Kessara CPI 7.5%, FC forward LIBOR, FX at the inflation differential) | Lenders' view at COD. |
| A8 | Overrun item timing | Amounts only | Timing per month in `case_p.OVERRUN_TIMING` | Amounts unchanged (39.27). |
| A9 | Onshore EPC price | Fixed in KCR at 519.4 | FC base budgets it at USD 82.67; the actual run converts the KCR price at actual FX | Gives a KCR-depreciation saving in the actual run. |

Editor rulings applied in v1.2: standby drawn in range (P-C43); equity IRR gap explained by P-F64; LC model value adopted (P-C44); Halbeck RBL logic corrected (P-F59; signing about 281 and 2023 about 363; the annex expectation is revised to these values in v1.3, P-C46); IFRIC 12 loss against lenders' basis gain kept; COD re-sculpt 1.31x rising to 1.35x after the LD prepayment kept (P-F19).

## 7. Modeling conventions (stated once; adopt centrally)

* Accounting basis (P-F04, P-F45, proposed for central adoption): IFRS, USD functional currency (revenue and debt are USD-denominated). For simplicity the model presents the plant as property, plant and equipment. A BOOT PPA with a state utility that fixes the tariff and takes the plant for USD 1 at expiry may fall within IFRIC 12 (financial-asset model, given the availability-based capacity payments) or contain a lease under IFRS 16; either treatment changes the balance-sheet presentation and revenue recognition, not the cash flows, CFADS, ratios or returns. Book depreciation: straight line over the 25-year PPA term to nil at transfer. Capitalized cost = all construction uses (incl. IDC, fees, ECA premium, development fee, capitalized SHL interest) less DSRA funding and initial working capital, less delay LDs, DSU proceeds and performance LDs received. Receivables at amortized cost; no expected-credit-loss provision is modeled.
* Deferred tax: 30% of (book value of plant - tax written-down value - deferred depreciation pool).
* Tax: paid in the period computed; holiday by operating-month bands (OY1-OY5 exempt, OY6-OY8 15%, then 30%); depreciation of holiday months deemed deferred and used against later positive results; minimum turnover tax 0.5% of non-fuel revenue from OY6; tax = max(CIT, MTT); losses carried forward (none arise in any scenario); interest limitation 30% of tax EBITDA not binding because all loans and the 2025 bond are grandfathered.
* CFADS = revenue - operating costs - tax paid - increase in working capital - MMRA contributions + MMRA releases (MMRA inside CFADS); DSRA flows excluded; late payment interest received is revenue.
* Debt service = interest (incl. WHT gross-up) + swap net settlement + PRI premium + PCG fee + scheduled principal; one-off waiver fee excluded from DSCR.
* LLCR = (PV of CFADS to final maturity at the period all-in senior cost + DSRA balance) / senior debt outstanding. Average DSCR = sum of CFADS / sum of debt service over the loan life. Gearing = senior debt / total funding requirement.
* Waterfall order: CFADS (+ lock-up and trapped cash brought forward) -> senior interest, swap, premiums and fees -> scheduled principal -> DSRA drawing if short -> DSRA top-up or release -> handback reserve (from OY20) -> distribution test -> soft mini-perm sweep (50% from 2027, commercial tranche) or lock-up account -> SHL interest -> SHL principal -> dividends within distributable reserves -> trapped cash.
* Distribution test in the waterfall: first repayment made, historic 12-month DSCR >= 1.20x, DSRA at target, no uncured default, and (actual history) the waiver release condition. Projected DSCR and LLCR are reported on the Ratios sheet but not wired into the waterfall (they would close a loop through tax). Check: with the LLCR defined incl. the DSRA (book convention) no scenario breaches the 1.25x LLCR lock-up in a period where distributions are made; the projected 12-month DSCR (perfect foresight) would have locked up the actual-history distribution of June 30, 2022, one period before the historic test did.
* Prepayments (LDs, sweeps) reduce remaining installments pro rata (scheduled principal = balance x installment share of the remaining profile); the swap notional is not reduced by prepayments.
* Interest on reserve, lock-up and trapped cash balances: nil.
* Major maintenance outside the LTSA is spent in the period containing month 7 of OY4, 8, 12, 16, 20, 24; the MMRA collects one sixth in each of the six periods before.
* DSRA target: next period scheduled debt service on balances after this period's scheduled payment and non-cash-dependent prepayments.
* Swap floating leg equal to the loan base rate (LIBOR to 2022, Term SOFR + 0.42826% from 2023); LIBOR/SOFR basis in H1 2023 ignored.

## 8d. Version 1.5 (ECA tranche in equal installments, D-128; Chapter 36 review, October 3, 2026)

D-128: the OECD Annex VII tests are measured on the ECA-covered tranche's own contractual schedule. In v1.4 every tranche shared one sculpted profile whose contractual WAL from COD was 7.79 years (the 7.18 years printed in P-F09 was measured on principal paid after the commercial sweep). The ECA-covered tranche now repays in 26 equal semiannual installments from 2021H2 to 2034H1: WAL 6.92 years, largest installment 3.8%, first repayment 8 months after COD, term 13.16 years, 11.5% repaid within 24 months; all pass. The A-loan, B-loan and commercial tranches share a sculpted profile so that total scheduled debt service is CFADS / 1.35 in each period (contractual WAL 8.17 years; no OECD limit applies to them). Senior debt falls to 629.95 (DSCR still binds): the ECA tranche, the cheapest, now amortizes faster, so the blended cost of the outstanding debt is higher and the same CFADS supports less debt. Workbook: Debt rows 145 to 150 appended (ECA profile and sculpting helpers); the ECA scheduled principal (row 24), its DSRA-target row (Debt row 119), the Funding DSRA coefficient F12 (ECA), the live sculpting block (rows 127 to 135) and the ECA test rows 137 to 142 now use them; Checks F23 applies in every scenario.

Chapter 36 reconciliation (P-F09): scheduled principal 530.4623 plus the soft mini-perm sweep 99.4873 equals the debt 629.9497. DSCR on scheduled debt service is exactly 1.35x from 2021H2 to 2027H1; from 2027H2 the sweep has reduced the commercial balance, its later installments are its profile share of the reduced balance, so scheduled debt service falls and the DSCR rises, reaching about 2.2x after the commercial tranche is repaid by sweep. The average 1.55x is the debt-service-weighted average of CFADS / scheduled debt service (the term-sheet ratio); with the sweep in the denominator it is 1.39x; without the sweep the profile gives 1.35x. P-F36 now applies all four sizing tests in every row (the 1.30x rows bind on the downside test). Unrounded slack rows in P-F08: downside 0.1883, gearing 13.1317, LLCR 8.4940 (USD m); ECA WAL room 122.1 days. P-F19: the COD re-sculpt holds the debt drawn at COD and the June 30, 2034 maturity; its level DSCR 1.2811x is an output.

## 8c. Version 1.4 (u09 round 1 requests and ledger extensions, October 3, 2026)

Appended rows only; no existing address moved (verified cell by cell against the v1.3 workbook: every v1.3 cell keeps its address and content except Time F16 and Operations rows 31, 37 and 39, which gained a Monte Carlo branch that is inert while Inputs F311 = 0, Checks F8, F13 and F14, suspended while a run is active, Checks F19, extended to the new checks, and four labels). Calendar rows stay where they are (D-047).

| Request | Rows | Content |
|---|---|---|
| R1 | Checks rows 20, 21 | Operating months sum to the PPA term; construction flags sum to construction months; both in master check F19 |
| R2 | Cover row 22 | Master check link to Checks F19, red fill when not 0 |
| R3 | Ratios rows 20, 21 | Projected 12-month DSCR on the next two periods (report only) and a below-lock-up flag |
| R4 | Financials rows 31 to 52; Checks row 22 | Cash flow statement (EBITDA to change in project-account cash, with the MMRA, Compensation Account, bond, unwind, DSRA initial funding and construction LD lines) and the cash check, 0 in every period and scenario |
| R5 | Inputs F311 (run), F312 (active flag), rows 313 to 1312 (draw table, columns J to AL), per-run results pasted in AN to AR; Inputs F1321 (26 shock years) | Hooks: Time F16 (FX drift), Operations rows 31 (availability profile; the shock enters here so the EOH scaling matches P-F42), 37 (dispatch) and 39 (heat rate, degradation term). No native data table (stamped paste, noted on the Cover row 29). Checks F8, F13, F14 are suspended while a run is active |
| R6 | Outputs rows 26 to 42 (pasted table), F44 (compare row); Checks row 25 | Row 24 of Outputs is the existing all-checks line, so the table starts at row 26 |
| R10 | Operations rows 98, 99 | Fuel pass-through test (= P-F47 margin) and GTA pass-through test (0) |
| R11 | Debt rows 137 to 142; Inputs rows 1315 to 1320 (limits); Checks row 23 | WAL, largest installment, term, months to first repayment, share repaid within 24 months from COD; the check applies to Scenario 1 (FC base), where P-F09 is defined; sweeps in other scenarios move the paid profile (Scenario 3: WAL 7.28 years) |
| R12 | Checks row 24 | MMRA window equals the input number of periods |
| R8 | model/exercises/Case_P_Model_AuditExercise_reader.xlsx | Reader copy of the audit exercise without the AuditKey sheet (the other R8 files belong to the build agent) |

Ledger extensions: P-F16 debt capacity at 1.35x by sensitivity (FC base 629.9; lowest 578.2, FC downside); P-F17 annual shadow sizing 615.3 against 629.9 (-14.7, the time-grain effect); P-F49 every Month 1 use itemized (sum 121.52 = total); P-F40 netting set-offs by month July 2023 to June 2025 (total 90.08, all within the 9.0 cap; half-year falls spread evenly because the model is semiannual); P-F63 prepayment cure 81.3 (pro rata, eq:51.3) and 80.2 (proportional, eq:37.4) for 1.10x; P-F65 every monthly forward listed (sum = KCR 32,204 million) with its schedule basis; P-F26 deferred consideration line (nil); labels for D-046 illustrative paths and the P-F02 reconversion proxy.

Monte Carlo funding (P-F42): runs whose construction costs exceed the committed facilities now draw the standby facility and contingent equity 75:25, as the workbook does, instead of drawing senior debt above the commitment; P-F42 percentiles move by less than 0.0001 (no printed value changes).

Build-stage confirmation (Section 0.5 of the u09 brief): the Chapter 40 file must paste Construction row 38 only; the Chapter 41 file must paste Debt rows 103, 104, 110, 112 and Waterfall rows 33 and 43 only; Chapters 39, 42 and 43 paste nothing. With those rows pasted every stage reconciles to the full model on Scenario 1 (largest difference 1e-12; `case_p_verification.md`). Assignment of the v1.4 rows for the build files: Ch 39 Checks 20, 21, Cover 22, Inputs F311, F312 and F1321 (run 0, inert until the draw table is pasted); Ch 41 Operations 98, 99; Ch 42 Financials 30 to 52, Debt 136 to 142, Inputs 1314 to 1320, Checks 22 to 24; Ch 43 Inputs draw table and pasted results (rows 313 to 1312), Ratios 20, 21, Outputs 25 to 44, Checks 25. Inputs row 226 (months per period) is needed in Ch 39 by Time row 21; the u09 row map lists it under both Ch 39 and Ch 41 and should keep Ch 39.

## 8b. Version 1.3 (editor fixes, October 3, 2026)

P-F64 is now a sequential attribution from the reconstructed bid model (16.00%) to the FC base (13.15%), in the order shown; each step re-sizes the debt; the steps sum to -2.85 pp, the full gap, with no residual and no interaction line. The bid model's swapped base rate is the one undocumented bid input; it is solved at 3.38% flat so that the reconstruction returns 16.0% (modeler reconstruction, a conservative bid-stage rate). The 2016 indicative terms are annex 4.7 (margins 1.50/3.90/3.75/4.50, upfront fees ECA 1.25 and commercial 2.50, ECA premium 11.5%; A- and B-loan upfront fees as at FC).

| Step | Equity IRR | Change (pp) | Gearing |
|---|---|---|---|
| Kilnworth bid model, September 2016 (reconstructed; tariff USD 14.36/kW-month) | 16.00% | +0.00 | 75.0% |
| Base rate: reconstructed bid-model swapped rate (flat) replaced by the FC forward curve and the 2.947% swap | 16.50% | +0.50 | 75.0% |
| Debt terms: 2016 indicative margins, upfront fees and ECA premium (annex 4.7) replaced by the FC terms | 16.95% | +0.45 | 75.0% |
| PRI cover on the commercial tranche and the 10% WHT gross-up, added in diligence | 16.06% | -0.89 | 75.0% |
| Soft mini-perm cash sweep from 2027 (FC term sheet) | 15.93% | -0.13 | 75.0% |
| Capex: bid-stage USD 655.0m before financing grows to the FC budget of USD 710.99m (owner's cost, resettlement, contingency) | 14.13% | -1.80 | 75.0% |
| VAT facility interest (omitted from the bid model, annex Kunal Mehrotra) | 14.06% | -0.06 | 74.9% |
| Tax: minimum turnover tax and thin-cap disallowance | 13.98% | -0.08 | 74.7% |
| FX: KCR depreciation on the local tariff shares and costs (bid model held the KCR flat) | 13.20% | -0.79 | 73.7% |
| IRR dating: measured from the February 2018 LNTP payment rather than from financial close | 13.15% | -0.04 | 73.7% |

P-C43 is no longer a single calibration line: the USD 42.17m is split into named cost categories (modeler assumptions consistent with Chapter 61), each incurred evenly over Months 34 to 40, so every downstream figure is unchanged.

| Category | USD m |
|---|---|
| EPC claims settlement: COVID-19 disruption and compensable events beyond the 9.40 variation order (Lindauer, settled at taking-over) | 12.00 |
| Acceleration agreement with Lindauer to hold taking-over at November 2021 after the grid event | 9.50 |
| Extended owner's costs and site team beyond the 6.93 (owner's engineer, site team, security, camp) | 7.20 |
| Re-commissioning after the grid event (repeat backfeed, protection coordination study, OEM field service) | 6.40 |
| Transformer replacement expediting, freight and installation not recovered under the EAR policy | 3.10 |
| Additional IE, lenders' legal and expert-determination costs beyond the 0.86 | 2.35 |
| Operator mobilization and training held seven months longer (O&M contractor standby) | 1.62 |
| Total | 42.17 |

Halbeck RBL (P-F59): the model result is accepted (signing about USD 281m, 2023 redetermination about USD 363m); case-bible-annex-p.md 4.13 is updated (P-C46).

## 8a. Version 1.2 (editor rulings, October 3, 2026)

P-C43 delay-related overrun (named categories from v1.3); D-114 construction FX hedge (P-F65, P-F66); P-F64 bid-to-close IRR bridge; P-C44 LC; RBL logic (P-F59); all hard-coded constants moved to Inputs and Time (scan_hardcodes_p.py: 0 literals); deferred-principal repayment now dfo / remaining repayment dates (same values); bond face carried as a row (no column-specific formulas). Ledger values that changed: every actual-history figure (P-F04, P-F18 to P-F26, P-F29, P-F31, P-F37 to P-F40, P-F46, P-F51 to P-F54, P-F56, P-F58, P-F63) through the larger overrun, the standby drawing and the FX hedge; FC figures unchanged except P-F16 months covered (annex LC formula).

## 8. Annex P absorption (case-bible-annex-p.md and case-p-input-requests.md)

Model version 1.1. Priority A items: 2 ECA test (absorbed; P-F09 adds the 2% test, values unchanged); 6 actual 2022 dispatch (absorbed, key `case_p.ACT_DISPATCH`, workbook row Operations disp; changes P-F04, P-F18 to P-F25, P-F40, P-F46, P-F58 and every actual-history ledger value slightly); 13 termination definitions (absorbed: the model already used them; P-F25 changes only through item 6); 19 and 20 development fee and premium split (absorbed in P-F49; project-company figures unchanged); 39 IFRIC 12 (absorbed as P-F56; lenders' basis unchanged); 42 retained 36% fair value at the sale price per point and hedge-reserve recycling (absorbed; P-F26 recomputed). Priority B items absorbed as new figures P-F46 to P-F63 (rules stated in each ledger row); item 16 PRI premium accrues with each period rather than semiannually in advance (different timing rule, same amounts by period); item 37 equity cure computed on the 12-month historic test; item 43 Pillar Two on the simplified basis (top-up nil in 2024 and 2025 because GloBE income is below the substance carve-out). Priority C items confirmed: 1 (policy rates; 2016 and 2017 not used by the model), 3, 4, 5, 7 (GSA and GTA charges continue after 2043 as pass-through), 10, 11, 17, 18, 22 (no receivable booked for the grid claim), 23 to 26.

## 9. Python-only figures

Computed in `case_p.py` only (not in the workbook): P-F01 (inputs), P-F03, P-F05, P-F06, P-F17 (sizing runs; the seeded errors are also in `Case_P_Model_AuditExercise.xlsx`), P-F19 variants, P-F23 equity PV gain, P-F24, P-F25, P-F26, P-F27, P-F29, P-F31, P-F32, P-F33, P-F36, P-F42 (Monte Carlo), P-F43 equity-first variant, breakevens in P-F16, P-F64 bridge, P-F66 MTM, and P-F46 to P-F63 (annex figures, derived from the verified runs or from annex inputs). All other figures are reproduced by the workbook (scenario switch) and verified in `case_p_verification.md`.
