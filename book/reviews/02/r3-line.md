# Chapter 2 review, round 3: line editor

File: `chapters/02-what-project-finance-is.tex` (round-2 revision; the log is the "Round 2" section of `reviews/02/r1-revision.md`).

`scan_prose.py`: 0 hits. Em dashes: 0. I read every passage changed since commit 5237fb6 against `standards.md` Section 8 and the style sheet.

## Verdict: FAIL (narrowly)

All 15 round-2 items are resolved (table below). The chapter fails on two new defects introduced by this round's revisions:

- **R3-1:** a meaning error in the fit test, a framework other chapters will cite.
- **R3-2:** walkthrough Step 2 has grown into a single 489-word paragraph that the book's other walkthroughs would copy.

R3-3 to R3-7 are minor and do not block a pass on their own. Once R3-1 and R3-2 are fixed, the chapter passes the prose test and can serve as the voice exemplar.

## Verification of round-2 items

| R2 | Status | Note |
|---|---|---|
| 1 | Resolved | The opening hook is lighter. The balance-sheet gloss moved to line 24. |
| 2 | Resolved | Line 36. |
| 3 | Resolved | Line 213. |
| 4 | Resolved | Lines 173 and 324: the references are now attached to the claims. |
| 5 | Resolved | Line 297 has no count sentence; line 239 is one sentence. |
| 6, 7 | Resolved | Lines 310 to 312. |
| 8 | Resolved | Line 223 now reads correctly. |
| 9 | Resolved | Line 515. |
| 10 | Resolved | Lines 203 and 205. |
| 11 | Resolved | Line 306. |
| 12 | Resolved | Line 24. |
| 13 | Resolved | Line 404. |
| 14 | Resolved | Line 92: the three layers come first, then the notes. |
| 15 | Resolved | Line 588. |

The ssec:2.4.3 heading was reverted on the coordinator's registry ruling. I accept the reversion and withdraw R1-31.

## Defects

R3-1. **Fit-test question 2 now asks only about currency (meaning error).** Line 412: "Is the revenue, whether contracted with a counterparty creditworthy enough to pay for longer than the debt will be outstanding or predictable enough for lenders to forecast it for that long, earned in a currency the debt can be serviced in?" The "whether ... or ..." clause turns the credit and forecastability tests into an assumption, so the only thing the question asks is the currency. A reader can answer "yes" for uncontracted, unforecastable revenue in dollars, and Northvolt (line 421) would pass question 2. Required fix: make the question ask both conditions. "Is the revenue either contracted with a counterparty creditworthy enough to pay for longer than the debt will be outstanding, or predictable enough for lenders to forecast it for that long, and is it earned in a currency the debt can be serviced in?" Then propagate the corrected wording to the u01 and u17 briefs, as the log says was done for the current wording.

R3-2. **Walkthrough Step 2 is a 489-word single paragraph covering five ideas (§8 one idea per paragraph; monotone rhythm; false contrast).** Line 430 runs through:
   - the cushion arithmetic;
   - the cushion policy and dividend restraint;
   - the quarterly forecast;
   - the rejected alternatives;
   - the standby facility, with its drawing order, fees and fallback.

   It is now longer than the other six steps combined, and a walkthrough must be one a reader "could perform the next morning". Required fix:
   - Keep Step 2 as one `\item`, but break it into three paragraphs: (a) the leverage arithmetic and the 4.8% and 0.2% cushions; (b) the cushion policy, met by the dividend restraint and the USD 29.2 million cap, with the quarterly forecast; (c) the standby facility and the fallback.
   - Move the rejected alternatives to the end of (b), as one sentence.
   - Replace "That is a concession, not protection for the lenders: the standby is more senior debt, drawn exactly when the project is in trouble." This is a false-contrast reframe with a colon reveal. Write instead: "For the lenders the standby is a concession: it is more senior debt, drawn exactly when the project is in trouble."
   - Correct "Even a cap of USD 29.2 million, the most the headroom allows". Headroom allows USD 30.4 million (Solution 2.7), so write "Even a cap of USD 29.2 million, 7.5% of cost and just inside the USD 30.4 million of headroom,".

R3-3. **The PPA settlement mechanics are repeated (§8 explanations repeated).** Step 4 (line 434) restates line 133 almost word for word: "pay-as-produced and settled at the wind farm's own node, so the miner bears the price difference between nodes while GLA keeps curtailment". Required fix: in Step 4, write "the 15-year US-dollar PPA of \cref{ex:2.1}, with GLA keeping curtailment risk, and the other 20% of output sold at market prices that the lenders give little credit."

R3-4. **Overloaded sentence with an ambiguous referent (§8 rhythm; clarity).** Line 133: "The power does not travel to the mine: the PPA is pay-as-produced and settled through Chile's national power market at the wind farm's own node, so the miner pays the contract price for 80% of whatever the wind farm produces and bears the difference between the price at the wind farm's node and at its own, while GLA keeps the risk that the system operator curtails the wind farm." This is one sentence of about 70 words, and "its own" could mean the wind farm's node or the miner's. Required fix: split it into three sentences: "The power does not travel to the mine. The PPA is pay-as-produced and settled through Chile's national power market: the miner pays the contract price for 80% of whatever the wind farm produces and bears the difference between the market price at the wind farm's node and at the mine's. GLA keeps the risk that the system operator curtails the wind farm."

R3-5. **The rating scale is introduced after the threshold it explains (§8 concrete before abstract; order).** Line 112: "The grades run from AAA at the top through AA, A, and BBB, then BB and below." comes after the sentence that names BBB- as the investment-grade floor. Required fix: move it in front of that sentence, so the scale comes first and the threshold second.

R3-6. **Repeated clause across adjacent drill paragraphs (§8 summary sandwich).** Line 568 ends "and the USD 389.6 million would stay on its balance sheet." Line 572 says again "while under the corporate route the whole USD 389.6 million stays on GLA's balance sheet." Required fix: cut the clause at line 568, because line 572 makes the comparison.

R3-7. **Mixed units in one exhibit cell (style sheet §6.1).** Line 457 of Exhibit 2.3 reads "All-in annual cost (bps) & 141.4 & 248.0 (3.1 a year more)". The parenthetical is USD million inside a bps row, so the reader cannot tell which unit "3.1" is in. Required fix: restore a separate row, "Extra annual cost of project finance (USD m) & -- & 3.1 (3.0 before agency fee)".

## Counts

7 defects. R3-1 and R3-2 block a pass. R3-3 to R3-7 are minor line edits.
