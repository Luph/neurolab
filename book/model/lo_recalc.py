"""Recalculate an .xlsx in headless LibreOffice through UNO, iterating hard recalculations until
the watched cells stop changing, then save a copy with cached values (read by openpyxl with
data_only=True). Usage: python3 lo_recalc.py in.xlsx out.xlsx [scenario] [contribution_option]

Each calculateAll() runs LibreOffice's iterative solver (iterations enabled in the file); the
model's circular block (financing costs, sizing, sculpting) converges as a fixed point over
repeated passes, as it would in Excel pressing F9 with iterative calculation on.
"""
import os
import subprocess
import sys
import time

import uno
from com.sun.star.beans import PropertyValue


def prop(name, value):
    p = PropertyValue()
    p.Name, p.Value = name, value
    return p


def connect(port):
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
    for _ in range(100):
        try:
            return resolver.resolve(f"uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext")
        except Exception:
            time.sleep(0.2)
    raise RuntimeError("cannot connect to soffice")


def recalc(src, dst, scenario=None, contrib=None, port=2002, max_passes=400, tol=1e-9):
    proc = subprocess.Popen(["soffice", "--headless", "--invisible", "--nologo", "--norestore",
                             f"--accept=socket,host=localhost,port={port};urp;"],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        ctx = connect(port)
        smgr = ctx.ServiceManager
        desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
        url = uno.systemPathToFileUrl(os.path.abspath(src))
        doc = desktop.loadComponentFromURL(url, "_blank", 0, (prop("Hidden", True),))
        doc.IsIterationEnabled = True
        doc.IterationCount = 1000
        doc.IterationEpsilon = 1e-10
        sh_in = doc.Sheets.getByName("Inputs")
        rows = {}
        for r in range(0, 40):
            lab = sh_in.getCellByPosition(3, r).getString()
            if lab.startswith("Scenario (1-13"):
                rows["scen"] = r
            if lab.startswith("Contribution option"):
                rows["contrib"] = r
        if scenario is not None:
            sh_in.getCellByPosition(5, rows["scen"]).setValue(scenario)
        if contrib is not None:
            sh_in.getCellByPosition(5, rows["contrib"]).setValue(contrib)
        out = doc.Sheets.getByName("Outputs")
        watch = [out.getCellByPosition(5, r) for r in range(5, 30)]
        # also watch whole-row sums of key timeline rows via the Checks sheet
        chk = doc.Sheets.getByName("Checks")
        watch += [chk.getCellByPosition(5, r) for r in range(5, 25)]
        prev = None
        passes = 0
        for passes in range(1, max_passes + 1):
            doc.calculateAll()
            vals = [c.getValue() for c in watch]
            if prev is not None and max(abs(a - b) for a, b in zip(vals, prev)) < tol and passes > 5:
                break
            prev = vals
        dst_url = uno.systemPathToFileUrl(os.path.abspath(dst))
        doc.storeToURL(dst_url, (prop("FilterName", "Calc Office Open XML"),))
        doc.close(True)
        return passes
    finally:
        try:
            desktop.terminate()
        except Exception:
            pass
        proc.wait(timeout=60)


if __name__ == "__main__":
    a = sys.argv
    sc = int(a[3]) if len(a) > 3 else None
    co = int(a[4]) if len(a) > 4 else None
    n = recalc(a[1], a[2], sc, co)
    print("passes", n)
