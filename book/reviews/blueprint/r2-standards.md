# Blueprint review round 2: standards lens (standards.md Sections 6 to 10)

Reviewer: standards lens, round 2 (fresh reviewer). Date: October 3, 2026.
Scope: the revised briefs `bible/briefs/u01.md` to `u17.md` (round 1 revisions), the regenerated `bible/anchor-registry.md` (consolidation A, 5,558 labels), `bible/architecture.md`, `bible/style-sheet.md` with Addendum A.9 to A.11, `bible/fact-sheet-plan.md`, `facts/`, and the three figure ledgers. I checked them against round 1 report `reviews/blueprint/standards.md`.

Method. Scripts and outputs are in the session scratchpad (`r2/`).
- **Headings.** I extracted all 3,572 `ch:`, `sec:` and `ssec:` captions from the registry. I parsed the locked TOC lines of all seventeen briefs: 3,049 labels in the generic formats, plus 301 u16 lines in u16's own format. Against the registry they show 0 wording differences, apart from reviser annotations such as "(retitled)" and one registry truncation (new defect 2).
- **Heading scan.** I re-ran the banned-pattern scan on every caption:
  - colon outside the four allowed prefixes;
  - every formula heading in standards Section 8;
  - question headings, dashes, "Why …", "… that matter";
  - "Key", production jargon, template repeats, pronoun or bare headings;
  - British spellings, combined-case prefixes, missing serial commas;
  - duplicates across chapters.
- **Chapter titles.** I checked all 88 against architecture.md.
- **Running-case figure IDs.** Every P-F, T-F and R-F ID cited in a brief body exists in a ledger.
- **Fact-sheet slugs.** I checked all 19 round 1 slugs against `facts/` and the plan.
- **Unlocated examples.** I scanned all 584 worked-example specifications for an unlocated setting.
- **Calculation exercises.** I scanned 216 calculation exercises for missing answers.
- **Recomputation.** I recomputed 33 worked examples and 20 exercise answers in Python. All were chosen from items the revision logs list as changed. The table is at the end.

## Verdict: PASS

All 19 round 1 defects are fixed or reduced to minor residue. The blocking heading defect is fixed: the scan finds no banned colon, formula, question, "Why" or combined-case heading. Every major defect is fixed. The numbers are accurate: 53 recomputed items match, and one exercise key differs by 0.001 in its third decimal. No blocking or major defect remains open.

New findings: 0 blocking, 0 major, 8 minor. Two round 1 minors remain partly fixed.

---

## Round 1 defects: status

| # | Round 1 defect (severity) | Status | Evidence (current location) |
|---|---|---|---|
| 1 | Banned TOC headings: colon-subtitle, formula, "Real case:", combined-case, dash (blocking) | FIXED | The scan finds 0 colon headings outside "Case P/T/R:" and "Walkthrough:", 0 formula headings and 0 combined-case prefixes. Registry rows confirm the fix: sec:8.8 "The same reactor at two costs of capital"; sec:64.12; ssec:22.8.3; ssec:35.5.2; ssec:66.6.1; sec:86.3 "The risk, mitigant, and residual table"; the splits at sec:68.11/ssec:68.11.1 to 68.11.2 and sec:84.12/ssec:84.12.1 to 84.12.3; sec:73.9 "Case R: battery tolls and floors"; registry Section 2 B6. The en dash in ssec:75.5.2 is left over (new defect 8). |
| 2 | Registry chapter titles contradict architecture.md and R-113 (major) | FIXED | All 88 `ch:` captions and "### Chapter N" headers equal the architecture.md Title column verbatim (scripted). Brief headers match. Registry Section 2 B12 records it. |
| 3 | Template headings in Ch 77 to 83; "Key risks", "Verified anchors" (major) | FIXED | No registry heading contains "contract set" (except sec:71.6 "The offshore wind contract set" and the walkthrough sec:54.7), "Typical financing terms", "Key risks", "Modeling specifics", "Indicative ranges" or "Verified anchors". For example, sec:79.6 is now "Concession deed, D&C contract, and tolling-system contract for a toll road", and ssec:77.8.1 is now "Financing terms at Sadara, Northvolt Ett, Duqm, and the DOE battery plants". Duplicates outside the sector chapters remain (new defect 3). |
| 4 | Most worked examples unlocated (major) | FIXED | The heuristic scan of 584 example specifications flags 89 with no place word. I checked every flag:<br>- Most continue a located example (Llano Pardo, Quebracho Alto, Cerro Albarda, Bjerregaard Vind, Sur Andino, Tsiskari, and so on).<br>- The rest are placeless arithmetic labeled as such under A.10 (Example 79.6 says "Setting: placeless arithmetic"; Examples 13.1 and 42.1).<br>- Sector examples in Ch 71 to 82 now name the market, the date and the parties: Ex 78.4 Cerro Albarda, Chile; Ex 80.2 Pennine Rail Leasing, England, 2025; Ex 81.2 East Java, 2025.<br>- One exception remains (new defect 5). |
| 5 | Style-sheet figure 412.6 reused; round principals (major) | FIXED | In brief bodies, "412.6" now appears only in notes that ban it, outside the revision logs. The replacements: Ex 17.4 396.8; Ex 36.10 403.7; Ex 61.3 438.7; Ex 78.4 403.7 Mt; Ex 80.2 GBP 438.9 million; Ex 81.2 398.3 million m3; Exercise 46.10 NZD 397.3 million. Round principals are made lumpy or labeled as round on purpose (Exercise 86.6 "USD 45.0 million (round, as a typical club ticket, and said so)"). The replacement figures now recur across units (new defect 4). |
| 6 | About 87 calculation exercises lack inputs or answers (major) | FIXED | No exercise body contains "given", "supplied" or "writer specifies" without numbers. Of 216 scripted calculation exercises, all carry answers. The 5 the script flagged carry their answers in parentheses or are template-build tasks. The flagged sets now give inputs and answers, for example Ch 21 (Exercises 21.6 to 21.10 and 21.16, u05), Ch 78 (78.5 to 78.8 and 78.10, u16) and Ch 61 (61.6 to 61.12, u13). |
| 7 | Target lengths too short in multi-sector chapters (major) | FIXED | u15 headers: Ch 70, 72, 73, 75 and 76 at 11,000 to 13,000 words, with unit rule 8 "floors, not caps". u16 headers: Ch 80 to 83 at 13,000 to 15,000 words, with the floor line. `tracker.md` has no per-chapter target table, so it needs no update. |
| 8 | 19 non-existent fact-sheet slugs (major) | FIXED | No brief body cites a missing slug as a source. Each one is either mapped to its delivered sheet in the text or listed as "fact sheet requested" with a teach-without instruction:<br>- delivered under another name: u09 l.2304 and u07 l.1882;<br>- "fact sheet requested" with a teach-without instruction: u03 l.931 and 1538, u05 l.529 and 2022, u10 l.1590, u13 l.652, 907 and 1308.<br>`fact-sheet-plan.md` has the request-mapping and open-request tables. |
| 9 | Clause variants missing in Ch 32, 37, 38, 47, 52 and 63 (major) | FIXED | Registry groups: cl:32.2a to c; cl:37.2a and b; cl:37.3a to c; cl:38.2a to c; cl:47.1a to c; cl:52.3a and b; cl:63.1a to c. Each has a landing paragraph in its brief (for example u08 ssec:37.3.1 and ssec:37.4.3). Caption debris on cl:47.1 is new defect 2. |
| 10 | Exercise 35.14 key wrong (minor) | FIXED | u08 l.333: "1.31x (1.314); 1.33x (1.335); 1.39x (1.395)"; BI proceeds alone give 1.37x. Recomputed and correct. |
| 11 | 0.996x printed as 1.00x in Ex 35.4 (minor) | FIXED | u08 l.195 prints "0.996x, debt service not fully covered" and adds the display-rule sentence, which ssec:35.2.3 (l.108) repeats. |
| 12 | Clause-variant rows missing; debris rows cl:35.2 "with" and cl:35.2c (minor) | FIXED | Every variant group is registered (B3). cl:35.2 has a and b only. New debris is noted in new defect 2. |
| 13 | "Why", "…that matter" and pronoun or bare headings (minor) | FIXED | 0 headings begin with "Why". All five "…that matter" headings and all ten pronoun or bare headings are renamed (for example ssec:57.5.2 "Measuring contingent liabilities", ssec:35.4.1 "The PLCR defined", ssec:62.6.1 "The KPIs lenders test by asset type"). One instance the round 1 list missed is new defect 1. |
| 14 | British spellings (minor) | PARTLY FIXED | Fixed in headings (ssec:78.5.6, 43.7.1, 68.2.1, 68.3.1) and in u14's Basel terms, which now quote the source spelling once. Two residues remain:<br>- "programme" survives in five u13 lines (117, 283, 1638, 1781, 1823), although u13's revision log says it was "corrected throughout".<br>- "tonne" survives in u05, for example the glossary row at l.1618 "per dry metric tonne", against the canon's "dry metric ton". u05's log says "tonne → t". u16 and u09 also use "tonne(s)" in prose.<br>Fix: change "programme" to "program" (or "schedule") in the five u13 lines, and "metric tonne" to "metric ton" in u05 l.1432 and l.1618. Record in the style sheet whether "tonne" or "metric ton" is the house unit word; the canon uses "metric ton". |
| 15 | Serial comma missing in about 330 headings (minor) | PARTLY FIXED | Three headings still lack it:<br>- sec:17.9 "Case P: the tender, the implementation agreement and the guarantee" (u05 l.137 and l.275)<br>- sec:26.8 "Case P: the shareholders' agreement among Kilnworth, Talmé and the ABDB fund" (u06 l.857)<br>- ssec:25.7.3 "Linear rights for pipelines, lines and roads" (u06 l.606 and l.721)<br>Fix: insert the comma before "and" in the brief TOC lines and the anchor tables, and in the three registry rows. |
| 16 | Ch 86 has no walkthrough heading (minor) | FIXED | sec:86.8 "Walkthrough: Castellan's credit paper for Bélanou, May 2018"; sec:86.9 "Case P: reading the 2018 paper in 2026". Every chapter now has both a "Walkthrough:" heading and a "Case P/T/R:" heading (scripted). |
| 17 | Lake Turkana penalty mechanism against "Do not state" (minor) | FIXED | u06 l.663 and l.1390 use "reported at about EUR 127 million, part of it recovered from Kenyan consumers through a tariff surcharge". No lump-sum or six-year split remains. |
| 18 | Thin example density (minor) | FIXED | Registry example counts: Ch 28 has 5, Ch 74 has 5, Ch 30 has 6, Ch 54 has 6, Ch 52 has 5 and Ch 88 has 5. Each listed run now names its material: ssec:4.3.1 to 4.3.4 (u01 l.1144 to 1147), ssec:44.4.1 to 44.4.3 (u09 l.1890 to 1892), ssec:39.6.3 and 39.6.4, and ssec:61.7.1 to 61.7.3. |
| 19 | Inline `\xl{}` formulas containing "%" (minor) | FIXED | No `\xl{}` in any brief contains "%". The remaining "%" formulas are marked "excel block" (for example u04 l.1132 and l.1151, u02 Ex 9.5). Style sheet A.9 is in place. |

---

## New defects

### 1. Pronoun-only heading ssec:60.2.3
- Severity: minor
- Location: u12 l.1331 and l.1527; registry `ssec:60.2.3`.
- Defect: "Structuring against it" does not name its object in the TOC or the PDF bookmarks. Standards Section 8 requires a heading that "names its content plainly and specifically", and round 1 defect 13 set the same rule.
- Fix: retitle the subsection "Structuring a project against the obsolescing bargain" in the u12 TOC line, the u12 anchor table and the registry row.

### 2. Registry caption debris
- Severity: minor
- Location: `bible/anchor-registry.md`, rows `cl:47.1`, `cl:47.1a`, `cl:47.1b`, `cl:47.1c` (l.3513 to 3516) and `ssec:84.3.1` (l.6105).
- Defect:
  - The four cl:47.1 captions carry the parser fragment "(clausevariants parent)". It is not in u10's anchor table (u10 l.844 and l.845).
  - ssec:84.3.1 has lost its closing quotation mark: "How the Taxonomy defines "environmentally sustainable". The brief (u14 l.1350 and l.1557) has it.
  - Writers copy captions from the registry, so the defects would print.
- Fix:
  - Set cl:47.1 to "Permitted leakage and leakage indemnity, share purchase agreement".
  - Set cl:47.1a, cl:47.1b and cl:47.1c to that caption followed by "(Illustrative, seller-friendly)", "(Illustrative, lender-friendly)" and "(Illustrative, buyer-friendly)".
  - Restore the closing quotation mark on ssec:84.3.1.

### 3. Section and caption titles still shared across chapters
- Severity: minor
- Location: registry Section 6 "Unresolved (1)". The duplicated headings are:
  - sec:7.9 and sec:41.6 "Working capital"
  - ssec:10.2.1 and sec:51.3 "Representations and warranties"
  - ssec:10.2.2 and sec:51.4 "Covenants"
  - ssec:11.7.1 and ssec:73.1.1 "Power, energy, and duration"
  - ssec:11.11.3 and ssec:18.4.3 "Curtailment"
  - ssec:14.14.4 and sec:60.7 "Sanctions"
  - captions ex:21.6 and ex:45.7; exh:40.4 and exh:55.9
- Defect: round 1 defect 3 required that no two sections share a title apart from the fixed element headings. A repeated heading gives the PDF bookmarks and the index two identical entries for different content. The registry leaves the retitling to the writers under R-117. It is still unassigned: no brief carries the new titles.
- Fix: retitle the later occurrence now in its brief and in the registry, so the Phase 3 writer receives a locked title:
  - sec:41.6 "Working capital rows in the model"
  - sec:51.3 "Representations and warranties in the facility agreement"
  - sec:51.4 "Covenants in the facility agreement"
  - ssec:73.1.1 "Power, energy, and duration in a storage project's contracts"
  - ssec:18.4.3 "Curtailment under a PPA"
  - sec:60.7 "Sanctions in live projects"
  - ex:45.7 "Availability deductions in the model"
  - exh:55.9 "Case P closing-day sources and uses"

### 4. Replacement figures recur across units as different quantities
- Severity: minor
- Location (brief bodies, revision logs excluded):
  - USD 438.7 million is three unrelated principals: Ex 29.2 export contract (u07 l.158), Ex 55.1 underwritten debt (u11 l.1312) and Ex 61.3 EPC price (u13 l.199).
  - 403.7: Ex 36.10 CFADS (u08 l.599) and Ex 78.4 reserves (u16 l.466).
  - 397.3: Ex 21.4 NSR revenue (u05 l.1434) and Exercise 46.10 EV (u10 l.342).
  - 438.9: u15 l.524 GWh and Ex 80.2 GBP fleet cost (u16 l.1049).
  - 437.9: u02 Ch 7 drill PP&E (l.895) and Ex 12.9 capex (u03 l.977).
  - 186.4 is a different input in eight places across seven units: a loan, hard costs, reserves in Mt twice, a claim and others (u02 l.579, u07 l.821, u09 l.1076 and 2132, u10 l.1104, u11 l.1026, and others).
- Defect: none of these is a style-sheet figure, so A.11 is not breached. But the revisers picked their replacements independently in the 380 to 440 band around 412.6, and the result is the pattern round 1 defect 5 objected to: the same lumpy number reappearing across chapters as debt, capex, reserves and value. Standards Section 8 (epistemic tics) applies.
- Fix:
  - Keep the first occurrence of each figure in book order.
  - Change the others to distinct values and recompute the dependent results, so that no illustrative input value of three or more significant figures appears in two different examples or exercises unless the item is the same deal. The Ex 61.3 change carries through to Exercise 61.8.
  - Add to A.11: "Before fixing an input, search all briefs for the value; a figure already used elsewhere may not be reused for a different quantity."

### 5. Example 9.6 reprints the style-sheet sample passage
- Severity: minor
- Location: u02 l.1425 (Example 9.6); `bible/style-sheet.md` Section 12 and Addenda A.10 and A.11.
- Defect: Example 9.6 uses the Section 12 sample passage "verbatim in substance and numbers" (120 MW, 380.0 GWh, USD 52.40/MWh, and so on), and the brief says it "stays unlocated". This conflicts with two Addenda:
  - A.11 names "the figures in the sample passage of Section 12" among the figures no writer may use as inputs;
  - A.10 requires every example that models a project to be located.

  Section 12, however, labels the passage `ex:9.6`. Two binding rules contradict each other.
- Fix: choose one route and record it in decisions.md.
  - (a) Add an explicit exception to A.10 and A.11: "Section 12 is Example 9.6 and is printed as written."
  - (b) Locate Example 9.6 (for example, at a fictional 120 MW wind farm in Schleswig-Holstein, 2026) with fresh lumpy inputs, recompute it, and mark Section 12 as format-only.

### 6. Suspiciously round inputs in two revised items
- Severity: minor
- Location:
  - u02 Example 9.9 (l.1428): prices USD 48.0, 52.0, 57.0 and 63.0/MWh, which give an expected price of exactly 55.0.
  - u16 Exercise 78.6 (l.540): reserves 96.0 Mt, throughput 8.0 Mtpa, an exact 12-year life, and CFADS of USD 486.0 million.
- Defect: these are the round, symmetrical illustrative figures that standards Section 8 (epistemic tics) and A.11 ban. Neither item says the round numbers are the teaching point.
- Fix: replace them with lumpy values and recompute the stated answers in Python:
  - Ex 9.9: expected price, expected output, product of expectations, expected revenue, covariance and correlation.
  - Exercise 78.6: tonnage-tail tenor, NPV of CFADS, and the remaining-NPV shares at 6 and 7 years.

### 7. Exercise 21.9 answer key: one value is truncated, not rounded
- Severity: minor
- Location: u05 Exercise 21.9 (l.1525).
- Defect: the years 9 to 13 delivery margin is 7,670 × (1,960 − 450) = USD 11,581,700, which prints as USD 11.582 million to three decimals. The brief prints 11.581. The other answers (15.033, 13.269, IRR 9.32%, flat-price IRR 11.31%) are correct.
- Fix: change "11.581" to "11.582".

### 8. En dash in a heading
- Severity: minor
- Location: registry and u15 TOC, ssec:75.5.2 "The Chad–Cameroon pipeline as a project-financed export system".
- Defect: style sheet 3.1 says headings have "no dashes". The en dash is the conventional form of this name, and standards Section 4 spells it that way, but no rule says whether a proper-name en dash is allowed in a heading. The writer and the build checker will disagree.
- Fix: add one line to style sheet 3.1, "An en dash inside a proper name (Chad–Cameroon) is not a dash for this rule", and log it in decisions.md. Otherwise, retitle the heading "The Chad and Cameroon pipeline as a project-financed export system".

---

## Recomputation (Python)

All items below were changed in the round 1 revision, per each brief's revision log or "recomputed" notes. They were recomputed from the brief's own inputs.

### Worked examples (33): all match to the printed precision

| Item (brief) | Key results checked | Result |
|---|---|---|
| Ex 3.3 (u01) | delay interest 91.9, 187.3, 286.4 | match |
| Ex 3.4 (u01) | 24.91, 18.18, 27.0% less | match |
| Ex 9.1 (u02) | mean 436.48; median 436.15; s.d. 25.38 and 24.74; CV 5.81%; bins 4, 4, 6, 4, 2 | match |
| Ex 9.2 (u02) | expected delay 52.07 days; s.d. 76.3; USD 9.69 million | match |
| Ex 9.3 (u02) | mode 1.029 (352.6); median 370.1; mean 1.106 (379.2); P90 1.432 (490.7) | match |
| Ex 9.4 (u02) | 41.9 GWh; 9.7 GWh | match |
| Ex 9.5 (u02) | P75 399.1; P90 373.6; P95 358.4; P99 329.9 | match |
| Ex 9.7 (u02) | σ 9.01%, 6.20%, 6.00%; P90 377.9, 393.4, 394.4; P99 337.7, 365.7, 367.6 | match |
| Ex 9.8 (u02) | σ 48.70, 61.24, 68.34; P90 652.2, 636.1, 627.0 (equals the sum of the two P90s) | match |
| Ex 9.9 (u02) | 55.0; 408.0; 22.44; 22.28; −0.157; −0.97 | match (round inputs: new defect 6) |
| Ex 12.9 (u03) | 86.69 million m3; 37.7 MW; 313,809 MWh; CRF 0.08658; 0.437; 0.175; total 0.754 | match |
| Ex 17.4 (u05) | DS 40.92; exposure table for years 0, 3, 6, 10, 15 and 20; year 4 537.6; year 5 523.5; shortfall 59.4 | match |
| Ex 19.1 (u05) | IRR 11.04%; level cash 5.805 (−43.5%); debt service 5.759; equity 0.05 | match |
| Ex 25.4 (u06) | 70,016 a day; 29.83; 25.63; 4.20; interest 13.4632 (simple) | match |
| Ex 29.2 (u07) | 65.81; 372.90; 219.35; 22.0%; 469.30; 503.81; premium 34.51; 25.19; loss 226.71, 11.34, 215.4 | match |
| Ex 29.3 (u07) | 2.87% to 5.79%; WAL 6.975; 7.90 at 7.5%; break-even growth 6.98% | match |
| Ex 34.1 (u07) | DS 27.45; revenue 52.26 (119.62/MWh); blended 0.71, 5.09, 17.84; 46.28 (105.94; −11.4%); cost 4.66%; grant element 57.9% | match |
| Ex 34.2 (u07) | senior EL 2.59%; first-loss EL 12.0% | match |
| Ex 35.4 (u08) | six-month DSCRs 1.72, 0.97, 1.75, 0.89, 1.65, 0.996; 12-month 1.32, 1.33 (1.325), 1.36; USD 16.2 million; sculpted series | match |
| Ex 36.10 (u08) | debt 3,540.0; year-1 DS 310.5 and interest 260.2; year-7 balance 2,991.7 (84.5%); soft mini-perm balances 2,781.6 to 185.5, nil in year 17 | match |
| Ex 36.11 (u08) | revenue 19.12 (13.10 and 6.02); CFADS 14.27, 11.81, 10.55, 8.78; bucket 79.9; 1.46x, 1.45x, 2.00x; uniform 94.4; contracted only 53.0 | match |
| Ex 51.2 (u11) | sources 145.3; shortfall 5.9 | match |
| Ex 59.6 (u12) | DSCR 1.96x; 129.0; 66.1; 62.8; 0.65x | match |
| Ex 61.3 (u13) | planned value 267.6; earned value 238.2; SPI 0.890; 38.2 months; 15.7 | match |
| Ex 61.4 (u13) | 7.48, 2.23, 17.12, 2.50, 29.34; LDs 19.66; gap 9.69; at 240, 365 and 400 days: 61.19/39.31/21.88, 94.36/57.93/36.43, 103.65/45.72; cap at 353.7 days | match (PPA LDs 2.505 printed 2.50) |
| Ex 61.5 (u13) | 295.4; 445.3; 401.07; 44.23; 268.0 | match |
| Ex 70.2 (u15) | capture prices and revenue in years 1, 5, 10, 14 and 15; cumulative 204.77 against 238.74; capacity factor 25.7% | match |
| Ex 78.4 (u16) | reserve life 13.24 years; maximum tenor 9.27 years; 32.0% | match |
| Ex 80.2 (u16) | 65.84; PV 14.98; annuity factor 12.663; rental 33.48 and 34.66; 1.18 | match |
| Ex 81.2 (u16) | 231.0 million m3 / 188.9; 278.8 / 228.0; 39.1 | match |
| Ex 86.2 (u17) | 26.458; 19.518; 389.2 GWh; 25.221; 7.530; 17.691; DS 13.105; 1.49x; 14.458; 1.22x; factor 9.0414; debt 118.48 and 130.72 | match |
| Ex 86.3 (u17) | 1.158, 1.293, 1.310, 1.332; 0.237 | match |
| Ex 86.4 (u17) | spread 1.9474%; RAROC 12.17%; income 0.838 | match |

### Exercise answers (20): 19 match; 1 display error

| Item (brief) | Key answers checked | Result |
|---|---|---|
| Exercise 17.13 (u05) | NPV-only and greater-of exposure in years 0, 5, 8, 10, 15 and 20 (586.9 to 1,550.4) | match |
| Exercise 21.6 (u05) | netbacks, variable charges, margins and decisions for both Henry Hub prices; fee 9.41 | match |
| Exercise 21.7 (u05) | 51.640 / 50.142 / 50.142; charges on actual flow 37.107 and 23.310; top-ups 13.035 and 26.832; 49.413 | match |
| Exercise 21.8 (u05) | 46.07%; 1,280.75; 3.6009 and 0.4206 oz; 13.21; 2.40; NSR 1,126.55 | match |
| Exercise 21.9 (u05) | margins 15.033, 13.269, 11.581; IRR 9.32%; 11.31% | mismatch: 11.582 (new defect 7) |
| Exercise 21.10 (u05) | 82 weighted unavailable lane-hours; 0.0915; 0.1099; 0.2014 | match |
| Exercise 35.14 (u08) | 1.31x, 1.33x, 1.39x; 1.37x | match (round 1 defect 10 fixed) |
| Exercise 36.8 (u08) | 341.9; 252.2; 255.0; 59.0% | match |
| Exercise 36.17 (u08) | 123.5 outstanding at the end of year 17; repaid in year 18 | match |
| Exercise 46.10 (u10) | 3.35; 126.15; 88.25; 136.9 | match |
| Exercise 61.8 (u13) | 258.0; 0.964; 35.3 months | match |
| Exercise 61.9 (u13) | 45.27; 29.48; 15.78 | match |
| Exercise 61.10 (u13) | 454.96; 9.66 | match |
| Exercise 78.5 (u16) | 305.92 million lb; 119.1; 81.6; 16.4; C1 0.40; royalty 11.9; AISC 0.57; margin 0.74 | match |
| Exercise 78.6 (u16) | 8.4 years; 2,874.9; 31.0% and 24.0%; 6 years | match (round inputs: new defect 6) |
| Exercise 78.7 (u16) | 327.7; 5.2332; 1,714.8; 1.04x; 5.1851; 311.0; 1.37x; 304.3; 1,577.7; 34.7 | match |
| Exercise 78.8 (u16) | 20.09, 16.61, 13.91; IRR 9.25%, 6.21%, 3.60% | match |
| Exercise 78.10 (u16) | year-1 CFADS 302.7, 243.2, 165.9; year-10 114.0, 77.2, 29.3; totals 2,083.5, 1,601.8, 975.6 | match |
| Exercise 86.5 (u17) | 382.0 GWh; 24.752; 17.222; 12.757; 115.34 (3.14 less) | match |
| Exercise 86.6 (u17) | spread 1.6427%; RAROC 10.27%; 0.554; 5.40; 7.13% after downgrade | match |
