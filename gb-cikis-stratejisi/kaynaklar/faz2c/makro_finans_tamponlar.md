# Türkiye makro-finansal tamponlar: notlar (GB çıkış çalışması)

Session date: 18 Oct 2026. 

**Tag key**
- [VERIFIED]: primary or official data that I read this session (CBRT/TCMB, EVDS3, HMB, SBB, IMF, BoE, ECB, Banxico).
- [DERIVED]: my own arithmetic on [VERIFIED] primary data. The method is stated each time.
- [PARTIAL]: secondary sources (press, broker reports, search snippets of official pages I could not open) or my own inference.
- [UNVERIFIED]: not confirmed.

**How I got the data.** EVDS3 is a React SPA. Its own public frontend endpoint answers without a key:
- `POST https://evds3.tcmb.gov.tr/igmevdsms-dis/fe` with a JSON body (series, startDate, endDate, frequency).
- `GET https://evds3.tcmb.gov.tr/igmevdsms-dis/serieList/fe/type=json&code=<datagroup>` for series lists.

The script that makes these calls is `scripts/evds_fetch.py`. Data groups used:
- `bie_abres2`: weekly CBRT reserves.
- `bie_ulusdovlkd`: IMF reserve template, monthly.
- `bie_abanlbil`: analytical balance sheet, daily.
- `bie_swaptektarf`: CBRT swap stocks.
- `bie_tluzvdov`: TL-settled forwards.
- `bie_hariccariacik`: current account, gold, energy.
- `bie_tukfiy2025`, `bie_oktug2025`, `bie_tukfiy2003`: CPI.
- `bie_dkdovytl`: FX rates.

HMB pages are also a SPA. I read them through the site's WordPress API (`https://www.hmb.gov.tr/portal/v2/posts?slug=...`) and the XLS files on ms.hmb.gov.tr.

The IMF PDFs return Akamai 403 to curl. I obtained them through WebFetch, copied them into `dl/imf/`, and parsed them with pdftotext.

---

## 1. Rezervler (brüt / net / swap hariç net)

### 1a. Latest official figures: CBRT "Uluslararası Rezervler ve Döviz Likiditesi", week of 9 Oct 2026 (published 15 Oct 2026) [VERIFIED]

Sources:
- Developments PDF: https://www.tcmb.gov.tr/wps/wcm/connect/8192e55e-5e96-491d-aaad-8d5f893e0f1e/URDL_Geli%C5%9Fmeleri.pdf?MOD=AJPERES
- Weekly template: https://www.tcmb.gov.tr/wps/wcm/connect/cc755e33-b5c0-4632-bfe4-2434d35da011/RT20261009TR.pdf?MOD=AJPERES
- Page: https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Odemeler+Dengesi+ve+Ilgili+Istatistikler/Uluslararasi+Rezervler+ve+Doviz+Likiditesi/

| Item (USD mn) | Sep-2026 (monthly) | 02.10.2026 | 09.10.2026 |
|---|---|---|---|
| I.A Official reserve assets (resmi rezerv varlıkları) | 166,069 | 167,388 | **171,575** |
| FX assets | 51,323 | 52,657 | 56,922 |
| Gold (incl. gold deposits/swaps); troy oz mn | 107,093 (25.567) | 107,062 | 107,008 (25.558 ≈ 795 t) |
| IMF reserve position + SDR | 7,653 | 7,669 | 7,645 (SDR 7,492) |
| II.1 FX loans, securities, deposits, outflows ≤12m | −40,015 | −40,004 | −38,530 |
| II.2 FX swaps, forward short position | −20,150 | −19,340 | **−16,473** (−185 ≤1m; −16,288 4m–1y) |
| II.3 Other (incl. gold swaps), receivable | +3,532 | +3,407 | +2,954 |
| III.1 Contingent FX liabilities (mainly banks' FX/gold RR at CBRT) | −67,823 | −67,733 | −68,706 |
| Memo: standard gold held by banks under RR | 29,181 | | 29,380 |
| Memo: reserves in non-SDR-basket currencies | 11,789 | | 11,791 |
| Memo: TL-settled FX derivatives, short position | −10 | | −4 |

Composition on 9 Oct 2026: gold 62.4%, FX 33.2%, IMF/SDR 4.5%. Gold sensitivity: 10% gold price ≈ ±$10.7bn of gross reserves.

The CBRT's own wording: the net FX liability from total foreign-currency swaps is **$16.5bn**, and net receivables from gold swaps are **$3.0bn**.

### 1b. Gross reserves path, weekly official (EVDS `TP.AB.TOPLAM`, equal to template I.A) [VERIFIED]

Full series: `data/weekly_reserves_nir.csv`.

| Date | Gross ($bn) | Note |
|---|---|---|
| 29 Dec 2023 | 141.1 | |
| 29 Mar 2024 | 123.1 | 2024 low |
| 27 Dec 2024 | 155.1 | Monthly Dec-24 template: 155.2 |
| 14 Mar 2025 | 171.1 | Before the March 2025 political shock |
| 2 May 2025 | 138.5 | 2025 low (FX part 97.1 → 57.6) |
| 17 Oct 2025 | 198.4 | |
| 26 Dec 2025 | 193.9 | Monthly Dec-25 template: 184.0. IMF GIR end-2025: 184.1. ESR: 186 |
| 30 Jan 2026 | **218.2** | Record |
| 27 Feb 2026 | 210.3 | Iran war starts 28 Feb 2026 |
| 27 Mar 2026 | 155.3 | |
| 26 Jun 2026 | **149.2** | 2026 low |
| 21 Aug 2026 | 188.4 | |
| 2 Oct 2026 | 167.4 | |
| 9 Oct 2026 | **171.6** | Latest |

Decomposition of March 2026 from the monthly template [DERIVED from VERIFIED]: official reserve assets fell **−$59.5bn**, from 210.3 to 150.8.
- FX: −24.1
- Gold quantity: −18.9 (−4.15mn oz, about −129 t sold or swapped out)
- Gold price: −16.4 (implied price $5,174 → $4,554/oz)

So intervention in March (FX plus gold quantity) was about $43bn. This is consistent with Bloomberg's "~$43.4bn, record monthly fall" (https://www.bloomberg.com/news/articles/2026-05-13/turkey-depleted-reserves-at-record-pace-in-march-over-iran-war) [PARTIAL].

Other months:
- Jun 2026: −11.8, almost all gold price.
- Sep 2026: −20.6 (FX −10.6, gold price −10.5).

USD/TRY (CBRT buying rate) [VERIFIED/DERIVED]:
- 27 Feb → 31 Mar 2026: +1.3%.
- 18 → 25 Mar 2025: +3.4%.
- End-2025 → 16 Oct 2026: 42.8623 → 49.3315, +15.1%.

The revealed reaction function is to hold the crawl and spend reserves.

### 1c. Net reserves: definitions and values

The CBRT does **not** publish a numeric "net reserves" or "swap hariç net rezerv" series. Its Inflation Reports chart "Net Rezervler" (IR 2026-III, Grafik 2.2.5) without numbers. Analysts compute it from the CBRT analytical balance sheet and the reserve template. Formulas differ, so results spread by ±5–8bn.

**(i) Press/analyst figures (AA via Yeniçağ, 15 Oct 2026)** [PARTIAL]
Source: https://www.yenicaggazetesi.com/merkez-bankas-rezervleri-yukseldi-swap-haric-net-rezerv-442-milyar-dolar-1082383h.htm and BoldMedya https://boldmedya.com/2026/10/15/merkez-bankasi-rezervlerinde-466-milyar-dolarlik-rekor-kayip/
- Week of 9 Oct 2026: gross 171.6, **net 57.7** (2 Oct: 53.8), **net excl. swaps 44.2** (2 Oct: 37.9).
- The 13.5 gap equals the template's 16.5 FX-swap legs minus 3.0 gold-swap receivables.

**(ii) Path of net excl. swaps, analyst series** [PARTIAL]

| Date | $bn | Source |
|---|---|---|
| End-Mar 2024 | −65.5 | Gedik, https://cdn.gedik.com/media/media/zbjb1p4o/gedik_yatirim_-parasal-buyuklukler-raporu_03012025.pdf |
| 27 Dec 2024 | 43.7 (net 63.6, gross 155.1) | Gedik, same report |
| 10 Oct 2025 | 61.8 (net 79.6) | Daily Sabah search snippet; page 403 |
| 28 Nov 2025 | 57.7 | Gedik |
| End-2025 | about 57.5 | Implied by Gedik 22 Jan 2026: 78.5 on 16 Jan after +21bn YTD |
| 23 Jan 2026 | 85.5 (AA) or 83 (Gedik) | Peak |
| 27 Mar 2026 | 20.2 | |
| 3 Apr 2026 | 18.4 | Trough |
| 8 May 2026 | 39.2 | |
| 22 May 2026 | 28.7 | |
| 26 Jun 2026 | 30.6 | Gedik shows 24.8 mid-June |
| 28 Aug 2026 | 55.9 | SteelRadar, https://www.steelradar.com/en/five-week-rise-in-cbrt-reserves-comes-to-an-end/ |
| 25 Sep 2026 | 40.2 | |
| 2 Oct 2026 | 37.9 | |
| 9 Oct 2026 | 44.2 | |

**(iii) My computation from the CBRT analytical balance sheet** [DERIVED]
- Formula: NIR = A.1 Dış varlıklar (TP.AB.A02) − P.1 Toplam döviz yükümlülükleri (TP.AB.A10), converted at the CBRT USD buying rate of the same day.
- Values: end-2023 27.3; end-Mar 2024 6.9; end-2024 55.2; end-2025 66.1; end-Feb 2026 83.1; end-Mar 2026 29.2; end-Jun 2026 42.8; end-Aug 2026 62.1; end-Sep 2026 51.2; **9 Oct 2026 52.3**; 15 Oct 2026 46.6.
- This runs about 5–8bn below the press "net" figure. The bankers' exact formula is not published.
- Domestic FX-swap stock of the CBRT with banks (EVDS `TP.SWAPTEKTAR.TOTALSTOKALIMYONLU`): $48.7bn (end-2023) → 0 from Jul 2024. Small blips in 2026: 12.2bn on 3 Apr 2026, 2.9bn on 2 Oct 2026, 0 on 9 Oct 2026.

**(iv) Template-based measure** [DERIVED]
- Formula: I.A + II (all ≤12m predetermined drains incl. swap legs) + III (contingent).
- Values: Dec-24 45.2; Dec-25 65.5; Jan-26 97.2; Mar-26 18.4; Jun-26 27.3; Aug-26 66.0; Sep-26 41.6; **9 Oct 2026 50.8** (weekly).
- Adding back the swap legs gives 67.3 on 9 Oct 2026.

**(v) IMF definitions (CR 26/43, Jan 2026)** [VERIFIED]
- NIR: end-2024 $65.9bn; end-2025 $75.6bn. Pre-war projections were $84.2bn (2026) and $91.2bn (2027).
- "Core NIR" = GIR less all CBRT FX liabilities incl. swaps. It was "over $50 billion" at end-2025.
- In March 2025, core reserves fell from $56.9bn on 18 Mar to $29.1bn on 25 Mar 2025.

Other domestic FX liabilities from the analytical balance sheet [DERIVED]:
- Public & other FX deposits at CBRT (A13): $12.4bn end-2024; $11.1bn end-2025; $5.9bn end-Jun 2026; **$7.25bn on 9 Oct 2026**.
- Banks' FX deposits at CBRT (A14): $99.8bn on 9 Oct 2026.
- External liabilities (A11): $14.5bn.

**Context for 2026** [PARTIAL unless noted]
- US/Israel attack on Iran on 28 Feb 2026; Hormuz disruption and oil shock (IR 2026-III and OVP mention "ABD/İsrail-İran Savaşı") [VERIFIED].
- May 2026: court ruling removing the CHP leader; about $7bn of sales (Turkish Minute, https://www.turkishminute.com/2026/05/29/turkish-central-bank-sold-7-bn-in-foreign-currency-as-removal-of-chp-leader-iran-war-hit-lira/).
- Sep 2026: investment-fund turmoil. The Capital Markets Board (SPK) ordered 131 funds liquidated, with more than $18bn in assets. BIST −8% in a week (https://www.turkishminute.com/2026/09/25/turkeys-central-bank-reserves-fall-4-3-billion-amid-fund-turmoil/). The CBRT eased TL liquidity on 17 Sep 2026 (DUY2026-41) [VERIFIED].
- Turkish holdings of US Treasuries reportedly fell from $15.72bn (end-Feb) to $1.78bn (end-Mar 2026), per TIC as reported by Turkish Minute/Bloomberg: https://www.turkishminute.com/2026/05/21/turkeys-us-treasury-holdings-plunge-as-central-bank-defends-lira-report/

### 1d. CBRT IR 2026-II, Box 2.1 "Dışsal Şok Dönemlerinde Döviz Talebi" (14 May 2026) [VERIFIED]

Source: https://www.tcmb.gov.tr/wps/wcm/connect/434cf25f-fa4b-485e-ac6d-19d2d68d87e3/enf_26_ii_tam.pdf?MOD=AJPERES

- **Non-residents accounted for 70.2% of net FX demand in the Mar–May 2025 shock and 71.5% in the Feb–Apr 2026 shock.** Residents accounted for 29.8% and 28.5%.
- 2026 corporate demand: energy 56%, gold sector 36%.
- 2026 individual demand: 95% precious metals.

### 1e. IMF Box 1, March 2025 episode (CR 26/43) [VERIFIED]

- Foreigners liquidated about **$18bn of lira assets in two weeks**, including 70% of their carry positions.
- Residents withdrew about **$19bn of lira deposits** (5%).
- Lira −4% on 19 Mar.
- The IMF also estimates non-resident financial assets (FX deposits, equities, government bonds) at about **$80bn**, as of 12 Nov 2025. Its chart splits this roughly into equities 31, government debt 16, TL deposits 11, FX deposits 22. Carry positions come on top.
- Domestic lira deposits are about $350bn.

---

## 2. Bilateral swap lines (CBRT announcements) [VERIFIED unless noted]

USD equivalents use CBRT rates of 16 Oct 2026 (CNY 7.3309, KRW 0.0365, KZT 0.1083, AED 13.3562, USD 49.3315 TRY) [DERIVED].

| Counterparty | Size | ≈USD | Signed / renewed | Term / expiry | Source |
|---|---|---|---|---|---|
| Qatar Central Bank | QAR/TRY equiv. of **$15bn** (raised from $5bn) | 15.0 | Original 17 Aug 2018; amended 20 May 2020 | Dec-2021 three-year extension per foreign ministries' joint statement [PARTIAL]; **current status/expiry not published by CBRT [UNVERIFIED]** | DUY2020-29 https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Duyurular/Basin/2020/DUY2020-29 |
| PBoC (China) | **CNY 35bn / TRY 189bn** | ≈5.2 | Renewed 13 Jun 2025 (raised to CNY 35bn on 15 Jun 2021) | 3 years → about Jun 2028, extendable | DUY2025-36 https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Duyurular/Basin/2025/DUY2025-36 |
| CBUAE (UAE) | **AED 18bn / TRY 198bn** | ≈4.9 | New agreement 2 Oct 2025 (first one 19 Jan 2022, AED 18bn/TRY 64bn, 3 years) | Term not stated in the 2025 release [UNVERIFIED] | DUY2025-52; DUY2022-04 |
| Bank of Korea | **KRW 2.3tn / TRY 56bn** | ≈1.7 | Renewed 12 Aug 2024 (first 12 Aug 2021) | 3 years → Aug 2027 | DUY2024-43 |
| National Bank of Kazakhstan | **KZT 423bn / TRY 28bn** | ≈0.9 | 24 Apr 2025 | 3 years → Apr 2028 | DUY2025-27 |
| Japan (BoJ) | **none found** | | | | CBRT press-release titles 2020–2026 scanned. Only MoUs with SAMA (2024-49), Oman, etc. |

- Total notional is about **$27.7bn** [DERIVED].
- Drawn amounts are not published by counterparty. The template's swap forward short position in the 4m–1y bucket was $16.3bn on 9 Oct 2026, stable since Apr 2026 (≈19.5bn early 2025, 17.1bn end-2025). This indicates most bilateral lines are already drawn and inside gross reserves [DERIVED/PARTIAL].
- The IMF ESR 2026 notes that non-SDR-basket currencies are about 16% of FX reserves (end-2025) and calls reserve quality an issue [VERIFIED].
- A domestic tool with the same role: TL-settled forward FX sales at the CBRT (DUY2026-10, 1 Mar 2026). The position peaked at **$9.6bn on 11 Jun 2026** and was **$4mn on 16 Oct 2026** (EVDS `TP.TLUZVADDOV.S3`). Earlier peaks: $4.3bn (Mar 2024), $2.3bn (Mar 2025) [VERIFIED].

---

## 3. External debt, financing needs, IMF reserve adequacy

**Short-term external debt (CBRT, July 2026, published about 17 Sep 2026)** [VERIFIED]
Sources: https://www.tcmb.gov.tr/wps/wcm/connect/2d8fcd41-aef8-4282-af32-59df600a0360/KVDB_AylikGelismeler.pdf?MOD=AJPERES ; tables https://www.tcmb.gov.tr/wps/wcm/connect/5bf5b69f-2828-4c03-b3aa-39766325bb65/kv.pdf?MOD=AJPERES
- By original maturity: **$177.1bn**.
- **By remaining maturity: $248.1bn**:
  - CBRT 23.1
  - General government 13.4 (central govt 12.8)
  - Banks 114.6 (loans 46.6, FX deposits of non-residents 21.6, bank deposits 19.8, TL deposits 26.6)
  - Other sectors 97.0 (trade credits 65.8, other loans 31.2)
- By borrower: public 64.5 (incl. public banks 46.7), CBRT 23.1, private 160.5.
- Currency composition of original-maturity STED: USD 34.3%, EUR 26.5%, TRY 26.0%, other 13.2%.
- August data was not yet out on 18 Oct.
- Ratios [DERIVED]: gross reserves / STED by remaining maturity = **171.6 / 248.1 = 69%**. Net excl. swaps / STED = 18%.

**IMF 2025 Article IV (Country Report 26/43, staff report dated 26 Jan 2026; Board 6 Feb 2026; PR 26/047, 13 Feb 2026)** [VERIFIED]
Sources: report PDF https://www.imf.org/-/media/files/publications/cr/2026/english/1turea2026001-source-pdf.pdf ; PR https://www.imf.org/en/news/articles/2026/02/13/pr-26047-turkiye-imf-executive-board-concludes-2025-article-iv-consultation
- "At end-2025, gross international reserves were around **80 percent of the Fund's ARA metric**, with most of the improvement driven by increases in gold prices. Core reserves, at over $50 billion…"
- Table rows, ratio to ARA (EM metric): 2024 73.3; 2025 79.5; 2026p 80.2; 2027p 79.1; 2028p 75.4; 2030p 70.2.
- GIR projections: 190.5 (2026), 197.5 (2027).
- The PR adds: "reserves expected to stay at around 80 percent of the IMF's adequacy metric".
- **Gross external financing requirements** (Table 3, pre-war):
  - 2025: $259.7bn (16.5% of GDP)
  - **2026: $286.3bn (18.2%)**
  - **2027: $292.4bn (18.3%)**
  - 2026 components: CA 22.3, government eurobond amortization 12.5, medium/long-term amortization 51.3, short-term amortization 200.2.
- Short-term external debt by remaining maturity, % of GDP: 16.8 (2025), 17.3 (2026p).

**IMF External Sector Report 2026, Ch.2 Table 2.28 Türkiye (29 Jul 2026)** [VERIFIED]
Source: https://www.imf.org/-/media/files/publications/esr/2026/english/ch2.pdf
- GIR $186bn at end-2025, up from $156bn at end-2024.
- "73 percent of the IMF's ARA metric at end-Dec 2024 (de facto crawl-like) … rose to **78.7 percent by end-2025** — still below the recommended 100 to 150 percent range."
- "Significant reserves buildup is needed, but the accumulation of reserves should be opportunistic."
- Reserve quality is an issue (swaps, non-SDR currencies about 16%).
- Gross external financing needs **about 18% of GDP on average 2026–31**.
- REER overvalued 12.1% (range 9.8–14.4). CA gap −2.9% of GDP.
- External debt 32.6% of GDP, of which 32.2% short-term.
- Nonfinancial corporates' net FX position −$188bn (short-term +$11.7bn).
- Implied ARA metric ≈ GIR / 0.787 ≈ **$236bn** [DERIVED]. A search snippet claiming "102.9% of ARA" was wrong; the PDF text shows 78.7%.

**My adjustment for the 2026–27 financing need** [PARTIAL/DERIVED]
- The OVP 2027–29 now projects a CA deficit of $47.5bn (2026) and $38.5bn (2027), against the IMF's $22.3bn and $23.1bn.
- Replacing the IMF CA line gives GEFR of about **$311bn (2026)** and **$308bn (2027)**, about 17% of GDP.
- A simple 12-month proxy: STED by remaining maturity (248.1) plus the 12-month CA deficit (42.1) ≈ $290bn.

---

## 4. Public debt (HMB) [VERIFIED unless noted]

**Central government debt, 31 Aug 2026 (released 21 Sep 2026)**
Source: https://www.hmb.gov.tr/duyuru/31-agustos-2026-tarihi-itibariyla-merkezi-yonetim-borc-stoku (read via API https://www.hmb.gov.tr/portal/v2/posts?slug=31-agustos-2026-tarihi-itibariyla-merkezi-yonetim-borc-stoku) and XLS https://ms.hmb.gov.tr/uploads/2026/09/Merkezi_Yonetim_Borc_Stoku_Doviz-Faiz_Yapisi-b67115a66629e0bf.xls
- Total TRY 15,893.8bn: TL TRY 7,748.0bn; **FX-denominated TRY 8,145.8bn = 51.3%**.
- Domestic TRY 9,545.4bn; external TRY 6,348.5bn. Domestic FX/gold-linked about TRY 1.8tn.
- FX share path [DERIVED from monthly HMB releases]: end-2022 65.5%; end-2023 64.2%; end-2024 56.1%; end-2025 53.1% (7,249.2 / 13,656); Aug 2026 51.3%.
- The FX share includes gold-linked instruments, per HMB's TL/FX split.

**Average maturity of domestic cash borrowing**
Source: XLS https://ms.hmb.gov.tr/uploads/2026/10/Ic-Borclanmanin-Ortalama-Vadesi-bd2aca28e5ffe8dd.xls (saved 8 Oct 2026)
- 2023: 65.1 months; 2024: 47.8; 2025: 33.0.
- **2026 Jan–Sep cumulative: 32.2 months.** Single month Sep 2026: 51.2.
- HMB statement of 26 Feb 2026 confirms 65.1 → 33.8 months (Jan 2026). Composition of 2025 borrowing: TLREF 20.9%, FX-denominated 14.5%, gold 5.5%, 5-year fixed 14.2%, 10-year fixed 1.9%.

**Average time to maturity of the stock (Aug 2026)**: domestic 2.5 years; external 6.3; total 4.0.
Source: https://ms.hmb.gov.tr/uploads/2026/09/Merkezi_Yonetim_Borc_Stokunun_Vadeye_Kalan_Ortalama_Suresi-105e4c1dd29ebf81.xls

**Central government external debt service, projection of 1 Sep 2026** ($bn)
Source: https://ms.hmb.gov.tr/uploads/2026/09/Merkezi_Yonetim_Dis_Borc_Odeme_Projeksiyonlari_Yillik-c30bd35d792a1386.xlsx
- Sep–Dec 2026: 3.7 principal + 2.0 interest = 5.7
- **2027: 12.8 + 7.3 = 20.1**
- 2028: 11.1 + 6.5 = 17.7

**General government debt (EU definition) and net debt, 30 Jun 2026** (HMB release 30 Sep 2026)
- EU-defined general government debt: TRY 16,273bn = **22.3% of GDP** (end-2025: 23.8%).
- Public net debt: TRY 10,046bn = 13.8% of GDP.
- Net debt XLS: https://ms.hmb.gov.tr/uploads/2026/09/Kamu_Net_Borc_Stoku-d309439a1a47fc92.xls

**Treasury FX deposits**: HMB does not publish a standalone series. Best proxy: CBRT analytical balance sheet "Kamu ve Diğer Döviz Mevduatı" (A13) = **$7.25bn on 9 Oct 2026**, $11.1bn end-2025, $12.4bn end-2024 [DERIVED; covers public and "other", so it is an upper bound].

**2026 external market issuance**: **$12.2bn** by 24 Sep 2026 (HMB releases on ms.hmb.gov.tr)
- 14 Jan: $2bn 2033 at 6.35% and $1.5bn 2038 at 6.90%
- 10 Feb: €2bn 2034 at 5.20% (MS+242bp)
- 22 Apr: $2bn 2031 at 6.40%
- 2 Jul: $2.75bn 6-year sukuk at 6.75%
- 30 Sep: $1.5bn ESG 2037 at 7.65%
- Sources: https://ms.hmb.gov.tr/uploads/2026/01/20260107_Basin_TR-51a124d55d1b113a.pdf … https://ms.hmb.gov.tr/uploads/2026/09/20260924_Basin-Duyurusu-6143c30a7872a848.pdf

**Domestic gold mobilization**: Treasury gold bonds and gold lease certificates sold to institutional investors in 2026 YTD total **145.2 t** (8 issues, 26 Jan – 5 Oct 2026, maturities 2027–28) (HMB posts, e.g. 5 Oct 2026) [VERIFIED]. The effect on CBRT reserves is not published [PARTIAL].

---

## 5. Inflation, policy, targets, pass-through

**CPI (TÜİK via EVDS, 2025=100; computed y/y)** [VERIFIED]
- Sep 2026: **29.73% y/y, 1.84% m/m**. Aug 2026: 31.50% (OVP text: 31.51%). Core C: 28.71% y/y.
- Press confirms the TÜİK release of 5 Oct 2026: https://gazeteoksijen.com/ekonomi/eylulde-enflasyon-yillik-yuzde-29-73-aylik-yuzde-1-84-oldu-291680 [PARTIAL].
- End-2025: 30.9%.

**Policy rate** [VERIFIED]
- One-week repo **37%**; overnight lending 40%; overnight borrowing 35.5%.
- Cut from 38% on 22 Jan 2026 (DUY2026-01).
- Held on 12 Mar, 22 Apr, 11 Jun, 23 Jul and **10 Sep 2026** (DUY2026-38, https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Duyurular/Basin/2026/DUY2026-38).
- One-week repo auctions were suspended 1 Mar 2026 (DUY2026-11) and resumed 23 Aug 2026 (DUY2026-35). IR 2026-III says the weighted average funding cost was kept at about 40%.
- FX reserve requirements raised to 32% (demand and up to 1 month) and 28% (longer), effective 17 Jul 2026 (DUY2026-26).
- Next MPC: 22 Oct 2026 [PARTIAL, press calendar].

**Targets (IR 2026-III, 13 Aug 2026)** [VERIFIED]
Source: https://www.tcmb.gov.tr/wps/wcm/connect/740c52dd-06ee-4270-84c1-6d1ff0e7f3a6/enf26_iii_tam.pdf?MOD=AJPERES
- Interim targets: **2026 24%, 2027 15%, 2028 9%**. Medium-term target 5%.
- CBRT forecasts: 28% / 15% / 9%. Forecast ranges suspended since IR 2026-II.
- OVP 2027–29 CPI path: 28.4 / 21 / 13.5 / 9.
- IMF (Jan 2026): 23 / 19 / 15.

**Pass-through** [VERIFIED]
- CBRT IR 2023-III Box 2.5 (https://www.tcmb.gov.tr/wps/wcm/connect/af64cb46-5d4b-4f36-8bcc-a4a7534fbced/Kutu_2.5_2023_iii..pdf?MOD=AJPERES): cost-channel pass-through is about **25% over one year**. "A 10% rise in the FX basket → about **2.5 pp** CPI within a year", controlling for expectations. The estimate is higher when the expectations channel is not separated. Pass-through has risen since 2018 and accelerated from 2020.
- CBRT blog (Kara, Öğünç, Özmen, Sarıkaya, 20 Jan 2017, https://tcmbblog.org/wps/wcm/connect/blog/en/main+menu/analyses/exchange+rate+pass-through): about 15% on average after one year; about 25% when the economy is overheating; below 10% in slack; higher when depreciation is expected to persist.
- **The study's 250bp per 10% is the CBRT's central cost-channel estimate.** It could be an underestimate if expectations de-anchor [PARTIAL inference].

---

## 6. Access to IMF and BIS; precedents

**IMF** [VERIFIED]
- Türkiye's quota is **SDR 4,658.6mn** (https://www.imf.org/en/countries/tur), about $6.31bn at USD/SDR 1.3539 (CBRT, 16 Oct 2026).
- Normal GRA access limits are **200% of quota per year and 600% cumulative** (PR 24/499, Dec 2024; https://www.imf.org/en/news/articles/2024/12/23/pr24499-imf-exec-board-concludes-2024-comprehensive-rev-general-resources-account-access-limits). That is about SDR 9.3bn ≈ **$12.6bn a year** and SDR 28bn ≈ $37.8bn cumulative [DERIVED]. Exceptional access is possible with conditionality.
- FCL and SLL criteria include "low, stable inflation" and comfortable reserves (factsheet, updated Apr 2025: https://www.imf.org/en/About/Factsheets/Sheets/2023/Flexible-Credit-Line-FCL). With 29.7% CPI and reserves at about 79% of ARA, **Türkiye does not qualify** [DERIVED].
- PLL is unlikely. The realistic options are an SBA or EFF (conditional, politically costly) or the RFI. The RFI limit of about 50% of quota per year is [UNVERIFIED].
- Last Article IV Board: 6 Feb 2026. Türkiye has no IMF arrangement now. SDR holdings of $7.49bn are usable.

**BIS** [VERIFIED]
- The CBRT has been a member since 1951: 8,000 shares, SDR 40mn, 1.5% of BIS capital (https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/About+the+Bank/International+Relations/Central+Banks+Relations+with+International+Institutions).
- Reserves held with "other central banks, BIS and IMF": $32.6bn (template, 9 Oct 2026).
- BIS short-term credit and gold services to member central banks exist, but terms are confidential [UNVERIFIED].

**Fed FIMA repo**: it needs US Treasury collateral. Reported Turkish UST holdings were $1.78bn at end-Mar 2026 [PARTIAL]. Rebuilding UST holdings would restore this channel.

**Precedents**
- **UK 2016** [VERIFIED]: BoE, 7 Mar 2016, announced three extra ILTR operations "in the weeks around the EU Referendum" (14, 21 and 28 Jun 2016) and kept weekly USD repo running (https://www.bankofengland.co.uk/news/2016/march/additional-indexed-long-term-repo-operations-7-march-2016).
- **UK 2019** [VERIFIED]: ECB and BoE activated their standing swap line, with weekly BoE euro lending, as a "prudent and precautionary step" (5 Mar 2019, https://www.ecb.europa.eu/press/pr/date/2019/html/ecb.pr190305~be78defb5c.en.html). Liquidity backstops were the UK's focus; it did not build FX reserves.
- **Mexico 2017** [VERIFIED]:
  - The FX Commission (SHCP–Banxico) on 21 Feb 2017 announced **peso-settled FX hedges (NDFs) up to $20bn**, auctioned by Banxico.
  - 25 Oct 2017: +$4bn explicitly citing **NAFTA renegotiation** uncertainty.
  - By 26 Dec 2017: $5bn auctioned plus $0.5bn that day, with all maturities rolled.
  - Sources: https://www.banxico.org.mx/publicaciones-y-prensa/anuncios-de-la-comision-de-cambios/%7B85FE0A45-F8B4-1D02-7F5D-12DDD33A360B%7D.pdf and …%7BC52A69B2-3AC4-4A51-6C17-FF669B3AE773%7D.pdf
  - In parallel, the IMF renewed Mexico's FCL at **SDR 62.39bn (about $88bn)** for two years on 29 Nov 2017, treated as precautionary and citing the risk of an "abrupt change in Mexico's trade relations" (PR 17/459, https://www.imf.org/en/News/Articles/2017/11/30/pr17459-mexico-imf-executive-board-approves-new-two-year-us-88-billion-fcl-arrangement).
  - The peso settlement meant no reserves were used (imcp summary) [PARTIAL].
- **Canada 2018** [PARTIAL]: no shock-specific FX pre-funding was found. Canada relied on standing buffers:
  - Exchange Fund Account liquid FX ≥3% of nominal GDP: US$81.2bn at 31 Mar 2018 (canada.ca reserves report and Statement of Investment Policy; the site would not download).
  - Permanent standing swap lines with Fed, ECB, BoE, BoJ and SNB since 31 Oct 2013 (Fed release https://www.federalreserve.gov/newsevents/pressreleases/monetary20131031a.htm; the ECB 2019 release confirms the network) [ECB part VERIFIED].
- **Türkiye analog** [VERIFIED]: the CBRT's TL-settled forward sales since 1 Mar 2026 peaked at $9.6bn, which is the same instrument as Banxico's.

---

## 7. Current account and OVP

**CBRT BoP, August 2026 (released 12 Oct 2026)** [VERIFIED]
Source: https://www.tcmb.gov.tr/wps/wcm/connect/549c1316-4b5b-444a-b368-357963e576a6/%C3%96demelerDengesi_A%C4%9Fustos2026.pdf?MOD=AJPERES
- August CA: **+$4.05bn**. Excluding gold and energy: +$8.2bn.
- **12-month CA deficit: about $42.1bn**.
- 12-month components: BoP-defined trade −78.4; services +63.9; primary income −25.6; secondary income −1.9.
- 12-month financing: portfolio +5.5, loans +47.1, trade credits +0.5; derivatives −4.8, net FDI −0.9, currency & deposits −17.7. **CBRT FX net reserve decrease $30.1bn.**
- Official reserves +$7.1bn in August.

**12-month sums to Aug 2026 (EVDS `bie_hariccariacik`)** [VERIFIED/DERIVED]
- Energy (ch. 27) net −$51.9bn; non-monetary gold net −$16.2bn.
- CA ex-gold −$25.9bn; ex-energy +$9.8bn; ex-gold & energy +$26.0bn.
- The 12-month deficit was −23.8bn in Aug 2025 and −30.3bn in Dec 2025, then widened through the war shock.

**OVP 2027–2029 (Resmi Gazete mükerrer, 6 Sep 2026)** [VERIFIED]
Source: https://www.sbb.gov.tr/wp-content/uploads/2026/09/Orta-Vadeli-Program-2027-2029.pdf (digit glyphs decoded with `scripts/ovp_decode.py`)

| Item | 2025 | 2026GT | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|
| CA ($bn) | −30.3 | −47.5 | −38.5 | −37.0 | −35.5 |
| CA (% GDP) | −1.9 | −2.6 | −1.9 | −1.8 | −1.6 |
| Ex-gold CA ($bn) | −10.3 | −34.0 | −23.5 | −20.5 | −18.0 |
| Energy imports ($bn) | 62.5 | 71.0 | 66.0 | 63.5 | 61.0 |
| Brent ($/bbl) | 69.1 | 88 | 76 | 72 | 67 |
| GDP ($bn) | 1,602 | 1,821 | 1,984 | 2,091 | 2,225 |
| Growth (%) | 3.7 | 3.3 | 4.2 | 4.6 | 5.0 |
| CPI year-end (%) | 30.9 | 28.4 | 21 | 13.5 | 9 |

- **No numerical reserve target in the OVP.** The narrative cites gross reserves of $188.2bn on 28 Aug 2026 and states that KKM is fully wound down. Individual KKM balances reached zero in Aug 2026 and corporate balances were zero from Dec 2025. The TL share of deposits was 61.5% on 28 Aug 2026, and CDS stayed below 220bp in Aug 2026.

---

## 8. Assessment: how large an FX buffer an exit announcement would need

**Assumptions** (my judgment, [PARTIAL])
1. The announcement acts like the two recent stress episodes, but is larger and more persistent. It is a confidence and carry-unwind shock first; trade effects come later during the transition. About 70% of net FX demand comes from non-residents (CBRT Box 2.1).
2. The CBRT keeps its revealed reaction function: hold the crawl, tighten liquidity, and spend reserves. In March 2026, about $43bn of FX and gold intervention kept USD/TRY at +1.3% for the month.
3. Each 10% of depreciation that is not prevented adds about 250bp to CPI (CBRT). That pushes end-2027 CPI from about 15–21% toward 18–25%.
4. Gold stays about 60% of gross reserves (±$10.7bn per ±10% gold price). It is usable through swaps and sales, as with the 129 t in March 2026.

**Size of the drain over 12 months**
- Front-loaded part, first 4–8 weeks: **$50–65bn**. Calibration: March 2026 intervention about $43bn in a month, with net excl. swaps falling $65–67bn including valuation. March–April 2025: core reserves −$28bn in one week and analysts' estimate of about $50bn of FX sales.
- Non-residents: half of about $80bn of financial assets plus carry ≈ $40bn.
- Residents: 5–8% of about $350bn TL deposits ≈ $18–28bn, of which roughly half hits reserves.
- Rollover: 10–15pp lower rollover on about $125bn of bank and corporate external loans ≈ $12–18bn.
- Current account: +$10–15bn in year 1 from lost preferential EU access and weaker FDI.
- **Total about $80–100bn over 12 months.**

**Required pre-announcement buffer**
- **Net reserves excl. swaps of about $95–110bn.** That is enough to absorb the front-loaded $50–65bn and still stay above about $35–40bn; the April 2026 trough of $18bn was a stress level.
- **Contingent and off-balance-sheet capacity of about $30–40bn:**
  - Upsized or undrawn bilateral swaps; total notional today ≈ $28bn, mostly drawn.
  - TL-settled forwards, which use no reserves.
  - Treasury FX deposits raised from about $7bn to $15–20bn.
  - IMF SBA or RFI as a last resort (≈$12.6bn a year under normal access).
- **Gross reserves of about $230–240bn**, which is roughly 100% of the IMF ARA metric (≈$236bn).

**Gap today**
- Net excl. swaps: $44.2bn now → a gap of **about $50–65bn**.
- Gross: $171.6bn now → a gap of about $60–65bn.
- Pace: the CBRT rebuilt about $37bn of net excl. swaps between April and August 2026, so a $50–65bn build over 12–18 months is feasible only with sustained inflows and tight policy.

**What raises which measure**
| Action | Gross reserves | Net reserves | Note |
|---|---|---|---|
| CBRT purchases of FX and gold (opportunistic) | Up | **Up** | The only channel that raises net reserves |
| Treasury pre-funding (Eurobond, sukuk) | Up | Neutral | Pre-finances 2027 FX debt service of $20.1bn |
| Gold bonds, higher FX/gold reserve requirements | Up | Neutral | Liability is booked at the CBRT |
| Extending swap tenors past the exit horizon | – | – | Avoids rollovers during a crisis |
| Rebuilding UST holdings | – | – | Restores Fed FIMA repo access |
| Keeping TL-settled forward capacity | – | – | Hedges the market with no reserve outflow |
