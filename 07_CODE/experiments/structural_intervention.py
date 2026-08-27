import sys, random, json
from collections import defaultdict
import numpy as np
from scipy.stats import binomtest

# Historical research script recovered from the ChatGPT Library.
# Original runtime depended on /mnt/data/tgcv_recovery/run_tgcv_protocol.py;
# that environment-specific dependency is intentionally documented rather than fabricated.
# Canonical result: 03_EXPERIMENTS/EXT-1.1_Rust/STRUCTURAL_INTERVENTION_RESULTS.json

ROOT='/mnt/data/tgcv_recovery/empirical_test_final'

def deg_signature(s):
    C=set(s['components']); E=set(map(tuple,s['edges']))
    out=sorted(sum(a==u for a,b in E) for u in C)
    inn=sorted(sum(b==u for a,b in E) for u in C)
    return tuple(sorted(s['components'])), tuple(s['resources']), len(E), tuple(out), tuple(inn)

def connected_variant(s, rng, g):
    C=sorted(s['components']); E=set(map(tuple,s['edges']))
    edges=list(E)
    if len(edges)<2: return None
    for _ in range(100):
        a,b=rng.sample(edges,2); u,v=a; x,y=b
        if len({u,v,x,y})<4: continue
        e1=(u,y); e2=(x,v)
        if e1 in E or e2 in E or e1==e2: continue
        E2=(E-{a,b})|{e1,e2}
        s2={'components':C,'edges':sorted(E2),'resources':list(s['resources'])}
        if any(g.any_path(set(C),E,c,d)!=g.any_path(set(C),E2,c,d) for c in C for d in C if c!=d):
            return s2
    return None

def run_state(s,obj,seed,g):
    rng=random.Random(seed); state=json.loads(json.dumps(s))
    for t in range(g.H):
        aa=g.acc(state)
        if not aa: break
        tr=rng.choice(aa); state=g.apply(state,tr)
    return int(g.goal(state,obj))

# Build matched pairs preserving conventional baseline.
# This is the recovered historical algorithm; see result file for sealed output.
