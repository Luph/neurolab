import json, re
H='/home/user/neurolab/book'
o=json.load(open(f'{H}/model/outputs_case_p.json')); P=o['figures']
lines=open(f'{H}/bible/case-bible.md').read().split('\n')
i0=[i for i,l in enumerate(lines) if l.startswith('| Ch | Case | Story date')][0]
rows=[]
for l in lines[i0+2:]:
    if not l.startswith('|'): break
    c=[x.strip() for x in l.strip('|').split('|')]
    if 'P' in c[1].replace('(small)','').split(', ') or c[1].startswith('P'): rows.append(c)
extra={  # additional figure IDs and notes per chapter
 '5':('P-F02','Indices are the September 2021 readings; FX 654.9 (2022H1 average); capacity 581.9 MW applies (reset at taking-over in November 2021).'),
 '6':('P-F03, P-F22','P-F03 uses an approximate July 2016 LIBOR of 0.95% (fact-check). The CAS costs little because 80% of the debt is swapped and the model sets the swap floating leg equal to the loan base rate.'),
 '7':('P-F04','Lenders reporting basis (fixed-asset model); say once that the IFRS accounts present the PPA as an IFRIC 12 financial asset (P-F56, Chapter 66); the receivable increase includes USD 18.4 million overdue at June 30 and 68.9 at December 31, 2022; deferred tax is an asset. Do not explain covenants.'),
 '8':('P-F05','Debt is forced to each gearing level on the sculpted profile; at 75% and 80% the minimum DSCR is below 1.35x (the DSCR test binds at 74.1%).'),
 '18':('P-F02, P-F32, P-F39','LC on the two-plus-one formula: P-F39 (USD 36.2 million in 2022; P-C44 replaces the earlier 33.8).'),
 '24':('P-F11, P-F34','MMRA contributions are inside CFADS.'),
 '25':('P-F35','Downside dispatch is 76.5% (Bible 1.10 definition); the 50% dispatch sensitivity is the case that triggers take-or-pay.'),
 '32':('P-F07','Equity lines only.'),
 '35':('P-F10, P-F08, P-F41','First full operating year: FC base July 1, 2021 to June 30, 2022; actual calendar 2022 (annex 4.15). LLCR includes the DSRA.'),
 '36':('P-F08, P-F09, P-F36','DSCR (1.35x) binds at USD 633.3 million; gearing cap would allow 642.9; downside 1.20x gives 633.4 (all within 1.5%). ECA first repayment tested at 24 months (2018 OECD terms).'),
 '37':('P-F11, P-F12','Swap notional accretes with the FC drawdown and amortizes with the contract profile.'),
 '38':('P-F12','Show all-in cost variants with and without PRI, WHT gross-up and financed ECA premium.'),
 '40':('P-F07, P-F13, P-F37, P-F43','Closed-form gross-up (alpha/beta) is the workbook method; Python iterates.'),
 '41':('P-F14, P-F32, P-F34, P-F37, P-F38, P-F44','Thin cap per P-F38 rule.'),
 '42':('P-F15, P-F41','Without shareholder loans, up to USD 172.8 million would be trapped.'),
 '43':('P-F16, P-F42','Breakevens and Monte Carlo are Python outputs.'),
 '44':('P-F17','Exercise workbook Case_P_Model_AuditExercise.xlsx carries the ten errors; E9 shows only off the 76.5% dispatch (banking case).'),
 '55':('P-F07','Funds flow at July 17, 2018: Month 1 uses in P-F13.'),
 '56':('P-F36',''),
 '59':('P-F20, P-F25, P-F40','2022 dispatch was 84.0% / 81.5% (drought). The LC drawn in February 2023 is the 2023 reset value (P-F40, P-C44). 80% of the overdue amounts are energy-charge arrears matched by deferred SNHK/GCK payables (modeler calibration A1). The DSRA is drawn only at June 30, 2023 (USD 2.5 million). Leave the breach and waiver to Chapter 62.'),
 '61':('P-F18, P-F19, P-F30, P-F52, P-F66','Overrun includes the calibrated delay-related EPC acceleration and owner cost escalation (P-C43). Funding order: contingency (base facilities), delay LDs, DSU, then standby (about USD 10.0 million) and contingent equity (about 3.3 million). The FX forwards gained for the project.'),
 '62':('P-F21, P-F31','Historic DSCR 1.14x at December 31, 2022 (lock-up only) and 0.97x at June 30, 2023 (default); release in 2024H2.'),
 '63':('P-F23, P-F24',''),
 '65':('P-F29',''),
 '66':('P-F26','IFRS basis is IFRIC 12 (annex 4.6): on IFRS carrying amounts the loss of control gives a loss, on the lenders basis a gain (both in P-F26); fair value of the retained 36% = sale price per point x 36; hedge reserve recycled.'),
 '67':('P-F27, P-F38',''),
 '69':('P-F16',''),
 '86':('P-F28',''),
 '47':('P-F06','Levelized tariff USD 73.00/MWh in 2016 prices; runner-up 4.6% higher.'),
 '17':('P-F25 (formula only)',''),
}
L=['# Case state by chapter: Case P (Bélanou)','',
 'Model version 1.2 (Case Bible annex P absorbed; editor rulings applied) (`model/case_p.py`, `model/Case_P_Model.xlsx`); story as of October 3, 2026. For every chapter of Case Bible Part 6 that features Case P: the state of the case at the start and end of the installment (Bible storyline plus modeled state) and the ledger figure IDs (`model/figure-ledger-case-p.md`) the chapter may print. "Inputs" means Case Bible Part 1 values after the change log.','',
 '| Ch | Story date | State at start | State at end | Figure IDs the chapter shows | Notes for the writer |','|---|---|---|---|---|---|']
ADD={'21':['P-F46'],'75':['P-F46','P-F59'],'18':['P-F47'],'48':['P-F47','P-F61'],'24':['P-F48'],'28':['P-F48'],'65':['P-F48'],
 '55':['P-F49'],'38':['P-F50', 'P-F65'],'56':['P-F50'],'27':['P-F51'],'60':['P-F51'],'61':['P-F52'],'66':['P-F53','P-F56','P-F66'],'67':['P-F54','P-F37'],
 '68':['P-F55'],'86':['P-F55','P-F39'],'7':['P-F56 (one-line note)'],'69':['P-F57'],'72':['P-F58'],'85':['P-F60'],'47':['P-F62', 'P-F64'],'46':['P-F64'],'59':['P-F39', 'P-F66'],'62':['P-F63'],
 '31':['P-F37'],'35':['P-F16 (breakevens)'],'43':['P-F42'],'40':['P-F43', 'P-F65'],'41':['P-F44'],'42':['P-F45'],'37':['P-F11a', 'P-F65'],'24b':[]}
for c in rows:
    ch,case,dt,scene,chars,figs,st,en=c[:8]
    ids,note=extra.get(ch,(figs,''))
    ids=ids.replace('P-F11,','P-F11a, P-F11b,').replace('P-F11 ','P-F11a/b ')
    for x in ADD.get(ch,[]):
        if x.split(' ')[0] not in ids: ids=(ids+', '+x) if ids not in ('None','–','') else x
    if ids!=figs and figs not in ('None','–') and not figs.startswith('Inputs'):
        pass
    if figs.startswith('Inputs') and ch not in extra: ids=figs
    L.append(f'| {ch} | {dt} | {st} | {en} | {ids} | {note} |')
S=P['P-F20']
L+=['','State of Case P at key dates (for chapters that refer back):','','| Date | State | Figures |','|---|---|---|',
 f"| 2018-07-17 | Financial close: senior debt USD {P['P-F08']['senior_debt']:.1f} million (DSCR-bound), total funding USD {P['P-F07']['uses']['total']:.1f} million, gearing {P['P-F07']['gearing']*100:.1f}% | P-F07, P-F08 |",
 f"| 2021-05-01 | Scheduled COD (FC base); DSRA USD {P['P-F11']['dsra_initial']:.1f} million | P-F11 |",
 "| 2021-12-01 | Actual COD; capacity reset to 581.9 MW; standby not drawn | P-F18, P-F19 |",
 "| 2022-06-30 | First repayment; USD 18.485 million LD prepayment | P-F19, P-F20 |",
 f"| 2022-12-31 | Historic DSCR {P['P-F21']['historic_dscr_2022_12_31']:.2f}x: lock-up | P-F20, P-F21 |",
 f"| 2023-06-30 | Historic DSCR {P['P-F21']['historic_dscr_2023_06_30']:.2f}x: event of default; DSRA drawn | P-F21, P-F25 |",
 "| 2023-10-26 | Waiver and amendment | P-F21 |",
 f"| 2024-12-31 | Lock-up released ({P['P-F21']['release_period']}) | P-F20 |",
 f"| 2025-06-30 | Bond USD {P['P-F23']['bond_face']:.1f} million; commercial, B-loan and standby prepaid | P-F23 |",
 f"| 2026-09-30 | 24% sold at USD {P['P-F24']['price_at_completion']:.1f} million; Kilnworth 36% | P-F24, P-F26 |"]
open(f'{H}/model/case-state-case-p.md','w').write('\n'.join(L)+'\n')
print(len(rows))
