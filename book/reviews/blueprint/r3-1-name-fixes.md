# R3-1 name fixes: fictional names reused for different parties

Continuity editor, October 3, 2026. Source: defect R3-1 in `reviews/blueprint/r3-verification.md`. The first party in book order keeps each name, and every later, different party is renamed. Only the names changed. No input, result or other number was touched. Each rename is registered in Case Bible Part 5A.6. The 5A.2 Tallo Bhir row and the 5A.5 u14 and u17 rows are also updated.

Web checks were run with the session's web search tool. No personal identifier was sent, and no bot block was bypassed. "Clear" means the search found no company, project or plant of that name. The drafted chapters (`chapters/02-what-project-finance-is.tex`, `chapters/36-sizing-and-sculpting-debt.tex`, `chapters/99-test.tex`) contain none of the clashing names, so no chapter file changed.

## Renames

| # | Old name (later party) | New name | File and line(s) | Chapter | Kept by (first party) | Check |
|---|---|---|---|---|---|---|
| 1 | Ventos do Seridó Energia SA | Ventos da Várzea Comprida Energia SA | `bible/briefs/u06.md` l.638 | Ch 25 (Example 25.4, 132 MW) | u05 Exercises 22.6 and 22.11 | Clear |
| 2 | Ventos do Seridó Energia S.A. | Eólica Lajedo Alto Energia S.A. | `bible/briefs/u11.md` l.162 | Ch 51 (Example 51.5, 164 MW; R3-1 calls it the "Ch 52 example", but the label is `ex:51.5`) | same | Clear |
| 3 | Ventos do Seridó Energia SA; sponsor Seridó Renováveis Ltda | Ventos do Baixio Seco Energia SA; Baixio Seco Renováveis Ltda | `bible/briefs/u17.md` l.181 (85.8 teaser) and l.1838 (name list); `bible/case-bible.md` 5A.5 u17 row | Ch 85 (220.5 MW) | same | Clear |
| 4 | Saguaro Flats Solar Holdings LLC | Sandwash Ridge Solar Holdings LLC | `bible/briefs/u07.md` l.164 | Ch 29 (Example 29.5) | u03 Example 10.3 | Clear (near misses Sand Ridge and Sandy Ridge Solar, not used) |
| 5 | Saguaro Flats Solar LLC | Bitterbrush Mesa Solar LLC | `bible/briefs/u10.md` l.223 | Ch 46 (Example 46.5, 140 MW; Copperline Renewables remains the seller) | same | Clear (near miss Blythe Mesa Solar, not used) |
| 6 | Saguaro Flats Solar LLC | Coyote Bajada Solar LLC | `bible/briefs/u13.md` l.622 | Ch 62 (Example 62.5, 147.5 MWac) | same | Clear |
| 7 | Saguaro Flats Solar LLC | Tinajas Flat Solar LLC | `bible/briefs/u15.md` l.524 | Ch 70 (Example 70.4, 200 MWac) | same | Clear |
| 8 | Brazos Bend Power LLC | Lampasas Fork Power LLC | `bible/briefs/u07.md` l.502 | Ch 30 (Example 30.2, 640 MW CCGT) | u05 Example 20.2 (Brazos Bend Wind LLC) | Clear |
| 9 | Brazos Bend Peaking LLC | Salado Gap Peaking LLC | `bible/briefs/u13.md` l.967 | Ch 63 (Example 63.2) | same | Clear |
| 10 | Brazos Bend Power LLC | Sulphur Draw Power LLC | `bible/briefs/u15.md` l.187 | Ch 69 (Example 69.3, 620 MW CCGT) | same | Clear |
| 11 | Bull Run Data Campus LLC; "the Bull Run campus" | Hogback Hollow Data Campus LLC; "the Hogback Hollow campus" | `bible/briefs/u16.md` l.1605, l.1607 | Ch 82 (Examples 82.4 and 82.5, 96 MW IT) | u05 Example 21.9 | Clear |
| 12 | Mekong Delta Power JSC | Ham Luong Gas Power JSC | `bible/briefs/u12.md` l.1394 | Ch 60 (Example 60.1, 450 MW) | u10 Example 49.2 | Clear |
| 13 | Viento del Istmo S.A.P.I. de C.V. | Eólica Guiengola S.A.P.I. de C.V. | `bible/briefs/u11.md` l.1316 | Ch 55 (Example 55.3, 280 MW) | u03 Chapter 13 drill | Clear |
| 14 | Ankobra Power Ltd | Fosu Lagoon Power Ltd | `bible/briefs/u14.md` l.207 and l.1728 (name list); `bible/case-bible.md` 5A.5 u14 row | Ch 66 (Example 66.8, 310 MW) | u05 Chapter 17 | Clear |
| 15 | Tallo Bhir Hydropower Ltd; "(Tallo Bhir)" | Rato Pakha Hydropower Ltd; "(Rato Pakha)" | `bible/briefs/u10.md` l.1072 (Example 48.1), l.1238 (Exercise 48.5); `bible/case-bible.md` 5A.2 row | Ch 48 (96 MW) | u03 Example 11.5 | Clear (near miss Ratle HEP, India, not used) |
| 16 | Prampram Power Company | Lolonya Power Company | `bible/briefs/u09.md` l.1138 (Example 40.4) | Ch 40 (340 MW near Tema) | u02 Example 5.18 (Prampram Power Ltd) | Clear |

R3-1 rows for Bukhara Quyosh Energy and Llanos de Mérida Solar were already fixed in round 3, so this pass made no change to them.

## Names rejected during checking

- Juazeiral: too close to the Juazeiro, Bahia, solar hub.
- Arrowweed Flat: close to Arrowleaf Solar, California.
- Greasewood: a real Texas solar project.
- Tehuacana Creek: a real Texas solar and storage project.
- Vam Co: a real Vietnamese JSC.
- Esiama: the site of a real Aggreko plant in Ghana.
- Amanzule: close to Amandi Energy.
- Bonsa: a sub-basin of the Ankobra, so it would echo the kept name.

## Verification

- A scripted cross-unit scan over every name that ends in a corporate suffix found no further clash between different parties. The remaining repeats are running-case parties or the same deal reused.
- After the edits, each old name occurs only in its first party's unit:
  - u05: Ventos do Seridó, Brazos Bend, Bull Run and Ankobra;
  - u03: Saguaro Flats, Viento del Istmo and Tallo Bhir;
  - u10: Mekong Delta Power;
  - u02: Prampram.
- The u03 name-check list (l.1611) keeps its first-party names unchanged.
