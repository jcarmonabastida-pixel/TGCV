#!/usr/bin/env python3
"""Independent NEXT3 reconstruction harness.

This artifact intentionally reimplements the transition logic independently
from the scientific executor interface and performs no scientific execution.
"""
import json
import hashlib

ACTIONS = ["A","B","C","D"]
SLOTS = ["slot_1","slot_2","slot_3","slot_4"]
PROFILE_VALUES = {
 "slot_1":(1,1,1,1),"slot_2":(2,1,1,2),
 "slot_3":(3,2,2,2),"slot_4":(4,3,3,3)
}
def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"))
def h(x): return hashlib.sha256(canon(x).encode()).hexdigest()
def apply(s,a,slot):
 x=json.loads(canon(s)); p=PROFILE_VALUES[slot]; base=len(x.get("active",[]))+1
 for i in range(p[0]): x.setdefault("active",[]).append(base+i)
 x["active"]=sorted(set(x["active"]))
 x.setdefault("relations",[])
 for _ in range(p[3]):
  if len(x["active"])>=2: x["relations"].append([x["active"][-1],x["active"][-2],a])
 x["relations"]=sorted(x["relations"])
 x.setdefault("constraints",[])
 for i in range(p[1]): x["constraints"].append([a,slot,i])
 x["constraints"]=sorted(x["constraints"])
 return x
def valid(s):
 A=set(s["active"]); return all(r[0] in A and r[1] in A for r in s["relations"])
def tr(s,n):
 return {"added_active":sorted(set(n["active"])-set(s["active"])),
         "added_relations":[r for r in n["relations"] if r not in s["relations"]],
         "added_constraints":[c for c in n["constraints"] if c not in s["constraints"]]}
def reconstruct(s,a,z):
 n=apply(s,a,z[a])
 if not valid(n): raise ValueError("invalid")
 t=tr(s,n); return h(n),h(t)
