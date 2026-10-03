# Build-along series: verification

Model version 1.5 (`model/build_excel_p.py`, `model/case_p.py`). Built by `model/build/build_stages.py`, verified by `model/build/verify_stages.py` (this file written by `write_verification_md.py`), 2026-10-03.

## Method

1. **Generation by filtering, not retyping.** `build_stages.py` runs the master build script (`build_excel_p.build`, Scenario 1) and cuts its output to each stage: it keeps the sheets and rows that the u09 Section 0.4 row map assigns to Chapters 39 up to the stage, deletes every other cell, and pastes the provisional rows. No formula is written by hand except the restated master check Checks F19 (the sum of the absolute values of the checks present).
2. **Row assignments.** u09 Section 0.4 (regenerated from v1.5) and Section 0.5, with the modeler's confirmed assignments (`case_p_report.md` 8c and 8d; v1.5 Debt rows 143 to 147 in Ch 40, 148 to 150 in Ch 42): Inputs row 226 stays in Chapter 39; provisional rows only in the Chapter 40 file (Construction row 38) and the Chapter 41 file (Debt rows 103, 104, 110 and 112; Waterfall rows 33 and 43); the Chapter 39, 42 and 43 files paste nothing.
3. **Provisional rows (D-051 (c)).** Values are the FC base (Scenario 1) values of the LibreOffice-recalculated master, pasted as numbers in input color (blue on pale yellow); each label carries the suffix "(provisional: pasted FC base values; replaced by formulas in Chapter N)"; the row-total formula in column G is kept.
4. **Recalculation.** LibreOffice 24.2 headless, private profile `-env:UserInstallation=file:///tmp/lo_profile_buildalong`, own output directory (`$BUILDALONG_WORK/recalc_out`). Masters for each scenario are rebuilt with the master script (v1.5) and recalculated in the same run.
5. **Comparisons.** (a) every built row with a Python-mirror counterpart (`build_excel_p.rowmap`, the same row list `verify_p.py` uses) against `case_p.run(case_p.scen(s))`, tolerance 0.01 (USD m, x, percentage points for IRRs); (b) every numeric cell of the stage against the recalculated master of the same scenario; (c) every check present and the restated master check; (d) a forward-reference scan (no formula refers to a sheet or row the stage does not contain); (e) cumulative containment (each file contains every cell of the previous one, except the cells the later chapter is meant to replace); (f) macro-free (.xlsx, no vbaProject part, iterative calculation off).
6. **Scenarios.** Files without provisional rows (Ch 39, 42, 43) are run in all fifteen scenarios; the Ch 40 and Ch 41 files hold Scenario 1 values in their provisional rows, so they reconcile on Scenario 1 only (u09 Section 0.1 item 4; their Covers say so).

## Results by stage

| Stage | File | Sheets | Formulas | Forward refs | Macro-free, no iteration | Scenarios run | Python rows compared (per run) | Largest difference vs Python | Numeric cells vs master (per run) | Largest difference vs master | Checks present (all 0) | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ch 39 | `Ch39_skeleton.xlsx` | 5 | 2,514 | 0 | yes | 1 to 15 | 4 | 0.0e+00 | 2,888 | 0.0e+00 | F19, F20, F21 | PASS |
| Ch 40 | `Ch40_funding.xlsx` | 8 | 7,435 | 0 | yes | 1 | 62 | 2.2e-11 | 8,854 | 0.0e+00 | F7, F8, F9, F16, F17, F19, F20, F21 | PASS |
| Ch 41 | `Ch41_operations.xlsx` | 10 | 13,070 | 0 | yes | 1 | 153 | 5.0e-08 | 15,105 | 9.9e-14 | F7, F8, F9, F15, F16, F17, F19, F20, F21 | PASS |
| Ch 42 | `Ch42_waterfall.xlsx` | 12 | 24,182 | 0 | yes | 1 to 15 | 303/304 | 5.2e-08 | 25,890 | 0.0e+00 | F7, F8, F9, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20, F21, F22, F23, F24 | PASS |
| Ch 43 | `Ch43_outputs.xlsx` | 15 | 25,284 | 0 | yes | 1 to 15 | 314/315 | 5.2e-08 | 61,251 | 0.0e+00 | F7, F8, F9, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20, F21, F22, F23, F24, F25 | PASS |

Sheets per stage: Ch 39: Cover, Inputs, Time, Construction, Checks; Ch 40: Cover, Inputs, Time, Construction, Operations, Funding, Debt, Checks; Ch 41: Cover, Inputs, Time, Construction, Operations, Tax, Funding, Debt, Waterfall, Checks; Ch 42: Cover, Inputs, Time, Construction, Operations, Tax, Funding, Debt, Reserves, Waterfall, Financials, Checks; Ch 43: Cover, Inputs, Time, Construction, Operations, Tax, Funding, Debt, Reserves, Waterfall, Financials, Ratios, Returns, Checks, Outputs.

Python rows compared rise from 4 (Ch 39: the Time sheet operating months and days rows) to 315 in Ch 43 (314 in Scenarios 14 and 15 and 303/304 in Ch 42, where one mirror item is not defined for the actual-history and re-forecast runs). No error value (#REF!, #VALUE!, #NAME? and so on) appears in any recalculated stage file.

### Chapter 39 calendar facts (u09 Section 0.5)

| Scenario | COD | PPA expiry | Construction months | COD period (months) | First debt-service period | Last funding month | Last operating period (months) | Operating months | Matches Section 0.5 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2021-05-01 | 2046-04-30 | 33 | 6 2021H1 (2) | 7 | 35 (2021-06) | 56 2046H1 (4) | 300 | yes |
| 8 | 2021-11-01 | 2046-10-31 | 39 | 7 2021H2 (2) | 8 | 41 (2021-12) | 57 2046H2 (4) | 300 | yes |
| 15 | 2021-12-01 | 2046-11-30 | 40 | 7 2021H2 (1) | 8 | 41 (2021-12) | 57 2046H2 (5) | 300 | yes |

Every scenario 1 to 15 of the Chapter 39 file: total operating months 300 (Checks F20 = 0), construction flags equal the construction months (Checks F21 = 0), master check 0.

### Ledger spot checks (Scenario 1, recalculated stage files)

| Cell | Ledger line | Ledger value | Ch 40 | Ch 41 | Ch 42 | Ch 43 | Match |
|---|---|---|---|---|---|---|---|
| Construction!G32 | P-F07 uses before financing | 710.99 | 710.9900 | 710.9900 | 710.9900 | 710.9900 | yes |
| Funding!G44 | P-F07 DSRA initial funding | 37.25 | 37.2459 | 37.2459 | 37.2459 | 37.2459 | yes |
| Funding!G48 | P-F07 ECA premium | 20.5 | 20.5049 | 20.5049 | 20.5049 | 20.5049 | yes |
| Funding!F75 | P-F07 total uses | 854.55 | 854.5519 | 854.5519 | 854.5519 | 854.5519 | yes |
| Funding!F25 | P-F07 senior debt total | 629.95 | 629.9497 | 629.9497 | 629.9497 | 629.9497 | yes |
| Funding!G57 | P-F07 debt ECA | 188.98 | 188.9849 | 188.9849 | 188.9849 | 188.9849 | yes |
| Funding!G58 | P-F07 debt A | 138.59 | 138.5889 | 138.5889 | 138.5889 | 138.5889 | yes |
| Funding!G59 | P-F07 debt B | 62.99 | 62.9950 | 62.9950 | 62.9950 | 62.9950 | yes |
| Funding!G60 | P-F07 debt COM | 239.38 | 239.3809 | 239.3809 | 239.3809 | 239.3809 | yes |
| Funding!G67 | P-F07 equity total | 224.6 | 224.6022 | 224.6022 | 224.6022 | 224.6022 | yes |
| Funding!G69 | P-F07 share capital | 44.92 | 44.9204 | 44.9204 | 44.9204 | 44.9204 | yes |
| Funding!G70 | P-F07 shareholder loans | 179.68 | 179.6818 | 179.6818 | 179.6818 | 179.6818 | yes |
| Funding!G71 | P-F07 SHL interest capitalized | 24.5 | 24.4966 | 24.4966 | 24.4966 | 24.4966 | yes |
| Funding!F24 | P-F43 closed-form total funding at the 75% cap | 857.4 | 857.4418 | 857.4418 | 857.4418 | 857.4418 | yes |
| Debt!F130 | P-F08 debt capacity at 1.35x | 629.9 |  |  | 629.9497 | 629.9497 | yes |
| Debt!F131 | P-F08 debt at the 75% gearing cap | 643.1 |  |  | 643.0814 | 643.0814 | yes |
| Outputs!F17 | P-F08 minimum DSCR (FC base) | 1.35 |  |  |  | 1.3500 | yes |
| Outputs!F21 | P-F16 equity IRR (%, x100) | 13.2 |  |  |  | 13.1519 | yes |
| Outputs!F23 | P-F16 equity NPV at 16.0% | -45.3 |  |  |  | -45.3092 | yes |

## Provisional rows (Scenario 1)

Pasted values in the earlier file against the formula values of the file that replaces them. Every total the replacement touches is unchanged.

| Row | Pasted in | Formula from | Largest difference, any column | Row total pasted | Row total with formulas |
|---|---|---|---|---|---|
| Construction 38 | Ch 40 | Ch 41 | 0 | 1.634867 | 1.634867 |
| Debt 103 | Ch 41 | Ch 42 | 0 | 0.000000 | 0.000000 |
| Debt 104 | Ch 41 | Ch 42 | 0 | 0.000000 | 0.000000 |
| Debt 110 | Ch 41 | Ch 42 | 0 | 0.000000 | 0.000000 |
| Debt 112 | Ch 41 | Ch 42 | 0 | 316.861636 | 316.861636 |
| Waterfall 33 | Ch 41 | Ch 42 | 0 |  |  |
| Waterfall 43 | Ch 41 | Ch 42 | 0 |  |  |

## Cumulative containment

| Step | Cells in the earlier file | Replaced as intended | Unexpected changes |
|---|---|---|---|
| 39 to 40 | 3,395 | 5 | 0 |
| 40 to 41 | 10,001 | 58 | 0 |
| 41 to 42 | 16,809 | 353 | 0 |
| 42 to 43 | 28,182 | 181 | 0 |

"Replaced as intended" covers the provisional rows (values and label suffix) when their chapter writes the formulas, the D-125 cells in Chapter 43, the restated master check F19 and the Cover stage note.

## Where the v1.4 and v1.5 changes land (D-125, D-128)

| Change | Cells | Stage file | Note |
|---|---|---|---|
| R1 timeline checks | Checks F20, F21 | Ch 39 | in the restated master check from Ch 39 |
| R2 master-check link | Cover row 22 | Ch 39 | see "Assignment conflicts" below |
| R10 pass-through tests | Operations rows 98, 99 | Ch 41 | |
| R4 cash flow statement and cash check | Financials rows 30 to 52; Checks F22 | Ch 42 | |
| R11 ECA tests | Debt rows 136 to 142; Inputs rows 1314 to 1320; Checks F23 | Ch 42 | |
| R12 MMRA-window check | Checks F24 | Ch 42 | |
| R5 Monte Carlo block | Inputs F311, F312, rows 313 to 1312 (draw table J:AL, pasted per-run results AN:AR), F1321; Cover row 29 | Ch 43 | 8c had listed F311, F312 and F1321 under Ch 39; under D-125 and the round-2 u09 Sections 0.4 and 0.5 they are Ch 43 rows (unreferenced before Ch 43) |
| R3 projected DSCR | Ratios rows 20, 21 | Ch 43 | |
| R6 fifteen-scenario table and compare row | Outputs rows 25 to 44; Checks F25 | Ch 43 | |
| Monte Carlo branches in existing cells | Time F16; Operations rows 31, 37, 39 (all 57 columns) | Ch 43 | Ch 39 to 42 files hold the pre-hook formulas and labels, read from the v1.3 workbook (git commit 8addab2, `book/model/Case_P_Model.xlsx`) |
| Run suspension of checks | Checks F8, F13, F14 | Ch 43 | pre-hook formulas (v1.3) and the F8 label in the Ch 40 to 42 files |
| Run suspension of the ECA-test check (v1.4 only) | Checks F23 | — | superseded in v1.5: F23 has no Monte Carlo condition and applies in every scenario |
| Run suspension of the Outputs compare row | Outputs F44 | Ch 43 | born with the condition (Outputs is a Ch 43 sheet) |
| Master check extended | Checks F19 | each stage | restated over the checks present; equal to the master formula in Ch 43 |

| v1.5 ECA equal-installment profile (D-128) | Debt rows 143 to 147 (block header 144; rows 145 to 147 installment share, remaining profile, share of remaining balance) | Ch 40 | read by Funding F12 (Ch 40) and by Debt rows 24 and 119 (Ch 42) |
| v1.5 sculpting helpers (D-128) | Debt rows 148 to 150 (swap cost per USD of scheduled balance, ECA debt service in the sculpting, its PV) | Ch 42 | read by the live sculpting block |
| v1.5 formulas changed in place | Debt row 24 (ECA scheduled principal), row 119 (ECA next-period debt service), rows 127 to 135 (live sculpting), rows 137 to 142 (ECA tests on the ECA schedule); Funding F12 (ECA DSRA coefficient) | Ch 42 (Debt), Ch 40 (Funding F12) | carried as built in v1.5; no stage holds a v1.4 form |
| v1.5 Checks F23 | applies in every scenario; no Monte Carlo condition | Ch 42 | identical in Ch 42 and Ch 43 (the D-125 Ch 42 edit of v1.4 no longer applies) |

With Inputs F311 = 0 every Monte Carlo branch is inert, so the Ch 43 file reproduces the Ch 42 values cell for cell (largest difference 0 in all fifteen scenarios against the v1.5 master, which itself was verified against the mirror with runs 1, 500 and 1,000 in `case_p_verification.md`).

## Ch43_outputs.xlsx against Case_P_Model.xlsx

Compared cell by cell with the committed `model/Case_P_Model.xlsx`: sheet order identical; defined names identical (`Scenario` only); 64,874 non-empty cells compared for content (formula text or constant).

| Kind | Cells that differ | Where | Intended |
|---|---|---|---|
| Content (formulas and constants) | 5 | Cover!D31, Cover!D32, Cover!D33, Cover!D34, Cover!D35 | yes: the R7 stage note (rows 31 to 35, empty in the master) |
| Style (font color, fill, number format) | 1 | Cover!D31 | yes: bold first line of the stage note |
| Recalculated values (Scenario 1) | 5 text cells; numeric max difference 0.0 over 64,874 cells | the same five note cells | yes |

No other intentional difference exists: every formula, input, label, unit, number format, conditional format range and the scenario name equal the master.

## Assignment conflicts and decisions

- **Cover row 22 (master-check link).** u09 R2 ("39 (link), 43 (complete)"), the Chapter 39 installment (39.J step 5, "Cover link (R2)") and `case_p_report.md` 8c put the link in Chapter 39; the round-2 Sections 0.3 to 0.5 list it under Chapter 43. The link is in the Ch 39 file (its formula is final from Chapter 39; the master check it shows is completed check by check through Chapter 43). If the editor prefers the Section 0.4 reading, the change is to delete Cover D22:F22 from the Ch 39 to Ch 42 files in `build_stages.py` (`COVER` map).
- **Inputs F311, F312, F1321.** Chapter 43 (D-125; round-2 Section 0.4), not Chapter 39 as 8c had it.
- **Data validation on the scenario selector** (39.J step 2 mentions "data validation 1 to 15"): not added, because the master workbook has none and Ch 43 must equal it.

## Reproduce

```
cd model/build
python3 build_stages.py            # five files, from build_excel_p.py (v1.5)
python3 verify_stages.py           # 63 LibreOffice recalculations, comparisons, verify_results.json
python3 write_verification_md.py   # this file
```
