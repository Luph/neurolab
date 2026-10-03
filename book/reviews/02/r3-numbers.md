# Chapter 2, round 3: numbers review

Reviewer role: numbers auditor (standards 12.4). Script: `/tmp/claude-0/-home-user-neurolab/a8d2e1e2-d243-5cdc-b359-eb0b0ebba7b3/scratchpad/review-02/recompute_r3.py`. The round 1 and round 2 scripts were re-run for the unchanged figures.

## Verdict: FAIL

Both round-2 items are fixed, and every new number recomputes correctly. Three defects remain, all in Exhibit 2.3 and the sentence in Step 2 that it summarizes. The worst is that the exhibit mixes leverage figures with and without the dividend restraint. Each is a one-line fix.

## Round-2 items

| R2 | Status | Check |
|---|---|---|
| 1. Approval amount and accounting step left out the standby | Fixed | Step 1: 292.2 + 29.2 = 321.4 committed. Step 4: 292.2 + 25.3 = 317.5 drawn after a 14% overrun, with the effect on cover ratios stated. Step 6: "up to USD 321.4 million". |
| 2. Standby fees under-described | Fixed | "before the standby facility's fees" now appears in Exhibit 2.3, Step 3 and the drill. Step 2 gives the upfront fee: 0.0225 x 29.2 = 0.657, "about USD 0.66 million". |

## New numbers recomputed (all correct)

- **Cushion without the policy:**
  - Breakeven EBITDA 608.0/3.50 = 173.71, printed as 173.7; a fall of 4.76%, printed as 4.8%.
  - After a full 29.2 call: 637.2/182.4 = 3.493x, printed as 3.49x; 1.2 to spare; breach at a fall of 0.19%, printed as 0.2%.
- **Dividend restraint:**
  - Half of 67.2 is 33.6. Net debt 608.0 - 33.6 = 574.4, which is 3.149x, printed as 3.15x.
  - Fall that breaks the covenant before a call: 10.03%, printed as 10.0%.
  - After a full call: 603.6, which is 3.309x, printed as 3.31x. Breakeven EBITDA 172.46, printed as 172.5; a fall of 5.45%, printed as 5.5%. This meets the "about 5%" policy.
- **Standby and losses:** standby 58.4 - 29.2 = 29.2; GLA pays 29.2 and the standby 25.3; worst case 97.4 + 29.2 = 126.6.
- **Solution 2.7 cross-reference:** 7.5% cap, 5.5% cushion; consistent.
- **Drill:** "halved 2025 dividend to keep a 5.5% EBITDA cushion"; consistent.
- **Alto Huelén settlement:** pay-as-produced, settled at the wind farm's node, 80% of output. Qualitative, and stated the same way in Example 2.1 and Step 4. No arithmetic depends on it.
- **Unchanged figures:** everything listed in r1/r2 still recomputes: ladder, Examples 2.3 to 2.5, drill, Solutions 2.6 to 2.9, 2.11 and 2.14, real-case figures, and Llano Pardo and Case P.

## Defects

1. **Exhibit 2.3 mixes leverage figures with and without the dividend restraint.** (exh:2.3, rows "Parent net debt to EBITDA, construction", "after COD" and "Covenant".)
   - The project-finance column shows 3.33x for construction and after COD, and "30.4 headroom". All three exclude the restraint.
   - The next rows give 3.31x after a call and a 10.0% / 5.5% EBITDA cushion. These include the restraint.
   - A reader comparing 3.33x (before a call) with 3.31x (after a call) sees leverage fall when the call adds debt.
   - Required fix:
     - Construction row and after-COD row: "3.15 with dividend restraint (3.33 without)". The figure is 574.4/182.4. The retained cash still lowers net debt after COD, and the note already assumes no project dividends in that year.
     - Covenant row: "Met; 64.0 headroom with restraint (30.4 without)". The figure is 638.4 - 574.4.
2. **Step 2 calls USD 29.2 million "the most the headroom allows". It is not.** (sec:2.8, Step 2: "Even a cap of USD 29.2 million, the most the headroom allows, ...".)
   - The headroom allows 30.4, as Solution 2.7 computes ("the largest cap ... is USD 30.4 million, 7.8% of cost").
   - Required fix: "Even a cap of USD 29.2 million, 7.5% of cost and just inside the USD 30.4 million the headroom allows, would leave ...".
3. **Exhibit 2.3, "All-in annual cost (bps)" row: "248.0 (3.1 a year more)" puts a USD figure in a bps row with no unit.** The exhibit header says USD m, but this row is labeled bps, so "3.1" reads as 3.1 bps.
   - Required fix: "248.0 (USD 3.1 million a year more)", or restore the separate row "Extra annual cost of project finance | -- | 3.1 (3.0 before agency fee)".
