# Case Bible Annex TR: Case T and Case R resolutions, name register additions

Version 1.0, October 3, 2026. Owner: Case Bible editor, under the editor-in-chief. Binding on every writer, reviewer and modeler.

**Precedence.** Where this annex and `case-bible.md` differ, this annex governs. Where this annex is silent, `case-bible.md` governs. Model outputs still come only from the figure ledgers (`model/figure-ledger-case-r.md`; the Case T ledger when released). Every new number in this annex that a model must absorb is listed, with units and target figure IDs, in `bible/case-tr-input-requests.md`. Numbers marked **(book input)** are fixed facts of the story that no model needs; writers may print them as Case Bible inputs. Simple arithmetic shown in this annex is permitted under D-013 and was computed in Python on October 3, 2026.

**Scope.** This annex resolves every Case T and Case R flaw raised in the brief writers' "Case Bible flaws" sections (u01 to u17) and `brief-feedback.md`, adds the name-register entries for the Chapter 1 illustrative deal and the capstone, and records the result of coordination with the two modelers: the Case R model is complete (R-1.1); the Case T model is at version 1.0 with its ledger (`model/figure-ledger-case-t.md`, T-F01 to T-F17) and report (Sections 12 and 13 record the plan classes, equity allocation and assumption changes); this annex adopts the Case T modeler's calibrations (`inputs_case_t.json`, `modeler_assumptions`; Case Bible Part 8 rows T-C05 to T-C11) rather than overriding them. Case P flaws are out of scope and remain with the contract-terms annex.

Concordance of flaws to sections is in Section 0.

---

## 0. Flaw concordance

| Flaw (unit, ID) | Subject | Resolved in |
|---|---|---|
| u12 #1; u12 brief 58.3.5 | Case T KPI and deduction regime | T.1 |
| u12 #2; u10 BF-u10-3; u12 T-F02 request | Procurement: evaluation, bid security, committed finance, Northgate, gaps, third consortium | T.2 |
| u10 BF-u10-3 | Pellow value-of-time cases | T.3 |
| u06 BF-1 | D&C interface agreement, tolling subcontractor, D&C caps, JV character | T.4, T.5 |
| u03 #7 | Merrick Ridge Tunnel ground and method | T.6 |
| u03 #8 | SR 14 pre-opening counts | T.7 |
| u12 #3 | Handback requirements | T.8 |
| u12 #5; u12 T-F01 request | Value for money implausibly large | T.9 |
| u13 CBF-5 | Restructuring plan classes, votes, dissent, relevant alternative | T.10 |
| u13 CBF-6 | Equity allocation rationale (state price per share) | T.11 |
| u12 #4 | Owen Reddaway's 2012 title | T.12 |
| u16 CB-u16-3 | 2024 light-rail line; 2024 Partnerships Brannock director | T.13 |
| u16 CB-u16-4 | 2016 hospital PPP | T.14 |
| u14 BF-8 | Ardmore insurers' capital regime | T.15 |
| u16 CB-u16-8 | Callum's "last scene" note | T.16 |
| u03 #5 | Sasha in the Chapter 12 scene | T.16 |
| u16 CB-u16-7; u09 T-F18 request | Traffic ratios; shortfall decomposition by cause | T.17 |
| u10 BF-u10-1 | A1 sale process terms and competing bids | R.1 |
| u16 CB-u16-5 | Ostrander credit profile and vPPA collateral | R.2 |
| u16 CB-u16-6 | 2024 hydrogen developer and PPA terms | R.3 |
| u15 #3 | R7 revenue floor mechanics and payments | R.4 |
| u09 F-22, R-F11 request | Battery fade and augmentation, R6 and R7 | R.5 |
| u14 BF-9 | Green USPP framework, reviewer, reporting, pricing | R.6 |
| u10 BF-u10-8 | Terminal value rule | R.7 |
| u17 BF-u17-05 | 2026 data-center PPA offer to Lattimer | R.8 |
| u15 #7 | Lattimer 2025 IC month (Chapter 71) | R.9 |
| u13 CBF-9 | Chapter 65 against Chapter 88 timing in 2026 | R.9 |
| u14 BF-12 | Gwen Treharne in Chapter 84 | R.9 |
| u02 BF-u02-3, BF-u02-4 | Case R P99s and correlations | Closed by R-C09 and R-C10 (Case Bible Part 8); no further action |
| u01 BF-u01-6 | Chapter 1 illustrative deal names; Sterrenberg and ABDB as 2016 lenders | N.1, N.4 |
| u17 BF-u17-06 | Capstone names (Salinera, SLP and others) | N.2 |

Figure ID note: two briefs proposed different contents for "T-F11" (u09: shortfall by cause; u16: actual-to-forecast ratios) and two proposed different contents for "R-F11" (u09: battery capacity; u15: R7 floor). Meanwhile the Case T modeler assigned T-F11 to T-F17 (sizing, ratio summary, sensitivities, balances, outturn, tax, USD equivalents) and the Case R modeler R-F11 to R-F17. This annex therefore assigns the briefs' requests to new IDs: T-F18 (traffic ratios), T-F19 (shortfall by cause), T-F20 (performance payments), T-F21 (optional VoT variants), R-F18 (R7 floor) and R-F19 (battery capacity). Full list in Section F.

---

# Part T. Case T: the Merrick Link

## T.1 Performance regime for a user-pay road (Concession Deed, Schedule 7)

The concessionaire takes full demand risk, so the state pays no unitary charge from which to deduct. The Concession Deed therefore uses a **performance payment** that the concessionaire pays to BRTA, plus a **performance points** regime that escalates to monitoring and, ultimately, termination. Deductions are a cost to the concessionaire, not a reduction of tolls. All money amounts are in 2015 prices, indexed by Ardmore CPI (book inputs except where Section F says otherwise).

### Lane availability

| Item | Term |
|---|---|
| Measurement unit | Lane-km-hour of a running lane that is closed or restricted below posted speed by a cause within the concessionaire's control |
| Unavailability charge, peak (weekdays 06:00 to 09:30 and 15:30 to 19:00) | ARD 1,850 per lane-km-hour |
| Unavailability charge, other daytime and weekends | ARD 620 per lane-km-hour |
| Night window (22:00 to 05:00), planned closures notified at least 7 days ahead | Nil |
| Night window, unplanned or late-notified closures | ARD 280 per lane-km-hour |
| Merrick Ridge Tunnel bore closure (either bore, concessionaire cause) | ARD 9,500 per bore-hour, in place of the lane charge |
| Exempt | Closures ordered by police or BRTA for incidents not caused by the concessionaire; works under an approved traffic management plan for BRTA-instructed changes (including the 2024 to 2025 Holloway Junction upgrade within approved windows) |

### Service KPIs and performance points

| KPI | Standard | Points per failure |
|---|---|---|
| Incident attendance | Patrol on scene within 20 minutes, 95% of incidents each month | 5 per month missed, plus 1 per incident over 40 minutes |
| Debris and hazard removal | Within 60 minutes of notification | 2 |
| Tunnel safety systems (ventilation, fire detection and suppression, emergency communications, lighting) | 99.8% monthly availability | 10 per month below standard; 20 if a safety system is unavailable while the bore is open |
| Category 1 pavement and structural defects | Made safe within 24 hours; repaired within 28 days | 5 |
| Tolling accuracy | Customer billing error rate below 0.10% of transactions each month | 5 per month above |
| Reporting | Monthly performance report by the 10th business day | 1 per day late |

| Points threshold | Consequence |
|---|---|
| 300 points in any rolling 6 months | Warning notice; increased monitoring at the concessionaire's cost |
| 500 points in any rolling 12 months | BRTA may require a remedial plan, approved by the independent certifier |
| 800 points in any rolling 12 months | Concessionaire event of default (subject to the Financiers' Direct Deed cure and step-in regime, Case Bible 2.7) |

Each performance point also carries a performance payment of ARD 2,400. Performance payments (lane unavailability charges plus point payments) are paid to BRTA quarterly in arrears and are capped at 2.5% of the previous calendar year's net toll revenue. They are deductible for tax.

### Relief and the actual record

The COVID-19 Relief Event (Case Bible 2.7, 2.8) suspended all performance payments and points from March 23, 2020 to September 30, 2021. BRTA's refusal of compensation does not affect the suspension.

Actual performance payments (ARD million, nominal; to be absorbed by the actual-history run, figure T-F20):

| Half-year | Amount | Main cause |
|---|---|---|
| 2019 H1 (from May 6) | 0.14 | Tunnel ventilation commissioning faults after opening |
| 2019 H2 | 0.24 | Same, to September 2019; tolling billing errors above standard in July and August |
| 2020 H1 | 0.03 | January to March 22 |
| 2020 H2 | 0.00 | Relief |
| 2021 H1 | 0.00 | Relief |
| 2021 H2 | 0.02 | October to December |
| 2022 H1 | 0.05 | |
| 2022 H2 | 0.06 | |
| 2023 H1 | 0.04 | |
| 2023 H2 | 0.05 | |
| 2024 H1 | 0.08 | Holloway Junction works traffic switches overrunning approved windows |
| 2024 H2 | 0.09 | Same |
| 2025 H1 | 0.03 | |
| 2025 H2 | 0.04 | |

Annual totals: 2019 0.38; 2020 0.03; 2021 0.02; 2022 0.11; 2023 0.09; 2024 0.17; 2025 0.07. The points total never exceeded 300 in a rolling six months. Teaching point for Chapter 58.3.5: on a demand-risk road, lost tolls already punish poor availability, so the performance regime is calibrated to safety and service, and its money amounts are small next to traffic risk. The 2023 restructuring (Case Bible 2.8, "new KPIs" for Corvus) adds no new Concession Deed KPIs; the "new KPIs" are in the Corvus O&M contract and pass performance payments through to Corvus up to 50% of its annual fixed fee.

## T.2 Procurement details (2013 to 2015)

### Evaluation method

The RFP (September 2, 2013) evaluated in three stages:

1. Pass/fail compliance: legal, insurance, Concession Deed markup within permitted departures, bid security, committed finance (below).
2. Technical score out of 100 (design and construction 35, tunnel and structures 20, operations and maintenance 20, tolling and customer service 15, traffic management during construction 10); minimum 70 to proceed.
3. Price: the lowest requested state construction contribution, a nominal amount payable at opening, among bids passing stages 1 and 2. Maximum tolls were fixed by the state, so the contribution was the only price variable (Case Bible 2.3).

Traffic forecasts were not scored. Partnerships Brannock's own traffic adviser (an engineering firm's transport-planning arm; never named) reviewed each bid's traffic case for "reasonableness" only, because bidders carried demand risk. Its August 2014 note called Pellow's car value of time "at the upper end of the plausible range." Maggie Dunleavy filed the note without asking for a sensitivity; this is part of her "where wrong" (Case Bible 4.2).

### Bid security

ARD 20.0 million per bidder, an on-demand guarantee from a bank rated A- or better, lodged with the bids (March 27, 2014) and maintained through BAFO. Forfeit if the preferred bidder withdrew, materially changed its bid, or failed to reach financial close within 180 days of appointment for reasons within its control. Northgate's security was returned on October 3, 2014. Merrick Motorway Partners' security was extended twice because the delay to close was NILO's credit approval, not the bidder's; it was released at financial close on May 27, 2015.

### Committed finance

| Instrument | Requirement at BAFO | Merrick Motorway Partners' BAFO |
|---|---|---|
| Bank mini-perm and contribution bridge | Credit-approved commitment letters with agreed term sheets, conditional only on documentation | Letters from Castellan, Penhallow, Kaito Pacific and Sterrenberg |
| BIFA revenue bonds | Underwriting commitment with a maximum coupon | Castellan Bank and Penhallow Bank as underwriters, coupon cap 5.10% (priced at 4.85% in May 2015) |
| NILO loan | NILO eligibility letter (NILO approves credit only for a named preferred bidder) | Eligibility letter; full credit approval came in April 2015, which is why close slipped from December 2014 to May 27, 2015 |
| Equity | Sponsor board approvals and equity commitment letters | Holbrook, Wexcombe III and Corvus board approvals |

Base-rate risk between BAFO and financial close sat with the bidder; the contribution did not move.

### The other bidders

- **Northgate Mobility Consortium**: a consortium of a foreign construction group, a domestic pension fund's infrastructure arm and a European toll operator (members never named). BAFO contribution ARD 361.0 million. Traffic basis: its own adviser's forecast, mature 2019 level 53.9 thousand trips a day; ramp-up factors 2019 0.76, 2020 0.88, 2021 0.95, 2022 0.99, 2023 on 1.00; growth 3.0% to 2030, 2.1% 2031 to 2040, 1.1% after. Bid-case equity IRR stated in its BAFO model: 11.0% nominal post-tax. (Book inputs; the Northgate case is not a Case T model run.)
- **The third consortium** (never named; led by a European contractor) withdrew in January 2014 because its contractor would not take full Merrick Ridge Tunnel ground risk under the RFP's risk allocation (T.6).

### Gaps between the winner, the reference and Northgate (book inputs, D-013 arithmetic)

| Comparison | ARD m | Percent |
|---|---|---|
| Reference contribution less winning contribution (410.0 less 287.4) | 122.6 | Winning bid 29.9% below the reference |
| Northgate less winning contribution (361.0 less 287.4) | 73.6 | Winning bid 20.4% below Northgate |
| Reference less Northgate (410.0 less 361.0) | 49.0 | Northgate 12.0% below the reference |

Northgate's mature traffic (53.9) sits between Ridgeway's banking level (52.6) and Pellow's (58.4), which is the winner's-curse picture Chapter 47 draws: the lowest contribution came from the most optimistic traffic case.

## T.3 Pellow's value-of-time cases (2014)

Pellow's 2014 bid report presented three car value-of-time (VoT) cases, in 2014 prices. Pellow recommended the central case; Callum Petrie chose the high case for the BAFO (Case Bible 4.2).

| Pellow case | Car VoT (ARD per vehicle-hour, 2014 prices) | Mature 2019 level (k trips/day) | Use |
|---|---|---|---|
| Low | 17.10 | 51.2 | Sensitivity |
| Central | 19.80 | 54.6 | Pellow's recommendation |
| High | 22.45 | 58.4 | Sponsor base case (Case Bible 2.6) |

The 2021 revealed-preference survey (Case Bible 2.6) found a car VoT of ARD 18.40 per vehicle-hour in 2014 prices; the high case is 22% above it (18.40 x 1.22 = 22.45). Ramp-up factors and growth rates are the sponsor base's for all three cases. Heavy-vehicle VoT was common to all cases. The bid equity IRR at ARD 287.4 million on the low and central cases is requested as figure T-F21 (optional for Chapter 47).

## T.4 D&C contract, interface agreement and tolling subcontract

### D&C liability regime (adds to Case Bible 2.5)

| Term | Value |
|---|---|
| Aggregate liability cap | 60% of the D&C contract price (ARD 1,010.6 million on ARD 1,684.3 million) |
| Delay LD sub-cap | 20% of price (Case Bible 2.5), within the aggregate cap |
| Exclusions from the cap | Fraud, wilful default, abandonment, death and personal injury, losses recovered under project insurances |
| Ground risk | Full ground risk with the JV, including the Merrick Ridge Tunnel; the geotechnical baseline report informed pricing but gives no relief (T.6) |
| Parent guarantees | From the ultimate parents of Holbrook Civil and Daneshill Construction, joint and several, each capped at the aggregate cap |
| Performance security | 10% (Case Bible 2.5) by on-demand bank bond |

### Interface Agreement

Signed at financial close on May 27, 2015 among Merrick Link Concession Co Ltd, the Holbrook-Daneshill Joint Venture and Corvus Road Services; Quillfield Tolling Systems Ltd acceded on the same day for tolling matters. Terms:

- Corvus reviews designs for maintainability and operability at 30%, 70% and 100% stages; its comments bind the JV unless the independent certifier rules them a change.
- Joint commissioning program; tolling and ITS handover to Corvus only after the tolling acceptance test (below).
- Defects reported by Corvus during the 24-month defects period go straight to the JV with copies to the concessionaire.
- A single three-member Dispute Board hears any dispute involving more than one of the D&C contract, the O&M contract and the Concession Deed, so that the three contracts get one finding of fact.
- Liability for interface breaches: up to ARD 10.0 million per party per year, inside each party's main-contract cap.

### Tolling subcontract

| Term | Value |
|---|---|
| Subcontractor | Quillfield Tolling Systems Ltd, subcontractor to the JV (not to the concessionaire) |
| Scope | Free-flow gantries, transponder and video (automatic number plate recognition) systems, roadside and central systems, integration with the Corvus back office |
| Price | ARD 48.6 million, inside the D&C price (Case Bible 2.5) |
| Delay LDs to the JV | ARD 95,000 per day, capped at 15% of the subcontract price (ARD 7.29 million) |
| Aggregate cap | 100% of the subcontract price |
| Tolling acceptance test | 30-day trial operation on live traffic: at least 99.0% transaction capture and at least 98.5% correct vehicle classification and video matching |
| After opening | An 8-year Tolling Maintenance and Support Agreement directly between Quillfield and Corvus Road Services, from opening, matching the 8-year tolling and ITS replacement cycle (Case Bible 2.5); its cost is inside Corvus's tolling back-office charge (no new model input) |

### Cause of the 36-day opening delay

The first tolling acceptance test (February 4 to March 5, 2019) reached 97.2% video matching against the 98.5% standard. Quillfield retuned the video-matching software; the second test ran from April 4 to May 3, 2019 and passed, and the road opened on May 6, 2019. The JV paid the concessionaire delay LDs of ARD 10.26 million (36 days at ARD 285,000; Case Bible 2.5) and recovered ARD 3.42 million from Quillfield (36 days at ARD 95,000). The tunnel finished on time. This is the Chapter 23 interface lesson.

## T.5 New character: Dimitri Kalogeropoulos (D&C project director)

Ardmorean, born 1966 in Port Ellery to Greek-born parents. Civil and tunneling engineer; twenty years with Daneshill Construction on rail and road tunnels; Project Director of the Holbrook-Daneshill Joint Venture (2014 to 2019), seconded from Daneshill.

He wants the tunnel through on program and the JV's margin intact. He fears ground he has not seen, and owners' engineers who redesign during construction. He negotiates by program, conceding money before days. Verbal habit: speaks in chainages ("at chainage 14.2 that's three weeks").

Where he is wrong: in 2014 he tells Callum the fault zone can be priced at the baseline (the JV later absorbs the overrun, T.6); in 2018 he treats tolling integration as "Quillfield's problem," and the failed acceptance test delays opening by 36 days. Arc: prices the D&C for the BAFO (2014, Chapter 23), runs construction (2015 to 2019), hands over in May 2019. Chapters: 12 (optional, alongside Callum and Sasha), 23.

## T.6 Merrick Ridge Tunnel: ground conditions and method

| Item | Value |
|---|---|
| Configuration | Twin two-lane bores, 1.9 km each, about 30 m apart; 14 cross-passages at about 120 m spacing; jet-fan longitudinal ventilation |
| Maximum cover | About 95 m |
| Geology | Interbedded sandstone and siltstone, moderately to slightly weathered, with a fault zone about 180 m wide near mid-ridge containing crushed, clay-rich and water-bearing ground |
| Method | Sequential excavation by roadheader with shotcrete and rock bolts; pipe-umbrella presupport, face bolting and drainage drilling through the fault zone; drained design with a waterproofing membrane and cast in-situ final lining |
| Excavation | From both portals, 2016 to 2017; northbound breakthrough October 2017, southbound December 2017 |
| What happened | Water inflows and overbreak in the fault zone exceeded the geotechnical baseline in mid-2017. Under full ground risk the JV bore the extra cost (about ARD 26 million, a JV loss and not a project cost; book input) and added a third shift. No delay to opening came from the tunnel. |

## T.7 SR 14 pre-opening traffic counts

Two-way annual average daily traffic (vehicles a day) at BRTA's Coldwater North screenline on State Route 14 (book inputs):

| Year | Vehicles a day | Heavy vehicles share | Note |
|---|---|---|---|
| 2008 | 54,200 | 12.4% | |
| 2012 | 61,400 | 12.8% | Business case base year |
| 2014 | 66,900 | 13.0% | Bid year; weekday peak end-to-end travel time 71 minutes over 47.6 km |
| 2018 | 74,300 | 13.1% | Last full year before opening |
| 2019 H2 | 52,800 | 14.6% | After opening (heavy vehicles stayed on SR 14, Case Bible 2.6) |

Screenline vehicles a day on SR 14 are not the same unit as Merrick Link trips a day (Case Bible 2.6: average trip 23.8 km); writers say so whenever they compare them.

## T.8 Handback requirements (Concession Deed, Schedule 15)

Handback date: May 26, 2059 (extended term). Requirements at handback, certified by the independent certifier:

| Asset | Requirement |
|---|---|
| Pavement | At least 7 years of residual structural life; surface condition at or better than the Schedule 15 roughness and rutting limits; no Category 1 defects outstanding |
| Structures (viaduct, bridges, tunnel lining) | No element below condition rating 3 on the 1 to 5 inspection scale |
| Tunnel mechanical and electrical systems | Each major system with at least 5 years of residual design life, or replaced within the last 10 years |
| Tolling and ITS | Fully operational; source code and data delivered under escrow; transferable licenses |
| Records | As-built drawings, asset register, maintenance history |

Process: joint handback survey 60 months before expiry (May 2054), repeated at 24 months; the certifier fixes a handback works estimate. The concessionaire funds a handback reserve over the final five years (ten semiannual periods) to that estimate; BRTA may draw the reserve for works not completed, and the balance is released to the concessionaire after the final certificate. The model uses a handback works estimate of ARD 42.6 million in 2015 prices (Case T modeler's assumption, adopted here).

## T.9 Value for money (recalibration adopted)

The Case T modeler recalibrated the PSC risk adjustments after the editor-in-chief's review (u12 flaw 5): construction risk 7.8% of raw capex, traffic revenue risk 4.8% of retained toll revenue, operating risk 3.8% of O&M and lifecycle, competitive neutrality 1.0% of gross costs, replacing the Case Bible 2.3 values (221.7, 274.0, 41.3, 38.4). This annex adopts the recalibration (the modeler's change T-C05 in Case Bible Part 8). The new values are in `inputs_case_t.json` and T-F01; writers print the PSC components only from T-F01. Teaching point retained for Chapter 57: the PSC still drew on Pellow's corridor study, so the traffic revenue retained by the state in the PSC is optimistic, and the value-for-money margin of the winning bid rests on the same optimism as the bid. T-F01 must also report VfM as a share of the gross PSC cost (costs and risks before netting retained toll revenue) as well as of the net PSC (Section F).

## T.10 Restructuring plan: classes, votes and cram-down

The plan was sanctioned by the Supreme Court of Brannock under Part 9 of the Companies Act (Ardmore) after the November 30, 2023 hearing; judgment was given on December 11, 2023 and the plan took effect on December 18, 2023. This annex adopts the Case T modeler's class structure (`modeler_assumptions.plan_classes_and_votes`):

| Class | Members | Vote (by value) | Result |
|---|---|---|---|
| 1 | Senior bank lenders (Castellan, Penhallow, Kaito Pacific, Sterrenberg) | 100% for | Approves |
| 2 | BIFA Series 2015 bondholders, voting through the bondholders' representative | 88.6% turnout; 91.4% of those voting for | Approves |
| 3 | NILO | 100% for | Approves |
| 4 | Shareholders and shareholder lenders (Holbrook 40%, Wexcombe 35%, Corvus 25%) | 60% for (Wexcombe and Corvus for; Holbrook against) | Dissents |

Threshold: 75% by value of those voting in each class. Banks and bondholders vote separately because their rights differ (the bank swap set-off, the bond's tax-exempt status and conduit structure), though the plan treats them equally. The court applied cross-class cram-down to class 4. Relevant alternative: termination for concessionaire default followed by retendering under Case Bible 2.7, valued at June 30, 2022 in T-F08 and updated by the plan's evidence to the hearing date; in it shareholders and shareholder lenders recover nothing, so they are no worse off under the plan, and the plan was approved by classes that would receive value in the relevant alternative. Holbrook's objection (that the state's contribution was "value created for the state, not the creditors") failed. The state is not a plan creditor; it is a party to the restructuring support agreement and the Concession Deed amendments. Trade creditors, Corvus's O&M contract and the JV (no outstanding claims by 2023) were left out of the plan. By June 2023 about a quarter of the bonds by value had been sold by insurers to distressed-debt funds (T.15); those funds voted for. The judgment date (December 11, 2023) is a book input.

## T.11 Equity allocation rationale

The Case T modeler values the plan's securities at a 14.0% equity rate, a 7.50% market yield for the Restructured Senior Notes and NILO's 3.06% contract rate (`modeler_assumptions.plan_valuation`); results in T-F09. On that valuation, the state's ARD 120.0 million splits into two parts (`modeler_assumptions.state_money_allocation`, adopted here):

1. A subscription for 15% of the new equity at the plan value of that 15%; and
2. A capital grant equal to the remainder, applied to the Holloway Junction interchange upgrade, a public asset the state wanted and had deferred (Case Bible 2.6).

So the state's price per percentage point is several times the creditors' conversion price, and that is intended. The creditors' 85% is not a bargain either: they give up the 14.0 cancelled points as well as the 10.0 converted points, and their recovery is the notes plus the equity (T-F09 reports all three prices per percentage point and the recoveries). Story: Owen Reddaway insisted that "any state money buys equity" (Case Bible 4.2) to avoid a grant headline; Quarrington's plan valuation showed that most of the money was in substance a grant; the parties kept the equity form, and the 2023 parliamentary inquiry recorded the grant element. Writers print the per-point prices, the plan equity value and the implied grant only from T-F09. The six-year extension, the heavy-vehicle toll cut and the CPI-only escalation are concessions with their own value effects, shown in T-F10; they are not part of the ARD 120.0 million.

## T.12 Owen Reddaway's career (replaces the dates in Case Bible 4.2)

Treasury economist (1996 to 2009); Director, Fiscal Risks Unit, Brannock Treasury (2009 to 2015), which is his title in the November 2012 business-case scene (Chapter 57); Executive Director, Commercial Projects (2015 to 2019); Deputy Secretary (Commercial) from 2019.

## T.13 The 2024 light-rail line and the 2024 Partnerships Brannock director

- **Ellery Crosstown Light Rail**: a 16.2 km line with 21 stops across Port Ellery's inner suburbs; availability-based DBFOM including rolling stock; the state keeps fare revenue and demand risk (the lesson drawn from the Merrick Link). Estimated capital cost ARD 3.1 billion in 2024 prices. Expressions of interest March 2024; three consortia shortlisted September 2024; RFP planned for 2025. (Book inputs; Chapter 80, small.)
- **Nerida Faulkes**, Director, Partnerships Brannock, from July 2020 (Maggie Dunleavy's successor). Ardmorean, born 1976. Government lawyer; Partnerships Brannock commercial lead on the 2016 hospital PPP (T.14); Director from 2020. Wants a pipeline of availability PPPs that the state can afford and explain. Fears another demand-risk failure on her watch. Verbal habit: "Show me the payment mechanism." Minor character; Chapters 80 and 81 (optional). The Chapter 80 scene may keep Maggie in her Advisory Board role and bring Nerida in as the official presenting the line.

## T.14 The 2016 hospital PPP

**Port Ellery Northern Hospital**: 412 beds; availability-based DBFM (hard facilities management only; clinical and soft services stay with the state health service). Capital cost ARD 735 million. Preferred bidder March 2016; financial close August 30, 2016; construction to April 2019; 25-year service period. Maximum annual service payment ARD 68.2 million in 2016 prices, 75% indexed to Ardmore CPI, with an availability-and-performance deduction regime by functional unit. Concessionaire: Ellery Health Infrastructure Partners (consortium; members never named). Senior debt: 88% of funding, from a bank club led by Penhallow Bank with Kaito Pacific Bank. Run by Partnerships Brannock under Maggie Dunleavy, with Nerida Faulkes as commercial lead. (Book inputs; Chapter 81, small.)

## T.15 Ardmore insurers' capital regime (Chapter 68)

Ardmore insurers are regulated by the Commonwealth's prudential regulator (never named) under a risk-based standard formula. Bonds carry a spread-risk charge that rises with lower ratings and longer duration; the formula has no separate infrastructure asset class and no matching-adjustment equivalent. Demand for the BIFA Series 2015 bonds came from their tax-exempt coupon (Case Bible 2.5), not from capital relief. The bonds were rated BBB by one agency at issue (May 2015), downgraded to BB+ in June 2020 and to B- in April 2021 after the standstill. Each downgrade raised insurers' capital charges, and several insurers sold to distressed-debt funds in 2021 and 2022 (T.10). (Book inputs.)

## T.16 Character and storyline fixes

- Callum Petrie (Case Bible 4.2): read "Callum's last scene in story order is the restructuring meeting where Holbrook gets nothing (Chapter 64)." He still appears in Chapter 79 (story date 2021), which comes later in book order.
- Part 6, row 12: add Sasha Hrytsenko (and optionally Dimitri Kalogeropoulos) to the Case T characters.
- Part 6, row 23: add Dimitri Kalogeropoulos. Inputs: T.4.
- Part 6, row 58: inputs T.1, T.2; figures T-F01 (extended), T-F02 (extended).
- Part 6, row 47: Case T figures T-F02 (extended), optional T-F21; inputs T.2 and T.3.
- Part 6, row 64: inputs T.10 and T.11; figures as before.
- Part 6, row 79: figures T-F04, T-F06, T-F18, T-F19.
- Part 6, rows 45 and 48: add T-F18 and T-F19 where the traffic shortfall is discussed.
- Part 6, rows 80 and 81: T.13 and T.14 as inputs; Nerida Faulkes optional.

## T.17 Traffic ratios and shortfall decomposition

- **T-F18** (new): ratio of actual traffic to the Pellow sponsor base, to the Ridgeway banking case and to the downside, by year 2019 to 2026; from 2024 also the ratio to Ridgeway's 2023 restructuring case. Computed by the Case T modeler from T-F04 values.
- **T-F19** (new): decomposition of the shortfall of actual traffic against the Pellow case, 2019 to 2022, by cause. The shares are Bible inputs; the modeler multiplies them by each year's shortfall.

| Cause | 2019 | 2020 | 2021 | 2022 |
|---|---|---|---|---|
| Coldwater Plains housing completions about four years late | 41% | 23% | 29% | 36% |
| Car value of time 22% above revealed preference (T.3) | 29% | 16% | 20% | 25% |
| Heavy vehicles avoiding the road on trips under 30 km | 20% | 11% | 14% | 18% |
| SR 14 traffic-calming works deferred by BRTA | 10% | 5% | 7% | 9% |
| COVID-19 and persistent working from home | 0% | 45% | 30% | 12% |
| Total | 100% | 100% | 100% | 100% |

---

# Part R. Case R: Mesa Corta Renewables

## R.1 The A1 sale process (2021 to 2022)

Seller Hollenbeck Energy North America ran a two-round auction through its financial adviser, a New York investment bank (never named).

| Date | Step |
|---|---|
| August 2021 | Teaser and confidentiality agreements; 14 parties sign |
| October 12, 2021 | Non-binding first-round bids; 9 received; 4 admitted to the second round |
| October to November 2021 | Virtual data room, management presentations, site visits |
| December 2, 2021 | Binding bids with SPA markups; 3 received (the "three final bidders", Case Bible 3.9) |
| December 4, 2021 | Lattimer selected; exclusivity granted |
| December 9, 2021 | SPA signed (Case Bible 3.6) |
| March 22, 2022 | Closing (Case Bible 3.6); long-stop date June 30, 2022 |

Chapter 9's diligence scene (P50 and P90 reading) is set in the confirmatory week of December 2021, between December 2 and December 9, or in late November before the binding bid.

### Price mechanism

Locked box at September 30, 2021, cash-free and debt-free (Hollenbeck repaid all asset-level debt at closing). Headline locked-box price USD 436.0 million, plus a ticker of 5.00% a year (simple, actual/365) on the headline from October 1, 2021 to closing: 173 days, USD 10.3 million. Total consideration paid at closing: USD 446.3 million, the figure fixed by D-014 and used by the model and R-F04 and R-F05. (Arithmetic: 436.0 x 5.00% x 173/365 = 10.33.) Leakage covenant from the locked-box date with permitted leakage limited to ordinary-course payments to Hollenbeck's affiliates of up to USD 0.4 million (asset management fees), which the headline already reflects.

### Warranties, indemnities and W&I

| Term | Value |
|---|---|
| Buy-side W&I policy limit | USD 118.0 million (Case Bible 3.6) |
| Retention | 0.5% of enterprise value (USD 2.2 million), falling to 0.25% after 12 months |
| Premium | 1.20% of the limit (USD 1.42 million), inside the USD 14.9 million transaction costs |
| Policy periods | General warranties 3 years; fundamental and tax warranties 7 years |
| Seller's liability | USD 1 for general warranties (clean exit); fundamental warranties to the price |
| Specific indemnity | From Hollenbeck for any February 2021 Winter Storm Uri settlement adjustments or charges allocated to R1 or R4 after signing, capped at USD 5.0 million and backed by a USD 5.0 million escrow for 18 months (known matter, excluded from W&I) |
| Conditions | Antitrust waiting-period expiry; consent of Castellan Bank as tax equity investor in R3 and R5; change-of-control consents under the R2 PPA and the R5 vPPA |

### Competing bids

| Bidder | Headline locked-box price (USD m) | Note |
|---|---|---|
| Lattimer Energy Transition Fund II | 436.0 | Winner; total consideration 446.3 with the ticker |
| Bidder B: a Canadian pension-backed renewables platform (never named) | 421.5 | Asked for a 10% escrow for R3 tax-equity flip risk |
| Bidder C: the unregulated arm of a US utility (never named) | 409.0 | Excluded the Uri indemnity from its markup |

Lattimer's first-round indication was USD 395 million to USD 415 million. Rafael raised it for the binding round on the high-case West solar capture (his "where wrong", Case Bible 4.3). All bidders bid on the same ticker. These are book inputs and do not change any model figure: the winner's consideration is already USD 446.3 million, slightly above the base-case breakeven in R-F04.

## R.2 Ostrander Data Systems: credit profile and vPPA credit support

Ostrander Data Systems Inc. is a privately held colocation and build-to-suit data-center operator, owned since 2018 by two infrastructure funds (never named). Profile (book inputs):

| Item | 2020 | 2024 | 2026 |
|---|---|---|---|
| Data centers (operating and under construction) | 11 | 21 | 34 |
| Critical IT load (MW, committed) | about 240 | about 610 | about 1,050 |
| Revenue (USD billion) | 0.71 | 1.52 | about 2.3 (run rate) |
| Corporate rating (one agency) | Unrated | BB- (upgraded November 2024 from B+, assigned 2022 on its debut notes) | BB- |

Funding: secured term loans, data-center asset-backed notes and build-to-suit leases with hyperscale tenants. Lattimer cannot see the lease terms behind its growth (Chapter 82).

R5 vPPA (signed by Hollenbeck in March 2020; Case Bible 3.4) credit support:

| Term | Value |
|---|---|
| Ostrander standing LC | USD 5.0 million, from a bank rated A- or better |
| Ostrander collateral threshold | Mark-to-market exposure of R5 to Ostrander above USD 10.0 million is collateralized by cash or LC; the threshold falls to nil if Ostrander is rated below B or defaults |
| R5 collateral threshold | Mark-to-market exposure of Ostrander to R5 above USD 15.0 million is collateralized by an LC from the opco LC facility |
| Parent support | None; Ostrander is the contracting entity |
| Termination | Either side may terminate on the other's failure to post within 3 business days |

Teaching point: at the base-case prices the strike (USD 27.85/MWh) is below the settlement value, so R5 pays settlements (R-F02) and the exposure mostly runs from Ostrander to Mesa Corta; Ostrander's credit matters chiefly in the low price case. The posted amount at any date is not a ledger figure and is not printed. The model ignores LC fees (no new model input).

## R.3 The 2024 hydrogen developer (Chapter 83, small)

Marlowe Gulf Hydrogen LLC, a venture-backed developer planning a 120 MW electrolyzer near Corpus Christi, approached Lattimer in March 2024 for power from R2 (Sandoval Hills, coastal, South Hub) after the Orchard PPA ends. Proposed terms: 12 years from July 1, 2029; 100% of R2's as-generated output; USD 39.00/MWh flat, settled at South Hub, with hourly-matched RECs; conditional on Marlowe's final investment decision and on its qualifying for the federal clean hydrogen production credit (writers take the credit's rules only from the `t-hydrogen-support` fact sheet); credit support a USD 4.0 million LC and no parent guarantee. Lattimer's IC passed in May 2024: the offer was conditional, the credit thin, and the price did not compensate for giving up R2's merchant upside after 2029. (Book inputs; no model figure. Writers do not compare the price with model capture prices unless the ledger gives R2's post-2029 node price, R-F06.)

## R.4 R7 revenue floor: mechanics and payments

Adds to Case Bible 3.4 (Galloway Risk Solutions; floor USD 74.00/kW-year; premium USD 5.80/kW-year; 20% upside share above USD 140/kW-year; April 2, 2024 to April 1, 2032):

- Reference revenue: a benchmark 2-hour ERCOT battery revenue index (energy arbitrage plus ancillary services), which in the book is the Case Bible's illustrative battery revenue path (Case Bible 3.5), multiplied by R7's measured availability. The floor therefore protects against market revenue, not against R7's own dispatch performance. This is the rule the Case R model already applies (`case_r.py`).
- Settlement: quarterly on one quarter of the annual floor, trued up annually on the contract year; the first and last contract years are pro rata.
- Premium: netted against floor payments; Galloway's upside share is paid by R7 when reference revenue exceeds USD 140/kW-year.
- Credit support: Galloway's obligations are unsecured (it is an insurer-backed provider); R7's premium and upside obligations are backed by an LC from the opco LC facility (Case Bible 3.4).
- Floor payments (Galloway to R7) and upside share by year are new figure **R-F18**. In the base case the reference revenue (USD 61.8/kW-year in 2024, falling to 52.4 in 2025) is below the floor throughout, so Galloway pays every year. Writers print the amounts only from R-F18.

## R.5 Battery capacity fade and augmentation (R6 and R7)

New inputs (both batteries, LFP, 2-hour):

| Item | Value |
|---|---|
| Initial overbuild at COD | 8% of nameplate energy: R6 216 MWh usable at COD against 200 MWh nameplate; R7 324 MWh against 300 MWh |
| Capacity fade (percentage points of beginning-of-life usable energy per year, linear) | Year 1: 2.0; years 2 to 10: 1.5 a year; year 11 onward: 1.0 a year |
| Augmentation (Case Bible 3.3, unchanged) | 6% of nameplate MWh (R6 12 MWh; R7 18 MWh) installed at the start of calendar years COD+5 and COD+9, at USD 41/kWh in 2025 prices escalating 2.5% a year (model supplementary assumption, adopted) |
| Fade of augmentation modules | Same schedule from their own installation |
| Revenue rule | Merchant and reference revenue scale by the lesser of 1 and usable energy divided by nameplate energy |
| R6 toll | Paid in full while usable energy is at least 200 MWh and availability at least 97.0% (Case Bible 3.4) |

Check (R6, D-013 arithmetic): end of year 4, 216 x (1 - 0.065) = 202.0 MWh; end of year 7 (toll expiry, July 2030), base modules 216 x (1 - 0.110) = 192.2 MWh plus the first augmentation 12 x (1 - 0.020 - 0.015 x 2) = 11.4 MWh, total 203.6 MWh, so the toll requirement holds through its term. New figure **R-F19**: usable energy, augmentation MWh and augmentation cost by year, R6 and R7. If absorbing the fade moves the A2 or A3 base-case breakeven below the D-014 price by more than USD 1.0 million, the modeler reports it to the editor-in-chief; the D-014 prices stand.

## R.6 The green USPP (Case Bible 3.7, row 84)

| Item | Term |
|---|---|
| Framework | Mesa Corta Green Financing Framework, October 2025, prepared to align with the ICMA Green Bond Principles (the edition then current; writers cite the edition only from the `t-sustainable-finance-2` fact sheet) |
| Eligible categories | Renewable energy (R1 to R5, R8); energy storage (R6, R7) |
| Use of proceeds | 100% allocated at funding to refinance eligible assets (repayment of the opco term loan and the Redfern loan); no unallocated proceeds |
| Second-party opinion | Quenby Sustainability Review LLC (fictional), dated October 8, 2025: aligned with the principles, with one observation that grid-charged storage is not 100% renewable and that Mesa Corta should disclose charging sources |
| Reporting | Annual allocation and impact report until the notes are repaid: generation by asset (MWh), storage throughput, capacity, and avoided emissions using a stated grid emission factor |
| Covenant | Reporting is an undertaking; failure to report is not an event of default and carries no coupon step-up |
| Pricing | The label did not change pricing in the model; the coupons are those in Case Bible 3.7. Writers must not claim a greenium for this issue |
| Cost | SPO and framework costs inside the 1.10% transaction costs (no new model input) |

Characters: Thandeka leads the framework; Gwen Treharne may appear for two lines as lenders' IE (approved, u14 BF-12).

## R.7 Terminal value rule (decision)

Replace the "Terminal (after 2040)" row and the following sentence in Case Bible 3.8 with:

- Cash flows after 2040 and within each asset's useful life are discounted at the 10.50% unlevered post-2040 rate, applied from the valuation date for the whole period (the model's rule: discount factor (1.105)^-t for every year after 2040). Before 2040 each cash flow takes its bucket rate.
- No terminal value is taken beyond any asset's useful life (Case Bible 3.3). R1's repowering option is valued at zero in the base case.
- No separate post-2040 levered rate exists. Levered valuations (fund NAV) use the bucket-weighted levered rates in every year.
- In Chapter 46 the 10.50% is taught as a "tail rate" for long-dated, fully merchant cash flows, not as a terminal-value capitalization rate.

This matches model R-1.1; no model change.

## R.8 The 2026 data-center PPA offer (Chapter 88)

| Item | Term |
|---|---|
| Counterparty | Ketterman Digital Campuses LLC (fictional), developer of a hyperscale campus in West Texas, a special purpose company owned by a private developer and an infrastructure fund (never named) |
| Offer received | February 17, 2026 |
| Product | 15-year virtual PPA from January 1, 2029 on the output of a repowered R1, settled at West Hub, RECs bundled. Two options: (A) as-generated at USD 46.75/MWh flat; (B) an 85 MW 7x24 hourly block at USD 63.40/MWh flat, with Mesa Corta buying any shortfall hour at hub ("firming" risk on the seller) |
| Escalation | None |
| Credit support | Ketterman parent guarantee capped at USD 20.0 million plus a USD 12.0 million LC; stepping to a guarantee from the anchor tenant once a lease is signed |
| Conditions | Anchor-tenant lease signed by September 30, 2026; Mesa Corta repowering FID by March 31, 2027 |
| Repowering | Full repower: 47 turbines of 4.3 MW (202.1 MW nameplate, export limited to the existing 201.6 MW interconnection); P50 net capacity factor 43.5%; capital cost USD 1,350 to USD 1,600 per kW, central USD 1,450 per kW (2026 prices), so about USD 272 million to USD 323 million, central about USD 292 million on 201.6 MW |
| Timing | Construction January to November 2028, after R1's fixed-volume swap ends on December 31, 2027, so no swap volume falls in the construction outage; the existing turbines' decommissioning (R-F10) moves from 2044 to 2028, net of salvage |
| Tax credits | The base evaluation assumes no federal tax credit for the repowered R1; any credit is upside, and writers take its rules only from the US tax-equity fact sheet |
| Financing constraint | R1 is part of the USPP collateral (R-F12); repowering needs noteholder consent or the permitted-capex basket |
| Outcome | Open at the end of Chapter 88 (Case Bible Part 6) |

Figures: none (the storyline row stands). All prices labeled Illustrative.

## R.9 Timing and minor fixes

- **Chapter 71** (Lattimer IC declines a US offshore wind minority stake): May 2025 (Tuesday, May 20, 2025 if a date is needed).
- **Chapter 65** (R1 repower-or-retire and decommissioning provisions): January 2026, before the Ketterman offer; Carmen's analysis frames repower-or-retire generally and does not mention the offer.
- **Chapter 88**: offer received February 17, 2026; investment committee March 24, 2026. Case Bible 3.9 row "2026-03" stands.
- **Chapter 84**: Gwen Treharne may appear for two lines (approved).
- **Chapter 83**: story date March to May 2024 (R.3).
- **Chapter 47**: A1 auction per R.1.

---

# Part N. Name register additions (Case Bible Part 5)

Check method: web search on October 3, 2026 (searches were available for this pass). "Clear" means no real country, region, well-known city or organization of that name in a related field was found. Names constructed from already-registered fictional places (Port Ellery, Coldwater, Merrick) inherit their check.

## N.1 Chapter 1 illustrative deal (not a running case)

| Name | Type | Check |
|---|---|---|
| Republic of Corredana; Corredanan | Country (fictional, dollarized) | Clear as a country or region (near misses: a footballer's surname "Corredana"; Correda, Italy; Corredores canton, Costa Rica) |
| Llano Pardo; Llano Pardo plateau | Place | Clear (near misses: Llano Estacado, Texas; "Llanos" solar parks in Argentina and Chile) |
| Llano Pardo Solar SA | Project company | Clear |
| Electricidad Nacional de Corredana (ELNACOR) | State utility offtaker | Clear (near miss: Elecnor, a Spanish contractor; different spelling and field) |
| Tallisford Energy Partners | Developer and sponsor | Clear (near miss: Tallgrass Energy Partners, a US pipeline company; never mentioned) |
| Grupo Arismendi | Local sponsor | Clear as a company (Arismendi is a surname and a Venezuelan place and power-station name; the book never refers to those) |
| Montajes Cordillera SA | EPC contractor | Clear |
| Cordillera Servicios SA | O&M contractor | Clear (generic Spanish words) |
| Cooperativa Agrícola de Llano Pardo | Community stakeholder | Clear (inherits Llano Pardo) |

## N.2 Capstone (Chapter 89)

| Name | Type | Check |
|---|---|---|
| Republic of Salinera; Salineran | Country | Clear as a country or region. "Salinera" is a Spanish common noun (salt works) and appears in hotel and restaurant names (Strunjan, Slovenia; Palamós, Spain) and in "Salineras de Maras", Peru. Kept: it reads as grounded Spanish, not fantasy; no collision with a polity |
| Salineran peso, code SLP | Currency | **SLP is not an ISO 4217 code** (checked against the ISO 4217 active and historic lists via Wikipedia's ISO 4217 page and code-list searches; the nearest codes are SLE and the withdrawn SLL, Sierra Leone). Kept |
| UDS (Salineran inflation-indexed unit of account) | Unit of account | Not an ISO 4217 code; kept |
| Punta Garúa; Punta Garúa Desalination and Conveyance Project | Place and project | Clear ("garúa" is the coastal fog of Peru and Chile; no place of that exact name found) |
| Other capstone names (state water utility, PPP agency, mine, sponsors, contractors, DFI, ECA, banks) | Various | Not yet named by the capstone brief; to be checked and added when the capstone mini-Bible names them |

## N.3 Case T and Case R additions

| Name | Type | Case | Check |
|---|---|---|---|
| Quillfield Tolling Systems Ltd | Tolling subcontractor | T | Clear (no tolling or systems company of that name found) |
| Dimitri Kalogeropoulos | D&C JV project director | T | Character; not meant to resemble a real person |
| Nerida Faulkes | Director, Partnerships Brannock (2020 on) | T | Character; not meant to resemble a real person |
| Ellery Crosstown Light Rail | 2024 PPP line | T | Clear (built from fictional Port Ellery) |
| Port Ellery Northern Hospital; Ellery Health Infrastructure Partners | 2016 hospital PPP and its concessionaire | T | Clear (built from fictional Port Ellery) |
| Marlowe Gulf Hydrogen LLC | Hydrogen developer | R | Clear (no company of that name found; Marlowe is a surname) |
| Quenby Sustainability Review LLC | Second-party opinion provider | R | Clear (no ESG reviewer of that name found; Quenby Hall is an English country house) |
| Ketterman Digital Campuses LLC | Data-center developer | R | Clear (no data-center company of that name found; Ketterman is a surname) |

## N.4 Cross-case use of institutions (adds to Case Bible 4.4)

| Institution | Additional use |
|---|---|
| Sterrenberg Bank NV | Lender to the Chapter 1 illustrative deal, Llano Pardo Solar (2016) |
| Atlantic Basin Development Bank (ABDB) | Lender to Llano Pardo Solar (2016), illustrative |
| Penhallow Bank, Kaito Pacific Bank | Lenders to Port Ellery Northern Hospital (2016), Case T background |
| Castellan Bank, Penhallow Bank | Underwriters of the BIFA Series 2015 bonds (Case T) |

## N.5 Character register additions (Case Bible 4.5)

| Name | Case | Nationality | Born | Employer |
|---|---|---|---|---|
| Dimitri Kalogeropoulos | T | Ardmorean | 1966 | Daneshill Construction (Holbrook-Daneshill JV) |
| Nerida Faulkes | T (minor) | Ardmorean | 1976 | Partnerships Brannock |

---

# Part F. Figure register additions (Case Bible Part 7)

| ID | Figure | Scenario | Chapters |
|---|---|---|---|
| T-F01 (extended) | Adds VfM as a share of gross PSC cost and of net PSC, reference and winning bid, on the recalibrated PSC (T.9) | Inputs plus PV | 57, 58 |
| T-F02 (extended) | Adds the winning contribution's gap to the reference and to Northgate (T.2, ARD m and percent; arithmetic already in this annex) | Inputs | 47, 58 |
| T-F09 (extended) | Plan equity value; state subscription at plan value and implied capital grant; price per percentage point for the state and creditors; recoveries by class (T.10, T.11) | Actual history | 64 |
| T-F18 | Ratio of actual traffic to the Pellow, Ridgeway banking and downside cases, 2019 to 2026, plus ratio to Ridgeway 2023 from 2024 | Inputs | 45, 48, 79 |
| T-F19 | Shortfall against Pellow, 2019 to 2022, by cause (T.17 shares) | Actual history | 45, 48, 79 |
| T-F20 | Performance payments to BRTA by half-year 2019 to 2025 and their effect on CFADS and T-F07 DSCRs | Actual history | 58, 64 |
| T-F21 (optional) | Bid equity IRR at ARD 287.4 million on Pellow's low and central VoT cases (T.3) | Bid variants | 47 |
| R-F18 | R7 floor: reference revenue, floor payments from Galloway, premium, upside share, by contract year 2024 to 2032 | Base, low, high | 20, 73 |
| R-F19 | R6 and R7 usable energy, augmentation MWh and cost, revenue scaling factor by year | Base | 45, 73 |

---

# Part L. Change log for this annex

Format as Case Bible Part 8. These rows are also appended to `case-bible.md` Part 8. The Case T modeler's own rows T-C05 to T-C11 (PSC recalibration, bid CPI, ramp-up and sizing, test timing, NILO profile, plan classes and valuation, termination inputs) were entered in Part 8 concurrently; this annex adopts them and numbers its own rows from T-C12. T-C19 below records the judgment date and narrative on top of the modeler's T-C10.

| # | Date in story | Chapter | Case | Item changed | Old value | New value | Source of figure |
|---|---|---|---|---|---|---|---|
| T-C12 | 2013-09-02 to 2015-05-27 | 47, 58 | T | Procurement terms | Unspecified | Three-stage evaluation; ARD 20.0m bid security; committed-finance rules; Northgate traffic basis; third consortium's reason | Annex T.2 (book inputs) |
| T-C13 | 2015-05-27 | 23, 58 | T | Performance regime | "KPI deductions" only | Lane charges, KPI points, ARD 2,400 per point, 2.5% cap, thresholds 300/500/800 | Annex T.1 |
| T-C14 | 2019 to 2025 | 58, 64 | T | Actual performance payments | None | 2019 0.38 to 2025 0.07 (ARD m) by half-year | Annex T.1; T-F20 |
| T-C15 | 2015-05-27 | 23 | T | D&C cap, interface agreement, tolling subcontract | Unspecified | 60% aggregate cap; Interface Agreement; Quillfield subcontract; acceptance test | Annex T.4 |
| T-C16 | 2019-02 to 2019-05-06 | 23, 79 | T | Cause of the 36-day delay | Unspecified | Tolling acceptance test failure; JV recovers ARD 3.42m from Quillfield | Annex T.4 |
| T-C17 | 2016 to 2017 | 12, 23 | T | Tunnel ground and method | Unspecified | Sandstone/siltstone with fault zone; sequential excavation; JV absorbs overrun | Annex T.6 |
| T-C18 | 2059-05-26 | 58, 65 | T | Handback requirements | Reserve only | Schedule 15 requirements; surveys at 60 and 24 months | Annex T.8 |
| T-C19 | 2023-12-11 | 64 | T | Plan classes, votes, judgment date | Unspecified | Four classes; class 4 dissents and is crammed down; judgment December 11, 2023 | Annex T.10 |
| T-C20 | 2023-12-18 | 64 | T | State's ARD 120.0m characterization | 15% of equity | Subscription at plan value plus capital grant | Annex T.11; T-F09 |
| T-C21 | n/a | 57 | T | Owen Reddaway's career dates | Undated | Fiscal Risks Unit director 2009 to 2015 | Annex T.12 |
| R-C11 | 2021-08 to 2022-03-22 | 47 | R | A1 process and price mechanism | Price only | Locked box at 2021-09-30; headline 436.0 plus 5.00% ticker; total 446.3 unchanged; W&I terms; bids 421.5 and 409.0 | Annex R.1 |
| R-C12 | 2024-04-02 | 20, 73 | R | R7 floor reference and settlement | Floor terms only | Benchmark index times availability; quarterly with annual true-up | Annex R.4; R-F18 |
| R-C13 | 2023-07-14 and 2024-04-02 | 45, 73 | R | Battery overbuild and fade | Augmentation only | 8% overbuild; fade 2.0 / 1.5 / 1.0 points a year | Annex R.5; R-F19 |
| R-C14 | 2025-10 | 84 | R | Green USPP framework | Label only | Framework, Quenby SPO, reporting, no greenium | Annex R.6 |
| R-C15 | n/a | 46 | R | Terminal value wording | "Terminal (after 2040)" and "no terminal value" | Post-2040 tail rate within useful life; no TV beyond life; no post-2040 levered rate | Annex R.7 |
| R-C16 | 2026-02-17 | 88 | R | Data-center offer terms | Tenor only | Ketterman Digital Campuses; options A and B; repowering parameters | Annex R.8 |
| R-C17 | 2020-03; 2024-11 | 20, 82 | R | Ostrander profile and vPPA credit support | Absent | Profile; thresholds 10.0 and 15.0; LC 5.0 | Annex R.2 |
| R-C18 | 2024-03 to 2024-05 | 83 | R | Hydrogen developer offer | Unnamed | Marlowe Gulf Hydrogen; 12 years at USD 39.00/MWh; IC passes May 2024 | Annex R.3 |
| N-C01 | n/a | 1, 89 | All | Name register | Unregistered | Part N entries | Annex N |
