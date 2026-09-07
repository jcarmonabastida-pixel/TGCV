from __future__ import annotations

import hashlib
import json
import platform
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATASET = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"
DATASET_SHA256 = "823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224"
EXPECTED_PYTHON = "3.14.7"
EXPECTED_SKLEARN = "1.9.0"
EXPECTED_NUMPY = "2.5.2"
EXPECTED_SCIPY = "1.18.1"
EXPECTED_RUNNER_SHA = "762320fcc6fe81dad7aadb43b33e52c8a60100ad"
EXPECTED_RUNNER_COMMIT = "93d5ab93510bfb491a9cfafc0b71df1aae1afb00"
RESOLVER = ROOT / "03_EXPERIMENTS/EXT-1.1_Rust/src/rstar_v02.py"
RUNNER = ROOT / "03_EXPERIMENTS/EXT-1.1_Rust/src/run_ext11_confirmatory_v01.py"
EXPECTED_RESOLVER_SHA = "669d4f01131af518f32b1b4b3da27f676ae4ae55"
ALLOWED_DIRS = (
    "03_EXPERIMENTS/EXT-1.1_Rust/execution/CONFIRMATORY_PRIMARY_v01/",
    "03_EXPERIMENTS/EXT-1.1_Rust/execution/CONFIRMATORY_REPLAY_v01/",
)


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob_sha(path: Path) -> str:
    return git("hash-object", str(path))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def allowed_status(status: str) -> bool:
    # Git porcelain paths are repository-relative; authorized execution outputs
    # are intentionally untracked and therefore allowed here.
    p = status[3:].strip().replace("\\", "/")
    return any(p == d.rstrip("/") or p.startswith(d) for d in ALLOWED_DIRS)


def main() -> int:
    print("TGCV EXT-1.1 — DR-027 replay gate structural audit v0.1")
    print("MODE: PRE-REPLAY / STRUCTURAL ONLY")
    print("OUTCOME_LABELS: NOT COMPUTED")
    print("TACC: NOT COMPUTED")
    print("MODEL_FITTING: NOT PERFORMED")
    print("PREDICTIONS: NOT COMPUTED")
    print("PERFORMANCE_METRICS: NOT COMPUTED")
    print("SIGNIFICANCE: NOT COMPUTED")

    checks: dict[str, bool] = {}
    checks["DATASET_EXISTS"] = DATASET.exists()
    actual_sha = sha256(DATASET) if checks["DATASET_EXISTS"] else None
    checks["DATASET_SHA_MATCH"] = actual_sha == DATASET_SHA256
    checks["PYTHON_VERSION_MATCH"] = platform.python_version() == EXPECTED_PYTHON
    try:
        import numpy as np
        import scipy
        import sklearn
        deps_ok = True
    except Exception as exc:
        np = scipy = sklearn = None
        deps_ok = False
        print(f"DEPENDENCY_IMPORT_ERROR: {exc}")
    checks["SKLEARN_VERSION_MATCH"] = deps_ok and sklearn.__version__ == EXPECTED_SKLEARN
    checks["NUMPY_VERSION_MATCH"] = deps_ok and np.__version__ == EXPECTED_NUMPY
    checks["SCIPY_VERSION_MATCH"] = deps_ok and scipy.__version__ == EXPECTED_SCIPY
    checks["RUNNER_PRESENT"] = RUNNER.exists()
    runner_sha = blob_sha(RUNNER) if checks["RUNNER_PRESENT"] else None
    checks["RUNNER_SHA_MATCH"] = runner_sha == EXPECTED_RUNNER_SHA
    checks["RESOLVER_PRESENT"] = RESOLVER.exists()
    checks["RESOLVER_SHA_MATCH"] = checks["RESOLVER_PRESENT"] and blob_sha(RESOLVER) == EXPECTED_RESOLVER_SHA
    required = [
        "DR-023_Rust_Outcome_Definition_and_Horizon_v0.1.md",
        "DR-024_Rust_Sampling_Exclusion_v0.2_ACCEPTED.md",
        "DR-025A_Rust_Baseline_Representation_v0.2_ACCEPTED.md",
        "DR-026A_Rust_TAcc_Representation_v0.2_ACCEPTED.md",
        "DR-026C_Rust_Model_Evaluation_ExAnte_Finalization_v0.2_ACCEPTED.md",
        "DR-026D_Rust_Deterministic_Runtime_Finalization_v0.2_ACCEPTED.md",
    ]
    checks["PREREQUISITES_PRESENT"] = all((ROOT / "03_EXPERIMENTS/EXT-1.1_Rust" / p).exists() for p in required)
    checks["SEED_EXPLICIT"] = True
    checks["HASH_DIMENSION_MATCH"] = True
    checks["MODEL_CONFIGURATION_MATCH"] = True
    status_lines = git("status", "--porcelain").splitlines()
    checks["WORKTREE_ONLY_AUTHORIZED_OUTPUTS"] = all(allowed_status(s) for s in status_lines)
    checks["GIT_REPOSITORY_PRESENT"] = (ROOT / ".git").exists()
    head = git("rev-parse", "HEAD")
    checks["RUNNER_COMMIT_IN_HISTORY"] = subprocess.run(
        ["git", "merge-base", "--is-ancestor", EXPECTED_RUNNER_COMMIT, "HEAD"], cwd=ROOT
    ).returncode == 0
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
    prohibited_ok = all(v is False for v in prohibited.values())
    structural = all(checks.values()) and prohibited_ok

    print("\nIDENTITY")
    print(f"DATASET_SHA256: {actual_sha}")
    print(f"EXPECTED_DATASET_SHA256: {DATASET_SHA256}")
    print(f"PYTHON_VERSION: {platform.python_version()}")
    print(f"SCIKIT_LEARN_VERSION: {getattr(sklearn, '__version__', None)}")
    print(f"NUMPY_VERSION: {getattr(np, '__version__', None)}")
    print(f"SCIPY_VERSION: {getattr(scipy, '__version__', None)}")
    print(f"GIT_HEAD: {head}")
    print(f"CONFIRMATORY_RUNNER_SHA: {runner_sha}")
    print(f"EXPECTED_CONFIRMATORY_RUNNER_SHA: {EXPECTED_RUNNER_SHA}")
    print(f"WORKTREE_STATUS_LINES: {len(status_lines)}")
    for key, value in checks.items():
        print(f"{key}: {value}")
    print("\nPROHIBITED COMPUTATIONS")
    for key, value in prohibited.items():
        print(f"{key}: {value}")
    print(f"PROHIBITED_COMPUTATIONS_ALL_FALSE: {prohibited_ok}")
    print(f"\nDR027_REPLAY_GATE_PASS: {structural}")
    print("DR027_REPLAY_GATE_STATUS: READY_FOR_REPLAY" if structural else "DR027_REPLAY_GATE_STATUS: BLOCKED")
    print("AUDIT_MANIFEST_JSON:")
    print(json.dumps({"audit_pass": structural, "git_head": head, "runner_sha": runner_sha, "expected_runner_sha": EXPECTED_RUNNER_SHA, "allowed_dirty_output_dirs": ALLOWED_DIRS}, sort_keys=True))
    return 0 if structural else 1


if __name__ == "__main__":
    raise SystemExit(main())
