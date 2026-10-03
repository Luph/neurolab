# Chapter 36 review, round 2: numbers

Reviewer role: numbers auditor (standards §12.4). Scripts: `/tmp/claude-0/-home-user-neurolab/a8d2e1e2-d243-5cdc-b359-eb0b0ebba7b3/scratchpad/review-36/` (round-1 scripts, rerun) and `review-36/r2/` (r2.py, ex11.py). Case P figures were checked against `model/figure-ledger-case-p.md` (v1.5), `model/figure-ledger-case-p-changes-v1.5.md` and `model/outputs_case_p.json` (meta.version 1.5: `sizing`, `figures.P-F09`, `figures.P-F36.grid`). Revision log read: `reviews/36/r1-revision.md`.

## Verdict: FAIL

All 15 round-1 defects are fixed (table below). On a full recompute, everything not listed under Defects reproduces:
- Ex 36.1 to 36.12, including the changed Ex 36.4 at 13.0%, Ex 36.6 Step 3 and the year-15 leverage paragraph, and the Ex 36.8 reserve at 7.00%.
- Exhibits 36.1 to 36.13, and Exhibit 36.11 rerun on 569.9 GWh.
- The judgment drill and the close (1 − 1/1.35 = 25.9%).
- All 19 solutions, including the new Exr 36.19 package (factor 0.5 × 1.868 = 0.934; effective P50 DSCR 1.35 × 167.1/160.0 = 1.41x; 70.0%).
- Every Case P figure in sec:36.12, except the items in defects 1, 2 and 4.

Five defects remain. All are small.

## Round-1 defects: verification

| R1 | Status | Check |
|---|---|---|
| 1 | Fixed | (14.37 + 16.00)/120.54 = 25.2%, printed as "a quarter (25%)" |
| 2 | Fixed | 47.7% nominal and 25.5% PV both stated and correct |
| 3 | Fixed | Contracted-only column now 1.82 / 1.67 / 1.59; note correct |
| 4 | Fixed | Year-15 merchant CFADS 8.78 to 5.71 (−35.0%); bucket year-15 DSCR 1.3005x |
| 5 | Fixed | Base LLCR 1.3746 = 1.37x (exhibit and Step 5) |
| 6 | Fixed | LLCR-constraint debt 138.55, slack 2.58, DSRA scaled |
| 7 | Fixed | 569.9 GWh: 138.37 / 136.16 / 138.02; slacks 2.39 / 0.18 / 2.04; P99 minimum 1.0150 = 1.02x |
| 8 | Fixed (v1.5) | Downside 630.138 − 629.950 = 0.188, printed as about 0.2; ratio 1.200359 |
| 9 | Fixed (v1.5) | Gearing slack 643.081 − 629.950 = 13.13, printed as 13.1; 10.96, printed as 11.0, against current funding; 75% × 854.55 = 640.9; closed form 857.4 |
| 10 | Superseded (v1.5) | 530.462 + 99.487 = 629.950 (ledger and JSON agree) |
| 11 | Superseded (v1.5) | ECA WAL 6.9158 against 7.25, room 122 days ("about four months") |
| 12 | Fixed | Equal installments on Case P dates: WAL 6.92, room 0.33 |
| 13 | Fixed | COD resculpt 1.28x (1.281051, P-F19) against the 1.30x completion floor (Annex P item 8) |
| 14 | Fixed | +15.3 / −14.1 |
| 15 | Fixed | 120.537 and 167.465 used in the checks |

## New and changed material: the main checks

Ex 36.4 (13.0% nominal):

| Item | Recomputed |
|---|---|
| Base | 580.82 |
| P90 k | 1.4631 |
| P90 debt | 516.07 |
| Cost k | 1.2954 |
| Cost debt | 582.89 |
| Gearing | 43.5% |
| USD equivalent | 95.2 |
| Real rate | 1.13/1.04 − 1 = 8.65% |
| P90 debt at 6% | 866.1, against a cap of 830.2 |

Ex 36.6 Step 3:

| Item | Recomputed |
|---|---|
| P99 CFADS, year 1 | 13.36 |
| P99 CFADS, year 15 | 16.35 |
| Factor, year 1 | 1.469 |
| Factor, year 15 | 1.506 |
| Year-15 revenue / CFADS | 1.50 |
| Year-15 CFADS fall | 33.6% |
| USD equivalent | 178.6 |

Ex 36.8 (c):

| Item | Recomputed |
|---|---|
| Undiscounted shortfalls | 245.84 |
| PV of shortfalls at 7.00% | 218.84 |
| PV as share of debt | 8.2% |
| 75% of the PV | 164.13 |
| USD equivalent | 144.9 |

Ex 36.11 Step 5: merchant PV of debt service 26.93 (33.7%); merchant share of CFADS 49.0%.

Ex 36.12: 491.7 × 1.23707/1.35 = 450.57.

Exhibit 36.12 matches JSON `sizing.candidates`:

| Item | Recomputed |
|---|---|
| DSCR debt | 629.950 |
| Downside debt | 630.138 |
| LLCR debt | 638.444 |
| LLCR slack | 8.49 |
| Gearing | 73.72% |
| Tranches, rounded | 189.0 + 138.6 + 63.0 + 239.4 = 630.0 |
| LLCR with DSRA | 1.4189 |
| LLCR without DSRA | 1.3598 |
| Failing margin without DSRA | 0.04 |

Exhibit 36.13 matches P-F09 / JSON `eca_tests`:

| Item | Recomputed |
|---|---|
| Repayment term | 13.1636 |
| WAL | 6.9158 |
| Largest installment | 1/26 = 3.85% |
| Repaid within 24 months | 3/26 = 11.5% |
| Other-tranche WAL | 8.169 |
| All-tranche WAL | 7.793 |
| ECA installment | 188.98/26 = 7.27 |

Exhibit 36.13 dates: tail from June 30, 2034 to April 30, 2046 (`ppa_expiry_base`) is 11.83 years. Average DSCR in sec:36.12: 1.5481, 1.3855 and 1.3525. Exhibit 36.14 debts and IRRs match the P-F36 grid.

## Defects

1. **Exhibit 36.14, column "Downside min DSCR (x)".** The column rounds twice. JSON `figures.P-F36.grid` has 1.274709 for the three 70% rows and 1.244818 for the two 1.40x/75% and 80% rows. The ledger prints these to three decimals as 1.275x and 1.245x, and the chapter rounded those again. Fix:
   - The rows 1.30x/70%, 1.35x/70% and 1.40x/70%: change 1.28 to 1.27.
   - The rows 1.40x/75% and 1.40x/80%: change 1.25 to 1.24.

   Suggest the ledger keeper print P-F36 downside minima to two decimals, or to four.

2. **Sweep period: sec:36.12 line 809 ("between 2027 and 2031") and Exhibit 36.13 memo line ("Forecast cash sweep of the commercial tranche, 2027--2031").** The sweep includes USD 4.571 million in 2032H1, the period that retires the commercial tranche (P-F09 row 2032H1; commercial opening 5.711). Without it the 2027H1–2031H2 sweeps sum to 94.92, not 99.49. Fix: "between 2027 and mid-2032", and in the memo line "2027--2032". The ledger row label "Cash sweep prepayment total (... ) | 2027-2031" carries the same error; flag it to the ledger keeper.

3. **Ex 36.11 Step 1 (line 538), "CFADS is EUR~14.27~million (9.78 contracted, 4.49 merchant)", and Step 2, "$9.78/1.30 + 4.49/2.00$".** Merchant year-1 CFADS is 4.4954, which rounds to 4.50; contracted is 9.7763. The 4.49 was forced to make the parts add to 14.27. Fix: print "(9.78 contracted, 4.50 merchant; the parts add to 14.28 because of rounding)". In Step 2 use $9.78/1.30 + 4.50/2.00 = 9.77$; the result is unchanged.

4. **Exhibit 36.13 memo lines and note, "Scheduled principal plus the forecast sweep equals the debt at close".** The printed lines are 530.5 + 99.5 = 630.0, against 629.9 printed as the debt. Fix: append to the note "the printed figures add to 630.0 because of rounding; unrounded, 530.46 + 99.49 = 629.95". This is consistent with the Exhibit 36.12 note.

5. **Sizing-sheet cell collision (ssec:36.3.1 line 215 against ssec:36.8.1 line 533).** The lesser-of block puts the four constraint debts in F27 to F30 (flags G27 to G30, MIN in F32). The bucket block then puts "contracted CFADS in row 30 and merchant CFADS in row 31, with their targets in F30 and F31". F30 cannot hold both the fourth constraint's debt and the contracted target, and row 30 would mix a constraint row with a CFADS row. Fix: move the bucket block to rows 40 to 43. That gives contracted CFADS in row 40 with its target in F40, merchant CFADS in row 41 with its target in F41, and bucket debt service in row 43 as `=J$8*(J40/$F$40+J41/$F$41)`, with row 43 replacing row 12. The WAL block (rows 35 to 38) does not collide with anything.

## Notes (not counted)
- Line 776, "four ten-thousandths to spare": the margin is 0.000359. That is acceptable as "about four"; "less than four ten-thousandths" would be exact.
- In the Sizing sheet, `I$8` in J14 and J18 must be blank or 0 if column J is the first repayment column; a text label in I8 would return #VALUE!. Saying "leave column I empty" would remove the risk.
