# Pilot exemplars

Both pilot chapters passed the full six-reviewer cycle plus a final verification (2026-10-03). Every writer reads both before drafting and matches their voice, depth, apparatus and LaTeX usage.

| Chapter | File | Shows | Verification |
|---|---|---|---|
| 2 | chapters/02-what-project-finance-is.tex | Conceptual chapter: real cases from fact sheets, Case P introduction, frameworks, clause variants, novice glossing, exercises and solutions, sources | reviews/02/final-verification.md |
| 36 | chapters/36-sizing-and-sculpting-debt.tex | Technical chapter: equations, worked examples recomputed in Python, ledger-sourced Case P exhibits, Excel build-along (`excel` env, cell references), rounding notes, scenes | reviews/36/final-verification.md |

What the review rounds caught most often (check your draft for each before reporting):
1. Terms used before their home chapter without a one-clause gloss; abbreviations not expanded at first use in the chapter.
2. Running-case numbers not matching the ledger at stated rounding; double rounding in derived table cells; missing rounding notes where rounded parts do not sum to the rounded total.
3. Real-world claims generalized beyond what the fact sheet supports (e.g. one market's practice stated as universal).
4. Spreadsheet layouts that collide (two blocks on the same rows) or solutions that use a different layout from the body.
5. Case characters used before they are introduced by role; "borrower" where the canon says "project company".
6. Line-level tics: "in our experience", orphaned sentences left by edits, paragraphs that do not open with their claim, labels over 25 words.
7. Brief text that is out of date: per D-140 the ledger and Bible win; report the conflict in writer-notes.
