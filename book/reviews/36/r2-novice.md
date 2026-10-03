# Chapter 36 review, round 2: novice

Reviewer role: novice (reader who knows only Chapters 1 to 35). I checked every round-1 defect against the revised chapter (case figures on model v1.5) and read the whole chapter again from start to finish. Where a step looked like a jump, I redid the arithmetic. Spot checks:

- Example 36.8: reserve PV at 7.00% = 218.8.
- Example 36.11: merchant share 26.9/79.9 = 33.7%; stressed year-15 cover 1.30x.
- Example 36.12: resize 491.7 × 1.237/1.35 = 450.6.
- Exhibit 36.11: LLCR 1.3228 + 7.03/135.98 = 1.37.
- Case P: 0.75 × 854.6 = 640.9; 629.9/854.6 = 73.7%.
- Solution 36.19: P99 factor 0.934.

## Verdict: FAIL

All 29 round-1 defects are resolved; defect 24 has one leftover point, carried forward as defect 2 below. The rewritten Case P section can now be followed without outside help. One new defect blocks a pass: the Excel cell map on the Sizing sheet puts two different things in the same cells. Because the chapter teaches modeling cell by cell, a reader building the workbook as instructed would overwrite one set of values with the other.

## Status of round-1 defects

| R1 | Status |
|---|---|
| 1 Opening-balance notation | Resolved ($D_{t-1}$, line 117) |
| 2 Unitary charge | Resolved |
| 3 DBFM gloss | Resolved |
| 4 Equation order | Resolved (36.4 to 36.7 in order of appearance) |
| 5 Total funding requirement | Resolved (defined inline, line 215) |
| 6 30% of principal | Resolved (25%) |
| 7 Ex 36.4 money step | Resolved |
| 8 "real interest rate" | Resolved (real rate stated and meant: 13.0% nominal, about 8.7% real) |
| 9 Ex 36.6 one test in full | Resolved (Step 3) |
| 10 Operating leverage in the binding year | Resolved (year 15, 1.50, 33.6%) |
| 11 LLCR "target" ambiguity | Resolved |
| 12 Ramp-up debt, reserve rate, rounding | Resolved (debt derivation, 7.00% deposit rate, nominal 245.8 noted) |
| 13 Option (b) 2.39x | Resolved |
| 14 TIFIA, Chapter 11, prepack | Resolved |
| 15 Indiana debt figures | Resolved (both figures dated, no implied identity) |
| 16 4.50 vs 4.49 | Resolved |
| 17 Merchant share derivation | Resolved (Step 5) |
| 18 Bucket stress reasoning | Resolved (line 566) |
| 19 Ex 36.12 resize method | Resolved |
| 20 Printout LLCR | Resolved (1.37x; LLCR debt 138.55 with scaled DSRA) |
| 21 ABDB, A loan, B loan | Resolved |
| 22 Common terms agreement | Resolved |
| 23 LLCR 1.36x vs 1.35x | Resolved (discount-rate basis, line 780) |
| 24 Case P profile, sweep, average DSCR | Largely resolved; one leftover point, see new defect 2 |
| 25 P-F36 downside not imposed | Resolved (full-test grid; note says all four tests applied) |
| 26 Scene's last line | Resolved |
| 27 Interest cover; DSRA in drill | Resolved |
| 28 "35% of cushion" | Resolved |
| 29 Glosses | Resolved (cash sweep, lock-up level, zero-coupon, monoline, OREC, hydrology reserve) |

## Defects

1. **Sizing-sheet cell map: the same cells are used twice (lines 215, 221, 533; Solution 36.15 line 1100).**
   - Line 215 puts the four constraint debts in F27 to F30, the lesser-of debt in F32 (`=MIN(F27:F30)`) and the binding flags in G27 to G30.
   - Line 533 then puts contracted and merchant CFADS in rows 30 and 31, with their bucket targets in **F30 and F31**. F30 is already the fourth constraint's debt, and row 30 already holds a flag in G30.
   - Line 215 also calls F27 to F30 "a column of constants", but line 221 makes F28 a formula (`=F16*F11/F25`).
   - Solution 36.15 places the same block in F27 to F29 with the debt in F31, so it does not match the body layout.

   A reader who builds one Sizing sheet as the text directs will overwrite the constraint table with the bucket inputs. **Fix:**
   - Move the bucket block to rows not used elsewhere, e.g. contracted CFADS row 40, merchant row 41, targets in F40 and F41, bucket debt service row 43 (`=J$8*(J40/$F$40+J41/$F$41)`), "row 43 then replaces row 12".
   - Change "a column of constants" to "a column holding each constraint's debt (F27 links to F16, F28 is the downside formula below)".
   - Either align Solution 36.15 with F27:F30/F32, or say that the exercise workbook uses its own three-row layout.

2. **ssec:36.12, line 807 against line 809 (leftover from R1 defect 24).**
   - Line 807 says the sculpted profile is "chosen so that total scheduled debt service, ECA installments included, equals CFADS divided by 1.35 in every period".
   - Line 809 then says the DSCR on scheduled debt service is 1.35x only to June 2027, and rises after that because the forecast sweep "shrinks the commercial tranche's later installments".

   Read together, the first statement is false for the base case after 2027. Neither line says how a prepayment changes the scheduled installments at close. **Fix:**
   - In line 807, write "equals CFADS divided by 1.35 in every period before any sweep".
   - In line 809, add the mechanism, e.g. "each sweep prepayment is applied pro rata against the commercial tranche's remaining installments, so the scheduled installments the base case shows after 2027 are already net of the forecast sweep".
