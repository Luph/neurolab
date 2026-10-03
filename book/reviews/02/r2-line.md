# Chapter 2 review, round 2: line editor

File: `chapters/02-what-project-finance-is.tex` (revised; log `reviews/02/r1-revision.md`). Standards: `standards.md` Section 8 and Section 12.7; `bible/style-sheet.md` with Addendum; D-126.

`scan_prose.py`: 0 hits. Em dashes: 0.

## Verdict: FAIL (narrowly)

The revision is substantial and mostly successful. Of my 55 round-1 defects, 54 are resolved and 1 (defect 1) is partly resolved; the verification table below records each. The patterns that would have spread across 87 chapters are gone: the italic run-in labels, the "Label: yes." block, the "Lenders gain from the same" formula and the "mechanism to carry away" formula. The four-lens collision at line 195 and the ranked Case P fit-test prose at lines 514 to 516 are now good models to copy.

Fifteen defects remain. Ten were introduced by the new glosses and additions, three are leftovers the earlier fixes did not touch, and two are partly unresolved. Two are clear errors a top editor would not pass:

- The sentence at line 223 now says the opposite of what it means.
- The sentence at line 36 is garbled.

The rest are line-level. All fifteen can be fixed in about an hour, and none needs restructuring.

## Verification of round-1 defects

| R1 | Status | Note |
|---|---|---|
| 1 | Partly resolved | Pointer endings are down to about 16 of 112 paragraphs, which is acceptable. Two were rewritten as hollow pseudo-claims instead of being cut; see R2-4. |
| 2 | Resolved, with one new instance | See R2-5 (line 297). |
| 3 to 7 | Resolved | |
| 8 to 11 | Resolved | |
| 12 to 14 | Resolved | The opening no longer duplicates 2.1.3, and the pull at line 9 is strong. See R2-1 on the gloss load in the first sentence. |
| 15 | Resolved | This created a back-to-back double definition; see R2-12. |
| 16, 17 | Resolved | |
| 18 | Not resolved as written | The new hook sentence is garbled; see R2-2. |
| 19 to 29 | Resolved | Sabine Pass now repeats one point across two paragraphs; see R2-10. |
| 30 | Resolved | The new opening introduced a vague "That is"; see R2-3. |
| 31 to 33 | Resolved | |
| 34, 35 | Resolved | 35 left a restatement; see R2-11. |
| 36 | Resolved | It left an orphan one-sentence paragraph; see R2-6. |
| 37 to 55 | Resolved | |

## Defects

R2-1. **The opening hook is front-loaded with glosses (§12.7 opening pull; §8 rhythm).** Line 3: the first sentence ends in a definition of Chapter 11, and the second carries a 20-word gloss of "consolidated balance sheet" plus a cross-reference. The scene stalls before the reader reaches the puzzle. Required fix: shorten both glosses to a few words. For example, "filed for Chapter 11 bankruptcy protection, which let it keep operating while a court supervised its debts", and "its consolidated balance sheet, the combined accounts of SunEdison and every company it controlled,". Drop `\cref{ssec:7.4.1}` from the opening; the first use in 2.3.1 or 2.5.1 can carry it.

R2-2. **Garbled hook sentence (§8 clarity; R1-18 not resolved).** Line 36: "A lender that checks only that it cannot be made to chase the sponsors can forget to check that the sponsors' creditors cannot reach the project." A lender does not check that it "cannot be made to chase" anyone. Required fix: "A lender that confirms only that the sponsors are protected from the project can forget to confirm that the project is protected from the sponsors' creditors."

R2-3. **Vague "That" opener introduced by the R1-30 fix (§8 vague This/That).** Line 213: "That is \term{corporate finance}, also called balance-sheet financing: ...". Required fix: "Borrowing of that kind, on the strength of a company's whole balance sheet and all its cash flows, is \term{corporate finance}, also called balance-sheet financing."

R2-4. **Pointers rewritten as hollow pseudo-claims (§8 hollow bridges; R1-1 partly resolved).** Two sentences exist only to carry a cross-reference:
   - Line 173: "Mapping the whole web and scanning it for such gaps before signing is a method of its own (\cref{ch:28})."
   - Line 323: "How governments measure them, and how statistical agencies decide whether such a plant counts as public debt, is a question of public finance in its own right (\cref{ch:57})."

   Required fix: attach the reference to the substantive sentence before each one, and cut the pointer sentence. At 173: "... so no contract moved the soiling loss away from the sponsors (\cref{ch:28} shows how to scan a web for such gaps)." At 323: end on "... and they appear in no budget until they do (\cref{ch:57})."

R2-5. **Signposted counts in new text (§8 signposted enumeration).** Line 297: "Two further gains follow from the same structure. Gearing ... And project finance lets ...". Required fix: delete the count sentence and open on gearing: "Gearing, the share of a project's cost funded with debt (\cref{ssec:8.2.1}), lets GLA own ...". Line 239 ("Securitization is one member of the family. Another is ... A third is ...") is milder. Recast it as one sentence: "The family includes securitization, the whole-business securitizations of some UK and European airports and water companies, which secure ..., and the hybrid structures that technology companies have begun to use for data centers."

R2-6. **Orphan one-sentence paragraph (§8 hollow bridge; rhythm).** Line 301, "A project lender's exposure, for its part, does not depend on ...", is left over after the R1-4 fix. It ends 2.5.1 with nothing attached, and "for its part" is filler. Required fix: move the sentence to open the Moody's paragraph in 2.5.2 as the lender's half of the argument, without "for its part". For example: "A project lender's exposure does not depend on whether the sponsor's other businesses prosper, and its information is far more complete than a corporate lender's. Moody's study ... shows what that is worth."

R2-7. **Overlong paragraph with an ambiguous pronoun (§8 one idea per paragraph; vague reference).** Line 311 runs to 252 words and covers two ideas: the default and recovery record, and what lenders get for it. It ends "Lenders buy it with transparency ..., control ..., security ..., and a price ...", where "it" could mean the record, the discipline or the lower pricing. Required fix: split the paragraph after "... once a project has a few years of operating history." Open the second paragraph with "Lenders get that record from four things: transparency (...), control (...), security over everything the project company owns, and a price set for each project's own risk." Alternatively, name the noun in place of "it".

R2-8. **Meaning inverted by a pseudo-cleft (§8 "It is X that ..." shapes; accuracy).** Line 223: "What makes the asset valuable is the difference from project finance." This says the difference from project finance makes a turboprop valuable. Round 1's sentence said the reverse and was correct. Required fix: "The difference from project finance lies in what makes the asset valuable."

R2-9. **Sentence overloaded by a gloss (§8 rhythm; clarity).** Line 514: "... but not the trust, the common-law device that lets one security agent hold security for every lender so that lenders can change without the security being taken again, so the lenders would need the substitute mechanics of \cref{ch:52}." Two "so" clauses are stacked inside an appositive. Required fix: split it. "... but not the trust. A trust is the common-law device that lets one security agent hold security for every lender, so lenders can change without the security being retaken. Without it, the lenders would need the substitute mechanics of \cref{ch:52}."

R2-10. **One point stated twice in consecutive paragraphs (§8 summary sandwich).** Lines 203 ("the lenders sized their debt to the fees from rated offtakers") and 205 ("the fixed fee was payable whether or not a cargo was lifted, and the lenders had sized their debt to that fee"). Line 201 has already said the offtaker "still pays the fixed fee on volumes it does not take." Required fix: end 205 on the COVID mechanism alone ("... but the mechanism is the one the Sabine Pass contracts created."), or cut the sizing clause from 203. Keep it in one place only.

R2-11. **Restatement inside the R1-35 fix (§8 summary sandwich).** Line 307: "... cannot divert a dollar to a second solar plant or a new venture, because ... Every dollar that passes the distribution test reaches the sponsors, and none can be spent on a venture the lenders have not approved." The second clause repeats the previous sentence. Required fix: end at "reaches the sponsors."

R2-12. **Double definition (§8 summary sandwich).** Line 24 opens with "... is what project finance means." The next sentence gives the formal `\term{Project finance}` definition. Required fix: make the first sentence lead into the definition instead of defining. For example: "The committee's question, what the plant would do and who had promised what, is the one every project lender asks. \term{Project finance} is financing in which ...".

R2-13. **Vague "It" opening a paragraph (§8 vague This/That).** Line 403 begins "It had no contracted revenue.", directly after a paragraph that ends on the facilities, the hedging and the debt service reserve account (Millar 2024). The antecedent is unclear. Required fix: "Northvolt Ett had no contracted revenue."

R2-14. **Gloss load stalls the real-case narrative (§8 rhythm; §12.7).** Line 92 runs to about 230 words, and three glosses (notes and bonds, "senior", indenture) interrupt the three-layer structure the paragraph is meant to show. Required fix:
   - Keep the bond gloss to one clause ("notes, which are bonds sold to investors (\cref{ssec:6.7.1})").
   - Move the senior, unsecured and guarantee sentence to Solution 2.12, where the classification needs it, or cut it to "unsecured senior notes guaranteed by Terra LLC".
   - Keep the indenture gloss, because 2.1.3 needs the reporting covenant.
   - Put the "At the top sat SunEdison" sentence back within two sentences of "In the middle sat TerraForm Power".

R2-15. **Overclaim in the close (§9 accuracy of tone; §8 grandiose claims).** Line 587: "None of those rules was obvious when lenders first used the structure on a megaproject." The Channel Tunnel was not the first project-financed megaproject; North Sea oil field financings in the 1970s came earlier, and Chapter 3 will teach them. Required fix: "None of those rules was settled when the Channel Tunnel's banks underwrote it." Alternatively, name the claim more narrowly. The facts reviewer should confirm the wording against `facts/eurotunnel.md`.

## Counts

15 defects. R2-2 and R2-8 are errors of meaning. The other 13 are line edits.
