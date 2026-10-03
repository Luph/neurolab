# Chapter 2 writer notes (pilot, narrative-heavy)

File: `chapters/02-what-project-finance-is.tex` (label `ch:2`). Date: 2026-10-03.

## Word count

- pdftotext of the standalone PDF: about 19,100 words (includes running heads, table cells and sources).
- Source count excluding LaTeX commands and TikZ: body (opening to the close, Section 2.12) about 14,900; exercises and solutions about 3,550; sources about 380.
- Brief target: 10,500. The chapter is over target. Nothing was padded: the brief requires five worked examples, two frameworks, an annotated clause, four real cases (SunEdison, Sabine Pass, Hyperion, Northvolt), a seven-step walkthrough with a summary exhibit, a Case P scene plus six fit-test paragraphs, a notebook, a drill, and 14 exercises with complete solutions (two tables and a model clause among them). Every element is at the depth the standards ask for. If the editor wants the length nearer the target, the cleanest cuts are (a) Section 2.4.2's last paragraph and 2.4.4's second paragraph, (b) the Moody's paragraph in 2.5.2, (c) Exercise 2.12's table (answer in prose). I have not made them.

## Deviations from the brief (and why)

1. **Example and exhibit labels renumbered to print order.** The brief's locked TOC places Example 2.2 (ssec:2.2.2) and Example 2.3 (ssec:2.3.2) before Example 2.1 (ssec:2.5.1), and Exhibit 2.3 (ssec:2.1.2) before Exhibits 2.1 (2.4) and 2.2 (2.8). Counters print in order of appearance, so the registry labels could not match printed numbers (style sheet 3.2 requires they match). Nobody outside Ch 2 cites these labels (grep of all briefs and the Case Bible). New labels, by position:
   - `ex:2.1` Climbing the recourse ladder (ssec:2.2.2) — was ex:2.2
   - `ex:2.2` Assigning the 2018 soiling loss at Llano Pardo (ssec:2.3.2) — was ex:2.3
   - `ex:2.3` Two ways to fund a wind farm (ssec:2.5.1) — was ex:2.1
   - `ex:2.4`, `ex:2.5` unchanged
   - `exh:2.1` The two directions of ring-fencing (ssec:2.1.2) — was exh:2.3
   - `exh:2.2` Project finance and its six neighbors (Illustrative) (end of sec:2.4) — was exh:2.1 (status label added because the example column is illustrative)
   - `exh:2.3` Board paper summary ... (USD m) (Illustrative) (sec:2.8) — was exh:2.2
   **Registry update needed.** The GLA wind farm is therefore introduced in the recourse-ladder example (Ex 2.1), and Ex 2.3 does the leverage arithmetic.
2. **New clause anchor `cl:2.2`**: the model answer to Exercise 2.10 is a `clause` box (style sheet 4.7 requires drafting solutions in a clause box), which takes the next clause number. Caption: "Single-purpose and separateness undertaking, Llano Pardo common terms agreement (Illustrative)". Registry update needed.
3. **Recourse ladder after completion (Example 2.1, Exercise 2.8).** The brief's answer "151.9 before completion, 97.4 after" for the capped cost-overrun undertaking is only right if no overrun occurred. With the 54.5 overrun funded before completion (the example's premise), GLA has 151.9 at risk after completion as well; completion releases the contingent promise, not money already spent. I print 151.9 / 151.9, and state explicitly that without the overrun the rung's exposure is 155.8 (cap) to completion and 97.4 after. Completion guarantee: 444.1 before, 151.9 after (brief gave only "exposure falls to 97.4 at completion", same issue). Exhibit 2.3 carries "151.9 (97.4 if no overrun)". Please confirm with the numbers auditor.
4. **Example 2.4 all-in difference.** Brief: "about 104 bps a year (plus agency fee 2.6 bps) ... about USD 3.0 million". Printed: 104.0 bps before the agency fee (USD 3.0 million) and 106.6 bps with it (USD 3.1 million); the drill uses 248.0 all-in including agency (brief's figure). Exercise 2.14's B25 gives 103.9 (unrounded components); the solution explains the difference.
5. **Clause 2.1** is drafted for the Alto Huelén wind-farm common terms agreement (Chile, 2024, English law) rather than for Llano Pardo, so that Exercise 2.10 (Llano Pardo) is a genuine adaptation task (grid-asset transfer to ELNACOR; Grupo Arismendi group companies).
6. **Example 2.3 (soiling)** treats the USD 441 thousand as the combined soiling-plus-firmware shortfall (as the Ch 1 spec states) and assigns only the soiling part; the firmware fault is named as a separate risk with a different owner. No new figures.
7. **Walkthrough**: dated the board paper June 10, 2024 and the turbine reservation deadline July 15, 2024 (brief said "board must decide by July 2024"; drill sets the board meeting Thursday June 20, 2024). Both are illustrative.
8. **Opening**: per the brief, I do not say the yieldcos filed or that USD 16.1 billion was debt. I did not state that every project "kept paying its lenders" (the fact sheet supports only that neither yieldco was filed or consolidated and both were sold as going concerns); the text says the project lenders "kept their claims on their own projects".
9. **Llano Pardo battery episode (2.6.2)** cites debt outstanding at end-2024 of USD 32.9 million from exh:1.4 (base case 32,929 k); no other new figures.

## New terms not in the glossary canon

- **recourse ladder** and **project finance fit test**: set with `\term{}` per style sheet 4.5 (framework names at first definition); canon has no rows for framework names. Request canon rows (home ssec:2.2.2 and sec:2.7) or confirm frameworks are listed only in the registry.
- **separateness undertaking**: used in plain words, not bolded (the canon has only "single-purpose undertaking"). Suggest a canon row (home ssec:2.1.2): "A covenant by the project company to keep its own books, accounts and decisions separate from its owners' and to deal with them only at arm's length."
- PPA and EPC contract are bolded at ssec:2.3.1 because the canon now homes them there (R-123).
- "halo" is used in quotation marks with a forward reference to Ch 60; not defined here.

## Facts verified beyond the fact sheets

- Jensen, Michael C. 1986. "Agency Costs of Free Cash Flow, Corporate Finance, and Takeovers." American Economic Review 76 (2): 323–329 (web search, SSRN listing https://papers.ssrn.com/sol3/papers.cfm?abstract_id=99580). Used for the agency-cost argument in ssec:2.5.2 (paraphrased, no quotation).
- Moody's 1983–2021 default/recovery figures come from `facts/t-ratings-2.md` (not a brief-named sheet, but a delivered sheet whose teaching angle names Chapter 2).
- Eurotunnel facts in the close and Exercise 2.12 come from `facts/eurotunnel.md` (treaty date, ~50-bank GBP 5 billion underwriting, ~GBP 8 billion debt at opening "approximately", September 1995 suspension).
- Name checks (web search 2026-10-03): "Generadora Litoral Andino" — no exact match; near miss "Generación Litoral S.A." (an Argentine generator with a Santiago address), different name, flagged only. "Alto Huelén" — no wind project found.

## Flags for reviewers

- General market statements without a sheet, kept qualitative: US projects commonly use LLCs; reserve-based loans usually redetermined twice a year (consistent with `t-rbl`); facility agreements commonly exclude non-recourse project-subsidiary debt from covenant net debt; PPAs of this kind usually contain termination-payment provisions. Domain expert please confirm wording.
- Example 2.4 cost figures are labeled illustrative and "not market data" (per brief); the notebook's 5% rule of thumb is labeled as derived from the chapter's examples.
- Case P: scene uses only inputs (USD 14.8 million, USD 12 million, 75%, 4.1 GW, BBB-). Tomasz's dollar-tariff error is left unresolved and pointed to Ch 59; Philippa's under-budget mistake is not flagged (pointed to Ch 4). The statement that Kilnworth "had project-financed plants before" follows the brief ("Kilnworth used to lender control"); the Case Bible does not say how its earlier plants were financed. The Phase-2 condition of the co-development agreement is from Annex P 1.14.1.
- `\raggedright` placed at the start of the `sources` list to stop long URLs overflowing (hyphenated URLs do not break). Suggest the coordinator add `\raggedright` (or the url `hyphens` option) to the `sources` environment in pfbook.sty and remove it from the chapter.
- Exhibit 2.2 "Home chapter" column uses `\cref{ch:N}`; row 1 is a self-reference to Chapter 2.

## Build and scan results

- `bash scripts/build_chapter.sh chapters/02-what-project-finance-is.tex`: BUILD OK, 46 pages. Overfull boxes: 1 (0.27pt, under the 5pt limit). Undefined references: cross-chapter only (ch:1, 3, 4, 8, 13, 15, 17, 21, 22, 26, 28, 30, 32, 38, 47, 51, 52, 57, 59, 60, 61, 62, 64, 66, 76, 77, 82; ex:1.9; exh:1.1, 1.3, 1.4, 1.10; sec:18.1, 31.3, 37.4, 75.3; ssec:6.3.2, 7.3.1, 8.2.1, 14.18.1, 36.1.1, 82.7.2). All cited labels exist in the anchor registry (scripted check).
- `python3 scripts/scan_prose.py`: 0 hits. Em dashes (`---`): 0. Manual sweep done for vague This/That openers, false contrasts, zingers, rule-of-three cadence, colon reveals and character tics; fixes applied.
- All numbers recomputed in Python (`scratchpad/ch02/nums.py`): 4.94x, 4.02x, 3.33x, 127.8, 30.4, 54.5, 58.4, 444.1, 151.9, 155.8, 13.83 (3.55%), 2.35, 50.4/6.4 bps, 104.0/106.6 bps, USD 3.0/3.1 million, 2.6 bps agency, drill 2.7 bps waiver / 162.7 / 85 bps / USD 2.5 million / 50.5 headroom, rooftops 15.6%, 55 kWp, USD 86,900, Exercise 2.14 thresholds 257.2 / 215.9 / 33.5.
