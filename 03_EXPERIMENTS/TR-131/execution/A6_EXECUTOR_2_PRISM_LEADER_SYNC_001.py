#!/usr/bin/env python3
"""TGCV TR-131 A6 Executor-2: independent PRISM leader_sync3_2 reconstruction.

This implementation deliberately uses explicit transition tables and relational
state rewriting rather than Executor-1's procedural state construction.
"""
from __future__ import annotations
import argparse, hashlib, json
from itertools import product
from pathlib import Path

EXPECTED_SHA = "bf96477357435e16a41c904bd91b63660246fd2f"

def canon(d):
    return tuple((k, d[k]) for k in sorted(d))

def load_fixture(path):
    b = path.read_bytes()
    h = hashlib.sha256(b).hexdigest()
    if h != EXPECTED_SHA:
        raise RuntimeError(f"FIXTURE_SHA_MISMATCH expected={EXPECTED_SHA} actual={h}")
    return h

def initial():
    d = {"c":1}
    for i in range(1,4):
        d.update({f"s{i}":0, f"u{i}":False, f"v{i}":0, f"p{i}":0})
    return canon(d)

def enabled(s):
    d = dict(s)
    labels = set()
    if d["s1"] == 0: labels.add("pick")
    if d["s1"] == 1: labels.add("read")
    if d["s1"] == 2:
        labels.add("done" if any(d[f"u{i}"] for i in range(1,4)) else "retry")
    if d["s1"] == 3: labels.add("loop")
    return tuple(sorted(labels))

def rewrite_pick(s, choice):
    d = dict(s)
    for i, value in enumerate(choice, 1):
        d[f"s{i}"] = 1
        d[f"p{i}"] = value
        d[f"v{i}"] = value
        d[f"u{i}"] = True
    return canon(d)

def rewrite_read(s):
    d = dict(s)
    old_v = {i:d[f"v{i}"] for i in range(1,4)}
    old_p = {i:d[f"p{i}"] for i in range(1,4)}
    nxt = {1:old_v[2], 2:old_v[3], 3:old_v[1]}
    for i in range(1,4):
        d[f"u{i}"] = old_p[i] != nxt[i]
        d[f"v{i}"] = nxt[i]
    d["c"] = 2
    for i in range(1,4):
        d[f"s{i}"] = 2
        d[f"v{i}"] = 0
        d[f"p{i}"] = 0
    return canon(d)

def rewrite_branch(s, label):
    d = dict(s)
    if label == "retry":
        for i in range(1,4):
            d[f"s{i}"] = 0
            d[f"u{i}"] = False
            d[f"v{i}"] = 0
            d[f"p{i}"] = 0
        d["c"] = 1
    elif label == "done":
        for i in range(1,4):
            d[f"s{i}"] = 3
            d[f"u{i}"] = False
            d[f"v{i}"] = 0
            d[f"p{i}"] = 0
    else:
        raise ValueError(label)
    return canon(d)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fixture", type=Path)
    ap.add_argument("-o","--output",type=Path,required=True)
    args = ap.parse_args()
    digest = load_fixture(args.fixture)
    s0 = initial()
    rows = [{"kind":"state","id":"S0","state":s0,"t_acc":enabled(s0)}]
    for choice in sorted(product((0,1), repeat=3)):
        s1 = rewrite_pick(s0, choice)
        rows.append({"kind":"realization","source":"S0","transformation":"pick",
                     "realization":choice,"successor":s1,"t_acc":enabled(s1)})
        s2 = rewrite_read(s1)
        rows.append({"kind":"transition","source":s1,"transformation":"read",
                     "successor":s2,"t_acc":enabled(s2)})
        label = enabled(s2)[0]
        s3 = rewrite_branch(s2, label)
        rows.append({"kind":"transition","source":s2,"transformation":label,
                     "successor":s3,"t_acc":enabled(s3)})
    result = {"executor":"EXECUTOR_2","fixture_sha256":digest,"rows":rows}
    args.output.write_text(json.dumps(result,sort_keys=True,indent=2),encoding="utf-8")
if __name__ == "__main__":
    main()
