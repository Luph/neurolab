# Style sheet

Binding on every writer, reviewer, and editor. The book is authored in LaTeX and compiled to PDF with LuaLaTeX and the house package `latex/pfbook.sty` (decision D-008). Where this sheet and `standards.md` differ, `standards.md` wins, except that D-008 replaces the Markdown and Mermaid conventions of `standards.md` Section 10. Every choice below is final; do not reopen one inside a chapter.

Text this sheet quotes as an example of what not to write is marked **[BAD]**; text marked **[GOOD]** is a model to imitate. All figures in this sheet (delay days, DSCR ranges, dates, amounts) illustrate format only. They are not Case Bible figures or verified market data, and no writer may cite them. LaTeX source is shown in code blocks exactly as it goes in the chapter file.

## 1. Voice

### 1.1 The brilliant senior colleague

Write as the most capable person on the deal team, explaining something to a sharp new colleague at the end of a long day: direct, specific, warm, and willing to say what is hard or unresolved. The reader is a future peer. Never lecture, reassure, or flatter.

- Lead with the case, the number, or the scene, then state the general rule. A paragraph that opens with an abstraction reaches a concrete instance within two sentences.
- Every rule comes with its mechanism: what problem it solves, what breaks without it, and who pushed for it.
- Use "you" for the reader acting in a role ("You are the facility agent, and the project company's compliance certificate is three days late"). Use "we" only for shared calculation steps ("we discount at 8.5%"). Never use "I".
- Wry is allowed once or twice a chapter, when the humor carries information. A joke that could appear in any book is cut.
- When practitioners disagree, give both positions, then say which one this book favors and why (`standards.md` Section 9).
- Market norms are always dated and placed: "In 2025--2026 European bank deals for contracted onshore wind, minimum DSCRs on P90 sat at roughly 1.20x to 1.25x." Never state a bare norm.

### 1.2 The four lenses in prose

Every major topic is seen from the sponsor, the lender, the host government, and the contractor or operator. Do not render this as a four-item list after every concept. Show it in prose through what each party needs, fears, and will trade, and let the lenses collide.

**[GOOD]** "The sponsor wants delay liquidated damages capped at 15% of the contract price so the EPC contractor's bid stays low. The lenders want the cap high enough to pay interest through the full delay the independent engineer thinks plausible, which on this project is 210 days, or about USD 38.4 million. The EPC contractor will accept a higher cap only if the price rises to cover it. The host government, which guarantees the offtaker's payments, ignores the cap until a delay pushes first power past the winter peak, at which point it becomes the government's problem in parliament."

**[BAD]** "From the sponsor's perspective, the cap matters. From the lender's perspective, it also matters. The government and the contractor also have views."

A chapter passes the lens test when a reader can answer, for each major concept, "who loses money if this goes wrong, and what did they ask for in advance to prevent it?"

### 1.3 Running-case scenes

Running-case installments are scenes, not dramatized lectures. People interrupt, posture, bluff, misread each other, concede badly, and are sometimes wrong; the narration or a later section shows who was wrong and why. No character delivers a paragraph of exposition, no one says "As you know," and no scene ends on a spoken or narrated moral. Physical detail appears only if it changes the outcome (the term sheet printed without the latest markup; the ECA representative on a train who keeps dropping off the call). Characters come only from the Case Bible. Dialogue goes inside a `casescene` box (Section 4.6); narration that teaches goes outside it.

**[BAD]** (mouthpiece speech)

> "As you know," said the lead arranger, "lenders size debt on P90 because the P50 is only a median estimate, and if production falls below it in any given year, the debt service coverage ratio could drop below the lock-up threshold, which would harm both lenders and sponsors. That is why we must insist on P90." The developer nodded thoughtfully. "That makes perfect sense."

**[GOOD]** (scene with friction, as LaTeX source)

```latex
\begin{casescene}{Case R}{Arranger's offices, February 2027}
``One-point-three-five on P50,'' the developer said. ``That's what Brightmoor got last quarter.''

``Brightmoor has a ten-year operating record. You have a met mast and a consultant's report.'' The arranger didn't look up from the sizing printout. ``We're at one-point-two on the one-year P90.''

``That's eleven million less debt.''

``Twelve-point-four. I checked.''

The developer's counsel cut in. ``If we take the P90 case, we want the lock-up at one-point-oh-five, not one-ten.''

``Different conversation.''
\end{casescene}

It was the same conversation: the lock-up level and the sizing case are two dials
on the same risk, and \cref{sec:37.4} shows how lenders set them together.
```

The paragraph after the box is narration that explains a mechanism and points to where it is taught. It does not moralize. Number words in dialogue are spelled as people say them; the narration states the figure in numerals if the reader needs it.

## 2. Spelling, usage, and numbers

Each rule gives the printed form and, where it differs, the LaTeX source.

### 2.1 American English

American spelling throughout prose: modeling, labor, program, center, defense, license (noun and verb), analyze, organization, judgment, fulfill, aging, sulfur, gray, catalog, enroll. Exceptions: proper names (Thames Tideway Tunnel, Ministry of Defence), titles of sources, and drafted clauses governed by English law, which may use British forms ("Utilisation Request") because such documents are drafted that way. Write "financial close" (not "financial closing") and "per year" (not "per annum" outside clauses).

Serial (Oxford) comma always: "the sponsor, the lenders, and the offtaker." Double quotation marks, typed ` ``like this'' `; single quotation marks inside double, typed `` `like this' ``. Periods and commas go inside closing quotation marks.

Hyphenate compound modifiers before a noun when needed for sense (a 20-year PPA, a fixed-price contract), never after it (the PPA runs for 20 years). Never stack more than two hyphenated compound modifiers in one noun phrase.

### 2.2 Dates and periods

- Prose dates: October 3, 2026. Month and year only: October 2026.
- Table cells and timeline exhibits: ISO format 2026-10-03, or "Q3 2027" where the period is the point.
- Ranges use an en dash, typed `--`, with no spaces: `2019--2023`, `pages 45--67`, `1.20x--1.25x` is not used (write "1.20x to 1.25x" for ratio ranges in prose).
- Project time: the first full year of operation is Operating Year 1 in prose and OY1 in tables. Construction months are Month 1 to Month 34, counted from notice to proceed.
- Calendar periods: Q3 2027, H1 2028. Fiscal years: FY2027, and the chapter states once when the fiscal year ends.
- Model periods are named by their end date: "the period ending June 30, 2028."

### 2.3 Numbers

- Spell out one to nine in prose; use numerals for 10 and above. Always use numerals with units, money, percentages, ratios, multiples, cross-referenced numbers, years, and model periods.
- Never begin a sentence with a numeral; rewrite the sentence.
- Thousands separator is a comma: 12,450 hours. Inside math, protect the comma: `$1{,}055.06$`.
- Write "million" and "billion" in prose, never "mn", "mm", "bn", or "MM" (except in the unit MMBtu).
- In dialogue, write numbers as spoken ("one-point-two").
- Approximate real-world figures carry "approximately" (Section 9). Illustrative figures look like real data: USD 412.6 million, not USD 400 million.

### 2.4 Money

| Printed | LaTeX source | Rule |
|---|---|---|
| USD 412.6 million | `\USDm{412.6}` | Default for millions, one decimal |
| USD 1.2 billion | `USD~1.2~billion` | Only above USD 1,000 million when precision is not the point |
| USD 45,000 | `USD~45,000` | Amounts below one million |
| USD 52.40/MWh | `USD~52.40/MWh` | Unit prices: two decimals |
| KDR 9,860.0 million | `KDR~9,860.0~million` | Fictional currency, code from the Case Bible |
| KDR 129.05 per USD | `KDR~129.05 per USD` | Exchange rate in prose; header "KDR/USD" |

No currency symbols anywhere ($, €, £ are banned as currency markers; € may appear inside a name such as €STR). Table headers carry the unit "USD m" and cells hold bare numbers. Fictional currency codes are three letters assigned by the Case Bible and never an existing ISO 4217 code. Every local-currency figure that matters appears once per example with its USD equivalent and the rate used. State real or nominal once per example: "USD 52.40/MWh in 2026 real terms."

### 2.5 Percentages, rates, basis points, multiples, ratios

| Printed | LaTeX source | Rule |
|---|---|---|
| 8.5% | `8.5\%` | No space. "Percentage points" (written out) for differences |
| SOFR 4.31% | `SOFR 4.31\%` | Interest rates two decimals; returns one decimal (13.8%) |
| 175 bps | `175\bps` | Margins, fees, spreads, rate changes; `\bps` supplies the thin space. Before a word write `175\bps{} over`, because the macro swallows the next space |
| 1.35x | `1.35\x` | DSCR, LLCR, PLCR, net debt to EBITDA, money multiples; always two decimals. Before a word write `1.35\x{} on` |
| 75.0% / 75% | `75.0\%` | Gearing: one decimal in tables, none in prose when round |
| 75:25 | `75:25` | Debt-to-equity split |
| P90 | `P90` | No space or hyphen; state "one-year" or "ten-year" when it matters |

### 2.6 Units

A non-breaking space joins numeral and unit: `650~MW`, `4,725~GWh`, `7,150~kJ/kWh`, `28~km`, `120,000~bbl/d`, `4.5~mtpa`, `110~kV`.

- Capacity in MW or GW; energy in kWh, MWh, GWh, or TWh. Never "MW per hour".
- Price per unit: code, slash, unit: USD/MWh, USD/MMBtu, USD/kW-month, USD/t.
- Heat rate in kJ/kWh (net, LHV unless stated).
- Gas: MMBtu for energy, MMscfd for flow, bcm for annual volume; LNG in mtpa. Oil: bbl and bbl/d. Mining: t, Mt, g/t.
- Traffic: vehicles per day (vpd after first use); AADT for annual average daily traffic.

### 2.7 Signs

- Tables: negatives in parentheses, (12.4). Nil is an en dash `--` in financial tables, 0.0 where a zero result is being checked.
- Prose and formulas: a true minus in math mode, `$-12.4$`; prefer words in prose ("an outflow of USD 12.4 million").
- Model convention: costs and outflows are stored as positive numbers on calculation sheets and subtracted explicitly; cash flow statements and the waterfall display outflows in parentheses. Chapter 39 states this once; others cross-reference it.

## 3. Structure, labels, and cross-references

### 3.1 Chapter file and headings

One file per chapter, `chapters/NN-slug.tex`, containing exactly one `\chapter`. No preamble, no `\documentclass`, no `\begin{document}`. Part openers are handled by the build (`latex/parts.tex`); chapters never contain `\part`.

All headings are sentence case, with no dashes and no terminal period. Every numbered heading carries a label whose number matches the printed number.

```latex
\chapter{Sizing and sculpting debt}\label{ch:36}
\section{Sizing debt to a minimum DSCR}\label{sec:36.3}
\subsection{Sculpting to a target ratio}\label{ssec:36.3.2}
```

Do not go below `\subsection` for numbered structure. `\subsection*` is used only for the fixed element subheadings listed in Section 4. Headings name their content plainly: "Sizing debt to a minimum DSCR," never "The art of debt sizing." Never put `\xl`, `\cref`, `\term`, or math in a heading.

### 3.2 Label scheme

| Object | Environment or command | Label | Printed as |
|---|---|---|---|
| Chapter | `\chapter` | `ch:36` | Chapter 36 |
| Section | `\section` | `sec:36.3` | Section 36.3 |
| Subsection | `\subsection` | `ssec:36.3.2` | Section 36.3.2 |
| Example | `example` | `ex:36.4` | Example 36.4 |
| Exhibit (table, diagram, chart) | `exhibit` or `longtable` | `exh:36.2` | Exhibit 36.2 |
| Clause | `clause` | `cl:18.3` | Clause 18.3 |
| Clause variant | `clausevariant` | `cl:18.3a` | Clause 18.3a |
| Exercise | `exercise` | `exr:36.11` | Exercise 36.11 |
| Equation | `equation` | `eq:35.1` | Equation (35.1) |
| Framework | `framework` | `[label={fw:who-pays-if}]` | Framework 28.2 |

`K` in each label is the printed sequence number in that chapter; the writer keeps them in order. Framework labels use a short slug from the anchor registry. Place `\label` immediately after the `\caption`, the `\begin{...}{title}` line, or the heading it belongs to.

### 3.3 Status labels

Every example, exhibit, and clause carries exactly one status label, placed at the end of its title or caption argument:

| Status | LaTeX | Printed |
|---|---|---|
| Invented material outside the running cases | `\illustrative` | (Illustrative) |
| Running-case material from the Case Bible | `\casep`, `\caset`, `\caser` | (Case P) |
| Real deal, from a fact sheet | `\realcase{Paiton I, 1999--2002}` | (Real case: Paiton I, 1999–2002) |

```latex
\begin{example}{Sizing one semiannual period \illustrative}\label{ex:36.4}
\caption{Case P sources and uses at financial close (USD m) \casep}\label{exh:40.3}
\begin{example}{The 2002 tariff renegotiation \realcase{Paiton I, 1999--2002}}\label{ex:59.2}
```

Clauses are always Illustrative and say so (Section 7). `\casep`, `\caset`, `\caser`, and `\realcase` are requested macros (Section 13).

### 3.4 Cross-references

- Always `\cref{...}`; at the start of a sentence `\Cref{...}`. Never type "Section 36.4" by hand, and never write "as discussed earlier", "as mentioned above", or "as we have seen".
- Several targets: `\cref{ex:36.1,ex:36.2}`; ranges: `\crefrange{exr:36.1}{exr:36.5}`.
- Equations print with parentheses automatically: `\cref{eq:35.1}` gives "Equation (35.1)".
- Forward references: one or two sentences, always with the destination. **[GOOD]** `\Cref{ch:37} shows how the debt service reserve is sized; here, assume it holds six months of debt service.`
- Cite only labels in the anchor registry. A cross-chapter `\cref` shows as "??" in a standalone build and is expected; any undefined label inside the chapter's own numbers is a defect. If an anchor you need is missing, report it; do not invent one.

## 4. Chapter skeleton and environments

### 4.1 Skeleton

```latex
\chapter{Sizing and sculpting debt}\label{ch:36}

% Opening: two to eight paragraphs, no heading. A real deal moment, a failure,
% a puzzle, or a running-case scene. Never announce the chapter's contents.

\section*{What you will be able to do}
\begin{itemize}
  \item Size senior debt to a minimum DSCR on a contracted cash flow (Capability 5).
  \item Sculpt a repayment profile and test it against LLCR (Capability 4).
\end{itemize}

\section{Sizing debt to a minimum DSCR}\label{sec:36.1}
% ... core teaching sections with examples, exhibits, frameworks, real cases ...
\section{Walkthrough: reading a lender's sizing printout}\label{sec:36.6}
\section{Case P: the lenders size the debt}\label{sec:36.7}
\section{Practitioner's notebook}\label{sec:36.9}
\section{Judgment drill}\label{sec:36.10}
\section{Sizing fixes the debt; the reserves decide whether it survives a bad year}\label{sec:36.11}
\section{Exercises}\label{sec:36.12}
\section{Solutions to exercises}\label{sec:36.13}
\section*{Sources}
```

Rules for each element:

- "What you will be able to do" is the only unnumbered `\section*` besides "Sources". Two to four items, each starting with a verb and ending with the capability number from `standards.md` Section 3.
- Walkthroughs: `\section{Walkthrough: ...}` naming the artifact or task. A chapter may have several.
- Real cases: the section heading names the deal and what it teaches ("Ichthys LNG and cost growth under ECA cover").
- Running case: the heading begins "Case P:", "Case T:", or "Case R:". Those three prefixes and "Walkthrough:" are the only heading forms that take a colon.
- Practitioner's notebook: `\subsection*` headings, in this order, each omitted only when the chapter has nothing for it: Checklist; Red flags; Rules of thumb and their limits; Common mistakes; Questions experts ask. Items are `itemize` (or `enumerate` for a real sequence), each a full sentence with its reason, never a bold label plus colon.
- Judgment drill: `\subsection*{The situation}` (second person, specific, with numbers and a deadline), `\subsection*{Reasoning it through}` (prose: trade-offs and the answer an expert gives), `\subsection*{What would change the answer}` (named conditions and the direction each moves the decision).
- Close: a numbered section whose heading states the open problem or the idea it crystallizes. **[BAD]** headings: "Conclusion", "Summary", "Key takeaways", "Wrapping up", "Looking ahead". The last paragraph poses a concrete problem the next chapter solves.
- No other boxes, callouts, or labels. **[BAD]** "Pro tip", "Key insight", "Remember", "Fun fact". The Source and Note lines under exhibits (Section 4.3) are the only labels of that kind.

### 4.2 Examples

```latex
\begin{example}{Sizing one semiannual period \illustrative}\label{ex:36.4}
Prose and calculations, every step shown. Equations, \xl{...} formulas, and
small tables (tabularx, no caption) are allowed inside; a captioned exhibit is not.
\end{example}
```

The title is plain and specific and ends with the status macro. The environment prints its own closing rule; do not add one.

### 4.3 Exhibits

```latex
\begin{exhibit}[H]
\caption{Case P debt sizing on the banking case (USD m) \casep}\label{exh:36.2}
\small
\begin{tabularx}{\linewidth}{@{}L rrrr@{}}
\toprule
Item & OY1 & OY2 & OY3 & OY4\\
\midrule
CFADS & 61.4 & 63.0 & 62.2 & 64.9\\
Debt service & (45.5) & (46.7) & (46.1) & (48.1)\\
\midrule
DSCR (x) & 1.35 & 1.35 & 1.35 & 1.35\\
\bottomrule
\end{tabularx}
\exhibitsource{Case P reference model, banking case (Chapter 36 state).}
\exhibitnote{Figures may not sum because of rounding.}
\end{exhibit}
```

- Always `[H]`. Caption on top (the package places it), in the form "title (unit) status". The caption is a noun phrase without a final period.
- `\exhibitsource{...}` is required on every exhibit; `\exhibitnote{...}` only when needed. Use "Figures may not sum because of rounding" only when that is true and a check line shows the difference. Both are requested macros (Section 13).
- Diagrams and charts go in the same `exhibit` float with `\centering` before the `tikzpicture`.

### 4.4 Clauses

Covered in Section 7.

### 4.5 Frameworks

```latex
\begin{framework}[label={fw:who-pays-if}]{Who pays if\ldots? trace}
Steps of the framework as an enumerate list, then one sentence on when to use it.
\end{framework}
```

Frameworks are numbered within their home chapter (Framework 28.2), which makes each number unique across the book and correct in standalone builds. The label is `fw:slug` from the anchor registry and goes in the optional argument, `[label={fw:slug}]`, not as a `\label` inside the box (a `\label` inside resolves to the enclosing section). The name is set in sentence case; the prose that first defines it uses `\term{}`. Established frameworks are credited in the prose next to the box. The current package prints "Framework: Name" without a number; the numbered version is a requested macro (Section 13). Only the home chapter uses the `framework` box; other chapters `\cref` it.

### 4.6 Running-case scenes

```latex
\begin{casescene}{Case P}{Ministry of Energy, Kesari, March 2026}
``...'' dialogue and scene narration ...
\end{casescene}
```

First argument is exactly `Case P`, `Case T`, or `Case R`; the second is place and month-year from the Case Bible. Paragraphs inside the box are separated by a blank line. Teaching narration, numbers tables, and exhibits stay outside the box. (The place name in this example is a format placeholder; use the Case Bible's.)

### 4.7 Exercises and solutions

```latex
\section{Exercises}\label{sec:36.12}
\subsection*{Tier 1: Concept checks}
\begin{exercise}\label{exr:36.1}
Question text.
\end{exercise}
\subsection*{Tier 2: Calculation and drafting}
\subsection*{Tier 3: Case problems and model tasks}

\section{Solutions to exercises}\label{sec:36.13}
\subsection*{Tier 1: Concept checks}
\begin{solution}{exr:36.1}
Answer in the first sentence, then every step, then a check.
\end{solution}
```

Exercises are numbered continuously across tiers (36.1 to 36.15), and every exercise has exactly one solution in the same order. Each Tier 3 exercise names the starting file or the Case Bible figures it uses. Each solution gives the answer first, then every step, then a reconciliation; Tier 2 and Tier 3 solutions end with the most common wrong answer and why it is wrong. Drafting solutions give a model clause in a `clause` box plus annotations.

### 4.8 Sources

```latex
\section*{Sources}
\begin{sources}
\item Asian Development Bank. 2021. \textit{Title of the Report in Title Case}. Manila: Asian Development Bank. \url{https://www.example.org/report}. Accessed October 3, 2026.
\item Surname, Given Name, and Given Name Surname. 2019. ``Article Title in Title Case.'' \textit{Journal Name} 12 (3): 45--67.
\end{sources}
```

Chicago author-date, alphabetical by author or organization. Report and book titles in `\textit{}`; article titles in quotation marks. URLs in `\url{}` (never escape characters inside `\url`). Access date required for web sources. No BibTeX. `sources` is a requested environment (Section 13). Omit the section only if the chapter states no real-world fact.

## 5. Notation and Excel

### 5.1 Mathematics

- Inline math `$...$`. Display math: `equation` with a label when the formula is built, cited, or appears in the formula sheet; `equation*` or `align*` for intermediate steps. Never `$$...$$`.
- Multi-letter variables in `\mathrm{}`: `$\mathrm{CFADS}_t$`, never `$CFADS_t$`. Time subscript is always $t$.
- Multiplication `\times`; division as `\frac{}{}` in display and `/` inline.
- No Unicode in math: write `\times`, `-`, `\le`, `\ge`, `\sigma`, `\Delta`, never ×, −, ≤, ≥, σ, Δ.
- Every display formula is followed by a sentence defining any symbol not in the canon below, then its Excel implementation.

### 5.2 Symbol canon

| Symbol (LaTeX) | Meaning | Unit |
|---|---|---|
| `t` | period index (model period, usually semiannual) | – |
| `n`; `N` | number of periods; final period of the loan | – |
| `T` | final period of the project or concession life | – |
| `r` | discount rate per period | % |
| `i` | interest rate per period on debt | % |
| `\mathrm{DF}_t` | discount factor, `(1+r)^{-t}` | – |
| `\mathrm{NPV}`, `\mathrm{IRR}` | net present value; internal rate of return | currency; % |
| `\mathrm{CF}_t` | generic cash flow | currency |
| `\mathrm{Rev}_t`, `\mathrm{Opex}_t`, `\mathrm{Capex}_t`, `\mathrm{Tax}_t` | revenue, operating costs, capital expenditure, cash tax | currency |
| `\Delta\mathrm{WC}_t` | change in working capital (increase is a use of cash) | currency |
| `\mathrm{CFADS}_t` | cash flow available for debt service | currency |
| `P_t`, `I_t` | scheduled principal; interest paid | currency |
| `\mathrm{DS}_t` | debt service, `P_t + I_t` | currency |
| `D_t` | debt outstanding at the start of period `t` | currency |
| `\mathrm{DSCR}_t`; `\mathrm{DSCR}^{*}` | debt service cover ratio; sculpting target ratio | x |
| `\mathrm{LLCR}_t`, `\mathrm{PLCR}_t` | loan life and project life cover ratios | x |
| `G`; `E` | gearing; equity amount | %; currency |
| `\mathrm{P50}`, `\mathrm{P90}`, `\mathrm{P99}` | exceedance levels | quantity |
| `\sigma` | standard deviation (state one-year or ten-year) | quantity or % |
| `A_t` | availability factor | % |
| `C` | contracted capacity | MW |
| `\mathrm{CP}_t`; `\mathrm{cpr}` | capacity payment; capacity payment rate | currency; USD/kW-month |
| `\mathrm{EP}_t` | energy payment | currency |
| `E^{\mathrm{del}}_t` | energy delivered | MWh |
| `\mathrm{HR}` | net heat rate | kJ/kWh |
| `p^{\mathrm{fuel}}_t` | fuel price | USD/MMBtu |
| `\mathrm{IF}_t` | indexation factor, `\mathrm{CPI}_t/\mathrm{CPI}_0` | – |
| `\mathrm{FX}_t` | exchange rate, local currency per USD | LCY/USD |
| `\mathrm{LD}` | liquidated damages | currency |

Core formulas, owned by their home chapters (Chapter 35 owns CFADS and the ratios, including LLCR discounting and DSRA treatment; Chapter 18 owns tariff formulas):

```latex
\begin{equation}\label{eq:35.1}
\mathrm{DSCR}_t = \frac{\mathrm{CFADS}_t}{\mathrm{DS}_t}
\end{equation}

\begin{equation*}
\mathrm{CP}_t = C \times 1{,}000 \times \mathrm{cpr} \times \mathrm{IF}_t \times A_t \times m_t
\qquad
\mathrm{EP}_t = E^{\mathrm{del}}_t \times \frac{\mathrm{HR} \times p^{\mathrm{fuel}}_t}{1{,}055.06}
\end{equation*}
```

In the tariff formulas, `m_t` is months in the period, 1,000 converts MW to kW, and 1,055.06 converts MWh multiplied by kJ/kWh into MMBtu (1 MMBtu = 1,055,056 kJ).

### 5.3 Formula, then Excel

Every formula the reader must build is followed by its Excel implementation, introduced by a sentence stating the cell layout. Short single formulas use `\xl{...}` inline; a set of rows uses the `excel` block. Formulas are written for the first timeline column and copied right.

```latex
On the Ratios sheet, CFADS sits in row 12 and debt service in row 14, with the
first operating period in column J. The DSCR for that period, in J16, is
\xl{=IF(J$8=1, J12/J14, "")}, where row 8 is the repayment flag linked from Time.
\begin{excel}
Ratios!J12   CFADS          USD m   =Waterfall!J40
Ratios!J14   Debt service   USD m   =Debt!J55+Debt!J61
Ratios!J16   DSCR           x       =IF(J$8=1, J12/J14, "")
\end{excel}
```

Content inside `excel` and `\xl{}` is verbatim: never escape `%`, `$`, `&`, or `_` there. `\xl{}` may not contain `%`, `#`, `\`, `{`, or `}`, and inside a table cell it may not contain `&`. It may not appear in headings, `\caption`, `\exhibitsource`, `\exhibitnote`, or any other command's argument; it does work in body text, inside example, clause, and casescene boxes, and in `tabularx` cells (tested). Formulas that break these limits go in an `excel` block.

### 5.4 Model conventions (FAST-consistent)

- Sheets, in this order: Cover, Inputs, Time, Construction, Operations, Tax, Funding, Debt, Reserves, Waterfall, Financials, Ratios, Returns, Checks, Outputs. Cited in prose without quotes: "the Debt sheet".
- Time runs across columns; one row, one calculation, one formula copied across the row. Columns: A--C grouping indents, D label, E units, F constants, G row total or check, H--I blank, J first model period. Case P runs monthly in construction and semiannual in operations.
- Every row has a unit in column E: USD m, MWh, %, x, flag, date, factor.
- Flags are 1 or 0, named with a "Flag" prefix: `Flag_Construction`, `Flag_Operations`, `Flag_Repayment`, `Flag_FirstOpsPeriod`. In LaTeX prose, write them with `\xl{Flag_Repayment}` (no escaping) or as "the repayment flag". Never TRUE/FALSE flags.
- Cell references: `\xl{Debt!J55}`, or "row 55 of the Debt sheet". No range names except the scenario selector `Scenario` (fixed in Chapter 13).
- Colors: inputs blue font on pale yellow fill; calculations black, no fill; links from other sheets green font; checks show 0 when passing and red fill when failing. Exhibits of sheets describe colors in words or use `\cellcolor{pfinput}` for input cells.
- Banned on calculation sheets: OFFSET, INDIRECT, merged cells, and hard-coded numbers in formulas (except 0, 1, 12, and unit conversions labeled in column E). Circularity is resolved by the method fixed in Chapter 40; earlier chapters forward-reference it.

## 6. Tables, diagrams, and charts

### 6.1 Tables

Use a table when the reader compares three or more numbers, or several items across several attributes. Two numbers belong in a sentence.

- `booktabs` rules only (`\toprule`, `\midrule`, `\bottomrule`); no vertical lines, no `\hline`, no cell shading except `pfinput` for model inputs.
- `tabularx` at `\linewidth` with `@{}` at both ends. Text columns `L` (ragged right X); number columns `r`, same decimals down a column. Do not use siunitx `S` columns.
- Units in the caption when the table shares them; otherwise in each header ("Capacity (MW)").
- Totals and subtotals sit below a `\midrule`, labeled "Total" or by what they are ("CFADS", "Total uses").
- Tables that must reconcile end with a check row ("Sources minus uses & 0.0") or a note.
- Periods run across columns when there are more than four; items down rows.
- No empty cells: `--` for nil, "n/a" for not applicable.
- Width: the text block is 5.25in. Up to six numeric columns at normal size; seven to nine with `\small` after `\caption`; 10 to 12 with `\footnotesize`; never smaller. Above 12 columns, split the table by period range into two exhibits. Landscape (`\begin{landscape}` from pdflscape, a requested package) is for full annual model printouts only.
- Tables longer than a page use `longtable` outside any float. With the requested setting (Section 13), its caption is numbered as an Exhibit:

```latex
\begin{longtable}{@{}lrrr@{}}
\caption{Case P construction drawdown schedule (USD m) \casep}\label{exh:40.5}\\
\toprule Month & EPC & Owner's costs & Total\\ \midrule \endfirsthead
\toprule Month & EPC & Owner's costs & Total\\ \midrule \endhead
\bottomrule \endlastfoot
1 & 61.9 & 3.4 & 65.3\\
\end{longtable}
\exhibitsource{Case P reference model.}
```

### 6.2 TikZ diagrams

All diagrams are TikZ inside an `exhibit` float, using only the `pfbook.sty` styles:

| Style | Use |
|---|---|
| `pfspv` | the project company (one per diagram) |
| `pfbox` | private parties, process steps, outcomes |
| `pfgov` | host government, contracting authority, regulators |
| `pflend` | lenders, agents, ECAs, DFIs |
| `pfarrow` | contracts and obligations (gray) |
| `pfflow` | money flows (blue, heavy) |
| `pflabel` | every edge label |

Rules: canonical party names (Section 8) in sentence case; edge labels name the contract or the flow; at most 15 nodes; no amounts in diagrams (they go in tables), except dates on timelines; no other colors or fills; position with the `positioning` library (`above=of`, `below left=of`), not absolute coordinates, except on timelines and charts. Every diagram must fit 5.25in; check the build log for Overfull boxes. Decision nodes are diamonds that pose a yes/no question.

All four examples below were compiled with `scripts/build_chapter.sh`.

Contract map:

```latex
\begin{exhibit}[H]
\caption{Case P contract map \casep}\label{exh:28.1}
\centering
\begin{tikzpicture}[node distance=9mm and 14mm]
\node[pfspv] (pc) {Project company};
\node[pfbox, above=of pc] (spon) {Sponsors};
\node[pflend, left=of spon] (lend) {Lenders};
\node[pfgov, right=of spon] (gov) {Host government};
\node[pfbox, below left=of pc] (epc) {EPC contractor};
\node[pfbox, below=of pc] (om) {O\&M operator};
\node[pfbox, below right=of pc] (off) {Offtaker};
\draw[pfflow] (spon) -- node[pflabel] {Equity} (pc);
\draw[pfflow] (lend) |- node[pflabel, pos=0.25] {Loans} (pc);
\draw[pfarrow] (gov) |- node[pflabel, pos=0.25] {Implementation agreement} (pc);
\draw[pfarrow] (pc) -- node[pflabel] {EPC contract} (epc);
\draw[pfarrow] (pc) -- node[pflabel] {O\&M agreement} (om);
\draw[pfarrow] (pc) -- node[pflabel] {PPA} (off);
\end{tikzpicture}
\exhibitsource{Case Bible.}
\end{exhibit}
```

Cash waterfall:

```latex
\begin{exhibit}[H]
\caption{Operating cash waterfall \illustrative}\label{exh:52.3}
\centering
\begin{tikzpicture}[node distance=4mm, every node/.style={text width=58mm}]
\node[pfspv] (rev) {Revenue account};
\node[pfbox, below=of rev] (s1) {1. Operating costs and taxes};
\node[pfbox, below=of s1] (s2) {2. Senior interest and fees};
\node[pfbox, below=of s2] (s3) {3. Senior principal};
\node[pfbox, below=of s3] (s4) {4. DSRA top-up};
\node[pfbox, below=of s4] (s5) {5. Distribution test};
\node[pfbox, below=of s5] (s6) {6. Distributions to sponsors};
\foreach \a/\b in {rev/s1,s1/s2,s2/s3,s3/s4,s4/s5,s5/s6} \draw[pfflow] (\a) -- (\b);
\end{tikzpicture}
\exhibitsource{Illustrative.}
\end{exhibit}
```

Timeline (one year is 4 units of 5 mm; bars are quarters):

```latex
\begin{exhibit}[H]
\caption{Development to commercial operation \casep}\label{exh:4.2}
\centering
\begin{tikzpicture}[x=5mm, y=7mm, font=\small\sffamily]
\foreach \yr [count=\i from 0] in {2026,2027,2028,2029,2030} {
  \draw[pfgray] (\i*4,0.3) -- (\i*4,-3.6);
  \node[anchor=south] at (\i*4+2,0.3) {\yr};
}
\draw[pfgray] (20,0.3) -- (20,-3.6);
\fill[pfblue!25] (0,-0.9) rectangle (3.6,-0.3);  \node[anchor=east] at (0,-0.6) {Tender};
\fill[pfblue!25] (3,-1.9) rectangle (6,-1.3);    \node[anchor=east] at (0,-1.6) {Financing};
\fill[pfblue!50] (6,-2.9) rectangle (17,-2.3);   \node[anchor=east] at (0,-2.6) {Construction};
\node[diamond, fill=pfblue, inner sep=2pt] at (6,-3.4) {};
\node[anchor=west, font=\scriptsize\sffamily] at (6.2,-3.4) {Financial close};
\end{tikzpicture}
\exhibitsource{Case Bible.}
\end{exhibit}
```

Decision tree:

```latex
\begin{exhibit}[H]
\caption{Choosing payment security \illustrative}\label{exh:59.4}
\centering
\begin{tikzpicture}[node distance=7mm and 6mm,
  dec/.style={pfbox, diamond, aspect=2.4, inner sep=1pt, text width=26mm}]
\node[dec] (q1) {Offtaker investment grade?};
\node[pfbox, below left=of q1, text width=30mm] (a1) {One-month letter of credit};
\node[dec, below right=of q1] (q2) {Sovereign guarantee available?};
\node[pfbox, below left=of q2, text width=28mm] (a2) {Guarantee plus three-month LC};
\node[pfbox, below right=of q2, text width=28mm] (a3) {DFI partial risk guarantee};
\draw[pfarrow] (q1) -| node[pflabel, pos=0.25] {Yes} (a1);
\draw[pfarrow] (q1) -| node[pflabel, pos=0.25] {No} (q2);
\draw[pfarrow] (q2) -| node[pflabel, pos=0.25] {Yes} (a2);
\draw[pfarrow] (q2) -| node[pflabel, pos=0.25] {No} (a3);
\end{tikzpicture}
\exhibitsource{Illustrative.}
\end{exhibit}
```

Timeline dates in a real exhibit must match the Case Bible; the dates above are format examples only.

### 6.3 Charts (pgfplots)

Charts show shape (ratio profiles, debt balances, price curves); the numbers behind a chart also appear in a table or the text. Inside `exhibit`, `width=\linewidth`, `height=55mm`; axis labels with units ("USD m", "x"); `xtick=data` for period axes; legend below the plot; fills `pfblue!60` and `SeaGreen!50` for the first two series, `pfgray` for a third; at most four series.

```latex
\begin{tikzpicture}
\begin{axis}[width=\linewidth, height=55mm, ybar, bar width=8pt, xtick=data,
  enlarge x limits=0.15, xlabel={Operating year}, ylabel={USD m}, ymin=0,
  legend style={font=\scriptsize, at={(0.5,-0.3)}, anchor=north, legend columns=2},
  tick label style={font=\scriptsize}, label style={font=\small}]
\addplot[fill=pfblue!60] coordinates {(1,13.8) (2,14.1) (3,14.0) (4,13.6)};
\addplot[fill=SeaGreen!50] coordinates {(1,10.6) (2,10.6) (3,10.6) (4,10.6)};
\legend{CFADS, Debt service}
\end{axis}
\end{tikzpicture}
```

## 7. Drafted clause excerpts

All clause language is drafted originally for this book. Never reproduce or closely paraphrase LMA, LSTA, APLMA, FIDIC, ISDA, government standard forms, textbooks, or published contracts. A writer who recognizes a published formulation in a draft rewrites it from the principle.

A single clause:

```latex
\begin{clause}{Delay liquidated damages, EPC contract \illustrative}\label{cl:22.2}
\begin{enumerate}[label=(\alph*)]
\item If Completion has not occurred by the Guaranteed Completion Date, the Contractor
      shall pay Delay Liquidated Damages at the Daily Rate for each day of delay.
\item The aggregate Delay Liquidated Damages shall not exceed 20 per cent of the Contract Price.
\end{enumerate}
\end{clause}
\begin{enumerate}
\item Paragraph (a). What the words do, who they protect, what a party would push to change.
\item Paragraph (b). ...
\end{enumerate}
```

- The title names the provision and the document, then `\illustrative`.
- Paragraphs inside are lettered (a), (b) with `enumerate[label=(\alph*)]`, sub-paragraphs (i), (ii) with `label=(\roman*)`. Defined terms inside clauses are capitalized as in real drafting; "per cent" and English-law spellings are permitted inside clauses governed by English law. `%` in a clause is written `\%`.
- Annotations follow the box at once as a plain `enumerate`, one item per lettered paragraph, beginning "Paragraph (a)." and running one to four sentences. Every paragraph is annotated.

Negotiated variants (sponsor-friendly, lender-friendly, government-friendly) share one number and take letters:

```latex
\begin{clausevariants}\label{cl:18.3}
\begin{clausevariant}{Deemed energy, PPA}{Illustrative, sponsor-friendly}\label{cl:18.3a}
\begin{enumerate}[label=(\alph*)]
\item If the Seller is able and offers to deliver Net Energy Output and the Buyer fails
      to accept it for any reason other than Seller Fault, the Buyer shall pay for
      Deemed Energy as if it had been delivered.
\end{enumerate}
\end{clausevariant}
% annotations for 18.3a
\begin{clausevariant}{Deemed energy, PPA}{Illustrative, lender-friendly}\label{cl:18.3b}
...
\end{clausevariant}
% annotations for 18.3b
\begin{clausevariant}{Deemed energy, PPA}{Illustrative, government-friendly}\label{cl:18.3c}
...
\end{clausevariant}
% annotations for 18.3c
\end{clausevariants}
```

Letters are fixed: a is sponsor-friendly, b lender-friendly, c government-friendly (for a contract with no government party, c is the counterparty-friendly variant, named in the second argument, e.g. "Illustrative, offtaker-friendly"). Immediately after `\end{clausevariants}`, an ordinary prose paragraph with no label states where the clause usually lands, with market and date ("In Sub-Saharan African IPPs closed 2018--2025, the compromise was..."). `clausevariants` and `clausevariant` are requested environments (Section 13).

## 8. Defined terms and canonical names

### 8.1 Bold at first definition only

A term is bold once in the book, at its home definition (the section that owns it per `architecture.md`), using `\term{...}`. Bold appears nowhere else; `\textbf` is banned in chapters. Acronyms: the full term, then the acronym in parentheses: `\term{debt service cover ratio} (DSCR)`. At the first use in each later chapter, write the full term once again (not bold) with the acronym, then use the acronym. Exempt from re-expansion: currency codes, MW, MWh, GWh, kWh, and Case P, Case T, Case R. Do not create an acronym used fewer than three times in a chapter. `\emph{}` is for the rare word that carries spoken stress, and for foreign words; never for emphasis in sequence.

Common nouns that are defined terms stay lowercase in prose ("project company", "financial close", "commercial operation date"). Capitalized forms appear only inside clauses.

### 8.2 Canonical forms

| Canonical form | Acronym | Not |
|---|---|---|
| project company | – | SPV, vehicle, entity, borrower, ProjectCo (SPV only when discussing the legal form itself, Chapter 2) |
| sponsor, sponsors | – | developer (except the developer character or a pure developer company), shareholder (except in shareholder-agreement context) |
| lenders | – | banks (unless only banks), financiers, creditors (except in insolvency) |
| senior lenders | – | only when distinguishing from mezzanine or holdco lenders |
| offtaker | – | buyer, purchaser, off-taker (Buyer only inside clauses) |
| host government | – | the state, the government (alone), authorities |
| contracting authority | – | Case T and PPP chapters only: the public body that signs the PPP contract |
| EPC contractor | – | contractor (alone), builder, EPC firm |
| O&M operator | – | operator (alone), O&M contractor, O&M provider |
| LTSA provider | LTSA | OEM service provider |
| independent engineer | IE | lenders' technical advisor, LTA |
| facility agent | – | agent bank, administrative agent (except US-law contexts, noted once) |
| intercreditor agent | – | intercreditor representative |
| security agent | – | collateral agent; security trustee only in Chapter 52 when the trust mechanism is the topic |
| export credit agency | ECA | – |
| development finance institution | DFI | multilateral (alone) |
| engineering, procurement, and construction | EPC | – |
| power purchase agreement | PPA | power offtake agreement |
| commercial operation date | COD | completion date (completion is a separate defined term) |
| financial close | – | closing, financial closing |
| cash flow available for debt service | CFADS | – |
| debt service reserve account | DSRA | – |
| gearing | – | leverage (except debt's effect on returns, Chapter 8) |

In LaTeX source, "O&M" is typed `O\&M`.

## 9. Real cases and sources

- First mention names the project, country, and dates: "Paiton I, a 1,230 MW coal plant in East Java, Indonesia." Figures and dates come from that case's fact sheet in `book/facts/`.
- Approximate figures carry "approximately" before the number. Never round a precise sourced figure without marking it.
- Never quote a real person or document unless the fact sheet gives the exact words and source; paraphrase otherwise.
- A fact not in the sheets is verified from at least one primary or reputable secondary source and listed in the status note under "verification flags" with its source.
- In-text citation: author-date in parentheses at the first statement of a sourced figure or claim, "(MIGA 2016)". No footnotes. Every in-text citation resolves to exactly one entry in Sources (Section 4.8).
- The lesson of a real case is stated as a mechanism the reader can apply, never as a moral.

## 10. LaTeX hygiene

Every chapter compiles with `scripts/build_chapter.sh chapters/NN-slug.tex` before it is reported done. Allowed residue: undefined cross-chapter references only. Zero Overfull boxes wider than 5pt.

- Escape in running text: `\%`, `\$`, `\&`, `\#`, `\_`, `\{`, `\}`; write `\textasciitilde` and `\textasciicircum` for literal tilde and caret. Never escape inside `excel`, `\xl{}`, or `\url{}`.
- Dashes: `-` for hyphens, `--` for ranges, `---` for an em dash with no spaces around it. The prose limit stands: at most one `---` (or one pair) per paragraph, and most paragraphs have none. Never type Unicode dashes.
- Quotes: ` ``...'' ` and `` `...' ``; never the straight `"` in prose (it is fine inside `\xl` and `excel`). Apostrophes are `'`.
- Ellipsis `\ldots`. Multiplication sign for ratios via `\x`; elsewhere `$\times$`.
- Non-breaking space `~` between a number and its unit or currency (`650~MW`, `USD~45,000`), and inside `\USDm{}` automatically. Do not put `~` before `\cref` (cleveref handles it). Thin space `\,` only where a macro does not already supply it, such as `$1{,}000\,\mathrm{kW}$` in math.
- Unicode is allowed for letters in names (Ørsted, Société Générale, €STR as a name) and nowhere else: no Unicode quotes, dashes, math symbols, arrows, non-breaking spaces, or emoji.
- No `\newcommand`, `\renewcommand`, `\def`, `\let`, `\usepackage`, `\setlength`, or `\definecolor` in chapter files. Request macros through the coordinator, who adds them to `pfbook.sty`.
- No manual layout: no `\\` to break prose lines, no `\vspace`, `\newpage`, `\clearpage`, `\noindent` in prose, or font-size commands outside tables and TikZ.
- No `\footnote`, `\textbf`, `\underline`, or color commands in prose.
- Lists: `itemize` and `enumerate` only, never nested more than one level, and only for true checklists and sequences (`standards.md` Section 8).
- Paragraphs are separated by one blank line. One sentence per source line is optional; never hard-wrap inside `\xl{}`.

## 11. Prose enforcement: the ten tics technical writers fall into most

The full list is `standards.md` Section 8, "AI writing tics to avoid". Writers scan for all of it. The ten below recur most in technical drafts. Quoted text in this section is **[BAD]** unless marked otherwise.

1. Em dashes. **[BAD]** "The DSRA (a reserve)---usually six months---protects lenders---and sponsors pay for it." At most one `---` or pair per paragraph; most paragraphs have none. Rewrite with a period, comma, or parentheses; do not swap in semicolons wholesale. Check with `grep -n -- '---' chapters/NN-*.tex` and inspect every paragraph with more than one hit.
2. Inflated verbs and adjectives: "crucial", "robust", "ensure", "leverage" (as "use"), "key" (as an adjective), "facilitate". Name what the thing does: "the reserve pays six months of debt service," not "the reserve plays a crucial role in ensuring robust debt service."
3. Vague "This" opening a sentence. **[BAD]** "This means lenders are protected." Use the noun: "The cap means lenders recover delay costs up to USD 38.4 million."
4. False-contrast reframes. **[BAD]** "A DSRA isn't just a reserve; it's a signal." State the positive claim with its mechanism, or delete.
5. Tacked-on significance clauses. **[BAD]** "..., highlighting the importance of contract design." Make it a separate claim with evidence, or cut.
6. Signposted enumeration and the reflexive rule of three. **[BAD]** "There are three reasons. First..." Write connected prose in order of importance, with as many items as the content has.
7. Hedge stacking and reflexive "can" or "may". **[BAD]** "This can potentially lead to issues in many cases." Give the condition and frequency: "When the offtaker pays more than 60 days late, the DSRA is drawn."
8. Elegant variation. **[BAD]** "the project company... the SPV... the borrower... the vehicle." Use the canonical term from Section 8.2 every time.
9. Zinger endings and summary sandwiches. **[BAD]** "And that is the whole game." Cut the last sentence of any paragraph that restates the paragraph; sections end on their last substantive point.
10. "It depends" without direction, and non-conclusions. **[BAD]** "The right tenor depends on many factors." Name the two or three decisive factors, rank them, and say which way each moves the answer and by how much.

Swapping a banned word for a synonym is the same failure (`standards.md` Section 8, "Applying the list"). Writers run a banned-word scan on every chapter file before reporting done and report the count in the status note.

## 12. Sample passage

The reference for tone and density, as LaTeX source. It compiles as shown.

```latex
\begin{example}{Why lenders size on P90 \illustrative}\label{ex:9.6}
Take a 120~MW wind farm whose consultant forecasts 380.0~GWh a year at \term{P50},
the output level the farm is expected to beat in half of all years. At a tariff of
USD~52.40/MWh, that is revenue of \USDm{19.9}. Operating costs are \USDm{6.1}, so
CFADS is \USDm{13.8}.

Suppose the lenders sized the debt on that P50 case at a minimum DSCR of 1.30\x.
Annual debt service would be \USDm{10.6}. Now give the wind a bad year. If annual
output has a standard deviation of 10\%, the one-year \term{P90}, the level beaten in
90\% of years, is 331.3~GWh. Revenue falls to \USDm{17.4}, CFADS to \USDm{11.3}, and
the DSCR to 1.06\x. A typical lock-up test blocks distributions below 1.10\x, so one
ordinary bad year would trap the sponsors' cash in the project company.

Lenders therefore run the sizing on P90 as well and ask the bad year to clear its own
ratio. At 1.20\x{} on the P90 case, debt service drops to \USDm{9.4}, and the sponsors
lose \USDm{1.2} a year of debt capacity. That \USDm{1.2} buys the lenders a structure in
which the predictable bad year pays its debt service with room to spare, while only a
rarer, worse year tests the reserve account.
\end{example}
```

About 200 words; no dashes. Arithmetic: 380.0 × 52.40 = 19,912 (USD 19.9 million); 19.912 − 6.1 = 13.812; 13.812 / 1.30 = 10.62; 380.0 × (1 − 1.2816 × 0.10) = 331.3 GWh; 331.3 × 52.40 = 17,360 (USD 17.4 million); 17.360 − 6.1 = 11.26; 11.26 / 10.62 = 1.06x; 11.26 / 1.20 = 9.38 (USD 9.4 million); 10.62 − 9.38 = 1.24 (USD 1.2 million). Note `1.20\x{}` before a space: `\x` swallows the following space, so write `\x{}` when a word follows and `\x` before punctuation. (The P50 and P90 terms are bold here only because this passage stands in for their home definition in Chapter 9.)

## 13. Macros (now merged into latex/pfbook.sty)

Status: all macros below are merged into `latex/pfbook.sty` as of 2026-10-03. `\x` and `\bps` now use `xspace`, so `1.35\x on` and `175\bps over` space correctly; the `{}` form still works.

Add to `latex/pfbook.sty` (before the hyperref/cleveref block unless noted; the `framework` and `casescene` definitions replace the existing ones). Each was compiled in a scratch document with the package and the rendered PDF inspected; definitions are exact.

```latex
% Status labels (match \illustrative)
\newcommand{\casep}{\textsc{\textcolor{pfgray}{(Case P)}}}
\newcommand{\caset}{\textsc{\textcolor{pfgray}{(Case T)}}}
\newcommand{\caser}{\textsc{\textcolor{pfgray}{(Case R)}}}
\newcommand{\realcase}[1]{\textsc{\textcolor{pfgray}{(Real case: #1)}}}

% Exhibit source and note lines
\newcommand{\exhibitsource}[1]{\par\smallskip{\footnotesize\sffamily\raggedright Source: #1\par}}
\newcommand{\exhibitnote}[1]{\par{\footnotesize\sffamily\raggedright Note: #1\par}}

% Clause variants: \begin{clausevariants}\label{cl:N.K} ... \begin{clausevariant}{Title}{Status}\label{cl:N.Ka}
\newcounter{pfclausevar}[pfclause]
\renewcommand{\thepfclausevar}{\thepfclause\alph{pfclausevar}}
\newtcolorbox{pfclausevarbox}[2]{breakable,enhanced,colback=white,colframe=pfgray,boxrule=0.5pt,
  left=6pt,right=6pt,top=4pt,bottom=4pt,fonttitle=\sffamily\bfseries\small,coltitle=black,colbacktitle=pflight,
  title={Clause~\thepfclausevar\quad #1\quad\textmd{\textsc{(#2)}}},fontupper=\small}
\newenvironment{clausevariants}{\refstepcounter{pfclause}}{}
\newenvironment{clausevariant}[2]{\refstepcounter{pfclausevar}\begin{pfclausevarbox}{#1}{#2}}{\end{pfclausevarbox}}

% Numbered framework box (replaces the current \newtcolorbox{framework})
% Usage: \begin{framework}[label={fw:slug}]{Name}
\newtcolorbox[auto counter,number within=chapter,crefname={Framework}{Frameworks}]{framework}[2][]{%
  breakable,enhanced,colback=pflight,colframe=pfblue,boxrule=0.8pt,
  fonttitle=\sffamily\bfseries,title={Framework~\thetcbcounter\quad #2},left=6pt,right=6pt,#1}

% Running-case scene (replaces the current casescene: its "attach title to upper"
% title did not render in the test build; this version prints it as the first line,
% and parbox=false gives normal paragraph indents instead of hanging lines)
\newtcolorbox{casescene}[2]{breakable,enhanced,parbox=false,colback=white,colframe=pfblue!50,boxrule=0pt,
  leftrule=2.5pt,arc=0pt,left=8pt,right=4pt,top=2pt,bottom=2pt,
  before upper={{\sffamily\small\color{pfblue}#1\ \textperiodcentered\ #2}\par\smallskip}}

% Sources list with hanging indent
\newenvironment{sources}{\begin{list}{}{\setlength{\leftmargin}{1.5em}%
  \setlength{\itemindent}{-1.5em}\setlength{\itemsep}{3pt}\small}}{\end{list}}

% Long tables numbered as exhibits
\def\LTcaptype{exhibit}

% Landscape pages for wide model printouts
\RequirePackage{pdflscape}

% In the cleveref block (after \RequirePackage{cleveref}):
\crefname{pfclausevar}{Clause}{Clauses}
```

With the `\crefname{pfclausevar}` line in the preamble after cleveref, `\cref{cl:18.3a}` printed "Clause 18.3a" in the test; the numbered framework printed "Framework 28.1" and resolved through `\cref`; `\xl{}` inside a `tabularx` cell compiled and rendered.

## Addendum 2026-10-03

Issued by the architecture editor with `bible/ownership-resolutions.md` (rulings cited in parentheses). Where this addendum and an earlier section differ, the addendum wins.

### A.1 USD thousands for small illustrative deals (R-110)

- Exhibits for a small illustrative deal (total project cost under about USD 100 million: the Chapter 1 Llano Pardo deal, the Chapter 4 examples that reuse it, and similar deals elsewhere) may be stated in USD thousands, whole numbers, with the table header "USD k". Cells hold bare whole numbers with the thousands comma: 48,809.
- Prose keeps the house format: "USD 48.8 million", or "USD 28,700 a day" for amounts below one million. Never write "USD 48,809k" or "USDk" in prose.
- One exhibit uses one unit. Running cases (P, T, R) always use USD m (or the case currency in millions) and never USD k.
- In LaTeX the header is typed `USD k`; no macro is needed.

### A.2 Chapter 1 previews terms without bolding (R-110)

Chapter 1 introduces about forty terms intuitively. It sets none in bold and uses no `\term{}`; each term gets one sentence of plain meaning and, at first use, a `\cref` to its home chapter. The bold home definition stays with the owning chapter (`bible/glossary-canon.md`). Reviewers do not flag Chapter 1 for undefined terms, nor later chapters for re-teaching a term Chapter 1 previewed.

### A.3 Canonical forms and reserved abbreviations (R-059, R-114)

Add to the table in Section 8.2:

| Canonical form | Acronym | Not |
|---|---|---|
| equity contribution agreement | – (never abbreviated) | ECA, ECA agreement, equity agreement |
| export credit agency | ECA | – (ECA means only this) |
| share purchase agreement | – | SPA (SPA is reserved for the commodity sale and purchase agreement, sec:21.2) |
| partial credit guarantee | PCG | – |
| parent company guarantee | – | PCG |
| public sector comparator | PSC | – |
| production sharing contract | – | PSC |
| mandated lead arranger | MLA | – |
| master lease agreement | – | MLA |
| erection all risks | EAR | – |
| effective annual rate | – | EAR |
| enterprise value; present value | EV; PV | – |
| earned value; planned value | – | EV; PV |
| force majeure | FM | – ("hard FM" and "soft FM" are allowed only as compounds for facilities management) |
| turbine supply agreement | TSA | – |
| transmission service agreement | – | TSA |
| unitary charge | – | UC |
| risk-free rate (reference-rate sense: SOFR, SONIA, €STR) | RFR | – |
| risk-free rate (finance sense, CAPM input) | – (symbol $r_f$) | RFR |
| risk-adjusted return on capital | RAROC | RORAC |
| trapped cash | – | cash trap (accepted synonym in quotations of documents only) |
| financial completion | – | lenders' completion and project completion are synonyms; prefer "financial completion" |
| financial advisor | – | financial adviser |

### A.4 Lock-in against lock-up (R-060)

- "Lock-up" means only a block on distributions when a distribution condition fails (Chapter 37, ssec:37.4.1). Cash held as a result is "trapped cash" (ssec:37.4.3).
- "Lock-in" means only a restriction on transferring shares or a requirement to keep a minimum holding for a period, whether in a shareholders' agreement, a concession or the finance documents (Chapter 26, ssec:26.3.3).
- Never "share lock-up", "equity lock-up" or "distribution lock-in".

### A.5 Symbol canon additions (R-049)

Add to the table in Section 5.2:

| Symbol (LaTeX) | Meaning | Unit |
|---|---|---|
| `A^{*}` | target (contracted) availability against which the capacity payment is capped, as in $\min(1, A_t/A^{*})$ | % |
| `\mathrm{HR}^{\mathrm{c}}` | contracted heat rate at which the PPA pays for fuel (net, LHV) | kJ/kWh |
| `k_{\mathrm{HHV/LHV}}` | ratio of higher to lower heating value used to convert an LHV heat rate to the GCV basis of gas pricing (Case P: 1.108) | – |
| `\mathrm{EP}^{\mathrm{fuel}}_t` | fuel (energy) payment under eq:18.2 | currency |

The canonical tariff formulas are Chapter 18's eq:18.1 and eq:18.2; they replace the display in Section 5.2:

```latex
\mathrm{CP}_t = C \times 1{,}000 \times \mathrm{cpr} \times \mathrm{IF}_t \times \min(1, A_t/A^{*}) \times m_t
\qquad
\mathrm{EP}^{\mathrm{fuel}}_t = E^{\mathrm{del}}_t \times \mathrm{HR}^{\mathrm{c}} \times k_{\mathrm{HHV/LHV}} \times \frac{p^{\mathrm{fuel}}_t}{1{,}055.06}
```

`HR` without a superscript remains the plant's actual net heat rate.

### A.5a Symbol canon additions: earned value (R-100, R-114; u13 request)

Add to the table in Section 5.2:

| Symbol (LaTeX) | Meaning | Unit |
|---|---|---|
| `W^{\mathrm{earned}}_t` | earned value at month $t$: the budgeted cost of the work actually performed | currency |
| `W^{\mathrm{planned}}_t` | planned value at month $t$: the budgeted cost of the work scheduled to date | currency |
| `\mathrm{SPI}_t` | schedule performance index, $W^{\mathrm{earned}}_t / W^{\mathrm{planned}}_t$ | – |
| `T_{\mathrm{plan}}`; `\hat{T}` | planned construction duration; forecast duration, $T_{\mathrm{plan}}/\mathrm{SPI}_t$ | months |

Earned value and planned value are never written EV or PV, which R-114 reserves for enterprise value and present value. Chapter 61's eq:61.3 is the home equation (ssec:61.4.2).

### A.6 Calendar rows in the model (R-021 as amended by D-047)

Amended October 3, 2026 (consolidation A, D-047): the rows stay where the verified Case P workbook holds them. Calendar-driven series that are not project inputs by period (reference base rates such as 6M LIBOR and Term SOFR, FX rates, CPI and other indices, the Kessaran policy rate) are entered in native periodicity on the Inputs sheet and mapped once onto each timeline in a calendar block on that timeline's own sheet: for the semiannual timeline, the "Macro paths" block at the head of the Operations sheet (Case P: Operations rows 7 to 15, with the index rows 16 to 27 below it); for the monthly construction timeline, calendar rows on the Construction sheet (Case P: Construction rows 16 to 18). One block per timeline, one row per series, units in column E. Calculation rows link to those rows (green font) and never look up the Inputs series directly. The sheet order in Section 5.4 is unchanged. Chapter 39 teaches the principle and names the placement (ssec:39.3.4, ssec:39.5.4); Chapters 40 to 43 link to it. (Superseded text: "in a block at the foot of the Time sheet, below the flags".)

### A.7 Label scheme for front matter (R-107)

- Front matter (file 00) uses unnumbered `\chapter*` and `\section*` headings with labels `fm:slug`, from the anchor registry: `fm:how-built`, `fm:running-cases`, `fm:conventions`, `fm:routes`, `fm:study-plan`, `fm:exercises`, `fm:model-builds`, `fm:caveat`.
- Front-matter exhibits are labeled `exh:fm.1` to `exh:fm.3` and print as Exhibit FM.1 to FM.3.
- Chapters 89 to 94 use the chapter scheme of Section 3.2.
- `\cref` to an `fm:` label prints the section name, not a number.

### A.8 Formulas owned elsewhere (R-116)

A chapter that displays a formula owned by another chapter does so only as a model row or a specialized application. Its equation caption names the application and the text cites the home equation ("implementing eq:37.1"). The anchor registry lists the repurposed captions.

### A.9 Excel formulas that contain a percent sign (blueprint review; D-041)

Any Excel formula containing `%` (for example `=PV(8.4%,20,-1.27)` or `=PMT(6.35%,10,-126.5)`) is shown in a display `excel` block, never inline in `\xl{}`, because `\xl{}` cannot carry `%` (Section 5.3). Prefer cell references (`=PV(F5,F6,-F7)`, with the rate in F5 and the layout stated in the lead-in sentence), which may then go inline. The same applies to formulas containing `#`, `\`, `{` or `}`. Briefs mark such formulas "excel block".

### A.10 Every worked example is located (blueprint review; D-041)

Every worked example, exercise or clause that models a project, a financing or a contract names its place (country, state or market), its date or year, and its parties (fictional names, or real ones labeled as a real case). Fictional parties follow Section 8 and the Case Bible naming conventions. Only placeless arithmetic whose subject is the technique itself (for example a discount factor or a day-count fraction) may stay unlocated, and then it states no sector or deal type. Within each Part, examples cover at least four regions (Americas; Europe; Middle East and Africa; Asia-Pacific), and sector examples sit in markets where that sector is actually financed.

### A.11 Never reuse the style sheet's sample figures as inputs (blueprint review; D-041)

Never reuse the style sheet's sample figures as inputs. The numbers that illustrate formats in this file (USD 412.6 million, the table values in Section 6.1, and the figures in the sample passage of Section 12) show format only: no writer may use them as an example's or exercise's capex, debt, CFADS, energy, reserves or any other input or result. Choose distinct, lumpy, realistic figures for each example and recompute the results in Python. A round principal is allowed only when the round number is the teaching point, and the text then says so (for example "a USD 400 million commitment, typical of a club deal"). The numbers auditor checks this rule.
