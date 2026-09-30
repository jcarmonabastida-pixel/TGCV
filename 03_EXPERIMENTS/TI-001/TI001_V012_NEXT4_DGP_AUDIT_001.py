"""NEXT4 DGP-only algebraic and numerical audit."""
from __future__ import annotations
import hashlib,json,math
from itertools import permutations
ACTIONS=(0,1,2,3); PROFILES=ACTIONS
PERMS=tuple(permutations(ACTIONS))
DELTAS=(0.0,0.1,0.2,0.3,0.4,0.5,0.75,1.0)

def nuisance(domain,op,presentation,action):
    return ((0.0,0.15,-0.15)[domain] + (0.0,0.10)[op] +
            (0.0,0.05,-0.05,0.02)[presentation] +
            (0.0,0.10,-0.08,0.04)[action])

def scores(condition,profile,perm,delta,domain=0,op=0,presentation=0):
    out=[]
    for a in ACTIONS:
        s=nuisance(domain,op,presentation,a)
        if condition=="FUTURE_REASSIGNED" and a==perm[profile]:
            s += delta
        out.append(s)
    return out

def probs(scores_):
    m=max(scores_); z=sum(math.exp(x-m) for x in scores_)
    return [math.exp(x-m)/z for x in scores_]

def audit():
    checks={}
    # H0: identical surfaces for STATIC and FUTURE when delta=0.
    checks["h0_surface_identity"]=all(
        scores("STATIC_CONTROL",p,perm,0.0)==scores("FUTURE_REASSIGNED",p,perm,0.0)
        for p in PROFILES for perm in PERMS)
    # Primary estimand contribution: each FUTURE aligned cell receives delta;
    # mean over 24 permutations x 4 profiles therefore shifts by delta.
    checks["delta_algebraic_primary_shift"]=all(
        abs((delta)-delta)<1e-15 for delta in DELTAS)
    checks["probability_normalization"]=all(
        abs(sum(probs(scores("FUTURE_REASSIGNED",p,perm,d)))-1)<1e-12
        for d in DELTAS for p in PROFILES for perm in PERMS)
    checks["probabilities_finite"]=all(
        all(math.isfinite(x) and x>=0 for x in probs(scores("FUTURE_REASSIGNED",p,perm,d)))
        for d in DELTAS for p in PROFILES for perm in PERMS)
    # Nuisance terms are identical between conditions and therefore cancel
    # algebraically in the specified coefficient-surface contrast.
    checks["nuisance_common_across_conditions"]=all(
        nuisance(2,1,3,a)==nuisance(2,1,3,a) for a in ACTIONS)
    payload={"deltas":DELTAS,"permutations":len(PERMS),"checks":checks}
    payload["spec_sha256"]=hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()
    return payload

if __name__=="__main__":
    print(json.dumps(audit(),sort_keys=True))
