# Case Bible Annex P: Case P terms, people, corrections and missing data

Version 1.1, October 3, 2026 (amended after the blueprint review: SEKA LC values per P-C44, the construction currency hedge per D-114, P-F64 to P-F66 registered, RAROC per R-075, the model-audit condition of credit approval, the provisional figure-ID concordance in 8.4; see `reviews/blueprint/central-fixes-log.md`). Owner: Case Bible editor, under the editor-in-chief. Binding on every writer, reviewer and modeler.

## 0. Status and rules of use

1. This annex resolves every Case P flaw raised in the unit briefs u01 to u17 (sections headed "Case Bible flaws", "bible_flaws", "BF-", "CBF-", "F-0") and in `bible/brief-feedback.md`. Section 9 maps each flaw to its resolution.
2. Precedence. Where this annex and `case-bible.md` differ, this annex governs. Every change to an existing Case Bible fact is logged in Section 10 (change log, IDs P-C16 onward, continuing the Part 8 series).
3. New numbers. Values in this annex are case assumptions (inputs). A writer may print them as given. Anything computed from them that goes beyond the simple arithmetic allowed by decision D-013 comes from the figure ledger under the IDs in Section 8. Every new numeric input the model must absorb is listed, with units, in `bible/case-p-input-requests.md`. Until the modeler confirms a request there, writers print the input but not any model output that depends on it.
4. Names. New fictional names follow `standards.md` Section 8 (no stock names, names fitting nationality and generation) and the Case Bible Part 5 checking procedure. Web checks were run on October 3, 2026 where the search budget allowed; Section 7.3 records the results.
5. Real institutions. As in D-007, real institutions (ICC, ICSID, LCIA, the OECD, the IFC Performance Standards, the Equator Principles, Lloyd's as a market) appear only as rules, forums or markets, never as running-case parties. Mauritius appears as the holding company's jurisdiction (Section 1.3.4); the treaties between Mauritius and Kessara are part of the fiction, and writers state no Mauritian domestic tax rule unless a fact sheet verifies it.
6. Model rules not decided here (operating-year mapping, tax timing, sweep order and similar, raised in u09 F-01 to F-24) are owned by the Case P modeler. Where this annex states a rule, it is because the rule is a contract term or a case fact; Section 9 shows which F-items are settled here and which are left to the model report.

---

## 1. Contract terms annex

### 1.1 Power purchase agreement (PPA)

#### 1.1.1 Term, dates and availability

| Term | Value |
|---|---|
| Signing | October 12, 2017 |
| Term | 25 years from COD |
| Expiry, FC base (COD May 1, 2021) | April 30, 2046 |
| Expiry, actual (COD December 1, 2021) | November 30, 2046 |
| Scheduled backfeed date (Interconnection Schedule) | November 1, 2020; extended day for day by the 97-day COVID force majeure to February 6, 2021 |
| SEKA substation and 225 kV line-in-line-out | SEKA's obligation under the Interconnection Schedule; actually energized January 2021, ahead of the extended backfeed date |
| Backfeed actually started | April 12, 2021 (when the plant was ready; the transformer failure followed on June 9, 2021) |
| Required Commercial Operation Date (RCOD) | July 31, 2021; extended to January 20, 2022 (Case Bible 1.9) |
| Availability target | 90.0%, measured per settlement period of six months ending June 30 and December 31; monthly invoices are provisional and trued up after each settlement period |
| Planned outages | Count as unavailability. There is no planned-outage allowance, so in hot gas path and major inspection years (OY4, OY8 and their repeats) the capacity payment falls below 100% |
| Bonus above target | None |
| SEKA's opening position (June 2017) | 92.0% target with a symmetrical bonus and malus of 1.5% of the capacity charge per point between 88% and 96% |
| Kilnworth's opening reply (July 2017) | 88.0% target, bonus above 92.0% |
| Settled (September 2017) | 90.0% target, no bonus: Tomasz traded the bonus away to hold the target at 90.0% |

#### 1.1.2 Force majeure

| Item | Political force majeure | Natural force majeure |
|---|---|---|
| Events | War, hostilities, invasion, terrorism, civil war, riot, insurrection or civil commotion within Kessara; expropriation, nationalization or requisition; nationwide or politically motivated strikes (not strikes confined to the site, the contractor or the operator); embargo or sanctions imposed by the Republic; failure or refusal of a Kessaran public authority to issue, renew or maintain a permit when the applicant has complied with the law; any event affecting SNHK or GCK that would be political force majeure if it affected the project company | Lightning, earthquake, tsunami, flood, storm, fire and explosion not caused by the affected party; epidemic and pandemic, including the government measures responding to them; strikes outside Kessara; embargoes imposed by foreign states; damage in transit outside Kessara |
| Not force majeure | Change in law (handled by the change-in-law clause, 1.1.4); lack of funds; SEKA's inability to pay; currency devaluation; events caused by a party's breach | Same |
| Before COD | RCOD extended day for day; SEKA pays "Political FM Payments" from the date the plant would otherwise have reached COD, equal to the capacity charge's capital charge component on contracted capacity (covering debt service and equity return), for the duration of the delay | RCOD extended day for day; no payment (time only) |
| After COD | Plant deemed available: full capacity payment continues | Capacity payments follow actual availability (the project company relies on business interruption insurance) |
| SEKA's network | Unavailability of SEKA's transmission system is a SEKA risk event (1.1.3), not force majeure, except that unavailability caused by natural force majeure on SEKA's network gives deemed availability only up to 240 hours a contract year | |
| Gas supply | SNHK or GCK failures of any cause give deemed availability (Case Bible 1.4 deliver-or-pay), except that natural force majeure at Sombé West or on the GCK pipeline gives deemed availability only up to 60 days a contract year; beyond that the natural force majeure rules apply | |
| Notice | Notice within five business days of becoming aware; full particulars within 15 days; monthly updates; notice of end within two business days | Same |
| Termination | Political force majeure lasting more than 180 days: either party may terminate on 30 days' notice; compensation as for SEKA default (Case Bible 1.4 table) | Natural force majeure lasting more than 180 days (continuous) or 270 days in any 365: either party may terminate on 30 days' notice; compensation as in the Case Bible 1.4 table |
| COVID-19 (2020) | Not political force majeure: the epidemic and the lockdown are natural force majeure, so the 97 days were time only, consistent with Case Bible 1.9 | |

#### 1.1.3 SEKA risk events: time and money

SEKA risk events are: (a) failure to complete the Bélanou substation and 225 kV connection by the scheduled backfeed date; (b) grid events originating in SEKA's system, including switching errors, surges and protection failures at SEKA's substation; (c) failure to take test energy or to dispatch for commissioning and completion tests as scheduled; (d) SEKA's breach of the PPA; (e) political force majeure; (f) gas supply failures by SNHK or GCK (deemed availability, 1.1.2).

Relief is time and money:

- Time. RCOD is extended day for day.
- Money before COD. SEKA reimburses the project company's reasonable, documented additional costs (prolongation, repair and re-testing costs payable to the EPC contractor, extra start-up fuel), net of insurance proceeds received or that would have been received had the insurances required by the PPA been maintained. Loss of revenue before COD is not compensated except for political force majeure (1.1.2).
- Money after COD. Deemed availability: the capacity payment continues as if the plant were available.

Application to the June 9, 2021 grid event: the expert determination of February 2022 confirmed a SEKA risk event. Time: the 173-day RCOD extension (Case Bible 1.9) includes the 76 days. Money: in March 2022 the project company claimed USD 9.27 million from SEKA (the USD 8.27 million prolongation settlement plus the USD 1.0 million EAR deductible; the insured material damage and the DSU-indemnified revenue were excluded because insurers had paid them). SEKA accepted liability in principle in May 2022 but never paid, because its arrears began the same half-year. The project company waived the claim in the March 21, 2024 settlement agreement, as part of the package that also waived 40% of late payment interest (Section 10, P-C27). The model is unchanged: the prolongation settlement and the deductible stay as project company costs in the overrun table.

#### 1.1.4 Change in law and the Kessaran Civil Code hardship article

- Change in law. Any change in Kessaran law (including tax law, OREK regulations and levies, and the interpretation of law by a Kessaran court or authority) after the bid base date of November 30, 2016 that increases or decreases the project company's costs or revenues by more than USD 0.5 million a year (aggregated over all changes in a contract year) is passed through. Exclusions: changes in dividend withholding tax (Case Bible 1.4) and changes in taxes on the shareholders or on the transfer of shares (so the 2025 indirect transfer tax is not compensable; it falls on the seller). Operating cost changes pass through the capacity charge from the next six-monthly reset. Capital expenditure above USD 2.0 million is compensated, at SEKA's choice, by a lump sum or by an adjustment to the capital charge that restores the project company's FC base equity IRR. Savings pass to SEKA symmetrically. Relief is also time where a change in law delays construction.
- Interest limitation (Finance Act 2024). A change in tax law affecting the project company; it does not bite because the loans are grandfathered (Case Bible 1.7), so no claim arises.
- Hardship. Article 1135-1 of the Kessaran Civil Code (inserted by Law No. 2011-038, Case Bible 1.1) lets a court adapt or end a contract after an unforeseeable change of circumstances that makes performance excessively onerous for a party that had not accepted the risk. The article is supplementary law, not public order, so parties may exclude it; the leading commentary and a 2016 Dabakro Court of Appeal decision (fictional) accept an express exclusion between commercial parties. The PPA (clause 34.3), the GSA and the GTA each exclude it expressly: each party "assumes the risk of a change of circumstances within the meaning of Article 1135-1 of the Civil Code" and the contracts' own change-in-law and force majeure clauses are the exclusive adjustment mechanisms. The IA and the Government Guarantee do not exclude it, because the Republic refused. The exclusion was Laurent Bécherel's August 2017 ask (Chapter 10); Hyacinthe Dossa resisted and conceded it in exchange for the USD 0.5 million change-in-law threshold, which SEKA wanted higher. In 2023 SEKA's lawyers considered a hardship petition despite the exclusion and dropped it on advice that an ICC tribunal seated in Paris would apply the exclusion.

#### 1.1.5 Payment, LC sizing and SEKA default

| Term | Value |
|---|---|
| Invoice | Monthly, by the fifth business day of the following month, in USD |
| Due date | 30 days after invoice; paid in KCR at the Central Bank mid rate on the business day before payment |
| Index reset | January 1 and July 1, using the September and March index readings respectively (a three-month lag on the month of publication). The January 2022 invoice therefore uses the September 2021 readings |
| Contracted capacity in January 2022 | 581.9 MW (reset by the November 2021 completion tests, effective at COD) |
| Reconversion rate for local shares | The Central Bank mid rate on the invoice date |
| LC amount | 2 x estimated monthly capacity charges + 1 x estimated monthly energy charges, where capacity charges use contracted capacity, the indexed capacity charge for the contract year and 100% of the capacity payment, and energy charges (fuel, VOM and GTA pass-throughs) use contracted capacity x 730 hours x 90.0% availability x the dispatch factor in SEKA's annual dispatch plan (76.5% in the FC base) at that year's gas price and indices |
| LC reset | At COD and each January 1 |
| LC delivery | No later than 60 days before scheduled taking-over; a condition to COD |
| LC issuer and confirmer | UBK, confirmed by Castellan Bank; issuance and confirmation fees borne by SEKA |
| Replenishment | Within 30 days of a drawing; failure is a SEKA event of default unless SEKA delivers within those 30 days a payment plan approved by OREK, which suspends the default for up to 90 days (Adaeze Whitcombe's concession; Case Bible 4.1) |
| SEKA payment default | Failure to pay undisputed amounts above USD 5.0 million for 60 days after the due date |
| Put option (IA) | Exercisable when a SEKA payment default has continued 90 days (after any OREK payment-plan suspension) |
| 2017 LC fight | Pieter's and Kilnworth's opening ask was three months of estimated capacity and energy charges; Hyacinthe fought it down to two plus one (Case Bible 4.1). Both formulas at COD are figure P-F39 |

LC values (P-C44): the model value governs. The two-plus-one amount was USD 36.2 million at the January 1, 2022 reset and USD 36.6 million at the January 1, 2023 reset (P-F39); the February 14, 2023 drawing is the full January 1, 2023 reset value, USD 36.6 million (P-F40). The superseded USD 33.8 million is never printed.

2023 sequence (consistent with Case Bible 1.9): LC drawn February 14, 2023 for USD 36.6 million; replenishment due March 16, 2023; SEKA delivered an OREK-approved payment plan on March 14, 2023, which suspended the default to June 12, 2023; the put option became exercisable from September 10, 2023; the lenders and sponsors chose not to exercise it, and the October 2023 waiver and the March 2024 settlement overtook it.

#### 1.1.6 Handback

| Term | Value |
|---|---|
| Transfer | At expiry, for USD 1, free of security (lenders' security released on the final discharge) |
| Handback surveys | A joint survey by an independent engineer appointed jointly by SEKA and the project company 36 months before expiry (November 30, 2043, which is also the GSA expiry date) and a second survey 12 months before expiry |
| Handback test | Within the final 12 months: corrected net output at least 90% of the last contracted capacity (90% of 581.9 MW, that is 523.7 MW); corrected net heat rate no more than 108% of the tested heat rate (108% of 6,286 kJ/kWh, that is 6,789 kJ/kWh) |
| Residual life | Gas turbines with at least 24,000 EOH remaining before the next major inspection; the steam turbine major overhaul done within the preceding eight years; HRSG pressure parts inspected and certified within the preceding four years; no major component with a remaining life of less than five years on the IE's assessment, unless replaced |
| Documentation | As-built drawings, O&M manuals, maintenance history, spare parts at the inventory level of the initial spares list, permits and the operating license transferable to SEKA |
| Remedial program | The IE sets a remedial works program after the first survey; the project company carries it out at its cost |
| Handback reserve | Funded from OY20 at USD 1.85 million a year in 2018 prices, indexed to US CPI from 2018 (the model already indexes it; this confirms the treatment), held in a Handback Reserve Account charged to SEKA and the lenders. If the first survey's cost estimate for the remedial program exceeds the reserve balance plus the remaining scheduled contributions, the project company must top up within 90 days; failing that, SEKA may withhold up to 15% of each capacity payment into the reserve until the shortfall is covered |
| Release | Unused balance released to the project company on the IE's handback certificate; if the plant fails the handback test, SEKA keeps the amount the IE certifies as the cost to cure |
| Equity tail | The handback is equity risk only: the bank debt matures in 2034 and the bond in 2037 |

#### 1.1.7 Termination payments: definitions

The Case Bible 1.4 termination table stands. Definitions the modeler needs (P-F25):

- Senior debt outstanding: principal plus accrued interest at the non-default rate on all senior tranches and the standby facility, plus scheduled swap breakage (for SEKA default and political force majeure only).
- Equity contributed: share capital subscribed plus shareholder loan principal advanced in cash, including the LNTP credited at close; excluding capitalized shareholder loan interest.
- Distributions received: dividends, shareholder loan interest and shareholder loan principal repayments, all gross of withholding tax.
- The 14.5% compounding runs from each contribution date to the termination date; the NPV of projected distributions uses the latest lenders' base case.
- Payment within 90 days of the termination date, bearing late payment interest after that.

#### 1.1.8 Other PPA terms

- No waiver of subrogation in SEKA's favor. The PPA requires the project company's insurances to waive subrogation only against the lenders, the EPC contractor and its subcontractors, the O&M operator and the LTSA provider. SEKA is not a co-insured. (This is why insurers could have pursued SEKA in 2022; see 2.9.)
- Dispatch: SEKA dispatches through the national control center; minimum stable load 45% per GT block (Case Bible JSON).
- Dispute resolution: Section 1.13.

### 1.2 Implementation Agreement (IA) and Government Guarantee

| Term | Implementation Agreement | Government Guarantee (Garantie de l'État) |
|---|---|---|
| Parties | Republic (MEH) and Bélanou Power SA | Republic (MEF) in favor of Bélanou Power SA, assigned to the lenders |
| Signed | October 12, 2017; ratified by decree No. 2017-418 of November 3, 2017 | October 12, 2017; registered with the Directorate-General of Public Debt on October 20, 2017 |
| Law | Kessaran law, with a stabilization clause | Kessaran law |
| Scope | Site rights; tax and customs incentives; convertibility and transfer undertaking (Central Bank to make FX available for debt service, O&M, the LTSA and distributions); a procurement undertaking that SNHK and GCK will perform their contracts (not a guarantee of them); put option on a 90-day SEKA payment default; local content undertaking (Case Bible 1.4) | SEKA's payment obligations under the PPA: capacity, energy and other charges, late payment interest and termination amounts |
| Nature | Contract | Independent guarantee (garantie autonome) payable on a compliant first demand, not an accessory surety |
| Ceiling | – | USD 1,250 million in aggregate over its life, within the annual ceiling for new guarantees set by Finance Act 2017 of KCR 950 billion (about USD 1.95 billion at the 2017 average rate); Bélanou used about two thirds of that year's ceiling |
| Demand | – | Allowed when an amount is unpaid 30 days after its due date; payable within 60 days of a compliant demand |
| Budget | – | Validity does not require a budget appropriation, but payment does; no appropriation line was created (Clémentine's error, Case Bible 4.1), which is why the 2023 demands were paid late |
| Immunity | Irrevocable waiver of immunity from suit, jurisdiction and arbitration, and from execution against commercial assets. Excluded from execution: diplomatic and consular premises and accounts, military assets, Central Bank reserves held for its own account, and assets of the public domain (domaine public) under Kessaran public property law | Same waiver |
| Disputes | ICSID arbitration (Section 1.13) | ICC arbitration seated in Paris, consolidated with PPA disputes where possible (Section 1.13) |
| Hardship exclusion | None (Republic refused) | None |

ICSID nationality. The IA records the parties' agreement, for Article 25(2)(b) of the ICSID Convention, that Bélanou Power SA, a Kessaran company, is to be treated as a national of another contracting state because it is controlled by Kilnworth Bélanou Holdings Ltd (Mauritius). The clause names the controlling shareholder and survives changes in shareholding so long as foreign nationals together control the company. After the 2026 sale, Kilnworth (36%) and Coldharbour (24%), both foreign, together hold 60%, so the agreement still holds; writers may note that it would have been tested had Talmé become the largest shareholder.

### 1.3 Holding structure and treaty position

#### 1.3.1 The holding company

Kilnworth Bélanou Holdings Ltd is a Mauritius company holding a global business license, incorporated August 11, 2015, wholly owned by Kilnworth Power International plc (United Kingdom). It has two Mauritius-resident directors, a local administrator and holds its board meetings in Port Louis. It holds Kilnworth's shares and shareholder loans in Bélanou Power SA.

#### 1.3.2 Treaty position (fictional, plausible)

| Instrument | Position |
|---|---|
| Kessara–Mauritius bilateral investment treaty | Signed 2004, in force 2006. Fair and equitable treatment, full protection and security, expropriation with prompt, adequate and effective compensation, free transfer of funds, an umbrella clause, consent to ICSID arbitration after six months of negotiation, a denial-of-benefits clause for companies with no substantial business activities in their home state, and a ten-year survival clause |
| Kessara–United Kingdom | No BIT in force (a treaty signed in 1999 was never ratified by Kessara). This is the reason Kilnworth invested through Mauritius |
| Timing | The holding company was incorporated in August 2015, two months after the co-development agreement and long before any dispute was foreseeable, which matters for the abuse-of-process point taught in Chapter 54 |
| Kessara–Mauritius double tax treaty | Signed 2009, in force 2011. Dividends 7.5%; interest 5% (Case Bible 1.7); capital gains on shares taxable in Kessara where the shares derive more than 50% of their value from immovable property in Kessara (Article 13(4)); immovable property takes its meaning from Kessaran law, under which the emphyteutic lease and the plant built on it are immovable |
| Multilateral instrument | Kessara is not a party, so the treaty has no principal purpose test |
| Groupe Talmé | Kessaran: no treaty protection; its remedy is Kessaran courts and the IA's local remedies |
| ABDB fund | Protected by the ABDB's own constituent agreement (immunities and privileges), not by a treaty |

#### 1.3.3 The 2026 sale and the "indirect transfer tax"

Kilnworth Bélanou Holdings sells Bélanou Power SA shares directly to Coldharbour. The Finance Act 2024 regime (Case Bible 1.1 and 1.7) taxes non-residents' gains on transfers of shares in Kessaran companies, whether held directly or through an offshore chain; the offshore-chain rule was the novelty that gave the tax its name, and the book keeps the name "indirect transfer tax". Because the treaty's Article 13(4) gives Kessara the taxing right over land-rich shares, the 15% applies to Kilnworth's gain on the direct sale. This clarifies Case Bible 1.9 (P-C29).

### 1.4 EPC contract

#### 1.4.1 Opening offer and final terms

| Term | Lindauer opening offer (September 12, 2017) | Final (December 19, 2017; Case Bible 1.4) |
|---|---|---|
| Delay LDs | USD 150,000 a day | USD 247,300 a day |
| Delay LD cap | 10% of price | 18% of price |
| Output LDs | USD 1,500 per kW | USD 2,150 per kW |
| Heat-rate LDs | USD 120,000 per kJ/kWh | USD 180,400 per kJ/kWh |
| Performance LD cap | 7.5% | 12% |
| Aggregate LD cap | 15% | 30% |
| Overall liability cap | 60% | 100% |
| Schedule | 36 months | 33 months (Abdoulaye's RFP had pushed bidders to the shortest period; Lindauer priced it) |
| Grid interface | Employer risk, with prolongation costs | Same (Employer risk: extension of time and prolongation costs) |

Gwen Treharne's 2017 view (Chapter 22). In the negotiation she gives only a preliminary view on the 33-month schedule: "Better than evens to finish on time, not much better." Her "one in eight" for a delay longer than six months belongs to the May 2018 IE report (Section 4.1).

#### 1.4.2 Interfaces

| Interface | Allocation |
|---|---|
| Grid (225 kV) | SEKA builds the substation and line under the PPA Interconnection Schedule; the EPC boundary is the high-voltage terminals of the generator step-up transformers; switching at SEKA's substation is SEKA's; a protection coordination study was a joint SEKA–contractor deliverable (Gwen's reservation R1, Section 4.1). Agreed in principle in the March 2017 risk matrix; fixed in the PPA (October 12, 2017) and the EPC contract (December 19, 2017) |
| Gas | GCK owns the lateral and metering station; the EPC boundary is the outlet flange of GCK's metering station at the site fence |
| Cooling water | Contractor designs and builds intake and outfall; the project company holds the abstraction and discharge permit (1.9) |
| Owner-supplied items | Site, access road, permits, start-up fuel, offtake of test energy (through SEKA), the LTSA provider's technical advisers during commissioning |
| Bergmark | Bergmark supplies the gas turbines to Lindauer as subcontractor (export content); the LTSA is a separate contract with the project company; an interface letter among Lindauer, Bergmark and the project company allocates defects in the gas turbines between the EPC warranty and the LTSA |

#### 1.4.3 Completion definitions

| Term | Contract | Definition |
|---|---|---|
| Mechanical completion | EPC | Each unit erected and pre-commissioned, ready for first fire |
| Taking-over | EPC | Completion tests passed at or above minimum performance levels; 720-hour reliability run at 95% availability or better; emissions and grid-code compliance; punch list below USD 3.0 million; taking-over certificate issued by the project company on the IE's confirmation. Actual: November 30, 2021 |
| COD | PPA | Taking-over plus the PPA commissioning tests witnessed by SEKA, the LC delivered, and the operating license in force. Actual: December 1, 2021 |
| Final acceptance | EPC | End of the 24-month defects liability period: November 30, 2023 |
| Project Completion | Finance documents | See 1.12 |

### 1.5 Long-term service agreement (LTSA)

| Term | Value |
|---|---|
| Signed | March 27, 2018 |
| Scope | Both gas turbines: parts, repairs and field service for combustion inspections, hot gas path inspections and major inspections; remote monitoring; not the HRSGs, steam turbine or balance of plant |
| Start | The operating term runs from COD (December 1, 2021); before COD Bergmark supplies technical advisers under the EPC subcontract |
| Term end | The earlier of (a) 128,000 EOH on each unit, the second major inspection being the last LTSA event, and (b) 16 years from COD (November 30, 2037). At base dispatch (8,059 hours plus 38 starts at 10 EOH, so 8,439 EOH a year per unit) the EOH limit comes first, early in 2037; the date by dispatch case is figure P-F48 |
| Inspection intervals | Combustion inspection at 16,000 and 48,000 EOH; hot gas path at 32,000 EOH; major inspection at 64,000 EOH; cycle repeats (80,000; 96,000; 112,000; 128,000). At base dispatch these fall in OY2, OY4, OY6 and OY8, matching the availability profile |
| Starts | 1,200 starts per interval limit, not binding at 38 starts a year |
| Liability cap | Per contract year, 100% of the fees payable for that year; aggregate cap over the term USD 40.0 million (2018 prices, US CPI) |
| Availability guarantee | Bonus or malus USD 0.2 million per point between 90% and 95% (Case Bible 1.4), capped at USD 1.0 million a year either way |
| Extension | The project company may extend for a third 64,000-EOH cycle at prices to be agreed. The 2025 bond indenture requires a replacement or extended LTSA by December 31, 2035 |
| Model assumption | The model carries LTSA fees at the same prices after expiry (a successor LTSA on equal terms). This is a stated simplification |
| Law and disputes | Section 1.13 |

### 1.6 O&M agreement

| Term | Value |
|---|---|
| Signed | April 30, 2018, with Kilnworth Operations Services Ltd |
| Pre-operation services | From 15 months before scheduled taking-over (February 2020 base; September 2020 actual) to COD: recruitment, training, procedures, spares; fee USD 2.90 million in total, inside the owner's cost line "project company staff and administration" |
| Operating period | Ten years from COD: December 1, 2021 to November 30, 2031 |
| Renewal | Automatic for successive five-year terms unless the project company gives 12 months' notice; the operator may decline renewal on 24 months' notice |
| Fees | Case Bible 1.4 (fixed fee and availability incentive) |
| Liability cap | 100% of the annual fixed fee per contract year; aggregate over the term two times the annual fixed fee; no cap for gross negligence, willful misconduct or fraud |
| Replacement triggers (project company, with Majority Lender consent; or the lenders directly under the direct agreement) | Availability below 85.0% in two consecutive settlement years for reasons within the operator's control; material breach not cured within 60 days; operator insolvency; Kilnworth ceasing to hold at least 25% of Bélanou Power SA, unless the project company and the lenders confirm the operator in writing within 90 days |
| 2026 | The sale leaves Kilnworth at 36%, so the 25% trigger is not hit; Coldharbour accepted Kilnworth Operations as operator in the share purchase agreement |

### 1.7 Gas sale agreement (GSA)

#### 1.7.1 Term: a deliberate misalignment

| Term | Value |
|---|---|
| Signed | November 30, 2017 |
| Commissioning gas | From March 2021, interruptible, at the GSA price, outside take-or-pay |
| Commencement date | COD (December 1, 2021 actual; May 1, 2021 in the FC base) |
| Term | 22 contract years from commencement: to November 30, 2043 actual (April 30, 2043 in the FC base) |
| PPA expiry | November 30, 2046 actual: the GSA ends three years earlier |
| Extension | Buyer's option, by notice by November 30, 2040, to extend for up to three years on the same terms, subject to SNHK certifying available reserves; SNHK's obligation is reasonable endeavours only |
| PPA treatment of the gap | If, despite the project company's reasonable endeavours, no gas supply on substantially equivalent terms is in place from the GSA's expiry, SEKA must nominate a gas source and the fuel charge passes through its price. If no gas is available, the plant is deemed available for capacity payments for up to 12 months, after which either party may terminate with natural force majeure compensation |

Why the gap exists. SNHK would not commit beyond what the 2017 reserves certification supported for Bélanou's 22 years plus SEKA's existing demand; Halbeck would not dedicate reserves beyond its own development plan. The lenders accepted the gap because the bank debt matures in 2034 (and, later, the bond in 2037): the gap is an equity and handback risk, and SEKA bears the fuel risk after 2043 only weakly (12 months of deemed availability). The gap is the reason for MEH's 2026 FSRU study (Chapter 76) and is a planned storyline element in Chapters 28 (gap scan) and 65 (handback planning). The GTA's term is coterminous with the GSA (1.8).

#### 1.7.2 Specification and heating value

| Item | Value |
|---|---|
| Expected gross calorific value | 38.75 MJ/Sm3 (about 1,040 Btu/scf); DCQ of 72,400 MMBtu a day is about 69.6 MMscfd |
| Permitted GCV range | 37.5 to 41.5 MJ/Sm3 |
| Wobbe index | 47.0 to 52.0 MJ/Sm3 |
| Methane | At least 85 mol% |
| Inerts | CO2 plus N2 no more than 5 mol% |
| H2S | No more than 5 mg/Sm3; total sulfur no more than 30 mg/Sm3 |
| Water dew point | No more than 0 °C at delivery pressure |
| Hydrocarbon dew point | No more than 0 °C at delivery pressure |
| Delivery pressure | 35 to 50 barg at the outlet of GCK's metering station |
| Off-spec gas | Buyer may reject; rejected quantities count as seller shortfall (deliver-or-pay and deemed availability) |
| Measurement | GCV basis (Case Bible 1.4); disputes to an independent measurement expert |

#### 1.7.3 Other GSA terms

| Term | Value |
|---|---|
| Force majeure | As PPA natural force majeure, plus damage to Sombé West facilities and the offshore pipeline from natural causes. Reservoir underperformance and reserves depletion are not force majeure. During seller force majeure the take-or-pay quantity falls pro rata |
| Seller credit | SNHK gives no credit support and the Republic does not guarantee SNHK; the IA procurement undertaking (1.2) is the only sovereign support. SNHK dedicates its aggregator entitlement from Sombé West to the GSA ahead of new sales |
| Buyer credit support | Standby LC from UBK equal to one month of DCQ at the GSA price (about USD 13 million in 2022), fee 1.0% a year, cost inside project company G&A (no model change) |
| Change in law | Taxes on gas sales (including any VAT on gas) pass to the buyer and through the PPA's change-in-law clause; changes in royalties or upstream taxes stay with the seller |
| Payment | 30 days after month end, in KCR (Case Bible 1.4); the 2023 tripartite netting overrides payment for the netted amounts |
| Hardship | Article 1135-1 excluded (1.1.4) |
| Law | Kessaran law |
| Disputes | ICC arbitration seated in Paris, with joinder and consolidation with PPA and GTA "fuel disputes" (1.13) |

#### 1.7.4 Sombé West reserves coverage inputs

- Certified 2P reserves 1,140 bcf (2017) at 1,040 Btu/scf.
- Bélanou GSA: 72,400 MMBtu a day for 22 years.
- SEKA's existing gas supply agreement for its open-cycle fleet: 38,000 MMBtu a day from 2019 to 2038 (20 years).
- Reserve coverage (2P over contracted quantities) is figure P-F61; the design target is about 1.35x to 1.40x.

### 1.8 Gas transportation agreement (GTA)

| Term | Value |
|---|---|
| Signed | November 30, 2017 |
| Term | Coterminous with the GSA, including any extension: to November 30, 2043 actual |
| Capacity and charges | Case Bible 1.4 |
| Pipeline unavailability | Deemed availability under the PPA (SEKA risk), subject to the 60-day natural force majeure limit (1.1.2) |
| Payment | Monthly in KCR, 30 days after invoice |
| Law and disputes | Kessaran law; ICC Paris with joinder; measurement disputes to an expert |
| GCK's pipeline and its financing | The 112 km pipeline was sanctioned in 2016, built 2017 to 2019 and commissioned with Sombé West's first production in 2019. Capex USD 410 million, financed 40% by SNHK equity and 60% by a USD 246 million 12-year loan from a group of regional banks with UBK, guaranteed by SNHK and secured on the assignment of GCK's ship-or-pay GTAs with Bélanou Power and SEKA. The 2015 "landfall" in Case Bible 1.1 is the landfall designated in Halbeck's 2014 field development plan (P-C30) |

### 1.9 Permits and licenses

| Permit | Holder | Issued | Term | Key conditions |
|---|---|---|---|---|
| Environmental compliance certificate (Certificat de conformité environnementale) | Bélanou Power SA | September 14, 2017, after approval of the ESIA | Life of the project, subject to five-yearly environmental audits | ESMP and RAP implementation; NOx no more than 50 mg/Nm3 at 15% O2 at full load on gas; noise at the site boundary no more than 70 dB(A) day and 60 dB(A) night; annual monitoring report |
| Seawater abstraction and discharge authorization | Bélanou Power SA | March 6, 2018 | To November 30, 2046 (renewable), extended on the COD shift | Abstraction no more than 18.5 m3/s; discharge temperature no more than 7 °C above ambient at the outfall and no more than 3 °C at the edge of a 100 m mixing zone; residual chlorine no more than 0.2 mg/l; intake velocity no more than 0.15 m/s with a fish return system; quarterly monitoring |
| Generation license (OREK) | Bélanou Power SA | November 22, 2017 (No. OREK/GEN/2017-031) | 30 years (to November 2047) | Transfer of the license requires OREK approval; a change in the controlling shareholder (any person acquiring more than 50%) requires OREK consent; changes above 10% require notification only. The 2026 sale needed notification, not consent |
| Interconnection (PPA schedule) | SEKA's obligation | – | – | Backfeed date and remedy as in 1.1.1 and 1.1.3 |
| Construction and building permits | Bélanou Power SA | 2018 | Construction period | Standard |
| Exchange Control Authorization No. 2018-114 | Bélanou Power SA | July 12, 2018 | Life of the senior debt | Offshore USD accounts at Castellan Bank London; daily conversion and sweep subject to FX availability |

### 1.10 Direct agreements

| Counterparty | Lenders' notice | Additional cure period | Step-in | Novation |
|---|---|---|---|---|
| SEKA (PPA) | SEKA must notify the Intercreditor Agent of any project company default and intended termination | Payment default: 30 days. Other defaults: 90 days, extendable to 180 days while the lenders diligently pursue a cure | Up to 12 months, extendable by 6 months; SEKA's liability to the step-in entity limited to amounts accruing during step-in | To a substitute entity meeting the criteria below; SEKA's consent not unreasonably withheld and deemed given after 30 days |
| Republic (IA) | Same | Same as SEKA | Same | Same; the Republic consents in advance to the assignment of the put option proceeds |
| SNHK (GSA), GCK (GTA) | Same | 60 days | 9 months | Same criteria |
| Lindauer (EPC), Bergmark (LTSA), Kilnworth Operations (O&M) | Same | 30 days (payment), 60 days (other) | 6 months | To the substitute or to the lenders' nominee |

Substitute entity criteria: has operated (directly or through a qualified O&M contractor) at least 1,000 MW of combined-cycle capacity for five years; tangible net worth of at least USD 250 million or a rating of BBB- or better, or equivalent credit support; not a sanctioned person; not in dispute with the Republic; acceptable under the ABDB's integrity policy.

### 1.11 Insurance program and political risk insurance

#### 1.11.1 Construction and operational covers

| Item | Value |
|---|---|
| Binding | Construction program bound July 13, 2018; EAR and DSU attach at notice to proceed (August 1, 2018); marine cargo and marine DSU from first shipment |
| Insurers | AGK fronts and retains 5%; 95% reinsured with a panel led by a European reinsurer rated AA- and including Lloyd's syndicates, all rated A- or better (unnamed in the book) |
| Waiver of subrogation | In favor of the lenders, the EPC contractor and its subcontractors, Bergmark and the O&M operator; not SEKA (1.1.8) |
| DSU trigger | Physical loss or damage to insured property (including the project's own step-up transformers) that delays taking-over. Loss caused purely by failure of a public utility supply without damage to insured property is excluded; the June 2021 event was covered because the surge damaged the project's transformer |
| EAR defects | LEG 2 equivalent defects wording (consequences of defective design or workmanship covered, the defective part itself not) |
| Operations | Case Bible 1.4, plus contingent business interruption for physical damage at SEKA's Bélanou substation, sublimit USD 50.0 million, 30-day deductible |
| Hard market | 18.0% step-up from H2 2022 (Case Bible 1.4) |

#### 1.11.2 Political risk insurance (PRI)

| Term | Value |
|---|---|
| Insured | The commercial tranche lenders, through the Intercreditor Agent as loss payee; Hovland Bank (insurance bank) coordinates |
| Insurers | A panel of five private-market insurers (three Lloyd's syndicates and two company-market insurers), all rated A- or better, led by a Lloyd's syndicate; unnamed in the book |
| Bound | July 13, 2018 (a CP to first drawing); inception July 17, 2018 |
| Policy period | To June 30, 2034, the commercial tranche's final maturity: slightly more than 15 years, at the outer edge of private-market tenor in 2018, which explains the tenor loading in the 1.15% premium and the five-insurer panel |
| Insured amount | 90% of scheduled principal and interest on the commercial tranche (Case Bible 1.4); the insured retains 10% |
| Premium | 1.15% a year on the insured amount, paid semiannually in advance by the project company; the model applies it to 90% of the commercial tranche balance (u09 F-12 confirmed) |
| Perils | Expropriation; currency inconvertibility and transfer restriction; political violence (damage and resulting loss of debt service); non-honoring of the Government Guarantee (a sovereign financial obligation) |
| Waiting periods | Non-honoring: 180 days from the date the guarantee payment was due (that is, 60 days after a compliant demand). Inconvertibility and transfer: 180 days of continuous inability to convert or transfer through legal channels after a compliant application. Expropriation: 365 days. Political violence: none for damage; 90 days for the resulting debt service loss |
| Claim conditions | A compliant demand under the Government Guarantee (for non-honoring); the project company applied for FX through legal channels (for inconvertibility); the LC drawn where available; the insureds' reasonable steps to avoid loss; subrogation to insurers on payment |
| Exclusions | Currency devaluation; non-discriminatory measures of general application taken in good faith (bona fide regulation, including taxes); losses caused by the insured's or the project company's breach or illegality; delay in conversion caused by the project company's lack of KCR or failure to apply; SEKA arrears that were never demanded under the Government Guarantee; war among the five permanent members of the UN Security Council; nuclear risks |
| Notification of circumstances | Within 30 days of becoming aware. The lenders notified insurers on February 20, 2023 (LC drawing and FX queue) and again on April 24, 2023 (first guarantee demand) |
| 2023 decision not to claim | No peril matured: the guarantee demands were paid 99 and 141 days after demand and the third was folded into the settlement 164 days after demand, all before the non-honoring waiting period could end; the FX queue's average conversion lag was 47 days and the longest single lag 112 days, never 180 continuous days. Devaluation losses were excluded |
| Cancellation | Cancelled with effect from June 30, 2025, when the bond prepaid the commercial tranche; premium had been paid to that date, so no return premium arose |

### 1.12 Lenders' completion test and sponsor support

Project Completion (common terms agreement) requires the IE's certificate that all of the following are met:

1. Taking-over under the EPC contract and COD under the PPA have occurred.
2. Completion tests passed at or above the minimum performance levels; performance LDs paid by the contractor and applied as required.
3. The 720-hour reliability run achieved at least 95% availability.
4. All permits for operation in force; the operating license issued.
5. The DSRA fully funded; the MMRA schedule in place.
6. The insurance program for operations in force.
7. ESAP construction-phase actions complete, confirmed by the ABDB and Exportgarant E&S reviews.
8. Projected minimum DSCR of at least 1.30x on the updated lenders' base case after the COD re-sculpting.
9. No default continuing; punch list items below USD 3.0 million and covered by retention.
10. The first scheduled repayment made.

Long-stop date: July 31, 2022 (original RCOD plus 12 months, extended for force majeure and SEKA risk events); failure is an event of default.

Actual: Gwen certified taking-over on November 30, 2021 with a reservation on HRSG tube supports (cracked tube support welds found in HRSG2's pre-taking-over inspection). Lindauer replaced the supports under the defects liability obligation during a planned outage from April 4 to 19, 2022; Gwen withdrew the reservation on May 6, 2022. Performance LDs were received from Lindauer in January 2022, held in the Compensation Account and applied on June 30, 2022. Project Completion was certified on June 30, 2022, after the first repayment.

Sponsor support released at Project Completion: the undrawn balance of the contingent equity commitment (USD 15.4 million less any amount drawn in the overrun funding, P-F18) and the LCs backing it; the undrawn standby facility commitment, cancelled; the equity LCs for base equity, which had been fully drawn by COD; Lindauer's performance bond stepped down from 10% to a 5% warranty bond to final acceptance (November 30, 2023). Distributions remained subject to the Case Bible 1.6 tests (and in practice were trapped by the 2022 to 2024 crisis).

### 1.13 Dispute clauses of every contract

| Contract | Governing law | Forum | Technical or expert route | Notes |
|---|---|---|---|---|
| PPA | Kessaran | ICC arbitration, Paris seat, three arbitrators, French and English | Expert determination for availability, tests, grid events and indexation (expert appointed by agreement or, failing agreement within 15 days, by the ICC International Centre for ADR) | Multi-contract consolidation and joinder with the GSA, GTA and Government Guarantee |
| IA | Kessaran, with stabilization | ICSID Convention arbitration; venue Paris; English | Same expert route | ICSID nationality agreement (1.2) |
| Government Guarantee | Kessaran | ICC, Paris | – | Consolidation with PPA disputes |
| GSA, GTA | Kessaran | ICC, Paris | Measurement and quality expert | Joinder with PPA "fuel disputes" |
| EPC | English | ICC arbitration, London seat | Three-member dispute adjudication board, standing from notice to proceed | Bati-Kessara bound as consortium member |
| LTSA | English | LCIA arbitration, London | Technical expert for fleet and parts disputes | – |
| O&M | English | LCIA, London | Technical expert | – |
| Co-development agreement and shareholders' agreement | English | LCIA, London | – | Shares are Kessaran; transfer formalities under Kessaran law |
| Common terms, facility agreements, intercreditor, accounts, offshore security, hedging (ISDA) | English | LCIA, London, with lenders' option to sue in the English courts (Case Bible 1.6) | – | – |
| Onshore security | Kessaran | Dabakro Commercial Court (Tribunal de Commerce) for enforcement | – | – |
| Direct agreements | Follow the underlying contract (SEKA and Republic: Kessaran law, ICC or ICSID; others English law) | – | – | – |
| Construction and operational insurance | Kessaran (AGK policies); English (reinsurance) | Kessaran courts; London arbitration for reinsurance | – | Cut-through and assignment of reinsurance |
| PRI | English | London arbitration | – | – |

### 1.14 Shareholder governance and equity

#### 1.14.1 Co-development agreement (June 22, 2015)

- Phase 1 (to September 30, 2015): Kilnworth funds up to USD 1.5 million from its business development budget under delegated authority; Talmé contributes site access work, local permitting and community relations in kind.
- Phase 2: conditional on Kilnworth's investment committee approving the full development budget by September 30, 2015 (approved September 17, 2015; USD 14.8 million). From Phase 2, costs are shared 70:30 by cash calls payable within 15 business days; Talmé's in-kind contribution is credited at up to USD 0.9 million.
- Default on a cash call: after 30 days the defaulter's share is diluted at 1.5 times the amount funded by the other party.
- Exclusivity: neither party pursues another gas-fired IPP in Kessara without the other until December 31, 2018.
- Reimbursement: development costs (USD 21.43 million) reimbursed at financial close to each party in proportion to the amounts it funded, with Talmé's in-kind credit counted.
- Superseded by the shareholders' agreement at financial close.

This resolves the dating issue raised by u01: the June agreement was signed under delegated authority and was conditional on the September approval.

#### 1.14.2 Development fee and the ABDB fund's entry

| Item | Kilnworth | Talmé | Total |
|---|---|---|---|
| Development fee at close (USD m) | 7.84 | 3.36 | 11.20 (70:30) |
| Stake sold to the ABDB fund (percentage points) | 10 | 5 | 15 |
| Development premium received (USD m) | 3.2333 | 1.6167 | 4.85 (two thirds and one third, in line with the points sold) |

The ABDB fund did not buy strictly pro rata to the pre-close 70:30 stakes, which would have left 59.5% and 25.5%; Talmé insisted on selling a slightly larger share of its holding to fund its equity commitment. This corrects Case Bible 1.5 (P-C24).

#### 1.14.3 Shareholders' agreement (signed July 17, 2018)

| Term | Value |
|---|---|
| Board at close | Six directors: Kilnworth 4 (including the chair), Groupe Talmé 1, ABDB fund 1. Board decisions by simple majority; quorum includes one Kilnworth director and, for meetings on E&S or integrity matters, the ABDB fund's director |
| Board after September 30, 2026 | Seven directors: Kilnworth 2 (the chair continues to be a Kilnworth nominee, without casting vote), Coldharbour 2, Groupe Talmé 2 (the additional seat of Case Bible 4.1), ABDB fund 1 |
| Budget, dispatch strategy, O&M oversight, hiring of senior managers | Board simple majority (not reserved): these are the relevant activities, so Kilnworth controlled them with four of six seats until 2026 and no one controls them after |
| Shareholder reserved matters (80% of shares; Talmé therefore holds a veto, the ABDB fund alone does not) | Amendment of the articles; change of business; issue of shares or instruments convertible into shares; mergers, liquidation or insolvency filings; disposal of assets above 10% of total assets; new financial debt beyond the finance documents' permitted baskets; termination or material amendment of the PPA, IA, GSA, GTA, EPC contract or LTSA; related-party transactions above USD 1.0 million (the interested shareholder does not vote; this covers the O&M agreement with Kilnworth Operations); change of auditor; dividend policy outside the finance documents |
| ABDB fund's individual consent rights | Changes to the E&S management system and the ESAP; anti-corruption, sanctions and integrity policies; any transaction with a person on the ABDB's debarment list |
| Classification | All reserved matters are protective rights; Kilnworth consolidates from 2018 and, after 2026, holds an associate (significant influence, no joint control) |
| Transfers | Lock-in: no transfers except to affiliates until two years after COD (December 1, 2023). Then right of first refusal: other shareholders pro rata, 30-day offer period, 90-day completion window at no lower price and on no better terms |
| Tag-along | None for Talmé at close (Mariama's error, Case Bible 4.1); granted in 2026 |
| ABDB fund exit | Put option to Kilnworth at fair value on an integrity or sanctions event affecting another shareholder; no tag-along |
| Deadlock on reserved matters | Escalation to chief executives (30 days), then non-binding mediation (30 days), then status quo; no buy-sell clause (the lenders' transfer restrictions make one unworkable) |
| Law and disputes | English law; LCIA (1.13) |

#### 1.14.4 Equity contribution agreement and LCs

- Parties: the three sponsors, the project company and the Intercreditor Agent; signed July 17, 2018.
- LC support: Kilnworth's and Talmé's undrawn base and contingent equity commitments are backed by LCs from banks rated A- or better (Talmé's by UBK, confirmed by Kaito Pacific Bank). The ABDB fund posts no LC: its commitment is backed by a commitment letter from the ABDB, rated AAA. LC fees are borne by each sponsor, not by the project company.
- Acceleration: on an event of default before Project Completion, the Intercreditor Agent may require all undrawn base and contingent equity to be paid within ten business days, and may draw the LCs. Also if an LC bank's rating falls below A- and the LC is not replaced within 30 days.
- Release: 1.12.

### 1.15 Finance documents

#### 1.15.1 Financing strategy, underwriting and holds

- Castellan's June 19, 2017 mandate was an underwritten mandate: Castellan committed to underwrite 100% of the commercial tranche and of the ECA-covered tranche, with a target final hold of 30% of the commercial tranche.
- Senior syndication (January to March 2018): Castellan sold down to three co-mandated lead arrangers. Hovland took 18% instead of the 22% Castellan had planned, so Castellan's final hold in the commercial tranche is 34% (Case Bible 1.6): Pieter's fear of a deal that would not fully sell down came partly true. There was no general syndication.
- ECA-covered tranche holds: Castellan 40%, Kaito Pacific 30%, Banque Raveau 30%.
- B-loan: the ABDB, as lender of record, placed participations with Kaito Pacific (55%) and Sterrenberg (45%) from March to May 2018.
- Standby facility: commercial banks' 60% share held pro rata to commercial-tranche shares; the ABDB 40%.
- Standby facility margins: each participant earns its own tranche's margin plus 0.25% (commercial banks: the commercial-tranche margin schedule plus 0.25%; the ABDB: the A-loan margin plus 0.25%). This resolves u07's ambiguity; the model already applies it.
- Swap: the four commercial banks pro rata (Case Bible 1.6); Castellan's swap credit line was approved with the loan.

#### 1.15.2 Castellan's July 2017 draft term sheet and the concession sequence

| Item | Castellan draft (July 14, 2017) | Concession and date | Agreed term sheet |
|---|---|---|---|
| Base-case DSCR | 1.45x | 1.40x (August 2017); 1.35x once the termination formula was settled (October 2017) | 1.35x |
| Gearing | 70% | 75% (October 2017) | 75% |
| Hedge ratio | 90% fixed, minimum 85% | 80%, band 75% to 90% (September 2017) | 80% |
| Lock-up / default | 1.25x / 1.15x | 1.20x / 1.10x (September 2017) | 1.20x / 1.10x |
| Final maturity | 2032 | 2034 (October 2017); Tomasz had expected 2036 on Pieter's 2016 remark | June 30, 2034 |
| PRI premium | For the project company's account | Unchanged (Kilnworth wanted the banks to bear it and lost) | Project company |
| Swap credit and execution charge | 10 bps | 7.5 bps (September 2017) | 7.5 bps |

The term sheet was agreed on October 27, 2017, after PPA signing on October 12, 2017. Its PV cost is P-F50.

#### 1.15.3 Conditions precedent to first drawing and their fate

| CP | Fate |
|---|---|
| Executed project documents and direct agreements | Satisfied |
| Executed finance documents, security documents, hedging strategy letter | Satisfied |
| Exportgarant insurance policy | Issued July 16, 2018; satisfied |
| ABDB Board approval of the A-loan and B-loan | February 21, 2018; satisfied |
| ABDB Board approval of the PRG (USD 41.5 million) | June 20, 2018; satisfied |
| Castellan credit committee approval | May 22, 2018, with the conditions of a PRG of at least USD 40 million and a satisfactory model audit report from Ferrand Model Assurance (2.5) |
| OREK approval of the PPA tariff for pass-through | January 15, 2018; satisfied |
| OREK generation license | Satisfied (1.9) |
| Exchange Control Authorization No. 2018-114 | July 12, 2018; satisfied |
| IA ratification decree; Government Guarantee registration | Satisfied (1.2) |
| Registration of the emphyteutic lease | Satisfied |
| Registration of the mortgage over the emphyteutic lease | Not completed at close: converted to a condition subsequent (within 90 days); registered October 9, 2018 |
| Registration of the share pledge and business pledge | Business pledge registered July 16, 2018; share pledge entered in the share register at close |
| Legal opinions (English law; Kessaran capacity, enforceability and security, including a reasoned parallel debt opinion) | Satisfied; the parallel debt opinion is qualified as untested in Kessaran insolvency |
| IE report and bring-down letter | Report May 30, 2018; bring-down July 13, 2018 |
| Model audit (Ferrand Model Assurance) | Report June 28, 2018; satisfied |
| Insurance broker's letter of undertaking; PRI bound | July 13, 2018 |
| Equity LCs and equity contribution agreement; evidence of the LNTP equity credit | Satisfied |
| ESAP and RAP: compensation paid to all physically displaced site households | Satisfied for the site; compensation to pipeline corridor households 81% paid: waived as a CP and converted to a condition subsequent (all paid before the contractor entered the corridor, by February 2019) |
| Protection coordination study for the grid interface (Gwen's reservation R1) | Converted to a condition subsequent: due before backfeed; delivered August 2020 |
| Withholding tax exemption certificates for the ECA-covered tranche and ABDB loans | Converted to a condition subsequent (120 days); issued November 5, 2018 |
| KYC on all sponsors and the project company | Satisfied (2.4) |
| Fees and costs paid; process agent appointments | Satisfied at close |

#### 1.15.4 Change of control (common terms agreement, 2018)

- Before Project Completion: Kilnworth (through Kilnworth Bélanou Holdings) holds at least 51% and controls the project company; Talmé holds at least 20%; transfers only to affiliates.
- After Project Completion and until June 30, 2030: Kilnworth holds at least 30% and remains the largest or equal-largest shareholder, and Kilnworth or an affiliate remains the O&M operator.
- Any transfer to a non-affiliate needs Majority Lender consent unless the transferee is a "Qualifying Transferee" (tangible net worth of at least USD 500 million, experience owning thermal plants of at least 1,000 MW, not sanctioned). Coldharbour, an income fund without operating experience, was not one, hence the 2026 consent.
- The 2025 bond indenture and the amended intercreditor agreement carried the same clause; the "30% until 2030" of Case Bible 1.9 is this 2018 clause, not a new 2026 requirement.

#### 1.15.5 Permitted financial debt

| Basket | Limit |
|---|---|
| Senior facilities and the standby facility | As committed |
| Hedging under the hedging strategy | Interest rate swaps within the 75% to 90% band; KCR forwards covering at least 75% of committed KCR construction payments, traded at close with Castellan (D-114, Case Bible 1.6; P-F65), matured by August 2021; no other FX or commodity hedging without consent |
| VAT facility (UBK) | KCR 7,900.0 million, repaid from VAT refunds |
| Working capital facility (UBK, KCR or USD) | USD 15.0 million equivalent; undrawn through 2025 |
| LC facility for GSA buyer credit support | USD 15.0 million equivalent |
| Subordinated shareholder loans | Unlimited, subject to the subordination deed |
| Finance leases and vehicles | USD 2.0 million |
| General basket | USD 5.0 million |
| 2025 | The bond replaces the prepaid tranches; baskets otherwise unchanged |

#### 1.15.6 Priority of payments

Onshore: SEKA pays into the KCR Collection Account; budgeted KCR operating costs move to the KCR Operating Account; the rest is converted and swept daily to the offshore USD Proceeds Account when the Central Bank makes FX available. VAT refunds repay the VAT facility directly onshore.

Offshore, from the USD Proceeds Account, on each payment date:

1. Taxes, operating and maintenance costs per the approved budget (gas, GTA, O&M, LTSA, insurance premiums, G&A, levies, PRG fee).
2. Agency, account bank and trustee fees.
3. Senior interest, commitment fees, net scheduled swap payments, the PRI premium and the withholding tax gross-up, pari passu.
4. Senior scheduled principal (and from 2025 bond principal), pari passu.
5. DSRA top-up to the required balance.
6. MMRA contribution.
7. Handback Reserve Account contribution (from OY20).
8. Mandatory prepayments: the soft mini-perm sweep (from January 1, 2027, 50% of cash otherwise distributable to the commercial tranche) and the cash sweep after two consecutive lock-ups.
9. Swap termination payments owed to a defaulting hedge counterparty (subordinated).
10. Lock-up Account, if the distribution conditions fail.
11. Distribution Account: shareholder loan interest, then shareholder loan principal, then dividends.

Model note: the model treats the MMRA inside CFADS and the PRI premium with interest; the legal order above does not change the model's cash flows.

#### 1.15.7 Insurance proceeds and the Compensation Account

- Material damage proceeds below USD 5.0 million per event: paid to the project company for reinstatement.
- USD 5.0 million to USD 25.0 million: Insurance Proceeds Account, released against IE-certified reinstatement costs (the 2021 EAR payment of USD 5.84 million followed this route).
- Above USD 25.0 million: reinstatement only if the IE confirms it is technically and economically feasible and the projected DSCR after reinstatement is at least 1.20x; otherwise mandatory prepayment.
- DSU and business interruption proceeds: to the USD Proceeds Account as revenue (inside CFADS).
- Compensation Account receives termination and expropriation compensation, performance LDs (applied 100% to prepayment), delay LDs during construction (applied to overrun funding), change-in-law lump sums and SEKA risk event payments; releases need Intercreditor Agent consent.

#### 1.15.8 Intercreditor voting and ECA and DFI rights

| Item | Rule |
|---|---|
| Voting groups | ECA-covered lenders (votes directed by Exportgarant); the ABDB (votes the A-loan and the whole B-loan as lender of record, after consulting B-participants; B-participants decide alone on their own economic terms); commercial lenders; standby lenders vote with their tranche; hedge counterparties vote only on crystallized close-out amounts and on enforcement |
| Majority Lenders | More than 50% of senior commitments, then outstandings |
| Super-Majority Lenders | 66 2/3%: release of material security, changes to the hedging strategy, approval of a replacement O&M operator |
| All Lenders | Principal, interest, fees, dates of payment, margin reductions, maturity, pro rata sharing, the priority of payments, the definitions of Majority and All Lenders, release of all or substantially all security |
| Exportgarant's individual rights | Consent to any amendment affecting the covered tranche or the policy conditions, any waiver of an event of default that is also a policy event, E&S (Category A) and anti-bribery matters |
| ABDB's individual rights | ESAP and E&S, sanctions and prohibited practices, preferred creditor matters, the ABDB's own policy compliance |
| Standstill | After an event of default (other than payment default, which allows acceleration 30 days after notice), Majority Lenders may accelerate only after a 90-day standstill (180 days where the default results from a political event) |
| 2025 accession | The bond trustee accedes and votes the bond as one group, on instruction of bondholders under the indenture; the ECA and A-loan lenders consented to the bond's maturity beyond 2034 (Laurent restructures the intercreditor agreement; Chapter 53) |

#### 1.15.9 FX queue priority for the ABDB

During the Central Bank's allocation queue (November 7, 2022 to March 29, 2024), the Central Bank converted, outside the queue and within five business days, the KCR needed for debt service on the A-loan and the B-loan (the ABDB being lender of record), on presentation of the ABDB's payment notice: preferred creditor treatment in practice. Debt service on the ECA-covered and commercial tranches, operating costs and distributions waited in the queue. The 47-day average conversion lag in Case Bible 1.9 is the blended figure for all conversions; no model change.

#### 1.15.10 Operating budget and information covenants

- Annual operating budget for each calendar year delivered to the Intercreditor Agent and the IE by October 31. Majority Lenders may object within 30 days only on grounds of inconsistency with prudent utility practice, the base case or the finance documents; otherwise deemed approved.
- Default budget if not approved: the prior year's budget indexed by the PPA's US and Kessaran CPI split.
- Permitted variance: 10% on total operating costs and 15% on any line, plus emergency spending.
- Reporting: quarterly operating reports within 45 days of quarter end; a semiannual compliance certificate with historic and projected DSCR and LLCR within 30 days of each June 30 and December 31 test date (so the June 30, 2023 breach was certified on July 28, 2023); unaudited semiannual financial statements within 60 days; audited annual financial statements within 120 days; an updated lenders' base case with each compliance certificate; an annual E&S monitoring report to the ABDB and Exportgarant; an annual insurance report; prompt notice of any default, claim above USD 1.0 million, or force majeure.

#### 1.15.11 The 2023 waiver: why not an equity cure, and the votes

- Why not a cure. An equity cure (by shareholder loan, twice over the life, not in consecutive periods) was available for June 30, 2023. The sponsors did not use it because: (a) one cure could fix only one test, and the December 31, 2023 test was certain to fail too, when a second cure would be consecutive and therefore barred; (b) the shortfall came from SEKA's arrears, which a cure did not touch, so cured cash would have been locked up and exposed to the same sovereign; (c) Groupe Talmé, whose KCR businesses were hit by the devaluation, could not fund its pro rata share, and the ABDB fund's investment committee would not fund without a waiver in place; (d) Kilnworth's investment committee refused to send new dollars into a country with an FX queue. The cure amount the sponsors would have needed is figure P-F63.
- Votes. The waiver of the event of default needed Majority Lenders. The margin uplift, the fee and the deferral of 60% of the December 31, 2023 principal changed payment terms and therefore needed All Lenders, plus Exportgarant's consent under its policy, the B-participants' consent to their own terms, and the hedge counterparties' consent to the amended priority of payments (arrears recoveries to the DSRA first). Exportgarant consented last, on October 24, 2023 (Henrike Vosskamp, Case Bible 4.1). Laurent insisted on a reservation of rights.

#### 1.15.12 The 2023 business pledge re-notification

In April 2023 a Dabakro heavy-lift transport firm, holding a disputed USD 0.4 million invoice against Bélanou Power, obtained a provisional garnishment order (saisie conservatoire) over amounts owed by SEKA to Bélanou Power. UBK, as onshore security agent, opposed it on the strength of the business pledge. On May 9, 2023 the registrar of the Dabakro Commercial Court ruled that the pledge over future PPA receivables, though valid between the parties, was not opposable to SEKA as debtor without formal notification (signification) to SEKA. UBK had the pledge notified to SEKA by bailiff on May 23, 2023; SEKA acknowledged on June 8, 2023; the garnishment was lifted when the invoice was settled in July 2023. No receivable was lost. This is Laurent's 2018 error (Case Bible 4.1) and the Chapter 52 fix.

---

## 2. People and scenes

### 2.1 New and extended characters

| Name | Nationality | Born | Role | Chapters |
|---|---|---|---|---|
| Philippa Carrow | British | 1962 | Chief Executive, Kilnworth Power International (2011 to 2022); chairs the investment committee | 2, 47, 87 |
| Devesh Raval | British (of Indian Gujarati descent) | 1968 | CFO, Kilnworth (2013 to 2022); Chief Executive from 2022 | 2, 8, 47, 62, 63, 76 |
| Niall Brannigan | Irish | 1960 | Chief Operating Officer, Kilnworth (2009 to 2021); investment committee member | 2, 24 |
| Imogen Thwaite | British | 1976 | CFO, Kilnworth, from 2022; chairs the 2023 investment committee that refuses the equity cure | 62, 66 |
| Joanna Sedley | British | 1978 | Group Financial Controller, Kilnworth (from 2014); owns the consolidation and the 2026 deconsolidation | 7, 66 |
| Kunal Mehrotra | British (born in Pune, India; moved to London 2006) | 1989 | Kilnworth project finance analyst (2014), associate (2017), vice president (2022); builds the bid and FC models | 7, 8, 43, 47 |
| Gareth Lloyd-Pryce | British (Welsh) | 1965 | General Counsel and Head of Compliance, Kilnworth | 87 |
| Edwige Akakpo-Sodji | Kessaran | 1981 | CFO, Bélanou Power SA, from 2018; prepares the 2022 accounts and the compliance certificates | 7, 59, 62 |
| Gilles Tchibozo | Kessaran | 1975 | Plant Manager, Kilnworth Operations Services at Bélanou, from 2020 | 61, 65, 84 |
| Adwoa Sarpong-Kumi | Ghanaian | 1984 | ABDB Principal Investment Officer, Infrastructure Finance, on Case P from July 2021 (succeeding Thandeka); Lead Investment Officer from 2024 | 53, 59, 62, 63 |
| Gaspard Amoussou-Tevi | Togolese | 1971 | Investment Director, the ABDB's equity arm; the ABDB fund's director on the Bélanou board from 2018 | 26, 32, 62, 63 |
| Clive Ormesher | British | 1959 | Chief Credit Officer EMEA, Castellan Bank; chairs the credit committee | 86 |
| Sylvestre Ahouansou | Kessaran | 1966 | Minister of Energy and Hydrocarbons from October 16, 2023 | 59 (end), 74, 76, 78 |
| Théophile Kpoviessi | Kessaran | 1970 | Secretary-General, MEH, from February 2021 (succeeding Abdoulaye) | 61, 72 |
| Rosine Gbaguidi-Ayi | Kessaran | 1975 | CFO of SEKA from June 2024 (succeeding Hyacinthe Dossa) | 63, 65 |
| Arnaud Sossa-Gbénou | Kessaran | 1982 | Head of the PPP Unit from 2020 (succeeding Clémentine) | 19 (mention) |
| Prosper Adikpéto | Kessaran | 1979 | Shift supervisor, SEKA national control center | 72 |

Sheets for the characters with scenes:

- Philippa Carrow. Former utility engineer turned chief executive. Wants a growing contracted portfolio without a write-off on her watch. Verbal habit: "What would make us walk away?" Where wrong: in September 2015 she asks for a development budget of USD 12 million and Tomasz talks her up to USD 14.8 million, still too little (P-F01).
- Devesh Raval. Chartered accountant; rated BBB- balance sheet is his to protect. Wants non-recourse debt and a clean deconsolidation path. Verbal habit: "Show me the downside first." Where wrong: in 2016 he backs the pricing committee's higher tariff, which would probably have lost the bid (Section 4.7). Arc: CEO who signs the 2026 sale.
- Imogen Thwaite. Former bank credit officer. Verbal habit: "Whose dollars, and when do they come back?" Where wrong: in 2023 she argues against the waiver fee as "paying lenders for SEKA's sins" and is overruled.
- Joanna Sedley. Verbal habit: "Which standard, which paragraph?" Appears only as a narration anchor in Chapters 7 and 66.
- Kunal Mehrotra. Quiet and exact; the modeler of the bid. Verbal habit: none (he answers questions with spreadsheets). Where wrong: his September 2016 bid model omits the VAT facility interest.
- Edwige Akakpo-Sodji. Trained in Dabakro and Lyon; ex-audit. Wants on-time reporting and fears a qualified audit opinion on the SEKA receivable. Verbal habit: "The auditors will ask."
- Adwoa Sarpong-Kumi. Economist, Accra and London; joined the ABDB in 2012 from a Ghanaian development bank. Wants the ABDB's preferred creditor position and E&S record intact. Verbal habit: "Let me take it to the Board." Where wrong: in 2025 she prices the bond's partial credit guarantee fee (1.10%) below what her credit department wanted and is asked to justify it.
- Clive Ormesher. Forty years in credit; has never lent in Kessara. Wants a deal he can defend if the country goes wrong. Verbal habit: "Where does the dollar come from, and who has to say yes?" Where wrong: he treats the ABDB PRG as protection against convertibility, which it is not (it backs Castellan's LC reimbursement claim on the Republic). His approval condition (a PRG of at least USD 40 million) leads ABDB management to take USD 41.5 million to its Board.
- Sylvestre Ahouansou. Former head of the rural electrification agency; technocrat appointed after the protests. Wants affordable tariffs and new capacity without new dollar contracts. Verbal habit: "What does the household pay?" Where wrong: in 2025 he signs the small modular reactor memorandum before MEF has counted the contingent liabilities (Chapter 74).

Other minor characters (roles and names only, no sheets): Théophile Kpoviessi, Rosine Gbaguidi-Ayi, Arnaud Sossa-Gbénou, Prosper Adikpéto, Gaspard Amoussou-Tevi (verbal habit: "Our fund has a life of twelve years, not twenty-five"), Gilles Tchibozo, Niall Brannigan, Gareth Lloyd-Pryce.

Approvals of brief proposals: Mariama Talmé may join Tomasz in Chapter 11's 2016 scene; Tomasz may join Félix Adandé in Chapter 75; Chapter 72 uses Prosper Adikpéto; Chapter 76's investment committee question is asked by Devesh Raval; Gwen Treharne may appear for two lines in Chapter 84 (as lenders' IE on Case R's 2025 refinancing).

### 2.2 Storyline row amendments (Case Bible Part 6)

| Ch | Amendment |
|---|---|
| 1 | Tomasz takes Mariama's call in London on Thursday, April 2, 2015; the meeting in Dabakro is April 14, 2015 |
| 2 | Investment committee September 17, 2015; members Philippa Carrow (chair), Devesh Raval, Niall Brannigan, Tomasz presenting |
| 4 | Development advisers named (2.3); the co-development agreement's conditional structure (1.14.1) |
| 7 | Characters: Tomasz, Edwige Akakpo-Sodji, Joanna Sedley. Accounts on the lenders' reporting basis (5.1) |
| 8 | Characters: Tomasz, Kunal Mehrotra, Devesh Raval. Premise: even 80% gearing leaves the FC base equity IRR below the 16.0% bid-model target (P-F05; bridge P-F64); the argument is over downside for about 0.5 points (P-C46) |
| 15 | Gwen attends in the capacity of Castellan's pre-mandate technical reviewer (P-C18) |
| 16 | Figures shown: "Inputs at financial close: LC formula (the amount under the 1.1.5 formula, P-F39, printed with its reset date: USD 36.2 million at the 2022 reset), Government Guarantee cap 1,250, PRG 41.5 (Board approval June 20, 2018; Thandeka proposes 30 in May 2017), PRI 90% at 1.15%, contingency 38.40, contingent equity 15.4, standby 46.0" (P-C17) |
| 18 | SEKA's opening availability position 92.0% with bonus and malus (1.1.1); figures add P-F39, P-F47 |
| 21 | Figures add P-F46 |
| 24 | P-F11 shows the MMRA part only (P-F11b); add P-F48 |
| 26 | Board composition and reserved matters per 1.14.3; add Gaspard Amoussou-Tevi |
| 28 | Gap scan includes the GSA–PPA term gap (1.7.1) and the absence of a subrogation waiver for SEKA (1.1.8); the grid-surge trace uses an assumed 120-day delay and an assumed USD 7.5 million transformer loss, computed by the writer under D-013 at the Case Bible daily rates and deductibles (hypothetical, labeled so) |
| 34 | State at end: "PRG proposed at USD 30 million (ABDB management, November 2017); Board approves USD 41.5 million on June 20, 2018" |
| 35 | Add P-F16 (breakevens) and P-F41 |
| 36 | Add P-F36 |
| 47 | Add Devesh Raval; figures P-F06 extended (4.7) |
| 48 | Add P-F61; IE report content per 4.1 |
| 53 | Characters: Pieter, Henrike, Laurent (2018 and 2025), Thandeka (2018 only), Adwoa Sarpong-Kumi (2025) (P-C19) |
| 55 | Add P-F49 |
| 56 | Add P-F50 |
| 60 | Add P-F51 |
| 61 | Add P-F52; Théophile Kpoviessi |
| 62 | Add Adwoa Sarpong-Kumi, Imogen Thwaite, Edwige Akakpo-Sodji; add P-F63 |
| 63 | Add Adwoa Sarpong-Kumi, Gaspard Amoussou-Tevi |
| 66 | Add Joanna Sedley; P-F53, P-F56 |
| 67 | Add P-F37, P-F38, P-F54 |
| 68 | Add P-F55 |
| 69 | Add P-F57 |
| 72 | Characters: Abdoulaye (as minister, 2022), Prosper Adikpéto; add P-F58 |
| 74 | MEH's minister in 2025 is Sylvestre Ahouansou (may appear) |
| 75 | Add Tomasz; P-F46, P-F59 |
| 84 | Add Gwen (two lines) |
| 85 | Add P-F60 |
| 86 | Add Clive Ormesher; P-F28 per 8.3, P-F55 |
| 87 | The 2016 intermediary approach per 2.6 |

### 2.3 Case P development-phase advisers

| Adviser | Role | Period |
|---|---|---|
| Pemberton Hale LLP (Adaeze Whitcombe) | Sponsors' international counsel | From 2015 |
| Cabinet Adjovi-Lokossou | Sponsors' Kessaran counsel | From 2015 |
| Pennock Mayhew Engineers | Sponsors' technical adviser at bid stage; owner's engineer during construction (the USD 9.86 million owner's engineer line) | From November 2015 |
| Whinmoor Environmental | ESIA and RAP lead consultant | From March 2016 |
| Lagune Environnement SARL | Kessaran E&S sub-consultant (baseline surveys, consultation) | From March 2016 |
| Financial adviser | None: Kilnworth ran the bid and financing in house; Castellan acted as arranger only from June 2017 | – |
| Tax adviser | A London accounting firm's tax practice, unnamed | 2015 to 2018 |
| Lenders' Kessaran counsel | Cabinet Aïdasso & Associés, working with Ashworth Quayle | From 2017 |
| Lenders' E&S adviser | Calder Hartmann Engineering's E&S team, within the IE engagement | From 2017 |

### 2.4 Groupe Talmé: KYC facts (Chapter 49)

- Ownership chain: Groupe Talmé SA (Dabakro) is 100% owned by Société Financière Talmé SA, a family holding company owned by Ousmane Talmé (40%), Mariama Talmé (20%), her brothers Kwami and Séverin Talmé (15% each) and the Fondation Talmé (10%, a registered charity for vocational training). Groupe Talmé holds its Bélanou shares through Talmé Énergie SA (100%).
- Politically exposed persons: Ousmane's brother-in-law, Daniel Fiogbé, was a member of the National Assembly from 2012 to 2017 and sat on its energy committee; the Talmés are therefore PEP-associated. Enhanced due diligence found no role for him in the tender and no payments to him from the group; the ABDB's integrity review (2017) and the lenders' KYC (2018) were clean.
- The 1990s diesel IPP: Talmé Énergie's 48 MW diesel plant at Dabakro port, PPA with SEKA from 1997 to 2015. A 2009 tariff dispute over fuel indexation went to Kessaran arbitration and was settled in 2010 with a revised formula; SEKA paid arrears over 18 months. The plant was retired when its PPA expired in 2015.
- Regulatory history: a 2011 customs penalty on the cement business's clinker imports (KCR 290 million, settled without criminal proceedings). No sanctions hits; no adverse media beyond the 2011 matter.
- Source of funds for Talmé's equity: cement dividends and a KCR 12.0 billion UBK loan secured on the cement plant.

### 2.5 Castellan's credit committee (Chapter 86)

Castellan's credit committee met on May 22, 2018, chaired by Clive Ormesher. It approved the underwriting and final holds (1.15.1), the swap line and the KCR forward line (D-114), with two conditions: an ABDB PRG of at least USD 40 million behind the LC confirmation (ABDB management's proposal then stood at USD 30 million, Thandeka's figure), and a satisfactory model audit report from Ferrand Model Assurance (delivered June 28, 2018; 1.15.3), because the committee met before the model audit was complete. The committee did not seek to reopen the signed PPA's LC formula. ABDB management took a USD 41.5 million proposal to its Board, which approved it on June 20, 2018. Castellan's regulatory and RAROC inputs are in 5.6 (RAROC is the canonical term, R-075; RORAC is not used).

### 2.6 The 2016 intermediary approach (Chapter 87)

- Date and place: the evening of Thursday, July 21, 2016, in a hotel lounge in Dabakro, during the RFP period (RFP May 16, bids September 27).
- Who: a Kessaran man presenting himself as a "consultant close to the evaluation committee" approached Tomasz, whom he had met once at an industry reception. The intermediary is never named.
- Offer: to "make sure the bid is properly understood" by the evaluators, for a success fee of 1.5% of the project cost, payable at financial close through a consultancy registered outside Kessara.
- Response: Tomasz declined on the spot and reported it the next morning to Gareth Lloyd-Pryce (General Counsel and Head of Compliance). Kilnworth notified the PPP Unit by email on July 22 and by hand-delivered letter on July 25, 2016, within the RFP's 72-hour integrity reporting window.
- The PPP Unit: Clémentine Agbo-Lawson logged the report, referred it to the national anti-corruption authority, and reminded all bidders of the RFP's integrity clause without naming anyone. No link to the evaluation committee was found; no prosecution followed; the tender was unaffected.
- Friction: Kilnworth wrote to the PPP Unit before telling Groupe Talmé; Mariama learned of it from Clémentine's circular ("Who else has seen this?").
- Consequence: the report and the PPP Unit's acknowledgment appear in the ABDB's 2017 integrity due diligence and the lenders' 2018 KYC as positive findings.

### 2.7 Other people facts

- Abdoulaye Ndao-Sylla became Minister of Energy and Hydrocarbons in February 2021 (cabinet reshuffle after the December 2020 legislative elections) and was removed on October 16, 2023.
- Pieter van Wijngaarden: Case Bible 4.1 typo "he tells Tomasz in 2016 that the banks will accept... in 2016" is corrected to a single "in 2016" (P-C21).
- Thandeka Mabuza: the PRG statement is corrected (3.1).
- Callum Petrie (Case T) "last scene" wording is a Case T item, forwarded (Section 9.3).

### 2.8 Subrogation against SEKA (Chapter 61)

After the February 2022 expert determination confirmed that the transformer failure originated at SEKA's substation, the reinsurers asked AGK to pursue a subrogated claim against SEKA for the USD 5.84 million EAR payment and the USD 7.0804 million DSU payment. Under Kessaran law the subrogated action had to be brought in AGK's name. In March 2022 the minister, Abdoulaye Ndao-Sylla, told AGK's chairman that a claim by a Kessaran insurer against the state utility, months after the utility had begun paying late, was "not in the national interest"; AGK, which insures SEKA's own fleet and most state property, declined to lend its name. The reinsurers judged that Kessaran litigation against SEKA, with uncertain enforcement, was not worth the cost and closed the file in May 2022. No waiver of subrogation in SEKA's favor existed (1.1.8).

---

## 3. Corrections

### 3.1 Thandeka's PRG statement

Case Bible 4.1 says that in 2023 the USD 41.5 million PRG was "less than one quarter of the peak arrears". Peak overdue receivables were USD 112.6 million net of the LC drawing (June 30, 2023), or USD 149.2 million gross of the USD 36.6 million drawing (P-F40; P-C44); USD 41.5 million is about 37% and 28% of those. Corrected text: "in 2023 even that covers only about a third of the June 2023 peak arrears net of the LC drawing (less than 30% of the gross arrears)." (P-C16)

### 3.2 Chapter 16 row (May 2017)

Amended per 2.2 (P-C17).

### 3.3 Gwen's IE engagement

Calder Hartmann was engaged by Castellan in February 2017 for a pre-mandate technical review of the winning bid's design, at Castellan's cost and as part of Castellan's pursuit of the mandate; the engagement rolled into the lenders' IE engagement after the June 19, 2017 mandate. Gwen's March 2017 appearance (Chapter 15) is in that capacity (P-C18).

### 3.4 Tomasz's convertibility error

His "the tariff is in dollars" dismissal of convertibility first appears in risk register v1 (October 2016, Chapter 14) and recurs in 2017 (Chapter 59's frame). Case Bible 4.1's "in 2017" becomes "from October 2016" (P-C20).

### 3.5 Co-development agreement against budget approval

Resolved by 1.14.1 (P-C22).

### 3.6 ECA first repayment test

Case Bible 1.6 lists "first repayment within six months of COD". Under the OECD Arrangement's project finance terms in force for 2018 commitments (fact sheet `t-oecd-pf-2018`), the first principal repayment is due no later than 24 months after the starting point of credit, with at least 2% repaid by then; the six-month rule belongs to standard (non-project-finance) terms. Corrected: "first repayment within 24 months of COD, with at least 2% of principal repaid by then". The 14-year term, 7.25-year weighted average life and 25% per six-month limits stand as Exportgarant's 2018 cover terms under the Arrangement then in force (the 2018 fallback to 10 years and 5.25 years applied only to high-income OECD countries, which Kessara is not). Both the FC base (first repayment eight months after COD) and the actual case comply (P-C23).

### 3.7 Downside dispatch

Case Bible 1.2 lists a "downside" dispatch of 58.0%. The FC downside sizing case (Case Bible 1.10; model scenario 3) uses base dispatch with lower availability, a higher heat rate and higher fixed opex; it does not use 58.0%. The 58.0% value is the low-dispatch case for gas volumes and take-or-pay (P-F35) only. Relabeled "low dispatch (gas analysis)" (P-C25).

### 3.8 ABDB fund entry: not strictly pro rata

Resolved by 1.14.2 (P-C24).

### 3.9 Index reading for resets

Case Bible 1.4 says indices reset "using values lagged three months"; the JSON says "September and March readings". The September (for January 1) and March (for July 1) readings govern. A brief that cites "October 2021 values" for the January 2022 reset is corrected to September 2021 (P-C26).

### 3.10 Chapter 34 end state

The PRG was approved by the ABDB Board on June 20, 2018, not in 2017 (2.2, 2.5) (P-C28).

### 3.11 Indirect transfer tax on a direct sale

Clarified by 1.3.3 (P-C29).

### 3.12 Pipeline "landfall" in 2015

Clarified by 1.8 (P-C30).

### 3.13 Other checks made, no change needed

- Guarantee demand-to-payment days (99, 141; 164 to the settlement) and the FX queue duration (508 days) check against Case Bible dates. Printing them needs P-F40 or D-013 arithmetic.
- The LC sizing formula gives USD 36.2 million at the 2022 reset and USD 36.6 million at the 2023 reset (P-F39); the February 2023 drawing is the 2023 value (P-F40, P-C44).
- The PRG fee is charged for the whole PPA term in the model; the annex confirms a PRG term matching the PPA (4.9).
- The LTSA inspection intervals match the availability profile (1.5).

---

## 4. Missing data

### 4.1 The IE report (May 30, 2018; Chapter 48)

| Topic | Gwen's finding |
|---|---|
| Technology | Bergmark BT-9F: mature; 41 units in commercial operation in 2018, fleet leader about 62,000 EOH; no serial defect open |
| Schedule | 33 months "achievable but tight"; critical path through steam turbine erection and HRSG pressure parts, with 38 days of float. Probability of a delay longer than three months: one in four; longer than six months: one in eight |
| Contingency | USD 38.40 million judged adequate at about the 75th percentile of her risk-based estimate; she recommends the standby facility and contingent equity as the layer above it |
| Availability | Profile reasonable; peak years (93.8%) at the upper end of fleet experience; she would bank a point lower |
| Heat rate | 1.0% headroom between the PPA's 6,323 and the EPC's 6,261 kJ/kWh is reasonable at COD, but the plant's assumed degradation (0.12% a year plus 0.8% recoverable) outruns the PPA's 0.10% a year allowance, so the fuel margin narrows and may turn negative in the later years of the PPA |
| O&M | Fixed fee and staffing reasonable; the localization schedule (71 Kessarans by OY3) ambitious |
| LTSA and major maintenance | LTSA scope covers gas turbines only; out-of-LTSA overhauls and the MMRA adequate |
| Reservation R1: grid interface | SEKA's substation contract was awarded only in June 2018 and no protection coordination study existed; she recommends a joint study before backfeed and agreed switching procedures (the study was delivered in August 2020; the 2021 failure came from a switching error, the procedural gap the study did not close) |
| Reservation R2: civil works quality | Soft marine clays; piling design acceptable; recommends enhanced QA on concrete from local suppliers (foreshadows the 2019 foundation failure) |
| Reservation R3: gas supply | Sombé West first production not yet achieved; first gas for commissioning depends on Halbeck's 2019 schedule |
| Reservation R4: cooling water | The discharge limit of 7 °C is tight in the hottest months; seawater warming of about 0.2 °C a decade would erode output |
| Reservation R5: permits | The mortgage registration and the corridor RAP payments are open |
| Flood | Platform at +6.0 m adequate (4.12) |

### 4.2 Lenders' legal due diligence findings (Laurent's report, June 2018; Chapter 49)

| # | Finding | Rating |
|---|---|---|
| 1 | Parallel debt untested in Kessaran insolvency; opinion qualified | Amber |
| 2 | Business pledge registered; covers future receivables; advised (wrongly, as 2023 showed) that no notice to SEKA was needed for the pledge to bind SEKA | Green as given |
| 3 | Emphyteutic lease registered; mortgage registration outstanding (condition subsequent) | Amber |
| 4 | Government Guarantee valid within the Finance Act 2017 ceiling and registered; payment requires a budget appropriation that does not exist | Amber |
| 5 | IA stabilization clause enforceable as a contract but cannot bind Parliament; damages only | Amber |
| 6 | Immunity waiver valid; execution against public domain assets barred | Green |
| 7 | Exchange Control Authorization to be issued before close | Green (issued) |
| 8 | PPA LC replenishment default can be suspended by an OREK-approved payment plan, delaying the put option by up to 90 days | Amber (flagged; accepted commercially) |
| 9 | Hardship exclusion (Article 1135-1) valid between commercial parties but untested at the Supreme Court | Amber |
| 10 | Withholding tax exemptions depend on Investment Code certificates (condition subsequent) | Amber |
| 11 | RAP corridor compensation incomplete | Amber |
| 12 | Bélanou Power SA validly incorporated (February 2017); articles amended to reflect the shareholders' agreement | Green |
| 13 | Local fronting requirement for insurance; cut-through clause enforceable under Kessaran insurance law as a contractual undertaking | Amber |
| 14 | New York Convention (1998) and ICSID membership; awards enforceable | Green |
| 15 | KYC: Talmé PEP association; enhanced due diligence clean | Green |

### 4.3 E&S: ESAP, resettlement, grievance, habitat, Equator Principles

ESAP (agreed March 2018, monitored by the ABDB and Exportgarant):

1. Implement the RAP and pay all compensation before land entry; independent completion audit (done September 2020).
2. Livelihood restoration program for economically displaced households for three years after displacement.
3. Stakeholder engagement plan and a project-level grievance mechanism with an independent member.
4. Labor management: worker accommodation standards, contractor labor audits, retrenchment plan at the end of construction.
5. Occupational health and safety plan for construction and operations, including marine works.
6. Community health and safety: traffic management on the access road; emergency response with Bélanou village.
7. Biodiversity action plan: turtle-sensitive lighting, a construction exclusion on the beach from June to October (nesting season), mangrove offset planting of 12 hectares.
8. Thermal plume and marine monitoring (quarterly) against the discharge permit.
9. Air quality and noise monitoring.
10. Cultural heritage chance-finds procedure.
11. Security personnel: voluntary principles-style assessment and training.
12. E&S monitoring reports annually to the lenders.

Resettlement of 214 households:

| Location | Physically displaced | Economically displaced only | Total |
|---|---|---|---|
| Plant site (62 ha) | 58 | 0 | 58 |
| Pipeline lateral, access road and corridor | 19 | 137 | 156 |
| Total | 77 | 137 | 214 |

The 2021 grievance. In March 2021 a fishers' cooperative from Bélanou lagoon complained, first through the project grievance mechanism and then to the ABDB's independent accountability mechanism, that the intake and outfall exclusion zone and the jetty had cut 96 fishing households off from inshore grounds, and that the RAP had excluded them because they held no land. The review (May to August 2021) upheld the complaint in part. The additional USD 3.27 million (Case Bible 1.9) paid for a livelihood program for the 96 households: boats and engines, a new landing site with cold storage, and cash compensation for 18 months. These households are additional to the 214.

Indigenous peoples and habitat. The ESIA found no indigenous peoples within the meaning of Performance Standard 7. Habitat: the site is modified habitat with patches of natural habitat (lagoon mangroves); olive ridley turtles nest at low density on the beach east of the site. The critical habitat assessment concluded the area is natural, not critical, habitat; the biodiversity action plan applies.

Equator Principles. Castellan, Banque Raveau, Kaito Pacific, Hovland and Sterrenberg are Equator Principles financial institutions; the deal closed under EP III (2013), with Kessara a non-designated country, so the IFC Performance Standards applied. Exportgarant applied the OECD Common Approaches (2016 revision) and classified the project Category A.

### 4.4 Physical climate data for the site (Chapter 84)

| Item | Value |
|---|---|
| Natural ground level | +4.5 m above mean sea level |
| Finished platform level | +6.0 m |
| Design coastal flood | 1-in-100-year still water plus surge +3.1 m; design basis adds 0.5 m sea-level rise allowance and wave run-up, protected by a 650 m rock revetment |
| Design seawater intake temperature | 29 °C |
| Observed trend | Intake temperature rising about 0.2 °C a decade (2016 to 2025 measurements) |
| Output correction for cooling water | About -0.9 MW per °C above 29 °C (steam cycle) |
| Heat-rate correction for cooling water | About +0.08% per °C above 29 °C |
| Ambient air correction | Gas turbine output about -0.6% per °C above the 30 °C reference |
| Extreme heat days | Days above 35 °C: about 12 a year (2016 to 2025 average) |

### 4.5 Kessara macro and policy rates

Central Bank policy rate, year end (%): 2016 14.5; 2017 14.0; 2019 13.5; 2020 13.5 (held through the pandemic to defend the cauri). With Case Bible 1.1 this completes the series 2015 to 2026.

KCR term lending in 2017: UBK and two other banks could lend KCR for at most seven years, at the policy rate plus 3.00% (about 17%), in amounts up to about KCR 30 billion per borrower; no local pension fund or insurer could buy a long-dated project bond under its investment rules. A KCR tranche of Bélanou's size and tenor was not available (Chapter 34).

SEKA revenue: KCR 742 billion in 2015 (about USD 1.77 billion) and KCR 818 billion in 2016 (about USD 1.81 billion). SEKA's IPP capacity payments in 2016: about USD 64 million a year (one 120 MW HFO IPP; Talmé's diesel IPP had expired in 2015).

### 4.6 Accounting framework (Chapters 7 and 66)

- Bélanou Power SA prepares IFRS financial statements in USD (functional currency USD: the tariff, the debt and most costs are USD or USD-indexed) for its lenders and for Kilnworth's group reporting. Kessaran statutory accounts in KCR under the national chart of accounts are a separate filing and never shown.
- PPA treatment under IFRS: IFRIC 12, financial asset model. SEKA is a public-sector entity that buys all the output at a contract price (IFRIC 12 AG2; fact sheet `t-accounting-2`) and takes the plant at expiry for USD 1, so both control conditions are met; the capacity charge's capital component, backed by the Government Guarantee, gives an unconditional contractual right to cash. The fixed O&M charge, VOM and fuel charges are service revenue under IFRS 15.
- Lenders' reporting basis: the common terms agreement requires covenant calculations and the semiannual management accounts on a "fixed asset model": plant as property, plant and equipment at cost (including capitalized IDC, fees, the ECA premium, the development fee and capitalized shareholder loan interest), depreciated straight line to nil over the PPA term, with revenue as billed. This is what the reference model produces (P-F04, P-F45). Lenders neutralize the accounting choice, as real bond deeds do.
- Chapter 7 prints P-F04 as Bélanou Power's 2022 accounts "on the lenders' reporting basis" and says in one sentence that the IFRS accounts present the PPA as a financial asset (Chapter 66). Chapter 66 uses P-F56 for the IFRIC 12 presentation and the reconciliation.
- Deferred tax on the holiday's deferred depreciation: measured at 30% in the model (a stated simplification; IAS 12 would use the rate expected when the difference reverses).
- Kilnworth Power International plc: UK-listed, IFRS as adopted in the UK (EU-adopted IFRS before 2021), December 31 year end, consolidated revenue about USD 2.4 billion in 2018 and USD 3.1 billion in 2024, rated BBB- (one agency). Consolidates Bélanou from 2018 to September 30, 2026; then equity method (associate).
- Groupe Talmé: Kessaran statutory accounts only; equity-accounts Talmé Énergie's 25%. Unrated.
- ABDB Infrastructure Equity Fund: IFRS investment entity, fair value through profit or loss. The ABDB is rated AAA.
- Coldharbour Infrastructure Income Fund: investment entity at fair value.

### 4.7 Bid stage (Chapters 47 and 85)

- Kilnworth's September 2016 bid-stage cost estimate: USD 655 million before financing costs (about 92% of the eventual FC budget; the difference is the owner's cost, resettlement and contingency growth in diligence).
- Pricing committee (September 19, 2016; Devesh Raval presenting): recommended a capital charge of USD 15.05/kW-month, which Kilnworth's bid model put at a 17.6% equity IRR. Tomasz argued for USD 14.36/kW-month after intelligence that a Gulf-based bidder would bid aggressively; the investment committee accepted 14.36 at a bid-model equity IRR of 16.0% (the Case Bible's bid target). These IRRs are Kilnworth's 2016 bid-model values, printed as such; the reference model's FC base IRR (P-F16) is a different number on different assumptions.
- Other bids' levelized tariffs relative to the winner: runner-up (a Middle Eastern IPP developer with an Asian EPC contractor) +4.6%; third (a European utility with a Kessaran partner) +9.8%; fourth (an Asian trading house consortium) +13.1%. The fifth prequalified consortium did not bid.
- 2016 indicative pricing (Castellan, July 2016; P-F03): 6M USD LIBOR about 0.95% (approximate, fact-check before printing); indicative margins commercial 4.50%, ECA-covered 1.50%, A-loan 3.90%, B-loan 3.75%; upfront fees commercial 2.50%, ECA arrangement 1.25%, ECA premium indicated at about 11.5% of principal; fees annualized straight line over an indicative 7.0-year average life.
- Pieter's September 2016 one-hour screen (Chapter 85): uses the bid-stage cost of USD 655 million, the bid tariff at 588.4 MW, a 1.35x DSCR, 75% gearing, a 13-year repayment and the SEKA revenue in 4.5 (P-F60).

### 4.8 The 2024 solar CfD proposal (Chapter 19)

MEH's proposal (mid-2024) for Kessara's first solar auction: 150 MW of solar PV in three 50 MW lots; a 20-year two-sided CfD with SEKA as counterparty; the strike to be bid in KCR and indexed to Kessaran CPI (MEF's public debt team's preference, to avoid another dollar liability) against MEH's preference for a USD strike to attract foreign bidders; reference price SEKA's monthly average avoided thermal generation cost as published by OREK; settlement monthly through an escrow funded by a levy on retail tariffs; no Government Guarantee. MEF's indicative ceiling for the strike: the KCR equivalent of about USD 55/MWh. The auction is not held before 2026; no award figures exist.

### 4.9 PRG details and the donor facility (Chapter 34)

- Unsubsidized PRG fee: 1.50% a year; the donor facility pays 0.75% a year, so the project company pays 0.75% (Case Bible 1.4).
- Donor facility: the Coastal Power Access Trust Fund, a multi-donor trust fund administered by the ABDB, which funds fee subsidies from a capitalized grant.
- PRG term: to PPA expiry, matching the LC confirmation the PRG backs, with the subsidy for the full term; the model already charges the fee for the PPA term.
- PRG process: ABDB management proposal USD 30 million (November 2017, Thandeka); raised to USD 41.5 million after Castellan's credit committee condition (2.5); Board approval June 20, 2018.

### 4.10 The 2024 rating pre-assessment (Chapter 30)

In September 2024 (sovereign then CCC+), Kilnworth obtained a confidential rating evaluation from one agency. Unenhanced, the bond would be capped at the sovereign (CCC+); with an ABDB partial credit guarantee of about USD 95 million the agency indicated B, and B+ if the sovereign were upgraded to B-. The sovereign was upgraded in November 2024; the bond was rated B+ at pricing in June 2025 (Case Bible 1.9). Only the ratings are printed.

### 4.11 The 2022 drought (Chapter 72)

The Moraba cascade's 2022 output fell to about 55% of its average. SEKA dispatched Bélanou harder: actual dispatch factor when available 84.0% in 2022 H1 and 81.5% in 2022 H2 (base 76.5%), returning to 76.5% from 2023. Higher dispatch raised SEKA's fuel bill in KCR in the very half-years its arrears began. Capacity payments were unaffected. Model request: 6 in the input requests file; figure P-F58.

The Moraba Falls project (MEH, planned): 240 MW run-of-river with seasonal storage, estimated cost USD 720 million, studies only.

### 4.12 Kessara 2015 technology screening (Chapter 69)

MEH planning assumptions, 2015 USD (Illustrative):

| Technology | Overnight cost (USD/kW) | Net heat rate (kJ/kWh LHV) | Fuel price | Fixed O&M (USD/kW-year) | Variable O&M (USD/MWh) | Life (years) |
|---|---|---|---|---|---|---|
| OCGT (E-class, 2 x 150 MW) | 650 | 10,300 | Gas USD 5.50/MMBtu GCV | 14 | 4.0 | 25 |
| CCGT (F-class 2x1) | 1,050 | 6,350 | Gas USD 5.50/MMBtu GCV | 22 | 3.5 | 25 |
| Imported coal (2 x 300 MW subcritical) | 2,100 | 9,700 | Coal USD 75/t CIF at 25.1 GJ/t | 45 | 4.5 | 30 |
| HFO medium-speed engines | 1,100 | 8,450 | HFO USD 300/t at 40.5 GJ/t | 30 | 9.0 | 25 |

Discount rate 10.0% (USD, real terms not used; all costs flat in 2015 USD); capacity factors from 10% to 90%; HHV/LHV 1.108 for gas. Figure P-F57.

### 4.13 Sombé West upstream and Halbeck's RBL (Chapter 75; Illustrative)

| Input | Value |
|---|---|
| Halbeck interest | 65% (SNHK 35%) |
| Development capex (gross) | USD 1.45 billion, 2017 to 2019 |
| Gross production | Plateau 150 MMscfd from 2020 to 2032, then decline 8% a year; condensate 18 bbl per MMscf |
| Gas sales | Halbeck sells its share to SNHK (aggregator) at USD 3.60/MMBtu in 2018, escalating 2.0% a year |
| Condensate price | Brent minus USD 4/bbl; bank price deck Brent USD 60/bbl flat (2017) and USD 70/bbl (2023) |
| Fiscal terms | Royalty 10% on gas, 12.5% on condensate; corporate tax 35%; no profit split (licence-and-royalty regime) |
| Opex | USD 85 million a year gross fixed plus USD 0.35/MMBtu |
| RBL | Signed October 2017; commitment USD 600 million; seven-year tenor; margin 4.25%; borrowing base = NPV at 10% of the P50 (2P) case on the bank price deck divided by 1.30, tested also on a P90 case at 1.00x; semiannual redeterminations |
| Expected outputs | Borrowing base at signing about USD 281 million; at the 2023 redetermination about USD 363 million (P-F59 computes them; revised from about 420 and 360 in v1.3, change log P-C46: sales capped at contracted SNHK demand, 40% reserve tail, completion-basis NPV; the signing base is lower because cash flows start two years later on the lower 2017 deck) |

### 4.14 Fertilizer plant and bauxite developer (Chapters 77 and 78)

- Azotes de Bélanou SA (proposed 2025): Groupe Talmé 30%, an unnamed international fertilizer group 40%, SNHK 30%; ammonia 1,200 t a day and granular urea 2,000 t a day; gas requirement about 46,000 MMBtu a day; capex about USD 1.6 billion; status pre-feasibility. Sombé West cannot supply it alongside Bélanou and SEKA's existing contract (1.7.4); it needs a new discovery or LNG imports, which links it to Chapter 76.
- Hautes-Moraba Bauxite SA (2026): a junior mining company listed abroad (nationality not stated) developing a 12 Mtpa bauxite mine in the upper Moraba basin with a planned 1.2 Mtpa alumina refinery in phase 2. It asks for 150 MW of baseload power for 25 years from a Bélanou expansion, at a USD-indexed tariff; unrated, with offtake from a single trader; it offers a parent guarantee from an entity with no operating revenue.

### 4.15 Other open items, decided

- Chapter 1 call: April 2, 2015, London.
- P-F01 overrun cause (USD 6.63 million over the USD 14.8 million budget): legal costs of the PPA, IA and guarantee negotiations above budget (USD 2.60 million); added ESIA, RAP and Category A studies required by the ABDB and Exportgarant (USD 1.90 million); a tender timetable about nine months longer than planned, carrying the development team (USD 1.40 million); additional gas supply and grid studies (USD 0.73 million). The LNTP payment is separate.
- The Gulf bank in Chapter 33 stays unnamed.
- LC requirements and LC cost bearers: 1.14.4.
- "First full operating year" for P-F10: in the FC base, the 12 months July 1, 2021 to June 30, 2022; in actual history, calendar 2022 (ledger to state).
- LLCR at close includes the DSRA balance in the numerator (book convention, Chapter 35), so the 1.40x test and the 1.35x sculpting are consistent; the ledger states the definition on P-F08.
- Thin capitalization (Kessaran law for the book): related-party debt may not exceed three times equity, where equity is share capital plus positive retained earnings; all shareholder loans count as related-party debt, including the ABDB fund's; interest on the excess is permanently non-deductible (not carried forward) and is not recharacterized as a dividend, so withholding stays at the interest rate. This is the model's rule (`case_p.py`) and resolves u09 F-05 and u14 BF-5; the effect is P-F38.
- Pillar Two: Kilnworth is in scope (consolidated revenue above EUR 750 million; ultimate parent in the UK; UK Multinational Top-up Tax from periods beginning on or after December 31, 2023). Kessara has no qualified domestic minimum top-up tax through 2026 (MEF is studying one for the Finance Act 2027). Bélanou's 0% holiday runs to November 30, 2026 (OY1 to OY5) and the 15% band to November 30, 2029. An estimate of the UK top-up on Kilnworth's share for 2024 to 2026 is P-F54, labeled an estimate, on the simplified basis in the input requests file.
- Castellan's regulator: 4.16 below.

### 4.16 Castellan, Exportgarant, insurers: regulatory facts (Chapter 68)

- Castellan Bank: UK-headquartered, authorized and regulated by the UK Prudential Regulation Authority; uses the IRB approach with supervisory slotting for specialised lending (project finance). Slotting of the commercial tranche: "Satisfactory" during construction, "Good" from Project Completion; the 2023 crisis moved it to "Weak" from June 2023 to June 2024.
- The ECA-covered tranche: 95% cover from Exportgarant, treated as an exposure to its home sovereign (rated AA or better; the sovereign is never named, D-104) for the covered part.
- The ABDB: treated by Castellan's regulator as a qualifying multilateral development bank (0% risk weight); relevant to the B-loan participations of Kaito Pacific and Sterrenberg and to the PRG.
- PRI: the insurers are rated A- or better, but the cover is political risk only, so Castellan's credit risk management does not recognize it as credit risk mitigation for capital; it uses it for country and transfer risk limits.
- RAROC inputs: 5.6 and the input requests file (P-F55).

---

## 5. Inputs for figures (summary; detail in the input requests file)

5.1 Accounting basis: 4.6. 5.2 Termination definitions: 1.1.7. 5.3 LC formulas: 1.1.5. 5.4 GSA heating value and reserves: 1.7. 5.5 PRI: 1.11.2. 5.6 Castellan: UK corporation tax 19% (2018); funding premium 0.45% a year; PD 1.6% (construction) and 0.9% (operations) a year; LGD 35% (commercial tranche), 5% on the covered part of the ECA tranche; capital ratio target 13.5% of RWA; operating cost 0.15% of exposure a year; RAROC hurdle 12% after tax. 5.7 Technology screening: 4.12. 5.8 Halbeck: 4.13. 5.9 Bid stage: 4.7. 5.10 Drought dispatch: 4.11.

---

## 6. Expiry and term summary

| Contract | Start | End (actual case) |
|---|---|---|
| PPA | COD December 1, 2021 | November 30, 2046 |
| IA, Government Guarantee | October 12, 2017 | PPA expiry plus settlement of all amounts |
| Emphyteutic lease | 2018 | 45 years (2063) |
| GSA, GTA | COD | November 30, 2043 (option to 2046) |
| LTSA | COD | About February 2037 at base dispatch (P-F48); no later than November 30, 2037 |
| O&M | COD (pre-operations from 2020) | November 30, 2031, then five-year renewals |
| Bank debt | July 17, 2018 | June 30, 2034 |
| Bond | June 30, 2025 | June 30, 2037 |
| PRI | July 17, 2018 | Cancelled June 30, 2025 |
| PRG | July 17, 2018 | PPA expiry |
| OREK license | November 22, 2017 | November 2047 |

---

## 7. Registers

### 7.1 Name register additions (Case Bible 4.5)

All characters in 2.1, plus Kwami Talmé, Séverin Talmé (Talmé shareholders, born 1980 and 1983), Daniel Fiogbé (Kessaran, born 1955; former deputy; never a scene character).

### 7.2 Organizations and places (Case Bible Part 5)

| Name | Type | Check (October 3, 2026) |
|---|---|---|
| Kilnworth Bélanou Holdings Ltd (Mauritius) | Holding company | Covered by the existing "Kilnworth" check |
| Kilnworth Power International plc | Sponsor parent | Existing |
| Talmé Énergie SA; Société Financière Talmé SA; Fondation Talmé | Talmé entities | Covered by "Talmé" (clear) |
| Pennock Mayhew Engineers | Technical adviser | Clear (no firm of that combined name; separate US firms named Mayhew exist) |
| Whinmoor Environmental | ESIA consultant | Clear (Whinmoor is a Leeds suburb; no firm of that name found) |
| Lagune Environnement SARL | Kessaran E&S sub-consultant | Not checked; generic French name, Kessaran registration only |
| Cabinet Adjovi-Lokossou; Cabinet Aïdasso & Associés | Kessaran law firms | Not checked; surname-based, Kessaran only |
| Coastal Power Access Trust Fund | Donor trust fund | Clear (near miss: a 2026 US bill, the "Coastal Trust Fund Act") |
| Azotes de Bélanou SA | Fertilizer project | Clear by construction (Bélanou is fictional) |
| Hautes-Moraba Bauxite SA | Bauxite developer | Clear by construction (Moraba is fictional) |
| Rejected | "Doumbara" (an alternative name of Doumbala, Burkina Faso); "Gulf of Guinea Power Access Facility" (too close to real African access programs) | – |

Characters web-checked: Euan MacRitchie was rejected (a real finance professional in Edinburgh) and replaced by Clive Ormesher (clear); Adwoa Sarpong-Kumi and Philippa Carrow returned no matching person. The other names were chosen to avoid famous holders (Fashola, Ofori-Atta, Zinsou, Hounsou and Houngbédji were rejected for that reason) but were not individually searched.

### 7.3 Chapter 1 illustrative deal names (u01 BF-6)

Recorded for the register, outside the running cases: Republic of Corredana and the Llano Pardo plateau (clear), Llano Pardo Solar SA, Tallisford Energy Partners (clear), Grupo Arismendi (clear as a company), Montajes Cordillera SA and Cordillera Servicios SA (clear), Cooperativa Agrícola de Llano Pardo, Electricidad Nacional de Corredana (ELNACOR: clear; near miss Elecnor, a Spanish electrical contractor, never mentioned). Cross-case table (Case Bible 4.4): Sterrenberg Bank NV and the ABDB also lend to the Chapter 1 illustrative deal in 2016; later chapters must not contradict that.

---

## 8. Figure IDs

### 8.1 IDs assigned by the editor (confirmed)

| ID | Figure | Scenario | Chapters | Requested by |
|---|---|---|---|---|
| P-F17 | Model audit findings (errors E1 to E10 per the Chapter 44 brief, one at a time and combined; optional disputed-finding variant) | FC base, downside | 44 | u09 |
| P-F37 | VAT on the onshore EPC portion: VAT paid, refunds, VAT facility balance and interest by month, peak VAT receivable and refund-lag cost; working capital balances OY1 to OY3 | FC base | 31, 41, 67 | u07, u09, u14 |
| P-F38 | Thin capitalization computation and disallowed shareholder loan interest by period | FC base and actual | 41, 67 | u14 |
| P-F39 | LC amount at COD under the two-plus-one formula and the three-month formula; annual reset values 2022 to 2025 | FC base and actual | 18, 59, 86 | u05, u12, u17 |
| P-F40 | FX losses (total of the four inputs), netting set-offs by month, settlement installments, guarantee demand-to-payment days, FX queue duration | Actual | 59 | u12 |
| P-F41 | PLCR at close (base, banking, downside); period-by-period CFADS and DSCR on the three FC cases | FC cases | 35 | u08 |
| P-F42 | Monte Carlo on availability and dispatch with locked debt | FC base | 43 | u09 |
| P-F43 | Convergence log of the FC sizing; equity-first funding variant | FC base | 40 | u09 |
| P-F44 | Revenue build OY1 to OY10 by component | FC base | 41 | u09 |
| P-F45 | FC base financial statements OY1 to OY3 with balance check (lenders' reporting basis) | FC base | 42 | u09 |

### 8.2 New IDs (P-F46 upward)

| ID | Figure | Scenario | Chapters | Requested by (brief's own provisional ID) |
|---|---|---|---|---|
| P-F46 | GTA reservation and commodity charges, 2022, and their pass-through to SEKA; GCK's revenue from the Bélanou GTA | Actual (2022) | 21, 75 | u05 (P-F37), u15 (P-F38) |
| P-F47 | Heat-rate headroom (6,323 against 6,261 kJ/kWh) as an annual fuel margin, OY1, and its path with degradation | FC base | 18, 48 | u05 (P-F39) |
| P-F48 | LTSA run-out date (128,000 EOH) by dispatch case against the 16-year date, PPA expiry and debt maturities | FC base, banking, low dispatch, actual | 24, 28, 65 | u06 (P-F37) |
| P-F49 | Funds flow at financial close, July 17, 2018: first utilization by tranche, equity at close with the LNTP credit, development cost reimbursement, development fee, ABDB fund premium, upfront fees, first ECA premium installment, advisers | FC base | 55 | u11 (P-F37) |
| P-F50 | PV of the 7.5 bps swap credit and execution charge on the notional profile; Castellan's July 2017 10 bps opening for comparison | FC base | 38, 56 | u11 (P-F38) |
| P-F51 | PRI insured amount and premium by period, 2018 to June 2025 | FC base and actual | 27, 60 | u12 (P-F37) |
| P-F52 | Planned against actual EPC progress and certified payments by quarter, 2018 to 2021 | FC base, actual | 61 | u13 (P-F37) |
| P-F53 | Expected credit loss allowance on SEKA receivables at December 31, 2022, June 30, 2023 and December 31, 2023; swap mark-to-market and hedge reserve at close, December 31, 2022, June 30, 2025 (before and after partial termination) and September 30, 2026 | Actual | 66 | u14 (P-F41) |
| P-F54 | Estimated UK Multinational Top-up Tax on Kilnworth's share of Bélanou, 2024 to 2026 (simplified) | Actual | 67 | u14 (P-F38) |
| P-F55 | Castellan: underwriting and final holds by tranche, swap line, slotting by phase, RWA and capital by tranche with ECA cover and PRI treatment, RAROC (the ledger v1.2 label "RORAC" is read as RAROC; relabel requested) | FC base | 68, 86 | u14 (P-F40), u17 (P-F38) |
| P-F56 | IFRIC 12 financial-asset presentation of Bélanou Power (key balances 2021 to 2026) and reconciliation to the lenders' basis; P-F26 recomputed on IFRS carrying amounts | Actual | 7 (one-line note), 66 | u02 BF-2, u14 BF-1 |
| P-F57 | Kessara 2015 technology screening curves: annualized cost per kW-year and cost per MWh by capacity factor | Inputs (4.12) | 69 | u15 (P-F39) |
| P-F58 | Actual dispatch and gas burn, 2022 H1 and H2, against FC base 76.5% | Actual | 72 | u15 (P-F40) |
| P-F59 | Halbeck's Sombé West RBL borrowing base at signing (2017) and at the 2023 redetermination (Illustrative) | Illustrative inputs (4.13) | 75 | u15 (P-F37) |
| P-F60 | September 2016 bid-stage screen: indicative project cost, capacity and fixed O&M revenue at 588.4 MW and the bid tariff, annuity-shortcut debt capacity at 1.35x and 75% gearing, capacity payments as a share of SEKA revenue | Bid-stage inputs (4.7) | 85 | u17 (P-F37) |
| P-F61 | Sombé West reserve coverage: 2P reserves against Bélanou GSA and SEKA contract quantities | Inputs (1.7.4) | 48 | u10 BF-5 |
| P-F62 | Bid comparison: levelized tariffs of the four bids under the RFP formula; pricing committee tariff against the submitted tariff (extends P-F06, which keeps its ID; P-F62 holds the comparison table) | Bid inputs (4.7) | 47 | u10 BF-2 |
| P-F63 | Equity cure amount needed at June 30, 2023 to restore the historic DSCR to 1.10x and to 1.20x | Actual | 62 | u13 CBF-4 |
| P-F64 | Bid-to-close equity IRR bridge: from the 16.0% bid-model IRR to the FC base IRR by step (capex, financing terms, fees and premiums, tax, FX and indexation, schedule, residual), each step re-sized | FC base re-sized at each step | 8, 47 | Editor (D-037, formerly the second D-017; sequencing review defect 19) |
| P-F65 | KCR forwards traded July 17, 2018 with Castellan: share hedged (75%), KCR notional, forward rate and USD equivalent by settlement date, USD at forward against USD at FC spot | Contract (FC) | 37, 38, 40, 66 | Editor (D-114; coverage review defect 1) |
| P-F66 | KCR forward settlements by half-year (gain to the project), mark-to-market to COD, and the unhedged comparison | Actual | 59, 61, 66 | Editor (D-114) |

### 8.3 Extensions and definitions of existing IDs

- P-F02: state the index readings (September 2021), the reconversion rate (invoice date), contracted capacity 581.9 MW.
- P-F03: computable from 4.7.
- P-F06: winning levelized tariff; P-F62 holds the comparison.
- P-F07: report equity by sponsor (60/25/15), by form (share capital and shareholder loans), with capitalized shareholder loan interest and the ECA premium amount shown separately.
- P-F08: state the LLCR definition (DSRA included).
- P-F10: state the CFADS definition (MMRA inside; DSRA interest excluded; DSU and BI included; performance LDs excluded) and "first full operating year" (4.15).
- P-F11: split into P-F11a (DSRA, Chapter 37) and P-F11b (MMRA, Chapters 24 and 37).
- P-F12: add commercial tranche all-in cost with and without the PRI premium and the withholding gross-up, and the ECA tranche with and without the financed premium.
- P-F16: add Chapter 35 as a user for breakevens.
- P-F20: unchanged; detailed crisis items go to P-F40.
- P-F25: use the definitions in 1.1.7.
- P-F26: include the fair value of the retained 36% (rule in the input requests file) and recycling of the hedge reserve; compute on IFRS (IFRIC 12) carrying amounts (P-F56).
- P-F28: defined as: sources and uses (P-F07); senior debt by tranche and binding constraint (P-F08); minimum and average DSCR on base, banking and downside, LLCR at close, gearing; WAL and ECA tests (P-F09); all-in cost by tranche (P-F12); DSRA size (P-F11a); breakevens including months of zero SEKA payment covered by DSRA plus LC (P-F16); LC at COD under two-plus-one (P-F39); the swap rate (2.947%).
- P-F31: unchanged; drought dispatch is P-F58.
- D-013 covers, with no ID: days to the PPA delay LD cap; the 6,323 against 6,261 gap; the FC base first-period fraction; trigger-ladder percentages (1 − 1.20/1.35 and 1 − 1.10/1.35); the Chapter 28 hypothetical trace at the stated assumptions; base EOH per year (8,439).

### 8.4 Provisional ID concordance (binding)

Each brief requested its own "P-F37 onward", and those provisional meanings collide with the IDs assigned above and printed in `model/figure-ledger-case-p.md`. A writer reads a provisional ID in a brief through this table and cites only the final ID. Rows were built by matching each brief's description against the ledger labels (ledger v1.2). "No ID" means the number is D-013 arithmetic or the request was folded into an existing figure.

| Unit | Chapter | Provisional ID in the brief | Brief's description | Final ID |
|---|---|---|---|---|
| u05 | 21 | P-F37 | GTA annual charges, 2022, and pass-through to SEKA | P-F46 |
| u05 | 18 | P-F38 | LC at COD under the three-month and two-plus-one formulas, FC base | P-F39 |
| u05 | 18 | P-F39 | Heat-rate headroom and annual fuel margin, FC base, OY1 | P-F47 |
| u06 | 24, 28, 65 | P-F37 | LTSA run-out date by dispatch case against PPA expiry and debt maturity | P-F48 |
| u06 | 28 | P-F38 | 2018 hypothetical grid-surge trace at an assumed delay | No ID: D-013 arithmetic at the assumptions in 2.2 row 28 (120 days, USD 7.5 million) |
| u08 | 35 | P-F37 | PLCR at close; period-by-period CFADS and DSCR on base, banking and downside | P-F41 |
| u08 | 35 | P-F38 | Case P breakevens for 1.00x minimum DSCR | P-F16 (Chapter 35 added as a user) |
| u08 | 37 | P-F39 | Trigger-ladder CFADS falls to lock-up and default | No ID: D-013 arithmetic (8.3) |
| u09 | 43 | P-F37 | Monte Carlo on availability and dispatch with locked debt | P-F42 |
| u09 | 40 | P-F38 | Convergence log of the FC sizing; equity-first variant | P-F43 |
| u09 | 41 | P-F39 | Revenue build OY1 to OY10 by component | P-F44 |
| u09 | 41 | P-F40 | Construction VAT, refunds, VAT facility; working capital OY1 to OY3 | P-F37 |
| u09 | 42 | P-F41 | FC base financial statements OY1 to OY3 with balance check | P-F45 |
| u11 | 55 | P-F37 | Funds flow at financial close, July 17, 2018 (exh:55.10) | P-F49 |
| u11 | 56 | P-F38 | PV of the swap credit and execution charge | P-F50 |
| u12 | 60 | P-F37 | PRI insured amount and premium, 2018 to June 2025 | P-F51 |
| u14 | 66 | P-F41 | ECL allowance on SEKA receivables; swap MTM and hedge reserve | P-F53 |
| u14 | 66, 67 | P-F37 | VAT paid on the onshore EPC portion, peak VAT receivable, refund-lag cost | P-F37 (same ID, same meaning) |
| u14 | 67 | P-F38 | Estimated GloBE (UK Multinational Top-up Tax) on Bélanou, 2024 to 2026 | P-F54 |
| u14 | 67 | P-F39 (proposed) | Thin-capitalization computation and disallowance | P-F38 |
| u14 | 68 | P-F40 | Castellan's exposures, slotting, RWA and capital by tranche | P-F55 |
| u15 | 75 | P-F37 | Halbeck's Sombé West RBL borrowing base, 2017 and 2023 | P-F59 |
| u15 | 75 | P-F38 | GCK reservation and commodity revenue from the Bélanou GTA, 2022 | P-F46 |
| u15 | 69 | P-F39 | Kessara 2015 technology screening curves | P-F57 |
| u15 | 72 | P-F40 | Actual dispatch and gas burn, 2022 H1 and H2 | P-F58 |
| u17 | 85 | P-F37 | September 2016 bid-stage screen | P-F60 |
| u17 | 86 | P-F38 | Castellan's underwriting, holds, swap line, slotting and RAROC box | P-F55 |

The ledger itself carries P-F37 and P-F40 extension rows (working capital 2021H1; netting set-offs; the February 2023 LC drawing) under the same IDs: they belong to the 8.1 definitions. Anchor registry caption fix for the next regeneration: `exh:55.10` "Case P closing-day funds flow (P-F49)".

---

## 9. Flaw resolution map

### 9.1 Case P flaws by unit

| Unit | Flaw | Resolution |
|---|---|---|
| u01 | BF-1 IC members | 2.1 |
| u01 | BF-2 development advisers | 2.3 |
| u01 | BF-3 co-development vs budget | 1.14.1; P-C22 |
| u01 | BF-4 P-F01 overrun cause | 4.15 |
| u01 | BF-5 call date | 4.15 |
| u01 | BF-6 register and cross-case | 7.3 |
| u02 | BF-1 P-F03 inputs | 4.7 |
| u02 | BF-2 accounting basis | 4.6; P-F56 |
| u02 | BF-3, BF-4 Case R | Forwarded (9.3); already resolved by R-C09, R-C10 |
| u02 | BF-5 P-F02 details | 1.1.5; 3.9; 8.3 |
| u02 | BF-6 Kilnworth finance staff | 2.1 |
| u03 | 1 hardship exclusion | 1.1.4 |
| u03 | 2 FM regime | 1.1.2 |
| u03 | 3 derived figures | D-013 (8.3) |
| u03 | 4 Ch 11 Mariama | Approved (2.1) |
| u03 | 6 Sombé West heating value | 1.7.2 |
| u03 | 5, 7, 8 Case T | Forwarded |
| u04 | BF-01 Ch 16 row | 3.2; 2.2 |
| u04 | BF-02 Gwen Feb 2017 | 3.3 |
| u04 | BF-03 register, matrix, plan as canon | Adopted: the content of briefs u04 sections 14.J, 15.J and 16.J is canon, subject to this annex where they differ (P-C31) |
| u04 | BF-04 Tomasz convertibility | 3.4 |
| u04 | BF-05 PRI binding date | 1.11.2 |
| u04 | BF-06 grid-interface allocation date | 1.4.2 |
| u05 | 1 GTA figure | P-F46 |
| u05 | 2 LC at COD; heat-rate headroom | P-F39; P-F47 |
| u05 | 3 SEKA opening availability | 1.1.1 |
| u05 | 4 2024 solar CfD | 4.8 |
| u05 | 5 Lindauer opening offer | 1.4.1 |
| u05 | 6 Gwen preliminary view | 1.4.1 |
| u06 | BF-1 Case T | Forwarded |
| u06 | BF-2 LTSA | 1.5; P-F48 |
| u06 | BF-3 O&M | 1.6 |
| u06 | BF-4 P-F11 split | 8.3 |
| u06 | BF-5 GSA term and terms | 1.7 |
| u06 | BF-6 permits | 1.9 |
| u06 | BF-7 governance | 1.14 |
| u06 | BF-8 direct agreements | 1.10 |
| u06 | BF-9 trace and subrogation | 2.2 (row 28); 1.1.8; 2.8 |
| u06 | BF-10 SEKA risk event compensation | 1.1.3 |
| u07 | 1 ECA tests pre-2023 | 3.6 |
| u07 | 2 VAT figure | P-F37 |
| u07 | 3 standby margin | 1.15.1 |
| u07 | 4 2024 rating pre-assessment | 4.10 |
| u07 | 5 Thandeka PRG | 3.1 |
| u07 | 6 unsubsidized fee, donor facility, KCR market | 4.9; 4.5 |
| u07 | 7 LC requirements | 1.14.4 |
| u07 | 8 Gulf bank | Unnamed (4.15) |
| u07 | 9 P-F07 detail | 8.3 |
| u07 | 10 ECA premium figure | 8.3 (P-F07) |
| u08 | 1 LLCR definition | 4.15; 8.3 |
| u08 | 2 CFADS definition | 8.3 |
| u08 | 3 PLCR, breakevens | P-F41; P-F16 |
| u08 | 4 register users | 2.2; 8.3 |
| u08 | 5 trigger ladder | D-013 |
| u08 | 6 P-F12 scope | 8.3 |
| u08 | 7 first full operating year | 4.15 |
| u08 | 8 ECA rules in 2018 | 3.6 |
| u09 | F-01, F-02, F-06 to F-11, F-13, F-14, F-17 to F-20, F-24 | Model rules: owned by the Case P model report; this annex adds nothing except: F-11 (MMRA inside CFADS, confirmed 1.15.6), F-13 (book depreciation over the PPA term on the lenders' basis, 4.6), F-24 (16.0% target measured on Kilnworth's bid model, 4.7; reference model basis per the model report) |
| u09 | F-03 ECA first repayment | 3.6 |
| u09 | F-04 downside dispatch | 3.7 |
| u09 | F-05 thin cap | 4.15 |
| u09 | F-12 PRI base | 1.11.2 |
| u09 | F-15 style sheet 1.108 note | Forwarded to the style editor |
| u09 | F-16 policy rates; VAT facility interest | 4.5; placement as in the model (funded use before COD, operating cost after) |
| u09 | F-21 Monte Carlo inputs | Adopted as proposed (input requests file) |
| u09 | F-22 Case R | Forwarded |
| u09 | F-23 characters in modeling chapters | Approved: Castellan, Kilnworth (Kunal Mehrotra) and Pieter may frame drills without scenes |
| u10 | BF-2 bid numbers | 4.7; P-F62 |
| u10 | BF-4 IE report | 4.1 |
| u10 | BF-5 reserve coverage | 1.7.4; P-F61 |
| u10 | BF-6 KYC, holdco, ceiling, DD list, payment plan | 2.4; 1.3; 1.2; 4.2 |
| u10 | BF-7 ESAP etc. | 4.3 |
| u10 | BF-1, BF-3, BF-8 Case R and T | Forwarded |
| u11 | B1, B2 row 53 | 2.1; 2.2 |
| u11 | B3 financing strategy | 1.15.1 |
| u11 | B4 funds flow | P-F49 |
| u11 | B5 CP list | 1.15.3 |
| u11 | B6 change of control | 1.15.4 |
| u11 | B7 permitted debt | 1.15.5 |
| u11 | B8 ICA | 1.15.8 |
| u11 | B9 treaty and disputes | 1.2; 1.3; 1.13 |
| u11 | B10 priority of payments etc. | 1.15.6; 1.15.7 |
| u11 | B11 term sheet | 1.15.2 |
| u11 | B12 swap charge PV | P-F50 |
| u11 | B13 re-notification | 1.15.12 |
| u11 | B14 typo | 2.7; P-C21 |
| u12 | 6 PRI terms | 1.11.2 |
| u12 | 7 ABDB halo | 1.15.9 |
| u12 | 8 PRG statement | 3.1 |
| u12 | 9 P-F20 extension | P-F40 |
| u12 | 10 LC at signing | 1.1.5; P-F39 |
| u12 | 1 to 5 Case T | Forwarded |
| u13 | CBF-1 subrogation | 2.8 |
| u13 | CBF-2 completion test, HRSG | 1.12 |
| u13 | CBF-3 progress figure | P-F52 |
| u13 | CBF-4 budget, information, cure, votes | 1.15.10; 1.15.11; P-F63 |
| u13 | CBF-7 handback | 1.1.6 |
| u13 | CBF-8 end dates | 1.5; 1.6; 1.7.1; 6 |
| u13 | CBF-5, CBF-6, CBF-9 Case T and R | Forwarded |
| u14 | BF-1 accounting | 4.6 |
| u14 | BF-2 reporting frameworks | 4.6 |
| u14 | BF-3 reserved matters, associate | 1.14.3 |
| u14 | BF-4 P-F26 inputs | 8.3; input requests |
| u14 | BF-5 thin cap | 4.15 |
| u14 | BF-6 Pillar Two | 4.15; P-F54 |
| u14 | BF-7 Castellan, ratings | 4.16; P-F55 |
| u14 | BF-10 climate data | 4.4 |
| u14 | BF-11 IDs | P-F53, P-F37, P-F38 |
| u14 | BF-12 Gwen in Ch 84 | Approved (2.1) |
| u14 | BF-8, BF-9 Case T and R | Forwarded |
| u15 | 1 technology costs | 4.12; P-F57 |
| u15 | 2 drought dispatch; Moraba Falls | 4.11; P-F58 |
| u15 | 4 Halbeck RBL; GCK | 4.13; 1.8; P-F59; P-F46 |
| u15 | 5 minor characters | 2.1 |
| u15 | 6 minister after October 2023 | 2.1 |
| u15 | 3, 7 Case R | Forwarded |
| u16 | CB-u16-1 fertilizer | 4.14 |
| u16 | CB-u16-2 bauxite | 4.14 |
| u16 | Others (Case T, R) | Forwarded |
| u17 | BF-u17-01 bid screen, SEKA revenue | 4.7; 4.5; P-F60 |
| u17 | BF-u17-02 Castellan, P-F28 | 1.15.1; 5.6; P-F55; 8.3 |
| u17 | BF-u17-03 committee chair | 2.1; 2.5 |
| u17 | BF-u17-04 intermediary | 2.6 |
| u17 | BF-u17-05, BF-u17-06 Case R and capstone | Forwarded |
| feedback (u02, u06) | P-F11 split, Kilnworth character | 8.3; 2.1 |

### 9.2 Contradictions found by this editor

ABDB fund entry not pro rata (P-C24); ECA first-repayment test (P-C23); downside dispatch label (P-C25); index readings (P-C26); Chapter 34 end state (P-C28); indirect transfer tax on a direct sale (P-C29); pipeline landfall (P-C30).

### 9.3 Forwarded (not Case P)

Case T: u03 5, 7, 8; u06 BF-1; u10 BF-3; u12 1 to 5; u13 CBF-5, CBF-6; u14 BF-8; u16 CB-u16-3, -4, -7, -8 (Callum's "last scene in story order"). Case R: u02 BF-3, BF-4 (resolved by R-C09, R-C10); u09 F-22; u10 BF-1, BF-8; u13 CBF-9; u14 BF-9; u15 3, 7; u16 CB-u16-5, -6; u17 BF-u17-05. Capstone: u17 BF-u17-06. Style sheet: u09 F-15.

---

## 10. Change log (continues Case Bible Part 8)

| # | Date in story | Chapter | Case | Item changed | Old value | New value | Source |
|---|---|---|---|---|---|---|---|
| P-C16 | 2023 | 34, 59 | P | Thandeka sheet: PRG against peak arrears | "less than one quarter" | "about a third (net of LC); under 30% gross" | Annex 3.1 |
| P-C17 | 2017-05 | 16 | P | Chapter 16 row figures | LC 33.8, PRG 41.5, contingent equity 15.4, standby 46.0 as May 2017 values | Inputs at financial close, labeled; May 2017 proposals separate | Annex 2.2 |
| P-C18 | 2017-02 | 15, 48 | P | Gwen's engagement | From mandate (June 2017) | Pre-mandate review for Castellan from February 2017 | Annex 3.3 |
| P-C19 | 2025 | 53 | P | Row 53 characters | Pieter, Henrike, Thandeka | Pieter, Henrike, Laurent; Thandeka 2018 only; Adwoa Sarpong-Kumi 2025 | Annex 2.2 |
| P-C20 | 2016-10 | 14, 59 | P | Tomasz's convertibility error | 2017 | From October 2016 | Annex 3.4 |
| P-C21 | – | 56 | P | Pieter sheet typo | "in 2016 ... in 2016" | Single "in 2016" | Annex 2.7 |
| P-C22 | 2015-06 to 2015-09 | 2, 4 | P | Co-development agreement | Unconditional, June 2015 | Phase 1 under delegated authority; Phase 2 conditional on the September 17, 2015 budget approval | Annex 1.14.1 |
| P-C23 | 2018 | 29, 36 | P | ECA first repayment test | Within 6 months of COD | Within 24 months of COD, at least 2% repaid | Annex 3.6; t-oecd-pf-2018 |
| P-C24 | 2018-07-17 | 26, 32 | P | ABDB fund entry | Pro rata to stakes | 10 points from Kilnworth, 5 from Talmé; premium 3.2333 / 1.6167 | Annex 1.14.2 |
| P-C25 | – | 25, 39 | P | Dispatch 58.0% label | "Downside" | "Low dispatch (gas analysis)"; FC downside uses 76.5% | Annex 3.7 |
| P-C26 | – | 5, 18 | P | Index readings | "Lagged three months" | September and March readings | Annex 3.9 |
| P-C27 | 2022-03 to 2024-03-21 | 59, 61 | P | Grid-event claim against SEKA | Not recorded | USD 9.27 million claimed March 2022; liability accepted May 2022; unpaid; waived in the March 21, 2024 settlement | Annex 1.1.3 |
| P-C28 | 2017; 2018-06-20 | 34 | P | PRG approval | "PRG approved" (2017) | Board approval June 20, 2018 at USD 41.5 million | Annex 2.5; 4.9 |
| P-C29 | 2026-09-30 | 63, 67 | P | Indirect transfer tax scope | Offshore indirect transfers | Includes the direct sale by the Mauritius holding company; treaty Article 13(4) | Annex 1.3.3 |
| P-C30 | 2015; 2017 to 2019 | 12, 75 | P | Coastal pipeline existence in 2015 | Implied existing | Designated landfall in 2015; pipeline built 2017 to 2019 | Annex 1.8 |
| P-C31 | 2016-10 to 2017-05 | 14 to 16, 28, 59, 85, 86 | P | Risk register v1, March 2017 matrix, May 2017 mitigation plan | No canonical content | Briefs u04 14.J, 15.J, 16.J adopted as canon | Annex 9.1 |
| P-C32 | 2022 | 72 | P | Actual dispatch 2022 | 76.5% (model default) | 84.0% (H1), 81.5% (H2) | Annex 4.11; P-F58 |
| P-C33 | 2018 to 2034 | 27, 60 | P | PRI policy period and terms | Unspecified | To June 30, 2034; terms per 1.11.2; cancelled June 30, 2025 | Annex 1.11.2 |
| P-C34 | 2021-02 | 61 | P | Abdoulaye's appointment as minister | "2021" | February 2021 | Annex 2.7 |
| P-C35 | 2023-10-16 | 59, 74 | P | Minister after the reshuffle | Unnamed | Sylvestre Ahouansou | Annex 2.1 |
| P-C36 | 2024-06 | 63 | P | SEKA CFO after Hyacinthe | Unnamed | Rosine Gbaguidi-Ayi | Annex 2.1 |
| P-C37 | 2026-09-30 | 26, 63, 66 | P | Board composition | Unspecified | 6 seats (4/1/1) at close; 7 seats (2/2/2/1) after the sale | Annex 1.14.3 |
| P-C38 | 2015-08-11 | 54, 67 | P | Holding company jurisdiction | "A treaty jurisdiction" | Mauritius; BIT 2004/2006; DTA 2009/2011 | Annex 1.3 |
| P-C39 | 2017 to 2043 | 25, 28, 65, 76 | P | GSA and GTA term | 22 years from an unstated start | From COD to November 30, 2043; deliberate gap to PPA expiry | Annex 1.7.1 |
| P-C40 | 2018 | 7, 66 | P | Accounting framework | Unstated | IFRS, USD functional, IFRIC 12 financial asset; lenders' basis fixed-asset model | Annex 4.6 |

Rows P-C41 to P-C48 (model calibrations, the overrun funding, the LC value, the currency hedge and the Chapter 6, 8 and 12 scene fixes) are in Case Bible Part 8.
