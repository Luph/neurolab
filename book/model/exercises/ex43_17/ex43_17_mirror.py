#!/usr/bin/env python3
"""Exercise 43.17 (u09 brief, Chapter 43): Cactus Ridge Solar and Storage (fictional; Illustrative).

Python mirror of the solution workbook ex43_17_solution.xlsx.  Inputs are Exhibit 43.8 as stated in
the brief (bible/briefs/u09.md, Exercise 43.17).  Interpretations where the brief is silent are listed
in INTERPRETATIONS and in model/exercises/README.md.

Run: python3 ex43_17_mirror.py   (prints the answers and the comparison with the brief)
"""
import json
from datetime import date
import calendar

INTERPRETATIONS = [
    "Construction months January to December 2027 (NTP January 1, 2027; COD January 1, 2028); cash flows dated at month ends.",
    "Contingency USD 9.6 million is spent in February to December 2027 in proportion to that month's PV EPC payment percentage (4.5, 6.0, ..., 4.0; they sum to 90.0).",
    "Interest during construction accrues each month at 7.25%/12 on the opening loan balance and is a use of that month, funded pro rata.",
    "The commitment fee accrues each month at 0.70%/12 on the undrawn commitment at the start of the month (commitment less opening balance).",
    "Every month's uses (hard costs, IDC, commitment fee, the upfront fee in January, the DSRA in December) are funded at the debt share D/T; equity is the rest.",
    "Operating half-years 2028H1 to 2047H2; solar P50 energy of operating year y is 512.8 GWh x 0.996^(y-1), compounding, 52% in H1 and 48% in H2.",
    "PPA price, battery capacity payment and fixed opex escalate on each January 1 (2028 = base year); the battery payment is 60 MW x 1,000 x USD 11.40 x 6 months per half-year.",
    "Tax: 30% on revenue less opex less interest less depreciation; depreciation is straight line over 40 half-years from 2028H1 on total uses less the DSRA; in the holiday half-years (2028 to 2030) no tax is due and any loss is lost; later losses carry forward without limit.",
    "CFADS = revenue - opex - tax.  Senior interest 3.625% per half-year on the opening balance; debt service sculpted to CFADS(sizing case)/1.30 in each of the 30 half-years 2028H1 to 2042H2; debt = present value of that debt service at 3.625%.",
    "Tax depends on interest and depreciation, which depend on the debt, so the sizing is iterated to a fixed point (debt to USD 1e-9 million); no circularity is left in the workbook, which holds the converged repayment profile as an input with a live check.",
    "DSRA: balance at each half-year end equals the next half-year's scheduled debt service (released in full at final maturity, 2042H2); top-ups and releases pass through the distribution account; the DSRA earns no interest.",
    "Distribution test: historic 12-month DSCR (this and the previous half-year; the period DSCR in 2028H1) at least 1.15x; cash failing the test is held and released when the test next passes.",
    "Equity IRR is XIRR on dated flows: monthly contributions at month ends (negative) and semiannual distributions at June 30 and December 31 (positive).",
    "Case runs keep the debt locked at the sizing-case amount and profile (principal by half-year).",
]

RATE_M = 0.0725 / 12
RATE_H = 0.03625
PV_PCT = [10.0, 4.5, 6.0, 8.5, 10.5, 12.0, 12.5, 11.0, 9.0, 7.0, 5.0, 4.0]


def month_end(y, m):
    return date(y, m, calendar.monthrange(y, m)[1])


M_DATES = [month_end(2027, m) for m in range(1, 13)]
H_DATES = [date(2028 + k // 2, 6 if k % 2 == 0 else 12, 30 if k % 2 == 0 else 31) for k in range(40)]
N_DEBT = 30


def hard_costs():
    pv = [168.4 * p / 100 for p in PV_PCT]
    bat = [0.0] * 12; bat[0] = 0.20 * 61.7; bat[9] = 0.80 * 61.7
    dev = [0.0] * 12; dev[0] = 12.9
    cont = [0.0] + [9.6 * p / sum(PV_PCT[1:]) for p in PV_PCT[1:]]
    return pv, bat, dev, cont


def operations(case):
    p90 = 0.917 if case in ('sizing', 'downside') else 1.0
    opex_f = 1.10 if case == 'downside' else 1.0
    rows = []
    for k in range(40):
        yr = 2028 + k // 2; oy = k // 2 + 1; share = 0.52 if k % 2 == 0 else 0.48
        energy = 512.8 * (1 - 0.004) ** (oy - 1) * share * p90           # GWh
        price = 49.80 * 1.015 ** (yr - 2028)
        rev_e = energy * price / 1000                                    # USD m
        rev_b = 60 * 1000 * 11.40 * 1.015 ** (yr - 2028) * 6 / 1e6
        opex = (4.36 * 1.025 ** (yr - 2028) / 2 + energy * 1.12 / 1000) * opex_f
        rows.append(dict(year=yr, energy=energy, price=price, rev_e=rev_e, rev_b=rev_b, rev=rev_e + rev_b, opex=opex,
                         ebitda=rev_e + rev_b - opex, holiday=1 if yr <= 2030 else 0))
    return rows


def construction(D, T):
    """Monthly funding at the debt share g = D/T; returns the monthly table."""
    g = D / T
    pv, bat, dev, cont = hard_costs()
    bal = 0.0; out = []
    for m in range(12):
        hard = pv[m] + bat[m] + dev[m] + cont[m]
        idc = bal * RATE_M
        cfee = (D - bal) * 0.007 / 12
        upf = 0.0175 * D if m == 0 else 0.0
        dsra = 0.0
        out.append(dict(hard=hard, idc=idc, cfee=cfee, upf=upf, dsra=dsra, bal_open=bal))
        bal += g * (hard + idc + cfee + upf)       # DSRA added in the caller for month 12
    return out


def tax_and_cfads(ops, interest, dep):
    loss = 0.0; res = []
    for k, o in enumerate(ops):
        ti = o['ebitda'] - interest[k] - dep
        if o['holiday']:
            tax = 0.0                              # holiday: no tax; any loss is lost
        else:
            use = min(loss, max(0.0, ti))
            loss = loss - use + max(0.0, -ti)
            tax = 0.30 * max(0.0, ti - use)
        res.append(tax)
    return res


def solve():
    """Fixed point: debt D, total funding T, repayment profile (sizing case)."""
    ops = operations('sizing')
    D, T = 180.0, 270.0
    prin = [D / N_DEBT] * N_DEBT
    for it in range(500):
        # construction at current D, T; DSRA = first half-year's debt service (from current profile)
        con = construction(D, T)
        ds1 = prin[0] + D * RATE_H
        uses = [c['hard'] + c['idc'] + c['cfee'] + c['upf'] for c in con]
        uses[11] += ds1
        T_new = sum(uses)
        cap = T_new - ds1
        dep = cap / 40
        # sculpting with tax: interest on the current profile
        bal = D; interest = []
        for k in range(40):
            interest.append(bal * RATE_H if k < N_DEBT else 0.0)
            if k < N_DEBT:
                bal -= prin[k]
        tax = tax_and_cfads(ops, interest, dep)
        cfads = [o['ebitda'] - t for o, t in zip(ops, tax)]
        ds = [c / 1.30 for c in cfads[:N_DEBT]]
        D_new = sum(d / (1 + RATE_H) ** (k + 1) for k, d in enumerate(ds))
        D_new = min(D_new, 0.75 * T_new)
        # principal profile from the sculpted debt service
        bal = D_new; prin_new = []
        for k in range(N_DEBT):
            p = ds[k] - bal * RATE_H
            prin_new.append(p); bal -= p
        err = abs(D_new - D) + abs(T_new - T) + max(abs(a - b) for a, b in zip(prin_new, prin))
        D, T, prin = D_new, T_new, prin_new
        if err < 1e-11:
            break
    con = construction(D, T)
    return dict(D=D, T=T, prin=prin, con=con, iterations=it + 1, dep=(T - (prin[0] + D * RATE_H)) / 40)


def run_case(sol, case):
    ops = operations(case)
    D, T, prin = sol['D'], sol['T'], sol['prin']
    g = D / T
    con = sol['con']
    ds1 = prin[0] + D * RATE_H
    uses = [c['hard'] + c['idc'] + c['cfee'] + c['upf'] for c in con]; uses[11] += ds1
    eq_m = [(1 - g) * u for u in uses]
    dep = (T - ds1) / 40
    bal = D; interest = []; principal = []
    for k in range(40):
        if k < N_DEBT:
            interest.append(bal * RATE_H); principal.append(prin[k]); bal -= prin[k]
        else:
            interest.append(0.0); principal.append(0.0)
    tax = tax_and_cfads(ops, interest, dep)
    cfads = [o['ebitda'] - t for o, t in zip(ops, tax)]
    ds = [i + p for i, p in zip(interest, principal)]
    dscr = [c / d if d > 1e-9 else None for c, d in zip(cfads, ds)]
    # DSRA and distributions with the lock-up test
    dsra_prev = ds1; locked = 0.0; dist = []; lockups = 0; hist = []
    for k in range(40):
        target = ds[k + 1] if k + 1 < 40 else 0.0
        move = dsra_prev - target                        # release (+) or top-up (-)
        cash = cfads[k] - ds[k] + move + locked
        if ds[k] > 1e-9:
            h = (cfads[k] + (cfads[k - 1] if k > 0 else 0.0)) / (ds[k] + (ds[k - 1] if k > 0 else 0.0))
        else:
            h = None
        hist.append(h)
        if h is not None and h < 1.15:
            locked = cash; dist.append(0.0); lockups += 1
        else:
            locked = 0.0; dist.append(cash)
        dsra_prev = target
    flows = [(d, -e) for d, e in zip(M_DATES, eq_m)] + list(zip(H_DATES, dist))
    rep = [x for x in dscr[:N_DEBT]]
    return dict(case=case, min_dscr=min(rep), avg_dscr=sum(cfads[:N_DEBT]) / sum(ds[:N_DEBT]), lockups=lockups,
                equity_irr=xirr(flows), equity=sum(eq_m), cfads=cfads, ds=ds, tax=tax, dist=dist, flows=flows,
                dscr=dscr, hist=hist)


def xirr(flows, guess=0.1):
    d0 = flows[0][0]
    def f(r):
        return sum(v / (1 + r) ** ((d - d0).days / 365) for d, v in flows)
    lo, hi = -0.9, 1.0
    for _ in range(300):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


BRIEF = dict(hard=252.600, idc=5.968, cfee=0.722, upf=3.245, dsra=10.636, T=273.171, D=185.425, gearcap=204.878,
             gearing=67.9, equity=87.746, ds1=10.636, sizing=(1.30, 1.30), base=(1.372, 1.383), downside=(1.275, 1.279),
             irr_base=9.83, irr_sizing=7.98, irr_down=7.51)


def answers():
    sol = solve()
    con = sol['con']; D, T = sol['D'], sol['T']
    ds1 = sol['prin'][0] + D * RATE_H
    out = dict(hard=sum(c['hard'] for c in con), idc=sum(c['idc'] for c in con), cfee=sum(c['cfee'] for c in con),
               upf=sum(c['upf'] for c in con), dsra=ds1, T=T, D=D, gearcap=0.75 * T, gearing=100 * D / T,
               equity=T - D, ds1=ds1, iterations=sol['iterations'])
    cases = {c: run_case(sol, c) for c in ('sizing', 'base', 'downside')}
    for c in cases:
        out[c] = (cases[c]['min_dscr'], cases[c]['avg_dscr'])
        out['lockups_' + c] = cases[c]['lockups']
    out['irr_base'] = 100 * cases['base']['equity_irr']; out['irr_sizing'] = 100 * cases['sizing']['equity_irr']
    out['irr_down'] = 100 * cases['downside']['equity_irr']
    return out, sol, cases


def compare(out):
    rows = []
    for k, v in BRIEF.items():
        x = out[k]
        if isinstance(v, tuple):
            for j, (a, b) in enumerate(zip(x, v)):
                dp = 2 if b in (1.30,) else 3
                rows.append((f'{k}[{"min" if j == 0 else "avg"}]', a, b, round(a, dp) == round(b, dp)))
        else:
            dp = len(str(v).split('.')[1]) if '.' in str(v) else 0
            rows.append((k, x, v, round(x, dp) == round(v, dp)))
    return rows


if __name__ == '__main__':
    out, sol, cases = answers()
    for k, a, b, ok in compare(out):
        print(f'{k:16s} mirror {a:12.5f}  brief {b:10}  {"OK" if ok else "DIFF"}')
    print('iterations', out['iterations'], 'lock-ups', {c: out['lockups_' + c] for c in cases})
