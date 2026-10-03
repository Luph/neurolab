# Chapter 36, round 1, line review

Reviewer role: line (standards §8, prose test §12.7; style sheet §1, §11 and Addendum).
File: chapters/36-sizing-and-sculpting-debt.tex (1,188 lines; about 22,700 source words against a 16,000 target).
Mechanical checks: `scripts/scan_prose.py` reports 0 hits. There are no `---` dashes. A manual grep found British spellings (defect 19).

## Verdict: FAIL

The prose is mostly clean, specific and well paced, so this chapter can serve as an exemplar once the defects below are fixed. Two problems stop it from passing now. First, production apparatus has leaked into the reader's text: ledger IDs, decision IDs, Case Bible and Annex references, fact-sheet slugs, and one sentence about an "early draft of the Case Bible" (defect 26). Second, about 30 sentence-level and structural tics remain, together with repetition worth roughly 1,200 to 1,500 words.

## Length judgment (exhaustive, never padded)

Most of the overrun is substance the brief requires. The chapter has twelve worked examples, a walkthrough, a Case P installment with three exhibits, and nineteen exercises with full solutions. Exercises and solutions alone run to about 4,850 source words. Do not cut substance to reach 16,000. The padding that should go is named in defects 1, 2, 5, 8, 10, 17, 18, 22, 27, 28, 29 and 31. Together these come to roughly 1,200 to 1,500 words. The biggest single block is the duplication between the ssec:36.10.1 prose and Exhibit 36.10 (defect 22). The others are the recap in the close (defect 28), the repeated Port Arthur, Gulf and LNG facts (defects 17 and 22), and the Tier 1 solutions that restate body paragraphs nearly word for word (defect 31). After these cuts, expect about 21,000 source words, which is defensible for this brief.

## Defects

1. **Opening, lines 5 and 7 (meta-announcement and a stock opener).** "The second is the subject of this whole chapter." and "That banker's tools are the ones this chapter builds. They start with ... They end with judgment that no formula supplies: ..." announce the chapter's contents, which style sheet §4.1 forbids. Line 19 repeats the same "one move" idea. "Somewhere in a lead arranger's office a structuring banker ..." is the banned "Somewhere, right now..." opener. Fix: cut "The second is the subject of this whole chapter." Start that sentence with "At the lead arranger, a structuring banker took ...". Delete paragraph 7 entirely; line 19 already carries the CFADS/target idea. If one bridge is wanted, keep only the clause naming the judgments (which case, how long, how much refinancing risk, which constraint binds) and attach it to the end of paragraph 5.

2. **sec:36.2, line 104 (announcing and a reflexive triplet).** "Here is its mathematics, its implementation, and the ways it fails." Fix: delete the sentence. Keep the cross-reference sentence before it.

3. **ssec:36.1.2, line 100 (negation opener and awkward phrasing).** "The unused capacity is not an abstraction." and "The lenders gain nothing in return that they asked for". Fix: begin the paragraph "On a USD 111 million loan, 21% of the debt is ...". Rewrite the second phrase as "The lenders get nothing in return:".

4. **ssec:36.2.4, line 196 (false contrast).** "Lenders treat negative principal as a sizing error, not a feature, and fix it ..." Fix: cut ", not a feature".

5. **ssec:36.2.4, line 202 (summary sandwich inside one paragraph).** "Sculpting removes slack from every period equally." makes the same point as "a sculpted profile has exactly the target cushion in every year". The closing clause "sculpting converts any optimism in the forecast directly into thinner coverage across the whole life of the loan" restates "every period falls below target together". Fix: delete the first sentence. End the paragraph at "... for the reserves of \cref{ch:37}."

6. **ssec:36.3.1, line 259 (filler and false contrast).** "The cost downside is instructive in its own right." and "A downside that never binds is not useless; it is evidence that ...". Fix: start with "The cost downside allows more debt than the base test (785.0 against 782.2), because ...". Replace the second sentence with "A downside that never binds shows that the base-case target already absorbs that risk."

7. **ssec:36.3.2, line 267 (colon reveal).** "for a reason that has nothing to do with cash flow: equity at risk." Fix: "Lenders keep a gearing cap even where it rarely binds because it fixes the sponsor's equity at risk."

8. **ssec:36.3.2, line 269 (zinger ending), and lines 269 and 648 (a repeated superlative).** "Each tranche was sized on the risk of the cash that repaid it." restates the sentence before it. Fix: delete it. Also replace "The clearest real illustration of two binding logics" (line 269) and "is the clearest recent example" (line 648) with plain statements, for example "Dogger Bank in the UK North Sea shows both binding logics in one financing." and "Ørsted's Ocean Wind 1 off New Jersey shows the mechanism."

9. **sec:36.4, line 318 (cliché and meta).** "Resource projects live or die on that kind of test, so it deserves its own treatment." Fix: "For wind, solar and hydro projects the P-value tests usually set the debt."

10. **ssec:36.4.1, line 326 (a hollow paragraph that repeats itself).** "The combination matters more than any single level ... whichever is most demanding ... will bind." This repeats line 324 ("Practice therefore pairs a long-run test with a short-run floor") and anticipates line 360. Fix: delete the paragraph.

11. **Self-answered questions used as transitions, lines 120, 341 and 520.** "Why does discounting ...? Because ...", "Why does a 22.3% fall ... need ...? Operating leverage (\cref{eq:14.2})." and "Why do LNG lenders accept this? Because ...". Fix: keep line 120, where the answer is not obvious. Rewrite line 341 as "Operating leverage (\cref{eq:14.2}) explains why a 22.3% fall in output needs an effective P50 cover of 1.51x to keep a 1.00x floor." Rewrite line 520 as a statement: "LNG lenders accept the structure because ...". Also cut its three-part "because ..., the bank market ..., and the sponsors ..." chain to the two reasons that carry weight: refinanceability once operating, and construction risk priced in the bank market.

12. **ssec:36.5.1, line 397 (filler opener).** "The LLCR row shows a property worth remembering." Fix: delete. Start the paragraph "Under pure sculpting, with no reserve in the numerator, ...".

13. **ssec:36.6.1, line 417 (reflexive triplets and a duplicated item).** "for three reasons: to ..., to ..., and to ..." is followed by "the debt is not falling while the asset ages, the weighted average life lengthens, and the lenders' exposure stays at its peak for longer". The first and third items say the same thing. Fix: cut "and the lenders' exposure stays at its peak for longer". Replace "Sponsors ask for post-COD grace for three reasons:" with "Sponsors ask for post-COD grace to ...".

14. **ssec:36.6.2, lines 458 and 460 (colon reveal and narrated morals).** "The transferable lesson: when debt is sized ..." and "Accreting debt is how a ramp-up shortfall gets financed ..., and the accretion compounds the original error." Fix: at line 458 drop "The transferable lesson:" and state the mechanism directly ("Debt sized to a single ramp-up forecast with thin cover and no funded reserve has nothing to absorb the first years of shortfall."). At line 460 delete the last sentence. The USD 310 million to USD 1.114 billion figures already make the point.

15. **ssec:36.7.1, line 480 (stock opener).** "The refinancing test is only as good as its assumptions." Fix: delete. Start with "At 7.00% and 1.40x, years 11 to 15 support ...".

16. **ssec:36.7.2, line 518 ("that's the point" formula).** "The sponsors' loss of distributions is the point." Fix: "Losing distributions is what drives the sponsor to refinance." Then continue with the next sentence.

17. **ssec:36.7.2, line 520 (repeats the opening).** The first sentence restates line 3 almost word for word: seven-year maturity, 20-year sculpted profile, most principal refinanced. Fix: "Port Arthur LNG, the opening case, is a hard mini-perm by maturity (Sempra 2023)." Keep the Rio Grande sentence.

18. **ssec:36.7.2, line 522 (wrong-direction phrase and a zinger).** "The extreme case runs the other way." is inaccurate, because Indiana Toll Road goes further in the same direction (more refinancing risk). "A bullet converts a long-lived asset's debt entirely into refinancing risk" restates "the whole debt was a refinancing bet on a 75-year asset". Fix: open with "The extreme case is a loan with no amortization at all." Delete the restating clause and keep only "\cref{ch:37} returns to the swap."

19. **American spelling (style sheet §2.1).** "cancelled" (line 458) should be "canceled". "panellist" (line 563 and twice in line 646) should be "panelist".

20. **ssec:36.8.2, line 567 ("depends" without direction).** "Which they choose depends on the share of debt the tail carries and the depth of the market for the asset's output." Fix: "The larger the share of debt service the tail carries and the thinner the market for the output, the further lenders move from merchant-ratio tail debt toward no tail debt or a sweep."

21. **ssec:36.9.2, line 601 (capitalization).** "...; \Cref{ch:38} gives the tools ..." appears in mid-sentence. Fix: use `\cref{ch:38}`.

22. **ssec:36.10.1, lines 611 to 617 against Exhibit 36.10 (largest repetition in the chapter).** The four driver paragraphs restate almost every number in Exhibit 36.10: NRF DSCR bands, Gulf maturities, Skouries and QB2, IFC 62% to 80%, PFC 20-year loans, Ferrovial 2047 to 2058, and LNG 52% and two-thirds. The table then repeats them. The Gulf clause in line 611 also repeats line 405. The LNG sentence in line 617 ("Large US LNG projects use seven-year bank mini-perms, with sponsors accepting the refinancing risk in exchange for bank pricing") repeats lines 3 and 520. "Those are single deals, not a regional norm." (line 615) repeats the exhibit note at line 641. Fix: in prose, give each driver its direction, its mechanism and one anchoring number. Leave the evidence list to the exhibit. Replace the Gulf clause with `\cref{ssec:36.5.2}`. Cut the LNG mini-perm clause and keep only the gearing contrast (52% and two-thirds against 80%-plus). Cut the line-615 caveat. This saves about 200 to 250 words.

23. **ssec:36.10.2, line 648 (colon reveal).** "The mechanism for a sizing banker: a fixed-price contract ..." Fix: "A fixed-price contract signed years before financing transfers ..."

24. **sec:36.11, line 695 (dangling modifier).** "As a CCSU transaction longer than 15 years, the WAL limit is 70% of 18 years" makes the limit the transaction. Fix: "Because the loan is a CCSU transaction longer than 15 years, its WAL limit is 70% of 18 years, 12.6 years; ..."

25. **sec:36.12 scene, lines 709 to 739.**
    (a) Line 730, "Pieter didn't look up.", copies the style sheet's own sample line ("The arranger didn't look up ...") and is a stock body-language beat that changes nothing. Cut it.
    (b) Line 718, "One-twenty on the downside lets you six-three-three-point-four.", is missing its verb. Write "lets you borrow six-three-three-point-four".
    (c) Line 738, "Fine. And the day it goes wrong?", has no clear speaker. Alternation makes it Pieter's, but "Fine" answers nothing, so Tomasz's kilowatt-month question hangs and the reader cannot tell who is speaking. Give Pieter a real response to the COD question (a deflection or a bad concession) and attribute the last line.
    (d) Line 710 ("had the printout upside down before Pieter finished sliding it across") and line 718 ("Pieter tapped the downside row") are stage business with no effect on the outcome (style sheet §1.3). Keep at most one.

26. **Production apparatus in reader-facing text (§8: meta-commentary and signs of a draft).** The reader has no ledger, decision log, Case Bible, annex or fact-sheet register. Fixes:
    - Line 811: "An early draft of the Case Bible said the first repayment had to fall within six months of COD." Delete the sentence. If the six-month point teaches something, recast it as: "Outside the project finance terms the Arrangement's standard rule is a first repayment within six months; the FC base profile, first repaying eight months after COD, would have failed it."
    - Ledger and decision IDs: line 769 "(P-F08)", line 771 "(D-013 arithmetic on P-F08: ...)", line 773 "(P-F08)", line 811 "(P-F09)" and "(Annex P~3.6; ...)", line 813 "(D-013 arithmetic on the input dates)" and "(P-F08)", line 1096 "(P-F08)", "(D-013 arithmetic on ledger values)", "(P-F43)", "(P-F07)", "(P-F09)". Move every ID into LaTeX `%` comments. Exhibit sources at lines 765, 807 and 833 should read "Case P reference model, FC base" without IDs, or the IDs go in comments.
    - "(Case Bible inputs)" at lines 569 and 813, and "from the Case Bible" at line 807: write "Case P inputs" or "the case inputs".
    - Exercise 36.13, line 972: "Using P-F07, P-F08 and P-F09 and the Case Bible inputs" should read "Using \cref{exh:36.12,exh:36.13} and the Case P inputs".
    - Fact-sheet slugs: line 640 "t-market-norms and t-market-norms-2 fact sheets:" and line 1135 "(t-market-norms; t-market-norms-2)". Delete them and cite the underlying sources only.
    - Solution 36.18, line 1129: "No fact sheet records the worst observed UK wind year" should read "Without a published worst-year record for UK onshore wind". Also: "No other agency threshold is quoted, because none is verified." should read "Other agencies publish no comparable threshold table" (or delete).

27. **Practitioner's notebook, lines 845 to 860 (duplicate items).** Checklist item 8 (line 849, converged IDC, fees and DSRA) repeats item 4 (line 845, converged financing costs in the gearing denominator). Checklist item 6 (line 847) and red flag 6 (line 860) both say to rerun WAL after late CFADS changes. Red flag 1 (line 855) recycles the line-202 wording. Fix: merge 849 into 845. Keep only one of 847 and 860. Reword 855 so it names the evidence to look for, for example "no downside run at all in the credit paper".

28. **Close, sec:36.15, lines 911 and 913 (summary sandwich and a question stack).** "Everything in this chapter reduces to one move ..." repeats line 19 ("Every sizing method in this chapter is a variation on one move"). The following list ("Sculpting uses the whole cash flow; the lesser-of rule makes every test count; P-value tests, tenor, tail, grace, balloons, mini-perms, buckets and average-life limits each ...") is a recap of the table of contents. Line 913 stacks a triplet ("Wind will be weak, the offtaker will pay late, a turbine will trip before the peak season") on a three-question run ("What pays ..., who decides ..., and what forces ...?"), then a three-part answer. Fix:
    - Delete the second and third sentences of line 911. Keep "Sizing turns a forecast into a number." and the Case P sentence.
    - In line 913, keep one failure example and one question ("What pays debt service in the half-year when CFADS falls below it?"). Let the `\cref{ch:37}` sentence name the reserve, the lock-up and sweeps, and the covenants.

29. **sec:36.12, line 813 against the Exhibit 36.13 note (line 808) (repetition).** Both explain that the commercial tranche's sweep shrinks later scheduled installments, and Solution 36.13 says it a third time. Fix: in line 813 keep only the step-up and sweep terms and the 1.54x average DSCR point. Cite the exhibit note for the 538.2 against 633.3 gap.

30. **ssec:36.2.3 and ssec:36.2.4, lines 186 to 202 (monotone run-in labels).** Eight consecutive paragraphs open with a label sentence ("Which case.", "Which CFADS.", "Which rate.", "Seasonal sculpting.", "Negative principal.", "Circularity.", "Resculpting at COD.", "Sculpting to a forecast that proves high.") and follow the same shape. This is a bullet list in prose form. Line 188 also uses signposted enumeration ("Two errors are common. One is ... The other is ..."). Fix: keep the labels in ssec:36.2.3, where they mirror the three questions in line 184. In ssec:36.2.4, turn the labels into topic sentences, for example "Pure sculpting can produce negative principal." and "Many term sheets let the lenders resculpt at COD ...".

31. **Tier 1 solutions 36.3, 36.4 and 36.5 (lines 1012 to 1020) restate body paragraphs.** These solutions repeat lines 486, 403 (including the same 40-year gas plant) and 563 nearly word for word. Fix: give the answer, then one reasoning line with a `\cref` to the teaching paragraph, then the numeric check already present. This saves about 200 words without losing substance.
