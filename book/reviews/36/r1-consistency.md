# Chapter 36 review, round 1: consistency

Reviewer role: consistency. File: `chapters/36-sizing-and-sculpting-debt.tex`. Checked against `bible/glossary-canon.md`, `bible/anchor-registry.md`, `bible/ownership-resolutions.md`, `bible/case-bible.md` (Part 5A, Part 6, Part 7), `bible/case-bible-annex-p.md`, `model/figure-ledger-case-p.md`, `bible/style-sheet.md` with its Addendum, `bible/briefs/u08.md` (Chapter 36) and the other unit briefs where they name the same parties or real cases.

**Verdict: FAIL**

## Build

`bash scripts/build_chapter.sh chapters/36-sizing-and-sculpting-debt.tex`: BUILD OK, 54 pages, 0 overfull boxes. The 52 undefined references are all cross-chapter (the script prints only the first 50). Every `\cref` target in the chapter was checked against the anchor registry, and all of them exist. Every Chapter 36 label prints the number it names in the `.aux` file. Residue in the log:
- One LaTeX warning: "Command \texttimes invalid in math mode on input line 1049" (defect 20).
- 10 underfull `\vbox` warnings on pages 10, 12, 28, 30, 31, 33, 34, 35, 40 and 45 (badness up to 10000). They come from `[H]` exhibits being pushed to the next page. They are cosmetic, but check these pages for large white gaps at integration.

## Defects

1. **Equation numbers print out of order (lines 217, 529, 578).** The three `\tag` commands print the equations as 36.1, 36.2, 36.3, 36.4, 36.7, 36.6, 36.5. That breaks anchor-registry rule 3 ("equations are numbered in order of appearance") and style sheet 3.2 ("the writer keeps them in order"). A tagged equation also reaches cleveref with counter value 2147483647 and an empty chapter prefix (`.aux` lines 65–66, 149–150, 165–166), so sorting and compressing in multi-target `\cref` lists is unreliable.
   - Fix: the editor-in-chief renumbers the registry in order of appearance:
     - `eq:36.5`: effective base-case target from a downside test (ssec:36.3.1).
     - `eq:36.6`: bucket sculpting (ssec:36.8.1).
     - `eq:36.7`: average-life constraint on a sculpted profile, citing eq:6.2 (repurposed, R-005). The "repurposed" note moves with this equation.
   - Then update the same equation names in R-005 and R-116 (`ownership-resolutions.md`), registry Section 2 row A3, and the u08 brief anchors and key formulas.
   - In the chapter, delete the three `\tag`s, relabel the equations, and update every `\cref` to them (lines 220, 277, 337, 539, 1008, 1020, 1049).
   - No other brief or chapter cites eq:36.5 to eq:36.7 (searched), so the change stays inside this chapter.

2. **Internal production references are printed for the reader.** The reader has no access to the decisions log, Annex P, the Case Bible's drafting history or the fact-sheet file names. Remove or replace each of these:
   - "D-013 arithmetic on P-F08" (line 771), "D-013 arithmetic on the input dates" (813) and "D-013 arithmetic on ledger values" (1096).
   - "Annex P~3.6" (811).
   - "An early draft of the Case Bible said the first repayment had to fall within six months of COD" (811). Delete it, and keep only the substantive point that six months is the Arrangement's standard rule outside the project finance terms.
   - "Case Bible inputs" (569, 813, 972) and "from the Case Bible" (807). Use "the Case P financing terms".
   - Fact-sheet slugs "t-market-norms and t-market-norms-2 fact sheets" (640, exhibit source) and "(t-market-norms; t-market-norms-2)" (1135). Cite the underlying sources by author and date.
   - Figure IDs P-F07, P-F08, P-F09, P-F36 and P-F43 in prose and in Exercise 36.13 (765, 769, 771, 773, 807, 811, 813, 833, 972, 1096). The reader cannot look these up. Point to Exhibits 36.12 to 36.14 instead, and keep exhibit sources in the style-sheet form "Case P reference model, FC base". Exercise 36.13 should read "Using Exhibits 36.12 and 36.13 and the Case P terms in Section 36.12". If the editor-in-chief wants figure IDs printed book-wide, that needs a ruling and a front-matter explanation.

3. **The PPA expiry date is mixed between two cases (lines 807, 813).** The chapter sizes on the FC base, where COD is May 1, 2021. It then measures the tail to the actual-run PPA expiry of November 30, 2046. Annex P's PPA table gives the FC-base expiry as April 30, 2046 (COD May 1, 2021) and November 30, 2046 only for the actual December 1, 2021 COD. In April 2018 the lenders were sizing against April 30, 2046.
   - Fix: use April 30, 2046 and a tail of "about 11.8 years" (June 30, 2034 to April 30, 2046), and correct the exhibit 36.13 source line to match.
   - Alternatively, say explicitly that 12.4 years is the tail after the actual delay, and move it out of the April 2018 narrative.
   - Flag to the editor: the u08 brief's "about 12.4 years" carries the same error.

4. **Line 813 cites the wrong chapter for Case P's later use of the tail.** It says the tail "gave the lenders room that \cref{ch:64} would later be glad of". Chapter 64's running-case installment is Case T only (Case Bible Part 6, row 64). Case P's lenders used the post-2034 room in two other chapters:
   - Chapter 62: the October 2023 waiver deferred 60% of the December 2023 installment.
   - Chapter 63: the 2025 bond matures on June 30, 2037, beyond 2034, with the ECA-covered and A-loan lenders consenting.
   - Fix: replace the reference with `\cref{ch:62,ch:63}` and name what happened.

5. **The chapter contradicts itself on pro rata amortization, and some figures have no ledger source.**
   - Line 741 says "Case P's tranches all amortize pro rata on one common profile". The note to Exhibit 36.13 and line 813 say the commercial tranche's sweep reduces that tranche's later scheduled installments, so scheduled principal adds to 538.2, not 633.3. Rewrite line 741: "amortize pro rata on one common scheduled profile set at close; from 2027 the commercial tranche is also prepaid by its sweep."
   - The writer computed several figures from ledger values rather than taking them from the ledger: the 9.0% repaid within 24 months (Exhibit 36.13), "about USD 95 million" of sweep (Exhibit 36.13 note), the 538.2 total, and the claim that the sweep is "largely" why the average DSCR is 1.54x. These go beyond D-013 arithmetic on inputs and Case Bible rule 1. Before print, either get ledger rows for them (a P-F09 extension: scheduled principal total, FC-base sweep total, share repaid within 24 months of COD) or delete them. The writer already raised this in the notes, and the editor must act on it.

6. **Line 707: "after nine weeks of concessions".** Annex P 1.15.2 dates Castellan's draft July 14, 2017, the concessions to August, September and October 2017, and the agreed term sheet to October 27, 2017. That is 15 weeks from the draft. Fix: "after fifteen weeks of negotiation from Castellan's July 14 draft", or drop the duration.

7. **Party names conflict with the name register (Case Bible Part 5A).**
   - (a) Exercise 36.19 (line 996) uses "Dhaulagiri Kholsi Hydro Pvt Ltd". Part 5A.3 already registers "Tamsarit Hydro Pvt Ltd" as the checked-clear replacement for "Kali Gandaki Hydro Pvt Ltd" in exactly this exercise. Use Tamsarit Hydro Pvt Ltd.
   - (b) "Llanos de Mérida Solar S.L." (Example 36.11, line 535; Exercise 36.5 solution) is already a different party in Chapter 24: Example 24.4 in the u06 brief, a 180 MWac Extremadura plant operating since 2021. The Chapter 36 party is a 250 MWac plant closing in 2025. Rename the Chapter 36 party, since its chapter comes later.
   - (c) "Bukhara Quyosh Energy LLC" (judgment drill, line 893) is already the project company in the Chapter 28 drill (u06): a 360 MW solar-plus-storage project in Bukhara Region signing on October 28, 2026. Chapter 36 makes it a 300 MWac solar plant going to credit committee in the same weeks. Rename the Chapter 36 party.
   - (d) "Northshore Justice Partners" (Example 36.1) shares a root with "Northshore Connector Partners" (Exercise 13.7, u03), another Canadian availability-PPP concessionaire. Part 5A's precedent (Lindqvist) renames the later one. Rename it.
   - (e) Ask the editor to register in Part 5A every name the chapter introduces, with its check status: Redfish Pass LNG Train 1 LLC, Catoctin Hollow Digital LLC, Pecan Bayou Storage LLC, Alto Lombada Eólica S.A., Ventos da Chapada do Caju S.A., Vía Norte Tepotzotlán S.A. de C.V., Wadi Hommath Wind SAE, Rioni Zemo Hydro LLC, Las Cumbres Salud S.A., Thar Rekha Solar Pvt Ltd, Pampa Clara Solar SpA, Cheviot Edge Wind Ltd, Toba Panas Bumi, Cap Vert Power S.A., and the replacements for (b) to (d).
   - The writer's other renames, made after a web check under the Part 5 rule, are consistent and accepted.

8. **Non-canonical terms and spellings.**
   - Line 23 "unitary payment" should be "unitary charge" (glossary, ssec:21.6.1; style A.3).
   - Line 23 "the public authority" should be "the contracting authority" (style 8.2 for PPPs).
   - Lines 415 and 486 "borrower" should be "project company" (style 8.2).
   - "panellist" (lines 563, 646) should be "panelist", and "cancelled" (line 458) should be "canceled" (American English, style 2.1).

9. **Abbreviations are used before or without their first expansion in this chapter** (style 8.1 and writer instructions):
   - Used before the expansion: CFADS at line 7 (expanded at 19), COD at 141 (expanded at 200).
   - Never expanded: PPP (23), PPA (58), ECA (198: "export credit agency (ECA)"), DFI (371), IPP (590), LNG (3), IRR (820), ABDB (Exhibit 36.12, line 759: "Atlantic Basin Development Bank (ABDB)"), TIFIA (458), PABs (632), OPBA (Solution 36.18, line 1129).
   - PPP, IRR, ABDB and PABs each appear fewer than three times, so write them out in full rather than coining an acronym.

10. **Terms used before their home chapter with no forward reference.**
    - "lock-up level" (lines 324 and 836; home ssec:37.4.1): add `\cref{sec:37.4}` at line 324.
    - "modeling bank" (652; home ssec:55.2.2): add a gloss and a reference.
    - "prepackaged Chapter 11" (522; home ssec:64.8.2): add `\cref{ssec:64.8.2}`.
    - "cash sweeps" at first use (188; home ssec:37.3.1): add `\cref{ssec:37.3.1}` there instead of only at line 486.

11. **Real cases that earlier chapters already teach are retold without cross-references.**
    - Indiana Toll Road (line 522) is taught in ssec:6.8.4, ssec:14.12.3 and ssec:16.6.3. Cite ssec:14.12.3 and keep only the bullet-maturity point. Make clear that "USD 3.9 billion fell due" is a different measure from Chapter 14's "secured claims of about USD 6 billion".
    - Dulles Greenway (460): add `\cref{ssec:21.7.2}`.
    - Ocean Wind (648): add `\cref{ssec:14.12.2}`.
    - Dogger Bank offshore transmission (269): add `\cref{ssec:11.3.3}`.
    - Trim the facts already stated there.

12. **Clause 36.1 (line 1078) prints a number but has no label and no registry entry.** Ask the editor-in-chief to register `cl:36.1`, "Refinancing test, term sheet (Illustrative)", and add `\label{cl:36.1}` after the `\begin{clause}` line.

13. **Three display equations have no Excel implementation** (style 5.1 and 5.3).
    - eq:36.4, the lesser-of rule: the `=MIN(...)` appears only in Solution 36.15. Move it under the equation.
    - eq:36.6, bucket debt service: add a row formula, for example contracted CFADS row divided by the contracted target plus merchant CFADS row divided by the merchant target.
    - eq:36.5, the WAL constraint: add `=SUMPRODUCT(time row, principal row)/SUM(principal row)` with a check against the limit cell.
    - State the cell layout for each.

14. **The Excel sizing block (lines 124–136) collides with the Case P workbook map.**
    - It addresses Debt!J10 to J26. In the Case P model (u09 row map), Debt rows 7–19 hold rates and the contract profile, and rows 126–135 hold the live sculpting check.
    - It names `Flag_FirstRepayment` and `Flag_Repayment`. The Case P flag set has `Flag_SculptingPeriod` (Time row 53) and `Flag_DebtService` (Time row 35).
    - Line 136 says sec:42.2 "rebuilds the same block". The Case P check works differently: it takes PV of CFADS over the fixed debt.
    - Fix: say the block sits on a standalone sizing sheet, not the Case P Debt sheet, and rephrase line 136 as "\Cref{sec:42.2} builds the Case P version, the live sculpting check".

15. **Some table cells are empty or hold the wrong unit** (style 6.1 and 6.3).
    - Empty cells: Exhibit 36.2 (Total row), Exhibit 36.3 (Binding column; Debt and Resulting gearing rows), Exhibit 36.5 (Binding column), Exhibit 36.11 (Binding column; Senior debt row), and Exhibit 36.12 (Test and Result cells in the senior debt and tranche rows). Fill each with "--" or "n/a".
    - Exhibit 36.12, LLCR row: "1.42x achieved" sits in the "Debt allowed (USD m)" column. Put "n/a" there and the ratio in the Result column.
    - Exhibit 36.8: the notional-profile balances plotted in the chart appear in no table or text. Add them to the note.

16. **Number formats are inconsistent** (style 2.3 and 2.5).
    - Ratios in the house format take two decimals: "1.0\x" (lines 324 twice, 1135), "2.0\x" (563, 611), and "1.0x" and "2.0x" in Exhibit 36.10 become 1.00x and 2.00x.
    - The three-decimal k columns (Exhibits 36.3 and 36.5, Solution 36.19 table) and "1.506\x" (992) and "1.342\x" (1104) should either drop to two decimals or be labeled as a factor rather than a ratio. Keep 1.5999x and 1.3501x, where the extra precision is the teaching point.
    - Years in compound modifiers are mixed: "7-year" at lines 893, 898, 984, 988 and 1125 against "seven-year" at 495 and 1133. Use the spelled form throughout.

17. **Local-currency examples lack a USD equivalent and do not say whether figures are real or nominal** (style 2.4).
    - Examples 36.1 (CAD), 36.3 and 36.5 (EUR), 36.6 (GBP), 36.8 (MXN) and 36.11 (EUR) give no USD equivalent with a stated illustrative rate. Example 36.4 does it correctly. Add one per example.
    - Examples 36.3, 36.7, 36.8, 36.9 and 36.11 do not state whether figures are real or nominal. Add the statement once per example.

18. **Two exercises are not located** (style Addendum A.10). Exercise 36.11 (Ghana gas plant) and Exercise 36.12 (Rotterdam warehouse) give no year and no project company. Add a fictional party and a year to each.

19. **One citation does not match its source entry.** The in-text "(GIIA 2015)" at line 522 cites an entry listed as "Global Infrastructure Investor Association (GIIA). n.d." (line 1165). Make the two agree, using the fact sheet's date.

20. **LaTeX and cross-reference hygiene.**
    - Line 1049: `$27.9/24.00 = 1.16\x$` puts `\x` in math mode, which causes the log warning. Write `$27.9/24.00 = 1.16$\x`.
    - Line 601: "; \Cref{ch:38}" is mid-sentence, so it should be `\cref`.
    - Line 699: "this printout's footnote". The exhibit has a Note line, not a footnote. Write "this printout's note".

21. **Two pilot lessons from the writer instructions are broken.**
    - The close (line 913) ends on rhetorical questions followed by "\Cref{ch:37} answers with ...". End instead on the concrete open problem.
    - Lines 520–522 restate the opening's Port Arthur facts (seven-year maturity on a 20-year profile, March 2023 close). Cross-reference the opening and keep only the new point, the hard-by-maturity classification.

## Central-file flags for the editor (not chapter defects)

- Anchor registry: renumber eq:36.5 to eq:36.7 (defect 1) and add cl:36.1 (defect 12). Also sync the u08 brief with the writer's justified deviations: Example 36.8 options (b) and (c), the four constraints in Example 36.4, the 1.44x in Example 36.11, and the Exercise 36.10 answer.
- Case Bible Part 7.1 register: P-F07 lists users 32, 40 and 55, and P-F43 lists 40 only. Add Chapter 36 to both; the Part 7.4 index already includes it.
- Case Bible Part 5A cites decision D-134 for the Kali Gandaki replacements, and the writer instructions cite D-126. Neither appears in `bible/decisions.md`, which ends at D-125. Log them.
- Glossary canon: consider adding "effective base-case target" (the k of the current eq:36.7), which the chapter uses as a named concept and the registry uses in a caption.
- Exhibit 36.14's "below the 1.20x lock-up level" compares a projected downside minimum with the historic-DSCR lock-up. The two thresholds have the same value in the Case P terms, so this is consistent. The domain reviewer may prefer "below the 1.20x downside test".
