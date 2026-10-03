# Chapter 2 review, round 1: novice reader

Reviewer role: novice (standards §12.2). I know only what Chapter 1 teaches, as set out in its brief (bible/briefs/u01.md, Sections 1.A and 1.3 to 1.12; Chapter 1 has not been drafted yet, so I used the brief's list of concepts introduced intuitively). I checked first uses against bible/glossary-canon.md home labels. Line numbers refer to chapters/02-what-project-finance-is.tex as reviewed.

## Verdict: FAIL

The chapter's argument is clear and its worked examples are easy to follow. However, a large set of finance, accounting, legal, and energy terms appears before the book has taught them and without any gloss. Chapter 1 does not introduce them and this chapter does not define them, so a reader starting from zero stalls at the opening, at Sabine Pass, at the clause, and in the Case P scene. A careful editor would not pass the chapter in this state. Each fix below is a clause or a sentence, not a rewrite.

## Defects

1. **Opening, lines 3 to 7; ssec:2.1.3, line 91.** "Chapter 11", "list of debtors", "bankruptcy estate", "going-concern explanatory note", and "creditors' committee" are all used without explanation. The hook turns on these terms, and the reader does not know what any of them mean. Fix:
   - Line 3: gloss Chapter 11 in one clause ("the US bankruptcy procedure under which a company keeps operating while it restructures its debts under court supervision").
   - Line 7: gloss the going-concern note ("a warning from the auditors that the company might not be able to keep operating for the next year"), with a reference to ssec:7.11.1.
   - Line 7: gloss "bankruptcy estate" ("the pool of assets and claims a bankrupt company's creditors share").

2. **"Consolidate" is used in two senses, and neither is defined.** The accounting sense appears at lines 3 and 5 ("consolidated balance sheet"), at line 291 ("consolidated accounts", "deconsolidation"), at line 240 (Hyperion), in Exhibit 2.3 ("Group accounts: Consolidated"), and in Solution 2.13. The bankruptcy sense appears at line 7 ("a bankruptcy court might consolidate it with SunEdison"), at line 81, and at line 91 ("substantive consolidation"). A novice will read them as the same idea. Fix:
   - Line 3: define accounting consolidation ("a parent's accounts that add together its own figures and those of every company it controls"), with a reference to ch:66.
   - Line 7: name and define the court remedy ("substantive consolidation: a court treating a parent and a subsidiary as one debtor, so the creditors of each can reach the assets of both").
   - Line 91: add a short reminder that this is the line 7 sense, not the accounting one.

3. **"Balance sheet" is used about 20 times, starting at line 3, and never defined.** Its home is ssec:7.4.1, and Chapter 1's brief does not introduce it. The chapter's central metaphor ("contracts in place of a balance sheet", ssec:2.3.1) depends on it. Fix: at the first use (line 3 or line 22), add one plain sentence ("a statement of what a company owns, what it owes, and the difference, its owners' equity"), with `\cref{ssec:7.4.1}`.

4. **Bonds and notes are undefined: line 7 ("bond indentures"), line 87 ("senior notes"), line 210, ssec:2.6.1, and Exercise 2.12.** Standards §1 says the reader does not yet know what a bond is, and its home is ssec:6.7.1. Fix: at line 87, gloss notes as bonds ("tradable loans sold to investors, paying a fixed rate of interest and repaying their face value at maturity"), with `\cref{ssec:6.7.1}`. Gloss "indenture" as the bond's governing contract. Gloss "senior" as "paid ahead of other debts".

5. **Credit ratings are used from line 107 onward but first explained at line 303, and the scale is never connected.** The terms involved are "rating agencies" (line 107), "investment-grade" (line 198, before the Baa3 gloss at line 303), and "triple-B-minus" and "one notch from junk" (Case P scene, lines 470 to 472). The brief's assumed list requires ratings "at intuitive level (forward to Ch 30)", and the chapter never gives that level. Fix: at the first use (line 107), add two or three sentences covering:
   - an agency's letter-grade opinion of credit;
   - S&P/Fitch BBB- and Moody's Baa3 as the lowest investment grade;
   - "junk" (sub-investment grade) as anything below that;
   - why a downgrade raises a company's borrowing cost;
   - `\cref{ssec:30.5.1}`.

   Then line 303 can refer back to it.

6. **LNG is never spelled out, and the Sabine Pass vocabulary is left unexplained.** LNG first appears at line 26, then at lines 166 and 196. Also unexplained are "liquefaction trains" (lines 26 and 196), "MMBtu" (line 198), "Henry Hub" (line 198, only half-explained), and "lump-sum turnkey" (line 200). Fix:
   - Expand "liquefied natural gas (LNG)" at line 26.
   - At line 196, add a clause saying a train is one processing line that cools gas to about −160°C so it can be shipped.
   - Gloss MMBtu as the standard unit of gas energy (million British thermal units).
   - Gloss Henry Hub as the US benchmark gas price, set at a Louisiana trading point.
   - Gloss "lump-sum turnkey" as "a single fixed price for a plant handed over ready to run", matching the EPC definition at line 166.

7. **ssec:2.3.3, line 198: "work like the capacity payment in a power plant's PPA" compares the fees to something the reader has never seen.** Chapter 1's PPA is energy-only (USD 58.20/MWh as produced), and the PPA definition at line 166 mentions "capacity" without explaining it. Fix: add one sentence to the PPA definition at line 166: "A capacity payment is a fixed monthly amount for keeping the plant available whether or not the buyer takes its output; an energy payment is paid per megawatt-hour delivered." Add `\cref{ssec:18.1.1}`.

8. **Take-or-pay is used without being taught: line 399 ("not take-or-pay obligations"), line 416, and Framework 2.2 commentary.** Sabine Pass describes the mechanism ("pays the fixed fee on the volumes it does not take") but never names it, so the term arrives cold in Section 2.7. Fix: at line 198, add "an obligation known as take-or-pay: the buyer pays for the contracted quantity whether or not it takes it (\cref{ssec:18.4.1})".

9. **Clause 2.1, lines 66 to 79: the defined-term convention and several defined terms are unexplained.** The reader does not know that capitalized words are defined in the agreement. Unexplained terms include "Intercreditor Agent" (paragraph (c)iv, the only consent party, and not the facility agent the reader knows from Chapter 1), "Project Documents", "Affiliate", "Subsidiary", "Financial Year", "indemnity", "amalgamation, demerger", and, in annotation (b), "subordinated shareholder loans" and "working-capital basket". Fix:
   - Before the clause, add one sentence: capitalized words are defined in the agreement's definitions clause, and Chapter 10 and Chapter 51 teach the conventions.
   - In the annotations, gloss Intercreditor Agent ("the agent that acts for all the senior lender groups together"), Affiliate ("any company in the same group as a Sponsor"), and basket ("a capped amount allowed as an exception").

10. **Subordination is undefined: line 76 ("subordinated shareholder loans"), line 113 ("usually as subordinated equity"), and line 230 ("that structural subordination").** At line 230 the term is used as if the reader already knew it. Fix:
    - At line 76, define subordinated ("repaid only after the senior lenders have been paid").
    - At line 230, rewrite as "This position behind the project debt, called structural subordination, sets the pricing and structure."

11. **ssec:2.4.5, line 236: the bold definition of structured finance relies on "tranching" and "credit enhancement", which are undefined.** Credit enhancement's home is ssec:16.9.1. "Repackaged loans" is also opaque. Fix:
    - Gloss tranching ("splitting the debt into slices that are repaid in order of seniority").
    - Gloss credit enhancement ("support, such as a guarantee, extra collateral, or a junior slice, that improves the senior investors' position", with `\cref{ssec:16.9.1}`).
    - Replace "repackaged loans" with a concrete example the reader can picture.

12. **Example 2.2 (soiling), lines 179 and 185: the capacity argument uses a loss that the example itself has just separated.** Line 179 says the USD 441 thousand combined soiling and the firmware fault, and that the firmware fault was "a different risk with a different owner". Line 185 then argues capacity from "a loss of the size seen in 2018", which is the combined figure. The reader cannot tell how much of the loss was soiling, so the step does not follow. "Some fraction of its fee" is also vague. Fix:
    - Say explicitly that Chapter 1 does not split the USD 441 thousand.
    - Base the capacity test on the comparison the reader can check: a soiling loss of the 2018 order of magnitude, or one in a worse dust year, is comparable to or larger than the USD 412 thousand fee.
    - Replace "some fraction of its fee" with "a cap expressed as a share of the annual fee, set in negotiation". No new figures are needed.

13. **ssec:2.3.2, line 190: "force majeure and deemed-payment provisions" are used undefined.** Force majeure's home is ssec:10.5.1. Fix: add a gloss ("force majeure clauses, which excuse a party from performance prevented by events beyond its control (\cref{ssec:10.5.1})") and connect deemed payment to Chapter 1's deemed energy for curtailment.

14. **Example 2.4, line 352, and the drill, line 567: "over the reference rate" and "credit spread" are new.** From Chapter 1 the reader knows only a fixed all-in 5.40% loan and an intuitive margin. The reader does not know what a reference rate is or why a bond has a "spread" rather than a margin. Fix: add one sentence: "Both are premiums for credit risk over a benchmark interest rate: a loan's margin is added to a floating reference rate, a bond's credit spread to a government bond yield (\cref{ch:6})." At line 321 ("A corporate bond needs a prospectus and a rating"), gloss prospectus ("the offering document sold to investors"). At line 377, gloss "fee letter" ("the side letter that sets the arrangers' fees").

15. **ssec:2.9, line 463: "share costs 70:30" does not say which partner pays 70%.** Solution 2.13 (line 806) then depends on "At 70% ownership Kilnworth would consolidate". The reader also does not learn that Groupe Talmé is Mariama Talmé's family group from the Chapter 1 call. Fix: at line 463, write "Groupe Talmé, the Talmé family group whose call ends Chapter 1 ... in which Kilnworth would pay 70% of costs and Groupe Talmé 30%". The 70% stake is then available for Solution 2.13. Also state at line 463 that ownership would follow the same split, or else change Solution 2.13 to say "as the 70% partner".

16. **Case P scene, lines 468 to 486: three items need glosses in the surrounding narration.** "The revolver" (line 468) is a revolving credit facility, which the reader meets only at ssec:2.4.3, and then for reserve-based lending. "Per kilowatt-month" (line 480) is a capacity-tariff unit the reader has never seen. "The PPP Unit" (line 486) leaves PPP undefined; its home is ssec:57.6.1. The rating terms are covered in defect 5. Keep the dialogue as written and gloss in the narration before or after the scene:
    - "a revolving corporate credit line it could draw and repay at will";
    - "capacity tariffs on gas plants are quoted per kilowatt of capacity per month (\cref{ch:18})";
    - "the public-private partnership (PPP) unit in Kessara's finance ministry, which would run the tender (\cref{ssec:57.6.1})".

17. **Northvolt, lines 397 and 399: "first- and second-lien facilities" is undefined, and "16 GWh of capacity against a 60 GWh target" is ambiguous.** A Chapter 1 reader knows GWh as energy produced, not as factory output. "Export credit agencies" also appears with only a name-level introduction from Chapter 1. Fix:
    - Gloss lien ranking ("first-lien lenders are paid from the security before second-lien lenders").
    - Write "16 GWh a year of cell-production capacity (enough cells to store 16 GWh)".
    - Gloss ECA in one clause ("government agencies that insure or lend to support their country's exports", `\cref{sec:29.2}` or the registry's ECA home).

18. **ssec:2.5.2, line 303: the Moody's evidence uses three undefined measures.** These are "Basel definition of default", "10-year cumulative default rate", and "ultimate recovery". Fix:
    - Gloss the cumulative default rate ("the share of loans that defaulted at some point within ten years of origination").
    - Gloss the Basel definition ("the bank regulators' test, which counts a loan as defaulted once a payment is 90 days late or repayment in full is judged unlikely", `\cref{ch:68}`).
    - Gloss ultimate recovery ("the share of the defaulted amount lenders eventually got back").

19. **ssec:2.5.2, line 299: "Every dollar of surplus reaches the shareholders" contradicts its own paragraph.** The same paragraph says distributions occur "only then, if the distribution test is passed", and ssec:2.6.2 says cash is trapped below the lock-up. A novice reads these as conflicting. Fix: "Every dollar of surplus either reaches the shareholders or, if the distribution test fails, stays in the project company's accounts; none can be diverted."

20. **ssec:2.5.1, line 291: "as Case P's Kilnworth does when it sells down in 2026" is jargon about an unexplained future event.** Fix: "as Case P's Kilnworth will when, in 2026, it sells part of its stake and gives up control (\cref{ch:66})". Alternatively, drop the Case P pointer.

21. **Solutions introduce concepts that were never taught.** Solution 2.3 (line 702) has "a reference ground baseline", and Solution 2.11 (line 776) has "make perfection costly". A novice checking answers meets them cold. Fix:
    - Solution 2.3: gloss in a clause ("a contractual description of the expected ground against which the contractor is paid extra for worse conditions", `\cref{ch:22}`), or drop it.
    - Solution 2.11: replace "perfection" with "registering the lenders' security over 214 separate roof leases costly (\cref{ssec:52.3.1})".

22. **Exercise 2.12 and its solution (lines 647 and 788 to 790) ask the reader to classify "using only the facts given in this chapter", but two answers rely on facts the chapter does not give.**
    - Hyperion row: "Senior secured on the venture's assets" is stated nowhere. Line 238 says only "a private bond offering".
    - Eurotunnel row: "Recourse to owner: None to governments, by treaty" answers a different question. The governments were not the owner, and the chapter says nothing about recourse to Eurotunnel's shareholders.

    Fix: either add the facts to the text (from the fact sheets: line 238 states that the notes are secured on the venture's assets; sec:2.12 states the 1987 facility's recourse position), or change the two cells to "Not stated in this chapter". Also amend the exercise to allow the answer "cannot be determined from the chapter", and explain in the solution how the reader should handle a missing fact.

23. **Exercise 2.4, line 609: the exercise asks the reader to distinguish limited from non-recourse "using Llano Pardo before and after financial close".** No loan existed before close, so the contrast the question implies does not exist, and the solution (line 706) has to say so. Fix: reword to "Explain why Llano Pardo's loan was non-recourse, and what change to its term sheet would have made it limited recourse."

24. **ssec:2.1.2, line 64: Clause 2.1 is presented as drafted for "a wind farm in Chile's Biobío region, the deal that Examples 2.1, 2.3 and 2.4 follow".** The reader has not met that deal; it first appears at line 128. Fix: introduce the deal in one sentence at line 64 (GLA, a Santiago-listed generator, funding the 240 MW Alto Huelén wind farm in 2024), or make Clause 2.1 a generic illustrative clause and attach it to the wind farm when Example 2.1 introduces it.

25. **Opening, line 9: "Chapter 1's Llano Pardo deal used the same structure without naming it" is not true of Chapter 1.** Its brief (Section 1.3) introduces project company, special purpose vehicle, ring-fencing, and non-recourse by name, each with a one-sentence meaning. A reader who has just finished Chapter 1 will be puzzled. Fix: "Chapter 1's Llano Pardo deal used the same structure and named its parts in passing; this chapter defines them."

26. **"Receivables" is undefined: line 40 ("the PPA receivables"), line 234 (securitization definition), and Exhibit 2.2.** It is an accounting term the reader does not have. Fix: at line 40, add "the PPA receivables (the money ELNACOR owes for power already delivered)".

27. **Case P narration, line 519: "but not the common-law trust, so the lenders would need a security agent and parallel-debt mechanics".** The reader knows from Chapter 1 that Corredana is civil-law, and knows the security agent role. The reader does not know what a trust is, or why its absence creates a problem. Fix: add one clause: "a trust, the common-law device that lets one security agent hold security on behalf of every lender, so that lenders can change without re-taking security (\cref{ch:52})".

28. **Exhibit 2.2, line 253: "Holdco loan" uses an abbreviation the chapter never introduces.** The text at line 228 says "holding company". Fix: write "Holding-company loan".
