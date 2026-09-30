"""Independent NEXT4 DGP -> Model-011 -> estimand population audit.

Does not import or execute Model-011. Reconstructs the frozen DGP-002 and the
Model-011 design matrix independently, then fits the population (expected
log-likelihood) multinomial model with no sampling error.

Gate criterion: for every beta in the frozen grid and every candidate N,
the recovered primary estimand must equal 0.75*beta within 1e-8.
"""
from __future__ import annotations
import hashlib, json
from itertools import permutations
import numpy as np
from scipy.optimize import minimize

ACTIONS=(0,1,2,3)
PROFILES=ACTIONS
CONDITIONS=("STATIC_CONTROL","FUTURE_REASSIGNED","SURFACE_CONTROL","UNINFORMATIVE_NULL")
DOMAINS=(0,1,2)
OPS=(0,1)
PRESENTATIONS=(0,1,2,3)
PERMS=tuple(permutations(ACTIONS))
CANDIDATE_N=(1728,2304,3456,5184,6912)
EFFECTS=(0,0.1,0.2,0.3,0.4,0.5,0.75,1)

def dgp_sets(n,beta):
    out=[]
    for i in range(n):
        d=i%3; o=(i//3)%2; p=(i//6)%4
        c=CONDITIONS[(i//24)%4]; perm=PERMS[i%24]; profile=i%4
        future=profile if c!="FUTURE_REASSIGNED" else perm[profile]
        logits=[]
        for a in ACTIONS:
            z=[0,0.1,-0.08,0.04][a]+[0,0.15,-0.15][d]+[0,0.1][o]+[0,0.05,-0.05,0.02][p]
            z += 0.04*((a+profile)%4)
            z += beta*int(c=="FUTURE_REASSIGNED" and a==future)
            logits.append(z)
        z=np.asarray(logits); e=np.exp(z-z.max()); probs=e/e.sum()
        out.append((d,o,p,c,perm,profile,future,probs))
    return out

def columns():
    c=["intercept"]+[f"action_{a}" for a in ACTIONS[1:]]+[f"profile_{p}" for p in PROFILES[1:]]
    c += [f"action_profile_{a}_{p}" for a in ACTIONS[1:] for p in PROFILES[1:]]
    c += [f"condition_{x}" for x in CONDITIONS[1:]]
    c += [f"condition_action_profile_{x}_{a}_{p}" for x in CONDITIONS[1:] for a in ACTIONS[1:] for p in PROFILES[1:]]
    c += [f"domain_{d}" for d in DOMAINS[1:]]+[f"operationalisation_{o}" for o in OPS[1:]]+[f"presentation_{p}" for p in PRESENTATIONS[1:]]
    c += ["future_reassigned_nonidentity_mapped_action"]
    return c

COLS=columns()
SIG=COLS.index("future_reassigned_nonidentity_mapped_action")

def matrix(sets):
    X=np.zeros((len(sets)*4,len(COLS)))
    for i,(d,o,p,c,perm,profile,future,_) in enumerate(sets):
        for a in ACTIONS:
            r=4*i+a; j=0; X[r,j]=1; j+=1
            for aa in ACTIONS[1:]: X[r,j]=int(a==aa); j+=1
            for pp in PROFILES[1:]: X[r,j]=int(profile==pp); j+=1
            for aa in ACTIONS[1:]:
                for pp in PROFILES[1:]: X[r,j]=int(a==aa and profile==pp); j+=1
            for cc in CONDITIONS[1:]:
                X[r,j]=int(c==cc); j+=1
                for aa in ACTIONS[1:]:
                    for pp in PROFILES[1:]:
                        X[r,j]=int(c==cc and a==aa and profile==pp); j+=1
            for dd in DOMAINS[1:]: X[r,j]=int(d==dd); j+=1
            X[r,j]=int(o==1); j+=1
            for pp in PRESENTATIONS[1:]: X[r,j]=int(p==pp); j+=1
            X[r,j]=int(c=="FUTURE_REASSIGNED" and future!=profile and a==future)
    return X

def fit_population(sets):
    X=matrix(sets).reshape(len(sets),4,-1)
    P=np.asarray([s[-1] for s in sets])
    def fg(b):
        z=np.einsum("nkp,p->nk",X,b); z-=z.max(axis=1,keepdims=True)
        q=np.exp(z); q/=q.sum(axis=1,keepdims=True)
        return float(-np.sum(P*np.log(q))), np.einsum("nkp,nk->p",X,q-P)
    res=minimize(lambda b: fg(b),np.zeros(len(COLS)),jac=True,method="BFGS",
                 options={"gtol":1e-10,"maxiter":3000})
    est=float(0.75*res.x[SIG])
    return {"estimate":est,"signal_coefficient":float(res.x[SIG]),
            "optimizer_success":bool(res.success),"gradient_inf_norm":float(np.max(np.abs(res.jac)))}

def audit():
    rows=[]
    for n in CANDIDATE_N:
        for beta in EFFECTS:
            r=fit_population(dgp_sets(n,beta))
            target=0.75*beta
            rows.append({"N":n,"beta":beta,"expected_theta":target,
                         "recovered_theta":r["estimate"],
                         "recovered_signal_coefficient":r["signal_coefficient"],
                         "absolute_error":abs(r["estimate"]-target),
                         **{k:r[k] for k in ("optimizer_success","gradient_inf_norm")}})
    maxerr=max(x["absolute_error"] for x in rows)
    return {"status":"PASS" if maxerr<=1e-8 else "FAIL",
            "criterion":"max absolute population recovery error <= 1e-8",
            "max_absolute_error":maxerr,"rows":rows,
            "independent_reconstruction":True,"sampling_error":False}

if __name__=="__main__":
    print(json.dumps(audit(),sort_keys=True))
