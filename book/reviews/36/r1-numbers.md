# Chapter 36 review, round 1: numbers

Reviewer role: numbers auditor (standards §12.4). Scripts: `/tmp/claude-0/-home-user-neurolab/a8d2e1e2-d243-5cdc-b359-eb0b0ebba7b3/scratchpad/review-36/` (lib.py, ex1_5.py, ex4.py, ex6.py, ex7.py, ex8.py, ex9.py, ex10.py, ex11.py, ex12.py, wt.py, drill.py, exr.py, ex14.py, ex16.py, ex18.py, ex19.py). I rebuilt every example independently from the inputs as printed. Case P figures were checked against `model/figure-ledger-case-p.md` and `model/outputs_case_p.json` (v1.4; `sizing`, `figures.P-F08`, `figures.P-F09`), and against `model/case_p.py` where the ledger is silent.

## Verdict: FAIL

The following reproduce exactly, to the printed precision:
- Examples 36.1, 36.2, 36.3 (schedule, totals and the rounding note), 36.4, 36.5, 36.6, 36.7, 36.8 (all three options and the failed three-year grace), 36.10 and 36.12.
- Exhibits 36.1 to 36.8 and 36.10.
- The judgment drill: 438.1, 473.1, 488.9, 443.6, 534.7 and 507.7; WALs of 11.9 and 12.9; interest cover of 1.91x; 72%.
- Solutions 36.1 to 36.12 and 36.14 to 36.19, including both Excel layouts.
- Exhibit 36.14 against P-F36, and the Case P tranche amounts, gearing (74.1%), LLCR (1.42x and 1.36x), average DSCR (1.54x), repayment term (13.16 years), tail (12.42 years) and ECA test values (WAL 7.177 recomputed from the P-F09 dates).

The defects below remain.

## Defects

1. **ssec:36.2.2, paragraph after Exhibit 36.2 (line 180), "30\% of the principal falls in the last two years".** Years 9 and 10 repay 14.37 + 16.00 = 30.37 of 120.54, which is 25.2%. Fix: "a quarter of the principal (25\%) falls in the last two years".

2. **Ex 36.9 Step 2 (line 473), "Total debt is USD~727.9~million, of which the balloon is 47.7\%".** The text compares the nominal year-10 balloon (347.2) with debt at close. The balloon's share of the 727.9 is its present value, 185.9, which is 25.5%. Fix: "Total debt is USD~727.9~million. The balloon of USD~347.2~million due at the end of year 10 equals 47.7\% of the debt at close; its present value, 185.9, is 25.5\% of it."

3. **Exhibit 36.9, column "Contracted only, 10 years" (lines 554 to 556) and its note.** DSCR is CFADS over debt service, and the project's whole CFADS (contracted plus the 30% merchant share) services this loan. At 53.0 the minimum DSCR is 1.82x in the base case, 1.67x with merchant prices down 20% and 1.59x with them down 30%, not 1.30x in every row. Even on contracted-bucket CFADS alone the figure is not invariant, because pro rata cost allocation moves cost onto the contracted bucket when merchant revenue falls: the year-1 contracted-bucket ratio is 1.27x at −20%. Fix: print 1.82 / 1.67 / 1.59. Change the note to: "The contracted-only loan is sized on contracted CFADS at 1.30x; its DSCR on total CFADS is higher, and merchant stress lowers it without taking it near 1.30x."

4. **ssec:36.8.1 (line 563), "so a 20\% fall still leaves 1.60\x{} on that cash, and the overall ratio stays at the contracted level".** Operating costs do not fall with price, so a 20% price cut lowers merchant CFADS by more than 20%. On the bucket profile the merchant-year DSCRs at −20% are 1.37x (year 11) falling to 1.30x (year 15). On merchant-bucket CFADS the year-1 ratio is 1.56x, not 1.60x. Fix: "so a 20\% fall in merchant prices, which cuts merchant CFADS by more because costs stay, still leaves the profile at 1.30\x{} or better in every year".

5. **Exhibit 36.11 panel C, Base LLCR "1.38", and Step 5 (line 699), "At 1.38\x{} including the DSRA".** (PV of P50 CFADS + DSRA 7.03) / 135.98 = 1.3746, which rounds to 1.37x. Fix both to 1.37x. The conclusion that it clears 1.35x still holds.

6. **Exhibit 36.11 panel A, row "LLCR at close incl. DSRA 1.35x / 138.45 / 2.47", and the exhibit note.** The 138.45 holds the DSRA at the 7.03 sized for 135.98. The DSRA is six months of debt service, so it scales with the debt. At 138.45 the LLCR is 1.351x, not 1.35x. With DSRA = CFADS₁ × D / PV, the LLCR is PV/D + CFADS₁/PV. Setting that equal to 1.35x gives D = PV / (1.35 − CFADS₁/PV) = 138.55 on the 569.9 GWh input, so the slack is 2.58. Fix: print 138.55 and 2.58, or keep 138.45 and change the note to "with the DSRA held at USD 7.03 million".

7. **Exhibit 36.11 source line vs table (inputs "P50 569.9 GWh").** On the printed 569.9 GWh, my results are:

   | Item | Recomputed | Printed |
   |---|---|---|
   | Base DSCR debt | 138.37 | 138.36 |
   | Downside DSCR debt | 136.16 | 136.15 |
   | One-year P99 debt | 138.02 | 138.01 |

   The writer's printout.py uses 152.0 × 8,760 × 0.428 = 569.89 GWh. On that input the P99 minimum DSCR is 1.0150 = 1.01x, not the printed 1.02x, so the table matches neither input. Fix: rerun on 569.9 GWh and print 138.37, 136.16 and 138.02. The slacks stay 2.39, 0.18 and 2.04, and the P99 minimum stays 1.02x (1.0150). All other cells are unchanged: WAL 10.66, largest installment 4.3%, base 1.32x, downside 1.15x/1.18x, PLCR 1.55x and DSRA 7.03.

8. **Case P downside slack: Exhibit 36.12 "Slack 0.1", sec:36.12 line 769 "slack by only USD~0.1~million (P-F08)", and the scene line "One hundred thousand dollars of room".** outputs_case_p.json `sizing.candidates` gives 633.4453 − 633.2560 = 0.189, so the slack is USD 0.2 million (about USD 190,000). The 0.1 comes from subtracting two ledger values that were each rounded to one decimal. Fix: Exhibit 36.12 "Slack 0.2"; line 769 "about USD~0.2~million"; dialogue "Not quite two hundred thousand dollars of room". Ask the ledger keeper to add a slack row to P-F08 so D-013 arithmetic is not done on rounded values.

9. **Case P gearing slack 9.6.** The figure appears in the scene ("By nine-point-six million"), Exhibit 36.12 ("Slack 9.6"), line 771 ("USD~9.6~million … $642.9 - 633.3$") and Solution 36.13(b). JSON gives 642.9083 − 633.2560 = 9.652, which rounds to 9.7. Fix: print 9.7 everywhere ("nine-point-seven" in dialogue), and show the arithmetic on the unrounded values (642.91 − 633.26). The same ledger request as defect 8 applies. The "within USD~10~million" in line 836 is still right.

10. **Exhibit 36.13 "Scheduled principal, 26 installments: 538.2", its note "(633.3 less 538.2)", and Solution 36.13 "add to USD~538.2~million".** The unrounded P-F09 installments in outputs_case_p.json (`figures.P-F09.principal_usd_m`) sum to 538.59. Only the rounded ledger values add to 538.2. The sweep prepayment is therefore 633.26 − 538.59 = 94.7, not 95.1. The ECA shares (4.6% largest installment and 9.0% within 24 months) are computed on 538.59. Fix:
    - Print "Scheduled principal, 26 installments: 538.6".
    - Add the note "installments shown add to 538.2 because of rounding".
    - Change the sweep wording to "prepays about USD 94.7 million (633.3 less 538.6)".
    - Correct Solution 36.13 to 538.6.
    - Correct the writer-notes flag to the ledger keeper, which reads "538.2 sum".

11. **WAL room "26 days" (scene, line 736; sec:36.12 line 811 "about 26 days"; sec:36.15 line 911 "26 days from failing").** P-F09 WAL is 7.17713 years, so the room is 7.25 − 7.17713 = 0.0729 years, or 26.6 days. The 26 comes from the rounded 0.07 × 365. Fix: "about 27 days" (dialogue "Twenty-seven days"), or "under four weeks".

12. **sec:36.9 Case P paragraph (line 603), "26 equal semiannual installments from COD over 13 years would have had a WAL of about 6.75 years, so a sculpted profile had only half a year of room".** The 6.75 assumes a first repayment six months after COD. Case P's 26 installments run from December 31, 2021 to June 30, 2034, starting eight months after the May 1, 2021 COD. Equal installments on those dates have a WAL of 6.92 years, which leaves 0.33 years of room, not 0.5. Fix: "26 equal installments on Case P's repayment dates (December 2021 to June 2034) would have had a WAL of about 6.92 years, so a sculpted profile had only about a third of a year of room."

13. **ssec:36.2.4 "Resculpting at COD" (line 200), "the lenders resculpted at COD to the same 1.35\x{} target on their updated forecast, keeping the final maturity".** P-F19 gives the COD re-sculpted constant DSCR as 1.28x before the LD prepayment (1.31x had capacity and heat rate held). `case_p.py resculpt_cod` keeps the debt amount and the 2034H1 maturity, and the DSCR is an output. This also matches the paragraph's own general description: "keeping the debt amount and the target" is not what Case P did. Fix: "In Case P's actual history the lenders resculpted at COD on their updated forecast, keeping the debt amount and the final maturity; the constant DSCR that resulted was 1.28\x{} (P-F19), and \cref{ch:61} follows what the LD prepayment then did to it."

14. **Ex 36.1 Step 3 (line 35), "A five-hundredths move in the target moves the debt by about CAD~15~million either way".** The moves are +15.3 (to 1.15x) and −14.1 (to 1.25x). The asymmetry is the point that ssec:36.3.3 teaches. Fix: "moves the debt up by CAD~15.3~million or down by CAD~14.1~million".

15. **Check lines that use rounded debt (Ex 36.5 line 296 and Solution 36.7).** The rounded debts do not reproduce the printed results:

    | Location | Printed check | Recomputed on rounded debt |
    |---|---|---|
    | Ex 36.5, line 296 | 120.54 × 1.30/1.20 = 130.58 | 130.585, which prints as 130.59 |
    | Solution 36.7 | 167.47 × 1.30/1.20 = 181.42 | 181.426, which prints as 181.43 |

    The printed results are correct only on the unrounded debts (120.537 and 167.465). Fix: write "$120.537 \times 1.30/1.20 = 130.58$" and "$167.465 \times 1.30/1.20 = 181.42$", or print the results as 130.59 and 181.43 with "to rounding".

## Notes (not counted as defects)
- The Excel formula in sec:36.3.1 for downside debt, `=SUMPRODUCT(J10:AN10,J$8:AN$8,1/J14:AN14)/F25`, implements eq:36.7 correctly. It returns #DIV/0! if any column in J:AN has a zero compound factor, for example a pre-repayment column. The equivalent `=F16*F11/F25` is exact under eq:36.3 and has no such risk.
- Ex 36.11's effective year-10 DSCR is 1.4448x, which rounds to 1.44x as printed (writer deviation 5 confirmed). Ex 36.8 four-year grace (writer deviation 1), Exercise 36.10 PLCR 1.5999x and trimmed debt 389.08 (writer deviation 4), and Ex 36.4 cost downside 785.0 (writer deviation 3) are all confirmed.
