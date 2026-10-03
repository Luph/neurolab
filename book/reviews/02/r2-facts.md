# Chapter 2 review, round 2: facts

Reviewer role: fact-checker (standards 12.6). Chapter: `chapters/02-what-project-finance-is.tex` (revised; log `reviews/02/r1-revision.md`). Date: 2026-10-03.

Checked against `facts/` (sunedison-terraform, sabine-pass, hyperion-meta, northvolt, t-ratings-2, eurotunnel, t-rbl, png-lng, tideway) and these fresh primary sources:
- SunEdison Q3 2015 10-Q, Note 8.
- TerraForm Power FY2015 10-K.
- UK Supreme Court case page for *Prest v Petrodel* (supremecourt.uk/cases/uksc-2013-0004).
- Légifrance, Code de commerce art. L621-2 (LEGIARTI000045178127, version in force from May 15, 2022).
- Meta's press release of October 21, 2025.

EDGAR blocks a plain curl user agent; the filings were read through WebFetch and the block was not bypassed.

## Round-1 defects: status

| R1 | Status |
|---|---|
| 1 Debt attribution | Closed. "About USD 3.8 billion" at TerraForm and its projects is correct (TERP USD 2,548 million + GLBL USD 1,240 million). "Much of the rest" non-recourse is also correct: about USD 4.8 billion of the USD 7.9 billion SunEdison segment, net of the convertible notes, exchangeable notes, margin loan and recourse carve-outs. |
| 2 "many of them built or bought" | Closed. |
| 3 Referent of "it" | Closed. |
| 4 Global sale source | Closed. |
| 5 USD 950 million notes | Closed. |
| 6 Settlement counterparty and committee motion | Closed. The November 7, 2016 motion is confirmed in the FY2015 10-K. |
| 7 Substantive consolidation | Closed in substance. Two new statements were added; see defects 1 and 2 below. |
| 8 Sabine Pass "half" | Closed. |
| 9 Bechtel/Cheniere source | Closed. |
| 10 Hyperion debt raiser | Partly closed. The raiser is now Blue Owl's side. However, the cited source does not support "largely", "senior secured" or "2049"; see defect 5. |
| 11 Exercise 2.12 cells | Closed, except the Hyperion cell, which depends on defect 5. |
| 12 Hyperion cost dated | Closed. |
| 13 Exhibit 2.2 note | Closed. |
| 14 Jensen and Meckling | Closed. Both citations are correct. |
| 15 D-011 | Closed. The new ranges are labeled "indicative" with market and period: Latin American renewables 2020–2025, and solar O&M caps 2015–2025. They still need the domain reviewer's sign-off under D-011. |
| 16 Geotechnical baseline report | Closed. |

## Verdict: FAIL

Seven defects remain. Three are serious:
- The French doctrine has no source.
- One Hyperion sentence is not supported by the source it cites.
- The definition of "senior" notes is wrong.

## Defects

1. **ssec:2.1.2, French doctrine ("French law reaches results close to substantive consolidation by extending a parent's insolvency proceedings to a subsidiary whose assets were commingled with the parent's").** The statement is correct in substance and is verified on Légifrance. Code de commerce art. L621-2, second paragraph, reads: "La procédure ouverte peut être étendue à une ou plusieurs autres personnes en cas de confusion de leur patrimoine avec celui du débiteur ou de fictivité de la personne morale." This article governs safeguard, and the rule is applied to reorganization and liquidation by reference. The problem is that the chapter gives no citation and no Sources entry. The wording is also narrower than the law, which reaches any person, not only a subsidiary, and covers a fictitious company as well as commingled assets.
   **Fix:** reword to: "French law can extend a debtor's insolvency proceedings to another company, such as a subsidiary, whose assets are commingled with the debtor's or which is a mere sham (Code de commerce, art. L621-2)." Add to Sources: "France. *Code de commerce*, article L621-2 (version in force from May 15, 2022). Légifrance. https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045178127. Accessed October 3, 2026."

2. **ssec:2.1.2, *Prest* (statement and Sources entry).** The case, its date (June 12, 2013) and its holding are verified. Lord Sumption's evasion principle applies where an existing legal obligation, liability or restriction is deliberately evaded, or its enforcement frustrated, by interposing a company. Two fixes are needed:
   - The chapter's "an obligation its controller already owes" omits "restriction" and the frustration limb. Change it to "to evade, or frustrate the enforcement of, an existing obligation or restriction of its controller".
   - The Sources entry lacks a URL and access date, unlike every other entry. Add "https://www.supremecourt.uk/cases/uksc-2013-0004. Accessed October 3, 2026." Also cite the case in the text in the house style, as "(Prest v Petrodel Resources Ltd 2013)" matching the Sources key. It currently appears only as an italic case name with the year.

3. **ssec:2.1.3 ("'Senior' means the notes ranked ahead of the company's other unsecured debts; ... guaranteed by Terra LLC and certain of its subsidiaries").** The first part is wrong. Senior unsecured notes rank equally with the issuer's other senior unsecured debt and ahead only of subordinated debt. They were also effectively junior to Terra Operating's secured revolver. The guarantor description is also imprecise. The FY2015 10-K says the notes are "guaranteed by Terra LLC and each of Terra Operating LLC's existing and future subsidiaries that guarantee its senior secured credit facility". "Its" in the chapter reads as Terra LLC's subsidiaries.
   **Fix:** "'Senior' means the notes ranked equally with Terra Operating's other unsecured debt and ahead of any subordinated debt; they were not secured on particular projects but were guaranteed by Terra LLC and by the Terra Operating subsidiaries that guaranteed its secured credit facility."

4. **ssec:2.1.3 ("and the board changes of November 2015 were its first use of them").** This is not supported by any source. Neither the fact sheet nor the 10-K says November 20, 2015 was SunEdison's first use of its votes; SunEdison had appointed TerraForm Power's board since the IPO. The sentence also attaches a January 2016 percentage to a November 2015 event.
   **Fix:** "By January 2016 SunEdison held 84.1% of TerraForm Power's votes against 34.5% of its economic interest; the board changes of November 2015 showed what that control could do."

5. **ssec:2.4.5 ("Blue Owl's side of the venture raised its funding largely through a private offering of senior secured notes anchored by PIMCO, maturing in 2049 (Meta Platforms 2025)").** The cited press release says only: "A portion of capital raised by Blue Owl will be funded by debt issued to PIMCO and select other bond investors through a private securities offering." It does not say "largely", "senior secured" or "2049". "Largely" implies the bond-to-equity proportions, which the fact sheet's Do-not-state list bars. "Senior secured" and "2049" come only from a mutual-fund holdings filing (fact sheet item 10, medium confidence).
   **Fix:** "Part of the Blue Owl side's capital came from debt sold privately to PIMCO and other bond investors (Meta Platforms 2025); fund holdings filings describe the notes as senior secured and maturing in 2049 (PIMCO Variable Insurance Trust 2025)." Add to Sources: PIMCO Variable Insurance Trust, Form N-PORT-P, filed November 26, 2025, https://www.sec.gov/Archives/edgar/data/1047304/000109926325004523/primary_doc.xml. Alternatively, drop "senior secured" and "2049", and make the Solution 2.12 Hyperion "Secured on" cell "Cannot be determined from the chapter".

6. **ssec:2.5.3, PNG LNG ("each committed to its share of one project company's equity").** This misdescribes the structure. Per `facts/png-lng.md` (items 3 and 12, and the financing details), PNG LNG was an unincorporated joint venture, financed through a jointly owned borrowing and marketing company, PNG LNG Global Company LDC. The co-venturers also gave completion guarantees, released at financial completion on February 6, 2015. So the partners' commitments were not limited to equity in one company. The ownership percentages are correct.
   **Fix:** "each held its share of an unincorporated joint venture that borrowed through a jointly owned company, PNG LNG Global Company, and the co-venturers guaranteed the debt until financial completion in 2015 (PNG LNG Global Company and ExxonMobil 2010)." Alternatively, cut the completion-guarantee clause and keep "unincorporated joint venture with a jointly owned borrowing company".

7. **ssec:2.4.5 ("the whole-business securitization used for some UK and European airports and water companies").** No fact sheet or source supports this. "European" in particular is unverified. `facts/tideway.md` supports only a "whole-business-style" structure for a UK water carve-out.
   **Fix:** narrow it to "used for some UK water companies and airports". Either cite a primary source (a Heathrow Funding or Anglian Water Services prospectus, for example) or attribute it to the Tideway sheet's description and say "whole-business-style".

## Re-check of every other real-world statement (no defects)

- **SunEdison and TerraForm:** the opening (Chapter 11 gloss; USD 16.1 billion and USD 11.7 billion; USD 300 million DIP); TERP's July 2014 IPO; the November 20, 2015 removals; the IDR and Class B pledges; the going-concern note and its two cited risks; the December 5, 2016 filing; the NASDAQ and indenture risk; Brookfield in March 2017; the Global sale in December 2017.
- **Sabine Pass:** "the first plant to export LNG from the lower 48 states"; USD 125 million each; the four SPAs; 115% of Henry Hub (worded as "meant to cover", consistent with the Do-not-state item); USD 2.25–3.00/MMBtu; about USD 2.3 billion after BG's added volumes; USD 3.6 billion from 21 banks; the chairman's quote; USD 932 million, attributed to Cheniere consolidated.
- **Hyperion:** 80/20; USD 27 billion dated as the then-estimate; USD 12.31 billion; the 16-year RVG starting at USD 28 billion; not the primary beneficiary; USD 46.03 billion and USD 2.9 billion.
- **Northvolt:** all figures and dates match the sheet; the expansion is described as never drawn.
- **Moody's 1983–2021:** 10,452 projects; 67% coverage; 4.8% (Basel) equal to Baa3; the Basel 90-day or unlikely-to-pay definition; 79.5%; 62%; the curve shape (high speculative grade in years 1–3, single-A by about year 7, per sheet item 23); 72.5% against 80.8%.
- **Ratings:** BBB- and Baa3 as the lowest investment grade.
- **Eurotunnel:** the treaty date and terms; about 50 banks; GBP 5 billion; about GBP 8 billion at opening; the September 1995 suspension.
- **PNG LNG percentages:** match `facts/png-lng.md` item 2.
- **RBL:** semiannual redetermination, and the US against international valuation basis, consistent with `t-rbl`.
- **Fictional names:** Mvuli Paa, GLA and Alto Huelén were checked in round 1.
