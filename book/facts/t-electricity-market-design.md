# Electricity market design: nodal vs zonal pricing, ERCOT price caps after Uri, capacity markets (PJM, GB, Italy), negative prices and ancillary services

As of: 2026-10-03 (latest events covered: PJM 2028/2029 Base Residual Auction report of 14 July 2026; ERCOT 2025 State of the Market report, June 2026)

## Summary

How a power market prices location, scarcity and capacity determines what a project can earn. In the US, the regional transmission organizations (RTOs) and independent system operators (ISOs) use locational marginal pricing (LMP), which sets a price at each node. Europe and Great Britain use zonal or single-zone pricing. In July 2025 the UK government decided to keep a single national wholesale price under "reformed national pricing" rather than move to zonal pricing.

ERCOT (the grid operator for most of Texas) runs an energy-only nodal market. After Winter Storm Uri in February 2021, the Public Utility Commission of Texas (PUCT) cut ERCOT's high system-wide offer cap (HCAP) from USD 9,000/MWh to USD 5,000/MWh, effective 1 January 2022. On 5 December 2025 ERCOT went live with real-time co-optimization of energy and ancillary services.

Capacity markets give an explicit payment for being available:
- PJM's capacity prices jumped from USD 28.92/MW-day (2024/25) to USD 269.92/MW-day (2025/26), then cleared at FERC-approved caps for 2026/27 (USD 329.17), 2027/28 (USD 333.44) and 2028/29 (USD 325.00). In each of the last two auctions PJM procured about 6.5–6.8 GW less than its reliability requirement.
- The GB T-4 auction for 2028/29 cleared at GBP 60.00/kW-year.
- Italy's market-wide reliability-option mechanism, approved by the European Commission in February 2018, procured 38.6 GW of national capacity at EUR 47,000/MW-year for delivery in 2027.

Negative prices are now common where wind and solar shares are high. Germany recorded negative wholesale prices in 457 of 8,784 hours in 2024, against 301 in 2023.

## Verified facts

Nodal vs zonal

1. FERC staff's Energy Primer (April 2020) explains that RTOs and ISOs calculate an LMP at each location on the grid. Each LMP has three components: energy, congestion and losses. Without congestion, LMPs do not vary much across the footprint. With congestion, they diverge because the operator cannot dispatch the least-cost generators across the whole region. The primer also describes the financial transmission rights (FTRs) used to hedge day-ahead congestion. [confidence: high] [source: 1]
2. Within the US nodal markets, settlement details differ. For example, FERC notes that virtual trading in NYISO takes place at the zonal level, not the nodal level. In ERCOT, load is settled at the load-weighted average price of its load zone, while generators are paid nodal prices. [confidence: high] [source: 1, 3]
3. ERCOT: according to its own profile, ERCOT serves about 27 million Texas customers, representing about 90% of the state's electric load, across more than 55,000 miles of transmission and 1,460+ generation units, covering about 75% of Texas's land area. ERCOT's nodal market began in 2010. Its four load zones (West, North, South, Houston) date from 2003, and the market monitor recommends updating them. [confidence: high] [source: 2, 3, 4]
4. Great Britain: on 10 July 2025 the UK government published its REMA (Review of Electricity Market Arrangements) summer update. It said the government had "decided not to implement zonal pricing" and would pursue "reformed national pricing" instead. A Reformed National Pricing delivery plan followed on 21 April 2026. GB therefore remains a single national price zone. [confidence: high] [source: 11]

ERCOT price caps after Uri

5. During Uri, ERCOT's HCAP and value of lost load (VOLL) were both USD 9,000/MWh. On 12 September 2013 the PUCT had directed ERCOT to implement the ORDC with VOLL set at USD 9,000/MWh; the ORDC was chosen at the time as an easier-to-implement alternative to real-time co-optimization. Prices were held at that level through the emergency, and the existing winter-storm-uri sheet covers those events. In 2021, prices were at or near the USD 9,000 cap in intervals totalling roughly 98 hours, and prices exceeded USD 1,000/MWh in 166 hours (against 7 hours in 2020). [confidence: high] [source: 2; see winter-storm-uri.md]
6. PUC Project No. 52631 (Review of 25.505; order dated 2 December 2021) set the HCAP at USD 5,000/MWh effective 1 January 2022. Under the ORDC (operating reserve demand curve) changes approved under Project No. 52373, the HCAP and VOLL fell from USD 9,000 to USD 5,000/MWh and the minimum contingency level rose to 3,000 MW, both effective 1 January 2022. These ORDC changes make prices rise faster at small shortages but plateau at a lower level. [confidence: high] [source: 2]
7. Separately, PUC Project No. 51871 (24 June 2021) removed the link between the low system-wide offer cap (LCAP) and gas prices. Resources are instead made whole to their actual marginal costs when the LCAP is in effect. The Commission later de-coupled VOLL from the system-wide offer cap (Project No. 53191), with VOLL remaining at USD 5,000/MWh at the time of the 2021 report. [confidence: high] [source: 2]
8. In its 2025 report, ERCOT's independent market monitor (Potomac Economics) said the VOLL underlying ERCOT's ancillary service demand curves is far below what a 1-in-10 reliability standard implies. It recommended USD 35,000–40,000/MWh for pricing shallow shortages, even if deep shortages remain capped at USD 5,000. [confidence: high] [source: 3]
9. In 2025 ERCOT's ORDC was active for only 57 hours. That is just over one-third of the 2024 total and less than 8% of the 2021–2024 annual average, because large additions of solar and batteries outpaced peak demand growth. The ORDC added less than USD 0.02/MWh to the annual average real-time price. [confidence: high] [source: 3]

Ancillary services

10. FERC's Energy Primer defines the main operating reserves. Spinning reserves come from online, synchronized units with spare capacity that can respond within a specified time, such as 10 minutes. Non-spinning reserves can be brought online within a specified time, such as 10 minutes. Supplemental reserves are available within, for example, 30 minutes. Regulation adjusts output every few seconds to hold frequency at 60 Hz. Demand-side resources can provide several of these. [confidence: high] [source: 1]
11. ERCOT's ancillary service products are regulation service (up and down), Responsive Reserve Service (RRS), ERCOT Contingency Reserve Service (ECRS) and Non-Spinning Reserve Service (NSRS). ECRS was implemented in June 2023 and, according to the market monitor, had a "profound impact" on prices in 2023. [confidence: high] [source: 3]
12. ERCOT implemented real-time co-optimization (RTC) on 5 December 2025, a project that began in January 2019. Under RTC, energy and ancillary services are procured together in real time. Day-ahead energy and ancillary service awards become purely financial positions, settled against real-time prices. Virtual ancillary service positions were also introduced, and operators no longer deploy ECRS manually. The monitor reports that energy storage resources provide the vast majority of regulation, most RRS together with non-controllable load resources, and a growing share of ECRS and NSRS. [confidence: high] [source: 3]
13. The monitor also reports that ERCOT's ancillary service methodology raises requirements to more than double the quantities needed for a reasonable reliability standard. This includes about 2 GW of reserves that give "virtually no incremental reliability value". [confidence: high] [source: 3]

Capacity markets: PJM (Reliability Pricing Model, Base Residual Auction)

14. 2025/2026 BRA (report dated 30 July 2024): RTO clearing price USD 269.92/MW-day, up from USD 28.92/MW-day for 2024/2025. Two constrained areas cleared higher: BGE (Baltimore Gas and Electric) at USD 466.35 and DOM (Dominion) at USD 444.26. 135,684 MW of unforced capacity (UCAP) cleared. [confidence: high] [source: 5]
15. 2026/2027 BRA (report dated 22 July 2025): all prices cleared at the cap of USD 329.17/MW-day. 134,310.8 MW UCAP cleared. Total cleared supply multiplied by price came to about USD 16.1 billion. [confidence: high] [source: 6]
16. 2027/2028 BRA (report dated 17 December 2025): all prices cleared at the temporary cap of USD 333.44/MW-day UCAP. Total procured capacity was 6,516.6 MW UCAP below the RTO reliability requirement. RPM cleared a 14.4% installed reserve margin against a 20% target. Total value was about USD 16.4 billion. [confidence: high] [source: 7]
17. 2028/2029 BRA (report dated 14 July 2026): the cap of USD 325.00/MW-day and floor of USD 175.00/MW-day were approved by FERC in Docket ER26-1556. All prices cleared at the cap. RPM cleared 138,317.8 MW UCAP, and the Fixed Resource Requirement (FRR) alternative, under which a utility supplies its own capacity outside the auction, committed 10,863.8 MW. Total procurement was 6,831.3 MW UCAP below the reliability requirement, and the reserve margin was 14.4% against 20%. It was the second BRA in a row more than one percentage point below target. Total value was about USD 16.4 billion. [confidence: high] [source: 8]

Capacity markets: Great Britain

18. The GB Capacity Market rests on the Energy Act 2013 (Royal Assent 18 December 2013), the Electricity Capacity Regulations 2014 and the Capacity Market Rules 2014. The National Energy System Operator (NESO) acts as the EMR Delivery Body and runs the auctions. T-4 auctions procure capacity four years ahead of delivery and T-1 auctions one year ahead. [confidence: high] [source: 9, 10]
19. In 2018 the EU General Court's judgment in Case T-793/14 (Tempus Energy) imposed a standstill on the scheme. The government kept running it but withheld payments, and planned a T-1 auction for summer 2019 that was conditional on European Commission approval. [confidence: high] [source: 10]
20. The 2024 T-4 auction, for delivery year 2028/29, ran on 11 March 2025 and cleared in Round 3. The Auction Monitor (Deloitte) reported a clearing price of GBP 60.00 and capacity agreements totalling 43,055.073 MW. GB capacity market prices are expressed per kW of de-rated capacity per year. [confidence: high for figures; medium for unit wording] [source: 9]

Capacity markets: Italy

21. On 7 February 2018 the European Commission approved capacity mechanisms in six member states under EU state aid rules: strategic reserves in Belgium and Germany; market-wide mechanisms in Italy and Poland; and demand-response schemes in France and Greece. The Commission found that Italy had shown that significant capacity risked exiting the market and that new investment was unlikely without the mechanism. [confidence: high] [source: 12]
22. Italy's first capacity auction ("asta madre"), for delivery year 2022, was held on 6 November 2019 and ended the next day. It assigned 40.9 GW (36.5 GW national, 4.4 GW foreign) at an annual cost of about EUR 1.3 billion. The premium was EUR 33,000/MW-year for existing capacity and EUR 75,000/MW-year for new capacity, with a marginal premium of EUR 75,000/MW-year in all national areas. [confidence: high] [source: 13]
23. The asta madre for delivery year 2027 was held on 26–27 February 2025. It assigned 38,047 MW of existing and 594 MW of new authorized national capacity, all at EUR 47,000/MW-year. Foreign capacity was 4,200 MW (North) at EUR 7,199, 113 MW (Centre-South) at EUR 5,579 and 52 MW (South) at EUR 6,500/MW-year. The total cost was EUR 1,847.3 million. [confidence: high] [source: 14]

Negative prices

24. According to Bundesnetzagentur (SMARD) data, German day-ahead wholesale prices were negative in 457 of 8,784 hours in 2024, against 301 of 8,760 hours in 2023. Prices above EUR 100/MWh fell from 4,106 hours (2023) to 2,296 hours (2024). [confidence: high] [source: 15]
25. In ERCOT in 2025, the West load zone had the highest number of negative-price intervals and the most frequent price spikes. This is because it contains both the export-constrained Panhandle (wind and solar) and the import-constrained Permian Basin (fast load growth). Batteries increasingly charge during midday low or negative prices. [confidence: high] [source: 3]

## Timeline

- 2003: ERCOT's four load zones established.
- 2010: ERCOT nodal market begins.
- 12 September 2013: PUCT directs ERCOT to implement the ORDC with VOLL at USD 9,000/MWh.
- 18 December 2013: Energy Act 2013 receives Royal Assent (GB Capacity Market).
- 7 February 2018: European Commission approves six capacity mechanisms, including Italy.
- 6–7 November 2019: Italy's first capacity auction (delivery 2022).
- February 2021: Winter Storm Uri; prices held at USD 9,000/MWh.
- 24 June 2021: PUCT Project 51871 decouples the LCAP from gas prices.
- 2 December 2021: PUCT Project 52631 sets HCAP at USD 5,000/MWh.
- 1 January 2022: HCAP and VOLL become USD 5,000/MWh; minimum contingency level 3,000 MW.
- June 2023: ERCOT launches ECRS.
- 30 July 2024: PJM 2025/26 BRA results (USD 269.92/MW-day).
- 26–27 February 2025: Italy's auction for delivery 2027.
- 11 March 2025: GB T-4 auction for 2028/29 (GBP 60.00).
- 10 July 2025: UK REMA update rejects zonal pricing.
- 22 July 2025: PJM 2026/27 BRA clears at the cap of USD 329.17.
- 5 December 2025: ERCOT RTC goes live.
- 17 December 2025: PJM 2027/28 BRA clears at USD 333.44.
- 21 April 2026: UK Reformed National Pricing delivery plan.
- 14 July 2026: PJM 2028/29 BRA clears at USD 325.00.

## Financing and structure details

- A capacity payment is a fixed availability revenue (USD/MW-day, GBP/kW-year, EUR/MW-year) that lenders can underwrite more readily than energy margins. GB T-4 and Italian agreements for new capacity can run multiple years. The length of agreements for new build was not verified in this session, so cite the scheme rules before stating it. [source: 9, 14]
- PJM's cap and floor (Docket ER25-1357 for 2026/27 and 2027/28; ER26-1556 for 2028/29) limit both upside and downside for the delivery years covered. A lender's base case should not extrapolate capped prices past the years covered. [source: 6, 7, 8]

## What went wrong or right, and why

- The ERCOT market monitor attributes the drop in shortage pricing (ORDC active only 57 hours in 2025) to fast additions of solar and storage without matching peak growth. It says that ancillary service over-procurement and out-of-market reliability-unit commitments suppress the scarcity signals an energy-only market depends on. [source: 3]
- PJM itself notes that a price cap below the VRR (variable resource requirement) curve "can reduce the amount of investment, and therefore supply". It says shortfalls of more than one percentage point below the installed reserve margin target mean operating "with slimmer reserves and greater level of risk". [source: 8]

## Teaching angles by chapter

- Ch 11 (how power assets and markets work): Teach LMP = energy + congestion + losses with a two-node example, then contrast it with GB's single national price (kept in 2025) and with EU bidding zones. Explain why ERCOT pays generators nodal prices but settles load zonally, which creates basis risk. Use the Germany 301 → 457 negative-hours data to show what high renewable shares do to price distributions.
- Ch 20 (merchant revenue and hedges): Price caps define the tail of a hedge book. Show how the drop from USD 9,000 to USD 5,000 changed the maximum hourly exposure of a fixed-shape hedge (see winter-storm-uri.md). Build a capacity-revenue line for a PJM peaker at USD 269.92–333.44/MW-day and stress it at the 2028/29 floor (USD 175). Show how ERCOT RTC changed ancillary service revenue for batteries, now that day-ahead awards are financial and settled in real time.

## Do not state

- PJM capacity prices before 2024/25, or any LDA-specific prices other than those quoted above, without checking the BRA reports.
- GB T-4 clearing prices for other auctions (for example 2027/28 or 2029/30). Only the 2028/29 auction was verified.
- Agreement lengths for GB or Italian new-build capacity contracts (for example "15 years"). These were not verified in this session.
- Italy's reliability-option strike price mechanics or the PUN-to-zonal transition dates. These were not verified in this session.
- Australian NEM market price cap values (the AEMC/AEMO sources returned 403).
- German negative-price hours for 2025, or any CAISO or SPP negative-price frequencies. These were not verified.
- That GB has introduced locational pricing. It has not: zonal pricing was rejected on 10 July 2025.

## Sources

1. FERC staff, "Energy Primer: A Handbook of Energy Market Basics", April 2020, https://www.ferc.gov/sites/default/files/2020-06/energy-primer-2020.pdf
2. Potomac Economics (ERCOT IMM), "2021 State of the Market Report for the ERCOT Electricity Markets", May 2022, https://www.potomaceconomics.com/wp-content/uploads/2022/05/2021-State-of-the-Market-Report.pdf
3. Potomac Economics (ERCOT IMM), "2025 State of the Market Report for the ERCOT Electricity Markets", June 2026, https://www.potomaceconomics.com/wp-content/uploads/2026/06/2025-State-of-the-Market-Report-for-ERCOT.pdf
4. ERCOT, "About ERCOT – Profile", accessed 3 October 2026, https://www.ercot.com/about/profile
5. PJM, "2025/2026 Base Residual Auction Report", 30 July 2024, https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2025-2026/2025-2026-base-residual-auction-report.pdf
6. PJM, "2026/2027 Base Residual Auction Report", 22 July 2025, https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2026-2027/2026-2027-bra-report.pdf
7. PJM, "2027/2028 Base Residual Auction Report", 17 December 2025, https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2027-2028/2027-2028-bra-report.pdf
8. PJM, "2028/2029 Base Residual Auction Report", 14 July 2026, https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2028-2029/2028-2029-bra-results-report.pdf
9. Deloitte LLP for NESO/DESNZ, "2024 four year ahead Capacity Auction (T-4) Delivery Year 2028/29: Auction Monitor report", 13 March 2025 (published 17 March 2025), https://assets.publishing.service.gov.uk/media/67d44b1db1e34f07631b5bf8/t4-2024-for-delivery-2028-2029-auction-monitor-report.pdf
10. GOV.UK, "Capacity Market" collection page (DESNZ/BEIS), last updated 23 January 2023, https://www.gov.uk/government/collections/electricity-market-reform-capacity-market
11. DESNZ, "Review of electricity market arrangements (REMA): Summer update, 2025", 10 July 2025, https://assets.publishing.service.gov.uk/media/686f71412557debd867cbeff/review-of-electricity-market-arrangements-rema-summer-update-2025.pdf; and "Reformed National Pricing (RNP): delivery plan", 21 April 2026, https://www.gov.uk/government/publications/reformed-national-pricing-rnp-delivery-plan
12. European Commission, press release IP/18/682, "State aid: Commission approves six electricity capacity mechanisms to ensure security of supply in Belgium, France, Germany, Greece, Italy and Poland", 7 February 2018, https://ec.europa.eu/commission/presscorner/detail/en/IP_18_682
13. Terna, "Mercato della Capacità – Rendiconto degli esiti – Asta Madre 2022", December 2019, https://download.terna.it/terna/2019_12_06_Rendiconto%20EsitiAsta%202022_PUBBLICATO_8d7c06cc9f8470b.pdf
14. Terna, "Mercato della Capacità – Rendiconto degli esiti – Asta Madre 2027", 2025, https://download.terna.it/terna/Rendiconto-Esiti-Asta-Madre_2027_8dd97982c75d724.pdf
15. Bundesnetzagentur, press release on 2024 electricity market data (SMARD), 3 January 2025, https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/DE/2025/20250103_smard.html
