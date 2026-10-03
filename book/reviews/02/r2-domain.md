# Chapter 2 review, round 2: domain expert

**Verdict: FAIL**

I checked the round-2 file `chapters/02-what-project-finance-is.tex` against `reviews/02/r1-domain.md` and the writer's log `reviews/02/r1-revision.md`, then read the whole chapter again.

The round-1 work is thorough. 28 of 29 round-1 defects are fixed and one is partly fixed.

The re-engineered board paper fixes the arithmetic of the old covenant breach. It now has two new defects of judgment that a credit committee or a CFO would not let through:

- It recommends a structure that leaves GLA almost no covenant cushion.
- It misdescribes what a standby facility is from the lenders' side.

Both defects are in the walkthrough, which the brief says is the chapter's centrepiece. That is why the verdict is FAIL. They can be fixed in about three paragraphs.

## Round-1 defects

| R1 | Status | Note |
|---|---|---|
| 1 Covenant breach in the overrun case | PARTLY | The breach is now shown (3.63x; 3.65x at the full cap; headroom covers 52% of the cap) and carried through. The replacement structure introduces new defects N1 and N2. |
| 2 Step 7 condition reversed | FIXED | |
| 3 Alto Huelén had no revenue contract | FIXED | Gains a 15-year US-dollar PPA with a miner rated BBB- for 80% of output. See N3 for one precision point. |
| 4 Non-recourse rung ignored contingency and standby | FIXED | |
| 5 "Modest risk" and the foundation scope | FIXED | Now framed as the interface between the turbine supply agreement and the balance-of-plant contract. |
| 6 Equity LC listed as sponsor support | FIXED | |
| 7 "Every dollar of surplus" | FIXED | |
| 8 Substantive consolidation | FIXED | US doctrine, *Prest*, and the French extension of proceedings are all stated correctly. |
| 9 RBL valuation basis and cure period | FIXED | |
| 10 Sabine Pass "most" capacity; the 115% multiplier | FIXED | |
| 11 Geotechnical baseline | FIXED | |
| 12 Moody's default-curve shape | FIXED | |
| 13 Bélanou "a fraction of a percent" | FIXED | |
| 14 Cost claim generalized | FIXED | |
| 15 Example 2.4 simplifications undeclared | FIXED | Every item is named and the direction of each is right. |
| 16 Leverage and credit substitution missing | FIXED | |
| 17 Fit test lacked credit and currency | FIXED | Bélanou is now conditional under question 2. See N4 for a wording point. |
| 18 Frequency ranking | FIXED | |
| 19 Syndicate consent for the covenant relaxation | FIXED | |
| 20 Arbitrary one-year-of-EBITDA threshold | FIXED | |
| 21 SunEdison project-level default risk | FIXED | |
| 22 Holding-company layer | FIXED | |
| 23 Sizing and repayment as a distinguishing question; whole-business securitization | FIXED | The missing registry home for whole-business securitization is correctly passed to the coordinator. |
| 24 Soiling: loss measure, parent guarantee, cap range | FIXED | |
| 25 Insured loss used as the non-recourse example | FIXED | |
| 26 Battery: PPA amendment and ELNACOR's consent | FIXED | |
| 27 Separateness undertaking definition | FIXED | |
| 28 Eurotunnel recourse column | FIXED | |
| 29 Terra Operating classification | FIXED | |

## New defects

### N1. The recommended cap leaves GLA no real cushion, and the drill criticizes the corporate route for the same thing

Where: sec:2.8 Step 2; Exhibit 2.3; Solution 2.7 ("to leave a margin"); sec:2.11 reasoning.

**The defect.** The paper recommends a USD 29.2 million cap because a full call would take leverage to 3.49x, "with USD 1.2 million to spare". That cushion is not a margin at all.

- At net debt of 637.2, leverage reaches 3.50x once EBITDA falls to 182.1, which is a fall of 0.2%.
- Even the equity-only position (net debt of 608.0) breaches if EBITDA falls 4.8%, to 173.7.

A Chilean generator's EBITDA moves by more than that with hydrology and spot prices in an ordinary year. The analysis also holds GLA's net debt and EBITDA fixed for the whole construction period. In reality GLA's own free cash flow after dividends, its other capital spending, and the timing of covenant tests (quarterly, on trailing twelve-month EBITDA) all move headroom by more than USD 1.2 million.

The drill then says the corporate route would leave GLA "with nothing left for the next project". The recommended project finance route also leaves nothing during construction, and the chapter does not acknowledge this.

**Required fix**, in Step 2 and mirrored in Exhibit 2.3 and the drill:

1. Have the paper state the EBITDA fall that would cause a breach under the project finance route: 4.8% before any call, 0.2% after a full call of the 29.2 cap.
2. Have the paper set a cushion policy and size the cap to it. For example, keep leverage at or below about 3.25x after a full call, or keep a stated share of EBITDA in reserve. Recompute the cap and the standby facility (Python; numbers auditor to verify).
3. Alternatively, keep the cap and show how the cushion is built in practice, and say what the board must approve for that:
   - a construction-period covenant forecast using GLA's projected EBITDA and free cash flow;
   - a dividend restraint or a pre-agreed source of funds if a call comes.
4. Delete "to leave a margin" from Solution 2.7, or replace it with the cushion actually chosen.
5. In the drill, have the reasoning concede that the project finance route also uses up GLA's construction-period headroom. Then say why it still wins:
   - the use of headroom is temporary and capped;
   - after completion the 29.2 cap falls away, so GLA's capacity for the next project comes back;
   - under the corporate route the 389.6 stays on GLA's balance sheet.

### N2. The standby facility is presented as the lenders' protection, but it is the lenders' own extra exposure

Where: sec:2.8 Steps 2 and 4; Exhibit 2.3 and its note.

**The defect.** Step 2 says the lenders "receive their remaining overrun protection from a USD 29.2 million standby facility inside the project financing". From the lenders' side, that facility is not protection. It is additional senior debt the lenders themselves commit, drawn exactly when the project is in trouble.

Replacing USD 29.2 million of sponsor support with lender debt is a concession the lenders must agree to. They will attach conditions:

- **Sizing.** The base loan plus the fully drawn standby must still meet the minimum DSCR and gearing tests. That can mean a smaller base loan of 292.2 or more equity.
- **Drawing order.** The standby is typically drawn only after the budget contingency, and pro rata with sponsor money. The canon definition of standby facility (sec:31.7) says "usually drawn with contingent equity in a fixed ratio". In the board paper GLA pays first and the standby pays the rest; that sequence must be stated as a negotiated term.
- **Price.** The standby carries an upfront fee and a commitment fee, often a higher margin, and possibly a tighter completion test or extra independent-engineer contingency.

Exhibit 2.3 also lists transaction costs of 13.83 "before the standby commitment fee". That figure also leaves out the standby's upfront fee: about USD 0.66 million at the example's 2.25%.

**Required fix:**

1. Rewrite the sentence in Step 2: "and asks the lenders to provide the remaining USD 29.2 million of overrun funding themselves, through a standby facility inside the project financing, sized with the independent engineer so that the base loan and the fully drawn standby together still pass the lenders' cover-ratio tests (\cref{sec:31.7})."
2. Add one sentence giving the expected price of that concession (standby upfront and commitment fees, and possibly a higher margin), and the fallback if the lenders refuse (an equity-funded overrun reserve or an LC, with its covenant cost).
3. Change the Exhibit 2.3 cell to "13.83, before the standby facility's fees".
4. In Step 4, note that if the standby is drawn, project debt rises to about 317.5. That lowers project cover ratios and the sponsors' distributions, and the paper should say so.

### N3. The Alto Huelén PPA needs one clause on how it is settled

Where: Example 2.1, Step 4.

**The defect.** In Chile a generator in Biobío selling to a copper miner in the north does not deliver power to the mine. The contract settles through the national system's marginal-cost market. The generator injects at its own node and is paid the contract price for the contracted volume or profile. It is exposed to the price gap between its node and the withdrawal node, and to curtailment. These were the defining Chilean renewables risks of 2022 to 2024.

"Sells 80% of its expected output for 15 years" also leaves unclear whether the contract is pay-as-produced or a fixed block. If it is a block, the generator must buy any shortfall at spot. Question 2 of the fit test turns on exactly this.

**Required fix:** add one illustrative clause to Example 2.1, for example: "pay-as-produced, settled at the wind farm's injection node, so the miner and not GLA bears the price difference between nodes". Alternatively, if the writer prefers GLA to keep that risk, say it does and that the lenders size against it. Then refer back to it in Step 4.

### N4. Fit-test question 2 applies the currency condition only to contracted revenue

Where: `fw:pf-fit-test`, question 2.

**The defect.** As worded, "in a currency the debt can be serviced in" attaches only to the contracted branch. The "or else predictable enough" (merchant) branch escapes the currency test. Merchant revenue in local currency against dollar debt fails the same test.

**Required fix:** "Is the revenue, whether contracted with a counterparty creditworthy enough to pay for longer than the debt will be outstanding or predictable enough for lenders to forecast it for that long, earned in a currency the debt can be serviced in?" Keep the coordinator's flag on the framework wording change.

## Sign-offs

- **Indicative range:** the soiling cap range (half to all of one year's fee; utility-scale solar O&M, Latin America and Europe, 2015–2025) is approved under D-011.
- **Framework 2.2 (Llano Pardo, Nairobi, Northvolt, Bélanou):** the four applications are correct under the revised wording.
- **Leverage and credit-substitution paragraphs; Example 2.4 simplification paragraph:** both are accurate.
