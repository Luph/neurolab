# Case Bible

Version 1.2, October 3, 2026 (consolidation after the round 1 brief revisions: storyline rows and figure-register users merged from the revisers' requests, ledger conflicts resolved in the ledger's favor, the Case T lenders' traffic adviser added, the round 1 illustrative names registered in Part 5A; cells and rows changed in this version carry "(round 1)"; see `reviews/blueprint/consolidation-B-log.md`). Version 1.1, October 3, 2026 (Version 1.0 amended after the blueprint review: Case P model and ledger v1.2, the construction currency hedge of D-114, the SEKA LC value of P-C44, the overrun funding of P-C43, the annex amendments merged into Parts 6 and 7, and the Case T cast additions; see `reviews/blueprint/central-fixes-log.md`). Owner: Case Bible designer, under the editor-in-chief. Binding on every writer, reviewer, and modeler.

## 0. How to use this file

The book follows three fictional running cases. This file fixes everything about them that a writer could otherwise invent: the countries, the institutions, the people, the contracts, the dates, the assumption values, and the order in which events reach the reader. It does not contain model outputs. Debt quantum, interest during construction, ratios, returns, valuations, and every other computed figure come from the reference models built from the three input files in `book/model/`:

| Case | Input file | Model periodicity |
|---|---|---|
| Case P | `model/inputs_case_p.json` | Construction monthly (Month 1 = August 2018); operations semiannual, periods ending June 30 and December 31 |
| Case T | `model/inputs_case_t.json` | Construction quarterly (stub from May 27, 2015); operations semiannual, periods ending June 30 and December 31 |
| Case R | `model/inputs_case_r.json` | Annual, calendar years 2022 to 2059 |

Four rules govern use.

1. Writers take running-case numbers from this file (assumptions) or from the figure ledger (model outputs, keyed by the figure IDs in Section 7). A writer never computes a running-case figure. If a chapter needs a number that has no figure ID, the writer reports it in the status note and the editor-in-chief adds it.
2. Where this file states an expected range for a model output (for example, "senior debt expected between USD 600 million and USD 660 million"), the range is a design target for the modelers and a sanity check for reviewers. It is never printed in the book.
3. Every change to a case assumption after Version 1.0 goes into the change log (Section 8) with its date in story, the chapter where the reader learns of it, the old and new values, and the source.
4. The JSON files use ASCII names without accents (Belanou, Talme, Sombe, Societe). The book prints the accented forms given here (Bélanou, Talmé, Sombé, Société).

Story dates and book order differ. The book teaches in concept order, so a reader meets the 2022 operating accounts of Case P in Chapter 7, before the 2018 financial close is narrated in Chapter 55. Each storyline row in Section 6 states the story date, and a writer whose installment jumps forward or back in time says so in the first sentence of the installment ("Four years after financial close, ..."). The concept-ownership rule applies to the installment, not to the story: a Chapter 7 installment may show the 2022 accounts because Chapter 7 teaches accounts, but it may not explain the DSCR covenant breach, because DSCR is taught in Chapter 35.

Annex TR (`bible/case-bible-annex-tr.md`) resolves the Case T and Case R gaps raised by the brief writers and adds name-register entries; it takes precedence over this file where they differ. New model inputs it creates are listed in `bible/case-tr-input-requests.md`.

Style for every number printed from this file follows `bible/style-sheet.md`: USD 412.6 million in prose, "USD m" in table headers, ratios to two decimals with "x", dates as October 3, 2026 in prose and ISO in tables.

---

# Part 1. Case P: the Bélanou Combined Cycle Power Project, Republic of Kessara

## 1.1 The Republic of Kessara

Kessara is a fictional coastal republic on the Gulf of Guinea in West Africa. It is described in the book only generically: a country of about 27.4 million people in 2015 with a 540 km Atlantic coastline, a capital and main port at Dabakro, an offshore gas province discovered in the 2000s, a hydro-heavy northern grid, and a French-derived civil-law system inherited at independence in 1960. The book never places it next to a named real country. Its demonym is Kessaran.

The name was chosen because it reads as a plausible West African state name and belongs to no real country, region, or well-known city (checked by web search on October 3, 2026: the nearest real uses are a Bangkok hotel, a Thai given name, and Keesara, an Indian village; see decision D-101).

### Macro profile

| Item | 2015 | 2018 | 2021 | 2022 | 2023 | 2025 |
|---|---|---|---|---|---|---|
| Population (million) | 27.4 | 29.5 | 31.8 | 32.6 | 33.4 | 35.1 |
| GDP (USD billion, current) | 48.7 | 58.3 | 71.9 | 66.2 | 60.8 | 70.4 |
| Real GDP growth (%) | 5.8 | 6.1 | 4.8 | 3.1 | 2.4 | 4.6 |
| Kessaran CPI, annual average change (%) | 8.7 | 7.6 | 10.6 | 26.3 | 34.8 | 12.4 |
| KCR per USD, annual average | 418.6 | 516.8 | 603.5 | 742.6 | 1,048.3 | 1,029.7 |
| KCR per USD, year end | 436.2 | 531.7 | 618.7 | 897.4 | 1,112.6 | 1,018.2 |
| Central bank policy rate, year end (%) | 14.0 | 13.5 | 13.5 | 19.0 | 27.0 | 18.0 |

The full annual and semiannual paths, including 2016, 2017, 2019, 2020, 2024 and 2026, are in `inputs_case_p.json` under `macro` and `country`. The cauri peaked at KCR 1,186.0 per USD on June 30, 2023.

US macro paths (decision D-046; round 1). The US CPI, 6M USD LIBOR, Term SOFR and swap-rate paths in `inputs_case_p.json` are stylized illustrative paths close to, but not identical with, the official series (for example, P-F02's September 2021 US CPI reading of 111.60 on a November 2016 base, against about 113.66 for BLS CPI-U rebased over the same months). Chapters label them "Case P index (illustrative)" or "Case P rate path (illustrative)" and never present them as BLS, ICE or CME values; facts about the real series come only from `facts/t-us-cpi.md` and `facts/t-reference-rates.md`. The Kessaran series above are fictional by construction.

Sovereign rating (one agency, foreign currency): B+ stable from 2015; B stable from May 2020 (pandemic); B- negative from September 2022; CCC+ from March 2023; B- stable from November 2024; B stable from May 2026. In 2023 Kessara agreed a three-year stabilization program with its multilateral creditors. The book never names the lending institution (decision D-007) and refers to it as "the stabilization program."

### Currency

The Kessaran cauri, code KCR, plural cauris. The name recalls the cowrie shells once used as money along the West African coast. KCR is not an ISO 4217 code. The cauri floats under a managed regime; the Central Bank of Kessara (Banque Centrale du Kessara) runs an interbank market and publishes a daily mid rate. Exchange controls require Central Bank authorization for offshore accounts; Bélanou Power received Exchange Control Authorization No. 2018-114 at financial close.

### Legal system

Kessara is a civil-law jurisdiction. Its Civil Code and Commercial Code follow the French codes of the 1960s with later amendments; its company law provides for the société anonyme (SA); its security law recognizes pledges (nantissements) over shares, receivables and bank accounts, a pledge over the business as a going concern (nantissement du fonds de commerce), and mortgages over registered land rights, but not the common-law trust or the English floating charge. The courts follow the doctrine of imprévision only where a contract or statute admits it, and the Kessaran Civil Code (as amended in 2011) does allow a court to adapt a contract on a party's request after an unforeseeable change of circumstances that makes performance excessively onerous. Kessara is party to the New York Convention (since 1998) and a member of ICSID; its Arbitration Law of 2004 follows the UNCITRAL Model Law.

Case P is the book's civil-law case and Case T the common-law case (decision D-102), so the reader sees parallel debt, the security agent without a trust, the business pledge, and judicial hardship adaptation in Case P, and trusts, floating charges, the scheme-style restructuring plan, and the common-law penalty rule in Case T.

### Legal and institutional framework for IPPs

| Institution | Role in Case P |
|---|---|
| Ministry of Energy and Hydrocarbons (MEH) | Sector policy; signs the Implementation Agreement; Secretary-General Abdoulaye Ndao-Sylla |
| Ministry of Economy and Finance (MEF) | Issues the Government Guarantee; houses the PPP Unit |
| Unité des Partenariats Public-Privé (PPP Unit), MEF | Runs IPP and PPP procurement under the PPP Law; head Clémentine Agbo-Lawson |
| Office de Régulation de l'Énergie du Kessara (OREK) | Licenses generation; approves PPA tariffs for pass-through into SEKA's retail tariff; collects a levy of 0.25% of non-fuel revenue |
| Société d'Électricité du Kessara (SEKA) | State-owned vertically integrated utility; single buyer and system operator; offtaker under the PPA; CFO Hyacinthe Dossa |
| Société Nationale des Hydrocarbures du Kessara (SNHK) | State oil and gas company; 35% partner in the Sombé West field; gas aggregator and seller under the GSA |
| Gazoduc Côtier du Kessara SA (GCK) | SNHK subsidiary owning the 112 km coastal pipeline (68 km offshore, 44 km onshore); transporter under the GTA |
| Banque Centrale du Kessara | Exchange controls, FX allocation |
| Union Bancaire du Kessara (UBK) | Largest local commercial bank; onshore account bank, SEKA's LC issuer, VAT facility lender |

The laws: the Electricity Code (Law No. 2009-112) opened generation to independent power producers (IPPs) under a single-buyer model; the PPP Law (Law No. 2013-047) governs competitive procurement of IPPs and PPPs, permits unsolicited proposals only with a Swiss challenge, and authorizes the Minister of Economy and Finance to issue guarantees within an annual ceiling set by the Finance Act; the Investment Code (2012) grants IPP incentives (tax holiday, import duty and VAT exemptions on plant equipment, withholding tax exemption on interest paid to DFIs and on officially supported export credits). Finance Act 2024 introduced a 30% of tax EBITDA interest limitation (with grandfathering) and a 15% tax on indirect transfers of Kessaran assets, both effective January 1, 2025.

### The power sector in 2015

In 2015 Kessara had 2,310 MW installed but only 1,780 MW available against a peak demand of 2,140 MW growing at 7.4% a year. The mix: 640 MW hydro on the northern Moraba River cascade (output falling in dry years), 820 MW of aging heavy fuel oil and diesel units, 690 MW of SEKA-owned open-cycle gas turbines, and 160 MW of other capacity. Load-shedding of up to eight hours a day in Dabakro in the 2014 dry season pushed the government to announce an Emergency Power Plan in March 2015 whose centerpiece was a competitively procured 450 MW to 650 MW gas-fired IPP at a government-allocated coastal site at Bélanou, 38 km east of Dabakro, beside the landfall of the coastal pipeline.

The gas comes from Sombé West, an offshore field in 72 m of water operated by Halbeck Energy (fictional, 65%) with SNHK (35%). Sombé West started production in 2019 with certified 2P reserves of 1,140 billion cubic feet (2017 certification), sufficient for a 22-year GSA at Bélanou's contract quantities plus existing SEKA demand. Halbeck's upstream financing (a reserve-based loan) is a Chapter 75 illustration and is never a Case P party.

## 1.2 The project

Bélanou Power SA (the project company) builds, owns, operates, and at the end of the PPA transfers to SEKA (BOOT) a 2x1 combined-cycle gas turbine (CCGT) plant.

| Item | Value | Source key |
|---|---|---|
| Configuration | Two F-class gas turbines (Bergmark BT-9F), two triple-pressure reheat heat recovery steam generators (HRSGs), one reheat condensing steam turbine, once-through seawater cooling, gas only | `plant.configuration` |
| Site reference conditions | 30 °C, 1.013 bar, 80% relative humidity | `plant.site_reference_conditions` |
| Guaranteed net output (EPC, new and clean) | 588.4 MW | `plant.guaranteed_net_output_mw` |
| Guaranteed net heat rate (EPC, LHV, 100% load) | 6,261 kJ/kWh (net efficiency about 57.5%) | `plant.guaranteed_net_heat_rate_kj_per_kwh_lhv` |
| PPA contracted heat rate (LHV, 100% load) | 6,323 kJ/kWh, plus 0.10% per year degradation allowance | `ppa.contracted_heat_rate...` |
| Part-load heat-rate penalty | 75% load +4.2%; 50% load +11.8%; average at base dispatch +2.3% | `plant.part_load...` |
| HHV/LHV ratio for gas | 1.108; 1 MMBtu = 1,055,056 kJ | `plant.hhv_to_lhv_ratio` |
| Degradation | Output: 0.15% a year non-recoverable plus 1.0% average recoverable. Heat rate: 0.12% a year plus 0.8% average recoverable | `plant.degradation` |
| Availability by operating year (8-year cycle) | 93.8, 92.9, 93.8, 90.6 (hot gas path), 93.8, 92.9, 93.8, 88.7 (major inspection and steam turbine overhaul) | `plant.availability_profile...` |
| Dispatch factor when available | Base 76.5%; banking 72.0%; downside 58.0% | `plant.dispatch_factor...` |
| Gas turbine operation | 8,059 hours and 38 starts per gas turbine per year (base); 10 equivalent operating hours (EOH) per start | `plant.gt_hours_and_starts` |
| Completion test results (November 2021) | 581.9 MW; 6,286 kJ/kWh | `plant.tested_...` |

The plant connects at 225 kV to SEKA's Bélanou substation, built by SEKA under the PPA's interconnection schedule. The gas lateral and metering station belong to GCK.

## 1.3 Capital cost

The budget at financial close, before financing costs, is USD 710.99 million. The model adds interest during construction (IDC), commitment fees, upfront and arrangement fees, the ECA premium, agency fees during construction, and the initial funding of the debt service reserve account (DSRA) at COD. The total funding requirement is a model output (figure P-F07) and is expected to fall between USD 830 million and USD 870 million.

| Use of funds (USD m) | Amount |
|---|---|
| EPC contract price | 571.84 |
| of which offshore portion (paid in USD) | 489.17 |
| of which onshore portion (fixed in KCR at 519.4 per USD) | 82.67 |
| Owner's costs | 46.18 |
| of which owner's engineer | 9.86 |
| of which project company staff and administration | 11.27 |
| of which site preparation and access road | 4.92 |
| of which initial spares | 8.31 |
| of which start-up fuel net of test-energy sales | 6.74 |
| of which resettlement and community (RAP implementation) | 5.08 |
| Insurance during construction | 7.62 |
| Development costs reimbursed at financial close | 21.43 |
| Development fee to sponsors at financial close | 11.20 |
| Lenders' advisors and legal | 8.97 |
| Contingency | 38.40 |
| Initial working capital (spares inventory and fuel) | 5.35 |
| Subtotal before financing costs | 710.99 |
| IDC, fees, ECA premium, DSRA funding | Model (P-F07) |

The EPC contract price includes a limited notice to proceed (LNTP) payment of USD 14.20 million made in February 2018 and funded by the sponsors before financial close; it is credited as equity at close. The export contract value eligible for ECA support (Bergmark's gas turbine package and Lindauer's home-country supply) is USD 263.7 million. The monthly EPC payment profile (10% advance at notice to proceed, progress payments, 7.5% at taking-over against a retention bond) is in the JSON file in both the base (33-month) and actual (40-month) versions.

VAT at 18% applies to the onshore EPC portion and is recoverable after a nine-month lag; imported plant is exempt from duty and VAT under the Investment Code. UBK provides a KCR 7,900.0 million VAT facility at the policy rate plus 2.50%, repaid from refunds.

## 1.4 The contract set

### Power purchase agreement (PPA)

Signed October 12, 2017 between Bélanou Power SA and SEKA; governed by Kessaran law; disputes to ICC arbitration seated in Paris, in French and English. Term 25 years from COD. BOOT: the plant transfers to SEKA at expiry for USD 1, subject to handback conditions certified by an independent engineer.

The tariff is denominated in USD, invoiced monthly in USD, and paid in KCR at the Central Bank mid rate on the business day before payment. It has four parts.

| Tariff component | Base value (prices of November 30, 2016) | Indexation |
|---|---|---|
| Capital charge | USD 14.36/kW-month | 80% fixed; 20% indexed to US CPI |
| Fixed O&M charge | USD 2.31/kW-month | 62% indexed to US CPI; 38% converted to KCR at the bid base rate of 462.35, indexed to Kessaran CPI, and reconverted to USD at the invoice-date rate (contract term, Annex P 1.1.5; the model uses the 2022 H1 average rate as its proxy, so P-F02 prints "2022 H1 average"; round 1) |
| Variable O&M charge | USD 3.86/MWh | 70% US CPI; 30% Kessaran CPI with the same reconversion |
| Fuel charge | Pass-through | Net energy (MWh) times the contracted heat rate at the dispatched load times 1.108 divided by 1,055,056, times the GSA gas price (USD/MMBtu); plus GTA charges and dispatch-caused GSA take-or-pay amounts as pass-throughs |

Indices reset January 1 and July 1 using values lagged three months. Capacity payments equal the capacity charge times contracted capacity times the lesser of 1 and availability divided by the 90.0% target; there is no bonus above target. Contracted capacity is 588.4 MW until the completion tests reset it to the tested 581.9 MW.

Payment security: a standby letter of credit issued for SEKA by UBK and confirmed by Castellan Bank equal to two months of estimated capacity charges plus one month of estimated energy charges (the amount under the Annex P 1.1.5 formula, figure P-F39: USD 36.2 million at the January 1, 2022 reset and USD 36.6 million at the January 1, 2023 reset; P-C44), to be replenished within 30 days of any drawing; a Government Guarantee from the Ministry of Economy and Finance covering SEKA's payment obligations and termination amounts, capped at USD 1,250 million; and a USD 41.5 million partial risk guarantee from the Atlantic Basin Development Bank (ABDB) that backs Castellan's reimbursement claim on the Republic if it pays under the LC confirmation and SEKA and the government fail to reimburse it. A donor facility subsidizes the PRG fee to 0.75% a year; this is Case P's concessional element (Chapter 34). Late payment interest is 6M Term SOFR plus 2.00% (6M LIBOR plus 2.00% before 2023).

Other terms: PPA delay liquidated damages payable to SEKA of USD 94,150 per day after the Required Commercial Operation Date (RCOD), originally July 31, 2021, capped at USD 25.0 million; RCOD extended day for day for force majeure and SEKA risk events; change in Kessaran law affecting costs by more than USD 0.5 million a year passed through, excluding changes to dividend withholding tax; no refinancing gain-sharing. Termination compensation:

| Termination ground | Compensation payable by SEKA, backed by the Government Guarantee |
|---|---|
| SEKA or government default; political force majeure | Senior debt outstanding plus swap breakage plus the equity amount, which is the greater of the NPV of projected distributions at 14.5% and equity contributed compounded at 14.5% less distributions received |
| Project company default | 100% of senior debt outstanding (principal and non-default interest, excluding default interest and swap breakage beyond scheduled hedges), less insurance proceeds |
| Natural force majeure lasting more than 180 days | Senior debt outstanding plus equity contributed less distributions received |
| Expiry | USD 1 |

### Implementation Agreement and Government Guarantee

The Implementation Agreement (IA) between the Republic (represented by MEH) and the project company, signed October 12, 2017, governed by Kessaran law with a stabilization clause, disputes to ICSID arbitration. It grants the site rights, tax and customs incentives, convertibility and transfer undertakings (the Republic undertakes that the Central Bank will make foreign exchange available for debt service, O&M, and distributions), and a put option obliging the Republic to buy the plant for the PPA termination amount on a SEKA payment default lasting 90 days. The Government Guarantee (Garantie de l'État) is issued the same day by MEF.

### Gas sale agreement (GSA)

SNHK sells gas from Sombé West to the project company for 22 years. Daily contract quantity (DCQ) 72,400 MMBtu; maximum daily quantity (MDQ) 96,500 MMBtu; annual contract quantity equals DCQ times days. Take-or-pay at 80% of ACQ with make-up recoverable over three years. Deliver-or-pay: shortfalls below 95% of nominations earn a 25% price discount on the shortfall and deemed availability under the PPA. Price USD 5.86/MMBtu (GCV) on January 1, 2018, escalating 2.0% each January 1. Payment 30 days after month end, in KCR. First gas for commissioning: March 2021. Signed November 30, 2017.

### Gas transportation agreement (GTA)

GCK transports gas through the 112 km coastal pipeline. Reserved capacity 96,500 MMBtu a day, 100% ship-or-pay. Reservation charge USD 0.62/MMBtu of reserved capacity, commodity charge USD 0.19/MMBtu (both 2018 prices, escalating 1.5% a year). All GTA charges pass through to SEKA. Signed November 30, 2017.

### EPC contract

Lump-sum turnkey, date-certain, fixed-price EPC contract signed December 19, 2017 with a joint and several consortium of Lindauer Kraftwerksbau AG (leader, 82%) and Bati-Kessara SA (civil works, 18%). Lindauer's parent, Lindauer Holding AG, gives a full-scope parent company guarantee. Lindauer's home country is a Western European OECD member that the book never names (decision D-104).

| EPC term | Value |
|---|---|
| Guaranteed completion date | April 30, 2021 (33 months from notice to proceed on August 1, 2018) |
| Delay liquidated damages | USD 247,300 per day; cap 18% of price (USD 102.9 million) |
| Output performance LDs | USD 2,150 per kW below 588.4 MW |
| Heat-rate performance LDs | USD 180,400 per kJ/kWh above 6,261 kJ/kWh |
| Performance LD cap | 12% of price |
| Aggregate LD cap | 30% of price |
| Overall liability cap | 100% of price |
| Minimum performance (rejection) levels | Output at least 95% of guarantee; heat rate no more than 3% above guarantee |
| Performance bond | 10% of price |
| Advance payment | 10% against an advance payment guarantee |
| Retention | 5%, released at taking-over against a retention bond |
| Defects liability period | 24 months |
| Completion tests | Corrected net output and heat rate; 720-hour reliability run at 95% availability or better; emissions and grid code compliance |

### Long-term service agreement (LTSA)

Signed March 27, 2018 with Bergmark Turbinen AG (the LTSA provider), covering both gas turbines for 16 years or 128,000 EOH per unit. Fixed fee USD 2.64 million a year; variable fee USD 486 per EOH per gas turbine (2018 prices, US CPI). Bergmark supplies parts, repairs, and field service for combustion inspections, hot gas path inspections and major inspections, and guarantees availability (bonus or malus of USD 0.2 million per point between 90% and 95%; modeled as nil in the base case).

### O&M agreement

Signed April 30, 2018 with Kilnworth Operations Services Ltd (the O&M operator), a Kilnworth affiliate, for 10 years renewable. Fixed fee USD 7.92 million a year (2018 prices; 65% USD indexed to US CPI, 35% KCR indexed to Kessaran CPI). Availability incentive plus or minus USD 0.60 million a year, linear between 89% and 95% availability and zero at 92%. 96 staff at steady state, 71 of them Kessaran by OY3 (local content undertaking in the IA).

### Other operating costs

All in 2018 prices unless stated: operational insurance USD 4.37 million a year (US CPI, plus an 18.0% market step-up from H2 2022); project company general and administrative costs USD 3.18 million a year (half US CPI, half Kessaran CPI); land lease and permits KCR 368.0 million a year (Kessaran CPI); community development fund 0.30% and OREK levy 0.25% of non-fuel revenue; variable consumables USD 1.08/MWh; major maintenance outside the LTSA of USD 9.47 million in OY8, OY16 and OY24 (steam turbine and balance of plant) and USD 2.18 million in OY4, OY12 and OY20 (HRSG and balance of plant); agency and account fees of USD 255,000 a year; a handback reserve of USD 1.85 million a year from OY20.

### Insurance program

Arranged by Fenwick Lowe Insurance Brokers, reviewed for lenders by Marchbank Risk Advisory, fronted locally by Assurances Générales du Kessara (AGK) with 95% reinsured offshore, cut-through and assignment of reinsurance to the lenders.

| Cover | Key terms |
|---|---|
| Erection all risks (EAR) | Sum insured USD 640.0 million; deductible USD 1.0 million |
| Delay in start-up (DSU) | Indemnity period 18 months; time deductible 45 days; daily indemnity USD 228,400 (debt service plus fixed costs) |
| Marine cargo and marine DSU | USD 310.0 million; marine DSU deductible 45 days |
| Third-party liability | USD 50.0 million construction; USD 75.0 million operations |
| Operational property damage and business interruption | USD 690.0 million; deductible USD 2.5 million; BI indemnity 18 months, 60-day deductible |
| Political risk insurance | Private-market cover for 90% of the commercial tranche's principal and interest (expropriation, currency inconvertibility and transfer, political violence, non-honoring of the Government Guarantee); premium 1.15% a year on the insured amount, paid by the project company |

### Land

A 45-year emphyteutic lease (bail emphytéotique) of 62 hectares from the Republic, registered at the land registry so that it can be mortgaged. Resettlement of 214 households from the site and the pipeline corridor under a Resettlement Action Plan (RAP) prepared to the IFC Performance Standards, which the ABDB requires (the book names the IFC Performance Standards as the standard; IFC is not a party).

## 1.5 Sponsors and equity

| Sponsor | Description | Pre-close stake | Stake at financial close | After 2026 sale |
|---|---|---|---|---|
| Kilnworth Power International | London-headquartered IPP developer and owner, 4.1 GW in operation across Africa, South Asia and the Middle East in 2015; holds through Kilnworth Bélanou Holdings, a holding company in a jurisdiction with a tax treaty with Kessara | 70% | 60% | 36% |
| Groupe Talmé | Dabakro family conglomerate (cement, logistics, real estate, a 1990s diesel IPP), founded by Ousmane Talmé in 1978 | 30% | 25% | 25% |
| ABDB Infrastructure Equity Fund | Equity fund managed by the ABDB's equity arm | – | 15% | 15% |
| Coldharbour Infrastructure Income Fund | London-based infrastructure income fund backed by pension investors | – | – | 24% |

The ABDB fund bought its 15% at financial close from Kilnworth (10 points) and Talmé (5 points), not strictly pro rata to their stakes (Annex P 1.14.2, P-C24; round 1 alignment), paying its share of development costs plus a development premium of USD 4.85 million (USD 3.2333 million to Kilnworth and USD 1.6167 million to Talmé; P-F49).

Development: Kilnworth's board approved a development budget of USD 14.8 million in 2015; costs to financial close were USD 21.43 million, reimbursed at close together with a development fee of USD 11.20 million.

Equity is 25% of the total funding requirement, contributed 20% as share capital and 80% as USD shareholder loans at 9.50% (interest capitalized to COD, then paid subordinated to senior debt service and reserves). Equity is drawn pro rata with debt (25:75), with each sponsor's undrawn commitment backed by letters of credit from banks rated A- or better; Talmé's LC is issued by UBK and confirmed by Kaito Pacific Bank. Sponsors also commit USD 15.4 million of contingent equity, drawn 25:75 alongside the standby facility after contingency is exhausted. The sponsors' bid target was a USD nominal post-tax equity IRR of 16.0% on the base case.

## 1.6 The lenders and the financing at close

Financial close: July 17, 2018. Castellan Bank was mandated lead arranger on June 19, 2017.

### Debt sizing targets

| Parameter | Value |
|---|---|
| Base-case minimum DSCR | 1.35x |
| Downside minimum DSCR | 1.20x (availability 6.5 points below profile every year, heat rate +1.5%, fixed opex +10%) |
| Maximum gearing | 75% of total funding requirement |
| Minimum LLCR at close | 1.40x |
| Repayment | Sculpted to base-case CFADS / 1.35x; 26 semiannual installments from December 31, 2021 to June 30, 2034; all tranches pro rata on the common profile |
| ECA constraints to test | Repayment term from COD of 14 years or less; weighted average life of repayment 7.25 years or less; no installment above 25% of principal; first repayment within 24 months of COD, with at least 2% of principal repaid by then (Annex P 3.6, P-C23; round 1 alignment) |
| Expected outcome | Senior debt USD 600 million to USD 660 million; gearing cap binding or within 3% of binding |

### Tranches

| Tranche | Share of senior debt | Lenders | Pricing and fees |
|---|---|---|---|
| ECA-covered tranche | 30% (capped at USD 224.1 million, 85% of eligible export value) | Castellan Bank (ECA agent), Kaito Pacific Bank, Banque Raveau; 95% comprehensive cover from Exportgarant | Margin 1.35%; ECA premium 10.85% of principal, paid upfront pro rata to drawdowns and financed; arrangement fee 1.10%; commitment fee 0.45% a year |
| ABDB A-loan | 22% | Atlantic Basin Development Bank | Margin 3.65%; front-end fee 1.25%; commitment fee 0.75% |
| ABDB B-loan | 10% | ABDB as lender of record; participants Kaito Pacific Bank (55%) and Sterrenberg Bank NV (45%) | Margin 3.40%; upfront fee 1.50%; commitment fee 0.85% |
| Commercial tranche (uncovered, with private PRI) | 38% | Castellan Bank 34% (mandated lead arranger, bookrunner, modeling bank, hedge coordinator), Banque Raveau 26% (documentation bank), Kaito Pacific Bank 22% (technical bank), Hovland Bank ASA 18% (insurance bank) | Margin 4.10% to December 2025, 4.60% 2026 to 2029, 5.10% from 2030; upfront fee 2.15%; commitment fee 40% of margin; soft mini-perm: from January 2027 50% of distributable cash sweeps this tranche |
| Standby facility | USD 46.0 million committed | Commercial banks 60%, ABDB 40% | Tranche margin plus 0.25%; commitment fee 0.60%; drawn after contingency, 75:25 with contingent equity |

All loans are USD, floating on 6M USD LIBOR until December 31, 2022, and on 6M Term SOFR plus the ISDA 6-month spread adjustment of 0.42826% from January 1, 2023 (the LIBOR switch amendment was agreed in November 2022). Interest periods are six months; default interest is 2.00%. Commercial-tranche interest bears 10% Kessaran withholding tax grossed up by the project company; the ABDB loans, the ECA-covered tranche and the 2025 bond are exempt.

Agency roles: Castellan Bank is intercreditor agent and offshore security agent; UBK is onshore security agent and onshore account bank; Castellan Bank London is offshore account bank.

### Covenants and reserves

Historic DSCR (12 months to each June 30 and December 31 test date, cash basis): lock-up below 1.20x, event of default below 1.10x. Projected DSCR lock-up 1.20x; LLCR lock-up 1.25x. Distribution conditions: no default, DSRA and MMRA fully funded, historic and projected DSCR at least 1.20x, first repayment made, completion certified by the independent engineer. Equity cure by shareholder loan permitted twice over the life, not in consecutive periods.

DSRA: six months of next debt service, fully funded at COD from the final drawdown; LC substitution allowed for sponsors with A- rated LCs. Major maintenance reserve account (MMRA): one sixth of the next out-of-LTSA overhaul accumulated in each of the six semiannual periods before it. Handback reserve from OY20.

### Hedging

Interest rate swap at 2.947% fixed (mid-market 2.872% plus 7.5 bps credit and execution charge), traded at financial close with the four commercial banks pro rata to their commercial-tranche shares, covering 80% of projected floating senior debt (permitted band 75% to 90%), accreting in construction and amortizing to June 30, 2034. The swaps move to compounded SOFR plus 0.42826% from the first reset after June 30, 2023 under the ISDA 2020 IBOR Fallbacks Protocol, to which all parties adhered. Between January and June 2023 the loans paid Term SOFR plus the spread while the swaps still received LIBOR; the model ignores that six-month basis and Chapter 6 discusses it.

Construction-period currency hedge (decision D-114; P-C45). The onshore EPC portion is fixed in KCR (KCR 42,939 million, the USD 82.67 million of Section 1.3 at 519.4 KCR per USD), so the common terms agreement's hedging policy requires the project company to hedge at least 75% of committed KCR construction payments. At financial close on July 17, 2018 the project company bought KCR forward against USD from Castellan Bank for 75% of each scheduled onshore EPC payment (KCR 32,204 million in all, one forward per monthly onshore EPC payment from August 2018; the ledger lists the profile and prints every sixth month; settlements are reported by half-year from 2018 H2 to 2021 H2; round 1 correction of "seven semiannual settlement dates", ledger wins), at covered-interest-parity forward rates (KCR policy rate 13.5% against the FC forward 6M LIBOR), cash-settled in USD and secured pari passu with the interest rate swaps. Notional profile, forward rates and USD equivalents: figure P-F65. The FC base budgets the onshore portion at the FC spot rate; in the actual run the forwards settle with a gain to the project (figure P-F66) because the forward points of about 10% a year exceeded the cauri's actual fall of about 5% a year, while the unhedged quarter of the onshore payments gained from the cauri's fall. The VAT facility is left unhedged because it is matched by the KCR VAT refunds. Accounting (round 1, u14): Bélanou Power designated the July 17, 2018 forwards as cash flow hedges of the highly probable forecast KCR EPC payments under IFRS 9. The effective part of each forward's gain or loss was held in the cash flow hedge reserve and removed from it when the hedged payment was recognized, as part of the cost of the construction asset (Chapter 66, sec:66.12, states the treatment and its source). No forward balance remained in the reserve after COD, so the hedge reserve recycled on the 2026 loss of control (P-F26) relates only to the interest rate swaps. After COD there is no FX hedge: the tariff is USD-indexed and paid in KCR at the prevailing rate, so the operating exposure is to convertibility, transfer delay, and SEKA's ability to pay, not to the exchange rate itself.

### Accounts

Onshore: KCR Collection Account and KCR Operating Account at UBK. Offshore at Castellan Bank London: USD Proceeds, Debt Service, DSRA, MMRA, Insurance Proceeds, Compensation, and Distribution Accounts. KCR collections are converted and swept offshore daily when the Central Bank makes FX available.

### Documentation and law

Common terms agreement, facility agreements, intercreditor agreement, accounts agreement and offshore security under English law; onshore security (share pledge, business pledge, receivables and account pledges, mortgage of the emphyteutic lease, assignment of insurances) under Kessaran law, held by the onshore security agent through a parallel debt undertaking in the intercreditor agreement because Kessaran law does not recognize a security trust. Direct agreements with SEKA, the Republic (under the IA), SNHK, GCK, the EPC contractor, Bergmark and the O&M operator. Disputes under the finance documents: LCIA arbitration seated in London, with the lenders' option to sue in the English courts.

## 1.7 Tax

| Item | Rule |
|---|---|
| Corporate income tax | 30% |
| Tax holiday (Investment Code) | 0% for OY1 to OY5; 15% for OY6 to OY8; 30% from OY9 |
| Minimum turnover tax | 0.5% of non-fuel revenue from OY6 |
| Depreciation | Straight line from COD: plant 92% of capitalized cost over 20 years; buildings and civil works 5% over 25 years; development and financing intangibles 3% over 5 years. Capitalized cost includes IDC, fees, ECA premium and development fee; excludes DSRA funding and working capital |
| Deferred depreciation during holiday | Depreciation of holiday years is deemed deferred and deductible later without time limit |
| Losses | Carried forward five years |
| Shareholder loan interest | Deductible; thin capitalization 3:1 related-party debt to equity |
| Interest limitation | 30% of tax EBITDA from January 1, 2025; loans signed before January 1, 2023 grandfathered, including refinancing that does not increase principal |
| Withholding tax | Dividends 15% domestic, 7.5% treaty; interest 10% domestic, 5% treaty on shareholder loans; exemptions listed in Section 1.6 |
| Indirect transfer tax | 15% of the seller's gain from January 1, 2025 |
| VAT | 18%; plant imports exempt |

## 1.8 Master timeline

| Date | Event |
|---|---|
| 2015-03 | Emergency Power Plan announced |
| 2015-04-14 | Tomasz Wierzbicki meets Mariama Talmé in Dabakro; origination |
| 2015-06-22 | Kilnworth and Groupe Talmé sign co-development agreement (70:30) |
| 2016-02-09 | PPP Unit issues RFQ for a 450 MW to 650 MW gas IPP at Bélanou; 9 respondents |
| 2016-04-28 | 5 consortia prequalified |
| 2016-05-16 | RFP issued |
| 2016-09-27 | 4 bids received; evaluation on levelized tariff (25 years, 10.0% USD discount rate, 70% dispatch, reference gas price USD 5.50/MMBtu) |
| 2016-11-30 | Bid base date for indexation (KCR 462.35 per USD) |
| 2016-12-08 | Kilnworth-Talmé named preferred bidder; runner-up's levelized tariff 4.6% higher |
| 2017-04-11 | ABDB fund equity term sheet; ABDB lending mandate |
| 2017-06-19 | Castellan Bank mandated lead arranger |
| 2017-10-12 | PPA, IA and Government Guarantee signed |
| 2017-11-30 | GSA and GTA signed |
| 2017-12-19 | EPC contract signed |
| 2018-02-05 | LNTP (USD 14.20 million, sponsor funded) |
| 2018-03-27 | LTSA signed |
| 2018-04-30 | O&M agreement signed |
| 2018-07-17 | Financial close; interest rate swaps and KCR forwards traded |
| 2018-08-01 | Notice to proceed (Month 1) |
| 2019-11 | Steam turbine foundation concrete fails strength tests; demolition and re-pour (contractor delay) |
| 2020-03-21 | Kessaran COVID-19 lockdown; EPC force majeure notice |
| 2020-09 | COVID variation order agreed (USD 9.40 million); EOT of 97 days |
| 2021-03 | First gas for commissioning |
| 2021-06-09 | GT2 generator step-up transformer fails during backfeed; cause traced to a switching error at SEKA's Bélanou substation |
| 2021-11-30 | Taking-over; completion tests passed (581.9 MW; 6,286 kJ/kWh) |
| 2021-12-01 | COD (base case had May 1, 2021) |
| 2022-02 | Expert determination confirms grid event as a SEKA risk event; RCOD extension of 173 days |
| 2022-06-30 | First repayment; performance LDs of USD 18.485 million prepay senior debt |
| 2022 H1 | Dollar strengthens, cauri weakens; SEKA arrears begin |
| 2022-11 | LIBOR switch amendment signed (effective January 1, 2023) |
| 2022-11-07 | Central Bank FX allocation queue begins |
| 2023-02-14 | SEKA LC drawn (USD 36.6 million, the January 1, 2023 reset value; P-F39, P-F40); not replenished |
| 2023-04-18 | First Government Guarantee demand |
| 2023-06-29 | Tripartite gas netting agreement |
| 2023-06-30 | Historic DSCR below 1.10x; event of default; DSRA drawn |
| 2023-10-26 | Waiver and amendment letter |
| 2024-03-21 | Arrears settlement agreement |
| 2024-03-29 | FX queue ends |
| 2024-11 | Sovereign upgraded to B- |
| 2025-06-17 | Bond priced |
| 2025-06-30 | Refinancing settles: commercial tranche, B-loan and standby facility prepaid |
| 2026-04-14 | Kilnworth signs sale of 24% to Coldharbour |
| 2026-09-30 | Sale completes |
| 2046-11-30 | PPA expiry and transfer to SEKA |

## 1.9 Events and their assumptions

### Construction delay and cost overrun (2019 to 2021)

Three delays hit the critical path, in sequence:

| Delay | Days | Cause | Contractual treatment |
|---|---|---|---|
| COVID-19 | 97 | Lockdowns in Kessara and the contractor's home country; travel bans for commissioning engineers | Force majeure under EPC and PPA: extension of time, no LDs; variation order of USD 9.40 million for COVID measures (camp isolation, charter flights, testing) paid by the project company |
| Civil rework | 41 | Steam turbine foundation concrete poured by Bati-Kessara failed 28-day strength tests; demolition and re-pour | Contractor risk: delay LDs |
| Grid event | 76 | GT2 step-up transformer destroyed by a switching surge from SEKA's substation during backfeed on June 9, 2021; replacement shipped from the manufacturer's spare pool | Employer risk under the EPC (grid interface): extension of time and prolongation costs; SEKA risk event under the PPA (RCOD extension, confirmed by expert determination in February 2022); EAR covers material damage; DSU covers lost revenue after the deductible |

Total delay: 214 days. The extended EPC guaranteed completion date was October 20, 2021 (April 30 plus 173 days); taking-over on November 30, 2021 was 41 days late, so delay LDs are 41 times USD 247,300, or USD 10.1393 million. The RCOD moved from July 31, 2021 to January 20, 2022, so no PPA delay LDs were payable. Insurers declined to pursue a subrogated claim against SEKA after the Ministry of Energy intervened; Annex P 2.8 gives the facts and Chapter 61 tells the story (round 1).

Insurance claim: EAR material damage loss USD 6.84 million less the USD 1.0 million deductible, so USD 5.84 million paid through the Insurance Proceeds Account to the EPC contractor for reinstatement; the deductible is borne by the project company. DSU: 76 days less the 45-day deductible equals 31 indemnified days at USD 228,400, or USD 7.0804 million.

Hard cost overrun (USD m):

| Item | Amount |
|---|---|
| COVID variation order | 9.40 |
| Grid-event prolongation settlement (claimed 11.60) | 8.27 |
| Extended owner's costs (7 months) | 6.93 |
| Project company COVID measures | 4.11 |
| Additional resettlement compensation after grievance review | 3.27 |
| Customs duty settlement on spare parts | 2.64 |
| Insurance extension premium | 1.42 |
| Additional start-up fuel, net | 1.37 |
| EAR deductible | 1.00 |
| Additional lenders' advisor costs | 0.86 |
| Total | 39.27 |

The model adds the extra IDC and commitment fees from the seven-month delay and the DSRA re-sizing. The funding order is: unused contingency (USD 38.40 million), EPC delay LDs, DSU proceeds, then the standby facility and contingent equity 75:25 for any remainder (figure P-F18). Ledger v1.2 adds the modeler's calibration of delay-related EPC acceleration and owner cost escalation in Months 34 to 40 (P-C43) and the KCR forward settlements (P-F66), and both the standby facility and the contingent equity are drawn: writers print the drawn amounts only from P-F18, and Chapters 31, 32 and 61 say they were drawn.

### Completion tests and performance LDs (November 2021)

Corrected net output 581.9 MW (6.5 MW short): output LDs USD 13.975 million. Corrected heat rate 6,286 kJ/kWh (25 kJ/kWh over): heat-rate LDs USD 4.510 million. Total performance LDs USD 18.485 million, applied 100% to mandatory prepayment of senior debt pro rata on June 30, 2022. Contracted capacity resets to 581.9 MW.

### LIBOR transition (2021 to 2023)

Loans: LIBOR switch amendment signed November 2022, effective January 1, 2023: 6M Term SOFR plus 0.42826% plus the unchanged margin. Swaps: ISDA fallbacks from the first reset after June 30, 2023. The PPA's late payment interest switched by SEKA's consent to Term SOFR plus 2.00%.

### Offtaker payment crisis and currency shock (2022 to 2025)

SEKA's retail tariff was frozen after street protests in October 2022 while its KCR cost of USD-indexed IPP and gas purchases rose with the cauri's fall. SEKA paid late, then partially.

| Date | Overdue receivables beyond normal 45 days (USD m, net of LC drawing) |
|---|---|
| 2021-12-31 | 0.0 |
| 2022-06-30 | 18.4 |
| 2022-12-31 | 68.9 |
| 2023-06-30 | 112.6 |
| 2023-12-31 | 71.8 |
| 2024-06-30 | 34.6 |
| 2024-12-31 | 12.3 |
| 2025-06-30 | 0.0 |

Further assumptions: Central Bank FX queue from November 7, 2022 to March 29, 2024 with an average conversion lag of 47 days; FX losses on trapped cauris of USD 1.27 million (H2 2022), USD 3.84 million (H1 2023), USD 1.12 million (H2 2023) and USD 0.31 million (H1 2024); LC drawn for USD 36.6 million on February 14, 2023 (the January 1, 2023 reset value; P-F39, P-F40; P-C44) and never replenished; Government Guarantee demands of USD 21.6 million (April 18, 2023, paid July 26, 2023), USD 18.9 million (July 12, 2023, paid November 30, 2023) and USD 17.4 million (October 9, 2023, unpaid and folded into the settlement); tripartite netting agreement of June 29, 2023 (up to USD 9.0 million a month of SEKA energy-charge arrears set off against the project company's gas payables to SNHK); settlement agreement of March 21, 2024 providing 15 monthly installments from April 2024 to June 2025 with 40% of late payment interest waived.

### Covenant breach and waiver (2023)

The historic DSCR at June 30, 2023 falls below the 1.10x default level (model figure P-F21: 0.96x at June 30, 2023 after 1.13x at December 31, 2022; these ledger values govern, and the 1.14x and 0.97x in `model/case-state-case-p.md` are superseded; round 1). The DSRA pays the June 30, 2023 shortfall. Waiver and amendment letter of October 26, 2023: tests at June 30 and December 31, 2023 waived; waiver fee 0.25% of outstanding senior debt; margin uplift 0.50% from July 1, 2023 to December 31, 2024; 60% of the December 31, 2023 principal installment deferred and repaid in four equal parts on June 30, 2024, December 31, 2024, June 30, 2025 and December 31, 2025; 100% of arrears recoveries applied to DSRA replenishment first; distributions locked up until two consecutive historic DSCR tests of at least 1.25x and a full DSRA.

### Refinancing (2025)

Settled June 30, 2025, an interest payment date, so no loan breakage. A USD senior secured amortizing project bond (144A/Reg S, listed), coupon 7.875% semiannual (30/360), issue price 99.512, final maturity June 30, 2037, rated B+ by one agency against a B- sovereign, with a USD 95.0 million ABDB partial credit guarantee (fee 1.10% a year, upfront fee 0.75%). Bond proceeds prepay the commercial tranche, the B-loan and the standby facility; the ECA-covered tranche and the A-loan stay in place and consent to the bond's maturity beyond 2034. Bond amount equals the prepaid principal after the June 30, 2025 scheduled payment plus transaction costs (underwriting 1.00% of the bond, other costs USD 3.10 million) less the swap unwind receipt; no upsizing, so the interest limitation grandfathering survives. The swaps attributable to the prepaid tranches are terminated at market (flat swap rate 3.68% for the remaining profile; the project company receives the value because 2.947% is below market). The bond amortizes on a profile sculpted together with the remaining ECA and A-loan debt service so that the combined DSCR is level. Because the bond amount is fixed by the prepaid principal (no upsizing), not by a DSCR target, the level combined DSCR is a model output: 1.59x on the post-refinancing case (P-F23). The 1.35x of Version 1.0 was the design floor, not the outcome; writers print only the ledger value (round 1; P-C51).

### Partial sale (2026)

Kilnworth sells 24% of the project company (40% of its 60% holding) in shares and shareholder loans pro rata to Coldharbour Infrastructure Income Fund. Share purchase agreement signed April 14, 2026 (never abbreviated; SPA means the commodity contract, R-084); locked-box date December 31, 2025 with a 6.50% a year ticker; completion September 30, 2026. Buyer's discount rate 13.75% (USD, post-tax, levered); Kilnworth's reserve discount rate 12.50%; price = 24% of equity value at the agreed rate (model, P-F24). Deferred consideration of USD 4.0 million if SEKA's overdue receivables stay at zero through June 30, 2027; the model measures it at nil at completion, so P-F26's consideration line (the cash price) excludes it, and Chapter 66 says so (round 1; P-C56). W&I insurance limit USD 18.0 million. Consents: lenders and bondholders (Kilnworth must keep at least 30% until 2030), SEKA, MEH under the IA, and right-of-first-refusal waivers by Groupe Talmé and the ABDB fund. Kilnworth pays the 15% indirect transfer tax on its gain. After completion Kilnworth holds 36% and stops consolidating the project company (Chapter 66).

## 1.10 Case P scenarios

| Scenario | Definition |
|---|---|
| FC base | Financial close base case: COD May 1, 2021; 588.4 MW; base availability and dispatch; FC forward LIBOR curve; FX projected from 2018 by inflation differential using 2018 expectations (Kessaran CPI 7.5%, US CPI 2.2%) |
| FC banking | FC base with 72.0% dispatch |
| FC downside | Availability 6.5 points lower every year, heat rate +1.5%, fixed opex +10% |
| Actual history | Every event in Section 1.9 and the KCR forward settlements of Section 1.6, with historical macro paths to H1 2026, assumptions after |
| Sensitivities | Availability -3 points; heat rate +2%; fixed opex +10%; capex +10% funded pro rata; COD delay of six months without LDs; base rate +200 bps on the unhedged portion; 40% devaluation with 90-day conversion lag; SEKA payment delay of 120 days for 12 months; dispatch 50%; gas price +30% (pass-through check) |
| Breakevens | Availability for 1.00x minimum DSCR; capacity charge cut for 1.00x; months of zero SEKA payment covered by DSRA plus LC |

---

# Part 2. Case T: the Merrick Link toll road, State of Brannock, Commonwealth of Ardmore

## 2.1 The jurisdiction

The Commonwealth of Ardmore is a fictional federal parliamentary democracy and OECD member with a common-law legal system, six states, a population of about 31 million, and its own floating currency, the Ardmore dollar (code ARD, never printed with a symbol). Its PPP practice resembles that of the common-law federations that pioneered state-level PPP programs: each state runs its own PPP unit, publishes value-for-money guidelines and a public sector comparator methodology, and procures through expressions of interest, a shortlist, a request for proposals, and best and final offers. The federal government lends to state-sponsored infrastructure through a federal credit program.

The State of Brannock is Ardmore's third-largest state (5.4 million people in 2012), with its capital and main port at Port Ellery. Its growth area, the Coldwater Plains north of Port Ellery, doubled in population between 1996 and 2011 and is served by a single free road, State Route 14, which runs 47.6 km through four signalized town centers to the inland freight terminal at Holloway Junction.

Neither "Ardmore" as a country nor "Brannock" as a state exists (checked October 3, 2026; Ardmore is the name of small towns in the US and Ireland, which the book never mentions; see D-103). Writers name the country rarely ("the Commonwealth") and the state often.

| Institution | Role in Case T |
|---|---|
| Brannock Cabinet | Approves the business case (March 2012) and the decision to procure as a PPP (December 2012) |
| Brannock Treasury | Owns the PPP policy and the state budget; Deputy Secretary Owen Reddaway leads the state's side of the 2022 to 2023 restructuring |
| Partnerships Brannock | The state's PPP unit inside Treasury; procuring agency; Director Margaret (Maggie) Dunleavy |
| Brannock Roads and Transport Authority (BRTA) | Contracting authority; signs the Concession Deed; manages the contract |
| Brannock Infrastructure Finance Authority (BIFA) | State conduit issuer of the tax-exempt revenue bonds |
| National Infrastructure Lending Office (NILO) | Federal agency running the Commonwealth Infrastructure Credit Program, which lends subordinated, long-tenor, fixed-rate loans to qualifying projects |
| Supreme Court of Brannock | Sanctions the 2023 restructuring plan under Part 9 of the Companies Act (Ardmore), which allows cross-class cram-down |

ARD macro paths (CPI 1.4% to 7.1%, the 6-month Ardmore Bank Bill Rate (ABBR) from 0.06% to 4.41%) are in `inputs_case_t.json`. Illustrative USD per ARD rates for cross-case comparisons: 0.81 (2012), 0.76 (2015), 0.70 (2019), 0.67 (2023), 0.66 (2025).

## 2.2 The road

The Merrick Link is a 41.3 km four-lane (2+2) tolled motorway, with structures sized for 3+3, from the Port Ellery northern ring road through the Coldwater Plains to Holloway Junction. It has seven interchanges, the 620 m Merrick River viaduct, and the 1.9 km twin-bore Merrick Ridge Tunnel. Tolling is free-flow, electronic and distance-based (transponder and video). The road is delivered as a design, build, finance, operate and maintain (DBFOM) concession with full demand risk on the concessionaire.

| Item | Value |
|---|---|
| Concession term | 38 years from financial close: May 27, 2015 to May 26, 2053 (extended in 2023 to May 26, 2059) |
| Construction period | 46 months; scheduled opening March 31, 2019; actual opening May 6, 2019 (36 days late) |
| Car toll | ARD 0.1525 per km in June 2014 prices |
| Class multipliers | Car 1.0; light commercial 1.6; heavy vehicle 2.85 (2.40 from January 1, 2024) |
| Vehicle mix | 79.4% cars, 9.0% light commercial, 11.6% heavy vehicles (77.6%, 8.6%, 13.8% from 2024) |
| Average trip length | 23.8 km |
| Toll escalation | Each July 1 by the greater of CPI and 3.0% until June 30, 2030, then CPI; CPI only from July 1, 2024 after the restructuring |
| Toll regime | Concession sets maximum tolls; the concessionaire may discount |
| Revenue leakage | 1.8% of gross toll revenue |
| State land | Provided by the state (ARD 212.5 million, outside the concession) |

## 2.3 Procurement and the public-sector case

Partnerships Brannock built the business case and public sector comparator (PSC) in 2012 at a nominal discount rate of 6.85%. The PSC, in ARD millions of 2012 present value: raw capital cost 1,478.6; O&M and lifecycle 486.2; toll revenue retained by the state (1,821.4); construction risk 115.3; traffic revenue risk 87.4; operating risk 18.5; competitive neutrality 19.6 (recalibrated before publication, change log T-C05). Value for money is reported as a share of the risk-adjusted PSC. The PPP reference project assumed a state construction contribution of ARD 410.0 million paid at opening, retained risks of 52.8 and contract management of 21.6. The model computes PSC and PPP present costs and value for money (figure T-F01). Land (ARD 212.5 million) is common to both and excluded.

| Date | Step |
|---|---|
| 2012-03-20 | Cabinet approves business case development |
| 2012-11-08 | Business case and PSC completed |
| 2012-12-04 | Cabinet decides to procure as a user-pay DBFOM PPP |
| 2013-02-18 | Expressions of interest and RFQ issued |
| 2013-06-10 | Three consortia shortlisted: Merrick Motorway Partners, Northgate Mobility Consortium, and a third consortium that withdrew in January 2014 |
| 2013-09-02 | RFP issued; bid variable is the state construction contribution, with maximum tolls fixed by the state |
| 2014-03-27 | Two bids received |
| 2014-07-01 | BAFO requested |
| 2014-08-15 | BAFOs received; Merrick Motorway Partners asks for ARD 287.4 million, Northgate for ARD 361.0 million |
| 2014-09-23 | Merrick Motorway Partners named preferred bidder |
| 2015-05-27 | Concession Deed signed and financial close (delayed from December 2014 by NILO credit approval) |

The winning contribution, ARD 287.4 million against a reference of ARD 410.0 million, rested on the sponsor's traffic forecast (Pellow). Chapter 47 uses it to teach the winner's curse.

## 2.4 Parties

| Party | Role |
|---|---|
| Merrick Link Concession Co Ltd | Project company (concessionaire) |
| Merrick Motorway Partners | Winning consortium: Holbrook Infrastructure 40% (construction-led sponsor), Wexcombe Infrastructure Fund III 35% (financial investor), Corvus Toll Roads 25% (toll road operator) |
| Holbrook-Daneshill Joint Venture | Design and construction (D&C) contractor: Holbrook Civil 60%, Daneshill Construction 40%, joint and several, with parent guarantees |
| Corvus Road Services | O&M operator and tolling back office (Corvus Toll Roads affiliate) |
| Pellow Transport Economics | Sponsor's traffic advisor (Sasha Hrytsenko) |
| Ridgeway Traffic Consultants | Lenders' traffic advisor: the 2014 banking case, the traffic counts behind the lenders' monitoring reports from 2019, and the 2023 restructuring case (director Elspeth Varga, Annex TR T.19; round 1) |
| Calder Hartmann Engineering | Lenders' independent engineer and, from opening, lenders' technical and traffic monitoring adviser (cross-case firm; the Case T team is led by Rhys Tanaka-Bell of the Port Ellery office, not Gwen Treharne; Annex TR T.18) |
| Galbraith Stowe | Lenders' counsel to the bank club, the BIFA bondholders' representative and NILO on the intercreditor terms (partner Lachlan Mereweather; Annex TR T.18) |
| Dunmore Pryor | Counsel to Merrick Motorway Partners and the concessionaire from the bid to the 2023 plan (partner Anjali Thevarajah; Annex TR T.18) |
| Independent certifier | Appointed jointly by BRTA and the concessionaire |
| Castellan Bank, Penhallow Bank, Kaito Pacific Bank, Sterrenberg Bank NV | Bank club: senior mini-perm and contribution bridge |
| BIFA bondholders | Ardmore insurers and funds holding the tax-exempt revenue bonds |
| NILO | Subordinated federal loan |
| Quarrington Advisory | Restructuring adviser to the senior lenders from January 2022 (Pieter van Wijngaarden) |

## 2.5 Costs and financing at close

| Use of funds (ARD m) | Amount |
|---|---|
| D&C contract price (lump sum, including tolling system 48.6) | 1,684.3 |
| Development and bid costs reimbursed | 41.2 |
| Project company costs during construction | 37.8 |
| Insurance during construction | 12.6 |
| Independent certifier (concessionaire's share) | 3.4 |
| Lenders' advisors and legal | 9.7 |
| Contingency | 52.4 |
| Subtotal before financing costs | 1,841.4 |
| IDC, fees, DSRA, bond escrow negative carry | Model (T-F03) |

D&C terms: delay LDs ARD 285,000 per day capped at 20% of price; performance security 10%; retention 5% (half released at completion, half after a 24-month defects period). The actual 36-day delay produced LDs of ARD 10.26 million.

The state pays its ARD 287.4 million construction contribution at opening. A Contribution Bridge Facility of the same amount from the bank club (margin 1.60%, fee 1.00%) funds it during the last six construction quarters and is repaid from the contribution.

Sizing rules and instruments:

| Instrument | Terms |
|---|---|
| Equity | 22.0% of the funding requirement net of the state contribution (minimum 20%); 15% share capital, 85% shareholder loans at 10.25%; contributed first (equity first, in contrast to Case P's pro rata funding); bid target equity IRR 11.4% nominal post-tax |
| Senior debt (bank plus bonds) | Lesser of the DSCR-sculpted amount at 1.50x on the banking case (Ridgeway), LLCR 1.55x, and 55% of the funding requirement net of the contribution; downside minimum DSCR 1.15x; first repayment June 30, 2021; final repayment December 31, 2048; split 45% bank, 55% bonds |
| Bank mini-perm | Castellan, Penhallow, Kaito Pacific, Sterrenberg; maturity May 27, 2022; margin 2.35% to May 2020 then 2.60%; upfront fee 1.85%; commitment fee 0.95%; base case assumes refinancing at maturity at ABBR + 2.25% with 1.25% fees on the same profile; swapped 100% at 3.48% to June 30, 2035 |
| Brannock Infrastructure Revenue Bonds, Series 2015 | Issued by BIFA and on-lent; coupon 4.85% fixed; fully funded at close, proceeds in escrow earning 2.10% until used; amortizing June 2021 to December 2048 pro rata with the bank profile; interest tax-exempt for holders under the Commonwealth's Qualified Infrastructure Bond regime; issue costs 1.20%; par call from May 27, 2025 |
| NILO loan | 3.06% fixed (Commonwealth 30-year yield plus 0.01%); amount = remainder after senior and equity, checked against 33% of eligible costs and a combined senior plus NILO minimum DSCR of 1.25x on the banking case; drawn pro rata with senior after equity; interest capitalized to March 31, 2024; sculpted repayment June 2024 to December 2052; subordinated in payment with a springing lien that becomes pari passu on bankruptcy or insolvency; application fee 0.10% |
| Covenants | Senior lock-up 1.20x, default 1.05x; DSRA six months of senior debt service; lifecycle reserve accumulated over six periods ahead of each item |
| Expected outcome | Senior about 55%, NILO 22% to 25%, equity 22% of the funding requirement net of the contribution |

Operating costs (ARD millions, 2015 prices, Ardmore CPI): Corvus fixed O&M 11.84 a year; tolling back office 6.2% of toll revenue plus 2.15 a year; insurance 3.36; project company costs 2.71. Lifecycle: pavement resurfacing 42.6 in OY12, OY24 and OY36; tunnel mechanical and electrical 31.9 in OY15 and OY30; tolling and ITS replacement 14.7 every eight years from OY8; handback reserve over the final five years.

Tax: 30%; the concession asset is amortized straight line over the remaining term from opening; losses carry forward indefinitely subject to a continuity of ownership or same business test (passed in 2023); forgiven commercial debt reduces carried-forward losses first, then the asset's tax cost base; 10% withholding on interest to foreign lenders.

## 2.6 Traffic

Traffic is expressed as average daily vehicle trips (thousands). Revenue equals trips times days times 23.8 km times the car toll per km times the weighted class multiplier, less 1.8% leakage.

| Case | Mature level 2019 (k trips/day) | Ramp-up factors | Growth |
|---|---|---|---|
| Sponsor base (Pellow) | 58.4 | 2019 0.80; 2020 0.90; 2021 0.96; 2022 on 1.00 | 3.4% to 2030; 2.3% 2031 to 2040; 1.2% after |
| Banking (Ridgeway) | 52.6 | 2019 0.72; 2020 0.84; 2021 0.93; 2022 0.98; 2023 on 1.00 | 2.9%; 2.0%; 1.0% |
| Downside | 46.7 | 2019 0.65; 2020 0.78; 2021 0.88; 2022 0.95; 2023 on 1.00 | 2.2%; 1.6%; 0.8% |

Actual traffic (k trips/day):

| Period | Actual | Note |
|---|---|---|
| 2019 H1 (from May 6) | 28.1 | |
| 2019 H2 | 31.1 | 2019 average 30.4 against a base forecast of 46.7 (34.9% below) |
| 2020 H1 | 21.4 | April 2020 traffic 62% below February 2020 |
| 2020 H2 | 30.0 | |
| 2021 H1 | 31.8 | Second lockdown; working from home persists |
| 2021 H2 | 36.0 | |
| 2022 H1 | 39.1 | |
| 2022 H2 | 41.3 | 2022 average 40.2 against base 64.6 (37.7% below) |
| 2023 H1 | 41.9 | |
| 2023 H2 | 43.3 | |
| 2024 H1 | 43.9 | Heavy-vehicle toll cut takes effect |
| 2024 H2 | 45.5 | |
| 2025 H1 | 45.8 | |
| 2025 H2 | 46.8 | |
| 2026 H1 | 47.1 | |

The causes, which Chapter 48 and Chapter 79 analyze: Pellow assumed Coldwater Plains housing completions that slipped by about four years; it used a value of time for cars 22% above what a later revealed-preference survey found; trucks avoided the road because the heavy-vehicle multiplier made the tolled route dearer than SR 14 for trips under 30 km; and BRTA's promised SR 14 traffic-calming works were deferred. Ridgeway's 2023 restructuring case starts from the 2023 actual of 42.6, adds a 2.4% uplift in total trips from 2024 (heavy vehicles move to 13.8% of the mix), and grows at 2.6% to 2030, 1.8% to 2040 and 0.9% after.

## 2.7 Termination compensation regime

| Ground | Compensation |
|---|---|
| Authority default or voluntary termination | Senior debt including breakage plus NILO outstanding plus equity compensation equal to the NPV of base-case distributions at the base-case equity IRR of 11.4% |
| Concessionaire default | Retendering procedure: the adjusted highest compliant tender price less retendering costs; if there is no liquid market, an estimated fair value; no floor at senior debt |
| Relief events (including COVID-19) | Relief from termination and performance deductions; no compensation |
| Prolonged uninsurable force majeure (more than 270 days) | Senior debt plus NILO plus equity contributed less distributions |
| Lender step-in | 90 days, extendable to 180, under the Financiers' Direct Deed |
| Refinancing gain | The state takes 50% of any refinancing gain (never triggered) |

Because concessionaire-default compensation has no debt floor, the senior lenders' alternative to restructuring in 2022 was a retender at a market value below their claims (figure T-F08). Chapter 64 builds the comparison.

## 2.8 Distress and restructuring (2019 to 2023)

| Date | Event |
|---|---|
| 2019-12-31 | First senior DSCR test; below the 1.20x lock-up (figure T-F07) |
| 2020-03-23 | COVID-19 restrictions; the concessionaire claims a Relief Event; BRTA accepts relief but refuses compensation |
| 2020-12-31 | Senior DSCR below 1.05x; event of default |
| 2021-03-26 | Standstill agreement: interest paid as cash allows, principal deferred, 100% cash sweep, no enforcement |
| 2021 | Sponsors lend ARD 45.0 million of support (22.5 in each half) as subordinated shareholder loans, then stop |
| 2022-01-17 | Senior lenders appoint Quarrington Advisory (Pieter van Wijngaarden) |
| 2022-05-20 | Amend and extend: bank maturity moved from May 27, 2022 to December 31, 2023; fee 0.50%; margin 3.25% |
| 2023-06-14 | Restructuring support agreement and term sheet signed by senior lenders, bondholders' representative, NILO and the state |
| 2023-11-30 | Court sanction hearing |
| 2023-12-18 | Restructuring effective (modeled at December 31, 2023) |

Restructuring terms:

| Element | Term |
|---|---|
| Senior claims | Bank and bond principal plus accrued unpaid interest at December 31, 2023; the bank swap terminated at market (swap rate 4.36% against the 3.48% fixed rate, so the value is in the concessionaire's favor) and set off |
| Write-down | 24.0% of senior claims: 14.0 points cancelled, 10.0 points converted into 85% of new equity |
| Restructured Senior Notes | 76.0% of claims; single class; 5.10% fixed; sculpted semiannual amortization June 30, 2024 to December 31, 2052 on the Ridgeway 2023 case, with 1.30x as the minimum DSCR the plan allows (a floor, not the outcome: because the notes are fixed at 76.0% of claims, the model's sculpting divisor is 2.65x and the minimum notes DSCR is 2.00x, T-F09 and T-F10; round 1, T-C25); 50% excess cash sweep to December 31, 2030 |
| NILO | No write-down; 1.00% PIK interest to December 31, 2030, then 3.06% cash; maturity December 31, 2058; ranking unchanged |
| State | ARD 120.0 million new money for 15% of new equity, used for the Holloway Junction interchange upgrade (78.3, 2024 to 2025) and a reserve top-up (41.7); concession extended six years to May 26, 2059; heavy-vehicle multiplier cut to 2.40 from January 1, 2024; toll escalation at CPI only from July 1, 2024; state takes 30% of annual toll revenue above ARD 260.0 million (2023 prices, CPI-indexed) |
| Original equity | Shares cancelled; shareholder loans including the 2021 support written off; Wexcombe and Corvus receive warrants over 3% of new equity, exercisable only after the senior notes are repaid in full; Holbrook receives nothing |
| O&M | Corvus contract retained with an 8% fee cut and new KPIs |
| Costs | ARD 21.6 million of restructuring costs (2022 to 2023) paid by the concessionaire |

The model computes claims, recoveries, the new note quantum, and post-restructuring projections (figures T-F09 and T-F10).

---

# Part 3. Case R: the Mesa Corta Renewables portfolio, ERCOT

## 3.1 Market choice

Case R sits in ERCOT, the real energy-only market covering most of Texas, with fictional assets, owners and counterparties and clearly illustrative prices (decision D-105). The reasons: ERCOT is the cleanest real example of an energy-only market with nodal pricing, hub settlement, scarcity pricing and no capacity market, so hub-to-node basis, capture prices, shape risk and battery merchant revenue all arise naturally; Winter Storm Uri (February 2021) is a real case the book teaches in Chapter 20, and a portfolio in the same market lets Chapter 20 run a Uri-type stress on Case R's own hedges; and real market rules can be verified, which a fictional market cannot. The cost is the risk that a reader takes the price paths as data. Every Case R price exhibit therefore carries the label "Illustrative" and the exhibit source line "Case Bible illustrative price paths; not ERCOT settlement data and not a forecast." The stylized 2022 to 2025 hub averages are of the same order as published hub averages (for example, ERCOT reported a 2023 real-time hub average of about USD 62.79/MWh and a 2024 average of about USD 28.84/MWh in its January 2025 market update); writers never present Case R's numbers as historical ERCOT data. US tax items (bonus depreciation, PTC, ITC, transferability) are law-dependent and dated; writers take them from the US tax-equity fact sheet.

## 3.2 The owner

Lattimer Infrastructure Partners is a fictional Houston and New York infrastructure manager. Its Lattimer Energy Transition Fund II (2021 vintage) has USD 2,380.0 million of commitments, a 1.40% management fee on commitments during the investment period, 15% carry over an 8% preferred return, and a 10-plus-2-year term. The fund owns 100% of Mesa Corta Renewables LLC, whose holding company (Mesa Corta HoldCo LLC) owns Mesa Corta OpCo LLC, which owns the asset companies. Asset management costs USD 3.2 million a year (2022 prices).

## 3.3 Assets

| ID | Asset | Technology | Capacity | COD | Hub | P50 NCF | P50 (GWh/yr) | P90 one-year | P90 ten-year | P99 one-year | Contract |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | Thatcher Flats Wind | 96 x 2.1 MW | 201.6 MW | 2014-12-15 | West | 39.4% | 695.8 | 87.6% | 92.9% | 77.5% | Merchant plus 40 MW fixed-volume swap 2023 to 2027 |
| R2 | Sandoval Hills Wind | 108 x 2.3 MW, coastal | 248.4 MW | 2017-06-30 | South | 36.1% | 785.5 | 89.2% | 94.1% | 80.4% | Physical as-generated PPA to June 2029 |
| R3 | Ollie Creek Wind | 51 x 3.0 MW, Panhandle | 153.0 MW | 2019-11-20 | West (Panhandle node) | 46.2% | 619.2 | 86.9% | 92.4% | 76.2% | Proxy revenue swap to December 2029; PTC tax equity |
| R4 | Peeler Draw Solar | Tracking PV, 131.3 MWdc | 98.7 MWac | 2020-10-09 | West | 27.1% | 234.3 | 94.6% | 96.8% | 90.2% | Fixed-shape hedge 2022 to 2026 |
| R5 | Calloway Mesa Solar | Tracking PV, 241.0 MWdc | 182.4 MWac | 2021-06-28 | West | 28.3% | 452.2 | 94.2% | 96.5% | 89.5% | Virtual PPA to June 2033; ITC tax equity |
| R6 | Redfern Storage | LFP, 2-hour | 100.0 MW / 200 MWh | 2023-07-14 | North | – | – | – | – | – | Toll to July 2030 |
| R7 | Kerrigan Storage | LFP, 2-hour | 150.0 MW / 300 MWh | 2024-04-02 | Houston | – | – | – | – | – | Merchant with revenue floor to April 2032 |
| R8 | Barlow Gap Solar | Tracking PV, 162.0 MWdc | 120.0 MWac | 2024-12-19 | South | 27.6% | 290.1 | 94.4% | 96.6% | 89.8% | Fixed-shape hedge on 60% of P50, 2025 to 2034 |

P90 and P99 columns are percentages of P50. Yield is modeled as normal: one-year variance is long-term uncertainty plus inter-annual variability, ten-year variance is long-term uncertainty plus one-tenth of inter-annual variability; the P90s are the anchors and the P99s follow from them (modeler calibration R-C09). Portfolio P-values use inter-asset correlations (R-C10; values in `model/inputs_case_r.json`, figures in R-F01). Totals: wind 603.0 MW, solar 401.1 MWac, storage 250.0 MW / 500 MWh. Degradation: wind 0.20% a year, solar 0.45% (R8 0.40%). Battery round-trip efficiency 86.0% (R6) and 86.5% (R7), availability 97.5%, augmentation of 6% of MWh in years 5 and 9 at USD 41/kWh (2025 prices). Useful lives end 2044 (R1), 2047 (R2), 2049 (R3), 2055 (R4), 2056 (R5), 2043 (R6), 2044 (R7) and 2059 (R8). Curtailment: West wind 4.5% in 2022 rising to 6.0% from 2025; Panhandle 5.2% rising to 7.0%; coastal wind 1.5%; West solar 2.0% rising to 3.5%; South solar 1.8%.

Tax equity: Castellan Bank's US tax-equity desk is the tax equity investor in R3 (PTC partnership flip: 99% of tax and 40% of cash to the investor until an expected flip on December 31, 2029, then 5%) and R5 (ITC partnership flip: 99% of tax and 20% of cash until an expected flip on June 30, 2027, then 5%). Mesa Corta owns the sponsor (class B) interests.

## 3.4 Hedge book

| Asset | Instrument | Counterparty | Key terms |
|---|---|---|---|
| R1 | Fixed-volume swap, 7x24 | Castellan Bank (commodities desk) | 40 MW at USD 48.25/MWh West Hub, January 2023 to December 2027 |
| R2 | Physical as-generated PPA | Orchard Power Retail LLC | USD 31.40/MWh flat, to June 30, 2029 |
| R3 | Proxy revenue swap | Galloway Risk Solutions | Galloway pays USD 25.84 million a year fixed; the project pays proxy revenue (proxy generation times West Hub price); 2020 to 2029; USD 12.0 million LC posted by the project |
| R4 | Fixed-shape solar hedge | Castellan Bank (commodities desk) | 168.4 GWh a year in solar shape at USD 44.10/MWh West Hub, 2022 to 2026 |
| R5 | Virtual PPA | Ostrander Data Systems Inc. | USD 27.85/MWh as generated, settled at West Hub, to June 30, 2033, with RECs |
| R6 | Battery toll | Orchard Power Retail LLC | USD 9.15/kW-month for 7 years from COD; 97.0% availability guarantee; owner augments to keep 200 MWh |
| R7 | Revenue floor (put) | Galloway Risk Solutions | Floor USD 74.00/kW-year for 8 years; premium USD 5.80/kW-year; Galloway takes 20% of revenue above USD 140/kW-year |
| R8 | Fixed-shape solar hedge | Castellan Bank (commodities desk) | 174.1 GWh a year (60% of P50) at USD 38.90/MWh South Hub, 2025 to 2034 |

Castellan's hedges are secured pari passu in the opco security package as first-lien hedges, with no cash collateral; Galloway's contracts are supported by LCs from the opco LC facility.

## 3.5 Illustrative prices

ERCOT North Hub around-the-clock annual average, USD/MWh nominal, illustrative:

| Year | Base | Low | High |
|---|---|---|---|
| 2022 (stylized history) | 74.6 | 74.6 | 74.6 |
| 2023 (stylized history) | 61.2 | 61.2 | 61.2 |
| 2024 (stylized history) | 30.1 | 30.1 | 30.1 |
| 2025 (stylized history) | 39.8 | 39.8 | 39.8 |
| 2026 | 44.6 | 35.2 | 56.3 |
| 2027 | 47.3 | 36.4 | 60.4 |
| 2028 | 49.1 | 37.3 | 63.2 |
| 2029 | 50.4 | 38.0 | 65.1 |
| 2030 | 51.8 | 38.6 | 66.9 |
| After 2030 | +2.0% a year | +1.0% a year | +2.8% a year |

Hub ratios to North Hub: West 0.968, South 0.991, Houston 1.012. Capture ratios to the asset's own hub (base case): West wind 0.74 in 2022 falling 0.6 points a year to a floor of 0.62; Panhandle wind 0.66 falling 0.5 points to 0.58 (node basis included); coastal wind 0.92 falling 0.3 points to 0.85; West solar 0.86 falling 2.0 points to 0.60; South solar 0.90 falling 1.8 points to 0.64. The low case declines 1.5 times as fast with floors 0.04 lower; the high case declines half as fast. Node capture for hedge settlement equals hub capture less basis of 0.04 (West wind), 0.07 (Panhandle), 0.03 (West solar), 0.02 (South solar) and 0.01 (coastal wind).

Battery merchant revenue (2-hour, energy arbitrage plus ancillary services, illustrative), USD/kW-year: 2023 142.5; 2024 61.8; 2025 52.4; 2026 base 57.9, low 39.0, high 84.5; then +1.5%, +0.5% and +2.5% a year.

## 3.6 Acquisitions

| Deal | Signed | Closed | Target | Seller | Price | Funding |
|---|---|---|---|---|---|---|
| A1 | 2021-12-09 | 2022-03-22 | Mesa Corta Renewables LLC (R1 to R5, sponsor interests) | Hollenbeck Energy North America | Enterprise value USD 446.3 million (calibrated, R-C04); transaction costs USD 14.9 million; buy-side W&I limit USD 118.0 million | New opco term loan, holdco term loan, fund equity |
| A2 | 2023-06-02 | 2023-08-31 | Redfern Storage LLC (R6), at COD | Tolliver Energy Development LLC | USD 63.7 million (calibrated, R-C05); costs USD 2.6 million; ITC claimed by seller | Redfern term loan and fund equity |
| A3 | 2024-02-15 | R7 2024-04-02; R8 2024-12-19 | Kerrigan Storage LLC (R7) and Barlow Gap Solar LLC (R8), late construction | Tolliver Energy Development LLC | R7 USD 87.4 million; R8 USD 101.9 million (calibrated, R-C06; 20% deposit at signing); costs USD 4.4 million; seller bears construction risk; long-stop June 30, 2025 | Holdco incremental loan, fund equity, ITC transfer proceeds |

The fund claims and sells the 30% ITC on R7 (92% eligible basis) and R8 (94% eligible basis) at USD 0.925 per USD 1 of credit; no energy community adder is assumed.

## 3.7 Debt

| Facility | Date | Terms |
|---|---|---|
| Mesa Corta OpCo term loan | 2022-03-22 | Castellan, Kaito Pacific, Sterrenberg, Penhallow (US branch); 7-year mini-perm to March 22, 2029; Term SOFR 3M + 1.625% to March 2026, then + 1.875%; upfront fee 1.50%; sized by revenue bucket at DSCR 1.30x contracted, 1.40x hedged, 2.00x merchant on P50, with P99 one-year DSCR at least 1.00x; notional amortization to 2040; sweep 50% in 2026 to 2027 and 100% from 2028; 85% hedged at 2.41% to 2029; DSRA six months by LC. Amount: model output (R-F05) |
| Mesa Corta HoldCo term loan B | 2022-03-22 | Institutional TLB arranged by Castellan; to March 22, 2028; SOFR (floor 0.50%) + 4.75%; OID 98.0; 1% a year amortization; 50% excess cash sweep; sized at distribution coverage 1.75x on P50 base and at most 45% of opco equity value. Amount: model output (R-F05) |
| Redfern term loan | 2023-08-31 | Penhallow Bank (US branch); SOFR + 2.10%; fee 1.40%; fully amortizing to June 30, 2030 on toll cash flow at 1.35x; 75% hedged at 4.38% |
| HoldCo incremental term loan | 2024-02-15 | SOFR + 4.25%; OID 99.0; maturity March 22, 2028; sized at 1.75x on incremental P50 distributions from R7 and R8 |
| Refinancing: Mesa Corta Senior Secured Notes (US private placement) | Priced 2025-10-21, funded 2025-12-16 (modeled December 31, 2025) | Issuer Mesa Corta OpCo; rated BBB- by one agency; Series A 7 years 5.71%, Series B 12 years 6.08%, Series C 18 years 6.39%, amortizing sequentially by tenor so that series sizes are outputs of the sculpted profile (R-C07; launch split of 30/40/30 superseded); sized at 1.35x contracted, 1.50x hedged, 2.25x merchant, P99 one-year at least 1.05x; make-whole at Treasuries + 50 bps; costs 1.10%; repays the opco term loan and the Redfern loan; opco swap unwound at 3.55% (receivable), Redfern swap at 3.55% (payable). Amount: model output (R-F08) |
| Refinancing: HoldCo repricing | 2025-12-16 | Margin 3.50%; maturity December 31, 2031; OID 99.5; sized at 1.75x on post-refinancing distributions |

SOFR (3M, annual average, approximate): 2022 2.04%; 2023 5.17%; 2024 5.16%; 2025 4.27%; 2026 3.66%; 2027 3.45%; 3.50% after.

## 3.8 Operating costs, tax and valuation

Opex (USD per kW-ac per year, 2022 prices, +2.5% a year, covering O&M, land, insurance, property tax and site costs): wind built before 2018 41.5; later wind 37.2; solar 18.4; storage 14.6. Wind land leases add 4.0% of revenue. Insurance steps up 22% in 2023. Decommissioning net of salvage (USD per kW, 2022): wind 62, solar 38, storage 21, secured by surety bonds costing 0.6% a year.

Tax: federal 21%; Texas margin tax at 0.75% of 70% of revenue; asset-purchase basis step-up allocated 85% to 5-year MACRS, 10% to 15-year property, 5% to land and other; bonus depreciation 100% (2022), 80% (2023), 60% (2024), 40% (2025 before January 20) and 100% (property acquired after January 19, 2025); NOLs indefinite, limited to 80% of taxable income.

Valuation (nominal, post-tax):

| Risk bucket | Unlevered discount rate | Levered equity discount rate |
|---|---|---|
| Contracted | 6.75% | 8.25% |
| Hedged | 7.75% | 9.50% |
| Merchant | 9.25% | 11.50% |
| Storage merchant | 10.25% | 12.50% |
| Terminal (after 2040) | 10.50% | – |

No terminal value beyond useful life; R1's repowering option is valued at zero in the base case. Fund target net IRR 11% to 13%. Valuation dates: March 22, 2022 (A1 bid), August 31, 2023 (A2), February 15, 2024 (A3), December 31, 2025 (refinancing and fund NAV).

Scenarios: base, low and high price and capture; P90 and P99 one-year volumes. Sensitivities: West solar capture -5 points; battery revenue low case; curtailment +3 points; opex +10%; SOFR +100 bps unhedged; and a Uri-type stress on R1's fixed-volume swap (72 hours at USD 5,000/MWh with the wind farm at 15% availability).

## 3.9 Case R timeline

| Date | Event |
|---|---|
| 2021-02 | Winter Storm Uri (real event, before Case R begins; Hollenbeck's R1 had no fixed-volume hedge then) |
| 2021-06 | Thandeka Mabuza joins Lattimer from the ABDB |
| 2021-12-09 | A1 signed after a competitive auction run by Hollenbeck's adviser (three final bidders) |
| 2022-03-22 | A1 closes; opco term loan and holdco TLB funded |
| 2022-10 | R1 fixed-volume swap traded for 2023 to 2027 |
| 2023-06-02 | A2 signed |
| 2023-08-31 | A2 closes; Redfern loan |
| 2024-02-15 | A3 signed; holdco incremental loan |
| 2024-04-02 | R7 COD and payment |
| 2024-12-19 | R8 COD and payment |
| 2025-10-21 | USPP priced |
| 2025-12-16 | Refinancing funded; holdco repriced; distribution to the fund |
| 2026-03 | Lattimer's investment committee reviews an offer from a data-center developer for a 15-year PPA from a repowered R1 (Chapter 88) |

---

# Part 4. Characters

Rules for writers. Characters come only from this list. Use a character's verbal habit at most once per chapter, and only in a scene where it carries information. No character explains a concept the reader needs; narration does that (style sheet 1.3). Characters are sometimes wrong, and each sheet says where. Ages are given as birth years so that every scene can compute them. Names were chosen to fit nationality and generation and to avoid the stock names in `standards.md` Section 8; none is meant to resemble a real person. Where a character works for an institution in Part 5, the institution is fictional.

## 4.1 Case P characters

### Tomasz Wierzbicki (developer lead)

Polish, born 1972 in Gdańsk. Kilnworth Power International: Vice President, Business Development West Africa (2014 to 2019); Managing Director, Africa (2019 to 2024); Head of Portfolio Management (from 2024). Mechanical engineer (Gdańsk University of Technology, 1996); gas turbine commissioning engineer for an OEM's field service arm in Poland and the Gulf (1996 to 2004); joined Kilnworth in 2004 as a project engineer; developed a 340 MW open-cycle plant in South Asia and a 120 MW HFO plant in East Africa before Bélanou.

He wants Bélanou to be the first flagship deal he leads from site to close, and to prove that an engineer can run a deal as well as a banker. He fears writing off a development budget (his first East African project had a tariff renegotiation that wiped out most of its equity value, and he was in the room) and being outmaneuvered on terms he does not fully understand. He negotiates by conceding small points fast to bank goodwill, then digging in on the items he understands physically: dispatch, heat rate, availability, LDs. He reads political signals poorly and trusts a signed contract more than he should. Verbal habit: converts every proposal into tariff terms, "What does that cost us per kilowatt-month?"

Where he is wrong: from October 2016 (risk register v1, Chapter 14) and again in 2017 he dismisses convertibility risk because "the tariff is in dollars" (Chapter 59 shows why that was the wrong frame; P-C20), and in 2016 he pushes the bid tariff lower than Kilnworth's pricing committee wanted. Arc: closes the deal (2018), survives the delay (he signs off the COVID variation without board approval and is reprimanded), manages the 2022 to 2023 crisis badly at first and well later, champions the 2025 bond, and in 2026 leads the partial sale he once said Kilnworth would never make.

### Mariama Talmé (local sponsor)

Kessaran, born 1977 in Dabakro. Deputy Chief Executive of Groupe Talmé (2008 to 2021), Chief Executive from 2021 when her father, the founder Ousmane Talmé (born 1946), retires to the chairmanship. MBA in Paris; six years in a Paris investment bank's Africa coverage team; returned in 2008 to run group finance.

She wants Groupe Talmé to graduate from a small diesel IPP to a serious infrastructure partner, with a board seat, reserved matters, and a share of the O&M jobs for Kessarans. She fears being treated as the partner who "handles the government," and being blamed in Dabakro if tariffs rise. She negotiates patiently, times her asks to political events she sees coming before the foreigners do, and trades economics for governance. Verbal habit: answers a proposal with "Who else has seen this?"

Where she is wrong: in 2017 she accepts a 25% stake without a tag-along right that would have let Talmé sell alongside Kilnworth, which costs her leverage in 2026. Arc: becomes the indispensable channel to ministers during the 2023 crisis and brokers the gas netting agreement with SNHK; in 2026 waives her right of first refusal over Kilnworth's stake in exchange for an additional board seat and a tag-along right.

### Pieter van Wijngaarden (lead arranger, later restructuring adviser)

Dutch, born 1966 in Rotterdam. Joined a Dutch bank in 1990; posted to Jakarta 1995 to 1999, where he worked on restructurings of dollar-tariff IPP loans after the 1997 crisis; London from 2000; Castellan Bank from 2008, Managing Director and Head of Project and Export Finance, EMEA (2014 to 2020). Leaves Castellan in late 2020 when its EMEA project finance team is cut after unrelated losses; Partner, Quarrington Advisory, from 2021.

At Castellan he wants a landmark mandate, the underwriting and hedging fees that come with it, and a clean record at credit committee. He fears underwriting a deal that will not sell down, and he never stops worrying about convertibility (Jakarta). He negotiates bluntly, anchors early, hides behind his credit committee, and trades price for structure. Verbal habit: "Fine. And the day it goes wrong?"

Where he is wrong: he insists on an 80% swap hedge with the swaps priced by his own bank, and the 7.5 bps execution charge becomes a sponsor grievance (this fight is staged once, in September 2017, Chapter 56); in 2016 he tells Tomasz that the banks will accept a final maturity in 2036, which they do not (the common profile ends on June 30, 2034). Arc: lead arranger of Case P (2017 to 2018); out of the bank in 2020; restructuring adviser to the Case T senior lenders (2022 to 2023), where he sits opposite sponsors as he once sat opposite borrowers; debt adviser to Kilnworth on the 2025 Case P bond, re-reading his own 2018 term sheet from the borrower's side.

### Adaeze Whitcombe (sponsor's counsel)

British-Nigerian, born 1971 in London. Partner, Pemberton Hale LLP (London), energy and infrastructure finance. Oxford law; trained at Pemberton Hale; seconded to a Lagos firm in 1999; partner in 2007; acts for Kilnworth on every Case P document from the PPA to the 2026 sale.

She wants documents that are bankable without giving away more than the lenders need, and she wants the termination regime exactly right because she has seen a Government Guarantee fail on a drafting point. She fears a gap that is later traced to her draft. She drafts overnight, concedes words rather than substance, and quotes lenders' counsel's own precedents back at them. Verbal habit: "Let's read the clause."

Where she is wrong: the PPA lets SEKA cure a failure to replenish the LC within 30 days by a "payment plan" approved by OREK, which delays the put option in 2023; she accepted the wording in a late-night trade for the 14.5% equity rate in the termination formula. Arc: wins the termination formula (2017), drafts the waiver request (2023), acts on the bond (2025) and the sale (2026).

### Laurent Bécherel (lenders' counsel)

French, born 1961 in Lyon. Partner, Ashworth Quayle LLP (Paris office), finance and security in francophone civil-law jurisdictions; avocat since 1988; joined Ashworth Quayle in 1999. Leads the lenders' legal team on Case P; his London colleagues handle the English-law documents.

He wants security that a Kessaran court will enforce. He fears a parallel debt clause challenged in a Kessaran insolvency, and an unregistered pledge. He negotiates formally and slowly, cites precedent, never moves on conditions precedent, and is flexible on anything he classifies as "commercial, not legal." Verbal habit: opens objections with "En droit kessarais" (in Kessaran law).

Where he is wrong: he advises in 2018 that the business pledge captures future receivables under the PPA without a separate notice to SEKA, and a Dabakro court registrar disagrees in 2023 (fixed by re-notification, Chapter 52). Arc: builds the onshore security package (2018), insists on a reservation of rights in the 2023 waiver, restructures the intercreditor arrangements to admit the bond trustee (2025).

### Abdoulaye Ndao-Sylla (host government official)

Kessaran, born 1958. Electrical engineer; 25 years at SEKA, rising to Director of Generation; Secretary-General of the Ministry of Energy and Hydrocarbons (2014 to 2021); Minister of Energy and Hydrocarbons (2021 to October 2023, removed in a cabinet reshuffle after the tariff protests).

He wants power on the grid before the 2019 elections, and a plant that is visibly Kessaran (local staff, training, a SEKA engineer seconded to the control room). He fears load-shedding, and being remembered for an expensive dollar tariff. He negotiates with deadlines and political support rather than money, delays signatures to extract concessions, and speaks of capacity as places. Verbal habit: translates megawatts into towns ("that is Dabakro's evening peak").

Where he is wrong: in 2016 he pushes for the shortest possible construction period in the RFP, and bidders price the risk. In 2022, as minister, he attacks the "dollar tariff" in parliament, which makes lenders and SEKA's suppliers more nervous, not less. Arc: champion of Bélanou (2015 to 2018); public critic (2022); quiet broker of the netting agreement (2023); leaves office.

### Clémentine Agbo-Lawson (PPP Unit head, later public debt director)

Kessaran, born 1979. Economics trained in Paris and Montreal; six years in an international consulting firm's public sector practice; returned in 2012 to set up the PPP Unit at the Ministry of Economy and Finance and headed it until 2020; Director-General of Public Debt at MEF from 2020.

At the PPP Unit she wants Kessara's first competitive IPP to be a clean, transparent model, and she wants the contingent liabilities counted. She fears a procurement challenge, a bypass by the Energy Ministry, and a guarantee call. She runs process strictly, writes everything down, and uses competition rather than relationships. Verbal habit: "Where is that written?"

Where she is wrong: she caps the Government Guarantee at USD 1,250 million but never budgets for a call, and in 2023 the Treasury has no line for it. Arc: designs and runs the 2016 tender; in 2023, as Director-General of Public Debt, she is the official who receives the guarantee demands, pays two late, and folds the third into the settlement she negotiates with Tomasz and Hyacinthe Dossa.

### Hyacinthe Dossa (utility CFO)

Kessaran, born 1964. Chartered accountant; audit practice in Dabakro; SEKA finance from 2001; Chief Financial Officer of SEKA from 2016 to 2024.

He wants SEKA to stay solvent, and he wants IPP payments not to crowd out his own maintenance budget. He fears a public payment default, personal liability as an officer, and losing his job when ministers look for someone to blame. He pleads poverty, delays, pays in part, and offers comfort letters instead of cash. Verbal habit: "Not in this cash calendar."

Where he is wrong: in 2017 he fights the LC size down from three months to the two-plus-one formula and then in 2023 cannot replenish even that. Arc: adversary in the PPA negotiation; designer, with SNHK, of the 2023 netting agreement; signatory of the 2024 settlement; leaves SEKA in 2024.

### Konrad Elsässer (EPC project director)

National of the EPC contractor's unnamed Western European home country, born 1960. Project Director, Lindauer Kraftwerksbau AG. Thirty years building combined-cycle plants in the Gulf, Southeast Asia and Latin America; Bélanou is his last project before retirement.

He wants to finish on time and keep his margin, and to avoid LDs. He fears ending his career in an arbitration. He negotiates through schedules, files claims early and often, and trades acceleration for money. Verbal habit: puts dates on everything ("that is the fourteenth of March, not a day later").

Where he is wrong: he blames the failed foundation concrete on the cement supplier rather than his civil partner Bati-Kessara, which delays the fix by three weeks. Arc: claims force majeure (2020), loses on the civil rework (41 days of LDs), wins the grid-event extension, settles prolongation at USD 8.27 million against USD 11.60 million claimed, hands over and retires in 2022.

### Gwen Treharne (independent engineer)

Welsh, born 1966. Partner, Calder Hartmann Engineering (Cardiff and London). Performance engineer at a UK CCGT operator for nine years; independent engineer for twenty.

She wants a report she can defend in ten years. She fears certifying something that later proves wrong, and her own liability cap. She does not negotiate; the craft is in how she words reservations. Verbal habit: puts odds on things ("I would put that at one in five").

Where she is wrong: her 2018 report puts the probability of a delay longer than six months at one in eight. Arc: writes the 2018 IE report (Chapter 48), certifies drawdowns, gathers the evidence that the transformer failure started at SEKA's substation, certifies completion with a reservation on HRSG tube supports, and in 2025 acts as lenders' independent engineer on Case R's refinancing.

### Thandeka Mabuza (DFI investment officer, later fund principal)

South African, born 1983 in Durban. Actuarial science (Cape Town); four years on a Johannesburg bank's project finance desk working on renewable IPP tenders; ABDB Investment Officer (2014 to 2018) and Principal (2018 to 2021) on the lending side; Principal at Lattimer Infrastructure Partners from June 2021, Director from 2024.

At the ABDB she wants additionality she can defend to her board, and an environmental and social record without a stain. She fears a resettlement grievance becoming a campaign. She uses DFI policy as leverage, ties E&S conditions to disbursements, and is quiet and persistent. Verbal habit: "What's the counterfactual?"

Where she is wrong: in 2017 she argues for a smaller PRG (USD 30 million); the Board raises it to USD 41.5 million, and in 2023 even that covers only about a third of the June 2023 peak arrears net of the LC drawing (less than 30% of the gross arrears; P-C16). Arc: drives the RAP, the ESAP and the PRG on Case P; moves to Lattimer in 2021; leads diligence on Case R's A2 and A3 and the 2025 refinancing.

### Henrike Vosskamp (ECA underwriter)

National of the EPC contractor's unnamed home country, born 1975. Senior Underwriter, Exportgarant. Economist; ministry of economics; Exportgarant since 2005.

She wants the content rules met, the environmental review clean, and a premium that matches the country risk. She fears country risk reclassification and public criticism of fossil fuel support. She negotiates only inside the OECD Arrangement and is slow. Verbal habit: cites Arrangement provisions by number, once.

Arc: classifies Bélanou as a Category A project under the OECD Common Approaches and approves cover (2018); must consent to the 2023 waiver and does so last; consents to the bond's maturity beyond 2034 (2025).

### Félix Adandé (gas seller)

Kessaran, born 1969. Commercial Director, SNHK. Wants a take-or-pay strong enough for Halbeck to finance Sombé West; fears Halbeck walking away. Appears in Chapters 25 and 59.

### Yusuf Demirci (buyer of the 2026 stake)

Turkish-British, born 1979. Partner, Coldharbour Infrastructure Income Fund. Former infrastructure banker. Wants a contracted dollar yield with an emerging-market premium; fears a second SEKA crisis. Appears in Chapter 63.

## 4.2 Case T characters

### Margaret (Maggie) Dunleavy (PPP unit director)

Ardmorean, born 1965 in Port Ellery. Civil engineer at the state roads agency (1987 to 2002); Treasury PPP team from 2002; Director, Partnerships Brannock (2011 to 2020); Commissioner of the independent Brannock Infrastructure Advisory Board from 2020.

She wants the Merrick Link built without the state carrying traffic risk, and a value-for-money case that survives audit. She fears a failed PPP becoming a political story, and accusations that she hid liabilities. She runs competitive tension hard, defends the standard form, and refuses to move on risk transfer. Verbal habit: "What does the standard form say?"

Where she is wrong: the PSC used the same traffic optimism as the bidders (it drew on Pellow's earlier corridor study), so the value-for-money margin was overstated, and she accepts a contribution far below the reference without testing the winning traffic case hard enough. Arc: designs the procurement, takes the low bid (2014), and in 2023 gives evidence to a parliamentary inquiry where she concedes the PSC point and defends the risk transfer, which worked as designed: lenders and equity, not the state, took the loss.

### Callum Petrie (bid team leader)

Scottish-born Ardmorean, born 1974 in Paisley; moved to Ardmore in 2003. Quantity surveyor and construction claims specialist in Glasgow; Holbrook from 2005; Bid Director for three PPPs (lost two); Head of Investments, Holbrook Infrastructure, from 2016.

He wants to win, because Holbrook's real prize is the D&C margin, and he wants Holbrook's equity as small as possible. He fears a third straight loss. He is aggressive and optimistic, presses his traffic advisor for upside, and uses deadlines. Verbal habit: "Close enough to win."

Where he is wrong: he selects Pellow's high value-of-time case for the BAFO. Arc: wins (2014); Holbrook earns its construction margin; Holbrook's equity is wiped out in 2023, and Callum's last scene is the restructuring meeting where Holbrook gets nothing (Chapter 64).

### Oleksandr (Sasha) Hrytsenko (traffic advisor)

Ukrainian-born Ardmorean, born 1970 in Kharkiv; emigrated 1998. Applied mathematician; transport modeling at a Kyiv research institute; PhD in Ardmore; Director, Pellow Transport Economics, from 2009.

He wants a model he can defend and repeat sponsor work. He fears being the forecaster blamed for a failed toll road. He hedges in writing, resists direct pressure, but supplies "sensitivity ranges" from which bid teams choose. Verbal habit: talks in elasticities ("the elasticity on trucks is minus point six, not minus point three").

Where he is wrong: he accepts the bid team's housing timetable without independent check. Arc: produces the bid forecast (2014); revisits it in 2021; gives evidence in 2023; in Chapter 45 his revised ramp-up method is the worked example.

### Owen Reddaway (state treasury official in the restructuring)

Ardmorean, born 1971. Treasury economist, then head of the fiscal risks unit; Deputy Secretary (Commercial), Brannock Treasury, from 2019.

He wants to limit the state's exposure, avoid a termination payment, and avoid a "bailout" headline. He fears setting a precedent that the state rescues failed PPPs, and a rating agency comment. He offers term, tolls and regulation rather than cash, and insists that any state money buys equity. Verbal habit: "The state does not write checks."

Arc: refuses compensation for COVID-19 (2020); in 2023 agrees ARD 120.0 million of new money for 15% of the equity, a six-year extension and the heavy-vehicle toll cut.

### Kirsten Lowry (federal lender)

Ardmorean, born 1968. Credit Director, NILO. Wants to protect the federal loan and the program's no-write-down policy. Uses the springing lien as leverage in 2023 and accepts PIK interest and an extension instead of a haircut. Appears in Chapters 29, 58 and 64.

### Pieter van Wijngaarden

See Section 4.1. Restructuring adviser to the Case T senior lenders from January 2022.

### Elspeth Varga (lenders' traffic advisor; round 1)

Ardmorean, born 1973 in Port Ellery to a Hungarian father who emigrated in 1957 and a Scottish mother. Statistician and transport planner; eight years in the state roads agency's demand-modeling unit; Ridgeway Traffic Consultants from 2005, director from 2011. Leads Ridgeway's work for the bank club, the BIFA bondholders' representative and NILO: the 2014 banking case (Case Bible 2.6), the traffic counts that Rhys Tanaka-Bell's monitoring reports use from 2019, and the 2023 restructuring case behind the plan valuation.

She wants a case lenders can size on and that she can defend after the fact. She fears being the second forecaster blamed for the same road. She does not negotiate; she haircuts, and documents each haircut. Verbal habit: "Which year's survey is that?"

Where she is wrong: her 2014 banking case cuts Pellow's mature level and ramp-up, but it keeps Pellow's Coldwater Plains housing timetable without an independent check, so the banking case also overstates the first years (T-F18). Arc: the 2014 banking case (Chapters 45 and 48); the counts behind the 2019 to 2021 monitoring alarms (sec:79.14); the 2023 restructuring case used for the plan valuation (ssec:64.14.1). Full sheet: Annex TR T.19.

### Lachlan Mereweather (lenders' counsel), Anjali Thevarajah (sponsors' counsel) and Rhys Tanaka-Bell (independent engineer)

Added after the blueprint review so that Case T has the lawyers' seats and the lenders' technical seat in every negotiation. Full sheets, verbal habits and where-wrong notes: Annex TR T.18. Lachlan appears at close (sec:58.13) and in the restructuring plan (ssec:64.14.5); Anjali at close and across the restructuring (Chapters 58 and 64); Rhys in the ramp-up (sec:79.14) and the restructuring evidence (ssec:64.14.1).

## 4.3 Case R characters

### Rafael Quintanilla (fund partner)

American, born 1971 in San Antonio, Texas. Power trader on a Houston utility trading desk (1996 to 2006); built and hedged an ERCOT generation portfolio for a utility (2006 to 2012); Partner, Lattimer Infrastructure Partners, from 2012, leading Fund II's energy transition investments.

He wants to deploy Fund II at target returns and to be known as the investor who understands merchant risk. He fears overpaying in auctions, being wrong on batteries, and another Uri. He knows the market better than most counterparties, prices shape risk tightly, and is impatient with lenders. Verbal habit: "What's the shape?"

Where he is wrong: he underwrites A2 and A3 on 2023 battery revenues that halve in 2024, and his West solar capture assumption in A1 is the high case in hindsight. Arc: wins A1 (2022) at a full price; is hurt by the 2024 battery revenue fall; restores fund returns through the 2025 refinancing; in 2026 brings the data-center repowering idea to his investment committee.

### Carmen Villarreal-Ochoa (asset manager)

American, born 1986 in El Paso, Texas. Electrical engineer; operator at a qualified scheduling entity in Austin (2009 to 2015); asset manager for a solar developer (2015 to 2022); Asset Manager, Mesa Corta Renewables, from 2022.

She wants assets run well and numbers she can stand behind with lenders. She fears hedge settlement surprises, battery degradation, and a compliance breach. She negotiates with data and refuses to sign optimistic budgets. Verbal habit: "Let me pull the settlement data."

Arc: finds the shape mismatch on R1's fixed-volume swap (2023), pushes the augmentation plan for R6 and R7, runs the 2025 refinancing data room.

### Declan Furlong (hedge desk counterparty)

Irish, born 1981 in Cork. Physicist; quantitative analyst on a London utility trading desk; Director, Castellan Bank commodities desk, Houston, from 2014.

He wants margin on hedges and limited credit exposure. He fears being on the wrong side of a scarcity event with a weak counterparty. He is fast and numerical, and always offers an alternative structure. Verbal habit: "I can show you a price."

Arc: sells the R1 fixed-volume swap (2022), structures the R8 fixed-shape hedge (2024), and negotiates the hedges' first-lien ranking with the USPP noteholders (2025).

### Thandeka Mabuza

See Section 4.1. Principal, then Director, at Lattimer from June 2021; leads A2 and A3 diligence and the 2025 refinancing.

## 4.4 Cross-case movements

| Character | Case P | Case T | Case R |
|---|---|---|---|
| Pieter van Wijngaarden | Lead arranger (2017 to 2018); Kilnworth's debt adviser (2025) | Senior lenders' restructuring adviser (2022 to 2023) | – |
| Thandeka Mabuza | ABDB officer (2014 to 2021) | – | Lattimer principal and director (2021 on) |
| Gwen Treharne | Independent engineer (2018 to 2023) | – (her firm, a different partner) | Lenders' independent engineer for the 2025 refinancing |
| Castellan Bank (institution) | MLA, ECA agent, hedge provider | Bank club member | Opco lender, TLB arranger, hedge desk, tax equity investor |
| Kaito Pacific Bank, Sterrenberg Bank NV | Lenders | Bank club | Opco lenders |
| Penhallow Bank | – | Bank club | Opco lender, Redfern lender |

## 4.5 Character name register

| Name | Case | Nationality | Born | Employer |
|---|---|---|---|---|
| Tomasz Wierzbicki | P | Polish | 1972 | Kilnworth Power International |
| Mariama Talmé | P | Kessaran | 1977 | Groupe Talmé |
| Ousmane Talmé | P (minor) | Kessaran | 1946 | Groupe Talmé (founder) |
| Pieter van Wijngaarden | P, T | Dutch | 1966 | Castellan Bank; Quarrington Advisory |
| Adaeze Whitcombe | P | British | 1971 | Pemberton Hale LLP |
| Laurent Bécherel | P | French | 1961 | Ashworth Quayle LLP |
| Abdoulaye Ndao-Sylla | P | Kessaran | 1958 | Ministry of Energy and Hydrocarbons |
| Clémentine Agbo-Lawson | P | Kessaran | 1979 | Ministry of Economy and Finance |
| Hyacinthe Dossa | P | Kessaran | 1964 | SEKA |
| Konrad Elsässer | P | (unnamed home country) | 1960 | Lindauer Kraftwerksbau AG |
| Gwen Treharne | P, R | British (Welsh) | 1966 | Calder Hartmann Engineering |
| Thandeka Mabuza | P, R | South African | 1983 | ABDB; Lattimer |
| Henrike Vosskamp | P | (unnamed home country) | 1975 | Exportgarant |
| Félix Adandé | P (minor) | Kessaran | 1969 | SNHK |
| Yusuf Demirci | P (minor) | Turkish-British | 1979 | Coldharbour Infrastructure Income Fund |
| Margaret (Maggie) Dunleavy | T | Ardmorean | 1965 | Partnerships Brannock |
| Callum Petrie | T | Ardmorean (Scottish-born) | 1974 | Holbrook Infrastructure |
| Oleksandr (Sasha) Hrytsenko | T | Ardmorean (Ukrainian-born) | 1970 | Pellow Transport Economics |
| Owen Reddaway | T | Ardmorean | 1971 | Brannock Treasury |
| Kirsten Lowry | T (minor) | Ardmorean | 1968 | NILO |
| Lachlan Mereweather | T | Ardmorean | 1969 | Galbraith Stowe |
| Anjali Thevarajah | T | Ardmorean (Sri Lankan Tamil descent) | 1975 | Dunmore Pryor |
| Rhys Tanaka-Bell | T | Ardmorean (Welsh and Japanese parents) | 1971 | Calder Hartmann Engineering (Port Ellery) |
| Elspeth Varga | T | Ardmorean (Hungarian and Scottish parents) | 1973 | Ridgeway Traffic Consultants (round 1) |
| Rafael Quintanilla | R | American | 1971 | Lattimer Infrastructure Partners |
| Carmen Villarreal-Ochoa | R | American | 1986 | Lattimer (Mesa Corta) |
| Declan Furlong | R | Irish | 1981 | Castellan Bank |

---

# Part 5. Register of fictional names

Every name below is fictional. Each was checked by web search on October 3, 2026 for a real country, region, well-known city, or organization with the same name in a related field. "Clear" means no such match was found; "Near miss" records the closest real use, which the book never mentions. Real institutions appear only in real-world teaching, never as running-case parties (D-007).

| Name | Type | Case | Check |
|---|---|---|---|
| Republic of Kessara; Kessaran | Country | P | Clear (Bangkok hotel and Thai given name "Kessara"; Indian village Keesara) |
| Kessaran cauri (KCR) | Currency | P | Clear; KCR is not an ISO 4217 code |
| Dabakro | Capital city | P | Not checked separately; Akan-style place name, no well-known city |
| Bélanou | Plant site | P | Clear |
| Moraba River | River | P | Not a well-known place name |
| Sombé West | Gas field | P | Clear |
| Halbeck Energy | Upstream operator | P | Clear |
| Société d'Électricité du Kessara (SEKA) | Utility | P | Clear (country-specific) |
| Société Nationale des Hydrocarbures du Kessara (SNHK) | State gas company | P | Clear (country-specific) |
| Gazoduc Côtier du Kessara SA (GCK) | Pipeline company | P | Clear (country-specific) |
| Office de Régulation de l'Énergie du Kessara (OREK) | Regulator | P | Clear (country-specific) |
| Banque Centrale du Kessara | Central bank | P | Clear (country-specific) |
| Union Bancaire du Kessara (UBK) | Local bank | P | Clear (near miss: Union Bancaire pour le Commerce et l'Industrie, Tunisia) |
| Assurances Générales du Kessara (AGK) | Local insurer | P | Clear (country-specific) |
| Bélanou Power SA | Project company | P | Clear |
| Kilnworth Power International; Kilnworth Operations Services Ltd; Kilnworth Bélanou Holdings | Sponsor and affiliates | P | Clear |
| Groupe Talmé | Local sponsor | P | Clear |
| ABDB Infrastructure Equity Fund | DFI equity fund | P | Clear |
| Atlantic Basin Development Bank (ABDB) | Multilateral DFI | P | Clear |
| Exportgarant | ECA of the unnamed EPC home country | P | Clear (no ECA of that name; German official cover is branded differently) |
| Castellan Bank | International bank | P, T, R | Clear for banks (near misses: US advisory firms named Castellan; Castell Bank, Germany) |
| Banque Raveau | French-style bank | P | Clear |
| Kaito Pacific Bank | Japanese-style bank | P, T, R | Clear |
| Hovland Bank ASA | Norwegian-style bank | P | Clear (Hovland is a Minnesota community and a surname) |
| Sterrenberg Bank NV | Dutch-style bank | P, T, R | Clear |
| Lindauer Kraftwerksbau AG; Lindauer Holding AG | EPC contractor and parent | P | Clear (near miss: Lindauer Dornier, textile machinery) |
| Bati-Kessara SA | Local civil contractor | P | Clear |
| Bergmark Turbinen AG; Bergmark BT-9F | Turbine OEM and LTSA provider; gas turbine model | P | Clear |
| Calder Hartmann Engineering | Independent engineer | P, T, R | Clear |
| Pemberton Hale LLP | Sponsor's counsel | P | Clear (US firms named Pemberton exist; no "Pemberton Hale") |
| Ashworth Quayle LLP | Lenders' counsel | P | Clear |
| Fenwick Lowe Insurance Brokers | Broker | P | Clear |
| Marchbank Risk Advisory | Lenders' insurance advisor | P | Clear |
| Ferrand Model Assurance | Lenders' model auditor | P | Clear |
| Coldharbour Infrastructure Income Fund | Buyer of 2026 stake | P | Clear |
| Quarrington Advisory | Restructuring and debt adviser | P, T | Clear |
| Commonwealth of Ardmore; Ardmorean; Ardmore dollar (ARD) | Country and currency | T | Clear as a country (towns named Ardmore exist in the US and Ireland); ARD is not an ISO 4217 code |
| State of Brannock; Port Ellery; Coldwater Plains; Holloway Junction; Merrick River; Merrick Ridge | State and places | T | Clear |
| Merrick Link; Merrick Link Concession Co Ltd | Road and project company | T | Clear (Merrick Road in New York is a different road) |
| Partnerships Brannock; Brannock Treasury; BRTA; BIFA | State bodies | T | Clear |
| National Infrastructure Lending Office (NILO); Commonwealth Infrastructure Credit Program | Federal lender | T | Clear |
| Ardmore Bank Bill Rate (ABBR) | Reference rate | T | Clear |
| Merrick Motorway Partners; Northgate Mobility Consortium | Bid consortia | T | Clear |
| Holbrook Infrastructure; Holbrook Civil | Construction sponsor | T | Clear |
| Daneshill Construction | D&C partner | T | Clear |
| Corvus Toll Roads; Corvus Road Services | Operator sponsor | T | Clear |
| Wexcombe Infrastructure Fund III | Financial sponsor | T | Clear |
| Pellow Transport Economics | Sponsor's traffic advisor | T | Clear |
| Ridgeway Traffic Consultants | Lenders' traffic advisor | T | Clear |
| Penhallow Bank | Ardmorean bank | T, R | Clear |
| Galbraith Stowe | Case T lenders' counsel (Port Ellery law firm) | T | Clear (separate US firms named Galbraith and Stowe exist; no firm of the combined name; checked October 3, 2026) |
| Dunmore Pryor | Case T sponsors' and concessionaire's counsel (Port Ellery law firm) | T | Clear (Dunmore, Pennsylvania and Pryor, Oklahoma are towns; no firm of the combined name) |
| Lattimer Infrastructure Partners; Lattimer Energy Transition Fund II | Fund manager and fund | R | Clear (Lattimer is an unrelated UK glass-equipment maker) |
| Mesa Corta Renewables LLC; Mesa Corta HoldCo LLC; Mesa Corta OpCo LLC | Platform | R | Clear |
| Thatcher Flats Wind; Sandoval Hills Wind; Ollie Creek Wind; Peeler Draw Solar; Calloway Mesa Solar; Redfern Storage; Kerrigan Storage; Barlow Gap Solar | Assets | R | Clear for Thatcher Flats and Ollie Creek; the others are not names of known ERCOT projects |
| Hollenbeck Energy North America | Seller of A1 | R | Clear (near miss: Hollenbeck Industries, a parts supplier) |
| Tolliver Energy Development LLC | Seller of A2 and A3 | R | Clear |
| Galloway Risk Solutions | Insurer-style hedge provider | R | Clear |
| Orchard Power Retail LLC | Retail electric provider | R | Clear |
| Ostrander Data Systems Inc. | Corporate vPPA buyer | R | Clear |

Names rejected during checking (do not use): Thornfield (UK energy companies), Arnstein (Canadian credit union), Halyard (private equity firms), Redbud (real power plants), Calvera (Spanish hydrogen company), Caliche (Houston storage developer), Sotol Energy (Texas oil operator), Tidewater (infrastructure companies), Kingsmere (UK rail and civils group), Fairhaven (US bank branches and savings bank), Daubeny (UK laboratory project), Sangora (town in Burkina Faso), Bassanga (Burkina Faso), Lusara (fiction).


## 5A. Illustrative names introduced by the round 1 brief revisions (round 1)

These names belong to illustrative examples, drills and exercises outside the three running cases. They are registered here so that no name is used for two different parties and so that every name has a check status. Status values: **Clear (date, by whom)**: a web search found no real organization, project or polity of that name in a related field; **Rename**: a real project, company or polity of the same or nearly the same name exists, so the writer replaces the name in the same style and reports the change; **Rename advised**: a near miss that a reader could take for a real party; **Internal clash**: the name collides with another fictional party in this book; **Not checked**: the writer runs the Part 5 check before drafting (instruction in every brief). Checks by the consolidation editor were run on October 3, 2026 for a risk-ranked sample (names built on real places and project-like names); the remaining names were not individually searched.

### 5A.1 Fictional jurisdictions and currencies

| Name | Use | Units | Check |
|---|---|---|---|
| Republic of Pasundra; Pasundran; Pasundran kati, code PSK | Fictional Southeast Asian republic with a dollar-tariff IPP crisis (Example 3.2, Chapter 3 drill) | u01 | Clear (u01 reviser, October 3, 2026: no country, place or currency of that name; PSK is not an ISO 4217 code) |
| Lembaga Elektrik Pasundra (LEP) | Pasundra's state utility | u01 | Clear by construction (inherits Pasundra) |
| Republic of Tavarra; Tavarran; Tavarran rupee, code TVR | Fictional lower-middle-income South Asian coastal republic, Chapters 85 to 87 only (u17 unit note 7) | u17 | Clear (u17 reviser, October 3, 2026: no place of that name; near misses Tavareh, Iran, and Tavares, Florida, never mentioned); TVR is not an ISO 4217 code |
| Tavarra Power Purchasing Corporation (TPPC); Port Halvan | Tavarra's single buyer; plant site | u17 | Clear by construction (inherits Tavarra); Port Halvan not checked |
| Republic of Corredana; ELNACOR | Chapter 1 illustrative deal (Annex TR N.1), reused in the Chapter 7 drill | u01, u02 | Clear (Annex TR N.1). Reuse recorded in Annex P 7.3: Chapter 7 may reuse Corredana and ELNACOR only consistently with Chapter 1 |
| Valdoria | Fictional state in a u03 example | u03 | Not checked |

### 5A.2 Names that must be replaced or should be

| Name (unit) | Status | Finding (October 3, 2026) |
|---|---|---|
| Thar Surya Power (u03) | Renamed (round 1) to Kesarvan Solar Power Pvt Ltd; not web-checked (consolidation A) | Thar Surya 1 is a real 300 MW solar project in Bikaner, Rajasthan (Enel Green Power India; IFC financing proposed 2021) |
| Al Dhafra Sun Two (u03) | Renamed (round 1) to Rimal Sabkha Solar PJSC; not web-checked (consolidation A) | Al Dhafra PV2 is the real 2 GW Abu Dhabi solar plant (TAQA, Masdar, EDF Renewables, Jinko Power) |
| Termoeléctrica del Sur SA (u02) | Renamed (round 1) to Termoeléctrica Cerro Guanaco SA; not web-checked (consolidation A) | Planta Termoeléctrica del Sur is a real 480 MW combined-cycle plant in Tarija, Bolivia (ENDE) |
| Seti Khola Hydropower (u03) | Renamed (round 1) to Tallo Bhir Hydropower Ltd (u03 and u10); not web-checked (consolidation A) | Seti Khola Hydropower is a real 22 MW run-of-river project in Kaski, Nepal |
| Ocmulgee Valley Electric Membership Corporation (u03) | Renamed (round 1) to Sandhill Fall Line Electric Membership Corporation; not web-checked (consolidation A) | Ocmulgee EMC is a real Georgia electric cooperative (Eastman, Georgia) |
| Calcasieu Point LNG (u03) | Renamed (round 1) to Mermentau Shoals LNG; not web-checked (consolidation A) | Too close to Calcasieu Pass LNG (Venture Global, Louisiana) and the Calcasieu LNG project |
| Ras Gharib Wind SAE (u14) | Renamed (round 1) to Abu Nakhla Wind SAE; not web-checked (consolidation A) | Ras Ghareb Wind Energy SAE is the real 262.5 MW Engie, Toyota Tsusho/Eurus and Orascom wind IPP in Egypt |
| Calatagan Power (u03) | Renamed (round 1) to Tulay Bato Power Corp.; not web-checked (consolidation A) | Calatagan Solar Farm is a real 63.3 MW Solar Philippines plant in Batangas |
| Noor Draa Solaire SA (u14) | Renamed (round 1) to Ksar Amellal Solaire SA; not web-checked (consolidation A) | "Noor" is the brand of Morocco's state solar program (Noor Ouarzazate, Noor Midelt); a "Noor" project company implies a real MASEN project (editor's knowledge; not searched) |
| Bałtyk Wiatr; Bałtyk Północ Wiatr (u03) | Renamed (round 1) to Bursztynowa Ławica Wiatr and Jantarowy Brzeg Wiatr (u03); the u06 drill party (formerly also "Bałtyk Wiatr Holdings") is Pomorskie Wzgórza Wiatr Holdings; not web-checked (consolidation A) | Real Polish offshore wind projects carry the Bałtyk name (Bałtyk I to III; Bałtyk Północ was an earlier project name) (editor's knowledge; not searched) |
| Mid North Wind (u03) | Renamed (round 1) to Yarrowie Gap Wind Pty Ltd; not web-checked (consolidation A) | The Mid North of South Australia hosts many real wind farms (Hallett, Snowtown, Willogoleche); the name reads as a real regional project |
| Darling Downs Storage Pty Ltd (u14) | Renamed (round 1) to Condamine Bend Storage Pty Ltd; not web-checked (consolidation A) | Darling Downs Power Station (Origin) and Darling Downs Solar Farm (APA) are real Queensland assets |
| Moorabool Peaking Partners (u14) | Renamed (round 1) to Lerderderg Peaking Partners; not web-checked (consolidation A) | Moorabool Wind Farm is a real Victorian wind farm |
| Thessaly Airports (u03) | Renamed (round 1) to Pagasitikos Airports S.A.; not web-checked (consolidation A) | Thessaly is a real Greek region with state airports; an "airports" concession under its name implies a real concession |
| Autostrada Pedemontana Est SpA (u14) | Renamed (round 1) to Autostrada Colli Berici Est SpA; not web-checked (consolidation A) | The Pedemontana Lombarda and Pedemontana Veneta motorways are real PPPs (editor's knowledge; not searched) |
| Ostrander Bank (u02) | Renamed (round 1) to Kettleby Bank; not web-checked (consolidation A) | Case R's vPPA buyer is Ostrander Data Systems Inc.; use another bank name |
| Lindqvist Hydro Partners AB (u17) and Lindqvist Kraft AB (u14) | Renamed (round 1) to Forsberga Hydro Partners AB (u17); Lindqvist Kraft AB (u14) is kept; not web-checked (consolidation A) | Two unrelated Swedish parties with the same root; rename one (u17's, which appears later) |
| Calloway Materials Inc (u17) | Renamed (round 1) to Ashwicken Materials Inc; not web-checked (consolidation A) | Case R's asset R5 is Calloway Mesa Solar; rename |
| Campiña Solar and Campiña Sur Solar (u03) | Renamed (round 1) to u03 Exercise 10.11: Marchenilla Fotovoltaica S.L.; u03 Exercise 13.9: Haza del Lirio Solar S.L.; u02 Example 9.4 and Exercise 9.7 (also "Campiña Solar SL"): Cerro Albarizo Solar SL; u11 Example 52.3 (also "Campiña Solar S.L."): Cañada Rosalejo Solar S.L.; not web-checked (consolidation A) | Two different u03 examples; rename one unless they are the same party |

### 5A.3 Names checked clear in this pass

| Name (unit) | Check (October 3, 2026, consolidation editor) |
|---|---|
| Elspeth Varga (Case T character; this version) | Clear: no person of that name found |
| Aldermoor Bank plc (u17) | Clear |
| Orrell Energy plc (u17) | Clear |
| Kurrajong Ridge Energy (u17) | Clear (Kurrajong is a New South Wales locality; no energy company of the name found) |
| Harlow Vantage Energy (u02) | Clear (near misses: Vantage Wind Energy, Washington; Vantage RE, UK; never mentioned) |
| Coral Coast Peaking (u03) | Clear (Coral Coast is a tourism region name in Fiji and Western Australia) |
| Vientos del Chubut (u03) | Clear as a company (Chubut is a real Argentine province; the example may name it as the place) |
| Glasfaser Oberpfalz (u03) | Clear as a company; near miss Glasfaser Direkt (Amberg), a real Upper Palatinate fiber builder, never mentioned |
| Mojave Flats Storage, Tehachapi Mesa Solar, Sangamon Sun (u03) | Clear (near miss: the decommissioned Tehachapi Energy Storage Project) |
| Cholla Ridge Storage HoldCo LLC (u14) | Clear |

### 5A.4 Names checked by the unit revisers

| Names | Unit | Status |
|---|---|---|
| Selat Ombak Power Company; Tessaway Oil Company LLC; Halvergate Energy Credit LP (Halvergate is an English village); Mvuli Paa Energy Ltd | u01 | Clear (u01 reviser) |
| Concesionaria Túnel Cordillera Norte SA; Generadora Litoral Andino SA; Parque Eólico Alto Huelén | u01 | Not individually checked ("Alto Huelén" returned no Chilean place; a real Biobío project, Pillancó, was avoided) |

### 5A.5 Names not yet checked (writer runs the Part 5 check before drafting)

| Unit | Names |
|---|---|
| u02 | Pampa Tamarugal Solar SpA; Bjerregaard Vind; other illustrative parties in Chapters 5 to 9 (the reviser listed these as examples, not a complete list) |
| u03 | Satilla Bioenergy; Altamaha Pellet Company; Fenwick Marsh Power; Calder Turbine Services (shares "Calder" with the cross-case Calder Hartmann Engineering; confirm it is not meant to be the same group); Redmesa Infrastructure Fund; Saguaro Flats Solar; Copperline Renewables; Térmica Río Seco; Complexo Eólico Chapada Alta; Sorraia Gás Comercialização; Ribafria Energia; Central Térmica Valle Hondo; Bayu Rimba Power; Meseta Solar Holdings; Turan Energy; Leeward Islands Power Corporation; Ras Madrakah Power; Nordmark Erzeugung; Mojave Flats Storage (clear, 5A.3); Golfo Azul Energía; Mantaro Alto Generación; Corbeau Deep and Leeward Petroleum; Quebrada Honda Copper; Autocesta Slavonija Istok; Autocesta Posavina; Rio Grande Line; Terminal Bahía Azul; Lakehead Regional Hospital; Ras Mashat IWP; Iskandar DC Holdings; Volta Coast Power; Mount Gawler Copper; Caroni Ammonia; Kwahu Gold; Rocky Pass Iron; Parque Eólico Quebracho Alto; Austral Viento Holdings; Minera Sierra Peñón; Eólica Constructora del Pacífico; Northshore Connector Partners; Viento del Istmo |
| u14 | Atacama Meridian Energía SA; Pampa Lagunas Solar SpA; Laurentide Pension Infrastructure; Rheinmark Infrastruktur Fonds; Polderwind Noord BV; Nordlys Kraft ASA; Caravela Previdência; Hospital Tejo Concessões SA; Autovía del Valle de Lecrín SA; Bayou Ridge Storage LLC; Coastal Prairie Energy Retail LLC; Desierto Alto Solar S. de R.L. de C.V.; Ankobra Power Ltd; Brindabella Energy Ltd; Weserland Energie AG; Halden Infra Partners; Lagune Solaire SA; Hoshino Trust Bank; Sumatra Panas Bumi; Vent du Rif SA; Termoelektrana Sava d.o.o.; Sagebrush Flats Solar Inc.; Soleil du Nord Kessara SA (uses the fictional Kessara: confirm it does not contradict Case P, which has no other IPP named before 2026); Comoé Hydro Partners; Elbtal Energie AG; Halvorsen Ports Capital; Banco Meseta; Viento de Páramo SL; Rheinland Kreditbank AG; Banque Lyonnaise du Rhône; Assicurazioni Laguna SpA; Meseta Sur Híbrido SL; Eléctrica del Duero SA; Sole Appennino Holding SpA; Ao Pradu Power Co. Ltd; Centrale Maasvlakte Oost BV; Kampot Rice Husk Power Co. Ltd; Pradera Verde Energía SA; Central Hidro Vilcanota SAC; Nordvest Vind ApS; Viento y Sol del Bajío SA de CV; Rio Mayo Hidro SA; Sol do Alentejo Lda. |
| u17 | Vegasur Renovables SL; Via Tâmega Norte Concessões SA; Ventos do Seridó Energia SA; Seridó Renováveis Ltda; Hidro Quijos Alto SA; Minera Antapampa SAC; Tres Ríos Royalty Corp; Salud Meseta Concesiones SA; UTE Obras Meseta; Sugarland Run Data Campus LLC; Harbourline Infrastructure Debt; Tsiskari Hydro LLC; Thornbury Infrastructure Partners; Jarrah Flats Solar Pty Ltd; Bursztyn Wind Farm sp. z o.o.; Nordvik Renewables AS; Kestrel Lane Capital; Penrose Fairley Engineers; Mei Ling Tan (character name, Chapter 87); Brandywine Ridge Data Campus LLC; Loch Garvan Storage Ltd; Pampa Verde Hidrógeno SpA; Whitsunday Coast Motorway Pty Ltd; Halcyon Reactor Company; Northfork Power Partners; Brazos Mesa Data LLC; Rheinhafen Bank AG; Ostmarsch Speicher GmbH; Kahurangi Geothermal Ltd (Matter 90) |
| u05 to u13, u15, u16 | Their revision logs do not list the names they introduced; each brief instructs the writer to run the Part 5 check on every invented party before drafting (u13 notes that its 28 examples are unchecked). The consistency checker compiles any new names from the drafts into this table |

Rules: a renamed party keeps its nationality, sector and style; the writer reports the new name in the chapter status note, and the editor adds it here. No name in this part may be used for a running-case party.

---

# Part 6. Storyline by chapter

Every chapter carries a running-case installment (`standards.md` Section 6, item 8). The table gives, for each chapter, the case, the story date, the scene or event, the characters, the figures shown (IDs from Part 7; "inputs" means values stated in Parts 1 to 3), and the state of the case at the start and end of the installment. Where a chapter has no natural beat, the installment is short and marked "(small)". Each installment respects concept ownership: it uses only concepts owned by that chapter or earlier ones, and refers forward only by an explicit one- or two-sentence pointer.

| Ch | Case | Story date | Scene or event | Characters | Figures shown | State at start | State at end |
|---|---|---|---|---|---|---|---|
| 1 | P | April 2015; call April 2, 2015 in London; meeting April 14, 2015 (Annex P) | Closing scene: Tomasz takes a call from Mariama Talmé about Kessara's Emergency Power Plan and books a flight to Dabakro | Tomasz, Mariama | Inputs: 2015 peak demand 2,140 MW against 1,780 MW available | No project | Origination |
| 2 | P | September 2015; investment committee September 17, 2015 (Annex P) | Kilnworth's investment committee weighs project finance against funding Bélanou on Kilnworth's balance sheet; approves project finance and a development budget | Tomasz; Philippa Carrow (chair), Devesh Raval, Niall Brannigan (Annex P) | P-F01 (budget line); inputs: development budget USD 14.8 million; target gearing 75% (forward reference to ssec:8.2.1 for gearing) (central fix 2026-10-03) | Opportunity identified | Decision to project-finance |
| 3 | P | February 2016 (with 1997 to 1999 memory) | Pieter reads the Kessara RFQ and recalls dollar-tariff IPP restructurings he worked on in Jakarta; he flags convertibility to his team (small) | Pieter | None | RFQ issued | Castellan decides to pursue a mandate |
| 4 | P | June 2015 to February 2016 | Co-development agreement (70:30); development team and advisers appointed; lifecycle map of Case P from origination to 2046 transfer; development advisers named (Annex P 2.3); co-development agreement conditional structure (Annex P 1.14.1) (Annex P) | Tomasz, Mariama, Adaeze | P-F01; Case P lifecycle timeline (inputs) | Origination | Development under way |
| 5 | P | Flash-forward: January 2022 invoice | Indexation of the capacity charge from the November 2016 base date; partial indexation; the local share converted at 462.35 and reconverted; real versus nominal tariff | Tomasz, Hyacinthe | P-F02 | Tariff as bid | Indexed tariff for January 2022 |
| 6 | P | July 2016; flash-forward to November 2022 | Castellan's indicative term sheet, pursued before its June 2017 mandate, on 6M LIBOR plus the July 2016 indicative margins (P-F03 and Annex P 4.7 only); the swap explained; Pieter floats a hedging requirement "for the term sheet" without a hedge ratio or pricing (the 80% ratio and the execution-charge fight belong to Chapter 56, September 2017); in November 2022 the LIBOR switch amendment (Term SOFR plus 0.42826%) and the 2018 financial-close margins as the margins in force (central fix 2026-10-03) | Pieter, Tomasz | P-F03, P-F22 | Indicative pricing | Pricing basis understood; transition shown |
| 7 | P | Flash-forward: year to December 31, 2022 | Bélanou Power's first full-year accounts: capitalized IDC, depreciation, tax holiday and deferred tax, receivables swelling with SEKA arrears; accounts on the lenders' reporting basis (Annex P 4.6) (Annex P) | Tomasz; Edwige Akakpo-Sodji, Joanna Sedley (Annex P) | P-F04 | First operating year | Accounts read |
| 8 | P | 2017 (FC base case) | Kilnworth's finance team shows equity IRR at 60% to 80% gearing on the FC base (senior debt set at each gearing; P-F05 equity IRR and debt lines only, never its DSCR lines). The committee sees that even 80% gearing leaves the FC base equity IRR below the 16.0% bid-model target (P-F05; bridge P-F64), and the argument is over how much downside to accept for about 0.5 points (central fix 2026-10-03) | Tomasz, Kunal Mehrotra, Devesh Raval (Annex P) | P-F05 (equity IRR and debt lines), P-F64 (central fix 2026-10-03) | Bid won | Gearing preference set |
| 9 | R | December 2021 | Lattimer's diligence team reads P50, P90 and P99 for R1, R2 and R3; one-year versus ten-year P90; portfolio diversification | Rafael, Thandeka | R-F01 (inputs) | A1 under diligence | Yield view formed |
| 10 | P | August 2017 | First look at the draft PPA: force majeure, Kessaran-law hardship, delay LDs, governing law | Adaeze, Laurent, Hyacinthe | Inputs: PPA delay LD USD 94,150 per day, cap USD 25.0 million | PPA draft received | First markup |
| 11 | P, R | 2016; 2022 | Bélanou's 2x1 F-class technology, heat rate and part load; ERCOT market rules and capture prices for Mesa Corta's assets | Tomasz, Carmen; Mariama (joins Tomasz in the 2016 scene, Annex P 2.1) (round 1) | Inputs: Part 1.2 table; Part 3.5 capture ratios | – | – |
| 12 | P, T | 2017; 2013 | The Sombé West field and the GCK pipeline; the Merrick Link alignment, tunnel and viaduct; Félix asks Tomasz physical questions about the offshore section's outage history and the field's plateau; take-or-pay is not argued here (principle ssec:18.4.1, fuel-side mechanics Chapter 25) (central fix 2026-10-03) | Félix, Callum; Sasha Hrytsenko; optionally Dimitri Kalogeropoulos (Annex TR); Tomasz (Félix puts his questions to Tomasz) (round 1) | Inputs; P-F61 (Sombé West reserve coverage, Annex P 1.7.4) (round 1) | – | – |
| 13 | P | Model build | A practice workbook with Case P's monthly construction flags and the EPC payment profile; the switch to semiannual operating periods is previewed in one sentence (Chapter 39 owns the Case P timeline, R-017, R-131) (central fix 2026-10-03) | – | Inputs: EPC payment profile | – | – |
| 14 | P | October 2016 | Kilnworth's bid-stage risk register v1; register v1 includes a KCR construction-cost row (u04 14.J, adopted as canon under P-C31; P-C58) (round 1) | Tomasz, Mariama | None (qualitative) | Bid submitted | Register v1 |
| 15 | P | March 2017 | Risk matrix and bankability ladder; Pieter and Tomasz argue over who carries grid-interface risk (seeding 2021); the March 2017 matrix carries the KCR construction-cost exposure (u04 15.J; P-C58) (round 1) | Pieter, Tomasz, Gwen; Gwen as Castellan's pre-mandate technical reviewer (P-C18) (Annex P) | None | Register v1 | Risk matrix |
| 16 | P | May 2017 | Mitigation plan: LC, guarantee, PRG, PRI, reserves, swaps, insurance, contingent equity, standby facility; Pieter proposes forwards for the KCR share of the EPC price, the origin of the D-114 hedge (u04 16.J; P-C58); Exhibit 16.6 lists the forwards among the terms at financial close (round 1) | Tomasz, Pieter, Thandeka | Inputs at financial close, labeled: LC formula (P-F39 at the reset date shown: USD 36.2 million in 2022, USD 36.6 million in 2023), Government Guarantee cap 1,250, PRG 41.5 (Board approval June 20, 2018; Thandeka proposes 30 in May 2017), PRI 90% at 1.15%, contingency 38.40, contingent equity 15.4, standby 46.0 (P-C17, P-C44) (Annex P); P-F65 (preview of the forwards traded at close; settlements stay in Chapter 59) (round 1) | Risk matrix | Mitigation plan |
| 17 | P | February 2016 to October 2017 | The PPP Unit's competitive tender; Implementation Agreement and Government Guarantee negotiation; termination compensation principles | Clémentine, Abdoulaye, Tomasz, Adaeze | Inputs: termination regime table; guarantee cap USD 1,250 million | Tender launched | IA and guarantee signed |
| 18 | P | June to October 2017 | PPA negotiation: capacity charge, 90% availability target, contracted heat-rate headroom, fuel pass-through, LC sizing fight; SEKA's opening availability position 92.0% with bonus and malus (Annex P 1.1.1) (Annex P) | Tomasz, Hyacinthe, Adaeze | P-F02, P-F32; P-F39, P-F47 (Annex P) | Draft PPA | PPA signed |
| 19 | P (small) | 2024 | MEF's public debt team compares Bélanou's capacity tariff with a two-sided CfD proposed for Kessara's first solar auction | Clémentine | None | – | – |
| 20 | R | October 2022 to 2023 | The hedge book: R1 swap, R3 proxy revenue swap, R4 shape hedge, R5 vPPA, R6 toll, R7 floor; a Uri-type stress on R1; valuation method ssec:6.8.3; close-out at principle level Chapter 20; hedge value inside the A1 risk-bucket valuation ssec:46.4.2 (R-006) (central fix 2026-10-03) | Rafael, Declan, Carmen | R-F02, R-F03 | A1 closed | Hedge book in place |
| 21 | T, P | 2013 to 2014; 2017 | The Merrick Link toll regime (maximum tolls, escalation, class multipliers); Bélanou's GTA ship-or-pay | Maggie, Callum, Félix | T-F05; inputs (GTA); P-F46 (Annex P) | – | – |
| 22 | P | September to December 2017 | EPC negotiation: delay LD rate calibrated to interest, fixed costs and PPA LDs; caps; performance LDs | Tomasz, Konrad, Gwen, Pieter | P-F33; inputs; P-F47 (heat-rate headroom); P-F65 as a one-sentence forward pointer only (ssec:22.2.1) (round 1) | EPC draft | EPC signed |
| 23 | T | 2014 | Holbrook-Daneshill D&C joint venture; interface with Corvus and the tolling subcontract | Callum; Dimitri Kalogeropoulos (Annex TR) | Inputs: D&C price, LDs; inputs Annex TR T.4 (Annex TR) | Bid team | D&C structure fixed |
| 24 | P | March to April 2018 | LTSA with Bergmark and O&M with Kilnworth Operations; EOH-based fees; out-of-LTSA major maintenance | Tomasz, Gwen | P-F11, P-F34; P-F11 shows the MMRA part only (P-F11b); P-F48 (Annex P) | – | LTSA and O&M signed |
| 25 | P | November 2017 | GSA negotiation: DCQ, MDQ, 80% take-or-pay, make-up, deliver-or-pay, pass-through to SEKA | Tomasz, Félix, Hyacinthe | P-F35 | Draft GSA | GSA signed |
| 26 | P | April 2017 to July 2018 | Shareholders' agreement among Kilnworth, Talmé and the ABDB fund; reserved matters; ROFR without tag-along; equity contribution agreement; development premium; board composition and reserved matters per Annex P 1.14.3 (Annex P) | Tomasz, Mariama, Thandeka; Gaspard Amoussou-Tevi (Annex P) | Inputs: stakes, premium USD 4.85 million | Two sponsors | Three sponsors |
| 27 | P | 2018; 2022 | Insurance program design; DSU daily indemnity sizing; lenders' requirements; the 2022 hard-market step-up | Tomasz, Pieter | Inputs: Part 1.4 insurance table | – | Program bound |
| 28 | P | June 2018 | Full contract map; gap scan; a "Who pays if...?" trace of a grid surge destroying a step-up transformer during commissioning; gap scan includes the GSA-PPA term gap (Annex P 1.7.1) and the absence of a subrogation waiver for SEKA (1.1.8); the grid-surge trace uses an assumed 120-day delay and an assumed USD 7.5 million transformer loss, computed under D-013 and labeled hypothetical (Annex P) | Adaeze, Laurent, Gwen | None | Contracts signed | Gaps logged |
| 29 | P, T | 2017 to 2018; 2014 to 2015 | Case P lender group: commercial banks, Exportgarant cover, ABDB A and B loans; Case T's NILO credit application | Pieter, Henrike, Thandeka, Kirsten | Inputs: tranche shares; ECA eligible value 263.7 and cap 224.1 | Mandate | Lender group formed |
| 30 | P | 2018; 2024 | Why no bond at financial close; a 2024 rating pre-assessment of a refinancing bond | Pieter, Tomasz | None | – | Bond option alive |
| 31 | R, P | March 2022; 2018 | Case R's holdco TLB sized on opco distributions (coverage ratio by forward reference to Chapter 35); Case P's standby and VAT facilities; Case P's standby facility, drawn in 2021 (P-F18; forward reference to Chapter 61) (central fix 2026-10-03) | Rafael, Declan | R-F05 (holdco lines); P-F18 (standby line), P-F37 (VAT facility) (central fix 2026-10-03) | A1 signing | Holdco funded |
| 32 | P | 2017 to 2018 | The equity plan: share capital and shareholder loans, pro rata funding with LCs, contingent equity, development premium, ABDB farm-in; contingent equity drawn in 2021 alongside the standby (P-F18; forward reference to Chapter 61) (central fix 2026-10-03) | Tomasz, Mariama, Thandeka | P-F07 (equity lines) | – | Equity committed |
| 33 | P (small) | Early 2025 | A Gulf bank proposes an ijara tranche for the refinancing; rejected because onshore security would have to be restructured | Pieter, Tomasz | None | – | – |
| 34 | P | 2017 | The ABDB PRG with a donor-subsidized fee; why a KCR loan was not available at the tenor needed | Thandeka, Clémentine | Inputs: PRG 41.5, fee 0.75% | – | PRG proposed at USD 30 million (ABDB management, November 2017); Board approves USD 41.5 million on June 20, 2018 (Annex P) |
| 35 | P | 2018 (FC base) | CFADS for the first full operating year; DSCR, LLCR, PLCR; base, banking and downside cases | Pieter | P-F10, P-F08 (ratios); P-F16 (breakevens), P-F41 (Annex P) | – | – |
| 36 | P | April 2018 | The lenders size the debt: sculpting at 1.35x, the 75% gearing cap, the ECA weighted average life test | Pieter, Tomasz | P-F08, P-F09; P-F36 (Annex P) | Term sheet agreed | Debt sized |
| 37 | P | 2018 | DSRA, MMRA, lock-up and default levels; 80% swap at 2.947%; the hedging policy's currency-hedging requirement: at least 75% of committed KCR construction payments, met by the KCR forwards with Castellan (sec:37.10) (central fix 2026-10-03) | Pieter, Tomasz | P-F11, P-F12 (swap profile); P-F11a (DSRA), P-F11b (MMRA), P-F65 (central fix 2026-10-03) | – | Reserve and hedge structure set |
| 38 | P | 2018 | Pricing: margins, fees, ECA premium, all-in cost by tranche; the credit charge on the KCR forwards as part of the all-in cost (central fix 2026-10-03) | Pieter, Henrike | P-F12 (all-in cost); P-F50, P-F65 (central fix 2026-10-03) | – | – |
| 39 | P | Model build | Model skeleton: timeline, flags, inputs from Exhibit 39.5 (round 1; the reader does not load the JSON file), scenario switch; the two-timeline design with the band-overlap rule as the book's model, the mixed timeline with stubs as the labeled alternative; build-along file model/build/Ch39_*.xlsx (u09 Section 0.1) (round 1) | – | None | – | – |
| 40 | P | Model build (FC base) | Funding sheet: sources and uses, monthly drawdowns, IDC circularity; the KCR forwards in the two-currency Funding sheet (ssec:40.1.4, local-currency costs) (central fix 2026-10-03); build-along file Ch40 with labeled provisional rows (u09 Section 0.1) (round 1) | – | P-F07, P-F13; P-F43, P-F65 (central fix 2026-10-03) | – | – |
| 41 | P | Model build | Revenue and cost build, indexation, tax holiday and deferred depreciation, working capital, VAT facility | – | P-F14, P-F32, P-F34; P-F37, P-F44 (central fix 2026-10-03); P-F10, P-F38, P-F47 (round 1) | – | – |
| 42 | P | Model build | Waterfall, sculpting, reserves, lock-up, dividend trap and the shareholder-loan solution | – | P-F15; P-F45 (central fix 2026-10-03); P-F08, P-F09, P-F11a, P-F11b (round 1) | – | – |
| 43 | P | Model build | Returns, ratios, sensitivities, breakevens, a Monte Carlo on availability and dispatch; Exercise 43.17: an unguided full build of a solar-plus-storage project from a one-page term sheet (blank-workbook test of Capability 4; solution workbook model/exercises/ex43_17/) (round 1) | – | P-F16; P-F42 (central fix 2026-10-03); P-F28, P-F41 (round 1) | – | – |
| 44 | P | June 2018 | Ferrand Model Assurance's audit of the sponsor model: findings and fixes | Pieter, Tomasz | P-F17 | Draft model | Audited model |
| 45 | T, R | 2014; 2021; 2023 | Traffic ramp-up model with Pellow's and Ridgeway's cases against actuals; Case R's yield and capture model | Sasha, Carmen; Elspeth Varga (Ridgeway's banking case against Pellow's, Annex TR T.19) (round 1) | T-F04, T-F06, R-F06; T-F18, T-F19 (Annex TR); R-F01, R-F19 (round 1) | – | – |
| 46 | R | November to December 2021 | Valuing A1 by risk bucket | Rafael, Thandeka | R-F04; inputs Annex TR R.1 (locked-box build-up: headline USD 436.0 million plus ticker 10.3 = USD 446.3 million) and R.7 (terminal value rule); A1 price USD 446.3 million (D-014) (round 1) | Diligence | Bid price set |
| 47 | P, T, R | September 2016; August 2014; December 2021 | Case P's tariff bid; Case T's BAFO contribution and the winner's curse; Case R's A1 auction | Tomasz, Callum, Rafael; Devesh Raval (Annex P); Philippa Carrow, Kunal Mehrotra (Annex P 2.1); Devesh does not say the committee tariff would have lost (P-F62; Annex P 2.1 as amended, P-C53) (round 1) | P-F06, T-F02, R-F04; P-F06 extended (Annex P 4.7), P-F62, P-F64; T-F02 extended, optional T-F21; inputs Annex TR T.2, T.3 (Annex P) (Annex TR); R-F05 (round 1) | Bids prepared | Bids won |
| 48 | P, T | 2018; 2014 | Gwen's IE report walkthrough; Pellow's and Ridgeway's traffic studies compared | Gwen, Sasha; Elspeth Varga (Ridgeway's 2014 study); optionally Rhys Tanaka-Bell (lenders' technical diligence, 2014) (round 1) | T-F04; inputs; P-F61; T-F18, T-F19; IE report content per Annex P 4.1 (Annex P) (Annex TR); P-F47 (round 1) | – | – |
| 49 | P | 2018 | Lenders' legal due diligence report: parallel debt, business pledge, emphyteutic lease, guarantee, FX authorization; KYC on Groupe Talmé | Laurent, Mariama | inputs Annex P 2.4 (Talmé KYC) and 4.2 (lenders' legal due diligence findings) (round 1) | – | – |
| 50 | P | 2017 to 2021 | Resettlement of 214 households; ESAP; Category A review; 2021 grievance and additional compensation | Thandeka, Henrike | Inputs: RAP 5.08; additional 3.27; inputs Annex P 4.3 (ESAP, resettlement, grievance, habitat, Equator Principles) (round 1) | – | – |
| 51 | P | 2018 | The common terms agreement: CPs, representations, covenants, events of default, equity cure, distributions, change of control | Laurent, Adaeze | Inputs: covenant levels; P-F63 (cure amounts for Exercise 51.16), P-F65 (the hedging policy in the common terms agreement) (round 1) | – | CTA agreed |
| 52 | P | 2018; 2023 | Accounts agreement and waterfall; parallel debt; business pledge; the 2023 re-notification fix | Laurent | P-F15 (structure) | – | – |
| 53 | P | 2018; 2025 | Intercreditor agreement: ECA and DFI rights, A/B structure, hedge counterparties, voting; the 2025 bondholder accession | Pieter, Henrike, Laurent (2018 and 2025), Thandeka (2018 only), Adwoa Sarpong-Kumi (2025) (P-C19) (Annex P) | Inputs: tranche shares; P-F65 (the KCR forward counterparty in the intercreditor arrangements) (round 1) | – | ICA signed |
| 54 | P | 2017 | Dispute clauses across PPA, IA and finance documents; treaty protection through the holding company; immunity waiver | Adaeze, Clémentine | None | – | – |
| 55 | P | June to July 2018 | Financial close: CP satisfaction, funds flow on July 17, 2018; Castellan's two approval conditions (ABDB PRG of at least USD 40 million; a satisfactory Ferrand Model Assurance model audit report) narrated per Annex P 2.5 (round 1) | Pieter, Tomasz, Laurent, Adaeze | P-F07; P-F49 (Annex P); P-F65 (round 1) | Documents agreed | Financial close |
| 56 | P | July to October 2017 | Term sheet negotiation: DSCR target, gearing, hedge ratio, lock-up, PRI cost; the hedge-ratio fight follows Annex P 1.15.2: Castellan's July 14, 2017 draft at 90% fixed and 10 bps, landing at 80% in a 75% to 90% band at 7.5 bps; term sheet agreed October 27, 2017 (round 1) | Pieter, Tomasz, Adaeze | P-F36; P-F50 (Annex P) | Indicative terms | Agreed term sheet |
| 57 | T | 2012 | Brannock's decision to procure: business case, PSC, value for money, affordability, contingent liabilities | Maggie, Owen | T-F01 | Corridor need | Decision to procure |
| 58 | T | 2013 to 2015 | Procurement to preferred bidder and close; termination regime and refinancing gain share design | Maggie, Callum, Kirsten; Lachlan Mereweather (lenders' counsel), Anjali Thevarajah (sponsors' counsel) at close (sec:58.13) (Annex TR) | T-F01, T-F02, T-F03; inputs Annex TR T.1, T.2; T-F01 and T-F02 extended, T-F20 (Annex TR) | Decision to procure | Financial close |
| 59 | P | 2022 to 2024 | Offtaker crisis and currency shock: arrears, FX queue, LC drawing, guarantee demands, netting, settlement; the KCR forwards had settled in the project's favor before the devaluation (sec:59.10); no hedge remained after COD (central fix 2026-10-03) | Tomasz, Hyacinthe, Clémentine, Mariama, Abdoulaye; Edwige Akakpo-Sodji, Adwoa Sarpong-Kumi; Sylvestre Ahouansou at the end (Annex P 2.1) (round 1) | P-F20, P-F25; P-F39, P-F40, P-F66 (central fix 2026-10-03); P-F65 (round 1) | Plant operating | Settlement signed |
| 60 | P | 2018; 2022 to 2023 | PRI placement and the 2023 decision not to claim; ABDB's preferred creditor halo; the minister's attack on the dollar tariff; local content | Tomasz, Abdoulaye, Mariama | Inputs: PRI premium 1.15%; P-F51 (Annex P) | – | – |
| 61 | P | August 2018 to November 2021 | Construction: drawdowns, COVID force majeure, civil rework, the transformer failure and insurance claim, LDs, overrun funding, completion tests | Konrad, Gwen, Tomasz, Abdoulaye; Théophile Kpoviessi (Annex P); Gilles Tchibozo (Annex P 2.1) (round 1) | P-F18, P-F19, P-F30; P-F52, P-F66 (central fix 2026-10-03); P-F33 (round 1) | Financial close | COD December 1, 2021 |
| 62 | P | 2022 to 2024 | Operations: reporting, budgets, ratio tests, the June 2023 breach, the October 2023 waiver | Tomasz, Adaeze, Laurent, Henrike; Adwoa Sarpong-Kumi, Imogen Thwaite, Edwige Akakpo-Sodji (Annex P); Gaspard Amoussou-Tevi (Annex P 2.1) (round 1) | P-F21, P-F31; P-F63 (Annex P); P-F21 ledger values 1.13x (December 31, 2022) and 0.96x (June 30, 2023) govern (round 1) | Operating | Waiver in force |
| 63 | P, R | 2025 to 2026; 2025 | Case P bond refinancing and the 24% sale; Case R USPP refinancing and holdco repricing | Pieter, Tomasz, Yusuf, Mariama; Thandeka, Rafael, Declan; Adwoa Sarpong-Kumi, Gaspard Amoussou-Tevi (Annex P); Rosine Gbaguidi-Ayi (Annex P 2.1) (round 1) | P-F23, P-F24, R-F08, R-F09; P-F23 level combined DSCR from the ledger (1.59x), never the 1.35x design floor (round 1) | Pre-refinancing | Refinanced; stake sold |
| 64 | T | 2019 to 2023 | Distress and restructuring: warnings, standstill, A&E, restructuring plan, cram-down, NILO, the state's role | Pieter, Callum, Owen, Kirsten, Maggie; Lachlan Mereweather (lenders' counsel, ssec:64.14.5), Anjali Thevarajah (counsel to the concessionaire and its shareholders), Rhys Tanaka-Bell (lenders' technical and traffic monitoring adviser, ssec:64.14.1) (Annex TR); Elspeth Varga (Ridgeway's 2023 case behind the plan valuation, ssec:64.14.1) (round 1) | T-F07, T-F08, T-F09, T-F10; inputs Annex TR T.10, T.11; T-F20 (Annex TR); T-F09 and T-F10 for the notes: 1.30x is the plan's floor, the ledger minimum notes DSCR governs (T-C25) (round 1) | Lock-up | Restructured |
| 65 | P, R | 2026 looking to 2046; 2026 | Bélanou handback planning; R1 repower-or-retire and decommissioning provisions | Tomasz, Carmen; Gilles Tchibozo, Rosine Gbaguidi-Ayi (Annex P 2.1) (round 1) | P-F29, R-F10; P-F48 (round 1) | – | – |
| 66 | P | 2018 to 2026 | Sponsor accounting: consolidation, equity method, loss of control in 2026, hedge accounting, expected credit losses on SEKA receivables; the KCR forwards designated as a cash-flow hedge of the onshore EPC payments (sec:66.12) (central fix 2026-10-03); the forwards' designation and the removal of their reserve into the cost of the construction asset per Case Bible 1.6; P-F26's consideration excludes the USD 4.0 million deferred consideration (nil at completion), and the swap hedge-reserve recycling is reported outside the loss on loss of control (P-C56) (round 1) | Tomasz, Mariama; Joanna Sedley (Annex P) | P-F26; P-F53, P-F56, P-F66 (Annex P) (central fix 2026-10-03) | – | – |
| 67 | P | 2017; 2025 | Holding structure, treaty withholding rates, interest gross-up, thin capitalization, interest limitation grandfathering, indirect transfer tax | Adaeze, Tomasz | P-F27; P-F37, P-F38, P-F54 (Annex P) | – | – |
| 68 | P, T (small) | 2018; 2015 | Castellan's slotting grade for Case P; Case T's insurer bondholders and their capital treatment | Pieter | P-F55 (Annex P) | – | – |
| 69 | P | 2015 to 2016 | Why a CCGT: Kessara's alternatives (OCGT, coal, HFO) compared; Bélanou in the thermal sector | Abdoulaye, Tomasz | Inputs; P-F16; P-F57 (Annex P) | – | – |
| 70 | R | 2022 to 2025 | Wind and solar in Mesa Corta: capture decline, curtailment, tax credits | Carmen, Rafael | R-F06 | – | – |
| 71 | R (small) | 2025 | Lattimer's IC declines a minority stake in a US offshore wind project | Rafael | None | – | – |
| 72 | P (small) | 2022 | The Moraba hydro cascade in a drought year raises Bélanou's dispatch; MEH's planned 240 MW Moraba Falls project | Abdoulaye; Abdoulaye (as minister, 2022), Prosper Adikpéto (Annex P) | Inputs: hydro 640 MW; P-F58 (Annex P) | – | – |
| 73 | R, P | 2023 to 2024 | R6 toll versus R7 merchant with floor; augmentation; Bélanou's 225 kV interconnection | Carmen, Thandeka | R-F07; R-F18, R-F19 (Annex TR F) (round 1) | – | – |
| 74 | P (small) | 2025 | MEH signs a small modular reactor memorandum; MEF's public debt team weighs it | Clémentine; Sylvestre Ahouansou (may appear) (Annex P) | None | – | – |
| 75 | P | 2017; 2023 | Sombé West upstream financing (Halbeck's reserve-based loan, illustrative) and GCK's ship-or-pay pipeline | Félix; Tomasz (Annex P) | Inputs: reserves 1,140 bcf; P-F46, P-F59 (Annex P) | – | – |
| 76 | P (small) | 2026 | MEH studies an FSRU for LNG imports to back a Bélanou Phase 2 | Tomasz; Devesh Raval (asks the investment committee's question, Annex P 2.1) (round 1) | None | – | – |
| 77 | P (small) | 2025 | Groupe Talmé's plan for a gas-based fertilizer plant | Mariama | None | – | – |
| 78 | P (small) | 2026 | A bauxite developer asks for power from a Bélanou expansion | Tomasz | None | – | – |
| 79 | T | 2019 to 2025 (Callum's scene is set in 2021) (central fix 2026-10-03) | The Merrick Link ramp-up against the record of real toll-road failures | Sasha, Callum; Rhys Tanaka-Bell (lenders' technical and traffic monitoring adviser, sec:79.14) (Annex TR); optionally Elspeth Varga (Ridgeway's counts in the monitoring reports) (round 1) | T-F04, T-F06, T-F18, T-F19 (Annex TR) | – | – |
| 80 | T (small) | 2024 | Brannock procures a light-rail line as an availability PPP after the Merrick Link | Maggie | inputs Annex TR T.13; Nerida Faulkes optional (Annex TR) | – | – |
| 81 | T (small) | 2016 | Partnerships Brannock's availability-based hospital PPP as the contrast to user-pay | Maggie | inputs Annex TR T.14; Nerida Faulkes optional (Annex TR) | – | – |
| 82 | R | 2024 to 2026 | Ostrander's data-center growth and the credit of the R5 vPPA counterparty | Rafael, Carmen | None | – | – |
| 83 | R (small) | 2024 | Lattimer screens and passes on a hydrogen offtake from R2 | Rafael | None | – | – |
| 84 | R, P | 2025 | The USPP labeled green; why Case P's bond was not; physical climate risk at Bélanou (sea level, cooling-water temperature) | Thandeka, Tomasz; Gwen (two lines) (Annex P) | None | – | – |
| 85 | P (with T, R) | September 2016 | A one-hour screen of Case P at bid stage; quick screens of T and R | Pieter | Inputs; P-F60 (Annex P) | – | – |
| 86 | P | May 2018 | Castellan's credit paper for Case P | Pieter; Clive Ormesher (Annex P) | P-F28; P-F28 per Annex P 8.3, P-F55 (Annex P); P-F39, P-F61 (round 1) | – | Credit approval |
| 87 | P, T, R | 2016 to 2026 | Careers and judgment: Pieter, Thandeka and Tomasz; an intermediary's 2016 approach during the tender, which Kilnworth reports; the 2016 intermediary approach per Annex P 2.6 (Annex P) | Pieter, Thandeka, Tomasz, Clémentine | None | – | – |
| 88 | R | March 2026 | Lattimer's IC weighs a 15-year data-center PPA from a repowered R1 using the new-structure framework | Rafael, Carmen, Thandeka | None | – | Open decision |

Concept-ownership notes for writers:

- Chapters 5 to 8 use flash-forwards and the FC base case; they never discuss DSCR (Chapter 35), reserves (Chapter 37), or the covenant breach (Chapter 62).
- Chapter 7's 2022 accounts show trade receivables rising; the narrative names the cause (SEKA paying late) without teaching payment security (Chapter 59).
- Chapter 20 introduces R1's fixed-volume swap and its Uri stress. Valuation method: ssec:6.8.3; close-out at principle level: Chapter 20; hedge value inside the A1 risk-bucket valuation: ssec:46.4.2 (R-006).
- Cells marked "(Annex P)" or "(Annex TR)" merge the row amendments of Annex P 2.2 and Annex TR T.16; cells marked "(central fix 2026-10-03)" apply the blueprint review (`reviews/blueprint/central-fixes-log.md`); text marked "(round 1)" merges the storyline requests in the revision logs of the round 1 briefs (`reviews/blueprint/consolidation-B-log.md`). The annexes still govern where they differ.
- Chapter 31 shows the holdco loan's size and the cash it depends on, with a forward reference to Chapter 35 for the coverage ratio.
- Chapter 59 may say that the DSRA was drawn (Chapter 37) but leaves the covenant breach and waiver to Chapter 62.
- Chapter 61 tells the insurance claim using Chapter 27's covers; Chapter 28's "Who pays if...?" trace of the same kind of event is written in 2018 as a hypothetical and must not reveal that the event later happened.

---

# Part 7. Figure register

The modelers compute each figure below from the input files and record its values in the figure ledgers (`model/figure-ledger-case-p.md`, `model/figure-ledger-case-t.md` and `model/figure-ledger-case-r.md`; Case P ledger at model v1.3) under the same ID. Writers cite figures by ID in their status notes. "Scenario" names a scenario from Sections 1.10, 2.8 and 3.8. A figure marked "inputs" needs no model run; it is listed so that every running-case number in the book has an ID.

## 7.1 Case P

| ID | Figure | Scenario | Chapters |
|---|---|---|---|
| P-F01 | Development budget (USD 14.8 million approved 2015) against actual costs to close (USD 21.43 million), by year | Inputs (annual split: 2015 3.12, 2016 6.87, 2017 7.64, 2018 3.80) | 2, 4 |
| P-F02 | Capacity charge, fixed O&M charge and VOM charge indexed to the January 2022 invoice; real versus nominal; reconversion rate: the ledger prints the 2022 H1 average KCR rate, the model's proxy for the invoice-date Central Bank mid rate of the contract (Annex P 1.1.5, P-C54); US CPI path illustrative (D-046) (round 1) | Actual history indices | 5, 18 |
| P-F03 | Indicative 2016 all-in floating cost by tranche (6M LIBOR at 2016 levels plus margins and fees annualized); 6M LIBOR input approximate; Case P rate paths illustrative (D-046) (round 1) | Inputs plus simple calculation | 6 |
| P-F04 | 2022 income statement, balance sheet and cash flow statement of Bélanou Power SA | Actual history | 7 |
| P-F05 | Equity IRR at gearing of 60%, 65%, 70%, 75% and 80% (senior debt set at each gearing; Chapter 8 prints only the equity IRR and debt lines) | FC base | 8 |
| P-F06 | Levelized tariff of the winning bid under the RFP evaluation formula; runner-up 4.6% higher | FC base inputs | 47 |
| P-F07 | Sources and uses at financial close, including IDC, fees, ECA premium, DSRA; equity split between share capital and shareholder loans | FC base | 32, 40, 55 |
| P-F08 | Senior debt by tranche; binding constraint; minimum and average DSCR on base, banking and downside; LLCR at close | FC base, banking, downside | 35, 36, 42 (round 1) |
| P-F09 | Sculpted repayment profile; ECA weighted average life and largest installment tests | FC base | 36, 42 (round 1) |
| P-F10 | CFADS build for the first full operating year | FC base | 35, 41 (round 1) |
| P-F11a | DSRA initial balance (Annex P 8.3 split) | FC base | 37, 42 (round 1) |
| P-F11b | MMRA accumulation schedule (Annex P 8.3 split) | FC base | 24, 37, 42 (round 1) |
| P-F12 | Swap notional profile; hedged and unhedged cost; all-in cost of debt by tranche including ECA premium | FC base | 37, 38 |
| P-F13 | Monthly construction drawdown schedule and IDC | FC base | 40 |
| P-F14 | Tax computation OY1 to OY10: holiday, deferred depreciation, minimum turnover tax | FC base | 41 |
| P-F15 | Cash waterfall OY1 to OY3; distributions; dividend-trap check with and without shareholder loans | FC base | 42, 52 |
| P-F16 | Equity IRR, project IRR, NPV at 16.0%, payback; sensitivity table; breakevens | FC base and sensitivities | 35 (breakevens), 43, 69 |
| P-F17 | Model audit findings (seeded errors and their effect on debt size), specified by the Chapter 44 brief | FC base | 44 |
| P-F18 | Actual construction sources and uses; overrun funding (contingency, LDs, DSU, FX forward gains, standby, contingent equity; both drawn in ledger v1.2, P-C43); IDC against FC base | Actual history | 31, 32, 61 |
| P-F19 | Completion test results; performance LDs; effect of the prepayment and the 581.9 MW reset on projected DSCR | Actual history | 61 |
| P-F20 | Arrears path; cash DSCR by period 2022 H1 to 2025 H1; DSRA drawing and replenishment; FX losses | Actual history | 59 |
| P-F21 | Historic DSCR at June 30, 2023; waiver economics (fee, margin uplift, deferral); ledger values (1.13x at December 31, 2022; 0.96x at June 30, 2023) govern any other note (round 1, P-C57) | Actual history | 62 |
| P-F22 | Interest cost before and after the LIBOR switch; effect of the 0.42826% spread adjustment; Term SOFR and LIBOR inputs are Case P illustrative paths (D-046) (round 1) | Actual history | 6 |
| P-F23 | 2025 bond size; transaction costs; swap unwind value; new combined profile and DSCR; NPV effect for equity; the combined DSCR is level by construction and is a model output (1.59x in the ledger); 1.35x was the Version 1.0 design floor (round 1, P-C51) | Actual history | 63 |
| P-F24 | Equity value at December 31, 2025 at 13.75% and 12.50%; price for 24%; Kilnworth's realized IRR on the sold stake; indirect transfer tax | Actual history | 63 |
| P-F25 | Termination compensation at June 30, 2023 under SEKA default, project company default and natural force majeure, against senior debt outstanding | Actual history | 17 (formula only), 59 |
| P-F26 | Kilnworth's accounting: consolidation to September 30, 2026; remeasurement gain on loss of control; equity-method carrying value; the consideration line is the cash price and excludes the USD 4.0 million deferred consideration, measured at nil at completion; the parent share of the swap hedge reserve recycled (2.1) is reported outside the loss on loss of control (round 1, P-C56) | Actual history | 66 |
| P-F27 | Withholding tax leakage on distributions and shareholder loan interest, treaty against domestic rates; commercial-tranche interest gross-up cost | FC base and actual | 67 |
| P-F28 | Credit paper key metrics at close (definition in Annex P 8.3) | FC base, banking, downside | 43, 86 (round 1) |
| P-F29 | Handback reserve accumulation and plant condition at transfer (assumption-based) | Actual history | 65 |
| P-F30 | Insurance claim: EAR material damage and DSU computation | Inputs | 61 |
| P-F31 | OY1 actual against the FC base case: availability, revenue, opex, CFADS | Actual history and FC base | 62 |
| P-F32 | Example monthly invoice for January 2022: capacity, VOM and fuel charges | Actual history | 18, 41 |
| P-F33 | Delay LD calibration: daily interest, fixed costs and PPA LDs at the scheduled COD, compared with USD 247,300 | FC base | 22, 61 (round 1) |
| P-F34 | Operating cost build OY1 to OY10, including LTSA fixed and variable fees | FC base | 24, 41 |
| P-F35 | Annual gas volume against DCQ and the take-or-pay level at base, banking and downside dispatch | FC base | 25 |
| P-F36 | Senior debt at DSCR targets of 1.30x, 1.35x and 1.40x and gearing caps of 70%, 75% and 80% | FC base | 36, 56 |
| P-F37 | VAT on the onshore EPC portion: VAT paid, refunds, VAT facility balance and interest, peak VAT receivable and refund-lag cost; working capital balances OY1 to OY3 (Annex P 8.1) | FC base | 31, 41, 67 |
| P-F38 | Thin capitalization computation and disallowed shareholder loan interest (Annex P 8.1) | FC base and actual | 41, 67 |
| P-F39 | SEKA LC amount at COD under the two-plus-one and three-month formulas; reset values 2022 to 2025 (Annex P 8.1) | FC base and actual | 16, 18, 59, 86 |
| P-F40 | FX losses, netting set-offs, settlement installments, guarantee demand-to-payment days, FX queue duration; the February 14, 2023 LC drawing (Annex P 8.1; P-C44); netting set-offs: the ledger gives the average per month for 2023 H2 and 2024 H1; a monthly series is requested (`bible/model-requests-round1.md`) (round 1) | Actual | 59 |
| P-F41 | PLCR at close; period-by-period CFADS and DSCR on the three FC cases (Annex P 8.1) | FC cases | 35, 43 (round 1) |
| P-F42 | Monte Carlo on availability and dispatch with locked debt (Annex P 8.1) | FC base | 43 |
| P-F43 | Convergence log of the FC sizing; equity-first funding variant (Annex P 8.1) | FC base | 40 |
| P-F44 | Revenue build OY1 to OY10 by component (Annex P 8.1) | FC base | 41 |
| P-F45 | FC base financial statements OY1 to OY3 with balance check (Annex P 8.1) | FC base | 42 |
| P-F46 | GTA charges 2022 and their pass-through; GCK's revenue from the Bélanou GTA (Annex P 8.2) | Actual | 21, 75 |
| P-F47 | Heat-rate headroom as an annual fuel margin (Annex P 8.2) | FC base | 18, 22, 41, 48 (round 1) |
| P-F48 | LTSA run-out date by dispatch case (Annex P 8.2) | FC base, banking, low dispatch, actual | 24, 28, 65 |
| P-F49 | Funds flow at financial close, July 17, 2018 (Annex P 8.2); itemization of every use in the month-1 total (USD 121.59 million) requested so that Exhibit 55.10 reconciles without a residual (round 1) | FC base | 55 |
| P-F50 | PV of the 7.5 bps swap credit and execution charge; the 10 bps opening (Annex P 8.2) | FC base | 38, 56 |
| P-F51 | PRI insured amount and premium by period (Annex P 8.2) | FC base and actual | 27, 60 |
| P-F52 | Planned against actual EPC progress and payments by quarter (Annex P 8.2) | FC base, actual | 61 |
| P-F53 | ECL allowance on SEKA receivables; swap MTM and hedge reserve (Annex P 8.2) | Actual | 66 |
| P-F54 | Estimated UK Multinational Top-up Tax on Kilnworth's share (Annex P 8.2) | Actual | 67 |
| P-F55 | Castellan: underwriting and holds, swap line, slotting, RWA and capital, RAROC (Annex P 8.2) | FC base | 68, 86 |
| P-F56 | IFRIC 12 financial-asset presentation and reconciliation to the lenders' basis (Annex P 8.2) | Actual | 7 (one-line note), 66 |
| P-F57 | Kessara 2015 technology screening curves (Annex P 8.2) | Inputs | 69 |
| P-F58 | Actual dispatch and gas burn, 2022 (Annex P 8.2) | Actual | 72 |
| P-F59 | Halbeck RBL borrowing base, 2017 and 2023 (Illustrative; Annex P 8.2) | Illustrative inputs | 75 |
| P-F60 | September 2016 bid-stage screen (Annex P 8.2) | Bid-stage inputs | 85 |
| P-F61 | Sombé West reserve coverage (Annex P 8.2) | Inputs | 12, 48, 86 (round 1) |
| P-F62 | Bid comparison: levelized tariffs of the four bids (Annex P 8.2) | Bid inputs | 47 |
| P-F63 | Equity cure amount needed at June 30, 2023 (Annex P 8.2); pro rata prepayment cure requested as an extension for Exercise 51.16 (round 1) | Actual | 51, 62 (round 1) |
| P-F64 | Bid-to-close equity IRR bridge from the 16.0% bid-model IRR to the FC base (Annex P 8.2; D-037, formerly the second D-017) | FC base re-sized at each step | 8, 46, 47 (round 1) |
| P-F65 | KCR forwards traded at financial close: share hedged, KCR notional, forward rates and USD equivalents by settlement date (D-114); one forward per monthly onshore EPC payment; the ledger prints every sixth month of the profile and the totals (round 1, P-C52) | Contract (FC) | 16 (preview), 22 (pointer), 37, 38, 40, 51, 53, 55, 59, 61, 66 (round 1) |
| P-F66 | KCR forward settlements and mark-to-market to COD; unhedged comparison (D-114) | Actual | 59, 61, 66 |

## 7.2 Case T

| ID | Figure | Scenario | Chapters |
|---|---|---|---|
| T-F01 | PSC and PPP present costs; value for money for the reference and the winning bid; retained-toll-revenue breakeven requested as an extension (round 1) | Inputs plus PV | 57, 58 |
| T-F02 | Bid equity IRR at the ARD 287.4 million contribution; the contribution needed at 11.4% on the banking case | Bid base, banking | 47, 58 |
| T-F03 | Sources and uses at close; senior, NILO and equity amounts; contribution bridge | Bid base and banking | 58 |
| T-F04 | Traffic: Pellow, Ridgeway, downside and actual, 2019 to 2026 | Inputs | 45, 48, 79 |
| T-F05 | Nominal toll per km by class, 2015 to 2030, original and restructured regimes | Inputs plus indexation | 21 |
| T-F06 | Revenue ramp-up: forecast against actual, 2019 to 2025 | Bid base, banking, actual | 45, 79 |
| T-F07 | Senior DSCR history 2019 H2 to 2023 H2 against banking projections | Actual history | 64 |
| T-F08 | Termination compensation under concessionaire default (estimated fair value) against senior claims at June 30, 2022 | Actual history | 64 |
| T-F09 | Restructuring: claims, write-down, new notes, equity split, recoveries by class, NILO | Actual history | 64 |
| T-F10 | Post-restructuring projections: DSCR, equity value, state revenue share; minimum notes DSCR 2.00x and sculpting divisor 2.65x (T-F09) are the outcome; 1.30x is the plan floor (round 1, T-C25) | Ridgeway 2023 case | 64 |
| T-F11 | Senior sizing: capacity under each constraint, binding constraint, sculpting divisors (added by the modeler) | Banking | 58, 64 |
| T-F12 | Ratio summary for bid base, banking and downside: DSCR, ramp-up DSCR, senior plus NILO DSCR, LLCR, PLCR (added by the modeler) | Bid base, banking, downside | 47, 58, 64 |
| T-F13 | Sensitivities on the bid base: equity IRR, NPV, minimum DSCR (added by the modeler) | Bid base | 47, 79 |
| T-F14 | Scheduled senior and NILO balances on the financing at close (added by the modeler) | Banking | 29, 58 |
| T-F15 | Outturn: equity invested and lost, first event of default, DSRA use (added by the modeler) | Actual history | 64, 79 |
| T-F16 | Tax at the restructuring: losses and debt forgiveness (added by the modeler) | Restructuring case | 64 |
| T-F17 | Illustrative USD equivalents of financing at close and restructuring amounts (added by the modeler) | Banking, restructuring case | 58, 64 |
| T-F18 | Ratio of actual traffic to Pellow, Ridgeway banking and downside cases, 2019 to 2026, and to Ridgeway 2023 from 2024 (Annex TR) | Inputs | 45, 48, 79 |
| T-F19 | Traffic shortfall against Pellow by cause, 2019 to 2022 (Annex TR T.17) | Actual history | 45, 48, 79 |
| T-F20 | Performance payments to BRTA by half-year 2019 to 2025 and effect on CFADS (Annex TR T.1) | Actual history | 58, 64 |
| T-F21 | Optional: bid equity IRR at ARD 287.4 million on Pellow's low and central VoT cases (Annex TR T.3) | Bid variants | 47 |

## 7.3 Case R

| ID | Figure | Scenario | Chapters |
|---|---|---|---|
| R-F01 | P50, P90 and P99 (one-year and ten-year) by asset, uncertainty components, correlations, and correlated portfolio P50/P90/P99 | Yield model | 9, 45 (round 1) |
| R-F02 | Hedge book by year: volumes, prices, share of revenue contracted, hedged and merchant | Base | 20 |
| R-F03 | Uri-type stress on R1's fixed-volume swap | Sensitivity | 20 |
| R-F04 | A1 valuation by asset and risk bucket at bid; enterprise value against the USD 446.3 million price | Base, low, high | 46, 47 |
| R-F05 | A1 sources and uses; opco term loan sizing by bucket; holdco TLB sizing | Base, P99 | 31, 47 (round 1) |
| R-F06 | Capture price and revenue build by asset, 2022 to 2030 | Base and low | 45, 70 |
| R-F07 | A2 and A3 valuation and funding; ITC transfer proceeds | Base | 73 |
| R-F08 | 2025 refinancing: USPP size by series, blended coupon, swap unwinds, holdco repricing, distribution to the fund | Base | 63 |
| R-F09 | Fund returns on Case R to December 31, 2025: gross IRR, multiple, NAV | Base | 63 |
| R-F10 | Decommissioning obligations by asset | Base | 65 |
| R-F11 | Redfern loan and holdco incremental loan; early opco TL DSCRs and 2024 holdco coverage (added by modeler) | Base | 31, 73 |
| R-F12 | Opco debt by asset (opco TL 2022, USPP 2025) (added by modeler) | Base | 31, 63 |
| R-F13 | Scenario and sensitivity results: CFADS, DSCRs, holdco coverage, fund IRR (added by modeler) | All | 20, 45, 70, 73 |
| R-F14 | Cash tax and NOL profile (added by modeler) | Base | 70 |
| R-F15 | USPP debt service, DSCR and balance profile (added by modeler) | Base | 63 |
| R-F16 | Opco TL sculpted debt service and balance profile (added by modeler) | Base | 31 |
| R-F17 | Repriced holdco balance and coverage profile (added by modeler) | Base | 63 |
| R-F18 | R7 revenue floor: reference revenue, Galloway floor payments, premium, upside share by contract year 2024 to 2032 (Annex TR R.4) | Base, low, high | 20, 73 |
| R-F19 | R6 and R7 usable energy, augmentation MWh and cost, revenue scaling by year (Annex TR R.5) | Base | 45, 73 |

## 7.4 Figure mentions in the round 1 briefs (automated index; round 1)

The Chapters column of 7.1 to 7.3 lists the chapters that print a figure. This index lists every chapter whose revised brief cites the ID in a line that is not a replacement, withdrawal or neighbor note (script scan of `bible/briefs/u01.md` to `u17.md`, October 3, 2026). It over-counts pointers and assumed-concept rows, so it is a checklist for the consistency checker, not a license to print: a chapter prints a figure only if the Chapters column or its storyline row lists it.

| ID | Chapters whose brief cites it |
|---|---|
| P-F01 | 2, 4, 5, 32, 46 |
| P-F02 | 5, 6, 9, 18, 22, 41, 85 |
| P-F03 | 5, 6, 7, 9, 85 |
| P-F04 | 6, 7, 8, 66 |
| P-F05 | 7, 8, 9 |
| P-F06 | 47 |
| P-F07 | 26, 32, 34, 36, 38, 39, 40, 41, 55, 56, 86 |
| P-F08 | 34, 35, 36, 38, 41, 42, 43, 44, 86 |
| P-F09 | 36, 41, 42, 43, 45, 86 |
| P-F10 | 34, 35, 38, 41, 51 |
| P-F11 | 28, 37, 45 |
| P-F11a | 24, 28, 37, 41, 42, 43, 45, 86 |
| P-F11b | 24, 28, 37, 41, 42, 43, 45 |
| P-F12 | 34, 37, 38, 39, 67, 86 |
| P-F13 | 13, 39, 40, 41 |
| P-F14 | 40, 41, 42 |
| P-F15 | 41, 42, 43, 52 |
| P-F16 | 35, 38, 42, 43, 44, 45, 46, 69, 86 |
| P-F17 | 41, 43, 44, 45, 49 |
| P-F18 | 40, 61, 86 |
| P-F19 | 22, 61, 86 |
| P-F20 | 59, 60, 86 |
| P-F21 | 59, 62, 86 |
| P-F22 | 5, 6, 7 |
| P-F23 | 63, 66, 67, 84, 86 |
| P-F24 | 63, 66, 67 |
| P-F25 | 17, 59 |
| P-F26 | 66 |
| P-F27 | 41, 42, 43, 67 |
| P-F28 | 43, 86, 88 |
| P-F30 | 61 |
| P-F31 | 62 |
| P-F32 | 22, 40, 41, 59 |
| P-F33 | 22, 61 |
| P-F34 | 24, 40, 41, 42 |
| P-F35 | 25 |
| P-F36 | 36, 38, 56 |
| P-F37 | 31, 34, 40, 41, 42, 45, 67 |
| P-F38 | 40, 41, 42, 45, 49, 67 |
| P-F39 | 16, 22, 34, 45, 59, 60, 86 |
| P-F40 | 45, 59, 60, 86 |
| P-F41 | 35, 38, 42, 43, 44, 45 |
| P-F42 | 42, 43, 44, 45 |
| P-F43 | 36, 39, 40, 41, 42, 45 |
| P-F44 | 40, 41, 42, 45 |
| P-F45 | 41, 42, 43, 45 |
| P-F46 | 21, 22, 75 |
| P-F47 | 11, 18, 22, 41, 48, 50 |
| P-F48 | 24, 28, 65 |
| P-F49 | 55, 56 |
| P-F50 | 37, 38, 56 |
| P-F51 | 27, 60 |
| P-F52 | 61 |
| P-F53 | 66, 86 |
| P-F54 | 67 |
| P-F55 | 68, 86, 88 |
| P-F56 | 66 |
| P-F57 | 69 |
| P-F58 | 72 |
| P-F59 | 75 |
| P-F60 | 85, 88 |
| P-F61 | 12, 25, 48, 50, 76, 77, 86 |
| P-F62 | 47, 50, 58 |
| P-F63 | 51, 56, 62, 65 |
| P-F64 | 7, 8, 9, 32, 43, 45, 47, 50 |
| P-F65 | 16, 22, 34, 37, 38, 39, 40, 41, 51, 55, 59, 66, 86 |
| P-F66 | 38, 40, 59, 66 |
| T-F01 | 34, 56, 57, 58, 60 |
| T-F02 | 34, 47, 50, 58, 60, 85 |
| T-F03 | 29, 58, 66, 68, 85, 86 |
| T-F04 | 44, 48, 79 |
| T-F05 | 21, 22 |
| T-F06 | 44, 45, 79 |
| T-F07 | 64 |
| T-F08 | 64 |
| T-F09 | 64, 65 |
| T-F10 | 64 |
| T-F11 | 45 |
| T-F15 | 64 |
| T-F16 | 64 |
| T-F18 | 44, 48, 64, 79, 83 |
| T-F19 | 44, 45, 48, 64, 79, 83 |
| T-F20 | 58, 60, 64 |
| T-F21 | 47, 50 |
| R-F01 | 8, 9, 44, 45 |
| R-F02 | 20, 22 |
| R-F03 | 20, 22 |
| R-F04 | 45, 46, 85, 86 |
| R-F05 | 30, 31, 46, 86 |
| R-F06 | 11, 44, 45, 70, 83 |
| R-F07 | 73 |
| R-F08 | 63, 84 |
| R-F10 | 65 |
| R-F11 | 45 |
| R-F18 | 20, 22, 73 |
| R-F19 | 44, 45, 73 |

---

# Part 8. Change log

Every change to a case after this version is logged here. "Date in story" is when it happens to the case; "Chapter" is where the reader learns of it; "Source of figure" is "assumption (Case Bible section)" or a figure ID. The rows already entered are the planned changes built into the cases at Version 1.0, so that later edits can be traced against them.

| # | Date in story | Chapter | Case | Item changed | Old value | New value | Source of figure |
|---|---|---|---|---|---|---|---|
| P-C01 | 2016-12-08 | 47 | P | Shareholding | Kilnworth 70%, Talmé 30% | unchanged until close | Assumption (1.5) |
| P-C02 | 2018-07-17 | 26, 32 | P | Shareholding at close | 70:30 | Kilnworth 60%, Talmé 25%, ABDB fund 15% | Assumption (1.5) |
| P-C03 | 2020-09 | 61 | P | EPC guaranteed completion date | 2021-04-30 | 2021-08-05 (COVID EOT, 97 days) | Assumption (1.9) |
| P-C04 | 2021-06 to 2022-02 | 61 | P | EPC guaranteed completion date | 2021-08-05 | 2021-10-20 (grid event EOT, 76 days) | Assumption (1.9) |
| P-C05 | 2022-02 | 61 | P | PPA RCOD | 2021-07-31 | 2022-01-20 | Assumption (1.9) |
| P-C06 | 2021-12-01 | 61 | P | COD | 2021-05-01 | 2021-12-01 | Assumption (1.9) |
| P-C07 | 2021-11 | 61 | P | Contracted capacity | 588.4 MW | 581.9 MW | Assumption (1.9) |
| P-C08 | 2018 to 2021 | 61 | P | Construction cost | FC budget | +USD 39.27 million hard costs plus model financing costs | Assumption (1.9); P-F18 |
| P-C09 | 2022-06-30 | 61 | P | Senior debt | FC profile | Prepaid by USD 18.485 million performance LDs; first repayment moved to 2022-06-30; 25 installments | P-F19 |
| P-C10 | 2023-01-01 | 6 | P | Loan base rate | 6M LIBOR | 6M Term SOFR + 0.42826% | Assumption (1.9); P-F22 |
| P-C11 | 2023-07-01 | 6 | P | Swap floating leg | 6M LIBOR | Compounded SOFR + 0.42826% | Assumption (1.6) |
| P-C12 | 2023-10-26 | 62 | P | Margins, fee, principal schedule | FC terms | +0.50% to 2024-12-31; 0.25% fee; 60% of 2023-12-31 principal deferred | Assumption (1.9); P-F21 |
| P-C13 | 2024-03-21 | 59 | P | SEKA arrears | Unsettled | 15 installments to June 2025; 40% of late interest waived | Assumption (1.9) |
| P-C14 | 2025-06-30 | 63 | P | Debt structure | Four tranches plus standby | ECA tranche, A-loan, 7.875% bond to 2037 | Assumption (1.9); P-F23 |
| P-C15 | 2026-09-30 | 63 | P | Shareholding | Kilnworth 60% | Kilnworth 36%, Coldharbour 24% | Assumption (1.9); P-F24 |
| T-C01 | 2014-08-15 | 47, 58 | T | State contribution | Reference ARD 410.0 million | Bid ARD 287.4 million | Assumption (2.3) |
| T-C02 | 2019-05-06 | 45 (first revealed; Chapters 64 and 79 restate it) | T | Opening date | 2019-03-31 | 2019-05-06 | Assumption (2.2) |
| T-C03 | 2022-05-20 | 64 | T | Bank maturity and margin | 2022-05-27; 2.60% | 2023-12-31; 3.25% | Assumption (2.8) |
| T-C04 | 2023-12-18 | 64 | T | Senior debt, equity, NILO terms, concession term, tolls | Original | Per Section 2.8 restructuring table | Assumption (2.8); T-F09 |
| T-C05 | 2012-11-08 | 57, 58 | T | PSC risk adjustments (modeler calibration, pre-publication; editor-in-chief note) | Construction 221.7; traffic revenue 274.0; operating 41.3; competitive neutrality 38.4 (ARD m, PV 2012) | Construction 115.3; traffic revenue 87.4; operating 18.5; competitive neutrality 19.6; VfM reported as a share of the risk-adjusted PSC | Assumption (2.3); T-F01. Old values gave a reference VfM of 52% of the PSC |
| T-C06 | 2014-08-15 | 47, 58 | T | CPI in the bid, banking, downside and sensitivity runs (modeler calibration, pre-publication; new) | Not specified | 2.5% a year from 2015; actual CPI path only in actual-history runs | `inputs_case_t.json` modeler_assumptions; T-F02, T-F03 |
| T-C07 | 2015-05-27 | 58 | T | Ramp-up structure and senior sizing (modeler calibration, pre-publication; new) | No ramp-up provision; senior "about 55%", NILO 22% to 25% (design targets) | Ramp-up interest account at completion (pays senior interest above banking CFADS/1.50 to the first repayment); DS = max(interest, CFADS/s) to 2048; sizing adds 1.50x interest cover in every repayment period, which binds: senior 51.1%, NILO 26.9% of funding net of contribution (23.1% of eligible costs) | Assumption (2.5); T-F03, T-F11 |
| T-C08 | 2019-12-31 | 64 | T | Covenant test timing (modeler calibration, pre-publication; new) | Not specified | First test covers six months; default DSCR covenant first tested 2020-12-31; no distributions before 2021-06-30 | Assumption (2.5, 2.8); T-F07 |
| T-C09 | 2015-05-27 | 29, 58, 64 | T | NILO profile (modeler calibration, pre-publication; new) | Sculpted 2024-2052; restructured maturity 2058 | Sculpted on CFADS after senior debt service; capped at 33% of eligible costs with equity topping up; restructured repayment 2031-06-30 to 2058-12-31 | Assumption (2.5, 2.8); T-F14 |
| T-C10 | 2023-11-30 | 64 | T | Plan classes, votes and plan valuation (modeler calibration, pre-publication; editor-in-chief note) | Not specified | Classes: (1) banks 100% for; (2) bondholders 88.6% turnout, 91.4% of votes cast for; (3) NILO for; (4) shareholders and shareholder lenders 60% for (Holbrook against), dissenting class crammed down (nil in the relevant alternative). Plan valuation: equity at 14.0%, notes at a 7.50% yield; state ARD 120.0 million = 15% subscription at plan value plus implied capital grant for the interchange upgrade | Assumption (2.8); T-F08, T-F09 |
| T-C11 | 2022-06-30 | 64 | T | Termination comparison inputs (modeler calibration, pre-publication; new) | Not specified | Fair value on pre-tax unlevered cash flows at 9.0% (Ridgeway 2023 case without the heavy-vehicle uplift, original terms); retendering costs ARD 12.5 million; handback works estimate ARD 42.6 million (2015 prices) funded over 10 periods | Assumption (2.5, 2.7); T-F08 |
| R-C01 | 2023-08-31 | 73 | R | Portfolio | R1 to R5 | Adds R6 | Assumption (3.6) |
| R-C02 | 2024-04-02 and 2024-12-19 | 73 | R | Portfolio | R1 to R6 | Adds R7 and R8 | Assumption (3.6) |
| R-C03 | 2025-12-16 | 63 | R | Debt structure | Opco TL, holdco TLB, Redfern loan | USPP notes; repriced holdco | Assumption (3.7); R-F08 |
| R-C04 | 2021-12-09 | 46, 47 | R | A1 enterprise value (modeler calibration, pre-publication) | USD 1,184.6 million | USD 446.3 million | Assumption (3.6); R-F04. v1.0 price was 2.7x the base-case breakeven value of USD 438.2 million given Bible revenues, costs and discount rates |
| R-C05 | 2023-06-02 | 73 | R | A2 price (modeler calibration, pre-publication) | USD 132.4 million | USD 63.7 million | Assumption (3.6); R-F07 |
| R-C06 | 2024-02-15 | 73 | R | A3 prices (modeler calibration, pre-publication) | R7 USD 171.9 million; R8 USD 168.3 million | R7 USD 87.4 million; R8 USD 101.9 million | Assumption (3.6); R-F07 |
| R-C07 | 2025-10-21 | 63 | R | USPP series split (modeler calibration, pre-publication) | 30/40/30 | Sequential amortization by tenor; series sizes are model outputs | Assumption (3.7); R-F08 |
| R-C08 | n/a | n/a | R | Expected debt ranges, design targets only (modeler calibration, pre-publication) | Opco TL 520-600; holdco TLB 160-210; USPP 750-860 (USD m) | Superseded by model outputs | R-F05, R-F08 |
| R-C09 | 2021-12 | 9 | R | P99 one-year by asset (modeler calibration, pre-publication; editor-in-chief note) | R1 81.2%, R2 84.0%, R3 80.1%, R4 91.9%, R5 91.4%, R8 91.6% | R1 77.5%, R2 80.4%, R3 76.2%, R4 90.2%, R5 89.5%, R8 89.8% (normal, from the P90s) | Assumption (3.3); R-F01 |
| R-C10 | 2021-12 | 9 | R | Yield uncertainty model and inter-asset correlations (modeler calibration, pre-publication; new) | None | Normal; long-term and inter-annual components; IAV correlations wind-wind 0.60 (West/Panhandle), 0.30 (with coastal), solar-solar 0.85 (West), 0.50 (West-South), wind-solar -0.10; long-term 0.50 within technology, 0 across | Assumption (3.3); R-F01 |

| T-C12 | 2013-09-02 to 2015-05-27 | 47, 58 | T | Procurement terms | Unspecified | Three-stage evaluation; ARD 20.0m bid security; committed-finance rules; Northgate traffic basis; third consortium's reason | Annex T.2 (book inputs) |
| T-C13 | 2015-05-27 | 23, 58 | T | Performance regime | "KPI deductions" only | Lane charges, KPI points, ARD 2,400 per point, 2.5% cap, thresholds 300/500/800 | Annex T.1 |
| T-C14 | 2019 to 2025 | 58, 64 | T | Actual performance payments | None | 2019 0.38 to 2025 0.07 (ARD m) by half-year | Annex T.1; T-F20 |
| T-C15 | 2015-05-27 | 23 | T | D&C cap, interface agreement, tolling subcontract | Unspecified | 60% aggregate cap; Interface Agreement; Quillfield subcontract; acceptance test | Annex T.4 |
| T-C16 | 2019-02 to 2019-05-06 | 23, 79 | T | Cause of the 36-day delay | Unspecified | Tolling acceptance test failure; JV recovers ARD 3.42m from Quillfield | Annex T.4 |
| T-C17 | 2016 to 2017 | 12, 23 | T | Tunnel ground and method | Unspecified | Sandstone/siltstone with fault zone; sequential excavation; JV absorbs overrun | Annex T.6 |
| T-C18 | 2059-05-26 | 58, 65 | T | Handback requirements | Reserve only | Schedule 15 requirements; surveys at 60 and 24 months | Annex T.8 |
| T-C19 | 2023-12-11 | 64 | T | Plan classes, votes, judgment date | Unspecified | Four classes; class 4 dissents and is crammed down; judgment December 11, 2023 | Annex T.10 |
| T-C20 | 2023-12-18 | 64 | T | State's ARD 120.0m characterization | 15% of equity | Subscription at plan value plus capital grant | Annex T.11; T-F09 |
| T-C21 | n/a | 57 | T | Owen Reddaway's career dates | Undated | Fiscal Risks Unit director 2009 to 2015 | Annex T.12 |
| T-C22 | 2019 to 2025 | 45, 47, 58, 64, 79 | T | Model v1.1 (modeler calibration, pre-publication): annex TR inputs absorbed | v1.0 | Performance payments in actual-history CFADS (moves T-F07 to T-F10, T-F15, T-F16 by up to ARD 0.7 million or 0.01x; no covenant outcome changes); Pellow low and central VoT bid runs; T-F18 to T-F21 and T-F01, T-F02, T-F04 extensions; bid-base IRR 12.3% retained (editor ruling: bidder priced on its sponsor case) | Annex T.1, T.3, T.9, T.17; T-F18 to T-F21 |
| R-C11 | 2021-08 to 2022-03-22 | 47 | R | A1 process and price mechanism | Price only | Locked box at 2021-09-30; headline 436.0 plus 5.00% ticker; total 446.3 unchanged; W&I terms; bids 421.5 and 409.0 | Annex R.1 |
| R-C12 | 2024-04-02 | 20, 73 | R | R7 floor reference and settlement | Floor terms only | Benchmark index times availability; quarterly with annual true-up | Annex R.4; R-F18 |
| R-C13 | 2023-07-14 and 2024-04-02 | 45, 73 | R | Battery overbuild and fade | Augmentation only | 8% overbuild; fade 2.0 / 1.5 / 1.0 points a year | Annex R.5; R-F19 |
| R-C14 | 2025-10 | 84 | R | Green USPP framework | Label only | Framework, Quenby SPO, reporting, no greenium | Annex R.6 |
| R-C15 | n/a | 46 | R | Terminal value wording | "Terminal (after 2040)" and "no terminal value" | Post-2040 tail rate within useful life; no TV beyond life; no post-2040 levered rate | Annex R.7 |
| R-C16 | 2026-02-17 | 88 | R | Data-center offer terms | Tenor only | Ketterman Digital Campuses; options A and B; repowering parameters | Annex R.8 |
| R-C17 | 2020-03; 2024-11 | 20, 82 | R | Ostrander profile and vPPA credit support | Absent | Profile; thresholds 10.0 and 15.0; LC 5.0 | Annex R.2 |
| R-C18 | 2024-03 to 2024-05 | 83 | R | Hydrogen developer offer | Unnamed | Marlowe Gulf Hydrogen; 12 years at USD 39.00/MWh; IC passes May 2024 | Annex R.3 |
| P-C41 | 2022-06 to 2025-06 | 59, 62 | P | Cash effect of SEKA arrears (modeler calibration, pre-publication) | Not specified (full overdue increase hits cash) | 80% of overdue amounts are energy-charge arrears matched by deferred payments to SNHK and GCK (formalized by the June 2023 netting agreement); 20% hits cash | Assumption; P-F20, P-F21, P-F40 |
| P-C42 | 2021 onward | 24, 41 | P | LTSA equivalent operating hours (modeler rule, pre-publication) | Hours fixed at 8,059 a year | Hours scale with availability and with dispatch relative to 76.5% (8,439 EOH a year per unit at base) | Annex 1.5; P-F48 |
| P-C43 | 2021-05 to 2021-11 | 61 | P | Construction overrun: delay-related costs (modeler calibration, pre-publication; editor rulings v1.2 and v1.3) | Hard-cost overrun USD 39.27 million; standby and contingent equity not drawn | Plus USD 42.17 million delay-related costs incurred Months 34 to 40: EPC claims settlement: COVID-19 disruption and compensable events beyond the 9.40 variation order (Lindauer, settled at taking-over) 12.00; Acceleration agreement with Lindauer to hold taking-over at November 2021 after the grid event 9.50; Extended owner's costs and site team beyond the 6.93 (owner's engineer, site team, security, camp) 7.20; Re-commissioning after the grid event (repeat backfeed, protection coordination study, OEM field service) 6.40; Transformer replacement expediting, freight and installation not recovered under the EAR policy 3.10; Additional IE, lenders' legal and expert-determination costs beyond the 0.86 2.35; Operator mobilization and training held seven months longer (O&M contractor standby) 1.62; standby drawn USD 10.0 million and contingent equity USD 3.3 million after contingency, delay LDs, DSU and FX gains | P-F18 |
| P-C44 | 2022-01-01; 2023-02-14 | 16, 18, 59 | P | SEKA standby LC amount (editor ruling) | USD 33.8 million (2022); drawing USD 33.8 million | USD 36.2 million on the two-plus-one formula (2022); drawing USD 36.6 million (2023 reset); overdue path unchanged | P-F39, P-F40 |
| P-C45 | 2018-07-17 | 37, 38, 40, 59, 66 | P | Construction FX hedge (D-114) | No currency hedge | USD/KCR forwards with Castellan buying KCR for 75% of onshore EPC payments (KCR 32,204 million; average forward 612.6), covered-parity pricing, cash-settled; settlements USD 4.40 million gain | P-F65, P-F66 |
| P-C46 | 2017-10; 2023 | 75 | P | Halbeck RBL expected borrowing base (annex 4.13; editor ruling v1.3) | About USD 420 million at signing; about 360 million at the 2023 redetermination | USD 280.7 million at signing; USD 362.7 million in 2023 (model logic: sales capped at contracted SNHK demand, 40% reserve tail, completion-basis NPV; inputs unchanged) | P-F59 |
| P-C47 | 2016-09 | 46, 47 | P | Kilnworth bid model reconstruction for the P-F64 bridge (modeler calibration, pre-publication) | Bid-model IRR 16.0% (annex 4.7); bid-model base rate not stated | Swapped base rate 3.44% flat, solved so that the reconstruction returns 16.0% with the annex 4.7 indicative terms, the 655 capex, no PRI or WHT gross-up, no mini-perm, no VAT facility interest, no minimum turnover tax or thin cap, KCR flat; the bridge to the FC base (13.3%) is sequential with no residual | P-F64 |
| N-C01 | n/a | 1, 89 | All | Name register | Unregistered | Part N entries | Annex N |
| P-C49 (was the second P-C46; renumbered round 1) | 2017 | 8 | P | Chapter 8 scene premise (central fix) | "Committee wants 80% gearing to protect the 16.0% bid target" | No gearing up to 80% reaches 16.0% on the FC base (P-F05); the scene argues over downside for about 0.5 points, with the bid-to-close bridge P-F64; characters per Annex P 2.2 | P-F05, P-F64 |
| P-C50 (was the second P-C47; renumbered round 1) | 2016-07 | 6, 56 | P | Chapter 6 scene (central fix) | 2018 margin grid in a July 2016 scene; Pieter insists on an 80% hedge priced by Castellan | July 2016 indicative margins only (P-F03, Annex P 4.7); Pieter floats a hedging requirement without ratio or pricing; the 80% and execution-charge fight is staged once, September 2017 (Chapter 56, Annex P 1.15.2) | P-F03 |
| P-C48 | 2017-11 | 12, 25 | P | Chapter 12 scene (central fix) | Félix argues for take-or-pay | Félix asks physical questions (offshore outages, plateau); take-or-pay is argued only in Chapter 25 | Inputs |
| T-C23 | 2014 to 2023 | 58, 64, 79 | T | Case T cast (central fix; coverage review defect 10) | No lenders' counsel, sponsors' counsel or lenders' technical seat | Lachlan Mereweather (Galbraith Stowe), Anjali Thevarajah (Dunmore Pryor), Rhys Tanaka-Bell (Calder Hartmann) | Annex TR T.18 |
| T-C24 | 2021 | 79 | T | Callum's Chapter 79 story date (central fix) | Annex TR "2021" against Part 6 "2019 to 2025" | Callum's Chapter 79 scene is set in 2021 within the row's 2019 to 2025 span | Annex TR T.16 |

| P-C51 | 2025-06-30 | 63 | P | 2025 bond combined DSCR wording (round 1; ledger wins) | "Sculpted ... to a combined base-case minimum DSCR of 1.35x" | Level combined DSCR is a model output, 1.59x (P-F23); 1.35x was the design floor | P-F23 |
| P-C52 | 2018-07-17 | 37, 40, 66 | P | KCR forward settlement profile and accounting (round 1) | "Seven semiannual settlement dates"; no hedge designation recorded | One forward per monthly onshore EPC payment (ledger profile); designated as cash flow hedges under IFRS 9, reserve removed into the cost of the construction asset | P-F65, P-F66 |
| P-C53 | 2016-09-19 | 47 | P | Devesh Raval's "where wrong" (round 1) | The committee's higher tariff "would probably have lost the bid" | The committee tariff (USD 74.35/MWh levelized) would still have beaten the runner-up (USD 76.36/MWh); his error was dismissing the Gulf bidder's threat without measuring the margin | P-F62; Annex P 2.1 |
| P-C54 | 2022-01 | 5, 18, 41 | P | Reconversion rate shown in P-F02 (round 1) | Contract: Central Bank mid rate on the invoice date | Contract term unchanged; the model and ledger use the 2022 H1 average rate as a proxy and say so | P-F02; Annex P 1.1.5 |
| P-C55 | n/a | 5, 6, 18, 22 | P | US macro paths (round 1) | Unlabeled | Labeled "Case P index (illustrative)" (D-046); no model rerun | D-046 |
| P-C56 | 2026-09-30 | 66 | P | P-F26 reading (round 1) | Deferred consideration and hedge-reserve recycling unstated | Consideration excludes the USD 4.0 million deferred consideration (nil at completion); recycling (2.1, swaps only) outside the 82.0 loss | P-F26 |
| P-C57 | 2023-06-30 | 62 | P | Covenant-breach DSCRs in the modeler's case-state note (round 1) | 1.14x and 0.97x (`model/case-state-case-p.md`) | Ledger P-F21 governs: 1.13x (December 31, 2022) and 0.96x (June 30, 2023); case-state correction requested | P-F21 |
| P-C58 | 2016-10 to 2017-05 | 14, 15, 16 | P | Additions to the P-C31 canon (round 1, u04) | No currency row; no forward proposal | KCR construction-cost row in register v1 and the March 2017 matrix; Pieter's May 2017 proposal of forwards for the KCR share of the EPC price | Annex P 9.1; D-114 |
| P-C59 | 2018-07-17 | 26, 32 | P | Case Bible 1.5 ABDB entry text aligned with P-C24 (round 1) | "Pro rata to their stakes" | 10 points from Kilnworth, 5 from Talmé | Annex P 1.14.2 |
| T-C25 | 2023-12-18 | 64 | T | Restructured notes DSCR wording (round 1; ledger wins) | "Sculpted ... at 1.30x minimum DSCR" | 1.30x is the plan floor; sculpting divisor 2.65x and minimum notes DSCR 2.00x are the outcome | T-F09, T-F10 |
| T-C26 | 2014 to 2023 | 45, 48, 64, 79 | T | Lenders' traffic advisor character (round 1) | Ridgeway Traffic Consultants unnamed | Elspeth Varga, director, Ridgeway | Annex TR T.19 |
| N-C02 | n/a | 1 to 88 | All | Name register for round 1 illustrative names (round 1) | Unregistered | Part 5A entries with check status | Part 5A |

Rows T-C12 to T-C21, R-C11 to R-C18 and N-C01 are detailed in `bible/case-bible-annex-tr.md` (Annex TR, October 3, 2026), which takes precedence over this file where they differ. Change-log ID collision fixed in round 1: P-C46 and P-C47 were each used twice; the Halbeck RBL row (P-C46) and the bid-model reconstruction row (P-C47) keep their IDs, which D-115 and Annex P 4.13 cite, and the two central-fix scene rows become P-C49 (Chapter 8) and P-C50 (Chapter 6). Documents written before this version that cite "P-C46" for the Chapter 8 premise or "P-C47" for the Chapter 6 scene mean P-C49 and P-C50.

Template for new entries:

| # | Date in story | Chapter | Case | Item changed | Old value | New value | Source of figure |
|---|---|---|---|---|---|---|---|
| X-Cnn | YYYY-MM-DD | NN | P, T or R | | | | |

---

# Part 9. Notes for the modelers

1. Build each case from its JSON file and nothing else. If an input is missing or ambiguous, log a change request in `bible/decisions.md` rather than inventing a value.
2. Case P needs four runs: FC base, FC banking, FC downside, and actual history. The FC runs use the forward LIBOR curve in `macro.usd_base_rates.fc_forward_libor_6m_pct` and an FX path projected from 2018 at 7.5% Kessaran and 2.2% US inflation; the actual run uses historical paths. In the FC runs, contingency is spent pro rata with EPC payments; in the actual run, contingency is spent on the listed overrun items first.
3. Case P debt sizing: sculpt aggregate senior debt service to CFADS divided by 1.35 on the FC base, compute the PV at the all-in senior rate (hedged and unhedged blend plus margins), cap at 75% gearing, then test the downside (1.20x), the LLCR (1.40x) and the ECA constraints. Report which constraint binds. Resolve the IDC and fee circularity by iteration with a convergence tolerance of USD 1,000 and report the number of iterations.
4. Case P actual run: re-sculpt at COD to the same final maturity on 25 installments with the same 1.35x target applied to the re-forecast CFADS (the lenders' COD re-sculpting), apply the performance LD prepayment on June 30, 2022, and then apply the crisis cash flows (receipts reduced by the change in overdue receivables, FX losses deducted), the waiver terms, the refinancing and the sale.
5. Case T: the bid base and banking runs share the financing; size on the banking case. The actual run follows the events in Section 2.8 and applies the restructuring at December 31, 2023.
6. Case R: value each asset by year and risk bucket. Classify revenue in each year as contracted (PPA, vPPA strike leg, PRS fixed leg, toll, floor up to the floor level), hedged (fixed-volume and fixed-shape hedge volumes) or merchant (the rest). Tax equity cash to the investor is deducted before Mesa Corta's share.
7. Every model output that a chapter will print goes into the figure ledger with its ID, scenario, value, unit and the model version that produced it. Ranges stated in this file are design targets; report any output that falls outside its range to the editor-in-chief before the ledger is released, together with the input that drives it.
