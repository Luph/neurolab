# Rating agency project finance methodologies, part 2: S&P and Moody's criteria, and project finance default and recovery statistics

As of: 2026-10-03. Latest events covered: S&P "General Project Finance Rating Methodology" (14 December 2022), last republished with nonmaterial changes on 19 December 2025. Moody's "Default and recovery rates for project finance bank loans, 1983-2021" (4 April 2023), the latest edition verified. S&P "2023 Annual Infrastructure Default And Rating Transition Study" (11 September 2024).

## Summary

This sheet adds to t-ratings.md, which covers Fitch. The S&P material comes from the full criteria text. S&P Global Ratings Maalot, S&P's Israeli rating subsidiary, republishes the criteria as PDFs on its public website, and those copies were read in full.

S&P rates project finance debt under a "General Project Finance Rating Methodology" published on 14 December 2022, together with a "Sector-Specific Project Finance Rating Methodology" of the same date. The 2022 criteria replaced the 2013-2014 suite of project finance criteria (framework, construction, operations and transaction structure).

The method runs in this order:
- S&P checks that minimum structural features are present.
- It derives an operations phase stand-alone credit profile (SACP). It first maps an operations phase business assessment (OPBA, scale 1-12) against the forecast minimum base-case debt service coverage ratio (DSCR) in a published table. It then applies modifiers for resiliency in a downside scenario, median DSCR, debt structure, liquidity, refinancing risk and future value.
- It derives a construction phase SACP from a construction phase business assessment (CPBA, 1-6) and a construction phase financial assessment (CPFA, 1-6). The CPFA rests on ratios of funding sources to downside-case uses.
- It takes the lower of the two phase SACPs.
- It then adjusts for parent linkage, sovereign and other external influences, and guarantees.

Moody's primary methodology documents were not accessible: ratings.moodys.com returned a bot challenge, which was not bypassed. Moody's "Generic Project Finance Methodology" scorecard is known here from a secondary source that reproduces the exhibit (Center for Public Enterprise, September 2024). It shows three factors: Business Profile 50%, Operating Risk 20% and Leverage and Coverage 30%. DSCR carries 30% for amortizing debt, with rating-category thresholds that vary by project risk.

For default and recovery data, Moody's publishes an annual study of unrated project finance bank loans built on a lender data consortium. The April 2023 edition covers 10,452 projects from 1983 to 2021. It reports a 10-year cumulative default rate of 4.8% on the Basel definition and 3.3% on Moody's definition, and an average ultimate recovery of 79.5% (Basel). Recovery was 100% in 62% of cases. Construction-phase defaults recovered less on average than operations-phase defaults.

## Verified facts

### A. S&P Global Ratings: criteria architecture and dates (global; current criteria listed at disclosure.spglobal.com/ratings/en/regulatory/ratings-criteria)

1. **Current criteria.** S&P's current global project finance criteria are "General Project Finance Rating Methodology", originally published 14 December 2022 and effective that date (except where local registration was required). S&P republished the article with nonmaterial changes on 2 June 2023, 19 December 2023, 5 June 2024, 14 March 2025 and 19 December 2025. [confidence: high] [source: 1, 2, 3]
2. **Companion documents.** Sector-specific credit factors and assumptions sit in a companion "Sector-Specific Project Finance Rating Methodology", also dated 14 December 2022. A "Sector And Industry Variables: Project Finance Rating Methodology" report of the same date was published too. On 5 June 2024 its content was moved, without substantive change, into an Appendix of the general criteria. [confidence: high] [source: 1, 2, 4]
3. **Consultation.** The 2022 criteria followed a "Request For Comment: Project Finance Rating Methodology" published 9 August 2022. An "RFC Process Summary" was published 14 December 2022. [confidence: high] [source: 2]
4. **What the 2022 criteria fully superseded.** [confidence: high] [source: 2]
   - Project Finance Framework Methodology (16 September 2014).
   - Project Finance Transaction Structure Methodology (16 September 2014).
   - Project Finance Operations Methodology (16 September 2014).
   - Project Finance Construction Methodology (15 November 2013).
   - Project Finance Construction and Operations Counterparty Methodology (20 December 2011).
   - Single-Sponsor Pension Plan Risk Assessments For Project Finance Funding Commitments (16 December 2014).
   - Methodology For Assessing Project Finance Debt Instruments With Deferrable Features, Such As Those Issued Under TIFIA (27 September 2019).
5. **Scope.** The criteria apply to transactions with these features:
   - Debt is primarily serviced from the project's cash flow available for debt service (CFADS), with limited or no recourse to sponsors.
   - Debtholders typically hold a senior security interest.
   - A cash management structure sets the priority of payments.
   - Covenants restrict what the project can do.

   Projects with unsustainable commitments are rated under S&P's 'CCC' criteria instead. [confidence: high] [source: 1]

### B. S&P: operations phase SACP

6. **Five steps.** [confidence: high] [source: 1]
   1. Determine the OPBA.
   2. Run a base case and find the forecast minimum DSCR through the operations phase.
   3. Combine the two into the preliminary operations phase SACP.
   4. Apply modifiers and caps for resiliency, debt structure, liquidity, refinancing risk and future value.
   5. Apply a holistic adjustment, the structural protection analysis and counterparty constraints.
7. **What the OPBA measures.** The OPBA runs from 1 (lowest risk) to 12. It reflects S&P's view of cash flow volatility and combines performance risk, market risk and country risk. [confidence: high] [source: 1]
   - **Performance risk** starts from an "asset class operations stability" (ACOS) score of 1-10. That score is adjusted for six project-specific attributes: performance redundancy, operating leverage, O&M management, technological performance, performance standards and other operational risks. It is also adjusted for regulatory risk, management and governance risk, and resource risk.
   - The attribute adjustment is capped at +3, or −2 for more complex assets (−1 where ACOS is 3 or lower).
   - Resource risk assessed "high" adds 2 to 3 to the ACOS. For renewables, S&P typically adds 2 where long-term volume variance is estimated at 10%-20%, and 3 where it is 20%-30%.
8. **Market exposure.** S&P measures market exposure by the projected decline in CFADS from the base case to a "market exposure case". [confidence: high] [source: 1]

   | Decline in CFADS | Assessment | S&P's typical examples |
   |---|---|---|
   | <5% | not applicable | availability or fixed-price projects |
   | 5%-15% | low | mature toll road with traffic risk |
   | 15%-30% | medium | |
   | 30%-50% | high | partly contracted merchant power or gas processing |
   | >50% | very high | mines, refineries, merchant power in volatile markets |

   The market stress is typically applied for up to five years, starting at the project's most vulnerable point.
9. **Country risk.** S&P's country risk assessment (1-6) is neutral at 1-3 and worsens the OPBA at 4-6. It can be treated as neutral if it is effectively mitigated, for example by transferring economic risk to a counterparty or, to a lesser extent, by political risk insurance. [confidence: high] [source: 1]
10. **Minimum DSCR as the financial assessment.** S&P uses the forecast minimum base-case DSCR "as a proxy for the project's default risk". [confidence: high] [source: 1]
    - DSCR is CFADS divided by scheduled debt service, normally on a rolling 12-month basis at each payment date.
    - CFADS excludes reserve balances such as the debt service reserve account (DSRA). Narrow exceptions apply for mandatory, documented, fully funded reserve releases.
    - Revolving facilities and permitted debt baskets are generally assumed fully drawn.
    - For projects with refinancing risk, S&P also forecasts post-refinancing DSCRs and uses the lower minimum.
    - A one-off low period lasting no more than 24 months can be excluded, subject to conditions: no covenant breach, sufficient liquidity, and reversion to the base case within 24 months.
11. **The preliminary operations phase SACP table (Table 1/Table 8 of the criteria), verbatim ranges.** [confidence: high] [source: 1, 2]

    | OPBA | aa | a | bbb | bb | b |
    |---|---|---|---|---|---|
    | 1-2 | ≥1.75x | 1.75x-1.20x | 1.20x-1.10x | 1.10x-1.05x | <1.05x |
    | 3-4 | n/a | ≥1.40x | 1.40x-1.175x | 1.175x-1.10x | <1.10x |
    | 5-6 | n/a | ≥1.75x | 1.75x-1.30x | 1.30x-1.15x | <1.15x |
    | 7-8 | n/a | ≥2.50x | 2.50x-1.60x | 1.60x-1.35x | <1.35x |
    | 9-10 | n/a | ≥5.00x | 5.00x-2.50x | 2.50x-1.50x | <1.50x |
    | 11-12 | n/a | n/a | n/a | ≥3.00x | <3.00x |

    Ranges include the lower bound but not the upper; for example, 1.20x-1.10x includes 1.10x but excludes 1.20x. S&P adds a plus or minus according to where the DSCR sits in the range. In S&P's own example, an OPBA of 8 with a minimum DSCR of 2.40x would likely give 'bbb+', and an OPBA of 8 with 1.80x would likely give 'bbb-'. The table was unchanged between the December 2022 original and the December 2025 republication.
12. **Downside resiliency.** S&P builds a downside scenario that combines the market exposure case with project-level operating stresses and macroeconomic and financial stresses (interest rates, inflation, foreign exchange). For example, the downside risk-free curve adds 100-300 basis points to the base-case curve. [confidence: high] [source: 1]

    S&P grades resiliency on five levels:
    - **Very high:** DSCR always above 1.0x, an exceptional cushion, and downside DSCRs mapping to at least the 'bbb' category in most periods ('bb' if liquidity reserves are stronger).
    - **High:** DSCR always above 1.0x, and downside DSCRs mapping to at least 'bb' in most periods ('b' with stronger reserves).
    - **Moderate:** DSCR generally above 1.0x. If it falls below 1.0x, reserves cover debt service for at least five years.
    - **Modest:** limited confidence that DSCR stays above 1.0x, but the project survives at least three years before reserves run out.
    - **Low:** reserves are likely depleted by year three.

    "Stronger liquidity reserves" means at least one year of debt service or at least 5% of total project debt.
13. **Resiliency adjustments (Table 10).** [confidence: high] [source: 1]

    | Base-case SACP | Very high | High | Moderate | Modest | Low |
    |---|---|---|---|---|---|
    | 'a' or higher | +1 | none | cap at 'bbb' category | cap at 'bb' category | cap at 'b' category |
    | 'bbb' | +2 | +1 | none | cap at 'bb' category | cap at 'b' category |
    | 'bb' | +2 | +2 | +1 | none | cap at 'b' category |
    | 'b' | +2 | +2 | +2 | +1 | none |

    A median base-case DSCR that maps to a higher category than the minimum can add one further notch. This does not apply where the DSCR trajectory is declining. In rare cases, such as ramp-up projects with strong dedicated reserves, S&P "rates to the downside": the resiliency outcome alone sets the preliminary SACP (very high or high = 'a', moderate = 'bbb', modest = 'bb', low = 'b').
14. **Other operations-phase modifiers.** [confidence: high] [source: 1]
    - **Debt structure:** 0 to −3 notches. Triggers include material reliance on cash sweeps, excessive leverage, back-ended amortization, high inflation exposure, and amortization sculpted to uncertain capex. Where minimal amortization and material sweep dependence apply, the cut is at least two notches for 'bbb' or higher, and at least one for 'bb'.
    - **Liquidity:** strong (+1), neutral (0) or less than adequate (at least −1), over a 12-month horizon. "Less than adequate" applies in any of these cases:
      - sources do not cover the next 12 months' debt service by at least 1x;
      - there is no DSRA, or the DSRA is insufficient;
      - covenant headroom is thin, meaning a CFADS decline of 15% or less (OPBA 5-12) or 10% or less (OPBA 1-4) would breach a covenant;
      - reserves are not funded upfront or not replenished;
      - distribution tests are absent and the absence is not mitigated.
    - **Refinancing risk:** rating caps set by the project life coverage ratio (PLCR) at refinancing and by cash flow stability:
      - PLCR below 1.1x caps at 'bb+' for OPBA 1-4, 'b+' for OPBA 5-8 and 'b-' for OPBA 9-12.
      - PLCR of 1.1x-1.5x caps at 'bb+' for OPBA 5-8 and 'b+' for OPBA 9-12.
      - PLCR of 1.5x-3.0x caps at 'bb+' for OPBA 9-12 only.
      - PLCR of 3.0x or above: no cap.
    - **Future value:** up to +1. It requires no refinancing need and a tail of at least 10 years and at least 20% of the original debt tenor.
    - S&P does not expect the cumulative effect of the modifiers to raise the SACP by more than one rating category, "although it is possible".
15. **Construction phase SACP.** [confidence: high] [source: 1]
    - **What the CPBA covers (scale 1-6):** construction difficulty (scale 1-5, from a school at the simple end to a nuclear plant at the difficult end), technology and design, stakeholder experience, contract type and risk allocation, project management, progress to date, and country risk. The CPBA is capped at 6 in two cases: a negative risk-allocation assessment combined with inexperienced contractors, or difficulty of 4-5 with only preliminary design at financial close.
    - **What the CPFA measures (scale 1-6):** funding sources against uses in a downside scenario that includes likely delays and overruns.
    - **Core ratio (certain sources ÷ downside uses):** ≥1.15x = 1; 1.00x-1.15x = 2; 0.90x-1.00x = 3; 0.80x-0.90x = 4; 0.50x-0.80x = 5; <0.50x = 6.
    - **Supplemental ratio (certain plus likely sources ÷ downside uses):** ≥1.30x = 1; 1.15x-1.30x = 2; 1.05x-1.15x = 3; 1.025x-1.05x = 4; 1.00x-1.025x = 5; <1.00x = 6. It can improve the CPFA by one. A supplemental score of 6 caps the preliminary construction SACP at 'b-'.
    - **Combination:** a published table combines CPBA and CPFA. For example, CPBA 1 with CPFA 1 gives 'a+'; CPBA 4 with CPFA 4 gives 'bb'; CPFA 6 gives 'b-' at every CPBA.
    - **Credit substitution:** if a third party guarantees all construction obligations, including performance, shortfall funding and debt repayment on non-completion, S&P substitutes the guarantor's credit quality.
16. **Combining the phases.** The preliminary project SACP is the lower of the construction and operations phase SACPs. After completion it reverts to the operations phase SACP. S&P's example: construction 'bb+' and operations 'bbb-' give 'bb+' during construction and 'bbb-' after sign-off. S&P then applies parent linkage:
    - **Delinked:** the parent does not constrain the project.
    - **Linked:** the project can be up to three notches above the parent.
    - **Capped:** the project can be no higher than the parent.

    Finally, S&P considers external influences: government support or intervention, sovereign risk and full guarantees. [confidence: high] [source: 1]
17. **Recovery ratings.** S&P assigns recovery ratings ('1+' to '6') only when the senior debt is rated 'BB+' or lower and the jurisdiction is Group A or B under its jurisdiction ranking criteria. Unlike for corporates, project finance recovery ratings do not affect the issue rating. [confidence: high] [source: 1]
18. **Internal inconsistency in the S&P text.** S&P's Section 1 overview says greater resiliency may raise the preliminary SACP "by up to three notches". Section 3 says a highly resilient project may be "up to two notches above" it. Table 2 shows up to +2 for the resiliency assessment plus 0 to +1 for median DSCR. Writers should cite the tables. [confidence: high] [source: 1]

### C. Moody's: generic project finance methodology (global; current methodology at ratings.moodys.com, methodology list)

19. **Title and version.** Moody's publishes a "Generic Project Finance Methodology". A 2022 version (cited by the Center for Public Enterprise as Medina, John, et al., 2022) is now labelled "OUTDATED METHODOLOGY" in Moody's online library, which means a later version has replaced it. That later version's date and content could not be accessed. [confidence: medium] [source: 8, 9]
20. **Scorecard, as reproduced from Moody's 2022 exhibit "Generic Project Finance Scorecard".** [confidence: medium; secondary reproduction of a Moody's exhibit, superseded version] [source: 8]

    | Factor (weight) | Sub-factor | Amortizing debt | Non-amortizing debt |
    |---|---|---|---|
    | Business Profile (50%) | Market Position | 25% | 25% |
    | | Predictability of Net Cash Flows | 25% | 25% |
    | Operating Risk (20%) | Technology | 5% | 5% |
    | | Capital Reinvestment | 5% | 5% |
    | | Operating Track Record | 5% | 5% |
    | | Operator and Sponsor Experience, Quality and Support | 5% | 5% |
    | Leverage and Coverage (30%) | DSCR | 30% | 15% |
    | | Project Cash from Operations / Adjusted Debt | none | 15% |

    The notching factors that follow the preliminary outcome are: Liquidity; Structural Features; Refinancing Risk; Construction and Ramp-up Risk; and Priority of Claim, Structural Subordination and Double Leverage. Off-taker Risk then acts as a potential constraint before the scorecard-indicated outcome.
21. **DSCR thresholds, amortizing debt (2022 exhibit, as reproduced).** For "DSCR (Cost Recovery)" projects, DSCR is scored at the level of the off-taker's credit quality. The other three rows are: [confidence: medium] [source: 8]

    | DSCR row | Aaa | Aa | A | Baa | Ba | B | Caa | Ca |
    |---|---|---|---|---|---|---|---|---|
    | Low | ≥5x | 3.5x-5x | 2x-3.5x | 1.4x-2x | 1.15x-1.4x | 1.05x-1.15x | 1x-1.05x | <1x |
    | Medium | ≥7x | 5x-7x | 3.5x-5x | 2x-3.5x | 1.4x-2x | 1.2x-1.4x | 1.1x-1.2x | <1.1x |
    | High | ≥10x | 7x-10x | 5x-7x | 3.5x-5x | 2x-3.5x | 1.4x-2x | 1.2x-1.4x | <1.2x |

    The same source says Moody's uses the average DSCR over the debt life for this sub-factor.
22. **Power generation projects.** Moody's separate "Power Generation Projects" methodology (cited as Sabatelle et al., 2024) weights Leverage and Coverage at 35%. The DSCR grid reads: Aa ≥3.5x; A 1.9x-3.5x; Baa 1.4x-1.9x; Ba 1.2x-1.4x; B 1.1x-1.2x; Caa 1.0x-1.1x; Ca <1.0x. [confidence: medium] [source: 8]

### D. Project finance default and recovery statistics

23. **Moody's latest verified study.** Moody's "Default and recovery rates for project finance bank loans, 1983-2021" (Data Report, 4 April 2023) is the 13th annual edition. Its data come from the Moody's Analytics Data Alliance Project Finance Data Consortium of lenders. It covers 10,452 projects originated 1 January 1983 to 31 December 2021, about 67% of all project finance transactions originated globally in that period. It counts 645 defaults on the Basel definition and 455 on Moody's definition. [confidence: high] [source: 5]
24. **Headline results of the 1983-2021 study.** [confidence: high] [source: 5]
    - The average 10-year cumulative default rate (CDR) was 4.8% on the Basel definition, the lowest since the study began, down from 5.3% in the March 2022 study (1983-2020). It was 3.3% on Moody's definition.
    - For comparison, Moody's cites average 10-year CDRs of 4.8% for Baa3-rated companies and 8.5% for Ba1-rated companies.
    - Marginal annual default rates resemble high speculative grade in the first three years, and trend toward the single-A category by year seven from cohort formation.
    - Most defaults occur in the early years of operations.
25. **Recovery results of the 1983-2021 study.** [confidence: high] [source: 5]
    - Average ultimate recovery was 79.5% (Basel) and 76.9% (Moody's).
    - The most likely outcome is 100% recovery (no economic loss), which occurred in 62% of cases.
    - Workouts recovered more than distressed sales.
    - Senior secured corporate bank loans in Moody's data set averaged 83.1% recovery between 1987 and 2021, against 78.9% for all corporate bank loans.
26. **Defaults and recoveries by phase (1983-2021, Exhibit 44).** [confidence: high] [source: 5]

    | Phase | Basel defaults | Avg years to default | Avg ultimate recovery (Basel) | Moody's-definition defaults | Avg ultimate recovery (Moody's) |
    |---|---|---|---|---|---|
    | Construction | 92 | 2.5 | 72.5% | 64 | 71.1% |
    | Operations | 542 | 4.6 | 80.8% | 389 | 78.1% |

    85.5% of Basel defaults occurred in operations. Phase was not known for every default, so the totals are 634 and 453 rather than 645 and 455.
27. **By sector and region (1983-2021).** [confidence: high] [source: 5]
    - PPP projects had the lowest default risk, with a 10-year CDR of 3.3% (Basel) and 2.0% (Moody's). All infrastructure projects had 3.4% (Basel).
    - Emerging market and developing economy subsets had 10-year CDRs of about 8.0%-8.5% (Basel), with recoveries consistent with the study average.
    - Power accounted for about 41% of defaults, infrastructure about 23%, and oil and gas about 13%.
28. **Earlier editions (record of how the figures have moved).** [confidence: high] [source: 6, 7]
    - **1983-2015 edition** (6 March 2017, republished with a correction 21 March 2017): 6,389 projects; 10-year CDR 6.7%, against 6.4% in the March 2016 study; average ultimate recovery 79.5%; full recovery in almost two-thirds of cases; lower recoveries for construction-phase defaults.
    - **1983-2018 edition** (March 2020): 10-year CDR 5.5% (Basel) and 3.7% (Moody's); average ultimate recovery 77.9% (Basel) and 75.8% (Moody's). These figures come from the 17 August 2020 addendum. That addendum, on sustainable project finance loans drawn from 8,583 loans, reports 10-year CDRs of 1.1% (Basel) for social projects, 4.9% for green and 7.1% for non-green.
29. **S&P's rated-infrastructure studies.** S&P Global Ratings publishes an annual infrastructure default and rating transition study covering its rated infrastructure issuers, both corporate and project finance. [confidence: medium; publisher abstracts via a research distributor] [source: 10, 11]
    - **2022 edition** (15 November 2023): a two-year average cumulative default rate for infrastructure of 0.9% over 1981-2022, against 3.7% for global nonfinancial corporates; three infrastructure defaults in 2022.
    - **2023 edition** (11 September 2024): nine infrastructure defaults in 2023 (seven power-related), against three in 2022; a default rate of 0.6%; no investment-grade defaults for the third year running.
30. **S&P Market Intelligence's bank-loan study.** S&P Global Market Intelligence (not S&P Global Ratings) published an "Annual Global Project Finance Default And Recovery Study, 1980-2014" on unrated project finance loans. The PDF exists on spglobal.com but returned "Access Denied" to automated retrieval, so its contents were not read. [confidence: medium, as to existence and title only] [source: 12]

## Timeline (dated events, if applicable)

| Date | Event |
|---|---|
| 20 Dec 2011 | S&P Project Finance Construction and Operations Counterparty Methodology |
| 15 Nov 2013 | S&P Project Finance Construction Methodology |
| 16 Sep 2014 | S&P Project Finance Framework, Operations and Transaction Structure Methodologies |
| Mar 2016 | Moody's PF bank loan study (previous edition to the 2017 study): 10-year CDR 6.4% |
| 6 Mar 2017 | Moody's PF bank loan study, 1983-2015 (6,389 projects; 10-year CDR 6.7%) |
| Mar 2020 | Moody's PF bank loan study, 1983-2018 (10-year CDR 5.5% Basel) |
| 17 Aug 2020 | Moody's sustainable PF loans addendum (1983-2018) |
| 2022 | Moody's Generic Project Finance Methodology version cited by CPE; since marked outdated |
| Mar 2022 | Moody's PF bank loan study, 1983-2020 (10-year CDR 5.3% Basel) |
| 9 Aug 2022 | S&P Request for Comment on project finance rating methodology |
| 14 Dec 2022 | S&P General and Sector-Specific Project Finance Rating Methodologies published; 2011-2014 suite superseded |
| 4 Apr 2023 | Moody's PF bank loan study, 1983-2021 (10,452 projects; 10-year CDR 4.8% Basel) |
| 2 Jun 2023; 19 Dec 2023 | S&P nonmaterial republications |
| 5 Jun 2024 | S&P republication; sector and industry variables moved into the criteria Appendix |
| 11 Sep 2024 | S&P 2023 Annual Infrastructure Default And Rating Transition Study |
| 14 Mar 2025 | S&P republication (modifiers apply cumulatively; project value methods clarified) |
| 19 Dec 2025 | S&P republication (cross-references and contacts) |

## Financing and structure details (parties, tranches, amounts, tenors, guarantees, where verified)

Not a transaction sheet. Several S&P criteria rules connect directly to term-sheet features (verified, source 1):
- A DSRA, or reserves equal to at least one year of debt service or 5% of debt, qualifies as "stronger liquidity reserves" in the resiliency test.
- Lack of a DSRA, unfunded or non-replenished reserves, or no distribution tests make liquidity "less than adequate" (at least −1 notch).
- Covenant headroom below a 10%-15% CFADS decline is penalized.
- Cash sweep dependence and back-ended amortization are penalized by up to three notches.
- A tail of at least 10 years and 20% of tenor can earn +1.
- Revolvers and permitted debt baskets are assumed fully drawn.
- Letters of credit funding a DSRA are treated as drawn, with their fees in debt service.

## What went wrong or right, and why (well-established analysis only, attributed to named sources)

- **Moody's (source 5):** marginal default rates fall as loans season. This suggests "the default risk of a project declines as construction is completed and the project starts to build its operating track record." Moody's links the elevated early-year rates to construction risk and ramp-up problems. It also reports that PF recoveries are less tied to the economic cycle than corporate recoveries, though their volatility has risen over the last decade.
- **Moody's (source 6):** the 2017 edition concluded that its findings "continue to suggest that the risk allocation, structural features, underwriting disciplines and incentive structures which characterize the project finance asset class have proven effective."
- **Center for Public Enterprise (source 8, a policy think tank):** argues that the DSCR thresholds make rating outcomes strongly dependent on contracted, predictable cash flow. This penalizes merchant and novel projects. It is an advocacy view, not a neutral assessment.

## Teaching angles by chapter (for each listed chapter: the transferable lesson and the angle to take, 2–4 sentences)

- **Chapter 30 (Project bonds and ratings):** Use S&P's two-phase architecture as the worked template: operations SACP, construction SACP, the lower of the two, then parent and sovereign overlays. Set this beside Fitch (t-ratings.md) and Moody's weighted scorecard to show three ways of arriving at a similar answer. Walk a Case P bond through S&P Table 8. Pick an OPBA, read off the DSCR range, then show how a modest resiliency result or a sweep-dependent structure caps or cuts the outcome. Make clear that the same 1.30x minimum DSCR implies a different rating at OPBA 2 than at OPBA 8.
- **Chapter 35 (CFADS and cover ratios):** Contrast S&P's use of the minimum DSCR, with median DSCR as a secondary check, against Moody's average-DSCR scorecard. Show PLCR at work in S&P's refinancing caps. The lesson is that the choice of metric reflects what each agency treats as the riskiest point.
- **Chapter 36 (Sizing and sculpting debt):** S&P's grid shows why sculpting to a flat DSCR suits ratings: a back-ended profile or reliance on cash sweeps gets notched down. Show the tail rule (at least 10 years and 20% of tenor) next to lenders' tail conventions.
- **Chapter 37 (Reserves, sweeps, covenants and hedging):** Use S&P's liquidity tests (1x 12-month coverage, a DSRA, 10%-15% covenant headroom, replenishment, distribution tests) to show which covenant package features carry rating value and which cost notches.
- **Chapter 2 / Chapter 15 (why project finance works; pricing risk):** Use Moody's 1983-2021 data, citing the edition and both default definitions. The 10-year CDR is about 4.8% (Basel), comparable to Baa3 corporates. Marginal default rates fall to single-A levels by year seven. Average recovery is about 80%, and recovery is 100% in 62% of cases. Construction defaults recover less (72.5% against 80.8% for operations). These figures explain why construction margins are higher and why risk-weight debates arise.

## Do not state (claims commonly repeated but unverified or wrong, and uncertain details)

- **Moody's current Generic Project Finance Methodology.** Its date, and whether its weights or DSCR grid changed from the 2022 version, were not verified (ratings.moodys.com was inaccessible). Present the scorecard as "Moody's 2022 version, as reproduced by the Center for Public Enterprise". Do not present it as current.
- The definitions of Moody's "Low/Medium/High" DSCR rows (the exhibit footnotes were not visible). The DSCR grid for non-amortizing debt and the Project Cash from Operations / Adjusted Debt thresholds. Not verified.
- Moody's sector methodologies: titles, dates and weights for PFI/PPP, construction risk in PFI, and power generation (beyond the secondary figures in item 22). Not verified.
- The Center for Public Enterprise brief defines DSCR as "net income" divided by debt service. Do not repeat this; DSCR is based on cash flow available for debt service.
- **Moody's PF bank loan studies after April 2023** (for example 1983-2022 or 1983-2023 editions). Not found; later editions may exist. Do not cite figures beyond the 1983-2021 edition as "latest" without checking.
- **S&P Market Intelligence 1980-2014 study figures.** Search snippets mention about 8,000 deals, a 10-year CDR in line with BBB corporates, and about 77% average recovery. These were not read in the document. Do not state them.
- S&P's 2024 or later annual infrastructure default study. Not found.
- Do not say S&P's minimum DSCR table alone sets the rating. Modifiers, caps, counterparty and sovereign constraints all apply, and committees exercise judgment.
- Do not cite "up to three notches" for S&P resiliency without the table context (see item 18).
- The Sector-Specific Project Finance Rating Methodology's sector stresses and ACOS by asset class (Chart 10 is an image and was not extracted). Not verified here.

## Sources (numbered: title, publisher/author, date, URL)

1. "General Project Finance Rating Methodology" (Criteria, Infrastructure, General), S&P Global Ratings, 14 December 2022, republished 19 December 2025. Copy hosted by S&P Global Ratings Maalot. https://www.maalot.co.il/Publications/MT20260201110512.pdf
2. "General Project Finance Rating Methodology", S&P Global Ratings, 14 December 2022 (original version, with Key Publication Information and superseded criteria list). Copy hosted by S&P Global Ratings Maalot. https://www.maalot.co.il/Publications/MT20221215151143.PDF
3. "General Project Finance Rating Methodology", S&P Global Ratings, republished 14 March 2025. Copy hosted by S&P Global Ratings Maalot. https://www.maalot.co.il/Publications/MT20250327160408.pdf
4. "Sector And Industry Variables: Project Finance Rating Methodology", S&P Global Ratings, 14 December 2022. Copy hosted by S&P Global Ratings Maalot. https://www.maalot.co.il/Publications/GCG20221215161953.PDF
5. "Default and recovery rates for project finance bank loans, 1983-2021" (Data Report, Infrastructure and Project Finance – Global), Moody's Investors Service, 4 April 2023. https://dkf1ato8y5dsg.cloudfront.net/uploads/52/504/default-and-recovery-rates-pif-2023-pbc-1358354.pdf (linked from Moody's events page https://events.moodys.com/project-finance-bank-loan-default-study-data-alliance-consortium/resources)
6. "Default and Recovery Rates for Project Finance Bank Loans, 1983-2015" (Sector In-Depth), Moody's Investors Service, 6 March 2017 (republished 21 March 2017). Third-party copy: https://www.almendron.com/tribuna/wp-content/uploads/2019/03/moodys-project-finance-default-study-1983-2015.pdf
7. "Default and recovery rates for project finance bank loans, 1983-2018: Sustainable project finance bank loans" (Sector In-Depth), Moody's Investors Service, 17 August 2020. https://ma.moodys.com/rs/961-KCJ-308/images/Default%20Reports%20-%20Default-research-Global%20-%2017Aug20.pdf
8. "Project finance: Credit ratings and investment strategies", Advait Arun, Center for Public Enterprise, September 2024 (reproduces Moody's Generic Project Finance Scorecard and DSCR exhibit). https://publicenterprise.org/wp-content/uploads/Project-Finance-September-2024.pdf
9. Moody's Ratings document library entry titled "OUTDATED METHODOLOGY ... Generic Project Finance Methodology" (title and search-indexed text only; page blocked by bot protection). https://ratings.moodys.com/api/rmc-documents/361401
10. "Default, Transition, and Recovery: 2023 Annual Infrastructure Default And Rating Transition Study", S&P Global Ratings, 11 September 2024 (abstract via Alacra Store). https://www.alacrastore.com/s-and-p-credit-research/Default-Transition-and-Recovery-2023-Annual-Infrastructure-Default-And-Rating-Transition-Study-3248495
11. "Default, Transition, and Recovery: 2022 Annual Infrastructure Default And Rating Transition Study", S&P Global Ratings, 15 November 2023 (abstract via Alacra Store). https://www.alacrastore.com/s-and-p-credit-research/Default-Transition-and-Recovery-2022-Annual-Infrastructure-Default-And-Rating-Transition-Study-3089774
12. "Annual Global Project Finance Default And Recovery Study, 1980-2014", S&P Global Market Intelligence (existence and title only; access denied). https://www.spglobal.com/content/dam/spglobal/mi/en/documents/general/Annual-Global-Project-Finance-Default-And-Recovery-Study--1980-2014.pdf
