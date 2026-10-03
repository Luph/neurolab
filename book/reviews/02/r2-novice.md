# Chapter 2 review, round 2: novice reader

Reviewer role: novice (standards §12.2). I know only what Chapter 1 teaches, as set out in the Chapter 1 brief (u01.md, Sections 1.A and 1.3 to 1.12). I checked the revised `chapters/02-what-project-finance-is.tex` (844 lines) against my round-1 report and against the writer's log (`reviews/02/r1-revision.md`), then read the chapter straight through again. Line numbers refer to the revised file.

## Verdict: FAIL (narrowly)

All 28 round-1 defects are fixed. The chapter now reads cleanly for a reader starting from zero. The new material added in the revision (the overrun-cap analysis, the sizing contrasts, the Moody's default curve, and the simplifications paragraph) brought in five small gaps of the same kind I flagged in round 1. Each gap needs one clause to fix. Because this is the pilot chapter, I am holding it to the full standard: it passes once these five fixes are made.

## Round-1 defects: verification

| # | Status | Where fixed |
|---|---|---|
| 1 | Fixed | Chapter 11 (l.3); going-concern note (l.96); creditors' committee (l.96); "bankruptcy estate" removed |
| 2 | Fixed | Consolidated balance sheet (l.3); substantive consolidation defined (l.86) and reused (l.94, l.96); accounting sense restated (l.299) |
| 3 | Fixed | Balance sheet glossed at first use (l.3, with `\cref{ssec:7.4.1}`) |
| 4 | Fixed | Notes, bonds, senior and indenture (l.92) |
| 5 | Fixed | Ratings paragraph (l.112), placed before Sabine Pass and the Case P scene |
| 6 | Fixed | LNG (l.26, l.199); trains (l.199); Henry Hub and MMBtu (l.201); lump-sum turnkey (l.203) |
| 7 | Fixed | Capacity and energy payments (l.171); reused at l.201 |
| 8 | Fixed | Take-or-pay named and defined (l.201); reused at l.403 |
| 9 | Fixed | Defined-term convention (l.69); Facility Agent, Affiliate, Subsidiary, Project Documents, indemnity and basket (l.80 to l.83) |
| 10 | Fixed | Subordinated (l.81); structural subordination (l.233) |
| 11 | Fixed | Tranching and credit enhancement (l.239); concrete examples given |
| 12 | Fixed | Example 2.2 now uses the revenue shortfall, says the split between causes is unknown, and gives an indicative cap range (l.182 to l.190) |
| 13 | Fixed | Force majeure and deemed payments (l.193) |
| 14 | Fixed | Reference rate, margin and credit spread (l.360); prospectus (l.329); fee letter (l.385) |
| 15 | Fixed | 70:30 split assigned, ownership follows it, Groupe Talmé identified (l.470); Solution 2.13 says "as the 70% partner" |
| 16 | Fixed | Revolver and kilowatt-month (l.512); PPP unit (l.470) |
| 17 | Fixed | Lien ranking, ECAs and cell-production GWh (l.401, l.403) |
| 18 | Fixed | Cumulative default rate, Basel definition and ultimate recovery (l.311) |
| 19 | Fixed | l.307 |
| 20 | Fixed | l.299 |
| 21 | Fixed | Geotechnical baseline report glossed (Solution 2.3); perfection replaced by a gloss (Solution 2.11) |
| 22 | Fixed | Exercise 2.12 allows "cannot be determined"; solution cells now match the text (l.92 and l.241 supply the facts used) |
| 23 | Fixed | Exercise 2.4 reworded |
| 24 | Fixed | GLA and Alto Huelén introduced before Clause 2.1 (l.69) |
| 25 | Fixed | l.9 |
| 26 | Fixed | l.40 |
| 27 | Fixed | Trust glossed (l.514) |
| 28 | Fixed | Exhibit 2.2 now reads "Holding-company loan" |

## New defects

1. **ssec:2.3.2, line 193: "a parent guarantee, a bank bond, or insurance" uses "bond" in a second, undefined sense.** At line 92 the reader learned that a bond is a tradable loan sold to investors. Here "bond" means a bank's guarantee of a contractor's performance. A novice will read it as a loan and the sentence will make no sense. Fix: write "a bank guarantee (in construction usually called a performance bond, \cref{ch:22})", or replace "bank bond" with "bank guarantee".

2. **Line 381, with an earlier use at line 219: "a bullet bond with an amortizing loan" uses two repayment terms the reader has not met.** Line 219 already says "the loan usually amortizes". Chapter 1 shows installments only as "sculpted repayment", so neither "bullet" nor "amortize" has been introduced. Fix: at line 219, gloss amortizes ("repaid in installments over the asset's life"). At line 381, write "a bullet bond, repaid in one sum at maturity, with an amortizing loan, repaid in installments". Line 233 ("a single repayment at maturity") can then use the word "bullet".

3. **ssec:2.5.2, line 311: "resembled those of high speculative-grade borrowers and fell toward single-A levels" uses grades the reader cannot place.** The ratings paragraph at line 112 gives only the investment-grade threshold (BBB-/Baa3). The reader does not know that A ranks above BBB, or what "high speculative-grade" means on the scale. Fix: add one short sentence to the line 112 paragraph: "The grades run from AAA at the top through AA, A and BBB, then BB and below". At line 311, write "resembled those of borrowers rated around BB, the top of speculative grade, and fell toward the level of borrowers rated A". Check the exact grade wording against the Moody's source.

4. **Exhibit 2.3, lines 449 and 465: the after-COD project-finance leverage stays at 3.33x, but the note says GLA's covenant "counts only dividends received".** A novice who follows the note expects dividends from the wind farm to raise GLA's EBITDA after COD, and so to lower its leverage below 3.33x. The table shows no change and nothing explains why. Fix: add to the note "No dividends are assumed in the first year after COD, so after-COD leverage is shown unchanged; distributions from the wind farm would lower it." Alternatively, state the assumption at line 288 in Example 2.3.

5. **Section 2.9: "PPP unit" in the narration (line 470) becomes "PPP Unit" in Tomasz's line (line 493).** The capital letter makes the dialogue look like a different, named body, and the narration gave no proper name. Fix: use one form in both places. The Case Bible name is "Unité des Partenariats Public-Privé (PPP Unit)". Either give that name at line 470 and keep "PPP Unit" throughout, or lowercase the dialogue.

No other step blocked me. The worked examples, the walkthrough, the Case P installment, the drill and the exercises can all be followed using only Chapter 1 and the glosses this chapter now provides.
