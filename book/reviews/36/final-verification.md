# Chapter 36: final verification (after round 2)

File: `chapters/36-sizing-and-sculpting-debt.tex`. Checked against the six round-2 reports, the writer's Round 2 log in `r1-revision.md`, the Case P ledger v1.5 (`model/figure-ledger-case-p.md`, plus `outputs_case_p.json` for unrounded values), the Case Bible and Annex P, and the fact sheets (`facts/uk-pfi.md`, `facts/t-market-norms-2.md`).

## Verdict: PASS

All 29 round-2 chapter defects are fixed: 29 PASS, 0 FAIL. The build is clean, the prose scan reports 0 hits, and every Case P number matches the ledger at its stated rounding. The fresh read found one new mechanical defect, a missing full stop introduced by the Line 8 edit. I fixed it myself (see "Fixes made by the verifier"). Two central-file residues remain. They are not chapter defects and are listed at the end for the editor.

## Fixes made by the verifier

| # | Location | Before | After | Reason |
|---|---|---|---|---|
| V1 | sec:36.15, para. 2 (line 909) | "...before it no longer covers debt service Suppose the offtaker..." | "...before it no longer covers debt service. Suppose the offtaker..." | The full stop was lost when ", and no further" was cut (Line 8). The result was a run-on sentence. |

No other edits were made.

## Round-2 defects

| Report | # | Status | Current text (quoted) |
|---|---|---|---|
| Domain | 1 | PASS | ssec:36.5.2: "the contract carries no demand or price risk (availability PPPs, Comber's feed-in tariff, the Gulf contracts above)"; "a contract with demand, price or renewal risk"; red flag in sec:36.13: "a contract with real demand, price or renewal risk" |
| Domain | 2 | PASS | sec:36.12: "a six-month delay squeezes the same principal into fewer periods, so even after the lenders resculpt to a level profile every period's DSCR is below 1.35\x{} (\cref{ssec:36.2.4})" |
| Domain | 3 | PASS | sec:36.15: "in that half-year CFADS falls by a third or more, well past the 26\% the cushion absorbs" |
| Domain | 4 | PASS | ssec:36.10.1: "Country and counterparty risk come third for the DSCR and second for tenor: weaker sovereign or offtaker credit pushes the target up (\cref{sec:36.14})." This gives the direction only, with no figure, as required. |
| Novice | 1 | PASS | Line 215: "F27 to F30 (F27 links to F16; F28 is the downside formula below) ... \xl{=MIN(F27:F30)}". Line 533: "contracted CFADS in row 40 and merchant CFADS in row 41, with their targets in F40 and F41; bucket debt service in row 43 is \xl{=J$8*(J40/$F$40+J41/$F$41)}, and row 43 then replaces row 12". Sol 36.15: "Using the body layout, put the three amounts in F27 to F29 (F30 is unused), the debt in F32 as \xl{=MIN(F27:F29)}". Across the whole Sizing sheet (rows 8–21, 23–25, 27–32, 35–38, 40–43) no cell is used twice. |
| Novice | 2 | PASS | "equals CFADS divided by 1.35 in every period before any sweep"; "Each sweep prepayment is applied pro rata against the tranche's remaining installments, so the scheduled installments the base case shows after 2027 are already net of the forecast sweep." |
| Numbers | 1 | PASS | Exh 36.14: 1.27 in the three 70% rows (ledger 1.275x; JSON 1.274709); 1.24 in the 1.40x/75% and 1.40x/80% rows (ledger 1.245x; JSON 1.244818). |
| Numbers | 2 | PASS | Exh 36.13 memo: "Forecast cash sweep of the commercial tranche, 2027--2032"; narration: "between 2027 and mid-2032, when the last sweep retires it" and "the sweep repays it by June 30, 2032". Matches P-F09 rows 2027H1–2032H1 (last sweep 4.571 on a 5.711 opening balance; nil from 2032H2). |
| Numbers | 3 | PASS | Ex 36.11: "(9.78 contracted, 4.50 merchant; the parts add to 14.28 because of rounding)"; Step 2: "$9.78/1.30 + 4.50/2.00 = 9.77$" (recomputed 9.773). |
| Numbers | 4 | PASS | Exh 36.13 note: "the printed figures add to 630.0 because of rounding (unrounded, 530.46 + 99.49 = 629.95)". Ledger: 530.462332 + 99.487343 = 629.949675. |
| Numbers | 5 | PASS | Same fix as Novice 1. |
| Numbers | note | PASS | "with less than four ten-thousandths to spare" (1.200359 − 1.20 = 0.000359) |
| Facts | 1 | PASS | Same fix as Domain 1. The domain reviewer's wording was used. It is consistent with the facts reviewer's intent: the contract removes demand or price risk. |
| Facts | 2 | PASS | sec:36.10: "A 20-year tenor is available from an Indian state lender, while the US bank clubs that financed LNG export plants in 2023 lent seven-year mini-perms." |
| Facts | 3 | PASS | Exh 36.6 note: "which allows ECA repayment terms of up to 22 years depending on the sector listed in its Appendix I" |
| Facts | 4 | PASS | Sol 36.18(c): "This book has no verified worst-year record for UK onshore wind, so the one-year P99 (factor 0.777) is the defensible proxy" |
| Facts | PF2 (writer change) | PASS | ssec:36.3.2: "it planned equity of 20\% to 25\%, but all six PF2 projects closed at about 10\% equity and 90\% debt, the structure of the earlier private finance deals (National Audit Office 2018)". Matches `facts/uk-pfi.md` item 8 (planned 20% to 25%; as at September 2017 all six projects at about 10:90). NAO 2018 is in Sources. |
| Line | 1 | PASS | "Accreting structures like option (a) do exist, mostly with public lenders or subordinated creditors". "in our experience" no longer appears anywhere. |
| Line | 2 | PASS | Scene opens "``Six-two-nine-point-nine,'' Tomasz said." The text "right way up" no longer appears. |
| Line | 3 | PASS | "...accepting the back end at unchanged margins was the concession Pieter had spent credit to win." |
| Line | 4 | PASS | Moved to ssec:36.6.1: "Credits outside those project finance terms had to start repaying within six months of the starting point under the 2017 text (the current text allows one year), a rule Case P's first repayment, eight months after COD, would have failed." |
| Line | 5 | PASS | Body: "Against the base-case funding requirement of USD~854.6~million the slack is USD~11.0~million rather than 13.1." Sol 36.13: "against the base-case funding requirement of USD~854.6~million the slack is USD~11.0~million". |
| Line | 6 | PASS | The LNG gearing sentence is gone from ssec:36.10.1. The 52% figure remains only in Exh 36.10, as the reviewer intended. |
| Line | 7 | PASS | "The 1.25\x{} target is the request to resist." |
| Line | 8 | PASS (after V1) | ", and no further" cut; no trailing whitespace anywhere in the file. The edit dropped a full stop, which I restored (V1). |
| Line | 9 | PASS | Opens "In this book's view, tail length follows what the cash after maturity depends on and how long a restructuring would take, not the region." Ends "These are indicative judgments for contracted power and infrastructure financed by commercial banks, ECAs and DFIs in North America, Europe, the Gulf and DFI-led emerging markets in 2023 to 2026, not survey data." |
| Consistency | 1 | PASS | Same fix as Novice 1. |
| Consistency | 2 | PASS | Same fix as Numbers 2. |
| Consistency | 3 | PASS | Before the box: "Pieter van Wijngaarden, Castellan's lead arranger, had negotiated it with Tomasz Wierzbicki of Kilnworth Power International, the lead sponsor." |
| Consistency | 4 | PASS | First use (Exh 36.6 note): "Climate Change Sector Understanding (CCSU)"; "CCSU" is used afterward at lines 410, 588, 601, 660, 703, 894, 958 and 1069. Line 332: "it is indexed to the consumer price index". Line 588 keeps "the climate change and nuclear sector understandings", a generic plural covering two instruments. That is acceptable. |
| Consistency | 5 | PASS | "the days the project company has to cure a missed payment" |

Counts: Domain 4/4, Novice 2/2, Numbers 5/5 (plus the note), Facts 4/4 (plus the PF2 rewording), Line 9/9, Consistency 5/5. Total 29/29 PASS.

## Regression checks

| Check | Result |
|---|---|
| Prose scan (`scripts/scan_prose.py`) | 0 hits (rerun after V1). No `---` dashes. |
| Build (`scripts/build_chapter.sh chapters/36-sizing-and-sculpting-debt.tex`) | BUILD OK, 55 pages, 0 overfull boxes (the limit was none over 10pt; there are none at all). 11 underfull boxes, all cosmetic. |
| Undefined references | 0 chapter-36 references are undefined: every `*:36.*` reference resolves to a label in the file. The standalone build reports 69 cross-chapter references as undefined, as it must. All 69 are present in `bible/anchor-registry.md`. The full-book build resolves them. |
| Case P numbers against ledger v1.5 | All match. Debt 629.9 (629.9497); downside 630.1 (630.138), slack 0.2; LLCR debt 638.4, slack 8.5; gearing debt 643.1 (643.081), slack 13.1; 640.9 (75% × 854.55); 857.4; slack 11.0; tranches 189.0 / 138.6 / 63.0 / 239.4 (30/22/10/38%); gearing 73.7%; LLCR 1.42x / 1.36x, fails 1.40x by 0.04 without the DSRA; ECA WAL 6.92 (6.9158), term 13.16, largest 3.8%, first repayment 8 months, 11.5% within 24 months; other / all WAL 8.17 / 7.79; installment 3.85% ≈ 7.27; 530.5 + 99.5; DSCR exactly 1.35x 2021H2–2027H1; average 1.55x / 1.39x / 1.35x; P-F36 grid (debts, binding tests, downside minima, IRRs); COD resculpt 1.28x (P-F19); margins 4.10 / 4.60 / 5.10% and a 50% sweep from January 2027 (Case Bible 1.6); ECA cap 224.1; term-sheet dates July 14 and October 27, 2017; tail 11.8 years to April 30, 2046. |
| Other edited arithmetic | Drill: 8.0 / 11.6 / 1.3 / 22.1 / 15.9%, 72% of the uplift; close 1 − 1/1.35 = 25.9%; Ex 36.11 Step 2 = 9.77. All recomputed and correct. |
| Cross-references in edited passages | ssec:36.2.4, sec:36.14, ssec:36.6.2, ssec:36.9.1, sec:36.12, ssec:51.5.2, ssec:51.1.3: all resolve or are registered. |

## Fresh read (defects only)

- V1, above: the only new defect a reader would catch. Fixed.
- Lines 621–622 hold a double blank line left by the Line 6 deletion. It has no effect on the output and needs no action.

## Central-file items for the editor (not chapter defects)

- **C1 residue.** `bible/briefs/u08.md` lines 404 and 723 are renumbered, but line 524 still reads "Equation 36.5, repurposed (R-005): the average-life constraint". It should read eq:36.7.
- **C2.** Done: the Case Bible 1.6 commercial-tranche row now describes D-128, and the phrase "pro rata on the common profile" no longer appears in `bible/`.
- **C3 residue.** The P-F09 total label now reads "2027-2032H1", which is correct. The ledger's narrative row "Why the average exceeds 1.35x" (ledger line 239) still says the commercial tranche "is repaid by sweep in 2031H2". The ledger's own period rows show it repaid in 2032H1 (opening 5.711 in 2032H1, nil from 2032H2). The chapter follows the period rows and is correct.
- **C4.** The coordinator's v1.5 note (535.287 / 94.662) still differs from the ledger. The chapter follows the ledger.
