# Case P workbook verification

Model version 1.3. Method. `model/verify_p.py` builds `Case_P_Model.xlsx` with the scenario selector set to each of the 15 scenarios, recalculates every copy with LibreOffice 24.2 headless using a private user profile (`soffice -env:UserInstallation=file:///tmp/lo_profile_case_p --headless --calc --convert-to xlsx`) into `model/recalc_p/out/`, reads the recalculated values with openpyxl (`data_only=True`) and compares them with the Python mirror (`case_p.py`) row by row: every mapped calculation row over all its columns (monthly or semiannual) and every mapped scalar. Tolerance: 0.01 in displayed units (USD m for amounts, x for ratios, percentage points for IRRs). The workbook has no circular references and no macros; iterative calculation is off.

## Results by scenario

| Scenario | Name | Rows and scalars compared | Failures | Largest absolute difference | Workbook checks (0 = pass) | Result |
|---|---|---|---|---|---|---|
| 1 | FC base | 281 | 0 | 5.03e-08 | 0 | PASS |
| 2 | FC banking | 281 | 0 | 4.84e-08 | 0 | PASS |
| 3 | FC downside | 281 | 0 | 5.22e-08 | 0 | PASS |
| 4 | Sens: availability -3 points | 281 | 0 | 5.03e-08 | 0 | PASS |
| 5 | Sens: heat rate +2% | 281 | 0 | 5.22e-08 | 0 | PASS |
| 6 | Sens: fixed opex +10% | 281 | 0 | 5.03e-08 | 0 | PASS |
| 7 | Sens: capex +10% funded pro rata | 281 | 0 | 5.03e-08 | 0 | PASS |
| 8 | Sens: COD delay 6 months, no LDs | 281 | 0 | 5.03e-08 | 0 | PASS |
| 9 | Sens: base rate +200 bps (unhedged) | 281 | 0 | 5.03e-08 | 0 | PASS |
| 10 | Sens: KCR devaluation 40%, 90-day lag | 281 | 0 | 5.03e-08 | 0 | PASS |
| 11 | Sens: SEKA pays 120 days late for 12 months | 281 | 0 | 5.03e-08 | 0 | PASS |
| 12 | Sens: dispatch 50% | 281 | 0 | 6.52e-09 | 0 | PASS |
| 13 | Sens: gas price +30% | 281 | 0 | 5.03e-08 | 0 | PASS |
| 14 | COD re-forecast (2021 lenders case) | 280 | 0 | 4.84e-08 | 0 | PASS |
| 15 | Actual history | 280 | 0 | 4.84e-08 | 0 | PASS |
| audit copy | Case_P_Model_AuditExercise.xlsx (FC base, errors E1-E10 seeded) | 281 | 0 | 5.03e-08 | 1 | PASS (the one failing check is the intended audit clue: debt above the correct gearing cap) |

## Key outputs, Python against workbook (selected scenarios)

| Scenario | Output | Python | Workbook | Difference |
|---|---|---|---|---|
| 1 | Total funding requirement | 855.0897 | 855.0897 | 1.51e-10 |
| 1 | Senior debt (four tranches) | 633.2560 | 633.2560 | 2.26e-10 |
| 1 | Minimum DSCR | 1.3500 | 1.3500 | 7.49e-11 |
| 1 | Average DSCR (debt-service weighted) | 1.5382 | 1.5382 | 3.62e-10 |
| 1 | LLCR at first debt service period (incl. DSRA) | 1.4191 | 1.4191 | 2.05e-10 |
| 1 | PLCR at first debt service period | 1.8597 | 1.8597 | 3.99e-10 |
| 1 | Equity IRR | 13.2662% | 13.2662% | 1.21e-09 pp |
| 1 | Project IRR, post-tax | 10.9610% | 10.9610% | 2.38e-08 pp |
| 1 | Equity NPV at 16.0% (at FC) | -43.0674 | -43.0674 | 4.43e-10 |
| 3 | Total funding requirement | 855.0897 | 855.0897 | 1.51e-10 |
| 3 | Senior debt (four tranches) | 633.2560 | 633.2560 | 2.26e-10 |
| 3 | Minimum DSCR | 1.2004 | 1.2004 | 1.88e-10 |
| 3 | Average DSCR (debt-service weighted) | 1.3763 | 1.3763 | 1.23e-10 |
| 3 | LLCR at first debt service period (incl. DSRA) | 1.3061 | 1.3061 | 7.91e-11 |
| 3 | PLCR at first debt service period | 1.7178 | 1.7178 | 1.49e-10 |
| 3 | Equity IRR | 11.3605% | 11.3605% | 3.34e-09 pp |
| 3 | Project IRR, post-tax | 10.0651% | 10.0651% | 2.86e-08 pp |
| 3 | Equity NPV at 16.0% (at FC) | -73.6294 | -73.6294 | 2.05e-10 |
| 15 | Total funding requirement | 885.6322 | 885.6322 | 4.57e-10 |
| 15 | Senior debt (four tranches) | 633.2560 | 633.2560 | 2.26e-10 |
| 15 | Minimum DSCR | 0.9160 | 0.9160 | 4.16e-11 |
| 15 | Average DSCR (debt-service weighted) | 1.4995 | 1.4995 | 4.09e-10 |
| 15 | LLCR at first debt service period (incl. DSRA) | 1.4660 | 1.4660 | 4.69e-10 |
| 15 | PLCR at first debt service period | 1.6955 | 1.6955 | 3.05e-10 |
| 15 | Equity IRR | 12.4956% | 12.4956% | 1.43e-08 pp |
| 15 | Project IRR, post-tax | 10.1333% | 10.1333% | 4.88e-08 pp |
| 15 | Equity NPV at 16.0% (at FC) | -54.5199 | -54.5199 | 7.90e-11 |

## Coverage

Compared rows include: the Time sheet operating months and days; every Construction use line and the VAT facility (KCR) rows; every Funding row (tranche drawdowns, balances, interest by tranche, commitment and upfront fees, ECA premium, DSRA funding, uses, equity, share capital, shareholder loans and capitalized interest, the alpha and beta rows of the closed-form gross-up and the closed-form total funding requirement); Operations macro paths, indices, plant, revenue lines, operating costs, working capital; every Tax row; every Debt tranche corkscrew (interest, scheduled principal, deferral, LD prepayment, refinancing, sweeps, closing balances), the swap, PRI, PCG and waiver fee, debt service and the DSRA target; Reserves (MMRA, DSRA, handback); the full Waterfall (tests, flags, sweeps, shareholder-loan payments, dividends, trapped cash, retained earnings); Financials (income statement, balance sheet and balance check); Ratios (DSCR, LLCR, PLCR); and Returns (equity IRR, project IRRs, NPV). Python-only figures are listed in `case_p_report.md` Section 8.

## Known deviations from the style sheet (not verification failures)

* FAST check (v1.2): `model/scan_hardcodes_p.py` lists every numeric literal inside calculation formulas other than 0, 1, 12 and the unit conversions 100, 1,000 and 1,000,000. Result for Case_P_Model.xlsx: 0. Event dates, period lengths, operating-year bands, day bases, shares and tolerances are named inputs on the Inputs sheet; event flags (Flag_LDPrepayment, Flag_WaiverDeferral, Flag_Refinancing and others) sit on the Time sheet; every calculation row uses one formula copied across (the first column reads the blank column I as the prior period). The audit exercise copy keeps only its deliberate seeded errors (E4 uses 0.5 and 1/12, E9 types 0.765).
* The Inputs sheet holds time-series inputs on the model timelines (semiannual and monthly blocks), not on a separate date header.
