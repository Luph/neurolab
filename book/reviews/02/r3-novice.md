# Chapter 2 review, round 3: novice reader

Reviewer role: novice (standards §12.2). I know only what Chapter 1 teaches, as set out in the Chapter 1 brief. I verified my five round-2 items against the "Round 2" section of `reviews/02/r1-revision.md`. I then read every passage changed in round 2: Example 2.1's PPA paragraph, ssec:2.4.5, ssec:2.5.2, ssec:2.5.3, walkthrough Steps 1 to 6, Exhibit 2.3, the judgment drill, and Solution 2.7. Line numbers refer to the current file.

## Verdict: FAIL

All five round-2 items are fixed. The round-2 domain and facts changes added new content, and six new gaps came with it, the same kind of gap as in earlier rounds:
- **Undefined terms (defects 1, 2, 5 and 6):** nodal settlement, "unincorporated joint venture", "bankruptcy-remote", and "trailing twelve-month EBITDA".
- **Exhibit 2.3 (defect 3):** the leverage figures no longer match the walkthrough text.
- **Standby facility (defect 4):** Example 2.1 and Step 2 now describe it in ways that seem to contradict each other.

Each fix is one clause or one table cell.

## Round-2 items: verification

| # | Status | Evidence |
|---|---|---|
| 1 | Fixed | l.193: "a bank guarantee (in construction usually called a performance bond, \cref{ch:22})" |
| 2 | Fixed | l.219 glosses "amortizes"; l.382 glosses "bullet bond" |
| 3 | Fixed | l.112 gives the grade ladder (AAA to BB); l.310 reads "around BB" and "borrowers rated A" |
| 4 | Fixed | The Exhibit 2.3 note explains the unchanged after-COD leverage. Defect 3 below raises a separate mismatch. |
| 5 | Fixed | l.471 and l.494 both use "PPP unit" |

## New defects

1. **Example 2.1 (l.133) and walkthrough Step 4 use market-settlement terms the reader has not met.** The passages say "settled through Chile's national power market at the wind farm's own node", "the difference between the price at the wind farm's node and at its own", and "the system operator curtails". Chapter 1's PPA was a plain sale to a single-buyer utility, so the reader has no idea what a node, nodal price, settlement, or system operator is. Without that, the sentence about who bears the price difference cannot be followed. Fix: at l.133 add one clause: "in a market that sets a separate wholesale price at each point (node) of the grid, the system operator being the body that runs the grid and decides which plants run". Point to the home of nodal pricing (\cref{ch:12}), and rephrase as "the miner pays GLA the contract price and settles any difference between the two nodes' prices".

2. **ssec:2.5.3, l.316: "an unincorporated joint venture that borrowed through a jointly owned company" is undefined.** The phrase also seems to contradict the paragraph's own claim that partners invest through "a project company with its own debt". Fix: gloss in one clause, for example "a partnership created by contract rather than a company, in which each partner owns its share of the assets directly". Then say that PNG LNG Global Company played the borrowing role that a project company plays at Llano Pardo. Optionally, point out that the co-venturers' guarantee until financial completion is the completion-guarantee rung of \cref{fw:recourse-ladder}, which ties the example back to the chapter.

3. **Exhibit 2.3 (l.448 to l.454) no longer agrees with Step 2.** Step 2 says the halved dividend brings parent leverage after the equity to 3.15x. The exhibit's first two rows still show project-finance leverage of 3.33x for construction and after COD, while its "EBITDA fall" row ("10.0% before a call") depends on the 3.15x figure. A reader comparing the exhibit with the text cannot tell which leverage applies. Fix: label the two leverage rows "before dividend restraint" and add a row "Parent net debt to EBITDA after the equity, with dividend restraint (x): 3.15". Alternatively, show "3.33 (3.15 with restraint)" in both cells.

4. **The standby facility is described inconsistently between Example 2.1 (l.145) and Step 2.** Example 2.1 says lenders to a non-recourse construction loan "size a contingency inside the budget and often a standby facility" as their buffer against overruns. Step 2 says "That is a concession, not protection for the lenders: the standby is more senior debt". To a novice these statements contradict each other. Fix: in Step 2 replace the sentence with "For the lenders the standby cuts both ways: it ensures the overrun is funded, but it is more senior debt, drawn exactly when the project is in trouble, so they treat it as a concession to the sponsor." Optionally, add "(the buffer of \cref{ex:2.1}, here sized to replace sponsor support)".

5. **ssec:2.4.5, l.239: "the bankruptcy-remote structure of the company that built London's Thames Tideway Tunnel ... an entire licensed business" uses two terms the book has not taught.** "Bankruptcy-remote" and "licensed business" in the regulatory sense are both new to the reader. Fix:
   - Gloss bankruptcy-remote: "a structure designed so that the company cannot easily be pulled into an insolvency, its own or its owners'". Note that this is the ring-fence idea of ssec:2.1.2.
   - Gloss licensed business: "a business that operates under a government license, here regulated as a utility".

6. **Walkthrough Step 2: "on trailing twelve-month EBITDA" is undefined.** The same sentence's "hydrology" (meaning a hydro-heavy generator's output in wet and dry years) is also unclear. Fix:
   - Gloss trailing twelve-month EBITDA: "EBITDA over the most recent four quarters, the basis on which the covenant is tested".
   - Write "rainfall, which drives hydro output," in place of "hydrology".

No other passage blocked me. The rewritten walkthrough's arithmetic is laid out step by step and can be followed.
