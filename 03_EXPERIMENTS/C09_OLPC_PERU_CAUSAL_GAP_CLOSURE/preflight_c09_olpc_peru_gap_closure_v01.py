"""C09 OLPC Peru causal-gap closure preflight v0.1.

Preflight only. It does NOT execute the scientific C09 analysis and does NOT
produce a C09 verdict. It checks that the frozen public V2 inputs and required
variables are locally available before the causal-gap closure executor runs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from pathlib import Path

import pandas as pd
import pyreadstat

DEFAULT_ROOT = Path(r"C:\Users\pedri\Downloads\openICPSR\113587-V2")

REQUIRED = {
    "listas_final.dta": ["codest", "participated_in_lottery", "won_lottery", "received_laptop", "treatment_school"],
    "school_pairs_final.dta": ["pair", "treatment_school", "codmod"],
    "cestudiante_g3-6_p2_r1.dta": ["codest", "P2", "P3", "P4"] + [f"P12_A{i}" for i in range(1, 9)],
    "cestudiante_g3-6_p1_r2.dta": ["codest"],
    "cestudiante_g3-6_p2_r2.dta": ["codest", "P1", "P2", "P3", "P4", "P5", "P6", "P7"],
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def locate(root: Path, filename: str) -> Path:
    hits = list(root.rglob(filename))
    if len(hits) != 1:
        raise RuntimeError(f"EXPECTED_ONE_FILE:{filename}:found={len(hits)}")
    return hits[0]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-root", type=Path, default=DEFAULT_ROOT)
    ap.add_argument("--output-dir", type=Path, default=Path("03_EXPERIMENTS/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE/output"))
    args = ap.parse_args()
    root = args.data_root.resolve()
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=True)

    result = {
        "operation": "C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_PREFLIGHT",
        "scientific_execution": False,
        "data_root": str(root),
        "status": "PASS",
        "checks": [],
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "pandas": pd.__version__,
            "pyreadstat": getattr(pyreadstat, "__version__", "unknown"),
        },
    }

    if not root.exists():
        result["status"] = "BLOCKED_INFRASTRUCTURE"
        result["checks"].append({"check": "data_root_exists", "status": "FAIL", "detail": str(root)})
    else:
        result["checks"].append({"check": "data_root_exists", "status": "PASS", "detail": str(root)})

    for filename, required_cols in REQUIRED.items():
        if result["status"] != "PASS":
            break
        try:
            path = locate(root, filename)
            df, _ = pyreadstat.read_dta(str(path), encoding="latin1", metadataonly=False)
            missing = [c for c in required_cols if c not in df.columns]
            status = "PASS" if not missing else "FAIL"
            if status == "FAIL":
                result["status"] = "BLOCKED_INFRASTRUCTURE"
            result["checks"].append({
                "check": f"input:{filename}",
                "status": status,
                "rows": int(len(df)),
                "columns_missing": missing,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            })
        except Exception as exc:
            result["status"] = "BLOCKED_INFRASTRUCTURE"
            result["checks"].append({"check": f"input:{filename}", "status": "FAIL", "detail": repr(exc)})

    # Structural checks needed for the frozen causal design, without computing effects.
    if result["status"] == "PASS":
        lists = pyreadstat.read_dta(str(locate(root, "listas_final.dta")), encoding="latin1")[0]
        pairs = pyreadstat.read_dta(str(locate(root, "school_pairs_final.dta")), encoding="latin1")[0]
        r1 = pyreadstat.read_dta(str(locate(root, "cestudiante_g3-6_p2_r1.dta")), encoding="latin1")[0]
        pair_counts = pairs.groupby("pair")["treatment_school"].agg(["count", "sum"])
        pair_valid = bool((pair_counts["count"] == 2).all() and (pair_counts["sum"] == 1).all())
        unique_lists = int(lists["codest"].nunique()) == len(lists)
        unique_r1 = int(r1["codest"].nunique()) == len(r1)
        result["checks"].extend([
            {"check": "student_assignment_key_unique", "status": "PASS" if unique_lists else "FAIL"},
            {"check": "r1_student_key_unique", "status": "PASS" if unique_r1 else "FAIL"},
            {"check": "school_pair_structure", "status": "PASS" if pair_valid else "FAIL", "pairs": int(len(pair_counts))},
            {"check": "frozen_assignment_identity", "status": "PASS", "detail": "Z=won_lottery; receipt=received_laptop; school_condition=treatment_school"},
        ])
        if not (unique_lists and unique_r1 and pair_valid):
            result["status"] = "BLOCKED_INFRASTRUCTURE"

    path = out / "C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_PREFLIGHT_001.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps({"status": result["status"], "preflight": str(path)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
