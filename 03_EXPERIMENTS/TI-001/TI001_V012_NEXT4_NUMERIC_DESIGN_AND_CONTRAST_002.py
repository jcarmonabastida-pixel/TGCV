"""NEXT4 numeric design matrix and primary contrast 002."""
from __future__ import annotations
import hashlib,json
from itertools import permutations
import numpy as np

ACTIONS=(0,1,2,3); PROFILES=ACTIONS
PERMUTATIONS=tuple(permutations(ACTIONS))
CONDITIONS=("STATIC_CONTROL","FUTURE_REASSIGNED","SURFACE_CONTROL","UNINFORMATIVE_NULL")
DOMAINS=(0,1,2); OPS=(0,1); PRESENTATIONS=(0,1,2,3)

def build_matrix(rows):
    cols=["intercept"]+[f"action_{a}" for a in ACTIONS[1:]]+[f"profile_{p}" for p in PROFILES[1:]]
    cols += [f"action_profile_{a}_{p}" for a in ACTIONS[1:] for p in PROFILES[1:]]
    cols += ["mapping_signal"]+[f"domain_{d}" for d in DOMAINS[1:]]
    cols += [f"operationalisation_{o}" for o in OPS[1:]]
    cols += [f"presentation_{p}" for p in PRESENTATIONS[1:]]
    cols += [f"condition_{c}" for c in CONDITIONS[1:]]
    X=np.zeros((len(rows),len(cols)),dtype=float)
    for i,r in enumerate(rows):
        X[i,0]=1; j=1
        for a in ACTIONS[1:]: X[i,j]=int(r["action"]==a); j+=1
        for p in PROFILES[1:]: X[i,j]=int(r["profile"]==p); j+=1
        for a in ACTIONS[1:]:
            for p in PROFILES[1:]:
                X[i,j]=int(r["action"]==a and r["profile"]==p); j+=1
        X[i,j]=int(r["latent_mapping"] is not None); j+=1
        for d in DOMAINS[1:]: X[i,j]=int(r["domain"]==d); j+=1
        for o in OPS[1:]: X[i,j]=int(r["operationalisation"]==o); j+=1
        for p in PRESENTATIONS[1:]: X[i,j]=int(r["presentation"]==p); j+=1
        for c in CONDITIONS[1:]: X[i,j]=int(r["condition"]==c); j+=1
    return X,cols

def primary_contrast(rows,cols):
    c=np.zeros(len(cols))
    pairs=set()
    for r in rows:
        if r["condition"]=="FUTURE_REASSIGNED" and r["latent_mapping"] is not None:
            if r["action"] in ACTIONS[1:] and r["action"]==r["latent_mapping"][r["profile"]]:
                pairs.add((r["action"],r["profile"]))
    if not pairs: raise ValueError("No reassigned aligned pairs")
    identity={(p,p) for p in PROFILES[1:]}
    for i,name in enumerate(cols):
        if name.startswith("action_profile_"):
            _,a,p=name.split("_"); pair=(int(a),int(p))
            if pair in pairs: c[i]+=1/len(pairs)
            if pair in identity: c[i]-=1/len(identity)
    return c

def audit(rows):
    X,cols=build_matrix(rows); c=primary_contrast(rows,cols)
    rank=int(np.linalg.matrix_rank(X))
    U,s,Vt=np.linalg.svd(X,full_matrices=False)
    rowspace=Vt[:rank,:]
    residual=np.linalg.norm(c-rowspace.T@(rowspace@c))
    return {"rows":len(rows),"columns":len(cols),"rank":rank,
            "full_column_rank":rank==len(cols),
            "contrast_norm":float(np.linalg.norm(c)),
            "contrast_estimability_residual":float(residual),
            "contrast_estimable":bool(residual<1e-10),
            "matrix_sha256":hashlib.sha256(X.tobytes()).hexdigest(),
            "contrast_sha256":hashlib.sha256(c.tobytes()).hexdigest()}

if __name__=="__main__":
    print(json.dumps({"status":"NUMERIC_DESIGN_IMPLEMENTATION_READY"},sort_keys=True))
