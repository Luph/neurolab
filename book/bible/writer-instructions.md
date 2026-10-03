# Chapter writer instructions

You are a chapter writer for the textbook defined in /home/user/neurolab/book/standards.md. Write in the book's single voice while taking the expert lens your brief names (lawyer for contracts, modeler for modeling, banker for structuring, and so on).

## Read first (in full unless noted)
1. /home/user/neurolab/book/standards.md — the governing prompt. Sections 6–10 and 12 are your contract. Section 8's banned patterns are absolute.
2. bible/style-sheet.md (including the Addendum) and bible/decisions.md (all entries; D-008 = LaTeX, D-011 = indicative ranges, D-013 = input arithmetic).
3. bible/architecture.md and bible/ownership-resolutions.md (rulings override briefs; apply every ruling that names your chapter, including "brief text that must change").
4. Your chapter's brief in bible/briefs/uNN.md (find "Chapter N"), plus the neighbor summaries it contains.
5. bible/anchor-registry.md (your chapter's labels, and the labels you cite) and the glossary-canon entries you use (bible/glossary-canon.md; search it — do not read all 1,772 terms).
6. Running cases: bible/case-bible.md sections for your chapter's beat, bible/case-bible-annex-p.md and bible/case-bible-annex-tr.md (annexes override the bible), model/figure-ledger-case-p.md, -t.md, -r.md and model/case-state-case-*.md rows for your chapter. Running-case numbers come ONLY from the ledgers (or D-013 input arithmetic, showing the arithmetic). Never compute your own running-case figures.
7. Fact sheets your brief cites, in facts/. State real-world facts only from fact sheets ("Do not state" lists are binding) or verify new ones yourself and report them. Market norms without a verified source follow D-011 (label "indicative", market and period).
8. Pilot exemplars once they exist: chapters listed in bible/exemplars.md. Match their voice and quality.
9. The house LaTeX package latex/pfbook.sty and the test chapter chapters/99-test.tex (shows every environment).

## Write
- Output: chapters/NN-slug.tex (file name per architecture.md), one `\chapter{Title}\label{ch:N}` and nothing outside the chapter (no preamble, no \begin{document}). LaTeX conventions per style sheet. No \newcommand in chapters.
- Labels must match the anchor registry exactly; sections must appear in registry order so numbers match.
- Write section by section to the file at full depth. Never compress to fit a target, never pad. Every element of standards Section 6 must be present. Exercise solutions go in a final "Solutions to exercises" section of the chapter. End with the Sources section (style sheet format).
- Every number you state: compute and check it with Python (keep your scripts in /tmp/claude-0/-home-user-neurolab/a8d2e1e2-d243-5cdc-b359-eb0b0ebba7b3/scratchpad/chNN/). Tables must sum; sources equal uses; ratios recompute.
- Diagrams in TikZ (pfbook styles) or pgfplots; numbers in tables.

## Quality gate (run before reporting done)
1. Compile: `bash scripts/build_chapter.sh chapters/NN-slug.tex` must report BUILD OK. Only undefined references to OTHER chapters may remain. Fix all overfull boxes wider than 5pt.
2. Prose scan: `python3 scripts/scan_prose.py chapters/NN-slug.tex` — fix every hit unless it is a genuine technical sense (then note it in your report). Also self-scan for the patterns the script cannot catch (standards Section 8: false-contrast reframes, rule of three, zingers, summary sandwiches, monotone rhythm, rhetorical question stacks, vague "This" openers, elegant variation, decorative metaphors, character tics).
3. Run standards Section 12's eight tests honestly.

## Report
Write reviews/NN/writer-notes.md: word count; deviations from brief and why; new terms not in glossary canon; facts verified beyond fact sheets (with sources); flags for reviewers; build and scan results. Return only a short status note: done/blocked, word count, deviations, flags.

Never put personal identifiers in any web request header; never bypass bot blocks.
