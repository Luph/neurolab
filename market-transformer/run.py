"""Walk-forward runner.  Usage: python run.py {predict|fair|linear} [n_seeds]"""
import os
import pickle
import sys
import time

import numpy as np
import torch

from mt.train import fixed_groups, folds, infer_fair, infer_predict, linear_bases, train_model

torch.set_num_threads(int(os.environ.get("THREADS", "4")))
OUT = os.environ.get("MT_OUT", "outputs")
os.makedirs(OUT, exist_ok=True)
kind = sys.argv[1]
n_seeds = int(sys.argv[2]) if len(sys.argv) > 2 else 2
u, A = pickle.load(open(os.environ["MT_CACHE"], "rb"))
classes = sorted(set(u.cls))
cls_ids = np.array([classes.index(c) for c in u.cls])
groups = fixed_groups(len(u.tickers))
A["groups"] = groups
F = folds(u.dates)
logf = open(f"{OUT}/log_{kind}.txt", "a")


def log(s):
    print(s, flush=True)
    logf.write(s + "\n")
    logf.flush()


for k, fold in enumerate(F):
    path = f"{OUT}/{kind}_fold{k}.npz"
    if os.path.exists(path):
        continue
    t0 = time.time()
    log(f"fold {k}: train {u.dates[fold['train'][0]].date()}..{u.dates[fold['train'][-1]].date()} "
        f"val ..{u.dates[fold['val'][-1]].date()} test {u.dates[fold['test'][0]].date()}..{u.dates[fold['test'][-1]].date()}")
    bpath = f"{OUT}/base_fold{k}.npz"
    if not os.path.exists(bpath):
        bp, bf = linear_bases(A, fold, groups)
        np.savez(bpath, bp=bp, bf=bf)
        np.savez(f"{OUT}/linear_fold{k}.npz", idx=fold["test"], pred=bp[fold["test"]], fair=bf[fold["test"]])
        log(f"  linear bases done {time.time() - t0:.0f}s")
    b = np.load(bpath)
    A["base_pred"], A["base_fair"] = b["bp"], b["bf"]
    if kind == "linear":
        pass
    else:
        preds = []
        for s in range(n_seeds):
            m = train_model(kind, A, cls_ids, fold, seed=100 * k + s, log=log)
            preds.append(infer_predict(m, A, cls_ids, fold["test"]) if kind == "predict"
                         else infer_fair(m, A, cls_ids, fold["test"], groups))
            if k == len(F) - 1:
                torch.save(m.state_dict(), f"{OUT}/{kind}_fold{k}_seed{s}.pt")
        np.savez(path, idx=fold["test"], pred=np.mean(preds, 0), seeds=np.stack(preds))
    log(f"  fold {k} done in {time.time() - t0:.0f}s")
