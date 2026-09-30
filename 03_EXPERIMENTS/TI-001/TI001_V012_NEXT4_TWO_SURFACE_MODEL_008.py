"""NEXT4 explicit two-surface action×profile model 008."""
from __future__ import annotations
import hashlib,json
import numpy as np
from itertools import permutations
ACTIONS=(0,1,2,3); PROFILES=ACTIONS
CONDITIONS=("STATIC_CONTROL","FUTURE_REASSIGNED","SURFACE_CONTROL","UNINFORMATIVE_NULL")
DOMAINS=(0,1,2); OPS=(0,1); PRESENTATIONS=(0,1,2,3)
CANDIDATE_N=(1728,2304,3456,5184,6912); PERMS=tuple(permutations(ACTIONS))

def allocate(n):
    q=n//96; rows=[]; i=0
    for c in CONDITIONS:
      for d in DOMAINS:
       for o in OPS:
        for p in PRESENTATIONS:
         for k in range(q):
          rows.append({"choice_set_id":i,"condition":c,"domain":d,"operationalisation":o,
                       "presentation":p,"permutation":PERMS[(i+k)%24]}); i+=1
    return rows

def expand(rows):
    return [dict(r,profile=p,action=a)
            for r in rows for p in PROFILES for a in ACTIONS]

def build_matrix(rows):
    # Explicit two-surface parameterisation. Each surface has its own
    # action×profile cell parameters; no surface is represented as a
    # condition dummy plus an interaction relative to an arbitrary reference.
    cells=[(a,p) for a in ACTIONS for p in PROFILES]
    cols=["intercept"]
    cols += [f"surface_{s}_ap_{a}_{p}" for s in ("STATIC","FUTURE")
             for a,p in cells]
    cols += [f"condition_{c}" for c in CONDITIONS if c not in ("STATIC_CONTROL","FUTURE_REASSIGNED")]
    cols += [f"domain_{d}" for d in DOMAINS[1:]]
    cols += [f"operationalisation_{o}" for o in OPS[1:]]
    cols += [f"presentation_{p}" for p in PRESENTATIONS[1:]]
    X=np.zeros((len(rows),len(cols)))
    for i,r in enumerate(rows):
      j=0; X[i,j]=1; j+=1
      s={"STATIC_CONTROL":"STATIC","FUTURE_REASSIGNED":"FUTURE"}.get(r["condition"])
      for surf in ("STATIC","FUTURE"):
       for a,p in cells:
        X[i,j]=int(surf==s and r["action"]==a and r["profile"]==p); j+=1
      for c in CONDITIONS:
       if c not in ("STATIC_CONTROL","FUTURE_REASSIGNED"):
        X[i,j]=int(r["condition"]==c); j+=1
      for d in DOMAINS[1:]: X[i,j]=int(r["domain"]==d); j+=1
      for o in OPS[1:]: X[i,j]=int(r["operationalisation"]==o); j+=1
      for p in PRESENTATIONS[1:]: X[i,j]=int(r["presentation"]==p); j+=1
    return X,cols

def primary_contrast(cols):
    c=np.zeros(len(cols)); w=1/(24*4)
    for perm in PERMS:
      for p in PROFILES:
       a=perm[p]
       c[cols.index(f"surface_FUTURE_ap_{a}_{p}")]+=w
       c[cols.index(f"surface_STATIC_ap_{p}_{p}")]-=w
    return c

def audit(n):
    X,cols=build_matrix(expand(allocate(n))); c=primary_contrast(cols)
    rank=int(np.linalg.matrix_rank(X))
    # estimability is c in row space of X
    _,s,vt=np.linalg.svd(X,full_matrices=False)
    rs=vt[:rank,:]
    resid=float(np.linalg.norm(c-rs.T@(rs@c)))
    return {"n":n,"rows":X.shape[0],"columns":X.shape[1],"rank":rank,
            "full_column_rank":rank==X.shape[1],
            "singular_values_min":float(s[-1]),
            "contrast_norm":float(np.linalg.norm(c)),
            "estimability_residual":resid,"contrast_estimable":resid<1e-10,
            "matrix_sha256":hashlib.sha256(X.tobytes()).hexdigest(),
            "contrast_sha256":hashlib.sha256(c.tobytes()).hexdigest()}
if __name__=="__main__":
 print(json.dumps({"status":"TWO_SURFACE_MODEL_008_READY",
                   "audits":[audit(n) for n in CANDIDATE_N]},sort_keys=True))
