# Figure ledger: Case P (Bélanou Combined Cycle Power Project)

Source: `model/outputs_case_p.json`, produced by `model/case_p.py` (Case P model v1.5; story as of October 3, 2026); formatted by `model/ledger_p.py` (no computation). Amounts in USD million, nominal, unless stated. Scenario numbers are the workbook scenario switch (1 FC base, 2 FC banking, 3 FC downside, 4-13 sensitivities, 14 COD re-forecast, 15 actual history). P-F01 to P-F36 are the Case Bible register; P-F37 to P-F45 are editor assignments and P-F46 to P-F63 come from case-bible-annex-p.md (P-F11 is split into P-F11a DSRA and P-F11b MMRA). Model version 1.5 (ECA-covered tranche in equal installments, D-128; u09 requests R1 to R12 and ledger extensions absorbed; annex absorbed; editor rulings of October 3, 2026: delay-related overrun categories P-C43, FX hedge D-114, P-F64 to P-F66, sequential P-F64 bridge, RBL expectation revised P-C46). Writers cite the ID; print values in the style-sheet format.

Definitions used throughout: DSCR = CFADS / (interest incl. WHT gross-up + swap net + PRI premium + PCG fee + scheduled principal); average DSCR = sum of CFADS / sum of debt service over the loan life; LLCR = (PV of CFADS to final maturity at the period all-in senior cost + DSRA balance) / senior debt, at the start of the first repayment period; gearing = senior debt / total funding requirement; CFADS = revenue - operating costs - tax paid - increase in working capital - MMRA contributions + MMRA releases. Equity IRR is at project-company level from the LNTP date (February 5, 2018), before shareholder withholding tax.

| ID | Figure | Value | Units | Model run (scenario) | As-of story date |
|---|---|---|---|---|---|
| P-F01 | Development budget approved 2015 | 14.80 | USD m | Inputs | 2015-09 |
| P-F01 | Development costs incurred 2015 | 3.12 | USD m | Inputs | 2018-07-17 |
| P-F01 | Development costs incurred 2016 | 6.87 | USD m | Inputs | 2018-07-17 |
| P-F01 | Development costs incurred 2017 | 7.64 | USD m | Inputs | 2018-07-17 |
| P-F01 | Development costs incurred 2018 | 3.80 | USD m | Inputs | 2018-07-17 |
| P-F01 | Development costs to financial close | 21.43 | USD m | Inputs | 2018-07-17 |
| P-F01 | Overrun against the 2015 budget | 6.63 | USD m | Inputs | 2018-07-17 |
| P-F02 | US CPI index reading for the January 2022 reset (September 2021; Nov 2016 = 100; illustrative path, D-046) | 111.60 | index | Actual history (15) | 2022-01-01 |
| P-F02 | Kessara CPI index reading (September 2021; Nov 2016 = 100) | 149.74 | index | Actual history (15) | 2022-01-01 |
| P-F02 | FX used to reconvert local shares (2022H1 average; proxy for the invoice-date Central Bank mid rate, P-C54) | 654.9 | KCR/USD | Actual history (15) | 2022-01-01 |
| P-F02 | Contracted capacity applying in January 2022 (reset at completion tests) | 581.9 | MW | Actual history (15) | 2022-01-01 |
| P-F02 | Capital charge, indexed (base 14.36) | 14.69 | USD/kW-month | Actual history (15) | 2022-01-01 |
| P-F02 | Fixed O&M charge, indexed (base 2.31) | 2.53 | USD/kW-month | Actual history (15) | 2022-01-01 |
| P-F02 | Total capacity charge, nominal | 17.22 | USD/kW-month | Actual history (15) | 2022-01-01 |
| P-F02 | Total capacity charge in November 2016 dollars (real) | 15.43 | USD/kW-month | Actual history (15) | 2022-01-01 |
| P-F02 | VOM charge, indexed (base 3.86) | 4.24 | USD/MWh | Actual history (15) | 2022-01-01 |
| P-F02 | VOM charge in November 2016 dollars (real) | 3.80 | USD/MWh | Actual history (15) | 2022-01-01 |
| P-F03 | 6M USD LIBOR, July 2016 (approximate; illustrative path, D-046) | 0.95% | % | Annex 4.7 inputs | 2016-07 |
| P-F03 | Indicative 2016 margin, ECA | 1.50% | % | Annex 4.7 inputs | 2016-07 |
| P-F03 | Indicative 2016 margin, A | 3.90% | % | Annex 4.7 inputs | 2016-07 |
| P-F03 | Indicative 2016 margin, B | 3.75% | % | Annex 4.7 inputs | 2016-07 |
| P-F03 | Indicative 2016 margin, COM | 4.50% | % | Annex 4.7 inputs | 2016-07 |
| P-F03 | Indicative all-in floating cost, ECA (LIBOR + margin + upfront fee over 7.0 years + ECA premium 11.5% over 7.0 years) | 4.27% | % pa | Annex 4.7 inputs plus calculation | 2016-07 |
| P-F03 | Indicative all-in floating cost, A (LIBOR + margin + upfront fee over 7.0 years) | 5.03% | % pa | Annex 4.7 inputs plus calculation | 2016-07 |
| P-F03 | Indicative all-in floating cost, B (LIBOR + margin + upfront fee over 7.0 years) | 4.91% | % pa | Annex 4.7 inputs plus calculation | 2016-07 |
| P-F03 | Indicative all-in floating cost, COM (LIBOR + margin + upfront fee over 7.0 years) | 5.81% | % pa | Annex 4.7 inputs plus calculation | 2016-07 |
| P-F03 | Commercial tranche incl. PRI premium and WHT gross-up | 7.45% | % pa | Annex 4.7 inputs plus calculation | 2016-07 |
| P-F03 | Indicative weighted all-in floating cost (30/22/10/38) | 5.09% | % pa | Annex 4.7 inputs plus calculation | 2016-07 |
| P-F04 | FY2022 income statement: revenue | 333.9 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: late payment interest | 0.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: operating costs | 236.9 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: of which fuel and transport | 197.5 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: ebitda | 97.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: depreciation | 33.6 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: finance costs | 61.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: of which shareholder loan interest | 20.8 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: current tax | 0.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: deferred tax | -10.1 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: net income | 12.5 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: ebitda | 97.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: tax paid | 0.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: increase in working capital | 13.9 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: mmra net | 0.9 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: cfads | 82.2 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: senior interest and fees | 40.2 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: senior principal | 33.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: ld prepayment | 18.5 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: sweeps | 0.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: dsra topup less release | 8.7 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: shl interest paid | 0.3 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: shl principal repaid | 0.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: dividends | 0.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: plant | 803.1 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: cash in project accounts | 38.3 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: of which dsra | 37.4 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: receivables | 109.4 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: of which overdue | 68.9 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: inventory | 5.3 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: deferred tax asset | 10.9 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: total assets | 967.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: senior debt | 588.6 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: shareholder loans | 234.8 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: payables | 80.9 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: deferred tax liability | 0.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: share capital | 45.6 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: retained earnings | 17.1 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: total liabilities and equity | 967.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: balance check | 0.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Financing costs capitalized during construction (IDC, fees, ECA premium, VAT interest) | 107.4 | USD m | Actual history (15) | 2021-12-01 |
| P-F04 | Shareholder-loan interest capitalized to COD | 30.2 | USD m | Actual history (15) | 2021-12-01 |
| P-F05 | Equity IRR at 60% gearing | 12.2% | % nominal post-tax | FC base (1), debt set at gearing | 2017 |
| P-F05 | Senior debt at 60% gearing | 495.1 | USD m | FC base (1) | 2017 |
| P-F05 | Minimum DSCR at 60% gearing | 1.71x | x | FC base (1) | 2017 |
| P-F05 | Equity IRR at 65% gearing | 12.5% | % nominal post-tax | FC base (1), debt set at gearing | 2017 |
| P-F05 | Senior debt at 65% gearing | 543.2 | USD m | FC base (1) | 2017 |
| P-F05 | Minimum DSCR at 65% gearing | 1.56x | x | FC base (1) | 2017 |
| P-F05 | Equity IRR at 70% gearing | 12.9% | % nominal post-tax | FC base (1), debt set at gearing | 2017 |
| P-F05 | Senior debt at 70% gearing | 592.5 | USD m | FC base (1) | 2017 |
| P-F05 | Minimum DSCR at 70% gearing | 1.43x | x | FC base (1) | 2017 |
| P-F05 | Equity IRR at 75% gearing | 13.3% | % nominal post-tax | FC base (1), debt set at gearing | 2017 |
| P-F05 | Senior debt at 75% gearing | 643.0 | USD m | FC base (1) | 2017 |
| P-F05 | Minimum DSCR at 75% gearing | 1.32x | x | FC base (1) | 2017 |
| P-F05 | Equity IRR at 80% gearing | 13.8% | % nominal post-tax | FC base (1), debt set at gearing | 2017 |
| P-F05 | Senior debt at 80% gearing | 694.9 | USD m | FC base (1) | 2017 |
| P-F05 | Minimum DSCR at 80% gearing | 1.23x | x | FC base (1) | 2017 |
| P-F06 | Levelized tariff of the winning bid (RFP formula) | 73.00 | USD/MWh (2016 prices) | FC base inputs | 2016-09-27 |
| P-F06 | of which capacity | 32.62 | USD/MWh | FC base inputs | 2016-09-27 |
| P-F06 | of which VOM | 3.86 | USD/MWh | FC base inputs | 2016-09-27 |
| P-F06 | of which fuel | 36.52 | USD/MWh | FC base inputs | 2016-09-27 |
| P-F06 | Runner-up levelized tariff (4.6% higher) | 76.36 | USD/MWh | FC base inputs | 2016-09-27 |
| P-F07 | Use: epc | 571.84 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: of which lntp paid before close | 14.20 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: owners costs | 46.18 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: insurance during construction | 7.62 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: development costs and fee | 32.63 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: lenders advisors | 8.97 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: contingency | 38.40 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: initial working capital | 5.35 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: subtotal before financing | 710.99 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: idc loans | 60.68 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: swap net during construction | -0.78 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: pri premium | 3.67 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: commitment fees | 10.07 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: upfront fees | 9.90 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: eca premium | 20.50 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: agency fees | 0.74 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: vat facility interest | 1.52 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: dsra initial | 37.25 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: total | 854.55 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: debt ECA | 188.98 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: debt A | 138.59 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: debt B | 62.99 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: debt COM | 239.38 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: debt total | 629.95 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: share capital | 44.92 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: shareholder loans | 179.68 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: equity total | 224.60 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: of which lntp credit | 14.20 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: total | 854.55 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Gearing (senior debt / total funding requirement) | 73.7% | % | FC base (1) | 2018-07-17 |
| P-F07 | Shareholder-loan interest capitalized to COD (non-cash) | 24.5 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Shareholder-loan balance at COD | 204.2 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Senior debt, ECA tranche | 189.0 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Senior debt, A tranche | 138.6 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Senior debt, B tranche | 63.0 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Senior debt, COM tranche | 239.4 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Senior debt, total | 629.9 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Binding constraint | DSCR (1.35x) | text | FC base (1) | 2018-07-17 |
| P-F08 | Debt at the 75% gearing cap | 643.1 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Debt capacity at 1.35x | 629.9 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Debt meeting the 1.20x downside | 630.1 | USD m | FC downside (3) | 2018-07-17 |
| P-F08 | Minimum DSCR, base | 1.35x | x | FC base (1) | 2018-07-17 |
| P-F08 | Average DSCR (debt-service weighted), base | 1.55x | x | FC base (1) | 2018-07-17 |
| P-F08 | Minimum DSCR, banking | 1.35x | x | FC banking (2) | 2018-07-17 |
| P-F08 | Average DSCR (debt-service weighted), banking | 1.55x | x | FC banking (2) | 2018-07-17 |
| P-F08 | Minimum DSCR, downside | 1.20x | x | FC downside (3) | 2018-07-17 |
| P-F08 | Average DSCR (debt-service weighted), downside | 1.38x | x | FC downside (3) | 2018-07-17 |
| P-F08 | LLCR at close (PV CFADS + DSRA over debt; first repayment period) | 1.42x | x | FC base (1) | 2018-07-17 |
| P-F08 | LLCR at close excluding DSRA | 1.36x | x | FC base (1) | 2018-07-17 |
| P-F08 | Does the 1.40x LLCR test bind? | No | text | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2021H2 | 15.6 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2022H1 | 16.2 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2022H2 | 17.0 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2023H1 | 17.4 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2023H2 | 18.2 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2024H1 | 18.7 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2024H2 | 19.9 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2025H1 | 20.5 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2025H2 | 19.9 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2026H1 | 19.9 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2026H2 | 20.7 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2027H1 | 21.3 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2027H2 | 22.0 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2028H1 | 22.3 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2028H2 | 23.9 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2029H1 | 24.3 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2029H2 | 24.4 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2030H1 | 23.9 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2030H2 | 23.9 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2031H1 | 23.1 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2031H2 | 22.1 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2032H1 | 19.9 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2032H2 | 19.7 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2033H1 | 20.2 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2033H2 | 17.8 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2034H1 | 17.5 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Repayment structure | ECA-covered tranche: equal semiannual installments 2021H2 to 2034H1 (26); A-loan, B-loan and commercial: sculpted so that total scheduled debt service = CFADS / 1.35 (D-128) | text | FC base (1) | 2018-07-17 |
| P-F09 | ECA-covered tranche installment 2021H2 | 3.8462% | % of the ECA amount | FC base (1) | 2021H2 |
| P-F09 | ECA-covered tranche installment 2022H1 | 3.8462% | % of the ECA amount | FC base (1) | 2022H1 |
| P-F09 | ECA-covered tranche installment 2022H2 | 3.8462% | % of the ECA amount | FC base (1) | 2022H2 |
| P-F09 | ECA-covered tranche installment 2023H1 | 3.8462% | % of the ECA amount | FC base (1) | 2023H1 |
| P-F09 | ECA-covered tranche installment 2023H2 | 3.8462% | % of the ECA amount | FC base (1) | 2023H2 |
| P-F09 | ECA-covered tranche installment 2024H1 | 3.8462% | % of the ECA amount | FC base (1) | 2024H1 |
| P-F09 | ECA-covered tranche installment 2024H2 | 3.8462% | % of the ECA amount | FC base (1) | 2024H2 |
| P-F09 | ECA-covered tranche installment 2025H1 | 3.8462% | % of the ECA amount | FC base (1) | 2025H1 |
| P-F09 | ECA-covered tranche installment 2025H2 | 3.8462% | % of the ECA amount | FC base (1) | 2025H2 |
| P-F09 | ECA-covered tranche installment 2026H1 | 3.8462% | % of the ECA amount | FC base (1) | 2026H1 |
| P-F09 | ECA-covered tranche installment 2026H2 | 3.8462% | % of the ECA amount | FC base (1) | 2026H2 |
| P-F09 | ECA-covered tranche installment 2027H1 | 3.8462% | % of the ECA amount | FC base (1) | 2027H1 |
| P-F09 | ECA-covered tranche installment 2027H2 | 3.8462% | % of the ECA amount | FC base (1) | 2027H2 |
| P-F09 | ECA-covered tranche installment 2028H1 | 3.8462% | % of the ECA amount | FC base (1) | 2028H1 |
| P-F09 | ECA-covered tranche installment 2028H2 | 3.8462% | % of the ECA amount | FC base (1) | 2028H2 |
| P-F09 | ECA-covered tranche installment 2029H1 | 3.8462% | % of the ECA amount | FC base (1) | 2029H1 |
| P-F09 | ECA-covered tranche installment 2029H2 | 3.8462% | % of the ECA amount | FC base (1) | 2029H2 |
| P-F09 | ECA-covered tranche installment 2030H1 | 3.8462% | % of the ECA amount | FC base (1) | 2030H1 |
| P-F09 | ECA-covered tranche installment 2030H2 | 3.8462% | % of the ECA amount | FC base (1) | 2030H2 |
| P-F09 | ECA-covered tranche installment 2031H1 | 3.8462% | % of the ECA amount | FC base (1) | 2031H1 |
| P-F09 | ECA-covered tranche installment 2031H2 | 3.8462% | % of the ECA amount | FC base (1) | 2031H2 |
| P-F09 | ECA-covered tranche installment 2032H1 | 3.8462% | % of the ECA amount | FC base (1) | 2032H1 |
| P-F09 | ECA-covered tranche installment 2032H2 | 3.8462% | % of the ECA amount | FC base (1) | 2032H2 |
| P-F09 | ECA-covered tranche installment 2033H1 | 3.8462% | % of the ECA amount | FC base (1) | 2033H1 |
| P-F09 | ECA-covered tranche installment 2033H2 | 3.8462% | % of the ECA amount | FC base (1) | 2033H2 |
| P-F09 | ECA-covered tranche installment 2034H1 | 3.8462% | % of the ECA amount | FC base (1) | 2034H1 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2021H2 | 1.8901% | % of their amount | FC base (1) | 2021H2 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2022H1 | 2.0291% | % of their amount | FC base (1) | 2022H1 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2022H2 | 2.2003% | % of their amount | FC base (1) | 2022H2 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2023H1 | 2.3051% | % of their amount | FC base (1) | 2023H1 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2023H2 | 2.4786% | % of their amount | FC base (1) | 2023H2 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2024H1 | 2.6031% | % of their amount | FC base (1) | 2024H1 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2024H2 | 2.8744% | % of their amount | FC base (1) | 2024H2 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2025H1 | 3.0080% | % of their amount | FC base (1) | 2025H1 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2025H2 | 2.8718% | % of their amount | FC base (1) | 2025H2 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2026H1 | 2.8634% | % of their amount | FC base (1) | 2026H1 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2026H2 | 3.0439% | % of their amount | FC base (1) | 2026H2 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2027H1 | 3.1769% | % of their amount | FC base (1) | 2027H1 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2027H2 | 3.4032% | % of their amount | FC base (1) | 2027H2 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2028H1 | 3.5687% | % of their amount | FC base (1) | 2028H1 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2028H2 | 4.0498% | % of their amount | FC base (1) | 2028H2 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2029H1 | 4.2979% | % of their amount | FC base (1) | 2029H1 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2029H2 | 4.5077% | % of their amount | FC base (1) | 2029H2 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2030H1 | 4.6201% | % of their amount | FC base (1) | 2030H1 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2030H2 | 4.9394% | % of their amount | FC base (1) | 2030H2 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2031H1 | 5.1404% | % of their amount | FC base (1) | 2031H1 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2031H2 | 5.4759% | % of their amount | FC base (1) | 2031H2 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2032H1 | 5.7172% | % of their amount | FC base (1) | 2032H1 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2032H2 | 6.1742% | % of their amount | FC base (1) | 2032H2 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2033H1 | 6.4209% | % of their amount | FC base (1) | 2033H1 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2033H2 | 5.2460% | % of their amount | FC base (1) | 2033H2 |
| P-F09 | Sculpted profile, A-loan, B-loan and commercial, 2034H1 | 5.0938% | % of their amount | FC base (1) | 2034H1 |
| P-F09 | ECA-covered tranche (contractual schedule): weighted average life from COD | 6.9158 | years (limit 7.25) | FC base (1) | 2018-07-17 |
| P-F09 | ECA-covered tranche: largest installment | 3.8% | % of principal (limit 25%) | FC base (1) | 2018-07-17 |
| P-F09 | ECA-covered tranche: repayment term from COD | 13.1636 | years (limit 14) | FC base (1) | 2018-07-17 |
| P-F09 | ECA-covered tranche: first repayment after COD | 8 | months (limit 24) | FC base (1) | 2018-07-17 |
| P-F09 | Contractual WAL from COD, all tranches / A, B and commercial (no OECD limit) | 7.7932 / 8.1693 | years | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal total (unrounded) | 530.462332 | USD m | FC base (1) | 2021-2034 |
| P-F09 | Cash sweep prepayment total (soft mini-perm, commercial tranche, unrounded) | 99.487343 | USD m | FC base (1) | 2027-2031 |
| P-F09 | Scheduled principal + cash sweep = senior debt | 629.949675 = 629.949675 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Periods with DSCR exactly 1.35x on scheduled debt service | 2021H2, 2022H1, 2022H2, 2023H1, 2023H2, 2024H1, 2024H2, 2025H1, 2025H2, 2026H1, 2026H2, 2027H1 | periods | FC base (1) | 2018-07-17 |
| P-F09 | Average DSCR on scheduled debt service (term-sheet basis) / including the sweep in the denominator / minimum including the sweep | 1.5481 / 1.3855 / 1.1470 | x | FC base (1) | 2018-07-17 |
| P-F09 | Counterfactual without the mini-perm sweep: average / minimum / maximum DSCR | 1.3525 / 1.3500 / 1.4161 | x | FC base (1) without sweep | 2018-07-17 |
| P-F09 | Why the average exceeds 1.35x | The repayment profile is sculpted so that CFADS / scheduled debt service = 1.35x in every period from 2021H2 to 2034H1 on the FC base without sweeps (the profile is a share of the original debt). From 2027 the soft mini-perm sweep (50% of cash available for distribution) prepays the commercial tranche ahead of its schedule; each tranche's later installments are its profile share times its reduced balance, so scheduled debt service falls below CFADS / 1.35 and the period DSCR rises (from 2027H2), and after the commercial tranche is repaid by sweep in 2031H2 only the ECA, A and B tranches remain (2.2x). Scheduled principal plus sweep equals the debt. The 1.54x average is the debt-service-weighted average of CFADS / scheduled debt service (the term-sheet DSCR, which excludes voluntary and sweep prepayments); it is not an average over a different set of periods. Including the sweep in the denominator the average is shown above; without the sweep the profile gives 1.35x in every period. The first period (2021H2, after the two-month COD period) is a full half-year and is at 1.35x. | text | FC base (1) | 2018-07-17 |
| P-F09 | 2021H2: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 50.282 / 37.246 / 15.603 / 0.000 / 1.3500 / 1.3500 / 239.381 | USD m, x | FC base (1) | 2021H2 |
| P-F09 | 2022H1: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 50.162 / 37.157 / 16.216 / 0.000 / 1.3500 / 1.3500 / 234.856 | USD m, x | FC base (1) | 2022H1 |
| P-F09 | 2022H2: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 50.793 / 37.625 / 16.971 / 0.000 / 1.3500 / 1.3500 / 229.999 | USD m, x | FC base (1) | 2022H2 |
| P-F09 | 2023H1: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 50.400 / 37.333 / 17.434 / 0.000 / 1.3500 / 1.3500 / 224.732 | USD m, x | FC base (1) | 2023H1 |
| P-F09 | 2023H2: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 50.964 / 37.751 / 18.198 / 0.000 / 1.3500 / 1.3500 / 219.214 | USD m, x | FC base (1) | 2023H2 |
| P-F09 | 2024H1: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 50.720 / 37.571 / 18.747 / 0.000 / 1.3500 / 1.3500 / 213.281 | USD m, x | FC base (1) | 2024H1 |
| P-F09 | 2024H2: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 51.689 / 38.288 / 19.944 / 0.000 / 1.3500 / 1.3500 / 207.049 | USD m, x | FC base (1) | 2024H2 |
| P-F09 | 2025H1: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 51.331 / 38.023 / 20.533 / 0.000 / 1.3500 / 1.3500 / 200.168 | USD m, x | FC base (1) | 2025H1 |
| P-F09 | 2025H2: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 49.851 / 36.927 / 19.932 / 0.000 / 1.3500 / 1.3500 / 192.968 | USD m, x | FC base (1) | 2025H2 |
| P-F09 | 2026H1: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 49.370 / 36.570 / 19.895 / 0.000 / 1.3500 / 1.3500 / 186.093 | USD m, x | FC base (1) | 2026H1 |
| P-F09 | 2026H2: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 49.776 / 36.871 / 20.691 / 0.000 / 1.3500 / 1.3500 / 179.239 | USD m, x | FC base (1) | 2026H2 |
| P-F09 | 2027H1: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 49.375 / 36.574 / 21.278 / 6.185 / 1.3500 / 1.1547 / 171.953 | USD m, x | FC base (1) | 2027H1 |
| P-F09 | 2027H2: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 49.956 / 36.395 / 21.969 / 7.160 / 1.3726 / 1.1470 / 158.162 | USD m, x | FC base (1) | 2027H2 |
| P-F09 | 2028H1: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 49.751 / 35.507 / 22.292 / 6.818 / 1.4012 / 1.1755 / 143.162 | USD m, x | FC base (1) | 2028H1 |
| P-F09 | 2028H2: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 51.663 / 36.072 / 23.870 / 8.156 / 1.4322 / 1.1681 / 128.515 | USD m, x | FC base (1) | 2028H2 |
| P-F09 | 2029H1: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 51.746 / 35.131 / 24.279 / 8.759 / 1.4729 / 1.1790 / 111.921 | USD m, x | FC base (1) | 2029H1 |
| P-F09 | 2029H2: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 51.907 / 34.060 / 24.369 / 9.641 / 1.5240 / 1.1878 / 94.816 | USD m, x | FC base (1) | 2029H2 |
| P-F09 | 2030H1: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 51.539 / 32.391 / 23.883 / 10.078 / 1.5912 / 1.2136 / 77.162 | USD m, x | FC base (1) | 2030H1 |
| P-F09 | 2030H2: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 52.209 / 31.139 / 23.905 / 11.464 / 1.6766 / 1.2255 / 59.783 | USD m, x | FC base (1) | 2030H2 |
| P-F09 | 2031H1: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 51.801 / 28.844 / 23.082 / 12.367 / 1.7959 / 1.2570 / 41.639 | USD m, x | FC base (1) | 2031H1 |
| P-F09 | 2031H2: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 52.403 / 26.527 / 22.129 / 14.289 / 1.9754 / 1.2839 / 23.822 | USD m, x | FC base (1) | 2031H2 |
| P-F09 | 2032H1: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 52.165 / 22.866 / 19.933 / 4.571 / 2.2813 / 1.9012 / 5.711 | USD m, x | FC base (1) | 2032H1 |
| P-F09 | 2032H2: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 53.276 / 21.834 / 19.715 / 0.000 / 2.4400 / 2.4400 / 0.000 | USD m, x | FC base (1) | 2032H2 |
| P-F09 | 2033H1: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 52.900 / 21.766 / 20.212 / 0.000 / 2.4304 / 2.4304 / 0.000 | USD m, x | FC base (1) | 2033H1 |
| P-F09 | 2033H2: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 44.109 / 18.831 / 17.844 / 0.000 / 2.3424 / 2.3424 / 0.000 | USD m, x | FC base (1) | 2033H2 |
| P-F09 | 2034H1: CFADS / scheduled DS / scheduled principal / sweep / DSCR scheduled / DSCR incl. sweep / commercial opening | 41.633 / 18.023 / 17.537 / 0.000 / 2.3100 / 2.3100 / 0.000 | USD m, x | FC base (1) | 2034H1 |
| P-F08 | Sizing slack (unrounded): downside test 1.20x | 0.188304 USD m; ratio 1.200359x (+0.000359) | USD m, x | FC downside (3) | 2018-07-17 |
| P-F08 | Sizing slack (unrounded): 75% gearing cap | 13.131692 USD m to the closed-form cap 643.081367 (10.964246 at the current total funding); gearing 73.7170% | USD m, % | FC base (1) | 2018-07-17 |
| P-F08 | Sizing slack (unrounded): LLCR 1.40x | 8.493955 USD m; LLCR 1.418877x (+0.018877) | USD m, x | FC base (1) | 2018-07-17 |
| P-F08 | ECA room (unrounded): WAL / tenor | 122.06 days (6.915811 years vs 7.25) / 305.50 days (13.163587 years vs 14) | days | FC base (1) | 2018-07-17 |
| P-F08 | Equal-installment WAL from COD on the FC base repayment dates (2021H2 to 2034H1, 26 installments) | 6.915811 | years | FC base (1) | 2018-07-17 |
| P-F08 | Equal-installment WAL from COD on the actual repayment dates incl. the 2025 bond (2022H1 to 2037H1, 31 installments) | 8.079839 | years | Actual history (15) | 2018-07-17 |
| P-F08 | Equal-installment WAL from COD on the actual bank repayment dates to 2034 (2022H1 to 2034H1, 25 installments) | 6.579822 | years | Actual history (15) | 2018-07-17 |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): capacity payments | 121.1 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): vom | 15.3 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): fuel and transport pass through | 183.9 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): total revenue | 320.3 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): fuel and transport costs | 183.6 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): om fixed | 8.5 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): om incentive | 0.4 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): ltsa fixed | 2.8 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): ltsa variable | 8.9 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): insurance | 4.7 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): g and a | 3.4 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): land | 0.8 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): community and levy | 0.8 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): consumables | 4.3 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): agency | 0.3 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): prg fee | 0.3 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): vat interest | 0.1 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): fx losses | 0.0 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): late payment interest | 0.0 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): major maintenance | 0.0 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): ebitda | 101.5 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): tax | 0.0 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): increase in working capital | 0.3 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): mmra contribution | 0.8 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): mmra release | 0.0 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): cfads | 100.4 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): debt service | 74.4 | USD m | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | FC base first full operating year (2021-07-01 to 2022-06-30 (annex 4.15)): dscr | 1.35x | x | FC base (1) | 2021-07-01 to 2022-06-30 (annex 4.15) |
| P-F10 | Actual first full operating year (calendar 2022): capacity payments | 120.3 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): vom | 16.4 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): fuel and transport pass through | 197.1 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): total revenue | 333.9 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): fuel and transport costs | 197.5 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): om fixed | 8.8 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): om incentive | 0.4 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): ltsa fixed | 3.0 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): ltsa variable | 10.0 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): insurance | 5.4 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): g and a | 3.5 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): land | 0.8 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): community and levy | 0.8 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): consumables | 4.7 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): agency | 0.3 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): prg fee | 0.3 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): vat interest | 0.1 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): fx losses | 1.3 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): late payment interest | 0.0 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): major maintenance | 0.0 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): ebitda | 97.0 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): tax | 0.0 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): increase in working capital | 13.9 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): mmra contribution | 0.9 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): mmra release | 0.0 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): cfads | 82.2 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): debt service | 73.1 | USD m | Actual history (15) | calendar 2022 |
| P-F10 | Actual first full operating year (calendar 2022): dscr | 1.12x | x | Actual history (15) | calendar 2022 |
| P-F11a | DSRA initial balance (funded at COD; next period debt service) | 37.2 | USD m | FC base (1) | 2021-05-01 |
| P-F11a | DSRA balance 2021H1 | 37.2 | USD m | FC base (1) | 2021H1 |
| P-F11a | DSRA balance 2021H2 | 37.2 | USD m | FC base (1) | 2021H2 |
| P-F11a | DSRA balance 2022H1 | 37.6 | USD m | FC base (1) | 2022H1 |
| P-F11a | DSRA balance 2022H2 | 37.3 | USD m | FC base (1) | 2022H2 |
| P-F11a | DSRA balance 2023H1 | 37.8 | USD m | FC base (1) | 2023H1 |
| P-F11a | DSRA balance 2023H2 | 37.6 | USD m | FC base (1) | 2023H2 |
| P-F11a | DSRA balance 2024H1 | 38.3 | USD m | FC base (1) | 2024H1 |
| P-F11a | DSRA balance 2024H2 | 38.0 | USD m | FC base (1) | 2024H2 |
| P-F11b | MMRA contribution 2021H2 | 0.42 | USD m | FC base (1) | 2021H2 |
| P-F11b | MMRA contribution 2022H1 | 0.42 | USD m | FC base (1) | 2022H1 |
| P-F11b | MMRA contribution 2022H2 | 0.42 | USD m | FC base (1) | 2022H2 |
| P-F11b | MMRA contribution 2023H1 | 0.42 | USD m | FC base (1) | 2023H1 |
| P-F11b | MMRA contribution 2023H2 | 0.42 | USD m | FC base (1) | 2023H2 |
| P-F11b | MMRA contribution 2024H1 | 0.42 | USD m | FC base (1) | 2024H1 |
| P-F11b | MMRA contribution 2025H2 | 1.97 | USD m | FC base (1) | 2025H2 |
| P-F11b | MMRA contribution 2026H1 | 1.97 | USD m | FC base (1) | 2026H1 |
| P-F11b | MMRA contribution 2026H2 | 1.97 | USD m | FC base (1) | 2026H2 |
| P-F11b | MMRA contribution 2027H1 | 1.97 | USD m | FC base (1) | 2027H1 |
| P-F11b | MMRA contribution 2027H2 | 1.97 | USD m | FC base (1) | 2027H2 |
| P-F11b | MMRA contribution 2028H1 | 1.97 | USD m | FC base (1) | 2028H1 |
| P-F11b | MMRA contribution 2029H2 | 0.50 | USD m | FC base (1) | 2029H2 |
| P-F11b | MMRA contribution 2030H1 | 0.50 | USD m | FC base (1) | 2030H1 |
| P-F11b | MMRA contribution 2030H2 | 0.50 | USD m | FC base (1) | 2030H2 |
| P-F11b | Out-of-LTSA major maintenance spend 2024H2 | 2.50 | USD m | FC base (1) | 2024H2 |
| P-F11b | Out-of-LTSA major maintenance spend 2028H2 | 11.84 | USD m | FC base (1) | 2028H2 |
| P-F11b | Out-of-LTSA major maintenance spend 2032H2 | 2.97 | USD m | FC base (1) | 2032H2 |
| P-F11b | Out-of-LTSA major maintenance spend 2036H2 | 14.09 | USD m | FC base (1) | 2036H2 |
| P-F11b | Out-of-LTSA major maintenance spend 2040H2 | 3.54 | USD m | FC base (1) | 2040H2 |
| P-F11b | Out-of-LTSA major maintenance spend 2044H2 | 16.77 | USD m | FC base (1) | 2044H2 |
| P-F12 | Swap fixed rate | 2.947% | % | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional peak during construction | 501.8 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional 2021H2 | 504.0 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional 2023H2 | 451.0 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional 2025H2 | 389.0 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional 2027H2 | 323.6 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional 2029H2 | 246.3 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional 2031H2 | 155.3 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional 2033H2 | 48.1 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Blended base rate on 80% hedged / 20% unhedged (2022) | 2.98% | % | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost ECA: full (base, margin, fees, ECA premium, PRI, gross-up) | 5.70% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost ECA: excluding PRI premium | 5.70% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost ECA: excluding WHT gross-up | 5.70% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost ECA: excluding financed ECA premium | 4.46% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost ECA: base and margin only | 4.33% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost A: full (base, margin, fees, ECA premium, PRI, gross-up) | 6.77% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost A: excluding PRI premium | 6.77% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost A: excluding WHT gross-up | 6.77% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost A: excluding financed ECA premium | 6.77% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost A: base and margin only | 6.63% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost B: full (base, margin, fees, ECA premium, PRI, gross-up) | 6.55% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost B: excluding PRI premium | 6.55% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost B: excluding WHT gross-up | 6.55% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost B: excluding financed ECA premium | 6.55% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost B: base and margin only | 6.38% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost COM: full (base, margin, fees, ECA premium, PRI, gross-up) | 9.15% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost COM: excluding PRI premium | 8.11% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost COM: excluding WHT gross-up | 8.36% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost COM: excluding financed ECA premium | 9.15% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | All-in cost COM: base and margin only | 7.08% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | Weighted all-in cost of senior debt | 7.33% | % pa | FC base (1) | 2018-07-17 |
| P-F12 | Model all-in senior cost in 2022 (financing costs / opening debt) | 6.77% | % pa | FC base (1) | 2022 |
| P-F13 | Construction total: uses | 854.6 | USD m | FC base (1) | 2021-06-30 |
| P-F13 | Construction total: debt | 629.9 | USD m | FC base (1) | 2021-06-30 |
| P-F13 | Construction total: equity | 224.6 | USD m | FC base (1) | 2021-06-30 |
| P-F13 | Construction total: idc incl swap pri | 63.6 | USD m | FC base (1) | 2021-06-30 |
| P-F13 | Month 2018-08: uses / debt / equity / IDC | 121.5 / 89.6 / 31.9 / 0.00 | USD m | FC base (1) | 2018-08 |
| P-F13 | Month 2019-01: uses / debt / equity / IDC | 8.9 / 6.6 / 2.3 / 0.58 | USD m | FC base (1) | 2019-01 |
| P-F13 | Month 2019-07: uses / debt / equity / IDC | 26.9 / 19.9 / 7.1 / 1.00 | USD m | FC base (1) | 2019-07 |
| P-F13 | Month 2020-01: uses / debt / equity / IDC | 36.5 / 26.9 / 9.6 / 1.81 | USD m | FC base (1) | 2020-01 |
| P-F13 | Month 2020-07: uses / debt / equity / IDC | 25.7 / 18.9 / 6.8 / 2.65 | USD m | FC base (1) | 2020-07 |
| P-F13 | Month 2021-01: uses / debt / equity / IDC | 8.7 / 6.4 / 2.3 / 3.12 | USD m | FC base (1) | 2021-01 |
| P-F13 | Month 2021-04: uses / debt / equity / IDC | 54.2 / 40.0 / 14.3 / 3.14 | USD m | FC base (1) | 2021-04 |
| P-F13 | Month 2021-05: uses / debt / equity / IDC | 41.8 / 30.8 / 11.0 / 3.44 | USD m | FC base (1) | 2021-05 |
| P-F14 | OY1 ebitda | 101.5 | USD m | FC base (1) | OY1 |
| P-F14 | OY1 depreciation deferred | 45.2 | USD m | FC base (1) | OY1 |
| P-F14 | OY1 depreciation current | 0.0 | USD m | FC base (1) | OY1 |
| P-F14 | OY1 deferred used | 0.0 | USD m | FC base (1) | OY1 |
| P-F14 | OY1 taxable income | 0.0 | USD m | FC base (1) | OY1 |
| P-F14 | OY1 cit | 0.0 | USD m | FC base (1) | OY1 |
| P-F14 | OY1 minimum turnover tax | 0.0 | USD m | FC base (1) | OY1 |
| P-F14 | OY1 tax paid | 0.0 | USD m | FC base (1) | OY1 |
| P-F14 | OY2 ebitda | 102.0 | USD m | FC base (1) | OY2 |
| P-F14 | OY2 depreciation deferred | 45.2 | USD m | FC base (1) | OY2 |
| P-F14 | OY2 depreciation current | 0.0 | USD m | FC base (1) | OY2 |
| P-F14 | OY2 deferred used | 0.0 | USD m | FC base (1) | OY2 |
| P-F14 | OY2 taxable income | 0.0 | USD m | FC base (1) | OY2 |
| P-F14 | OY2 cit | 0.0 | USD m | FC base (1) | OY2 |
| P-F14 | OY2 minimum turnover tax | 0.0 | USD m | FC base (1) | OY2 |
| P-F14 | OY2 tax paid | 0.0 | USD m | FC base (1) | OY2 |
| P-F14 | OY3 ebitda | 102.5 | USD m | FC base (1) | OY3 |
| P-F14 | OY3 depreciation deferred | 45.2 | USD m | FC base (1) | OY3 |
| P-F14 | OY3 depreciation current | 0.0 | USD m | FC base (1) | OY3 |
| P-F14 | OY3 deferred used | 0.0 | USD m | FC base (1) | OY3 |
| P-F14 | OY3 taxable income | 0.0 | USD m | FC base (1) | OY3 |
| P-F14 | OY3 cit | 0.0 | USD m | FC base (1) | OY3 |
| P-F14 | OY3 minimum turnover tax | 0.0 | USD m | FC base (1) | OY3 |
| P-F14 | OY3 tax paid | 0.0 | USD m | FC base (1) | OY3 |
| P-F14 | OY4 ebitda | 100.6 | USD m | FC base (1) | OY4 |
| P-F14 | OY4 depreciation deferred | 45.2 | USD m | FC base (1) | OY4 |
| P-F14 | OY4 depreciation current | 0.0 | USD m | FC base (1) | OY4 |
| P-F14 | OY4 deferred used | 0.0 | USD m | FC base (1) | OY4 |
| P-F14 | OY4 taxable income | 0.0 | USD m | FC base (1) | OY4 |
| P-F14 | OY4 cit | 0.0 | USD m | FC base (1) | OY4 |
| P-F14 | OY4 minimum turnover tax | 0.0 | USD m | FC base (1) | OY4 |
| P-F14 | OY4 tax paid | 0.0 | USD m | FC base (1) | OY4 |
| P-F14 | OY5 ebitda | 103.4 | USD m | FC base (1) | OY5 |
| P-F14 | OY5 depreciation deferred | 40.1 | USD m | FC base (1) | OY5 |
| P-F14 | OY5 depreciation current | 4.5 | USD m | FC base (1) | OY5 |
| P-F14 | OY5 deferred used | 1.6 | USD m | FC base (1) | OY5 |
| P-F14 | OY5 taxable income | 0.0 | USD m | FC base (1) | OY5 |
| P-F14 | OY5 cit | 0.0 | USD m | FC base (1) | OY5 |
| P-F14 | OY5 minimum turnover tax | 0.1 | USD m | FC base (1) | OY5 |
| P-F14 | OY5 tax paid | 0.1 | USD m | FC base (1) | OY5 |
| P-F14 | OY6 ebitda | 103.8 | USD m | FC base (1) | OY6 |
| P-F14 | OY6 depreciation deferred | 5.0 | USD m | FC base (1) | OY6 |
| P-F14 | OY6 depreciation current | 35.7 | USD m | FC base (1) | OY6 |
| P-F14 | OY6 deferred used | 14.7 | USD m | FC base (1) | OY6 |
| P-F14 | OY6 taxable income | 0.0 | USD m | FC base (1) | OY6 |
| P-F14 | OY6 cit | 0.0 | USD m | FC base (1) | OY6 |
| P-F14 | OY6 minimum turnover tax | 0.6 | USD m | FC base (1) | OY6 |
| P-F14 | OY6 tax paid | 0.6 | USD m | FC base (1) | OY6 |
| P-F14 | OY7 ebitda | 104.3 | USD m | FC base (1) | OY7 |
| P-F14 | OY7 depreciation deferred | 0.0 | USD m | FC base (1) | OY7 |
| P-F14 | OY7 depreciation current | 40.1 | USD m | FC base (1) | OY7 |
| P-F14 | OY7 deferred used | 20.6 | USD m | FC base (1) | OY7 |
| P-F14 | OY7 taxable income | 0.0 | USD m | FC base (1) | OY7 |
| P-F14 | OY7 cit | 0.0 | USD m | FC base (1) | OY7 |
| P-F14 | OY7 minimum turnover tax | 0.7 | USD m | FC base (1) | OY7 |
| P-F14 | OY7 tax paid | 0.7 | USD m | FC base (1) | OY7 |
| P-F14 | OY8 ebitda | 92.4 | USD m | FC base (1) | OY8 |
| P-F14 | OY8 depreciation deferred | 0.0 | USD m | FC base (1) | OY8 |
| P-F14 | OY8 depreciation current | 40.1 | USD m | FC base (1) | OY8 |
| P-F14 | OY8 deferred used | 13.1 | USD m | FC base (1) | OY8 |
| P-F14 | OY8 taxable income | 0.0 | USD m | FC base (1) | OY8 |
| P-F14 | OY8 cit | 0.0 | USD m | FC base (1) | OY8 |
| P-F14 | OY8 minimum turnover tax | 0.7 | USD m | FC base (1) | OY8 |
| P-F14 | OY8 tax paid | 0.7 | USD m | FC base (1) | OY8 |
| P-F14 | OY9 ebitda | 105.3 | USD m | FC base (1) | OY9 |
| P-F14 | OY9 depreciation deferred | 0.0 | USD m | FC base (1) | OY9 |
| P-F14 | OY9 depreciation current | 40.1 | USD m | FC base (1) | OY9 |
| P-F14 | OY9 deferred used | 31.0 | USD m | FC base (1) | OY9 |
| P-F14 | OY9 taxable income | 0.0 | USD m | FC base (1) | OY9 |
| P-F14 | OY9 cit | 0.0 | USD m | FC base (1) | OY9 |
| P-F14 | OY9 minimum turnover tax | 0.7 | USD m | FC base (1) | OY9 |
| P-F14 | OY9 tax paid | 0.7 | USD m | FC base (1) | OY9 |
| P-F14 | OY10 ebitda | 105.8 | USD m | FC base (1) | OY10 |
| P-F14 | OY10 depreciation deferred | 0.0 | USD m | FC base (1) | OY10 |
| P-F14 | OY10 depreciation current | 40.1 | USD m | FC base (1) | OY10 |
| P-F14 | OY10 deferred used | 37.1 | USD m | FC base (1) | OY10 |
| P-F14 | OY10 taxable income | 0.0 | USD m | FC base (1) | OY10 |
| P-F14 | OY10 cit | 0.0 | USD m | FC base (1) | OY10 |
| P-F14 | OY10 minimum turnover tax | 0.7 | USD m | FC base (1) | OY10 |
| P-F14 | OY10 tax paid | 0.7 | USD m | FC base (1) | OY10 |
| P-F14 | First period with corporate income tax above the minimum tax | 2033H2 | period | FC base (1) | 2018-07-17 |
| P-F15 | OY1 cfads | 85.6 | USD m | FC base (1) | OY1 |
| P-F15 | OY1 senior interest and fees | 35.6 | USD m | FC base (1) | OY1 |
| P-F15 | OY1 senior principal | 26.4 | USD m | FC base (1) | OY1 |
| P-F15 | OY1 dsra topup net | 0.2 | USD m | FC base (1) | OY1 |
| P-F15 | OY1 shl interest paid | 16.3 | USD m | FC base (1) | OY1 |
| P-F15 | OY1 shl principal | 7.1 | USD m | FC base (1) | OY1 |
| P-F15 | OY1 dividends | 0.0 | USD m | FC base (1) | OY1 |
| P-F15 | OY1 net income | 22.9 | USD m | FC base (1) | OY1 |
| P-F15 | OY2 cfads | 101.1 | USD m | FC base (1) | OY2 |
| P-F15 | OY2 senior interest and fees | 40.9 | USD m | FC base (1) | OY2 |
| P-F15 | OY2 senior principal | 34.0 | USD m | FC base (1) | OY2 |
| P-F15 | OY2 dsra topup net | 0.1 | USD m | FC base (1) | OY2 |
| P-F15 | OY2 shl interest paid | 18.9 | USD m | FC base (1) | OY2 |
| P-F15 | OY2 shl principal | 7.2 | USD m | FC base (1) | OY2 |
| P-F15 | OY2 dividends | 0.0 | USD m | FC base (1) | OY2 |
| P-F15 | OY2 net income | 18.9 | USD m | FC base (1) | OY2 |
| P-F15 | OY3 cfads | 101.6 | USD m | FC base (1) | OY3 |
| P-F15 | OY3 senior interest and fees | 38.7 | USD m | FC base (1) | OY3 |
| P-F15 | OY3 senior principal | 36.5 | USD m | FC base (1) | OY3 |
| P-F15 | OY3 dsra topup net | 0.4 | USD m | FC base (1) | OY3 |
| P-F15 | OY3 shl interest paid | 18.2 | USD m | FC base (1) | OY3 |
| P-F15 | OY3 shl principal | 7.7 | USD m | FC base (1) | OY3 |
| P-F15 | OY3 dividends | 0.0 | USD m | FC base (1) | OY3 |
| P-F15 | OY3 net income | 22.1 | USD m | FC base (1) | OY3 |
| P-F15 | Maximum trapped cash with 80% shareholder loans | 0.0 | USD m | FC base (1) | 2018-07-17 |
| P-F15 | Maximum trapped cash with 100% share capital | 175.6 | USD m | FC base (1), no SHL variant | 2018-07-17 |
| P-F15 | Equity IRR with 100% share capital | 12.6% | % | FC base (1), no SHL variant | 2018-07-17 |
| P-F16 | Equity IRR (project-company level, from LNTP date, before WHT) | 13.2% | % nominal post-tax | FC base (1) | 2018-07-17 |
| P-F16 | Equity IRR including development spend and reimbursement | 13.5% | % | FC base (1) | 2018-07-17 |
| P-F16 | Project IRR, post-tax | 11.0% | % | FC base (1) | 2018-07-17 |
| P-F16 | Project IRR, pre-tax | 11.6% | % | FC base (1) | 2018-07-17 |
| P-F16 | Equity NPV at 16.0% at financial close | -45.3 | USD m | FC base (1) | 2018-07-17 |
| P-F16 | Equity payback (cumulative equity cash flow turns positive) | 2031-06-30 | date | FC base (1) | 2018-07-17 |
| P-F16 | FC base: minimum DSCR / average DSCR / equity IRR | 1.35x / 1.55x / 13.2% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | FC banking: minimum DSCR / average DSCR / equity IRR | 1.35x / 1.55x / 13.1% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | FC downside: minimum DSCR / average DSCR / equity IRR | 1.20x / 1.38x / 11.3% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: availability -3 points: minimum DSCR / average DSCR / equity IRR | 1.32x / 1.54x / 13.1% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: heat rate +2%: minimum DSCR / average DSCR / equity IRR | 1.30x / 1.50x / 12.4% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: fixed opex +10%: minimum DSCR / average DSCR / equity IRR | 1.32x / 1.52x / 12.7% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: capex +10% funded pro rata: minimum DSCR / average DSCR / equity IRR | 1.23x / 1.39x / 11.3% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: COD delay 6 months, no LDs: minimum DSCR / average DSCR / equity IRR | 1.25x / 1.45x / 12.0% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: base rate +200 bps (unhedged): minimum DSCR / average DSCR / equity IRR | 1.30x / 1.52x / 12.8% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: KCR devaluation 40%, 90-day lag: minimum DSCR / average DSCR / equity IRR | 0.45x / 1.53x / 12.7% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: SEKA pays 120 days late for 12 months: minimum DSCR / average DSCR / equity IRR | 0.13x / 1.55x / 13.1% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: dispatch 50%: minimum DSCR / average DSCR / equity IRR | 1.34x / 1.54x / 13.0% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: gas price +30%: minimum DSCR / average DSCR / equity IRR | 1.35x / 1.55x / 13.2% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Breakeven availability shift for 1.00x minimum DSCR | -21.4 | points below profile | FC base (1) | 2018-07-17 |
| P-F16 | Breakeven capacity charge cut for 1.00x minimum DSCR | 25.0% | % | FC base (1) | 2018-07-17 |
| P-F16 | Months of zero SEKA payment covered by DSRA plus LC (gas paid) | 3.0 | months | FC base (1) | 2022H1 |
| P-F16 | Months covered if gas payments are deferred | 8.1 | months | FC base (1) | 2022H1 |
| P-F17 | correct: correct model | debt 629.9 (+0.0), DSCR; min DSCR 1.35x; avg 1.55x; downside 1.20x; banking 1.35x; LLCR 1.42x; equity IRR 13.2% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E1: Capacity payment without the availability cap (A/90% not capped at 1) | debt 639.0 (+9.0), downside; min DSCR 1.37x; avg 1.57x; downside 1.20x; banking 1.37x; LLCR 1.44x; equity IRR 14.0% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E2: LTSA variable fee on one gas turbine instead of two | debt 643.3 (+13.3), gearing; min DSCR 1.37x; avg 1.57x; downside 1.22x; banking 1.37x; LLCR 1.44x; equity IRR 14.3% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E3: Tariff indexation reads the index at period end instead of the lagged (Sep/Mar) reading | debt 637.0 (+7.0), DSCR; min DSCR 1.35x; avg 1.55x; downside 1.20x; banking 1.35x; LLCR 1.42x; equity IRR 13.5% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E4: Senior loan interest on 30/360 instead of ACT/360 | debt 632.9 (+3.0), DSCR; min DSCR 1.35x; avg 1.55x; downside 1.20x; banking 1.35x; LLCR 1.42x; equity IRR 13.3% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E5: Full tax exemption applied to OY1-OY8 (15% band ignored) | debt 635.4 (+5.5), DSCR; min DSCR 1.35x; avg 1.55x; downside 1.20x; banking 1.35x; LLCR 1.42x; equity IRR 13.6% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E6: Deferred holiday depreciation lost (pool never credited) | debt 611.7 (-18.2), DSCR; min DSCR 1.35x; avg 1.54x; downside 1.20x; banking 1.35x; LLCR 1.42x; equity IRR 12.4% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E7: DSRA initial funding drawn 100% from senior debt instead of pro rata | debt 630.0 (+0.1), DSCR; min DSCR 1.35x; avg 1.55x; downside 1.20x; banking 1.35x; LLCR 1.42x; equity IRR 13.1% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E8: Sculpting on CFADS before tax | debt 636.7 (+6.8), DSCR; min DSCR 1.34x; avg 1.52x; downside 1.20x; banking 1.34x; LLCR 1.40x; equity IRR 13.3% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E9: Fuel-charge revenue uses a typed 76.5% dispatch instead of the live dispatch | debt 629.9 (+0.0), DSCR; min DSCR 1.35x; avg 1.55x; downside 1.20x; banking 1.47x; LLCR 1.42x; equity IRR 13.2% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E10: Swap net settlement with legs reversed | debt 619.9 (-10.0), DSCR; min DSCR 1.35x; avg 1.55x; downside 1.20x; banking 1.35x; LLCR 1.42x; equity IRR 12.8% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | ALL: all ten errors together | debt 655.0 (+25.0), gearing; min DSCR 1.42x; avg 1.53x; downside 1.25x; banking 1.54x; LLCR 1.42x; equity IRR 15.1% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F18 | Actual use: epc | 565.12 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: epc fx gain on onshore | 6.72 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: owners costs incl extension | 53.11 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: overrun items excl extension | 74.51 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: hard cost overrun total | 81.44 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: of which bible items | 39.27 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: of which delay related added | 42.17 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: delay-related cost added (P-C43): EPC claims settlement: COVID-19 disruption and compensable events beyond the 9.40 variation order (Lindauer, settled at taking-over) | 12.00 | USD m | Modeler assumption (P-C43), Months 34-40 | 2021-05 to 2021-11 |
| P-F18 | Actual use: delay-related cost added (P-C43): Acceleration agreement with Lindauer to hold taking-over at November 2021 after the grid event | 9.50 | USD m | Modeler assumption (P-C43), Months 34-40 | 2021-05 to 2021-11 |
| P-F18 | Actual use: delay-related cost added (P-C43): Extended owner's costs and site team beyond the 6.93 (owner's engineer, site team, security, camp) | 7.20 | USD m | Modeler assumption (P-C43), Months 34-40 | 2021-05 to 2021-11 |
| P-F18 | Actual use: delay-related cost added (P-C43): Re-commissioning after the grid event (repeat backfeed, protection coordination study, OEM field service) | 6.40 | USD m | Modeler assumption (P-C43), Months 34-40 | 2021-05 to 2021-11 |
| P-F18 | Actual use: delay-related cost added (P-C43): Transformer replacement expediting, freight and installation not recovered under the EAR policy | 3.10 | USD m | Modeler assumption (P-C43), Months 34-40 | 2021-05 to 2021-11 |
| P-F18 | Actual use: delay-related cost added (P-C43): Additional IE, lenders' legal and expert-determination costs beyond the 0.86 | 2.35 | USD m | Modeler assumption (P-C43), Months 34-40 | 2021-05 to 2021-11 |
| P-F18 | Actual use: delay-related cost added (P-C43): Operator mobilization and training held seven months longer (O&M contractor standby) | 1.62 | USD m | Modeler assumption (P-C43), Months 34-40 | 2021-05 to 2021-11 |
| P-F18 | Actual use: contingency available | 38.40 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: other base | 54.57 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: subtotal before financing | 742.91 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: idc loans | 44.67 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: swap net | 13.59 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: pri | 4.16 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: commitment fees | 12.18 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: upfront fees | 9.90 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: eca premium | 20.50 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: agency | 0.87 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: vat interest | 1.49 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: dsra initial | 34.93 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: total | 885.21 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: senior debt drawn | 629.95 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: senior commitment | 629.95 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: undrawn commitment cancelled | 0.00 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: base equity | 224.60 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: delay lds received | 10.14 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: dsu received | 7.08 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: lds and dsu applied to construction | 17.22 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: lds and dsu unused to operating cash | 0.00 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: standby drawn | 10.08 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: contingent equity drawn | 3.36 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | total funding fc | 854.55 | USD m | Actual history (15) vs FC base (1) | 2021-12-01 |
| P-F18 | idc fc | 63.57 | USD m | Actual history (15) vs FC base (1) | 2021-12-01 |
| P-F18 | idc actual | 62.42 | USD m | Actual history (15) vs FC base (1) | 2021-12-01 |
| P-F19 | Tested net output / heat rate | 581.9 MW / 6,286 kJ/kWh | inputs | Inputs | 2021-11-30 |
| P-F19 | Output LDs / heat-rate LDs / total | 13.975 / 4.510 / 18.485 | USD m | Inputs | 2021-11-30 |
| P-F19 | COD re-sculpted constant DSCR (before the LD prepayment; debt drawn at COD and final maturity June 30, 2034 held, so the level DSCR is the output, not a re-sculpt to 1.35x; ECA tranche in equal installments) | 1.28x (1.281051) | x | COD re-forecast (14) | 2021-12-01 |
| P-F19 | Same, had capacity and heat rate stayed at 588.4 MW / 6,261 | 1.31x | x | COD re-forecast (14) variant | 2021-12-01 |
| P-F19 | Projected minimum DSCR after the June 2022 LD prepayment | 1.32x | x | COD re-forecast (14) | 2022-06-30 |
| P-F19 | Projected average DSCR after the prepayment | 1.52x | x | COD re-forecast (14) | 2022-06-30 |
| P-F19 | Projected minimum DSCR without the prepayment | 1.28x | x | COD re-forecast (14) variant | 2022-06-30 |
| P-F20 | 2022H1: overdue / deferred SNHK-GCK payables / CFADS / debt service / DSCR / DSRA draw / DSRA balance | 18.4 / 14.7 / 44.8 / 35.6 / 1.26x / 0.0 / 37.5 | USD m, x | Actual history (15) | 2022H1 |
| P-F20 | 2022H2: overdue / deferred SNHK-GCK payables / CFADS / debt service / DSCR / DSRA draw / DSRA balance | 68.9 / 55.1 / 37.4 / 37.5 / 1.00x / 0.2 / 37.4 | USD m, x | Actual history (15) | 2022H2 |
| P-F20 | 2023H1: overdue / deferred SNHK-GCK payables / CFADS / debt service / DSCR / DSRA draw / DSRA balance | 112.6 / 90.1 / 35.8 / 39.1 / 0.91x / 3.3 / 34.0 | USD m, x | Actual history (15) | 2023H1 |
| P-F20 | 2023H2: overdue / deferred SNHK-GCK payables / CFADS / debt service / DSCR / DSRA draw / DSRA balance | 71.8 / 57.4 / 56.2 / 30.6 / 1.83x / 0.0 / 44.1 | USD m, x | Actual history (15) | 2023H2 |
| P-F20 | 2024H1: overdue / deferred SNHK-GCK payables / CFADS / debt service / DSCR / DSRA draw / DSRA balance | 34.6 / 27.7 / 57.4 / 44.1 / 1.30x / 0.0 / 44.3 | USD m, x | Actual history (15) | 2024H1 |
| P-F20 | 2024H2: overdue / deferred SNHK-GCK payables / CFADS / debt service / DSCR / DSRA draw / DSRA balance | 12.3 / 9.8 / 56.7 / 44.3 / 1.28x / 0.0 / 42.2 | USD m, x | Actual history (15) | 2024H2 |
| P-F20 | 2025H1: overdue / deferred SNHK-GCK payables / CFADS / debt service / DSCR / DSRA draw / DSRA balance | 0.0 / 0.0 / 55.4 / 42.2 / 1.31x / 0.0 / 32.5 | USD m, x | Actual history (15) | 2025H1 |
| P-F20 | FX conversion losses, total 2022H2-2024H1 | 6.54 | USD m | Inputs | 2024-06-30 |
| P-F20 | Late payment interest accrued / received (60%) | 8.7 / 5.2 | USD m | Actual history (15) | 2025-06-30 |
| P-F20 | Lock-up periods (distribution test failed) | 2022H2, 2023H1, 2023H2, 2024H1 | periods | Actual history (15) | 2024-12-31 |
| P-F21 | Historic DSCR at December 31, 2022 | 1.12x | x | Actual history (15) | 2022-12-31 |
| P-F21 | Historic DSCR at June 30, 2023 (event of default below 1.10x) | 0.95x | x | Actual history (15) | 2023-06-30 |
| P-F21 | Period DSCR 2023H1 | 0.91x | x | Actual history (15) | 2023-06-30 |
| P-F21 | DSRA drawing at June 30, 2023 | 3.33 | USD m | Actual history (15) | 2023-06-30 |
| P-F21 | Waiver fee (0.25% of senior debt) | 1.43 | USD m | Actual history (15) | 2023-10-26 |
| P-F21 | Margin uplift cost, 2023H2-2024H2 | 4.46 | USD m | Actual history (15) | 2024-12-31 |
| P-F21 | Principal deferred from December 31, 2023 (60%) | 10.85 | USD m | Actual history (15) | 2023-12-31 |
| P-F21 | Each of four deferred repayments (2024H1-2025H2) | 2.71 | USD m | Actual history (15) | 2024-06-30 |
| P-F21 | Historic DSCR at December 31, 2023 (waived test) | 1.32x | x | Actual history (15) | 2023-12-31 |
| P-F21 | Lock-up released (two tests >= 1.25x and DSRA full) | 2024H2 | period | Actual history (15) | 2024-12-31 |
| P-F22 | Base rate 2022H2 (6M LIBOR; illustrative path, D-046) | 2.94% | % | Actual history (15) | 2022-07 |
| P-F22 | Base rate 2023H1 (6M Term SOFR 4.86%, approximate, illustrative path D-046, + 0.42826%) | 5.29% | % | Actual history (15) | 2023-01 |
| P-F22 | Senior financing cost 2022H2 / 2023H1 | 20.8 / 21.8 | USD m | Actual history (15) | 2023-06-30 |
| P-F22 | All-in senior cost 2022H2 / 2023H1 | 6.72% / 7.36% | % pa | Actual history (15) | 2023-06-30 |
| P-F22 | Unhedged balance 2023H1 (debt less swap notional) | 123.7 | USD m | Actual history (15) | 2023-01 |
| P-F22 | Cost of the 0.42826% spread adjustment, 2023H1 / calendar 2023 | 0.27 / 0.53 | USD m | Actual history (15) | 2023-12-31 |
| P-F23 | prepaid principal | 252.44 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | swap unwind receipt | 6.28 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | bond face | 253.75 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | bond proceeds | 252.52 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | oid | 1.24 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | underwriting | 2.54 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | other costs | 3.10 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | pcg upfront | 0.71 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | transaction costs total | 7.59 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | remaining eca | 133.14 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | remaining a loan | 111.97 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | equity pv gain at 13 75pct | 13.95 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | equity pv gain at 12 50pct | 9.75 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | prepaid B | 50.90 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | prepaid COM | 193.40 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | prepaid SB | 8.15 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Combined sculpted DSCR (ECA + A-loan + bond, constant) | 1.59x | x | Actual history (15) | 2025-06-30 |
| P-F23 | Minimum DSCR after refinancing | 1.59x | x | Actual history (15) | 2025-06-30 |
| P-F23 | Equity IRR with / without the refinancing | 12.4% / 12.0% | % | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2025H2 | 1.73 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2026H2 | 3.38 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2027H2 | 3.95 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2028H2 | 4.57 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2029H2 | 6.10 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2030H2 | 6.83 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2031H2 | 7.65 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2032H2 | 8.47 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2033H2 | 9.72 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2034H2 | 24.09 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2035H2 | 22.95 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2036H2 | 24.60 | USD m | Actual history (15) | 2025-06-30 |
| P-F24 | equity value 100pct at 13 75 | 325.02 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | equity value 100pct at 12 50 | 356.46 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | value 24pct at 13 75 | 78.00 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | value 24pct at 12 50 | 85.55 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | leakage h1 2026 distribution 24pct | 4.27 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | price at completion | 77.52 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | kilnworth reserve price 24pct | 85.43 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | deferred consideration | 4.00 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | cost basis 24pct | 40.92 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | seller gain | 36.60 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | indirect transfer tax | 5.49 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | Locked-box ticker factor (6.5% simple, 273 days) | 1.0486 | factor | Actual history (15) | 2026-09-30 |
| P-F24 | Kilnworth's IRR on the sold 24% (after transfer tax) | 9.6% | % | Actual history (15) | 2026-09-30 |
| P-F24 | Same including the USD 4.0 million deferred consideration (taxed) | 10.1% | % | Actual history (15) | 2027-06-30 |
| P-F25 | senior debt outstanding | 571.3 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | swap mtm to project | 30.2 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | equity npv distributions 14 5 | 285.7 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | equity contributed compounded less distributions | 358.1 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | equity amount | 358.1 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | seka default compensation | 899.1 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | project default compensation | 571.3 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | natural fm compensation | 798.9 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | equity contributed | 228.0 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | distributions received | 0.3 | USD m | Actual history (15) | 2023-06-30 |
| P-F26 | book equity lenders basis | 110.3 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | ifrs12 equity adjustment pretax | 143.1 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | shl at completion | 208.1 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | consideration | 77.5 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | fv retained 36pct | 116.3 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | carrying amount 60pct lenders basis | 191.0 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | carrying amount 60pct ifrs | 276.9 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | gain on loss of control lenders basis | 2.8 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | gain on loss of control ifrs | -83.1 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | hedge reserve parent share recycled | 2.1 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | equity method carrying value 36pct | 116.3 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | indirect transfer tax | 5.5 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | Deferred consideration: face / fair value at completion (measured at nil, Annex P 8.3; outside the consideration line) | 4.0 / 0.0 | USD m | Actual history (15) | 2026-09-30 |
| P-F27 | fc base: dividends (life total) | 997.6 | USD m | FC base (1) | 2018-2046 |
| P-F27 | fc base: shl interest (life total) | 190.6 | USD m | FC base (1) | 2018-2046 |
| P-F27 | fc base: wht dividends treaty 7 5 (life total) | 74.8 | USD m | FC base (1) | 2018-2046 |
| P-F27 | fc base: wht dividends domestic 15 (life total) | 149.6 | USD m | FC base (1) | 2018-2046 |
| P-F27 | fc base: wht shl interest treaty 5 (life total) | 9.5 | USD m | FC base (1) | 2018-2046 |
| P-F27 | fc base: wht shl interest domestic 10 (life total) | 19.1 | USD m | FC base (1) | 2018-2046 |
| P-F27 | fc base: commercial grossup cost (life total) | 16.9 | USD m | FC base (1) | 2018-2046 |
| P-F27 | actual: dividends (life total) | 923.3 | USD m | Actual history (15) | 2018-2046 |
| P-F27 | actual: shl interest (life total) | 145.6 | USD m | Actual history (15) | 2018-2046 |
| P-F27 | actual: wht dividends treaty 7 5 (life total) | 69.3 | USD m | Actual history (15) | 2018-2046 |
| P-F27 | actual: wht dividends domestic 15 (life total) | 138.5 | USD m | Actual history (15) | 2018-2046 |
| P-F27 | actual: wht shl interest treaty 5 (life total) | 7.3 | USD m | Actual history (15) | 2018-2046 |
| P-F27 | actual: wht shl interest domestic 10 (life total) | 14.6 | USD m | Actual history (15) | 2018-2046 |
| P-F27 | actual: commercial grossup cost (life total) | 9.8 | USD m | Actual history (15) | 2018-2046 |
| P-F28 | Senior debt / total funding / gearing | 629.9 / 854.6 / 73.7% | USD m, % | FC base (1) | 2018-05 |
| P-F28 | Tenor from COD / WAL | 13.2 / 6.92 | years | FC base (1) | 2018-05 |
| P-F28 | base: min DSCR / avg DSCR / LLCR | 1.35x / 1.55x / 1.42x | x | FC base (1) | 2018-05 |
| P-F28 | banking: min DSCR / avg DSCR / LLCR | 1.35x / 1.55x / 1.42x | x | FC banking (2) | 2018-05 |
| P-F28 | downside: min DSCR / avg DSCR / LLCR | 1.20x / 1.38x / 1.30x | x | FC downside (3) | 2018-05 |
| P-F28 | Equity IRR / project IRR (base) | 13.2% / 11.0% | % | FC base (1) | 2018-05 |
| P-F29 | Handback reserve contribution 2040 | 0.28 | USD m | Actual history (15) | 2040 |
| P-F29 | Handback reserve contribution 2041 | 3.42 | USD m | Actual history (15) | 2041 |
| P-F29 | Handback reserve contribution 2042 | 3.50 | USD m | Actual history (15) | 2042 |
| P-F29 | Handback reserve contribution 2043 | 3.58 | USD m | Actual history (15) | 2043 |
| P-F29 | Handback reserve contribution 2044 | 3.66 | USD m | Actual history (15) | 2044 |
| P-F29 | Handback reserve contribution 2045 | 3.75 | USD m | Actual history (15) | 2045 |
| P-F29 | Handback reserve contribution 2046 | 3.51 | USD m | Actual history (15) | 2046 |
| P-F29 | Handback reserve at PPA expiry | 21.7 | USD m | Actual history (15) | 2046-11-30 |
| P-F30 | EAR loss / deductible / paid to EPC contractor | 6.84 / 1.00 / 5.84 | USD m | Inputs | 2021-06-09 |
| P-F30 | DSU: 76 days delay less 45-day deductible = 31 days x USD 228,400 | 7.08 | USD m | Inputs | 2021-11 |
| P-F31 | OY1 availability pct: actual (Dec 2021-Nov 2022) / FC base (May 2021-Apr 2022) | 93.7 / 93.7 | % or USD m | Actual history (15) / FC base (1) | 2022-11-30 |
| P-F31 | OY1 revenue: actual (Dec 2021-Nov 2022) / FC base (May 2021-Apr 2022) | 332.6 / 319.7 | % or USD m | Actual history (15) / FC base (1) | 2022-11-30 |
| P-F31 | OY1 operating costs: actual (Dec 2021-Nov 2022) / FC base (May 2021-Apr 2022) | 235.3 / 218.2 | % or USD m | Actual history (15) / FC base (1) | 2022-11-30 |
| P-F31 | OY1 ebitda: actual (Dec 2021-Nov 2022) / FC base (May 2021-Apr 2022) | 97.3 / 101.5 | % or USD m | Actual history (15) / FC base (1) | 2022-11-30 |
| P-F31 | OY1 cfads: actual (Dec 2021-Nov 2022) / FC base (May 2021-Apr 2022) | 69.6 / 85.6 | % or USD m | Actual history (15) / FC base (1) | 2022-11-30 |
| P-F31 | OY1 overdue change: actual (Dec 2021-Nov 2022) / FC base (May 2021-Apr 2022) | 26.8 / 15.2 | % or USD m | Actual history (15) / FC base (1) | 2022-11-30 |
| P-F32 | January 2022 invoice: energy mwh | 307,515 | MWh | Actual history (15) formulas | 2022-01-31 |
| P-F32 | January 2022 invoice: capacity payment | 10.02 | USD m | Actual history (15) formulas | 2022-01-31 |
| P-F32 | January 2022 invoice: vom payment | 1.30 | USD m | Actual history (15) formulas | 2022-01-31 |
| P-F32 | January 2022 invoice: fuel charge | 13.25 | USD m | Actual history (15) formulas | 2022-01-31 |
| P-F32 | January 2022 invoice: gta pass through | 2.39 | USD m | Actual history (15) formulas | 2022-01-31 |
| P-F32 | January 2022 invoice: take or pay | 0.00 | USD m | Actual history (15) formulas | 2022-01-31 |
| P-F32 | January 2022 invoice: invoice total | 26.97 | USD m | Actual history (15) formulas | 2022-01-31 |
| P-F32 | Gas price 2022 | 6.34 | USD/MMBtu | Actual history (15) | 2022-01 |
| P-F33 | daily interest per day | 117,623 | USD | FC base (1) | 2021-05-01 |
| P-F33 | daily fixed costs per day | 57,410 | USD | FC base (1) | 2021-05-01 |
| P-F33 | ppa delay ld per day | 94,150 | USD | FC base (1) | 2021-05-01 |
| P-F33 | total per day | 269,183 | USD | FC base (1) | 2021-05-01 |
| P-F33 | epc delay ld per day | 247,300 | USD | FC base (1) | 2021-05-01 |
| P-F33 | daily capacity revenue per day | 328,541 | USD | FC base (1) | 2021-05-01 |
| P-F34 | OY1 om fixed | 8.50 | USD m | FC base (1) | OY1 |
| P-F34 | OY1 ltsa fixed | 2.84 | USD m | FC base (1) | OY1 |
| P-F34 | OY1 ltsa var | 8.82 | USD m | FC base (1) | OY1 |
| P-F34 | OY1 insurance | 4.70 | USD m | FC base (1) | OY1 |
| P-F34 | OY1 ga | 3.41 | USD m | FC base (1) | OY1 |
| P-F34 | OY1 consumables | 4.24 | USD m | FC base (1) | OY1 |
| P-F34 | OY1 mm contr | 0.69 | USD m | FC base (1) | OY1 |
| P-F34 | OY1 opex om | 34.95 | USD m | FC base (1) | OY1 |
| P-F34 | OY2 om fixed | 8.69 | USD m | FC base (1) | OY2 |
| P-F34 | OY2 ltsa fixed | 2.90 | USD m | FC base (1) | OY2 |
| P-F34 | OY2 ltsa var | 9.01 | USD m | FC base (1) | OY2 |
| P-F34 | OY2 insurance | 4.80 | USD m | FC base (1) | OY2 |
| P-F34 | OY2 ga | 3.49 | USD m | FC base (1) | OY2 |
| P-F34 | OY2 consumables | 4.30 | USD m | FC base (1) | OY2 |
| P-F34 | OY2 mm contr | 0.83 | USD m | FC base (1) | OY2 |
| P-F34 | OY2 opex om | 35.53 | USD m | FC base (1) | OY2 |
| P-F34 | OY3 om fixed | 8.88 | USD m | FC base (1) | OY3 |
| P-F34 | OY3 ltsa fixed | 2.96 | USD m | FC base (1) | OY3 |
| P-F34 | OY3 ltsa var | 9.21 | USD m | FC base (1) | OY3 |
| P-F34 | OY3 insurance | 4.91 | USD m | FC base (1) | OY3 |
| P-F34 | OY3 ga | 3.56 | USD m | FC base (1) | OY3 |
| P-F34 | OY3 consumables | 4.40 | USD m | FC base (1) | OY3 |
| P-F34 | OY3 mm contr | 0.83 | USD m | FC base (1) | OY3 |
| P-F34 | OY3 opex om | 36.35 | USD m | FC base (1) | OY3 |
| P-F34 | OY4 om fixed | 9.07 | USD m | FC base (1) | OY4 |
| P-F34 | OY4 ltsa fixed | 3.03 | USD m | FC base (1) | OY4 |
| P-F34 | OY4 ltsa var | 9.42 | USD m | FC base (1) | OY4 |
| P-F34 | OY4 insurance | 5.02 | USD m | FC base (1) | OY4 |
| P-F34 | OY4 ga | 3.64 | USD m | FC base (1) | OY4 |
| P-F34 | OY4 consumables | 4.39 | USD m | FC base (1) | OY4 |
| P-F34 | OY4 mm contr | 0.14 | USD m | FC base (1) | OY4 |
| P-F34 | OY4 opex om | 36.55 | USD m | FC base (1) | OY4 |
| P-F34 | OY5 om fixed | 9.27 | USD m | FC base (1) | OY5 |
| P-F34 | OY5 ltsa fixed | 3.10 | USD m | FC base (1) | OY5 |
| P-F34 | OY5 ltsa var | 9.62 | USD m | FC base (1) | OY5 |
| P-F34 | OY5 insurance | 5.13 | USD m | FC base (1) | OY5 |
| P-F34 | OY5 ga | 3.72 | USD m | FC base (1) | OY5 |
| P-F34 | OY5 consumables | 4.58 | USD m | FC base (1) | OY5 |
| P-F34 | OY5 mm contr | 3.29 | USD m | FC base (1) | OY5 |
| P-F34 | OY5 opex om | 37.91 | USD m | FC base (1) | OY5 |
| P-F34 | OY6 om fixed | 9.48 | USD m | FC base (1) | OY6 |
| P-F34 | OY6 ltsa fixed | 3.16 | USD m | FC base (1) | OY6 |
| P-F34 | OY6 ltsa var | 9.83 | USD m | FC base (1) | OY6 |
| P-F34 | OY6 insurance | 5.24 | USD m | FC base (1) | OY6 |
| P-F34 | OY6 ga | 3.80 | USD m | FC base (1) | OY6 |
| P-F34 | OY6 consumables | 4.66 | USD m | FC base (1) | OY6 |
| P-F34 | OY6 mm contr | 3.95 | USD m | FC base (1) | OY6 |
| P-F34 | OY6 opex om | 38.64 | USD m | FC base (1) | OY6 |
| P-F34 | OY7 om fixed | 9.69 | USD m | FC base (1) | OY7 |
| P-F34 | OY7 ltsa fixed | 3.23 | USD m | FC base (1) | OY7 |
| P-F34 | OY7 ltsa var | 10.05 | USD m | FC base (1) | OY7 |
| P-F34 | OY7 insurance | 5.35 | USD m | FC base (1) | OY7 |
| P-F34 | OY7 ga | 3.89 | USD m | FC base (1) | OY7 |
| P-F34 | OY7 consumables | 4.76 | USD m | FC base (1) | OY7 |
| P-F34 | OY7 mm contr | 3.95 | USD m | FC base (1) | OY7 |
| P-F34 | OY7 opex om | 39.47 | USD m | FC base (1) | OY7 |
| P-F34 | OY8 om fixed | 9.90 | USD m | FC base (1) | OY8 |
| P-F34 | OY8 ltsa fixed | 3.31 | USD m | FC base (1) | OY8 |
| P-F34 | OY8 ltsa var | 10.27 | USD m | FC base (1) | OY8 |
| P-F34 | OY8 insurance | 5.47 | USD m | FC base (1) | OY8 |
| P-F34 | OY8 ga | 3.97 | USD m | FC base (1) | OY8 |
| P-F34 | OY8 consumables | 4.68 | USD m | FC base (1) | OY8 |
| P-F34 | OY8 mm contr | 0.66 | USD m | FC base (1) | OY8 |
| P-F34 | OY8 opex om | 39.34 | USD m | FC base (1) | OY8 |
| P-F34 | OY9 om fixed | 10.12 | USD m | FC base (1) | OY9 |
| P-F34 | OY9 ltsa fixed | 3.38 | USD m | FC base (1) | OY9 |
| P-F34 | OY9 ltsa var | 10.50 | USD m | FC base (1) | OY9 |
| P-F34 | OY9 insurance | 5.59 | USD m | FC base (1) | OY9 |
| P-F34 | OY9 ga | 4.06 | USD m | FC base (1) | OY9 |
| P-F34 | OY9 consumables | 4.95 | USD m | FC base (1) | OY9 |
| P-F34 | OY9 mm contr | 0.83 | USD m | FC base (1) | OY9 |
| P-F34 | OY9 opex om | 41.17 | USD m | FC base (1) | OY9 |
| P-F34 | OY10 om fixed | 10.34 | USD m | FC base (1) | OY10 |
| P-F34 | OY10 ltsa fixed | 3.45 | USD m | FC base (1) | OY10 |
| P-F34 | OY10 ltsa var | 10.73 | USD m | FC base (1) | OY10 |
| P-F34 | OY10 insurance | 5.72 | USD m | FC base (1) | OY10 |
| P-F34 | OY10 ga | 4.15 | USD m | FC base (1) | OY10 |
| P-F34 | OY10 consumables | 5.05 | USD m | FC base (1) | OY10 |
| P-F34 | OY10 mm contr | 0.99 | USD m | FC base (1) | OY10 |
| P-F34 | OY10 opex om | 42.03 | USD m | FC base (1) | OY10 |
| P-F35 | 2022 gas burned, base | 24.66 | million MMBtu | base | 2022 |
| P-F35 | 2022 take-or-pay payment, base | 0.00 | USD m | base | 2022 |
| P-F35 | 2022 gas burned, banking | 23.21 | million MMBtu | banking | 2022 |
| P-F35 | 2022 take-or-pay payment, banking | 0.00 | USD m | banking | 2022 |
| P-F35 | 2022 gas burned, downside | 23.28 | million MMBtu | downside | 2022 |
| P-F35 | 2022 take-or-pay payment, downside | 0.00 | USD m | downside | 2022 |
| P-F35 | 2022 gas burned, dispatch_50 | 16.12 | million MMBtu | dispatch_50 | 2022 |
| P-F35 | 2022 take-or-pay payment, dispatch_50 | 31.87 | USD m | dispatch_50 | 2022 |
| P-F35 | Annual contract quantity / take-or-pay level | 26.43 / 21.14 | million MMBtu | Inputs | 2022 |
| P-F36 | DSCR 1.30x / gearing 70% (all four sizing tests applied) | debt 592.48 (binding: gearing); candidates gearing 592.48 / DSCR 653.38 / downside 629.37 / LLCR 637.03; base min/avg DSCR 1.43x/1.67x; downside min 1.275x; LLCR 1.505x; equity IRR 12.9% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.30x / gearing 75% (all four sizing tests applied) | debt 630.14 (binding: downside); candidates gearing 640.95 / DSCR 654.18 / downside 630.14 / LLCR 638.45; base min/avg DSCR 1.35x/1.55x; downside min 1.200x; LLCR 1.418x; equity IRR 13.2% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.30x / gearing 80% (all four sizing tests applied) | debt 630.14 (binding: downside); candidates gearing 683.67 / DSCR 654.18 / downside 630.14 / LLCR 638.45; base min/avg DSCR 1.35x/1.55x; downside min 1.200x; LLCR 1.418x; equity IRR 13.2% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.35x / gearing 70% (all four sizing tests applied) | debt 592.48 (binding: gearing); candidates gearing 592.48 / DSCR 629.18 / downside 629.37 / LLCR 637.03; base min/avg DSCR 1.43x/1.67x; downside min 1.275x; LLCR 1.505x; equity IRR 12.9% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.35x / gearing 75% (all four sizing tests applied) | debt 629.95 (binding: DSCR); candidates gearing 640.91 / DSCR 629.95 / downside 630.14 / LLCR 638.44; base min/avg DSCR 1.35x/1.55x; downside min 1.200x; LLCR 1.419x; equity IRR 13.2% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.35x / gearing 80% (all four sizing tests applied) | debt 629.95 (binding: DSCR); candidates gearing 683.64 / DSCR 629.95 / downside 630.14 / LLCR 638.44; base min/avg DSCR 1.35x/1.55x; downside min 1.200x; LLCR 1.419x; equity IRR 13.2% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.40x / gearing 70% (all four sizing tests applied) | debt 592.48 (binding: gearing); candidates gearing 592.48 / DSCR 606.71 / downside 629.37 / LLCR 637.03; base min/avg DSCR 1.43x/1.67x; downside min 1.275x; LLCR 1.505x; equity IRR 12.9% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.40x / gearing 75% (all four sizing tests applied) | debt 606.94 (binding: DSCR); candidates gearing 637.17 / DSCR 606.94 / downside 629.61 / LLCR 637.53; base min/avg DSCR 1.40x/1.62x; downside min 1.245x; LLCR 1.471x; equity IRR 13.0% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.40x / gearing 80% (all four sizing tests applied) | debt 606.94 (binding: DSCR); candidates gearing 679.64 / DSCR 606.94 / downside 629.61 / LLCR 637.53; base min/avg DSCR 1.40x/1.62x; downside min 1.245x; LLCR 1.471x; equity IRR 13.0% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | Basis | Each row is a full sizing: debt = the least of the gearing cap x total funding, PV(CFADS)/DSCR target, the amount at which the downside (76.5% to the downside case) minimum DSCR is 1.20x, and the amount at which the LLCR at the first repayment (incl. DSRA) is 1.40x; the binding test is named and every candidate amount is shown. The DSCR target is the sculpting target of the base case. | text | FC base (1) | 2017-10 |
| P-F37 | VAT fc base: vat paid kcr | 7,729.0 | KCR m | FC base (1) | 2018-2022 |
| P-F37 | VAT fc base: vat paid usd | 13.9 | USD m | FC base (1) | 2018-2022 |
| P-F37 | VAT fc base: peak facility kcr | 3,281.0 | KCR m | FC base (1) | 2018-2022 |
| P-F37 | VAT fc base: interest usd total | 1.6 | USD m | FC base (1) | 2018-2022 |
| P-F37 | VAT fc base: interest construction | 1.5 | USD m | FC base (1) | 2018-2022 |
| P-F37 | VAT fc base: interest operations | 0.1 | USD m | FC base (1) | 2018-2022 |
| P-F37 | VAT fc base: last refund month | 2022-01 | month | FC base (1) | 2018-2022 |
| P-F37 | VAT actual: vat paid kcr | 7,729.0 | KCR m | Actual history (15) | 2018-2022 |
| P-F37 | VAT actual: vat paid usd | 13.7 | USD m | Actual history (15) | 2018-2022 |
| P-F37 | VAT actual: peak facility kcr | 2,663.7 | KCR m | Actual history (15) | 2018-2022 |
| P-F37 | VAT actual: interest usd total | 1.6 | USD m | Actual history (15) | 2018-2022 |
| P-F37 | VAT actual: interest construction | 1.5 | USD m | Actual history (15) | 2018-2022 |
| P-F37 | VAT actual: interest operations | 0.1 | USD m | Actual history (15) | 2018-2022 |
| P-F37 | VAT actual: last refund month | 2022-08 | month | Actual history (15) | 2018-2022 |
| P-F38 | Thin cap fc base: SHL interest total / deductible / disallowed | 196.4 / 192.5 / 3.9 | USD m | FC base (1) | life |
| P-F38 | Thin cap fc base: deductible share in the COD period | 66.0% | % | FC base (1) | COD |
| P-F38 | Thin cap actual: SHL interest total / deductible / disallowed | 202.9 / 184.5 / 18.3 | USD m | Actual history (15) | life |
| P-F38 | Thin cap actual: deductible share in the COD period | 64.3% | % | Actual history (15) | COD |
| P-F39 | LC FC base at COD (588.4 MW): two-plus-one / three-month | 36.1 / 78.2 | USD m | FC base (1) | 2021-05-01 |
| P-F39 | LC Actual at COD (581.9 MW): two-plus-one / three-month | 35.8 / 77.5 | USD m | Actual history (15) | 2021-12-01 |
| P-F39 | LC reset January 1, 2022: two-plus-one / three-month | 36.2 / 78.6 | USD m | Actual history (15) | 2022-01-01 |
| P-F39 | LC reset January 1, 2023: two-plus-one / three-month | 36.6 / 79.6 | USD m | Actual history (15) | 2023-01-01 |
| P-F39 | LC reset January 1, 2024: two-plus-one / three-month | 37.6 / 81.7 | USD m | Actual history (15) | 2024-01-01 |
| P-F39 | LC reset January 1, 2025: two-plus-one / three-month | 38.6 / 83.8 | USD m | Actual history (15) | 2025-01-01 |
| P-F40 | FX conversion losses total (2022H2-2024H1) | 6.54 | USD m | Inputs | 2024-03-29 |
| P-F40 | Energy-charge arrears matched by deferred SNHK/GCK payables, peak (2023-06-30) | 90.1 | USD m | Actual history (15) | 2023-06-30 |
| P-F40 | Overdue reduction 2024H1 / 2024H2 / 2025H1 | 37.2 / 22.3 / 12.3 | USD m | Inputs | 2025-06-30 |
| P-F40 | Implied monthly settlement installment 2024H2 / 2025H1 | 3.72 / 2.05 | USD m | Inputs | 2025-06-30 |
| P-F40 | Late payment interest received / waived | 5.22 / 3.48 | USD m | Actual history (15) | 2025-06-30 |
| P-F41 | PLCR at close, base | 1.85x | x | FC base (1) | 2018-07-17 |
| P-F41 | LLCR at close (incl. DSRA), base | 1.42x | x | FC base (1) | 2018-07-17 |
| P-F41 | PLCR at close, banking | 1.84x | x | FC banking (2) | 2018-07-17 |
| P-F41 | LLCR at close (incl. DSRA), banking | 1.42x | x | FC banking (2) | 2018-07-17 |
| P-F41 | PLCR at close, downside | 1.71x | x | FC downside (3) | 2018-07-17 |
| P-F41 | LLCR at close (incl. DSRA), downside | 1.30x | x | FC downside (3) | 2018-07-17 |
| P-F41 | FC base 2021H2: CFADS / DS / DSCR | 50.3 / 37.2 / 1.35x | USD m, x | FC base (1) | 2021H2 |
| P-F41 | FC base 2022H1: CFADS / DS / DSCR | 50.2 / 37.2 / 1.35x | USD m, x | FC base (1) | 2022H1 |
| P-F41 | FC base 2022H2: CFADS / DS / DSCR | 50.8 / 37.6 / 1.35x | USD m, x | FC base (1) | 2022H2 |
| P-F41 | FC base 2023H1: CFADS / DS / DSCR | 50.4 / 37.3 / 1.35x | USD m, x | FC base (1) | 2023H1 |
| P-F41 | FC base 2023H2: CFADS / DS / DSCR | 51.0 / 37.8 / 1.35x | USD m, x | FC base (1) | 2023H2 |
| P-F41 | FC base 2024H1: CFADS / DS / DSCR | 50.7 / 37.6 / 1.35x | USD m, x | FC base (1) | 2024H1 |
| P-F41 | FC base 2024H2: CFADS / DS / DSCR | 51.7 / 38.3 / 1.35x | USD m, x | FC base (1) | 2024H2 |
| P-F41 | FC base 2025H1: CFADS / DS / DSCR | 51.3 / 38.0 / 1.35x | USD m, x | FC base (1) | 2025H1 |
| P-F41 | FC base 2025H2: CFADS / DS / DSCR | 49.9 / 36.9 / 1.35x | USD m, x | FC base (1) | 2025H2 |
| P-F41 | FC base 2026H1: CFADS / DS / DSCR | 49.4 / 36.6 / 1.35x | USD m, x | FC base (1) | 2026H1 |
| P-F41 | FC base 2026H2: CFADS / DS / DSCR | 49.8 / 36.9 / 1.35x | USD m, x | FC base (1) | 2026H2 |
| P-F41 | FC base 2027H1: CFADS / DS / DSCR | 49.4 / 36.6 / 1.35x | USD m, x | FC base (1) | 2027H1 |
| P-F41 | FC base 2027H2: CFADS / DS / DSCR | 50.0 / 36.4 / 1.37x | USD m, x | FC base (1) | 2027H2 |
| P-F41 | FC base 2028H1: CFADS / DS / DSCR | 49.8 / 35.5 / 1.40x | USD m, x | FC base (1) | 2028H1 |
| P-F41 | FC base 2028H2: CFADS / DS / DSCR | 51.7 / 36.1 / 1.43x | USD m, x | FC base (1) | 2028H2 |
| P-F41 | FC base 2029H1: CFADS / DS / DSCR | 51.7 / 35.1 / 1.47x | USD m, x | FC base (1) | 2029H1 |
| P-F41 | FC base 2029H2: CFADS / DS / DSCR | 51.9 / 34.1 / 1.52x | USD m, x | FC base (1) | 2029H2 |
| P-F41 | FC base 2030H1: CFADS / DS / DSCR | 51.5 / 32.4 / 1.59x | USD m, x | FC base (1) | 2030H1 |
| P-F41 | FC base 2030H2: CFADS / DS / DSCR | 52.2 / 31.1 / 1.68x | USD m, x | FC base (1) | 2030H2 |
| P-F41 | FC base 2031H1: CFADS / DS / DSCR | 51.8 / 28.8 / 1.80x | USD m, x | FC base (1) | 2031H1 |
| P-F41 | FC base 2031H2: CFADS / DS / DSCR | 52.4 / 26.5 / 1.98x | USD m, x | FC base (1) | 2031H2 |
| P-F41 | FC base 2032H1: CFADS / DS / DSCR | 52.2 / 22.9 / 2.28x | USD m, x | FC base (1) | 2032H1 |
| P-F41 | FC base 2032H2: CFADS / DS / DSCR | 53.3 / 21.8 / 2.44x | USD m, x | FC base (1) | 2032H2 |
| P-F41 | FC base 2033H1: CFADS / DS / DSCR | 52.9 / 21.8 / 2.43x | USD m, x | FC base (1) | 2033H1 |
| P-F41 | FC base 2033H2: CFADS / DS / DSCR | 44.1 / 18.8 / 2.34x | USD m, x | FC base (1) | 2033H2 |
| P-F41 | FC base 2034H1: CFADS / DS / DSCR | 41.6 / 18.0 / 2.31x | USD m, x | FC base (1) | 2034H1 |
| P-F41 | FC banking 2021H2: CFADS / DS / DSCR | 50.2 / 37.2 / 1.35x | USD m, x | FC banking (2) | 2021H2 |
| P-F41 | FC banking 2022H1: CFADS / DS / DSCR | 50.1 / 37.2 / 1.35x | USD m, x | FC banking (2) | 2022H1 |
| P-F41 | FC banking 2022H2: CFADS / DS / DSCR | 50.7 / 37.6 / 1.35x | USD m, x | FC banking (2) | 2022H2 |
| P-F41 | FC banking 2023H1: CFADS / DS / DSCR | 50.3 / 37.3 / 1.35x | USD m, x | FC banking (2) | 2023H1 |
| P-F41 | FC banking 2023H2: CFADS / DS / DSCR | 50.9 / 37.8 / 1.35x | USD m, x | FC banking (2) | 2023H2 |
| P-F41 | FC banking 2024H1: CFADS / DS / DSCR | 50.6 / 37.6 / 1.35x | USD m, x | FC banking (2) | 2024H1 |
| P-F41 | FC banking 2024H2: CFADS / DS / DSCR | 51.6 / 38.3 / 1.35x | USD m, x | FC banking (2) | 2024H2 |
| P-F41 | FC banking 2025H1: CFADS / DS / DSCR | 51.3 / 38.0 / 1.35x | USD m, x | FC banking (2) | 2025H1 |
| P-F41 | FC banking 2025H2: CFADS / DS / DSCR | 49.8 / 36.9 / 1.35x | USD m, x | FC banking (2) | 2025H2 |
| P-F41 | FC banking 2026H1: CFADS / DS / DSCR | 49.3 / 36.6 / 1.35x | USD m, x | FC banking (2) | 2026H1 |
| P-F41 | FC banking 2026H2: CFADS / DS / DSCR | 49.7 / 36.9 / 1.35x | USD m, x | FC banking (2) | 2026H2 |
| P-F41 | FC banking 2027H1: CFADS / DS / DSCR | 49.3 / 36.6 / 1.35x | USD m, x | FC banking (2) | 2027H1 |
| P-F41 | FC banking 2027H2: CFADS / DS / DSCR | 49.9 / 36.4 / 1.37x | USD m, x | FC banking (2) | 2027H2 |
| P-F41 | FC banking 2028H1: CFADS / DS / DSCR | 49.7 / 35.5 / 1.40x | USD m, x | FC banking (2) | 2028H1 |
| P-F41 | FC banking 2028H2: CFADS / DS / DSCR | 51.6 / 36.1 / 1.43x | USD m, x | FC banking (2) | 2028H2 |
| P-F41 | FC banking 2029H1: CFADS / DS / DSCR | 51.7 / 35.2 / 1.47x | USD m, x | FC banking (2) | 2029H1 |
| P-F41 | FC banking 2029H2: CFADS / DS / DSCR | 51.8 / 34.1 / 1.52x | USD m, x | FC banking (2) | 2029H2 |
| P-F41 | FC banking 2030H1: CFADS / DS / DSCR | 51.5 / 32.4 / 1.59x | USD m, x | FC banking (2) | 2030H1 |
| P-F41 | FC banking 2030H2: CFADS / DS / DSCR | 52.1 / 31.2 / 1.67x | USD m, x | FC banking (2) | 2030H2 |
| P-F41 | FC banking 2031H1: CFADS / DS / DSCR | 51.7 / 28.9 / 1.79x | USD m, x | FC banking (2) | 2031H1 |
| P-F41 | FC banking 2031H2: CFADS / DS / DSCR | 52.3 / 26.6 / 1.97x | USD m, x | FC banking (2) | 2031H2 |
| P-F41 | FC banking 2032H1: CFADS / DS / DSCR | 52.1 / 23.0 / 2.27x | USD m, x | FC banking (2) | 2032H1 |
| P-F41 | FC banking 2032H2: CFADS / DS / DSCR | 53.2 / 21.8 / 2.44x | USD m, x | FC banking (2) | 2032H2 |
| P-F41 | FC banking 2033H1: CFADS / DS / DSCR | 52.8 / 21.8 / 2.43x | USD m, x | FC banking (2) | 2033H1 |
| P-F41 | FC banking 2033H2: CFADS / DS / DSCR | 44.8 / 18.8 / 2.38x | USD m, x | FC banking (2) | 2033H2 |
| P-F41 | FC banking 2034H1: CFADS / DS / DSCR | 41.6 / 18.0 / 2.31x | USD m, x | FC banking (2) | 2034H1 |
| P-F41 | FC downside 2021H2: CFADS / DS / DSCR | 46.8 / 37.2 / 1.26x | USD m, x | FC downside (3) | 2021H2 |
| P-F41 | FC downside 2022H1: CFADS / DS / DSCR | 46.5 / 37.2 / 1.25x | USD m, x | FC downside (3) | 2022H1 |
| P-F41 | FC downside 2022H2: CFADS / DS / DSCR | 46.7 / 37.6 / 1.24x | USD m, x | FC downside (3) | 2022H2 |
| P-F41 | FC downside 2023H1: CFADS / DS / DSCR | 46.4 / 37.3 / 1.24x | USD m, x | FC downside (3) | 2023H1 |
| P-F41 | FC downside 2023H2: CFADS / DS / DSCR | 47.3 / 37.8 / 1.25x | USD m, x | FC downside (3) | 2023H2 |
| P-F41 | FC downside 2024H1: CFADS / DS / DSCR | 46.5 / 37.6 / 1.24x | USD m, x | FC downside (3) | 2024H1 |
| P-F41 | FC downside 2024H2: CFADS / DS / DSCR | 46.0 / 38.3 / 1.20x | USD m, x | FC downside (3) | 2024H2 |
| P-F41 | FC downside 2025H1: CFADS / DS / DSCR | 45.8 / 38.0 / 1.21x | USD m, x | FC downside (3) | 2025H1 |
| P-F41 | FC downside 2025H2: CFADS / DS / DSCR | 45.8 / 36.9 / 1.24x | USD m, x | FC downside (3) | 2025H2 |
| P-F41 | FC downside 2026H1: CFADS / DS / DSCR | 45.5 / 36.6 / 1.24x | USD m, x | FC downside (3) | 2026H1 |
| P-F41 | FC downside 2026H2: CFADS / DS / DSCR | 45.5 / 36.9 / 1.23x | USD m, x | FC downside (3) | 2026H2 |
| P-F41 | FC downside 2027H1: CFADS / DS / DSCR | 45.1 / 36.6 / 1.23x | USD m, x | FC downside (3) | 2027H1 |
| P-F41 | FC downside 2027H2: CFADS / DS / DSCR | 46.1 / 36.6 / 1.26x | USD m, x | FC downside (3) | 2027H2 |
| P-F41 | FC downside 2028H1: CFADS / DS / DSCR | 44.9 / 35.9 / 1.25x | USD m, x | FC downside (3) | 2028H1 |
| P-F41 | FC downside 2028H2: CFADS / DS / DSCR | 45.1 / 36.8 / 1.22x | USD m, x | FC downside (3) | 2028H2 |
| P-F41 | FC downside 2029H1: CFADS / DS / DSCR | 45.1 / 36.4 / 1.24x | USD m, x | FC downside (3) | 2029H1 |
| P-F41 | FC downside 2029H2: CFADS / DS / DSCR | 47.4 / 35.9 / 1.32x | USD m, x | FC downside (3) | 2029H2 |
| P-F41 | FC downside 2030H1: CFADS / DS / DSCR | 47.5 / 34.7 / 1.37x | USD m, x | FC downside (3) | 2030H1 |
| P-F41 | FC downside 2030H2: CFADS / DS / DSCR | 47.7 / 34.0 / 1.40x | USD m, x | FC downside (3) | 2030H2 |
| P-F41 | FC downside 2031H1: CFADS / DS / DSCR | 47.3 / 32.4 / 1.46x | USD m, x | FC downside (3) | 2031H1 |
| P-F41 | FC downside 2031H2: CFADS / DS / DSCR | 48.3 / 31.1 / 1.55x | USD m, x | FC downside (3) | 2031H2 |
| P-F41 | FC downside 2032H1: CFADS / DS / DSCR | 47.5 / 28.6 / 1.66x | USD m, x | FC downside (3) | 2032H1 |
| P-F41 | FC downside 2032H2: CFADS / DS / DSCR | 47.0 / 25.9 / 1.82x | USD m, x | FC downside (3) | 2032H2 |
| P-F41 | FC downside 2033H1: CFADS / DS / DSCR | 46.9 / 21.8 / 2.15x | USD m, x | FC downside (3) | 2033H1 |
| P-F41 | FC downside 2033H2: CFADS / DS / DSCR | 46.6 / 18.8 / 2.47x | USD m, x | FC downside (3) | 2033H2 |
| P-F41 | FC downside 2034H1: CFADS / DS / DSCR | 46.4 / 18.0 / 2.58x | USD m, x | FC downside (3) | 2034H1 |
| P-F41 | Actual 2022H1: CFADS / DS / DSCR | 44.8 / 35.6 / 1.26x | USD m, x | Actual history (15) | 2022H1 |
| P-F41 | Actual 2022H2: CFADS / DS / DSCR | 37.4 / 37.5 / 1.00x | USD m, x | Actual history (15) | 2022H2 |
| P-F41 | Actual 2023H1: CFADS / DS / DSCR | 35.8 / 39.1 / 0.91x | USD m, x | Actual history (15) | 2023H1 |
| P-F41 | Actual 2023H2: CFADS / DS / DSCR | 56.2 / 30.6 / 1.83x | USD m, x | Actual history (15) | 2023H2 |
| P-F41 | Actual 2024H1: CFADS / DS / DSCR | 57.4 / 44.1 / 1.30x | USD m, x | Actual history (15) | 2024H1 |
| P-F41 | Actual 2024H2: CFADS / DS / DSCR | 56.7 / 44.3 / 1.28x | USD m, x | Actual history (15) | 2024H2 |
| P-F41 | Actual 2025H1: CFADS / DS / DSCR | 55.4 / 42.2 / 1.31x | USD m, x | Actual history (15) | 2025H1 |
| P-F41 | Actual 2025H2: CFADS / DS / DSCR | 51.7 / 32.5 / 1.59x | USD m, x | Actual history (15) | 2025H2 |
| P-F41 | Actual 2026H1: CFADS / DS / DSCR | 49.1 / 30.9 / 1.59x | USD m, x | Actual history (15) | 2026H1 |
| P-F41 | Actual 2026H2: CFADS / DS / DSCR | 49.9 / 31.3 / 1.59x | USD m, x | Actual history (15) | 2026H2 |
| P-F42 | Monte Carlo inputs | availability_shock: per operating year, normal(0, 2.0 points), truncated to -10/+5 points, independent across years; dispatch: one draw per run, triangular(55.0%, 76.5%, 85.0%); heat_rate_degradation: non-recoverable rate per year, normal(0.12%, 0.04%), floored at 0; fx: KCR depreciation drift per year, normal(5.19%, 3.0%) applied to the FC FX path; debt: locked at the FC base contract (amount and repayment profile); 1000 runs, seed 20180717 | text | FC base (1), debt locked | 2018-07-17 |
| P-F42 | Minimum DSCR P10 / P50 / P90 | 1.32x / 1.34x / 1.35x | x | FC base (1) | 2018-07-17 |
| P-F42 | Equity IRR P10 / P50 / P90 | 12.8% / 13.1% / 13.6% | % | FC base (1) | 2018-07-17 |
| P-F42 | Probability of a historic DSCR below 1.20x / 1.10x in any test | 0.0% / 0.0% | % | FC base (1) | 2018-07-17 |
| P-F42 | Minimum DSCR histogram (bins 1.0,1.1,1.2,1.25,1.3,1.35,1.4,1.5,+) | 0, 0, 0, 25, 769, 206, 0, 0 | runs | FC base (1) | 2018-07-17 |
| P-F43 | Sizing passes to USD 1,000 tolerance (profile, debt, notional) | 11 | passes | FC base (1) | 2018-07-17 |
| P-F43 | Sizing residuals by pass | 529.5, 529.5, 625.6, 14.25, 3.492, 0.08721, 0.06927, 0.0008557, 0.0005, 1.838e-05, 3.857e-06 | USD m | FC base (1) | 2018-07-17 |
| P-F43 | Construction fixed-point passes (Python) | 12 | passes | FC base (1) | 2018-07-17 |
| P-F43 | Closed-form total funding at the 75% gearing cap | 857.4 | USD m | FC base (1) | 2018-07-17 |
| P-F43 | Pro rata: total funding / debt / IDC incl. swap and PRI | 854.6 / 629.9 / 63.6 | USD m | FC base (1) | 2018-07-17 |
| P-F43 | Equity first: total funding / debt / equity / IDC / commitment fees | 840.7 / 630.5 / 210.2 / 47.2 / 12.6 | USD m | FC base (1) variant | 2018-07-17 |
| P-F44 | OY1 revenue: capacity / VOM / fuel / GTA / take-or-pay / total | 121.0 / 15.3 / 155.5 / 27.9 / 0.0 / 319.7 | USD m | FC base (1) | OY1 |
| P-F44 | OY2 revenue: capacity / VOM / fuel / GTA / take-or-pay / total | 121.9 / 15.5 / 157.5 / 28.3 / 0.0 / 323.1 | USD m | FC base (1) | OY2 |
| P-F44 | OY3 revenue: capacity / VOM / fuel / GTA / take-or-pay / total | 122.7 / 15.8 / 161.0 / 28.8 / 0.0 / 328.4 | USD m | FC base (1) | OY3 |
| P-F44 | OY4 revenue: capacity / VOM / fuel / GTA / take-or-pay / total | 123.7 / 15.8 / 160.6 / 29.1 / 0.0 / 329.1 | USD m | FC base (1) | OY4 |
| P-F44 | OY5 revenue: capacity / VOM / fuel / GTA / take-or-pay / total | 124.6 / 16.5 / 167.3 / 29.6 / 0.0 / 338.0 | USD m | FC base (1) | OY5 |
| P-F44 | OY6 revenue: capacity / VOM / fuel / GTA / take-or-pay / total | 125.6 / 16.8 / 170.2 / 30.0 / 0.0 / 342.5 | USD m | FC base (1) | OY6 |
| P-F44 | OY7 revenue: capacity / VOM / fuel / GTA / take-or-pay / total | 126.5 / 17.1 / 173.5 / 30.5 / 0.0 / 347.7 | USD m | FC base (1) | OY7 |
| P-F44 | OY8 revenue: capacity / VOM / fuel / GTA / take-or-pay / total | 126.6 / 16.9 / 170.7 / 30.7 / 0.0 / 344.9 | USD m | FC base (1) | OY8 |
| P-F44 | OY9 revenue: capacity / VOM / fuel / GTA / take-or-pay / total | 128.6 / 17.8 / 180.4 / 31.4 / 0.0 / 358.1 | USD m | FC base (1) | OY9 |
| P-F44 | OY10 revenue: capacity / VOM / fuel / GTA / take-or-pay / total | 129.6 / 18.2 / 183.8 / 31.8 / 0.0 / 363.4 | USD m | FC base (1) | OY10 |
| P-F44 | 2022H1 revenue build: om | 6.00 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: avail | 93.50 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: energy | 1,822,457.67 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: hr_act | 6,463.34 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: hr_con | 6,474.36 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: gas_price | 6.34 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: gas_mmbtu | 12,370,265.73 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: us_tar | 110.90 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: kc_tar | 142.84 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: fx | 627.83 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: cap_charge | 14.67 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: fom_charge | 2.51 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: avail_factor | 1.00 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: cap_pay | 60.67 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: vom_rate | 4.21 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: vom | 7.68 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: fuel_rev | 78.60 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: gta_res | 11.49 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: gta_com | 2.49 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: top_pay | 0.00 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: revenue | 160.94 | see model row | FC base (1) | 2022H1 |
| P-F44 | 2022H1 revenue build: fuel_cost | 78.47 | see model row | FC base (1) | 2022H1 |
| P-F45 | OY1 revenue (lenders basis) | 319.7 | USD m | FC base (1) | OY1 |
| P-F45 | OY1 operating costs (lenders basis) | 218.2 | USD m | FC base (1) | OY1 |
| P-F45 | OY1 ebitda (lenders basis) | 101.5 | USD m | FC base (1) | OY1 |
| P-F45 | OY1 depreciation (lenders basis) | 33.5 | USD m | FC base (1) | OY1 |
| P-F45 | OY1 finance costs (lenders basis) | 55.1 | USD m | FC base (1) | OY1 |
| P-F45 | OY1 current tax (lenders basis) | 0.0 | USD m | FC base (1) | OY1 |
| P-F45 | OY1 deferred tax (lenders basis) | -10.0 | USD m | FC base (1) | OY1 |
| P-F45 | OY1 net income (lenders basis) | 22.9 | USD m | FC base (1) | OY1 |
| P-F45 | OY1 cfads (lenders basis) | 85.6 | USD m | FC base (1) | OY1 |
| P-F45 | OY1 debt service (lenders basis) | 62.0 | USD m | FC base (1) | OY1 |
| P-F45 | OY1 distributions (lenders basis) | 23.4 | USD m | FC base (1) | OY1 |
| P-F45 | OY2 revenue (lenders basis) | 323.1 | USD m | FC base (1) | OY2 |
| P-F45 | OY2 operating costs (lenders basis) | 221.1 | USD m | FC base (1) | OY2 |
| P-F45 | OY2 ebitda (lenders basis) | 102.0 | USD m | FC base (1) | OY2 |
| P-F45 | OY2 depreciation (lenders basis) | 33.5 | USD m | FC base (1) | OY2 |
| P-F45 | OY2 finance costs (lenders basis) | 59.8 | USD m | FC base (1) | OY2 |
| P-F45 | OY2 current tax (lenders basis) | 0.0 | USD m | FC base (1) | OY2 |
| P-F45 | OY2 deferred tax (lenders basis) | -10.0 | USD m | FC base (1) | OY2 |
| P-F45 | OY2 net income (lenders basis) | 18.9 | USD m | FC base (1) | OY2 |
| P-F45 | OY2 cfads (lenders basis) | 101.1 | USD m | FC base (1) | OY2 |
| P-F45 | OY2 debt service (lenders basis) | 74.9 | USD m | FC base (1) | OY2 |
| P-F45 | OY2 distributions (lenders basis) | 26.1 | USD m | FC base (1) | OY2 |
| P-F45 | OY3 revenue (lenders basis) | 328.4 | USD m | FC base (1) | OY3 |
| P-F45 | OY3 operating costs (lenders basis) | 225.9 | USD m | FC base (1) | OY3 |
| P-F45 | OY3 ebitda (lenders basis) | 102.5 | USD m | FC base (1) | OY3 |
| P-F45 | OY3 depreciation (lenders basis) | 33.5 | USD m | FC base (1) | OY3 |
| P-F45 | OY3 finance costs (lenders basis) | 56.9 | USD m | FC base (1) | OY3 |
| P-F45 | OY3 current tax (lenders basis) | 0.0 | USD m | FC base (1) | OY3 |
| P-F45 | OY3 deferred tax (lenders basis) | -10.0 | USD m | FC base (1) | OY3 |
| P-F45 | OY3 net income (lenders basis) | 22.1 | USD m | FC base (1) | OY3 |
| P-F45 | OY3 cfads (lenders basis) | 101.6 | USD m | FC base (1) | OY3 |
| P-F45 | OY3 debt service (lenders basis) | 75.2 | USD m | FC base (1) | OY3 |
| P-F45 | OY3 distributions (lenders basis) | 25.9 | USD m | FC base (1) | OY3 |
| P-F45 | Balance sheet 2021-06-30: plant | 830.9 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2021-06-30: cash in project accounts | 39.1 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2021-06-30: of which dsra | 37.2 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2021-06-30: receivables | 39.1 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2021-06-30: of which overdue | 0.0 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2021-06-30: inventory | 5.3 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2021-06-30: deferred tax asset | 1.7 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2021-06-30: total assets | 916.1 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2021-06-30: senior debt | 629.9 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2021-06-30: shareholder loans | 207.4 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2021-06-30: payables | 24.1 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2021-06-30: deferred tax liability | 0.0 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2021-06-30: share capital | 44.9 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2021-06-30: retained earnings | 9.7 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2021-06-30: total liabilities and equity | 916.1 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2021-06-30: balance check | -0.0 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | Balance sheet 2022-06-30: plant | 797.4 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2022-06-30: cash in project accounts | 38.5 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2022-06-30: of which dsra | 37.6 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2022-06-30: receivables | 40.0 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2022-06-30: of which overdue | 0.0 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2022-06-30: inventory | 5.3 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2022-06-30: deferred tax asset | 11.7 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2022-06-30: total assets | 892.9 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2022-06-30: senior debt | 598.1 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2022-06-30: shareholder loans | 199.4 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2022-06-30: payables | 24.7 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2022-06-30: deferred tax liability | 0.0 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2022-06-30: share capital | 44.9 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2022-06-30: retained earnings | 25.8 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2022-06-30: total liabilities and equity | 892.9 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2022-06-30: balance check | -0.0 | USD m | FC base (1) | 2022-06-30 |
| P-F45 | Balance sheet 2023-06-30: plant | 764.0 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2023-06-30: cash in project accounts | 39.4 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2023-06-30: of which dsra | 37.8 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2023-06-30: receivables | 40.5 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2023-06-30: of which overdue | 0.0 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2023-06-30: inventory | 5.3 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2023-06-30: deferred tax asset | 21.7 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2023-06-30: total assets | 871.0 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2023-06-30: senior debt | 563.7 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2023-06-30: shareholder loans | 192.0 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2023-06-30: payables | 25.2 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2023-06-30: deferred tax liability | 0.0 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2023-06-30: share capital | 44.9 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2023-06-30: retained earnings | 45.2 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2023-06-30: total liabilities and equity | 871.0 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2023-06-30: balance check | -0.0 | USD m | FC base (1) | 2023-06-30 |
| P-F45 | Balance sheet 2024-06-30: plant | 730.5 | USD m | FC base (1) | 2024-06-30 |
| P-F45 | Balance sheet 2024-06-30: cash in project accounts | 40.8 | USD m | FC base (1) | 2024-06-30 |
| P-F45 | Balance sheet 2024-06-30: of which dsra | 38.3 | USD m | FC base (1) | 2024-06-30 |
| P-F45 | Balance sheet 2024-06-30: receivables | 40.8 | USD m | FC base (1) | 2024-06-30 |
| P-F45 | Balance sheet 2024-06-30: of which overdue | 0.0 | USD m | FC base (1) | 2024-06-30 |
| P-F45 | Balance sheet 2024-06-30: inventory | 5.3 | USD m | FC base (1) | 2024-06-30 |
| P-F45 | Balance sheet 2024-06-30: deferred tax asset | 31.8 | USD m | FC base (1) | 2024-06-30 |
| P-F45 | Balance sheet 2024-06-30: total assets | 849.2 | USD m | FC base (1) | 2024-06-30 |
| P-F45 | Balance sheet 2024-06-30: senior debt | 526.8 | USD m | FC base (1) | 2024-06-30 |
| P-F45 | Balance sheet 2024-06-30: shareholder loans | 184.3 | USD m | FC base (1) | 2024-06-30 |
| P-F45 | Balance sheet 2024-06-30: payables | 25.4 | USD m | FC base (1) | 2024-06-30 |
| P-F45 | Balance sheet 2024-06-30: deferred tax liability | 0.0 | USD m | FC base (1) | 2024-06-30 |
| P-F45 | Balance sheet 2024-06-30: share capital | 44.9 | USD m | FC base (1) | 2024-06-30 |
| P-F45 | Balance sheet 2024-06-30: retained earnings | 67.9 | USD m | FC base (1) | 2024-06-30 |
| P-F45 | Balance sheet 2024-06-30: total liabilities and equity | 849.2 | USD m | FC base (1) | 2024-06-30 |
| P-F45 | Balance sheet 2024-06-30: balance check | 0.0 | USD m | FC base (1) | 2024-06-30 |
| P-F37 | Working capital 2021H1: receivables / gas / GTA / O&M-LTSA / other payables / net | 39.1 / 19.0 / 2.3 / 1.7 / 1.2 / 15.0 | USD m | FC base (1) | 2021H1 |
| P-F37 | Working capital 2021H2: receivables / gas / GTA / O&M-LTSA / other payables / net | 39.0 / 18.9 / 2.3 / 1.7 / 1.2 / 15.0 | USD m | FC base (1) | 2021H2 |
| P-F37 | Working capital 2022H1: receivables / gas / GTA / O&M-LTSA / other payables / net | 40.0 / 19.5 / 2.3 / 1.7 / 1.2 / 15.3 | USD m | FC base (1) | 2022H1 |
| P-F37 | Working capital 2022H2: receivables / gas / GTA / O&M-LTSA / other payables / net | 39.3 / 19.1 / 2.3 / 1.7 / 1.2 / 15.1 | USD m | FC base (1) | 2022H2 |
| P-F37 | Working capital 2023H1: receivables / gas / GTA / O&M-LTSA / other payables / net | 40.5 / 19.8 / 2.4 / 1.7 / 1.2 / 15.4 | USD m | FC base (1) | 2023H1 |
| P-F37 | Working capital 2023H2: receivables / gas / GTA / O&M-LTSA / other payables / net | 40.1 / 19.6 / 2.3 / 1.7 / 1.2 / 15.2 | USD m | FC base (1) | 2023H2 |
| P-F37 | Working capital 2024H1: receivables / gas / GTA / O&M-LTSA / other payables / net | 40.8 / 20.0 / 2.4 / 1.8 / 1.2 / 15.4 | USD m | FC base (1) | 2024H1 |
| P-F40 | Netting set-off per month 2023H2 / 2024H1 (fall in deferred SNHK/GCK payables) | 5.44 / 4.96 | USD m | Actual history (15) | 2024-03-31 |
| P-F40 | Guarantee demand 2023-04-18 (USD 21.6 m): paid 2023-07-26 | 99 | days | Inputs | 2023-04-18 |
| P-F40 | Guarantee demand 2023-07-12 (USD 18.9 m): paid 2023-11-30 | 141 | days | Inputs | 2023-07-12 |
| P-F40 | Guarantee demand 2023-10-09 (USD 17.4 m): paid folded into the 2024-03-21 settlement | 164 | days | Inputs | 2023-10-09 |
| P-F40 | FX queue duration (2022-11-07 to 2024-03-29) | 508 | days | Inputs | 2024-03-29 |
| P-F09 | ECA-covered tranche: share of principal repaid within 24 months of COD (FC base; minimum 2%) | 11.5% | % | FC base (1) | 2018-07-17 |
| P-F09 | ECA-covered tranche, actual (equal installments from 2022H1): WAL / tenor / first repayment / repaid within 24 months | 6.58 y / 12.58 y / 7 months / 12.0% | years, months, % | Actual history (15) | 2021-12-01 |
| P-F07 | Equity at close by sponsor: Kilnworth (60%): share capital / SHL / total | 26.95 / 107.81 / 134.76 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Equity at close by sponsor: Talme (25%): share capital / SHL / total | 11.23 / 44.92 / 56.15 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Equity at close by sponsor: ABDB fund (15%): share capital / SHL / total | 6.74 / 26.95 / 33.69 | USD m | FC base (1) | 2018-07-17 |
| P-F46 | GTA 2022: reservation / commodity / total passed to SEKA (= GCK revenue from Belanou) | 23.2 / 5.4 / 28.5 | USD m | Actual history (15) | 2022-12-31 |
| P-F46 | Gas burned 2022 | 26.64 | million MMBtu | Actual history (15) | 2022-12-31 |
| P-F47 | Fuel margin from heat-rate headroom, OY1 | 0.28 | USD m | FC base (1) | OY1 |
| P-F47 | Fuel margin from heat-rate headroom, OY2 | 0.25 | USD m | FC base (1) | OY2 |
| P-F47 | Fuel margin from heat-rate headroom, OY5 | 0.17 | USD m | FC base (1) | OY5 |
| P-F47 | Fuel margin from heat-rate headroom, OY10 | 0.00 | USD m | FC base (1) | OY10 |
| P-F47 | Fuel margin from heat-rate headroom, OY15 | -0.20 | USD m | FC base (1) | OY15 |
| P-F47 | Fuel margin from heat-rate headroom, OY20 | -0.42 | USD m | FC base (1) | OY20 |
| P-F47 | Fuel margin from heat-rate headroom, OY25 | -0.71 | USD m | FC base (1) | OY25 |
| P-F47 | Contracted / plant heat rate, 2021H2 (incl. part-load 2.3%) | 6,471 / 6,459 | kJ/kWh | FC base (1) | 2021H2 |
| P-F48 | LTSA 128,000 EOH run-out, base | 2036-06-30 (8,439 EOH/yr; 15.2 years) | date | base | 2036-06-30 |
| P-F48 | LTSA 128,000 EOH run-out, banking | 2037-05-26 (7,965 EOH/yr; 16.1 years) | date | banking | 2037-05-26 |
| P-F48 | LTSA 128,000 EOH run-out, low_dispatch_58 | 2041-01-19 (6,490 EOH/yr; 19.7 years) | date | low_dispatch_58 | 2041-01-19 |
| P-F48 | LTSA 128,000 EOH run-out, actual | 2037-01-30 (8,439 EOH/yr; 15.2 years) | date | actual | 2037-01-30 |
| P-F48 | 16-year LTSA date (FC base / actual) | 2037-04-30 / 2037-11-30 | date | Inputs | 2037 |
| P-F49 | First utilization, ECA | 26.87 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | First utilization, A | 19.71 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | First utilization, B | 8.96 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | First utilization, COM | 34.04 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | first utilization total | 89.58 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | equity at close | 31.94 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | of which lntp credit | 14.20 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | equity cash at close | 17.74 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | epc advance gross | 57.18 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | epc advance cash net of lntp | 42.98 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | upfront fees | 9.90 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | first eca premium | 2.92 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | advisers at close | 6.28 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | insurance at close | 6.48 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | idc month1 | 0.00 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | total uses month1 | 121.52 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | Use in Month 1 (itemized): EPC advance (10% of the EPC price; includes the USD 14.20m LNTP already paid by equity) | 57.184 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | Use in Month 1 (itemized): Owner's costs, Month 1 | 5.542 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | Use in Month 1 (itemized): Insurance at close (85% of the construction premium) | 6.477 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | Use in Month 1 (itemized): Development cost reimbursement | 21.430 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | Use in Month 1 (itemized): Development fee | 11.200 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | Use in Month 1 (itemized): Lenders' advisers and legal at close (70%) | 6.279 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | Use in Month 1 (itemized): Upfront fees | 9.903 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | Use in Month 1 (itemized): First ECA premium installment | 2.916 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | Use in Month 1 (itemized): Commitment fees, Month 1 (senior tranches) | 0.547 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | Use in Month 1 (itemized): Standby facility commitment fee, Month 1 | 0.024 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | Use in Month 1 (itemized): Agency fees, Month 1 | 0.021 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | Use in Month 1 (itemized): Interest during construction, Month 1 (no balance outstanding before the first utilization) | 0.000 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | Uses in Month 1, sum of the itemized lines (= total uses month 1; sources: first utilization + equity at close) | 121.522 | USD m | FC base (1) | 2018-07-17 |
| P-F49 | development cost reimbursement: Kilnworth | 15.45 | USD m | Annex 1.14 | 2018-07-17 |
| P-F49 | development cost reimbursement: Talme | 5.98 | USD m | Annex 1.14 | 2018-07-17 |
| P-F49 | development cost reimbursement: total | 21.43 | USD m | Annex 1.14 | 2018-07-17 |
| P-F49 | development fee: Kilnworth | 7.84 | USD m | Annex 1.14 | 2018-07-17 |
| P-F49 | development fee: Talme | 3.36 | USD m | Annex 1.14 | 2018-07-17 |
| P-F49 | development fee: total | 11.20 | USD m | Annex 1.14 | 2018-07-17 |
| P-F49 | abdb fund premium paid by fund: Kilnworth | 3.2333 | USD m | Annex 1.14 | 2018-07-17 |
| P-F49 | abdb fund premium paid by fund: Talme | 1.6167 | USD m | Annex 1.14 | 2018-07-17 |
| P-F49 | abdb fund premium paid by fund: total | 4.8500 | USD m | Annex 1.14 | 2018-07-17 |
| P-F49 | Total development receipts at close, Kilnworth | 26.52 | USD m | Annex 1.14 | 2018-07-17 |
| P-F49 | Total development receipts at close, Talme | 10.96 | USD m | Annex 1.14 | 2018-07-17 |
| P-F50 | PV of the 7.5 bps swap charge / at 10 bps / difference | 2.84 / 3.79 / 0.95 | USD m | FC base (1) | 2018-07-17 |
| P-F51 | PRI premium 2018H2 (insured amount 34.2) | 0.12 | USD m | Actual history (15) | 2018H2 |
| P-F51 | PRI premium 2019H1 (insured amount 50.2) | 0.23 | USD m | Actual history (15) | 2019H1 |
| P-F51 | PRI premium 2019H2 (insured amount 81.6) | 0.36 | USD m | Actual history (15) | 2019H2 |
| P-F51 | PRI premium 2020H1 (insured amount 121.3) | 0.56 | USD m | Actual history (15) | 2020H1 |
| P-F51 | PRI premium 2020H2 (insured amount 157.7) | 0.79 | USD m | Actual history (15) | 2020H2 |
| P-F51 | PRI premium 2021H1 (insured amount 184.5) | 0.97 | USD m | Actual history (15) | 2021H1 |
| P-F51 | PRI premium 2021H2 (insured amount 215.4) | 1.13 | USD m | Actual history (15) | 2021H2 |
| P-F51 | PRI premium 2022H1 (insured amount 215.4) | 1.23 | USD m | Actual history (15) | 2022H1 |
| P-F51 | PRI premium 2022H2 (insured amount 205.1) | 1.19 | USD m | Actual history (15) | 2022H2 |
| P-F51 | PRI premium 2023H1 (insured amount 200.5) | 1.14 | USD m | Actual history (15) | 2023H1 |
| P-F51 | PRI premium 2023H2 (insured amount 195.8) | 1.14 | USD m | Actual history (15) | 2023H2 |
| P-F51 | PRI premium 2024H1 (insured amount 193.7) | 1.11 | USD m | Actual history (15) | 2024H1 |
| P-F51 | PRI premium 2024H2 (insured amount 187.6) | 1.09 | USD m | Actual history (15) | 2024H2 |
| P-F51 | PRI premium 2025H1 (insured amount 181.1) | 1.03 | USD m | Actual history (15) | 2025H1 |
| P-F51 | PRI premium total to cancellation (actual) | 12.09 | USD m | Actual history (15) | 2025-06-30 |
| P-F52 | EPC cumulative progress 2018-Q3: planned / actual | 10.0% / 10.0% | % of contract price | FC base / actual | 2018-Q3 |
| P-F52 | EPC cumulative progress 2018-Q4: planned / actual | 11.1% / 10.7% | % of contract price | FC base / actual | 2018-Q4 |
| P-F52 | EPC cumulative progress 2019-Q1: planned / actual | 15.5% / 13.6% | % of contract price | FC base / actual | 2019-Q1 |
| P-F52 | EPC cumulative progress 2019-Q2: planned / actual | 24.1% / 19.1% | % of contract price | FC base / actual | 2019-Q2 |
| P-F52 | EPC cumulative progress 2019-Q3: planned / actual | 36.6% / 27.3% | % of contract price | FC base / actual | 2019-Q3 |
| P-F52 | EPC cumulative progress 2019-Q4: planned / actual | 51.2% / 37.7% | % of contract price | FC base / actual | 2019-Q4 |
| P-F52 | EPC cumulative progress 2020-Q1: planned / actual | 65.9% / 49.3% | % of contract price | FC base / actual | 2020-Q1 |
| P-F52 | EPC cumulative progress 2020-Q2: planned / actual | 78.4% / 61.1% | % of contract price | FC base / actual | 2020-Q2 |
| P-F52 | EPC cumulative progress 2020-Q3: planned / actual | 87.0% / 71.9% | % of contract price | FC base / actual | 2020-Q3 |
| P-F52 | EPC cumulative progress 2020-Q4: planned / actual | 91.4% / 80.9% | % of contract price | FC base / actual | 2020-Q4 |
| P-F52 | EPC cumulative progress 2021-Q1: planned / actual | 92.5% / 87.4% | % of contract price | FC base / actual | 2021-Q1 |
| P-F52 | EPC cumulative progress 2021-Q2: planned / actual | 100.0% / 91.1% | % of contract price | FC base / actual | 2021-Q2 |
| P-F52 | EPC cumulative progress 2021-Q3: planned / actual | 100.0% / 92.4% | % of contract price | FC base / actual | 2021-Q3 |
| P-F52 | EPC cumulative progress 2021-Q4: planned / actual | 100.0% / 100.0% | % of contract price | FC base / actual | 2021-Q4 |
| P-F53 | ECL allowance 2022H2 (normal / 1-90 / 91-180 / >180 days aged) | 3.31 (40.5 / 25.2 / 25.2 / 18.4) | USD m | Actual history (15) | 2022H2 |
| P-F53 | ECL allowance 2023H1 (normal / 1-90 / 91-180 / >180 days aged) | 8.17 (40.0 / 21.9 / 21.9 / 68.9) | USD m | Actual history (15) | 2023H1 |
| P-F53 | ECL allowance 2023H2 (normal / 1-90 / 91-180 / >180 days aged) | 7.26 (39.8 / 0.0 / 0.0 / 71.8) | USD m | Actual history (15) | 2023H2 |
| P-F53 | Swap MTM to project (= hedge reserve, pre-tax), 2018-07-17 (2.872%) | -2.84 | USD m | Actual history (15) | 2018-07-17 |
| P-F53 | Swap MTM to project (= hedge reserve, pre-tax), 2022-12-31 (4.05%) | 28.93 | USD m | Actual history (15) | 2022-12-31 |
| P-F53 | Swap MTM to project (= hedge reserve, pre-tax), 2023-06-30 (4.35%) | 33.89 | USD m | Actual history (15) | 2023-06-30 |
| P-F53 | Swap MTM to project (= hedge reserve, pre-tax), 2025-06-30 before termination (3.68%) | 13.08 | USD m | Actual history (15) | 2025-06-30 |
| P-F53 | Swap MTM to project (= hedge reserve, pre-tax), 2025-06-30 after termination (52%) | 6.80 | USD m | Actual history (15) | 2025-06-30 |
| P-F53 | Swap MTM to project (= hedge reserve, pre-tax), 2026-09-30 (3.40%, approximate) | 3.51 | USD m | Actual history (15) | 2026-09-30 |
| P-F54 | 2024 estimate: GloBE income / covered taxes / SBIE / UK top-up on Kilnworth share | 30.7 / 0.00 / 58.2 / 0.00 | USD m | Actual history (15) | 2024-12-31 |
| P-F54 | 2025 estimate: GloBE income / covered taxes / SBIE / UK top-up on Kilnworth share | 38.2 / 0.00 / 54.2 / 0.00 | USD m | Actual history (15) | 2025-12-31 |
| P-F54 | 2026 estimate: GloBE income / covered taxes / SBIE / UK top-up on Kilnworth share | 44.9 / 0.06 / 50.3 / 0.00 | USD m | Actual history (15) | 2026-12-31 |
| P-F55 | Underwritten at mandate (ECA-covered + commercial) / final holds commercial / ECA-covered | 428.4 / 81.4 / 75.6 | USD m | FC base (1) | 2018-07-17 |
| P-F55 | Castellan construction_2020H1: RWA / capital / net income (annual) / RAROC | 71.5 / 9.65 / 1.89 / 19.6% | USD m, % | FC base (1) | 2020H1 |
| P-F55 | Castellan operations_2022H1: RWA / capital / net income (annual) / RAROC | 75.1 / 10.14 / 2.71 / 26.7% | USD m, % | FC base (1) | 2022H1 |
| P-F56 | IFRIC 12 financial asset at COD / effective interest rate | 839.5 / 12.81% a year | USD m, % | Actual history (15) | 2021-12-01 |
| P-F56 | 2021: financial asset / PP&E (lenders) / finance income / capital charge collected / PBT difference / cumulative equity difference | 831.0 / 836.7 / 0.0 / 8.5 / -5.7 / -5.7 | USD m | Actual history (15) | 2021-12-31 |
| P-F56 | 2022: financial asset / PP&E (lenders) / finance income / capital charge collected / PBT difference / cumulative equity difference | 831.3 / 803.1 / 103.3 / 102.9 / 33.9 / 28.2 | USD m | Actual history (15) | 2022-12-31 |
| P-F56 | 2023: financial asset / PP&E (lenders) / finance income / capital charge collected / PBT difference / cumulative equity difference | 830.0 / 769.5 / 103.3 / 104.6 / 32.3 / 60.5 | USD m | Actual history (15) | 2023-12-31 |
| P-F56 | 2024: financial asset / PP&E (lenders) / finance income / capital charge collected / PBT difference / cumulative equity difference | 827.5 / 735.9 / 103.1 / 105.6 / 31.0 / 91.6 | USD m | Actual history (15) | 2024-12-31 |
| P-F56 | 2025: financial asset / PP&E (lenders) / finance income / capital charge collected / PBT difference / cumulative equity difference | 823.8 / 702.4 / 102.7 / 106.4 / 29.9 / 121.5 | USD m | Actual history (15) | 2025-12-31 |
| P-F56 | 2026: financial asset / PP&E (lenders) / finance income / capital charge collected / PBT difference / cumulative equity difference | 819.0 / 668.8 / 102.3 / 107.1 / 28.7 / 150.2 | USD m | Actual history (15) | 2026-12-31 |
| P-F57 | OCGT: annualized fixed cost / fuel cost / cost at 30%, 50%, 70%, 90% CF | 85.6 USD/kW-yr / 59.5 / 96.1, 83.0, 77.5, 74.4 | USD/MWh (2015) | Annex 4.12 inputs | 2015 |
| P-F57 | CCGT: annualized fixed cost / fuel cost / cost at 30%, 50%, 70%, 90% CF | 137.7 USD/kW-yr / 36.7 / 92.6, 71.6, 62.6, 57.6 | USD/MWh (2015) | Annex 4.12 inputs | 2015 |
| P-F57 | Coal: annualized fixed cost / fuel cost / cost at 30%, 50%, 70%, 90% CF | 267.8 USD/kW-yr / 29.0 / 135.4, 94.6, 77.2, 67.4 | USD/MWh (2015) | Annex 4.12 inputs | 2015 |
| P-F57 | HFO: annualized fixed cost / fuel cost / cost at 30%, 50%, 70%, 90% CF | 151.2 USD/kW-yr / 62.6 / 129.1, 106.1, 96.2, 90.8 | USD/MWh (2015) | Annex 4.12 inputs | 2015 |
| P-F58 | 2022H1: dispatch / gas burn actual / at 76.5% / fuel charge actual / at 76.5% | 84.0% / 13.53 / 12.32 million MMBtu / 85.7 / 78.0 | %, MMBtu, USD m | Actual history (15) vs COD re-forecast (14) | 2022H1 |
| P-F58 | 2022H2: dispatch / gas burn actual / at 76.5% / fuel charge actual / at 76.5% | 81.5% / 13.11 / 12.30 million MMBtu / 82.9 / 77.9 | %, MMBtu, USD m | Actual history (15) vs COD re-forecast (14) | 2022H2 |
| P-F59 | Halbeck RBL at_signing_2017: NPV10 of operating cash flows to the reserve tail (65% share) / borrowing base (NPV / 1.30, max 600) | 364.9 / 280.7 | USD m | Illustrative (annex 4.13) | 2017 |
| P-F59 | Halbeck RBL at_2023_redetermination: NPV10 of operating cash flows to the reserve tail (65% share) / borrowing base (NPV / 1.30, max 600) | 471.4 / 362.7 | USD m | Illustrative (annex 4.13) | tion |
| P-F59 | Gas price to SNHK that would give a USD 420m base at signing | 4.62 | USD/MMBtu (2018) | Illustrative | 2017-10 |
| P-F60 | Bid screen: cost / capacity + FOM revenue / fixed costs / CFADS proxy | 655.0 / 117.7 / 18.1 / 99.6 | USD m | Annex 4.7 inputs | 2016-09 |
| P-F60 | Bid screen: debt capacity at 1.35x over 13 years / debt at 75% gearing / capacity payments share of SEKA revenue | 689.4 / 491.2 / 6.5% | USD m, % | Annex 4.7 inputs | 2016-09 |
| P-F61 | 2P reserves / Belanou GSA / SEKA contract / coverage | 1140 / 559 / 267 bcf / 1.38x | bcf, x | Annex 1.7.4 inputs | 2017 |
| P-F62 | Levelized tariffs: winner / runner-up / third / fourth | 73.00 / 76.36 / 80.16 / 82.57 | USD/MWh (2016) | Bid inputs | 2016-09-27 |
| P-F62 | Pricing committee tariff at USD 15.05/kW-month (bid-model IRR 17.6%) vs submitted (16.0%) | 74.35 vs 73.00 | USD/MWh | Bid inputs | 2016-09-19 |
| P-F63 | June 30, 2023: 12-month CFADS / debt service / historic DSCR | 73.1 / 76.6 / 0.95x | USD m, x | Actual history (15) | 2023-06-30 |
| P-F63 | Equity cure needed for 1.10x / 1.20x | 11.2 / 18.8 | USD m | Actual history (15) | 2023-06-30 |
| P-F63 | Pro rata prepayment cure (eq:51.3, deemed at July 1, 2022) for 1.10x / 1.20x | 81.3 / 125.6 | USD m | Actual history (15) | 2023-06-30 |
| P-F63 | Proportional prepayment cure (eq:37.4, x D/DS) for 1.10x / 1.20x | 80.2 / 123.9 | USD m | Actual history (15) | 2023-06-30 |
| P-F63 | Prepayment-cure inputs: scheduled principal 12m / senior debt at July 1, 2022 / all-in rate a year | 34.1 / 605.3 / 6.86% | USD m, % | Actual history (15) | 2022-07-01 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2023-07 (half-year fall spread evenly) | 5.44 | USD m | Actual history (15) | 2023-07 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2023-08 (half-year fall spread evenly) | 5.44 | USD m | Actual history (15) | 2023-08 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2023-09 (half-year fall spread evenly) | 5.44 | USD m | Actual history (15) | 2023-09 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2023-10 (half-year fall spread evenly) | 5.44 | USD m | Actual history (15) | 2023-10 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2023-11 (half-year fall spread evenly) | 5.44 | USD m | Actual history (15) | 2023-11 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2023-12 (half-year fall spread evenly) | 5.44 | USD m | Actual history (15) | 2023-12 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2024-01 (half-year fall spread evenly) | 4.96 | USD m | Actual history (15) | 2024-01 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2024-02 (half-year fall spread evenly) | 4.96 | USD m | Actual history (15) | 2024-02 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2024-03 (half-year fall spread evenly) | 4.96 | USD m | Actual history (15) | 2024-03 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2024-04 (half-year fall spread evenly) | 4.96 | USD m | Actual history (15) | 2024-04 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2024-05 (half-year fall spread evenly) | 4.96 | USD m | Actual history (15) | 2024-05 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2024-06 (half-year fall spread evenly) | 4.96 | USD m | Actual history (15) | 2024-06 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2024-07 (half-year fall spread evenly) | 2.97 | USD m | Actual history (15) | 2024-07 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2024-08 (half-year fall spread evenly) | 2.97 | USD m | Actual history (15) | 2024-08 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2024-09 (half-year fall spread evenly) | 2.97 | USD m | Actual history (15) | 2024-09 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2024-10 (half-year fall spread evenly) | 2.97 | USD m | Actual history (15) | 2024-10 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2024-11 (half-year fall spread evenly) | 2.97 | USD m | Actual history (15) | 2024-11 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2024-12 (half-year fall spread evenly) | 2.97 | USD m | Actual history (15) | 2024-12 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2025-01 (half-year fall spread evenly) | 1.64 | USD m | Actual history (15) | 2025-01 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2025-02 (half-year fall spread evenly) | 1.64 | USD m | Actual history (15) | 2025-02 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2025-03 (half-year fall spread evenly) | 1.64 | USD m | Actual history (15) | 2025-03 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2025-04 (half-year fall spread evenly) | 1.64 | USD m | Actual history (15) | 2025-04 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2025-05 (half-year fall spread evenly) | 1.64 | USD m | Actual history (15) | 2025-05 |
| P-F40 | Netting set-off under the June 29, 2023 agreement, 2025-06 (half-year fall spread evenly) | 1.64 | USD m | Actual history (15) | 2025-06 |
| P-F40 | Netting set-offs, total July 2023 to June 2025 (all within the USD 9.0m monthly cap) | 90.08 | USD m | Actual history (15) | 2025-06-30 |
| P-F16 | Debt capacity at 1.35x (Debt F130), FC base | 629.95 | USD m | Debt locked | 2018-07-17 |
| P-F16 | Debt capacity at 1.35x (Debt F130), FC banking | 629.22 | USD m | Debt locked | 2018-07-17 |
| P-F16 | Debt capacity at 1.35x (Debt F130), FC downside | 578.16 | USD m | Debt locked | 2018-07-17 |
| P-F16 | Debt capacity at 1.35x (Debt F130), Sens: availability -3 points | 629.27 | USD m | Debt locked | 2018-07-17 |
| P-F16 | Debt capacity at 1.35x (Debt F130), Sens: heat rate +2% | 613.29 | USD m | Debt locked | 2018-07-17 |
| P-F16 | Debt capacity at 1.35x (Debt F130), Sens: fixed opex +10% | 619.43 | USD m | Debt locked | 2018-07-17 |
| P-F16 | Debt capacity at 1.35x (Debt F130), Sens: capex +10% funded pro rata | 633.88 | USD m | Debt locked | 2018-07-17 |
| P-F16 | Debt capacity at 1.35x (Debt F130), Sens: COD delay 6 months, no LDs | 620.16 | USD m | Debt locked | 2018-07-17 |
| P-F16 | Debt capacity at 1.35x (Debt F130), Sens: base rate +200 bps (unhedged) | 616.39 | USD m | Debt locked | 2018-07-17 |
| P-F16 | Debt capacity at 1.35x (Debt F130), Sens: KCR devaluation 40%, 90-day lag | 620.69 | USD m | Debt locked | 2018-07-17 |
| P-F16 | Debt capacity at 1.35x (Debt F130), Sens: SEKA pays 120 days late for 12 months | 627.75 | USD m | Debt locked | 2018-07-17 |
| P-F16 | Debt capacity at 1.35x (Debt F130), Sens: dispatch 50% | 625.65 | USD m | Debt locked | 2018-07-17 |
| P-F16 | Debt capacity at 1.35x (Debt F130), Sens: gas price +30% | 630.14 | USD m | Debt locked | 2018-07-17 |
| P-F17 | Annual shadow sizing 2021: CFADS / all-in rate / discount factor (1 half-years) | 50.28 / 3.533% / 0.96588 | USD m, %, factor | FC base (1) | 2021 |
| P-F17 | Annual shadow sizing 2022: CFADS / all-in rate / discount factor (2 half-years) | 100.96 / 7.202% / 0.90099 | USD m, %, factor | FC base (1) | 2022 |
| P-F17 | Annual shadow sizing 2023: CFADS / all-in rate / discount factor (2 half-years) | 101.36 / 7.219% / 0.84032 | USD m, %, factor | FC base (1) | 2023 |
| P-F17 | Annual shadow sizing 2024: CFADS / all-in rate / discount factor (2 half-years) | 102.41 / 7.226% / 0.78369 | USD m, %, factor | FC base (1) | 2024 |
| P-F17 | Annual shadow sizing 2025: CFADS / all-in rate / discount factor (2 half-years) | 101.18 / 7.216% / 0.73095 | USD m, %, factor | FC base (1) | 2025 |
| P-F17 | Annual shadow sizing 2026: CFADS / all-in rate / discount factor (2 half-years) | 99.15 / 7.433% / 0.68038 | USD m, %, factor | FC base (1) | 2026 |
| P-F17 | Annual shadow sizing 2027: CFADS / all-in rate / discount factor (2 half-years) | 99.33 / 7.431% / 0.63332 | USD m, %, factor | FC base (1) | 2027 |
| P-F17 | Annual shadow sizing 2028: CFADS / all-in rate / discount factor (2 half-years) | 101.41 / 7.437% / 0.58948 | USD m, %, factor | FC base (1) | 2028 |
| P-F17 | Annual shadow sizing 2029: CFADS / all-in rate / discount factor (2 half-years) | 103.65 / 7.427% / 0.54873 | USD m, %, factor | FC base (1) | 2029 |
| P-F17 | Annual shadow sizing 2030: CFADS / all-in rate / discount factor (2 half-years) | 103.75 / 7.645% / 0.50976 | USD m, %, factor | FC base (1) | 2030 |
| P-F17 | Annual shadow sizing 2031: CFADS / all-in rate / discount factor (2 half-years) | 104.20 / 7.644% / 0.47356 | USD m, %, factor | FC base (1) | 2031 |
| P-F17 | Annual shadow sizing 2032: CFADS / all-in rate / discount factor (2 half-years) | 105.44 / 7.651% / 0.43990 | USD m, %, factor | FC base (1) | 2032 |
| P-F17 | Annual shadow sizing 2033: CFADS / all-in rate / discount factor (2 half-years) | 97.01 / 7.646% / 0.40866 | USD m, %, factor | FC base (1) | 2033 |
| P-F17 | Annual shadow sizing 2034: CFADS / all-in rate / discount factor (1 half-years) | 41.63 / 3.742% / 0.39392 | USD m, %, factor | FC base (1) | 2034 |
| P-F17 | Annual shadow sizing: PV of CFADS / shadow debt at 1.35x / model debt / difference | 830.6 / 615.3 / 629.9 / -14.7 | USD m | FC base (1) | 2018-07-17 |
| P-F64 | Bid-to-close IRR bridge (sequential, in this order): Kilnworth bid model, September 2016 (reconstructed; tariff USD 14.36/kW-month) | 16.00% (+0.00 pp) | % (cumulative) | FC base (1) re-sized at each step | 2016-09 to 2018-07 |
| P-F64 | Bid-to-close IRR bridge (sequential, in this order): Base rate: reconstructed bid-model swapped rate (flat) replaced by the FC forward curve and the 2.947% swap | 16.50% (+0.50 pp) | % (cumulative) | FC base (1) re-sized at each step | 2016-09 to 2018-07 |
| P-F64 | Bid-to-close IRR bridge (sequential, in this order): Debt terms: 2016 indicative margins, upfront fees and ECA premium (annex 4.7) replaced by the FC terms | 16.95% (+0.45 pp) | % (cumulative) | FC base (1) re-sized at each step | 2016-09 to 2018-07 |
| P-F64 | Bid-to-close IRR bridge (sequential, in this order): PRI cover on the commercial tranche and the 10% WHT gross-up, added in diligence | 16.06% (-0.89 pp) | % (cumulative) | FC base (1) re-sized at each step | 2016-09 to 2018-07 |
| P-F64 | Bid-to-close IRR bridge (sequential, in this order): Soft mini-perm cash sweep from 2027 (FC term sheet) | 15.93% (-0.13 pp) | % (cumulative) | FC base (1) re-sized at each step | 2016-09 to 2018-07 |
| P-F64 | Bid-to-close IRR bridge (sequential, in this order): Capex: bid-stage USD 655.0m before financing grows to the FC budget of USD 710.99m (owner's cost, resettlement, contingency) | 14.13% (-1.80 pp) | % (cumulative) | FC base (1) re-sized at each step | 2016-09 to 2018-07 |
| P-F64 | Bid-to-close IRR bridge (sequential, in this order): VAT facility interest (omitted from the bid model, annex Kunal Mehrotra) | 14.06% (-0.06 pp) | % (cumulative) | FC base (1) re-sized at each step | 2016-09 to 2018-07 |
| P-F64 | Bid-to-close IRR bridge (sequential, in this order): Tax: minimum turnover tax and thin-cap disallowance | 13.98% (-0.08 pp) | % (cumulative) | FC base (1) re-sized at each step | 2016-09 to 2018-07 |
| P-F64 | Bid-to-close IRR bridge (sequential, in this order): FX: KCR depreciation on the local tariff shares and costs (bid model held the KCR flat) | 13.20% (-0.79 pp) | % (cumulative) | FC base (1) re-sized at each step | 2016-09 to 2018-07 |
| P-F64 | Bid-to-close IRR bridge (sequential, in this order): IRR dating: measured from the February 2018 LNTP payment rather than from financial close | 13.15% (-0.04 pp) | % (cumulative) | FC base (1) re-sized at each step | 2016-09 to 2018-07 |
| P-F64 | Bridge total: bid model to FC base / sum of steps (no residual) | -2.85 pp / -2.85 pp | pp | FC base (1) | 2016-09 to 2018-07 |
| P-F64 | Reconstructed bid-model swapped base rate (modeler reconstruction, solved to the 16.0% bid IRR) | 3.38% | % flat | Modeler reconstruction | 2016-09 |
| P-F65 | FX forwards (Castellan, traded 2018-07-17): share hedged / KCR notional / USD at forward / USD at FC spot / average forward | 75% / 32,204 / 52.6 / 62.0 / 612.6 | %, KCR m, USD m, KCR/USD | Contract (FC) | 2018-07-17 |
| P-F65 | Forward settling 2018-08 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 3,220.41 / 525.96 / 6.123 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2018-08 |
| P-F65 | Forward settling 2018-09 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 3.28 / 530.37 / 0.006 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2018-09 |
| P-F65 | Forward settling 2018-10 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 27.95 / 534.98 / 0.052 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2018-10 |
| P-F65 | Forward settling 2018-11 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 73.55 / 539.47 / 0.136 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2018-11 |
| P-F65 | Forward settling 2018-12 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 136.38 / 544.15 / 0.251 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2018-12 |
| P-F65 | Forward settling 2019-01 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 212.93 / 548.09 / 0.389 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2019-01 |
| P-F65 | Forward settling 2019-02 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 299.92 / 552.27 / 0.543 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2019-02 |
| P-F65 | Forward settling 2019-03 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 394.24 / 556.94 / 0.708 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2019-03 |
| P-F65 | Forward settling 2019-04 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 493.08 / 561.50 / 0.878 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2019-04 |
| P-F65 | Forward settling 2019-05 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 593.75 / 566.24 / 1.049 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2019-05 |
| P-F65 | Forward settling 2019-06 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 693.84 / 570.88 / 1.215 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2019-06 |
| P-F65 | Forward settling 2019-07 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 791.09 / 574.83 / 1.376 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2019-07 |
| P-F65 | Forward settling 2019-08 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 883.55 / 579.62 / 1.524 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2019-08 |
| P-F65 | Forward settling 2019-09 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 969.34 / 584.29 / 1.659 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2019-09 |
| P-F65 | Forward settling 2019-10 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 1,046.92 / 589.16 / 1.777 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2019-10 |
| P-F65 | Forward settling 2019-11 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 1,114.87 / 593.90 / 1.877 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2019-11 |
| P-F65 | Forward settling 2019-12 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 1,172.10 / 598.85 / 1.957 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2019-12 |
| P-F65 | Forward settling 2020-01 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 1,217.57 / 603.12 / 2.019 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2020-01 |
| P-F65 | Forward settling 2020-02 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 1,250.58 / 607.78 / 2.058 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2020-02 |
| P-F65 | Forward settling 2020-03 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 1,270.61 / 612.80 / 2.073 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2020-03 |
| P-F65 | Forward settling 2020-04 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 1,277.21 / 617.70 / 2.068 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2020-04 |
| P-F65 | Forward settling 2020-05 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 1,270.61 / 622.80 / 2.040 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2020-05 |
| P-F65 | Forward settling 2020-06 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 1,250.58 / 627.78 / 1.992 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2020-06 |
| P-F65 | Forward settling 2020-07 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 1,217.57 / 632.46 / 1.925 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2020-07 |
| P-F65 | Forward settling 2020-08 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 1,172.10 / 637.67 / 1.838 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2020-08 |
| P-F65 | Forward settling 2020-09 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 1,114.87 / 642.75 / 1.735 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2020-09 |
| P-F65 | Forward settling 2020-10 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 1,046.92 / 648.03 / 1.616 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2020-10 |
| P-F65 | Forward settling 2020-11 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 969.34 / 653.19 / 1.484 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2020-11 |
| P-F65 | Forward settling 2020-12 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 883.55 / 658.57 / 1.342 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2020-12 |
| P-F65 | Forward settling 2021-01 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 791.09 / 663.50 / 1.192 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2021-01 |
| P-F65 | Forward settling 2021-02 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 693.84 / 668.41 / 1.038 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2021-02 |
| P-F65 | Forward settling 2021-03 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 593.75 / 673.90 / 0.881 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2021-03 |
| P-F65 | Forward settling 2021-04 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 493.08 / 679.24 / 0.726 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2021-04 |
| P-F65 | Forward settling 2021-05 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 394.24 / 684.82 / 0.576 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2021-05 |
| P-F65 | Forward settling 2021-06 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 299.92 / 690.25 / 0.435 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2021-06 |
| P-F65 | Forward settling 2021-07 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 212.93 / 695.92 / 0.306 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2021-07 |
| P-F65 | Forward settling 2021-08 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 136.38 / 701.63 / 0.194 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2021-08 |
| P-F65 | Forward settling 2021-09 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 73.55 / 707.19 / 0.104 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2021-09 |
| P-F65 | Forward settling 2021-10 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 27.95 / 713.00 / 0.039 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2021-10 |
| P-F65 | Forward settling 2021-11 (one per monthly onshore EPC payment): KCR notional / forward rate / USD at forward | 2,418.59 / 718.66 / 3.365 | KCR m, KCR/USD, USD m | Rates fixed at FC; settlement months on the actual payment schedule | 2021-11 |
| P-F65 | Sum of the monthly forwards: KCR notional / USD at forward (equals the totals above) | 32,204.1 / 52.57 | KCR m, USD m | Rates fixed at FC | 2018-07-17 |
| P-F65 | Schedule basis | one forward per monthly onshore EPC payment; forward rates fixed at financial close by covered interest parity; settlement months follow the actual payment certificates (August 2018 to November 2021, 40 months), because the forwards were re-dated without cost as certificates slipped (modeler simplification; under the FC schedule the last payment would have been April 2021) | text | Rates fixed at FC | 2018-07-17 |
| P-F66 | FX forward settlement 2018H2 (gain to project) | 0.03 | USD m | Actual history (15) | 2018H2 |
| P-F66 | FX forward settlement 2019H1 (gain to project) | 0.20 | USD m | Actual history (15) | 2019H1 |
| P-F66 | FX forward settlement 2019H2 (gain to project) | 0.67 | USD m | Actual history (15) | 2019H2 |
| P-F66 | FX forward settlement 2020H1 (gain to project) | 1.07 | USD m | Actual history (15) | 2020H1 |
| P-F66 | FX forward settlement 2020H2 (gain to project) | 1.11 | USD m | Actual history (15) | 2020H2 |
| P-F66 | FX forward settlement 2021H1 (gain to project) | 0.62 | USD m | Actual history (15) | 2021H1 |
| P-F66 | FX forward settlement 2021H2 (gain to project) | 0.70 | USD m | Actual history (15) | 2021H2 |
| P-F66 | FX forward settlements, total | 4.40 | USD m | Actual history (15) | 2021-11-30 |
| P-F66 | FX forward MTM to project at 2018-12-31 | 1.23 | USD m | Actual history (15) | 2018-12-31 |
| P-F66 | FX forward MTM to project at 2019-06-30 | 2.19 | USD m | Actual history (15) | 2019-06-30 |
| P-F66 | FX forward MTM to project at 2019-12-31 | 2.36 | USD m | Actual history (15) | 2019-12-31 |
| P-F66 | FX forward MTM to project at 2020-06-30 | 1.86 | USD m | Actual history (15) | 2020-06-30 |
| P-F66 | FX forward MTM to project at 2020-12-31 | 1.05 | USD m | Actual history (15) | 2020-12-31 |
| P-F66 | FX forward MTM to project at 2021-06-30 | 0.57 | USD m | Actual history (15) | 2021-06-30 |
| P-F66 | FX forward MTM to project at 2021-11-30 | 0.00 | USD m | Actual history (15) | 2021-11-30 |
| P-F66 | Unhedged KCR depreciation saving on the onshore EPC (for comparison) | 6.72 | USD m | Actual history (15) | 2021-11-30 |
| P-F40 | SEKA LC drawing, February 14, 2023 (2023 reset value; P-C44) | 36.6 | USD m | Actual history (15) | 2023-02-14 |

FC base equity IRR is below the 16.0% bid-model target; P-F64 bridges the gap sequentially with no residual (steps printed to 0.01 pp may sum to the total within 0.01 by rounding). See `model/case_p_report.md` Section 8b.
