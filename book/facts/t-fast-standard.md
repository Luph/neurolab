# The FAST Standard and other financial modelling standards (ICAEW Financial Modelling Code, SMART/Corality, Best Practice Modelling)

As of: 2026-10-03 (latest events covered: FAST Standard Organisation confirmation statement, 31 March 2026; ICAEW Financial Modelling Code, 2024 reissue; UK AQuA Book guidance republished 30 July 2025)

## Summary

Several published standards exist for spreadsheet financial models, and they agree on most essentials: separate inputs, calculations and outputs; keep formulas consistent along each row; keep formulas short; avoid hidden logic and circularity; and build in checks. The most prescriptive, and the most common in UK and European project finance, is the FAST Standard. FAST stands for Flexible, Appropriate, Structured, Transparent. Its founders, John Richter and Morten Siersted, date its origins to 1999. Since 2011 it has been maintained by the FAST Standard Organisation Ltd (FSO), a UK company limited by guarantee incorporated on 28 April 2011. The Standard is published openly. Its rule book is numbered by chapter (workbook, worksheet, line item, Excel features). Version 02a (29 May 2014) contains about 109 numbered rules plus explicit exceptions. Later versions are 02c (July 2019, released under a Creative Commons Attribution 4.0 licence) and, per its publisher listing, 02d (February 2022). Other standards include:
- the ICAEW Financial Modelling Code (13 November 2018; reissued 2024), a principles-based code built from a review of seven methodologies;
- SMART, developed by Corality (founded in Sydney in 2008, acquired by Mazars in 2016, now Forvis Mazars Financial Modelling);
- the Best Practice Spreadsheet Modelling Standards maintained since 2003 by the Spreadsheet Standards Review Board (SSRB), set up by BPM (now the Modano brand).
A 2010 EuSpRIG paper found that three independently developed methodologies (FAST, Operis and BPM) converged on similar, mechanistic design practices.

## Verified facts

### A. The FAST Standard (source of current text: fast-standard.org; the site blocked automated access in this session)

1. FAST stands for Flexible, Appropriate, Structured and Transparent. The Standard describes itself as "practical, structured design rules for financial modelling". It deals with spreadsheet design, not the wider control environment (back-up, version control, testing). It says models "must be as simple as possible, but no simpler". [confidence: high] [source: 1]
2. Governing body: FAST Standard Organisation Ltd, UK company number 07617819, a private company limited by guarantee without share capital. It was incorporated on 28 April 2011, with its registered office in Bristol and SIC code 94120 (professional membership organisations). It is active, with its last confirmation statement dated 31 March 2026. [confidence: high] [source: 2]
3. History (as stated on the FSO website and in practitioner commentary):
   - FAST was created in 1999 and fully documented publicly in 2011.
   - Its founders were John Richter and Morten Siersted (who founded F1F9 in 1999).
   - They gifted their intellectual property in the Standard to the FSO when it was set up.
   - Before the FSO, the methodology was known as the "FAST Alliance".
   [confidence: medium (FSO site content seen only through search summaries; FAST Alliance naming from a 2010 EuSpRIG paper)] [source: 3, 4, 5]
4. Versioning: the Standard is "saved to a new version every time a major update is performed". The first version was FAST01a, with letters running a to z before reaching 02. Version FAST02a is dated 29 May 2014. [confidence: high] [source: 1]
5. Later versions:
   - Version 02c is dated July 2019. The FSO states that 02c is released under a Creative Commons Attribution 4.0 International licence, with attribution to the FSO.
   - The FSO's Issuu publisher listing shows "FAST Standard 02d February 2022".
   [confidence: medium (02c licence from the FSO licence page via search summary; 02d from the publisher listing only)] [source: 3, 6]
6. Structure of 02a:
   - 1.0 Workbook Design;
   - 2.0 Worksheet Design;
   - 3.0 The Line Item;
   - 4.0 Excel Features Used in Modelling;
   - appendices on formatting, terminology and "Rules in Short".
   Rules are numbered by section, for example "FAST 3.03-01", and exceptions are numbered separately, for example "FAST-3.03-09.1". A count of rule identifiers in 02a gives 109 numbered rules. [confidence: high for structure; count is the author's own tally of 02a] [source: 1]
7. Representative 02a rules (exact rule titles):
   - FAST 1.01-01 "Group or separate worksheets by type: Foundation, Workings, Presentation, and Control"
   - FAST 1.01-02 "Maintain consistent column structure across all sheets"
   - FAST 1.01-07 "Calculate only once"
   - FAST 1.01-11 "Never release a model with purposeful use of circularity"
   - FAST 1.02-01 "Arrange sheets so that calculation order flows left to right"
   - FAST 1.02-03 "Separate flags and factors onto dedicated sheets"
   - FAST 2.01-08 "Do not hide anything"
   - FAST 2.02-05 "Use corkscrew calculation blocks for balance accumulation"
   - FAST 3.02-01 "Formulas must be consistent"
   - FAST 3.03-01 "Do not write a formula longer than your thumb"
   - FAST 3.03-02 "No formula should take more than 24 seconds to explain"
   - FAST 3.03-07 "Never use nested IFs"
   - FAST 3.03-08 "Do not use Excel Names"
   - FAST 3.04-01 "Do not write formulas with embedded constants"
   - FAST 3.06-02 "Do not create daisy chains; do not link to links"
   - FAST 3.07-01 "Use timing flags"
   - FAST 4.01-03 "Do not use OFFSET or INDIRECT functions"
   [confidence: high] [source: 1]
8. On circularity, 02a advises testing for lack of convergence (for example, insufficient debt commitments) rather than setting a model up to converge automatically. On timing, it says conditional timing logic should be moved out of the main formulas into timing flags or partial period factors (PPFs). [confidence: high] [source: 1]
9. Practitioner Kenny Whitelaw-Jones (February 2022), an FSO advisory board member, wrote that FAST relies on extensive "call-ups" (local links) and that "not much development has gone into FAST over recent years". [confidence: medium] [source: 5]

### B. ICAEW Financial Modelling Code (current text: icaew.com/financialmodelling)

10. The ICAEW published the Financial Modelling Code on 13 November 2018. The current PDF is marked © ICAEW 2024. It was developed by the ICAEW Excel Community's advisory group. It says it was "formed from a review of seven methodologies and input from over a dozen financial modelling organisations". It is principles-based and "not intended to be a tick-box compliance tool". It builds on ICAEW's "Twenty principles for good spreadsheet practice". [confidence: high] [source: 7, 8]
11. Its sections:
    - model definition and purpose;
    - layout and structure;
    - user interface and transparency;
    - consistency;
    - clarity;
    - error reduction (review and test, include checks, include a master check);
    - calculation techniques (minimise complexity, avoid hardcoding, avoid circular references, avoid unnecessary rounding, use VBA sparingly).
    On circularity, it recommends disabling iterative calculation, resolving circularities algebraically or with simplifying assumptions, and handling any self-reference with Goal Seek or a copy-paste macro clearly flagged as possibly not live. Contributors included modellers from Operis, Mazars, Modano, KPMG, Grant Thornton, RSM and others. [confidence: high] [source: 7]

### C. SMART (Corality, now Forvis Mazars)

12. Corality was founded in Sydney in 2008. Mazars announced its acquisition of Corality Financial Group in July 2016, completing in August 2016. The combined business operates as Forvis Mazars Financial Modelling, which continues to model to the standard Corality taught. [confidence: high] [source: 9, 10]
13. Practitioner commentary describes SMART as the Mazars financial modelling standard. It has about 15 guiding philosophies, including "use plain English, not Excel-speak" and separating inputs, calculations and outputs. [confidence: medium] [source: 5]

### D. Best Practice Modelling (BPM) and the SSRB

14. The Spreadsheet Standards Review Board (SSRB) was established in 2003 by BPM Analytical Empowerment Pty Ltd to maintain publicly a set of "Best Practice Spreadsheet Modeling Standards". The Standards were first published in July 2003. Practitioner commentary describes BPM as the first systematic codification (2003), now continued under the Modano brand. The latest version number could not be confirmed. [confidence: medium (ssrb.org unavailable in this session)] [source: 4, 5]

### E. Comparative and public-sector benchmarks

15. Grossman and Özlük, "Spreadsheets Grow Up: Three Spreadsheet Engineering Methodologies for Large Financial Planning Models" (EuSpRIG 2010), compared FAST, Operis and BPM. They found the three share many design practices and standardised, mechanistic construction procedures, and that written standards alone are not enough to understand a methodology fully. [confidence: high] [source: 4]
16. UK government: HM Treasury's AQuA Book (first published 26 March 2015) sets quality-assurance guidance for government analysis and models. A new edition was published on GOV.UK on 30 July 2025. [confidence: high] [source: 11]

## Timeline

- 1999: FAST methodology originates (F1F9 founded).
- July 2003: BPM/SSRB Best Practice Spreadsheet Modeling Standards first published.
- 2008: Corality founded in Sydney (SMART).
- 2010: Grossman and Özlük compare FAST, Operis and BPM at EuSpRIG.
- 28 April 2011: FAST Standard Organisation Ltd incorporated.
- 29 May 2014: FAST02a.
- 26 March 2015: AQuA Book first published.
- July/August 2016: Mazars acquires Corality.
- 13 November 2018: ICAEW Financial Modelling Code published.
- July 2019: FAST 02c (CC BY 4.0).
- February 2022: FAST 02d (per publisher listing).
- 2024: ICAEW Code reissued (© 2024).
- 30 July 2025: AQuA Book new edition on GOV.UK.

## Financing and structure details

Not a financing topic. In practice, lenders and sponsors may name a modelling standard in the model protocol or the model auditor's engagement letter. The model audit (Chapter 44) then tests compliance and logic against it. Whether a standard is required is a deal-specific choice; no verified market statistic exists.

## What went wrong or right, and why

- The ICAEW says most earlier methodologies were developed for particular sectors and are "detail-oriented and not accepted very widely". That gap is why it wrote a high-level, consensus code [7].
- Grossman and Özlük credit standardised methodologies with better productivity, accuracy and maintainability for large planning models [4].
- See spreadsheet-errors.md for the error-rate evidence (EuSpRIG/Panko) that motivates standards and independent review.

## Teaching angles by chapter

- **Chapter 39 (Model architecture, standards, and timing)**: Teach FAST's four sheet types (Foundation, Workings, Presentation, Control), consistent columns and time ruler, left-to-right and top-to-bottom flow, flags and PPFs for timing, and corkscrews for balances. Cite rule numbers rather than paraphrasing loosely. Contrast FAST's prescriptive rule book (about 109 rules in 02a) with the ICAEW Code's principles-based approach, and explain why a project finance team adopts one house standard.
- **Chapter 44 (Auditing a model)**: Use the ICAEW Code's error-reduction section (checks, master check, review and test) and FAST's "do not hide anything", "calculate only once" and "no purposeful circularity" as the auditor's checklist anchors. Show how the circularity guidance (copy-paste macro or algebraic solution, flagged as not live) becomes an audit finding when breached. Cross-reference spreadsheet-errors.md for why single reviewers miss errors.

## Do not state

- That FAST is mandatory or a regulatory standard. It is voluntary.
- The exact current FAST version or its changes since 02a. 02c (July 2019) is confirmed; 02d (February 2022) only from the publisher listing; the change log was not verified.
- The rule count for 02c or 02d. Only the 02a tally (109) was made.
- The founding of the FSO "by F1F9" or a list of founding member firms. Not verified.
- The current SSRB/BPM version number. Claims of "version 7.2" were not verified.
- The full list of SMART's 15 philosophies, or any claim that SMART stands for an acronym. Not verified.
- Market-share figures for any standard. Not verified.

## Sources

1. FAST Standard Organisation, "The FAST Standard: Practical, structured design rules for financial modelling", Version FAST02a, 29 May 2014 (copy hosted at themodelanswer.com; original at fast-standard.org). http://www.themodelanswer.com/wp/downloads/FASTStandard_02a.pdf
2. Companies House, "FAST STANDARD ORGANISATION LTD", company number 07617819, accessed 3 October 2026. https://find-and-update.company-information.service.gov.uk/company/07617819
3. FAST Standard Organisation, "The FAST Standard – Creative Commons licence" and "About the FSO" pages (seen via search summaries only). https://fast-standard.org/fast-standard-creative-commons-licence/ ; https://fast-standard.org/about-fso/
4. Grossman, T. A. and Özlük, Ö., "Spreadsheets Grow Up: Three Spreadsheet Engineering Methodologies for Large Financial Planning Models", EuSpRIG 2010 Proceedings, arXiv:1008.4174. https://arxiv.org/abs/1008.4174
5. Whitelaw-Jones, K., "An introduction to financial modelling standards", Full Stack Modeller, 10 February 2022. https://www.fullstackmodeller.com/blog/an-introduction-to-financial-modelling-standards
6. FAST Standard (Issuu publisher page), "FAST Standard 02d February 2022". https://issuu.com/faststandard/docs/fast_standard_02c_july_2019
7. ICAEW, "Financial Modelling Code: A set of principles for robust financial modelling", ICAEW Thought Leadership, © ICAEW 2024. https://www.icaew.com/-/media/corporate/files/technical/technology/excel/financial-modelling-code.ashx
8. Accountancy Age, "ICAEW Financial Modelling Code report", 15 November 2018. https://accountancyage.com/2018/11/15/icaew-financial-modelling-code-report/
9. Forvis Mazars Financial Modelling, "Our history". https://financialmodelling.forvismazars.com/forvis-mazars/our-history/
10. Accountancy Age, "Mazars buys Corality Financial Group", 13 July 2016. https://accountancyage.com/2016/07/13/mazars-buys-corality-financial-group/
11. GOV.UK, "The AQuA Book" (guidance, published 30 July 2025; original publication 26 March 2015). https://www.gov.uk/guidance/the-aqua-book
