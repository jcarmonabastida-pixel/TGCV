"""NEXT4 power simulation engine 003.

Consumes DGP Specification 001. Design-stage only: synthetic responses,
no provider calls and no scientific execution.
"""

from __future__ import annotations
from dataclasses import dataclass
import hashlib, json, random
from itertools import permutations
from math import exp
from typing import Any

ACTIONS=(0,1,2,3)
PROFILES=ACTIONS
DOMAINS=(0,1,2)
OPS=(0,1)
PRESENTATIONS=(0,1,2,3)
CONDITIONS=("STATIC_CONTROL","FUTURE_REASSIGNED","SURFACE_CONTROL","UNINFORMATIVE_NULL")
PERMUTATIONS=tuple(permutations(ACTIONS))
EFFECTS={"NULL":0.0,"VERY_SMALL":0.10,"SMALL":0.25,"MODERATE":0.50,"OPTIMISTIC":0.80}

@dataclass(frozen=True)
class Scenario:
    effect_label:str
    n_choice_sets:int
    replicate:int
    master_seed:int

    @property
    def beta(self): return EFFECTS[self.effect_label]

def seed_for(s:Scenario,i:int)->int:
    raw=f"{s.master_seed}|{s.effect_label}|{s.n_choice_sets}|{s.replicate}|{i}".encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:8],"big")

def softmax(xs):
    m=max(xs); ex=[exp(x-m) for x in xs]; z=sum(ex)
    return [x/z for x in ex]

def latent_mapping(condition, permutation):
    if condition=="STATIC_CONTROL": return (0,1,2,3)
    if condition=="FUTURE_REASSIGNED": return permutation
    if condition=="SURFACE_CONTROL": return (0,1,2,3)
    if condition=="UNINFORMATIVE_NULL": return None
    raise ValueError(condition)

def build_choice_set(s:Scenario,i:int)->dict[str,Any]:
    rng=random.Random(seed_for(s,i))
    domain=i%3; op=(i//3)%2; presentation=(i//6)%4
    condition=CONDITIONS[(i//24)%4]
    permutation=PERMUTATIONS[i%24]
    mapping=latent_mapping(condition,permutation)
    profile=PROFILES[i%4]
    future=None if mapping is None else mapping[profile]
    logits=[]
    for action in ACTIONS:
        baseline=.05*action + .04*((action+profile)%4) + .03*domain + .02*op
        aligned=(mapping is not None and action==future)
        signal=s.beta if aligned else 0.0
        logits.append(baseline+signal)
    probs=softmax(logits)
    u=rng.random(); cumulative=0.0; chosen=ACTIONS[-1]
    for action,p in zip(ACTIONS,probs):
        cumulative += p
        if u <= cumulative:
            chosen=action; break
    return {
        "choice_set_id":i,"domain":domain,"operationalisation":op,
        "presentation":presentation,"condition":condition,
        "permutation":permutation,"latent_mapping":mapping,
        "profile":profile,"future":future,
        "mapping_signal":0 if mapping is None else 1,
        "chosen_action":chosen,"probabilities":probs,
        "effect_label":s.effect_label,"effect_size":s.beta
    }

def action_rows(cs):
    return [{
        "choice_set_id":cs["choice_set_id"],"action":a,
        "chosen":int(a==cs["chosen_action"]),
        "profile":cs["profile"],"domain":cs["domain"],
        "operationalisation":cs["operationalisation"],
        "presentation":cs["presentation"],"condition":cs["condition"],
        "permutation":cs["permutation"],"latent_mapping":cs["latent_mapping"],
        "future":cs["future"],
        "mapping_aligned":int(cs["future"] is not None and a==cs["future"])
    } for a in ACTIONS]

def generate(s:Scenario):
    sets=[build_choice_set(s,i) for i in range(s.n_choice_sets)]
    rows=[r for cs in sets for r in action_rows(cs)]
    return sets,rows

def digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def factorial_audit(sets):
    counts={(c,d,o,p):0 for c in CONDITIONS for d in DOMAINS for o in OPS for p in PRESENTATIONS}
    for x in sets:
        counts[(x["condition"],x["domain"],x["operationalisation"],x["presentation"])] += 1
    return {
        "all_cells_present":all(v>0 for v in counts.values()),
        "min_cell":min(counts.values()),
        "max_cell":max(counts.values()),
        "unique_permutations":len({x["permutation"] for x in sets}),
        "condition_counts":{c:sum(x["condition"]==c for x in sets) for c in CONDITIONS}
    }

if __name__=="__main__":
    s=Scenario("NULL",1728,0,410927)
    sets,rows=generate(s)
    print(json.dumps({
        "status":"DGP_ENGINE_003_READY",
        "choice_sets":len(sets),"action_rows":len(rows),
        "factorial_audit":factorial_audit(sets),
        "dataset_sha256":digest(rows),
        "provider_api_calls":False,"scientific_executor_calls":False
    },sort_keys=True))
