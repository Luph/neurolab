# Figure ledger: Case P (Bélanou Combined Cycle Power Project)

Source: `model/outputs_case_p.json`, produced by `model/case_p.py` (Case P model v1.0; story as of October 3, 2026); formatted by `model/ledger_p.py` (no computation). Amounts in USD million, nominal, unless stated. Scenario numbers are the workbook scenario switch (1 FC base, 2 FC banking, 3 FC downside, 4-13 sensitivities, 14 COD re-forecast, 15 actual history). P-F01 to P-F36 are the Case Bible register; P-F37 to P-F45 are new (editor-in-chief assignments). Writers cite the ID; print values in the style-sheet format.

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
| P-F02 | US CPI index reading for the January 2022 reset (September 2021; Nov 2016 = 100) | 111.60 | index | Actual history (15) | 2022-01-01 |
| P-F02 | Kessara CPI index reading (September 2021; Nov 2016 = 100) | 149.74 | index | Actual history (15) | 2022-01-01 |
| P-F02 | FX used to reconvert local shares (2022H1 average) | 654.9 | KCR/USD | Actual history (15) | 2022-01-01 |
| P-F02 | Contracted capacity applying in January 2022 (reset at completion tests) | 581.9 | MW | Actual history (15) | 2022-01-01 |
| P-F02 | Capital charge, indexed (base 14.36) | 14.69 | USD/kW-month | Actual history (15) | 2022-01-01 |
| P-F02 | Fixed O&M charge, indexed (base 2.31) | 2.53 | USD/kW-month | Actual history (15) | 2022-01-01 |
| P-F02 | Total capacity charge, nominal | 17.22 | USD/kW-month | Actual history (15) | 2022-01-01 |
| P-F02 | Total capacity charge in November 2016 dollars (real) | 15.43 | USD/kW-month | Actual history (15) | 2022-01-01 |
| P-F02 | VOM charge, indexed (base 3.86) | 4.24 | USD/MWh | Actual history (15) | 2022-01-01 |
| P-F02 | VOM charge in November 2016 dollars (real) | 3.80 | USD/MWh | Actual history (15) | 2022-01-01 |
| P-F03 | 6M USD LIBOR assumed for July 2016 (approximate; fact-check) | 0.95% | % | Inputs (modeler) | 2016-07 |
| P-F03 | Average life of the senior loans from financial close (fee annualization) | 8.74 | years | FC base (1) | 2016-07 |
| P-F03 | Indicative all-in floating cost, ECA tranche (incl. fees, ECA premium, PRI and gross-up) | 3.67% | % pa | Inputs plus calculation | 2016-07 |
| P-F03 | Indicative all-in floating cost, A tranche (incl. fees, ECA premium, PRI and gross-up) | 4.74% | % pa | Inputs plus calculation | 2016-07 |
| P-F03 | Indicative all-in floating cost, B tranche (incl. fees, ECA premium, PRI and gross-up) | 4.52% | % pa | Inputs plus calculation | 2016-07 |
| P-F03 | Indicative all-in floating cost, COM tranche (incl. fees, ECA premium, PRI and gross-up) | 6.89% | % pa | Inputs plus calculation | 2016-07 |
| P-F03 | Indicative all-in floating cost, commercial tranche excl. PRI and WHT gross-up | 5.30% | % pa | Inputs plus calculation | 2016-07 |
| P-F03 | Indicative weighted all-in floating cost | 5.22% | % pa | Inputs plus calculation | 2016-07 |
| P-F04 | FY2022 income statement: revenue | 319.5 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: late payment interest | 0.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: operating costs | 222.6 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: of which fuel and transport | 184.4 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: ebitda | 96.9 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: depreciation | 32.1 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: finance costs | 58.7 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: of which shareholder loan interest | 19.3 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: current tax | 0.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: deferred tax | -9.6 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 income statement: net income | 15.8 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: ebitda | 96.9 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: tax paid | 0.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: increase in working capital | 13.8 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: mmra net | 0.9 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: cfads | 82.1 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: senior interest and fees | 39.4 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: senior principal | 32.5 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: ld prepayment | 18.5 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: sweeps | 0.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: dsra topup less release | 2.2 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: shl interest paid | 9.8 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: shl principal repaid | 7.9 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | FY2022 cash flow: dividends | 0.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: plant | 766.7 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: cash in project accounts | 38.2 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: of which dsra | 37.3 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: receivables | 108.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: of which overdue | 68.9 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: inventory | 5.3 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: deferred tax asset | 10.4 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: total assets | 928.6 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: senior debt | 575.9 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: shareholder loans | 208.7 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: payables | 79.6 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: deferred tax liability | 0.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: share capital | 43.9 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: retained earnings | 20.5 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: total liabilities and equity | 928.6 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Balance sheet at 2022-12-31: balance check | -0.0 | USD m | Actual history (15) | 2022-12-31 |
| P-F04 | Financing costs capitalized during construction (IDC, fees, ECA premium, VAT interest) | 107.5 | USD m | Actual history (15) | 2021-12-01 |
| P-F04 | Shareholder-loan interest capitalized to COD | 29.8 | USD m | Actual history (15) | 2021-12-01 |
| P-F05 | Equity IRR at 60% gearing | 12.3% | % nominal post-tax | FC base (1), debt set at gearing | 2017 |
| P-F05 | Senior debt at 60% gearing | 495.0 | USD m | FC base (1) | 2017 |
| P-F05 | Minimum DSCR at 60% gearing | 1.72x | x | FC base (1) | 2017 |
| P-F05 | Equity IRR at 65% gearing | 12.6% | % nominal post-tax | FC base (1), debt set at gearing | 2017 |
| P-F05 | Senior debt at 65% gearing | 543.1 | USD m | FC base (1) | 2017 |
| P-F05 | Minimum DSCR at 65% gearing | 1.57x | x | FC base (1) | 2017 |
| P-F05 | Equity IRR at 70% gearing | 12.9% | % nominal post-tax | FC base (1), debt set at gearing | 2017 |
| P-F05 | Senior debt at 70% gearing | 592.3 | USD m | FC base (1) | 2017 |
| P-F05 | Minimum DSCR at 70% gearing | 1.44x | x | FC base (1) | 2017 |
| P-F05 | Equity IRR at 75% gearing | 13.4% | % nominal post-tax | FC base (1), debt set at gearing | 2017 |
| P-F05 | Senior debt at 75% gearing | 642.9 | USD m | FC base (1) | 2017 |
| P-F05 | Minimum DSCR at 75% gearing | 1.33x | x | FC base (1) | 2017 |
| P-F05 | Equity IRR at 80% gearing | 13.9% | % nominal post-tax | FC base (1), debt set at gearing | 2017 |
| P-F05 | Senior debt at 80% gearing | 694.7 | USD m | FC base (1) | 2017 |
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
| P-F07 | Use: idc loans | 60.99 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: swap net during construction | -0.78 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: pri premium | 3.69 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: commitment fees | 10.12 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: upfront fees | 9.95 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: eca premium | 20.61 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: agency fees | 0.74 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: vat facility interest | 1.52 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: dsra initial | 37.25 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Use: total | 855.09 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: debt ECA | 189.98 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: debt A | 139.32 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: debt B | 63.33 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: debt COM | 240.64 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: debt total | 633.26 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: share capital | 44.37 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: shareholder loans | 177.47 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: equity total | 221.83 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: of which lntp credit | 14.20 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Source: total | 855.09 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Gearing (senior debt / total funding requirement) | 74.1% | % | FC base (1) | 2018-07-17 |
| P-F07 | Shareholder-loan interest capitalized to COD (non-cash) | 24.2 | USD m | FC base (1) | 2018-07-17 |
| P-F07 | Shareholder-loan balance at COD | 201.7 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Senior debt, ECA tranche | 190.0 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Senior debt, A tranche | 139.3 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Senior debt, B tranche | 63.3 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Senior debt, COM tranche | 240.6 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Senior debt, total | 633.3 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Binding constraint | DSCR (1.35x) | text | FC base (1) | 2018-07-17 |
| P-F08 | Debt at the 75% gearing cap | 642.9 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Debt capacity at 1.35x | 633.3 | USD m | FC base (1) | 2018-07-17 |
| P-F08 | Debt meeting the 1.20x downside | 633.4 | USD m | FC downside (3) | 2018-07-17 |
| P-F08 | Minimum DSCR, base | 1.35x | x | FC base (1) | 2018-07-17 |
| P-F08 | Average DSCR (debt-service weighted), base | 1.54x | x | FC base (1) | 2018-07-17 |
| P-F08 | Minimum DSCR, banking | 1.34x | x | FC banking (2) | 2018-07-17 |
| P-F08 | Average DSCR (debt-service weighted), banking | 1.53x | x | FC banking (2) | 2018-07-17 |
| P-F08 | Minimum DSCR, downside | 1.20x | x | FC downside (3) | 2018-07-17 |
| P-F08 | Average DSCR (debt-service weighted), downside | 1.38x | x | FC downside (3) | 2018-07-17 |
| P-F08 | LLCR at close (PV CFADS + DSRA over debt; first repayment period) | 1.42x | x | FC base (1) | 2018-07-17 |
| P-F08 | LLCR at close excluding DSRA | 1.36x | x | FC base (1) | 2018-07-17 |
| P-F08 | Does the 1.40x LLCR test bind? | No | text | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2021H2 | 15.5 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2022H1 | 16.1 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2022H2 | 16.9 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2023H1 | 17.4 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2023H2 | 18.2 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2024H1 | 18.8 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2024H2 | 20.1 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2025H1 | 20.7 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2025H2 | 20.1 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2026H1 | 20.1 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2026H2 | 20.9 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2027H1 | 21.5 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2027H2 | 22.2 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2028H1 | 22.5 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2028H2 | 24.1 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2029H1 | 24.5 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2029H2 | 24.6 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2030H1 | 24.1 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2030H2 | 24.1 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2031H1 | 23.2 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2031H2 | 22.3 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2032H1 | 20.3 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2032H2 | 21.5 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2033H1 | 22.0 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2033H2 | 18.1 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Scheduled principal 2034H1 | 18.4 | USD m | FC base (1) | 2018-07-17 |
| P-F09 | Weighted average life of repayment from COD | 7.18 | years (limit 7.25) | FC base (1) | 2018-07-17 |
| P-F09 | Largest installment | 4.6% | % of principal (limit 25%) | FC base (1) | 2018-07-17 |
| P-F09 | Repayment term from COD | 13.16 | years (limit 14) | FC base (1) | 2018-07-17 |
| P-F09 | First repayment after COD | 8 | months (limit 24) | FC base (1) | 2018-07-17 |
| P-F10 | FY2022 capacity payments | 121.6 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 vom | 15.4 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 fuel and transport pass through | 184.8 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 total revenue | 321.8 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 fuel and transport costs | 184.6 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 om fixed | 8.6 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 om incentive | 0.3 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 ltsa fixed | 2.9 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 ltsa variable | 8.9 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 insurance | 4.8 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 g and a | 3.5 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 land | 0.8 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 community and levy | 0.8 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 consumables | 4.3 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 agency | 0.3 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 prg fee | 0.3 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 vat interest | 0.0 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 major maintenance | 0.0 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 ebitda | 101.9 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 tax | 0.0 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 increase in working capital | 0.1 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 mmra contribution | 0.8 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 mmra release | 0.0 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 cfads | 101.0 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 debt service | 74.8 | USD m | FC base (1) | FY2022 (first full calendar year) |
| P-F10 | FY2022 dscr | 1.35x | x | FC base (1) | FY2022 (first full calendar year) |
| P-F11 | DSRA initial balance (funded at COD) | 37.2 | USD m | FC base (1) | 2021-05-01 |
| P-F11 | MMRA contribution 2021H2 | 0.42 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | MMRA contribution 2022H1 | 0.42 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | MMRA contribution 2022H2 | 0.42 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | MMRA contribution 2023H1 | 0.42 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | MMRA contribution 2023H2 | 0.42 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | MMRA contribution 2024H1 | 0.42 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | MMRA contribution 2025H2 | 1.97 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | MMRA contribution 2026H1 | 1.97 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | MMRA contribution 2026H2 | 1.97 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | MMRA contribution 2027H1 | 1.97 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | MMRA contribution 2027H2 | 1.97 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | MMRA contribution 2028H1 | 1.97 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | MMRA contribution 2029H2 | 0.50 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | MMRA contribution 2030H1 | 0.50 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | MMRA contribution 2030H2 | 0.50 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | Out-of-LTSA major maintenance spend 2024H2 | 2.50 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | Out-of-LTSA major maintenance spend 2028H2 | 11.84 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | Out-of-LTSA major maintenance spend 2032H2 | 2.97 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | Out-of-LTSA major maintenance spend 2036H2 | 14.09 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | Out-of-LTSA major maintenance spend 2040H2 | 3.54 | USD m | FC base (1) | 2018-07-17 |
| P-F11 | Out-of-LTSA major maintenance spend 2044H2 | 16.77 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Swap fixed rate | 2.947% | % | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional peak during construction | 504.4 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional 2021H2 | 506.6 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional 2023H2 | 453.8 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional 2025H2 | 391.6 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional 2027H2 | 325.4 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional 2029H2 | 247.1 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional 2031H2 | 154.9 | USD m | FC base (1) | 2018-07-17 |
| P-F12 | Swap notional 2033H2 | 47.2 | USD m | FC base (1) | 2018-07-17 |
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
| P-F12 | Model all-in senior cost in 2022 (financing costs / opening debt) | 6.75% | % pa | FC base (1) | 2022 |
| P-F13 | Construction total: uses | 855.1 | USD m | FC base (1) | 2021-06-30 |
| P-F13 | Construction total: debt | 633.3 | USD m | FC base (1) | 2021-06-30 |
| P-F13 | Construction total: equity | 221.8 | USD m | FC base (1) | 2021-06-30 |
| P-F13 | Construction total: idc incl swap pri | 63.9 | USD m | FC base (1) | 2021-06-30 |
| P-F13 | Month 2018-08: uses / debt / equity / IDC | 121.6 / 90.0 / 31.5 / 0.00 | USD m | FC base (1) | 2018-08 |
| P-F13 | Month 2019-01: uses / debt / equity / IDC | 8.9 / 6.6 / 2.3 / 0.58 | USD m | FC base (1) | 2019-01 |
| P-F13 | Month 2019-07: uses / debt / equity / IDC | 27.0 / 20.0 / 7.0 / 1.01 | USD m | FC base (1) | 2019-07 |
| P-F13 | Month 2020-01: uses / debt / equity / IDC | 36.5 / 27.0 / 9.5 / 1.82 | USD m | FC base (1) | 2020-01 |
| P-F13 | Month 2020-07: uses / debt / equity / IDC | 25.7 / 19.0 / 6.7 / 2.66 | USD m | FC base (1) | 2020-07 |
| P-F13 | Month 2021-01: uses / debt / equity / IDC | 8.8 / 6.5 / 2.3 / 3.14 | USD m | FC base (1) | 2021-01 |
| P-F13 | Month 2021-04: uses / debt / equity / IDC | 54.3 / 40.2 / 14.1 / 3.16 | USD m | FC base (1) | 2021-04 |
| P-F13 | Month 2021-05: uses / debt / equity / IDC | 41.8 / 31.0 / 10.8 / 3.46 | USD m | FC base (1) | 2021-05 |
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
| P-F14 | OY5 depreciation deferred | 40.2 | USD m | FC base (1) | OY5 |
| P-F14 | OY5 depreciation current | 4.5 | USD m | FC base (1) | OY5 |
| P-F14 | OY5 deferred used | 1.7 | USD m | FC base (1) | OY5 |
| P-F14 | OY5 taxable income | 0.0 | USD m | FC base (1) | OY5 |
| P-F14 | OY5 cit | 0.0 | USD m | FC base (1) | OY5 |
| P-F14 | OY5 minimum turnover tax | 0.1 | USD m | FC base (1) | OY5 |
| P-F14 | OY5 tax paid | 0.1 | USD m | FC base (1) | OY5 |
| P-F14 | OY6 ebitda | 103.8 | USD m | FC base (1) | OY6 |
| P-F14 | OY6 depreciation deferred | 5.0 | USD m | FC base (1) | OY6 |
| P-F14 | OY6 depreciation current | 35.7 | USD m | FC base (1) | OY6 |
| P-F14 | OY6 deferred used | 15.5 | USD m | FC base (1) | OY6 |
| P-F14 | OY6 taxable income | 0.0 | USD m | FC base (1) | OY6 |
| P-F14 | OY6 cit | 0.0 | USD m | FC base (1) | OY6 |
| P-F14 | OY6 minimum turnover tax | 0.6 | USD m | FC base (1) | OY6 |
| P-F14 | OY6 tax paid | 0.6 | USD m | FC base (1) | OY6 |
| P-F14 | OY7 ebitda | 104.3 | USD m | FC base (1) | OY7 |
| P-F14 | OY7 depreciation deferred | 0.0 | USD m | FC base (1) | OY7 |
| P-F14 | OY7 depreciation current | 40.2 | USD m | FC base (1) | OY7 |
| P-F14 | OY7 deferred used | 21.6 | USD m | FC base (1) | OY7 |
| P-F14 | OY7 taxable income | 0.0 | USD m | FC base (1) | OY7 |
| P-F14 | OY7 cit | 0.0 | USD m | FC base (1) | OY7 |
| P-F14 | OY7 minimum turnover tax | 0.7 | USD m | FC base (1) | OY7 |
| P-F14 | OY7 tax paid | 0.7 | USD m | FC base (1) | OY7 |
| P-F14 | OY8 ebitda | 92.4 | USD m | FC base (1) | OY8 |
| P-F14 | OY8 depreciation deferred | 0.0 | USD m | FC base (1) | OY8 |
| P-F14 | OY8 depreciation current | 40.2 | USD m | FC base (1) | OY8 |
| P-F14 | OY8 deferred used | 14.2 | USD m | FC base (1) | OY8 |
| P-F14 | OY8 taxable income | 0.0 | USD m | FC base (1) | OY8 |
| P-F14 | OY8 cit | 0.0 | USD m | FC base (1) | OY8 |
| P-F14 | OY8 minimum turnover tax | 0.7 | USD m | FC base (1) | OY8 |
| P-F14 | OY8 tax paid | 0.7 | USD m | FC base (1) | OY8 |
| P-F14 | OY9 ebitda | 105.3 | USD m | FC base (1) | OY9 |
| P-F14 | OY9 depreciation deferred | 0.0 | USD m | FC base (1) | OY9 |
| P-F14 | OY9 depreciation current | 40.2 | USD m | FC base (1) | OY9 |
| P-F14 | OY9 deferred used | 32.2 | USD m | FC base (1) | OY9 |
| P-F14 | OY9 taxable income | 0.0 | USD m | FC base (1) | OY9 |
| P-F14 | OY9 cit | 0.0 | USD m | FC base (1) | OY9 |
| P-F14 | OY9 minimum turnover tax | 0.7 | USD m | FC base (1) | OY9 |
| P-F14 | OY9 tax paid | 0.7 | USD m | FC base (1) | OY9 |
| P-F14 | OY10 ebitda | 105.8 | USD m | FC base (1) | OY10 |
| P-F14 | OY10 depreciation deferred | 0.0 | USD m | FC base (1) | OY10 |
| P-F14 | OY10 depreciation current | 40.2 | USD m | FC base (1) | OY10 |
| P-F14 | OY10 deferred used | 38.4 | USD m | FC base (1) | OY10 |
| P-F14 | OY10 taxable income | 0.0 | USD m | FC base (1) | OY10 |
| P-F14 | OY10 cit | 0.0 | USD m | FC base (1) | OY10 |
| P-F14 | OY10 minimum turnover tax | 0.7 | USD m | FC base (1) | OY10 |
| P-F14 | OY10 tax paid | 0.7 | USD m | FC base (1) | OY10 |
| P-F14 | First period with corporate income tax above the minimum tax | 2033H1 | period | FC base (1) | 2018-07-17 |
| P-F15 | OY1 cfads | 85.6 | USD m | FC base (1) | OY1 |
| P-F15 | OY1 senior interest and fees | 35.8 | USD m | FC base (1) | OY1 |
| P-F15 | OY1 senior principal | 26.3 | USD m | FC base (1) | OY1 |
| P-F15 | OY1 dsra topup net | 0.2 | USD m | FC base (1) | OY1 |
| P-F15 | OY1 shl interest paid | 16.1 | USD m | FC base (1) | OY1 |
| P-F15 | OY1 shl principal | 7.3 | USD m | FC base (1) | OY1 |
| P-F15 | OY1 dividends | 0.0 | USD m | FC base (1) | OY1 |
| P-F15 | OY1 net income | 23.0 | USD m | FC base (1) | OY1 |
| P-F15 | OY2 cfads | 101.1 | USD m | FC base (1) | OY2 |
| P-F15 | OY2 senior interest and fees | 41.0 | USD m | FC base (1) | OY2 |
| P-F15 | OY2 senior principal | 33.9 | USD m | FC base (1) | OY2 |
| P-F15 | OY2 dsra topup net | 0.1 | USD m | FC base (1) | OY2 |
| P-F15 | OY2 shl interest paid | 18.6 | USD m | FC base (1) | OY2 |
| P-F15 | OY2 shl principal | 7.5 | USD m | FC base (1) | OY2 |
| P-F15 | OY2 dividends | 0.0 | USD m | FC base (1) | OY2 |
| P-F15 | OY2 net income | 19.1 | USD m | FC base (1) | OY2 |
| P-F15 | OY3 cfads | 101.6 | USD m | FC base (1) | OY3 |
| P-F15 | OY3 senior interest and fees | 38.6 | USD m | FC base (1) | OY3 |
| P-F15 | OY3 senior principal | 36.6 | USD m | FC base (1) | OY3 |
| P-F15 | OY3 dsra topup net | 0.4 | USD m | FC base (1) | OY3 |
| P-F15 | OY3 shl interest paid | 17.9 | USD m | FC base (1) | OY3 |
| P-F15 | OY3 shl principal | 8.0 | USD m | FC base (1) | OY3 |
| P-F15 | OY3 dividends | 0.0 | USD m | FC base (1) | OY3 |
| P-F15 | OY3 net income | 22.5 | USD m | FC base (1) | OY3 |
| P-F15 | Maximum trapped cash with 80% shareholder loans | 0.0 | USD m | FC base (1) | 2018-07-17 |
| P-F15 | Maximum trapped cash with 100% share capital | 172.8 | USD m | FC base (1), no SHL variant | 2018-07-17 |
| P-F15 | Equity IRR with 100% share capital | 12.8% | % | FC base (1), no SHL variant | 2018-07-17 |
| P-F16 | Equity IRR (project-company level, from LNTP date, before WHT) | 13.3% | % nominal post-tax | FC base (1) | 2018-07-17 |
| P-F16 | Equity IRR including development spend and reimbursement | 13.6% | % | FC base (1) | 2018-07-17 |
| P-F16 | Project IRR, post-tax | 11.0% | % | FC base (1) | 2018-07-17 |
| P-F16 | Project IRR, pre-tax | 11.6% | % | FC base (1) | 2018-07-17 |
| P-F16 | Equity NPV at 16.0% at financial close | -43.1 | USD m | FC base (1) | 2018-07-17 |
| P-F16 | Equity payback (cumulative equity cash flow turns positive) | 2031-06-30 | date | FC base (1) | 2018-07-17 |
| P-F16 | FC base: minimum DSCR / average DSCR / equity IRR | 1.35x / 1.54x / 13.3% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | FC banking: minimum DSCR / average DSCR / equity IRR | 1.34x / 1.53x / 13.1% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | FC downside: minimum DSCR / average DSCR / equity IRR | 1.20x / 1.38x / 11.4% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: availability -3 points: minimum DSCR / average DSCR / equity IRR | 1.32x / 1.53x / 13.2% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: heat rate +2%: minimum DSCR / average DSCR / equity IRR | 1.30x / 1.49x / 12.5% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: fixed opex +10%: minimum DSCR / average DSCR / equity IRR | 1.32x / 1.51x / 12.8% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: capex +10% funded pro rata: minimum DSCR / average DSCR / equity IRR | 1.23x / 1.38x / 11.4% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: COD delay 6 months, no LDs: minimum DSCR / average DSCR / equity IRR | 1.25x / 1.45x / 12.1% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: base rate +200 bps (unhedged): minimum DSCR / average DSCR / equity IRR | 1.30x / 1.51x / 12.9% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: KCR devaluation 40%, 90-day lag: minimum DSCR / average DSCR / equity IRR | 0.45x / 1.52x / 12.9% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: SEKA pays 120 days late for 12 months: minimum DSCR / average DSCR / equity IRR | 0.13x / 1.54x / 13.2% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: dispatch 50%: minimum DSCR / average DSCR / equity IRR | 1.29x / 1.48x / 12.4% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Sens: gas price +30%: minimum DSCR / average DSCR / equity IRR | 1.35x / 1.54x / 13.3% | x, x, % | Sensitivity (debt locked) | 2018-07-17 |
| P-F16 | Breakeven availability shift for 1.00x minimum DSCR | -21.4 | points below profile | FC base (1) | 2018-07-17 |
| P-F16 | Breakeven capacity charge cut for 1.00x minimum DSCR | 25.0% | % | FC base (1) | 2018-07-17 |
| P-F16 | Months of zero SEKA payment covered by DSRA plus LC (gas paid) | 3.0 | months | FC base (1) | 2022H1 |
| P-F16 | Months covered if gas payments are deferred | 8.2 | months | FC base (1) | 2022H1 |
| P-F17 | correct: correct model | debt 633.3 (+0.0), DSCR; min DSCR 1.35x; avg 1.54x; downside 1.20x; banking 1.34x; LLCR 1.42x; equity IRR 13.3% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E1: Capacity payment without the availability cap (A/90% not capped at 1) | debt 641.9 (+8.7), downside; min DSCR 1.37x; avg 1.56x; downside 1.20x; banking 1.36x; LLCR 1.44x; equity IRR 14.1% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E2: LTSA variable fee on one gas turbine instead of two | debt 643.1 (+9.9), gearing; min DSCR 1.38x; avg 1.57x; downside 1.23x; banking 1.37x; LLCR 1.45x; equity IRR 14.4% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E3: Tariff indexation reads the index at period end instead of the lagged (Sep/Mar) reading | debt 640.1 (+6.8), DSCR; min DSCR 1.35x; avg 1.54x; downside 1.20x; banking 1.34x; LLCR 1.42x; equity IRR 13.6% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E4: Senior loan interest on 30/360 instead of ACT/360 | debt 636.0 (+2.8), DSCR; min DSCR 1.35x; avg 1.54x; downside 1.20x; banking 1.34x; LLCR 1.42x; equity IRR 13.4% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E5: Full tax exemption applied to OY1-OY8 (15% band ignored) | debt 639.9 (+6.6), DSCR; min DSCR 1.35x; avg 1.54x; downside 1.20x; banking 1.34x; LLCR 1.42x; equity IRR 13.7% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E6: Deferred holiday depreciation lost (pool never credited) | debt 614.2 (-19.1), DSCR; min DSCR 1.35x; avg 1.54x; downside 1.20x; banking 1.34x; LLCR 1.42x; equity IRR 12.5% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E7: DSRA initial funding drawn 100% from senior debt instead of pro rata | debt 633.3 (+0.1), DSCR; min DSCR 1.35x; avg 1.54x; downside 1.20x; banking 1.34x; LLCR 1.42x; equity IRR 13.2% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E8: Sculpting on CFADS before tax | debt 641.2 (+8.0), DSCR; min DSCR 1.34x; avg 1.51x; downside 1.20x; banking 1.33x; LLCR 1.40x; equity IRR 13.4% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E9: Fuel-charge revenue uses a typed 76.5% dispatch instead of the live dispatch | debt 633.3 (+0.0), DSCR; min DSCR 1.35x; avg 1.54x; downside 1.20x; banking 1.46x; LLCR 1.42x; equity IRR 13.3% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | E10: Swap net settlement with legs reversed | debt 623.4 (-9.9), DSCR; min DSCR 1.35x; avg 1.54x; downside 1.20x; banking 1.34x; LLCR 1.42x; equity IRR 12.9% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F17 | ALL: all ten errors together | debt 654.6 (+21.4), gearing; min DSCR 1.44x; avg 1.53x; downside 1.26x; banking 1.54x; LLCR 1.43x; equity IRR 15.2% | USD m, x, % | FC base, sponsor model v0.9 | 2018-06 |
| P-F18 | Actual use: epc | 565.12 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: epc fx gain on onshore | 6.72 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: owners costs incl extension | 53.11 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: overrun items excl extension | 32.34 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: hard cost overrun total | 39.27 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: contingency available | 38.40 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: other base | 54.57 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: subtotal before financing | 705.14 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: idc loans | 44.70 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: swap net | 13.66 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: pri | 4.16 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: commitment fees | 12.30 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: upfront fees | 9.95 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: eca premium | 20.41 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: agency | 0.87 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: vat interest | 1.49 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: dsra initial | 33.84 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual use: total | 846.53 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: senior debt drawn | 626.92 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: senior commitment | 633.26 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: undrawn commitment cancelled | 6.34 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: base equity | 219.61 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: delay lds received | 10.14 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: dsu received | 7.08 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: lds and dsu applied to construction | -0.00 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: lds and dsu unused to operating cash | 17.22 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: standby drawn | 0.00 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | Actual source: contingent equity drawn | 0.00 | USD m | Actual history (15) | 2021-12-01 |
| P-F18 | total funding fc | 855.09 | USD m | Actual history (15) vs FC base (1) | 2021-12-01 |
| P-F18 | idc fc | 63.90 | USD m | Actual history (15) vs FC base (1) | 2021-12-01 |
| P-F18 | idc actual | 62.52 | USD m | Actual history (15) vs FC base (1) | 2021-12-01 |
| P-F19 | Tested net output / heat rate | 581.9 MW / 6,286 kJ/kWh | inputs | Inputs | 2021-11-30 |
| P-F19 | Output LDs / heat-rate LDs / total | 13.975 / 4.510 / 18.485 | USD m | Inputs | 2021-11-30 |
| P-F19 | COD re-sculpted constant DSCR (before the LD prepayment) | 1.31x | x | COD re-forecast (14) | 2021-12-01 |
| P-F19 | Same, had capacity and heat rate stayed at 588.4 MW / 6,261 | 1.33x | x | COD re-forecast (14) variant | 2021-12-01 |
| P-F19 | Projected minimum DSCR after the June 2022 LD prepayment | 1.35x | x | COD re-forecast (14) | 2022-06-30 |
| P-F19 | Projected average DSCR after the prepayment | 1.55x | x | COD re-forecast (14) | 2022-06-30 |
| P-F19 | Projected minimum DSCR without the prepayment | 1.31x | x | COD re-forecast (14) variant | 2022-06-30 |
| P-F20 | 2022H1: overdue / deferred SNHK-GCK payables / CFADS / debt service / DSCR / DSRA draw / DSRA balance | 18.4 / 14.7 / 44.8 / 35.1 / 1.28x / 0.0 / 36.8 | USD m, x | Actual history (15) | 2022H1 |
| P-F20 | 2022H2: overdue / deferred SNHK-GCK payables / CFADS / debt service / DSCR / DSRA draw / DSRA balance | 68.9 / 55.1 / 37.3 / 36.8 / 1.01x / 0.0 / 37.3 | USD m, x | Actual history (15) | 2022H2 |
| P-F20 | 2023H1: overdue / deferred SNHK-GCK payables / CFADS / debt service / DSCR / DSRA draw / DSRA balance | 112.6 / 90.1 / 35.7 / 38.2 / 0.94x / 2.5 / 34.8 | USD m, x | Actual history (15) | 2023H1 |
| P-F20 | 2023H2: overdue / deferred SNHK-GCK payables / CFADS / debt service / DSCR / DSRA draw / DSRA balance | 71.8 / 57.4 / 56.2 / 29.7 / 1.89x / 0.0 / 43.1 | USD m, x | Actual history (15) | 2023H2 |
| P-F20 | 2024H1: overdue / deferred SNHK-GCK payables / CFADS / debt service / DSCR / DSRA draw / DSRA balance | 34.6 / 27.7 / 57.4 / 43.1 / 1.33x / 0.0 / 43.3 | USD m, x | Actual history (15) | 2024H1 |
| P-F20 | 2024H2: overdue / deferred SNHK-GCK payables / CFADS / debt service / DSCR / DSRA draw / DSRA balance | 12.3 / 9.8 / 56.7 / 43.3 / 1.31x / 0.0 / 41.3 | USD m, x | Actual history (15) | 2024H2 |
| P-F20 | 2025H1: overdue / deferred SNHK-GCK payables / CFADS / debt service / DSCR / DSRA draw / DSRA balance | 0.0 / 0.0 / 55.4 / 41.3 / 1.34x / 0.0 / 32.0 | USD m, x | Actual history (15) | 2025H1 |
| P-F20 | FX conversion losses, total 2022H2-2024H1 | 6.54 | USD m | Inputs | 2024-06-30 |
| P-F20 | Late payment interest accrued / received (60%) | 8.7 / 5.2 | USD m | Actual history (15) | 2025-06-30 |
| P-F20 | Lock-up periods (distribution test failed) | 2022H2, 2023H1, 2023H2, 2024H1 | periods | Actual history (15) | 2024-12-31 |
| P-F21 | Historic DSCR at December 31, 2022 | 1.14x | x | Actual history (15) | 2022-12-31 |
| P-F21 | Historic DSCR at June 30, 2023 (event of default below 1.10x) | 0.97x | x | Actual history (15) | 2023-06-30 |
| P-F21 | Period DSCR 2023H1 | 0.94x | x | Actual history (15) | 2023-06-30 |
| P-F21 | DSRA drawing at June 30, 2023 | 2.46 | USD m | Actual history (15) | 2023-06-30 |
| P-F21 | Waiver fee (0.25% of senior debt) | 1.40 | USD m | Actual history (15) | 2023-10-26 |
| P-F21 | Margin uplift cost, 2023H2-2024H2 | 4.35 | USD m | Actual history (15) | 2024-12-31 |
| P-F21 | Principal deferred from December 31, 2023 (60%) | 10.77 | USD m | Actual history (15) | 2023-12-31 |
| P-F21 | Each of four deferred repayments (2024H1-2025H2) | 2.69 | USD m | Actual history (15) | 2024-06-30 |
| P-F21 | Historic DSCR at December 31, 2023 (waived test) | 1.35x | x | Actual history (15) | 2023-12-31 |
| P-F21 | Lock-up released (two tests >= 1.25x and DSRA full) | 2024H2 | period | Actual history (15) | 2024-12-31 |
| P-F22 | Base rate 2022H2 (6M LIBOR) | 2.94% | % | Actual history (15) | 2022-07 |
| P-F22 | Base rate 2023H1 (6M Term SOFR 4.86% + 0.42826%) | 5.29% | % | Actual history (15) | 2023-01 |
| P-F22 | Senior financing cost 2022H2 / 2023H1 | 20.2 / 21.0 | USD m | Actual history (15) | 2023-06-30 |
| P-F22 | All-in senior cost 2022H2 / 2023H1 | 6.68% / 7.26% | % pa | Actual history (15) | 2023-06-30 |
| P-F22 | Unhedged balance 2023H1 (debt less swap notional) | 108.2 | USD m | Actual history (15) | 2023-01 |
| P-F22 | Cost of the 0.42826% spread adjustment, 2023H1 / calendar 2023 | 0.23 / 0.46 | USD m | Actual history (15) | 2023-12-31 |
| P-F23 | prepaid principal | 233.00 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | swap unwind receipt | 6.30 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | bond face | 233.99 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | bond proceeds | 232.85 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | oid | 1.14 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | underwriting | 2.34 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | other costs | 3.10 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | pcg upfront | 0.71 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | transaction costs total | 7.29 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | remaining eca | 145.62 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | remaining a loan | 106.79 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | equity pv gain at 13 75pct | 13.97 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | equity pv gain at 12 50pct | 10.06 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | prepaid B | 48.54 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | prepaid COM | 184.46 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | prepaid SB | 0.00 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Combined sculpted DSCR (ECA + A-loan + bond, constant) | 1.62x | x | Actual history (15) | 2025-06-30 |
| P-F23 | Minimum DSCR after refinancing | 1.62x | x | Actual history (15) | 2025-06-30 |
| P-F23 | Equity IRR with / without the refinancing | 13.4% / 13.0% | % | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2025H2 | 2.63 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2026H2 | 4.24 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2027H2 | 4.54 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2028H2 | 4.82 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2029H2 | 5.65 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2030H2 | 6.03 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2031H2 | 6.35 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2032H2 | 6.64 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2033H2 | 5.50 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2034H2 | 20.85 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2035H2 | 22.43 | USD m | Actual history (15) | 2025-06-30 |
| P-F23 | Bond amortization 2036H2 | 24.05 | USD m | Actual history (15) | 2025-06-30 |
| P-F24 | equity value 100pct at 13 75 | 327.37 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | equity value 100pct at 12 50 | 358.72 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | value 24pct at 13 75 | 78.57 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | value 24pct at 12 50 | 86.09 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | leakage h1 2026 distribution 24pct | 4.39 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | price at completion | 78.00 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | kilnworth reserve price 24pct | 85.89 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | deferred consideration | 4.00 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | cost basis 24pct | 33.90 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | seller gain | 44.10 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | indirect transfer tax | 6.62 | USD m | Actual history (15) | 2025-12-31 (locked box); 2026-09-30 (completion) |
| P-F24 | Locked-box ticker factor (6.5% simple, 273 days) | 1.0486 | factor | Actual history (15) | 2026-09-30 |
| P-F24 | Kilnworth's IRR on the sold 24% (after transfer tax) | 11.5% | % | Actual history (15) | 2026-09-30 |
| P-F24 | Same including the USD 4.0 million deferred consideration (taxed) | 12.0% | % | Actual history (15) | 2027-06-30 |
| P-F25 | senior debt outstanding | 558.8 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | swap mtm to project | 30.4 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | equity npv distributions 14 5 | 291.9 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | equity contributed compounded less distributions | 326.5 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | equity amount | 326.5 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | seka default compensation | 854.9 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | project default compensation | 558.8 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | natural fm compensation | 760.7 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | equity contributed | 219.6 | USD m | Actual history (15) | 2023-06-30 |
| P-F25 | distributions received | 17.7 | USD m | Actual history (15) | 2023-06-30 |
| P-F26 | book equity at completion (simplified; framework to be confirmed) | 134.0 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | shl at completion (simplified; framework to be confirmed) | 163.8 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | kilnworth carrying amount 60pct (simplified; framework to be confirmed) | 178.7 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | consideration (simplified; framework to be confirmed) | 78.0 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | fv retained 36pct (simplified; framework to be confirmed) | 123.6 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | remeasurement and disposal gain (simplified; framework to be confirmed) | 22.9 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | equity method carrying value 36pct (simplified; framework to be confirmed) | 123.6 | USD m | Actual history (15) | 2026-09-30 |
| P-F26 | indirect transfer tax (simplified; framework to be confirmed) | 6.6 | USD m | Actual history (15) | 2026-09-30 |
| P-F27 | fc base: dividends (life total) | 1,005.3 | USD m | FC base (1) | 2018-2046 |
| P-F27 | fc base: shl interest (life total) | 184.7 | USD m | FC base (1) | 2018-2046 |
| P-F27 | fc base: wht dividends treaty 7 5 (life total) | 75.4 | USD m | FC base (1) | 2018-2046 |
| P-F27 | fc base: wht dividends domestic 15 (life total) | 150.8 | USD m | FC base (1) | 2018-2046 |
| P-F27 | fc base: wht shl interest treaty 5 (life total) | 9.2 | USD m | FC base (1) | 2018-2046 |
| P-F27 | fc base: wht shl interest domestic 10 (life total) | 18.5 | USD m | FC base (1) | 2018-2046 |
| P-F27 | fc base: commercial grossup cost (life total) | 16.3 | USD m | FC base (1) | 2018-2046 |
| P-F27 | actual: dividends (life total) | 1,008.4 | USD m | Actual history (15) | 2018-2046 |
| P-F27 | actual: shl interest (life total) | 104.5 | USD m | Actual history (15) | 2018-2046 |
| P-F27 | actual: wht dividends treaty 7 5 (life total) | 75.6 | USD m | Actual history (15) | 2018-2046 |
| P-F27 | actual: wht dividends domestic 15 (life total) | 151.3 | USD m | Actual history (15) | 2018-2046 |
| P-F27 | actual: wht shl interest treaty 5 (life total) | 5.2 | USD m | Actual history (15) | 2018-2046 |
| P-F27 | actual: wht shl interest domestic 10 (life total) | 10.4 | USD m | Actual history (15) | 2018-2046 |
| P-F27 | actual: commercial grossup cost (life total) | 9.5 | USD m | Actual history (15) | 2018-2046 |
| P-F28 | Senior debt / total funding / gearing | 633.3 / 855.1 / 74.1% | USD m, % | FC base (1) | 2018-05 |
| P-F28 | Tenor from COD / WAL | 13.2 / 7.18 | years | FC base (1) | 2018-05 |
| P-F28 | base: min DSCR / avg DSCR / LLCR | 1.35x / 1.54x / 1.42x | x | FC base (1) | 2018-05 |
| P-F28 | banking: min DSCR / avg DSCR / LLCR | 1.34x / 1.53x / 1.41x | x | FC banking (2) | 2018-05 |
| P-F28 | downside: min DSCR / avg DSCR / LLCR | 1.20x / 1.38x / 1.31x | x | FC downside (3) | 2018-05 |
| P-F28 | Equity IRR / project IRR (base) | 13.3% / 11.0% | % | FC base (1) | 2018-05 |
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
| P-F31 | OY1 revenue: actual (Dec 2021-Nov 2022) / FC base (May 2021-Apr 2022) | 319.2 / 319.7 | % or USD m | Actual history (15) / FC base (1) | 2022-11-30 |
| P-F31 | OY1 operating costs: actual (Dec 2021-Nov 2022) / FC base (May 2021-Apr 2022) | 222.0 / 218.2 | % or USD m | Actual history (15) / FC base (1) | 2022-11-30 |
| P-F31 | OY1 ebitda: actual (Dec 2021-Nov 2022) / FC base (May 2021-Apr 2022) | 97.2 / 101.5 | % or USD m | Actual history (15) / FC base (1) | 2022-11-30 |
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
| P-F33 | daily interest per day | 118,240 | USD | FC base (1) | 2021-05-01 |
| P-F33 | daily fixed costs per day | 57,410 | USD | FC base (1) | 2021-05-01 |
| P-F33 | ppa delay ld per day | 94,150 | USD | FC base (1) | 2021-05-01 |
| P-F33 | total per day | 269,800 | USD | FC base (1) | 2021-05-01 |
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
| P-F36 | DSCR 1.30x / gearing 70% | debt 592.3 (gearing); downside min 1.28x; equity IRR 12.9% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.30x / gearing 75% | debt 642.9 (gearing); downside min 1.18x; equity IRR 13.4% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.30x / gearing 80% | debt 658.1 (DSCR); downside min 1.19x; equity IRR 13.5% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.35x / gearing 70% | debt 592.3 (gearing); downside min 1.28x; equity IRR 12.9% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.35x / gearing 75% | debt 633.3 (DSCR); downside min 1.20x; equity IRR 13.3% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.35x / gearing 80% | debt 633.3 (DSCR); downside min 1.20x; equity IRR 13.3% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.40x / gearing 70% | debt 592.3 (gearing); downside min 1.28x; equity IRR 12.9% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.40x / gearing 75% | debt 610.1 (DSCR); downside min 1.24x; equity IRR 13.1% | USD m, x, % | FC base (1) | 2017-10 |
| P-F36 | DSCR 1.40x / gearing 80% | debt 610.1 (DSCR); downside min 1.24x; equity IRR 13.1% | USD m, x, % | FC base (1) | 2017-10 |
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
| P-F38 | Thin cap fc base: SHL interest total / deductible / disallowed | 189.8 / 186.0 / 3.8 | USD m | FC base (1) | life |
| P-F38 | Thin cap fc base: deductible share in the COD period | 66.0% | % | FC base (1) | COD |
| P-F38 | Thin cap actual: SHL interest total / deductible / disallowed | 146.8 / 139.4 / 7.4 | USD m | Actual history (15) | life |
| P-F38 | Thin cap actual: deductible share in the COD period | 64.1% | % | Actual history (15) | COD |
| P-F39 | LC size on the PPA formula, FC base (2021H2 rates) | 36.6 | USD m | FC base (1) | 2021-05-01 |
| P-F39 | LC size on the PPA formula, actual (2022H1 rates) | 36.6 | USD m | Actual history (15) | 2021-12-01 |
| P-F40 | FX conversion losses total (2022H2-2024H1) | 6.54 | USD m | Inputs | 2024-03-29 |
| P-F40 | Energy-charge arrears matched by deferred SNHK/GCK payables, peak (2023-06-30) | 90.1 | USD m | Actual history (15) | 2023-06-30 |
| P-F40 | Overdue reduction 2024H1 / 2024H2 / 2025H1 | 37.2 / 22.3 / 12.3 | USD m | Inputs | 2025-06-30 |
| P-F40 | Implied monthly settlement installment 2024H2 / 2025H1 | 3.72 / 2.05 | USD m | Inputs | 2025-06-30 |
| P-F40 | Late payment interest received / waived | 5.22 / 3.48 | USD m | Actual history (15) | 2025-06-30 |
| P-F41 | PLCR at close | 1.86x | x | FC base (1) | 2018-07-17 |
| P-F41 | LLCR at close (incl. DSRA) | 1.42x | x | FC base (1) | 2018-07-17 |
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
| P-F41 | FC base 2028H1: CFADS / DS / DSCR | 49.8 / 35.4 / 1.40x | USD m, x | FC base (1) | 2028H1 |
| P-F41 | FC base 2028H2: CFADS / DS / DSCR | 51.7 / 36.0 / 1.44x | USD m, x | FC base (1) | 2028H2 |
| P-F41 | FC base 2029H1: CFADS / DS / DSCR | 51.7 / 35.0 / 1.48x | USD m, x | FC base (1) | 2029H1 |
| P-F41 | FC base 2029H2: CFADS / DS / DSCR | 51.9 / 33.9 / 1.53x | USD m, x | FC base (1) | 2029H2 |
| P-F41 | FC base 2030H1: CFADS / DS / DSCR | 51.5 / 32.2 / 1.60x | USD m, x | FC base (1) | 2030H1 |
| P-F41 | FC base 2030H2: CFADS / DS / DSCR | 52.2 / 31.0 / 1.68x | USD m, x | FC base (1) | 2030H2 |
| P-F41 | FC base 2031H1: CFADS / DS / DSCR | 51.8 / 28.7 / 1.81x | USD m, x | FC base (1) | 2031H1 |
| P-F41 | FC base 2031H2: CFADS / DS / DSCR | 52.4 / 26.4 / 1.98x | USD m, x | FC base (1) | 2031H2 |
| P-F41 | FC base 2032H1: CFADS / DS / DSCR | 52.2 / 23.0 / 2.26x | USD m, x | FC base (1) | 2032H1 |
| P-F41 | FC base 2032H2: CFADS / DS / DSCR | 53.3 / 23.7 / 2.25x | USD m, x | FC base (1) | 2032H2 |
| P-F41 | FC base 2033H1: CFADS / DS / DSCR | 52.5 / 23.6 / 2.23x | USD m, x | FC base (1) | 2033H1 |
| P-F41 | FC base 2033H2: CFADS / DS / DSCR | 42.4 / 19.1 / 2.22x | USD m, x | FC base (1) | 2033H2 |
| P-F41 | FC base 2034H1: CFADS / DS / DSCR | 41.5 / 18.9 / 2.20x | USD m, x | FC base (1) | 2034H1 |
| P-F41 | Actual 2022H1: CFADS / DS / DSCR | 44.8 / 35.1 / 1.28x | USD m, x | Actual history (15) | 2022H1 |
| P-F41 | Actual 2022H2: CFADS / DS / DSCR | 37.3 / 36.8 / 1.01x | USD m, x | Actual history (15) | 2022H2 |
| P-F41 | Actual 2023H1: CFADS / DS / DSCR | 35.7 / 38.2 / 0.94x | USD m, x | Actual history (15) | 2023H1 |
| P-F41 | Actual 2023H2: CFADS / DS / DSCR | 56.2 / 29.7 / 1.89x | USD m, x | Actual history (15) | 2023H2 |
| P-F41 | Actual 2024H1: CFADS / DS / DSCR | 57.4 / 43.1 / 1.33x | USD m, x | Actual history (15) | 2024H1 |
| P-F41 | Actual 2024H2: CFADS / DS / DSCR | 56.7 / 43.3 / 1.31x | USD m, x | Actual history (15) | 2024H2 |
| P-F41 | Actual 2025H1: CFADS / DS / DSCR | 55.4 / 41.3 / 1.34x | USD m, x | Actual history (15) | 2025H1 |
| P-F41 | Actual 2025H2: CFADS / DS / DSCR | 51.7 / 32.0 / 1.62x | USD m, x | Actual history (15) | 2025H2 |
| P-F41 | Actual 2026H1: CFADS / DS / DSCR | 49.1 / 30.4 / 1.62x | USD m, x | Actual history (15) | 2026H1 |
| P-F41 | Actual 2026H2: CFADS / DS / DSCR | 49.9 / 30.8 / 1.62x | USD m, x | Actual history (15) | 2026H2 |
| P-F42 | Monte Carlo inputs | availability_shock: per operating year, normal(0, 2.0 points), truncated to -10/+5 points, independent across years; dispatch: one draw per run, triangular(55.0%, 76.5%, 85.0%); heat_rate_degradation: non-recoverable rate per year, normal(0.12%, 0.04%), floored at 0; fx: KCR depreciation drift per year, normal(5.19%, 3.0%) applied to the FC FX path; debt: locked at the FC base contract (amount and repayment profile); 1000 runs, seed 20180717 | text | FC base (1), debt locked | 2018-07-17 |
| P-F42 | Minimum DSCR P10 / P50 / P90 | 1.31x / 1.33x / 1.36x | x | FC base (1) | 2018-07-17 |
| P-F42 | Equity IRR P10 / P50 / P90 | 12.7% / 13.1% / 13.7% | % | FC base (1) | 2018-07-17 |
| P-F42 | Probability of a historic DSCR below 1.20x / 1.10x in any test | 0.0% / 0.0% | % | FC base (1) | 2018-07-17 |
| P-F42 | Minimum DSCR histogram (bins 1.0,1.1,1.2,1.25,1.3,1.35,1.4,1.5,+) | 0, 0, 1, 64, 763, 172, 0, 0 | runs | FC base (1) | 2018-07-17 |
| P-F43 | Sizing passes to USD 1,000 tolerance (profile, debt, notional) | 11 | passes | FC base (1) | 2018-07-17 |
| P-F43 | Sizing residuals by pass | 529.5, 529.5, 628.6, 11.76, 3.726, 0.09861, 0.07889, 0.001761, 0.0004971, 3.45e-05, 3.53e-06 | USD m | FC base (1) | 2018-07-17 |
| P-F43 | Construction fixed-point passes (Python) | 12 | passes | FC base (1) | 2018-07-17 |
| P-F43 | Closed-form total funding at the 75% gearing cap | 857.2 | USD m | FC base (1) | 2018-07-17 |
| P-F43 | Pro rata: total funding / debt / IDC incl. swap and PRI | 855.1 / 633.3 / 63.9 | USD m | FC base (1) | 2018-07-17 |
| P-F43 | Equity first: total funding / debt / equity / IDC / commitment fees | 840.5 / 630.4 / 210.1 / 47.2 / 12.6 | USD m | FC base (1) variant | 2018-07-17 |
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
| P-F45 | balance sheet 2018 12 31: plant | 139.1 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet 2018 12 31: cash in project accounts | 0.0 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet 2018 12 31: of which dsra | 0.0 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet 2018 12 31: receivables | 0.0 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet 2018 12 31: of which overdue | 0.0 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet 2018 12 31: inventory | 0.0 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet 2018 12 31: deferred tax asset | 0.0 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet 2018 12 31: total assets | 139.1 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet 2018 12 31: senior debt | 102.4 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet 2018 12 31: shareholder loans | 29.5 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet 2018 12 31: payables | 0.0 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet 2018 12 31: deferred tax liability | 0.0 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet 2018 12 31: share capital | 7.2 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet 2018 12 31: retained earnings | 0.0 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet 2018 12 31: total liabilities and equity | 139.1 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet 2018 12 31: balance check | -0.0 | USD m | FC base (1) | 2018-12-31 |
| P-F45 | balance sheet at cod period end: plant | 831.1 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | balance sheet at cod period end: cash in project accounts | 39.1 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | balance sheet at cod period end: of which dsra | 37.2 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | balance sheet at cod period end: receivables | 39.1 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | balance sheet at cod period end: of which overdue | 0.0 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | balance sheet at cod period end: inventory | 5.3 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | balance sheet at cod period end: deferred tax asset | 1.7 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | balance sheet at cod period end: total assets | 916.4 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | balance sheet at cod period end: senior debt | 633.3 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | balance sheet at cod period end: shareholder loans | 204.9 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | balance sheet at cod period end: payables | 24.1 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | balance sheet at cod period end: deferred tax liability | 0.0 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | balance sheet at cod period end: share capital | 44.4 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | balance sheet at cod period end: retained earnings | 9.8 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | balance sheet at cod period end: total liabilities and equity | 916.4 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | balance sheet at cod period end: balance check | 0.0 | USD m | FC base (1) | 2021-06-30 |
| P-F45 | FY2022 income statement: revenue | 321.8 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 income statement: late payment interest | 0.0 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 income statement: operating costs | 219.9 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 income statement: of which fuel and transport | 184.6 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 income statement: ebitda | 101.9 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 income statement: depreciation | 33.5 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 income statement: finance costs | 60.5 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 income statement: of which shareholder loan interest | 18.8 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 income statement: current tax | 0.0 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 income statement: deferred tax | -10.0 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 income statement: net income | 17.9 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 cash flow: ebitda | 101.9 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 cash flow: tax paid | 0.0 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 cash flow: increase in working capital | 0.1 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 cash flow: mmra net | 0.8 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 cash flow: cfads | 101.0 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 cash flow: senior interest and fees | 41.7 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 cash flow: senior principal | 33.1 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 cash flow: ld prepayment | 0.0 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 cash flow: sweeps | 0.0 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 cash flow: dsra topup less release | 0.2 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 cash flow: shl interest paid | 18.8 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 cash flow: shl principal repaid | 7.2 | USD m | FC base (1) | FY2022 |
| P-F45 | FY2022 cash flow: dividends | 0.0 | USD m | FC base (1) | FY2022 |

Values outside Case Bible design ranges (reported to the editor-in-chief): standby facility and contingent equity drawing 0.0 (range 5 to 15); FC base equity IRR below the 16.0% bid target. See `model/case_p_report.md` Section 6.
