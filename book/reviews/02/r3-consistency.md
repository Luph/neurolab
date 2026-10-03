# Chapter 2 review, round 3: consistency

File: `chapters/02-what-project-finance-is.tex` (commit 0f841cf, the round-2 revision). Checked against the round-2 report, `bible/anchor-registry.md`, `bible/briefs/u01.md` (Chapter 2 section), `bible/briefs/u17.md` (Chapter 85), `bible/decisions.md` (D-140) and the Case Bible. All lines changed since round 2 were re-read (`git diff 5237fb6 HEAD`).

## Verdict: FAIL

All six round-2 items are fixed, and `ssec:2.4.3` matches the registry. Two new internal inconsistencies came in with the revised board paper (walkthrough Step 2 and Exhibit 2.3), and one registry note is stale. Each needs a one-line fix.

## Build

`bash scripts/build_chapter.sh chapters/02-what-project-finance-is.tex`: BUILD OK, 53 pages. There is one overfull box, 0.27pt at source line 752 (Solution 2.9 `align*`). It is under the 5pt limit, so no action is needed. The only undefined references are cross-chapter ones. No errors.

Scripted checks on the current file:
- All 93 distinct `\cref` targets resolve in the registry.
- Every section and subsection title matches its registry caption.
- Every example, exhibit and clause caption matches its registry row.
- The new in-text citations (Bazalgette Tunnel Limited 2026, France 2022, PIMCO Variable Insurance Trust 2025, *Prest v Petrodel Resources Ltd* 2013) each resolve to one Sources entry.
- The Sources list is in alphabetical order.

## Round-2 items

| R2 | Status |
|---|---|
| 1 Mariama Talmé's role | Fixed. Line 471 reads "the Dabakro family conglomerate whose deputy chief executive, Mariama Talmé", which matches the Case Bible character sheet |
| 2 Tense of the Kilnworth sell-down | Fixed. Line 299 reads "did when it sold part of its stake in 2026 (\cref{ch:66})" |
| 3 "about" before sourced figures | Fixed. Line 5 reads "Approximately USD~3.8 billion" and line 310 reads "approximately 67\%" |
| 4 DSRA and ECAs used once | Fixed. Both parentheticals are deleted, and neither abbreviation appears in the chapter |
| 5 "the operator's" | Fixed. It now reads "the O\&M operator's solvency" |
| 6 u01 Chapter 2 brief, and the Chapter 85 citation | Fixed. The brief's §2.4 table of contents, §2.6 example list (now ex:2.3 / ex:2.1 / ex:2.2 by content), §2.7 artifact and steps, §2.8 framework lines, Exercise 2.8 answer (151.9 before and after) and §2.14 anchor table all match the registry, and a header note cites the print-order renumbering. The brief's `fw:pf-fit-test` text matches the chapter's framework box verbatim, including question 2, and cites D-140. u17 line 73 (Chapter 85) cites `fw:pf-fit-test` with the same question-2 wording and does not restate the test |

The `ssec:2.4.3` title in the chapter (line 225) is "Reserve-based lending compared with project finance". It matches the registry (line 317) and the brief (§2.4 and §2.14).

## Defects

1. **Step 2 calls USD 29.2 million "the most the headroom allows", but Solution 2.7 gives the largest cap as USD 30.4 million (sec:2.8, line 430).** The text reads: "Even a cap of USD~29.2 million, the most the headroom allows, would leave USD~1.2 million to spare after a full call". Solution 2.7 (line 723) and Example 2.3 give the largest cap that keeps GLA within the covenant as USD 30.4 million (7.8% of cost). Solution 2.7 then rounds the cap down to 7.5% (line 732). Required fix: "Even a cap of USD~29.2 million, 7.5\% of cost and just inside the USD~30.4 million the headroom allows, would leave USD~1.2 million to spare after a full call".

2. **Exhibit 2.3 mixes two bases in one column (lines 448 to 454, 466).** The leverage rows show 3.33x during construction and after COD, which is the figure *without* the dividend restraint. The next two rows are labeled "with dividend restraint". Row 5 gives 3.31x after a full call, and row 6 gives "10.0% before a call", a fall that holds only at the restrained 3.15x (608.0 − 33.6 = 574.4; 574.4 / 182.4 = 3.15x; 1 − 574.4 / (3.50 × 182.4) = 10.0%). A reader cannot get from 3.33x to a 10.0% cushion. Required fix: change the construction cell to "3.33 (3.15 with dividend restraint)". Also either show the same pair in the after-COD cell, or extend the note to say whether the retained USD 33.6 million is assumed still held after COD. As written, the note says only that no project dividends are assumed in the first year after COD.

3. **The registry note for `ssec:2.4.3` is stale (coordinator; not a chapter edit).** `bible/anchor-registry.md` line 317 carries the Note "retitled in Ch 2 round 1 revision (line edit: sibling headings)". The title has since been restored to the original caption. Required fix: clear the Note, or change it to "title restored in Ch 2 round 2 revision", so that no one goes looking for a retitle.

## Other new material checked (no action)

- Walkthrough Steps 1, 4 and 6, the drill (line 572) and Solution 2.7 (line 732) all use the restructured figures consistently: standby facility 29.2 committed and 25.3 drawn; USD 321.4 million committed in all; dividend of 67.2 halved to retain 33.6; 3.31x after a full call; 5.5% cushion.
- New real-case material (Thames Tideway as a whole-business-style financing; the PIMCO filing for Hyperion; *Prest v Petrodel*; Code de commerce L621-2) is cited author-date with matching Sources entries. Fact-checking the content is left to the facts reviewer.
- Inside the Case P scene, Tomasz now says "PPP unit", lowercase, which matches the canon spelling and the narration at line 470.
