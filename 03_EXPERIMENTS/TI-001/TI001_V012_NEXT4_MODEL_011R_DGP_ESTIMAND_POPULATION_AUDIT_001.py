"""Independent NEXT4 DGP-002 -> Model-011R population representability audit.

This audit is algebraic and sampling-free. It reconstructs the frozen DGP-002
logits and the Model-011R design matrix independently, then verifies that the
DGP logits are represented exactly by a Model-011R coefficient vector for
every candidate N and every frozen effect value.

Gate:
  beta_nonidentity = delta
  beta_fixedpoint  = delta
  theta = 0.75*beta_nonidentity + 0.25*beta_fixedpoint = delta

No Monte Carlo, provider calls, or empirical outcomes are used.
"""
from __future__ import annotations
import hashlib
import json
from itertools import permutations
import numpy as np

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
EFFECTS = (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0)


def allocate(n):
    per = n // 96
    rows = []
    i = 0
    for condition in CONDITIONS:
        for domain in DOMAINS:
            for op in OPS:
                for presentation in PRESENTATIONS:
                    for k in range(per):
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


def columns():
    c = ["intercept"]
    c += [f"action_{a}" for a in ACTIONS[1:]]
    c += [f"profile_{p}" for p in PROFILES[1:]]
    c += [
        f"action_profile_{a}_{p}"
        for a in ACTIONS[1:]
        for p in PROFILES[1:]
    ]
    c += [f"condition_{x}" for x in CONDITIONS[1:]]
    c += [
        f"condition_action_profile_{x}_{a}_{p}"
        for x in CONDITIONS[1:]
        for a in ACTIONS[1:]
        for p in PROFILES[1:]
    ]
    c += [f"domain_{d}" for d in DOMAINS[1:]]
    c += [f"operationalisation_{o}" for o in OPS[1:]]
    c += [f"presentation_{p}" for p in PRESENTATIONS[1:]]
    c += [
        "future_reassigned_nonidentity_mapped_action",
        "future_reassigned_fixedpoint_mapped_action",
    ]
    return c


COLS = columns()


def model_matrix(rows):
    X = np.zeros((len(rows), len(COLS)))
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
    return X


def nuisance_logits(r):
    baseline = (0.0, 0.1, -0.08, 0.04)
    domain = (0.0, 0.15, -0.15)
    op = (0.0, 0.1)
    presentation = (0.0, 0.05, -0.05, 0.02)
    return (
        baseline[r["action"]]
        + 0.04 * ((r["action"] + r["profile"]) % 4)
        + domain[r["domain"]]
        + op[r["operationalisation"]]
        + presentation[r["presentation"]]
    )


def dgp_logits(rows, delta):
    z = np.zeros(len(rows))
    for i, r in enumerate(rows):
        signal = int(
            r["condition"] == "FUTURE_REASSIGNED"
            and r["action"] == r["future"]
        )
        z[i] = nuisance_logits(r) + delta * signal
    return z


def coefficient_vector(delta):
    b = np.zeros(len(COLS))
    b[COLS.index("intercept")] = 0.0

    baseline = (0.0, 0.1, -0.08, 0.04)

    # Exact saturated action x profile representation of
    # baseline[action] + 0.04*((action+profile) mod 4).
    for a in ACTIONS[1:]:
        b[COLS.index(f"action_{a}")] = baseline[a] + 0.04 * (a % 4)
    for p in PROFILES[1:]:
        b[COLS.index(f"profile_{p}")] = 0.04 * (p % 4)
    for a in ACTIONS[1:]:
        for p in PROFILES[1:]:
            target = 0.04 * ((a + p) % 4)
            additive = 0.04 * (a % 4) + 0.04 * (p % 4)
            b[COLS.index(f"action_profile_{a}_{p}")] = target - additive

    for d in DOMAINS[1:]:
        b[COLS.index(f"domain_{d}")] = (0.0, 0.15, -0.15)[d]
    b[COLS.index("operationalisation_1")] = 0.1
    for p in PRESENTATIONS[1:]:
        b[COLS.index(f"presentation_{p}")] = (0.0, 0.05, -0.05, 0.02)[p]

    # DGP-002 applies the same delta to both mapping surfaces.
    b[COLS.index("future_reassigned_nonidentity_mapped_action")] = delta
    b[COLS.index("future_reassigned_fixedpoint_mapped_action")] = delta
    return b


def audit():
    rows_out = []
    max_abs = 0.0
    max_nonidentity_signal_error = 0.0
    max_fixedpoint_signal_error = 0.0

    for n in CANDIDATE_N:
        rows = expand(allocate(n))
        X = model_matrix(rows)
        for delta in EFFECTS:
            beta = coefficient_vector(delta)
            dgp = dgp_logits(rows, delta)
            represented = X @ beta
            residual = float(np.max(np.abs(dgp - represented)))

            nonidentity = np.array([
                int(
                    r["condition"] == "FUTURE_REASSIGNED"
                    and r["future"] != r["profile"]
                    and r["action"] == r["future"]
                )
                for r in rows
            ])
            fixedpoint = np.array([
                int(
                    r["condition"] == "FUTURE_REASSIGNED"
                    and r["future"] == r["profile"]
                    and r["action"] == r["future"]
                )
                for r in rows
            ])
            # The coefficient assignments themselves are the population
            # component coefficients; these checks make the intended mapping
            # explicit and independent of any likelihood optimizer.
            b_nonidentity = float(beta[COLS.index(
                "future_reassigned_nonidentity_mapped_action"
            )])
            b_fixedpoint = float(beta[COLS.index(
                "future_reassigned_fixedpoint_mapped_action"
            )])
            theta = 0.75 * b_nonidentity + 0.25 * b_fixedpoint
            signal_target_error = abs(theta - delta)

            max_abs = max(max_abs, residual)
            max_nonidentity_signal_error = max(
                max_nonidentity_signal_error, abs(b_nonidentity - delta)
            )
            max_fixedpoint_signal_error = max(
                max_fixedpoint_signal_error, abs(b_fixedpoint - delta)
            )

            rows_out.append({
                "N": n,
                "delta": delta,
                "choice_sets": n,
                "action_rows": len(rows),
                "nonidentity_cells": int(nonidentity.sum()),
                "fixedpoint_cells": int(fixedpoint.sum()),
                "beta_nonidentity": b_nonidentity,
                "beta_fixedpoint": b_fixedpoint,
                "theta": theta,
                "theta_target": delta,
                "theta_absolute_error": signal_target_error,
                "max_logit_representation_error": residual,
                "matrix_sha256": hashlib.sha256(X.tobytes()).hexdigest(),
            })

    status = (
        max_abs <= 1e-12
        and max_nonidentity_signal_error <= 1e-12
        and max_fixedpoint_signal_error <= 1e-12
        and max(x["theta_absolute_error"] for x in rows_out) <= 1e-12
    )
    return {
        "artifact": "TI001_V012_NEXT4_MODEL_011R_DGP_ESTIMAND_POPULATION_AUDIT_001",
        "status": "PASS" if status else "FAIL",
        "audit_type": "INDEPENDENT_ALGEBRAIC_DGP_TO_MODEL_011R_REPRESENTABILITY",
        "sampling_error": False,
        "provider_calls": False,
        "monte_carlo": False,
        "gate": "Exact DGP-002 logit representation in Model-011R and theta=delta for every N and delta.",
        "candidate_N": list(CANDIDATE_N),
        "effect_grid": list(EFFECTS),
        "signal_weights": {"nonidentity": 0.75, "fixedpoint": 0.25},
        "max_logit_representation_error": max_abs,
        "max_nonidentity_coefficient_error": max_nonidentity_signal_error,
        "max_fixedpoint_coefficient_error": max_fixedpoint_signal_error,
        "max_theta_error": max(x["theta_absolute_error"] for x in rows_out),
        "rows": rows_out,
    }


if __name__ == "__main__":
    print(json.dumps(audit(), sort_keys=True))
