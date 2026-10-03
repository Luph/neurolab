# Chapter 2: final verification after round 3

File: `chapters/02-what-project-finance-is.tex`. Inputs: r3-numbers, r3-novice, r3-domain, r3-line and r3-consistency (r3-facts had already passed), plus the writer's "Round 3" log in `r1-revision.md`. Date: 2026-10-03.

## Verdict: PASS

All 21 round-3 defects are fixed in the chapter, or in the bible for the two that belong there. Every number in Exhibit 2.3 and walkthrough Step 2 recomputes. The new Ley 18.046 art. 79 citation matches two primary sources. While reading the changed passages for Section 8 patterns, I found three minor line defects and fixed them directly (see the last section). After those fixes:

- **Build:** BUILD OK, 53 pages. One overfull box of 0.27pt (Solution 2.9 `align*`), under the 5pt limit. No undefined Chapter 2 references; only cross-chapter references are undefined, as expected in a standalone build.
- **`scan_prose.py`:** 0 hits.
- **Em dashes:** 0.

## Numbers recomputed

Script: `scratchpad/review-02/final_verify.py`. Everything below matches the printed figures.

**Corporate route and base project-finance position**

| Quantity | Computation | Result | Printed |
|---|---|---|---|
| Covenant capacity | 3.50 x 182.4 | 638.4 | 638.4 |
| Headroom before the wind farm | 638.4 - 510.6 | 127.8 | 127.8 |
| Corporate leverage, construction | 900.2 / 182.4 | 4.935 | 4.94x |
| Corporate leverage, after COD | 900.2 / 223.7 | 4.024 | 4.02x |
| Project-finance leverage, no restraint | 608.0 / 182.4 | 3.333 | 3.33x |
| Headroom left, no restraint | 638.4 - 608.0 | 30.4 | 30.4 |
| Largest cap | 30.4, which is 7.80% of cost | 30.4 | 30.4 (7.8%) |
| EBITDA cushion, no restraint | 608.0 / 3.50 = 173.71 | fall of 4.76% | 4.8% |
| After a full call of the 29.2 cap, no restraint | 637.2 / 182.4 = 3.493x; 1.2 spare | fall of 0.19% | 3.49x; 0.2% |
| Lenders' first ask (58.4) called in full | 666.4 / 182.4 | 3.654 | 3.65x |

**With the dividend restraint**

| Quantity | Computation | Result | Printed |
|---|---|---|---|
| Retained cash | 67.2 / 2 | 33.6 | 33.6 |
| Net debt | 608.0 - 33.6 | 574.4 | 574.4 |
| Leverage | 574.4 / 182.4 | 3.149 | 3.15x |
| Headroom | 638.4 - 574.4 | 64.0 | 64.0 |
| EBITDA cushion | 1 - 574.4 / 638.4 | 10.03% | 10.0% |
| After a full call: net debt | 574.4 + 29.2 | 603.6 | 603.6 |
| After a full call: leverage | 603.6 / 182.4 | 3.309 | 3.31x |
| After a full call: breakeven EBITDA | 603.6 / 3.50 | 172.46 | 172.5 |
| After a full call: EBITDA cushion | | fall of 5.45% | 5.5% |

**Dividend and Ley 18.046 minimum**

| Quantity | Computation | Result | Printed |
|---|---|---|---|
| GLA net profit | 67.2 / 0.65 | 103.38 | 103.4 |
| Halved dividend as a share of net profit | 33.6 / 103.38 | 32.5% | 32.5% |
| Legal minimum | 30% of net profit | 31.0 | below 33.6, so the dividend complies |

**Standby, losses and cost**

| Quantity | Computation | Result | Printed |
|---|---|---|---|
| Standby committed | 58.4 - 29.2 | 29.2 | 29.2 |
| Standby drawn after a 14% overrun | 54.5 - 29.2 | 25.3 | 25.3 |
| Project debt drawn | 292.2 + 25.3 | 317.5 | 317.5 |
| Committed in all | 292.2 + 29.2 | 321.4 | 321.4 |
| Worst-case loss | 97.4 + 29.2 | 126.6 | 126.6 |
| Upfront fee | 0.0225 x 29.2 | 0.657 | 0.66 |
| All-in difference | 248.0 - 141.4 = 106.6 bps; 0.01066 x 292.2 | 3.11 | 3.1 |

## Law citation

Chile, Ley 18.046, art. 79, checked on 2026-10-03 against two primary sources. The cited SII copy (`sii.cl/.../ley_18046b.htm`, HTTP 200) and the BCN consolidated text (LeyChile JSON service, idNorma 29473) both read:

> "Salvo acuerdo diferente adoptado en la junta respectiva, por la unanimidad de las acciones emitidas, las sociedades anónimas abiertas deberán distribuir anualmente como dividendo en dinero a sus accionistas ... a lo menos el 30% de las utilidades líquidas de cada ejercicio."

The chapter states that the minimum of 30% applies to open corporations "unless every share votes otherwise (Chile 1981)", and that the shareholders' meeting approves the dividend on the board's proposal. Both statements are accurate.

## Round-3 defects and their status

| Report | # | Defect | Status | Fixed text (quoted) |
|---|---|---|---|---|
| numbers | 1 | Exhibit 2.3 mixed figures with and without the restraint | Fixed | "3.15 (3.33 without restraint)" in both leverage rows; "Met; headroom 64.0 (30.4 without restraint)"; "3.31 (3.49 without restraint)"; note: "Project finance figures include the dividend restraint (33.6 retained, assumed still held after COD) unless stated ... Without the restraint the breaking EBITDA falls are 4.8\% and 0.2\%." |
| numbers | 2 | "The most the headroom allows" | Fixed | "Even a cap of USD~29.2 million, 7.5\% of cost and just inside the USD~30.4 million the headroom allows, would leave USD~1.2 million to spare" |
| numbers | 3 | USD figure in the bps row | Fixed | "248.0 (106.6 more; USD 3.1 million a year)" |
| novice | 1 | Node, settlement and system operator undefined | Fixed | "Chile's wholesale market sets a separate price at each point, or node, of the grid (\cref{ssec:11.11.1}) ... the system operator, the body that runs the grid and decides which plants run" |
| novice | 2 | "Unincorporated joint venture" undefined | Fixed | "an unincorporated joint venture, a partnership created by contract rather than a company, in which each partner owns its share of the assets directly. A jointly owned company, PNG LNG Global Company, played the borrowing role a project company plays at Llano Pardo" |
| novice | 3 | Exhibit 2.3 did not agree with Step 2 | Fixed | See numbers 1 |
| novice | 4 | Standby described inconsistently | Fixed (wording then tightened, see below) | "the buffer of \cref{ex:2.1} here sized to replace sponsor support ... The standby funds the overrun, but for the lenders it is more senior debt, drawn exactly when the project is in trouble, so they treat it as a concession to the sponsor." |
| novice | 5 | "Bankruptcy-remote" and "licensed business" undefined | Fixed | "an entire licensed business, one that operates under a government license and is regulated as a utility"; "a bankruptcy-remote structure: one designed so that the company cannot easily be pulled into its own or its owners' insolvency, the ring-fence idea of \cref{ssec:2.1.2}" |
| novice | 6 | Trailing twelve-month EBITDA undefined; "hydrology" unclear | Fixed | "trailing twelve-month EBITDA (the EBITDA of the most recent four quarters)"; "with rainfall, which drives hydro output, and with spot prices" |
| domain | D1 | 5% policy not justified against the 4.8% judged too thin | Fixed | "GLA's treasury policy, an illustrative one set by its board: in a joint stress, with the overrun cap called in full while EBITDA is down, EBITDA must still be able to fall about 5\% before the covenant breaks, and before any call the cushion must be about twice that" (10.0%) |
| domain | D2 | Dividend cut presented as the board's decision; no legal minimum | Fixed | "The board will propose to the 2025 ordinary shareholders' meeting a dividend of half the usual USD~67.2 million ... 32.5\% of net profit and stays above the minimum of 30\% that Chilean law requires an open corporation to distribute unless every share votes otherwise (Chile 1981). The paper drafts the message to investors and rating agencies ... a one-year retention to fund Alto Huelén" |
| domain | minor | bps row | Fixed | See numbers 3 |
| line | R3-1 | Fit-test question 2 asked only about currency | Fixed | "Is the revenue either contracted with a counterparty creditworthy enough ... or predictable enough for lenders to forecast it for that long; and, whether contracted or merchant, is it earned in the currency of the debt or hedged into it?" The same wording is in u01.md l.678 and u17.md l.73. |
| line | R3-2 | Step 2 was a single 489-word paragraph | Fixed | Now three paragraphs: 159, 295 and 186 words. The rejected alternatives close the second. The false-contrast reframe is gone, and the headroom error is corrected. |
| line | R3-3 | PPA mechanics repeated in Step 4 | Fixed | "the 15-year US-dollar PPA of \cref{ex:2.1}, with GLA keeping curtailment risk, and the other 20\% of output sold at market prices that the lenders give little credit" |
| line | R3-4 | Overloaded PPA sentence; "its own" ambiguous | Fixed | "The power does not travel to the mine." Separate sentences follow, ending "... at the wind farm's node and at the mine's. GLA keeps the risk ..." |
| line | R3-5 | Rating scale came after the threshold | Fixed | "The grades run from AAA at the top through AA, A, and BBB, then BB and below; on the scales of S\&P and Fitch, BBB- is the lowest grade ..." |
| line | R3-6 | Repeated 389.6 clause in the drill | Fixed | The first reasoning paragraph now ends "with nothing left for the next project." The comparison appears only in the risk paragraph. |
| line | R3-7 | Mixed units in a cell | Fixed | See numbers 3 |
| consistency | 1 | "The most the headroom allows" | Fixed | See numbers 2 |
| consistency | 2 | Exhibit 2.3 on two bases; after-COD assumption unstated | Fixed | See numbers 1; the note states "assumed still held after COD" |
| consistency | 3 | Stale registry note for `ssec:2.4.3` | Fixed (bible) | anchor-registry.md l.317: "title restored in Ch 2 round 2 revision" |

## Section 8 read of the changed passages: minor fixes made

I made three line-level fixes directly. None changes a fact, a number or a cross-reference. A copy of the file before these edits is in `scratchpad/review-02/ch02-before-final.tex`.

1. **ssec:2.4.5, Tideway sentence (92 words).** The new glosses had produced a 92-word sentence with nested parentheses: an overloaded sentence, the same defect as R3-4. I split it into three sentences with the same content:
   - "The family includes securitization, whole-business-style financings, and the hybrid structures ...";
   - "A whole-business-style financing secures the debt on an entire licensed business ...";
   - "The company that built London's Thames Tideway Tunnel is financed this way, through a bankruptcy-remote structure: ... (Bazalgette Tunnel Limited 2026)."
2. **Step 2(c).** "For the lenders the standby cuts both ways: it ensures the overrun is funded, but ..." used a stock idiom close to the banned "double-edged sword", a reflexive "ensure" and a colon reveal. It now reads "The standby funds the overrun, but for the lenders it is more senior debt, drawn exactly when the project is in trouble, so they treat it as a concession to the sponsor." The sentence keeps the novice-4 reconciliation.
3. **Step 2(b).** "trailing twelve-month EBITDA, the EBITDA of the most recent four quarters, and GLA's own capital spending ..." read as a three-item list. The gloss is now in parentheses.

No other Section 8 pattern was found in the changed passages. "A one-year retention ..., not a change of dividend policy" is kept: it is the paper's message correcting a reading that investors would actually make.

## Note carried forward (not a defect)

The writer's flag on a pending Chilean bill that would change the unanimity quorum in art. 79 is still unverified. The chapter does not mention it. Recheck at the facts pass before print.
