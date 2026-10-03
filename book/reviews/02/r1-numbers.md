# Chapter 2, round 1: numbers review

Reviewer role: numbers auditor (standards 12.4). Pilot chapter, so every figure was recomputed. Script: `/tmp/claude-0/-home-user-neurolab/a8d2e1e2-d243-5cdc-b359-eb0b0ebba7b3/scratchpad/review-02/recompute.py`.

## Verdict: FAIL

Almost all of the arithmetic is correct. Three defects remain that an editor would not pass: one gap in the analysis behind the board paper, one wrong magnitude in the Case P fit test, and one real-case figure that does not follow from the inputs printed beside it.

## Writer's flag: recourse-ladder correction (writer notes, deviation 3)

**Confirmed.** The brief gives "151.9 before completion, 97.4 after" for the capped cost-overrun rung, which is wrong under the example's own premise. The USD 54.5 million overrun has already been funded before completion. Completion releases only the promise to fund future overruns. It does not return money already spent, so the exposure is 151.9 / 151.9. The completion-guarantee rung is 444.1 / 151.9 for the same reason. The figures 155.8 (97.4 + 58.4) to completion and 97.4 after apply only when no overrun occurs, and that is how the chapter prints them in Example 2.1, the ladder table, Exhibit 2.3 ("151.9 (97.4 if no overrun)"), Exercise 2.8 and Solution 2.8. All of these agree with each other. Gaps in the ladder: 444.1 - 151.9 = 292.2 and 151.9 - 97.4 = 54.5. Both are correct. The brief (u01.md 2.6, Example 2.2 bullet, and 2.13, Exercise 2.8 answer) should be corrected to match, so that later chapters do not copy the old figure.

## Figures verified correct (no action)

- Example 2.1: debt 0.75 x 389.6 = 292.2; equity 97.4; overrun 0.14 x 389.6 = 54.54 -> 54.5; cap 0.15 x 389.6 = 58.44 -> 58.4. Full recourse 444.1. Completion guarantee 444.1 / 151.9. Capped undertaking 151.9 / 151.9 (155.8 ex ante). Non-recourse 97.4.
- Example 2.3: 510.6/182.4 = 2.80x; 900.2/182.4 = 4.94x; 900.2/223.7 = 4.02x; headroom 3.50 x 182.4 - 510.6 = 127.8 (32.8% of cost, "about a third"); 608.0/182.4 = 3.33x; 127.8 - 97.4 = 30.4; 389.6/127.8 = 3.05 ("3.0").
- Example 2.4: lenders' advisors 2.85 + 0.62 + 0.18 + 0.21 = 3.86. Upfront fee 6.5745 -> 6.57. Total 13.8345 -> 13.83, which is 3.55% of cost. Bond 1.7532 + 0.60 = 2.35. 50.37 -> 50.4 bps; 6.43 -> 6.4 bps. Agency fee 2.62 -> 2.6 bps. Subtotals 245.4 / 141.4; all-in 248.0. Difference 104.0 / 106.6 bps, which is USD 3.04 / 3.11 million.
- Example 2.5: 11.8/214 = 0.0551 MWp (55 kWp); 18.6/214 = USD 86,916 ("about 86,900"); 2.9/18.6 = 15.6%.
- Drill: waiver fee 0.974; 2.66 -> 2.7 bps; 162.7 ("about 163"); 248.0 - 162.7 = 85.3 bps, which is USD 2.49 million on 292.2. Post-COD headroom at 4.25x: 4.25 x 223.7 - 900.2 = 50.5. 14 - 3 = 11 months.
- Exhibit 2.3: every cell matches Examples 2.1, 2.3 and 2.4.
- Exercises and solutions 2.6 to 2.9 and 2.14: all values match. B25 103.94 unrounded (245.37 - 141.43) is correct. B26 257.2, B27 215.9, B28 33.5 (18.4%, "about 18%"). Check 257.2 x 3.50 = 900.2. Wrong answers: 272.4 (Sol 2.7); 37.8 bps, which is 75% of 50.4, so "by a quarter" (Sol 2.9). The Excel formulas B18 to B28 implement the math shown.
- Llano Pardo against the brief, 1.A: equity 16,270 -> 16.3; debt 48,809 -> 48.8; total 65,078 -> 65.1; EPC 49,100; delay damages 28,700 a day; O&M 412 for five years; LC three months; curtailment threshold 50 hours; 152 ha; 30-year lease; OY1 shortfall 7.5%; distributions 1,822 -> 1,381 (441); performance ratio 81.4% against 81.0%; contractor record 410 MW; cleaning cycles 4 -> 7; debt at end-2024 32,929; lock-up 1.15x; 14 km line; opex 1,085 ("about 1.1 million"); 50.0 MWac; 4 x 65.1 = 260.4 ("about 260"); COD December 2017.
- Case P against the Case Bible, Annex P and the P ledger: 14.8 (P-F01), 12, 75%, 4.1 GW, BBB-, co-development agreement 70:30 signed June 22, approval required by September 30, 450 to 650 MW, Emergency Power Plan March 2015, RFQ in 2016 ("won't be out before next year"), Kilnworth's 70% (Sol 2.13). April 2 to September 17 is five and a half months.
- Weekdays: September 17, 2015 is a Thursday; September 16, 2015 a Wednesday; June 10, 2024 a Monday; June 17, 2024 a Monday; June 20, 2024 a Thursday.
- Real cases against the fact sheets: SunEdison 16.1 / 11.7 / 300; 84.1% / 34.5%; notes USD 800 million at 5.875% due 2023 and USD 300 million at 6.125% due 2025; filing December 5, 2016; November 20, 2015 is five months before April 21, 2016. Sabine Pass: 125, 115%, 2.25 to 3.00, 3.6 bn, 21 banks, 932. Hyperion: 80/20, 27, 12.31, 28, 16 years, 46.03, 2.92 ("about 2.9"), 2049. Northvolt: tranches sum to 1,615 ("about 1.6 bn"); 55 bn; 16 against 60 GWh; 285 m -> 1.2 bn; 4.5 bn; 30 m. Moody's: 10,452 projects; 4.8% = Baa3; recovery 79.5%; full recovery in 62% of defaults; 72.5% / 80.8%. Eurotunnel: about 50 banks, GBP 5 bn, about GBP 8 bn.

## Defects

1. **Board paper and Exhibit 2.3: the recommended overrun undertaking does not fit inside GLA's covenant headroom. Neither the chapter nor the paper says so.** (sec:2.8 Step 1 and Step 2; exh:2.3 row "Covenant (3.50x)"; ex:2.1 last paragraph; sec:2.11.)
   - The paper recommends a cost-overrun undertaking capped at USD 58.4 million. Exhibit 2.3 reports "Met; 30.4 headroom left", but that figure assumes the undertaking is never called.
   - Example 2.3 funds GLA's equity with parent debt. If GLA funds the 14% overrun in the same way, which is the scenario in the worst-case row of the same exhibit, parent net debt reaches 510.6 + 97.4 + 54.5 = 662.5, and 662.5 / 182.4 = 3.63x. That breaches the 3.50x covenant by USD 24.1 million.
   - If the full cap is called, net debt is 666.4 and leverage 3.65x, which is USD 28.0 million (58.4 - 30.4) over the covenant.
   - Example 2.1 also says "A sponsor that can carry USD 155.8 million but not USD 444.1 million should fight for the capped undertaking". GLA's own covenant capacity is 127.8, below 155.8.
   - Required fix:
     - (a) Add a row to Exhibit 2.3: "Parent leverage if the overrun cap is called in full and debt-funded (x) | -- | 3.65 (breach)".
     - (b) In Step 2 or Step 4, add one sentence: "If the full USD 58.4 million cap were called and borrowed at the parent, leverage would reach (510.6 + 97.4 + 58.4) / 182.4 = 3.65x, so GLA must be ready to fund up to USD 28.0 million of any call from cash or new equity, or agree with its banks how the undertaking counts in the covenant."
     - (c) Mention the point once in the drill's reasoning, in the paragraph that begins "Start with whether the offer works", as the remaining weakness of the project finance route.

2. **Case P fit test, "Size: ample": "the ratio that killed the Nairobi rooftops would be a fraction of a percent here" is wrong by an order of magnitude.** (sec:2.9, fifth fit-test paragraph.)
   - The chapter's own Example 2.4 gives 3.55% for a USD 390 million wind farm. The upfront fee alone is 2.25% of the debt, or about 1.7% of cost.
   - For Bélanou, the P ledger (P-F07) gives lenders' advisors 8.97 plus upfront fees 9.95 against total funding of 855.1, which is 2.2%. Adding development costs of 21.43 brings it to 4.7%.
   - Required fix: replace the clause with "the ratio that killed the Nairobi rooftops would be a few percent here, in line with Alto Huelén's 3.55%". This uses no ledger figure, so the installment stays inputs-only.

3. **Sabine Pass fixed fees: USD 2.3 billion a year does not follow from "four ... agreements ... each for about 3.5 million tonnes a year".** (ssec:2.3.3, second paragraph.)
   - Four 3.5 mtpa SPAs (182.5 million MMBtu each, at USD 2.25, 2.49, 3.00 and 3.00) give about USD 1.96 billion a year (facts/sabine-pass.md, item 6).
   - The sheet's USD 2.3 billion for Trains 1 to 4 includes BG's later volume additions of 104 million MMBtu at USD 3.00, about USD 0.31 billion (total 2.27).
   - A reader who multiplies volume by fee cannot reach the printed figure.
   - Required fix: write "The fixed fees, about USD 2.3 billion a year for the first four trains once BG had added volumes to its contract, from buyers that were ..." or "about USD 2.0 billion a year from the four original contracts". Either form is supported by the sheet.

4. **Example 2.2 (soiling), "Capacity to absorb": the comparison with the O&M fee uses the combined soiling and firmware loss.** (ex:2.2, third paragraph.)
   - "A loss of the size seen in 2018 would exceed a full year's fee" compares 441 with 412. However, 441 is the combined soiling and firmware shortfall, and the example has just set the firmware part aside.
   - The firmware fault parked 11% of trackers for 23 days (brief 1.A.10), so soiling is most but not all of the 441.
   - Required fix: "The combined 2018 shortfall, USD 441 thousand and mostly soiling, already exceeded the operator's full annual fee; a dust year twice as bad ..."

5. **Solution 2.11: "the margin needed to recover USD 2.9 million on an USD 18.6 million loan would make every system uneconomic" is a numerical claim with no number behind it, and the loan is not 18.6.** (sec:2.14, exr:2.11 solution, last sentence.)
   - Required fix: give the figure with the chapter's own convention. Spread over a 9.4-year average life, USD 2.9 million on a 75% loan of USD 14.0 million is 2.9 / (14.0 x 9.4) = 2.2%, about 220 bps a year before any credit margin.
   - Suggested wording: "the fixed costs alone would add about 220 bps a year to a 75% loan (2.9 / (0.75 x 18.6 x 9.4)), more than the whole margin on Alto Huelén."
   - Also correct "an USD" to "a USD".

6. **Llano Pardo units are mixed against R-110 and brief 2.0 ("Llano Pardo figures cited from Chapter 1 stay in USD k").**
   - The chapter prints USD 16.3 million (ssec:2.2.1, Sol 2.2, Sol 2.4), USD 65.1 million (ssec:2.5.3, 2.5.4, sec:2.7), USD 49.1 million (ssec:2.3.1), USD 48.8 million (Sol 2.4), USD 32.9 million (ssec:2.6.2) and USD 1.1 million (Sol 2.10).
   - It also prints USD 412 thousand and USD 1,822 thousand, so units are mixed for the same deal, sometimes within a paragraph. In ssec:2.3.1, for example, "USD 49.1 million" sits next to "USD 412 thousand".
   - Required fix: either print Llano Pardo figures in USD thousand throughout (16,270; 65,078 or "about 65.1 million" only where rounding is the point; 49,100; 48,809; 32,929; 1,085), or get a coordinator ruling that USD million is allowed for rounded totals in Ch 2 and record it in the style sheet addendum. The brief's own TOC text ("USD 16.3 million") conflicts with its rule 2.0, so the ruling is needed in either case.
