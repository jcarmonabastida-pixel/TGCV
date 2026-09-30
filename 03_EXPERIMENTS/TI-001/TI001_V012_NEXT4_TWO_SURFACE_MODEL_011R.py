"""NEXT4 Model-011R: full DGP-aligned permutation mapping estimand.

Standalone revision of Model-011. The frozen DGP applies beta to every
permutation-aligned FUTURE_REASSIGNED cell, including fixed points. Model-011R
therefore represents the signal as two explicit components:

    nonidentity mapped alignment
    fixed-point mapped alignment

The scientific contrast averages the two components with their exact
population weights 72/96 and 24/96. Under DGP-002, both component coefficients
are beta, so the declared population estimand is exactly beta.
"""
from __future__ import annotations

import hashlib
import json
import numpy as np
from itertools import permutations

ACTIONS = (0, 1, 2, 3)
PROFILES = ACTIONS
CONDITIONS = (
    "STATIC_CONTROL",
    "FUTURE_REASSIGNED",
    "SURFACE_CONTROL",
    "UNINFORMATIVE_NULL",
)
DOMAINS = (0, 1, 2)
OPS = (0, 1)
PRESENTATIONS = (0, 1, 2, 3)
PERMS = tuple(permutations(ACTIONS))
CANDIDATE_N = (1728, 2304, 3456, 5184, 6912)


def allocate(n):
    per = n // 96
    rows = []
    i = 0
    for condition in CONDITIONS:
        for domain in DOMAINS:
            for op in OPS:
                for presentation in PRESENTATIONS:
                    for k in range(per):
                        rows.append(
                            {
                                "choice_set_id": i,
                                "condition": condition,
                                "domain": domain,
                                "operationalisation": op,
                                "presentation": presentation,
                                "permutation": PERMS[(i + k) % 24],
                            }
                        )
                        i += 1
    return rows


def expand(rows):
    out = []
    for r in rows:
        for profile in PROFILES:
            for action in ACTIONS:
                x = dict(r)
                x.update({"profile": profile, "action": action})
                x["future"] = (
                    profile
                    if r["condition"] != "FUTURE_REASSIGNED"
                    else r["permutation"][profile]
                )
                out.append(x)
    return out


def build_matrix(rows):
    cols = ["intercept"]
    cols += [f"action_{a}" for a in ACTIONS[1:]]
    cols += [f"profile_{p}" for p in PROFILES[1:]]
    cols += [
        f"action_profile_{a}_{p}"
        for a in ACTIONS[1:]
        for p in PROFILES[1:]
    ]
    cols += [f"condition_{c}" for c in CONDITIONS[1:]]
    cols += [
        f"condition_action_profile_{c}_{a}_{p}"
        for c in CONDITIONS[1:]
        for a in ACTIONS[1:]
        for p in PROFILES[1:]
    ]
    cols += [f"domain_{d}" for d in DOMAINS[1:]]
    cols += [f"operationalisation_{o}" for o in OPS[1:]]
    cols += [f"presentation_{p}" for p in PRESENTATIONS[1:]]
    cols += [
        "future_reassigned_nonidentity_mapped_action",
        "future_reassigned_fixedpoint_mapped_action",
    ]

    X = np.zeros((len(rows), len(cols)))
    for i, r in enumerate(rows):
        j = 0
        X[i, j] = 1
        j += 1

        for a in ACTIONS[1:]:
            X[i, j] = int(r["action"] == a)
            j += 1

        for p in PROFILES[1:]:
            X[i, j] = int(r["profile"] == p)
            j += 1

        for a in ACTIONS[1:]:
            for p in PROFILES[1:]:
                X[i, j] = int(r["action"] == a and r["profile"] == p)
                j += 1

        for c in CONDITIONS[1:]:
            X[i, j] = int(r["condition"] == c)
            j += 1
            for a in ACTIONS[1:]:
                for p in PROFILES[1:]:
                    X[i, j] = int(
                        r["condition"] == c
                        and r["action"] == a
                        and r["profile"] == p
                    )
                    j += 1

        for d in DOMAINS[1:]:
            X[i, j] = int(r["domain"] == d)
            j += 1

        for o in OPS[1:]:
            X[i, j] = int(r["operationalisation"] == o)
            j += 1

        for p in PRESENTATIONS[1:]:
            X[i, j] = int(r["presentation"] == p)
            j += 1

        X[i, j] = int(
            r["condition"] == "FUTURE_REASSIGNED"
            and r["future"] != r["profile"]
            and r["action"] == r["future"]
        )
        j += 1

        X[i, j] = int(
            r["condition"] == "FUTURE_REASSIGNED"
            and r["future"] == r["profile"]
            and r["action"] == r["future"]
        )

    return X, cols


def primary_contrast(cols):
    """Population-weighted full DGP signal: 72/96 nonidentity + 24/96 fixed."""
    c = np.zeros(len(cols))
    c[cols.index("future_reassigned_nonidentity_mapped_action")] = 72 / 96
    c[cols.index("future_reassigned_fixedpoint_mapped_action")] = 24 / 96
    return c


def audit(n):
    rows = expand(allocate(n))
    X, cols = build_matrix(rows)
    c = primary_contrast(cols)

    rank = int(np.linalg.matrix_rank(X))
    _, s, vt = np.linalg.svd(X, full_matrices=False)
    rowspace = vt[:rank, :]
    residual = float(np.linalg.norm(c - rowspace.T @ (rowspace @ c)))

    return {
        "n": n,
        "rows": len(rows),
        "columns": len(cols),
        "rank": rank,
        "nullity": len(cols) - rank,
        "full_column_rank": rank == len(cols),
        "estimability_residual": residual,
        "contrast_estimable": residual < 1e-10,
        "contrast_norm": float(np.linalg.norm(c)),
        "matrix_sha256": hashlib.sha256(X.tobytes()).hexdigest(),
        "contrast_sha256": hashlib.sha256(c.tobytes()).hexdigest(),
    }


if __name__ == "__main__":
    print(
        json.dumps(
            {
                "status": "MODEL_011R_READY",
                "signal_components": {
                    "nonidentity_weight": 72 / 96,
                    "fixedpoint_weight": 24 / 96,
                },
                "audits": [audit(n) for n in CANDIDATE_N],
            },
            sort_keys=True,
        )
    )
