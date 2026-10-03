# Reference rates (SOFR, SONIA, €STR, EURIBOR), LIBOR cessation dates, conventions

As of: 2026-10-03 (latest data point: rate fixings for 1 October 2026; latest rule event: LIBOR's final publication on 30 September 2024)

## Summary

LIBOR has ended. On 5 March 2021 the UK Financial Conduct Authority (FCA) and ICE Benchmark Administration (IBA) announced that panel-bank LIBOR would stop. All sterling, euro, Swiss franc and yen settings and the 1-week and 2-month US dollar settings ended after 31 December 2021, and the remaining US dollar settings after 30 June 2023. Temporary "synthetic" settings for legacy contracts then ran down, ending with the 1-, 3- and 6-month US dollar synthetic settings, published for the last time on 30 September 2024. The main replacements are overnight risk-free rates (RFRs):
- SOFR (US dollar, secured, Federal Reserve Bank of New York);
- SONIA (sterling, unsecured, Bank of England);
- €STR (euro, unsecured, European Central Bank).

In euros the term rate EURIBOR, administered by the European Money Markets Institute (EMMI), survived reform and remains the dominant floating benchmark for euro loans. Project finance loans now typically reference either an overnight RFR compounded (or simply averaged) "in arrears" with a lookback, or a forward-looking term rate set in advance (CME Term SOFR in dollars, EURIBOR in euros). Because RFRs are nearly credit-risk-free and LIBOR included bank credit risk, legacy contracts that fell back to RFRs added fixed credit adjustment spreads (for USD, 0.11448% for 1-month, 0.26161% for 3-month and 0.42826% for 6-month, set on 5 March 2021). On 1 October 2026 SOFR was 3.87%, €STR 2.442% and the Fed funds target range 3.75-4.00%. On 30 September 2026 SONIA was 3.7329% against Bank Rate of 3.75%. The ECB deposit facility rate was 2.50%, and 3-month EURIBOR averaged about 2.64% in September 2026.

## Verified facts

### LIBOR cessation (UK FCA; global)

1. On 5 March 2021 the FCA confirmed that LIBOR panels would cease or become non-representative immediately after 31 December 2021 for "all sterling, euro, Swiss franc and Japanese yen settings, and the 1-week and 2-month US dollar settings", and immediately after 30 June 2023 for "the remaining US dollar settings". [confidence: high] [source: 1]
2. The 5 March 2021 announcement fixed the ISDA IBOR fallback spread adjustments on that date. [confidence: high] [source: 1]
3. Synthetic sterling LIBOR. The 1-month and 6-month settings were required until end-March 2023. The 3-month setting was required until end-March 2024 and was last published on 28 March 2024. Synthetic yen LIBOR was required until end-2022. [confidence: high] [source: 2]
4. The US dollar overnight and 12-month settings permanently ceased at end-June 2023. Synthetic 1-, 3- and 6-month US dollar LIBOR was published for the final time on 30 September 2024, which the FCA describes as the end of LIBOR overall. [confidence: high] [source: 2]
5. The UK Working Group on Sterling Risk-Free Reference Rates was wound down effective 1 October 2024. The Bank of England encouraged keeping Term SONIA to limited use cases and using SONIA compounded in arrears especially in derivatives. [confidence: high] [source: 6]

### US statutory fallback (United States)

6. The Adjustable Interest Rate (LIBOR) Act (12 U.S.C. ch. 55) replaced LIBOR in "tough legacy" US contracts that lacked workable fallbacks with a Federal Reserve Board-selected SOFR-based benchmark plus a statutory tenor spread adjustment. The spreads are 0.00644% (overnight), 0.11448% (1-month), 0.26161% (3-month), 0.42826% (6-month) and 0.71513% (12-month). The "LIBOR replacement date" is the first London banking day after 30 June 2023, unless the Board determines otherwise. [confidence: high] [source: 3]
7. The Federal Reserve adopted its implementing rule (Regulation ZZ) on 16 December 2022. It identifies SOFR-based replacements for overnight and 1-, 3-, 6- and 12-month LIBOR in covered contracts after 30 June 2023 and gives safe harbor to parties that use the Board-selected replacement. Current rule: Regulation ZZ (12 CFR Part 253; CFR part number medium confidence). [confidence: high] [source: 4]

### SOFR (US dollar)

8. SOFR is "a broad measure of the cost of borrowing cash overnight collateralized by Treasury securities". It is calculated as a volume-weighted median of tri-party repo, GCF Repo and FICC-cleared bilateral Treasury repo transactions, and published by the New York Fed each business day at about 8:00 a.m. ET. [confidence: high] [source: 5]
9. The first SOFR value is for 2 April 2018 (published 3 April 2018). [confidence: high] [source: 5a]
10. The Alternative Reference Rates Committee (ARRC) selected SOFR as its recommended USD LIBOR alternative in 2017. It formally recommended the CME Group's forward-looking Term SOFR rates on 29 July 2021 and limited their recommended use mainly to business loans, related hedges and certain securitizations. Its closing report of 30 November 2023 reiterated that limited scope. [confidence: high] [source: 7, 8]
11. The New York Fed also publishes 30-, 90- and 180-day compounded SOFR Averages and a SOFR Index. For 2 October 2026 these were 3.76116% (30-day), 3.68732% (90-day) and 3.67765% (180-day). [confidence: high] [source: 5a]
12. SOFR for 1 October 2026 was 3.87% on a volume of USD 3,067 billion. The effective federal funds rate for the same day was 3.88%, with a target range of 3.75-4.00%. [confidence: high, data] [source: 5a]

### SONIA (sterling)

13. SONIA, administered by the Bank of England, measures the rate banks pay to borrow sterling overnight unsecured from other financial institutions and institutional investors. It is a trimmed mean of reported transactions, published by 10:00 a.m. on the following London business day. It was reformed in April 2018, and a SONIA Compounded Index was introduced on 3 August 2020. [confidence: high] [source: 6]
14. SONIA for 30 September 2026 was 3.7329%. Bank Rate was 3.75%. [confidence: high, data] [source: 6a]

### €STR (euro)

15. The ECB began publishing €STR on 2 October 2019. It is published daily on TARGET2 business days for the previous day's transactions and calculated as a trimmed mean. EONIA was recalibrated as €STR plus 8.5 basis points until its discontinuation; the last publication was on 3 January 2022. [confidence: high, except the EONIA end date: medium] [source: 9]
16. €STR for 1 October 2026 was 2.442%, from 853 transactions totaling EUR 67.1 billion. [confidence: high, data] [source: 9]
17. The ECB deposit facility rate was 2.50% as of October 2026. It was cut to 2.00% from 11 June 2025, then raised to 2.25% (17 June 2026) and 2.50% (16 September 2026). [confidence: high, data] [source: 10]

### EURIBOR (euro)

18. EURIBOR, administered by EMMI, reflects the rate at which credit institutions in the EU and EFTA could obtain wholesale unsecured euro funding. It is published in five tenors (1 week and 1, 3, 6 and 12 months) at or shortly after 11:00 CET on TARGET2 days. It is calculated by a panel of about 20 banks under a "hybrid methodology". The European Commission designated EURIBOR a critical benchmark in 2016. [confidence: high] [source: 11]
19. The hybrid methodology has a Level 1 (eligible unsecured transactions with a minimum EUR 10 million notional, reduced from EUR 20 million in 2021) and Level 2 (interpolation and other techniques). Level 3 was discontinued in the methodology version effective 21 February 2024. Further revisions took effect on 5 December 2024 and 29 June 2026. [confidence: high] [source: 12]
20. Monthly average 3-month EURIBOR was about 2.635% in September 2026 (about 2.513% in August 2026). Six-month EURIBOR averaged about 2.922% in September 2026. [confidence: high, data] [source: 10a]

### Loan conventions

21. ARRC's recommended "in arrears" structures for syndicated business loans (22 July 2020) are Daily Simple SOFR and Daily Compounded SOFR. They recommend a business-day lookback without observation shift (illustrated with five business days) and an Actual/360 day count, noting that Actual/365 is the norm for sterling. They also recommend that any floor apply daily. [confidence: high] [source: 13]
22. For Term SOFR and SOFR Averages applied in advance, ARRC recommended using the rate published two US Government Securities Business Days before the interest period starts, on an Actual/360 day count. [confidence: high] [source: 14]
23. The User's Guide to SOFR explains the in-arrears mechanics that give time to compute and pay interest: payment delays, lookbacks (with or without observation shift) and lockouts. It notes 3-5 day lookbacks in SONIA and SOFR floating-rate notes, and that ISDA's derivatives fallback uses a lookback with observation shift. [confidence: high] [source: 15]
24. Where a legacy loan with a LIBOR floor fell back to SOFR plus a spread adjustment, ARRC guidance was to keep economic parity. For example, a 0 bp LIBOR floor with a 25 bp spread adjustment becomes a -25 bp SOFR floor. [confidence: high] [source: 13]
25. Day-count conventions: SOFR and USD money markets use Actual/360 and sterling uses Actual/365 (ARRC). €STR and EURIBOR follow the euro money-market Actual/360 convention. [confidence: high for USD and GBP; medium for EUR, market convention, not verified in an EMMI document for this sheet] [source: 13]

### Market norms and drivers (indicative)

26. Market observations, not rules: Term SOFR (in advance) has been widely used in US dollar project and corporate loans since 2021-22, alongside daily simple or compounded SOFR. Euro project loans overwhelmingly use EURIBOR, and sterling loans mostly use compounded SONIA in arrears. No verified survey with market shares was found for this sheet, so present this as qualitative. [confidence: medium] [source: 6, 8]
27. What moves the rates: central bank policy (SOFR tracks the Fed funds target range; SONIA tracks Bank Rate; €STR trades a few basis points below the ECB deposit facility rate). Repo market liquidity also matters for SOFR, including quarter-end and month-end spikes and the level of reserves. For term rates (Term SOFR, EURIBOR), expectations of future policy matter, and EURIBOR also carries a bank credit and term premium over €STR. The September 2026 data illustrates this: 3-month EURIBOR averaged about 2.64% against €STR of about 2.44%. [confidence: high for the mechanics; the cited data from sources 5a, 9, 10, 10a]

## Timeline

| Date | Event |
|---|---|
| 2017 | ARRC selects SOFR |
| 2 Apr 2018 | First SOFR value (published 3 Apr 2018) |
| Apr 2018 | Reformed SONIA |
| 2 Oct 2019 | €STR first published |
| 22 Jul 2020 | ARRC SOFR in-arrears syndicated loan conventions |
| 3 Aug 2020 | SONIA Compounded Index |
| 5 Mar 2021 | FCA/IBA cessation announcement; ISDA spread adjustments fixed |
| 29 Jul 2021 | ARRC formally recommends CME Term SOFR |
| 31 Dec 2021 | GBP, EUR, CHF, JPY and USD 1-week and 2-month LIBOR panels end |
| 3 Jan 2022 | EONIA's final publication (medium confidence) |
| 2022 | LIBOR Act enacted; Regulation ZZ adopted 16 Dec 2022 |
| End-2022 | Synthetic JPY LIBOR ends |
| End-Mar 2023 | Synthetic GBP 1-month and 6-month LIBOR end |
| 30 Jun 2023 | Remaining USD LIBOR panels end |
| 30 Nov 2023 | ARRC closing report |
| 28 Mar 2024 | Last synthetic GBP 3-month LIBOR |
| 30 Sep 2024 | Last synthetic USD LIBOR; LIBOR ends |
| 1 Oct 2024 | Sterling RFR Working Group wound down |

## Financing and structure details

How these appear in a project finance term sheet:
- **Base rate.** One of the following:
  - Term SOFR (in advance, two US Government Securities Business Days before the period starts);
  - Daily Simple or Compounded SOFR in arrears, with a 5-business-day lookback;
  - Compounded SONIA in arrears;
  - EURIBOR for the period, in advance.
- **Margin and floor.** A margin is added on top, and a zero floor commonly applies to the base rate (per ARRC, applied daily for in-arrears rates).
- **Hedging.** Interest rate swaps must match the loan's rate convention. A Term SOFR loan hedged with a SOFR OIS swap leaves basis risk. ARRC noted firms hedging Term SOFR with SOFR OIS and limited Term SOFR derivatives to dealer-to-end-user use.
- **Legacy contracts.** Pre-2021 deals may carry a credit adjustment spread (for example, 3-month USD at 0.26161%).

## What went wrong or right, and why

- **Right.** The transition met its fixed deadlines. Statutory backstops (the US LIBOR Act and the UK synthetic LIBOR regime) dealt with "tough legacy" contracts, and the FCA's 5 March 2021 announcement made the fallback spreads certain on that day. [source: 1, 2, 3]
- **Caveat.** ARRC's closing report stressed sustaining a balance between overnight SOFR and Term SOFR. It warned against wider Term SOFR use because Term SOFR depends on derivative liquidity in SOFR itself. [source: 8]

## Teaching angles by chapter

- **Ch 6 (Debt and interest rates).** Teach why LIBOR failed (thin underlying transactions) and how RFRs differ: overnight, transaction-based and nearly credit-risk-free, so a term premium and credit spread must be supplied by the market or the contract. Work an example of compounding daily SOFR in arrears with a 5-day lookback against Term SOFR set in advance, on Actual/360. Then work the same exercise for SONIA on Actual/365 and show the effect of day count. Use the legacy fallback spreads (0.26161% for 3-month USD) to explain the credit adjustment spread. Present current levels (SOFR 3.87%, SONIA about 3.73%, €STR about 2.44%, 3-month EURIBOR about 2.64% in September 2026) as dated snapshots and tell the reader where to find live values: the New York Fed, the Bank of England, the ECB and EMMI.

## Do not state

- Current CME Term SOFR fixings. Not verified for this sheet (licensed data). Use only a dated value from CME if needed.
- Market-share percentages for Term SOFR against daily SOFR in project loans. Not verified.
- That EURIBOR will be discontinued. No such announcement was found; EMMI continues to revise and publish it.
- That LIBOR "still exists" in any form after 30 September 2024. It does not.
- A specific LMA lookback convention as "the" market standard. Five banking days is common (ARRC example), but documents vary; verify against the facility.
- The exact enactment date of the US LIBOR Act (March 2022, within the Consolidated Appropriations Act, 2022). Not verified from a primary source for this sheet; say "2022".
- The SONIA reform date as a precise day (often given as 23 April 2018). Verified only to April 2018.

## Sources

1. Financial Conduct Authority, "FCA announcement on future cessation and loss of representativeness of the LIBOR benchmarks," 5 March 2021. https://www.fca.org.uk/news/press-releases/announcements-end-libor
2. Financial Conduct Authority, "LIBOR transition" (status page), accessed 2026-10-03. https://www.fca.org.uk/markets/libor-transition
3. 12 U.S. Code § 5802 (Adjustable Interest Rate (LIBOR) Act definitions), Legal Information Institute, Cornell, accessed 2026-10-03. https://www.law.cornell.edu/uscode/text/12/5802
4. Board of Governors of the Federal Reserve System, press release, "Federal Reserve Board adopts final rule that implements Adjustable Interest Rate (LIBOR) Act," 16 December 2022. https://www.federalreserve.gov/newsevents/pressreleases/bcreg20221216a.htm
5. Federal Reserve Bank of New York, "Secured Overnight Financing Rate Data," accessed 2026-10-03. https://www.newyorkfed.org/markets/reference-rates/sofr
5a. Federal Reserve Bank of New York, Markets Data API (SOFR, EFFR, SOFR Averages and Index), queried 2026-10-03. https://markets.newyorkfed.org/api/rates/secured/sofr/last/3.json ; https://markets.newyorkfed.org/api/rates/secured/sofrai/last/1.json ; https://markets.newyorkfed.org/api/rates/unsecured/effr/last/1.json
6. Bank of England, "SONIA interest rate benchmark" and "Transition to sterling risk-free rates from LIBOR," accessed 2026-10-03. https://www.bankofengland.co.uk/markets/sonia-benchmark ; https://www.bankofengland.co.uk/markets/transition-to-sterling-risk-free-rates-from-libor
6a. Bank of England Database, series IUDSOIA (SONIA) and IUDBEDR (Bank Rate), queried 2026-10-03. https://www.bankofengland.co.uk/boeapps/database/
7. ARRC, "SOFR transition" page, Federal Reserve Bank of New York, accessed 2026-10-03. https://www.newyorkfed.org/arrc/sofr-transition
8. ARRC, "ARRC Closing Report: Final Reflections on the Transition from LIBOR," 30 November 2023. https://www.newyorkfed.org/medialibrary/Microsites/arrc/files/2023/ARRC-Closing-Report.pdf
9. European Central Bank, "Euro short-term rate (€STR)," accessed 2026-10-03, and ECB Data Portal series EST.B.EU000A2X2A25.WT. https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_short-term_rate/html/index.en.html
10. ECB Data Portal, key ECB interest rates, deposit facility (FM.B.U2.EUR.4F.KR.DFR.LEV), queried 2026-10-03. https://data.ecb.europa.eu/
10a. ECB Data Portal, EURIBOR 3-month and 6-month monthly averages (FM.M.U2.EUR.RT.MM.EURIBOR3MD_.HSTA; ...EURIBOR6MD_.HSTA), queried 2026-10-03. https://data.ecb.europa.eu/
11. EMMI, "Euribor®" benchmark page, accessed 2026-10-03. https://www.emmi-benchmarks.eu/benchmarks/euribor/
12. EMMI, "Euribor® Hybrid Methodology" page and version history (D0016A-2019 to D0016G-2019), accessed 2026-10-03. https://www.emmi-benchmarks.eu/benchmarks/euribor/methodology/
13. ARRC, "SOFR 'In Arrears' Conventions for Syndicated Business Loans," 22 July 2020. https://www.newyorkfed.org/medialibrary/Microsites/arrc/files/2020/ARRC_SOFR_Synd_Loan_Conventions.pdf
14. ARRC Business Loans Working Group, "Forward Looking Term SOFR and SOFR Averages (Applied in Advance) Conventions for Syndicated and Bilateral Business Loans," 21 July 2021. https://www.newyorkfed.org/medialibrary/Microsites/arrc/files/2021/Term_SOFR_Avgs_Conventions.pdf
15. ARRC, "An Updated User's Guide to SOFR," 2021 update. https://www.newyorkfed.org/medialibrary/Microsites/arrc/files/2021/users-guide-to-sofr2021-update.pdf
