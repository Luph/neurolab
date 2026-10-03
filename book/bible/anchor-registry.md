# Anchor registry

Status: canonical, 2026-10-03. Compiled by the architecture editor from the anchors, tables of contents, worked-example, exhibit, clause and equation specifications of the 17 unit briefs (`bible/briefs/u01.md` to `u17.md`), with the fixes ordered in `bible/ownership-resolutions.md` (rulings R-128 to R-136 and the label consequences of other rulings). Rulings take precedence over briefs.

Totals: 5240 labels (91 ch, 1384 sec, 2038 ssec, 572 ex, 589 exh, 159 cl including clause variants, 254 eq, 153 fw), plus 8 front-matter labels.

## 1. How to use this registry

1. Cite only labels listed here (style sheet 3.4). A label of another chapter prints "??" in a standalone build; that is expected. A label missing from this registry is reported in the status note, never invented.
2. Section and subsection titles are the briefs' locked TOC headings. Writers may polish wording but must keep numbering; any change of number is a registry change and goes through the editor-in-chief.
3. Examples, exhibits, clauses and equations are numbered in order of appearance within the chapter. Where the Note column says "implied", the brief describes the object without declaring a label; the writer assigns the label shown, in order of appearance, and reports the final list.
4. Clause variants (`cl:N.Ka`, `cl:N.Kb`, ...) exist only inside a `clausevariants` group whose parent is `cl:N.K`. No other label carries a letter suffix.
5. Exercise labels (`exr:N.K`) run from 1 in each chapter and are not listed individually; they may be cited only inside their own chapter and by matter file 93 (checklists and templates).
6. A later chapter may display a formula owned elsewhere only as a model row or a specialized application; its equation caption says so and cites the home equation (ruling R-133). Repurposed captions are marked in the Note column.
7. Frameworks are numbered within their home chapter (Framework 28.2). Only the home chapter sets the `framework` box; others `\cref` it.
8. Front matter uses unnumbered headings with `fm:` labels (ruling R-106); matter Chapters 89 to 94 use the chapter scheme.

## 2. Duplicates, collisions and fixes

| # | Problem found | Fix (binding) |
|---|---|---|
| A1 | Ch 86 brief declares "Exhibit 86.2a" (case table) and then "Exhibit 86.2" (tornado); credit-paper Part 10 has an unnumbered exhibit; Part 6 is "inside Exhibit 86.11 or a separate exhibit". | Renumber Ch 86 exhibits as listed under Chapter 86 below: case table becomes exh:86.2; every later exhibit moves up by one; Part 5 and Part 6 share exh:86.12; Part 10 gets exh:86.17; the 2026 hindsight table becomes exh:86.19. No letter suffixes (R-130). |
| A2 | u14 (Ch 66 assumed list) cites `sec:6.x`, a placeholder. | Read `sec:6.8` (swaps) and `ssec:6.8.3` (valuing a swap and breaking it). |
| A3 | Two equations define WAL (eq:6.2, eq:29.3, eq:36.5); two define bond price (eq:6.5, eq:30.1); YTM is eq:38.6 as well as Ch 6; levelization appears as eq:5.11, eq:47.1, eq:11.6, eq:83.1 and eq:88.2; minimum margin is eq:38.1 and eq:68.1; spark spread is eq:11.7 and eq:69.2; make-whole is eq:30.2 and eq:63.2; RAROC is eq:29.1 and eq:86.1. | Home equations: eq:6.2 (WAL), eq:6.5 (bond price and YTM), eq:5.11 (levelized price), eq:11.6 (LCOE as an instance of eq:5.11), eq:83.1 (LCOH), eq:38.1 (minimum margin), eq:11.7 (clean spark spread), eq:30.2 (make-whole), eq:29.1 (RAROC). The later labels keep their numbers (no renumbering) but are repurposed to the chapter-specific application named in the Note column (R-133). |
| A4 | Model-row equations restate owned formulas: eq:42.3, eq:42.4, eq:42.5, eq:43.1, eq:45.3, eq:45.5. | Captions changed to "... row, implementing eq:X"; the model chapter does not re-derive the formula. |
| A5 | Headings duplicate home headings in later chapters: ssec:30.3.1 ("Coupon, price, and yield", duplicating ssec:6.7.1), ssec:30.3.2 and ssec:36.9.1 (WAL, duplicating ssec:6.3.2), sec:65.5 and ssec:65.5.2 ("Terminal value", duplicating ssec:46.4.3), ssec:68.5.1 ("The minimum margin", duplicating ssec:38.1.1), ssec:80.2.2 ("Single till and dual till", duplicating ssec:21.8.1), ssec:6.8.2 (credit and execution charge, owned by ssec:38.4.1). | Retitled as shown in the chapter tables (R-004, R-005, R-007, R-014, R-050, R-076). |
| A6 | Framework names collide: Framework 87.3 "integrity check" against Framework 43.2 "integrity-check catalogue" (model checks). | Framework 87.3 becomes "The integrity test", slug `fw:integrity-test` (R-129). |
| A7 | Framework 79.1 (`fw:demand-risk-menu`) teaches instruments owned by Ch 57 and Ch 58. | Kept as a sector selection tool, renamed "Demand-risk sharing menu for toll roads"; it cites ssec:57.5.1 and ssec:58.1.3 for mechanics (R-047). |
| A8 | New subsections required by rulings. | `ssec:27.3.4` Cyber cover for operating assets; `ssec:62.5.4` Operational-technology cyber controls and reporting; `ssec:66.4.7` Decommissioning provisions and asset retirement obligations. Each is appended after the last existing subsection, so no existing label moves. |
| A9 | Briefs for Chapters 5 to 9, 15, 67, 68, 84 and 86 describe some exhibits and clauses without declaring labels (for example "Exhibit 5.3", "Exhibit 7.1", "Clause 15.1", "Clause 67.1"). | Listed below as implied labels; writers assign them in order of appearance. |
| A10 | Placeholder strings in briefs (`cl:N.K`, `eq:N.K`, `sec:N.M`, `ch:NN`, `fm:slug`, `ex:89.K`, `exh:89.K`) and range notation (`ex:1.1 to ex:1.10`, `sec:39.1 to sec:39.14`). | Placeholders are not labels. Ranges were expanded against the brief's own TOC and example lists; the expanded labels appear below. |
| A11 | `eq:85.1` (annuity screening shortcut) could be cited for sizing. | Registered as a screening approximation only; sizing cites eq:36.1 to eq:36.3 (R-108). |
| A12 | `fw:deal-on-a-page` (Ch 1) and `fw:loss-trace` (Ch 3) are reused by later chapters. | Ch 85 (sec:85.2) cites `fw:deal-on-a-page` for the first screen block; Ch 28 (sec:28.6) and Ch 64 cite `fw:loss-trace` alongside `fw:who-pays-if` (R-111). |
| A13 | Risk templates for matter file 93. | Matter 93 reproduces `exh:14.6` (risk register) and `exh:15.3` (allocation matrix) (R-031). |
| A14 | Book-wide uniqueness check. | No label is declared by two briefs; no section, subsection, example, exhibit or equation number is declared twice with different content within a chapter except those fixed in A1 to A5; framework numbers are unique within each chapter. |

## 3. Frameworks, book-wide

| Framework | Label | Name | Home chapter | Home section |
|---|---|---|---|---|
| 1.1 | `fw:deal-on-a-page` | The deal on a page | Ch 1 | ssec:1.1.2 |
| 2.1 | `fw:recourse-ladder` | The recourse ladder | Ch 2 | ssec:2.2.2 |
| 2.2 | `fw:pf-fit-test` | The project finance fit test | Ch 2 | sec:2.7 |
| 3.1 | `fw:loss-trace` | The loss trace | Ch 3 | sec:3.10 |
| 4.1 | `fw:party-map` | The party map | Ch 4 | sec:4.9 |
| 4.2 | `fw:lifecycle-gates` | The lifecycle gates | Ch 4 | sec:4.10 |
| 5.1 | `fw:irr-four-questions` | Four questions before trusting an IRR | Ch 5 | ssec:5.6.5 |
| 5.2 | `fw:indexation-audit` | Indexation audit | Ch 5 | ssec:5.10.4 |
| 6.1 | `fw:loan-hedge-tieout` | Loan-and-hedge tie-out | Ch 6 | sec:6.10 |
| 6.2 | `fw:rate-quote-decoder` | Rate quote decoder | Ch 6 | sec:6.2 |
| 7.1 | `fw:project-accounts-read` | First read of project company accounts | Ch 7 | ssec:7.11.1 |
| 8.1 | `fw:leverage-ledger` | Leverage ledger | Ch 8 | sec:8.11 |
| 9.1 | `fw:pvalue-reading` | P-value reading checklist | Ch 9 | sec:9.10 |
| 9.2 | `fw:uncertainty-tool-choice` | Choosing the uncertainty tool | Ch 9 | ssec:9.8.4 |
| 10.1 | `fw:clause-consequence-test` | Clause consequence test | Ch 10 | ssec:10.2.4 |
| 10.2 | `fw:excuse-ladder` | Excuse ladder | Ch 10 | ssec:10.5.5 |
| 11.1 | `fw:megawatt-to-revenue` | Megawatt-to-revenue chain | Ch 11 | sec:11.14 |
| 12.1 | `fw:physical-chain-map` | Physical chain map | Ch 12 | sec:12.12 |
| 13.1 | `fw:formula-robustness-test` | Formula robustness test | Ch 13 | sec:13.5 |
| 14.1 | `fw:risk-card` | The risk card | Ch 14 | ssec:14.1.2 |
| 14.2 | `fw:phase-risk-map` | Phase-by-category risk map | Ch 14 | ssec:14.2.4 |
| 15.1 | `fw:risk-cycle` | Risk management cycle | Ch 15 | ssec:15.1.1 |
| 15.2 | `fw:allocation-test` | Allocation test | Ch 15 | ssec:15.5.1 |
| 15.3 | `fw:bankability-ladder` | Bankability ladder | Ch 15 | ssec:15.9.2 |
| 16.1 | `fw:mitigation-grid` | Mitigation selection grid | Ch 16 | ssec:16.11.1 |
| 16.2 | `fw:loss-stack` | Layered loss stack | Ch 16 | ssec:16.10.1 |
| 16.3 | `fw:mitigation-test` | Mitigation cost-benefit test | Ch 16 | ssec:16.11.2 |
| 17.1 | `fw:termination-compensation-matrix` | Termination compensation matrix | Ch 17 | ssec:17.4.2 |
| 17.2 | `fw:support-strength-test` | Support instrument strength test | Ch 17 | ssec:17.5.4 |
| 18.1 | `fw:tariff-to-cost-match` | Tariff-to-cost match test | Ch 18 | ssec:18.1.1 |
| 18.2 | `fw:volume-risk-checklist` | Volume risk allocation checklist | Ch 18 | ssec:18.4.1 |
| 19.1 | `fw:support-scheme-risk-map` | Support scheme risk map | Ch 19 | ssec:19.1.2 |
| 19.2 | `fw:support-durability-test` | Statute-or-contract durability test | Ch 19 | sec:19.3 |
| 20.1 | `fw:four-risk-decomposition` | Four-risk decomposition of merchant revenue | Ch 20 | ssec:20.1.1 |
| 20.2 | `fw:scarcity-stress` | Scarcity stress for a hedge book | Ch 20 | sec:20.8 |
| 21.1 | `fw:fixed-fee-test` | Fixed-fee test | Ch 21 | ssec:21.1.1 |
| 21.2 | `fw:revenue-contract-grid` | Revenue contract classification grid | Ch 21 | ssec:21.1.2 |
| 22.1 | `fw:delay-ld-calibration` | Delay LD calibration stack | Ch 22 | ssec:22.3.1 |
| 22.2 | `fw:epc-security-stack` | EPC security stack | Ch 22 | ssec:22.6.2 |
| 23.1 | `fw:construction-structure-selector` | Construction structure selector | Ch 23 | ssec:23.1.3 |
| 24.1 | `fw:operating-incentive-alignment` | Operating incentive alignment test | Ch 24 | sec:24.6 |
| 25.1 | `fw:input-chain-alignment` | Input chain alignment grid | Ch 25 | sec:25.9 |
| 26.1 | `fw:sponsor-support-spectrum` | Sponsor support spectrum | Ch 26 | ssec:26.5.1 |
| 27.1 | `fw:insurance-adequacy-test` | Insurance program adequacy test | Ch 27 | sec:27.8 |
| 28.1 | `fw:contract-gap-scan` | Contract gap scan | Ch 28 | sec:28.2 |
| 28.2 | `fw:who-pays-if` | "Who pays if...?" trace | Ch 28 | ssec:28.6.1 |
| 29.1 | `fw:lender-fit-map` | Lender-fit map | Ch 29 | sec:29.8 |
| 29.2 | `fw:eca-cover-build` | ECA cover build | Ch 29 | ssec:29.3.7 |
| 30.1 | `fw:bond-or-loan-test` | Bond-or-loan test | Ch 30 | ssec:30.4.4 |
| 30.2 | `fw:rating-stress-ladder` | Rating-case stress ladder | Ch 30 | ssec:30.5.5 |
| 31.1 | `fw:subordination-stack` | Subordination stack test | Ch 31 | sec:31.8 |
| 32.1 | `fw:equity-commitment-ladder` | Equity commitment ladder | Ch 32 | sec:32.10 |
| 33.1 | `fw:sharia-structure-selector` | Sharia structure selector | Ch 33 | sec:33.6 |
| 33.2 | `fw:islamic-parity-check` | Islamic and conventional parity check | Ch 33 | ssec:33.5.2 |
| 34.1 | `fw:blending-decision-test` | Blending decision test | Ch 34 | ssec:34.3.2 |
| 34.2 | `fw:local-currency-route-map` | Local-currency route map | Ch 34 | ssec:34.6.5 |
| 35.1 | `fw:four-ratio-read` | Four-ratio read | Ch 35 | ssec:35.6.3 |
| 36.1 | `fw:sizing-constraint-stack` | Sizing constraint stack | Ch 36 | ssec:36.3.2 |
| 37.1 | `fw:trigger-ladder` | Trigger ladder | Ch 37 | ssec:37.5.1 |
| 37.2 | `fw:hedge-fit-test` | Hedge fit test | Ch 37 | ssec:37.7.2 |
| 38.1 | `fw:all-in-cost-build` | All-in cost build | Ch 38 | sec:38.6 |
| 39.1 | `fw:model-blueprint` | The model blueprint | Ch 39 | ssec:39.1.3 |
| 40.1 | `fw:circularity-ladder` | The circularity ladder | Ch 40 | ssec:40.5.5 |
| 41.1 | `fw:tariff-to-row-map` | The tariff-to-row map | Ch 41 | ssec:41.4.4 |
| 41.2 | `fw:tax-computation-stack` | The tax computation stack | Ch 41 | ssec:41.5.6 |
| 42.1 | `fw:waterfall-tier` | The four-row waterfall tier | Ch 42 | ssec:42.1.2 |
| 42.2 | `fw:dividend-trap-test` | The dividend trap test | Ch 42 | ssec:42.5.3 |
| 43.1 | `fw:locked-debt-test-protocol` | The locked-debt test protocol | Ch 43 | sec:43.2 |
| 43.2 | `fw:integrity-check-catalogue` | The integrity-check catalogue | Ch 43 | ssec:43.7.1 |
| 44.1 | `fw:seven-pass-review` | The seven-pass model review | Ch 44 | sec:44.2 |
| 44.2 | `fw:finding-severity` | Finding severity grades | Ch 44 | ssec:44.2.8 |
| 45.1 | `fw:revenue-driver-decomposition` | Revenue driver decomposition | Ch 45 | sec:45.1 |
| 46.1 | `fw:value-staircase` | The value staircase | Ch 46 | ssec:46.3.2 |
| 46.2 | `fw:risk-bucket-valuation` | Risk-bucket valuation | Ch 46 | ssec:46.4.2 |
| 47.1 | `fw:bid-discipline-check` | The bid discipline check | Ch 47 | ssec:47.2.4 |
| 47.2 | `fw:pricing-mechanism-choice` | Choosing the price mechanism | Ch 47 | ssec:47.3.4 |
| 48.1 | `fw:dd-scope-matrix` | The diligence scope matrix | Ch 48 | ssec:48.1.2 |
| 48.2 | `fw:report-challenge` | The report challenge protocol | Ch 48 | ssec:48.1.3 |
| 49.1 | `fw:red-flag-grid` | The red-flag grid | Ch 49 | ssec:49.1.2 |
| 49.2 | `fw:counterparty-credit-card` | The counterparty credit card | Ch 49 | ssec:49.5.4 |
| 49.3 | `fw:ownership-trace` | The ownership trace | Ch 49 | ssec:49.6.2 |
| 50.1 | `fw:es-credit-map` | The E&S-to-credit transmission map | Ch 50 | ssec:50.1.1 |
| 50.2 | `fw:es-applicability` | The E&S applicability tree | Ch 50 | ssec:50.2.2 |
| 51.1 | `fw:boilerplate-or-bargain` | Boilerplate-or-bargain sort | Ch 51 | ssec:51.1.5 |
| 51.2 | `fw:eod-severity-grid` | Event of default severity grid | Ch 51 | ssec:51.5.2 |
| 52.1 | `fw:security-control-test` | Security package control test | Ch 52 | ssec:52.1.2 |
| 52.2 | `fw:trace-a-dollar` | Trace-a-dollar test | Ch 52 | sec:52.7 |
| 53.1 | `fw:intercreditor-matrix` | Intercreditor decision matrix | Ch 53 | ssec:53.3.2 |
| 54.1 | `fw:enforcement-first-forum` | Enforcement-first forum choice | Ch 54 | ssec:54.2.4 |
| 54.2 | `fw:treaty-protection-test` | Treaty protection test | Ch 54 | ssec:54.6.3 |
| 55.1 | `fw:financing-strategy-selector` | Financing strategy selector | Ch 55 | ssec:55.1.2 |
| 55.2 | `fw:critical-path-to-close` | Critical path to close | Ch 55 | ssec:55.9.1 |
| 56.1 | `fw:market-check` | Market check | Ch 56 | ssec:56.1.1 |
| 56.2 | `fw:trade-off-ledger` | Trade-off ledger | Ch 56 | ssec:56.4.5 |
| 56.3 | `fw:escalation-ladder` | Escalation ladder | Ch 56 | ssec:56.5.4 |
| 57.1 | `fw:vfm-flip` | Value-for-money flip test | Ch 57 | ssec:57.2.5 |
| 57.2 | `fw:ppp-gateway` | PPP decision gateway | Ch 57 | sec:57.6 |
| 58.1 | `fw:deduction-calibration` | Deduction calibration test | Ch 58 | ssec:58.3.4 |
| 58.2 | `fw:ppp-failure-map` | PPP design failure map | Ch 58 | ssec:58.10.1 |
| 59.1 | `fw:country-scorecard` | Country risk scorecard | Ch 59 | ssec:59.1.3 |
| 59.2 | `fw:payment-stack` | Payment security stack | Ch 59 | ssec:59.4.2 |
| 60.1 | `fw:pr-instrument-map` | Political risk instrument map | Ch 60 | ssec:60.1.1 |
| 60.2 | `fw:bargain-clock` | Obsolescing bargain clock | Ch 60 | ssec:60.2.3 |
| 61.1 | `fw:delay-cash-bridge` | Delay cash bridge | Ch 61 | ssec:61.6.3 |
| 61.2 | `fw:contractor-distress-ladder` | Contractor distress ladder | Ch 61 | ssec:61.8.3 |
| 61.3 | `fw:completion-test-matrix` | Completion test matrix | Ch 61 | ssec:61.11.2 |
| 62.1 | `fw:operating-covenant-calendar` | Operating covenant calendar | Ch 62 | ssec:62.1.2 |
| 62.2 | `fw:waiver-request-ladder` | Waiver request ladder | Ch 62 | ssec:62.7.1 |
| 62.3 | `fw:optimization-gate` | Optimization gate | Ch 62 | ssec:62.8.3 |
| 63.1 | `fw:refinancing-gain-bridge` | Refinancing gain bridge | Ch 63 | ssec:63.2.1 |
| 63.2 | `fw:stake-sale-consent-map` | Stake-sale consent map | Ch 63 | ssec:63.6.3 |
| 64.1 | `fw:distress-dashboard` | Distress early-warning dashboard | Ch 64 | ssec:64.2.3 |
| 64.2 | `fw:restructure-sell-enforce-terminate` | Restructure, sell, enforce or terminate | Ch 64 | ssec:64.6.3 |
| 65.1 | `fw:handback-readiness-timeline` | Handback readiness timeline | Ch 65 | ssec:65.3.2 |
| 65.2 | `fw:end-of-life-option-tree` | End-of-life option tree | Ch 65 | ssec:65.4.2 |
| 66.1 | `fw:accounting-outcome-map` | Accounting outcome map | Ch 66 | ssec:66.8.5 |
| 67.1 | `fw:tax-leakage-map` | Tax leakage map | Ch 67 | ssec:67.1.2 |
| 67.2 | `fw:pillar-two-screen` | Pillar Two screen | Ch 67 | ssec:67.9.6 |
| 68.1 | `fw:capital-to-price-bridge` | Capital-to-price bridge | Ch 68 | ssec:68.5.2 |
| 69.1 | `fw:fuel-chain-trace` | Fuel-chain trace | Ch 69 | sec:69.4 |
| 70.1 | `fw:resource-revenue-bridge` | Resource-to-revenue bridge | Ch 70 | sec:70.9 |
| 71.1 | `fw:pre-fid-exposure-clock` | Pre-FID exposure clock | Ch 71 | ssec:71.5.1 |
| 72.1 | `fw:hydrology-allocation` | Hydrology allocation test | Ch 72 | ssec:72.2.2 |
| 72.2 | `fw:geothermal-staging` | Geothermal resource staging | Ch 72 | ssec:72.5.5 |
| 73.1 | `fw:storage-stack-screen` | Storage revenue stack screen | Ch 73 | ssec:73.3.1 |
| 73.2 | `fw:transmission-revenue-selector` | Transmission revenue model selector | Ch 73 | sec:73.4 |
| 74.1 | `fw:nuclear-risk-bearer` | Nuclear risk-bearer map | Ch 74 | sec:74.3 |
| 75.1 | `fw:borrowing-base-walk` | Borrowing base walk | Ch 75 | ssec:75.3.2 |
| 75.2 | `fw:throughput-credit-test` | Throughput credit test | Ch 75 | ssec:75.4.3 |
| 76.1 | `fw:lng-chain-credit` | LNG chain credit map | Ch 76 | ssec:76.3.3 |
| 76.2 | `fw:charter-credit-test` | Charter-backed credit test | Ch 76 | ssec:76.8.4 |
| 77.1 | `fw:margin-ladder` | Margin protection ladder | Ch 77 | ssec:77.5.1 |
| 78.1 | `fw:four-part-completion` | Four-part completion test | Ch 78 | ssec:78.7.3 |
| 78.2 | `fw:deck-tail-test` | Deck-tail-test triangle | Ch 78 | ssec:78.7.3 |
| 79.1 | `fw:demand-risk-menu` | Demand-risk sharing menu for toll roads | Ch 79 | ssec:79.4.4 |
| 79.2 | `fw:ramp-up-diagnosis` | Ramp-up diagnosis | Ch 79 | ssec:79.5.1 |
| 80.1 | `fw:footloose-demand` | Footloose-demand test | Ch 80 | ssec:80.4.1 |
| 81.1 | `fw:payment-chain` | Payment-chain trace | Ch 81 | ssec:81.5.1 |
| 82.1 | `fw:lease-life-gap` | Lease-life gap test | Ch 82 | ssec:82.5.1 |
| 83.1 | `fw:market-risk-trace` | Market-risk holder trace | Ch 83 | ssec:83.5.1 |
| 84.1 | `fw:label-test` | Three-question label test | Ch 84 | ssec:84.1.2 |
| 84.2 | `fw:project-climate-screen` | Project climate risk screen | Ch 84 | ssec:84.6.6 |
| 85.1 | `fw:one-hour-deal-screen` | One-hour deal screen | Ch 85 | sec:85.2 |
| 85.2 | `fw:deal-questions` | Questions to ask on any deal | Ch 85 | ssec:85.4.1 |
| 85.3 | `fw:data-room-reading-order` | Data room reading order | Ch 85 | ssec:85.5.2 |
| 86.1 | `fw:credit-paper-structure` | Credit paper structure | Ch 86 | sec:86.2 |
| 86.2 | `fw:risk-mitigant-residual` | Risk–mitigant–residual table | Ch 86 | ssec:86.2.4 |
| 86.3 | `fw:committee-pre-mortem` | Committee pre-mortem | Ch 86 | ssec:86.5.3 |
| 87.1 | `fw:advisor-cycle` | Advisor management cycle | Ch 87 | ssec:87.1.3 |
| 87.2 | `fw:judgment-plan` | Judgment-building plan | Ch 87 | ssec:87.8.7 |
| 87.3 | `fw:integrity-test` | The integrity test | Ch 87 | ssec:87.5.2 |
| 88.1 | `fw:new-structure-test` | New-structure test | Ch 88 | ssec:88.2.1 |
| 88.2 | `fw:foak-ladder` | First-of-a-kind financing ladder | Ch 88 | ssec:88.3.1 |

Established frameworks credited in prose next to their home box: critical path method (Framework 55.2), pre-mortem technique (Framework 86.3 and the pre-mortem in ssec:15.1.3), FAST standard (cited in Ch 39, not a numbered framework), EP4 scope rules (Framework 50.2 is original but built on them), IFC Performance Standards and OECD Arrangement rules (Framework 29.2 is original procedure built on the Arrangement). All other frameworks are original to this book.

## 4. Front matter labels

| Label | Title |
|---|---|
| `fm:how-built` | How the book is built |
| `fm:running-cases` | The three running cases |
| `fm:conventions` | How to read the conventions |
| `fm:routes` | Routes through the book |
| `fm:study-plan` | A realistic study plan |
| `fm:exercises` | How to work the exercises |
| `fm:model-builds` | How to work the model builds |
| `fm:caveat` | The general caveat |

Front-matter exhibits are labeled `exh:fm.1` to `exh:fm.3` (capability map, cast list, study plan) and print as Exhibit FM.1 to FM.3.

## 5. Labels by chapter

### Chapter 1: A small deal, start to finish

Source brief: `briefs/u01.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:1` | A small deal, start to finish |  |
| `sec:1.1` | Llano Pardo Solar on one page |  |
| `ssec:1.1.1` | The plant, the place, and the parties |  |
| `ssec:1.1.2` | The deal on a page |  |
| `sec:1.2` | Development: from an option on grazing land to a winning bid |  |
| `ssec:1.2.1` | Land, sunlight, and the measurement record |  |
| `ssec:1.2.2` | Permits and the grid connection |  |
| `ssec:1.2.3` | The tender and the bid tariff |  |
| `sec:1.3` | The contracts that make the cash flow predictable |  |
| `ssec:1.3.1` | The power purchase agreement |  |
| `ssec:1.3.2` | The EPC contract |  |
| `ssec:1.3.3` | Operations, land, and insurance |  |
| `ssec:1.3.4` | How the contracts lock together |  |
| `sec:1.4` | The model: from sunlight to cash for lenders |  |
| `ssec:1.4.1` | One year of cash flow |  |
| `ssec:1.4.2` | Twenty years in one table |  |
| `sec:1.5` | Sizing the debt |  |
| `ssec:1.5.1` | How much debt one year can carry |  |
| `ssec:1.5.2` | Two tests, and the smaller one wins |  |
| `ssec:1.5.3` | Testing the bad years |  |
| `sec:1.6` | Walkthrough: the Llano Pardo term sheet |  |
| `sec:1.7` | Financial close |  |
| `sec:1.8` | Construction |  |
| `sec:1.9` | Operations and repayment |  |
| `ssec:1.9.1` | The first year comes in 7.5% short |  |
| `ssec:1.9.2` | The waterfall every December |  |
| `ssec:1.9.3` | Repayment to 2035, and the years after |  |
| `sec:1.10` | What the sponsors earned |  |
| `sec:1.11` | Case P: a call from Dabakro |  |
| `sec:1.12` | What changes when the deal is large |  |
| `sec:1.13` | Practitioner's notebook |  |
| `sec:1.14` | Judgment drill |  |
| `sec:1.15` | Every contract here assumed someone would pay |  |
| `sec:1.16` | Exercises |  |
| `sec:1.17` | Solutions to exercises |  |
| `ex:1.1` | Estimating the plant's first-year output |  |
| `ex:1.2` | Revenue under the PPA and the size of the letter of credit |  |
| `ex:1.3` | Why delay damages are USD 28,700 a day |  |
| `ex:1.4` | From sunlight to CFADS in Operating Year 1 |  |
| `ex:1.5` | How much debt service one year can carry |  |
| `ex:1.6` | Two sizing tests, one loan |  |
| `ex:1.7` | Testing a bad year |  |
| `ex:1.8` | Sources and uses at financial close |  |
| `ex:1.9` | The first year comes in short |  |
| `ex:1.10` | What the sponsors earned |  |
| `exh:1.1` | Llano Pardo contract map (Illustrative) |  |
| `exh:1.2` | Llano Pardo on one page (Illustrative) |  |
| `exh:1.3` | Llano Pardo operating costs in Operating Year 1 (USD thousands) (Illustrative) |  |
| `exh:1.4` | Llano Pardo base-case projection, 2018 to 2037 (USD thousands) (Illustrative) |  |
| `exh:1.5` | CFADS and debt service, 2018 to 2037 (USD thousands) (Illustrative) |  |
| `exh:1.6` | Llano Pardo term sheet, August 2016 (Illustrative) |  |
| `exh:1.7` | Sources and uses at financial close (USD thousands) (Illustrative) |  |
| `exh:1.8` | Construction drawdowns by quarter (USD thousands) (Illustrative) |  |
| `exh:1.9` | Llano Pardo from land option to decommissioning (Illustrative) |  |
| `exh:1.10` | The Llano Pardo cash waterfall (Illustrative) |  |
| `fw:deal-on-a-page` | Framework 1.1 The deal on a page | home ssec:1.1.2 |

### Chapter 2: What project finance is, and when to use it

Source brief: `briefs/u01.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:2` | What project finance is, and when to use it |  |
| `sec:2.1` | The project company and its ring-fence |  |
| `ssec:2.1.1` | A company with one asset and no history |  |
| `ssec:2.1.2` | What the ring-fence keeps in and keeps out |  |
| `ssec:2.1.3` | SunEdison and TerraForm: a ring-fence tested |  |
| `sec:2.2` | Recourse: what lenders can reach |  |
| `ssec:2.2.1` | Non-recourse, limited recourse, full recourse |  |
| `ssec:2.2.2` | Where limited recourse sits in practice |  |
| `sec:2.3` | The contractual web |  |
| `ssec:2.3.1` | Contracts in place of a balance sheet |  |
| `ssec:2.3.2` | Giving each risk to the party best able to manage it |  |
| `ssec:2.3.3` | Sabine Pass: contracts that made a plant financeable |  |
| `sec:2.4` | Project finance and its neighbors |  |
| `ssec:2.4.1` | Corporate finance |  |
| `ssec:2.4.2` | Asset finance and leasing |  |
| `ssec:2.4.3` | Reserve-based lending |  |
| `ssec:2.4.4` | Acquisition finance |  |
| `ssec:2.4.5` | Securitization and structured finance |  |
| `sec:2.5` | Why sponsors, lenders, and governments choose it |  |
| `ssec:2.5.1` | Risk isolation and debt capacity |  |
| `ssec:2.5.2` | Governance and agency costs |  |
| `ssec:2.5.3` | Partnering and political deterrence |  |
| `ssec:2.5.4` | What the host government gets |  |
| `sec:2.6` | What project finance costs |  |
| `ssec:2.6.1` | Money and time |  |
| `ssec:2.6.2` | Rigidity, information, and control |  |
| `sec:2.7` | When project finance is the wrong tool |  |
| `sec:2.8` | Walkthrough: a board paper choosing between corporate debt and project finance |  |
| `sec:2.9` | Case P: Kilnworth decides how to fund Bélanou |  |
| `sec:2.10` | Practitioner's notebook |  |
| `sec:2.11` | Judgment drill |  |
| `sec:2.12` | The structure is old; its rules were learned one failure at a time |  |
| `sec:2.13` | Exercises |  |
| `sec:2.14` | Solutions to exercises |  |
| `ex:2.1` | Two ways to fund a wind farm |  |
| `ex:2.2` | Climbing the recourse ladder |  |
| `ex:2.3` | Who should carry module soiling at Llano Pardo? |  |
| `ex:2.4` | What project finance costs on the wind farm |  |
| `ex:2.5` | Too small for project finance |  |
| `exh:2.1` | Project finance and its six neighbors |  |
| `exh:2.2` | Board paper summary: corporate route against project finance (USD m) (Illustrative) |  |
| `exh:2.3` | if it teaches |  |
| `cl:2.1` | Single-purpose and separateness undertaking, common terms agreement (Illustrative) |  |
| `fw:recourse-ladder` | Framework 2.1 The recourse ladder | home ssec:2.2.2 |
| `fw:pf-fit-test` | Framework 2.2 The project finance fit test | home sec:2.7 |

### Chapter 3: How project finance evolved

Source brief: `briefs/u01.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:3` | How project finance evolved |  |
| `sec:3.1` | Lending against oil in the ground |  |
| `ssec:3.1.1` | Production payments |  |
| `ssec:3.1.2` | The North Sea and field financing |  |
| `sec:3.2` | Independent power in the United States |  |
| `sec:3.3` | The emerging-market IPP wave |  |
| `ssec:3.3.1` | Hub Power and the sovereign support package |  |
| `ssec:3.3.2` | Dabhol: a contract cannot make power affordable |  |
| `ssec:3.3.3` | Paiton I and the Asian crisis |  |
| `ssec:3.3.4` | Multilateral institutions as lenders and shields |  |
| `sec:3.4` | Megaprojects and the debt trap |  |
| `sec:3.5` | The PFI and PPP era |  |
| `sec:3.6` | After 2008: banks retreat, rules change, new lenders arrive |  |
| `ssec:3.6.1` | The crisis and the banks |  |
| `ssec:3.6.2` | Basel and the price of a project loan |  |
| `ssec:3.6.3` | Insurers, pension funds and debt funds |  |
| `sec:3.7` | Public credit for new technology: Ivanpah |  |
| `sec:3.8` | The energy transition at scale |  |
| `sec:3.9` | Digital infrastructure and the new frontier |  |
| `sec:3.10` | What each era taught |  |
| `sec:3.11` | Walkthrough: reading a post-mortem of a landmark deal |  |
| `sec:3.12` | Case P: an arranger reads the Kessara RFQ |  |
| `sec:3.13` | Practitioner's notebook |  |
| `sec:3.14` | Judgment drill |  |
| `sec:3.15` | Every era's lesson became a clause; the clauses need parties to sign them |  |
| `sec:3.16` | Exercises |  |
| `sec:3.17` | Solutions to exercises |  |
| `ex:3.1` | How a production payment works |  |
| `ex:3.2` | A dollar tariff meets a devaluation |  |
| `ex:3.3` | The debt trap |  |
| `ex:3.4` | What a longer tenor buys |  |
| `exh:3.1` | Project finance eras, 1930s to 2026 |  |
| `exh:3.2` | What each era taught |  |
| `fw:loss-trace` | Framework 3.1 The loss trace | home sec:3.10 |

### Chapter 4: The parties and the project lifecycle

Source brief: `briefs/u01.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:4` | The parties and the project lifecycle |  |
| `sec:4.1` | Sponsors |  |
| `ssec:4.1.1` | Strategic sponsors |  |
| `ssec:4.1.2` | Financial sponsors |  |
| `ssec:4.1.3` | Developers |  |
| `ssec:4.1.4` | Sponsors under stress |  |
| `sec:4.2` | The project company and its management |  |
| `sec:4.3` | Lenders |  |
| `ssec:4.3.1` | Commercial banks and the arranger |  |
| `ssec:4.3.2` | Export credit agencies |  |
| `ssec:4.3.3` | Development finance institutions |  |
| `ssec:4.3.4` | Bondholders, institutional investors and private credit |  |
| `ssec:4.3.5` | Lenders under stress |  |
| `sec:4.4` | Offtakers |  |
| `sec:4.5` | Host governments, contracting authorities and regulators |  |
| `sec:4.6` | Builders, equipment suppliers and operators |  |
| `ssec:4.6.1` | EPC contractors and OEMs |  |
| `ssec:4.6.2` | O&M operators and long-term service providers |  |
| `ssec:4.6.3` | A contractor fails mid-construction |  |
| `sec:4.7` | Input suppliers, insurers and hedge providers |  |
| `sec:4.8` | Advisors, agents, trustees and rating agencies |  |
| `sec:4.9` | Reading the whole cast |  |
| `sec:4.10` | The project lifecycle |  |
| `ssec:4.10.1` | Origination |  |
| `ssec:4.10.2` | Development |  |
| `ssec:4.10.3` | Financing and financial close |  |
| `ssec:4.10.4` | Construction and completion |  |
| `ssec:4.10.5` | Operations |  |
| `ssec:4.10.6` | Refinancing and sale |  |
| `ssec:4.10.7` | Decommissioning or handback |  |
| `sec:4.11` | Walkthrough: a development budget and team plan |  |
| `sec:4.12` | Case P: a partnership, a budget and a team |  |
| `sec:4.13` | Practitioner's notebook |  |
| `sec:4.14` | Judgment drill |  |
| `sec:4.15` | Every party has a price; the first one to name is the price of money over time |  |
| `sec:4.16` | Exercises |  |
| `sec:4.17` | Solutions to exercises |  |
| `ex:4.1` | Where Llano Pardo's revenue went |  |
| `ex:4.2` | Money at risk through development |  |
| `ex:4.3` | A six-month construction delay: who pays |  |
| `ex:4.4` | ELNACOR pays 60 days late |  |
| `exh:4.1` | Llano Pardo party map (Illustrative) |  |
| `exh:4.2` | Llano Pardo lifecycle gates (USD thousands) (Illustrative) |  |
| `exh:4.3` | Where Llano Pardo's revenue went, 2018 to 2037 (USD thousands) (Illustrative) |  |
| `exh:4.4` | Llano Pardo development budget and appointments (USD thousands) (Illustrative) |  |
| `exh:4.5` | Case P lifecycle, 2015 to 2046 (Case P) |  |
| `exh:4.6` | Case P development budget against actual costs to financial close (USD m) (Case P) |  |
| `fw:party-map` | Framework 4.1 The party map | home sec:4.9 |
| `fw:lifecycle-gates` | Framework 4.2 The lifecycle gates | home sec:4.10 |

### Chapter 5: Money and time

Source brief: `briefs/u02.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:5` | Money and time |  |
| `sec:5.1` | Interest and compounding |  |
| `ssec:5.1.1` | Simple and compound interest |  |
| `ssec:5.1.2` | Compounding frequency and the effective annual rate |  |
| `ssec:5.1.3` | The rule of 72 and when it fails |  |
| `sec:5.2` | Discounting and present value |  |
| `ssec:5.2.1` | Present value of a single future amount |  |
| `ssec:5.2.2` | The discount-factor table |  |
| `ssec:5.2.3` | What the discount rate stands for |  |
| `sec:5.3` | Annuities, perpetuities and levelized prices |  |
| `ssec:5.3.1` | Level annuities |  |
| `ssec:5.3.2` | Growing annuities and perpetuities |  |
| `ssec:5.3.3` | Levelized cost and levelized tariff |  |
| `sec:5.4` | Net present value |  |
| `ssec:5.4.1` | The NPV rule |  |
| `ssec:5.4.2` | The NPV profile |  |
| `ssec:5.4.3` | The Excel NPV function and its first-period trap |  |
| `sec:5.5` | Internal rate of return |  |
| `ssec:5.5.1` | IRR as the break-even discount rate |  |
| `ssec:5.5.2` | Reading IRR against NPV |  |
| `sec:5.6` | Where IRR misleads |  |
| `ssec:5.6.1` | Multiple IRRs and no IRR |  |
| `ssec:5.6.2` | The reinvestment assumption and MIRR |  |
| `ssec:5.6.3` | Scale and incremental IRR |  |
| `ssec:5.6.4` | Timing and the crossover rate |  |
| `ssec:5.6.5` | Four questions before trusting an IRR |  |
| `sec:5.7` | Irregular dates: XNPV and XIRR |  |
| `ssec:5.7.1` | Why period counting breaks |  |
| `ssec:5.7.2` | Computing XIRR |  |
| `ssec:5.7.3` | Annualizing periodic returns |  |
| `sec:5.8` | Payback and discounted payback |  |
| `ssec:5.8.1` | Payback as a liquidity and risk screen |  |
| `sec:5.9` | Inflation, real and nominal values |  |
| `ssec:5.9.1` | Price indices and base dates |  |
| `ssec:5.9.2` | Real and nominal cash flows |  |
| `ssec:5.9.3` | Inflation in a project's cash flows |  |
| `sec:5.10` | Indexation in long-term contracts |  |
| `ssec:5.10.1` | Full, partial and fixed-escalator indexation |  |
| `ssec:5.10.2` | Lags, resets and caps |  |
| `ssec:5.10.3` | Local-currency shares and reconversion |  |
| `ssec:5.10.4` | Indexation audit |  |
| `sec:5.11` | Walkthrough: building an NPV and IRR sheet in a blank workbook |  |
| `sec:5.12` | Walkthrough: reading an indexation formula |  |
| `sec:5.13` | Case P: indexing the January 2022 invoice |  |
| `sec:5.14` | Practitioner's notebook |  |
| `sec:5.15` | Judgment drill |  |
| `sec:5.16` | A discount rate needs a source |  |
| `sec:5.17` | Exercises |  |
| `sec:5.18` | Solutions to exercises |  |
| `ex:5.1` | Growing a deposit under different compounding |  |
| `ex:5.2` | Effective and periodic rates |  |
| `ex:5.3` | Present value of a deferred payment |  |
| `ex:5.4` | Valuing a land lease |  |
| `ex:5.5` | An escalating O&M fee |  |
| `ex:5.6` | Levelized cost of a solar plant |  |
| `ex:5.7` | NPV of a gas-engine life extension |  |
| `ex:5.8` | The Excel NPV first-period trap |  |
| `ex:5.9` | A mine with a reclamation bill |  |
| `ex:5.10` | Reinvestment and MIRR |  |
| `ex:5.11` | Scale: the smaller project with the higher IRR |  |
| `ex:5.12` | Timing and the crossover rate |  |
| `ex:5.13` | XIRR on an equity investor's dated cash flows |  |
| `ex:5.14` | Payback and discounted payback |  |
| `ex:5.15` | Rebasing an index to a contract base date |  |
| `ex:5.16` | Real and nominal give the same answer if you are consistent |  |
| `ex:5.17` | How partial indexation erodes a price |  |
| `ex:5.18` | A local-currency share under parity and under overshoot |  |
| `exh:5.1` | Discount factors at 9.25% |  |
| `exh:5.2` | NPV profile of the gas-engine life extension |  |
| `exh:5.3` | pgfplots line chart of the same | implied by the brief text; writer assigns this label in order of appearance |
| `exh:5.4` | Two NPV profiles that cross |  |
| `exh:5.5` | Nominal and real paths of a partially indexed charge |  |
| `exh:5.6` | Layout of an NPV and IRR sheet |  |
| `exh:5.7` | Case P capacity and O&M charges indexed to January 2022 |  |
| `cl:5.1` | Capacity charge indexation, PPA (Illustrative) |  |
| `eq:5.1` | Future value with compounding |  |
| `eq:5.2` | Present value and the discount factor |  |
| `eq:5.3` | Annuity factor |  |
| `eq:5.4` | Growing annuity |  |
| `eq:5.5` | Perpetuity and growing perpetuity |  |
| `eq:5.6` | Net present value |  |
| `eq:5.7` | Internal rate of return |  |
| `eq:5.8` | XNPV with Actual/365 year fractions |  |
| `eq:5.9` | Fisher relation |  |
| `eq:5.10` | Partial indexation |  |
| `eq:5.11` | Levelized price |  |
| `fw:irr-four-questions` | Framework 5.1 Four questions before trusting an IRR | home ssec:5.6.5 |
| `fw:indexation-audit` | Framework 5.2 Indexation audit | home ssec:5.10.4 |

### Chapter 6: Debt and interest rates

Source brief: `briefs/u02.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:6` | Debt and interest rates |  |
| `sec:6.1` | What a loan is |  |
| `ssec:6.1.1` | Principal, interest and fees |  |
| `ssec:6.1.2` | Fees on commitments and drawings |  |
| `sec:6.2` | Interest periods and day counts |  |
| `ssec:6.2.1` | Interest periods and payment dates |  |
| `ssec:6.2.2` | Day-count conventions |  |
| `sec:6.3` | Repayment profiles |  |
| `ssec:6.3.1` | Bullet, annuity and straight-line |  |
| `ssec:6.3.2` | Weighted average life |  |
| `ssec:6.3.3` | Sculpted repayment in outline |  |
| `sec:6.4` | Fixed and floating rates |  |
| `ssec:6.4.1` | Who carries rate risk |  |
| `ssec:6.4.2` | Margins and basis points |  |
| `sec:6.5` | Reference rates after LIBOR |  |
| `ssec:6.5.1` | How LIBOR worked and why it ended |  |
| `ssec:6.5.2` | The risk-free rates |  |
| `ssec:6.5.3` | Term rates and compounding in arrears |  |
| `ssec:6.5.4` | Credit adjustment spreads and fallbacks |  |
| `sec:6.6` | The yield curve, forward rates and discount factors |  |
| `ssec:6.6.1` | Zero rates and discount factors |  |
| `ssec:6.6.2` | Forward rates |  |
| `sec:6.7` | Bonds in one section |  |
| `ssec:6.7.1` | Coupon, price and yield |  |
| `ssec:6.7.2` | Bonds against loans in one paragraph |  |
| `sec:6.8` | Interest rate swaps |  |
| `ssec:6.8.1` | How a swap turns floating into fixed |  |
| `ssec:6.8.2` | The swap rate and the credit and execution charge | ruling: The par swap rate (retitled, R-007) |
| `ssec:6.8.3` | Valuing a swap and breaking it |  |
| `ssec:6.8.4` | Amortizing, accreting and mismatched swaps |  |
| `ssec:6.8.5` | Caps and collars |  |
| `sec:6.9` | Walkthrough: reading the interest clause of a facility agreement |  |
| `sec:6.10` | Walkthrough: reading a swap confirmation's economic terms |  |
| `sec:6.11` | Case P: from LIBOR plus a margin to Term SOFR |  |
| `sec:6.12` | Practitioner's notebook |  |
| `sec:6.13` | Judgment drill |  |
| `sec:6.14` | Interest is a cash cost; the accounts tell a different story |  |
| `sec:6.15` | Exercises |  |
| `sec:6.16` | Solutions to exercises |  |
| `ex:6.1` | The first-year cost of a construction facility |  |
| `ex:6.2` | One period under three day counts |  |
| `ex:6.3` | One loan, three repayment profiles |  |
| `ex:6.4` | A sculpted profile in outline |  |
| `ex:6.5` | Interest on a floating amortizing loan |  |
| `ex:6.6` | Compounding SOFR in arrears |  |
| `ex:6.7` | Day count equivalence |  |
| `ex:6.8` | A LIBOR fallback and floor parity |  |
| `ex:6.9` | Building discount factors, forwards and a swap rate from a curve |  |
| `ex:6.10` | Pricing a bond at three yields |  |
| `ex:6.11` | Four swap settlements |  |
| `ex:6.12` | Marking a swap to market |  |
| `exh:6.1` | Day-count conventions by market |  |
| `exh:6.2` | Annuity repayment schedule |  |
| `exh:6.3` | pgfplots chart of the three balances | implied by the brief text; writer assigns this label in order of appearance |
| `exh:6.4` | Reference rates at a glance |  |
| `exh:6.5` | curve table | implied by the brief text; writer assigns this label in order of appearance |
| `exh:6.6` | How a payer swap fixes a floating loan |  |
| `exh:6.7` | Economic terms of a swap confirmation |  |
| `exh:6.8` | Case P indicative 2016 cost by tranche |  |
| `exh:6.9` | Case P interest cost before and after the LIBOR switch |  |
| `cl:6.1` | Interest rate and fallback, facility agreement (Illustrative) |  |
| `eq:6.1` | Interest with a day-count fraction |  |
| `eq:6.2` | Weighted average life |  |
| `eq:6.3` | Compounded rate in arrears |  |
| `eq:6.4` | Forward rate from discount factors |  |
| `eq:6.5` | Bond price |  |
| `eq:6.6` | Par swap rate |  |
| `eq:6.7` | Value of a payer swap |  |
| `fw:loan-hedge-tieout` | Framework 6.1 Loan-and-hedge tie-out | home sec:6.10 |
| `fw:rate-quote-decoder` | Framework 6.2 Rate quote decoder | home sec:6.2 |

### Chapter 7: Accounting from zero

Source brief: `briefs/u02.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:7` | Accounting from zero |  |
| `sec:7.1` | Why a financier reads accounts |  |
| `sec:7.2` | The accounting equation and double entry |  |
| `ssec:7.2.1` | Assets, liabilities and equity |  |
| `ssec:7.2.2` | A project company's first transactions |  |
| `sec:7.3` | The income statement |  |
| `ssec:7.3.1` | From revenue to net income |  |
| `ssec:7.3.2` | Accruals: earned is not received |  |
| `sec:7.4` | The balance sheet |  |
| `ssec:7.4.1` | Assets of a project company |  |
| `ssec:7.4.2` | Liabilities and equity |  |
| `sec:7.5` | The cash flow statement and the three-way link |  |
| `ssec:7.5.1` | Indirect method |  |
| `ssec:7.5.2` | Linking the three statements |  |
| `sec:7.6` | Depreciation, amortization and impairment |  |
| `ssec:7.6.1` | Spreading the cost of a long-lived asset |  |
| `ssec:7.6.2` | Book depreciation versus tax depreciation |  |
| `ssec:7.6.3` | Impairment |  |
| `sec:7.7` | Capitalized interest during construction |  |
| `ssec:7.7.1` | Why construction interest becomes part of the asset |  |
| `ssec:7.7.2` | What capitalization does later |  |
| `sec:7.8` | Deferred tax |  |
| `ssec:7.8.1` | Temporary differences |  |
| `ssec:7.8.2` | Accelerated tax depreciation and the deferred tax liability |  |
| `ssec:7.8.3` | Tax holidays, losses and deferred tax assets |  |
| `sec:7.9` | Working capital |  |
| `ssec:7.9.1` | Receivables, payables and inventory |  |
| `ssec:7.9.2` | When the offtaker pays late |  |
| `sec:7.10` | Provisions and contingent liabilities |  |
| `ssec:7.10.1` | Decommissioning and handback provisions |  |
| `ssec:7.10.2` | Onerous contracts and contingent liabilities |  |
| `sec:7.11` | Reading a project company's accounts |  |
| `ssec:7.11.1` | A disciplined first read |  |
| `ssec:7.11.2` | When the accounts do not show the plant |  |
| `ssec:7.11.3` | Distributions and the accounts |  |
| `sec:7.12` | Walkthrough: linking three statements in a blank workbook |  |
| `sec:7.13` | Case P: Bélanou Power's 2022 accounts |  |
| `sec:7.14` | Practitioner's notebook |  |
| `sec:7.15` | Judgment drill |  |
| `sec:7.16` | Profit is not the measure of a project; the right return depends on the debt |  |
| `sec:7.17` | Exercises |  |
| `sec:7.18` | Solutions to exercises |  |
| `ex:7.1` | A project company's first transactions |  |
| `ex:7.2` | The first operating year's income statement |  |
| `ex:7.3` | Earned is not received |  |
| `ex:7.4` | Linking the three statements for one year |  |
| `ex:7.5` | Three depreciation methods |  |
| `ex:7.6` | An impairment test |  |
| `ex:7.7` | Interest capitalized during construction |  |
| `ex:7.8` | Accelerated tax depreciation and a deferred tax liability |  |
| `ex:7.9` | A tax holiday with deferred depreciation |  |
| `ex:7.10` | An offtaker that pays at 120 days |  |
| `ex:7.11` | A decommissioning provision |  |
| `exh:7.1` | balance sheet after each | implied by the brief text; writer assigns this label in order of appearance |
| `exh:7.2` | Three linked statements for one year |  |
| `exh:7.3` | How the three statements link |  |
| `exh:7.4` | seven-year table | implied by the brief text; writer assigns this label in order of appearance |
| `exh:7.5` | Abridged accounts of a solar project company |  |
| `exh:7.6` | (caption not stated in brief; writer supplies) | implied by the brief text; writer assigns this label in order of appearance |
| `exh:7.7` | Bélanou Power income statement, 2022 |  |
| `exh:7.8` | Bélanou Power balance sheet, December 31, 2022 |  |
| `exh:7.9` | Bélanou Power cash flow statement, 2022 |  |
| `eq:7.1` | Accounting equation |  |
| `eq:7.2` | Deferred tax on a temporary difference |  |
| `eq:7.3` | Receivables from days |  |
| `fw:project-accounts-read` | Framework 7.1 First read of project company accounts | home ssec:7.11.1 |

### Chapter 8: Leverage, risk and the cost of capital

Source brief: `briefs/u02.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:8` | Leverage, risk and the cost of capital |  |
| `sec:8.1` | Debt and equity as claims on one project |  |
| `ssec:8.1.1` | Who gets paid first |  |
| `ssec:8.1.2` | What each claimant wants |  |
| `sec:8.2` | How leverage changes equity returns |  |
| `ssec:8.2.1` | The leverage equation |  |
| `ssec:8.2.2` | Leverage over a project's life |  |
| `ssec:8.2.3` | Leverage widens the spread |  |
| `sec:8.3` | The Modigliani-Miller intuition |  |
| `ssec:8.3.1` | Why leverage alone creates no value in a perfect market |  |
| `ssec:8.3.2` | What breaks the result |  |
| `ssec:8.3.3` | Why project finance can carry so much debt |  |
| `sec:8.4` | Risk and the required return |  |
| `ssec:8.4.1` | Diversifiable and systematic risk |  |
| `ssec:8.4.2` | Which risks a project's investors are paid for |  |
| `sec:8.5` | The capital asset pricing model |  |
| `ssec:8.5.1` | Beta and the security market line |  |
| `ssec:8.5.2` | Unlevering and relevering beta |  |
| `ssec:8.5.3` | Country risk in a cost of equity |  |
| `sec:8.6` | The cost of debt |  |
| `ssec:8.6.1` | Promised and expected returns on debt |  |
| `ssec:8.6.2` | After-tax cost of debt |  |
| `sec:8.7` | WACC and APV |  |
| `ssec:8.7.1` | Weighted average cost of capital |  |
| `ssec:8.7.2` | Why a constant WACC misfits amortizing project debt |  |
| `ssec:8.7.3` | Adjusted present value |  |
| `ssec:8.7.4` | Which method to use when |  |
| `sec:8.8` | Real case: the same reactor at two costs of capital |  |
| `sec:8.9` | Walkthrough: building a gearing-versus-return table |  |
| `sec:8.10` | Case P: how much debt Kilnworth wanted |  |
| `sec:8.11` | Practitioner's notebook |  |
| `sec:8.12` | Judgment drill |  |
| `sec:8.13` | Expected returns assume an expected case |  |
| `sec:8.14` | Exercises |  |
| `sec:8.15` | Solutions to exercises |  |
| `ex:8.1` | Debt and equity payoffs |  |
| `ex:8.2` | The leverage equation in one period |  |
| `ex:8.3` | Equity IRR against gearing over 25 years |  |
| `ex:8.4` | The same shock at three gearings |  |
| `ex:8.5` | Modigliani-Miller Proposition II |  |
| `ex:8.6` | Diversification with two states |  |
| `ex:8.7` | Cost of equity from a listed comparable |  |
| `ex:8.8` | Adding a country risk premium |  |
| `ex:8.9` | After-tax cost of debt |  |
| `ex:8.10` | A WACC |  |
| `ex:8.11` | APV against a constant WACC |  |
| `exh:8.1` | pgfplots payoff lines: debt capped, equity residual | implied by the brief text; writer assigns this label in order of appearance |
| `exh:8.2` | Equity IRR by gearing, base and downside |  |
| `exh:8.3` | Equity IRR against gearing |  |
| `exh:8.4` | (caption not stated in brief; writer supplies) | implied by the brief text; writer assigns this label in order of appearance |
| `exh:8.5` | Case P equity IRR by gearing |  |
| `eq:8.1` | Leverage equation for the return on equity |  |
| `eq:8.2` | Modigliani-Miller Proposition II |  |
| `eq:8.3` | Interest tax shield |  |
| `eq:8.4` | Capital asset pricing model |  |
| `eq:8.5` | Asset beta |  |
| `eq:8.6` | Relevered equity beta |  |
| `eq:8.7` | Weighted average cost of capital |  |
| `eq:8.8` | Adjusted present value |  |
| `fw:leverage-ledger` | Framework 8.1 Leverage ledger | home sec:8.11 |

### Chapter 9: Probability and uncertainty

Source brief: `briefs/u02.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:9` | Probability and uncertainty |  |
| `sec:9.1` | Outcomes as distributions |  |
| `ssec:9.1.1` | From a data series to a histogram |  |
| `ssec:9.1.2` | Discrete and continuous distributions |  |
| `sec:9.2` | Expected value, median and mode |  |
| `ssec:9.2.1` | Expected value of a discrete outcome |  |
| `ssec:9.2.2` | Skewed outcomes |  |
| `sec:9.3` | Measuring spread |  |
| `ssec:9.3.1` | Variance and standard deviation |  |
| `ssec:9.3.2` | Coefficient of variation |  |
| `sec:9.4` | The normal distribution and its limits |  |
| `ssec:9.4.1` | Percentiles of a normal distribution |  |
| `ssec:9.4.2` | Lognormal outcomes and fat tails |  |
| `sec:9.5` | Exceedance levels: P50, P90 and P99 |  |
| `ssec:9.5.1` | Defining exceedance |  |
| `ssec:9.5.2` | Why lenders look at P90 |  |
| `sec:9.6` | One-year and ten-year P-values |  |
| `ssec:9.6.1` | Two kinds of uncertainty |  |
| `ssec:9.6.2` | Computing one-year and ten-year P90 |  |
| `ssec:9.6.3` | Which P-value answers which question |  |
| `sec:9.7` | Correlation |  |
| `ssec:9.7.1` | Covariance and the correlation coefficient |  |
| `ssec:9.7.2` | Diversification across assets |  |
| `ssec:9.7.3` | When price and volume move together |  |
| `sec:9.8` | Sensitivity, scenario and Monte Carlo analysis |  |
| `ssec:9.8.1` | Sensitivity analysis and the tornado chart |  |
| `ssec:9.8.2` | Scenarios that hang together |  |
| `ssec:9.8.3` | Monte Carlo simulation |  |
| `ssec:9.8.4` | Choosing the tool |  |
| `sec:9.9` | Forecasts are distributions too |  |
| `ssec:9.9.1` | The winner sits in the tail |  |
| `ssec:9.9.2` | Reference classes |  |
| `sec:9.10` | Walkthrough: reading an energy yield assessment |  |
| `sec:9.11` | Case R: Lattimer reads Mesa Corta's P-values |  |
| `sec:9.12` | Practitioner's notebook |  |
| `sec:9.13` | Judgment drill |  |
| `sec:9.14` | A bad year belongs to someone |  |
| `sec:9.15` | Exercises |  |
| `sec:9.16` | Solutions to exercises |  |
| `ex:9.1` | Twenty years of output |  |
| `ex:9.2` | Expected delay |  |
| `ex:9.3` | A skewed overrun |  |
| `ex:9.4` | Comparing spreads |  |
| `ex:9.5` | P-values from a mean and a standard deviation |  |
| `ex:9.6` | Why lenders size on P90 |  |
| `ex:9.7` | One-year, ten-year and twenty-year P90 |  |
| `ex:9.8` | Two wind farms in one portfolio |  |
| `ex:9.9` | Price and volume that move together |  |
| `ex:9.10` | A sensitivity table and tornado |  |
| `ex:9.11` | A coherent downside scenario |  |
| `ex:9.12` | A Monte Carlo simulation |  |
| `exh:9.1` | data and bins table | implied by the brief text; writer assigns this label in order of appearance |
| `exh:9.2` | pgfplots histogram | implied by the brief text; writer assigns this label in order of appearance |
| `exh:9.3` | Standard normal z-values for common exceedance levels |  |
| `exh:9.4` | P90 and P99 by averaging period |  |
| `exh:9.5` | Tornado chart of annual cash |  |
| `exh:9.6` | results table | implied by the brief text; writer assigns this label in order of appearance |
| `exh:9.7` | histogram of simulated cash | implied by the brief text; writer assigns this label in order of appearance |
| `exh:9.8` | Summary of an energy yield assessment |  |
| `exh:9.9` | Case R exceedance levels by asset |  |
| `eq:9.1` | Expected value |  |
| `eq:9.2` | Variance and standard deviation |  |
| `eq:9.3` | Exceedance level under a normal distribution |  |
| `eq:9.4` | Uncertainty over an N-year average |  |
| `eq:9.5` | Root sum of squares |  |
| `eq:9.6` | Covariance |  |
| `eq:9.7` | Correlation coefficient |  |
| `eq:9.8` | Variance of a sum of two outcomes |  |
| `fw:pvalue-reading` | Framework 9.1 P-value reading checklist | home sec:9.10 |
| `fw:uncertainty-tool-choice` | Framework 9.2 Choosing the uncertainty tool | home ssec:9.8.4 |

### Chapter 10: Law for financiers

Source brief: `briefs/u03.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:10` | Law for financiers |  |
| `sec:10.1` | What a contract gives you when the other side fails |  |
| `ssec:10.1.1` | When a promise becomes enforceable |  |
| `ssec:10.1.2` | Damages, mitigation, and remoteness |  |
| `ssec:10.1.3` | Specific performance, injunctions, and termination |  |
| `sec:10.2` | Representations, warranties, covenants, and conditions |  |
| `ssec:10.2.1` | Representations and warranties |  |
| `ssec:10.2.2` | Covenants |  |
| `ssec:10.2.3` | Conditions precedent and conditions subsequent |  |
| `ssec:10.2.4` | Classifying a clause by its consequence |  |
| `sec:10.3` | Indemnities, liability caps, and exclusions |  |
| `ssec:10.3.1` | Indemnities and how they differ from damages |  |
| `ssec:10.3.2` | Liability caps, sub-caps, and carve-outs |  |
| `ssec:10.3.3` | Excluding indirect and consequential loss |  |
| `ssec:10.3.4` | What each party asks for |  |
| `sec:10.4` | Liquidated damages and the rule against penalties |  |
| `ssec:10.4.1` | Why parties agree damages in advance |  |
| `ssec:10.4.2` | The penalty rule in English law |  |
| `ssec:10.4.3` | Penalty clauses in civil law |  |
| `ssec:10.4.4` | LDs, caps, and termination |  |
| `sec:10.5` | Force majeure, frustration, impossibility, and hardship |  |
| `ssec:10.5.1` | What a force majeure clause does |  |
| `ssec:10.5.2` | Frustration in English law and impracticability in New York law |  |
| `ssec:10.5.3` | Force majeure and impossibility in civil codes |  |
| `ssec:10.5.4` | Hardship and imprévision |  |
| `ssec:10.5.5` | The excuse ladder |  |
| `sec:10.6` | Mundra and the limits of force majeure |  |
| `sec:10.7` | Common law and civil law |  |
| `ssec:10.7.1` | Where the law comes from |  |
| `ssec:10.7.2` | Interpretation, good faith, and implied terms |  |
| `ssec:10.7.3` | Differences that change a project financing |  |
| `sec:10.8` | Security and insolvency in principle |  |
| `ssec:10.8.1` | What security is |  |
| `ssec:10.8.2` | What insolvency does |  |
| `ssec:10.8.3` | Why project lenders take security over everything |  |
| `sec:10.9` | Governing law, courts, and arbitration |  |
| `ssec:10.9.1` | Choosing a governing law |  |
| `ssec:10.9.2` | Courts versus arbitration |  |
| `ssec:10.9.3` | The split-law structure of a project financing |  |
| `sec:10.10` | Walkthrough: the architecture of a project contract |  |
| `sec:10.11` | Walkthrough: reading a force majeure clause |  |
| `sec:10.12` | Case P: the first draft of the PPA |  |
| `sec:10.13` | Practitioner's notebook |  |
| `sec:10.14` | Judgment drill |  |
| `sec:10.15` | A contract allocates risk only as far as the asset lets it |  |
| `sec:10.16` | Exercises |  |
| `sec:10.17` | Solutions to exercises |  |
| `ex:10.1` | Damages for a repudiated pellet supply contract and the duty to mitigate |  |
| `ex:10.2` | Classifying six sentences from an O&M agreement |  |
| `ex:10.3` | Warranty claim versus indemnity after a share purchase |  |
| `ex:10.4` | An O&M liability cap and its negligence carve-out |  |
| `ex:10.5` | Testing three delay LD rates against the penalty rule |  |
| `ex:10.6` | Who bears 63 days of force majeure |  |
| `ex:10.7` | A gas price shock under three legal regimes |  |
| `ex:10.8` | Secured recovery in liquidation and in a going-concern sale |  |
| `exh:10.1` | Contract term types, triggers, and remedies (Illustrative) |  |
| `exh:10.2` | Common law and civil law compared for project finance (Illustrative) |  |
| `exh:10.3` | Choosing between courts and arbitration (Illustrative) |  |
| `exh:10.4` | Clause map of an O&M agreement (Illustrative) |  |
| `exh:10.5` | Case P draft PPA provisions under review (Case P) |  |
| `cl:10.1` | Representations and warranties of the Operator, O&M agreement |  |
| `cl:10.2` | Limitation of liability, O&M agreement |  |
| `cl:10.3` | Delay liquidated damages, PPA |  |
| `cl:10.4` | Force majeure, PPA |  |
| `cl:10.5` | Governing law and arbitration, offtake contract |  |
| `fw:clause-consequence-test` | Framework 10.1 Clause consequence test | home ssec:10.2.4 |
| `fw:excuse-ladder` | Framework 10.2 Excuse ladder | home ssec:10.5.5 |

### Chapter 11: How power assets and electricity markets work

Source brief: `briefs/u03.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:11` | How power assets and electricity markets work |  |
| `sec:11.1` | Megawatts, megawatt-hours, and the vocabulary of output |  |
| `ssec:11.1.1` | Capacity and energy |  |
| `ssec:11.1.2` | Availability, dispatch, and capacity factor |  |
| `sec:11.2` | Thermal plants |  |
| `ssec:11.2.1` | Heat rate and efficiency |  |
| `ssec:11.2.2` | Open-cycle, combined-cycle, and steam plants |  |
| `ssec:11.2.3` | Part load, degradation, and the maintenance cycle |  |
| `ssec:11.2.4` | What a financier checks on a thermal plant |  |
| `sec:11.3` | Wind |  |
| `ssec:11.3.1` | The power curve and the wind resource |  |
| `ssec:11.3.2` | From gross to net energy |  |
| `ssec:11.3.3` | Onshore and offshore |  |
| `sec:11.4` | Solar |  |
| `ssec:11.4.1` | Irradiance, modules, and inverters |  |
| `ssec:11.4.2` | DC/AC ratio, trackers, clipping, and degradation |  |
| `ssec:11.4.3` | Concentrating solar power and first-of-a-kind risk |  |
| `sec:11.5` | Hydropower |  |
| `ssec:11.5.1` | Head, flow, and output |  |
| `ssec:11.5.2` | Run-of-river, reservoir, and pumped storage |  |
| `ssec:11.5.3` | Hydrology and the dry year |  |
| `sec:11.6` | Nuclear |  |
| `ssec:11.6.1` | How a reactor makes power |  |
| `ssec:11.6.2` | Why nuclear economics are about capital and time |  |
| `sec:11.7` | Batteries |  |
| `ssec:11.7.1` | Power, energy, and duration |  |
| `ssec:11.7.2` | Round-trip efficiency, cycles, degradation, and augmentation |  |
| `ssec:11.7.3` | Fire, safety, and site design |  |
| `sec:11.8` | Comparing technologies with levelized cost |  |
| `sec:11.9` | Grids |  |
| `ssec:11.9.1` | Transmission, distribution, and the system operator |  |
| `ssec:11.9.2` | Frequency, inertia, and the grid code |  |
| `ssec:11.9.3` | Connecting a plant and the interface risk |  |
| `sec:11.10` | How electricity markets set prices |  |
| `ssec:11.10.1` | Market models |  |
| `ssec:11.10.2` | Merit order and marginal pricing |  |
| `ssec:11.10.3` | Scarcity pricing and energy-only markets |  |
| `ssec:11.10.4` | Capacity markets and ancillary services |  |
| `ssec:11.10.5` | Spark spreads and dark spreads |  |
| `sec:11.11` | Nodal and zonal pricing, congestion, curtailment, and negative prices |  |
| `ssec:11.11.1` | Zonal and nodal markets |  |
| `ssec:11.11.2` | Congestion and locational prices |  |
| `ssec:11.11.3` | Curtailment |  |
| `ssec:11.11.4` | Negative prices |  |
| `sec:11.12` | Capture prices and cannibalization |  |
| `sec:11.13` | Chile's northern solar and the price of location |  |
| `sec:11.14` | Walkthrough: reading a gas turbine plant's performance guarantee sheet |  |
| `sec:11.15` | Case P: choosing Bélanou's machines |  |
| `sec:11.16` | Case R: why Mesa Corta's solar earns less than the hub |  |
| `sec:11.17` | Practitioner's notebook |  |
| `sec:11.18` | Judgment drill |  |
| `sec:11.19` | Megawatt-hours have to come from somewhere |  |
| `sec:11.20` | Exercises |  |
| `sec:11.21` | Solutions to exercises |  |
| `ex:11.1` | Energy from a combined-cycle plant |  |
| `ex:11.2` | Fuel and carbon cost per MWh for three thermal plants |  |
| `ex:11.3` | From gross to net energy at a wind farm |  |
| `ex:11.4` | A tracking solar plant's first-year and later energy |  |
| `ex:11.5` | Output of a run-of-river hydro plant in a mean and a dry year |  |
| `ex:11.6` | A day of arbitrage for a four-hour battery |  |
| `ex:11.7` | Levelized cost for four technologies at two discount rates |  |
| `ex:11.8` | Clearing the market in four hours |  |
| `ex:11.9` | Congestion between two nodes |  |
| `ex:11.10` | Capture price and capture ratio for a solar plant on two days |  |
| `exh:11.1` | Thermal generating technologies compared (Illustrative) |  |
| `exh:11.2` | Levelized cost of electricity at two discount rates (Illustrative) |  |
| `exh:11.3` | Electricity market models and who bears price and volume risk (Illustrative) |  |
| `exh:11.4` | Merit-order stack for Example 11.8 (Illustrative) |  |
| `exh:11.5` | Merit-order supply curve and four demand levels (Illustrative) |  |
| `exh:11.6` | Two-node system with a congested line (Illustrative) |  |
| `exh:11.7` | Hourly prices and solar output on a typical and a spring day (Illustrative) |  |
| `exh:11.8` | Performance guarantee sheet for a 2x1 F-class combined cycle (Illustrative) |  |
| `exh:11.9` | Bélanou plant parameters (Case P) |  |
| `exh:11.10` | Mesa Corta capture-ratio assumptions by technology and hub (Case R) |  |
| `eq:11.1` | Capacity factor |  |
| `eq:11.2` | Efficiency from heat rate |  |
| `eq:11.3` | Fuel cost per MWh |  |
| `eq:11.4` | Hydro power |  |
| `eq:11.5` | Battery charge energy |  |
| `eq:11.6` | LCOE |  |
| `eq:11.7` | Clean spark spread |  |
| `eq:11.8` | Capture price |  |
| `eq:11.9` | Capture ratio |  |
| `fw:megawatt-to-revenue` | Framework 11.1 Megawatt-to-revenue chain | home sec:11.14 |

### Chapter 12: How resource, transport, social and digital assets work

Source brief: `briefs/u03.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:12` | How resource, transport, social and digital assets work |  |
| `sec:12.1` | Oil and gas from reservoir to market |  |
| `ssec:12.1.1` | Reservoirs, resources, and reserves |  |
| `ssec:12.1.2` | Build-up, plateau, and decline in production |  |
| `ssec:12.1.3` | Processing and pipelines |  |
| `ssec:12.1.4` | Oil from field to refinery |  |
| `sec:12.2` | The LNG chain |  |
| `ssec:12.2.1` | Liquefaction |  |
| `ssec:12.2.2` | Shipping and regasification |  |
| `ssec:12.2.3` | The delivered cost stack |  |
| `ssec:12.2.4` | Sabine Pass and PNG LNG as two shapes of the chain |  |
| `sec:12.3` | Mines and processing plants |  |
| `ssec:12.3.1` | Resources, reserves, and the competent person |  |
| `ssec:12.3.2` | Open-pit and underground mining |  |
| `ssec:12.3.3` | From ore to saleable product |  |
| `ssec:12.3.4` | Cut-off grade, mine life, tailings, and closure |  |
| `ssec:12.3.5` | Oyu Tolgoi and the geology of cost |  |
| `sec:12.4` | Roads, bridges, and tunnels |  |
| `ssec:12.4.1` | Measuring traffic |  |
| `ssec:12.4.2` | Revenue, ramp-up, and elasticity |  |
| `ssec:12.4.3` | Building roads, bridges, and tunnels |  |
| `ssec:12.4.4` | Operating a road |  |
| `sec:12.5` | Rail and urban transit |  |
| `sec:12.6` | Airports |  |
| `sec:12.7` | Ports |  |
| `sec:12.8` | Hospitals and other social infrastructure |  |
| `sec:12.9` | Desalination and water treatment |  |
| `sec:12.10` | Fiber networks and towers |  |
| `sec:12.11` | Data centers |  |
| `sec:12.12` | Walkthrough: mapping a physical chain from source to customer |  |
| `sec:12.13` | Walkthrough: reading a mineral reserve statement |  |
| `sec:12.14` | Case P: the gas behind Bélanou |  |
| `sec:12.15` | Case T: the Merrick Link on the ground |  |
| `sec:12.16` | Practitioner's notebook |  |
| `sec:12.17` | Judgment drill |  |
| `sec:12.18` | Physics sets the risks before anyone drafts a word |  |
| `sec:12.19` | Exercises |  |
| `sec:12.20` | Solutions to exercises |  |
| `ex:12.1` | A gas field's plateau, decline, and the plant it can feed |  |
| `ex:12.2` | The delivered cost of LNG |  |
| `ex:12.3` | From ore to copper concentrate |  |
| `ex:12.4` | Toll revenue through ramp-up |  |
| `ex:12.5` | Farebox recovery on a light rail line |  |
| `ex:12.6` | An airport's revenue under single and dual till |  |
| `ex:12.7` | Container terminal capacity and utilization |  |
| `ex:12.8` | A hospital's hard FM and lifecycle profile |  |
| `ex:12.9` | The cost of a cubic meter of desalinated water |  |
| `ex:12.10` | A fiber network's take-up curve |  |
| `ex:12.11` | Power for a 48 MW data center |  |
| `exh:12.1` | Gas and LNG units and conversions (Illustrative) |  |
| `exh:12.2` | Delivered LNG cost stack (Illustrative) |  |
| `exh:12.3` | Physical chain map for an LNG-to-power project (Illustrative) |  |
| `exh:12.4` | Mineral resource and ore reserve statement for a copper mine (Illustrative) |  |
| `exh:12.5` | Bélanou's physical gas-to-power chain (Case P) |  |
| `exh:12.6` | Merrick Link physical description (Case T) |  |
| `eq:12.1` | Exponential decline |  |
| `eq:12.2` | Recovered metal |  |
| `eq:12.3` | Break-even cut-off grade |  |
| `eq:12.4` | Toll revenue |  |
| `eq:12.5` | Facility power from IT load and PUE |  |
| `eq:12.6` | Desalination energy cost |  |
| `fw:physical-chain-map` | Framework 12.1 Physical chain map | home sec:12.12 |

### Chapter 13: Excel for project finance

Source brief: `briefs/u03.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:13` | Excel for project finance |  |
| `sec:13.1` | How a project finance workbook is laid out |  |
| `ssec:13.1.1` | Inputs, calculations, checks, and outputs on separate sheets |  |
| `ssec:13.1.2` | Time across columns, one formula per row |  |
| `ssec:13.1.3` | Units, signs, and colors |  |
| `sec:13.2` | Cell references and the copy-across discipline |  |
| `sec:13.3` | Dates, counters, and timing flags |  |
| `ssec:13.3.1` | Period dates with EOMONTH and EDATE |  |
| `ssec:13.3.2` | Counters and flags |  |
| `ssec:13.3.3` | Stub periods and day fractions |  |
| `sec:13.4` | Core functions |  |
| `ssec:13.4.1` | Sums and SUMPRODUCT |  |
| `ssec:13.4.2` | Caps, floors, and cumulative limits |  |
| `ssec:13.4.3` | Lookups with INDEX, MATCH, and XLOOKUP |  |
| `ssec:13.4.4` | Logic without nested IFs |  |
| `ssec:13.4.5` | Excel's finance functions and their traps |  |
| `sec:13.5` | Fragile formulas and how to replace them |  |
| `sec:13.6` | Range names and the one exception |  |
| `sec:13.7` | Data tables and goal seek |  |
| `ssec:13.7.1` | One-way and two-way data tables |  |
| `ssec:13.7.2` | Goal seek |  |
| `ssec:13.7.3` | Limits of both tools |  |
| `sec:13.8` | Circular references |  |
| `ssec:13.8.1` | Where circularity comes from in project models |  |
| `ssec:13.8.2` | Iterative calculation and why lenders dislike it |  |
| `ssec:13.8.3` | The copy-paste macro |  |
| `ssec:13.8.4` | Closed-form solutions |  |
| `sec:13.9` | Error checks |  |
| `sec:13.10` | Walkthrough: building a practice workbook cell by cell |  |
| `sec:13.11` | Case P: Bélanou's construction timeline in a practice workbook |  |
| `sec:13.12` | Practitioner's notebook |  |
| `sec:13.13` | Judgment drill |  |
| `sec:13.14` | A trustworthy workbook needs an architecture before it needs formulas |  |
| `sec:13.15` | Exercises |  |
| `sec:13.16` | Solutions to exercises |  |
| `ex:13.1` | Indexing a tariff with mixed references |  |
| `ex:13.2` | Construction and operations flags with a stub period |  |
| `ex:13.3` | A cumulative cap with MIN |  |
| `ex:13.4` | Choosing a scenario and looking up an index |  |
| `ex:13.5` | How an OFFSET formula broke a revenue line |  |
| `ex:13.6` | A two-way data table of NPV |  |
| `ex:13.7` | Goal seek for a breakeven tariff |  |
| `ex:13.8` | Resolving an IDC circularity three ways |  |
| `ex:13.9` | Designing the checks for the practice workbook |  |
| `exh:13.1` | Fragile formulas and robust replacements (Illustrative) |  |
| `exh:13.2` | Two-way data table of NPV by tariff and discount rate (Illustrative) |  |
| `exh:13.3` | The interest-during-construction loop (Illustrative) |  |
| `exh:13.4` | Bélanou EPC payment profile, financial close base case, percent of contract price by month (Case P) |  |
| `eq:13.1` | Timing flag |  |
| `eq:13.2` | Operating fraction of a period |  |
| `eq:13.3` | Capped cumulative accrual |  |
| `eq:13.4` | Closed-form debt with IDC |  |
| `fw:formula-robustness-test` | Framework 13.1 Formula robustness test | home sec:13.5 |

### Chapter 14: The risk taxonomy

Source brief: `briefs/u04.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:14` | The risk taxonomy |  |
| `sec:14.1` | What counts as a project risk |  |
| `ssec:14.1.1` | Risk as variation that someone must absorb |  |
| `ssec:14.1.2` | The risk card |  |
| `ssec:14.1.3` | Why classification decides who pays |  |
| `sec:14.2` | How the risk profile changes over the project's life |  |
| `ssec:14.2.1` | Development: high probability, small money |  |
| `ssec:14.2.2` | Construction and commissioning: the peak |  |
| `ssec:14.2.3` | Ramp-up and steady operations |  |
| `ssec:14.2.4` | End of life |  |
| `sec:14.3` | Development and permitting risk |  |
| `ssec:14.3.1` | What kills projects before financial close |  |
| `ssec:14.3.2` | Permits that are challenged after they are granted |  |
| `sec:14.4` | Construction risk: cost, time and performance |  |
| `ssec:14.4.1` | Cost overrun |  |
| `ssec:14.4.2` | Delay and what a day costs |  |
| `ssec:14.4.3` | Performance shortfall |  |
| `ssec:14.4.4` | When the fixed price does not hold |  |
| `sec:14.5` | Technology risk |  |
| `ssec:14.5.1` | Proven, scaled-up and first-of-a-kind |  |
| `ssec:14.5.2` | A plant that runs but does not deliver the contracted output |  |
| `ssec:14.5.3` | Manufacturing scale-up as technology risk |  |
| `sec:14.6` | Resource and reserves risk |  |
| `ssec:14.6.1` | Resource uncertainty by asset type |  |
| `ssec:14.6.2` | Resource risk after completion |  |
| `sec:14.7` | Demand, volume, price and market risk |  |
| `ssec:14.7.1` | Demand and volume risk |  |
| `ssec:14.7.2` | Price and market risk |  |
| `ssec:14.7.3` | Curtailment as volume risk created by the grid |  |
| `sec:14.8` | Input supply risk |  |
| `ssec:14.8.1` | Quantity, quality, price and delivery |  |
| `ssec:14.8.2` | The fuel price the bid assumed |  |
| `sec:14.9` | Operating risk |  |
| `ssec:14.9.1` | Availability, performance and cost |  |
| `ssec:14.9.2` | Catastrophic loss and the size of insurance limits |  |
| `sec:14.10` | Counterparty credit risk |  |
| `ssec:14.10.1` | Every counterparty is a credit |  |
| `ssec:14.10.2` | The offtaker that cannot pay |  |
| `ssec:14.10.3` | The contractor that fails mid-build |  |
| `ssec:14.10.4` | Concentration |  |
| `sec:14.11` | Interface risk |  |
| `ssec:14.11.1` | Where one party's work meets another's |  |
| `ssec:14.11.2` | A wind farm with no line to the market |  |
| `sec:14.12` | Interest rate, inflation, refinancing and liquidity risk |  |
| `ssec:14.12.1` | Interest rate risk |  |
| `ssec:14.12.2` | Inflation risk and indexation mismatch |  |
| `ssec:14.12.3` | Refinancing risk |  |
| `ssec:14.12.4` | Liquidity risk |  |
| `sec:14.13` | Currency risk: devaluation, convertibility and transfer |  |
| `ssec:14.13.1` | Devaluation and the currency mismatch |  |
| `ssec:14.13.2` | Convertibility and transfer |  |
| `sec:14.14` | Political risk |  |
| `ssec:14.14.1` | Expropriation, direct and creeping |  |
| `ssec:14.14.2` | Political violence |  |
| `ssec:14.14.3` | Breach of contract, change in law and non-honoring |  |
| `ssec:14.14.4` | Sanctions |  |
| `sec:14.15` | Regulatory, legal and enforceability risk |  |
| `ssec:14.15.1` | Regulatory risk |  |
| `ssec:14.15.2` | Legal validity and enforceability |  |
| `sec:14.16` | Environmental and social risk |  |
| `ssec:14.16.1` | How E&S failures become cash-flow events |  |
| `sec:14.17` | Force majeure as an overlay on the categories |  |
| `ssec:14.17.1` | Natural and political force majeure |  |
| `ssec:14.17.2` | Prolonged force majeure and pandemic relief |  |
| `sec:14.18` | Sponsor risk |  |
| `ssec:14.18.1` | Sponsor credit, commitment and conflicts |  |
| `sec:14.19` | Climate, cyber and decommissioning risk |  |
| `ssec:14.19.1` | Physical climate risk |  |
| `ssec:14.19.2` | Transition risk |  |
| `ssec:14.19.3` | Cyber risk |  |
| `ssec:14.19.4` | Decommissioning risk |  |
| `sec:14.20` | How risks cluster and travel together |  |
| `ssec:14.20.1` | Common triggers |  |
| `ssec:14.20.2` | Wrong-way risk |  |
| `sec:14.21` | Walkthrough: building a risk register from a project description |  |
| `sec:14.22` | Case P: Kilnworth's bid-stage risk register |  |
| `sec:14.23` | Practitioner's notebook |  |
| `sec:14.24` | Judgment drill |  |
| `sec:14.25` | A list of risks does not say who should carry them |  |
| `sec:14.26` | Exercises |  |
| `sec:14.27` | Solutions to exercises |  |
| `ex:14.1` | What a 90-day delay costs a wind farm (Illustrative) |  |
| `ex:14.2` | A geothermal field that declines faster than forecast (Illustrative) |  |
| `ex:14.3` | Operating leverage on a toll road (Illustrative) |  |
| `ex:14.4` | The coal price the bid assumed (Illustrative) |  |
| `ex:14.5` | Interest rates and inflation on an availability-payment rail PPP (Illustrative) |  |
| `ex:14.6` | A mini-perm's maturity (Illustrative) |  |
| `ex:14.7` | A local-currency tariff and a dollar loan (Illustrative) |  |
| `exh:14.1` | The risk card template (Illustrative) |  |
| `exh:14.2` | One event, four labels, four bearers (Illustrative, built on the Mundra fact pattern) |  |
| `exh:14.3` | Money at risk across a project's life (Illustrative) |  |
| `exh:14.4` | Phase-by-category risk map for a contracted thermal IPP (Illustrative) |  |
| `exh:14.5` | How a devaluation triggers a cluster of risks (Illustrative) |  |
| `exh:14.6` | Risk register for a 140 MW run-of-river hydropower project (Illustrative) |  |
| `exh:14.7` | Case P risk register v1, October 2016 (Case P) |  |
| `eq:14.1` | Daily cost of delay |  |
| `eq:14.2` | Operating leverage multiplier |  |
| `eq:14.3` | FX breakeven rate |  |
| `fw:risk-card` | Framework 14.1 The risk card | home ssec:14.1.2 |
| `fw:phase-risk-map` | Framework 14.2 Phase-by-category risk map | home ssec:14.2.4 |

### Chapter 15: Analyzing, allocating and pricing risk

Source brief: `briefs/u04.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:15` | Analyzing, allocating and pricing risk |  |
| `sec:15.1` | The risk management cycle on a project |  |
| `ssec:15.1.1` | Seven steps and what each produces |  |
| `ssec:15.1.2` | Who runs the cycle at each stage |  |
| `ssec:15.1.3` | Finding the risks nobody listed |  |
| `sec:15.2` | Analyzing a risk: from trigger to cash flow |  |
| `ssec:15.2.1` | Mechanism and drivers |  |
| `ssec:15.2.2` | Which risks deserve numbers |  |
| `sec:15.3` | Quantifying risk |  |
| `ssec:15.3.1` | Expected loss and the tail |  |
| `ssec:15.3.2` | Three-point estimates and discrete scenarios |  |
| `ssec:15.3.3` | Correlated risks and joint scenarios |  |
| `ssec:15.3.4` | Risks that resist numbers |  |
| `sec:15.4` | Building a risk matrix |  |
| `ssec:15.4.1` | The scoring matrix |  |
| `ssec:15.4.2` | The allocation matrix |  |
| `ssec:15.4.3` | What heat maps hide |  |
| `sec:15.5` | Allocating risk |  |
| `ssec:15.5.1` | From principle to a working test |  |
| `ssec:15.5.2` | Pass-through to the offtaker, users or the state |  |
| `ssec:15.5.3` | Back-to-back with contractors and suppliers |  |
| `ssec:15.5.4` | Risks no private party can carry: retention and sharing bands |  |
| `sec:15.6` | Residual risk: what equity and debt are left holding |  |
| `ssec:15.6.1` | Payoff shapes |  |
| `ssec:15.6.2` | Residual risk after allocation |  |
| `sec:15.7` | Why lenders watch the downside and sponsors the upside |  |
| `ssec:15.7.1` | What volatility does to each claim |  |
| `ssec:15.7.2` | Behaviors the asymmetry explains |  |
| `sec:15.8` | Pricing risk |  |
| `ssec:15.8.1` | What each bearer charges |  |
| `ssec:15.8.2` | The price of transfer against the cost of retention |  |
| `ssec:15.8.3` | How risk reaches the tariff |  |
| `sec:15.9` | What "bankable" means |  |
| `ssec:15.9.1` | A definition that lenders would sign |  |
| `ssec:15.9.2` | The bankability ladder |  |
| `ssec:15.9.3` | Moving a risk up the ladder, and what it costs |  |
| `sec:15.10` | Allocation on paper and allocation in practice |  |
| `ssec:15.10.1` | Whether the bearer can pay when the loss happens |  |
| `ssec:15.10.2` | Evidence from failed allocations |  |
| `ssec:15.10.3` | Exit rights change behavior |  |
| `sec:15.11` | Monitoring risk after financial close |  |
| `ssec:15.11.1` | The live register and key risk indicators |  |
| `sec:15.12` | Walkthrough: turning a risk register into an allocation matrix |  |
| `sec:15.13` | Case P: the risk matrix and the grid-interface argument |  |
| `sec:15.14` | Practitioner's notebook |  |
| `sec:15.15` | Judgment drill |  |
| `sec:15.16` | An allocated risk still needs a tool that pays when it happens |  |
| `sec:15.17` | Exercises |  |
| `sec:15.18` | Solutions to exercises |  |
| `ex:15.1` | Sizing a cost-overrun risk from three estimates (Illustrative) |  |
| `ex:15.2` | A risk matrix for a desalination plant, and what it hides (Illustrative) |  |
| `ex:15.3` | Residual risk and the asymmetry of debt and equity (Illustrative) |  |
| `ex:15.4` | Paying a contractor to take construction risk, or keeping it (Illustrative) |  |
| `ex:15.5` | A back-to-back that is not (Illustrative) |  |
| `ex:15.6` | What a delay-LD promise is worth (Illustrative) |  |
| `exh:15.1` | The risk management cycle (Illustrative) |  |
| `exh:15.2` | Heat map for the desalination plant (Illustrative) |  |
| `exh:15.3` | Allocation matrix template (Illustrative) |  |
| `exh:15.4` | Debt and equity payoffs against project value (Illustrative) |  |
| `exh:15.5` | The bankability ladder (Illustrative) |  |
| `exh:15.6` | Allocation matrix for the 140 MW run-of-river hydropower project (Illustrative) |  |
| `exh:15.7` | Case P risk matrix, March 2017 (Case P) |  |
| `cl:15.1` | (caption not stated in brief; writer supplies) | implied by the brief text; writer assigns this label in order of appearance |
| `eq:15.1` | Expected loss |  |
| `eq:15.2` | Debt payoff |  |
| `eq:15.3` | Equity payoff |  |
| `eq:15.4` | Risk-adjusted value of a protection |  |
| `eq:15.5` | Cost of retaining a risk |  |
| `fw:risk-cycle` | Framework 15.1 Risk management cycle | home ssec:15.1.1 |
| `fw:allocation-test` | Framework 15.2 Allocation test | home ssec:15.5.1 |
| `fw:bankability-ladder` | Framework 15.3 Bankability ladder | home ssec:15.9.2 |

### Chapter 16: The mitigation toolkit

Source brief: `briefs/u04.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:16` | The mitigation toolkit |  |
| `sec:16.1` | What mitigation does to a risk |  |
| `ssec:16.1.1` | Avoid, reduce, transfer, absorb |  |
| `ssec:16.1.2` | Eight tool families and the risks they serve |  |
| `sec:16.2` | Contracts as mitigation |  |
| `ssec:16.2.1` | Revenue contracts that remove market risk |  |
| `ssec:16.2.2` | Construction and operating contracts that move physical risk |  |
| `ssec:16.2.3` | What contracts cannot do |  |
| `sec:16.3` | Insurance |  |
| `ssec:16.3.1` | What insurance covers and what it leaves |  |
| `ssec:16.3.2` | Choosing a deductible |  |
| `sec:16.4` | Guarantees and payment security |  |
| `ssec:16.4.1` | Who guarantees what |  |
| `ssec:16.4.2` | Layered payment security |  |
| `sec:16.5` | Reserves and liquidity |  |
| `ssec:16.5.1` | Contingency, reserve accounts and standby facilities |  |
| `ssec:16.5.2` | What a reserve costs |  |
| `sec:16.6` | Hedges |  |
| `ssec:16.6.1` | Interest rate, currency and commodity hedges |  |
| `ssec:16.6.2` | The price of currency cover |  |
| `ssec:16.6.3` | Hedges that create risk |  |
| `sec:16.7` | Structural features |  |
| `ssec:16.7.1` | Leverage, tenor and repayment shape |  |
| `ssec:16.7.2` | Cash traps, sweeps, covenants and control |  |
| `sec:16.8` | Sponsor support |  |
| `ssec:16.8.1` | Completion support and contingent equity |  |
| `ssec:16.8.2` | How much support before non-recourse is lost |  |
| `sec:16.9` | Credit enhancement |  |
| `ssec:16.9.1` | Third-party wraps, guarantees and subordinated public money |  |
| `ssec:16.9.2` | State support for tail risks |  |
| `sec:16.10` | Combining tools: the layered loss stack |  |
| `ssec:16.10.1` | Order of loss absorption |  |
| `ssec:16.10.2` | Tracing a construction overrun through the stack |  |
| `sec:16.11` | Choosing tools |  |
| `ssec:16.11.1` | The mitigation selection grid |  |
| `ssec:16.11.2` | Testing whether a mitigant is worth its price |  |
| `sec:16.12` | How mitigation fails |  |
| `ssec:16.12.1` | Common-mode failure and collectability |  |
| `ssec:16.12.2` | Basis, gaps and small security |  |
| `sec:16.13` | Walkthrough: writing a mitigation plan for a risk matrix |  |
| `sec:16.14` | Case P: the mitigation plan |  |
| `sec:16.15` | Practitioner's notebook |  |
| `sec:16.16` | Judgment drill |  |
| `sec:16.17` | Every mitigant is a promise by someone who must still perform |  |
| `sec:16.18` | Exercises |  |
| `sec:16.19` | Solutions to exercises |  |
| `ex:16.1` | Three ways to cover three months of late payment (Illustrative) |  |
| `ex:16.2` | Choosing an insurance deductible for a battery plant (Illustrative) |  |
| `ex:16.3` | Tracing a construction overrun through the loss stack (Illustrative) |  |
| `ex:16.4` | What currency cover costs (Illustrative) |  |
| `ex:16.5` | Whether a partial credit guarantee is worth its fee (Illustrative) |  |
| `exh:16.1` | Tool families, the responses they provide and who pays (Illustrative) |  |
| `exh:16.2` | The layered loss stack (Illustrative) |  |
| `exh:16.3` | Construction overrun through the loss stack (USD m) (Illustrative) |  |
| `exh:16.4` | Selection grid applied to the desalination plant's risks (Illustrative) |  |
| `exh:16.5` | Mitigation plan for the desalination plant (Illustrative) |  |
| `exh:16.6` | Case P mitigation plan, May 2017 proposal against terms at financial close (Case P) |  |
| `eq:16.1` | Carrying cost of a cash reserve |  |
| `eq:16.2` | Forward exchange rate from the interest differential |  |
| `eq:16.3` | Net benefit of a mitigant |  |
| `fw:mitigation-grid` | Framework 16.1 Mitigation selection grid | home ssec:16.11.1 |
| `fw:loss-stack` | Framework 16.2 Layered loss stack | home ssec:16.10.1 |
| `fw:mitigation-test` | Framework 16.3 Mitigation cost-benefit test | home ssec:16.11.2 |

### Chapter 17: Concessions, implementation agreements and government support

Source brief: `briefs/u05.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:17` | Concessions, implementation agreements and government support |  |
| `sec:17.1` | What the state signs and why |  |
| `ssec:17.1.1` | Concessions, project agreements and implementation agreements |  |
| `ssec:17.1.2` | Where the government agreement sits in the contractual web |  |
| `ssec:17.1.3` | Administrative contracts and economic equilibrium |  |
| `sec:17.2` | Granting the rights |  |
| `ssec:17.2.1` | Grant, term and exclusivity |  |
| `ssec:17.2.2` | Undertakings that make a project financeable |  |
| `ssec:17.2.3` | What the project company gives up |  |
| `sec:17.3` | Allocating government risk during the term |  |
| `ssec:17.3.1` | Change in law |  |
| `ssec:17.3.2` | Compensation events, MAGA and relief events |  |
| `ssec:17.3.3` | Force majeure in a government contract |  |
| `sec:17.4` | Termination and what the state pays |  |
| `ssec:17.4.1` | Termination events and cure |  |
| `ssec:17.4.2` | Four ways to compensate |  |
| `ssec:17.4.3` | Computing termination amounts |  |
| `ssec:17.4.4` | Defining the protected debt |  |
| `ssec:17.4.5` | Paying the termination amount |  |
| `sec:17.5` | Government support instruments |  |
| `ssec:17.5.1` | The support spectrum |  |
| `ssec:17.5.2` | Sovereign guarantees |  |
| `ssec:17.5.3` | Letters of support and comfort letters |  |
| `ssec:17.5.4` | Testing an instrument's strength |  |
| `ssec:17.5.5` | What support costs the state |  |
| `sec:17.6` | Hub Power and the implementation agreement as enabling legislation |  |
| `sec:17.7` | Guarantee chains that paid and one that did not: Lake Turkana, REIPPPP and Dabhol |  |
| `sec:17.8` | Walkthrough: marking up an implementation agreement's termination schedule |  |
| `sec:17.9` | Case P: the tender, the implementation agreement and the guarantee |  |
| `sec:17.10` | Practitioner's notebook |  |
| `sec:17.11` | Judgment drill |  |
| `sec:17.12` | A guarantee pays only what the offtake contract says is owed |  |
| `sec:17.13` | Exercises |  |
| `sec:17.14` | Solutions to exercises |  |
| `ex:17.1` | A new levy and the change-in-law threshold |  |
| `ex:17.2` | Restoring economic equilibrium by term extension or by tariff |  |
| `ex:17.3` | Termination compensation for a 320 MW gas-fired IPP under three termination grounds |  |
| `ex:17.4` | Sizing a sovereign guarantee cap |  |
| `exh:17.1` | Concessions, project agreements and implementation agreements compared |  |
| `exh:17.2` | The government agreement in the contractual web (diagram) |  |
| `exh:17.3` | Termination compensation matrix for an emerging-market IPP and an OECD user-pay concession |  |
| `exh:17.4` | Government support instruments compared |  |
| `exh:17.5` | Guaranteed exposure against a flat guarantee cap (USD m) |  |
| `exh:17.6` | Illustrative IA termination schedule |  |
| `exh:17.7` | Case P termination compensation regime |  |
| `cl:17.1` | Grant of rights, implementation agreement |  |
| `cl:17.2` | Convertibility and transfer undertaking, implementation agreement |  |
| `cl:17.3` | Change in law, implementation agreement |  |
| `cl:17.4` | Termination amount on project company default, implementation agreement |  |
| `cl:17.5` | Put option on offtaker payment default, implementation agreement |  |
| `cl:17.6` | Demand under a sovereign guarantee |  |
| `cl:17.7` | Letter of support from a finance ministry |  |
| `eq:17.1` | Equity compensation, greater-of formula: $E^{comp}} = (_{k} Dist}_{k}/(1+r_E)^{k},\ E_0(1+r_E)^{} - Dist}^{rec}})$ |  |
| `eq:17.2` | Termination amount on government default: $TA} = D + SB} + E^{comp}}$ |  |
| `fw:termination-compensation-matrix` | Framework 17.1 Termination compensation matrix | home ssec:17.4.2 |
| `fw:support-strength-test` | Framework 17.2 Support instrument strength test | home ssec:17.5.4 |

### Chapter 18: Power purchase and tolling agreements

Source brief: `briefs/u05.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:18` | Power purchase and tolling agreements |  |
| `sec:18.1` | What a power purchase agreement pays for |  |
| `ssec:18.1.1` | The two-part tariff |  |
| `ssec:18.1.2` | Single-part tariffs for wind and solar |  |
| `ssec:18.1.3` | Term, conditions precedent and the required commercial operation date |  |
| `sec:18.2` | Capacity payments and availability |  |
| `ssec:18.2.1` | Contracted capacity and capacity tests |  |
| `ssec:18.2.2` | Availability and the capacity payment |  |
| `ssec:18.2.3` | Deemed availability and offtaker risk events |  |
| `sec:18.3` | Energy payments, dispatch and fuel pass-through |  |
| `ssec:18.3.1` | Dispatch |  |
| `ssec:18.3.2` | The fuel charge and the contracted heat rate |  |
| `ssec:18.3.3` | Other pass-throughs |  |
| `sec:18.4` | Volume risk: take-or-pay, deemed energy and curtailment |  |
| `ssec:18.4.1` | Take-or-pay in an offtake contract |  |
| `ssec:18.4.2` | Deemed energy |  |
| `ssec:18.4.3` | Curtailment |  |
| `sec:18.5` | Indexation and currency |  |
| `ssec:18.5.1` | Matching indexation to costs |  |
| `ssec:18.5.2` | Denomination and payment currency |  |
| `ssec:18.5.3` | Tariff reviews and regulatory approval |  |
| `sec:18.6` | Getting paid |  |
| `ssec:18.6.1` | Invoicing, disputes and late payment |  |
| `ssec:18.6.2` | Payment security in outline |  |
| `ssec:18.6.3` | PPA termination |  |
| `sec:18.7` | Tolling agreements |  |
| `ssec:18.7.1` | How a tolling agreement works |  |
| `ssec:18.7.2` | PPA or tolling for a gas plant |  |
| `ssec:18.7.3` | Where tolling is used |  |
| `sec:18.8` | Tata Mundra and the price of an unindexed fuel charge |  |
| `sec:18.9` | Lake Turkana and who pays when the grid is late |  |
| `sec:18.10` | Walkthrough: building one month's PPA invoice |  |
| `sec:18.11` | Case P: negotiating the Bélanou PPA |  |
| `sec:18.12` | Practitioner's notebook |  |
| `sec:18.13` | Judgment drill |  |
| `sec:18.14` | A PPA is only as strong as the buyer who signs it |  |
| `sec:18.15` | Exercises |  |
| `sec:18.16` | Solutions to exercises |  |
| `ex:18.1` | Capacity payment at three availability levels |  |
| `ex:18.2` | Fuel charge, heat-rate headroom and the project company's fuel margin |  |
| `ex:18.3` | Part-load dispatch and who pays for it |  |
| `ex:18.4` | Deemed energy for a wind farm whose grid connection is late |  |
| `ex:18.5` | Sizing an offtaker letter of credit |  |
| `ex:18.6` | PPA with fuel pass-through or tolling agreement |  |
| `ex:18.7` | What an unindexed fuel charge cost Mundra |  |
| `exh:18.1` | Tariff-to-cost map for an illustrative CCGT |  |
| `exh:18.2` | Availability, outage allowance and offtaker risk events (illustrative month) |  |
| `exh:18.3` | Volume risk allocation under three PPA positions |  |
| `exh:18.4` | Risk allocation under a fuel pass-through PPA and a tolling agreement |  |
| `exh:18.5` | Illustrative monthly PPA invoice |  |
| `exh:18.6` | Case P January 2022 invoice (Case P) |  |
| `cl:18.1` | Capacity payment, PPA |  |
| `cl:18.2` | Fuel charge and contracted heat rate, PPA |  |
| `cl:18.3` | Deemed energy, PPA |  |
| `cl:18.4` | Curtailment compensation, PPA |  |
| `cl:18.5` | Letter of credit replenishment and cure, PPA |  |
| `cl:18.6` | Fuel supply and conversion efficiency, tolling agreement |  |
| `eq:18.1` | Capacity payment: $CP}_t = C 1{,}000 cpr} IF}_t (1, A_t/A^{*}) m_t$ |  |
| `eq:18.2` | Fuel charge: $EP}^{fuel}}_t = E^{del}}_t HR}^{c}} k_{HHV/LHV}} p^{fuel}}_t / 1{,}055.06$ |  |
| `eq:18.3` | Variable O&M charge: $VOM}_t = E^{del}}_t vom} IF}^{VOM}}_t$ |  |
| `fw:tariff-to-cost-match` | Framework 18.1 Tariff-to-cost match test | home ssec:18.1.1 |
| `fw:volume-risk-checklist` | Framework 18.2 Volume risk allocation checklist | home ssec:18.4.1 |

### Chapter 19: Feed-in tariffs, contracts for difference and regulated asset base models

Source brief: `briefs/u05.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:19` | Feed-in tariffs, contracts for difference and regulated asset base models |  |
| `sec:19.1` | Supporting a project without an offtaker |  |
| `ssec:19.1.1` | The financing problem a support scheme solves |  |
| `ssec:19.1.2` | Five designs on one axis |  |
| `sec:19.2` | Feed-in tariffs and premiums |  |
| `ssec:19.2.1` | How a feed-in tariff works |  |
| `ssec:19.2.2` | Premiums on top of the market |  |
| `ssec:19.2.3` | From administrative tariffs to auctions |  |
| `sec:19.3` | Spain and the support that was a statute |  |
| `sec:19.4` | Contracts for difference |  |
| `ssec:19.4.1` | The two-sided CfD |  |
| `ssec:19.4.2` | What the reference price leaves behind |  |
| `ssec:19.4.3` | Negative prices and curtailment |  |
| `ssec:19.4.4` | Milestones, start dates and long-stops |  |
| `ssec:19.4.5` | Change in law inside a CfD |  |
| `ssec:19.4.6` | Financing a CfD project |  |
| `ssec:19.4.7` | Allocation rounds, budgets and administrative strike prices |  |
| `sec:19.5` | Hinkley Point C and construction risk under a CfD |  |
| `sec:19.6` | Cap-and-floor regimes |  |
| `ssec:19.6.1` | How cap-and-floor works |  |
| `ssec:19.6.2` | What lenders lend against |  |
| `sec:19.7` | The regulated asset base model |  |
| `ssec:19.7.1` | How a RAB pays |  |
| `ssec:19.7.2` | Paying during construction and sharing overruns |  |
| `ssec:19.7.3` | Government support for tail risks |  |
| `ssec:19.7.4` | What the RAB leaves with investors and consumers |  |
| `sec:19.8` | Thames Tideway and Sizewell C: paid from the first day of construction |  |
| `sec:19.9` | Walkthrough: comparing four support offers for one project |  |
| `sec:19.10` | Case P: a capacity tariff and a contract for difference |  |
| `sec:19.11` | Practitioner's notebook |  |
| `sec:19.12` | Judgment drill |  |
| `sec:19.13` | A support scheme fixes the price; the market still sets the shape |  |
| `sec:19.14` | Exercises |  |
| `sec:19.15` | Solutions to exercises |  |
| `ex:19.1` | Spain's plant-life reasonable return applied to an older plant |  |
| `ex:19.2` | Settling a two-sided CfD over six hours |  |
| `ex:19.3` | One plant, three revenue regimes, three price paths |  |
| `ex:19.4` | How much debt a CfD supports compared with merchant revenue |  |
| `ex:19.5` | A cap-and-floor regime over five years |  |
| `ex:19.6` | Allowed revenue under a RAB during construction |  |
| `ex:19.7` | Sharing an overrun between two thresholds |  |
| `exh:19.1` | Support scheme risk map |  |
| `exh:19.2` | CfD settlement over six hours |  |
| `exh:19.3` | Revenue under three regimes and three price paths (EUR m) |  |
| `exh:19.4` | Tail-risk support instruments and the risks they remove (Tideway and Sizewell C) |  |
| `exh:19.5` | Four support offers compared |  |
| `cl:19.1` | Difference amount, contract for difference |  |
| `cl:19.2` | Negative pricing, contract for difference |  |
| `cl:19.3` | Milestone requirement and long-stop date, contract for difference |  |
| `cl:19.4` | Qualifying change in law, contract for difference |  |
| `cl:19.5` | Cap and floor adjustment, interconnector licence |  |
| `cl:19.6` | Cost sharing above the baseline, RAB licence |  |
| `eq:19.1` | CfD difference amount: $DA}_t = (K - P^{ref}}_t) E^{del}}_t$ |  |
| `eq:19.2` | RAB allowed revenue: $AR}_t = RAB}_{t-1} WACC} + Dep}_t + Opex}^{allow}}_t$, indexed |  |
| `fw:support-scheme-risk-map` | Framework 19.1 Support scheme risk map | home ssec:19.1.2 |
| `fw:support-durability-test` | Framework 19.2 Statute-or-contract durability test | home sec:19.3 |

### Chapter 20: Merchant revenue, corporate PPAs and hedges

Source brief: `briefs/u05.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:20` | Merchant revenue, corporate PPAs and hedges |  |
| `sec:20.1` | Selling into a market without a buyer |  |
| `ssec:20.1.1` | Four risks in one revenue line |  |
| `ssec:20.1.2` | Who buys long-term power |  |
| `sec:20.2` | Corporate power purchase agreements |  |
| `ssec:20.2.1` | Physical corporate PPAs |  |
| `ssec:20.2.2` | Virtual PPAs |  |
| `ssec:20.2.3` | Term, termination and the buyer's credit |  |
| `sec:20.3` | Hedges with fixed volumes and fixed shapes |  |
| `ssec:20.3.1` | Fixed-volume swaps |  |
| `ssec:20.3.2` | Fixed-shape hedges |  |
| `ssec:20.3.3` | Drafting the volume obligation |  |
| `sec:20.4` | Hedges that move volume risk |  |
| `ssec:20.4.1` | As-produced hedges |  |
| `ssec:20.4.2` | Proxy revenue swaps |  |
| `sec:20.5` | Floors, puts and collars |  |
| `ssec:20.5.1` | Revenue floors and puts |  |
| `ssec:20.5.2` | Collars |  |
| `sec:20.6` | Storage revenue: tolls, capacity and ancillary services |  |
| `ssec:20.6.1` | Battery tolls |  |
| `ssec:20.6.2` | Capacity revenues |  |
| `ssec:20.6.3` | Ancillary-service revenues and stacking |  |
| `sec:20.7` | Collateral and the hedge provider in the capital structure |  |
| `ssec:20.7.1` | Credit support |  |
| `ssec:20.7.2` | Termination and close-out |  |
| `sec:20.8` | Winter Storm Uri and the volume you cannot guarantee |  |
| `sec:20.9` | Chile's solar contracts and the node they settled at |  |
| `sec:20.10` | Walkthrough: settling a month of a hedge book |  |
| `sec:20.11` | Case R: building the Mesa Corta hedge book |  |
| `sec:20.12` | Practitioner's notebook |  |
| `sec:20.13` | Judgment drill |  |
| `sec:20.14` | A hedge fixes a price for a quantity; a capacity contract fixes a fee |  |
| `sec:20.15` | Exercises |  |
| `sec:20.16` | Solutions to exercises |  |
| `ex:20.1` | Settling a virtual PPA over six hours, with basis |  |
| `ex:20.2` | A fixed-volume swap in a scarcity event |  |
| `ex:20.3` | Fixed shape against actual shape on two days |  |
| `ex:20.4` | A year under a proxy revenue swap |  |
| `ex:20.5` | A battery revenue floor with upside sharing |  |
| `ex:20.6` | A battery toll with an availability shortfall |  |
| `ex:20.7` | Stacking capacity, ancillary and arbitrage revenue |  |
| `exh:20.1` | Which instrument fixes which risk |  |
| `exh:20.2` | vPPA settlement over six hours (USD) |  |
| `exh:20.3` | Fixed-shape hedge on a mild day and a scarcity day (USD) |  |
| `exh:20.4` | Illustrative monthly hedge book settlement |  |
| `exh:20.5` | Case R hedge book by year (Case R) |  |
| `exh:20.6` | Uri-type stress on R1's fixed-volume swap (Case R) |  |
| `cl:20.1` | Settlement amount, virtual PPA |  |
| `cl:20.2` | Contract quantity and force majeure, fixed-volume hedge |  |
| `cl:20.3` | Proxy generation, proxy revenue swap |  |
| `cl:20.4` | Availability and capacity maintenance, battery toll |  |
| `cl:20.5` | Credit support, power hedge |  |
| `eq:20.1` | vPPA settlement: $S_t = (K - P^{hub}}_t) E^{del}}_t$ |  |
| `eq:20.2` | Fixed-volume swap settlement: $S_t = (K - P^{hub}}_t) Q_t$ |  |
| `eq:20.3` | Realized price decomposition: $p^{real}} = K - _t (P^{hub}}_t - P^{node}}_t)E_t / _t E_t$ (vPPA case) |  |
| `fw:four-risk-decomposition` | Framework 20.1 Four-risk decomposition of merchant revenue | home ssec:20.1.1 |
| `fw:scarcity-stress` | Framework 20.2 Scarcity stress for a hedge book | home sec:20.8 |

### Chapter 21: Revenue contracts beyond power

Source brief: `briefs/u05.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:21` | Revenue contracts beyond power |  |
| `sec:21.1` | Paying for capacity instead of product |  |
| `ssec:21.1.1` | The fixed-fee test |  |
| `ssec:21.1.2` | A grid for any revenue contract |  |
| `sec:21.2` | LNG sale and purchase agreements and tolling |  |
| `ssec:21.2.1` | Two LNG pricing families |  |
| `ssec:21.2.2` | The fixed fee and the cancellation right |  |
| `ssec:21.2.3` | Liquefaction tolling |  |
| `ssec:21.2.4` | What lenders need from an LNG offtake book |  |
| `sec:21.3` | Pipeline transportation and ship-or-pay |  |
| `ssec:21.3.1` | Reserved capacity and ship-or-pay |  |
| `ssec:21.3.2` | Shippers, credit and regulation |  |
| `sec:21.4` | Mining offtake |  |
| `ssec:21.4.1` | How a concentrate is paid for |  |
| `ssec:21.4.2` | Offtake as a financing tool |  |
| `sec:21.5` | Royalties and streams |  |
| `ssec:21.5.1` | Royalties |  |
| `ssec:21.5.2` | Streams |  |
| `sec:21.6` | Availability payments |  |
| `ssec:21.6.1` | The contract form |  |
| `sec:21.7` | User tolls and tariffs |  |
| `ssec:21.7.1` | Maximum tolls and escalation |  |
| `ssec:21.7.2` | Regulated tolls and upfront fees |  |
| `sec:21.8` | Airports and ports |  |
| `ssec:21.8.1` | Airport charges |  |
| `ssec:21.8.2` | Port concessions |  |
| `sec:21.9` | Data-center leases |  |
| `ssec:21.9.1` | The lease |  |
| `ssec:21.9.2` | Short leases and residual value guarantees |  |
| `sec:21.10` | Sabine Pass and the fee that survived a cargo glut |  |
| `sec:21.11` | Walkthrough: applying the fixed-fee test to a port terminal term sheet |  |
| `sec:21.12` | Case T: setting the Merrick Link toll regime |  |
| `sec:21.13` | Case P: ship-or-pay on the coastal pipeline |  |
| `sec:21.14` | Practitioner's notebook |  |
| `sec:21.15` | Judgment drill |  |
| `sec:21.16` | A fixed fee is only as good as the capacity it pays for |  |
| `sec:21.17` | Exercises |  |
| `sec:21.18` | Solutions to exercises |  |
| `ex:21.1` | Sabine Pass's fixed fee and a buyer's cargo decision |  |
| `ex:21.2` | A ship-or-pay transportation agreement in a low-flow year |  |
| `ex:21.3` | Net smelter return on a tonne of copper concentrate |  |
| `ex:21.4` | A net smelter return royalty |  |
| `ex:21.5` | A gold stream's economics for the streamer |  |
| `ex:21.6` | An availability payment with deductions |  |
| `ex:21.7` | Toll escalation with a floor |  |
| `ex:21.8` | Single till against dual till |  |
| `ex:21.9` | A data-center lease and a residual value guarantee |  |
| `exh:21.1` | Revenue contract classification grid |  |
| `exh:21.2` | Sabine Pass fixed fees by buyer (Real case) |  |
| `exh:21.3` | Concentrate invoice build per dry metric tonne |  |
| `exh:21.4` | Illustrative container terminal concession term sheet |  |
| `exh:21.5` | Merrick Link maximum tolls by class (Case T) |  |
| `exh:21.6` | Bélanou gas transportation charges (Case P) |  |
| `cl:21.1` | Fixed fee and cargo cancellation, LNG SPA |  |
| `cl:21.2` | Reservation charge and ship-or-pay, gas transportation agreement |  |
| `cl:21.3` | Payable metals and deductions, concentrate offtake agreement |  |
| `cl:21.4` | Delivery obligation, precious metals stream agreement |  |
| `cl:21.5` | Availability deductions, availability-based PPP agreement |  |
| `cl:21.6` | Toll setting and escalation, concession agreement |  |
| `cl:21.7` | Rent commencement and power delivery, data-center lease |  |
| `eq:21.1` | LNG SPA price: $p^{LNG}}_t = 1.15 HH}_t + F$ (Sabine-type) |  |
| `eq:21.2` | Net smelter return per dmt: payable value of each metal less TC, RCs and penalties |  |
| `eq:21.3` | Availability payment: $AP}_t = AP}^{}_t - AD}_t - PD}_t$ |  |
| `fw:fixed-fee-test` | Framework 21.1 Fixed-fee test | home ssec:21.1.1 |
| `fw:revenue-contract-grid` | Framework 21.2 Revenue contract classification grid | home ssec:21.1.2 |

### Chapter 22: The EPC contract

Source brief: `briefs/u05.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:22` | The EPC contract |  |
| `sec:22.1` | What an EPC contract promises |  |
| `ssec:22.1.1` | Four promises in one contract |  |
| `ssec:22.1.2` | Scope and fitness for purpose |  |
| `ssec:22.1.3` | What stays with the owner |  |
| `sec:22.2` | Price and payment |  |
| `ssec:22.2.1` | Milestones, advance and currency |  |
| `sec:22.3` | Delay liquidated damages |  |
| `ssec:22.3.1` | What delay LDs must pay for |  |
| `ssec:22.3.2` | The cap and its adequacy |  |
| `ssec:22.3.3` | Drafting delay LDs |  |
| `sec:22.4` | Performance guarantees and testing |  |
| `ssec:22.4.1` | Guarantees, minimum levels and buy-down LDs |  |
| `ssec:22.4.2` | Tests, taking-over and acceptance |  |
| `sec:22.5` | Changes, time and claims |  |
| `ssec:22.5.1` | Variations |  |
| `ssec:22.5.2` | Extension of time and concurrent delay |  |
| `ssec:22.5.3` | Notices, time bars and claims |  |
| `sec:22.6` | Liability, security and the contractor's credit |  |
| `ssec:22.6.1` | Caps, sub-caps and carve-outs |  |
| `ssec:22.6.2` | The security package |  |
| `ssec:22.6.3` | When the contractor fails |  |
| `sec:22.7` | Defects liability and warranties |  |
| `ssec:22.7.1` | Defects, latent defects and serial defects |  |
| `sec:22.8` | How the EPC contract fits the rest of the web |  |
| `ssec:22.8.1` | Back to back with the PPA |  |
| `ssec:22.8.2` | Insurance and the EPC |  |
| `ssec:22.8.3` | Beyond the single EPC contract |  |
| `sec:22.9` | Sabine Pass, Vogtle and Carillion: three fixed prices, three outcomes |  |
| `sec:22.10` | Triple Point and liquidated damages after termination |  |
| `sec:22.11` | Walkthrough: calibrating and marking up an EPC liability package |  |
| `sec:22.12` | Case P: negotiating the Bélanou EPC contract |  |
| `sec:22.13` | Practitioner's notebook |  |
| `sec:22.14` | Judgment drill |  |
| `sec:22.15` | Single point responsibility ends where the interfaces begin |  |
| `sec:22.16` | Exercises |  |
| `sec:22.17` | Solutions to exercises |  |
| `ex:22.1` | Calibrating the delay LD rate |  |
| `ex:22.2` | How many days does the cap cover? |  |
| `ex:22.3` | Pricing performance LDs as the NPV of lost margin |  |
| `ex:22.4` | Extension of time under three concurrency rules |  |
| `ex:22.5` | What the security package covers when the contractor fails |  |
| `exh:22.1` | The four EPC promises and the remedy behind each |  |
| `exh:22.2` | Delay LD calibration stack for a 342 MW CCGT (USD per day) |  |
| `exh:22.3` | EPC security stack at contractor failure (USD m) |  |
| `exh:22.4` | Illustrative EPC term sheet extract |  |
| `exh:22.5` | Case P delay LD calibration (Case P) |  |
| `exh:22.6` | Case P EPC risk package (Case P) |  |
| `cl:22.1` | Scope and fitness for purpose, EPC contract |  |
| `cl:22.2` | Delay liquidated damages, EPC contract |  |
| `cl:22.3` | Performance liquidated damages, EPC contract |  |
| `cl:22.4` | Taking-over and completion tests, EPC contract |  |
| `cl:22.5` | Extension of time and concurrent delay, EPC contract |  |
| `cl:22.6` | Limitation of liability, EPC contract |  |
| `cl:22.7` | Call on the performance bond, EPC contract |  |
| `cl:22.8` | Defects liability, EPC contract |  |
| `eq:22.1` | Daily delay cost: $c^{delay}} = D i/365 + c^{fix}} + LD}^{PPA}} (+ P/days} + E^{dist}}/365)$ |  |
| `eq:22.2` | Performance LD rate per kW: $LD}^{kW}} = 12 cpr} [1-(1+r)^{-n}]/r$ |  |
| `eq:22.3` | Heat-rate LD rate per kJ/kWh: annual extra fuel cost per kJ/kWh times the annuity factor |  |
| `fw:delay-ld-calibration` | Framework 22.1 Delay LD calibration stack | home ssec:22.3.1 |
| `fw:epc-security-stack` | Framework 22.2 EPC security stack | home ssec:22.6.2 |

### Chapter 23: Construction structures beyond the single EPC

Source brief: `briefs/u06.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:23` | Construction structures beyond the single EPC |  |
| `sec:23.1` | What a single EPC contract buys |  |
| `ssec:23.1.1` | One point of responsibility and its price |  |
| `ssec:23.1.2` | Why sponsors break the wrap |  |
| `ssec:23.1.3` | What lenders ask for in exchange |  |
| `sec:23.2` | Split and multi-contract structures |  |
| `ssec:23.2.1` | The onshore and offshore split |  |
| `ssec:23.2.2` | Multi-contracting in offshore wind |  |
| `ssec:23.2.3` | Supply-only, supply-and-install, and free-issue equipment |  |
| `sec:23.3` | Interfaces and the interface agreement |  |
| `ssec:23.3.1` | Mapping interfaces |  |
| `ssec:23.3.2` | How one late handover cascades |  |
| `ssec:23.3.3` | Drafting the interface agreement |  |
| `sec:23.4` | Wraps |  |
| `ssec:23.4.1` | Full, partial and performance wraps |  |
| `ssec:23.4.2` | Wrap caps and the sum-of-caps problem |  |
| `ssec:23.4.3` | Who can give a wrap |  |
| `sec:23.5` | EPCM and owner-managed delivery |  |
| `ssec:23.5.1` | How EPCM works |  |
| `ssec:23.5.2` | Pricing the risk the owner keeps |  |
| `ssec:23.5.3` | Cost-reimbursable, target-cost and alliance contracts |  |
| `sec:23.6` | Design and construction contracts in PPPs and the joint-venture contractor |  |
| `ssec:23.6.1` | Back-to-back D&C contracts under a concession |  |
| `ssec:23.6.2` | Joint and several liability and the JV agreement |  |
| `sec:23.7` | FIDIC, NEC and other standard forms |  |
| `ssec:23.7.1` | The FIDIC family and how each book allocates risk |  |
| `ssec:23.7.2` | NEC4 and the process-driven contract |  |
| `ssec:23.7.3` | Why lenders amend standard forms |  |
| `sec:23.8` | Walkthrough: marking up a standard-form contract for a project financing |  |
| `sec:23.9` | Supply-chain risk |  |
| `ssec:23.9.1` | Concentration, lead times and logistics |  |
| `ssec:23.9.2` | Price adjustment clauses |  |
| `ssec:23.9.3` | Origin, trade and sanctions constraints |  |
| `sec:23.10` | Equipment-supplier credit |  |
| `ssec:23.10.1` | What the owner relies on after delivery |  |
| `ssec:23.10.2` | Measuring supplier credit exposure |  |
| `ssec:23.10.3` | Security packages for suppliers |  |
| `ssec:23.10.4` | Vogtle and a fixed price from a contractor that failed |  |
| `sec:23.11` | Carillion and the difference a joint venture makes |  |
| `sec:23.12` | Case T: the Holbrook-Daneshill design and construction joint venture |  |
| `sec:23.13` | Practitioner's notebook |  |
| `sec:23.14` | Judgment drill |  |
| `sec:23.15` | The plant is built; who carries its performance for the next 25 years |  |
| `sec:23.16` | Exercises |  |
| `sec:23.17` | Solutions to exercises |  |
| `ex:23.1` | Wrapped or multi-contract offshore wind |  |
| `ex:23.2` | One late handover in a split hydro contract |  |
| `ex:23.3` | EPCM against lump-sum turnkey for a copper concentrator |  |
| `ex:23.4` | A steel price adjustment with a band and sharing |  |
| `ex:23.5` | A battery supplier's credit exposure over ten years |  |
| `exh:23.1` | Delivery structures compared: single EPC, split, multi-contract, EPCM (who carries interface, price and schedule risk) (Illustrative) |  |
| `exh:23.2` | Interface matrix for a split hydro contract (Illustrative) |  |
| `exh:23.3` | FIDIC books and their risk allocation (source) |  |
| `exh:23.4` | Offshore wind package map (TikZ diagram, Illustrative) |  |
| `exh:23.5` | Supplier exposure against security by year (Illustrative) |  |
| `exh:23.6` | Case T D&C and tolling interface map (Case T) |  |
| `cl:23.1` | Interface agreement, core obligations |  |
| `cl:23.2` | Wrap guarantee liability cap |  |
| `eq:23.1` | Price adjustment formula |  |
| `fw:construction-structure-selector` | Framework 23.1 Construction structure selector | home ssec:23.1.3 |

### Chapter 24: Operations and maintenance contracts

Source brief: `briefs/u06.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:24` | Operations and maintenance contracts |  |
| `sec:24.1` | What operating contracts must deliver |  |
| `ssec:24.1.1` | The operating cost line and the revenue at risk |  |
| `ssec:24.1.2` | Who does what after COD |  |
| `sec:24.2` | The O&M agreement |  |
| `ssec:24.2.1` | Scope, standards and the operating budget |  |
| `ssec:24.2.2` | Fixed fee, cost-plus and hybrids |  |
| `ssec:24.2.3` | Performance regimes and liability caps |  |
| `ssec:24.2.4` | Mobilization, term, termination and replacement |  |
| `ssec:24.2.5` | Affiliated operators and conflicts |  |
| `sec:24.3` | Long-term service agreements |  |
| `ssec:24.3.1` | What the OEM sells and why |  |
| `ssec:24.3.2` | Equivalent operating hours, starts and fees |  |
| `ssec:24.3.3` | OEM availability, performance and parts guarantees |  |
| `ssec:24.3.4` | Term, the end-of-agreement cliff, and termination |  |
| `sec:24.4` | Asset management agreements |  |
| `sec:24.5` | Planning and paying for major maintenance |  |
| `ssec:24.5.1` | Cycles by technology |  |
| `ssec:24.5.2` | Smoothing a lumpy cost |  |
| `ssec:24.5.3` | Lifecycle risk in PPPs |  |
| `sec:24.6` | Designing incentives that work |  |
| `sec:24.7` | Walkthrough: reading an LTSA fee schedule against a dispatch forecast |  |
| `sec:24.8` | Metronet and the tied supply chain |  |
| `sec:24.9` | Case P: the Bergmark LTSA and the Kilnworth O&M agreement |  |
| `sec:24.10` | Practitioner's notebook |  |
| `sec:24.11` | Judgment drill |  |
| `sec:24.12` | A plant that runs needs fuel, water, a grid and land it can keep |  |
| `sec:24.13` | Exercises |  |
| `sec:24.14` | Solutions to exercises |  |
| `ex:24.1` | Fixed fee or cost-plus for a geothermal plant |  |
| `ex:24.2` | How much of an availability shortfall the operator bears |  |
| `ex:24.3` | LTSA cost per MWh for a peaker and a baseload unit |  |
| `ex:24.4` | Smoothing an inverter replacement |  |
| `exh:24.1` | Who does what after COD (diagram, Illustrative) |  |
| `exh:24.2` | Fee structures compared (Illustrative) |  |
| `exh:24.3` | Major maintenance cycles by technology (Illustrative, with Case P and Case T inputs flagged) |  |
| `exh:24.4` | LTSA fees under peaking and baseload duty (Illustrative) |  |
| `exh:24.5` | Case P operating cost build OY1 to OY10 (Case P, P-F34) |  |
| `cl:24.1` | O&M availability guarantee and cap |  |
| `eq:24.1` | Equivalent operating hours |  |
| `fw:operating-incentive-alignment` | Framework 24.1 Operating incentive alignment test | home sec:24.6 |

### Chapter 25: Inputs and access: fuel, water, grid, land and permits

Source brief: `briefs/u06.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:25` | Inputs and access: fuel, water, grid, land and permits |  |
| `sec:25.1` | Inputs the project company cannot control |  |
| `sec:25.2` | Fuel and feedstock supply agreements |  |
| `ssec:25.2.1` | Matching the fuel contract to the offtake contract |  |
| `ssec:25.2.2` | Contract quantities and nominations |  |
| `ssec:25.2.3` | Take-or-pay, make-up and carry-forward |  |
| `ssec:25.2.4` | Deliver-or-pay and supply shortfalls |  |
| `ssec:25.2.5` | Price, indexation and pass-through |  |
| `ssec:25.2.6` | Quality, measurement and the delivery point |  |
| `ssec:25.2.7` | Supplier credit and reserves |  |
| `ssec:25.2.8` | Coal, LNG, biomass and other feedstocks |  |
| `sec:25.3` | Transportation from the shipper's side |  |
| `ssec:25.3.1` | Reserving capacity |  |
| `ssec:25.3.2` | Lining up the gas chain end to end |  |
| `sec:25.4` | Water |  |
| `ssec:25.4.1` | Cooling and process water |  |
| `ssec:25.4.2` | Water rights, permits and drought |  |
| `sec:25.5` | Grid connection and interconnection |  |
| `ssec:25.5.1` | Connection agreements, use-of-system and who builds what |  |
| `ssec:25.5.2` | Late connection and deemed energy |  |
| `ssec:25.5.3` | Firm and non-firm access and curtailment |  |
| `sec:25.6` | Lake Turkana and the line that came late |  |
| `sec:25.7` | Land rights |  |
| `ssec:25.7.1` | Forms of land right |  |
| `ssec:25.7.2` | What lenders need from a land right |  |
| `ssec:25.7.3` | Linear rights for pipelines, lines and roads |  |
| `sec:25.8` | Permits and their transferability |  |
| `ssec:25.8.1` | The permit register |  |
| `ssec:25.8.2` | Transferability, change of control and enforcement |  |
| `sec:25.9` | Testing the input chain |  |
| `sec:25.10` | Mundra and the limits of a fuel contract |  |
| `sec:25.11` | Walkthrough: building a permits and inputs register for a lender |  |
| `sec:25.12` | Case P: negotiating the gas sale agreement |  |
| `sec:25.13` | Practitioner's notebook |  |
| `sec:25.14` | Judgment drill |  |
| `sec:25.15` | The contracts are in place; who stands behind the project company |  |
| `sec:25.16` | Exercises |  |
| `sec:25.17` | Solutions to exercises |  |
| `ex:25.1` | Setting DCQ and MDQ for an open-cycle plant |  |
| `ex:25.2` | A take-or-pay and make-up account over four years |  |
| `ex:25.3` | When the PPA does not pass take-or-pay through |  |
| `ex:25.4` | Fourteen months waiting for the grid |  |
| `ex:25.5` | Does the land lease outlast the debt |  |
| `exh:25.1` | The input chain of a gas-fired IPP (diagram, Illustrative) |  |
| `exh:25.2` | Gas chain alignment by dimension (Illustrative, with Case P input column) |  |
| `exh:25.3` | Make-up account over four years (Illustrative) |  |
| `exh:25.4` | Permits and inputs register template (Illustrative) |  |
| `exh:25.5` | Input chain alignment grid applied to an OCGT (Illustrative) |  |
| `exh:25.6` | Case P gas volumes against DCQ and take-or-pay (Case P, P-F35) |  |
| `cl:25.1` | Take-or-pay and make-up, gas sale agreement |  |
| `cl:25.1a` | buyer-friendly |  |
| `cl:25.1b` | lender-friendly |  |
| `cl:25.1c` | seller-friendly) Take-or-pay and make-up, gas sale agreement |  |
| `eq:25.1` | Daily fuel requirement |  |
| `eq:25.2` | Deficiency payment |  |
| `fw:input-chain-alignment` | Framework 25.1 Input chain alignment grid | home sec:25.9 |

### Chapter 26: Sponsor and shareholder documents

Source brief: `briefs/u06.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:26` | Sponsor and shareholder documents |  |
| `sec:26.1` | The documents that bind the owners |  |
| `sec:26.2` | Development and co-development agreements |  |
| `ssec:26.2.1` | Exclusivity, cost sharing and decision-making |  |
| `ssec:26.2.2` | Funding defaults and dilution |  |
| `ssec:26.2.3` | Development fees and reimbursement at financial close |  |
| `ssec:26.2.4` | Withdrawal, deadlock and break-up |  |
| `sec:26.3` | The shareholders' agreement |  |
| `ssec:26.3.1` | Boards, quorum and reserved matters |  |
| `ssec:26.3.2` | Funding obligations and defaulting shareholders |  |
| `ssec:26.3.3` | Transfer restrictions and exit rights |  |
| `ssec:26.3.4` | Related-party contracts and conflicts |  |
| `ssec:26.3.5` | How the shareholders' agreement sits under the finance documents |  |
| `sec:26.4` | Equity contribution agreements |  |
| `ssec:26.4.1` | The commitment and its conditions |  |
| `ssec:26.4.2` | Acceleration, LC support and contingent equity |  |
| `sec:26.5` | Sponsor support and completion guarantees |  |
| `ssec:26.5.1` | The sponsor support spectrum |  |
| `ssec:26.5.2` | Financial completion |  |
| `ssec:26.5.3` | Capped, several and joint guarantees |  |
| `ssec:26.5.4` | Cost-overrun undertakings, keepwells and other support |  |
| `sec:26.6` | Completion guarantees in the LNG and petrochemical mega-projects |  |
| `sec:26.7` | Walkthrough: negotiating a reserved-matters schedule |  |
| `sec:26.8` | Case P: the shareholders' agreement among Kilnworth, Talmé and the ABDB fund |  |
| `sec:26.9` | Practitioner's notebook |  |
| `sec:26.10` | Judgment drill |  |
| `sec:26.11` | Sponsors stand behind the build; insurers stand behind the accidents |  |
| `sec:26.12` | Exercises |  |
| `sec:26.13` | Solutions to exercises |  |
| `ex:26.1` | Diluting a partner who stops paying |  |
| `ex:26.2` | Who can block a reserved matter |  |
| `ex:26.3` | An equity commitment backed by letters of credit |  |
| `ex:26.4` | A capped, several completion guarantee |  |
| `exh:26.1` | The sponsor documents from development to release (timeline, Illustrative) |  |
| `exh:26.2` | Transfer rights compared: lock-in, ROFR, ROFO, tag-along, drag-along (Illustrative) |  |
| `exh:26.3` | The sponsor support spectrum (diagram, Illustrative) |  |
| `exh:26.4` | Completion support in three mega-projects (Real case: Ichthys, PNG LNG, Sadara) |  |
| `exh:26.5` | Case P shareholdings before close, at close and the governance map (Case P, inputs) |  |
| `cl:26.1` | Right of first refusal, shareholders' agreement |  |
| `cl:26.1a` | majority-sponsor-friendly |  |
| `cl:26.1b` | lender-friendly |  |
| `cl:26.1c` | minority-friendly) Right of first refusal, shareholders' agreement |  |
| `cl:26.2` | Financial completion definition, common terms agreement or completion guarantee |  |
| `eq:26.1` | Dilution on a funding default |  |
| `fw:sponsor-support-spectrum` | Framework 26.1 Sponsor support spectrum | home ssec:26.5.1 |

### Chapter 27: Insurance

Source brief: `briefs/u06.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:27` | Insurance |  |
| `sec:27.1` | How project insurance works |  |
| `ssec:27.1.1` | Insurable and uninsurable risk |  |
| `ssec:27.1.2` | The vocabulary of a policy |  |
| `ssec:27.1.3` | Insurers, brokers, reinsurers and fronting |  |
| `sec:27.2` | Construction covers |  |
| `ssec:27.2.1` | Construction and erection all risks |  |
| `ssec:27.2.2` | Delay in start-up |  |
| `ssec:27.2.3` | Marine cargo and marine delay in start-up |  |
| `ssec:27.2.4` | Third-party liability and other construction covers |  |
| `sec:27.3` | Operational covers |  |
| `ssec:27.3.1` | Operational property damage and machinery breakdown |  |
| `ssec:27.3.2` | Business interruption |  |
| `ssec:27.3.3` | Limits and the maximum foreseeable loss |  |
| `ssec:27.3.4` | Cyber cover for operating assets (new, R-029) | new label |
| `sec:27.4` | Moss Landing and the gap between insured and economic loss |  |
| `sec:27.5` | Political risk and credit insurance |  |
| `sec:27.6` | What lenders require |  |
| `ssec:27.6.1` | Loss payee, non-vitiation and waiver of subrogation |  |
| `ssec:27.6.2` | Local fronting, cut-through and assignment of reinsurance |  |
| `ssec:27.6.3` | Insurer security, brokers' undertakings and cancellation |  |
| `ssec:27.6.4` | Applying insurance proceeds |  |
| `sec:27.7` | When cover is unavailable or unaffordable |  |
| `ssec:27.7.1` | The insurance market cycle |  |
| `ssec:27.7.2` | Unavailability clauses and who carries uninsurable risk |  |
| `sec:27.8` | The insurance program adequacy test |  |
| `sec:27.9` | Walkthrough: reading the lenders' insurance advisor's report |  |
| `sec:27.10` | Case P: designing the Bélanou insurance program |  |
| `sec:27.11` | Practitioner's notebook |  |
| `sec:27.12` | Judgment drill |  |
| `sec:27.13` | Each contract and policy works alone; the lenders need them to work together |  |
| `sec:27.14` | Exercises |  |
| `sec:27.15` | Solutions to exercises |  |
| `ex:27.1` | Sizing and claiming delay in start-up |  |
| `ex:27.2` | An operational transformer failure |  |
| `ex:27.3` | Limit adequacy at Moss Landing |  |
| `ex:27.4` | Reinstate or prepay |  |
| `ex:27.5` | A hard-market renewal |  |
| `exh:27.1` | Covers by project phase (Illustrative) |  |
| `exh:27.2` | DSU indemnity bases compared (Illustrative) |  |
| `exh:27.3` | Moss Landing disclosed losses against limits (Real case: Moss Landing, 2025--2026) |  |
| `exh:27.4` | Lenders' insurance requirements checklist (Illustrative) |  |
| `exh:27.5` | Case P insurance program (Case P, inputs) |  |
| `cl:27.1` | Application of insurance proceeds |  |
| `cl:27.2` | Loss payee and non-vitiation, lenders' insurance endorsement |  |
| `eq:27.1` | DSU daily indemnity (debt service plus fixed costs basis) |  |
| `eq:27.2` | DSU or BI claim with a time deductible |  |
| `fw:insurance-adequacy-test` | Framework 27.1 Insurance program adequacy test | home sec:27.8 |

### Chapter 28: Direct agreements and the contract map as a system

Source brief: `briefs/u06.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:28` | Direct agreements and the contract map as a system |  |
| `sec:28.1` | The contract map |  |
| `ssec:28.1.1` | Drawing the map |  |
| `ssec:28.1.2` | Reading the map as a system |  |
| `sec:28.2` | Direct agreements |  |
| `ssec:28.2.1` | Why lenders need their own contract with each counterparty |  |
| `ssec:28.2.2` | Parties, form and the consent to security |  |
| `ssec:28.2.3` | Notice and cure periods |  |
| `ssec:28.2.4` | Step-in and step-out |  |
| `ssec:28.2.5` | Novation and substitution |  |
| `ssec:28.2.6` | Direct agreements with governments |  |
| `ssec:28.2.7` | Consents beyond the direct agreements |  |
| `sec:28.3` | Walkthrough: reviewing a direct agreement line by line |  |
| `sec:28.4` | Sydney's tunnels and step-in in practice |  |
| `sec:28.5` | The contract gap scan |  |
| `ssec:28.5.1` | The dimensions to scan |  |
| `ssec:28.5.2` | Scoring and fixing gaps |  |
| `ssec:28.5.3` | A gap scan on a solar-plus-storage project |  |
| `sec:28.6` | Tracing who pays when something goes wrong |  |
| `ssec:28.6.1` | The steps |  |
| `ssec:28.6.2` | A trace in numbers |  |
| `ssec:28.6.3` | Lake Turkana traced to the taxpayer |  |
| `sec:28.7` | The Purple Line and back-to-back termination rights |  |
| `sec:28.8` | Case P: the contract map, the gap scan and a trace |  |
| `sec:28.9` | Practitioner's notebook |  |
| `sec:28.10` | Judgment drill |  |
| `sec:28.11` | The contracts allocate the risk; the lenders still have to decide whose money carries what is left |  |
| `sec:28.12` | Exercises |  |
| `sec:28.13` | Solutions to exercises |  |
| `ex:28.1` | How long a cure period must be |  |
| `ex:28.2` | A gap scan on a solar-plus-storage project |  |
| `ex:28.3` | Who pays when a wind farm's main transformer fails |  |
| `exh:28.1` | Case P contract map (Case P) |  |
| `exh:28.2` | Direct agreement structure (diagram, Illustrative) |  |
| `exh:28.3` | Contract gap scan grid (template, Illustrative) |  |
| `exh:28.4` | Term mismatches against debt and PPA (chart and table, Illustrative) |  |
| `exh:28.5` | Loss allocation in a transformer failure (Illustrative) |  |
| `exh:28.6` | Case P gap log, June 2018 (Case P, inputs) |  |
| `cl:28.1` | Step-in, direct agreement with a state-owned offtaker |  |
| `cl:28.2` | Cure period and standstill, direct agreement |  |
| `fw:contract-gap-scan` | Framework 28.1 Contract gap scan | home sec:28.2 |
| `fw:who-pays-if` | Framework 28.2 "Who pays if...?" trace | home ssec:28.6.1 |

### Chapter 29: The lenders

Source brief: `briefs/u07.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:29` | The lenders |  |
| `sec:29.1` | Six questions that separate one lender from another |  |
| `ssec:29.1.1` | What a lender is really selling |  |
| `ssec:29.1.2` | How the mix of lenders has moved since 2008 |  |
| `sec:29.2` | Commercial banks |  |
| `ssec:29.2.1` | How a bank earns its return on a project loan |  |
| `ssec:29.2.2` | Why banks lend short and floating |  |
| `ssec:29.2.3` | Appetite, limits, and the credit committee |  |
| `ssec:29.2.4` | The roles banks take in a deal |  |
| `ssec:29.2.5` | Local banks |  |
| `sec:29.3` | Export credit agencies |  |
| `ssec:29.3.1` | Why governments lend to buyers of their exports |  |
| `ssec:29.3.2` | The OECD Arrangement as the outer boundary |  |
| `ssec:29.3.3` | Pure cover, direct lending, and the percentage of cover |  |
| `ssec:29.3.4` | Content rules and why mega-projects use several ECAs |  |
| `ssec:29.3.5` | How the premium is set and paid |  |
| `ssec:29.3.6` | Repayment-profile limits and the average-life test |  |
| `ssec:29.3.7` | What an ECA checks before it commits |  |
| `sec:29.4` | Development finance institutions |  |
| `ssec:29.4.1` | Who the DFIs are |  |
| `ssec:29.4.2` | Mandate and additionality |  |
| `ssec:29.4.3` | Preferred creditor status |  |
| `ssec:29.4.4` | A/B loans and parallel loans |  |
| `ssec:29.4.5` | Guarantees, insurance, and equity from the same institutions |  |
| `ssec:29.4.6` | What DFIs require in return |  |
| `sec:29.5` | Public lenders at home |  |
| `sec:29.6` | Institutional investors |  |
| `ssec:29.6.1` | Insurers and pension funds as lenders |  |
| `ssec:29.6.2` | What an institution needs before it lends |  |
| `sec:29.7` | Infrastructure debt funds and private credit |  |
| `ssec:29.7.1` | How a debt fund is built and paid |  |
| `ssec:29.7.2` | Where private credit wins and what it costs |  |
| `sec:29.8` | Comparing lender offers |  |
| `sec:29.9` | PNG LNG and Ichthys as mega-financings built from ECA layers |  |
| `sec:29.10` | Walkthrough: reading an ECA cover term sheet |  |
| `sec:29.11` | Case P: forming the lender group |  |
| `sec:29.12` | Practitioner's notebook |  |
| `sec:29.13` | Judgment drill |  |
| `sec:29.14` | Lenders hold loans; investors buy bonds |  |
| `sec:29.15` | Exercises |  |
| `sec:29.16` | Solutions to exercises |  |
| `ex:29.1` | A bank's return on a project loan |  |
| `ex:29.2` | Building an ECA-covered tranche from an export contract |  |
| `ex:29.3` | Testing a sculpted repayment profile against Arrangement limits |  |
| `ex:29.4` | An A/B loan in a frontier-market power project |  |
| `ex:29.5` | Three lender offers for the same refinancing |  |
| `exh:29.1` | Lender types against the six questions |  |
| `exh:29.2` | Core terms of the OECD Arrangement, January 2026 text |  |
| `exh:29.3` | ECA cover types: who funds and who bears each risk |  |
| `exh:29.4` | B-loan participant voting thresholds |  |
| `exh:29.5` | A/B loan and parallel loan structures |  |
| `exh:29.6` | Three lender offers compared (USD m) |  |
| `exh:29.7` | PNG LNG sources of debt, December 2009 (USD bn) |  |
| `exh:29.8` | Ichthys LNG sources of debt, December 2012 (USD bn) |  |
| `exh:29.9` | Case P lender group at financial close, by tranche |  |
| `exh:29.10` | Case P lender structure |  |
| `cl:29.1` | Participation and lender of record, B-loan participation agreement |  |
| `eq:29.1` | Risk-adjusted return on allocated capital |  |
| `eq:29.2` | Covered loan with a financed premium |  |
| `eq:29.3` | Weighted average life of a repayment profile | ruling: ECA average-life test as a share of tenor, citing eq:6.2 (repurposed, R-005) |
| `fw:lender-fit-map` | Framework 29.1 Lender-fit map | home sec:29.8 |
| `fw:eca-cover-build` | Framework 29.2 ECA cover build | home ssec:29.3.7 |

### Chapter 30: Project bonds and ratings

Source brief: `briefs/u07.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:30` | Project bonds and ratings |  |
| `sec:30.1` | What a project bond is |  |
| `ssec:30.1.1` | The same debt, sold as a security |  |
| `ssec:30.1.2` | Who buys project bonds and why |  |
| `sec:30.2` | Where project bonds are sold |  |
| `ssec:30.2.1` | Rule 144A and Regulation S offerings |  |
| `ssec:30.2.2` | US private placements |  |
| `ssec:30.2.3` | Domestic, tax-exempt, and local-currency bonds |  |
| `ssec:30.2.4` | Green, social, and sustainability labels on project bonds |  |
| `ssec:30.2.5` | Sukuk in brief |  |
| `sec:30.3` | Bond arithmetic |  |
| `ssec:30.3.1` | Coupon, price, and yield | ruling: Bond market conventions: bond-equivalent yield, accrued interest and issue discount (retitled, R-004) |
| `ssec:30.3.2` | Amortization and average life | ruling: Amortizing bonds and sinking funds (retitled, R-005) |
| `ssec:30.3.3` | Negative carry |  |
| `ssec:30.3.4` | Call protection and the make-whole |  |
| `sec:30.4` | Choosing between bonds and loans |  |
| `ssec:30.4.1` | Construction risk and the bond investor |  |
| `ssec:30.4.2` | Living with bondholders after close |  |
| `ssec:30.4.3` | Bonds and loans in one structure |  |
| `ssec:30.4.4` | The bond-or-loan test |  |
| `sec:30.5` | How rating agencies analyze projects |  |
| `ssec:30.5.1` | What a rating measures |  |
| `ssec:30.5.2` | Rating a project in construction |  |
| `ssec:30.5.3` | Rating a project in operation |  |
| `ssec:30.5.4` | Sovereign ceiling, offtaker credit, and structures that pierce them |  |
| `ssec:30.5.5` | The rating-case stress ladder |  |
| `sec:30.6` | Colombia's 4G bonds and the guarantee that beat the sovereign rating |  |
| `sec:30.7` | Walkthrough: reading a project bond offering memorandum |  |
| `sec:30.8` | Case P: no bond in 2018, a rating view in 2024 |  |
| `sec:30.9` | Practitioner's notebook |  |
| `sec:30.10` | Judgment drill |  |
| `sec:30.11` | Debt that ranks second |  |
| `sec:30.12` | Exercises |  |
| `sec:30.13` | Solutions to exercises |  |
| `ex:30.1` | Pricing an amortizing project bond at issue |  |
| `ex:30.2` | The cost of negative carry on a pre-funded bond |  |
| `ex:30.3` | A make-whole on a private placement prepayment |  |
| `ex:30.4` | Breakeven availability in a rating case |  |
| `exh:30.1` | Project bond and project loan compared |  |
| `exh:30.2` | Escrow balance of a pre-funded bond during construction (USD m) |  |
| `exh:30.3` | Pacífico 3 and Puerta de Hierro bonds compared |  |
| `cl:30.1` | Make-whole redemption, indenture |  |
| `cl:30.2` | Permitted additional senior debt, indenture (variants 30.2a issuer-friendly, 30.2b bondholder-friendly) |  |
| `eq:30.1` | Price of a bond as the present value of its scheduled payments | ruling: Price of an amortizing bond on a semiannual bond-equivalent basis, citing eq:6.5 (repurposed, R-004) |
| `eq:30.2` | Make-whole amount |  |
| `fw:bond-or-loan-test` | Framework 30.1 Bond-or-loan test | home ssec:30.4.4 |
| `fw:rating-stress-ladder` | Framework 30.2 Rating-case stress ladder | home ssec:30.5.5 |

### Chapter 31: Mezzanine, holdco and ancillary facilities

Source brief: `briefs/u07.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:31` | Mezzanine, holdco and ancillary facilities |  |
| `sec:31.1` | The capital stack below and beside the senior debt |  |
| `sec:31.2` | Mezzanine debt |  |
| `ssec:31.2.1` | What mezzanine fills and who provides it |  |
| `ssec:31.2.2` | Contractual subordination |  |
| `ssec:31.2.3` | Pricing a mezzanine loan |  |
| `sec:31.3` | Holdco debt |  |
| `ssec:31.3.1` | Structural subordination |  |
| `ssec:31.3.2` | How holdco lenders protect themselves |  |
| `ssec:31.3.3` | Term loan B and the institutional loan market |  |
| `ssec:31.3.4` | Back-leverage under tax equity |  |
| `sec:31.4` | Equity bridge loans |  |
| `sec:31.5` | VAT and working-capital facilities |  |
| `ssec:31.5.1` | VAT facilities |  |
| `ssec:31.5.2` | Working-capital facilities |  |
| `sec:31.6` | Letter-of-credit facilities |  |
| `sec:31.7` | Standby and cost-overrun facilities |  |
| `sec:31.8` | Testing any junior or ancillary facility |  |
| `sec:31.9` | Azura-Edo's DFI mezzanine and a lender-provided gas LC |  |
| `sec:31.10` | Walkthrough: a holdco term sheet line by line |  |
| `sec:31.11` | Case R: the holdco loan behind A1, and Case P's standby and VAT facilities |  |
| `sec:31.12` | Practitioner's notebook |  |
| `sec:31.13` | Judgment drill |  |
| `sec:31.14` | What counts as equity |  |
| `sec:31.15` | Exercises |  |
| `sec:31.16` | Solutions to exercises |  |
| `ex:31.1` | A mezzanine lender's return |  |
| `ex:31.2` | Following one bad year through an opco and a holdco |  |
| `ex:31.3` | An equity bridge loan and the sponsors' IRR |  |
| `ex:31.4` | Sizing a VAT facility |  |
| `ex:31.5` | Letters of credit or cash |  |
| `ex:31.6` | Funding an overrun through the standby layers |  |
| `exh:31.1` | The capital stack below and beside the senior debt |  |
| `exh:31.2` | Opco and holdco cash in a base and a downside year (USD m) |  |
| `exh:31.3` | VAT facility balance by quarter (USD m) |  |
| `exh:31.4` | Azura-Edo financing layers and pricing |  |
| `exh:31.5` | Case R A1 sources and uses and holdco sizing (USD m) |  |
| `cl:31.1` | Payment blockage and standstill, subordination agreement (variants 31.1a sponsor-friendly, 31.1b senior-lender-friendly, 31.1c mezzanine-lender-friendly) |  |
| `eq:31.1` | Accretion of a PIK balance |  |
| `fw:subordination-stack` | Framework 31.1 Subordination stack test | home sec:31.8 |

### Chapter 32: Equity

Source brief: `briefs/u07.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:32` | Equity |  |
| `sec:32.1` | What equity does in a project financing |  |
| `sec:32.2` | The legal forms of equity |  |
| `ssec:32.2.1` | Share capital |  |
| `ssec:32.2.2` | Shareholder loans |  |
| `ssec:32.2.3` | Preference shares and other hybrids |  |
| `sec:32.3` | When the equity goes in |  |
| `ssec:32.3.1` | Upfront, pro rata, and back-ended equity |  |
| `ssec:32.3.2` | Making an equity commitment certain |  |
| `ssec:32.3.3` | Contingent equity |  |
| `sec:32.4` | Development equity and the development premium |  |
| `ssec:32.4.1` | What development capital buys |  |
| `ssec:32.4.2` | Pricing a development premium |  |
| `sec:32.5` | Farm-downs and partners |  |
| `ssec:32.5.1` | Selling down at financial close and after COD |  |
| `ssec:32.5.2` | What lenders require when equity changes hands |  |
| `sec:32.6` | Who provides project equity |  |
| `ssec:32.6.1` | Strategic sponsors, developers, and contractor-sponsors |  |
| `ssec:32.6.2` | Financial investors and infrastructure funds |  |
| `ssec:32.6.3` | DFIs and governments as shareholders |  |
| `sec:32.7` | Listed vehicles and yieldcos |  |
| `sec:32.8` | SunEdison and TerraForm Power |  |
| `sec:32.9` | US tax equity and the sale of tax credits |  |
| `ssec:32.9.1` | Why tax equity exists |  |
| `ssec:32.9.2` | The partnership flip |  |
| `ssec:32.9.3` | Transferability, hybrids, and direct sales |  |
| `ssec:32.9.4` | The 2025 law changes and what a lender must check |  |
| `sec:32.10` | Designing an equity plan |  |
| `sec:32.11` | Walkthrough: an equity plan schedule at financial close |  |
| `sec:32.12` | Case P: the equity plan |  |
| `sec:32.13` | Practitioner's notebook |  |
| `sec:32.14` | Judgment drill |  |
| `sec:32.15` | Capital that may not charge interest |  |
| `sec:32.16` | Exercises |  |
| `sec:32.17` | Solutions to exercises |  |
| `ex:32.1` | Share capital or shareholder loan |  |
| `ex:32.2` | When the equity goes in |  |
| `ex:32.3` | Pricing a development premium in a farm-down at financial close |  |
| `ex:32.4` | A yieldco's cost of equity and its incentive distribution rights |  |
| `ex:32.5` | Monetizing an investment tax credit by transfer |  |
| `exh:32.1` | What each party wants from the equity layer |  |
| `exh:32.2` | Equity IRR and lender exposure under three contribution timings |  |
| `exh:32.3` | TerraForm Power ownership and control, early 2016 |  |
| `exh:32.4` | Partnership flip allocations before and after the flip |  |
| `exh:32.5` | US federal credit dates for wind, solar and storage, as of October 3, 2026 |  |
| `exh:32.6` | Case P equity at financial close by sponsor and form (USD m) |  |
| `cl:32.1` | Equity letter of credit replacement, equity contribution agreement |  |
| `eq:32.1` | Development premium for a stake sold at financial close |  |
| `eq:32.2` | Cost of equity of a growing yieldco |  |
| `fw:equity-commitment-ladder` | Framework 32.1 Equity commitment ladder | home sec:32.10 |

### Chapter 33: Islamic project finance

Source brief: `briefs/u07.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:33` | Islamic project finance |  |
| `sec:33.1` | Why some capital will not take interest |  |
| `ssec:33.1.1` | Riba, gharar, and maysir |  |
| `ssec:33.1.2` | Sharia boards, fatwas, and standard-setters |  |
| `sec:33.2` | The contracts project finance uses |  |
| `ssec:33.2.1` | Istisna'a for construction |  |
| `ssec:33.2.2` | Ijara and forward ijara |  |
| `ssec:33.2.3` | Wakala |  |
| `ssec:33.2.4` | Murabaha and commodity murabaha |  |
| `ssec:33.2.5` | Musharaka and diminishing musharaka |  |
| `sec:33.3` | Building an Islamic tranche for a project |  |
| `ssec:33.3.1` | The istisna'a and ijara structure step by step |  |
| `ssec:33.3.2` | The owner's risks and how they are passed back |  |
| `ssec:33.3.3` | Pricing, late payment, and prepayment |  |
| `sec:33.4` | Sukuk in project finance |  |
| `sec:33.5` | Sitting beside conventional lenders |  |
| `ssec:33.5.1` | Matching economics and sharing losses |  |
| `ssec:33.5.2` | Where the structures diverge |  |
| `sec:33.6` | Choosing a structure |  |
| `sec:33.7` | Sadara's project sukuk beside ECA and bank debt |  |
| `sec:33.8` | Walkthrough: tracing one rental payment through an istisna'a and ijara tranche |  |
| `sec:33.9` | Case P: the ijara proposal that did not fit |  |
| `sec:33.10` | Practitioner's notebook |  |
| `sec:33.11` | Judgment drill |  |
| `sec:33.12` | When commercial money will not come at any price |  |
| `sec:33.13` | Exercises |  |
| `sec:33.14` | Solutions to exercises |  |
| `ex:33.1` | Rentals under an istisna'a and forward ijara |  |
| `ex:33.2` | A commodity murabaha working-capital line |  |
| `ex:33.3` | Periodic distributions on a project sukuk |  |
| `ex:33.4` | Sharing an enforcement loss between Islamic and conventional tranches |  |
| `exh:33.1` | The five contracts compared |  |
| `exh:33.2` | An istisna'a and ijara project structure |  |
| `exh:33.3` | Sadara senior debt at the 2013 closings |  |
| `cl:33.1` | Total loss and service agent's insurance obligation, forward lease |  |
| `eq:33.1` | Rental for a period under an ijara |  |
| `fw:sharia-structure-selector` | Framework 33.1 Sharia structure selector | home sec:33.6 |
| `fw:islamic-parity-check` | Framework 33.2 Islamic and conventional parity check | home ssec:33.5.2 |

### Chapter 34: Blended, concessional and local-currency finance

Source brief: `briefs/u07.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:34` | Blended, concessional and local-currency finance |  |
| `sec:34.1` | Why commercial money is sometimes not enough |  |
| `sec:34.2` | Concessional finance |  |
| `ssec:34.2.1` | What makes a loan concessional |  |
| `ssec:34.2.2` | Climate funds and concessional windows |  |
| `ssec:34.2.3` | How concessional terms reach the tariff |  |
| `ssec:34.2.4` | On-lending through a public entity |  |
| `sec:34.3` | First-loss capital and the limits of blending |  |
| `ssec:34.3.1` | First-loss capital |  |
| `ssec:34.3.2` | Minimum concessionality and crowding out |  |
| `sec:34.4` | Guarantees |  |
| `ssec:34.4.1` | Partial risk guarantees |  |
| `ssec:34.4.2` | Partial credit guarantees |  |
| `ssec:34.4.3` | The indemnity behind the guarantee |  |
| `ssec:34.4.4` | Guarantees and political risk insurance compared |  |
| `sec:34.5` | Viability-gap funding |  |
| `sec:34.6` | Local-currency solutions |  |
| `ssec:34.6.1` | Why dollar debt fails local-currency projects |  |
| `ssec:34.6.2` | Local banks, development banks, and debt funds |  |
| `ssec:34.6.3` | Local and inflation-linked bonds |  |
| `ssec:34.6.4` | Currency hedges from specialist funds |  |
| `ssec:34.6.5` | The local-currency route map |  |
| `sec:34.7` | Noor Ouarzazate I and concessional money on-lent by the state |  |
| `sec:34.8` | Colombia's 4G program and a local-currency market built around a pipeline |  |
| `sec:34.9` | Walkthrough: a partial risk guarantee term sheet and its indemnity |  |
| `sec:34.10` | Case P: the ABDB guarantee and the cauri loan nobody offered |  |
| `sec:34.11` | Practitioner's notebook |  |
| `sec:34.12` | Judgment drill |  |
| `sec:34.13` | How much debt the cash flow can carry |  |
| `sec:34.14` | Exercises |  |
| `sec:34.15` | Solutions to exercises |  |
| `ex:34.1` | How concessional debt lowers the tariff |  |
| `ex:34.2` | First-loss capital and the senior lender's expected loss |  |
| `ex:34.3` | A partial risk guarantee behind an offtaker's letter of credit |  |
| `ex:34.4` | A partial credit guarantee on a local-currency bond |  |
| `ex:34.5` | Sizing viability-gap funding |  |
| `ex:34.6` | Dollar debt against local revenue under devaluation |  |
| `exh:34.1` | Four financing gaps and the tools that address them |  |
| `exh:34.2` | Commercial and blended debt service by year (USD m) |  |
| `exh:34.3` | Noor Ouarzazate I financing and offtake structure |  |
| `exh:34.4` | Azura-Edo revenue security stack |  |
| `exh:34.5` | The indemnity chain behind a partial risk guarantee |  |
| `exh:34.6` | Guarantees and political risk insurance compared |  |
| `exh:34.7` | Noor Ouarzazate I appraisal financing plan (USD m) |  |
| `cl:34.1` | Demand under a liquidity guarantee, partial risk guarantee agreement |  |
| `eq:34.1` | Grant element of a loan |  |
| `fw:blending-decision-test` | Framework 34.1 Blending decision test | home ssec:34.3.2 |
| `fw:local-currency-route-map` | Framework 34.2 Local-currency route map | home ssec:34.6.5 |

### Chapter 35: Cash flow available for debt service and the cover ratios

Source brief: `briefs/u08.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:35` | Cash flow available for debt service and the cover ratios |  |
| `sec:35.1` | What lenders are paid from: cash flow available for debt service |  |
| `ssec:35.1.1` | Building CFADS from revenue down |  |
| `ssec:35.1.2` | Cash, not accruals |  |
| `ssec:35.1.3` | The items lenders and sponsors argue about |  |
| `ssec:35.1.4` | CFADS against EBITDA |  |
| `sec:35.2` | The debt service cover ratio |  |
| `ssec:35.2.1` | One period, one ratio |  |
| `ssec:35.2.2` | Minimum and average DSCR |  |
| `ssec:35.2.3` | Looking back and looking forward: historic and projected DSCR |  |
| `ssec:35.2.4` | Sizing ratios and covenant ratios |  |
| `sec:35.3` | The loan life cover ratio |  |
| `ssec:35.3.1` | Definition, discount rate, and the DSRA |  |
| `ssec:35.3.2` | LLCR as an average DSCR in present-value terms |  |
| `ssec:35.3.3` | What LLCR adds that DSCR cannot |  |
| `sec:35.4` | The project life cover ratio and the tail |  |
| `ssec:35.4.1` | Definition |  |
| `ssec:35.4.2` | Reading the gap between PLCR and LLCR |  |
| `sec:35.5` | Gearing |  |
| `ssec:35.5.1` | Gearing on the funding requirement |  |
| `ssec:35.5.2` | Why gearing still matters when DSCR sizes the debt |  |
| `sec:35.6` | Base, banking, downside, and break-even cases |  |
| `ssec:35.6.1` | Who owns which case |  |
| `ssec:35.6.2` | Downside cases |  |
| `ssec:35.6.3` | Break-even cases and headroom |  |
| `ssec:35.6.4` | Whose forecast: optimism in the base case |  |
| `sec:35.7` | Chile's northern solar defaults: when produced energy is not cash |  |
| `sec:35.8` | Walkthrough: reading the CFADS and ratio definitions in a common terms agreement |  |
| `sec:35.9` | Walkthrough: auditing a ratio summary table |  |
| `sec:35.10` | Case P: CFADS and the ratios at financial close |  |
| `sec:35.11` | Practitioner's notebook |  |
| `sec:35.12` | Judgment drill |  |
| `sec:35.13` | Ratios describe a debt; they do not yet size it |  |
| `sec:35.14` | Exercises |  |
| `sec:35.15` | Solutions to exercises |  |
| `ex:35.1` | Building CFADS for one operating year (Illustrative) |  |
| `ex:35.2` | The same year on accruals and on cash (Illustrative) |  |
| `ex:35.3` | Minimum and average DSCR on a 12-year loan (Illustrative) |  |
| `ex:35.4` | Seasonal cash flow and 12-month tests (Illustrative) |  |
| `ex:35.5` | The loan life cover ratio (Illustrative) |  |
| `ex:35.6` | The project life cover ratio and the tail (Illustrative) |  |
| `ex:35.7` | One deal, four gearing numbers (Illustrative) |  |
| `ex:35.8` | Base, banking, downside, and break-even cases (Illustrative) |  |
| `exh:35.1` | CFADS build for one operating year (USD m) (Illustrative) |  |
| `exh:35.2` | Disputed CFADS items and their usual treatment (Illustrative) |  |
| `exh:35.3` | DSCR sizing levels by technology and revenue type, US market, early 2024 to early 2026 (x) (Real case: NRF Cost of Capital outlooks, 2024--2026) |  |
| `exh:35.4` | DSCR, LLCR, and PLCR for a transmission concession (USD m) (Illustrative) |  |
| `exh:35.5` | Ratios on base, banking, downside, and break-even cases for a run-of-river hydro plant (Illustrative) |  |
| `exh:35.6` | A ratio summary with five errors (Illustrative) |  |
| `exh:35.7` | Case P CFADS for the first full operating year (USD m) (Case P) |  |
| `exh:35.8` | Case P ratios at financial close on base, banking, and downside (Case P) |  |
| `exh:35.9` | Case P CFADS and DSCR profile (chart) (Case P) |  |
| `cl:35.1` | Ratio definitions, common terms agreement (Illustrative) |  |
| `cl:35.2` | with |  |
| `cl:35.2c` | if required) CFADS definition variants |  |
| `eq:35.1` | DSCR |  |
| `eq:35.2` | CFADS |  |
| `eq:35.3` | LLCR |  |
| `eq:35.4` | LLCR as PV-weighted DSCR |  |
| `eq:35.5` | PLCR |  |
| `eq:35.6` | weighted average DSCR |  |
| `eq:35.7` | historic DSCR |  |
| `eq:35.8` | projected DSCR |  |
| `eq:35.9` | gearing |  |
| `fw:four-ratio-read` | Framework 35.1 Four-ratio read | home ssec:35.6.3 |

### Chapter 36: Sizing and sculpting debt

Source brief: `briefs/u08.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:36` | Sizing and sculpting debt |  |
| `sec:36.1` | From a ratio to a debt amount |  |
| `ssec:36.1.1` | Debt capacity of a flat cash flow |  |
| `ssec:36.1.2` | Why level repayment wastes capacity |  |
| `sec:36.2` | Sculpting |  |
| `ssec:36.2.1` | The two sculpting equations |  |
| `ssec:36.2.2` | Building the schedule period by period |  |
| `ssec:36.2.3` | What to sculpt on |  |
| `ssec:36.2.4` | Where sculpting goes wrong |  |
| `sec:36.3` | Sizing to several constraints at once |  |
| `ssec:36.3.1` | The lesser-of rule |  |
| `ssec:36.3.2` | Gearing caps and when they bind |  |
| `ssec:36.3.3` | How much debt a tenth of a turn costs |  |
| `sec:36.4` | Sizing on P90 and P99 |  |
| `ssec:36.4.1` | Why one P-value is not enough |  |
| `ssec:36.4.2` | Running four tests on one wind farm |  |
| `sec:36.5` | Tenor and tail |  |
| `ssec:36.5.1` | Tenor against contract and asset life |  |
| `ssec:36.5.2` | Why lenders want a tail and how long |  |
| `sec:36.6` | Grace periods, ramp-up, and the first repayment |  |
| `ssec:36.6.1` | Grace periods |  |
| `ssec:36.6.2` | Sizing through a ramp-up |  |
| `sec:36.7` | Balloons and mini-perms |  |
| `ssec:36.7.1` | Balloons and the refinancing test |  |
| `ssec:36.7.2` | Hard and soft mini-perms |  |
| `sec:36.8` | Merchant tails and sizing by revenue bucket |  |
| `ssec:36.8.1` | The bucket method |  |
| `ssec:36.8.2` | Merchant tails after the contract |  |
| `sec:36.9` | Repayment-profile rules: weighted average life and installment limits |  |
| `ssec:36.9.1` | Weighted average life | ruling: Average-life limits as a sizing constraint (retitled, R-005) |
| `ssec:36.9.2` | Testing and repairing a sculpted profile |  |
| `sec:36.10` | How sizing parameters vary by sector, contract, market, and cycle |  |
| `ssec:36.10.1` | The four drivers ranked |  |
| `ssec:36.10.2` | How the cycle moves terms |  |
| `sec:36.11` | Walkthrough: reading a lender's sizing printout |  |
| `sec:36.12` | Case P: the lenders size the debt |  |
| `sec:36.13` | Practitioner's notebook |  |
| `sec:36.14` | Judgment drill |  |
| `sec:36.15` | Sizing fixes the debt; the reserves decide whether it survives a bad year |  |
| `sec:36.16` | Exercises |  |
| `sec:36.17` | Solutions to exercises |  |
| `ex:36.1` | Debt capacity of a flat availability payment (Illustrative) |  |
| `ex:36.2` | Annuity against sculpted repayment on a declining cash flow (Illustrative) |  |
| `ex:36.3` | Sculpting a 10-year repayment schedule (Illustrative) |  |
| `ex:36.4` | Four constraints, one binding (Illustrative) |  |
| `ex:36.5` | Debt sensitivity to the target DSCR (Illustrative) |  |
| `ex:36.6` | P50, P90, and P99 tests on one wind farm (Illustrative) |  |
| `ex:36.7` | Tenor, tail, and debt capacity (Illustrative) |  |
| `ex:36.8` | Sizing through a traffic ramp-up (Illustrative) |  |
| `ex:36.9` | A balloon sized to its refinancing (Illustrative) |  |
| `ex:36.10` | Hard and soft mini-perms (Illustrative) |  |
| `ex:36.11` | Sizing by revenue bucket with a merchant tail (Illustrative) |  |
| `ex:36.12` | Testing a sculpted ECA tranche against profile rules (Illustrative) |  |
| `exh:36.1` | Annuity and sculpted debt service against CFADS (chart) (Illustrative) |  |
| `exh:36.2` | A sculpted 10-year repayment schedule (EUR m) (Illustrative) |  |
| `exh:36.3` | Debt by constraint for a Brazilian wind farm (BRL m) (Illustrative) |  |
| `exh:36.4` | Debt against target DSCR (EUR m) (Illustrative) |  |
| `exh:36.5` | Debt by P-value test (GBP m) (Illustrative) |  |
| `exh:36.6` | Debt, tail, and PLCR by tenor (USD m) (Illustrative) |  |
| `exh:36.7` | Ramp-up sizing options for a toll road (MXN m) (Illustrative) |  |
| `exh:36.8` | Soft mini-perm balance path (USD m) (Illustrative) |  |
| `exh:36.9` | Bucket against uniform sizing under merchant stress (EUR m) (Illustrative) |  |
| `exh:36.10` | Sizing parameters by sector and revenue type, with sources and periods (Real case: market surveys and filings, 2023--2026) |  |
| `exh:36.11` | A lender's sizing printout (Illustrative) |  |
| `exh:36.12` | Case P sizing constraints and binding constraint (Case P) |  |
| `exh:36.13` | Case P sculpted repayment profile and ECA tests (Case P) |  |
| `exh:36.14` | Case P debt at alternative DSCR targets and gearing caps (Case P, if P-F36 released) |  |
| `eq:36.1` | annuity sizing |  |
| `eq:36.2` | sculpted debt service |  |
| `eq:36.3` | debt as PV of sculpted debt service with cumulative discount factors |  |
| `eq:36.4` | lesser-of rule |  |
| `eq:36.5` | weighted average life | ruling: Average-life constraint on a sculpted profile, citing eq:6.2 (repurposed, R-005) |
| `eq:36.6` | bucket sculpting |  |
| `eq:36.7` | effective base-case target from a downside test |  |
| `fw:sizing-constraint-stack` | Framework 36.1 Sizing constraint stack | home ssec:36.3.2 |

### Chapter 37: Reserves, sweeps, covenants and hedging

Source brief: `briefs/u08.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:37` | Reserves, sweeps, covenants and hedging |  |
| `sec:37.1` | The debt service reserve account |  |
| `ssec:37.1.1` | What the DSRA buys |  |
| `ssec:37.1.2` | Sizing the DSRA |  |
| `ssec:37.1.3` | Funding the DSRA at COD and letters of credit |  |
| `ssec:37.1.4` | Drawing and refilling |  |
| `sec:37.2` | Maintenance and other reserves |  |
| `ssec:37.2.1` | The major maintenance reserve |  |
| `ssec:37.2.2` | Other reserves and when lenders ask for them |  |
| `sec:37.3` | Cash sweeps |  |
| `ssec:37.3.1` | Types of sweep |  |
| `ssec:37.3.2` | How a sweep changes the loan |  |
| `sec:37.4` | Distribution lock-ups and the distribution test |  |
| `ssec:37.4.1` | The distribution conditions |  |
| `ssec:37.4.2` | Setting the lock-up level with the sizing case |  |
| `ssec:37.4.3` | Trapped cash and its release |  |
| `sec:37.5` | Financial covenants |  |
| `ssec:37.5.1` | The trigger ladder |  |
| `ssec:37.5.2` | Setting the levels |  |
| `ssec:37.5.3` | Equity cures |  |
| `sec:37.6` | Non-financial covenants |  |
| `ssec:37.6.1` | What each covenant protects |  |
| `ssec:37.6.2` | Design choices and their costs |  |
| `sec:37.7` | Hedging requirements and hedge profiles |  |
| `ssec:37.7.1` | Why lenders require hedges |  |
| `ssec:37.7.2` | Matching the hedge to the debt profile |  |
| `ssec:37.7.3` | Currency and inflation hedging requirements |  |
| `ssec:37.7.4` | Hedge counterparties in the structure |  |
| `sec:37.8` | Indiana Toll Road and the swap that outgrew the road |  |
| `sec:37.9` | Walkthrough: the reserves, covenants, and hedging section of a term sheet |  |
| `sec:37.10` | Case P: reserves, triggers, and the 80% swap |  |
| `sec:37.11` | Practitioner's notebook |  |
| `sec:37.12` | Judgment drill |  |
| `sec:37.13` | Protection has a price, and someone has to pay it |  |
| `sec:37.14` | Exercises |  |
| `sec:37.15` | Solutions to exercises |  |
| `ex:37.1` | Sizing and funding a DSRA (Illustrative) |  |
| `ex:37.2` | A drought draws the DSRA (Illustrative) |  |
| `ex:37.3` | Smoothing an overhaul with an MMRA (Illustrative) |  |
| `ex:37.4` | A cash sweep on a copper mine (Illustrative) |  |
| `ex:37.5` | Setting the lock-up level against the sizing case (Illustrative) |  |
| `ex:37.6` | Trapping and releasing cash (Illustrative) |  |
| `ex:37.7` | Covenant headroom and the equity cure (Illustrative) |  |
| `ex:37.8` | Hedge ratio and a 200 basis point shock (Illustrative) |  |
| `ex:37.9` | Prepayment, over-hedging, and breakage (Illustrative) |  |
| `exh:37.1` | DSRA through a drought (USD m) (Illustrative) |  |
| `exh:37.2` | Reserve accounts: purpose, sizing, funding (Illustrative) |  |
| `exh:37.3` | Sweep scenarios on a copper loan (USD m) (Illustrative) |  |
| `exh:37.4` | Lock-up probabilities by sizing ratio (Illustrative) |  |
| `exh:37.5` | Trigger ladder for a project sized at 1.38x (Illustrative) |  |
| `exh:37.6` | Non-financial covenants and the risks they control (Illustrative) |  |
| `exh:37.7` | Minimum DSCR by hedge ratio after a rate shock (Illustrative) |  |
| `exh:37.8` | Hedge notional against debt after a prepayment (USD m) (Illustrative) |  |
| `exh:37.9` | Term sheet extract: reserves, covenants, hedging (Illustrative) |  |
| `exh:37.10` | Case P DSRA and MMRA (Case P) |  |
| `exh:37.11` | Case P trigger ladder (Case P) |  |
| `exh:37.12` | Case P swap notional and hedge ratio (Case P) |  |
| `cl:37.1` | DSRA letter of credit substitution (Illustrative) (used in the Exercise 37.11 solution) |  |
| `eq:37.1` | DSRA target |  |
| `eq:37.2` | MMRA accrual |  |
| `eq:37.3` | sweep amount |  |
| `eq:37.4` | equity cure amounts |  |
| `eq:37.5` | hedge ratio |  |
| `eq:37.6` | CFADS fall to a trigger |  |
| `fw:trigger-ladder` | Framework 37.1 Trigger ladder | home ssec:37.5.1 |
| `fw:hedge-fit-test` | Framework 37.2 Hedge fit test | home ssec:37.7.2 |

### Chapter 38: Pricing project debt

Source brief: `briefs/u08.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:38` | Pricing project debt |  |
| `sec:38.1` | What a lender has to earn |  |
| `ssec:38.1.1` | The four building blocks of a margin |  |
| `ssec:38.1.2` | Why the price is not the cost |  |
| `sec:38.2` | Margins and ratchets |  |
| `ssec:38.2.1` | Construction and operating margins |  |
| `ssec:38.2.2` | Step-ups over the tenor |  |
| `ssec:38.2.3` | Ratchets down |  |
| `sec:38.3` | Fees |  |
| `ssec:38.3.1` | Upfront fees and who earns them |  |
| `ssec:38.3.2` | Commitment fees |  |
| `ssec:38.3.3` | Agency, security agent, and account bank fees |  |
| `sec:38.4` | The cost of hedging |  |
| `ssec:38.4.1` | Credit and execution charges |  |
| `sec:38.5` | ECA premia, DFI pricing, insurance, and tax in the cost of debt |  |
| `ssec:38.5.1` | Folding an ECA premium into the all-in cost |  |
| `ssec:38.5.2` | DFI loans and A/B pricing |  |
| `ssec:38.5.3` | Political risk insurance and withholding tax gross-ups as costs of debt |  |
| `sec:38.6` | The all-in cost of debt |  |
| `ssec:38.6.1` | Defining all-in cost as an IRR |  |
| `ssec:38.6.2` | The quick approximation and where it fails |  |
| `sec:38.7` | Bonds against loans |  |
| `ssec:38.7.1` | Coupons, issue prices, and yield |  |
| `ssec:38.7.2` | Putting a bond and a loan on one basis |  |
| `sec:38.8` | Market flex |  |
| `ssec:38.8.1` | What flex is and why underwriters need it |  |
| `ssec:38.8.2` | Who pays under flex |  |
| `sec:38.9` | How pricing moves with risk and the cycle |  |
| `ssec:38.9.1` | Revenue quality, technology, and counterparty |  |
| `ssec:38.9.2` | Country, tenor, and the cycle |  |
| `sec:38.10` | Walkthrough: comparing financing offers on an all-in basis |  |
| `sec:38.11` | Case P: what the debt costs |  |
| `sec:38.12` | Practitioner's notebook |  |
| `sec:38.13` | Judgment drill |  |
| `sec:38.14` | From term sheet to model |  |
| `sec:38.15` | Exercises |  |
| `sec:38.16` | Solutions to exercises |  |
| `ex:38.1` | Building a minimum margin (Illustrative) |  |
| `ex:38.2` | The weighted average margin of a step-up schedule (Illustrative) |  |
| `ex:38.3` | Fee economics of a syndicate (Illustrative) |  |
| `ex:38.4` | Commitment fees on an S-curve (Illustrative) |  |
| `ex:38.5` | The cost of a swap execution charge (Illustrative) |  |
| `ex:38.6` | Covered against uncovered: the ECA premium in the all-in cost (Illustrative) |  |
| `ex:38.7` | Grossing up for withholding tax (Illustrative) |  |
| `ex:38.8` | All-in cost of a construction-plus-term loan (Illustrative) |  |
| `ex:38.9` | Yield on a bond issued below par (Real case: Applied Digital notes, 2025) |  |
| `ex:38.10` | Market flex: who pays (Illustrative) |  |
| `exh:38.1` | Minimum margin by risk weight (bps) (Illustrative) |  |
| `exh:38.2` | Step-up schedule and weighted margin (Illustrative) |  |
| `exh:38.3` | Syndicate fee flows (USD m) (Illustrative) |  |
| `exh:38.4` | Commitment fees on an S-curve (USD m) (Illustrative) |  |
| `exh:38.5` | Covered against uncovered tranche cash flows and all-in cost (USD m) (Illustrative) |  |
| `exh:38.6` | All-in cost build for a construction-plus-term loan (USD m) (Illustrative) |  |
| `exh:38.7` | Bond yield against coupon (Real case: Applied Digital notes, 2025) |  |
| `exh:38.8` | Flex economics (USD m) (Illustrative) |  |
| `exh:38.9` | Indicative pricing by revenue type and sector, US, 2024--2026 (Real case: NRF Cost of Capital outlooks and filings) |  |
| `exh:38.10` | Four financing offers on one basis (Illustrative) |  |
| `exh:38.11` | Case P pricing terms by tranche (Case P) |  |
| `exh:38.12` | Case P all-in cost by tranche (Case P) |  |
| `cl:38.1` | Margin step-up and ratchet (Illustrative), used in the Exercise 38.10 solution |  |
| `eq:38.1` | minimum margin |  |
| `eq:38.2` | all-in cost as IRR |  |
| `eq:38.3` | all-in approximation |  |
| `eq:38.4` | withholding gross-up |  |
| `eq:38.5` | financed premium principal |  |
| `eq:38.6` | yield to maturity | ruling: All-in cost of a bond from issue price, fees and coupons, citing eq:6.5 (repurposed, R-004) |
| `fw:all-in-cost-build` | Framework 38.1 All-in cost build | home sec:38.6 |

### Chapter 39: Model architecture, standards and timing

Source brief: `briefs/u09.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:39` | Model architecture, standards and timing |  |
| `sec:39.1` | What a project finance model is for |  |
| `ssec:39.1.1` | Decisions a model serves |  |
| `ssec:39.1.2` | Bid, financial-close and operating models |  |
| `ssec:39.1.3` | The model blueprint |  |
| `sec:39.2` | Standards for a model other people must trust |  |
| `ssec:39.2.1` | Why standards exist |  |
| `ssec:39.2.2` | The FAST standard |  |
| `ssec:39.2.3` | The house rules of this book's model |  |
| `ssec:39.2.4` | Where modelers disagree |  |
| `sec:39.3` | Sheet structure and the flow of a model |  |
| `ssec:39.3.1` | The fifteen sheets |  |
| `ssec:39.3.2` | The standard header and column layout |  |
| `ssec:39.3.3` | The corkscrew |  |
| `ssec:39.3.4` | One source for every number |  |
| `sec:39.4` | Building the timeline |  |
| `ssec:39.4.1` | Choosing periodicity and the number of timelines |  |
| `ssec:39.4.2` | Period start and end dates |  |
| `ssec:39.4.3` | Partial periods and day counts |  |
| `ssec:39.4.4` | Counters and bands |  |
| `sec:39.5` | Flags |  |
| `ssec:39.5.1` | Rules for flags |  |
| `ssec:39.5.2` | The core flags of a project model |  |
| `ssec:39.5.3` | Flag arithmetic and the off-by-one error |  |
| `ssec:39.5.4` | Bringing calendar inputs onto the model timeline |  |
| `sec:39.6` | Inputs and scenario control |  |
| `ssec:39.6.1` | Laying out the Inputs sheet |  |
| `ssec:39.6.2` | Scenario columns and the live column |  |
| `ssec:39.6.3` | Sensitivities are not scenarios |  |
| `ssec:39.6.4` | Time-series inputs |  |
| `ssec:39.6.5` | Version control and the change log |  |
| `sec:39.7` | Checks from the first row |  |
| `ssec:39.7.1` | Building a check |  |
| `ssec:39.7.2` | Timeline checks and the master check |  |
| `sec:39.8` | Walkthrough: critiquing a sponsor's model layout |  |
| `sec:39.9` | Case P: building the model skeleton |  |
| `sec:39.10` | Practitioner's notebook |  |
| `sec:39.11` | Judgment drill |  |
| `sec:39.12` | From a calendar to a funding requirement |  |
| `sec:39.13` | Exercises |  |
| `sec:39.14` | Solutions to exercises |  |
| `ex:39.1` | The Case P model blueprint |  |
| `ex:39.2` | A reserve corkscrew |  |
| `ex:39.3` | Counting columns for three periodicity choices |  |
| `ex:39.4` | One stub, three day counts |  |
| `ex:39.5` | The off-by-one operations flag |  |
| `ex:39.6` | Mapping annual inflation onto semiannual periods and a lagged reading |  |
| `ex:39.7` | A three-scenario switch |  |
| `exh:39.1` | Sheet flow of the Case P model (diagram) |  |
| `exh:39.2` | Color and format key |  |
| `exh:39.3` | Case P Time sheet, selected columns |  |
| `exh:39.4` | Defects in an illustrative sponsor model |  |
| `eq:39.1` | Period end rule (mixed timeline) |  |
| `eq:39.2` | Band overlap of operating months |  |
| `eq:39.3` | Year fraction rows (ACT/360, ACT/365, 30/360) |  |
| `fw:model-blueprint` | Framework 39.1 The model blueprint | home ssec:39.1.3 |

### Chapter 40: Modeling construction and funding

Source brief: `briefs/u09.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:40` | Modeling construction and funding |  |
| `sec:40.1` | The construction budget in the model |  |
| `ssec:40.1.1` | From a budget table to monthly costs |  |
| `ssec:40.1.2` | Timing rules for owner's costs, insurance, development costs and advisors |  |
| `ssec:40.1.3` | Contingency |  |
| `ssec:40.1.4` | Local-currency costs |  |
| `sec:40.2` | Sources and uses |  |
| `ssec:40.2.1` | Uses |  |
| `ssec:40.2.2` | Sources |  |
| `ssec:40.2.3` | Total funding requirement and gearing |  |
| `sec:40.3` | Drawdown order |  |
| `ssec:40.3.1` | Equity first, pro rata, debt first |  |
| `ssec:40.3.2` | Pro rata with letter-of-credit backing in Case P |  |
| `ssec:40.3.3` | Share capital, shareholder loans and capitalized interest |  |
| `ssec:40.3.4` | Standby facility and contingent equity |  |
| `sec:40.4` | Interest during construction and fees |  |
| `ssec:40.4.1` | IDC by tranche |  |
| `ssec:40.4.2` | Commitment fees |  |
| `ssec:40.4.3` | Upfront fees, agency fees, PRI premium and gross-up |  |
| `ssec:40.4.4` | The financed ECA premium |  |
| `sec:40.5` | The funding circularity and clean ways to resolve it |  |
| `ssec:40.5.1` | Where the loops are |  |
| `ssec:40.5.2` | Iterative calculation with a circuit breaker |  |
| `ssec:40.5.3` | Closed-form algebra |  |
| `ssec:40.5.4` | Pasted values and the converge macro |  |
| `ssec:40.5.5` | The method this book uses |  |
| `sec:40.6` | Walkthrough: one month of Case P funding |  |
| `sec:40.7` | Case P: the Funding sheet |  |
| `sec:40.8` | Practitioner's notebook |  |
| `sec:40.9` | Judgment drill |  |
| `sec:40.10` | A debt amount without a cash flow to repay it |  |
| `sec:40.11` | Exercises |  |
| `sec:40.12` | Solutions to exercises |  |
| `ex:40.1` | Sources and uses with financing costs |  |
| `ex:40.2` | Three drawdown orders |  |
| `ex:40.3` | Three ways to close the loop |  |
| `ex:40.4` | Withholding-tax gross-up |  |
| `ex:40.5` | A financed ECA premium in one month |  |
| `ex:40.6` | One month's commitment fee |  |
| `ex:40.7` | One month of IDC with a swap |  |
| `exh:40.1` | The funding loops (diagram) |  |
| `exh:40.2` | Construction cost timing rules for Case P (table of Inputs H rules) |  |
| `exh:40.3` | Month 1 of Case P funding |  |
| `exh:40.4` | Case P sources and uses at financial close |  |
| `exh:40.5` | Case P monthly drawdown schedule |  |
| `eq:40.1` | IDC by tranche |  |
| `eq:40.2` | Commitment fee |  |
| `eq:40.3` | Financed premium gross-up |  |
| `eq:40.4` | Lagged receipt by date (the SUMIFS device, used in Chapter 41) |  |
| `eq:40.5` | Total funding requirement |  |
| `eq:40.6` | Pro rata drawdown |  |
| `eq:40.7` | Affine solution for the total funding requirement |  |
| `fw:circularity-ladder` | Framework 40.1 The circularity ladder | home ssec:40.5.5 |

### Chapter 41: Modeling operations, tax and working capital

Source brief: `briefs/u09.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:41` | Modeling operations, tax and working capital |  |
| `sec:41.1` | Technical drivers: availability, dispatch, degradation and energy |  |
| `ssec:41.1.1` | Availability by operating year |  |
| `ssec:41.1.2` | Dispatch and energy delivered |  |
| `ssec:41.1.3` | Degradation and heat-rate headroom |  |
| `ssec:41.1.4` | Fuel quantities and equivalent operating hours |  |
| `sec:41.2` | Indexation in the model |  |
| `ssec:41.2.1` | Index levels from annual inflation |  |
| `ssec:41.2.2` | Reset dates and lagged readings |  |
| `ssec:41.2.3` | Partial indexation and the local share |  |
| `ssec:41.2.4` | FX paths |  |
| `sec:41.3` | Revenue build |  |
| `ssec:41.3.1` | Capacity payment with an availability cap |  |
| `ssec:41.3.2` | VOM and fuel pass-through |  |
| `ssec:41.3.3` | Transport and take-or-pay pass-throughs |  |
| `ssec:41.3.4` | Testing a pass-through |  |
| `sec:41.4` | Operating cost build |  |
| `ssec:41.4.1` | Fixed fees in two currencies |  |
| `ssec:41.4.2` | Usage-driven fees and incentives |  |
| `ssec:41.4.3` | Revenue-linked and lumpy costs |  |
| `ssec:41.4.4` | The tariff-to-row map |  |
| `sec:41.5` | Tax |  |
| `ssec:41.5.1` | Tax depreciation |  |
| `ssec:41.5.2` | Holidays and deferred depreciation |  |
| `ssec:41.5.3` | Interest deductibility |  |
| `ssec:41.5.4` | Losses and expiry |  |
| `ssec:41.5.5` | Minimum tax and tax paid |  |
| `ssec:41.5.6` | Withholding taxes |  |
| `sec:41.6` | Working capital |  |
| `sec:41.7` | VAT during construction |  |
| `sec:41.8` | Walkthrough: from a monthly invoice to the model |  |
| `sec:41.9` | Case P: operations and tax |  |
| `sec:41.10` | Practitioner's notebook |  |
| `sec:41.11` | Judgment drill |  |
| `sec:41.12` | Cash before debt service is not yet CFADS |  |
| `sec:41.13` | Exercises |  |
| `sec:41.14` | Solutions to exercises |  |
| `ex:41.1` | Capacity payment with an availability cap |  |
| `ex:41.2` | Partial indexation with a local share |  |
| `ex:41.3` | Fuel pass-through and heat-rate headroom |  |
| `ex:41.4` | Deferred against lost holiday depreciation |  |
| `ex:41.5` | Loss expiry under first in, first out |  |
| `ex:41.6` | Thin capitalization at 3:1 |  |
| `ex:41.7` | Interest limitation with carryforward and reactivation |  |
| `ex:41.8` | Working capital from days of flow |  |
| `ex:41.9` | Construction VAT and a VAT facility |  |
| `ex:41.10` | An LTSA variable fee |  |
| `exh:41.1` | Case P availability cycle and operating-year mapping |  |
| `exh:41.2` | Case P tariff-to-row map |  |
| `exh:41.3` | January 2022 invoice reconciliation |  |
| `exh:41.4` | Case P revenue build OY1 to OY10 |  |
| `exh:41.5` | Case P operating cost build OY1 to OY10 |  |
| `exh:41.6` | Case P tax computation OY1 to OY10 |  |
| `exh:41.7` | Case P construction VAT and working capital |  |
| `eq:41.1` | Capacity charge with partial indexation and local share |  |
| `eq:41.2` | Fuel charge on HHV |  |
| `eq:41.3` | Energy delivered |  |
| `eq:41.4` | Working capital balance from days |  |
| `eq:41.5` | Loss expiry under FIFO |  |
| `eq:41.6` | Interest limitation with reactivation |  |
| `fw:tariff-to-row-map` | Framework 41.1 The tariff-to-row map | home ssec:41.4.4 |
| `fw:tax-computation-stack` | Framework 41.2 The tax computation stack | home ssec:41.5.6 |

### Chapter 42: Modeling the waterfall, debt and reserves

Source brief: `briefs/u09.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:42` | Modeling the waterfall, debt and reserves |  |
| `sec:42.1` | From EBITDA to CFADS in the model |  |
| `ssec:42.1.1` | The CFADS row |  |
| `ssec:42.1.2` | The waterfall as tiers |  |
| `sec:42.2` | Sculpting in the model |  |
| `ssec:42.2.1` | The all-in cost factor |  |
| `ssec:42.2.2` | Discount factors and debt capacity |  |
| `ssec:42.2.3` | When the gearing cap binds |  |
| `ssec:42.2.4` | Scheduled balance and principal |  |
| `ssec:42.2.5` | Tranches on a common profile |  |
| `ssec:42.2.6` | ECA repayment tests |  |
| `ssec:42.2.7` | Closing the sizing loop |  |
| `ssec:42.2.8` | Sizing mode and locked-debt mode |  |
| `sec:42.3` | Reserve accounts |  |
| `ssec:42.3.1` | The DSRA |  |
| `ssec:42.3.2` | The MMRA |  |
| `ssec:42.3.3` | Handback reserve and the lock-up account |  |
| `sec:42.4` | Distribution tests, lock-ups and sweeps |  |
| `ssec:42.4.1` | The distribution test in rows |  |
| `ssec:42.4.2` | Lock-up cash and the two-consecutive rule |  |
| `ssec:42.4.3` | The soft mini-perm sweep |  |
| `ssec:42.4.4` | Dulles Greenway and the long lock-up |  |
| `sec:42.5` | Paying the shareholders and the dividend trap |  |
| `ssec:42.5.1` | Shareholder-loan interest and principal |  |
| `ssec:42.5.2` | The dividend trap |  |
| `ssec:42.5.3` | Solutions and their limits |  |
| `sec:42.6` | Financial statements from the model |  |
| `ssec:42.6.1` | Income statement and retained earnings |  |
| `ssec:42.6.2` | Balance sheet and the balance check |  |
| `ssec:42.6.3` | Cash flow statement and the cash check |  |
| `sec:42.7` | Walkthrough: one period through the Case P waterfall |  |
| `sec:42.8` | Case P: the waterfall, sculpting and reserves |  |
| `sec:42.9` | Practitioner's notebook |  |
| `sec:42.10` | Judgment drill |  |
| `sec:42.11` | A model that works but has not been tested |  |
| `sec:42.12` | Exercises |  |
| `sec:42.13` | Solutions to exercises |  |
| `ex:42.1` | Sculpting six periods in the model |  |
| `ex:42.2` | Scaling when gearing binds |  |
| `ex:42.3` | A sensitivity in sizing mode and in locked mode |  |
| `ex:42.4` | DSRA through a shortfall |  |
| `ex:42.5` | MMRA accumulation |  |
| `ex:42.6` | Historic DSCR and the lock-up |  |
| `ex:42.7` | The soft mini-perm sweep |  |
| `ex:42.8` | The dividend trap and the shareholder-loan solution |  |
| `exh:42.1` | The Case P model waterfall (diagram) |  |
| `exh:42.2` | Sizing mode and locked mode compared (rows) |  |
| `exh:42.3` | One period through the Case P waterfall |  |
| `exh:42.4` | Case P senior debt sizing results |  |
| `exh:42.5` | Case P sculpted repayment profile and ECA tests |  |
| `exh:42.6` | Case P DSRA and MMRA |  |
| `exh:42.7` | Case P waterfall OY1 to OY3 and dividend-trap check |  |
| `exh:42.8` | Case P financial statements OY1 to OY3 |  |
| `eq:42.1` | CFADS row |  |
| `eq:42.2` | All-in cost factor |  |
| `eq:42.3` | Debt capacity | ruling: Debt capacity row, implementing eq:36.3 (model row) |
| `eq:42.4` | Sculpted principal | ruling: Sculpted principal row, implementing eq:36.2 (model row) |
| `eq:42.5` | DSRA target | ruling: DSRA target row with look-ahead, implementing eq:37.1 (model row) |
| `eq:42.6` | MMRA contribution |  |
| `eq:42.7` | Distributable reserves |  |
| `fw:waterfall-tier` | Framework 42.1 The four-row waterfall tier | home ssec:42.1.2 |
| `fw:dividend-trap-test` | Framework 42.2 The dividend trap test | home ssec:42.5.3 |

### Chapter 43: Returns, ratios, scenarios and outputs

Source brief: `briefs/u09.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:43` | Returns, ratios, scenarios and outputs |  |
| `sec:43.1` | Ratios in the model |  |
| `ssec:43.1.1` | Period, historic and projected DSCR |  |
| `ssec:43.1.2` | LLCR and PLCR as rows |  |
| `ssec:43.1.3` | Summary statistics |  |
| `sec:43.2` | Returns |  |
| `ssec:43.2.1` | Equity cash flows |  |
| `ssec:43.2.2` | XIRR and XNPV on mixed periods |  |
| `ssec:43.2.3` | Project IRR |  |
| `ssec:43.2.4` | Payback, multiple and cash yield |  |
| `sec:43.3` | Scenarios |  |
| `ssec:43.3.1` | Sizing cases and test cases |  |
| `ssec:43.3.2` | Running scenarios by macro |  |
| `ssec:43.3.3` | Scenarios that move the timeline |  |
| `sec:43.4` | Sensitivities and breakevens |  |
| `ssec:43.4.1` | Wiring the ten Case P sensitivities |  |
| `ssec:43.4.2` | Tornado presentation |  |
| `ssec:43.4.3` | Breakevens |  |
| `sec:43.5` | Monte Carlo simulation |  |
| `ssec:43.5.1` | Choosing what to simulate |  |
| `ssec:43.5.2` | Implementing it |  |
| `ssec:43.5.3` | Reading the results |  |
| `ssec:43.5.4` | What simulation misses |  |
| `sec:43.6` | Outputs and dashboards |  |
| `ssec:43.6.1` | What a committee reads |  |
| `ssec:43.6.2` | Charts that carry information |  |
| `ssec:43.6.3` | Live outputs and pasted results |  |
| `sec:43.7` | Integrity checks |  |
| `ssec:43.7.1` | The catalogue |  |
| `ssec:43.7.2` | Errors and warnings |  |
| `sec:43.8` | Walkthrough: reading the Case P scenario and sensitivity table |  |
| `sec:43.9` | Case P: returns, ratios and outputs |  |
| `sec:43.10` | Practitioner's notebook |  |
| `sec:43.11` | Judgment drill |  |
| `sec:43.12` | A model its builder trusts |  |
| `sec:43.13` | Exercises |  |
| `sec:43.14` | Solutions to exercises |  |
| `ex:43.1` | XIRR against IRR on uneven periods |  |
| `ex:43.2` | A tornado for one period |  |
| `ex:43.3` | Breakeven by goal seek and by algebra |  |
| `ex:43.4` | The cap and the simulation mean |  |
| `ex:43.5` | Locked and unlocked downside |  |
| `exh:43.1` | Ratio rows and term-sheet definitions |  |
| `exh:43.2` | Case P sensitivity wiring |  |
| `exh:43.3` | Case P dashboard |  |
| `exh:43.4` | Case P scenario and sensitivity results |  |
| `exh:43.5` | Case P ratios by case |  |
| `exh:43.6` | Case P returns and breakevens |  |
| `exh:43.7` | Case P Monte Carlo results |  |
| `eq:43.1` | LLCR row at a period end | ruling: LLCR row at a period end, implementing eq:35.3 (model row) |
| `eq:43.2` | PLCR row |  |
| `eq:43.3` | XIRR condition |  |
| `eq:43.4` | Expected capped payment factor |  |
| `eq:43.5` | Months-of-zero-payment breakeven |  |
| `fw:locked-debt-test-protocol` | Framework 43.1 The locked-debt test protocol | home sec:43.2 |
| `fw:integrity-check-catalogue` | Framework 43.2 The integrity-check catalogue | home ssec:43.7.1 |

### Chapter 44: Auditing a model

Source brief: `briefs/u09.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:44` | Auditing a model |  |
| `sec:44.1` | What a model audit is for |  |
| `ssec:44.1.1` | Why lenders require it and what they rely on |  |
| `ssec:44.1.2` | Audit, review, shadow model and reperformance |  |
| `sec:44.2` | The audit process |  |
| `ssec:44.2.1` | Scoping |  |
| `ssec:44.2.2` | Structural review |  |
| `ssec:44.2.3` | Unique-formula review |  |
| `ssec:44.2.4` | Input reconciliation |  |
| `ssec:44.2.5` | Analytical review |  |
| `ssec:44.2.6` | Reperformance and the shadow model |  |
| `ssec:44.2.7` | Flex testing |  |
| `ssec:44.2.8` | Reporting |  |
| `sec:44.3` | The classic errors |  |
| `ssec:44.3.1` | Timing errors |  |
| `ssec:44.3.2` | Units and sign errors |  |
| `ssec:44.3.3` | Contract logic errors |  |
| `ssec:44.3.4` | Range and copy errors |  |
| `ssec:44.3.5` | Hard-coded numbers and scenario leaks |  |
| `ssec:44.3.6` | Circularity and convergence errors |  |
| `ssec:44.3.7` | Tax and accounting errors |  |
| `ssec:44.3.8` | Errors of omission |  |
| `sec:44.4` | Reviewing someone else's model in two days |  |
| `ssec:44.4.1` | The first hour |  |
| `ssec:44.4.2` | The first day |  |
| `ssec:44.4.3` | The second day |  |
| `sec:44.5` | Walkthrough: one finding from discovery to closure |  |
| `sec:44.6` | Case P: Ferrand Model Assurance's audit |  |
| `sec:44.7` | Practitioner's notebook |  |
| `sec:44.8` | Judgment drill |  |
| `sec:44.9` | An audited model of one asset |  |
| `sec:44.10` | Exercises |  |
| `sec:44.11` | Solutions to exercises |  |
| `ex:44.1` | The missing availability cap |  |
| `ex:44.2` | A hard-coded dispatch factor |  |
| `ex:44.3` | Analytical review of a DSCR profile |  |
| `ex:44.4` | A shadow sizing |  |
| `ex:44.5` | A SUM one column short |  |
| `exh:44.1` | Error families and the pass that catches each |  |
| `exh:44.2` | A findings-log entry |  |
| `exh:44.3` | Case P audit findings and effects |  |
| `exh:44.4` | The two-day review plan |  |
| `fw:seven-pass-review` | Framework 44.1 The seven-pass model review | home sec:44.2 |
| `fw:finding-severity` | Framework 44.2 Finding severity grades | home ssec:44.2.8 |

### Chapter 45: Sector-specific modeling

Source brief: `briefs/u09.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:45` | Sector-specific modeling |  |
| `sec:45.1` | The sector module pattern |  |
| `sec:45.2` | Energy yield and P-values |  |
| `ssec:45.2.1` | From a yield report to model rows |  |
| `ssec:45.2.2` | Which P-value in which case |  |
| `ssec:45.2.3` | Portfolios |  |
| `ssec:45.2.4` | Case R's inputs as rows |  |
| `sec:45.3` | Degradation and augmentation |  |
| `ssec:45.3.1` | Wind and solar degradation rows |  |
| `ssec:45.3.2` | Battery fade, state of health and augmentation |  |
| `ssec:45.3.3` | Case R's augmentation inputs |  |
| `sec:45.4` | Availability and curtailment |  |
| `ssec:45.4.1` | Technical and contractual availability; deemed energy |  |
| `ssec:45.4.2` | Curtailment and capture prices |  |
| `ssec:45.4.3` | Merchant revenue with hedges as rows |  |
| `sec:45.5` | Traffic ramp-up |  |
| `ssec:45.5.1` | Traffic to revenue |  |
| `ssec:45.5.2` | Ramp-up and growth |  |
| `ssec:45.5.3` | Elasticity and toll changes |  |
| `ssec:45.5.4` | Tracking forecast against actual |  |
| `sec:45.6` | Mining reserves, grades and recoveries |  |
| `ssec:45.6.1` | From reserve statement to mine plan rows |  |
| `ssec:45.6.2` | Recovery, concentrate and net smelter return |  |
| `ssec:45.6.3` | Grade decline and the reserve tail |  |
| `sec:45.7` | LNG and commodity-linked revenue |  |
| `ssec:45.7.1` | Tolling-style LNG sales |  |
| `ssec:45.7.2` | Oil-linked and hybrid pricing |  |
| `ssec:45.7.3` | Price decks |  |
| `sec:45.8` | PPP payment mechanisms and deductions |  |
| `ssec:45.8.1` | Unitary charge and deductions in rows |  |
| `ssec:45.8.2` | Deductions in the financial model |  |
| `sec:45.9` | Walkthrough: reading a yield assessment into the model |  |
| `sec:45.10` | Case T: the traffic model against actual traffic |  |
| `sec:45.11` | Case R: the yield and capture model |  |
| `sec:45.12` | Practitioner's notebook |  |
| `sec:45.13` | Judgment drill |  |
| `sec:45.14` | Cash flows waiting for a discount rate |  |
| `sec:45.15` | Exercises |  |
| `sec:45.16` | Solutions to exercises |  |
| `ex:45.1` | A solar yield module |  |
| `ex:45.2` | Portfolio P90 |  |
| `ex:45.3` | Battery fade and augmentation |  |
| `ex:45.4` | Toll-road ramp-up and elasticity |  |
| `ex:45.5` | A copper concentrate module |  |
| `ex:45.6` | LNG and oil-linked revenue |  |
| `ex:45.7` | An availability payment with deductions |  |
| `ex:45.8` | Revenue buckets for a hedged wind farm |  |
| `exh:45.1` | Sector module interfaces |  |
| `exh:45.2` | Illustrative wind yield assessment summary |  |
| `exh:45.3` | Case T traffic: forecasts and actuals |  |
| `exh:45.4` | Case T revenue ramp-up against actual |  |
| `exh:45.5` | Case R P-values by asset |  |
| `exh:45.6` | Case R capture and revenue build |  |
| `exh:45.7` | Case R battery capacity and augmentation (pending R-F11) |  |
| `eq:45.1` | Combined uncertainty |  |
| `eq:45.2` | P-value from P50 and sigma |  |
| `eq:45.3` | Toll revenue | ruling: Toll revenue row by vehicle class with leakage, implementing eq:12.4 (model row) |
| `eq:45.4` | Net smelter return |  |
| `eq:45.5` | Availability deduction | ruling: Availability deduction row for a supplied mechanism, implementing eq:58.2 (model row, forward reference) |
| `fw:revenue-driver-decomposition` | Framework 45.1 Revenue driver decomposition | home sec:45.1 |

### Chapter 46: Equity returns and valuation through the project's life

Source brief: `briefs/u10.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:46` | Equity returns and valuation through the project's life |  |
| `sec:46.1` | Four measures of what equity earns |  |
| `ssec:46.1.1` | Project IRR and equity IRR |  |
| `ssec:46.1.2` | NPV at a hurdle rate, and why IRR is not a price |  |
| `ssec:46.1.3` | Cash yield and payback |  |
| `ssec:46.1.4` | Money multiples and the IRR-multiple tension |  |
| `ssec:46.1.5` | Stating a return so it can be compared |  |
| `sec:46.2` | The cost of equity and hurdle rates by stage |  |
| `ssec:46.2.1` | From CAPM to a project hurdle |  |
| `ssec:46.2.2` | Stage premia and what each point pays for |  |
| `ssec:46.2.3` | Country, currency and contract-quality premia |  |
| `ssec:46.2.4` | Hurdles in practice, from committee targets to bid and hold rates |  |
| `sec:46.3` | Development economics and where value is created |  |
| `ssec:46.3.1` | The development budget as an option premium |  |
| `ssec:46.3.2` | Valuation at each milestone with the value staircase |  |
| `ssec:46.3.3` | Who captures the step-ups |  |
| `ssec:46.3.4` | Value created in construction and at COD |  |
| `sec:46.4` | Valuing an operating project |  |
| `ssec:46.4.1` | Unlevered and levered DCF, and the equity bridge |  |
| `ssec:46.4.2` | Valuation by risk bucket |  |
| `ssec:46.4.3` | Finite lives, tails and residual value |  |
| `ssec:46.4.4` | Multiples as cross-checks, and why they mislead |  |
| `ssec:46.4.5` | A sensitivity hierarchy for operating-asset value |  |
| `sec:46.5` | What secondary sales reveal about equity value in UK PFI |  |
| `ssec:46.5.1` | The M25 equity sale and returns on early equity |  |
| `ssec:46.5.2` | Refinancing and the jump in projected equity IRR |  |
| `ssec:46.5.3` | Equity competitions and disclosed returns |  |
| `sec:46.6` | Walkthrough: reading a valuation report on an operating portfolio |  |
| `sec:46.7` | Case R: valuing A1 by risk bucket |  |
| `sec:46.8` | Practitioner's notebook |  |
| `sec:46.9` | Judgment drill |  |
| `sec:46.10` | A valuation sets your ceiling, and the bid must beat other bidders' ceilings |  |
| `sec:46.11` | Exercises |  |
| `sec:46.12` | Solutions to exercises |  |
| `ex:46.1` | Five return metrics on one solar plant |  |
| `ex:46.2` | Building a cost of equity for a contracted operating asset |  |
| `ex:46.3` | The value staircase for a wind project |  |
| `ex:46.4` | Pricing a 30% stake sold at financial close |  |
| `ex:46.5` | Valuing an operating asset by risk bucket |  |
| `ex:46.6` | Why EV/EBITDA misleads for finite-life assets |  |
| `exh:46.1` | Return metrics compared on one project (Illustrative) |  |
| `exh:46.2` | Indicative hurdle rates by project stage (Illustrative; indicative ranges) |  |
| `exh:46.3` | The value staircase (chart) (Illustrative) |  |
| `exh:46.4` | Valuation by risk bucket against a single blended rate (USD m) (Illustrative) |  |
| `exh:46.5` | Case R A1 valuation by asset and risk bucket at bid (USD m) (Case R) |  |
| `exh:46.6` | Disclosed PF2 equity returns (Real case: UK PF2, 2012--2021) |  |
| `eq:46.1` | Equity IRR definition (equity cash flows including shareholder loans) | ruling: Equity cash flow convention for IRR measurement (conventions owned here; definition ssec:8.2.1, R-013) |
| `eq:46.2` | Milestone value roll-back |  |
| `eq:46.3` | Equity bridge |  |
| `fw:value-staircase` | Framework 46.1 The value staircase | home ssec:46.3.2 |
| `fw:risk-bucket-valuation` | Framework 46.2 Risk-bucket valuation | home ssec:46.4.2 |

### Chapter 47: Bidding, acquisitions and infrastructure funds

Source brief: `briefs/u10.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:47` | Bidding, acquisitions and infrastructure funds |  |
| `sec:47.1` | How competitive tenders set the price |  |
| `ssec:47.1.1` | Bid variables and how bidders read an evaluation formula |  |
| `ssec:47.1.2` | Building the bid tariff from a target return |  |
| `ssec:47.1.3` | What sits behind a record tariff |  |
| `ssec:47.1.4` | Bid costs, bid security and committed finance |  |
| `sec:47.2` | The winner's curse |  |
| `ssec:47.2.1` | Why the winner is the most optimistic bidder |  |
| `ssec:47.2.2` | Where optimism hides in a bid |  |
| `ssec:47.2.3` | Bid shading and the expected-value bid |  |
| `ssec:47.2.4` | The bid discipline check |  |
| `ssec:47.2.5` | Indiana Toll Road and a winning bid financed to the limit |  |
| `sec:47.3` | Buying and selling operating assets |  |
| `ssec:47.3.1` | The auction process from teaser to completion |  |
| `ssec:47.3.2` | Bilateral deals, pre-emption rights and consents |  |
| `ssec:47.3.3` | The sale and purchase agreement |  |
| `ssec:47.3.4` | Locked box versus completion accounts |  |
| `ssec:47.3.5` | Warranty and indemnity insurance |  |
| `ssec:47.3.6` | Buying a construction-stage asset |  |
| `sec:47.4` | Portfolio construction |  |
| `ssec:47.4.1` | Diversifying cash yield |  |
| `ssec:47.4.2` | Concentration limits and correlation in stress |  |
| `ssec:47.4.3` | Platforms versus single assets |  |
| `sec:47.5` | How infrastructure funds think, invest and are paid |  |
| `ssec:47.5.1` | Fund structures and strategies |  |
| `ssec:47.5.2` | Fees, preferred return and carried interest |  |
| `ssec:47.5.3` | Gross and net returns, and what investors actually earn |  |
| `ssec:47.5.4` | How fund economics shape behavior |  |
| `sec:47.6` | Walkthrough: the bid committee pack for a tariff tender |  |
| `sec:47.7` | Walkthrough: a locked-box SPA, clause by clause |  |
| `sec:47.8` | Case P: the 2016 tariff bid |  |
| `sec:47.9` | Case T: the BAFO that won the Merrick Link |  |
| `sec:47.10` | Case R: the A1 auction |  |
| `sec:47.11` | Practitioner's notebook |  |
| `sec:47.12` | Judgment drill |  |
| `sec:47.13` | Winning the asset starts the diligence |  |
| `sec:47.14` | Exercises |  |
| `sec:47.15` | Solutions to exercises |  |
| `ex:47.1` | Solving the bid tariff for a solar tender (Illustrative) |  |
| `ex:47.2` | How much the winner overestimates (Illustrative) |  |
| `ex:47.3` | The expected-value bid (Illustrative) |  |
| `ex:47.4` | Locked box against completion accounts (Illustrative) |  |
| `ex:47.5` | What a W&I policy pays (Illustrative) |  |
| `ex:47.6` | Diversifying a portfolio's cash yield (Illustrative) |  |
| `ex:47.7` | A fund waterfall from gross to net (Illustrative) |  |
| `exh:47.1` | Bid tariff sensitivities (USD/MWh) (Illustrative) |  |
| `exh:47.2` | Expected bias of the winning estimate by number of bidders (Illustrative) |  |
| `exh:47.3` | Expected NPV of a bid by tariff (USD m) (Illustrative) |  |
| `exh:47.4` | An auction sale process and its timeline (Illustrative) |  |
| `exh:47.5` | SPA terms: seller, buyer and market positions (Illustrative; indicative ranges) |  |
| `exh:47.6` | Fund distribution waterfall by year (USD m) (Illustrative) |  |
| `exh:47.7` | Case P bid evaluation basis and tariff components (Case P) |  |
| `exh:47.8` | Case T BAFO contributions against the reference (ARD m) (Case T) |  |
| `exh:47.9` | Case R A1 bid against valuation (USD m) (Case R) |  |
| `cl:47.1` | Permitted leakage and leakage indemnity, share purchase agreement |  |
| `cl:47.2` | Limitation of seller liability where a W&I policy is in place, share purchase agreement |  |
| `eq:47.1` | Levelized tariff | ruling: Bid tariff solved for a target equity IRR, citing eq:5.11 (repurposed, R-001) |
| `eq:47.2` | Expected error of the winning estimate |  |
| `eq:47.3` | Expected NPV of a bid |  |
| `eq:47.4` | Locked-box price with ticker and leakage |  |
| `fw:bid-discipline-check` | Framework 47.1 The bid discipline check | home ssec:47.2.4 |
| `fw:pricing-mechanism-choice` | Framework 47.2 Choosing the price mechanism | home ssec:47.3.4 |

### Chapter 48: Technical, resource and market diligence

Source brief: `briefs/u10.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:48` | Technical, resource and market diligence |  |
| `sec:48.1` | How diligence is organized and who relies on whom |  |
| `ssec:48.1.1` | Advisors, reliance and duty of care |  |
| `ssec:48.1.2` | Scoping a diligence program |  |
| `ssec:48.1.3` | The report challenge protocol |  |
| `sec:48.2` | The independent engineer |  |
| `ssec:48.2.1` | What the independent engineer reviews |  |
| `ssec:48.2.2` | Technology risk and equipment bankability |  |
| `ssec:48.2.3` | Testing the construction budget and contingency |  |
| `ssec:48.2.4` | Testing the schedule and the probability of delay |  |
| `ssec:48.2.5` | Reviewing operating assumptions |  |
| `ssec:48.2.6` | The IE after financial close |  |
| `sec:48.3` | Resource and reserves diligence |  |
| `ssec:48.3.1` | Wind and solar energy yield |  |
| `ssec:48.3.2` | Hydrology and geothermal resource |  |
| `ssec:48.3.3` | Mineral and hydrocarbon reserves |  |
| `ssec:48.3.4` | Fuel and feedstock supply adequacy |  |
| `sec:48.4` | Market and price-curve diligence |  |
| `ssec:48.4.1` | How a market advisor builds a price curve |  |
| `ssec:48.4.2` | Capture prices, cannibalization and basis in the curve |  |
| `ssec:48.4.3` | Comparing two advisors' curves |  |
| `ssec:48.4.4` | Commodity markets beyond power |  |
| `ssec:48.4.5` | Which curve the lenders size on |  |
| `sec:48.5` | Traffic and demand studies |  |
| `ssec:48.5.1` | How a traffic study is built |  |
| `ssec:48.5.2` | Value of time, elasticity and diversion |  |
| `ssec:48.5.3` | Ramp-up and land-use assumptions |  |
| `ssec:48.5.4` | Sydney's Cross City and Lane Cove tunnels and the winning forecast |  |
| `ssec:48.5.5` | Demand studies beyond roads |  |
| `sec:48.6` | Walkthrough: reading an independent engineer's report |  |
| `sec:48.7` | Case P: Gwen Treharne's report and the one-in-eight call |  |
| `sec:48.8` | Case T: two traffic studies for one road |  |
| `sec:48.9` | Practitioner's notebook |  |
| `sec:48.10` | Judgment drill |  |
| `sec:48.11` | Engineering reports measure physical risk, and documents hide the rest |  |
| `sec:48.12` | Exercises |  |
| `sec:48.13` | Solutions to exercises |  |
| `ex:48.1` | Is the contingency enough? (Illustrative) |  |
| `ex:48.2` | What a delay distribution costs (Illustrative) |  |
| `ex:48.3` | Challenging a wind yield report (Illustrative) |  |
| `ex:48.4` | Reserve life against loan tenor (Illustrative) |  |
| `ex:48.5` | Two price curves for one merchant tail (Illustrative) |  |
| `ex:48.6` | Value of time and diversion (Illustrative) |  |
| `exh:48.1` | Diligence scope matrix for an onshore wind financing (Illustrative) |  |
| `exh:48.2` | Three-point capex estimates and contingency confidence (USD m) (Illustrative) |  |
| `exh:48.3` | Delay bands, cost and LD recovery (USD m) (Illustrative) |  |
| `exh:48.4` | Energy yield loss chain and uncertainty, sponsor against lenders' consultant (Illustrative) |  |
| `exh:48.5` | Two price curves and merchant-tail value (EUR m) (Illustrative) |  |
| `exh:48.6` | Diversion share against value of time (chart) (Illustrative) |  |
| `exh:48.7` | Cross City Tunnel forecasts against actual traffic (Real case: Cross City Tunnel, 2002--2006) |  |
| `exh:48.8` | Case T traffic cases and actuals (thousand trips a day) (Case T) |  |
| `exh:48.9` | Case P technical inputs reviewed by the IE (Case P) |  |
| `eq:48.1` | PERT mean and standard deviation |  |
| `eq:48.2` | Net energy from gross through the loss chain |  |
| `eq:48.3` | Reserve tail |  |
| `eq:48.4` | Binary logit diversion |  |
| `fw:dd-scope-matrix` | Framework 48.1 The diligence scope matrix | home ssec:48.1.2 |
| `fw:report-challenge` | Framework 48.2 The report challenge protocol | home ssec:48.1.3 |

### Chapter 49: Legal, insurance, model, tax and integrity diligence

Source brief: `briefs/u10.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:49` | Legal, insurance, model, tax and integrity diligence |  |
| `sec:49.1` | Legal and regulatory due diligence |  |
| `ssec:49.1.1` | What lenders' counsel reviews and why |  |
| `ssec:49.1.2` | The legal due diligence report and its red-flag grid |  |
| `ssec:49.1.3` | Permits, licenses and land against the loan's life |  |
| `ssec:49.1.4` | Reviewing the project contracts |  |
| `ssec:49.1.5` | Legal opinions and their qualifications |  |
| `ssec:49.1.6` | Regulatory diligence |  |
| `sec:49.2` | Insurance due diligence |  |
| `ssec:49.2.1` | The lenders' insurance advisor's mandate |  |
| `ssec:49.2.2` | Testing the program against the losses that matter |  |
| `ssec:49.2.3` | Insurer security, fronting and reinsurance |  |
| `ssec:49.2.4` | The broker's letter of undertaking and the insurance CPs |  |
| `sec:49.3` | Model audit engagement |  |
| `ssec:49.3.1` | Scope of a model audit engagement |  |
| `ssec:49.3.2` | Materiality and sign-off |  |
| `ssec:49.3.3` | Reliance, liability caps and the bring-down |  |
| `sec:49.4` | Tax and accounting due diligence |  |
| `ssec:49.4.1` | Reviewing project-level tax |  |
| `ssec:49.4.2` | Quantifying leakage |  |
| `ssec:49.4.3` | Tax opinions, rulings and indemnities |  |
| `ssec:49.4.4` | Accounting diligence |  |
| `sec:49.5` | Counterparty credit diligence |  |
| `ssec:49.5.1` | Which counterparties matter and how much |  |
| `ssec:49.5.2` | Analyzing a state-owned offtaker |  |
| `ssec:49.5.3` | Contractor, supplier and hedge counterparty credit |  |
| `ssec:49.5.4` | The counterparty credit card |  |
| `sec:49.6` | KYC, sanctions and anti-corruption diligence |  |
| `ssec:49.6.1` | Know your customer and beneficial ownership |  |
| `ssec:49.6.2` | Sanctions screening and ownership tracing |  |
| `ssec:49.6.3` | Anti-corruption diligence |  |
| `ssec:49.6.4` | From findings to documents |  |
| `ssec:49.6.5` | When the screen changes after close |  |
| `sec:49.7` | Walkthrough: reading a lenders' legal due diligence report |  |
| `sec:49.8` | Case P: the legal due diligence report and KYC on Groupe Talmé |  |
| `sec:49.9` | Practitioner's notebook |  |
| `sec:49.10` | Judgment drill |  |
| `sec:49.11` | The project's neighbors need their own diligence |  |
| `sec:49.12` | Exercises |  |
| `sec:49.13` | Solutions to exercises |  |
| `ex:49.1` | Testing permits and land against the loan (Illustrative) |  |
| `ex:49.2` | Does the delay and business interruption cover pay the debt? (Illustrative) |  |
| `ex:49.3` | How material is a model error? (Illustrative) |  |
| `ex:49.4` | Quantifying tax leakage (Illustrative) |  |
| `ex:49.5` | Can the utility pay? (Illustrative) |  |
| `ex:49.6` | Tracing ownership through a sanctions screen (Illustrative) |  |
| `exh:49.1` | A red-flag grid for an IPP financing (Illustrative) |  |
| `exh:49.2` | Permit and land schedule against the loan (Illustrative) |  |
| `exh:49.3` | BI cover against debt service and spare lead times (USD m) (Illustrative) |  |
| `exh:49.4` | Utility cash available for IPPs (USD m per month) (Illustrative) |  |
| `exh:49.5` | Ownership chart and sanctions test (Illustrative) |  |
| `exh:49.6` | Case P legal DD findings graded (Case P) |  |
| `cl:49.1` | Opinion paragraph on enforceability with qualifications, local-law legal opinion |  |
| `eq:49.1` | Required BI daily indemnity |  |
| `eq:49.2` | Withholding tax gross-up cost |  |
| `fw:red-flag-grid` | Framework 49.1 The red-flag grid | home ssec:49.1.2 |
| `fw:counterparty-credit-card` | Framework 49.2 The counterparty credit card | home ssec:49.5.4 |
| `fw:ownership-trace` | Framework 49.3 The ownership trace | home ssec:49.6.2 |

### Chapter 50: Environmental and social risk and standards

Source brief: `briefs/u10.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:50` | Environmental and social risk and standards |  |
| `sec:50.1` | Why environmental and social failure is credit risk |  |
| `ssec:50.1.1` | How E&S failure reaches the lenders |  |
| `ssec:50.1.2` | Pricing an E&S delay |  |
| `ssec:50.1.3` | Cobre Panamá and compliance without legitimacy |  |
| `sec:50.2` | The rulebooks lenders apply |  |
| `ssec:50.2.1` | The IFC Performance Standards |  |
| `ssec:50.2.2` | The Equator Principles |  |
| `ssec:50.2.3` | The World Bank Environmental and Social Framework |  |
| `ssec:50.2.4` | Export credit agencies and the OECD Common Approaches |  |
| `ssec:50.2.5` | One action plan for several lenders |  |
| `sec:50.3` | The assessment and management documents |  |
| `ssec:50.3.1` | The ESIA |  |
| `ssec:50.3.2` | ESMS and ESMP |  |
| `ssec:50.3.3` | The ESAP and how it becomes conditions and covenants |  |
| `ssec:50.3.4` | The independent E&S consultant and monitoring |  |
| `sec:50.4` | Stakeholder engagement and grievance |  |
| `ssec:50.4.1` | Stakeholder engagement plans and disclosure |  |
| `ssec:50.4.2` | Grievance mechanisms that work |  |
| `sec:50.5` | Land acquisition and resettlement |  |
| `ssec:50.5.1` | PS5 principles |  |
| `ssec:50.5.2` | Building a resettlement budget |  |
| `ssec:50.5.3` | Resettlement and the construction schedule |  |
| `sec:50.6` | Indigenous peoples and free, prior and informed consent |  |
| `ssec:50.6.1` | When PS7 applies |  |
| `ssec:50.6.2` | What FPIC requires and what it does not |  |
| `ssec:50.6.3` | FPIC in high-income countries under EP4 |  |
| `sec:50.7` | Biodiversity |  |
| `ssec:50.7.1` | Habitat classification and critical habitat |  |
| `ssec:50.7.2` | Offsets, no net loss and net gain |  |
| `ssec:50.7.3` | Bujagali and an offset undone by the host government's own project |  |
| `sec:50.8` | Labor, safety, security and human rights |  |
| `ssec:50.8.1` | Labor and working conditions |  |
| `ssec:50.8.2` | Community health, safety and security |  |
| `ssec:50.8.3` | Human rights due diligence |  |
| `ssec:50.8.4` | Cultural heritage |  |
| `sec:50.9` | Compliance certified and outcome failed in Chad and Cameroon |  |
| `sec:50.10` | Walkthrough: turning an ESAP into conditions precedent and covenants |  |
| `sec:50.11` | Case P: resettlement at Bélanou and the Category A review |  |
| `sec:50.12` | Practitioner's notebook |  |
| `sec:50.13` | Judgment drill |  |
| `sec:50.14` | Every diligence finding has to land in a document |  |
| `sec:50.15` | Exercises |  |
| `sec:50.16` | Solutions to exercises |  |
| `ex:50.1` | What a community blockade costs (Illustrative) |  |
| `ex:50.2` | Does EP4 apply? (Illustrative) |  |
| `ex:50.3` | Emissions thresholds for a gas plant (Illustrative) |  |
| `ex:50.4` | A resettlement budget at full replacement cost (Illustrative) |  |
| `ex:50.5` | Testing a biodiversity offset (Illustrative) |  |
| `exh:50.1` | E&S-to-credit transmission map (diagram) (Illustrative) |  |
| `exh:50.2` | The eight Performance Standards and their financing consequences (Illustrative) |  |
| `exh:50.3` | Resettlement budget at full replacement cost (USD) (Illustrative) |  |
| `exh:50.4` | EP4 applicability decisions for six transactions (Illustrative) |  |
| `exh:50.5` | Case P resettlement and E&S cost items (USD m) (Case P) |  |
| `cl:50.1` | Environmental and social covenant with ESAP compliance and cure period, common terms agreement |  |
| `eq:50.1` | Habitat units and offset gain |  |
| `fw:es-credit-map` | Framework 50.1 The E&S-to-credit transmission map | home ssec:50.1.1 |
| `fw:es-applicability` | Framework 50.2 The E&S applicability tree | home ssec:50.2.2 |

### Chapter 51: The finance documents

Source brief: `briefs/u11.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:51` | The finance documents |  |
| `sec:51.1` | The document set and how it flows |  |
| `ssec:51.1.1` | From mandate letter to financial close |  |
| `ssec:51.1.2` | Mandate letters, commitment letters and fee letters |  |
| `ssec:51.1.3` | The common terms agreement and the facility agreements |  |
| `ssec:51.1.4` | Hedging documents under the ISDA framework |  |
| `ssec:51.1.5` | Working with LMA, LSTA and APLMA forms |  |
| `sec:51.2` | Conditions precedent |  |
| `ssec:51.2.1` | What conditions precedent are for |  |
| `ssec:51.2.2` | The initial conditions precedent list |  |
| `ssec:51.2.3` | Drawdown conditions during construction |  |
| `ssec:51.2.4` | Waiving conditions and converting them to conditions subsequent |  |
| `sec:51.3` | Representations and warranties |  |
| `ssec:51.3.1` | What representations do in a non-recourse loan |  |
| `ssec:51.3.2` | Project-specific representations |  |
| `sec:51.4` | Covenants |  |
| `ssec:51.4.1` | Information covenants |  |
| `ssec:51.4.2` | Positive and negative covenants |  |
| `ssec:51.4.3` | Financial covenants as drafted |  |
| `ssec:51.4.4` | Permitted debt, permitted security and permitted disposals |  |
| `ssec:51.4.5` | Distributions and restricted payments as drafted |  |
| `sec:51.5` | Events of default and remedies |  |
| `ssec:51.5.1` | The standard list and the project list |  |
| `ssec:51.5.2` | Grace periods, materiality and thresholds |  |
| `ssec:51.5.3` | Remedies and why project lenders rarely accelerate |  |
| `ssec:51.5.4` | Equity cures |  |
| `sec:51.6` | Change of control and transfers |  |
| `ssec:51.6.1` | Change of control and sponsor lock-in |  |
| `ssec:51.6.2` | Lender transfers |  |
| `sec:51.7` | Amendments, waivers and voting |  |
| `ssec:51.7.1` | Decision thresholds inside a facility |  |
| `ssec:51.7.2` | Defaulting lenders, deemed consent and replacing a holdout |  |
| `ssec:51.7.3` | The waiver and amendment letter |  |
| `sec:51.8` | Walkthrough: reading a common terms agreement in one sitting |  |
| `sec:51.9` | Case P: the common terms agreement |  |
| `sec:51.10` | Practitioner's notebook |  |
| `sec:51.11` | Judgment drill |  |
| `sec:51.12` | The documents give lenders rights; security decides whether they can use them |  |
| `sec:51.13` | Exercises |  |
| `sec:51.14` | Solutions to exercises |  |
| `ex:51.1` | Sorting terms between the common terms agreement and the facility agreements |  |
| `ex:51.2` | A cost-to-complete test on a drawdown request |  |
| `ex:51.3` | An incurrence test for additional senior debt |  |
| `ex:51.4` | Testing a distribution request |  |
| `ex:51.5` | Equity cure arithmetic |  |
| `ex:51.6` | Voting arithmetic in a seven-bank club |  |
| `exh:51.1` | The project finance document set (diagram) |  |
| `exh:51.2` | Finance documents: parties, governing law, purpose and drafter |  |
| `exh:51.3` | Chassis, adapted and bespoke clauses in a common terms agreement |  |
| `exh:51.4` | Initial conditions precedent checklist template |  |
| `exh:51.5` | Reporting calendar in construction and operations |  |
| `exh:51.6` | Event of default severity grid, twelve events of default |  |
| `exh:51.7` | Reading order for a common terms agreement |  |
| `exh:51.8` | Case P common terms agreement covenant and cure terms |  |
| `cl:51.1` | Clear market undertaking, mandate letter |  |
| `cl:51.2` | Conditions to each utilisation in construction, common terms agreement |  |
| `cl:51.3` | Information and projections representation, common terms agreement |  |
| `cl:51.4` | Historic DSCR and supporting definitions, common terms agreement |  |
| `cl:51.5` | Material project document event of default, common terms agreement |  |
| `cl:51.6` | Equity cure, common terms agreement |  |
| `eq:51.1` | Maximum additional senior debt under an incurrence test |  |
| `eq:51.2` | CFADS cure amount |  |
| `eq:51.3` | Prepayment cure amount, pro rata application |  |
| `fw:boilerplate-or-bargain` | Framework 51.1 Boilerplate-or-bargain sort | home ssec:51.1.5 |
| `fw:eod-severity-grid` | Framework 51.2 Event of default severity grid | home ssec:51.5.2 |

### Chapter 52: Security, accounts and the cash waterfall

Source brief: `briefs/u11.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:52` | Security, accounts and the cash waterfall |  |
| `sec:52.1` | What security is for in project finance |  |
| `ssec:52.1.1` | Control, protection and leverage |  |
| `ssec:52.1.2` | The security package |  |
| `sec:52.2` | Common-law and civil-law security |  |
| `ssec:52.2.1` | Charges and the security trust in common law |  |
| `ssec:52.2.2` | Pledges, the accessory principle and parallel debt in civil law |  |
| `ssec:52.2.3` | Security agents, security trustees and statutory regimes |  |
| `sec:52.3` | Perfection and priority |  |
| `ssec:52.3.1` | Perfecting security |  |
| `ssec:52.3.2` | What security does not beat |  |
| `sec:52.4` | Enforcement as a going concern |  |
| `ssec:52.4.1` | The enforcement routes |  |
| `ssec:52.4.2` | What constrains enforcement |  |
| `sec:52.5` | The accounts structure |  |
| `ssec:52.5.1` | The accounts and what each is for |  |
| `ssec:52.5.2` | Who controls the accounts |  |
| `ssec:52.5.3` | Construction-phase flows |  |
| `sec:52.6` | The cash waterfall in full |  |
| `ssec:52.6.1` | The order of payments and why each step sits where it does |  |
| `ssec:52.6.2` | One period through the waterfall |  |
| `ssec:52.6.3` | Special flows |  |
| `ssec:52.6.4` | Drafting the priority of payments |  |
| `sec:52.7` | Walkthrough: tracing a dollar through an accounts agreement |  |
| `sec:52.8` | Case P: the accounts agreement, parallel debt and the business pledge |  |
| `sec:52.9` | Practitioner's notebook |  |
| `sec:52.10` | Judgment drill |  |
| `sec:52.11` | Security binds the project company; it does not settle the lenders' disputes with each other |  |
| `sec:52.12` | Exercises |  |
| `sec:52.13` | Solutions to exercises |  |
| `ex:52.1` | Going-concern versus liquidation recovery |  |
| `ex:52.2` | Parallel debt and the distribution of enforcement proceeds |  |
| `ex:52.3` | One semiannual period through the waterfall |  |
| `ex:52.4` | Insurance proceeds and the reinstatement test |  |
| `exh:52.1` | The security package by asset class |  |
| `exh:52.2` | Perfection checklist by asset class |  |
| `exh:52.3` | Enforcement routes compared |  |
| `exh:52.4` | Account map of an operating project (diagram) |  |
| `exh:52.5` | Operating cash waterfall (diagram) |  |
| `exh:52.6` | Tracing a dollar through the accounts agreement |  |
| `exh:52.7` | Case P accounts and flows |  |
| `cl:52.1` | Parallel debt undertaking, intercreditor agreement |  |
| `cl:52.2` | Priority of payments, accounts agreement |  |
| `eq:52.1` | Pro rata distribution of net enforcement proceeds |  |
| `fw:security-control-test` | Framework 52.1 Security package control test | home ssec:52.1.2 |
| `fw:trace-a-dollar` | Framework 52.2 Trace-a-dollar test | home sec:52.7 |

### Chapter 53: Intercreditor arrangements

Source brief: `briefs/u11.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:53` | Intercreditor arrangements |  |
| `sec:53.1` | Why lenders need an agreement among themselves |  |
| `sec:53.2` | Ranking, sharing and turnover |  |
| `ssec:53.2.1` | Pari passu ranking and pro rata sharing |  |
| `ssec:53.2.2` | Subordinated, mezzanine and shareholder debt |  |
| `sec:53.3` | Voting and decision-making |  |
| `ssec:53.3.1` | Who votes and how votes are counted |  |
| `ssec:53.3.2` | Entrenched rights and the decision matrix |  |
| `ssec:53.3.3` | Bondholders in an intercreditor agreement |  |
| `sec:53.4` | ECA and DFI rights |  |
| `ssec:53.4.1` | ECAs in the intercreditor agreement |  |
| `ssec:53.4.2` | DFIs in the intercreditor agreement |  |
| `sec:53.5` | Hedge counterparties |  |
| `ssec:53.5.1` | Ranking and voting of hedge claims |  |
| `ssec:53.5.2` | Hedges through prepayments and refinancings |  |
| `sec:53.6` | Standstills and the conduct of enforcement |  |
| `ssec:53.6.1` | Acceleration, enforcement instructions and standstills |  |
| `ssec:53.6.2` | Applying enforcement proceeds |  |
| `sec:53.7` | Adding creditors after financial close |  |
| `sec:53.8` | Conventional and Islamic tranches in one intercreditor agreement |  |
| `sec:53.9` | Walkthrough: building an intercreditor decision matrix |  |
| `sec:53.10` | Case P: the intercreditor agreement and the bondholders' accession |  |
| `sec:53.11` | Practitioner's notebook |  |
| `sec:53.12` | Judgment drill |  |
| `sec:53.13` | Lenders can agree among themselves; whether a state pays depends on the forum |  |
| `sec:53.14` | Exercises |  |
| `sec:53.15` | Solutions to exercises |  |
| `ex:53.1` | Sharing after one lender's set-off |  |
| `ex:53.2` | Mezzanine recovery under subordination |  |
| `ex:53.3` | One waiver vote under three counting rules |  |
| `ex:53.4` | Hedge claims pari passu or super senior |  |
| `ex:53.5` | Enforce now or wait |  |
| `ex:53.6` | Conventional and ijara facilities sharing enforcement proceeds |  |
| `exh:53.1` | What each creditor class wants after a default |  |
| `exh:53.2` | Intercreditor decision matrix for a four-tranche financing |  |
| `exh:53.3` | Case P creditor classes and voting mechanics |  |
| `cl:53.1` | Instructing group for waivers of financial covenant events of default, intercreditor agreement |  |
| `cl:53.2` | Application of enforcement proceeds, intercreditor agreement |  |
| `eq:53.1` | Pro rata sharing of a recovery |  |
| `eq:53.2` | Expected value of enforcement after a standstill |  |
| `fw:intercreditor-matrix` | Framework 53.1 Intercreditor decision matrix | home ssec:53.3.2 |

### Chapter 54: Governing law, disputes and investment protection

Source brief: `briefs/u11.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:54` | Governing law, disputes and investment protection |  |
| `sec:54.1` | Choosing governing law |  |
| `ssec:54.1.1` | What the parties can choose and what local law decides anyway |  |
| `ssec:54.1.2` | Governing law across the contract web |  |
| `sec:54.2` | Courts or arbitration |  |
| `ssec:54.2.1` | Litigation and jurisdiction clauses |  |
| `ssec:54.2.2` | Seat, rules and tribunal in arbitration |  |
| `ssec:54.2.3` | Multi-tier clauses and multi-contract disputes |  |
| `ssec:54.2.4` | Choosing the forum by working backwards from enforcement |  |
| `sec:54.3` | Enforcing awards |  |
| `ssec:54.3.1` | The New York Convention |  |
| `ssec:54.3.2` | The ICSID Convention |  |
| `ssec:54.3.3` | Annulment and set-aside risk |  |
| `sec:54.4` | Sovereign immunity and its waiver |  |
| `ssec:54.4.1` | Immunity from suit and immunity from execution |  |
| `ssec:54.4.2` | What the 2026 decisions changed |  |
| `ssec:54.4.3` | Drafting the waiver |  |
| `sec:54.5` | Stabilization and economic-equilibrium clauses |  |
| `ssec:54.5.1` | Freezing, equilibrium and hybrid clauses |  |
| `ssec:54.5.2` | Pricing a change in law |  |
| `ssec:54.5.3` | What Spain teaches about statute and contract |  |
| `sec:54.6` | Investment treaties |  |
| `ssec:54.6.1` | What treaties protect and whom |  |
| `ssec:54.6.2` | Defenses and how tribunals split |  |
| `ssec:54.6.3` | Structuring for treaty protection |  |
| `ssec:54.6.4` | Winning and collecting |  |
| `sec:54.7` | Walkthrough: drafting the dispute clauses for a project's contract set |  |
| `sec:54.8` | Case P: dispute clauses, treaty protection and the immunity waiver |  |
| `sec:54.9` | Practitioner's notebook |  |
| `sec:54.10` | Judgment drill |  |
| `sec:54.11` | Rights on paper become a financing only when the documents are signed and funded |  |
| `sec:54.12` | Exercises |  |
| `sec:54.13` | Solutions to exercises |  |
| `ex:54.1` | Expected recovery under three forums |  |
| `ex:54.2` | Award value with interest |  |
| `ex:54.3` | Pricing a change in law under an equilibrium clause |  |
| `ex:54.4` | Treaty timing and the sunset clause |  |
| `exh:54.1` | Governing law and forum across an illustrative contract web |  |
| `exh:54.2` | Arbitral institutions and rule sets compared |  |
| `exh:54.3` | Case P dispute map |  |
| `cl:54.1` | Waiver of immunity, implementation agreement |  |
| `cl:54.2` | Economic equilibrium clause, implementation agreement |  |
| `cl:54.3` | Arbitration agreement with ICSID consent and UNCITRAL fallback, implementation agreement |  |
| `eq:54.1` | Expected recovery of a claim in a forum |  |
| `eq:54.2` | Grossed-up tariff uplift for a revenue levy |  |
| `fw:enforcement-first-forum` | Framework 54.1 Enforcement-first forum choice | home ssec:54.2.4 |
| `fw:treaty-protection-test` | Framework 54.2 Treaty protection test | home ssec:54.6.3 |

### Chapter 55: Running a financing to close

Source brief: `briefs/u11.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:55` | Running a financing to close |  |
| `sec:55.1` | Choosing the financing strategy |  |
| `ssec:55.1.1` | Club, underwritten or best efforts |  |
| `ssec:55.1.2` | Bank, bond or both |  |
| `ssec:55.1.3` | Financing in a competitive tender |  |
| `sec:55.2` | Advisors and arrangers |  |
| `ssec:55.2.1` | The financial advisor |  |
| `ssec:55.2.2` | Arrangers, bookrunners and coordinating roles |  |
| `sec:55.3` | Information memorandum and lender presentation |  |
| `ssec:55.3.1` | What the information memorandum contains |  |
| `ssec:55.3.2` | Lender presentation, site visit and questions |  |
| `sec:55.4` | Credit approval inside a bank |  |
| `ssec:55.4.1` | From deal team to committee |  |
| `ssec:55.4.2` | What makes a committee say yes |  |
| `sec:55.5` | Syndication and sell-down |  |
| `ssec:55.5.1` | General syndication and allocation |  |
| `ssec:55.5.2` | Sub-underwriting, sell-down and the secondary market |  |
| `sec:55.6` | Managing the documentation |  |
| `ssec:55.6.1` | Who drafts what |  |
| `ssec:55.6.2` | Issues lists, versions and all-party meetings |  |
| `sec:55.7` | Satisfying conditions precedent |  |
| `ssec:55.7.1` | The CP tracker |  |
| `ssec:55.7.2` | Legal opinions, certificates and the last mile |  |
| `sec:55.8` | Signing, financial close and funds flow |  |
| `ssec:55.8.1` | Signing versus financial close |  |
| `ssec:55.8.2` | The closing memorandum and the funds flow |  |
| `sec:55.9` | Timelines and critical paths |  |
| `ssec:55.9.1` | Building the timetable |  |
| `ssec:55.9.2` | What delay costs |  |
| `sec:55.10` | Walkthrough: the last 72 hours before financial close |  |
| `sec:55.11` | Case P: financial close on July 17, 2018 |  |
| `sec:55.12` | Practitioner's notebook |  |
| `sec:55.13` | Judgment drill |  |
| `sec:55.14` | Every closed term was negotiated somewhere |  |
| `sec:55.15` | Exercises |  |
| `sec:55.16` | Solutions to exercises |  |
| `ex:55.1` | Underwriting economics |  |
| `ex:55.2` | Allocating an oversubscribed syndication |  |
| `ex:55.3` | A closing-day funds flow |  |
| `ex:55.4` | Critical path to close |  |
| `ex:55.5` | The cost of an eight-week slip |  |
| `exh:55.1` | Financing strategy selector applied to four projects |  |
| `exh:55.2` | Arranging and agency roles and how each is paid |  |
| `exh:55.3` | Information memorandum contents and what lenders read first |  |
| `exh:55.4` | The credit approval path inside a bank |  |
| `exh:55.5` | Drafting responsibility matrix |  |
| `exh:55.6` | Funds flow memorandum format |  |
| `exh:55.7` | Critical path to close (Gantt chart) |  |
| `exh:55.8` | Closing call script and checklist |  |
| `exh:55.9` | Case P sources and uses at financial close |  |
| `exh:55.10` | Case P closing-day funds flow (conditional on P-F37) |  |
| `exh:55.11` | Case P timeline from mandate to financial close |  |
| `cl:55.1` | CP satisfaction notice, common terms agreement schedule (single clause with annotations; used as the model answer format for Exercise 55.11) |  |
| `eq:55.1` | Arranger's retained fees under an underwriting |  |
| `eq:55.2` | Float of a task on the critical path |  |
| `fw:financing-strategy-selector` | Framework 55.1 Financing strategy selector | home ssec:55.1.2 |
| `fw:critical-path-to-close` | Framework 55.2 Critical path to close | home ssec:55.9.1 |

### Chapter 56: Negotiating project finance

Source brief: `briefs/u11.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:56` | Negotiating project finance |  |
| `sec:56.1` | What market means and why it moves |  |
| `ssec:56.1.1` | The evidence for a market term |  |
| `ssec:56.1.2` | Why norms differ by sector, region and contract quality |  |
| `sec:56.2` | The levers each side holds |  |
| `sec:56.3` | Converting terms into money |  |
| `ssec:56.3.1` | A common currency for trades |  |
| `ssec:56.3.2` | Small terms with large prices |  |
| `sec:56.4` | The trade-offs on each key term |  |
| `ssec:56.4.1` | Debt size, tenor and profile |  |
| `ssec:56.4.2` | Pricing, fees and flex |  |
| `ssec:56.4.3` | Hedging, reserves, sweeps and lock-ups |  |
| `ssec:56.4.4` | Covenants, events of default, CPs and sponsor support |  |
| `ssec:56.4.5` | The trade-off ledger |  |
| `sec:56.5` | Tactics, sequencing and escalation |  |
| `ssec:56.5.1` | Alternatives, reservation points and the zone of agreement |  |
| `ssec:56.5.2` | Anchors, packages and concession patterns |  |
| `ssec:56.5.3` | Sequencing and the issues list |  |
| `ssec:56.5.4` | Escalation and deadlock |  |
| `sec:56.6` | How terms move with the market cycle |  |
| `sec:56.7` | Negotiating with governments, contractors and offtakers |  |
| `ssec:56.7.1` | Governments |  |
| `ssec:56.7.2` | Contractors |  |
| `ssec:56.7.3` | Offtakers |  |
| `sec:56.8` | Walkthrough: marking up a term sheet |  |
| `sec:56.9` | Case P: the term sheet negotiation, July to October 2017 |  |
| `sec:56.10` | Practitioner's notebook |  |
| `sec:56.11` | Judgment drill |  |
| `sec:56.12` | When the counterparty is the state, the negotiation starts with the public case |  |
| `sec:56.13` | Exercises |  |
| `sec:56.14` | Solutions to exercises |  |
| `ex:56.1` | A 0.05x DSCR change in debt, equity IRR and tariff |  |
| `ex:56.2` | The present value of a swap execution charge |  |
| `ex:56.3` | The lock-up level and the chance of trapped cash |  |
| `ex:56.4` | Ranking concessions with a trade-off ledger |  |
| `ex:56.5` | The zone of agreement on a margin |  |
| `exh:56.1` | US project finance DSCR and spread ranges, 2024 to 2026 |  |
| `exh:56.2` | Negotiating levers by party |  |
| `exh:56.3` | Key terms: what each side asks for and how they trade |  |
| `exh:56.4` | Term sheet markup: draft, markup, response and landing |  |
| `exh:56.5` | Case P senior debt at alternative DSCR targets and gearing caps |  |
| `eq:56.1` | Probability that a DSCR test falls below a lock-up level |  |
| `eq:56.2` | Zone of possible agreement on a margin |  |
| `fw:market-check` | Framework 56.1 Market check | home ssec:56.1.1 |
| `fw:trade-off-ledger` | Framework 56.2 Trade-off ledger | home ssec:56.4.5 |
| `fw:escalation-ladder` | Framework 56.3 Escalation ladder | home ssec:56.5.4 |

### Chapter 57: The public-sector case for PPPs

Source brief: `briefs/u12.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:57` | The public-sector case for PPPs |  |
| `sec:57.1` | What a government buys with a PPP |  |
| `ssec:57.1.1` | Whole-life cost, risk transfer and private due diligence |  |
| `ssec:57.1.2` | The financing premium |  |
| `ssec:57.1.3` | The critiques at full strength |  |
| `ssec:57.1.4` | When PPP is the right tool |  |
| `sec:57.2` | Value for money and the public sector comparator |  |
| `ssec:57.2.1` | What value for money means |  |
| `ssec:57.2.2` | Building the comparator |  |
| `ssec:57.2.3` | Pricing risk as an expected value |  |
| `ssec:57.2.4` | The discount rate decides more than it should |  |
| `ssec:57.2.5` | The value-for-money flip test |  |
| `ssec:57.2.6` | Gaming, timing and the limits of the number |  |
| `sec:57.3` | Affordability |  |
| `ssec:57.3.1` | Affordable is a different question from good value |  |
| `ssec:57.3.2` | Budget envelopes and program ceilings |  |
| `ssec:57.3.3` | Affordability when users pay |  |
| `sec:57.4` | Fiscal and statistical treatment |  |
| `ssec:57.4.1` | Why the accounting treatment drives the choice |  |
| `ssec:57.4.2` | The classification tests |  |
| `ssec:57.4.3` | Designing for the accounts versus designing for value |  |
| `sec:57.5` | Contingent liabilities |  |
| `ssec:57.5.1` | What the state still owes after signing |  |
| `ssec:57.5.2` | Measuring them |  |
| `ssec:57.5.3` | Managing them |  |
| `ssec:57.5.4` | Metronet and the guarantee that took the risk back |  |
| `sec:57.6` | PPP units and programs |  |
| `ssec:57.6.1` | What a PPP unit does |  |
| `ssec:57.6.2` | Programs rather than deals |  |
| `ssec:57.6.3` | Managing contracts for 30 years |  |
| `sec:57.7` | Unsolicited proposals |  |
| `ssec:57.7.1` | Why governments receive them and what can go wrong |  |
| `ssec:57.7.2` | Three ways to introduce competition |  |
| `ssec:57.7.3` | Paying for ideas without paying for influence |  |
| `sec:57.8` | The UK PFI and the price of buying risk transfer with private capital |  |
| `ssec:57.8.1` | From Ryrie Rules to more than 700 projects |  |
| `ssec:57.8.2` | PF2 reforms that changed little |  |
| `ssec:57.8.3` | The 2018 decision and the unfinished business |  |
| `sec:57.9` | Walkthrough: reading a value-for-money report |  |
| `sec:57.10` | Case T: Brannock decides to procure the Merrick Link |  |
| `sec:57.11` | Practitioner's notebook |  |
| `sec:57.12` | Judgment drill |  |
| `sec:57.13` | A positive value-for-money test is a promise the procurement must keep |  |
| `sec:57.14` | Exercises |  |
| `sec:57.15` | Solutions to exercises |  |
| `ex:57.1` | The financing premium on a hospital availability charge (Illustrative) |  |
| `ex:57.2` | Building a public sector comparator for a justice center (Illustrative) |  |
| `ex:57.3` | Pricing construction risk as an expected value (Illustrative) |  |
| `ex:57.4` | Testing a program against an affordability ceiling (Illustrative) |  |
| `ex:57.5` | Valuing a minimum revenue guarantee and a debt guarantee (Illustrative) |  |
| `ex:57.6` | An unsolicited proposal under a Swiss challenge and a bonus system (Illustrative) |  |
| `ex:57.7` | What the NAO's PF2 numbers say about the financing premium (Real case: UK PFI and PF2, 1992–2018) |  |
| `ex:57.8` | Paying for risk transfer the guarantee took back (Real case: Metronet, 2003–2009) |  |
| `exh:57.1` | Who carries each risk under conventional procurement, design-build and DBFOM (Illustrative) |  |
| `exh:57.2` | Public sector comparator and PPP cost build for the justice center (CAD m, PV at 6.0%) (Illustrative) |  |
| `exh:57.3` | Value for money against the discount rate (CAD m) (Illustrative) |  |
| `exh:57.4` | Design choices that move statistical classification and what each costs (Illustrative) |  |
| `exh:57.5` | Contingent liabilities a PPP leaves with the state: trigger and measure (Illustrative) |  |
| `exh:57.6` | Three regimes for unsolicited proposals compared (Illustrative) |  |
| `exh:57.7` | The UK PFI and PF2, 1989–2048 (Real case: UK PFI and PF2, 1989–2048) |  |
| `exh:57.8` | Brannock public sector comparator and value for money for the reference project (ARD m, PV 2012) (Case T) |  |
| `exh:57.9` | Brannock's decision to procure, 2012 (Case T) |  |
| `eq:57.1` | VfM = PSC − PPP risk-adjusted present cost |  |
| `eq:57.2` | PSC = raw cost + competitive neutrality + transferable risk + retained risk |  |
| `eq:57.3` | Expected guarantee payout: E[max(0, G − R_t)] = Σ p_s max(0, G − R_s) |  |
| `fw:vfm-flip` | Framework 57.1 Value-for-money flip test | home ssec:57.2.5 |
| `fw:ppp-gateway` | Framework 57.2 PPP decision gateway | home sec:57.6 |

### Chapter 58: Procuring and designing PPPs

Source brief: `briefs/u12.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:58` | Procuring and designing PPPs |  |
| `sec:58.1` | Choosing the delivery model |  |
| `ssec:58.1.1` | The family of models and what each transfers |  |
| `ssec:58.1.2` | Availability payments or user charges |  |
| `ssec:58.1.3` | Hybrids that share demand risk |  |
| `ssec:58.1.4` | Term and asset life |  |
| `sec:58.2` | Running the procurement |  |
| `ssec:58.2.1` | The stages from market sounding to financial close |  |
| `ssec:58.2.2` | Competitive dialogue and what must stay fixed |  |
| `ssec:58.2.3` | Bid security, committed finance and funding competitions |  |
| `ssec:58.2.4` | Designing the evaluation |  |
| `ssec:58.2.5` | From preferred bidder to financial close |  |
| `sec:58.3` | Payment mechanisms and deduction regimes |  |
| `ssec:58.3.1` | The unitary charge |  |
| `ssec:58.3.2` | Availability deductions |  |
| `ssec:58.3.3` | Performance deductions |  |
| `ssec:58.3.4` | Calibrating deductions against the debt |  |
| `ssec:58.3.5` | Performance regimes when users pay |  |
| `sec:58.4` | Change, benchmarking and market testing |  |
| `ssec:58.4.1` | Change protocols |  |
| `ssec:58.4.2` | Benchmarking and market testing of soft services |  |
| `ssec:58.4.3` | Relief events and compensation events |  |
| `sec:58.5` | Termination regimes and compensation formulas |  |
| `ssec:58.5.1` | The grounds and the logic of compensating each |  |
| `ssec:58.5.2` | The formulas |  |
| `ssec:58.5.3` | Keeping the formula honest after a refinancing |  |
| `ssec:58.5.4` | The extended-delay exit |  |
| `sec:58.6` | Refinancing gain sharing |  |
| `ssec:58.6.1` | Where refinancing gains come from and why the public sector claims them |  |
| `ssec:58.6.2` | Calculating the gain and taking the share |  |
| `sec:58.7` | Handback |  |
| `ssec:58.7.1` | Handback requirements |  |
| `ssec:58.7.2` | Securing handback |  |
| `sec:58.8` | Sharing risks no one can price |  |
| `ssec:58.8.1` | Risk bands and caps |  |
| `ssec:58.8.2` | The Port of Miami Tunnel geotechnical band |  |
| `sec:58.9` | Standard contracts and program documents |  |
| `ssec:58.9.1` | Why standardize and what to leave open |  |
| `ssec:58.9.2` | The main families of guidance |  |
| `sec:58.10` | Lessons from PPP successes and failures |  |
| `ssec:58.10.1` | The PPP design failure map |  |
| `ssec:58.10.2` | What the successes have in common |  |
| `sec:58.11` | Walkthrough: the payment mechanism schedule, clause by clause |  |
| `sec:58.12` | Walkthrough: evaluating a best and final offer |  |
| `sec:58.13` | Case T: from shortlist to financial close |  |
| `sec:58.14` | Practitioner's notebook |  |
| `sec:58.15` | Judgment drill |  |
| `sec:58.16` | The contract shifts risk on paper, and the next part tests it against a weaker state |  |
| `sec:58.17` | Exercises |  |
| `sec:58.18` | Solutions to exercises |  |
| `ex:58.1` | Scoring three bids under two price formulas (Illustrative) |  |
| `ex:58.2` | Letting traffic set the concession term (Illustrative) |  |
| `ex:58.3` | One month of deductions at a 230-bed hospital (Illustrative) |  |
| `ex:58.4` | How much deduction the debt can absorb (Illustrative) |  |
| `ex:58.5` | Pricing a capital change (Illustrative) |  |
| `ex:58.6` | Benchmarking a cleaning service (Illustrative) |  |
| `ex:58.7` | Termination compensation under four grounds (Illustrative) |  |
| `ex:58.8` | Calculating and sharing a refinancing gain (Illustrative) |  |
| `ex:58.9` | The Norfolk and Norwich refinancing (Real case: Norfolk and Norwich hospital, 1998–2006) |  |
| `ex:58.10` | Sharing geotechnical risk in a band (Real case: Port of Miami Tunnel, 2009–2014) |  |
| `ex:58.11` | Sizing handback security (Illustrative) |  |
| `ex:58.12` | The 365-day exit (Real case: Maryland Purple Line, 2016–2022) |  |
| `exh:58.1` | Delivery models and the risks each transfers (Illustrative) |  |
| `exh:58.2` | Choosing availability payments or user charges (Illustrative) |  |
| `exh:58.3` | Procurement stages with Case T's dates, 2012–2015 (Case T) |  |
| `exh:58.4` | Bid scores under two price formulas (Illustrative) |  |
| `exh:58.5` | Payment flows under an availability PPP (Illustrative) |  |
| `exh:58.6` | One month's deductions at the hospital (GBP) (Illustrative) |  |
| `exh:58.7` | Termination compensation by ground (EUR m) (Illustrative) |  |
| `exh:58.8` | Refinancing gain sharing in UK PFI contracts, 1995–2016 (Real case: UK PFI, 1995–2016) |  |
| `exh:58.9` | The Port of Miami Tunnel geotechnical band with illustrative overruns (USD m) (Real case: Port of Miami Tunnel, 2009–2014) |  |
| `exh:58.10` | Merrick Link termination compensation regime (Case T) |  |
| `exh:58.11` | Merrick Link sources and uses at financial close (ARD m) (Case T) |  |
| `exh:58.12` | PPP design failure map (Illustrative) |  |
| `cl:58.1` | Availability deduction, project agreement (Illustrative) |  |
| `cl:58.2` | Compensation on contractor default, project agreement (variants) |  |
| `cl:58.2a` | Compensation on contractor default, project agreement (Illustrative, sponsor-friendly) |  |
| `cl:58.2b` | Compensation on contractor default, project agreement (Illustrative, lender-friendly) |  |
| `cl:58.2c` | Compensation on contractor default, project agreement (Illustrative, government-friendly) |  |
| `cl:58.3` | Refinancing gain share, project agreement (Illustrative) |  |
| `cl:58.4` | Handback requirements and retention, project agreement (Illustrative) |  |
| `eq:58.1` | LPVR term condition: smallest T with Σ_{t≤T} Rev_t / (1+r)^t ≥ LPVR |  |
| `eq:58.2` | Availability deduction = monthly UC × area weight × units share × days share × multiplier |  |
| `eq:58.3` | Termination compensation by ground (authority default; force majeure; contractor default) |  |
| `eq:58.4` | Refinancing gain = PV(post-refinancing distributions) − PV(pre-refinancing distributions) at the base-case equity IRR |  |
| `fw:deduction-calibration` | Framework 58.1 Deduction calibration test | home ssec:58.3.4 |
| `fw:ppp-failure-map` | Framework 58.2 PPP design failure map | home ssec:58.10.1 |

### Chapter 59: Country, currency and payment risk

Source brief: `briefs/u12.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:59` | Country, currency and payment risk |  |
| `sec:59.1` | Country risk and sovereign risk |  |
| `ssec:59.1.1` | Four risks that travel together |  |
| `ssec:59.1.2` | Reading a country |  |
| `ssec:59.1.3` | The country risk scorecard |  |
| `ssec:59.1.4` | How country risk shapes the deal |  |
| `sec:59.2` | Currency risk taken apart |  |
| `ssec:59.2.1` | Devaluation, convertibility and transfer |  |
| `ssec:59.2.2` | Finding the mismatch |  |
| `ssec:59.2.3` | Stressing a project for devaluation |  |
| `ssec:59.2.4` | Where the risk lands when the currency falls |  |
| `sec:59.3` | Solutions to currency risk |  |
| `ssec:59.3.1` | Hard-currency revenue and indexed tariffs |  |
| `ssec:59.3.2` | Local-currency debt and FX liquidity facilities |  |
| `ssec:59.3.3` | Convertibility and transfer undertakings |  |
| `ssec:59.3.4` | Offshore accounts |  |
| `ssec:59.3.5` | Sizing debt for a devaluation |  |
| `sec:59.4` | Payment risk from weak offtakers |  |
| `ssec:59.4.1` | How a state utility runs out of cash |  |
| `ssec:59.4.2` | Liquidity, credit and termination |  |
| `sec:59.5` | Payment security instruments |  |
| `ssec:59.5.1` | Standby letters of credit |  |
| `ssec:59.5.2` | Escrow and receivables accounts |  |
| `ssec:59.5.3` | Government guarantees as a payment backstop |  |
| `ssec:59.5.4` | Liquidity facilities and partial risk guarantees behind the LC |  |
| `ssec:59.5.5` | Netting, set-off and fuel-supply links |  |
| `ssec:59.5.6` | Sizing the stack in months of runway |  |
| `sec:59.6` | Dabhol and the guarantee chain that rested on one fiscal capacity |  |
| `sec:59.7` | Paiton and the exchange-rate-indexed tariff in a crisis |  |
| `sec:59.8` | Argentina 2002 and the indexation that was legislated away |  |
| `sec:59.9` | Walkthrough: following one SEKA invoice from issue to the offshore debt service account |  |
| `sec:59.10` | Case P: arrears, the FX queue and the settlement, 2022 to 2024 |  |
| `sec:59.11` | Practitioner's notebook |  |
| `sec:59.12` | Judgment drill |  |
| `sec:59.13` | Contracts can move currency and credit risk, but only a state can take political risk away |  |
| `sec:59.14` | Exercises |  |
| `sec:59.15` | Solutions to exercises |  |
| `ex:59.1` | Scoring two countries (Illustrative) |  |
| `ex:59.2` | Devaluation stress on a local-currency wind tariff (Illustrative) |  |
| `ex:59.3` | The cost of a conversion lag (Illustrative) |  |
| `ex:59.4` | Sizing a standby LC and counting the months of runway (Illustrative) |  |
| `ex:59.5` | PLN's May 1999 payment (Real case: Paiton I, 1994–2003) |  |
| `ex:59.6` | Pesification arithmetic (Real case: Argentina, 2002) |  |
| `ex:59.7` | Azura-Edo's three layers (Real case: Azura-Edo, 2013–2024) |  |
| `ex:59.8` | Tracing a gas netting set-off (Case P) |  |
| `exh:59.1` | Country risk scorecard for two countries (Illustrative) |  |
| `exh:59.2` | Three currency risks and the instruments that answer them (Illustrative) |  |
| `exh:59.3` | DSCR under devaluation and indexation (USD m) (Illustrative) |  |
| `exh:59.4` | The payment security stack (Illustrative) |  |
| `exh:59.5` | Choosing payment security (Illustrative) |  |
| `exh:59.6` | Bélanou Power's onshore and offshore accounts (Case P) |  |
| `exh:59.7` | Kessara macro indicators and sovereign rating, 2015–2025 (Case P) |  |
| `exh:59.8` | SEKA overdue receivables, 2021–2025 (USD m) (Case P) |  |
| `exh:59.9` | The payment crisis, November 2022 to March 2024 (Case P) |  |
| `exh:59.10` | Arrears, cash DSCR, DSRA and FX losses, 2022 H1 to 2025 H1 (Case P) |  |
| `exh:59.11` | Termination compensation at June 30, 2023 by ground (USD m) (Case P) |  |
| `cl:59.1` | LC replenishment and cure, PPA (variants) |  |
| `cl:59.1a` | LC replenishment and cure, PPA (Illustrative, sponsor-friendly) |  |
| `cl:59.1b` | LC replenishment and cure, PPA (Illustrative, lender-friendly) |  |
| `cl:59.1c` | LC replenishment and cure, PPA (Illustrative, offtaker-friendly) |  |
| `cl:59.2` | Convertibility and transfer undertaking, implementation agreement (Illustrative) |  |
| `cl:59.3` | Conversion and offshore sweep, accounts agreement (Illustrative) |  |
| `eq:59.1` | USD revenue under partial indexation: Rev_USD = E × tariff_0 × (1 + k × d) / (FX_0 × (1 + d)) |  |
| `eq:59.2` | LC size = a × monthly capacity charge + b × monthly energy charge |  |
| `eq:59.3` | Months of runway = (LC + DSRA + free cash) / monthly needs with zero receipts |  |
| `eq:59.4` | Conversion-lag loss = invoice × (1 − 1/(1 + δ)^(lag/30.4)) |  |
| `fw:country-scorecard` | Framework 59.1 Country risk scorecard | home ssec:59.1.3 |
| `fw:payment-stack` | Framework 59.2 Payment security stack | home ssec:59.4.2 |

### Chapter 60: Political risk and its protection

Source brief: `briefs/u12.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:60` | Political risk and its protection |  |
| `sec:60.1` | What political risk is and how it arrives |  |
| `ssec:60.1.1` | The perils, named precisely |  |
| `ssec:60.1.2` | Sudden events and creeping pressure |  |
| `ssec:60.1.3` | When the risk comes from home |  |
| `sec:60.2` | The obsolescing bargain |  |
| `ssec:60.2.1` | Why bargaining power moves to the host after construction |  |
| `ssec:60.2.2` | The record |  |
| `ssec:60.2.3` | Structuring against it |  |
| `sec:60.3` | Host-government relations and local content |  |
| `ssec:60.3.1` | Mapping the state |  |
| `ssec:60.3.2` | The local partner |  |
| `ssec:60.3.3` | Local content |  |
| `sec:60.4` | Political risk insurance |  |
| `ssec:60.4.1` | Who sells it |  |
| `ssec:60.4.2` | What each cover pays for and when |  |
| `ssec:60.4.3` | Pricing and the economics of buying cover |  |
| `ssec:60.4.4` | How a claim works |  |
| `ssec:60.4.5` | PRI, ECA cover and DFI guarantees compared |  |
| `sec:60.5` | The multilateral halo |  |
| `ssec:60.5.1` | What deters a host |  |
| `ssec:60.5.2` | Where the halo fails |  |
| `sec:60.6` | Corruption risk and anti-bribery law |  |
| `ssec:60.6.1` | Why bribery is a credit risk |  |
| `ssec:60.6.2` | The FCPA and the UK Bribery Act |  |
| `ssec:60.6.3` | Intermediaries, agents and local partners |  |
| `sec:60.7` | Sanctions |  |
| `ssec:60.7.1` | How sanctions regimes reach a project |  |
| `ssec:60.7.2` | Nord Stream 2 and Arctic LNG 2 |  |
| `ssec:60.7.3` | Contract tools |  |
| `sec:60.8` | Disputes and treaty claims in practice |  |
| `ssec:60.8.1` | From dispute to cash |  |
| `ssec:60.8.2` | The economics of a claim |  |
| `ssec:60.8.3` | Arbitration as leverage and the negotiated exit |  |
| `sec:60.9` | Walkthrough: reading a political risk insurance policy |  |
| `sec:60.10` | Case P: buying cover in 2018 and deciding not to claim in 2023 |  |
| `sec:60.11` | Practitioner's notebook |  |
| `sec:60.12` | Judgment drill |  |
| `sec:60.13` | Protection is bought before close and tested on a construction site |  |
| `sec:60.14` | Exercises |  |
| `sec:60.15` | Solutions to exercises |  |
| `ex:60.1` | How much a host can take after the plant is built (Illustrative) |  |
| `ex:60.2` | What PRI costs and what it saves (Illustrative) |  |
| `ex:60.3` | The loss probability a PRI premium implies (Illustrative) |  |
| `ex:60.4` | Screening an intermediary (Illustrative) |  |
| `ex:60.5` | Applying the 50 percent rule (Illustrative) |  |
| `ex:60.6` | The expected value of a treaty claim (Illustrative) |  |
| `ex:60.7` | Hub Power's 2000 settlement (Real case: Hub Power, 1998–2000) |  |
| `ex:60.8` | When creeping pressure misses the policy trigger (Real case: Oyu Tolgoi, 2009–2023) |  |
| `exh:60.1` | Political risk instrument map (Illustrative) |  |
| `exh:60.2` | Who bears each slice of a tariff cut after construction (USD m) (Illustrative) |  |
| `exh:60.3` | MIGA covers and what triggers each (Real case: MIGA products, 2026) |  |
| `exh:60.4` | PRI, ECA cover and DFI guarantees compared (Illustrative) |  |
| `exh:60.5` | The sequence of a political risk insurance claim (Illustrative) |  |
| `exh:60.6` | Sanctions and two Russian gas projects, 2022–2026 (Real case: Nord Stream 2 and Arctic LNG 2, 2022–2026) |  |
| `exh:60.7` | Expected value of a treaty claim (USD m) (Illustrative) |  |
| `exh:60.8` | Bélanou's political risk protection at financial close (Case P) |  |
| `exh:60.9` | Crisis events against PRI waiting periods, 2022–2024 (Case P) |  |
| `cl:60.1` | Anti-corruption representation and covenant, facility agreement (Illustrative) |  |
| `cl:60.2` | Local content undertaking, implementation agreement (variants) |  |
| `cl:60.2a` | Local content undertaking, implementation agreement (Illustrative, sponsor-friendly) |  |
| `cl:60.2b` | Local content undertaking, implementation agreement (Illustrative, lender-friendly) |  |
| `cl:60.2c` | Local content undertaking, implementation agreement (Illustrative, government-friendly) |  |
| `cl:60.3` | Sanctions covenant, facility agreement (Illustrative) |  |
| `eq:60.1` | Extractable revenue share before shutdown = (Rev − Opex) / Rev |  |
| `eq:60.2` | Implied annual loss probability = premium rate / loss given claim |  |
| `eq:60.3` | Expected PV of a claim = C × p_win × a × (1 − p_annul) × p_collect / (1 + r)^n − PV(costs) |  |
| `fw:pr-instrument-map` | Framework 60.1 Political risk instrument map | home ssec:60.1.1 |
| `fw:bargain-clock` | Framework 60.2 Obsolescing bargain clock | home ssec:60.2.3 |

### Chapter 61: Construction to completion

Source brief: `briefs/u13.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:61` | Construction to completion |  |
| `sec:61.1` | The construction period from the lenders' side |  |
| `ssec:61.1.1` | What changes at financial close |  |
| `ssec:61.1.2` | The monitoring team and who pays for it |  |
| `ssec:61.1.3` | Information covenants during construction |  |
| `sec:61.2` | Drawdowns and certification |  |
| `ssec:61.2.1` | The drawdown cycle |  |
| `ssec:61.2.2` | Conditions to each drawdown |  |
| `ssec:61.2.3` | The cost-to-complete test |  |
| `ssec:61.2.4` | Partial and withheld certification |  |
| `sec:61.3` | Managing contingency |  |
| `ssec:61.3.1` | Whose contingency it is |  |
| `ssec:61.3.2` | Testing contingency adequacy |  |
| `ssec:61.3.3` | When contingency runs out |  |
| `sec:61.4` | Monitoring progress and reading the warning signs |  |
| `ssec:61.4.1` | Schedule, critical path and float |  |
| `ssec:61.4.2` | Earned value for lenders |  |
| `ssec:61.4.3` | Red flags in monthly reports |  |
| `sec:61.5` | Change orders and claims in practice |  |
| `ssec:61.5.1` | Variations through the finance documents |  |
| `ssec:61.5.2` | Claims management |  |
| `ssec:61.5.3` | Aligning relief across contracts |  |
| `sec:61.6` | Delays and the flow of liquidated damages |  |
| `ssec:61.6.1` | Counting delay |  |
| `ssec:61.6.2` | Where LDs go |  |
| `ssec:61.6.3` | The delay cash bridge |  |
| `sec:61.7` | Insurance claims during construction |  |
| `ssec:61.7.1` | From incident to proceeds |  |
| `ssec:61.7.2` | Proving a DSU loss |  |
| `ssec:61.7.3` | Subrogation inside the contractual web |  |
| `sec:61.8` | Contractor distress and replacement |  |
| `ssec:61.8.1` | Early signs of contractor distress |  |
| `ssec:61.8.2` | The toolkit |  |
| `ssec:61.8.3` | Pricing a replacement contractor |  |
| `sec:61.9` | Carillion's hospitals and the loss of a contractor mid-build |  |
| `sec:61.10` | Purple Line and Vogtle when a contractor walks away |  |
| `sec:61.11` | Completion tests |  |
| `ssec:61.11.1` | Three completions |  |
| `ssec:61.11.2` | What a lenders' completion test contains |  |
| `ssec:61.11.3` | Performance shortfalls and buy-down LDs |  |
| `ssec:61.11.4` | Ichthys LNG and the 90-day completion test |  |
| `sec:61.12` | Releasing sponsor support |  |
| `ssec:61.12.1` | What falls away at completion |  |
| `ssec:61.12.2` | When completion does not come |  |
| `sec:61.13` | Walkthrough: an independent engineer's monthly report and drawdown certificate |  |
| `sec:61.14` | Walkthrough: the lenders' completion package |  |
| `sec:61.15` | Case P: from notice to proceed to commercial operation |  |
| `ssec:61.15.1` | Drawdowns and the failed foundation, 2018 to 2019 |  |
| `ssec:61.15.2` | COVID-19 force majeure and the variation order, 2020 |  |
| `ssec:61.15.3` | The transformer surge and the insurance claim, 2021 |  |
| `ssec:61.15.4` | Funding the overrun |  |
| `ssec:61.15.5` | Completion tests and the performance LD prepayment |  |
| `sec:61.16` | Practitioner's notebook |  |
| `sec:61.17` | Judgment drill |  |
| `sec:61.18` | Completion hands the lenders an operating credit they now have to watch |  |
| `sec:61.19` | Exercises |  |
| `sec:61.20` | Solutions to exercises |  |
| `ex:61.1` | Running the cost-to-complete test on a solar drawdown |  |
| `ex:61.2` | Testing contingency against open risks |  |
| `ex:61.3` | Earned value on a desalination EPC |  |
| `ex:61.4` | The delay cash bridge on a run-of-river hydro plant |  |
| `ex:61.5` | Pricing a replacement contractor |  |
| `ex:61.6` | A performance shortfall and the buy-down that does not quite buy down |  |
| `ex:61.7` | Case P's transformer loss under the EAR and DSU covers |  |
| `ex:61.8` | Case P's completion tests and performance LDs |  |
| `exh:61.1` | Construction-phase control map |  |
| `exh:61.2` | One monthly drawdown cycle |  |
| `exh:61.3` | Planned value, earned value and certified payments on a desalination EPC |  |
| `exh:61.4` | How LDs, DSU proceeds and PPA LDs move through the accounts |  |
| `exh:61.5` | Three completions compared |  |
| `exh:61.6` | Delay cost against LDs at four delay lengths |  |
| `exh:61.7` | Anatomy of an independent engineer's monthly report |  |
| `exh:61.8` | Case P construction timeline, August 2018 to December 2021 |  |
| `exh:61.9` | Case P hard-cost overrun and its funding |  |
| `exh:61.10` | Lenders' completion package checklist |  |
| `cl:61.1` | Lenders' completion financial test, common terms agreement (in the solution to Exercise 61.11; Illustrative) |  |
| `eq:61.1` | Funding shortfall under the cost-to-complete test |  |
| `eq:61.2` | Risk-weighted contingency exposure |  |
| `eq:61.3` | Schedule performance index and forecast duration |  |
| `eq:61.4` | Prepayment needed to restore the target DSCR after a performance shortfall |  |
| `fw:delay-cash-bridge` | Framework 61.1 Delay cash bridge | home ssec:61.6.3 |
| `fw:contractor-distress-ladder` | Framework 61.2 Contractor distress ladder | home ssec:61.8.3 |
| `fw:completion-test-matrix` | Framework 61.3 Completion test matrix | home ssec:61.11.2 |

### Chapter 62: Operating the project as owner and lender

Source brief: `briefs/u13.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:62` | Operating the project as owner and lender |  |
| `sec:62.1` | What lenders watch once the plant runs |  |
| `ssec:62.1.1` | From construction control to covenant monitoring |  |
| `ssec:62.1.2` | The operating covenant calendar |  |
| `sec:62.2` | Reporting and compliance |  |
| `ssec:62.2.1` | The operating report |  |
| `ssec:62.2.2` | The compliance certificate |  |
| `ssec:62.2.3` | Updating the banking case |  |
| `ssec:62.2.4` | Environmental, social and permit compliance in operation |  |
| `sec:62.3` | Budgets |  |
| `ssec:62.3.1` | The annual operating budget |  |
| `ssec:62.3.2` | Variance rules and the default budget |  |
| `ssec:62.3.3` | Capital and major-maintenance budgets |  |
| `sec:62.4` | Ratio testing and distributions |  |
| `ssec:62.4.1` | Test dates and calculation periods |  |
| `ssec:62.4.2` | Running the distribution test |  |
| `ssec:62.4.3` | Lock-up, trapped cash and its release |  |
| `ssec:62.4.4` | Equity cures in practice |  |
| `sec:62.5` | Maintenance and availability management |  |
| `ssec:62.5.1` | Planned outages against availability targets |  |
| `ssec:62.5.2` | Major maintenance, LTSA claims and spares |  |
| `ssec:62.5.3` | Insurance renewals in operation |  |
| `ssec:62.5.4` | Operational-technology cyber controls and reporting (new, R-029) | new label |
| `sec:62.6` | Performance management |  |
| `ssec:62.6.1` | The KPIs that matter by asset type |  |
| `ssec:62.6.2` | Managing the O&M operator and LTSA provider |  |
| `ssec:62.6.3` | Ivanpah and an output guarantee that the plant could not meet |  |
| `sec:62.7` | Waivers and amendments |  |
| `ssec:62.7.1` | Waiver, consent or amendment |  |
| `ssec:62.7.2` | Writing the request |  |
| `ssec:62.7.3` | Pricing a waiver |  |
| `ssec:62.7.4` | The waiver letter |  |
| `sec:62.8` | Optimizing the asset during the debt life |  |
| `ssec:62.8.1` | Uprates, repowering and hybridization |  |
| `ssec:62.8.2` | Financing an optimization inside an existing financing |  |
| `ssec:62.8.3` | The optimization gate |  |
| `sec:62.9` | Walkthrough: a semiannual compliance certificate, line by line |  |
| `sec:62.10` | Walkthrough: a waiver request from first call to signed letter |  |
| `sec:62.11` | Case P: two years of operation, a breach and a waiver |  |
| `ssec:62.11.1` | The first operating year against the financial close base case |  |
| `ssec:62.11.2` | The June 30, 2023 test |  |
| `ssec:62.11.3` | Negotiating the waiver |  |
| `ssec:62.11.4` | What the waiver cost and what it bought |  |
| `sec:62.12` | Practitioner's notebook |  |
| `sec:62.13` | Judgment drill |  |
| `sec:62.14` | A waiver buys time but does not change the debt |  |
| `sec:62.15` | Exercises |  |
| `sec:62.16` | Solutions to exercises |  |
| `ex:62.1` | Testing an operating budget against variance rules |  |
| `ex:62.2` | A distribution test on a semiannual test date |  |
| `ex:62.3` | A forced outage and the availability headroom |  |
| `ex:62.4` | What a waiver costs and what a cure costs |  |
| `ex:62.5` | Adding a battery to a solar plant inside an existing financing |  |
| `exh:62.1` | The operating covenant calendar for one year |  |
| `exh:62.2` | Test, calculation, payment and distribution dates for a semiannual borrower |  |
| `exh:62.3` | A semiannual compliance certificate |  |
| `exh:62.4` | Case P operating year 1 against the financial close base case |  |
| `exh:62.5` | Case P waiver and amendment terms, October 2023 |  |
| `cl:62.1` | Waiver and amendment letter, operative provisions |  |
| `cl:62.2` | Reservation of rights in a waiver letter (variants 62.2a sponsor-friendly, 62.2b lender-friendly) |  |
| `fw:operating-covenant-calendar` | Framework 62.1 Operating covenant calendar | home ssec:62.1.2 |
| `fw:waiver-request-ladder` | Framework 62.2 Waiver request ladder | home ssec:62.7.1 |
| `fw:optimization-gate` | Framework 62.3 Optimization gate | home ssec:62.8.3 |

### Chapter 63: Refinancing, repricing and secondary sales

Source brief: `briefs/u13.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:63` | Refinancing, repricing and secondary sales |  |
| `sec:63.1` | Why projects refinance |  |
| `ssec:63.1.1` | The de-risking dividend |  |
| `ssec:63.1.2` | Planned refinancings and mini-perms |  |
| `ssec:63.1.3` | Opportunistic refinancings |  |
| `ssec:63.1.4` | Who gains and who must agree |  |
| `sec:63.2` | The economics of a refinancing |  |
| `ssec:63.2.1` | Measuring the gain |  |
| `ssec:63.2.2` | Breaking loans, swaps and bonds early |  |
| `ssec:63.2.3` | Tax and accounting frictions |  |
| `sec:63.3` | Repricing without refinancing |  |
| `ssec:63.3.1` | Margin step-downs and repricing amendments |  |
| `ssec:63.3.2` | Institutional term loans and soft call protection |  |
| `sec:63.4` | Re-gearing and equity release |  |
| `ssec:63.4.1` | Debt capacity after completion |  |
| `ssec:63.4.2` | The public counterparty's exposure |  |
| `sec:63.5` | Executing a refinancing |  |
| `ssec:63.5.1` | Choosing the instrument |  |
| `ssec:63.5.2` | Timetable and settlement mechanics |  |
| `ssec:63.5.3` | Consents from the lenders who stay |  |
| `sec:63.6` | Selling a stake in an operating project |  |
| `ssec:63.6.1` | Why sponsors sell and who buys |  |
| `ssec:63.6.2` | Pricing a stake in a project-financed company |  |
| `ssec:63.6.3` | The consent map |  |
| `ssec:63.6.4` | Sequencing a refinancing and a sale |  |
| `sec:63.7` | Holdco leverage in practice |  |
| `ssec:63.7.1` | Distribution coverage and the opco lock-up |  |
| `ssec:63.7.2` | Leverage on listed shares |  |
| `ssec:63.7.3` | SunEdison, TerraForm Power and a margin loan on yieldco shares |  |
| `sec:63.8` | Walkthrough: building a refinancing gain calculation in the model |  |
| `sec:63.9` | Walkthrough: selling a stake in a project-financed company, from teaser to completion |  |
| `sec:63.10` | Case P: the 2025 bond and the 2026 sale |  |
| `ssec:63.10.1` | Why refinance in 2025 |  |
| `ssec:63.10.2` | The bond, the guarantee and the swap unwind |  |
| `ssec:63.10.3` | Selling 24% to Coldharbour |  |
| `sec:63.11` | Case R: the 2025 private placement and the holdco repricing |  |
| `sec:63.12` | Practitioner's notebook |  |
| `sec:63.13` | Judgment drill |  |
| `sec:63.14` | Refinancing assumes a lender who wants the risk |  |
| `sec:63.15` | Exercises |  |
| `sec:63.16` | Solutions to exercises |  |
| `ex:63.1` | Measuring a refinancing gain on a contracted wind farm |  |
| `ex:63.2` | A make-whole on fixed-rate notes |  |
| `ex:63.3` | Re-gearing after completion |  |
| `ex:63.4` | Pricing a 30% stake in a project company |  |
| `ex:63.5` | Holdco coverage when the opco locks up |  |
| `ex:63.6` | A margin loan on listed yieldco shares |  |
| `exh:63.1` | Refinancing gain bridge for a contracted wind farm |  |
| `exh:63.2` | Make-whole premium at four Treasury yields |  |
| `exh:63.3` | Refinancing timetable from mandate to settlement |  |
| `exh:63.4` | Consent map for the sale of a stake in a project-financed company |  |
| `exh:63.5` | Stake sale steps and indicative durations |  |
| `exh:63.6` | Case P 2025 refinancing bridge |  |
| `exh:63.7` | Case P 2026 sale: price, consents and consideration |  |
| `exh:63.8` | Case R 2025 private placement by series and holdco repricing |  |
| `cl:63.1` | Minimum holding covenant, common terms agreement (in the solution to Exercise 63.11; Illustrative) |  |
| `eq:63.1` | Refinancing gain on an identical profile |  |
| `eq:63.2` | Make-whole premium | ruling: Make-whole cost at the refinancing settlement date, applying eq:30.2 (repurposed, R-095) |
| `fw:refinancing-gain-bridge` | Framework 63.1 Refinancing gain bridge | home ssec:63.2.1 |
| `fw:stake-sale-consent-map` | Framework 63.2 Stake-sale consent map | home ssec:63.6.3 |

### Chapter 64: Distress, restructuring and enforcement

Source brief: `briefs/u13.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:64` | Distress, restructuring and enforcement |  |
| `sec:64.1` | How projects get into trouble |  |
| `ssec:64.1.1` | Four routes into distress |  |
| `ssec:64.1.2` | Why distress in project finance looks different from corporate distress |  |
| `sec:64.2` | Early warning signs |  |
| `ssec:64.2.1` | Financial indicators |  |
| `ssec:64.2.2` | Operational, counterparty and market indicators |  |
| `ssec:64.2.3` | The distress early-warning dashboard |  |
| `sec:64.3` | The first ninety days |  |
| `ssec:64.3.1` | Reservation of rights and information |  |
| `ssec:64.3.2` | Organizing the creditors |  |
| `ssec:64.3.3` | Standstill agreements |  |
| `sec:64.4` | Buying time |  |
| `ssec:64.4.1` | Waivers and deferrals in distress |  |
| `ssec:64.4.2` | Amend-and-extend |  |
| `ssec:64.4.3` | Cash sweeps and cash control in distress |  |
| `ssec:64.4.4` | Dulles Greenway and deferring debt service into the future |  |
| `sec:64.5` | Sponsor support in distress |  |
| `ssec:64.5.1` | Why sponsors put money in and why they stop |  |
| `ssec:64.5.2` | Forms of sponsor support |  |
| `sec:64.6` | Valuing the alternatives |  |
| `ssec:64.6.1` | Enterprise value and the relevant alternative |  |
| `ssec:64.6.2` | The recovery waterfall |  |
| `ssec:64.6.3` | Restructure, sell, enforce or terminate |  |
| `sec:64.7` | Restructuring the debt |  |
| `ssec:64.7.1` | Sizing sustainable debt |  |
| `ssec:64.7.2` | Debt-for-equity swaps and allocating the new equity |  |
| `ssec:64.7.3` | New money, PIK and DIP financing |  |
| `ssec:64.7.4` | Hedge close-outs in restructurings |  |
| `sec:64.8` | Distressed sales |  |
| `ssec:64.8.1` | Selling a distressed project |  |
| `ssec:64.8.2` | Indiana Toll Road and the prepackaged sale |  |
| `ssec:64.8.3` | Sydney's tunnels and receivership sales |  |
| `sec:64.9` | Enforcement |  |
| `ssec:64.9.1` | Enforcing over shares |  |
| `ssec:64.9.2` | Enforcing over assets |  |
| `ssec:64.9.3` | Step-in in practice |  |
| `ssec:64.9.4` | SH 130 and lenders taking the keys |  |
| `sec:64.10` | Insolvency regimes |  |
| `ssec:64.10.1` | Chapter 11 in the United States |  |
| `ssec:64.10.2` | Schemes and restructuring plans in England |  |
| `ssec:64.10.3` | Civil-law and EU preventive frameworks |  |
| `ssec:64.10.4` | Cross-class cram-down arithmetic |  |
| `sec:64.11` | PPP-specific dynamics |  |
| `ssec:64.11.1` | Termination compensation as the floor, or no floor |  |
| `ssec:64.11.2` | The contracting authority's levers and limits |  |
| `ssec:64.11.3` | Eurotunnel and the serial restructuring of a concession |  |
| `sec:64.12` | The role of the state |  |
| `ssec:64.12.1` | The state as stabilizer |  |
| `ssec:64.12.2` | The state as creditor |  |
| `ssec:64.12.3` | The state as regulator, grantor and shareholder |  |
| `sec:64.13` | Walkthrough: a restructuring term sheet, clause by clause |  |
| `sec:64.14` | Case T: the Merrick Link from lock-up to restructuring plan |  |
| `ssec:64.14.1` | Warnings and default, 2019 to 2020 |  |
| `ssec:64.14.2` | Standstill and sponsor support, 2021 |  |
| `ssec:64.14.3` | Advisers and the amend-and-extend, 2022 |  |
| `ssec:64.14.4` | The alternatives on the table |  |
| `ssec:64.14.5` | The restructuring support agreement and the plan, 2023 |  |
| `ssec:64.14.6` | The restructured Merrick Link |  |
| `sec:64.15` | Practitioner's notebook |  |
| `sec:64.16` | Judgment drill |  |
| `sec:64.17` | Restructuring settles who owns the project until its contracts end |  |
| `sec:64.18` | Exercises |  |
| `sec:64.19` | Solutions to exercises |  |
| `ex:64.1` | Liquidity runway at a container terminal |  |
| `ex:64.2` | The price of an amend-and-extend |  |
| `ex:64.3` | Recoveries under four alternatives |  |
| `ex:64.4` | Sizing sustainable debt and the write-down |  |
| `ex:64.5` | Allocating the new equity |  |
| `ex:64.6` | Testing a cross-class cram-down |  |
| `exh:64.1` | Routes into distress in eight real cases |  |
| `exh:64.2` | Distress early-warning dashboard thresholds |  |
| `exh:64.3` | Recoveries by class under four alternatives |  |
| `exh:64.4` | Restructure, sell, enforce or terminate decision tree |  |
| `exh:64.5` | Allocation of restructuring surplus |  |
| `exh:64.6` | Restructuring tools compared: Chapter 11, Part 26 and 26A, StaRUG, WHOA, French accelerated safeguard |  |
| `exh:64.7` | A restructuring term sheet |  |
| `exh:64.8` | Case T timeline, December 2019 to December 2023 |  |
| `exh:64.9` | Case T restructuring terms by class |  |
| `cl:64.1` | Standstill agreement, operative provisions |  |
| `cl:64.2` | Standstill termination events (variants 64.2a sponsor-friendly, 64.2b lender-friendly) |  |
| `eq:64.1` | Liquidity runway |  |
| `eq:64.2` | Recovery of a class in a priority waterfall |  |
| `eq:64.3` | Sustainable debt |  |
| `fw:distress-dashboard` | Framework 64.1 Distress early-warning dashboard | home ssec:64.2.3 |
| `fw:restructure-sell-enforce-terminate` | Framework 64.2 Restructure, sell, enforce or terminate | home ssec:64.6.3 |

### Chapter 65: Decommissioning, handback and end-of-life value

Source brief: `briefs/u13.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:65` | Decommissioning, handback and end-of-life value |  |
| `sec:65.1` | How a project ends |  |
| `ssec:65.1.1` | Contract end, technical end and economic end |  |
| `ssec:65.1.2` | What each party wants at the end |  |
| `sec:65.2` | Decommissioning obligations |  |
| `ssec:65.2.1` | Where the obligation comes from |  |
| `ssec:65.2.2` | Estimating the cost |  |
| `ssec:65.2.3` | Securing the obligation |  |
| `ssec:65.2.4` | Decommissioning, the waterfall and the lenders' tail |  |
| `ssec:65.2.5` | Moss Landing and remediation costs that outran the estimate |  |
| `sec:65.3` | Handback in practice |  |
| `ssec:65.3.1` | Handback conditions and how they are measured |  |
| `ssec:65.3.2` | The handback timeline |  |
| `ssec:65.3.3` | Funding the handback works |  |
| `ssec:65.3.4` | UK PFI contract expiry |  |
| `sec:65.4` | Life extension economics |  |
| `ssec:65.4.1` | What extends a plant's life |  |
| `ssec:65.4.2` | Extend, repower or retire |  |
| `ssec:65.4.3` | Financing at the end of the original debt |  |
| `sec:65.5` | Terminal value and end-of-life value | ruling: End-of-life value in bids and lending (retitled, R-014) |
| `ssec:65.5.1` | How much value sits in the tail |  |
| `ssec:65.5.2` | Terminal value conventions | ruling: Tail conventions at contract end and asset end (retitled, R-014) |
| `ssec:65.5.3` | Tail value in bids and lending |  |
| `sec:65.6` | Walkthrough: reading a decommissioning cost estimate and security plan |  |
| `sec:65.7` | Case P: planning Bélanou's handback to SEKA |  |
| `sec:65.8` | Case R: repower or retire Thatcher Flats, and the portfolio's decommissioning obligations |  |
| `sec:65.9` | Practitioner's notebook |  |
| `sec:65.10` | Judgment drill |  |
| `sec:65.11` | The last years of a project are decided in its first contracts |  |
| `sec:65.12` | Exercises |  |
| `sec:65.13` | Solutions to exercises |  |
| `ex:65.1` | Estimating a wind farm's decommissioning cost |  |
| `ex:65.2` | Sinking fund or surety bond |  |
| `ex:65.3` | Funding a toll road's handback works |  |
| `ex:65.4` | Extend, repower or retire a 20-year-old wind farm |  |
| `ex:65.5` | How much of the value is in the tail |  |
| `exh:65.1` | Decommissioning cost estimate for a 48-turbine wind farm |  |
| `exh:65.2` | Sinking fund against surety bond |  |
| `exh:65.3` | Handback readiness timeline |  |
| `exh:65.4` | Handback reserve schedule for a toll road |  |
| `exh:65.5` | Extend, repower or retire: cash flows and NPV |  |
| `exh:65.6` | Annotated decommissioning estimate and security plan |  |
| `exh:65.7` | Case P contract, debt and land end dates to 2046 |  |
| `exh:65.8` | Case R useful lives and decommissioning obligations by asset |  |
| `cl:65.1` | Handback survey and works, concession agreement (in the solution to Exercise 65.9; Illustrative) |  |
| `eq:65.1` | Sinking-fund contribution |  |
| `fw:handback-readiness-timeline` | Framework 65.1 Handback readiness timeline | home ssec:65.3.2 |
| `fw:end-of-life-option-tree` | Framework 65.2 End-of-life option tree | home ssec:65.4.2 |

### Chapter 66: Accounting for projects and sponsors

Source brief: `briefs/u14.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:66` | Accounting for projects and sponsors |  |
| `sec:66.1` | Who consolidates the project company |  |
| `ssec:66.1.1` | Control and the three questions behind it |  |
| `ssec:66.1.2` | Reserved matters as substantive or protective rights |  |
| `ssec:66.1.3` | Consolidating without a majority under the variable interest entity model |  |
| `ssec:66.1.4` | What consolidation does to the sponsor's numbers |  |
| `sec:66.2` | Joint arrangements and the equity method |  |
| `ssec:66.2.1` | Joint control and unanimous consent |  |
| `ssec:66.2.2` | Joint venture or joint operation |  |
| `ssec:66.2.3` | The equity method step by step |  |
| `ssec:66.2.4` | Shareholder loans in the investor's books |  |
| `sec:66.3` | Partial sales and loss of control |  |
| `ssec:66.3.1` | Selling a minority while keeping control |  |
| `ssec:66.3.2` | Losing control, remeasuring the retained stake and recognizing a gain |  |
| `ssec:66.3.3` | Recycled reserves, deferred consideration and transaction costs |  |
| `sec:66.4` | Service concessions under IFRIC 12 and ASC 853 |  |
| `ssec:66.4.1` | The scope test |  |
| `ssec:66.4.2` | The financial asset model |  |
| `ssec:66.4.3` | The intangible model and the bifurcated model |  |
| `ssec:66.4.4` | What the model choice does to covenants and ratings |  |
| `ssec:66.4.5` | ASC 853 and US practice |  |
| `ssec:66.4.6` | Testing whether an IPP is a concession, with Bélanou as the case |  |
| `ssec:66.4.7` | Decommissioning provisions and asset retirement obligations (new, R-015) | new label |
| `sec:66.5` | Leases hidden in offtake contracts |  |
| `ssec:66.5.1` | The lease test applied to PPAs, tolls and battery contracts |  |
| `ssec:66.5.2` | Classifying the lease from the project company's side |  |
| `ssec:66.5.3` | What changes for the offtaker |  |
| `sec:66.6` | Hedge accounting for project hedges |  |
| `ssec:66.6.1` | Why hedge accounting matters to a project and its sponsors |  |
| `ssec:66.6.2` | Cash flow hedge mechanics |  |
| `ssec:66.6.3` | De-designation when drawdowns slip |  |
| `ssec:66.6.4` | Power purchase agreements and virtual PPAs |  |
| `ssec:66.6.5` | Hedge accounting under ASC 815 and ASU 2017-12 |  |
| `sec:66.7` | Expected credit losses |  |
| `ssec:66.7.1` | From incurred loss to expected loss |  |
| `ssec:66.7.2` | Offtaker receivables backed by a letter of credit and a sovereign guarantee |  |
| `ssec:66.7.3` | A project loan that slides, seen from the lender's side |  |
| `sec:66.8` | How accounting goals shape structures |  |
| `ssec:66.8.1` | The deconsolidation motive |  |
| `ssec:66.8.2` | The volatility motive |  |
| `ssec:66.8.3` | Covenants written on accounts and the frozen GAAP clause |  |
| `ssec:66.8.4` | IFRS 18 from 2027 |  |
| `ssec:66.8.5` | The accounting outcome map |  |
| `sec:66.9` | NEOM Green Hydrogen and consolidation by a one-third owner |  |
| `sec:66.10` | What consolidation and impairment did to TerraForm Power's and Ørsted's reported results |  |
| `sec:66.11` | Walkthrough: writing the accounting position paper for a new project |  |
| `sec:66.12` | Case P: Kilnworth's accounts from consolidation to the equity method |  |
| `sec:66.13` | Practitioner's notebook |  |
| `sec:66.14` | Judgment drill |  |
| `sec:66.15` | Reported profit is not taxable profit |  |
| `sec:66.16` | Exercises |  |
| `sec:66.17` | Solutions to exercises |  |
| `ex:66.1` | Consolidating versus equity-accounting the same project (Illustrative) |  |
| `ex:66.2` | Rolling forward an equity-method investment (Illustrative) |  |
| `ex:66.3` | Losing control and remeasuring the retained stake (Illustrative) |  |
| `ex:66.4` | The financial asset model for an availability PPP (Illustrative) |  |
| `ex:66.5` | The intangible model for a user-pay toll road (Illustrative) |  |
| `ex:66.6` | Classifying a battery toll as a lease (Illustrative) |  |
| `ex:66.7` | A project swap under cash flow hedge accounting (Illustrative) |  |
| `ex:66.8` | Expected credit loss on offtaker arrears (Illustrative) |  |
| `ex:66.9` | Kilnworth's gain on loss of control (Case P) |  |
| `exh:66.1` | Reserved matters in a project shareholders' agreement, classified (Illustrative) |  |
| `exh:66.2` | Classifying a project's main asset: IFRIC 12, lease or plant (Illustrative) |  |
| `exh:66.3` | Sponsor metrics under consolidation and equity accounting (USD m) (Illustrative) |  |
| `exh:66.4` | Kilnworth's accounting for Bélanou Power, 2018 to 2026 (USD m) (Case P) |  |
| `cl:66.1` | Accounting principles and changes in accounting standards, common terms agreement (Illustrative) |  |
| `eq:66.1` | Gain on loss of control |  |
| `eq:66.2` | Cash flow hedge reserve (lower-of rule) |  |
| `fw:accounting-outcome-map` | Framework 66.1 Accounting outcome map | home ssec:66.8.5 |

### Chapter 67: Tax structuring

Source brief: `briefs/u14.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:67` | Tax structuring |  |
| `sec:67.1` | Where tax leaks between the project and the investor |  |
| `ssec:67.1.1` | Five taxing points on one stream of cash |  |
| `ssec:67.1.2` | Measuring leakage |  |
| `sec:67.2` | Holding structures and tax treaties |  |
| `ssec:67.2.1` | Why projects are held through holding companies |  |
| `ssec:67.2.2` | What a double tax treaty changes |  |
| `ssec:67.2.3` | Anti-abuse rules and substance |  |
| `ssec:67.2.4` | The host government's view |  |
| `sec:67.3` | Withholding tax on interest and the gross-up |  |
| `ssec:67.3.1` | Who bears withholding tax |  |
| `ssec:67.3.2` | Pricing the gross-up |  |
| `ssec:67.3.3` | Exemptions for development and officially supported lenders |  |
| `ssec:67.3.4` | Drafting the gross-up and tax indemnity |  |
| `sec:67.4` | Shareholder loans and thin capitalization |  |
| `ssec:67.4.1` | Why sponsors lend instead of subscribing for shares |  |
| `ssec:67.4.2` | Thin capitalization ratios |  |
| `ssec:67.4.3` | Recharacterization and the treaty mismatch |  |
| `sec:67.5` | Earnings-based interest limitation |  |
| `ssec:67.5.1` | The OECD design |  |
| `ssec:67.5.2` | The EU rule in ATAD Article 4 |  |
| `ssec:67.5.3` | The UK corporate interest restriction and the public infrastructure exemption |  |
| `ssec:67.5.4` | US section 163(j) after OBBBA |  |
| `ssec:67.5.5` | What a 30% cap does to a project's profile |  |
| `ssec:67.5.6` | Grandfathering and refinancing |  |
| `sec:67.6` | Transfer pricing inside a project |  |
| `ssec:67.6.1` | The arm's-length principle applied to project contracts |  |
| `ssec:67.6.2` | Pricing a shareholder loan at arm's length |  |
| `ssec:67.6.3` | Documentation and disputes |  |
| `sec:67.7` | VAT and indirect taxes during construction |  |
| `ssec:67.7.1` | How VAT reaches a project under construction |  |
| `ssec:67.7.2` | The cost of the refund lag |  |
| `ssec:67.7.3` | When refunds stop |  |
| `sec:67.8` | Tax incentives and holidays |  |
| `ssec:67.8.1` | The incentive menu |  |
| `ssec:67.8.2` | What a holiday is worth |  |
| `ssec:67.8.3` | Holidays and tariffs |  |
| `sec:67.9` | Pillar Two and the global minimum tax |  |
| `ssec:67.9.1` | Who is in scope |  |
| `ssec:67.9.2` | The top-up calculation |  |
| `ssec:67.9.3` | Who collects |  |
| `ssec:67.9.4` | The Side-by-Side Package of January 5, 2026 |  |
| `ssec:67.9.5` | Tax credits under GloBE |  |
| `ssec:67.9.6` | The Pillar Two screen |  |
| `sec:67.10` | US clean-energy credits as structuring constraints |  |
| `ssec:67.10.1` | The deadlines |  |
| `ssec:67.10.2` | Prohibited foreign entities in the cap table and the debt stack |  |
| `ssec:67.10.3` | What lenders and tax equity investors now ask for |  |
| `sec:67.11` | Taxes on exit |  |
| `ssec:67.11.1` | Capital gains on a project sale |  |
| `ssec:67.11.2` | Indirect transfer taxes |  |
| `sec:67.12` | Oyu Tolgoi, Cobre Panamá and Bujagali and the host's power to reopen fiscal terms |  |
| `sec:67.13` | Walkthrough: the tax structure paper for a cross-border project |  |
| `sec:67.14` | Case P: holding structure, gross-up, grandfathering and exit tax |  |
| `sec:67.15` | Practitioner's notebook |  |
| `sec:67.16` | Judgment drill |  |
| `sec:67.17` | The rules that decide who may lend |  |
| `sec:67.18` | Exercises |  |
| `sec:67.19` | Solutions to exercises |  |
| `ex:67.1` | Leakage on USD 100 of project profit (Illustrative) |  |
| `ex:67.2` | The cost of grossing up interest withholding (Illustrative) |  |
| `ex:67.3` | Thin capitalization (Illustrative) |  |
| `ex:67.4` | A 30% EBITDA cap over the first eight operating years (Illustrative) |  |
| `ex:67.5` | Section 163(j) on an EBIT and an EBITDA basis (Illustrative) |  |
| `ex:67.6` | Testing a shareholder-loan rate against arm's length (Illustrative) |  |
| `ex:67.7` | The cost of a nine-month VAT refund lag (Illustrative) |  |
| `ex:67.8` | What a five-year holiday is worth (Illustrative) |  |
| `ex:67.9` | Pillar Two top-up on a holiday project (Illustrative) |  |
| `ex:67.10` | Testing a cap table and debt stack for foreign influence (Illustrative) |  |
| `ex:67.11` | An indirect transfer tax on a stake sale (Illustrative) |  |
| `ex:67.12` | Case P withholding leakage and gross-up cost (Case P) |  |
| `exh:67.1` | Where tax leaks from a cross-border project (Illustrative) |  |
| `exh:67.2` | Interest limitation regimes compared: OECD, EU, UK, US (as of October 3, 2026) |  |
| `exh:67.3` | Pillar Two: who collects the top-up (Illustrative) |  |
| `exh:67.4` | US wind, solar and storage credit deadlines and foreign-entity tests (as of October 3, 2026) |  |
| `exh:67.5` | Case P withholding rates and exemptions (Case P) |  |
| `cl:67.1` | (caption not stated in brief; writer supplies) | implied by the brief text; writer assigns this label in order of appearance |
| `eq:67.1` | Pillar Two top-up |  |
| `eq:67.2` | Gross-up payment, $P = I/(1-w)$ |  |
| `eq:67.3` | Earnings-based cap: deductible interest $= (NI}_t, 0.30 EBITDA}^{tax}}_t + CF}^{used}}_t)$ (writer finalizes notation consistent with Chapter 41) |  |
| `fw:tax-leakage-map` | Framework 67.1 Tax leakage map | home ssec:67.1.2 |
| `fw:pillar-two-screen` | Framework 67.2 Pillar Two screen | home ssec:67.9.6 |

### Chapter 68: Capital rules for banks and insurers

Source brief: `briefs/u14.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:68` | Capital rules for banks and insurers |  |
| `sec:68.1` | Why capital rules decide who lends |  |
| `ssec:68.1.1` | Capital as a cost of lending |  |
| `ssec:68.1.2` | Two regulated balance sheets, two logics |  |
| `sec:68.2` | Three routes to bank capital |  |
| `ssec:68.2.1` | The standardised approach |  |
| `ssec:68.2.2` | Internal ratings |  |
| `ssec:68.2.3` | Supervisory slotting |  |
| `sec:68.3` | The Basel III project finance ladder and the output floor |  |
| `ssec:68.3.1` | The standardised ladder |  |
| `ssec:68.3.2` | The output floor |  |
| `sec:68.4` | Three jurisdictions, three answers |  |
| `ssec:68.4.1` | The EU rules in CRR3 |  |
| `ssec:68.4.2` | The UK Basel 3.1 rules |  |
| `ssec:68.4.3` | The US proposals of March 2026 |  |
| `ssec:68.4.4` | Why the same loan carries different capital in London, Frankfurt and New York |  |
| `sec:68.5` | From capital to price |  |
| `ssec:68.5.1` | The minimum margin | ruling: The capital charge under each route (retitled, R-076) |
| `ssec:68.5.2` | What the bridge shows |  |
| `ssec:68.5.3` | Regulatory expected loss and accounting provisions |  |
| `sec:68.6` | Credit risk mitigation in project lending |  |
| `ssec:68.6.1` | ECA cover and sovereign substitution |  |
| `ssec:68.6.2` | MDBs, A/B loans and preferred creditor treatment |  |
| `ssec:68.6.3` | Insurance as credit protection |  |
| `sec:68.7` | Insurers and Solvency II |  |
| `ssec:68.7.1` | The standard formula in one page |  |
| `ssec:68.7.2` | Qualifying infrastructure investments |  |
| `ssec:68.7.3` | Qualifying infrastructure corporates |  |
| `ssec:68.7.4` | The 2025 to 2027 review |  |
| `ssec:68.7.5` | Solvency UK and the matching adjustment |  |
| `ssec:68.7.6` | What the charges mean in spread |  |
| `sec:68.8` | Banks, insurers and the life of a project |  |
| `ssec:68.8.1` | Who holds construction risk and who holds operating risk |  |
| `ssec:68.8.2` | Designing for capital |  |
| `ssec:68.8.3` | Who pays for a change in capital rules |  |
| `sec:68.9` | IFC's B-loans and preferred creditor treatment in bank capital |  |
| `sec:68.10` | Walkthrough: the capital section of a bank's credit application |  |
| `sec:68.11` | Case P and Case T: Castellan grades Bélanou, and the Merrick Link's insurer bondholders |  |
| `sec:68.12` | Practitioner's notebook |  |
| `sec:68.13` | Judgment drill |  |
| `sec:68.14` | Capital prices the debt; the market decides what to build |  |
| `sec:68.15` | Exercises |  |
| `sec:68.16` | Solutions to exercises |  |
| `ex:68.1` | Capital and the minimum margin under each route (Illustrative) |  |
| `ex:68.2` | The EU output floor on a project book (Illustrative) |  |
| `ex:68.3` | Capital on a bank's share of a multi-tranche deal (Illustrative) |  |
| `ex:68.4` | What Solvency II infrastructure qualification is worth to an insurer (Illustrative) |  |
| `ex:68.5` | Bank or insurer debt for an availability PPP at completion (Illustrative) |  |
| `ex:68.6` | Castellan's capital on its Case P exposures (Case P) |  |
| `exh:68.1` | EU slotting risk weights by category and remaining maturity |  |
| `exh:68.2` | EU slotting expected-loss rates by category and remaining maturity |  |
| `exh:68.3` | EU high-quality project finance criteria and the project features that meet them |  |
| `exh:68.4` | EU output floor phase-in, 2025 to 2030 |  |
| `exh:68.5` | One operational project loan under EU, UK and US rules (EUR m) (Illustrative) |  |
| `exh:68.6` | Solvency II qualifying infrastructure checklist (Illustrative) |  |
| `exh:68.7` | Slotting scorecard template (Illustrative) |  |
| `cl:68.1` | (caption not stated in brief; writer supplies) | implied by the brief text; writer assigns this label in order of appearance |
| `eq:68.1` | Minimum margin from capital | ruling: Capital charge per unit of exposure, feeding eq:38.1 (repurposed, R-076) |
| `eq:68.2` | Output floor: $RWA} = (RWA}_{IRB}}, x RWA}_{SA}})$ |  |
| `fw:capital-to-price-bridge` | Framework 68.1 Capital-to-price bridge | home ssec:68.5.2 |

### Chapter 69: Thermal power

Source brief: `briefs/u15.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:69` | Thermal power |  |
| `sec:69.1` | Where thermal plants make money |  |
| `ssec:69.1.1` | Capital-heavy and fuel-heavy plants |  |
| `ssec:69.1.2` | The screening curve |  |
| `ssec:69.1.3` | System roles and what they pay |  |
| `sec:69.2` | What a financier needs from the engineering |  |
| `ssec:69.2.1` | Heat rate, degradation and recovery |  |
| `ssec:69.2.2` | Starts, hours and maintenance intervals |  |
| `ssec:69.2.3` | Fuel flexibility and fuel-chain lock-in |  |
| `sec:69.3` | Revenue models for thermal plants |  |
| `ssec:69.3.1` | The single-buyer capacity-plus-energy PPA |  |
| `ssec:69.3.2` | Tolling and the IWPP |  |
| `ssec:69.3.3` | Merchant energy and scarcity pricing |  |
| `ssec:69.3.4` | Capacity markets and hybrid revenue |  |
| `sec:69.4` | Risks that decide thermal deals |  |
| `ssec:69.4.1` | Fuel supply, price and deliverability |  |
| `ssec:69.4.2` | Heat rate and performance |  |
| `ssec:69.4.3` | Dispatch and affordability |  |
| `ssec:69.4.4` | Transition, permits and stranding |  |
| `ssec:69.4.5` | Water, emissions and site |  |
| `sec:69.5` | The thermal contract set |  |
| `ssec:69.5.1` | The set and its interlocks |  |
| `ssec:69.5.2` | Where thermal contracts leave gaps |  |
| `ssec:69.5.3` | A sector clause: carbon-cost pass-through in a tolling agreement |  |
| `sec:69.6` | Financing terms for thermal plants |  |
| `ssec:69.6.1` | Contracted IPPs in emerging and Gulf markets |  |
| `ssec:69.6.2` | Merchant and capacity-backed thermal in liberalized markets |  |
| `ssec:69.6.3` | ECA rules and tenor |  |
| `sec:69.7` | Modeling a thermal plant |  |
| `ssec:69.7.1` | Dispatch and part load |  |
| `ssec:69.7.2` | Fuel and pass-through checks |  |
| `ssec:69.7.3` | Maintenance cycle and reserves |  |
| `ssec:69.7.4` | Merchant margin modeling |  |
| `sec:69.8` | Thermal IPPs that failed with the plant running |  |
| `ssec:69.8.1` | Dabhol and the plant too big for its buyer |  |
| `ssec:69.8.2` | Paiton I and zero dispatch |  |
| `ssec:69.8.3` | Mundra and the fuel chain that broke |  |
| `ssec:69.8.4` | Hub Power, Azura-Edo and the Gulf programs |  |
| `sec:69.9` | Walkthrough: reading a thermal plant's dispatch and fuel model |  |
| `sec:69.10` | Case P: why Kessara chose a CCGT |  |
| `sec:69.11` | Practitioner's notebook |  |
| `sec:69.12` | Judgment drill |  |
| `sec:69.13` | A thermal plant is repaid by its buyer and its fuel chain |  |
| `sec:69.14` | Exercises |  |
| `sec:69.15` | Solutions to exercises |  |
| `ex:69.1` | Screening four technologies for a coastal single-buyer system |  |
| `ex:69.2` | Merchant gross margin of a CCGT in an energy-only market |  |
| `ex:69.3` | Heat-rate headroom under a fuel pass-through |  |
| `ex:69.4` | Take-or-pay exposure when dispatch falls |  |
| `ex:69.5` | What starts cost a cycling plant |  |
| `exh:69.1` | Technology cost inputs for screening (Illustrative) |  |
| `exh:69.2` | Screening curves for four thermal technologies (Illustrative) |  |
| `exh:69.3` | Thermal revenue models compared |  |
| `exh:69.4` | Contract map of a gas-fired IPP (Illustrative) |  |
| `exh:69.5` | Financing terms for thermal plants by segment |  |
| `exh:69.6` | Extract of a lender's dispatch and fuel model (Illustrative) |  |
| `exh:69.7` | Bélanou sensitivities as a thermal reference (Case P) |  |
| `cl:69.1` | Carbon-cost pass-through, tolling agreement (sponsor-, lender-, offtaker-friendly) |  |
| `eq:69.1` | Cost per MWh at a capacity factor (screening curve) |  |
| `eq:69.2` | Spark spread and clean spark spread | ruling: Merchant gross margin from the spark spread over dispatched hours, citing eq:11.7 (repurposed, R-101) |
| `fw:fuel-chain-trace` | Framework 69.1 Fuel-chain trace | home sec:69.4 |

### Chapter 70: Onshore wind and solar

Source brief: `briefs/u15.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:70` | Onshore wind and solar |  |
| `sec:70.1` | The economics of plants with no fuel bill |  |
| `ssec:70.1.1` | Cost falls, revenue risk rises |  |
| `ssec:70.1.2` | Scale and portfolios |  |
| `sec:70.2` | What a financier needs from the engineering |  |
| `ssec:70.2.1` | Wind: turbines, availability and cold weather |  |
| `ssec:70.2.2` | Solar: modules, inverters, trackers and clipping |  |
| `ssec:70.2.3` | Hybrids |  |
| `sec:70.3` | Revenue models |  |
| `ssec:70.3.1` | Auctions, CfDs and utility PPAs |  |
| `ssec:70.3.2` | Corporate offtake and hedges |  |
| `ssec:70.3.3` | Merchant revenue and capture |  |
| `sec:70.4` | Risks that decide wind and solar deals |  |
| `ssec:70.4.1` | Resource and performance |  |
| `ssec:70.4.2` | Congestion, curtailment and basis |  |
| `ssec:70.4.3` | Grid connection and evacuation |  |
| `ssec:70.4.4` | Policy dependence |  |
| `ssec:70.4.5` | Weather extremes and hedge volume |  |
| `sec:70.5` | The wind and solar contract set |  |
| `ssec:70.5.1` | Wind: turbine supply, balance of plant and the full-service agreement |  |
| `ssec:70.5.2` | Solar: modules, EPC and warranties |  |
| `ssec:70.5.3` | Interconnection, land and permits |  |
| `ssec:70.5.4` | A sector clause: the turbine availability guarantee |  |
| `sec:70.6` | Financing terms for onshore wind and solar |  |
| `ssec:70.6.1` | The US ladder by revenue quality |  |
| `ssec:70.6.2` | Tax-credit bridges and back-leverage |  |
| `ssec:70.6.3` | Other markets |  |
| `ssec:70.6.4` | When the ladder breaks |  |
| `sec:70.7` | Modeling wind and solar |  |
| `ssec:70.7.1` | From P50 to cash |  |
| `ssec:70.7.2` | Clipping, hybrids and augmentation hooks |  |
| `ssec:70.7.3` | Hedge settlement and liquidity |  |
| `ssec:70.7.4` | Tax-credit and tax-equity cash |  |
| `sec:70.8` | Real cases in wind and solar |  |
| `ssec:70.8.1` | REIPPPP and the bankable standard document |  |
| `ssec:70.8.2` | Northern Chile and the price of the wrong node |  |
| `ssec:70.8.3` | Lake Turkana and the line that was not there |  |
| `ssec:70.8.4` | CSP: Ivanpah and Noor Ouarzazate I |  |
| `sec:70.9` | Walkthrough: building the resource-to-revenue bridge for a solar plant |  |
| `sec:70.10` | Case R: capture, curtailment and credits at Mesa Corta |  |
| `sec:70.11` | Practitioner's notebook |  |
| `sec:70.12` | Judgment drill |  |
| `sec:70.13` | The megawatt-hour is worth what the node pays for it |  |
| `sec:70.14` | Exercises |  |
| `sec:70.15` | Solutions to exercises |  |
| `ex:70.1` | Capture decline on a merchant solar plant |  |
| `ex:70.2` | One cash flow, two debt amounts |  |
| `ex:70.3` | A fixed-price contract at the wrong node |  |
| `ex:70.4` | Choosing the inverter loading ratio |  |
| `ex:70.5` | What the investment tax credit is worth to a solar project in 2026 |  |
| `exh:70.1` | Cost structure of a wind farm and a solar plant (Illustrative) |  |
| `exh:70.2` | Revenue models and what each leaves with the project company |  |
| `exh:70.3` | Contract map of a split-contracted wind farm (Illustrative) |  |
| `exh:70.4` | Financing terms for onshore wind and solar, 2023 to 2026 |  |
| `exh:70.5` | Resource-to-revenue bridge for a 150 MWac solar plant (Illustrative) |  |
| `exh:70.6` | Mesa Corta capture price and revenue build, 2022 to 2030 (Case R) |  |
| `cl:70.1` | Turbine availability guarantee, full-service agreement (sponsor-, lender-, OEM-friendly) |  |
| `eq:70.1` | Captured revenue: energy after curtailment times hub price times capture ratio |  |
| `fw:resource-revenue-bridge` | Framework 70.1 Resource-to-revenue bridge | home sec:70.9 |

### Chapter 71: Offshore wind

Source brief: `briefs/u15.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:71` | Offshore wind |  |
| `sec:71.1` | The economics of building at sea |  |
| `ssec:71.1.1` | Where the money goes |  |
| `ssec:71.1.2` | Scale, supply chain and the vessel bottleneck |  |
| `sec:71.2` | How an offshore wind farm works for a financier |  |
| `ssec:71.2.1` | From turbine to onshore grid |  |
| `ssec:71.2.2` | Access, availability and losses |  |
| `sec:71.3` | Revenue models |  |
| `ssec:71.3.1` | Two-sided CfDs |  |
| `ssec:71.3.2` | Certificate contracts and fixed escalators |  |
| `ssec:71.3.3` | Corporate offtake and merchant tails |  |
| `sec:71.4` | Construction risk at sea |  |
| `ssec:71.4.1` | Weather, vessels and the installation season |  |
| `ssec:71.4.2` | Interfaces in a multi-contract build |  |
| `ssec:71.4.3` | Serial defects and cables |  |
| `ssec:71.4.4` | Dogger Bank A's delays |  |
| `sec:71.5` | Pre-FID exposure and the Ocean Wind cancellation |  |
| `ssec:71.5.1` | The exposure clock |  |
| `ssec:71.5.2` | Ocean Wind 1 and 2 |  |
| `ssec:71.5.3` | What later solicitations changed |  |
| `sec:71.6` | The offshore wind contract set |  |
| `ssec:71.6.1` | Packages and their interfaces |  |
| `ssec:71.6.2` | The marine warranty surveyor and insurers |  |
| `ssec:71.6.3` | A sector clause: weather downtime in a transport and installation contract |  |
| `sec:71.7` | Financing offshore wind |  |
| `ssec:71.7.1` | Phase ring-fencing and two-part gearing |  |
| `ssec:71.7.2` | ECAs, DFIs and new markets |  |
| `ssec:71.7.3` | US offshore wind and tax credits |  |
| `ssec:71.7.4` | Sell-downs and equity recycling |  |
| `ssec:71.7.5` | Typical terms |  |
| `sec:71.8` | Modeling offshore wind |  |
| `ssec:71.8.1` | Yield, availability and access |  |
| `ssec:71.8.2` | Construction schedule, delay and revenue start |  |
| `ssec:71.8.3` | The OFTO sale in the model |  |
| `sec:71.9` | Walkthrough: reading an offshore wind construction risk register |  |
| `sec:71.10` | Case R: Lattimer declines an offshore stake |  |
| `sec:71.11` | Practitioner's notebook |  |
| `sec:71.12` | Judgment drill |  |
| `sec:71.13` | Offshore, the price is fixed early and the cost is fixed late |  |
| `sec:71.14` | Exercises |  |
| `sec:71.15` | Solutions to exercises |  |
| `ex:71.1` | Two-part gearing for a 1.2 GW phase |  |
| `ex:71.2` | A fixed price meets cost inflation and higher rates |  |
| `ex:71.3` | The cost of a lost installation season |  |
| `ex:71.4` | From gross to net energy offshore |  |
| `exh:71.1` | Capex breakdown of a 1.2 GW offshore phase (Illustrative) |  |
| `exh:71.2` | Offshore wind farm from turbine to grid (Illustrative) |  |
| `exh:71.3` | Pre-FID exposure timeline (Illustrative) |  |
| `exh:71.4` | Contract map of a multi-contract offshore wind phase (Illustrative) |  |
| `exh:71.5` | Offshore wind financings and terms, 2020 to 2025 |  |
| `exh:71.6` | Extract of an offshore construction risk register (Illustrative) |  |
| `cl:71.1` | Weather downtime, transport and installation contract (sponsor-, lender-, contractor-friendly) |  |
| `fw:pre-fid-exposure-clock` | Framework 71.1 Pre-FID exposure clock | home ssec:71.5.1 |

### Chapter 72: Hydropower and geothermal

Source brief: `briefs/u15.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:72` | Hydropower and geothermal |  |
| `sec:72.1` | The economics of hydropower |  |
| `ssec:72.1.1` | Capital now, energy for a century |  |
| `ssec:72.1.2` | Plant types as cash-flow profiles |  |
| `sec:72.2` | Hydrology risk and who carries it |  |
| `ssec:72.2.1` | Energy tariffs, capacity tariffs and tiers |  |
| `ssec:72.2.2` | The hydrology allocation test |  |
| `ssec:72.2.3` | Droughts, climate and cascades |  |
| `sec:72.3` | Ground risk and the hydro construction contract |  |
| `ssec:72.3.1` | Why a fixed price does not fix ground risk |  |
| `ssec:72.3.2` | Baselines, sharing and contingency |  |
| `ssec:72.3.3` | E&S on the critical path |  |
| `sec:72.4` | Financing hydropower |  |
| `ssec:72.4.1` | DFI-led packages and political risk cover |  |
| `ssec:72.4.2` | Currency matching |  |
| `ssec:72.4.3` | Tenor, refinancing and the long-life mismatch |  |
| `ssec:72.4.4` | Typical terms |  |
| `sec:72.5` | Geothermal power |  |
| `ssec:72.5.1` | From exploration to power plant |  |
| `ssec:72.5.2` | Drilling risk |  |
| `ssec:72.5.3` | Reservoir decline and make-up wells |  |
| `ssec:72.5.4` | Contract structures for geothermal |  |
| `ssec:72.5.5` | Financing geothermal |  |
| `sec:72.6` | Modeling hydro and geothermal |  |
| `ssec:72.6.1` | Hydrology series to energy |  |
| `ssec:72.6.2` | Tiered tariffs in the model |  |
| `ssec:72.6.3` | Geothermal wells and decline |  |
| `sec:72.7` | Nam Theun 2, Bujagali and Sarulla |  |
| `ssec:72.7.1` | Nam Theun 2 and the export hydro template |  |
| `ssec:72.7.2` | Bujagali and the second attempt |  |
| `ssec:72.7.3` | Sarulla and resource risk after COD |  |
| `sec:72.8` | Walkthrough: reading a hydrology report for a run-of-river plant |  |
| `sec:72.9` | Case P: a drought on the Moraba |  |
| `sec:72.10` | Practitioner's notebook |  |
| `sec:72.11` | Judgment drill |  |
| `sec:72.12` | Underground and upstream risk must sit with someone who can carry it |  |
| `sec:72.13` | Exercises |  |
| `sec:72.14` | Solutions to exercises |  |
| `ex:72.1` | Who carries the dry year |  |
| `ex:72.2` | What tenor does to a hydro tariff |  |
| `ex:72.3` | How many wells to prove the steam |  |
| `ex:72.4` | Make-up wells to hold output |  |
| `exh:72.1` | Hydro plant types and their cash-flow profiles |  |
| `exh:72.2` | Hydrology allocation under three tariff forms (Illustrative) |  |
| `exh:72.3` | Hydropower financings compared |  |
| `exh:72.4` | Geothermal spend against resource confidence by stage (Illustrative) |  |
| `exh:72.5` | Summary of a hydrology report for a run-of-river plant (Illustrative) |  |
| `cl:72.1` | Unforeseen ground conditions, hydro EPC contract (sponsor-, lender-, contractor-friendly) |  |
| `cl:72.2` | Steam supply shortfall, geothermal steam supply arrangement (Illustrative) |  |
| `fw:hydrology-allocation` | Framework 72.1 Hydrology allocation test | home ssec:72.2.2 |
| `fw:geothermal-staging` | Framework 72.2 Geothermal resource staging | home ssec:72.5.5 |

### Chapter 73: Storage, transmission and interconnectors

Source brief: `briefs/u15.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:73` | Storage, transmission and interconnectors |  |
| `sec:73.1` | The economics of storage |  |
| `ssec:73.1.1` | Power, energy and duration |  |
| `ssec:73.1.2` | Revenues that shrink as fleets grow |  |
| `sec:73.2` | Battery technology and safety risk |  |
| `ssec:73.2.1` | Cells, integrators and warranties |  |
| `ssec:73.2.2` | Degradation, augmentation and overbuild |  |
| `ssec:73.2.3` | Fire, propagation and clean-up |  |
| `sec:73.3` | Storage revenue models and how lenders size them |  |
| `ssec:73.3.1` | The revenue stack |  |
| `ssec:73.3.2` | Sizing by revenue quality |  |
| `ssec:73.3.3` | Long-duration storage and pumped hydro |  |
| `sec:73.4` | Transmission revenue models |  |
| `ssec:73.4.1` | Regulated transmission |  |
| `ssec:73.4.2` | Competitive transmission and availability payments |  |
| `ssec:73.4.3` | Offshore transmission and OFTO sales |  |
| `ssec:73.4.4` | Offtaker-built interconnection for IPPs |  |
| `ssec:73.4.5` | Merchant lines |  |
| `sec:73.5` | Interconnectors |  |
| `ssec:73.5.1` | How an interconnector earns |  |
| `ssec:73.5.2` | Cap and floor for interconnectors |  |
| `ssec:73.5.3` | Two regulators, two governments |  |
| `sec:73.6` | Financing storage, transmission and interconnectors |  |
| `ssec:73.6.1` | Storage terms |  |
| `ssec:73.6.2` | Transmission and interconnector terms |  |
| `sec:73.7` | Modeling storage and transmission |  |
| `ssec:73.7.1` | Storage in the model |  |
| `ssec:73.7.2` | Transmission in the model |  |
| `ssec:73.7.3` | Interconnector revenue with a cap and floor |  |
| `sec:73.8` | Walkthrough: reading a battery storage technical due diligence report |  |
| `sec:73.9` | Case R and Case P: tolls, floors and a 225 kV line |  |
| `sec:73.10` | Practitioner's notebook |  |
| `sec:73.11` | Judgment drill |  |
| `sec:73.12` | Assets that earn from a difference must contract the difference or price it |  |
| `sec:73.13` | Exercises |  |
| `sec:73.14` | Solutions to exercises |  |
| `ex:73.1` | The same battery under a toll and under a floor |  |
| `ex:73.2` | Overbuild or augment |  |
| `ex:73.3` | An availability deduction on a transmission line |  |
| `ex:73.4` | An interconnector under a cap and floor |  |
| `exh:73.1` | Storage durations, costs and revenue lines (Illustrative) |  |
| `exh:73.2` | Battery revenue path in an energy-only market (Case R, Illustrative prices) |  |
| `exh:73.3` | Storage revenue stack and sizing buckets (Illustrative) |  |
| `exh:73.4` | Transmission and interconnector revenue models compared |  |
| `exh:73.5` | Financing terms and anchors for storage and transmission |  |
| `exh:73.6` | Contents of a battery technical due diligence report (Illustrative) |  |
| `exh:73.7` | A2 and A3 valuation, funding and ITC proceeds (Case R) |  |
| `cl:73.1` | Capacity maintenance, battery toll (sponsor-, lender-, offtaker-friendly) |  |
| `cl:73.2` | Availability deduction, transmission service agreement (Illustrative) |  |
| `fw:storage-stack-screen` | Framework 73.1 Storage revenue stack screen | home ssec:73.3.1 |
| `fw:transmission-revenue-selector` | Framework 73.2 Transmission revenue model selector | home sec:73.4 |

### Chapter 74: Nuclear power

Source brief: `briefs/u15.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:74` | Nuclear power |  |
| `sec:74.1` | The economics of nuclear power |  |
| `ssec:74.1.1` | Overnight cost, time and money |  |
| `ssec:74.1.2` | First-of-a-kind and the learning curve |  |
| `ssec:74.1.3` | Long life and low marginal cost |  |
| `sec:74.2` | Why lenders avoid nuclear construction risk |  |
| `ssec:74.2.1` | Size, duration and contractor capacity |  |
| `ssec:74.2.2` | Licensing, politics and shutdown risk |  |
| `ssec:74.2.3` | Liability and insurance |  |
| `sec:74.3` | Five ways nuclear plants have been financed |  |
| `ssec:74.3.1` | Sponsor balance sheets under a CfD: Hinkley Point C |  |
| `ssec:74.3.2` | A nuclear RAB: Sizewell C |  |
| `ssec:74.3.3` | Regulated utilities and federal guarantees: Vogtle 3 and 4 |  |
| `ssec:74.3.4` | A sovereign lends to itself: Barakah |  |
| `ssec:74.3.5` | SMRs and state sponsors |  |
| `sec:74.4` | Decommissioning, waste and the long tail |  |
| `ssec:74.4.1` | Funded decommissioning |  |
| `ssec:74.4.2` | Waste |  |
| `sec:74.5` | Financing terms and ECA support for nuclear |  |
| `ssec:74.5.1` | What the market shows |  |
| `ssec:74.5.2` | ECAs and the Nuclear Sector Understanding |  |
| `sec:74.6` | Modeling a nuclear project |  |
| `ssec:74.6.1` | Long construction and IDC |  |
| `ssec:74.6.2` | RAB revenue and cost sharing |  |
| `ssec:74.6.3` | Decommissioning and fuel |  |
| `sec:74.7` | Walkthrough: reading a nuclear government support package |  |
| `sec:74.8` | Case P: Kessara signs a small modular reactor memorandum |  |
| `sec:74.9` | Practitioner's notebook |  |
| `sec:74.10` | Judgment drill |  |
| `sec:74.11` | In nuclear, the state chooses how much risk to keep before anyone else can lend |  |
| `sec:74.12` | Exercises |  |
| `sec:74.13` | Solutions to exercises |  |
| `ex:74.1` | How much of a nuclear plant's cost is money |  |
| `ex:74.2` | Who pays for an overrun under a RAB with sharing |  |
| `ex:74.3` | Funding decommissioning over the operating life |  |
| `exh:74.1` | Five nuclear financing models compared |  |
| `exh:74.2` | Nuclear financings, sources and terms |  |
| `exh:74.3` | A nuclear government support package (Illustrative) |  |
| `cl:74.1` | Political shutdown compensation, nuclear support agreement (sponsor-, lender-, government-friendly) |  |
| `eq:74.1` | Cost at COD from an even spend profile and a financing rate |  |
| `fw:nuclear-risk-bearer` | Framework 74.1 Nuclear risk-bearer map | home sec:74.3 |

### Chapter 75: Upstream and midstream oil and gas (incl. reserve-based lending)

Source brief: `briefs/u15.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:75` | Upstream and midstream oil and gas (incl. reserve-based lending) |  |
| `sec:75.1` | The economics of oil and gas fields |  |
| `ssec:75.1.1` | Phases and who funds them |  |
| `ssec:75.1.2` | Decline, price and the shape of field cash flow |  |
| `sec:75.2` | Fiscal regimes and the state's share |  |
| `ssec:75.2.1` | Concessions, royalties and taxes |  |
| `ssec:75.2.2` | Production sharing contracts |  |
| `ssec:75.2.3` | Fiscal terms and lenders |  |
| `sec:75.3` | Reserve-based lending |  |
| `ssec:75.3.1` | What an RBL is |  |
| `ssec:75.3.2` | Computing the borrowing base |  |
| `ssec:75.3.3` | Redetermination and deficiency |  |
| `ssec:75.3.4` | Hedging, LCs and decommissioning security |  |
| `ssec:75.3.5` | Other upstream financing |  |
| `sec:75.4` | Midstream assets and how they are paid |  |
| `ssec:75.4.1` | Pipelines, processing and storage |  |
| `ssec:75.4.2` | Ship-or-pay, cost of service and negotiated tariffs |  |
| `ssec:75.4.3` | The throughput credit test |  |
| `sec:75.5` | Cross-border pipelines |  |
| `ssec:75.5.1` | Two states, one asset |  |
| `ssec:75.5.2` | Chad–Cameroon: an equity-funded upstream and a project-financed export system |  |
| `ssec:75.5.3` | Sanctions on a pipeline: Nord Stream 2 |  |
| `sec:75.6` | Financing terms for upstream and midstream |  |
| `ssec:75.6.1` | RBL terms |  |
| `ssec:75.6.2` | Midstream terms |  |
| `sec:75.7` | Modeling upstream and midstream |  |
| `ssec:75.7.1` | Production, prices and the fiscal regime |  |
| `ssec:75.7.2` | The borrowing-base model |  |
| `ssec:75.7.3` | Pipeline throughput and tariff models |  |
| `sec:75.8` | Walkthrough: a borrowing-base redetermination from reserves report to new commitment |  |
| `sec:75.9` | Case P: Sombé West's lenders and the GCK pipeline |  |
| `sec:75.10` | Practitioner's notebook |  |
| `sec:75.11` | Judgment drill |  |
| `sec:75.12` | Upstream debt follows reserves and price and midstream debt follows shippers |  |
| `sec:75.13` | Exercises |  |
| `sec:75.14` | Solutions to exercises |  |
| `ex:75.1` | Computing a borrowing base |  |
| `ex:75.2` | A redetermination after the price deck falls |  |
| `ex:75.3` | Who takes what under a production sharing contract |  |
| `ex:75.4` | A cost-of-service pipeline tariff |  |
| `exh:75.1` | Upstream phases, risks and typical capital |  |
| `exh:75.2` | An oil and gas chain and its contracts (Illustrative) |  |
| `exh:75.3` | Upstream and midstream financing structures compared |  |
| `exh:75.4` | Redetermination timetable and documents (Illustrative) |  |
| `cl:75.1` | Borrowing-base redetermination and deficiency cure, RBL facility (sponsor-friendly, lender-friendly) |  |
| `eq:75.1` | Borrowing base as the minimum of the cover-ratio tests |  |
| `eq:75.2` | Cost-of-service revenue requirement |  |
| `fw:borrowing-base-walk` | Framework 75.1 Borrowing base walk | home ssec:75.3.2 |
| `fw:throughput-credit-test` | Framework 75.2 Throughput credit test | home ssec:75.4.3 |

### Chapter 76: LNG liquefaction, regasification and FPSOs

Source brief: `briefs/u15.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:76` | LNG liquefaction, regasification and FPSOs |  |
| `sec:76.1` | The economics of LNG |  |
| `ssec:76.1.1` | The chain and where the money goes |  |
| `ssec:76.1.2` | How LNG is priced |  |
| `ssec:76.1.3` | Contracting before FID |  |
| `sec:76.2` | Three ways to structure an LNG project |  |
| `ssec:76.2.1` | Integrated projects |  |
| `ssec:76.2.2` | Tolling and merchant liquefaction |  |
| `ssec:76.2.3` | The US fixed-fee model |  |
| `sec:76.3` | The SPA portfolio as collateral |  |
| `ssec:76.3.1` | Fixed fees, buyers and tenor |  |
| `ssec:76.3.2` | Cancellation rights and lenders |  |
| `ssec:76.3.3` | The LNG chain credit map |  |
| `sec:76.4` | Building an LNG plant |  |
| `ssec:76.4.1` | LSTK contracts and the few contractors who sign them |  |
| `ssec:76.4.2` | Cost growth and its anatomy |  |
| `ssec:76.4.3` | Completion guarantees and financial completion |  |
| `sec:76.5` | Country, security and sanctions risk |  |
| `ssec:76.5.1` | Mozambique LNG: force majeure, restart and re-documentation |  |
| `ssec:76.5.2` | Sanctions and LNG: Arctic LNG 2 |  |
| `sec:76.6` | Financing LNG |  |
| `ssec:76.6.1` | ECA-led mega-financings |  |
| `ssec:76.6.2` | US Gulf Coast bank mini-perms |  |
| `ssec:76.6.3` | Refinancing after completion |  |
| `sec:76.7` | Regasification terminals and FSRUs |  |
| `ssec:76.7.1` | Onshore terminals and terminal use agreements |  |
| `ssec:76.7.2` | FSRUs |  |
| `ssec:76.7.3` | Import-terminal credit |  |
| `sec:76.8` | FPSOs |  |
| `ssec:76.8.1` | What an FPSO is and who owns it |  |
| `ssec:76.8.2` | Day rates and the charter as collateral |  |
| `ssec:76.8.3` | Early termination and the lenders |  |
| `ssec:76.8.4` | The charter-backed credit test |  |
| `sec:76.9` | Modeling LNG and floating assets |  |
| `ssec:76.9.1` | SPA revenue and coverage tests |  |
| `ssec:76.9.2` | Completion timing and the guarantee release |  |
| `ssec:76.9.3` | Charter revenue |  |
| `sec:76.10` | Walkthrough: reading an LNG financing's completion test |  |
| `sec:76.11` | Case P: an FSRU for Bélanou Phase 2 |  |
| `sec:76.12` | Practitioner's notebook |  |
| `sec:76.13` | Judgment drill |  |
| `sec:76.14` | LNG debt rests on contracts signed before the first concrete |  |
| `sec:76.15` | Exercises |  |
| `sec:76.16` | Solutions to exercises |  |
| `ex:76.1` | Fixed-fee coverage of a liquefaction project |  |
| `ex:76.2` | How much must be contracted before FID |  |
| `ex:76.3` | Financing an FPSO on its charter |  |
| `ex:76.4` | FSRU or onshore regasification |  |
| `exh:76.1` | The LNG chain and its contracts (Illustrative) |  |
| `exh:76.2` | Three LNG project structures compared |  |
| `exh:76.3` | LNG financings compared |  |
| `exh:76.4` | Completion test schedule for an integrated LNG project (Illustrative) |  |
| `cl:76.1` | Early termination fee, FPSO lease-and-operate contract (sponsor-, lender-, charterer-friendly) |  |
| `fw:lng-chain-credit` | Framework 76.1 LNG chain credit map | home ssec:76.3.3 |
| `fw:charter-credit-test` | Framework 76.2 Charter-backed credit test | home ssec:76.8.4 |

### Chapter 77: Refining, petrochemicals and manufacturing (gigafactory) finance

Source brief: `briefs/u16.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:77` | Refining, petrochemicals and manufacturing (gigafactory) finance |  |
| `sec:77.1` | Plants that earn a spread |  |
| `ssec:77.1.1` | Revenue that is a difference between two prices |  |
| `ssec:77.1.2` | Three plant types and what they share |  |
| `ssec:77.1.3` | Who sponsors industrial plants and why they borrow non-recourse |  |
| `sec:77.2` | Refining economics |  |
| `ssec:77.2.1` | Crack spreads and the gross refining margin |  |
| `ssec:77.2.2` | Configuration and complexity |  |
| `ssec:77.2.3` | Capture rate and why realized margins trail the benchmark |  |
| `sec:77.3` | Petrochemical economics |  |
| `ssec:77.3.1` | Feedstock advantage |  |
| `ssec:77.3.2` | Integration and co-products |  |
| `ssec:77.3.3` | The capacity-wave cycle |  |
| `sec:77.4` | Factory economics |  |
| `ssec:77.4.1` | Throughput, yield and scrap |  |
| `ssec:77.4.2` | Learning curves against price deflation |  |
| `ssec:77.4.3` | Customer contracts and the difference between orders and take-or-pay |  |
| `sec:77.5` | Protecting the margin |  |
| `ssec:77.5.1` | The margin protection ladder |  |
| `ssec:77.5.2` | Processing fees against merchant margins |  |
| `ssec:77.5.3` | Who pays for protection |  |
| `sec:77.6` | Key risks |  |
| `ssec:77.6.1` | Completion and ramp-up in multi-unit plants |  |
| `ssec:77.6.2` | Feedstock and utilities |  |
| `ssec:77.6.3` | Technology and licensing |  |
| `ssec:77.6.4` | Market, customer and policy risk |  |
| `ssec:77.6.5` | Supply chain and geopolitics |  |
| `sec:77.7` | The contract set |  |
| `ssec:77.7.1` | The industrial contract map |  |
| `ssec:77.7.2` | Technology license and process guarantee |  |
| `ssec:77.7.3` | Feedstock supply, marketing and lifting agreements |  |
| `ssec:77.7.4` | Construction for a complex: EPC packages, EPCM and the wrap |  |
| `ssec:77.7.5` | Sponsor completion support for industrial plants |  |
| `sec:77.8` | Typical financing terms |  |
| `ssec:77.8.1` | Verified anchors |  |
| `ssec:77.8.2` | Indicative ranges and their drivers |  |
| `ssec:77.8.3` | Covenants that matter more here |  |
| `sec:77.9` | Modeling an industrial plant |  |
| `ssec:77.9.1` | Joint price decks and margin correlation |  |
| `ssec:77.9.2` | Throughput and yield ramp curves |  |
| `ssec:77.9.3` | Working capital, turnarounds and maintenance capex |  |
| `sec:77.10` | Sadara and the limits of sponsor support |  |
| `sec:77.11` | Northvolt Ett and the factory financed like a power plant |  |
| `sec:77.12` | Walkthrough: testing a petrochemical complex for completion |  |
| `sec:77.13` | Case P: Groupe Talmé's fertilizer plan |  |
| `sec:77.14` | Practitioner's notebook |  |
| `sec:77.15` | Judgment drill |  |
| `sec:77.16` | A margin needs an owner before it needs a lender |  |
| `sec:77.17` | Exercises |  |
| `sec:77.18` | Solutions to exercises |  |
| `ex:77.1` | Crack spread and refinery EBITDA |  |
| `ex:77.2` | Ethane against naphtha cracker margins |  |
| `ex:77.3` | Processing fee against merchant sale for a urea plant |  |
| `ex:77.4` | Gigafactory ramp, yield and breakeven |  |
| `ex:77.5` | Reading a reliability-run result against a three-envelope completion test |  |
| `exh:77.1` | Refinery process flow (Illustrative) |  |
| `exh:77.2` | Contract map for an integrated petrochemical complex (Illustrative) |  |
| `exh:77.3` | Verified financing terms for industrial project financings |  |
| `exh:77.4` | Northvolt capital structure at the Chapter 11 petition date (Real case) |  |
| `cl:77.1` | Process performance guarantee and remedy, technology license agreement (Illustrative) |  |
| `cl:77.2` | Project completion test schedule for a multi-unit complex (Illustrative) |  |
| `eq:77.1` | 3-2-1 crack spread |  |
| `eq:77.2` | Cash cost per good unit |  |
| `eq:77.3` | Breakeven yield |  |
| `fw:margin-ladder` | Framework 77.1 Margin protection ladder | home ssec:77.5.1 |

### Chapter 78: Mining, metals and critical minerals

Source brief: `briefs/u16.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:78` | Mining, metals and critical minerals |  |
| `sec:78.1` | How mines make and lose money |  |
| `ssec:78.1.1` | Price takers on a cost curve |  |
| `ssec:78.1.2` | Grade, strip ratio and recovery |  |
| `ssec:78.1.3` | Cycles, capital intensity and who borrows non-recourse |  |
| `sec:78.2` | Critical minerals |  |
| `ssec:78.2.1` | What makes a mineral critical for a lender |  |
| `ssec:78.2.2` | Pricing without a deep terminal market |  |
| `ssec:78.2.3` | Processing plants as manufacturing credits |  |
| `ssec:78.2.4` | Public money in critical minerals |  |
| `sec:78.3` | What a lender needs to know about the mine itself |  |
| `ssec:78.3.1` | From deposit to payable metal |  |
| `ssec:78.3.2` | Infrastructure, power and water |  |
| `ssec:78.3.3` | Tailings, closure and care and maintenance |  |
| `sec:78.4` | Revenue models and funding from the offtake side |  |
| `ssec:78.4.1` | Concentrate, cathode and metal sales |  |
| `ssec:78.4.2` | Offtake-linked finance and prepayments |  |
| `ssec:78.4.3` | Streams and royalties as construction capital |  |
| `sec:78.5` | Key risks |  |
| `ssec:78.5.1` | Geology and geotechnics |  |
| `ssec:78.5.2` | Metallurgy and ramp-up |  |
| `ssec:78.5.3` | Price, by-products and currency |  |
| `ssec:78.5.4` | Fiscal terms and resource nationalism |  |
| `ssec:78.5.5` | The legal foundation of the right to mine |  |
| `ssec:78.5.6` | Social licence |  |
| `sec:78.6` | The contract set |  |
| `ssec:78.6.1` | Host agreements and stability |  |
| `ssec:78.6.2` | State carried interests and who funds them |  |
| `ssec:78.6.3` | EPCM, owner's team and construction packages |  |
| `ssec:78.6.4` | Offtake, stream, infrastructure access and closure bonding |  |
| `sec:78.7` | Structuring and sizing mining debt |  |
| `ssec:78.7.1` | Bank price decks |  |
| `ssec:78.7.2` | Reserve tail and tenor |  |
| `ssec:78.7.3` | The four-part completion test |  |
| `ssec:78.7.4` | Multi-source structures and debt caps |  |
| `ssec:78.7.5` | Indicative terms and their drivers |  |
| `sec:78.8` | Modeling a mine |  |
| `ssec:78.8.1` | The mine-plan chain |  |
| `ssec:78.8.2` | Price decks, by-products and FX in the model |  |
| `ssec:78.8.3` | Closure, sustaining capex and royalty variants |  |
| `sec:78.9` | Oyu Tolgoi and multi-source mining finance under a demanding host |  |
| `sec:78.10` | Cobre Panamá and the mine that lost its legal foundation |  |
| `sec:78.11` | Walkthrough: marking up a mining completion test |  |
| `sec:78.12` | Case P: a bauxite developer asks for power |  |
| `sec:78.13` | Practitioner's notebook |  |
| `sec:78.14` | Judgment drill |  |
| `sec:78.15` | A mine is a wasting asset with a political half-life |  |
| `sec:78.16` | Exercises |  |
| `sec:78.17` | Solutions to exercises |  |
| `ex:78.1` | C1 and AISC for a copper-gold mine |  |
| `ex:78.2` | Reserve tail and maximum tenor |  |
| `ex:78.3` | Sizing on a bank price deck and testing a downside |  |
| `ex:78.4` | The cost of a gold stream as construction capital |  |
| `ex:78.5` | Testing a completion result |  |
| `exh:78.1` | Industry cost curve with the example mine (Illustrative) |  |
| `exh:78.2` | From deposit to payable metal (Illustrative) |  |
| `exh:78.3` | Contract map of a limited-recourse copper-gold mine (Illustrative) |  |
| `exh:78.4` | Oyu Tolgoi reported tranche structure, December 2015 (Real case) |  |
| `cl:78.1` | Fiscal stability, mining investment agreement (variants cl:78.1a sponsor-friendly, cl:78.1b lender-friendly, cl:78.1c government-friendly) |  |
| `cl:78.1a` | sponsor-friendly, cl:78.1b lender-friendly, cl:78.1c government-friendly |  |
| `cl:78.1b` | lender-friendly, cl:78.1c government-friendly |  |
| `cl:78.1c` | government-friendly |  |
| `cl:78.2` | Completion test schedule, mining facility agreement (Illustrative) |  |
| `eq:78.1` | Maximum tenor from reserve tail |  |
| `eq:78.2` | C1 cash cost per pound |  |
| `eq:78.3` | All-in sustaining cost per pound |  |
| `fw:four-part-completion` | Framework 78.1 Four-part completion test | home ssec:78.7.3 |
| `fw:deck-tail-test` | Framework 78.2 Deck-tail-test triangle | home ssec:78.7.3 |

### Chapter 79: Toll roads, bridges and tunnels (Case T ramp-up)

Source brief: `briefs/u16.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:79` | Toll roads, bridges and tunnels (Case T ramp-up) |  |
| `sec:79.1` | What a toll road sells |  |
| `ssec:79.1.1` | Value of time and willingness to pay |  |
| `ssec:79.1.2` | Elasticity and the revenue-maximizing toll |  |
| `ssec:79.1.3` | Greenfield and brownfield |  |
| `ssec:79.1.4` | Networks, free alternatives and promised public works |  |
| `sec:79.2` | Bridges and tunnels |  |
| `ssec:79.2.1` | Monopoly crossings and captive demand |  |
| `ssec:79.2.2` | Ground risk and how to share it |  |
| `ssec:79.2.3` | Safety systems, lifecycle and regulation after close |  |
| `sec:79.3` | How roads earn revenue |  |
| `ssec:79.3.1` | Real tolls, shadow tolls, availability and hybrids |  |
| `ssec:79.3.2` | Managed lanes and dynamic pricing |  |
| `ssec:79.3.3` | Free-flow tolling, class mix and leakage |  |
| `sec:79.4` | Sharing demand risk |  |
| `ssec:79.4.1` | Minimum revenue guarantees and revenue-sharing bands |  |
| `ssec:79.4.2` | Flexible-term concessions |  |
| `ssec:79.4.3` | Rebalancing and term extension |  |
| `ssec:79.4.4` | Choosing a structure |  |
| `sec:79.5` | Ramp-up and how it fails |  |
| `ssec:79.5.1` | Timing shortfalls and structural shortfalls |  |
| `ssec:79.5.2` | Catch-up arithmetic |  |
| `ssec:79.5.3` | The record |  |
| `sec:79.6` | The contract set |  |
| `ssec:79.6.1` | The road contract map |  |
| `ssec:79.6.2` | Competing facilities and network change |  |
| `ssec:79.6.3` | Toll regime, tolling back office and enforcement |  |
| `ssec:79.6.4` | Relief events and pandemic outcomes |  |
| `sec:79.7` | Typical financing terms |  |
| `ssec:79.7.1` | Verified anchors |  |
| `ssec:79.7.2` | Indicative ranges and their drivers |  |
| `ssec:79.7.3` | Structures that turn traffic risk into refinancing risk |  |
| `sec:79.8` | Modeling a road for lenders |  |
| `ssec:79.8.1` | From trips to toll revenue |  |
| `ssec:79.8.2` | Linking tolls to traffic |  |
| `ssec:79.8.3` | Lifecycle, handback and tunnel systems |  |
| `sec:79.9` | SH 130 and the Indiana Toll Road, two roads to Chapter 11 |  |
| `sec:79.10` | Sydney's tunnels and the outlier forecast |  |
| `sec:79.11` | Eurotunnel and the Greenway, when the market is smaller than the forecast |  |
| `sec:79.12` | Colombia's 4G program and how a template made demand risk bankable |  |
| `sec:79.13` | Walkthrough: diagnosing a ramp-up shortfall from the first year of transaction data |  |
| `sec:79.14` | Case T: the Merrick Link ramp-up, 2019 to 2025 |  |
| `sec:79.15` | Practitioner's notebook |  |
| `sec:79.16` | Judgment drill |  |
| `sec:79.17` | Drivers choose; lenders can only price the choice |  |
| `sec:79.18` | Exercises |  |
| `sec:79.19` | Solutions to exercises |  |
| `ex:79.1` | Willingness to pay and diversion |  |
| `ex:79.2` | A toll cut at two elasticities |  |
| `ex:79.3` | Minimum revenue guarantee with a revenue-sharing band |  |
| `ex:79.4` | Least present value of revenue |  |
| `ex:79.5` | Revenue build and the cost of losing trucks |  |
| `ex:79.6` | Catch-up arithmetic |  |
| `exh:79.1` | Port of Miami Tunnel geotechnical risk-sharing band (Real case) |  |
| `exh:79.2` | Toll-road ramp-up failures compared (Real cases) |  |
| `exh:79.3` | Contract map of a user-pay road concession (Illustrative) |  |
| `exh:79.4` | Verified financing terms for toll roads and tunnels |  |
| `exh:79.5` | First-year transaction data against the banking case (Illustrative) |  |
| `exh:79.6` | Merrick Link traffic, forecast and actual (Case T, T-F04) |  |
| `exh:79.7` | Merrick Link traffic ramp-up chart (Case T, T-F04) |  |
| `exh:79.8` | Merrick Link revenue ramp-up, forecast against actual (Case T, T-F06) |  |
| `cl:79.1` | Competing facilities, concession deed (variants cl:79.1a sponsor-friendly, cl:79.1b lender-friendly, cl:79.1c government-friendly) |  |
| `cl:79.1a` | sponsor-friendly, cl:79.1b lender-friendly, cl:79.1c government-friendly |  |
| `cl:79.1b` | lender-friendly, cl:79.1c government-friendly |  |
| `cl:79.1c` | government-friendly |  |
| `eq:79.1` | Binary logit share of the tolled route |  |
| `eq:79.2` | Years for actual traffic to converge with forecast |  |
| `eq:79.3` | Constant-elasticity traffic response to a toll change |  |
| `fw:demand-risk-menu` | Framework 79.1 Demand-risk sharing menu for toll roads | home ssec:79.4.4 |
| `fw:ramp-up-diagnosis` | Framework 79.2 Ramp-up diagnosis | home ssec:79.5.1 |

### Chapter 80: Rail, urban transit, airports and ports

Source brief: `briefs/u16.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:80` | Rail, urban transit, airports and ports |  |
| `sec:80.1` | Who pays for a train |  |
| `ssec:80.1.1` | Farebox recovery and the public budget |  |
| `ssec:80.1.2` | Four ways to contract a railway |  |
| `ssec:80.1.3` | Interfaces that break rail projects |  |
| `ssec:80.1.4` | Rolling stock finance |  |
| `sec:80.2` | Airports |  |
| `ssec:80.2.1` | Two businesses under one roof |  |
| `ssec:80.2.2` | Single till and dual till | ruling: Choosing a till and a price cap (retitled, R-050) |
| `ssec:80.2.3` | Privatizations, concessions and terminal PPPs |  |
| `sec:80.3` | Ports |  |
| `ssec:80.3.1` | Landlord, tool and service ports |  |
| `ssec:80.3.2` | Terminals and the shipping lines that choose them |  |
| `ssec:80.3.3` | Concession fees and the minimum annual guarantee |  |
| `sec:80.4` | Footloose demand |  |
| `ssec:80.4.1` | The footloose-demand test |  |
| `ssec:80.4.2` | What lenders do with a footloose score |  |
| `sec:80.5` | Key risks |  |
| `ssec:80.5.1` | Demand shocks |  |
| `ssec:80.5.2` | Construction interfaces and cost growth |  |
| `ssec:80.5.3` | Supply-chain governance |  |
| `ssec:80.5.4` | Regulatory resets and counterparty concentration |  |
| `sec:80.6` | The contract set |  |
| `ssec:80.6.1` | Transit availability PPP |  |
| `ssec:80.6.2` | Airport concession |  |
| `ssec:80.6.3` | Port terminal concession |  |
| `sec:80.7` | Typical financing terms |  |
| `ssec:80.7.1` | What the verified record shows |  |
| `ssec:80.7.2` | Indicative ranges and their drivers |  |
| `ssec:80.7.3` | Structures that match the sector |  |
| `sec:80.8` | Modeling specifics |  |
| `ssec:80.8.1` | Passengers, yield and commercial revenue |  |
| `ssec:80.8.2` | Throughput, MAG and fees |  |
| `ssec:80.8.3` | Rail performance regimes and fleet lifecycle |  |
| `sec:80.9` | Metronet and Tube Lines, same contract and different supply chains |  |
| `sec:80.10` | The Purple Line and the 365-day exit |  |
| `sec:80.11` | Rail contracts in the pandemic and the end of revenue risk |  |
| `sec:80.12` | Walkthrough: reading a container terminal concession agreement |  |
| `sec:80.13` | Case T: Brannock procures a light-rail line |  |
| `sec:80.14` | Practitioner's notebook |  |
| `sec:80.15` | Judgment drill |  |
| `sec:80.16` | Demand that belongs to someone else's network |  |
| `sec:80.17` | Exercises |  |
| `sec:80.18` | Solutions to exercises |  |
| `ex:80.1` | Single till against dual till |  |
| `ex:80.2` | A container terminal's minimum annual guarantee |  |
| `ex:80.3` | Farebox recovery of a light-rail line |  |
| `ex:80.4` | Leasing a fleet with a residual value |  |
| `ex:80.5` | An airport through a passenger shock |  |
| `exh:80.1` | Four ways to contract a railway and who carries each risk (Illustrative) |  |
| `exh:80.2` | Footloose-demand scores for five transport assets (Illustrative) |  |
| `exh:80.3` | Term sheet of a container terminal concession (Illustrative) |  |
| `cl:80.1` | Minimum annual guarantee, port terminal concession agreement (variants cl:80.1a sponsor-friendly, cl:80.1b lender-friendly, cl:80.1c port-authority-friendly) |  |
| `cl:80.1a` | sponsor-friendly, cl:80.1b lender-friendly, cl:80.1c port-authority-friendly |  |
| `cl:80.1b` | lender-friendly, cl:80.1c port-authority-friendly |  |
| `cl:80.1c` | port-authority-friendly |  |
| `eq:80.1` | Single-till charge per passenger |  |
| `eq:80.2` | Dual-till aeronautical charge per passenger |  |
| `eq:80.3` | Farebox recovery ratio |  |
| `fw:footloose-demand` | Framework 80.1 Footloose-demand test | home ssec:80.4.1 |

### Chapter 81: Social infrastructure, water, desalination and waste-to-energy

Source brief: `briefs/u16.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:81` | Social infrastructure, water, desalination and waste-to-energy |  |
| `sec:81.1` | What the state buys when it buys a building |  |
| `ssec:81.1.1` | Accommodation and services, not outcomes |  |
| `ssec:81.1.2` | Why availability credit carries high gearing and thin cover |  |
| `ssec:81.1.3` | Hard FM, soft FM, lifecycle and equipment |  |
| `ssec:81.1.4` | The thin-equity problem |  |
| `sec:81.2` | Water and wastewater |  |
| `ssec:81.2.1` | Concessions, treatment-plant BOTs and regulated utilities |  |
| `ssec:81.2.2` | Tariffs, affordability, collection and non-revenue water |  |
| `ssec:81.2.3` | Carving a project out of a utility |  |
| `sec:81.3` | Desalination |  |
| `ssec:81.3.1` | Reverse osmosis, thermal plants and energy |  |
| `ssec:81.3.2` | The water purchase agreement |  |
| `ssec:81.3.3` | Decoupling water from power |  |
| `sec:81.4` | Waste-to-energy |  |
| `ssec:81.4.1` | Three revenue lines and two cost lines |  |
| `ssec:81.4.2` | Waste supply and calorific value |  |
| `ssec:81.4.3` | Technology, emissions and permits |  |
| `sec:81.5` | Risks that remain when payment is certain |  |
| `ssec:81.5.1` | The payment-chain trace |  |
| `ssec:81.5.2` | Construction and contractor credit |  |
| `ssec:81.5.3` | Performance, deductions and passdown |  |
| `ssec:81.5.4` | Pandemic and payment continuity |  |
| `ssec:81.5.5` | Political and affordability risk in water |  |
| `sec:81.6` | The contract set |  |
| `ssec:81.6.1` | Social infrastructure project agreement and subcontracts |  |
| `ssec:81.6.2` | Water purchase and energy supply agreements |  |
| `ssec:81.6.3` | Waste supply, power sale and residue contracts |  |
| `sec:81.7` | Typical financing terms |  |
| `ssec:81.7.1` | Verified anchors |  |
| `ssec:81.7.2` | Indicative ranges and their drivers |  |
| `ssec:81.7.3` | Refinancing and gain sharing |  |
| `sec:81.8` | Modeling specifics |  |
| `ssec:81.8.1` | Lifecycle and deductions |  |
| `ssec:81.8.2` | Water volumes, availability and energy |  |
| `ssec:81.8.3` | Waste tonnage, calorific value and thermal capacity |  |
| `sec:81.9` | Carillion's hospitals and the limits of risk transfer |  |
| `sec:81.10` | Thames Tideway and the carve-out from a utility |  |
| `sec:81.11` | Gulf desalination and the price of competition |  |
| `sec:81.12` | Walkthrough: a desalination water purchase agreement tariff schedule |  |
| `sec:81.13` | Case T: Brannock's availability hospital |  |
| `sec:81.14` | Practitioner's notebook |  |
| `sec:81.15` | Judgment drill |  |
| `sec:81.16` | Certain payment moves risk; it does not remove it |  |
| `sec:81.17` | Exercises |  |
| `sec:81.18` | Solutions to exercises |  |
| `ex:81.1` | Gearing and cover in a hospital availability PPP |  |
| `ex:81.2` | Building a desalination tariff |  |
| `ex:81.3` | A waste-to-energy plant's revenue stack |  |
| `ex:81.4` | Non-revenue water and cash revenue |  |
| `ex:81.5` | Cost to complete after a contractor fails |  |
| `exh:81.1` | Water sector models and who carries each risk (Illustrative) |  |
| `exh:81.2` | Saudi independent water project tariffs, 2009 to 2026 (Real case: Sharakat program) |  |
| `exh:81.3` | Payment-chain traces for four assets (Illustrative) |  |
| `exh:81.4` | Contract map of an availability hospital PPP (Illustrative) |  |
| `exh:81.5` | Tariff schedule of a reverse-osmosis water purchase agreement (Illustrative) |  |
| `cl:81.1` | Capacity charge and availability, water purchase agreement (Illustrative) |  |
| `cl:81.2` | Put-or-pay, waste supply agreement (variants cl:81.2a sponsor-friendly, cl:81.2b lender-friendly, cl:81.2c municipality-friendly) |  |
| `cl:81.2a` | sponsor-friendly, cl:81.2b lender-friendly, cl:81.2c municipality-friendly |  |
| `cl:81.2b` | lender-friendly, cl:81.2c municipality-friendly |  |
| `cl:81.2c` | municipality-friendly |  |
| `eq:81.1` | Desalination tariff as capacity charge plus output charge |  |
| `eq:81.2` | WtE electricity output from tonnage, calorific value and efficiency |  |
| `eq:81.3` | Tonnage cap from thermal capacity |  |
| `fw:payment-chain` | Framework 81.1 Payment-chain trace | home ssec:81.5.1 |

### Chapter 82: Telecoms, fiber, towers and data centers

Source brief: `briefs/u16.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:82` | Telecoms, fiber, towers and data centers |  |
| `sec:82.1` | Infrastructure that ages like technology |  |
| `ssec:82.1.1` | What makes digital assets financeable |  |
| `ssec:82.1.2` | Four asset types and their payers |  |
| `sec:82.2` | Towers |  |
| `ssec:82.2.1` | Tenancy and the economics of sharing |  |
| `ssec:82.2.2` | Master lease agreements and carve-outs |  |
| `ssec:82.2.3` | Consolidation, network sharing and technology |  |
| `sec:82.3` | Fiber |  |
| `ssec:82.3.1` | Backbone, metro and FTTH |  |
| `ssec:82.3.2` | Penetration, ARPU and overbuild |  |
| `ssec:82.3.3` | Wholesale open access and subsidy programs |  |
| `sec:82.4` | Data centers |  |
| `ssec:82.4.1` | Hyperscale, colocation and edge |  |
| `ssec:82.4.2` | Power is the constraint |  |
| `ssec:82.4.3` | Leases, tenants and tenor |  |
| `ssec:82.4.4` | Lending against compute |  |
| `sec:82.5` | Key risks |  |
| `ssec:82.5.1` | The lease-life gap test |  |
| `ssec:82.5.2` | Tenant concentration and credit |  |
| `ssec:82.5.3` | Power, cooling and water |  |
| `ssec:82.5.4` | Overbuild and residual value |  |
| `sec:82.6` | The contract set |  |
| `ssec:82.6.1` | Towers and fiber contracts |  |
| `ssec:82.6.2` | Data-center contracts |  |
| `ssec:82.6.3` | Residual value guarantee clause |  |
| `sec:82.7` | Typical financing terms |  |
| `ssec:82.7.1` | Verified anchors |  |
| `ssec:82.7.2` | Towers and fiber |  |
| `ssec:82.7.3` | Securitization and whole-business structures |  |
| `sec:82.8` | Modeling specifics |  |
| `ssec:82.8.1` | Lease-up and tenancy curves |  |
| `ssec:82.8.2` | Penetration, churn and ARPU |  |
| `ssec:82.8.3` | Power pass-through, refresh capex and residual value |  |
| `sec:82.9` | Hyperion and the short lease with a long guarantee |  |
| `sec:82.10` | Walkthrough: reading a hyperscale data-center lease for lenders |  |
| `sec:82.11` | Case R: Ostrander Data Systems as a power buyer |  |
| `sec:82.12` | Practitioner's notebook |  |
| `sec:82.13` | Judgment drill |  |
| `sec:82.14` | The lease is short, the building is long, the power is scarce |  |
| `sec:82.15` | Exercises |  |
| `sec:82.16` | Solutions to exercises |  |
| `ex:82.1` | Tower margins as tenancy rises |  |
| `ex:82.2` | An FTTH network through its penetration ramp |  |
| `ex:82.3` | Sizing data-center debt against a long lease and against a short lease with an RVG |  |
| `ex:82.4` | Power cost and PUE |  |
| `exh:82.1` | Four digital asset types and their payers (Illustrative) |  |
| `exh:82.2` | Lease-life gap timelines for four assets (Illustrative) |  |
| `exh:82.3` | Contract map of a hyperscale build-to-suit joint venture (Illustrative) |  |
| `exh:82.4` | Verified data-center financing terms, 2024 to 2026 |  |
| `exh:82.5` | Summary of a hyperscale data-center lease (Illustrative) |  |
| `cl:82.1` | Residual value guarantee, data-center lease (Illustrative) |  |
| `eq:82.1` | Tenancy ratio and tower EBITDA |  |
| `eq:82.2` | Data-center energy use from IT load, load factor and PUE |  |
| `eq:82.3` | Maximum debt with a balloon capped by an RVG |  |
| `fw:lease-life-gap` | Framework 82.1 Lease-life gap test | home ssec:82.5.1 |

### Chapter 83: Hydrogen and derivatives, carbon capture and storage, sustainable fuels

Source brief: `briefs/u16.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:83` | Hydrogen and derivatives, carbon capture and storage, sustainable fuels |  |
| `sec:83.1` | Selling a product that has no market price |  |
| `ssec:83.1.1` | Policy-made demand |  |
| `ssec:83.1.2` | Where the market stands |  |
| `sec:83.2` | Hydrogen and its derivatives |  |
| `ssec:83.2.1` | Electrolysis and the levelized cost of hydrogen |  |
| `ssec:83.2.2` | Ammonia, methanol and fuels as carriers |  |
| `ssec:83.2.3` | Revenue models for hydrogen |  |
| `ssec:83.2.4` | Power supply and shape |  |
| `sec:83.3` | Carbon capture and storage |  |
| `ssec:83.3.1` | The chain and its interfaces |  |
| `ssec:83.3.2` | Who pays to store carbon |  |
| `ssec:83.3.3` | Three business models |  |
| `ssec:83.3.4` | Storage liability |  |
| `sec:83.4` | Sustainable fuels |  |
| `ssec:83.4.1` | Pathways and feedstocks |  |
| `ssec:83.4.2` | The revenue stack |  |
| `ssec:83.4.3` | Feedstock contracts and offtake by airlines |  |
| `sec:83.5` | Who holds the market risk |  |
| `ssec:83.5.1` | The market-risk holder trace |  |
| `ssec:83.5.2` | Role concentration |  |
| `ssec:83.5.3` | First-of-a-kind and cost risk |  |
| `sec:83.6` | The contract set |  |
| `ssec:83.6.1` | Molecule offtake agreements |  |
| `ssec:83.6.2` | Power, electrolyzer and integration contracts |  |
| `ssec:83.6.3` | CO2 transport and storage agreements and government support contracts |  |
| `sec:83.7` | Typical financing terms |  |
| `ssec:83.7.1` | What the verified deals show |  |
| `ssec:83.7.2` | Why there are no market norms yet |  |
| `sec:83.8` | Modeling specifics |  |
| `ssec:83.8.1` | Power profile and electrolyzer utilization |  |
| `ssec:83.8.2` | Degradation, stack replacement and conversion |  |
| `ssec:83.8.3` | Support payments, credits and chain volumes |  |
| `sec:83.9` | NEOM Green Hydrogen and the offtaker as the credit |  |
| `sec:83.10` | Northern Lights and the state as chain integrator |  |
| `sec:83.11` | Walkthrough: marking up a hydrogen offtake term sheet |  |
| `sec:83.12` | Case R: Lattimer passes on a hydrogen offtake |  |
| `sec:83.13` | Practitioner's notebook |  |
| `sec:83.14` | Judgment drill |  |
| `sec:83.15` | Someone must agree to pay before anyone can lend |  |
| `sec:83.16` | Exercises |  |
| `sec:83.17` | Solutions to exercises |  |
| `ex:83.1` | Levelized cost of hydrogen |  |
| `ex:83.2` | From hydrogen to ammonia |  |
| `ex:83.3` | A hydrogen CfD and volume risk |  |
| `ex:83.4` | Cross-chain stranding in CCS |  |
| `ex:83.5` | A SAF plant's revenue stack |  |
| `exh:83.1` | The CCS chain (Illustrative) |  |
| `exh:83.2` | Market-risk holder traces for four projects (Illustrative and Real cases, labeled by column) |  |
| `exh:83.3` | Contract map of a UK-style CCS cluster (Illustrative) |  |
| `exh:83.4` | Verified financing facts for NEOM Green Hydrogen and Northern Lights (Real cases) |  |
| `exh:83.5` | Term sheet of a green ammonia offtake (Illustrative) |  |
| `cl:83.1` | Offtake obligation, ammonia sale agreement (variants cl:83.1a producer-friendly, cl:83.1b lender-friendly, cl:83.1c offtaker-friendly) |  |
| `cl:83.1a` | producer-friendly, cl:83.1b lender-friendly, cl:83.1c offtaker-friendly |  |
| `cl:83.1b` | lender-friendly, cl:83.1c offtaker-friendly |  |
| `cl:83.1c` | offtaker-friendly |  |
| `eq:83.1` | Levelized cost of hydrogen |  |
| `eq:83.2` | Hydrogen output from electrolyzer capacity, capacity factor and efficiency |  |
| `eq:83.3` | CfD difference payment on sold volume |  |
| `fw:market-risk-trace` | Framework 83.1 Market-risk holder trace | home ssec:83.5.1 |

### Chapter 84: Sustainable finance and climate risk

Source brief: `briefs/u14.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:84` | Sustainable finance and climate risk |  |
| `sec:84.1` | Who sets a label, what it certifies, and who checks it |  |
| `ssec:84.1.1` | Voluntary principles and legislated standards |  |
| `ssec:84.1.2` | The three-question label test |  |
| `ssec:84.1.3` | Market size and who buys |  |
| `sec:84.2` | Use-of-proceeds loans and bonds |  |
| `ssec:84.2.1` | The four core components |  |
| `ssec:84.2.2` | Making a project financing green |  |
| `ssec:84.2.3` | Mixed portfolios and allocation |  |
| `ssec:84.2.4` | Social, sustainability, blue and nature labels |  |
| `sec:84.3` | The EU Taxonomy and the European Green Bond Standard |  |
| `ssec:84.3.1` | How the Taxonomy defines "environmentally sustainable" |  |
| `ssec:84.3.2` | The 2026 simplification |  |
| `ssec:84.3.3` | The European Green Bond |  |
| `ssec:84.3.4` | When a project should use the EuGB label |  |
| `sec:84.4` | Sustainability-linked loans and bonds |  |
| `ssec:84.4.1` | How the instruments work |  |
| `ssec:84.4.2` | Choosing KPIs and setting targets |  |
| `ssec:84.4.3` | The economics of a margin ratchet |  |
| `ssec:84.4.4` | Why sustainability-linked structures fit platforms better than single projects |  |
| `sec:84.5` | Transition finance |  |
| `ssec:84.5.1` | The problem transition labels address |  |
| `ssec:84.5.2` | The Climate Transition Bond Guidelines |  |
| `ssec:84.5.3` | Transition loans |  |
| `ssec:84.5.4` | Export credit and transition |  |
| `sec:84.6` | Climate risk in the credit case |  |
| `ssec:84.6.1` | Physical risk as hazard, exposure and vulnerability |  |
| `ssec:84.6.2` | Chronic risk in operating numbers |  |
| `ssec:84.6.3` | Transition risk from policy, technology, markets and reputation |  |
| `ssec:84.6.4` | Scenarios and the downside case |  |
| `ssec:84.6.5` | Climate disclosure from TCFD to ISSB |  |
| `ssec:84.6.6` | The project climate risk screen |  |
| `sec:84.7` | Carbon markets and project revenue |  |
| `ssec:84.7.1` | Compliance and voluntary markets |  |
| `ssec:84.7.2` | Article 6 of the Paris Agreement |  |
| `ssec:84.7.3` | Additionality and over-crediting |  |
| `ssec:84.7.4` | Carbon revenue in a project's base case |  |
| `sec:84.8` | Greenwashing risk |  |
| `ssec:84.8.1` | How a label fails |  |
| `ssec:84.8.2` | Contractual consequences |  |
| `ssec:84.8.3` | Regulatory, reputational and refinancing consequences |  |
| `sec:84.9` | Labeled project financings at NEOM, Tideway and Baltic Power |  |
| `sec:84.10` | The ICVCM's renewable decision and the first Article 6.4 credits |  |
| `sec:84.11` | Walkthrough: reading a green financing framework and its second-party opinion |  |
| `sec:84.12` | Case R and Case P: a green private placement and a bond that could not be green |  |
| `sec:84.13` | Practitioner's notebook |  |
| `sec:84.14` | Judgment drill |  |
| `sec:84.15` | Labels describe the debt; the screen decides the deal |  |
| `sec:84.16` | Exercises |  |
| `sec:84.17` | Solutions to exercises |  |
| `ex:84.1` | Allocating a green bond's proceeds and testing the EuGB rule (Illustrative) |  |
| `ex:84.2` | The economics of a sustainability-linked margin ratchet (Illustrative) |  |
| `ex:84.3` | Expected annual flood loss today and in 2050 (Illustrative) |  |
| `ex:84.4` | Cooling-water temperature and a coastal CCGT's output (Illustrative) |  |
| `ex:84.5` | What a carbon price does to a CCGT's costs (Illustrative) |  |
| `ex:84.6` | Carbon credit revenue under Article 6.4 (Illustrative) |  |
| `ex:84.7` | Case R's green notes and Case P's unlabeled bond (Case R, Case P) |  |
| `exh:84.1` | Five sustainable debt labels under the three-question test (as of October 3, 2026) |  |
| `exh:84.2` | EU Taxonomy tests applied to a wind farm, a battery and a CCGT (Illustrative) |  |
| `exh:84.3` | Loss-exceedance curve for a coastal plant, today and in 2050 (USD m) (Illustrative) |  |
| `exh:84.4` | Carbon cost for a CCGT at three carbon prices (Illustrative) |  |
| `exh:84.5` | Article 6.2 and 6.4 compared |  |
| `cl:84.1` | (caption not stated in brief; writer supplies) | implied by the brief text; writer assigns this label in order of appearance |
| `eq:84.1` | Expected annual loss, $EAL} = L(p)\,dp$ approximated by trapezoids |  |
| `eq:84.2` | Emissions intensity, $e = HR} EF}$ |  |
| `eq:84.3` | Net Article 6.4 credits, $N = ER} (1 - s - o)$ |  |
| `fw:label-test` | Framework 84.1 Three-question label test | home ssec:84.1.2 |
| `fw:project-climate-screen` | Framework 84.2 Project climate risk screen | home ssec:84.6.6 |

### Chapter 85: Screening deals and reading data rooms

Source brief: `briefs/u17.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:85` | Screening deals and reading data rooms |  |
| `sec:85.1` | What a screen decides |  |
| `ssec:85.1.1` | Spend or walk |  |
| `ssec:85.1.2` | Two ways to get a screen wrong |  |
| `ssec:85.1.3` | The same deal from four seats |  |
| `sec:85.2` | The one-hour deal screen |  |
| `ssec:85.2.1` | The deal on one page, minutes 0 to 10 |  |
| `ssec:85.2.2` | Revenue, minutes 10 to 25 |  |
| `ssec:85.2.3` | Build and operate, minutes 25 to 35 |  |
| `ssec:85.2.4` | The killers, minutes 35 to 45 |  |
| `ssec:85.2.5` | The numbers, minutes 45 to 55 |  |
| `ssec:85.2.6` | Verdict and the screen note, minutes 55 to 60 |  |
| `sec:85.3` | Back-of-envelope numbers |  |
| `ssec:85.3.1` | CFADS in three lines |  |
| `ssec:85.3.2` | Debt capacity from an annuity |  |
| `ssec:85.3.3` | Equity return and where it lives |  |
| `ssec:85.3.4` | Breakevens that decide |  |
| `ssec:85.3.5` | Offtaker affordability |  |
| `sec:85.4` | The questions to ask on any deal |  |
| `ssec:85.4.1` | The questions and the reason behind each |  |
| `ssec:85.4.2` | Asking them in the room |  |
| `ssec:85.4.3` | What changes by sector |  |
| `sec:85.5` | Reading a data room |  |
| `ssec:85.5.1` | How data rooms are built and who builds them |  |
| `ssec:85.5.2` | Reading order |  |
| `ssec:85.5.3` | Following one number through every document |  |
| `ssec:85.5.4` | The absence index |  |
| `ssec:85.5.5` | What you may and may not use |  |
| `sec:85.6` | Lake Turkana and the interface a screen should catch |  |
| `sec:85.7` | Dabhol and the affordability question |  |
| `sec:85.8` | Walkthrough: screening a teaser in sixty minutes |  |
| `sec:85.9` | Case P: Pieter screens Bélanou in an hour |  |
| `sec:85.10` | Practitioner's notebook |  |
| `sec:85.11` | Judgment drill |  |
| `sec:85.12` | A screen says yes; now someone must write the case for a committee |  |
| `sec:85.13` | Exercises |  |
| `sec:85.14` | Solutions to exercises |  |
| `ex:85.1` | Screening a contracted solar plant in an hour (Illustrative) |  |
| `ex:85.2` | How far traffic can fall before debt service is missed (Illustrative) |  |
| `ex:85.3` | An affordability ratio for a single-buyer utility (Illustrative) |  |
| `ex:85.4` | One EPC price, three documents (Illustrative) |  |
| `exh:85.1` | Fatal flaws, priced risks and conditions across six sectors (Illustrative) |  |
| `exh:85.2` | The one-page screen note template (Illustrative) |  |
| `exh:85.3` | The questions that matter most by sector (Illustrative) |  |
| `exh:85.4` | Tracing the EPC price through the data room (USD m) (Illustrative) |  |
| `exh:85.5` | Teaser for a 220 MW wind farm in north-eastern Brazil (Illustrative) |  |
| `exh:85.6` | Completed screen note for the wind farm teaser (Illustrative) |  |
| `exh:85.7` | Pieter's screen note on Bélanou, September 2016 (Case P) |  |
| `exh:85.8` | Quick screens of the Merrick Link (2014) and Mesa Corta A1 (2021) (Case T, Case R) |  |
| `eq:85.1` | Screening debt capacity by annuity | ruling: Screening debt capacity by annuity (screening approximation only; never cited for sizing, R-108) |
| `eq:85.2` | Breakeven revenue for a DSCR test |  |
| `fw:one-hour-deal-screen` | Framework 85.1 One-hour deal screen | home sec:85.2 |
| `fw:deal-questions` | Framework 85.2 Questions to ask on any deal | home ssec:85.4.1 |
| `fw:data-room-reading-order` | Framework 85.3 Data room reading order | home ssec:85.5.2 |

### Chapter 86: Credit papers and investment committees

Source brief: `briefs/u17.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:86` | Credit papers and investment committees |  |
| `sec:86.1` | What a credit paper is for |  |
| `ssec:86.1.1` | The decision and who makes it |  |
| `ssec:86.1.2` | Approved for the right reasons |  |
| `ssec:86.1.3` | Same bones, different questions |  |
| `sec:86.2` | The structure of a credit paper |  |
| `ssec:86.2.1` | Recommendation and request first |  |
| `ssec:86.2.2` | The transaction in two pages |  |
| `ssec:86.2.3` | The parties and their credit |  |
| `ssec:86.2.4` | Risk analysis |  |
| `ssec:86.2.5` | Financial analysis |  |
| `ssec:86.2.6` | Structure and terms |  |
| `ssec:86.2.7` | E&S, legal and integrity |  |
| `ssec:86.2.8` | Pricing, profitability and hold |  |
| `ssec:86.2.9` | Conditions of approval and monitoring triggers |  |
| `sec:86.3` | The risk–mitigant–residual table |  |
| `ssec:86.3.1` | Building the rows |  |
| `ssec:86.3.2` | Residual risk: whose, and how much |  |
| `ssec:86.3.3` | How tables mislead |  |
| `sec:86.4` | Writing the investment committee memo |  |
| `ssec:86.4.1` | What an equity committee asks |  |
| `ssec:86.4.2` | The returns bridge |  |
| `ssec:86.4.3` | The bid number and the walk-away number |  |
| `ssec:86.4.4` | DFI and government papers |  |
| `sec:86.5` | Presenting to a committee |  |
| `ssec:86.5.1` | Twenty minutes |  |
| `ssec:86.5.2` | Answering questions |  |
| `ssec:86.5.3` | The committee pre-mortem |  |
| `ssec:86.5.4` | Conditions, declines and the second visit |  |
| `sec:86.6` | The paper after approval |  |
| `sec:86.7` | Sydney's Cross City Tunnel and the forecast nobody tabled |  |
| `sec:86.8` | Case P: Castellan's credit paper for Bélanou, May 2018 |  |
| `sec:86.9` | Case P: reading the 2018 paper in 2026 |  |
| `sec:86.10` | Practitioner's notebook |  |
| `sec:86.11` | Judgment drill |  |
| `sec:86.12` | Approval gives a deal team a mandate; the craft is in carrying it |  |
| `sec:86.13` | Exercises |  |
| `sec:86.14` | Solutions to exercises |  |
| `ex:86.1` | Rewriting a recommendation paragraph (Illustrative) |  |
| `ex:86.2` | The sponsor's case and the bank's case (Illustrative) |  |
| `ex:86.3` | Sensitivities in order of impact (Illustrative) |  |
| `ex:86.4` | The profitability box (Illustrative) |  |
| `ex:86.5` | The returns bridge from sponsor case to IC case (Illustrative) |  |
| `exh:86.1` | Credit papers, IC memos, DFI board papers, ECA memos and government papers compared (Illustrative) | renumbered, R-130 |
| `exh:86.2` | Sponsor case against bank case: adjustments and sources (Illustrative) (was "Exhibit 86.2a") | renumbered, R-130 |
| `exh:86.3` | Sensitivities ordered by impact on DSCR (Illustrative) (was exh:86.2) | renumbered, R-130 |
| `exh:86.4` | Conditions of approval, well and badly drafted (Illustrative) (was exh:86.3) | renumbered, R-130 |
| `exh:86.5` | A risk–mitigant–residual row and its rewrite (Illustrative) (was exh:86.4) | renumbered, R-130 |
| `exh:86.6` | Returns bridge from sponsor case to IC case (USD m, %) (Illustrative) (was exh:86.5) | renumbered, R-130 |
| `exh:86.7` | One-page annual review summary (Illustrative) (was exh:86.6) | renumbered, R-130 |
| `exh:86.8` | Castellan credit paper, Part 1: recommendation and request (Case P) | renumbered, R-130 |
| `exh:86.9` | Castellan credit paper, Part 2: transaction summary and sources and uses (Case P) | renumbered, R-130 |
| `exh:86.10` | Castellan credit paper, Part 3: sponsors and equity (Case P) | renumbered, R-130 |
| `exh:86.11` | Castellan credit paper, Part 4: country, offtaker and government support (Case P) | renumbered, R-130 |
| `exh:86.12` | Castellan credit paper, Parts 5 and 6: project, construction and gas supply chain (Case P) | renumbered, R-130 |
| `exh:86.13` | Castellan credit paper, Part 7: risk–mitigant–residual table (Case P) | renumbered, R-130 |
| `exh:86.14` | Castellan credit paper, Part 8: financial analysis, key metrics (Case P) | renumbered, R-130 |
| `exh:86.15` | Castellan credit paper, Part 8: case table and sensitivities (Case P) | renumbered, R-130 |
| `exh:86.16` | Castellan credit paper, Part 9: structure and terms (Case P) | renumbered, R-130 |
| `exh:86.17` | Castellan credit paper, Part 10: E&S, legal and integrity (Case P) | renumbered, R-130 |
| `exh:86.18` | Castellan credit paper, Part 11: pricing, profitability and hold (Case P) | renumbered, R-130 |
| `exh:86.19` | The 2018 risk–mitigant–residual table read in 2026 (Case P) (was exh:86.17) | renumbered, R-130 |
| `eq:86.1` | Return on risk-adjusted capital for a facility hold | ruling: Facility profitability box: post-tax RAROC on the hold, applying eq:29.1 (repurposed, R-076) |
| `fw:credit-paper-structure` | Framework 86.1 Credit paper structure | home sec:86.2 |
| `fw:risk-mitigant-residual` | Framework 86.2 Risk–mitigant–residual table | home ssec:86.2.4 |
| `fw:committee-pre-mortem` | Framework 86.3 Committee pre-mortem | home ssec:86.5.3 |

### Chapter 87: The practitioner's craft and career

Source brief: `briefs/u17.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:87` | The practitioner's craft and career |  |
| `sec:87.1` | Managing advisors |  |
| `ssec:87.1.1` | Who hires whom, who pays, and whose duty |  |
| `ssec:87.1.2` | Engagement letters as management tools |  |
| `ssec:87.1.3` | The advisor management cycle |  |
| `ssec:87.1.4` | Budgets and overruns |  |
| `ssec:87.1.5` | Challenging without capturing |  |
| `sec:87.2` | Leading a deal team |  |
| `ssec:87.2.1` | Roles on a sponsor team and a bank team |  |
| `ssec:87.2.2` | The issues list |  |
| `ssec:87.2.3` | Review discipline |  |
| `ssec:87.2.4` | Fatigue and quality |  |
| `sec:87.3` | Running a timetable to close |  |
| `ssec:87.3.1` | The weekly cadence |  |
| `ssec:87.3.2` | The cost of a week |  |
| `ssec:87.3.3` | Escalation |  |
| `ssec:87.3.4` | Holding a date or moving it |  |
| `sec:87.4` | Relationships and reputation |  |
| `ssec:87.4.1` | A small market with long memories |  |
| `ssec:87.4.2` | Credibility as an account |  |
| `ssec:87.4.3` | Governments and communities |  |
| `sec:87.5` | Ethics and integrity |  |
| `ssec:87.5.1` | The situations that arise |  |
| `ssec:87.5.2` | The integrity check |  |
| `ssec:87.5.3` | Reporting and protection |  |
| `ssec:87.5.4` | Pressure on the numbers |  |
| `sec:87.6` | Career-limiting mistakes |  |
| `sec:87.7` | Career paths |  |
| `ssec:87.7.1` | The seats |  |
| `ssec:87.7.2` | Moving between seats |  |
| `ssec:87.7.3` | Specialist or generalist |  |
| `sec:87.8` | A deliberate plan for building judgment |  |
| `ssec:87.8.1` | Why deals teach slowly |  |
| `ssec:87.8.2` | The deal log and the decision journal |  |
| `ssec:87.8.3` | Scoring your own forecasts |  |
| `ssec:87.8.4` | Reference classes from your own record |  |
| `ssec:87.8.5` | Reconstructing closed deals |  |
| `ssec:87.8.6` | Sitting in every chair |  |
| `ssec:87.8.7` | The 24-month plan |  |
| `sec:87.9` | Staying current |  |
| `ssec:87.9.1` | What changes and how fast |  |
| `ssec:87.9.2` | The sources that matter |  |
| `ssec:87.9.3` | Updating a market norm |  |
| `ssec:87.9.4` | A routine |  |
| `sec:87.10` | Carillion and the counterparty everyone knew |  |
| `sec:87.11` | Walkthrough: challenging an independent engineer's draft report |  |
| `sec:87.12` | Case P: three careers and a phone call |  |
| `sec:87.13` | Practitioner's notebook |  |
| `sec:87.14` | Judgment drill |  |
| `sec:87.15` | Judgment learned on old deals meets structures nobody has done |  |
| `sec:87.16` | Exercises |  |
| `sec:87.17` | Solutions to exercises |  |
| `ex:87.1` | An advisor budget that ran over (Illustrative) |  |
| `ex:87.2` | What a week of delay costs (Illustrative) |  |
| `ex:87.3` | Scoring your own forecasts (Illustrative) |  |
| `ex:87.4` | Your own reference class (Illustrative) |  |
| `exh:87.1` | Advisors on a large project financing: who appoints, pays and is owed a duty (Illustrative) |  |
| `exh:87.2` | Extract from a deal issues list (Illustrative) |  |
| `exh:87.3` | Career seats: the work, the judgment built and what it lacks (Illustrative) |  |
| `exh:87.4` | Deal log and decision journal fields (Illustrative) |  |
| `exh:87.5` | A 24-month judgment-building plan (Illustrative) |  |
| `exh:87.6` | Sources for staying current and what each updates (Illustrative) |  |
| `eq:87.1` | Brier score |  |
| `fw:advisor-cycle` | Framework 87.1 Advisor management cycle | home ssec:87.1.3 |
| `fw:judgment-plan` | Framework 87.2 Judgment-building plan | home ssec:87.8.7 |
| `fw:integrity-test` | Framework 87.3 The integrity test (renamed; slug fw:integrity-test) | home ssec:87.5.2 |

### Chapter 88: The frontier: evaluating new structures

Source brief: `briefs/u17.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:88` | The frontier: evaluating new structures |  |
| `sec:88.1` | What makes a structure new |  |
| `ssec:88.1.1` | Five kinds of new |  |
| `ssec:88.1.2` | The evidence gap |  |
| `ssec:88.1.3` | How structures become standard |  |
| `sec:88.2` | The new-structure test |  |
| `ssec:88.2.1` | The questions in order |  |
| `ssec:88.2.2` | Three verdicts |  |
| `ssec:88.2.3` | The test on one structure |  |
| `sec:88.3` | From first-of-a-kind to nth-of-a-kind |  |
| `ssec:88.3.1` | The financing ladder |  |
| `ssec:88.3.2` | Pricing first-of-a-kind cost risk |  |
| `ssec:88.3.3` | Who carries the tail |  |
| `ssec:88.3.4` | First-of-a-kind risk under public lenders at Ivanpah and Northvolt |  |
| `sec:88.4` | The test across the frontier |  |
| `ssec:88.4.1` | Energy-transition financing gaps |  |
| `ssec:88.4.2` | AI and data-center power demand |  |
| `ssec:88.4.3` | New nuclear and small modular reactors |  |
| `ssec:88.4.4` | Long-duration storage |  |
| `ssec:88.4.5` | Hydrogen |  |
| `ssec:88.4.6` | Carbon capture and storage |  |
| `ssec:88.4.7` | Adaptation and resilience |  |
| `ssec:88.4.8` | Critical minerals |  |
| `ssec:88.4.9` | Private credit |  |
| `ssec:88.4.10` | Local-currency and blended solutions |  |
| `ssec:88.4.11` | Digital deal execution |  |
| `sec:88.5` | Walkthrough: testing an unsolicited SMR power proposal for a data-center campus |  |
| `sec:88.6` | Case R: a data-center PPA from a repowered Thatcher Flats |  |
| `sec:88.7` | Practitioner's notebook |  |
| `sec:88.8` | Judgment drill |  |
| `sec:88.9` | The deal you have not seen yet |  |
| `sec:88.10` | Exercises |  |
| `sec:88.11` | Solutions to exercises |  |
| `ex:88.1` | Pricing first-of-a-kind cost risk (Illustrative) |  |
| `ex:88.2` | A short lease, long debt and a residual value guarantee (Illustrative) |  |
| `ex:88.3` | Debt on a floor versus debt on a merchant forecast (Illustrative) |  |
| `ex:88.4` | The cost gap for green hydrogen (Illustrative) |  |
| `exh:88.1` | Eleven frontiers classified by what is new (Illustrative) |  |
| `exh:88.2` | Technologies on the first-of-a-kind financing ladder, October 2026 (Illustrative) |  |
| `exh:88.3` | The new-structure test applied to the SMR proposal (Illustrative) |  |
| `exh:88.4` | The new-structure test applied to the R1 data-center offer (Case R) |  |
| `eq:88.1` | Cost at a chosen percentile under a lognormal overrun |  |
| `eq:88.2` | Levelized cost of hydrogen (if not owned by Chapter 83) | ruling: Cost gap and implied subsidy per kilogram, citing eq:83.1 (repurposed, R-002) |
| `fw:new-structure-test` | Framework 88.1 New-structure test | home ssec:88.2.1 |
| `fw:foak-ladder` | Framework 88.2 First-of-a-kind financing ladder | home ssec:88.3.1 |

### Chapter 89: Capstone deal simulation

Source brief: `briefs/u17.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:89` | Capstone deal simulation |  |
| `exh:89.1` | (caption not stated in brief; writer supplies) | implied by the brief text; writer assigns this label in order of appearance |
| `exh:89.2` | (caption not stated in brief; writer supplies) | implied by the brief text; writer assigns this label in order of appearance |
| `exh:89.3` | (caption not stated in brief; writer supplies) | implied by the brief text; writer assigns this label in order of appearance |

### Chapter 90: Final examination

Source brief: `briefs/u17.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:90` | Final examination |  |
| `exh:90.1` | compiled and checked mechanically in Phase 7 | implied by the brief text; writer assigns this label in order of appearance |

### Chapter 91: Glossary

Source brief: `briefs/u17.md`.

| Label | Caption or title | Note |
|---|---|---|
| `ch:91` | Glossary |  |
| `exh:91.1` | (caption not stated in brief; writer supplies) | implied by the brief text; writer assigns this label in order of appearance |
