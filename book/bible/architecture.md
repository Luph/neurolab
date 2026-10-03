# Architecture (editor-in-chief's master plan)

This file fixes the book's skeleton: title, Parts, chapter numbering, chapter file names, concept ownership at chapter level, and running-case beats by chapter. Part brief writers expand each chapter to subsection level in `bible/briefs/part-NN.md` and must not change chapter numbers, titles' substance, or ownership without logging a request in `bible/decisions.md` (section "Change requests").

Working title: **Project Finance: The Complete Practice — From First Principles to Financial Close and Beyond**

Variety of English: American. Base number format: USD millions to one decimal place (USD 412.6 million in prose; tables headed "USD m"). See `bible/style-sheet.md`.

Running cases (detail in `bible/case-bible.md`):

- **Case P (primary)**: greenfield gas-fired combined-cycle power plant with a full domestic gas-supply chain in a fictional emerging-market country; state utility offtaker under a capacity-plus-energy PPA; EPC contractor; O&M operator plus turbine OEM long-term service agreement; lender group of commercial banks, an ECA-covered tranche and a DFI; interest-rate swaps and currency issues.
- **Case T (PPP)**: user-pay toll road PPP (demand risk) in a fictional OECD jurisdiction with common-law PPP practice; from the government's decision to procure through bid, close, ramp-up shortfall, distress and restructuring.
- **Case R (portfolio)**: operating wind, solar and battery storage portfolio in a liberalized energy-only power market with merchant exposure; acquisitions, valuation, hedging, holdco financing and refinancing.

## Chapter list and concept ownership

Ownership rule: a concept listed under a chapter is taught there in full. Every other chapter cross-references it by section number. A chapter may preview a later-owned concept only through a one- or two-sentence explicit forward reference.

### Part I — The Shape of a Deal

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 1 | 01-a-small-deal-start-to-finish.tex | A small deal, start to finish | Simplified end-to-end walkthrough of one small illustrative deal (a ~50 MW solar plant with a 20-year PPA, distinct from the running cases): site, permits, PPA, EPC, model, debt sizing by DSCR in simple form, term sheet, close, construction, operations, repayment. Introduces vocabulary intuitively with forward references to home chapters. | Introduce cast of Case P briefly at the end (the developer gets a call). |
| 2 | 02-what-project-finance-is.tex | What project finance is, and when to use it | SPV and ring-fencing; limited vs non-recourse; contractual web (the book's defined concept); "allocate each risk to the party best able to manage it"; comparison with corporate finance, asset finance and leasing, RBL (overview), acquisition finance, securitization, structured finance; why sponsors, lenders and governments use it (risk isolation, debt capacity, agency costs, partnering, political deterrence) and its costs (transaction cost, time, rigidity, information burden, lender control); when PF is the wrong tool. | Case P sponsor board decides whether to project-finance. |
| 3 | 03-how-project-finance-evolved.tex | How project finance evolved | History: production payments, North Sea, US PURPA and independent power, 1990s emerging-market IPPs, PFI/PPP era, Asian crisis lessons, post-2008 and Basel, institutional and private credit, energy transition, digital infrastructure; the lesson of each era. | — |
| 4 | 04-the-parties-and-the-lifecycle.tex | The parties and the project lifecycle | The cast (sponsors strategic/financial/developers, project company, lender types, offtakers, host governments and regulators, EPC contractors and OEMs, operators, input suppliers, insurers, advisors, agents and trustees, rating agencies, hedge providers): how each earns money, fears, behaves under stress. Lifecycle end to end: origination, development, financing, close, construction, completion, operations, refinancing, sale, decommissioning or handback. | Case P origination: developer identifies the opportunity; development budget; team formed. |

### Part II — Foundations

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 5 | 05-time-value-of-money.tex | Money and time | Interest, compounding, discounting, annuities, NPV, IRR and its traps (multiple IRRs, reinvestment, scale, timing), XNPV/XIRR, payback, real vs nominal, inflation and indexation (CPI/partial indexation mechanics). | Case P: tariff indexation example. |
| 6 | 06-debt-and-interest-rates.tex | Debt and interest rates | Principal, interest, fees; bullet, annuity, straight-line, sculpted (intro only; sculpting math owned by Ch 36); day counts; fixed vs floating; reference rates (SOFR, SONIA, €STR, EURIBOR, term vs compounded in arrears) and LIBOR transition; margins and bps; swaps at intuitive level (swap valuation basics, MTM). | Case P: indicative SOFR-based loan. |
| 7 | 07-accounting-for-the-project-company.tex | Accounting from zero | Three statements and linkages, accruals vs cash, depreciation/amortization, deferred tax, working capital, capitalized interest (IDC) in accounts, reading a project company's accounts. (Sponsor-level accounting is Ch 66.) | Case P: year-1 operating accounts. |
| 8 | 08-leverage-risk-and-cost-of-capital.tex | Leverage, risk and the cost of capital | Capital structure, leverage effect on equity returns, MM intuition, cost of capital, CAPM, WACC vs APV, risk and return; why PF achieves high leverage. | Case P: equity IRR at different gearing. |
| 9 | 09-probability-and-uncertainty.tex | Probability and uncertainty | Distributions, expected values, P50/P90/P99 exceedance, one-year vs ten-year P-values, correlation, sensitivity vs scenario vs Monte Carlo (concepts; implementation in Ch 43). | Case R: wind yield P-values. |
| 10 | 10-law-for-financiers.tex | Law for financiers | How contracts work: reps, warranties, covenants, conditions, indemnities, liability caps, LDs and the penalty rule (Cavendish v Makdessi), force majeure, frustration/impossibility/hardship; common vs civil law; security and insolvency in principle; governing law; courts vs arbitration (overview; detail Ch 54). | Case P: first look at a draft PPA clause. |
| 11 | 11-how-power-assets-and-markets-work.tex | How power assets and electricity markets work | Thermal (OCGT/CCGT/coal, heat rate, efficiency, availability), wind, solar, hydro, nuclear, batteries at financier depth; grids; electricity markets: merit order, marginal pricing, capacity and ancillary markets, nodal vs zonal, curtailment, negative prices; capture prices and cannibalization. | Case P plant technology; Case R market. |
| 12 | 12-how-resource-transport-social-digital-assets-work.tex | How resource, transport, social and digital assets work | Oil, gas, LNG chains; mines and processing; roads, rail, airports, ports; hospitals; water plants; fiber and data centers — at financier depth. | Case P gas field and pipeline; Case T road. |
| 13 | 13-excel-for-project-finance.tex | Excel for project finance | Layout, timing flags (intro), core functions (INDEX/MATCH, XLOOKUP, SUMPRODUCT, EOMONTH, MIN/MAX, OFFSET avoidance), fragile formulas, data tables, goal seek, circularity (concept and copy-paste macro vs closed form), error checks, range names policy. | Small practice workbook. |

### Part III — Risk

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 14 | 14-the-risk-taxonomy.tex | The risk taxonomy | Every risk category listed in coverage map C, defined with mechanism, example and typical bearer. | Case P risk register v1. |
| 15 | 15-analyzing-allocating-pricing-risk.tex | Analyzing, allocating and pricing risk | Method: identify, analyze, quantify, allocate, mitigate, price, monitor; risk matrix construction; residual risk to equity vs debt; "bankable" defined (bankability ladder framework); pass-through and back-to-back; allocation on paper vs in practice; lender downside vs sponsor upside asymmetry. | Case P risk matrix. |
| 16 | 16-the-mitigation-toolkit.tex | The mitigation toolkit | Overview and selection of contracts, insurance, guarantees, reserves, hedges, structural features, sponsor support, credit enhancement — how they combine; cost of each. (Detailed instruments owned elsewhere: insurance Ch 27, reserves Ch 37, hedges Ch 37, guarantees Ch 34/60.) | Case P mitigation plan. |

### Part IV — The Contracts

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 17 | 17-concessions-and-government-support.tex | Concessions, implementation agreements and government support | Concession/project/implementation agreements; government support instruments (guarantees, letters of support, comfort letters); termination events and compensation regimes (principles; PPP-specific formulas Ch 58). | Case P implementation agreement and sovereign support letter; competitive procurement of Case P IPP. |
| 18 | 18-power-purchase-and-tolling-agreements.tex | Power purchase and tolling agreements | PPAs: capacity and energy payments, availability, deemed energy, curtailment, take-or-pay, pass-throughs, indexation, heat-rate and fuel pass-through, dispatch, payment security (overview; detail Ch 59), tolling agreements. | Case P PPA negotiation. |
| 19 | 19-support-schemes-cfds-and-rab.tex | Feed-in tariffs, contracts for difference and regulated asset base models | FiTs, CfDs (two-sided, strike/reference price), RAB model, cap-and-floor, how each allocates risk and shapes financing. | — |
| 20 | 20-merchant-revenue-and-hedges.tex | Merchant revenue, corporate PPAs and hedges | Corporate PPAs physical and virtual; fixed-volume, fixed-shape, as-produced, proxy revenue swaps, floors, collars, tolls for batteries; capacity and ancillary-service revenue; basis and shape risk (Winter Storm Uri). | Case R hedge book. |
| 21 | 21-revenue-contracts-beyond-power.tex | Revenue contracts beyond power | LNG SPAs and tolling (Sabine Pass), pipeline transportation and ship-or-pay, mining offtake (payables, TC/RCs, penalties), streams and royalties, availability payments (contract form; regime design Ch 58), user tolls and tariffs, airport and port revenue models, data-center leases. | Case T toll regime; Case P gas transportation. |
| 22 | 22-the-epc-contract.tex | The EPC contract | Lump-sum turnkey date-certain EPC; delay and performance LDs and calibration; liability caps; bonds, guarantees, retention; variations, EOT, claims; testing and completion; defects liability; contractor credit. | Case P EPC negotiation. |
| 23 | 23-construction-structures-beyond-epc.tex | Construction structures beyond the single EPC | Split and multi-contract structures; EPCM; wraps; interface agreements; FIDIC and other standard forms (Silver/Yellow/Emerald etc.), NEC; supply-chain risk; equipment-supplier credit. | Case T design-build JV. |
| 24 | 24-operations-and-maintenance-contracts.tex | Operations and maintenance contracts | O&M agreements, LTSAs, asset management agreements, major maintenance, performance regimes, fixed vs cost-plus, incentive design. | Case P O&M and LTSA. |
| 25 | 25-inputs-and-access.tex | Inputs and access: fuel, water, grid, land and permits | Fuel and feedstock supply (GSA, take-or-pay, make-up, DCQ), transportation, water, grid connection and interconnection, land rights, permits and transferability. | Case P GSA negotiation. |
| 26 | 26-sponsor-and-shareholder-documents.tex | Sponsor and shareholder documents | Shareholders'/JV agreements, equity contribution agreements, sponsor support and completion guarantees, development and co-development agreements. | Case P JVA among sponsors. |
| 27 | 27-insurance.tex | Insurance | CAR/EAR, DSU/ALOP, marine cargo and marine DSU, TPL, operational all risks, BI, political risk (overview; Ch 60), credit insurance; lender requirements (loss payee, non-vitiation, cut-through, reinsurance assignment); market cycles. | Case P insurance program. |
| 28 | 28-direct-agreements-and-the-contract-map.tex | Direct agreements and the contract map as a system | Direct agreements, consents, step-in and novation; contract map; contract gap scan framework; "Who pays if…?" trace framework. | Case P full contract map and gap scan. |

### Part V — Sources of Capital

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 29 | 29-lenders.tex | The lenders | Commercial banks (business model; capital-rule detail Ch 68), ECAs (OECD Arrangement, cover types, content rules, premia), multilateral and bilateral DFIs (mandates, additionality, preferred creditor status, A/B and parallel loans, guarantees), institutional investors, infrastructure debt funds and private credit. | Case P lender group formed. |
| 30 | 30-project-bonds-and-ratings.tex | Project bonds and ratings | Project bonds, 144A/Reg S, private placements (USPP), green/sustainability bond format (instrument detail Ch 84), sukuk overview (detail Ch 33), bond vs loan, negative carry, how rating agencies analyze projects in construction and operation. | Case P refinancing bond option previewed. |
| 31 | 31-mezzanine-holdco-and-ancillary-facilities.tex | Mezzanine, holdco and ancillary facilities | Mezzanine, holdco debt, equity bridge loans, VAT and working-capital facilities, LC facilities, standby and cost-overrun facilities. | Case R holdco facility. |
| 32 | 32-equity.tex | Equity | Sponsor equity, shareholder loans, contingent and back-ended equity, equity LCs, development premia, farm-downs, infrastructure funds (overview; Ch 47), listed vehicles and yieldcos (SunEdison/TerraForm), US tax equity and tax-credit transfer (dated, flagged). | Case P equity plan. |
| 33 | 33-islamic-project-finance.tex | Islamic project finance | Ijara, istisna'a, wakala, murabaha, musharaka; sukuk; co-financing with conventional tranches (Sadara). | — |
| 34 | 34-blended-concessional-local-currency.tex | Blended, concessional and local-currency finance | Blended and concessional finance, first-loss, guarantees (partial risk/credit guarantees), viability-gap funding, climate funds, local-currency solutions (TCX-type hedges, local bonds). | Case P DFI concessional element. |

### Part VI — Structuring Debt

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 35 | 35-cfads-and-cover-ratios.tex | Cash flow available for debt service and the cover ratios | CFADS definition; DSCR (min/avg), LLCR, PLCR, gearing; base/banking/downside/break-even cases. | Case P CFADS. |
| 36 | 36-sizing-and-sculpting-debt.tex | Sizing and sculpting debt | Sizing by DSCR and gearing; sculpting math; tenor and tail; balloons and mini-perms (hard/soft); grace periods; P90/P99 sizing; merchant tails; how parameters vary by sector, contract quality, market, cycle. | Case P debt sized. |
| 37 | 37-reserves-sweeps-covenants-and-hedging.tex | Reserves, sweeps, covenants and hedging | DSRA, MMRA and other reserves (funding, sizing, LC substitution); cash sweeps; distribution lock-ups; financial and non-financial covenants (design; drafting Ch 51); hedging requirements and hedge profiles. | Case P reserve and hedge structure. |
| 38 | 38-pricing-project-debt.tex | Pricing project debt | Margins and ratchets; arrangement, underwriting, participation, commitment, agency fees; ECA premia in all-in cost; all-in cost of debt; market flex. | Case P pricing. |

### Part VII — Financial Modeling: A Complete Course

Built cell by cell on Case P. Companion model in `model/`.

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 39 | 39-model-architecture-and-timing.tex | Model architecture, standards and timing | Architecture, FAST standard, sheet structure, timelines and flags, inputs and scenario control, model map. | Case P model skeleton. |
| 40 | 40-modeling-construction-and-funding.tex | Modeling construction and funding | Construction budget, sources and uses, drawdown order, equity-first vs pro rata, IDC and fee circularity and clean resolutions. | Case P funding sheet. |
| 41 | 41-modeling-operations-tax-working-capital.tex | Modeling operations, tax and working capital | Revenue and cost builds, indexation, tax (depreciation, losses, interest limitation, withholding), working capital, VAT. | Case P ops and tax. |
| 42 | 42-modeling-the-waterfall-debt-and-reserves.tex | Modeling the waterfall, debt and reserves | Operating waterfall and CFADS in model, sculpting in model, reserves, sweeps, lock-ups, the dividend trap and solutions. | Case P waterfall. |
| 43 | 43-returns-ratios-scenarios-outputs.tex | Returns, ratios, scenarios and outputs | Equity and project returns in model, ratio calculations, sensitivities, scenarios, breakevens, Monte Carlo implementation, dashboards, integrity checks. | Case P outputs. |
| 44 | 44-auditing-a-model.tex | Auditing a model | Model audit process, review checklist, classic errors, auditing someone else's model. | Case P model audit findings. |
| 45 | 45-sector-specific-modeling.tex | Sector-specific modeling | Energy yield and P-values in model, degradation and augmentation, availability and curtailment; traffic ramp-up; mining reserves, grades, recoveries; LNG and commodity-linked revenues; PPP payment mechanisms and deductions. | Case T traffic model; Case R yield model. |

### Part VIII — Equity, Valuation and Investment Decisions

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 46 | 46-equity-returns-and-valuation.tex | Equity returns and valuation through the project's life | Equity IRR, project IRR, NPV, cash yield, multiples; cost of equity and hurdles by stage; valuation at each development milestone; development economics and where value is created. | Case R valuation of an acquisition target. |
| 47 | 47-bidding-acquisitions-and-funds.tex | Bidding, acquisitions and infrastructure funds | Bid pricing in competitive tenders and winner's curse; buying and selling operating assets (process, SPA, W&I, locked box vs completion accounts); portfolio construction; how infra funds think, invest and are paid. | Case P tariff bid; Case T bid; Case R acquisition. |

### Part IX — Due Diligence

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 48 | 48-technical-resource-and-market-diligence.tex | Technical, resource and market diligence | Independent engineer; resource and reserves; market and price curves; traffic and demand studies; scoping, reading, challenging. | Case P IE report walkthrough; Case T traffic study. |
| 49 | 49-legal-insurance-model-tax-integrity-diligence.tex | Legal, insurance, model, tax and integrity diligence | Legal and regulatory DD; insurance advisor; model audit engagement; tax and accounting DD; counterparty credit; KYC, sanctions, anti-corruption DD. | Case P legal DD report. |
| 50 | 50-environmental-and-social-risk.tex | Environmental and social risk and standards | ESIA, ESMP, ESAP; IFC Performance Standards; Equator Principles; World Bank ESF; community engagement; land acquisition and resettlement; indigenous peoples and FPIC; biodiversity; labor and human rights; why E&S failure is credit risk. | Case P resettlement and ESAP. |

### Part X — Finance Documents and the Legal Framework

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 51 | 51-the-finance-documents.tex | The finance documents | Document set and flow (mandate, commitment letters, term sheets, CTA, facility agreements, fee letters, ISDA overview), reps, CPs, covenants, EoDs, remedies, equity cures, permitted debt and distributions, change of control, amendments and voting; LMA, LSTA, APLMA. | Case P CTA. |
| 52 | 52-security-accounts-and-waterfall.tex | Security, accounts and the cash waterfall | Security package and purpose; common-law vs civil-law (trusts vs parallel debt, floating charges); perfection; enforcement as going concern (principles; process Ch 64); accounts structure and cash waterfall in full. | Case P accounts agreement. |
| 53 | 53-intercreditor-arrangements.tex | Intercreditor arrangements | Tranches, voting, ECA and DFI rights, hedge counterparties, standstills, enforcement, conventional–Islamic interface. | Case P ICA. |
| 54 | 54-governing-law-disputes-and-investment-protection.tex | Governing law, disputes and investment protection | Governing law and jurisdiction choices, arbitration (ICC, LCIA, ICSID, UNCITRAL), enforcement of awards (New York Convention), sovereign immunity and waiver, stabilization clauses, investment treaties and treaty structuring. | Case P dispute clause. |

### Part XI — The Deal Process and Negotiation

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 55 | 55-running-a-financing-to-close.tex | Running a financing to close | Financing strategy (club, underwritten, best efforts; bank vs bond), financial advisor role, IM and lender presentations, credit approval inside a bank, syndication and sell-down, documentation management, CPs, signing vs financial close, funds flow and closing mechanics, timelines and critical paths. | Case P financial close. |
| 56 | 56-negotiating-project-finance.tex | Negotiating project finance | What is market and why; levers; trade-offs on every key term; tactics, sequencing, escalation; market cycle; negotiating with governments, contractors, offtakers and lenders; term sheet markup walkthrough. | Case P term sheet negotiation. |

### Part XII — Public–Private Partnerships

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 57 | 57-the-public-sector-case-for-ppps.tex | The public-sector case for PPPs | Rationale and critiques; value for money and PSC; affordability; fiscal and statistical treatment and contingent liabilities; PPP units and programs; unsolicited proposals; UK PFI history and end. | Case T government decision to procure. |
| 58 | 58-procuring-and-designing-ppps.tex | Procuring and designing PPPs | Procurement (prequalification, competitive dialogue, RFPs, BAFO, evaluation); delivery models (DBFOM, BOT, BOOT, BOO; availability vs user-pay); payment mechanisms and deduction regimes; handback; change, benchmarking, market testing; termination regimes and compensation formulas; refinancing gain sharing; standard contract guidance; lessons. | Case T procurement and preferred bidder. |

### Part XIII — International and Emerging Markets

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 59 | 59-country-currency-and-payment-risk.tex | Country, currency and payment risk | Country and sovereign risk analysis; currency risk and solutions; offshore accounts; payment security for weak offtakers (LCs, escrow, guarantees, liquidity facilities). | Case P offtaker payment crisis and currency shock. |
| 60 | 60-political-risk-and-its-protection.tex | Political risk and its protection | PRI (MIGA, ECAs, private market); multilateral halo; obsolescing bargain; host-government relations and local content; corruption risk and anti-bribery laws (FCPA, UKBA); sanctions; disputes and treaty claims in practice. | Case P political-risk cover. |

### Part XIV — The Project Through Its Life

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 61 | 61-construction-to-completion.tex | Construction to completion | Drawdowns and certification, contingency management, monitoring, change orders, delays and LD flows, insurance claims in practice, contractor distress, completion tests, release of sponsor support. | Case P construction delay, overrun, insurance claim, completion. |
| 62 | 62-operating-the-project.tex | Operating the project as owner and lender | Reporting and compliance, budgets, ratio testing and distributions, maintenance, performance management, waivers and amendments, asset optimization (repowering, life extension, hybridization). | Case P operations; covenant breach and waiver. |
| 63 | 63-refinancing-and-secondary-sales.tex | Refinancing, repricing and secondary sales | Refinancing and repricing; secondary sales and M&A execution of stakes; holdco leverage in practice. | Case P refinancing and partial sale; Case R refinancing. |
| 64 | 64-distress-restructuring-and-enforcement.tex | Distress, restructuring and enforcement | Early warning signs, standstills, waivers (in distress), amend-and-extend, sponsor support, debt-for-equity, cash sweeps, distressed sales, enforcement over shares and assets, insolvency regimes (Ch 11, UK schemes and restructuring plans, civil-law regimes), PPP-specific dynamics, role of the state. | Case T distress and restructuring. |
| 65 | 65-end-of-life.tex | Decommissioning, handback and end-of-life value | Decommissioning obligations and reserves, handback regimes in practice, life extension economics, terminal value. | Case P handback planning; Case R decommissioning. |

### Part XV — Accounting, Tax and Regulation

| Ch | File | Title | Owns | Case beats |
|---|---|---|---|---|
| 66 | 66-accounting-for-projects-and-sponsors.tex | Accounting for projects and sponsors | Consolidation and equity accounting, joint arrangements, service concessions (IFRIC 12; ASC 853), leases embedded in offtake contracts, hedge accounting, ECL, how accounting goals shape structures. | Case P sponsor accounting. |
| 67 | 67-tax-structuring.tex | Tax structuring | Holding structures, treaties, withholding taxes, interest limitation and thin cap, transfer pricing, VAT during construction, incentives and holidays, Pillar Two global minimum tax. | Case P holding structure. |
| 68 | 68-capital-rules-for-banks-and-insurers.tex | Capital rules for banks and insurers | Basel framework for PF (slotting, IRB, output floor), insurer capital (Solvency II infrastructure classes), how both shape who lends and price. | — |

### Part XVI — Sector Deep Dives

Each: industry economics, how the asset works (cross-ref Ch 11/12), revenue models, key risks, contract set, typical financing terms (dated ranges), modeling specifics (cross-ref Ch 45), landmark deals and failures.

| Ch | File | Title |
|---|---|---|
| 69 | 69-thermal-power.tex | Thermal power |
| 70 | 70-onshore-wind-and-solar.tex | Onshore wind and solar |
| 71 | 71-offshore-wind.tex | Offshore wind |
| 72 | 72-hydropower-and-geothermal.tex | Hydropower and geothermal |
| 73 | 73-storage-transmission-and-interconnectors.tex | Storage, transmission and interconnectors |
| 74 | 74-nuclear.tex | Nuclear power |
| 75 | 75-upstream-and-midstream-oil-and-gas.tex | Upstream and midstream oil and gas (incl. reserve-based lending) |
| 76 | 76-lng-and-fpsos.tex | LNG liquefaction, regasification and FPSOs |
| 77 | 77-industrial-projects.tex | Refining, petrochemicals and manufacturing (gigafactory) finance |
| 78 | 78-mining-and-critical-minerals.tex | Mining, metals and critical minerals |
| 79 | 79-roads-bridges-and-tunnels.tex | Toll roads, bridges and tunnels (Case T ramp-up) |
| 80 | 80-rail-airports-and-ports.tex | Rail, urban transit, airports and ports |
| 81 | 81-social-infrastructure-water-and-waste.tex | Social infrastructure, water, desalination and waste-to-energy |
| 82 | 82-digital-infrastructure.tex | Telecoms, fiber, towers and data centers |
| 83 | 83-hydrogen-ccs-and-sustainable-fuels.tex | Hydrogen and derivatives, carbon capture and storage, sustainable fuels |

### Part XVII — Sustainability

| Ch | File | Title | Owns |
|---|---|---|---|
| 84 | 84-sustainable-finance.tex | Sustainable finance and climate risk | Green, social, sustainability and sustainability-linked loans and bonds (GBP, GLP, SLLP, SLBP), taxonomies (EU and others), transition finance, carbon markets (compliance, voluntary, Article 6), climate risk assessment (physical and transition; TCFD/ISSB), greenwashing risk. |

### Part XVIII — The Financier's Craft and the Frontier

| Ch | File | Title | Owns |
|---|---|---|---|
| 85 | 85-screening-deals-and-reading-data-rooms.tex | Screening deals and reading data rooms | One-hour deal screen framework; the questions to ask on any deal; reading a data room. Case P and others screened. |
| 86 | 86-credit-papers-and-investment-committees.tex | Credit papers and investment committees | Writing a credit paper and IC memo; presenting to a committee; full Case P credit paper. |
| 87 | 87-the-practitioners-craft.tex | The practitioner's craft and career | Managing advisors and a deal team; running a timetable; relationships and reputation; ethics and integrity; career-limiting mistakes; career paths; deliberate plan for building judgment; staying current. |
| 88 | 88-the-frontier.tex | The frontier: evaluating new structures | Frameworks for evaluating new structures; energy-transition gaps, AI/data-center power demand, new nuclear and SMRs, long-duration storage, hydrogen, CCS, adaptation and resilience, critical minerals, private credit, local-currency and blended solutions, digital deal execution. |

### Matter (Phase 6, in `matter/`)

- 00-front-matter.tex: how to use the book, study plan, how to work exercises and model builds, general caveat (stated once).
- 89-capstone.md: capstone end-to-end deal simulation with full expert solution.
- 90-final-examination.tex: final exam with worked answers.
- 91-glossary.tex, 92-formula-sheet.tex, 93-checklists-and-templates.tex, 94-index-of-cases.tex.
