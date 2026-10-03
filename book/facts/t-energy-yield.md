# Wind and solar energy yield assessment: P50/P90 conventions, uncertainty components, IEC 61400-12/-15, PV degradation norms, and evidence on P50 bias

As of: 2026-10-03 (latest events covered: kWh Analytics Solar Risk Assessment 2025, June 2025; IEC 61400-15-1:2025, March 2025; IEC TC 88 new work item proposal for 61400-15-2, June 2024)

## Summary

An energy yield assessment (EYA) estimates a plant's long-term annual energy production (AEP) as a probability distribution. The P50 is the median: the level expected to be exceeded half the time. P90 and P99 are the levels exceeded 90% and 99% of the time. Under a normal distribution, P90 = P50 − 1.282σ, where σ is the combined uncertainty. Uncertainty components are combined, usually as a root-sum-square of independent items. The future inter-annual variability component depends on the averaging period: a one-year P90 includes the full year-to-year variability, while a ten-year P90 averages much of it out, so it sits closer to the P50. Lenders size debt on these numbers (see t-market-norms.md for DSCR-on-P50/P99 norms).

For wind, IEC 61400-12-1 (Edition 3.0, 2022) governs turbine power-curve measurement. IEC 61400-15-1 (Edition 1.0, March 2025) governs site-suitability input conditions. A companion part, 61400-15-2, on reporting wind resource and energy yield, was still in development (new work item proposed June 2024). Its working-group framework for losses and uncertainties is already widely used.

The evidence shows systematic optimism. NREL's review of over 150 sources (Lee and Fields, 2021) found that wind P50 overprediction has fallen over time towards zero on average, but the uncertainty of individual projects remains above 6%. An NREL study cited there found 3.5–4.5% overprediction in a US subset. For solar, kWh Analytics (2025) found US PV sites underperforming P50 by 8.6% on average, weather-adjusted (2015–2023 data). Berkeley Lab found system-level degradation of −1.3% per year for 21 GWDC of US utility PV, against the −0.5% per year commonly assumed. NREL's PV Fleet study found a median 0.75% per year system performance loss. That rate is about 0.48% per year in cooler climates and 0.88% per year in hotter ones.

## Verified facts

### A. P-value conventions

1. Definitions (NREL, Dobos, Gilman and Kasberg, 2012):
   - P50 is the annual output exceeded with 50% probability; P90 the output exceeded with 90% probability.
   - For a normal distribution with mean µ and standard deviation σ, P90 = µ − 1.282σ.
   - NREL's System Advisor Model (SAM) can also compute P50/P90 empirically from multi-year weather data.
   [confidence: high] [source: 1]
2. Standard normal quantiles for the other P-values: P75 = µ − 0.674σ; P95 = µ − 1.645σ; P99 = µ − 2.326σ. [confidence: high (mathematical identity, computed)] [source: 1; computed]
3. Lee and Fields (2021) note that P50 values are defined with timescales such as 1, 10 and 20 years. In the IEC 61400-15 working-group framework, "project evaluation period" uncertainty covers how closely the wind resource and plant performance over the modelled period (1 or 10 years) will match the long-term average. [confidence: high] [source: 2]
4. Illustrative arithmetic (author's calculation, not a market norm). Assume 8% non-variability uncertainty and 6% one-year inter-annual variability, independent and combined by root-sum-square:
   - One-year σ = √(8² + 6²) = 10.0%, so the one-year P90 is 87.2% of P50.
   - Ten-year σ = √(8² + (6/√10)²) ≈ 8.2%, so the ten-year P90 is about 89.5% of P50.
   This assumes year-to-year independence and normality. [confidence: high as arithmetic] [computed]

### B. Uncertainty and loss components (IEC 61400-15 framework as reported by NREL)

5. Uncertainty categories in the IEC 61400-15 working-group framework (Filippelli et al., 2018, as tabulated by Lee and Fields; "does not represent the final standards"):
   - historical wind resource: long-term period/inter-annual variability, reference data, long-term adjustment, wind speed and direction distribution, on-site data synthesis;
   - project evaluation period: variability over the modelled operational period, climate change;
   - measurement: wind speed and direction sensors, other atmospheric parameters, data integrity;
   - horizontal and vertical extrapolation: model inputs, model components, model stress;
   - plant performance: power curve, wakes, availability, electrical and other losses.
   [confidence: high] [source: 2]
6. Loss categories in the same framework:
   - wake effects (internal, external, future);
   - availability (turbine, balance of plant, grid);
   - electrical (efficiency, facility parasitic consumption);
   - turbine performance (suboptimal performance, generic and site-specific power-curve adjustments, high-wind hysteresis);
   - environmental (icing, degradation, environmental shutdowns, exposure);
   - curtailments or operational strategies (load, grid, environmental or permit curtailment).
   Across the eight studies reporting total loss, Lee and Fields found predicted total losses of 9.5% to 22.5%. Wake loss is among the largest and most variable losses. [confidence: high] [source: 2]

### C. IEC standards (current editions: IEC Webstore, webstore.iec.ch)

7. IEC 61400-12-1:2022 (Edition 3.0, published 5 September 2022), "Power performance measurements of electricity producing wind turbines", specifies how to measure a single turbine's power curve and derive AEP ("AEP-measured" and "AEP-extrapolated"), including uncertainty assessment. A CENELEC corrigendum (EN IEC 61400-12-1:2022/AC:2025-06) followed in 2025. [confidence: high] [source: 3, 4]
8. IEC 61400-15-1:2025 (Edition 1.0, March 2025), "Site suitability input conditions for wind power plants", sets a framework for assessing and reporting site and turbine suitability conditions for onshore and offshore (fixed and floating) wind plants, with traceable documentation. [confidence: high] [source: 5]
9. IEC 61400-15-2 ("Framework for assessment and reporting of the wind resource and energy yield"):
   - It was the subject of new work item proposal 88/1038/NP, proposed by the United States and circulated on 21 June 2024, with voting closing on 16 August 2024.
   - A companion JSON-schema "EYA DEF" digital exchange format for EYA reporting is published on GitHub in draft status.
   - Publication of 61400-15-2 as a standard was not confirmed as of this sheet's date.
   [confidence: high for the proposal; status after 2024 unverified] [source: 6, 7]
10. (Context) IEC TS 61400-28:2025 covers life extension; see t-repowering.md.

### D. Evidence on P50 bias

11. Wind: Lee and Fields (NREL, Wind Energy Science 6, 311–365, published 5 March 2021) reviewed over 150 sources. They found:
    - a long-term reduction in mean P50 overprediction bias, converging towards zero (R² = 0.578 for the regression on the larger-sample subset; not strictly statistically significant);
    - a mean standard deviation of P50 error of 6.6% across 15 data sources, still above 6% for studies after 2016;
    - a 95% prediction interval exceeding 10%.
    They also cite an NREL study (Lunacek et al., 2018) finding 3.5% to 4.5% average P50 overprediction in a US subset, after accounting for curtailment. [confidence: high] [source: 2]
12. Lee and Fields cite (Healer, 2018) an offtake risk. If a PPA lets the buyer terminate after underproduction over a rolling two-year period, a 1% chance per period gives about a 16.5% chance over 18 periods: 1 − 0.99¹⁸. [confidence: high] [source: 2]
13. Solar: kWh Analytics' Solar Risk Assessment 2025 (June 2025) analysed more than 34,000 system-months of monthly operating reports from 2015 to 2023. Measured by a weather-adjusted performance index (actual generation divided by P50), US PV sites underperformed P50 by 8.6% on average. Performance declined over the years analysed, and underperformance was greatest in winter and in the South, the latter attributed possibly to curtailment. Suggested causes include underestimated losses (extreme weather, shading, curtailment, DC health, sub-hourly clipping), optimistic availability assumptions and financial incentives that encourage inflated P50 estimates. [confidence: high] [source: 8]
14. Bolinger, Gorman, Millstein and Jordan (Journal of Renewable and Sustainable Energy, 2020) studied 411 US utility-scale PV projects (21.1 GWDC, 16.3 GWAC; commercial operation 2007–2016). They found:
    - first-year performance generally met expectations;
    - system-level degradation was −1.3% per year (±0.2%), worse than the ex ante assumption (commonly −0.5% per year) and earlier studies (−0.8% to −1.0% per year);
    - degradation was lower for newer and larger projects and cooler sites.
    The figure includes soiling, balance-of-plant degradation and downtime, not only module degradation. [confidence: high] [source: 9]

### E. PV degradation norms

15. Jordan and Kurtz, "Photovoltaic Degradation Rates—An Analytical Review" (Progress in Photovoltaics 21(1), January 2013), compiled nearly 2,000 published degradation rates and found a median of 0.5% per year. [confidence: high] [source: 10, 11]
16. Jordan et al., "Photovoltaic fleet degradation insights" (Progress in Photovoltaics, 2022; NREL PV Fleet Performance Data Initiative) used data from more than 7.2 GW, 1,700 sites and 19,000 inverters, about 6–7% of the US PV market. They found:
    - median system performance loss rate (PLR) of 0.75% per year;
    - median 0.48% per year in cooler climates and 0.88% per year in hotter climates;
    - tracked silicon and CdTe comparable with fixed-tilt systems.
    The authors attribute the gap from the 0.5% per year literature median partly to that literature being mostly (80%) module-level measurements. [confidence: high] [source: 11]

## Timeline

- May 2012: NREL P50/P90 paper on SAM methods (World Renewable Energy Forum).
- January 2013: Jordan and Kurtz degradation review (median 0.5% per year).
- 2018: IEC 61400-15 working group consensus loss and uncertainty framework (Filippelli et al.).
- 2020: Bolinger et al. find −1.3% per year system-level PV degradation.
- 5 March 2021: Lee and Fields wind P50 bias review published.
- 2022: NREL PV Fleet degradation insights (0.75% per year median).
- 5 September 2022: IEC 61400-12-1 Edition 3.0.
- June 2024: new work item proposal for IEC 61400-15-2.
- March 2025: IEC 61400-15-1 Edition 1.0.
- June 2025: kWh Analytics reports PV underperformance of 8.6% versus P50.

## Financing and structure details

- Lenders typically size on P50 with one DSCR and test a downside case (P90 or P99, one-year or ten-year) with a lower DSCR. Dated norms are in t-market-norms.md (for example, US contracted solar at 1.25x P50 and about 1.0x P99).
- The choice between one-year and ten-year P90/P99 changes debt capacity materially because inter-annual variability shrinks with averaging (fact 4). Which convention a lender uses is a term-sheet point to verify for each deal.
- The independent engineer's EYA, and reliance on it, is the subject of Chapter 48.

## What went wrong or right, and why

- Lee and Fields attribute the falling wind bias to methodological corrections, including better wake and loss modelling and measurement techniques. But they stress that prediction "is becoming more accurate and yet is imprecise" at project level [2].
- kWh Analytics names optimistic losses and availability, and incentives that reward high P50s, as possible causes of solar underperformance [8]. Bolinger et al. show that degradation assumptions (−0.5% per year) were too optimistic at system level [9].

## Teaching angles by chapter

- **Chapter 9 (Probability and uncertainty)**: Derive P90 = P50 − 1.282σ and show the one-year versus ten-year difference with the illustrative 87.2% versus 89.5% numbers. Make the point that averaging reduces only the variability component, not measurement or modelling bias. Use Lee and Fields as a real reference-class: accurate on average after correction, but with project-level σ above 6%.
- **Chapter 45 (Sector-specific modelling)**: Build the yield stack from gross AEP through losses to net P50, then to P90/P99 rows and degradation. Show sensitivity to degradation of 0.5% versus 0.75% versus 1.3% per year over 25 years, citing the three sources and explaining why the figures differ (module-level, fleet-median and system-level).
- **Chapter 48 (Technical, resource and market diligence)**: Teach how to read an EYA: the IEC 61400-15 loss and uncertainty categories, the long-term correction, and the 61400-12-1 power-curve basis. Challenge it with base rates: wind P50 bias history and solar underperformance of 8.6%. Note that 61400-15-2 (reporting) was not yet a published standard when this sheet was written.
- **Chapter 70 (Onshore wind and solar)**: Use the solar evidence (8.6% below P50; −1.3% per year system degradation) and the wind evidence (3.5–4.5% overprediction in a US subset, falling over time). Ask why sponsors, lenders and buyers should haircut P50s or require post-construction re-forecasts, and how a PPA underproduction termination right turns yield uncertainty into credit risk (the 16.5% example).

## Do not state

- That IEC 61400-15-2 has been published, or its final content. Status after June 2024 not verified.
- That the IEC 61400-15 loss and uncertainty tables in Lee and Fields are the final standard. They are the 2018 working-group framework.
- A single "industry standard" PV module degradation rate or warranty curve (for example "0.4% per year linear warranty"). Not verified here; cite the module datasheet or warranty for a given deal.
- That one-year versus ten-year P90 differences have a fixed size. They depend on the uncertainty mix.
- Any figure for US wind P50 bias after 2021, or kWh Analytics figures for later years. Not verified.
- Lender preference for one-year rather than ten-year P99. This is deal-specific and not verified as a norm.

## Sources

1. Dobos, A. P., Gilman, P. and Kasberg, M., "P50/P90 Analysis for Solar Energy Systems Using the System Advisor Model", NREL/CP-6A20-54488, World Renewable Energy Forum, Denver, May 2012 (now hosted at docs.nlr.gov). https://docs.nlr.gov/docs/fy12osti/54488.pdf
2. Lee, J. C. Y. and Fields, M. J., "An overview of wind-energy-production prediction bias, losses, and uncertainties", Wind Energy Science 6, 311–365, 5 March 2021. https://wes.copernicus.org/articles/6/311/2021/
3. IEC, "IEC 61400-12-1:2022 Wind energy generation systems – Part 12-1: Power performance measurements of electricity producing wind turbines", Edition 3.0, 2022. https://webstore.iec.ch/en/publication/68499
4. iTeh Standards catalogue, "EN IEC 61400-12-1:2022/AC:2025-06". https://standards.iteh.ai/catalog/standards/clc/6915090e-3d93-4031-8723-730de2c9da0c/en-iec-61400-12-1-2022-ac-2025-06
5. IEC, "IEC 61400-15-1:2025 Wind energy generation systems – Part 15-1: Site suitability input conditions for wind power plants", Edition 1.0, 2025-03 (sample pages). https://cdn.standards.iteh.ai/samples/iec/iec-61400-15-1-2025/a30a157df8054717a5349ff48878b8eb/iec-61400-15-1-2025.pdf ; https://webstore.iec.ch/en/publication/29169
6. IEC TC 88, document 88/1038/NP, "New work item proposal: Wind energy generation systems – Part 15-2: Framework for assessment and reporting of the wind resource and energy yield", 20 June 2024. https://www.aresca.us/wp-content/uploads/2024/06/88_1038e_NP.pdf
7. IEC 61400-15 working group, "The IEC 61400-15-2 EYA DEF" (GitHub repository README, draft). https://github.com/IEC-61400/eya-def
8. kWh Analytics, "Solar Risk Assessment 2025" (article by P. Hwang, "PV Sites Around the Country are Underperforming by 8.6% on Average"), June 2025. https://kwhanalytics.com/wp-content/uploads/2025/06/Solar-Risk-Assessment-2025.pdf
9. Bolinger, M., Gorman, W., Millstein, D. and Jordan, D., "System-level performance and degradation of 21 GWDC of utility-scale PV plants in the United States", Journal of Renewable and Sustainable Energy, 2020 (OSTI record). https://www.osti.gov/pages/biblio/2561469-system-level-performance-degradation-gwdc-utility-scale-pv-plants-united-states
10. Jordan, D. C. and Kurtz, S. R., "Photovoltaic Degradation Rates—An Analytical Review", Progress in Photovoltaics 21(1), January 2013 (OSTI record). https://www.osti.gov/biblio/1073525
11. Jordan, D. C. et al., "Photovoltaic fleet degradation insights", Progress in Photovoltaics, 2022, DOI 10.1002/pip.3566. https://docs.nlr.gov/docs/fy22osti/81314.pdf
