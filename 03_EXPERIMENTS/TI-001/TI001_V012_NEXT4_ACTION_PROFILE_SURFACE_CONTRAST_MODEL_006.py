"""NEXT4 action×profile surface and permutation contrast model 006.

No deterministic mapping columns are added to X. The frozen permutation only
defines the linear contrast over the action×profile coefficient surface.
"""
from __future__ import annotations
import hashlib,json
from itertools import permutations
import numpy as np

ACTIONS=(0,1,2,3); PROFILES=ACTIONS
CONDITIONS=("STATIC_CONTROL","FUTURE_REASSIGNED","SURFACE_CONTROL","UNINFORMATIVE_NULL")
DOMAINS=(0,1,2); OPS=(0,1); PRESENTATIONS=(0,1,2,3)

def build_matrix(rows):
    cols=["intercept"]
    cols += [f"action_{a}" for a in ACTIONS[1:]]
    cols += [f"profile_{p}" for p in PROFILES[1:]]
    cols += [f"action_profile_{a}_{p}" for a in ACTIONS[1:] for p in PROFILES[1:]]
    cols += [f"condition_{c}" for c in CONDITIONS[1:]]
    cols += [f"condition_action_profile_{c}_{a}_{p}"
             for c in CONDITIONS[1:] for a in ACTIONS[1:] for p in PROFILES[1:]]
    cols += [f"domain_{d}" for d in DOMAINS[1:]]
    cols += [f"operationalisation_{o}" for o in OPS[1:]]
    cols += [f"presentation_{p}" for p in PRESENTATIONS[1:]]
    X=np.zeros((len(rows),len(cols)))
    for i,r in enumerate(rows):
        X[i,0]=1; j=1
        for a in ACTIONS[1:]: X[i,j]=int(r["action"]==a); j+=1
        for p in PROFILES[1:]: X[i,j]=int(r["profile"]==p); j+=1
        for a in ACTIONS[1:]:
            for p in PROFILES[1:]:
                X[i,j]=int(r["action"]==a and r["profile"]==p); j+=1
        for c in CONDITIONS[1:]:
            X[i,j]=int(r["condition"]==c); j+=1
            for a in ACTIONS[1:]:
                for p in PROFILES[1:]:
                    X[i,j]=int(r["condition"]==c and r["action"]==a and r["profile"]==p); j+=1
        for d in DOMAINS[1:]: X[i,j]=int(r["domain"]==d); j+=1
        for o in OPS[1:]: X[i,j]=int(r["operationalisation"]==o); j+=1
        for p in PRESENTATIONS[1:]: X[i,j]=int(r["presentation"]==p); j+=1
    return X,cols

def coefficient_index(cols,condition,a,p):
    if condition=="STATIC_CONTROL":
        name=f"action_profile_{a}_{p}"
    else:
        name=f"condition_action_profile_{condition}_{a}_{p}"
    return cols.index(name)

def permutation_contrast(cols, permutation):
    """Average action×profile surface along reassigned mapping minus identity."""
    c=np.zeros(len(cols))
    nonref_profiles=PROFILES[1:]
    w=1/len(nonref_profiles)
    for p in nonref_profiles:
        a_reassigned=permutation[p]
        c[coefficient_index(cols,"FUTURE_REASSIGNED",a_reassigned,p)] += w
        c[coefficient_index(cols,"STATIC_CONTROL",p,p)] -= w
    return c

def audit(rows, permutation):
    X,cols=build_matrix(rows); c=permutation_contrast(cols,permutation)
    rank=int(np.linalg.matrix_rank(X))
    U,s,Vt=np.linalg.svd(X,full_matrices=False)
    rowspace=Vt[:rank,:]
    residual=float(np.linalg.norm(c-rowspace.T@(rowspace@c)))
    return {"rows":len(rows),"columns":len(cols),"rank":rank,
            "full_column_rank":rank==len(cols),
            "contrast_norm":float(np.linalg.norm(c)),
            "contrast_estimability_residual":residual,
            "contrast_estimable":residual<1e-10,
            "matrix_sha256":hashlib.sha256(X.tobytes()).hexdigest(),
            "contrast_sha256":hashlib.sha256(c.tobytes()).hexdigest(),
            "permutation":permutation}

if __name__=="__main__":
    print(json.dumps({"status":"ACTION_PROFILE_SURFACE_CONTRAST_MODEL_006_READY"},sort_keys=True))
