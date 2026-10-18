# Notes 03 - NANDO (Türkiye) and PEM (retrieved 18 Oct 2026)

## NANDO via public EC Search API used by SMCS front-end (apiKey embedded in https://webgate.ec.europa.eu/single-market-compliance-space/ bundle)
Endpoint: POST https://webgate.ec.europa.eu/es/search-api/rest/search?apiKey=e2418f53-ea99-4bc4-a12f-c4cdd419de2c&text=*
Query: organizationCountryId=792 (Türkiye), csType=nando_body, organizationIfLatestVersion=Y -> 108 records (raw: dl/nando_tr_bodies.json)
- NB-type records: 95 unique body numbers; 81 with no end date or end date after 18 Oct 2026; 14 with expired/ended validity.
- Other: RTPO (PED recognised third-party orgs) 8 active; TAB (CPR technical assessment bodies) 2; AB (old) 2.
- Recent designations: 3073-3234 numbers added 2025-2026 (e.g., 3225 Aves Global Jun 2026; 3234 Avrasya Cephe-Dogrami Test Sep 2026).
- MDR-relevant: UDEM (2292), Kiwa Belgelendirme (1984), Szutest (2195) etc. (sector check not done per body)
- Notifying authority latest record: "Ministry of Trade - DG Product Safety and Inspection" legislation codes: Regulation (EU) 2024/3110 (new CPR), 90/385/EEC, 92/42/EEC, 93/42/EEC, 98/79/EC, 2000/14/EC, 2006/42/EC, Regulation (EU) 305/2011, 2013/29/EU, 2013/53/EU, 2014/28/EU, 2014/29/EU, 2014/30/EU, 2014/31/EU, 2014/32/EU, 2014/33/EU, 2014/34/EU, 2014/53/EU, 2014/68/EU, Reg 2016/425 (PPE), Reg 2017/745 (MDR), Reg 2016/426 (GAR), Reg 2016/424 (cableways). TURKAK listed with role 4 (accreditation body).
- Turkish Ministry of Trade page (via search snippet; site unreachable from sandbox): "Türkiye has notified 65 national conformity assessment bodies as Notified Body under 16 New Approach directives (as of April 2025)" https://www.trade.gov.tr/legislation/product-safety-and-technical-regulation/general-rules-and-procedures-on-technical-regulations
- Legal basis: Decision 1/95 Arts 8-10; Decision 2/97 (list of instruments, Annex II); Decision No 1/2006 of the EC-Turkey Association Council of 15 May 2006 implementing Art 9 of Decision 1/95 (CUJC statement + notification of Turkish CABs/identification numbers).

## PEM
- Türkiye signed PEM Convention 4 Nov 2011, deposited acceptance 4 Dec 2013; in force for Türkiye 1 Feb 2014 (EU: 1 May 2012) - recital 6 of Decision No 1/2025 of the EU-Türkiye Association Council (OJ L 2026/1903, 31.7.2026).
- Decision No 1/2025 AC (22 Dec 2025): replaces Protocol 3 to Decision 1/98 (agri) with dynamic reference to PEM Convention "as last amended"; applies first day of month following last notification. Art 4: if withdrawal from Convention, bilateral cumulation only + continued application of rules at moment of withdrawal.
- Decision No 1/2025 EU-Türkiye (ECSC) Joint Committee (22 Dec 2025) replaces Protocol 1 of 1996 ECSC agreement (OJ L 2026/359).
- COM(2026) 477 (17 Sep 2026): new Customs Cooperation Committee decision to replace Decision No 1/2006 of CCC of 26 Sep 2006 ('bridging legislation', A.TR rules) to align with UCC and PEM; retroactive from 1 Jan 2026; covers e-movement certificates, INF 2/INF 4, non-alteration, full cumulation and duty drawback for goods exported outside the CU. Legal basis Art 207(4) first subpara + 218(9) TFEU.
- Revised PEM (Decision No 1/2023 of the PEM Joint Committee, OJ L 2024/390), applies from 1 Jan 2025:
  * Art 5 tolerance: 15% net weight (Ch 2, 4-24 excl. processed fishery Ch 16) / 15% ex-works price (others); textiles Ch 50-63 use Notes 6-7 (15% weight of basic textile materials for mixtures).
  * Art 7(3) full cumulation except Ch 50-63.
  * Art 16 drawback: prohibition ONLY for products of Ch 50-63; para 4: no prohibition for products originating via Art 7(4)/(5) cumulation; para 5: no prohibition in bilateral trade between EFTA/Türkiye/EU and Barcelona participants other than Türkiye and Israel without cumulation.
  * Andorra (Ch 25-97) and San Marino CU products treated as EU-originating (Arts 39-40). No equivalent clause for the EU-Türkiye CU.
- Commission PEM page: revised/transitional rules applied bilaterally with EU from 2021-2023 by Albania, Faroe, Georgia, Iceland, Jordan, Palestine, Norway, Switzerland (1 Sep 2021), N. Macedonia, Moldova, Serbia, Montenegro, Kosovo, Ukraine (1 Dec 2023), BiH; Tunisia 1 Mar 2025, Egypt 11 Mar 2025, Morocco Decision 1/2025 in force 2 Oct 2025 (parallel). Joint Committee Decision 2/2024: 2012 rules applicable in parallel through 31 Dec 2025. Page notes new diagonal cumulation possibilities incl. Albania-Türkiye, Türkiye-Serbia, Türkiye-Moldova, Türkiye-Egypt.
  https://taxation-customs.ec.europa.eu/customs-4/international-affairs/pan-euro-mediterranean-cumulation-and-pem-convention_en
