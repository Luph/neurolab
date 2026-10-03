# Model and ledger requests from the round 1 brief revisions

Compiled October 3, 2026 by the consolidation editor (part B) from the "Revision log (round 1)" and "Central changes needed" sections of `bible/briefs/u01.md` to `u17.md`, the briefs' open-request sections they point to (u09 Section 0.7, u12 "Figure requests", u17 89-6a and 90-5), and `reviews/blueprint/central-fixes-log.md` Section 10. Owners: **Case P modeler**, **Case T modeler**, **Case R modeler**, **build agent** (build-along series and exercise workbooks), **Phase 6** (capstone and examination modeling agent under standards Section 11 Phase 6).

Rules that apply to every item:

1. Appended rows only: no request may move an existing workbook address (u09 Section 0.1; D-047 keeps the calendar rows where they are).
2. Every supplied workbook is macro-free (D-113, u09 Section 0.6, u17 fm:model-builds). Optional VBA is the reader's own (ssec:13.8.5).
3. New ledger values go into the existing ID as an extension unless a new ID is listed here; the editor-in-chief assigns any new ID (D-013).
4. Until an item is delivered, chapters use the fallback named in the "Fallback" column and print nothing that depends on it.
5. Status (updated in round 2, October 3, 2026, against model version 1.4, D-124 and D-125): the "Status" column of each table governs. "Delivered (v1.4)" means the item is in `model/Case_P_Model.xlsx` version 1.4 or its ledger and chapters use it, not the fallback. "In progress" means the owner is building it; files may already be present (for example draft build-along files in `model/build/` and `model/exercises/ex43_17/ex43_17_mirror.py`), but chapters keep the fallback until the editor marks the item delivered. "Open" means not started. Nothing in `model/capstone/` or `model/exam/` exists yet (Phase 6).

## 1. Case P workbook and build-along series (u09 Section 0.7)

| ID | Request | Owner | Stage (chapter) | Fallback until delivered | Status |
|---|---|---|---|---|---|
| u09-R1 | Checks rows 20 and 21: operating months sum to the PPA term; construction flags sum to construction months; both in the master check F19 | Case P modeler (companion), build agent (build files) | 39 | Ch 39 describes the checks and computes them by hand on Exhibit 39.5 | Delivered (v1.4): Checks rows 20 and 21, in F19 |
| u09-R2 | Cover row 22: master-check link to Checks F19, red fill when not 0 | Case P modeler, build agent | 39, 43 | Text points to Checks F19 | Delivered (v1.4): Cover row 22 |
| u09-R3 | Ratios rows 20 and 21: projected 12-month DSCR on the next two periods (report only) and a below-1.20x flag | Case P modeler, build agent | 43 | Text uses `model/case_p_report.md` Section 7 | Delivered (v1.4): Ratios rows 20 and 21 |
| u09-R4 | Financials rows 31 onward: cash flow statement and cash check, linked to Checks row 22 | Case P modeler, build agent | 42 | ssec:42.6.3 fallback (statement built by the reader) | Delivered (v1.4): Financials rows 31 to 52; Checks row 22 |
| u09-R5 | Monte Carlo block: Inputs F311 run selector, draw table from row 313 (1,000 runs, seed 20180717, P-F42 parameters), Operations rows 32 and 37 hooks, one-variable data table over runs; if a native data table cannot be generated and verified, paste the mirror's per-run results with a stamp and say so on the Cover | Case P modeler, build agent | 43 | ssec:43.5.2 fallback (pasted results) | Delivered (v1.4), four drivers (D-125): Inputs F311, F312, rows 313 to 1312 (draws J to AL; pasted per-run results AN to AR), F1321; branches in Time F16 and Operations rows 31, 37 and 39 (not rows 32 and 37); no native data table (Cover row 29) |
| u09-R6 | Outputs rows 24 onward: the fifteen-scenario results table (case_p_report.md Section 1) pasted with version and run date, plus a check row against the live dashboard | Case P modeler, build agent | 43 | Text reproduces rows by switching Inputs F8 | Delivered (v1.4): Outputs rows 26 to 44; Checks row 25 |
| u09-R7 | Cover of each build-along file: stage, provisional rows held, scenarios that reconcile | Build agent | all | – | In progress (build agent) |
| u09-R8 | Exercise files: `model/exercises/ch39_sponsor_solar_layout.xlsx` (220 MW solar sponsor model with the seeded layout defects of Exhibit 39.4; Walkthrough 39.8, Exercises 39.13 and 44.13); `model/exercises/ex43_17/` (solution workbook and Python mirror reproducing the Exercise 43.17 answers stated in u09); reader copy of `Case_P_Model_AuditExercise.xlsx` without the AuditKey sheet (Chapter 44) | Build agent (with Case P modeler for the audit copy) | 39, 43, 44 | Exercises print their inputs in full; no solution file is cited | Partly delivered: audit reader copy delivered (`model/exercises/Case_P_Model_AuditExercise_reader.xlsx`); `ex43_17/` in progress (mirror present, solution workbook not yet); `ch39_sponsor_solar_layout.xlsx` and the Exercise 43.14 files (`ex43_14/Ch43_start_no_mc.xlsx`, `ex43_14/ch43_draw_table.xlsx`; added in round 2) open |
| u09-R9 | Ledger extensions: P-F16 debt capacity at 1.35x (Debt F130) under each of the ten sensitivities (Exercise 43.13); P-F17 annual shadow sizing of the FC base (annual CFADS, FC all-in rate, 1.35x) and its difference from USD 633.3 million (Exercise 44.12) | Case P modeler | 43, 44 | Exercises 43.13 and 44.12 state that the answer is in the ledger and are not printed until it is | Delivered (v1.4 ledger): P-F16 debt capacity at 1.35x by sensitivity; P-F17 annual shadow sizing |
| u09-R10 | Operations rows 98 and 99: fuel pass-through test (equals the P-F47 headroom margin) and GTA pass-through test (0 every period) | Case P modeler, build agent | 41 | Text computes one period by hand | Delivered (v1.4): Operations rows 98 and 99 |
| u09-R11 | Debt rows 137 to 142: ECA tests on the selected profile (WAL from COD, largest installment, repayment term, months to first repayment, share repaid by 24 months), each with its limit as an input and a check linked to Checks row 23 (values as P-F09; the 24-month rule per Annex P 3.6) | Case P modeler, build agent | 42 | P-F09 printed values | Delivered (v1.4): Debt rows 137 to 142; Inputs rows 1314 to 1320; Checks row 23 |
| u09-R12 | Checks row 24: MMRA window equals the input number of periods | Case P modeler, build agent | 42 | – | Delivered (v1.4): Checks row 24 |
| u09-BA | Build-along series `model/build/Ch39_skeleton.xlsx`, `Ch40_*.xlsx`, `Ch41_operations.xlsx`, `Ch42_waterfall.xlsx`, `Ch43_outputs.xlsx`, cumulative, with labeled provisional rows (Construction row 38 in Ch40; Waterfall rows 33 and 43 and Debt rows 103, 104, 110 and 112 in Ch41) and the reconciliation targets of u09 Section 0.5; confirmation that the Chapter 40 and 41 provisional rows reconcile on Scenario 1 | Build agent; confirmation by Case P modeler | 39 to 43 | Chapters cite `Case_P_Model.xlsx` rows (u09 Section 0.4) | In progress (build agent): draft files `Ch39_skeleton.xlsx` to `Ch43_outputs.xlsx` and `build_stages.py`, `verify_stages.py` are present in `model/build/` but not yet verified against u09 Section 0.5 or released |
| u09-REG | If any request adds rows that shift addresses (it must not), regenerate the u09 Section 0.4 row map mechanically and report the shifts | Build agent | 39 to 45 | – | Done in round 2: v1.4 moved no address; Section 0.4 regenerated for the changed cells and appended rows |

## 2. Case P ledger extensions and corrections

| ID | Request | Requested by | Owner | Fallback | Status |
|---|---|---|---|---|---|
| P-F16 / P-F17 | Extensions in u09-R9 above | u09 | Case P modeler | As above | Delivered (v1.4 ledger) |
| P-F49 | Itemize every use in "total uses month 1" (USD 121.59 million) so that Exhibit 55.10 reconciles without a computed residual. The ledger lines now visible sum to USD 115.45 million on the gross EPC advance (57.18 + upfront fees 9.95 + first ECA premium 2.93 + advisers 6.28 + insurance 6.48 + development cost reimbursement 21.43 + development fee 11.20), leaving USD 6.14 million unitemized; sources are first utilization 90.05 plus equity 31.54 = 121.59 | u11 (central change 16) | Case P modeler | Exhibit 55.10 prints the ledger lines and the total and labels the difference "other closing-day uses (ledger)" only if the modeler confirms it; otherwise the exhibit waits | Delivered (v1.4 ledger): itemized lines sum to 121.59 |
| P-F63 | Add the pro rata prepayment cure for June 30, 2023 (amount of prepayment that restores 1.10x and 1.20x), alongside the equity cure amounts 11.0 and 18.7, for Exercise 51.16 | u11 (central change 17, optional) | Case P modeler | Exercise 51.16 answers the equity-cure form only | Delivered (v1.4 ledger): pro rata and proportional prepayment cures |
| P-F40 | Netting set-offs actually made under the June 29, 2023 agreement, by month (July 2023 to March 2024), for Example 59.8. The ledger now gives only the average per month by half-year (5.44 in 2023 H2, 4.96 in 2024 H1) | u12 (figure request) | Case P modeler | Example 59.8 prints the half-yearly deferred payables (P-F20) and the peak matched arrears (P-F40) only | Delivered (v1.4 ledger): monthly set-offs July 2023 to June 2025, each half-year's fall spread evenly (5.44 a month in 2023H2, 4.96 in 2024H1, 2.97 in 2024H2, 1.64 in 2025H1; total 90.08, all within the USD 9.0 million monthly cap) |
| P-F02 | Option A: compute the January 2022 invoice's reconversion at the Central Bank mid rate on the invoice date (Annex P 1.1.5). Option B (adopted for now; Annex P 1.1.5 and P-C54): keep the 2022 H1 average as the model's proxy and keep the ledger label "2022H1 average" | u02 (C-8) | Case P modeler | Chapter 5 prints the ledger label and says it is a proxy | Option B adopted (P-C54); ledger label carries "illustrative path" |
| P-F02, P-F03, P-F22 labels | Add "illustrative path (D-046)" to the US CPI, LIBOR and Term SOFR rows and "approximate" to the July 2016 LIBOR and the Term SOFR inputs; no rerun (D-046) | u02 (C-9) | Case P modeler | Chapters label the values "Case P index (illustrative)" | Delivered (v1.4 ledger) |
| P-F65 | Label the profile rows "every sixth month shown" (the ledger prints `schedule[::6]`, so the listed rows do not sum to the KCR 32,204 million total), or print the full monthly profile; state whether the forward schedule follows the FC payment schedule (33 months) or the actual one (the listed months run to 2021-08, past the FC schedule's end) and reconcile the "Contract (FC)" scenario label | Consolidation editor (Case Bible 1.6 correction, P-C52) | Case P modeler | Chapters print the totals only (share hedged, KCR notional, USD at forward, average forward) | Delivered (v1.4 ledger): all 40 monthly forwards, August 2018 to November 2021, and the totals (P-C61) |
| P-F26 | Optional fair-value line for the USD 4.0 million deferred consideration (the model measures it at nil at completion; Annex P 8.3 now records that the 77.3 consideration excludes it and that the 2.1 hedge-reserve recycling sits outside the 82.0 loss) | u14 | Case P modeler | Example 66.9 states the nil measurement | Delivered (v1.4 ledger): deferred consideration face 4.0, fair value nil |
| case-state P row 62 | Correct `model/case-state-case-p.md` row 62 from 1.14x and 0.97x to the ledger's P-F21 values 1.13x (December 31, 2022) and 0.96x (June 30, 2023) | u13 (central change 11) | Case P modeler | Case Bible 1.9 and P-C57 record that the ledger governs | Delivered: row 62 reads 1.13x and 0.96x |
| P-F55 / RORAC | Relabel any remaining "RORAC" in `bible/case-p-input-requests.md` (2 occurrences) to RAROC (R-075). The ledger and `case_p.py` are already clean | u17 (central change 3); central-fixes-log Section 10 | Case P modeler (file owner) | D-043 reads RORAC as RAROC | Delivered: no RORAC remains in `bible/case-p-input-requests.md` |
| Input workbooks | `model/inputs_case_p.xlsx` (and T, R below): one sheet per Case Bible block, each value with its JSON key and unit, so no reader reads JSON (u17 fm:model-builds; capabilities review defect 14) | u17, u09 | Case P modeler | Chapters print input exhibits (39.5, 40.7, 41.8) | Delivered for Case P (`model/inputs_case_p.xlsx`); T and R in Section 3 |

## 3. Case T and Case R

| ID | Request | Requested by | Owner | Fallback | Status |
|---|---|---|---|---|---|
| T-F01 extension | Breakeven reduction in the PSC's "toll revenue retained by the state" (PV 2012, ARD m and percent) at which the reference VfM reaches zero, and the same for the winning bid (sec:57.10, Exercise 57.12) | u12 (figure request; central change 4) | Case T modeler | Chapter 57 compares the two T-F01 lines without computing a new number | Open |
| T-F10 note | No rerun: the Case Bible now treats 1.30x as the plan floor and prints the ledger's 2.00x minimum notes DSCR and 2.65x divisor (T-C25). Confirm in the Case T report that no covenant or sweep depends on a 1.30x sculpting target | Consolidation editor (u13 central change 9) | Case T modeler | – | Open |
| Inputs workbook T | `model/inputs_case_t.xlsx` as for Case P | u17 | Case T modeler | Input exhibits in chapters | Open |
| Exercise 79.11 | Confirm the ledger values Exercise 79.11 uses (T-F04, T-F06, T-F18, T-F19) are final in the v1.1 ledger | u16 (not fixed list) | Case T modeler | Answers printed from the ledger | Open |
| Inputs workbook R | `model/inputs_case_r.xlsx` as for Case P | u17 | Case R modeler | Input exhibits in chapters | Open |

## 4. Exercise workbooks outside the Case P build

| File | Exercise | Requested by | Owner | Fallback | Status |
|---|---|---|---|---|---|
| `model/exercises/ch13/Ch13_Practice_Solution.xlsx` | Exercise 13.12 and Section 13.10 (Quebracho Alto practice workbook, macro-free; circularity by closed form plus unrolled iteration rows) | u03 (central change 3) | Build agent | Exercise prints inputs and expected values | Open |
| `model/exercises/ch13/Ch13_Inherited_Sheet.xlsx` | Exercise 13.13 (the seeded inherited sheet exactly as specified in u03) | u03 | Build agent | Sheet printed in the exercise | Open |
| `model/exercises/ch13/Ch13_LlanoPardo_Solution.xlsx` | Exercise 13.15 (rebuild of the Chapter 1 Llano Pardo projection, k = 1.38074, reproducing u01 Section 1.A.7) | u03, u01 (central change 3) | Build agent | Exercise prints inputs and expected outputs | Open |
| `model/exercises/ex85_12/ex85_12_solution.xlsx` | Exercise 85.12 (one-tab screening sheet for Equations 85.1 and 85.2) | u17 (Open requests 2; central change 7) | Build agent | Exercise prints answers | Open |
| `model/exercises/ex86_13/` | Exercise 86.13 (tornado chart from Example 86.3's sensitivities) | u17 | Build agent | Exercise prints the ordered bars | Open |
| `model/exercises/ch39_sponsor_solar_layout.xlsx`, `ex43_17/`, audit reader copy | See u09-R8 | u09 | Build agent | As above | See u09-R8 |
| Front-matter listing | `fm:model-builds` lists the five build-along files, the audit reader copy, every `model/exercises/` file and the file each Tier 3 task starts from; Phase 6 confirms the files exist before writing it | u09 (central change 6), u17 | Phase 6 | – | Open (Phase 6) |

## 5. Capstone and examination (Phase 6)

| Item | Specification | Owner |
|---|---|---|
| Capstone mini-Bible | `bible/capstone-bible.md` before any modeling: setting, parties and names (Case Bible Part 5 check, capstone register), contracts, stage events with relative dates (Year 0 to Year 8), every u17 89-3 input restated (u17 89-6a item 1) | Phase 6 |
| Capstone inputs | `model/capstone/inputs_capstone.json` and reader-facing `inputs_capstone.xlsx` (89-6a item 2) | Phase 6 |
| Capstone reference model | `model/capstone/capstone.py` (mirror, source of truth), `Capstone_Model.xlsx` (macro-free), `verify_capstone.py` (89-6a item 3) | Phase 6 |
| Capstone starting and seeded files | `Capstone_Start.xlsx` (inputs and empty labeled sheets); `Capstone_SponsorModel_Seeded.xlsx` with three seeded errors (timing flag, reserve-release sign, hardcoded indexation factor) for Task 4(b) (89-6a item 4) | Phase 6 |
| Capstone ledger | `model/capstone/figure-ledger-capstone.md`, IDs C-F01 to C-F24 as fixed in 89-6a item 5 (D-034) | Phase 6 |
| Examination files | `model/exam/`: Paper 4A take-home model build (60.4 MW geothermal plant, Taupō Volcanic Zone, Kahurangi Geothermal Ltd, NZD, 2027 close; scope as stated in u17 90-5) with a reference solution and mirror; Paper 4B audit workbook with eight seeded errors (D-034) and its key | Phase 6 |
| Name checks | Capstone and examination names entered in Case Bible Part 5A (Kahurangi Geothermal Ltd already listed as unchecked) | Phase 6 |

## 6. Items closed without a model change

- D-047: calendar rows stay where the workbook has them; R-021 and style sheet A.6 amended (u09 central change 1).
- D-046: US macro paths stay as stylized illustrative paths; no rerun (u02 C-9).
- P-F23 combined DSCR, T-F10 notes DSCR, P-F21 ratios, P-F39/P-F40 LC values, Annex P 3.1 gross arrears (USD 149.2 million = P-F20 112.6 + P-F40 36.6): resolved in the Case Bible in the ledger's favor (Case Bible Part 8, P-C51, P-C57, T-C25; Annex P 3.1).
