# EU CBAM (SKDM) – verified parameters for Türkiye liability modelling (2026–2034)

Prepared 18 October 2026 for the EU–Türkiye Customs Union exit strategy study.

**Tags**
- [VERIFIED]: I read the primary text myself in this session (EUR-Lex/OJ PDF or HTML, Commission site, Council or EP document, Resmî Gazete).
- [PARTIAL]: the source is secondary (law firm, trade press, industry), or the figure is my own inference or calculation from verified parameters.
- [UNVERIFIED]: not confirmed.

Downloads and parsing scripts were kept outside the package; parsed values are quoted below with their URLs.

**Output files** (derived tables; the package recomputes them from the official files, see `kod/f2i_skdm.py`):
- `cbam_annex1_cn.csv`: Annex I CN codes in force. 90 rows, including excluded and out-of-scope codes, with notes.
- `tr_default_values_IR2026_1740.csv`: all 283 Türkiye default-value rows from IR (EU) 2026/1740. Includes fallback resolution and mark-up values for 2026, 2027 and 2028+.
- `tr_net_obligation_defaults_2026_2034.csv`: net certificates per tonne for 14 representative goods when default values are used. Covers 2026–2034 under current law and under the COM(2026) 616 proposal. These are calculations.
- `cbam_downstream_proposal_COM2025_989.csv`: the Annex I amendment proposed in COM(2025) 989. Lists 114 new line items, plus existing and excluded codes.

---

## 0. Legal map (what is in force on 18.10.2026)

| Act | Date / OJ | Role | Tag |
|---|---|---|---|
| Regulation (EU) 2023/956 (CBAM) | 10.5.2023, OJ L 130, 16.5.2023 | Basic act | [VERIFIED] |
| Regulation (EU) 2025/2083 ("simplifying and strengthening") | 8.10.2025, OJ L 17.10.2025; in force from the third day after publication (20.10.2025) | Only amending act. The current consolidated version is 02023R0956-20251020, and the EUR-Lex "ALL" page lists 2025/2083 as the only "Modified by" act, apart from language corrigenda. | [VERIFIED] |
| Directive (EU) 2023/959 (amends ETS Directive 2003/87/EC) | OJ L 130, 16.5.2023 | Art 10a(1a) sets the CBAM factor, i.e. the free-allocation phase-out | [VERIFIED] |
| IR (EU) 2025/2547 | 10.12.2025, OJ 22.12.2025 | Calculation methods for embedded emissions | Cited in other acts; not read in full |
| IR (EU) 2025/2548 | 10.12.2025, OJ 22.12.2025 | Calculation and publication of the certificate price | [VERIFIED] |
| IR (EU) 2025/2620 | 16.12.2025, OJ 22.12.2025 | Free allocation adjustment (Art 31) and CBAM benchmarks | [VERIFIED] |
| IR (EU) 2025/2621 | 16.12.2025, OJ 31.12.2025, applies from 1.1.2026 | Default values (2,400 pp.) | [VERIFIED] |
| IR (EU) 2026/1740 | 20.7.2026, OJ 31.7.2026, applies retroactively from 1.1.2026 | Replaces Annexes I and IV of IR 2025/2621 (1,913 pp.) | [VERIFIED] |
| Implementing Decision (EU) 2026/1862 | 23.7.2026, OJ 24.7.2026 | Cross-sectoral correction factor (CSCF) = 100 % for every year 2026–2030 | [VERIFIED] |
| Other acts: IR 2025/486 and 2025/2549 (authorisation), IR 2024/3210 and 2025/2550 (registry), IR 2025/2546 (verification), DR 2025/2551 (accreditation), IR 2025/2619 (customs), IR 2025/2210 (continental shelf/EEZ) | — | Listed on the Commission's CBAM legislation page | [VERIFIED] (listing only) |

Sources:
- https://eur-lex.europa.eu/eli/reg/2025/2083/oj (PDF: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202502083)
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02023R0956-20251020
- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32023R0956
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023L0959
- http://data.europa.eu/eli/reg_impl/2025/2548/oj
- http://data.europa.eu/eli/reg_impl/2025/2620/oj
- http://data.europa.eu/eli/reg_impl/2025/2621/oj
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202601740
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026D1862
- https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en

**Strategic note for the CU-exit study [VERIFIED].**
- Türkiye is not exempt under the Customs Union.
- Art 2(4) and Annex III point 1 exempt only Iceland, Liechtenstein, Norway, Switzerland and five territories.
- Under Art 2(6), a country can be listed in Annex III only if:
  - (a) the EU ETS applies to it, or its ETS is fully linked to the EU ETS by agreement; and
  - (b) its carbon price "is effectively charged on the greenhouse gas emissions embedded in those goods without any rebates beyond those also applied in accordance with the EU ETS".
- Under Art 2(5), origin follows the non-preferential origin rules (UCC Art 59). CU free-circulation status is therefore irrelevant to CBAM.

---

## 1. Annex I – CN codes covered (consolidated, in force)

CSV: `cbam_annex1_cn.csv`. The columns are cn_code, sector, description and note. Chapter 72 is expanded to 4-digit headings, and to sub-headings for 7202.

The only 2025–2026 change to Annex I is Reg 2025/2083 Art 1(28) [VERIFIED]. It replaces "2507 00 80 – Other kaolinic clays" with "ex 2507 00 80 – Other kaolinic clays except non-calcined kaolinic clays". IR 2026/1740 therefore uses TARIC 2507 00 80 80 "Calcined clay".

Reg 2025/2083 Art 1(29) also adds electricity (2716 00 00) to Annex II, the list of goods for which only direct emissions count [VERIFIED].

**Coverage summary [VERIFIED]** (from consolidated Annex I):

- **Cement (CO2):** ex 2507 00 80; 2523 10 00; 2523 21 00; 2523 29 00; 2523 30 00; 2523 90 00. Direct and indirect emissions count.
- **Electricity (CO2):** 2716 00 00. Direct only since 2025/2083.
- **Fertilisers:**
  - 2808 00 00 (CO2+N2O)
  - 2814 (CO2)
  - 2834 21 00 (CO2+N2O)
  - 3102 (CO2+N2O)
  - 3105 (CO2+N2O), except 3105 60 00
  - Direct and indirect emissions count.
- **Iron and steel (CO2):**
  - "72 – Iron and steel", except:
    - 7202 2 (ferro-silicon), 7202 30 00, 7202 50 00, 7202 70 00, 7202 80 00, 7202 91 00, 7202 92 00, 7202 93 00, 7202 99 10/30/80;
    - 7204 (ferrous waste and scrap).
  - So FeMn (7202 11/19), FeCr (7202 41/49) and FeNi (7202 60 00) are covered.
  - Also covered: 2601 12 00 (agglomerated iron ore, which counts indirect emissions as well); 7301; 7302; 7303 00; 7304; 7305; 7306; 7307; 7308; 7309 00; 7310; 7311 00; 7318; 7326.
  - Direct only (Annex II), except 2601 12 00.
- **Aluminium (CO2+PFCs):** 7601; 7603; 7604; 7605; 7606; 7607; 7608; 7609 00 00; 7610; 7611 00 00; 7612; 7613 00 00; 7614; 7616. Direct only. Not covered: 7602 (scrap) and 7615.
- **Hydrogen (CO2):** 2804 10 00, in the Annex I table "Chemicals". Direct only.

---

## 2. Phase-in: the CBAM factor and how the obligation is reduced

### 2.1 Current law [VERIFIED]

Directive 2003/87/EC Art 10a(1a), as inserted by Directive (EU) 2023/959, reads:

> "The CBAM factor shall be equal to 100 % for the period between the entry into force of that Regulation and the end of 2025 and … shall be equal to 97,5 % in 2026, 95 % in 2027, 90 % in 2028, 77,5 % in 2029, 51,5 % in 2030, 39 % in 2031, 26,5 % in 2032 and 14 % in 2033. From 2034, no CBAM factor shall apply."

### 2.2 How the factor enters the CBAM obligation [VERIFIED]

- CBAM Art 31(1) says certificates are "adjusted to reflect the extent to which EU ETS allowances are allocated free of charge".
- Under IR 2025/2620 Annex point 2: FAA_g = SEFA_g,y × M_g.
- With default values (Annex point 4, Eq. 6): SEFA = CBAM_y × CSCF_y × BM_g. BM_g is the default CBAM benchmark (Column B) for the production route that IR 2025/2621/2026/1740 assigns to the country.
- With actual data (Eq. 2–4): process benchmarks (Column A) are combined recursively with the SEFA of the precursors.
- The CSCF is 100 % for each year 2026–2030 (Decision (EU) 2026/1862 Art 1). For 2031 onwards it has not been determined; my tables assume 1 [PARTIAL].
- The certificates to surrender are the embedded emissions minus the FAA minus any Art 9 reduction. This follows from Art 6(2)(c) as amended: "after the reduction that is due on the account of the carbon price paid in a third country in accordance with Article 9 and the adjustment … in accordance with Article 31".

**Implication [PARTIAL – inference].**
- "1 − CBAM factor" (2.5 % in 2026 … 100 % in 2034) is the share of the EU benchmark that is no longer covered by free allocation. It is not the share of the importer's embedded emissions that is charged.
- The share of embedded emissions charged is 1 − CF_y × BM/EE.
- Türkiye's steel defaults are about 1.5–1.8× the route-(C) benchmark (rebar 2.310/1.364 = 1.69; HRC 2.428/1.370 = 1.77; 7305 2.182/1.458 = 1.50).
- Even in 2026, roughly 41–50 % of the marked-up default embedded emissions of Turkish pipes, long and flat products is therefore payable (rebar 1.211/2.541 = 48 %; HRC 50 %; 7305 41 %). See section 6.4.

### 2.3 Pending proposal: ETS review COM(2026) 616 final, 17.7.2026 (procedure 2026/0210(COD)) [VERIFIED text, NOT ADOPTED]

The amended Art 10a(1a) would read:

> "97,5 % in 2026, 95 % in 2027, 91.5 % in 2028, 81 % in 2029, 59% in 2030, 48% in 2031, 37,5% in 2032 and 27% in 2033, 15% from 2034 to 2037. From 2038, a CBAM factor of 0 % shall apply."

- The explanatory memorandum says "15 % of the free allocation phased out due to the CBAM factor be reintroduced, starting in 2028".
- The recital says the CBAM-factor amendment "should also apply from 30 September 2027 onwards".
- From 2031, free allocation would also depend on decarbonisation investment.
- Newly added CBAM goods would get 97.9 % in the first year and 95.8 % in the second year of the next allocation period.
- Status: the Council Presidency note ST 13435/26 of 25.9.2026 says the proposal is "slowing down CBAM phase-in from 2034 to 2038". The Environment Council held a policy debate on 12.10.2026. The Presidency aims for a general approach in December, and leaders target completion by Q1 2027.

Sources:
- Proposal (EUR-Lex HTML served via the Commission's climate site): https://climate.ec.europa.eu/document/download/c0b4ca8e-0e12-4b4e-9976-98c0b4224410_en (= CELEX 52026PC0616)
- https://data.consilium.europa.eu/doc/document/ST-13435-2026-INIT/en/pdf

### 2.4 Phase-in table

| Year | CBAM factor (law) | 1−CF (law) | CBAM factor (COM(2026) 616) | 1−CF (proposal) | CSCF |
|---|---|---|---|---|---|
| 2026 | 97.5 % | 2.5 % | 97.5 % | 2.5 % | 100 % [V] |
| 2027 | 95 % | 5 % | 95 % | 5 % | 100 % [V] |
| 2028 | 90 % | 10 % | 91.5 % | 8.5 % | 100 % [V] |
| 2029 | 77.5 % | 22.5 % | 81 % | 19 % | 100 % [V] |
| 2030 | 51.5 % | 48.5 % | 59 % | 41 % | 100 % [V] |
| 2031 | 39 % | 61 % | 48 % | 52 % | not set (assume 100 %) |
| 2032 | 26.5 % | 73.5 % | 37.5 % | 62.5 % | not set |
| 2033 | 14 % | 86 % | 27 % | 73 % | not set |
| 2034 | 0 % | 100 % | 15 % (to 2037), 0 % from 2038 | 85 % | n/a |

---

## 3. CBAM certificate price

**Law [VERIFIED].**
- Art 21(1), as amended, sets the weekly rule from 2027: "average of the closing prices of EU ETS allowances on the auction platform … for each calendar week".
- Art 21(1a) sets the 2026 rule: for emissions declared for 2026, "the quarterly average of the closing prices … of the quarter of importation of the goods".
- Sales of certificates on the common central platform start on 1 February 2027 (Art 20(1); Art 36(2)(d)).

**IR 2025/2548 [VERIFIED].**
- Art 1: for 2026, the price is the quarterly average of auction clearing prices (Delegated Reg 2023/2830 Art 7), weighted by auctioned volume. It covers common and opt-out platforms, excludes cancelled auctions, and is calculated in the first calendar week of the following quarter.
- Art 4: publication follows on the first working day of the next week.
- Art 5: from 1 January 2027 the price is a weekly volume-weighted average of auction clearing prices.
- Art 8: the weekly price is published on the first working day of the week after the auctions.

**Published 2026 prices, Commission page [VERIFIED].**

| Quarter | Published | Price |
|---|---|---|
| Q1 2026 | 7 Apr 2026 | €75.36 |
| Q2 2026 | 6 Jul 2026 | €75.28 |
| Q3 2026 | 5 Oct 2026 | €82.32 |
| Q4 2026 | due 4 Jan 2027 | — |

Source: https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/price-cbam-certificates_en

**Market level, October 2026 [PARTIAL].**
- GMK Center, citing ICE: EUA Dec-26 futures peaked at €87.99 on 14 Sep; the September average was €85.6; prices reached €88.3 on 12 Oct.
- cbamguide.com, citing EEX: auction clearing price €86.28 on 12 Oct; its Q4-to-date running average over 8 auctions (1–12 Oct) is €84.76.
- Sources: https://gmk.center/en/news/european-carbon-prices-rose-to-e88-t-in-october/ ; https://cbamguide.com/news/2026-10-12-environment-council-ets-review-cbam-phase-in-carbon-price/

---

## 4. Article 9 – carbon price paid in the country of origin

### 4.1 Regulation text (Art 9 as replaced by Reg 2025/2083 Art 1(8)) [VERIFIED]

- **9(1).** A reduction is possible only "Where the embedded emissions are determined on the basis of actual emissions". It applies "only if the carbon price has been effectively paid in a third country", and "any rebate or other form of compensation available in that country that would have resulted in a reduction of that carbon price shall be taken into account".
- **9(2).** The declarant keeps documentation showing that the price was effectively paid. This includes evidence on rebates and "references to the relevant legislation of that country". The documentation must be certified by a person "independent from the authorised CBAM declarant and from the authorities of the third country". The declarant also keeps "evidence of the actual payment".
- **9(3).** Records are kept until the end of the fourth year after the declaration.
- **9(4).** Default carbon prices:
  - The declarant may claim a reduction "by reference to yearly default carbon prices", net of rebates.
  - This is allowed only "where a carbon price was set by the rules applicable in the third country and a yearly default carbon price can be determined, including on a conservative basis".
  - "Where the embedded emissions are determined on the basis of default values, a reduction may be claimed only by a reference to yearly default carbon prices."
  - "As from 2027, the Commission may … determine and make available, in the CBAM registry … the default carbon prices for those third countries and publish the methodology."
- **9(5).** Implementing acts will cover: conversion into certificates, euro conversion at the yearly average exchange rate, evidence of payment, examples of rebates, and the qualifications and independence of the certifier.
- **Art 10(5)(d), (7).** A third-country operator registered in the CBAM registry may upload the carbon-price evidence and disclose it to declarants.

### 4.2 Draft implementing regulation under Art 9(5)

The draft is Ares(2026)4841230 of 13.5.2026 [VERIFIED draft text]. Feedback ran 13.5–10.6.2026.

**Status:** the Have Your Say API shows initiative 14830 at stage "ISC_WORKFLOW", with an adoption-stage record not yet populated. It is **not adopted as of 18.10.2026** [VERIFIED status via API].

Key provisions of the draft:
- **Art 2(3) – eligible mechanisms.** A "carbon price mechanism" is a carbon tax, fee or levy, or an ETS. A baseline-and-credit ETS is included (Art 2(5)).
- **Art 3 – effective price.** The price effectively paid is determined per good, using the same reporting period as the emissions verification. Prices from several mechanisms are aggregated.
- **Art 4 – defaults.** Commission default carbon prices may be used for precursors produced outside the installation, and for indirect emissions.
- **Art 5 – FX.** Conversion uses the yearly average exchange rate published by the Commission, based on ECB or Eurostat rates.
- **Art 6 – formulas.**
  - Reduction = (€EFF_CP_g / Ref Price CBAM) × Q_g, where €EFF_CP_g is in EUR per tonne of good.
  - Default variant: (€DCP × SEE_g / Ref Price) × Q_g.
  - Ref Price = the yearly average of the CBAM certificate prices published under IR 2025/2548.
- **Art 8(1) – rebates to deduct.**
  - (a) reduced tax rates;
  - (b)(i) "emissions associated with free allowances received by the operator", (ii) emissions below a baseline, (iii) exempted emissions;
  - (c) refunds, "including forms of indirect cost compensation";
  - (d) any other compensation.
- **Art 8(2) – revenue-recycling carve-out.** Subsidies financed by carbon-price revenues are not deducted if:
  - (a) all covered installations are eligible;
  - (b) support requires an application;
  - (c) the award decision is public; and
  - (d) the objective is to reduce the beneficiary's emissions.
- **Art 8(3).** If entitlement to a rebate exists but its amount cannot be evidenced, no deduction is allowed.
- **Recital 13 – international credits.** Article 6.2 and 6.4 credits used for domestic compliance count up to "a maximum of 10 % of the reported and confirmed emissions under the carbon price mechanism". The operative detail is in the draft annex, which I did not read.
- **Certification.** An accredited independent person (EN ISO/IEC 17029:2019) gives reasonable assurance.
- **Art 32.** The draft would apply from 1 January 2026.

Sources:
- https://ec.europa.eu/info/law/better-regulation/brpapi/groupInitiatives/14830
- Draft: https://ec.europa.eu/info/law/better-regulation/api/download/090166e52d80a42e

### 4.3 What this means for "keeping CBAM money in Türkiye" [PARTIAL – derivation from verified and draft texts]

Per tonne of good:

> Certificates = (EE − FAA_EU) − P_TR·(EE − FA_TR)/RefPrice

Here FA_TR is the free allocation the Turkish ETS gives per tonne, and EE is the embedded emissions.

- Full neutralisation requires P_TR·(EE − FA_TR) = (EE − FAA_EU)·RefPrice.
- If the Turkish ETS gives no free allocation, P_TR ≥ RefPrice × (1 − FAA_EU/EE) suffices.
- If Türkiye copies the EU free allocation (FA_TR = FAA_EU), it needs P_TR = RefPrice.
- Free allowances in the Turkish ETS reduce the deduction one-for-one (draft Art 8(1)(b)(i)).
- Recycling revenues into decarbonisation subsidies under the four Art 8(2) conditions does not reduce the deduction.
- Exporters that use default values can benefit only through a Commission-published default carbon price for Türkiye. That is discretionary ("may") and available from 2027.
- A Turkish carbon price therefore helps only actual-value, verified exporters by default.
- The Ministry of Trade's slide shows that actual-data use in Turkish CBAM reports was already 64–82 % in the transitional period (section 8).

---

## 5. De minimis, authorisation, deadlines (Reg 2025/2083) [VERIFIED]

**De minimis.**
- New Art 2a and Annex VII set a "single mass-based threshold" of **50 tonnes net mass** per importer per calendar year. It is cumulative over all CN codes in iron and steel, aluminium, fertilisers and cement.
- If an importer exceeds it, all obligations apply to **all** emissions in **all** goods imported that year (Art 2a(2)).
- It does **not** apply to electricity or hydrogen (Art 2a(4)).
- Each year by 30 April, the Commission reviews whether the threshold keeps the exemption at ≤ 1 % of embedded emissions. A delegated act follows if the result deviates by more than 15 t.
- Recital 5: the threshold ensures "at least 99 % of emissions embedded in imported goods remain within the scope", while "the vast majority" of importers are exempted.
- Anti-splitting rules apply (Art 25a(4), Art 27(2)(b)). Importers that exceed the threshold without being authorised face penalties (Art 26(2a)).
- Effect for Türkiye [PARTIAL]: negligible for bulk exports, since lots far exceed 50 t. The threshold exempts small importers of hardware and steel articles.

**Authorised CBAM declarant.**
- Only authorised declarants may import (Art 4; Art 25(1) "without prejudice to Article 2a").
- An application is required before importing (Art 5(1)).
- Indirect customs representatives may act as declarants (Art 5(1a), (2), (2a)).
- Transitional relief, Art 17(7a): applicants who filed by **31 March 2026** "may provisionally continue to import goods until the competent authority takes a decision".
- A guarantee is required if the applicant has not been established for the two prior financial years (Art 17(5)).

**Declaration and surrender.**
- Annual declaration and surrender by **30 September** each year, "for the first time in 2027 for the year 2026" (Art 6(1), 22(1)).
- From 2027, at each quarter-end the declarant must hold at least **50 %** of the embedded emissions of imports to date. This is computed on defaults without mark-up or on the previous year's surrender, and is adjusted for free allocation (Art 22(2); applies from 1.1.2027).
- The previous holding rule was 80 % (recital).

**Certificates.**
- Sales start on 1 Feb 2027 (Art 20(1)).
- Repurchase requests are due by 31 October (Art 23(1)). Certificates bought in 2027 for 2026 emissions can be repurchased only in 2027 (Art 23(2a)).
- Cancellation (Art 24(2)): certificates for 2026 emissions are cancelled on 1 Nov 2027.

**Penalty.**
- Art 26(1) sets the penalty equal to the EU ETS excess-emissions penalty (Directive Art 16(3)–(4)) for each certificate not surrendered.
- Paying it does not remove the obligation to surrender (Art 26(3)).

---

## 6. Default values (Türkiye) and benchmarks

### 6.1 Acts and rules [VERIFIED]

- IR 2025/2621 Art 1 sets: Annex I for goods; Annex II for indirect emissions; Annex III for electricity imports; Annex IV for precursors of unknown origin.
- Art 2: it applies from 1.1.2026 and "shall be revised in 2027 at the latest". Recital 11: "The default values and mark-ups shall be revised by December 2027 at the latest".
- IR 2026/1740 replaced Annexes I and IV retroactively from 1.1.2026.
  - It corrects transcription errors. For Türkiye's rows, the values are identical to IR 2025/2621.
  - It deletes the marked-up columns and states the rule in the opening paragraph:
  > "For goods in the cement, iron and steel, aluminium and hydrogen sectors, the mark-up shall be 10 % for the year 2026, 20 % for the year 2027 and 30 % for the year 2028 and onwards. For goods in the fertiliser sector, the mark-up shall be 1 % for the year 2026 and onwards."
  - The mark-up applies to the "total emissions" column. The direct and indirect columns are "only provided for information" (recital 10).
- Fallback rule:
  > "Where a country or territory is explicitly listed but no value is provided or the relevant field shows '–', the default value … from the table 'Other countries and territories' needs to be selected."
  - Basic act Annex IV point 4.1, as amended, says this fallback is the average of the 10 highest-intensity exporting countries.
- Cross-check: my parse of the IR 2026/1740 PDF (Türkiye, 283 rows) matches the Commission's information Excel (version 2, 6.8.2026) with 0 mismatches. Excel: https://taxation-customs.ec.europa.eu/document/download/1c05d211-80cb-4aaa-8ef0-e08005a95d7e_en?filename=DV%20correcting%20act_final%20update_06.08.xlsx

### 6.2 Türkiye default values, IR 2026/1740 Annex I (tCO2e per tonne, total) [VERIFIED]

Route indicators: (C) BF/BOF carbon steel; (K) primary aluminium; (A) grey clinker.

| Good | CN | Türkiye value | Route | 2026 (+10 %) | 2027 (+20 %) | 2028+ (+30 %) | EU default BM (Col. B) |
|---|---|---|---|---|---|---|---|
| Grey clinker | 2523 10 00 90 | **"–" → fallback 1.410** (direct 1.370 + indirect 0.050) | (A) | 1.551 | 1.692 | 1.833 | 0.666 |
| Grey Portland cement | 2523 29 00 | **"–" → fallback 1.440** | – | 1.584 | 1.728 | 1.872 | 0.666 |
| Aluminous cement | 2523 30 00 | 1.950 | – | 2.145 | 2.340 | 2.535 | 0.717 (2026–27) / 0.686 (2028–30) |
| HR flat ≥600 mm | 7208 | 2.428 | (C) | 2.671 | 2.914 | 3.156 | 1.370 (C); 0.481 (D); 0.072 (E) |
| Cold-rolled / coated flat | 7209 / 7210 | 2.510 | (C) | 2.761 | 3.012 | 3.263 | — |
| Wire rod | 7213 | 2.310 | (C) | 2.541 | 2.772 | 3.003 | 1.364 (C); 0.475 (D); 0.066 (E) |
| Rebar | 7214 20 00 (and 7214 99) | 2.310 | (C) | 2.541 | 2.772 | 3.003 | 1.364 (C) |
| Forged bars | 7214 10 00 | 3.087 | (C) | 3.396 | 3.704 | 4.013 | 1.629 (C) |
| Semi-finished (billets) | 7207 (most codes) | 2.310 (3.087 for some 8-digit codes) | (C) | — | — | — | 1.364 (C) |
| Seamless pipe (non-stainless) | 7304 19 / 23 / 29 / 31 / 39 / 90 | 2.340 | (C) | 2.574 | 2.808 | 3.042 | 1.383 (C) for 7304 19 |
| Seamless stainless | 7304 11 / 22 / 24 / 41 / 49 | 5.690 | – | — | — | — | — |
| Welded pipe >406.4 mm | 7305 | 2.182 | (C) | 2.400 | 2.618 | 2.837 | 1.458 (C) for 7305 11 00 |
| Welded tubes (non-stainless) | 7306 19 00, 7306 30 xx, etc. | 2.244 | (C) | 2.468 | 2.693 | 2.917 | 1.458 (7306 19); 1.491 (7306 30 41) |
| Welded stainless | 7306 11 / 21 / 40 / 61 10 / 69 10 | 5.920 (7306 40 80: 5.850) | – | — | — | — | — |
| Structures | 7308 | 5.520 | (C) | — | — | — | — |
| Unwrought aluminium | 7601 | 1.700 | (K) | 1.870 | 2.040 | 2.210 | 1.423 (K); 0.091 (L) |
| Al bars/profiles | 7604 | 3.741 | (K) | — | — | — | e.g. 1.493 (K), 7604 21 |
| Al plates/sheets | 7606 | 2.714 | (K) | — | — | — | — |
| Urea >45 % N | 3102 10 19 | 1.510 (1.440 + 0.080) | – | 1.525 | 1.525 | 1.525 | 0.902 |
| Ammonium nitrate | 3102 30 90 | 2.600 (2.530 + 0.070) | – | 2.626 | 2.626 | 2.626 | 0.767 |
| AN in solution | 3102 30 10 | 1.690 | – | 1.707 | 1.707 | 1.707 | 0.508 |
| CAN ≤28 % N | 3102 40 10 | 2.230 | – | 2.252 | 2.252 | 2.252 | 0.688 |
| UAN solution | 3102 80 00 | 1.640 | – | 1.656 | 1.656 | 1.656 | 0.625 |
| Anhydrous ammonia | 2814 10 00 | 2.270 | – | 2.293 | 2.293 | 2.293 | 1.522 |
| Nitric acid | 2808 00 00 | 2.720 | – | 2.747 | 2.747 | 2.747 | 0.582 |
| Hydrogen | 2804 10 00 | 10.820 | – | 11.902 | 12.984 | 14.066 | 5.089 |

The full list is in `tr_default_values_IR2026_1740.csv`. The fallback cement values were checked in both IR 2025/2621 ("Grey clinker … 1,410 … 1,551 1,692 1,833") and IR 2026/1740.

Other Türkiye factors in IR 2025/2621 [VERIFIED]:
- Grid factor for indirect emissions (Annex II): **0.420 tCO2/MWh**.
- Default for imported electricity (Annex III): **0.718 tCO2/MWh**. This is a fossil-based factor (the EU figure is 0.612). COM(2025) 989 would switch it to an all-sources grid average.

### 6.3 Interpretation [PARTIAL]

- **Steel.** Türkiye's steel defaults carry route (C), BF/BOF, and are about 2.3 tCO2/t for long products. Türkiye produces about 72 % of its crude steel by EAF (section 9). The defaults are therefore far above an EAF mill's direct emissions; the EU scrap-EAF process benchmark is 0.065 t/t for semis plus 0.038 for rolling. EAF exporters have a strong incentive to use verified actual values.
- **Cement.** Türkiye has **no country-specific clinker or cement default**, so the "Other countries" value (top-10 average) applies.
  - Türkçimento (ZKG 03/2026) confirms that "no country-specific default value has been defined for Turkey". It reports members' actual grey-clinker emissions of about 0.88 tCO2/t, against the 1.551 default.
  - Source: https://www.zkg.de/en/artikel/t-rk-imento-addresses-fair-competition-practices-for-cbam-83238.html
- **Revision.** The Commission's December 2025 note on default values names Turkey among countries whose values could change, including in primary aluminium (Eurometal, 10.12.2025). Source: https://eurometal.net/eu-commission-looks-to-update-methodology-for-cbam-default-values-after-industry-concerns/

### 6.4 Net certificates per tonne using Türkiye defaults [PARTIAL – my calculation from VERIFIED inputs; CSCF = 1]

net = DV×(1+mark-up) − CF_y×BM. Full table: `tr_net_obligation_defaults_2026_2034.csv`.

| Good | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 |
|---|---|---|---|---|---|---|---|---|---|
| Rebar/wire rod (law) | 1.211 | 1.476 | 1.775 | 1.946 | 2.301 | 2.471 | 2.642 | 2.812 | 3.003 |
| Rebar (COM(2026) 616) | 1.211 | 1.476 | 1.755 | 1.898 | 2.198 | 2.348 | 2.492 | 2.635 | 2.798 |
| HR flat 7208 (law) | 1.335 | 1.612 | 1.923 | 2.095 | 2.451 | 2.622 | 2.793 | 2.965 | 3.156 |
| Seamless 7304 19 (law) | 1.226 | 1.494 | 1.797 | 1.970 | 2.330 | 2.503 | 2.676 | 2.848 | 3.042 |
| Welded 7305 (law) | 0.979 | 1.233 | 1.524 | 1.707 | 2.086 | 2.268 | 2.450 | 2.632 | 2.837 |
| Welded 7306 19 (law) | 1.047 | 1.308 | 1.605 | 1.787 | 2.166 | 2.349 | 2.531 | 2.713 | 2.917 |
| Al 7601 (law) | 0.483 | 0.688 | 0.929 | 1.107 | 1.477 | 1.655 | 1.833 | 2.011 | 2.210 |
| Grey clinker (law) | 0.902 | 1.059 | 1.234 | 1.317 | 1.490 | 1.573 | 1.657 | 1.740 | 1.833 |
| Grey cement (law) | 0.935 | 1.095 | 1.273 | 1.356 | 1.529 | 1.612 | 1.696 | 1.779 | 1.872 |
| Urea (law) | 0.646 | 0.668 | 0.713 | 0.826 | 1.061 | 1.173 | 1.286 | 1.399 | 1.525 |
| Ammonium nitrate (law) | 1.878 | 1.897 | 1.936 | 2.032 | 2.231 | 2.327 | 2.423 | 2.519 | 2.626 |

Worked example: rebar imported in Q1 2026 on defaults costs 1.211 × €75.36 ≈ €91 per tonne. In 2034 at €85/t it would cost 3.003 × 85 ≈ €255 per tonne under current law.

---

## 7. Downstream extension and anti-circumvention

### 7.1 Proposal COM(2025) 989 final, 17.12.2025 (procedure 2025/0419(COD)) [VERIFIED text]

**Scope and timing.**
- Annex I gets a new "Combined metal products" table. It covers machinery, motors, electrical conductors, washing machines and refrigerators, vehicles (8704, 8706 chassis, 8707 bodies, 8708 parts), furniture (9401/9403) and prefabricated buildings.
- The iron and steel table gains 7312 10, 7314 39 00, 7320 20 89, 7320 90 90, 7323 94 00, 7323 99 00 and 7325.
- My extraction gives 114 new line items (some at 6-digit or "ex" level). The Commission speaks of "180 additional CN" (financial statement). The Ministry of Trade slide gives "180 ÜRÜN – ORTALAMA % 79 DEMİR-ÇELİK ALÜMİNYUM GİRDİSİ" by category: vehicles 39, machinery 34, metal articles 28, vehicle parts 21, appliances 18, construction/lifting 17, engines 7, electrical 6, medical 5, agricultural 5.
- Article 2: Art 1(21) (the Annex I scope extension) and Art 1(24) (Annex VIII, pre-consumer scrap) apply **from 1 January 2028**. Points 1 and 6 of Annex II (the electricity rules) would apply from 1 January 2026.
- List: `cbam_downstream_proposal_COM2025_989.csv`.

**Anti-circumvention measures.**
- Pre-consumer steel and aluminium scrap (ex 7204, ex 7602) becomes a precursor in a new Annex VIII.
- A new circumvention practice is added to Art 27(2)(c): "artificially adjusting the supply chains to make the goods benefit from lower default values".
- The Commission is empowered (delegated acts) to set extra evidence requirements on place and time of production, where "sufficient evidence pointing towards a high risk of abusive practices" exists for given CN codes and origins. Such acts must be adopted within 3 months of that finding.
- A definition of "abusive practices" is added (Art 3(35)).
- The Commission is empowered to require reporting of material and chemical composition.
- New Art 27a lets the Commission temporarily remove a good from Annex I in "serious and unforeseen circumstances".

**Electricity.** The default factor becomes the weighted average CO2 intensity of all generation, and the PPA conditions are relaxed. The Ministry slide says "ELEKTRİK İÇİN VARSAYILAN DEĞERLERDE % 30 DÜŞÜŞ" (30 % fall in electricity default values).

**Companion proposal COM(2025) 990, 2025/0418(COD): Temporary Decarbonisation Fund.**
- It is financed by Member State contributions equal to 25 % of national CBAM certificate revenues.
- It supports EU producers' production in 2026–2027, with payouts in 2028–2029, to address leakage.
- Sources: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025PC0989 ; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025PC0990

### 7.2 Status on 18.10.2026

- **EP [VERIFIED]** (OEIL): ENVI vote 06.07.2026; report A10-0201/2026 tabled 09.07.2026; plenary decision 15.09.2026 (T10-0276/2026); "Matter referred back to the committee responsible for interinstitutional negotiations". Source: https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0419(COD)
- **Council [VERIFIED].** ST 10208/26 ADD 1 (11.6.2026) is titled "– General approach = Statements" for the Council meeting. The general approach was on 12.6.2026 at ECOFIN [PARTIAL for the exact date]. Source: https://data.consilium.europa.eu/doc/document/ST-10208-2026-ADD-1/en/pdf
- **Positions [PARTIAL]** (EPRS and Mayer Brown, 7.10.2026):
  - Council: about 200 products, with an annual review from 2028.
  - EP: 457 products (the comparison table says 453); it deletes Art 27a; it would include post-consumer aluminium scrap as a precursor; and it applies country defaults "from the outset" for high-risk good and origin combinations.
  - First trilogue 20.10.2026; second trilogue provisionally 30.11.2026.
  - Sources: https://eprs.europarl.europa.eu/contents/publications/EPRS/2026/09/EPRS_ATA(2026)791461.html ; https://www.mayerbrown.com/en/insights/publications/2026/10/eus-cbam-downstream-extension-and-anti-circumvention-amendments-the-road-to-trilogue

---

## 8. Türkiye's response

**Climate Law, İklim Kanunu No. 7552 [VERIFIED].** Adopted 2.7.2025; Resmî Gazete 9.7.2025, No. 32951. Source: https://www.resmigazete.gov.tr/eskiler/2025/07/20250709-1.htm
- **Art 8(1)(ç):** "Türkiye Gümrük Bölgesinde ithal edilen malların gömülü sera gazı emisyonlarını ele almak için Sınırda Karbon Düzenleme Mekanizması kurulabilir" ("A Border Carbon Adjustment Mechanism may be established to address the embedded greenhouse gas emissions of goods imported into the Turkish customs territory"). Rules are to be set by the Ministry of Trade.
- **Art 9:** the Climate Change Presidency establishes the ETS, national allocation plans and market-stability mechanisms. Art 9(6): free allocation may be based on historical emissions or benchmarks ("tarihsel emisyon verileri veya kıyaslama değerleri"). Art 9(7): allocation plans are published in the Resmî Gazete.
- **Provisional Art 1(1):** "ETS tamamen uygulanmaya başlanmadan önce pilot dönem uygulaması yapılır" ("A pilot phase is implemented before the ETS fully starts"). Its scope and duration are set by the Karbon Piyasası Kurulu (Carbon Market Board). Administrative fines during the pilot are reduced by 80 %.
- **Provisional Art 1(2):** covered operators must obtain GHG permits within 3 years of the Law's entry into force (extendable by 2 years).

**Türkiye ETS Regulation, Türkiye Emisyon Ticaret Sistemi Yönetmeliği [VERIFIED].** Resmî Gazete 27.8.2026, No. 33353; in force on publication. Source: https://www.resmigazete.gov.tr/eskiler/2026/08/20260827-7.htm
- **Scope (Art 5):** Category B installations (>50,000 to ≤500,000 tCO2e/yr) and Category C installations (>500,000 tCO2e/yr) carrying out Annex 1 (EK-1) activities.
- **Provisional Art 1:** the ETS starts with a pilot period whose scope and duration the Carbon Market Board sets.
- **Provisional Art 3:** pilot installations must submit their first monitoring methodology plans within **2 months** (about 27.10.2026), extendable by up to 6 months.
- **Provisional Art 4:** the first implementation period has two sub-periods, and benchmarks are announced in the National Allocation Plan after verification reports.
- **Pilot dates:** no Board decision found [UNVERIFIED]. Earlier draft-based press said the pilot would cover 2026–2027 emissions [PARTIAL].

**Official exposure figures.**
- Ministry of Trade presentation, 5.1.2026, published 12.1.2026 [VERIFIED; Turkish primary]. Slide "SKDM Gözden Geçirme Raporu–Türkiye" (CBAM transitional registry, Q4 2023–Q2 2025): Türkiye ranks **1st in cement, 4th in iron and steel, 1st in aluminium and 9th in fertilisers** among exporters to the EU. Actual-data use was 66 %, 82 %, 64 % and 74 % respectively. Priorities listed include "TÜRKAK'ın akreditasyonunun tanınması" (recognition of TÜRKAK accreditation) and "Varsayılan değerlerin doğruluğu" (accuracy of default values). Source: https://ticaret.gov.tr/data/695e1fdf13b8762ee85467e9/SKDM%205%20OCAK%202026.pdf
- Commission review report COM(2025) 783 (16.12.2025) [VERIFIED]: about 156 Mt of CBAM goods were imported in Q4 2023–Q2 2025. "The biggest exporters … were Ukraine and Türkiye, responsible for roughly 14% and 12% of overall mass volume". Source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025DC0783
- Minister Bolat, as reported in the İSO EU Bulletin, Jan 2026 [PARTIAL]: about **US$23 bn** of Turkish exports to the EU fall in CBAM sectors (iron and steel, aluminium, fertilisers, cement, electricity, hydrogen). Source: https://www.iso.org.tr/Sites/1/upload/files/AB_Bulteni_Ocak_2026-13310.pdf
- Study hosted on iklim.gov.tr: EBRD/MidSEFF, Climate Focus et al., "Potential Impact of the CBAM on the Turkish Economy", March 2023 [PARTIAL; dated assumptions, Scope 1+2].
  - CBAM costs: **€138 m in 2027** at €75/t, rising to **€2.5 bn per year by 2032** at €150/t (figure: €2,579 m).
  - With a domestic carbon price of €20, 2027 costs fall to €56 m.
  - With €50, 2032 costs fall to €1.08 bn, meaning about €1.5 bn is retained in Türkiye.
  - Source: https://iklim.gov.tr/db/turkce/haberler/files/20230523%20Impacts%20of%20CBAM%20on%20Turkiye%20phase%202%20report%20FV3%20(2)-sayfalar-1,3,5-16%20(1)%20(1).pdf

**EU–Türkiye dialogue.**
- COM(2025) 783 [VERIFIED] lists CBAM dialogues under the EU–Türkiye High-Level Dialogue on Trade, the High-Level Dialogue on Climate and the Customs Union Joint Committee, plus a Commission mission to Türkiye.
- 18.3.2026 working group, co-chaired by Deputy Minister M. Tuzcu and DG TAXUD's G. Thomas [PARTIAL; AA/TRT citing the Ministry]. Topics:
  - counting renewable energy in the calculations;
  - recognising verification so that actual values can be used;
  - reviewing default values for some sectors;
  - reflecting EU ETS exemptions;
  - "karbon fiyatlandırma uygulamasının SKDM hesaplamasından mahsup edilmesi" (deducting Turkish carbon pricing from the CBAM calculation).
  - Source: https://www.trthaber.com/haber/ekonomi/ticaret-bakanligi-ile-avrupa-komisyonu-arasinda-e-ticaret-ve-skdm-toplantisi-938266.html
- I found **no recognition or linking agreement** [UNVERIFIED that none exists].

---

## 9. Emission-intensity cross-checks

- **Steel production, TÇÜD 2025 [VERIFIED]:** 38.1 Mt crude steel; "72.2% … Electric Arc Furnaces", "27.8% by Integrated Plants". worldsteel *World Steel in Figures 2026* gives Türkiye Oxygen 27.8 % / Electric 72.2 % for 2025 [VERIFIED].
  - https://celik.org.tr/en/info-center/assessment/turkey-s-crude-steel-production-rises-by-3-3-to-38-1-million-tons-in-2025
  - https://worldsteel.org/wp-content/uploads/World-Steel-in-Figures-2026.pdf
- **worldsteel intensities, 2024 activity data [VERIFIED; WSIF 2026]:**
  - CO2: global average 1.92, BF-BOF 2.34, DRI-EAF 1.47, scrap-EAF 0.69 tCO2/t.
  - GHG basis: 2.18 / 2.66 / 1.66 / 0.71.
  - worldsteel's boundary includes electricity and upstream inputs, so these are not comparable to CBAM, which counts direct emissions only for steel [PARTIAL].
- **Sanity check [PARTIAL]:**
  - Türkiye's long-product default of 2.31 is close to the worldsteel BF-BOF average of 2.34. It is far above scrap-EAF direct emissions; for reference, the EU process benchmarks for scrap-EAF are 0.065 for semis and 0.038 for rolling.
  - A Sabancı IPM report, citing JRC data, gives Türkiye's weighted crude-steel intensity as about 1 tCO2/t on a Scope 1+2 basis [PARTIAL].
- **Cement [PARTIAL]:** Türkçimento reports actual grey clinker emissions of about 0.88 tCO2/t, against the fallback default of 1.410 (1.551 in 2026). The EU ETS/CBAM grey clinker benchmark is 0.666 [VERIFIED].
- **Aluminium [VERIFIED value; PARTIAL interpretation]:** the Türkiye 7601 default is 1.700 (direct plus PFC, primary route K), against the EU benchmark of 1.423. Eurometal reports stakeholder claims that some primary aluminium defaults, including Turkey's, were "very low".

---

## 10. Recommended model parameters

| Parameter | Value | Tag |
|---|---|---|
| Liability formula | Cert_y = Σ_g Q_g × [SEE_g × (1 + mk_y if default) − CF_y × CSCF_y × BM_g] − Art 9 reduction; payment = Cert × P_y | [VERIFIED] structure |
| CBAM factor CF_y, law | 0.975, 0.95, 0.90, 0.775, 0.515, 0.39, 0.265, 0.14, 0 (2026→2034) | [VERIFIED] |
| CF_y, COM(2026) 616 scenario | 0.975, 0.95, 0.915, 0.81, 0.59, 0.48, 0.375, 0.27, 0.15 (0.15 to 2037; 0 from 2038) | [VERIFIED] proposal |
| CSCF | 1.00 for 2026–2030; assume 1.00 after 2030 | [VERIFIED] / assumption |
| Mark-up on defaults | 10 % / 20 % / 30 % (2026 / 2027 / 2028+); fertilisers 1 % | [VERIFIED]; revision by Dec 2027 |
| Price 2026 | Quarterly: €75.36, €75.28, €82.32; Q4 pending (Oct running ≈ €85) | [VERIFIED] / [PARTIAL] |
| Price 2027–2034, scenario (not a forecast) | Low €70, central €85 (Oct-2026 market), high €130–150 (cf. the official 2023 study's €150 scenario) | assumption |
| Türkiye defaults | See 6.2; steel ≈ 2.2–2.4 (route C); clinker 1.410 and cement 1.440 (fallback); Al 1.700; urea 1.510; AN 2.600 | [VERIFIED] |
| Benchmarks (default path) | Rebar/wire rod 1.364; HRC 1.370; 7304 19 1.383; 7305/7306 19 1.458; Al 1.423; clinker/cement 0.666; urea 0.902; AN 0.767; NH3 1.522 | [VERIFIED] |
| Grid factor Türkiye | 0.420 (indirect); 0.718 (electricity imports) | [VERIFIED] |

## 11. Open items / caveats

- The Art 9 implementing act is still a draft. Commission default carbon prices for Türkiye do not exist yet; under Art 9(4) they are optional and available "as from 2027".
- The CSCF after 2030 and the 2031–2035 benchmarks are not set.
- Default values must be revised by December 2027. Türkiye's cement fallback could change.
- The downstream scope and COM(2026) 616 are both under negotiation.
- The consolidated IR 2025/2621 is "available soon" per the Commission.
- Turkish ETS pilot dates and the National Allocation Plan have not been published.
- ticaret.gov.tr could not be reached by scripted download. Its documents were read via WebFetch.
