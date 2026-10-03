# Case P input requests for the modeler

Version 1.0, October 3, 2026. From the Case Bible editor to the Case P modeler. Source of every value: `bible/case-bible-annex-p.md` (section numbers in brackets). Do not treat this file as an edit to `inputs_case_p.json`; the modeler absorbs these values into the JSON and the model when the current build allows, and reports back in the model report which were absorbed, with the model version. Units follow the JSON key convention.

Priority: A = changes an existing output or is needed for a ledger figure a chapter prints; B = new figure only; C = confirmation of a rule the model already applies (no change expected).

## 1. New or changed numeric inputs

| # | Input | Value | Units | Annex | Affects | Priority |
|---|---|---|---|---|---|---|
| 1 | Kessara policy rate, year end, missing years | 2016: 14.5; 2017: 14.0; 2019: 13.5; 2020: 13.5 | % | 4.5 | VAT facility interest during construction (model already uses 13.5 for 2019 and 2020) | C |
| 2 | ECA first-repayment test | No later than 24 months after COD, with at least 2.0% of principal repaid by then (replaces 6 months) | months; % | 3.6 | ECA test reporting (P-F09) | A |
| 3 | FC downside dispatch | 76.5 (base dispatch); 58.0 is the low-dispatch case for gas analysis only (P-F35) | % | 3.7 | Confirms scenario 3 | C |
| 4 | Index readings for tariff resets | September reading for January 1; March reading for July 1 | – | 3.9 | P-F02 | C |
| 5 | Contracted capacity in January 2022 | 581.9 | MW | 1.1.5 | P-F02, P-F32 | C |
| 6 | Actual dispatch factor when available, 2022 | 2022H1: 84.0; 2022H2: 81.5; from 2023: 76.5 | % | 4.11 | Actual history: fuel and VOM revenue, gas volumes, LTSA EOH, take-or-pay; P-F58 | A |
| 7 | GSA and GTA expiry | 22 contract years from COD: 2043-04-30 (FC base), 2043-11-30 (actual); option to extend to PPA expiry | date | 1.7.1, 1.8 | Model assumption after expiry: fuel and GTA charges continue as pass-through on the same terms (state as a simplification) | C |
| 8 | LTSA term | Earlier of 128,000 EOH per GT and 16 years from COD; model continues LTSA fees at the same prices afterward (successor LTSA) | EOH; years | 1.5 | P-F48 | B |
| 9 | LTSA inspection intervals | CI at 16,000 and 48,000 EOH; HGP at 32,000; MI at 64,000; repeat | EOH | 1.5 | P-F48 (check against the availability profile) | B |
| 10 | Base EOH per GT per year | 8,059 hours + 38 starts x 10 EOH = 8,439 | EOH | 1.5 | P-F48 | C |
| 11 | Handback reserve indexation | US CPI from 2018 (already modeled) | – | 1.1.6 | P-F29 | C |
| 12 | Handback test thresholds | Output at least 523.7 MW (90% of 581.9); heat rate no more than 6,789 kJ/kWh (108% of 6,286) | MW; kJ/kWh | 1.1.6 | P-F29 narrative check against degraded performance at OY25 | B |
| 13 | Termination amount definitions | Equity contributed = share capital + shareholder loan principal advanced in cash including the LNTP, excluding capitalized SHL interest; distributions = dividends + SHL interest + SHL principal, gross of WHT; 14.5% compounding from each contribution date; payment within 90 days | – | 1.1.7 | P-F25 | A |
| 14 | LC formula (two-plus-one) | 2 x monthly capacity charges (contracted capacity x indexed capacity charge, 100% payment) + 1 x monthly energy charges (contracted capacity x 730 h x 90.0% x dispatch plan factor; fuel + VOM + GTA) at that year's prices; reset at COD and each January 1 | USD m | 1.1.5 | P-F39 | B |
| 15 | LC formula (three-month, Kilnworth's 2017 opening ask) | 3 x (monthly capacity charges + monthly energy charges), same estimating basis | USD m | 1.1.5 | P-F39 | B |
| 16 | PRI policy | Inception 2018-07-17; to 2034-06-30; premium 1.15% a year on 90% of the commercial tranche balance, semiannually in advance; cancelled 2025-06-30 with no return premium | % ; dates | 1.11.2 | P-F51 (model already applies the premium) | C |
| 17 | PRG | USD 41.5 million to PPA expiry; fee 0.75% a year paid by the project company (unsubsidized 1.50%) | USD m; % | 4.9 | Confirms the model | C |
| 18 | Standby facility margin | Each participant's own tranche margin + 0.25% (commercial banks: commercial schedule + 0.25; ABDB: A-loan margin + 0.25) | % | 1.15.1 | Confirms the model | C |
| 19 | Development fee split | Kilnworth 7.84; Talmé 3.36 | USD m | 1.14.2 | P-F07, P-F49, returns by sponsor | A |
| 20 | ABDB fund development premium split | Paid to Kilnworth 3.2333; to Talmé 1.6167 (fund bought 10 points from Kilnworth, 5 from Talmé) | USD m | 1.14.2 | P-F49; Kilnworth's and Talmé's realized returns | A |
| 21 | Development cost reimbursement split | In proportion to amounts funded under the co-development agreement: Phase 1 (2015, up to USD 1.5 million) 100% Kilnworth, then 70:30 cash calls, with Talmé's in-kind credit of USD 0.9 million counted as Talmé funding | USD m | 1.14.1 | P-F49 | B |
| 22 | Grid-event claim | USD 9.27 million claimed from SEKA in March 2022; never paid; waived 2024-03-21 | USD m | 1.1.3 | None (no cash flow); confirm the model books no receivable | C |
| 23 | Thin capitalization rule | Related-party debt (all shareholder loans, including the ABDB fund's) <= 3 x (share capital + positive retained earnings); excess interest permanently non-deductible; no recharacterization | x | 4.15 | P-F38 (the model's rule) | C |
| 24 | Monte Carlo (u09 F-21, adopted; extended to four drivers in model v1.4, D-125) | Availability shock per operating year N(0, 2.0 points), truncated at -10/+5 points, independent across years; dispatch one draw per run, triangular (55.0, 76.5, 85.0)%; non-recoverable heat-rate degradation one draw per run, N(0.12%, 0.04%) a year, floored at 0; KCR depreciation (FX) drift one draw per run, N(5.19%, 3.0%) a year applied to the FC FX path; 1,000 runs; seed 20180717; debt locked at the FC base profile; Scenario 1 only | points; %; runs | 9.1 | P-F42 | B |
| 25 | First full operating year | FC base: 2021-07-01 to 2022-06-30; actual: calendar 2022 | dates | 4.15 | P-F10 | C |
| 26 | LLCR definition at close | PV of CFADS to final maturity at the all-in rate plus DSRA balance, over debt outstanding | – | 4.15 | P-F08 (the model computes `llcr_dsra`) | C |
| 27 | 2016 indicative pricing (P-F03) | 6M USD LIBOR July 2016 about 0.95 (approximate, fact-check before printing); margins commercial 4.50, ECA-covered 1.50, A-loan 3.90, B-loan 3.75; upfront commercial 2.50, ECA arrangement 1.25, ECA premium about 11.5 of principal; annualize fees straight line over 7.0 years | % ; years | 4.7 | P-F03 | B |
| 28 | Bid-stage screen (P-F60) | Project cost before financing 655.0; capacity charge 14.36 and fixed O&M charge 2.31 USD/kW-month at 588.4 MW; DSCR 1.35x; gearing 75%; repayment 13 years; SEKA revenue 2016 KCR 818 billion at 451.7 KCR/USD (2015: KCR 742 billion at 418.6) | USD m; USD/kW-month; x; years | 4.7, 4.5 | P-F60 | B |
| 29 | Bid comparison (P-F62) | Levelized tariff relative to winner: runner-up +4.6%, third +9.8%, fourth +13.1%; pricing committee capital charge 15.05 USD/kW-month (Kilnworth bid model 17.6% equity IRR) against 14.36 (16.0%) | % ; USD/kW-month | 4.7 | P-F62 (the IRRs are bid-model inputs, not reference-model outputs) | B |
| 30 | Sombé West reserve coverage (P-F61) | 2P 1,140 bcf; GCV 1,040 Btu/scf (38.75 MJ/Sm3); Bélanou 72,400 MMBtu/d for 22 years; SEKA existing contract 38,000 MMBtu/d for 2019 to 2038 | bcf; Btu/scf; MMBtu/d; years | 1.7.4 | P-F61 | B |
| 31 | Technology screening (P-F57) | Table in annex 4.12: overnight cost (USD/kW), heat rate (kJ/kWh LHV), fuel prices, fixed O&M (USD/kW-year), VOM (USD/MWh), life (years); discount rate 10.0%; capacity factors 10% to 90% | as stated | 4.12 | P-F57 | B |
| 32 | Halbeck RBL (P-F59, Illustrative) | Inputs in annex 4.13: 65% interest; capex USD 1.45 billion gross 2017 to 2019; plateau 150 MMscfd 2020 to 2032 then -8% a year; condensate 18 bbl/MMscf; gas price to SNHK 3.60 USD/MMBtu (2018) +2.0% a year; condensate Brent - 4 USD/bbl, deck Brent 60 (2017), 70 (2023); royalty 10% gas, 12.5% condensate; tax 35%; opex USD 85 million a year gross + 0.35 USD/MMBtu; RBL commitment 600, NPV10 of P50 / 1.30, P90 test at 1.00x | as stated | 4.13 | P-F59 | B |
| 33 | GCK revenue from Bélanou (P-F46) | Existing GTA inputs (reserved 96,500 MMBtu/d at 0.62 USD/MMBtu; commodity 0.19 USD/MMBtu; 1.5% a year from 2018) for 2022 actual volumes (with item 6) | USD/MMBtu | 1.8 | P-F46 | B |
| 34 | Heat-rate headroom (P-F47) | 6,323 (+0.10% a year allowance) against 6,261 guaranteed (plant degradation per JSON) and 6,286 tested | kJ/kWh | 4.1 | P-F47 | B |
| 35 | EPC progress (P-F52) | Planned: `epc_payment_pct_by_month_base`; actual: `epc_payment_pct_by_month_actual`; report quarterly cumulative percent and certified payments | % | 1.4 | P-F52 | B |
| 36 | Swap charge PV (P-F50) | 7.5 bps on the FC swap notional profile, discounted at the FC swap curve (2.872% flat); comparison at Castellan's 10 bps opening | bps | 1.15.2 | P-F50 | B |
| 37 | Equity cure amount (P-F63) | Shareholder loan injected at the June 30, 2023 test treated as CFADS for the 12-month historic test; report amounts to reach 1.10x and 1.20x | USD m | 1.15.11 | P-F63 | B |
| 38 | Funds flow at close (P-F49) | Items as listed in annex 8.2 with items 19 to 21 | USD m | 8.2 | P-F49 | B |
| 39 | IFRIC 12 presentation (P-F56) | Financial asset at amortized cost recognized over construction at cost (construction margin nil, because the EPC is subcontracted at arm's length), equal to capitalized cost on the lenders' basis at COD; the receivable stream is the capital charge component of the capacity charge at 100% availability on contracted capacity (the guaranteed, unconditional part); effective interest rate fixed at COD so that the PV of that stream equals the asset; fixed O&M, VOM and fuel are IFRS 15 revenue; availability shortfalls below 90% reduce service revenue, not the asset; report key balances 2021 to 2026 and the reconciliation of equity and profit to the lenders' basis | – | 4.6 | P-F56; P-F26 | A |
| 40 | ECL on SEKA receivables (P-F53) | Simplified approach; loss rates (after the Government Guarantee, treated as integral to the PPA): not overdue 0.2%; 1 to 90 days overdue 1.5%; 91 to 180 days 4.0%; over 180 days 10.0%; age the overdue balance first-in first-out from the arrears path in `events.offtaker_crisis` | % | 4.6 | P-F53 | B |
| 41 | Swap valuation curve points (P-F53) | Flat par swap rate for the remaining profile: 2018-07-17 2.872; 2022-12-31 4.05; 2023-06-30 4.35; 2025-06-30 3.68 (existing input); 2026-09-30 3.40 (approximate, fact-check before printing exact market levels) | % | 8.2 | P-F53, P-F26 | B |
| 42 | Retained 36% fair value (P-F26) | Price per percentage point of the 24% sale (P-F24) x 36, no control premium or discount; recycle the parent's share of the cash flow hedge reserve on loss of control | – | 8.3 | P-F26 | A |
| 43 | Pillar Two estimate (P-F54) | Kilnworth in scope; no Kessaran QDMTT through 2026; UK MTT top-up = max(0, 15% - jurisdictional ETR) x max(0, GloBE income - SBIE) x 60%, with GloBE income = IFRS profit before tax (IFRIC 12 basis, P-F56), covered taxes = current tax + minimum turnover tax; SBIE carve-out rates 2024: payroll 9.8%, tangible assets 7.8%; 2025: 9.6%, 7.6%; 2026: 9.4%, 7.4%; payroll = O&M fee labor share 60% of the fixed O&M fee plus project company staff costs 50% of G&A; tangible assets = carrying value of PP&E on the lenders' basis (flagged simplification); calendar years 2024 to 2026; label "estimate" | % | 4.15 | P-F54 | B |
| 44 | Castellan RAROC and capital (P-F55) | Holds: commercial 34%, ECA-covered 40%, standby (commercial share) 34% of 60%, swap 34% of notional; underwriting at mandate 100% of commercial and ECA-covered tranches; slotting risk weights (UK CRR): construction Satisfactory 115%, operations Good 90%, Weak 250% (June 2023 to June 2024); ECA-covered part: 95% substituted to an AA-or-better sovereign at 0%; ABDB 0%; PRI not recognized; capital 13.5% of RWA; funding premium 0.45% a year; PD 1.6% (construction), 0.9% (operations); LGD 35% (commercial), 5% (covered part); operating cost 0.15% of exposure a year; tax 19%; hurdle RAROC 12% after tax | as stated | 4.16, 5.6 | P-F55 | B |

## 2. Figure IDs and chapter mapping

Editor-assigned IDs (confirmed): P-F17 (Ch 44), P-F37 (Ch 31, 41, 67), P-F38 (Ch 41, 67), P-F39 (Ch 18, 59, 86), P-F40 (Ch 59), P-F41 (Ch 35), P-F42 (Ch 43), P-F43 (Ch 40), P-F44 (Ch 41), P-F45 (Ch 42).

New IDs from this annex:

| ID | Figure | Chapters | Inputs (section 1 #) |
|---|---|---|---|
| P-F46 | GTA charges 2022 and pass-through; GCK revenue from Bélanou | 21, 75 | 6, 33 |
| P-F47 | Heat-rate headroom as annual fuel margin OY1 and over time | 18, 48 | 34 |
| P-F48 | LTSA run-out date by dispatch case | 24, 28, 65 | 8, 9, 10 |
| P-F49 | Funds flow at financial close, July 17, 2018 | 55 | 19, 20, 21, 38 |
| P-F50 | PV of the swap credit and execution charge | 38, 56 | 36 |
| P-F51 | PRI insured amount and premium, 2018 to June 2025 | 27, 60 | 16 |
| P-F52 | Planned against actual EPC progress and certified payments, quarterly | 61 | 35 |
| P-F53 | ECL allowance on SEKA receivables; swap MTM and hedge reserve | 66 | 40, 41 |
| P-F54 | Estimated UK top-up tax on Kilnworth's share, 2024 to 2026 | 67 | 43 |
| P-F55 | Castellan holds, slotting, RWA, capital, RAROC | 68, 86 | 44 |
| P-F56 | IFRIC 12 presentation and reconciliation to the lenders' basis | 7 (note), 66 | 39 |
| P-F57 | Kessara 2015 technology screening curves | 69 | 31 |
| P-F58 | Actual 2022 dispatch and gas burn against 76.5% | 72 | 6 |
| P-F59 | Halbeck RBL borrowing base, 2017 and 2023 (Illustrative) | 75 | 32 |
| P-F60 | September 2016 bid-stage screen | 85 | 28 |
| P-F61 | Sombé West reserve coverage | 48 | 30 |
| P-F62 | Bid comparison table (extends P-F06) | 47 | 29 |
| P-F63 | Equity cure amount at June 30, 2023 | 62 | 37 |

Extensions of existing IDs (no new ID): P-F02, P-F03, P-F06, P-F07, P-F08, P-F10, P-F11 (split into P-F11a DSRA and P-F11b MMRA), P-F12, P-F16 (add Chapter 35), P-F25, P-F26, P-F28 (content defined in annex 8.3). Inputs: section 1 items 2, 4, 5, 13, 19 to 21, 25 to 27, 39, 42.

## 3. Reporting back

For each item, the modeler records in the model report: absorbed (with JSON key), absorbed with a different rule (state it), or declined (state why). For priority A items that change an existing ledger value (items 2, 6, 13, 19, 20, 39, 42), list the ledger IDs whose values change and the size of the change.
