# Chapter 2, round 2: numbers review

Reviewer role: numbers auditor (standards 12.4). I recomputed every figure in the revised chapter again. Scripts:
- `/tmp/claude-0/-home-user-neurolab/a8d2e1e2-d243-5cdc-b359-eb0b0ebba7b3/scratchpad/review-02/recompute.py` (round 1)
- `recompute_r2.py` in the same folder (round 2)

## Verdict: FAIL

All six round-1 defects are fixed, and every printed number recomputes correctly. Two small labeling defects remain in the new standby-facility material. Each is a one-line fix. After that the chapter passes on numbers.

## Round-1 defects: status

| R1 | Status | Check |
|---|---|---|
| 1. Overrun cap larger than covenant headroom | Fixed | Ex 2.3 now shows the problem: 608.0 + 54.5 = 662.5, so 3.63x, a breach of 24.1. At the full cap, 666.4 gives 3.65x, a breach of 28.0. Headroom covers 30.4/58.4 = 52% of the cap. The "funding from cash does not help" logic is correct for net debt. In the board paper the cap is 7.5% x 389.6 = 29.22, printed as 29.2. If called: (608.0 + 29.2)/182.4 = 3.493, printed as 3.49x, with 638.4 - 637.2 = 1.2 to spare. Standby: 58.4 - 29.2 = 29.2. On a 14% overrun GLA pays 29.2 and the standby pays 54.5 - 29.2 = 25.3. Worst case 97.4 + 29.2 = 126.6, before and after completion (97.4 with no overrun). Sol 2.7: largest cap 30.4/389.6 = 7.80%; check (608.0 + 30.4)/182.4 = 3.50x. Drill: 1.2 of headroom. Notebook red flag and checklist added. |
| 2. Bélanou "fraction of a percent" | Fixed | Now "a few percent, the range Alto Huelén showed". This agrees with the P ledger: P-F07 gives (8.97 + 9.95)/855.1 = 2.2%, or 4.7% with development costs. |
| 3. Sabine Pass USD 2.3 bn | Fixed | Now "Once BG had added volumes ... approximately USD 2.3 billion". The four original SPAs come to 1,960; adding BG's extra volumes gives 2,272 (fact sheet items 6 and 7). |
| 4. Soiling compared with the O&M fee | Fixed | Revenue 7,841 - 7,253 = 588, printed as 0.59. Distribution 1.82 to 1.38 (441). Firmware fault: 11% of trackers for 23 days. The soiling share is stated as unknown but "most". "Of the same order as a full year's fee" (0.59 against 0.41) holds. Cap range 0.5 to 1.0 x 412 = 0.21 to 0.41. |
| 5. Solution 2.11 margin claim | Fixed | 0.75 x 18.6 = 13.95, printed as 14.0. 2.9/(13.95 x 9.4) = 2.21%, about 220 bps, which is above Alto Huelén's 195 bps margin. "an USD" removed. |
| 6. Llano Pardo units | Fixed under D-126 | Prose is now in USD million throughout: 16.3, 65.1, 49.1, 48.8, 32.9, 0.41, 0.44, 0.59, 7.25/7.84, 1.82/1.38, 1.1. No "USD thousand" remains. |

## Full recomputation of the revised chapter (all correct)

- **Ex 2.1 (ladder), at the lenders' first-ask 15% cap:**
  - Overrun 54.54, printed as 54.5. Cap 58.44, printed as 58.4. Debt 292.2, equity 97.4.
  - Rungs: 444.1/444.1, 444.1/151.9, 151.9/151.9, 97.4/97.4. Ex ante 155.8.
  - Gaps between rungs: 292.2 and 54.5.
  - The table, Exercise 2.8 and Solution 2.8 are consistent. Using 15% in Ex 2.1 does not conflict with the board paper's 7.5%, because Ex 2.1 now labels it "the rung the lenders' first term sheet asks for".
- **Alto Huelén PPA (new):** 80% of output, 15 years, US dollars, BBB- copper miner. No arithmetic depends on it, and it is stated the same way in Ex 2.1 and Step 4.
- **Ex 2.3:**
  - Leverage 2.80x, 4.94x, 4.02x and 3.33x.
  - Headroom 127.8 (32.8% of cost), with 30.4 left after the equity.
  - 389.6/127.8 = 3.05, printed as 3.0.
  - Failure case: "97.4 (plus any overrun it funded)".
- **ssec:2.5.1 gearing:** 97.4/389.6 = 25%, "a quarter".
- **Ex 2.4 and Sol 2.9:**
  - Costs: 3.86, 6.5745 printed as 6.57, total 13.8345 printed as 13.83, 3.55%; bond 1.7532 + 0.60 = 2.35.
  - Spread: 50.37 bps printed as 50.4, 6.43 as 6.4, agency fee 2.62 as 2.6. Subtotals 245.4 and 141.4; all-in 248.0.
  - Difference 104.0 bps (USD 3.04m) and 106.6 bps (USD 3.11m). Common wrong answer 37.8 bps, "a quarter" low.
  - 14 - 3 = 11 months.
- **Ex 2.5:** 0.0551 MWp (55 kWp); USD 86,916; 15.6%.
- **Drill:**
  - Waiver fee 0.974; 2.66 bps; 162.7 bps (about 163).
  - Saving 85.3 bps, which is USD 2.49m on 292.2. 2.49/182.4 = 1.37%, printed as 1.4%.
  - Headroom at 4.25x after COD: 50.5. Remaining headroom at the 29.2 cap: 1.2.
- **Exhibit 2.3:** every cell matches the examples and the walkthrough.
- **Sol 2.6, 2.7 and 2.14:**
  - Sol 2.7 wrong answer 272.35, printed as 272.4.
  - Sol 2.14: B25 103.94; B26 257.2; B27 215.9; B28 33.5 (18.4%). The Excel formulas implement the math shown.
- **Real-case figures:**
  - SunEdison: 16.1 / 11.7 / 300. The 3.8 bn TerraForm share comes from the facts review (10-Q). Notes 800 + 150 = 950 and 300. Votes 84.1% against economic interest 34.5%.
  - Sabine Pass: half the capacity (1.0 + 1.0 of 4.0 Bcf/d); 125; 115%; 2.25 to 3.00; 3.6 bn; 21 banks; 932.
  - Hyperion: 80/20; 27; 12.31; 28; 16 years; 46.03; 2.92 (about 2.9); 2049.
  - Northvolt: tranches sum to 1,615 (about 1.6 bn); 55 bn; 16/60 GWh; 285 m to 1.2 bn; 4.5 bn; 30 m.
  - Moody's: 10,452 projects; 67% coverage; 4.8% = Baa3; 79.5%; 62%; 72.5/80.8; marginal default rate at single-A by about year seven.
  - PNG LNG: shares sum to 100.0%.
  - Eurotunnel: about 50 banks; GBP 5 bn; about GBP 8 bn.
- **Llano Pardo and Case P:** unchanged figures re-checked against brief 1.A and the Case Bible, Annex P and P-F01: 14.8, 12, 75%, 70:30, 4.1 GW, BBB-, 450 to 650 MW. Dates and weekdays as in round 1 (September 17, 2015 a Thursday; June 10, 17 and 20, 2024 a Monday, Monday and Thursday).

## Defects

1. **The board paper's approval amount and accounting step leave out the standby facility it recommends.** (sec:2.8, Step 1 and Step 6.)
   - Step 1 asks the board to approve "a limited recourse project financing of USD 292.2 million". Step 2 then adds "a USD 29.2 million standby facility inside the project financing". The facilities actually committed total 292.2 + 29.2 = 321.4.
   - Step 6 says the group accounts will show "its USD 292.2 million of debt". With the 14% overrun, project debt would be 292.2 + 25.3 = 317.5, and up to 321.4 if the standby is fully drawn.
   - Required fix:
     - Step 1: "a limited recourse project financing of USD 292.2 million of senior debt plus a USD 29.2 million standby facility".
     - Step 6: "its USD 292.2 million of debt (up to USD 321.4 million if the standby facility is drawn)".
2. **The standby facility's cost is under-described.** (exh:2.3 row "Transaction costs"; Step 3; drill paragraph 2.)
   - The rows say "13.83, before the standby commitment fee" and "before the standby facility's commitment fee". At the example's own 2.25% upfront rate, the standby would also carry an upfront fee of about USD 0.66 million (0.0225 x 29.2), which is excluded as well.
   - Required fix: change all three places to "before the standby facility's fees". Optionally add "(an upfront fee of about USD 0.66 million at the example's 2.25%, plus a commitment fee)" in Step 3.
