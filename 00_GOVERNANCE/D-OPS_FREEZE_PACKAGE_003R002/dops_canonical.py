import json

def canon(x):
    if isinstance(x, dict):
        return {k: canon(x[k]) for k in sorted(x)}
    if isinstance(x, list):
        return sorted((canon(v) for v in x), key=lambda v: json.dumps(v, sort_keys=True, separators=(",",":")))
    return x

def canon_directed_edges(edges):
    # R3 edges are ordered pairs: endpoint order is semantic and must be preserved.
    return sorted((list(edge) for edge in edges),
                  key=lambda e: json.dumps(e, separators=(",",":")))

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def canonical_omega(fixture, r3):
    U=[t["id"] for t in fixture["transformations"]]
    R1=[]
    R2=[]
    for t in fixture["transformations"]:
        tid=t["id"]
        for p in t["preconditions"]: R1.append([tid,p])
        for a in t["add_effects"]: R2.append([tid,"ADD",a])
        for d in t["delete_effects"]: R2.append([tid,"DELETE",d])
    R3=r3["edges"]
    return {"U":sorted(U),"equivalence":[],"R1":canon(R1),"R2":canon(R2),"R3":canon_directed_edges(R3)}
