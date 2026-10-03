# Chapter 36 review, round 1: novice

Reviewer role: novice. The reader knows only Chapters 1 to 35, as described by briefs u01 to u08 and the homes in the glossary canon. I read the chapter straight through and checked the arithmetic in examples wherever a step looked like a jump (scripts in the session scratchpad `review-36/nov.py`, `n2.py`).

## Verdict: FAIL

Most of the chapter can be followed without outside help. It fails the novice test (§12.2) in five places where a careful reader who does the arithmetic gets a different answer from the text, or meets an apparent contradiction the text does not resolve. These are defects 6, 12, 18, 24 and 25. The other defects are steps that are skipped or terms used before they are defined.

## Defects

1. **ssec:36.2.1, line 118 (principal and balance notation).** $D_0$ is defined as "the debt at the start of the first repayment period", and then $P_t = \mathrm{DS}_t - i_t D_t$ with "$D_{t+1} = D_t - P_t$". On this indexing, $D_1$ is the opening balance of period 1, and that is $D_0$. Readers cannot tell whether $D_t$ is an opening or a closing balance. **Fix:** write $P_t = \mathrm{DS}_t - i_t D_{t-1}$ and $D_t = D_{t-1} - P_t$, with $D_{t-1}$ named as the opening balance of period $t$. Then $D_0$ is used consistently with \cref{eq:36.1} and \cref{eq:36.3}.

2. **ssec:36.1.1, line 23 (term).** "fixed unitary payment" is used here, but Chapter 21 taught the canon term **unitary charge** (ssec:21.6.1, ruling R-051). A novice will wonder whether this is a different payment. **Fix:** replace "unitary payment" with "unitary charge".

3. **Ex 36.1, line 26.** "design-build-finance-maintain" is used with no gloss. Its home is ssec:58.1.1, which comes later in the book. **Fix:** add a short gloss, e.g. "(a PPP in which the private party designs, builds, finances and maintains the building; \cref{ssec:58.1.1})".

4. **Equations 36.7, 36.6 and 36.5 (lines 217, 529, 578).** The equations appear in the order 36.4, 36.7, 36.6, 36.5. A reader who meets Equation 36.7 straight after 36.4 thinks two equations have been missed. **Fix:** renumber in order of appearance and update the registry: lesser-of 36.4, effective target 36.5, bucket 36.6, WAL constraint 36.7. The writer's notes already offer this. If the registry numbers must stay, add one sentence at the first out-of-order equation explaining the numbering.

5. **ssec:36.3.1, line 214.** $F$ is "the total funding requirement (\cref{ssec:40.2.3})". That home is five chapters ahead, and nothing here defines the term. **Fix:** define it inline at first use, e.g. "all uses of funds to COD, including IDC, fees and the initial reserve funding, that debt and equity together must pay", and mark the cref as a forward reference.

6. **ssec:36.2.2, line 180.** "30% of the principal falls in the last two years." From Exhibit 36.2, $(14.37 + 16.00)/120.54 = 25.2\%$. A reader who checks gets a different number from the text. **Fix:** "a quarter of the principal (25%) falls in the last two years". Alternatively, "37% in the last three".

7. **Ex 36.4, Step 3 (line 229).** "So $k = 1.463$, and the debt is BRL 695.0 million" skips the step that turns $k$ into money. **Fix:** add "$= 782.2 \times 1.30/1.463$, because debt shaped on base CFADS is inversely proportional to $k$ (\cref{eq:36.7})". Also replace "the fixed operating costs". The costs escalate at 4.5%; "fixed" here means they do not vary with output, so write "operating costs, which do not fall with output,".

8. **ssec:36.3.2, line 265.** "a high Brazilian real interest rate" can be read as a real (inflation-adjusted) rate. The 8.75% in the example is nominal BRL. **Fix:** "a high BRL interest rate".

9. **Ex 36.6, Step 3 (line 337).** Step 3 points straight to Exhibit 36.5. The reader never sees CFADS in any P-case or how any $k$ is computed, so the exhibit's 1.413, 1.472 and 1.506 cannot be reproduced. **Fix:** show one test in full, e.g. P99 CFADS in year 1 ($28.05 \times 0.7767 - 8.42 = 13.37$) and year 15 (16.37), $k = \max_t(1.00 \times \mathrm{CFADS}^{50}_t/\mathrm{CFADS}^{99}_t) = 1.506$ (year 15), and debt $= 155.3 \times 1.35/1.506 = 139.3$.

10. **Ex 36.6, closing paragraph (line 341).** The paragraph explains the 1.51x with year-1 operating leverage (1.43, "roughly a 32% fall"). That gives $1/(1-0.319) = 1.47$, not 1.51. The binding year is year 15. There, revenue/CFADS is 1.50 because costs escalate faster than the tariff, CFADS falls 33.5%, and $k = 1.506$. A reader who follows the year-1 numbers gets 1.47 and cannot reach the exhibit. **Fix:** rewrite the paragraph on year 15. State that the multiplier grows over the life because opex escalates at 2.8% against 2.0% indexation, and that this is why the last year binds.

11. **ssec:36.5.1, line 397.** "an LLCR test set at or below the sculpting target cannot bind on the sizing case; it bites only if the target is lower". The second "target" is ambiguous. **Fix:** "it bites only if the sculpting target is set below the LLCR test level, or if the profile is not sculpted".

12. **Ex 36.8, option (c) (line 432).** Two steps are missing, and one hidden assumption is left unstated:
   (i) No reason is given for the debt of 2,666.6. **Fix:** state that interest-only years keep the balance constant, so the debt equals the present value at the end of year 4 of years 5 to 18 debt service, and that this is the same number as option (a)'s year-4 peak.
   (ii) The reserve of 208.4 is "the present value of those shortfalls", but no discount rate is given. The figure uses the 10.15% loan rate, which assumes the reserve cash earns 10.15%. A novice will ask why the reserve is not the nominal sum, $118.9 + 78.6 + 40.9 + 7.4 = 245.8$. **Fix:** state the rate and the assumption. Then either fund it at the nominal sum (or at a stated deposit rate) or justify the loan rate.
   (iii) Year-1 shortfall: $270.66 - 151.71 = 118.95$, printed as 118.9. Add a rounding note or print 119.0.

13. **Ex 36.8, option (b) (line 430).** "spread over the full 18 years it carries a DSCR of 2.39x from year 2 onward" does not say what profile is meant. **Fix:** "sculpted over years 2 to 18 instead, the constant DSCR would be 2.39x".

14. **ssec:36.6.2, SH 130 paragraph (line 458).** "Chapter 11" is used with no gloss; the reader has not met US bankruptcy law. TIFIA is used without its expansion or a back-reference to sec:29.5, where it was taught. **Fix:** "a federal TIFIA loan (\cref{sec:29.5})" and "filed for Chapter 11, the US court-supervised reorganization procedure, ...". Line 522 uses "prepackaged Chapter 11", whose home is ssec:64.8.2. Add a forward reference or a gloss ("a filing with the restructuring plan agreed before filing").

15. **ssec:36.7.2, Indiana Toll Road (line 522).** The initial debt is "approximately USD 3.4 billion", but "about USD 3.9 billion of the debt fell due". The reader cannot see how the debt grew. **Fix:** add the reason the facts sheet supports (for example, the additional facilities or the swap termination exposure). If no reason is supported, state both figures without implying they are the same facility.

16. **Ex 36.11, Step 1 (line 537).** The bucket split prints as 9.78 + 4.50 = 14.28, against CFADS of 14.27. The unrounded merchant figure is 4.495. **Fix:** print 4.49, or add the book's rounding note.

17. **ssec:36.8.1, line 563 (merchant share).** "the merchant share of debt service, in present-value terms, is 33.7%" is not computed anywhere in Ex 36.11 (it checks at 33.70%). **Fix:** add a Step 5 to the example: PV of merchant debt service divided by PV of total debt service, with both figures shown.

18. **ssec:36.8.1, line 563 (wrong reasoning).** "a 20% fall still leaves 1.60x on that cash, and the overall ratio stays at the contracted level." This is wrong. Opex is allocated to the buckets, so a 20% merchant price cut reduces merchant CFADS by more than 20% (operating leverage, taught one section earlier in Ex 36.6). Recomputed, the 1.30x minimum in Exhibit 36.9 occurs in **year 15, a merchant-only year**, where merchant cover is $2.00 \times 5.71/8.78 = 1.30$. It is not "the contracted level". A reader who has just learned operating leverage will see the contradiction. **Fix:** rewrite as follows: "a 20% price fall cuts year-15 merchant CFADS by about 35% because costs do not fall, so 2.00x cover falls to 1.30x, still above 1.00x; the uniform profile falls to 0.85x". Also make clear that the 1.30x coincides with the contracted target only by chance.

19. **Ex 36.12, Step 4 (line 598).** "Solve for the debt at which the blended profile's minimum DSCR is 1.35x" gives no method. Earlier the chapter says closed form beats goal seek, so a reader will not know whether to goal-seek. The answer is closed form: scale the blended schedule, and its minimum DSCR scales inversely with the debt. **Fix:** "Because every installment and every interest payment scales with the debt, the minimum DSCR is inversely proportional to it: $491.7 \times 1.237/1.35 = 450.6$". Also print the unrounded 1.237, since $491.7 \times 1.24/1.35 = 451.6$ does not reproduce the answer.

20. **sec:36.11, Exhibit 36.11 and Step 5 (lines 667, 682, 699).** Step 5 says the LLCR without the DSRA is 1.32x (the effective sculpting ratio, 1.3228) and with it 1.38x. However, the exhibit note gives the DSRA as USD 7.03 million, and $1.3228 + 7.03/135.98 = 1.3745$, which rounds to **1.37x**. Panel A's LLCR debt of 138.45 does not reproduce either: solving $(179.87 + 0.0517D)/D = 1.35$ gives 138.5. **Fix:** recompute the LLCR (and its panel-A debt) or the DSRA amount so that the printout reconciles. If the LLCR is measured at a date other than the start of repayment, say so in the note.

21. **ssec:36.12, Exhibit 36.12 (lines 759 to 760).** "ABDB A-loan" and "ABDB B-loan": the acronym is not expanded in this chapter. Chapter 29 teaches "B loan" (canon spelling, no hyphen). **Fix:** expand ABDB at first use in the chapter. Write "A loan" and "B loan" as in the canon, and add \cref{ssec:29.4.4}.

22. **ssec:36.12, line 773.** "The common terms agreement defines LLCR ..." The common terms agreement's home is ssec:51.1.3, which is ahead. **Fix:** gloss it ("the agreement holding the terms common to all tranches") with a forward reference.

23. **ssec:36.12, line 773 against ssec:36.5.1 line 397.** The chapter taught that, under pure sculpting with no reserve, LLCR at the start of repayment equals the target DSCR. Case P is sculpted at 1.35x, yet its LLCR without the DSRA is 1.36x. The difference is not explained. **Fix:** add one sentence explaining the 0.01x, using whatever the model shows (e.g. the LLCR discount rate differs from the period interest rates, or the sweep and fees).

24. **ssec:36.12, Case P profile (line 741 against Exhibit 36.13 note and line 813).** Line 741 says "Case P's tranches all amortize pro rata on one common profile". The Exhibit 36.13 note says the commercial tranche's sweep prepays about USD 95 million and "reduces that tranche's later scheduled installments", which means the profiles are no longer common after 2027. Separately, the chapter has taught three things: sculpting gives the target DSCR in every period, the principal column sums to the debt, and the closing balance check must be zero. Case P breaks all three: the minimum is 1.35x but the average is 1.54x, and principal sums to 538.2 against debt of 633.3. Line 813 also explains the post-2029 fall in principal with "capacity payments are partly indexed while the debt declines", which accounts for a rise, not a fall. **Fix:** add a short paragraph after Exhibit 36.13 that does four things:
   - (a) states that the common profile applies to scheduled installments at close, and that the sweep then reduces the commercial tranche's later installments;
   - (b) names the periods in which the 1.35x is reached;
   - (c) explains that the later DSCRs are above 1.35x because forecast sweep prepayments shrink later scheduled debt service;
   - (d) gives the actual reason principal falls after 2029.

   Amend line 741 to match.

25. **ssec:36.12, Exhibit 36.14 and line 836 (P-F36).** Exhibit 36.12 lists the 1.20x downside DSCR as a sizing constraint (allowing 633.4). Yet Exhibit 36.14's 1.30x rows show debt of 642.9 and 658.1 with downside minimum DSCRs of 1.18x and 1.19x. Both are below 1.20x, so on the chapter's own lesser-of rule the downside test should have capped the debt. The ledger confirms that P-F36 varies only the base target and the gearing cap. Line 836 then calls 1.20x "the lock-up level", which is a different concept: lock-up's home is ssec:37.4.1, and the reader has not met it as a number for Case P. **Fix:**
   - Add an exhibit note: "Each row applies only the base DSCR and gearing constraints; the 1.20x downside test is reported, not imposed".
   - In line 836, say the 1.30x/75% row "would fail the 1.20x downside test that the lenders also impose", rather than calling 1.20x a lock-up level. If the lock-up is also 1.20x, say so explicitly, with a forward reference.

26. **Case P scene, lines 736 to 738.** Tomasz asks "What does it cost us per kilowatt-month if the independent engineer moves COD back six months?" The next line, "Fine. And the day it goes wrong?", is unattributed and answers nothing. The reader cannot tell who speaks or what "Fine" accepts. Line 741's comment that it "was not a tariff question" makes it more confusing, because kilowatt-month is a tariff unit. **Fix:** give Pieter an actual reply (e.g. that the cost depends on whether the lenders resculpt, or that he will run it). Attribute each line, and make the narration say plainly why a COD delay is a profile question and not a tariff one.

27. **Judgment drill, sec:36.14 (lines 896 and 900).** "interest cover of 1.91x in the grace year" uses a ratio the book has not defined. Neither "interest cover" nor ICR appears in the canon. **Fix:** "CFADS is 1.91 times the interest due in the grace year". Line 900 also refers to "The six-month DSRA", but the situation never says the deal has one. **Fix:** add "a six-month DSRA" to the situation paragraph.

28. **Close, sec:36.15, line 913.** "A profile sculpted at 1.35x has 35% of cushion in every period" invites the misreading that CFADS can fall 35%. In fact it can fall only 26% ($1 - 1/1.35$) before cover reaches 1.00x. **Fix:** "has CFADS 35% above debt service in every period, so CFADS can fall about 26% before it no longer covers debt service".

29. **Minor terms used before their home, no gloss or forward reference:**
   - "cash sweeps" (line 188, before the gloss at line 486);
   - "lock-up level" (line 324; home ssec:37.4.1);
   - "zero-coupon" and "MBIA-insured" (line 460; add "monoline-insured (\cref{ssec:3.6.1})" and "bonds that pay no interest until maturity, accreting instead");
   - "offshore renewable energy certificate" (line 648; home ssec:71.3.2);
   - "hydrology reserve" (Solution 36.19).

   **Fix:** give each a one-clause gloss or a \cref at first use.
