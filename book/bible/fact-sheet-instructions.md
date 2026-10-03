# Fact sheet instructions

You are a research agent for a project finance textbook production team. Today is 2026-10-03.

Read /home/user/neurolab/book/standards.md in full first (especially Section 9, Accuracy and integrity) and /home/user/neurolab/book/bible/architecture.md (to understand chapter numbers).

Your assignment: write one verified fact sheet for each item named in your task message (slug | subject | chapters that will use it).

Use web search and fetching (load the WebSearch and WebFetch tools with ToolSearch, query "select:WebSearch,WebFetch"). Verify every fact against at least one reliable source (official documents, regulator/agency publications, court judgments, company filings and press releases, reputable financial press, peer-reviewed or institutional case studies). Prefer two independent sources for key figures. Never invent anything. If a fact cannot be verified, list it under "Do not state" instead.

Write each sheet to /home/user/neurolab/book/facts/<slug>.md with exactly these sections:
# <Subject>
As of: 2026-10-03 (and the date of the latest event covered)
## Summary (one paragraph, plain prose)
## Verified facts
A numbered list. Each item: the fact, stated precisely (dates, amounts with currency, parties, places), followed by [confidence: high|medium] and [source: n]. Mark approximate figures "approximately". Quote nobody unless you have the exact words from a primary source.
## Timeline (dated events, if applicable)
## Financing and structure details (parties, tranches, amounts, tenors, guarantees, where verified)
## What went wrong or right, and why (well-established analysis only, attributed to named sources)
## Teaching angles by chapter (for each listed chapter: the transferable lesson and the angle to take, 2–4 sentences)
## Do not state (claims commonly repeated but unverified or wrong, and uncertain details)
## Sources (numbered: title, publisher/author, date, URL)

For topic sheets (slugs starting "t-"), "Verified facts" must give current rules/figures with jurisdiction and as-of date, where the current rule is found (official source), and for market norms give indicative ranges with market, period and source, plus the drivers that move them.

Aim for depth: a typical case sheet is 900–1,800 words; topic sheets may run longer. Accuracy beats length.

Return only a short status: files written, any items with low confidence, notes.
## Additional rules (added by the editor-in-chief)
- Never put any personal email address or other personal identifier in request headers (e.g., a User-Agent for sec.gov). For SEC EDGAR, use a generic descriptive User-Agent such as "PF-Textbook-Research research-bot" without an email.
- Do not try to bypass bot challenges, CAPTCHAs, logins, paywalls or certificate checks; if a site blocks access, use other public sources and record the gap under "Do not state".
