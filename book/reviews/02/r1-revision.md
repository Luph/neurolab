# Chapter 2, round 1 revision log

File: `chapters/02-what-project-finance-is.tex` (rewritten section by section; v1 kept in the writer's scratchpad). Date: 2026-10-03.

Build: BUILD OK, 51 pages, 1 overfull box (0.27pt, Solution 2.9 `align*`, under limit); only cross-chapter references undefined; every `\cref` target exists in the registry (scripted). `scan_prose.py`: 0 hits; em dashes: 0. Words (source, excluding commands): body about 17,100, exercises and solutions about 3,800, sources about 540. The body grew by about 2,200 words, almost all of it glosses the novice reviewer asked for and the domain additions (leverage, credit substitution, holdco layer, sizing contrast, simplifications paragraph, covenant finding). Repetition was cut: the opening no longer restates 2.1.3; walkthrough Step 6 and the old Exhibit 2.3 restatements were trimmed.

Every new or changed number was recomputed in Python (`scratchpad/ch02/nums2.py`):
- overrun funded by the parent: 662.5 / 182.4 = 3.63x, a breach of 24.1; full 15% cap: 666.4 / 182.4 = 3.65x, a breach of 28.0; headroom covers 52% of the cap;
- revised cap of 7.5% = 29.2, giving (608.0 + 29.2) / 182.4 = 3.49x with 1.2 left; standby 58.4 − 29.2 = 29.2; with a 14% overrun, GLA pays 29.2 and the standby pays 25.3; GLA's worst case is 97.4 + 29.2 = 126.6;
- largest cap 30.4 / 389.6 = 7.8%;
- drill: 2.49 / 182.4 = 1.4% of EBITDA;
- Solution 2.11: 2.9 / (0.75 × 18.6 × 9.4) = 2.2% (about 220 bps);
- Sabine Pass original four SPAs about USD 1.96 billion; with BG's added volumes about USD 2.3 billion (fact sheet);
- Llano Pardo revenue shortfall 7,841 − 7,253 = 588 (USD 0.59 million); O&M cap range 0.21 to 0.41.

## Bible edits made (coordinator instructions)

- `bible/anchor-registry.md`:
  - rows `ex:2.1`–`ex:2.3` and `exh:2.1`–`exh:2.3` recaptioned to the chapter, with "was ..." notes;
  - `cl:2.2` added;
  - `ssec:2.4.3` retitled "Reserve-based lending" (line edit 31).
- `bible/briefs/u01.md` line 1153: `ex:2.3` → `ex:2.2` (soiling example). Not changed, and flagged for the coordinator: the Chapter 2 brief's own anchor table, example list (2.6) and Exercise 2.8 answer ("151.9 then 97.4") still carry the old numbering and the old figure (numbers review, writer-flag section).
- `bible/glossary-canon.md`: row "separateness undertaking" added (home `ssec:2.1.2`); the term is now bolded there.
- `\raggedright` removed from the sources list.

## Conflicts between reviewers and the choice made

1. **Units for Llano Pardo.** The numbers review (6), consistency review (20) and line review (7) disagreed. D-126 governs: prose now uses USD million (two decimals where precision matters, for example USD 0.41 million and USD 0.44 million); amounts under one million that are not Llano Pardo figures keep the house format (USD 28,700 a day, USD 76,500).
2. **Battery episode outcome (line 40) against the brief ("narrative, no new figures").** I followed the brief. The vague sentence "all of it cost months and fees" is replaced by the concrete gate sequence ending "before any battery could be ordered". No invented durations or fees were added.
3. **Soiling cap.** The line review suggested a number such as 30% of fee; the domain review gave a signed-off indicative range. I used the domain range (half to all of one year's fee, USD 0.21 million to USD 0.41 million, labeled indicative with market and period).
4. **Exhibit 2.2 font.** Consistency asked for `\small`; done. Cells were shortened so the exhibit fits the page.
5. **Covenant breach (domain A1, numbers 1, coordinator).** I re-engineered the recommended structure and also made the breach a finding of the board paper:
   - the lenders' first ask, a 15% cap, is shown to breach the covenant (3.65x);
   - the paper recommends cutting the cap to the headroom (7.5%, USD 29.2 million, 3.49x if called) and giving the lenders the rest of their overrun protection through a USD 29.2 million standby facility inside the project financing;
   - the same figures run through Example 2.3, Step 2 and Step 4 of the walkthrough, Exhibit 2.3, the drill and Exercise 2.7.
6. **Fit-test wording (domain 17, 18).** Question 2 now covers counterparty credit and currency, and the lead-in no longer claims a frequency ranking. This changes the wording of framework `fw:pf-fit-test`, which is flagged for the coordinator.

## Domain review (r1-domain.md)

| ID | Fix |
|---|---|
| 1 | Example 2.3 adds the overrun paragraph (662.5; 3.63x; 3.65x at the full cap; 52%). Walkthrough Step 2 gives the finding, the options weighed (letter of credit, covenant carve-out, share issue) and the recommendation (cap 29.2 plus standby 29.2). Exhibit 2.3 gains the rows for the cap and for leverage if called (3.49; 3.65 at first ask). The drill acknowledges the strain and explains why project finance still wins. |
| 2 | Step 7 now reads "a material rise in project finance margins relative to GLA's bond spread, or a fall in GLA's own spread". |
| 3 | Example 2.1 gives Alto Huelén a 15-year US-dollar PPA with a BBB- copper miner for 80% of expected output (illustrative). Step 4 refers back to it. |
| 4 | The non-recourse rung adds the contingency and standby facility sentence (`sec:31.7`). |
| 5 | "Modest risk" is cut. The overrun is now framed as turbine supply agreement versus balance-of-plant interface risk (`ch:23`). |
| 6 | Sponsor support now lists three forms. The equity letter of credit is moved to its own paragraph as support for the base equity (`ssec:32.3.2`). |
| 7 | The waterfall sentence now reads "Every dollar that passes the distribution test reaches the sponsors ...". |
| 8 | The text now states US substantive consolidation, *Prest v Petrodel* [2013] UKSC 34, and the French extension of proceedings for commingled assets. |
| 9 | The RBL valuation basis is given for both US and international practice, and the cure period is corrected. |
| 10 | Sabine Pass capacity is now "half". The 115% multiplier is described as covering feed gas plus fuel, and the fixed fee as paying for liquefaction capacity. |
| 11 | Solution 2.3 now uses "geotechnical baseline report" (`ssec:72.3.2`). |
| 12 | The Moody's default-curve shape and the 67% consortium coverage are added. |
| 13 | Bélanou size is now "a few percent, the range Alto Huelén showed". |
| 14 | The cost difference is tied to the illustration ("an investment-grade sponsor such as GLA"); the close now says "pays a price in margin and time"; the counter-case of a sponsor with weaker credit is added. |
| 15 | A simplifications paragraph after Example 2.4 covers the commitment fee, hedging, DSRA, negative carry, bullet versus amortizing debt and spread bases, with the direction of each and `ch:6` and `ch:38`. |
| 16 | `ssec:2.5.1` gains a leverage paragraph (GLA owns 389.6 with 97.4; `ssec:8.2.1`, `ch:8`) and a credit-substitution paragraph (Sabine Pass). |
| 17 | Fit-test question 2 is rewritten. Llano Pardo, Nairobi (shilling contracts, shilling debt), Northvolt and Bélanou are re-applied; the committee's miss is now framed as failing to apply question 2. |
| 18 | The framework lead-in no longer claims a frequency ranking. |
| 19 | The bank now offers to lead a syndicate request; the reasoning adds majority-lender consent and the expiry cliff. |
| 20 | Condition 2 is now based on the USD 127.8 million headroom and rating impact. |
| 21 | The going-concern note's project-level default risk and the loss of SunEdison's services are added. |
| 22 | The holding-company layer paragraph is added (`ssec:67.2.1`, `ssec:31.3.1`), and the Exhibit 2.1 note says it is omitted. |
| 23 | A fourth question on sizing and repayment is added; sizing is contrasted in 2.4.1, 2.4.2, 2.4.4 (term loan B) and the Exhibit 2.2 note; whole-business securitization is named. Coverage request: no registry home exists for whole-business securitization. |
| 24 | The soiling example now compares against the revenue shortfall (USD 0.59 million), states that the split between causes is unknown, gives the indicative cap range, and adds a parent guarantee from Montajes Cordillera. |
| 25 | The washed-away plant is replaced by "Had ELNACOR stopped paying in 2019". |
| 26 | The battery episode now has the PPA amendment and ELNACOR's (and the Ministry's) consent as the first gate. |
| 27 | Separateness undertaking is defined in bold, with no meta clause; the canon row is added. |
| 28 | The Eurotunnel row now reads "No government funds or guarantees under the treaty; shareholders' position cannot be determined". |
| 29 | The Terra Operating notes are classified as holding-company debt in the sense of `ssec:2.4.4`. |
| Confirmations | The covenant note now adds "count only the dividends those subsidiaries pay up". |

## Facts review (r1-facts.md)

| ID | Fix |
|---|---|
| 1 | Debt split: about USD 3.8 billion at TerraForm and the projects beneath it, much of the rest at project companies and warehouse vehicles SunEdison owned directly. |
| 2 | Now reads "many of them built or bought by SunEdison". |
| 3 | The opening sentence is rebuilt so that SunEdison is the explicit subject. |
| 4 | TerraForm Global 2017 8-K is cited and added to Sources. |
| 5 | Notes now total USD 950 million (800 + 150), plus 300. |
| 6 | The creditors' committee motion is dated November 2016, and the settlement is with the SunEdison debtors, signed alongside the Brookfield agreement. |
| 7 | Substantive consolidation is now presented as a US doctrine (see domain 8). |
| 8 | Sabine Pass capacity is now "half", with the other half reserved by a Cheniere affiliate. |
| 9 | The Cheniere 2022 Train 6 release is cited and added to Sources. |
| 10 | Debt is now raised on Blue Owl's side (Meta Platforms 2025 press release added). |
| 11 | Solution 2.12 cells are rewritten. The chapter text now states that the Terra Operating notes were unsecured and guaranteed by Terra LLC, and that the Hyperion notes are senior secured. |
| 12 | Cost figure is now "then estimated at approximately USD 27 billion". |
| 13 | The structured-finance example is made generic; the Exhibit 2.2 source line is rewritten. |
| 14 | Jensen and Meckling (1976) is credited for agency cost and Jensen (1986) for the debt argument; both Sources entries are updated. |
| 15 | (a) and (b) are tied to Example 2.4; (c) the close no longer states a market claim; (d) "like most" is now "like many". |
| 16 | Now reads "geotechnical baseline report". |

## Numbers review (r1-numbers.md)

| ID | Fix |
|---|---|
| 1 | Covenant breach resolved; see the conflicts list (item 5) and domain 1. |
| 2 | Bélanou is now "a few percent". |
| 3 | Sabine Pass fees: "Once BG had added volumes ... approximately USD 2.3 billion". |
| 4 | Soiling capacity now compares the revenue shortfall, "most of it soiling". |
| 5 | Solution 2.11 gives 220 bps (2.9 / (0.75 × 18.6 × 9.4)); "an USD" is removed. |
| 6 | Applied D-126. |

## Novice review (r1-novice.md)

| ID | Fix |
|---|---|
| 1 | Chapter 11 glossed (opening); going-concern note glossed (`ssec:7.11.1`, 2.1.3). "Bankruptcy estate" is no longer used; creditors' committee glossed. |
| 2 | Consolidated balance sheet glossed in the opening; substantive consolidation defined in 2.1.2; 2.1.3 now says "substantively consolidated". |
| 3 | Balance sheet glossed at first use (`ssec:7.4.1`). |
| 4 | Notes, bonds, senior and indenture glossed (`ssec:6.7.1`). |
| 5 | Ratings paragraph in 2.2.1 covers BBB-, Baa3, junk and downgrade cost (`ssec:30.5.1`). |
| 6 | LNG expanded; trains, MMBtu (`ssec:11.2.1`), Henry Hub and lump-sum turnkey (`ssec:22.1.1`) glossed. |
| 7 | Capacity and energy payments explained in the PPA definition (`ssec:18.1.1`). |
| 8 | Take-or-pay named at Sabine Pass (`ssec:18.4.1`). |
| 9 | Defined-term convention sentence added before Clause 2.1. Intercreditor Agent replaced by Facility Agent; Affiliate, Subsidiary, Project Documents, indemnity, subordinated and basket glossed in the annotations. |
| 10 | Subordinated glossed (annotation (b)); structural subordination defined in 2.4.4. |
| 11 | Tranching and credit enhancement glossed; "repackaged loans" replaced by whole-business securitization. |
| 12 | Soiling split stated; cap range given. |
| 13 | Force majeure (`ssec:10.5.1`) and deemed payment glossed. |
| 14 | Reference rate, margin and credit spread (`ssec:6.4.2`), prospectus and fee letter (`ssec:51.1.2`) glossed. |
| 15 | 70:30 split and ownership stated; Groupe Talmé identified; Solution 2.13 says "as the 70% partner". |
| 16 | Revolver, kilowatt-month and PPP unit glossed in narration (`ssec:57.6.1`, `ch:18`). |
| 17 | Lien ranking, ECA (`ssec:4.3.2`) and GWh of production capacity clarified. |
| 18 | Cumulative default rate, Basel definition (`ch:68`) and ultimate recovery glossed. |
| 19 | Waterfall sentence fixed. |
| 20 | Kilnworth sell-down rephrased. |
| 21 | Solution 2.3 and Solution 2.11 terms glossed or replaced. |
| 22 | Exercise 2.12 allows "cannot be determined"; solution cells changed accordingly. |
| 23 | Exercise 2.4 reworded. |
| 24 | Alto Huelén and GLA introduced where Clause 2.1 is presented. |
| 25 | Opening's final paragraph now says Chapter 1 "named its parts in passing". |
| 26 | Receivables glossed. |
| 27 | Trust glossed in the Case P fit-test paragraph. |
| 28 | Holdco now spelled out as "Holding-company loan". |

## Line review (r1-line.md)

| ID | Fix |
|---|---|
| 1 | Pointer endings reduced to 16 of 112 body paragraphs, mostly parenthetical references attached to a substantive sentence. The ch:8, ch:66, ch:52, ch:62, ch:77, ch:15, ch:21, ch:47 and ch:75 pointer sentences are moved mid-paragraph or cut. The "teaches ... in full" pointer phrasing is gone. |
| 2 | Count announcements removed at all of the listed places except the six fit-test questions. The four sizing questions and "three questions beyond the debt" remain because each is a checklist. |
| 3 | Italic run-in labels replaced by sentence openers in Examples 2.1 to 2.3; the walkthrough is now an `enumerate` of plain sentences. |
| 4 | "Lenders gain from the same" removed from both places. |
| 5 | Both "mechanism" formulas rewritten as direct claims. |
| 6 | Meta clause deleted; "From here on the book calls" and "as this book uses it" removed. The book's own coinages are marked only for the contractual web and the recourse ladder. |
| 7 | Money formats per D-126 (see the conflicts list, item 1). |
| 8 | "Over the next 20" now in numerals; the "twenty minutes" beat is cut. |
| 9 | Hand-typed references replaced with `\cref`; vague "above" and "below" references replaced. |
| 10 | Now "host government", "facility agent", "the sponsors", "O&M operator" and "tunneling contractor". In 2.1.1 the company is named rather than called "the borrower". |
| 11 | "CFO" spelled out. |
| 12 | Opening trimmed; details moved to 2.1.3; 2.1.3 adds only the new facts. |
| 13 | Pronoun fixed. |
| 14 | Opening pull now ends on the specific puzzle. |
| 15 | "That shift" sentence rewritten. |
| 16 | "Pile of steel" deleted. |
| 17 | Rhetorical question removed; paragraph now in the past tense. |
| 18 | Hook names the misjudgment. |
| 19 | Market norm labeled indicative with market and period; "a common way". |
| 20 | French doctrine named. |
| 21 | Announcement cut. |
| 22 | Fence images reduced; literal statements used ("separation of debt and assets held", "Control was never separated"). |
| 23 | Done. |
| 24 | "Interlocking" line cut; the third dependency is reshaped into the Llano Pardo gap. |
| 25 | Bridge sentence and two-line paragraph folded in. |
| 26 | "Precise" claim removed; cap range given. |
| 27 | Four-lens paragraph rewritten as a collision over the curtailment threshold, with the currency claim referenced to `ch:59`. |
| 28 | Zinger cut. |
| 29 | Sabine Pass paragraph openers varied; moral replaced by the mechanism. |
| 30 | 2.4.1 now opens on GLA. |
| 31 | Heading retitled; registry updated. |
| 32 | The consequence is stated (higher margin; sizing). |
| 33 | Reveal and personification cut. |
| 34 | Definition given once. |
| 35 | Corrected. |
| 36 | "Far more complete". |
| 37 | PNG LNG partners from the fact sheet, cited. |
| 38 | Noun named; generalization cut. |
| 39 | Bridge folded in. |
| 40 | See the conflicts list, item 2. "Two masters" replaced; lock-up syntax fixed. |
| 41 | Fixed-cost sentences moved to open 2.7. |
| 42 | Positive statement; the example ends on the securitization alternative. |
| 43 | "Enter X" removed. |
| 44 | Now "It had no contracted revenue." |
| 45 | Paragraph opens on Llano Pardo; the order-volume rule moved to Red flags. |
| 46 | Director questions kept only in Steps 1, 5 and 7, with shapes varied. |
| 47 | Now "State the accounting treatment". |
| 48 | The one-line answer is written. |
| 49 | Sample-passage gesture replaced (Devesh reading the agency's report); silence beat and "marked in red" cut. |
| 50 | Labeled block replaced by ranked prose: three conditional answers, then the clean ones. |
| 51 | Now "a few percent". |
| 52 | Both phrases fixed. |
| 53 | Replaced by 1.4% of EBITDA. |
| 54 | Close ends on the concrete open problem with a parenthetical `\cref`, with no rhetorical question and no announcement. |
| 55 | Now "The answer fixes". |

## Consistency review (r1-consistency.md)

| ID | Fix |
|---|---|
| 1–3 | Registry and u01 line 1153 updated (see Bible edits). |
| 4–5 | Hand-typed and vague references fixed; exh:2.1 source and note split. |
| 6 | References now point to `sec:32.7` and `ssec:63.7.3`. |
| 7 | ssec:82.7.2 is now described as tower and fiber. |
| 8 | Reference now points to `sec:82.9`. |
| 9 | Contingent equity references `ssec:32.3.3`; financial completion gloss includes "commercial". |
| 10 | Column renamed "Taught further in"; row 1 shows "--"; RBL references `sec:75.3`. |
| 11 | Source line rewritten. |
| 12 | "2024" common terms agreement date removed. |
| 13 | Kilnworth sentence now adds no history. |
| 14 | Canon row added and bolded; meta clause removed. |
| 15 | Canonical forms applied. |
| 16 | COD, O&M, LNG, PPA and EPC expanded at first use; SPA is no longer used. |
| 17 | Now 4.94x. |
| 18 | "Approximately" used before sourced real-world figures. |
| 19 | USD/MMBtu format used. |
| 20 | D-126 applied. |
| 21 | `\small` used in Exhibit 2.2; no size command in Exhibit 2.3. |
| 22 | `\raggedright` removed. |
| 23 | Kept `USD~X million`. A trial of `USD~X~million` produced three overfull lines. |

## Flags for the coordinator

- The wording of framework `fw:pf-fit-test` has changed (question 2 and the lead-in). Chapter 85, and any chapter that cites the framework, should use the new wording.
- There is no home for whole-business securitization. Please make a coverage request to place it (Chapter 80 or 81, or Chapter 30).
- The Chapter 2 section of the u01 brief (example list, anchor table, Exercise 2.8 answer) still uses the old numbering and the incorrect "97.4 after completion".
- New illustrative fact: Alto Huelén's PPA (15 years, US dollar, a copper miner rated BBB-, 80% of output). It is not placed in any real Chilean auction (D-127).
- New verified facts: *Prest v Petrodel* [2013] UKSC 34 (decided June 12, 2013), a settled authority on veil-piercing; and the French extension of insolvency proceedings for commingled assets (*confusion des patrimoines*), stated in general terms without an article citation.
- Hyperion: "senior secured notes" rests on the fact sheet's medium-confidence item 10.

# Round 2 (2026-10-03)

**Status.**
- Build: BUILD OK, 53 pages, one overfull box of 0.27pt; only cross-chapter references are undefined; every `\cref` target exists in the registry; every section title matches the registry (scripted).
- Prose scan: 0 hits; em dashes: 0.
- Word count, excluding commands: body about 17,600; exercises and solutions about 3,800; sources about 600.

**Case P (D-128, model v1.5).** Chapter 2 prints only these Case P inputs: USD 14.8 million, USD 12 million, 75%, 4.1 GW, BBB-, and the 70:30 split. None of them is affected by `model/figure-ledger-case-p-changes-v1.5.md`, so no update was needed.

## New numbers (Python: `scratchpad/ch02/nums3.py`)

Thresholds (the EBITDA at which the 3.50x covenant breaks):

| Net debt (USD m) | Breaks at EBITDA (USD m) | EBITDA fall to breach |
|---|---|---|
| 608.0 | 173.7 | 4.8% |
| 637.2 | 182.1 | 0.2% |

Dividend restraint (half of an illustrative USD 67.2 million dividend, so 33.6 retained):

| Case | Net debt (USD m) | Leverage | EBITDA fall to breach |
|---|---|---|---|
| After the equity | 608.0 - 33.6 = 574.4 | 3.15x | 10.0% |
| After a full call of 29.2 | 603.6 | 3.31x | 5.5% (breach at 172.5) |

Standby facility:
- Committed: 292.2 + 29.2 = 321.4.
- Drawn after a 14% overrun: 292.2 + 25.3 = 317.5.
- Upfront fee: 0.0225 × 29.2 = 0.66.
- Base loan plus full standby is 71.7% of cost plus the cap overrun, under the 75% gearing reference.

## Domain (r2-domain.md)

**N1. Cushion.**
- Step 2 now states the EBITDA falls that would break the covenant: 4.8% before any call and 0.2% after a full call.
- The paper sets a cushion policy (about 5% EBITDA fall after a full call) and meets it with a halved 2025 dividend (USD 33.6 million retained) plus the USD 29.2 million cap. This gives 3.31x after a call and a 5.5% cushion.
- The paper attaches a quarterly covenant forecast on trailing EBITDA.
- Exhibit 2.3 gains the leverage-after-call and EBITDA-fall rows; its note gives the unrestrained figures.
- Solution 2.7 now uses this wording in place of "to leave a margin".
- The drill concedes that project finance uses up GLA's construction headroom, and that the use is capped, temporary, and released at completion.

**N2. Standby facility.**
- Rewritten as the lenders' concession. The base loan plus the fully drawn standby must pass the cover-ratio and gearing tests (`sec:31.7`).
- The drawing order is presented as a negotiated term, with the fixed-ratio alternative noted.
- Price: an upfront fee of about USD 0.66 million, a commitment fee, and possibly a higher margin.
- If the lenders refuse, the fallback is an equity-funded overrun reserve or a letter of credit.
- Step 4 now shows project debt of 317.5 if the standby is drawn, with its effect on cover ratios and distributions.
- Exhibit 2.3 now reads "before the standby facility's fees".

**N3. PPA settlement.** Example 2.1 now states that the PPA is pay-as-produced and settled through the national market at the wind farm's own node. The miner bears the price difference between nodes and GLA keeps curtailment risk. Step 4 refers back to this.

**N4. Fit-test question 2.** Reworded so the currency condition applies to both the contracted branch and the merchant branch. Fit-test wording now:
- Chapter 2 brief section in `bible/briefs/u01.md`: updated.
- `bible/briefs/u17.md` Chapter 85: no prior citation existed. A citation with the new wording has been added to the "Concepts assumed" list.

## Numbers (r2-numbers.md)

- **Item 1:** Step 1 now asks the board to approve USD 292.2 million of senior debt plus a USD 29.2 million standby facility, USD 321.4 million committed. Step 6 now says "up to USD 321.4 million if the standby facility is drawn in full".
- **Item 2:** All three places now read "before the standby facility's fees". The USD 0.66 million upfront fee is stated in Step 2.

## Novice (r2-novice.md)

1. "Bank bond" changed to "bank guarantee (in construction usually called a performance bond, ch:22)".
2. "Amortizes" glossed in 2.4.2; "bullet bond" glossed in the paragraph listing the simplifications of Example 2.4.
3. The rating-scale sentence (AAA to BB) added to the ratings paragraph. The Moody's curve is now worded as "around BB" and "borrowers rated A".
4. The Exhibit 2.3 note explains why after-COD leverage is unchanged (no dividends from the wind farm assumed in the first year).
5. "PPP unit" is now lowercase in both narration and dialogue.

## Facts (r2-facts.md)

1. **French law.** Reworded to cover any company, commingled assets or a sham, with the citation (France 2022). Code de commerce art. L621-2 added to Sources with its Légifrance URL.
2. ***Prest.*** Wording now reads "to evade, or frustrate the enforcement of, an existing obligation or restriction". The in-text citation is now in house style, and the Sources entry has a URL and access date.
3. **Terra Operating notes.** Now described as unsecured senior notes, ranking equally with Terra Operating's other unsecured debt. The guarantee is stated as "guaranteed by Terra LLC" in the text; the full ranking sentence was cut under line item R2-14, and Solution 2.12 matches.
4. **"First use".** Replaced with "showed what that control could do".
5. **Hyperion.** The debt is now described as part of Blue Owl's side, sold privately to PIMCO and other bond investors (Meta Platforms 2025). "Senior secured" and "2049" are attributed to the fund holdings filing (PIMCO Variable Insurance Trust 2025), which is added to Sources.
6. **PNG LNG.** Now described as an unincorporated joint venture borrowing through PNG LNG Global Company, with the co-venturers' guarantee until financial completion in 2015. The citation key now matches its Sources entry.
7. **Whole-business securitization.** Narrowed to "whole-business-style" financings, with the Thames Tideway Tunnel company as the example (Bazalgette Tunnel Limited 2026, from the Tideway fact sheet). The Tideway annual report is added to Sources.

## Consistency (r2-consistency.md)

1. Mariama Talmé is now Groupe Talmé's deputy chief executive.
2. Kilnworth's 2026 sale is now in the past tense ("did when it sold").
3. "Approximately" now used for USD 3.8 billion and for 67%.
4. The DSRA and ECAs acronyms are removed (each was used once).
5. Now reads "O&M operator's solvency".
6. **u01 brief, Chapter 2 section.**
   - A round 2 note has been added.
   - All example and exhibit numbers have been converted to print order.
   - The anchor table is reordered, `cl:2.2` is added, and "Illustrative" is added to the `exh:2.2` caption.
   - The fit-test entry carries the chapter's wording.
   - Exercise 2.8 already read "151.9 before and after".

## Line (r2-line.md)

| Item | Fix |
|---|---|
| R2-1 | Opening glosses shortened; the `ssec:7.4.1` reference moved to the first use of "balance sheet" in 2.1.1. |
| R2-2 | Hook sentence rewritten as suggested. |
| R2-3 | "Borrowing of that kind ... is corporate finance". |
| R2-4 | The ch:28 and ch:57 pointer sentences cut; the references are now attached to the preceding claims. |
| R2-5 | Count sentence deleted. The structured-finance family is now one sentence. |
| R2-6 | The orphan sentence now opens the Moody's paragraph. |
| R2-7 | Paragraph split; the second part opens "Lenders get that record from four things". |
| R2-8 | Now "The difference from project finance lies in what makes the asset valuable". |
| R2-9 | The trust sentence is split. |
| R2-10 | The sizing clause is kept once (in the Sabine Pass paragraph on 2020). |
| R2-11 | The restating clause is cut. |
| R2-12 | The first sentence now leads into the definition instead of defining. |
| R2-13 | "Northvolt Ett had no contracted revenue." |
| R2-14 | The TerraForm paragraph is reordered (three layers, then the notes); glosses shortened. |
| R2-15 | Close now reads "None of those rules was settled when the Channel Tunnel's banks underwrote it." |

**Coordinator item (ssec:2.4.3 title).** The heading is restored to the registry's locked title, "Reserve-based lending compared with project finance". This reverses the round-1 retitle requested in line item R1-31.

## Flags

- **D-134.** The illustrative dividend of USD 67.2 million does not repeat as a value in any other brief or chapter. The two grep hits are Chapter 67 section labels, not figures.
- **Unverified illustrative assumption.** The 5% EBITDA cushion policy and the GLA dividend are illustrative assumptions with no market source.

# Round 3 (2026-10-03)

**Status.** Build OK, 53 pages, with one overfull box (0.27pt). Prose scan: 0 hits. Em dashes: 0.

## New numbers (Python)

- GLA net profit: 67.2 / 0.65 = 103.4.
- Halved dividend: 33.6 / 103.4 = 32.5% of net profit, above the 30% legal minimum (minimum 31.0).
- Headroom with the dividend restraint: 638.4 − 574.4 = 64.0.
- All other figures are unchanged from round 2: 3.15x, 3.31x, 10.0%, 5.5%, 4.8%, 0.2%, 106.6 bps.

## Numbers (r3-numbers.md)

1. Exhibit 2.3 now uses one basis throughout:
   - Construction and after-COD leverage read "3.15 (3.33 without restraint)".
   - Covenant headroom reads "headroom 64.0 (30.4 without restraint)".
   - The note states that figures include the restraint, and that the 33.6 is assumed still held after COD.
2. Step 2 now reads: "Even a cap of USD 29.2 million, 7.5% of cost and just inside the USD 30.4 million the headroom allows".
3. Exhibit 2.3 cost row now reads "248.0 (106.6 more; USD 3.1 million a year)", per the coordinator's wording.

## Domain (r3-domain.md)

**D1.** The 5% floor is now explained as a joint-stress floor: a full call made while EBITDA is down. Before any call the cushion is about twice that, 10.0%. The floor is labeled as "GLA's treasury policy, an illustrative one set by its board".

**D2.** The dividend cut is now a board proposal to the 2025 ordinary shareholders' meeting.
- The paper shows that the halved dividend (32.5% of net profit of USD 103.4 million) stays above the 30% minimum distribution for open corporations.
- It drafts a message to investors and rating agencies presenting the cut as a one-year retention.
- The 30% minimum is cited to Chile, Ley 18.046, article 79. I verified the article's text on 2026-10-03 from the Servicio de Impuestos Internos copy (sii.cl). The BCN page (bcn.cl) did not load, so it was not used. The SII copy is listed in Sources as "Chile 1981".
- The text says "unless every share votes otherwise", which is the article's unanimity exception.
- Flag: a pending bill reported in the press would change the quorum for that exception. It has not been verified and is not stated in the chapter.

**Minor.** Exhibit 2.3 cost row: done (see numbers item 3).

## Novice (r3-novice.md)

1. **Example 2.1.** Nodes, nodal settlement (`ssec:11.11.1`) and the system operator are glossed. The sentence now reads "settles any difference between the market price at the wind farm's node and at the mine's".
2. **PNG LNG.** "Unincorporated joint venture" is glossed. PNG LNG Global Company is now said to play the borrowing role of a project company.
3. **Exhibit 2.3 basis.** Fixed (see numbers item 1).
4. **Standby facility in Step 2.** Now "For the lenders the standby cuts both ways ... they treat it as a concession to the sponsor", with "the buffer of Ex 2.1 here sized to replace sponsor support". It is now consistent with Example 2.1.
5. **Tideway.** "Bankruptcy-remote" and "licensed business" are glossed.
6. **Step 2.** "Trailing twelve-month EBITDA" is glossed, and "hydrology" is replaced by "rainfall, which drives hydro output".

## Line (r3-line.md)

| Item | Change |
|---|---|
| R3-1 | Fit-test question 2 is now two-part: (a) creditworthy contracted revenue or forecastable revenue; and (b), whether contracted or merchant, revenue earned in the currency of the debt or hedged into it. The exact wording is propagated to `bible/briefs/u01.md` (Chapter 2 framework entry) and `bible/briefs/u17.md` (Chapter 85 assumed list). |
| R3-2 | Step 2 is split into three paragraphs: (a) the leverage arithmetic and cushions; (b) the policy, dividend proposal, forecast and rejected alternatives; (c) the standby facility and fallback. The false-contrast reframe is removed and the "most the headroom allows" error is corrected. |
| R3-3 | Step 4 no longer restates the settlement mechanics. |
| R3-4 | The Example 2.1 sentence is split, and "its own" is replaced by "the mine's". |
| R3-5 | The rating-scale sentence now comes before the threshold. |
| R3-6 | The repeated clause at the end of the drill's first paragraph is cut. |
| R3-7 | Handled by the coordinator's bps-row wording (see numbers item 3) rather than a separate row. |

## Consistency (r3-consistency.md)

1. "Most the headroom allows": fixed (see numbers item 2).
2. Exhibit 2.3 basis: fixed (see numbers item 1).
3. Registry note for `ssec:2.4.3` now reads "title restored in Ch 2 round 2 revision".
