# Blueprint review round 2: capabilities lens

Reviewer: fresh round 2 reviewer, capabilities lens (standards Section 3; novice path). Date: October 3, 2026.

Files read: blueprint-review-instructions.md and blueprint-review-r2-instructions.md; round 1 report `reviews/blueprint/capabilities.md`; decisions.md (D-015 to D-055, D-114 to D-123); capability-map.md; model-requests-round1.md; u09 Section 0 (all), 39.J to 39.M, 40.C and 40.M, 42.C and 42.M, 43.B to 43.Q, revision log; u17 00-3 (FM.1, FM.3, fm:model-builds), 85-13, 86-13, 89-6, 90-3 and 90-5, 93-2, revision log; u01 1.13 and log; u02 Ch 5 (ssec:5.2.2, Walkthrough 1); u03 13.8.5 and 13.M; u07 Ch 32 assumed lists; u08 36.13 to 36.19 and Ch 38 assumed lists; u10 47.11, 48.9 to 48.13, 49.17, 50.16; u11 56.17 and Exhibit 56.6 references; u13 61.15, 62.14, 62.16, 64.19, 64.20; glossary-canon.md (tax and spreadsheet entries); anchor-registry.md (every new exhibit, exercise and subsection label cited below); case-bible.md Part 6 rows 39 and 43; `model/Case_P_Model.xlsx` (read with openpyxl), `model/case_p_report.md`, `model/case-state-case-p.md`, `model/figure-ledger-case-p.md` (P-F16, P-F42, P-F43, P-F65).

Method notes. (1) The u09 row map (Section 0.4) was compared mechanically with the delivered workbook: 488 rows checked for label and first-column formula. (2) Per the task note, the build-along workbooks (`model/build/Ch39_skeleton.xlsx` to `Ch43_outputs.xlsx`) and the exercise workbooks (`model/exercises/ch39_sponsor_solar_layout.xlsx`, `ex43_17/`, `ch13/`, `ex85_12/`, `ex86_13/`) and `inputs_case_t.xlsx`/`inputs_case_r.xlsx` are not yet built. They are judged on their specification (u09 Sections 0.1, 0.5, 0.7; D-051; D-121; model-requests-round1.md) and listed below as dependencies, not defects, where the specification is complete. (3) Arithmetic re-checked: FM.3 (24 + 54 + 240 + 85 + 64 + 22 + 107 + 46 = 642), the 89-6 task budgets (107), the 90-3 paper table (34 hours, 68 questions, 576 marks), FM.1 examination allocation (68), Exercise 43.17 identities (hard costs 252.600; gearing 67.9%; equity 87.746; upfront fee 3.245), Exercises 1.11 and 39.6.

## Verdict: FAIL

All 17 round 1 defects are fixed in the blueprint, the blocking defect included. One new major defect blocks a PASS. The Case P model moved to version 1.4 after u09 was revised, and the version 1.4 Monte Carlo has four stochastic drivers, while u09 still specifies two. A reader or build agent working from u09 cannot reproduce P-F42 (new defect 1). There are also 5 new minor defects.

## Round 1 defects: status

| # | Round 1 defect (severity) | Status | Where verified |
|---|---|---|---|
| 1 | Part VII build cannot be followed or reconciled to the companion (blocking) | FIXED (specification); files are a dependency | u09 0.1 to 0.9 rewritten. The row map in 0.4 was generated from the workbook, and 481 of 488 rows match version 1.4 exactly. The 7 that differ are the version 1.4 Monte Carlo edits (new defect 1). Build-along series, cumulative and macro-free: 0.1 item 3, 0.5, D-051(a, b), D-121, model-requests u09-BA. Provisional-row convention closes the Ch 40 DSRA loop: Funding rows 11 to 17 read Debt rows 7 to 19 and Operations rows 7 to 15, now assigned to Ch 40 (0.3, 0.5), with Construction row 38 provisional (D-051(c)). Macros removed from the companion and from every exercise (0.6; 40.10 and 42.12 are optional; 43.10 and 43.14 have no VBA). The two-timeline design with the band-overlap rule is the book's model, and the mixed timeline is labelled as an alternative (0.8, 39.J step 3, D-051(d)). Exercises 39.6 and 39.10 answer both designs. fm:model-builds lists the series (u17 00-3) |
| 2 | No unguided full build before the capstone (major) | FIXED; `ex43_17/` is a dependency | Exercise 43.17 with inputs (exh:43.8), Python-computed answers, and 43.Q naming it Capability 4's blank-workbook test. FM.3 gives it 15 hours. Solution files are requested (0.7 R8) |
| 3 | Time budgets inconsistent; exam cannot test Capability 4 (major) | FIXED | FM.3 totals 642 hours, with the capstone at 107. 89-6 budgets sum to 107. 90-3 splits Paper 4A (16 h, 60 marks) and 4B (8 h, 90 marks), totals reconcile, and 4A's scope is stated in 90-5 |
| 4 | Excel used from Ch 1 before Ch 13 (major, novice path) | FIXED | ssec:5.2.2 primer (u02, D-048, R-142). Ch 5 data table and automated payback marked optional with answers (u02 Walkthrough 1, steps 6 and 7). Exercise 1.11 is now a paper task (u01). The rebuild moved to 13.15. Glossary homes of relative and absolute reference moved |
| 5 | VBA required but never taught (major, novice path) | FIXED | ssec:13.8.5 with the Converge listing; Exercises 13.16 and 13.17 with answers. No exercise needs VBA (u09 log, defect 5). 40.C, 42.C and 43.C cite ssec:13.8.5 as optional |
| 6 | Drafting a full term sheet never practiced (major) | FIXED | Exhibit 56.6 and Exercise 56.17 (u11). 93-2 points to Exhibit 56.6 (u17, D-052). Capability map row 6 |
| 7 | DD scoping not practiced; request lists orphaned (major) | FIXED | Request-list exhibits: exh:47.10, exh:48.10 to 48.13, the Ch 49 and Ch 50 exhibits named in 93-2 (all in the anchor registry). Scope-letter exercises 48.17, 49.17 and 50.16 |
| 8 | No full credit paper before the capstone (major) | FIXED | Exercises 86.15 and 86.16 with data pack Exhibits 86.20 to 86.22 (u17 86-13) |
| 9 | One-hour screen practiced on one teaser (major) | FIXED | 85.11, 85.16 and 85.17: timed screens of a mine, a hospital PPP and a data center, with teaser Exhibits 85.10 to 85.12 |
| 10 | Tax concepts used before their home (major, novice path) | FIXED (one stale hedge remains; new defect 4) | ssec:7.11.4 (R-136, D-048); glossary homes of withholding tax, thin capitalization, earnings-based interest limitation and tax loss carryforward moved; assumed lists in u07, u08 and u09 cite it |
| 11 | No capability map (major) | FIXED | `bible/capability-map.md` (D-123), with the sub-skill column, a per-capability Part 2, and the Phase 4 and Phase 6 checks. Can-do lists are binding |
| 12 | Distress drafting thin (minor) | FIXED | Exercises 62.16, 64.19 and 64.20 (u13) |
| 13 | Ratings never revisited after Ch 35 (minor) | FIXED | Exercise 36.18 (u08; D-052) |
| 14 | Inputs only as JSON (minor) | FIXED; T and R input workbooks are a dependency | `model/inputs_case_p.xlsx` delivered. Input exhibits 39.5, 40.7 and 41.8. 39.J says "not the JSON file". fm:model-builds lists the input workbooks |
| 15 | Exercise workbooks not commissioned (minor) | FIXED; files are a dependency | u09 0.7 R8 and model-requests Section 4 list the Ch 13, 39, 43.17, 85.12 and 86.13 files. Exercise 61.15 needs no workbook. The audit reader copy is delivered (`model/exercises/Case_P_Model_AuditExercise_reader.xlsx`) |
| 16 | Sizing parameters never defended for a fresh market (minor) | FIXED | Exercise 36.19 (u08) |
| 17 | 85.11 duplicated the walkthrough (minor) | FIXED | Replaced (see 9) |

Dependencies (specified in full, not yet delivered): the five build-along files and `verify_build` (u09 0.5; model-requests u09-BA, u09-R7); `model/exercises/ch39_sponsor_solar_layout.xlsx`, `ex43_17/` (u09-R8); `model/exercises/ch13/` (three files), `ex85_12/`, `ex86_13/` (model-requests Section 4); `inputs_case_t.xlsx` and `inputs_case_r.xlsx`; capstone and examination files (Phase 6).

## New defects

### 1. Monte Carlo: u09 specifies two stochastic drivers, but the version 1.4 workbook and the ledger's P-F42 use four (major, Capability 4)

- Location: u09 Section 0.7 R5; 0.5 (Ch 43 row); 0.4 rows Time 16, Operations 37 and 39, Checks 8, 13, 14 and 19, and Inputs 311 onward; 43.5.1, 43.5.2, 43.J steps 1 and 5, and Exercise 43.14; case-bible.md Part 6 row 43 and the P-F42 register line; case-bible-annex-p.md P-F42 rows; against `model/figure-ledger-case-p.md` P-F42 (inputs row), `model/case_p_report.md` line 144, and `model/Case_P_Model.xlsx` Inputs F312 and the draw table J313 onward.
- Defect: u09 describes the simulation as availability and dispatch only. R5 specifies a draw table of 26 availability shocks plus one dispatch draw, and 43.5.1 gives only those parameters. But model version 1.4, built after the brief revision, simulates four drivers: availability, dispatch, heat-rate degradation (normal 0.12%, sd 0.04%, floored at 0) and KCR depreciation drift (normal 5.19%, sd 3.0%). The ledger's P-F42 percentiles (minimum DSCR 1.32x, 1.34x and 1.35x; equity IRR 12.9%, 13.2% and 13.7%), which 43.5.3 and Exercise 43.14 print, come from that four-driver run. Version 1.4 also adds:
  - an "active" flag (Inputs F312: run above 0 and Scenario 1 only);
  - Monte Carlo branches in rows built in Chapters 39 to 41: Time F16, and Operations rows 31, 37 and 39;
  - suspensions in Checks F8, F13 and F14.

  Section 0.5 does not list any of these as Chapter 43 modifications of earlier rows. A build agent following R5 would produce a `Ch43_outputs.xlsx` that cannot reproduce P-F42. A reader doing Exercise 43.14 to the 43.5.1 parameters would get different percentiles from the printed answer, which breaks Capability 4's "reconcile to the companion".
- Fix:
  1. In u09 43.5.1, 43.J and R5, state the four drivers and their parameters from the P-F42 inputs row. Set the draw table to 26 availability columns, 1 dispatch column, 1 heat-rate degradation column and 1 FX-drift column, as the workbook has them. Add the Inputs F312 active flag (Scenario 1 only) and explain why the simulation runs only on the FC base.
  2. Add a "Ch 43 modifies" line to Section 0.5 (Ch 43 row) for Time F16, Operations rows 31, 37 and 39, and Checks F8, F13, F14 and F19, with the rule that each Monte Carlo branch is inert while F311 = 0.
  3. Regenerate Section 0.4 from version 1.4 under 0.1 item 2. Update 0.1 items 1 and 2 from "version 1.3" to "version 1.4". Add Inputs 312 and the appended Inputs rows 1314 to 1321 (ECA limits for R11; Monte Carlo constants) to the Inputs block table.
  4. Change "Monte Carlo on availability and dispatch" to "Monte Carlo on availability, dispatch, heat-rate degradation and FX drift" in case-bible.md Part 6 row 43 and the P-F42 register line, in Annex P's P-F42 rows, and in u09 lines 1609 and 2015.

  Alternatively, the Case P modeler can rerun P-F42 on two drivers, and the ledger then governs. The editor must choose one of these two routes.

### 2. Exercise 43.14 targets a file that already contains its answer (minor)

- Location: u09 43.M, Exercise 43.14; 0.5 (Ch 43 adds "the appended Monte Carlo block").
- Defect: the task is "Implement the Case P Monte Carlo in `Ch43_outputs.xlsx`", which is the end-of-chapter file that already holds the block. The task does not say what the reader starts from.
- Fix: reword it as "Starting from your Chapter 43 workbook without the Monte Carlo block (or `Ch42_waterfall.xlsx` plus Exercise 43.12), paste the supplied draw table (`model/exercises/ch43_draw_table.xlsx`, or Inputs rows 313 to 1312 of `Ch43_outputs.xlsx`), implement the run index and the branches listed in Section 0.5, and reproduce P-F42; check against `Ch43_outputs.xlsx`." If the separate draw-table file is chosen, add it to R8.

### 3. Model-request status and the u09 version notes are stale after model version 1.4 (minor)

- Location: model-requests-round1.md rule 5 ("every item below is open. Nothing in ... `model/exercises/` ... exists yet") and the u09-R1 to R6, R9 to R12 rows; u09 0.1 items 1 and 2 and 0.7 ("model version 1.3 or later").
- Defect: version 1.4 has delivered R1 to R6 and R9 to R12, and the ledger and the case-state file say so. The audit reader copy exists. Writers reading the request file will use fallbacks that are no longer needed, for example the hand-computed timeline checks, and the ssec:42.6.3 statement built by the reader.
- Fix: add a status column to model-requests-round1.md Section 1. Mark u09-R1 to R6 and R9 to R12 "delivered in model v1.4 (October 3, 2026)" and the audit reader copy "delivered". Remove the rule 5 sentence. In u09 0.1 and 0.7, cite version 1.4.

### 4. Stale forward-reference hedge for ssec:7.11.4 in u08 (minor, novice path)

- Location: u08 Chapter 38 concepts assumed (line 1175): "until it is registered, cite sec:67.3 by forward reference"; also u08 log line 1133 ("central registration needed").
- Defect: D-048 records that the "if adopted" hedges were removed and ssec:7.11.4 is registered (glossary-canon and anchor registry). This leftover tells the Ch 38 writer to forward-reference Ch 67, which reopens round 1 defect 10.
- Fix: delete "; until it is registered, cite sec:67.3 by forward reference" and cite ssec:7.11.4 only.

### 5. fm:model-builds says supplied workbooks may use iterative calculation (minor)

- Location: u17 00-3, fm:model-builds ("every supplied workbook is macro-free, and circularity is resolved by closed form or by iterative calculation with a circuit breaker").
- Defect: this contradicts D-051(b), u09 0.2 ("Banned: ... iterative calculation") and 0.6. Under those rules, supplied workbooks use the closed form or unrolled rows, and iterative calculation is taught only as an alternative (u09 0.8).
- Fix: replace with "every supplied workbook is macro-free and has no circular reference or iterative calculation; circularity is resolved by closed form (or, in the Chapter 13 practice workbook, unrolled iteration rows); iterative calculation with a circuit breaker and the paste loop are taught as alternatives for the reader's own models."

### 6. "Kali Gandaki Hydro" is used for two different fictional projects and is close to a real plant (minor)

- Location: u08 Exercise 36.19 (Kali Gandaki Hydro Pvt Ltd, 90 MW, western Nepal); u09 Exercise 39.9 (Kali Gandaki Hydro, 142 MW, Nepal, 2028).
- Defect: one name has two inconsistent specifications. The 39.9 version, a roughly 142 MW run-of-river plant in Nepal, is close to the real Kali Gandaki "A" plant (about 144 MW), which breaks the standards Section 9 rule on real organizations. The name is not in Case Bible Part 5A.
- Fix: rename both projects to distinct, checked fictional names (for example "Myagdi Khola Hydro" for 39.9 and "Seti Dhara Hydro" for 36.19, after a Part 5 web check), and register them in Case Bible Part 5A.

## Other checks made (no defect)

- Capability map totals: examination allocation sums to 68, matching 90-4. Every capability has a walkthrough, a Tier 3 item before the capstone, a capstone task and at least three examination questions. All new labels (exh:43.8, 56.6, 85.10 to 85.12, 86.20 to 86.22, 47.10, 48.10 to 48.13; exr ranges for Chapters 13, 36, 43, 48, 49, 50, 56, 62, 64, 85 and 86; ssec:5.2.2, 7.11.4, 13.8.5) resolve in the anchor registry.
- The Ch 39 to 43 build order closes: every Funding constant reads rows assigned to Ch 40, and the only forward reads are the registered provisional rows (Construction row 38; Waterfall rows 33 and 43; Debt rows 103, 104, 110 and 112).
- The u09 row map matches the workbook in labels for all 488 rows, and in first-column formulas except the 7 Monte Carlo rows in defect 1. Exercise 62.14's Waterfall rows 21 to 26 match the workbook.
- Exercise 43.17's stated answers are internally consistent: uses, gearing, equity, upfront fee, and DSRA equal to the first half-year's debt service.
