# Blueprint review: sequencing lens

Reviewer lens: concept ownership and teaching order across Chapters 1 to 88, plus the agreement of the glossary canon, anchor registry, Case Bible (with Annexes P and TR), figure ledgers and briefs on homes, labels, dates, figure IDs, characters and story order. Date: October 3, 2026.

Method: I parsed `bible/anchor-registry.md` (5,240 labels), `bible/glossary-canon.md` (1,771 table rows), the 17 unit briefs (88 chapters split by section), Case Bible Part 6 and Part 7, Annex P Sections 2 and 8, Annex TR Parts T.16, R and F, and `model/figure-ledger-case-p.md`. I ran scripts for these checks:

- label numbering and sequence by type and chapter;
- framework table against the chapter tables;
- registry chapter titles against `architecture.md`;
- every label cited in any Bible file against the registry;
- canon homes against the 121 rulings and against the unit glossaries;
- early use of each canon term before its home chapter;
- duplicate section headings across chapters;
- brief running-case figure IDs and characters against the Part 6 rows.

I then read each candidate in context. All line numbers below refer to the files as of this review.

## Verdict: FAIL

The blueprint fails on one blocking defect: the provisional figure IDs P-F37 to P-F41 have different meanings in different briefs, and those meanings collide with the IDs that Annex P and the ledger now assign. It also has 25 major and 15 minor defects.

Counts: blocking 1, major 25, minor 15.

---

## Blocking

### 1. Figure IDs P-F37 to P-F41 mean different things in the briefs, Annex P and the ledger

- Location: briefs u05, u06, u08, u09, u11, u12, u14, u15 and u17 (running-case sections, bible-flaw lists and figure tables); `case-bible-annex-p.md` §8.1 and §8.2; `model/figure-ledger-case-p.md`; `anchor-registry.md` line 3772 (`exh:55.10` "conditional on P-F37").
- Defect: Each unit "requested" its own P-F37 to P-F41, and they disagree. Annex P renumbered them (P-F46 to P-F63), and the ledger now prints P-F37 = VAT, P-F38 = thin capitalization, P-F39 = LC sizes, P-F40 = FX and crisis items, and P-F41 = PLCR and DSCR profiles. The briefs still cite the old IDs, so a writer who follows the brief prints the wrong ledger block. Verified instances:
  - Ch 21 (u05:1401): P-F37 is the GTA charges; now P-F46.
  - Ch 35 (u08:240): P-F37 is PLCR; now P-F41.
  - Ch 40 (u09:772, 807, 808): P-F38 is the convergence log; now P-F43.
  - Ch 41 (u09:983, 1018): P-F39 is the revenue build, now P-F44; P-F40 is VAT, now P-F37.
  - Ch 42 (u09:1191, 1935): P-F41 is the financial statements; now P-F45.
  - Ch 43 (u09:1396, 1432): P-F37 is the Monte Carlo; now P-F42.
  - Ch 55 (u11:1360): P-F37 is the funds flow; now P-F49.
  - Ch 56 (u11:1740): P-F38 is the swap charge; now P-F50.
  - Ch 60 (u12:1427, 1631): P-F37 is the PRI premium; now P-F51.
  - Ch 66 (u14:215): P-F41 is the ECL and hedge reserve; now P-F53.
  - Ch 67: u14's P-F38 is the UK top-up tax, now P-F54. Confirmed P-F38 is thin capitalization, which Ch 67 also uses.
  - Ch 68 (u14:897, 999): P-F40 is Castellan's capital; now P-F55.
  - Ch 75 (u15:1876): P-F37 and P-F38 become P-F59 and P-F46.
  - Ch 85 (u17:208, 215): P-F37 is the bid screen; now P-F60.
  - Ch 86 (u17:541, 548): P-F38 is the RAROC box; now P-F55.
- Required fix:
  - Add a binding "Provisional ID concordance" table to Annex P §8, with one row per brief, chapter, provisional ID and final ID. Use the list above, plus u06's P-F37 to P-F48 and u05's P-F39 to P-F47.
  - Edit every listed brief line to the final ID. Annex P §8.2 already says briefs keep their provisional IDs, so editing the briefs is the only safe course.
  - Change the registry caption of `exh:55.10` to "Case P closing-day funds flow (P-F49)".
  - Add P-F37 to P-F63 (and the P-F11a/P-F11b split) to Case Bible Part 7, so that the register writers are told to use (D-111) is complete.

---

## Major

### 2. Clean spark spread is homed in Ch 69, against R-024 and R-116

- Location: `glossary-canon.md` line 239 ("clean spark spread … ssec:69.3.3"); u15-glossary line 12.
- Defect: R-024 gives Ch 11 (ssec:11.10.5) the spark, clean spark and dark spreads, and R-116 makes eq:11.7 "Clean spark spread" the home equation. The canon instead homes the term in "Merchant energy and scarcity pricing" (ssec:69.3.3). Ch 11 would then use an unbolded term defined 58 chapters later. The R-024 brief-change list deleted "spark spread" and "dark spread" from u15 but missed "clean spark spread".
- Required fix: Set the canon home of "clean spark spread" to ssec:11.10.5, and add the note "Ruling R-024; Ch 69 applies via eq:69.2". Delete the u15 glossary row. Add "clean spark spread" to the R-024 "Brief text that must change" list.

### 3. Probability of default and loss given default are homed in Ch 68, against R-041

- Location: `glossary-canon.md` lines 982 and 1287 (ssec:68.2.2); u14-glossary lines 61 and 62.
- Defect: R-041 makes Ch 38 (ssec:38.1.1) the home of PD and LGD as pricing inputs, and gives Ch 68 only the regulatory parameters. Ch 29 (Example 29.1, u07:149), Ch 15 (expected-loss definition) and Ch 38 all use PD and LGD before Ch 68.
- Required fix: Rehome both canon entries to ssec:38.1.1 with the note "Ruling R-041; Ch 68 (sec:68.2) owns regulatory PD, LGD and EAD and input floors". Add "regulatory PD and LGD" as a separate Ch 68 entry if the canon needs it. Delete PD and LGD from u14-glossary.

### 4. "Ten-year P90" is homed in Ch 45, although Ch 9 teaches it and Ch 35 relies on it

- Location: `glossary-canon.md` line 1650 (ssec:45.2.1); u09-glossary line 89.
- Defect:
  - `architecture.md` row 9 and the u02 Ch 9 brief (ssec:9.6.2 "Computing one-year and ten-year P90", Example 9.7) teach it in Ch 9.
  - The canon's own "banking case" entry (ssec:35.6.1) defines the banking case with "ten-year P90".
  - The term also duplicates "ten-year P-value" (ssec:9.6.1).
- Required fix: Rehome "ten-year P90" to ssec:9.6.2. Note in the entry that Ch 45 (ssec:45.2.1) models it. Delete it from u09-glossary.

### 5. Breakeven has four homes

- Location:
  - `glossary-canon.md` lines 175 ("break-even case", ssec:35.6.3), 178 ("breakeven", ssec:43.4.3) and 179 ("breakeven analysis", ssec:30.5.3 "Rating a project in operation");
  - u02 Ch 9 concepts item 9 (u02:1168, "breakeven analysis as a concept");
  - R-080.
- Defect: R-080 makes Ch 35 (sec:35.6) the home of the concept, Ch 43 the home of the Case P computation, and Ch 85 the home of screening breakevens. The canon instead spreads three near-synonyms over Ch 30, 35 and 43, and the Ch 9 brief also claims "breakeven analysis as a concept". A writer of Ch 30 or Ch 9 would bold and define the concept before Ch 35.
- Required fix:
  - Keep one concept entry, "break-even case" (ssec:35.6.3), and record "breakeven" as its synonym there.
  - Delete "breakeven analysis" (ssec:30.5.3). Ch 30 cites ssec:35.6.3 by forward reference.
  - Re-scope the "breakeven" entry at ssec:43.4.3 as "breakeven (model computation)", or delete it.
  - In u02 Ch 9 item 9, replace "breakeven analysis as a concept" with a one-sentence forward reference to sec:35.6.

### 6. "Sizing case" and "test case" are homed in Ch 43 but used in Ch 36 and Ch 37

- Location: `glossary-canon.md` lines 1536 and 1659 (ssec:43.3.1).
- Defect: The canon's own definitions of "sculpting" and "target DSCR" (home ssec:36.2.1) are written in terms of "the sizing case". Ch 37 has a locked subsection titled "Setting the lock-up level with the sizing case" (ssec:37.4.2, u08:780), and u08 Ch 36 uses the term in its walkthrough and checklist (u08:577, 604). No forward reference to Ch 43 exists.
- Required fix: Rehome "sizing case" to ssec:36.1.1, or to ssec:35.6.1 next to base and banking cases. Record the move in a new ruling (R-122). Ch 43 keeps "test case" and the mechanics of running both cases in the model.

### 7. Gearing is used throughout Ch 1 to Ch 8 but homed in Ch 35, and Ch 8 has no forward reference

- Location:
  - `glossary-canon.md` line 715 (ssec:35.5.1);
  - u02 Ch 8 concepts (u02:905 to 931), examples 8.2 to 8.11, walkthrough sec:8.9 and the Case P installment (P-F05 "equity IRR at gearing…");
  - u01 Ch 2 installment (u01:127, "target gearing of 75%").
- Defect: Ch 8 teaches with gearing in every example and builds a "gearing-versus-return table", but it neither owns nor forward-references the term. Its forward reference points only to "why lenders cap gearing (Chapter 36)". The canon definition (senior debt over the total funding requirement, including financing costs and reserves) is also not what Ch 8 computes (debt over project cost).
- Required fix: Split the term into two senses:
  - "gearing (general)": debt over debt plus equity. Home ssec:8.2.1, defined in one sentence in the u02 Ch 8 brief.
  - "gearing (project finance measurement)": keep ssec:35.5.1 and point it to ssec:8.2.1.

  Then add a one-sentence forward reference to sec:35.5 in the u02 Ch 8 forward-reference line. In the u01 Ch 2 installment, add a forward reference to ssec:8.2.1 where "target gearing of 75%" appears.

### 8. Core deal terms have no early home: PPA, EPC contract, term sheet and letter of credit

- Location: `glossary-canon.md` line 1259 ("power purchase agreement", sec:18.1) and line 1578 ("standby letter of credit", ssec:59.5.1). There are no entries for "EPC contract" (engineering, procurement and construction contract), "term sheet" or "letter of credit".
- Defect: Standards Section 8 requires every term to be defined at first use, and Phase 1 item 3 requires a home for every term.
  - PPA is used substantively in Ch 2, 3, 4, 5, 7, 10, 11 and 14 to 17. Ch 10's whole running-case installment is a draft PPA.
  - The EPC contract is used from Ch 2 (the fit test, question 3) and Ch 4 (Example 4.3).
  - Ch 6's installment is "Castellan's indicative term sheet".
  - The SEKA LC appears in Ch 16 and Ch 18, and DSRA and equity LCs appear in Ch 37 and Ch 32, all long before the Ch 59 home of the LC concept.
- Required fix: Add a ruling, modeled on R-063, that gives these basic definitions early homes:
  - "power purchase agreement" at ssec:2.3.1, next to offtaker. Ch 18 keeps the full contract and records the home in its notes.
  - "engineering, procurement and construction contract (EPC contract)" at ssec:2.3.1 or ssec:4.6.1. Ch 22 owns the full contract.
  - "term sheet" at ssec:4.10.3. Ch 51 owns the document set and Ch 56 the negotiation.
  - "letter of credit" as a generic instrument at ssec:16.4.x, or at ssec:10.3.1 next to guarantees and indemnities. Ch 59 keeps "standby letter of credit" as payment security.

  Add the four canon rows and edit the u01 and u04 briefs' concepts-owned lists to match.

### 9. VAT during construction is taught in both Ch 41 and Ch 67, with no ruling, and "input VAT" is homed after its first use

- Location:
  - u09 Ch 41 sec:41.7 "VAT during construction" (Example 41.9, the refund-lag cost);
  - u14 Ch 67 sec:67.7 "VAT and indirect taxes during construction" (ssec:67.7.2 "The cost of the refund lag", Example 67.7);
  - `glossary-canon.md` lines 850 ("input VAT", ssec:67.7.1), 1738 ("VAT facility", ssec:31.5.1) and 1739 ("VAT refund lag", sec:41.7).
- Defect: Two chapters each compute the cost of the refund lag. The VAT refund lag, homed in Ch 41, is defined with "input VAT", which is homed 26 chapters later. Ch 31's VAT facility also depends on VAT basics, and "value-added tax" itself has no entry. No ruling divides the topic, as R-020 does for thin capitalization.
- Required fix: Issue a ruling that splits the topic:
  - Ch 31 (ssec:31.5.1) owns the VAT facility and gives a one-paragraph definition of VAT, input VAT and refunds, as the glossary home of "value-added tax" and "input VAT".
  - Ch 41 (sec:41.7) owns only the model rows (the refund schedule, the facility corkscrew and its interest) and drops the refund-lag cost teaching from Example 41.9.
  - Ch 67 (sec:67.7) owns the tax rules, the cost of the lag, refund risk as host-government credit risk and indirect taxes.

  Move "VAT refund lag" to ssec:67.7.2.

### 10. The waiver letter is drafted in two chapters, and "reservation of rights" is homed after its first teaching

- Location:
  - u11 Ch 51 ssec:51.7.3 "The waiver and amendment letter" ("Form, conditions, fees, reservation of rights");
  - u13 Ch 62 ssec:62.7.4 "The waiver letter" (Clause 62.1 with variants 62.2a and 62.2b);
  - `glossary-canon.md` lines 1400 ("reservation of rights", ssec:62.7.4) and 1751.
- Defect: R-092 gives Ch 51 the waiver and amendment letter, and Ch 62 only "running waivers in operations". Ch 62 still owns a full drafted letter with variants, and the canon homes "reservation of rights" in Ch 62. Ch 51 teaches it first, and the canon's own definition of "waiver and amendment letter" uses it.
- Required fix:
  - Rehome "reservation of rights" to ssec:51.7.3.
  - Retitle ssec:62.7.4 "Applying the waiver letter to the Case P breach". Its content becomes the Case P letter's operative terms, citing the form in ssec:51.7.3.
  - Move Clause 62.1 and its variants to Ch 51 as Clause 51.x, or recast them as an annotated Case P application that cites the form clause.
  - Add both points to R-092's "Brief text that must change".

### 11. Commitment fees are still taught in Ch 38, against R-003

- Location: u08 Ch 38 ssec:38.3.2 "Commitment fees" with Example 38.4 (u08:1091); u08 glossary row "commitment fee" at 38.3.2 (u08:1312); `anchor-registry.md` ssec:38.3.2.
- Defect: R-003 makes ssec:6.1.2 the home of upfront and commitment fee mechanics. Its brief-change list deletes only the u08 glossary row, so the Ch 38 subsection and its worked example still re-teach the mechanics.
- Required fix:
  - Retitle ssec:38.3.2 "Commitment fee levels and conventions": market levels, the percentage-of-margin convention and the Port Arthur anchors.
  - Replace Example 38.4's computation with a citation of ssec:6.1.2, or re-scope it to "commitment fees in the all-in cost".
  - Extend R-003's change list to cover these edits.

### 12. Cash yield and money multiple are taught in Ch 43 before their Ch 46 home, and Ch 1 points to the wrong home

- Location: u09 Ch 43 concepts ("payback, multiple, cash yield", owned) and ssec:43.2.4 "Payback, multiple and cash yield … what each hides"; `glossary-canon.md` lines 229 and 1076 (ssec:46.1.3 and ssec:46.1.4); u01 Ch 1 assumed table (u01:259, "money multiple | Ch 5").
- Defect:
  - R-013 makes Ch 46 the owner of cash yield, the money multiple and their investment use.
  - Ch 43 owns them in its concepts list and teaches "what each hides" with no forward reference. Its assumed list forward-references Ch 46 only for "valuation interpretation of IRR and NPV".
  - Ch 1 tells the reader that the money multiple is taught in Ch 5, which does not teach it.
- Required fix:
  - Remove "multiple, cash yield" from the Ch 43 concepts-owned list.
  - Retitle ssec:43.2.4 "Payback, multiple and cash yield rows". Its content becomes formulas only, with a one-sentence forward reference to ssec:46.1.3 and ssec:46.1.4.
  - Change u01:259 to "Ch 5 (IRR, present value); Ch 46 (money multiple)".

### 13. Price decks are taught in Ch 45 before their Ch 75 home, and R-103 does not mention Ch 45

- Location: u09 Ch 45 ssec:45.7.3 "Price decks" (u09:1747: base, low and high decks; real against nominal; who supplies them) and its concepts list (u09:1701); R-103; `glossary-canon.md` line 127 ("bank price deck", ssec:75.3.2).
- Defect: Ch 45 teaches what a price deck is and who sets it 30 chapters before the home. Its brief carries no forward reference, and R-103's list of citing chapters (Ch 77 and Ch 78) omits Ch 45.
- Required fix: Retitle ssec:45.7.3 "Price-deck rows in the model": the deck as a supplied input, real-to-nominal conversion and labeling. Add a one-sentence forward reference to ssec:75.3.2 and add Ch 45 to R-103's "Other chapters".

### 14. Ch 46 still defines equity IRR and project IRR, against R-013

- Location: u10 Ch 46 concepts table (u10:48 and 49, owned at 46.1.1); ssec:46.1.1 "Project IRR and equity IRR. Defines both … states the inclusion rules" (u10:98); u10-glossary rows 7 and 8.
- Defect: R-013 puts the definitions and the shareholder-loan inclusion rule in ssec:8.2.1 and leaves Ch 46 only the conventions. Its change list covers the glossaries, the Ch 8 brief and eq:46.1, but not ssec:46.1.1 or the concepts table. A Ch 46 writer following the brief would re-define both measures.
- Required fix:
  - Retitle ssec:46.1.1 "Project IRR and equity IRR as investment measures".
  - Replace "Defines both … states the inclusion rules" with "Applies the definitions of ssec:8.2.1 to Example 46.1".
  - Change the u10 concepts rows from "owned" to "applied (home ssec:8.2.1)".
  - Add these edits to R-013.

### 15. Ch 13's running case builds the Case P timeline, which R-017 gives to Ch 39

- Location: Case Bible Part 6 row 13 ("A practice workbook with Case P timing flags: monthly construction, semiannual operations, the EPC payment profile"); u03 Ch 13 installment (u03:1273 to 1277, building "the semiannual operations timeline starting with the first period ending June 30, 2021").
- Defect: R-017 makes Ch 39 the owner of "the Case P timeline design, the monthly-to-semiannual switch, the full project flag set". Ch 13's installment builds exactly that, so Ch 39's installment repeats it.
- Required fix:
  - Rewrite Part 6 row 13 as "A practice workbook with Case P's monthly construction flags and the EPC payment profile; the switch to semiannual operating periods is previewed in one sentence (Chapter 39)".
  - Edit u03:1277 to drop the semiannual timeline and the operations flag check. Keep the 33 construction flags, the profile check and the SUMPRODUCT.

### 16. The Case Bible gives hedge valuation to Ch 46, against R-006

- Location: `case-bible.md` Part 6 concept-ownership notes, line 1143 ("Chapter 20 introduces R1's fixed-volume swap … the valuation of the hedges belongs to Chapter 46").
- Defect: R-006 gives swap valuation to ssec:6.8.3, commodity hedge close-out to Ch 20 at principle level, and allows Ch 46 to value hedges only inside the risk-bucket valuation. R-006's change list fixed u05 item 16 but not this Case Bible note, which writers of Ch 20 and Ch 46 both read.
- Required fix: Replace line 1143's second clause with "valuation method: ssec:6.8.3; close-out at principle level: Ch 20; hedge value inside the A1 risk-bucket valuation: ssec:46.4.2".

### 17. Case R's superseded A1 value is still in two briefs

- Location: u10 Ch 46 installment (u10:262 and 263, "enterprise value against the USD 1,184.6 million price"; "A1 enterprise value USD 1,184.6 million"); u17 Ch 85 installment (u17:213).
- Defect: Change-log row R-C04 (2021-12-09) and D-014 reset the A1 price to USD 446.3 million. Both briefs still state the v1.0 value as a Case Bible input.
- Required fix: Change both briefs to "USD 446.3 million (Case Bible 3.6 as amended by R-C04; locked-box structure per Annex TR R.1)". Correct the Case Bible 3.6 table entry if it still shows 1,184.6.

### 18. The SEKA letter of credit amount is inconsistent: USD 33.8 million in the Case Bible against USD 36.2 million in the ledger and D-017

- Location:
  - `case-bible.md` line 153 (1.4) and line 341 (timeline: 2023-02-14 "SEKA LC drawn (USD 33.8 million)");
  - Part 6 row 16;
  - Annex P §2.2 row 16 and §3.13;
  - `model/figure-ledger-case-p.md` lines 751 and 752 (P-F39: 2022 reset USD 36.2 million, 2023 reset USD 36.6 million);
  - `model/case_p_report.md` line 120;
  - D-017 (second entry, "LC model value 36.2m wins");
  - briefs u04:1149 (Ch 16), u07:1633 (Ch 34), u12:1052 (Ch 59), u17:534 (Ch 86).
- Defect: The decision log and ledger adopted the model value, but the Case Bible text and four briefs still print USD 33.8 million. In February 2023 the drawable LC would be the January 2023 reset of USD 36.6 million, which neither number matches. Annex P §3.1's arrears "net of the LC drawing" (USD 146.4 million gross less USD 112.6 million net, a difference of USD 33.8 million) uses the old figure.
- Required fix:
  - Amend Case Bible 1.4 and 1.8 and Part 6 row 16, plus Annex P §2.2 and §3.13, to "the amount under the annex 1.1.5 formula (P-F39)", and state which reset applies to the February 14, 2023 drawing.
  - Rerun P-F20 and Annex P §3.1's arrears on that drawing.
  - Replace "USD 33.8 million" in the four brief lines with "P-F39 (reset value at the date shown)".
  - Log the change as P-C43.

### 19. Ledger v1.1 contradicts the Case Bible's overrun funding, and a figure ID that D-017 relies on does not exist

- Location:
  - `case-bible.md` §1.9: overrun funding "then the standby facility and contingent equity 75:25 … expected drawing USD 5 million to USD 15 million";
  - P-C08;
  - `model/figure-ledger-case-p.md` lines 478 and 479 (P-F18: standby drawn 0.00, contingent equity drawn 0.00);
  - D-017 (second entry, v1.2 recalibration and "bid-to-close IRR bridge (P-F64)");
  - the ledger and Annex P §8, which stop at P-F63;
  - u07 Ch 31 coda (u07:809, "Forward reference Chapter 61 for how the standby was drawn");
  - u02 Ch 8 installment (u02:1028: "the committee wants 80% to protect the 16.0% bid target") against P-F05 (13.4% at 75% and 13.9% at 80%).
- Defect:
  - The released ledger contradicts the story in Ch 31, 32 and 61, which says the standby and contingent equity were drawn.
  - D-017 cites P-F64, which is in no register.
  - The Ch 8 scene's premise cannot be shown with P-F05, because no gearing up to 80% reaches 16.0%. Annex P §2.2 row 8 also changes the scene's characters (Kunal Mehrotra and Devesh Raval), which the brief does not reflect.
- Required fix:
  - Release ledger v1.2 before drafting Parts V and XIV.
  - Register P-F64 (the bid-to-close equity IRR bridge, used by Chapters 8 and 47) in Annex P §8.2 and the ledger.
  - Rewrite u02:1028 as "the committee sees that even 80% gearing leaves the FC base equity IRR below the 16.0% bid target (P-F05; bridge P-F64); the argument is over how much downside to accept for 0.5 points", and name the Annex P characters.

### 20. RORAC survives in the Case Bible annex, model and ledger, against R-075

- Location: `case-bible-annex-p.md` §2.5 ("Castellan's regulatory and RORAC inputs") and §8.2 P-F55 ("… RORAC"); `model/figure-ledger-case-p.md` (2 occurrences); `model/case_p.py` (5 occurrences); `bible/case-p-input-requests.md` (2 occurrences); u17 (14 occurrences, including eq:86.1 and the formula-sheet list at u17:1581).
- Defect: R-075 and D-024 make RAROC the canonical term ("RORAC is not used"), but the binding Case Bible and the ledger label that writers print still say RORAC.
- Required fix: Replace RORAC with RAROC in Annex P §2.5 and P-F55, in the ledger labels and model output keys (`case_p.py`, `ledger_p.py`), in the input-requests file and in u17. Restate eq:86.1 as an application of eq:29.1.

### 21. Anchor registry: clause-variant labels are missing or corrupted

- Location: `anchor-registry.md` chapter tables.
- Defect: Section 1 rule 4 and A10 say variants and ranges were expanded. In practice:
  - These briefs declare variants (or a1 to c ranges) that are absent from the registry: cl:10.4a to 10.4c, cl:15.1a to 15.1c, cl:23.2a to 23.2c, cl:24.1a to 24.1c, cl:27.1a to 27.1c, cl:28.1a to 28.1c, cl:35.2a and cl:35.2b, cl:51.3a to 51.3c, cl:67.1a to 67.1c, cl:68.1a and cl:68.1b, cl:69.1a to 69.1c, cl:70.1a to 70.1c, cl:71.1a to 71.1c, cl:72.1a to 72.1c, cl:73.1a to 73.1c, cl:74.1a to 74.1c, cl:75.1a and cl:75.1b, cl:76.1a to 76.1c and cl:84.1a to 84.1c.
  - The style sheet's own example labels cl:18.3a to cl:18.3c are absent too.
  - Several captions are parse debris:
    - `cl:35.2` "with" and `cl:35.2c` "if required) CFADS definition variants";
    - `cl:25.1a` "buyer-friendly" and `cl:25.1c` "seller-friendly) Take-or-pay and make-up, gas sale agreement";
    - `cl:26.1a` to `cl:26.1c`;
    - the variants of `cl:78.1`, `cl:79.1`, `cl:80.1`, `cl:81.2` and `cl:83.1`, whose captions embed other labels ("sponsor-friendly, cl:78.1b lender-friendly, …").
  - The A14 uniqueness claim cannot be relied on for clauses.
- Required fix:
  - Regenerate every clause block from the briefs, giving each variant the caption "<parent caption> (Illustrative, <party>-friendly)".
  - Add the missing variant rows listed above.
  - For cl:35.2, list only cl:35.2a and cl:35.2b, as the brief decides (u08:122).
  - Update the Section 1 totals.

### 22. Anchor registry: chapter titles were not updated for R-113 and D-028

- Location: `anchor-registry.md` `### Chapter N:` headings and the `ch:N` captions for Chapters 8, 12, 15, 17, 19, 20, 23, 25, 31, 34, 37, 39, 41 to 43, 47 to 49, 52, 54, 59, 63 to 65, 73 and 75 to 83.
- Defect: The registry, which writers cite by `\cref{ch:N}`, still carries the pre-ruling titles:
  - Ch 25 "Inputs and access: fuel, water, grid, land and permits";
  - Ch 88 "The frontier: evaluating new structures", a colon-and-subtitle form that standards Section 8 bans;
  - Ch 79 "Toll roads, bridges and tunnels (Case T ramp-up)";
  - Ch 75 "… (incl. reserve-based lending)";
  - Ch 77 "… (gigafactory) finance";
  - Ch 83 "Hydrogen and derivatives, …";
  - Ch 23 "… single EPC";
  - no serial commas.
- Required fix: Replace every `ch:N` caption and chapter heading with the `architecture.md` title verbatim. A script diff of the two files should then show no differences.

### 23. R-084 was not applied to the registry or to u13: "SPA" still means the share purchase agreement

- Location: `anchor-registry.md` ssec:47.3.3 "The sale and purchase agreement", sec:47.7 "Walkthrough: a locked-box SPA, clause by clause" and exh:47.5 "SPA terms…"; u10:441, 459, 516, 536, 595, 614 and 792 (glossary "sale and purchase agreement | SPA | … transfers shares"); u13 Ch 63 (u13:861, 1001 "SPA April 14, 2026").
- Defect: R-084 reserves SPA for the commodity contract (sec:21.2) and requires the acquisition contract to be "share purchase agreement", never abbreviated. Its change list names only u10, so u13 and the registry labels writers must cite were not corrected.
- Required fix:
  - Retitle ssec:47.3.3 "The share purchase agreement".
  - Retitle sec:47.7 "Walkthrough: a locked-box share purchase agreement, clause by clause".
  - Recaption exh:47.5 "Share purchase agreement terms: seller, buyer and market positions".
  - Make the same replacements in the u10 and u13 brief lines listed, and add u13 to R-084.

### 24. Ruling-mandated brief text is still unchanged, with no per-chapter errata for writers

- Location: briefs u01 to u17 (the briefs were not rewritten, by D-015).
- Defect: Writers work section by section from the brief. D-015 relies on them cross-reading 121 rulings, but many mandated changes are still in the briefs, and several rulings' change lists are incomplete (Defects 2, 10 to 14, 16 and 23). Verified unapplied text:
  - R-001: eq:47.1 "Levelized tariff" (u10:500, 564, 770) and the u10 glossary row (u10:784).
  - R-002: eq:88.2 LCOH derivation (u17:1153, 1285, 1581).
  - R-007: ssec:6.8.2 "The swap rate and the credit and execution charge" (u02:432).
  - R-006: u05:968.
  - R-014: ssec:65.5.2 "Terminal value conventions" (u13:1668, 1826) and u10:88, which forward-references terminal value to Ch 65.
  - R-016: three IFRIC 12 passages in Ch 7, not one: concepts item 9 (u02:649), ssec:7.7.2 (u02:698) and ssec:7.11.2's "one-paragraph forward reference" (u02:715).
  - R-030: no subrogation in u03 ssec:10.3.1.
  - R-042: no NOAK in u04 ssec:14.5.1.
  - R-046: no forward references to ssec:58.2.1 and ssec:58.2.4 in u05 Ch 17 or u10 Ch 47.
  - R-053: no competing-facility paragraph in u05 ssec:17.2.1.
  - R-073: u07 Ch 32 item 15 is still a full OBBBA treatment (u07:973).
  - R-115: "Exhibit 86.2a" and the old Ch 86 exhibit numbers (u17:429 to 546).
  - R-118: fw:integrity-check and "integrity check" (u17:781, 864, 931, 989, 1000), plus u17:114, which points Ch 85 to "Chapter 87's integrity check" (not in R-118's list).
- Required fix: Either edit the briefs in place, or, at minimum, add a block headed "Rulings that change this brief" at the top of each chapter brief. Each block lists every ruling that touches the chapter, with the exact replacement text, and the brief-change lists of R-001, R-003, R-006, R-013, R-016, R-084 and R-118 are extended as stated in this report. The pilot (Phase 2) should not start until this errata layer exists.

### 25. Ch 6 shows 2018 margins in a 2016 scene and repeats the 2017 hedge-ratio fight

- Location: u02 Ch 6 installment (u02:496, 498, 499); u11 Ch 56 installment (u11:1585, "September 2017 … the hedge ratio. Pieter insists on an 80% hedge priced by his own bank"); Annex P §1.15.2 and §4.7; ledger P-F03.
- Defect:
  - The July 2016 narration gives "the margin grid by tranche from Case Bible Section 1.6 inputs (ECA-covered 1.35%; … commercial 4.10%…)", which are the financial-close terms. The same exhibit shows P-F03, whose July 2016 indicative margins differ (ECA 1.50%, A 3.90%, B 3.75% and commercial 4.50%), so one chapter contains two contradictory 2016 grids.
  - The Ch 6 scene also has Pieter "insist on an 80% hedge priced by Castellan" in July 2016, and Ch 56 stages the same insistence as a new fight in September 2017. Story order is contradictory, and Castellan was not mandated until June 19, 2017.
- Required fix:
  - Change u02:498 so that the margin grid comes only from P-F03 and Annex P §4.7. Mention the 2018 margins only in Scene 2 (November 2022), as the margins in force.
  - Change u02:496 so that Pieter floats a hedging requirement "for the term sheet" without the 80% figure or Castellan pricing, and leave the 80% and execution-charge fight to Ch 56.

### 26. Ch 12 points take-or-pay to the wrong home and pre-stages the Ch 25 negotiation

- Location: u03 Ch 12 installment (u03:942: "Félix wants a take-or-pay strong enough for Halbeck to finance the field … Contract terms (take-or-pay, make-up, deliver-or-pay) are named but taught in Chapter 25"); u06 Ch 25 installment (u06:647, the same motive as the scene's core).
- Defect: Ch 12's brief names Ch 25 as the home of take-or-pay, but R-047 makes it ssec:18.4.1. Ch 12, 21 and 25 all set a Félix–Tomasz scene in November 2017. Ch 12's scene uses the take-or-pay motive 13 chapters before the concept's home and gives away the Ch 25 negotiation.
- Required fix:
  - In u03:942, change "taught in Chapter 25" to "principle in Chapter 18 (ssec:18.4.1), fuel-side mechanics in Chapter 25".
  - Replace Félix's take-or-pay ask in Ch 12 with a physical question, for example the offshore section's outage history or the field's plateau.

---

## Minor

### 27. "Default" is homed in the wrong subsection

- Location: `glossary-canon.md` line 454 (ssec:51.4.5 "Distributions and restricted payments as drafted").
- Defect: R-081 places "Default" with "event of default" in sec:51.5.
- Required fix: Set the home to ssec:51.5.1.

### 28. Two terms named by rulings are missing from the canon

- Location: `glossary-canon.md`.
- Defect: "hybrid till" (R-055: Ch 80, ssec:80.2.2) and "financial advisor" (R-066: Ch 4, sec:4.8) have no entries.
- Required fix: Add both entries with those homes.

### 29. MMBtu is homed after its first use

- Location: `glossary-canon.md` line 1041 ("million British thermal units", ssec:12.1.3).
- Defect: Ch 10 (Example 10.7) and Ch 11 (ssec:11.2.1, Example 11.2) use MMBtu first.
- Required fix: Rehome the term to ssec:11.2.1.

### 30. "Overbuild" has only its fiber sense

- Location: `glossary-canon.md` line 1181 ("overbuild", ssec:82.3.2, the fiber sense).
- Defect: The storage sense that R-023 gives Ch 73 (ssec:73.2.2) has no entry, and Annex TR R-C13 uses "battery overbuild".
- Required fix: Split the term into "overbuild (networks)" at ssec:82.3.2 and "overbuild (storage)" at ssec:73.2.2, and list it under R-083.

### 31. The FPSO entry's note cites the modeling section

- Location: `glossary-canon.md` line 678, note "Ch 76 (sec:76.9) owns FPSO financing".
- Defect: sec:76.9 is "Modeling LNG and floating assets". FPSO financing is in sec:76.8.
- Required fix: Correct the note to sec:76.8.

### 32. The canon miscounts its entries

- Location: `glossary-canon.md` header ("Entries: 1772") and D-030.
- Defect: The table has 1,771 rows.
- Required fix: Correct the count, or restore the missing row.

### 33. Registry captions for implied exhibits are parse fragments, and matter labels are missing

- Location: `anchor-registry.md`.
- Defect:
  - The captions of exh:2.3 ("if it teaches"), exh:5.3, exh:6.3, exh:6.5, exh:7.1, exh:7.4, exh:8.1, exh:9.1, exh:9.2, exh:9.6, exh:9.7 and exh:90.1 ("compiled and checked mechanically in Phase 7") are fragments.
  - exh:89.1 to exh:89.3 say "caption not stated", although u17:1461 gives Capability map, Data room index and Assessment rubric.
  - The reserved sec:89.1 to sec:89.29 and the sec:90.x labels (u17:1461, 1537) are absent.
  - ch:92, ch:93 and ch:94 are absent, although R-039 and R-107 rely on Chapter 93 and on the chapter scheme for files 89 to 94.
- Required fix: Recaption these labels from the briefs, and add the missing matter labels.

### 34. Duplicate headings that rulings did not retitle

- Location: `anchor-registry.md`.
- Defect: These headings duplicate a home heading:
  - ssec:9.8.3 and sec:43.5 are both "Monte Carlo simulation".
  - ssec:37.5.3 and ssec:51.5.4 are both "Equity cures".
  - ssec:22.6.2 and ssec:52.1.2 are both "The security package".
  - ssec:79.4.1 "Minimum revenue guarantees and revenue-sharing bands" repeats the instruments whose home R-052 places in ssec:57.5.1 and ssec:58.1.3.
- Required fix: Retitle the later headings:
  - sec:43.5 to "Implementing Monte Carlo in the model";
  - ssec:51.5.4 to "Drafting the equity cure";
  - ssec:22.6.2 to "Contractor security: bonds, guarantees and retention";
  - ssec:79.4.1 to "Calibrating guarantees and revenue-sharing bands for toll roads".

### 35. The decisions log has ID collisions and an outdated ledger path

- Location: `decisions.md`.
- Defect: D-016 and D-017 each appear twice: Case R v1.2 and the architecture home rule, then foundation homes and Case P v1.1. D-111 and Case Bible Part 7 name `model/figure-ledger.md`, but the ledger exists as three files, `figure-ledger-case-{p,t,r}.md`.
- Required fix: Renumber the second D-016 and D-017 to the next free IDs, and update D-111 and Case Bible Part 7 to the real paths.

### 36. Ch 8 mislabels P-F05 and risks printing DSCR

- Location: u02:1029.
- Defect: The brief calls P-F05 "debt on the sculpted profile", but the ledger labels it "debt set at gearing", and sculpting is not taught until Ch 36. P-F05's ledger lines also include minimum DSCR, which Ch 8 must not print (Case Bible Part 6 note).
- Required fix: Replace the description with "senior debt set at each gearing (P-F05, equity IRR and debt lines only)".

### 37. R-087 states two owners for the model-audit engagement

- Location: R-087 "Other chapters" ("Ch 44 and Ch 49 own the model-audit engagement").
- Defect: The ruling names two owners, contrary to its own rule.
- Required fix: Restate it as "Ch 44 owns the audit process and findings; Ch 49 (sec:49.3) owns the engagement: scope, materiality application and sign-off".

### 38. Case Bible Part 6 and Part 7 have not absorbed the annexes

- Location: `case-bible.md` Part 6 rows and Part 7 figure register.
- Defect: Neither part includes Annex P §2.2 or Annex TR T.16 amendments, the P-F11a/P-F11b split, or the new users of P-F16 and other figures. Writers read the main table first.
- Required fix: Merge the annex row amendments into Part 6 and Part 7, and mark each merged cell "(Annex P)" or "(Annex TR)".

### 39. Two Case T story dates disagree

- Location: Annex TR T.16; `case-bible.md` Part 6 row 79; T-C02.
- Defect:
  - T.16 says Callum appears in Chapter 79 at "story date 2021", but Part 6 row 79 gives 2019 to 2025.
  - T-C02 logs the May 6, 2019 opening as learned in Chapter 79, although Ch 45 (2019 actuals) and Ch 64 (2019 to 2023 distress) reveal it first.
- Required fix: Align the story dates, and set T-C02's chapter to 45.

### 40. Castellan's credit approval precedes the model audit, which is not one of its conditions

- Location: Annex P §2.5 (credit committee May 22, 2018); Part 6 row 44 (model audit June 2018); Annex P §4.1 (IE report May 30, 2018); u17:542 (conditions of approval).
- Defect: The committee approves before the model audit, but the conditions list the final IE report and not the model audit.
- Required fix: Add "satisfactory model audit report (Ferrand Model Assurance)" to u17:542 and to Annex P §2.5.

### 41. The completion long-stop date is defined with a merged term

- Location: `glossary-canon.md` line 287 ("completion long-stop date").
- Defect: The definition uses "lenders' completion", which R-050 merged into "financial completion".
- Required fix: Reword the definition to use "financial completion".
