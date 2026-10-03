# Figure ledger, Case R (Mesa Corta Renewables)

Every value below is read by `model/ledger_case_r.py` from `model/outputs_case_r.json` (model R-1.1 (inputs v1.1), generated 2026-10-03). The JSON path is given for each figure so a reviewer can trace it. Display rounding follows the style sheet: USD m to one decimal, ratios to two decimals with x, rates to two decimals, returns to one decimal in prose. Scenario names: base, low, high (price and capture cases), p90_1yr, p90_10yr, p99_1yr (volume cases applied in every year), status_quo (no 2025 refinancing), sens_* (sensitivities). Debt is sized once on the base case and held fixed in every other scenario. Every Case R price is Illustrative. Figures R-F11 to R-F17 are new IDs added by the modeler.

| ID | Figure | Value | Units | Scenario | Story date | JSON path |
|---|---|---|---|---|---|---|
| R-F01 | R1 P50 (input) | 695.8 | GWh/yr | inputs | 2021-12 | inputs_case_r.json assets |
| R-F01 | R1 P90 one-year | 87.60% | % | yield model | 2021-12 | `diversification.assets.R1.p90_1yr` |
| R-F01 | R1 P90 ten-year | 92.90% | % | yield model | 2021-12 | `diversification.assets.R1.p90_10yr` |
| R-F01 | R1 P99 one-year (recomputed, R-C09) | 77.49% | % | yield model | 2021-12 | `diversification.assets.R1.p99_1yr` |
| R-F01 | R1 P99 ten-year | 87.11% | % | yield model | 2021-12 | `diversification.assets.R1.p99_10yr` |
| R-F01 | R1 long-term sigma (fraction of P50) | 0.049 | ratio | yield model | 2021-12 | `diversification.assets.R1.sigma_lt` |
| R-F01 | R1 inter-annual sigma (fraction of P50) | 0.084 | ratio | yield model | 2021-12 | `diversification.assets.R1.sigma_iav` |
| R-F01 | R1 one-year sigma (fraction of P50) | 0.097 | ratio | yield model | 2021-12 | `diversification.assets.R1.sigma_1yr` |
| R-F01 | R1 ten-year sigma (fraction of P50) | 0.055 | ratio | yield model | 2021-12 | `diversification.assets.R1.sigma_10yr` |
| R-F01 | R2 P50 (input) | 785.5 | GWh/yr | inputs | 2021-12 | inputs_case_r.json assets |
| R-F01 | R2 P90 one-year | 89.20% | % | yield model | 2021-12 | `diversification.assets.R2.p90_1yr` |
| R-F01 | R2 P90 ten-year | 94.10% | % | yield model | 2021-12 | `diversification.assets.R2.p90_10yr` |
| R-F01 | R2 P99 one-year (recomputed, R-C09) | 80.40% | % | yield model | 2021-12 | `diversification.assets.R2.p99_1yr` |
| R-F01 | R2 P99 ten-year | 89.29% | % | yield model | 2021-12 | `diversification.assets.R2.p99_10yr` |
| R-F01 | R2 long-term sigma (fraction of P50) | 0.040 | ratio | yield model | 2021-12 | `diversification.assets.R2.sigma_lt` |
| R-F01 | R2 inter-annual sigma (fraction of P50) | 0.074 | ratio | yield model | 2021-12 | `diversification.assets.R2.sigma_iav` |
| R-F01 | R2 one-year sigma (fraction of P50) | 0.084 | ratio | yield model | 2021-12 | `diversification.assets.R2.sigma_1yr` |
| R-F01 | R2 ten-year sigma (fraction of P50) | 0.046 | ratio | yield model | 2021-12 | `diversification.assets.R2.sigma_10yr` |
| R-F01 | R3 P50 (input) | 619.2 | GWh/yr | inputs | 2021-12 | inputs_case_r.json assets |
| R-F01 | R3 P90 one-year | 86.90% | % | yield model | 2021-12 | `diversification.assets.R3.p90_1yr` |
| R-F01 | R3 P90 ten-year | 92.40% | % | yield model | 2021-12 | `diversification.assets.R3.p90_10yr` |
| R-F01 | R3 P99 one-year (recomputed, R-C09) | 76.22% | % | yield model | 2021-12 | `diversification.assets.R3.p99_1yr` |
| R-F01 | R3 P99 ten-year | 86.20% | % | yield model | 2021-12 | `diversification.assets.R3.p99_10yr` |
| R-F01 | R3 long-term sigma (fraction of P50) | 0.052 | ratio | yield model | 2021-12 | `diversification.assets.R3.sigma_lt` |
| R-F01 | R3 inter-annual sigma (fraction of P50) | 0.088 | ratio | yield model | 2021-12 | `diversification.assets.R3.sigma_iav` |
| R-F01 | R3 one-year sigma (fraction of P50) | 0.102 | ratio | yield model | 2021-12 | `diversification.assets.R3.sigma_1yr` |
| R-F01 | R3 ten-year sigma (fraction of P50) | 0.059 | ratio | yield model | 2021-12 | `diversification.assets.R3.sigma_10yr` |
| R-F01 | R4 P50 (input) | 234.3 | GWh/yr | inputs | 2021-12 | inputs_case_r.json assets |
| R-F01 | R4 P90 one-year | 94.60% | % | yield model | 2021-12 | `diversification.assets.R4.p90_1yr` |
| R-F01 | R4 P90 ten-year | 96.80% | % | yield model | 2021-12 | `diversification.assets.R4.p90_10yr` |
| R-F01 | R4 P99 one-year (recomputed, R-C09) | 90.20% | % | yield model | 2021-12 | `diversification.assets.R4.p99_1yr` |
| R-F01 | R4 P99 ten-year | 94.19% | % | yield model | 2021-12 | `diversification.assets.R4.p99_10yr` |
| R-F01 | R4 long-term sigma (fraction of P50) | 0.022 | ratio | yield model | 2021-12 | `diversification.assets.R4.sigma_lt` |
| R-F01 | R4 inter-annual sigma (fraction of P50) | 0.036 | ratio | yield model | 2021-12 | `diversification.assets.R4.sigma_iav` |
| R-F01 | R4 one-year sigma (fraction of P50) | 0.042 | ratio | yield model | 2021-12 | `diversification.assets.R4.sigma_1yr` |
| R-F01 | R4 ten-year sigma (fraction of P50) | 0.025 | ratio | yield model | 2021-12 | `diversification.assets.R4.sigma_10yr` |
| R-F01 | R5 P50 (input) | 452.2 | GWh/yr | inputs | 2021-12 | inputs_case_r.json assets |
| R-F01 | R5 P90 one-year | 94.20% | % | yield model | 2021-12 | `diversification.assets.R5.p90_1yr` |
| R-F01 | R5 P90 ten-year | 96.50% | % | yield model | 2021-12 | `diversification.assets.R5.p90_10yr` |
| R-F01 | R5 P99 one-year (recomputed, R-C09) | 89.47% | % | yield model | 2021-12 | `diversification.assets.R5.p99_1yr` |
| R-F01 | R5 P99 ten-year | 93.65% | % | yield model | 2021-12 | `diversification.assets.R5.p99_10yr` |
| R-F01 | R5 long-term sigma (fraction of P50) | 0.025 | ratio | yield model | 2021-12 | `diversification.assets.R5.sigma_lt` |
| R-F01 | R5 inter-annual sigma (fraction of P50) | 0.038 | ratio | yield model | 2021-12 | `diversification.assets.R5.sigma_iav` |
| R-F01 | R5 one-year sigma (fraction of P50) | 0.045 | ratio | yield model | 2021-12 | `diversification.assets.R5.sigma_1yr` |
| R-F01 | R5 ten-year sigma (fraction of P50) | 0.027 | ratio | yield model | 2021-12 | `diversification.assets.R5.sigma_10yr` |
| R-F01 | R8 P50 (input) | 290.1 | GWh/yr | inputs | 2021-12 | inputs_case_r.json assets |
| R-F01 | R8 P90 one-year | 94.40% | % | yield model | 2021-12 | `diversification.assets.R8.p90_1yr` |
| R-F01 | R8 P90 ten-year | 96.60% | % | yield model | 2021-12 | `diversification.assets.R8.p90_10yr` |
| R-F01 | R8 P99 one-year (recomputed, R-C09) | 89.84% | % | yield model | 2021-12 | `diversification.assets.R8.p99_1yr` |
| R-F01 | R8 P99 ten-year | 93.83% | % | yield model | 2021-12 | `diversification.assets.R8.p99_10yr` |
| R-F01 | R8 long-term sigma (fraction of P50) | 0.024 | ratio | yield model | 2021-12 | `diversification.assets.R8.sigma_lt` |
| R-F01 | R8 inter-annual sigma (fraction of P50) | 0.037 | ratio | yield model | 2021-12 | `diversification.assets.R8.sigma_iav` |
| R-F01 | R8 one-year sigma (fraction of P50) | 0.044 | ratio | yield model | 2021-12 | `diversification.assets.R8.sigma_1yr` |
| R-F01 | R8 ten-year sigma (fraction of P50) | 0.027 | ratio | yield model | 2021-12 | `diversification.assets.R8.sigma_10yr` |
| R-F01 | A1 portfolio (R1-R5) P50 | 2,787.0 | GWh | yield model (correlated) | 2021-12 | `diversification.A1.p50_gwh` |
| R-F01 | A1 portfolio (R1-R5) P90 one-year | 2,589.4 | GWh | yield model (correlated) | 2021-12 | `diversification.A1.p90_1yr_gwh` |
| R-F01 | A1 portfolio (R1-R5) P90 one-year | 92.91% | % | yield model (correlated) | 2021-12 | `diversification.A1.p90_1yr_pct` |
| R-F01 | A1 portfolio (R1-R5) P99 one-year | 2,428.4 | GWh | yield model (correlated) | 2021-12 | `diversification.A1.p99_1yr_gwh` |
| R-F01 | A1 portfolio (R1-R5) P99 one-year | 87.13% | % | yield model (correlated) | 2021-12 | `diversification.A1.p99_1yr_pct` |
| R-F01 | A1 portfolio (R1-R5) P90 ten-year | 2,670.5 | GWh | yield model (correlated) | 2021-12 | `diversification.A1.p90_10yr_gwh` |
| R-F01 | A1 portfolio (R1-R5) P90 ten-year | 95.82% | % | yield model (correlated) | 2021-12 | `diversification.A1.p90_10yr_pct` |
| R-F01 | A1 portfolio (R1-R5) P99 ten-year | 2,575.6 | GWh | yield model (correlated) | 2021-12 | `diversification.A1.p99_10yr_gwh` |
| R-F01 | A1 portfolio (R1-R5) P99 ten-year | 92.41% | % | yield model (correlated) | 2021-12 | `diversification.A1.p99_10yr_pct` |
| R-F01 | A1 portfolio (R1-R5) P90 one-year if fully correlated | 89.55% | % | yield model (correlated) | 2021-12 | `diversification.A1.p90_1yr_correlated_pct` |
| R-F01 | A1 portfolio (R1-R5) P90 one-year if independent | 94.67% | % | yield model (correlated) | 2021-12 | `diversification.A1.p90_1yr_independent_pct` |
| R-F01 | All generation (R1-R5, R8) P50 | 3,077.1 | GWh | yield model (correlated) | 2021-12 | `diversification.all_generation.p50_gwh` |
| R-F01 | All generation (R1-R5, R8) P90 one-year | 2,878.8 | GWh | yield model (correlated) | 2021-12 | `diversification.all_generation.p90_1yr_gwh` |
| R-F01 | All generation (R1-R5, R8) P90 one-year | 93.55% | % | yield model (correlated) | 2021-12 | `diversification.all_generation.p90_1yr_pct` |
| R-F01 | All generation (R1-R5, R8) P99 one-year | 2,717.1 | GWh | yield model (correlated) | 2021-12 | `diversification.all_generation.p99_1yr_gwh` |
| R-F01 | All generation (R1-R5, R8) P99 one-year | 88.30% | % | yield model (correlated) | 2021-12 | `diversification.all_generation.p99_1yr_pct` |
| R-F01 | All generation (R1-R5, R8) P90 ten-year | 2,959.5 | GWh | yield model (correlated) | 2021-12 | `diversification.all_generation.p90_10yr_gwh` |
| R-F01 | All generation (R1-R5, R8) P90 ten-year | 96.18% | % | yield model (correlated) | 2021-12 | `diversification.all_generation.p90_10yr_pct` |
| R-F01 | All generation (R1-R5, R8) P99 ten-year | 2,863.6 | GWh | yield model (correlated) | 2021-12 | `diversification.all_generation.p99_10yr_gwh` |
| R-F01 | All generation (R1-R5, R8) P99 ten-year | 93.06% | % | yield model (correlated) | 2021-12 | `diversification.all_generation.p99_10yr_pct` |
| R-F01 | All generation (R1-R5, R8) P90 one-year if fully correlated | 90.01% | % | yield model (correlated) | 2021-12 | `diversification.all_generation.p90_1yr_correlated_pct` |
| R-F01 | All generation (R1-R5, R8) P90 one-year if independent | 95.14% | % | yield model (correlated) | 2021-12 | `diversification.all_generation.p90_1yr_independent_pct` |
| R-F01 | Yield correlation iav_wind_west_west | 0.60 | rho | assumption (R-C10) | 2021-12 | `diversification.correlations.iav_wind_west_west` |
| R-F01 | Yield correlation iav_wind_west_coastal | 0.30 | rho | assumption (R-C10) | 2021-12 | `diversification.correlations.iav_wind_west_coastal` |
| R-F01 | Yield correlation iav_solar_west_west | 0.85 | rho | assumption (R-C10) | 2021-12 | `diversification.correlations.iav_solar_west_west` |
| R-F01 | Yield correlation iav_solar_west_south | 0.50 | rho | assumption (R-C10) | 2021-12 | `diversification.correlations.iav_solar_west_south` |
| R-F01 | Yield correlation iav_wind_solar | -0.10 | rho | assumption (R-C10) | 2021-12 | `diversification.correlations.iav_wind_solar` |
| R-F01 | Yield correlation lt_same_technology | 0.50 | rho | assumption (R-C10) | 2021-12 | `diversification.correlations.lt_same_technology` |
| R-F01 | Yield correlation lt_cross_technology | 0.00 | rho | assumption (R-C10) | 2021-12 | `diversification.correlations.lt_cross_technology` |
| R-F02 | R4 shape hedge volume 2022 | 168.4 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R4.con_vol.0` |
| R-F02 | R2 PPA volume 2022 | 773.7 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R2.con_vol.0` |
| R-F02 | R5 vPPA volume 2022 | 443.2 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R5.con_vol.0` |
| R-F02 | R2 PPA revenue 2022 | 24.3 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R2.settle.0` |
| R-F02 | R3 PRS net settlement 2022 | -2.1 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R3.settle.0` |
| R-F02 | R4 shape hedge settlement 2022 | -3.0 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R4.settle.0` |
| R-F02 | R5 vPPA settlement 2022 | -15.2 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R5.settle.0` |
| R-F02 | Share of Mesa revenue contracted 2022 | 54.3% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_contracted_all.0` |
| R-F02 | Share of Mesa revenue hedged 2022 | 8.1% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_hedged_all.0` |
| R-F02 | Share of Mesa revenue merchant 2022 | 37.6% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_merchant_all.0` |
| R-F02 | R1 swap volume 2023 | 350.4 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R1.con_vol.1` |
| R-F02 | R4 shape hedge volume 2023 | 168.4 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R4.con_vol.1` |
| R-F02 | R2 PPA volume 2023 | 772.2 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R2.con_vol.1` |
| R-F02 | R5 vPPA volume 2023 | 438.9 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R5.con_vol.1` |
| R-F02 | R1 swap settlement 2023 | -3.9 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R1.settle.1` |
| R-F02 | R2 PPA revenue 2023 | 24.2 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R2.settle.1` |
| R-F02 | R3 PRS net settlement 2023 | 3.3 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R3.settle.1` |
| R-F02 | R4 shape hedge settlement 2023 | -1.0 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R4.settle.1` |
| R-F02 | R5 vPPA settlement 2023 | -9.6 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R5.settle.1` |
| R-F02 | R6 toll revenue 2023 | 5.1 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R6.settle.1` |
| R-F02 | Share of Mesa revenue contracted 2023 | 63.1% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_contracted_all.1` |
| R-F02 | Share of Mesa revenue hedged 2023 | 28.8% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_hedged_all.1` |
| R-F02 | Share of Mesa revenue merchant 2023 | 8.1% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_merchant_all.1` |
| R-F02 | R1 swap volume 2024 | 351.4 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R1.con_vol.2` |
| R-F02 | R4 shape hedge volume 2024 | 168.4 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R4.con_vol.2` |
| R-F02 | R2 PPA volume 2024 | 770.6 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R2.con_vol.2` |
| R-F02 | R5 vPPA volume 2024 | 434.7 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R5.con_vol.2` |
| R-F02 | R1 swap settlement 2024 | 6.7 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R1.settle.2` |
| R-F02 | R2 PPA revenue 2024 | 24.2 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R2.settle.2` |
| R-F02 | R3 PRS net settlement 2024 | 14.9 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R3.settle.2` |
| R-F02 | R4 shape hedge settlement 2024 | 3.4 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R4.settle.2` |
| R-F02 | R5 vPPA settlement 2024 | 1.7 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R5.settle.2` |
| R-F02 | R6 toll revenue 2024 | 11.0 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R6.settle.2` |
| R-F02 | R7 revenue under floor contract 2024 | 7.6 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R7.settle.2` |
| R-F02 | Share of Mesa revenue contracted 2024 | 71.1% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_contracted_all.2` |
| R-F02 | Share of Mesa revenue hedged 2024 | 25.5% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_hedged_all.2` |
| R-F02 | Share of Mesa revenue merchant 2024 | 3.4% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_merchant_all.2` |
| R-F02 | R1 swap volume 2025 | 350.4 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R1.con_vol.3` |
| R-F02 | R4 shape hedge volume 2025 | 168.4 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R4.con_vol.3` |
| R-F02 | R8 shape hedge volume 2025 | 174.1 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R8.con_vol.3` |
| R-F02 | R2 PPA volume 2025 | 769.1 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R2.con_vol.3` |
| R-F02 | R5 vPPA volume 2025 | 430.5 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R5.con_vol.3` |
| R-F02 | R1 swap settlement 2025 | 3.4 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R1.settle.3` |
| R-F02 | R2 PPA revenue 2025 | 24.1 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R2.settle.3` |
| R-F02 | R3 PRS net settlement 2025 | 11.6 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R3.settle.3` |
| R-F02 | R4 shape hedge settlement 2025 | 2.2 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R4.settle.3` |
| R-F02 | R5 vPPA settlement 2025 | -1.3 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R5.settle.3` |
| R-F02 | R6 toll revenue 2025 | 11.0 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R6.settle.3` |
| R-F02 | R7 revenue under floor contract 2025 | 10.2 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R7.settle.3` |
| R-F02 | R8 shape hedge settlement 2025 | 1.0 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R8.settle.3` |
| R-F02 | Share of Mesa revenue contracted 2025 | 64.8% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_contracted_all.3` |
| R-F02 | Share of Mesa revenue hedged 2025 | 28.6% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_hedged_all.3` |
| R-F02 | Share of Mesa revenue merchant 2025 | 6.6% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_merchant_all.3` |
| R-F02 | R1 swap volume 2026 | 350.4 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R1.con_vol.4` |
| R-F02 | R4 shape hedge volume 2026 | 168.4 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R4.con_vol.4` |
| R-F02 | R8 shape hedge volume 2026 | 174.1 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R8.con_vol.4` |
| R-F02 | R2 PPA volume 2026 | 767.5 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R2.con_vol.4` |
| R-F02 | R5 vPPA volume 2026 | 428.6 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R5.con_vol.4` |
| R-F02 | R1 swap settlement 2026 | 1.8 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R1.settle.4` |
| R-F02 | R2 PPA revenue 2026 | 24.1 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R2.settle.4` |
| R-F02 | R3 PRS net settlement 2026 | 10.1 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R3.settle.4` |
| R-F02 | R4 shape hedge settlement 2026 | 1.8 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R4.settle.4` |
| R-F02 | R5 vPPA settlement 2026 | -2.5 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R5.settle.4` |
| R-F02 | R6 toll revenue 2026 | 11.0 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R6.settle.4` |
| R-F02 | R7 revenue under floor contract 2026 | 10.2 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R7.settle.4` |
| R-F02 | R8 shape hedge settlement 2026 | 0.4 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R8.settle.4` |
| R-F02 | Share of Mesa revenue contracted 2026 | 64.5% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_contracted_all.4` |
| R-F02 | Share of Mesa revenue hedged 2026 | 28.5% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_hedged_all.4` |
| R-F02 | Share of Mesa revenue merchant 2026 | 7.0% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_merchant_all.4` |
| R-F02 | R1 swap volume 2027 | 350.4 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R1.con_vol.5` |
| R-F02 | R8 shape hedge volume 2027 | 174.1 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R8.con_vol.5` |
| R-F02 | R2 PPA volume 2027 | 766.0 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R2.con_vol.5` |
| R-F02 | R5 vPPA volume 2027 | 426.6 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R5.con_vol.5` |
| R-F02 | R1 swap settlement 2027 | 0.9 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R1.settle.5` |
| R-F02 | R2 PPA revenue 2027 | 24.1 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R2.settle.5` |
| R-F02 | R3 PRS net settlement 2027 | 9.3 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R3.settle.5` |
| R-F02 | R5 vPPA settlement 2027 | -3.0 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R5.settle.5` |
| R-F02 | R6 toll revenue 2027 | 11.0 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R6.settle.5` |
| R-F02 | R7 revenue under floor contract 2027 | 10.2 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R7.settle.5` |
| R-F02 | R8 shape hedge settlement 2027 | 0.2 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R8.settle.5` |
| R-F02 | Share of Mesa revenue contracted 2027 | 65.7% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_contracted_all.5` |
| R-F02 | Share of Mesa revenue hedged 2027 | 21.9% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_hedged_all.5` |
| R-F02 | Share of Mesa revenue merchant 2027 | 12.4% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_merchant_all.5` |
| R-F02 | R8 shape hedge volume 2028 | 174.1 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R8.con_vol.6` |
| R-F02 | R2 PPA volume 2028 | 764.5 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R2.con_vol.6` |
| R-F02 | R5 vPPA volume 2028 | 424.7 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R5.con_vol.6` |
| R-F02 | R2 PPA revenue 2028 | 24.0 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R2.settle.6` |
| R-F02 | R3 PRS net settlement 2028 | 8.8 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R3.settle.6` |
| R-F02 | R5 vPPA settlement 2028 | -3.1 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R5.settle.6` |
| R-F02 | R6 toll revenue 2028 | 11.0 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R6.settle.6` |
| R-F02 | R7 revenue under floor contract 2028 | 10.2 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R7.settle.6` |
| R-F02 | R8 shape hedge settlement 2028 | 0.1 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R8.settle.6` |
| R-F02 | Share of Mesa revenue contracted 2028 | 66.2% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_contracted_all.6` |
| R-F02 | Share of Mesa revenue hedged 2028 | 6.2% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_hedged_all.6` |
| R-F02 | Share of Mesa revenue merchant 2028 | 27.6% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_merchant_all.6` |
| R-F02 | R8 shape hedge volume 2029 | 174.1 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R8.con_vol.7` |
| R-F02 | R2 PPA volume 2029 | 378.3 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R2.con_vol.7` |
| R-F02 | R5 vPPA volume 2029 | 422.8 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R5.con_vol.7` |
| R-F02 | R2 PPA revenue 2029 | 11.9 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R2.settle.7` |
| R-F02 | R3 PRS net settlement 2029 | 8.5 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R3.settle.7` |
| R-F02 | R5 vPPA settlement 2029 | -3.1 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R5.settle.7` |
| R-F02 | R6 toll revenue 2029 | 11.0 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R6.settle.7` |
| R-F02 | R7 revenue under floor contract 2029 | 10.2 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R7.settle.7` |
| R-F02 | R8 shape hedge settlement 2029 | 0.0 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R8.settle.7` |
| R-F02 | Share of Mesa revenue contracted 2029 | 52.5% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_contracted_all.7` |
| R-F02 | Share of Mesa revenue hedged 2029 | 6.0% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_hedged_all.7` |
| R-F02 | Share of Mesa revenue merchant 2029 | 41.5% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_merchant_all.7` |
| R-F02 | R8 shape hedge volume 2030 | 174.1 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R8.con_vol.8` |
| R-F02 | R5 vPPA volume 2030 | 420.9 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R5.con_vol.8` |
| R-F02 | R5 vPPA settlement 2030 | -3.1 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R5.settle.8` |
| R-F02 | R6 toll revenue 2030 | 5.8 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R6.settle.8` |
| R-F02 | R7 revenue under floor contract 2030 | 10.2 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R7.settle.8` |
| R-F02 | R8 shape hedge settlement 2030 | 0.0 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R8.settle.8` |
| R-F02 | Share of Mesa revenue contracted 2030 | 23.1% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_contracted_all.8` |
| R-F02 | Share of Mesa revenue hedged 2030 | 5.7% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_hedged_all.8` |
| R-F02 | Share of Mesa revenue merchant 2030 | 71.2% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_merchant_all.8` |
| R-F02 | R8 shape hedge volume 2031 | 174.1 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R8.con_vol.9` |
| R-F02 | R5 vPPA volume 2031 | 419.0 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R5.con_vol.9` |
| R-F02 | R5 vPPA settlement 2031 | -2.9 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R5.settle.9` |
| R-F02 | R7 revenue under floor contract 2031 | 10.2 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R7.settle.9` |
| R-F02 | R8 shape hedge settlement 2031 | 0.0 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R8.settle.9` |
| R-F02 | Share of Mesa revenue contracted 2031 | 18.4% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_contracted_all.9` |
| R-F02 | Share of Mesa revenue hedged 2031 | 5.8% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_hedged_all.9` |
| R-F02 | Share of Mesa revenue merchant 2031 | 75.8% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_merchant_all.9` |
| R-F02 | R8 shape hedge volume 2032 | 174.1 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R8.con_vol.10` |
| R-F02 | R5 vPPA volume 2032 | 417.1 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R5.con_vol.10` |
| R-F02 | R5 vPPA settlement 2032 | -2.7 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R5.settle.10` |
| R-F02 | R7 revenue under floor contract 2032 | 2.6 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R7.settle.10` |
| R-F02 | R8 shape hedge settlement 2032 | 0.1 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R8.settle.10` |
| R-F02 | Share of Mesa revenue contracted 2032 | 11.8% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_contracted_all.10` |
| R-F02 | Share of Mesa revenue hedged 2032 | 5.8% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_hedged_all.10` |
| R-F02 | Share of Mesa revenue merchant 2032 | 82.4% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_merchant_all.10` |
| R-F02 | R8 shape hedge volume 2033 | 174.1 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R8.con_vol.11` |
| R-F02 | R5 vPPA volume 2033 | 205.9 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R5.con_vol.11` |
| R-F02 | R5 vPPA settlement 2033 | -1.3 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R5.settle.11` |
| R-F02 | R8 shape hedge settlement 2033 | 0.1 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R8.settle.11` |
| R-F02 | Share of Mesa revenue contracted 2033 | 4.6% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_contracted_all.11` |
| R-F02 | Share of Mesa revenue hedged 2033 | 5.8% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_hedged_all.11` |
| R-F02 | Share of Mesa revenue merchant 2033 | 89.6% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_merchant_all.11` |
| R-F02 | R8 shape hedge volume 2034 | 174.1 | GWh | base | 2022-10 to 2023 | `scenarios.base.series.R8.con_vol.12` |
| R-F02 | R8 shape hedge settlement 2034 | 0.2 | USD m | base | 2022-10 to 2023 | `scenarios.base.series.R8.settle.12` |
| R-F02 | Share of Mesa revenue contracted 2034 | 0.0% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_contracted_all.12` |
| R-F02 | Share of Mesa revenue hedged 2034 | 5.7% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_hedged_all.12` |
| R-F02 | Share of Mesa revenue merchant 2034 | 94.3% | share | base | 2022-10 to 2023 | `scenarios.base.series.portfolio.share_merchant_all.12` |
| R-F02 | R1 settlement 2026 (low) | 5.0 | USD m | low | 2022-10 to 2023 | `scenarios.low.series.R1.settle.4` |
| R-F02 | R4 settlement 2026 (low) | 3.2 | USD m | low | 2022-10 to 2023 | `scenarios.low.series.R4.settle.4` |
| R-F02 | R5 settlement 2026 (low) | 1.1 | USD m | low | 2022-10 to 2023 | `scenarios.low.series.R5.settle.4` |
| R-F02 | R8 settlement 2026 (low) | 2.0 | USD m | low | 2022-10 to 2023 | `scenarios.low.series.R8.settle.4` |
| R-F02 | R1 settlement 2028 (low) | 0.0 | USD m | low | 2022-10 to 2023 | `scenarios.low.series.R1.settle.6` |
| R-F02 | R4 settlement 2028 (low) | 0.0 | USD m | low | 2022-10 to 2023 | `scenarios.low.series.R4.settle.6` |
| R-F02 | R5 settlement 2028 (low) | 1.4 | USD m | low | 2022-10 to 2023 | `scenarios.low.series.R5.settle.6` |
| R-F02 | R8 settlement 2028 (low) | 2.0 | USD m | low | 2022-10 to 2023 | `scenarios.low.series.R8.settle.6` |
| R-F02 | R1 settlement 2030 (low) | 0.0 | USD m | low | 2022-10 to 2023 | `scenarios.low.series.R1.settle.8` |
| R-F02 | R4 settlement 2030 (low) | 0.0 | USD m | low | 2022-10 to 2023 | `scenarios.low.series.R4.settle.8` |
| R-F02 | R5 settlement 2030 (low) | 2.0 | USD m | low | 2022-10 to 2023 | `scenarios.low.series.R5.settle.8` |
| R-F02 | R8 settlement 2030 (low) | 2.2 | USD m | low | 2022-10 to 2023 | `scenarios.low.series.R8.settle.8` |
| R-F02 | R1 settlement 2026 (high) | -2.2 | USD m | high | 2022-10 to 2023 | `scenarios.high.series.R1.settle.4` |
| R-F02 | R4 settlement 2026 (high) | -0.1 | USD m | high | 2022-10 to 2023 | `scenarios.high.series.R4.settle.4` |
| R-F02 | R5 settlement 2026 (high) | -7.2 | USD m | high | 2022-10 to 2023 | `scenarios.high.series.R5.settle.4` |
| R-F02 | R8 settlement 2026 (high) | -1.6 | USD m | high | 2022-10 to 2023 | `scenarios.high.series.R8.settle.4` |
| R-F02 | R1 settlement 2028 (high) | -0.0 | USD m | high | 2022-10 to 2023 | `scenarios.high.series.R1.settle.6` |
| R-F02 | R4 settlement 2028 (high) | -0.0 | USD m | high | 2022-10 to 2023 | `scenarios.high.series.R4.settle.6` |
| R-F02 | R5 settlement 2028 (high) | -9.0 | USD m | high | 2022-10 to 2023 | `scenarios.high.series.R5.settle.6` |
| R-F02 | R8 settlement 2028 (high) | -2.5 | USD m | high | 2022-10 to 2023 | `scenarios.high.series.R8.settle.6` |
| R-F02 | R1 settlement 2030 (high) | -0.0 | USD m | high | 2022-10 to 2023 | `scenarios.high.series.R1.settle.8` |
| R-F02 | R4 settlement 2030 (high) | -0.0 | USD m | high | 2022-10 to 2023 | `scenarios.high.series.R4.settle.8` |
| R-F02 | R5 settlement 2030 (high) | -9.5 | USD m | high | 2022-10 to 2023 | `scenarios.high.series.R5.settle.8` |
| R-F02 | R8 settlement 2030 (high) | -2.8 | USD m | high | 2022-10 to 2023 | `scenarios.high.series.R8.settle.8` |
| R-F03 | Swap volume over the event | 2,880 | MWh | sensitivity (72 h at USD 5,000/MWh, 15% availability) | 2022-10 | `uri_stress.swap_mwh` |
| R-F03 | R1 generation over the event | 2,177 | MWh | sensitivity (72 h at USD 5,000/MWh, 15% availability) | 2022-10 | `uri_stress.gen_mwh` |
| R-F03 | Volume shortfall | 703 | MWh | sensitivity (72 h at USD 5,000/MWh, 15% availability) | 2022-10 | `uri_stress.shortfall_mwh` |
| R-F03 | Swap settlement paid | 14.3 | USD m | sensitivity (72 h at USD 5,000/MWh, 15% availability) | 2022-10 | `uri_stress.swap_payment` |
| R-F03 | Physical revenue | 10.9 | USD m | sensitivity (72 h at USD 5,000/MWh, 15% availability) | 2022-10 | `uri_stress.physical_revenue` |
| R-F03 | Net cash over the event | -3.4 | USD m | sensitivity (72 h at USD 5,000/MWh, 15% availability) | 2022-10 | `uri_stress.net_cash` |
| R-F03 | Net cash versus normal hedged revenue for the same hours | -3.5 | USD m | sensitivity (72 h at USD 5,000/MWh, 15% availability) | 2022-10 | `uri_stress.net_vs_fully_covered` |
| R-F04 | A1 value R1 contracted | 0.0 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R1.contracted` |
| R-F04 | A1 value R1 hedged | 25.8 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R1.hedged` |
| R-F04 | A1 value R1 merchant | 52.8 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R1.merchant` |
| R-F04 | A1 value R1 total | 78.6 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R1.total` |
| R-F04 | A1 value R2 contracted | 51.4 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R2.contracted` |
| R-F04 | A1 value R2 hedged | 0.0 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R2.hedged` |
| R-F04 | A1 value R2 merchant | 68.7 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R2.merchant` |
| R-F04 | A1 value R2 total | 120.1 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R2.total` |
| R-F04 | A1 value R3 contracted | 62.6 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R3.contracted` |
| R-F04 | A1 value R3 hedged | 0.0 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R3.hedged` |
| R-F04 | A1 value R3 merchant | 18.6 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R3.merchant` |
| R-F04 | A1 value R3 total | 81.2 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R3.total` |
| R-F04 | A1 value R4 contracted | 0.0 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R4.contracted` |
| R-F04 | A1 value R4 hedged | 17.8 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R4.hedged` |
| R-F04 | A1 value R4 merchant | 27.0 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R4.merchant` |
| R-F04 | A1 value R4 total | 44.8 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R4.total` |
| R-F04 | A1 value R5 contracted | 46.5 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R5.contracted` |
| R-F04 | A1 value R5 hedged | 0.0 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R5.hedged` |
| R-F04 | A1 value R5 merchant | 17.2 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R5.merchant` |
| R-F04 | A1 value R5 total | 63.7 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.R5.total` |
| R-F04 | A1 value Platform costs contracted | -10.6 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.Platform costs.contracted` |
| R-F04 | A1 value Platform costs hedged | -3.2 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.Platform costs.hedged` |
| R-F04 | A1 value Platform costs merchant | -19.6 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.Platform costs.merchant` |
| R-F04 | A1 value Platform costs total | -33.4 | USD m | base | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.base.A1.by_asset.Platform costs.total` |
| R-F04 | A1 value by bucket contracted | 149.9 | USD m | base | 2021-12-09 | `valuations.base.A1.by_bucket.contracted` |
| R-F04 | A1 value by bucket hedged | 40.4 | USD m | base | 2021-12-09 | `valuations.base.A1.by_bucket.hedged` |
| R-F04 | A1 value by bucket merchant | 164.8 | USD m | base | 2021-12-09 | `valuations.base.A1.by_bucket.merchant` |
| R-F04 | A1 value before purchase-price tax shield | 355.1 | USD m | base | 2021-12-09 | `valuations.base.A1.pre_shield` |
| R-F04 | Tax shield at the price paid | 84.6 | USD m | base | 2021-12-09 | `valuations.base.A1.shield_at_price` |
| R-F04 | A1 enterprise value | 439.7 | USD m | base | 2021-12-09 | `valuations.base.A1.ev` |
| R-F04 | A1 price paid (calibrated, R-C04) | 446.3 | USD m | base | 2021-12-09 | `valuations.base.A1.price` |
| R-F04 | Value less price | -6.6 | USD m | base | 2021-12-09 | `valuations.base.A1.npv_vs_price` |
| R-F04 | Breakeven price | 438.2 | USD m | base | 2021-12-09 | `valuations.base.A1.breakeven_price` |
| R-F04 | A1 value R1 total | 51.5 | USD m | low | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.low.A1.by_asset.R1.total` |
| R-F04 | A1 value R2 total | 82.1 | USD m | low | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.low.A1.by_asset.R2.total` |
| R-F04 | A1 value R3 total | 64.3 | USD m | low | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.low.A1.by_asset.R3.total` |
| R-F04 | A1 value R4 total | 32.0 | USD m | low | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.low.A1.by_asset.R4.total` |
| R-F04 | A1 value R5 total | 51.7 | USD m | low | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.low.A1.by_asset.R5.total` |
| R-F04 | A1 value Platform costs total | -33.5 | USD m | low | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.low.A1.by_asset.Platform costs.total` |
| R-F04 | A1 value by bucket contracted | 149.1 | USD m | low | 2021-12-09 | `valuations.low.A1.by_bucket.contracted` |
| R-F04 | A1 value by bucket hedged | 39.7 | USD m | low | 2021-12-09 | `valuations.low.A1.by_bucket.hedged` |
| R-F04 | A1 value by bucket merchant | 59.4 | USD m | low | 2021-12-09 | `valuations.low.A1.by_bucket.merchant` |
| R-F04 | A1 value before purchase-price tax shield | 248.2 | USD m | low | 2021-12-09 | `valuations.low.A1.pre_shield` |
| R-F04 | Tax shield at the price paid | 84.6 | USD m | low | 2021-12-09 | `valuations.low.A1.shield_at_price` |
| R-F04 | A1 enterprise value | 332.8 | USD m | low | 2021-12-09 | `valuations.low.A1.ev` |
| R-F04 | A1 price paid (calibrated, R-C04) | 446.3 | USD m | low | 2021-12-09 | `valuations.low.A1.price` |
| R-F04 | Value less price | -113.5 | USD m | low | 2021-12-09 | `valuations.low.A1.npv_vs_price` |
| R-F04 | Breakeven price | 306.2 | USD m | low | 2021-12-09 | `valuations.low.A1.breakeven_price` |
| R-F04 | A1 value R1 total | 113.4 | USD m | high | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.high.A1.by_asset.R1.total` |
| R-F04 | A1 value R2 total | 167.0 | USD m | high | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.high.A1.by_asset.R2.total` |
| R-F04 | A1 value R3 total | 102.5 | USD m | high | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.high.A1.by_asset.R3.total` |
| R-F04 | A1 value R4 total | 63.2 | USD m | high | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.high.A1.by_asset.R4.total` |
| R-F04 | A1 value R5 total | 82.3 | USD m | high | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.high.A1.by_asset.R5.total` |
| R-F04 | A1 value Platform costs total | -33.3 | USD m | high | 2021-12-09 (bid), valued at 2022-03-22 | `valuations.high.A1.by_asset.Platform costs.total` |
| R-F04 | A1 value by bucket contracted | 150.5 | USD m | high | 2021-12-09 | `valuations.high.A1.by_bucket.contracted` |
| R-F04 | A1 value by bucket hedged | 41.2 | USD m | high | 2021-12-09 | `valuations.high.A1.by_bucket.hedged` |
| R-F04 | A1 value by bucket merchant | 303.5 | USD m | high | 2021-12-09 | `valuations.high.A1.by_bucket.merchant` |
| R-F04 | A1 value before purchase-price tax shield | 495.2 | USD m | high | 2021-12-09 | `valuations.high.A1.pre_shield` |
| R-F04 | Tax shield at the price paid | 84.6 | USD m | high | 2021-12-09 | `valuations.high.A1.shield_at_price` |
| R-F04 | A1 enterprise value | 579.8 | USD m | high | 2021-12-09 | `valuations.high.A1.ev` |
| R-F04 | A1 price paid (calibrated, R-C04) | 446.3 | USD m | high | 2021-12-09 | `valuations.high.A1.price` |
| R-F04 | Value less price | 133.5 | USD m | high | 2021-12-09 | `valuations.high.A1.npv_vs_price` |
| R-F04 | Breakeven price | 611.1 | USD m | high | 2021-12-09 | `valuations.high.A1.breakeven_price` |
| R-F05 | Uses: purchase price | 446.3 | USD m | base | 2022-03-22 | `scenarios.base.sources_uses.A1.price` |
| R-F05 | Uses: transaction costs | 14.9 | USD m | base | 2022-03-22 | `scenarios.base.sources_uses.A1.costs` |
| R-F05 | Uses: opco upfront fee | 4.9 | USD m | base | 2022-03-22 | `scenarios.base.sources_uses.A1.opco_fee` |
| R-F05 | Uses: holdco OID | 1.1 | USD m | base | 2022-03-22 | `scenarios.base.sources_uses.A1.holdco_oid` |
| R-F05 | Uses: total | 467.3 | USD m | base | 2022-03-22 | `scenarios.base.sources_uses.A1.uses` |
| R-F05 | Sources: opco term loan | 328.1 | USD m | base | 2022-03-22 | `scenarios.base.sources_uses.A1.opco_tl` |
| R-F05 | Sources: holdco TLB (face) | 57.3 | USD m | base | 2022-03-22 | `scenarios.base.sources_uses.A1.holdco_tlb` |
| R-F05 | Sources: fund equity | 81.9 | USD m | base | 2022-03-22 | `scenarios.base.sources_uses.A1.equity` |
| R-F05 | Opco TL capacity from contracted CFADS (PV) | 139.5 | USD m | base; P99 test | 2022-03-22 | `sizing.tl_pv_cap_contracted` |
| R-F05 | Opco TL capacity from hedged CFADS (PV) | 40.2 | USD m | base; P99 test | 2022-03-22 | `sizing.tl_pv_cap_hedged` |
| R-F05 | Opco TL capacity from merchant CFADS (PV) | 148.4 | USD m | base; P99 test | 2022-03-22 | `sizing.tl_pv_cap_merchant` |
| R-F05 | Opco term loan | 328.1 | USD m | base; P99 test | 2022-03-22 | `sizing.tl_debt` |
| R-F05 | Years the P99 test binds | 0 | years | base; P99 test | 2022-03-22 | `sizing.tl_p99_binds_years` |
| R-F05 | Holdco TLB supported by 1.75x coverage | 57.3 | USD m | base; P99 test | 2022-03-22 | `sizing.hc_face_cov` |
| R-F05 | Opco equity value (levered rates) | 147.0 | USD m | base; P99 test | 2022-03-22 | `sizing.opco_eq_val_2022` |
| R-F05 | Holdco cap at 45% of opco equity value | 66.1 | USD m | base; P99 test | 2022-03-22 | `sizing.hc_face_cap` |
| R-F05 | Holdco TLB face | 57.3 | USD m | base; P99 test | 2022-03-22 | `sizing.hc_face` |
| R-F05 | Holdco binding constraint | coverage | text | base; P99 test | 2022-03-22 | `sizing.hc_binding` |
| R-F05 | Opco TL sizing rate 2022 | 3.98% | % | base | 2022-03-22 | `sizing.tl_rate.0` |
| R-F05 | Opco TL sizing rate 2023 | 4.45% | % | base | 2022-03-22 | `sizing.tl_rate.1` |
| R-F05 | Opco TL sizing rate 2024 | 4.45% | % | base | 2022-03-22 | `sizing.tl_rate.2` |
| R-F05 | Opco TL sizing rate 2025 | 4.31% | % | base | 2022-03-22 | `sizing.tl_rate.3` |
| R-F05 | Gearing at A1 (opco TL / price) | 73.51% | % | base | 2022-03-22 | `derived.a1_opco_gearing_pct` |
| R-F05 | Total leverage at A1 ((opco TL + holdco) / price) | 86.34% | % | base | 2022-03-22 | `derived.a1_total_leverage_pct` |
| R-F06 | R1 generation 2022 | 664.5 | GWh | base | 2022 to 2030 | `scenarios.base.series.R1.gen.0` |
| R-F06 | R1 node capture ratio 2022 | 0.700 | ratio | base | 2022 to 2030 | `scenarios.base.series.R1.cap_node.0` |
| R-F06 | R1 realized node price 2022 | 50.55 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R1.node_price.0` |
| R-F06 | R1 revenue 2022 | 33.6 | USD m | base | 2022 to 2030 | `scenarios.base.series.R1.revenue.0` |
| R-F06 | R1 generation 2023 | 659.7 | GWh | base | 2022 to 2030 | `scenarios.base.series.R1.gen.1` |
| R-F06 | R1 node capture ratio 2023 | 0.694 | ratio | base | 2022 to 2030 | `scenarios.base.series.R1.cap_node.1` |
| R-F06 | R1 realized node price 2023 | 41.11 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R1.node_price.1` |
| R-F06 | R1 revenue 2023 | 23.3 | USD m | base | 2022 to 2030 | `scenarios.base.series.R1.revenue.1` |
| R-F06 | R1 generation 2024 | 654.9 | GWh | base | 2022 to 2030 | `scenarios.base.series.R1.gen.2` |
| R-F06 | R1 node capture ratio 2024 | 0.688 | ratio | base | 2022 to 2030 | `scenarios.base.series.R1.cap_node.2` |
| R-F06 | R1 realized node price 2024 | 20.05 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R1.node_price.2` |
| R-F06 | R1 revenue 2024 | 19.8 | USD m | base | 2022 to 2030 | `scenarios.base.series.R1.revenue.2` |
| R-F06 | R1 generation 2025 | 650.1 | GWh | base | 2022 to 2030 | `scenarios.base.series.R1.gen.3` |
| R-F06 | R1 node capture ratio 2025 | 0.682 | ratio | base | 2022 to 2030 | `scenarios.base.series.R1.cap_node.3` |
| R-F06 | R1 realized node price 2025 | 26.28 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R1.node_price.3` |
| R-F06 | R1 revenue 2025 | 20.5 | USD m | base | 2022 to 2030 | `scenarios.base.series.R1.revenue.3` |
| R-F06 | R1 generation 2026 | 648.8 | GWh | base | 2022 to 2030 | `scenarios.base.series.R1.gen.4` |
| R-F06 | R1 node capture ratio 2026 | 0.676 | ratio | base | 2022 to 2030 | `scenarios.base.series.R1.cap_node.4` |
| R-F06 | R1 realized node price 2026 | 29.18 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R1.node_price.4` |
| R-F06 | R1 revenue 2026 | 20.7 | USD m | base | 2022 to 2030 | `scenarios.base.series.R1.revenue.4` |
| R-F06 | R1 generation 2027 | 647.5 | GWh | base | 2022 to 2030 | `scenarios.base.series.R1.gen.5` |
| R-F06 | R1 node capture ratio 2027 | 0.670 | ratio | base | 2022 to 2030 | `scenarios.base.series.R1.cap_node.5` |
| R-F06 | R1 realized node price 2027 | 30.68 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R1.node_price.5` |
| R-F06 | R1 revenue 2027 | 20.7 | USD m | base | 2022 to 2030 | `scenarios.base.series.R1.revenue.5` |
| R-F06 | R1 generation 2028 | 646.2 | GWh | base | 2022 to 2030 | `scenarios.base.series.R1.gen.6` |
| R-F06 | R1 node capture ratio 2028 | 0.664 | ratio | base | 2022 to 2030 | `scenarios.base.series.R1.cap_node.6` |
| R-F06 | R1 realized node price 2028 | 31.56 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R1.node_price.6` |
| R-F06 | R1 revenue 2028 | 20.4 | USD m | base | 2022 to 2030 | `scenarios.base.series.R1.revenue.6` |
| R-F06 | R1 generation 2029 | 645.0 | GWh | base | 2022 to 2030 | `scenarios.base.series.R1.gen.7` |
| R-F06 | R1 node capture ratio 2029 | 0.658 | ratio | base | 2022 to 2030 | `scenarios.base.series.R1.cap_node.7` |
| R-F06 | R1 realized node price 2029 | 32.10 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R1.node_price.7` |
| R-F06 | R1 revenue 2029 | 20.7 | USD m | base | 2022 to 2030 | `scenarios.base.series.R1.revenue.7` |
| R-F06 | R1 generation 2030 | 643.7 | GWh | base | 2022 to 2030 | `scenarios.base.series.R1.gen.8` |
| R-F06 | R1 node capture ratio 2030 | 0.652 | ratio | base | 2022 to 2030 | `scenarios.base.series.R1.cap_node.8` |
| R-F06 | R1 realized node price 2030 | 32.69 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R1.node_price.8` |
| R-F06 | R1 revenue 2030 | 21.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R1.revenue.8` |
| R-F06 | R2 generation 2022 | 773.7 | GWh | base | 2022 to 2030 | `scenarios.base.series.R2.gen.0` |
| R-F06 | R2 node capture ratio 2022 | 0.910 | ratio | base | 2022 to 2030 | `scenarios.base.series.R2.cap_node.0` |
| R-F06 | R2 realized node price 2022 | 67.28 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R2.node_price.0` |
| R-F06 | R2 revenue 2022 | 24.3 | USD m | base | 2022 to 2030 | `scenarios.base.series.R2.revenue.0` |
| R-F06 | R2 generation 2023 | 772.2 | GWh | base | 2022 to 2030 | `scenarios.base.series.R2.gen.1` |
| R-F06 | R2 node capture ratio 2023 | 0.907 | ratio | base | 2022 to 2030 | `scenarios.base.series.R2.cap_node.1` |
| R-F06 | R2 realized node price 2023 | 55.01 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R2.node_price.1` |
| R-F06 | R2 revenue 2023 | 24.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.R2.revenue.1` |
| R-F06 | R2 generation 2024 | 770.6 | GWh | base | 2022 to 2030 | `scenarios.base.series.R2.gen.2` |
| R-F06 | R2 node capture ratio 2024 | 0.904 | ratio | base | 2022 to 2030 | `scenarios.base.series.R2.cap_node.2` |
| R-F06 | R2 realized node price 2024 | 26.97 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R2.node_price.2` |
| R-F06 | R2 revenue 2024 | 24.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.R2.revenue.2` |
| R-F06 | R2 generation 2025 | 769.1 | GWh | base | 2022 to 2030 | `scenarios.base.series.R2.gen.3` |
| R-F06 | R2 node capture ratio 2025 | 0.901 | ratio | base | 2022 to 2030 | `scenarios.base.series.R2.cap_node.3` |
| R-F06 | R2 realized node price 2025 | 35.54 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R2.node_price.3` |
| R-F06 | R2 revenue 2025 | 24.1 | USD m | base | 2022 to 2030 | `scenarios.base.series.R2.revenue.3` |
| R-F06 | R2 generation 2026 | 767.5 | GWh | base | 2022 to 2030 | `scenarios.base.series.R2.gen.4` |
| R-F06 | R2 node capture ratio 2026 | 0.898 | ratio | base | 2022 to 2030 | `scenarios.base.series.R2.cap_node.4` |
| R-F06 | R2 realized node price 2026 | 39.69 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R2.node_price.4` |
| R-F06 | R2 revenue 2026 | 24.1 | USD m | base | 2022 to 2030 | `scenarios.base.series.R2.revenue.4` |
| R-F06 | R2 generation 2027 | 766.0 | GWh | base | 2022 to 2030 | `scenarios.base.series.R2.gen.5` |
| R-F06 | R2 node capture ratio 2027 | 0.895 | ratio | base | 2022 to 2030 | `scenarios.base.series.R2.cap_node.5` |
| R-F06 | R2 realized node price 2027 | 41.95 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R2.node_price.5` |
| R-F06 | R2 revenue 2027 | 24.1 | USD m | base | 2022 to 2030 | `scenarios.base.series.R2.revenue.5` |
| R-F06 | R2 generation 2028 | 764.5 | GWh | base | 2022 to 2030 | `scenarios.base.series.R2.gen.6` |
| R-F06 | R2 node capture ratio 2028 | 0.892 | ratio | base | 2022 to 2030 | `scenarios.base.series.R2.cap_node.6` |
| R-F06 | R2 realized node price 2028 | 43.40 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R2.node_price.6` |
| R-F06 | R2 revenue 2028 | 24.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R2.revenue.6` |
| R-F06 | R2 generation 2029 | 763.0 | GWh | base | 2022 to 2030 | `scenarios.base.series.R2.gen.7` |
| R-F06 | R2 node capture ratio 2029 | 0.889 | ratio | base | 2022 to 2030 | `scenarios.base.series.R2.cap_node.7` |
| R-F06 | R2 realized node price 2029 | 44.40 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R2.node_price.7` |
| R-F06 | R2 revenue 2029 | 29.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R2.revenue.7` |
| R-F06 | R2 generation 2030 | 761.4 | GWh | base | 2022 to 2030 | `scenarios.base.series.R2.gen.8` |
| R-F06 | R2 node capture ratio 2030 | 0.886 | ratio | base | 2022 to 2030 | `scenarios.base.series.R2.cap_node.8` |
| R-F06 | R2 realized node price 2030 | 45.48 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R2.node_price.8` |
| R-F06 | R2 revenue 2030 | 34.6 | USD m | base | 2022 to 2030 | `scenarios.base.series.R2.revenue.8` |
| R-F06 | R3 generation 2022 | 587.0 | GWh | base | 2022 to 2030 | `scenarios.base.series.R3.gen.0` |
| R-F06 | R3 node capture ratio 2022 | 0.590 | ratio | base | 2022 to 2030 | `scenarios.base.series.R3.cap_node.0` |
| R-F06 | R3 realized node price 2022 | 42.61 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R3.node_price.0` |
| R-F06 | R3 revenue 2022 | 22.9 | USD m | base | 2022 to 2030 | `scenarios.base.series.R3.revenue.0` |
| R-F06 | R3 generation 2023 | 582.1 | GWh | base | 2022 to 2030 | `scenarios.base.series.R3.gen.1` |
| R-F06 | R3 node capture ratio 2023 | 0.585 | ratio | base | 2022 to 2030 | `scenarios.base.series.R3.cap_node.1` |
| R-F06 | R3 realized node price 2023 | 34.66 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R3.node_price.1` |
| R-F06 | R3 revenue 2023 | 23.4 | USD m | base | 2022 to 2030 | `scenarios.base.series.R3.revenue.1` |
| R-F06 | R3 generation 2024 | 577.3 | GWh | base | 2022 to 2030 | `scenarios.base.series.R3.gen.2` |
| R-F06 | R3 node capture ratio 2024 | 0.580 | ratio | base | 2022 to 2030 | `scenarios.base.series.R3.cap_node.2` |
| R-F06 | R3 realized node price 2024 | 16.90 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R3.node_price.2` |
| R-F06 | R3 revenue 2024 | 24.7 | USD m | base | 2022 to 2030 | `scenarios.base.series.R3.revenue.2` |
| R-F06 | R3 generation 2025 | 572.4 | GWh | base | 2022 to 2030 | `scenarios.base.series.R3.gen.3` |
| R-F06 | R3 node capture ratio 2025 | 0.575 | ratio | base | 2022 to 2030 | `scenarios.base.series.R3.cap_node.3` |
| R-F06 | R3 realized node price 2025 | 22.15 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R3.node_price.3` |
| R-F06 | R3 revenue 2025 | 24.3 | USD m | base | 2022 to 2030 | `scenarios.base.series.R3.revenue.3` |
| R-F06 | R3 generation 2026 | 571.3 | GWh | base | 2022 to 2030 | `scenarios.base.series.R3.gen.4` |
| R-F06 | R3 node capture ratio 2026 | 0.570 | ratio | base | 2022 to 2030 | `scenarios.base.series.R3.cap_node.4` |
| R-F06 | R3 realized node price 2026 | 24.61 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R3.node_price.4` |
| R-F06 | R3 revenue 2026 | 24.1 | USD m | base | 2022 to 2030 | `scenarios.base.series.R3.revenue.4` |
| R-F06 | R3 generation 2027 | 570.1 | GWh | base | 2022 to 2030 | `scenarios.base.series.R3.gen.5` |
| R-F06 | R3 node capture ratio 2027 | 0.565 | ratio | base | 2022 to 2030 | `scenarios.base.series.R3.cap_node.5` |
| R-F06 | R3 realized node price 2027 | 25.87 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R3.node_price.5` |
| R-F06 | R3 revenue 2027 | 24.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R3.revenue.5` |
| R-F06 | R3 generation 2028 | 569.0 | GWh | base | 2022 to 2030 | `scenarios.base.series.R3.gen.6` |
| R-F06 | R3 node capture ratio 2028 | 0.560 | ratio | base | 2022 to 2030 | `scenarios.base.series.R3.cap_node.6` |
| R-F06 | R3 realized node price 2028 | 26.62 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R3.node_price.6` |
| R-F06 | R3 revenue 2028 | 23.9 | USD m | base | 2022 to 2030 | `scenarios.base.series.R3.revenue.6` |
| R-F06 | R3 generation 2029 | 567.8 | GWh | base | 2022 to 2030 | `scenarios.base.series.R3.gen.7` |
| R-F06 | R3 node capture ratio 2029 | 0.555 | ratio | base | 2022 to 2030 | `scenarios.base.series.R3.cap_node.7` |
| R-F06 | R3 realized node price 2029 | 27.08 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R3.node_price.7` |
| R-F06 | R3 revenue 2029 | 23.9 | USD m | base | 2022 to 2030 | `scenarios.base.series.R3.revenue.7` |
| R-F06 | R3 generation 2030 | 566.7 | GWh | base | 2022 to 2030 | `scenarios.base.series.R3.gen.8` |
| R-F06 | R3 node capture ratio 2030 | 0.550 | ratio | base | 2022 to 2030 | `scenarios.base.series.R3.cap_node.8` |
| R-F06 | R3 realized node price 2030 | 27.58 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R3.node_price.8` |
| R-F06 | R3 revenue 2030 | 15.6 | USD m | base | 2022 to 2030 | `scenarios.base.series.R3.revenue.8` |
| R-F06 | R4 generation 2022 | 229.6 | GWh | base | 2022 to 2030 | `scenarios.base.series.R4.gen.0` |
| R-F06 | R4 node capture ratio 2022 | 0.830 | ratio | base | 2022 to 2030 | `scenarios.base.series.R4.cap_node.0` |
| R-F06 | R4 realized node price 2022 | 59.94 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R4.node_price.0` |
| R-F06 | R4 revenue 2022 | 10.7 | USD m | base | 2022 to 2030 | `scenarios.base.series.R4.revenue.0` |
| R-F06 | R4 generation 2023 | 227.4 | GWh | base | 2022 to 2030 | `scenarios.base.series.R4.gen.1` |
| R-F06 | R4 node capture ratio 2023 | 0.810 | ratio | base | 2022 to 2030 | `scenarios.base.series.R4.cap_node.1` |
| R-F06 | R4 realized node price 2023 | 47.99 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R4.node_price.1` |
| R-F06 | R4 revenue 2023 | 10.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R4.revenue.1` |
| R-F06 | R4 generation 2024 | 225.2 | GWh | base | 2022 to 2030 | `scenarios.base.series.R4.gen.2` |
| R-F06 | R4 node capture ratio 2024 | 0.790 | ratio | base | 2022 to 2030 | `scenarios.base.series.R4.cap_node.2` |
| R-F06 | R4 realized node price 2024 | 23.02 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R4.node_price.2` |
| R-F06 | R4 revenue 2024 | 8.6 | USD m | base | 2022 to 2030 | `scenarios.base.series.R4.revenue.2` |
| R-F06 | R4 generation 2025 | 223.1 | GWh | base | 2022 to 2030 | `scenarios.base.series.R4.gen.3` |
| R-F06 | R4 node capture ratio 2025 | 0.770 | ratio | base | 2022 to 2030 | `scenarios.base.series.R4.cap_node.3` |
| R-F06 | R4 realized node price 2025 | 29.67 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R4.node_price.3` |
| R-F06 | R4 revenue 2025 | 8.9 | USD m | base | 2022 to 2030 | `scenarios.base.series.R4.revenue.3` |
| R-F06 | R4 generation 2026 | 222.1 | GWh | base | 2022 to 2030 | `scenarios.base.series.R4.gen.4` |
| R-F06 | R4 node capture ratio 2026 | 0.750 | ratio | base | 2022 to 2030 | `scenarios.base.series.R4.cap_node.4` |
| R-F06 | R4 realized node price 2026 | 32.38 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R4.node_price.4` |
| R-F06 | R4 revenue 2026 | 8.9 | USD m | base | 2022 to 2030 | `scenarios.base.series.R4.revenue.4` |
| R-F06 | R4 generation 2027 | 221.1 | GWh | base | 2022 to 2030 | `scenarios.base.series.R4.gen.5` |
| R-F06 | R4 node capture ratio 2027 | 0.730 | ratio | base | 2022 to 2030 | `scenarios.base.series.R4.cap_node.5` |
| R-F06 | R4 realized node price 2027 | 33.42 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R4.node_price.5` |
| R-F06 | R4 revenue 2027 | 7.4 | USD m | base | 2022 to 2030 | `scenarios.base.series.R4.revenue.5` |
| R-F06 | R4 generation 2028 | 220.1 | GWh | base | 2022 to 2030 | `scenarios.base.series.R4.gen.6` |
| R-F06 | R4 node capture ratio 2028 | 0.710 | ratio | base | 2022 to 2030 | `scenarios.base.series.R4.cap_node.6` |
| R-F06 | R4 realized node price 2028 | 33.75 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R4.node_price.6` |
| R-F06 | R4 revenue 2028 | 7.4 | USD m | base | 2022 to 2030 | `scenarios.base.series.R4.revenue.6` |
| R-F06 | R4 generation 2029 | 219.1 | GWh | base | 2022 to 2030 | `scenarios.base.series.R4.gen.7` |
| R-F06 | R4 node capture ratio 2029 | 0.690 | ratio | base | 2022 to 2030 | `scenarios.base.series.R4.cap_node.7` |
| R-F06 | R4 realized node price 2029 | 33.66 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R4.node_price.7` |
| R-F06 | R4 revenue 2029 | 7.4 | USD m | base | 2022 to 2030 | `scenarios.base.series.R4.revenue.7` |
| R-F06 | R4 generation 2030 | 218.1 | GWh | base | 2022 to 2030 | `scenarios.base.series.R4.gen.8` |
| R-F06 | R4 node capture ratio 2030 | 0.670 | ratio | base | 2022 to 2030 | `scenarios.base.series.R4.cap_node.8` |
| R-F06 | R4 realized node price 2030 | 33.60 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R4.node_price.8` |
| R-F06 | R4 revenue 2030 | 7.3 | USD m | base | 2022 to 2030 | `scenarios.base.series.R4.revenue.8` |
| R-F06 | R5 generation 2022 | 443.2 | GWh | base | 2022 to 2030 | `scenarios.base.series.R5.gen.0` |
| R-F06 | R5 node capture ratio 2022 | 0.830 | ratio | base | 2022 to 2030 | `scenarios.base.series.R5.cap_node.0` |
| R-F06 | R5 realized node price 2022 | 59.94 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R5.node_price.0` |
| R-F06 | R5 revenue 2022 | 11.4 | USD m | base | 2022 to 2030 | `scenarios.base.series.R5.revenue.0` |
| R-F06 | R5 generation 2023 | 438.9 | GWh | base | 2022 to 2030 | `scenarios.base.series.R5.gen.1` |
| R-F06 | R5 node capture ratio 2023 | 0.810 | ratio | base | 2022 to 2030 | `scenarios.base.series.R5.cap_node.1` |
| R-F06 | R5 realized node price 2023 | 47.99 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R5.node_price.1` |
| R-F06 | R5 revenue 2023 | 11.4 | USD m | base | 2022 to 2030 | `scenarios.base.series.R5.revenue.1` |
| R-F06 | R5 generation 2024 | 434.7 | GWh | base | 2022 to 2030 | `scenarios.base.series.R5.gen.2` |
| R-F06 | R5 node capture ratio 2024 | 0.790 | ratio | base | 2022 to 2030 | `scenarios.base.series.R5.cap_node.2` |
| R-F06 | R5 realized node price 2024 | 23.02 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R5.node_price.2` |
| R-F06 | R5 revenue 2024 | 11.7 | USD m | base | 2022 to 2030 | `scenarios.base.series.R5.revenue.2` |
| R-F06 | R5 generation 2025 | 430.5 | GWh | base | 2022 to 2030 | `scenarios.base.series.R5.gen.3` |
| R-F06 | R5 node capture ratio 2025 | 0.770 | ratio | base | 2022 to 2030 | `scenarios.base.series.R5.cap_node.3` |
| R-F06 | R5 realized node price 2025 | 29.67 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R5.node_price.3` |
| R-F06 | R5 revenue 2025 | 11.5 | USD m | base | 2022 to 2030 | `scenarios.base.series.R5.revenue.3` |
| R-F06 | R5 generation 2026 | 428.6 | GWh | base | 2022 to 2030 | `scenarios.base.series.R5.gen.4` |
| R-F06 | R5 node capture ratio 2026 | 0.750 | ratio | base | 2022 to 2030 | `scenarios.base.series.R5.cap_node.4` |
| R-F06 | R5 realized node price 2026 | 32.38 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R5.node_price.4` |
| R-F06 | R5 revenue 2026 | 11.4 | USD m | base | 2022 to 2030 | `scenarios.base.series.R5.revenue.4` |
| R-F06 | R5 generation 2027 | 426.6 | GWh | base | 2022 to 2030 | `scenarios.base.series.R5.gen.5` |
| R-F06 | R5 node capture ratio 2027 | 0.730 | ratio | base | 2022 to 2030 | `scenarios.base.series.R5.cap_node.5` |
| R-F06 | R5 realized node price 2027 | 33.42 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R5.node_price.5` |
| R-F06 | R5 revenue 2027 | 11.3 | USD m | base | 2022 to 2030 | `scenarios.base.series.R5.revenue.5` |
| R-F06 | R5 generation 2028 | 424.7 | GWh | base | 2022 to 2030 | `scenarios.base.series.R5.gen.6` |
| R-F06 | R5 node capture ratio 2028 | 0.710 | ratio | base | 2022 to 2030 | `scenarios.base.series.R5.cap_node.6` |
| R-F06 | R5 realized node price 2028 | 33.75 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R5.node_price.6` |
| R-F06 | R5 revenue 2028 | 11.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.R5.revenue.6` |
| R-F06 | R5 generation 2029 | 422.8 | GWh | base | 2022 to 2030 | `scenarios.base.series.R5.gen.7` |
| R-F06 | R5 node capture ratio 2029 | 0.690 | ratio | base | 2022 to 2030 | `scenarios.base.series.R5.cap_node.7` |
| R-F06 | R5 realized node price 2029 | 33.66 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R5.node_price.7` |
| R-F06 | R5 revenue 2029 | 11.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.R5.revenue.7` |
| R-F06 | R5 generation 2030 | 420.9 | GWh | base | 2022 to 2030 | `scenarios.base.series.R5.gen.8` |
| R-F06 | R5 node capture ratio 2030 | 0.670 | ratio | base | 2022 to 2030 | `scenarios.base.series.R5.cap_node.8` |
| R-F06 | R5 realized node price 2030 | 33.60 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R5.node_price.8` |
| R-F06 | R5 revenue 2030 | 11.1 | USD m | base | 2022 to 2030 | `scenarios.base.series.R5.revenue.8` |
| R-F06 | R6 revenue 2022 | 0.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R6.revenue.0` |
| R-F06 | R6 revenue 2023 | 5.1 | USD m | base | 2022 to 2030 | `scenarios.base.series.R6.revenue.1` |
| R-F06 | R6 revenue 2024 | 11.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R6.revenue.2` |
| R-F06 | R6 revenue 2025 | 11.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R6.revenue.3` |
| R-F06 | R6 revenue 2026 | 11.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R6.revenue.4` |
| R-F06 | R6 revenue 2027 | 11.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R6.revenue.5` |
| R-F06 | R6 revenue 2028 | 11.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R6.revenue.6` |
| R-F06 | R6 revenue 2029 | 11.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R6.revenue.7` |
| R-F06 | R6 revenue 2030 | 8.6 | USD m | base | 2022 to 2030 | `scenarios.base.series.R6.revenue.8` |
| R-F06 | R7 revenue 2022 | 0.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R7.revenue.0` |
| R-F06 | R7 revenue 2023 | 0.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R7.revenue.1` |
| R-F06 | R7 revenue 2024 | 7.6 | USD m | base | 2022 to 2030 | `scenarios.base.series.R7.revenue.2` |
| R-F06 | R7 revenue 2025 | 10.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.R7.revenue.3` |
| R-F06 | R7 revenue 2026 | 10.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.R7.revenue.4` |
| R-F06 | R7 revenue 2027 | 10.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.R7.revenue.5` |
| R-F06 | R7 revenue 2028 | 10.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.R7.revenue.6` |
| R-F06 | R7 revenue 2029 | 10.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.R7.revenue.7` |
| R-F06 | R7 revenue 2030 | 10.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.R7.revenue.8` |
| R-F06 | R8 generation 2022 | 0.0 | GWh | base | 2022 to 2030 | `scenarios.base.series.R8.gen.0` |
| R-F06 | R8 node capture ratio 2022 | 0.880 | ratio | base | 2022 to 2030 | `scenarios.base.series.R8.cap_node.0` |
| R-F06 | R8 realized node price 2022 | 65.06 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R8.node_price.0` |
| R-F06 | R8 revenue 2022 | 0.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R8.revenue.0` |
| R-F06 | R8 generation 2023 | 0.0 | GWh | base | 2022 to 2030 | `scenarios.base.series.R8.gen.1` |
| R-F06 | R8 node capture ratio 2023 | 0.862 | ratio | base | 2022 to 2030 | `scenarios.base.series.R8.cap_node.1` |
| R-F06 | R8 realized node price 2023 | 52.28 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R8.node_price.1` |
| R-F06 | R8 revenue 2023 | 0.0 | USD m | base | 2022 to 2030 | `scenarios.base.series.R8.revenue.1` |
| R-F06 | R8 generation 2024 | 9.3 | GWh | base | 2022 to 2030 | `scenarios.base.series.R8.gen.2` |
| R-F06 | R8 node capture ratio 2024 | 0.844 | ratio | base | 2022 to 2030 | `scenarios.base.series.R8.cap_node.2` |
| R-F06 | R8 realized node price 2024 | 25.18 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R8.node_price.2` |
| R-F06 | R8 revenue 2024 | 0.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.R8.revenue.2` |
| R-F06 | R8 generation 2025 | 284.9 | GWh | base | 2022 to 2030 | `scenarios.base.series.R8.gen.3` |
| R-F06 | R8 node capture ratio 2025 | 0.826 | ratio | base | 2022 to 2030 | `scenarios.base.series.R8.cap_node.3` |
| R-F06 | R8 realized node price 2025 | 32.58 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R8.node_price.3` |
| R-F06 | R8 revenue 2025 | 10.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.R8.revenue.3` |
| R-F06 | R8 generation 2026 | 283.7 | GWh | base | 2022 to 2030 | `scenarios.base.series.R8.gen.4` |
| R-F06 | R8 node capture ratio 2026 | 0.808 | ratio | base | 2022 to 2030 | `scenarios.base.series.R8.cap_node.4` |
| R-F06 | R8 realized node price 2026 | 35.71 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R8.node_price.4` |
| R-F06 | R8 revenue 2026 | 10.5 | USD m | base | 2022 to 2030 | `scenarios.base.series.R8.revenue.4` |
| R-F06 | R8 generation 2027 | 282.6 | GWh | base | 2022 to 2030 | `scenarios.base.series.R8.gen.5` |
| R-F06 | R8 node capture ratio 2027 | 0.790 | ratio | base | 2022 to 2030 | `scenarios.base.series.R8.cap_node.5` |
| R-F06 | R8 realized node price 2027 | 37.03 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R8.node_price.5` |
| R-F06 | R8 revenue 2027 | 10.6 | USD m | base | 2022 to 2030 | `scenarios.base.series.R8.revenue.5` |
| R-F06 | R8 generation 2028 | 281.5 | GWh | base | 2022 to 2030 | `scenarios.base.series.R8.gen.6` |
| R-F06 | R8 node capture ratio 2028 | 0.772 | ratio | base | 2022 to 2030 | `scenarios.base.series.R8.cap_node.6` |
| R-F06 | R8 realized node price 2028 | 37.56 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R8.node_price.6` |
| R-F06 | R8 revenue 2028 | 10.6 | USD m | base | 2022 to 2030 | `scenarios.base.series.R8.revenue.6` |
| R-F06 | R8 generation 2029 | 280.3 | GWh | base | 2022 to 2030 | `scenarios.base.series.R8.gen.7` |
| R-F06 | R8 node capture ratio 2029 | 0.754 | ratio | base | 2022 to 2030 | `scenarios.base.series.R8.cap_node.7` |
| R-F06 | R8 realized node price 2029 | 37.66 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R8.node_price.7` |
| R-F06 | R8 revenue 2029 | 10.6 | USD m | base | 2022 to 2030 | `scenarios.base.series.R8.revenue.7` |
| R-F06 | R8 generation 2030 | 279.2 | GWh | base | 2022 to 2030 | `scenarios.base.series.R8.gen.8` |
| R-F06 | R8 node capture ratio 2030 | 0.736 | ratio | base | 2022 to 2030 | `scenarios.base.series.R8.cap_node.8` |
| R-F06 | R8 realized node price 2030 | 37.78 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.R8.node_price.8` |
| R-F06 | R8 revenue 2030 | 10.6 | USD m | base | 2022 to 2030 | `scenarios.base.series.R8.revenue.8` |
| R-F06 | West Hub ATC 2022 | 72.21 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.portfolio.west_atc.0` |
| R-F06 | Portfolio CFADS (Mesa share) 2022 | 45.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.portfolio.cfads_all.0` |
| R-F06 | West Hub ATC 2023 | 59.24 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.portfolio.west_atc.1` |
| R-F06 | Portfolio CFADS (Mesa share) 2023 | 49.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.portfolio.cfads_all.1` |
| R-F06 | West Hub ATC 2024 | 29.14 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.portfolio.west_atc.2` |
| R-F06 | Portfolio CFADS (Mesa share) 2024 | 56.8 | USD m | base | 2022 to 2030 | `scenarios.base.series.portfolio.cfads_all.2` |
| R-F06 | West Hub ATC 2025 | 38.53 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.portfolio.west_atc.3` |
| R-F06 | Portfolio CFADS (Mesa share) 2025 | 65.9 | USD m | base | 2022 to 2030 | `scenarios.base.series.portfolio.cfads_all.3` |
| R-F06 | West Hub ATC 2026 | 43.17 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.portfolio.west_atc.4` |
| R-F06 | Portfolio CFADS (Mesa share) 2026 | 65.3 | USD m | base | 2022 to 2030 | `scenarios.base.series.portfolio.cfads_all.4` |
| R-F06 | West Hub ATC 2027 | 45.79 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.portfolio.west_atc.5` |
| R-F06 | Portfolio CFADS (Mesa share) 2027 | 63.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.portfolio.cfads_all.5` |
| R-F06 | West Hub ATC 2028 | 47.53 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.portfolio.west_atc.6` |
| R-F06 | Portfolio CFADS (Mesa share) 2028 | 61.7 | USD m | base | 2022 to 2030 | `scenarios.base.series.portfolio.cfads_all.6` |
| R-F06 | West Hub ATC 2029 | 48.79 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.portfolio.west_atc.7` |
| R-F06 | Portfolio CFADS (Mesa share) 2029 | 65.2 | USD m | base | 2022 to 2030 | `scenarios.base.series.portfolio.cfads_all.7` |
| R-F06 | West Hub ATC 2030 | 50.14 | USD/MWh | base | 2022 to 2030 | `scenarios.base.series.portfolio.west_atc.8` |
| R-F06 | Portfolio CFADS (Mesa share) 2030 | 66.1 | USD m | base | 2022 to 2030 | `scenarios.base.series.portfolio.cfads_all.8` |
| R-F06 | R1 generation 2022 | 664.5 | GWh | low | 2022 to 2030 | `scenarios.low.series.R1.gen.0` |
| R-F06 | R1 node capture ratio 2022 | 0.700 | ratio | low | 2022 to 2030 | `scenarios.low.series.R1.cap_node.0` |
| R-F06 | R1 realized node price 2022 | 50.55 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R1.node_price.0` |
| R-F06 | R1 revenue 2022 | 33.6 | USD m | low | 2022 to 2030 | `scenarios.low.series.R1.revenue.0` |
| R-F06 | R1 generation 2023 | 659.7 | GWh | low | 2022 to 2030 | `scenarios.low.series.R1.gen.1` |
| R-F06 | R1 node capture ratio 2023 | 0.691 | ratio | low | 2022 to 2030 | `scenarios.low.series.R1.cap_node.1` |
| R-F06 | R1 realized node price 2023 | 40.94 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R1.node_price.1` |
| R-F06 | R1 revenue 2023 | 23.2 | USD m | low | 2022 to 2030 | `scenarios.low.series.R1.revenue.1` |
| R-F06 | R1 generation 2024 | 654.9 | GWh | low | 2022 to 2030 | `scenarios.low.series.R1.gen.2` |
| R-F06 | R1 node capture ratio 2024 | 0.682 | ratio | low | 2022 to 2030 | `scenarios.low.series.R1.cap_node.2` |
| R-F06 | R1 realized node price 2024 | 19.87 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R1.node_price.2` |
| R-F06 | R1 revenue 2024 | 19.7 | USD m | low | 2022 to 2030 | `scenarios.low.series.R1.revenue.2` |
| R-F06 | R1 generation 2025 | 650.1 | GWh | low | 2022 to 2030 | `scenarios.low.series.R1.gen.3` |
| R-F06 | R1 node capture ratio 2025 | 0.673 | ratio | low | 2022 to 2030 | `scenarios.low.series.R1.cap_node.3` |
| R-F06 | R1 realized node price 2025 | 25.93 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R1.node_price.3` |
| R-F06 | R1 revenue 2025 | 20.3 | USD m | low | 2022 to 2030 | `scenarios.low.series.R1.revenue.3` |
| R-F06 | R1 generation 2026 | 648.8 | GWh | low | 2022 to 2030 | `scenarios.low.series.R1.gen.4` |
| R-F06 | R1 node capture ratio 2026 | 0.664 | ratio | low | 2022 to 2030 | `scenarios.low.series.R1.cap_node.4` |
| R-F06 | R1 realized node price 2026 | 22.62 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R1.node_price.4` |
| R-F06 | R1 revenue 2026 | 19.6 | USD m | low | 2022 to 2030 | `scenarios.low.series.R1.revenue.4` |
| R-F06 | R1 generation 2027 | 647.5 | GWh | low | 2022 to 2030 | `scenarios.low.series.R1.gen.5` |
| R-F06 | R1 node capture ratio 2027 | 0.655 | ratio | low | 2022 to 2030 | `scenarios.low.series.R1.cap_node.5` |
| R-F06 | R1 realized node price 2027 | 23.08 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R1.node_price.5` |
| R-F06 | R1 revenue 2027 | 19.5 | USD m | low | 2022 to 2030 | `scenarios.low.series.R1.revenue.5` |
| R-F06 | R1 generation 2028 | 646.2 | GWh | low | 2022 to 2030 | `scenarios.low.series.R1.gen.6` |
| R-F06 | R1 node capture ratio 2028 | 0.646 | ratio | low | 2022 to 2030 | `scenarios.low.series.R1.cap_node.6` |
| R-F06 | R1 realized node price 2028 | 23.32 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R1.node_price.6` |
| R-F06 | R1 revenue 2028 | 15.1 | USD m | low | 2022 to 2030 | `scenarios.low.series.R1.revenue.6` |
| R-F06 | R1 generation 2029 | 645.0 | GWh | low | 2022 to 2030 | `scenarios.low.series.R1.gen.7` |
| R-F06 | R1 node capture ratio 2029 | 0.637 | ratio | low | 2022 to 2030 | `scenarios.low.series.R1.cap_node.7` |
| R-F06 | R1 realized node price 2029 | 23.43 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R1.node_price.7` |
| R-F06 | R1 revenue 2029 | 15.1 | USD m | low | 2022 to 2030 | `scenarios.low.series.R1.revenue.7` |
| R-F06 | R1 generation 2030 | 643.7 | GWh | low | 2022 to 2030 | `scenarios.low.series.R1.gen.8` |
| R-F06 | R1 node capture ratio 2030 | 0.628 | ratio | low | 2022 to 2030 | `scenarios.low.series.R1.cap_node.8` |
| R-F06 | R1 realized node price 2030 | 23.47 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R1.node_price.8` |
| R-F06 | R1 revenue 2030 | 15.1 | USD m | low | 2022 to 2030 | `scenarios.low.series.R1.revenue.8` |
| R-F06 | R2 generation 2022 | 773.7 | GWh | low | 2022 to 2030 | `scenarios.low.series.R2.gen.0` |
| R-F06 | R2 node capture ratio 2022 | 0.910 | ratio | low | 2022 to 2030 | `scenarios.low.series.R2.cap_node.0` |
| R-F06 | R2 realized node price 2022 | 67.28 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R2.node_price.0` |
| R-F06 | R2 revenue 2022 | 24.3 | USD m | low | 2022 to 2030 | `scenarios.low.series.R2.revenue.0` |
| R-F06 | R2 generation 2023 | 772.2 | GWh | low | 2022 to 2030 | `scenarios.low.series.R2.gen.1` |
| R-F06 | R2 node capture ratio 2023 | 0.905 | ratio | low | 2022 to 2030 | `scenarios.low.series.R2.cap_node.1` |
| R-F06 | R2 realized node price 2023 | 54.92 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R2.node_price.1` |
| R-F06 | R2 revenue 2023 | 24.2 | USD m | low | 2022 to 2030 | `scenarios.low.series.R2.revenue.1` |
| R-F06 | R2 generation 2024 | 770.6 | GWh | low | 2022 to 2030 | `scenarios.low.series.R2.gen.2` |
| R-F06 | R2 node capture ratio 2024 | 0.901 | ratio | low | 2022 to 2030 | `scenarios.low.series.R2.cap_node.2` |
| R-F06 | R2 realized node price 2024 | 26.88 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R2.node_price.2` |
| R-F06 | R2 revenue 2024 | 24.2 | USD m | low | 2022 to 2030 | `scenarios.low.series.R2.revenue.2` |
| R-F06 | R2 generation 2025 | 769.1 | GWh | low | 2022 to 2030 | `scenarios.low.series.R2.gen.3` |
| R-F06 | R2 node capture ratio 2025 | 0.896 | ratio | low | 2022 to 2030 | `scenarios.low.series.R2.cap_node.3` |
| R-F06 | R2 realized node price 2025 | 35.36 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R2.node_price.3` |
| R-F06 | R2 revenue 2025 | 24.1 | USD m | low | 2022 to 2030 | `scenarios.low.series.R2.revenue.3` |
| R-F06 | R2 generation 2026 | 767.5 | GWh | low | 2022 to 2030 | `scenarios.low.series.R2.gen.4` |
| R-F06 | R2 node capture ratio 2026 | 0.892 | ratio | low | 2022 to 2030 | `scenarios.low.series.R2.cap_node.4` |
| R-F06 | R2 realized node price 2026 | 31.12 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R2.node_price.4` |
| R-F06 | R2 revenue 2026 | 24.1 | USD m | low | 2022 to 2030 | `scenarios.low.series.R2.revenue.4` |
| R-F06 | R2 generation 2027 | 766.0 | GWh | low | 2022 to 2030 | `scenarios.low.series.R2.gen.5` |
| R-F06 | R2 node capture ratio 2027 | 0.887 | ratio | low | 2022 to 2030 | `scenarios.low.series.R2.cap_node.5` |
| R-F06 | R2 realized node price 2027 | 32.01 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R2.node_price.5` |
| R-F06 | R2 revenue 2027 | 24.1 | USD m | low | 2022 to 2030 | `scenarios.low.series.R2.revenue.5` |
| R-F06 | R2 generation 2028 | 764.5 | GWh | low | 2022 to 2030 | `scenarios.low.series.R2.gen.6` |
| R-F06 | R2 node capture ratio 2028 | 0.883 | ratio | low | 2022 to 2030 | `scenarios.low.series.R2.cap_node.6` |
| R-F06 | R2 realized node price 2028 | 32.64 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R2.node_price.6` |
| R-F06 | R2 revenue 2028 | 24.0 | USD m | low | 2022 to 2030 | `scenarios.low.series.R2.revenue.6` |
| R-F06 | R2 generation 2029 | 763.0 | GWh | low | 2022 to 2030 | `scenarios.low.series.R2.gen.7` |
| R-F06 | R2 node capture ratio 2029 | 0.878 | ratio | low | 2022 to 2030 | `scenarios.low.series.R2.cap_node.7` |
| R-F06 | R2 realized node price 2029 | 33.08 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R2.node_price.7` |
| R-F06 | R2 revenue 2029 | 24.6 | USD m | low | 2022 to 2030 | `scenarios.low.series.R2.revenue.7` |
| R-F06 | R2 generation 2030 | 761.4 | GWh | low | 2022 to 2030 | `scenarios.low.series.R2.gen.8` |
| R-F06 | R2 node capture ratio 2030 | 0.874 | ratio | low | 2022 to 2030 | `scenarios.low.series.R2.cap_node.8` |
| R-F06 | R2 realized node price 2030 | 33.43 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R2.node_price.8` |
| R-F06 | R2 revenue 2030 | 25.5 | USD m | low | 2022 to 2030 | `scenarios.low.series.R2.revenue.8` |
| R-F06 | R3 generation 2022 | 587.0 | GWh | low | 2022 to 2030 | `scenarios.low.series.R3.gen.0` |
| R-F06 | R3 node capture ratio 2022 | 0.590 | ratio | low | 2022 to 2030 | `scenarios.low.series.R3.cap_node.0` |
| R-F06 | R3 realized node price 2022 | 42.61 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R3.node_price.0` |
| R-F06 | R3 revenue 2022 | 22.9 | USD m | low | 2022 to 2030 | `scenarios.low.series.R3.revenue.0` |
| R-F06 | R3 generation 2023 | 582.1 | GWh | low | 2022 to 2030 | `scenarios.low.series.R3.gen.1` |
| R-F06 | R3 node capture ratio 2023 | 0.583 | ratio | low | 2022 to 2030 | `scenarios.low.series.R3.cap_node.1` |
| R-F06 | R3 realized node price 2023 | 34.51 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R3.node_price.1` |
| R-F06 | R3 revenue 2023 | 23.4 | USD m | low | 2022 to 2030 | `scenarios.low.series.R3.revenue.1` |
| R-F06 | R3 generation 2024 | 577.3 | GWh | low | 2022 to 2030 | `scenarios.low.series.R3.gen.2` |
| R-F06 | R3 node capture ratio 2024 | 0.575 | ratio | low | 2022 to 2030 | `scenarios.low.series.R3.cap_node.2` |
| R-F06 | R3 realized node price 2024 | 16.75 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R3.node_price.2` |
| R-F06 | R3 revenue 2024 | 24.7 | USD m | low | 2022 to 2030 | `scenarios.low.series.R3.revenue.2` |
| R-F06 | R3 generation 2025 | 572.4 | GWh | low | 2022 to 2030 | `scenarios.low.series.R3.gen.3` |
| R-F06 | R3 node capture ratio 2025 | 0.568 | ratio | low | 2022 to 2030 | `scenarios.low.series.R3.cap_node.3` |
| R-F06 | R3 realized node price 2025 | 21.86 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R3.node_price.3` |
| R-F06 | R3 revenue 2025 | 24.3 | USD m | low | 2022 to 2030 | `scenarios.low.series.R3.revenue.3` |
| R-F06 | R3 generation 2026 | 571.3 | GWh | low | 2022 to 2030 | `scenarios.low.series.R3.gen.4` |
| R-F06 | R3 node capture ratio 2026 | 0.560 | ratio | low | 2022 to 2030 | `scenarios.low.series.R3.cap_node.4` |
| R-F06 | R3 realized node price 2026 | 19.08 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R3.node_price.4` |
| R-F06 | R3 revenue 2026 | 24.5 | USD m | low | 2022 to 2030 | `scenarios.low.series.R3.revenue.4` |
| R-F06 | R3 generation 2027 | 570.1 | GWh | low | 2022 to 2030 | `scenarios.low.series.R3.gen.5` |
| R-F06 | R3 node capture ratio 2027 | 0.552 | ratio | low | 2022 to 2030 | `scenarios.low.series.R3.cap_node.5` |
| R-F06 | R3 realized node price 2027 | 19.47 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R3.node_price.5` |
| R-F06 | R3 revenue 2027 | 24.4 | USD m | low | 2022 to 2030 | `scenarios.low.series.R3.revenue.5` |
| R-F06 | R3 generation 2028 | 569.0 | GWh | low | 2022 to 2030 | `scenarios.low.series.R3.gen.6` |
| R-F06 | R3 node capture ratio 2028 | 0.545 | ratio | low | 2022 to 2030 | `scenarios.low.series.R3.cap_node.6` |
| R-F06 | R3 realized node price 2028 | 19.68 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R3.node_price.6` |
| R-F06 | R3 revenue 2028 | 24.4 | USD m | low | 2022 to 2030 | `scenarios.low.series.R3.revenue.6` |
| R-F06 | R3 generation 2029 | 567.8 | GWh | low | 2022 to 2030 | `scenarios.low.series.R3.gen.7` |
| R-F06 | R3 node capture ratio 2029 | 0.537 | ratio | low | 2022 to 2030 | `scenarios.low.series.R3.cap_node.7` |
| R-F06 | R3 realized node price 2029 | 19.77 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R3.node_price.7` |
| R-F06 | R3 revenue 2029 | 24.4 | USD m | low | 2022 to 2030 | `scenarios.low.series.R3.revenue.7` |
| R-F06 | R3 generation 2030 | 566.7 | GWh | low | 2022 to 2030 | `scenarios.low.series.R3.gen.8` |
| R-F06 | R3 node capture ratio 2030 | 0.530 | ratio | low | 2022 to 2030 | `scenarios.low.series.R3.cap_node.8` |
| R-F06 | R3 realized node price 2030 | 19.80 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R3.node_price.8` |
| R-F06 | R3 revenue 2030 | 11.2 | USD m | low | 2022 to 2030 | `scenarios.low.series.R3.revenue.8` |
| R-F06 | R4 generation 2022 | 229.6 | GWh | low | 2022 to 2030 | `scenarios.low.series.R4.gen.0` |
| R-F06 | R4 node capture ratio 2022 | 0.830 | ratio | low | 2022 to 2030 | `scenarios.low.series.R4.cap_node.0` |
| R-F06 | R4 realized node price 2022 | 59.94 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R4.node_price.0` |
| R-F06 | R4 revenue 2022 | 10.7 | USD m | low | 2022 to 2030 | `scenarios.low.series.R4.revenue.0` |
| R-F06 | R4 generation 2023 | 227.4 | GWh | low | 2022 to 2030 | `scenarios.low.series.R4.gen.1` |
| R-F06 | R4 node capture ratio 2023 | 0.800 | ratio | low | 2022 to 2030 | `scenarios.low.series.R4.cap_node.1` |
| R-F06 | R4 realized node price 2023 | 47.39 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R4.node_price.1` |
| R-F06 | R4 revenue 2023 | 9.9 | USD m | low | 2022 to 2030 | `scenarios.low.series.R4.revenue.1` |
| R-F06 | R4 generation 2024 | 225.2 | GWh | low | 2022 to 2030 | `scenarios.low.series.R4.gen.2` |
| R-F06 | R4 node capture ratio 2024 | 0.770 | ratio | low | 2022 to 2030 | `scenarios.low.series.R4.cap_node.2` |
| R-F06 | R4 realized node price 2024 | 22.44 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R4.node_price.2` |
| R-F06 | R4 revenue 2024 | 8.6 | USD m | low | 2022 to 2030 | `scenarios.low.series.R4.revenue.2` |
| R-F06 | R4 generation 2025 | 223.1 | GWh | low | 2022 to 2030 | `scenarios.low.series.R4.gen.3` |
| R-F06 | R4 node capture ratio 2025 | 0.740 | ratio | low | 2022 to 2030 | `scenarios.low.series.R4.cap_node.3` |
| R-F06 | R4 realized node price 2025 | 28.51 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R4.node_price.3` |
| R-F06 | R4 revenue 2025 | 8.8 | USD m | low | 2022 to 2030 | `scenarios.low.series.R4.revenue.3` |
| R-F06 | R4 generation 2026 | 222.1 | GWh | low | 2022 to 2030 | `scenarios.low.series.R4.gen.4` |
| R-F06 | R4 node capture ratio 2026 | 0.710 | ratio | low | 2022 to 2030 | `scenarios.low.series.R4.cap_node.4` |
| R-F06 | R4 realized node price 2026 | 24.19 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R4.node_price.4` |
| R-F06 | R4 revenue 2026 | 8.6 | USD m | low | 2022 to 2030 | `scenarios.low.series.R4.revenue.4` |
| R-F06 | R4 generation 2027 | 221.1 | GWh | low | 2022 to 2030 | `scenarios.low.series.R4.gen.5` |
| R-F06 | R4 node capture ratio 2027 | 0.680 | ratio | low | 2022 to 2030 | `scenarios.low.series.R4.cap_node.5` |
| R-F06 | R4 realized node price 2027 | 23.96 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R4.node_price.5` |
| R-F06 | R4 revenue 2027 | 5.3 | USD m | low | 2022 to 2030 | `scenarios.low.series.R4.revenue.5` |
| R-F06 | R4 generation 2028 | 220.1 | GWh | low | 2022 to 2030 | `scenarios.low.series.R4.gen.6` |
| R-F06 | R4 node capture ratio 2028 | 0.650 | ratio | low | 2022 to 2030 | `scenarios.low.series.R4.cap_node.6` |
| R-F06 | R4 realized node price 2028 | 23.47 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R4.node_price.6` |
| R-F06 | R4 revenue 2028 | 5.2 | USD m | low | 2022 to 2030 | `scenarios.low.series.R4.revenue.6` |
| R-F06 | R4 generation 2029 | 219.1 | GWh | low | 2022 to 2030 | `scenarios.low.series.R4.gen.7` |
| R-F06 | R4 node capture ratio 2029 | 0.620 | ratio | low | 2022 to 2030 | `scenarios.low.series.R4.cap_node.7` |
| R-F06 | R4 realized node price 2029 | 22.81 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R4.node_price.7` |
| R-F06 | R4 revenue 2029 | 5.0 | USD m | low | 2022 to 2030 | `scenarios.low.series.R4.revenue.7` |
| R-F06 | R4 generation 2030 | 218.1 | GWh | low | 2022 to 2030 | `scenarios.low.series.R4.gen.8` |
| R-F06 | R4 node capture ratio 2030 | 0.590 | ratio | low | 2022 to 2030 | `scenarios.low.series.R4.cap_node.8` |
| R-F06 | R4 realized node price 2030 | 22.05 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R4.node_price.8` |
| R-F06 | R4 revenue 2030 | 4.8 | USD m | low | 2022 to 2030 | `scenarios.low.series.R4.revenue.8` |
| R-F06 | R5 generation 2022 | 443.2 | GWh | low | 2022 to 2030 | `scenarios.low.series.R5.gen.0` |
| R-F06 | R5 node capture ratio 2022 | 0.830 | ratio | low | 2022 to 2030 | `scenarios.low.series.R5.cap_node.0` |
| R-F06 | R5 realized node price 2022 | 59.94 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R5.node_price.0` |
| R-F06 | R5 revenue 2022 | 11.4 | USD m | low | 2022 to 2030 | `scenarios.low.series.R5.revenue.0` |
| R-F06 | R5 generation 2023 | 438.9 | GWh | low | 2022 to 2030 | `scenarios.low.series.R5.gen.1` |
| R-F06 | R5 node capture ratio 2023 | 0.800 | ratio | low | 2022 to 2030 | `scenarios.low.series.R5.cap_node.1` |
| R-F06 | R5 realized node price 2023 | 47.39 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R5.node_price.1` |
| R-F06 | R5 revenue 2023 | 11.4 | USD m | low | 2022 to 2030 | `scenarios.low.series.R5.revenue.1` |
| R-F06 | R5 generation 2024 | 434.7 | GWh | low | 2022 to 2030 | `scenarios.low.series.R5.gen.2` |
| R-F06 | R5 node capture ratio 2024 | 0.770 | ratio | low | 2022 to 2030 | `scenarios.low.series.R5.cap_node.2` |
| R-F06 | R5 realized node price 2024 | 22.44 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R5.node_price.2` |
| R-F06 | R5 revenue 2024 | 11.7 | USD m | low | 2022 to 2030 | `scenarios.low.series.R5.revenue.2` |
| R-F06 | R5 generation 2025 | 430.5 | GWh | low | 2022 to 2030 | `scenarios.low.series.R5.gen.3` |
| R-F06 | R5 node capture ratio 2025 | 0.740 | ratio | low | 2022 to 2030 | `scenarios.low.series.R5.cap_node.3` |
| R-F06 | R5 realized node price 2025 | 28.51 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R5.node_price.3` |
| R-F06 | R5 revenue 2025 | 11.5 | USD m | low | 2022 to 2030 | `scenarios.low.series.R5.revenue.3` |
| R-F06 | R5 generation 2026 | 428.6 | GWh | low | 2022 to 2030 | `scenarios.low.series.R5.gen.4` |
| R-F06 | R5 node capture ratio 2026 | 0.710 | ratio | low | 2022 to 2030 | `scenarios.low.series.R5.cap_node.4` |
| R-F06 | R5 realized node price 2026 | 24.19 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R5.node_price.4` |
| R-F06 | R5 revenue 2026 | 11.5 | USD m | low | 2022 to 2030 | `scenarios.low.series.R5.revenue.4` |
| R-F06 | R5 generation 2027 | 426.6 | GWh | low | 2022 to 2030 | `scenarios.low.series.R5.gen.5` |
| R-F06 | R5 node capture ratio 2027 | 0.680 | ratio | low | 2022 to 2030 | `scenarios.low.series.R5.cap_node.5` |
| R-F06 | R5 realized node price 2027 | 23.96 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R5.node_price.5` |
| R-F06 | R5 revenue 2027 | 11.4 | USD m | low | 2022 to 2030 | `scenarios.low.series.R5.revenue.5` |
| R-F06 | R5 generation 2028 | 424.7 | GWh | low | 2022 to 2030 | `scenarios.low.series.R5.gen.6` |
| R-F06 | R5 node capture ratio 2028 | 0.650 | ratio | low | 2022 to 2030 | `scenarios.low.series.R5.cap_node.6` |
| R-F06 | R5 realized node price 2028 | 23.47 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R5.node_price.6` |
| R-F06 | R5 revenue 2028 | 11.4 | USD m | low | 2022 to 2030 | `scenarios.low.series.R5.revenue.6` |
| R-F06 | R5 generation 2029 | 422.8 | GWh | low | 2022 to 2030 | `scenarios.low.series.R5.gen.7` |
| R-F06 | R5 node capture ratio 2029 | 0.620 | ratio | low | 2022 to 2030 | `scenarios.low.series.R5.cap_node.7` |
| R-F06 | R5 realized node price 2029 | 22.81 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R5.node_price.7` |
| R-F06 | R5 revenue 2029 | 11.3 | USD m | low | 2022 to 2030 | `scenarios.low.series.R5.revenue.7` |
| R-F06 | R5 generation 2030 | 420.9 | GWh | low | 2022 to 2030 | `scenarios.low.series.R5.gen.8` |
| R-F06 | R5 node capture ratio 2030 | 0.590 | ratio | low | 2022 to 2030 | `scenarios.low.series.R5.cap_node.8` |
| R-F06 | R5 realized node price 2030 | 22.05 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R5.node_price.8` |
| R-F06 | R5 revenue 2030 | 11.3 | USD m | low | 2022 to 2030 | `scenarios.low.series.R5.revenue.8` |
| R-F06 | R6 revenue 2022 | 0.0 | USD m | low | 2022 to 2030 | `scenarios.low.series.R6.revenue.0` |
| R-F06 | R6 revenue 2023 | 5.1 | USD m | low | 2022 to 2030 | `scenarios.low.series.R6.revenue.1` |
| R-F06 | R6 revenue 2024 | 11.0 | USD m | low | 2022 to 2030 | `scenarios.low.series.R6.revenue.2` |
| R-F06 | R6 revenue 2025 | 11.0 | USD m | low | 2022 to 2030 | `scenarios.low.series.R6.revenue.3` |
| R-F06 | R6 revenue 2026 | 11.0 | USD m | low | 2022 to 2030 | `scenarios.low.series.R6.revenue.4` |
| R-F06 | R6 revenue 2027 | 11.0 | USD m | low | 2022 to 2030 | `scenarios.low.series.R6.revenue.5` |
| R-F06 | R6 revenue 2028 | 11.0 | USD m | low | 2022 to 2030 | `scenarios.low.series.R6.revenue.6` |
| R-F06 | R6 revenue 2029 | 11.0 | USD m | low | 2022 to 2030 | `scenarios.low.series.R6.revenue.7` |
| R-F06 | R6 revenue 2030 | 7.7 | USD m | low | 2022 to 2030 | `scenarios.low.series.R6.revenue.8` |
| R-F06 | R7 revenue 2022 | 0.0 | USD m | low | 2022 to 2030 | `scenarios.low.series.R7.revenue.0` |
| R-F06 | R7 revenue 2023 | 0.0 | USD m | low | 2022 to 2030 | `scenarios.low.series.R7.revenue.1` |
| R-F06 | R7 revenue 2024 | 7.6 | USD m | low | 2022 to 2030 | `scenarios.low.series.R7.revenue.2` |
| R-F06 | R7 revenue 2025 | 10.2 | USD m | low | 2022 to 2030 | `scenarios.low.series.R7.revenue.3` |
| R-F06 | R7 revenue 2026 | 10.2 | USD m | low | 2022 to 2030 | `scenarios.low.series.R7.revenue.4` |
| R-F06 | R7 revenue 2027 | 10.2 | USD m | low | 2022 to 2030 | `scenarios.low.series.R7.revenue.5` |
| R-F06 | R7 revenue 2028 | 10.2 | USD m | low | 2022 to 2030 | `scenarios.low.series.R7.revenue.6` |
| R-F06 | R7 revenue 2029 | 10.2 | USD m | low | 2022 to 2030 | `scenarios.low.series.R7.revenue.7` |
| R-F06 | R7 revenue 2030 | 10.2 | USD m | low | 2022 to 2030 | `scenarios.low.series.R7.revenue.8` |
| R-F06 | R8 generation 2022 | 0.0 | GWh | low | 2022 to 2030 | `scenarios.low.series.R8.gen.0` |
| R-F06 | R8 node capture ratio 2022 | 0.880 | ratio | low | 2022 to 2030 | `scenarios.low.series.R8.cap_node.0` |
| R-F06 | R8 realized node price 2022 | 65.06 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R8.node_price.0` |
| R-F06 | R8 revenue 2022 | 0.0 | USD m | low | 2022 to 2030 | `scenarios.low.series.R8.revenue.0` |
| R-F06 | R8 generation 2023 | 0.0 | GWh | low | 2022 to 2030 | `scenarios.low.series.R8.gen.1` |
| R-F06 | R8 node capture ratio 2023 | 0.853 | ratio | low | 2022 to 2030 | `scenarios.low.series.R8.cap_node.1` |
| R-F06 | R8 realized node price 2023 | 51.73 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R8.node_price.1` |
| R-F06 | R8 revenue 2023 | 0.0 | USD m | low | 2022 to 2030 | `scenarios.low.series.R8.revenue.1` |
| R-F06 | R8 generation 2024 | 9.3 | GWh | low | 2022 to 2030 | `scenarios.low.series.R8.gen.2` |
| R-F06 | R8 node capture ratio 2024 | 0.826 | ratio | low | 2022 to 2030 | `scenarios.low.series.R8.cap_node.2` |
| R-F06 | R8 realized node price 2024 | 24.64 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R8.node_price.2` |
| R-F06 | R8 revenue 2024 | 0.2 | USD m | low | 2022 to 2030 | `scenarios.low.series.R8.revenue.2` |
| R-F06 | R8 generation 2025 | 284.9 | GWh | low | 2022 to 2030 | `scenarios.low.series.R8.gen.3` |
| R-F06 | R8 node capture ratio 2025 | 0.799 | ratio | low | 2022 to 2030 | `scenarios.low.series.R8.cap_node.3` |
| R-F06 | R8 realized node price 2025 | 31.51 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R8.node_price.3` |
| R-F06 | R8 revenue 2025 | 10.1 | USD m | low | 2022 to 2030 | `scenarios.low.series.R8.revenue.3` |
| R-F06 | R8 generation 2026 | 283.7 | GWh | low | 2022 to 2030 | `scenarios.low.series.R8.gen.4` |
| R-F06 | R8 node capture ratio 2026 | 0.772 | ratio | low | 2022 to 2030 | `scenarios.low.series.R8.cap_node.4` |
| R-F06 | R8 realized node price 2026 | 26.93 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R8.node_price.4` |
| R-F06 | R8 revenue 2026 | 9.6 | USD m | low | 2022 to 2030 | `scenarios.low.series.R8.revenue.4` |
| R-F06 | R8 generation 2027 | 282.6 | GWh | low | 2022 to 2030 | `scenarios.low.series.R8.gen.5` |
| R-F06 | R8 node capture ratio 2027 | 0.745 | ratio | low | 2022 to 2030 | `scenarios.low.series.R8.cap_node.5` |
| R-F06 | R8 realized node price 2027 | 26.87 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R8.node_price.5` |
| R-F06 | R8 revenue 2027 | 9.6 | USD m | low | 2022 to 2030 | `scenarios.low.series.R8.revenue.5` |
| R-F06 | R8 generation 2028 | 281.5 | GWh | low | 2022 to 2030 | `scenarios.low.series.R8.gen.6` |
| R-F06 | R8 node capture ratio 2028 | 0.718 | ratio | low | 2022 to 2030 | `scenarios.low.series.R8.cap_node.6` |
| R-F06 | R8 realized node price 2028 | 26.54 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R8.node_price.6` |
| R-F06 | R8 revenue 2028 | 9.5 | USD m | low | 2022 to 2030 | `scenarios.low.series.R8.revenue.6` |
| R-F06 | R8 generation 2029 | 280.3 | GWh | low | 2022 to 2030 | `scenarios.low.series.R8.gen.7` |
| R-F06 | R8 node capture ratio 2029 | 0.691 | ratio | low | 2022 to 2030 | `scenarios.low.series.R8.cap_node.7` |
| R-F06 | R8 realized node price 2029 | 26.02 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R8.node_price.7` |
| R-F06 | R8 revenue 2029 | 9.4 | USD m | low | 2022 to 2030 | `scenarios.low.series.R8.revenue.7` |
| R-F06 | R8 generation 2030 | 279.2 | GWh | low | 2022 to 2030 | `scenarios.low.series.R8.gen.8` |
| R-F06 | R8 node capture ratio 2030 | 0.664 | ratio | low | 2022 to 2030 | `scenarios.low.series.R8.cap_node.8` |
| R-F06 | R8 realized node price 2030 | 25.40 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.R8.node_price.8` |
| R-F06 | R8 revenue 2030 | 9.3 | USD m | low | 2022 to 2030 | `scenarios.low.series.R8.revenue.8` |
| R-F06 | West Hub ATC 2022 | 72.21 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.portfolio.west_atc.0` |
| R-F06 | Portfolio CFADS (Mesa share) 2022 | 45.2 | USD m | low | 2022 to 2030 | `scenarios.low.series.portfolio.cfads_all.0` |
| R-F06 | West Hub ATC 2023 | 59.24 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.portfolio.west_atc.1` |
| R-F06 | Portfolio CFADS (Mesa share) 2023 | 49.1 | USD m | low | 2022 to 2030 | `scenarios.low.series.portfolio.cfads_all.1` |
| R-F06 | West Hub ATC 2024 | 29.14 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.portfolio.west_atc.2` |
| R-F06 | Portfolio CFADS (Mesa share) 2024 | 56.7 | USD m | low | 2022 to 2030 | `scenarios.low.series.portfolio.cfads_all.2` |
| R-F06 | West Hub ATC 2025 | 38.53 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.portfolio.west_atc.3` |
| R-F06 | Portfolio CFADS (Mesa share) 2025 | 65.5 | USD m | low | 2022 to 2030 | `scenarios.low.series.portfolio.cfads_all.3` |
| R-F06 | West Hub ATC 2026 | 34.07 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.portfolio.west_atc.4` |
| R-F06 | Portfolio CFADS (Mesa share) 2026 | 63.2 | USD m | low | 2022 to 2030 | `scenarios.low.series.portfolio.cfads_all.4` |
| R-F06 | West Hub ATC 2027 | 35.24 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.portfolio.west_atc.5` |
| R-F06 | Portfolio CFADS (Mesa share) 2027 | 59.2 | USD m | low | 2022 to 2030 | `scenarios.low.series.portfolio.cfads_all.5` |
| R-F06 | West Hub ATC 2028 | 36.11 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.portfolio.west_atc.6` |
| R-F06 | Portfolio CFADS (Mesa share) 2028 | 53.6 | USD m | low | 2022 to 2030 | `scenarios.low.series.portfolio.cfads_all.6` |
| R-F06 | West Hub ATC 2029 | 36.78 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.portfolio.west_atc.7` |
| R-F06 | Portfolio CFADS (Mesa share) 2029 | 52.5 | USD m | low | 2022 to 2030 | `scenarios.low.series.portfolio.cfads_all.7` |
| R-F06 | West Hub ATC 2030 | 37.36 | USD/MWh | low | 2022 to 2030 | `scenarios.low.series.portfolio.west_atc.8` |
| R-F06 | Portfolio CFADS (Mesa share) 2030 | 43.1 | USD m | low | 2022 to 2030 | `scenarios.low.series.portfolio.cfads_all.8` |
| R-F07 | A2 R6 value before shield | 50.4 | USD m | base | 2023-08-31 | `valuations.base.A2.pre_shield` |
| R-F07 | A2 tax shield | 12.1 | USD m | base | 2023-08-31 | `valuations.base.A2.shield_at_price` |
| R-F07 | A2 value | 62.5 | USD m | base | 2023-08-31 | `valuations.base.A2.ev` |
| R-F07 | A2 price (calibrated, R-C05) | 63.7 | USD m | base | 2023-08-31 | `valuations.base.A2.price` |
| R-F07 | A2 value less price | -1.2 | USD m | base | 2023-08-31 | `valuations.base.A2.npv_vs_price` |
| R-F07 | A2 breakeven price | 62.2 | USD m | base | 2023-08-31 | `valuations.base.A2.breakeven_price` |
| R-F07 | A2 R6 value contracted | 38.6 | USD m | base | 2023-08-31 | `valuations.base.A2.R6.contracted` |
| R-F07 | A2 R6 value merchant | 11.8 | USD m | base | 2023-08-31 | `valuations.base.A2.R6.merchant` |
| R-F07 | A2 uses: price | 63.7 | USD m | base | 2023-08-31 | `scenarios.base.sources_uses.A2.price` |
| R-F07 | A2 uses: costs | 2.6 | USD m | base | 2023-08-31 | `scenarios.base.sources_uses.A2.costs` |
| R-F07 | A2 uses: Redfern fee | 0.5 | USD m | base | 2023-08-31 | `scenarios.base.sources_uses.A2.fee` |
| R-F07 | A2 sources: Redfern loan | 36.6 | USD m | base | 2023-08-31 | `scenarios.base.sources_uses.A2.loan` |
| R-F07 | A2 sources: fund equity | 30.2 | USD m | base | 2023-08-31 | `scenarios.base.sources_uses.A2.equity` |
| R-F07 | Redfern loan minimum DSCR 2024-2029 | 1.35x | x | base | 2023-08-31 | `scenarios.base.scalars.rf_dscr_min` |
| R-F07 | A3 R7 value contracted | 35.3 | USD m | base | 2024-02-15 | `valuations.base.A3.R7.contracted` |
| R-F07 | A3 R7 value hedged | 0.0 | USD m | base | 2024-02-15 | `valuations.base.A3.R7.hedged` |
| R-F07 | A3 R7 value merchant | 15.0 | USD m | base | 2024-02-15 | `valuations.base.A3.R7.merchant` |
| R-F07 | A3 R7 value total | 50.2 | USD m | base | 2024-02-15 | `valuations.base.A3.R7.total` |
| R-F07 | A3 R8 value contracted | 0.0 | USD m | base | 2024-02-15 | `valuations.base.A3.R8.contracted` |
| R-F07 | A3 R8 value hedged | 24.9 | USD m | base | 2024-02-15 | `valuations.base.A3.R8.hedged` |
| R-F07 | A3 R8 value merchant | 30.1 | USD m | base | 2024-02-15 | `valuations.base.A3.R8.merchant` |
| R-F07 | A3 R8 value total | 55.0 | USD m | base | 2024-02-15 | `valuations.base.A3.R8.total` |
| R-F07 | R7 ITC | 24.1 | USD m | base | 2024-02-15 | `valuations.base.A3.itc7` |
| R-F07 | R8 ITC | 28.7 | USD m | base | 2024-02-15 | `valuations.base.A3.itc8` |
| R-F07 | ITC transfer proceeds (nominal) | 48.9 | USD m | base | 2024-02-15 | `valuations.base.A3.itc_proceeds` |
| R-F07 | ITC transfer proceeds (PV at signing) | 47.3 | USD m | base | 2024-02-15 | `valuations.base.A3.itc_pv` |
| R-F07 | A3 tax shield | 29.1 | USD m | base | 2024-02-15 | `valuations.base.A3.shield` |
| R-F07 | A3 value | 181.6 | USD m | base | 2024-02-15 | `valuations.base.A3.ev` |
| R-F07 | A3 prices (calibrated, R-C06) | 189.3 | USD m | base | 2024-02-15 | `valuations.base.A3.price_nominal` |
| R-F07 | A3 price payments (PV at signing) | 184.2 | USD m | base | 2024-02-15 | `valuations.base.A3.price_pv` |
| R-F07 | A3 value less PV of price | -2.6 | USD m | base | 2024-02-15 | `valuations.base.A3.npv_vs_price` |
| R-F07 | A3 R8 deposit | 20.4 | USD m | base | 2024-02-15 to 2024-12-19 | `scenarios.base.sources_uses.A3.r8_deposit` |
| R-F07 | A3 costs | 4.4 | USD m | base | 2024-02-15 to 2024-12-19 | `scenarios.base.sources_uses.A3.costs` |
| R-F07 | A3 holdco incremental OID | 0.9 | USD m | base | 2024-02-15 to 2024-12-19 | `scenarios.base.sources_uses.A3.oid` |
| R-F07 | Holdco incremental term loan | 93.3 | USD m | base | 2024-02-15 to 2024-12-19 | `scenarios.base.sources_uses.A3.holdco_incr` |
| R-F07 | R7 ITC proceeds | 22.3 | USD m | base | 2024-02-15 to 2024-12-19 | `scenarios.base.sources_uses.A3.itc7_proceeds` |
| R-F07 | R8 ITC proceeds | 26.6 | USD m | base | 2024-02-15 to 2024-12-19 | `scenarios.base.sources_uses.A3.itc8_proceeds` |
| R-F07 | A3 equity at signing | 0.0 | USD m | base | 2024-02-15 to 2024-12-19 | `scenarios.base.sources_uses.A3.eq_signing` |
| R-F07 | A3 equity at R7 COD | 0.0 | USD m | base | 2024-02-15 to 2024-12-19 | `scenarios.base.sources_uses.A3.eq_r7` |
| R-F07 | A3 equity at R8 COD | 52.4 | USD m | base | 2024-02-15 to 2024-12-19 | `scenarios.base.sources_uses.A3.eq_r8` |
| R-F07 | A3 fund equity | 52.4 | USD m | base | 2024-02-15 to 2024-12-19 | `scenarios.base.sources_uses.A3.equity` |
| R-F08 | USPP Series A size | 142.2 | USD m | base | 2025-10-21 (priced) | `sizing.u_series_size.A` |
| R-F08 | USPP Series A share | 39.90% | % | base | 2025-10-21 | `sizing.u_series_share.A` |
| R-F08 | USPP Series B size | 81.9 | USD m | base | 2025-10-21 (priced) | `sizing.u_series_size.B` |
| R-F08 | USPP Series B share | 22.98% | % | base | 2025-10-21 | `sizing.u_series_share.B` |
| R-F08 | USPP Series C size | 132.3 | USD m | base | 2025-10-21 (priced) | `sizing.u_series_size.C` |
| R-F08 | USPP Series C share | 37.12% | % | base | 2025-10-21 | `sizing.u_series_share.C` |
| R-F08 | USPP notes total | 356.3 | USD m | base | 2025-12-16 (modeled 2025-12-31) | `sizing.u_size` |
| R-F08 | Blended coupon (issue-weighted) | 6.05% | % | base | 2025-12-16 (modeled 2025-12-31) | `sizing.u_coupon` |
| R-F08 | USPP capacity from contracted CFADS (PV at blended coupon) | 121.4 | USD m | base | 2025-12-16 (modeled 2025-12-31) | `sizing.u_pv_cap_contracted` |
| R-F08 | USPP capacity from hedged CFADS (PV) | 32.1 | USD m | base | 2025-12-16 (modeled 2025-12-31) | `sizing.u_pv_cap_hedged` |
| R-F08 | USPP capacity from merchant CFADS (PV) | 205.9 | USD m | base | 2025-12-16 (modeled 2025-12-31) | `sizing.u_pv_cap_merchant` |
| R-F08 | Years the USPP P99 test binds | 0 | years | base | 2025-12-16 (modeled 2025-12-31) | `sizing.u_p99_binds_years` |
| R-F08 | Repriced holdco TLB face | 137.6 | USD m | base | 2025-12-16 (modeled 2025-12-31) | `sizing.hn_face` |
| R-F08 | Opco term loan repaid | 251.6 | USD m | base | 2025-12-16 | `scenarios.base.refinancing_cash.tl_repay` |
| R-F08 | Redfern loan repaid | 25.6 | USD m | base | 2025-12-16 | `scenarios.base.refinancing_cash.rf_repay` |
| R-F08 | Opco swap unwind receivable | 6.7 | USD m | base | 2025-12-16 | `scenarios.base.refinancing_cash.mtm_opco_receivable` |
| R-F08 | Redfern swap unwind payable | 0.4 | USD m | base | 2025-12-16 | `scenarios.base.refinancing_cash.mtm_redfern_payable` |
| R-F08 | USPP transaction costs | 3.9 | USD m | base | 2025-12-16 | `scenarios.base.refinancing_cash.costs` |
| R-F08 | Net opco proceeds to holdco | 81.5 | USD m | base | 2025-12-16 | `scenarios.base.refinancing_cash.opco_net` |
| R-F08 | Holdco tranches repaid at repricing | 126.7 | USD m | base | 2025-12-16 | `derived.holdco_repaid_at_repricing` |
| R-F08 | Holdco repricing net proceeds | 10.2 | USD m | base | 2025-12-16 | `scenarios.base.series.finance.recap_hold.3` |
| R-F08 | Recapitalization distribution to the fund | 91.7 | USD m | base | 2025-12-16 | `scenarios.base.scalars.recap_distribution_2025` |
| R-F08 | Minimum USPP DSCR 2026-2043 | 1.43x | x | base | 2025-12-31 | `scenarios.base.scalars.uspp_dscr_min_2026_2043` |
| R-F08 | Average USPP DSCR 2026-2043 | 2.03x | x | base | 2025-12-31 | `scenarios.base.scalars.uspp_dscr_avg_2026_2043` |
| R-F08 | Repriced holdco balance at 2031 maturity (refinancing requirement) | 88.0 | USD m | base | 2031-12-31 (projected) | `scenarios.base.scalars.holdco_balance_end_2031` |
| R-F08 | Fund gross IRR, life (base) | 11.33% | % | base | 2025-12-31 | `scenarios.base.scalars.fund_irr_life_pct` |
| R-F08 | Fund gross IRR to 2025 incl. NAV (base) | 11.29% | % | base | 2025-12-31 | `scenarios.base.scalars.fund_irr_2025_pct` |
| R-F08 | Fund gross IRR, life (status_quo) | 9.87% | % | status_quo | 2025-12-31 | `scenarios.status_quo.scalars.fund_irr_life_pct` |
| R-F08 | Fund gross IRR to 2025 incl. NAV (status_quo) | 4.39% | % | status_quo | 2025-12-31 | `scenarios.status_quo.scalars.fund_irr_2025_pct` |
| R-F08 | IRR impact of the refinancing, life (percentage points) | 1.46% | % | base less status_quo | 2025-12-31 | `derived.irr_impact_life_pts` |
| R-F08 | IRR impact of the refinancing, to 2025 incl. NAV (percentage points) | 6.90% | % | base less status_quo | 2025-12-31 | `derived.irr_impact_2025_pts` |
| R-F09 | Fund equity contributed (A1+A2+A3) (base) | 164.6 | USD m | base | 2025-12-31 | `scenarios.base.scalars.fund_contributions` |
| R-F09 | Distributions to December 31, 2025 (base) | 111.6 | USD m | base | 2025-12-31 | `scenarios.base.scalars.fund_distributions_to_2025` |
| R-F09 | NAV at December 31, 2025 (base) | 105.0 | USD m | base | 2025-12-31 | `scenarios.base.scalars.fund_nav_2025` |
| R-F09 | Gross IRR to December 31, 2025 incl. NAV (base) | 11.29% | % | base | 2025-12-31 | `scenarios.base.scalars.fund_irr_2025_pct` |
| R-F09 | Multiple to December 31, 2025 incl. NAV (base) | 1.32x | x | base | 2025-12-31 | `scenarios.base.scalars.fund_moic_2025_x` |
| R-F09 | Gross IRR, life (base) | 11.33% | % | base | 2025-12-31 | `scenarios.base.scalars.fund_irr_life_pct` |
| R-F09 | Multiple, life (base) | 3.54x | x | base | 2025-12-31 | `scenarios.base.scalars.fund_moic_life_x` |
| R-F09 | Fund equity contributed (A1+A2+A3) (status_quo) | 164.6 | USD m | status_quo | 2025-12-31 | `scenarios.status_quo.scalars.fund_contributions` |
| R-F09 | Distributions to December 31, 2025 (status_quo) | 20.0 | USD m | status_quo | 2025-12-31 | `scenarios.status_quo.scalars.fund_distributions_to_2025` |
| R-F09 | NAV at December 31, 2025 (status_quo) | 163.3 | USD m | status_quo | 2025-12-31 | `scenarios.status_quo.scalars.fund_nav_2025` |
| R-F09 | Gross IRR to December 31, 2025 incl. NAV (status_quo) | 4.39% | % | status_quo | 2025-12-31 | `scenarios.status_quo.scalars.fund_irr_2025_pct` |
| R-F09 | Multiple to December 31, 2025 incl. NAV (status_quo) | 1.11x | x | status_quo | 2025-12-31 | `scenarios.status_quo.scalars.fund_moic_2025_x` |
| R-F09 | Gross IRR, life (status_quo) | 9.87% | % | status_quo | 2025-12-31 | `scenarios.status_quo.scalars.fund_irr_life_pct` |
| R-F09 | Multiple, life (status_quo) | 4.11x | x | status_quo | 2025-12-31 | `scenarios.status_quo.scalars.fund_moic_life_x` |
| R-F09 | Fund distribution 2022 | 5.9 | USD m | base | 2022-12-31 | `scenarios.base.series.finance.fund_dist.0` |
| R-F09 | Fund distribution 2023 | 3.8 | USD m | base | 2023-12-31 | `scenarios.base.series.finance.fund_dist.1` |
| R-F09 | Fund distribution 2024 | 2.7 | USD m | base | 2024-12-31 | `scenarios.base.series.finance.fund_dist.2` |
| R-F09 | Fund distribution 2025 | 99.2 | USD m | base | 2025-12-31 | `scenarios.base.series.finance.fund_dist.3` |
| R-F10 | R1 decommissioning cost in 2022 prices (retires 2044-12-31) | 12.5 | USD m | base | 2026-03 | `decommissioning.R1.cost_2022_prices` |
| R-F10 | R1 decommissioning bonded amount 2026 (retires 2044-12-31) | 13.8 | USD m | base | 2026-03 | `decommissioning.R1.bonded_amount_2026` |
| R-F10 | R1 decommissioning surety cost 2026 (retires 2044-12-31) | 0.083 | USD m | base | 2026-03 | `decommissioning.R1.bond_cost_2026` |
| R-F10 | R1 decommissioning nominal cost at retirement (retires 2044-12-31) | 21.5 | USD m | base | 2026-03 | `decommissioning.R1.cost_nominal_at_retirement` |
| R-F10 | R2 decommissioning cost in 2022 prices (retires 2047-06-30) | 15.4 | USD m | base | 2026-03 | `decommissioning.R2.cost_2022_prices` |
| R-F10 | R2 decommissioning bonded amount 2026 (retires 2047-06-30) | 17.0 | USD m | base | 2026-03 | `decommissioning.R2.bonded_amount_2026` |
| R-F10 | R2 decommissioning surety cost 2026 (retires 2047-06-30) | 0.102 | USD m | base | 2026-03 | `decommissioning.R2.bond_cost_2026` |
| R-F10 | R2 decommissioning nominal cost at retirement (retires 2047-06-30) | 28.6 | USD m | base | 2026-03 | `decommissioning.R2.cost_nominal_at_retirement` |
| R-F10 | R3 decommissioning cost in 2022 prices (retires 2049-11-30) | 9.5 | USD m | base | 2026-03 | `decommissioning.R3.cost_2022_prices` |
| R-F10 | R3 decommissioning bonded amount 2026 (retires 2049-11-30) | 10.5 | USD m | base | 2026-03 | `decommissioning.R3.bonded_amount_2026` |
| R-F10 | R3 decommissioning surety cost 2026 (retires 2049-11-30) | 0.063 | USD m | base | 2026-03 | `decommissioning.R3.bond_cost_2026` |
| R-F10 | R3 decommissioning nominal cost at retirement (retires 2049-11-30) | 18.5 | USD m | base | 2026-03 | `decommissioning.R3.cost_nominal_at_retirement` |
| R-F10 | R4 decommissioning cost in 2022 prices (retires 2055-10-31) | 3.8 | USD m | base | 2026-03 | `decommissioning.R4.cost_2022_prices` |
| R-F10 | R4 decommissioning bonded amount 2026 (retires 2055-10-31) | 4.1 | USD m | base | 2026-03 | `decommissioning.R4.bonded_amount_2026` |
| R-F10 | R4 decommissioning surety cost 2026 (retires 2055-10-31) | 0.025 | USD m | base | 2026-03 | `decommissioning.R4.bond_cost_2026` |
| R-F10 | R4 decommissioning nominal cost at retirement (retires 2055-10-31) | 8.5 | USD m | base | 2026-03 | `decommissioning.R4.cost_nominal_at_retirement` |
| R-F10 | R5 decommissioning cost in 2022 prices (retires 2056-06-30) | 6.9 | USD m | base | 2026-03 | `decommissioning.R5.cost_2022_prices` |
| R-F10 | R5 decommissioning bonded amount 2026 (retires 2056-06-30) | 7.7 | USD m | base | 2026-03 | `decommissioning.R5.bonded_amount_2026` |
| R-F10 | R5 decommissioning surety cost 2026 (retires 2056-06-30) | 0.046 | USD m | base | 2026-03 | `decommissioning.R5.bond_cost_2026` |
| R-F10 | R5 decommissioning nominal cost at retirement (retires 2056-06-30) | 16.0 | USD m | base | 2026-03 | `decommissioning.R5.cost_nominal_at_retirement` |
| R-F10 | R6 decommissioning cost in 2022 prices (retires 2043-07-31) | 2.1 | USD m | base | 2026-03 | `decommissioning.R6.cost_2022_prices` |
| R-F10 | R6 decommissioning bonded amount 2026 (retires 2043-07-31) | 2.3 | USD m | base | 2026-03 | `decommissioning.R6.bonded_amount_2026` |
| R-F10 | R6 decommissioning surety cost 2026 (retires 2043-07-31) | 0.014 | USD m | base | 2026-03 | `decommissioning.R6.bond_cost_2026` |
| R-F10 | R6 decommissioning nominal cost at retirement (retires 2043-07-31) | 3.5 | USD m | base | 2026-03 | `decommissioning.R6.cost_nominal_at_retirement` |
| R-F10 | R7 decommissioning cost in 2022 prices (retires 2044-03-31) | 3.1 | USD m | base | 2026-03 | `decommissioning.R7.cost_2022_prices` |
| R-F10 | R7 decommissioning bonded amount 2026 (retires 2044-03-31) | 3.5 | USD m | base | 2026-03 | `decommissioning.R7.bonded_amount_2026` |
| R-F10 | R7 decommissioning surety cost 2026 (retires 2044-03-31) | 0.021 | USD m | base | 2026-03 | `decommissioning.R7.bond_cost_2026` |
| R-F10 | R7 decommissioning nominal cost at retirement (retires 2044-03-31) | 5.4 | USD m | base | 2026-03 | `decommissioning.R7.cost_nominal_at_retirement` |
| R-F10 | R8 decommissioning cost in 2022 prices (retires 2059-12-31) | 4.6 | USD m | base | 2026-03 | `decommissioning.R8.cost_2022_prices` |
| R-F10 | R8 decommissioning bonded amount 2026 (retires 2059-12-31) | 5.0 | USD m | base | 2026-03 | `decommissioning.R8.bonded_amount_2026` |
| R-F10 | R8 decommissioning surety cost 2026 (retires 2059-12-31) | 0.030 | USD m | base | 2026-03 | `decommissioning.R8.bond_cost_2026` |
| R-F10 | R8 decommissioning nominal cost at retirement (retires 2059-12-31) | 11.4 | USD m | base | 2026-03 | `decommissioning.R8.cost_nominal_at_retirement` |
| R-F11 | Redfern term loan | 36.6 | USD m | base | 2023-08-31 / 2024-02-15 | `sizing.rf_debt` |
| R-F11 | Holdco incremental term loan | 93.3 | USD m | base | 2023-08-31 / 2024-02-15 | `sizing.hi_face` |
| R-F11 | Holdco coverage 2024 (incremental interest before R8 COD) | 1.40x | x | base | 2024-12-31 | `scenarios.base.series.finance.hc_cov.2` |
| R-F11 | Minimum opco TL DSCR 2022-2025 | 1.35x | x | base | 2022 to 2025 | `scenarios.base.scalars.tl_dscr_min_2022_2025` |
| R-F11 | Opco TL DSCR 2022 | 1.51x | x | base | 2022 | `scenarios.base.series.finance.dscr_tl.0` |
| R-F11 | Opco TL DSCR 2023 | 1.37x | x | base | 2023 | `scenarios.base.series.finance.dscr_tl.1` |
| R-F11 | Opco TL DSCR 2024 | 1.35x | x | base | 2024 | `scenarios.base.series.finance.dscr_tl.2` |
| R-F11 | Opco TL DSCR 2025 | 1.35x | x | base | 2025 | `scenarios.base.series.finance.dscr_tl.3` |
| R-F12 | Opco TL allocated to R1 | 66.5 | USD m | base | 2022-03-22 | `debt_by_asset.opco_tl_2022.R1` |
| R-F12 | Opco TL allocated to R2 | 107.8 | USD m | base | 2022-03-22 | `debt_by_asset.opco_tl_2022.R2` |
| R-F12 | Opco TL allocated to R3 | 65.0 | USD m | base | 2022-03-22 | `debt_by_asset.opco_tl_2022.R3` |
| R-F12 | Opco TL allocated to R4 | 36.2 | USD m | base | 2022-03-22 | `debt_by_asset.opco_tl_2022.R4` |
| R-F12 | Opco TL allocated to R5 | 52.5 | USD m | base | 2022-03-22 | `debt_by_asset.opco_tl_2022.R5` |
| R-F12 | USPP allocated to R1 | 43.4 | USD m | base | 2025-12-31 | `debt_by_asset.uspp_2025.R1` |
| R-F12 | USPP allocated to R2 | 88.4 | USD m | base | 2025-12-31 | `debt_by_asset.uspp_2025.R2` |
| R-F12 | USPP allocated to R3 | 44.8 | USD m | base | 2025-12-31 | `debt_by_asset.uspp_2025.R3` |
| R-F12 | USPP allocated to R4 | 22.3 | USD m | base | 2025-12-31 | `debt_by_asset.uspp_2025.R4` |
| R-F12 | USPP allocated to R5 | 42.1 | USD m | base | 2025-12-31 | `debt_by_asset.uspp_2025.R5` |
| R-F12 | USPP allocated to R6 | 35.3 | USD m | base | 2025-12-31 | `debt_by_asset.uspp_2025.R6` |
| R-F12 | USPP allocated to R7 | 40.8 | USD m | base | 2025-12-31 | `debt_by_asset.uspp_2025.R7` |
| R-F12 | USPP allocated to R8 | 39.3 | USD m | base | 2025-12-31 | `debt_by_asset.uspp_2025.R8` |
| R-F13 | Portfolio CFADS 2026 (base) | 65.3 | USD m | base | 2025-12-31 view | `scenarios.base.scalars.cfads_2026` |
| R-F13 | Minimum USPP DSCR (base) | 1.43x | x | base | 2025-12-31 view | `scenarios.base.scalars.uspp_dscr_min_2026_2043` |
| R-F13 | Minimum holdco coverage 2023-2031 (base) | 1.40x | x | base | 2025-12-31 view | `scenarios.base.scalars.holdco_cov_min_2023_2031` |
| R-F13 | Fund gross IRR, life (base) | 11.33% | % | base | 2025-12-31 view | `scenarios.base.scalars.fund_irr_life_pct` |
| R-F13 | Fund gross IRR to 2025 incl. NAV (base) | 11.29% | % | base | 2025-12-31 view | `scenarios.base.scalars.fund_irr_2025_pct` |
| R-F13 | Years with holdco shortfall (base) | 2 | years | base | 2025-12-31 view | `scenarios.base.scalars.years_holdco_shortfall` |
| R-F13 | Portfolio CFADS 2026 (low) | 63.2 | USD m | low | 2025-12-31 view | `scenarios.low.scalars.cfads_2026` |
| R-F13 | Minimum USPP DSCR (low) | 0.32x | x | low | 2025-12-31 view | `scenarios.low.scalars.uspp_dscr_min_2026_2043` |
| R-F13 | Minimum holdco coverage 2023-2031 (low) | 0.55x | x | low | 2025-12-31 view | `scenarios.low.scalars.holdco_cov_min_2023_2031` |
| R-F13 | Fund gross IRR, life (low) | -12.31% | % | low | 2025-12-31 view | `scenarios.low.scalars.fund_irr_life_pct` |
| R-F13 | Fund gross IRR to 2025 incl. NAV (low) | -13.49% | % | low | 2025-12-31 view | `scenarios.low.scalars.fund_irr_2025_pct` |
| R-F13 | Years with holdco shortfall (low) | 30 | years | low | 2025-12-31 view | `scenarios.low.scalars.years_holdco_shortfall` |
| R-F13 | Portfolio CFADS 2026 (high) | 69.2 | USD m | high | 2025-12-31 view | `scenarios.high.scalars.cfads_2026` |
| R-F13 | Minimum USPP DSCR (high) | 1.52x | x | high | 2025-12-31 view | `scenarios.high.scalars.uspp_dscr_min_2026_2043` |
| R-F13 | Minimum holdco coverage 2023-2031 (high) | 1.41x | x | high | 2025-12-31 view | `scenarios.high.scalars.holdco_cov_min_2023_2031` |
| R-F13 | Fund gross IRR, life (high) | 19.89% | % | high | 2025-12-31 view | `scenarios.high.scalars.fund_irr_life_pct` |
| R-F13 | Fund gross IRR to 2025 incl. NAV (high) | 42.83% | % | high | 2025-12-31 view | `scenarios.high.scalars.fund_irr_2025_pct` |
| R-F13 | Years with holdco shortfall (high) | 1 | years | high | 2025-12-31 view | `scenarios.high.scalars.years_holdco_shortfall` |
| R-F13 | Portfolio CFADS 2026 (p90_1yr) | 59.2 | USD m | p90_1yr | 2025-12-31 view | `scenarios.p90_1yr.scalars.cfads_2026` |
| R-F13 | Minimum USPP DSCR (p90_1yr) | 1.30x | x | p90_1yr | 2025-12-31 view | `scenarios.p90_1yr.scalars.uspp_dscr_min_2026_2043` |
| R-F13 | Minimum holdco coverage 2023-2031 (p90_1yr) | 1.00x | x | p90_1yr | 2025-12-31 view | `scenarios.p90_1yr.scalars.holdco_cov_min_2023_2031` |
| R-F13 | Fund gross IRR, life (p90_1yr) | 5.87% | % | p90_1yr | 2025-12-31 view | `scenarios.p90_1yr.scalars.fund_irr_life_pct` |
| R-F13 | Fund gross IRR to 2025 incl. NAV (p90_1yr) | -6.77% | % | p90_1yr | 2025-12-31 view | `scenarios.p90_1yr.scalars.fund_irr_2025_pct` |
| R-F13 | Years with holdco shortfall (p90_1yr) | 6 | years | p90_1yr | 2025-12-31 view | `scenarios.p90_1yr.scalars.years_holdco_shortfall` |
| R-F13 | Portfolio CFADS 2026 (p90_10yr) | 61.8 | USD m | p90_10yr | 2025-12-31 view | `scenarios.p90_10yr.scalars.cfads_2026` |
| R-F13 | Minimum USPP DSCR (p90_10yr) | 1.35x | x | p90_10yr | 2025-12-31 view | `scenarios.p90_10yr.scalars.uspp_dscr_min_2026_2043` |
| R-F13 | Minimum holdco coverage 2023-2031 (p90_10yr) | 1.17x | x | p90_10yr | 2025-12-31 view | `scenarios.p90_10yr.scalars.holdco_cov_min_2023_2031` |
| R-F13 | Fund gross IRR, life (p90_10yr) | 8.36% | % | p90_10yr | 2025-12-31 view | `scenarios.p90_10yr.scalars.fund_irr_life_pct` |
| R-F13 | Fund gross IRR to 2025 incl. NAV (p90_10yr) | 1.71% | % | p90_10yr | 2025-12-31 view | `scenarios.p90_10yr.scalars.fund_irr_2025_pct` |
| R-F13 | Years with holdco shortfall (p90_10yr) | 3 | years | p90_10yr | 2025-12-31 view | `scenarios.p90_10yr.scalars.years_holdco_shortfall` |
| R-F13 | Portfolio CFADS 2026 (p99_1yr) | 54.2 | USD m | p99_1yr | 2025-12-31 view | `scenarios.p99_1yr.scalars.cfads_2026` |
| R-F13 | Minimum USPP DSCR (p99_1yr) | 1.19x | x | p99_1yr | 2025-12-31 view | `scenarios.p99_1yr.scalars.uspp_dscr_min_2026_2043` |
| R-F13 | Minimum holdco coverage 2023-2031 (p99_1yr) | 0.20x | x | p99_1yr | 2025-12-31 view | `scenarios.p99_1yr.scalars.holdco_cov_min_2023_2031` |
| R-F13 | Fund gross IRR, life (p99_1yr) | -0.74% | % | p99_1yr | 2025-12-31 view | `scenarios.p99_1yr.scalars.fund_irr_life_pct` |
| R-F13 | Fund gross IRR to 2025 incl. NAV (p99_1yr) | -22.02% | % | p99_1yr | 2025-12-31 view | `scenarios.p99_1yr.scalars.fund_irr_2025_pct` |
| R-F13 | Years with holdco shortfall (p99_1yr) | 13 | years | p99_1yr | 2025-12-31 view | `scenarios.p99_1yr.scalars.years_holdco_shortfall` |
| R-F13 | Portfolio CFADS 2026 (status_quo) | 65.3 | USD m | status_quo | 2025-12-31 view | `scenarios.status_quo.scalars.cfads_2026` |
| R-F13 | Minimum USPP DSCR (status_quo) | n.m. | x | status_quo | 2025-12-31 view | `scenarios.status_quo.scalars.uspp_dscr_min_2026_2043` |
| R-F13 | Minimum holdco coverage 2023-2031 (status_quo) | 1.40x | x | status_quo | 2025-12-31 view | `scenarios.status_quo.scalars.holdco_cov_min_2023_2031` |
| R-F13 | Fund gross IRR, life (status_quo) | 9.87% | % | status_quo | 2025-12-31 view | `scenarios.status_quo.scalars.fund_irr_life_pct` |
| R-F13 | Fund gross IRR to 2025 incl. NAV (status_quo) | 4.39% | % | status_quo | 2025-12-31 view | `scenarios.status_quo.scalars.fund_irr_2025_pct` |
| R-F13 | Years with holdco shortfall (status_quo) | 2 | years | status_quo | 2025-12-31 view | `scenarios.status_quo.scalars.years_holdco_shortfall` |
| R-F13 | Portfolio CFADS 2026 (sens_west_solar_capture_m5) | 65.1 | USD m | sens_west_solar_capture_m5 | 2025-12-31 view | `scenarios.sens_west_solar_capture_m5.scalars.cfads_2026` |
| R-F13 | Minimum USPP DSCR (sens_west_solar_capture_m5) | 1.43x | x | sens_west_solar_capture_m5 | 2025-12-31 view | `scenarios.sens_west_solar_capture_m5.scalars.uspp_dscr_min_2026_2043` |
| R-F13 | Minimum holdco coverage 2023-2031 (sens_west_solar_capture_m5) | 1.39x | x | sens_west_solar_capture_m5 | 2025-12-31 view | `scenarios.sens_west_solar_capture_m5.scalars.holdco_cov_min_2023_2031` |
| R-F13 | Fund gross IRR, life (sens_west_solar_capture_m5) | 10.85% | % | sens_west_solar_capture_m5 | 2025-12-31 view | `scenarios.sens_west_solar_capture_m5.scalars.fund_irr_life_pct` |
| R-F13 | Fund gross IRR to 2025 incl. NAV (sens_west_solar_capture_m5) | 9.83% | % | sens_west_solar_capture_m5 | 2025-12-31 view | `scenarios.sens_west_solar_capture_m5.scalars.fund_irr_2025_pct` |
| R-F13 | Years with holdco shortfall (sens_west_solar_capture_m5) | 2 | years | sens_west_solar_capture_m5 | 2025-12-31 view | `scenarios.sens_west_solar_capture_m5.scalars.years_holdco_shortfall` |
| R-F13 | Portfolio CFADS 2026 (sens_battery_low) | 65.3 | USD m | sens_battery_low | 2025-12-31 view | `scenarios.sens_battery_low.scalars.cfads_2026` |
| R-F13 | Minimum USPP DSCR (sens_battery_low) | 1.43x | x | sens_battery_low | 2025-12-31 view | `scenarios.sens_battery_low.scalars.uspp_dscr_min_2026_2043` |
| R-F13 | Minimum holdco coverage 2023-2031 (sens_battery_low) | 1.40x | x | sens_battery_low | 2025-12-31 view | `scenarios.sens_battery_low.scalars.holdco_cov_min_2023_2031` |
| R-F13 | Fund gross IRR, life (sens_battery_low) | 10.10% | % | sens_battery_low | 2025-12-31 view | `scenarios.sens_battery_low.scalars.fund_irr_life_pct` |
| R-F13 | Fund gross IRR to 2025 incl. NAV (sens_battery_low) | 7.64% | % | sens_battery_low | 2025-12-31 view | `scenarios.sens_battery_low.scalars.fund_irr_2025_pct` |
| R-F13 | Years with holdco shortfall (sens_battery_low) | 2 | years | sens_battery_low | 2025-12-31 view | `scenarios.sens_battery_low.scalars.years_holdco_shortfall` |
| R-F13 | Portfolio CFADS 2026 (sens_curtailment_p3) | 63.2 | USD m | sens_curtailment_p3 | 2025-12-31 view | `scenarios.sens_curtailment_p3.scalars.cfads_2026` |
| R-F13 | Minimum USPP DSCR (sens_curtailment_p3) | 1.39x | x | sens_curtailment_p3 | 2025-12-31 view | `scenarios.sens_curtailment_p3.scalars.uspp_dscr_min_2026_2043` |
| R-F13 | Minimum holdco coverage 2023-2031 (sens_curtailment_p3) | 1.27x | x | sens_curtailment_p3 | 2025-12-31 view | `scenarios.sens_curtailment_p3.scalars.holdco_cov_min_2023_2031` |
| R-F13 | Fund gross IRR, life (sens_curtailment_p3) | 9.68% | % | sens_curtailment_p3 | 2025-12-31 view | `scenarios.sens_curtailment_p3.scalars.fund_irr_life_pct` |
| R-F13 | Fund gross IRR to 2025 incl. NAV (sens_curtailment_p3) | 6.03% | % | sens_curtailment_p3 | 2025-12-31 view | `scenarios.sens_curtailment_p3.scalars.fund_irr_2025_pct` |
| R-F13 | Years with holdco shortfall (sens_curtailment_p3) | 3 | years | sens_curtailment_p3 | 2025-12-31 view | `scenarios.sens_curtailment_p3.scalars.years_holdco_shortfall` |
| R-F13 | Portfolio CFADS 2026 (sens_opex_p10) | 61.6 | USD m | sens_opex_p10 | 2025-12-31 view | `scenarios.sens_opex_p10.scalars.cfads_2026` |
| R-F13 | Minimum USPP DSCR (sens_opex_p10) | 1.35x | x | sens_opex_p10 | 2025-12-31 view | `scenarios.sens_opex_p10.scalars.uspp_dscr_min_2026_2043` |
| R-F13 | Minimum holdco coverage 2023-2031 (sens_opex_p10) | 1.14x | x | sens_opex_p10 | 2025-12-31 view | `scenarios.sens_opex_p10.scalars.holdco_cov_min_2023_2031` |
| R-F13 | Fund gross IRR, life (sens_opex_p10) | 8.61% | % | sens_opex_p10 | 2025-12-31 view | `scenarios.sens_opex_p10.scalars.fund_irr_life_pct` |
| R-F13 | Fund gross IRR to 2025 incl. NAV (sens_opex_p10) | 2.52% | % | sens_opex_p10 | 2025-12-31 view | `scenarios.sens_opex_p10.scalars.fund_irr_2025_pct` |
| R-F13 | Years with holdco shortfall (sens_opex_p10) | 4 | years | sens_opex_p10 | 2025-12-31 view | `scenarios.sens_opex_p10.scalars.years_holdco_shortfall` |
| R-F13 | Portfolio CFADS 2026 (sens_sofr_p100_unhedged) | 65.3 | USD m | sens_sofr_p100_unhedged | 2025-12-31 view | `scenarios.sens_sofr_p100_unhedged.scalars.cfads_2026` |
| R-F13 | Minimum USPP DSCR (sens_sofr_p100_unhedged) | 1.43x | x | sens_sofr_p100_unhedged | 2025-12-31 view | `scenarios.sens_sofr_p100_unhedged.scalars.uspp_dscr_min_2026_2043` |
| R-F13 | Minimum holdco coverage 2023-2031 (sens_sofr_p100_unhedged) | 1.24x | x | sens_sofr_p100_unhedged | 2025-12-31 view | `scenarios.sens_sofr_p100_unhedged.scalars.holdco_cov_min_2023_2031` |
| R-F13 | Fund gross IRR, life (sens_sofr_p100_unhedged) | 10.66% | % | sens_sofr_p100_unhedged | 2025-12-31 view | `scenarios.sens_sofr_p100_unhedged.scalars.fund_irr_life_pct` |
| R-F13 | Fund gross IRR to 2025 incl. NAV (sens_sofr_p100_unhedged) | 9.12% | % | sens_sofr_p100_unhedged | 2025-12-31 view | `scenarios.sens_sofr_p100_unhedged.scalars.fund_irr_2025_pct` |
| R-F13 | Years with holdco shortfall (sens_sofr_p100_unhedged) | 2 | years | sens_sofr_p100_unhedged | 2025-12-31 view | `scenarios.sens_sofr_p100_unhedged.scalars.years_holdco_shortfall` |
| R-F14 | Cash tax 2022 | 0.0 | USD m | base | 2022 | `scenarios.base.series.finance.tax.0` |
| R-F14 | NOL closing 2022 | 404.3 | USD m | base | 2022 | `scenarios.base.series.finance.nol_close.0` |
| R-F14 | Cash tax 2023 | 0.0 | USD m | base | 2023 | `scenarios.base.series.finance.tax.1` |
| R-F14 | NOL closing 2023 | 441.0 | USD m | base | 2023 | `scenarios.base.series.finance.nol_close.1` |
| R-F14 | Cash tax 2024 | 0.0 | USD m | base | 2024 | `scenarios.base.series.finance.tax.2` |
| R-F14 | NOL closing 2024 | 536.0 | USD m | base | 2024 | `scenarios.base.series.finance.nol_close.2` |
| R-F14 | Cash tax 2025 | 0.2 | USD m | base | 2025 | `scenarios.base.series.finance.tax.3` |
| R-F14 | NOL closing 2025 | 532.8 | USD m | base | 2025 | `scenarios.base.series.finance.nol_close.3` |
| R-F14 | Cash tax 2026 | 0.2 | USD m | base | 2026 | `scenarios.base.series.finance.tax.4` |
| R-F14 | NOL closing 2026 | 528.2 | USD m | base | 2026 | `scenarios.base.series.finance.nol_close.4` |
| R-F14 | Cash tax 2027 | 0.6 | USD m | base | 2027 | `scenarios.base.series.finance.tax.5` |
| R-F14 | NOL closing 2027 | 517.7 | USD m | base | 2027 | `scenarios.base.series.finance.nol_close.5` |
| R-F14 | Cash tax 2028 | 0.7 | USD m | base | 2028 | `scenarios.base.series.finance.tax.6` |
| R-F14 | NOL closing 2028 | 504.0 | USD m | base | 2028 | `scenarios.base.series.finance.nol_close.6` |
| R-F14 | Cash tax 2029 | 1.1 | USD m | base | 2029 | `scenarios.base.series.finance.tax.7` |
| R-F14 | NOL closing 2029 | 483.1 | USD m | base | 2029 | `scenarios.base.series.finance.nol_close.7` |
| R-F14 | Cash tax 2030 | 1.7 | USD m | base | 2030 | `scenarios.base.series.finance.tax.8` |
| R-F14 | NOL closing 2030 | 449.9 | USD m | base | 2030 | `scenarios.base.series.finance.nol_close.8` |
| R-F14 | Cash tax 2031 | 1.7 | USD m | base | 2031 | `scenarios.base.series.finance.tax.9` |
| R-F14 | NOL closing 2031 | 417.8 | USD m | base | 2031 | `scenarios.base.series.finance.nol_close.9` |
| R-F14 | Cash tax 2032 | 1.7 | USD m | base | 2032 | `scenarios.base.series.finance.tax.10` |
| R-F14 | NOL closing 2032 | 385.8 | USD m | base | 2032 | `scenarios.base.series.finance.nol_close.10` |
| R-F14 | Cash tax 2033 | 1.8 | USD m | base | 2033 | `scenarios.base.series.finance.tax.11` |
| R-F14 | NOL closing 2033 | 352.2 | USD m | base | 2033 | `scenarios.base.series.finance.nol_close.11` |
| R-F14 | Cash tax 2034 | 1.9 | USD m | base | 2034 | `scenarios.base.series.finance.tax.12` |
| R-F14 | NOL closing 2034 | 316.0 | USD m | base | 2034 | `scenarios.base.series.finance.nol_close.12` |
| R-F14 | Cash tax 2035 | 1.9 | USD m | base | 2035 | `scenarios.base.series.finance.tax.13` |
| R-F14 | NOL closing 2035 | 279.0 | USD m | base | 2035 | `scenarios.base.series.finance.nol_close.13` |
| R-F15 | USPP debt service 2026 | 45.6 | USD m | base | 2026 | `scenarios.base.series.finance.u_ds.4` |
| R-F15 | USPP DSCR 2026 | 1.43x | x | base | 2026 | `scenarios.base.series.finance.dscr_u.4` |
| R-F15 | USPP opening balance 2026 | 356.3 | USD m | base | 2026 | `scenarios.base.series.finance.u_open.4` |
| R-F15 | USPP debt service 2027 | 43.4 | USD m | base | 2027 | `scenarios.base.series.finance.u_ds.5` |
| R-F15 | USPP DSCR 2027 | 1.45x | x | base | 2027 | `scenarios.base.series.finance.dscr_u.5` |
| R-F15 | USPP opening balance 2027 | 332.3 | USD m | base | 2027 | `scenarios.base.series.finance.u_open.5` |
| R-F15 | USPP debt service 2028 | 40.4 | USD m | base | 2028 | `scenarios.base.series.finance.u_ds.6` |
| R-F15 | USPP DSCR 2028 | 1.53x | x | base | 2028 | `scenarios.base.series.finance.dscr_u.6` |
| R-F15 | USPP opening balance 2028 | 309.0 | USD m | base | 2028 | `scenarios.base.series.finance.u_open.6` |
| R-F15 | USPP debt service 2029 | 40.0 | USD m | base | 2029 | `scenarios.base.series.finance.u_ds.7` |
| R-F15 | USPP DSCR 2029 | 1.63x | x | base | 2029 | `scenarios.base.series.finance.dscr_u.7` |
| R-F15 | USPP opening balance 2029 | 287.5 | USD m | base | 2029 | `scenarios.base.series.finance.u_open.7` |
| R-F15 | USPP debt service 2030 | 34.7 | USD m | base | 2030 | `scenarios.base.series.finance.u_ds.8` |
| R-F15 | USPP DSCR 2030 | 1.90x | x | base | 2030 | `scenarios.base.series.finance.dscr_u.8` |
| R-F15 | USPP opening balance 2030 | 265.1 | USD m | base | 2030 | `scenarios.base.series.finance.u_open.8` |
| R-F15 | USPP debt service 2031 | 32.2 | USD m | base | 2031 | `scenarios.base.series.finance.u_ds.9` |
| R-F15 | USPP DSCR 2031 | 1.95x | x | base | 2031 | `scenarios.base.series.finance.dscr_u.9` |
| R-F15 | USPP opening balance 2031 | 246.7 | USD m | base | 2031 | `scenarios.base.series.finance.u_open.9` |
| R-F15 | USPP debt service 2032 | 30.0 | USD m | base | 2032 | `scenarios.base.series.finance.u_ds.10` |
| R-F15 | USPP DSCR 2032 | 2.03x | x | base | 2032 | `scenarios.base.series.finance.dscr_u.10` |
| R-F15 | USPP opening balance 2032 | 229.8 | USD m | base | 2032 | `scenarios.base.series.finance.u_open.10` |
| R-F15 | USPP debt service 2033 | 28.8 | USD m | base | 2033 | `scenarios.base.series.finance.u_ds.11` |
| R-F15 | USPP DSCR 2033 | 2.12x | x | base | 2033 | `scenarios.base.series.finance.dscr_u.11` |
| R-F15 | USPP opening balance 2033 | 214.2 | USD m | base | 2033 | `scenarios.base.series.finance.u_open.11` |
| R-F15 | USPP debt service 2034 | 28.6 | USD m | base | 2034 | `scenarios.base.series.finance.u_ds.12` |
| R-F15 | USPP DSCR 2034 | 2.19x | x | base | 2034 | `scenarios.base.series.finance.dscr_u.12` |
| R-F15 | USPP opening balance 2034 | 198.8 | USD m | base | 2034 | `scenarios.base.series.finance.u_open.12` |
| R-F15 | USPP debt service 2035 | 27.4 | USD m | base | 2035 | `scenarios.base.series.finance.u_ds.13` |
| R-F15 | USPP DSCR 2035 | 2.25x | x | base | 2035 | `scenarios.base.series.finance.dscr_u.13` |
| R-F15 | USPP opening balance 2035 | 182.7 | USD m | base | 2035 | `scenarios.base.series.finance.u_open.13` |
| R-F15 | USPP debt service 2036 | 27.3 | USD m | base | 2036 | `scenarios.base.series.finance.u_ds.14` |
| R-F15 | USPP DSCR 2036 | 2.25x | x | base | 2036 | `scenarios.base.series.finance.dscr_u.14` |
| R-F15 | USPP opening balance 2036 | 166.8 | USD m | base | 2036 | `scenarios.base.series.finance.u_open.14` |
| R-F15 | USPP debt service 2037 | 27.3 | USD m | base | 2037 | `scenarios.base.series.finance.u_ds.15` |
| R-F15 | USPP DSCR 2037 | 2.25x | x | base | 2037 | `scenarios.base.series.finance.dscr_u.15` |
| R-F15 | USPP opening balance 2037 | 150.0 | USD m | base | 2037 | `scenarios.base.series.finance.u_open.15` |
| R-F15 | USPP debt service 2038 | 27.4 | USD m | base | 2038 | `scenarios.base.series.finance.u_ds.16` |
| R-F15 | USPP DSCR 2038 | 2.25x | x | base | 2038 | `scenarios.base.series.finance.dscr_u.16` |
| R-F15 | USPP opening balance 2038 | 132.3 | USD m | base | 2038 | `scenarios.base.series.finance.u_open.16` |
| R-F15 | USPP debt service 2039 | 27.4 | USD m | base | 2039 | `scenarios.base.series.finance.u_ds.17` |
| R-F15 | USPP DSCR 2039 | 2.25x | x | base | 2039 | `scenarios.base.series.finance.dscr_u.17` |
| R-F15 | USPP opening balance 2039 | 113.4 | USD m | base | 2039 | `scenarios.base.series.finance.u_open.17` |
| R-F15 | USPP debt service 2040 | 27.5 | USD m | base | 2040 | `scenarios.base.series.finance.u_ds.18` |
| R-F15 | USPP DSCR 2040 | 2.25x | x | base | 2040 | `scenarios.base.series.finance.dscr_u.18` |
| R-F15 | USPP opening balance 2040 | 93.2 | USD m | base | 2040 | `scenarios.base.series.finance.u_open.18` |
| R-F15 | USPP debt service 2041 | 27.6 | USD m | base | 2041 | `scenarios.base.series.finance.u_ds.19` |
| R-F15 | USPP DSCR 2041 | 2.25x | x | base | 2041 | `scenarios.base.series.finance.dscr_u.19` |
| R-F15 | USPP opening balance 2041 | 71.6 | USD m | base | 2041 | `scenarios.base.series.finance.u_open.19` |
| R-F15 | USPP debt service 2042 | 27.7 | USD m | base | 2042 | `scenarios.base.series.finance.u_ds.20` |
| R-F15 | USPP DSCR 2042 | 2.25x | x | base | 2042 | `scenarios.base.series.finance.dscr_u.20` |
| R-F15 | USPP opening balance 2042 | 48.5 | USD m | base | 2042 | `scenarios.base.series.finance.u_open.20` |
| R-F15 | USPP debt service 2043 | 25.4 | USD m | base | 2043 | `scenarios.base.series.finance.u_ds.21` |
| R-F15 | USPP DSCR 2043 | 2.25x | x | base | 2043 | `scenarios.base.series.finance.dscr_u.21` |
| R-F15 | USPP opening balance 2043 | 23.9 | USD m | base | 2043 | `scenarios.base.series.finance.u_open.21` |
| R-F16 | Opco TL sculpted debt service 2022 | 30.0 | USD m | base | 2022-03-22 | `sizing.tl_ds.0` |
| R-F16 | Opco TL scheduled opening balance 2022 | 328.1 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.0` |
| R-F16 | Opco TL sculpted debt service 2023 | 33.6 | USD m | base | 2022-03-22 | `sizing.tl_ds.1` |
| R-F16 | Opco TL scheduled opening balance 2023 | 308.2 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.1` |
| R-F16 | Opco TL sculpted debt service 2024 | 30.8 | USD m | base | 2022-03-22 | `sizing.tl_ds.2` |
| R-F16 | Opco TL scheduled opening balance 2024 | 288.3 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.2` |
| R-F16 | Opco TL sculpted debt service 2025 | 30.4 | USD m | base | 2022-03-22 | `sizing.tl_ds.3` |
| R-F16 | Opco TL scheduled opening balance 2025 | 270.3 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.3` |
| R-F16 | Opco TL sculpted debt service 2026 | 29.9 | USD m | base | 2022-03-22 | `sizing.tl_ds.4` |
| R-F16 | Opco TL scheduled opening balance 2026 | 251.6 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.4` |
| R-F16 | Opco TL sculpted debt service 2027 | 27.8 | USD m | base | 2022-03-22 | `sizing.tl_ds.5` |
| R-F16 | Opco TL scheduled opening balance 2027 | 232.8 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.5` |
| R-F16 | Opco TL sculpted debt service 2028 | 25.5 | USD m | base | 2022-03-22 | `sizing.tl_ds.6` |
| R-F16 | Opco TL scheduled opening balance 2028 | 215.4 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.6` |
| R-F16 | Opco TL sculpted debt service 2029 | 26.1 | USD m | base | 2022-03-22 | `sizing.tl_ds.7` |
| R-F16 | Opco TL scheduled opening balance 2029 | 199.5 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.7` |
| R-F16 | Opco TL sculpted debt service 2030 | 23.6 | USD m | base | 2022-03-22 | `sizing.tl_ds.8` |
| R-F16 | Opco TL scheduled opening balance 2030 | 183.7 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.8` |
| R-F16 | Opco TL sculpted debt service 2031 | 23.4 | USD m | base | 2022-03-22 | `sizing.tl_ds.9` |
| R-F16 | Opco TL scheduled opening balance 2031 | 169.9 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.9` |
| R-F16 | Opco TL sculpted debt service 2032 | 23.1 | USD m | base | 2022-03-22 | `sizing.tl_ds.10` |
| R-F16 | Opco TL scheduled opening balance 2032 | 155.7 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.10` |
| R-F16 | Opco TL sculpted debt service 2033 | 22.8 | USD m | base | 2022-03-22 | `sizing.tl_ds.11` |
| R-F16 | Opco TL scheduled opening balance 2033 | 140.9 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.11` |
| R-F16 | Opco TL sculpted debt service 2034 | 22.4 | USD m | base | 2022-03-22 | `sizing.tl_ds.12` |
| R-F16 | Opco TL scheduled opening balance 2034 | 125.7 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.12` |
| R-F16 | Opco TL sculpted debt service 2035 | 22.0 | USD m | base | 2022-03-22 | `sizing.tl_ds.13` |
| R-F16 | Opco TL scheduled opening balance 2035 | 110.1 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.13` |
| R-F16 | Opco TL sculpted debt service 2036 | 22.0 | USD m | base | 2022-03-22 | `sizing.tl_ds.14` |
| R-F16 | Opco TL scheduled opening balance 2036 | 94.0 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.14` |
| R-F16 | Opco TL sculpted debt service 2037 | 21.9 | USD m | base | 2022-03-22 | `sizing.tl_ds.15` |
| R-F16 | Opco TL scheduled opening balance 2037 | 77.1 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.15` |
| R-F16 | Opco TL sculpted debt service 2038 | 21.9 | USD m | base | 2022-03-22 | `sizing.tl_ds.16` |
| R-F16 | Opco TL scheduled opening balance 2038 | 59.3 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.16` |
| R-F16 | Opco TL sculpted debt service 2039 | 21.9 | USD m | base | 2022-03-22 | `sizing.tl_ds.17` |
| R-F16 | Opco TL scheduled opening balance 2039 | 40.5 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.17` |
| R-F16 | Opco TL sculpted debt service 2040 | 21.9 | USD m | base | 2022-03-22 | `sizing.tl_ds.18` |
| R-F16 | Opco TL scheduled opening balance 2040 | 20.8 | USD m | base | 2022-03-22 | `sizing.tl_sched_open.18` |
| R-F17 | Repriced holdco opening balance 2026 | 137.6 | USD m | base | 2026 | `scenarios.base.series.finance.hc3_open.4` |
| R-F17 | Holdco coverage 2026 | 1.75x | x | base | 2026 | `scenarios.base.series.finance.hc_cov.4` |
| R-F17 | Repriced holdco opening balance 2027 | 132.1 | USD m | base | 2027 | `scenarios.base.series.finance.hc3_open.5` |
| R-F17 | Holdco coverage 2027 | 1.87x | x | base | 2027 | `scenarios.base.series.finance.hc_cov.5` |
| R-F17 | Repriced holdco opening balance 2028 | 126.4 | USD m | base | 2028 | `scenarios.base.series.finance.hc3_open.6` |
| R-F17 | Holdco coverage 2028 | 2.08x | x | base | 2028 | `scenarios.base.series.finance.hc_cov.6` |
| R-F17 | Repriced holdco opening balance 2029 | 119.9 | USD m | base | 2029 | `scenarios.base.series.finance.hc3_open.7` |
| R-F17 | Holdco coverage 2029 | 2.58x | x | base | 2029 | `scenarios.base.series.finance.hc_cov.7` |
| R-F17 | Repriced holdco opening balance 2030 | 111.3 | USD m | base | 2030 | `scenarios.base.series.finance.hc3_open.8` |
| R-F17 | Holdco coverage 2030 | 3.42x | x | base | 2030 | `scenarios.base.series.finance.hc_cov.8` |
| R-F17 | Repriced holdco opening balance 2031 | 99.7 | USD m | base | 2031 | `scenarios.base.series.finance.hc3_open.9` |
| R-F17 | Holdco coverage 2031 | 3.67x | x | base | 2031 | `scenarios.base.series.finance.hc_cov.9` |

New IDs: R-F11 A2 and A3 debt and early ratios (Chapters 31, 73); R-F12 opco debt by asset; R-F13 scenario and sensitivity results; R-F14 cash tax and NOL profile; R-F15 USPP debt service and DSCR profile; R-F16 opco term loan sculpted schedule; R-F17 repriced holdco profile.

