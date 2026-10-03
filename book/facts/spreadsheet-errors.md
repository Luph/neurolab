# Spreadsheet errors: Reinhart–Rogoff and Herndon–Ash–Pollin (2013), the JPMorgan CIO VaR spreadsheet (2013 Task Force findings), and EuSpRIG research on error rates

As of: 2026-10-03 (latest event covered: Panko, EuSpRIG 2015 proceedings; the core cases date from 2010–2013)

## Summary

Two widely cited cases show that spreadsheet errors can change policy arguments and risk numbers.

In April 2013, Thomas Herndon, Michael Ash and Robert Pollin of the University of Massachusetts Amherst tried to replicate Carmen Reinhart and Kenneth Rogoff's 2010 paper "Growth in a Time of Debt". Using Reinhart and Rogoff's own working spreadsheet, they found a coding error that left five countries (Australia, Austria, Belgium, Canada, Denmark) out of an average. They also found selective exclusion of available years and an unconventional weighting method. Corrected, average real GDP growth for advanced economies with public debt above 90% of GDP was 2.2%, not the published −0.1%.

In January 2013, JPMorgan Chase's management Task Force reported on the 2012 "London Whale" losses in the Chief Investment Office (CIO), which reached at least USD 6.2 billion. It found that the new CIO value-at-risk (VaR) model ran on spreadsheets using a manual, "error prone" process. One operational error divided by the sum of two rates instead of their average, which "likely had the effect of muting volatility by a factor of two and of lowering the VaR".

Research presented at the European Spreadsheet Risks Interest Group (EuSpRIG) helps explain why these failures are normal rather than freakish. Laboratory studies average a cell error rate of about 3.9%. Intensive audits of 85 operational spreadsheets found errors in 94% of them. People are poor at finding the errors they make.

## Verified facts

Reinhart–Rogoff and Herndon–Ash–Pollin

1. Reinhart, C. M. and Rogoff, K. S., "Growth in a Time of Debt", American Economic Review: Papers & Proceedings, vol. 100, no. 2, May 2010, pp. 573–578. An NBER working paper version is No. 15639. [confidence: high] [source: 3, 1]
2. Herndon, T., Ash, M. and Pollin, R., "Does High Public Debt Consistently Stifle Economic Growth? A Critique of Reinhart and Rogoff", PERI (Political Economy Research Institute) Working Paper 322, dated 15 April 2013. The PERI page records updates on 17 and 22 April 2013. A data and code package was later released, open-source under the BSD 2-clause licence (version of 17 May 2013). The paper was published in the Cambridge Journal of Economics, vol. 38, no. 2, pp. 257–279 (online 24 December 2013; issue dated 2014). [confidence: high] [source: 1, 2, 4]
3. Herndon, Ash and Pollin could not replicate the published results from Reinhart and Rogoff's publicly posted country data. Reinhart and Rogoff then provided their working spreadsheet, and with it the authors "were able to approximate closely the published RR results". [confidence: high] [source: 1]
4. The authors identified three problems: coding errors, selective exclusion of available data, and unconventional weighting of summary statistics. The spreadsheet coding error "entirely excludes five countries, Australia, Austria, Belgium, Canada, and Denmark". The omitted countries were consecutive in alphabetical order. The authors say this error, compounded with the other errors, accounts for a −0.3 percentage-point error in the published average for the highest debt category. [confidence: high] [source: 1]
5. Selective exclusions included early post-war years for Australia (1946–1950), New Zealand (1946–1949) and Canada (1946–1950). Combined with country-average weighting, New Zealand's single remaining high-debt year (−7.6% growth) received the same weight as the UK's 19 high-debt years. [confidence: high] [source: 1]
6. Headline correction: the corrected average real GDP growth for countries with public debt above 90% of GDP is 2.2%, not −0.1% as published. The authors conclude that growth above 90% debt "is not dramatically different" from growth at lower ratios. [confidence: high] [source: 1, 2]

JPMorgan Chase CIO (London Whale)

7. JPMorgan Chase's management Task Force issued its "Report of JPMorgan Chase & Co. Management Task Force Regarding 2012 CIO Losses" on 16 January 2013. The US Senate Permanent Subcommittee on Investigations released a bipartisan staff report, "JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and Abuses", with its 15 March 2013 hearing. It reports that the losses of the Synthetic Credit Portfolio reached at least USD 6.2 billion in 2012. [confidence: high] [source: 5]
8. The new CIO VaR model took effect on 27 January 2012. The Senate report quotes the Task Force (at p. 105). The Model Review Group had noted that "the VaR computation was being done on spreadsheets using a manual process and it was therefore 'error prone' and 'not easily scalable'", and approved the model anyway, with an automation action plan that was never carried out. The Task Force also found that "Data were uploaded manually without sufficient quality control" and that "Spreadsheet-based calculations were conducted with insufficient controls and frequent formula and code changes were made." [confidence: high] [source: 5]
9. The Task Force identified an operational error in calculating relative changes in hazard rates and correlation estimates. After subtracting the old rate from the new rate, "the spreadsheet divided by their sum instead of their average, as the modeler had intended". This error "likely had the effect of muting volatility by a factor of two and of lowering the VaR". The Senate report cites this to Task Force p. 128 and quotes the final clause. EuSpRIG quotes the full passage and cites pp. 131–132. [confidence: high for wording; page reference varies by source] [source: 5, 6]
10. According to the Senate report, the model's developer said he had to enter data manually into multiple spreadsheets each trading day, often taking hours. JPMorgan revoked the new CIO VaR model in May 2012, about four months after activation, and reinstated the prior model. [confidence: high] [source: 5]

EuSpRIG research on error rates

11. EuSpRIG describes itself as a voluntary, non-profit organisation on spreadsheet risk management. It holds annual conferences, with a library of over 200 papers spanning about 25 years. The 2026 conference was held on 9–10 July 2026 at the University of Greenwich, London. [confidence: high] [source: 7]
12. Panko (EuSpRIG 2015 proceedings): human error research suggests base error rates of 1%–5% for tasks such as calculating and programming. Fourteen laboratory spreadsheet-development studies with 967 participants working alone averaged a cell error rate of 3.9%. [confidence: high] [source: 8]
13. Panko's Table 2 combines intensive inspections of 85 operational spreadsheets: Hicks 1995 (1 spreadsheet, 100%), Coopers & Lybrand 1997 (23, 91%), KPMG 1998 (22, 91%), Lukasic 1998 (2, 100%), Butler 2000 (7, 86%) and Lawrence and Lee 2001 (30, 100%). Errors were found in 94% of spreadsheets on a weighted-average basis. Where cell error rates were measured, they were 1.2%, 2.2% and 2.5%. [confidence: high] [source: 8]
14. Lower rates have also been reported. Powell, Baker and Lawson (2008) found a 0.9% cell error rate once hardcoding was excluded, after about 3.25 hours of review per spreadsheet. Clermont, Hanin and Mittermeier (2000) found 0.4% using only static-analysis software. Panko argues that these lower figures reflect lighter inspection. [confidence: high (as reported by Panko)] [source: 8]
15. On detection, Panko cites software-inspection research in which single inspectors find only about 20%–40% of errors in a code module. This is why code inspection is done in teams of three to five or more. He also cites experimental results classifying errors as 45% logic, 23% mechanical and 31% omission (Panko and Halverson, 2001). [confidence: high (as reported by Panko)] [source: 8]

## Timeline

- May 2010: Reinhart and Rogoff publish "Growth in a Time of Debt" (AER Papers & Proceedings).
- 27 January 2012: JPMorgan's new CIO VaR model takes effect.
- May 2012: The CIO VaR model is revoked and the prior model reinstated.
- 16 January 2013: JPMorgan Task Force report published.
- 15 March 2013: US Senate Permanent Subcommittee on Investigations hearing and staff report.
- 15 April 2013: Herndon, Ash and Pollin publish PERI Working Paper 322 (updated 17 and 22 April).
- 17 May 2013: The updated data and code package is released.
- 24 December 2013: The paper appears online in the Cambridge Journal of Economics (vol. 38(2), 2014).
- 2015: Panko, "What We Don't Know About Spreadsheet Errors Today", EuSpRIG proceedings.

## Financing and structure details

Not applicable as a financing case. The relevance to project finance is model risk in financial models and in risk models used for credit and hedging.

## What went wrong or right, and why

- Reinhart–Rogoff: according to Herndon, Ash and Pollin, the errors were found only because the original authors shared their working spreadsheet. The public data alone did not allow replication. The spreadsheet error mattered less than the exclusions and weighting choices, which shows that an audit must cover methodology and data selection as well as formulas. [source: 1]
- JPMorgan CIO: the Task Force, as quoted by the Senate staff report, attributes the failure to process rather than to one bad cell. The model was approved despite known operational weaknesses, it was run by its creator who reported to the front office, data entry was manual, formulas changed often, and the automation plan was never checked. [source: 5]
- EuSpRIG/Panko: error is a base-rate phenomenon. In a long chain of dependent cells, even a 1% cell error rate makes a bottom-line error likely, and single reviewers miss most errors. Panko's prescription is much more testing, including team-based inspection. [source: 8]

## Teaching angles by chapter

- Ch 13 (Excel for project finance): Use the five-country omission to teach range errors. A SUM or AVERAGE over a range that stops short is invisible unless you check row counts or control totals. Use the JPMorgan sum-versus-average error to teach formula-intent checks, consistent formulas across rows, and no manual copy-paste into calculation sheets. Introduce Panko's numbers (about 3.9% lab cell error rate; errors in 94% of audited spreadsheets) to justify error checks and flags as standard layout.
- Ch 44 (auditing a model): Build an audit checklist from these cases:
  1. Can the results be replicated from the stated data?
  2. Are all intended rows and columns included?
  3. Does each formula match the documented method (sum versus average)?
  4. Who operates the model, and is there independence from the people whose positions it measures?
  5. Is data entry manual?
  6. Were remediation actions verified?

  Stress that single-reviewer audits miss most errors (20–40% detection in software inspection), which supports a team review and independent model audit before financial close.

## Do not state

- That the spreadsheet coding error alone overturned Reinhart and Rogoff's findings. Herndon, Ash and Pollin attribute the change to three issues combined, with the coding error contributing about −0.3 percentage points.
- Any quotation from Reinhart and Rogoff's response to the critique. Their response was not retrieved in this session. Writers may say that they replied publicly, but should check the exact wording before quoting.
- That the JPMorgan loss was "caused by an Excel error". The Task Force and the Senate report describe the spreadsheet errors as one element of broader failures in risk control, model governance and trading.
- Page numbers for the Task Force passage. The Senate report says p. 128 and EuSpRIG says pp. 131–132, so cite "the Task Force report" without a page, or check the original.
- The widely repeated figure "88% of spreadsheets contain errors" without a source. The verified figure here is 94% across 85 audited spreadsheets (Panko 2015).
- That JPMorgan used Microsoft Excel specifically. The sources reviewed say "spreadsheets".

## Sources

1. T. Herndon, M. Ash and R. Pollin, "Does High Public Debt Consistently Stifle Economic Growth? A Critique of Reinhart and Rogoff", PERI Working Paper 322, University of Massachusetts Amherst, 15 April 2013, https://peri.umass.edu/images/WP322.pdf
2. PERI, publication page for Working Paper 322 (abstract, update notes, data and code package), https://peri.umass.edu/publication/item/526-does-high-public-debt-consistently-stifle-economic-growth-a-critique-of-reinhart-and-rogoff
3. C. M. Reinhart and K. S. Rogoff, "Growth in a Time of Debt", American Economic Review, 100(2): 573–578, May 2010, https://doi.org/10.1257/aer.100.2.573
4. T. Herndon, M. Ash and R. Pollin, "Does high public debt consistently stifle economic growth? A critique of Reinhart and Rogoff", Cambridge Journal of Economics, 38(2): 257–279, 2014 (online 24 December 2013), https://doi.org/10.1093/cje/bet075
5. United States Senate Permanent Subcommittee on Investigations, "JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and Abuses", Majority and Minority Staff Report, released with the 15 March 2013 hearing, https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/REPORT%20-%20JPMorgan%20Chase%20Whale%20Trades%20(4-12-13).pdf (quoting "Report of JPMorgan Chase & Co. Management Task Force Regarding 2012 CIO Losses", 16 January 2013)
6. EuSpRIG, "Horror Stories" (entries for JP Morgan and Reinhart–Rogoff), accessed 3 October 2026, https://eusprig.org/research-info/horror-stories/
7. EuSpRIG, home page, accessed 3 October 2026, https://www.eusprig.org/
8. R. R. Panko, "What We Don't Know About Spreadsheet Errors Today: The Facts, Why We Don't Believe Them, and What We Need to Do", Proceedings of the EuSpRIG 2015 Conference, arXiv:1602.02601, https://arxiv.org/abs/1602.02601
