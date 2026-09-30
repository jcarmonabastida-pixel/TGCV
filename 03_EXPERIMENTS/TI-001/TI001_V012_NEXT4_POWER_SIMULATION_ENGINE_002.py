"""NEXT4 design-stage power engine 002 consuming canonical DGP 002."""
from __future__ import annotations
from dataclasses import dataclass
import hashlib,json,random
from itertools import permutations
from math import exp
from pathlib import Path
ACTIONS=(0,1,2,3); PROFILES=ACTIONS; DOMAINS=(0,1,2); OPS=(0,1); PRESENTATIONS=(0,1,2,3)
CONDITIONS=("STATIC_CONTROL","FUTURE_REASSIGNED","SURFACE_CONTROL","UNINFORMATIVE_NULL")
PERMUTATIONS=tuple(permutations(ACTIONS)); DGP_PATH=Path(__file__).with_name("TI001_V012_NEXT4_DGP_SPECIFICATION_002.json")
def load_dgp(): return json.loads(DGP_PATH.read_text(encoding="utf-8"))
@dataclass(frozen=True)
class Scenario:
 effect_label:str; effect_size:float; n_choice_sets:int; replicate:int; master_seed:int
def seed_for(s,i): return int.from_bytes(hashlib.sha256(f"{s.master_seed}|{s.effect_label}|{s.n_choice_sets}|{s.replicate}|{i}".encode()).digest()[:8],"big")
def softmax(xs):
 m=max(xs); ex=[exp(x-m) for x in xs]; z=sum(ex); return [x/z for x in ex]
def mapping_for(condition,permutation): return (0,1,2,3) if condition in ("SURFACE_CONTROL","UNINFORMATIVE_NULL") else permutation
def build_choice_set(s,i,dgp):
 rng=random.Random(seed_for(s,i)); domain=i%3; op=(i//3)%2; presentation=(i//6)%4
 condition=CONDITIONS[(i//24)%4]; permutation=PERMUTATIONS[i%24]; mapping=mapping_for(condition,permutation)
 profile=PROFILES[i%4]; future=mapping[profile]; n=dgp["nuisance"]; logits=[]
 for action in ACTIONS:
  baseline=n["baseline_action"][action]+n["domain"][domain]+n["operationalisation"][op]+n["presentation"][presentation]+0.04*((action+profile)%4)
  signal=s.effect_size*int(condition=="FUTURE_REASSIGNED" and action==future); logits.append(baseline+signal)
 probs=softmax(logits); u=rng.random(); c=0; chosen=ACTIONS[-1]
 for action,p in zip(ACTIONS,probs):
  c+=p
  if u<=c: chosen=action; break
 return {"choice_set_id":i,"domain":domain,"operationalisation":op,"presentation":presentation,"condition":condition,"permutation":permutation,"mapping":mapping,"profile":profile,"future":future,"chosen_action":chosen,"actions":list(ACTIONS),"probabilities":probs,"effect_label":s.effect_label,"effect_size":s.effect_size}
def choice_set_to_action_rows(cs):
 return [dict(choice_set_id=cs["choice_set_id"],action=a,chosen=int(a==cs["chosen_action"]),profile=cs["profile"],domain=cs["domain"],operationalisation=cs["operationalisation"],presentation=cs["presentation"],condition=cs["condition"],permutation=cs["permutation"],mapping=cs["mapping"],future=cs["future"],mapping_aligned=int(a==cs["future"])) for a in ACTIONS]
def generate_dataset(s):
 dgp=load_dgp(); sets=[build_choice_set(s,i,dgp) for i in range(s.n_choice_sets)]
 return sets,[r for cs in sets for r in choice_set_to_action_rows(cs)]
def digest(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()
if __name__=="__main__":
 dgp=load_dgp(); s=Scenario("NULL",0.0,1728,0,410927); sets,rows=generate_dataset(s)
 print(json.dumps({"status":"CHOICE_SET_ENGINE_READY","dgp_artifact":dgp["artifact"],"choice_sets":len(sets),"action_rows":len(rows),"dataset_sha256":digest(rows),"provider_api_calls":False,"scientific_executor_calls":False},sort_keys=True))
