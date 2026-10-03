# Consolidation part A: log

Date: October 3, 2026. Editor: consolidation editor, part A. Inputs read: `standards.md` Sections 10 and 11 (Phase 1); `bible/decisions.md` (through D-047, and part B's D-116 to D-123); `bible/ownership-resolutions.md`; `bible/style-sheet.md` Addendum; the "Revision log (round 1)" and "Central changes needed" sections of all seventeen briefs (`bible/briefs/u01.md` to `u17.md`); `reviews/blueprint/central-fixes-log.md`; the coordinator's later instruction (names, FM.1, P-C49/P-C50). Decisions: D-048 to D-055. Rulings: R-021 amended; R-142 to R-148 added (Section O).

## 1. Anchor registry regenerated (`bible/anchor-registry.md`)

- Built by script from the revised briefs (anchor sections in all their formats, locked TOCs, worked-example lists, range notation), then hand-fixed. Scripts and intermediates are in the session scratchpad (`reg/`).
- Result: 5,558 labels (94 ch, 1,425 sec, 2,053 ssec, 584 ex, 624 exh, 371 cl, 254 eq, 153 fw), 1,391 exercises in 89 range rows, 8 fm labels, 3 fm exhibits. Against the first issue: 317 new labels (cl 214, sec 41, exh 35, ssec 15, ex 12) and 981 changed captions.
- Section 2 keeps A1 to A14 and adds B1 to B12 (the regeneration conventions). Section 3 frameworks regenerated with homes moved for 6.2 (ssec:6.5.4), 8.1 (ssec:8.3.3), 28.1 (sec:28.5) and 86.2 (ssec:86.3.1); 43.2 spelled "catalog". Section 6 is the build report.
- Verified: no duplicate labels; 88 `ch:` captions equal architecture.md, and every brief header and `ch:` anchor row matches; numbering gap-free in every chapter for sec, ssec, ex, exh, cl, eq and variant letters, no orphan subsection; every label token in brief bodies and unit glossary files resolves except eight deliberate non-labels (placeholder `ch:N`, `cl:35.2c` stated as absent, the withdrawn `cl:62.1a`, `cl:62.1b`, `cl:62.2`, `cl:62.2a`, `cl:62.2b` named as withdrawn, and the writer-assigned `exh:89.4`); every glossary-canon home label resolves.
- Applied from central-fixes log item 9: exh:55.10 caption; R-141 retitles (sec:43.5, ssec:51.5.4, ssec:22.6.2, ssec:79.4.1, sec:86.3, combined-case splits at sec:68.11, sec:73.9, sec:84.12, and sec:31.11); American spellings; ruling retitles (ssec:62.7.4, ssec:38.3.2, ssec:43.2.4, ssec:45.7.3, ssec:46.1.1); R-137 retitles; new labels ssec:5.2.2, ssec:7.11.4, ssec:13.8.5; clause-variant rows for every group; fragment captions replaced; matter labels sec:89.1 to 89.29, sec:90.1 to 90.12, exh:89.1 to 89.3, exh:90.1, ch:92 to ch:94; DD request lists exh:47.10, 48.10 to 48.13, 49.7 to 49.12, 50.6; cl:21.8, 23.3, 24.2, 24.3, 25.2 to 25.5, 26.3 to 26.5, 51.7, 51.8, clauses in Ch 32, 37, 38, 47, 52, 58, 60, 63; exh:30.4, 30.5, 56.6; ssec:76.8.5, 82.3.4, 84.3.5.
- Unresolved (registry Section 6): eight caption pairs repeat across chapters (for example exh:40.4 and exh:55.9, both "Case P sources and uses at financial close"); left to the later chapter's writer under R-117. cl:10.1 to cl:10.5 keep first-issue captions (u03 gives none).

## 2. Brief edits (surgical)

| Brief | Edit | Source |
|---|---|---|
| u01, u03, u07, u08, u09, u10, u13, u14 | 54 lines: `ssec:5.0` to `ssec:5.2.2`, `ssec:7.6.4` to `ssec:7.11.4`, "if adopted" hedges removed (revision logs left as historical records) | u02 placements; D-048, R-142 |
| u01 | Ch 1 assumed table cites `ssec:7.11.4` for the tax computation | u01 central change 4 |
| u03 | ssec:13.8.5: the Converge macro is stated to be the paste loop of Exercises 40.10 and 42.12 | u09 central change 8 |
| u03 | Ch 12 installment checked: Félix's questions are already physical (R-139); no edit | u06 central change 11 |
| u06 | Clause 26.3 is the base equity contribution undertaking and LC support; acceleration is one sentence without variants; Exercise 26.12 and the anchor caption follow | u07 request; R-144 |
| u07 | ssec:32.9.4 cites Exhibit 67.4 | u07 request; R-145 |
| u08 | Exercise 36.18 cites Framework 30.2 and Exhibit 30.5 (reads 'bbb' at OPBA 3 and 'b' at OPBA 7, the ranges of Exercise 30.11); Example 38.1 points to sec:68.5 and Exhibit 68.1; "proposed R-122" now "R-122" | u07, u14 requests; D-055 |
| u09 | Glossary rows "pasted value" and "locked-debt mode" reworded; calendar-rows note now cites amended R-021 | u09 central change 3; D-047 |
| u10 | Ch 49 glossary row "OFAC 50 percent rule" marked applied (home ssec:60.7.1) | R-146 |
| u11 | ssec:51.7.3: Clause variants 51.8 take the reservation-of-rights and waiver-condition variants formerly specified for Ch 62 | u13 central change 7; R-143 |
| u12 | Generic LC home row now cites ssec:16.4.1 (R-123) instead of a pending ruling | R-123 |
| u13 | ssec:62.7.4 "Applying the waiver letter to the Case P breach"; Clause 62.1 is the Case P letter applying Clause 51.8 (former cl:62.2 merged; cl:62.1a and cl:62.1b withdrawn, their positions narrated in Walkthrough 62.10); 62.11.4, the 62.11 terms note, Exercise 62.10, concepts item 12, capability entries and anchors follow | u11 central change 12; R-126; R-143 |
| u14 | ssec:67.10.1 places Exhibit 67.4 as the credit-dates exhibit formerly planned as Exhibit 32.5; Ch 84 glossary row "transition climate risk" becomes "transition risk" applied | u07 request; R-145, R-147 |
| u15, u16 | Glossary rows: "funded decommissioning program"; "anticipated repayment date" not abbreviated | R-148 |
| u17 | Matter 93-2: term-sheet template points to Exhibits 56.6 and 56.4 and Exercise 56.17; DD request lists point to the registered Ch 47 to 50 exhibits; FM.1 Capability 5 walkthrough 36.11 | u10, u11 requests; coordinator |
| u02, u03, u06, u10, u11, u14, u17 | Fictional names renamed (list in D-054) | Coordinator; Case Bible Part 5A |

Verified without edit: Exercises 43.17 (u09) and 56.17 (u11) exist; fm:model-builds lists the build-along files; eq:37.4 and the forward reference to ssec:51.5.4 in u08; no brief cites P-C46 or P-C47 for the Ch 8 or Ch 6 scenes (u10's P-C47 is the bid-model row, correctly).

## 3. Glossary canon (`bible/glossary-canon.md`)

1,793 entries (1,784 before). 76 field changes, re-sorted.

- Homes moved: relative reference, absolute reference to ssec:5.2.2; withholding tax, thin capitalization, earnings-based interest limitation, tax loss carryforward to ssec:7.11.4; yank-the-bank to ssec:51.7.2.
- Added: qualifying facility (QF) and avoided cost (sec:3.2); tool port, service port (sec:12.7); cyber insurance, silent cyber (ssec:27.3.4); bond-equivalent yield, accrued interest (ssec:30.3.1); stand-alone credit profile (SACP, ssec:30.5.2); additional termination event (ATE, ssec:51.5.5); statutory security agent (ssec:52.2.3); optimism bias uplift (ssec:57.2.3); anticipated repayment date (ssec:82.7.3, not abbreviated: ARD is the Case T currency code).
- Deleted or merged: financial adviser (duplicate of financial advisor); PF2 (duplicate of Private Finance 2); OFAC 50 percent rule (synonym under "50 percent rule", ssec:60.7.1); transition climate risk (merged into transition risk, ssec:14.19.2).
- Renamed: regulatory risk parameters to regulatory PD and LGD (synonym kept); standardized approach; specialized lending; funded decommissioning program; risk, mitigant, and residual table.
- Definitions: PURPA (fact-sheet caveat removed); consequential loss (unverified English-law authority removed); make-whole premium (revised Ch 30 text); pasted value and locked-debt mode (macro-free); binding offer and permitted leakage ("share purchase agreement"); report challenge protocol ("An eight-step"); regulatory risk ("licenses"); functional unit ("operating theater"); UK Bribery Act and adequate procedures ("offense"); output floor, supervisory slotting, Side-by-Side Package (American spelling); cost oil (no PSC); gross calorific value note (home kept at ssec:25.2.6); advisor, metric ton swept.
- Already in the canon from the central fixes (checked): PPA, EPC contract, term sheet, letter of credit, gearing split, sizing case, PD and LGD, breakeven, ten-year P90, overbuild split, clean spark spread, MMBtu, hybrid till, reservation of rights, Default, input VAT, VAT refund lag, completion long-stop date, FPSO note, grace period senses, competing facility, compensation event (NEC), TSA and BOP homes; no u17 entry for teaser, tornado chart, walk-away price, issues list, RAROC, FOAK or NOAK.
- Rule 6 of the header updated; every home label resolves in the regenerated registry.

## 4. Ownership resolutions (`bible/ownership-resolutions.md`)

- R-021 rewritten per D-047 (rows stay in the workbook: Operations rows 7 to 15 with indices 16 to 27; Construction rows 16 to 18; Inputs rows 281 to 309), with the superseded text quoted.
- New Section O, R-142 to R-148: placement of the R-135/R-136 subsections; waiver conditions and the Case P letter; acceleration of base and contingent equity; the US credit-dates exhibit; one entry for the 50 percent rule; one entry for transition risk; canon homes confirmed at consolidation. "Amended by" lines added to R-068, R-073, R-088, R-091, R-092, R-126, R-135, R-136. Ruling count 148.
- u08's "proposed R-122" is the adopted R-122 (identical content); it is cited as R-122 and not duplicated. No unit proposed another ruling number.

## 5. Style sheet (`bible/style-sheet.md`)

- A.6 rewritten per D-047 ("Calendar rows in the model").
- A.5a added: earned-value symbols `W^{earned}_t`, `W^{planned}_t`, `SPI_t`, `T_{plan}`, `\hat{T}` for eq:61.3 (u13 central change 14).
- A.3 table: "anticipated repayment date", never ARD.

## 6. Case Bible and capability map (coordinator items)

- `bible/case-bible.md` Part 5A.2: each flagged name now reads "Renamed (round 1) to ...; not web-checked (consolidation A)". The replacement names were checked only against every file in `book/` (no collisions); they were not web-searched.
- `bible/capability-map.md`: the Capability 5 row and consistency finding 1 record the FM.1 correction to 36.11.

## 7. Left for others

- Case Bible, ledger and model items in the revision logs (part B and the modelers); tracker target lengths; fact-sheet plan; name checks for names not in Part 5A.2.
- Phase 3 writers: the eight repeated captions (registry Section 6); confirm cl:10.1 to cl:10.5 captions; web-check the D-054 replacement names before drafting.
