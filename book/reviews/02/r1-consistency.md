# Chapter 2 review, round 1: consistency

Reviewer role: consistency (glossary canon, anchor registry, concept ownership, running-case continuity, style-sheet conventions, build).
File: `chapters/02-what-project-finance-is.tex`. Checked against: `standards.md`, `bible/style-sheet.md` (with Addendum), `bible/decisions.md`, `bible/briefs/u01.md` (Chapter 1 deal specification 1.A, Chapter 2 brief, Chapter 4 brief), `bible/ownership-resolutions.md`, `bible/glossary-canon.md`, `bible/anchor-registry.md`, `bible/case-bible.md`, Annex P, Annex TR (N.1, N.4), `model/case-state-case-p.md`, `reviews/02/writer-notes.md`.

## Verdict: FAIL

The chapter compiles cleanly, every `\cref` target exists in the registry, all section and subsection titles match the registry exactly, every canon term homed in Chapter 2 is set in bold once at its home, and the Llano Pardo and Case P facts agree with the deal specification, the Case Bible and the case state. These defects remain. (1) The writer's renumbering of examples and exhibits leaves the registry and one other brief pointing at the wrong objects. The writer notes say no other chapter cites these labels, but the Chapter 4 brief does. (2) The chapter has hand-typed and vague cross-references. (3) Some cross-references point to the wrong home label. (4) Some party names do not use the canonical forms. (5) Some acronyms are never expanded. (6) There are a few style-sheet format breaches.

## Build

`bash scripts/build_chapter.sh chapters/02-what-project-finance-is.tex`: BUILD OK, 46 pages. There is one overfull box, 0.27pt at source line 750 (Solution 2.9 `align*`). It is under the 5pt limit, so no action is needed. The only undefined references are cross-chapter ones, which is expected. No errors.

Scripted checks: all 67 distinct `\cref`/`\Crefrange` targets resolve in `bible/anchor-registry.md`. All 31 `\section`/`\subsection` titles match the registry captions verbatim. The 25 canon terms homed in Chapter 2 are each bolded once at their home. The two extra `\term{}` uses (recourse ladder, project finance fit test) are framework names, which style sheet 4.5 allows.

## Defects

### A. Labels, registry and cross-chapter consistency

1. **Registry not updated for the renumbered labels (whole chapter).** Registry rows `ex:2.1` to `ex:2.3` and `exh:2.1` to `exh:2.3` (anchor-registry.md lines 336 to 343) still carry the brief's captions. In the chapter, `ex:2.1` is now "Climbing the recourse ladder", `ex:2.2` is the soiling example and `ex:2.3` is "Two ways to fund a wind farm". `exh:2.1` is now the ring-fencing diagram, `exh:2.2` is the six-neighbors table (which now also carries `\illustrative`) and `exh:2.3` is the board-paper summary. The renumbering itself is correct (registry rule 3 and style sheet 3.2 require print order). Required fix (coordinator): update the six registry rows to the chapter's captions, in the form listed in writer-notes deviation 1, and mark each "was ex:2.x / was exh:2.x" in the Note column. Also update the Chapter 2 brief's anchor table (u01.md lines 775 to 782) and its example list (u01.md lines 654 to 658) so the brief and registry agree.

2. **The new `cl:2.2` is not in the registry (Solution 2.10, line 756).** Required fix (coordinator): add the row `cl:2.2 | Single-purpose and separateness undertaking, Llano Pardo common terms agreement (Illustrative) | new label; model answer to Exercise 2.10`.

3. **A cross-chapter citation now points at the wrong example (Chapter 4 brief).** `bible/briefs/u01.md` line 1153 (ssec:4.6.2) cites `ex:2.3` for "the availability guarantee that did not cover soiling". After the renumbering, `ex:2.3` is the leverage example and the soiling example is `ex:2.2`. Writer-notes deviation 1 says that "nobody outside Ch 2 cites these labels", which is wrong. Required fix (coordinator): change `ex:2.3` to `ex:2.2` at u01.md line 1153 before Chapter 4 is drafted. Re-run `grep -rn 'ex:2\.\|exh:2\.\|cl:2\.' bible matter chapters` after the registry update to confirm no other stale citation.

### B. Cross-references (style sheet 3.4)

4. **Hand-typed chapter references.** Line 9: "Chapter~1's Llano Pardo deal". Change it to "\Cref{ch:1}'s Llano Pardo deal" or rephrase as "The Llano Pardo deal of \cref{ch:1}". Line 61 (`\exhibitsource` of exh:2.1): "Chapter~1 deal specification" names an internal production document the reader never sees. Replace it with `\exhibitsource{\Cref{ch:1}, \cref{exh:1.1}.}` and move "dashed arrows show the limits of each group's claim" into `\exhibitnote{...}` (style sheet 4.3).

5. **Vague positional references instead of `\cref`.**
   - Line 190: "as with the soiling loss above". Change to "as with the soiling loss in \cref{ex:2.2}".
   - Line 401: "The fit test below catches both problems". Change to "The project finance fit test (\cref{fw:pf-fit-test}) catches both problems".
   - Line 554: "as the soiling example showed". Change to "as \cref{ex:2.2} showed".

6. **Yieldco forward reference points to the chapter, not the home section (line 87).** "\Cref{ch:32} teaches this listed-vehicle structure, known as a yieldco". The canon homes both yieldco and incentive distribution rights at `sec:32.7` ("Listed vehicles and yieldcos"). Change to `\Cref{sec:32.7}`. Optional: line 91 describes SunEdison pledging its Class B shares and IDRs to its own lenders, which is the subject of `ssec:63.7.3` ("SunEdison, TerraForm Power, and a margin loan on yieldco shares"). Add "(\cref{ssec:63.7.3})" after "collateral for SunEdison's own creditors".

7. **The securitization forward reference misdescribes its target (line 392).** "\cref{ssec:82.7.2} teaches digital and distributed-asset securitizations". The registry title of ssec:82.7.2 is "Tower and fiber securitizations and bank debt", and no section of Chapter 82 covers distributed (rooftop) assets. Rewrite as "\cref{ssec:82.7.2} shows how tower and fiber portfolios are securitized", or drop the Chapter 82 pointer and keep `\cref{ssec:2.4.5}` only.

8. **Hyperion forward reference is too coarse (line 240).** "\cref{ch:82} teaches how lenders get comfortable with it". The registry has a dedicated section, `sec:82.9` ("Hyperion and the short lease with a long guarantee"), and `ssec:21.9.2` ("Short leases and residual value guarantees"). Change to "\cref{sec:82.9} teaches how lenders get comfortable with it".

9. **Instruments cited to the wrong owner (ssec:2.2.2, lines 111 to 113).** The paragraph says "\cref{ch:26} owns the instruments" and then defines contingent equity among them. Contingent equity is homed at `ssec:32.3.3`. Add "(\cref{ssec:32.3.3})" after the contingent-equity sentence. The inline gloss of financial completion ("the lenders' test of physical, operational, and financial performance") omits "commercial" from the canon definition (home `ssec:26.5.2`, canon rule 2: no change of conditions). Write "the lenders' test of physical, operational, commercial, and financial performance (\cref{ssec:26.5.2})".

10. **The "Home chapter" column of Exhibit 2.2 contradicts the glossary canon (lines 245 to 255).** Under the canon, all seven financings in the table are homed in Chapter 2 (ssec:2.1.1 and 2.4.1 to 2.4.5), apart from reserve-based lending, whose home is `sec:75.3`. Yet the column lists ch:8, ch:66, ch:75, ch:47 and ch:82, and row 1 refers to its own chapter. Required fix: rename the column "Taught further in". Change the reserve-based lending cell to `\cref{sec:75.3}` (the label the prose at line 224 uses). Change row 1's cell to `--`.

11. **Exhibit 2.2's source line contradicts its contents (line 258).** "Examples are illustrative descriptions, not specific transactions". But "50 MW solar plant, Corredana, 2016" is Llano Pardo, "Chilean generator's bank loan, 2024" is GLA, and "Data-center venture with a value guarantee, US, 2025" is Hyperion, a real case. Replace it with `\exhibitsource{Chapter analysis. The project finance, corporate finance and structured finance examples are Llano Pardo (\cref{ch:1}), GLA (\cref{ex:2.3}) and Hyperion (\cref{ssec:2.4.5}); the others are illustrative.}`.

### C. Running-case and example continuity

12. **Clause 2.1 is dated before the deal it belongs to could be signed (line 64).** "an illustrative version drafted under English law for a 2024 common terms agreement for a wind farm in Chile's Biobío region, the deal that \cref{ex:2.1,ex:2.3,ex:2.4} follow". GLA's board decides on June 20, 2024 (sec:2.8), and Example 2.4 puts mandate to first drawing at about 14 months, so Alto Huelén's common terms agreement cannot be a 2024 document. Delete "2024" ("for the common terms agreement of the Biobío wind farm that ... follow"), or write "2025".

13. **A Case P fact that is not in the Case Bible (sec:2.9, line 517).** "Kilnworth had project-financed plants before". The Case Bible (Part 1.5 sponsor table; Annex P 2.1) says only that Kilnworth had 4.1 GW in operation. It does not say how those plants were financed. Later chapters (8, 26, 32, 47) could contradict this sentence. Required fix: either the coordinator adds the fact to Case Bible 1.5 ("Kilnworth's existing fleet is largely project-financed"), or the writer rewrites the sentence so it adds no history: "Lender control: yes. Kilnworth wanted non-recourse debt and accepted the consents and reporting that come with it."

14. **"Separateness undertaking" is a concept the brief says Chapter 2 owns, but it has no canon row, and the prose disowns it (line 64).** The brief (u01.md §2.3, "Owned: ... single-purpose and separateness undertakings") assigns the concept here. The canon has only "single-purpose undertaking". The chapter's text, "A separateness undertaking, which the book uses without a formal definition, is the project company's promise ...", defines the term while saying that it does not. Required fix: delete ", which the book uses without a formal definition,". The coordinator adds the canon row the writer proposes (home `ssec:2.1.2`). Once the row exists, set the term with `\term{separateness undertaking}` at line 64. Also add canon or registry-only rulings for "recourse ladder" and "project finance fit test", as requested in the writer notes.

### D. Canonical forms (style sheet 8.2 and Addendum A.3)

15. **Non-canonical party names.** Replace each of the following:
   - Line 299: "an account controlled by the lenders' agent". Change to "the facility agent" (or "the account bank", sec:4.8). Line 301: "administered by an agent bank". "Agent bank" is explicitly listed as not canonical; change to "administered by the facility agent".
   - Line 299: "Every dollar of surplus reaches the shareholders". Change to "the sponsors". Line 301: "The waterfall also protects shareholders from each other". Change to "protects the sponsors from each other".
   - Lines 185, 187 and 702: "the operator" (alone). Change to "the O\&M operator".
   - Lines 166 and 198 to 202 (Sabine Pass): "The buyer under the PPA is the offtaker" is fine as a definition. After it, "the buyers", "Each buyer" and "the buyers did not use" should read "the offtakers" or "each offtaker". Keep "LNG buyer" only inside the offtaker definition.
   - Line 315: "What remained with the government". Change to "with the host government". Line 164: "gave the lenders the government's stated backing". Change to "the host government's stated backing".

16. **Acronyms used without expansion in this chapter (style sheet 8.1: full term once at first use in each later chapter, then the acronym).**
   - COD is used five times (exh:2.3 and Exercise 2.14 and its solution) and is never expanded. At line 274, write "After the commercial operation date (COD)".
   - O\&M is used 15 times and never expanded. At its first use (line 77), write "operations and maintenance (O\&M)".
   - LNG is used 6 times and never expanded. At line 26, write "liquefied natural gas (LNG) export trains".
   - PPA and EPC are first used at lines 30, 56 and 77, before the bold home definitions at line 166. At line 30, write "the power purchase agreement (PPA)" and at line 77 "engineering, procurement, and construction (EPC)". Keep the bold `\term{}` at line 166, its home under R-123.
   - SPA appears in Solution 2.12 (line 787, "four 20-year SPAs") and is never introduced. Write "four 20-year sale and purchase agreements".

### E. Number and format conventions (style sheet 2, 6, 10)

17. **Multiples not given to two decimals (line 574).** "at leverage near 5\x". Style sheet 2.5 requires two decimals for net debt to EBITDA. Write "at leverage of 4.94\x".

18. **Approximate real-world figures use "about" instead of "approximately" (style sheet 2.3 and 9).** Lines 196 (USD 125 million), 198 (3.5 million tonnes; USD 2.3 billion), 238 (USD 27 billion; USD 12.31 billion; USD 28 billion), 240 (USD 2.9 billion), 397 (USD 1.6 billion), 399 (USD 30 million) and 590 (50 banks). Change each "about" before a sourced real-world figure to "approximately". Illustrative figures (for example "about 14 months") are unaffected.

19. **Unit-price format (line 198).** "a fixed fee of USD~2.25 to 3.00 per MMBtu". Style sheet 2.6 requires code, slash, unit. Write "a fixed fee of USD~2.25/MMBtu to USD~3.00/MMBtu".

20. **Inconsistent treatment of sub-million amounts in prose.** The chapter writes "USD~28,700", "USD~76,500", "USD~86,900" and "USD 250,000" (house format, style sheet 2.4). It also writes "USD~412 thousand" (lines 164, 185, 702), "USD~441 thousand" (lines 168, 179) and "USD~1,822 thousand to USD~1,381 thousand" (line 179). Addendum A.1 keeps the house format in prose. Write "USD~412,000", "USD~441,000" and "from USD~1,822,000 to USD~1,381,000". Alternatively, the coordinator rules that the Chapter 1 and Chapter 4 briefs' "thousand" form is the book-wide prose convention for Llano Pardo, and the chapter then applies it to every sub-million Llano Pardo figure.

21. **Font size of Exhibit 2.2 (line 244).** A seven-column table takes `\small` (style sheet 6.1: seven to nine columns `\small`; `\footnotesize` only for 10 to 12). Change `\footnotesize` to `\small` and rebuild to confirm there is no overfull box. Exhibit 2.3 (line 438) has three columns and takes no size command. Delete `\small` unless the build overflows.

22. **Manual layout command in the chapter (line 820).** `\raggedright` after `\begin{sources}` is a layout fix that belongs in `pfbook.sty` (style sheet 10: no manual layout; macros and environments are changed only through the coordinator). Required fix: the coordinator adds `\raggedright` (or `\PassOptionsToPackage{hyphens}{url}`) to the `sources` environment in `latex/pfbook.sty`. The writer then removes it from the chapter.

23. **Money macro (minor).** Style sheet 2.4 gives `\USDm{412.6}` as the LaTeX source for "USD 412.6 million". The chapter types `USD~389.6 million` throughout, which allows a line break before "million". Either convert to `\USDm{}`, or at least use `USD~389.6~million`. The printed form is otherwise correct.

## Items checked and found consistent (no action)

- Llano Pardo facts against u01 §1.A: 50 MW, 152 hectares, ELNACOR, 20-year PPA at USD 58.20/MWh, curtailment above 50 hours, three-month SBLC, Ministry of Finance letter of support, EPC USD 49.1 million by December 31, 2017, LDs USD 28,700 a day, performance test 81.4% against 81.0%, Montajes Cordillera's 410 MW record, O&M fee 412 for five years, 30-year lease, sponsors 60/40 and equity 16,270, total cost 65,078, loan 48,809, lock-up 1.15x, debt 32,929 at end-2024, OY1 shortfall 7.5% and distributions 1,822/1,381/441, cleaning cycles four to seven from 2019, 14 km line transferred at COD, English-law loan agreement, the security package, and opex about USD 1.1 million.
- Case P against Case Bible 1.1, 1.5, 1.8, Annex P 1.14.1, 2.1 and 2.2, and the case state for Ch 2: September 17, 2015 (a Thursday) in London; five and a half months after April 2, 2015; members and chair as specified; verbal habits used once each; USD 12 million raised to 14.8 million; 75% target gearing with ssec:8.2.1; 4.1 GW; BBB-; the co-development agreement of June 22, 2015 with the Phase-2 70:30 condition by September 30; the Emergency Power Plan of March 2015 for 450 MW to 650 MW at Bélanou beside the pipeline landfall; RFQ in 2016 ("won't be out before next year"); SEKA, the PPP Unit, the Government Guarantee; Kessaran security law (business pledge, no trust); 70% ownership pre-close (Solution 2.13); sell-down and deconsolidation in 2026 (ssec:2.5.1); financial close in 2018 ("next three years").
- Dates and weekdays of the GLA material: June 10, 17 and 20, 2024 (Monday, Monday, Thursday), with the July 15, 2024 deadline consistent across Examples 2.1, 2.3 and 2.4, sec:2.8 and sec:2.11.
- R-063, R-083, R-101, R-121 and R-123 applied. Reserve-based lending and debt capacity are not bolded and carry forward references. PPA, EPC contract and offtaker are homed at ssec:2.3.1.
- The order of the notebook, drill and solution elements, the solution "answer first / check / most common wrong answer" pattern, clause annotations for every paragraph, framework labels in the optional argument, and a status label on every example, exhibit and clause.
