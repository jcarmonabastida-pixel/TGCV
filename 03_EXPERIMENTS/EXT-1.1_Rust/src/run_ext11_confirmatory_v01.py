#!/usr/bin/env python3
"""EXT-1.1 Rust confirmatory runner v0.1.

This runner is deliberately parameter-closed: scientific protocol values are
constants frozen by DR-023..DR-026D. The only operational argument is the
execution mode (primary or replay); the dataset path is the frozen path from
DR-026D and cannot be overridden.

The runner performs the confirmatory comparison only after identity/protocol
checks pass. It emits a manifest binding the execution to the exact Git HEAD
and to the frozen normative resolver source SHA recorded below.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import platform
import subprocess
import sys
import zipfile
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ----------------------------- frozen protocol -----------------------------
DATASET = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"
DATASET_SHA256 = "823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224"
DATASET_SIZE = 6047715996
EXPECTED_PYTHON = "3.14.7"
EXPECTED_SKLEARN = "1.9.0"
EXPECTED_NUMPY = "2.5.2"
EXPECTED_SCIPY = "1.18.1"
EXPECTED_OS = "Windows-11-10.0.26200-SP0"
EXPECTED_MACHINE = "AMD64"
RANDOM_STATE = 0
HORIZON_DAYS = 180
HASH_DIM = 2 ** 20
HASH_ALGORITHM = "blake2b-256"
SOLVER = "liblinear"
C = 1.0
MAX_ITER = 1000
TOL = 1e-8
PENALTY = "l2"
FIT_INTERCEPT = True
CLASS_WEIGHT = None

REQUIRED_DECISIONS = {
    "DR-023": "03_EXPERIMENTS/EXT-1.1_Rust/DR-023_Rust_Outcome_Definition_and_Horizon_v0.1.md",
    "DR-024": "03_EXPERIMENTS/EXT-1.1_Rust/DR-024_Rust_Sampling_Exclusion_v0.2_ACCEPTED.md",
    "DR-025A": "03_EXPERIMENTS/EXT-1.1_Rust/DR-025A_Rust_Baseline_Representation_v0.2_ACCEPTED.md",
    "DR-026A": "03_EXPERIMENTS/EXT-1.1_Rust/DR-026A_Rust_TAcc_Representation_v0.2_ACCEPTED.md",
    "DR-026C": "03_EXPERIMENTS/EXT-1.1_Rust/DR-026C_Rust_Model_Evaluation_ExAnte_Finalization_v0.2_ACCEPTED.md",
    "DR-026D": "03_EXPERIMENTS/EXT-1.1_Rust/DR-026D_Rust_Deterministic_Runtime_Finalization_v0.2_ACCEPTED.md",
}
NORMATIVE_RESOLVER = "03_EXPERIMENTS/EXT-1.1_Rust/src/rstar_v02.py"
NORMATIVE_RESOLVER_SHA = "669d4f01131af518f32b1b4b3da27f676ae4ae55"
RUNNER_PATH = "03_EXPERIMENTS/EXT-1.1_Rust/src/run_ext11_confirmatory_v01.py"


def die(msg: str) -> None:
    raise RuntimeError(msg)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def git(args: list[str]) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def repo_root() -> Path:
    return Path(git(["rev-parse", "--show-toplevel"]))


def git_head() -> str:
    return git(["rev-parse", "HEAD"])


def git_clean() -> bool:
    return git(["status", "--porcelain"]) == ""


def git_blob_sha(path: Path) -> str:
    rel = path.relative_to(repo_root()).as_posix()
    return git(["hash-object", str(path)])


def parse_dt(s: str) -> datetime:
    s = s.strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def find_member(zf: zipfile.ZipFile, suffix: str) -> str:
    hits = [n for n in zf.namelist() if n.endswith(suffix)]
    if len(hits) != 1:
        die(f"EXPECTED_ONE_MEMBER:{suffix}:{len(hits)}")
    return hits[0]


def hash_token(token: str) -> tuple[int, int]:
    d = hashlib.blake2b(token.encode("utf-8"), digest_size=32).digest()
    raw = int.from_bytes(d[:8], "big", signed=False)
    idx = raw % HASH_DIM
    sign = 1 if d[8] % 2 == 0 else -1
    return idx, sign


def add_token(row: int, token: str, rows: list[int], cols: list[int], data: list[int]) -> None:
    idx, sign = hash_token(token)
    rows.append(row)
    cols.append(idx)
    data.append(sign)


def version_key(version: str) -> tuple[int, int, int]:
    p = version.split(".")
    if len(p) != 3 or not all(x.isdigit() for x in p):
        die(f"UNSUPPORTED_VERSION_IN_DATASET:{version}")
    return tuple(map(int, p))


def requirement_kind(req: str) -> str:
    req = req.strip()
    import re
    if re.fullmatch(r"=\d+\.\d+\.\d+", req):
        return "EXACT"
    if re.fullmatch(r"\^\d+(?:\.\d+){1,2}", req):
        return "CARET"
    if re.fullmatch(r"\d+\.\d+\.\d+", req):
        return "CARET"
    return "UNSUPPORTED"


def satisfies(version: str, req: str) -> bool:
    import re
    kind = requirement_kind(req)
    if kind == "UNSUPPORTED":
        return False
    v = version_key(version)
    raw = req.strip()
    if kind == "EXACT":
        return v == version_key(raw[1:])
    parts = (raw[1:] if raw.startswith("^") else raw).split(".")
    parts += ["0"] * (3 - len(parts))
    base = tuple(map(int, parts))
    if base[0] > 0:
        upper = (base[0] + 1, 0, 0)
    elif base[1] > 0:
        upper = (0, base[1] + 1, 0)
    else:
        upper = (0, 0, base[2] + 1)
    return base <= v < upper


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("primary", "replay"), required=True)
    args = ap.parse_args()

    root = repo_root()
    if not git_clean():
        die("DIRTY_SCIENTIFIC_WORKTREE")
    if not DATASET.exists():
        die(f"DATASET_NOT_FOUND:{DATASET}")
    if DATASET.stat().st_size != DATASET_SIZE:
        die("DATASET_SIZE_MISMATCH")
    if sha256_file(DATASET) != DATASET_SHA256:
        die("DATASET_SHA256_MISMATCH")

    py = platform.python_version()
    if py != EXPECTED_PYTHON or platform.machine() != EXPECTED_MACHINE:
        die("PYTHON_OR_MACHINE_MISMATCH")
    os_id = f"{platform.system()}-{platform.release()}-{platform.version()}"
    if os_id != EXPECTED_OS:
        die(f"OS_MISMATCH:{os_id}")

    import numpy as np
    import scipy
    import sklearn
    from scipy.sparse import csr_matrix
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import log_loss, brier_score_loss, roc_auc_score
    from sklearn.preprocessing import StandardScaler

    if (sklearn.__version__, np.__version__, scipy.__version__) != (EXPECTED_SKLEARN, EXPECTED_NUMPY, EXPECTED_SCIPY):
        die("PYTHON_PACKAGE_VERSION_MISMATCH")

    for key, rel in REQUIRED_DECISIONS.items():
        p = root / rel
        if not p.exists():
            die(f"MISSING_DECISION:{key}")
    resolver = root / NORMATIVE_RESOLVER
    if not resolver.exists() or git_blob_sha(resolver) != NORMATIVE_RESOLVER_SHA:
        die("NORMATIVE_RESOLVER_SHA_MISMATCH")
    runner = root / RUNNER_PATH
    if not runner.exists():
        die("RUNNER_NOT_FOUND")

    execution_dir = root / "03_EXPERIMENTS" / "EXT-1.1_Rust" / "execution" / ("CONFIRMATORY_PRIMARY_v01" if args.mode == "primary" else "CONFIRMATORY_REPLAY_v01")
    execution_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = execution_dir / "EXECUTION_MANIFEST.json"
    results_path = execution_dir / "RESULTS.json"

    print("TGCV EXT-1.1 Rust — CONFIRMATORY RUNNER v0.1")
    print("MODE:", args.mode)
    print("DATASET_SHA256:", DATASET_SHA256)
    print("GIT_HEAD:", git_head())
    print("PRE-SCIENTIFIC-GATES: PASS")

    # Load retained release metadata.
    with zipfile.ZipFile(DATASET, "r") as zf:
        pv_name = find_member(zf, "package_versions.csv")
        p_name = find_member(zf, "packages.csv")
        d_name = find_member(zf, "package_dependencies.csv")

        versions_by_id: dict[str, tuple[str, str, datetime]] = {}
        versions_by_pkg: dict[str, list[tuple[str, str, datetime]]] = defaultdict(list)
        package_name_by_id: dict[str, str] = {}
        package_rows = 0
        with zf.open(p_name, "r") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""))
            for row in reader:
                package_rows += 1
                package_name_by_id[(row.get("id") or "").strip()] = (row.get("name") or "").strip()

        version_rows = 0
        with zf.open(pv_name, "r") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""))
            for row in reader:
                vid = (row.get("id") or "").strip()
                pid = (row.get("package_id") or "").strip()
                vs = (row.get("version_str") or "").strip()
                dt = parse_dt(row.get("created_at") or "")
                if not vid or not pid or not vs:
                    die("INVALID_VERSION_IDENTITY")
                if vid in versions_by_id:
                    die("DUPLICATE_VERSION_ID")
                versions_by_id[vid] = (pid, vs, dt)
                versions_by_pkg[pid].append((vid, vs, dt))
                version_rows += 1
        for pid in versions_by_pkg:
            versions_by_pkg[pid].sort(key=lambda x: (x[2], x[0]))

        min_dt = min(v[2] for v in versions_by_id.values())
        max_dt = max(v[2] for v in versions_by_id.values())
        horizon = timedelta(days=HORIZON_DAYS)
        eligible = []
        for vid, (pid, vs, dt) in versions_by_id.items():
            if dt + horizon <= max_dt:
                eligible.append((dt, vid, pid, vs))
        eligible.sort(key=lambda x: (x[0], x[1]))
        boundary = min_dt + (max_dt - min_dt) * 0.80
        train_ids = {x[1] for x in eligible if x[0] <= boundary}
        test_rows = [x for x in eligible if x[0] > boundary]
        train_rows = [x for x in eligible if x[0] <= boundary]

        # Outcome: later release of same package within 180 days, with complete follow-up guaranteed by eligibility.
        y_by_vid: dict[str, int] = {}
        for dt, vid, pid, vs in eligible:
            later = False
            for vid2, vs2, dt2 in versions_by_pkg[pid]:
                if dt < dt2 <= dt + horizon:
                    later = True
                    break
            y_by_vid[vid] = 1 if later else 0

        # Raw dependency declarations: retained for baseline D_o and T_acc construction.
        deps_by_origin: dict[str, list[tuple[str, str]]] = defaultdict(list)
        dep_rows = 0
        with zf.open(d_name, "r") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""))
            for row in reader:
                oid = (row.get("version_id") or row.get("package_version_id") or row.get("origin_version_id") or "").strip()
                tpid = (row.get("dependency_package_id") or row.get("target_package_id") or row.get("package_id") or "").strip()
                req = (row.get("req") or row.get("requirement") or row.get("version_req") or "").strip()
                if oid:
                    deps_by_origin[oid].append((tpid, req))
                dep_rows += 1

        # Build sparse feature matrices from the frozen representations.
        eligible_ids = [x[1] for x in eligible]
        row_index = {vid: i for i, vid in enumerate(eligible_ids)}
        n = len(eligible_ids)
        y = np.asarray([y_by_vid[vid] for vid in eligible_ids], dtype=np.int8)

        b_rows: list[int] = []
        b_cols: list[int] = []
        b_data: list[int] = []
        t_rows: list[int] = []
        t_cols: list[int] = []
        t_data: list[int] = []
        prior_release_count: list[float] = []
        package_age_days: list[float] = []
        dep_count: list[float] = []
        tacc_count: list[float] = []
        tacc_structural_hash = hashlib.sha256()
        resolved_edges = 0
        unresolved_edges = 0

        for i, vid in enumerate(eligible_ids):
            pid, vs, dt = versions_by_id[vid]
            pkg_versions = versions_by_pkg[pid]
            prior = sum(1 for _vid, _vs, _dt in pkg_versions if _dt < dt)
            age_days = (dt - pkg_versions[0][2]).total_seconds() / 86400.0
            dlist = deps_by_origin.get(vid, [])
            prior_release_count.append(float(prior))
            package_age_days.append(age_days)
            dep_count.append(float(len(dlist)))
            add_token(i, f"BASE_VERSION::{vs}", b_rows, b_cols, b_data)

            selected_pairs: list[tuple[str, str, str]] = []
            for target_pid, req in dlist:
                if target_pid not in versions_by_pkg or requirement_kind(req) == "UNSUPPORTED":
                    unresolved_edges += 1
                    continue
                candidates = [r for r in versions_by_pkg[target_pid] if r[2] <= dt and satisfies(r[1], req)]
                if not candidates:
                    unresolved_edges += 1
                    continue
                selected = max(candidates, key=lambda r: (version_key(r[1]), r[0]))
                selected_pairs.append((target_pid, selected[0], selected[1]))
            selected_pairs.sort(key=lambda x: (x[0], x[1], x[2]))
            for target_pid, target_vid, target_vs in selected_pairs:
                add_token(i, f"TACC_PAIR::{target_pid}::{target_vid}", t_rows, t_cols, t_data)
                resolved_edges += 1
            tacc_count.append(float(len(selected_pairs)))
            tacc_structural_hash.update(vid.encode("utf-8"))
            for target_pid, target_vid, target_vs in selected_pairs:
                tacc_structural_hash.update(b"|")
                tacc_structural_hash.update(target_pid.encode("utf-8"))
                tacc_structural_hash.update(b"|")
                tacc_structural_hash.update(target_vid.encode("utf-8"))
                tacc_structural_hash.update(b"|")
                tacc_structural_hash.update(target_vs.encode("utf-8"))
                tacc_structural_hash.update(b"\n")

        # Frozen numeric transformation: log1p, then training-only standardization.
        b_num = np.column_stack([prior_release_count, package_age_days, dep_count])
        t_num = np.asarray(tacc_count, dtype=float).reshape(-1, 1)
        train_mask = np.asarray([vid in train_ids for vid in eligible_ids], dtype=bool)
        test_mask = ~train_mask

        b_scaler = StandardScaler(with_mean=False)
        t_scaler = StandardScaler(with_mean=False)
        b_log = np.log1p(b_num)
        t_log = np.log1p(t_num)
        b_log[train_mask] = b_log[train_mask]
        t_log[train_mask] = t_log[train_mask]
        b_scaler.fit(b_log[train_mask])
        t_scaler.fit(t_log[train_mask])
        b_num_std = b_scaler.transform(b_log)
        t_num_std = t_scaler.transform(t_log)

        B_hash = csr_matrix((b_data, (b_rows, b_cols)), shape=(n, HASH_DIM), dtype=float)
        T_hash = csr_matrix((t_data, (t_rows, t_cols)), shape=(n, HASH_DIM), dtype=float)
        B = __import__("scipy.sparse").sparse.hstack([B_hash, b_num_std], format="csr")
        T = __import__("scipy.sparse").sparse.hstack([T_hash, t_num_std], format="csr")

        if B.shape != (n, HASH_DIM + 3) or T.shape != (n, HASH_DIM + 1):
            die("FEATURE_SHAPE_MISMATCH")
        if set(np.where(test_mask)[0]) != set(range(n)) - set(np.where(train_mask)[0]):
            die("SPLIT_MISMATCH")

        model_b = LogisticRegression(penalty=PENALTY, C=C, solver=SOLVER, fit_intercept=FIT_INTERCEPT, max_iter=MAX_ITER, tol=TOL, class_weight=CLASS_WEIGHT, random_state=RANDOM_STATE)
        model_t = LogisticRegression(penalty=PENALTY, C=C, solver=SOLVER, fit_intercept=FIT_INTERCEPT, max_iter=MAX_ITER, tol=TOL, class_weight=CLASS_WEIGHT, random_state=RANDOM_STATE)
        model_b.fit(B[train_mask], y[train_mask])
        model_t.fit(T[train_mask], y[train_mask])
        p_b = model_b.predict_proba(B[test_mask])[:, 1]
        p_t = model_t.predict_proba(T[test_mask])[:, 1]
        y_test = y[test_mask]

        ll_b = float(log_loss(y_test, p_b, labels=[0, 1]))
        ll_t = float(log_loss(y_test, p_t, labels=[0, 1]))
        delta = ll_b - ll_t
        brier_b = float(brier_score_loss(y_test, p_b))
        brier_t = float(brier_score_loss(y_test, p_t))
        auc_b = float(roc_auc_score(y_test, p_b)) if len(np.unique(y_test)) == 2 else None
        auc_t = float(roc_auc_score(y_test, p_t)) if len(np.unique(y_test)) == 2 else None

        manifest = {
            "experiment": "EXT-1.1_Rust",
            "runner": RUNNER_PATH,
            "runner_sha": git_blob_sha(runner),
            "mode": args.mode,
            "execution_timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "git_commit": git_head(),
            "git_clean_preflight": True,
            "dataset": {"path": str(DATASET), "size": DATASET_SIZE, "sha256": DATASET_SHA256},
            "runtime": {"python": py, "os": os_id, "machine": platform.machine(), "sklearn": sklearn.__version__, "numpy": np.__version__, "scipy": scipy.__version__},
            "decisions": REQUIRED_DECISIONS,
            "normative_resolver": {"path": NORMATIVE_RESOLVER, "git_blob_sha": NORMATIVE_RESOLVER_SHA},
            "population": {"all_version_rows": len(versions_by_id), "eligible_origins": n, "train_origins": int(train_mask.sum()), "test_origins": int(test_mask.sum())},
            "outcome": {"name": "Y_180", "horizon_days": HORIZON_DAYS},
            "temporal_boundary": str(boundary),
            "representations": {"B": "BASE_VERSION::<version_str> + log1p/prior_release_count/package_age_days/D_o", "T_acc": "TACC_PAIR::<target_package_id>::<target_version_id> + log1p/A_count", "hash_algorithm": HASH_ALGORITHM, "hash_dimension": HASH_DIM},
            "resolver_counts": {"resolved_transformations": resolved_edges, "unresolved_dependency_edges": unresolved_edges},
            "tacc_structural_sha256": tacc_structural_hash.hexdigest(),
            "learner": {"class": "sklearn.linear_model.LogisticRegression", "penalty": PENALTY, "C": C, "solver": SOLVER, "fit_intercept": FIT_INTERCEPT, "max_iter": MAX_ITER, "tol": TOL, "class_weight": CLASS_WEIGHT, "random_state": RANDOM_STATE},
            "primary_metric": "mean_test_log_loss",
            "primary_estimand": "LogLoss(B) - LogLoss(T_acc)",
            "replay_identifier": args.mode,
        }
        results = {
            "experiment": "EXT-1.1_Rust",
            "mode": args.mode,
            "eligible_origins": n,
            "train_origins": int(train_mask.sum()),
            "test_origins": int(test_mask.sum()),
            "test_positive": int(y_test.sum()),
            "test_negative": int((y_test == 0).sum()),
            "log_loss_B": ll_b,
            "log_loss_T_acc": ll_t,
            "delta_log_loss_B_minus_T_acc": delta,
            "brier_B": brier_b,
            "brier_T_acc": brier_t,
            "roc_auc_B": auc_b,
            "roc_auc_T_acc": auc_t,
        }
        manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
        results_path.write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")

        print("CONFIRMATORY_EXECUTION_COMPLETE: True")
        print("ELIGIBLE_ORIGINS:", n)
        print("TRAIN_ORIGINS:", int(train_mask.sum()))
        print("TEST_ORIGINS:", int(test_mask.sum()))
        print("LOG_LOSS_B:", ll_b)
        print("LOG_LOSS_TACC:", ll_t)
        print("DELTA_LOGLOSS_B_MINUS_TACC:", delta)
        print("RESULTS_WRITTEN:", results_path)
        print("MANIFEST_WRITTEN:", manifest_path)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"CONFIRMATORY_EXECUTION_INVALID: {exc}", file=sys.stderr)
        raise
