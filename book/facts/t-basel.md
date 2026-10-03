# Basel slotting approach for project finance; Basel III final / "3.1" implementation in the EU, UK and US

As of: 2026-10-03. Latest events covered: the US agencies' capital proposals of 19 March 2026 (Federal Register, 27 March 2026; comments closed 18 June 2026), and the EU CRR3 transitional schedule in force since 1 January 2025.

## Summary

Banks lending to projects hold capital in one of three ways:
- **Standardised approach (SA):** fixed risk weights.
- **Internal ratings-based (IRB) approach:** the bank's own probability of default (PD), and possibly loss given default (LGD), estimates.
- **Supervisory slotting approach:** a variant of IRB for specialised lending. Banks unable to estimate PD map each loan into one of five supervisory categories (Strong, Good, Satisfactory, Weak, Default). Each category carries a fixed risk weight and expected-loss (EL) rate, assessed on financial strength, political and legal environment, transaction characteristics, sponsor strength and security package.

The Basel Committee's December 2017 "Basel III: Finalising post-crisis reforms" package made three changes that matter here:
- it added a project-finance-specific SA treatment;
- it added input floors on IRB parameters;
- it added an output floor limiting modelled risk-weighted assets (RWA) to no less than 72.5% of standardised RWA.

The BCBS set implementation for 1 January 2023, with the output floor transition to 1 January 2028.

Implementation has diverged by jurisdiction:
- **EU:** applied the package through CRR3 (Regulation (EU) 2024/1623) from 1 January 2025. It phases the output floor in from 50% (2025) to 72.5% (2030), keeps its 0.75 infrastructure supporting factor, and halves the specialised-lending LGD input floors until 2027.
- **UK:** published near-final rules in September 2024. Among other things they add a 50% slotting weight for "substantially stronger" project finance and move the infrastructure and SME support factors into Pillar 2A. Start was deferred to 1 January 2027, with full implementation still 1 January 2030.
- **US:** rescinded its 2023 proposal. On 19 March 2026 it proposed a largely standardised framework for the largest banks with no internal credit models and no output floor. Project finance would carry 130% risk weight before operation and 100% in operation.

## Verified facts

**Slotting (supervisory categories), as transposed in the EU CRR**
1. **EU slotting risk weights.** Where a bank cannot estimate PDs for specialised lending, CRR Article 153(5) assigns these weights:

   | Remaining maturity | Category 1 (Strong) | Category 2 (Good) | Category 3 (Satisfactory) | Category 4 (Weak) | Category 5 (Default) |
   |---|---|---|---|---|---|
   | Under 2.5 years | 50% | 70% | 115% | 250% | 0% |
   | 2.5 years or more | 70% | 90% | 115% | 250% | 0% |

   The required assessment factors are financial strength, political and legal environment, transaction and/or asset characteristics, strength of the sponsor and developer (including any PPP income stream), and security package. [confidence: high] [source: 1]
2. **EU slotting EL rates** (CRR Article 158(6)):

   | Remaining maturity | Category 1 | Category 2 | Category 3 | Category 4 | Category 5 |
   |---|---|---|---|---|---|
   | Under 2.5 years | 0% | 0.4% | 2.8% | 8% | 50% |
   | 2.5 years or more | 0.4% | 0.8% | 2.8% | 8% | 50% |

   These match the Basel slotting calibration. Basel lets supervisors allow the lower weights for Strong and Good. [confidence: high for EU text; medium-high that Basel matches, since the BIS text could not be retrieved for this check] [source: 1, 2]

**Basel III final (BCBS)**
3. The BCBS published "Basel III: Finalising post-crisis reforms" on 7 December 2017. On 27 March 2020 the GHOS deferred implementation by one year, to 1 January 2023, and extended the output-floor transitional arrangements to 1 January 2028. [confidence: high] [source: 2, 3]
4. The Basel output floor is 72.5% of RWA calculated using only standardised approaches, as described by the US agencies in March 2026. [confidence: high] [source: 4]
5. **Basel SA for project finance.** For unrated project finance exposures the weights are:
   - 130% in the pre-operational phase;
   - 100% in the operational phase;
   - 80% for "high-quality" operational exposures meeting specified criteria.

   The EU (Article 122a) and the US proposal (130%/100%, no 80% tier) adopt these. [confidence: medium-high; derived from the EU and US transpositions, not from direct reading of the BIS text] [source: 4, 5]

**European Union: CRR3**
6. Regulation (EU) 2024/1623 of 31 May 2024 (CRR3) amended CRR 575/2013 for credit risk, CVA, operational risk, market risk and the output floor. It was published in the Official Journal on 19 June 2024 and applies from 1 January 2025, with some provisions applying from 9 July 2024. [confidence: high] [source: 5]
7. **Specialised lending definition.** CRR3 Article 122a creates a specialised-lending sub-class within SA corporates. Such an exposure has four features:
   - it is to an entity created specifically to finance or operate physical assets;
   - it is not residential or commercial real estate;
   - the lender has substantial control over the assets and their income;
   - repayment comes primarily from the income of the financed assets.

   Rated exposures take the corporate credit-quality-step weights: 20%, 50%, 75%, 100%, 150%, 150%. [confidence: high] [source: 5]
8. **Unrated specialised lending under SA (EU):**
   - object finance: 100%;
   - commodity finance: 100%;
   - project finance, pre-operational: 130%;
   - project finance, operational: 100%;
   - project finance, operational and high-quality: 80%, but only if the Article 501a infrastructure factor is not applied. [confidence: high] [source: 5]
9. **EU high-quality project finance criteria (80%):**
   - covenant restrictions, including no new debt without existing lenders' consent;
   - reserves fully funded in cash, or arrangements with an entity of at least credit quality step 3, covering contingency and working capital needs;
   - predictable cash flows covering all future repayments;
   - where revenues are not from many users, dependence on a main counterparty of sufficient quality (for example a 0%-weighted or credit-quality-step-3 government or a qualifying public sector entity);
   - pledged assets and contracts;
   - lender step-in rights.

   Cash flows count as "predictable" only if a substantial part of revenues is availability-based, subject to rate-of-return regulation, or under take-or-pay. [confidence: high] [source: 5]
10. **EU operational phase definition.** The project entity has positive net cash flow sufficient to cover remaining contractual obligations, and declining long-term debt. [confidence: high] [source: 5]
11. **EU output floor phase-in** (CRR3 Article 465). The factor x is:

    | Year | Factor x |
    |---|---|
    | 2025 | 50% |
    | 2026 | 55% |
    | 2027 | 60% |
    | 2028 | 65% |
    | 2029 | 70% |

    It reaches 72.5% thereafter, since Article 465 provides no transitional factor after 2029. Until 31 December 2032, IRB banks computing the floor may weight unrated corporates at 65% where their PD estimate is no more than 0.5%. [confidence: high] [source: 5]
12. **EU specialised-lending transitional** (CRR3 Article 495b). For IRB specialised lending with own LGD estimates, LGD input floors are multiplied by:
    - 50% from 2025 to 2027;
    - 80% in 2028;
    - 100% from 2029.

    The EBA was asked to report on SL risk-parameter calibration by 10 July 2026. The Commission was to propose legislation, where appropriate, by 31 December 2027. Until 31 December 2032, unrated high-quality object finance may take 80% where Article 501a is not applied. [confidence: high] [source: 5]
13. **EU infrastructure supporting factor** (CRR Article 501a, inserted by CRR2, Regulation 2019/876). It multiplies credit-risk own-funds requirements by 0.75 for qualifying infrastructure exposures to entities created to finance or operate essential public-service facilities. CRR3 amended its conditions but did not delete it. [confidence: high] [source: 5, 6]

**United Kingdom: Basel 3.1**
14. The PRA published near-final policy statement PS9/24 (Basel 3.1, part 2) on 12 September 2024. It then planned implementation from 1 January 2026, with transition to full implementation by 1 January 2030. [confidence: high] [source: 7]
15. **PS9/24 specialised-lending changes:**
    - a new 50% risk weight for "substantially stronger" project finance exposures under slotting, down from the 70% proposed in CP16/22;
    - removal of the SME and infrastructure support factors from Pillar 1, offset by new firm-specific Pillar 2A "SME lending adjustment" and "infrastructure lending adjustment".

    The PRA estimated the aggregate Tier 1 requirement increase for major UK banks at less than 1% by 1 January 2030. [confidence: high] [source: 7]
16. On 17 January 2025 the PRA delayed UK implementation to 1 January 2027, shortening transitional periods so that full implementation remains 1 January 2030. It cited the need for clarity on US plans. [confidence: high] [source: 8]

**United States**
17. The US agencies proposed Basel III-based rules on 27 July 2023 (published 88 FR 64028, 18 September 2023). In the March 2026 proposals the agencies state they are rescinding the 2023 proposal. [confidence: high] [source: 4, 9]
18. On 19 March 2026 the Federal Reserve, FDIC and OCC proposed three rules:
    - an "expanded risk-based approach" for Category I and II banking organisations (optional for others). The standardised approach would no longer apply to them and the advanced approaches would be removed;
    - revised standardised-approach weights for other banks, including a cut in the general corporate risk weight from 100% to 95%;
    - a GSIB surcharge revision.

    Comments were due by 18 June 2026. The agencies anticipated a modest decrease in overall capital. [confidence: high] [source: 9, 10]
19. **US treatment of project finance.** The March 2026 large-bank proposal defines a project finance exposure as a corporate exposure repaid from, and secured by, a single project's revenues, owed by a special-purpose obligor. It weights such exposures at 130% pre-operational and 100% operational. Operational means positive net cash flow sufficient for debt service and expenses, with declining long-term debt. Real-estate-reliant exposures, and exposures guaranteed by government or classed as public sector entity (PSE) obligations, are excluded. There is no slotting or 80% tier. [confidence: high] [source: 4]
20. **No US output floor.** The proposal would not include the Basel 72.5% output floor, because the requirements would be "almost completely standardized". The agencies asked for comment on the point. [confidence: high] [source: 4]
21. No final US rule implementing the March 2026 proposals had been located as of 2026-10-03. The Federal Reserve's banking-regulation press feed up to 2 October 2026 shows no final capital rule on these proposals. [confidence: medium] [source: 11]

## Timeline

| Date | Event |
|---|---|
| Jun 2004 | Basel II (introduces IRB and slotting for specialised lending) |
| 26 Jun 2013 | CRR 575/2013 adopted (slotting at Art 153(5)) |
| 7 Dec 2017 | BCBS "Basel III: Finalising post-crisis reforms" |
| 2019 | CRR2 (Reg 2019/876) adds 0.75 infrastructure supporting factor (Art 501a) |
| 27 Mar 2020 | GHOS defers implementation to 1 Jan 2023; output-floor transition to 1 Jan 2028 |
| 27 Jul 2023 | US agencies' Basel III endgame proposal (88 FR 64028) |
| 31 May 2024 | CRR3 adopted (OJ 19 Jun 2024) |
| 12 Sep 2024 | PRA PS9/24 near-final rules |
| 1 Jan 2025 | CRR3 applies; EU output floor 50% |
| 17 Jan 2025 | PRA delays Basel 3.1 to 1 Jan 2027 |
| 19 Mar 2026 | US agencies' three capital proposals; 2023 proposal rescinded |
| 18 Jun 2026 | US comment deadline |
| 10 Jul 2026 | EBA report on SL IRB calibration due (EU) |
| 1 Jan 2027 | UK Basel 3.1 start (per Jan 2025 announcement) |
| 31 Dec 2027 | Commission SL legislative proposal deadline, where appropriate |
| 1 Jan 2030 | EU floor at 72.5%; UK full implementation |
| 31 Dec 2032 | EU transitional 65% unrated-corporate and 80% object-finance treatments end |

## Financing and structure details

A worked comparison for the textbook: a EUR 100m operational project loan, 10 years remaining, at the 8% minimum total capital ratio, before buffers.

| Treatment | Risk weight | RWA | Minimum capital |
|---|---|---|---|
| EU slotting "Strong" (2.5 years or more) | 70% | EUR 70m | EUR 5.6m |
| EU slotting "Good" | 90% | EUR 90m | EUR 7.2m |
| EU slotting "Satisfactory" | 115% | EUR 115m | EUR 9.2m |
| EU SA, unrated operational | 100% | EUR 100m | EUR 8.0m |
| EU SA, high-quality operational | 80% | EUR 80m | EUR 6.4m |
| EU SA, pre-operational | 130% | EUR 130m | EUR 10.4m |

Under the full 72.5% output floor, an IRB bank's aggregate RWA cannot fall below 72.5% of its SA RWA. Applied illustratively to a single loan, a 100% SA weight sets a floor of 72.5% against a 70% Strong slot, so the floor binds slightly. During the EU phase-in, x is 50-70%. Calculations are illustrative arithmetic, not sourced figures.

## What went wrong or right, and why

- The policy tension is between risk sensitivity and comparability. The BCBS reforms aimed to reduce RWA variability across banks (BCBS 2017 package, source 2). Project finance industry groups have argued that SA weights overstate risk for operational PF. Regulators responded in three ways:
  - the 80% high-quality tier in Basel and the EU;
  - the UK's 50% "substantially stronger" slot;
  - EU transitional relief on LGD floors.
- The UK explicitly tied its timetable to US progress (PRA, January 2025, source 8). The US March 2026 proposal drops the output floor and internal credit models (source 4). These two choices show competitive pressure shaping implementation.
- Do not attribute specific default-and-recovery studies, such as Moody's PF default studies, unless sourced in the chapter.

## Teaching angles by chapter

- **Ch 68 (Capital rules for banks and insurers):**
  - Teach the three routes (SA, slotting, IRB) with the EU tables and the worked EUR 100m example.
  - Show how each route converts a project's credit quality into capital and therefore into the minimum margin a bank needs for its return-on-equity hurdle.
  - Use the 130/100/80 SA ladder to show why construction risk is "expensive" for banks and why refinancing at COD lowers the cost of capital.
  - Map the 80% high-quality criteria onto ordinary PF features (reserves, covenants, availability or take-or-pay revenues, step-in). Structuring choices like these move capital.
  - Contrast the EU, UK and US to show that the same loan carries different capital in different jurisdictions. This affects which banks win PF mandates.
  - Stress the as-of date. The US rules were proposals only, and the EU and UK schedules are transitional, so the reader should check the EUR-Lex consolidated CRR, the PRA Rulebook and the Federal Register.

## Do not state

- Do not state that Basel's own output-floor phase-in percentages for 2023-2027 are identical to the EU's. The EU began in 2025. Basel's schedule (50% in 2023 rising to 72.5% in 2028) is widely reported but was not directly verified here.
- Do not state UK output-floor transitional percentages for 2027-2029. They were not verified after the January 2025 delay.
- Do not state that the UK's 50% "substantially stronger" slot also applies to object finance or income-producing real estate (IPRE). Only project finance was confirmed.
- Do not state that the EBA delivered its July 2026 SL report, or what it recommended. This was not verified.
- Do not describe the US March 2026 proposals as final rules, or give an effective date.
- Do not say Basel requires slotting. It is the fallback for banks that cannot meet IRB PD estimation requirements for specialised lending.
- Do not cite aggregate capital-impact numbers for EU or US banks beyond those quoted from the PRA in PS9/24 (fact 15).

## Sources

1. Regulation (EU) No 575/2013 (CRR), Articles 153(5) and 158(6), as published 27 June 2013. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32013R0575
2. Basel Committee on Banking Supervision, "Basel III: Finalising post-crisis reforms", BIS, 7 December 2017 (landing page; full PDF not retrievable for this check). https://www.bis.org/bcbs/publ/d424.htm
3. "Governors and Heads of Supervision announce deferral of Basel III implementation to increase operational capacity of banks and supervisors to respond to Covid-19", BIS press release, 27 March 2020. https://www.bis.org/press/p200327.htm
4. Federal Reserve, FDIC, OCC, "Regulatory Capital Rule: Category I and II Banking Organizations, Banking Organizations With Significant Trading Activity, and Optional Adoption for Other Banking Organizations", proposed rule, Federal Register Vol. 91, No. 59, 27 March 2026 (FR Doc. 2026-05959). https://www.govinfo.gov/content/pkg/FR-2026-03-27/pdf/2026-05959.pdf
5. Regulation (EU) 2024/1623 of 31 May 2024 (CRR3), OJ L, 19 June 2024 (Articles 122a, 465, 495b, 501a amendments; Article 2 application dates). https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1623
6. Regulation (EU) 2019/876 (CRR2), Article 501a. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32019R0876
7. Prudential Regulation Authority, PS9/24 "Implementation of the Basel 3.1 standards near-final policy statement part 2", Bank of England, 12 September 2024. https://www.bankofengland.co.uk/prudential-regulation/publication/2024/september/implementation-of-the-basel-3-1-standards-near-final-policy-statement-part-2
8. "The PRA announces a delay to the implementation of Basel 3.1", Bank of England, 17 January 2025. https://www.bankofengland.co.uk/news/2025/january/the-pra-announces-a-delay-to-the-implementation-of-basel-3-1
9. "Agencies request comment on proposals to modernize the regulatory capital framework and maintain the strength of the banking system", Federal Reserve press release, 19 March 2026. https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260319a.htm
10. "Fact Sheet: Proposals to Modernize the Regulatory Capital Framework", Federal Reserve/FDIC/OCC, 19 March 2026. https://www.federalreserve.gov/newsevents/pressreleases/files/fact-sheet-20260319.pdf
11. Federal Reserve press release index (banking and consumer regulatory policy), accessed 2026-10-03; includes "Agencies request comment on proposed rules to strengthen capital requirements for large banks", 27 July 2023. https://www.federalreserve.gov/newsevents/pressreleases/bcreg20230727a.htm
