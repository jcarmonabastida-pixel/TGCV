"""N-R8.3 operationalisation primitives.

Result-blind implementation of G2, matched-state construction primitives,
and the independent R2 representation. No learner, outcome, trajectory, or
N-R7 result dependency is permitted.
"""
from __future__ import annotations

import hashlib
import json
import math
import random
from dataclasses import dataclass
from typing import Iterable, Sequence

FAMILIES = ("ADD_COMPONENT", "REMOVE_COMPONENT", "ADD_EDGE", "REMOVE_EDGE", "REWIRE_EDGE", "MODIFY_RESOURCE")
OBJECTIVES = tuple(f"O{i:02d}" for i in range(1, 13))
COMPONENTS = ("A1", "A2", "B1", "B2", "C1", "C2")

@dataclass(frozen=True)
class State:
    components: tuple[str, ...]
    edges: tuple[tuple[str, str], ...]
    resources: tuple[int, int, int]
    objective: str
    def canonical(self) -> dict:
        return {"components": list(self.components), "edges": [list(e) for e in self.edges], "objective": self.objective, "resources": list(self.resources)}
    def sha256(self) -> str:
        b = json.dumps(self.canonical(), sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
        return hashlib.sha256(b).hexdigest()

def canonical_state(components: Iterable[str], edges: Iterable[tuple[str,str]], resources: Sequence[int], objective: str) -> State:
    raw_edges = list(edges)
    c = tuple(sorted(components)); e = tuple(sorted(raw_edges))
    if len(e) != len(set(e)): raise ValueError("duplicate edge")
    if any(a == b for a,b in e): raise ValueError("self-loop")
    if any(a not in c or b not in c for a,b in e): raise ValueError("edge endpoint absent")
    if objective not in OBJECTIVES: raise ValueError("invalid objective")
    if len(resources) != 3 or any(int(x) not in range(4) for x in resources): raise ValueError("invalid resources")
    return State(c, e, tuple(map(int, resources)), objective)

def generate_g1(rng: random.Random) -> State:
    n = rng.choice((3,4,5)); c = rng.sample(list(COMPONENTS), n)
    possible = [(a,b) for a in c for b in c if a != b]; k = rng.randint(0, len(possible))
    return canonical_state(c, rng.sample(possible, k), tuple(rng.randrange(4) for _ in range(3)), rng.choice(OBJECTIVES))

def _round_half_up(x: float) -> int: return math.floor(x + 0.5)

def generate_g2(rng: random.Random) -> State:
    n = rng.choices((3,4,5), weights=(0.10,0.30,0.60), k=1)[0]
    c = rng.sample(list(COMPONENTS), n); possible = [(a,b) for a in c for b in c if a != b]
    d = rng.choices((0.20,0.50,0.80), weights=(0.50,0.30,0.20), k=1)[0]
    k = max(0, min(len(possible), _round_half_up(d * len(possible))))
    r = tuple(rng.choices((0,1,2,3), weights=(0.10,0.20,0.30,0.40), k=1)[0] for _ in range(3))
    o = rng.choices(OBJECTIVES, weights=(0.10,)*6 + (1/15,)*6, k=1)[0]
    return canonical_state(c, rng.sample(possible, k), r, o)

def enumerate_transformations(s: State) -> list[tuple]:
    c=set(s.components); edges=set(s.edges); out=[]
    for x in COMPONENTS:
        if x not in c and len(c) < 6: out.append(("ADD_COMPONENT", x))
    for x in sorted(c):
        if len(c) > 1: out.append(("REMOVE_COMPONENT", x))
    for a in sorted(c):
        for b in sorted(c):
            if a != b and (a,b) not in edges: out.append(("ADD_EDGE", a,b))
    for a,b in sorted(edges): out.append(("REMOVE_EDGE", a,b))
    for u,v in sorted(edges):
        for w in sorted(c):
            if w != u and w != v and (u,w) not in edges: out.append(("REWIRE_EDGE", u,v,w))
    for i in range(3):
        for d in (-1,1):
            if 0 <= s.resources[i] + d <= 3: out.append(("MODIFY_RESOURCE", i, d))
    return sorted(out)

def apply(s: State, t: tuple) -> State:
    fam=t[0]; c=set(s.components); e=set(s.edges); r=list(s.resources)
    if fam == "ADD_COMPONENT": c.add(t[1])
    elif fam == "REMOVE_COMPONENT":
        c.remove(t[1]); e={x for x in e if t[1] not in x}
    elif fam == "ADD_EDGE": e.add((t[1],t[2]))
    elif fam == "REMOVE_EDGE": e.remove((t[1],t[2]))
    elif fam == "REWIRE_EDGE": e.remove((t[1],t[2])); e.add((t[1],t[3]))
    elif fam == "MODIFY_RESOURCE": r[t[1]] += t[2]
    else: raise ValueError("unknown family")
    return canonical_state(c,e,r,s.objective)

def tacc(s: State) -> list[tuple]: return [(t, apply(s,t)) for t in enumerate_transformations(s)]

def _jaccard(a: set, b: set) -> float:
    u=a|b; return float(len(a&b)/len(u)) if u else 1.0

def r2(s: State) -> tuple[float,...]:
    pairs=tacc(s)
    if not pairs: return (0.0,)*24
    fam_counts={f:0 for f in FAMILIES}; rows=[]; C=set(s.components); E=set(s.edges)
    for t,s2 in pairs:
        fam=t[0]; fam_counts[fam]+=1
        src,dst=set(),set()
        if fam == "ADD_COMPONENT": dst={t[1]}
        elif fam == "REMOVE_COMPONENT": src={t[1]}
        elif fam in ("ADD_EDGE","REMOVE_EDGE"): src={t[1]}; dst={t[2]}
        elif fam == "REWIRE_EDGE": src={t[1]}; dst={t[3]}
        ed=len(s2.edges)-len(s.edges); cd=len(s2.components)-len(s.components); rd=sum(abs(a-b) for a,b in zip(s.resources,s2.resources))
        rows.append((fam,len(src),len(dst),ed,cd,rd,_jaccard(C,set(s2.components)),_jaccard(E,set(s2.edges))))
    n=len(rows); p=[fam_counts[f]/n for f in FAMILIES]; entropy=-sum(x*math.log(x) for x in p if x>0); hhi=sum(x*x for x in p)
    mean=lambda xs: sum(xs)/n; ed=[x[3] for x in rows]; cd=[x[4] for x in rows]
    sd=lambda xs: math.sqrt(sum((x-mean(xs))**2 for x in xs)/n)
    return (float(n), float(sum(v>0 for v in fam_counts.values())), float(entropy), float(hhi),
            float(mean(x[1] for x in rows)), float(mean(x[2] for x in rows)), float(mean(x[5] for x in rows)),
            float(mean(cd)), float(mean(ed)), float(mean(max(x,0) for x in ed)), float(mean(-min(x,0) for x in ed)),
            float(fam_counts["ADD_COMPONENT"]/n), float(fam_counts["REMOVE_COMPONENT"]/n), float(fam_counts["MODIFY_RESOURCE"]/n),
            float(sum(x[0] in ("ADD_EDGE","REMOVE_EDGE","REWIRE_EDGE") for x in rows)/n), float(sum(x[0] in ("ADD_COMPONENT","REMOVE_COMPONENT") for x in rows)/n),
            float(sum(x[4]==0 for x in rows)/n), float(sum(x[3]==0 for x in rows)/n), float(sum(x[0]=="MODIFY_RESOURCE" for x in rows)/n),
            float(sum(x[0] in ("ADD_EDGE","REMOVE_EDGE","REWIRE_EDGE") for x in rows)/n), float(mean(x[6] for x in rows)), float(mean(x[7] for x in rows)), float(sd(ed)), float(sd(cd)))

def b_vector(s: State) -> tuple[float,...]:
    return (float(len(s.components)), float(s.resources[0]), float(s.resources[1]), float(s.resources[2])) + tuple(1.0 if s.objective==o else 0.0 for o in OBJECTIVES)

def low_order_r1(s: State) -> tuple:
    pairs=tacc(s); fam={f:0 for f in FAMILIES}; inc={x:0 for x in COMPONENTS}
    for t,_ in pairs:
        fam[t[0]]+=1
        if t[0] in ("ADD_EDGE","REMOVE_EDGE"): inc[t[1]]+=1; inc[t[2]]+=1
        elif t[0]=="REWIRE_EDGE": inc[t[1]]+=1; inc[t[2]]+=1; inc[t[3]]+=1
    return (len(pairs), sum(v>0 for v in fam.values()), tuple(fam[f] for f in FAMILIES), tuple(inc[x] for x in COMPONENTS))
