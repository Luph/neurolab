# Case T and Case R: input requests to the modelers

Version 1.0, October 3, 2026. Source: `bible/case-bible-annex-tr.md` (the annex governs where it differs from `case-bible.md`). The Case Bible editor has not edited any model file or inputs JSON; each modeler adds the inputs below to its own JSON, reruns, and records the new figures in its ledger. Every Case R price stays Illustrative.

Status of coordination: Case R model R-1.1 is complete; the items below need a rerun (R-1.2). Case T model 1.0 has an empty "Assumption changes" section in its report; the annex adopts the Case T modeler's own `modeler_assumptions` (PSC recalibration, plan valuation, state money allocation, plan classes and votes, handback estimate), so those need no action beyond logging them in the report.

## 1. Case T (`model/inputs_case_t.json`)

| # | Input | Value | Unit | Annex | Target figure | Model use |
|---|---|---|---|---|---|---|
| T-IR-01 | Performance payments to BRTA, actual history | 2019H1 0.14; 2019H2 0.24; 2020H1 0.03; 2020H2 0.00; 2021H1 0.00; 2021H2 0.02; 2022H1 0.05; 2022H2 0.06; 2023H1 0.04; 2023H2 0.05; 2024H1 0.08; 2024H2 0.09; 2025H1 0.03; 2025H2 0.04 | ARD m nominal, by half-year | T.1 | T-F13; flows into T-F07, T-F09, T-F10 | Operating cost in the half incurred (actual-history run only); tax-deductible; nil in bid, banking, downside runs |
| T-IR-02 | Performance payment cap (check only) | 2.5% of previous calendar year's net toll revenue | % | T.1 | T-F13 | Verify no half-year exceeds the cap; report |
| T-IR-03 | Relief period (performance payments suspended) | 2020-03-23 to 2021-09-30 | dates | T.1 | T-F13 | Documentation; amounts in T-IR-01 already reflect it |
| T-IR-04 | Traffic ratios | None (computed from existing traffic inputs) | ratio | T.17 | T-F11 | Actual / Pellow, actual / Ridgeway banking, actual / downside, annual 2019 to 2026; actual / Ridgeway 2023 case from 2024 |
| T-IR-05 | Shortfall shares by cause | 2019: housing 41, VoT 29, trucks 20, SR 14 works 10, COVID 0. 2020: 23, 16, 11, 5, 45. 2021: 29, 20, 14, 7, 30. 2022: 36, 25, 18, 9, 12 | % of (Pellow less actual), annual average k trips/day | T.17 | T-F12 | Shares times each year's shortfall; report k trips/day and %; optionally revenue equivalent |
| T-IR-06 | Pellow VoT variants (optional) | Mature 2019 level: low 51.2; central 54.6 (high 58.4 = existing sponsor base); ramp-up and growth as sponsor base | k trips/day | T.3 | T-F14 | Two extra bid runs with financing locked; report equity IRR at ARD 287.4m and NPV at 11.4% |
| T-IR-07 | VfM presentation | Gross PSC cost = raw capex + O&M and lifecycle + all risk adjustments (before netting retained toll revenue) | ARD m PV 2012 | T.9 | T-F01 (extended) | Report VfM (reference and winning bid) as % of gross PSC cost and as % of net PSC |
| T-IR-08 | Contribution gaps | Reference 410.0, Northgate 361.0, winner 287.4 | ARD m nominal | T.2 | T-F02 (extended) | Report gaps (122.6; 73.6; 49.0) and percentages (29.9%; 20.4%; 12.0%) for the ledger |
| T-IR-09 | Plan allocation reporting | None new (uses existing plan valuation) | ARD m; ARD m per 1% | T.10, T.11 | T-F09 (extended) | Ensure ledger rows for plan equity value, state subscription at plan value, implied capital grant, prices per percentage point (state, creditor conversion, creditor give-up), recovery by class |
| T-IR-10 | Northgate traffic basis (book input; no run required) | Mature 2019 53.9; ramp 0.76, 0.88, 0.95, 0.99, 1.00; growth 3.0% / 2.1% / 1.1% | k trips/day; factors; % a year | T.2 | None (optional comparison row in T-F04) | Only if the modeler adds Northgate as a traffic comparison line; no financing run |

No Case T input changes the financing at close (T-F03) or the bid returns (T-F02 core rows). T-IR-01 changes the actual-history CFADS by at most ARD 0.24m in a half-year; the modeler reports the effect on T-F07 to T-F10 and flags any change at the displayed precision.

## 2. Case R (`model/inputs_case_r.json`)

| # | Input | Value | Unit | Annex | Target figure | Model use |
|---|---|---|---|---|---|---|
| R-IR-01 | Initial overbuild at COD, R6 and R7 | 8% of nameplate energy (R6 216 MWh; R7 324 MWh usable at COD) | % of nameplate MWh | R.5 | R-F19 | Starting usable energy |
| R-IR-02 | Capacity fade, R6 and R7 (and each augmentation tranche from its own installation) | Year 1: 2.0; years 2 to 10: 1.5 a year; year 11 on: 1.0 a year | percentage points of beginning-of-life usable energy per year, linear | R.5 | R-F19 | Usable energy path; mid-year or annual convention to be stated by the modeler |
| R-IR-03 | Augmentation (unchanged inputs, confirm) | 6% of nameplate MWh in calendar years COD+5 and COD+9; USD 41/kWh in 2025 prices, +2.5% a year | % ; USD/kWh | R.5 | R-F19 | Already modeled; add the MWh to usable energy |
| R-IR-04 | Revenue scaling rule | Merchant revenue and R7 floor reference revenue scale by min(1, usable MWh / nameplate MWh) | ratio | R.5 | R-F19; affects R-F02, R-F04 (no: A1 has no batteries), R-F07, R-F08, R-F09, R-F13 | Apply in base, low, high and volume cases |
| R-IR-05 | R6 toll condition | Toll paid in full while usable energy at least 200 MWh and availability at least 97.0% | MWh; % | R.5 | R-F19 check | Check; report any year the condition fails (the annex arithmetic says none through July 2030) |
| R-IR-06 | R7 floor settlement reporting | No new value: reference revenue = battery revenue index x availability (existing rule) | USD/kW-year; USD m | R.4 | R-F18 | Report by contract year 2024 to 2032 (pro rata first and last years): reference revenue, floor payment from Galloway, premium, upside share, net; base, low, high |
| R-IR-07 | Materiality report | Threshold USD 1.0 million | USD m | R.5 | R-F07 | If the fade moves the A2 or A3 base-case breakeven below the D-014 price by more than the threshold, report to the editor-in-chief; prices stay |
| R-IR-08 | Terminal value rule (confirmation only) | 10.50% post-2040 tail rate applied from the valuation date; no TV beyond useful life; no post-2040 levered rate | % | R.7 | R-F04, R-F07, R-F09 | No change to R-1.1; record the wording in the ledger header |

Book inputs that need no model absorption (listed so no one hunts for them in the JSON):

- Case T: KPI rates and thresholds (T.1); bid security, evaluation weights and committed-finance terms (T.2); Pellow VoT values in ARD per vehicle-hour and the revealed-preference value (T.3); D&C cap, interface liability cap, Quillfield prices, LDs and test thresholds, the ARD 3.42m recovery (T.4); tunnel parameters and the JV's ARD 26m loss (T.6); SR 14 counts (T.7); handback requirements (T.8; the ARD 42.6m estimate is already a modeler input); class vote percentages and judgment date (T.10); bond ratings (T.15); light-rail and hospital facts (T.13, T.14).
- Case R: A1 dates, headline price USD 436.0m, ticker 5.00% and USD 10.3m (total consideration unchanged at USD 446.3m), W&I retention and premium (premium already inside the USD 14.9m costs), escrow, competing bids (R.1); Ostrander profile, collateral thresholds and LC (R.2; LC fees ignored); Marlowe Gulf Hydrogen terms (R.3); green framework and SPO (R.6; costs inside 1.10%); Ketterman offer and repowering parameters (R.8; Chapter 88 shows no figures).

## 3. New figure IDs

T-F11, T-F12, T-F13, T-F14 (optional); extensions to T-F01, T-F02, T-F09. R-F18, R-F19. The IDs R-F11 to R-F17 stay as the Case R modeler assigned them; the briefs' proposed "R-F11" contents are now R-F18 (R7 floor) and R-F19 (battery capacity), and the briefs' proposed "T-F11" contents are T-F11 (ratios, u16) and T-F12 (decomposition, u09).
