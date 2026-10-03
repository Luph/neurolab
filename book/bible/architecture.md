# Architecture (editor-in-chief's master plan)

This file fixes the book's skeleton: title, Parts, chapter numbering, chapter file names, concept ownership at chapter level, and running-case beats by chapter. Part brief writers expand each chapter to subsection level in `bible/briefs/part-NN.md` and must not change chapter numbers, titles' substance, or ownership without logging a request in `bible/decisions.md` (section "Change requests").

Working title: **Project Finance: The Complete Practice — From First Principles to Financial Close and Beyond**

Variety of English: American. Base number format: USD millions to one decimal place (USD 412.6 million in prose; tables headed "USD m"). See `bible/style-sheet.md`.

Running cases (detail in `bible/case-bible.md`):

- **Case P (primary)**: greenfield gas-fired combined-cycle power plant with a full domestic gas-supply chain in a fictional emerging-market country; state utility offtaker under a capacity-plus-energy PPA; EPC contractor; O&M operator plus turbine OEM long-term service agreement; lender group of commercial banks, an ECA-covered tranche and a DFI; interest-rate swaps and currency issues.
- **Case T (PPP)**: user-pay toll road PPP (demand risk) in a fictional OECD jurisdiction with common-law PPP practice; from the government's decision to procure through bid, close, ramp-up shortfall, distress and restructuring.
- **Case R (portfolio)**: operating wind, solar and battery storage portfolio in a liberalized energy-only power market with merchant exposure; acquisitions, valuation, hedging, holdco financing and refinancing.

## Chapter list and concept ownership

Ownership refinements and every boundary between chapters are fixed in `bible/ownership-resolutions.md` (2026-10-03), which takes precedence over this table where they differ; glossary homes are in `bible/glossary-canon.md` and labels in `bible/anchor-registry.md`. A note such as (+R-013) cites the ruling that adds or bounds an item.

Ownership rule: a concept listed under a chapter is taught there in full. Every other chapter cross-references it by section number. A chapter may preview a later-owned concept only through a one- or two-sentence explicit forward reference.

### Part I — The Shape of a Deal

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 1 | 01-a-small-deal-start-to-finish.tex | A small deal, start to finish | Simplified end-to-end walkthrough of one small illustrative deal (a ~50 MW solar plant with a 20-year PPA, distinct from the running cases): site, permits, PPA, EPC, model, debt sizing by DSCR in simple form, term sheet, close, construction, operations, repayment. Introduces vocabulary intuitively with forward references to home chapters; bolds no term; exhibits in USD thousands (+R-110). | Introduce cast of Case P briefly at the end (the developer gets a call). |
| 2 | 02-what-project-finance-is.tex | What project finance is, and when to use it | SPV and ring-fencing; limited vs non-recourse; contractual web (the book's defined concept); basic definitions of sponsor and offtaker (+R-063); "allocate each risk to the party best able to manage it"; comparison with corporate finance, asset finance and leasing, RBL (one-paragraph overview; full home Ch 75), acquisition finance, securitization, structured finance; why sponsors, lenders and governments use it (risk isolation, debt capacity, agency costs, partnering, political deterrence) and its costs (transaction cost, time, rigidity, information burden, lender control); when PF is the wrong tool. | Case P sponsor board decides whether to project-finance. |
| 3 | 03-how-project-finance-evolved.tex | How project finance evolved | History: production payments, North Sea, US PURPA and independent power (home of IPP, +R-064), 1990s emerging-market IPPs, PFI/PPP era (era overview only; detail Ch 57, +R-097), Asian crisis lessons, post-2008 and Basel, institutional and private credit, energy transition, digital infrastructure; the lesson of each era. | — |
| 4 | 04-the-parties-and-the-lifecycle.tex | The parties and the project lifecycle | The cast (sponsors strategic/financial/developers, project company, lender types, offtakers, host governments and regulators, EPC contractors and OEMs, operators, input suppliers, insurers, advisors, agents and trustees, rating agencies, hedge providers): how each earns money, fears, behaves under stress. Lifecycle end to end: origination, development, financing, close, construction, completion, operations, refinancing, sale, decommissioning or handback; glossary home of party and role terms (ECA, DFI, MLA, agents, trustees) and of stage-level financial close, completion and COD (+R-066, +R-065). | Case P origination: developer identifies the opportunity; development budget; team formed. |

### Part II — Foundations

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 5 | 05-time-value-of-money.tex | Money and time | Interest, compounding, discounting, annuities, NPV, IRR and its traps (multiple IRRs, reinvestment, scale, timing), XNPV/XIRR, payback, real vs nominal, inflation and indexation (CPI/partial indexation mechanics); levelized price and levelized tariff (+R-001). | Case P: tariff indexation example. |
| 6 | 06-debt-and-interest-rates.tex | Debt and interest rates | Principal, interest, upfront and commitment fee mechanics (+R-003); bullet, annuity, straight-line, sculpted (intro only; sculpting math owned by Ch 36); day counts; fixed vs floating; reference rates (SOFR, SONIA, €STR, EURIBOR, term vs compounded in arrears) and LIBOR transition; margins and bps; swaps at intuitive level (swap valuation basics, MTM, breakage); weighted average life; bond basics and yield to maturity (+R-005, +R-004). | Case P: indicative SOFR-based loan. |
| 7 | 07-accounting-for-the-project-company.tex | Accounting from zero | Three statements and linkages, accruals vs cash, depreciation/amortization, deferred tax, working capital, capitalized interest (IDC) in accounts, reading a project company's accounts; decommissioning provision basics. (Sponsor-level accounting, IFRIC 12 and asset retirement obligations are Ch 66; +R-016, +R-015.) | Case P: year-1 operating accounts. |
| 8 | 08-leverage-risk-and-cost-of-capital.tex | Leverage, risk, and the cost of capital | Capital structure, leverage effect on equity returns, MM intuition, cost of capital, CAPM, WACC vs APV, risk and return; why PF achieves high leverage; equity IRR and project IRR defined as levered and unlevered IRR (conventions Ch 46; +R-013). | Case P: equity IRR at different gearing. |
| 9 | 09-probability-and-uncertainty.tex | Probability and uncertainty | Distributions, expected values, P50/P90/P99 exceedance, one-year vs ten-year P-values, correlation, sensitivity vs scenario vs Monte Carlo (concepts; implementation in Ch 43); natural hedge, optimism bias, reference-class forecasting, energy yield assessment (+R-043). | Case R: wind yield P-values. |
| 10 | 10-law-for-financiers.tex | Law for financiers | How contracts work: reps, warranties, covenants, conditions, indemnities, liability caps, LDs and the penalty rule (Cavendish v Makdessi), force majeure, frustration/impossibility/hardship; subrogation (+R-030); common vs civil law; security and insolvency in principle; governing law; courts vs arbitration (overview; detail Ch 54). | Case P: first look at a draft PPA clause. |
| 11 | 11-how-power-assets-and-markets-work.tex | How power assets and electricity markets work | Thermal (OCGT/CCGT/coal, heat rate, efficiency, availability), wind, solar, hydro, nuclear, batteries at financier depth; grids; electricity markets: merit order, marginal pricing, capacity and ancillary markets, nodal vs zonal, curtailment, negative prices; capture prices and cannibalization; spark and dark spreads; LCOE (+R-001, +R-024). | Case P plant technology; Case R market. |
| 12 | 12-how-resource-transport-social-digital-assets-work.tex | How resource, transport, social, and digital assets work | Oil, gas, LNG chains; mines and processing; roads, rail, airports, ports; hospitals; water plants; fiber and data centers — at financier depth; reserves and resources classifications (+R-025). | Case P gas field and pipeline; Case T road. |
| 13 | 13-excel-for-project-finance.tex | Excel for project finance | Layout, timing flags and date techniques (Case P timeline and corkscrew are Ch 39; +R-017), core functions (INDEX/MATCH, XLOOKUP, SUMPRODUCT, EOMONTH, MIN/MAX, OFFSET avoidance), fragile formulas, data tables, goal seek, circularity (concept and copy-paste macro vs closed form), error checks, range names policy. | Small practice workbook. |

### Part III — Risk

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 14 | 14-the-risk-taxonomy.tex | The risk taxonomy | Every risk category listed in coverage map C, defined with mechanism, example and typical bearer; operating leverage; wrong-way risk; first-of-a-kind and nth-of-a-kind; cyber risk (cover Ch 27, controls Ch 62) (+R-035, +R-036, +R-042, +R-037). | Case P risk register v1. |
| 15 | 15-analyzing-allocating-pricing-risk.tex | Analyzing, allocating, and pricing risk | Method: identify, analyze, quantify, allocate, mitigate, price, monitor; risk matrix construction; residual risk to equity vs debt; "bankable" defined (bankability ladder framework); pass-through and back-to-back; allocation on paper vs in practice; lender downside vs sponsor upside asymmetry; expected loss, three-point estimates, pre-mortem; pricing of risk (+R-041, +R-038). | Case P risk matrix. |
| 16 | 16-the-mitigation-toolkit.tex | The mitigation toolkit | Overview and selection of contracts, insurance, guarantees, reserves, hedges, structural features, sponsor support, credit enhancement — how they combine; cost of each. (Detailed instruments owned elsewhere: insurance Ch 27, reserves Ch 37, hedges Ch 37, guarantees Ch 34/60.) Comparative cost of payment security (detail Ch 59); carrying cost of a reserve (negative carry on bonds is Ch 30) (+R-033, +R-034). | Case P mitigation plan. |

### Part IV — The Contracts

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 17 | 17-concessions-and-government-support.tex | Concessions, implementation agreements, and government support | Concession/project/implementation agreements; government support instruments (guarantees, letters of support, comfort letters); termination events and compensation regimes (principles; PPP-specific formulas Ch 58); change in law, compensation events, MAGA, relief events, economic equilibrium; exclusivity and competing-facility undertakings (+R-045, +R-053). | Case P implementation agreement and sovereign support letter; competitive procurement of Case P IPP (stages named descriptively, forward reference to Ch 58; +R-046). |
| 18 | 18-power-purchase-and-tolling-agreements.tex | Power purchase and tolling agreements | PPAs: capacity and energy payments, availability, deemed energy, curtailment, take-or-pay, pass-throughs, indexation, heat-rate and fuel pass-through, dispatch, payment security (outline; cost comparison Ch 16, detail Ch 59), tolling agreements; take-or-pay principle and take-and-pay (fuel-side mechanics Ch 25); canonical tariff formulas eq:18.1 to eq:18.3; PPA pass-through of change in law (+R-047, +R-049, +R-033). | Case P PPA negotiation. |
| 19 | 19-support-schemes-cfds-and-rab.tex | Feed-in tariffs, contracts for difference, and regulated asset base models | FiTs, CfDs (two-sided, strike/reference price), RAB model, cap-and-floor, how each allocates risk and shapes financing. | — |
| 20 | 20-merchant-revenue-and-hedges.tex | Merchant revenue, corporate PPAs, and hedges | Corporate PPAs physical and virtual; fixed-volume, fixed-shape, as-produced, proxy revenue swaps, floors, collars, tolls for batteries; capacity and ancillary-service revenue; basis and shape risk (Winter Storm Uri). | Case R hedge book. |
| 21 | 21-revenue-contracts-beyond-power.tex | Revenue contracts beyond power | LNG SPAs and tolling (Sabine Pass), pipeline transportation and ship-or-pay (the transporter's revenue contract; +R-048), mining offtake (payables, TC/RCs, penalties), streams and royalties, availability payments, unitary charge and availability deductions (contract form; regime design Ch 58; +R-051), user tolls and tariffs, airport and port revenue models (home of single and dual till; +R-055), data-center leases. | Case T toll regime; Case P gas transportation. |
| 22 | 22-the-epc-contract.tex | The EPC contract | Lump-sum turnkey date-certain EPC; delay and performance LDs and calibration; liability caps; bonds, guarantees, retention; variations, EOT, claims; testing and completion; defects liability; contractor credit. | Case P EPC negotiation. |
| 23 | 23-construction-structures-beyond-epc.tex | Construction structures beyond the single EPC contract | Split and multi-contract structures, including turbine supply and balance-of-plant contracts (+R-067); EPCM; wraps; interface agreements; FIDIC and other standard forms (Silver/Yellow/Emerald etc.), NEC; supply-chain risk; equipment-supplier credit. | Case T design-build JV. |
| 24 | 24-operations-and-maintenance-contracts.tex | Operations and maintenance contracts | O&M agreements, LTSAs, asset management agreements, major maintenance, performance regimes, fixed vs cost-plus, incentive design. | Case P O&M and LTSA. |
| 25 | 25-inputs-and-access.tex | Securing fuel, water, grid access, land, and permits | Fuel and feedstock supply (GSA, fuel-side take-or-pay mechanics, make-up, DCQ; principle Ch 18), transportation as an input (+R-047, +R-048), water, grid connection and interconnection, land rights, permits and transferability. | Case P GSA negotiation. |
| 26 | 26-sponsor-and-shareholder-documents.tex | Sponsor and shareholder documents | Shareholders'/JV agreements (lock-in), equity contribution agreements (never abbreviated), financial completion as the release trigger (+R-050, +R-060), sponsor support and completion guarantees, development and co-development agreements. | Case P JVA among sponsors. |
| 27 | 27-insurance.tex | Insurance | CAR/EAR, DSU/ALOP, marine cargo and marine DSU, TPL, operational all risks, BI, political risk (overview and glossary home; detail Ch 60), credit insurance (overview; ECA cover Ch 29), cyber cover (+R-057, +R-037); lender requirements (loss payee, non-vitiation, cut-through, reinsurance assignment); market cycles. | Case P insurance program. |
| 28 | 28-direct-agreements-and-the-contract-map.tex | Direct agreements and the contract map as a system | Direct agreements, consents, step-in and novation; contract map; contract gap scan framework; "Who pays if…?" trace framework. | Case P full contract map and gap scan. |

### Part V — Sources of Capital

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 29 | 29-lenders.tex | The lenders | Commercial banks (business model; capital-rule detail Ch 68), ECAs (OECD Arrangement, cover types, content rules, premia), multilateral and bilateral DFIs (mandates, additionality, preferred creditor status, A/B and parallel loans, guarantees (overview; instruments Ch 34; +R-069); RAROC logic (+R-075)), institutional investors, infrastructure debt funds and private credit. | Case P lender group formed. |
| 30 | 30-project-bonds-and-ratings.tex | Project bonds and ratings | Project bonds, 144A/Reg S, private placements (USPP), green/sustainability bond format (instrument detail Ch 84), sukuk overview (detail Ch 33), bond vs loan, negative carry, make-whole and call protection (+R-078), how rating agencies analyze projects in construction and operation. | Case P refinancing bond option previewed. |
| 31 | 31-mezzanine-holdco-and-ancillary-facilities.tex | Mezzanine, holdco, and ancillary facilities | Mezzanine, holdco debt, equity bridge loans, VAT and working-capital facilities, LC facilities, standby and cost-overrun facilities. | Case R holdco facility. |
| 32 | 32-equity.tex | Equity | Sponsor equity, shareholder loans, contingent and back-ended equity, equity LCs, development premia, farm-downs, infrastructure funds (overview; Ch 47), listed vehicles and yieldcos (SunEdison/TerraForm), US tax equity and tax-credit transfer (dated, flagged). | Case P equity plan. |
| 33 | 33-islamic-project-finance.tex | Islamic project finance | Ijara, istisna'a, wakala, murabaha, musharaka; sukuk; co-financing with conventional tranches (Sadara). | — |
| 34 | 34-blended-concessional-local-currency.tex | Blended, concessional, and local-currency finance | Blended and concessional finance, first-loss, guarantees (partial risk/credit guarantees), viability-gap funding, climate funds, local-currency financing instruments (TCX-type hedges, local bonds, cross-currency swaps); currency risk analysis and contractual solutions are Ch 59 (+R-070). | Case P DFI concessional element. |

### Part VI — Structuring Debt

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 35 | 35-cfads-and-cover-ratios.tex | Cash flow available for debt service and the cover ratios | CFADS definition; DSCR (min/avg), LLCR, PLCR, gearing; base/banking/downside/break-even cases. | Case P CFADS. |
| 36 | 36-sizing-and-sculpting-debt.tex | Sizing and sculpting debt | Sizing by DSCR and gearing; sculpting math; tenor (sizing sense); average-life limits as a constraint (WAL itself Ch 6); tenor and tail; balloons and mini-perms (hard/soft); grace periods; P90/P99 sizing; merchant tails; how parameters vary by sector, contract quality, market, cycle. | Case P debt sized. |
| 37 | 37-reserves-sweeps-covenants-and-hedging.tex | Reserves, sweeps, covenants, and hedging | DSRA, MMRA and other reserves (funding, sizing, LC substitution); cash sweeps; distribution lock-ups and trapped cash; equity cure design (+R-081); financial and non-financial covenants (design; drafting Ch 51); hedging requirements and hedge profiles. | Case P reserve and hedge structure. |
| 38 | 38-pricing-project-debt.tex | Pricing project debt | Minimum margin build-up (capital input Ch 68; +R-075); margins and ratchets; swap credit and execution charges (+R-007); arrangement, underwriting, participation, commitment, agency fees; ECA premia in all-in cost; all-in cost of debt; market flex. | Case P pricing. |

### Part VII — Financial Modeling: A Complete Course

Built cell by cell on Case P. Companion model in `model/`.

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 39 | 39-model-architecture-and-timing.tex | Model architecture, standards, and timing | Architecture, FAST standard, sheet structure, timelines and the project flag set, the corkscrew, calendar rows on the Time sheet, inputs and scenario control, model map (+R-017, +R-021). | Case P model skeleton. |
| 40 | 40-modeling-construction-and-funding.tex | Modeling construction and funding | Construction budget, sources and uses, drawdown order, equity-first vs pro rata (modeling only; commercial choice Ch 32; +R-071), IDC and fee circularity and clean resolutions. | Case P funding sheet. |
| 41 | 41-modeling-operations-tax-working-capital.tex | Modeling operations, tax, and working capital | Revenue and cost builds, indexation, tax computation (depreciation, losses, interest limitation and thin capitalization as computed; rules Ch 67; +R-020; withholding), working capital, VAT. | Case P ops and tax. |
| 42 | 42-modeling-the-waterfall-debt-and-reserves.tex | Modeling the waterfall, debt, and reserves | Operating waterfall and CFADS in model, sculpting in model, reserves, sweeps, lock-ups, the dividend trap and solutions; integrated financial statements in the model (+R-019). | Case P waterfall. |
| 43 | 43-returns-ratios-scenarios-outputs.tex | Returns, ratios, scenarios, and outputs | Equity and project returns in model (definitions Ch 8, conventions Ch 46), ratio calculations, sensitivities, scenarios, breakevens, Monte Carlo implementation, dashboards, integrity checks. | Case P outputs. |
| 44 | 44-auditing-a-model.tex | Auditing a model | Model audit process, review checklist, classic errors, auditing someone else's model. | Case P model audit findings. |
| 45 | 45-sector-specific-modeling.tex | Sector-specific modeling | Energy yield and P-values in model, degradation and augmentation, availability and curtailment; traffic ramp-up; mining reserves, grades, recoveries; LNG and commodity-linked revenues; PPP payment mechanisms and deductions (supplied mechanism; design Ch 58; +R-022). | Case T traffic model; Case R yield model. |

### Part VIII — Equity, Valuation, and Investment Decisions

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 46 | 46-equity-returns-and-valuation.tex | Equity returns and valuation through the project's life | Return conventions for equity IRR and project IRR, NPV, cash yield, multiples; terminal value as a valuation method (+R-014); cost of equity and hurdles by stage; valuation at each development milestone; development economics and where value is created. | Case R valuation of an acquisition target. |
| 47 | 47-bidding-acquisitions-and-funds.tex | Bidding, acquisitions, and infrastructure funds | Bid pricing in competitive tenders and winner's curse; buying and selling operating assets (process, teaser, confidentiality agreement, information memorandum, share purchase agreement, W&I; +R-087, +R-084; locked box vs completion accounts); portfolio construction; how infra funds think, invest and are paid. | Case P tariff bid; Case T bid; Case R acquisition. |

### Part IX — Due Diligence

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 48 | 48-technical-resource-and-market-diligence.tex | Technical, resource, and market diligence | Independent engineer; reliance letters and advisor duty of care (+R-087); resource and reserves; market and price curves; traffic and demand studies; scoping, reading, challenging. | Case P IE report walkthrough; Case T traffic study. |
| 49 | 49-legal-insurance-model-tax-integrity-diligence.tex | Legal, insurance, model, tax, and integrity diligence | Legal and regulatory DD; insurance advisor; model audit engagement; tax and accounting DD; counterparty credit; KYC, sanctions, anti-corruption DD (screening process; law Ch 60; +R-088). | Case P legal DD report. |
| 50 | 50-environmental-and-social-risk.tex | Environmental and social risk and standards | ESIA, ESMP, ESAP; IFC Performance Standards; Equator Principles; World Bank ESF; OECD Common Approaches (+R-090); community engagement; land acquisition and resettlement; indigenous peoples and FPIC; biodiversity; labor and human rights; why E&S failure is credit risk. | Case P resettlement and ESAP. |

### Part X — Finance Documents and the Legal Framework

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 51 | 51-the-finance-documents.tex | The finance documents | Document set and flow (mandate, commitment letters, term sheets, CTA, facility agreements, fee letters, ISDA overview), reps, CPs, covenants, EoDs, remedies, equity cures, permitted debt and distributions, change of control, amendments and voting inside a facility (home of waiver, consent and amendment; +R-092); LMA, LSTA, APLMA. | Case P CTA. |
| 52 | 52-security-accounts-and-waterfall.tex | Security, accounts, and the cash waterfall | Security package and purpose; common-law vs civil-law (trusts vs parallel debt, floating charges); perfection; enforcement as going concern (principles; process Ch 64); accounts structure (including offshore accounts as architecture; +R-093) and cash waterfall in full. | Case P accounts agreement. |
| 53 | 53-intercreditor-arrangements.tex | Intercreditor arrangements | Tranches, voting, ECA and DFI rights, hedge counterparties, standstills, enforcement, conventional–Islamic interface. | Case P ICA. |
| 54 | 54-governing-law-disputes-and-investment-protection.tex | Governing law, disputes, and investment protection | Governing law and jurisdiction choices, arbitration (ICC, LCIA, ICSID, UNCITRAL), enforcement of awards (New York Convention), sovereign immunity and waiver, stabilization clauses, investment treaties and treaty structuring. | Case P dispute clause. |

### Part XI — The Deal Process and Negotiation

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 55 | 55-running-a-financing-to-close.tex | Running a financing to close | Financing strategy (club, underwritten, best efforts; bank vs bond), financial advisor role, IM and lender presentations, credit approval inside a bank, syndication and sell-down, documentation management, CPs, signing vs financial close, funds flow and closing mechanics, timelines and critical paths. | Case P financial close. |
| 56 | 56-negotiating-project-finance.tex | Negotiating project finance | What is market and why; levers; trade-offs on every key term; tactics, sequencing, escalation; market cycle; negotiating with governments, contractors, offtakers and lenders; term sheet markup walkthrough. | Case P term sheet negotiation. |

### Part XII — Public–Private Partnerships

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 57 | 57-the-public-sector-case-for-ppps.tex | The public-sector case for PPPs | Rationale and critiques; value for money and PSC; affordability; fiscal and statistical treatment and contingent liabilities; PPP units and programs; unsolicited proposals; UK PFI history and end. | Case T government decision to procure. |
| 58 | 58-procuring-and-designing-ppps.tex | Procuring and designing PPPs | Procurement for PPPs and IPP tenders (+R-046; prequalification, competitive dialogue, RFPs, BAFO, evaluation); delivery models (DBFOM, BOT, BOOT, BOO; availability vs user-pay; shadow tolls, revenue-sharing bands, LPVR; +R-052); payment mechanisms and deduction regimes; handback; change, benchmarking, market testing; termination regimes and compensation formulas; refinancing gain sharing; standard contract guidance; lessons. | Case T procurement and preferred bidder. |

### Part XIII — International and Emerging Markets

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 59 | 59-country-currency-and-payment-risk.tex | Country, currency, and payment risk | Country and sovereign risk analysis; currency risk and contractual solutions; why offshore accounts mitigate convertibility and transfer risk; payment security for weak offtakers (LCs, escrow, guarantees, liquidity facilities). | Case P offtaker payment crisis and currency shock. |
| 60 | 60-political-risk-and-its-protection.tex | Political risk and its protection | PRI (MIGA, ECAs, private market); multilateral halo; obsolescing bargain; host-government relations and local content; corruption risk and anti-bribery laws (FCPA, UKBA); sanctions; disputes and treaty claims in practice. | Case P political-risk cover. |

### Part XIV — The Project Through Its Life

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 61 | 61-construction-to-completion.tex | Construction to completion | Drawdowns and certification, cost-to-complete test, contingency management, monitoring including earned value management (+R-100), change orders, delays and LD flows, insurance claims in practice, contractor distress, lenders' completion tests in practice, release of sponsor support (+R-050). | Case P construction delay, overrun, insurance claim, completion. |
| 62 | 62-operating-the-project.tex | Operating the project as owner and lender | Reporting and compliance, budgets, ratio testing and distributions, maintenance, performance management, waivers and amendments, asset optimization during the debt life (repowering, uprates, hybridization; life extension at end of life is Ch 65; +R-099); OT cyber controls (+R-037). | Case P operations; covenant breach and waiver. |
| 63 | 63-refinancing-and-secondary-sales.tex | Refinancing, repricing, and secondary sales | Refinancing and repricing; secondary sales: project-finance execution of stakes (consents, minimum holdings, sequencing; generic M&A toolkit Ch 47; +R-085); holdco leverage in practice. | Case P refinancing and partial sale; Case R refinancing. |
| 64 | 64-distress-restructuring-and-enforcement.tex | Distress, restructuring, and enforcement | Early warning signs, standstills, waivers (in distress), amend-and-extend, sponsor support, debt-for-equity, cash sweeps, distressed sales, enforcement over shares and assets, insolvency regimes (Ch 11, UK schemes and restructuring plans, civil-law regimes), PPP-specific dynamics, role of the state. | Case T distress and restructuring. |
| 65 | 65-end-of-life.tex | Decommissioning, handback, and end-of-life value | Decommissioning obligations and reserves, handback regimes in practice, life extension economics, end-of-life value conventions (terminal value as a method is Ch 46; +R-014, +R-015). | Case P handback planning; Case R decommissioning. |

### Part XV — Accounting, Tax, and Regulation

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 66 | 66-accounting-for-projects-and-sponsors.tex | Accounting for projects and sponsors | Consolidation and equity accounting, joint arrangements, service concessions (IFRIC 12; ASC 853), leases embedded in offtake contracts, hedge accounting, ECL, decommissioning provisions and asset retirement obligations, how accounting goals shape structures. | Case P sponsor accounting. |
| 67 | 67-tax-structuring.tex | Tax structuring | Holding structures, treaties, withholding taxes, interest limitation and thin cap, transfer pricing, VAT during construction, incentives and holidays, Pillar Two global minimum tax; US clean-energy credit constraints after 2025 (+R-073). | Case P holding structure. |
| 68 | 68-capital-rules-for-banks-and-insurers.tex | Capital rules for banks and insurers | Basel framework for PF (slotting, IRB, output floor), insurer capital (Solvency II infrastructure classes), how both shape who lends and price; the capital input to the minimum margin (+R-075). | — |

### Part XVI — Sector Deep Dives

Each: industry economics, how the asset works (cross-ref Ch 11/12), revenue models, key risks, contract set, typical financing terms (dated ranges), modeling specifics (cross-ref Ch 45), landmark deals and failures.

Ownership in Part XVI (+R-101): a sector chapter owns only sector-specific mechanics, structures, frameworks and terms that no earlier chapter teaches. Asset physics stays with Ch 11 and Ch 12, contract forms with Ch 17 to Ch 28, instruments with Ch 29 to Ch 34, structuring with Ch 35 to Ch 38, modeling method with Ch 45, and life-cycle practice with Ch 61 to Ch 65; sector chapters cite them. Chapter 75 is the full home of reserve-based lending (Ch 2 gives a one-paragraph overview). Case beats for Ch 69 to 83 are in Case Bible Part 6.

| Ch | File | Title | Owns |
|---|---|---|---|
| 69 | 69-thermal-power.tex | Thermal power | Thermal-specific only: screening curve and system roles; comparison of thermal revenue models by system role and credit (PPA, tolling, IWPP, merchant, capacity); merchant thermal margins applied from Ch 11 spreads; heat-rate headroom outcomes; dispatch and fuel take-or-pay mismatch; starts-based maintenance cost; fuel-chain lock-in (fw:fuel-chain-trace); thermal transition and stranding constraints; home of IWPP (+R-067). |
| 70 | 70-onshore-wind-and-solar.tex | Onshore wind and solar | Resource-to-revenue bridge (fw:resource-revenue-bridge); DC/AC and clipping economics; turbine choice, availability guarantees and cold-weather packages; congestion and basis in high-penetration markets; policy-support dependence; hybrid co-location as revenue protection; CSP contrast; onshore wind and solar financing terms. TSA and BOP are applied from Ch 23. |
| 71 | 71-offshore-wind.tex | Offshore wind | Offshore capex stack and supply-chain bottlenecks; access-driven availability; offshore transmission split (OFTO) and two-part gearing; pre-FID exposure clock (fw:pre-fid-exposure-clock); T&I weather-downtime sharing; sell-downs around FID; offshore decommissioning specifics. |
| 72 | 72-hydropower-and-geothermal.tex | Hydropower and geothermal | Hydro plant types as financial profiles; hydrology risk allocation (fw:hydrology-allocation) and tiered tariffs; unforeseen ground conditions and capped pass-through; water rights and dam safety as financing issues; geothermal resource staging (fw:geothermal-staging), drilling success and make-up wells, steam-field and power-plant splits. |
| 73 | 73-storage-transmission-and-interconnectors.tex | Storage, transmission, and interconnectors | Storage revenue stack screen; storage debt sizing by revenue quality; augmentation versus overbuild decision (modeling Ch 45); pumped storage and long-duration storage under cap-and-floor (+R-102); transmission revenue models (fw:transmission-revenue-selector); interconnector cap-and-floor and cross-border risk; transmission availability deductions. |
| 74 | 74-nuclear.tex | Nuclear power | Nuclear cost structure; why commercial PF avoids nuclear construction; nuclear financing models compared (fw:nuclear-risk-bearer); the legal plumbing of a nuclear RAB; government support packages for nuclear; nuclear liability as a category; decommissioning and waste funding; SMR financing; NSU export finance. |
| 75 | 75-upstream-and-midstream-oil-and-gas.tex | Upstream and midstream oil and gas, including reserve-based lending | Full home of reserve-based lending: borrowing base, bank price deck, redetermination and deficiency, field life cover ratio, tail test, LC sublimits, decommissioning security (fw:borrowing-base-walk; +R-101, +R-103); upstream fiscal regimes (concessions, production sharing contracts); other upstream financing structures; midstream asset economics and throughput credit (fw:throughput-credit-test); cross-border pipelines. |
| 76 | 76-lng-and-fpsos.tex | LNG liquefaction, regasification, and FPSOs | LNG project structures; the SPA portfolio as collateral (fw:lng-chain-credit); LNG completion support and tests (applying Ch 26 and 61); sponsor co-lending; regasification, terminal use agreements (home) and FSRU charters; FPSO lease-and-operate credit (fw:charter-credit-test) and early termination fees. |
| 77 | 77-industrial-projects.tex | Refining, petrochemicals, and manufacturing finance | Spread businesses: crack spreads, petrochemical cash margins, gigafactory throughput and yield economics; industrial processing agreements (industrial tolling; +R-054); margin protection ladder; licensor guarantees; multi-unit completion tests; sponsor marketing agreements; industrial-policy finance. |
| 78 | 78-mining-and-critical-minerals.tex | Mining, metals, and critical minerals | Cost curve, C1 and AISC; critical minerals as a finance category; mining host agreements and state carried interests; four-part completion test; reserve tail requirement (concept Ch 45); price-deck sizing (deck from Ch 75); streams as construction capital (instrument Ch 21); debt caps and staged development. |
| 79 | 79-roads-bridges-and-tunnels.tex | Toll roads, bridges, and tunnels | Toll-road demand economics (value of time from Ch 12 applied, revenue-maximizing toll, diversion); greenfield against brownfield; bridge and tunnel specifics; road revenue forms at sector level; application and calibration of demand-risk sharing instruments owned by Ch 57 and Ch 58 (fw:demand-risk-menu for toll roads; +R-052); ramp-up diagnosis (fw:ramp-up-diagnosis); competing-facility drafting for roads (principle Ch 17; +R-053). Case T ramp-up beat. |
| 80 | 80-rail-airports-and-ports.tex | Rail, urban transit, airports, and ports | Farebox economics and transit delivery models; rolling stock finance; airport regulation beyond the till basics of Ch 21 (hybrid till, price caps; +R-055); port economics and concession terms (MAG from Ch 21); footloose-demand test; governments as stabilizers in transport demand shocks. |
| 81 | 81-social-infrastructure-water-and-waste.tex | Social infrastructure, water, desalination, and waste-to-energy | What the state buys in social PPPs; contractor dependence; water sector models (affermage, BOT with water purchase agreements, regulated utilities); desalination contract structure; waste-to-energy (gate fees, put-or-pay, NCV); payment-chain trace. |
| 82 | 82-digital-infrastructure.tex | Telecoms, fiber, towers, and data centers | Tower economics and master lease agreements (never abbreviated); fiber penetration economics; data-center lease structures and credit; power as the binding constraint; GPU and compute-backed lending; lease-life gap test; digital-specific risks. |
| 83 | 83-hydrogen-ccs-and-sustainable-fuels.tex | Hydrogen and its derivatives, carbon capture and storage, and sustainable fuels | Hydrogen production routes and the levelized cost of hydrogen (home, eq:83.1; +R-002); derivatives and conversion; hydrogen revenue models; CCS chain, business models and storage liability; sustainable fuel pathways and revenue stack; market-risk holder trace. |

### Part XVII — Sustainability

| Ch | File | Title | Owns |
|---|---|---|---|
| 84 | 84-sustainable-finance.tex | Sustainable finance and climate risk | Climate risk assessment method (categories Ch 14; EP4 trigger Ch 50; adaptation as an investment theme Ch 88; +R-091); green, social, sustainability and sustainability-linked loans and bonds (GBP, GLP, SLLP, SLBP), taxonomies (EU and others), transition finance, carbon markets (compliance, voluntary, Article 6), climate risk assessment (physical and transition; TCFD/ISSB), greenwashing risk. |

### Part XVIII — The Financier's Craft and the Frontier

| Ch | File | Title | Owns |
|---|---|---|---|
| 85 | 85-screening-deals-and-reading-data-rooms.tex | Screening deals and reading data rooms | One-hour deal screen framework (uses the Ch 14 taxonomy and the Ch 15 bankability ladder; +R-040); the questions to ask on any deal; reading a data room (virtual data room, Q&A log, clean team, number trace, absence index; +R-087). Case P and others screened. |
| 86 | 86-credit-papers-and-investment-committees.tex | Credit papers and investment committees | Writing a credit paper and IC memo; the facility profitability box (RAROC applied from Ch 29; +R-075); presenting to a committee; full Case P credit paper. |
| 87 | 87-the-practitioners-craft.tex | The practitioner's craft and career | Managing advisors and a deal team (personal craft; reliance letters Ch 48); running a timetable (method Ch 55; +R-095); relationships and reputation; ethics and integrity; career-limiting mistakes; career paths; deliberate plan for building judgment; staying current. |
| 88 | 88-the-frontier.tex | Evaluating new structures at the frontier | Frameworks for evaluating new structures (title +R-113); FOAK financing ladder (FOAK and NOAK defined in Ch 14; +R-042); cost gap for hydrogen using LCOH from Ch 83 (+R-002); energy-transition gaps, AI/data-center power demand, new nuclear and SMRs, long-duration storage, hydrogen, CCS, adaptation and resilience, critical minerals, private credit, local-currency and blended solutions, digital deal execution. |

### Matter (Phase 6, in `matter/`)

- 00-front-matter.tex: how to use the book, study plan, how to work exercises and model builds, general caveat (stated once), running-case summaries and cast list, capability-to-chapter map; labels fm:slug (+R-107, +R-108).
- 89-capstone.tex: capstone end-to-end deal simulation with full expert solution; own inputs, model and ledger C-F01 to C-F24, and a capstone mini-Bible (+R-106).
- 90-final-examination.tex: final exam with worked answers; model-task inputs and an audit workbook in model/exam/ (+R-106).
- 91-glossary.tex, 92-formula-sheet.tex, 93-checklists-and-templates.tex, 94-index-of-cases.tex.
