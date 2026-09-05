"""N-R7 scientific execution runner v0.1.

First controlled Branch N learner execution. This runner is deliberately
strict: it verifies frozen inputs, joins labels only from the frozen N-R4B.4
outcome corpus, fits only registered learners, and writes deterministic
machine-readable outputs. It does not use historical EMP-1.1 results.

Run from repository root. Scientific execution is local-only; this file does
not access the network.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EXP = ROOT / "03_EXPERIMENTS" / "EMP-1.1"
SRC = EXP / "src"
PRED = EXP / "artifacts" / "N-R5.3_PREDICTOR_DATASET"
CORP = EXP / "artifacts" / "N-R4B.4_CONTROLLED_CORPUS"
OUT = EXP / "artifacts" / "N-R7_SCIENTIFIC_EXECUTION"

TRAIN_PRED = PRED / "train_predictors.jsonl"
TEST_PRED = PRED / "test_predictors.jsonl"
TRAIN_TRAJ = CORP / "train_trajectories.jsonl"
TEST_TRAJ = CORP / "test_trajectories.jsonl"

EXPECTED = {
    "train_predictors_sha256": "d40e3d5f5bd8839d5c83efb1fa2a2d33f432c65c47f568516152dce578f991bd",
    "test_predictors_sha256": "8ae5d84ef0bd1dc50835b1b006e20f299437f2a49395b31e057c0f016d1d3b35",
    "train_count": 30000,
    "test_count": 10000,
    "B_DIM": 16,
    "R_DIM": 58,
    "BR_DIM": 74,
    "train_seed": 3100000,
    "test_seed": 4100000,
    "trajectory_seed_base": {"train": 3100000, "test": 4100000},
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"MODULE_LOAD_FAILED:{path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def read_jsonl(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def canonical_json(obj) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("ascii")


def verify_predictors(rows: list[dict], expected_count: int, expected_b: int, expected_r: int, expected_br: int):
    if len(rows) != expected_count:
        raise RuntimeError(f"PREDICTOR_COUNT_MISMATCH:{len(rows)}:{expected_count}")
    ids = [r["episode_id"] for r in rows]
    if ids != list(range(expected_count)):
        raise RuntimeError("PREDICTOR_EPISODE_ORDER_MISMATCH")
    required = {"episode_id", "initial_snapshot_sha256", "B", "R", "BR"}
    for r in rows:
        if set(r) != required:
            raise RuntimeError("PREDICTOR_SCHEMA_MISMATCH")
        if len(r["B"]) != expected_b or len(r["R"]) != expected_r or len(r["BR"]) != expected_br:
            raise RuntimeError("PREDICTOR_DIMENSION_MISMATCH")
        if r["BR"] != r["B"] + r["R"]:
            raise RuntimeError("BR_CONCATENATION_MISMATCH")


def load_labels(path: Path, expected_count: int, split: str) -> dict[tuple[int, str], int]:
    rows = read_jsonl(path)
    if len(rows) != expected_count:
        raise RuntimeError(f"OUTCOME_COUNT_MISMATCH:{split}:{len(rows)}:{expected_count}")
    labels: dict[tuple[int, str], int] = {}
    for r in rows:
        key = (int(r["episode_id"]), str(r["initial_snapshot_sha256"]))
        if key in labels:
            raise RuntimeError(f"DUPLICATE_LABEL_KEY:{split}:{key}")
        y = int(r["outcome"])
        if y not in (0, 1):
            raise RuntimeError(f"NON_BINARY_OUTCOME:{split}:{key}")
        labels[key] = y
    return labels


def join_labels(pred_rows: list[dict], labels: dict[tuple[int, str], int], split: str):
    y = []
    for r in pred_rows:
        key = (int(r["episode_id"]), str(r["initial_snapshot_sha256"]))
        if key not in labels:
            raise RuntimeError(f"MISSING_LABEL:{split}:{key}")
        y.append(labels[key])
    if len(y) != len(pred_rows):
        raise RuntimeError(f"JOIN_COUNT_MISMATCH:{split}")
    return y


def matrix(rows: list[dict], field: str):
    import numpy as np
    return np.asarray([r[field] for r in rows], dtype=float)


def save_json(path: Path, obj: dict):
    path.write_bytes(canonical_json(obj))


def save_jsonl(path: Path, rows: list[dict]):
    with path.open("wb") as f:
        for row in rows:
            f.write(canonical_json(row))


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)

    # Load the registered learner only after frozen input checks are possible.
    learner = load_module("branch_n_r6_learner_v01", SRC / "branch_n_r6_learner_v01.py")
    import numpy as np

    input_hashes = {
        "train_predictors": sha256_file(TRAIN_PRED),
        "test_predictors": sha256_file(TEST_PRED),
        "train_trajectories": sha256_file(TRAIN_TRAJ),
        "test_trajectories": sha256_file(TEST_TRAJ),
    }
    if input_hashes["train_predictors"] != EXPECTED["train_predictors_sha256"]:
        raise RuntimeError("FROZEN_TRAIN_PREDICTOR_HASH_MISMATCH")
    if input_hashes["test_predictors"] != EXPECTED["test_predictors_sha256"]:
        raise RuntimeError("FROZEN_TEST_PREDICTOR_HASH_MISMATCH")

    train = read_jsonl(TRAIN_PRED)
    test = read_jsonl(TEST_PRED)
    verify_predictors(train, EXPECTED["train_count"], 16, 58, 74)
    verify_predictors(test, EXPECTED["test_count"], 16, 58, 74)

    train_labels = load_labels(TRAIN_TRAJ, EXPECTED["train_count"], "train")
    test_labels = load_labels(TEST_TRAJ, EXPECTED["test_count"], "test")
    y_train = np.asarray(join_labels(train, train_labels, "train"), dtype=int)
    y_test = np.asarray(join_labels(test, test_labels, "test"), dtype=int)

    xb_train = matrix(train, "B")
    xbr_train = matrix(train, "BR")
    xb_test = matrix(test, "B")
    xbr_test = matrix(test, "BR")
    xr_train = matrix(train, "R")

    # Primary B vs B+R.
    model_b = learner.fit_primary(xb_train, y_train)
    model_br = learner.fit_primary(xbr_train, y_train)
    primary = learner.evaluate_pair(model_b, model_br, xb_test, xbr_test, y_test)

    # Count-only R control: six frozen R2 cardinality columns, first six R1,
    # followed by six R2 columns in the registered family order.
    xr_count_train = xr_train[:, 6:12]
    xr_count_test = matrix(test, "R")[:, 6:12]
    model_count = learner.fit_primary(xb_train, y_train)
    model_b_count = learner.fit_primary(np.concatenate([xb_train, xr_count_train], axis=1), y_train)
    count_control = learner.evaluate_pair(
        model_count, model_b_count, xb_test,
        np.concatenate([xb_test, xr_count_test], axis=1), y_test
    )

    # Per-column training-R permutation control, exactly as frozen in N-R6.1.
    rng = np.random.default_rng(24681357)
    xr_perm_train = xr_train.copy()
    for j in range(xr_perm_train.shape[1]):
        rng.shuffle(xr_perm_train[:, j])
    model_perm = learner.fit_primary(np.concatenate([xb_train, xr_perm_train], axis=1), y_train)
    permuted = learner.evaluate_pair(
        model_b, model_perm, xb_test,
        xbr_test, y_test
    )

    # RandomForest alternative, B vs B+R.
    rf_b = learner.make_random_forest()
    rf_br = learner.make_random_forest()
    rf_b.fit(xb_train, y_train)
    rf_br.fit(xbr_train, y_train)
    rf = learner.evaluate_pair(rf_b, rf_br, xb_test, xbr_test, y_test)

    # Per-episode predictions/losses for the primary pair.
    pb = model_b.predict_proba(xb_test)[:, 1]
    pbr = model_br.predict_proba(xbr_test)[:, 1]
    lb = -np.log(np.clip(np.where(y_test == 1, pb, 1.0 - pb), 1e-15, 1.0))
    lbr = -np.log(np.clip(np.where(y_test == 1, pbr, 1.0 - pbr), 1e-15, 1.0))
    pred_rows = []
    for r, y, p0, p1, l0, l1 in zip(test, y_test, pb, pbr, lb, lbr):
        pred_rows.append({
            "episode_id": int(r["episode_id"]),
            "initial_snapshot_sha256": r["initial_snapshot_sha256"],
            "y": int(y),
            "p_B": float(p0),
            "p_BR": float(p1),
            "logloss_B": float(l0),
            "logloss_BR": float(l1),
            "delta_logloss": float(l0 - l1),
        })
    save_jsonl(OUT / "primary_test_predictions.jsonl", pred_rows)
    save_json(OUT / "primary_results.json", primary)
    save_json(OUT / "control_count_only_results.json", count_control)
    save_json(OUT / "control_permuted_marginals_results.json", permuted)
    save_json(OUT / "control_random_forest_results.json", rf)

    prov = {
        "artifact": "N-R7_SCIENTIFIC_EXECUTION",
        "status": "FIRST_EXECUTION",
        "historical_recovery": False,
        "historical_result_used_as_tuning_target": False,
        "train_count": len(train),
        "test_count": len(test),
        "input_hashes": input_hashes,
        "learner_module_sha256": sha256_file(SRC / "branch_n_r6_learner_v01.py"),
        "python": sys.version,
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "numpy": np.__version__,
        "scikit_learn": learner.HGB_PARAMS and __import__("sklearn").__version__,
        "hgb_params": dict(learner.HGB_PARAMS),
        "rf_params": dict(learner.RF_PARAMS),
        "signflip_permutations": learner.PERMUTATIONS,
        "signflip_seed": learner.PERMUTATION_SEED,
        "permuted_marginals_seed": 24681357,
        "permuted_marginals_procedure": "training_R_only; independently shuffle each of 58 columns; B unchanged",
        "label_join_key": "episode_id + initial_snapshot_sha256",
        "label_source_hashes": {"train_trajectories": input_hashes["train_trajectories"], "test_trajectories": input_hashes["test_trajectories"]},
        "execution_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "scientific_execution": True,
        "independent_repeat": False,
    }
    save_json(OUT / "PROVENANCE.json", prov)

    manifest = {
        "status": "PASS_FIRST_EXECUTION",
        "primary": primary,
        "controls": {
            "count_only": count_control,
            "permuted_marginals": permuted,
            "random_forest": rf,
        },
        "prediction_sha256": sha256_file(OUT / "primary_test_predictions.jsonl"),
        "provenance_sha256": sha256_file(OUT / "PROVENANCE.json"),
    }
    save_json(OUT / "EXECUTION_MANIFEST.json", manifest)
    print(json.dumps(manifest, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
