# Chapter 36 review, round 2: consistency

Reviewer role: consistency. File: `chapters/36-sizing-and-sculpting-debt.tex`, revised per `reviews/36/r1-revision.md`. Checked against the anchor registry, glossary canon, ownership rulings, Case Bible Parts 1.6, 5A and 6, Annex P, the regenerated Case P ledger (model v1.5), decisions D-126 to D-139, and the style sheet.

**Verdict: FAIL.** The round 1 defects are fixed, apart from parts of 19 and 20 (see below), and the chapter now matches the v1.5 ledger. Five small new or residual chapter defects remain, and two of them involve teaching layouts and running-case dates.

## Build

`bash scripts/build_chapter.sh`: BUILD OK, 55 pages, 0 overfull boxes. There are no LaTeX warnings except the expected undefined cross-chapter references, and each of those is present in the registry. There are 14 underfull `\vbox` warnings from `[H]` floats; they are cosmetic, so check page white space at integration. Every Chapter 36 label prints its own number (`.aux` check). Every label is in the registry, including `cl:36.1` and eq:36.5 to eq:36.7 in their new order. No `\tag` remains.

## Round 1 defects: status

| # | Status |
|---|---|
| 1 Equation order | Fixed. The chapter prints 36.1 to 36.7 in order, and the registry (rows, A3), R-005 and R-116 are updated. The u08 brief is only partly updated; see central flag C1. |
| 2 Production references | Fixed. No D-numbers, Annex, Case Bible or slug references remain in reader text, and figure IDs appear only in `%` comments. |
| 3 FC-base PPA expiry and tail | Fixed: April 30, 2046 and about 11.8 years, with the exhibit source line matching. |
| 4 ch:64 | Fixed: the reference is now `\cref{ch:62,ch:63}`. |
| 5 Pro rata contradiction and unledgered figures | Fixed. The structure now follows D-128 (the covered tranche repays in equal installments; the other tranches are sculpted). Every Case P number checks against the v1.5 ledger: 629.9, 630.1, 638.4, 643.1, the slacks 0.2, 8.5, 13.1 and 11.0, 854.6, 640.9, 857.4, the tranches, 73.7%, WAL 6.92, 8.17 and 7.79, 13.16 years, 3.8%, 11.5%, 530.5 and 99.5, 1.55x, 1.39x and 1.35x, the P-F36 grid, and 1.28x at COD. One sweep date is wrong; see new defect 2. |
| 6 Negotiation length | Fixed: "15 weeks". |
| 7 Names | Fixed. The chapter uses Tamsarit Hydro (the rename decision is D-136, which Part 5A now cites), Campo Albarrán Solar, Shofirkon Sun Power and Kenogami Justice Partners. Every Chapter 36 name is registered in Part 5A, row 1122, with its check status, and no other file uses the new names. |
| 8 Canonical terms and spellings | Fixed: unitary charge, contracting authority and American spellings. One generic "borrower" remains at line 416; see new defect 5. |
| 9 Abbreviations | Fixed for the listed items. Two small residues remain (new defect 4). |
| 10 Forward references | Fixed. |
| 11 Real-case cross-references | Fixed (ssec:14.12.3, ssec:21.7.2, ssec:14.12.2, ssec:11.3.3). |
| 12 cl:36.1 | Fixed: registered and labeled. |
| 13 Excel for eq:36.4, 36.6, 36.7 | Added. The new Sizing-sheet layout collides with itself; see new defect 1. |
| 14 Case P workbook collision | Fixed: the block now sits on a standalone Sizing sheet, and sec:42.2 is described as the Case P live sculpting check. |
| 15 Empty cells and the LLCR column | Fixed. No empty table cells remain. The Exhibit 36.8 note now lists the notional balances. |
| 16 Number formats | Fixed. |
| 17 USD equivalents and nominal basis | Fixed. |
| 18 Unlocated exercises | Fixed: Oti Valley Power Company Ltd and Waalhaven Logistiek B.V., both 2026. |
| 19 GIIA citation | Fixed: GIIA n.d. |
| 20 LaTeX hygiene | Fixed. |
| 21 Close and Port Arthur repetition | Fixed. |

## Remaining defects

1. **The Sizing sheet's cell addresses collide with one another.**
   - Line 215 puts the constraint debts in F27 to F30, the lesser-of result in F32 and the flags in G27 to G30.
   - Line 533 puts contracted and merchant CFADS in rows 30 and 31 and their targets in F30 and F31. F30 is then both "fourth constraint debt" and "contracted target", and row 30 carries two labels.
   - Solution 36.15 (line 1100) uses a third layout: F27 to F29, the result in F31, and flags in G27 to G29. Its F31 also clashes with the merchant target in line 533.
   - Required fix: give the bucket block its own rows, for example contracted and merchant CFADS in rows 40 and 41 with targets in F40 and F41, and bucket debt service in row 43, which replaces row 12. Align Solution 36.15 with line 215: F27 to F29 hold the three amounts, F32 holds `=MIN(F27:F29)`, and G27 to G29 hold `=IF(F27=$F$32,1,0)`. Alternatively, state in the solution that the fourth constraint row, F30, is unused.

2. **The commercial-tranche sweep dates are wrong (Exhibit 36.13, line 799; narration, line 809).** The chapter says "Forecast cash sweep of the commercial tranche, 2027–2031" and "prepays part of the commercial tranche between 2027 and 2031". The ledger's period rows (P-F09, 2027H1 to 2032H1) show sweeps every half-year from 2027H1 to 2032H1. The last, USD 4.571 million on June 30, 2032, retires the tranche, whose opening balance is nil from 2032H2. Those rows sum to 99.488, the total the chapter prints.
   - Fix: write "2027–2032" in the exhibit row and "between 2027 and mid-2032, when the sweep retires the tranche" in the narration.
   - The sentence "although it amortizes fully on its schedule" should add that in the base case the sweep repays the tranche by June 30, 2032, two years before its scheduled final installment.
   - Ledger label error (central flag C3): the ledger's own total row is labeled "2027-2031".

3. **Characters and the sponsor appear without their roles in this chapter (sec:36.12).**
   - In the scene, only Tomasz is named. Pieter appears first in the narration after the box ("Pieter was wrong in 2016").
   - Kilnworth appears with no gloss ("Kilnworth's finance team").
   - Neither man's seat is stated anywhere in the chapter.
   - Fix: in the paragraph before the box, add one clause naming Pieter van Wijngaarden, Castellan Bank's lead arranger, and Tomasz Wierzbicki of Kilnworth Power International, the lead sponsor (Case Bible 4.1).

4. **Abbreviation residues.**
   - Lines 395, 410, 958 and 1069 write "the climate change sector understanding" in lower case, and lines 395 and 410 come before the expansion at line 588. The canon form is "Climate Change Sector Understanding (CCSU)". Expand it at line 395 with initial capitals and use "CCSU" afterwards.
   - "CPI-indexed" at line 332 is never expanded. Write "indexed to the consumer price index".

5. **Line 416 still uses "the days a borrower has to cure a missed payment".** Use "the days the project company has to cure a missed payment" (style 8.2).

## Central-file flags for the editor (not chapter defects)

- **C1. The u08 brief still carries the old equation numbers in two places.** Line 404 ("eq:36.5 is repurposed to 'Average-life constraint…'") and the line 723 anchor list (eq:36.5 = average-life, eq:36.7 = effective target) contradict the registry and the brief's own key-formula lines 729 and 731. Change both to the new numbering.
- **C2. The Case Bible repayment row is out of date.** Case Bible 1.6, "Debt sizing targets", Repayment row, still reads "all tranches pro rata on the common profile". That contradicts D-128, the v1.5 ledger (P-F09 repayment structure) and the chapter. Amend the row: the ECA-covered tranche repays 26 equal semiannual installments, and the other tranches are sculpted so that total scheduled debt service equals CFADS divided by 1.35. Also check Annex P 3.6 and the Chapter 42 brief for the same phrase.
- **C3. One ledger label is wrong.** P-F09 "Cash sweep prepayment total … 2027-2031" should read 2027–2032 (the last sweep is 2032H1, USD 4.571 million).
- **C4. The coordinator's v1.5 note disagrees with the regenerated ledger.** The note gives 535.287 and 94.662; the ledger gives 530.462 and 99.487. The writer's revision log already records this. The chapter follows the ledger, which is correct.
