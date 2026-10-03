# Chapter 2 review, round 3: domain expert

**Verdict: FAIL.**

I checked the round-2 section of `reviews/02/r1-revision.md` and reread every passage it changed: Example 2.1 (the PPA), framework question 2, walkthrough Steps 1, 2, 4 and 6, Exhibit 2.3, Solution 2.7, and the drill.

All four round-2 items are fixed and the new figures check out. The verdict is FAIL only because of two short defects in Step 2 of the walkthrough, which is the chapter's centrepiece:

- the cushion reasoning contradicts itself (D1);
- the dividend cut is presented as the board's to make, which it is not under Chilean law (D2).

Each needs one or two sentences. Once both are in, I expect to pass the chapter without another full read.

## Round-2 items

| Item | Status | Note |
|---|---|---|
| N1 The cushion | FIXED, but see D1 | Step 2 now states the breaking falls (4.8%; 0.2%). It sets a policy, retains 33.6 of the dividend, and gives 3.15x before a call and 3.31x after a full call, which breaches only on a 5.5% fall. It attaches a quarterly trailing-twelve-month forecast and lists the rejected alternatives. The drill now concedes that the headroom use is capped and temporary. I recomputed: 574.4/182.4 = 3.15x; 603.6/182.4 = 3.31x; breaking EBITDA 172.5 (−5.4%; 5.5% as printed rounds from 5.45%); 164.1 before a call (−10.0%). These are consistent. |
| N2 The standby facility as a lender concession | FIXED | The text now says it is "a concession, not protection for the lenders". It states that the base loan plus the fully drawn standby must pass the cover-ratio and gearing tests. Drawing order is a negotiated term, with the fixed-ratio alternative mentioned. Fees are given (0.66 upfront, a commitment fee, possibly a higher margin). The fallback and its cost to headroom are named. Step 4 shows 317.5 drawn and its effect on cover ratios and distributions. Committed 321.4 is 71.7% of cost plus the cap overrun, within the 75% gearing limit. |
| N3 PPA settlement | FIXED | The PPA is pay-as-produced and settled at the wind farm's node, so the miner bears the node basis and GLA keeps curtailment risk. This matches Chilean practice for a contract defined at the injection node, and Step 4 refers back to it. |
| N4 Fit-test currency | FIXED | Question 2 now applies the currency test to both contracted and merchant revenue. The four applications still hold. |

## New defects

**D1. Step 2 calls a 4.8% cushion too thin, then adopts a 5% policy without explaining why that is enough.**

Step 2 says the 3.33x position "is already a thin cushion" because "a Chilean generator's EBITDA moves by more than that [4.8%] with hydrology and spot prices in an ordinary year". It then sets a policy of about 5% after a full call. Read as written, the paper rejects 4.8% as inadequate and accepts 5.5%.

The policy can be defended, but only on reasoning the text does not give. After the dividend restraint, the base cushion is 10.0%. The 5% floor applies only in a joint stress: the full cap has been called **and** EBITDA has fallen at the same time.

Required fix: add one sentence after the policy is stated, along these lines: "The 5% floor applies only after a full call of the cap, a joint stress in which the overrun and a weak hydrological year coincide; before any call the restraint keeps a 10.0% cushion, about double what the paper judged too thin at 3.33x." The words may differ but the logic must be there.

Also label the policy as GLA's own, for example "GLA's illustrative treasury policy", so that it does not read as a market norm.

**D2. The dividend cut is presented as the board's decision, with no legal or market constraint.**

"GLA will pay half its usual USD 67.2 million annual dividend in 2025" treats the cut as the board's alone. For a Chilean listed sociedad anónima this is wrong in two ways:

- The final dividend is approved by the ordinary shareholders' meeting on the board's proposal.
- Law 18,046 on corporations (Ley 18.046, art. 79) requires an open corporation to distribute at least 30% of each year's net profit unless shareholders agree unanimously otherwise.

Halving a listed generator's dividend also sends a signal that investors and rating agencies will read. A board paper must deal with that.

Required fix:
1. Reword to "the board will propose to the 2025 shareholders' meeting a dividend of half the usual USD 67.2 million, which stays above the legal minimum of 30% of net profit (Chile, Law 18,046, art. 79)".
2. Add a clause noting that the paper must explain the cut to investors as a one-year retention to fund Alto Huelén.

The facts reviewer should confirm the article citation against the current text on bcn.cl. The rule itself is settled.

**Minor (consistency or numbers to confirm): Exhibit 2.3, row "All-in annual cost (bps)".**

The cell "248.0 (3.1 a year more)" puts a USD million figure in a row labeled in bps. Required fix: "248.0 (106.6 more; USD 3.1 million a year)".

## Sign-off: the illustrative 5% EBITDA cushion policy

**Signed off on condition that D1 is fixed.**

A floor of about 5% of EBITDA after a full call of a capped sponsor undertaking is a defensible treasury policy for an investment-grade generator, provided:

- it is presented as a joint-stress floor;
- the base-case cushion is materially larger (here 10.0%);
- it is labeled as GLA's illustrative policy, not a market norm.

In the base case, practitioners in this position usually aim for wider cushions: of the order of 10% to 20% of EBITDA, or about 0.25x to 0.5x below the covenant. The chapter's 10.0% base cushion falls within that range, which is why I sign off the 5% figure.
