"""NEXT4 Model 010: identifiable within-profile action-logit differences.

The categorical choice likelihood identifies only differences between action
logits within each (surface, profile) block. This implementation uses a fixed
reference action and estimates three relative logits per surface/profile.
The primary estimand is the frozen permutation-aligned difference-in-differences
of within-profile logits between FUTURE_REASSIGNED and STATIC_CONTROL.
"""
from __future__ import annotations
import hashlib, json
import numpy as np
from itertools import permutations

ACTIONS = (0, 1, 2, 3)
PROFILES = ACTIONS
CONDITIONS = ("STATIC_CONTROL", "FUTURE_REASSIGNED", "SURFACE_CONTROL", "UNINFORMATIVE_NULL")
DOMAINS = (0, 1, 2)
OPS = (0, 1)
PRESENTATIONS = (0, 1, 2, 3)
CANDIDATE_N = (1728, 2304, 3456, 5184, 6912)
PERMS = tuple(permutations(ACTIONS))

def allocate(n):
    q = n // 96
    rows = []
    i = 0
    for condition in CONDITIONS:
        for domain in DOMAINS:
            for op in OPS:
                for presentation in PRESENTATIONS:
                    for k in range(q):
                        rows.append({
                            "choice_set_id": i,
                            "condition": condition,
                            "domain": domain,
                            "operationalisation": op,
                            "presentation": presentation,
                            "permutation": PERMS[(i + k) % 24],
                        })
                        i += 1
    return rows

def expand(rows):
    return [dict(r, profile=p, action=a) for r in rows for p in PROFILES for a in ACTIONS]

def parameter_columns(reference=0):
    actions = tuple(a for a in ACTIONS if a != reference)
    cols = [f"{surface}_profile_{p}_delta_action_{a}_ref_{reference}"
            for surface in ("STATIC", "FUTURE")
            for p in PROFILES for a in actions]
    cols += [f"condition_{c}" for c in CONDITIONS
             if c not in ("STATIC_CONTROL", "FUTURE_REASSIGNED")]
    cols += [f"domain_{d}" for d in DOMAINS[1:]]
    cols += [f"operationalisation_{o}" for o in OPS[1:]]
    cols += [f"presentation_{p}" for p in PRESENTATIONS[1:]]
    return cols

def build_matrix(rows, reference=0):
    actions = tuple(a for a in ACTIONS if a != reference)
    cols = parameter_columns(reference)
    X = np.zeros((len(rows), len(cols)))
    for i, r in enumerate(rows):
        j = 0
        surface = {"STATIC_CONTROL": "STATIC", "FUTURE_REASSIGNED": "FUTURE"}.get(r["condition"])
        for s in ("STATIC", "FUTURE"):
            for p in PROFILES:
                for a in actions:
                    X[i, j] = int(surface == s and r["profile"] == p and r["action"] == a)
                    j += 1
        for c in CONDITIONS:
            if c not in ("STATIC_CONTROL", "FUTURE_REASSIGNED"):
                X[i, j] = int(r["condition"] == c); j += 1
        for d in DOMAINS[1:]:
            X[i, j] = int(r["domain"] == d); j += 1
        for o in OPS[1:]:
            X[i, j] = int(r["operationalisation"] == o); j += 1
        for p in PRESENTATIONS[1:]:
            X[i, j] = int(r["presentation"] == p); j += 1
    return X, cols

def primary_contrast(cols, reference=0):
    c = np.zeros(len(cols))
    w = 1.0 / (24 * 4)
    for perm in PERMS:
        for p in PROFILES:
            a = perm[p]
            if a == p:
                continue
            # d_s(p,a)-d_s(p,p), with d_s(p,reference)=0.
            for surface, sign in (("FUTURE", 1.0), ("STATIC", -1.0)):
                prefix = f"{surface}_profile_{p}_delta_action_"
                if a != reference:
                    c[cols.index(prefix + f"{a}_ref_{reference}")] += sign * w
                if p != reference:
                    c[cols.index(prefix + f"{p}_ref_{reference}")] -= sign * w
    return c

def reference_change_matrix(old_reference, new_reference):
    """Map identifiable logits under a change of reference action.

    Old coordinates are d_a = eta_a-eta_old_ref; new coordinates are
    d_new_a = eta_a-eta_new_ref. For every non-reference action this is
    d_old_a-d_old_new_ref, with the old-reference coordinate interpreted as 0.
    """
    old = tuple(a for a in ACTIONS if a != old_reference)
    new = tuple(a for a in ACTIONS if a != new_reference)
    T = np.zeros((len(new), len(old)))
    for i, a in enumerate(new):
        if a != old_reference:
            T[i, old.index(a)] += 1.0
        if new_reference != old_reference:
            T[i, old.index(new_reference)] -= 1.0
    return T

def audit(n):
    rows = expand(allocate(n))
    X, cols = build_matrix(rows, reference=0)
    c = primary_contrast(cols, reference=0)
    rank = int(np.linalg.matrix_rank(X))
    _, s, vt = np.linalg.svd(X, full_matrices=False)
    rowspace = vt[:rank, :]
    resid = float(np.linalg.norm(c - rowspace.T @ (rowspace @ c)))
    return {
        "n": n, "rows": int(X.shape[0]), "columns": int(X.shape[1]),
        "rank": rank, "full_column_rank": rank == X.shape[1],
        "nullity": int(X.shape[1] - rank),
        "singular_values_min": float(s[-1]),
        "contrast_norm": float(np.linalg.norm(c)),
        "estimability_residual": resid,
        "contrast_estimable": resid < 1e-10,
        "matrix_sha256": hashlib.sha256(X.tobytes()).hexdigest(),
        "contrast_sha256": hashlib.sha256(c.tobytes()).hexdigest(),
    }

if __name__ == "__main__":
    print(json.dumps({
        "status": "TWO_SURFACE_MODEL_010_READY",
        "audits": [audit(n) for n in CANDIDATE_N],
    }, sort_keys=True))