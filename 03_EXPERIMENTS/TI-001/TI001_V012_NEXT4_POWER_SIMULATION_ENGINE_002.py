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


def fit_primary_contrast(sets):
    """Fit the frozen model-009 surface contrast by multinomial choice likelihood.

    This implementation uses scipy.optimize.minimize when available. The
    parameterization is the 32 surface cells plus the declared nuisance terms,
    with no redundant intercept. The primary contrast is the mean FUTURE
    permutation-aligned cell minus STATIC identity cell across 24 permutations
    and 4 profiles.
    """
    import numpy as np
    from scipy.optimize import minimize

    cells=[(a,p) for a in ACTIONS for p in PROFILES]
    cols=[("STATIC",a,p) for a,p in cells]+[("FUTURE",a,p) for a,p in cells]
    cols += [("condition",c) for c in ("SURFACE_CONTROL","UNINFORMATIVE_NULL")]
    cols += [("domain",d) for d in (1,2)]
    cols += [("op",1)]
    cols += [("presentation",p) for p in (1,2,3)]
    index={c:i for i,c in enumerate(cols)}
    X=[]; y=[]
    for cs in sets:
        for a in ACTIONS:
            row=np.zeros(len(cols))
            # Condition-specific two-surface basis.
            if cs["condition"]=="STATIC_CONTROL":
                row[index[("STATIC",a,cs["profile"])]]=1
            elif cs["condition"]=="FUTURE_REASSIGNED":
                row[index[("FUTURE",a,cs["profile"])]]=1
            if cs["condition"]=="SURFACE_CONTROL": row[index[("condition","SURFACE_CONTROL")]]=1
            if cs["condition"]=="UNINFORMATIVE_NULL": row[index[("condition","UNINFORMATIVE_NULL")]]=1
            if cs["domain"] in (1,2): row[index[("domain",cs["domain"])]]=1
            if cs["operationalisation"]==1: row[index[("op",1)]]=1
            if cs["presentation"] in (1,2,3): row[index[("presentation",cs["presentation"])]]=1
            X.append(row); y.append(cs["chosen_action"]==a)
    X=np.asarray(X); y=np.asarray(y,dtype=float)
    groups=np.repeat(np.arange(len(sets)),4)
    def nll(beta):
        z=(X@beta).reshape(-1,4)
        z-=z.max(axis=1,keepdims=True)
        lse=np.log(np.exp(z).sum(axis=1))
        chosen=np.asarray([cs["chosen_action"] for cs in sets])
        return float(np.sum(-z[np.arange(len(sets)),chosen]+lse))
    def grad(beta):
        z=(X@beta).reshape(-1,4); z-=z.max(axis=1,keepdims=True)
        e=np.exp(z); pr=e/e.sum(axis=1,keepdims=True)
        target=np.zeros_like(pr)
        chosen=np.asarray([cs["chosen_action"] for cs in sets]); target[np.arange(len(sets)),chosen]=1
        return (X.reshape(-1,4,X.shape[1])*(pr-target)[:,:,None]).sum(axis=(0,1))
    fit=minimize(nll,np.zeros(X.shape[1]),jac=grad,method="BFGS")
    beta=fit.x
    # Observed information from multinomial Hessian.
    z=(X@beta).reshape(-1,4); z-=z.max(axis=1,keepdims=True)
    e=np.exp(z); pr=e/e.sum(axis=1,keepdims=True)
    H=np.zeros((X.shape[1],X.shape[1]))
    Xg=X.reshape(-1,4,X.shape[1])
    for i in range(len(sets)):
        Xi=Xg[i]; W=np.diag(pr[i])-np.outer(pr[i],pr[i]); H+=Xi.T@W@Xi
    cov=np.linalg.pinv(H,rcond=1e-10)
    c=np.zeros(X.shape[1])
    w=1/(24*4)
    for perm in PERMUTATIONS:
        for p in PROFILES:
            c[index[("FUTURE",perm[p],p)]]+=w
            c[index[("STATIC",p,p)]]-=w
    est=float(c@beta); se=float(np.sqrt(max(0,c@cov@c)))
    zstat=est/se if se>0 else float("nan")
    from math import erf,sqrt
    pval=float(1-erf(abs(zstat)/sqrt(2))) if se>0 else float("nan")
    return {"converged":bool(fit.success),"message":str(fit.message),"estimate":est,
            "se":se,"wald_z":zstat,"p_value":pval,"reject_alpha_0_05":bool(pval<0.05),
            "rank_hessian":int(np.linalg.matrix_rank(H)),"n_parameters":int(X.shape[1])}
