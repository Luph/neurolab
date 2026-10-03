# Chapter 36 writer notes (pilot, calculation-heavy)

File: `chapters/36-sizing-and-sculpting-debt.tex`. Date: 2026-10-03.

## Word count
About 21,500 words by source count (including tables, exhibit notes, solutions and the Sources list); about 22,700 words in the PDF text. Brief target 16,000. The excess is in the 19 full solutions (each with answer, steps, reconciliation and commonest wrong answer), two added explanations (the gearing funding-requirement circularity in sec:36.12 and the P-F09 sweep reconciliation) and the walkthrough. No padding found on self-review; the line editor may tighten the 36.10 drivers prose. 54 pages.

## Build and scan
- `bash scripts/build_chapter.sh chapters/36-sizing-and-sculpting-debt.tex`: BUILD OK, 0 overfull boxes. Only cross-chapter references undefined (ch:2, 6, 34, 35, 37, 38, 61, 63, 64; sec/ssec/eq/fw/exh labels in Ch 5, 6, 9, 11, 13, 14, 19, 20, 21, 29, 30, 35, 37, 38, 40, 42, 45, 46, 51, 75); every one checked present in the anchor registry.
- `python3 scripts/scan_prose.py`: 0 hits. Manual self-scan: no em dashes; vague "This/That" openers rewritten (8 instances); no false-contrast reframes, zingers or question stacks found. The opening asks two questions in sequence (the chapter's puzzle, answered in sec:36.7.2 and the whole chapter); flag if the line editor reads it as a stack.
- All label numbers verified against printed numbers from the .aux file.

## Numbers
Every figure recomputed in Python (scripts in the session scratchpad `ch36/`: lib.py, ex1_2.py, ex3.py, ex4.py, ex6.py, ex7.py, ex8.py, ex8b.py, ex9.py, ex10.py, ex11.py, ex12.py, drill.py, exr.py, ex16.py, ex18.py, ex19.py, printout.py). Case P figures only from the ledger (P-F07, P-F08, P-F09, P-F36, P-F43) plus D-013 arithmetic (642.9 - 633.3 = 9.6; 538.2 sum of P-F09; 633.3 - 538.2 about 95; tail 12.4 years from input dates; 75% x 855.09 = 641.3).

## Deviations from the brief (and why)
1. **Example 36.8 option (c) changed from a three-year to a four-year grace.** Recomputation showed the brief's three-year grace still has negative principal in year 4 (sculpted DS 263.2 < interest 270.0), contradicting its own no-capitalization premise. Four-year grace: debt MXN 2,666.6 m, reserve MXN 208.4 m covering shortfalls 118.9/78.6/40.9/7.4; first principal year 5 = 16.7. The three-year result (2,659.8; 201.6) is mentioned as the failed first try.
2. **Example 36.8 option (b) reframed.** The brief's 1,494.7 cap is kept, but a single sculpting target cannot meet a no-negative-principal rule on this cash flow; the text now says the cap is set by year-1 interest cover at 1.40x and the debt is then repaid by year 10 at 1.40x (or 2.39x over 18 years).
3. **Example 36.4 now has four constraints.** The locked title says "Four constraints" but the brief computed three; added a cost downside (opex +15% at 1.20x, BRL 785.0 m, slack).
4. **Exercise 36.10:** at 20 years the PLCR is 1.5999x, which fails a 1.60x test. Answer kept at 20 years but on debt trimmed by USD 0.03 m to 389.08; the rounding trap is the "commonest wrong answer".
5. **Example 36.11:** effective DSCR in year 10 is 1.44x (1.4448), not the brief's 1.45x.
6. **Example 36.3 total interest:** unrounded total 37.78 (rounded column sums to 37.79); exhibit shows unrounded totals with a rounding note.
7. **Names changed after a web check (Case Bible Part 5 rule):** Matagorda Bay LNG -> Redfish Pass LNG Train 1 LLC (real Lantern LNG "Matagorda Bay" project, 4 mtpa trains); Broadlands Digital -> Catoctin Hollow Digital LLC (real CyrusOne Broadlands campus, Loudoun); Comal Storage -> Pecan Bayou Storage LLC (real ~200 MW batteries in Comal County); Kali Gandaki Hydro -> Dhaulagiri Kholsi Hydro Pvt Ltd (real 144 MW Kali Gandaki A plant); Alto Minho Eólica -> Alto Lombada Eólica, S.A., Trás-os-Montes (real 240 MW Alto Minho wind farm); Ventos do Potiguar -> Ventos da Chapada do Caju S.A. (real Ventos Potiguar offshore project); Libramiento Norte Edomex -> Vía Norte Tepotzotlán S.A. de C.V. (generic name close to the real Libramiento Mexiquense). Checked clear (no match found): Cheviot Edge, Pampa Clara Solar, Toba Panas Bumi, Llanos de Mérida Solar, Bukhara Quyosh, Northshore Justice Partners, Cap Vert Power, and the new names above. New unchecked names: Wadi Hommath Wind SAE (walkthrough), Rioni Zemo Hydro LLC, Las Cumbres Salud S.A., Thar Rekha Solar Pvt Ltd (exercises). Please add all to Case Bible Part 5A.
8. **Walkthrough printout (Exhibit 36.11)** built on an original Egyptian wind farm (Gulf of Suez, 25-year USD PPA, CCSU ECA tranche), with gearing binding and the downside slack by USD 0.18 m, so the printout teaches a near-co-binding read. All numbers computed (printout.py).
9. **Judgment drill:** the grace period is shown not to breach the CCSU WAL limit (12.93 years against 13.3 with all three requests); the text says it uses up room rather than "possibly breaching".
10. **Exercise 36.12** adds a drafted refinancing-test clause (Illustrative) with annotations; the clause has no label because the anchor registry lists no Ch 36 clause.

## Equation numbering (flag for the editor)
The registry numbers eq:36.5 (WAL, sec:36.9), eq:36.6 (bucket, sec:36.8) and eq:36.7 (effective target, ssec:36.3.1) out of order of appearance. To keep the registry numbers I used `\tag{36.7}`, `\tag{36.6}`, `\tag{36.5}` on those three; `\cref` prints "Equation (36.x)" correctly. If the editor prefers, renumber in the registry instead (order of appearance would be 36.4 lesser-of, 36.5 effective target, 36.6 bucket, 36.7 WAL).

## Ledger and Bible flags
- **P-F09 scheduled principal sums to USD 538.2 m, not 633.3 m.** Confirmed in `model/case_p.py` (FC base, `p['miniperm']`): the commercial tranche's 50% sweep from January 2027 prepays about USD 94.7 m in the model run (ledger difference 95.1), and the ECA tests (largest installment 4.6%, WAL 7.18, 9.0% within 24 months) are measured on the 538.2 of scheduled installments. The chapter prints this with an exhibit note. Suggest the ledger add a row "FC base mini-perm sweep, total" so writers need not derive it, and that Ch 39/42 writers are told.
- P-F08's "Debt at the 75% gearing cap" (642.9) is 75% of the closed-form total funding at the cap (P-F43, 857.2), not of the FC base total (855.09). Explained in sec:36.12; Ch 35/40 writers should use the same explanation.
- The base-case average DSCR of 1.54x against a 1.35x minimum is attributed (hedged: "largely") to the sweep shrinking later scheduled debt service; based on reading the model, not a ledger row.
- Ledger header says model v1.4; the brief says v1.3. Values used are the ledger's.
- Scene place "Castellan Bank, London" is inferred (Pieter is London-based; Castellan Bank London is the offshore account bank); the Case Bible beat gives no place.

## New terms (not in glossary canon)
None defined with \term beyond the brief's owned list. Used without bold: "tenth of a turn" (explained in text), "effective base-case target" (the k of eq:36.7; consider adding to the canon), "ramp-up reserve" (introduced in one sentence, not bold, because its home is ssec:37.2.2).

## Facts beyond the fact sheets
None added. All real-world statements come from t-market-norms, t-market-norms-2, t-oecd-arrangement, t-oecd-pf-2018, dogger-bank, sh130, dulles-greenway, indiana-toll-road and ocean-wind; "Do not state" lists respected (no regional single norms, no rating-agency thresholds beyond Exhibit 30.5, Annex VII not called Annex X, no claim on extension of the 2017 terms). Dropped the brief-implied "merchant after CfD" for Dogger Bank (not in the sheet). The indicative tail-length judgment in ssec:36.5.2 is labeled as the book's indicative view (D-011) and needs domain-expert sign-off.

## For reviewers
- Numbers auditor: the Python scripts above reproduce every table; Exhibit 36.11 inputs are in its source line.
- Domain expert: please test the ssec:36.5.2 tail judgment and the 36.14 drill answer.
