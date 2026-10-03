# Lithium-ion BESS degradation and augmentation: cycle and calendar fade, warranty structures, augmentation strategies, NLR (formerly NREL) and Lazard assumptions

As of: 2026-10-03 (latest events covered: Fluence Energy 10-K for the year to 30 September 2025, filed 25 November 2025; NLR 2025 Annual Technology Baseline; Lazard LCOE+ July 2026, LCOS v11.0)

## Summary

Lithium-ion batteries lose usable capacity in two ways. Calendar fade depends on time, temperature and state of charge (SOC). Cycle fade depends on throughput, depth of discharge (DOD), C-rate and temperature. NREL's 2017 cell-ageing work on NMC cells found that high or low average temperature, high average SOC and high maximum DOD all accelerate lithium-loss capacity fade. Field data are still thin. A study of 21 German home storage systems over up to eight years (Figgener et al., Nature Energy, September 2024) found usable capacity falling by about 2–3 percentage points a year.

Because a storage contract or capacity obligation is usually written in MW and MWh, owners keep usable energy up by one of three means:
- **overbuild**: installing extra capacity on day one;
- **augmentation**: adding modules or containers later;
- **replacement**: replacing cells at mid-life.

Integrators sell this as a service. Fluence's FY2025 10-K describes augmentation commitments either to keep capacity above a threshold for a stated term or to perform a fixed number of augmentations. Equipment warranties are typically assurance-type for one to five years, with extended (service-type) warranties and performance guarantees backed by liquidated damages beyond that.

Modelling conventions differ. The NLR (National Laboratory of the Rockies, formerly NREL) 2025 Annual Technology Baseline puts augmentation inside fixed O&M, at 4% of capex per year, so a system holds rated capacity over a 15-year life, with about one cycle a day and 85% round-trip efficiency. Lazard's LCOS v11.0 (July 2026) uses a 10% overbuild plus augmentation costs within O&M, 90% DOD and 350 cycles a year. Lenders require sponsors to budget and reserve for augmentation over the 15–20 year offtake term.

## Verified facts

### A. Degradation mechanisms

1. NREL (Smith et al., "Life Prediction Model for Grid-Connected Li-ion Battery Energy Storage System", NREL/CP-5400-67102, August 2017; presented at the American Control Conference, May 2017) ran ageing tests on commercial graphite/NMC cells (eleven 75 Ah cells under nine conditions from 0°C to 55°C). The model predicted capacity fade with 1.4% RMS error and resistance growth with 15% RMS error. [confidence: high] [source: 1]
2. The same paper says:
   - Li-ion degrades with each charge and discharge cycle;
   - cycle life is greatest near room temperature and falls at temperature extremes;
   - cycle life depends on DOD and C-rate;
   - "high or low average temperature, high average SOC and high maximum DOD all accelerate Li-loss capacity fade";
   - high temperature and SOC accelerate the SEI side reaction, and deep cycling mechanically disturbs the SEI;
   - its model includes resistance growth proportional to the square root of calendar time.
   [confidence: high] [source: 1]
3. Field evidence: Figgener et al., "Multi-year field measurements of home storage systems and their use in capacity estimation", Nature Energy, published 16 September 2024 (RWTH Aachen and co-authors), studied 21 privately operated home storage systems in Germany with up to eight years of data. They found average usable capacity loss of about 2–3% a year. The lead author said most systems reached their warranty thanks to built-in capacity reserves. This is residential first-generation equipment, not utility-scale data. [confidence: medium-high (journal metadata verified; the loss figure from two secondary reports)] [source: 2, 3]

### B. Modelling conventions (US laboratory and advisory benchmarks)

4. NLR 2025 Annual Technology Baseline, utility-scale battery storage:
   - it represents lithium-ion with costs based on lithium iron phosphate (LFP) cells, for durations of 2–10 hours (Base Year 60 MW system);
   - fixed O&M "include battery augmentation costs, which enables the system to operate at its rated capacity throughout its 15-year lifetime", estimated at 4% of capital cost in $/kW;
   - about one cycle a day (a 4-hour device has a 16.7% capacity factor);
   - round-trip efficiency is 85%;
   - "degradation is a function of the usage rate" and systems "might need to be replaced" during the analysis period.
   The source study is Cole, Ramasamy and Olmez Turan, "Cost Projections for Utility-Scale Battery Storage: 2025 Update". [confidence: high] [source: 4]
5. The NLR site identifies itself as the National Laboratory of the Rockies, operated under the same DOE contract (DE-AC36-08GO28308) as NREL. NREL documents are now served from docs.nlr.gov. [confidence: high (as shown on the site)] [source: 4]
6. Lazard LCOE+ (July 2026), LCOS v11.0. Detailed figures are in t-power-tech-norms.md (facts 12–14). In summary:
   - all storage cases use 90% DOD and a 10% overbuild;
   - degradation is modelled through available capacity: in Lazard's 100 MW illustration, 110 MW at year 0, then 109, 107, 104 and 102 MW;
   - O&M includes "augmentation costs (incurred in years needed to maintain usable energy at original storage module cost)" and warranty costs.
   [confidence: high] [source: 5; cross-ref t-power-tech-norms.md]

### C. Warranties, guarantees and augmentation contracts

7. Fluence Energy 10-K (fiscal year ended 30 September 2025, filed 25 November 2025):
   - Some service agreements commit Fluence to augmentation, "typically ... installation of additional batteries, and other components as needed, to compensate for partially lost capacity due to degradation".
   - The obligation takes one of two forms: "maintaining battery capacity above a given threshold for a stated term", or "a fixed number of augmentations over a contract term". Threshold-type arrangements may be service-type warranties.
   - Assurance-type warranties "typically extend from one to five years" from commercial operation or substantial completion.
   - Contracts and long-term service agreements include performance liquidated damages if guaranteed performance thresholds are not met.
   - FY2025 services revenue rose by USD 39.1 million, partly from increased augmentation activity.
   [confidence: high] [source: 6]
8. Practitioner panel (Norton Rose Fulbright Project Finance NewsWire, June 2019):
   - standard lithium-ion warranties then covered about two years for defects and performance, with extended warranties purchasable;
   - some suppliers (for example LG Chem) warranted energy throughput over 10 years rather than a capacity percentage;
   - 10-year warranties requiring 75% of year-one capacity were described as common in C&I projects;
   - a 10-year warranty typically assumed a 14–15 year design life;
   - degradation was described as non-linear;
   - warranties are voided if temperature or SOC windows are breached.
   [confidence: medium (panel commentary, 2019)] [source: 7]
9. Banker view (CIBC, Project Finance NewsWire, August 2021):
   - sponsors must budget for cell augmentation over 15–20 year contract terms;
   - augmentation reserves are built either quickly in the early years or gradually;
   - most deals include manufacturer warranties of 10–15+ years;
   - leverage is around 90% of value for capacity-type deals, with DSCRs of about 1.2x for availability deals;
   - about 90% of storage deals were lithium-ion.
   [confidence: medium (2021 commentary)] [source: 8]

## Timeline

- May/August 2017: NREL life-prediction model for grid Li-ion.
- June 2019: NRF panel on storage warranties.
- August 2021: CIBC on bank evaluation of storage (augmentation reserves).
- 16 September 2024: Figgener et al. field study (2–3% a year).
- 2025: NLR ATB 2025 and Cole et al. 2025 cost update (augmentation in FOM, 15-year life).
- 25 November 2025: Fluence FY2025 10-K.
- July 2026: Lazard LCOS v11.0.

## Financing and structure details

- **Overbuild versus augmentation**: overbuild raises day-one capex but avoids later construction and interconnection work. Augmentation defers capex and benefits from falling cell prices (the ATB projects cost declines), but adds execution risk, integration risk with mixed cell generations, and dependence on the integrator's credit. The augmentation obligation shows up in the LTSA (threshold or fixed-event type) and in a lender-required augmentation reserve [6, 8].
- **Warranty stack**: assurance warranty (1–5 years), extended warranty or capacity guarantee, and performance LDs. Lenders look for a creditworthy supplier and warranty coverage that matches the offtake term [6, 7, 8].
- **Debt sizing**: by revenue quality; see t-market-norms.md (contracted storage 1.15–1.20x P50, merchant storage 2.0x or more) and Chapter 73.
- **Safety and insurance** (thermal runaway, Moss Landing): see t-storage-safety.md and moss-landing.md.

## What went wrong or right, and why

- Figgener et al. found that first-generation home systems mostly met warranty because manufacturers built in capacity reserves. That is in effect a hidden overbuild [3].
- Fluence warns that limited operating history makes warranty-cost estimates uncertain and that real-world performance may differ from test conditions. This is a reminder that degradation curves are extrapolations [6].

## Teaching angles by chapter

- **Chapter 45 (Sector-specific modelling)**: Model usable MWh by year as nameplate × (1 + overbuild) × state of health, with calendar and cycle components, and trigger augmentation when usable energy falls below contracted MWh. Compare the ATB convention (augmentation as 4% of capex per year in FOM) with Lazard's (10% overbuild plus augmentation in the years needed). Show how cycles per year drive both revenue and fade.
- **Chapter 73 (Storage, transmission and interconnectors)**: Frame augmentation versus overbuild as a real option traded against integrator credit and future cell prices. Read an LTSA's augmentation clause in its two forms (threshold or fixed number; Fluence 10-K). Explain why lenders size reserves to the augmentation schedule over a 15–20 year tolling or capacity contract.

## Do not state

- A single "standard" annual degradation rate for utility-scale LFP BESS (for example "2% a year"). It depends on chemistry, cycling, SOC window and temperature. The 2–3% field figure is for residential systems.
- That warranties are uniformly 10 years, 15 years or 20 years. Terms vary by supplier and contract. The 2019 and 2021 commentary is dated.
- Cycle-life numbers for specific chemistries (for example "6,000 cycles for LFP"). Not verified here.
- Specific supplier warranty terms for Tesla, CATL, BYD or others. Not verified.
- The date on which NREL was renamed the National Laboratory of the Rockies. Not verified; say only that the laboratory now publishes under that name.
- Any statistic on utility-scale augmentation frequency or cost per MWh. Not verified.

## Sources

1. Smith, K., Saxon, A., Keyser, M., Lundstrom, B., Cao, Z. and Roc, A., "Life Prediction Model for Grid-Connected Li-ion Battery Energy Storage System", NREL/CP-5400-67102, August 2017 (2017 American Control Conference). https://docs.nlr.gov/docs/fy17osti/67102.pdf
2. Figgener, J. et al., "Multi-year field measurements of home storage systems and their use in capacity estimation", Nature Energy, 16 September 2024, DOI 10.1038/s41560-024-01620-9 (metadata via Crossref). https://www.nature.com/articles/s41560-024-01620-9
3. TechXplore, "Reliably estimating the capacity of household systems to store the excess electricity generated by photovoltaics", October 2024. https://techxplore.com/news/2024-10-reliably-capacity-household-excess-electricity.html
4. National Laboratory of the Rockies (formerly NREL), "Utility-Scale Battery Storage", 2025 Annual Technology Baseline. https://atb.nlr.gov/electricity/2025/utility-scale_battery_storage
5. Lazard, "Levelized Cost of Energy+ (LCOE+)", July 2026 (LCOS v11.0). https://lazard.com/media/kcfconhf/lazards-lcoeplus_vf.pdf
6. Fluence Energy, Inc., Form 10-K for the fiscal year ended 30 September 2025, filed 25 November 2025, SEC EDGAR. https://www.sec.gov/Archives/edgar/data/1868941/000186894125000081/flnc-20250930.htm
7. Norton Rose Fulbright, "Energy storage: Warranties, insurance and O&M issues", Project Finance NewsWire, June 2019. https://www.projectfinance.law/publications/2019/june/energy-storage-warranties-insurance-and-om-issues
8. Wright, J. (CIBC Capital Markets), "How banks evaluate energy storage", Project Finance NewsWire, 13 August 2021. https://www.projectfinance.law/publications/2021/august/how-banks-evaluate-energy-storage/
