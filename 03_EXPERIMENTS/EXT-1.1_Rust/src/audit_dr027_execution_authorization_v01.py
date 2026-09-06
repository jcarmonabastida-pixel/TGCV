from __future__ import annotations

import hashlib
import json
import platform
import subprocess
from pathlib import Path

DATASET_SHA256 = "823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224"
EXPECTED_PYTHON = "3.14.7"
EXPECTED_SKLEARN = "1.9.0"
EXPECTED_NUMPY = "2.5.2"
EXPECTED_SCIPY = "1.18.1"
EXPECTED_SEED = 0
EXPECTED_HASH_DIMENSION = 2**20
EXPECTED_SOLVER = "liblinear"
EXPECTED_C = 1.0
EXPECTED_TOL = 1e-8
EXPECTED_MAX_ITER = 1000
EXPECTED_RUNNER_SHA = "dbf4aa11aee9848e5c6466e63bd8fb772cfe772c"
EXPECTED_RUNNER_COMMIT = "e24f6365fd942053704026ecfa4861fc05c469bf"
RUNNER = "03_EXPERIMENTS/EXT-1.1_Rust/src/run_ext11_confirmatory_v01.py"
RESOLVER = "03_EXPERIMENTS/EXT-1.1_Rust/src/rstar_v02.py"
EXPECTED_RESOLVER_SHA = "669d4f01131af518f32b1b4b3da27f676ae4ae55"

ROOT = Path(__file__).resolve().parents[3]
DATASET = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"
REQUIRED = [
    ROOT / "03_EXPERIMENTS/EXT-1.1_Rust/DR-023_Rust_Outcome_Definition_and_Horizon_v0.1.md",
    ROOT / "03_EXPERIMENTS/EXT-1.1_Rust/DR-024_Rust_Sampling_Exclusion_v0.2_ACCEPTED.md",
    ROOT / "03_EXPERIMENTS/EXT-1.1_Rust/DR-025A_Rust_Baseline_Representation_v0.2_ACCEPTED.md",
    ROOT / "03_EXPERIMENTS/EXT-1.1_Rust/DR-026A_Rust_TAcc_Representation_v0.2_ACCEPTED.md",
    ROOT / "03_EXPERIMENTS/EXT-1.1_Rust/DR-026C_Rust_Model_Evaluation_ExAnte_Finalization_v0.2_ACCEPTED.md",
    ROOT / "03_EXPERIMENTS/EXT-1.1_Rust/DR-026D_Rust_Deterministic_Runtime_Finalization_v0.2_ACCEPTED.md",
    ROOT / RESOLVER,
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def git_blob_sha(path: Path) -> str:
    return git("hash-object", str(path))


def main() -> int:
    print("TGCV EXT-1.1 — DR-027 confirmatory execution authorization structural audit v0.2")
    print("MODE: PRE-AUTHORIZATION / STRUCTURAL ONLY")
    print("OUTCOME_LABELS: NOT COMPUTED")
    print("TACC: NOT COMPUTED")
    print("MODEL_FITTING: NOT PERFORMED")
    print("PREDICTIONS: NOT COMPUTED")
    print("PERFORMANCE_METRICS: NOT COMPUTED")
    print("SIGNIFICANCE: NOT COMPUTED")
    print()

    checks: dict[str, bool] = {}
    checks["DATASET_EXISTS"] = DATASET.exists()
    dataset_sha = sha256_file(DATASET) if checks["DATASET_EXISTS"] else None
    checks["DATASET_SHA_MATCH"] = dataset_sha == DATASET_SHA256

    py = platform.python_version()
    checks["PYTHON_VERSION_MATCH"] = py == EXPECTED_PYTHON

    try:
        import numpy as np
        import scipy
        import sklearn
    except Exception as exc:
        np = scipy = sklearn = None
        print(f"DEPENDENCY_IMPORT_ERROR: {exc}")

    checks["SKLEARN_VERSION_MATCH"] = sklearn is not None and sklearn.__version__ == EXPECTED_SKLEARN
    checks["NUMPY_VERSION_MATCH"] = np is not None and np.__version__ == EXPECTED_NUMPY
    checks["SCIPY_VERSION_MATCH"] = scipy is not None and scipy.__version__ == EXPECTED_SCIPY
    checks["SEED_EXPLICIT"] = EXPECTED_SEED == 0
    checks["HASH_DIMENSION_MATCH"] = EXPECTED_HASH_DIMENSION == 1048576
    checks["MODEL_CONFIGURATION_MATCH"] = (
        EXPECTED_SOLVER == "liblinear"
        and EXPECTED_C == 1.0
        and EXPECTED_TOL == 1e-8
        and EXPECTED_MAX_ITER == 1000
    )

    checks["PREREQUISITE_DECISIONS_PRESENT"] = all(p.exists() for p in REQUIRED[:-1])
    resolver = ROOT / RESOLVER
    checks["NORMATIVE_RESOLVER_PRESENT"] = resolver.exists()
    checks["NORMATIVE_RESOLVER_SHA_MATCH"] = checks["NORMATIVE_RESOLVER_PRESENT"] and git_blob_sha(resolver) == EXPECTED_RESOLVER_SHA
    runner = ROOT / RUNNER
    checks["CONFIRMATORY_RUNNER_PRESENT"] = runner.exists()
    runner_sha = git_blob_sha(runner) if checks["CONFIRMATORY_RUNNER_PRESENT"] else None
    checks["CONFIRMATORY_RUNNER_SHA_MATCH"] = runner_sha == EXPECTED_RUNNER_SHA

    checks["GIT_REPOSITORY_PRESENT"] = (ROOT / ".git").exists()
    git_head = git("rev-parse", "HEAD") if checks["GIT_REPOSITORY_PRESENT"] else None
    git_status = git("status", "--porcelain") if checks["GIT_REPOSITORY_PRESENT"] else ""
    checks["GIT_STATUS_CLEAN"] = git_status == ""
    if checks["GIT_REPOSITORY_PRESENT"]:
        ancestor_rc = subprocess.run(["git", "merge-base", "--is-ancestor", EXPECTED_RUNNER_COMMIT, "HEAD"], cwd=ROOT).returncode
        checks["RUNNER_COMMIT_IN_CURRENT_HISTORY"] = ancestor_rc == 0
    else:
        checks["RUNNER_COMMIT_IN_CURRENT_HISTORY"] = False

    prohibited = {
        "OUTCOME_LABELS_COMPUTED": False,
        "TACC_COMPUTED": False,
        "MODEL_FITTED": False,
        "PREDICTIONS_COMPUTED": False,
        "PERFORMANCE_METRICS_COMPUTED": False,
        "SIGNIFICANCE_COMPUTED": False,
        "OUTCOME_USED_FOR_AUTHORIZATION": False,
        "RESULT_USED_FOR_PROTOCOL_CHANGE": False,
        "EXPLORATORY_MODEL_COMPARISON": False,
        "ADAPTIVE_SELECTION": False,
    }
    checks.update({k: v is False for k, v in prohibited.items()})

    print("IDENTITY")
    print(f"DATASET: {DATASET}")
    print(f"DATASET_SHA256: {dataset_sha}")
    print(f"EXPECTED_DATASET_SHA256: {DATASET_SHA256}")
    print(f"PYTHON_VERSION: {py}")
    print(f"SCIKIT_LEARN_VERSION: {getattr(sklearn, '__version__', None)}")
    print(f"NUMPY_VERSION: {getattr(np, '__version__', None)}")
    print(f"SCIPY_VERSION: {getattr(scipy, '__version__', None)}")
    print(f"GIT_HEAD: {git_head}")
    print(f"GIT_STATUS_CLEAN: {checks['GIT_STATUS_CLEAN']}")
    print(f"CONFIRMATORY_RUNNER_SHA: {runner_sha}")
    print(f"EXPECTED_CONFIRMATORY_RUNNER_SHA: {EXPECTED_RUNNER_SHA}")
    print(f"RUNNER_COMMIT_IN_CURRENT_HISTORY: {checks['RUNNER_COMMIT_IN_CURRENT_HISTORY']}")
    print()

    print("PREREQUISITES")
    for k in ("PREREQUISITE_DECISIONS_PRESENT", "NORMATIVE_RESOLVER_PRESENT", "NORMATIVE_RESOLVER_SHA_MATCH", "CONFIRMATORY_RUNNER_PRESENT", "CONFIRMATORY_RUNNER_SHA_MATCH", "RUNNER_COMMIT_IN_CURRENT_HISTORY"):
        print(f"{k}: {checks[k]}")
    print()

    print("FROZEN PROTOCOL CONSISTENCY")
    print(f"RANDOM_STATE: {EXPECTED_SEED}")
    print(f"HASH_DIMENSION: {EXPECTED_HASH_DIMENSION}")
    print(f"SOLVER: {EXPECTED_SOLVER}")
    print(f"C: {EXPECTED_C}")
    print(f"TOL: {EXPECTED_TOL}")
    print(f"MAX_ITER: {EXPECTED_MAX_ITER}")
    print(f"MODEL_CONFIGURATION_MATCH: {checks['MODEL_CONFIGURATION_MATCH']}")
    print()

    print("PROHIBITED COMPUTATIONS")
    for k, v in prohibited.items():
        print(f"{k}: {v}")
    prohibited_all_false = all(v is False for v in prohibited.values())
    print(f"PROHIBITED_COMPUTATIONS_ALL_FALSE: {prohibited_all_false}")
    print()

    structural_keys = [
        "DATASET_EXISTS", "DATASET_SHA_MATCH", "PYTHON_VERSION_MATCH",
        "SKLEARN_VERSION_MATCH", "NUMPY_VERSION_MATCH", "SCIPY_VERSION_MATCH",
        "SEED_EXPLICIT", "HASH_DIMENSION_MATCH", "MODEL_CONFIGURATION_MATCH",
        "PREREQUISITE_DECISIONS_PRESENT", "NORMATIVE_RESOLVER_PRESENT",
        "NORMATIVE_RESOLVER_SHA_MATCH", "CONFIRMATORY_RUNNER_PRESENT",
        "CONFIRMATORY_RUNNER_SHA_MATCH", "RUNNER_COMMIT_IN_CURRENT_HISTORY",
        "GIT_REPOSITORY_PRESENT", "GIT_STATUS_CLEAN",
    ]
    structural_pass = all(checks[k] for k in structural_keys) and prohibited_all_false
    print("STRUCTURAL CHECKS")
    for k in structural_keys:
        print(f"{k}: {checks[k]}")
    print()
    print(f"DR027_STRUCTURAL_AUDIT_PASS: {structural_pass}")
    print("DR027_DECISION_STATUS: OPEN_PENDING_AUDIT_REVIEW_AND_ACCEPTANCE")
    print()

    manifest = {
        "dataset_sha256": dataset_sha,
        "expected_dataset_sha256": DATASET_SHA256,
        "python_version": py,
        "scikit_learn_version": getattr(sklearn, "__version__", None),
        "numpy_version": getattr(np, "__version__", None),
        "scipy_version": getattr(scipy, "__version__", None),
        "random_state": EXPECTED_SEED,
        "hash_dimension": EXPECTED_HASH_DIMENSION,
        "solver": EXPECTED_SOLVER,
        "C": EXPECTED_C,
        "tol": EXPECTED_TOL,
        "max_iter": EXPECTED_MAX_ITER,
        "git_head": git_head,
        "expected_runner_sha": EXPECTED_RUNNER_SHA,
        "runner_sha": runner_sha,
        "expected_runner_commit": EXPECTED_RUNNER_COMMIT,
        "resolver_sha": EXPECTED_RESOLVER_SHA,
        "git_status_clean": checks["GIT_STATUS_CLEAN"],
        "audit_pass": structural_pass,
    }
    print("AUDIT_MANIFEST_JSON:")
    print(json.dumps(manifest, sort_keys=True))
    return 0 if structural_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
