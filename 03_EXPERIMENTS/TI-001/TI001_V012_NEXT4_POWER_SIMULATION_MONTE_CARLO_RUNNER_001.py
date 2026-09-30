"""NEXT4 frozen Monte Carlo runner.

Executes one frozen (N, effect) cell with 1000 replicates.
No provider calls, adaptive stopping, or post-result tuning.
"""
from __future__ import annotations
import argparse, hashlib, json, random
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from TI001_V012_NEXT4_POWER_SIMULATION_ENGINE_002 import (
    ACTIONS, CONDITIONS, DOMAINS, OPS, PRESENTATIONS, PERMUTATIONS,
    Scenario, load_dgp, load_model, seed_for, build_model_matrix,
)

ROOT = Path(__file__).resolve().parent
MASTER_SEED = 20260930
REPLICATES = 1000
ALPHA = 0.05
EFFECTS = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0)
NS = (1728, 2304, 3456, 5184, 6912)


def stable_seed(master_seed, effect_label, n, replicate, choice_set_id):
    return int.from_bytes(
        hashlib.sha256(
            f"{master_seed}|{effect_label}|{n}|{replicate}|{choice_set_id}".encode()
        ).digest()[:8], "big"
    )


def choice_data(s, dgp):
    rng = [random.Random(stable_seed(s.master_seed, s.effect_label, s.n_choice_sets, s.replicate, int(i))).random()
           for i in range(s.n_choice_sets)]
    i = np.arange(s.n_choice_sets, dtype=np.int64)
    domain = i % 3
    op = (i // 3) % 2
    presentation = (i // 6) % 4
    condition_idx = (i // 24) % 4
    profile = i % 4
    perm_idx = i % 24
    perms = np.asarray(PERMUTATIONS, dtype=np.int64)
    permutation = perms[perm_idx]
    is_signal = (condition_idx == 1)
    future = np.where(is_signal, permutation[np.arange(s.n_choice_sets), profile], profile)

    n = dgp["nuisance"]
    pa = float(n["profile_action_formula"].split("*", 1)[0])
    logits = np.empty((s.n_choice_sets, 4), dtype=float)
    for a in ACTIONS:
        logits[:, a] = (
            n["baseline_action"][a]
            + np.asarray(n["domain"], dtype=float)[domain]
            + np.asarray(n["operationalisation"], dtype=float)[op]
            + np.asarray(n["presentation"], dtype=float)[presentation]
            + pa * ((a + profile) % 4)
            + s.effect_size * (is_signal & (a == future))
        )
    logits -= logits.max(axis=1, keepdims=True)
    p = np.exp(logits)
    p /= p.sum(axis=1, keepdims=True)
    u = np.asarray(rng, dtype=float)
    chosen = (u[:, None] > np.cumsum(p, axis=1)).sum(axis=1)
    return chosen, domain, op, presentation, condition_idx, profile, future, permutation


def fit_cell(s, dgp, model):
    chosen, domain, op, presentation, condition_idx, profile, future, permutation = choice_data(s, dgp)
    sets = []
    for i in range(s.n_choice_sets):
        condition = CONDITIONS[int(condition_idx[i])]
        sets.append({
            "choice_set_id": i, "domain": int(domain[i]),
            "operationalisation": int(op[i]), "presentation": int(presentation[i]),
            "condition": condition, "permutation": tuple(permutation[i]),
            "mapping": tuple(permutation[i]) if condition in ("STATIC_CONTROL","FUTURE_REASSIGNED") else (0,1,2,3),
            "profile": int(profile[i]), "future": int(future[i]), "chosen_action": int(chosen[i]),
        })

    X, active_cols, full_cols, _ = build_model_matrix(sets, model, reference=0)
    n = len(sets)
    k = X.shape[1]
    Xg = X.reshape(n, 4, k)

    def probs(beta):
        z = np.einsum("nak,k->na", Xg, beta)
        z -= z.max(axis=1, keepdims=True)
        e = np.exp(z)
        return e / e.sum(axis=1, keepdims=True)

    def nll(beta):
        p = probs(beta)
        return float(-np.log(np.maximum(p[np.arange(n), chosen], 1e-300)).sum())

    def grad(beta):
        p = probs(beta)
        target = np.zeros_like(p)
        target[np.arange(n), chosen] = 1.0
        return np.einsum("na,nak->k", p-target, Xg)

    fit = minimize(nll, np.zeros(k), jac=grad, method="BFGS")
    p = probs(fit.x)
    H = np.zeros((k,k))
    for i in range(n):
        W = np.diag(p[i]) - np.outer(p[i], p[i])
        H += Xg[i].T @ W @ Xg[i]
    cov = np.linalg.pinv(H, rcond=1e-10)

    c_full = model.primary_contrast(full_cols)
    full_indices = {name: j for j, name in enumerate(full_cols)}
    active_indices = np.asarray([full_indices[name] for name in active_cols], dtype=int)
    c = c_full[active_indices]
    est = float(c @ fit.x)
    se = float(np.sqrt(max(0.0, c @ cov @ c)))
    z = est / se if se > 0 else np.nan
    pv = float(2.0 * __import__("scipy").special.ndtr(-abs(z))) if se > 0 else np.nan
    return (
        bool(fit.success), est, se, pv, int(np.linalg.matrix_rank(H)),
        hashlib.sha256(c.tobytes()).hexdigest(),
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, choices=NS, required=True)
    ap.add_argument("--effect", type=float, choices=EFFECTS, required=True)
    ap.add_argument("--replicates", type=int, default=REPLICATES)
    args = ap.parse_args()
    if args.replicates != REPLICATES:
        raise SystemExit("Frozen specification requires exactly 1000 replicates")
    dgp, model = load_dgp(), load_model()
    label = f"DELTA_{args.effect:g}"
    rows=[]; failures=0; rejections=0; estimates=[]; ses=[]
    for r in range(REPLICATES):
        s=Scenario(label,args.effect,args.n,r,MASTER_SEED)
        ok,est,se,pv,rank,ch=fit_cell(s,dgp,model)
        failures += int(not ok or not np.isfinite(est) or not np.isfinite(se))
        if ok and np.isfinite(pv):
            rejections += int(pv < ALPHA)
            estimates.append(est); ses.append(se)
        rows.append({"replicate":r,"converged":ok,"estimate":est,"se":se,"p_value":pv,"rank_hessian":rank,"contrast_sha256":ch})
    valid=len(estimates)
    out={
      "artifact":"TI001_V012_NEXT4_POWER_SIMULATION_CELL_RESULT_001",
      "specification":"TI001_V012_NEXT4_POWER_SIMULATION_EXECUTION_SPECIFICATION_002",
      "engine":"TI001_V012_NEXT4_POWER_SIMULATION_ENGINE_002.py",
      "model":"TI001_V012_NEXT4_TWO_SURFACE_MODEL_011R",
      "dgp":"TI001_V012_NEXT4_DGP_SPECIFICATION_002",
      "master_seed":MASTER_SEED,"N":args.n,"effect_size":args.effect,"effect_label":label,
      "replicates":REPLICATES,"convergence_count":REPLICATES-failures,"valid_fit_count":valid,
      "rejection_count":rejections,"empirical_rejection_rate":rejections/valid if valid else None,
      "mean_estimate":float(np.mean(estimates)) if estimates else None,
      "sd_estimate":float(np.std(estimates,ddof=1)) if valid>1 else None,
      "mean_se":float(np.mean(ses)) if ses else None,
      "diagnostics":{"fit_failures":failures,"nonfinite_estimates":sum(not np.isfinite(x["estimate"]) for x in rows),
                     "nonfinite_se":sum(not np.isfinite(x["se"]) for x in rows),
                     "singular_or_rank_failures":sum(x["rank_hessian"]<k for x in rows),
                     "seed_replay_hash":hashlib.sha256(json.dumps([stable_seed(MASTER_SEED,label,args.n,r,r) for r in range(REPLICATES)]).encode()).hexdigest()},
      "scientific_execution":True,"provider_api_calls":False,"adaptive_stopping":False,"parameter_tuning_after_results":False,
      "replicates_detail":rows
    }
    raw=json.dumps(out,sort_keys=True,separators=(",",":"),allow_nan=False).encode()
    out["result_sha256"]=hashlib.sha256(raw).hexdigest()
    outpath=ROOT/f"TI001_V012_NEXT4_POWER_SIMULATION_CELL_N{args.n}_E{args.effect:g}.json"
    outpath.write_text(json.dumps(out,sort_keys=True,indent=2)+"\\n",encoding="utf-8")
    print(outpath.name)
    print(json.dumps({k:out[k] for k in ("N","effect_size","replicates","convergence_count","valid_fit_count","rejection_count","empirical_rejection_rate","result_sha256")},sort_keys=True))

if __name__=="__main__":
    main()
