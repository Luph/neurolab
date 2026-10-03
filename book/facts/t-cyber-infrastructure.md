# Cyber risk in infrastructure: Colonial Pipeline (2021), Ukrainian grid attacks (2015/2016), cyber insurance and war exclusions, NERC CIP

As of: 2026-10-03 (latest events covered: FERC Orders No. 918 and 919, effective 26 May 2026; TSA pipeline security directive renewals of 1 May 2026)

## Summary

Cyber risk reaches infrastructure projects in two ways. Operational technology (OT) can be attacked directly, as in Ukraine in 2015 and 2016. Or an attack on information technology (IT) forces the operator to shut down OT as a precaution, as at Colonial Pipeline in 2021. On 7 May 2021, Colonial found a ransom note on an IT system. Within about 15 minutes it shut down its entire pipeline system of more than 5,500 miles, which carries nearly half the fuel consumed on the US East Coast. The cause was ransomware from the criminal group DarkSide, and the FBI confirmed DarkSide's responsibility on 10 May. Colonial paid a ransom, began restarting on the evening of 12 May, and announced a full restart on 13 May. Its CEO later told the Senate the attacker probably used a legacy VPN profile that was not meant to be in use. On 23 December 2015, Russian state actors (per the US government) remotely opened breakers at three Ukrainian distribution companies, cutting power to about 225,000 customers. In December 2016, the purpose-built "CrashOverride/Industroyer" malware attacked Ukrainian grid control systems using standard grid protocols. For financiers, three institutional responses matter. Regulation: in the US electric sector, NERC's Critical Infrastructure Protection (CIP) standards are mandatory and enforceable, with maximum civil penalties of USD 1,584,648 per violation per day (FERC's 2025 adjustment). Pipelines have been subject to TSA security directives since 2021. Insurance: the US cyber market was about USD 9.7 billion of direct written premium in 2022 (NAIC). Lloyd's has required, from 31 March 2023, that standalone cyber-attack policies exclude state-backed cyber-attacks, using model clauses such as the LMA's four. Contracts: force majeure, insurance requirements and security covenants now address cyber explicitly. Project cyber losses may sit in the gap between property policies (which often exclude cyber), cyber policies (with sublimits and exclusions for war and state-backed attacks) and business-interruption cover.

## Verified facts

### Colonial Pipeline (May 2021)

1. Colonial's system spans more than 5,500 miles. It carries product from 29 Gulf Coast refineries to New York Harbor, may transport more than 100 million gallons a day, and supplies "nearly half of the fuel consumed on the East Coast", serving more than 50 million Americans. It has about 260 delivery points across 13 states and Washington, D.C. Colonial does not own the fuel. [confidence: high] [source: 1]

2. Timeline from the CEO's testimony. An employee found the ransom note on an IT-network system just before 5:00 a.m. EDT on Friday 7 May 2021. The control centre then stopped operations so the malware could not spread to the OT network. Shutdown began at about 5:55 a.m. and all 5,500 miles were confirmed shut by 6:10 a.m., about 15 minutes in all. Colonial restored its OT network and began returning all lines to service on the evening of Wednesday 12 May. [confidence: high] [source: 1]

3. DOE dates the restart differently. On 13 May 2021 Colonial announced it had restarted its entire pipeline system and that product delivery had commenced to all markets. The FBI was notified on 9 May and confirmed on 10 May that "Darkside ransomware" was responsible. CISA and the FBI issued a joint advisory on DarkSide on 11 May 2021. [confidence: high] [source: 2]

4. Colonial's CEO, Joseph Blount, testified to the US Senate Homeland Security and Governmental Affairs Committee on 8 June 2021. He said he decided Colonial would pay the ransom, and that the company took steps to follow regulatory guidance before paying. He said the attacker likely exploited "a legacy virtual private network (VPN) profile that was not intended to be in use". Mandiant assisted the response. [confidence: high] [source: 1, 3]

5. The ransom amount was widely reported as about USD 4.4 million in bitcoin. The US Department of Justice announced on 7 June 2021 that it had seized about 63.7 bitcoin, then worth about USD 2.3 million, of the ransom. The primary DOJ release could not be retrieved in this research (bot-blocked), so these figures rest on secondary reporting. [confidence: medium] [source: 1 (payment confirmed, amount not stated)]

6. Federal response. DOE was the lead federal agency (CRS, 11 May 2021). Responders included DOT (hours-of-service and overweight-load waivers), PHMSA, EPA (fuel waivers) and FERC (on 10 May the FERC Chairman called for examining mandatory pipeline cyber standards). CRS noted that until then TSA had not issued pipeline security regulations and relied on voluntary guidelines. [confidence: high] [source: 2, 4]

7. After the attack, TSA issued pipeline security directives. The Pipeline-2021-01 series covers enhancing pipeline cybersecurity. The Pipeline-2021-02 series covers mitigation actions, contingency planning and testing. Both have been reissued repeatedly, most recently as versions "G" dated 1 May 2026. [confidence: medium-high (TSA list read via a summarizing fetch)] [source: 5]

8. CISA's two-year retrospective (May 2023) dates the attack to 7 May 2021. It lists the follow-on measures: stopransomware.gov, the Joint Ransomware Task Force with the FBI, the Joint Cyber Defense Collaborative, expanded CyberSentry, and Cybersecurity Performance Goals. [confidence: high] [source: 6]

### Ukraine 2015 and 2016

9. On 23 December 2015, attacks on three Ukrainian regional electricity distribution companies (oblenergos) caused unscheduled outages for approximately 225,000 customers. Six Ukrainian organizations were intruded upon in total. The attacks at different facilities occurred within 30 minutes of each other. [confidence: high] [source: 7]

10. Methods (US alert IR-ALERT-H-16-056-01): attackers operated breakers remotely using existing remote administration tools or ICS client software over VPN connections. BlackEnergy malware was delivered by spear-phishing emails with malicious Microsoft Office attachments. KillDisk erased files and corrupted master boot records. Firmware of serial-to-Ethernet devices at substations was corrupted. Uninterruptible power supplies were disconnected through their remote management interfaces. The US government attributes the activity to Russian nation-state cyber actors (alert last revised 20 July 2021). [confidence: high] [source: 7]

11. The CrashOverride/Industroyer malware was used against Ukrainian critical infrastructure in 2016 (US alert TA17-163A, 12 June 2017). It speaks the grid protocols IEC 60870-5-101, IEC 60870-5-104 and IEC 61850, plus OPC DA. It can issue valid commands directly to remote terminal units, including rapid open-close sequences on circuit breakers. CISA noted these protocols are more common outside the US, and that there was no evidence the malware had affected US critical infrastructure. [confidence: high] [source: 8]

12. The 2016 incident is widely described as hitting a transmission substation near Kyiv on 17–18 December 2016, causing an outage of about an hour. The date, site and duration were not verified from a primary source here. [confidence: medium] [source: 8 (year and target only)]

### Cyber insurance market and war / state-backed exclusions

13. US market size (NAIC, 3 November 2023, data year 2022). The US cyber insurance market, including US-domiciled and alien surplus lines insurers, wrote about USD 9.7 billion in direct written premiums in 2022, up 47.6%. US-domiciled insurers wrote about USD 7.2 billion (up 49.9%), of which about USD 5.1 billion was standalone (up 61.5%) and about USD 2.1 billion package (up 28.1%). Alien surplus lines insurers, including Lloyd's, wrote about USD 2.4 billion (up 41.1%). The top-20 groups' average direct loss ratio was 44.6% in 2022, against 66.4% in 2021. The NAIC describes the US as the largest cyber insurance market in the world. [confidence: high] [source: 9]

14. NAIC's consumer page states that 2020 cyber premiums were approximately USD 6.5 billion, a 61% increase over 2019. [confidence: medium-high (summarizing fetch)] [source: 10]

15. Lloyd's Market Bulletin Y5381, "State backed cyber-attack exclusions", 16 August 2022, from Tony Chaudhry (Underwriting Director). It requires all standalone cyber-attack policies in Lloyd's risk codes CY and CZ to include, unless agreed by Lloyd's, a suitable clause excluding liability for losses from any state-backed cyber-attack, in addition to any war exclusion. It applies from 31 March 2023 at inception or renewal. Existing in-force policies need not be endorsed unless they expire more than 12 months after 31 March 2023. [confidence: high] [source: 11]

16. Y5381 minimum requirements. The clause must (1) exclude losses from war, declared or not, where there is no separate war exclusion; (2) exclude losses from state-backed cyber-attacks that significantly impair the ability of a state to function or its security capabilities; (3) be clear on cover for computer systems outside the affected state; (4) set a robust basis for attributing an attack to a state; and (5) define all key terms. Managing agents must show the clauses have been legally reviewed, and must align them with their reinsurance programmes. [confidence: high] [source: 11]

17. Y5381 states that the LMA produced model clauses for state-backed cyber-attacks, "issued as LMA21-043-PD", and that adopting "any of the four model clauses" meets Lloyd's requirements. Those four clauses are commonly numbered LMA5564–LMA5567, the "War, Cyber War and Cyber Operation Exclusion" Nos. 1–4, issued in November 2021, with No. 1 the broadest exclusion and No. 4 offering the most cover. The clause numbers and their ordering were not verified from an LMA primary source in this research. [confidence: high for "four model clauses, LMA21-043-PD"; medium for the LMA5564–5567 numbering and issue month] [source: 11]

18. Y5381 also records that from 2020, on a phased basis, Lloyd's required all policies to state clearly whether cyber cover is provided, affirmatively or by exclusion (Market Bulletin Y5258, the "silent cyber" initiative). It cites the PRA's Supervisory Statement SS4/17 (July 2017) on cyber insurance underwriting risk. [confidence: high] [source: 11]

### NERC CIP and FERC (US bulk electric system)

19. Legal basis. The Energy Policy Act of 2005 (enacted 8 August 2005) added section 215 to the Federal Power Act (16 U.S.C. 824o). It requires a FERC-certified Electric Reliability Organization (NERC) to develop mandatory and enforceable Reliability Standards, including for cybersecurity. FERC implemented this in Order No. 672 (3 February 2006). FERC approved the first eight CIP standards (version 1) in Order No. 706 on 18 January 2008, and CIP version 5 in Order No. 791 on 22 November 2013, the last major revision. Version 5 categorizes BES Cyber Systems as high, medium or low impact. High impact includes large control centres. Medium impact includes smaller control centres, ultra-high-voltage transmission and large substations and generating facilities. Everything else is low impact. [confidence: high] [source: 12]

20. Since 2013 FERC has approved new and modified CIP standards on supply chain risk management, cyber incident reporting, communications between control centres (CIP-012-1, approved in early 2020) and physical security of critical transmission facilities. [confidence: high] [source: 12, 13]

21. Recent actions:
   - CIP-015-1 (Internal Network Security Monitoring) was approved by Order No. 907, effective 2 September 2025. FERC also directed extension of internal monitoring to electronic access control/monitoring systems and physical access control systems outside the electronic security perimeter.
   - Order No. 912 (effective 24 November 2025) directed NERC to strengthen supply chain risk management standards.
   - Order No. 918 approved CIP-003-11 (security management controls, addressing coordinated attacks on low-impact facilities).
   - Order No. 919 approved 11 modified CIP standards enabling virtualization, with new and modified glossary definitions.
   Orders 918 and 919 were both published 24 March 2026 and effective 26 May 2026.
   [confidence: high] [source: 13]

22. Penalties. FERC's 2025 inflation adjustment (published 14 January 2025) set the maximum civil penalty under FPA section 316A (16 U.S.C. 825o-1(b)), which covers Reliability Standard violations, at USD 1,584,648 per violation per day, up from USD 1,544,521. A later annual adjustment may apply, so check FERC's most recent civil penalty inflation adjustment rule for the current figure. [confidence: high for the 2025 figure] [source: 14]

23. Where the current rules are found: NERC's US Reliability Standards page (nerc.com/standards) for in-force CIP versions and effective dates; FERC orders via the Federal Register (docket RM-series); and TSA's security directives page for pipelines. [confidence: high] [source: 5, 12, 13]

## Timeline (dated events, if applicable)

| Date | Event |
|---|---|
| 8 Aug 2005 | EPAct 2005 creates FPA s.215 mandatory reliability standards |
| 18 Jan 2008 | FERC Order 706 approves CIP version 1 |
| 22 Nov 2013 | FERC Order 791 approves CIP version 5 |
| 23 Dec 2015 | Ukraine distribution grid attack; about 225,000 customers lose power |
| Dec 2016 | Industroyer/CrashOverride attack on Ukrainian grid |
| 12 Jun 2017 | US alert TA17-163A on CrashOverride |
| 2020 onward | Lloyd's phased requirement to make cyber cover explicit (Y5258) |
| 7 May 2021 | Colonial ransomware; full system shutdown by 6:10 a.m. EDT |
| 10 May 2021 | FBI confirms DarkSide |
| 12–13 May 2021 | Colonial restarts; full restart announced 13 May |
| 8 Jun 2021 | Blount Senate testimony |
| Nov 2021 | LMA model cyber war / state-backed clauses (LMA21-043-PD) |
| 16 Aug 2022 | Lloyd's Market Bulletin Y5381 |
| 31 Mar 2023 | Y5381 requirements take effect |
| 2 Sep 2025 | CIP-015-1 approval effective (Order 907) |
| 1 May 2026 | TSA pipeline SD 2021-01G and 2021-02G |
| 26 May 2026 | Orders 918 (CIP-003-11) and 919 (virtualization) effective |

## Financing and structure details (parties, tranches, amounts, tenors, guarantees, where verified)

Not applicable to a single deal. Practice points for documentation (well established; no single source):
- Lenders' insurance requirements increasingly specify cyber cover or require evidence that property and business-interruption policies do not silently exclude cyber-triggered physical damage.
- Force majeure clauses: whether a cyber-attack counts as force majeure, and whether a state-backed attack is a political force majeure event, determine who bears the loss. Insurance war and state-backed exclusions may leave the same event uninsured.
- Covenants: compliance with NERC CIP or TSA directives, incident notification to the agent, and maintenance of security programs.

## What went wrong or right, and why (well-established analysis only, attributed to named sources)

- Colonial: an IT intrusion caused an OT shutdown, because the company could not be sure the malware had not crossed into OT (Blount, source 1). The shutdown itself was the economic event. The point of entry was a dormant legacy VPN profile (source 1). CRS noted that pipeline cybersecurity had relied on voluntary TSA guidelines (source 4). Mandatory directives followed (source 5).
- Ukraine 2015: coordinated, remote operation of breakers, combined with destructive malware and attacks on UPS and serial devices that slowed recovery (source 7). It shows that grid-scale attacks were already feasible in 2015.
- Insurance: Lloyd's explained in Y5381 that cyber-attack losses "have the potential to greatly exceed what the insurance market is able to absorb", and that state-backed attacks create a similar systemic risk to war (source 11). The consequence for projects is that the most catastrophic scenarios are the least insurable.

## Teaching angles by chapter (for each listed chapter: the transferable lesson and the angle to take, 2–4 sentences)

- **Chapter 14 (Risk taxonomy):** Define cyber risk by its mechanism (IT compromise, OT compromise, precautionary shutdown, data extortion), with examples (Colonial, Ukraine) and typical bearers: the operator first, then insurers within sublimits, and offtakers or users through outages. Emphasize correlation, since one state-backed campaign can hit many assets at once.
- **Chapter 27 (Insurance):** Use Y5381 to teach how war and state-backed exclusions work, including attribution clauses and coverage for systems outside the impaired state. Contrast the cyber market's size (about USD 9.7 billion US DWP in 2022) with infrastructure exposures. Show the coverage gap a lender must close between property/BI and cyber policies.
- **Chapter 62 (Operating the project):** Treat cyber compliance (NERC CIP, TSA directives) as an operating covenant with real penalties (up to USD 1.58 million per violation per day). Use Colonial to discuss incident response, regulator notification, lender reporting, and why a decision to shut down quickly can be right even when it is costly.

## Do not state

- Do not state the Colonial ransom amount (USD 4.4 million / 75 BTC) or the DOJ recovery (63.7 BTC / USD 2.3 million) as primary-verified. They are medium confidence, from reporting.
- Do not say DarkSide was a state actor. It was a criminal ransomware-as-a-service group (CRS, source 4).
- Do not say the Colonial attack penetrated the OT/pipeline control network. Colonial said it shut OT down as a precaution and was investigating.
- Do not give exact 2016 Kyiv outage size, duration or substation as verified.
- Do not give the LMA5564–5567 clause numbers, their titles or their relative breadth as primary-verified (medium).
- Do not cite the Merck v. Ace (NotPetya) war-exclusion decision as verified. The New Jersey appellate opinion (2023) could not be retrieved in this research.
- Do not state current NERC CIP version numbers beyond those named in FERC orders above without checking NERC's standards page.
- Do not quote a 2026 FERC penalty cap. Only the January 2025 figure is verified.

## Sources

1. Joseph A. Blount, Jr., President and CEO, Colonial Pipeline Company, written testimony to the US Senate Committee on Homeland Security and Governmental Affairs, "Threats to Critical Infrastructure: Examining the Colonial Pipeline Cyber Attack", 8 June 2021. https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/Testimony-Blount-2021-06-08.pdf
2. US Department of Energy, Office of Cybersecurity, Energy Security, and Emergency Response, "Colonial Pipeline Cyber Incident" (federal agency actions page), retrieved 3 October 2026. https://www.energy.gov/ceser/colonial-pipeline-cyber-incident
3. US Senate HSGAC, hearing page, 8 June 2021. https://www.hsgac.senate.gov/hearings/threats-to-critical-infrastructure-examining-the-colonial-pipeline-cyber-attack
4. Congressional Research Service, "Colonial Pipeline: The DarkSide Strikes", CRS Insight IN11667, 11 May 2021 (via EveryCRSReport). https://www.everycrsreport.com/reports/IN11667.html
5. Transportation Security Administration, "Security Directives and Emergency Amendments" page, retrieved 3 October 2026. https://www.tsa.gov/sd-and-ea
6. CISA, "The Attack on Colonial Pipeline: What We've Learned & What We've Done Over the Past Two Years", May 2023. https://www.cisa.gov/news-events/news/attack-colonial-pipeline-what-weve-learned-what-weve-done-over-past-two-years
7. CISA (ICS-CERT), "Cyber-Attack Against Ukrainian Critical Infrastructure", IR-ALERT-H-16-056-01, February 2016 (revised 20 July 2021). https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01
8. CISA (US-CERT), "CrashOverride Malware", Alert TA17-163A, 12 June 2017 (updated 20 July 2021). https://www.cisa.gov/news-events/alerts/2017/06/12/crashoverride-malware
9. NAIC staff, memorandum to the Property and Casualty Insurance (C) Committee, "Report on the Cybersecurity Insurance Market", 3 November 2023. https://content.naic.org/sites/default/files/inline-files/Final%202023%20Cyber%20Report.pdf
10. NAIC, "Cybersecurity" insurance topic page, retrieved 3 October 2026. https://content.naic.org/insurance-topics/cybersecurity
11. Lloyd's, Market Bulletin Y5381, "State backed cyber-attack exclusions", 16 August 2022. https://assets.lloyds.com/media/35926dc8-c885-497b-aed8-6d2f87c1415d/Y5381%20Market%20Bulletin%20-%20Cyber-attack%20exclusions.pdf
12. FERC, "Commission Information Collection Activities (FERC-725B); Comment Request; Extension", 91 FR 35681, 12 June 2026 (history of CIP standards and Orders 672, 706, 791). https://www.govinfo.gov/content/pkg/FR-2026-06-12/html/2026-11877.htm
13. Federal Register (FERC): Order No. 907, CIP-015-1, 90 FR 28889 (2 July 2025); Order No. 912, supply chain, 90 FR 45661 (23 September 2025); Order No. 918, CIP-003-11, 91 FR 13952 (24 March 2026); Order No. 919, virtualization, 91 FR 13957 (24 March 2026); CIP-012-1 final rule (February 2020). https://www.federalregister.gov/documents/2025/07/02/2025-12309 ; https://www.federalregister.gov/documents/2026/03/24/2026-05711 ; https://www.federalregister.gov/documents/2026/03/24/2026-05716
14. FERC, "Civil Monetary Penalty Inflation Adjustments", final rule, Federal Register, 14 January 2025 (FR Doc 2025-00516). https://www.govinfo.gov/content/pkg/FR-2025-01-14/html/2025-00516.htm
