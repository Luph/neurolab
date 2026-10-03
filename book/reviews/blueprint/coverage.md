# Blueprint review: coverage lens

Reviewer lens: coverage (standards Section 4, the coverage map A to T; Section 4.P sector deep dives; Section 5 running-case requirements; Section 7 candidate real cases).
Date: 2026-10-03.
Files audited: `standards.md`; `bible/architecture.md`; `bible/ownership-resolutions.md` (as it bears on homes); `bible/briefs/u01.md` to `u17.md` (locked TOCs, coverage checks, clause, exhibit and real-case tables, fact-sheet requests); `bible/anchor-registry.md` (all `sec`, `ssec`, `cl`, `exh` labels); `bible/case-bible.md`, `case-bible-annex-p.md`, `case-bible-annex-tr.md` (Parts 1 to 6, characters, storyline by chapter); `bible/decisions.md`; `bible/fact-sheet-plan.md`; `facts/` (160 sheets).

## Verdict: FAIL

One blocking defect (a Section 5 running-case requirement is not met and no decision logs the deviation), five major defects, five minor defects.

Counts: blocking 1, major 5, minor 5.

The coverage map is in good shape overall. Every bullet of Section 4 A to T has a named home chapter, and every Section 7 candidate case has a fact sheet and one or more assigned sections (summary tables at the end of this report). The defects below are the places where an item has a home but is not taught in full, or where a Section 5 requirement or Section 4 T template has no source.

---

## Defects

### 1. Case P has no currency hedging (blocking)

- **Location:** `bible/case-bible.md` Part 1.6 "Hedging" ("No FX hedge: the tariff is USD-indexed..."); `bible/architecture.md` Case P summary ("interest-rate swaps and currency issues"); Case Bible Part 6 rows 37, 38, 40, 41, 59, 66; `model/inputs_case_p.json`.
- **Defect:** Standards Section 5 requires the primary case's lender group to come "with interest-rate and currency hedging." Case P has interest-rate swaps only. The Case Bible explicitly rules out any FX hedge, and no entry in `decisions.md` records or justifies the deviation. As a result the book's only cross-border running case never exercises a currency hedge: no hedge sizing, no hedge in the funding sheet, no MTM under the 2022 to 2024 devaluation, and no hedge accounting for one. The generic teaching in ssec:34.6.4, ssec:37.7.3 and ssec:16.6.2 has no running-case installment to apply it to. Case P does carry real exposure: the onshore EPC portion is fixed in KCR (USD 82.67 million at 519.4 KCR per USD, Case Bible 1.3), there is KCR VAT and a KCR VAT facility, and KCR operating costs follow.
- **Required fix:**
  1. Add a currency hedge to Case P in Case Bible 1.6 and log it as a new D-1xx decision. The recommended design is a strip of KCR/USD deliverable forwards (or a USD/KCR cross-currency swap) with UBK and one Castellan-group bank, traded at financial close (July 17, 2018). It covers the KCR-fixed onshore EPC payments and the VAT-facility drawdown and repayment profile through COD, under a CTA hedging-policy requirement to hedge a fixed share (for example 75% to 100%) of committed KCR construction costs. State tenor, notional profile, rate and credit charge as inputs.
  2. Add the inputs to `model/inputs_case_p.json`. Have the Case P modeler add the hedge to the Funding sheet (two-currency funding) and assign new figure IDs, for example P-F64+ (hedge notional and settlements, the hedge's effect on the USD cost of the onshore portion, and the MTM at the 2022 devaluation if any tail remains), with values recorded in `model/figure-ledger-case-p.md`.
  3. Amend Case Bible Part 6 so the hedge is scheduled:
     - Ch 37 row: the currency-hedging requirement in the term sheet, in sec:37.10.
     - Ch 38 row: its cost in the all-in cost.
     - Ch 40 row: the hedge in the Funding sheet, in ssec:40.1.4 "Local-currency costs".
     - Ch 59 row: the hedge's outcome against the devaluation, in sec:59.10.
     - Ch 66 row: the hedge's designation as a cash-flow hedge, in sec:66.12.
  4. Update the `architecture.md` Case P summary line to read "interest-rate swaps and a construction-period currency hedge."
  5. If the editor-in-chief instead keeps "no FX hedge," the standards text still requires currency hedging. The only alternative compliant fix is to give Case P a hedged KCR tranche at the 2025 refinancing: a cross-currency swap on a KCR bond tranche, in sec:63.10 and Ch 34's sec:34.10 installment. That change must be modeled and logged the same way.

### 2. The mandatory "due-diligence request lists" template has no home content (major)

- **Location:** `bible/briefs/u17.md` Matter 93 (row "Due-diligence request lists", home "Chapters 48 to 50 (and 47 for acquisitions)"); `bible/briefs/u10.md` Chapters 47 to 50; `bible/anchor-registry.md` exh:47.x to exh:50.x.
- **Defect:** Standards Section 4.T lists "due-diligence request lists" among the mandatory back-matter templates, and Matter 93's own checks forbid it from introducing content the chapters do not teach. The briefs for Chapters 47 to 50 specify no request list for any workstream. The only list-like artifacts are Framework 48.1 (scope matrix, exh:48.1), Framework 49.1 (red-flag grid) and Exercise 49.14, which asks for a KYC list for Groupe Talmé. No registered exhibit is a request list. Phase 6 therefore has nothing to compile.
- **Required fix:** Add a numbered request-list exhibit to each diligence chapter's practitioner's notebook. Append each as the chapter's next free exhibit label so existing labels do not move, and register them in `anchor-registry.md`:
  - Ch 48 sec:48.9: technical/IE, resource (wind and solar, hydrology, geothermal, mineral and hydrocarbon reserves), market and price-curve, traffic and demand request lists.
  - Ch 49 sec:49.9: legal and regulatory, insurance, model audit, tax and accounting, counterparty credit, and KYC, sanctions and anti-corruption request lists.
  - Ch 50 sec:50.12: E&S request list (ESIA, ESMS and ESMP, RAP, SEP and grievance log, labor and security, biodiversity, cultural heritage, monitoring reports).
  - Ch 47 sec:47.11: an acquisition (buy-side) data-room request list.

  Each list carries 20 to 40 items with the reason for each item, following the pattern of Framework 85.2. Update Matter 93's row to cite these exhibit labels.

### 3. Original clause language is missing for several Section 4.D contracts (major)

- **Location:** `bible/anchor-registry.md` clause labels for Chapters 21 and 23 to 26; `bible/briefs/u06.md` (Ch 23 to 26); `bible/briefs/u05.md` (Ch 21).
- **Defect:** Section 4.D says that for each contract the book gives "purpose, structure, key clauses, market positions, ... negotiation dynamics ... and original illustrative clause language." Section 7 adds that where negotiation matters, the clause shows sponsor-, lender- and government-friendly variants. The registry shows contracts that are taught with no clause at all:
  - **Ch 24:** only cl:24.1 (O&M availability guarantee). There is no clause for the long-term service agreement, the core OEM contract that Case P negotiates with Bergmark (EOH-based fees, availability and heat-rate guarantees, end-of-term cliff), and none for the asset management agreement (sec:24.4, a single section with no subsection).
  - **Ch 25:** only cl:25.1 (GSA take-or-pay). There are no clauses for the grid connection agreement (sec:25.5), land rights (sec:25.7; lender protections such as mortgageability, non-disturbance and step-in), water supply (sec:25.4) or the shipper-side transportation agreement (sec:25.3).
  - **Ch 26:** cl:26.1 (ROFR) and cl:26.2 (financial completion definition) only. There is no clause for the equity contribution agreement (sec:26.4; acceleration on default and LC support), the completion guarantee's operative obligation (sec:26.5), or the co-development agreement (sec:26.2; funding default and dilution).
  - **Ch 23:** no EPCM clause (sec:23.5; the EPCM contractor's standard of care and liability cap are the negotiation point).
  - **Ch 21:** no clause for airport charges or a port concession's minimum annual guarantee (sec:21.8), or for a royalty (ssec:21.5.1).
- **Required fix:** Append the following clause specifications to the briefs and register the labels. Each clause is Illustrative, annotated line by line, and where negotiated carries variants a, b, c with a landing paragraph:
  - cl:24.2: LTSA fees and guarantees (EOH and starts-based fee, availability and heat-rate guarantees with LD caps), with sponsor, lender and OEM variants, placed in ssec:24.3.3.
  - cl:24.3: asset management agreement scope and termination for underperformance, in sec:24.4.
  - cl:25.2: grid connection agreement, connection date and remedy for late energization (ssec:25.5.2).
  - cl:25.3: land lease lender-protection provisions (ssec:25.7.2).
  - cl:25.4: water supply or abstraction quantity and curtailment priority (ssec:25.4.2).
  - cl:26.3: equity contribution undertaking with acceleration (ssec:26.4.2).
  - cl:26.4: completion guarantee, the guarantor's obligation and release (ssec:26.5.3).
  - cl:26.5: co-development funding default and dilution (ssec:26.2.2).
  - cl:23.3: EPCM standard of care and liability cap (ssec:23.5.2).
  - cl:21.8: port minimum annual guarantee and throughput fee (ssec:21.8.2).

  Update each chapter's exercise set with one drafting task that uses a new clause.

### 4. Several Section 4.P sector deep dives lack the "landmark deals and failures" element, and some lack verified financing terms (major)

- **Location:** `bible/briefs/u15.md` Chapters 73, 75, 76 (real-case tables and fact-sheet request list, lines about 2286 to 2301); `bible/briefs/u16.md` Chapters 80, 81, 82 (fact-sheet requests); anchor-registry TOCs for Chapters 72, 73, 75, 76, 80, 81, 82.
- **Defect:** Section 4.P requires each sector to have "industry economics, how the asset works, revenue models, key risks, the contract set, typical financing terms, modeling specifics, landmark deals and failures." The locked TOCs and real-case tables leave these sectors without any landmark deal or failure:
  - **FPSOs:** sec:76.8 has no real case. `fpso-financing` exists but appears only in the request list.
  - **Regasification and FSRUs:** sec:76.7 has no real case. `fsru-charters` and `coral-sul-flng` exist but are unplaced.
  - **Upstream oil and gas:** the only upstream case is Chad–Cameroon's equity-funded upstream (ssec:75.5.2). `upstream-field-pf` (Jubilee), `commodity-prepay`, `t-rbl` and `tap-pipeline` exist but are unplaced. ssec:75.6.1 says "No verified RBL norms," although `t-rbl` now supplies them.
  - **Transmission and interconnectors:** sec:73.4 and sec:73.5 have no landmark deal or failure. The only item is the Dogger Bank OFTO advance (ssec:73.4.3). `t-cap-and-floor` exists, and the requested `t-interconnector-cap-floor` was not produced.
  - **Pumped storage (Section 4.P "other storage"):** `pumped-storage` (Snowy 2.0 cost growth from about AUD 3.8 to 4.5 billion to AUD 12 billion) exists but is unplaced. ssec:73.3.3 cites only the GB LDES window.
  - **Waste-to-energy:**
    - sec:81.4 makes no real-case claims ("no real-case claims without fact sheet wte").
    - ssec:81.7.1 has no WtE financing anchor.
    - The delivered `wte` sheet covers the English waste PFI pre-construction failures (Norfolk Willows, terminated at GBP 33.7 million; EnviRecover) but no project-financed operating WtE plant. Its "Do not state" list bars Riverside, Warsan and the Manchester and Merseyside PFIs.
  - **Airports and ports:** `airport-concession` (LaGuardia Terminal B) and `port-concession` (Lekki) were delivered, but sec:80.2 and sec:80.3 carry no named real-case section. Placement is conditional in the brief.
  - **Water concessions:** `municipal-water-concession` (Manila) is delivered but unplaced. ssec:81.2.1 and ssec:81.2.2 have no real case; Tideway (sec:81.10) is a carve-out from a utility, not a concession.
  - **Geothermal:** `geothermal-risk-facilities` (GRMF, the Turkey contingent grant, GREM, Kenya's steam-sales model) is unplaced. Geothermal's revenue model and public drilling-risk instruments are therefore taught without a verified case beyond Sarulla.
  - **Offshore wind:** `vineyard-wind-2024` (serial blade failure) and `us-offshore-wind-2025` are unplaced, although ssec:71.4.3 "Serial defects and cables" and ssec:71.7.3 "US offshore wind and tax credits" need them.
  - **Battery safety:** `t-storage-safety` is unplaced; the ssec:73.2.3 walkthrough step 2 says to state no standard "unless a fact sheet verifies it."
- **Required fix:** Issue a "sector placement addendum" to u15 and u16. It may be a section appended to `ownership-resolutions.md` or a new `bible/briefs/u15-u16-addendum.md` cited from the architecture. For each item it assigns the fact sheet to a named subsection, states the angle and lesson in one line, and adds a real-case row to the chapter's real-case table:
  - `fpso-financing` to ssec:76.8.2 to 76.8.4.
  - `fsru-charters` to ssec:76.7.2.
  - `coral-sul-flng` to ssec:76.6.1 or a new ssec:76.8.5 "Floating LNG" (appended).
  - `upstream-field-pf` and `t-rbl` to ssec:75.3.5 and 75.6.1.
  - `commodity-prepay` to ssec:75.3.5.
  - `tap-pipeline` to ssec:75.5.1.
  - `t-cap-and-floor` to ssec:73.5.2 and 73.6.2, with one named interconnector under the Ofgem regime as the landmark.
  - `pumped-storage` to ssec:73.3.3, as the failure-and-reset case for long-duration storage construction risk.
  - `geothermal-risk-facilities` to ssec:72.5.2 and 72.5.5.
  - `vineyard-wind-2024` to ssec:71.4.3.
  - `us-offshore-wind-2025` to ssec:71.5.3 and 71.7.3.
  - `t-storage-safety` to ssec:73.2.3.
  - `airport-concession` to ssec:80.2.3 and 80.7.1.
  - `port-concession` to ssec:80.3.3 and 80.7.1.
  - `municipal-water-concession` to ssec:81.2.2, as the currency-mismatch water concession.
  - `wte` (Willows) to ssec:81.4.3 and 81.5.1, as the WtE pre-construction failure and its termination cost.

  For WtE, also commission one fact sheet on a project-financed operating EfW plant with verified financial close and terms, and place it in ssec:81.7.1. If none can be verified, record in ssec:81.7.1 that WtE financing terms are taught as D-011 indicative ranges, and state that Willows is the sector's landmark failure.

### 5. Second-wave fact sheets are not recorded in the fact-sheet plan, and ratings methodology is taught without the agencies' frameworks (major)

- **Location:**
  - `bible/fact-sheet-plan.md`, which lists only about 74 first-wave sheets; `facts/` now holds 160.
  - `bible/briefs/u07.md` Ch 30 sec:30.5 ("No agency quotes"), where `t-ratings-2` is referenced by no brief.
  - Brief requests that were never delivered: `t-repowering` ("needed", u13 for Ch 62 and Ch 65), `t-ppp-norms` (u16 Ch 81), `t-refi-repricing-norms` and `t-operating-waivers` (u13), `subsea-cable` (u16 Ch 82), `chile-lpvr` and `t-airport-regulation` (u16; partly substituted by `chile-concessions` and `t-airport-port-revenue`).
- **Defect:** Section 4.F requires "Ratings: how agencies analyze projects in construction and in operation." Chapter 30's brief teaches this generically: questions an analyst asks and a rating-case stress ladder built on one DBRS-rated example. Earlier, t-ratings was partial (Fitch only). `t-ratings-2` now verifies S&P's methodology in full and Moody's at medium confidence, but no brief uses it. A practitioner would expect the actual agency frameworks: S&P's construction-phase and operations-phase SACP, the operations-phase business assessment, DSCR-threshold financial assessment, modifiers and the sovereign and counterparty caps; Fitch's attribute-based approach; and Moody's scorecard factors. Separately, the fact-sheet plan does not record the roughly 86 second-wave sheets or their chapters. Writers and fact-checkers therefore cannot see from the plan which sheet serves which section, and briefs that wrote "if fact sheet X exists" were never updated.
- **Required fix:**
  1. Amend the Ch 30 brief:
     - ssec:30.5.2 and ssec:30.5.3 teach S&P's construction-phase and operations-phase analysis from `t-ratings-2` and Fitch's attribute approach from `t-ratings`, with Moody's labeled at the confidence the sheet gives.
     - Add Exhibit 30.x (appended label): a side-by-side table of how two agencies rate one project in construction and in operation.
     - Example 30.4 applies one agency's operations-phase DSCR thresholds.
     - Keep the "no agency quotes" rule (paraphrase only).
  2. Rewrite `fact-sheet-plan.md` to list all 160 sheets with subject, main chapters and assigned sections. Mark every brief request not delivered as either "superseded by <slug>" or "not delivered: teach as D-011 indicative or Illustrative."
  3. Commission `t-repowering`, which u13 marks as needed for ssec:62.8.1, sec:65.4 and Case R's R1 repower-or-retire in sec:65.8. Otherwise amend those sections to teach repowering economics as Illustrative with no market facts.

### 6. Taxonomies are taught for the EU only (minor)

- **Location:** `bible/briefs/u14.md` Ch 84, sec:84.3; `architecture.md` Ch 84 row ("taxonomies (EU and others)").
- **Defect:** Section 4.Q lists "taxonomies" (plural), and the architecture assigns "EU and others." The brief's TOC treats only the EU Taxonomy and the EuGB. A reader working on a non-EU deal (the book's primary case is in West Africa; Case R is in the US) gets no non-EU reference point and no account of interoperability.
- **Required fix:** Append ssec:84.3.5 "Other taxonomies and interoperability". Cover two or three non-EU taxonomies verified in a `t-sustainable-finance-2` sheet (queued in the tracker, not yet delivered), for example China's green bond catalogue and a regional taxonomy such as ASEAN's, plus the Common Ground Taxonomy concept. Add one exercise mapping a project across two taxonomies. If the sheet cannot be produced, state the existence of non-EU taxonomies only at the level the existing `t-sustainable-finance` sheet verifies.

### 7. "Hedging under ISDA" is covered only at overview level (minor)

- **Location:** `bible/briefs/u11.md` ssec:51.1.4; related ssec:20.7.2, ssec:37.7.4, sec:53.5, ssec:64.7.4.
- **Defect:** Section 4.J lists "hedging under ISDA" as part of the document set the reader must be able to work with, and capability 6 requires marking up finance documents. ssec:51.1.4 gives "master agreement, schedule and confirmations at the level a financier needs" with no clause and no walkthrough. The project-finance-specific schedule elections are not taught anywhere: additional termination events tied to loan acceleration and prepayment; no CSA and secured pari passu status instead; restrictions on transfer and novation; close-out amount and its ranking; and the hedge counterparty's limited events of default. Pieces are scattered across four chapters.
- **Required fix:** Expand ssec:51.1.4 to teach the project-finance schedule elections. Add Clause 51.x (appended label), an Illustrative additional termination event linked to mandatory prepayment and acceleration, with hedge-bank-friendly and sponsor-friendly variants. Cross-reference sec:53.5 for ranking and ssec:63.2.2 and 64.7.4 for breakage and close-out. Add one exercise.

### 8. Repowering and life-extension teaching has no fact base (minor)

- **Location:** `bible/briefs/u13.md` ssec:62.8.1 and sec:65.4 (fact-sheet request `t-repowering`, marked "needed"); Case Bible Part 6 row 65 (R1 repower or retire).
- **Defect:** Section 4.N names "asset optimization (repowering, life extension, hybridization)." The requested sheet was not produced, and the existing sheets mention repowering only incidentally. The sections can teach the economics, but not current practice: US repowering credit requalification, European repowering permitting rules, life-extension certification.
- **Required fix:** Covered by fix 5(3). In addition, label the R1 repowering figures in sec:65.8 as Case R model outputs only, and do not state market practice in ssec:62.8.1 or ssec:65.4.1 beyond what `t-eu-support-schemes` and `t-us-tax-credits` verify.

### 9. Telecoms coverage omits subsea cables and other non-tower, non-fiber telecom assets (minor)

- **Location:** `bible/briefs/u16.md` Ch 82 (TOC and the optional `subsea-cable` request, not delivered).
- **Defect:** Section 4.P lists "telecoms, fiber, towers, and data centers." Chapter 82 covers towers, fiber and data centers well, but "telecoms" beyond these is absent. Subsea cables are financed on capacity pre-sales and IRUs with consortium and DFI structures, a project-finance pattern different from towers and fiber.
- **Required fix:** Append ssec:82.3.4 "Subsea cables and capacity pre-sales," covering IRU pre-sales as revenue contracts, consortium versus private-cable models, and DFI participation. Commission the `subsea-cable` sheet for one verified financing. If it cannot be verified, teach the subsection with a labeled Illustrative example.

### 10. Case T's recurring cast lacks lenders' counsel, sponsor's counsel and an independent engineer (minor)

- **Location:** `bible/case-bible.md` Part 4.2; `bible/case-bible-annex-tr.md` T.5 and T.16; Part 6 rows 58, 64, 79.
- **Defect:** Section 5 asks for recurring characters (developer, lead arranger, sponsor's counsel, lenders' counsel, government official, EPC project director, independent engineer) "so the reader experiences every negotiation from every seat." Case P has all seven. Case T, which carries the common-law documentation, the restructuring plan and the cram-down (Ch 64), has no lenders' counsel, no sponsor's counsel and no independent engineer or traffic-monitoring engineer. Its D&C project director (Dimitri Kalogeropoulos) appears only in Ch 23. The restructuring negotiation in sec:64.14 therefore has no lawyer's seat, and the ramp-up in sec:79.14 has no lenders' technical seat.
- **Required fix:** Add two Ardmorean characters to annex TR, with name checks, sheets, verbal habits and where-wrong notes per Case Bible conventions:
  - lenders' counsel, appearing at close (sec:58.13) and in the restructuring plan (ssec:64.14.5);
  - the lenders' technical and traffic monitoring adviser, appearing in sec:79.14 and ssec:64.14.1.

  Amend Part 6 rows 58, 64 and 79 accordingly.

---

## Coverage map audit (Section 4 A to T): where each bullet is taught

Status key: Full = taught in full at a named home. Partial = home exists but an element is missing (defect number given).

| Item | Home chapter and sections | Status |
|---|---|---|
| A Money and time | Ch 5 (sec:5.1 to 5.10) | Full |
| A Debt basics | Ch 6 (sec:6.1 to 6.8); sculpting math Ch 36 | Full |
| A Accounting from zero | Ch 7 | Full |
| A Corporate finance essentials | Ch 8 | Full |
| A Probability | Ch 9 | Full |
| A Law for financiers | Ch 10 (sec:10.1 to 10.9) | Full |
| A How the assets work | Ch 11 (power, grids, markets), Ch 12 (resources, transport, social, digital) | Full |
| A Excel | Ch 13 | Full |
| B Essence; neighbors; why and cost | Ch 2 | Full |
| B History | Ch 3 (PFI detail sec:57.8) | Full |
| B Cast; lifecycle | Ch 4 | Full |
| C Taxonomy | Ch 14 (sec:14.3 to 14.19, every listed category) | Full |
| C Method, matrix, bankable, pass-through, paper vs practice, asymmetry | Ch 15 | Full |
| C Mitigation toolkit | Ch 16 | Full |
| D Concessions and government support | Ch 17 | Full |
| D Offtake and revenue (all listed forms) | Ch 18, 19, 20, 21 | Full, except clauses missing for airport and port charges and royalties (defect 3) |
| D Construction | Ch 22, 23 | Full, except no EPCM clause (defect 3) |
| D Operations | Ch 24 | Partial: no LTSA or AMA clause (defect 3) |
| D Inputs and access | Ch 25 | Partial: no grid, land, water or GTA clause (defect 3) |
| D Corporate and sponsor | Ch 26 | Partial: no ECA, completion-guarantee or co-development clause (defect 3) |
| D Insurance | Ch 27 (PRI detail Ch 60) | Full |
| D Direct agreements; contract map, gap scan, "Who pays if...?" | Ch 28 | Full |
| E Debt providers | Ch 29; capital rules Ch 68 | Full |
| E Capital markets | Ch 30; sukuk Ch 33; labels Ch 84 | Full |
| E Other facilities | Ch 31 | Full |
| E Equity (incl. US tax equity, dated) | Ch 32; tax constraints sec:67.10 | Full |
| E Islamic | Ch 33; ICA sec:53.8 | Full |
| E Blended, concessional, local currency | Ch 34 | Full |
| F Mathematics and judgment | Ch 35, 36, 37 | Full |
| F Pricing | Ch 38 | Full |
| F Ratings | sec:30.5 | Partial: agency frameworks not taught (defect 5) |
| G Modeling course | Ch 39 to 44 | Full |
| G Sector-specific modeling | Ch 45, plus each sector chapter's modeling section | Full |
| G Cell-by-cell and companion model | Ch 13, 39 to 43; `model/` | Full |
| H Equity, valuation, investment decisions | Ch 46, 47 | Full |
| I Due diligence (all workstreams) | Ch 48, 49, 50 (model audit method Ch 44) | Full (request lists missing; see defect 2 under T) |
| J Document set and clauses | Ch 51 | Full, except ISDA at overview level (defect 7) |
| J Security; accounts and waterfall | Ch 52 | Full |
| J Intercreditor | Ch 53 | Full |
| J Governing law, disputes, treaties | Ch 54 | Full |
| J LMA, LSTA, APLMA | ssec:51.1.5 | Full |
| K Deal process | Ch 55 | Full |
| K Negotiation | Ch 56 | Full |
| L PPPs | Ch 57, 58 (applied Ch 79 to 81) | Full |
| M International and emerging markets | Ch 59, 60 (law Ch 54) | Full |
| N Construction | Ch 61 | Full |
| N Operations | Ch 62 | Full; repowering lacks a fact base (defect 8) |
| N Refinancing, secondary sales, holdco leverage | Ch 63 | Full |
| N Distress, restructuring, enforcement | Ch 64 | Full |
| N Decommissioning, handback, end of life | Ch 65 | Full |
| O Accounting | Ch 66 | Full |
| O Tax | Ch 67 | Full |
| O Regulation of capital providers | Ch 68 | Full |
| P Sector deep dives | Ch 69 to 83 | Partial for FPSOs, regas and FSRU, upstream, transmission and interconnectors, pumped storage, WtE, airports, ports, water, telecoms (defects 4, 9) |
| Q E&S standards, engagement, resettlement, FPIC, biodiversity, labor, credit risk | Ch 50 | Full |
| Q Climate risk, labeled debt, taxonomies, transition, carbon, greenwashing | Ch 84 | Partial: EU taxonomy only (defect 6) |
| R Financier's craft | Ch 85, 86, 87 | Full |
| S Frontier | Ch 88 (sector-level teaching in Ch 73, 74, 78, 82, 83) | Full |
| T Front matter | Matter 00 (how to use, study plan, exercises, model builds, caveat) | Full |
| T Back matter: glossary, formula sheet with Excel, index of cases, capstone, exam | Matter 91, 92, 94, 89, 90 | Full |
| T Back matter: templates | Matter 93 | Partial: DD request lists have no source (defect 2) |

## Sector deep dives (Section 4.P): the eight required elements

Elements: economics (Ec), asset (As), revenue (Rv), risks (Rk), contract set (Ct), financing terms (Fn), modeling (Md), landmark deals and failures (Lm).

| Sector | Chapter | Ec | As | Rv | Rk | Ct | Fn | Md | Lm |
|---|---|---|---|---|---|---|---|---|---|
| Thermal power | 69 | Y | Y | Y | Y | Y | Y | Y | Y (Dabhol, Paiton, Mundra, Hub, Azura, Gulf) |
| Onshore wind; solar | 70 | Y | Y | Y | Y | Y | Y | Y | Y (REIPPPP, Chile, Lake Turkana, Ivanpah, Noor) |
| Offshore wind | 71 | Y | Y | Y | Y | Y | Y | Y | Y (Dogger Bank, Ocean Wind); Vineyard Wind unplaced (4) |
| Hydropower | 72 | Y | Y | Y | Y | Y | Y | Y | Y (NT2, Bujagali) |
| Geothermal | 72.5 | Y | Y | thin | Y | Y | Y | Y | Sarulla only; drilling-risk facilities unplaced (4) |
| Battery and other storage | 73 | Y | Y | Y | Y | Y | Y | Y | Moss Landing; pumped storage case unplaced (4) |
| Nuclear (RAB, CfD) | 74, 19 | Y | Y | Y | Y | Y | Y | Y | Y (HPC, SZC, Vogtle, Barakah) |
| Transmission and interconnectors | 73.4 to 73.7 | Y | Y | Y | Y | Y | indicative | Y | No (4) |
| Upstream (RBL) | 75 | Y | Y | Y | Y | Y | Y (t-rbl unplaced) | Y | No financed upstream case placed (4) |
| Midstream | 75.4 to 75.5 | Y | Y | Y | Y | Y | Y | Y | Chad–Cameroon, Nord Stream 2; TAP unplaced (4) |
| LNG liquefaction | 76 | Y | Y | Y | Y | Y | Y | Y | Y (Sabine, PNG, Ichthys, Mozambique, Arctic LNG 2) |
| Regasification and FSRU | 76.7 | Y | Y | Y | Y | Y | thin | Y | No (4) |
| FPSOs | 76.8 | Y | Y | Y | Y | Y | thin | Y | No (4) |
| Refining and petrochemicals | 77 | Y | Y | Y | Y | Y | Y | Y | Y (Sadara, Duqm) |
| Mining and metals; critical minerals | 78 | Y | Y | Y | Y | Y | Y | Y | Y (Oyu Tolgoi, Cobre Panamá) |
| Toll roads, bridges, tunnels | 79 | Y | Y | Y | Y | Y | Y | Y | Y |
| Rail and urban transit | 80 | Y | Y | Y | Y | Y | Y | Y | Y (Metronet, Purple Line) |
| Airports | 80.2 | Y | Y | Y | Y | Y | Y | Y | Fact sheet delivered, no section placement (4) |
| Ports | 80.3 | Y | Y | Y | Y | Y | Y | Y | Fact sheet delivered, no section placement (4) |
| Social infrastructure | 81 | Y | Y | Y | Y | Y | indicative | Y | Y (Carillion, UK PFI) |
| Water and desalination | 81.2 to 81.3 | Y | Y | Y | Y | Y | Y | Y | Desal Y (Gulf); water concession unplaced (4) |
| Waste-to-energy | 81.4 | Y | Y | Y | Y | Y | none | Y | No (4) |
| Telecoms, fiber, towers, data centers | 82 | Y | Y | Y | Y | Y | Y | Y | Y (Hyperion, tower carve-out, FTTH); subsea absent (9) |
| Hydrogen and derivatives | 83 | Y | Y | Y | Y | Y | Y | Y | Y (NEOM) |
| CCS | 83 | Y | Y | Y | Y | Y | Y | Y | Y (Northern Lights) |
| Sustainable fuels | 83 | Y | Y | Y | Y | Y | Y | Y | Y (saf-project) |
| Manufacturing (gigafactory) | 77 | Y | Y | Y | Y | Y | Y | Y | Y (Northvolt) |

## Section 5 running-case requirements: scheduling check

| Requirement | Chapter(s) scheduled | Status |
|---|---|---|
| Case P: emerging-market greenfield contracted power; state utility offtaker; EPC; O&M; banks, ECA, DFI | Case Bible Part 1; Ch 29 | Met |
| Case P: interest-rate hedging | Ch 6, 37, 63 (unwind) | Met |
| Case P: currency hedging | none | **Not met (defect 1)** |
| Origination and development | Ch 1 (close), 2, 4 | Met |
| Competitive procurement | Ch 17 (tender), Ch 47 (bid) | Met |
| Contract negotiation | Ch 10, 17, 18, 22, 24, 25, 26, 27 | Met |
| Due diligence | Ch 48, 49, 50 | Met |
| Model build | Ch 13, 39 to 44 | Met |
| Debt sizing | Ch 35, 36 | Met |
| Term-sheet negotiation | Ch 56 | Met |
| Financial close | Ch 55 | Met |
| Construction delay and cost overrun | Ch 61 (ssec:61.15.1 to 61.15.4) | Met |
| Insurance claim | Ch 61 (ssec:61.15.3) | Met |
| Completion testing | Ch 61 (ssec:61.15.5) | Met |
| Operations | Ch 7, 62 | Met |
| Offtaker payment crisis and currency shock | Ch 59 | Met |
| Covenant breach and waiver | Ch 62 | Met |
| Refinancing | Ch 63 | Met |
| Partial sale | Ch 63 (accounting Ch 66, tax Ch 67) | Met |
| Case T: decision to procure | Ch 57 | Met |
| Case T: bid | Ch 47, 58 | Met |
| Case T: financial close | Ch 58 (sec:58.13) | Met |
| Case T: ramp-up | Ch 45, 79 | Met |
| Case T: distress and restructuring | Ch 64 | Met |
| Case T: public-sector view, demand risk, PPP mechanics | Ch 21, 57, 58, 68, 80, 81 | Met |
| Case R: acquisitions | Ch 47 (A1), Ch 73 (A2, A3) | Met |
| Case R: valuation | Ch 46 | Met |
| Case R: hedging | Ch 20 | Met |
| Case R: holdco financing | Ch 31, 63 | Met |
| Case R: refinancing | Ch 63 | Met |
| Recurring characters: developer (Tomasz), lead arranger (Pieter), sponsor's counsel (Adaeze), lenders' counsel (Laurent), government officials (Abdoulaye, Clémentine), EPC project director (Konrad), IE (Gwen) | Case P across Ch 1 to 88 | Met for Case P; Case T lacks three seats (defect 10) |
| Every chapter has an installment | Case Bible Part 6 rows 1 to 88 (D-112) | Met |

## Section 7 candidate real cases: where each is taught

All 35 candidates have a fact sheet and at least one dedicated section or subsection. None is used only in passing.

| Case | Main sections |
|---|---|
| Eurotunnel | sec:3.4; ssec:64.11.3; sec:79.11 |
| Dabhol | ssec:3.3.2; sec:17.7; sec:59.6; ssec:69.8.1; sec:85.7 |
| Paiton I | ssec:3.3.3; sec:59.7; ssec:69.8.2 |
| Hub Power | ssec:3.3.1; sec:17.6; ssec:69.8.4; Ch 60 |
| Nam Theun 2 | ssec:50.3.4, 50.5.3; ssec:72.7.1; Ch 28 (one paragraph on MIGA cover) |
| Chad–Cameroon | sec:50.9; ssec:75.5.2 |
| Sadara | sec:33.7; sec:77.10 |
| Gulf IWPP programs | ssec:47.1.3; ssec:69.8.4; sec:81.11 |
| Sabine Pass | ssec:2.3.3; sec:21.10; sec:22.9; Ch 76 |
| PNG LNG, Ichthys | sec:29.9; ssec:61.11.4; Ch 76 |
| Mozambique LNG | ssec:76.5.1; Ch 60 |
| Oyu Tolgoi | ssec:12.3.5; sec:67.12; sec:78.9 |
| Tata and Adani Mundra | sec:10.6; sec:18.8; sec:25.10; ssec:69.8.3 |
| Argentina 2002 | sec:59.8; Ch 54, 60 |
| Spain retroactive cuts | sec:19.3; ssec:54.5.3 |
| Chile northern solar | sec:11.13; sec:20.9; sec:35.7; ssec:70.8.2 |
| Winter Storm Uri | sec:20.8; ssec:70.4.5 |
| Lake Turkana | sec:17.7; sec:18.9; sec:25.6; ssec:28.6.3; ssec:70.8.3; sec:85.6 |
| REIPPPP | sec:17.7; ssec:57.6.2; ssec:58.2.3; ssec:70.8.1 |
| Indiana Toll Road, SH 130 | sec:37.8; ssec:47.2.5; ssec:64.8.2; ssec:64.9.4; sec:79.9 |
| Sydney Cross City and Lane Cove | sec:28.4; ssec:48.5.4; ssec:64.8.3; sec:79.10; sec:86.7 |
| Dulles Greenway | ssec:42.4.4; ssec:64.4.4; sec:79.11 |
| Metronet | sec:24.8; ssec:57.5.4; sec:80.9 |
| Carillion | sec:22.9; sec:23.11; sec:61.9; sec:81.9; sec:87.10 |
| Purple Line | sec:28.7; sec:61.10; sec:80.10 |
| Port of Miami Tunnel | ssec:58.8.2 |
| Thames Tideway | sec:19.8; sec:81.10; sec:84.9 |
| Hinkley Point C, Sizewell C | sec:19.5; sec:19.8; ssec:74.3.1, 74.3.2 |
| Ocean Wind 1 and 2 | sec:71.5 |
| SunEdison and TerraForm | ssec:2.1.3; sec:32.8; ssec:63.7.3; sec:66.10 |
| Ivanpah | sec:3.7; ssec:62.6.3; ssec:70.8.4; ssec:88.3.4 |
| Northvolt | sec:77.11; ssec:88.3.4 |
| UK PFI | sec:3.5; sec:46.5; sec:57.8; ssec:65.3.4; ssec:81.7.3 |
| COVID-19 and transport concessions | ssec:79.6.4; sec:80.11; ssec:81.5.4; Ch 64 |
| Sanctions since 2022 | ssec:60.7.2; ssec:75.5.3; ssec:76.5.2 |

Additional regions and recent deals beyond the list are adequately represented: Colombia 4G, Cobre Panamá, Azura-Edo, Bujagali, Noor Ouarzazate, Sarulla, NEOM, Northern Lights, Dogger Bank, Hyperion, Moss Landing and Odebrecht. Once defect 4 is fixed, Jubilee, Lekki, LaGuardia, Manila Water and Snowy 2.0 are added.
