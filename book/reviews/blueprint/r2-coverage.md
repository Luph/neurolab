# Blueprint review round 2: coverage lens

Reviewer lens: coverage (standards Section 4 A to T, Section 4.P sector elements, Section 5 running-case requirements, Section 7 candidate cases). Fresh reviewer; round-1 report `reviews/blueprint/coverage.md`.
Date: 2026-10-03.
Files checked: revised briefs `bible/briefs/u01.md` to `u17.md`; `bible/architecture.md`; `bible/decisions.md` (D-038, D-042, D-044, D-114, D-116, D-117, D-119, D-122); `bible/ownership-resolutions.md` (R-144); `bible/anchor-registry.md`; `bible/case-bible.md` v1.2 with annexes P and TR; `bible/fact-sheet-plan.md`; `bible/tracker.md`; `bible/capability-map.md`; `model/figure-ledger-case-p.md` (P-F65, P-F66); `facts/` (172 files).

## Verdict: FAIL

All ten round-1 defects were acted on, and the blocking one (Case P currency hedging) is fixed in the Case Bible, the decisions log, the model ledger and the briefs. Three major defects remain open, all new or residual from the revisions:
- N1: two briefs describe the KCR forwards in a way that contradicts the ledger.
- N2: three briefs still say Case T's new counsel and adviser characters do not exist.
- N3: twelve fact sheets were delivered after the round-1 placements but are not placed or recorded as delivered.

Counts of new defects: blocking 0, major 3, minor 2.

## Round-1 defects: status

| # | Round-1 defect (severity) | Status | Evidence (current location) |
|---|---|---|---|
| 1 | Case P has no currency hedging (blocking) | FIXED (residual inconsistency logged as N1) | D-114, D-117; Case Bible 1.6 (line 282: forwards, policy requirement, IFRS 9 designation), timeline 2018-07-17, Part 6 rows 37, 38, 40, 53, 59, 66, Part 7 P-F65/P-F66, change log P-C45/P-C52; `architecture.md` Case P summary ("interest-rate swaps and a construction-period currency hedge (D-114)"); ledger P-F65 and P-F66; u08 sec:37.10 (Exhibit 37.13), ssec:37.7.3, sec:38.11; u09 ssec:40.1.4; u12 sec:59.10 beat 2 (Exhibit 59.12); u14 sec:66.12; u13 sec:61.15 |
| 2 | DD request lists have no home content (major) | FIXED | u10 Exhibit 47.10 (sec:47.11), Exhibits 48.10 to 48.13 (sec:48.9), 49.7 to 49.12, 50.6; all registered in `anchor-registry.md`; u17 Matter 93 row (line 1758) cites every label; capstone task 7 builds on them |
| 3 | Original clause language missing in Ch 21, 23 to 26 (major) | FIXED | Registry: cl:21.4 (royalty, a to c), cl:21.8 (port MAG, a to c), cl:23.3, cl:24.2, cl:24.3, cl:25.2 to cl:25.5, cl:26.1, cl:26.3, cl:26.5, each with variants; drafting exercises 23.12, 24.12 to 24.13, 25.12 to 25.13, 26.12 to 26.13 (u06 revision log). The renumbered labels (cl:21.5 to 21.9, cl:26.x, cl:27.x, cl:28.x) have no stale citations in other briefs. The optional airport-charges clause was declined with a reason (u05 line 2060). Acceptable. |
| 4 | Sector deep dives lack landmark deals and failures (major) | FIXED (WtE through the agreed fallback; see N3) | u15: ssec:71.4.3 (vineyard-wind-2024), 71.5.3 and 71.7.3 (us-offshore-wind-2025), 72.5.2 and 72.5.5 (geothermal-risk-facilities), 73.2.3 (t-storage-safety), 73.3.3 (pumped-storage, Snowy 2.0), 73.5.2 and 73.6.2 (t-cap-and-floor, Greenlink), 75.6.1 (t-rbl; "No verified RBL norms" removed), 75.3.5 (upstream-field-pf, commodity-prepay), 75.5.1 (tap-pipeline), 76.7.2 (fsru-charters), 76.8.2 to 76.8.4 (fpso-financing), new ssec:76.8.5 (coral-sul-flng, registered). u16: ssec:80.2.3 (LaGuardia), 80.3.3 (Lekki), 81.2.2 (Manila), 81.4.3, 81.5.1 and 81.7.1 (wte/Willows, with the D-011 fallback for WtE terms) |
| 5 | Fact-sheet plan stale; ratings taught without agency frameworks (major) | PARTLY FIXED | Ratings: fixed (u07 sec:30.5 items 14 to 16 teach S&P CPBA/OPBA from t-ratings-2, Fitch from t-ratings, Moody's as labeled; Exhibit 30.4 registered; Example 30.4). Plan: rewritten with a delivered-sheets table and a request map (D-042, D-122), but it is stale again. It says "160" files (`facts/` holds 172), and it lists t-repowering as both "Not delivered; commission" (line 269) and "In progress" (line 396), although tracker lines 117 to 118 record it as done. t-repowering is delivered but unused (see N3). |
| 6 | Taxonomies taught for the EU only (minor) | FIXED (fallback) | u14 ssec:84.3.5 "Other taxonomies and interoperability" (registered) and Exercise 84.16, taught at concept level with no non-EU taxonomy named. This is the round-1 fallback. The delivered t-sustainable-finance-2 covers no non-EU taxonomy, so the fallback stands; the plan's line 401 should say so (N3). |
| 7 | ISDA hedging at overview level only (minor) | FIXED | u11 ssec:51.1.4 expanded (schedule elections); new ssec:51.5.5; Clause 51.7 (additional termination events, a sponsor, b lender, c hedge-bank), registered |
| 8 | Repowering has no fact base (minor) | PARTLY FIXED | u13 ssec:62.8.1, sec:65.4 and sec:65.8 teach it as principle and Illustrative (lines 565, 652, 1795, 1971). t-repowering (80/20 rule, RED III, IEC TS 61400-28, lender consents) has since been delivered, but u13 still says "not delivered" and does not use it (N3). |
| 9 | Telecoms omit subsea cables (minor) | FIXED (fallback; see N3) | u16 new ssec:82.3.4 and Example 82.3 (Illustrative); sec:82.3 retitled "Fiber and subsea networks"; registry matches; the data-center example became ex:82.4, with no stale citations elsewhere. subsea-cable-pf (EASSy/WIOCC) is now delivered but unplaced. |
| 10 | Case T cast lacks lenders' counsel, sponsors' counsel and IE (minor) | PARTLY FIXED | Case Bible and Annex TR fixed: D-044, D-119; Annex TR T.18 and T.19; Part 6 rows 58, 64, 79 name Lachlan Mereweather, Anjali Thevarajah, Rhys Tanaka-Bell and Elspeth Varga. u12 sec:58.13 uses them. u13 sec:64.14, u16 sec:79.14 and u10 sec:48.8 still say they do not exist (N2). |

## New defects

### N1. The KCR forward profile in Chapters 37 and 59 contradicts the ledger (major)

- **Location:**
  - `bible/briefs/u08.md` line 1009 (sec:37.10, Exhibit 37.13: "the seven semiannual forwards from August 2018 to August 2021 (P-F65)").
  - `bible/briefs/u12.md` line 1079 (sec:59.10 beat 2: "maturing semiannually from August 2018 to August 2021 ... the seven forward dates and rates ... The last forward matured in August 2021, fifteen months before the queue began").
- **Defect:**
  - D-116 and change-log row P-C52 rule that there is one forward per monthly onshore EPC payment, with the ledger winning. Case Bible 1.6 also withdraws the "seven semiannual settlement dates" wording.
  - Ledger P-F65 lists monthly forwards from 2018-08, and P-F66's last settlement and nil MTM are dated 2021-11-30. u14 line 252 correctly says November 2021.
  - The Central Bank FX queue began November 7, 2022 (Case Bible line 414), so the gap after the last forward is about twelve months, not fifteen.
  - As briefed, Exhibits 37.13 and 59.12 would print a profile the ledger does not contain.
- **Fix:**
  - **u08 line 1009:** replace "the seven semiannual forwards from August 2018 to August 2021" with "the monthly forwards from August 2018 to November 2021, one per onshore EPC payment, with every sixth month and the totals as the ledger prints them (P-F65; P-C52)".
  - **u12 line 1079:** replace "maturing semiannually from August 2018 to August 2021" with "one forward per monthly onshore EPC payment, August 2018 to November 2021". Replace "the seven forward dates and rates" with "the profile the ledger prints (every sixth month) and the totals". Replace "The last forward matured in August 2021, fifteen months before the queue began" with "The last forward settled on November 30, 2021, almost a year before the queue began on November 7, 2022".
  - **Check the exhibits:** confirm that the Exhibit 59.12 caption ("2018–2021") and the Exhibit 37.13 contents follow the same profile.

### N2. Three briefs still say Case T has no lenders' counsel or monitoring adviser (major)

- **Location:**
  - `bible/briefs/u13.md` line 1425 (sec:64.14 beat): "Case T has no lenders' counsel or traffic-monitoring engineer in the Case Bible ... the legal argument at the sanction hearing is narrated without a named lawyer, and no character is invented."
  - `bible/briefs/u16.md` line 801 and revision-log line 2038 (sec:79.14): "until then no lenders' adviser is named"; "does not yet exist in the Case Bible".
  - `bible/briefs/u10.md` line 1174 (sec:48.8): "Ridgeway's team unnamed".
- **Defect:**
  - The Case Bible v1.2 Part 6 assigns these characters to exactly these sections:
    - row 64 names Mereweather (ssec:64.14.5), Thevarajah and Tanaka-Bell (ssec:64.14.1);
    - row 79 names Tanaka-Bell (sec:79.14) and optionally Varga;
    - D-119 places Elspeth Varga in Chapters 45, 48 and 64.
  - The briefs tell writers the opposite. As written, the restructuring negotiation, which is the scene Section 5's "every seat" requirement most needs, has no lawyer's seat. This reopens round-1 defect 10 in the chapters that matter.
- **Fix:**
  - **u13 sec:64.14 beat (line 1425):**
    - Add to Characters: Lachlan Mereweather (Galbraith Stowe, lenders' counsel; drafts the restructuring support agreement and argues the cram-down at the November 30, 2023 sanction hearing, ssec:64.14.5); Anjali Thevarajah (Dunmore Pryor, counsel to the concessionaire and its shareholders, ssec:64.14.5); Rhys Tanaka-Bell (Calder Hartmann, lenders' monitoring adviser, ssec:64.14.1, reporting the 2019 to 2020 shortfall); Elspeth Varga (Ridgeway, author of the 2023 restructuring traffic case, ssec:64.14.4).
    - Each character gets the verbal habit and "where wrong" note from Annex TR T.18 and T.19.
    - Delete the sentence "Case T has no lenders' counsel ... no character is invented."
  - **u16 sec:79.14 (line 801):** name Rhys Tanaka-Bell as the lenders' seat in the narration (one or two lines; Annex TR T.18). Allow Varga's counts as optional per Part 6 row 79. Close revision-log item 2038.
  - **u10 sec:48.8 (line 1174):** replace "Ridgeway's team unnamed" with "Elspeth Varga (Ridgeway, author of the 2014 banking case; Annex TR T.19)".
  - **u09 sec:45.10:** add Varga, which D-119 also lists for Chapter 45.

### N3. Twelve fact sheets delivered after round 1 are unplaced, and the plan and D-122 still call them undelivered (major)

- **Location:** `bible/tracker.md` lines 117 to 118 ("All requested fact sheets delivered (172 files)"); `bible/fact-sheet-plan.md` lines 87 to 89 ("160"), 269, 274, 275, 384 to 407, 515, 617 ("none yet (round 2 placement)"); `bible/decisions.md` D-122 ("in progress ... cited only after the editor marks them delivered"); briefs u13 (lines 565, 652, 1971), u14 (ssec:84.3.5), u16 (lines 1360, 1636); u13 Ch 61 and u16 Ch 83 for the sheets no brief cites.
- **Defect:** The sheets that close round-1 defects 4 (WtE), 5(3), 8 and 9 now exist in `facts/` but are neither placed in a brief nor marked delivered:
  - `wte-operating-pf`: Dublin Poolbeg, an operating project-financed EfW plant.
  - `subsea-cable-pf`: EASSy and WIOCC.
  - `t-repowering`.
  - `t-earned-value`, `h2global` and `saf-mandates`: no brief cites them.

  As a result, the WtE financing-terms cell (Fn) and the subsea landmark remain empty, and writers following the briefs are told the sheets do not exist. Under D-122 they may not cite them until the editor marks them delivered, and no record does so. The plan also contradicts itself (t-repowering is both "Not delivered; commission" and "In progress"). Its line 401 expects t-sustainable-finance-2 to cover non-EU taxonomies, which it does not.
- **Fix:**
  1. Add a decision D-1xx marking the twelve D-122 sheets as delivered. Update `fact-sheet-plan.md`:
     - the header count reads 172;
     - lines 269, 274 and 275 change to "Delivered";
     - the open-requests table (lines 384 to 407) changes to "Delivered";
     - the citation-scan rows give the placements below.
  2. Place the sheets:
     - **`wte-operating-pf`** in u16 ssec:81.7.1, as the verified WtE financing (terms attributed and dated). Add it to the real-case row of sec:81.4 as the operating counterpart to Willows. Delete the "until it exists" sentence at u16 line 1360.
     - **`subsea-cable-pf`** in u16 ssec:82.3.4, as the verified DFI-financed consortium cable, kept beside Example 82.3. Delete the "until it exists" sentence at line 1636.
     - **`t-repowering`** in u13 ssec:62.8.1 and ssec:65.4.1, covering the US 80/20 rule, RED III repowering permitting, IEC TS 61400-28 life-extension assessment and lender consents. The R1 figures in sec:65.8 stay Case R model outputs. Delete the "not delivered" text at u13 lines 565, 652, 1795 and 1971.
     - **`t-earned-value`** in u13 sec:61.x, where eq:61.3 (earned value, style sheet A.5a) is taught, for the standard's origin only.
     - **`h2global`** in u16 Ch 83's hydrogen revenue-support subsection.
     - **`saf-mandates`** in u16 Ch 83's sustainable-fuels revenue subsection.
     - **`kenya-steam-sales`** is already cited in u15 Ch 72; confirm it is in ssec:72.5.5.
  3. Change fact-sheet-plan line 401 to say that t-sustainable-finance-2 covers EU gas criteria, ISSB, NGFS, the Climate Bonds Standard and CBAM, but no non-EU taxonomy. ssec:84.3.5 keeps its concept-level fallback.

### N4. The fact-sheet plan's delivered-sheets table header undercounts (minor)

- **Location:** `bible/fact-sheet-plan.md` line 89 ("One row per file actually delivered (160)").
- **Defect:** `facts/` holds 172 sheets. Every slug appears somewhere in the plan, but the header count and the "Delivered" table predate the fourth wave.
- **Fix:** Regenerate the table with all 172 rows and the count 172 when making fix N3(1).

### N5. Matter 93 and the coverage table do not record that airport charges have no clause (minor)

- **Location:** `bible/briefs/u05.md` line 2060; `bible/briefs/u17.md` coverage table, row D.
- **Defect:** The u05 reviser declined an airport-charges clause, which is acceptable because the round-1 required fix did not ask for one. However, the Section 4.D statement "original illustrative clause language" for "airport and port revenue models" is now met for ports only (cl:21.8), and no coverage record says airport charges are taught by Example 21.8 and the H7 anchor instead.
- **Fix:** In u05's coverage-check bullet (line 1644), add: "airport charges: no clause; taught by Example 21.8 (dual till) and the H7 settlement; the port MAG clause cl:21.8 is the clause for airport and port revenue models". Alternatively, add `cl:21.10`, an airport charges and till-basis clause (Illustrative; airline-, lender- and airport-friendly variants), appended so that no label moves.

## Fresh audit: items rechecked with no defect

- **Section 4 A to T homes:** unchanged from round 1. Every bullet has a home chapter, and items D, F (ratings), I, J (ISDA), P, Q (taxonomies) and T (request lists) now show Full or the agreed fallback.
- **Section 7 candidate cases:** all 35 retain registered sections. The 99 section labels cited in the round-1 table were checked against `anchor-registry.md`, and none is missing. Jubilee, Lekki, LaGuardia, Manila Water, Snowy 2.0, Coral Sul, TAP, Greenlink and Vineyard Wind are added.
- **Section 5:**
  - Case P now meets interest-rate and currency hedging.
  - Case T has all seven seats in the Case Bible (the brief gap is N2).
  - Case R requirements are unchanged and met.
- **Newly registered labels:** these exist in the registry: ssec:76.8.5, ssec:51.5.5, ssec:84.3.5, ssec:82.3.4, exh:30.4, exh:37.13, exh:59.12, exh:47.10, exh:48.10 to 48.13, exh:49.7 to 49.12, exh:50.6, cl:51.7, and the new Ch 21 and 23 to 26 clauses.
