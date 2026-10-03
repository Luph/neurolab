# CAPM inputs: market risk premium estimates, US 10-year Treasury yields, and infrastructure equity return evidence

As of: 2026-10-03 (latest data: Treasury par yields for 2 October 2026; Damodaran implied ERP for 1 September 2026)

## Summary

The capital asset pricing model needs a risk-free rate, a beta and an equity (market) risk premium (ERP). This sheet gives dated, sourced values for two of the three. The risk-free rate is the US 10-year Treasury par yield from the US Treasury's official daily yield curve. The ERP is taken from Aswath Damodaran's implied ERP series (NYU Stern), which backs out the premium from S&P 500 prices and expected cash flows each month. Kroll (formerly Duff & Phelps) publishes a widely cited "recommended" US ERP used with a "normalized" risk-free rate. Kroll's website blocked access in this research, so only one Kroll data point is verified, via SEC-filed fairness analyses: 5.5% as of February 2024. The 10-year yield ran from a low of 0.52% (4 August 2020) to 5.28% on 2 October 2026, having risen about 50 basis points in September 2026 alone. Damodaran's implied ERP has stayed in a band of roughly 4.0–6.0% since 2016 (trailing-cash-yield basis, start of each year), and was 4.09–4.14% on 1 September 2026. A simple CAPM at today's inputs (10-year 5.28%, ERP about 4.1%) gives a cost of equity of about 7.7–9.4% for betas of 0.6–1.0. That is below the 10–13% nominal equity IRRs actually bid or agreed on project-financed UK PPP and nuclear deals. The gap is the point to teach: project equity hurdle rates add development, construction, leverage, illiquidity and country premiums that a single market beta does not capture.

## Verified facts

### A. US 10-year Treasury (risk-free rate)

1. Source and definition. US Department of the Treasury, Daily Treasury Par Yield Curve Rates (constant-maturity, bond-equivalent basis), downloaded for 2016–2026 on 3 October 2026. [confidence: high] [source: 1]

2. 10-year par yield at key dates:

| Date | 10Y | Note |
|---|---|---|
| 4 Jan 2016 | 2.24% | first 2016 trading day |
| 30 Dec 2016 | 2.45% | |
| 29 Dec 2017 | 2.40% | |
| 31 Dec 2018 | 2.69% | |
| 31 Dec 2019 | 1.92% | |
| 9 Mar 2020 | 0.54% | COVID market shock |
| 4 Aug 2020 | 0.52% | 2016–2026 low |
| 31 Dec 2020 | 0.93% | |
| 31 Dec 2021 | 1.52% | |
| 30 Dec 2022 | 3.88% | |
| 30 Jun 2023 | 3.81% | |
| 19 Oct 2023 | 4.98% | 2023 high |
| 29 Dec 2023 | 3.88% | |
| 31 Dec 2024 | 4.58% | |
| 31 Dec 2025 | 4.18% | |
| 30 Jun 2026 | 4.44% | |
| 1 Sep 2026 | 4.79% | |
| 30 Sep 2026 | 5.29% | |
| 2 Oct 2026 | 5.28% | latest |

[confidence: high, official data] [source: 1]

3. 10-year annual averages, minimums and maximums (computed from the daily series): 2016 average 1.84% (range 1.37–2.60%); 2017 2.33% (2.05–2.62%); 2018 2.91% (2.44–3.24%); 2019 2.14% (1.47–2.79%); 2020 0.89% (0.52–1.88%); 2021 1.45% (0.93–1.74%); 2022 2.95% (1.63–4.25%); 2023 3.96% (3.30–4.98%); 2024 4.21% (3.63–4.70%); 2025 4.29% (3.97–4.79%); 2026 to 2 October 4.47% (3.97–5.29%). [confidence: high, computed from official data] [source: 1]

4. Other tenors on 2 October 2026: 6-month 4.27%, 2-year 4.83%, 20-year 5.67%, 30-year 5.63%. The curve was upward-sloping from 6 months to 20 years. Long infrastructure cash flows often justify a 20- or 30-year risk-free rate rather than the 10-year. [confidence: high] [source: 1]

### B. Damodaran implied equity risk premium (US)

5. Method. Damodaran (NYU Stern) estimates an implied ERP each month by solving for the discount rate that equates the S&P 500 level to expected cash flows to equity, meaning dividends plus buybacks, with analyst growth followed by stable growth. He then subtracts the 10-year Treasury rate. The annual series runs from 1960. [confidence: high] [source: 2, 3]

6. Annual implied ERP, FCFE basis, as at the start of each year. Damodaran's spreadsheet labels each value by the year that is ending, so the "2025" row is the 1 January 2026 estimate. The T-bond rate he used is shown alongside:

| Estimate date | Implied ERP (FCFE) | ERP, sustainable-payout variant | 10Y T-bond used |
|---|---|---|---|
| 1 Jan 2016 | 6.12% | 5.16% | 2.27% |
| 1 Jan 2017 | 5.69% | 4.50% | 2.45% |
| 1 Jan 2018 | 5.08% | 4.75% | 2.41% |
| 1 Jan 2019 | 5.96% | 5.55% | 2.68% |
| 1 Jan 2020 | 5.20% | 5.06% | 1.92% |
| 1 Jan 2021 | 4.72% | 4.94% | 0.93% |
| 1 Jan 2022 | 4.24% | 4.90% | 1.51% |
| 1 Jan 2023 | 5.94% | 5.11% | 3.88% |
| 1 Jan 2024 | 4.60% | 4.57% | 3.88% |
| 1 Jan 2025 | 4.33% | 4.00% | 4.58% |
| 1 Jan 2026 | 4.23% | 4.18% | 4.18% |

The spreadsheet's "Date updated" field reads January 2026 (last saved 7 January 2026). The monthly file also reports the 1 January 2026 value as 4.23% (trailing-12-month cash yield) and 4.18% (sustainable payout). [confidence: high] [source: 2, 3]

7. Monthly implied ERP in 2026 (start of month; trailing-12-month cash-yield basis; with Damodaran's T-bond rate): Jan 4.23% (4.18%); Feb 4.25% (4.26%); Mar 4.37% (3.95%); Apr 4.77% (4.32%); May 4.36% (4.40%); Jun 4.31% (4.44%); Jul 4.20% (4.45%); Aug 4.23% (4.74%); Sep 4.09% (4.75%). [confidence: high] [source: 3]

8. On his home page (retrieved 3 October 2026), Damodaran gives the implied ERP on 1 September 2026 in five variants: 4.14% (trailing 12 months, adjusted payout); 4.09% (trailing 12-month cash yield); 6.05% (average cash-flow yield over the last 10 years); 3.80% (net cash yield); and 3.56% (normalized earnings and payout). All use a US Treasury rate of 4.75%. He notes that a user netting the US sovereign default spread (0.22%) out of the Treasury rate, for an adjusted dollar risk-free rate of 4.53%, should add that spread to each premium. [confidence: high] [source: 4]

9. Selected mid-year values (1 July; trailing-12-month cash-yield basis): 2016 6.27%; 2017 5.13%; 2018 5.37%; 2019 5.67%; 2020 5.37%; 2021 3.96%; 2022 6.01%; 2023 5.00%; 2024 4.12%; 2025 4.21%; 2026 4.20%. [confidence: high] [source: 3]

10. Drivers. The implied ERP rises when stock prices fall faster than expected cash flows (start of 2019 and mid-2022). It also rose briefly in April 2026, to 4.77%, when the S&P 500 dropped from 6,879 on 1 March to 6,528 on 1 April 2026. It falls when prices run ahead of cash flows (2021). It is not mechanically tied to the risk-free rate. The ratio of ERP to the risk-free rate fell below 1 in the 1 January 2025 estimate (0.95), meaning the premium was smaller than the Treasury yield. It was 5.08 at 1 January 2021 and 1.01 at 1 January 2026. [confidence: high] [source: 2, 3]

### C. Kroll (formerly Duff & Phelps) recommended US ERP

11. Kroll publishes a "recommended" US ERP for use with a "normalized" risk-free rate, or with the spot 20-year yield if that is higher. It changes the recommendation at irregular intervals. Kroll's page could not be accessed (HTTP 403), so the full history is not verified here. [confidence: high for the existence of the recommendation; history not verified] [source: 5, 6]

12. Two independent SEC filings record the Kroll recommended US ERP as 5.5% "as at 28-Feb-24" / "as of February 2024". One is the MariaDB plc tender-offer filing (SC TO-T, 24 May 2024). The other is the Thoughtworks Holding, Inc. going-private filing (SC 13E3, 3 September 2024), which paired it with a Kroll historical long-horizon ERP of 7.17% as of December 2023. [confidence: high for 5.5% at February 2024] [source: 5, 6]

13. For any other Kroll recommendation date or level (before 2024, or changes during and after 2024), see "Do not state". Practitioners should take the current figure from Kroll's Cost of Capital Navigator or its published "Recommended U.S. Equity Risk Premium and Corresponding Risk-Free Rates" page. [confidence: n/a]

### D. Infrastructure and project equity return evidence (published)

14. UK PF2 expected equity returns (NAO, January 2018), as forecast post-tax base-case equity IRRs at financial close: PSBP schools South 10.3%, North East 12.0%, North West 12.4%, Midlands 11.7% and Yorkshire 11.2%; Midland Metropolitan Hospital 10%. [confidence: high] [source: 7]

15. Equity competition (NAO 2018). For a 40% equity stake in the Midland Metropolitan Hospital PF2 project there were five bidders. The winning bid's expected return of 8.6% cut the price of the project equity from 12% to 10%. [confidence: high] [source: 7]

16. Secondary-market returns (NAO 2018). On the M25 PFI (contract signed 2009), the NAO estimated that original equity holders realised about 31% a year over 2009-10 to 2016-17 on a GBP 100 million investment. This includes the sale of a 50% stake for GBP 330 million in 2016-17 by Skanska and Atkins. The NAO attributes the high return to the lower return required by buyers of operational-phase equity, and possibly to the project being more profitable than forecast. [confidence: high] [source: 7]

17. Cross-references, not duplicated here. Hinkley Point C / Sizewell C expected equity returns (Sizewell C construction WACC 6.73% CPIH-real; equity IRR 10.8–13.0% nominal post-tax) are in facts/hinkley-sizewell.md. Updated PF2 schools equity IRRs as at 31 March 2021 are in facts/uk-pfi.md. Tideway's real regulated WACC is in facts/tideway.md. Lazard's 12% cost-of-equity modelling convention is in facts/t-power-tech-norms.md. [confidence: per those sheets]

18. Infrastructure investor surveys (e.g., EDHECinfra, Preqin and Infrastructure Investor fundraising surveys of target returns by strategy) were not retrievable in this research. Indicative market norms for unlevered and levered target returns by strategy (core, core-plus, value-add, greenfield and emerging markets) should come from facts/t-market-norms.md and t-market-norms-2.md, or be re-verified before publication. [confidence: n/a]

### E. Illustrative CAPM arithmetic (computed)

19. Cost of equity = risk-free rate + beta × ERP. With the 2 October 2026 10-year yield (5.28%) and Damodaran's 1 September 2026 ERP (4.09%), betas of 0.6, 0.8 and 1.0 give 7.73%, 8.55% and 9.37%. With Damodaran's own 1 September inputs (4.75% Treasury, 4.14% ERP) they give 7.23%, 8.06% and 8.89%. The 49 bp rise in the 10-year yield between 1 September and 2 October 2026 changes the answer by about as much as raising beta by 0.1 at a 4–5% ERP. [confidence: high, arithmetic]

## Timeline (dated events, if applicable)

| Date | Event |
|---|---|
| 1 Jan 2016 | Damodaran implied ERP 6.12%; 10Y about 2.27% |
| Jan 2018 | NAO PFI and PF2 report (PF2 equity IRRs 10.0–12.4%) |
| 4 Aug 2020 | 10Y at 0.52% (low of period) |
| 1 Jan 2022 | Implied ERP 4.24%; 10Y 1.51% |
| 1 Jul 2022 | Implied ERP 6.01% after the equity sell-off |
| 19 Oct 2023 | 10Y 4.98% |
| Feb 2024 | Kroll recommended US ERP 5.5% (per SEC filings) |
| 1 Jan 2026 | Implied ERP 4.23%; 10Y 4.18% |
| 1 Sep 2026 | Implied ERP 4.09–4.14%; Damodaran T-bond 4.75% |
| 2 Oct 2026 | 10Y 5.28%; 30Y 5.63% |

## Financing and structure details (parties, tranches, amounts, tenors, guarantees, where verified)

Not applicable (topic sheet). Model note: store the risk-free date, the tenor (10Y or 20Y/30Y), the ERP source and variant, and the beta source (unlevered or relevered at the project's gearing) as separate dated inputs.

## What went wrong or right, and why (well-established analysis only, attributed to named sources)

- High realised secondary returns (M25, about 31% a year) were attributed by the NAO to lower required returns once construction risk has passed. The NAO also noted the risk that high returns reflect inefficient initial pricing of equity (source 7). This is the classic stage-dependent hurdle-rate story.
- The equity competition on Midland Metropolitan lowered the equity price from 12% to 10%. The NAO then noted that equity was typically only 10% of PF2 financing, so total financing cost depends mostly on debt (source 7).
- Damodaran's position is that implied (forward-looking) premiums adapt to market conditions better than historical averages (source 2). Kroll combines a recommended ERP with a normalized risk-free rate. Practitioners disagree on which is preferable. A defensible textbook stance is to show both, state the date and basis, and stress-test the result.

## Teaching angles by chapter (for each listed chapter: the transferable lesson and the angle to take, 2–4 sentences)

- **Chapter 8 (Leverage, risk and the cost of capital):** Build CAPM live with the dated inputs. Use 2 October 2026 (5.28% plus beta × 4.09%), then rerun it with 4 August 2020 (0.52% 10-year) to show how much of the "cost of equity" is just the rate cycle. Show that the implied ERP and the risk-free rate do not move one-for-one: the ERP-to-risk-free ratio was 5.08 at the start of 2021 and 1.01 at the start of 2026. Then relever beta to project gearing to show why project equity at 70–80% debt needs a higher return.
- **Chapter 46 (Equity returns and valuation):** Contrast the CAPM output of about 8–9% with the 10–12.4% PF2 bid IRRs and the 10.8–13.0% nuclear equity IRRs. Attribute the gap to development and construction risk, leverage, illiquidity and the size of the ticket. Use the M25 sale (about 31% a year realised) and the Midland Metropolitan equity competition (12% to 10%) to show how required returns fall by stage, and why secondary buyers pay up for de-risked equity.

## Do not state

- Do not state a Kroll/Duff & Phelps recommended ERP history (e.g., specific changes in 2016, 2017, 2018, 2020, 2022, 2023, 2024 or later) as verified. Only "5.5% as of February 2024" is confirmed here. Common recollections such as "lowered to 5.0% in June 2024" were not verified.
- Do not quote Torchlight/Roth's "7.0% based on Duff and Phelps Recommended U.S. ERP" (2021 SEC filing) as the D&P recommendation. It is a banker's estimate and its basis is unclear.
- Do not mix Damodaran variants (FCFE trailing cash yield, sustainable payout, normalized) without naming the variant.
- Do not describe Damodaran's "2025" annual row as the end-2025 ERP without explaining that it is the 1 January 2026 estimate.
- Do not present infrastructure fund target-return ranges from surveys as verified. None were retrieved here.
- Do not treat the 10-year as the only valid risk-free tenor for 25–35-year project cash flows.

## Sources

1. US Department of the Treasury, "Daily Treasury Par Yield Curve Rates", CSV downloads for 2016–2026, retrieved 3 October 2026. https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve
2. Aswath Damodaran, "Historical Implied Equity Risk Premiums" (histimpl.xls), NYU Stern, updated January 2026. https://pages.stern.nyu.edu/~adamodar/pc/datasets/histimpl.xls
3. Aswath Damodaran, "Implied ERP by month" (ERPbymonth.xlsx, September 2008 to September 2026), NYU Stern, retrieved 3 October 2026. https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPbymonth.xlsx
4. Aswath Damodaran, Damodaran Online home page (implied ERP on 1 September 2026), retrieved 3 October 2026. https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm
5. MariaDB plc, Schedule TO-T (tender offer statement), SEC EDGAR, filed 24 May 2024 (cost of capital note citing Kroll "recommended" ERP 5.5% as at 28 February 2024). https://efts.sec.gov/LATEST/search-index?q=%22Kroll%20recommended%20ERP%22
6. Thoughtworks Holding, Inc., Schedule 13E-3, SEC EDGAR, filed 3 September 2024 (cites Kroll recommended ERP 5.50% as of February 2024 and historical ERP 7.17% as of December 2023). https://efts.sec.gov/LATEST/search-index?q=%22Kroll%20recommended%22
7. National Audit Office, "PFI and PF2", report by the Comptroller and Auditor General, 18 January 2018. https://www.nao.org.uk/wp-content/uploads/2018/01/PFI-and-PF2.pdf
