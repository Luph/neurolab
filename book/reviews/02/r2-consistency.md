# Chapter 2 review, round 2: consistency

File: `chapters/02-what-project-finance-is.tex` (revised per `reviews/02/r1-revision.md`). Checked against the round-1 report, `bible/anchor-registry.md`, `bible/glossary-canon.md` (including the new "separateness undertaking" row), `bible/style-sheet.md` (with Addendum), `bible/decisions.md` (D-126, D-127), the Case Bible, Annex P and the Case P case state.

## Verdict: FAIL

Twenty of the 23 round-1 defects are fixed outright and the other three are partly fixed. The revision also introduced a few new problems. One of them is a running-case continuity error: Mariama Talmé is called the head of Groupe Talmé in 2015, but the Case Bible makes her deputy chief executive until 2021. Six defects remain, five in the chapter and one in the brief. All are one-line fixes.

## Build

`bash scripts/build_chapter.sh chapters/02-what-project-finance-is.tex`: BUILD OK, 51 pages. There is one overfull box, 0.27pt at source line 751 (Solution 2.9 `align*`). It is under the 5pt limit, so no action is needed. The only undefined references are cross-chapter ones. No errors.

Scripted checks:
- All 96 distinct `\cref` targets resolve in the registry, including about 30 labels new in this revision (for example `ssec:7.4.1`, `ssec:16.9.1`, `ssec:52.3.1`, `ssec:67.2.1`, `ssec:72.3.2` and `sec:82.9`). Each one points at a section whose registry title matches the use.
- All section and subsection titles match the registry, including the retitled `ssec:2.4.3`.
- All example, exhibit and clause captions match the updated registry rows. `cl:2.2` is now registered.
- Every canon term homed in Chapter 2 is bolded once, now including "separateness undertaking", and its definition matches the new canon row.

## Round-1 defects: status

| R1 | Status |
|---|---|
| 1 Registry rows ex/exh 2.1–2.3 | Fixed (registry lines 336–343 recaptioned with "was" notes) |
| 2 `cl:2.2` registry row | Fixed (line 345) |
| 3 Ch 4 brief cites ex:2.3 for soiling | Fixed (u01.md line 1153 now `ex:2.2`). Related leftover: see defect 6 |
| 4 Hand-typed chapter references | Fixed (line 9 and the exh:2.1 source; note split out) |
| 5 Vague "above/below" references | Fixed (lines 193 and 551 cite `ex:2.2`; the "fit test below" sentence is gone) |
| 6 Yieldco reference | Fixed (`sec:32.7`; `ssec:63.7.3` added) |
| 7 ssec:82.7.2 described wrongly | Fixed (line 398) |
| 8 Hyperion reference | Fixed (`sec:82.9`) |
| 9 Contingent equity and financial completion homes | Fixed (`ssec:32.3.3`, `ssec:26.5.2`, "commercial" added) |
| 10 Exhibit 2.2 "Home chapter" column | Fixed ("Taught further in"; row 1 `--`; `sec:75.3`) |
| 11 Exhibit 2.2 source line | Fixed (line 261) |
| 12 Clause 2.1 dated 2024 | Fixed (line 69: "was preparing to finance in 2024") |
| 13 Kilnworth project-finance history | Fixed (line 516) |
| 14 Separateness undertaking | Fixed (canon row added; bolded at line 65; no meta clause) |
| 15 Canonical party names | Mostly fixed. One "the operator's" remains (defect 5) |
| 16 Acronyms | Fixed for COD, O&M, LNG, PPA and EPC; SPA no longer used. New acronyms DSRA and ECAs are each used only once (defect 4) |
| 17 "near 5x" | Fixed (4.94x) |
| 18 "about" before sourced figures | Mostly fixed. Two remain (defect 3) |
| 19 USD/MMBtu format | Fixed |
| 20 Sub-million amounts | Fixed under D-126 (no "thousand" left; Llano Pardo prose in USD million) |
| 21 Table font sizes | Fixed |
| 22 `\raggedright` in sources | Fixed |
| 23 `\USDm` | Not applied. The writer's reason (a trial of tied spaces produced three overfull lines) is accepted; no further action |

## Defects

1. **Mariama Talmé is given the wrong role in 2015 (sec:2.9, line 470).** The chapter has "Groupe Talmé, the family group whose head, Mariama Talmé, had made that call". The Case Bible (Mariama Talmé character sheet) says she was Deputy Chief Executive of Groupe Talmé from 2008 to 2021. Her father, the founder Ousmane Talmé, led the group until he retired to the chairmanship in 2021. Required fix: "Groupe Talmé, the Dabakro family conglomerate whose deputy chief executive, Mariama Talmé, had made that call".

2. **Wrong tense for the Case P sell-down (ssec:2.5.1, line 299).** The chapter has "as Case P's Kilnworth will when, in 2026, it sells part of its stake". The book's present is October 2026, and the sale completed on September 30, 2026, after which Kilnworth stopped consolidating the project company (Case Bible, 2026 sell-down entry). Required fix: "as Case P's Kilnworth did when it sold part of its stake in 2026 (\cref{ch:66})".

3. **Two sourced real-world figures still carry "about" (style sheet 2.3 and 9).** Line 5: "About USD~3.8 billion of SunEdison's consolidated debt" should read "Approximately USD~3.8 billion". Line 311: "covering about 67\% of the project financings" should read "approximately 67\%". The other uses of "about" in the chapter are attached to illustrative figures and are correct.

4. **Acronyms defined but never used again (style sheet 8.1: do not create an acronym used fewer than three times).** Line 307 defines "debt service reserve account (DSRA)", and DSRA appears nowhere else in the chapter. Line 401 defines "export credit agencies (ECAs)", and ECA appears nowhere else. Delete " (DSRA)" and " (ECAs)". SPV (the canonical abbreviation at its home definition) and PPP (narration plus the dialogue's "PPP Unit") can stay.

5. **One non-canonical "operator" remains (ex:2.2, line 188).** The chapter has "a dust year twice as bad would threaten the operator's solvency". It should read "the O\&M operator's solvency" (style sheet 8.2).

6. **The Chapter 2 brief contradicts the registry (coordinator; not a chapter edit).** In `bible/briefs/u01.md`, the following still carry the pre-renumbering labels and captions:
   - the example list in Chapter 2 brief §2.6;
   - the walkthrough artifact in §2.7 ("Exhibit 2.2 (`exh:2.2`) ... (Example 2.1)");
   - the framework demonstration lines in §2.8 ("Demonstrated in Example 2.2");
   - the anchor table in §2.14;
   - the Exercise 2.8 answer in §2.13 ("151.9 then 97.4").

   The registry header declares the briefs authoritative, so a later writer or reviewer could act on the stale numbering. Required fix: update those entries to the registry's numbering (`ex:2.1` recourse ladder, `ex:2.2` soiling, `ex:2.3` two ways to fund; `exh:2.1` ring-fencing, `exh:2.2` neighbors, `exh:2.3` board paper; Exercise 2.8 answer "151.9 before and after completion; 155.8 to completion and 97.4 after had no overrun occurred"). Also note the revised wording of `fw:pf-fit-test` in the brief §2.8 and in any citing brief (Chapter 85), as the revision log asks.

## New material checked and found consistent (no action)

- The Alto Huelén PPA (15 years, US dollars, a BBB- copper miner, 80% of output) is used consistently in Example 2.1, Step 4 and the drill. It is not placed in a real auction, which complies with D-127.
- The overrun-cap redesign uses the same figures in Example 2.3, Steps 1, 2 and 4, Exhibit 2.3, the drill and Solution 2.7: cap 29.2, 3.49x, headroom 1.2, worst case 126.6, standby 29.2 and 25.3.
- The Llano Pardo figures under D-126 are 0.41, 0.44, 0.59, 1.82/1.38, 7.25/7.84, 16.3, 32.9, 48.8, 49.1, 65.1 and 1.1. All agree with u01 §1.A, and the firmware detail (11% of trackers for 23 days in March) agrees with §1.A.10.
- The Case P narration agrees with the Case Bible and Annex P: 70:30 Phase-2 cost sharing and the same equity split; the March 2015 Emergency Power Plan; the PPP unit in the Ministry of Economy and Finance; 2016 procurement; a government guarantee; Kessaran security law and the trust; the committee members and their verbal habits used once each; USD 12 million raised to 14.8 million; the 75% gearing reference to `ssec:8.2.1`; Solution 2.13's "70% partner".
- New canonical terms are glossed in plain words with references to their homes, and none is bolded: balance sheet, going concern, credit rating and investment grade, bond, margin and reference rate, fee letter, credit enhancement, structural subordination, term loan B, take-or-pay, lump-sum turnkey, liquefaction train and LNG, PPP unit, and force majeure.
