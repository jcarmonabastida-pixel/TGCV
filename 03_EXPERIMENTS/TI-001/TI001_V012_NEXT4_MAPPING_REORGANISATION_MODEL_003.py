"""NEXT4 mapping-reorganisation design 003.

Uses a single response-independent mapping-alignment regressor and its
interaction with action identity. Condition is encoded without a collinear
mapping main effect. The scientific estimand is the differential
action×profile reorganisation aligned with the imposed permutation.
"""
from __future__ import annotations
import hashlib,json
import numpy as np

ACTIONS=(0,1,2,3); PROFILES=ACTIONS
CONDITIONS=("STATIC_CONTROL","FUTURE_REASSIGNED","SURFACE_CONTROL","UNINFORMATIVE_NULL")
DOMAINS=(0,1,2); OPS=(0,1); PRESENTATIONS=(0,1,2,3)

def build_matrix(rows):
    cols=["intercept"]
    cols += [f"action_{a}" for a in ACTIONS[1:]]
    cols += [f"profile_{p}" for p in PROFILES[1:]]
    cols += [f"action_profile_{a}_{p}" for a in ACTIONS[1:] for p in PROFILES[1:]]
    # Scientific term: whether the candidate action is aligned with the
    # latent profile->future mapping, interacted with action identity.
    cols += [f"action_alignment_{a}" for a in ACTIONS[1:]]
    cols += [f"domain_{d}" for d in DOMAINS[1:]]
    cols += [f"operationalisation_{o}" for o in OPS[1:]]
    cols += [f"presentation_{p}" for p in PRESENTATIONS[1:]]
    cols += [f"condition_{c}" for c in CONDITIONS[1:]]
    X=np.zeros((len(rows),len(cols)))
    for i,r in enumerate(rows):
        action=r["action"]; future=r["future"]
        aligned=(future is not None and action==future)
        X[i,0]=1; j=1
        for a in ACTIONS[1:]: X[i,j]=int(action==a); j+=1
        for p in PROFILES[1:]: X[i,j]=int(r["profile"]==p); j+=1
        for a in ACTIONS[1:]:
            for p in PROFILES[1:]:
                X[i,j]=int(action==a and r["profile"]==p); j+=1
        for a in ACTIONS[1:]:
            X[i,j]=int(action==a and aligned); j+=1
        for d in DOMAINS[1:]: X[i,j]=int(r["domain"]==d); j+=1
        for o in OPS[1:]: X[i,j]=int(r["operationalisation"]==o); j+=1
        for p in PRESENTATIONS[1:]: X[i,j]=int(r["presentation"]==p); j+=1
        for c in CONDITIONS[1:]: X[i,j]=int(r["condition"]==c); j+=1
    return X,cols

def primary_contrast(cols):
    c=np.zeros(len(cols))
    # Contrast: average action-alignment coefficients for non-reference actions.
    for i,name in enumerate(cols):
        if name.startswith("action_alignment_"): c[i]=1/3
    return c

def audit(rows):
    X,cols=build_matrix(rows); c=primary_contrast(cols)
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
            "contrast_sha256":hashlib.sha256(c.tobytes()).hexdigest()}

if __name__=="__main__":
    print(json.dumps({"status":"MAPPING_REORGANISATION_MODEL_003_READY"},sort_keys=True))
