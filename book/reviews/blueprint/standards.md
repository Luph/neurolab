# Blueprint review: standards lens (standards.md Sections 6 to 10)

Reviewer: standards lens. Date: October 3, 2026.
Scope: all 88 chapter briefs (`bible/briefs/u01.md` to `u17.md`), read against `standards.md` Sections 6 to 10, the style sheet with its Addendum, D-008, `bible/ownership-resolutions.md`, `bible/anchor-registry.md`, `bible/architecture.md`, the figure ledgers and `facts/`.

Method. I split the briefs into 88 chapter chunks by script and checked every chunk mechanically for all 17 brief components, the target length, the exercise count by tier, the can-do statement (2 to 4 items, each tied to a capability number), the opening and the close. I extracted all 3,513 chapter, section and subsection headings from the anchor registry and confirmed they match the briefs' locked TOC headings exactly (3,297 TOC lines parsed, 0 differences), then scanned them for the banned heading patterns. I tallied place, sector and round-number use across all 572 worked examples. I cross-checked fact-sheet slugs cited in the briefs against `facts/`, and the numbers in every fact sheet's "Do not state" list against the briefs. I recomputed 26 worked examples and 15 exercise answers in Python. Scripts and outputs are in the session scratchpad.

## Verdict: FAIL

One blocking defect: the locked TOC breaks the Section 8 heading rules in 60 headings. The briefs pass on most other points. All 88 chapters have every Section 6 element. Every chapter has three exercise tiers with 10 to 18 exercises in total. Every can-do statement has 2 to 4 items tied to capabilities. Every running-case figure ID cited exists in the ledgers. The modeling course is specified cell by cell, with notation and Excel. Numerical accuracy is excellent: 25 of the 26 recomputed examples match exactly, and the 26th differs only in a rounding display.

Counts: 1 blocking, 9 major, 10 minor.

---

## Blocking

### 1. Locked TOC headings use banned forms (colon-subtitle and formula headings)
- Severity: blocking
- Location: `bible/anchor-registry.md` Section 5 (canonical headings) and the matching TOC lines in the briefs.
- Defect: Standards Section 8 ("Headings and titles") bans colon-and-subtitle headings and formula headings. Style sheet 4.1 allows only "Case P:", "Case T:", "Case R:" and "Walkthrough:" to take a colon. Registry rule 2 tells writers to use these headings as locked. A scripted scan found:
  - (a) 49 colon-subtitle headings, plus 3 combined-case prefixes ("Case P and Case T:", "Case R and Case P:") that the style sheet does not allow;
  - (b) 5 banned formula headings and 1 non-compliant prefix:
    - ssec:22.8.3 "Beyond the single EPC contract" ("Beyond X")
    - sec:64.12 "The role of the state" ("The Role of X")
    - ssec:35.5.2 "Why gearing still matters when DSCR sizes the debt" ("Why X Matters")
    - ssec:66.6.1 "Why hedge accounting matters to a project and its sponsors" ("Why X Matters")
    - sec:8.8 "Real case: the same reactor at two costs of capital" (a "Real case:" prefix, which the style sheet does not provide for)
  - (c) one dash heading: sec:86.3 "The risk–mitigant–residual table" (style sheet 3.1: no dashes in headings).
- Required fix: retitle each heading in the anchor registry, keeping its label and number, and record the list as a ruling in `ownership-resolutions.md` so writers use the new titles. Proposed titles:

| Label | Current | Required |
|---|---|---|
| sec:1.2 | Development: from an option on grazing land to a winning bid | From an option on grazing land to a winning bid |
| sec:1.4 | The model: from sunlight to cash for lenders | Modeling sunlight into cash for lenders |
| ssec:2.1.3 | SunEdison and TerraForm: a ring-fence tested | SunEdison, TerraForm, and a ring-fence under test |
| sec:2.2 | Recourse: what lenders can reach | What lenders can reach |
| ssec:2.3.3 | Sabine Pass: contracts that made a plant financeable | How contracts made Sabine Pass financeable |
| ssec:3.3.2 | Dabhol: a contract cannot make power affordable | Dabhol and the limits of a contract on affordability |
| sec:3.6 | After 2008: banks retreat, rules change, new lenders arrive | Bank retreat, new rules, and new lenders after 2008 |
| sec:3.7 | Public credit for new technology: Ivanpah | Ivanpah and public credit for new technology |
| sec:5.7 | Irregular dates: XNPV and XIRR | XNPV and XIRR for irregular dates |
| ssec:7.3.2 | Accruals: earned is not received | Earned is not received |
| sec:8.8 | Real case: the same reactor at two costs of capital | The same reactor at two costs of capital |
| sec:9.5 | Exceedance levels: P50, P90 and P99 | Exceedance levels P50, P90, and P99 |
| ssec:14.2.1 | Development: high probability, small money | Development risk with high probability and small money |
| ssec:14.2.2 | Construction and commissioning: the peak | Construction and commissioning as the risk peak |
| sec:14.4 | Construction risk: cost, time and performance | Construction cost, time, and performance risk |
| sec:14.13 | Currency risk: devaluation, convertibility and transfer | Devaluation, convertibility, and transfer risk |
| sec:15.2 | Analyzing a risk: from trigger to cash flow | Tracing a risk from trigger to cash flow |
| ssec:15.5.4 | Risks no private party can carry: retention and sharing bands | Retention and sharing bands for risks no private party can carry |
| sec:15.6 | Residual risk: what equity and debt are left holding | What equity and debt are left holding |
| sec:16.10 | Combining tools: the layered loss stack | Combining tools in a layered loss stack |
| sec:17.7 | Guarantee chains that paid and one that did not: Lake Turkana, REIPPPP and Dabhol | Guarantee chains at Lake Turkana, REIPPPP, and Dabhol |
| sec:18.4 | Volume risk: take-or-pay, deemed energy and curtailment | Take-or-pay, deemed energy, and curtailment |
| sec:19.8 | Thames Tideway and Sizewell C: paid from the first day of construction | Thames Tideway and Sizewell C, paid from the first day of construction |
| sec:20.6 | Storage revenue: tolls, capacity and ancillary services | Storage tolls, capacity, and ancillary-service revenue |
| sec:22.9 | Sabine Pass, Vogtle and Carillion: three fixed prices, three outcomes | Three fixed prices at Sabine Pass, Vogtle, and Carillion |
| ssec:22.8.3 | Beyond the single EPC contract | When one EPC contract is not enough |
| sec:35.1 | What lenders are paid from: cash flow available for debt service | Cash flow available for debt service |
| ssec:35.2.3 | Looking back and looking forward: historic and projected DSCR | Historic and projected DSCR |
| ssec:35.5.2 | Why gearing still matters when DSCR sizes the debt | Gearing as a cap when DSCR sizes the debt |
| ssec:35.6.4 | Whose forecast: optimism in the base case | Optimism in the sponsor's base case |
| sec:35.7 | Chile's northern solar defaults: when produced energy is not cash | Chile's northern solar defaults and energy that never became cash |
| sec:36.9 | Repayment-profile rules: weighted average life and installment limits | Average-life and installment limits on the repayment profile |
| sec:41.1 | Technical drivers: availability, dispatch, degradation and energy | Availability, dispatch, degradation, and energy |
| ssec:66.6.1 | Why hedge accounting matters to a project and its sponsors | What hedge accounting changes for a project and its sponsors |
| sec:64.12 | The role of the state | What the state does in a project restructuring |
| sec:68.11 | Case P and Case T: Castellan grades Bélanou, and the Merrick Link's insurer bondholders | Case P: Castellan grades Bélanou (move the Case T beat to its own ssec or to sec:68.12 headed "Case T: ...") |
| ssec:69.5.3 | A sector clause: carbon-cost pass-through in a tolling agreement | Carbon-cost pass-through in a tolling agreement |
| ssec:70.2.1 | Wind: turbines, availability and cold weather | Wind turbines, availability, and cold weather |
| ssec:70.2.2 | Solar: modules, inverters, trackers and clipping | Solar modules, inverters, trackers, and clipping |
| ssec:70.5.1 | Wind: turbine supply, balance of plant and the full-service agreement | Wind turbine supply, balance of plant, and the full-service agreement |
| ssec:70.5.2 | Solar: modules, EPC and warranties | Solar modules, EPC, and warranties |
| ssec:70.5.4 | A sector clause: the turbine availability guarantee | The turbine availability guarantee |
| ssec:70.8.4 | CSP: Ivanpah and Noor Ouarzazate I | Concentrated solar at Ivanpah and Noor Ouarzazate I |
| ssec:71.6.3 | A sector clause: weather downtime in a transport and installation contract | Weather downtime in a transport and installation contract |
| sec:73.9 | Case R and Case P: tolls, floors and a 225 kV line | Case R: battery tolls and floors (Case P's 225 kV line as a second casescene in the same section, or its own section "Case P: ...") |
| ssec:74.3.1 | Sponsor balance sheets under a CfD: Hinkley Point C | Hinkley Point C on sponsor balance sheets under a CfD |
| ssec:74.3.2 | A nuclear RAB: Sizewell C | Sizewell C under a nuclear RAB |
| ssec:74.3.3 | Regulated utilities and federal guarantees: Vogtle 3 and 4 | Vogtle 3 and 4 under rate regulation and federal guarantees |
| ssec:74.3.4 | A sovereign lends to itself: Barakah | Barakah and a sovereign lending to itself |
| ssec:75.5.2 | Chad–Cameroon: an equity-funded upstream and a project-financed export system | The Chad–Cameroon pipeline as a project-financed export system |
| ssec:75.5.3 | Sanctions on a pipeline: Nord Stream 2 | Nord Stream 2 and sanctions on a pipeline |
| ssec:76.5.1 | Mozambique LNG: force majeure, restart and re-documentation | Force majeure, restart, and re-documentation at Mozambique LNG |
| ssec:76.5.2 | Sanctions and LNG: Arctic LNG 2 | Arctic LNG 2 under sanctions |
| ssec:77.7.4 | Construction for a complex: EPC packages, EPCM and the wrap | EPC packages, EPCM, and the wrap for a process complex |
| sec:84.12 | Case R and Case P: a green private placement and a bond that could not be green | Case R: a green private placement (Case P's bond as a second casescene, or its own "Case P:" section) |
| ssec:86.3.2 | Residual risk: whose, and how much | Who holds the residual risk, and how much |
| sec:86.3 | The risk–mitigant–residual table | The risk, mitigant, and residual table (rename Framework 86.2 to match) |

Alternatively, amend style sheet 4.1 to allow "Case P and Case T:" and record the change in `decisions.md`. Either way, one rule must cover the three combined-case headings.

---

## Major

### 2. Registry chapter titles contradict architecture.md and ruling R-113
- Severity: major
- Location: `bible/anchor-registry.md`, the "### Chapter N:" headers and `ch:` rows for Ch 23, 25, 75, 77, 79, 83, and 88 (lines 1769, 1884, 5123, 5241, 5388, 5667, 6016); also the serial-comma titles of Ch 8, 12, 15, 17, 19, 20, 31, 34, 37, 39, 41 to 43, 47 to 49, 52, 54, 59, 63 to 65, 73, and 76 to 82.
- Defect: The registry calls itself canonical and claims to include the rulings, but it never applied R-113 or D-028.
  - Ch 25 "Inputs and access: fuel, water, grid, land and permits" and Ch 88 "The frontier: evaluating new structures" both keep banned colon-subtitle forms.
  - Ch 75 keeps "(incl. reserve-based lending)", Ch 79 keeps "(Case T ramp-up)", and Ch 77 keeps "(gigafactory)".
  - Ch 23 and Ch 83 keep their old wording.
  - About 30 titles lack the serial comma.
  - The brief headers for Ch 88 and Ch 77 carry the same stale titles.
- Required fix: copy the architecture.md title column verbatim into the registry `ch:` rows and "### Chapter N" headers for all 88 chapters. Add a line to registry Section 2 recording that R-113 is applied.

### 3. Sector chapters use template headings that do not name their content
- Severity: major
- Location: registry and brief TOCs for Ch 77 to 83:
  - "The contract set": sec:77.7, 78.6, 79.6, 80.6, 81.6, 82.6, 83.6
  - "Typical financing terms": sec:77.8, 79.7, 80.7, 81.7, 82.7, 83.7
  - "Key risks": sec:77.6, 78.5, 80.5, 82.5
  - "Modeling specifics": sec:80.8, 81.8, 82.8, 83.8
  - "Verified anchors": ssec:77.8.1, 79.7.1, 81.7.1, 82.7.1
  - "Indicative ranges and their drivers": ssec:77.8.2, 79.7.2, 80.7.2, 81.7.2
- Defect: Section 8 requires a heading that "names its content plainly and specifically". "Key" as an all-purpose adjective is banned. "Verified anchors" is production jargon from the fact-sheet process and would print in the book. Repeating identical headings across seven chapters reads as a template, which the AI-tic list warns against.
- Required fix: retitle each heading with the sector's own content. For example:
  - sec:79.6 becomes "Concession deed, D&C contract, and tolling-system contract for a toll road"
  - sec:82.5 becomes "Tenant concentration, power supply, and obsolescence risk in digital assets"
  - ssec:77.8.1 becomes "Financing terms at Sadara and Northvolt Ett"
  - ssec:77.8.2 becomes "Tenor, gearing, and cover ranges for spread businesses, 2022 to 2026"

  Apply the same pattern to the other 21. No two sections in the book should share a title, apart from the fixed element headings.

### 4. Most worked examples have no place, and the sector chapters have none located at all
- Severity: major
- Location: worked-example lists ("Worked examples" item 6) across the briefs.
- Defect: Section 7 requires examples that "vary scale, sector, and geography". Section 8 bans "generic examples that could be set anywhere" and requires sector, size, place, date, and parties. By script, 363 of the 572 examples (63%) name no country, region, market, running case, or real case in their specification. Every example in Ch 8, 9, 13, 20, 33, 42, 44, 45, 63, 71 to 78, 80 to 82, 86, and 87 is unlocated. In the sector deep dives (Ch 71 to 82) not one example states a place. Examples whose subject is placeless arithmetic (Ch 5.4, 6.3, 8.2) are acceptable. Deal-type examples are not: for example 17.3 "a 320 MW gas-fired IPP", 71.2 "a 1,000 MW project", 75.2 RBL redetermination, 81.2 "a 600,000 m3/day RO plant", 82.x data centers, 86.x credit papers.
- Required fix: for every example that models a project, financing, or contract, add to its specification a country or market, a date or year, and named (fictional) parties. Spread them so that each Part covers at least four regions (Americas, Europe, Middle East and Africa, Asia-Pacific). In Ch 71 to 82 each sector example should sit in the market where that sector is actually financed: for example, offshore wind in the UK, Taiwan, or the US Northeast; RBL in the North Sea or West Africa; desalination in the Gulf or Morocco. Add a note to brief-instructions so later briefs carry this field.

### 5. The style sheet's sample figure "412.6" is reused as an input across the book, and round principals recur
- Severity: major
- Location:
  - The figure "412.6" appears 27 times across 13 units. Among the examples and exercises using it are Ex 17.4 (senior debt USD 412.6 million), Ex 25.4 (P50 412.6 GWh), Ex 29.2, Ex 34.1 (capex USD 412.6 million), Ex 36.x (CFADS USD 412.6 million), Exercise 36.8, Ex 39.4, Ex 41.4, Ex 44.4, Exercise 46.10, Ex 61.x (EPC USD 412.6 million), Ex 70.1 (412.6 GWh), Ex 78.2 (reserves 412.6 Mt), Ex 80.4, and the u02 Ch 7 drill.
  - Round principals appear in Ex 32.1 and 32.2 (USD 100.0 million and 400.0 million), Ex 38.2 to 38.10 (USD 100, 250, 300, 400, 500, and 600 million), Ex 19.1 (EUR 100.0 million), and about 20 more (scripted list: 3.3, 3.4, 6.6, 15.3, 16.5, 27.3, 27.4, 29.5, 30.3, 31.6, 33.4, 34.6, 50.2, 58.9, 58.10, 58.12, 60.6, 67.10, 68.1, 68.3, 68.4).
- Defect: The style sheet says its figures "illustrate format only… no writer may cite them". When the same number turns up as capex, debt, CFADS, energy, and ore reserves in a dozen chapters, it is exactly the "suspiciously round or symmetrical" pattern that Section 8 (epistemic tics) and Section 7 ("realistic figures") ban, and an attentive reader will notice it.
- Required fix:
  - Replace every 412.6 input with a distinct lumpy figure and recompute the dependent results in Python. Ex 44.4 (410.9 against 412.6) and Ex 39.4 need their results recomputed.
  - Replace round principals with lumpy ones unless the round number is the teaching point. A commitment can be round, but then say so (for example "a USD 400 million commitment, typical of a club deal"). Ex 38.4 to 38.10 should use lumpy commitments.
  - Add "never reuse a style-sheet sample figure as an input" to brief-instructions and to the numbers-auditor checklist.

### 6. About 87 calculation exercises have no inputs or answers
- Severity: major
- Location: Exercise sets (item 13). By script, 87 Tier 2 and Tier 3 calculation items say "given", "supplied", "stated", or "writer specifies" without the numbers. Heaviest in:
  - Ch 21 (5: 21.x pipeline, NSR, stream, deductions, invoicing model)
  - Ch 10 (4), Ch 22 (4: 22.6 to 22.9), Ch 78 (4)
  - Ch 6, 8, 9, 20, 41, 42, 43, 58, 77, and 79 (3 each)
  - Ch 7, 17, 18, 25, 45, 52, 55, 56, 59, and 83 (2 each)

  Separately, Tier 2 sets in Ch 17 to 22, 26 to 34, 47 to 49, 57 to 60, 66 to 67, 77 to 83, and 86 to 88 carry no answer values at all. By contrast, u08 (Ch 35 to 38) and u13 (Ch 61 to 65) give inputs and Python-checked answers for every Tier 2 item.
- Defect: Section 6 item 11 and Section 12 (practice test) require complete worked solutions. Section 7 requires realistic, lumpy, reconciled numbers. Where a brief gives neither inputs nor answers, the writer must invent numbers that nobody has checked, and the numbers auditor has nothing in the brief to verify them against.
- Required fix: for each listed exercise, add to the brief the full input set (lumpy, with units) and the Python-computed key answers, in the u08 format ("Inputs: …; Answers: …"). Do the listed 87 items first, then add key answers to every Tier 2 calculation item in the chapters named above.

### 7. Target lengths for multi-sector chapters are too short for the content assigned
- Severity: major
- Location: Header target lengths for:

| Chapter | Sectors covered | Target (words) |
|---|---|---|
| Ch 70 | onshore wind and solar | 9,500 |
| Ch 72 | hydro and geothermal | 9,000 |
| Ch 73 | storage, transmission, and interconnectors | 9,500 |
| Ch 75 | upstream, midstream, and RBL | 9,500 |
| Ch 76 | liquefaction, regasification, and FPSOs | 9,500 |
| Ch 80 | rail, urban transit, airports, and ports | 10,000 to 11,000 |
| Ch 81 | social infrastructure, water, desalination, and waste-to-energy | 10,000 to 11,000 |
| Ch 82 | telecoms, fiber, towers, and data centers | 9,500 to 10,500 |
| Ch 83 | hydrogen, CCS, and sustainable fuels | 10,000 to 11,000 |

- Defect: Coverage map P requires, for each sector, industry economics, asset workings, revenue models, key risks, contract set, financing terms, modeling specifics, and landmark deals and failures. Each of these chapters also carries 12 or 13 exercises with full solutions, a walkthrough, a running-case installment, a notebook, a drill, and real-case sections. That fixed apparatus takes roughly 6,000 to 7,000 words. In Ch 80 and Ch 81, for example, about 3,500 to 4,500 words would remain for the core teaching of four sectors, under 1,200 words a sector. Section 6 says "never compress to fit".
- Required fix:
  - Raise the targets to 13,000 to 15,000 words for Ch 80, 81, 82, and 83 (four or three sectors each), and to 11,000 to 13,000 words for Ch 70, 72, 73, 75, and 76.
  - Add a line to each of these briefs: "the target is a floor for the core teaching of each sector, not a cap."
  - Update the per-chapter targets in `tracker.md`.

### 8. Briefs cite 19 fact-sheet slugs that do not exist, with no mapping to the sheets that do
- Severity: major
- Location:
  - u03 (t-infra-asset-metrics), u05 (t-thermal-ipp-terms), u08 (t-flex-and-fees)
  - u09 (t-spreadsheet-errors, t-fast-standard, t-mining-reporting, t-energy-yield, t-traffic-forecast-bias, t-battery-degradation)
  - u10 (t-legal-opinions), u12 (t-country-risk)
  - u13 (t-operating-waivers, t-refi-repricing-norms, t-step-in-practice, t-decommissioning, t-repowering)
  - u14 (t-sustainable-finance-2), u15 and u07 (t-oecd-arrangement-history), u17 (t-critical-minerals-finance)
  - `bible/fact-sheet-plan.md`, which lists none of the roughly 60 later sheets and has no request-to-slug table.
- Defect: Section 11 Phase 1 item 6 and Section 9 tie real-world facts to fact sheets. Several brief sections depend on these slugs:
  - ssec:39.2.2 (the four FAST principles "from t-fast-standard")
  - ssec:59.1.2 (sovereign ceiling method "only from t-country-risk")
  - Ch 62 and 65 ("t-repowering (needed)")
  - Ch 45 (energy-yield and battery-fade norms)
  - Ch 84 (EU Taxonomy gas thresholds, FR-6)

  Some requests were fulfilled under other names (spreadsheet-errors, t-traffic-forecast-accuracy, t-decommissioning-liabilities, t-reserves-codes, t-oecd-pf-2018, t-critical-minerals-policy), but no file tells a writer so.
- Required fix:
  - Add a "Request mapping" table to `fact-sheet-plan.md` giving each requested slug its delivered slug: t-spreadsheet-errors to spreadsheet-errors; t-traffic-forecast-bias to t-traffic-forecast-accuracy; t-decommissioning to t-decommissioning-liabilities; t-mining-reporting to t-reserves-codes; t-oecd-arrangement-history to t-oecd-pf-2018; t-critical-minerals-finance to t-critical-minerals-policy (confirm it covers offtake-linked finance). Then add every later sheet to the plan's tables.
  - Commission t-fast-standard, t-country-risk (or confirm that t-dfis and t-political-risk-theory cover the sovereign ceiling), t-repowering, t-energy-yield, t-battery-degradation, and t-sustainable-finance-2.
  - For the optional ones (t-legal-opinions, t-operating-waivers, t-refi-repricing-norms, t-step-in-practice, t-flex-and-fees, t-thermal-ipp-terms, t-infra-asset-metrics), either commission them or amend the citing brief sections to say "no fact sheet; state no market figure".

### 9. Clause variants are missing where negotiation drives the outcome
- Severity: major
- Location: Ch 37 (u08), Ch 38 (u08), Ch 32 (u07), Ch 47 (u10), Ch 63 (u13), Ch 52 (u11).
- Defect: Section 7 requires "sponsor-friendly, lender-friendly, and government-friendly variants and where they usually land" wherever negotiation matters. Each of these chapters falls short:
  - Ch 37 owns DSRA sizing, lock-up levels, cash sweeps, and covenant design, which are among the most negotiated terms in a financing, yet its only clause (cl:37.1, DSRA LC substitution) sits inside an exercise solution and has no variants.
  - Ch 38 owns pricing, market flex, and ratchets, and again has only one clause inside an exercise solution.
  - Ch 32's equity-contribution clause is "a single clause (no variants)".
  - Ch 47 (cl:47.1 leakage, cl:47.2 W&I limitation) has annotations but no variants.
  - Ch 63 has only cl:63.1, inside an exercise solution.
  - Ch 52's priority-of-payments clause has no lender-against-sponsor variants on where distributions and sweeps sit.
- Required fix: add to each TOC a core-teaching clause with variants a, b, and c and a landing paragraph:

| Chapter | Clause to add | Section |
|---|---|---|
| Ch 37 | Distribution conditions and lock-up release; cash sweep keyed to LLCR or the tail | ssec:37.4.x and sec:37.3 |
| Ch 38 | Market flex clause in a mandate letter (arranger-, sponsor-, and borrower-friendly) | sec:38.8 |
| Ch 32 | Equity contribution agreement: acceleration of contingent equity on default (sponsor and lender variants) | |
| Ch 47 | Leakage indemnity (seller and buyer variants) | |
| Ch 63 | Voluntary prepayment and refinancing provisions (prepayment fee, make-whole, minimum amounts) with sponsor and lender variants | |
| Ch 52 | A distributions and sweep position in the waterfall clause | |

  Register each new label in the anchor registry.

---

## Minor

### 10. Exercise 35.14 answer key is wrong
- Severity: minor
- Location: u08, Ch 35 item 13, Exercise 35.14.
- Defect: The brief gives "1.31x; 1.34x; 1.40x". Recomputed: 52.7/40.1 = 1.314x; (52.7 + 0.83)/40.1 = 1.3349x, which prints as 1.33x; (52.7 + 0.83 + 2.4)/40.1 = 1.3948x, which prints as 1.39x.
- Required fix: change the answers to "1.31x; 1.33x; 1.39x". If the exercise intends the BI proceeds alone as the third version, state (52.7 + 2.4)/40.1 = 1.37x and reword the question so it names the three versions explicitly.

### 11. A ratio below 1.00x prints as 1.00x in Example 35.4
- Severity: minor
- Location: u08 Ex 35.4.
- Defect: The H2 2029 DSCR is 22.31/22.40 = 0.996x, and the brief prints it as "1.00". In a chapter that teaches what 1.00x means, rounding a shortfall up to break-even misleads the reader.
- Required fix: print "0.996x (debt service not fully covered)" and add one sentence on why a ratio below 1.00x must never be rounded to 1.00x.

### 12. Clause-variant labels missing from the registry, and malformed rows
- Severity: minor
- Location: `bible/anchor-registry.md`.
- Defect: The briefs define more than 40 variant groups. Examples: 17.2, 17.3, 17.4, 17.6; 18.3, 18.4, 18.5; 19.2, 19.3, 19.4, 19.6; 20.2, 20.5; 21.1, 21.6, 21.7; 22.2, 22.5, 22.6; 23.2; 24.1; 26.1; 27.1; 28.1; 51.6; 53.1; 54.1; and the sector clauses 69.1 to 76.1. Most have no `cl:N.Ka/b/c` rows. Rows `cl:35.2 | with` and `cl:35.2c | if required) CFADS definition variants` are parse debris. D-008 and registry rule 1 forbid citing unregistered labels.
- Required fix: add a, b, and c rows (with the variant name) for every variant group named in the briefs. Replace the two debris rows with `cl:35.2` "CFADS definition variants, common terms agreement", plus `cl:35.2a` (sponsor-friendly) and `cl:35.2b` (lender-friendly).

### 13. Indirect-question, filler, and pronoun headings
- Severity: minor
- Location (registry):
  - 55 headings begin with "Why".
  - "...that matter(s)": ssec:49.2.2, 49.5.1, 62.6.1, 77.8.3, 87.9.2.
  - Pronoun or bare headings: ssec:43.5.2 "Implementing it", ssec:57.5.2 "Measuring them", ssec:57.5.3 "Managing them", ssec:61.8.2 "The toolkit", ssec:28.6.1 "The steps", ssec:60.2.2 and ssec:79.5.3 "The record", ssec:58.5.2 "The formulas", ssec:43.7.1 "The catalogue", ssec:35.4.1 "Definition".
- Defect: Section 8 bans question headings "as a default" and requires specific headings. A heading that only makes sense under its parent ("Measuring them") does not name its content in the PDF bookmarks or the TOC.
- Required fix:
  - Rename the pronoun and bare headings with their object, for example "Measuring contingent liabilities", "Implementing Monte Carlo in Excel", "The PLCR defined".
  - Reword the "...that matter" headings to state the criterion, for example "The KPIs lenders test by asset type".
  - Convert at least half of the "Why …" headings to declarative form, for example "Sponsors break the wrap for five reasons".

### 14. British spellings in headings and specifications
- Severity: minor
- Location:
  - Headings: ssec:78.5.6 "Social licence", ssec:43.7.1 "The catalogue", ssec:68.2.1 "The standardised approach", ssec:68.3.1 "The standardised ladder".
  - Specifications: "programme" (u13 Ex 61.x), "specialised" and "standardised" (u14 Ex 68.2).
- Defect: D-006 and style sheet Section 2 set American spelling; the style sheet lists "catalog". Sections 68.2.1 and 68.3.1 use Basel's own term as a heading word, not inside a proper name.
- Required fix: use "Social license", "The catalog", and "The standardized approach" (with "Basel's 'standardised approach'" quoted once in the text as the source term), and correct the specification spellings.

### 15. Serial comma missing in about 330 headings
- Severity: minor
- Location: registry headings with three-item lists, for example ssec:4.3.4, sec:4.5 to 4.8, ssec:5.10.1, sec:6.6, and ssec:6.7.1.
- Defect: D-009 and R-113 require the serial comma in list titles. R-113 fixed chapter titles only.
- Required fix: apply the serial comma to every registry heading containing a list of three or more items; this can be done by script.

### 16. Ch 86 has no walkthrough section heading
- Severity: minor
- Location: u17 Ch 86, item 7; registry sec:86.1 to 86.14.
- Defect: Style sheet 4.1 requires at least one `\section{Walkthrough: …}`. The brief folds the walkthrough into sec:86.8 (a "Case P:" section) and into ssec:86.5.3, so the chapter prints no walkthrough heading.
- Required fix: either add sec:86.x "Walkthrough: reading a project finance credit paper section by section", built on an Illustrative paper, and keep sec:86.8 as the Case P installment; or extend the style sheet to accept a "Case P:" section that is also the walkthrough, and log the change in decisions.md.

### 17. Lake Turkana penalty mechanism stated against "Do not state"
- Severity: minor
- Location: u06 Ch 25, item 5 (Opening).
- Defect: `facts/lake-turkana.md` "Do not state" says to present the EUR 127 million total "and avoid asserting the mechanism". The opening says it is "to be paid partly as a lump sum and partly through a tariff surcharge over six years".
- Required fix: replace that clause with "a penalty reported at about EUR 127 million, part of it recovered from Kenyan consumers through a tariff surcharge", which is verified fact 7 in the sheet, and drop the lump-sum and six-year split.

### 18. Thin example density in some chapters
- Severity: minor
- Location:
  - Chapters with the fewest worked examples for their length: Ch 28 (3 examples for 12,000 to 14,000 words), Ch 74 (3 for 8,500), Ch 30 (4 for 11,500), Ch 52 (4 for 12,000), Ch 54 (4 for 11,000), Ch 88 (4 for 12,000).
  - TOC runs of two or more subsections whose content notes name no example, exhibit, number, case, or scene:
    - Ch 44: ssec:44.3.6 to 44.4.3 (six in a row)
    - Ch 62: ssec:62.2.1 to 62.3.1 (five)
    - Ch 39: ssec:39.6.3 to 39.7.2 (five)
    - Ch 4: ssec:4.3.1 to 4.3.4
    - Ch 61: ssec:61.7.1 to 61.7.3
- Defect: Section 7 sets the rule of no more than two pages without a concrete example, number, scene, or case. Exhibits and cases fill some of these gaps, but these runs are the places where a writer is most likely to produce a page and a half of description.
- Required fix:
  - For each listed run, name in the content note the example, exhibit, or case that the subsection uses. For example, ssec:62.2.2 should work a compliance certificate on Example 62.2's numbers; ssec:44.4.1 to 44.4.3 should apply the audit days to Example 44.x or the Case P audit copy; ssec:4.3.1 to 4.3.4 should use the Llano Pardo lenders.
  - Add two numbered examples each to Ch 28 (a "Who pays if…?" trace with numbers on a second sector), Ch 74, Ch 30, and Ch 54.

### 19. Excel formulas containing "%" are specified for inline `\xl{}`
- Severity: minor
- Location: 12 backticked Excel formulas in the briefs contain "%", for example u02 Ex 5.4 `=PV(8.4%,20,-1.27)` and u02 Ex 6.3 `=PMT(6.35%,10,-126.5)`.
- Defect: D-008 and style sheet 5.3 forbid "%", "#", "\", "{", and "}" inside `\xl{}`. A writer copying these formulas inline will break the build or have to edit them silently.
- Required fix: rewrite them with cell references (`=PV(F5,F6,-F7)`, with the rate in F5), or mark them "excel block" in the brief.

---

## Spot-check of worked-example numbers (Python)

I recomputed 26 worked examples and 15 exercise answers from the brief inputs. All match to the printed precision, except the Exercise 35.14 key (defect 10) and the 0.996x display in Example 35.4 (defect 11).

| Item | Key results checked | Result |
|---|---|---|
| Ex 35.1 | revenue 11.07; EBITDA 8.60; CFADS 7.56; 0.88; sponsor variant 7.96 (+5.3%) | match |
| Ex 35.2 | 1.345x; receivables 12.71; cash CFADS 31.87; 0.96x | match |
| Ex 35.3 | debt service 32.63; min 1.26x; both averages 1.35x | match |
| Ex 35.4 | six-month DSCRs; historic 1.32x; projected 1.325x; rolling 1.36x; USD 16.2m; sculpted series | match (0.996x shown as 1.00, defect 11) |
| Ex 35.5 | PV 359.67; LLCR 1.34x and 1.40x; DSRA 16.32; year-5 balance 179.91; LLCR 1.38x; 1.44x and 1.25x | match |
| Ex 35.6 | PV 634.31; PLCR 2.36x; tail 274.65; tail series reproduces the 1.8% growth and 4.5% dips | match |
| Ex 35.7 | 75.0%, 86.3%, 74.1%, 67.6%; total 289.0 | match |
| Ex 35.8 | CFADS 15.12 and 13.59; debt service 11.20; debt 97.42; cases 1.20x, 1.03x, 0.85x; break-evens 188.3 GWh, 200.7 GWh, USD 68.19/MWh | match |
| Ex 2.1 | 900.2; 4.94x; 4.02x; 127.8; 292.2; 97.4; 3.33x | match |
| Ex 2.4 | 13.83; 3.55%; 2.35; 50.4 bps; 6.4 bps; agency 2.6 bps | match |
| Ex 5.4 | annuity factor 9.53265; 12.11; 13.12; 15.12 | match |
| Ex 6.3 | bullet, annuity, and straight-line totals; WALs; first and last schedule rows | match |
| Ex 8.2 | ROE at 0, 50, 75, and 90% gearing in both asset-return cases | match |
| Ex 13.3 | 243.5 days; eight monthly accruals; final 1,167,000 | match |
| Ex 18.4 | 375,430 MWh; 23.051; 8.843; variant 266,555.0 MWh and 16.366 | match |
| Ex 20.2 | −38.700; 12.745; −25.955; 21.944 | match |
| Ex 29.1 | revenue 1.8187%; RAROC 10.76%; 11.34%; break-even margin 1.6789%; USD 1.14m, 0.48m, 5.69m | match |
| Ex 39.4 | 4.2437; 4.1856; 4.1741 | match |
| Ex 44.1 | 0.99917; 1.03194; 3.281%; 2.656; 1.913 | match |
| Ex 62.2 | 1.287x; 3.22; 1.177x | match |
| Ex 62.3 | 30.834; 96.13%; 89.78%; 30.758; 0.076; 84.81%; 1.779 | match |
| Ex 63.2 | PV 164.225; make-whole 14.225 (9.48%); 23.94; 5.15; nil | match |
| Ex 68.2 | floors 3,440 to 4,988; uplifts 260, 604, 776 | match |
| Ex 71.2 | 3,898.2 GWh; IRR 5.56% and 3.33%; USD 117.01 and 138.42/MWh | match |
| Ex 78.2 | 13.53 years; 9.47 years; 33.5% | match |
| Ex 81.2 | 41.97; 10.58; 67.15; 208.05; 0.3228; 1.25x; 0.2378; 0.5606; about 0.41 | match |
| Exercises 35.6 to 35.10, 36.6 to 36.8, 36.11, 36.12, 14.6, 14.7, 69.7, 61.9 | stated answers | match |
| Exercise 35.14 | 1.31x; 1.34x; 1.40x | mismatch: 1.31x; 1.33x; 1.39x (defect 10) |
