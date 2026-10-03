# Case Bible

Version 1.0, October 3, 2026. Owner: Case Bible designer, under the editor-in-chief. Binding on every writer, reviewer, and modeler.

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
| Fixed O&M charge | USD 2.31/kW-month | 62% indexed to US CPI; 38% converted to KCR at the bid base rate of 462.35, indexed to Kessaran CPI, and reconverted to USD at the invoice-date rate |
| Variable O&M charge | USD 3.86/MWh | 70% US CPI; 30% Kessaran CPI with the same reconversion |
| Fuel charge | Pass-through | Net energy (MWh) times the contracted heat rate at the dispatched load times 1.108 divided by 1,055,056, times the GSA gas price (USD/MMBtu); plus GTA charges and dispatch-caused GSA take-or-pay amounts as pass-throughs |

Indices reset January 1 and July 1 using values lagged three months. Capacity payments equal the capacity charge times contracted capacity times the lesser of 1 and availability divided by the 90.0% target; there is no bonus above target. Contracted capacity is 588.4 MW until the completion tests reset it to the tested 581.9 MW.

Payment security: a standby letter of credit issued for SEKA by UBK and confirmed by Castellan Bank equal to two months of estimated capacity charges plus one month of estimated energy charges (USD 33.8 million in 2022), to be replenished within 30 days of any drawing; a Government Guarantee from the Ministry of Economy and Finance covering SEKA's payment obligations and termination amounts, capped at USD 1,250 million; and a USD 41.5 million partial risk guarantee from the Atlantic Basin Development Bank (ABDB) that backs Castellan's reimbursement claim on the Republic if it pays under the LC confirmation and SEKA and the government fail to reimburse it. A donor facility subsidizes the PRG fee to 0.75% a year; this is Case P's concessional element (Chapter 34). Late payment interest is 6M Term SOFR plus 2.00% (6M LIBOR plus 2.00% before 2023).

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

The ABDB fund bought its 15% at financial close from Kilnworth and Talmé pro rata to their stakes, paying its share of development costs plus a development premium of USD 4.85 million.

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
| ECA constraints to test | Repayment term from COD of 14 years or less; weighted average life of repayment 7.25 years or less; no installment above 25% of principal; first repayment within six months of COD |
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

No FX hedge: the tariff is USD-indexed and paid in KCR at the prevailing rate, so the project company's exposure is to convertibility, transfer delay, and SEKA's ability to pay, not to the exchange rate itself.

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
| 2018-07-17 | Financial close; swaps traded |
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
| 2023-02-14 | SEKA LC drawn (USD 33.8 million); not replenished |
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

Total delay: 214 days. The extended EPC guaranteed completion date was October 20, 2021 (April 30 plus 173 days); taking-over on November 30, 2021 was 41 days late, so delay LDs are 41 times USD 247,300, or USD 10.1393 million. The RCOD moved from July 31, 2021 to January 20, 2022, so no PPA delay LDs were payable. Insurers declined to pursue a subrogated claim against SEKA after the Ministry of Energy intervened; Chapter 61 tells why.

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

The model adds the extra IDC and commitment fees from the seven-month delay and the DSRA re-sizing. The funding order is: unused contingency (USD 38.40 million), EPC delay LDs, DSU proceeds, then the standby facility and contingent equity 75:25 for any remainder (figure P-F18; expected drawing USD 5 million to USD 15 million).

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

Further assumptions: Central Bank FX queue from November 7, 2022 to March 29, 2024 with an average conversion lag of 47 days; FX losses on trapped cauris of USD 1.27 million (H2 2022), USD 3.84 million (H1 2023), USD 1.12 million (H2 2023) and USD 0.31 million (H1 2024); LC drawn for USD 33.8 million on February 14, 2023 and never replenished; Government Guarantee demands of USD 21.6 million (April 18, 2023, paid July 26, 2023), USD 18.9 million (July 12, 2023, paid November 30, 2023) and USD 17.4 million (October 9, 2023, unpaid and folded into the settlement); tripartite netting agreement of June 29, 2023 (up to USD 9.0 million a month of SEKA energy-charge arrears set off against the project company's gas payables to SNHK); settlement agreement of March 21, 2024 providing 15 monthly installments from April 2024 to June 2025 with 40% of late payment interest waived.

### Covenant breach and waiver (2023)

The historic DSCR at June 30, 2023 falls below the 1.10x default level (expected between 0.80x and 1.00x; model figure P-F21). The DSRA pays the June 30, 2023 shortfall. Waiver and amendment letter of October 26, 2023: tests at June 30 and December 31, 2023 waived; waiver fee 0.25% of outstanding senior debt; margin uplift 0.50% from July 1, 2023 to December 31, 2024; 60% of the December 31, 2023 principal installment deferred and repaid in four equal parts on June 30, 2024, December 31, 2024, June 30, 2025 and December 31, 2025; 100% of arrears recoveries applied to DSRA replenishment first; distributions locked up until two consecutive historic DSCR tests of at least 1.25x and a full DSRA.

### Refinancing (2025)

Settled June 30, 2025, an interest payment date, so no loan breakage. A USD senior secured amortizing project bond (144A/Reg S, listed), coupon 7.875% semiannual (30/360), issue price 99.512, final maturity June 30, 2037, rated B+ by one agency against a B- sovereign, with a USD 95.0 million ABDB partial credit guarantee (fee 1.10% a year, upfront fee 0.75%). Bond proceeds prepay the commercial tranche, the B-loan and the standby facility; the ECA-covered tranche and the A-loan stay in place and consent to the bond's maturity beyond 2034. Bond amount equals the prepaid principal after the June 30, 2025 scheduled payment plus transaction costs (underwriting 1.00% of the bond, other costs USD 3.10 million) less the swap unwind receipt; no upsizing, so the interest limitation grandfathering survives. The swaps attributable to the prepaid tranches are terminated at market (flat swap rate 3.68% for the remaining profile; the project company receives the value because 2.947% is below market). The bond amortizes on a profile sculpted with the remaining ECA and A-loan debt service to a combined base-case minimum DSCR of 1.35x (figure P-F23).

### Partial sale (2026)

Kilnworth sells 24% of the project company (40% of its 60% holding) in shares and shareholder loans pro rata to Coldharbour Infrastructure Income Fund. SPA signed April 14, 2026; locked-box date December 31, 2025 with a 6.50% a year ticker; completion September 30, 2026. Buyer's discount rate 13.75% (USD, post-tax, levered); Kilnworth's reserve discount rate 12.50%; price = 24% of equity value at the agreed rate (model, P-F24). Deferred consideration of USD 4.0 million if SEKA's overdue receivables stay at zero through June 30, 2027. W&I insurance limit USD 18.0 million. Consents: lenders and bondholders (Kilnworth must keep at least 30% until 2030), SEKA, MEH under the IA, and right-of-first-refusal waivers by Groupe Talmé and the ABDB fund. Kilnworth pays the 15% indirect transfer tax on its gain. After completion Kilnworth holds 36% and stops consolidating the project company (Chapter 66).

## 1.10 Case P scenarios

| Scenario | Definition |
|---|---|
| FC base | Financial close base case: COD May 1, 2021; 588.4 MW; base availability and dispatch; FC forward LIBOR curve; FX projected from 2018 by inflation differential using 2018 expectations (Kessaran CPI 7.5%, US CPI 2.2%) |
| FC banking | FC base with 72.0% dispatch |
| FC downside | Availability 6.5 points lower every year, heat rate +1.5%, fixed opex +10% |
| Actual history | Every event in Section 1.9 with historical macro paths to H1 2026, assumptions after |
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

Partnerships Brannock built the business case and public sector comparator (PSC) in 2012 at a nominal discount rate of 6.85%. The PSC, in ARD millions of 2012 present value: raw capital cost 1,478.6; O&M and lifecycle 486.2; toll revenue retained by the state (1,821.4); construction risk 221.7; traffic revenue risk 274.0; operating risk 41.3; competitive neutrality 38.4. The PPP reference project assumed a state construction contribution of ARD 410.0 million paid at opening, retained risks of 52.8 and contract management of 21.6. The model computes PSC and PPP present costs and value for money (figure T-F01). Land (ARD 212.5 million) is common to both and excluded.

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
| Ridgeway Traffic Consultants | Lenders' traffic advisor |
| Calder Hartmann Engineering | Lenders' independent engineer (cross-case firm; the Case T team is led by a different partner, not Gwen Treharne) |
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
| Restructured Senior Notes | 76.0% of claims; single class; 5.10% fixed; sculpted semiannual amortization June 30, 2024 to December 31, 2052 at 1.30x minimum DSCR on the Ridgeway 2023 case; 50% excess cash sweep to December 31, 2030 |
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
| R1 | Thatcher Flats Wind | 96 x 2.1 MW | 201.6 MW | 2014-12-15 | West | 39.4% | 695.8 | 87.6% | 92.9% | 81.2% | Merchant plus 40 MW fixed-volume swap 2023 to 2027 |
| R2 | Sandoval Hills Wind | 108 x 2.3 MW, coastal | 248.4 MW | 2017-06-30 | South | 36.1% | 785.5 | 89.2% | 94.1% | 84.0% | Physical as-generated PPA to June 2029 |
| R3 | Ollie Creek Wind | 51 x 3.0 MW, Panhandle | 153.0 MW | 2019-11-20 | West (Panhandle node) | 46.2% | 619.2 | 86.9% | 92.4% | 80.1% | Proxy revenue swap to December 2029; PTC tax equity |
| R4 | Peeler Draw Solar | Tracking PV, 131.3 MWdc | 98.7 MWac | 2020-10-09 | West | 27.1% | 234.3 | 94.6% | 96.8% | 91.9% | Fixed-shape hedge 2022 to 2026 |
| R5 | Calloway Mesa Solar | Tracking PV, 241.0 MWdc | 182.4 MWac | 2021-06-28 | West | 28.3% | 452.2 | 94.2% | 96.5% | 91.4% | Virtual PPA to June 2033; ITC tax equity |
| R6 | Redfern Storage | LFP, 2-hour | 100.0 MW / 200 MWh | 2023-07-14 | North | – | – | – | – | – | Toll to July 2030 |
| R7 | Kerrigan Storage | LFP, 2-hour | 150.0 MW / 300 MWh | 2024-04-02 | Houston | – | – | – | – | – | Merchant with revenue floor to April 2032 |
| R8 | Barlow Gap Solar | Tracking PV, 162.0 MWdc | 120.0 MWac | 2024-12-19 | South | 27.6% | 290.1 | 94.4% | 96.6% | 91.6% | Fixed-shape hedge on 60% of P50, 2025 to 2034 |

P90 and P99 columns are percentages of P50. Totals: wind 603.0 MW, solar 401.1 MWac, storage 250.0 MW / 500 MWh. Degradation: wind 0.20% a year, solar 0.45% (R8 0.40%). Battery round-trip efficiency 86.0% (R6) and 86.5% (R7), availability 97.5%, augmentation of 6% of MWh in years 5 and 9 at USD 41/kWh (2025 prices). Useful lives end 2044 (R1), 2047 (R2), 2049 (R3), 2055 (R4), 2056 (R5), 2043 (R6), 2044 (R7) and 2059 (R8). Curtailment: West wind 4.5% in 2022 rising to 6.0% from 2025; Panhandle 5.2% rising to 7.0%; coastal wind 1.5%; West solar 2.0% rising to 3.5%; South solar 1.8%.

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
| A1 | 2021-12-09 | 2022-03-22 | Mesa Corta Renewables LLC (R1 to R5, sponsor interests) | Hollenbeck Energy North America | Enterprise value USD 1,184.6 million; transaction costs USD 14.9 million; buy-side W&I limit USD 118.0 million | New opco term loan, holdco term loan, fund equity |
| A2 | 2023-06-02 | 2023-08-31 | Redfern Storage LLC (R6), at COD | Tolliver Energy Development LLC | USD 132.4 million; costs USD 2.6 million; ITC claimed by seller | Redfern term loan and fund equity |
| A3 | 2024-02-15 | R7 2024-04-02; R8 2024-12-19 | Kerrigan Storage LLC (R7) and Barlow Gap Solar LLC (R8), late construction | Tolliver Energy Development LLC | R7 USD 171.9 million; R8 USD 168.3 million (20% deposit at signing); costs USD 4.4 million; seller bears construction risk; long-stop June 30, 2025 | Holdco incremental loan, fund equity, ITC transfer proceeds |

The fund claims and sells the 30% ITC on R7 (92% eligible basis) and R8 (94% eligible basis) at USD 0.925 per USD 1 of credit; no energy community adder is assumed.

## 3.7 Debt

| Facility | Date | Terms |
|---|---|---|
| Mesa Corta OpCo term loan | 2022-03-22 | Castellan, Kaito Pacific, Sterrenberg, Penhallow (US branch); 7-year mini-perm to March 22, 2029; Term SOFR 3M + 1.625% to March 2026, then + 1.875%; upfront fee 1.50%; sized by revenue bucket at DSCR 1.30x contracted, 1.40x hedged, 2.00x merchant on P50, with P99 one-year DSCR at least 1.00x; notional amortization to 2040; sweep 50% in 2026 to 2027 and 100% from 2028; 85% hedged at 2.41% to 2029; DSRA six months by LC. Expected USD 520 million to USD 600 million |
| Mesa Corta HoldCo term loan B | 2022-03-22 | Institutional TLB arranged by Castellan; to March 22, 2028; SOFR (floor 0.50%) + 4.75%; OID 98.0; 1% a year amortization; 50% excess cash sweep; sized at distribution coverage 1.75x on P50 base and at most 45% of opco equity value. Expected USD 160 million to USD 210 million |
| Redfern term loan | 2023-08-31 | Penhallow Bank (US branch); SOFR + 2.10%; fee 1.40%; fully amortizing to June 30, 2030 on toll cash flow at 1.35x; 75% hedged at 4.38% |
| HoldCo incremental term loan | 2024-02-15 | SOFR + 4.25%; OID 99.0; maturity March 22, 2028; sized at 1.75x on incremental P50 distributions from R7 and R8 |
| Refinancing: Mesa Corta Senior Secured Notes (US private placement) | Priced 2025-10-21, funded 2025-12-16 (modeled December 31, 2025) | Issuer Mesa Corta OpCo; rated BBB- by one agency; Series A 7 years 5.71% (30%), Series B 12 years 6.08% (40%), Series C 18 years 6.39% (30%); sized at 1.35x contracted, 1.50x hedged, 2.25x merchant, P99 one-year at least 1.05x; make-whole at Treasuries + 50 bps; costs 1.10%; repays the opco term loan and the Redfern loan; opco swap unwound at 3.55% (receivable), Redfern swap at 3.55% (payable). Expected USD 750 million to USD 860 million |
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

Where he is wrong: in 2017 he dismisses convertibility risk because "the tariff is in dollars" (Chapter 59 shows why that was the wrong frame), and in 2016 he pushes the bid tariff lower than Kilnworth's pricing committee wanted. Arc: closes the deal (2018), survives the delay (he signs off the COVID variation without board approval and is reprimanded), manages the 2022 to 2023 crisis badly at first and well later, champions the 2025 bond, and in 2026 leads the partial sale he once said Kilnworth would never make.

### Mariama Talmé (local sponsor)

Kessaran, born 1977 in Dabakro. Deputy Chief Executive of Groupe Talmé (2008 to 2021), Chief Executive from 2021 when her father, the founder Ousmane Talmé (born 1946), retires to the chairmanship. MBA in Paris; six years in a Paris investment bank's Africa coverage team; returned in 2008 to run group finance.

She wants Groupe Talmé to graduate from a small diesel IPP to a serious infrastructure partner, with a board seat, reserved matters, and a share of the O&M jobs for Kessarans. She fears being treated as the partner who "handles the government," and being blamed in Dabakro if tariffs rise. She negotiates patiently, times her asks to political events she sees coming before the foreigners do, and trades economics for governance. Verbal habit: answers a proposal with "Who else has seen this?"

Where she is wrong: in 2017 she accepts a 25% stake without a tag-along right that would have let Talmé sell alongside Kilnworth, which costs her leverage in 2026. Arc: becomes the indispensable channel to ministers during the 2023 crisis and brokers the gas netting agreement with SNHK; in 2026 waives her right of first refusal over Kilnworth's stake in exchange for an additional board seat and a tag-along right.

### Pieter van Wijngaarden (lead arranger, later restructuring adviser)

Dutch, born 1966 in Rotterdam. Joined a Dutch bank in 1990; posted to Jakarta 1995 to 1999, where he worked on restructurings of dollar-tariff IPP loans after the 1997 crisis; London from 2000; Castellan Bank from 2008, Managing Director and Head of Project and Export Finance, EMEA (2014 to 2020). Leaves Castellan in late 2020 when its EMEA project finance team is cut after unrelated losses; Partner, Quarrington Advisory, from 2021.

At Castellan he wants a landmark mandate, the underwriting and hedging fees that come with it, and a clean record at credit committee. He fears underwriting a deal that will not sell down, and he never stops worrying about convertibility (Jakarta). He negotiates bluntly, anchors early, hides behind his credit committee, and trades price for structure. Verbal habit: "Fine. And the day it goes wrong?"

Where he is wrong: he insists on an 80% swap hedge with the swaps priced by his own bank, and the 7.5 bps execution charge becomes a sponsor grievance; in 2016 he tells Tomasz in 2016 that the banks will accept a final maturity in 2036, which they do not (the common profile ends on June 30, 2034). Arc: lead arranger of Case P (2017 to 2018); out of the bank in 2020; restructuring adviser to the Case T senior lenders (2022 to 2023), where he sits opposite sponsors as he once sat opposite borrowers; debt adviser to Kilnworth on the 2025 Case P bond, re-reading his own 2018 term sheet from the borrower's side.

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

Where she is wrong: in 2017 she argues for a smaller PRG (USD 30 million); the Board raises it to USD 41.5 million, and in 2023 even that is less than one quarter of the peak arrears. Arc: drives the RAP, the ESAP and the PRG on Case P; moves to Lattimer in 2021; leads diligence on Case R's A2 and A3 and the 2025 refinancing.

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
| Rafael Quintanilla | R | American | 1971 | Lattimer Infrastructure Partners |
| Carmen Villarreal-Ochoa | R | American | 1986 | Lattimer (Mesa Corta) |
| Declan Furlong | R | Irish | 1981 | Castellan Bank |
