# Basel credit risk mitigation for project lending: guarantees, ECA and credit insurance cover, the 0% MDB list, large exposures, the NSFR and the Basel output-floor phase-in

As of: 2026-10-03. Latest documents covered: Basel Framework chapters CRE20, CRE22, RBC90, LEX20/30 and NSF30 as published on bis.org (including the CRE22 version published 28 October 2025, effective 1 November 2028), and the EU CRR consolidated text of 1 January 2025.

## Summary

Banks lending to projects reduce their capital requirement by getting someone stronger to stand behind the borrower. Under the Basel standardised approach (CRE22), an eligible guarantee or credit derivative lets the bank **substitute** the protection provider's risk weight for the borrower's on the covered portion. The uncovered portion keeps the borrower's weight.

To qualify, the protection must be:

- direct, explicit, irrevocable and unconditional;
- callable without first suing the borrower;
- for guarantees, covering all payment types, or else recognised only proportionally.

Eligible providers include:

- sovereigns, public sector entities (PSEs) and multilateral development banks (MDBs);
- banks and other prudentially regulated financial institutions, explicitly including regulated insurers;
- in some cases rated corporates.

An export credit agency (ECA) guarantee is therefore typically treated as a guarantee by the sovereign behind it. In the EU, such guarantees of officially supported export credits are also eligible for exemptions in the large-exposures and leverage-ratio rules.

Sixteen named MDBs, including the World Bank Group entities, the regional development banks, the EIB and AIIB, carry a **0% risk weight** in both the Basel framework and the EU CRR. Cover from them is as good as cover from a top-rated sovereign.

Long-tenor project loans also consume liquidity capacity. Under the **net stable funding ratio** (NSFR, minimum 100%), a performing loan of a year or more to a non-financial borrower needs 85% stable funding, or 65% if it would qualify for a 35% or lower risk weight.

**Large-exposure** rules cap exposure to one client or connected group at 25% of Tier 1 capital, measured after eligible credit risk mitigation.

Basel's own **output floor** phases in from 50% on 1 January 2023 to 72.5% on 1 January 2028. The EU runs a later schedule, 2025–2030 (see t-basel).

## Verified facts

### Guarantee substitution under the Basel standardised approach (CRE22)

1. **Substitution principle (CRE22.70, 22.79).**
   - Banks may substitute the guarantor's risk weight for the counterparty's if the conditions are met.
   - The protected portion takes the protection provider's weight; the uncovered portion keeps the counterparty's.
   - A materiality threshold below which the provider does not pay is treated as a retained first loss and weighted at 1250%.
   - Only protection from an entity with a lower risk weight than the counterparty reduces capital (CRE22.23).

   [confidence: high] [source: 1]
2. **Core requirements (CRE22.71).** A guarantee or credit derivative must:
   - be a direct claim on the provider;
   - be explicitly referenced to specific exposures so the cover is "clearly defined and incontrovertible";
   - be irrevocable, apart from non-payment of the protection premium;
   - contain no clause letting the provider unilaterally cancel cover, change maturity, or raise its cost as credit quality deteriorates;
   - be unconditional, with no clause outside the bank's direct control that could prevent timely payment when the obligor defaults.

   [confidence: high] [source: 1]
3. **Guarantee-specific requirements (CRE22.73).**
   - On default, the bank may pursue the guarantor in a timely manner, without first taking legal action against the obligor.
   - The guarantor may pay a lump sum or assume the obligor's future payments.
   - The guarantee must be explicitly documented.
   - It must cover all payment types. If it covers principal only, interest and other uncovered amounts are treated as unsecured.

   [confidence: high] [source: 1]
4. **Proportional and tranched cover (CRE22.80–22.81).** Pro rata loss sharing earns proportional relief. Tranched protection of different seniority falls under the securitisation framework. [confidence: high] [source: 1]
5. **Currency mismatch (CRE22.82–22.83).** Where protection is in a different currency from the exposure, the protected amount is reduced by a haircut of 8% for a 10-business-day holding period, scaled by the square root of time to the revaluation frequency. [confidence: high] [source: 1]
6. **Eligible providers (CRE22.76).**
   - Sovereigns (including the BIS, IMF, ECB, EU, ESM, EFSF and 0%-weighted MDBs, per footnote 10), PSEs, MDBs, banks, securities firms and other prudentially regulated financial institutions with a lower risk weight than the counterparty.
   - Footnote 11 says prudentially regulated institutions "include, but are not limited to, prudentially regulated insurance companies".
   - Where external ratings are used: other externally rated entities, including parents and affiliates with a lower risk weight.
   - Where they are not: investment-grade entities meeting listed conditions.

   [confidence: high] [source: 1]
7. **Sovereign counter-guarantees (CRE22.84).** An exposure guaranteed by an entity that is itself counter-guaranteed by a sovereign may be treated as sovereign-guaranteed if three conditions hold:
   - the counter-guarantee covers all credit risk elements;
   - both guarantees meet the operational requirements, though the counter-guarantee need not be direct;
   - the supervisor is satisfied the cover is robust.

   [confidence: high] [source: 1]
8. **Forthcoming CRE22 text.** The Basel Committee published a CRE22 version on 28 October 2025, effective 1 November 2028. It restates CRE22.79: the unprotected portion takes the counterparty's risk weight "without consideration of the credit protection". It adds a cross-reference to CRE51.18 for fixed or capped protection on derivative counterparty exposures. [confidence: high] [source: 2]

### ECA cover and sovereign risk weights

9. **ECA country risk scores (CRE20.9).** Supervisors may let banks risk-weight sovereign exposures using country risk scores published by ECAs that subscribe to the OECD-agreed methodology, or the consensus scores of Participants to the OECD Arrangement on Officially Supported Export Credits:

   | ECA score | 0–1 | 2 | 3 | 4–6 | 7 |
   |---|---|---|---|---|---|
   | Risk weight | 0% | 20% | 50% | 100% | 150% |

   [confidence: high] [source: 3]
10. **EU equivalent (CRR Article 137).**
    - EU institutions may use ECA credit assessments that are either a consensus risk score of ECAs participating in the OECD Arrangement, or published by an ECA subscribing to the OECD methodology and tied to one of its eight minimum export insurance premium (MEIP) categories.
    - CRR Table 9 maps MEIP categories to risk weights:

      | MEIP category | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
      |---|---|---|---|---|---|---|---|---|
      | Risk weight | 0% | 0% | 20% | 50% | 100% | 100% | 100% | 150% |

    - The CRR defines "officially supported export credits" as loans or credits financing exports of goods and services for which an official ECA provides guarantees, insurance or direct financing (Article 4(1)(81)).

    [confidence: high] [source: 4]
11. **EU large-exposure and leverage-ratio treatment of ECA-backed exposures.**
    - Under Article 400(2)(l), competent authorities may exempt from the large-exposure limit exposures in the form of a guarantee for officially supported export credits by an ECA rated at least the lower of credit quality step 2 and its home Member State's sovereign rating.
    - Under Article 429a, the guaranteed parts of export-credit exposures may be excluded from the leverage-ratio exposure measure where the guarantee comes from an eligible provider, including an ECA or central government, and attracts a 0% risk weight.

    [confidence: high] [source: 4]

### Credit insurance and political risk insurance

12. **EU eligible providers (CRR Article 201(1)).** Eligible providers of unfunded credit protection include:
    - central governments and central banks;
    - regional and local authorities;
    - MDBs;
    - 0%-weighted international organisations;
    - PSEs;
    - institutions;
    - "regulated financial sector entities" (point (fa), added by CRR3);
    - rated other undertakings (not for securitisation exposures);
    - qualifying central counterparties.

    IRB banks may also use internally rated corporates (Article 201(2)). Guarantees are eligible unfunded credit protection (Article 203). [confidence: high] [source: 4]
13. **EU requirements (CRR Articles 213 and 215).** Protection must be:
    - direct, clearly set out and incontrovertible;
    - free of clauses outside the lender's control that would allow unilateral cancellation, raise the cost on credit deterioration, prevent timely payout, or let the provider shorten maturity;
    - legally effective in all relevant jurisdictions.

    Two CRR3 additions matter for insurance policies:
    - A clause providing that "flawed due diligence or fraud by the lending institution" cancels or reduces cover does not disqualify the protection (Article 213(1)).
    - Payment by the guarantor "shall not be subject to the lending institution first having to pursue the obligor" (Article 215(1)).

    For guarantees by or counter-guaranteed by sovereigns, PSEs or 0% MDBs (Article 214(2)), timeliness can be met through a provisional payment mechanism (Article 215(2)). [confidence: high] [source: 4]
14. **EBA mandate on credit insurance (CRR Article 506).** CRR3 required the EBA, in close cooperation with EIOPA, to report to the Commission by 30 June 2024 on the eligibility and use of credit insurance as a credit risk mitigation technique, including risk parameters and observed riskiness. [confidence: high] [source: 4]

### MDB 0% risk-weight list

15. **Basel list (CRE20.14, footnote 8).** MDBs currently eligible for 0%:
    - the World Bank Group: IBRD, IFC, MIGA and IDA;
    - the Asian Development Bank;
    - the African Development Bank;
    - EBRD;
    - the Inter-American Development Bank;
    - EIB and EIF;
    - the Nordic Investment Bank;
    - the Caribbean Development Bank;
    - the Islamic Development Bank;
    - the Council of Europe Development Bank;
    - the International Finance Facility for Immunization;
    - the Asian Infrastructure Investment Bank.

    That is 16 entities. [confidence: high] [source: 3]
16. **Basel eligibility criteria (CRE20.14).**
    - A majority of external ratings AAA (an applicant must be AAA when applying; once listed, a downgrade to no lower than AA- is tolerated, per footnote 9).
    - Significant AA- or better sovereign shareholding, or mainly paid-in capital with little leverage.
    - Strong shareholder support (paid-in and callable capital, continued contributions).
    - Adequate capital and liquidity.
    - Strict statutory lending requirements and conservative financial policies.

    [confidence: high] [source: 3]
17. **Other MDBs (CRE20.15, Table 5).** By external rating:

    | Rating | AAA to AA- | A+ to A- | BBB+ to BBB- | BB+ to B- | Below B- | Unrated |
    |---|---|---|---|---|---|---|
    | Risk weight | 20% | 30% | 50% | 100% | 150% | 50% |

    Jurisdictions that do not use external ratings weight them at 50%. [confidence: high] [source: 3]
18. **EU list (CRR Article 117(2), consolidated to 1 January 2025).** The same 16 MDBs receive 0%:
    - (a)–(n): IBRD, IFC, IDB, ADB, AfDB, CEB, NIB, CDB, EBRD, EIB, EIF, MIGA, IFFIm and IsDB;
    - (o)–(p), added by CRR2: IDA and AIIB.

    The Commission may amend the list by delegated act in line with international standards. Other MDBs get 20–150% by credit quality step, or 50% unrated (Article 117(1), Table 1). The CRR names the Inter-American Investment Corporation, the Black Sea Trade and Development Bank, the Central American Bank for Economic Integration and CAF as MDBs, but not 0%-weighted ones. [confidence: high] [source: 4]

### Large exposures

19. **Basel limit (LEX20).**
    - Exposure to a single counterparty or group of connected counterparties must not exceed 25% of Tier 1 capital at all times; 15% for a G-SIB's exposure to another G-SIB.
    - Banks must report exposures of 10% or more of Tier 1 (measured with and without credit risk mitigation) and their 20 largest exposures.

    [confidence: high] [source: 5]
20. **Mitigation and sovereign exemption (LEX30).**
    - Recognised unfunded protection reduces the exposure to the original counterparty but creates an equivalent exposure to the protection provider (substitution).
    - Exposures to sovereigns and their central banks, and PSEs treated as sovereigns, are exempt.
    - Any portion guaranteed by such entities is likewise exempt.
    - Entities controlled by, or economically dependent on, an exempt sovereign need not be treated as connected merely for that reason.

    [confidence: high] [source: 6]
21. **EU limit (CRR Article 395(1)).** 25% of Tier 1 after credit risk mitigation. For exposures to institutions, the limit is the higher of 25% of Tier 1 and EUR 150 million, subject to a cap on non-institution connected clients. Article 400(1) exempts claims on, or explicitly guaranteed by, central governments, 0%-weighted international organisations and MDBs, and PSEs, where unsecured they would be weighted 0%. [confidence: high] [source: 4]

### Net stable funding ratio

22. **Standard.** The Basel Committee published the NSFR in October 2014. It was to become a minimum standard by 1 January 2018. Available stable funding must equal at least 100% of required stable funding on an ongoing basis. [confidence: high] [source: 7]
23. **Required stable funding factors for loans (NSF30).**

    | Asset (unencumbered, residual maturity one year or more) | RSF factor |
    |---|---|
    | Performing loans to non-financials, sovereigns, MDBs, PSEs and national development banks that would qualify for a 35% or lower standardised risk weight | 65% |
    | Other performing loans that do not qualify for a 35% or lower weight (excluding loans to financial institutions) | 85% |
    | Encumbered for a year or more, non-performing loans, loans to financial institutions of a year or more | 100% |
    | Undrawn irrevocable or conditionally revocable credit and liquidity facilities | 5% |

    [confidence: high] [source: 8, 7]
24. **Available stable funding (NSF30.10).** Liabilities and capital instruments with effective residual maturity of one year or more receive a 100% ASF factor. Cash flows within one year of longer-dated liabilities do not. [confidence: high] [source: 8]
25. **EU NSFR (CRR Article 428b).** Institutions must maintain an NSFR of at least 100%, calculated in the reporting currency across all transactions. CRR Article 428ag sets the 85% RSF category. [confidence: high] [source: 4]

### Output floor phase-in (Basel)

26. **Original 2017 schedule (Basel III finalisation, December 2017).** Implementation was set for 1 January 2022, with the output floor at 50% (2022), 55% (2023), 60% (2024), 65% (2025), 70% (2026) and 72.5% (1 January 2027). [confidence: high] [source: 9]
27. **One-year deferral (27 March 2020).** The Group of Central Bank Governors and Heads of Supervision deferred implementation by one year to 1 January 2023, and extended the output floor transition by one year to 1 January 2028, to free capacity for responding to Covid-19. [confidence: high] [source: 10]
28. **Current schedule (RBC90.1).**

    | Date | Floor |
    |---|---|
    | 1 January 2023 | 50% |
    | 1 January 2024 | 55% |
    | 1 January 2025 | 60% |
    | 1 January 2026 | 65% |
    | 1 January 2027 | 70% |
    | 1 January 2028 | 72.5% |

    During the phase-in, supervisors may cap the floor-driven increase in a bank's RWA at 25% of its pre-floor RWA (RBC90.2). [confidence: high] [source: 11]
29. **Full floor (RBC20).** From 1 January 2028 a bank's RWA is the higher of its modelled RWA and 72.5% of RWA calculated using only standardised approaches. The minimum ratios are 4.5% CET1, 6% Tier 1 and 8% total capital, plus a 2.5% capital conservation buffer. [confidence: high] [source: 12]
30. **Specialised lending definition change.** In the CRE20 version effective 1 January 2028 (published 10 June 2025), an exposure is treated as specialised lending if it has "all", rather than "some or all", of the listed characteristics. [confidence: high] [source: 3]

## Timeline

- **October 2014:** NSFR standard published; minimum standard by 1 January 2018. [source: 7]
- **December 2017:** Basel III finalisation; output floor 50% (2022) to 72.5% (2027). [source: 9]
- **27 March 2020:** GHOS defers implementation to 2023; floor transition to 2028. [source: 10]
- **1 January 2023:** Basel floor 50%. [source: 11]
- **1 January 2025:** EU CRR3 applies; EU floor starts at 50% (see t-basel). Basel floor 60%. [source: 11]
- **10 June 2025:** CRE20 version effective 2028 published (specialised lending "all" characteristics). [source: 3]
- **28 October 2025:** CRE22 version effective 1 November 2028 published. [source: 2]
- **1 January 2026:** Basel floor 65%. [source: 11]
- **1 January 2028:** Basel floor 72.5% (fully phased). [source: 11]

## Financing and structure details

Not a transaction. Structural points for a typical ECA-covered project loan follow from the rules above. They are illustrations, not quoted market practice.

- **Tranche-by-tranche capital.** A commercial bank in an ECA-covered tranche with 95% comprehensive cover from an ECA backed by a sovereign weighted 0%:
  - weights the covered 95% at the sovereign's risk weight, subject to the operational requirements and any currency haircut;
  - weights the uncovered 5% at the project's own weight (for example 100–130% standardised, or a slotting weight; see t-basel).

  The same bank's uncovered commercial tranche carries the full project weight.
- **MDB A/B loans and guarantees.** Cover from a listed MDB (0%) is as capital-efficient as top-rated sovereign cover. Cover from an unlisted MDB is weighted by its rating (Table 5). See t-dfis for preferred creditor status and B-loans.
- **Private credit and political risk insurance.** Policies from regulated insurers can be eligible unfunded protection in principle (facts 6, 12). Recognition turns on the policy wording meeting the "direct, irrevocable, unconditional, pay without first pursuing the obligor" tests (facts 2–3, 13). Comprehensive non-payment policies are written to try to meet them. Political-risk-only policies cover defined perils, so whether, and how far, they can be recognised as credit risk mitigation is a legal and supervisory question for each bank. This is why the EU asked the EBA to study credit insurance (fact 14).
- **Large exposures.** Large lenders can hold bigger tickets in sovereign-ECA-backed tranches because the guaranteed part is exempt or shifted to the sovereign (facts 20–21).
- **Liquidity cost of tenor.** An 18-year project loan sits in the 85% RSF bucket for most of its life. A sovereign-guaranteed loan qualifying for a 35% or lower weight could fall into the 65% bucket (fact 23). Banks must fund these assets with stable funding of a year or more, which is one reason banks prefer shorter tenors, mini-perms and take-outs.

## What went wrong or right, and why

- **Why the floor transition slipped.** The GHOS deferred Basel III by one year in March 2020 explicitly to increase banks' and supervisors' operational capacity to respond to Covid-19. It said the revised timeline was not expected to dilute capital strength (fact 27). The EU and UK then set later dates of their own (see t-basel). [source: 10]
- **Why substitution is strict.** The Basel text requires protection to be unconditional and payable in a timely manner without legal action against the obligor (facts 2–3), because capital relief assumes the bank will actually be paid when the borrower defaults. CRR3's changes on fraud and due-diligence clauses, and on not having to pursue the obligor first (fact 13), address features of credit insurance contracts that previously cast doubt on eligibility. [source: 1, 4]

## Teaching angles by chapter

**Chapter 68 (Capital rules for banks and insurers).**

- Use Castellan Bank's Case P exposures to compute capital tranche by tranche:
  - the ECA-covered tranche: substitution on the covered share, project weight on the uncovered share;
  - the PRI-insured tranche: whether the policy wording passes CRE22.71/73 or CRR Articles 213/215;
  - the uncovered commercial tranche.
- Show how a 0%-listed MDB guarantor differs from an unlisted one.
- Add the NSFR (85% versus 65%) and large-exposure lenses to explain why banks favour covered tranches, shorter tenors and club deals.
- Close with the Basel output-floor schedule (50% in 2023 to 72.5% in 2028), contrasted with the EU's 2025–2030 schedule. This is why modelled slotting benefits shrink over time.

## Do not state

- That all ECA cover automatically earns a 0% risk weight. The covered portion takes the weight of the ECA or its sovereign, which depends on that sovereign's rating or ECA score, the currency, and whether the operational requirements are met.
- That political risk insurance is generally recognised as credit risk mitigation. Not verified; it depends on the policy terms and the supervisor.
- The content or conclusions of the EBA's Article 506 report on credit insurance (due 30 June 2024). Not retrieved.
- Any MDB added to the CRR 0% list after the 1 January 2025 consolidation, or any addition to the Basel list after the CRE20 text reviewed (for example the New Development Bank). Not verified.
- The EU NSFR application date (commonly given as 28 June 2021 under CRR2). Not verified for this sheet.
- UK (PRA) equivalents of these rules. Not verified here.
- That the specialised-lending wording change effective 2028 ("all" characteristics) changes any project's classification. Its practical effect was not verified.

## Sources

1. Basel Committee on Banking Supervision, Basel Framework, CRE22 "Standardised approach: credit risk mitigation", version effective 1 January 2023 (published 26 November 2020). https://www.bis.org/committees/bcbs/basel-framework/standard/cre/22/inforce/2023-01-01/published/2020-11-26
2. Basel Framework, CRE22, version effective 1 November 2028 (published 28 October 2025). https://www.bis.org/committees/bcbs/basel-framework/standard/cre/22/inforce/2028-11-01/published/2025-10-28
3. Basel Framework, CRE20 "Standardised approach: individual exposures", versions effective 1 January 2023 and 1 January 2028 (both published 10 June 2025). https://www.bis.org/committees/bcbs/basel-framework/standard/cre/20/inforce/2023-01-01/published/2025-06-10 ; https://www.bis.org/committees/bcbs/basel-framework/standard/cre/20/inforce/2028-01-01/published/2025-06-10
4. Regulation (EU) No 575/2013 (CRR), consolidated text 02013R0575 of 1 January 2025 (Articles 4(1)(81), 117, 137, 201, 203, 213–215, 395, 400, 428b, 428ag, 429a, 506), EUR-Lex. https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:02013R0575-20250101
5. Basel Framework, LEX20 "Requirements" (large exposures), effective 15 December 2019. https://www.bis.org/committees/bcbs/basel-framework/standard/lex/20/inforce/2019-12-15/published/2019-12-15
6. Basel Framework, LEX30 "Exposure measurement", effective 1 January 2023. https://www.bis.org/committees/bcbs/basel-framework/standard/lex/30/inforce/2023-01-01/published/2020-03-27
7. Basel Committee on Banking Supervision, "Basel III: the net stable funding ratio", BIS, October 2014. https://www.bis.org/publications/201410-standards-basel-iii-net-stable-funding-ratio.pdf
8. Basel Framework, NSF30 "Available and required stable funding" (version published 5 July 2024). https://www.bis.org/committees/bcbs/basel-framework/standard/nsf/30/inforce/2019-12-15/published/2024-07-05
9. Basel Committee on Banking Supervision, "Basel III: Finalising post-crisis reforms", BIS, December 2017 (implementation table, p. 2). https://www.bis.org/publications/201712-standards-basel-iii-finalising-post-crisis-reforms.pdf
10. "Governors and Heads of Supervision announce deferral of Basel III implementation to increase operational capacity of banks and supervisors to respond to Covid-19", BIS press release, 27 March 2020. https://www.bis.org/press/p200327.htm
11. Basel Framework, RBC90 "Transitional arrangements" (output floor), effective 1 January 2023, last updated 27 March 2020. https://www.bis.org/committees/bcbs/basel-framework/standard/rbc/90/inforce/2023-01-01/published/2020-03-27
12. Basel Framework, RBC20 "Calculation of minimum risk-based capital requirements", effective 1 January 2023. https://www.bis.org/committees/bcbs/basel-framework/standard/rbc/20/inforce/2023-01-01/published/2020-11-26
