# Decisions log

Format: D-NNN | date | phase | decision | reason

- D-001 | 2026-10-03 | Setup | Workspace placed at `book/` inside the session repository (luph/neurolab, branch claude/new-session-om8qqc); work committed and pushed at each phase boundary so the ephemeral container cannot lose it. | Only writable, persistent location available.
- D-002 | 2026-10-03 | Setup | Orchestration runs through the Workflow tool (several concurrent workflows) plus background Agent calls; all agents inherit the session's most capable model. Per-workflow concurrency is capped by the 4-CPU container, so waves run as multiple concurrent workflows. | Environment constraint.
- D-003 | 2026-10-03 | P1 | 88 chapters in 18 Parts, plus matter files 00 and 89–94 (see architecture.md). Sector deep dives grouped into 15 chapters; modeling course is 7 chapters built on Case P. | Teaching sequence: deal-in-miniature first, foundations, risk, contracts, capital, structuring, modeling, equity, diligence, documents, process, PPP, international, life cycle, accounting/tax/regulation, sectors, sustainability, craft and frontier.
- D-004 | 2026-10-03 | P1 | Primary case technology: gas-fired CCGT with domestic gas supply chain. | Exercises fuel supply, take-or-pay, heat-rate pass-through, capacity+energy tariff, LTSA, ECA cover on turbines, currency and offtaker risk — widest concept coverage.
- D-005 | 2026-10-03 | P1 | PPP case: user-pay toll road in a fictional common-law OECD jurisdiction, ending in distress and restructuring rather than refinancing (Case P and Case R carry refinancing). | Coverage map requires demand risk; restructuring gives Part XIV a PPP storyline.
- D-006 | 2026-10-03 | P1 | American English; USD millions one decimal as base format; Excel as modeling platform; Python mirror as computational source of truth with Excel workbook verified against it. | Prompt Section 10; reproducibility.
- D-007 | 2026-10-03 | P1 | All running-case institutions (banks, ECA, DFI, contractors, utilities) are fictional; real institutions (IFC, MIGA, OECD, ICSID) appear only in real-world facts and teaching, never as running-case parties. | Avoids inventing facts about real organizations.

## Change requests
