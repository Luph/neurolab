# Unit u09 glossary (Chapters 39 to 45)

Terms owned by Part VII. Home section numbers follow the u09 briefs. Terms used but owned elsewhere (IDC, commitment fee, ECA premium, CFADS, DSCR, LLCR, P50/P90, Monte Carlo simulation, XIRR) are not repeated here.

| Term | Abbreviation | Definition | Home section |
|---|---|---|---|
| financial model (project finance) | – | A spreadsheet that projects a project company's cash flows period by period and computes the debt, ratios and returns a decision depends on. | Section 39.1.1 |
| model blueprint | – | A one-page specification of the decisions, outputs, cases, periodicity, currencies, sheets, checks and ownership of a model, written before it is built. | Section 39.1.3 |
| FAST standard | FAST | A published spreadsheet modeling standard whose name stands for flexible, appropriate, structured and transparent. | Section 39.2.2 |
| sign convention | – | This book's rule that costs and outflows are stored as positive numbers on calculation sheets and subtracted explicitly. | Section 39.2.3 |
| model map | – | The list of a model's sheets in order with the purpose of each and the direction in which numbers flow between them. | Section 39.3.1 |
| corkscrew | – | A block of rows that rolls a balance forward: opening balance equal to the prior closing balance, additions, subtractions, closing balance. | Section 39.3.3 |
| model period | – | The span of time one column of a model represents, defined by a start date and an end date on the Time sheet. | Section 39.4.1 |
| stub period | – | A model period shorter than the standard period, such as the months between COD and the next June 30 or December 31. | Section 39.4.3 |
| year fraction | – | The length of a model period expressed in years under a day-count convention, held on its own row. | Section 39.4.3 |
| operating year | OY | The count of years of operation used for contract and tax rules; in this book's model, the period's months since COD rounded up to whole years. | Section 39.4.4 |
| flag | – | A row of 1s and 0s computed from dates that switches a calculation on or off in each period. | Section 39.5.1 |
| live column | – | The column of the Inputs sheet that holds the value of each scenario-dependent input for the case currently selected. | Section 39.6.2 |
| scenario selector | – | The single input cell, named Scenario, whose value selects which scenario column the model uses. | Section 39.6.2 |
| sensitivity flex | – | An input cell that moves one driver away from its scenario value by a stated amount while every other input stays fixed. | Section 39.6.3 |
| check row | – | A row that computes a difference that must equal zero when the model is working. | Section 39.7.1 |
| master check | – | The single cell that sums the absolute values of every check in the model and is shown on every sheet. | Section 39.7.2 |
| payment profile | – | The share of a contract price paid in each period, held as an input row and applied to the price. | Section 40.1.1 |
| total funding requirement | – | All uses of funds to COD, including financing costs and the initial reserve funding, that debt and equity together must pay. | Section 40.2.3 |
| drawdown order | – | The rule fixing whether equity is spent before, alongside or after debt during construction. | Section 40.3.1 |
| pro rata funding | – | A drawdown order in which each period's uses are paid by debt and equity in a fixed ratio. | Section 40.3.1 |
| equity-first funding | – | A drawdown order in which the sponsors' equity pays all uses until it is spent, and debt pays the rest. | Section 40.3.1 |
| debt-first funding | – | A drawdown order in which debt pays uses until it is fully drawn, with sponsors' equity commitments backed by letters of credit. | Section 40.3.1 |
| funding circularity | – | The loop in which the debt amount determines financing costs that are themselves funded partly by debt. | Section 40.5.1 |
| closed-form gross-up | – | An algebraic solution of an in-period loop, such as dividing a requirement by one minus the share that funds itself. | Section 40.5.3 |
| pasted value | – | A number written by a macro into an input cell to break a circular reference, with a calculated twin and a residual check beside it. | Section 40.5.4 |
| converge macro | – | A short macro that copies calculated values over their pasted twins and recalculates until the residual is below a tolerance. | Section 40.5.4 |
| circuit breaker | – | A switch that cuts a circular reference so a model with iterative calculation can be reset after an error. | Section 40.5.2 |
| convergence residual | – | The absolute difference between a pasted value and its calculated twin after recalculation. | Section 40.5.4 |
| availability cycle | – | The repeating pattern of planned outages over a plant's maintenance interval, which sets availability by operating year. | Section 41.1.1 |
| output degradation | – | The decline in a plant's net output over time, split into a non-recoverable trend and losses recovered at overhauls. | Section 41.1.3 |
| heat-rate headroom | – | The margin between the contracted heat rate used to charge fuel and the plant's actual heat rate, which leaves fuel profit or loss with the project company. | Section 41.1.3 |
| equivalent operating hours | EOH | Running hours plus a fixed number of hours charged for each start, used to schedule gas-turbine maintenance and price LTSA fees. | Section 41.1.4 |
| index reading date | – | The month whose index value sets a tariff at a reset date. | Section 41.2.2 |
| partial indexation | – | Indexation of only a stated share of a tariff component, the rest staying fixed in nominal terms. | Section 41.2.3 |
| reconversion | – | Converting a local-currency tariff share back to the tariff currency at the exchange rate on the invoice date. | Section 41.2.3 |
| pass-through test | – | A model row that subtracts a passed-through cost from the revenue that recovers it and must show only the contractual margin. | Section 41.3.4 |
| deferred holiday depreciation | – | Tax depreciation for tax-holiday years that the law treats as deferred and deductible in later years rather than lost. | Section 41.5.2 |
| thin capitalization | – | A tax rule that disallows interest on related-party debt above a stated ratio of debt to equity. | Section 41.5.3 |
| tax EBITDA | – | Earnings before interest, tax, depreciation and amortization as defined by a tax law for interest-limitation purposes. | Section 41.5.3 |
| interest reactivation | – | Deduction in a later year of interest disallowed earlier under an interest-limitation rule, when capacity appears. | Section 41.5.3 |
| minimum turnover tax | MTT | A tax on revenue payable when it exceeds the income tax computed on profit. | Section 41.5.5 |
| receivable days | – | The number of days of revenue outstanding as receivables at a balance date, used to model working capital. | Section 41.6 |
| VAT refund lag | – | The time between paying input VAT and receiving its refund from the tax authority. | Section 41.7 |
| waterfall tier | – | One level of a priority of payments in a model, built as cash available, amount due, amount paid and remainder. | Section 42.1.2 |
| all-in cost factor | – | The period's total senior interest cost per unit of scheduled debt, including margins, swap settlement and gross-up, used to discount target debt service. | Section 42.2.1 |
| debt capacity | – | The present value, at the all-in cost, of the target debt service in every repayment period. | Section 42.2.2 |
| scheduled balance | – | The senior debt balance that would result from scheduled repayments alone, used to sculpt without feedback from sweeps. | Section 42.2.4 |
| sizing mode | – | The state of a model in which the debt amount and repayment profile are recalculated from CFADS. | Section 42.2.8 |
| locked-debt mode | – | The state of a model in which the debt amount, repayment profile and swap notional are held at pasted values so that tests show their effect on ratios. | Section 42.2.8 |
| lock-up account | – | The account in which cash that fails the distribution test is held until the test is passed or the cash is swept. | Section 42.3.3 |
| distribution flag | – | A model row equal to 1 when every condition for paying shareholders is met in a period. | Section 42.4.1 |
| trapped cash | – | Cash available for shareholders that cannot lawfully be paid as dividends because distributable reserves are insufficient. | Section 42.5.2 |
| dividend trap | – | The situation in which a project company has cash for shareholders but negative or insufficient retained earnings, so dividends are unlawful. | Section 42.5.2 |
| distributable reserves | – | The accumulated profits a company may lawfully distribute as dividends. | Section 42.5.2 |
| balance check | – | A model row equal to total assets minus total liabilities and equity, which must be zero in every period. | Section 42.6.2 |
| historic DSCR (model) | – | The ratio of CFADS to debt service over the twelve months ending at a test date, computed from two semiannual periods. | Section 43.1.1 |
| projected DSCR (model) | – | The ratio of projected CFADS to scheduled debt service over the twelve months after a test date. | Section 43.1.1 |
| equity cash flow | – | The net cash flow between the sponsors and the project company in a period: contributions negative, interest, principal and dividends received positive. | Section 43.2.1 |
| project IRR | – | The internal rate of return on the project's cash flows before financing, under the tax convention the model states. | Section 43.2.3 |
| sizing case | – | The scenario on which the debt amount and repayment profile are computed. | Section 43.3.1 |
| test case | – | A scenario run with the debt locked at the sizing-case profile to measure its effect on ratios and returns. | Section 43.3.1 |
| tornado chart | – | A bar chart of sensitivities ranked by the size of their effect on one output. | Section 43.4.2 |
| breakeven | – | The value of one input at which an output reaches a stated threshold, such as a DSCR of 1.00x. | Section 43.4.3 |
| draw table | – | A pasted table of random draws, generated with a recorded seed, that a Monte Carlo run reads by run number. | Section 43.5.2 |
| dashboard | – | A one-page output sheet that presents the results a decision-maker needs with the model's check status and version. | Section 43.6.1 |
| reasonableness warning | – | A check that flags an output outside a plausible range without counting as a model error. | Section 43.7.2 |
| model audit | – | An independent examination of a financial model's structure, formulas, inputs and outputs against its source documents, ending in a written opinion. | Section 44.1.1 |
| model review | – | A limited examination of a model, narrower than an audit, that does not end in a full opinion. | Section 44.1.2 |
| shadow model | – | A short independent model that reproduces a key output of another model to test it. | Section 44.1.2 |
| reperformance | – | Recomputing a model's results independently from the same inputs. | Section 44.1.2 |
| unique formula | – | A formula that differs from its neighbor in the same row, so that reviewing all unique formulas reviews the whole model. | Section 44.2.3 |
| analytical review | – | Testing a model by examining the shape and plausibility of its outputs rather than its formulas. | Section 44.2.5 |
| flex testing | – | Changing switches and inputs, including to extremes, to check that outputs move as they should and only as they should. | Section 44.2.7 |
| findings log | – | The auditor's record of each finding with its location, effect, grade, recommendation, responses and status. | Section 44.2.8 |
| scenario leak | – | An error that has no effect in the base case but distorts results when another scenario or sensitivity runs. | Section 44.3.5 |
| materiality threshold | – | The size of effect on a decision output above which a finding must be fixed before the model is relied on. | Section 44.2.1 |
| sector module | – | The block of model rows that turns a sector's physical and contract drivers into revenue and variable-cost drivers for the core model. | Section 45.1 |
| net energy yield | – | Expected annual energy delivered after all modeled losses, before uncertainty. | Section 45.2.1 |
| interannual variability | IAV | The year-to-year variation of a renewable resource around its long-term mean, expressed as a standard deviation. | Section 45.2.1 |
| ten-year P90 | – | The energy level that average annual output over ten years is expected to exceed with 90% probability. | Section 45.2.1 |
| diversification benefit | – | The amount by which a portfolio's P90 exceeds the sum of its assets' stand-alone P90s. | Section 45.2.3 |
| state of health | SOH | A battery's usable energy capacity as a share of its nameplate capacity. | Section 45.3.2 |
| augmentation | – | Adding battery modules to restore usable capacity lost to fade. | Section 45.3.2 |
| capture ratio | – | The ratio of the price an asset earns on its own output profile to the average price at its reference hub. | Section 45.4.2 |
| ramp-up | – | The period after opening in which traffic rises toward its mature level as users learn and adopt a new road. | Section 45.5.2 |
| toll elasticity | – | The percentage change in traffic for a 1% change in the toll. | Section 45.5.3 |
| head grade | – | The metal content of ore fed to the processing plant. | Section 45.6.1 |
| metallurgical recovery | – | The share of contained metal in the ore that the plant recovers into concentrate. | Section 45.6.2 |
| payable metal | – | The quantity of metal in concentrate that the buyer pays for after the contract's deductions. | Section 45.6.2 |
| net smelter return | NSR | The value of concentrate after treatment and refining charges, penalties and freight. | Section 45.6.2 |
| reserve tail | – | Reserves remaining after the final debt maturity, expressed as a share of the original reserves. | Section 45.6.3 |
| liquefaction fee | – | The fixed charge per unit of contracted LNG capacity that a buyer pays whether or not it lifts cargoes. | Section 45.7.1 |
| oil-price slope | – | The coefficient that links a gas or LNG price to an oil price index. | Section 45.7.2 |
| unitary charge | – | The single periodic payment an authority makes under an availability-based PPP, before deductions. | Section 45.8.1 |
| availability deduction | – | The reduction of a unitary charge for an unavailable unit of service, weighted by unit, time and severity. | Section 45.8.1 |
| performance points | – | Points incurred for service failures that convert into payment deductions once thresholds are passed. | Section 45.8.1 |
