# Consolidation after the round 1 brief revisions: part B log

Date: October 3, 2026. Editor: consolidation editor, part B. Scope: the Case Bible and its two annexes, model and ledger follow-ups, the fact-sheet plan, two fact-sheet corrections, the capability map and the decisions log. Part A edits the briefs, registry, glossary, rulings and style sheet; part B touched none of those files.

Inputs read: `standards.md` Sections 5 and 9; `bible/decisions.md` (all); `bible/case-bible.md`, `case-bible-annex-p.md`, `case-bible-annex-tr.md`; the three figure ledgers in `model/`; the "Revision log (round 1)" and "Central changes needed" sections of `bible/briefs/u01.md` to `u17.md`, plus the open-request sections they point to (u09 Section 0.7, u12 figure requests, u17 00-3, 89-6a, 90-4 and 90-5); `reviews/blueprint/central-fixes-log.md`. Spot checks against `model/case_p.py` (P-F26, P-F65) and `model/case-state-case-p.md`.

Decisions appended: D-116 to D-123. The log's highest ID was D-115 when re-read just before appending.

## 1. Case Bible (now Version 1.2) and annexes (now Version 1.2)

Every changed cell or paragraph carries "(round 1)".

### Ledger conflicts, resolved for the ledger

| Item | Was | Now | Where |
|---|---|---|---|
| 2025 bond combined DSCR (P-F23) | "sculpted ... to a combined base-case minimum DSCR of 1.35x" | The level combined DSCR is a model output, 1.59x. The bond amount is set by the prepaid principal. 1.35x was the design floor. | Bible 1.9, Part 7, Part 6 row 63, P-C51; Annex P 8.3 |
| Case T notes minimum DSCR (T-F10) | "sculpted ... at 1.30x minimum DSCR" | 1.30x is the plan's floor. The outcome is the 2.65x divisor and the 2.00x minimum (T-F09, T-F10). | Bible 2.8, Part 7, Part 6 row 64, T-C25; Annex TR T.16, Part F, Part L |
| Covenant-breach ratios (P-F21) | Bible design range 0.80x to 1.00x; case-state note 1.14x and 0.97x | Ledger 1.13x (December 31, 2022) and 0.96x (June 30, 2023) govern. The case-state correction is requested from the modeler. | Bible 1.9, Part 6 row 62, Part 7, P-C57 |
| LC amounts (P-F39, P-F40) | Already fixed in v1.1 (36.2 / 36.6) | Checked: no 33.8 remains outside change-log row P-C44 | – |
| KCR forward profile (P-F65) | "seven semiannual settlement dates" | One forward per monthly onshore EPC payment. The ledger prints every sixth month and the totals. | Bible 1.6, Part 7, P-C52 |
| Annex P 3.1 gross arrears | Request said 146.4. The file already had 149.2 from the v1.1 fix. | 149.2 = P-F20 112.6 + P-F40 36.6 (D-013), with both sources cited. 146.4 is noted as superseded and never printed. | Annex P 3.1 |
| P-F02 reconversion rate | Annex P 1.1.5 "invoice-date mid rate"; ledger "2022H1 average" | The contract term is unchanged. The model's half-year average is a labeled proxy. No rerun. | Bible 1.4, Annex P 1.1.5 and 8.3, Part 7, P-C54 |
| P-F26 consideration | Unstated | Read from `case_p.py`: 77.3 is the cash price and excludes the USD 4.0 million deferred consideration (nil at completion). The 2.1 swap hedge-reserve recycling sits outside the 82.0 loss. | Bible 1.9, Part 6 row 66, Part 7, Annex P 8.3, P-C56 |
| Macro paths (D-046) | Unlabeled | Bible 1.1 note: the US CPI, LIBOR, SOFR and swap paths are "Case P index (illustrative)". P-F02, P-F03 and P-F22 are labeled. | Bible 1.1, Part 7, P-C55 |

### Other requested changes

- Annex P 1.15.5: the hedging basket now reads "any hedging under the hedging policy". That covers the swaps and the KCR forwards that D-114 requires. Only FX or commodity hedging outside the policy needs Majority Lenders' consent (u11 central change 15).
- Cash-flow-hedge designation of the 2018 forwards was added to Bible 1.6 and Part 6 row 66. Under IFRS 9, the reserve is removed into the cost of the construction asset, so the hedge reserve recycled in 2026 belongs to the swaps alone (u14).
- Annex P 2.1, Devesh Raval: his "where wrong" was rewritten against P-F62. The committee tariff of 74.35 would still have beaten 76.36. His error was dismissing the threat without measuring a margin of under 3% (u10 central change 4; P-C53).
- Bible 1.5: the ABDB fund's entry is 10 points from Kilnworth and 5 from Talmé, not pro rata (u06 central change 10; P-C59).
- Bible 1.6: the ECA first-repayment test reads 24 months, with 2% repaid (u08 central change 7; Annex P 3.6).
- Bible 1.9: the subrogation pointer now goes to Annex P 2.8 (u13 central change 10).
- Annex P 7.3: the Chapter 7 drill's reuse of Corredana and ELNACOR is recorded (u02 C-11).
- Change-log ID collision: P-C46 and P-C47 were each used twice. The central-fix scene rows are renumbered P-C49 (Chapter 8) and P-C50 (Chapter 6). Annex P 2.2 row 8 is updated. D-115 and Annex P 4.13 keep P-C46 and P-C47 for the RBL and bid-model rows. Briefs that cite "P-C46" for the Chapter 8 premise mean P-C49; they belong to part A and were not edited.
- New change-log rows: P-C51 to P-C59, T-C25, T-C26, N-C02.
- Part 7 header: the ledger is at model v1.3.

### Part 6 storyline rows merged (characters and figures per scene)

Rows 11 (Mariama), 12 (Tomasz; P-F61), 14 to 16 (u04 additions to P-C31: the KCR cost row, Pieter's May 2017 forward proposal, the P-F65 preview; P-C58), 22 (P-F47; P-F65 pointer), 39 (Exhibit 39.5 replaces the JSON file; two-timeline design; build-along file), 40, 41 (P-F10, P-F38, P-F47), 42 (P-F08, P-F09, P-F11a, P-F11b), 43 (P-F28, P-F41; Exercise 43.17), 45 (Elspeth Varga; R-F01, R-F19), 46 (Annex TR R.1 and R.7; A1 USD 446.3 million = 436.0 + 10.3), 47 (Philippa Carrow, Kunal Mehrotra; R-F05; the Devesh constraint), 48 (Elspeth Varga, optional Rhys; P-F47), 49 (Annex P 2.4, 4.2), 50 (Annex P 4.3), 51 (P-F63, P-F65), 53 (P-F65), 55 (Castellan's two approval conditions; P-F65), 56 (Annex P 1.15.2 sequence; term sheet October 27, 2017), 59 (Edwige, Adwoa, Sylvestre; P-F65), 61 (Gilles Tchibozo; P-F33), 62 (Gaspard; P-F21 values), 63 (Rosine Gbaguidi-Ayi; P-F23 note), 64 (Elspeth Varga; T-F09/T-F10 note), 65 (Gilles, Rosine; P-F48), 66 (designation; P-F26 reading), 73 (R-F18, R-F19), 76 (Devesh), 79 (optional Elspeth), 86 (P-F39, P-F61). These rows were already merged in v1.1 and were checked: 16 (LC), 23, 24, 26, 28, 35 to 38, 58, 60, 69, 72, 74, 75, 80, 81.

### Part 7 figure register

- Printing-chapter users were extended from the revisers' requests for P-F08, P-F09, P-F10, P-F11a, P-F11b, P-F28, P-F33, P-F41, P-F47, P-F61, P-F63, P-F64, P-F65, R-F01 and R-F05.
- Descriptive notes were added to P-F02, P-F03, P-F21, P-F22, P-F23, P-F26, P-F40, P-F49, P-F63, P-F65, T-F01 and T-F10.
- New Part 7.4 is an automated index of figure-ID mentions in the round 1 briefs. It excludes replacement and neighbor lines and serves as a checklist for the consistency checker.

### Case T lenders' traffic advisor

- The new character is Elspeth Varga: Ardmorean, born 1973 to a Hungarian father and a Scottish mother, director of Ridgeway Traffic Consultants.
- Her work: the 2014 banking case, the counts behind Rhys Tanaka-Bell's monitoring reports, and the 2023 restructuring case. Where she is wrong: she kept Pellow's housing timetable.
- She appears in Chapters 45, 48 and 64, and optionally 79.
- A web check on October 3, 2026 found no person of that name.
- Entries: Bible 2.4, 4.2 and 4.5; Annex TR T.19, N.3, N.5, T.16 and T-C26. Rhys keeps the IE and monitoring seat; the reviser requests are met by T.18 plus T.19.

### Name register (Bible Part 5A)

- Registered: every illustrative name listed in the revision logs (u01, u02, u03, u14, u17), plus Pasundra/PSK/LEP and Tavarra/TVR/TPPC, which are marked clear.
- Risk-ranked web checks were run on October 3, 2026. Results:
  - Rename (a real namesake exists): Thar Surya Power, Al Dhafra Sun Two, Termoeléctrica del Sur SA, Seti Khola Hydropower, Ocmulgee Valley EMC, Calcasieu Point LNG, Ras Gharib Wind SAE, Calatagan Power, Noor Draa Solaire SA (the last from the editor's knowledge).
  - Rename advised: the two Bałtyk names, Mid North Wind, Darling Downs Storage, Moorabool Peaking Partners, Thessaly Airports, Autostrada Pedemontana Est.
  - Internal clashes: Ostrander Bank (against Case R's Ostrander Data Systems), Lindqvist (u14 and u17), Calloway Materials (against Case R's Calloway Mesa), Campiña Solar and Campiña Sur Solar.
  - Clear in this pass: Elspeth Varga, Aldermoor Bank, Orrell Energy, Kurrajong Ridge Energy, Harlow Vantage Energy, Coral Coast Peaking, Vientos del Chubut, Glasfaser Oberpfalz, Mojave Flats Storage, Tehachapi Mesa Solar, Sangamon Sun, Cholla Ridge Storage.
- All remaining names are "not checked", and writers run the Part 5 check before drafting. The units u05 to u13, u15 and u16 did not list their new names; the consistency checker compiles them from the drafts.
- The renames belong in the briefs (part A) or in drafting.

## 2. Model follow-ups

`bible/model-requests-round1.md` (new) lists every model and ledger request, each with an owner and a fallback:

- u09 R1 to R12 and the build-along series
- P-F16 and P-F17 ledger extensions
- P-F49 itemization: the visible lines sum to 115.45 against the 121.59 total, leaving 6.14 unitemized
- P-F63 prepayment cure
- P-F40 monthly netting set-offs
- the P-F02 option
- the P-F65 sample-row labeling and the FC versus actual schedule question
- the P-F26 optional fair-value line
- the case-state note correction
- RORAC in `case-p-input-requests.md`
- T-F01 retained-toll breakeven
- the T-F10 confirmation
- the input workbooks for P, T and R
- `model/exercises/ch13/` (three files), `ex85_12/` and `ex86_13/`
- the u09-R8 exercise files
- the fm:model-builds listing
- the capstone mini-Bible, inputs, model, starting and seeded files, and the C-F01 to C-F24 ledger
- the `model/exam/` files

Owners: Case P modeler, Case T modeler, Case R modeler, build agent and Phase 6. Found during compilation: the P-F65 ledger rows print `schedule[::6]`, so the listed months do not sum to the KCR 32,204 million total. They also run to 2021-08 under a "Contract (FC)" label.

## 3. Fact-sheet plan

The following sections were appended to `bible/fact-sheet-plan.md`:

- Round 1 placements by unit and section, compiled from the revision logs.
- A request-to-slug mapping added in round 1.
- Open requests with their status: the twelve sheets in progress (t-repowering, t-fast-standard, t-energy-yield, t-battery-degradation, t-earned-value, t-sustainable-finance-2, wte-operating-pf, subsea-cable-pf, saf-mandates, h2global, kenya-steam-sales, t-decommissioning-accounting) and 24 optional or undelivered requests, each with a fallback.
- The corrections made to delivered sheets.
- An automated slug-to-chapter citation scan of all 172 files in `facts/`. The five in-progress sheets that no brief cites yet are marked for round 2 placement.

A precedence note in the old mapping section says the round 1 tables govern. Files for the in-progress slugs already exist in `facts/`, but they are not to be cited until the editor marks them delivered.

## 4. Fact-sheet corrections

- `facts/cobre-panama.md`: the "361 of 370 fulfilled, 7 partial, 3 non-compliant" counts sum to 371, and 361/370 = 97.6% does not match the reported 87.7%. A web check on October 3, 2026 explained the gap: the 87.73% is a weighted score across four components (90.20 / 88.23 / 87.64 / 81.70), and sources report both 370 and 371 commitments. The sheet's summary and item 19 now state the score and its components. A correction note was added, the split went into "Do not state", and two secondary sources were added. The split itself could not be reconciled.
- `facts/t-frontier-data.md` item 20 now matches `t-cap-and-floor.md`: 73 projects assessed (77 eligible, 4 withdrew), durations of 8 to 32 hours, and a consultation that closed on August 14, 2026 (Ofgem), not August 7. An alignment note was added and "Do not state" was extended. `t-cap-and-floor` governs.

## 5. Capability map

`bible/capability-map.md` (new) has three parts:

- Part 1: Exhibit FM.1 with the sub-skill column.
- Part 2: for each of the fifteen capabilities, the citing chapters and a per-chapter table of the worked examples, walkthroughs and exercises the briefs name. It includes 43.17, 56.17 and 86.15/86.16, plus 36.18, 36.19, 48.17, 49.17, 50.16, 62.16, 64.19, 64.20, 85.11, 85.16 and 85.17. Each capability also lists its capstone task and its examination allocation (u17 90-4).
- Part 3: consistency findings. The main one: FM.1's Capability 5 walkthrough "36.6" should be 36.11, a u17 fix for part A.

Part 2 was compiled by script from the briefs' capability tables and can-do lists, then supplemented by hand where the briefs list items in prose. Chapters that cite a capability without itemizing are listed separately.

## 6. Not done, with reason

- The renames flagged in Part 5A and the corrections to Exhibit FM.1 are in brief files, which belong to part A. Both are listed for part A and the writers.
- `model/case-state-case-p.md` was not edited; it is a modeler file and the correction is in the model requests. The same applies to the P-F65 labels.
- Case Bible 4.4 Castellan and Sterrenberg in the capstone (u17 central change 8, optional): left to the Phase 6 capstone mini-Bible.
- Not every illustrative name was web-checked. Checks covered a risk-ranked sample, and the rest are marked "not checked" for the writers.
