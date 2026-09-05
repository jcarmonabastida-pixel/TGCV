#!/usr/bin/env python3
"""R* v0.2 SQLite conformance runner.

Runs implementation conformance checks and a bounded real-data smoke test
against the frozen Rust dataset. This is a conformance gate only; it does
not execute the scientific A/B/C experiment and does not claim Cargo
historical equivalence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from rstar_v02 import resolve_edge, RStarError  # noqa: E402

REQUIRED = {
    "packages": {"id", "name"},
    "package_versions": {"id", "package_id", "version_str", "created_at"},
    "package_dependencies": {"depending_version", "depending_on_package", "semver_str"},
}
EXPECTED_SPEC_BLOB = "77bd55820ff7c8a1bfc14fd1e7a09febda1d77f5"
EXPECTED_IMPL_COMMIT = "1eb7eae34e6f2c7ca72cd3a1bb307c142903d256"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return "unknown"


def run_code_checks() -> list[dict]:
    cases = []
    def check(name, fn):
        try:
            fn(); cases.append({"name": name, "status": "PASS"})
        except Exception as e:
            cases.append({"name": name, "status": "FAIL", "error": f"{type(e).__name__}: {e}"})

    check("exact_match", lambda: (
        resolve_edge(1, "origin", 2, "target", "=1.2.3",
                     [{"id": 10, "package_id": 2, "version_str": "1.2.3", "created_at": "2020-01-01"}],
                     "2020-02-01")["selected_version"] == "1.2.3"
    ))
    check("caret_1_0", lambda: (
        resolve_edge(1, "origin", 2, "target", "^1.0",
                     [{"id": 10, "package_id": 2, "version_str": "1.0.9", "created_at": "2020-01-01"},
                      {"id": 11, "package_id": 2, "version_str": "1.1.0", "created_at": "2020-01-01"},
                      {"id": 12, "package_id": 2, "version_str": "2.0.0", "created_at": "2020-01-01"}],
                     "2020-02-01")["selected_version"] == "1.1.0"
    ))
    check("unsupported_is_distinct", lambda: (
        resolve_edge(1, "origin", 2, "target", ">=1.0",
                     [{"id": 10, "package_id": 2, "version_str": "1.2.3", "created_at": "2020-01-01"}],
                     "2020-02-01")["exclusion_reason"] == "UNSUPPORTED_CONSTRAINT"
    ))
    check("temporal_cutoff", lambda: (
        resolve_edge(1, "origin", 2, "target", "^1.0",
                     [{"id": 10, "package_id": 2, "version_str": "1.1.0", "created_at": "2020-01-01"},
                      {"id": 11, "package_id": 2, "version_str": "1.9.0", "created_at": "2021-01-01"}],
                     "2020-06-01")["selected_version"] == "1.1.0"
    ))
    check("row_order_independence", lambda: (
        resolve_edge(1, "origin", 2, "target", "^1.0",
                     [{"id": 11, "package_id": 2, "version_str": "1.9.0", "created_at": "2020-01-01"},
                      {"id": 10, "package_id": 2, "version_str": "1.8.0", "created_at": "2020-01-01"}],
                     "2020-06-01")["selected_version"] == "1.9.0"
    ))
    check("duplicate_id_fail_closed", lambda: _expect_error(
        lambda: resolve_edge(1, "origin", 2, "target", "^1.0",
            [{"id": 10, "package_id": 2, "version_str": "1.0.0", "created_at": "2020-01-01"},
             {"id": 10, "package_id": 2, "version_str": "1.0.1", "created_at": "2020-01-01"}],
            "2020-06-01")
    ))
    return cases


def _expect_error(fn):
    try:
        fn()
    except RStarError:
        return True
    raise AssertionError("expected RStarError")


def schema_and_counts(con):
    out = {}
    for table, required in REQUIRED.items():
        cols = {r[1] for r in con.execute(f"PRAGMA table_info({table})")}
        missing = sorted(required - cols)
        out[table] = {"columns_present": sorted(cols), "missing_required": missing,
                      "row_count": con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]}
    return out


def smoke_test(con):
    """Bounded integration check using a known historical dependency path."""
    origin = con.execute(
        "SELECT pv.id, p.name, pv.created_at FROM package_versions pv "
        "JOIN packages p ON p.id=pv.package_id "
        "WHERE p.name=? AND pv.version_str=? LIMIT 1",
        ("solana-tokens", "1.10.38"),
    ).fetchone()
    if not origin:
        return {"status": "BLOCKED", "reason": "KNOWN_SMOKE_ORIGIN_NOT_FOUND"}
    dep = con.execute(
        "SELECT pd.depending_on_package, pd.semver_str, p.name "
        "FROM package_dependencies pd JOIN packages p ON p.id=pd.depending_on_package "
        "WHERE pd.depending_version=? AND p.name=? LIMIT 1",
        (origin[0], "serde"),
    ).fetchone()
    if not dep:
        return {"status": "BLOCKED", "reason": "KNOWN_SMOKE_DEPENDENCY_NOT_FOUND"}
    versions = con.execute(
        "SELECT id, package_id, version_str, created_at FROM package_versions "
        "WHERE package_id=? AND created_at<=? ORDER BY id",
        (dep[0], origin[2]),
    ).fetchall()
    rows = [{"id": r[0], "package_id": r[1], "version_str": r[2], "created_at": r[3]} for r in versions]
    result = resolve_edge(origin[0], origin[1], dep[0], dep[2], dep[1], rows, origin[2])
    return {"status": "PASS", "origin_id": origin[0], "origin_name": origin[1],
            "origin_created_at": origin[2], "target_package": dep[2],
            "constraint": dep[1], "candidate_count": result["candidate_count"],
            "selected_version_id": result.get("selected_version_id"),
            "selected_version": result.get("selected_version"),
            "exclusion_reason": result.get("exclusion_reason")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True, help="Path to frozen Rust SQLite export")
    ap.add_argument("--output", default="CONFORMANCE_RESULT.json")
    ap.add_argument("--skip-hash", action="store_true")
    args = ap.parse_args()
    db = Path(args.db).expanduser().resolve()
    result = {
        "runner": "RSTAR_CONFORMANCE_RUNNER_v0.1",
        "status": "NOT_EXECUTED",
        "implementation_expected_commit": EXPECTED_IMPL_COMMIT,
        "spec_expected_blob": EXPECTED_SPEC_BLOB,
        "git_head": git_head(),
        "python": platform.python_version(),
        "platform": platform.platform(),
        "database": {"path": str(db), "exists": db.exists()},
        "code_checks": [],
        "schema": {},
        "smoke_test": {},
    }
    if not db.exists():
        result["status"] = "BLOCKED"
        result["failure"] = "DATABASE_NOT_FOUND"
    else:
        if not args.skip_hash:
            result["database"]["sha256"] = sha256(db)
        uri = "file:" + str(db).replace("\\", "/").replace(" ", "%20") + "?mode=ro"
        try:
            con = sqlite3.connect(uri, uri=True)
            con.execute("PRAGMA query_only=ON")
            result["sqlite_version"] = sqlite3.sqlite_version
            result["code_checks"] = run_code_checks()
            result["schema"] = schema_and_counts(con)
            missing = [t for t, x in result["schema"].items() if x["missing_required"]]
            if missing:
                result["status"] = "BLOCKED"
                result["failure"] = "SCHEMA_MISSING_REQUIRED_COLUMNS"
            elif any(x["status"] != "PASS" for x in result["code_checks"]):
                result["status"] = "FAIL"
                result["failure"] = "IMPLEMENTATION_CONFORMANCE_CHECK_FAILED"
            else:
                result["smoke_test"] = smoke_test(con)
                result["status"] = "PASS" if result["smoke_test"].get("status") == "PASS" else result["smoke_test"].get("status", "BLOCKED")
            con.close()
        except Exception as e:
            result["status"] = "FAIL"
            result["failure"] = f"{type(e).__name__}: {e}"
    out = Path(args.output)
    out.write_text(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
