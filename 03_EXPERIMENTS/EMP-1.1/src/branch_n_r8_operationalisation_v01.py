"""N-R8.3 operationalisation primitives.

No learner, outcome, or N-R7 result dependency.  This module only constructs
G2 states, matched pairs, and the independent R2 representation from initial
Branch-N states and the frozen transformation semantics.
"""
from __future__ import annotations

import hashlib
import json
import math
import random
from dataclasses import dataclass
from typing import Iterable, Sequence

FAMILIES = (
    "ADD_COMPONENT", "REMOVE_COMPONENT", "ADD_EDGE", "REMOVE_EDGE",
    "REWIRE_EDGE", "MODIFY_RESOURCE",
)
OBJECTIVES = tuple(f"O{i:02d}" for i in range(1, 13))
COMPONENTS = ("A1", "A2", "B1", "B2", "C1", "C2")

@dataclass(frozen=True)
class State:
    components: tuple[str, ...]
    edges: tuple[tuple[str, str], ...]
    resources: tuple[int, int, int]
    objective: str

    def canonical(self) -> dict:
        return {
            "components": list(self.components),
            "edges": [list(e) for e in self.edges],
            "objective": self.objective,
            "resources": list(self.resources),
        }

    def sha256(self) -> str:
        b = json.dumps(self.canonical(), sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
        return hashlib.sha256(b).hexdigest()

def canonical_state(components: Iterable[str], edges: Iterable[tuple[str,str]], resources: Sequence[int], objective: str) -> State:
    c = tuple(sorted(components))
    e = tuple(sorted(set(edges)))
    if len(e) != len(tuple(edges)):
        # caller should normally pass materialised edges; retained as a safety check
        raise ValueError("duplicate edge")
    if any(a == b for a,b in e): raise ValueError("self-loop")
    if any(a not in c or b not in c for a,b in e): raise ValueError("edge endpoint absent")
    if objective not in OBJECTIVES: raise ValueError("invalid objective")
    if len(resources) != 3 or any(int(x) not in range(4) for x in resources): raise ValueError("invalid resources")
    return State(c, e, tuple(map(int, resources)), objective)

def generate_g1(rng: random.Random) -> State:
    n = rng.choice((3,4,5))
    c = rng.sample(list(COMPONENTS), n)
    possible = [(a,b) for a in c for b in c if a != b]
    k = rng.randint(0, len(possible))
    e = rng.sample(possible, k)
    r = tuple(rng.randrange(4) for _ in range(3))
    o = rng.choice(OBJECTIVES)
    return canonical_state(c,e,r,o)

def _round_half_up(x: float) -> int:
    return math.floor(x + 0.5)

def generate_g2(rng: random.Random) -> State:
    n = rng.choices((3,4,5), weights=(0.10,0.30,0.60), k=1)[0]
    c = rng.sample(list(COMPONENTS), n)
    possible = [(a,b) for a in c for b in c if a != b]
    d = rng.choices((0.20,0.50,0.80), weights=(0.50,0.30,0.20), k=1)[0]
    k = max(0, min(len(possible), _round_half_up(d * len(possible))))
    e = rng.sample(possible, k)
    r = tuple(rng.choices((0,1,2,3), weights=(0.10,0.20,0.30,0.40), k=1)[0] for _ in range(3))
    o = rng.choices(OBJECTIVES, weights=(0.10,)*6 + (1/15,)*6, k=1)[0]
    return canonical_state(c,e,r,o)

def enumerate_transformations(s: State) -> list[tuple]:
    c = set(s.components); edges = set(s.edges)
    out = []
    for x in COMPONENTS:
        if x not in c: out.append(("ADD_COMPONENT", x))
    for x in sorted(c): out.append(("REMOVE_COMPONENT", x))
    for a in sorted(c):
        for b in sorted(c):
            if a != b and (a,b) not in edges: out.append(("ADD_EDGE", a,b))
    for e in sorted(edges): out.append(("REMOVE_EDGE", e[0],e[1]))
    for e in sorted(edges):
        for a in sorted(c):
            for b in sorted(c):
                if a != b and (a,b) not in edges and (a,b) != e:
                    out.append(("REWIRE_EDGE", e[0],e[1],a,b))
    for i in range(3):
        for v in range(4):
            if v != s.resources[i]: out.append(("MODIFY_RESOURCE", i, v))
    return sorted(out)

def apply(s: State, t: tuple) -> State:
    fam = t[0]; c=set(s.components); e=set(s.edges); r=list(s.resources)
    if fam == "ADD_COMPONENT": c.add(t[1])
    elif fam == "REMOVE_COMPONENT":
        c.remove(t[1]); e={x for x in e if t[1] not in x}
    elif fam == "ADD_EDGE": e.add((t[1],t[2]))
    elif fam == "REMOVE_EDGE": e.remove((t[1],t[2]))
    elif fam == "REWIRE_EDGE": e.remove((t[1],t[2])); e.add((t[3],t[4]))
    elif fam == "MODIFY_RESOURCE": r[t[1]]=t[2]
    else: raise ValueError("unknown family")
    return canonical_state(c,e,r,s.objective)

def tacc(s: State) -> list[tuple]:
    return [(t, apply(s,t)) for t in enumerate_transformations(s)]

def r2(s: State) -> tuple[float,...]:
    pairs=tacc(s)
    if not pairs: return (0.0,)*24
    fam_counts={f:0 for f in FAMILIES}
    vals=[]
    for t,s2 in pairs:
        fam_counts[t[0]] += 1
        ed=(len(s2.edges)-len(s.edges)); cd=(len(s2.components)-len(s.components)); rd=sum(abs(a-b) for a,b in zip(s.resources,s2.resources))
        vals.append((ed,cd,rd,t[0],s2))
    n=len(vals); p=[fam_counts[f]/n for f in FAMILIES]
    entropy=-sum(x*math.log(x) for x in p if x>0); hhi=sum(x*x for x in p)
    mean=lambda xs: sum(xs)/n
    comp_j=[]; edge_j=[]
    C=set(s.components); E=set(s.edges)
    for *_,s2 in vals:
        C2=set(s2.components); E2=set(s2.edges)
        comp_j.append(len(C&C2)/len(C|C2) if C|C2 else 1.0)
        edge_j.append(len(E&E2)/len(E|E2) if E|E2 else 1.0)
    edge_d=[x[0] for x in vals]; comp_d=[x[1] for x in vals]
    sd=lambda xs: math.sqrt(sum((x-mean(xs))**2 for x in xs)/n)
    fam={x[3] for x in vals}
    return (float(n), float(len(fam)), float(entropy), float(hhi),
            0.0, 0.0, float(mean(x[2] for x in vals)), float(mean(comp_d)),
            float(mean(edge_d)), float(mean([max(x,0) for x in edge_d])),
            float(mean([-min(x,0) for x in edge_d])), float(sum(x[3]=="ADD_COMPONENT" for x in vals)/n),
            float(sum(x[3]=="REMOVE_COMPONENT" for x in vals)/n),
            float(sum(x[3]=="MODIFY_RESOURCE" for x in vals)/n),
            float(sum(x[3] in ("ADD_EDGE","REMOVE_EDGE","REWIRE_EDGE") for x in vals)/n),
            float(sum(x[3] in ("ADD_COMPONENT","REMOVE_COMPONENT") for x in vals)/n),
            float(sum(x[1]==0 for x in vals)/n), float(sum(x[0]==0 for x in vals)/n),
            float(sum(x[3]=="MODIFY_RESOURCE" for x in vals)/n), float(sum(x[3] in ("ADD_EDGE","REMOVE_EDGE","REWIRE_EDGE") for x in vals)/n),
            float(mean(comp_j)), float(mean(edge_j)), float(sd(edge_d)), float(sd(comp_d)))

def b_vector(s: State) -> tuple[float,...]:
    obj=tuple(1.0 if s.objective==o else 0.0 for o in OBJECTIVES)
    return (float(len(s.components)), float(s.resources[0]), float(s.resources[1]), float(s.resources[2])) + obj

def low_order_r1(s: State) -> tuple:
    pairs=tacc(s); fam={f:0 for f in FAMILIES}
    inc={x:0 for x in COMPONENTS}
    for t,_ in pairs:
        fam[t[0]] += 1
        if t[0] in ("ADD_EDGE","REMOVE_EDGE","REWIRE_EDGE"):
            for x in t[1:]:
                if x in COMPONENTS: inc[x]+=1
    return (len(pairs), sum(v>0 for v in fam.values()), tuple(fam[f] for f in FAMILIES), tuple(inc[x] for x in COMPONENTS))
