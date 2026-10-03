# Chapter 36, Round 2, Domain review

Read in full: the revised `chapters/36-sizing-and-sculpting-debt.tex` (1,187 lines), `reviews/36/r1-revision.md` and decision D-128.

## Verdict: FAIL

Four defects remain, all one- or two-line edits. They include one error in the tail paragraph, which I wrote; I flag it myself. Every substantive round-1 defect is fixed. Once the four edits below are made, I pass the chapter without another full round: the editor-in-chief can check them against this report.

## Round-1 defects: verification

| R1 | Status | Note |
|---|---|---|
| 1 (ECA WAL, blocking) | Fixed | D-128 is applied cleanly. Exh 36.13 tests the covered tranche's own 26 equal installments (WAL 6.92 against 7.25). It shows the other tranches (8.17 years) and all tranches (7.79 years) as memo lines. The rule appears in ssec:36.9.1, stack step 6, the checklist and the red flags. The wrong explanation of the profile's shape is gone. The scene now stages the real negotiation: the other lenders take the back end at unchanged margins. Exr 36.13(d) teaches the principle. |
| 2 (resculpting) | Fixed | Debt and maturity are held, the level DSCR is an output, the 1.30x completion floor applies, and LDs restore it. The 1.28x figure matches P-F19. |
| 3 (tail) | Fixed, with one wording error | See Defect 1 below and the sign-off section. Case P's tail is now described as a by-product of the ECA cap, and the walkthrough and drill tails are reframed. |
| 4 (Brazil rate) | Fixed | IPCA-linked loan at 13.0% nominal. I re-checked 516.1, 580.8, 582.9 and the 6% contrast of 866 against 830.2; all agree with my script. |
| 5 (CfD) | Fixed | 15-year contract described generically; the AR7 20-year term is stated with a DESNZ source. |
| 6 (ramp-up reserve) | Fixed | The reserve is placed in the funding requirement and funded pro rata or by equity. The 164.1 debt-funded amount is shown, and equity funding is presented as a negotiated point. The no-capitalization rule for ECA-covered debt is added. |
| 7 (tax circularity) | Fixed | |
| 8 (Exh 36.14) | Fixed | A full four-test grid. The 1.30x rows now bind on the downside, and the narration draws the right lesson: the tenth of a turn would have bought almost nothing. |
| 9 (soft mini-perm) | Fixed | |
| 10 (merchant share) | Fixed | The measure is declared undefined in the source, PV of debt service is the book's proxy, and the CFADS share (49.0%) is given. The cross-market sentence is fixed. |
| 11 (driver ranking) | Fixed, see Defect 4 | |
| 12 (CCSU 22 years) | Fixed | |
| 13 (tenor increments) | Fixed | |
| 14 (ECA equal-principal installments) | Fixed | |
| 15 (six-month rule tense) | Fixed | |
| 16 (walkthrough question) | Fixed | |
| 17 (drill payment risk) | Fixed | The counter is now 1.30x plus 12 months of payment security, and the P99 floor is described as nearly free. I sign off on the drill answer. |
| 18 (Exr 36.19 package) | Fixed | The P99 test now counts the DSRA (factor 0.934), the 70% gearing cap binds at 160.0, and the stand-alone floor is named as the wrong design. |
| 19 (four lenses) | Fixed | An authority-lens paragraph is added in ssec:36.3.2 and a contractor-lens paragraph in ssec:36.2.4. *Facts reviewer:* verify the NAO 2018 statement that PF2 "launched at 75:25 … in practice reverted to 90:10" against the report. |
| 20 (dual profile) | Fixed | |
| Minors | Fixed | |

## Sign-off: tail-length judgment, ssec:36.5.2

**Signed off, once Defect 1 is corrected.** The paragraph is my round-1 text with a complete D-011 label (markets, lenders and 2023–2026 period, marked "not survey data").

## Remaining defects

**1. ssec:36.5.2, tail judgment: "the contract carries no volume risk (availability PPPs, Comber's feed-in tariff, the Gulf contracts above)."** This wording came from my round-1 text and it is wrong. Sakaka is a solar PPA and Comber a wind feed-in tariff. Both pay per megawatt-hour, so the project carries resource (output) volume risk. What these contracts lack is demand or market risk.
Required fix: replace "the contract carries no volume risk" with "the contract carries no demand or price risk". In the next sentence, replace "a contract with volume or renewal risk" with "a contract with demand, price or renewal risk". Make the same change to the red flag "real renewal or volume risk" in sec:36.13.

**2. sec:36.12, narration after the scene: "a six-month delay squeezes the same principal into fewer periods unless the lenders resculpt, and every period's DSCR then falls below 1.35x."** Resculpting with the maturity fixed does not avoid the fall. It only spreads the fall evenly, and Case P's own COD resculpting came out at 1.28x (ssec:36.2.4).
Required fix: "… squeezes the same principal into fewer periods, so even after the lenders resculpt to a level profile every period's DSCR is below 1.35x (\cref{ssec:36.2.4})."

**3. sec:36.15: "Suppose the offtaker pays two monthly invoices four months late: in that half-year CFADS falls far more than 26%."** Two invoices out of six is about a third of the half-year's revenue, and somewhat more of CFADS. That is above 26%, not "far more", and a numerate reader will check the claim.
Required fix: "… in that half-year CFADS falls by a third or more, well past the 26% the cushion absorbs, …".

**4. ssec:36.10.1, the country-and-counterparty paragraph.** This driver is ranked third for the DSCR, but the paragraph speaks only to tenor and gearing and never states the DSCR direction.
Required fix: add one clause, for example "weaker sovereign or offtaker credit pushes the target up, as the judgment drill's 'what would change' shows (\cref{sec:36.14})". Keep it as a direction only, with no figure, because no verified norm exists.

## Fresh read: other domain checks (no action)

These are accurate and correctly framed:
- **Case P v1.5 structure.** The ECA tranche repays in equal installments while the other tranches are sculpted so that total debt service is CFADS/1.35. This is standard practice, and Exr 36.13(d) teaches the principle.
- **Case P average DSCR.** The weighted average DSCR on scheduled debt service (1.55x) against the sweep-inclusive figure (1.39x) is a correct distinction.
- **Case P LLCR.** The explanation of why LLCR excluding the DSRA (1.36x) exceeds 1.35x (a different discount-rate basis) is sound.
- **Contractor lens.** Performance and delay LDs are correctly tied to sizing.
- **Option (c) reserve.** Sizing the reserve at a deposit rate rather than the loan rate is better practice than round 1.
- **Exr 36.19.** The liquidity-test arithmetic, 0.5 × max(P50/P99), is correct for a six-month DSRA.
