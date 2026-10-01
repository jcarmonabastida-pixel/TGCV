import json, hashlib

def canonical_action(a):
    params=[tuple(p) for p in a["parameters"]]
    def lit(x): return tuple(x)
    return {
        "name": a["name"],
        "parameters": params,
        "preconditions": sorted({lit(x) for x in a["preconditions"]}),
        "add_effects": sorted({lit(x) for x in a["add_effects"]}),
        "delete_effects": sorted({lit(x) for x in a["delete_effects"]})
    }

def canonicalize(src):
    actions=[canonical_action(a) for a in src["actions"]]
    return {
        "types": sorted(src["types"]),
        "objects": {k: sorted(v) for k,v in sorted(src["objects"].items())},
        "actions": sorted(actions,key=lambda a:(a["name"],a["parameters"]))
    }

def grounded_universe(c):
    return [tuple([a["name"]]+list(p)) for a in c["actions"] for p in [tuple(x[0] for x in a["parameters"])]]

def build_relations(c):
    U=[(a["name"], tuple(a["parameters"])) for a in c["actions"]]
    r1=[]; r2=[]; r3=[]
    for a in c["actions"]:
        tid=(a["name"],tuple(a["parameters"]))
        for x in a["preconditions"]: r1.append((tid,tuple(x)))
        for x in a["add_effects"]: r2.append((tid,"ADD",tuple(x)))
        for x in a["delete_effects"]: r2.append((tid,"DELETE",tuple(x)))
    for a in c["actions"]:
        ai=(a["name"],tuple(a["parameters"]))
        for b in c["actions"]:
            bj=(b["name"],tuple(b["parameters"]))
            if ai==bj: continue
            if any(e in b["preconditions"] for e in a["add_effects"]+a["delete_effects"]):
                r3.append((ai,bj))
    return {"R1":sorted(r1), "R2":sorted(r2), "R3":sorted(set(r3))}

def omega(src):
    c=canonicalize(src)
    return {"U":[(a["name"],tuple(a["parameters"])) for a in c["actions"]],"relations":build_relations(c)}

def sha(obj):
    b=json.dumps(obj,sort_keys=True,separators=(",",":")).encode()
    return hashlib.sha256(b).hexdigest()
