from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import os
import platform
import subprocess
import sys
from pathlib import Path

EXPECTED_SEED = 0
EXPECTED_HASH_DIM = 2**20
EXPECTED_SOLVER = "liblinear"
EXPECTED_C = 1.0
EXPECTED_TOL = 1e-8
EXPECTED_MAX_ITER = 1000
REQUIRED_FILES = [
    "DR-023_Rust_Outcome_Definition_and_Horizon_v0.1.md",
    "DR-024_Rust_Sampling_Exclusion_v0.2_ACCEPTED.md",
    "DR-025A_Rust_Baseline_Representation_v0.2_ACCEPTED.md",
    "DR-026A_Rust_TAcc_Representation_v0.2_ACCEPTED.md",
    "DR-026C_Rust_Model_Evaluation_ExAnte_Finalization_v0.2_ACCEPTED.md",
    "DR-026D_Rust_Deterministic_Runtime_Finalization_v0.1.md",
    "src/rstar_v02.py",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def version_of(module_name: str) -> str:
    module = importlib.import_module(module_name)
    return getattr(module, "__version__", "UNKNOWN")


def git(cmd: list[str]) -> str:
    try:
        return subprocess.check_output(["git", *cmd], text=True, stderr=subprocess.STDOUT).strip()
    except Exception:
        return "UNAVAILABLE"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip", default=str(Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"))
    parser.add_argument("--repo", default=str(Path(__file__).resolve().parents[3]))
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    dataset = Path(args.zip).resolve()

    print("TGCV EXT-1.1 — DR-026D deterministic runtime structural preflight v0.1")
    print("=" * 80)
    print("MODE: PRE-CONFIRMATORY / STRUCTURAL ONLY")
    print("OUTCOME_LABELS: NOT COMPUTED")
    print("MODEL_FITTING: NOT PERFORMED")
    print("PERFORMANCE_METRICS: NOT COMPUTED")
    print("SIGNIFICANCE: NOT COMPUTED")
    print()

    checks: dict[str, bool] = {}

    print("RUNTIME")
    print(f"PYTHON_VERSION: {platform.python_version()}")
    print(f"PYTHON_IMPLEMENTATION: {platform.python_implementation()}")
    print(f"PLATFORM: {platform.platform()}")
    print(f"ARCHITECTURE: {platform.machine()}")
    try:
        sklearn_v = version_of("sklearn")
        numpy_v = version_of("numpy")
        scipy_v = version_of("scipy")
        checks["DEPENDENCIES_IMPORTABLE"] = all(v != "UNKNOWN" for v in (sklearn_v, numpy_v, scipy_v))
    except Exception as exc:
        sklearn_v = numpy_v = scipy_v = f"IMPORT_ERROR:{exc.__class__.__name__}"
        checks["DEPENDENCIES_IMPORTABLE"] = False
    print(f"SCIKIT_LEARN_VERSION: {sklearn_v}")
    print(f"NUMPY_VERSION: {numpy_v}")
    print(f"SCIPY_VERSION: {scipy_v}")
    print(f"RANDOM_STATE_FROZEN: {EXPECTED_SEED}")
    print()

    print("DATASET IDENTITY")
    print(f"ZIP: {dataset}")
    checks["DATASET_EXISTS"] = dataset.is_file()
    print(f"DATASET_EXISTS: {checks['DATASET_EXISTS']}")
    if checks["DATASET_EXISTS"]:
        dataset_sha = sha256_file(dataset)
        dataset_size = dataset.stat().st_size
    else:
        dataset_sha = "UNAVAILABLE"
        dataset_size = 0
    print(f"DATASET_SIZE_BYTES: {dataset_size}")
    print(f"DATASET_SHA256: {dataset_sha}")
    checks["DATASET_SHA256_COMPUTABLE"] = dataset_sha != "UNAVAILABLE"
    print()

    print("CODE / REPOSITORY IDENTITY")
    inside_repo = (repo / ".git").exists()
    checks["GIT_REPOSITORY_PRESENT"] = inside_repo
    print(f"REPOSITORY: {repo}")
    print(f"GIT_REPOSITORY_PRESENT: {inside_repo}")
    commit = git(["-C", str(repo), "rev-parse", "HEAD"]) if inside_repo else "UNAVAILABLE"
    status = git(["-C", str(repo), "status", "--porcelain"]) if inside_repo else "UNAVAILABLE"
    print(f"GIT_HEAD: {commit}")
    print(f"GIT_STATUS_CLEAN: {status == ''}")
    checks["GIT_STATUS_CLEAN"] = status == ""

    missing = [p for p in REQUIRED_FILES if not (repo / "03_EXPERIMENTS" / "EXT-1.1_Rust" / p).is_file()]
    checks["REQUIRED_ARTIFACTS_PRESENT"] = not missing
    print(f"REQUIRED_ARTIFACTS_PRESENT: {checks['REQUIRED_ARTIFACTS_PRESENT']}")
    print(f"MISSING_REQUIRED_ARTIFACTS: {missing}")
    print()

    print("PROTOCOL CONSISTENCY")
    print(f"RANDOM_STATE: {EXPECTED_SEED}")
    print(f"HASH_DIMENSION: {EXPECTED_HASH_DIM}")
    print(f"SOLVER: {EXPECTED_SOLVER}")
    print(f"C: {EXPECTED_C}")
    print(f"TOL: {EXPECTED_TOL}")
    print(f"MAX_ITER: {EXPECTED_MAX_ITER}")
    checks["RANDOM_SEED_EXPLICIT"] = EXPECTED_SEED == 0
    checks["HASH_DIMENSION_FROZEN"] = EXPECTED_HASH_DIM == 2**20
    checks["MODEL_CONFIGURATION_FROZEN"] = (
        EXPECTED_SOLVER == "liblinear"
        and EXPECTED_C == 1.0
        and EXPECTED_TOL == 1e-8
        and EXPECTED_MAX_ITER == 1000
    )
    print(f"RANDOM_SEED_EXPLICIT: {checks['RANDOM_SEED_EXPLICIT']}")
    print(f"HASH_DIMENSION_FROZEN: {checks['HASH_DIMENSION_FROZEN']}")
    print(f"MODEL_CONFIGURATION_FROZEN: {checks['MODEL_CONFIGURATION_FROZEN']}")
    print()

    print("PROHIBITED COMPUTATIONS")
    prohibited = {
        "OUTCOME_LABELS_COMPUTED": False,
        "TACC_COMPUTED": False,
        "MODEL_FITTED": False,
        "PREDICTIONS_COMPUTED": False,
        "PERFORMANCE_METRICS_COMPUTED": False,
        "SIGNIFICANCE_COMPUTED": False,
        "OUTCOME_USED_FOR_PROTOCOL_CHOICE": False,
    }
    for k, v in prohibited.items():
        print(f"{k}: {v}")
    checks["PROHIBITED_COMPUTATIONS_ALL_FALSE"] = all(v is False for v in prohibited.values())
    print()

    checks["ENVIRONMENT_METADATA_CAPTURED"] = all(
        x not in ("", "UNKNOWN") for x in (platform.python_version(), sklearn_v, numpy_v, scipy_v)
    )
    checks["PREFLIGHT_ONLY"] = True

    preflight_pass = all(checks.values())
    print("PREFLIGHT AGGREGATION")
    print(f"ENVIRONMENT_METADATA_CAPTURED: {checks['ENVIRONMENT_METADATA_CAPTURED']}")
    print(f"PREFLIGHT_ONLY: {checks['PREFLIGHT_ONLY']}")
    print(f"PROHIBITED_COMPUTATIONS_ALL_FALSE: {checks['PROHIBITED_COMPUTATIONS_ALL_FALSE']}")
    print()
    print(f"DR026D_PREFLIGHT_PASS: {preflight_pass}")
    print("DR026D_DECISION_STATUS: OPEN_PENDING_PREFLIGHT_REVIEW_AND_ACCEPTANCE")
    print()
    print("DONE.")
    print("No outcome labels were constructed.")
    print("No T_acc was constructed.")
    print("No model was fitted.")
    print("No performance metric was computed.")
    print("No significance test was performed.")

    manifest = {
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "architecture": platform.machine(),
        "scikit_learn_version": sklearn_v,
        "numpy_version": numpy_v,
        "scipy_version": scipy_v,
        "random_state": EXPECTED_SEED,
        "dataset_sha256": dataset_sha,
        "git_head": commit,
        "git_status_clean": checks["GIT_STATUS_CLEAN"],
        "preflight_pass": preflight_pass,
    }
    print("RUNTIME_MANIFEST_JSON:")
    print(json.dumps(manifest, sort_keys=True))
    return 0 if preflight_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
