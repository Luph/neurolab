# Case R reference model report: Mesa Corta Renewables (ERCOT)

Model version R-1.1, inputs file version 1.1, generated 2026-10-03. All money USD millions nominal unless stated. Every Case R price is Illustrative (Case Bible illustrative price paths; not ERCOT settlement data and not a forecast). Source of every number: `model/outputs_case_r.json`, produced by `python3 model/case_r.py`.

## 1. Assumption changes (modeler calibration, pre-publication)

The v1.0 inputs produce a base-case unlevered value for A1 of about USD 438 million against a USD 1,184.6 million price (high case about USD 611 million), a fund IRR below zero and opco debt of about USD 328 million against a 520 to 600 design range. Revenue per MW is realistic for ERCOT (West Texas wind about USD 100,000 per MW-year in 2025); the prices were not. The fix keeps every market, contract, asset and financing term and recalibrates the four acquisition prices (R-C04 to R-C08; R-C09 and R-C10 follow the editor-in-chief's yield note) to just above the model's base-case breakeven values, so the bids read as full auction prices. These are larger than 'small' changes and need editor-in-chief sign-off.

| ID | Item | Old | New | Reason |
|---|---|---|---|---|
| R-C04 | A1 enterprise value (bid price) | 1184.6 | 446.3 | v1.0 price was 2.7x the base-case breakeven value (USD 438.2m) and 1.9x the high-case breakeven (USD 611.1m) given the Bible revenue, opex and discount-rate inputs; new price is about 1.9% above the base-case breakeven (full auction price) |
| R-C05 | A2 price (Redfern Storage) | 132.4 | 63.7 | v1.0 price was 2.1x base-case value of a 100 MW/200 MWh toll asset earning USD 10.98m/yr; new price slightly above base breakeven |
| R-C06 | A3 prices (Kerrigan R7, Barlow Gap R8) | [171.9, 168.3] | [87.4, 101.9] | v1.0 prices about 1.7-2.0x base-case value including ITC transfer proceeds; new prices slightly above base breakeven |
| R-C07 | USPP series split | 30/40/30 fixed | outputs of sequential sculpted amortization by tenor | sculpted profile retires only about 63% of principal by 2037, so a 70% A+B share cannot be repaid within the B tenor |
| R-C08 | expected debt ranges (design targets) | opco TL 520-600; holdco TLB 160-210; USPP 750-860 | superseded by model outputs (see ledger R-F05, R-F08) | ranges assumed revenue about 1.7x what the Bible inputs produce |
| R-C09 | P99 one-year by asset | R1 81.2, R2 84.0, R3 80.1, R4 91.9, R5 91.4, R8 91.6 (% of P50) | R1 77.5, R2 80.4, R3 76.2, R4 90.2, R5 89.5, R8 89.8 (computed from the P90s under a normal distribution) | editor-in-chief note: v1.0 P99s were inconsistent with the normal distribution implied by the stated P90s |
| R-C10 | yield uncertainty model and inter-asset correlations (new) | none | normal; sigma split into long-term and inter-annual components; ten-year P90/P99 and correlated portfolio P50/P90/P99 computed (R-F01) | editor-in-chief note |


Supplementary assumptions where the Case Bible is silent (also on the workbook Inputs sheet):

| Item | Value | Use |
|---|---|---|
| Insurance share of base opex | 15.0% | the 22% 2023 insurance step-up applies to this share |
| R3 PTC rate 2026 to November 2029 | USD 30.00/MWh | held at the 2025 value; 99% to tax equity |
| Curtailment 2023 and 2024 | linear between 2022 and 2025 values | West wind 5.0%, 5.5%; Panhandle 5.8%, 6.4%; West solar 2.5%, 3.0% |
| Availability of wind and solar | P50 is net of long-term availability (factor 100%) | batteries: 97.5% applied to merchant revenue; toll paid in full above 97.0% |
| Yield distribution | normal; sigma split into long-term and inter-annual components | P99s recomputed from P90s (R-C09); correlations added (R-C10) |
| P50 reference year for degradation | 2022 (A1 assets), 2025 (R8) | degradation compounds from the reference year |
| Battery augmentation cost | USD 41/kWh in 2025 prices, +2.5% a year | 6% of MWh in calendar year COD+5 and COD+9 |
| Holdco coverage test years | 2023-2027 (2022 TLB); 2025-2027 (2024 incremental); 2026-2031 (2025 repricing) | full years before maturity |
| Holdco amortization | 1% a year of original face on every tranche, 50% excess cash sweep | repriced tranche keeps the sweep |
| Tax | Mesa Corta is modeled as a taxable blocker (21%); bonus and MACRS on purchase prices (85% 5-year, 10% 15-year, 5% land); ITC basis reduction 50% of credit; NOL 80% limit | fees, OID and swap unwind gains are not deducted; interest limitation not modeled; Mesa's 1% PTC share ignored |


Model conventions:

- Annual periods 2022 to 2059, first period in column J; day-count fractions for every partial year (acquisitions, COD, contract end, loan dates).
- Asset rows are 100% of each asset for its operating fraction; Mesa's share applies the owned share (from the acquisition date) and deducts tax-equity cash (R3 40% to December 31, 2029 then 5%; R5 20% to June 30, 2027 then 5%).
- Hub capture ratio follows the bucket path (low: 1.5x decline, floor 0.04 lower; high: 0.5x decline). Node capture = hub capture minus the basis. Physical sales settle at node capture; hedges and the vPPA settle at hub (R4 and R8 shape factor = solar hub capture ratio).
- Revenue buckets: contracted = R2 PPA revenue, R3 PRS fixed payment, R5 vPPA strike x volume, R6 toll, R7 floor less premium; hedged = swap and shape-hedge volume x strike; merchant = the rest (can be negative where basis is paid). CFADS is split across buckets in proportion to Mesa-share revenue.
- Debt is sized once, on the base price case at P50 with the P99 one-year test, and held fixed in every other scenario. Sculpted debt service = min(sum of bucket CFADS / bucket DSCR, P99 CFADS / P99 minimum DSCR).
- Status quo (no refinancing) case: the opco term loan continues on its sculpted notional profile to 2040 at the stepped margin (unhedged after March 22, 2029), the Redfern loan runs to 2030, holdco tranches keep 1% amortization and the 50% sweep; maturities are assumed extended like-for-like (balances at maturity are reported as refinancing requirements). Cash sweeps at opco are not applied in either case.
- Fund cash flows are gross of fund fees and carry; acquisition equity on the deal dates, distributions at December 31. Negative holdco cash is treated as an equity cure (fund contribution). NAV at December 31, 2025 = PV of later fund distributions at the levered equity rates weighted by portfolio revenue bucket shares, floored at zero.
- Bid valuations: Mesa's unlevered post-tax cash flow by asset, split by revenue bucket and discounted at the bucket rate (storage merchant rate for battery merchant revenue); all cash flows after 2040 at the 10.50% terminal rate; tax computed stand-alone (losses valued when generated); the purchase-price depreciation shield is a separate portfolio line discounted at the contracted rate. Breakeven price solves V = P in closed form because the shield is linear in price.

## 2. Circularity

There is no circular reference in the Case R model, so no iteration is needed and the workbook runs with iterative calculation off. The four places where circularity usually appears are handled as follows: (1) sculpted debt is the sum of debt-service capacity times forward discount-factor products at each year's all-in rate, DF_t = DF_{t-1} / (1 + r_t x f_t), so the debt amount follows directly; (2) USPP series sizes are solved backward from 2043, P_t = (DS_t - sum of coupons x next-year opening balances) / (1 + coupon of the series amortizing in t), which needs only later columns; (3) upfront fees, OID and transaction costs are funded by equity as the plug, so debt size does not depend on them; (4) the bid valuation's tax shield is linear in price, so the breakeven price is closed form, P* = V_pre / (1 - tax rate x PV of depreciation per dollar). Interest is charged on opening balances, so cash sweeps and taxes do not feed back into interest.

## 3. Asset yield (R-F01, R-F06)

Distribution: annual net energy is normal. One-year sigma^2 = sigma_LT^2 + sigma_IAV^2 and ten-year sigma^2 = sigma_LT^2 + sigma_IAV^2/10, where sigma_LT is long-term (measurement, model, long-term resource) uncertainty and sigma_IAV inter-annual variability. The Bible's P90 one-year and ten-year values are the anchors; P99 values follow (z = 1.2816 for P90, 2.3263 for P99). Wind and solar P50s are net of long-term availability and gross of curtailment; degradation and curtailment apply on top.

| Asset | Name | MWac | P50 GWh | sigma LT | sigma IAV | sigma 1-yr | sigma 10-yr | P90 1-yr | P90 10-yr | P99 1-yr | P99 10-yr | Net gen 2026 base (GWh) | Node capture 2026 | Node price 2026 (USD/MWh) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | Thatcher Flats Wind | 201.6 | 695.8 | 4.9% | 8.4% | 9.7% | 5.5% | 87.6% | 92.9% | 77.5% | 87.1% | 648.8 | 0.68 | 29.18 |
| R2 | Sandoval Hills Wind | 248.4 | 785.5 | 4.0% | 7.4% | 8.4% | 4.6% | 89.2% | 94.1% | 80.4% | 89.3% | 767.5 | 0.90 | 39.69 |
| R3 | Ollie Creek Wind | 153.0 | 619.2 | 5.2% | 8.8% | 10.2% | 5.9% | 86.9% | 92.4% | 76.2% | 86.2% | 571.3 | 0.57 | 24.61 |
| R4 | Peeler Draw Solar | 98.7 | 234.3 | 2.2% | 3.6% | 4.2% | 2.5% | 94.6% | 96.8% | 90.2% | 94.2% | 222.1 | 0.75 | 32.38 |
| R5 | Calloway Mesa Solar | 182.4 | 452.2 | 2.5% | 3.8% | 4.5% | 2.7% | 94.2% | 96.5% | 89.5% | 93.6% | 428.6 | 0.75 | 32.38 |
| R8 | Barlow Gap Solar | 120.0 | 290.1 | 2.4% | 3.7% | 4.4% | 2.7% | 94.4% | 96.6% | 89.8% | 93.8% | 283.7 | 0.81 | 35.71 |


Correlations: iav_wind_west_west 0.60, iav_wind_west_coastal 0.30, iav_solar_west_west 0.85, iav_solar_west_south 0.50, iav_wind_solar -0.10, lt_same_technology 0.50, lt_cross_technology 0.00.


Portfolio yield (correlated):

| Group | Horizon | P50 GWh | sigma GWh | P90 GWh | P90 % of P50 | P99 GWh | P99 % of P50 | P90 if fully correlated | P90 if independent |
|---|---|---|---|---|---|---|---|---|---|
| A1 | 1yr | 2787.0 | 154.2 | 2589.4 | 92.9% | 2428.4 | 87.1% | 89.6% | 94.7% |
| A1 | 10yr | 2787.0 | 90.9 | 2670.5 | 95.8% | 2575.6 | 92.4% | 94.0% | 97.0% |
| all_generation | 1yr | 3077.1 | 154.7 | 2878.8 | 93.6% | 2717.1 | 88.3% | 90.0% | 95.1% |
| all_generation | 10yr | 3077.1 | 91.8 | 2959.5 | 96.2% | 2863.6 | 93.1% | 94.3% | 97.2% |


Revenue build by asset, base case (USD m, 100% of asset):

| Asset | 2022 | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|---|---|---|---|
| R1 | 33.6 | 23.3 | 19.8 | 20.5 | 20.7 | 20.7 | 20.4 | 20.7 | 21.0 |
| R2 | 24.3 | 24.2 | 24.2 | 24.1 | 24.1 | 24.1 | 24.0 | 29.0 | 34.6 |
| R3 | 22.9 | 23.4 | 24.7 | 24.3 | 24.1 | 24.0 | 23.9 | 23.9 | 15.6 |
| R4 | 10.7 | 10.0 | 8.6 | 8.9 | 8.9 | 7.4 | 7.4 | 7.4 | 7.3 |
| R5 | 11.4 | 11.4 | 11.7 | 11.5 | 11.4 | 11.3 | 11.2 | 11.2 | 11.1 |
| R6 | 0.0 | 5.1 | 11.0 | 11.0 | 11.0 | 11.0 | 11.0 | 11.0 | 8.6 |
| R7 | 0.0 | 0.0 | 7.6 | 10.2 | 10.2 | 10.2 | 10.2 | 10.2 | 10.2 |
| R8 | 0.0 | 0.0 | 0.2 | 10.2 | 10.5 | 10.6 | 10.6 | 10.6 | 10.6 |
| Portfolio CFADS (Mesa share) | 45.2 | 49.2 | 56.8 | 65.9 | 65.3 | 63.2 | 61.7 | 65.2 | 66.1 |


Revenue build by asset, low case (USD m, 100% of asset):

| Asset | 2022 | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|---|---|---|---|
| R1 | 33.6 | 23.2 | 19.7 | 20.3 | 19.6 | 19.5 | 15.1 | 15.1 | 15.1 |
| R2 | 24.3 | 24.2 | 24.2 | 24.1 | 24.1 | 24.1 | 24.0 | 24.6 | 25.5 |
| R3 | 22.9 | 23.4 | 24.7 | 24.3 | 24.5 | 24.4 | 24.4 | 24.4 | 11.2 |
| R4 | 10.7 | 9.9 | 8.6 | 8.8 | 8.6 | 5.3 | 5.2 | 5.0 | 4.8 |
| R5 | 11.4 | 11.4 | 11.7 | 11.5 | 11.5 | 11.4 | 11.4 | 11.3 | 11.3 |
| R6 | 0.0 | 5.1 | 11.0 | 11.0 | 11.0 | 11.0 | 11.0 | 11.0 | 7.7 |
| R7 | 0.0 | 0.0 | 7.6 | 10.2 | 10.2 | 10.2 | 10.2 | 10.2 | 10.2 |
| R8 | 0.0 | 0.0 | 0.2 | 10.1 | 9.6 | 9.6 | 9.5 | 9.4 | 9.3 |
| Portfolio CFADS (Mesa share) | 45.2 | 49.1 | 56.7 | 65.5 | 63.2 | 59.2 | 53.6 | 52.5 | 43.1 |


## 4. Hedge book (R-F02, base)

| Year | R1 swap settlement | R3 PRS net | R4 shape settlement | R5 vPPA settlement | R6 toll | R7 floor contract | R8 shape settlement | Mesa revenue | Contracted | Hedged | Merchant |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2022 | 0.0 | (2.1) | (3.0) | (15.2) | 0.0 | 0.0 | 0.0 | 71.2 | 54.3% | 8.1% | 37.6% |
| 2023 | (3.9) | 3.3 | (1.0) | (9.6) | 5.1 | 0.0 | 0.0 | 84.4 | 63.1% | 28.8% | 8.1% |
| 2024 | 6.7 | 14.9 | 3.4 | 1.7 | 11.0 | 7.6 | 0.0 | 95.7 | 71.1% | 25.5% | 3.4% |
| 2025 | 3.4 | 11.6 | 2.2 | (1.3) | 11.0 | 10.2 | 1.0 | 108.7 | 64.8% | 28.6% | 6.6% |
| 2026 | 1.8 | 10.1 | 1.8 | (2.5) | 11.0 | 10.2 | 0.4 | 109.1 | 64.5% | 28.5% | 7.0% |
| 2027 | 0.9 | 9.3 | 0.0 | (3.0) | 11.0 | 10.2 | 0.2 | 108.3 | 65.7% | 21.9% | 12.4% |
| 2028 | 0.0 | 8.8 | 0.0 | (3.1) | 11.0 | 10.2 | 0.1 | 108.7 | 66.2% | 6.2% | 27.6% |
| 2029 | 0.0 | 8.5 | 0.0 | (3.1) | 11.0 | 10.2 | 0.0 | 113.8 | 52.5% | 6.0% | 41.5% |
| 2030 | 0.0 | 0.0 | 0.0 | (3.1) | 5.8 | 10.2 | 0.0 | 117.8 | 23.1% | 5.7% | 71.2% |
| 2031 | 0.0 | 0.0 | 0.0 | (2.9) | 0.0 | 10.2 | 0.0 | 115.8 | 18.4% | 5.8% | 75.8% |
| 2032 | 0.0 | 0.0 | 0.0 | (2.7) | 0.0 | 2.6 | 0.1 | 115.8 | 11.8% | 5.8% | 82.4% |
| 2033 | 0.0 | 0.0 | 0.0 | (1.3) | 0.0 | 0.0 | 0.1 | 117.6 | 4.6% | 5.8% | 89.6% |
| 2034 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.2 | 119.5 | 0.0% | 5.7% | 94.3% |


## 5. A1 financing (R-F05)

| Uses | USD m | Sources | USD m |
|---|---|---|---|
| Purchase price | 446.3 | Opco term loan | 328.1 |
| Transaction costs | 14.9 | Holdco TLB (face) | 57.3 |
| Opco upfront fee | 4.9 | Fund equity | 81.9 |
| Holdco OID | 1.1 |  |  |
| Total | 467.3 | Total | 467.3 |


Opco term loan sizing: PV of debt-service capacity by bucket at the sizing rates: contracted 139.5, hedged 40.2, merchant 148.4; total 328.1. The P99 one-year test (1.00x) binds in 0 years. Debt 328.1. Holdco TLB: coverage test 57.3, cap at 45% of opco equity value 66.1 (opco equity value 147.0); binding: coverage; face 57.3.

| Year | Bucket capacity | P99 capacity | Sculpted DS | All-in rate | Opening balance |
|---|---|---|---|---|---|
| 2022 | 30.0 | 34.5 | 30.0 | 3.979% | 328.1 |
| 2023 | 33.6 | 34.0 | 33.6 | 4.449% | 308.2 |
| 2024 | 30.8 | 32.9 | 30.8 | 4.447% | 288.3 |
| 2025 | 30.4 | 31.6 | 30.4 | 4.314% | 270.3 |
| 2026 | 29.9 | 30.4 | 29.9 | 4.417% | 251.6 |
| 2027 | 27.8 | 28.1 | 27.8 | 4.441% | 232.8 |
| 2028 | 25.5 | 27.2 | 25.5 | 4.449% | 215.4 |
| 2029 | 26.1 | 30.2 | 26.1 | 5.169% | 199.5 |
| 2030 | 23.6 | 28.1 | 23.6 | 5.375% | 183.7 |
| 2031 | 23.4 | 27.5 | 23.4 | 5.375% | 169.9 |
| 2032 | 23.1 | 26.9 | 23.1 | 5.375% | 155.7 |
| 2033 | 22.8 | 27.4 | 22.8 | 5.375% | 140.9 |
| 2034 | 22.4 | 27.7 | 22.4 | 5.375% | 125.7 |
| 2035 | 22.0 | 26.9 | 22.0 | 5.375% | 110.1 |
| 2036 | 22.0 | 26.6 | 22.0 | 5.375% | 94.0 |
| 2037 | 21.9 | 26.3 | 21.9 | 5.375% | 77.1 |
| 2038 | 21.9 | 26.1 | 21.9 | 5.375% | 59.3 |
| 2039 | 21.9 | 25.8 | 21.9 | 5.375% | 40.5 |
| 2040 | 21.9 | 25.6 | 21.9 | 5.375% | 20.8 |


Opco debt by asset (pro rata to PV of each asset's own debt-service capacity):

| Asset | Opco TL 2022 | USPP 2025 | Redfern 2023 |
|---|---|---|---|
| R1 | 66.5 | 43.4 | -- |
| R2 | 107.8 | 88.4 | -- |
| R3 | 65.0 | 44.8 | -- |
| R4 | 36.2 | 22.3 | -- |
| R5 | 52.5 | 42.1 | -- |
| R6 | -- | 35.3 | 36.6 |
| R7 | -- | 40.8 | -- |
| R8 | -- | 39.3 | -- |


## 6. Valuations (R-F04, R-F07)

| Case | Contracted | Hedged | Merchant | Value before shield | Tax shield at price | Enterprise value | Price | Value less price | Breakeven price |
|---|---|---|---|---|---|---|---|---|---|
| base | 149.9 | 40.4 | 164.8 | 355.1 | 84.6 | 439.7 | 446.3 | (6.6) | 438.2 |
| low | 149.1 | 39.7 | 59.4 | 248.2 | 84.6 | 332.8 | 446.3 | (113.5) | 306.2 |
| high | 150.5 | 41.2 | 303.5 | 495.2 | 84.6 | 579.8 | 446.3 | 133.5 | 611.1 |


A1 by asset (base by bucket; totals in low and high):

| Asset | Contracted | Hedged | Merchant | Base total | Low total | High total |
|---|---|---|---|---|---|---|
| R1 | 0.0 | 25.8 | 52.8 | 78.6 | 51.5 | 113.4 |
| R2 | 51.4 | 0.0 | 68.7 | 120.1 | 82.1 | 167.0 |
| R3 | 62.6 | 0.0 | 18.6 | 81.2 | 64.3 | 102.5 |
| R4 | 0.0 | 17.8 | 27.0 | 44.8 | 32.0 | 63.2 |
| R5 | 46.5 | 0.0 | 17.2 | 63.7 | 51.7 | 82.3 |
| Platform costs | (10.6) | (3.2) | (19.6) | (33.4) | (33.5) | (33.3) |


A2 (R6, at 2023-08-31): contracted 38.6, merchant 11.8, shield 12.1, value 62.5 against price 63.7 (breakeven 62.2). A3 (at 2024-02-15): R7 50.2, R8 55.0, ITC transfer proceeds PV 47.3 (nominal 48.9 on credits of 24.1 and 28.7), shield 29.1, value 181.6 against price PV 184.2 (nominal 189.3).


A2 sources and uses: price 63.7, costs 2.6, fee 0.5, loan 36.6, uses 66.8, equity 30.2


A3 sources and uses: r7_price 87.4, r8_price 101.9, r8_deposit 20.4, costs 4.4, oid 0.9, holdco_incr 93.3, itc7 24.1, itc8 28.7, itc7_proceeds 22.3, itc8_proceeds 26.6, eq_signing 0.0, eq_r7 0.0, eq_r8 52.4, carry 67.6, carry2 2.5, cash_left_after_r8 0.0, uses 194.6, equity 52.4


## 7. 2025 refinancing (R-F08)

| Series | Tenor (years) | Coupon | Size | Share |
|---|---|---|---|---|
| A | 7 | 5.71% | 142.2 | 39.9% |
| B | 12 | 6.08% | 81.9 | 23.0% |
| C | 18 | 6.39% | 132.3 | 37.1% |
| Total |  | 6.05% (issue-weighted) | 356.3 | 100.0% |


USPP P99 test binds in 0 years. Uses and proceeds at December 31, 2025:

| Item | USD m |
|---|---|
| USPP proceeds | 356.3 |
| Repay opco term loan | (251.6) |
| Repay Redfern loan | (25.6) |
| Opco swap unwind (receivable) | 6.7 |
| Redfern swap unwind (payable) | (0.4) |
| Transaction costs (1.10%) | (3.9) |
| Net opco proceeds to holdco | 81.5 |
| Repriced holdco TLB (face) | 137.6 |
| Repay holdco TLB and incremental | (126.7) |
| Holdco OID (0.5%) | (0.7) |
| Recapitalization distribution to the fund | 91.7 |


IRR impact (gross, fund level): lifetime IRR 11.33% with the refinancing against 9.87% without (+1.46 points); IRR to December 31, 2025 including NAV 11.29% against 4.39%; NAV 105.0 against 163.3; multiple to 2025 1.32x against 1.11x.

| Year | CFADS | USPP DS | USPP DSCR | USPP opening | Repriced holdco opening | Holdco coverage | Cash tax | Fund distribution |
|---|---|---|---|---|---|---|---|---|
| 2022 | 45.2 | 0.0 | n.m. | 0.0 | 0.0 | 4.38 | 0.0 | 5.9 |
| 2023 | 49.2 | 0.0 | n.m. | 0.0 | 0.0 | 2.36 | 0.0 | 3.8 |
| 2024 | 56.8 | 0.0 | n.m. | 0.0 | 0.0 | 1.40 | 0.0 | 2.7 |
| 2025 | 65.9 | 0.0 | n.m. | 0.0 | 0.0 | 2.15 | 0.2 | 99.2 |
| 2026 | 65.3 | 45.6 | 1.43 | 356.3 | 137.6 | 1.75 | 0.2 | 4.1 |
| 2027 | 63.2 | 43.4 | 1.45 | 332.3 | 132.1 | 1.87 | 0.6 | 4.3 |
| 2028 | 61.7 | 40.4 | 1.53 | 309.0 | 126.4 | 2.08 | 0.7 | 5.2 |
| 2029 | 65.2 | 40.0 | 1.63 | 287.5 | 119.9 | 2.58 | 1.1 | 7.2 |
| 2030 | 66.1 | 34.7 | 1.90 | 265.1 | 111.3 | 3.42 | 1.7 | 10.2 |
| 2031 | 62.9 | 32.2 | 1.95 | 246.7 | 99.7 | 3.67 | 1.7 | 10.3 |
| 2032 | 61.0 | 30.0 | 2.03 | 229.8 | 88.0 | 4.11 | 1.7 | 10.9 |
| 2033 | 61.1 | 28.8 | 2.12 | 214.2 | 75.8 | 4.84 | 1.8 | 12.0 |
| 2034 | 62.6 | 28.6 | 2.19 | 198.8 | 62.4 | 5.91 | 1.9 | 13.2 |
| 2035 | 61.6 | 27.4 | 2.25 | 182.7 | 47.9 | 7.24 | 1.9 | 13.8 |
| 2036 | 61.5 | 27.3 | 2.25 | 166.8 | 32.8 | 9.31 | 2.0 | 14.2 |
| 2037 | 61.5 | 27.3 | 2.25 | 150.0 | 17.1 | 13.25 | 2.1 | 14.7 |
| 2038 | 61.5 | 27.4 | 2.25 | 132.3 | 1.0 | 30.57 | 2.2 | 30.9 |
| 2039 | 61.8 | 27.4 | 2.25 | 113.4 | 0.0 | n.m. | 2.3 | 32.0 |
| 2040 | 62.0 | 27.5 | 2.25 | 93.2 | 0.0 | n.m. | 2.4 | 32.1 |
| 2041 | 62.2 | 27.6 | 2.25 | 71.6 | 0.0 | n.m. | 2.4 | 32.1 |
| 2042 | 62.3 | 27.7 | 2.25 | 48.5 | 0.0 | n.m. | 7.4 | 27.2 |
| 2043 | 57.2 | 25.4 | 2.25 | 23.9 | 0.0 | n.m. | 11.7 | 20.1 |


## 8. Fund returns (R-F09) and scenarios

| Scenario | CFADS 2026 | Min TL DSCR 2022-25 | Min USPP DSCR | Avg USPP DSCR | Min holdco cover | Equity in | Recap 2025 | NAV 2025 | IRR to 2025 | Lifetime IRR | Lifetime multiple | Years with holdco shortfall |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| base | 65.3 | 1.35 | 1.43 | 2.03 | 1.40 | 164.6 | 91.7 | 105.0 | 11.3% | 11.3% | 3.54 | 2 |
| low | 63.2 | 1.34 | 0.32 | 0.91 | 0.55 | 164.6 | 91.3 | 6.5 | -13.5% | -12.3% | 0.72 | 30 |
| high | 69.2 | 1.35 | 1.52 | 3.62 | 1.41 | 164.6 | 92.0 | 331.8 | 42.8% | 19.9% | 9.44 | 1 |
| p90_1yr | 59.2 | 1.17 | 1.30 | 1.71 | 1.00 | 164.6 | 79.4 | 50.9 | -6.8% | 5.9% | 2.19 | 6 |
| p90_10yr | 61.8 | 1.26 | 1.35 | 1.85 | 1.17 | 164.6 | 84.7 | 74.1 | 1.7% | 8.4% | 2.77 | 3 |
| p99_1yr | 54.2 | 1.01 | 1.19 | 1.46 | 0.20 | 164.6 | 74.1 | 13.2 | -22.0% | -0.7% | 0.91 | 13 |
| status_quo | 65.3 | 1.35 | n.m. | n.m. | 1.40 | 164.6 | 0.0 | 163.3 | 4.4% | 9.9% | 4.11 | 2 |
| sens_west_solar_capture_m5 | 65.1 | 1.35 | 1.43 | 1.98 | 1.39 | 164.6 | 91.4 | 98.2 | 9.8% | 10.9% | 3.30 | 2 |
| sens_battery_low | 65.3 | 1.35 | 1.43 | 1.87 | 1.40 | 164.6 | 91.7 | 86.8 | 7.6% | 10.1% | 3.12 | 2 |
| sens_curtailment_p3 | 63.2 | 1.30 | 1.39 | 1.93 | 1.27 | 164.6 | 87.7 | 87.4 | 6.0% | 9.7% | 3.09 | 3 |
| sens_opex_p10 | 61.6 | 1.26 | 1.35 | 1.86 | 1.14 | 164.6 | 85.5 | 76.0 | 2.5% | 8.6% | 2.82 | 4 |
| sens_sofr_p100_unhedged | 65.3 | 1.33 | 1.43 | 2.03 | 1.24 | 164.6 | 88.8 | 100.0 | 9.1% | 10.7% | 3.44 | 2 |


Fund distributions are floored at zero (limited liability); a holdco shortfall year is one in which opco distributions do not cover tax and holdco debt service, which in practice means a default or a negotiated cure. IRR 'n.m.' means the fund does not recover its equity.


## 9. Uri-type stress on R1 (R-F03)

| Item | Value |
|---|---|
| Event | 72 hours at USD 5,000/MWh; R1 at 15% availability |
| Swap volume (MWh) | 2880 |
| R1 generation (MWh) | 2177 |
| Volume shortfall (MWh) | 703 |
| Swap settlement paid (USD m) | 14.3 |
| Physical revenue (USD m) | 10.9 |
| Net cash over the event (USD m) | (3.4) |
| Versus normal hedged revenue for the same hours (USD m) | (3.5) |


## 10. Decommissioning (R-F10)

| Asset | Retirement | USD/kW (2022) | Cost, 2022 prices | Bonded amount 2026 | Bond cost 2026 | Nominal cost at retirement |
|---|---|---|---|---|---|---|
| R1 | 2044-12-31 | 62 | 12.5 | 13.8 | 0.083 | 21.5 |
| R2 | 2047-06-30 | 62 | 15.4 | 17.0 | 0.102 | 28.6 |
| R3 | 2049-11-30 | 62 | 9.5 | 10.5 | 0.063 | 18.5 |
| R4 | 2055-10-31 | 38 | 3.8 | 4.1 | 0.025 | 8.5 |
| R5 | 2056-06-30 | 38 | 6.9 | 7.7 | 0.046 | 16.0 |
| R6 | 2043-07-31 | 21 | 2.1 | 2.3 | 0.014 | 3.5 |
| R7 | 2044-03-31 | 21 | 3.1 | 3.5 | 0.021 | 5.4 |
| R8 | 2059-12-31 | 38 | 4.6 | 5.0 | 0.030 | 11.4 |


## 11. Design ranges against outputs

| Item | v1.0 design range | Model |
|---|---|---|
| Opco term loan 2022 | 520-600 | 328.1 |
| Holdco TLB 2022 | 160-210 | 57.3 |
| USPP 2025 | 750-860 | 356.3 |
| Fund net IRR target | 11-13% (net) | gross lifetime 11.3% |


Ranges were superseded with the price calibration (R-C08); the debt amounts follow from the Bible's revenue inputs and are reported to the editor-in-chief.


## 12. Checks

64 checks run, 0 failed.

| Check | Value | Pass |
|---|---|---|
| Opco TL sculpted balance after 2040 (USD m) | -1.60e-13 | yes |
| Redfern sculpted balance after 2030 (USD m) | 7.99e-15 | yes |
| USPP balance after 2043: opening 2026 minus total principal (USD m) | 5.68e-14 | yes |
| USPP DS = interest + principal vs sculpted target, max abs diff | 7.11e-15 | yes |
| [base] revenue buckets sum to revenue, max abs diff | 0.00e+00 | yes |
| [base] NOL never negative (min NOL, if <0) | 0.00e+00 | yes |
| [base] debt balances never negative (min, if <0) | 0.00e+00 | yes |
| [base] A1 sources = uses | 0.00e+00 | yes |
| [base] A3 sources = uses | 0.00e+00 | yes |
