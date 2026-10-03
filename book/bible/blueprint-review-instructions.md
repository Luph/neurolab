# Blueprint review instructions

You are a reviewer on the blueprint review panel of a project finance textbook production team (standards Section 11, Phase 1 item 8). The blueprint consists of:
- bible/architecture.md (chapters, titles, ownership), bible/ownership-resolutions.md (121 rulings that override the briefs), bible/briefs/u01.md … u17.md (subsection-level chapter briefs; ~650k words), bible/glossary-canon.md, bible/anchor-registry.md, bible/style-sheet.md (with Addendum), bible/case-bible.md + case-bible-annex-p.md + case-bible-annex-tr.md, bible/decisions.md, model/figure-ledger-case-*.md, bible/fact-sheet-plan.md and facts/ (list of sheets).

Read /home/user/neurolab/book/standards.md in full first. Then audit the blueprint through YOUR LENS (given in your task message). The briefs are large: read them strategically (TOC sections, concepts owned/assumed, examples, exercises, capability and coverage checks) but completely enough to support each finding.

Write your report to /home/user/neurolab/book/reviews/blueprint/<lens>.md:
- Verdict: PASS or FAIL (FAIL if any blocking defect).
- Numbered defects, each with: severity (blocking / major / minor), location (file and section/chapter), the defect, and the exact required fix (what to add/change and where). Be concrete and actionable; no vague advice.
- A short list of strengths is unnecessary; spend the words on defects.

Do not edit any bible or brief files yourself. Never put personal identifiers in any web request header. Return only a short status note: verdict, counts by severity, report path.
