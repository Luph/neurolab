# Blueprint review round 3: verification

Verifier: round-3 blueprint verifier (standards.md Section 11, Phase 1 item 8). Date: October 3, 2026.

Inputs read:
- The four round-2 reports: `r2-coverage.md`, `r2-capabilities.md`, `r2-sequencing.md` and `r2-standards.md`.
- The fixer's log `r2-fix-log.md`.
- In their current state: `bible/briefs/u01.md` to `u17.md` and the unit glossary files; `bible/*.md` (anchor registry, glossary canon, Case Bible and annexes, decisions, style sheet, fact-sheet plan, model requests, writer instructions); `facts/` (172 files); `model/figure-ledger-case-{p,t,r}.md`.

The Case P ledger in the working tree is the uncommitted model v1.5 (D-128). HEAD holds v1.4, which the round-2 fixes were made against. Both were checked (see D1).

## Verdict: PASS

- Every defect the round-2 reports left open is fixed in the current files: 34 new defects and 9 round-1 items marked partly fixed. No blocking or major defect remains open.
- This round found three new minor defects and one dependency:
  - two minor defects are listed below with exact fixes;
  - the trivial ones were fixed directly (section "Fixed directly in round 3");
  - the dependency is the pending Case P v1.5 cascade, which D-128 already tracks.

## Mechanical checks (scripts in the session scratchpad, re-run after the round-3 edits)

| Check | Result |
|---|---|
| (a) Figure IDs cited in briefs and `bible/*.md` against the three ledgers (107 IDs) | Every cited ID exists in both the v1.4 (HEAD) and v1.5 (working tree) ledgers. The only non-ledger token is the bare `P-F11`, which is used only where the text explains the P-F11a/P-F11b split. No defect. |
| (b) Every label token (`ch:`, `sec:`, `ssec:`, `ex:`, `exh:`, `cl:`, `eq:`, `fw:`, `exr:`, `fm:`) in briefs and `bible/*.md` against the registry (5,572 labels plus 1,391 expanded `exr:` labels) | 29 non-resolving tokens. All are placeholders (`sec:N.M`, `cl:N.Ka`, `fm:slug`, `ex:69.x`, `sec:89.x`), labels named as withdrawn (`cl:35.2c`, `cl:62.1a`, `cl:62.1b`, `cl:62.2`, `cl:62.2a`, `cl:62.2b`), the writer-assigned `exh:89.4`, or rulings and log text that quote the superseded `ssec:5.0`, `ssec:7.6.4` and `sec:6.x`. One live miss, "sec:79.4.4" in the u16 round-2 log (u16:2082), was corrected to `ssec:79.4.4`. |
| (c) Glossary-canon home labels | All 1,795 rows resolve, and every label in the Notes column resolves. The header count (1,793) was stale and is corrected to 1,795 (fixed directly). |
| (d) Heading scan over all 3,572 `ch:`/`sec:`/`ssec:` registry captions | 0 colon headings outside "Case P/T/R:" and "Walkthrough:". 0 formula headings ("reserved matters" in ssec:26.3.1 is a false hit). 0 question headings. 0 headings ending with a period. 0 British spellings. The only dash is the Chad–Cameroon en dash, which D-132/A.13 allows. Duplicates are only the fixed element headings, plus one registry truncation: ssec:2.4.3 read "Reserve-based lending" (a duplicate of sec:75.3), while the brief reads "Reserve-based lending compared with project finance". This was fixed in the registry. The brief TOC lines and anchor tables otherwise equal the registry captions, apart from reviser annotations. |
| (d') Non-heading captions (ex, exh, cl, eq, fw) | exh:61.7 "Anatomy of an independent engineer's monthly report" uses a banned formula ("The Anatomy of X"). It was recaptioned in the registry and in the u13 anchor table (fixed directly). Two captions begin with "Why": ex:1.3 and ex:9.6. ex:9.6 is the title form the style sheet's own sample (Section 12) uses, so neither is logged as a defect. |
| (e) Fictional names across briefs | 10 names are used for two or more different parties. See new defect R3-1. |
| (f) Recomputation of changed examples (Python) | 11 items, all match to printed precision. One text slip was fixed (Exercise 78.6 stub). See the table below. |

## Status of every round-2 defect

Severity is as rated by the round-2 reviewer. "r1" marks a round-1 item that round 2 found only partly fixed.

### Coverage (`r2-coverage.md`)

| # | Sev. | Defect | Status | Evidence in current files |
|---|---|---|---|---|
| N1 | major | KCR forward profile in Ch 37 and Ch 59 contradicts the ledger | FIXED | u08 Exhibit 37.13 and u12:1079 now read "one forward per monthly onshore EPC payment, August 2018 to November 2021". The last settlement is November 30, 2021, "almost a year before the queue began on November 7, 2022". No "semiannual forwards" and no "fifteen months" remain. The ledger has 40 monthly P-F65 rows, and P-F66 settles on 2021-11-30. |
| N2 | major | Case T counsel and adviser said not to exist | FIXED | u13 sec:64.14 (l.1425, 1432) uses Mereweather, Thevarajah, Tanaka-Bell and Varga. u16 sec:79.14 (l.801) names Tanaka-Bell, and the log item at l.2038 is closed. u10 sec:48.8 names Varga. u09 sec:45.10 adds Varga. No "no lenders' counsel", "no character is invented" or "team unnamed" text remains. |
| N3 | major | Twelve delivered fact sheets unplaced | FIXED | D-129. Each of the twelve slugs exists in `facts/` and is cited in its target brief: wte-operating-pf, subsea-cable-pf, h2global and saf-mandates in u16; t-repowering and t-earned-value in u13; kenya-steam-sales in u15; t-decommissioning-accounting in u02, u13 and u14; t-sustainable-finance-2 in u14; t-fast-standard, t-energy-yield and t-battery-degradation in u09. The "until it exists" and "not delivered" fallbacks are gone for these twelve. The fallbacks that remain refer to sheets that were never commissioned and are absent from `facts/`. The plan's line on non-EU taxonomies is corrected. |
| N4 | minor | Plan's delivered-table header undercounts | FIXED | The header says 172. The table has 172 rows, and its slug set equals `facts/` exactly (scripted diff). |
| N5 | minor | Airport charges have no clause and this is not recorded | FIXED | u05 coverage bullet (l.1644) carries the airport-charges note. |
| r1-5, r1-8, r1-9, r1-10 | — | Partly fixed in round 1 | FIXED | Closed by the N2 to N4 fixes. t-repowering is placed. The plan statuses read "Delivered (D-129)". |

### Capabilities (`r2-capabilities.md`)

| # | Sev. | Defect | Status | Evidence |
|---|---|---|---|---|
| 1 | major | Monte Carlo: two drivers in u09, four in v1.4 | FIXED | u09 0.4 (Inputs 311 to 312 and 313 to 1312, with draw-table columns for the four drivers), 0.5 (Ch 43 modifies), R5 (F312 active flag), 43.5.1 ("four in the companion", D-125), 43.J and Exercise 43.14. Case Bible Part 6 row 43 and Annex P now name all four drivers. No "availability and dispatch only" text remains. |
| 2 | minor | Exercise 43.14 targets a file that already holds its answer | FIXED | Ex 43.14 starts from `model/exercises/ex43_14/Ch43_start_no_mc.xlsx` plus `ch43_draw_table.xlsx`. Both are listed in R8 (u09:769). |
| 3 | minor | Model-request status stale | FIXED | `model-requests-round1.md` rule 5 and the Status column. u09 0.1 cites v1.4. |
| 4 | minor | Stale forward-reference hedge in u08 | FIXED | No "until it is registered" text remains in u08. |
| 5 | minor | fm:model-builds allows iterative calculation | FIXED | u17:1438 says supplied workbooks have "no iterative calculation ... no circular reference" (D-135). The capstone mention at u17:1554 concerns the reader's own model, which D-051 allows. |
| 6 | minor | "Kali Gandaki Hydro" twice and close to a real plant | FIXED | Renamed Himkiran Hydro (u09 Ex 39.9, 131 MW) and Tamsarit Hydro Pvt Ltd (u08 Ex 36.19), and registered in Case Bible 5A (l.1120 to 1121). D-136. |

### Sequencing (`r2-sequencing.md`)

| # | Sev. | Defect | Status | Evidence |
|---|---|---|---|---|
| 1 | major | Ch 8 P-F64 bridge contradicts ledger v1.4 | FIXED | u02:1169 and 1170 and Exercise 8.13 (l.1216) run the bridge from 16.0% to 13.3% with the ledger's nine steps. The values are +0.56, +0.44, −0.86, −0.14, −1.79, −0.05, −0.06, −0.79 and −0.05, total −2.73 pp with no residual. The capex step is −1.79 in ledger v1.4, so the reviewer's "−1.80" was a rounding of the cumulative difference. A clause says the ledger current at writing time governs. u10:125 lists the ledger's step categories. See D1 for v1.5. |
| 2 | minor | Ch 60 claims the subrogation home | FIXED | The u12 Ch 60 glossary row is gone. ssec:60.4.4 (l.1344) cites ssec:10.3.1 under R-030. |
| 3 | minor | Unit glossary files out of sync with the canon | FIXED | All 17 `uNN-glossary.md` files are now one-line "Superseded by bible/glossary-canon.md" pointers (D-130). |
| 4 | minor | Framework slug spelling | FIXED | Only `fw:integrity-check-catalog` occurs, in the registry, the canon and the briefs (D-137). |
| 5 | minor | Malformed labels | FIXED | fact-sheet-plan t-islamic cites `sec:53.8`. u16 log l.2051 cites `ssec:79.4.4`. The round-2 log line u16:2082 repeated the malformed form, and round 3 fixed it. |
| 6 | minor | Stale conditional instructions | FIXED | No "until the canon", "only after the canon" or "if adopted" text remains in any brief. `ssec:5.0` and `ssec:7.6.4` survive only in rulings, logs and "proposed as" notes. |
| 7 | minor | Clause-variant caption debris | FIXED | "clausevariants parent" occurs 0 times in the registry and in u10. cl:47.1 to cl:47.1c read as prescribed. |
| 8 | minor | Stale model-status notes | FIXED | The Annex P RORAC parenthesis is gone (l.677 now says only that RAROC is canonical). u12 Example 59.8 prints the P-F40 monthly set-offs (l.1699, 1706). u09 0.1 and the Case Bible cite v1.4. |
| 9 | minor | Annex P concordance lacks u13 | FIXED | Annex P l.1088: "u13 / 61 / P-F37 / EPC cumulative progress, planned and actual / P-F52". |
| 10 | minor | Writer instructions canon size | FIXED, then updated | The fixer's 1,793 was already off by one, and the Ch 36 review has since added a row. The table now has 1,795 rows, and the writer instructions and canon header are set to 1,795 (fixed directly). |
| r1-19 | — | P-F64 (partly fixed) | FIXED | See 1. |
| r1-23 | — | "SPA" for the share purchase agreement (partly fixed) | FIXED | u13 Walkthrough 63.9 and the u02 Ch 9 Case R scene read "share purchase agreement". Every remaining "SPA" in the briefs is the commodity sense or a rule statement. The canon definitions of "binding offer" and "permitted leakage" say "share purchase agreement". |

### Standards (`r2-standards.md`)

| # | Sev. | Defect | Status | Evidence |
|---|---|---|---|---|
| 1 | minor | Pronoun heading ssec:60.2.3 | FIXED | The registry and u12 read "Structuring a project against the obsolescing bargain". |
| 2 | minor | Registry caption debris (cl:47.1 group, ssec:84.3.1) | FIXED | The registry rows match the prescribed captions. The closing quotation mark on ssec:84.3.1 is restored. |
| 3 | minor | Six shared section titles and two shared captions | FIXED | The registry has sec:41.6, sec:51.3, sec:51.4, ssec:73.1.1, ssec:18.4.3, sec:60.7, ex:45.7 and exh:55.9 as prescribed (D-138), and the "Unresolved (1)" note records the resolution. A seventh duplicate, ssec:2.4.3/sec:75.3, was a registry truncation that round 3 fixed. |
| 4 | minor | Replacement figures recur across units | FIXED for the six named figures | 438.7, 403.7, 397.3, 438.9, 437.9 and 186.4 each now occur once as an input. Their other occurrences are change notes or logs. The u17:1195 hit is "1,186.4". The general rule the fixer added (D-134, A.11) is not yet met across the briefs: see new defect R3-2. |
| 5 | minor | Example 9.6 reprints the style-sheet sample | FIXED | Route (b), D-131: Souss Atlas Éolien, 117 MW, Guelmim, 2026, with fresh inputs, recomputed below. Style sheet Section 12 is marked "Format sample only" and carries no label. |
| 6 | minor | Round inputs in Ex 9.9 and Exercise 78.6 | FIXED | Both have lumpy inputs, recomputed below. |
| 7 | minor | Exercise 21.9 key truncated | FIXED | 11.582 (recomputed). |
| 8 | minor | En dash in ssec:75.5.2 | FIXED | D-132. Style sheet 3.1 and A.13 allow an en dash inside a proper name. |
| r1-14 | — | British spellings (partly fixed) | FIXED | No "programme" remains outside proper names and log quotations. No "tonne" remains outside "million tonnes per annum" and logs (D-133, A.12). |
| r1-15 | — | Serial commas (partly fixed) | FIXED | sec:17.9, sec:26.8 and ssec:25.7.3 carry the serial comma in the registry and the briefs. |

## Recomputation of changed items (Python)

All items were changed in round 2, according to the fix log. Each was recomputed from the brief's own inputs.

| Item (brief) | Key results checked | Result |
|---|---|---|
| Ex 9.6 (u02) | revenue 17.98; CFADS 12.57; DS 9.670; P90 318.2 GWh; 15.815; 10.405; DSCR 1.076 (1.08x); P90-sized DS 8.671; loss 0.999 | match |
| Ex 9.9 (u02) | E[p] 54.675; E[q] 407.85; 22.30; 22.14; cov −0.159; corr −0.98; reversed 22.46, +0.161, +0.997 | match |
| Ex 12.9 (u03) | 37.7 MW; 86.69 million m3; 313,809 MWh; 0.175; CRF 0.08658; capital 0.434; total 0.751; 23% and 58% | match |
| Ex 48.4 and Exercise 48.8 (u10) | life 13.44; 0.979 Mt; 866.1 kt; 64.43 kt/yr; tails 33.1%, 25.6%, 18.2%; 11.56 yrs and 22.2%; 14.71 yrs and 205.9 Mt | match |
| Exercise 46.10 (u10) | 3.35; 121.45; 83.55; wrong answer 132.2 | match |
| Ex 55.1 (u11) | fees 9.94; to sell 347.3; 6.46 (6.85%); hold 190.3 (2.02x); 7.42 (3.90%); 0.87; 5.59 (5.93%) | match |
| Ex 61.3 and Exercise 61.8 (u13) | 271.4; 241.6; SPI 0.890; 38.2 months; 12.3; 261.6; 0.964; 35.3 months | match |
| Ex 78.4 (u16) | life 13.34; max tenor 9.34; 32.5% at 9 years | match |
| Exercise 78.6 (u16) | 12.28-year life; 8.6 years; year 12 CFADS 264.4; year 13 250.4; stub 70.2; NPV 2,897.0; 31.9% and 24.9%; NPV tail 6 years | match. The text printed "0.28-year stub, 250.4 × 0.28 = 70.2", but 250.4 × 0.28 = 70.1. The answer uses the exact 0.2805-year stub (70.23), so the text was corrected to "0.2805-year stub (93.7 / 7.63 − 12), CFADS 250.4 × 0.2805 = USD 70.2 million". The answers are unchanged. |
| Ex 80.2 (u16) | residual 65.46; PV 14.90; annuity factor 12.663; rentals 33.29 and 34.46; difference 1.18 | match |
| Exercise 21.9 key (u05) | 7,670 × 1,510 = 11.582 | match |

## New defects

### R3-1. Minor: fictional names reused for different parties across chapters

- Rule: Case Bible Part 5A (l.1069) says names are registered "so that no name is used for two different parties".
- Method:
  - Every capitalized name ending in a corporate or asset suffix, or followed by "(fictional", was extracted by script.
  - Names appearing in more than one chapter were read in context.
  - Running-case parties and real names were excluded.
  - Same-deal reuse was accepted where the specifications agree: Sohar North Power (Ch 41 and 44), Kribi Bay Energy (Ch 41 and 43), Lagune Ébrié Power SA (Ch 38 and 60) and Tema Bay Power (Ch 43 and 49).
- Fix rule:
  - Keep the first party in book order.
  - Rename each later party to a new root, after the Part 5 web check.
  - Register every new name in Part 5A.
  - Change only the name, never the inputs.

| Name | Conflicting uses | Exact fix |
|---|---|---|
| Ventos do Seridó (Energia) SA | Exercises 22.6 and 22.11 (u05: 210 MW, COD 2027); Ex 25.4 (u06, 132 MW); Ch 52 example (u11, 164 MW); Ch 85 teaser (u17, 220.5 MW, with sponsor Seridó Renováveis Ltda) | Keep Ch 22. Rename the Ch 25, Ch 52 and Ch 85 parties to three distinct Brazilian names. In u17, rename the sponsor with its project, in the u17 name list and in Case Bible 5A.5. |
| Saguaro Flats Solar LLC | Ch 10 example (u03: 74 MWac, Pinal County, sold September 30, 2024 by Copperline to Redmesa); Ex 29.5 "Saguaro Flats Solar Holdings LLC" (u07:164, four plants); Ex 46.5 (u10:223, 140 MW, Maricopa, owned by Copperline in December 2026); Ch 62 example (u13:622, 147.5 MWac, Maricopa, financed 2021); Ex 70.4 (u15, construction started May 2026) | Keep Ch 10. Rename the parties in Ch 29, 46, 62 and 70. Copperline Renewables may stay as the Ch 46 seller of a different plant. |
| Brazos Bend (Power/Wind/Peaking) LLC | Ex 20.2 "Brazos Bend Wind LLC" (u05, 165 MW); Ex 30.2 "Brazos Bend Power LLC" (u07:502, 640 MW CCGT financed 2026); Ch 63 "Brazos Bend Peaking LLC" (u13:967); Ex 69.3 "Brazos Bend Power LLC" (u15:187, 620 MW CCGT operating in 2023) | Keep Ch 20. Rename the parties in Ch 30, 63 and 69 to distinct roots. |
| Bull Run Data Campus LLC | Ex 21.9 and Exercise 21.x (u05, 48 MW IT lease); Ch 82 example (u16, 96 MW IT build-to-suit, financed 2025) | Keep Ch 21. Rename the Ch 82 party. |
| Bukhara Quyosh Energy LLC | Ch 28 drill (u06:1412, 360 MW solar-plus-storage, signing October 28, 2026); Ch 36 drill (u08:673, 300 MWac solar) | Fixed in round 3. The Ch 36 writer had already registered "Shofirkon Sun Power LLC" (Case Bible l.1122) and used it in `chapters/36-sizing-and-sculpting-debt.tex`; u08 now uses it. |
| Llanos de Mérida Solar | Ex 24.4 (u06:395, 180 MWac, operating since 2021); Ex 36.11 and Exercises 37.11 and 37.14 (u08, 250 MWac, financial close 2025) | Fixed in round 3. u08 now uses the registered "Campo Albarrán Solar S.L.", as the Ch 36 draft does. |
| Mekong Delta Power | Ex 49.2 "Mekong Delta Power Company Ltd" (u10, 431 MW CCGT, Ba Ria-Vung Tau, operating); Ex 60.1 "Mekong Delta Power JSC" (u12:1394, 450 MW gas plant, 2026) | Rename the Ch 60 party. |
| Viento del Istmo S.A.P.I. de C.V. | Ch 13 drill (u03:1406, 297 MW, USD 410 million financing); Ex 55.3 (u11:1316, 280 MW, Juchitán, closes March 12, 2026) | Rename the Ch 55 party. Alternatively, set Ex 55.3 to 297 MW and state that it is the Ch 13 deal at close. |
| Ankobra Power Ltd | Ch 17 examples (u05:153, 320 MW open-cycle, Takoradi, financial close March 2018); Ex 66.8 (u14:207, "310 MW gas-fired IPP") | Either change Ex 66.8 to "the 320 MW open-cycle plant of Chapter 17 (Example 17.1)", which works because its ECL arithmetic does not use capacity, or rename it. |
| Tallo Bhir Hydropower Ltd | Ex 11.5 (u03:591, computed capacity 113.3 MW); Ex 48.1 (u10:1072, 96 MW) | Rename the Ch 48 party and update the Case Bible 5A row (l.1089), which currently records one name for both. |

The other six Ch 36 renames that the Case Bible registers (l.1122) were also missing from u08: Kenogami Justice Partners, Alto Lombada Eólica (Trás-os-Montes), Ventos da Chapada do Caju, Vía Norte Tepotzotlán, Catoctin Hollow Digital, Redfish Pass LNG Train 1 and Pecan Bayou Storage. They were synced in round 3 (see below). Prampram Power Ltd (u02 Ex 5.18) and Prampram Power Company (u09 Ex 40.4, 340 MW near Tema) are near-identical names. Fix: in u09 Ex 40.4, write "Prampram Power Ltd (the Example 5.18 plant)" or rename it.

### R3-2. Minor: rule D-134 and style sheet A.11 are not yet met by the briefs

- Defect:
  - Round 2 fixed the six figures that STD-4 named.
  - It also adopted a general rule: no illustrative input of three or more significant figures may appear in two different examples or exercises unless they treat the same deal.
  - A scan was run on four-significant-figure values of the form ddd.d. It covered example, exercise, scenario and input lines, and excluded running-case lines, logs and ban notes.
  - 141 values appear in two or more chapters. For example, 212.4 appears in six chapters as a basis, a CFADS, an opening balance and a debt balance; 248.6 appears as revenue and as capex; 148.6 appears as equity, plant MWac, debt and revenue.
  - Some hits are results, not inputs, or are same-deal continuations, so the list is a candidate list.
- Fix (choose one and record it in `decisions.md`):
  - (a) Amend D-134 and A.11 to say: "Inputs already in the briefs at round 3 are checked against the candidate list in `reviews/blueprint/r3-verification.md` Appendix A by the writer of the later chapter at drafting and by the Phase 4 numbers auditor; the later occurrence is changed and recomputed."
  - (b) Run a central de-duplication pass now over Appendix A, keeping the first occurrence in book order and recomputing the dependents.

  Route (a) is enough for a PASS because every brief already requires Python recomputation of any changed input.

## Dependency (tracked, not a blueprint defect)

### D1. Case P model v1.5 cascade (D-128)

- What changes:
  - The working-tree ledger is v1.5 (uncommitted), against v1.4 at HEAD. Values change under 39 IDs, and the briefs cite those IDs 679 times.
  - The briefs print v1.4 values in places. For example:
    - u02:1170 and Exercise 8.13: the P-F64 steps become +0.50, +0.45, −0.89, −0.13 and so on, with a total of −2.85 pp in v1.5;
    - u09 43.5.3 and Exercise 43.14: P-F42 equity IRR changes from 12.9/13.2/13.7% to 12.8/13.1/13.6% in v1.5;
    - u02 Ex 8.5: the P-F05 gearing table changes.
- Why it is not a blueprint defect:
  - Every such brief passage carries the "ledger current at writing time governs" rule (u02:1170; u09 0.1 item 5; writer-instructions item 6).
  - D-128 already records that the change cascades.
- Required when v1.5 is committed: repeat the round-2 regeneration for v1.5:
  - resync u09 Section 0.4 and the model-requests status column;
  - update the printed v1.4 values in u02 (Ch 8), u09 (Ch 43) and every other brief that prints a P-F value;
  - update the case-bible.md and Annex P version notes from v1.4 to v1.5.

## Fixed directly in round 3 (trivial, no substance changed)

1. `bible/anchor-registry.md` ssec:2.4.3: the caption is restored to the brief's "Reserve-based lending compared with project finance". The registry had truncated it, which duplicated sec:75.3. The drafted `chapters/02-what-project-finance-is.tex` still prints `\subsection{Reserve-based lending}`. The Ch 2 reviser should adopt the locked title.
2. `bible/anchor-registry.md` and `bible/briefs/u13.md` l.402, exh:61.7: "Anatomy of an independent engineer's monthly report" becomes "Parts of an independent engineer's monthly report". "The Anatomy of X" is a banned formula.
3. `bible/briefs/u16.md` l.2082 (round-2 log): "sec:79.4.4" becomes "ssec:79.4.4".
4. `bible/briefs/u16.md` l.540, Exercise 78.6: the stub arithmetic text is corrected. The answers are unchanged.
5. `bible/glossary-canon.md` header count is set from 1,793 to 1,795, the actual number of table rows. `bible/writer-instructions.md` item 5 is updated to 1,795.
6. `bible/briefs/u08.md`: the Ch 36 and Ch 37 party names are synced to the renames the Chapter 36 writer registered in Case Bible Part 5A (l.1122) and used in the drafted chapter:
   - Northshore Justice Partners becomes Kenogami Justice Partners;
   - Alto Minho Eólica S.A. (Alto Minho) becomes Alto Lombada Eólica, S.A. (Trás-os-Montes);
   - Ventos do Potiguar becomes Ventos da Chapada do Caju;
   - Libramiento Norte Edomex becomes Vía Norte Tepotzotlán;
   - Broadlands Digital becomes Catoctin Hollow Digital;
   - Matagorda Bay LNG Train 1 becomes Redfish Pass LNG Train 1;
   - Llanos de Mérida (Ex 36.11 and Exercises 37.11 and 37.14) becomes Campo Albarrán;
   - Bukhara Quyosh Energy becomes Shofirkon Sun Power;
   - Comal Storage becomes Pecan Bayou Storage.

   This closes two of the R3-1 clashes.

## Notes for the editor

- The fixer's "observed" clash (Quebrada Honda) is resolved: u10 now uses Minera Loma Cobrecita S.A.C. Case Bible 5A (l.1594) marks it "editor rename, not web-checked". The Ch 48 writer runs the check.
- The u02 round-1 revision table (l.1622) still says "Example 9.6 stays as the style-sheet sample". It is a historical log row, which D-131 and the round-2 log supersede. It was left unchanged.

## Appendix A. Candidate repeated inputs (four significant figures, ddd.d) across chapters (R3-2)

Each row gives the value, then each chapter where it appears with its first location (unit:line). Hits on results and on same-deal continuations are expected: the numbers auditor confirms each one.

| Value | Chapters (first location) |
|---|---|
| 212.4 | Ch 32 (u07:1105); Ch 36 (u08:591); Ch 37 (u08:931); Ch 40 (u09:1134); Ch 43 (u09:1765); Ch 78 (u16:460) |
| 118.4 | Ch 8 (u02:1143); Ch 30 (u07:506); Ch 51 (u11:149); Ch 60 (u12:1394); Ch 80 (u16:1051) |
| 148.6 | Ch 42 (u09:1558); Ch 45 (u09:2174); Ch 50 (u10:1953); Ch 54 (u11:1030); Ch 85 (u17:152) |
| 176.4 | Ch 11 (u03:587); Ch 16 (u04:1266); Ch 33 (u07:1394); Ch 38 (u08:1297); Ch 67 (u14:759) |
| 248.6 | Ch 7 (u02:846); Ch 13 (u03:1332); Ch 44 (u09:2023); Ch 51 (u11:164); Ch 67 (u14:621) |
| 318.6 | Ch 9 (u02:1499); Ch 15 (u04:758); Ch 19 (u05:806); Ch 22 (u05:1776); Ch 78 (u16:462) |
| 612.4 | Ch 17 (u05:234); Ch 18 (u05:565); Ch 38 (u08:1310); Ch 45 (u09:2181); Ch 48 (u10:1095) |
| 104.6 | Ch 11 (u03:610); Ch 19 (u05:812); Ch 26 (u06:945); Ch 82 (u16:1603) |
| 118.6 | Ch 29 (u07:162); Ch 38 (u08:1395); Ch 53 (u11:836); Ch 66 (u14:176) |
| 214.6 | Ch 23 (u06:145); Ch 51 (u11:239); Ch 68 (u14:1156); Ch 88 (u17:1202) |
| 236.8 | Ch 39 (u09:971); Ch 47 (u10:659); Ch 66 (u14:199); Ch 75 (u15:1967) |
| 312.4 | Ch 11 (u03:575); Ch 63 (u13:961); Ch 66 (u14:174); Ch 67 (u14:758) |
| 486.3 | Ch 15 (u04:715); Ch 56 (u11:1608); Ch 57 (u12:301); Ch 66 (u14:174) |
| 112.4 | Ch 23 (u06:143); Ch 58 (u12:586); Ch 64 (u13:1372) |
| 118.9 | Ch 42 (u09:1558); Ch 73 (u15:1398); Ch 80 (u16:1123) |
| 124.8 | Ch 23 (u06:220); Ch 54 (u11:1093); Ch 66 (u14:178) |
| 158.4 | Ch 20 (u05:1113); Ch 26 (u06:877); Ch 58 (u12:714) |
| 168.4 | Ch 25 (u06:638); Ch 36 (u08:700); Ch 43 (u09:1832) |
| 215.9 | Ch 2 (u01:733); Ch 4 (u01:1456); Ch 20 (u05:1117) |
| 236.4 | Ch 9 (u02:1423); Ch 51 (u11:237); Ch 52 (u11:562) |
| 236.5 | Ch 14 (u04:243); Ch 23 (u06:220); Ch 50 (u10:2099) |
| 243.5 | Ch 13 (u03:1338); Ch 16 (u04:1155); Ch 40 (u09:1133) |
| 247.6 | Ch 8 (u02:1135); Ch 18 (u05:563); Ch 38 (u08:1221) |
| 286.3 | Ch 62 (u13:617); Ch 80 (u16:1051); Ch 84 (u14:1529) |
| 312.6 | Ch 14 (u04:403); Ch 45 (u09:2174); Ch 76 (u15:2356) |
| 312.7 | Ch 53 (u11:778); Ch 57 (u12:171); Ch 76 (u15:2356) |
| 318.4 | Ch 53 (u11:839); Ch 56 (u11:1704); Ch 76 (u15:2268) |
| 386.4 | Ch 12 (u03:975); Ch 14 (u04:268); Ch 41 (u09:1342) |
| 386.5 | Ch 38 (u08:1288); Ch 71 (u15:904); Ch 82 (u16:1603) |
| 410.0 | Ch 14 (u04:401); Ch 16 (u04:1264); Ch 20 (u05:1201) |
| 416.9 | Ch 23 (u06:220); Ch 25 (u06:638); Ch 82 (u16:1681) |
| 418.6 | Ch 21 (u05:1434); Ch 55 (u11:1388); Ch 84 (u14:1420) |
| 486.2 | Ch 78 (u16:464); Ch 81 (u16:1323); Ch 83 (u16:2065) |
| 846.3 | Ch 27 (u06:1117); Ch 56 (u11:1598); Ch 58 (u12:713) |
| 100.0 | Ch 13 (u03:1340); Ch 41 (u09:1398) |
| 101.8 | Ch 23 (u06:137); Ch 41 (u09:1346) |
| 103.6 | Ch 23 (u06:209); Ch 66 (u14:178) |
| 108.3 | Ch 11 (u03:593); Ch 15 (u04:860) |
| 110.0 | Ch 13 (u03:1340); Ch 14 (u04:249) |
| 112.0 | Ch 32 (u07:1101); Ch 66 (u14:178) |
| 112.7 | Ch 47 (u10:638); Ch 80 (u16:1047) |
| 114.4 | Ch 36 (u08:692); Ch 78 (u16:460) |
| 118.5 | Ch 58 (u12:724); Ch 65 (u13:1764) |
| 120.7 | Ch 19 (u05:806); Ch 77 (u16:171) |
| 121.3 | Ch 1 (u01:457); Ch 58 (u12:714) |
| 121.9 | Ch 23 (u06:209); Ch 47 (u10:638) |
| 123.0 | Ch 1 (u01:382); Ch 8 (u02:1133) |
| 124.6 | Ch 1 (u01:384); Ch 19 (u05:814) |
| 126.0 | Ch 67 (u14:759); Ch 68 (u14:1149) |
| 127.5 | Ch 1 (u01:461); Ch 12 (u03:975) |
| 131.6 | Ch 61 (u13:186); Ch 80 (u16:1123) |
| 133.5 | Ch 19 (u05:810); Ch 22 (u05:2052) |
| 133.6 | Ch 19 (u05:810); Ch 22 (u05:2052) |
| 139.5 | Ch 80 (u16:1051); Ch 86 (u17:644) |
| 140.5 | Ch 3 (u01:1013); Ch 4 (u01:1456) |
| 143.8 | Ch 11 (u03:589); Ch 23 (u06:143) |
| 145.3 | Ch 8 (u02:1211); Ch 51 (u11:149) |
| 146.6 | Ch 51 (u11:237); Ch 75 (u15:1965) |
| 148.3 | Ch 53 (u11:778); Ch 68 (u14:1151) |
| 150.0 | Ch 16 (u04:1270); Ch 58 (u12:605) |
| 151.2 | Ch 15 (u04:860); Ch 51 (u11:149) |
| 151.6 | Ch 23 (u06:137); Ch 58 (u12:714) |
| 151.9 | Ch 2 (u01:725); Ch 58 (u12:714) |
| 154.8 | Ch 15 (u04:863); Ch 77 (u16:171) |
| 164.2 | Ch 58 (u12:724); Ch 75 (u15:1967) |
| 168.9 | Ch 20 (u05:1192); Ch 58 (u12:714) |
| 172.6 | Ch 18 (u05:491); Ch 19 (u05:879) |
| 173.5 | Ch 61 (u13:186); Ch 78 (u16:464) |
| 182.4 | Ch 2 (u01:654); Ch 14 (u04:242) |
| 185.3 | Ch 21 (u05:1386); Ch 78 (u16:405) |
| 186.0 | Ch 60 (u12:1396); Ch 63 (u13:983) |
| 186.2 | Ch 7 (u02:918); Ch 74 (u15:1762) |
| 186.3 | Ch 3 (u01:925); Ch 47 (u10:638) |
| 188.9 | Ch 47 (u10:659); Ch 81 (u16:1325) |
| 192.9 | Ch 57 (u12:175); Ch 75 (u15:1967) |
| 193.8 | Ch 8 (u02:1079); Ch 14 (u04:403) |
| 196.0 | Ch 57 (u12:295); Ch 58 (u12:605) |
| 196.5 | Ch 37 (u08:931); Ch 77 (u16:171) |
| 198.7 | Ch 19 (u05:879); Ch 45 (u09:2237) |
| 205.9 | Ch 19 (u05:879); Ch 48 (u10:1241) |
| 212.0 | Ch 75 (u15:1967); Ch 76 (u15:2272) |
| 212.7 | Ch 15 (u04:859); Ch 16 (u04:1401) |
| 213.4 | Ch 35 (u08:208); Ch 47 (u10:659) |
| 217.6 | Ch 17 (u05:161); Ch 88 (u17:1311) |
| 218.7 | Ch 9 (u02:1500); Ch 41 (u09:1401) |
| 227.5 | Ch 55 (u11:1378); Ch 71 (u15:824) |
| 227.6 | Ch 55 (u11:1378); Ch 72 (u15:1101) |
| 247.5 | Ch 63 (u13:988); Ch 76 (u15:2237) |
| 247.8 | Ch 23 (u06:207); Ch 61 (u13:186) |
| 248.7 | Ch 26 (u06:875); Ch 75 (u15:1967) |
| 256.9 | Ch 23 (u06:141); Ch 26 (u06:946) |
| 257.2 | Ch 2 (u01:733); Ch 4 (u01:1456) |
| 262.5 | Ch 20 (u05:1117); Ch 67 (u14:640) |
| 268.4 | Ch 21 (u05:1442); Ch 35 (u08:119) |
| 271.9 | Ch 13 (u03:1340); Ch 55 (u11:1388) |
| 273.8 | Ch 51 (u11:164); Ch 77 (u16:165) |
| 274.9 | Ch 19 (u05:806); Ch 23 (u06:220) |
| 281.7 | Ch 9 (u02:1499); Ch 11 (u03:593) |
| 286.4 | Ch 3 (u01:924); Ch 45 (u09:2237) |
| 287.4 | Ch 15 (u04:737); Ch 29 (u07:164) |
| 287.5 | Ch 64 (u13:1365); Ch 66 (u14:316) |
| 288.6 | Ch 36 (u08:504); Ch 85 (u17:299) |
| 289.1 | Ch 9 (u02:1499); Ch 17 (u05:170) |
| 296.8 | Ch 23 (u06:137); Ch 70 (u15:522) |
| 299.6 | Ch 23 (u06:220); Ch 69 (u15:187) |
| 312.0 | Ch 21 (u05:1428); Ch 66 (u14:178) |
| 313.2 | Ch 78 (u16:464); Ch 83 (u16:2065) |
| 318.2 | Ch 23 (u06:137); Ch 51 (u11:242) |
| 341.9 | Ch 36 (u08:691); Ch 45 (u09:2237) |
| 342.7 | Ch 9 (u02:1422); Ch 77 (u16:169) |
| 347.3 | Ch 19 (u05:810); Ch 55 (u11:1314) |
| 352.6 | Ch 9 (u02:1422); Ch 85 (u17:294) |
| 368.3 | Ch 11 (u03:589); Ch 53 (u11:838) |
| 373.1 | Ch 22 (u05:1840); Ch 77 (u16:243) |
| 374.7 | Ch 3 (u01:1013); Ch 4 (u01:1456) |
| 386.9 | Ch 59 (u12:1035); Ch 75 (u15:2060) |
| 388.4 | Ch 9 (u02:1501); Ch 19 (u05:806) |
| 402.3 | Ch 36 (u08:591); Ch 53 (u11:839) |
| 407.3 | Ch 22 (u05:1840); Ch 52 (u11:499) |
| 424.7 | Ch 9 (u02:1420); Ch 64 (u13:1451) |
| 447.9 | Ch 14 (u04:407); Ch 15 (u04:868) |
| 455.8 | Ch 36 (u08:591); Ch 74 (u15:1684) |
| 457.3 | Ch 53 (u11:776); Ch 64 (u13:1451) |
| 475.8 | Ch 9 (u02:1420); Ch 12 (u03:965) |
| 480.8 | Ch 19 (u05:810); Ch 23 (u06:220) |
| 483.7 | Ch 84 (u14:1528); Ch 87 (u17:883) |
| 499.5 | Ch 59 (u12:1014); Ch 80 (u16:1051) |
| 512.4 | Ch 36 (u08:565); Ch 45 (u09:2175) |
| 512.6 | Ch 20 (u05:1119); Ch 53 (u11:782) |
| 527.4 | Ch 14 (u04:281); Ch 16 (u04:1149) |
| 548.3 | Ch 17 (u05:234); Ch 61 (u13:213) |
| 607.4 | Ch 55 (u11:1320); Ch 75 (u15:1969) |
| 610.0 | Ch 14 (u04:401); Ch 67 (u14:642) |
| 617.4 | Ch 26 (u06:877); Ch 87 (u17:994) |
| 618.1 | Ch 78 (u16:464); Ch 83 (u16:2065) |
| 618.4 | Ch 16 (u04:1142); Ch 71 (u15:904) |
| 634.2 | Ch 33 (u07:1400); Ch 77 (u16:171) |
| 637.4 | Ch 57 (u12:184); Ch 82 (u16:1681) |
| 715.0 | Ch 76 (u15:2356); Ch 85 (u17:299) |
| 742.6 | Ch 47 (u10:659); Ch 73 (u15:1488) |
| 974.8 | Ch 82 (u16:1605); Ch 83 (u16:2065) |
