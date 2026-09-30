"""NEXT4 design-stage power engine 002 consuming canonical DGP 002 and Model-010."""
from __future__ import annotations
from dataclasses import dataclass
import hashlib
import importlib.util
import json
import random
from itertools import permutations
from math import exp
from pathlib import Path

ACTIONS = (0, 1, 2, 3)
PROFILES = ACTIONS
DOMAINS = (0, 1, 2)
OPS = (0, 1)
PRESENTATIONS = (0, 1, 2, 3)
CONDITIONS = (
    "STATIC_CONTROL",
    "FUTURE_REASSIGNED",
    "SURFACE_CONTROL",
    "UNINFORMATIVE_NULL",
)
PERMUTATIONS = tuple(permutations(ACTIONS))

BASE_DIR = Path(__file__).resolve().parent
DGP_PATH = BASE_DIR / "TI001_V012_NEXT4_DGP_SPECIFICATION_002.json"
MODEL_PATH = BASE_DIR / "TI001_V012_NEXT4_TWO_SURFACE_MODEL_010.py"
MODEL_COMMIT = "23f00c0971bf7fd7584ff546ec523693e99c8c03"


def load_dgp():
    return json.loads(DGP_PATH.read_text(encoding="utf-8"))


def load_model():
    spec = importlib.util.spec_from_file_location("ti001_next4_model_010", MODEL_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load canonical Model-010")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@dataclass(frozen=True)
class Scenario:
    effect_label: str
    effect_size: float
    n_choice_sets: int
    replicate: int
    master_seed: int


def seed_for(s, i):
    return int.from_bytes(
        hashlib.sha256(
            f"{s.master_seed}|{s.effect_label}|{s.n_choice_sets}|{s.replicate}|{i}".encode()
        ).digest()[:8],
        "big",
    )


def softmax(xs):
    m = max(xs)
    ex = [exp(x - m) for x in xs]
    z = sum(ex)
    return [x / z for x in ex]


def mapping_for(condition, permutation):
    return (0, 1, 2, 3) if condition in ("SURFACE_CONTROL", "UNINFORMATIVE_NULL") else permutation


def build_choice_set(s, i, dgp):
    rng = random.Random(seed_for(s, i))
    domain = i % 3
    op = (i // 3) % 2
    presentation = (i // 6) % 4
    condition = CONDITIONS[(i // 24) % 4]
    permutation = PERMUTATIONS[i % 24]
    mapping = mapping_for(condition, permutation)
    profile = PROFILES[i % 4]
    future = mapping[profile]
    n = dgp["nuisance"]
    logits = []
    for action in ACTIONS:
        baseline = (
            n["baseline_action"][action]
            + n["domain"][domain]
            + n["operationalisation"][op]
            + n["presentation"][presentation]
            + 0.04 * ((action + profile) % 4)
        )
        signal = s.effect_size * int(
            condition == "FUTURE_REASSIGNED" and action == future
        )
        logits.append(baseline + signal)

    probs = softmax(logits)
    u = rng.random()
    c = 0.0
    chosen = ACTIONS[-1]
    for action, p in zip(ACTIONS, probs):
        c += p
        if u <= c:
            chosen = action
            break

    return {
        "choice_set_id": i,
        "domain": domain,
        "operationalisation": op,
        "presentation": presentation,
        "condition": condition,
        "permutation": permutation,
        "mapping": mapping,
        "profile": profile,
        "future": future,
        "chosen_action": chosen,
        "actions": list(ACTIONS),
        "probabilities": probs,
        "effect_label": s.effect_label,
        "effect_size": s.effect_size,
    }


def choice_set_to_action_rows(cs):
    return [
        dict(
            choice_set_id=cs["choice_set_id"],
            action=a,
            chosen=int(a == cs["chosen_action"]),
            profile=cs["profile"],
            domain=cs["domain"],
            operationalisation=cs["operationalisation"],
            presentation=cs["presentation"],
            condition=cs["condition"],
            permutation=cs["permutation"],
            mapping=cs["mapping"],
            future=cs["future"],
            mapping_aligned=int(a == cs["future"]),
        )
        for a in ACTIONS
    ]


def generate_dataset(s):
    dgp = load_dgp()
    sets = [build_choice_set(s, i, dgp) for i in range(s.n_choice_sets)]
    return sets, [r for cs in sets for r in choice_set_to_action_rows(cs)]


def digest(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def build_model_matrix(sets, model, reference=0):
    """Build the observed-choice likelihood matrix exactly for Model-010.

    Model-010 defines three relative action logits per (surface, profile)
    relative to reference action 0. The reference-action row therefore carries
    no surface coefficient; action 1/2/3 carry the corresponding relative
    coefficient. Nuisance columns are those returned by Model-010 itself.
    """
    import numpy as np

    cols = model.parameter_columns(reference=reference)
    index = {c: i for i, c in enumerate(cols)}
    X = []

    actions = tuple(a for a in ACTIONS if a != reference)
    for cs in sets:
        surface = {
            "STATIC_CONTROL": "STATIC",
            "FUTURE_REASSIGNED": "FUTURE",
        }.get(cs["condition"])

        for action in ACTIONS:
            row = np.zeros(len(cols))

            if surface is not None and action != reference:
                key = (
                    f"{surface}_profile_{cs['profile']}_"
                    f"delta_action_{action}_ref_{reference}"
                )
                row[index[key]] = 1.0

            if cs["condition"] not in ("STATIC_CONTROL", "FUTURE_REASSIGNED"):
                row[index[f"condition_{cs['condition']}"]] = 1.0

            for d in DOMAINS[1:]:
                if cs["domain"] == d:
                    row[index[f"domain_{d}"]] = 1.0

            if cs["operationalisation"] == 1:
                row[index["operationalisation_1"]] = 1.0

            for p in PRESENTATIONS[1:]:
                if cs["presentation"] == p:
                    row[index[f"presentation_{p}"]] = 1.0

            X.append(row)

    return np.asarray(X), cols


def fit_primary_contrast(sets, reference=0):
    """Fit Model-010 and return its frozen primary contrast."""
    import numpy as np
    from scipy.optimize import minimize

    model = load_model()
    X, cols = build_model_matrix(sets, model, reference=reference)
    n_sets = len(sets)
    n_parameters = X.shape[1]

    def probabilities(beta):
        z = (X @ beta).reshape(n_sets, len(ACTIONS))
        z -= z.max(axis=1, keepdims=True)
        e = np.exp(z)
        return e / e.sum(axis=1, keepdims=True)

    chosen = np.asarray([cs["chosen_action"] for cs in sets], dtype=int)

    def nll(beta):
        pr = probabilities(beta)
        return float(-np.log(pr[np.arange(n_sets), chosen]).sum())

    def grad(beta):
        pr = probabilities(beta)
        target = np.zeros_like(pr)
        target[np.arange(n_sets), chosen] = 1.0
        Xg = X.reshape(n_sets, len(ACTIONS), n_parameters)
        return (Xg * (pr - target)[:, :, None]).sum(axis=(0, 1))

    fit = minimize(
        nll,
        np.zeros(n_parameters),
        jac=grad,
        method="BFGS",
    )
    beta = fit.x

    pr = probabilities(beta)
    H = np.zeros((n_parameters, n_parameters))
    Xg = X.reshape(n_sets, len(ACTIONS), n_parameters)
    for i in range(n_sets):
        Xi = Xg[i]
        W = np.diag(pr[i]) - np.outer(pr[i], pr[i])
        H += Xi.T @ W @ Xi

    cov = np.linalg.pinv(H, rcond=1e-10)
    c = model.primary_contrast(cols, reference=reference)
    est = float(c @ beta)
    se = float(np.sqrt(max(0.0, c @ cov @ c)))
    zstat = est / se if se > 0 else float("nan")

    from math import erf, sqrt
    pval = float(1 - erf(abs(zstat) / sqrt(2))) if se > 0 else float("nan")

    return {
        "model": "TI001_V012_NEXT4_TWO_SURFACE_MODEL_010",
        "model_commit": MODEL_COMMIT,
        "reference_action": reference,
        "parameter_columns": len(cols),
        "converged": bool(fit.success),
        "message": str(fit.message),
        "estimate": est,
        "se": se,
        "wald_z": zstat,
        "p_value": pval,
        "reject_alpha_0_05": bool(pval < 0.05),
        "rank_hessian": int(np.linalg.matrix_rank(H)),
        "n_parameters": int(n_parameters),
        "contrast_sha256": hashlib.sha256(c.tobytes()).hexdigest(),
    }


if __name__ == "__main__":
    dgp = load_dgp()
    model = load_model()
    s = Scenario("NULL", 0.0, 1728, 0, 410927)
    sets, rows = generate_dataset(s)
    print(
        json.dumps(
            {
                "status": "CHOICE_SET_ENGINE_READY_MODEL_010",
                "dgp_artifact": dgp["artifact"],
                "model": "TI001_V012_NEXT4_TWO_SURFACE_MODEL_010",
                "model_commit": MODEL_COMMIT,
                "model_parameter_columns": len(model.parameter_columns(reference=0)),
                "choice_sets": len(sets),
                "action_rows": len(rows),
                "dataset_sha256": digest(rows),
                "provider_api_calls": False,
                "scientific_executor_calls": False,
            },
            sort_keys=True,
        )
    )
