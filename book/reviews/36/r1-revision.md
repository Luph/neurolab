# Chapter 36, round 1 revision log

File: `chapters/36-sizing-and-sculpting-debt.tex`. Build: BUILD OK, 55 pages, 0 overfull boxes, no math-mode warnings; every undefined reference is cross-chapter and present in the anchor registry. `scan_prose.py`: 0 hits. Equations now print 36.1 to 36.7 in order of appearance. Case P figures are from model v1.5 (ledger regenerated); IDs are kept only in `%` comments.

Central files changed: `bible/anchor-registry.md` (eq:36.5 is now the effective base-case target, eq:36.7 the WAL constraint; registry row A3 updated; cl:36.1 added), `bible/ownership-resolutions.md` (R-005 and R-116 now cite eq:36.7), `bible/briefs/u08.md` (key-formula list relabeled), `bible/case-bible.md` Part 5A.3 (row registering every Chapter 36 name with its check status).

Note for the coordinator: your v1.5 note gives scheduled principal 535.287 and sweep 94.662. The regenerated ledger (P-F09) gives 530.462332 and 99.487343. The chapter prints the ledger values (530.5 and 99.5).

## Domain (r1-domain)
| ID | Fix |
|---|---|
| D1 | Case P rewritten for v1.5. ECA tests are run on the covered tranche's own 26 equal installments (WAL 6.92 against 7.25, largest 3.8%, term 13.16, first repayment 8 months, 11.5% within 24 months). The other tranches' 8.17-year WAL and the 7.79-year all-tranche WAL are shown as memo lines. The ECA-tranche rule is added to ssec:36.9.1, the stack's step 6, the checklist and the red flags. The scene, the close, Exr 36.13 and its solution are rewritten, and the wrong profile-shape sentence is removed. |
| D2 | The resculpting paragraph is rewritten: debt and maturity are held, the level DSCR is an output, and a completion floor applies with an LD prepayment. Case P: 1.28x against the 1.30x floor, pointing to ch:61. |
| D3 | Changed to "Two real examples show the short end". The tail-length judgment is replaced with the reviewer's text, carrying a full D-011 label. The Case P tail is described as a by-product of the ECA cap. The walkthrough and drill tails now read "well above the two-to-three-year minimum and typical of a DFI- and ECA-led deal". |
| D4 | Ex 36.4 is now an IPCA-linked loan at 13.0% nominal (about 8.7% real). Recomputed: P50 580.8; P90 516.1 binds; cost downside 582.9; gearing 830.2; 43.5%; USD 95.2 m. The 6% contrast is restated (P90 test 866 vs cap 830.2). |
| D5 | Ex 36.6 now has a 15-year CPI-indexed CfD "of the kind offered before the scheme moved to 20 years for its seventh round (2025–26)", with no round named (D-127). Indexation is assumed at 2.0%. DESNZ 2025 added to Sources. Exr 36.18 is consistent. |
| D6 | The reserve is placed in the funding requirement, pro rata or equity-funded. The effect if 75% is debt-funded (MXN 164.1 m) is shown, and the lender preference is presented as a negotiated point. |
| D7 | Tax-interest circularity added. |
| D8 | Exh 36.14 replaced by the v1.5 full-test grid: the 1.30x rows now bind on the downside at 630.1. The note states that all four tests are applied. The narration is rewritten. |
| D9 | Now reads "carries soft mini-perm features although it amortizes fully". |
| D10 | The NRF measure is declared undefined, with PV of debt service used as the proxy. The CFADS share (49.0%) is added to Ex 36.11 Step 5. The Spanish-lender sentence is fixed. Exr 36.16 solution states the measure. |
| D11 | The drivers are ranked per parameter: DSCR (contract, volatility, country, cycle) and tenor (contract length and lender type, country). The paragraphs are rewritten to match. |
| D12 | Exh 36.6 note: the CCSU 22-year cap, with the 24-year column carried by the DFI or an uncovered lender. Exr 36.10 solution notes 20 years is within 22. |
| D13 | Diminishing increments are attributed to discounting; tail and PLCR are presented as the separate price. |
| D14 | Now reads "ECA's standard equal-principal installments, more front-loaded still". |
| D15 | Tense fixed (2017 text; current allows one year). |
| D16 | Step 6's first question replaced (where is the ten-year P90 test). |
| D17 | Drill: cushion is the wrong instrument for a payment stop. Counter offered: 1.30x plus 12 months of payment security. P99 floor described as nearly free. |
| D18 | Exr 36.19 package now uses a P99 liquidity test with the DSRA counted (factor 0.934, not binding). The 70% gearing cap binds at USD 160.0 m (effective P50 1.41x). The stand-alone 1.00x floor (120.8) is named the commonest wrong design. |
| D19 | Authority lens paragraph added in ssec:36.3.2: termination compensation, affordability, refinancing gains, and PF2's 75:25 to 90:10 drift (NAO 2018). Contractor lens paragraph added in ssec:36.2.4 (performance and delay LDs calibrated to the sizing). |
| D20 | Dual-profile (target vs legal) treatment added to ssec:36.8.2. |
| Minors | Scene's last line now answers Tomasz. ECA no-capitalization rule added to Ex 36.8 discussion. "impossible for a seven-year bank mini-perm" replaced. |

## Numbers (r1-numbers)
| ID | Fix |
|---|---|
| N1 | 25% in the last two years. |
| N2 | Balloon: 47.7% nominal and 25.5% PV, stated. |
| N3 | Contracted-only column now 1.82/1.67/1.59, note replaced. |
| N4 | Merchant-stress sentence rewritten (35% CFADS cut; 1.30x minimum in year 15). |
| N5 | Base LLCR 1.37x in the exhibit and Step 5. |
| N6 | LLCR row 138.55, slack 2.58, DSRA scaled (note says so). |
| N7 | Printout rerun on 569.9 GWh: 138.37 / 136.16 / 138.02. P99 minimum 1.0150, printed as 1.02x. |
| N8 | Case P downside slack about USD 0.2 m (0.188, v1.5); dialogue "not quite two hundred thousand". |
| N9 | Gearing slack 13.1 (13.13 unrounded to the closed-form cap; 11.0 at current funding), per v1.5. |
| N10 | Superseded by v1.5: scheduled principal 530.5 + sweep 99.5 = 629.9 (ledger unrounded). |
| N11 | WAL room now about four months (122 days, v1.5); the "26 days" text is gone. |
| N12 | Equal-installment WAL 6.92 on Case P dates, "about a third of a year of room". |
| N13 | COD resculpt 1.28x, debt and maturity held. |
| N14 | Ex 36.1: up 15.3 / down 14.1. |
| N15 | Checks use unrounded 120.537 and 167.465. |
| Note | Downside Excel now `=F16*F11/F25`. |

## Facts (r1-facts)
| ID | Fix |
|---|---|
| F1 | "and their export credit agencies" removed. |
| F2 | "one-year" removed for the 2024 contracted-solar P99 (text, Exh 36.10, Solution 36.19); ratios printed as 1.00x. |
| F3 | Replaced with "below the 75% to 80% of cost at the DFI-led contracted wind and gas deals above". |
| F4 | Exh 36.10 LNG row reworded (two-thirds of term debt plus equity). |
| F5 | Mining described as two deals, with QB2's pre-completion start noted; exhibit row says "(two deals)". |
| F6 | Now "available from an Indian state lender". |
| F7 | (a) Tail label names the markets and lenders. (b) The unlabeled package paragraph is deleted. |
| F8 | Handled with D5, under D-127. |
| F9 | Fallback wording corrected; "on which Exportgarant's 2018 cover for Case P was based". |
| F10 | Annex reference and early-draft sentence deleted; six-month rule restated in the past tense. |
| F11 | SH 130 lesson rewritten without reserve or cover claims. |
| F12 | Now cites (GIIA n.d.). |
| F13 | D-127 applied: generic "provincial contracting authority", "a 20-year regulated auction contract", "a distribution-company supply auction". |
| F14 | Recast as the book's view ("In this book's view", "in our experience"). The DFI claim in Solution 36.19 is removed. |

## Novice (r1-novice)
| ID | Fix |
|---|---|
| 1 | Notation $D_{t-1}$ for the opening balance. |
| 2 | Unitary charge. |
| 3 | DBFM glossed, with ssec:58.1.1. |
| 4 | Equations renumbered. |
| 5 | Total funding requirement defined inline. |
| 6 | Same fix as N1. |
| 7 | Money step $580.8 \times 1.30/1.463$ shown; "operating costs, which do not fall with output". |
| 8 | Now "Brazil's high real interest rates", with the real rate stated. |
| 9 | P99 test shown in full (13.36, 16.35, k 1.506, 139.3). |
| 10 | Operating-leverage paragraph rewritten on year 15 (1.50 multiplier, 33.6%). |
| 11 | "sculpting target is set below the LLCR test level". |
| 12 | (i) The 2,666.6 debt is explained. (ii) Reserve sized at a stated 7.00% deposit rate (218.8, nominal 245.8 shown); it was 208.4 at the loan rate. (iii) Kept at 118.9 (118.94). |
| 13 | Option (b) profile stated. |
| 14 | Chapter 11 glossed, TIFIA expanded with sec:29.5, prepackaged glossed with ssec:64.8.2. |
| 15 | Both Indiana figures stated with dates and no implied cause; swap liability cited (Bond Buyer 2014). |
| 16 | Merchant 4.49. |
| 17 | Step 5 added (26.9 / 79.9). |
| 18 | Same fix as N4. |
| 19 | Closed-form inverse scaling, with the unrounded 1.237. |
| 20 | Same fixes as N5 and N6. |
| 21 | ABDB expanded; "A loan" and "B loan"; ssec:29.4.4. |
| 22 | Common terms agreement glossed, with ssec:51.1.3. |
| 23 | Explains why LLCR excluding the DSRA (1.36x) exceeds 1.35x: discount-rate basis. |
| 24 | Covered by the v1.5 rewrite: separate ECA schedule; DSCR exactly 1.35x on scheduled debt service to June 2027, rising after as the sweep shrinks installments. |
| 25 | Same fix as D8. |
| 26 | Scene attributions and reply fixed. |
| 27 | "CFADS is 1.91 times the interest"; six-month DSRA added to the situation. |
| 28 | Close: 35% above, can fall about 26%. |
| 29 | Glosses added for cash sweep, lock-up level (sec:37.4), zero-coupon and monoline (ssec:3.6.1), OREC (ssec:71.3.2) and hydrology reserve. |

## Line (r1-line)
| ID | Fix |
|---|---|
| 1 | Opening meta-sentences and the "Somewhere" opener cut; paragraph 7 deleted, with its judgment clause kept at the end of paragraph 2. |
| 2 | Cut. |
| 3 | Fixed. |
| 4 | Cut. |
| 5 | Cut. |
| 6 | Fixed. |
| 7 | Fixed. |
| 8 | Zinger and both superlatives removed. |
| 9 | Fixed. |
| 10 | Paragraph deleted. |
| 11 | Lines 341 and 520 rewritten as statements; the LNG chain cut to two reasons. |
| 12 | Fixed. |
| 13 | Fixed. |
| 14 | Colon reveal and moral removed. |
| 15 | Fixed. |
| 16 | Fixed. |
| 17 | Port Arthur repeat cut to one sentence. |
| 18 | Fixed. |
| 19 | Spellings fixed. |
| 20 | Directional sentence added. |
| 21 | \cref fixed. |
| 22 | Drivers cut to direction, mechanism and one anchor each; the Gulf and LNG repeats are gone. |
| 23 | Fixed. |
| 24 | Fixed. |
| 25 | (a) Body-language line cut. (b) Verb added. (c) Last line fixed. (d) One stage business kept. |
| 26 | All production apparatus removed from reader text: IDs only in `%` comments, no slugs, Case Bible or Annex references. |
| 27 | Checklist and red flags merged and reworded. |
| 28 | Close rewritten: no recap, one concrete failure, ends on the open problem with ch:37 mid-sentence. |
| 29 | Duplication removed; the exhibit's memo lines carry the reconciliation. |
| 30 | Run-in labels in ssec:36.2.4 turned into topic sentences; "Two errors are common" removed. |
| 31 | Tier 1 solutions condensed to answer, reference and check. |
| Length | The identified padding was cut, about 1,300 words. The domain, novice and facts fixes added about 1,000 words: authority and contractor lenses, dual profile, ECA-tranche rule, Case P restructure, explanations, glosses and USD equivalents. Net about 21,500 words excluding Sources (22,200 with them), against 22,000 excluding Sources before. |

## Consistency (r1-consistency)
| ID | Fix |
|---|---|
| 1 | Equations renumbered in the chapter, registry, R-005/R-116 and the brief key formulas. |
| 2 | Same fix as Line 26. |
| 3 | Tail measured to April 30, 2046: about 11.8 years. |
| 4 | Now cites ch:62 and ch:63. |
| 5 | Covered by the v1.5 rewrite; every figure is now from the ledger (incl. the sweep row and 11.5% within 24 months). |
| 6 | "After 15 weeks of negotiation". |
| 7 | (a) Tamsarit Hydro. (b) Campo Albarrán Solar. (c) Shofirkon Sun Power. (d) Kenogami Justice Partners. (e) All names registered in Part 5A. |
| 8 | Unitary charge; contracting authority; borrower → project company; American spelling. |
| 9 | Every abbreviation expanded at first use (DSCR, CFADS, COD, PPP, PPA, ECA, DFI, IFC, LNG, SOFR, IRR, ABDB, TIFIA, OECD, CCSU, EPC, LD). PABs, OPBA and the like are written in full. |
| 10 | Forward references added (lock-up, modeling bank, prepackaged, cash sweeps). |
| 11 | Cross-references added: Indiana ssec:14.12.3, Dulles ssec:21.7.2, Ocean Wind ssec:14.12.2, Dogger ssec:11.3.3. Retold detail trimmed. |
| 12 | cl:36.1 registered and labeled. |
| 13 | Excel added for eq:36.4 (MIN plus flags), eq:36.6 (bucket row) and eq:36.7 (SUMPRODUCT WAL plus check), with layouts. |
| 14 | Block moved to a standalone Sizing sheet with its own Flag_Repayment. The first-period test is computed in the row. sec:42.2 is described as the Case P live sculpting check. |
| 15 | All empty cells filled with "--" or "n/a"; LLCR moved to the Result column; notional balances added to the Exh 36.8 note. |
| 16 | Ratios printed as 1.00x and 2.00x. The k columns are labeled "factor". "Seven-year" is spelled out. |
| 17 | USD equivalents at stated illustrative rates for CAD, EUR, GBP, MXN and BRL. Nominal basis stated in each example. |
| 18 | Exr 36.11 Oti Valley Power Company Ltd (2026); Exr 36.12 Waalhaven Logistiek B.V. (2026). |
| 19 | GIIA n.d. |
| 20 | `\x` taken out of math; \cref casing fixed; "note" instead of "footnote". |
| 21 | Close fixed; Port Arthur repeat cut. |

## Round 2

Build OK (55 pages, 0 overfull boxes); scan 0 hits.

| Report | Item | Fix |
|---|---|---|
| Domain | 1 | Tail: "no demand or price risk" and "demand, price or renewal risk". Red flag in 36.13 changed to match. |
| Domain | 2 | COD-delay sentence now says the DSCR stays below 1.35x even after resculpting to a level profile, citing ssec:36.2.4. |
| Domain | 3 | Close: "falls by a third or more, well past the 26% the cushion absorbs". |
| Domain | 4 | Country driver now states its direction for the DSCR (weaker credit pushes the target up), citing sec:36.14. |
| Facts | 1 | Same fix as Domain 1. |
| Facts | 2 | The mini-perm claim is limited to the US bank clubs that financed LNG export plants in 2023. |
| Facts | 3 | Exh 36.6 note: "up to 22 years depending on the sector listed in its Appendix I". |
| Facts | 4 | Solution 36.18: "This book has no verified worst-year record...". |
| Facts | PF2 | Checked against facts/uk-pfi.md item 8. The "launched at 75:25" wording is replaced with the accurate statement: PF2 planned 20% to 25% equity, but all six projects closed at about 10:90 (NAO 2018). |
| Numbers | 1 | Exh 36.14 downside minima corrected to 1.27x and 1.24x. |
| Numbers | 2 | Sweep runs 2027 to mid-2032; memo line reads 2027–2032; narration adds that the sweep repays the tranche by June 30, 2032. |
| Numbers | 3 | Ex 36.11 shows 4.50, with a rounding note; Step 2 uses 4.50. |
| Numbers | 4 | Exh 36.13 note: printed figures add to 630.0 because of rounding (530.46 + 99.49 = 629.95). |
| Numbers | 5 | Bucket block moved to rows 40–43. Solution 36.15 aligned: F27–F29, MIN in F32, F30 unused. |
| Numbers | Note | Downside slack now "less than four ten-thousandths". |
| Novice | 1 | Same fix as Numbers 5. "Column of constants" is reworded: F27 links to F16, and F28 holds the downside formula. |
| Novice | 2 | "before any sweep" added. Narration explains that sweeps are applied pro rata against remaining installments, so the installments after 2027 are already net of the forecast sweep. |
| Line | 1 | "in our experience" cut. |
| Line | 2 | Orphan stage line replaced with "Tomasz said". |
| Line | 3 | "the concession Pieter had spent credit to win". |
| Line | 4 | Six-month-rule sentence moved to ssec:36.6.1. |
| Line | 5 | "base-case funding requirement of USD 854.6 million", in the body and in Solution 36.13. |
| Line | 6 | LNG gearing sentence deleted. |
| Line | 7 | Filler cut. |
| Line | 8 | ", and no further" cut; trailing space removed. |
| Line | 9 | Tail paragraph now opens with the claim; the D-011 label moves to its own closing sentence. |
| Consistency | 1 | Same fix as Numbers 5. |
| Consistency | 2 | Same fix as Numbers 2. |
| Consistency | 3 | Pieter van Wijngaarden (Castellan's lead arranger), Tomasz Wierzbicki and Kilnworth Power International (lead sponsor) introduced by role before the scene. |
| Consistency | 4 | Climate Change Sector Understanding (CCSU) expanded at first use (Exh 36.6 note) and abbreviated afterward. "Indexed to the consumer price index" replaces CPI-indexed. |
| Consistency | 5 | "borrower" changed to "the project company". |
| Consistency | C1 | u08 brief lines 404 and 723 renumbered. |

Not changed by the writer:
- C2: Case Bible 1.6 repayment row, Annex P 3.6 and the Ch 42 brief, flagged for the editor.
- C3: the ledger label, which the coordinator reports is now corrected.
