# Case R verification: Excel workbook against the Python mirror

Method: `python3 model/verify_case_r.py` builds `Case_R_Model.xlsx` once per scenario (switches set on the Inputs sheet), recalculates each copy with LibreOffice headless (`soffice --headless --convert-to xlsx`), reads the values with openpyxl (data_only=True) and compares every mapped cell with `outputs_case_r.json`. Series are compared in every one of the 38 annual columns. Tolerance: absolute difference of 0.01 in displayed units (USD m, GWh, USD/MWh, %, x, fractions). Sizing, Uri, yield-statistics and debt-by-asset items do not depend on the scenario switches and are compared in the base run only; valuations are compared in base, low and high. The delivered workbook is saved with the base scenario and refinancing on; its recalculated copy is `model/recalc/Case_R_Model.xlsx`.

## Summary

| Scenario | Values compared | Failures | Largest difference | Result |
|---|---|---|---|---|
| base | 14171 | 0 | 5.00e-11 | PASS |
| low | 12950 | 0 | 5.00e-11 | PASS |
| high | 12924 | 0 | 5.00e-11 | PASS |
| p90_1yr | 12878 | 0 | 5.00e-11 | PASS |
| p90_10yr | 12875 | 0 | 5.00e-11 | PASS |
| p99_1yr | 12894 | 0 | 5.00e-11 | PASS |
| status_quo | 12868 | 1 | 5.00e-11 | FAIL |
| sens_west_solar_capture_m5 | 12873 | 0 | 5.00e-11 | PASS |
| sens_battery_low | 12874 | 0 | 5.00e-11 | PASS |
| sens_curtailment_p3 | 12874 | 0 | 5.00e-11 | PASS |
| sens_opex_p10 | 12875 | 0 | 5.00e-11 | PASS |
| sens_sofr_p100_unhedged | 12873 | 0 | 5.00e-11 | PASS |

Overall: **FAIL**.

## Key outputs, base scenario (Python against Excel)

| Item | Python | Excel | Difference | Pass |
|---|---|---|---|---|
| sz.tl_debt | 328.0652 | 328.0652 | 0.0e+00 | yes |
| sz.hc_face | 57.2742 | 57.2742 | 1.1e-13 | yes |
| sz.rf_debt | 36.6060 | 36.6060 | 5.0e-14 | yes |
| sz.hi_face | 93.3137 | 93.3137 | 1.4e-14 | yes |
| sz.u_size | 356.3345 | 356.3345 | 5.1e-13 | yes |
| sz.u_series_size.A | 142.1814 | 142.1814 | 4.0e-13 | yes |
| sz.u_series_size.B | 81.8872 | 81.8872 | 2.8e-14 | yes |
| sz.u_series_size.C | 132.2659 | 132.2659 | 4.3e-13 | yes |
| sz.u_coupon | 6.0474 | 6.0474 | 5.3e-15 | yes |
| sz.hn_face | 137.5687 | 137.5687 | 2.6e-13 | yes |
| refi.opco_net | 81.5192 | 81.5192 | 8.5e-14 | yes |
| refi.mtm_opco_receivable | 6.7106 | 6.7106 | 4.4e-15 | yes |
| refi.mtm_redfern_payable | 0.4151 | 0.4151 | 4.4e-16 | yes |
| su.A1.equity | 81.9271 | 81.9271 | 4.3e-14 | yes |
| su.A2.equity | 30.2065 | 30.2065 | 3.6e-15 | yes |
| su.A3.equity | 52.4256 | 52.4256 | 4.3e-14 | yes |
| sc.tl_dscr_min_2022_2025 | 1.3493 | 1.3493 | 2.7e-15 | yes |
| sc.uspp_dscr_min_2026_2043 | 1.4307 | 1.4307 | 4.2e-15 | yes |
| sc.uspp_dscr_avg_2026_2043 | 2.0273 | 2.0273 | 3.1e-15 | yes |
| sc.holdco_cov_min_2023_2031 | 1.3985 | 1.3985 | 4.9e-15 | yes |
| sc.fund_irr_life_pct | 11.3319 | 11.3319 | 5.2e-14 | yes |
| sc.fund_irr_2025_pct | 11.2947 | 11.2947 | 3.6e-14 | yes |
| sc.fund_nav_2025 | 105.0409 | 105.0409 | 2.3e-13 | yes |
| sc.fund_moic_life_x | 3.5374 | 3.5374 | 4.9e-15 | yes |
| val.A1.ev | 439.6990 | 439.6990 | 6.3e-13 | yes |
| val.A1.breakeven_price | 438.1545 | 438.1545 | 6.3e-13 | yes |
| val.A2.ev | 62.5200 | 62.5200 | 4.3e-14 | yes |
| val.A3.ev | 181.6104 | 181.6104 | 3.1e-13 | yes |
| uri.net_cash | -3.3746 | -3.3746 | 1.3e-15 | yes |
| div.A1.p90_1yr_gwh | 2589.4335 | 2589.4335 | 4.1e-12 | yes |
| div.A1.p99_1yr_gwh | 2428.3867 | 2428.3867 | 2.7e-12 | yes |
| div.all_generation.p90_10yr_gwh | 2959.4929 | 2959.4929 | 2.7e-12 | yes |

## Detail (all comparisons, maximum absolute difference across columns)


### base

| Key | Sheet | Location | Max diff | Pass |
|---|---|---|---|---|
| portfolio.north_atc | Operations | row 52 | 0.0e+00 | yes |
| portfolio.west_atc | Operations | row 53 | 0.0e+00 | yes |
| portfolio.south_atc | Operations | row 54 | 0.0e+00 | yes |
| portfolio.houston_atc | Operations | row 55 | 0.0e+00 | yes |
| portfolio.batt_rate | Operations | row 56 | 0.0e+00 | yes |
| portfolio.cap_hub_west_wind | Operations | row 57 | 0.0e+00 | yes |
| portfolio.cap_hub_panhandle_wind | Operations | row 58 | 0.0e+00 | yes |
| portfolio.cap_hub_west_solar | Operations | row 59 | 0.0e+00 | yes |
| portfolio.cap_hub_south_solar | Operations | row 60 | 0.0e+00 | yes |
| portfolio.cap_hub_coastal_wind | Operations | row 61 | 0.0e+00 | yes |
| R1.op_frac | Operations | row 63 | 0.0e+00 | yes |
| R1.own_share | Operations | row 65 | 1.9e-11 | yes |
| R1.hub_atc | Operations | row 66 | 0.0e+00 | yes |
| R1.deg | Operations | row 68 | 5.0e-11 | yes |
| R1.curt | Operations | row 69 | 0.0e+00 | yes |
| R1.gen_full | Operations | row 70 | 5.0e-11 | yes |
| R1.gen | Operations | row 71 | 4.8e-11 | yes |
| R1.cap_hub | Operations | row 72 | 0.0e+00 | yes |
| R1.cap_node | Operations | row 73 | 0.0e+00 | yes |
| R1.node_price | Operations | row 74 | 0.0e+00 | yes |
| R1.con_frac | Operations | row 75 | 0.0e+00 | yes |
| R1.con_vol | Operations | row 76 | 0.0e+00 | yes |
| R1.settle | Operations | row 77 | 2.0e-15 | yes |
| R1.mkt_gen | Operations | row 78 | 4.8e-11 | yes |
| R1.rev_contracted | Operations | row 79 | 0.0e+00 | yes |
| R1.rev_hedged | Operations | row 80 | 0.0e+00 | yes |
| R1.mkt_rev | Operations | row 81 | 4.9e-11 | yes |
| R1.revenue | Operations | row 82 | 4.9e-11 | yes |
| R1.rev_merchant | Operations | row 83 | 4.9e-11 | yes |
| R1.opex | Operations | row 84 | 4.9e-11 | yes |
| R1.land | Operations | row 85 | 5.0e-11 | yes |
| R1.bond | Operations | row 86 | 4.8e-11 | yes |
| R1.margin_tax | Operations | row 87 | 4.9e-11 | yes |
| R1.ebitda | Operations | row 88 | 5.0e-11 | yes |
| R1.aug | Operations | row 89 | 0.0e+00 | yes |
| R1.decom | Operations | row 90 | 3.3e-11 | yes |
| R1.cf | Operations | row 91 | 5.0e-11 | yes |
| R1.te_cash | Operations | row 92 | 0.0e+00 | yes |
| R1.mesa_tax_share | Operations | row 93 | 0.0e+00 | yes |
| R1.mesa_cf | Operations | row 94 | 5.0e-11 | yes |
| R1.mesa_taxable | Operations | row 95 | 5.0e-11 | yes |
| R1.s_contracted | Operations | row 97 | 0.0e+00 | yes |
| R1.s_hedged | Operations | row 98 | 2.8e-11 | yes |
| R1.s_merchant | Operations | row 99 | 2.8e-11 | yes |
| R1.mesa_rev | Operations | row 103 | 4.9e-11 | yes |
| R2.op_frac | Operations | row 105 | 4.1e-11 | yes |
| R2.own_share | Operations | row 107 | 1.9e-11 | yes |
| R2.hub_atc | Operations | row 108 | 0.0e+00 | yes |
| R2.deg | Operations | row 110 | 5.0e-11 | yes |
| R2.curt | Operations | row 111 | 0.0e+00 | yes |
| R2.gen_full | Operations | row 112 | 5.0e-11 | yes |
| R2.gen | Operations | row 113 | 5.0e-11 | yes |
| R2.cap_hub | Operations | row 114 | 0.0e+00 | yes |
| R2.cap_node | Operations | row 115 | 0.0e+00 | yes |
| R2.node_price | Operations | row 116 | 0.0e+00 | yes |
| R2.con_frac | Operations | row 117 | 4.1e-11 | yes |
| R2.con_vol | Operations | row 118 | 4.4e-11 | yes |
| R2.settle | Operations | row 119 | 4.5e-11 | yes |
| R2.mkt_gen | Operations | row 120 | 5.0e-11 | yes |
| R2.rev_contracted | Operations | row 121 | 4.5e-11 | yes |
| R2.rev_hedged | Operations | row 122 | 0.0e+00 | yes |
| R2.mkt_rev | Operations | row 123 | 4.8e-11 | yes |
| R2.revenue | Operations | row 124 | 5.0e-11 | yes |
| R2.rev_merchant | Operations | row 125 | 4.8e-11 | yes |
| R2.opex | Operations | row 126 | 4.7e-11 | yes |
| R2.land | Operations | row 127 | 5.0e-11 | yes |
| R2.bond | Operations | row 128 | 4.7e-11 | yes |
| R2.margin_tax | Operations | row 129 | 5.0e-11 | yes |
| R2.ebitda | Operations | row 130 | 4.7e-11 | yes |
| R2.aug | Operations | row 131 | 0.0e+00 | yes |
| R2.decom | Operations | row 132 | 4.0e-11 | yes |
| R2.cf | Operations | row 133 | 4.7e-11 | yes |
| R2.te_cash | Operations | row 134 | 0.0e+00 | yes |
| R2.mesa_tax_share | Operations | row 135 | 0.0e+00 | yes |
| R2.mesa_cf | Operations | row 136 | 4.7e-11 | yes |
| R2.mesa_taxable | Operations | row 137 | 4.7e-11 | yes |
| R2.s_contracted | Operations | row 139 | 4.2e-11 | yes |
| R2.s_hedged | Operations | row 140 | 0.0e+00 | yes |
| R2.s_merchant | Operations | row 141 | 4.2e-11 | yes |
| R2.mesa_rev | Operations | row 145 | 5.0e-11 | yes |
| R3.op_frac | Operations | row 147 | 4.9e-11 | yes |
| R3.own_share | Operations | row 149 | 1.9e-11 | yes |
| R3.hub_atc | Operations | row 150 | 0.0e+00 | yes |
| R3.deg | Operations | row 152 | 5.0e-11 | yes |
| R3.curt | Operations | row 153 | 0.0e+00 | yes |
| R3.gen_full | Operations | row 154 | 5.0e-11 | yes |
| R3.gen | Operations | row 155 | 5.0e-11 | yes |
| R3.cap_hub | Operations | row 156 | 0.0e+00 | yes |
| R3.cap_node | Operations | row 157 | 0.0e+00 | yes |
| R3.node_price | Operations | row 158 | 0.0e+00 | yes |
| R3.con_frac | Operations | row 159 | 0.0e+00 | yes |
| R3.con_vol | Operations | row 160 | 4.8e-11 | yes |
| R3.settle | Operations | row 161 | 5.0e-11 | yes |
| R3.mkt_gen | Operations | row 162 | 5.0e-11 | yes |
| R3.rev_contracted | Operations | row 163 | 0.0e+00 | yes |
| R3.rev_hedged | Operations | row 164 | 0.0e+00 | yes |
| R3.mkt_rev | Operations | row 165 | 5.0e-11 | yes |
| R3.revenue | Operations | row 166 | 5.0e-11 | yes |
| R3.rev_merchant | Operations | row 167 | 5.0e-11 | yes |
| R3.opex | Operations | row 168 | 5.0e-11 | yes |
| R3.land | Operations | row 169 | 5.0e-11 | yes |
| R3.bond | Operations | row 170 | 4.8e-11 | yes |
| R3.margin_tax | Operations | row 171 | 4.5e-11 | yes |
| R3.ebitda | Operations | row 172 | 5.0e-11 | yes |
| R3.aug | Operations | row 173 | 0.0e+00 | yes |
| R3.decom | Operations | row 174 | 8.9e-12 | yes |
| R3.cf | Operations | row 175 | 4.4e-11 | yes |
| R3.te_cash | Operations | row 177 | 0.0e+00 | yes |
| R3.mesa_tax_share | Operations | row 178 | 0.0e+00 | yes |
| R3.mesa_cf | Operations | row 179 | 4.3e-11 | yes |
| R3.mesa_taxable | Operations | row 180 | 5.0e-11 | yes |
| R3.s_contracted | Operations | row 182 | 4.5e-11 | yes |
| R3.s_hedged | Operations | row 183 | 0.0e+00 | yes |
| R3.s_merchant | Operations | row 184 | 4.5e-11 | yes |
| R3.mesa_rev | Operations | row 188 | 5.0e-11 | yes |
| R3.ptc_total | Operations | row 189 | 4.5e-11 | yes |
| R4.op_frac | Operations | row 191 | 2.9e-11 | yes |
| R4.own_share | Operations | row 193 | 1.9e-11 | yes |
| R4.hub_atc | Operations | row 194 | 0.0e+00 | yes |
| R4.deg | Operations | row 196 | 5.0e-11 | yes |
| R4.curt | Operations | row 197 | 0.0e+00 | yes |
| R4.gen_full | Operations | row 198 | 5.0e-11 | yes |
| R4.gen | Operations | row 199 | 5.0e-11 | yes |
| R4.cap_hub | Operations | row 200 | 0.0e+00 | yes |
| R4.cap_node | Operations | row 201 | 0.0e+00 | yes |
| R4.node_price | Operations | row 202 | 0.0e+00 | yes |
| R4.con_frac | Operations | row 203 | 0.0e+00 | yes |
| R4.con_vol | Operations | row 204 | 0.0e+00 | yes |
| R4.settle | Operations | row 205 | 1.0e-15 | yes |
| R4.mkt_gen | Operations | row 206 | 5.0e-11 | yes |
| R4.rev_contracted | Operations | row 207 | 0.0e+00 | yes |
| R4.rev_hedged | Operations | row 208 | 0.0e+00 | yes |
| R4.mkt_rev | Operations | row 209 | 4.9e-11 | yes |
| R4.revenue | Operations | row 210 | 4.9e-11 | yes |
| R4.rev_merchant | Operations | row 211 | 4.9e-11 | yes |
| R4.opex | Operations | row 212 | 5.0e-11 | yes |
| R4.land | Operations | row 213 | 0.0e+00 | yes |
| R4.bond | Operations | row 214 | 5.0e-11 | yes |
| R4.margin_tax | Operations | row 215 | 5.0e-11 | yes |
| R4.ebitda | Operations | row 216 | 4.9e-11 | yes |
| R4.aug | Operations | row 217 | 0.0e+00 | yes |
| R4.decom | Operations | row 218 | 1.9e-11 | yes |
| R4.cf | Operations | row 219 | 4.9e-11 | yes |
| R4.te_cash | Operations | row 220 | 0.0e+00 | yes |
| R4.mesa_tax_share | Operations | row 221 | 0.0e+00 | yes |
| R4.mesa_cf | Operations | row 222 | 4.9e-11 | yes |
| R4.mesa_taxable | Operations | row 223 | 4.9e-11 | yes |
| R4.s_contracted | Operations | row 225 | 0.0e+00 | yes |
| R4.s_hedged | Operations | row 226 | 4.6e-11 | yes |
| R4.s_merchant | Operations | row 227 | 4.6e-11 | yes |
| R4.mesa_rev | Operations | row 231 | 4.9e-11 | yes |
| R5.op_frac | Operations | row 233 | 3.7e-11 | yes |
| R5.own_share | Operations | row 235 | 1.9e-11 | yes |
| R5.hub_atc | Operations | row 236 | 0.0e+00 | yes |
| R5.deg | Operations | row 238 | 5.0e-11 | yes |
| R5.curt | Operations | row 239 | 0.0e+00 | yes |
| R5.gen_full | Operations | row 240 | 4.1e-11 | yes |
| R5.gen | Operations | row 241 | 4.9e-11 | yes |
| R5.cap_hub | Operations | row 242 | 0.0e+00 | yes |
| R5.cap_node | Operations | row 243 | 0.0e+00 | yes |
| R5.node_price | Operations | row 244 | 0.0e+00 | yes |
| R5.con_frac | Operations | row 245 | 4.1e-11 | yes |
| R5.con_vol | Operations | row 246 | 4.0e-11 | yes |
| R5.settle | Operations | row 247 | 4.8e-11 | yes |
| R5.mkt_gen | Operations | row 248 | 4.9e-11 | yes |
| R5.rev_contracted | Operations | row 249 | 4.0e-11 | yes |
| R5.rev_hedged | Operations | row 250 | 0.0e+00 | yes |
| R5.mkt_rev | Operations | row 251 | 4.9e-11 | yes |
| R5.revenue | Operations | row 252 | 4.9e-11 | yes |
| R5.rev_merchant | Operations | row 253 | 4.9e-11 | yes |
| R5.opex | Operations | row 254 | 4.9e-11 | yes |
| R5.land | Operations | row 255 | 0.0e+00 | yes |
| R5.bond | Operations | row 256 | 4.9e-11 | yes |
| R5.margin_tax | Operations | row 257 | 4.5e-11 | yes |
| R5.ebitda | Operations | row 258 | 5.0e-11 | yes |
| R5.aug | Operations | row 259 | 0.0e+00 | yes |
| R5.decom | Operations | row 260 | 2.0e-13 | yes |
| R5.cf | Operations | row 261 | 5.0e-11 | yes |
| R5.te_cash | Operations | row 263 | 4.4e-11 | yes |
| R5.mesa_tax_share | Operations | row 264 | 1.4e-12 | yes |
| R5.mesa_cf | Operations | row 265 | 4.8e-11 | yes |
| R5.mesa_taxable | Operations | row 266 | 4.8e-11 | yes |
| R5.s_contracted | Operations | row 268 | 4.5e-11 | yes |
| R5.s_hedged | Operations | row 269 | 0.0e+00 | yes |
| R5.s_merchant | Operations | row 270 | 4.5e-11 | yes |
| R5.mesa_rev | Operations | row 274 | 4.7e-11 | yes |
| R6.op_frac | Operations | row 276 | 4.2e-11 | yes |
| R6.own_share | Operations | row 278 | 2.4e-11 | yes |
| R6.hub_atc | Operations | row 279 | 0.0e+00 | yes |
| R6.con_frac | Operations | row 280 | 4.2e-11 | yes |
| R6.settle | Operations | row 281 | 4.0e-11 | yes |
| R6.stor_rev | Operations | row 282 | 3.2e-11 | yes |
| R6.rev_contracted | Operations | row 283 | 4.0e-11 | yes |
| R6.rev_hedged | Operations | row 284 | 0.0e+00 | yes |
| R6.revenue | Operations | row 285 | 4.0e-11 | yes |
| R6.rev_merchant | Operations | row 286 | 3.2e-11 | yes |
| R6.opex | Operations | row 287 | 4.9e-11 | yes |
| R6.land | Operations | row 288 | 0.0e+00 | yes |
| R6.bond | Operations | row 289 | 4.8e-11 | yes |
| R6.margin_tax | Operations | row 290 | 5.0e-11 | yes |
| R6.ebitda | Operations | row 291 | 5.0e-11 | yes |
| R6.aug | Operations | row 292 | 4.8e-12 | yes |
| R6.decom | Operations | row 293 | 2.5e-11 | yes |
| R6.cf | Operations | row 294 | 5.0e-11 | yes |
| R6.te_cash | Operations | row 295 | 0.0e+00 | yes |
| R6.mesa_tax_share | Operations | row 296 | 0.0e+00 | yes |
| R6.mesa_cf | Operations | row 297 | 5.0e-11 | yes |
| R6.mesa_taxable | Operations | row 298 | 5.0e-11 | yes |
| R6.s_contracted | Operations | row 300 | 3.8e-11 | yes |
| R6.s_hedged | Operations | row 301 | 0.0e+00 | yes |
| R6.s_merchant | Operations | row 302 | 3.8e-11 | yes |
| R6.mesa_rev | Operations | row 306 | 4.0e-11 | yes |
| R7.op_frac | Operations | row 308 | 4.4e-11 | yes |
| R7.own_share | Operations | row 310 | 0.0e+00 | yes |
| R7.hub_atc | Operations | row 311 | 0.0e+00 | yes |
| R7.con_frac | Operations | row 312 | 4.4e-11 | yes |
| R7.settle | Operations | row 314 | 3.6e-11 | yes |
| R7.stor_rev | Operations | row 315 | 4.6e-11 | yes |
| R7.rev_contracted | Operations | row 316 | 3.6e-11 | yes |
| R7.rev_hedged | Operations | row 317 | 0.0e+00 | yes |
| R7.revenue | Operations | row 318 | 4.6e-11 | yes |
| R7.rev_merchant | Operations | row 319 | 4.6e-11 | yes |
| R7.opex | Operations | row 320 | 5.0e-11 | yes |
| R7.land | Operations | row 321 | 0.0e+00 | yes |
| R7.bond | Operations | row 322 | 4.8e-11 | yes |
| R7.margin_tax | Operations | row 323 | 5.0e-11 | yes |
| R7.ebitda | Operations | row 324 | 5.0e-11 | yes |
| R7.aug | Operations | row 325 | 3.8e-11 | yes |
| R7.decom | Operations | row 326 | 2.3e-11 | yes |
| R7.cf | Operations | row 327 | 5.0e-11 | yes |
| R7.te_cash | Operations | row 328 | 0.0e+00 | yes |
| R7.mesa_tax_share | Operations | row 329 | 0.0e+00 | yes |
| R7.mesa_cf | Operations | row 330 | 5.0e-11 | yes |
| R7.mesa_taxable | Operations | row 331 | 5.0e-11 | yes |
| R7.s_contracted | Operations | row 333 | 3.1e-11 | yes |
| R7.s_hedged | Operations | row 334 | 0.0e+00 | yes |
| R7.s_merchant | Operations | row 335 | 3.1e-11 | yes |
| R7.mesa_rev | Operations | row 339 | 4.6e-11 | yes |
| R8.op_frac | Operations | row 341 | 4.6e-11 | yes |
| R8.own_share | Operations | row 343 | 0.0e+00 | yes |
| R8.hub_atc | Operations | row 344 | 0.0e+00 | yes |
| R8.deg | Operations | row 346 | 4.7e-11 | yes |
| R8.curt | Operations | row 347 | 0.0e+00 | yes |
| R8.gen_full | Operations | row 348 | 4.9e-11 | yes |
| R8.gen | Operations | row 349 | 4.9e-11 | yes |
| R8.cap_hub | Operations | row 350 | 0.0e+00 | yes |
| R8.cap_node | Operations | row 351 | 0.0e+00 | yes |
| R8.node_price | Operations | row 352 | 0.0e+00 | yes |
| R8.con_frac | Operations | row 353 | 0.0e+00 | yes |
| R8.con_vol | Operations | row 354 | 0.0e+00 | yes |
| R8.settle | Operations | row 355 | 4.8e-11 | yes |
| R8.mkt_gen | Operations | row 356 | 4.9e-11 | yes |
| R8.rev_contracted | Operations | row 357 | 0.0e+00 | yes |
| R8.rev_hedged | Operations | row 358 | 0.0e+00 | yes |
| R8.mkt_rev | Operations | row 359 | 4.9e-11 | yes |
| R8.revenue | Operations | row 360 | 4.9e-11 | yes |
| R8.rev_merchant | Operations | row 361 | 4.9e-11 | yes |
| R8.opex | Operations | row 362 | 5.0e-11 | yes |
| R8.land | Operations | row 363 | 0.0e+00 | yes |
| R8.bond | Operations | row 364 | 4.8e-11 | yes |
| R8.margin_tax | Operations | row 365 | 4.8e-11 | yes |
| R8.ebitda | Operations | row 366 | 4.8e-11 | yes |
| R8.aug | Operations | row 367 | 0.0e+00 | yes |
| R8.decom | Operations | row 368 | 3.5e-11 | yes |
| R8.cf | Operations | row 369 | 4.8e-11 | yes |
| R8.te_cash | Operations | row 370 | 0.0e+00 | yes |
| R8.mesa_tax_share | Operations | row 371 | 0.0e+00 | yes |
| R8.mesa_cf | Operations | row 372 | 4.8e-11 | yes |
| R8.mesa_taxable | Operations | row 373 | 4.8e-11 | yes |
| R8.s_contracted | Operations | row 375 | 0.0e+00 | yes |
| R8.s_hedged | Operations | row 376 | 3.6e-11 | yes |
| R8.s_merchant | Operations | row 377 | 3.6e-11 | yes |
| R8.mesa_rev | Operations | row 381 | 4.9e-11 | yes |
| portfolio.am_cost | Operations | row 384 | 5.0e-11 | yes |
| portfolio.mesa_rev_contracted_a1 | Operations | row 386 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_a1 | Operations | row 387 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_a1 | Operations | row 388 | 4.9e-11 | yes |
| portfolio.mesa_rev_a1 | Operations | row 389 | 4.9e-11 | yes |
| portfolio.mesa_rev_contracted_all | Operations | row 391 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_all | Operations | row 392 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_all | Operations | row 393 | 5.0e-11 | yes |
| portfolio.mesa_rev_all | Operations | row 394 | 5.0e-11 | yes |
| portfolio.cfads_a1 | Operations | row 400 | 4.9e-11 | yes |
| portfolio.cfads_all | Operations | row 401 | 4.8e-11 | yes |
| portfolio.cfads_a3 | Operations | row 402 | 4.9e-11 | yes |
| portfolio.share_contracted_a1 | Operations | row 403 | 4.7e-11 | yes |
| portfolio.share_hedged_a1 | Operations | row 404 | 4.5e-11 | yes |
| portfolio.share_merchant_a1 | Operations | row 405 | 4.8e-11 | yes |
| portfolio.share_contracted_all | Operations | row 409 | 4.7e-11 | yes |
| portfolio.share_hedged_all | Operations | row 410 | 4.7e-11 | yes |
| portfolio.share_merchant_all | Operations | row 411 | 3.9e-11 | yes |
| finance.dep | Tax | row 24 | 0.0e+00 | yes |
| finance.taxable_ops | Tax | row 25 | 4.9e-11 | yes |
| sz.tl_f | Funding | row 8 | 1.9e-11 | yes |
| sz.tl_rate | Funding | row 12 | 4.5e-11 | yes |
| sz.tl_cap_bucket | Funding | row 13 | 4.9e-11 | yes |
| sz.tl_cap_p99 | Funding | row 14 | 4.9e-11 | yes |
| sz.tl_ds | Funding | row 15 | 4.9e-11 | yes |
| sz.tl_df | Funding | row 16 | 5.0e-11 | yes |
| sz.tl_sched_open | Funding | row 22 | 4.9e-11 | yes |
| sz.tl_sched_int | Funding | row 23 | 4.9e-11 | yes |
| sz.tl_sched_prin | Funding | row 24 | 5.0e-11 | yes |
| sz.dist_a1_base | Funding | row 26 | 4.9e-11 | yes |
| sz.hc_k | Funding | row 33 | 4.8e-11 | yes |
| sz.hc_cap_vec | Funding | row 35 | 4.0e-11 | yes |
| sz.rf_f | Funding | row 44 | 4.2e-11 | yes |
| sz.rf_cf | Funding | row 46 | 5.0e-11 | yes |
| sz.rf_ds | Funding | row 47 | 4.8e-11 | yes |
| sz.rf_rate | Funding | row 48 | 0.0e+00 | yes |
| sz.rf_sched_open | Funding | row 51 | 4.5e-11 | yes |
| sz.rf_sched_prin | Funding | row 52 | 4.8e-11 | yes |
| sz.hi_k | Funding | row 60 | 4.5e-11 | yes |
| sz.hi_cap_vec | Funding | row 62 | 2.8e-11 | yes |
| sz.u_f | Funding | row 69 | 0.0e+00 | yes |
| sz.u_cap_bucket | Funding | row 71 | 4.9e-11 | yes |
| sz.u_cap_p99 | Funding | row 72 | 4.9e-11 | yes |
| sz.u_ds | Funding | row 73 | 4.3e-11 | yes |
| sz.u_prin | Funding | row 74 | 4.9e-11 | yes |
| sz.u_open | Funding | row 78 | 4.7e-11 | yes |
| sz.u_int | Funding | row 79 | 4.8e-11 | yes |
| sz.hn_k | Funding | row 99 | 0.0e+00 | yes |
| sz.dist_post_base | Funding | row 101 | 4.9e-11 | yes |
| sz.hn_cap_vec | Funding | row 102 | 3.8e-11 | yes |
| finance.tl_open | Debt | row 14 | 4.8e-11 | yes |
| finance.tl_int | Debt | row 15 | 3.9e-11 | yes |
| finance.tl_prin | Debt | row 16 | 3.1e-11 | yes |
| finance.tl_prepay | Debt | row 17 | 2.6e-11 | yes |
| finance.tl_ds | Debt | row 18 | 4.9e-11 | yes |
| finance.rf_open | Debt | row 23 | 3.6e-11 | yes |
| finance.rf_int | Debt | row 24 | 4.4e-11 | yes |
| finance.rf_prin | Debt | row 25 | 4.4e-11 | yes |
| finance.rf_prepay | Debt | row 26 | 2.7e-11 | yes |
| finance.rf_ds | Debt | row 27 | 3.0e-11 | yes |
| finance.u_open | Debt | row 31 | 4.7e-11 | yes |
| finance.u_int | Debt | row 32 | 4.8e-11 | yes |
| finance.u_prin | Debt | row 33 | 4.9e-11 | yes |
| finance.u_ds | Debt | row 34 | 4.3e-11 | yes |
| finance.hc1_open | Debt | row 46 | 3.5e-11 | yes |
| finance.hc1_int | Debt | row 47 | 3.8e-11 | yes |
| finance.hc1_amort | Debt | row 48 | 1.4e-11 | yes |
| finance.hc1_sweep | Debt | row 49 | 2.7e-11 | yes |
| finance.hc1_repay | Debt | row 51 | 2.0e-11 | yes |
| finance.hc2_open | Debt | row 53 | 4.9e-11 | yes |
| finance.hc2_int | Debt | row 54 | 1.3e-11 | yes |
| finance.hc2_amort | Debt | row 55 | 3.9e-11 | yes |
| finance.hc2_sweep | Debt | row 56 | 4.0e-11 | yes |
| finance.hc2_repay | Debt | row 58 | 3.0e-11 | yes |
| finance.hc3_open | Debt | row 60 | 3.9e-11 | yes |
| finance.hc3_int | Debt | row 61 | 4.8e-11 | yes |
| finance.hc3_amort | Debt | row 62 | 1.2e-11 | yes |
| finance.hc3_sweep | Debt | row 63 | 4.9e-11 | yes |
| finance.hc_ds | Debt | row 67 | 4.8e-11 | yes |
| finance.taxable_income | Tax | row 29 | 4.7e-11 | yes |
| finance.nol_open | Tax | row 30 | 4.9e-11 | yes |
| finance.nol_used | Tax | row 31 | 4.6e-11 | yes |
| finance.tax | Tax | row 32 | 5.0e-11 | yes |
| finance.nol_close | Tax | row 33 | 4.9e-11 | yes |
| finance.opco_ds | Waterfall | row 9 | 4.9e-11 | yes |
| finance.opco_dist | Waterfall | row 10 | 4.9e-11 | yes |
| finance.recap_opco | Waterfall | row 11 | 3.6e-11 | yes |
| finance.hc_excess | Waterfall | row 16 | 5.0e-11 | yes |
| finance.fund_dist_ops | Waterfall | row 19 | 5.0e-11 | yes |
| finance.recap_hold | Waterfall | row 20 | 1.2e-11 | yes |
| finance.recap_total | Waterfall | row 21 | 4.8e-11 | yes |
| finance.fund_dist | Waterfall | row 22 | 5.0e-11 | yes |
| finance.dscr_tl | Ratios | row 8 | 4.7e-11 | yes |
| finance.dscr_rf | Ratios | row 9 | 0.0e+00 | yes |
| finance.dscr_u | Ratios | row 10 | 4.9e-11 | yes |
| finance.dscr_opco | Ratios | row 11 | 4.9e-11 | yes |
| finance.hc_cov | Ratios | row 12 | 4.8e-11 | yes |
| finance.nav_df | Returns | row 96 | 5.0e-11 | yes |
| ys.R1.sigma_1yr | Operations | F8 | 1.4e-17 | yes |
| ys.R1.sigma_10yr | Operations | F9 | 1.4e-17 | yes |
| ys.R1.sigma_iav | Operations | F10 | 2.8e-17 | yes |
| ys.R1.sigma_lt | Operations | F11 | 4.9e-17 | yes |
| ys.R1.p99_1yr | Operations | F12 | 1.4e-14 | yes |
| ys.R1.p99_10yr | Operations | F13 | 1.4e-14 | yes |
| ys.R2.sigma_1yr | Operations | F14 | 0.0e+00 | yes |
| ys.R2.sigma_10yr | Operations | F15 | 4.9e-17 | yes |
| ys.R2.sigma_iav | Operations | F16 | 2.8e-17 | yes |
| ys.R2.sigma_lt | Operations | F17 | 1.4e-17 | yes |
| ys.R2.p99_1yr | Operations | F18 | 4.3e-14 | yes |
| ys.R2.p99_10yr | Operations | F19 | 0.0e+00 | yes |
| ys.R3.sigma_1yr | Operations | F20 | 2.9e-16 | yes |
| ys.R3.sigma_10yr | Operations | F21 | 4.2e-17 | yes |
| ys.R3.sigma_iav | Operations | F22 | 2.8e-17 | yes |
| ys.R3.sigma_lt | Operations | F23 | 0.0e+00 | yes |
| ys.R3.p99_1yr | Operations | F24 | 2.8e-14 | yes |
| ys.R3.p99_10yr | Operations | F25 | 1.4e-14 | yes |
| ys.R4.sigma_1yr | Operations | F26 | 6.9e-18 | yes |
| ys.R4.sigma_10yr | Operations | F27 | 4.5e-17 | yes |
| ys.R4.sigma_iav | Operations | F28 | 3.5e-17 | yes |
| ys.R4.sigma_lt | Operations | F29 | 1.4e-17 | yes |
| ys.R4.p99_1yr | Operations | F30 | 2.8e-14 | yes |
| ys.R4.p99_10yr | Operations | F31 | 2.8e-14 | yes |
| ys.R5.sigma_1yr | Operations | F32 | 1.4e-17 | yes |
| ys.R5.sigma_10yr | Operations | F33 | 1.0e-17 | yes |
| ys.R5.sigma_iav | Operations | F34 | 4.2e-17 | yes |
| ys.R5.sigma_lt | Operations | F35 | 3.8e-17 | yes |
| ys.R5.p99_1yr | Operations | F36 | 0.0e+00 | yes |
| ys.R5.p99_10yr | Operations | F37 | 1.4e-14 | yes |
| ys.R8.sigma_1yr | Operations | F38 | 6.9e-18 | yes |
| ys.R8.sigma_10yr | Operations | F39 | 4.2e-17 | yes |
| ys.R8.sigma_iav | Operations | F40 | 3.5e-17 | yes |
| ys.R8.sigma_lt | Operations | F41 | 4.9e-17 | yes |
| ys.R8.p99_1yr | Operations | F42 | 4.3e-14 | yes |
| ys.R8.p99_10yr | Operations | F43 | 1.4e-14 | yes |
| uri.gen_mwh | Operations | F1159 | 4.5e-13 | yes |
| uri.swap_mwh | Operations | F1160 | 0.0e+00 | yes |
| uri.shortfall_mwh | Operations | F1161 | 2.3e-13 | yes |
| uri.swap_payment | Operations | F1162 | 0.0e+00 | yes |
| uri.physical_revenue | Operations | F1163 | 1.8e-15 | yes |
| uri.net_cash | Operations | F1164 | 1.3e-15 | yes |
| uri.net_vs_fully_covered | Operations | F1165 | 1.3e-15 | yes |
| div.A1.p50_gwh | Operations | F1168 | 0.0e+00 | yes |
| div.A1.sigma_1yr_gwh | Operations | F1171 | 2.8e-14 | yes |
| div.A1.p90_1yr_gwh | Operations | F1172 | 4.1e-12 | yes |
| div.A1.p99_1yr_gwh | Operations | F1173 | 2.7e-12 | yes |
| div.A1.p90_1yr_correlated_gwh | Operations | F1174 | 0.0e+00 | yes |
| div.A1.p90_1yr_independent_gwh | Operations | F1175 | 2.3e-12 | yes |
| div.A1.sigma_10yr_gwh | Operations | F1176 | 2.8e-14 | yes |
| div.A1.p90_10yr_gwh | Operations | F1177 | 4.1e-12 | yes |
| div.A1.p99_10yr_gwh | Operations | F1178 | 3.6e-12 | yes |
| div.A1.p90_10yr_correlated_gwh | Operations | F1179 | 0.0e+00 | yes |
| div.A1.p90_10yr_independent_gwh | Operations | F1180 | 4.5e-12 | yes |
| div.all_generation.p50_gwh | Operations | F1181 | 0.0e+00 | yes |
| div.all_generation.sigma_1yr_gwh | Operations | F1184 | 1.7e-13 | yes |
| div.all_generation.p90_1yr_gwh | Operations | F1185 | 9.1e-13 | yes |
| div.all_generation.p99_1yr_gwh | Operations | F1186 | 4.5e-12 | yes |
| div.all_generation.p90_1yr_correlated_gwh | Operations | F1187 | 0.0e+00 | yes |
| div.all_generation.p90_1yr_independent_gwh | Operations | F1188 | 2.3e-12 | yes |
| div.all_generation.sigma_10yr_gwh | Operations | F1189 | 2.8e-14 | yes |
| div.all_generation.p90_10yr_gwh | Operations | F1190 | 2.7e-12 | yes |
| div.all_generation.p99_10yr_gwh | Operations | F1191 | 4.5e-12 | yes |
| div.all_generation.p90_10yr_correlated_gwh | Operations | F1192 | 0.0e+00 | yes |
| div.all_generation.p90_10yr_independent_gwh | Operations | F1193 | 3.2e-12 | yes |
| val.A3.itc7 | Tax | F8 | 0.0e+00 | yes |
| val.A3.itc8 | Tax | F9 | 3.6e-15 | yes |
| sz.tl_debt | Funding | F17 | 0.0e+00 | yes |
| sz.tl_pv_cap_contracted | Funding | F18 | 5.7e-14 | yes |
| sz.tl_pv_cap_hedged | Funding | F19 | 0.0e+00 | yes |
| sz.tl_pv_cap_merchant | Funding | F20 | 4.3e-13 | yes |
| sz.tl_p99_binds_years | Funding | F21 | 0.0e+00 | yes |
| sz.hc_face_cov | Funding | F36 | 1.1e-13 | yes |
| sz.opco_eq_val_2022 | Funding | F39 | 5.7e-14 | yes |
| sz.hc_face_cap | Funding | F40 | 2.8e-14 | yes |
| sz.hc_face | Funding | F41 | 1.1e-13 | yes |
| sz.rf_debt | Funding | F50 | 5.0e-14 | yes |
| sz.hi_face | Funding | F63 | 1.4e-14 | yes |
| sz.u_series_size.A | Funding | F80 | 4.0e-13 | yes |
| sz.u_series_size.B | Funding | F81 | 2.8e-14 | yes |
| sz.u_series_size.C | Funding | F82 | 4.3e-13 | yes |
| sz.u_size | Funding | F83 | 5.1e-13 | yes |
| sz.u_series_share.A | Funding | F84 | 2.1e-14 | yes |
| sz.u_series_share.B | Funding | F85 | 2.5e-14 | yes |
| sz.u_series_share.C | Funding | F86 | 5.7e-14 | yes |
| sz.u_coupon | Funding | F87 | 5.3e-15 | yes |
| sz.u_pv_cap_contracted | Funding | F89 | 4.8e-13 | yes |
| sz.u_pv_cap_hedged | Funding | F90 | 4.3e-14 | yes |
| sz.u_pv_cap_merchant | Funding | F91 | 4.3e-13 | yes |
| sz.u_p99_binds_years | Funding | F92 | 0.0e+00 | yes |
| sz.hn_face | Funding | F103 | 2.6e-13 | yes |
| dba.opco_tl_2022.R1 | Funding | F116 | 2.8e-14 | yes |
| dba.opco_tl_2022.R2 | Funding | F117 | 4.3e-13 | yes |
| dba.opco_tl_2022.R3 | Funding | F118 | 2.8e-14 | yes |
| dba.opco_tl_2022.R4 | Funding | F119 | 3.6e-14 | yes |
| dba.opco_tl_2022.R5 | Funding | F120 | 7.1e-15 | yes |
| dba.uspp_2025.R1 | Funding | F137 | 2.8e-14 | yes |
| dba.uspp_2025.R2 | Funding | F138 | 0.0e+00 | yes |
| dba.uspp_2025.R3 | Funding | F139 | 2.1e-14 | yes |
| dba.uspp_2025.R4 | Funding | F140 | 2.1e-14 | yes |
| dba.uspp_2025.R5 | Funding | F141 | 3.6e-14 | yes |
| dba.uspp_2025.R6 | Funding | F142 | 4.3e-14 | yes |
| dba.uspp_2025.R7 | Funding | F143 | 2.8e-14 | yes |
| dba.uspp_2025.R8 | Funding | F144 | 3.6e-14 | yes |
| su.A1.opco_fee | Funding | F147 | 0.0e+00 | yes |
| su.A1.holdco_oid | Funding | F148 | 1.1e-15 | yes |
| su.A1.uses | Funding | F149 | 4.0e-13 | yes |
| su.A1.equity | Funding | F150 | 4.3e-14 | yes |
| su.A2.fee | Funding | F151 | 1.1e-16 | yes |
| su.A2.uses | Funding | F152 | 4.3e-14 | yes |
| su.A2.equity | Funding | F153 | 3.6e-15 | yes |
| su.A3.r8_deposit | Funding | F154 | 3.6e-15 | yes |
| su.A3.oid | Funding | F155 | 3.3e-16 | yes |
| su.A3.itc7_proceeds | Funding | F156 | 0.0e+00 | yes |
| su.A3.itc8_proceeds | Funding | F157 | 3.6e-15 | yes |
| su.A3.eq_signing | Funding | F159 | 0.0e+00 | yes |
| su.A3.carry | Funding | F160 | 1.4e-14 | yes |
| su.A3.eq_r7 | Funding | F162 | 0.0e+00 | yes |
| su.A3.carry2 | Funding | F163 | 4.9e-15 | yes |
| su.A3.eq_r8 | Funding | F165 | 4.3e-14 | yes |
| su.A3.cash_left_after_r8 | Funding | F166 | 0.0e+00 | yes |
| su.A3.uses | Funding | F167 | 1.4e-13 | yes |
| su.A3.equity | Funding | F168 | 4.3e-14 | yes |
| refi.mtm_opco_receivable | Funding | F174 | 4.4e-15 | yes |
| refi.mtm_redfern_payable | Funding | F175 | 4.4e-16 | yes |
| refi.costs | Funding | F176 | 4.0e-15 | yes |
| refi.tl_repay | Funding | F177 | 2.8e-13 | yes |
| refi.rf_repay | Funding | F178 | 5.0e-14 | yes |
| refi.opco_net | Funding | F179 | 8.5e-14 | yes |
| sc.tl_dscr_min_2022_2025 | Ratios | F15 | 2.7e-15 | yes |
| sc.tl_dscr_avg_2022_2025 | Ratios | F16 | 2.9e-15 | yes |
| sc.uspp_dscr_min_2026_2043 | Ratios | F17 | 4.2e-15 | yes |
| sc.uspp_dscr_avg_2026_2043 | Ratios | F18 | 3.1e-15 | yes |
| sc.rf_dscr_min | Ratios | F19 | 0.0e+00 | yes |
| sc.rf_dscr_avg | Ratios | F20 | 0.0e+00 | yes |
| sc.holdco_cov_min_2023_2031 | Ratios | F21 | 4.9e-15 | yes |
| sc.holdco_cov_avg_2023_2031 | Ratios | F22 | 5.3e-15 | yes |
| val.A1.by_asset.R1.contracted | Returns | F31 | 0.0e+00 | yes |
| val.A1.by_asset.R1.hedged | Returns | F32 | 3.6e-15 | yes |
| val.A1.by_asset.R1.merchant | Returns | F33 | 2.1e-14 | yes |
| val.A1.by_asset.R1.total | Returns | F34 | 1.4e-14 | yes |
| val.A1.by_asset.R2.contracted | Returns | F35 | 4.3e-14 | yes |
| val.A1.by_asset.R2.hedged | Returns | F36 | 0.0e+00 | yes |
| val.A1.by_asset.R2.merchant | Returns | F37 | 4.3e-14 | yes |
| val.A1.by_asset.R2.total | Returns | F38 | 2.3e-13 | yes |
| val.A1.by_asset.R3.contracted | Returns | F39 | 1.4e-14 | yes |
| val.A1.by_asset.R3.hedged | Returns | F40 | 0.0e+00 | yes |
| val.A1.by_asset.R3.merchant | Returns | F41 | 2.1e-14 | yes |
| val.A1.by_asset.R3.total | Returns | F42 | 4.3e-14 | yes |
| val.A1.by_asset.R4.contracted | Returns | F43 | 0.0e+00 | yes |
| val.A1.by_asset.R4.hedged | Returns | F44 | 2.1e-14 | yes |
| val.A1.by_asset.R4.merchant | Returns | F45 | 3.9e-14 | yes |
| val.A1.by_asset.R4.total | Returns | F46 | 1.4e-14 | yes |
| val.A1.by_asset.R5.contracted | Returns | F47 | 0.0e+00 | yes |
| val.A1.by_asset.R5.hedged | Returns | F48 | 0.0e+00 | yes |
| val.A1.by_asset.R5.merchant | Returns | F49 | 3.6e-14 | yes |
| val.A1.by_asset.R5.total | Returns | F50 | 3.6e-14 | yes |
| val.A1.by_asset.Platform costs.contracted | Returns | F52 | 8.9e-15 | yes |
| val.A1.by_asset.Platform costs.hedged | Returns | F53 | 0.0e+00 | yes |
| val.A1.by_asset.Platform costs.merchant | Returns | F54 | 2.1e-14 | yes |
| val.A1.by_asset.Platform costs.total | Returns | F55 | 4.3e-14 | yes |
| val.A1.by_bucket.contracted | Returns | F56 | 1.1e-13 | yes |
| val.A1.by_bucket.hedged | Returns | F57 | 4.3e-14 | yes |
| val.A1.by_bucket.merchant | Returns | F58 | 4.5e-13 | yes |
| val.A1.pre_shield | Returns | F59 | 6.3e-13 | yes |
| val.A1.pv_dep_per_usd | Returns | F60 | 2.2e-16 | yes |
| val.A1.shield_at_price | Returns | F61 | 1.4e-14 | yes |
| val.A1.ev | Returns | F62 | 6.3e-13 | yes |
| val.A1.npv_vs_price | Returns | F63 | 1.1e-13 | yes |
| val.A1.breakeven_price | Returns | F64 | 6.3e-13 | yes |
| val.A2.R6.contracted | Returns | F67 | 0.0e+00 | yes |
| val.A2.R6.hedged | Returns | F68 | 0.0e+00 | yes |
| val.A2.R6.merchant | Returns | F69 | 3.6e-15 | yes |
| val.A2.R6.total | Returns | F70 | 7.1e-15 | yes |
| val.A2.shield_at_price | Returns | F72 | 4.3e-14 | yes |
| val.A2.ev | Returns | F73 | 4.3e-14 | yes |
| val.A2.npv_vs_price | Returns | F74 | 2.2e-15 | yes |
| val.A2.breakeven_price | Returns | F75 | 2.8e-14 | yes |
| val.A3.R7.contracted | Returns | F78 | 1.4e-14 | yes |
| val.A3.R7.hedged | Returns | F79 | 0.0e+00 | yes |
| val.A3.R7.merchant | Returns | F80 | 5.3e-15 | yes |
| val.A3.R7.total | Returns | F81 | 7.1e-15 | yes |
| val.A3.R8.contracted | Returns | F82 | 0.0e+00 | yes |
| val.A3.R8.hedged | Returns | F83 | 3.6e-15 | yes |
| val.A3.R8.merchant | Returns | F84 | 2.5e-14 | yes |
| val.A3.R8.total | Returns | F85 | 2.8e-14 | yes |
| val.A3.itc_pv | Returns | F88 | 7.1e-15 | yes |
| val.A3.shield | Returns | F89 | 3.9e-14 | yes |
| val.A3.ev | Returns | F90 | 3.1e-13 | yes |
| val.A3.price_pv | Returns | F91 | 4.0e-13 | yes |
| val.A3.npv_vs_price | Returns | F92 | 4.4e-15 | yes |
| sc.fund_nav_2025 | Returns | F98 | 2.3e-13 | yes |
| sc.fund_contributions | Returns | F99 | 2.0e-13 | yes |
| sc.fund_distributions_life | Returns | F100 | 2.3e-13 | yes |
| sc.fund_distributions_to_2025 | Returns | F101 | 7.1e-14 | yes |
| sc.fund_moic_life_x | Returns | F102 | 4.9e-15 | yes |
| sc.fund_moic_2025_x | Returns | F103 | 2.7e-15 | yes |
| sc.fund_irr_life_pct | Returns | F150 | 5.2e-14 | yes |
| sc.fund_irr_2025_pct | Returns | F151 | 3.6e-14 | yes |

### low

| Key | Sheet | Location | Max diff | Pass |
|---|---|---|---|---|
| portfolio.north_atc | Operations | row 52 | 0.0e+00 | yes |
| portfolio.west_atc | Operations | row 53 | 0.0e+00 | yes |
| portfolio.south_atc | Operations | row 54 | 0.0e+00 | yes |
| portfolio.houston_atc | Operations | row 55 | 0.0e+00 | yes |
| portfolio.batt_rate | Operations | row 56 | 0.0e+00 | yes |
| portfolio.cap_hub_west_wind | Operations | row 57 | 0.0e+00 | yes |
| portfolio.cap_hub_panhandle_wind | Operations | row 58 | 0.0e+00 | yes |
| portfolio.cap_hub_west_solar | Operations | row 59 | 0.0e+00 | yes |
| portfolio.cap_hub_south_solar | Operations | row 60 | 0.0e+00 | yes |
| portfolio.cap_hub_coastal_wind | Operations | row 61 | 0.0e+00 | yes |
| R1.op_frac | Operations | row 63 | 0.0e+00 | yes |
| R1.own_share | Operations | row 65 | 1.9e-11 | yes |
| R1.hub_atc | Operations | row 66 | 0.0e+00 | yes |
| R1.deg | Operations | row 68 | 5.0e-11 | yes |
| R1.curt | Operations | row 69 | 0.0e+00 | yes |
| R1.gen_full | Operations | row 70 | 5.0e-11 | yes |
| R1.gen | Operations | row 71 | 4.8e-11 | yes |
| R1.cap_hub | Operations | row 72 | 0.0e+00 | yes |
| R1.cap_node | Operations | row 73 | 0.0e+00 | yes |
| R1.node_price | Operations | row 74 | 0.0e+00 | yes |
| R1.con_frac | Operations | row 75 | 0.0e+00 | yes |
| R1.con_vol | Operations | row 76 | 0.0e+00 | yes |
| R1.settle | Operations | row 77 | 0.0e+00 | yes |
| R1.mkt_gen | Operations | row 78 | 4.8e-11 | yes |
| R1.rev_contracted | Operations | row 79 | 0.0e+00 | yes |
| R1.rev_hedged | Operations | row 80 | 0.0e+00 | yes |
| R1.mkt_rev | Operations | row 81 | 4.7e-11 | yes |
| R1.revenue | Operations | row 82 | 4.7e-11 | yes |
| R1.rev_merchant | Operations | row 83 | 4.7e-11 | yes |
| R1.opex | Operations | row 84 | 4.9e-11 | yes |
| R1.land | Operations | row 85 | 5.0e-11 | yes |
| R1.bond | Operations | row 86 | 4.8e-11 | yes |
| R1.margin_tax | Operations | row 87 | 5.0e-11 | yes |
| R1.ebitda | Operations | row 88 | 4.9e-11 | yes |
| R1.aug | Operations | row 89 | 0.0e+00 | yes |
| R1.decom | Operations | row 90 | 3.3e-11 | yes |
| R1.cf | Operations | row 91 | 4.9e-11 | yes |
| R1.te_cash | Operations | row 92 | 0.0e+00 | yes |
| R1.mesa_tax_share | Operations | row 93 | 0.0e+00 | yes |
| R1.mesa_cf | Operations | row 94 | 4.9e-11 | yes |
| R1.mesa_taxable | Operations | row 95 | 4.9e-11 | yes |
| R1.s_contracted | Operations | row 97 | 0.0e+00 | yes |
| R1.s_hedged | Operations | row 98 | 3.3e-11 | yes |
| R1.s_merchant | Operations | row 99 | 3.3e-11 | yes |
| R1.mesa_rev | Operations | row 103 | 4.7e-11 | yes |
| R2.op_frac | Operations | row 105 | 4.1e-11 | yes |
| R2.own_share | Operations | row 107 | 1.9e-11 | yes |
| R2.hub_atc | Operations | row 108 | 0.0e+00 | yes |
| R2.deg | Operations | row 110 | 5.0e-11 | yes |
| R2.curt | Operations | row 111 | 0.0e+00 | yes |
| R2.gen_full | Operations | row 112 | 5.0e-11 | yes |
| R2.gen | Operations | row 113 | 5.0e-11 | yes |
| R2.cap_hub | Operations | row 114 | 0.0e+00 | yes |
| R2.cap_node | Operations | row 115 | 0.0e+00 | yes |
| R2.node_price | Operations | row 116 | 0.0e+00 | yes |
| R2.con_frac | Operations | row 117 | 4.1e-11 | yes |
| R2.con_vol | Operations | row 118 | 4.4e-11 | yes |
| R2.settle | Operations | row 119 | 4.5e-11 | yes |
| R2.mkt_gen | Operations | row 120 | 5.0e-11 | yes |
| R2.rev_contracted | Operations | row 121 | 4.5e-11 | yes |
| R2.rev_hedged | Operations | row 122 | 0.0e+00 | yes |
| R2.mkt_rev | Operations | row 123 | 4.9e-11 | yes |
| R2.revenue | Operations | row 124 | 4.9e-11 | yes |
| R2.rev_merchant | Operations | row 125 | 4.9e-11 | yes |
| R2.opex | Operations | row 126 | 4.7e-11 | yes |
| R2.land | Operations | row 127 | 4.8e-11 | yes |
| R2.bond | Operations | row 128 | 4.7e-11 | yes |
| R2.margin_tax | Operations | row 129 | 5.0e-11 | yes |
| R2.ebitda | Operations | row 130 | 4.7e-11 | yes |
| R2.aug | Operations | row 131 | 0.0e+00 | yes |
| R2.decom | Operations | row 132 | 4.0e-11 | yes |
| R2.cf | Operations | row 133 | 4.7e-11 | yes |
| R2.te_cash | Operations | row 134 | 0.0e+00 | yes |
| R2.mesa_tax_share | Operations | row 135 | 0.0e+00 | yes |
| R2.mesa_cf | Operations | row 136 | 4.7e-11 | yes |
| R2.mesa_taxable | Operations | row 137 | 4.7e-11 | yes |
| R2.s_contracted | Operations | row 139 | 5.7e-12 | yes |
| R2.s_hedged | Operations | row 140 | 0.0e+00 | yes |
| R2.s_merchant | Operations | row 141 | 5.7e-12 | yes |
| R2.mesa_rev | Operations | row 145 | 4.9e-11 | yes |
| R3.op_frac | Operations | row 147 | 4.9e-11 | yes |
| R3.own_share | Operations | row 149 | 1.9e-11 | yes |
| R3.hub_atc | Operations | row 150 | 0.0e+00 | yes |
| R3.deg | Operations | row 152 | 5.0e-11 | yes |
| R3.curt | Operations | row 153 | 0.0e+00 | yes |
| R3.gen_full | Operations | row 154 | 5.0e-11 | yes |
| R3.gen | Operations | row 155 | 5.0e-11 | yes |
| R3.cap_hub | Operations | row 156 | 0.0e+00 | yes |
| R3.cap_node | Operations | row 157 | 0.0e+00 | yes |
| R3.node_price | Operations | row 158 | 0.0e+00 | yes |
| R3.con_frac | Operations | row 159 | 0.0e+00 | yes |
| R3.con_vol | Operations | row 160 | 4.8e-11 | yes |
| R3.settle | Operations | row 161 | 3.8e-11 | yes |
| R3.mkt_gen | Operations | row 162 | 5.0e-11 | yes |
| R3.rev_contracted | Operations | row 163 | 0.0e+00 | yes |
| R3.rev_hedged | Operations | row 164 | 0.0e+00 | yes |
| R3.mkt_rev | Operations | row 165 | 4.0e-11 | yes |
| R3.revenue | Operations | row 166 | 4.6e-11 | yes |
| R3.rev_merchant | Operations | row 167 | 4.6e-11 | yes |
| R3.opex | Operations | row 168 | 5.0e-11 | yes |
| R3.land | Operations | row 169 | 4.8e-11 | yes |
| R3.bond | Operations | row 170 | 4.8e-11 | yes |
| R3.margin_tax | Operations | row 171 | 4.8e-11 | yes |
| R3.ebitda | Operations | row 172 | 4.9e-11 | yes |
| R3.aug | Operations | row 173 | 0.0e+00 | yes |
| R3.decom | Operations | row 174 | 8.9e-12 | yes |
| R3.cf | Operations | row 175 | 4.9e-11 | yes |
| R3.te_cash | Operations | row 177 | 0.0e+00 | yes |
| R3.mesa_tax_share | Operations | row 178 | 0.0e+00 | yes |
| R3.mesa_cf | Operations | row 179 | 4.7e-11 | yes |
| R3.mesa_taxable | Operations | row 180 | 4.7e-11 | yes |
| R3.s_contracted | Operations | row 182 | 4.3e-11 | yes |
| R3.s_hedged | Operations | row 183 | 0.0e+00 | yes |
| R3.s_merchant | Operations | row 184 | 4.3e-11 | yes |
| R3.mesa_rev | Operations | row 188 | 4.9e-11 | yes |
| R3.ptc_total | Operations | row 189 | 4.5e-11 | yes |
| R4.op_frac | Operations | row 191 | 2.9e-11 | yes |
| R4.own_share | Operations | row 193 | 1.9e-11 | yes |
| R4.hub_atc | Operations | row 194 | 0.0e+00 | yes |
| R4.deg | Operations | row 196 | 5.0e-11 | yes |
| R4.curt | Operations | row 197 | 0.0e+00 | yes |
| R4.gen_full | Operations | row 198 | 5.0e-11 | yes |
| R4.gen | Operations | row 199 | 5.0e-11 | yes |
| R4.cap_hub | Operations | row 200 | 0.0e+00 | yes |
| R4.cap_node | Operations | row 201 | 0.0e+00 | yes |
| R4.node_price | Operations | row 202 | 0.0e+00 | yes |
| R4.con_frac | Operations | row 203 | 0.0e+00 | yes |
| R4.con_vol | Operations | row 204 | 0.0e+00 | yes |
| R4.settle | Operations | row 205 | 1.0e-15 | yes |
| R4.mkt_gen | Operations | row 206 | 5.0e-11 | yes |
| R4.rev_contracted | Operations | row 207 | 0.0e+00 | yes |
| R4.rev_hedged | Operations | row 208 | 0.0e+00 | yes |
| R4.mkt_rev | Operations | row 209 | 4.9e-11 | yes |
| R4.revenue | Operations | row 210 | 4.9e-11 | yes |
| R4.rev_merchant | Operations | row 211 | 4.9e-11 | yes |
| R4.opex | Operations | row 212 | 5.0e-11 | yes |
| R4.land | Operations | row 213 | 0.0e+00 | yes |
| R4.bond | Operations | row 214 | 5.0e-11 | yes |
| R4.margin_tax | Operations | row 215 | 4.9e-11 | yes |
| R4.ebitda | Operations | row 216 | 4.9e-11 | yes |
| R4.aug | Operations | row 217 | 0.0e+00 | yes |
| R4.decom | Operations | row 218 | 1.9e-11 | yes |
| R4.cf | Operations | row 219 | 4.9e-11 | yes |
| R4.te_cash | Operations | row 220 | 0.0e+00 | yes |
| R4.mesa_tax_share | Operations | row 221 | 0.0e+00 | yes |
| R4.mesa_cf | Operations | row 222 | 4.9e-11 | yes |
| R4.mesa_taxable | Operations | row 223 | 4.9e-11 | yes |
| R4.s_contracted | Operations | row 225 | 0.0e+00 | yes |
| R4.s_hedged | Operations | row 226 | 3.8e-11 | yes |
| R4.s_merchant | Operations | row 227 | 3.8e-11 | yes |
| R4.mesa_rev | Operations | row 231 | 4.9e-11 | yes |
| R5.op_frac | Operations | row 233 | 3.7e-11 | yes |
| R5.own_share | Operations | row 235 | 1.9e-11 | yes |
| R5.hub_atc | Operations | row 236 | 0.0e+00 | yes |
| R5.deg | Operations | row 238 | 5.0e-11 | yes |
| R5.curt | Operations | row 239 | 0.0e+00 | yes |
| R5.gen_full | Operations | row 240 | 4.1e-11 | yes |
| R5.gen | Operations | row 241 | 4.9e-11 | yes |
| R5.cap_hub | Operations | row 242 | 0.0e+00 | yes |
| R5.cap_node | Operations | row 243 | 0.0e+00 | yes |
| R5.node_price | Operations | row 244 | 0.0e+00 | yes |
| R5.con_frac | Operations | row 245 | 4.1e-11 | yes |
| R5.con_vol | Operations | row 246 | 4.0e-11 | yes |
| R5.settle | Operations | row 247 | 4.8e-11 | yes |
| R5.mkt_gen | Operations | row 248 | 4.9e-11 | yes |
| R5.rev_contracted | Operations | row 249 | 4.0e-11 | yes |
| R5.rev_hedged | Operations | row 250 | 0.0e+00 | yes |
| R5.mkt_rev | Operations | row 251 | 4.7e-11 | yes |
| R5.revenue | Operations | row 252 | 4.8e-11 | yes |
| R5.rev_merchant | Operations | row 253 | 4.6e-11 | yes |
| R5.opex | Operations | row 254 | 4.9e-11 | yes |
| R5.land | Operations | row 255 | 0.0e+00 | yes |
| R5.bond | Operations | row 256 | 4.9e-11 | yes |
| R5.margin_tax | Operations | row 257 | 4.8e-11 | yes |
| R5.ebitda | Operations | row 258 | 5.0e-11 | yes |
| R5.aug | Operations | row 259 | 0.0e+00 | yes |
| R5.decom | Operations | row 260 | 2.0e-13 | yes |
| R5.cf | Operations | row 261 | 5.0e-11 | yes |
| R5.te_cash | Operations | row 263 | 4.4e-11 | yes |
| R5.mesa_tax_share | Operations | row 264 | 1.4e-12 | yes |
| R5.mesa_cf | Operations | row 265 | 5.0e-11 | yes |
| R5.mesa_taxable | Operations | row 266 | 5.0e-11 | yes |
| R5.s_contracted | Operations | row 268 | 4.5e-11 | yes |
| R5.s_hedged | Operations | row 269 | 0.0e+00 | yes |
| R5.s_merchant | Operations | row 270 | 4.5e-11 | yes |
| R5.mesa_rev | Operations | row 274 | 5.0e-11 | yes |
| R6.op_frac | Operations | row 276 | 4.2e-11 | yes |
| R6.own_share | Operations | row 278 | 2.4e-11 | yes |
| R6.hub_atc | Operations | row 279 | 0.0e+00 | yes |
| R6.con_frac | Operations | row 280 | 4.2e-11 | yes |
| R6.settle | Operations | row 281 | 4.0e-11 | yes |
| R6.stor_rev | Operations | row 282 | 3.2e-11 | yes |
| R6.rev_contracted | Operations | row 283 | 4.0e-11 | yes |
| R6.rev_hedged | Operations | row 284 | 0.0e+00 | yes |
| R6.revenue | Operations | row 285 | 4.0e-11 | yes |
| R6.rev_merchant | Operations | row 286 | 3.2e-11 | yes |
| R6.opex | Operations | row 287 | 4.9e-11 | yes |
| R6.land | Operations | row 288 | 0.0e+00 | yes |
| R6.bond | Operations | row 289 | 4.8e-11 | yes |
| R6.margin_tax | Operations | row 290 | 5.0e-11 | yes |
| R6.ebitda | Operations | row 291 | 5.0e-11 | yes |
| R6.aug | Operations | row 292 | 4.8e-12 | yes |
| R6.decom | Operations | row 293 | 2.5e-11 | yes |
| R6.cf | Operations | row 294 | 5.0e-11 | yes |
| R6.te_cash | Operations | row 295 | 0.0e+00 | yes |
| R6.mesa_tax_share | Operations | row 296 | 0.0e+00 | yes |
| R6.mesa_cf | Operations | row 297 | 5.0e-11 | yes |
| R6.mesa_taxable | Operations | row 298 | 5.0e-11 | yes |
| R6.s_contracted | Operations | row 300 | 2.7e-11 | yes |
| R6.s_hedged | Operations | row 301 | 0.0e+00 | yes |
| R6.s_merchant | Operations | row 302 | 2.7e-11 | yes |
| R6.mesa_rev | Operations | row 306 | 4.0e-11 | yes |
| R7.op_frac | Operations | row 308 | 4.4e-11 | yes |
| R7.own_share | Operations | row 310 | 0.0e+00 | yes |
| R7.hub_atc | Operations | row 311 | 0.0e+00 | yes |
| R7.con_frac | Operations | row 312 | 4.4e-11 | yes |
| R7.settle | Operations | row 314 | 3.6e-11 | yes |
| R7.stor_rev | Operations | row 315 | 4.4e-11 | yes |
| R7.rev_contracted | Operations | row 316 | 3.6e-11 | yes |
| R7.rev_hedged | Operations | row 317 | 0.0e+00 | yes |
| R7.revenue | Operations | row 318 | 8.2e-12 | yes |
| R7.rev_merchant | Operations | row 319 | 4.4e-11 | yes |
| R7.opex | Operations | row 320 | 5.0e-11 | yes |
| R7.land | Operations | row 321 | 0.0e+00 | yes |
| R7.bond | Operations | row 322 | 4.8e-11 | yes |
| R7.margin_tax | Operations | row 323 | 5.0e-11 | yes |
| R7.ebitda | Operations | row 324 | 5.0e-11 | yes |
| R7.aug | Operations | row 325 | 3.8e-11 | yes |
| R7.decom | Operations | row 326 | 2.3e-11 | yes |
| R7.cf | Operations | row 327 | 5.0e-11 | yes |
| R7.te_cash | Operations | row 328 | 0.0e+00 | yes |
| R7.mesa_tax_share | Operations | row 329 | 0.0e+00 | yes |
| R7.mesa_cf | Operations | row 330 | 5.0e-11 | yes |
| R7.mesa_taxable | Operations | row 331 | 5.0e-11 | yes |
| R7.s_contracted | Operations | row 333 | 8.2e-12 | yes |
| R7.s_hedged | Operations | row 334 | 0.0e+00 | yes |
| R7.s_merchant | Operations | row 335 | 8.2e-12 | yes |
| R7.mesa_rev | Operations | row 339 | 8.2e-12 | yes |
| R8.op_frac | Operations | row 341 | 4.6e-11 | yes |
| R8.own_share | Operations | row 343 | 0.0e+00 | yes |
| R8.hub_atc | Operations | row 344 | 0.0e+00 | yes |
| R8.deg | Operations | row 346 | 4.7e-11 | yes |
| R8.curt | Operations | row 347 | 0.0e+00 | yes |
| R8.gen_full | Operations | row 348 | 4.9e-11 | yes |
| R8.gen | Operations | row 349 | 4.9e-11 | yes |
| R8.cap_hub | Operations | row 350 | 0.0e+00 | yes |
| R8.cap_node | Operations | row 351 | 0.0e+00 | yes |
| R8.node_price | Operations | row 352 | 0.0e+00 | yes |
| R8.con_frac | Operations | row 353 | 0.0e+00 | yes |
| R8.con_vol | Operations | row 354 | 0.0e+00 | yes |
| R8.settle | Operations | row 355 | 4.0e-11 | yes |
| R8.mkt_gen | Operations | row 356 | 4.9e-11 | yes |
| R8.rev_contracted | Operations | row 357 | 0.0e+00 | yes |
| R8.rev_hedged | Operations | row 358 | 0.0e+00 | yes |
| R8.mkt_rev | Operations | row 359 | 4.8e-11 | yes |
| R8.revenue | Operations | row 360 | 4.8e-11 | yes |
| R8.rev_merchant | Operations | row 361 | 4.8e-11 | yes |
| R8.opex | Operations | row 362 | 5.0e-11 | yes |
| R8.land | Operations | row 363 | 0.0e+00 | yes |
| R8.bond | Operations | row 364 | 4.8e-11 | yes |
| R8.margin_tax | Operations | row 365 | 5.0e-11 | yes |
| R8.ebitda | Operations | row 366 | 5.0e-11 | yes |
| R8.aug | Operations | row 367 | 0.0e+00 | yes |
| R8.decom | Operations | row 368 | 3.5e-11 | yes |
| R8.cf | Operations | row 369 | 5.0e-11 | yes |
| R8.te_cash | Operations | row 370 | 0.0e+00 | yes |
| R8.mesa_tax_share | Operations | row 371 | 0.0e+00 | yes |
| R8.mesa_cf | Operations | row 372 | 5.0e-11 | yes |
| R8.mesa_taxable | Operations | row 373 | 5.0e-11 | yes |
| R8.s_contracted | Operations | row 375 | 0.0e+00 | yes |
| R8.s_hedged | Operations | row 376 | 5.0e-11 | yes |
| R8.s_merchant | Operations | row 377 | 5.0e-11 | yes |
| R8.mesa_rev | Operations | row 381 | 4.8e-11 | yes |
| portfolio.am_cost | Operations | row 384 | 5.0e-11 | yes |
| portfolio.mesa_rev_contracted_a1 | Operations | row 386 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_a1 | Operations | row 387 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_a1 | Operations | row 388 | 5.0e-11 | yes |
| portfolio.mesa_rev_a1 | Operations | row 389 | 5.0e-11 | yes |
| portfolio.mesa_rev_contracted_all | Operations | row 391 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_all | Operations | row 392 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_all | Operations | row 393 | 5.0e-11 | yes |
| portfolio.mesa_rev_all | Operations | row 394 | 5.0e-11 | yes |
| portfolio.cfads_a1 | Operations | row 400 | 4.8e-11 | yes |
| portfolio.cfads_all | Operations | row 401 | 4.9e-11 | yes |
| portfolio.cfads_a3 | Operations | row 402 | 5.0e-11 | yes |
| portfolio.share_contracted_a1 | Operations | row 403 | 4.6e-11 | yes |
| portfolio.share_hedged_a1 | Operations | row 404 | 4.3e-11 | yes |
| portfolio.share_merchant_a1 | Operations | row 405 | 5.0e-11 | yes |
| portfolio.share_contracted_all | Operations | row 409 | 3.8e-11 | yes |
| portfolio.share_hedged_all | Operations | row 410 | 4.8e-11 | yes |
| portfolio.share_merchant_all | Operations | row 411 | 4.7e-11 | yes |
| finance.dep | Tax | row 24 | 0.0e+00 | yes |
| finance.taxable_ops | Tax | row 25 | 4.9e-11 | yes |
| finance.tl_open | Debt | row 14 | 4.8e-11 | yes |
| finance.tl_int | Debt | row 15 | 3.9e-11 | yes |
| finance.tl_prin | Debt | row 16 | 3.1e-11 | yes |
| finance.tl_prepay | Debt | row 17 | 2.6e-11 | yes |
| finance.tl_ds | Debt | row 18 | 4.9e-11 | yes |
| finance.rf_open | Debt | row 23 | 3.6e-11 | yes |
| finance.rf_int | Debt | row 24 | 4.4e-11 | yes |
| finance.rf_prin | Debt | row 25 | 4.4e-11 | yes |
| finance.rf_prepay | Debt | row 26 | 2.7e-11 | yes |
| finance.rf_ds | Debt | row 27 | 3.0e-11 | yes |
| finance.u_open | Debt | row 31 | 4.7e-11 | yes |
| finance.u_int | Debt | row 32 | 4.8e-11 | yes |
| finance.u_prin | Debt | row 33 | 4.9e-11 | yes |
| finance.u_ds | Debt | row 34 | 4.3e-11 | yes |
| finance.hc1_open | Debt | row 46 | 4.8e-11 | yes |
| finance.hc1_int | Debt | row 47 | 4.9e-11 | yes |
| finance.hc1_amort | Debt | row 48 | 1.4e-11 | yes |
| finance.hc1_sweep | Debt | row 49 | 3.8e-11 | yes |
| finance.hc1_repay | Debt | row 51 | 3.0e-13 | yes |
| finance.hc2_open | Debt | row 53 | 4.6e-11 | yes |
| finance.hc2_int | Debt | row 54 | 1.3e-11 | yes |
| finance.hc2_amort | Debt | row 55 | 3.9e-11 | yes |
| finance.hc2_sweep | Debt | row 56 | 4.2e-11 | yes |
| finance.hc2_repay | Debt | row 58 | 3.9e-11 | yes |
| finance.hc3_open | Debt | row 60 | 4.8e-11 | yes |
| finance.hc3_int | Debt | row 61 | 5.0e-11 | yes |
| finance.hc3_amort | Debt | row 62 | 3.2e-12 | yes |
| finance.hc3_sweep | Debt | row 63 | 4.3e-11 | yes |
| finance.hc_ds | Debt | row 67 | 4.9e-11 | yes |
| finance.taxable_income | Tax | row 29 | 5.0e-11 | yes |
| finance.nol_open | Tax | row 30 | 4.9e-11 | yes |
| finance.nol_used | Tax | row 31 | 4.6e-11 | yes |
| finance.tax | Tax | row 32 | 4.7e-11 | yes |
| finance.nol_close | Tax | row 33 | 4.9e-11 | yes |
| finance.opco_ds | Waterfall | row 9 | 4.9e-11 | yes |
| finance.opco_dist | Waterfall | row 10 | 5.0e-11 | yes |
| finance.recap_opco | Waterfall | row 11 | 3.6e-11 | yes |
| finance.hc_excess | Waterfall | row 16 | 5.0e-11 | yes |
| finance.fund_dist_ops | Waterfall | row 19 | 4.3e-11 | yes |
| finance.recap_hold | Waterfall | row 20 | 4.0e-11 | yes |
| finance.recap_total | Waterfall | row 21 | 3.5e-12 | yes |
| finance.fund_dist | Waterfall | row 22 | 4.3e-11 | yes |
| finance.dscr_tl | Ratios | row 8 | 4.1e-11 | yes |
| finance.dscr_rf | Ratios | row 9 | 0.0e+00 | yes |
| finance.dscr_u | Ratios | row 10 | 3.8e-11 | yes |
| finance.dscr_opco | Ratios | row 11 | 4.1e-11 | yes |
| finance.hc_cov | Ratios | row 12 | 5.0e-11 | yes |
| finance.nav_df | Returns | row 96 | 5.0e-11 | yes |
| val.A3.itc7 | Tax | F8 | 0.0e+00 | yes |
| val.A3.itc8 | Tax | F9 | 3.6e-15 | yes |
| su.A1.opco_fee | Funding | F147 | 0.0e+00 | yes |
| su.A1.holdco_oid | Funding | F148 | 1.1e-15 | yes |
| su.A1.uses | Funding | F149 | 4.0e-13 | yes |
| su.A1.equity | Funding | F150 | 4.3e-14 | yes |
| su.A2.fee | Funding | F151 | 1.1e-16 | yes |
| su.A2.uses | Funding | F152 | 4.3e-14 | yes |
| su.A2.equity | Funding | F153 | 3.6e-15 | yes |
| su.A3.r8_deposit | Funding | F154 | 3.6e-15 | yes |
| su.A3.oid | Funding | F155 | 3.3e-16 | yes |
| su.A3.itc7_proceeds | Funding | F156 | 0.0e+00 | yes |
| su.A3.itc8_proceeds | Funding | F157 | 3.6e-15 | yes |
| su.A3.eq_signing | Funding | F159 | 0.0e+00 | yes |
| su.A3.carry | Funding | F160 | 1.4e-14 | yes |
| su.A3.eq_r7 | Funding | F162 | 0.0e+00 | yes |
| su.A3.carry2 | Funding | F163 | 4.9e-15 | yes |
| su.A3.eq_r8 | Funding | F165 | 4.3e-14 | yes |
| su.A3.cash_left_after_r8 | Funding | F166 | 0.0e+00 | yes |
| su.A3.uses | Funding | F167 | 1.4e-13 | yes |
| su.A3.equity | Funding | F168 | 4.3e-14 | yes |
| refi.mtm_opco_receivable | Funding | F174 | 4.4e-15 | yes |
| refi.mtm_redfern_payable | Funding | F175 | 4.4e-16 | yes |
| refi.costs | Funding | F176 | 4.0e-15 | yes |
| refi.tl_repay | Funding | F177 | 2.8e-13 | yes |
| refi.rf_repay | Funding | F178 | 5.0e-14 | yes |
| refi.opco_net | Funding | F179 | 8.5e-14 | yes |
| sc.tl_dscr_min_2022_2025 | Ratios | F15 | 6.7e-16 | yes |
| sc.tl_dscr_avg_2022_2025 | Ratios | F16 | 2.7e-15 | yes |
| sc.uspp_dscr_min_2026_2043 | Ratios | F17 | 6.1e-16 | yes |
| sc.uspp_dscr_avg_2026_2043 | Ratios | F18 | 0.0e+00 | yes |
| sc.rf_dscr_min | Ratios | F19 | 0.0e+00 | yes |
| sc.rf_dscr_avg | Ratios | F20 | 0.0e+00 | yes |
| sc.holdco_cov_min_2023_2031 | Ratios | F21 | 3.3e-16 | yes |
| sc.holdco_cov_avg_2023_2031 | Ratios | F22 | 1.3e-15 | yes |
| val.A1.by_asset.R1.contracted | Returns | F31 | 0.0e+00 | yes |
| val.A1.by_asset.R1.hedged | Returns | F32 | 3.9e-14 | yes |
| val.A1.by_asset.R1.merchant | Returns | F33 | 1.4e-14 | yes |
| val.A1.by_asset.R1.total | Returns | F34 | 4.3e-14 | yes |
| val.A1.by_asset.R2.contracted | Returns | F35 | 1.4e-14 | yes |
| val.A1.by_asset.R2.hedged | Returns | F36 | 0.0e+00 | yes |
| val.A1.by_asset.R2.merchant | Returns | F37 | 3.6e-14 | yes |
| val.A1.by_asset.R2.total | Returns | F38 | 2.8e-14 | yes |
| val.A1.by_asset.R3.contracted | Returns | F39 | 2.8e-14 | yes |
| val.A1.by_asset.R3.hedged | Returns | F40 | 0.0e+00 | yes |
| val.A1.by_asset.R3.merchant | Returns | F41 | 6.7e-16 | yes |
| val.A1.by_asset.R3.total | Returns | F42 | 1.4e-14 | yes |
| val.A1.by_asset.R4.contracted | Returns | F43 | 0.0e+00 | yes |
| val.A1.by_asset.R4.hedged | Returns | F44 | 2.8e-14 | yes |
| val.A1.by_asset.R4.merchant | Returns | F45 | 1.2e-14 | yes |
| val.A1.by_asset.R4.total | Returns | F46 | 1.4e-14 | yes |
| val.A1.by_asset.R5.contracted | Returns | F47 | 7.1e-15 | yes |
| val.A1.by_asset.R5.hedged | Returns | F48 | 0.0e+00 | yes |
| val.A1.by_asset.R5.merchant | Returns | F49 | 7.1e-15 | yes |
| val.A1.by_asset.R5.total | Returns | F50 | 4.3e-14 | yes |
| val.A1.by_asset.Platform costs.contracted | Returns | F52 | 2.5e-14 | yes |
| val.A1.by_asset.Platform costs.hedged | Returns | F53 | 3.6e-15 | yes |
| val.A1.by_asset.Platform costs.merchant | Returns | F54 | 3.9e-14 | yes |
| val.A1.by_asset.Platform costs.total | Returns | F55 | 7.1e-15 | yes |
| val.A1.by_bucket.contracted | Returns | F56 | 2.8e-13 | yes |
| val.A1.by_bucket.hedged | Returns | F57 | 1.4e-14 | yes |
| val.A1.by_bucket.merchant | Returns | F58 | 0.0e+00 | yes |
| val.A1.pre_shield | Returns | F59 | 3.1e-13 | yes |
| val.A1.pv_dep_per_usd | Returns | F60 | 2.2e-16 | yes |
| val.A1.shield_at_price | Returns | F61 | 1.4e-14 | yes |
| val.A1.ev | Returns | F62 | 3.4e-13 | yes |
| val.A1.npv_vs_price | Returns | F63 | 3.6e-13 | yes |
| val.A1.breakeven_price | Returns | F64 | 2.8e-13 | yes |
| val.A2.R6.contracted | Returns | F67 | 1.4e-14 | yes |
| val.A2.R6.hedged | Returns | F68 | 0.0e+00 | yes |
| val.A2.R6.merchant | Returns | F69 | 1.8e-15 | yes |
| val.A2.R6.total | Returns | F70 | 2.8e-14 | yes |
| val.A2.shield_at_price | Returns | F72 | 4.3e-14 | yes |
| val.A2.ev | Returns | F73 | 1.4e-14 | yes |
| val.A2.npv_vs_price | Returns | F74 | 1.8e-15 | yes |
| val.A2.breakeven_price | Returns | F75 | 7.1e-15 | yes |
| val.A3.R7.contracted | Returns | F78 | 2.1e-14 | yes |
| val.A3.R7.hedged | Returns | F79 | 0.0e+00 | yes |
| val.A3.R7.merchant | Returns | F80 | 1.8e-15 | yes |
| val.A3.R7.total | Returns | F81 | 7.1e-15 | yes |
| val.A3.R8.contracted | Returns | F82 | 0.0e+00 | yes |
| val.A3.R8.hedged | Returns | F83 | 1.4e-14 | yes |
| val.A3.R8.merchant | Returns | F84 | 3.2e-14 | yes |
| val.A3.R8.total | Returns | F85 | 5.0e-14 | yes |
| val.A3.itc_pv | Returns | F88 | 7.1e-15 | yes |
| val.A3.shield | Returns | F89 | 3.9e-14 | yes |
| val.A3.ev | Returns | F90 | 8.5e-14 | yes |
| val.A3.price_pv | Returns | F91 | 4.0e-13 | yes |
| val.A3.npv_vs_price | Returns | F92 | 7.1e-15 | yes |
| sc.fund_nav_2025 | Returns | F98 | 4.4e-15 | yes |
| sc.fund_contributions | Returns | F99 | 2.0e-13 | yes |
| sc.fund_distributions_life | Returns | F100 | 1.4e-14 | yes |
| sc.fund_distributions_to_2025 | Returns | F101 | 6.5e-13 | yes |
| sc.fund_moic_life_x | Returns | F102 | 6.7e-16 | yes |
| sc.fund_moic_2025_x | Returns | F103 | 7.8e-16 | yes |
| sc.fund_irr_life_pct | Returns | F150 | 3.6e-15 | yes |
| sc.fund_irr_2025_pct | Returns | F151 | 9.4e-14 | yes |

### high

| Key | Sheet | Location | Max diff | Pass |
|---|---|---|---|---|
| portfolio.north_atc | Operations | row 52 | 0.0e+00 | yes |
| portfolio.west_atc | Operations | row 53 | 0.0e+00 | yes |
| portfolio.south_atc | Operations | row 54 | 0.0e+00 | yes |
| portfolio.houston_atc | Operations | row 55 | 0.0e+00 | yes |
| portfolio.batt_rate | Operations | row 56 | 0.0e+00 | yes |
| portfolio.cap_hub_west_wind | Operations | row 57 | 0.0e+00 | yes |
| portfolio.cap_hub_panhandle_wind | Operations | row 58 | 0.0e+00 | yes |
| portfolio.cap_hub_west_solar | Operations | row 59 | 0.0e+00 | yes |
| portfolio.cap_hub_south_solar | Operations | row 60 | 0.0e+00 | yes |
| portfolio.cap_hub_coastal_wind | Operations | row 61 | 0.0e+00 | yes |
| R1.op_frac | Operations | row 63 | 0.0e+00 | yes |
| R1.own_share | Operations | row 65 | 1.9e-11 | yes |
| R1.hub_atc | Operations | row 66 | 0.0e+00 | yes |
| R1.deg | Operations | row 68 | 5.0e-11 | yes |
| R1.curt | Operations | row 69 | 0.0e+00 | yes |
| R1.gen_full | Operations | row 70 | 5.0e-11 | yes |
| R1.gen | Operations | row 71 | 4.8e-11 | yes |
| R1.cap_hub | Operations | row 72 | 0.0e+00 | yes |
| R1.cap_node | Operations | row 73 | 0.0e+00 | yes |
| R1.node_price | Operations | row 74 | 0.0e+00 | yes |
| R1.con_frac | Operations | row 75 | 0.0e+00 | yes |
| R1.con_vol | Operations | row 76 | 0.0e+00 | yes |
| R1.settle | Operations | row 77 | 0.0e+00 | yes |
| R1.mkt_gen | Operations | row 78 | 4.8e-11 | yes |
| R1.rev_contracted | Operations | row 79 | 0.0e+00 | yes |
| R1.rev_hedged | Operations | row 80 | 0.0e+00 | yes |
| R1.mkt_rev | Operations | row 81 | 4.8e-11 | yes |
| R1.revenue | Operations | row 82 | 4.8e-11 | yes |
| R1.rev_merchant | Operations | row 83 | 4.8e-11 | yes |
| R1.opex | Operations | row 84 | 4.9e-11 | yes |
| R1.land | Operations | row 85 | 4.9e-11 | yes |
| R1.bond | Operations | row 86 | 4.8e-11 | yes |
| R1.margin_tax | Operations | row 87 | 4.9e-11 | yes |
| R1.ebitda | Operations | row 88 | 4.1e-11 | yes |
| R1.aug | Operations | row 89 | 0.0e+00 | yes |
| R1.decom | Operations | row 90 | 3.3e-11 | yes |
| R1.cf | Operations | row 91 | 4.1e-11 | yes |
| R1.te_cash | Operations | row 92 | 0.0e+00 | yes |
| R1.mesa_tax_share | Operations | row 93 | 0.0e+00 | yes |
| R1.mesa_cf | Operations | row 94 | 4.1e-11 | yes |
| R1.mesa_taxable | Operations | row 95 | 4.1e-11 | yes |
| R1.s_contracted | Operations | row 97 | 0.0e+00 | yes |
| R1.s_hedged | Operations | row 98 | 4.6e-11 | yes |
| R1.s_merchant | Operations | row 99 | 4.6e-11 | yes |
| R1.mesa_rev | Operations | row 103 | 4.8e-11 | yes |
| R2.op_frac | Operations | row 105 | 4.1e-11 | yes |
| R2.own_share | Operations | row 107 | 1.9e-11 | yes |
| R2.hub_atc | Operations | row 108 | 0.0e+00 | yes |
| R2.deg | Operations | row 110 | 5.0e-11 | yes |
| R2.curt | Operations | row 111 | 0.0e+00 | yes |
| R2.gen_full | Operations | row 112 | 5.0e-11 | yes |
| R2.gen | Operations | row 113 | 5.0e-11 | yes |
| R2.cap_hub | Operations | row 114 | 0.0e+00 | yes |
| R2.cap_node | Operations | row 115 | 0.0e+00 | yes |
| R2.node_price | Operations | row 116 | 0.0e+00 | yes |
| R2.con_frac | Operations | row 117 | 4.1e-11 | yes |
| R2.con_vol | Operations | row 118 | 4.4e-11 | yes |
| R2.settle | Operations | row 119 | 4.5e-11 | yes |
| R2.mkt_gen | Operations | row 120 | 5.0e-11 | yes |
| R2.rev_contracted | Operations | row 121 | 4.5e-11 | yes |
| R2.rev_hedged | Operations | row 122 | 0.0e+00 | yes |
| R2.mkt_rev | Operations | row 123 | 4.9e-11 | yes |
| R2.revenue | Operations | row 124 | 4.9e-11 | yes |
| R2.rev_merchant | Operations | row 125 | 4.9e-11 | yes |
| R2.opex | Operations | row 126 | 4.7e-11 | yes |
| R2.land | Operations | row 127 | 4.9e-11 | yes |
| R2.bond | Operations | row 128 | 4.7e-11 | yes |
| R2.margin_tax | Operations | row 129 | 4.5e-11 | yes |
| R2.ebitda | Operations | row 130 | 4.9e-11 | yes |
| R2.aug | Operations | row 131 | 0.0e+00 | yes |
| R2.decom | Operations | row 132 | 4.0e-11 | yes |
| R2.cf | Operations | row 133 | 4.9e-11 | yes |
| R2.te_cash | Operations | row 134 | 0.0e+00 | yes |
| R2.mesa_tax_share | Operations | row 135 | 0.0e+00 | yes |
| R2.mesa_cf | Operations | row 136 | 4.9e-11 | yes |
| R2.mesa_taxable | Operations | row 137 | 4.9e-11 | yes |
| R2.s_contracted | Operations | row 139 | 2.9e-12 | yes |
| R2.s_hedged | Operations | row 140 | 0.0e+00 | yes |
| R2.s_merchant | Operations | row 141 | 2.9e-12 | yes |
| R2.mesa_rev | Operations | row 145 | 4.9e-11 | yes |
| R3.op_frac | Operations | row 147 | 4.9e-11 | yes |
| R3.own_share | Operations | row 149 | 1.9e-11 | yes |
| R3.hub_atc | Operations | row 150 | 0.0e+00 | yes |
| R3.deg | Operations | row 152 | 5.0e-11 | yes |
| R3.curt | Operations | row 153 | 0.0e+00 | yes |
| R3.gen_full | Operations | row 154 | 5.0e-11 | yes |
| R3.gen | Operations | row 155 | 5.0e-11 | yes |
| R3.cap_hub | Operations | row 156 | 0.0e+00 | yes |
| R3.cap_node | Operations | row 157 | 0.0e+00 | yes |
| R3.node_price | Operations | row 158 | 0.0e+00 | yes |
| R3.con_frac | Operations | row 159 | 0.0e+00 | yes |
| R3.con_vol | Operations | row 160 | 4.8e-11 | yes |
| R3.settle | Operations | row 161 | 4.6e-11 | yes |
| R3.mkt_gen | Operations | row 162 | 5.0e-11 | yes |
| R3.rev_contracted | Operations | row 163 | 0.0e+00 | yes |
| R3.rev_hedged | Operations | row 164 | 0.0e+00 | yes |
| R3.mkt_rev | Operations | row 165 | 4.7e-11 | yes |
| R3.revenue | Operations | row 166 | 4.8e-11 | yes |
| R3.rev_merchant | Operations | row 167 | 4.8e-11 | yes |
| R3.opex | Operations | row 168 | 5.0e-11 | yes |
| R3.land | Operations | row 169 | 4.8e-11 | yes |
| R3.bond | Operations | row 170 | 4.8e-11 | yes |
| R3.margin_tax | Operations | row 171 | 4.9e-11 | yes |
| R3.ebitda | Operations | row 172 | 4.5e-11 | yes |
| R3.aug | Operations | row 173 | 0.0e+00 | yes |
| R3.decom | Operations | row 174 | 8.9e-12 | yes |
| R3.cf | Operations | row 175 | 4.5e-11 | yes |
| R3.te_cash | Operations | row 177 | 0.0e+00 | yes |
| R3.mesa_tax_share | Operations | row 178 | 0.0e+00 | yes |
| R3.mesa_cf | Operations | row 179 | 5.0e-11 | yes |
| R3.mesa_taxable | Operations | row 180 | 5.0e-11 | yes |
| R3.s_contracted | Operations | row 182 | 4.7e-11 | yes |
| R3.s_hedged | Operations | row 183 | 0.0e+00 | yes |
| R3.s_merchant | Operations | row 184 | 4.7e-11 | yes |
| R3.mesa_rev | Operations | row 188 | 4.6e-11 | yes |
| R3.ptc_total | Operations | row 189 | 4.5e-11 | yes |
| R4.op_frac | Operations | row 191 | 2.9e-11 | yes |
| R4.own_share | Operations | row 193 | 1.9e-11 | yes |
| R4.hub_atc | Operations | row 194 | 0.0e+00 | yes |
| R4.deg | Operations | row 196 | 5.0e-11 | yes |
| R4.curt | Operations | row 197 | 0.0e+00 | yes |
| R4.gen_full | Operations | row 198 | 5.0e-11 | yes |
| R4.gen | Operations | row 199 | 5.0e-11 | yes |
| R4.cap_hub | Operations | row 200 | 0.0e+00 | yes |
| R4.cap_node | Operations | row 201 | 0.0e+00 | yes |
| R4.node_price | Operations | row 202 | 0.0e+00 | yes |
| R4.con_frac | Operations | row 203 | 0.0e+00 | yes |
| R4.con_vol | Operations | row 204 | 0.0e+00 | yes |
| R4.settle | Operations | row 205 | 1.6e-15 | yes |
| R4.mkt_gen | Operations | row 206 | 5.0e-11 | yes |
| R4.rev_contracted | Operations | row 207 | 0.0e+00 | yes |
| R4.rev_hedged | Operations | row 208 | 0.0e+00 | yes |
| R4.mkt_rev | Operations | row 209 | 4.8e-11 | yes |
| R4.revenue | Operations | row 210 | 4.8e-11 | yes |
| R4.rev_merchant | Operations | row 211 | 4.8e-11 | yes |
| R4.opex | Operations | row 212 | 5.0e-11 | yes |
| R4.land | Operations | row 213 | 0.0e+00 | yes |
| R4.bond | Operations | row 214 | 5.0e-11 | yes |
| R4.margin_tax | Operations | row 215 | 5.0e-11 | yes |
| R4.ebitda | Operations | row 216 | 4.9e-11 | yes |
| R4.aug | Operations | row 217 | 0.0e+00 | yes |
| R4.decom | Operations | row 218 | 1.9e-11 | yes |
| R4.cf | Operations | row 219 | 4.9e-11 | yes |
| R4.te_cash | Operations | row 220 | 0.0e+00 | yes |
| R4.mesa_tax_share | Operations | row 221 | 0.0e+00 | yes |
| R4.mesa_cf | Operations | row 222 | 4.9e-11 | yes |
| R4.mesa_taxable | Operations | row 223 | 4.9e-11 | yes |
| R4.s_contracted | Operations | row 225 | 0.0e+00 | yes |
| R4.s_hedged | Operations | row 226 | 4.2e-11 | yes |
| R4.s_merchant | Operations | row 227 | 4.2e-11 | yes |
| R4.mesa_rev | Operations | row 231 | 4.8e-11 | yes |
| R5.op_frac | Operations | row 233 | 3.7e-11 | yes |
| R5.own_share | Operations | row 235 | 1.9e-11 | yes |
| R5.hub_atc | Operations | row 236 | 0.0e+00 | yes |
| R5.deg | Operations | row 238 | 5.0e-11 | yes |
| R5.curt | Operations | row 239 | 0.0e+00 | yes |
| R5.gen_full | Operations | row 240 | 4.1e-11 | yes |
| R5.gen | Operations | row 241 | 4.9e-11 | yes |
| R5.cap_hub | Operations | row 242 | 0.0e+00 | yes |
| R5.cap_node | Operations | row 243 | 0.0e+00 | yes |
| R5.node_price | Operations | row 244 | 0.0e+00 | yes |
| R5.con_frac | Operations | row 245 | 4.1e-11 | yes |
| R5.con_vol | Operations | row 246 | 4.0e-11 | yes |
| R5.settle | Operations | row 247 | 4.8e-11 | yes |
| R5.mkt_gen | Operations | row 248 | 4.9e-11 | yes |
| R5.rev_contracted | Operations | row 249 | 4.0e-11 | yes |
| R5.rev_hedged | Operations | row 250 | 0.0e+00 | yes |
| R5.mkt_rev | Operations | row 251 | 4.9e-11 | yes |
| R5.revenue | Operations | row 252 | 4.9e-11 | yes |
| R5.rev_merchant | Operations | row 253 | 4.9e-11 | yes |
| R5.opex | Operations | row 254 | 4.9e-11 | yes |
| R5.land | Operations | row 255 | 0.0e+00 | yes |
| R5.bond | Operations | row 256 | 4.9e-11 | yes |
| R5.margin_tax | Operations | row 257 | 5.0e-11 | yes |
| R5.ebitda | Operations | row 258 | 4.7e-11 | yes |
| R5.aug | Operations | row 259 | 0.0e+00 | yes |
| R5.decom | Operations | row 260 | 2.0e-13 | yes |
| R5.cf | Operations | row 261 | 4.7e-11 | yes |
| R5.te_cash | Operations | row 263 | 4.4e-11 | yes |
| R5.mesa_tax_share | Operations | row 264 | 1.4e-12 | yes |
| R5.mesa_cf | Operations | row 265 | 4.5e-11 | yes |
| R5.mesa_taxable | Operations | row 266 | 4.9e-11 | yes |
| R5.s_contracted | Operations | row 268 | 4.4e-11 | yes |
| R5.s_hedged | Operations | row 269 | 0.0e+00 | yes |
| R5.s_merchant | Operations | row 270 | 4.4e-11 | yes |
| R5.mesa_rev | Operations | row 274 | 5.0e-11 | yes |
| R6.op_frac | Operations | row 276 | 4.2e-11 | yes |
| R6.own_share | Operations | row 278 | 2.4e-11 | yes |
| R6.hub_atc | Operations | row 279 | 0.0e+00 | yes |
| R6.con_frac | Operations | row 280 | 4.2e-11 | yes |
| R6.settle | Operations | row 281 | 4.0e-11 | yes |
| R6.stor_rev | Operations | row 282 | 4.1e-11 | yes |
| R6.rev_contracted | Operations | row 283 | 4.0e-11 | yes |
| R6.rev_hedged | Operations | row 284 | 0.0e+00 | yes |
| R6.revenue | Operations | row 285 | 4.1e-11 | yes |
| R6.rev_merchant | Operations | row 286 | 4.1e-11 | yes |
| R6.opex | Operations | row 287 | 4.9e-11 | yes |
| R6.land | Operations | row 288 | 0.0e+00 | yes |
| R6.bond | Operations | row 289 | 4.8e-11 | yes |
| R6.margin_tax | Operations | row 290 | 5.0e-11 | yes |
| R6.ebitda | Operations | row 291 | 5.0e-11 | yes |
| R6.aug | Operations | row 292 | 4.8e-12 | yes |
| R6.decom | Operations | row 293 | 2.5e-11 | yes |
| R6.cf | Operations | row 294 | 5.0e-11 | yes |
| R6.te_cash | Operations | row 295 | 0.0e+00 | yes |
| R6.mesa_tax_share | Operations | row 296 | 0.0e+00 | yes |
| R6.mesa_cf | Operations | row 297 | 5.0e-11 | yes |
| R6.mesa_taxable | Operations | row 298 | 5.0e-11 | yes |
| R6.s_contracted | Operations | row 300 | 2.1e-11 | yes |
| R6.s_hedged | Operations | row 301 | 0.0e+00 | yes |
| R6.s_merchant | Operations | row 302 | 2.1e-11 | yes |
| R6.mesa_rev | Operations | row 306 | 4.1e-11 | yes |
| R7.op_frac | Operations | row 308 | 4.4e-11 | yes |
| R7.own_share | Operations | row 310 | 0.0e+00 | yes |
| R7.hub_atc | Operations | row 311 | 0.0e+00 | yes |
| R7.con_frac | Operations | row 312 | 4.4e-11 | yes |
| R7.settle | Operations | row 314 | 8.2e-12 | yes |
| R7.stor_rev | Operations | row 315 | 4.9e-11 | yes |
| R7.rev_contracted | Operations | row 316 | 3.6e-11 | yes |
| R7.rev_hedged | Operations | row 317 | 0.0e+00 | yes |
| R7.revenue | Operations | row 318 | 4.9e-11 | yes |
| R7.rev_merchant | Operations | row 319 | 4.9e-11 | yes |
| R7.opex | Operations | row 320 | 5.0e-11 | yes |
| R7.land | Operations | row 321 | 0.0e+00 | yes |
| R7.bond | Operations | row 322 | 4.8e-11 | yes |
| R7.margin_tax | Operations | row 323 | 5.0e-11 | yes |
| R7.ebitda | Operations | row 324 | 4.7e-11 | yes |
| R7.aug | Operations | row 325 | 3.8e-11 | yes |
| R7.decom | Operations | row 326 | 2.3e-11 | yes |
| R7.cf | Operations | row 327 | 4.7e-11 | yes |
| R7.te_cash | Operations | row 328 | 0.0e+00 | yes |
| R7.mesa_tax_share | Operations | row 329 | 0.0e+00 | yes |
| R7.mesa_cf | Operations | row 330 | 4.7e-11 | yes |
| R7.mesa_taxable | Operations | row 331 | 4.7e-11 | yes |
| R7.s_contracted | Operations | row 333 | 4.4e-11 | yes |
| R7.s_hedged | Operations | row 334 | 0.0e+00 | yes |
| R7.s_merchant | Operations | row 335 | 4.4e-11 | yes |
| R7.mesa_rev | Operations | row 339 | 4.9e-11 | yes |
| R8.op_frac | Operations | row 341 | 4.6e-11 | yes |
| R8.own_share | Operations | row 343 | 0.0e+00 | yes |
| R8.hub_atc | Operations | row 344 | 0.0e+00 | yes |
| R8.deg | Operations | row 346 | 4.7e-11 | yes |
| R8.curt | Operations | row 347 | 0.0e+00 | yes |
| R8.gen_full | Operations | row 348 | 4.9e-11 | yes |
| R8.gen | Operations | row 349 | 4.9e-11 | yes |
| R8.cap_hub | Operations | row 350 | 0.0e+00 | yes |
| R8.cap_node | Operations | row 351 | 0.0e+00 | yes |
| R8.node_price | Operations | row 352 | 0.0e+00 | yes |
| R8.con_frac | Operations | row 353 | 0.0e+00 | yes |
| R8.con_vol | Operations | row 354 | 0.0e+00 | yes |
| R8.settle | Operations | row 355 | 4.7e-11 | yes |
| R8.mkt_gen | Operations | row 356 | 4.9e-11 | yes |
| R8.rev_contracted | Operations | row 357 | 0.0e+00 | yes |
| R8.rev_hedged | Operations | row 358 | 0.0e+00 | yes |
| R8.mkt_rev | Operations | row 359 | 5.0e-11 | yes |
| R8.revenue | Operations | row 360 | 5.0e-11 | yes |
| R8.rev_merchant | Operations | row 361 | 5.0e-11 | yes |
| R8.opex | Operations | row 362 | 5.0e-11 | yes |
| R8.land | Operations | row 363 | 0.0e+00 | yes |
| R8.bond | Operations | row 364 | 4.8e-11 | yes |
| R8.margin_tax | Operations | row 365 | 4.8e-11 | yes |
| R8.ebitda | Operations | row 366 | 5.0e-11 | yes |
| R8.aug | Operations | row 367 | 0.0e+00 | yes |
| R8.decom | Operations | row 368 | 3.5e-11 | yes |
| R8.cf | Operations | row 369 | 5.0e-11 | yes |
| R8.te_cash | Operations | row 370 | 0.0e+00 | yes |
| R8.mesa_tax_share | Operations | row 371 | 0.0e+00 | yes |
| R8.mesa_cf | Operations | row 372 | 5.0e-11 | yes |
| R8.mesa_taxable | Operations | row 373 | 5.0e-11 | yes |
| R8.s_contracted | Operations | row 375 | 0.0e+00 | yes |
| R8.s_hedged | Operations | row 376 | 4.8e-11 | yes |
| R8.s_merchant | Operations | row 377 | 4.8e-11 | yes |
| R8.mesa_rev | Operations | row 381 | 5.0e-11 | yes |
| portfolio.am_cost | Operations | row 384 | 5.0e-11 | yes |
| portfolio.mesa_rev_contracted_a1 | Operations | row 386 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_a1 | Operations | row 387 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_a1 | Operations | row 388 | 4.8e-11 | yes |
| portfolio.mesa_rev_a1 | Operations | row 389 | 4.8e-11 | yes |
| portfolio.mesa_rev_contracted_all | Operations | row 391 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_all | Operations | row 392 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_all | Operations | row 393 | 4.5e-11 | yes |
| portfolio.mesa_rev_all | Operations | row 394 | 4.5e-11 | yes |
| portfolio.cfads_a1 | Operations | row 400 | 5.0e-11 | yes |
| portfolio.cfads_all | Operations | row 401 | 4.9e-11 | yes |
| portfolio.cfads_a3 | Operations | row 402 | 5.0e-11 | yes |
| portfolio.share_contracted_a1 | Operations | row 403 | 5.0e-11 | yes |
| portfolio.share_hedged_a1 | Operations | row 404 | 4.3e-11 | yes |
| portfolio.share_merchant_a1 | Operations | row 405 | 4.7e-11 | yes |
| portfolio.share_contracted_all | Operations | row 409 | 4.8e-11 | yes |
| portfolio.share_hedged_all | Operations | row 410 | 4.6e-11 | yes |
| portfolio.share_merchant_all | Operations | row 411 | 4.5e-11 | yes |
| finance.dep | Tax | row 24 | 0.0e+00 | yes |
| finance.taxable_ops | Tax | row 25 | 4.9e-11 | yes |
| finance.tl_open | Debt | row 14 | 4.8e-11 | yes |
| finance.tl_int | Debt | row 15 | 3.9e-11 | yes |
| finance.tl_prin | Debt | row 16 | 3.1e-11 | yes |
| finance.tl_prepay | Debt | row 17 | 2.6e-11 | yes |
| finance.tl_ds | Debt | row 18 | 4.9e-11 | yes |
| finance.rf_open | Debt | row 23 | 3.6e-11 | yes |
| finance.rf_int | Debt | row 24 | 4.4e-11 | yes |
| finance.rf_prin | Debt | row 25 | 4.4e-11 | yes |
| finance.rf_prepay | Debt | row 26 | 2.7e-11 | yes |
| finance.rf_ds | Debt | row 27 | 3.0e-11 | yes |
| finance.u_open | Debt | row 31 | 4.7e-11 | yes |
| finance.u_int | Debt | row 32 | 4.8e-11 | yes |
| finance.u_prin | Debt | row 33 | 4.9e-11 | yes |
| finance.u_ds | Debt | row 34 | 4.3e-11 | yes |
| finance.hc1_open | Debt | row 46 | 4.4e-11 | yes |
| finance.hc1_int | Debt | row 47 | 2.4e-11 | yes |
| finance.hc1_amort | Debt | row 48 | 1.4e-11 | yes |
| finance.hc1_sweep | Debt | row 49 | 3.5e-11 | yes |
| finance.hc1_repay | Debt | row 51 | 1.4e-11 | yes |
| finance.hc2_open | Debt | row 53 | 3.1e-11 | yes |
| finance.hc2_int | Debt | row 54 | 3.0e-11 | yes |
| finance.hc2_amort | Debt | row 55 | 3.9e-11 | yes |
| finance.hc2_sweep | Debt | row 56 | 4.3e-11 | yes |
| finance.hc2_repay | Debt | row 58 | 1.4e-11 | yes |
| finance.hc3_open | Debt | row 60 | 3.7e-11 | yes |
| finance.hc3_int | Debt | row 61 | 3.5e-11 | yes |
| finance.hc3_amort | Debt | row 62 | 3.2e-12 | yes |
| finance.hc3_sweep | Debt | row 63 | 4.2e-11 | yes |
| finance.hc_ds | Debt | row 67 | 3.9e-11 | yes |
| finance.taxable_income | Tax | row 29 | 5.0e-11 | yes |
| finance.nol_open | Tax | row 30 | 5.0e-11 | yes |
| finance.nol_used | Tax | row 31 | 4.3e-11 | yes |
| finance.tax | Tax | row 32 | 4.9e-11 | yes |
| finance.nol_close | Tax | row 33 | 5.0e-11 | yes |
| finance.opco_ds | Waterfall | row 9 | 4.9e-11 | yes |
| finance.opco_dist | Waterfall | row 10 | 4.9e-11 | yes |
| finance.recap_opco | Waterfall | row 11 | 3.6e-11 | yes |
| finance.hc_excess | Waterfall | row 16 | 5.0e-11 | yes |
| finance.fund_dist_ops | Waterfall | row 19 | 5.0e-11 | yes |
| finance.recap_hold | Waterfall | row 20 | 2.2e-11 | yes |
| finance.recap_total | Waterfall | row 21 | 4.2e-11 | yes |
| finance.fund_dist | Waterfall | row 22 | 5.0e-11 | yes |
| finance.dscr_tl | Ratios | row 8 | 4.1e-11 | yes |
| finance.dscr_rf | Ratios | row 9 | 0.0e+00 | yes |
| finance.dscr_u | Ratios | row 10 | 4.9e-11 | yes |
| finance.dscr_opco | Ratios | row 11 | 4.9e-11 | yes |
| finance.hc_cov | Ratios | row 12 | 3.6e-11 | yes |
| finance.nav_df | Returns | row 96 | 5.0e-11 | yes |
| val.A3.itc7 | Tax | F8 | 0.0e+00 | yes |
| val.A3.itc8 | Tax | F9 | 3.6e-15 | yes |
| su.A1.opco_fee | Funding | F147 | 0.0e+00 | yes |
| su.A1.holdco_oid | Funding | F148 | 1.1e-15 | yes |
| su.A1.uses | Funding | F149 | 4.0e-13 | yes |
| su.A1.equity | Funding | F150 | 4.3e-14 | yes |
| su.A2.fee | Funding | F151 | 1.1e-16 | yes |
| su.A2.uses | Funding | F152 | 4.3e-14 | yes |
| su.A2.equity | Funding | F153 | 3.6e-15 | yes |
| su.A3.r8_deposit | Funding | F154 | 3.6e-15 | yes |
| su.A3.oid | Funding | F155 | 3.3e-16 | yes |
| su.A3.itc7_proceeds | Funding | F156 | 0.0e+00 | yes |
| su.A3.itc8_proceeds | Funding | F157 | 3.6e-15 | yes |
| su.A3.eq_signing | Funding | F159 | 0.0e+00 | yes |
| su.A3.carry | Funding | F160 | 1.4e-14 | yes |
| su.A3.eq_r7 | Funding | F162 | 0.0e+00 | yes |
| su.A3.carry2 | Funding | F163 | 4.9e-15 | yes |
| su.A3.eq_r8 | Funding | F165 | 4.3e-14 | yes |
| su.A3.cash_left_after_r8 | Funding | F166 | 0.0e+00 | yes |
| su.A3.uses | Funding | F167 | 1.4e-13 | yes |
| su.A3.equity | Funding | F168 | 4.3e-14 | yes |
| refi.mtm_opco_receivable | Funding | F174 | 4.4e-15 | yes |
| refi.mtm_redfern_payable | Funding | F175 | 4.4e-16 | yes |
| refi.costs | Funding | F176 | 4.0e-15 | yes |
| refi.tl_repay | Funding | F177 | 2.8e-13 | yes |
| refi.rf_repay | Funding | F178 | 5.0e-14 | yes |
| refi.opco_net | Funding | F179 | 8.5e-14 | yes |
| sc.tl_dscr_min_2022_2025 | Ratios | F15 | 8.9e-16 | yes |
| sc.tl_dscr_avg_2022_2025 | Ratios | F16 | 3.1e-15 | yes |
| sc.uspp_dscr_min_2026_2043 | Ratios | F17 | 4.4e-15 | yes |
| sc.uspp_dscr_avg_2026_2043 | Ratios | F18 | 3.1e-15 | yes |
| sc.rf_dscr_min | Ratios | F19 | 0.0e+00 | yes |
| sc.rf_dscr_avg | Ratios | F20 | 0.0e+00 | yes |
| sc.holdco_cov_min_2023_2031 | Ratios | F21 | 2.0e-15 | yes |
| sc.holdco_cov_avg_2023_2031 | Ratios | F22 | 5.3e-15 | yes |
| val.A1.by_asset.R1.contracted | Returns | F31 | 0.0e+00 | yes |
| val.A1.by_asset.R1.hedged | Returns | F32 | 2.1e-14 | yes |
| val.A1.by_asset.R1.merchant | Returns | F33 | 1.4e-14 | yes |
| val.A1.by_asset.R1.total | Returns | F34 | 3.1e-13 | yes |
| val.A1.by_asset.R2.contracted | Returns | F35 | 7.1e-15 | yes |
| val.A1.by_asset.R2.hedged | Returns | F36 | 0.0e+00 | yes |
| val.A1.by_asset.R2.merchant | Returns | F37 | 5.7e-14 | yes |
| val.A1.by_asset.R2.total | Returns | F38 | 3.1e-13 | yes |
| val.A1.by_asset.R3.contracted | Returns | F39 | 1.4e-14 | yes |
| val.A1.by_asset.R3.hedged | Returns | F40 | 0.0e+00 | yes |
| val.A1.by_asset.R3.merchant | Returns | F41 | 1.4e-14 | yes |
| val.A1.by_asset.R3.total | Returns | F42 | 9.9e-14 | yes |
| val.A1.by_asset.R4.contracted | Returns | F43 | 0.0e+00 | yes |
| val.A1.by_asset.R4.hedged | Returns | F44 | 4.6e-14 | yes |
| val.A1.by_asset.R4.merchant | Returns | F45 | 4.3e-14 | yes |
| val.A1.by_asset.R4.total | Returns | F46 | 0.0e+00 | yes |
| val.A1.by_asset.R5.contracted | Returns | F47 | 7.1e-15 | yes |
| val.A1.by_asset.R5.hedged | Returns | F48 | 0.0e+00 | yes |
| val.A1.by_asset.R5.merchant | Returns | F49 | 2.1e-14 | yes |
| val.A1.by_asset.R5.total | Returns | F50 | 0.0e+00 | yes |
| val.A1.by_asset.Platform costs.contracted | Returns | F52 | 8.9e-15 | yes |
| val.A1.by_asset.Platform costs.hedged | Returns | F53 | 4.4e-15 | yes |
| val.A1.by_asset.Platform costs.merchant | Returns | F54 | 4.3e-14 | yes |
| val.A1.by_asset.Platform costs.total | Returns | F55 | 4.3e-14 | yes |
| val.A1.by_bucket.contracted | Returns | F56 | 4.8e-13 | yes |
| val.A1.by_bucket.hedged | Returns | F57 | 5.7e-14 | yes |
| val.A1.by_bucket.merchant | Returns | F58 | 2.3e-13 | yes |
| val.A1.pre_shield | Returns | F59 | 1.7e-13 | yes |
| val.A1.pv_dep_per_usd | Returns | F60 | 2.2e-16 | yes |
| val.A1.shield_at_price | Returns | F61 | 1.4e-14 | yes |
| val.A1.ev | Returns | F62 | 1.1e-13 | yes |
| val.A1.npv_vs_price | Returns | F63 | 1.7e-13 | yes |
| val.A1.breakeven_price | Returns | F64 | 3.4e-13 | yes |
| val.A2.R6.contracted | Returns | F67 | 2.1e-14 | yes |
| val.A2.R6.hedged | Returns | F68 | 0.0e+00 | yes |
| val.A2.R6.merchant | Returns | F69 | 4.6e-14 | yes |
| val.A2.R6.total | Returns | F70 | 2.1e-14 | yes |
| val.A2.shield_at_price | Returns | F72 | 4.3e-14 | yes |
| val.A2.ev | Returns | F73 | 4.3e-14 | yes |
| val.A2.npv_vs_price | Returns | F74 | 3.6e-15 | yes |
| val.A2.breakeven_price | Returns | F75 | 1.4e-14 | yes |
| val.A3.R7.contracted | Returns | F78 | 5.0e-14 | yes |
| val.A3.R7.hedged | Returns | F79 | 0.0e+00 | yes |
| val.A3.R7.merchant | Returns | F80 | 4.3e-14 | yes |
| val.A3.R7.total | Returns | F81 | 1.4e-14 | yes |
| val.A3.R8.contracted | Returns | F82 | 0.0e+00 | yes |
| val.A3.R8.hedged | Returns | F83 | 4.3e-14 | yes |
| val.A3.R8.merchant | Returns | F84 | 7.1e-15 | yes |
| val.A3.R8.total | Returns | F85 | 4.3e-14 | yes |
| val.A3.itc_pv | Returns | F88 | 7.1e-15 | yes |
| val.A3.shield | Returns | F89 | 3.9e-14 | yes |
| val.A3.ev | Returns | F90 | 3.1e-13 | yes |
| val.A3.price_pv | Returns | F91 | 4.0e-13 | yes |
| val.A3.npv_vs_price | Returns | F92 | 7.1e-15 | yes |
| sc.fund_nav_2025 | Returns | F98 | 2.8e-13 | yes |
| sc.fund_contributions | Returns | F99 | 2.0e-13 | yes |
| sc.fund_distributions_life | Returns | F100 | 3.0e-12 | yes |
| sc.fund_distributions_to_2025 | Returns | F101 | 6.1e-13 | yes |
| sc.fund_moic_life_x | Returns | F102 | 5.3e-15 | yes |
| sc.fund_moic_2025_x | Returns | F103 | 4.4e-16 | yes |
| sc.fund_irr_life_pct | Returns | F150 | 1.8e-14 | yes |
| sc.fund_irr_2025_pct | Returns | F151 | 2.8e-14 | yes |

### p90_1yr

| Key | Sheet | Location | Max diff | Pass |
|---|---|---|---|---|
| portfolio.north_atc | Operations | row 52 | 0.0e+00 | yes |
| portfolio.west_atc | Operations | row 53 | 0.0e+00 | yes |
| portfolio.south_atc | Operations | row 54 | 0.0e+00 | yes |
| portfolio.houston_atc | Operations | row 55 | 0.0e+00 | yes |
| portfolio.batt_rate | Operations | row 56 | 0.0e+00 | yes |
| portfolio.cap_hub_west_wind | Operations | row 57 | 0.0e+00 | yes |
| portfolio.cap_hub_panhandle_wind | Operations | row 58 | 0.0e+00 | yes |
| portfolio.cap_hub_west_solar | Operations | row 59 | 0.0e+00 | yes |
| portfolio.cap_hub_south_solar | Operations | row 60 | 0.0e+00 | yes |
| portfolio.cap_hub_coastal_wind | Operations | row 61 | 0.0e+00 | yes |
| R1.op_frac | Operations | row 63 | 0.0e+00 | yes |
| R1.own_share | Operations | row 65 | 1.9e-11 | yes |
| R1.hub_atc | Operations | row 66 | 0.0e+00 | yes |
| R1.deg | Operations | row 68 | 5.0e-11 | yes |
| R1.curt | Operations | row 69 | 0.0e+00 | yes |
| R1.gen_full | Operations | row 70 | 4.9e-11 | yes |
| R1.gen | Operations | row 71 | 4.9e-11 | yes |
| R1.cap_hub | Operations | row 72 | 0.0e+00 | yes |
| R1.cap_node | Operations | row 73 | 0.0e+00 | yes |
| R1.node_price | Operations | row 74 | 0.0e+00 | yes |
| R1.con_frac | Operations | row 75 | 0.0e+00 | yes |
| R1.con_vol | Operations | row 76 | 0.0e+00 | yes |
| R1.settle | Operations | row 77 | 2.0e-15 | yes |
| R1.mkt_gen | Operations | row 78 | 4.9e-11 | yes |
| R1.rev_contracted | Operations | row 79 | 0.0e+00 | yes |
| R1.rev_hedged | Operations | row 80 | 0.0e+00 | yes |
| R1.mkt_rev | Operations | row 81 | 4.9e-11 | yes |
| R1.revenue | Operations | row 82 | 4.9e-11 | yes |
| R1.rev_merchant | Operations | row 83 | 4.9e-11 | yes |
| R1.opex | Operations | row 84 | 4.9e-11 | yes |
| R1.land | Operations | row 85 | 4.7e-11 | yes |
| R1.bond | Operations | row 86 | 4.8e-11 | yes |
| R1.margin_tax | Operations | row 87 | 5.0e-11 | yes |
| R1.ebitda | Operations | row 88 | 4.9e-11 | yes |
| R1.aug | Operations | row 89 | 0.0e+00 | yes |
| R1.decom | Operations | row 90 | 3.3e-11 | yes |
| R1.cf | Operations | row 91 | 4.9e-11 | yes |
| R1.te_cash | Operations | row 92 | 0.0e+00 | yes |
| R1.mesa_tax_share | Operations | row 93 | 0.0e+00 | yes |
| R1.mesa_cf | Operations | row 94 | 4.8e-11 | yes |
| R1.mesa_taxable | Operations | row 95 | 4.8e-11 | yes |
| R1.s_contracted | Operations | row 97 | 0.0e+00 | yes |
| R1.s_hedged | Operations | row 98 | 4.9e-11 | yes |
| R1.s_merchant | Operations | row 99 | 4.9e-11 | yes |
| R1.mesa_rev | Operations | row 103 | 4.9e-11 | yes |
| R2.op_frac | Operations | row 105 | 4.1e-11 | yes |
| R2.own_share | Operations | row 107 | 1.9e-11 | yes |
| R2.hub_atc | Operations | row 108 | 0.0e+00 | yes |
| R2.deg | Operations | row 110 | 5.0e-11 | yes |
| R2.curt | Operations | row 111 | 0.0e+00 | yes |
| R2.gen_full | Operations | row 112 | 4.9e-11 | yes |
| R2.gen | Operations | row 113 | 4.9e-11 | yes |
| R2.cap_hub | Operations | row 114 | 0.0e+00 | yes |
| R2.cap_node | Operations | row 115 | 0.0e+00 | yes |
| R2.node_price | Operations | row 116 | 0.0e+00 | yes |
| R2.con_frac | Operations | row 117 | 4.1e-11 | yes |
| R2.con_vol | Operations | row 118 | 4.3e-11 | yes |
| R2.settle | Operations | row 119 | 3.9e-11 | yes |
| R2.mkt_gen | Operations | row 120 | 4.9e-11 | yes |
| R2.rev_contracted | Operations | row 121 | 3.9e-11 | yes |
| R2.rev_hedged | Operations | row 122 | 0.0e+00 | yes |
| R2.mkt_rev | Operations | row 123 | 5.0e-11 | yes |
| R2.revenue | Operations | row 124 | 5.0e-11 | yes |
| R2.rev_merchant | Operations | row 125 | 5.0e-11 | yes |
| R2.opex | Operations | row 126 | 4.7e-11 | yes |
| R2.land | Operations | row 127 | 4.8e-11 | yes |
| R2.bond | Operations | row 128 | 4.7e-11 | yes |
| R2.margin_tax | Operations | row 129 | 4.9e-11 | yes |
| R2.ebitda | Operations | row 130 | 4.9e-11 | yes |
| R2.aug | Operations | row 131 | 0.0e+00 | yes |
| R2.decom | Operations | row 132 | 4.0e-11 | yes |
| R2.cf | Operations | row 133 | 4.9e-11 | yes |
| R2.te_cash | Operations | row 134 | 0.0e+00 | yes |
| R2.mesa_tax_share | Operations | row 135 | 0.0e+00 | yes |
| R2.mesa_cf | Operations | row 136 | 4.9e-11 | yes |
| R2.mesa_taxable | Operations | row 137 | 4.9e-11 | yes |
| R2.s_contracted | Operations | row 139 | 4.2e-11 | yes |
| R2.s_hedged | Operations | row 140 | 0.0e+00 | yes |
| R2.s_merchant | Operations | row 141 | 4.2e-11 | yes |
| R2.mesa_rev | Operations | row 145 | 5.0e-11 | yes |
| R3.op_frac | Operations | row 147 | 4.9e-11 | yes |
| R3.own_share | Operations | row 149 | 1.9e-11 | yes |
| R3.hub_atc | Operations | row 150 | 0.0e+00 | yes |
| R3.deg | Operations | row 152 | 5.0e-11 | yes |
| R3.curt | Operations | row 153 | 0.0e+00 | yes |
| R3.gen_full | Operations | row 154 | 5.0e-11 | yes |
| R3.gen | Operations | row 155 | 5.0e-11 | yes |
| R3.cap_hub | Operations | row 156 | 0.0e+00 | yes |
| R3.cap_node | Operations | row 157 | 0.0e+00 | yes |
| R3.node_price | Operations | row 158 | 0.0e+00 | yes |
| R3.con_frac | Operations | row 159 | 0.0e+00 | yes |
| R3.con_vol | Operations | row 160 | 3.9e-11 | yes |
| R3.settle | Operations | row 161 | 4.9e-11 | yes |
| R3.mkt_gen | Operations | row 162 | 5.0e-11 | yes |
| R3.rev_contracted | Operations | row 163 | 0.0e+00 | yes |
| R3.rev_hedged | Operations | row 164 | 0.0e+00 | yes |
| R3.mkt_rev | Operations | row 165 | 4.7e-11 | yes |
| R3.revenue | Operations | row 166 | 4.7e-11 | yes |
| R3.rev_merchant | Operations | row 167 | 4.7e-11 | yes |
| R3.opex | Operations | row 168 | 5.0e-11 | yes |
| R3.land | Operations | row 169 | 4.6e-11 | yes |
| R3.bond | Operations | row 170 | 4.8e-11 | yes |
| R3.margin_tax | Operations | row 171 | 4.9e-11 | yes |
| R3.ebitda | Operations | row 172 | 4.8e-11 | yes |
| R3.aug | Operations | row 173 | 0.0e+00 | yes |
| R3.decom | Operations | row 174 | 8.9e-12 | yes |
| R3.cf | Operations | row 175 | 4.8e-11 | yes |
| R3.te_cash | Operations | row 177 | 0.0e+00 | yes |
| R3.mesa_tax_share | Operations | row 178 | 0.0e+00 | yes |
| R3.mesa_cf | Operations | row 179 | 4.8e-11 | yes |
| R3.mesa_taxable | Operations | row 180 | 4.8e-11 | yes |
| R3.s_contracted | Operations | row 182 | 4.4e-11 | yes |
| R3.s_hedged | Operations | row 183 | 0.0e+00 | yes |
| R3.s_merchant | Operations | row 184 | 4.4e-11 | yes |
| R3.mesa_rev | Operations | row 188 | 4.9e-11 | yes |
| R3.ptc_total | Operations | row 189 | 4.9e-11 | yes |
| R4.op_frac | Operations | row 191 | 2.9e-11 | yes |
| R4.own_share | Operations | row 193 | 1.9e-11 | yes |
| R4.hub_atc | Operations | row 194 | 0.0e+00 | yes |
| R4.deg | Operations | row 196 | 5.0e-11 | yes |
| R4.curt | Operations | row 197 | 0.0e+00 | yes |
| R4.gen_full | Operations | row 198 | 4.8e-11 | yes |
| R4.gen | Operations | row 199 | 4.8e-11 | yes |
| R4.cap_hub | Operations | row 200 | 0.0e+00 | yes |
| R4.cap_node | Operations | row 201 | 0.0e+00 | yes |
| R4.node_price | Operations | row 202 | 0.0e+00 | yes |
| R4.con_frac | Operations | row 203 | 0.0e+00 | yes |
| R4.con_vol | Operations | row 204 | 0.0e+00 | yes |
| R4.settle | Operations | row 205 | 1.0e-15 | yes |
| R4.mkt_gen | Operations | row 206 | 4.8e-11 | yes |
| R4.rev_contracted | Operations | row 207 | 0.0e+00 | yes |
| R4.rev_hedged | Operations | row 208 | 0.0e+00 | yes |
| R4.mkt_rev | Operations | row 209 | 5.0e-11 | yes |
| R4.revenue | Operations | row 210 | 5.0e-11 | yes |
| R4.rev_merchant | Operations | row 211 | 5.0e-11 | yes |
| R4.opex | Operations | row 212 | 5.0e-11 | yes |
| R4.land | Operations | row 213 | 0.0e+00 | yes |
| R4.bond | Operations | row 214 | 5.0e-11 | yes |
| R4.margin_tax | Operations | row 215 | 5.0e-11 | yes |
| R4.ebitda | Operations | row 216 | 4.9e-11 | yes |
| R4.aug | Operations | row 217 | 0.0e+00 | yes |
| R4.decom | Operations | row 218 | 1.9e-11 | yes |
| R4.cf | Operations | row 219 | 4.9e-11 | yes |
| R4.te_cash | Operations | row 220 | 0.0e+00 | yes |
| R4.mesa_tax_share | Operations | row 221 | 0.0e+00 | yes |
| R4.mesa_cf | Operations | row 222 | 4.7e-11 | yes |
| R4.mesa_taxable | Operations | row 223 | 4.7e-11 | yes |
| R4.s_contracted | Operations | row 225 | 0.0e+00 | yes |
| R4.s_hedged | Operations | row 226 | 3.6e-11 | yes |
| R4.s_merchant | Operations | row 227 | 3.6e-11 | yes |
| R4.mesa_rev | Operations | row 231 | 5.0e-11 | yes |
| R5.op_frac | Operations | row 233 | 3.7e-11 | yes |
| R5.own_share | Operations | row 235 | 1.9e-11 | yes |
| R5.hub_atc | Operations | row 236 | 0.0e+00 | yes |
| R5.deg | Operations | row 238 | 5.0e-11 | yes |
| R5.curt | Operations | row 239 | 0.0e+00 | yes |
| R5.gen_full | Operations | row 240 | 4.7e-11 | yes |
| R5.gen | Operations | row 241 | 4.7e-11 | yes |
| R5.cap_hub | Operations | row 242 | 0.0e+00 | yes |
| R5.cap_node | Operations | row 243 | 0.0e+00 | yes |
| R5.node_price | Operations | row 244 | 0.0e+00 | yes |
| R5.con_frac | Operations | row 245 | 4.1e-11 | yes |
| R5.con_vol | Operations | row 246 | 3.9e-11 | yes |
| R5.settle | Operations | row 247 | 4.9e-11 | yes |
| R5.mkt_gen | Operations | row 248 | 4.7e-11 | yes |
| R5.rev_contracted | Operations | row 249 | 4.6e-11 | yes |
| R5.rev_hedged | Operations | row 250 | 0.0e+00 | yes |
| R5.mkt_rev | Operations | row 251 | 4.9e-11 | yes |
| R5.revenue | Operations | row 252 | 4.9e-11 | yes |
| R5.rev_merchant | Operations | row 253 | 4.9e-11 | yes |
| R5.opex | Operations | row 254 | 4.9e-11 | yes |
| R5.land | Operations | row 255 | 0.0e+00 | yes |
| R5.bond | Operations | row 256 | 4.9e-11 | yes |
| R5.margin_tax | Operations | row 257 | 4.8e-11 | yes |
| R5.ebitda | Operations | row 258 | 4.9e-11 | yes |
| R5.aug | Operations | row 259 | 0.0e+00 | yes |
| R5.decom | Operations | row 260 | 2.0e-13 | yes |
| R5.cf | Operations | row 261 | 4.9e-11 | yes |
| R5.te_cash | Operations | row 263 | 4.4e-11 | yes |
| R5.mesa_tax_share | Operations | row 264 | 1.4e-12 | yes |
| R5.mesa_cf | Operations | row 265 | 4.7e-11 | yes |
| R5.mesa_taxable | Operations | row 266 | 4.7e-11 | yes |
| R5.s_contracted | Operations | row 268 | 4.5e-11 | yes |
| R5.s_hedged | Operations | row 269 | 0.0e+00 | yes |
| R5.s_merchant | Operations | row 270 | 4.5e-11 | yes |
| R5.mesa_rev | Operations | row 274 | 5.0e-11 | yes |
| R6.op_frac | Operations | row 276 | 4.2e-11 | yes |
| R6.own_share | Operations | row 278 | 2.4e-11 | yes |
| R6.hub_atc | Operations | row 279 | 0.0e+00 | yes |
| R6.con_frac | Operations | row 280 | 4.2e-11 | yes |
| R6.settle | Operations | row 281 | 4.0e-11 | yes |
| R6.stor_rev | Operations | row 282 | 3.2e-11 | yes |
| R6.rev_contracted | Operations | row 283 | 4.0e-11 | yes |
| R6.rev_hedged | Operations | row 284 | 0.0e+00 | yes |
| R6.revenue | Operations | row 285 | 4.0e-11 | yes |
| R6.rev_merchant | Operations | row 286 | 3.2e-11 | yes |
| R6.opex | Operations | row 287 | 4.9e-11 | yes |
| R6.land | Operations | row 288 | 0.0e+00 | yes |
| R6.bond | Operations | row 289 | 4.8e-11 | yes |
| R6.margin_tax | Operations | row 290 | 5.0e-11 | yes |
| R6.ebitda | Operations | row 291 | 5.0e-11 | yes |
| R6.aug | Operations | row 292 | 4.8e-12 | yes |
| R6.decom | Operations | row 293 | 2.5e-11 | yes |
| R6.cf | Operations | row 294 | 5.0e-11 | yes |
| R6.te_cash | Operations | row 295 | 0.0e+00 | yes |
| R6.mesa_tax_share | Operations | row 296 | 0.0e+00 | yes |
| R6.mesa_cf | Operations | row 297 | 5.0e-11 | yes |
| R6.mesa_taxable | Operations | row 298 | 5.0e-11 | yes |
| R6.s_contracted | Operations | row 300 | 3.8e-11 | yes |
| R6.s_hedged | Operations | row 301 | 0.0e+00 | yes |
| R6.s_merchant | Operations | row 302 | 3.8e-11 | yes |
| R6.mesa_rev | Operations | row 306 | 4.0e-11 | yes |
| R7.op_frac | Operations | row 308 | 4.4e-11 | yes |
| R7.own_share | Operations | row 310 | 0.0e+00 | yes |
| R7.hub_atc | Operations | row 311 | 0.0e+00 | yes |
| R7.con_frac | Operations | row 312 | 4.4e-11 | yes |
| R7.settle | Operations | row 314 | 3.6e-11 | yes |
| R7.stor_rev | Operations | row 315 | 4.6e-11 | yes |
| R7.rev_contracted | Operations | row 316 | 3.6e-11 | yes |
| R7.rev_hedged | Operations | row 317 | 0.0e+00 | yes |
| R7.revenue | Operations | row 318 | 4.6e-11 | yes |
| R7.rev_merchant | Operations | row 319 | 4.6e-11 | yes |
| R7.opex | Operations | row 320 | 5.0e-11 | yes |
| R7.land | Operations | row 321 | 0.0e+00 | yes |
| R7.bond | Operations | row 322 | 4.8e-11 | yes |
| R7.margin_tax | Operations | row 323 | 5.0e-11 | yes |
| R7.ebitda | Operations | row 324 | 5.0e-11 | yes |
| R7.aug | Operations | row 325 | 3.8e-11 | yes |
| R7.decom | Operations | row 326 | 2.3e-11 | yes |
| R7.cf | Operations | row 327 | 5.0e-11 | yes |
| R7.te_cash | Operations | row 328 | 0.0e+00 | yes |
| R7.mesa_tax_share | Operations | row 329 | 0.0e+00 | yes |
| R7.mesa_cf | Operations | row 330 | 5.0e-11 | yes |
| R7.mesa_taxable | Operations | row 331 | 5.0e-11 | yes |
| R7.s_contracted | Operations | row 333 | 3.1e-11 | yes |
| R7.s_hedged | Operations | row 334 | 0.0e+00 | yes |
| R7.s_merchant | Operations | row 335 | 3.1e-11 | yes |
| R7.mesa_rev | Operations | row 339 | 4.6e-11 | yes |
| R8.op_frac | Operations | row 341 | 4.6e-11 | yes |
| R8.own_share | Operations | row 343 | 0.0e+00 | yes |
| R8.hub_atc | Operations | row 344 | 0.0e+00 | yes |
| R8.deg | Operations | row 346 | 4.7e-11 | yes |
| R8.curt | Operations | row 347 | 0.0e+00 | yes |
| R8.gen_full | Operations | row 348 | 5.0e-11 | yes |
| R8.gen | Operations | row 349 | 5.0e-11 | yes |
| R8.cap_hub | Operations | row 350 | 0.0e+00 | yes |
| R8.cap_node | Operations | row 351 | 0.0e+00 | yes |
| R8.node_price | Operations | row 352 | 0.0e+00 | yes |
| R8.con_frac | Operations | row 353 | 0.0e+00 | yes |
| R8.con_vol | Operations | row 354 | 0.0e+00 | yes |
| R8.settle | Operations | row 355 | 4.8e-11 | yes |
| R8.mkt_gen | Operations | row 356 | 5.0e-11 | yes |
| R8.rev_contracted | Operations | row 357 | 0.0e+00 | yes |
| R8.rev_hedged | Operations | row 358 | 0.0e+00 | yes |
| R8.mkt_rev | Operations | row 359 | 4.6e-11 | yes |
| R8.revenue | Operations | row 360 | 4.8e-11 | yes |
| R8.rev_merchant | Operations | row 361 | 4.8e-11 | yes |
| R8.opex | Operations | row 362 | 5.0e-11 | yes |
| R8.land | Operations | row 363 | 0.0e+00 | yes |
| R8.bond | Operations | row 364 | 4.8e-11 | yes |
| R8.margin_tax | Operations | row 365 | 4.7e-11 | yes |
| R8.ebitda | Operations | row 366 | 4.6e-11 | yes |
| R8.aug | Operations | row 367 | 0.0e+00 | yes |
| R8.decom | Operations | row 368 | 3.5e-11 | yes |
| R8.cf | Operations | row 369 | 4.7e-11 | yes |
| R8.te_cash | Operations | row 370 | 0.0e+00 | yes |
| R8.mesa_tax_share | Operations | row 371 | 0.0e+00 | yes |
| R8.mesa_cf | Operations | row 372 | 4.7e-11 | yes |
| R8.mesa_taxable | Operations | row 373 | 4.7e-11 | yes |
| R8.s_contracted | Operations | row 375 | 0.0e+00 | yes |
| R8.s_hedged | Operations | row 376 | 4.1e-11 | yes |
| R8.s_merchant | Operations | row 377 | 4.1e-11 | yes |
| R8.mesa_rev | Operations | row 381 | 4.8e-11 | yes |
| portfolio.am_cost | Operations | row 384 | 5.0e-11 | yes |
| portfolio.mesa_rev_contracted_a1 | Operations | row 386 | 4.7e-11 | yes |
| portfolio.mesa_rev_hedged_a1 | Operations | row 387 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_a1 | Operations | row 388 | 4.7e-11 | yes |
| portfolio.mesa_rev_a1 | Operations | row 389 | 4.6e-11 | yes |
| portfolio.mesa_rev_contracted_all | Operations | row 391 | 4.7e-11 | yes |
| portfolio.mesa_rev_hedged_all | Operations | row 392 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_all | Operations | row 393 | 5.0e-11 | yes |
| portfolio.mesa_rev_all | Operations | row 394 | 5.0e-11 | yes |
| portfolio.cfads_a1 | Operations | row 400 | 5.0e-11 | yes |
| portfolio.cfads_all | Operations | row 401 | 4.9e-11 | yes |
| portfolio.cfads_a3 | Operations | row 402 | 4.7e-11 | yes |
| portfolio.share_contracted_a1 | Operations | row 403 | 4.6e-11 | yes |
| portfolio.share_hedged_a1 | Operations | row 404 | 4.4e-11 | yes |
| portfolio.share_merchant_a1 | Operations | row 405 | 4.9e-11 | yes |
| portfolio.share_contracted_all | Operations | row 409 | 4.9e-11 | yes |
| portfolio.share_hedged_all | Operations | row 410 | 5.0e-11 | yes |
| portfolio.share_merchant_all | Operations | row 411 | 5.0e-11 | yes |
| finance.dep | Tax | row 24 | 0.0e+00 | yes |
| finance.taxable_ops | Tax | row 25 | 4.9e-11 | yes |
| finance.tl_open | Debt | row 14 | 4.8e-11 | yes |
| finance.tl_int | Debt | row 15 | 3.9e-11 | yes |
| finance.tl_prin | Debt | row 16 | 3.1e-11 | yes |
| finance.tl_prepay | Debt | row 17 | 2.6e-11 | yes |
| finance.tl_ds | Debt | row 18 | 4.9e-11 | yes |
| finance.rf_open | Debt | row 23 | 3.6e-11 | yes |
| finance.rf_int | Debt | row 24 | 4.4e-11 | yes |
| finance.rf_prin | Debt | row 25 | 4.4e-11 | yes |
| finance.rf_prepay | Debt | row 26 | 2.7e-11 | yes |
| finance.rf_ds | Debt | row 27 | 3.0e-11 | yes |
| finance.u_open | Debt | row 31 | 4.7e-11 | yes |
| finance.u_int | Debt | row 32 | 4.8e-11 | yes |
| finance.u_prin | Debt | row 33 | 4.9e-11 | yes |
| finance.u_ds | Debt | row 34 | 4.3e-11 | yes |
| finance.hc1_open | Debt | row 46 | 3.9e-11 | yes |
| finance.hc1_int | Debt | row 47 | 2.4e-11 | yes |
| finance.hc1_amort | Debt | row 48 | 1.4e-11 | yes |
| finance.hc1_sweep | Debt | row 49 | 3.8e-11 | yes |
| finance.hc1_repay | Debt | row 51 | 1.3e-11 | yes |
| finance.hc2_open | Debt | row 53 | 2.6e-11 | yes |
| finance.hc2_int | Debt | row 54 | 2.8e-11 | yes |
| finance.hc2_amort | Debt | row 55 | 3.9e-11 | yes |
| finance.hc2_sweep | Debt | row 56 | 4.0e-11 | yes |
| finance.hc2_repay | Debt | row 58 | 2.7e-11 | yes |
| finance.hc3_open | Debt | row 60 | 4.9e-11 | yes |
| finance.hc3_int | Debt | row 61 | 4.8e-11 | yes |
| finance.hc3_amort | Debt | row 62 | 3.2e-12 | yes |
| finance.hc3_sweep | Debt | row 63 | 4.0e-11 | yes |
| finance.hc_ds | Debt | row 67 | 4.5e-11 | yes |
| finance.taxable_income | Tax | row 29 | 5.0e-11 | yes |
| finance.nol_open | Tax | row 30 | 5.0e-11 | yes |
| finance.nol_used | Tax | row 31 | 4.8e-11 | yes |
| finance.tax | Tax | row 32 | 5.0e-11 | yes |
| finance.nol_close | Tax | row 33 | 5.0e-11 | yes |
| finance.opco_ds | Waterfall | row 9 | 4.9e-11 | yes |
| finance.opco_dist | Waterfall | row 10 | 4.9e-11 | yes |
| finance.recap_opco | Waterfall | row 11 | 3.6e-11 | yes |
| finance.hc_excess | Waterfall | row 16 | 5.0e-11 | yes |
| finance.fund_dist_ops | Waterfall | row 19 | 5.0e-11 | yes |
| finance.recap_hold | Waterfall | row 20 | 3.6e-11 | yes |
| finance.recap_total | Waterfall | row 21 | 2.8e-11 | yes |
| finance.fund_dist | Waterfall | row 22 | 5.0e-11 | yes |
| finance.dscr_tl | Ratios | row 8 | 5.0e-11 | yes |
| finance.dscr_rf | Ratios | row 9 | 0.0e+00 | yes |
| finance.dscr_u | Ratios | row 10 | 5.0e-11 | yes |
| finance.dscr_opco | Ratios | row 11 | 5.0e-11 | yes |
| finance.hc_cov | Ratios | row 12 | 5.0e-11 | yes |
| finance.nav_df | Returns | row 96 | 5.0e-11 | yes |
| su.A1.opco_fee | Funding | F147 | 0.0e+00 | yes |
| su.A1.holdco_oid | Funding | F148 | 1.1e-15 | yes |
| su.A1.uses | Funding | F149 | 4.0e-13 | yes |
| su.A1.equity | Funding | F150 | 4.3e-14 | yes |
| su.A2.fee | Funding | F151 | 1.1e-16 | yes |
| su.A2.uses | Funding | F152 | 4.3e-14 | yes |
| su.A2.equity | Funding | F153 | 3.6e-15 | yes |
| su.A3.r8_deposit | Funding | F154 | 3.6e-15 | yes |
| su.A3.oid | Funding | F155 | 3.3e-16 | yes |
| su.A3.itc7_proceeds | Funding | F156 | 0.0e+00 | yes |
| su.A3.itc8_proceeds | Funding | F157 | 3.6e-15 | yes |
| su.A3.eq_signing | Funding | F159 | 0.0e+00 | yes |
| su.A3.carry | Funding | F160 | 1.4e-14 | yes |
| su.A3.eq_r7 | Funding | F162 | 0.0e+00 | yes |
| su.A3.carry2 | Funding | F163 | 4.9e-15 | yes |
| su.A3.eq_r8 | Funding | F165 | 4.3e-14 | yes |
| su.A3.cash_left_after_r8 | Funding | F166 | 0.0e+00 | yes |
| su.A3.uses | Funding | F167 | 1.4e-13 | yes |
| su.A3.equity | Funding | F168 | 4.3e-14 | yes |
| refi.mtm_opco_receivable | Funding | F174 | 4.4e-15 | yes |
| refi.mtm_redfern_payable | Funding | F175 | 4.4e-16 | yes |
| refi.costs | Funding | F176 | 4.0e-15 | yes |
| refi.tl_repay | Funding | F177 | 2.8e-13 | yes |
| refi.rf_repay | Funding | F178 | 5.0e-14 | yes |
| refi.opco_net | Funding | F179 | 8.5e-14 | yes |
| sc.tl_dscr_min_2022_2025 | Ratios | F15 | 2.4e-15 | yes |
| sc.tl_dscr_avg_2022_2025 | Ratios | F16 | 2.9e-15 | yes |
| sc.uspp_dscr_min_2026_2043 | Ratios | F17 | 1.1e-15 | yes |
| sc.uspp_dscr_avg_2026_2043 | Ratios | F18 | 4.4e-16 | yes |
| sc.rf_dscr_min | Ratios | F19 | 0.0e+00 | yes |
| sc.rf_dscr_avg | Ratios | F20 | 0.0e+00 | yes |
| sc.holdco_cov_min_2023_2031 | Ratios | F21 | 1.3e-15 | yes |
| sc.holdco_cov_avg_2023_2031 | Ratios | F22 | 2.2e-15 | yes |
| sc.fund_nav_2025 | Returns | F98 | 6.4e-14 | yes |
| sc.fund_contributions | Returns | F99 | 2.0e-13 | yes |
| sc.fund_distributions_life | Returns | F100 | 2.8e-13 | yes |
| sc.fund_distributions_to_2025 | Returns | F101 | 1.8e-13 | yes |
| sc.fund_moic_life_x | Returns | F102 | 8.9e-16 | yes |
| sc.fund_moic_2025_x | Returns | F103 | 8.9e-16 | yes |
| sc.fund_irr_life_pct | Returns | F150 | 1.8e-15 | yes |
| sc.fund_irr_2025_pct | Returns | F151 | 3.5e-14 | yes |

### p90_10yr

| Key | Sheet | Location | Max diff | Pass |
|---|---|---|---|---|
| portfolio.north_atc | Operations | row 52 | 0.0e+00 | yes |
| portfolio.west_atc | Operations | row 53 | 0.0e+00 | yes |
| portfolio.south_atc | Operations | row 54 | 0.0e+00 | yes |
| portfolio.houston_atc | Operations | row 55 | 0.0e+00 | yes |
| portfolio.batt_rate | Operations | row 56 | 0.0e+00 | yes |
| portfolio.cap_hub_west_wind | Operations | row 57 | 0.0e+00 | yes |
| portfolio.cap_hub_panhandle_wind | Operations | row 58 | 0.0e+00 | yes |
| portfolio.cap_hub_west_solar | Operations | row 59 | 0.0e+00 | yes |
| portfolio.cap_hub_south_solar | Operations | row 60 | 0.0e+00 | yes |
| portfolio.cap_hub_coastal_wind | Operations | row 61 | 0.0e+00 | yes |
| R1.op_frac | Operations | row 63 | 0.0e+00 | yes |
| R1.own_share | Operations | row 65 | 1.9e-11 | yes |
| R1.hub_atc | Operations | row 66 | 0.0e+00 | yes |
| R1.deg | Operations | row 68 | 5.0e-11 | yes |
| R1.curt | Operations | row 69 | 0.0e+00 | yes |
| R1.gen_full | Operations | row 70 | 5.0e-11 | yes |
| R1.gen | Operations | row 71 | 5.0e-11 | yes |
| R1.cap_hub | Operations | row 72 | 0.0e+00 | yes |
| R1.cap_node | Operations | row 73 | 0.0e+00 | yes |
| R1.node_price | Operations | row 74 | 0.0e+00 | yes |
| R1.con_frac | Operations | row 75 | 0.0e+00 | yes |
| R1.con_vol | Operations | row 76 | 0.0e+00 | yes |
| R1.settle | Operations | row 77 | 2.0e-15 | yes |
| R1.mkt_gen | Operations | row 78 | 5.0e-11 | yes |
| R1.rev_contracted | Operations | row 79 | 0.0e+00 | yes |
| R1.rev_hedged | Operations | row 80 | 0.0e+00 | yes |
| R1.mkt_rev | Operations | row 81 | 5.0e-11 | yes |
| R1.revenue | Operations | row 82 | 5.0e-11 | yes |
| R1.rev_merchant | Operations | row 83 | 5.0e-11 | yes |
| R1.opex | Operations | row 84 | 4.9e-11 | yes |
| R1.land | Operations | row 85 | 4.9e-11 | yes |
| R1.bond | Operations | row 86 | 4.8e-11 | yes |
| R1.margin_tax | Operations | row 87 | 4.4e-11 | yes |
| R1.ebitda | Operations | row 88 | 4.8e-11 | yes |
| R1.aug | Operations | row 89 | 0.0e+00 | yes |
| R1.decom | Operations | row 90 | 3.3e-11 | yes |
| R1.cf | Operations | row 91 | 4.8e-11 | yes |
| R1.te_cash | Operations | row 92 | 0.0e+00 | yes |
| R1.mesa_tax_share | Operations | row 93 | 0.0e+00 | yes |
| R1.mesa_cf | Operations | row 94 | 4.8e-11 | yes |
| R1.mesa_taxable | Operations | row 95 | 4.8e-11 | yes |
| R1.s_contracted | Operations | row 97 | 0.0e+00 | yes |
| R1.s_hedged | Operations | row 98 | 4.3e-11 | yes |
| R1.s_merchant | Operations | row 99 | 4.3e-11 | yes |
| R1.mesa_rev | Operations | row 103 | 5.0e-11 | yes |
| R2.op_frac | Operations | row 105 | 4.1e-11 | yes |
| R2.own_share | Operations | row 107 | 1.9e-11 | yes |
| R2.hub_atc | Operations | row 108 | 0.0e+00 | yes |
| R2.deg | Operations | row 110 | 5.0e-11 | yes |
| R2.curt | Operations | row 111 | 0.0e+00 | yes |
| R2.gen_full | Operations | row 112 | 4.8e-11 | yes |
| R2.gen | Operations | row 113 | 4.6e-11 | yes |
| R2.cap_hub | Operations | row 114 | 0.0e+00 | yes |
| R2.cap_node | Operations | row 115 | 0.0e+00 | yes |
| R2.node_price | Operations | row 116 | 0.0e+00 | yes |
| R2.con_frac | Operations | row 117 | 4.1e-11 | yes |
| R2.con_vol | Operations | row 118 | 4.0e-11 | yes |
| R2.settle | Operations | row 119 | 4.4e-11 | yes |
| R2.mkt_gen | Operations | row 120 | 4.6e-11 | yes |
| R2.rev_contracted | Operations | row 121 | 4.4e-11 | yes |
| R2.rev_hedged | Operations | row 122 | 0.0e+00 | yes |
| R2.mkt_rev | Operations | row 123 | 4.8e-11 | yes |
| R2.revenue | Operations | row 124 | 4.6e-11 | yes |
| R2.rev_merchant | Operations | row 125 | 4.8e-11 | yes |
| R2.opex | Operations | row 126 | 4.7e-11 | yes |
| R2.land | Operations | row 127 | 4.4e-11 | yes |
| R2.bond | Operations | row 128 | 4.7e-11 | yes |
| R2.margin_tax | Operations | row 129 | 4.9e-11 | yes |
| R2.ebitda | Operations | row 130 | 4.9e-11 | yes |
| R2.aug | Operations | row 131 | 0.0e+00 | yes |
| R2.decom | Operations | row 132 | 4.0e-11 | yes |
| R2.cf | Operations | row 133 | 4.9e-11 | yes |
| R2.te_cash | Operations | row 134 | 0.0e+00 | yes |
| R2.mesa_tax_share | Operations | row 135 | 0.0e+00 | yes |
| R2.mesa_cf | Operations | row 136 | 4.9e-11 | yes |
| R2.mesa_taxable | Operations | row 137 | 4.9e-11 | yes |
| R2.s_contracted | Operations | row 139 | 4.2e-11 | yes |
| R2.s_hedged | Operations | row 140 | 0.0e+00 | yes |
| R2.s_merchant | Operations | row 141 | 4.2e-11 | yes |
| R2.mesa_rev | Operations | row 145 | 4.6e-11 | yes |
| R3.op_frac | Operations | row 147 | 4.9e-11 | yes |
| R3.own_share | Operations | row 149 | 1.9e-11 | yes |
| R3.hub_atc | Operations | row 150 | 0.0e+00 | yes |
| R3.deg | Operations | row 152 | 5.0e-11 | yes |
| R3.curt | Operations | row 153 | 0.0e+00 | yes |
| R3.gen_full | Operations | row 154 | 5.0e-11 | yes |
| R3.gen | Operations | row 155 | 5.0e-11 | yes |
| R3.cap_hub | Operations | row 156 | 0.0e+00 | yes |
| R3.cap_node | Operations | row 157 | 0.0e+00 | yes |
| R3.node_price | Operations | row 158 | 0.0e+00 | yes |
| R3.con_frac | Operations | row 159 | 0.0e+00 | yes |
| R3.con_vol | Operations | row 160 | 4.5e-11 | yes |
| R3.settle | Operations | row 161 | 4.2e-11 | yes |
| R3.mkt_gen | Operations | row 162 | 5.0e-11 | yes |
| R3.rev_contracted | Operations | row 163 | 0.0e+00 | yes |
| R3.rev_hedged | Operations | row 164 | 0.0e+00 | yes |
| R3.mkt_rev | Operations | row 165 | 4.8e-11 | yes |
| R3.revenue | Operations | row 166 | 4.7e-11 | yes |
| R3.rev_merchant | Operations | row 167 | 4.7e-11 | yes |
| R3.opex | Operations | row 168 | 5.0e-11 | yes |
| R3.land | Operations | row 169 | 4.7e-11 | yes |
| R3.bond | Operations | row 170 | 4.8e-11 | yes |
| R3.margin_tax | Operations | row 171 | 4.9e-11 | yes |
| R3.ebitda | Operations | row 172 | 4.7e-11 | yes |
| R3.aug | Operations | row 173 | 0.0e+00 | yes |
| R3.decom | Operations | row 174 | 8.9e-12 | yes |
| R3.cf | Operations | row 175 | 4.7e-11 | yes |
| R3.te_cash | Operations | row 177 | 0.0e+00 | yes |
| R3.mesa_tax_share | Operations | row 178 | 0.0e+00 | yes |
| R3.mesa_cf | Operations | row 179 | 4.9e-11 | yes |
| R3.mesa_taxable | Operations | row 180 | 4.9e-11 | yes |
| R3.s_contracted | Operations | row 182 | 4.7e-11 | yes |
| R3.s_hedged | Operations | row 183 | 0.0e+00 | yes |
| R3.s_merchant | Operations | row 184 | 4.7e-11 | yes |
| R3.mesa_rev | Operations | row 188 | 4.9e-11 | yes |
| R3.ptc_total | Operations | row 189 | 4.9e-11 | yes |
| R4.op_frac | Operations | row 191 | 2.9e-11 | yes |
| R4.own_share | Operations | row 193 | 1.9e-11 | yes |
| R4.hub_atc | Operations | row 194 | 0.0e+00 | yes |
| R4.deg | Operations | row 196 | 5.0e-11 | yes |
| R4.curt | Operations | row 197 | 0.0e+00 | yes |
| R4.gen_full | Operations | row 198 | 4.9e-11 | yes |
| R4.gen | Operations | row 199 | 4.9e-11 | yes |
| R4.cap_hub | Operations | row 200 | 0.0e+00 | yes |
| R4.cap_node | Operations | row 201 | 0.0e+00 | yes |
| R4.node_price | Operations | row 202 | 0.0e+00 | yes |
| R4.con_frac | Operations | row 203 | 0.0e+00 | yes |
| R4.con_vol | Operations | row 204 | 0.0e+00 | yes |
| R4.settle | Operations | row 205 | 1.0e-15 | yes |
| R4.mkt_gen | Operations | row 206 | 4.9e-11 | yes |
| R4.rev_contracted | Operations | row 207 | 0.0e+00 | yes |
| R4.rev_hedged | Operations | row 208 | 0.0e+00 | yes |
| R4.mkt_rev | Operations | row 209 | 4.8e-11 | yes |
| R4.revenue | Operations | row 210 | 4.8e-11 | yes |
| R4.rev_merchant | Operations | row 211 | 4.8e-11 | yes |
| R4.opex | Operations | row 212 | 5.0e-11 | yes |
| R4.land | Operations | row 213 | 0.0e+00 | yes |
| R4.bond | Operations | row 214 | 5.0e-11 | yes |
| R4.margin_tax | Operations | row 215 | 4.7e-11 | yes |
| R4.ebitda | Operations | row 216 | 5.0e-11 | yes |
| R4.aug | Operations | row 217 | 0.0e+00 | yes |
| R4.decom | Operations | row 218 | 1.9e-11 | yes |
| R4.cf | Operations | row 219 | 5.0e-11 | yes |
| R4.te_cash | Operations | row 220 | 0.0e+00 | yes |
| R4.mesa_tax_share | Operations | row 221 | 0.0e+00 | yes |
| R4.mesa_cf | Operations | row 222 | 5.0e-11 | yes |
| R4.mesa_taxable | Operations | row 223 | 5.0e-11 | yes |
| R4.s_contracted | Operations | row 225 | 0.0e+00 | yes |
| R4.s_hedged | Operations | row 226 | 4.9e-11 | yes |
| R4.s_merchant | Operations | row 227 | 4.9e-11 | yes |
| R4.mesa_rev | Operations | row 231 | 4.8e-11 | yes |
| R5.op_frac | Operations | row 233 | 3.7e-11 | yes |
| R5.own_share | Operations | row 235 | 1.9e-11 | yes |
| R5.hub_atc | Operations | row 236 | 0.0e+00 | yes |
| R5.deg | Operations | row 238 | 5.0e-11 | yes |
| R5.curt | Operations | row 239 | 0.0e+00 | yes |
| R5.gen_full | Operations | row 240 | 4.7e-11 | yes |
| R5.gen | Operations | row 241 | 4.7e-11 | yes |
| R5.cap_hub | Operations | row 242 | 0.0e+00 | yes |
| R5.cap_node | Operations | row 243 | 0.0e+00 | yes |
| R5.node_price | Operations | row 244 | 0.0e+00 | yes |
| R5.con_frac | Operations | row 245 | 4.1e-11 | yes |
| R5.con_vol | Operations | row 246 | 4.7e-11 | yes |
| R5.settle | Operations | row 247 | 5.0e-11 | yes |
| R5.mkt_gen | Operations | row 248 | 4.7e-11 | yes |
| R5.rev_contracted | Operations | row 249 | 3.7e-11 | yes |
| R5.rev_hedged | Operations | row 250 | 0.0e+00 | yes |
| R5.mkt_rev | Operations | row 251 | 4.4e-11 | yes |
| R5.revenue | Operations | row 252 | 4.9e-11 | yes |
| R5.rev_merchant | Operations | row 253 | 4.8e-11 | yes |
| R5.opex | Operations | row 254 | 4.9e-11 | yes |
| R5.land | Operations | row 255 | 0.0e+00 | yes |
| R5.bond | Operations | row 256 | 4.9e-11 | yes |
| R5.margin_tax | Operations | row 257 | 4.9e-11 | yes |
| R5.ebitda | Operations | row 258 | 4.7e-11 | yes |
| R5.aug | Operations | row 259 | 0.0e+00 | yes |
| R5.decom | Operations | row 260 | 2.0e-13 | yes |
| R5.cf | Operations | row 261 | 4.7e-11 | yes |
| R5.te_cash | Operations | row 263 | 4.4e-11 | yes |
| R5.mesa_tax_share | Operations | row 264 | 1.4e-12 | yes |
| R5.mesa_cf | Operations | row 265 | 4.8e-11 | yes |
| R5.mesa_taxable | Operations | row 266 | 4.8e-11 | yes |
| R5.s_contracted | Operations | row 268 | 4.5e-11 | yes |
| R5.s_hedged | Operations | row 269 | 0.0e+00 | yes |
| R5.s_merchant | Operations | row 270 | 4.5e-11 | yes |
| R5.mesa_rev | Operations | row 274 | 4.9e-11 | yes |
| R6.op_frac | Operations | row 276 | 4.2e-11 | yes |
| R6.own_share | Operations | row 278 | 2.4e-11 | yes |
| R6.hub_atc | Operations | row 279 | 0.0e+00 | yes |
| R6.con_frac | Operations | row 280 | 4.2e-11 | yes |
| R6.settle | Operations | row 281 | 4.0e-11 | yes |
| R6.stor_rev | Operations | row 282 | 3.2e-11 | yes |
| R6.rev_contracted | Operations | row 283 | 4.0e-11 | yes |
| R6.rev_hedged | Operations | row 284 | 0.0e+00 | yes |
| R6.revenue | Operations | row 285 | 4.0e-11 | yes |
| R6.rev_merchant | Operations | row 286 | 3.2e-11 | yes |
| R6.opex | Operations | row 287 | 4.9e-11 | yes |
| R6.land | Operations | row 288 | 0.0e+00 | yes |
| R6.bond | Operations | row 289 | 4.8e-11 | yes |
| R6.margin_tax | Operations | row 290 | 5.0e-11 | yes |
| R6.ebitda | Operations | row 291 | 5.0e-11 | yes |
| R6.aug | Operations | row 292 | 4.8e-12 | yes |
| R6.decom | Operations | row 293 | 2.5e-11 | yes |
| R6.cf | Operations | row 294 | 5.0e-11 | yes |
| R6.te_cash | Operations | row 295 | 0.0e+00 | yes |
| R6.mesa_tax_share | Operations | row 296 | 0.0e+00 | yes |
| R6.mesa_cf | Operations | row 297 | 5.0e-11 | yes |
| R6.mesa_taxable | Operations | row 298 | 5.0e-11 | yes |
| R6.s_contracted | Operations | row 300 | 3.8e-11 | yes |
| R6.s_hedged | Operations | row 301 | 0.0e+00 | yes |
| R6.s_merchant | Operations | row 302 | 3.8e-11 | yes |
| R6.mesa_rev | Operations | row 306 | 4.0e-11 | yes |
| R7.op_frac | Operations | row 308 | 4.4e-11 | yes |
| R7.own_share | Operations | row 310 | 0.0e+00 | yes |
| R7.hub_atc | Operations | row 311 | 0.0e+00 | yes |
| R7.con_frac | Operations | row 312 | 4.4e-11 | yes |
| R7.settle | Operations | row 314 | 3.6e-11 | yes |
| R7.stor_rev | Operations | row 315 | 4.6e-11 | yes |
| R7.rev_contracted | Operations | row 316 | 3.6e-11 | yes |
| R7.rev_hedged | Operations | row 317 | 0.0e+00 | yes |
| R7.revenue | Operations | row 318 | 4.6e-11 | yes |
| R7.rev_merchant | Operations | row 319 | 4.6e-11 | yes |
| R7.opex | Operations | row 320 | 5.0e-11 | yes |
| R7.land | Operations | row 321 | 0.0e+00 | yes |
| R7.bond | Operations | row 322 | 4.8e-11 | yes |
| R7.margin_tax | Operations | row 323 | 5.0e-11 | yes |
| R7.ebitda | Operations | row 324 | 5.0e-11 | yes |
| R7.aug | Operations | row 325 | 3.8e-11 | yes |
| R7.decom | Operations | row 326 | 2.3e-11 | yes |
| R7.cf | Operations | row 327 | 5.0e-11 | yes |
| R7.te_cash | Operations | row 328 | 0.0e+00 | yes |
| R7.mesa_tax_share | Operations | row 329 | 0.0e+00 | yes |
| R7.mesa_cf | Operations | row 330 | 5.0e-11 | yes |
| R7.mesa_taxable | Operations | row 331 | 5.0e-11 | yes |
| R7.s_contracted | Operations | row 333 | 3.1e-11 | yes |
| R7.s_hedged | Operations | row 334 | 0.0e+00 | yes |
| R7.s_merchant | Operations | row 335 | 3.1e-11 | yes |
| R7.mesa_rev | Operations | row 339 | 4.6e-11 | yes |
| R8.op_frac | Operations | row 341 | 4.6e-11 | yes |
| R8.own_share | Operations | row 343 | 0.0e+00 | yes |
| R8.hub_atc | Operations | row 344 | 0.0e+00 | yes |
| R8.deg | Operations | row 346 | 4.7e-11 | yes |
| R8.curt | Operations | row 347 | 0.0e+00 | yes |
| R8.gen_full | Operations | row 348 | 4.9e-11 | yes |
| R8.gen | Operations | row 349 | 4.9e-11 | yes |
| R8.cap_hub | Operations | row 350 | 0.0e+00 | yes |
| R8.cap_node | Operations | row 351 | 0.0e+00 | yes |
| R8.node_price | Operations | row 352 | 0.0e+00 | yes |
| R8.con_frac | Operations | row 353 | 0.0e+00 | yes |
| R8.con_vol | Operations | row 354 | 0.0e+00 | yes |
| R8.settle | Operations | row 355 | 4.8e-11 | yes |
| R8.mkt_gen | Operations | row 356 | 4.9e-11 | yes |
| R8.rev_contracted | Operations | row 357 | 0.0e+00 | yes |
| R8.rev_hedged | Operations | row 358 | 0.0e+00 | yes |
| R8.mkt_rev | Operations | row 359 | 4.8e-11 | yes |
| R8.revenue | Operations | row 360 | 4.7e-11 | yes |
| R8.rev_merchant | Operations | row 361 | 4.7e-11 | yes |
| R8.opex | Operations | row 362 | 5.0e-11 | yes |
| R8.land | Operations | row 363 | 0.0e+00 | yes |
| R8.bond | Operations | row 364 | 4.8e-11 | yes |
| R8.margin_tax | Operations | row 365 | 4.9e-11 | yes |
| R8.ebitda | Operations | row 366 | 4.8e-11 | yes |
| R8.aug | Operations | row 367 | 0.0e+00 | yes |
| R8.decom | Operations | row 368 | 3.5e-11 | yes |
| R8.cf | Operations | row 369 | 4.8e-11 | yes |
| R8.te_cash | Operations | row 370 | 0.0e+00 | yes |
| R8.mesa_tax_share | Operations | row 371 | 0.0e+00 | yes |
| R8.mesa_cf | Operations | row 372 | 4.8e-11 | yes |
| R8.mesa_taxable | Operations | row 373 | 4.8e-11 | yes |
| R8.s_contracted | Operations | row 375 | 0.0e+00 | yes |
| R8.s_hedged | Operations | row 376 | 4.9e-11 | yes |
| R8.s_merchant | Operations | row 377 | 4.9e-11 | yes |
| R8.mesa_rev | Operations | row 381 | 4.7e-11 | yes |
| portfolio.am_cost | Operations | row 384 | 5.0e-11 | yes |
| portfolio.mesa_rev_contracted_a1 | Operations | row 386 | 4.5e-11 | yes |
| portfolio.mesa_rev_hedged_a1 | Operations | row 387 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_a1 | Operations | row 388 | 5.0e-11 | yes |
| portfolio.mesa_rev_a1 | Operations | row 389 | 5.0e-11 | yes |
| portfolio.mesa_rev_contracted_all | Operations | row 391 | 4.5e-11 | yes |
| portfolio.mesa_rev_hedged_all | Operations | row 392 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_all | Operations | row 393 | 4.9e-11 | yes |
| portfolio.mesa_rev_all | Operations | row 394 | 4.9e-11 | yes |
| portfolio.cfads_a1 | Operations | row 400 | 4.8e-11 | yes |
| portfolio.cfads_all | Operations | row 401 | 4.9e-11 | yes |
| portfolio.cfads_a3 | Operations | row 402 | 5.0e-11 | yes |
| portfolio.share_contracted_a1 | Operations | row 403 | 5.0e-11 | yes |
| portfolio.share_hedged_a1 | Operations | row 404 | 3.5e-11 | yes |
| portfolio.share_merchant_a1 | Operations | row 405 | 4.4e-11 | yes |
| portfolio.share_contracted_all | Operations | row 409 | 4.6e-11 | yes |
| portfolio.share_hedged_all | Operations | row 410 | 4.7e-11 | yes |
| portfolio.share_merchant_all | Operations | row 411 | 4.6e-11 | yes |
| finance.dep | Tax | row 24 | 0.0e+00 | yes |
| finance.taxable_ops | Tax | row 25 | 4.9e-11 | yes |
| finance.tl_open | Debt | row 14 | 4.8e-11 | yes |
| finance.tl_int | Debt | row 15 | 3.9e-11 | yes |
| finance.tl_prin | Debt | row 16 | 3.1e-11 | yes |
| finance.tl_prepay | Debt | row 17 | 2.6e-11 | yes |
| finance.tl_ds | Debt | row 18 | 4.9e-11 | yes |
| finance.rf_open | Debt | row 23 | 3.6e-11 | yes |
| finance.rf_int | Debt | row 24 | 4.4e-11 | yes |
| finance.rf_prin | Debt | row 25 | 4.4e-11 | yes |
| finance.rf_prepay | Debt | row 26 | 2.7e-11 | yes |
| finance.rf_ds | Debt | row 27 | 3.0e-11 | yes |
| finance.u_open | Debt | row 31 | 4.7e-11 | yes |
| finance.u_int | Debt | row 32 | 4.8e-11 | yes |
| finance.u_prin | Debt | row 33 | 4.9e-11 | yes |
| finance.u_ds | Debt | row 34 | 4.3e-11 | yes |
| finance.hc1_open | Debt | row 46 | 3.4e-11 | yes |
| finance.hc1_int | Debt | row 47 | 2.6e-11 | yes |
| finance.hc1_amort | Debt | row 48 | 1.4e-11 | yes |
| finance.hc1_sweep | Debt | row 49 | 4.2e-11 | yes |
| finance.hc1_repay | Debt | row 51 | 3.7e-11 | yes |
| finance.hc2_open | Debt | row 53 | 1.1e-11 | yes |
| finance.hc2_int | Debt | row 54 | 1.3e-11 | yes |
| finance.hc2_amort | Debt | row 55 | 3.9e-11 | yes |
| finance.hc2_sweep | Debt | row 56 | 1.4e-11 | yes |
| finance.hc2_repay | Debt | row 58 | 4.0e-11 | yes |
| finance.hc3_open | Debt | row 60 | 4.8e-11 | yes |
| finance.hc3_int | Debt | row 61 | 4.9e-11 | yes |
| finance.hc3_amort | Debt | row 62 | 3.2e-12 | yes |
| finance.hc3_sweep | Debt | row 63 | 4.8e-11 | yes |
| finance.hc_ds | Debt | row 67 | 4.9e-11 | yes |
| finance.taxable_income | Tax | row 29 | 4.9e-11 | yes |
| finance.nol_open | Tax | row 30 | 4.9e-11 | yes |
| finance.nol_used | Tax | row 31 | 4.6e-11 | yes |
| finance.tax | Tax | row 32 | 4.7e-11 | yes |
| finance.nol_close | Tax | row 33 | 4.9e-11 | yes |
| finance.opco_ds | Waterfall | row 9 | 4.9e-11 | yes |
| finance.opco_dist | Waterfall | row 10 | 4.7e-11 | yes |
| finance.recap_opco | Waterfall | row 11 | 3.6e-11 | yes |
| finance.hc_excess | Waterfall | row 16 | 4.9e-11 | yes |
| finance.fund_dist_ops | Waterfall | row 19 | 4.9e-11 | yes |
| finance.recap_hold | Waterfall | row 20 | 2.5e-11 | yes |
| finance.recap_total | Waterfall | row 21 | 3.9e-11 | yes |
| finance.fund_dist | Waterfall | row 22 | 4.9e-11 | yes |
| finance.dscr_tl | Ratios | row 8 | 3.7e-11 | yes |
| finance.dscr_rf | Ratios | row 9 | 0.0e+00 | yes |
| finance.dscr_u | Ratios | row 10 | 4.8e-11 | yes |
| finance.dscr_opco | Ratios | row 11 | 4.8e-11 | yes |
| finance.hc_cov | Ratios | row 12 | 4.8e-11 | yes |
| finance.nav_df | Returns | row 96 | 5.0e-11 | yes |
| su.A1.opco_fee | Funding | F147 | 0.0e+00 | yes |
| su.A1.holdco_oid | Funding | F148 | 1.1e-15 | yes |
| su.A1.uses | Funding | F149 | 4.0e-13 | yes |
| su.A1.equity | Funding | F150 | 4.3e-14 | yes |
| su.A2.fee | Funding | F151 | 1.1e-16 | yes |
| su.A2.uses | Funding | F152 | 4.3e-14 | yes |
| su.A2.equity | Funding | F153 | 3.6e-15 | yes |
| su.A3.r8_deposit | Funding | F154 | 3.6e-15 | yes |
| su.A3.oid | Funding | F155 | 3.3e-16 | yes |
| su.A3.itc7_proceeds | Funding | F156 | 0.0e+00 | yes |
| su.A3.itc8_proceeds | Funding | F157 | 3.6e-15 | yes |
| su.A3.eq_signing | Funding | F159 | 0.0e+00 | yes |
| su.A3.carry | Funding | F160 | 1.4e-14 | yes |
| su.A3.eq_r7 | Funding | F162 | 0.0e+00 | yes |
| su.A3.carry2 | Funding | F163 | 4.9e-15 | yes |
| su.A3.eq_r8 | Funding | F165 | 4.3e-14 | yes |
| su.A3.cash_left_after_r8 | Funding | F166 | 0.0e+00 | yes |
| su.A3.uses | Funding | F167 | 1.4e-13 | yes |
| su.A3.equity | Funding | F168 | 4.3e-14 | yes |
| refi.mtm_opco_receivable | Funding | F174 | 4.4e-15 | yes |
| refi.mtm_redfern_payable | Funding | F175 | 4.4e-16 | yes |
| refi.costs | Funding | F176 | 4.0e-15 | yes |
| refi.tl_repay | Funding | F177 | 2.8e-13 | yes |
| refi.rf_repay | Funding | F178 | 5.0e-14 | yes |
| refi.opco_net | Funding | F179 | 8.5e-14 | yes |
| sc.tl_dscr_min_2022_2025 | Ratios | F15 | 4.0e-15 | yes |
| sc.tl_dscr_avg_2022_2025 | Ratios | F16 | 0.0e+00 | yes |
| sc.uspp_dscr_min_2026_2043 | Ratios | F17 | 5.1e-15 | yes |
| sc.uspp_dscr_avg_2026_2043 | Ratios | F18 | 4.9e-15 | yes |
| sc.rf_dscr_min | Ratios | F19 | 0.0e+00 | yes |
| sc.rf_dscr_avg | Ratios | F20 | 0.0e+00 | yes |
| sc.holdco_cov_min_2023_2031 | Ratios | F21 | 4.4e-15 | yes |
| sc.holdco_cov_avg_2023_2031 | Ratios | F22 | 4.2e-15 | yes |
| sc.fund_nav_2025 | Returns | F98 | 4.3e-14 | yes |
| sc.fund_contributions | Returns | F99 | 2.0e-13 | yes |
| sc.fund_distributions_life | Returns | F100 | 4.0e-13 | yes |
| sc.fund_distributions_to_2025 | Returns | F101 | 1.7e-13 | yes |
| sc.fund_moic_life_x | Returns | F102 | 2.2e-15 | yes |
| sc.fund_moic_2025_x | Returns | F103 | 4.4e-15 | yes |
| sc.fund_irr_life_pct | Returns | F150 | 1.2e-14 | yes |
| sc.fund_irr_2025_pct | Returns | F151 | 1.9e-14 | yes |

### p99_1yr

| Key | Sheet | Location | Max diff | Pass |
|---|---|---|---|---|
| portfolio.north_atc | Operations | row 52 | 0.0e+00 | yes |
| portfolio.west_atc | Operations | row 53 | 0.0e+00 | yes |
| portfolio.south_atc | Operations | row 54 | 0.0e+00 | yes |
| portfolio.houston_atc | Operations | row 55 | 0.0e+00 | yes |
| portfolio.batt_rate | Operations | row 56 | 0.0e+00 | yes |
| portfolio.cap_hub_west_wind | Operations | row 57 | 0.0e+00 | yes |
| portfolio.cap_hub_panhandle_wind | Operations | row 58 | 0.0e+00 | yes |
| portfolio.cap_hub_west_solar | Operations | row 59 | 0.0e+00 | yes |
| portfolio.cap_hub_south_solar | Operations | row 60 | 0.0e+00 | yes |
| portfolio.cap_hub_coastal_wind | Operations | row 61 | 0.0e+00 | yes |
| R1.op_frac | Operations | row 63 | 0.0e+00 | yes |
| R1.own_share | Operations | row 65 | 1.9e-11 | yes |
| R1.hub_atc | Operations | row 66 | 0.0e+00 | yes |
| R1.deg | Operations | row 68 | 5.0e-11 | yes |
| R1.curt | Operations | row 69 | 0.0e+00 | yes |
| R1.gen_full | Operations | row 70 | 4.9e-11 | yes |
| R1.gen | Operations | row 71 | 4.9e-11 | yes |
| R1.cap_hub | Operations | row 72 | 0.0e+00 | yes |
| R1.cap_node | Operations | row 73 | 0.0e+00 | yes |
| R1.node_price | Operations | row 74 | 0.0e+00 | yes |
| R1.con_frac | Operations | row 75 | 0.0e+00 | yes |
| R1.con_vol | Operations | row 76 | 0.0e+00 | yes |
| R1.settle | Operations | row 77 | 2.0e-15 | yes |
| R1.mkt_gen | Operations | row 78 | 4.9e-11 | yes |
| R1.rev_contracted | Operations | row 79 | 0.0e+00 | yes |
| R1.rev_hedged | Operations | row 80 | 0.0e+00 | yes |
| R1.mkt_rev | Operations | row 81 | 4.8e-11 | yes |
| R1.revenue | Operations | row 82 | 4.8e-11 | yes |
| R1.rev_merchant | Operations | row 83 | 4.8e-11 | yes |
| R1.opex | Operations | row 84 | 4.9e-11 | yes |
| R1.land | Operations | row 85 | 4.2e-11 | yes |
| R1.bond | Operations | row 86 | 4.8e-11 | yes |
| R1.margin_tax | Operations | row 87 | 4.9e-11 | yes |
| R1.ebitda | Operations | row 88 | 5.0e-11 | yes |
| R1.aug | Operations | row 89 | 0.0e+00 | yes |
| R1.decom | Operations | row 90 | 3.3e-11 | yes |
| R1.cf | Operations | row 91 | 5.0e-11 | yes |
| R1.te_cash | Operations | row 92 | 0.0e+00 | yes |
| R1.mesa_tax_share | Operations | row 93 | 0.0e+00 | yes |
| R1.mesa_cf | Operations | row 94 | 5.0e-11 | yes |
| R1.mesa_taxable | Operations | row 95 | 5.0e-11 | yes |
| R1.s_contracted | Operations | row 97 | 0.0e+00 | yes |
| R1.s_hedged | Operations | row 98 | 4.8e-11 | yes |
| R1.s_merchant | Operations | row 99 | 4.8e-11 | yes |
| R1.mesa_rev | Operations | row 103 | 4.8e-11 | yes |
| R2.op_frac | Operations | row 105 | 4.1e-11 | yes |
| R2.own_share | Operations | row 107 | 1.9e-11 | yes |
| R2.hub_atc | Operations | row 108 | 0.0e+00 | yes |
| R2.deg | Operations | row 110 | 5.0e-11 | yes |
| R2.curt | Operations | row 111 | 0.0e+00 | yes |
| R2.gen_full | Operations | row 112 | 4.8e-11 | yes |
| R2.gen | Operations | row 113 | 4.8e-11 | yes |
| R2.cap_hub | Operations | row 114 | 0.0e+00 | yes |
| R2.cap_node | Operations | row 115 | 0.0e+00 | yes |
| R2.node_price | Operations | row 116 | 0.0e+00 | yes |
| R2.con_frac | Operations | row 117 | 4.1e-11 | yes |
| R2.con_vol | Operations | row 118 | 4.8e-11 | yes |
| R2.settle | Operations | row 119 | 4.6e-11 | yes |
| R2.mkt_gen | Operations | row 120 | 3.9e-11 | yes |
| R2.rev_contracted | Operations | row 121 | 4.6e-11 | yes |
| R2.rev_hedged | Operations | row 122 | 0.0e+00 | yes |
| R2.mkt_rev | Operations | row 123 | 4.0e-11 | yes |
| R2.revenue | Operations | row 124 | 4.6e-11 | yes |
| R2.rev_merchant | Operations | row 125 | 4.0e-11 | yes |
| R2.opex | Operations | row 126 | 4.7e-11 | yes |
| R2.land | Operations | row 127 | 4.8e-11 | yes |
| R2.bond | Operations | row 128 | 4.7e-11 | yes |
| R2.margin_tax | Operations | row 129 | 4.8e-11 | yes |
| R2.ebitda | Operations | row 130 | 4.9e-11 | yes |
| R2.aug | Operations | row 131 | 0.0e+00 | yes |
| R2.decom | Operations | row 132 | 4.0e-11 | yes |
| R2.cf | Operations | row 133 | 4.8e-11 | yes |
| R2.te_cash | Operations | row 134 | 0.0e+00 | yes |
| R2.mesa_tax_share | Operations | row 135 | 0.0e+00 | yes |
| R2.mesa_cf | Operations | row 136 | 4.8e-11 | yes |
| R2.mesa_taxable | Operations | row 137 | 4.8e-11 | yes |
| R2.s_contracted | Operations | row 139 | 4.2e-11 | yes |
| R2.s_hedged | Operations | row 140 | 0.0e+00 | yes |
| R2.s_merchant | Operations | row 141 | 4.2e-11 | yes |
| R2.mesa_rev | Operations | row 145 | 4.6e-11 | yes |
| R3.op_frac | Operations | row 147 | 4.9e-11 | yes |
| R3.own_share | Operations | row 149 | 1.9e-11 | yes |
| R3.hub_atc | Operations | row 150 | 0.0e+00 | yes |
| R3.deg | Operations | row 152 | 5.0e-11 | yes |
| R3.curt | Operations | row 153 | 0.0e+00 | yes |
| R3.gen_full | Operations | row 154 | 5.0e-11 | yes |
| R3.gen | Operations | row 155 | 5.0e-11 | yes |
| R3.cap_hub | Operations | row 156 | 0.0e+00 | yes |
| R3.cap_node | Operations | row 157 | 0.0e+00 | yes |
| R3.node_price | Operations | row 158 | 0.0e+00 | yes |
| R3.con_frac | Operations | row 159 | 0.0e+00 | yes |
| R3.con_vol | Operations | row 160 | 4.1e-11 | yes |
| R3.settle | Operations | row 161 | 4.2e-11 | yes |
| R3.mkt_gen | Operations | row 162 | 5.0e-11 | yes |
| R3.rev_contracted | Operations | row 163 | 0.0e+00 | yes |
| R3.rev_hedged | Operations | row 164 | 0.0e+00 | yes |
| R3.mkt_rev | Operations | row 165 | 4.9e-11 | yes |
| R3.revenue | Operations | row 166 | 4.9e-11 | yes |
| R3.rev_merchant | Operations | row 167 | 4.9e-11 | yes |
| R3.opex | Operations | row 168 | 5.0e-11 | yes |
| R3.land | Operations | row 169 | 4.9e-11 | yes |
| R3.bond | Operations | row 170 | 4.8e-11 | yes |
| R3.margin_tax | Operations | row 171 | 4.8e-11 | yes |
| R3.ebitda | Operations | row 172 | 4.8e-11 | yes |
| R3.aug | Operations | row 173 | 0.0e+00 | yes |
| R3.decom | Operations | row 174 | 8.9e-12 | yes |
| R3.cf | Operations | row 175 | 4.8e-11 | yes |
| R3.te_cash | Operations | row 177 | 0.0e+00 | yes |
| R3.mesa_tax_share | Operations | row 178 | 0.0e+00 | yes |
| R3.mesa_cf | Operations | row 179 | 4.8e-11 | yes |
| R3.mesa_taxable | Operations | row 180 | 4.8e-11 | yes |
| R3.s_contracted | Operations | row 182 | 4.5e-11 | yes |
| R3.s_hedged | Operations | row 183 | 0.0e+00 | yes |
| R3.s_merchant | Operations | row 184 | 4.5e-11 | yes |
| R3.mesa_rev | Operations | row 188 | 4.8e-11 | yes |
| R3.ptc_total | Operations | row 189 | 4.4e-11 | yes |
| R4.op_frac | Operations | row 191 | 2.9e-11 | yes |
| R4.own_share | Operations | row 193 | 1.9e-11 | yes |
| R4.hub_atc | Operations | row 194 | 0.0e+00 | yes |
| R4.deg | Operations | row 196 | 5.0e-11 | yes |
| R4.curt | Operations | row 197 | 0.0e+00 | yes |
| R4.gen_full | Operations | row 198 | 5.0e-11 | yes |
| R4.gen | Operations | row 199 | 5.0e-11 | yes |
| R4.cap_hub | Operations | row 200 | 0.0e+00 | yes |
| R4.cap_node | Operations | row 201 | 0.0e+00 | yes |
| R4.node_price | Operations | row 202 | 0.0e+00 | yes |
| R4.con_frac | Operations | row 203 | 0.0e+00 | yes |
| R4.con_vol | Operations | row 204 | 0.0e+00 | yes |
| R4.settle | Operations | row 205 | 1.0e-15 | yes |
| R4.mkt_gen | Operations | row 206 | 5.0e-11 | yes |
| R4.rev_contracted | Operations | row 207 | 0.0e+00 | yes |
| R4.rev_hedged | Operations | row 208 | 0.0e+00 | yes |
| R4.mkt_rev | Operations | row 209 | 4.9e-11 | yes |
| R4.revenue | Operations | row 210 | 4.9e-11 | yes |
| R4.rev_merchant | Operations | row 211 | 4.9e-11 | yes |
| R4.opex | Operations | row 212 | 5.0e-11 | yes |
| R4.land | Operations | row 213 | 0.0e+00 | yes |
| R4.bond | Operations | row 214 | 5.0e-11 | yes |
| R4.margin_tax | Operations | row 215 | 5.0e-11 | yes |
| R4.ebitda | Operations | row 216 | 4.9e-11 | yes |
| R4.aug | Operations | row 217 | 0.0e+00 | yes |
| R4.decom | Operations | row 218 | 1.9e-11 | yes |
| R4.cf | Operations | row 219 | 4.9e-11 | yes |
| R4.te_cash | Operations | row 220 | 0.0e+00 | yes |
| R4.mesa_tax_share | Operations | row 221 | 0.0e+00 | yes |
| R4.mesa_cf | Operations | row 222 | 4.9e-11 | yes |
| R4.mesa_taxable | Operations | row 223 | 4.9e-11 | yes |
| R4.s_contracted | Operations | row 225 | 0.0e+00 | yes |
| R4.s_hedged | Operations | row 226 | 3.5e-11 | yes |
| R4.s_merchant | Operations | row 227 | 3.5e-11 | yes |
| R4.mesa_rev | Operations | row 231 | 4.9e-11 | yes |
| R5.op_frac | Operations | row 233 | 3.7e-11 | yes |
| R5.own_share | Operations | row 235 | 1.9e-11 | yes |
| R5.hub_atc | Operations | row 236 | 0.0e+00 | yes |
| R5.deg | Operations | row 238 | 5.0e-11 | yes |
| R5.curt | Operations | row 239 | 0.0e+00 | yes |
| R5.gen_full | Operations | row 240 | 4.8e-11 | yes |
| R5.gen | Operations | row 241 | 4.8e-11 | yes |
| R5.cap_hub | Operations | row 242 | 0.0e+00 | yes |
| R5.cap_node | Operations | row 243 | 0.0e+00 | yes |
| R5.node_price | Operations | row 244 | 0.0e+00 | yes |
| R5.con_frac | Operations | row 245 | 4.1e-11 | yes |
| R5.con_vol | Operations | row 246 | 4.8e-11 | yes |
| R5.settle | Operations | row 247 | 4.8e-11 | yes |
| R5.mkt_gen | Operations | row 248 | 4.8e-11 | yes |
| R5.rev_contracted | Operations | row 249 | 5.0e-11 | yes |
| R5.rev_hedged | Operations | row 250 | 0.0e+00 | yes |
| R5.mkt_rev | Operations | row 251 | 5.0e-11 | yes |
| R5.revenue | Operations | row 252 | 4.9e-11 | yes |
| R5.rev_merchant | Operations | row 253 | 4.9e-11 | yes |
| R5.opex | Operations | row 254 | 4.9e-11 | yes |
| R5.land | Operations | row 255 | 0.0e+00 | yes |
| R5.bond | Operations | row 256 | 4.9e-11 | yes |
| R5.margin_tax | Operations | row 257 | 4.9e-11 | yes |
| R5.ebitda | Operations | row 258 | 4.9e-11 | yes |
| R5.aug | Operations | row 259 | 0.0e+00 | yes |
| R5.decom | Operations | row 260 | 2.0e-13 | yes |
| R5.cf | Operations | row 261 | 4.9e-11 | yes |
| R5.te_cash | Operations | row 263 | 4.4e-11 | yes |
| R5.mesa_tax_share | Operations | row 264 | 1.4e-12 | yes |
| R5.mesa_cf | Operations | row 265 | 4.9e-11 | yes |
| R5.mesa_taxable | Operations | row 266 | 4.9e-11 | yes |
| R5.s_contracted | Operations | row 268 | 4.5e-11 | yes |
| R5.s_hedged | Operations | row 269 | 0.0e+00 | yes |
| R5.s_merchant | Operations | row 270 | 4.5e-11 | yes |
| R5.mesa_rev | Operations | row 274 | 4.8e-11 | yes |
| R6.op_frac | Operations | row 276 | 4.2e-11 | yes |
| R6.own_share | Operations | row 278 | 2.4e-11 | yes |
| R6.hub_atc | Operations | row 279 | 0.0e+00 | yes |
| R6.con_frac | Operations | row 280 | 4.2e-11 | yes |
| R6.settle | Operations | row 281 | 4.0e-11 | yes |
| R6.stor_rev | Operations | row 282 | 3.2e-11 | yes |
| R6.rev_contracted | Operations | row 283 | 4.0e-11 | yes |
| R6.rev_hedged | Operations | row 284 | 0.0e+00 | yes |
| R6.revenue | Operations | row 285 | 4.0e-11 | yes |
| R6.rev_merchant | Operations | row 286 | 3.2e-11 | yes |
| R6.opex | Operations | row 287 | 4.9e-11 | yes |
| R6.land | Operations | row 288 | 0.0e+00 | yes |
| R6.bond | Operations | row 289 | 4.8e-11 | yes |
| R6.margin_tax | Operations | row 290 | 5.0e-11 | yes |
| R6.ebitda | Operations | row 291 | 5.0e-11 | yes |
| R6.aug | Operations | row 292 | 4.8e-12 | yes |
| R6.decom | Operations | row 293 | 2.5e-11 | yes |
| R6.cf | Operations | row 294 | 5.0e-11 | yes |
| R6.te_cash | Operations | row 295 | 0.0e+00 | yes |
| R6.mesa_tax_share | Operations | row 296 | 0.0e+00 | yes |
| R6.mesa_cf | Operations | row 297 | 5.0e-11 | yes |
| R6.mesa_taxable | Operations | row 298 | 5.0e-11 | yes |
| R6.s_contracted | Operations | row 300 | 3.8e-11 | yes |
| R6.s_hedged | Operations | row 301 | 0.0e+00 | yes |
| R6.s_merchant | Operations | row 302 | 3.8e-11 | yes |
| R6.mesa_rev | Operations | row 306 | 4.0e-11 | yes |
| R7.op_frac | Operations | row 308 | 4.4e-11 | yes |
| R7.own_share | Operations | row 310 | 0.0e+00 | yes |
| R7.hub_atc | Operations | row 311 | 0.0e+00 | yes |
| R7.con_frac | Operations | row 312 | 4.4e-11 | yes |
| R7.settle | Operations | row 314 | 3.6e-11 | yes |
| R7.stor_rev | Operations | row 315 | 4.6e-11 | yes |
| R7.rev_contracted | Operations | row 316 | 3.6e-11 | yes |
| R7.rev_hedged | Operations | row 317 | 0.0e+00 | yes |
| R7.revenue | Operations | row 318 | 4.6e-11 | yes |
| R7.rev_merchant | Operations | row 319 | 4.6e-11 | yes |
| R7.opex | Operations | row 320 | 5.0e-11 | yes |
| R7.land | Operations | row 321 | 0.0e+00 | yes |
| R7.bond | Operations | row 322 | 4.8e-11 | yes |
| R7.margin_tax | Operations | row 323 | 5.0e-11 | yes |
| R7.ebitda | Operations | row 324 | 5.0e-11 | yes |
| R7.aug | Operations | row 325 | 3.8e-11 | yes |
| R7.decom | Operations | row 326 | 2.3e-11 | yes |
| R7.cf | Operations | row 327 | 5.0e-11 | yes |
| R7.te_cash | Operations | row 328 | 0.0e+00 | yes |
| R7.mesa_tax_share | Operations | row 329 | 0.0e+00 | yes |
| R7.mesa_cf | Operations | row 330 | 5.0e-11 | yes |
| R7.mesa_taxable | Operations | row 331 | 5.0e-11 | yes |
| R7.s_contracted | Operations | row 333 | 3.1e-11 | yes |
| R7.s_hedged | Operations | row 334 | 0.0e+00 | yes |
| R7.s_merchant | Operations | row 335 | 3.1e-11 | yes |
| R7.mesa_rev | Operations | row 339 | 4.6e-11 | yes |
| R8.op_frac | Operations | row 341 | 4.6e-11 | yes |
| R8.own_share | Operations | row 343 | 0.0e+00 | yes |
| R8.hub_atc | Operations | row 344 | 0.0e+00 | yes |
| R8.deg | Operations | row 346 | 4.7e-11 | yes |
| R8.curt | Operations | row 347 | 0.0e+00 | yes |
| R8.gen_full | Operations | row 348 | 4.8e-11 | yes |
| R8.gen | Operations | row 349 | 4.8e-11 | yes |
| R8.cap_hub | Operations | row 350 | 0.0e+00 | yes |
| R8.cap_node | Operations | row 351 | 0.0e+00 | yes |
| R8.node_price | Operations | row 352 | 0.0e+00 | yes |
| R8.con_frac | Operations | row 353 | 0.0e+00 | yes |
| R8.con_vol | Operations | row 354 | 0.0e+00 | yes |
| R8.settle | Operations | row 355 | 4.8e-11 | yes |
| R8.mkt_gen | Operations | row 356 | 4.8e-11 | yes |
| R8.rev_contracted | Operations | row 357 | 0.0e+00 | yes |
| R8.rev_hedged | Operations | row 358 | 0.0e+00 | yes |
| R8.mkt_rev | Operations | row 359 | 4.9e-11 | yes |
| R8.revenue | Operations | row 360 | 4.9e-11 | yes |
| R8.rev_merchant | Operations | row 361 | 4.9e-11 | yes |
| R8.opex | Operations | row 362 | 5.0e-11 | yes |
| R8.land | Operations | row 363 | 0.0e+00 | yes |
| R8.bond | Operations | row 364 | 4.8e-11 | yes |
| R8.margin_tax | Operations | row 365 | 4.9e-11 | yes |
| R8.ebitda | Operations | row 366 | 4.8e-11 | yes |
| R8.aug | Operations | row 367 | 0.0e+00 | yes |
| R8.decom | Operations | row 368 | 3.5e-11 | yes |
| R8.cf | Operations | row 369 | 4.8e-11 | yes |
| R8.te_cash | Operations | row 370 | 0.0e+00 | yes |
| R8.mesa_tax_share | Operations | row 371 | 0.0e+00 | yes |
| R8.mesa_cf | Operations | row 372 | 4.8e-11 | yes |
| R8.mesa_taxable | Operations | row 373 | 4.8e-11 | yes |
| R8.s_contracted | Operations | row 375 | 0.0e+00 | yes |
| R8.s_hedged | Operations | row 376 | 4.4e-11 | yes |
| R8.s_merchant | Operations | row 377 | 4.4e-11 | yes |
| R8.mesa_rev | Operations | row 381 | 4.9e-11 | yes |
| portfolio.am_cost | Operations | row 384 | 5.0e-11 | yes |
| portfolio.mesa_rev_contracted_a1 | Operations | row 386 | 4.4e-11 | yes |
| portfolio.mesa_rev_hedged_a1 | Operations | row 387 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_a1 | Operations | row 388 | 4.8e-11 | yes |
| portfolio.mesa_rev_a1 | Operations | row 389 | 4.8e-11 | yes |
| portfolio.mesa_rev_contracted_all | Operations | row 391 | 3.8e-11 | yes |
| portfolio.mesa_rev_hedged_all | Operations | row 392 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_all | Operations | row 393 | 5.0e-11 | yes |
| portfolio.mesa_rev_all | Operations | row 394 | 4.8e-11 | yes |
| portfolio.cfads_a1 | Operations | row 400 | 4.9e-11 | yes |
| portfolio.cfads_all | Operations | row 401 | 4.9e-11 | yes |
| portfolio.cfads_a3 | Operations | row 402 | 4.9e-11 | yes |
| portfolio.share_contracted_a1 | Operations | row 403 | 4.9e-11 | yes |
| portfolio.share_hedged_a1 | Operations | row 404 | 3.8e-11 | yes |
| portfolio.share_merchant_a1 | Operations | row 405 | 4.9e-11 | yes |
| portfolio.share_contracted_all | Operations | row 409 | 4.5e-11 | yes |
| portfolio.share_hedged_all | Operations | row 410 | 4.5e-11 | yes |
| portfolio.share_merchant_all | Operations | row 411 | 4.9e-11 | yes |
| finance.dep | Tax | row 24 | 0.0e+00 | yes |
| finance.taxable_ops | Tax | row 25 | 4.9e-11 | yes |
| finance.tl_open | Debt | row 14 | 4.8e-11 | yes |
| finance.tl_int | Debt | row 15 | 3.9e-11 | yes |
| finance.tl_prin | Debt | row 16 | 3.1e-11 | yes |
| finance.tl_prepay | Debt | row 17 | 2.6e-11 | yes |
| finance.tl_ds | Debt | row 18 | 4.9e-11 | yes |
| finance.rf_open | Debt | row 23 | 3.6e-11 | yes |
| finance.rf_int | Debt | row 24 | 4.4e-11 | yes |
| finance.rf_prin | Debt | row 25 | 4.4e-11 | yes |
| finance.rf_prepay | Debt | row 26 | 2.7e-11 | yes |
| finance.rf_ds | Debt | row 27 | 3.0e-11 | yes |
| finance.u_open | Debt | row 31 | 4.7e-11 | yes |
| finance.u_int | Debt | row 32 | 4.8e-11 | yes |
| finance.u_prin | Debt | row 33 | 4.9e-11 | yes |
| finance.u_ds | Debt | row 34 | 4.3e-11 | yes |
| finance.hc1_open | Debt | row 46 | 4.7e-11 | yes |
| finance.hc1_int | Debt | row 47 | 3.5e-11 | yes |
| finance.hc1_amort | Debt | row 48 | 1.4e-11 | yes |
| finance.hc1_sweep | Debt | row 49 | 4.0e-11 | yes |
| finance.hc1_repay | Debt | row 51 | 1.1e-11 | yes |
| finance.hc2_open | Debt | row 53 | 1.2e-11 | yes |
| finance.hc2_int | Debt | row 54 | 8.5e-12 | yes |
| finance.hc2_amort | Debt | row 55 | 3.9e-11 | yes |
| finance.hc2_sweep | Debt | row 56 | 1.8e-12 | yes |
| finance.hc2_repay | Debt | row 58 | 4.7e-11 | yes |
| finance.hc3_open | Debt | row 60 | 4.8e-11 | yes |
| finance.hc3_int | Debt | row 61 | 4.7e-11 | yes |
| finance.hc3_amort | Debt | row 62 | 3.2e-12 | yes |
| finance.hc3_sweep | Debt | row 63 | 5.0e-11 | yes |
| finance.hc_ds | Debt | row 67 | 4.9e-11 | yes |
| finance.taxable_income | Tax | row 29 | 4.9e-11 | yes |
| finance.nol_open | Tax | row 30 | 4.9e-11 | yes |
| finance.nol_used | Tax | row 31 | 4.5e-11 | yes |
| finance.tax | Tax | row 32 | 4.7e-11 | yes |
| finance.nol_close | Tax | row 33 | 4.9e-11 | yes |
| finance.opco_ds | Waterfall | row 9 | 4.9e-11 | yes |
| finance.opco_dist | Waterfall | row 10 | 4.9e-11 | yes |
| finance.recap_opco | Waterfall | row 11 | 3.6e-11 | yes |
| finance.hc_excess | Waterfall | row 16 | 4.8e-11 | yes |
| finance.fund_dist_ops | Waterfall | row 19 | 5.0e-11 | yes |
| finance.recap_hold | Waterfall | row 20 | 2.0e-11 | yes |
| finance.recap_total | Waterfall | row 21 | 1.6e-11 | yes |
| finance.fund_dist | Waterfall | row 22 | 5.0e-11 | yes |
| finance.dscr_tl | Ratios | row 8 | 5.0e-11 | yes |
| finance.dscr_rf | Ratios | row 9 | 0.0e+00 | yes |
| finance.dscr_u | Ratios | row 10 | 4.5e-11 | yes |
| finance.dscr_opco | Ratios | row 11 | 5.0e-11 | yes |
| finance.hc_cov | Ratios | row 12 | 5.0e-11 | yes |
| finance.nav_df | Returns | row 96 | 5.0e-11 | yes |
| su.A1.opco_fee | Funding | F147 | 0.0e+00 | yes |
| su.A1.holdco_oid | Funding | F148 | 1.1e-15 | yes |
| su.A1.uses | Funding | F149 | 4.0e-13 | yes |
| su.A1.equity | Funding | F150 | 4.3e-14 | yes |
| su.A2.fee | Funding | F151 | 1.1e-16 | yes |
| su.A2.uses | Funding | F152 | 4.3e-14 | yes |
| su.A2.equity | Funding | F153 | 3.6e-15 | yes |
| su.A3.r8_deposit | Funding | F154 | 3.6e-15 | yes |
| su.A3.oid | Funding | F155 | 3.3e-16 | yes |
| su.A3.itc7_proceeds | Funding | F156 | 0.0e+00 | yes |
| su.A3.itc8_proceeds | Funding | F157 | 3.6e-15 | yes |
| su.A3.eq_signing | Funding | F159 | 0.0e+00 | yes |
| su.A3.carry | Funding | F160 | 1.4e-14 | yes |
| su.A3.eq_r7 | Funding | F162 | 0.0e+00 | yes |
| su.A3.carry2 | Funding | F163 | 4.9e-15 | yes |
| su.A3.eq_r8 | Funding | F165 | 4.3e-14 | yes |
| su.A3.cash_left_after_r8 | Funding | F166 | 0.0e+00 | yes |
| su.A3.uses | Funding | F167 | 1.4e-13 | yes |
| su.A3.equity | Funding | F168 | 4.3e-14 | yes |
| refi.mtm_opco_receivable | Funding | F174 | 4.4e-15 | yes |
| refi.mtm_redfern_payable | Funding | F175 | 4.4e-16 | yes |
| refi.costs | Funding | F176 | 4.0e-15 | yes |
| refi.tl_repay | Funding | F177 | 2.8e-13 | yes |
| refi.rf_repay | Funding | F178 | 5.0e-14 | yes |
| refi.opco_net | Funding | F179 | 8.5e-14 | yes |
| sc.tl_dscr_min_2022_2025 | Ratios | F15 | 4.9e-15 | yes |
| sc.tl_dscr_avg_2022_2025 | Ratios | F16 | 2.4e-15 | yes |
| sc.uspp_dscr_min_2026_2043 | Ratios | F17 | 8.9e-16 | yes |
| sc.uspp_dscr_avg_2026_2043 | Ratios | F18 | 2.2e-15 | yes |
| sc.rf_dscr_min | Ratios | F19 | 0.0e+00 | yes |
| sc.rf_dscr_avg | Ratios | F20 | 0.0e+00 | yes |
| sc.holdco_cov_min_2023_2031 | Ratios | F21 | 1.1e-15 | yes |
| sc.holdco_cov_avg_2023_2031 | Ratios | F22 | 1.1e-16 | yes |
| sc.fund_nav_2025 | Returns | F98 | 7.1e-15 | yes |
| sc.fund_contributions | Returns | F99 | 2.0e-13 | yes |
| sc.fund_distributions_life | Returns | F100 | 3.4e-13 | yes |
| sc.fund_distributions_to_2025 | Returns | F101 | 1.4e-13 | yes |
| sc.fund_moic_life_x | Returns | F102 | 6.7e-16 | yes |
| sc.fund_moic_2025_x | Returns | F103 | 6.7e-16 | yes |
| sc.fund_irr_life_pct | Returns | F150 | 5.0e-15 | yes |
| sc.fund_irr_2025_pct | Returns | F151 | 3.6e-15 | yes |

### status_quo

| Key | Sheet | Location | Max diff | Pass |
|---|---|---|---|---|
| portfolio.north_atc | Operations | row 52 | 0.0e+00 | yes |
| portfolio.west_atc | Operations | row 53 | 0.0e+00 | yes |
| portfolio.south_atc | Operations | row 54 | 0.0e+00 | yes |
| portfolio.houston_atc | Operations | row 55 | 0.0e+00 | yes |
| portfolio.batt_rate | Operations | row 56 | 0.0e+00 | yes |
| portfolio.cap_hub_west_wind | Operations | row 57 | 0.0e+00 | yes |
| portfolio.cap_hub_panhandle_wind | Operations | row 58 | 0.0e+00 | yes |
| portfolio.cap_hub_west_solar | Operations | row 59 | 0.0e+00 | yes |
| portfolio.cap_hub_south_solar | Operations | row 60 | 0.0e+00 | yes |
| portfolio.cap_hub_coastal_wind | Operations | row 61 | 0.0e+00 | yes |
| R1.op_frac | Operations | row 63 | 0.0e+00 | yes |
| R1.own_share | Operations | row 65 | 1.9e-11 | yes |
| R1.hub_atc | Operations | row 66 | 0.0e+00 | yes |
| R1.deg | Operations | row 68 | 5.0e-11 | yes |
| R1.curt | Operations | row 69 | 0.0e+00 | yes |
| R1.gen_full | Operations | row 70 | 5.0e-11 | yes |
| R1.gen | Operations | row 71 | 4.8e-11 | yes |
| R1.cap_hub | Operations | row 72 | 0.0e+00 | yes |
| R1.cap_node | Operations | row 73 | 0.0e+00 | yes |
| R1.node_price | Operations | row 74 | 0.0e+00 | yes |
| R1.con_frac | Operations | row 75 | 0.0e+00 | yes |
| R1.con_vol | Operations | row 76 | 0.0e+00 | yes |
| R1.settle | Operations | row 77 | 2.0e-15 | yes |
| R1.mkt_gen | Operations | row 78 | 4.8e-11 | yes |
| R1.rev_contracted | Operations | row 79 | 0.0e+00 | yes |
| R1.rev_hedged | Operations | row 80 | 0.0e+00 | yes |
| R1.mkt_rev | Operations | row 81 | 4.9e-11 | yes |
| R1.revenue | Operations | row 82 | 4.9e-11 | yes |
| R1.rev_merchant | Operations | row 83 | 4.9e-11 | yes |
| R1.opex | Operations | row 84 | 4.9e-11 | yes |
| R1.land | Operations | row 85 | 5.0e-11 | yes |
| R1.bond | Operations | row 86 | 4.8e-11 | yes |
| R1.margin_tax | Operations | row 87 | 4.9e-11 | yes |
| R1.ebitda | Operations | row 88 | 5.0e-11 | yes |
| R1.aug | Operations | row 89 | 0.0e+00 | yes |
| R1.decom | Operations | row 90 | 3.3e-11 | yes |
| R1.cf | Operations | row 91 | 5.0e-11 | yes |
| R1.te_cash | Operations | row 92 | 0.0e+00 | yes |
| R1.mesa_tax_share | Operations | row 93 | 0.0e+00 | yes |
| R1.mesa_cf | Operations | row 94 | 5.0e-11 | yes |
| R1.mesa_taxable | Operations | row 95 | 5.0e-11 | yes |
| R1.s_contracted | Operations | row 97 | 0.0e+00 | yes |
| R1.s_hedged | Operations | row 98 | 2.8e-11 | yes |
| R1.s_merchant | Operations | row 99 | 2.8e-11 | yes |
| R1.mesa_rev | Operations | row 103 | 4.9e-11 | yes |
| R2.op_frac | Operations | row 105 | 4.1e-11 | yes |
| R2.own_share | Operations | row 107 | 1.9e-11 | yes |
| R2.hub_atc | Operations | row 108 | 0.0e+00 | yes |
| R2.deg | Operations | row 110 | 5.0e-11 | yes |
| R2.curt | Operations | row 111 | 0.0e+00 | yes |
| R2.gen_full | Operations | row 112 | 5.0e-11 | yes |
| R2.gen | Operations | row 113 | 5.0e-11 | yes |
| R2.cap_hub | Operations | row 114 | 0.0e+00 | yes |
| R2.cap_node | Operations | row 115 | 0.0e+00 | yes |
| R2.node_price | Operations | row 116 | 0.0e+00 | yes |
| R2.con_frac | Operations | row 117 | 4.1e-11 | yes |
| R2.con_vol | Operations | row 118 | 4.4e-11 | yes |
| R2.settle | Operations | row 119 | 4.5e-11 | yes |
| R2.mkt_gen | Operations | row 120 | 5.0e-11 | yes |
| R2.rev_contracted | Operations | row 121 | 4.5e-11 | yes |
| R2.rev_hedged | Operations | row 122 | 0.0e+00 | yes |
| R2.mkt_rev | Operations | row 123 | 4.8e-11 | yes |
| R2.revenue | Operations | row 124 | 5.0e-11 | yes |
| R2.rev_merchant | Operations | row 125 | 4.8e-11 | yes |
| R2.opex | Operations | row 126 | 4.7e-11 | yes |
| R2.land | Operations | row 127 | 5.0e-11 | yes |
| R2.bond | Operations | row 128 | 4.7e-11 | yes |
| R2.margin_tax | Operations | row 129 | 5.0e-11 | yes |
| R2.ebitda | Operations | row 130 | 4.7e-11 | yes |
| R2.aug | Operations | row 131 | 0.0e+00 | yes |
| R2.decom | Operations | row 132 | 4.0e-11 | yes |
| R2.cf | Operations | row 133 | 4.7e-11 | yes |
| R2.te_cash | Operations | row 134 | 0.0e+00 | yes |
| R2.mesa_tax_share | Operations | row 135 | 0.0e+00 | yes |
| R2.mesa_cf | Operations | row 136 | 4.7e-11 | yes |
| R2.mesa_taxable | Operations | row 137 | 4.7e-11 | yes |
| R2.s_contracted | Operations | row 139 | 4.2e-11 | yes |
| R2.s_hedged | Operations | row 140 | 0.0e+00 | yes |
| R2.s_merchant | Operations | row 141 | 4.2e-11 | yes |
| R2.mesa_rev | Operations | row 145 | 5.0e-11 | yes |
| R3.op_frac | Operations | row 147 | 4.9e-11 | yes |
| R3.own_share | Operations | row 149 | 1.9e-11 | yes |
| R3.hub_atc | Operations | row 150 | 0.0e+00 | yes |
| R3.deg | Operations | row 152 | 5.0e-11 | yes |
| R3.curt | Operations | row 153 | 0.0e+00 | yes |
| R3.gen_full | Operations | row 154 | 5.0e-11 | yes |
| R3.gen | Operations | row 155 | 5.0e-11 | yes |
| R3.cap_hub | Operations | row 156 | 0.0e+00 | yes |
| R3.cap_node | Operations | row 157 | 0.0e+00 | yes |
| R3.node_price | Operations | row 158 | 0.0e+00 | yes |
| R3.con_frac | Operations | row 159 | 0.0e+00 | yes |
| R3.con_vol | Operations | row 160 | 4.8e-11 | yes |
| R3.settle | Operations | row 161 | 5.0e-11 | yes |
| R3.mkt_gen | Operations | row 162 | 5.0e-11 | yes |
| R3.rev_contracted | Operations | row 163 | 0.0e+00 | yes |
| R3.rev_hedged | Operations | row 164 | 0.0e+00 | yes |
| R3.mkt_rev | Operations | row 165 | 5.0e-11 | yes |
| R3.revenue | Operations | row 166 | 5.0e-11 | yes |
| R3.rev_merchant | Operations | row 167 | 5.0e-11 | yes |
| R3.opex | Operations | row 168 | 5.0e-11 | yes |
| R3.land | Operations | row 169 | 5.0e-11 | yes |
| R3.bond | Operations | row 170 | 4.8e-11 | yes |
| R3.margin_tax | Operations | row 171 | 4.5e-11 | yes |
| R3.ebitda | Operations | row 172 | 5.0e-11 | yes |
| R3.aug | Operations | row 173 | 0.0e+00 | yes |
| R3.decom | Operations | row 174 | 8.9e-12 | yes |
| R3.cf | Operations | row 175 | 4.4e-11 | yes |
| R3.te_cash | Operations | row 177 | 0.0e+00 | yes |
| R3.mesa_tax_share | Operations | row 178 | 0.0e+00 | yes |
| R3.mesa_cf | Operations | row 179 | 4.3e-11 | yes |
| R3.mesa_taxable | Operations | row 180 | 5.0e-11 | yes |
| R3.s_contracted | Operations | row 182 | 4.5e-11 | yes |
| R3.s_hedged | Operations | row 183 | 0.0e+00 | yes |
| R3.s_merchant | Operations | row 184 | 4.5e-11 | yes |
| R3.mesa_rev | Operations | row 188 | 5.0e-11 | yes |
| R3.ptc_total | Operations | row 189 | 4.5e-11 | yes |
| R4.op_frac | Operations | row 191 | 2.9e-11 | yes |
| R4.own_share | Operations | row 193 | 1.9e-11 | yes |
| R4.hub_atc | Operations | row 194 | 0.0e+00 | yes |
| R4.deg | Operations | row 196 | 5.0e-11 | yes |
| R4.curt | Operations | row 197 | 0.0e+00 | yes |
| R4.gen_full | Operations | row 198 | 5.0e-11 | yes |
| R4.gen | Operations | row 199 | 5.0e-11 | yes |
| R4.cap_hub | Operations | row 200 | 0.0e+00 | yes |
| R4.cap_node | Operations | row 201 | 0.0e+00 | yes |
| R4.node_price | Operations | row 202 | 0.0e+00 | yes |
| R4.con_frac | Operations | row 203 | 0.0e+00 | yes |
| R4.con_vol | Operations | row 204 | 0.0e+00 | yes |
| R4.settle | Operations | row 205 | 1.0e-15 | yes |
| R4.mkt_gen | Operations | row 206 | 5.0e-11 | yes |
| R4.rev_contracted | Operations | row 207 | 0.0e+00 | yes |
| R4.rev_hedged | Operations | row 208 | 0.0e+00 | yes |
| R4.mkt_rev | Operations | row 209 | 4.9e-11 | yes |
| R4.revenue | Operations | row 210 | 4.9e-11 | yes |
| R4.rev_merchant | Operations | row 211 | 4.9e-11 | yes |
| R4.opex | Operations | row 212 | 5.0e-11 | yes |
| R4.land | Operations | row 213 | 0.0e+00 | yes |
| R4.bond | Operations | row 214 | 5.0e-11 | yes |
| R4.margin_tax | Operations | row 215 | 5.0e-11 | yes |
| R4.ebitda | Operations | row 216 | 4.9e-11 | yes |
| R4.aug | Operations | row 217 | 0.0e+00 | yes |
| R4.decom | Operations | row 218 | 1.9e-11 | yes |
| R4.cf | Operations | row 219 | 4.9e-11 | yes |
| R4.te_cash | Operations | row 220 | 0.0e+00 | yes |
| R4.mesa_tax_share | Operations | row 221 | 0.0e+00 | yes |
| R4.mesa_cf | Operations | row 222 | 4.9e-11 | yes |
| R4.mesa_taxable | Operations | row 223 | 4.9e-11 | yes |
| R4.s_contracted | Operations | row 225 | 0.0e+00 | yes |
| R4.s_hedged | Operations | row 226 | 4.6e-11 | yes |
| R4.s_merchant | Operations | row 227 | 4.6e-11 | yes |
| R4.mesa_rev | Operations | row 231 | 4.9e-11 | yes |
| R5.op_frac | Operations | row 233 | 3.7e-11 | yes |
| R5.own_share | Operations | row 235 | 1.9e-11 | yes |
| R5.hub_atc | Operations | row 236 | 0.0e+00 | yes |
| R5.deg | Operations | row 238 | 5.0e-11 | yes |
| R5.curt | Operations | row 239 | 0.0e+00 | yes |
| R5.gen_full | Operations | row 240 | 4.1e-11 | yes |
| R5.gen | Operations | row 241 | 4.9e-11 | yes |
| R5.cap_hub | Operations | row 242 | 0.0e+00 | yes |
| R5.cap_node | Operations | row 243 | 0.0e+00 | yes |
| R5.node_price | Operations | row 244 | 0.0e+00 | yes |
| R5.con_frac | Operations | row 245 | 4.1e-11 | yes |
| R5.con_vol | Operations | row 246 | 4.0e-11 | yes |
| R5.settle | Operations | row 247 | 4.8e-11 | yes |
| R5.mkt_gen | Operations | row 248 | 4.9e-11 | yes |
| R5.rev_contracted | Operations | row 249 | 4.0e-11 | yes |
| R5.rev_hedged | Operations | row 250 | 0.0e+00 | yes |
| R5.mkt_rev | Operations | row 251 | 4.9e-11 | yes |
| R5.revenue | Operations | row 252 | 4.9e-11 | yes |
| R5.rev_merchant | Operations | row 253 | 4.9e-11 | yes |
| R5.opex | Operations | row 254 | 4.9e-11 | yes |
| R5.land | Operations | row 255 | 0.0e+00 | yes |
| R5.bond | Operations | row 256 | 4.9e-11 | yes |
| R5.margin_tax | Operations | row 257 | 4.5e-11 | yes |
| R5.ebitda | Operations | row 258 | 5.0e-11 | yes |
| R5.aug | Operations | row 259 | 0.0e+00 | yes |
| R5.decom | Operations | row 260 | 2.0e-13 | yes |
| R5.cf | Operations | row 261 | 5.0e-11 | yes |
| R5.te_cash | Operations | row 263 | 4.4e-11 | yes |
| R5.mesa_tax_share | Operations | row 264 | 1.4e-12 | yes |
| R5.mesa_cf | Operations | row 265 | 4.8e-11 | yes |
| R5.mesa_taxable | Operations | row 266 | 4.8e-11 | yes |
| R5.s_contracted | Operations | row 268 | 4.5e-11 | yes |
| R5.s_hedged | Operations | row 269 | 0.0e+00 | yes |
| R5.s_merchant | Operations | row 270 | 4.5e-11 | yes |
| R5.mesa_rev | Operations | row 274 | 4.7e-11 | yes |
| R6.op_frac | Operations | row 276 | 4.2e-11 | yes |
| R6.own_share | Operations | row 278 | 2.4e-11 | yes |
| R6.hub_atc | Operations | row 279 | 0.0e+00 | yes |
| R6.con_frac | Operations | row 280 | 4.2e-11 | yes |
| R6.settle | Operations | row 281 | 4.0e-11 | yes |
| R6.stor_rev | Operations | row 282 | 3.2e-11 | yes |
| R6.rev_contracted | Operations | row 283 | 4.0e-11 | yes |
| R6.rev_hedged | Operations | row 284 | 0.0e+00 | yes |
| R6.revenue | Operations | row 285 | 4.0e-11 | yes |
| R6.rev_merchant | Operations | row 286 | 3.2e-11 | yes |
| R6.opex | Operations | row 287 | 4.9e-11 | yes |
| R6.land | Operations | row 288 | 0.0e+00 | yes |
| R6.bond | Operations | row 289 | 4.8e-11 | yes |
| R6.margin_tax | Operations | row 290 | 5.0e-11 | yes |
| R6.ebitda | Operations | row 291 | 5.0e-11 | yes |
| R6.aug | Operations | row 292 | 4.8e-12 | yes |
| R6.decom | Operations | row 293 | 2.5e-11 | yes |
| R6.cf | Operations | row 294 | 5.0e-11 | yes |
| R6.te_cash | Operations | row 295 | 0.0e+00 | yes |
| R6.mesa_tax_share | Operations | row 296 | 0.0e+00 | yes |
| R6.mesa_cf | Operations | row 297 | 5.0e-11 | yes |
| R6.mesa_taxable | Operations | row 298 | 5.0e-11 | yes |
| R6.s_contracted | Operations | row 300 | 3.8e-11 | yes |
| R6.s_hedged | Operations | row 301 | 0.0e+00 | yes |
| R6.s_merchant | Operations | row 302 | 3.8e-11 | yes |
| R6.mesa_rev | Operations | row 306 | 4.0e-11 | yes |
| R7.op_frac | Operations | row 308 | 4.4e-11 | yes |
| R7.own_share | Operations | row 310 | 0.0e+00 | yes |
| R7.hub_atc | Operations | row 311 | 0.0e+00 | yes |
| R7.con_frac | Operations | row 312 | 4.4e-11 | yes |
| R7.settle | Operations | row 314 | 3.6e-11 | yes |
| R7.stor_rev | Operations | row 315 | 4.6e-11 | yes |
| R7.rev_contracted | Operations | row 316 | 3.6e-11 | yes |
| R7.rev_hedged | Operations | row 317 | 0.0e+00 | yes |
| R7.revenue | Operations | row 318 | 4.6e-11 | yes |
| R7.rev_merchant | Operations | row 319 | 4.6e-11 | yes |
| R7.opex | Operations | row 320 | 5.0e-11 | yes |
| R7.land | Operations | row 321 | 0.0e+00 | yes |
| R7.bond | Operations | row 322 | 4.8e-11 | yes |
| R7.margin_tax | Operations | row 323 | 5.0e-11 | yes |
| R7.ebitda | Operations | row 324 | 5.0e-11 | yes |
| R7.aug | Operations | row 325 | 3.8e-11 | yes |
| R7.decom | Operations | row 326 | 2.3e-11 | yes |
| R7.cf | Operations | row 327 | 5.0e-11 | yes |
| R7.te_cash | Operations | row 328 | 0.0e+00 | yes |
| R7.mesa_tax_share | Operations | row 329 | 0.0e+00 | yes |
| R7.mesa_cf | Operations | row 330 | 5.0e-11 | yes |
| R7.mesa_taxable | Operations | row 331 | 5.0e-11 | yes |
| R7.s_contracted | Operations | row 333 | 3.1e-11 | yes |
| R7.s_hedged | Operations | row 334 | 0.0e+00 | yes |
| R7.s_merchant | Operations | row 335 | 3.1e-11 | yes |
| R7.mesa_rev | Operations | row 339 | 4.6e-11 | yes |
| R8.op_frac | Operations | row 341 | 4.6e-11 | yes |
| R8.own_share | Operations | row 343 | 0.0e+00 | yes |
| R8.hub_atc | Operations | row 344 | 0.0e+00 | yes |
| R8.deg | Operations | row 346 | 4.7e-11 | yes |
| R8.curt | Operations | row 347 | 0.0e+00 | yes |
| R8.gen_full | Operations | row 348 | 4.9e-11 | yes |
| R8.gen | Operations | row 349 | 4.9e-11 | yes |
| R8.cap_hub | Operations | row 350 | 0.0e+00 | yes |
| R8.cap_node | Operations | row 351 | 0.0e+00 | yes |
| R8.node_price | Operations | row 352 | 0.0e+00 | yes |
| R8.con_frac | Operations | row 353 | 0.0e+00 | yes |
| R8.con_vol | Operations | row 354 | 0.0e+00 | yes |
| R8.settle | Operations | row 355 | 4.8e-11 | yes |
| R8.mkt_gen | Operations | row 356 | 4.9e-11 | yes |
| R8.rev_contracted | Operations | row 357 | 0.0e+00 | yes |
| R8.rev_hedged | Operations | row 358 | 0.0e+00 | yes |
| R8.mkt_rev | Operations | row 359 | 4.9e-11 | yes |
| R8.revenue | Operations | row 360 | 4.9e-11 | yes |
| R8.rev_merchant | Operations | row 361 | 4.9e-11 | yes |
| R8.opex | Operations | row 362 | 5.0e-11 | yes |
| R8.land | Operations | row 363 | 0.0e+00 | yes |
| R8.bond | Operations | row 364 | 4.8e-11 | yes |
| R8.margin_tax | Operations | row 365 | 4.8e-11 | yes |
| R8.ebitda | Operations | row 366 | 4.8e-11 | yes |
| R8.aug | Operations | row 367 | 0.0e+00 | yes |
| R8.decom | Operations | row 368 | 3.5e-11 | yes |
| R8.cf | Operations | row 369 | 4.8e-11 | yes |
| R8.te_cash | Operations | row 370 | 0.0e+00 | yes |
| R8.mesa_tax_share | Operations | row 371 | 0.0e+00 | yes |
| R8.mesa_cf | Operations | row 372 | 4.8e-11 | yes |
| R8.mesa_taxable | Operations | row 373 | 4.8e-11 | yes |
| R8.s_contracted | Operations | row 375 | 0.0e+00 | yes |
| R8.s_hedged | Operations | row 376 | 3.6e-11 | yes |
| R8.s_merchant | Operations | row 377 | 3.6e-11 | yes |
| R8.mesa_rev | Operations | row 381 | 4.9e-11 | yes |
| portfolio.am_cost | Operations | row 384 | 5.0e-11 | yes |
| portfolio.mesa_rev_contracted_a1 | Operations | row 386 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_a1 | Operations | row 387 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_a1 | Operations | row 388 | 4.9e-11 | yes |
| portfolio.mesa_rev_a1 | Operations | row 389 | 4.9e-11 | yes |
| portfolio.mesa_rev_contracted_all | Operations | row 391 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_all | Operations | row 392 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_all | Operations | row 393 | 5.0e-11 | yes |
| portfolio.mesa_rev_all | Operations | row 394 | 5.0e-11 | yes |
| portfolio.cfads_a1 | Operations | row 400 | 4.9e-11 | yes |
| portfolio.cfads_all | Operations | row 401 | 4.8e-11 | yes |
| portfolio.cfads_a3 | Operations | row 402 | 4.9e-11 | yes |
| portfolio.share_contracted_a1 | Operations | row 403 | 4.7e-11 | yes |
| portfolio.share_hedged_a1 | Operations | row 404 | 4.5e-11 | yes |
| portfolio.share_merchant_a1 | Operations | row 405 | 4.8e-11 | yes |
| portfolio.share_contracted_all | Operations | row 409 | 4.7e-11 | yes |
| portfolio.share_hedged_all | Operations | row 410 | 4.7e-11 | yes |
| portfolio.share_merchant_all | Operations | row 411 | 3.9e-11 | yes |
| finance.dep | Tax | row 24 | 0.0e+00 | yes |
| finance.taxable_ops | Tax | row 25 | 4.9e-11 | yes |
| finance.tl_open | Debt | row 14 | 4.9e-11 | yes |
| finance.tl_int | Debt | row 15 | 4.9e-11 | yes |
| finance.tl_prin | Debt | row 16 | 5.0e-11 | yes |
| finance.tl_prepay | Debt | row 17 | 0.0e+00 | yes |
| finance.tl_ds | Debt | row 18 | 4.9e-11 | yes |
| finance.rf_open | Debt | row 23 | 4.5e-11 | yes |
| finance.rf_int | Debt | row 24 | 4.8e-11 | yes |
| finance.rf_prin | Debt | row 25 | 4.8e-11 | yes |
| finance.rf_prepay | Debt | row 26 | 0.0e+00 | yes |
| finance.rf_ds | Debt | row 27 | 4.8e-11 | yes |
| finance.u_open | Debt | row 31 | 0.0e+00 | yes |
| finance.u_int | Debt | row 32 | 0.0e+00 | yes |
| finance.u_prin | Debt | row 33 | 0.0e+00 | yes |
| finance.u_ds | Debt | row 34 | 0.0e+00 | yes |
| finance.hc1_open | Debt | row 46 | 5.0e-11 | yes |
| finance.hc1_int | Debt | row 47 | 4.9e-11 | yes |
| finance.hc1_amort | Debt | row 48 | 1.4e-11 | yes |
| finance.hc1_sweep | Debt | row 49 | 3.6e-11 | yes |
| finance.hc1_repay | Debt | row 51 | 0.0e+00 | yes |
| finance.hc2_open | Debt | row 53 | 5.0e-11 | yes |
| finance.hc2_int | Debt | row 54 | 4.4e-11 | yes |
| finance.hc2_amort | Debt | row 55 | 3.9e-11 | yes |
| finance.hc2_sweep | Debt | row 56 | 4.8e-11 | yes |
| finance.hc2_repay | Debt | row 58 | 0.0e+00 | yes |
| finance.hc3_open | Debt | row 60 | 0.0e+00 | yes |
| finance.hc3_int | Debt | row 61 | 0.0e+00 | yes |
| finance.hc3_amort | Debt | row 62 | 0.0e+00 | yes |
| finance.hc3_sweep | Debt | row 63 | 0.0e+00 | yes |
| finance.hc_ds | Debt | row 67 | 4.8e-11 | yes |
| finance.taxable_income | Tax | row 29 | 4.6e-11 | yes |
| finance.nol_open | Tax | row 30 | 4.9e-11 | yes |
| finance.nol_used | Tax | row 31 | 5.0e-11 | yes |
| finance.tax | Tax | row 32 | 5.0e-11 | yes |
| finance.nol_close | Tax | row 33 | 4.9e-11 | yes |
| finance.opco_ds | Waterfall | row 9 | 4.9e-11 | yes |
| finance.opco_dist | Waterfall | row 10 | 4.8e-11 | yes |
| finance.recap_opco | Waterfall | row 11 | 0.0e+00 | yes |
| finance.hc_excess | Waterfall | row 16 | 4.9e-11 | yes |
| finance.fund_dist_ops | Waterfall | row 19 | 4.9e-11 | yes |
| finance.recap_hold | Waterfall | row 20 | 0.0e+00 | yes |
| finance.recap_total | Waterfall | row 21 | 0.0e+00 | yes |
| finance.fund_dist | Waterfall | row 22 | 4.9e-11 | yes |
| finance.dscr_tl | Ratios | row 8 | 4.7e-11 | yes |
| finance.dscr_rf | Ratios | row 9 | 4.9e-11 | yes |
| finance.dscr_u | Ratios | row 10 | 0.0e+00 | yes |
| finance.dscr_opco | Ratios | row 11 | 4.6e-11 | yes |
| finance.hc_cov | Ratios | row 12 | 4.5e-11 | yes |
| finance.nav_df | Returns | row 96 | 5.0e-11 | yes |
| su.A1.opco_fee | Funding | F147 | 0.0e+00 | yes |
| su.A1.holdco_oid | Funding | F148 | 1.1e-15 | yes |
| su.A1.uses | Funding | F149 | 4.0e-13 | yes |
| su.A1.equity | Funding | F150 | 4.3e-14 | yes |
| su.A2.fee | Funding | F151 | 1.1e-16 | yes |
| su.A2.uses | Funding | F152 | 4.3e-14 | yes |
| su.A2.equity | Funding | F153 | 3.6e-15 | yes |
| su.A3.r8_deposit | Funding | F154 | 3.6e-15 | yes |
| su.A3.oid | Funding | F155 | 3.3e-16 | yes |
| su.A3.itc7_proceeds | Funding | F156 | 0.0e+00 | yes |
| su.A3.itc8_proceeds | Funding | F157 | 3.6e-15 | yes |
| su.A3.eq_signing | Funding | F159 | 0.0e+00 | yes |
| su.A3.carry | Funding | F160 | 1.4e-14 | yes |
| su.A3.eq_r7 | Funding | F162 | 0.0e+00 | yes |
| su.A3.carry2 | Funding | F163 | 4.9e-15 | yes |
| su.A3.eq_r8 | Funding | F165 | 4.3e-14 | yes |
| su.A3.cash_left_after_r8 | Funding | F166 | 0.0e+00 | yes |
| su.A3.uses | Funding | F167 | 1.4e-13 | yes |
| su.A3.equity | Funding | F168 | 4.3e-14 | yes |
| refi.mtm_opco_receivable | Funding | F174 | 4.4e-15 | yes |
| refi.mtm_redfern_payable | Funding | F175 | 4.4e-16 | yes |
| refi.costs | Funding | F176 | 4.0e-15 | yes |
| refi.tl_repay | Funding | F177 | 2.8e-13 | yes |
| refi.rf_repay | Funding | F178 | 5.0e-14 | yes |
| refi.opco_net | Funding | F179 | 8.5e-14 | yes |
| sc.tl_dscr_min_2022_2025 | Ratios | F15 | 2.7e-15 | yes |
| sc.tl_dscr_avg_2022_2025 | Ratios | F16 | 2.9e-15 | yes |
| sc.uspp_dscr_min_2026_2043 | Ratios | F17 | inf | NO |
| sc.uspp_dscr_avg_2026_2043 | Ratios | F18 | 0.0e+00 | yes |
| sc.rf_dscr_min | Ratios | F19 | 4.4e-16 | yes |
| sc.rf_dscr_avg | Ratios | F20 | 2.2e-16 | yes |
| sc.holdco_cov_min_2023_2031 | Ratios | F21 | 4.9e-15 | yes |
| sc.holdco_cov_avg_2023_2031 | Ratios | F22 | 8.9e-16 | yes |
| sc.fund_nav_2025 | Returns | F98 | 2.0e-13 | yes |
| sc.fund_contributions | Returns | F99 | 2.0e-13 | yes |
| sc.fund_distributions_life | Returns | F100 | 1.1e-13 | yes |
| sc.fund_distributions_to_2025 | Returns | F101 | 1.1e-14 | yes |
| sc.fund_moic_life_x | Returns | F102 | 1.8e-15 | yes |
| sc.fund_moic_2025_x | Returns | F103 | 3.3e-15 | yes |
| sc.fund_irr_life_pct | Returns | F150 | 3.6e-15 | yes |
| sc.fund_irr_2025_pct | Returns | F151 | 8.0e-15 | yes |

### sens_west_solar_capture_m5

| Key | Sheet | Location | Max diff | Pass |
|---|---|---|---|---|
| portfolio.north_atc | Operations | row 52 | 0.0e+00 | yes |
| portfolio.west_atc | Operations | row 53 | 0.0e+00 | yes |
| portfolio.south_atc | Operations | row 54 | 0.0e+00 | yes |
| portfolio.houston_atc | Operations | row 55 | 0.0e+00 | yes |
| portfolio.batt_rate | Operations | row 56 | 0.0e+00 | yes |
| portfolio.cap_hub_west_wind | Operations | row 57 | 0.0e+00 | yes |
| portfolio.cap_hub_panhandle_wind | Operations | row 58 | 0.0e+00 | yes |
| portfolio.cap_hub_west_solar | Operations | row 59 | 0.0e+00 | yes |
| portfolio.cap_hub_south_solar | Operations | row 60 | 0.0e+00 | yes |
| portfolio.cap_hub_coastal_wind | Operations | row 61 | 0.0e+00 | yes |
| R1.op_frac | Operations | row 63 | 0.0e+00 | yes |
| R1.own_share | Operations | row 65 | 1.9e-11 | yes |
| R1.hub_atc | Operations | row 66 | 0.0e+00 | yes |
| R1.deg | Operations | row 68 | 5.0e-11 | yes |
| R1.curt | Operations | row 69 | 0.0e+00 | yes |
| R1.gen_full | Operations | row 70 | 5.0e-11 | yes |
| R1.gen | Operations | row 71 | 4.8e-11 | yes |
| R1.cap_hub | Operations | row 72 | 0.0e+00 | yes |
| R1.cap_node | Operations | row 73 | 0.0e+00 | yes |
| R1.node_price | Operations | row 74 | 0.0e+00 | yes |
| R1.con_frac | Operations | row 75 | 0.0e+00 | yes |
| R1.con_vol | Operations | row 76 | 0.0e+00 | yes |
| R1.settle | Operations | row 77 | 2.0e-15 | yes |
| R1.mkt_gen | Operations | row 78 | 4.8e-11 | yes |
| R1.rev_contracted | Operations | row 79 | 0.0e+00 | yes |
| R1.rev_hedged | Operations | row 80 | 0.0e+00 | yes |
| R1.mkt_rev | Operations | row 81 | 4.9e-11 | yes |
| R1.revenue | Operations | row 82 | 4.9e-11 | yes |
| R1.rev_merchant | Operations | row 83 | 4.9e-11 | yes |
| R1.opex | Operations | row 84 | 4.9e-11 | yes |
| R1.land | Operations | row 85 | 5.0e-11 | yes |
| R1.bond | Operations | row 86 | 4.8e-11 | yes |
| R1.margin_tax | Operations | row 87 | 4.9e-11 | yes |
| R1.ebitda | Operations | row 88 | 5.0e-11 | yes |
| R1.aug | Operations | row 89 | 0.0e+00 | yes |
| R1.decom | Operations | row 90 | 3.3e-11 | yes |
| R1.cf | Operations | row 91 | 5.0e-11 | yes |
| R1.te_cash | Operations | row 92 | 0.0e+00 | yes |
| R1.mesa_tax_share | Operations | row 93 | 0.0e+00 | yes |
| R1.mesa_cf | Operations | row 94 | 5.0e-11 | yes |
| R1.mesa_taxable | Operations | row 95 | 5.0e-11 | yes |
| R1.s_contracted | Operations | row 97 | 0.0e+00 | yes |
| R1.s_hedged | Operations | row 98 | 2.8e-11 | yes |
| R1.s_merchant | Operations | row 99 | 2.8e-11 | yes |
| R1.mesa_rev | Operations | row 103 | 4.9e-11 | yes |
| R2.op_frac | Operations | row 105 | 4.1e-11 | yes |
| R2.own_share | Operations | row 107 | 1.9e-11 | yes |
| R2.hub_atc | Operations | row 108 | 0.0e+00 | yes |
| R2.deg | Operations | row 110 | 5.0e-11 | yes |
| R2.curt | Operations | row 111 | 0.0e+00 | yes |
| R2.gen_full | Operations | row 112 | 5.0e-11 | yes |
| R2.gen | Operations | row 113 | 5.0e-11 | yes |
| R2.cap_hub | Operations | row 114 | 0.0e+00 | yes |
| R2.cap_node | Operations | row 115 | 0.0e+00 | yes |
| R2.node_price | Operations | row 116 | 0.0e+00 | yes |
| R2.con_frac | Operations | row 117 | 4.1e-11 | yes |
| R2.con_vol | Operations | row 118 | 4.4e-11 | yes |
| R2.settle | Operations | row 119 | 4.5e-11 | yes |
| R2.mkt_gen | Operations | row 120 | 5.0e-11 | yes |
| R2.rev_contracted | Operations | row 121 | 4.5e-11 | yes |
| R2.rev_hedged | Operations | row 122 | 0.0e+00 | yes |
| R2.mkt_rev | Operations | row 123 | 4.8e-11 | yes |
| R2.revenue | Operations | row 124 | 5.0e-11 | yes |
| R2.rev_merchant | Operations | row 125 | 4.8e-11 | yes |
| R2.opex | Operations | row 126 | 4.7e-11 | yes |
| R2.land | Operations | row 127 | 5.0e-11 | yes |
| R2.bond | Operations | row 128 | 4.7e-11 | yes |
| R2.margin_tax | Operations | row 129 | 5.0e-11 | yes |
| R2.ebitda | Operations | row 130 | 4.7e-11 | yes |
| R2.aug | Operations | row 131 | 0.0e+00 | yes |
| R2.decom | Operations | row 132 | 4.0e-11 | yes |
| R2.cf | Operations | row 133 | 4.7e-11 | yes |
| R2.te_cash | Operations | row 134 | 0.0e+00 | yes |
| R2.mesa_tax_share | Operations | row 135 | 0.0e+00 | yes |
| R2.mesa_cf | Operations | row 136 | 4.7e-11 | yes |
| R2.mesa_taxable | Operations | row 137 | 4.7e-11 | yes |
| R2.s_contracted | Operations | row 139 | 4.2e-11 | yes |
| R2.s_hedged | Operations | row 140 | 0.0e+00 | yes |
| R2.s_merchant | Operations | row 141 | 4.2e-11 | yes |
| R2.mesa_rev | Operations | row 145 | 5.0e-11 | yes |
| R3.op_frac | Operations | row 147 | 4.9e-11 | yes |
| R3.own_share | Operations | row 149 | 1.9e-11 | yes |
| R3.hub_atc | Operations | row 150 | 0.0e+00 | yes |
| R3.deg | Operations | row 152 | 5.0e-11 | yes |
| R3.curt | Operations | row 153 | 0.0e+00 | yes |
| R3.gen_full | Operations | row 154 | 5.0e-11 | yes |
| R3.gen | Operations | row 155 | 5.0e-11 | yes |
| R3.cap_hub | Operations | row 156 | 0.0e+00 | yes |
| R3.cap_node | Operations | row 157 | 0.0e+00 | yes |
| R3.node_price | Operations | row 158 | 0.0e+00 | yes |
| R3.con_frac | Operations | row 159 | 0.0e+00 | yes |
| R3.con_vol | Operations | row 160 | 4.8e-11 | yes |
| R3.settle | Operations | row 161 | 5.0e-11 | yes |
| R3.mkt_gen | Operations | row 162 | 5.0e-11 | yes |
| R3.rev_contracted | Operations | row 163 | 0.0e+00 | yes |
| R3.rev_hedged | Operations | row 164 | 0.0e+00 | yes |
| R3.mkt_rev | Operations | row 165 | 5.0e-11 | yes |
| R3.revenue | Operations | row 166 | 5.0e-11 | yes |
| R3.rev_merchant | Operations | row 167 | 5.0e-11 | yes |
| R3.opex | Operations | row 168 | 5.0e-11 | yes |
| R3.land | Operations | row 169 | 5.0e-11 | yes |
| R3.bond | Operations | row 170 | 4.8e-11 | yes |
| R3.margin_tax | Operations | row 171 | 4.5e-11 | yes |
| R3.ebitda | Operations | row 172 | 5.0e-11 | yes |
| R3.aug | Operations | row 173 | 0.0e+00 | yes |
| R3.decom | Operations | row 174 | 8.9e-12 | yes |
| R3.cf | Operations | row 175 | 4.4e-11 | yes |
| R3.te_cash | Operations | row 177 | 0.0e+00 | yes |
| R3.mesa_tax_share | Operations | row 178 | 0.0e+00 | yes |
| R3.mesa_cf | Operations | row 179 | 4.3e-11 | yes |
| R3.mesa_taxable | Operations | row 180 | 5.0e-11 | yes |
| R3.s_contracted | Operations | row 182 | 4.5e-11 | yes |
| R3.s_hedged | Operations | row 183 | 0.0e+00 | yes |
| R3.s_merchant | Operations | row 184 | 4.5e-11 | yes |
| R3.mesa_rev | Operations | row 188 | 5.0e-11 | yes |
| R3.ptc_total | Operations | row 189 | 4.5e-11 | yes |
| R4.op_frac | Operations | row 191 | 2.9e-11 | yes |
| R4.own_share | Operations | row 193 | 1.9e-11 | yes |
| R4.hub_atc | Operations | row 194 | 0.0e+00 | yes |
| R4.deg | Operations | row 196 | 5.0e-11 | yes |
| R4.curt | Operations | row 197 | 0.0e+00 | yes |
| R4.gen_full | Operations | row 198 | 5.0e-11 | yes |
| R4.gen | Operations | row 199 | 5.0e-11 | yes |
| R4.cap_hub | Operations | row 200 | 0.0e+00 | yes |
| R4.cap_node | Operations | row 201 | 0.0e+00 | yes |
| R4.node_price | Operations | row 202 | 0.0e+00 | yes |
| R4.con_frac | Operations | row 203 | 0.0e+00 | yes |
| R4.con_vol | Operations | row 204 | 0.0e+00 | yes |
| R4.settle | Operations | row 205 | 1.0e-15 | yes |
| R4.mkt_gen | Operations | row 206 | 5.0e-11 | yes |
| R4.rev_contracted | Operations | row 207 | 0.0e+00 | yes |
| R4.rev_hedged | Operations | row 208 | 0.0e+00 | yes |
| R4.mkt_rev | Operations | row 209 | 5.0e-11 | yes |
| R4.revenue | Operations | row 210 | 5.0e-11 | yes |
| R4.rev_merchant | Operations | row 211 | 5.0e-11 | yes |
| R4.opex | Operations | row 212 | 5.0e-11 | yes |
| R4.land | Operations | row 213 | 0.0e+00 | yes |
| R4.bond | Operations | row 214 | 5.0e-11 | yes |
| R4.margin_tax | Operations | row 215 | 4.8e-11 | yes |
| R4.ebitda | Operations | row 216 | 5.0e-11 | yes |
| R4.aug | Operations | row 217 | 0.0e+00 | yes |
| R4.decom | Operations | row 218 | 1.9e-11 | yes |
| R4.cf | Operations | row 219 | 5.0e-11 | yes |
| R4.te_cash | Operations | row 220 | 0.0e+00 | yes |
| R4.mesa_tax_share | Operations | row 221 | 0.0e+00 | yes |
| R4.mesa_cf | Operations | row 222 | 5.0e-11 | yes |
| R4.mesa_taxable | Operations | row 223 | 5.0e-11 | yes |
| R4.s_contracted | Operations | row 225 | 0.0e+00 | yes |
| R4.s_hedged | Operations | row 226 | 4.5e-11 | yes |
| R4.s_merchant | Operations | row 227 | 4.5e-11 | yes |
| R4.mesa_rev | Operations | row 231 | 5.0e-11 | yes |
| R5.op_frac | Operations | row 233 | 3.7e-11 | yes |
| R5.own_share | Operations | row 235 | 1.9e-11 | yes |
| R5.hub_atc | Operations | row 236 | 0.0e+00 | yes |
| R5.deg | Operations | row 238 | 5.0e-11 | yes |
| R5.curt | Operations | row 239 | 0.0e+00 | yes |
| R5.gen_full | Operations | row 240 | 4.1e-11 | yes |
| R5.gen | Operations | row 241 | 4.9e-11 | yes |
| R5.cap_hub | Operations | row 242 | 0.0e+00 | yes |
| R5.cap_node | Operations | row 243 | 0.0e+00 | yes |
| R5.node_price | Operations | row 244 | 0.0e+00 | yes |
| R5.con_frac | Operations | row 245 | 4.1e-11 | yes |
| R5.con_vol | Operations | row 246 | 4.0e-11 | yes |
| R5.settle | Operations | row 247 | 4.5e-11 | yes |
| R5.mkt_gen | Operations | row 248 | 4.9e-11 | yes |
| R5.rev_contracted | Operations | row 249 | 4.0e-11 | yes |
| R5.rev_hedged | Operations | row 250 | 0.0e+00 | yes |
| R5.mkt_rev | Operations | row 251 | 4.7e-11 | yes |
| R5.revenue | Operations | row 252 | 4.7e-11 | yes |
| R5.rev_merchant | Operations | row 253 | 4.7e-11 | yes |
| R5.opex | Operations | row 254 | 4.9e-11 | yes |
| R5.land | Operations | row 255 | 0.0e+00 | yes |
| R5.bond | Operations | row 256 | 4.9e-11 | yes |
| R5.margin_tax | Operations | row 257 | 4.6e-11 | yes |
| R5.ebitda | Operations | row 258 | 4.8e-11 | yes |
| R5.aug | Operations | row 259 | 0.0e+00 | yes |
| R5.decom | Operations | row 260 | 2.0e-13 | yes |
| R5.cf | Operations | row 261 | 4.8e-11 | yes |
| R5.te_cash | Operations | row 263 | 4.4e-11 | yes |
| R5.mesa_tax_share | Operations | row 264 | 1.4e-12 | yes |
| R5.mesa_cf | Operations | row 265 | 4.9e-11 | yes |
| R5.mesa_taxable | Operations | row 266 | 4.9e-11 | yes |
| R5.s_contracted | Operations | row 268 | 4.5e-11 | yes |
| R5.s_hedged | Operations | row 269 | 0.0e+00 | yes |
| R5.s_merchant | Operations | row 270 | 4.5e-11 | yes |
| R5.mesa_rev | Operations | row 274 | 4.8e-11 | yes |
| R6.op_frac | Operations | row 276 | 4.2e-11 | yes |
| R6.own_share | Operations | row 278 | 2.4e-11 | yes |
| R6.hub_atc | Operations | row 279 | 0.0e+00 | yes |
| R6.con_frac | Operations | row 280 | 4.2e-11 | yes |
| R6.settle | Operations | row 281 | 4.0e-11 | yes |
| R6.stor_rev | Operations | row 282 | 3.2e-11 | yes |
| R6.rev_contracted | Operations | row 283 | 4.0e-11 | yes |
| R6.rev_hedged | Operations | row 284 | 0.0e+00 | yes |
| R6.revenue | Operations | row 285 | 4.0e-11 | yes |
| R6.rev_merchant | Operations | row 286 | 3.2e-11 | yes |
| R6.opex | Operations | row 287 | 4.9e-11 | yes |
| R6.land | Operations | row 288 | 0.0e+00 | yes |
| R6.bond | Operations | row 289 | 4.8e-11 | yes |
| R6.margin_tax | Operations | row 290 | 5.0e-11 | yes |
| R6.ebitda | Operations | row 291 | 5.0e-11 | yes |
| R6.aug | Operations | row 292 | 4.8e-12 | yes |
| R6.decom | Operations | row 293 | 2.5e-11 | yes |
| R6.cf | Operations | row 294 | 5.0e-11 | yes |
| R6.te_cash | Operations | row 295 | 0.0e+00 | yes |
| R6.mesa_tax_share | Operations | row 296 | 0.0e+00 | yes |
| R6.mesa_cf | Operations | row 297 | 5.0e-11 | yes |
| R6.mesa_taxable | Operations | row 298 | 5.0e-11 | yes |
| R6.s_contracted | Operations | row 300 | 3.8e-11 | yes |
| R6.s_hedged | Operations | row 301 | 0.0e+00 | yes |
| R6.s_merchant | Operations | row 302 | 3.8e-11 | yes |
| R6.mesa_rev | Operations | row 306 | 4.0e-11 | yes |
| R7.op_frac | Operations | row 308 | 4.4e-11 | yes |
| R7.own_share | Operations | row 310 | 0.0e+00 | yes |
| R7.hub_atc | Operations | row 311 | 0.0e+00 | yes |
| R7.con_frac | Operations | row 312 | 4.4e-11 | yes |
| R7.settle | Operations | row 314 | 3.6e-11 | yes |
| R7.stor_rev | Operations | row 315 | 4.6e-11 | yes |
| R7.rev_contracted | Operations | row 316 | 3.6e-11 | yes |
| R7.rev_hedged | Operations | row 317 | 0.0e+00 | yes |
| R7.revenue | Operations | row 318 | 4.6e-11 | yes |
| R7.rev_merchant | Operations | row 319 | 4.6e-11 | yes |
| R7.opex | Operations | row 320 | 5.0e-11 | yes |
| R7.land | Operations | row 321 | 0.0e+00 | yes |
| R7.bond | Operations | row 322 | 4.8e-11 | yes |
| R7.margin_tax | Operations | row 323 | 5.0e-11 | yes |
| R7.ebitda | Operations | row 324 | 5.0e-11 | yes |
| R7.aug | Operations | row 325 | 3.8e-11 | yes |
| R7.decom | Operations | row 326 | 2.3e-11 | yes |
| R7.cf | Operations | row 327 | 5.0e-11 | yes |
| R7.te_cash | Operations | row 328 | 0.0e+00 | yes |
| R7.mesa_tax_share | Operations | row 329 | 0.0e+00 | yes |
| R7.mesa_cf | Operations | row 330 | 5.0e-11 | yes |
| R7.mesa_taxable | Operations | row 331 | 5.0e-11 | yes |
| R7.s_contracted | Operations | row 333 | 3.1e-11 | yes |
| R7.s_hedged | Operations | row 334 | 0.0e+00 | yes |
| R7.s_merchant | Operations | row 335 | 3.1e-11 | yes |
| R7.mesa_rev | Operations | row 339 | 4.6e-11 | yes |
| R8.op_frac | Operations | row 341 | 4.6e-11 | yes |
| R8.own_share | Operations | row 343 | 0.0e+00 | yes |
| R8.hub_atc | Operations | row 344 | 0.0e+00 | yes |
| R8.deg | Operations | row 346 | 4.7e-11 | yes |
| R8.curt | Operations | row 347 | 0.0e+00 | yes |
| R8.gen_full | Operations | row 348 | 4.9e-11 | yes |
| R8.gen | Operations | row 349 | 4.9e-11 | yes |
| R8.cap_hub | Operations | row 350 | 0.0e+00 | yes |
| R8.cap_node | Operations | row 351 | 0.0e+00 | yes |
| R8.node_price | Operations | row 352 | 0.0e+00 | yes |
| R8.con_frac | Operations | row 353 | 0.0e+00 | yes |
| R8.con_vol | Operations | row 354 | 0.0e+00 | yes |
| R8.settle | Operations | row 355 | 4.8e-11 | yes |
| R8.mkt_gen | Operations | row 356 | 4.9e-11 | yes |
| R8.rev_contracted | Operations | row 357 | 0.0e+00 | yes |
| R8.rev_hedged | Operations | row 358 | 0.0e+00 | yes |
| R8.mkt_rev | Operations | row 359 | 4.9e-11 | yes |
| R8.revenue | Operations | row 360 | 4.9e-11 | yes |
| R8.rev_merchant | Operations | row 361 | 4.9e-11 | yes |
| R8.opex | Operations | row 362 | 5.0e-11 | yes |
| R8.land | Operations | row 363 | 0.0e+00 | yes |
| R8.bond | Operations | row 364 | 4.8e-11 | yes |
| R8.margin_tax | Operations | row 365 | 4.8e-11 | yes |
| R8.ebitda | Operations | row 366 | 4.8e-11 | yes |
| R8.aug | Operations | row 367 | 0.0e+00 | yes |
| R8.decom | Operations | row 368 | 3.5e-11 | yes |
| R8.cf | Operations | row 369 | 4.8e-11 | yes |
| R8.te_cash | Operations | row 370 | 0.0e+00 | yes |
| R8.mesa_tax_share | Operations | row 371 | 0.0e+00 | yes |
| R8.mesa_cf | Operations | row 372 | 4.8e-11 | yes |
| R8.mesa_taxable | Operations | row 373 | 4.8e-11 | yes |
| R8.s_contracted | Operations | row 375 | 0.0e+00 | yes |
| R8.s_hedged | Operations | row 376 | 3.6e-11 | yes |
| R8.s_merchant | Operations | row 377 | 3.6e-11 | yes |
| R8.mesa_rev | Operations | row 381 | 4.9e-11 | yes |
| portfolio.am_cost | Operations | row 384 | 5.0e-11 | yes |
| portfolio.mesa_rev_contracted_a1 | Operations | row 386 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_a1 | Operations | row 387 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_a1 | Operations | row 388 | 5.0e-11 | yes |
| portfolio.mesa_rev_a1 | Operations | row 389 | 4.9e-11 | yes |
| portfolio.mesa_rev_contracted_all | Operations | row 391 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_all | Operations | row 392 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_all | Operations | row 393 | 4.8e-11 | yes |
| portfolio.mesa_rev_all | Operations | row 394 | 4.8e-11 | yes |
| portfolio.cfads_a1 | Operations | row 400 | 5.0e-11 | yes |
| portfolio.cfads_all | Operations | row 401 | 4.7e-11 | yes |
| portfolio.cfads_a3 | Operations | row 402 | 4.9e-11 | yes |
| portfolio.share_contracted_a1 | Operations | row 403 | 4.3e-11 | yes |
| portfolio.share_hedged_a1 | Operations | row 404 | 3.9e-11 | yes |
| portfolio.share_merchant_a1 | Operations | row 405 | 4.1e-11 | yes |
| portfolio.share_contracted_all | Operations | row 409 | 4.1e-11 | yes |
| portfolio.share_hedged_all | Operations | row 410 | 4.9e-11 | yes |
| portfolio.share_merchant_all | Operations | row 411 | 4.8e-11 | yes |
| finance.dep | Tax | row 24 | 0.0e+00 | yes |
| finance.taxable_ops | Tax | row 25 | 4.7e-11 | yes |
| finance.tl_open | Debt | row 14 | 4.8e-11 | yes |
| finance.tl_int | Debt | row 15 | 3.9e-11 | yes |
| finance.tl_prin | Debt | row 16 | 3.1e-11 | yes |
| finance.tl_prepay | Debt | row 17 | 2.6e-11 | yes |
| finance.tl_ds | Debt | row 18 | 4.9e-11 | yes |
| finance.rf_open | Debt | row 23 | 3.6e-11 | yes |
| finance.rf_int | Debt | row 24 | 4.4e-11 | yes |
| finance.rf_prin | Debt | row 25 | 4.4e-11 | yes |
| finance.rf_prepay | Debt | row 26 | 2.7e-11 | yes |
| finance.rf_ds | Debt | row 27 | 3.0e-11 | yes |
| finance.u_open | Debt | row 31 | 4.7e-11 | yes |
| finance.u_int | Debt | row 32 | 4.8e-11 | yes |
| finance.u_prin | Debt | row 33 | 4.9e-11 | yes |
| finance.u_ds | Debt | row 34 | 4.3e-11 | yes |
| finance.hc1_open | Debt | row 46 | 4.6e-11 | yes |
| finance.hc1_int | Debt | row 47 | 4.3e-11 | yes |
| finance.hc1_amort | Debt | row 48 | 1.4e-11 | yes |
| finance.hc1_sweep | Debt | row 49 | 3.1e-11 | yes |
| finance.hc1_repay | Debt | row 51 | 2.1e-11 | yes |
| finance.hc2_open | Debt | row 53 | 3.2e-11 | yes |
| finance.hc2_int | Debt | row 54 | 9.6e-12 | yes |
| finance.hc2_amort | Debt | row 55 | 3.9e-11 | yes |
| finance.hc2_sweep | Debt | row 56 | 4.4e-11 | yes |
| finance.hc2_repay | Debt | row 58 | 1.1e-11 | yes |
| finance.hc3_open | Debt | row 60 | 5.0e-11 | yes |
| finance.hc3_int | Debt | row 61 | 4.9e-11 | yes |
| finance.hc3_amort | Debt | row 62 | 3.2e-12 | yes |
| finance.hc3_sweep | Debt | row 63 | 4.9e-11 | yes |
| finance.hc_ds | Debt | row 67 | 5.0e-11 | yes |
| finance.taxable_income | Tax | row 29 | 4.9e-11 | yes |
| finance.nol_open | Tax | row 30 | 4.9e-11 | yes |
| finance.nol_used | Tax | row 31 | 4.9e-11 | yes |
| finance.tax | Tax | row 32 | 4.8e-11 | yes |
| finance.nol_close | Tax | row 33 | 4.9e-11 | yes |
| finance.opco_ds | Waterfall | row 9 | 4.9e-11 | yes |
| finance.opco_dist | Waterfall | row 10 | 4.9e-11 | yes |
| finance.recap_opco | Waterfall | row 11 | 3.6e-11 | yes |
| finance.hc_excess | Waterfall | row 16 | 5.0e-11 | yes |
| finance.fund_dist_ops | Waterfall | row 19 | 5.0e-11 | yes |
| finance.recap_hold | Waterfall | row 20 | 3.2e-11 | yes |
| finance.recap_total | Waterfall | row 21 | 3.2e-11 | yes |
| finance.fund_dist | Waterfall | row 22 | 5.0e-11 | yes |
| finance.dscr_tl | Ratios | row 8 | 3.9e-11 | yes |
| finance.dscr_rf | Ratios | row 9 | 0.0e+00 | yes |
| finance.dscr_u | Ratios | row 10 | 4.9e-11 | yes |
| finance.dscr_opco | Ratios | row 11 | 4.9e-11 | yes |
| finance.hc_cov | Ratios | row 12 | 4.7e-11 | yes |
| finance.nav_df | Returns | row 96 | 5.0e-11 | yes |
| su.A1.opco_fee | Funding | F147 | 0.0e+00 | yes |
| su.A1.holdco_oid | Funding | F148 | 1.1e-15 | yes |
| su.A1.uses | Funding | F149 | 4.0e-13 | yes |
| su.A1.equity | Funding | F150 | 4.3e-14 | yes |
| su.A2.fee | Funding | F151 | 1.1e-16 | yes |
| su.A2.uses | Funding | F152 | 4.3e-14 | yes |
| su.A2.equity | Funding | F153 | 3.6e-15 | yes |
| su.A3.r8_deposit | Funding | F154 | 3.6e-15 | yes |
| su.A3.oid | Funding | F155 | 3.3e-16 | yes |
| su.A3.itc7_proceeds | Funding | F156 | 0.0e+00 | yes |
| su.A3.itc8_proceeds | Funding | F157 | 3.6e-15 | yes |
| su.A3.eq_signing | Funding | F159 | 0.0e+00 | yes |
| su.A3.carry | Funding | F160 | 1.4e-14 | yes |
| su.A3.eq_r7 | Funding | F162 | 0.0e+00 | yes |
| su.A3.carry2 | Funding | F163 | 4.9e-15 | yes |
| su.A3.eq_r8 | Funding | F165 | 4.3e-14 | yes |
| su.A3.cash_left_after_r8 | Funding | F166 | 0.0e+00 | yes |
| su.A3.uses | Funding | F167 | 1.4e-13 | yes |
| su.A3.equity | Funding | F168 | 4.3e-14 | yes |
| refi.mtm_opco_receivable | Funding | F174 | 4.4e-15 | yes |
| refi.mtm_redfern_payable | Funding | F175 | 4.4e-16 | yes |
| refi.costs | Funding | F176 | 4.0e-15 | yes |
| refi.tl_repay | Funding | F177 | 2.8e-13 | yes |
| refi.rf_repay | Funding | F178 | 5.0e-14 | yes |
| refi.opco_net | Funding | F179 | 8.5e-14 | yes |
| sc.tl_dscr_min_2022_2025 | Ratios | F15 | 5.1e-15 | yes |
| sc.tl_dscr_avg_2022_2025 | Ratios | F16 | 4.0e-15 | yes |
| sc.uspp_dscr_min_2026_2043 | Ratios | F17 | 8.9e-16 | yes |
| sc.uspp_dscr_avg_2026_2043 | Ratios | F18 | 3.3e-15 | yes |
| sc.rf_dscr_min | Ratios | F19 | 0.0e+00 | yes |
| sc.rf_dscr_avg | Ratios | F20 | 0.0e+00 | yes |
| sc.holdco_cov_min_2023_2031 | Ratios | F21 | 3.3e-15 | yes |
| sc.holdco_cov_avg_2023_2031 | Ratios | F22 | 8.9e-16 | yes |
| sc.fund_nav_2025 | Returns | F98 | 5.7e-14 | yes |
| sc.fund_contributions | Returns | F99 | 2.0e-13 | yes |
| sc.fund_distributions_life | Returns | F100 | 4.5e-13 | yes |
| sc.fund_distributions_to_2025 | Returns | F101 | 2.6e-13 | yes |
| sc.fund_moic_life_x | Returns | F102 | 1.8e-15 | yes |
| sc.fund_moic_2025_x | Returns | F103 | 4.0e-15 | yes |
| sc.fund_irr_life_pct | Returns | F150 | 2.0e-14 | yes |
| sc.fund_irr_2025_pct | Returns | F151 | 3.4e-14 | yes |

### sens_battery_low

| Key | Sheet | Location | Max diff | Pass |
|---|---|---|---|---|
| portfolio.north_atc | Operations | row 52 | 0.0e+00 | yes |
| portfolio.west_atc | Operations | row 53 | 0.0e+00 | yes |
| portfolio.south_atc | Operations | row 54 | 0.0e+00 | yes |
| portfolio.houston_atc | Operations | row 55 | 0.0e+00 | yes |
| portfolio.batt_rate | Operations | row 56 | 0.0e+00 | yes |
| portfolio.cap_hub_west_wind | Operations | row 57 | 0.0e+00 | yes |
| portfolio.cap_hub_panhandle_wind | Operations | row 58 | 0.0e+00 | yes |
| portfolio.cap_hub_west_solar | Operations | row 59 | 0.0e+00 | yes |
| portfolio.cap_hub_south_solar | Operations | row 60 | 0.0e+00 | yes |
| portfolio.cap_hub_coastal_wind | Operations | row 61 | 0.0e+00 | yes |
| R1.op_frac | Operations | row 63 | 0.0e+00 | yes |
| R1.own_share | Operations | row 65 | 1.9e-11 | yes |
| R1.hub_atc | Operations | row 66 | 0.0e+00 | yes |
| R1.deg | Operations | row 68 | 5.0e-11 | yes |
| R1.curt | Operations | row 69 | 0.0e+00 | yes |
| R1.gen_full | Operations | row 70 | 5.0e-11 | yes |
| R1.gen | Operations | row 71 | 4.8e-11 | yes |
| R1.cap_hub | Operations | row 72 | 0.0e+00 | yes |
| R1.cap_node | Operations | row 73 | 0.0e+00 | yes |
| R1.node_price | Operations | row 74 | 0.0e+00 | yes |
| R1.con_frac | Operations | row 75 | 0.0e+00 | yes |
| R1.con_vol | Operations | row 76 | 0.0e+00 | yes |
| R1.settle | Operations | row 77 | 2.0e-15 | yes |
| R1.mkt_gen | Operations | row 78 | 4.8e-11 | yes |
| R1.rev_contracted | Operations | row 79 | 0.0e+00 | yes |
| R1.rev_hedged | Operations | row 80 | 0.0e+00 | yes |
| R1.mkt_rev | Operations | row 81 | 4.9e-11 | yes |
| R1.revenue | Operations | row 82 | 4.9e-11 | yes |
| R1.rev_merchant | Operations | row 83 | 4.9e-11 | yes |
| R1.opex | Operations | row 84 | 4.9e-11 | yes |
| R1.land | Operations | row 85 | 5.0e-11 | yes |
| R1.bond | Operations | row 86 | 4.8e-11 | yes |
| R1.margin_tax | Operations | row 87 | 4.9e-11 | yes |
| R1.ebitda | Operations | row 88 | 5.0e-11 | yes |
| R1.aug | Operations | row 89 | 0.0e+00 | yes |
| R1.decom | Operations | row 90 | 3.3e-11 | yes |
| R1.cf | Operations | row 91 | 5.0e-11 | yes |
| R1.te_cash | Operations | row 92 | 0.0e+00 | yes |
| R1.mesa_tax_share | Operations | row 93 | 0.0e+00 | yes |
| R1.mesa_cf | Operations | row 94 | 5.0e-11 | yes |
| R1.mesa_taxable | Operations | row 95 | 5.0e-11 | yes |
| R1.s_contracted | Operations | row 97 | 0.0e+00 | yes |
| R1.s_hedged | Operations | row 98 | 2.8e-11 | yes |
| R1.s_merchant | Operations | row 99 | 2.8e-11 | yes |
| R1.mesa_rev | Operations | row 103 | 4.9e-11 | yes |
| R2.op_frac | Operations | row 105 | 4.1e-11 | yes |
| R2.own_share | Operations | row 107 | 1.9e-11 | yes |
| R2.hub_atc | Operations | row 108 | 0.0e+00 | yes |
| R2.deg | Operations | row 110 | 5.0e-11 | yes |
| R2.curt | Operations | row 111 | 0.0e+00 | yes |
| R2.gen_full | Operations | row 112 | 5.0e-11 | yes |
| R2.gen | Operations | row 113 | 5.0e-11 | yes |
| R2.cap_hub | Operations | row 114 | 0.0e+00 | yes |
| R2.cap_node | Operations | row 115 | 0.0e+00 | yes |
| R2.node_price | Operations | row 116 | 0.0e+00 | yes |
| R2.con_frac | Operations | row 117 | 4.1e-11 | yes |
| R2.con_vol | Operations | row 118 | 4.4e-11 | yes |
| R2.settle | Operations | row 119 | 4.5e-11 | yes |
| R2.mkt_gen | Operations | row 120 | 5.0e-11 | yes |
| R2.rev_contracted | Operations | row 121 | 4.5e-11 | yes |
| R2.rev_hedged | Operations | row 122 | 0.0e+00 | yes |
| R2.mkt_rev | Operations | row 123 | 4.8e-11 | yes |
| R2.revenue | Operations | row 124 | 5.0e-11 | yes |
| R2.rev_merchant | Operations | row 125 | 4.8e-11 | yes |
| R2.opex | Operations | row 126 | 4.7e-11 | yes |
| R2.land | Operations | row 127 | 5.0e-11 | yes |
| R2.bond | Operations | row 128 | 4.7e-11 | yes |
| R2.margin_tax | Operations | row 129 | 5.0e-11 | yes |
| R2.ebitda | Operations | row 130 | 4.7e-11 | yes |
| R2.aug | Operations | row 131 | 0.0e+00 | yes |
| R2.decom | Operations | row 132 | 4.0e-11 | yes |
| R2.cf | Operations | row 133 | 4.7e-11 | yes |
| R2.te_cash | Operations | row 134 | 0.0e+00 | yes |
| R2.mesa_tax_share | Operations | row 135 | 0.0e+00 | yes |
| R2.mesa_cf | Operations | row 136 | 4.7e-11 | yes |
| R2.mesa_taxable | Operations | row 137 | 4.7e-11 | yes |
| R2.s_contracted | Operations | row 139 | 4.2e-11 | yes |
| R2.s_hedged | Operations | row 140 | 0.0e+00 | yes |
| R2.s_merchant | Operations | row 141 | 4.2e-11 | yes |
| R2.mesa_rev | Operations | row 145 | 5.0e-11 | yes |
| R3.op_frac | Operations | row 147 | 4.9e-11 | yes |
| R3.own_share | Operations | row 149 | 1.9e-11 | yes |
| R3.hub_atc | Operations | row 150 | 0.0e+00 | yes |
| R3.deg | Operations | row 152 | 5.0e-11 | yes |
| R3.curt | Operations | row 153 | 0.0e+00 | yes |
| R3.gen_full | Operations | row 154 | 5.0e-11 | yes |
| R3.gen | Operations | row 155 | 5.0e-11 | yes |
| R3.cap_hub | Operations | row 156 | 0.0e+00 | yes |
| R3.cap_node | Operations | row 157 | 0.0e+00 | yes |
| R3.node_price | Operations | row 158 | 0.0e+00 | yes |
| R3.con_frac | Operations | row 159 | 0.0e+00 | yes |
| R3.con_vol | Operations | row 160 | 4.8e-11 | yes |
| R3.settle | Operations | row 161 | 5.0e-11 | yes |
| R3.mkt_gen | Operations | row 162 | 5.0e-11 | yes |
| R3.rev_contracted | Operations | row 163 | 0.0e+00 | yes |
| R3.rev_hedged | Operations | row 164 | 0.0e+00 | yes |
| R3.mkt_rev | Operations | row 165 | 5.0e-11 | yes |
| R3.revenue | Operations | row 166 | 5.0e-11 | yes |
| R3.rev_merchant | Operations | row 167 | 5.0e-11 | yes |
| R3.opex | Operations | row 168 | 5.0e-11 | yes |
| R3.land | Operations | row 169 | 5.0e-11 | yes |
| R3.bond | Operations | row 170 | 4.8e-11 | yes |
| R3.margin_tax | Operations | row 171 | 4.5e-11 | yes |
| R3.ebitda | Operations | row 172 | 5.0e-11 | yes |
| R3.aug | Operations | row 173 | 0.0e+00 | yes |
| R3.decom | Operations | row 174 | 8.9e-12 | yes |
| R3.cf | Operations | row 175 | 4.4e-11 | yes |
| R3.te_cash | Operations | row 177 | 0.0e+00 | yes |
| R3.mesa_tax_share | Operations | row 178 | 0.0e+00 | yes |
| R3.mesa_cf | Operations | row 179 | 4.3e-11 | yes |
| R3.mesa_taxable | Operations | row 180 | 5.0e-11 | yes |
| R3.s_contracted | Operations | row 182 | 4.5e-11 | yes |
| R3.s_hedged | Operations | row 183 | 0.0e+00 | yes |
| R3.s_merchant | Operations | row 184 | 4.5e-11 | yes |
| R3.mesa_rev | Operations | row 188 | 5.0e-11 | yes |
| R3.ptc_total | Operations | row 189 | 4.5e-11 | yes |
| R4.op_frac | Operations | row 191 | 2.9e-11 | yes |
| R4.own_share | Operations | row 193 | 1.9e-11 | yes |
| R4.hub_atc | Operations | row 194 | 0.0e+00 | yes |
| R4.deg | Operations | row 196 | 5.0e-11 | yes |
| R4.curt | Operations | row 197 | 0.0e+00 | yes |
| R4.gen_full | Operations | row 198 | 5.0e-11 | yes |
| R4.gen | Operations | row 199 | 5.0e-11 | yes |
| R4.cap_hub | Operations | row 200 | 0.0e+00 | yes |
| R4.cap_node | Operations | row 201 | 0.0e+00 | yes |
| R4.node_price | Operations | row 202 | 0.0e+00 | yes |
| R4.con_frac | Operations | row 203 | 0.0e+00 | yes |
| R4.con_vol | Operations | row 204 | 0.0e+00 | yes |
| R4.settle | Operations | row 205 | 1.0e-15 | yes |
| R4.mkt_gen | Operations | row 206 | 5.0e-11 | yes |
| R4.rev_contracted | Operations | row 207 | 0.0e+00 | yes |
| R4.rev_hedged | Operations | row 208 | 0.0e+00 | yes |
| R4.mkt_rev | Operations | row 209 | 4.9e-11 | yes |
| R4.revenue | Operations | row 210 | 4.9e-11 | yes |
| R4.rev_merchant | Operations | row 211 | 4.9e-11 | yes |
| R4.opex | Operations | row 212 | 5.0e-11 | yes |
| R4.land | Operations | row 213 | 0.0e+00 | yes |
| R4.bond | Operations | row 214 | 5.0e-11 | yes |
| R4.margin_tax | Operations | row 215 | 5.0e-11 | yes |
| R4.ebitda | Operations | row 216 | 4.9e-11 | yes |
| R4.aug | Operations | row 217 | 0.0e+00 | yes |
| R4.decom | Operations | row 218 | 1.9e-11 | yes |
| R4.cf | Operations | row 219 | 4.9e-11 | yes |
| R4.te_cash | Operations | row 220 | 0.0e+00 | yes |
| R4.mesa_tax_share | Operations | row 221 | 0.0e+00 | yes |
| R4.mesa_cf | Operations | row 222 | 4.9e-11 | yes |
| R4.mesa_taxable | Operations | row 223 | 4.9e-11 | yes |
| R4.s_contracted | Operations | row 225 | 0.0e+00 | yes |
| R4.s_hedged | Operations | row 226 | 4.6e-11 | yes |
| R4.s_merchant | Operations | row 227 | 4.6e-11 | yes |
| R4.mesa_rev | Operations | row 231 | 4.9e-11 | yes |
| R5.op_frac | Operations | row 233 | 3.7e-11 | yes |
| R5.own_share | Operations | row 235 | 1.9e-11 | yes |
| R5.hub_atc | Operations | row 236 | 0.0e+00 | yes |
| R5.deg | Operations | row 238 | 5.0e-11 | yes |
| R5.curt | Operations | row 239 | 0.0e+00 | yes |
| R5.gen_full | Operations | row 240 | 4.1e-11 | yes |
| R5.gen | Operations | row 241 | 4.9e-11 | yes |
| R5.cap_hub | Operations | row 242 | 0.0e+00 | yes |
| R5.cap_node | Operations | row 243 | 0.0e+00 | yes |
| R5.node_price | Operations | row 244 | 0.0e+00 | yes |
| R5.con_frac | Operations | row 245 | 4.1e-11 | yes |
| R5.con_vol | Operations | row 246 | 4.0e-11 | yes |
| R5.settle | Operations | row 247 | 4.8e-11 | yes |
| R5.mkt_gen | Operations | row 248 | 4.9e-11 | yes |
| R5.rev_contracted | Operations | row 249 | 4.0e-11 | yes |
| R5.rev_hedged | Operations | row 250 | 0.0e+00 | yes |
| R5.mkt_rev | Operations | row 251 | 4.9e-11 | yes |
| R5.revenue | Operations | row 252 | 4.9e-11 | yes |
| R5.rev_merchant | Operations | row 253 | 4.9e-11 | yes |
| R5.opex | Operations | row 254 | 4.9e-11 | yes |
| R5.land | Operations | row 255 | 0.0e+00 | yes |
| R5.bond | Operations | row 256 | 4.9e-11 | yes |
| R5.margin_tax | Operations | row 257 | 4.5e-11 | yes |
| R5.ebitda | Operations | row 258 | 5.0e-11 | yes |
| R5.aug | Operations | row 259 | 0.0e+00 | yes |
| R5.decom | Operations | row 260 | 2.0e-13 | yes |
| R5.cf | Operations | row 261 | 5.0e-11 | yes |
| R5.te_cash | Operations | row 263 | 4.4e-11 | yes |
| R5.mesa_tax_share | Operations | row 264 | 1.4e-12 | yes |
| R5.mesa_cf | Operations | row 265 | 4.8e-11 | yes |
| R5.mesa_taxable | Operations | row 266 | 4.8e-11 | yes |
| R5.s_contracted | Operations | row 268 | 4.5e-11 | yes |
| R5.s_hedged | Operations | row 269 | 0.0e+00 | yes |
| R5.s_merchant | Operations | row 270 | 4.5e-11 | yes |
| R5.mesa_rev | Operations | row 274 | 4.7e-11 | yes |
| R6.op_frac | Operations | row 276 | 4.2e-11 | yes |
| R6.own_share | Operations | row 278 | 2.4e-11 | yes |
| R6.hub_atc | Operations | row 279 | 0.0e+00 | yes |
| R6.con_frac | Operations | row 280 | 4.2e-11 | yes |
| R6.settle | Operations | row 281 | 4.0e-11 | yes |
| R6.stor_rev | Operations | row 282 | 3.2e-11 | yes |
| R6.rev_contracted | Operations | row 283 | 4.0e-11 | yes |
| R6.rev_hedged | Operations | row 284 | 0.0e+00 | yes |
| R6.revenue | Operations | row 285 | 4.0e-11 | yes |
| R6.rev_merchant | Operations | row 286 | 3.2e-11 | yes |
| R6.opex | Operations | row 287 | 4.9e-11 | yes |
| R6.land | Operations | row 288 | 0.0e+00 | yes |
| R6.bond | Operations | row 289 | 4.8e-11 | yes |
| R6.margin_tax | Operations | row 290 | 5.0e-11 | yes |
| R6.ebitda | Operations | row 291 | 5.0e-11 | yes |
| R6.aug | Operations | row 292 | 4.8e-12 | yes |
| R6.decom | Operations | row 293 | 2.5e-11 | yes |
| R6.cf | Operations | row 294 | 5.0e-11 | yes |
| R6.te_cash | Operations | row 295 | 0.0e+00 | yes |
| R6.mesa_tax_share | Operations | row 296 | 0.0e+00 | yes |
| R6.mesa_cf | Operations | row 297 | 5.0e-11 | yes |
| R6.mesa_taxable | Operations | row 298 | 5.0e-11 | yes |
| R6.s_contracted | Operations | row 300 | 2.7e-11 | yes |
| R6.s_hedged | Operations | row 301 | 0.0e+00 | yes |
| R6.s_merchant | Operations | row 302 | 2.7e-11 | yes |
| R6.mesa_rev | Operations | row 306 | 4.0e-11 | yes |
| R7.op_frac | Operations | row 308 | 4.4e-11 | yes |
| R7.own_share | Operations | row 310 | 0.0e+00 | yes |
| R7.hub_atc | Operations | row 311 | 0.0e+00 | yes |
| R7.con_frac | Operations | row 312 | 4.4e-11 | yes |
| R7.settle | Operations | row 314 | 3.6e-11 | yes |
| R7.stor_rev | Operations | row 315 | 4.4e-11 | yes |
| R7.rev_contracted | Operations | row 316 | 3.6e-11 | yes |
| R7.rev_hedged | Operations | row 317 | 0.0e+00 | yes |
| R7.revenue | Operations | row 318 | 8.2e-12 | yes |
| R7.rev_merchant | Operations | row 319 | 4.4e-11 | yes |
| R7.opex | Operations | row 320 | 5.0e-11 | yes |
| R7.land | Operations | row 321 | 0.0e+00 | yes |
| R7.bond | Operations | row 322 | 4.8e-11 | yes |
| R7.margin_tax | Operations | row 323 | 5.0e-11 | yes |
| R7.ebitda | Operations | row 324 | 5.0e-11 | yes |
| R7.aug | Operations | row 325 | 3.8e-11 | yes |
| R7.decom | Operations | row 326 | 2.3e-11 | yes |
| R7.cf | Operations | row 327 | 5.0e-11 | yes |
| R7.te_cash | Operations | row 328 | 0.0e+00 | yes |
| R7.mesa_tax_share | Operations | row 329 | 0.0e+00 | yes |
| R7.mesa_cf | Operations | row 330 | 5.0e-11 | yes |
| R7.mesa_taxable | Operations | row 331 | 5.0e-11 | yes |
| R7.s_contracted | Operations | row 333 | 8.2e-12 | yes |
| R7.s_hedged | Operations | row 334 | 0.0e+00 | yes |
| R7.s_merchant | Operations | row 335 | 8.2e-12 | yes |
| R7.mesa_rev | Operations | row 339 | 8.2e-12 | yes |
| R8.op_frac | Operations | row 341 | 4.6e-11 | yes |
| R8.own_share | Operations | row 343 | 0.0e+00 | yes |
| R8.hub_atc | Operations | row 344 | 0.0e+00 | yes |
| R8.deg | Operations | row 346 | 4.7e-11 | yes |
| R8.curt | Operations | row 347 | 0.0e+00 | yes |
| R8.gen_full | Operations | row 348 | 4.9e-11 | yes |
| R8.gen | Operations | row 349 | 4.9e-11 | yes |
| R8.cap_hub | Operations | row 350 | 0.0e+00 | yes |
| R8.cap_node | Operations | row 351 | 0.0e+00 | yes |
| R8.node_price | Operations | row 352 | 0.0e+00 | yes |
| R8.con_frac | Operations | row 353 | 0.0e+00 | yes |
| R8.con_vol | Operations | row 354 | 0.0e+00 | yes |
| R8.settle | Operations | row 355 | 4.8e-11 | yes |
| R8.mkt_gen | Operations | row 356 | 4.9e-11 | yes |
| R8.rev_contracted | Operations | row 357 | 0.0e+00 | yes |
| R8.rev_hedged | Operations | row 358 | 0.0e+00 | yes |
| R8.mkt_rev | Operations | row 359 | 4.9e-11 | yes |
| R8.revenue | Operations | row 360 | 4.9e-11 | yes |
| R8.rev_merchant | Operations | row 361 | 4.9e-11 | yes |
| R8.opex | Operations | row 362 | 5.0e-11 | yes |
| R8.land | Operations | row 363 | 0.0e+00 | yes |
| R8.bond | Operations | row 364 | 4.8e-11 | yes |
| R8.margin_tax | Operations | row 365 | 4.8e-11 | yes |
| R8.ebitda | Operations | row 366 | 4.8e-11 | yes |
| R8.aug | Operations | row 367 | 0.0e+00 | yes |
| R8.decom | Operations | row 368 | 3.5e-11 | yes |
| R8.cf | Operations | row 369 | 4.8e-11 | yes |
| R8.te_cash | Operations | row 370 | 0.0e+00 | yes |
| R8.mesa_tax_share | Operations | row 371 | 0.0e+00 | yes |
| R8.mesa_cf | Operations | row 372 | 4.8e-11 | yes |
| R8.mesa_taxable | Operations | row 373 | 4.8e-11 | yes |
| R8.s_contracted | Operations | row 375 | 0.0e+00 | yes |
| R8.s_hedged | Operations | row 376 | 3.6e-11 | yes |
| R8.s_merchant | Operations | row 377 | 3.6e-11 | yes |
| R8.mesa_rev | Operations | row 381 | 4.9e-11 | yes |
| portfolio.am_cost | Operations | row 384 | 5.0e-11 | yes |
| portfolio.mesa_rev_contracted_a1 | Operations | row 386 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_a1 | Operations | row 387 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_a1 | Operations | row 388 | 4.9e-11 | yes |
| portfolio.mesa_rev_a1 | Operations | row 389 | 4.9e-11 | yes |
| portfolio.mesa_rev_contracted_all | Operations | row 391 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_all | Operations | row 392 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_all | Operations | row 393 | 4.8e-11 | yes |
| portfolio.mesa_rev_all | Operations | row 394 | 4.9e-11 | yes |
| portfolio.cfads_a1 | Operations | row 400 | 4.9e-11 | yes |
| portfolio.cfads_all | Operations | row 401 | 5.0e-11 | yes |
| portfolio.cfads_a3 | Operations | row 402 | 5.0e-11 | yes |
| portfolio.share_contracted_a1 | Operations | row 403 | 4.7e-11 | yes |
| portfolio.share_hedged_a1 | Operations | row 404 | 4.5e-11 | yes |
| portfolio.share_merchant_a1 | Operations | row 405 | 4.8e-11 | yes |
| portfolio.share_contracted_all | Operations | row 409 | 4.7e-11 | yes |
| portfolio.share_hedged_all | Operations | row 410 | 4.7e-11 | yes |
| portfolio.share_merchant_all | Operations | row 411 | 3.1e-11 | yes |
| finance.dep | Tax | row 24 | 0.0e+00 | yes |
| finance.taxable_ops | Tax | row 25 | 5.0e-11 | yes |
| finance.tl_open | Debt | row 14 | 4.8e-11 | yes |
| finance.tl_int | Debt | row 15 | 3.9e-11 | yes |
| finance.tl_prin | Debt | row 16 | 3.1e-11 | yes |
| finance.tl_prepay | Debt | row 17 | 2.6e-11 | yes |
| finance.tl_ds | Debt | row 18 | 4.9e-11 | yes |
| finance.rf_open | Debt | row 23 | 3.6e-11 | yes |
| finance.rf_int | Debt | row 24 | 4.4e-11 | yes |
| finance.rf_prin | Debt | row 25 | 4.4e-11 | yes |
| finance.rf_prepay | Debt | row 26 | 2.7e-11 | yes |
| finance.rf_ds | Debt | row 27 | 3.0e-11 | yes |
| finance.u_open | Debt | row 31 | 4.7e-11 | yes |
| finance.u_int | Debt | row 32 | 4.8e-11 | yes |
| finance.u_prin | Debt | row 33 | 4.9e-11 | yes |
| finance.u_ds | Debt | row 34 | 4.3e-11 | yes |
| finance.hc1_open | Debt | row 46 | 3.5e-11 | yes |
| finance.hc1_int | Debt | row 47 | 3.8e-11 | yes |
| finance.hc1_amort | Debt | row 48 | 1.4e-11 | yes |
| finance.hc1_sweep | Debt | row 49 | 2.7e-11 | yes |
| finance.hc1_repay | Debt | row 51 | 2.0e-11 | yes |
| finance.hc2_open | Debt | row 53 | 4.9e-11 | yes |
| finance.hc2_int | Debt | row 54 | 1.3e-11 | yes |
| finance.hc2_amort | Debt | row 55 | 3.9e-11 | yes |
| finance.hc2_sweep | Debt | row 56 | 4.0e-11 | yes |
| finance.hc2_repay | Debt | row 58 | 3.0e-11 | yes |
| finance.hc3_open | Debt | row 60 | 4.1e-11 | yes |
| finance.hc3_int | Debt | row 61 | 4.8e-11 | yes |
| finance.hc3_amort | Debt | row 62 | 3.2e-12 | yes |
| finance.hc3_sweep | Debt | row 63 | 4.6e-11 | yes |
| finance.hc_ds | Debt | row 67 | 4.9e-11 | yes |
| finance.taxable_income | Tax | row 29 | 4.8e-11 | yes |
| finance.nol_open | Tax | row 30 | 4.8e-11 | yes |
| finance.nol_used | Tax | row 31 | 4.7e-11 | yes |
| finance.tax | Tax | row 32 | 5.0e-11 | yes |
| finance.nol_close | Tax | row 33 | 4.8e-11 | yes |
| finance.opco_ds | Waterfall | row 9 | 4.9e-11 | yes |
| finance.opco_dist | Waterfall | row 10 | 4.9e-11 | yes |
| finance.recap_opco | Waterfall | row 11 | 3.6e-11 | yes |
| finance.hc_excess | Waterfall | row 16 | 5.0e-11 | yes |
| finance.fund_dist_ops | Waterfall | row 19 | 4.8e-11 | yes |
| finance.recap_hold | Waterfall | row 20 | 1.2e-11 | yes |
| finance.recap_total | Waterfall | row 21 | 4.8e-11 | yes |
| finance.fund_dist | Waterfall | row 22 | 4.8e-11 | yes |
| finance.dscr_tl | Ratios | row 8 | 4.7e-11 | yes |
| finance.dscr_rf | Ratios | row 9 | 0.0e+00 | yes |
| finance.dscr_u | Ratios | row 10 | 4.8e-11 | yes |
| finance.dscr_opco | Ratios | row 11 | 4.8e-11 | yes |
| finance.hc_cov | Ratios | row 12 | 4.3e-11 | yes |
| finance.nav_df | Returns | row 96 | 5.0e-11 | yes |
| su.A1.opco_fee | Funding | F147 | 0.0e+00 | yes |
| su.A1.holdco_oid | Funding | F148 | 1.1e-15 | yes |
| su.A1.uses | Funding | F149 | 4.0e-13 | yes |
| su.A1.equity | Funding | F150 | 4.3e-14 | yes |
| su.A2.fee | Funding | F151 | 1.1e-16 | yes |
| su.A2.uses | Funding | F152 | 4.3e-14 | yes |
| su.A2.equity | Funding | F153 | 3.6e-15 | yes |
| su.A3.r8_deposit | Funding | F154 | 3.6e-15 | yes |
| su.A3.oid | Funding | F155 | 3.3e-16 | yes |
| su.A3.itc7_proceeds | Funding | F156 | 0.0e+00 | yes |
| su.A3.itc8_proceeds | Funding | F157 | 3.6e-15 | yes |
| su.A3.eq_signing | Funding | F159 | 0.0e+00 | yes |
| su.A3.carry | Funding | F160 | 1.4e-14 | yes |
| su.A3.eq_r7 | Funding | F162 | 0.0e+00 | yes |
| su.A3.carry2 | Funding | F163 | 4.9e-15 | yes |
| su.A3.eq_r8 | Funding | F165 | 4.3e-14 | yes |
| su.A3.cash_left_after_r8 | Funding | F166 | 0.0e+00 | yes |
| su.A3.uses | Funding | F167 | 1.4e-13 | yes |
| su.A3.equity | Funding | F168 | 4.3e-14 | yes |
| refi.mtm_opco_receivable | Funding | F174 | 4.4e-15 | yes |
| refi.mtm_redfern_payable | Funding | F175 | 4.4e-16 | yes |
| refi.costs | Funding | F176 | 4.0e-15 | yes |
| refi.tl_repay | Funding | F177 | 2.8e-13 | yes |
| refi.rf_repay | Funding | F178 | 5.0e-14 | yes |
| refi.opco_net | Funding | F179 | 8.5e-14 | yes |
| sc.tl_dscr_min_2022_2025 | Ratios | F15 | 2.7e-15 | yes |
| sc.tl_dscr_avg_2022_2025 | Ratios | F16 | 2.9e-15 | yes |
| sc.uspp_dscr_min_2026_2043 | Ratios | F17 | 4.2e-15 | yes |
| sc.uspp_dscr_avg_2026_2043 | Ratios | F18 | 3.6e-15 | yes |
| sc.rf_dscr_min | Ratios | F19 | 0.0e+00 | yes |
| sc.rf_dscr_avg | Ratios | F20 | 0.0e+00 | yes |
| sc.holdco_cov_min_2023_2031 | Ratios | F21 | 4.9e-15 | yes |
| sc.holdco_cov_avg_2023_2031 | Ratios | F22 | 5.3e-15 | yes |
| sc.fund_nav_2025 | Returns | F98 | 1.4e-14 | yes |
| sc.fund_contributions | Returns | F99 | 2.0e-13 | yes |
| sc.fund_distributions_life | Returns | F100 | 5.7e-13 | yes |
| sc.fund_distributions_to_2025 | Returns | F101 | 7.1e-14 | yes |
| sc.fund_moic_life_x | Returns | F102 | 1.3e-15 | yes |
| sc.fund_moic_2025_x | Returns | F103 | 4.0e-15 | yes |
| sc.fund_irr_life_pct | Returns | F150 | 1.4e-14 | yes |
| sc.fund_irr_2025_pct | Returns | F151 | 1.5e-14 | yes |

### sens_curtailment_p3

| Key | Sheet | Location | Max diff | Pass |
|---|---|---|---|---|
| portfolio.north_atc | Operations | row 52 | 0.0e+00 | yes |
| portfolio.west_atc | Operations | row 53 | 0.0e+00 | yes |
| portfolio.south_atc | Operations | row 54 | 0.0e+00 | yes |
| portfolio.houston_atc | Operations | row 55 | 0.0e+00 | yes |
| portfolio.batt_rate | Operations | row 56 | 0.0e+00 | yes |
| portfolio.cap_hub_west_wind | Operations | row 57 | 0.0e+00 | yes |
| portfolio.cap_hub_panhandle_wind | Operations | row 58 | 0.0e+00 | yes |
| portfolio.cap_hub_west_solar | Operations | row 59 | 0.0e+00 | yes |
| portfolio.cap_hub_south_solar | Operations | row 60 | 0.0e+00 | yes |
| portfolio.cap_hub_coastal_wind | Operations | row 61 | 0.0e+00 | yes |
| R1.op_frac | Operations | row 63 | 0.0e+00 | yes |
| R1.own_share | Operations | row 65 | 1.9e-11 | yes |
| R1.hub_atc | Operations | row 66 | 0.0e+00 | yes |
| R1.deg | Operations | row 68 | 5.0e-11 | yes |
| R1.curt | Operations | row 69 | 0.0e+00 | yes |
| R1.gen_full | Operations | row 70 | 4.4e-11 | yes |
| R1.gen | Operations | row 71 | 4.4e-11 | yes |
| R1.cap_hub | Operations | row 72 | 0.0e+00 | yes |
| R1.cap_node | Operations | row 73 | 0.0e+00 | yes |
| R1.node_price | Operations | row 74 | 0.0e+00 | yes |
| R1.con_frac | Operations | row 75 | 0.0e+00 | yes |
| R1.con_vol | Operations | row 76 | 0.0e+00 | yes |
| R1.settle | Operations | row 77 | 2.0e-15 | yes |
| R1.mkt_gen | Operations | row 78 | 4.4e-11 | yes |
| R1.rev_contracted | Operations | row 79 | 0.0e+00 | yes |
| R1.rev_hedged | Operations | row 80 | 0.0e+00 | yes |
| R1.mkt_rev | Operations | row 81 | 5.0e-11 | yes |
| R1.revenue | Operations | row 82 | 5.0e-11 | yes |
| R1.rev_merchant | Operations | row 83 | 5.0e-11 | yes |
| R1.opex | Operations | row 84 | 4.9e-11 | yes |
| R1.land | Operations | row 85 | 4.9e-11 | yes |
| R1.bond | Operations | row 86 | 4.8e-11 | yes |
| R1.margin_tax | Operations | row 87 | 4.3e-11 | yes |
| R1.ebitda | Operations | row 88 | 4.8e-11 | yes |
| R1.aug | Operations | row 89 | 0.0e+00 | yes |
| R1.decom | Operations | row 90 | 3.3e-11 | yes |
| R1.cf | Operations | row 91 | 4.8e-11 | yes |
| R1.te_cash | Operations | row 92 | 0.0e+00 | yes |
| R1.mesa_tax_share | Operations | row 93 | 0.0e+00 | yes |
| R1.mesa_cf | Operations | row 94 | 4.8e-11 | yes |
| R1.mesa_taxable | Operations | row 95 | 4.8e-11 | yes |
| R1.s_contracted | Operations | row 97 | 0.0e+00 | yes |
| R1.s_hedged | Operations | row 98 | 4.8e-11 | yes |
| R1.s_merchant | Operations | row 99 | 4.8e-11 | yes |
| R1.mesa_rev | Operations | row 103 | 5.0e-11 | yes |
| R2.op_frac | Operations | row 105 | 4.1e-11 | yes |
| R2.own_share | Operations | row 107 | 1.9e-11 | yes |
| R2.hub_atc | Operations | row 108 | 0.0e+00 | yes |
| R2.deg | Operations | row 110 | 5.0e-11 | yes |
| R2.curt | Operations | row 111 | 0.0e+00 | yes |
| R2.gen_full | Operations | row 112 | 4.8e-11 | yes |
| R2.gen | Operations | row 113 | 4.8e-11 | yes |
| R2.cap_hub | Operations | row 114 | 0.0e+00 | yes |
| R2.cap_node | Operations | row 115 | 0.0e+00 | yes |
| R2.node_price | Operations | row 116 | 0.0e+00 | yes |
| R2.con_frac | Operations | row 117 | 4.1e-11 | yes |
| R2.con_vol | Operations | row 118 | 2.2e-11 | yes |
| R2.settle | Operations | row 119 | 4.8e-11 | yes |
| R2.mkt_gen | Operations | row 120 | 4.8e-11 | yes |
| R2.rev_contracted | Operations | row 121 | 4.8e-11 | yes |
| R2.rev_hedged | Operations | row 122 | 0.0e+00 | yes |
| R2.mkt_rev | Operations | row 123 | 4.7e-11 | yes |
| R2.revenue | Operations | row 124 | 4.8e-11 | yes |
| R2.rev_merchant | Operations | row 125 | 4.7e-11 | yes |
| R2.opex | Operations | row 126 | 4.7e-11 | yes |
| R2.land | Operations | row 127 | 5.0e-11 | yes |
| R2.bond | Operations | row 128 | 4.7e-11 | yes |
| R2.margin_tax | Operations | row 129 | 5.0e-11 | yes |
| R2.ebitda | Operations | row 130 | 5.0e-11 | yes |
| R2.aug | Operations | row 131 | 0.0e+00 | yes |
| R2.decom | Operations | row 132 | 4.0e-11 | yes |
| R2.cf | Operations | row 133 | 5.0e-11 | yes |
| R2.te_cash | Operations | row 134 | 0.0e+00 | yes |
| R2.mesa_tax_share | Operations | row 135 | 0.0e+00 | yes |
| R2.mesa_cf | Operations | row 136 | 5.0e-11 | yes |
| R2.mesa_taxable | Operations | row 137 | 5.0e-11 | yes |
| R2.s_contracted | Operations | row 139 | 4.2e-11 | yes |
| R2.s_hedged | Operations | row 140 | 0.0e+00 | yes |
| R2.s_merchant | Operations | row 141 | 4.2e-11 | yes |
| R2.mesa_rev | Operations | row 145 | 4.8e-11 | yes |
| R3.op_frac | Operations | row 147 | 4.9e-11 | yes |
| R3.own_share | Operations | row 149 | 1.9e-11 | yes |
| R3.hub_atc | Operations | row 150 | 0.0e+00 | yes |
| R3.deg | Operations | row 152 | 5.0e-11 | yes |
| R3.curt | Operations | row 153 | 0.0e+00 | yes |
| R3.gen_full | Operations | row 154 | 5.0e-11 | yes |
| R3.gen | Operations | row 155 | 4.7e-11 | yes |
| R3.cap_hub | Operations | row 156 | 0.0e+00 | yes |
| R3.cap_node | Operations | row 157 | 0.0e+00 | yes |
| R3.node_price | Operations | row 158 | 0.0e+00 | yes |
| R3.con_frac | Operations | row 159 | 0.0e+00 | yes |
| R3.con_vol | Operations | row 160 | 4.3e-11 | yes |
| R3.settle | Operations | row 161 | 3.1e-11 | yes |
| R3.mkt_gen | Operations | row 162 | 4.7e-11 | yes |
| R3.rev_contracted | Operations | row 163 | 0.0e+00 | yes |
| R3.rev_hedged | Operations | row 164 | 0.0e+00 | yes |
| R3.mkt_rev | Operations | row 165 | 4.3e-11 | yes |
| R3.revenue | Operations | row 166 | 4.3e-11 | yes |
| R3.rev_merchant | Operations | row 167 | 4.3e-11 | yes |
| R3.opex | Operations | row 168 | 5.0e-11 | yes |
| R3.land | Operations | row 169 | 4.7e-11 | yes |
| R3.bond | Operations | row 170 | 4.8e-11 | yes |
| R3.margin_tax | Operations | row 171 | 5.0e-11 | yes |
| R3.ebitda | Operations | row 172 | 4.9e-11 | yes |
| R3.aug | Operations | row 173 | 0.0e+00 | yes |
| R3.decom | Operations | row 174 | 8.9e-12 | yes |
| R3.cf | Operations | row 175 | 4.9e-11 | yes |
| R3.te_cash | Operations | row 177 | 0.0e+00 | yes |
| R3.mesa_tax_share | Operations | row 178 | 0.0e+00 | yes |
| R3.mesa_cf | Operations | row 179 | 4.3e-11 | yes |
| R3.mesa_taxable | Operations | row 180 | 4.4e-11 | yes |
| R3.s_contracted | Operations | row 182 | 4.8e-11 | yes |
| R3.s_hedged | Operations | row 183 | 0.0e+00 | yes |
| R3.s_merchant | Operations | row 184 | 4.8e-11 | yes |
| R3.mesa_rev | Operations | row 188 | 4.8e-11 | yes |
| R3.ptc_total | Operations | row 189 | 4.7e-11 | yes |
| R4.op_frac | Operations | row 191 | 2.9e-11 | yes |
| R4.own_share | Operations | row 193 | 1.9e-11 | yes |
| R4.hub_atc | Operations | row 194 | 0.0e+00 | yes |
| R4.deg | Operations | row 196 | 5.0e-11 | yes |
| R4.curt | Operations | row 197 | 0.0e+00 | yes |
| R4.gen_full | Operations | row 198 | 5.0e-11 | yes |
| R4.gen | Operations | row 199 | 5.0e-11 | yes |
| R4.cap_hub | Operations | row 200 | 0.0e+00 | yes |
| R4.cap_node | Operations | row 201 | 0.0e+00 | yes |
| R4.node_price | Operations | row 202 | 0.0e+00 | yes |
| R4.con_frac | Operations | row 203 | 0.0e+00 | yes |
| R4.con_vol | Operations | row 204 | 0.0e+00 | yes |
| R4.settle | Operations | row 205 | 1.0e-15 | yes |
| R4.mkt_gen | Operations | row 206 | 5.0e-11 | yes |
| R4.rev_contracted | Operations | row 207 | 0.0e+00 | yes |
| R4.rev_hedged | Operations | row 208 | 0.0e+00 | yes |
| R4.mkt_rev | Operations | row 209 | 4.8e-11 | yes |
| R4.revenue | Operations | row 210 | 4.8e-11 | yes |
| R4.rev_merchant | Operations | row 211 | 4.8e-11 | yes |
| R4.opex | Operations | row 212 | 5.0e-11 | yes |
| R4.land | Operations | row 213 | 0.0e+00 | yes |
| R4.bond | Operations | row 214 | 5.0e-11 | yes |
| R4.margin_tax | Operations | row 215 | 5.0e-11 | yes |
| R4.ebitda | Operations | row 216 | 4.9e-11 | yes |
| R4.aug | Operations | row 217 | 0.0e+00 | yes |
| R4.decom | Operations | row 218 | 1.9e-11 | yes |
| R4.cf | Operations | row 219 | 4.9e-11 | yes |
| R4.te_cash | Operations | row 220 | 0.0e+00 | yes |
| R4.mesa_tax_share | Operations | row 221 | 0.0e+00 | yes |
| R4.mesa_cf | Operations | row 222 | 4.9e-11 | yes |
| R4.mesa_taxable | Operations | row 223 | 4.9e-11 | yes |
| R4.s_contracted | Operations | row 225 | 0.0e+00 | yes |
| R4.s_hedged | Operations | row 226 | 4.1e-11 | yes |
| R4.s_merchant | Operations | row 227 | 4.1e-11 | yes |
| R4.mesa_rev | Operations | row 231 | 4.8e-11 | yes |
| R5.op_frac | Operations | row 233 | 3.7e-11 | yes |
| R5.own_share | Operations | row 235 | 1.9e-11 | yes |
| R5.hub_atc | Operations | row 236 | 0.0e+00 | yes |
| R5.deg | Operations | row 238 | 5.0e-11 | yes |
| R5.curt | Operations | row 239 | 0.0e+00 | yes |
| R5.gen_full | Operations | row 240 | 4.7e-11 | yes |
| R5.gen | Operations | row 241 | 4.7e-11 | yes |
| R5.cap_hub | Operations | row 242 | 0.0e+00 | yes |
| R5.cap_node | Operations | row 243 | 0.0e+00 | yes |
| R5.node_price | Operations | row 244 | 0.0e+00 | yes |
| R5.con_frac | Operations | row 245 | 4.1e-11 | yes |
| R5.con_vol | Operations | row 246 | 4.7e-11 | yes |
| R5.settle | Operations | row 247 | 4.3e-11 | yes |
| R5.mkt_gen | Operations | row 248 | 4.7e-11 | yes |
| R5.rev_contracted | Operations | row 249 | 4.5e-11 | yes |
| R5.rev_hedged | Operations | row 250 | 0.0e+00 | yes |
| R5.mkt_rev | Operations | row 251 | 4.8e-11 | yes |
| R5.revenue | Operations | row 252 | 4.8e-11 | yes |
| R5.rev_merchant | Operations | row 253 | 4.9e-11 | yes |
| R5.opex | Operations | row 254 | 4.9e-11 | yes |
| R5.land | Operations | row 255 | 0.0e+00 | yes |
| R5.bond | Operations | row 256 | 4.9e-11 | yes |
| R5.margin_tax | Operations | row 257 | 4.8e-11 | yes |
| R5.ebitda | Operations | row 258 | 4.9e-11 | yes |
| R5.aug | Operations | row 259 | 0.0e+00 | yes |
| R5.decom | Operations | row 260 | 2.0e-13 | yes |
| R5.cf | Operations | row 261 | 4.9e-11 | yes |
| R5.te_cash | Operations | row 263 | 4.4e-11 | yes |
| R5.mesa_tax_share | Operations | row 264 | 1.4e-12 | yes |
| R5.mesa_cf | Operations | row 265 | 4.9e-11 | yes |
| R5.mesa_taxable | Operations | row 266 | 4.9e-11 | yes |
| R5.s_contracted | Operations | row 268 | 4.5e-11 | yes |
| R5.s_hedged | Operations | row 269 | 0.0e+00 | yes |
| R5.s_merchant | Operations | row 270 | 4.5e-11 | yes |
| R5.mesa_rev | Operations | row 274 | 4.8e-11 | yes |
| R6.op_frac | Operations | row 276 | 4.2e-11 | yes |
| R6.own_share | Operations | row 278 | 2.4e-11 | yes |
| R6.hub_atc | Operations | row 279 | 0.0e+00 | yes |
| R6.con_frac | Operations | row 280 | 4.2e-11 | yes |
| R6.settle | Operations | row 281 | 4.0e-11 | yes |
| R6.stor_rev | Operations | row 282 | 3.2e-11 | yes |
| R6.rev_contracted | Operations | row 283 | 4.0e-11 | yes |
| R6.rev_hedged | Operations | row 284 | 0.0e+00 | yes |
| R6.revenue | Operations | row 285 | 4.0e-11 | yes |
| R6.rev_merchant | Operations | row 286 | 3.2e-11 | yes |
| R6.opex | Operations | row 287 | 4.9e-11 | yes |
| R6.land | Operations | row 288 | 0.0e+00 | yes |
| R6.bond | Operations | row 289 | 4.8e-11 | yes |
| R6.margin_tax | Operations | row 290 | 5.0e-11 | yes |
| R6.ebitda | Operations | row 291 | 5.0e-11 | yes |
| R6.aug | Operations | row 292 | 4.8e-12 | yes |
| R6.decom | Operations | row 293 | 2.5e-11 | yes |
| R6.cf | Operations | row 294 | 5.0e-11 | yes |
| R6.te_cash | Operations | row 295 | 0.0e+00 | yes |
| R6.mesa_tax_share | Operations | row 296 | 0.0e+00 | yes |
| R6.mesa_cf | Operations | row 297 | 5.0e-11 | yes |
| R6.mesa_taxable | Operations | row 298 | 5.0e-11 | yes |
| R6.s_contracted | Operations | row 300 | 3.8e-11 | yes |
| R6.s_hedged | Operations | row 301 | 0.0e+00 | yes |
| R6.s_merchant | Operations | row 302 | 3.8e-11 | yes |
| R6.mesa_rev | Operations | row 306 | 4.0e-11 | yes |
| R7.op_frac | Operations | row 308 | 4.4e-11 | yes |
| R7.own_share | Operations | row 310 | 0.0e+00 | yes |
| R7.hub_atc | Operations | row 311 | 0.0e+00 | yes |
| R7.con_frac | Operations | row 312 | 4.4e-11 | yes |
| R7.settle | Operations | row 314 | 3.6e-11 | yes |
| R7.stor_rev | Operations | row 315 | 4.6e-11 | yes |
| R7.rev_contracted | Operations | row 316 | 3.6e-11 | yes |
| R7.rev_hedged | Operations | row 317 | 0.0e+00 | yes |
| R7.revenue | Operations | row 318 | 4.6e-11 | yes |
| R7.rev_merchant | Operations | row 319 | 4.6e-11 | yes |
| R7.opex | Operations | row 320 | 5.0e-11 | yes |
| R7.land | Operations | row 321 | 0.0e+00 | yes |
| R7.bond | Operations | row 322 | 4.8e-11 | yes |
| R7.margin_tax | Operations | row 323 | 5.0e-11 | yes |
| R7.ebitda | Operations | row 324 | 5.0e-11 | yes |
| R7.aug | Operations | row 325 | 3.8e-11 | yes |
| R7.decom | Operations | row 326 | 2.3e-11 | yes |
| R7.cf | Operations | row 327 | 5.0e-11 | yes |
| R7.te_cash | Operations | row 328 | 0.0e+00 | yes |
| R7.mesa_tax_share | Operations | row 329 | 0.0e+00 | yes |
| R7.mesa_cf | Operations | row 330 | 5.0e-11 | yes |
| R7.mesa_taxable | Operations | row 331 | 5.0e-11 | yes |
| R7.s_contracted | Operations | row 333 | 3.1e-11 | yes |
| R7.s_hedged | Operations | row 334 | 0.0e+00 | yes |
| R7.s_merchant | Operations | row 335 | 3.1e-11 | yes |
| R7.mesa_rev | Operations | row 339 | 4.6e-11 | yes |
| R8.op_frac | Operations | row 341 | 4.6e-11 | yes |
| R8.own_share | Operations | row 343 | 0.0e+00 | yes |
| R8.hub_atc | Operations | row 344 | 0.0e+00 | yes |
| R8.deg | Operations | row 346 | 4.7e-11 | yes |
| R8.curt | Operations | row 347 | 0.0e+00 | yes |
| R8.gen_full | Operations | row 348 | 5.0e-11 | yes |
| R8.gen | Operations | row 349 | 5.0e-11 | yes |
| R8.cap_hub | Operations | row 350 | 0.0e+00 | yes |
| R8.cap_node | Operations | row 351 | 0.0e+00 | yes |
| R8.node_price | Operations | row 352 | 0.0e+00 | yes |
| R8.con_frac | Operations | row 353 | 0.0e+00 | yes |
| R8.con_vol | Operations | row 354 | 0.0e+00 | yes |
| R8.settle | Operations | row 355 | 4.8e-11 | yes |
| R8.mkt_gen | Operations | row 356 | 5.0e-11 | yes |
| R8.rev_contracted | Operations | row 357 | 0.0e+00 | yes |
| R8.rev_hedged | Operations | row 358 | 0.0e+00 | yes |
| R8.mkt_rev | Operations | row 359 | 5.0e-11 | yes |
| R8.revenue | Operations | row 360 | 5.0e-11 | yes |
| R8.rev_merchant | Operations | row 361 | 5.0e-11 | yes |
| R8.opex | Operations | row 362 | 5.0e-11 | yes |
| R8.land | Operations | row 363 | 0.0e+00 | yes |
| R8.bond | Operations | row 364 | 4.8e-11 | yes |
| R8.margin_tax | Operations | row 365 | 4.9e-11 | yes |
| R8.ebitda | Operations | row 366 | 4.7e-11 | yes |
| R8.aug | Operations | row 367 | 0.0e+00 | yes |
| R8.decom | Operations | row 368 | 3.5e-11 | yes |
| R8.cf | Operations | row 369 | 4.7e-11 | yes |
| R8.te_cash | Operations | row 370 | 0.0e+00 | yes |
| R8.mesa_tax_share | Operations | row 371 | 0.0e+00 | yes |
| R8.mesa_cf | Operations | row 372 | 4.7e-11 | yes |
| R8.mesa_taxable | Operations | row 373 | 4.7e-11 | yes |
| R8.s_contracted | Operations | row 375 | 0.0e+00 | yes |
| R8.s_hedged | Operations | row 376 | 3.8e-11 | yes |
| R8.s_merchant | Operations | row 377 | 3.8e-11 | yes |
| R8.mesa_rev | Operations | row 381 | 5.0e-11 | yes |
| portfolio.am_cost | Operations | row 384 | 5.0e-11 | yes |
| portfolio.mesa_rev_contracted_a1 | Operations | row 386 | 5.0e-11 | yes |
| portfolio.mesa_rev_hedged_a1 | Operations | row 387 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_a1 | Operations | row 388 | 4.7e-11 | yes |
| portfolio.mesa_rev_a1 | Operations | row 389 | 4.7e-11 | yes |
| portfolio.mesa_rev_contracted_all | Operations | row 391 | 5.0e-11 | yes |
| portfolio.mesa_rev_hedged_all | Operations | row 392 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_all | Operations | row 393 | 4.8e-11 | yes |
| portfolio.mesa_rev_all | Operations | row 394 | 4.5e-11 | yes |
| portfolio.cfads_a1 | Operations | row 400 | 5.0e-11 | yes |
| portfolio.cfads_all | Operations | row 401 | 4.7e-11 | yes |
| portfolio.cfads_a3 | Operations | row 402 | 4.9e-11 | yes |
| portfolio.share_contracted_a1 | Operations | row 403 | 5.0e-11 | yes |
| portfolio.share_hedged_a1 | Operations | row 404 | 3.9e-11 | yes |
| portfolio.share_merchant_a1 | Operations | row 405 | 5.0e-11 | yes |
| portfolio.share_contracted_all | Operations | row 409 | 4.9e-11 | yes |
| portfolio.share_hedged_all | Operations | row 410 | 4.7e-11 | yes |
| portfolio.share_merchant_all | Operations | row 411 | 4.9e-11 | yes |
| finance.dep | Tax | row 24 | 0.0e+00 | yes |
| finance.taxable_ops | Tax | row 25 | 4.7e-11 | yes |
| finance.tl_open | Debt | row 14 | 4.8e-11 | yes |
| finance.tl_int | Debt | row 15 | 3.9e-11 | yes |
| finance.tl_prin | Debt | row 16 | 3.1e-11 | yes |
| finance.tl_prepay | Debt | row 17 | 2.6e-11 | yes |
| finance.tl_ds | Debt | row 18 | 4.9e-11 | yes |
| finance.rf_open | Debt | row 23 | 3.6e-11 | yes |
| finance.rf_int | Debt | row 24 | 4.4e-11 | yes |
| finance.rf_prin | Debt | row 25 | 4.4e-11 | yes |
| finance.rf_prepay | Debt | row 26 | 2.7e-11 | yes |
| finance.rf_ds | Debt | row 27 | 3.0e-11 | yes |
| finance.u_open | Debt | row 31 | 4.7e-11 | yes |
| finance.u_int | Debt | row 32 | 4.8e-11 | yes |
| finance.u_prin | Debt | row 33 | 4.9e-11 | yes |
| finance.u_ds | Debt | row 34 | 4.3e-11 | yes |
| finance.hc1_open | Debt | row 46 | 4.5e-11 | yes |
| finance.hc1_int | Debt | row 47 | 4.0e-11 | yes |
| finance.hc1_amort | Debt | row 48 | 1.4e-11 | yes |
| finance.hc1_sweep | Debt | row 49 | 4.8e-11 | yes |
| finance.hc1_repay | Debt | row 51 | 4.0e-11 | yes |
| finance.hc2_open | Debt | row 53 | 1.1e-11 | yes |
| finance.hc2_int | Debt | row 54 | 1.8e-11 | yes |
| finance.hc2_amort | Debt | row 55 | 3.9e-11 | yes |
| finance.hc2_sweep | Debt | row 56 | 1.2e-11 | yes |
| finance.hc2_repay | Debt | row 58 | 3.6e-11 | yes |
| finance.hc3_open | Debt | row 60 | 4.8e-11 | yes |
| finance.hc3_int | Debt | row 61 | 4.7e-11 | yes |
| finance.hc3_amort | Debt | row 62 | 3.2e-12 | yes |
| finance.hc3_sweep | Debt | row 63 | 4.9e-11 | yes |
| finance.hc_ds | Debt | row 67 | 5.0e-11 | yes |
| finance.taxable_income | Tax | row 29 | 4.9e-11 | yes |
| finance.nol_open | Tax | row 30 | 4.6e-11 | yes |
| finance.nol_used | Tax | row 31 | 4.8e-11 | yes |
| finance.tax | Tax | row 32 | 4.9e-11 | yes |
| finance.nol_close | Tax | row 33 | 4.6e-11 | yes |
| finance.opco_ds | Waterfall | row 9 | 4.9e-11 | yes |
| finance.opco_dist | Waterfall | row 10 | 4.7e-11 | yes |
| finance.recap_opco | Waterfall | row 11 | 3.6e-11 | yes |
| finance.hc_excess | Waterfall | row 16 | 5.0e-11 | yes |
| finance.fund_dist_ops | Waterfall | row 19 | 5.0e-11 | yes |
| finance.recap_hold | Waterfall | row 20 | 4.6e-11 | yes |
| finance.recap_total | Waterfall | row 21 | 1.8e-11 | yes |
| finance.fund_dist | Waterfall | row 22 | 5.0e-11 | yes |
| finance.dscr_tl | Ratios | row 8 | 3.3e-11 | yes |
| finance.dscr_rf | Ratios | row 9 | 0.0e+00 | yes |
| finance.dscr_u | Ratios | row 10 | 4.9e-11 | yes |
| finance.dscr_opco | Ratios | row 11 | 4.9e-11 | yes |
| finance.hc_cov | Ratios | row 12 | 4.3e-11 | yes |
| finance.nav_df | Returns | row 96 | 5.0e-11 | yes |
| su.A1.opco_fee | Funding | F147 | 0.0e+00 | yes |
| su.A1.holdco_oid | Funding | F148 | 1.1e-15 | yes |
| su.A1.uses | Funding | F149 | 4.0e-13 | yes |
| su.A1.equity | Funding | F150 | 4.3e-14 | yes |
| su.A2.fee | Funding | F151 | 1.1e-16 | yes |
| su.A2.uses | Funding | F152 | 4.3e-14 | yes |
| su.A2.equity | Funding | F153 | 3.6e-15 | yes |
| su.A3.r8_deposit | Funding | F154 | 3.6e-15 | yes |
| su.A3.oid | Funding | F155 | 3.3e-16 | yes |
| su.A3.itc7_proceeds | Funding | F156 | 0.0e+00 | yes |
| su.A3.itc8_proceeds | Funding | F157 | 3.6e-15 | yes |
| su.A3.eq_signing | Funding | F159 | 0.0e+00 | yes |
| su.A3.carry | Funding | F160 | 1.4e-14 | yes |
| su.A3.eq_r7 | Funding | F162 | 0.0e+00 | yes |
| su.A3.carry2 | Funding | F163 | 4.9e-15 | yes |
| su.A3.eq_r8 | Funding | F165 | 4.3e-14 | yes |
| su.A3.cash_left_after_r8 | Funding | F166 | 0.0e+00 | yes |
| su.A3.uses | Funding | F167 | 1.4e-13 | yes |
| su.A3.equity | Funding | F168 | 4.3e-14 | yes |
| refi.mtm_opco_receivable | Funding | F174 | 4.4e-15 | yes |
| refi.mtm_redfern_payable | Funding | F175 | 4.4e-16 | yes |
| refi.costs | Funding | F176 | 4.0e-15 | yes |
| refi.tl_repay | Funding | F177 | 2.8e-13 | yes |
| refi.rf_repay | Funding | F178 | 5.0e-14 | yes |
| refi.opco_net | Funding | F179 | 8.5e-14 | yes |
| sc.tl_dscr_min_2022_2025 | Ratios | F15 | 4.0e-15 | yes |
| sc.tl_dscr_avg_2022_2025 | Ratios | F16 | 3.8e-15 | yes |
| sc.uspp_dscr_min_2026_2043 | Ratios | F17 | 3.6e-15 | yes |
| sc.uspp_dscr_avg_2026_2043 | Ratios | F18 | 4.4e-16 | yes |
| sc.rf_dscr_min | Ratios | F19 | 0.0e+00 | yes |
| sc.rf_dscr_avg | Ratios | F20 | 0.0e+00 | yes |
| sc.holdco_cov_min_2023_2031 | Ratios | F21 | 6.7e-16 | yes |
| sc.holdco_cov_avg_2023_2031 | Ratios | F22 | 4.4e-16 | yes |
| sc.fund_nav_2025 | Returns | F98 | 1.4e-14 | yes |
| sc.fund_contributions | Returns | F99 | 2.0e-13 | yes |
| sc.fund_distributions_life | Returns | F100 | 2.3e-13 | yes |
| sc.fund_distributions_to_2025 | Returns | F101 | 2.6e-13 | yes |
| sc.fund_moic_life_x | Returns | F102 | 8.9e-16 | yes |
| sc.fund_moic_2025_x | Returns | F103 | 3.1e-15 | yes |
| sc.fund_irr_life_pct | Returns | F150 | 1.4e-14 | yes |
| sc.fund_irr_2025_pct | Returns | F151 | 2.0e-14 | yes |

### sens_opex_p10

| Key | Sheet | Location | Max diff | Pass |
|---|---|---|---|---|
| portfolio.north_atc | Operations | row 52 | 0.0e+00 | yes |
| portfolio.west_atc | Operations | row 53 | 0.0e+00 | yes |
| portfolio.south_atc | Operations | row 54 | 0.0e+00 | yes |
| portfolio.houston_atc | Operations | row 55 | 0.0e+00 | yes |
| portfolio.batt_rate | Operations | row 56 | 0.0e+00 | yes |
| portfolio.cap_hub_west_wind | Operations | row 57 | 0.0e+00 | yes |
| portfolio.cap_hub_panhandle_wind | Operations | row 58 | 0.0e+00 | yes |
| portfolio.cap_hub_west_solar | Operations | row 59 | 0.0e+00 | yes |
| portfolio.cap_hub_south_solar | Operations | row 60 | 0.0e+00 | yes |
| portfolio.cap_hub_coastal_wind | Operations | row 61 | 0.0e+00 | yes |
| R1.op_frac | Operations | row 63 | 0.0e+00 | yes |
| R1.own_share | Operations | row 65 | 1.9e-11 | yes |
| R1.hub_atc | Operations | row 66 | 0.0e+00 | yes |
| R1.deg | Operations | row 68 | 5.0e-11 | yes |
| R1.curt | Operations | row 69 | 0.0e+00 | yes |
| R1.gen_full | Operations | row 70 | 5.0e-11 | yes |
| R1.gen | Operations | row 71 | 4.8e-11 | yes |
| R1.cap_hub | Operations | row 72 | 0.0e+00 | yes |
| R1.cap_node | Operations | row 73 | 0.0e+00 | yes |
| R1.node_price | Operations | row 74 | 0.0e+00 | yes |
| R1.con_frac | Operations | row 75 | 0.0e+00 | yes |
| R1.con_vol | Operations | row 76 | 0.0e+00 | yes |
| R1.settle | Operations | row 77 | 2.0e-15 | yes |
| R1.mkt_gen | Operations | row 78 | 4.8e-11 | yes |
| R1.rev_contracted | Operations | row 79 | 0.0e+00 | yes |
| R1.rev_hedged | Operations | row 80 | 0.0e+00 | yes |
| R1.mkt_rev | Operations | row 81 | 4.9e-11 | yes |
| R1.revenue | Operations | row 82 | 4.9e-11 | yes |
| R1.rev_merchant | Operations | row 83 | 4.9e-11 | yes |
| R1.opex | Operations | row 84 | 4.7e-11 | yes |
| R1.land | Operations | row 85 | 5.0e-11 | yes |
| R1.bond | Operations | row 86 | 4.8e-11 | yes |
| R1.margin_tax | Operations | row 87 | 4.9e-11 | yes |
| R1.ebitda | Operations | row 88 | 4.6e-11 | yes |
| R1.aug | Operations | row 89 | 0.0e+00 | yes |
| R1.decom | Operations | row 90 | 3.3e-11 | yes |
| R1.cf | Operations | row 91 | 4.6e-11 | yes |
| R1.te_cash | Operations | row 92 | 0.0e+00 | yes |
| R1.mesa_tax_share | Operations | row 93 | 0.0e+00 | yes |
| R1.mesa_cf | Operations | row 94 | 4.6e-11 | yes |
| R1.mesa_taxable | Operations | row 95 | 4.6e-11 | yes |
| R1.s_contracted | Operations | row 97 | 0.0e+00 | yes |
| R1.s_hedged | Operations | row 98 | 2.8e-11 | yes |
| R1.s_merchant | Operations | row 99 | 2.8e-11 | yes |
| R1.mesa_rev | Operations | row 103 | 4.9e-11 | yes |
| R2.op_frac | Operations | row 105 | 4.1e-11 | yes |
| R2.own_share | Operations | row 107 | 1.9e-11 | yes |
| R2.hub_atc | Operations | row 108 | 0.0e+00 | yes |
| R2.deg | Operations | row 110 | 5.0e-11 | yes |
| R2.curt | Operations | row 111 | 0.0e+00 | yes |
| R2.gen_full | Operations | row 112 | 5.0e-11 | yes |
| R2.gen | Operations | row 113 | 5.0e-11 | yes |
| R2.cap_hub | Operations | row 114 | 0.0e+00 | yes |
| R2.cap_node | Operations | row 115 | 0.0e+00 | yes |
| R2.node_price | Operations | row 116 | 0.0e+00 | yes |
| R2.con_frac | Operations | row 117 | 4.1e-11 | yes |
| R2.con_vol | Operations | row 118 | 4.4e-11 | yes |
| R2.settle | Operations | row 119 | 4.5e-11 | yes |
| R2.mkt_gen | Operations | row 120 | 5.0e-11 | yes |
| R2.rev_contracted | Operations | row 121 | 4.5e-11 | yes |
| R2.rev_hedged | Operations | row 122 | 0.0e+00 | yes |
| R2.mkt_rev | Operations | row 123 | 4.8e-11 | yes |
| R2.revenue | Operations | row 124 | 5.0e-11 | yes |
| R2.rev_merchant | Operations | row 125 | 4.8e-11 | yes |
| R2.opex | Operations | row 126 | 4.8e-11 | yes |
| R2.land | Operations | row 127 | 5.0e-11 | yes |
| R2.bond | Operations | row 128 | 4.7e-11 | yes |
| R2.margin_tax | Operations | row 129 | 5.0e-11 | yes |
| R2.ebitda | Operations | row 130 | 4.9e-11 | yes |
| R2.aug | Operations | row 131 | 0.0e+00 | yes |
| R2.decom | Operations | row 132 | 4.0e-11 | yes |
| R2.cf | Operations | row 133 | 4.9e-11 | yes |
| R2.te_cash | Operations | row 134 | 0.0e+00 | yes |
| R2.mesa_tax_share | Operations | row 135 | 0.0e+00 | yes |
| R2.mesa_cf | Operations | row 136 | 4.9e-11 | yes |
| R2.mesa_taxable | Operations | row 137 | 4.9e-11 | yes |
| R2.s_contracted | Operations | row 139 | 4.2e-11 | yes |
| R2.s_hedged | Operations | row 140 | 0.0e+00 | yes |
| R2.s_merchant | Operations | row 141 | 4.2e-11 | yes |
| R2.mesa_rev | Operations | row 145 | 5.0e-11 | yes |
| R3.op_frac | Operations | row 147 | 4.9e-11 | yes |
| R3.own_share | Operations | row 149 | 1.9e-11 | yes |
| R3.hub_atc | Operations | row 150 | 0.0e+00 | yes |
| R3.deg | Operations | row 152 | 5.0e-11 | yes |
| R3.curt | Operations | row 153 | 0.0e+00 | yes |
| R3.gen_full | Operations | row 154 | 5.0e-11 | yes |
| R3.gen | Operations | row 155 | 5.0e-11 | yes |
| R3.cap_hub | Operations | row 156 | 0.0e+00 | yes |
| R3.cap_node | Operations | row 157 | 0.0e+00 | yes |
| R3.node_price | Operations | row 158 | 0.0e+00 | yes |
| R3.con_frac | Operations | row 159 | 0.0e+00 | yes |
| R3.con_vol | Operations | row 160 | 4.8e-11 | yes |
| R3.settle | Operations | row 161 | 5.0e-11 | yes |
| R3.mkt_gen | Operations | row 162 | 5.0e-11 | yes |
| R3.rev_contracted | Operations | row 163 | 0.0e+00 | yes |
| R3.rev_hedged | Operations | row 164 | 0.0e+00 | yes |
| R3.mkt_rev | Operations | row 165 | 5.0e-11 | yes |
| R3.revenue | Operations | row 166 | 5.0e-11 | yes |
| R3.rev_merchant | Operations | row 167 | 5.0e-11 | yes |
| R3.opex | Operations | row 168 | 4.8e-11 | yes |
| R3.land | Operations | row 169 | 5.0e-11 | yes |
| R3.bond | Operations | row 170 | 4.8e-11 | yes |
| R3.margin_tax | Operations | row 171 | 4.5e-11 | yes |
| R3.ebitda | Operations | row 172 | 4.9e-11 | yes |
| R3.aug | Operations | row 173 | 0.0e+00 | yes |
| R3.decom | Operations | row 174 | 8.9e-12 | yes |
| R3.cf | Operations | row 175 | 4.9e-11 | yes |
| R3.te_cash | Operations | row 177 | 0.0e+00 | yes |
| R3.mesa_tax_share | Operations | row 178 | 0.0e+00 | yes |
| R3.mesa_cf | Operations | row 179 | 5.0e-11 | yes |
| R3.mesa_taxable | Operations | row 180 | 4.5e-11 | yes |
| R3.s_contracted | Operations | row 182 | 4.5e-11 | yes |
| R3.s_hedged | Operations | row 183 | 0.0e+00 | yes |
| R3.s_merchant | Operations | row 184 | 4.5e-11 | yes |
| R3.mesa_rev | Operations | row 188 | 5.0e-11 | yes |
| R3.ptc_total | Operations | row 189 | 4.5e-11 | yes |
| R4.op_frac | Operations | row 191 | 2.9e-11 | yes |
| R4.own_share | Operations | row 193 | 1.9e-11 | yes |
| R4.hub_atc | Operations | row 194 | 0.0e+00 | yes |
| R4.deg | Operations | row 196 | 5.0e-11 | yes |
| R4.curt | Operations | row 197 | 0.0e+00 | yes |
| R4.gen_full | Operations | row 198 | 5.0e-11 | yes |
| R4.gen | Operations | row 199 | 5.0e-11 | yes |
| R4.cap_hub | Operations | row 200 | 0.0e+00 | yes |
| R4.cap_node | Operations | row 201 | 0.0e+00 | yes |
| R4.node_price | Operations | row 202 | 0.0e+00 | yes |
| R4.con_frac | Operations | row 203 | 0.0e+00 | yes |
| R4.con_vol | Operations | row 204 | 0.0e+00 | yes |
| R4.settle | Operations | row 205 | 1.0e-15 | yes |
| R4.mkt_gen | Operations | row 206 | 5.0e-11 | yes |
| R4.rev_contracted | Operations | row 207 | 0.0e+00 | yes |
| R4.rev_hedged | Operations | row 208 | 0.0e+00 | yes |
| R4.mkt_rev | Operations | row 209 | 4.9e-11 | yes |
| R4.revenue | Operations | row 210 | 4.9e-11 | yes |
| R4.rev_merchant | Operations | row 211 | 4.9e-11 | yes |
| R4.opex | Operations | row 212 | 5.0e-11 | yes |
| R4.land | Operations | row 213 | 0.0e+00 | yes |
| R4.bond | Operations | row 214 | 5.0e-11 | yes |
| R4.margin_tax | Operations | row 215 | 5.0e-11 | yes |
| R4.ebitda | Operations | row 216 | 5.0e-11 | yes |
| R4.aug | Operations | row 217 | 0.0e+00 | yes |
| R4.decom | Operations | row 218 | 1.9e-11 | yes |
| R4.cf | Operations | row 219 | 5.0e-11 | yes |
| R4.te_cash | Operations | row 220 | 0.0e+00 | yes |
| R4.mesa_tax_share | Operations | row 221 | 0.0e+00 | yes |
| R4.mesa_cf | Operations | row 222 | 5.0e-11 | yes |
| R4.mesa_taxable | Operations | row 223 | 5.0e-11 | yes |
| R4.s_contracted | Operations | row 225 | 0.0e+00 | yes |
| R4.s_hedged | Operations | row 226 | 4.6e-11 | yes |
| R4.s_merchant | Operations | row 227 | 4.6e-11 | yes |
| R4.mesa_rev | Operations | row 231 | 4.9e-11 | yes |
| R5.op_frac | Operations | row 233 | 3.7e-11 | yes |
| R5.own_share | Operations | row 235 | 1.9e-11 | yes |
| R5.hub_atc | Operations | row 236 | 0.0e+00 | yes |
| R5.deg | Operations | row 238 | 5.0e-11 | yes |
| R5.curt | Operations | row 239 | 0.0e+00 | yes |
| R5.gen_full | Operations | row 240 | 4.1e-11 | yes |
| R5.gen | Operations | row 241 | 4.9e-11 | yes |
| R5.cap_hub | Operations | row 242 | 0.0e+00 | yes |
| R5.cap_node | Operations | row 243 | 0.0e+00 | yes |
| R5.node_price | Operations | row 244 | 0.0e+00 | yes |
| R5.con_frac | Operations | row 245 | 4.1e-11 | yes |
| R5.con_vol | Operations | row 246 | 4.0e-11 | yes |
| R5.settle | Operations | row 247 | 4.8e-11 | yes |
| R5.mkt_gen | Operations | row 248 | 4.9e-11 | yes |
| R5.rev_contracted | Operations | row 249 | 4.0e-11 | yes |
| R5.rev_hedged | Operations | row 250 | 0.0e+00 | yes |
| R5.mkt_rev | Operations | row 251 | 4.9e-11 | yes |
| R5.revenue | Operations | row 252 | 4.9e-11 | yes |
| R5.rev_merchant | Operations | row 253 | 4.9e-11 | yes |
| R5.opex | Operations | row 254 | 5.0e-11 | yes |
| R5.land | Operations | row 255 | 0.0e+00 | yes |
| R5.bond | Operations | row 256 | 4.9e-11 | yes |
| R5.margin_tax | Operations | row 257 | 4.5e-11 | yes |
| R5.ebitda | Operations | row 258 | 4.8e-11 | yes |
| R5.aug | Operations | row 259 | 0.0e+00 | yes |
| R5.decom | Operations | row 260 | 2.0e-13 | yes |
| R5.cf | Operations | row 261 | 4.8e-11 | yes |
| R5.te_cash | Operations | row 263 | 4.4e-11 | yes |
| R5.mesa_tax_share | Operations | row 264 | 1.4e-12 | yes |
| R5.mesa_cf | Operations | row 265 | 5.0e-11 | yes |
| R5.mesa_taxable | Operations | row 266 | 5.0e-11 | yes |
| R5.s_contracted | Operations | row 268 | 4.5e-11 | yes |
| R5.s_hedged | Operations | row 269 | 0.0e+00 | yes |
| R5.s_merchant | Operations | row 270 | 4.5e-11 | yes |
| R5.mesa_rev | Operations | row 274 | 4.7e-11 | yes |
| R6.op_frac | Operations | row 276 | 4.2e-11 | yes |
| R6.own_share | Operations | row 278 | 2.4e-11 | yes |
| R6.hub_atc | Operations | row 279 | 0.0e+00 | yes |
| R6.con_frac | Operations | row 280 | 4.2e-11 | yes |
| R6.settle | Operations | row 281 | 4.0e-11 | yes |
| R6.stor_rev | Operations | row 282 | 3.2e-11 | yes |
| R6.rev_contracted | Operations | row 283 | 4.0e-11 | yes |
| R6.rev_hedged | Operations | row 284 | 0.0e+00 | yes |
| R6.revenue | Operations | row 285 | 4.0e-11 | yes |
| R6.rev_merchant | Operations | row 286 | 3.2e-11 | yes |
| R6.opex | Operations | row 287 | 5.0e-11 | yes |
| R6.land | Operations | row 288 | 0.0e+00 | yes |
| R6.bond | Operations | row 289 | 4.8e-11 | yes |
| R6.margin_tax | Operations | row 290 | 5.0e-11 | yes |
| R6.ebitda | Operations | row 291 | 5.0e-11 | yes |
| R6.aug | Operations | row 292 | 4.8e-12 | yes |
| R6.decom | Operations | row 293 | 2.5e-11 | yes |
| R6.cf | Operations | row 294 | 5.0e-11 | yes |
| R6.te_cash | Operations | row 295 | 0.0e+00 | yes |
| R6.mesa_tax_share | Operations | row 296 | 0.0e+00 | yes |
| R6.mesa_cf | Operations | row 297 | 5.0e-11 | yes |
| R6.mesa_taxable | Operations | row 298 | 5.0e-11 | yes |
| R6.s_contracted | Operations | row 300 | 3.8e-11 | yes |
| R6.s_hedged | Operations | row 301 | 0.0e+00 | yes |
| R6.s_merchant | Operations | row 302 | 3.8e-11 | yes |
| R6.mesa_rev | Operations | row 306 | 4.0e-11 | yes |
| R7.op_frac | Operations | row 308 | 4.4e-11 | yes |
| R7.own_share | Operations | row 310 | 0.0e+00 | yes |
| R7.hub_atc | Operations | row 311 | 0.0e+00 | yes |
| R7.con_frac | Operations | row 312 | 4.4e-11 | yes |
| R7.settle | Operations | row 314 | 3.6e-11 | yes |
| R7.stor_rev | Operations | row 315 | 4.6e-11 | yes |
| R7.rev_contracted | Operations | row 316 | 3.6e-11 | yes |
| R7.rev_hedged | Operations | row 317 | 0.0e+00 | yes |
| R7.revenue | Operations | row 318 | 4.6e-11 | yes |
| R7.rev_merchant | Operations | row 319 | 4.6e-11 | yes |
| R7.opex | Operations | row 320 | 4.6e-11 | yes |
| R7.land | Operations | row 321 | 0.0e+00 | yes |
| R7.bond | Operations | row 322 | 4.8e-11 | yes |
| R7.margin_tax | Operations | row 323 | 5.0e-11 | yes |
| R7.ebitda | Operations | row 324 | 4.7e-11 | yes |
| R7.aug | Operations | row 325 | 3.8e-11 | yes |
| R7.decom | Operations | row 326 | 2.3e-11 | yes |
| R7.cf | Operations | row 327 | 4.7e-11 | yes |
| R7.te_cash | Operations | row 328 | 0.0e+00 | yes |
| R7.mesa_tax_share | Operations | row 329 | 0.0e+00 | yes |
| R7.mesa_cf | Operations | row 330 | 4.7e-11 | yes |
| R7.mesa_taxable | Operations | row 331 | 4.7e-11 | yes |
| R7.s_contracted | Operations | row 333 | 3.1e-11 | yes |
| R7.s_hedged | Operations | row 334 | 0.0e+00 | yes |
| R7.s_merchant | Operations | row 335 | 3.1e-11 | yes |
| R7.mesa_rev | Operations | row 339 | 4.6e-11 | yes |
| R8.op_frac | Operations | row 341 | 4.6e-11 | yes |
| R8.own_share | Operations | row 343 | 0.0e+00 | yes |
| R8.hub_atc | Operations | row 344 | 0.0e+00 | yes |
| R8.deg | Operations | row 346 | 4.7e-11 | yes |
| R8.curt | Operations | row 347 | 0.0e+00 | yes |
| R8.gen_full | Operations | row 348 | 4.9e-11 | yes |
| R8.gen | Operations | row 349 | 4.9e-11 | yes |
| R8.cap_hub | Operations | row 350 | 0.0e+00 | yes |
| R8.cap_node | Operations | row 351 | 0.0e+00 | yes |
| R8.node_price | Operations | row 352 | 0.0e+00 | yes |
| R8.con_frac | Operations | row 353 | 0.0e+00 | yes |
| R8.con_vol | Operations | row 354 | 0.0e+00 | yes |
| R8.settle | Operations | row 355 | 4.8e-11 | yes |
| R8.mkt_gen | Operations | row 356 | 4.9e-11 | yes |
| R8.rev_contracted | Operations | row 357 | 0.0e+00 | yes |
| R8.rev_hedged | Operations | row 358 | 0.0e+00 | yes |
| R8.mkt_rev | Operations | row 359 | 4.9e-11 | yes |
| R8.revenue | Operations | row 360 | 4.9e-11 | yes |
| R8.rev_merchant | Operations | row 361 | 4.9e-11 | yes |
| R8.opex | Operations | row 362 | 5.0e-11 | yes |
| R8.land | Operations | row 363 | 0.0e+00 | yes |
| R8.bond | Operations | row 364 | 4.8e-11 | yes |
| R8.margin_tax | Operations | row 365 | 4.8e-11 | yes |
| R8.ebitda | Operations | row 366 | 4.9e-11 | yes |
| R8.aug | Operations | row 367 | 0.0e+00 | yes |
| R8.decom | Operations | row 368 | 3.5e-11 | yes |
| R8.cf | Operations | row 369 | 4.9e-11 | yes |
| R8.te_cash | Operations | row 370 | 0.0e+00 | yes |
| R8.mesa_tax_share | Operations | row 371 | 0.0e+00 | yes |
| R8.mesa_cf | Operations | row 372 | 4.9e-11 | yes |
| R8.mesa_taxable | Operations | row 373 | 4.9e-11 | yes |
| R8.s_contracted | Operations | row 375 | 0.0e+00 | yes |
| R8.s_hedged | Operations | row 376 | 3.6e-11 | yes |
| R8.s_merchant | Operations | row 377 | 3.6e-11 | yes |
| R8.mesa_rev | Operations | row 381 | 4.9e-11 | yes |
| portfolio.am_cost | Operations | row 384 | 5.0e-11 | yes |
| portfolio.mesa_rev_contracted_a1 | Operations | row 386 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_a1 | Operations | row 387 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_a1 | Operations | row 388 | 4.9e-11 | yes |
| portfolio.mesa_rev_a1 | Operations | row 389 | 4.9e-11 | yes |
| portfolio.mesa_rev_contracted_all | Operations | row 391 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_all | Operations | row 392 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_all | Operations | row 393 | 5.0e-11 | yes |
| portfolio.mesa_rev_all | Operations | row 394 | 5.0e-11 | yes |
| portfolio.cfads_a1 | Operations | row 400 | 4.9e-11 | yes |
| portfolio.cfads_all | Operations | row 401 | 4.6e-11 | yes |
| portfolio.cfads_a3 | Operations | row 402 | 4.8e-11 | yes |
| portfolio.share_contracted_a1 | Operations | row 403 | 4.7e-11 | yes |
| portfolio.share_hedged_a1 | Operations | row 404 | 4.5e-11 | yes |
| portfolio.share_merchant_a1 | Operations | row 405 | 4.8e-11 | yes |
| portfolio.share_contracted_all | Operations | row 409 | 4.7e-11 | yes |
| portfolio.share_hedged_all | Operations | row 410 | 4.7e-11 | yes |
| portfolio.share_merchant_all | Operations | row 411 | 3.9e-11 | yes |
| finance.dep | Tax | row 24 | 0.0e+00 | yes |
| finance.taxable_ops | Tax | row 25 | 4.6e-11 | yes |
| finance.tl_open | Debt | row 14 | 4.8e-11 | yes |
| finance.tl_int | Debt | row 15 | 3.9e-11 | yes |
| finance.tl_prin | Debt | row 16 | 3.1e-11 | yes |
| finance.tl_prepay | Debt | row 17 | 2.6e-11 | yes |
| finance.tl_ds | Debt | row 18 | 4.9e-11 | yes |
| finance.rf_open | Debt | row 23 | 3.6e-11 | yes |
| finance.rf_int | Debt | row 24 | 4.4e-11 | yes |
| finance.rf_prin | Debt | row 25 | 4.4e-11 | yes |
| finance.rf_prepay | Debt | row 26 | 2.7e-11 | yes |
| finance.rf_ds | Debt | row 27 | 3.0e-11 | yes |
| finance.u_open | Debt | row 31 | 4.7e-11 | yes |
| finance.u_int | Debt | row 32 | 4.8e-11 | yes |
| finance.u_prin | Debt | row 33 | 4.9e-11 | yes |
| finance.u_ds | Debt | row 34 | 4.3e-11 | yes |
| finance.hc1_open | Debt | row 46 | 4.4e-11 | yes |
| finance.hc1_int | Debt | row 47 | 4.0e-11 | yes |
| finance.hc1_amort | Debt | row 48 | 1.4e-11 | yes |
| finance.hc1_sweep | Debt | row 49 | 4.3e-11 | yes |
| finance.hc1_repay | Debt | row 51 | 4.2e-11 | yes |
| finance.hc2_open | Debt | row 53 | 4.6e-11 | yes |
| finance.hc2_int | Debt | row 54 | 4.4e-11 | yes |
| finance.hc2_amort | Debt | row 55 | 3.9e-11 | yes |
| finance.hc2_sweep | Debt | row 56 | 3.4e-11 | yes |
| finance.hc2_repay | Debt | row 58 | 4.4e-11 | yes |
| finance.hc3_open | Debt | row 60 | 4.6e-11 | yes |
| finance.hc3_int | Debt | row 61 | 4.1e-11 | yes |
| finance.hc3_amort | Debt | row 62 | 3.2e-12 | yes |
| finance.hc3_sweep | Debt | row 63 | 4.1e-11 | yes |
| finance.hc_ds | Debt | row 67 | 4.9e-11 | yes |
| finance.taxable_income | Tax | row 29 | 4.6e-11 | yes |
| finance.nol_open | Tax | row 30 | 4.7e-11 | yes |
| finance.nol_used | Tax | row 31 | 4.7e-11 | yes |
| finance.tax | Tax | row 32 | 4.8e-11 | yes |
| finance.nol_close | Tax | row 33 | 4.7e-11 | yes |
| finance.opco_ds | Waterfall | row 9 | 4.9e-11 | yes |
| finance.opco_dist | Waterfall | row 10 | 4.8e-11 | yes |
| finance.recap_opco | Waterfall | row 11 | 3.6e-11 | yes |
| finance.hc_excess | Waterfall | row 16 | 4.9e-11 | yes |
| finance.fund_dist_ops | Waterfall | row 19 | 4.9e-11 | yes |
| finance.recap_hold | Waterfall | row 20 | 8.7e-12 | yes |
| finance.recap_total | Waterfall | row 21 | 4.5e-11 | yes |
| finance.fund_dist | Waterfall | row 22 | 4.9e-11 | yes |
| finance.dscr_tl | Ratios | row 8 | 4.2e-11 | yes |
| finance.dscr_rf | Ratios | row 9 | 4.1e-11 | yes |
| finance.dscr_u | Ratios | row 10 | 4.4e-11 | yes |
| finance.dscr_opco | Ratios | row 11 | 4.4e-11 | yes |
| finance.hc_cov | Ratios | row 12 | 5.0e-11 | yes |
| finance.nav_df | Returns | row 96 | 5.0e-11 | yes |
| su.A1.opco_fee | Funding | F147 | 0.0e+00 | yes |
| su.A1.holdco_oid | Funding | F148 | 1.1e-15 | yes |
| su.A1.uses | Funding | F149 | 4.0e-13 | yes |
| su.A1.equity | Funding | F150 | 4.3e-14 | yes |
| su.A2.fee | Funding | F151 | 1.1e-16 | yes |
| su.A2.uses | Funding | F152 | 4.3e-14 | yes |
| su.A2.equity | Funding | F153 | 3.6e-15 | yes |
| su.A3.r8_deposit | Funding | F154 | 3.6e-15 | yes |
| su.A3.oid | Funding | F155 | 3.3e-16 | yes |
| su.A3.itc7_proceeds | Funding | F156 | 0.0e+00 | yes |
| su.A3.itc8_proceeds | Funding | F157 | 3.6e-15 | yes |
| su.A3.eq_signing | Funding | F159 | 0.0e+00 | yes |
| su.A3.carry | Funding | F160 | 1.4e-14 | yes |
| su.A3.eq_r7 | Funding | F162 | 0.0e+00 | yes |
| su.A3.carry2 | Funding | F163 | 4.9e-15 | yes |
| su.A3.eq_r8 | Funding | F165 | 4.3e-14 | yes |
| su.A3.cash_left_after_r8 | Funding | F166 | 0.0e+00 | yes |
| su.A3.uses | Funding | F167 | 1.4e-13 | yes |
| su.A3.equity | Funding | F168 | 4.3e-14 | yes |
| refi.mtm_opco_receivable | Funding | F174 | 4.4e-15 | yes |
| refi.mtm_redfern_payable | Funding | F175 | 4.4e-16 | yes |
| refi.costs | Funding | F176 | 4.0e-15 | yes |
| refi.tl_repay | Funding | F177 | 2.8e-13 | yes |
| refi.rf_repay | Funding | F178 | 5.0e-14 | yes |
| refi.opco_net | Funding | F179 | 8.5e-14 | yes |
| sc.tl_dscr_min_2022_2025 | Ratios | F15 | 4.2e-15 | yes |
| sc.tl_dscr_avg_2022_2025 | Ratios | F16 | 2.4e-15 | yes |
| sc.uspp_dscr_min_2026_2043 | Ratios | F17 | 2.4e-15 | yes |
| sc.uspp_dscr_avg_2026_2043 | Ratios | F18 | 4.4e-15 | yes |
| sc.rf_dscr_min | Ratios | F19 | 4.2e-15 | yes |
| sc.rf_dscr_avg | Ratios | F20 | 2.2e-15 | yes |
| sc.holdco_cov_min_2023_2031 | Ratios | F21 | 8.9e-16 | yes |
| sc.holdco_cov_avg_2023_2031 | Ratios | F22 | 1.1e-15 | yes |
| sc.fund_nav_2025 | Returns | F98 | 4.3e-14 | yes |
| sc.fund_contributions | Returns | F99 | 2.0e-13 | yes |
| sc.fund_distributions_life | Returns | F100 | 5.1e-13 | yes |
| sc.fund_distributions_to_2025 | Returns | F101 | 1.8e-13 | yes |
| sc.fund_moic_life_x | Returns | F102 | 6.2e-15 | yes |
| sc.fund_moic_2025_x | Returns | F103 | 2.7e-15 | yes |
| sc.fund_irr_life_pct | Returns | F150 | 1.2e-14 | yes |
| sc.fund_irr_2025_pct | Returns | F151 | 2.7e-14 | yes |

### sens_sofr_p100_unhedged

| Key | Sheet | Location | Max diff | Pass |
|---|---|---|---|---|
| portfolio.north_atc | Operations | row 52 | 0.0e+00 | yes |
| portfolio.west_atc | Operations | row 53 | 0.0e+00 | yes |
| portfolio.south_atc | Operations | row 54 | 0.0e+00 | yes |
| portfolio.houston_atc | Operations | row 55 | 0.0e+00 | yes |
| portfolio.batt_rate | Operations | row 56 | 0.0e+00 | yes |
| portfolio.cap_hub_west_wind | Operations | row 57 | 0.0e+00 | yes |
| portfolio.cap_hub_panhandle_wind | Operations | row 58 | 0.0e+00 | yes |
| portfolio.cap_hub_west_solar | Operations | row 59 | 0.0e+00 | yes |
| portfolio.cap_hub_south_solar | Operations | row 60 | 0.0e+00 | yes |
| portfolio.cap_hub_coastal_wind | Operations | row 61 | 0.0e+00 | yes |
| R1.op_frac | Operations | row 63 | 0.0e+00 | yes |
| R1.own_share | Operations | row 65 | 1.9e-11 | yes |
| R1.hub_atc | Operations | row 66 | 0.0e+00 | yes |
| R1.deg | Operations | row 68 | 5.0e-11 | yes |
| R1.curt | Operations | row 69 | 0.0e+00 | yes |
| R1.gen_full | Operations | row 70 | 5.0e-11 | yes |
| R1.gen | Operations | row 71 | 4.8e-11 | yes |
| R1.cap_hub | Operations | row 72 | 0.0e+00 | yes |
| R1.cap_node | Operations | row 73 | 0.0e+00 | yes |
| R1.node_price | Operations | row 74 | 0.0e+00 | yes |
| R1.con_frac | Operations | row 75 | 0.0e+00 | yes |
| R1.con_vol | Operations | row 76 | 0.0e+00 | yes |
| R1.settle | Operations | row 77 | 2.0e-15 | yes |
| R1.mkt_gen | Operations | row 78 | 4.8e-11 | yes |
| R1.rev_contracted | Operations | row 79 | 0.0e+00 | yes |
| R1.rev_hedged | Operations | row 80 | 0.0e+00 | yes |
| R1.mkt_rev | Operations | row 81 | 4.9e-11 | yes |
| R1.revenue | Operations | row 82 | 4.9e-11 | yes |
| R1.rev_merchant | Operations | row 83 | 4.9e-11 | yes |
| R1.opex | Operations | row 84 | 4.9e-11 | yes |
| R1.land | Operations | row 85 | 5.0e-11 | yes |
| R1.bond | Operations | row 86 | 4.8e-11 | yes |
| R1.margin_tax | Operations | row 87 | 4.9e-11 | yes |
| R1.ebitda | Operations | row 88 | 5.0e-11 | yes |
| R1.aug | Operations | row 89 | 0.0e+00 | yes |
| R1.decom | Operations | row 90 | 3.3e-11 | yes |
| R1.cf | Operations | row 91 | 5.0e-11 | yes |
| R1.te_cash | Operations | row 92 | 0.0e+00 | yes |
| R1.mesa_tax_share | Operations | row 93 | 0.0e+00 | yes |
| R1.mesa_cf | Operations | row 94 | 5.0e-11 | yes |
| R1.mesa_taxable | Operations | row 95 | 5.0e-11 | yes |
| R1.s_contracted | Operations | row 97 | 0.0e+00 | yes |
| R1.s_hedged | Operations | row 98 | 2.8e-11 | yes |
| R1.s_merchant | Operations | row 99 | 2.8e-11 | yes |
| R1.mesa_rev | Operations | row 103 | 4.9e-11 | yes |
| R2.op_frac | Operations | row 105 | 4.1e-11 | yes |
| R2.own_share | Operations | row 107 | 1.9e-11 | yes |
| R2.hub_atc | Operations | row 108 | 0.0e+00 | yes |
| R2.deg | Operations | row 110 | 5.0e-11 | yes |
| R2.curt | Operations | row 111 | 0.0e+00 | yes |
| R2.gen_full | Operations | row 112 | 5.0e-11 | yes |
| R2.gen | Operations | row 113 | 5.0e-11 | yes |
| R2.cap_hub | Operations | row 114 | 0.0e+00 | yes |
| R2.cap_node | Operations | row 115 | 0.0e+00 | yes |
| R2.node_price | Operations | row 116 | 0.0e+00 | yes |
| R2.con_frac | Operations | row 117 | 4.1e-11 | yes |
| R2.con_vol | Operations | row 118 | 4.4e-11 | yes |
| R2.settle | Operations | row 119 | 4.5e-11 | yes |
| R2.mkt_gen | Operations | row 120 | 5.0e-11 | yes |
| R2.rev_contracted | Operations | row 121 | 4.5e-11 | yes |
| R2.rev_hedged | Operations | row 122 | 0.0e+00 | yes |
| R2.mkt_rev | Operations | row 123 | 4.8e-11 | yes |
| R2.revenue | Operations | row 124 | 5.0e-11 | yes |
| R2.rev_merchant | Operations | row 125 | 4.8e-11 | yes |
| R2.opex | Operations | row 126 | 4.7e-11 | yes |
| R2.land | Operations | row 127 | 5.0e-11 | yes |
| R2.bond | Operations | row 128 | 4.7e-11 | yes |
| R2.margin_tax | Operations | row 129 | 5.0e-11 | yes |
| R2.ebitda | Operations | row 130 | 4.7e-11 | yes |
| R2.aug | Operations | row 131 | 0.0e+00 | yes |
| R2.decom | Operations | row 132 | 4.0e-11 | yes |
| R2.cf | Operations | row 133 | 4.7e-11 | yes |
| R2.te_cash | Operations | row 134 | 0.0e+00 | yes |
| R2.mesa_tax_share | Operations | row 135 | 0.0e+00 | yes |
| R2.mesa_cf | Operations | row 136 | 4.7e-11 | yes |
| R2.mesa_taxable | Operations | row 137 | 4.7e-11 | yes |
| R2.s_contracted | Operations | row 139 | 4.2e-11 | yes |
| R2.s_hedged | Operations | row 140 | 0.0e+00 | yes |
| R2.s_merchant | Operations | row 141 | 4.2e-11 | yes |
| R2.mesa_rev | Operations | row 145 | 5.0e-11 | yes |
| R3.op_frac | Operations | row 147 | 4.9e-11 | yes |
| R3.own_share | Operations | row 149 | 1.9e-11 | yes |
| R3.hub_atc | Operations | row 150 | 0.0e+00 | yes |
| R3.deg | Operations | row 152 | 5.0e-11 | yes |
| R3.curt | Operations | row 153 | 0.0e+00 | yes |
| R3.gen_full | Operations | row 154 | 5.0e-11 | yes |
| R3.gen | Operations | row 155 | 5.0e-11 | yes |
| R3.cap_hub | Operations | row 156 | 0.0e+00 | yes |
| R3.cap_node | Operations | row 157 | 0.0e+00 | yes |
| R3.node_price | Operations | row 158 | 0.0e+00 | yes |
| R3.con_frac | Operations | row 159 | 0.0e+00 | yes |
| R3.con_vol | Operations | row 160 | 4.8e-11 | yes |
| R3.settle | Operations | row 161 | 5.0e-11 | yes |
| R3.mkt_gen | Operations | row 162 | 5.0e-11 | yes |
| R3.rev_contracted | Operations | row 163 | 0.0e+00 | yes |
| R3.rev_hedged | Operations | row 164 | 0.0e+00 | yes |
| R3.mkt_rev | Operations | row 165 | 5.0e-11 | yes |
| R3.revenue | Operations | row 166 | 5.0e-11 | yes |
| R3.rev_merchant | Operations | row 167 | 5.0e-11 | yes |
| R3.opex | Operations | row 168 | 5.0e-11 | yes |
| R3.land | Operations | row 169 | 5.0e-11 | yes |
| R3.bond | Operations | row 170 | 4.8e-11 | yes |
| R3.margin_tax | Operations | row 171 | 4.5e-11 | yes |
| R3.ebitda | Operations | row 172 | 5.0e-11 | yes |
| R3.aug | Operations | row 173 | 0.0e+00 | yes |
| R3.decom | Operations | row 174 | 8.9e-12 | yes |
| R3.cf | Operations | row 175 | 4.4e-11 | yes |
| R3.te_cash | Operations | row 177 | 0.0e+00 | yes |
| R3.mesa_tax_share | Operations | row 178 | 0.0e+00 | yes |
| R3.mesa_cf | Operations | row 179 | 4.3e-11 | yes |
| R3.mesa_taxable | Operations | row 180 | 5.0e-11 | yes |
| R3.s_contracted | Operations | row 182 | 4.5e-11 | yes |
| R3.s_hedged | Operations | row 183 | 0.0e+00 | yes |
| R3.s_merchant | Operations | row 184 | 4.5e-11 | yes |
| R3.mesa_rev | Operations | row 188 | 5.0e-11 | yes |
| R3.ptc_total | Operations | row 189 | 4.5e-11 | yes |
| R4.op_frac | Operations | row 191 | 2.9e-11 | yes |
| R4.own_share | Operations | row 193 | 1.9e-11 | yes |
| R4.hub_atc | Operations | row 194 | 0.0e+00 | yes |
| R4.deg | Operations | row 196 | 5.0e-11 | yes |
| R4.curt | Operations | row 197 | 0.0e+00 | yes |
| R4.gen_full | Operations | row 198 | 5.0e-11 | yes |
| R4.gen | Operations | row 199 | 5.0e-11 | yes |
| R4.cap_hub | Operations | row 200 | 0.0e+00 | yes |
| R4.cap_node | Operations | row 201 | 0.0e+00 | yes |
| R4.node_price | Operations | row 202 | 0.0e+00 | yes |
| R4.con_frac | Operations | row 203 | 0.0e+00 | yes |
| R4.con_vol | Operations | row 204 | 0.0e+00 | yes |
| R4.settle | Operations | row 205 | 1.0e-15 | yes |
| R4.mkt_gen | Operations | row 206 | 5.0e-11 | yes |
| R4.rev_contracted | Operations | row 207 | 0.0e+00 | yes |
| R4.rev_hedged | Operations | row 208 | 0.0e+00 | yes |
| R4.mkt_rev | Operations | row 209 | 4.9e-11 | yes |
| R4.revenue | Operations | row 210 | 4.9e-11 | yes |
| R4.rev_merchant | Operations | row 211 | 4.9e-11 | yes |
| R4.opex | Operations | row 212 | 5.0e-11 | yes |
| R4.land | Operations | row 213 | 0.0e+00 | yes |
| R4.bond | Operations | row 214 | 5.0e-11 | yes |
| R4.margin_tax | Operations | row 215 | 5.0e-11 | yes |
| R4.ebitda | Operations | row 216 | 4.9e-11 | yes |
| R4.aug | Operations | row 217 | 0.0e+00 | yes |
| R4.decom | Operations | row 218 | 1.9e-11 | yes |
| R4.cf | Operations | row 219 | 4.9e-11 | yes |
| R4.te_cash | Operations | row 220 | 0.0e+00 | yes |
| R4.mesa_tax_share | Operations | row 221 | 0.0e+00 | yes |
| R4.mesa_cf | Operations | row 222 | 4.9e-11 | yes |
| R4.mesa_taxable | Operations | row 223 | 4.9e-11 | yes |
| R4.s_contracted | Operations | row 225 | 0.0e+00 | yes |
| R4.s_hedged | Operations | row 226 | 4.6e-11 | yes |
| R4.s_merchant | Operations | row 227 | 4.6e-11 | yes |
| R4.mesa_rev | Operations | row 231 | 4.9e-11 | yes |
| R5.op_frac | Operations | row 233 | 3.7e-11 | yes |
| R5.own_share | Operations | row 235 | 1.9e-11 | yes |
| R5.hub_atc | Operations | row 236 | 0.0e+00 | yes |
| R5.deg | Operations | row 238 | 5.0e-11 | yes |
| R5.curt | Operations | row 239 | 0.0e+00 | yes |
| R5.gen_full | Operations | row 240 | 4.1e-11 | yes |
| R5.gen | Operations | row 241 | 4.9e-11 | yes |
| R5.cap_hub | Operations | row 242 | 0.0e+00 | yes |
| R5.cap_node | Operations | row 243 | 0.0e+00 | yes |
| R5.node_price | Operations | row 244 | 0.0e+00 | yes |
| R5.con_frac | Operations | row 245 | 4.1e-11 | yes |
| R5.con_vol | Operations | row 246 | 4.0e-11 | yes |
| R5.settle | Operations | row 247 | 4.8e-11 | yes |
| R5.mkt_gen | Operations | row 248 | 4.9e-11 | yes |
| R5.rev_contracted | Operations | row 249 | 4.0e-11 | yes |
| R5.rev_hedged | Operations | row 250 | 0.0e+00 | yes |
| R5.mkt_rev | Operations | row 251 | 4.9e-11 | yes |
| R5.revenue | Operations | row 252 | 4.9e-11 | yes |
| R5.rev_merchant | Operations | row 253 | 4.9e-11 | yes |
| R5.opex | Operations | row 254 | 4.9e-11 | yes |
| R5.land | Operations | row 255 | 0.0e+00 | yes |
| R5.bond | Operations | row 256 | 4.9e-11 | yes |
| R5.margin_tax | Operations | row 257 | 4.5e-11 | yes |
| R5.ebitda | Operations | row 258 | 5.0e-11 | yes |
| R5.aug | Operations | row 259 | 0.0e+00 | yes |
| R5.decom | Operations | row 260 | 2.0e-13 | yes |
| R5.cf | Operations | row 261 | 5.0e-11 | yes |
| R5.te_cash | Operations | row 263 | 4.4e-11 | yes |
| R5.mesa_tax_share | Operations | row 264 | 1.4e-12 | yes |
| R5.mesa_cf | Operations | row 265 | 4.8e-11 | yes |
| R5.mesa_taxable | Operations | row 266 | 4.8e-11 | yes |
| R5.s_contracted | Operations | row 268 | 4.5e-11 | yes |
| R5.s_hedged | Operations | row 269 | 0.0e+00 | yes |
| R5.s_merchant | Operations | row 270 | 4.5e-11 | yes |
| R5.mesa_rev | Operations | row 274 | 4.7e-11 | yes |
| R6.op_frac | Operations | row 276 | 4.2e-11 | yes |
| R6.own_share | Operations | row 278 | 2.4e-11 | yes |
| R6.hub_atc | Operations | row 279 | 0.0e+00 | yes |
| R6.con_frac | Operations | row 280 | 4.2e-11 | yes |
| R6.settle | Operations | row 281 | 4.0e-11 | yes |
| R6.stor_rev | Operations | row 282 | 3.2e-11 | yes |
| R6.rev_contracted | Operations | row 283 | 4.0e-11 | yes |
| R6.rev_hedged | Operations | row 284 | 0.0e+00 | yes |
| R6.revenue | Operations | row 285 | 4.0e-11 | yes |
| R6.rev_merchant | Operations | row 286 | 3.2e-11 | yes |
| R6.opex | Operations | row 287 | 4.9e-11 | yes |
| R6.land | Operations | row 288 | 0.0e+00 | yes |
| R6.bond | Operations | row 289 | 4.8e-11 | yes |
| R6.margin_tax | Operations | row 290 | 5.0e-11 | yes |
| R6.ebitda | Operations | row 291 | 5.0e-11 | yes |
| R6.aug | Operations | row 292 | 4.8e-12 | yes |
| R6.decom | Operations | row 293 | 2.5e-11 | yes |
| R6.cf | Operations | row 294 | 5.0e-11 | yes |
| R6.te_cash | Operations | row 295 | 0.0e+00 | yes |
| R6.mesa_tax_share | Operations | row 296 | 0.0e+00 | yes |
| R6.mesa_cf | Operations | row 297 | 5.0e-11 | yes |
| R6.mesa_taxable | Operations | row 298 | 5.0e-11 | yes |
| R6.s_contracted | Operations | row 300 | 3.8e-11 | yes |
| R6.s_hedged | Operations | row 301 | 0.0e+00 | yes |
| R6.s_merchant | Operations | row 302 | 3.8e-11 | yes |
| R6.mesa_rev | Operations | row 306 | 4.0e-11 | yes |
| R7.op_frac | Operations | row 308 | 4.4e-11 | yes |
| R7.own_share | Operations | row 310 | 0.0e+00 | yes |
| R7.hub_atc | Operations | row 311 | 0.0e+00 | yes |
| R7.con_frac | Operations | row 312 | 4.4e-11 | yes |
| R7.settle | Operations | row 314 | 3.6e-11 | yes |
| R7.stor_rev | Operations | row 315 | 4.6e-11 | yes |
| R7.rev_contracted | Operations | row 316 | 3.6e-11 | yes |
| R7.rev_hedged | Operations | row 317 | 0.0e+00 | yes |
| R7.revenue | Operations | row 318 | 4.6e-11 | yes |
| R7.rev_merchant | Operations | row 319 | 4.6e-11 | yes |
| R7.opex | Operations | row 320 | 5.0e-11 | yes |
| R7.land | Operations | row 321 | 0.0e+00 | yes |
| R7.bond | Operations | row 322 | 4.8e-11 | yes |
| R7.margin_tax | Operations | row 323 | 5.0e-11 | yes |
| R7.ebitda | Operations | row 324 | 5.0e-11 | yes |
| R7.aug | Operations | row 325 | 3.8e-11 | yes |
| R7.decom | Operations | row 326 | 2.3e-11 | yes |
| R7.cf | Operations | row 327 | 5.0e-11 | yes |
| R7.te_cash | Operations | row 328 | 0.0e+00 | yes |
| R7.mesa_tax_share | Operations | row 329 | 0.0e+00 | yes |
| R7.mesa_cf | Operations | row 330 | 5.0e-11 | yes |
| R7.mesa_taxable | Operations | row 331 | 5.0e-11 | yes |
| R7.s_contracted | Operations | row 333 | 3.1e-11 | yes |
| R7.s_hedged | Operations | row 334 | 0.0e+00 | yes |
| R7.s_merchant | Operations | row 335 | 3.1e-11 | yes |
| R7.mesa_rev | Operations | row 339 | 4.6e-11 | yes |
| R8.op_frac | Operations | row 341 | 4.6e-11 | yes |
| R8.own_share | Operations | row 343 | 0.0e+00 | yes |
| R8.hub_atc | Operations | row 344 | 0.0e+00 | yes |
| R8.deg | Operations | row 346 | 4.7e-11 | yes |
| R8.curt | Operations | row 347 | 0.0e+00 | yes |
| R8.gen_full | Operations | row 348 | 4.9e-11 | yes |
| R8.gen | Operations | row 349 | 4.9e-11 | yes |
| R8.cap_hub | Operations | row 350 | 0.0e+00 | yes |
| R8.cap_node | Operations | row 351 | 0.0e+00 | yes |
| R8.node_price | Operations | row 352 | 0.0e+00 | yes |
| R8.con_frac | Operations | row 353 | 0.0e+00 | yes |
| R8.con_vol | Operations | row 354 | 0.0e+00 | yes |
| R8.settle | Operations | row 355 | 4.8e-11 | yes |
| R8.mkt_gen | Operations | row 356 | 4.9e-11 | yes |
| R8.rev_contracted | Operations | row 357 | 0.0e+00 | yes |
| R8.rev_hedged | Operations | row 358 | 0.0e+00 | yes |
| R8.mkt_rev | Operations | row 359 | 4.9e-11 | yes |
| R8.revenue | Operations | row 360 | 4.9e-11 | yes |
| R8.rev_merchant | Operations | row 361 | 4.9e-11 | yes |
| R8.opex | Operations | row 362 | 5.0e-11 | yes |
| R8.land | Operations | row 363 | 0.0e+00 | yes |
| R8.bond | Operations | row 364 | 4.8e-11 | yes |
| R8.margin_tax | Operations | row 365 | 4.8e-11 | yes |
| R8.ebitda | Operations | row 366 | 4.8e-11 | yes |
| R8.aug | Operations | row 367 | 0.0e+00 | yes |
| R8.decom | Operations | row 368 | 3.5e-11 | yes |
| R8.cf | Operations | row 369 | 4.8e-11 | yes |
| R8.te_cash | Operations | row 370 | 0.0e+00 | yes |
| R8.mesa_tax_share | Operations | row 371 | 0.0e+00 | yes |
| R8.mesa_cf | Operations | row 372 | 4.8e-11 | yes |
| R8.mesa_taxable | Operations | row 373 | 4.8e-11 | yes |
| R8.s_contracted | Operations | row 375 | 0.0e+00 | yes |
| R8.s_hedged | Operations | row 376 | 3.6e-11 | yes |
| R8.s_merchant | Operations | row 377 | 3.6e-11 | yes |
| R8.mesa_rev | Operations | row 381 | 4.9e-11 | yes |
| portfolio.am_cost | Operations | row 384 | 5.0e-11 | yes |
| portfolio.mesa_rev_contracted_a1 | Operations | row 386 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_a1 | Operations | row 387 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_a1 | Operations | row 388 | 4.9e-11 | yes |
| portfolio.mesa_rev_a1 | Operations | row 389 | 4.9e-11 | yes |
| portfolio.mesa_rev_contracted_all | Operations | row 391 | 4.9e-11 | yes |
| portfolio.mesa_rev_hedged_all | Operations | row 392 | 2.9e-11 | yes |
| portfolio.mesa_rev_merchant_all | Operations | row 393 | 5.0e-11 | yes |
| portfolio.mesa_rev_all | Operations | row 394 | 5.0e-11 | yes |
| portfolio.cfads_a1 | Operations | row 400 | 4.9e-11 | yes |
| portfolio.cfads_all | Operations | row 401 | 4.8e-11 | yes |
| portfolio.cfads_a3 | Operations | row 402 | 4.9e-11 | yes |
| portfolio.share_contracted_a1 | Operations | row 403 | 4.7e-11 | yes |
| portfolio.share_hedged_a1 | Operations | row 404 | 4.5e-11 | yes |
| portfolio.share_merchant_a1 | Operations | row 405 | 4.8e-11 | yes |
| portfolio.share_contracted_all | Operations | row 409 | 4.7e-11 | yes |
| portfolio.share_hedged_all | Operations | row 410 | 4.7e-11 | yes |
| portfolio.share_merchant_all | Operations | row 411 | 3.9e-11 | yes |
| finance.dep | Tax | row 24 | 0.0e+00 | yes |
| finance.taxable_ops | Tax | row 25 | 4.9e-11 | yes |
| finance.tl_open | Debt | row 14 | 4.8e-11 | yes |
| finance.tl_int | Debt | row 15 | 4.5e-11 | yes |
| finance.tl_prin | Debt | row 16 | 3.1e-11 | yes |
| finance.tl_prepay | Debt | row 17 | 2.6e-11 | yes |
| finance.tl_ds | Debt | row 18 | 4.6e-11 | yes |
| finance.rf_open | Debt | row 23 | 3.6e-11 | yes |
| finance.rf_int | Debt | row 24 | 3.9e-11 | yes |
| finance.rf_prin | Debt | row 25 | 4.4e-11 | yes |
| finance.rf_prepay | Debt | row 26 | 2.7e-11 | yes |
| finance.rf_ds | Debt | row 27 | 4.1e-11 | yes |
| finance.u_open | Debt | row 31 | 4.7e-11 | yes |
| finance.u_int | Debt | row 32 | 4.8e-11 | yes |
| finance.u_prin | Debt | row 33 | 4.9e-11 | yes |
| finance.u_ds | Debt | row 34 | 4.3e-11 | yes |
| finance.hc1_open | Debt | row 46 | 4.5e-11 | yes |
| finance.hc1_int | Debt | row 47 | 2.3e-11 | yes |
| finance.hc1_amort | Debt | row 48 | 1.4e-11 | yes |
| finance.hc1_sweep | Debt | row 49 | 4.9e-11 | yes |
| finance.hc1_repay | Debt | row 51 | 1.8e-11 | yes |
| finance.hc2_open | Debt | row 53 | 2.0e-11 | yes |
| finance.hc2_int | Debt | row 54 | 2.1e-11 | yes |
| finance.hc2_amort | Debt | row 55 | 3.9e-11 | yes |
| finance.hc2_sweep | Debt | row 56 | 2.1e-11 | yes |
| finance.hc2_repay | Debt | row 58 | 2.0e-11 | yes |
| finance.hc3_open | Debt | row 60 | 4.9e-11 | yes |
| finance.hc3_int | Debt | row 61 | 4.4e-11 | yes |
| finance.hc3_amort | Debt | row 62 | 3.2e-12 | yes |
| finance.hc3_sweep | Debt | row 63 | 4.6e-11 | yes |
| finance.hc_ds | Debt | row 67 | 4.3e-11 | yes |
| finance.taxable_income | Tax | row 29 | 4.4e-11 | yes |
| finance.nol_open | Tax | row 30 | 4.7e-11 | yes |
| finance.nol_used | Tax | row 31 | 4.5e-11 | yes |
| finance.tax | Tax | row 32 | 5.0e-11 | yes |
| finance.nol_close | Tax | row 33 | 4.7e-11 | yes |
| finance.opco_ds | Waterfall | row 9 | 5.0e-11 | yes |
| finance.opco_dist | Waterfall | row 10 | 4.9e-11 | yes |
| finance.recap_opco | Waterfall | row 11 | 3.6e-11 | yes |
| finance.hc_excess | Waterfall | row 16 | 5.0e-11 | yes |
| finance.fund_dist_ops | Waterfall | row 19 | 5.0e-11 | yes |
| finance.recap_hold | Waterfall | row 20 | 4.0e-11 | yes |
| finance.recap_total | Waterfall | row 21 | 3.5e-12 | yes |
| finance.fund_dist | Waterfall | row 22 | 5.0e-11 | yes |
| finance.dscr_tl | Ratios | row 8 | 3.8e-11 | yes |
| finance.dscr_rf | Ratios | row 9 | 5.0e-11 | yes |
| finance.dscr_u | Ratios | row 10 | 4.9e-11 | yes |
| finance.dscr_opco | Ratios | row 11 | 4.9e-11 | yes |
| finance.hc_cov | Ratios | row 12 | 4.6e-11 | yes |
| finance.nav_df | Returns | row 96 | 5.0e-11 | yes |
| su.A1.opco_fee | Funding | F147 | 0.0e+00 | yes |
| su.A1.holdco_oid | Funding | F148 | 1.1e-15 | yes |
| su.A1.uses | Funding | F149 | 4.0e-13 | yes |
| su.A1.equity | Funding | F150 | 4.3e-14 | yes |
| su.A2.fee | Funding | F151 | 1.1e-16 | yes |
| su.A2.uses | Funding | F152 | 4.3e-14 | yes |
| su.A2.equity | Funding | F153 | 3.6e-15 | yes |
| su.A3.r8_deposit | Funding | F154 | 3.6e-15 | yes |
| su.A3.oid | Funding | F155 | 3.3e-16 | yes |
| su.A3.itc7_proceeds | Funding | F156 | 0.0e+00 | yes |
| su.A3.itc8_proceeds | Funding | F157 | 3.6e-15 | yes |
| su.A3.eq_signing | Funding | F159 | 0.0e+00 | yes |
| su.A3.carry | Funding | F160 | 1.4e-14 | yes |
| su.A3.eq_r7 | Funding | F162 | 0.0e+00 | yes |
| su.A3.carry2 | Funding | F163 | 4.9e-15 | yes |
| su.A3.eq_r8 | Funding | F165 | 4.3e-14 | yes |
| su.A3.cash_left_after_r8 | Funding | F166 | 0.0e+00 | yes |
| su.A3.uses | Funding | F167 | 1.4e-13 | yes |
| su.A3.equity | Funding | F168 | 4.3e-14 | yes |
| refi.mtm_opco_receivable | Funding | F174 | 4.4e-15 | yes |
| refi.mtm_redfern_payable | Funding | F175 | 4.4e-16 | yes |
| refi.costs | Funding | F176 | 4.0e-15 | yes |
| refi.tl_repay | Funding | F177 | 2.8e-13 | yes |
| refi.rf_repay | Funding | F178 | 5.0e-14 | yes |
| refi.opco_net | Funding | F179 | 8.5e-14 | yes |
| sc.tl_dscr_min_2022_2025 | Ratios | F15 | 2.2e-16 | yes |
| sc.tl_dscr_avg_2022_2025 | Ratios | F16 | 8.9e-16 | yes |
| sc.uspp_dscr_min_2026_2043 | Ratios | F17 | 4.2e-15 | yes |
| sc.uspp_dscr_avg_2026_2043 | Ratios | F18 | 3.1e-15 | yes |
| sc.rf_dscr_min | Ratios | F19 | 2.2e-16 | yes |
| sc.rf_dscr_avg | Ratios | F20 | 3.8e-15 | yes |
| sc.holdco_cov_min_2023_2031 | Ratios | F21 | 1.6e-15 | yes |
| sc.holdco_cov_avg_2023_2031 | Ratios | F22 | 4.0e-15 | yes |
| sc.fund_nav_2025 | Returns | F98 | 1.7e-13 | yes |
| sc.fund_contributions | Returns | F99 | 2.0e-13 | yes |
| sc.fund_distributions_life | Returns | F100 | 1.1e-13 | yes |
| sc.fund_distributions_to_2025 | Returns | F101 | 2.7e-13 | yes |
| sc.fund_moic_life_x | Returns | F102 | 1.3e-15 | yes |
| sc.fund_moic_2025_x | Returns | F103 | 4.7e-15 | yes |
| sc.fund_irr_life_pct | Returns | F150 | 2.1e-14 | yes |
| sc.fund_irr_2025_pct | Returns | F151 | 7.1e-15 | yes |
