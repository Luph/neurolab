# Earned value management: origins and standards (US DoD C/SCSC 1967, ANSI/EIA-748, PMI and ISO standards)

As of: 2026-10-03 (latest events covered: SAE EIA-748-E, published early 2026; DFARS 234.201 as shown with DFARS change effective 7 May 2026)

## Summary

Earned value management (EVM) measures project progress by comparing three quantities:
- planned value (PV, formerly BCWS): the budgeted cost of work scheduled;
- earned value (EV, formerly BCWP): the budgeted cost of work performed;
- actual cost (AC, formerly ACWP): the actual cost of work performed.
From these come cost and schedule variances and indices (CPI = EV/AC; SPI = EV/PV) and estimates at completion.

EVM grew out of the US Navy/DoD PERT/Cost system (adopted 1962) and the US Air Force's earned value approach on the Minuteman programme (from 1963). It became DoD-wide with Department of Defense Instruction (DoDI) 7000.2, "Performance Measurement for Selected Acquisitions", issued on 22 December 1967. That instruction required contractors to meet the Cost/Schedule Control Systems Criteria (C/SCSC); the 1977 reissue contained 35 criteria. In the 1990s an industry initiative led by the National Defense Industrial Association (NDIA) rewrote these as 32 EVMS guidelines. The DoD accepted them in 1996, and they were issued as ANSI/EIA-748 in 1998. Revisions followed in 2002, 2007, 2013 and 2019 (EIA-748-D, SAE International). Revision E, published by SAE in early 2026, cuts the guidelines from 32 to 27.

In US defence contracting (DFARS 234.201), cost or incentive contracts of USD 20 million or more must comply with EIA-748, and those of USD 50 million or more need an EVMS validated by the cognizant agency (DCMA for DoD). PMI published a Practice Standard for EVM (2005; second edition 2011), replaced by ANSI/PMI 19-006-2019, "The Standard for Earned Value Management". ISO 21508:2018 is the international standard.

The most-cited empirical result is Christensen and Heise (1993): in 155 DoD contracts, the cumulative CPI was generally stable from 20% completion. Later work (Henderson and Zwikael) found this rule cannot be generalised, even within DoD.

## Verified facts

### A. Origins

1. PERT/Cost was developed between 1960 and 1962 by a joint Stanford/Navy team and adopted by the DoD and NASA on 1 June 1962. By 1964 more than ten variants existed. [confidence: high (detailed history, Weaver 2022)] [source: 1]
2. In 1963 the US Air Force implemented the first earned value approach on the Minuteman programme. The Air Force's Cost/Schedule Planning and Control Specification (C/SPCS) followed (1 August 1966; revised June 1967 into 35 criteria). [confidence: high] [source: 1]
3. On 22 December 1967 the DoD issued DoDI 7000.2, "Performance Measurement for Selected Acquisitions", at the initiative of Assistant Secretary of Defense (Comptroller) Robert N. Anthony.
   - It required the use of C/SCSC but did not itself state the criteria.
   - A C/SCSC Joint Implementation Guide was published on 27 January 1972.
   - DoDI 7000.2 was reissued in 1977 with the 35 criteria.
   [confidence: high] [source: 1]
4. DoDI 7000.2 was replaced by DoDI 5000.2 in 1991, then by DoD 5000.2-R in 1996. 5000.2-R reduced the criteria from 35 to 32, in line with the NDIA-led industry rewrite as "Earned Value Management System" guidelines. That rewrite moved EVM from a financial-management towards a project-management technique, and ownership of the guidelines from the DoD to industry. [confidence: high] [source: 1]

### B. ANSI/EIA-748 and SAE EIA-748 (current text sold by SAE International, sae.org; DoD implementation at DFARS 234.2 and 252.234-7001/-7002)

5. Revision history:
   - ANSI/EIA-748 approved May 1998 (adopted July 1998; DoD adoption 1999);
   - 748-A reaffirmed August 2002;
   - 748-B approved July 2007;
   - EIA-748-C approved March 2013 (TechAmerica);
   - EIA-748-D approved 8 January 2019 (SAE International).
   NDIA maintains the standard with SAE on a five-year cycle. ANSI no longer sponsors it. Revisions A to D kept 32 guidelines. [confidence: high] [source: 1]
6. EIA-748-E: SAE International published Revision E in early 2026 (reported as February 2026; consultancy notice dated 1 March 2026). It reduces the guidelines from 32 to 27: four deleted, two new, others merged, in five process categories. It separates change management into customer-directed changes, internal replanning, and over-target baseline/schedule. Contractors' system descriptions will need remapping, and the cognizant agencies (DCMA, NASA, DOE) will update their compliance processes. No formal transition deadline was reported. [confidence: medium-high (industry consultancy reports; SAE catalogue entry "SAE EIA 748E-2026")] [source: 2, 3]
7. DFARS 234.201 (text shown with DFARS change effective 7 May 2026). For DoD:
   - cost or incentive contracts and subcontracts of USD 20,000,000 or more must have an EVMS that complies with ANSI/EIA-748;
   - those of USD 50,000,000 or more must have an EVMS determined compliant by the cognizant federal agency;
   - below USD 20 million, EVM is optional and risk-based, with a documented cost-benefit analysis;
   - for firm-fixed-price contracts of any value, EVM is "discouraged" and needs a waiver;
   - DCMA determines compliance where DoD is the cognizant agency.
   [confidence: high] [source: 4]

### C. PMI and ISO standards

8. PMI published the Practice Standard for Earned Value Management in 2005 (PMI PSF-EVM-2005) and a second edition in 2011 (PSF-EVM-2011). It was succeeded by ANSI/PMI 19-006-2019, "The Standard for Earned Value Management" (2019). The 2019 standard integrates PMBOK Guide (6th edition) and Agile Practice Guide concepts and expands "value" to include earned schedule. [confidence: medium-high (catalogue listings and publisher descriptions)] [source: 5, 6]
9. ISO 21508:2018, "Earned value management in project and programme management" (first edition), was published in April 2018. Australia adopted a modified version as AS 4817-2019. [confidence: high for ISO; medium for AS] [source: 7, 8]

### D. Core definitions (standard identities)

10. Definitions: CV = EV − AC; SV = EV − PV; CPI = EV/AC; SPI = EV/PV. A common independent estimate at completion is EAC = BAC/CPI, where BAC is the budget at completion. Under C/SCSC the terms were BCWS, BCWP and ACWP; C/SCSC earlier used PVWS and PVWA. [confidence: high] [source: 1, 6]
11. Earned schedule, proposed by Lipke in 2003, converts EV data into time-based schedule measures (SPI(t)). This addresses the known flaw that SPI tends to 1.0 at completion whatever the delay. [confidence: high] [source: 1, 10]

### E. Empirical findings

12. Christensen and Heise, "Cost Performance Index Stability" (National Contract Management Journal 25, 1993), studied 155 contracts from 44 programmes, with performance periods from June 1971 to 1991.
    - The cumulative CPI range did not exceed 0.2 after the 50% point for 153 of the 155 contracts.
    - At the 20% completion point, 134 of 155 contracts had stable cumulative CPIs.
    - The work built on Christensen and Payne's finding that the cumulative CPI did not change by more than 10% from its value at 20% completion.
    - The paper notes that, after the A-12 cancellation (January 1991), OUSD(A) required EACs below the cumulative-CPI EAC to be specifically justified.
    [confidence: high] [source: 9]
13. Henderson and Zwikael ("Does Project Performance Stability Exist? A re-examination of CPI and evaluation of SPI(t) stability") examined projects from three countries: 26 for CPI stability and 37 for SPI(t). They concluded that the widely reported CPI stability rule "cannot be generalized even within the US Defense Department (US DoD) project portfolio". [confidence: high] [source: 10]

## Timeline

- 1 June 1962: PERT/Cost adopted by DoD and NASA.
- 1963: Air Force earned value on Minuteman.
- 1 August 1966: Air Force C/SPCS; June 1967 revision with 35 criteria.
- 22 December 1967: DoDI 7000.2 issued (C/SCSC DoD-wide).
- 27 January 1972: C/SCSC Joint Implementation Guide.
- 1977: DoDI 7000.2 reissued with 35 criteria.
- January 1991: A-12 cancelled; DoD tightens EAC policy.
- 1991: DoDI 7000.2 replaced by DoDI 5000.2.
- 1993: Christensen and Heise CPI stability study.
- 1996: DoD 5000.2-R adopts 32 industry guidelines.
- May/July 1998: ANSI/EIA-748 issued.
- 2002 (A), 2007 (B), 2013 (C), 8 January 2019 (D): revisions.
- 2003: Lipke proposes earned schedule.
- 2005 and 2011: PMI Practice Standard for EVM, first and second editions.
- April 2018: ISO 21508.
- 2019: ANSI/PMI 19-006-2019.
- Early 2026: SAE EIA-748-E (27 guidelines).

## Financing and structure details

Not a financing instrument. In project finance, lenders' technical advisers use EVM-style progress measures (planned versus earned versus actual) in monthly construction reports, drawdown certification and cost-to-complete tests (Chapter 61). Formal EIA-748 compliance is a US government contracting requirement, not a lender requirement. Whether a facility agreement requires EVM reporting is deal-specific.

## What went wrong or right, and why

- The A-12 cancellation (1991) is the canonical case of ignoring EVM signals. Christensen and Heise report that the programme office was criticised for treating the cumulative-CPI EAC as a ceiling rather than a floor [9].
- Weaver notes that the C/SCSC guide's discussions hardened into de facto requirements (for example arbitrary six-month rolling-wave horizons), and that 182 checklist items produced bureaucracy. That is part of why industry took over the guidelines in the 1990s and why Revision E streamlines them [1, 2].
- Henderson and Zwikael caution that the "CPI stable at 20%" rule is a DoD-portfolio finding, not a law [10].

## Teaching angles by chapter

- **Chapter 61 (Construction to completion)**: Teach PV/EV/AC with a Case P construction month: compute CV, SV, CPI, SPI and EAC = BAC/CPI, then compare with the contractor's own estimate to complete. Use Christensen and Heise to explain why lenders' advisers treat an early CPI below 1.0 as a warning that rarely reverses, and Henderson and Zwikael to warn against treating it as certain. Note that SPI converges to 1.0 at completion, so use earned schedule or critical-path analysis for delay. Mention EIA-748 (now 27 guidelines in Revision E) and DFARS thresholds only as the origin of the discipline, not as lender requirements.

## Do not state

- That EIA-748-E has been adopted in the DFARS or made mandatory for new DoD contracts by a specific date. Not verified; DFARS still refers to ANSI/EIA-748.
- The exact publication date of EIA-748-E. Reported as February 2026; the SAE catalogue was not accessed.
- That ANSI still sponsors EIA-748. Weaver says it no longer does.
- That the CPI "never" improves after 20% completion, or a universal ±10% rule. The finding is from DoD contracts.
- That C/SCSC had 35 criteria from the 1967 instruction. The 1967 DoDI did not state the criteria; the 35 criteria appear in the 1967 Air Force specification and the 1977 DoDI reissue.
- Any statistic on EVM use in commercial project finance. Not verified.

## Sources

1. Weaver, P., "The Origins and History of Earned Value Management", PM World Journal XI(VIII), August 2022. https://pmworldlibrary.net/wp-content/uploads/2022/08/pmwj120-Aug2022-Weaver-origins-and-history-of-earned-value-management.pdf
2. Humphreys & Associates, "EIA-748 Standard for EVMS Revision E Published", 1 March 2026. https://blog.humphreys-assoc.com/eia-748-standard-for-evms-revision-e-published/
3. ANSI Webstore listing, "SAE EIA 748E-2026 – Earned Value Management Systems" (title only; page access blocked). https://webstore.ansi.org/standards/sae/saeeia748e2026
4. Defense Federal Acquisition Regulation Supplement, 234.201 Policy, Acquisition.gov (DFARS change effective 7 May 2026). https://www.acquisition.gov/dfars/234.201-policy.
5. ANSI Webstore listing, "ANSI/PMI 19-006-2019 – The Standard for Earned Value Management". https://webstore.ansi.org/standards/pmi/ansipmi190062019
6. ANSI Webstore listing, "PMI PSF-EVM-2011 – Practice Standard for Earned Value Management – Second Edition". https://webstore.ansi.org/standards/pmi/pmipsfevm2011
7. ISO, "ISO 21508:2018 Earned value management in project and programme management". https://www.iso.org/standard/63582.html
8. IPMA, "ISO 21508 Earned value management in project and programme management released", 2018. https://www.ipma.world/iso-21508-earned-value-management-project-programme-management-released/
9. Christensen, D. S. and Heise, S. R., "Cost Performance Index Stability", National Contract Management Journal 25 (1993) 7–15 (copy hosted by Humphreys & Associates). https://www.humphreys-assoc.com/uploads/commerce/images/pdf/Christensen_and_Heise_CPI_Stability.pdf
10. Henderson, K. and Zwikael, O., "Does Project Performance Stability Exist? A re-examination of CPI and evaluation of SPI(t) stability" (copy hosted at earnedschedule.com; publication year not verified). https://www.earnedschedule.com/docs/does%20project%20performance%20stability%20exist%20%20henderson%20zwikael.pdf
