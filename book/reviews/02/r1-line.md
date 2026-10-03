# Chapter 2 review, round 1: line editor

File: `chapters/02-what-project-finance-is.tex`. Standards: `standards.md` Section 8 (all of "AI writing tics to avoid") and Section 12.7; `bible/style-sheet.md` with Addendum.

`python3 scripts/scan_prose.py`: TOTAL HITS 0. Em dashes (`---`): 0. Every defect below came from reading each paragraph. The scanner cannot catch them.

## Verdict: FAIL

The prose is mostly clean and often very good: the Llano Pardo ring-fence paragraphs, the recourse ladder, the battery episode, the drill's reasoning and the scene's unresolved "Pays in what?" are the right voice. Because this chapter will be the voice exemplar for 87 others, its repeated habits matter more than any single sentence. Writers will copy whatever shape recurs here, so these need fixing first:

- About 20 paragraphs end on a "\Cref{ch:N} teaches ..." pointer (defect 1).
- Signposted counts appear throughout ("three ways", "three things", "two ways", "three kinds", "three advantages") (defect 2).
- Run-in italic labels are used as the default way to structure examples and the walkthrough (defect 3).
- The six-paragraph "Label: yes." block appears in Case P (defect 50).
- "Lenders gain from the same ..." and "The mechanism (to carry away) is ..." are reused as formulas (defects 4 and 5).

A top editor would not pass any of these in a model chapter. There are also zingers, an undelivered claim of precision, two numeric statements that contradict the chapter's own examples, and several style-sheet breaches in money format, number words, hand-typed cross-references and canonical names.

## Defects

### Chapter-wide patterns

1. **Monotone paragraph endings on forward pointers (rhythm, standards §8 "Monotone rhythm"; "Hollow bridge").** At least 20 paragraphs close with the same shape, "\Cref{ch:N} teaches/shows/takes up/tells ...": lines 81, 87, 93, 168, 202, 212, 218, 224, 230, 291, 301, 315, 381, 401, 505, 521, 590, and the near variants at 107, 240, 284, 293. The phrase "in full" recurs at 87, 166 (twice), 224 and 301. Required fix: keep a pointer only where the reader needs the destination at that moment, and move it inside the paragraph next to the claim it supports, as at 28 and 265. Cut the pointers that only advertise a later chapter: at minimum 212 (ch:8), 218 (ch:66, whose content is already in Exhibit 2.2), 301 (ch:52, already cited at 81), 381 (ch:62) and 401 ("\Cref{ch:77} tells the full case."). Use "in full" at most once in the chapter. After the fix, no more than one paragraph in five should end on a cross-reference.

2. **Signposted enumeration as the default argument shape (§8 "Signposted enumeration"; style sheet §11.6).** Instances:
   - 107 "The distinction matters to three parties beyond the sponsors and lenders."
   - 190 "The principle fails in three recognizable ways. The first is ... The second is ... The third is ..."
   - 212 "Corporate finance has three advantages that project finance cannot match:"
   - 230 "carries two differences that change its risk."
   - 265 "The first reason a sponsor uses project finance is ... The second, closely tied to it, is ..."
   - 313 "Project finance gave it three things."
   - 381 "The battery episode shows three kinds of control the lenders hold."
   - 385 "Project finance fails as a tool in two ways. ... The first kind ... the second ..."
   - 392 "Three alternatives fit better."
   - 576 "Two moves follow."

   Required fix: keep a count only where the number itself teaches something. The four forms of sponsor support (111) and the six fit-test questions (404) qualify. Everywhere else, delete the count sentence and open on the most important item, in connected prose. For example, at 190: "The commonest failure is a counterparty too small to absorb the risk it controls ...". Strip "The first ... The second ... The third ..." at 190 and 265.

3. **Run-in italic labels used as structure (style sheet §8.1: `\emph` "never for emphasis in sequence"; §8 "Bullets that open with a bolded label").** Lines 134 to 140 (`\emph{Full recourse.}` and so on), 181 to 185 (`\emph{Control.}`, `\emph{Pricing.}`, `\emph{Capacity to absorb.}`), 270, 280, 286 (`\emph{Corporate route.}` ...) and 422 to 434 (`\emph{Step 1. ...}` to `\emph{Step 7. ...}`). Required fix:
   - In Examples 2.1 to 2.3, open each paragraph with a sentence that names its case: "On the full-recourse rung, GLA borrows ..."; "Start with control. Cordillera Servicios decides ..."; "If GLA takes the corporate route, it borrows ...".
   - For the walkthrough, a seven-step sequence is a true sequence. Set it as an `enumerate` whose items begin with the step's instruction as a plain sentence, or keep it as prose paragraphs without italic labels.
   - The `\emph` run-in heads inside the two `clause` boxes (68 to 71, 758 to 761) follow drafting convention and may stay.

4. **Repeated formula opener "Lenders gain from the same ..." (§8 "Default sentence shapes"; monotone).** 293 "Lenders gain from the same isolation." and 303 "Lenders gain from the same discipline." Required fix: give each paragraph its own subject. At 293, open on the claim: "A project lender's exposure does not depend on ...". At 303, open on the record: "Moody's study of 10,452 project loans ...". Then state transparency, control and security as the mechanism behind that record.

5. **Repeated formula "The mechanism (to carry away) is that ..." (§8 "Emphasis and reveals", "The lesson is clear" family).** 93 "The mechanism to carry away is that a ring-fence is a set of contracts and corporate separations ..." and 401 "The mechanism is that project finance structure cannot turn manufacturing ramp-up risk into contracted cash flow." Required fix: state the claim directly. At 93: "A ring-fence protects exactly what its contracts and corporate separations cover." At 401: "No project finance structure turns manufacturing ramp-up risk into contracted cash flow."

6. **Meta-commentary about the book (§8 Banned outright: "meta-commentary about the writing").** 64 "A separateness undertaking, which the book uses without a formal definition, is ..." is the worst case. Lighter instances are 26 "From here on the book calls the SPV ...", 125 "is the book's name for this method", 168 "what this book calls" and 172 "as this book uses it". Required fix: at 64, delete "which the book uses without a formal definition" and simply define the term (the consistency reviewer handles whether it is bolded). Keep at most two "this book calls" coinage markers in the chapter: the contractual web and the recourse ladder. At 26 and 172, write the definition without the self-reference.

7. **Money below one million in "thousand" format (style sheet §2.4: "USD 45,000" for amounts below one million).** Lines 164 ("USD 412 thousand a year"), 168 ("USD 441 thousand"), 179 ("USD 1,822 thousand to USD 1,381 thousand, a loss of USD 441 thousand"), 185 ("USD 412 thousand") and 702 ("USD 412 thousand"). Addendum A.1 permits "USD k" only in table headers and confirms the prose form "USD 28,700 a day". Required fix: "USD 412,000", "USD 441,000", "from USD 1,822,000 to USD 1,381,000" (or "USD 1.8 million to USD 1.4 million" if precision is not the point, but keep 441,000 exact).

8. **Number words for 10 and above (style sheet §2.3).** 22 "over the next twenty" becomes "over the next 20". 488 "Philippa Carrow had said nothing for twenty minutes." is narration, not dialogue, so it becomes "20 minutes", or the sentence is cut (see defect 49).

9. **Hand-typed cross-references and unpointed back-references (style sheet §3.4; standards §10).** 9 "Chapter~1's Llano Pardo deal" becomes "\Cref{ch:1}'s Llano Pardo deal" or "The Llano Pardo deal of \cref{ch:1}". 61 `\exhibitsource{Chapter~1 deal specification; ...}` becomes `\Cref{ch:1}` (457 shows `\Cref` works in that argument). 105 "which is why the next section gives them a framework" becomes "\cref{ssec:2.2.2}" (it is the next subsection, not section). 554 "as the soiling example showed" becomes "(\cref{ex:2.2})".

10. **Non-canonical party names and elegant variation (style sheet §8.2; §8 "Elegant variation").**
    - "the government" alone for the host government: 164 "the government's stated backing", 190 "the government that owns the geological data", 315 "What remained with the government", 511 "the government guarantee behind it", 702 "the government may hold the geological data". Use "host government", or "Corredana's government" where a specific one is meant.
    - The account controller is called three different things. 299 says "an account controlled by the lenders' agent" and 301 says "administered by an agent bank". Use "facility agent" (or "account bank" if the account-holding bank is meant) and use the same term both times.
    - 22 "the borrower had no audited accounts" refers to Llano Pardo Solar SA. Use "the company" or the name; the defined term arrives at 26.
    - "the contractor" alone at 190 and 702: write "the EPC contractor" or "the tunneling contractor".

11. **Acronym used once (style sheet §8.1: "Do not create an acronym used fewer than three times").** 576 "An experienced CFO" is the only "CFO"; everywhere else the chapter writes "chief financial officer". Write "An experienced chief financial officer".

### Opening (lines 3 to 9)

12. **The opening is repeated almost verbatim in Section 2.1.3 (§8 Banned: explanations repeated; "summary sandwich").** Line 7 gives the going-concern note, the December 5, 2016 filing, the risk to indentures and listing, and the removal of the CEO and CFO. Line 91 restates all four with dates. Line 5 "Neither TerraForm company was pulled into the bankruptcy ... Brookfield bought control ..." is restated at 89. Required fix: let the opening carry the scene and the puzzle, with fewer facts and more stakes. Keep the bankruptcy, the two fenced companies, the lenders who could look only to them, and the governance fight as one sharp detail (the November 20, 2015 removal of TerraForm's chief executive and chief financial officer). Move the going-concern note, the filing date and the indenture and listing risk to 2.1.3 only. In 2.1.3 cut the restatement at 89 to the one new fact (Brookfield's March 2017 agreement).

13. **Ambiguous pronoun in the opening (line 7).** "Its 2015 annual report was not filed until December 5, 2016, ... Five months before SunEdison's bankruptcy, it had used its voting control to remove TerraForm Power's chief executive ..." The nearest antecedent of "it" is TerraForm Power, but SunEdison is meant. Required fix: "SunEdison had used its voting control ...".

14. **Opening's final pull is generic (§12.7 "the opening pulls the reader in"; §8 "generic statements").** 9 "... are the first things a project financier needs to understand about it." This could close any chapter in any book, and "about it" has no clear antecedent. Required fix: end on the specific puzzle, for example: "Chapter 1's Llano Pardo deal used the same structure without naming it: a company that owned one plant, lenders who could look only to that plant, and owners who could lose only what they put in. The TerraForm companies had all three, and their sponsor's bankruptcy still reached them." The next section then answers how.

### Section 2.1

15. **Vague "That" opener plus a grand claim (§8 "vague This/That"; "Grandiose claims about the field").** 24 "That shift in the question defines the discipline." Required fix: name the shift and the claim: "Lending against what a plant will do and who has promised what, instead of against a borrower's history, is what project finance means."

16. **False contrast against a misconception the reader does not hold (§8 "False-contrast reframes").** 24 "the lender's protection on default is the ability to take over a working plant and its contracts, not the ability to sell a pile of steel." Required fix: delete ", not the ability to sell a pile of steel". The positive claim teaches the point, and 220 makes the scrap-value contrast properly later.

17. **Self-answered rhetorical question as a transition, plus tense drift (§8 "self-answered questions used as transitions").** 30 "Why form a new company at all, when Grupo Arismendi already had companies that could have signed the PPA? Each reason comes from a different chair at the table." The paragraph then shifts from present tense ("The lenders want", "The sponsors want") to past ("Tallisford ... needed", "ELNACOR and the Ministry ... wanted"). Required fix: open with a statement, for example "Grupo Arismendi already had companies that could have signed the PPA; every party at the table had a reason to want a new one instead." Put the whole paragraph in the past tense, since it describes the 2016 deal.

18. **Unsupported generalization as a paragraph hook (§8 "generic statements").** 36 "It works in two directions, and practitioners who remember only one of them misjudge deals." Required fix: name the misjudgment ("a lender who checks only that the sponsors cannot be reached forgets to check that the sponsors' creditors cannot reach the project"), or cut the clause.

19. **Bare market norm and unsupported superlative in the clause annotations (style sheet §1.1, "Never state a bare norm"; §8 "Superficial" claims).** 75 "The usual landing is a narrow clause plus a consent process." needs a market and period, for example "In Latin American renewable financings closed 2020 to 2025, ...". 77 "the most common way value leaks out of a fenced project" is unsupported, so write "a common way" or give the basis.

20. **Generic claim where the doctrine should be named (§8 "generic statements"; "Superficial comprehensiveness").** 81 "civil-law systems reach similar results through other doctrines." Required fix: name one doctrine and one jurisdiction (for example, extension of insolvency proceedings for commingled estates in French law), or cut the clause.

21. **Announcing instructiveness (§8 "Announcing candor or importance instead of showing it").** 85 "and the result was mixed in a way that teaches more than a clean success would have." Required fix: cut and state the result: "The debt and assets stayed fenced; the governance did not."

22. **"Fence" metaphor extended past the defined term (§8 "metaphors extended past the point where they teach").** "Ring-fence" is the industry term and is fine. The derived images pile up, though: 34 "build a fence around the project company with promises", 81 "Whether the fence holds", 87 "here only its fence matters", 89 "The fence around the projects ... held", 91 "The fence around governance did not hold, because SunEdison's control rights crossed it by design", 588 "a fence of promises". Required fix: use "ring-fence" as the term, and in at least half of these places say the literal thing ("the separation of debt and assets held"; "SunEdison's control rights were never separated").

### Section 2.2

23. **Vague quantifier and overclaim (§8 "Vague quantifiers").** 105 "Many project financings sit here, especially during construction." and "The defined amount and the defined period are the whole negotiation". Required fix: either give a qualified market observation with period and market, or write "Most construction-stage financings with a sponsor carrying technology or overrun risk sit here." Replace "the whole negotiation" with "what the parties negotiate".

### Section 2.3

24. **Announced emphasis (§8 "Emphasis and reveals"; "The key is ..." family).** 168 "``Interlocking'' is the working word." Required fix: delete it and run straight into the three dependencies. Those three "has to" sentences are themselves a rule-of-three cadence, so make the third a different shape, for example by attaching the O&M availability point to the Llano Pardo soiling gap that follows.

25. **Hollow bridge and zinger (§8 "Hollow bridge paragraphs"; "The zinger").** 172 ends "Each of the three tests asks a different question." That sentence is a bridge that only announces 174; cut it. 176 is a two-sentence paragraph ending "The work begins when they diverge." Fold it into 174 as the transition into Example 2.2, or cut it.

26. **Claimed precision not delivered (§8 "It depends" without how much; "Announcing").** Example 2.2, 185: "Capacity points away from the O&M operator once the loss passes some fraction of its fee." 187: "The answer the tests give is precise. ... pay for its failures up to a cap set as a share of its annual fee". The paragraph claims precision and then gives no number, and "its balance sheet runs to a few million dollars" is vague. Required fix: delete "The answer the tests give is precise." Give the cap as a number tied to the operator's capacity, for example "a cap of 30% of the annual fee, USD 123,600" (the numbers auditor to confirm), and state the operator's net worth as a figure from the Chapter 1 spec, or drop it.

27. **Four lenses as a parallel list, not a collision (style sheet §1.2 [BAD] pattern).** 192 "The sponsor reads it as ... The lender reads it as ... The EPC contractor reads ... The host government reads ..." These are four parallel sentences in which no lens meets another. The paragraph also ends on the bare claim "currency risk becomes the hardest negotiation on emerging-market deals". Required fix: rewrite around one risk on one deal (for example Llano Pardo's grid-curtailment risk above 50 hours a year) and show what each party asked for and what it traded, as in the style sheet's [GOOD] delay-LD paragraph. Support the currency claim with a pointer (`\cref{ch:59}`) or cut it.

28. **Zinger ending (§8 "The zinger").** 190 ends "Who pays for each is a negotiation over price, not a question the control test can settle." This restates the paragraph in a false-contrast shape. Cut it; the paragraph's last substantive point is the list of who holds uncontrollable risks.

29. **Repetitive paragraph openers and a tidy moral in Sabine Pass (§8 "Monotone rhythm"; "Tidy morals").** Consecutive paragraphs open 198 "The contracts made it financeable." and 200 "The contracts moved the commodity risk to the buyers.", followed by 202 "The test came eight years later." 202 then ends "which is the contractual web doing exactly what the lenders had underwritten." Required fix: open 198 on the event ("Between October 2011 and January 2012 the project company signed ...") and 200 on the financing ("On July 31, 2012, ..."), with the risk-transfer claim placed after the facts. End 202 on the mechanism without the moral: "The fixed fee was payable whether or not the cargo was lifted, and the lenders had sized their debt to that fee."

### Section 2.4

30. **Rule of three twice in a row, with a colon reveal (§8 "reflexive rule of three"; "Colon reveals").** 212 "Corporate finance has three advantages that project finance cannot match: it is cheap to arrange, fast, and flexible. One loan agreement funds many projects, the company can change its plans without asking anyone, and diversification does the risk management, ..." Required fix: open with GLA, for example "GLA can fund a new plant from its existing facilities in weeks, at the cost of a drawdown notice, and change the plan without asking anyone ...". Let the item count follow the content.

31. **Inconsistent sibling heading (§8 Headings: "names its content plainly"; consistency).** 222 "Reserve-based lending compared with project finance" sits among the siblings "Corporate finance", "Asset finance and leasing", "Acquisition finance" and "Securitization and structured finance". Required fix: "Reserve-based lending".

32. **Vague consequence (§8 "It depends" without direction).** 230 "Pricing and structure follow from that structural subordination." Required fix: say how. For example: "Holding-company lenders therefore charge a higher margin than the project lenders and size to distributions after a lock-up test, not to project CFADS (\cref{sec:31.3})." Use the canonical "trapped cash" wording if trapped cash is mentioned.

### Section 2.5

33. **Mini-reveal formula and a personified, unsupported claim (§8 "Emphasis and reveals"; "Personified abstractions").** 291 "The general idea has a name." and "The parenthesis carries a trap that catches finance directors every year." Required fix: cut the first sentence and open on the definition. Replace the second with the mistake itself: "Finance directors routinely confuse the two: GLA would own 100% ...". "Every year" cannot be supported, so drop it.

34. **Definition stated twice (§8 "summary sandwich").** 297 first says "Michael Jensen called the loss of value from managers acting in their own interest rather than their investors' an agency cost", then two sentences later "An \term{agency cost} is the loss of value that arises when managers or one set of owners act in their own interest at the expense of other investors." Required fix: give the `\term` definition once, at the first mention, and attribute the debt argument to Jensen in the next sentence.

35. **Zinger that is also wrong (§8 "The zinger"; accuracy).** 299 ends "Every dollar of surplus reaches the shareholders." That is not true under a lock-up, which 381 describes, or while reserves are being funded. Required fix: cut it, or write "Whatever is left after the waterfall and the distribution test reaches the shareholders, and nothing reaches a second plant or a new venture."

36. **Overclaim (§8 "Hedging"; accuracy of tone).** 293 "its information is complete in a way a corporate lender's never is". Required fix: "far more complete than a corporate lender's", or name what the corporate lender lacks.

37. **Generic example (§8 Epistemic tics: "Generic examples that could be set anywhere").** 307 "a mining major, a state oil company, and a Japanese trading house can share one LNG plant through one project company". Required fix: name a real partnership from a fact sheet (for example, PNG LNG's partners, if `facts/` supports it), or set it as a labeled illustration with a place.

38. **Vague "These" opener and unsupported generalization (§8 vague This/That; generic statements).** 315 "These are contingent liabilities, ..." should name the noun: "The termination payment and the implicit support for ELNACOR are contingent liabilities, ...". "matters more than most ministries admit when they sign" is an unsupported generalization; cut "than most ministries admit when they sign".

### Section 2.6

39. **Hollow bridge (§8).** 377 is a two-sentence paragraph ("The larger costs of project finance never appear in a fee letter. They are what the sponsors give up for the life of the loan.") that only introduces 379. Required fix: fold it into the first sentence of 379, or cut it.

40. **Vague outcome and stock idiom in the battery episode (§7 "concrete"; §8 Clichés).** 379 ends "None of that was unreasonable, and all of it cost months and fees." The chapter never says how many months, how much in fees, or whether the battery was built. 381 "so the project company's management works for two masters" is a stock idiom. 381 "Llano Pardo's being 1.15\x" is awkward syntax. Required fix:
    - Give the elapsed time and adviser cost (from the Chapter 1 spec, or labeled illustrative) and the outcome.
    - Replace "works for two masters" with the literal point: "reports to the lenders as well as to its board".
    - Write "below the lock-up level, 1.15\x{} at Llano Pardo,".

41. **One paragraph, two ideas (§8 "one idea per paragraph").** 373 covers the simplification first and then switches to fixed costs and project size ("The costs are largely fixed: ..."). Required fix: move the fixed-cost and size sentences to open Section 2.7, where they set up Example 2.5. "simplifies in one direction worth naming" becomes "simplifies in one direction".

### Section 2.7

42. **False contrast and zinger in Example 2.5 (§8 "False-contrast reframes"; "The zinger").** 392 "Nothing about the portfolio's risk rules out project finance. ... What rules it out is the ratio of fixed costs to the amount financed." The example ends "Small project financings fail on their fixed costs long before their risk becomes the question." Required fix: state it positively once ("The portfolio's risk would pass; its size would not: fixed costs are 15.6% of the amount financed."), and end the example on the third alternative.

43. **"Enter X" bridge (§8 Signposts: "Enter X.").** 395 "The opposite failure happens when the cash flows cannot be pinned down, whatever the size of the project. Northvolt shows it." Required fix: delete "Northvolt shows it." and merge the first sentence into the opening of 397 ("A project can fail the other test, forecastable cash flow, at any size. Northvolt AB, a Swedish ...").

44. **Pseudo-cleft reveal (§8 "Emphasis and reveals").** 397 to 399 "The structure had every feature of a project financing. ... What it could not have was a project's revenue." Required fix: "It had no contracted revenue." Then explain the orders.

45. **Paragraph mixes application with a new rule (§8 one idea per paragraph).** 416 applies the fit test to three projects and then states a new rule ("Before answering yes to question 2 on the strength of order volumes, ask what the buyer must pay ..."). The opening "gives clear answers on the three projects this chapter has met" is announcement. Required fix: open on Llano Pardo directly, and move the order-volume rule into the notebook (Red flags or Questions experts ask) or into its own short paragraph after the Northvolt verdict.

### Section 2.8 walkthrough

46. **Same closing shape in all seven steps (§8 "Monotone rhythm").** Every step ends with "A director asks: ...?", with variants at 428, 432 and 434, and several of the questions are then answered in the next breath ("Yes, through the change-of-control clause"). Required fix: keep the skeptical question in the steps where it changes what the paper must contain (Steps 1, 3, 5 and 7). In Steps 2, 4 and 6, state what the paper must anticipate as a plain instruction. Vary the sentence shapes.

47. **Announced candor (§8 "Announcing candor or importance").** 432 `\emph{Step 6. State the accounting honestly.}` and "the paper says plainly that ...". Required fix: "Step 6. State the accounting treatment." and "the paper says that ...".

48. **Promise not delivered (§1 "Practical"; §8 "promises of content that never arrives").** 434 "A director's last question is usually the best one: which of those conditions is most likely, and how would we know? A good paper answers it in one line." The line is never given. Required fix: write the line, for example "The likeliest is a rating-agency change: watch for the agency's methodology comment on GLA after the Q3 results, and treat any statement that project debt will be consolidated as the trigger to revisit." Cut "is usually the best one".

### Section 2.9 Case P

49. **Body-language tic copied from the style sheet sample (§8 Narrative tics; style sheet §1.3).** 470 "Devesh Raval didn't look up from the paper." is lifted from the style sheet's [GOOD] sample ("The arranger didn't look up from the sizing printout"). Writers of 87 chapters will copy it as a house tic. 488 "Philippa Carrow had said nothing for twenty minutes." is the stock silent-character-finally-speaks beat. 466 "the pipeline landfall marked in red" is physical detail that changes nothing (style sheet §1.3). Required fix: replace 470 with an action that carries information (for example, Devesh is reading the rating agency's last report on Kilnworth). Introduce Philippa by her role and her question with no silence beat. Drop "marked in red".

50. **Labeled-colon paragraphs (§8 "Bullets that open with a bolded label and a colon"; "Colon reveals"; monotone).** 509 to 519: six consecutive paragraphs open "Separable asset: yes.", "Contracted revenue: yes in structure ...", "Construction risk fixed: yes, in principle.", "Size: ample.", "Lender control: yes.", "Enforceable security: yes, with work." This is the bullet-label pattern set as prose, and it will be copied into 87 chapters. Required fix: either set the six questions as a three-column table (question, answer, condition), which suits a six-by-three comparison per style sheet §6.1, followed by one paragraph on the three conditional answers, or write connected prose that ranks the three conditional answers by how much they threaten the deal and gives a sentence to the three clean ones.

51. **Numeric statement contradicts the chapter's own example.** 515 "the ratio that killed the Nairobi rooftops would be a fraction of a percent here." Example 2.4 puts the same costs at 3.55% on a USD 389.6 million wind farm, so "a fraction of a percent" on a plant of several hundred megawatts is not credible. "Killed" is also decorative. Required fix: give an order of magnitude consistent with Example 2.4 ("likely 2% to 3% of cost, against 15.6% for the rooftops"), labeled as an estimate, or delete the clause.

### Notebook, drill, close, exercises

52. **Zinger and stock idiom in the notebook (§8 "The zinger"; Clichés).** 553 "transfers the paperwork, not the loss." Required fix: "... leaves the loss with the project company once it exceeds what that party can pay." 540 "recourse in everything but name" becomes "add up to recourse".

53. **Zinger in the drill (§8 "The zinger").** 572 "A saving of that size is real money to a board." Required fix: give the context and let the reader judge: "USD 2.5 million a year is 1.4% of GLA's EBITDA."

54. **Closing pull uses a rhetorical question plus a next-chapter announcement (§8 Signposts: "In the next chapter, we'll explore ..."; "Cliffhanger formulas"; §12.7 closing pull).** 590 "How did a ring-fenced, contract-backed financing reach that point, and what did lenders change afterward? \Cref{ch:3} answers that question, and in answering it shows where each of this chapter's rules came from." Required fix: end on the concrete open problem without announcing the next chapter. For example: "In September 1995 the company suspended interest on approximately GBP 8 billion of debt, and the lenders who had underwritten a ring-fenced, forecast-backed structure had to decide what their security was worth. (\cref{ch:3})." Cut "and in answering it shows where each of this chapter's rules came from."

55. **Vague "This" in a solution (§8 vague This/That).** 802 "This fixes Kilnworth's place on the recourse ladder ..." Required fix: "The answer fixes ...".

## Counts

55 defects. 11 are chapter-wide patterns (1 to 11), and 1 to 3 and 50 will propagate most if left in the exemplar.
