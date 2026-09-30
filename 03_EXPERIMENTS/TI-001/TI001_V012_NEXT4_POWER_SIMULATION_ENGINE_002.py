"""NEXT4 design-stage power engine 002.

Constructs explicit four-action choice sets. Still no provider calls and no
scientific execution. The statistical fit/contrast remains a separate gate.
"""

from __future__ import annotations
from dataclasses import dataclass
import hashlib, json, random
from itertools import permutations
from math import exp
from typing import Any

ACTIONS=(0,1,2,3)
PROFILES=(0,1,2,3)
DOMAINS=(0,1,2)
OPS=(0,1)
PRESENTATIONS=(0,1,2,3)
CONDITIONS=("STATIC_CONTROL","FUTURE_REASSIGNED","SURFACE_CONTROL","UNINFORMATIVE_NULL")
PERMUTATIONS=tuple(permutations(ACTIONS))

@dataclass(frozen=True)
class Scenario:
    effect_label:str
    effect_size:float
    n_choice_sets:int
    replicate:int
    master_seed:int

def seed_for(s:Scenario, choice_set_id:int)->int:
    raw=f"{s.master_seed}|{s.effect_label}|{s.n_choice_sets}|{s.replicate}|{choice_set_id}".encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:8],"big")

def softmax(xs):
    m=max(xs); ex=[exp(x-m) for x in xs]; z=sum(ex)
    return [x/z for x in ex]

def mapping_for(condition:str, permutation:tuple[int,...])->tuple[int,...]:
    if condition=="UNINFORMATIVE_NULL":
        return (0,1,2,3)
    if condition=="SURFACE_CONTROL":
        return (0,1,2,3)
    return permutation

def mapping_signal(mapping, profile, future):
    return int(mapping[profile]==future)

def build_choice_set(s:Scenario, i:int)->dict[str,Any]:
    rng=random.Random(seed_for(s,i))
    domain=i%3
    op=(i//3)%2
    presentation=(i//6)%4
    condition=CONDITIONS[(i//24)%4]
    permutation=PERMUTATIONS[i%24]
    mapping=mapping_for(condition,permutation)
    profile=PROFILES[i%4]
    future=mapping[profile]
    logits=[]
    for action in ACTIONS:
        baseline=.05*action+.03*domain+.02*op
        profile_term=.04*((action+profile)%4)
        aligned=int(action==future)
        signal=s.effect_size*aligned
        logits.append(baseline+profile_term+signal)
    probs=softmax(logits)
    u=rng.random(); c=0
    chosen=ACTIONS[-1]
    for action,p in zip(ACTIONS,probs):
        c+=p
        if u<=c:
            chosen=action; break
    return {
        "choice_set_id":i,"domain":domain,"operationalisation":op,
        "presentation":presentation,"condition":condition,
        "permutation":permutation,"mapping":mapping,"profile":profile,
        "future":future,"mapping_signal":mapping_signal(mapping,profile,future),
        "chosen_action":chosen,
        "actions":list(ACTIONS),
        "probabilities":probs,
        "effect_label":s.effect_label,"effect_size":s.effect_size
    }

def choice_set_to_action_rows(cs):
    rows=[]
    for action in ACTIONS:
        rows.append({
            "choice_set_id":cs["choice_set_id"],
            "action":action,
            "chosen":int(action==cs["chosen_action"]),
            "profile":cs["profile"],
            "domain":cs["domain"],
            "operationalisation":cs["operationalisation"],
            "presentation":cs["presentation"],
            "condition":cs["condition"],
            "permutation":cs["permutation"],
            "mapping":cs["mapping"],
            "future":cs["future"],
            "mapping_aligned":int(action==cs["future"]),
            "mapping_signal":cs["mapping_signal"]
        })
    return rows

def generate_dataset(s):
    sets=[build_choice_set(s,i) for i in range(s.n_choice_sets)]
    rows=[r for cs in sets for r in choice_set_to_action_rows(cs)]
    return sets,rows

def digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

if __name__=="__main__":
    s=Scenario("NULL",0.0,1728,0,410927)
    sets,rows=generate_dataset(s)
    print(json.dumps({
        "status":"CHOICE_SET_ENGINE_READY",
        "choice_sets":len(sets),"action_rows":len(rows),
        "dataset_sha256":digest(rows),
        "provider_api_calls":False,"scientific_executor_calls":False
    },sort_keys=True))
