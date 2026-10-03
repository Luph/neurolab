# Case state by chapter: Case P (Bélanou)

Model version 1.0 (`model/case_p.py`, `model/Case_P_Model.xlsx`); story as of October 3, 2026. For every chapter of Case Bible Part 6 that features Case P: the state of the case at the start and end of the installment (Bible storyline plus modeled state) and the ledger figure IDs (`model/figure-ledger-case-p.md`) the chapter may print. "Inputs" means Case Bible Part 1 values after the change log.

| Ch | Story date | State at start | State at end | Figure IDs the chapter shows | Notes for the writer |
|---|---|---|---|---|---|
| 1 | April 2015 | No project | Origination | Inputs: 2015 peak demand 2,140 MW against 1,780 MW available |  |
| 2 | September 2015 | Opportunity identified | Decision to project-finance | Inputs: development budget USD 14.8 million; target gearing 75% |  |
| 3 | February 2016 (with 1997 to 1999 memory) | RFQ issued | Castellan decides to pursue a mandate | None |  |
| 4 | June 2015 to February 2016 | Origination | Development under way | P-F01; Case P lifecycle timeline (inputs) |  |
| 5 | Flash-forward: January 2022 invoice | Tariff as bid | Indexed tariff for January 2022 | P-F02 | Indices are the September 2021 readings; FX 654.9 (2022H1 average); capacity 581.9 MW applies (reset at taking-over in November 2021). |
| 6 | July 2016; flash-forward to November 2022 | Indicative pricing | Pricing basis understood; transition shown | P-F03, P-F22 | P-F03 uses an approximate July 2016 LIBOR of 0.95% (fact-check). The CAS costs little because 80% of the debt is swapped and the model sets the swap floating leg equal to the loan base rate. |
| 7 | Flash-forward: year to December 31, 2022 | First operating year | Accounts read | P-F04 | IFRS presentation as stated in the ledger; the receivable increase includes USD 18.4 million overdue at June 30 and 68.9 at December 31, 2022; deferred tax is an asset. Do not explain covenants. |
| 8 | 2017 (FC base case) | Bid won | Gearing preference set | P-F05 | Debt is forced to each gearing level on the sculpted profile; at 75% and 80% the minimum DSCR is below 1.35x (the DSCR test binds at 74.1%). |
| 10 | August 2017 | PPA draft received | First markup | Inputs: PPA delay LD USD 94,150 per day, cap USD 25.0 million |  |
| 11 | 2016; 2022 | – | – | Inputs: Part 1.2 table; Part 3.5 capture ratios |  |
| 12 | 2017; 2013 | – | – | Inputs |  |
| 13 | Model build | – | – | Inputs: EPC payment profile |  |
| 14 | October 2016 | Bid submitted | Register v1 | None (qualitative) |  |
| 15 | March 2017 | Register v1 | Risk matrix | None |  |
| 16 | May 2017 | Risk matrix | Mitigation plan | Inputs: LC 33.8, PRG 41.5, contingent equity 15.4, standby 46.0 |  |
| 17 | February 2016 to October 2017 | Tender launched | IA and guarantee signed | P-F25 (formula only) |  |
| 18 | June to October 2017 | Draft PPA | PPA signed | P-F02, P-F32, P-F39 | LC on the PPA formula is about USD 36.6 million at first full-period rates; the Bible states USD 33.8 million for 2022: present 33.8 as the amount issued (estimated charges) and do not print P-F39 unless the editor reconciles. |
| 19 | 2024 | – | – | None |  |
| 21 | 2013 to 2014; 2017 | – | – | T-F05; inputs (GTA) |  |
| 22 | September to December 2017 | EPC draft | EPC signed | P-F33; inputs |  |
| 24 | March to April 2018 | – | LTSA and O&M signed | P-F11, P-F34 | MMRA contributions are inside CFADS. |
| 25 | November 2017 | Draft GSA | GSA signed | P-F35 | Downside dispatch is 76.5% (Bible 1.10 definition); the 50% dispatch sensitivity is the case that triggers take-or-pay. |
| 26 | April 2017 to July 2018 | Two sponsors | Three sponsors | Inputs: stakes, premium USD 4.85 million |  |
| 27 | 2018; 2022 | – | Program bound | Inputs: Part 1.4 insurance table |  |
| 28 | June 2018 | Contracts signed | Gaps logged | None |  |
| 29 | 2017 to 2018; 2014 to 2015 | Mandate | Lender group formed | Inputs: tranche shares; ECA eligible value 263.7 and cap 224.1 |  |
| 30 | 2018; 2024 | – | Bond option alive | None |  |
| 31 | March 2022; 2018 | A1 signing | Holdco funded | R-F05 (holdco lines) |  |
| 32 | 2017 to 2018 | – | Equity committed | P-F07 | Equity lines only. |
| 33 | Early 2025 | – | – | None |  |
| 34 | 2017 | – | PRG approved | Inputs: PRG 41.5, fee 0.75% |  |
| 35 | 2018 (FC base) | – | – | P-F10, P-F08, P-F41 | First full operating year = FY2022 (calendar). LLCR includes the DSRA. |
| 36 | April 2018 | Term sheet agreed | Debt sized | P-F08, P-F09, P-F36 | DSCR (1.35x) binds at USD 633.3 million; gearing cap would allow 642.9; downside 1.20x gives 633.4 (all within 1.5%). ECA first repayment tested at 24 months (2018 OECD terms). |
| 37 | 2018 | – | Reserve and hedge structure set | P-F11, P-F12 | Swap notional accretes with the FC drawdown and amortizes with the contract profile. |
| 38 | 2018 | – | – | P-F12 | Show all-in cost variants with and without PRI, WHT gross-up and financed ECA premium. |
| 39 | Model build | – | – | None |  |
| 40 | Model build (FC base) | – | – | P-F07, P-F13, P-F37, P-F43 | Closed-form gross-up (alpha/beta) is the workbook method; Python iterates. |
| 41 | Model build | – | – | P-F14, P-F32, P-F34, P-F37, P-F38, P-F44 | Thin cap per P-F38 rule. |
| 42 | Model build | – | – | P-F15, P-F41 | Without shareholder loans, up to USD 172.8 million would be trapped. |
| 43 | Model build | – | – | P-F16, P-F42 | Breakevens and Monte Carlo are Python outputs. |
| 44 | June 2018 | Draft model | Audited model | P-F17 | Exercise workbook Case_P_Model_AuditExercise.xlsx carries the ten errors; E9 shows only off the 76.5% dispatch (banking case). |
| 47 | September 2016; August 2014; December 2021 | Bids prepared | Bids won | P-F06 | Levelized tariff USD 73.00/MWh in 2016 prices; runner-up 4.6% higher. |
| 48 | 2018; 2014 | – | – | T-F04; inputs |  |
| 49 | 2018 | – | – | None |  |
| 50 | 2017 to 2021 | – | – | Inputs: RAP 5.08; additional 3.27 |  |
| 51 | 2018 | – | CTA agreed | Inputs: covenant levels |  |
| 52 | 2018; 2023 | – | – | P-F15 (structure) |  |
| 53 | 2018; 2025 | – | ICA signed | Inputs: tranche shares |  |
| 54 | 2017 | – | – | None |  |
| 55 | June to July 2018 | Documents agreed | Financial close | P-F07 | Funds flow at July 17, 2018: Month 1 uses in P-F13. |
| 56 | July to October 2017 | Indicative terms | Agreed term sheet | P-F36 |  |
| 59 | 2022 to 2024 | Plant operating | Settlement signed | P-F20, P-F25, P-F40 | 80% of the overdue amounts are energy-charge arrears matched by deferred SNHK/GCK payables (modeler calibration A1). The DSRA is drawn only at June 30, 2023 (USD 2.5 million). Leave the breach and waiver to Chapter 62. |
| 60 | 2018; 2022 to 2023 | – | – | Inputs: PRI premium 1.15% |  |
| 61 | August 2018 to November 2021 | Financial close | COD December 1, 2021 | P-F18, P-F19, P-F30 | Standby and contingent equity were not drawn (outside the Bible range of 5 to 15): contingency, low 2020-2021 LIBOR and KCR depreciation on the onshore EPC covered the overrun and extra interest. Undrawn senior commitment of USD 6.5 million cancelled; delay LDs and DSU went to operating cash. Editor to confirm the narrative. |
| 62 | 2022 to 2024 | Operating | Waiver in force | P-F21, P-F31 | Historic DSCR 1.14x at December 31, 2022 (lock-up only) and 0.97x at June 30, 2023 (default); release in 2024H2. |
| 63 | 2025 to 2026; 2025 | Pre-refinancing | Refinanced; stake sold | P-F23, P-F24 |  |
| 65 | 2026 looking to 2046; 2026 | – | – | P-F29 |  |
| 66 | 2018 to 2026 | – | – | P-F26 | Simplified loss-of-control computation; framework to be confirmed centrally. |
| 67 | 2017; 2025 | – | – | P-F27, P-F38 |  |
| 68 | 2018; 2015 | – | – | None |  |
| 69 | 2015 to 2016 | – | – | P-F16 |  |
| 72 | 2022 | – | – | Inputs: hydro 640 MW |  |
| 73 | 2023 to 2024 | – | – | R-F07 |  |
| 74 | 2025 | – | – | None |  |
| 75 | 2017; 2023 | – | – | Inputs: reserves 1,140 bcf |  |
| 76 | 2026 | – | – | None |  |
| 77 | 2025 | – | – | None |  |
| 78 | 2026 | – | – | None |  |
| 84 | 2025 | – | – | None |  |
| 85 | September 2016 | – | – | Inputs |  |
| 86 | May 2018 | – | Credit approval | P-F28 |  |
| 87 | 2016 to 2026 | – | – | None |  |

State of Case P at key dates (for chapters that refer back):

| Date | State | Figures |
|---|---|---|
| 2018-07-17 | Financial close: senior debt USD 633.3 million (DSCR-bound), total funding USD 855.1 million, gearing 74.1% | P-F07, P-F08 |
| 2021-05-01 | Scheduled COD (FC base); DSRA USD 37.2 million | P-F11 |
| 2021-12-01 | Actual COD; capacity reset to 581.9 MW; standby not drawn | P-F18, P-F19 |
| 2022-06-30 | First repayment; USD 18.485 million LD prepayment | P-F19, P-F20 |
| 2022-12-31 | Historic DSCR 1.14x: lock-up | P-F20, P-F21 |
| 2023-06-30 | Historic DSCR 0.97x: event of default; DSRA drawn | P-F21, P-F25 |
| 2023-10-26 | Waiver and amendment | P-F21 |
| 2024-12-31 | Lock-up released (2024H2) | P-F20 |
| 2025-06-30 | Bond USD 234.0 million; commercial, B-loan and standby prepaid | P-F23 |
| 2026-09-30 | 24% sold at USD 78.0 million; Kilnworth 36% | P-F24, P-F26 |
