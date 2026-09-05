"""N-R7 preflight/conformance runner.

This runner MUST NOT fit a learner or perform scientific inference. It validates
that the environment and frozen predictor artifacts satisfy the registered
execution boundary before scientific execution is authorized.
"""
from __future__ import annotations

import hashlib
import inspect
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EXP = ROOT / "03_EXPERIMENTS" / "EMP-1.1"
ART = EXP / "artifacts" / "N-R5.3_PREDICTOR_DATASET"
SPEC = EXP / "N-R7_CONTROLLED_LEARNER_EXECUTION_SPECIFICATION_v0.1.md"
LEARNER = EXP / "src" / "branch_n_r6_learner_v01.py"

EXPECTED = {
    "train_sha256": "d40e3d5f5bd8839d5c83efb1fa2a2d33f432c65c47f568516152dce578f991bd",
    "test_sha256": "8ae5d84ef0bd1dc50835b1b006e20f299437f2a49395b31e057c0f016d1d3b35",
    "train_count": 30000,
    "test_count": 10000,
    "b_dim": 16,
    "r_dim": 58,
    "br_dim": 74,
    "horizon": 6,
    "hgb_seed": 3100000,
    "signflip_seed": 13579,
    "signflip_n": 200000,
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_jsonl(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def main() -> None:
    checks = []

    checks.append({"name": "specification_exists", "status": "PASS" if SPEC.is_file() else "FAIL"})
    checks.append({"name": "learner_implementation_exists", "status": "PASS" if LEARNER.is_file() else "FAIL"})

    train = ART / "train_predictors.jsonl"
    test = ART / "test_predictors.jsonl"
    required = [train, test, ART / "PROVENANCE.json", ART / "INTEGRITY_REPORT.json"]
    checks.append({"name": "frozen_predictor_artifacts_exist", "status": "PASS" if all(p.is_file() for p in required) else "FAIL"})

    if train.is_file() and test.is_file():
        train_hash = sha256(train)
        test_hash = sha256(test)
        checks.append({"name": "frozen_predictor_hashes", "status": "PASS" if train_hash == EXPECTED["train_sha256"] and test_hash == EXPECTED["test_sha256"] else "FAIL", "train": train_hash, "test": test_hash})

        tr = load_jsonl(train)
        te = load_jsonl(test)
        checks.append({"name": "frozen_counts", "status": "PASS" if len(tr) == 30000 and len(te) == 10000 else "FAIL", "train": len(tr), "test": len(te)})

        def shape_ok(rows, dims):
            return all(len(x.get("B", [])) == dims[0] and len(x.get("R", [])) == dims[1] and len(x.get("BR", [])) == dims[2] for x in rows)

        checks.append({"name": "frozen_dimensions", "status": "PASS" if shape_ok(tr, (16,58,74)) and shape_ok(te, (16,58,74)) else "FAIL"})
        checks.append({"name": "canonical_episode_ids", "status": "PASS" if [x["episode_id"] for x in tr] == list(range(30000)) and [x["episode_id"] for x in te] == list(range(10000)) else "FAIL"})
        checks.append({"name": "BR_concatenation", "status": "PASS" if all(x["BR"] == x["B"] + x["R"] for x in tr + te) else "FAIL"})

    try:
        import numpy as np
        import sklearn
        from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier

        hgb_params = {
            "loss": "log_loss", "learning_rate": 0.1, "max_iter": 100,
            "max_leaf_nodes": 31, "max_depth": None, "min_samples_leaf": 20,
            "l2_regularization": 0.0, "max_features": 1.0, "max_bins": 255,
            "categorical_features": None, "early_stopping": "auto", "scoring": "loss",
            "validation_fraction": 0.1, "n_iter_no_change": 10, "tol": 1e-7,
            "random_state": 3100000, "class_weight": None,
        }
        rf_params = {
            "n_estimators": 100, "criterion": "gini", "max_depth": None,
            "min_samples_split": 2, "min_samples_leaf": 1, "max_features": "sqrt",
            "bootstrap": True, "class_weight": None, "random_state": 3100000, "n_jobs": 1,
        }
        hgb_sig = inspect.signature(HistGradientBoostingClassifier)
        rf_sig = inspect.signature(RandomForestClassifier)
        hgb_supported = all(k in hgb_sig.parameters for k in hgb_params)
        rf_supported = all(k in rf_sig.parameters for k in rf_params)
        checks.append({"name": "learner_api_support", "status": "PASS" if hgb_supported and rf_supported else "FAIL", "numpy": np.__version__, "sklearn": sklearn.__version__})
        try:
            HistGradientBoostingClassifier(**hgb_params)
            RandomForestClassifier(**rf_params)
            checks.append({"name": "exact_learner_configuration_instantiates", "status": "PASS"})
        except TypeError as e:
            checks.append({"name": "exact_learner_configuration_instantiates", "status": "FAIL", "error": str(e)})
    except Exception as e:
        checks.append({"name": "learner_environment", "status": "FAIL", "error": f"{type(e).__name__}: {e}"})

    source = LEARNER.read_text(encoding="utf-8") if LEARNER.is_file() else ""
    forbidden = [
        "0.07942359585000518", "30485713", "10225328", "requests", "urllib", "httpx", "socket",
        "train_trajectories", "test_trajectories", "trajectory", "terminal_reason",
    ]
    found = [x for x in forbidden if x in source]
    checks.append({"name": "historical_network_trajectory_firewall", "status": "PASS" if not found else "FAIL", "forbidden_tokens_found": found})

    import_count = len(re.findall(r"(?:^|\n)\s*[^#\n]*\.fit\(", source))
    checks.append({"name": "no_fit_at_import", "status": "PASS" if import_count == 0 else "FAIL", "fit_calls_in_source": import_count})

    # This is deliberately a blocking preflight item: N-R6.1 did not fully freeze
    # the permuted-marginals control procedure. Do not invent it here.
    checks.append({"name": "permuted_marginals_control_fully_frozen", "status": "BLOCKED", "reason": "N-R6.1 specifies the control concept but not its exact permutation procedure and seed."})

    checks.append({"name": "scientific_execution", "status": "NOT_PERFORMED"})
    checks.append({"name": "learner_execution", "status": "NOT_PERFORMED"})
    checks.append({"name": "confirmatory_inference", "status": "NOT_PERFORMED"})

    blocking = [c["name"] for c in checks if c["status"] in {"FAIL", "BLOCKED"}]
    status = "BLOCKED" if blocking else "PASS"
    print(json.dumps({
        "runner": "N_R7_PREFLIGHT_RUNNER_v0.1",
        "checks": checks,
        "blocking_checks": blocking,
        "scientific_execution": "NOT_PERFORMED",
        "learner_execution": "NOT_PERFORMED",
        "confirmatory_inference": "NOT_PERFORMED",
        "status": status,
        "python": sys.version,
    }, indent=2))
    raise SystemExit(2 if blocking else 0)


if __name__ == "__main__":
    main()
