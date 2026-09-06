#!/usr/bin/env python3
"""EXT-1.1 Rust confirmatory runner v0.2.

Parameter-closed confirmatory execution. Scientific protocol values are frozen
by DR-023..DR-026D; the only operational argument is --mode primary|replay.
R* is imported from the normative rstar_v02.py and is never reimplemented here.
"""
from __future__ import annotations

import argparse
import bisect
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

DATASET = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"
DATASET_SHA256 = "823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224"
DATASET_SIZE = 6047715996
EXPECTED_PYTHON = "3.14.7"
EXPECTED_SKLEARN = "1.9.0"
EXPECTED_NUMPY = "2.5.2"
EXPECTED_SCIPY = "1.18.1"
EXPECTED_OS = "Windows-11-10.0.26200"
EXPECTED_MACHINE = "AMD64"
RANDOM_STATE = 0
HORIZON_DAYS = 180
HASH_DIM = 2 ** 20
SOLVER = "liblinear"
C = 1.0
MAX_ITER = 1000
TOL = 1e-8

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
OUTPUT_DIRS = {
    "primary": "03_EXPERIMENTS/EXT-1.1_Rust/execution/CONFIRMATORY_PRIMARY_v01",
    "replay": "03_EXPERIMENTS/EXT-1.1_Rust/execution/CONFIRMATORY_REPLAY_v01",
}


def die(msg: str) -> None:
    raise RuntimeError(msg)


def git(args: list[str]) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def repo_root() -> Path:
    return Path(git(["rev-parse", "--show-toplevel"]))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def git_blob_sha(path: Path) -> str:
    return git(["hash-object", str(path)])


def git_clean_for_execution(root: Path) -> bool:
    allowed = tuple(OUTPUT_DIRS.values())
    for line in git(["status", "--porcelain"]).splitlines():
        path = line[3:].strip().replace("\\", "/")
        if not any(path == a.rstrip("/") or path.startswith(a) for a in allowed):
            return False
    return True


def parse_dt(s: str) -> datetime:
    s = s.strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def archive_member(zf: zipfile.ZipFile, basename: str) -> str:
    hits = [n for n in zf.namelist() if n.replace("\\", "/").rsplit("/", 1)[-1] == basename]
    if len(hits) != 1:
        die(f"ARCHIVE_MEMBER_RESOLUTION_ERROR:{basename}:{len(hits)}")
    return hits[0]


def rows(zf: zipfile.ZipFile, basename: str):
    member = archive_member(zf, basename)
    with zf.open(member, "r") as raw:
        yield from csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", newline=""))


def hash_token(token: str) -> tuple[int, int]:
    d = hashlib.blake2b(token.encode("utf-8"), digest_size=32).digest()
    idx = int.from_bytes(d[:8], "big", signed=False) % HASH_DIM
    sign = 1 if d[8] % 2 == 0 else -1
    return idx, sign


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("primary", "replay"), required=True)
    args = ap.parse_args()
    root = repo_root()

    if not git_clean_for_execution(root):
        die("DIRTY_SCIENTIFIC_WORKTREE_OUTSIDE_CONFIRMATORY_OUTPUTS")
    if not DATASET.exists() or DATASET.stat().st_size != DATASET_SIZE:
        die("DATASET_SIZE_OR_EXISTENCE_MISMATCH")
    if sha256_file(DATASET) != DATASET_SHA256:
        die("DATASET_SHA256_MISMATCH")
    if platform.python_version() != EXPECTED_PYTHON or platform.machine() != EXPECTED_MACHINE:
        die("PYTHON_OR_MACHINE_MISMATCH")
    os_id = f"{platform.system()}-{platform.release()}-{platform.version()}"
    if os_id != EXPECTED_OS:
        die(f"OS_MISMATCH:{os_id}")

    import numpy as np
    import scipy
    import sklearn
    from scipy.sparse import csr_matrix, hstack
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import brier_score_loss, log_loss, roc_auc_score
    from sklearn.preprocessing import StandardScaler

    if (sklearn.__version__, np.__version__, scipy.__version__) != (EXPECTED_SKLEARN, EXPECTED_NUMPY, EXPECTED_SCIPY):
        die("PYTHON_PACKAGE_VERSION_MISMATCH")
    for key, rel in REQUIRED_DECISIONS.items():
        if not (root / rel).exists():
            die(f"MISSING_DECISION:{key}")
    resolver = root / NORMATIVE_RESOLVER
    if git_blob_sha(resolver) != NORMATIVE_RESOLVER_SHA:
        die("NORMATIVE_RESOLVER_SHA_MISMATCH")

    here = root / "03_EXPERIMENTS" / "EXT-1.1_Rust" / "src"
    if str(here) not in sys.path:
        sys.path.insert(0, str(here))
    from rstar_v02 import resolve_edge

    runner = root / RUNNER_PATH
    runner_sha = git_blob_sha(runner)
    git_head = git(["rev-parse", "HEAD"])
    outdir = root / OUTPUT_DIRS[args.mode]
    outdir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(DATASET, "r") as zf:
        package_ids: set[int] = set()
        for r in rows(zf, "packages.csv"):
            package_ids.add(int(r["id"]))

        versions: dict[int, tuple[int, str, datetime]] = {}
        versions_by_package: dict[int, list[tuple[int, str, str]]] = defaultdict(list)
        times_by_package: dict[int, list[datetime]] = defaultdict(list)
        for r in rows(zf, "package_versions.csv"):
            vid = int(r["id"])
            pid = int(r["package_id"])
            vs = r["version_str"].strip()
            dt = parse_dt(r["created_at"])
            if vid in versions:
                die(f"DUPLICATE_VERSION_ID:{vid}")
            versions[vid] = (pid, vs, dt)
            iso = dt.isoformat()
            versions_by_package[pid].append((vid, vs, iso))
            times_by_package[pid].append(dt)
        for pid in versions_by_package:
            ordered = sorted(zip(times_by_package[pid], versions_by_package[pid]), key=lambda x: (x[0], x[1][0]))
            times_by_package[pid] = [x[0] for x in ordered]
            versions_by_package[pid] = [x[1] for x in ordered]

        snapshot_max = max(dt for _, _, dt in versions.values())
        horizon = timedelta(days=HORIZON_DAYS)
        eligible = [(dt, vid, pid, vs) for vid, (pid, vs, dt) in versions.items() if dt + horizon <= snapshot_max]
        eligible.sort(key=lambda x: (x[0], x[1]))
        if not eligible:
            die("EMPTY_ELIGIBLE_POPULATION")
        min_eligible = eligible[0][0]
        max_eligible = eligible[-1][0]
        boundary = min_eligible + (max_eligible - min_eligible) * 0.80

        y = np.empty(len(eligible), dtype=np.int8)
        for i, (dt, vid, pid, _) in enumerate(eligible):
            ts = times_by_package[pid]
            lo = bisect.bisect_right(ts, dt)
            hi = bisect.bisect_right(ts, dt + horizon)
            y[i] = 1 if hi > lo else 0

        deps_by_origin: dict[int, list[tuple[int, str]]] = defaultdict(list)
        dependency_rows = 0
        for r in rows(zf, "package_dependencies.csv"):
            oid = int(r["depending_version"])
            tpid = int(r["depending_on_package"])
            req = r["semver_str"].strip()
            if oid not in versions:
                die(f"MISSING_ORIGIN_VERSION:{oid}")
            if tpid not in package_ids:
                die(f"MISSING_TARGET_PACKAGE:{tpid}")
            deps_by_origin[oid].append((tpid, req))
            dependency_rows += 1

        n = len(eligible)
        b_rows: list[int] = []
        b_cols: list[int] = []
        b_data: list[int] = []
        t_rows: list[int] = []
        t_cols: list[int] = []
        t_data: list[int] = []
        prior = np.zeros(n, dtype=np.float64)
        age = np.zeros(n, dtype=np.float64)
        d_count = np.zeros(n, dtype=np.float64)
        a_count = np.zeros(n, dtype=np.float64)
        resolved_edges = 0
        unresolved_edges = 0
        unique_tacc_relations = 0

        first_release: dict[int, datetime] = {pid: ts[0] for pid, ts in times_by_package.items() if ts}
        for i, (dt, vid, pid, vs) in enumerate(eligible):
            prior[i] = bisect.bisect_left(times_by_package[pid], dt)
            age[i] = (dt - first_release[pid]).total_seconds() / 86400.0
            dlist = deps_by_origin.get(vid, [])
            d_count[i] = len(dlist)
            bidx, bsign = hash_token(f"BASE_VERSION::{vs}")
            b_rows.append(i); b_cols.append(bidx); b_data.append(bsign)

            selected: set[tuple[int, int]] = set()
            origin_iso = dt.isoformat()
            for tpid, req in dlist:
                target_versions = versions_by_package.get(tpid, [])
                result = resolve_edge(vid, str(pid), origin_iso, tpid, str(tpid), req, target_versions)
                if result["selected_version_id"] is None:
                    unresolved_edges += 1
                    continue
                pair = (tpid, int(result["selected_version_id"]))
                selected.add(pair)
            a_count[i] = len(selected)
            unique_tacc_relations += len(selected)
            for tpid, tvid in sorted(selected):
                tidx, tsign = hash_token(f"TACC_PAIR::{tpid}::{tvid}")
                t_rows.append(i); t_cols.append(tidx); t_data.append(tsign)
                resolved_edges += 1

        B_hash = csr_matrix((np.asarray(b_data, dtype=np.float64), (b_rows, b_cols)), shape=(n, HASH_DIM))
        T_hash = csr_matrix((np.asarray(t_data, dtype=np.float64), (t_rows, t_cols)), shape=(n, HASH_DIM))
        B_num = np.column_stack((prior, age, d_count))
        T_num = np.column_stack((prior, age, d_count, a_count))
        train_mask = np.asarray([dt <= boundary for dt, _, _, _ in eligible], dtype=bool)
        test_mask = ~train_mask
        if not train_mask.any() or not test_mask.any():
            die("EMPTY_TRAIN_OR_TEST")

        def transform_num(raw: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
            x = np.log1p(raw)
            scaler = StandardScaler(with_mean=True, with_std=True)
            scaler.fit(x[train_mask])
            z = scaler.transform(x)
            zero_sd = scaler.scale_ == 0
            if zero_sd.any():
                z[:, zero_sd] = 0.0
            return z, scaler.mean_, scaler.scale_

        Bz, Bmean, Bscale = transform_num(B_num)
        Tz, Tmean, Tscale = transform_num(T_num)
        X_B = hstack((B_hash, csr_matrix(Bz)), format="csr")
        X_T = hstack((T_hash, csr_matrix(Tz)), format="csr")

        model_kwargs = dict(penalty="l2", C=C, solver=SOLVER, fit_intercept=True, max_iter=MAX_ITER, tol=TOL, class_weight=None, random_state=RANDOM_STATE)
        model_B = LogisticRegression(**model_kwargs)
        model_T = LogisticRegression(**model_kwargs)
        model_B.fit(X_B[train_mask], y[train_mask])
        model_T.fit(X_T[train_mask], y[train_mask])
        p_B = model_B.predict_proba(X_B[test_mask])[:, 1]
        p_T = model_T.predict_proba(X_T[test_mask])[:, 1]
        y_test = y[test_mask]
        ll_B = float(log_loss(y_test, p_B, labels=[0, 1]))
        ll_T = float(log_loss(y_test, p_T, labels=[0, 1]))
        delta = ll_B - ll_T
        result = {
            "mode": args.mode,
            "n_versions": len(versions),
            "n_eligible": n,
            "n_train": int(train_mask.sum()),
            "n_test": int(test_mask.sum()),
            "n_dependency_rows": dependency_rows,
            "resolved_tacc_relations": resolved_edges,
            "unresolved_dependency_edges": unresolved_edges,
            "unique_tacc_relations": unique_tacc_relations,
            "temporal_boundary": boundary.isoformat(),
            "y_test_class_counts": {"0": int((y_test == 0).sum()), "1": int((y_test == 1).sum())},
            "log_loss_B": ll_B,
            "log_loss_T_acc": ll_T,
            "delta_log_loss_B_minus_T_acc": float(delta),
        }
        if len(np.unique(y_test)) == 2:
            result["brier_B"] = float(brier_score_loss(y_test, p_B))
            result["brier_T_acc"] = float(brier_score_loss(y_test, p_T))
            result["roc_auc_B"] = float(roc_auc_score(y_test, p_B))
            result["roc_auc_T_acc"] = float(roc_auc_score(y_test, p_T))
        else:
            result["brier_B"] = None; result["brier_T_acc"] = None; result["roc_auc_B"] = None; result["roc_auc_T_acc"] = None

        manifest = {
            "runner_path": RUNNER_PATH,
            "runner_blob_sha": runner_sha,
            "git_head": git_head,
            "mode": args.mode,
            "dataset_path": str(DATASET),
            "dataset_size": DATASET_SIZE,
            "dataset_sha256": DATASET_SHA256,
            "runtime": {"python": platform.python_version(), "os": os_id, "machine": platform.machine(), "sklearn": sklearn.__version__, "numpy": np.__version__, "scipy": scipy.__version__},
            "normative_resolver": {"path": NORMATIVE_RESOLVER, "blob_sha": NORMATIVE_RESOLVER_SHA},
            "random_state": RANDOM_STATE,
            "horizon_days": HORIZON_DAYS,
            "hash_dimension": HASH_DIM,
            "hash_algorithm": "blake2b-256",
            "hash_encoding": "UTF-8",
            "hash_index": "first_8_digest_bytes_big_endian_unsigned_mod_2^20",
            "hash_sign": "ninth_digest_byte_even_plus1_odd_minus1",
            "model": {"class": "sklearn.linear_model.LogisticRegression", "penalty": "l2", "C": C, "solver": SOLVER, "fit_intercept": True, "max_iter": MAX_ITER, "tol": TOL, "class_weight": None, "random_state": RANDOM_STATE},
            "split": "first 80% elapsed eligible-origin timeline; train <= boundary; test > boundary",
            "primary_metric": "mean_test_log_loss",
            "primary_comparison": "LogLoss(B)-LogLoss(T_acc)",
            "prohibited_inference": {"p_values": False, "confidence_intervals": False, "significance": False},
        }
        (outdir / "EXECUTION_MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
        (outdir / "RESULTS.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")

        print("EXT-1.1_RUST_CONFIRMATORY_RUNNER_V0.2")
        print(f"MODE: {args.mode}")
        print(f"ELIGIBLE_ORIGINS: {n}")
        print(f"TRAIN_ORIGINS: {int(train_mask.sum())}")
        print(f"TEST_ORIGINS: {int(test_mask.sum())}")
        print(f"RESOLVED_TACC_RELATIONS: {resolved_edges}")
        print(f"UNRESOLVED_DEPENDENCY_EDGES: {unresolved_edges}")
        print(f"LOGLOSS_B: {ll_B:.12f}")
        print(f"LOGLOSS_TACC: {ll_T:.12f}")
        print(f"DELTA_LOSS_B_MINUS_TACC: {delta:.12f}")
        print("CONFIRMATORY_EXECUTION_COMPLETED: True")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
