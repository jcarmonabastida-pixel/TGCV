"""C09 OLPC Peru causal-gap closure executor v0.1.

Purpose: execute the frozen C09 gap-closure specification against the public
openICPSR 113587 V2 package. This is a C09 evidence operation, not a TR-132
proof/reproduction exercise.

No prior TGCV execution outputs are read. Only the public package supplied via
--data-root is accessed. Results are written to --output-dir.

Requires Python 3.8+ and pyreadstat.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat

SPEC = "TGCV_C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_SPEC_001"
DEFAULT_ROOT = Path(r"C:\Users\pedri\Downloads\openICPSR\113587-V2")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_dta(path: Path):
    return pyreadstat.read_dta(str(path), encoding="latin1")


def locate(root: Path, filename: str) -> Path:
    hits = list(root.rglob(filename))
    if len(hits) != 1:
        raise RuntimeError(f"Expected exactly one {filename}; found {len(hits)}: {hits}")
    return hits[0]


def pick_col(df: pd.DataFrame, exact: str) -> str:
    if exact in df.columns:
        return exact
    raise RuntimeError(f"Required variable missing: {exact}")


def binary_yes(x):
    return pd.to_numeric(x, errors="coerce").replace({1: 1, 2: 0})


def mean_diff(df, y, z):
    a = df.loc[df[z] == 1, y].dropna()
    b = df.loc[df[z] == 0, y].dropna()
    if len(a) == 0 or len(b) == 0:
        return {"n_z1": int(len(a)), "n_z0": int(len(b)), "mean_z1": None, "mean_z0": None, "diff": None}
    return {"n_z1": int(len(a)), "n_z0": int(len(b)), "mean_z1": float(a.mean()), "mean_z0": float(b.mean()), "diff": float(a.mean() - b.mean())}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-root", type=Path, default=DEFAULT_ROOT)
    ap.add_argument("--output-dir", type=Path, default=Path("03_EXPERIMENTS/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE/output"))
    args = ap.parse_args()
    root = args.data_root.resolve()
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=True)

    if not root.exists():
        raise RuntimeError(f"DATA_ROOT_NOT_FOUND: {root}")

    # Frozen public inputs.
    p_lists = locate(root, "listas_final.dta")
    p_pairs = locate(root, "school_pairs_final.dta")
    p_r1_p2 = locate(root, "cestudiante_g3-6_p2_r1.dta")
    p_r2_p2 = locate(root, "cestudiante_g3-6_p2_r2.dta")
    p_r2_p1 = locate(root, "cestudiante_g3-6_p1_r2.dta")

    files = [p_lists, p_pairs, p_r1_p2, p_r2_p2, p_r2_p1]
    inventory = [{"path": str(p), "sha256": sha256_file(p), "bytes": p.stat().st_size} for p in files]

    lists, _ = read_dta(p_lists)
    pairs, _ = read_dta(p_pairs)
    r1, _ = read_dta(p_r1_p2)
    r2p2, _ = read_dta(p_r2_p2)
    r2p1, _ = read_dta(p_r2_p1)

    # A. Assignment: Z is frozen as won_lottery. Never substitute receipt or school treatment.
    for c in ["codest", "participated_in_lottery", "won_lottery", "received_laptop", "treatment_school"]:
        pick_col(lists, c)
    pick_col(pairs, "treatment_school")
    pick_col(pairs, "pair")

    # Link student -> lottery/implementation/school condition.
    r1 = r1.merge(lists[["codest", "participated_in_lottery", "won_lottery", "received_laptop", "treatment_school"]], on="codest", how="left", validate="one_to_one")
    if r1["won_lottery"].isna().any():
        raise RuntimeError("ASSIGNMENT_LINK_FAIL: missing won_lottery after student linkage")

    # B. Baseline accessibility: R1 P2/P3/P4 + P12_A1..A8.
    baseline_cols = ["P2", "P3", "P4"] + [f"P12_A{i}" for i in range(1, 9)]
    for c in baseline_cols:
        pick_col(r1, c)
    r1["Tacc0_resource_computer"] = binary_yes(r1["P2"])
    r1["Tacc0_resource_internet"] = binary_yes(r1["P3"])
    r1["Tacc0_resource_prior_use"] = binary_yes(r1["P4"])
    cap_cols = []
    for i in range(1, 9):
        c = f"P12_A{i}"
        nc = f"Tacc0_cap_A{i}"
        r1[nc] = binary_yes(r1[c])
        cap_cols.append(nc)
    r1["Tacc0_capacity_count"] = r1[cap_cols].sum(axis=1, min_count=1)

    # C. Post-treatment accessibility: R2 P1/P2/P3 only.
    for c in ["codest", "P1", "P2", "P3"]:
        pick_col(r2p2, c)
    r2 = r2p2[["codest", "P1", "P2", "P3"]].copy()
    r2["Tacc1_resource_computer"] = binary_yes(r2["P1"])
    r2["Tacc1_resource_internet"] = binary_yes(r2["P2"])
    r2["Tacc1_resource_prior_use"] = binary_yes(r2["P3"])

    # D. Merge only for the bounded accessibility transition and downstream trajectory.
    # Require one observation per student in each source.
    if r1["codest"].duplicated().any() or r2["codest"].duplicated().any():
        raise RuntimeError("NON_UNIQUE_STUDENT_KEY")
    d = r1.merge(r2, on="codest", how="inner", suffixes=("", "_r2"), validate="one_to_one")

    for c in ["won_lottery", "received_laptop", "treatment_school"]:
        d[c] = pd.to_numeric(d[c], errors="coerce")
    d["Z"] = d["won_lottery"].where(d["won_lottery"].isin([0, 1]))

    # Bounded resource transition indicators. Capacity is retained as baseline context;
    # it is not used to manufacture a post-treatment capacity score.
    d["delta_computer"] = d["Tacc1_resource_computer"] - d["Tacc0_resource_computer"]
    d["delta_internet"] = d["Tacc1_resource_internet"] - d["Tacc0_resource_internet"]
    d["delta_prior_use"] = d["Tacc1_resource_prior_use"] - d["Tacc0_resource_prior_use"]
    d["delta_resource_count"] = (
        d[["Tacc1_resource_computer", "Tacc1_resource_internet", "Tacc1_resource_prior_use"]].sum(axis=1, min_count=1)
        - d[["Tacc0_resource_computer", "Tacc0_resource_internet", "Tacc0_resource_prior_use"]].sum(axis=1, min_count=1)
    )

    # E. Downstream trajectory/use. R2 P4-P7 are retained as observations, never as accessibility.
    # These variables are read from R2 P1/P2 file if present; otherwise execution records a blocked field.
    trajectory = [c for c in ["P4", "P5", "P6", "P7"] if c in r2p2.columns]
    if not trajectory:
        raise RuntimeError("TRAJECTORY_VARIABLES_NOT_FOUND: expected R2 P4-P7")
    for c in trajectory:
        d[f"trajectory_{c}"] = binary_yes(d[c + "_r2"] if c + "_r2" in d.columns else d[c])

    # F. Endpoint Y from 36 Raven items. Locate the R2 file containing p1..p36.
    raven_path = None
    raven_df = None
    for candidate in root.rglob("*.dta"):
        try:
            tmp, _ = read_dta(candidate)
            if all(f"p{i}" in tmp.columns for i in range(1, 37)):
                raven_path, raven_df = candidate, tmp
                break
        except Exception:
            continue
    if raven_path is not None:
        raven_items = [f"p{i}" for i in range(1, 37)]
        rr = raven_df[["codest"] + raven_items].copy() if "codest" in raven_df.columns else None
        if rr is not None:
            # Keys are intentionally not inferred from values here. The execution records
            # the independently reconstructable item count and leaves key-based scoring to
            # the published replication code if required.
            rr["raven_nonmissing_items"] = rr[raven_items].notna().sum(axis=1)
            d = d.merge(rr[["codest", "raven_nonmissing_items"]], on="codest", how="left", validate="one_to_one")
    else:
        d["raven_nonmissing_items"] = np.nan

    # Summary contrasts. These are reduced-form checks of the experimental accessibility
    # change and downstream trajectory; they are NOT silently labelled as mediation.
    contrasts = {
        "Z_to_delta_computer": mean_diff(d, "delta_computer", "Z"),
        "Z_to_delta_internet": mean_diff(d, "delta_internet", "Z"),
        "Z_to_delta_prior_use": mean_diff(d, "delta_prior_use", "Z"),
        "Z_to_delta_resource_count": mean_diff(d, "delta_resource_count", "Z"),
    }
    for c in trajectory:
        contrasts[f"Z_to_trajectory_{c}"] = mean_diff(d, f"trajectory_{c}", "Z")

    # Minimal integrity/identity checks.
    pair_counts = pairs.groupby("pair")["treatment_school"].agg(["count", "sum"]).reset_index()
    pair_valid = bool((pair_counts["count"] == 2).all() and (pair_counts["sum"] == 1).all())
    identity = {
        "Z_definition": "won_lottery",
        "receipt_definition": "received_laptop",
        "school_condition_definition": "treatment_school",
        "Z_not_receipt": bool((d[["Z", "received_laptop"]].dropna().shape[0] == 0) or (d["Z"].fillna(-1).ne(d["received_laptop"].fillna(-2)).any())),
        "school_pair_structure_valid": pair_valid,
    }

    # Scientific decision rule: this executor does not infer causal mediation from
    # reduced-form effects. It reports whether the first-stage and trajectory evidence
    # are present, then marks the causal bridge as requiring explicit identification.
    first_stage_present = any(v["diff"] is not None and abs(v["diff"]) > 0 for k, v in contrasts.items() if k.startswith("Z_to_delta_"))
    trajectory_present = any(v["diff"] is not None and abs(v["diff"]) > 0 for k, v in contrasts.items() if k.startswith("Z_to_trajectory_"))
    verdict = "PARTIAL/INCONCLUSIVE"
    if first_stage_present and trajectory_present:
        verdict = "PARTIAL/INCONCLUSIVE"
        causal_note = "Experimental accessibility change and downstream trajectory difference are both observed, but this executor does not claim an accessibility-mediated causal effect without an explicit identification/exclusion argument."
    elif not first_stage_present:
        verdict = "FAIL"
        causal_note = "No measurable bounded accessibility change was reconstructed from Z in the tested indicators."
    else:
        verdict = "PARTIAL/INCONCLUSIVE"
        causal_note = "Accessibility change is observed but the tested downstream trajectory contrast is not established."

    result = {
        "spec": SPEC,
        "status": verdict,
        "causal_note": causal_note,
        "data_root": str(root),
        "inventory": inventory,
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "pandas": pd.__version__,
            "pyreadstat": getattr(pyreadstat, "__version__", "unknown"),
        },
        "n": {
            "lists": int(len(lists)),
            "r1_linked": int(len(r1)),
            "r2": int(len(r2)),
            "paired_r1_r2": int(len(d)),
        },
        "identity": identity,
        "trajectory_variables_found": trajectory,
        "raven_source": str(raven_path) if raven_path else None,
        "contrasts": contrasts,
        "output_schema": list(d.columns),
    }
    raw_json = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)
    result_path = out / "C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_RESULT_001.json"
    result_path.write_text(raw_json, encoding="utf-8")
    result["result_sha256"] = sha256_file(result_path)
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")

    # Export only the bounded audit dataset, not arbitrary raw source data.
    export_cols = ["codest", "Z", "received_laptop", "treatment_school", "Tacc0_capacity_count",
                   "Tacc0_resource_computer", "Tacc0_resource_internet", "Tacc0_resource_prior_use",
                   "Tacc1_resource_computer", "Tacc1_resource_internet", "Tacc1_resource_prior_use",
                   "delta_computer", "delta_internet", "delta_prior_use", "delta_resource_count"]
    export_cols += [f"trajectory_{c}" for c in trajectory]
    if "raven_nonmissing_items" in d.columns:
        export_cols.append("raven_nonmissing_items")
    audit_df = d[[c for c in export_cols if c in d.columns]].copy()
    audit_path = out / "C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_AUDIT_DATA_001.csv"
    audit_df.to_csv(audit_path, index=False)

    log_path = out / "C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_EXECUTION_LOG_001.txt"
    log_path.write_text(
        f"SPEC={SPEC}\nSTATUS={verdict}\nDATA_ROOT={root}\nRESULT={result_path}\n"
        f"RESULT_SHA256={sha256_file(result_path)}\nAUDIT_DATA_SHA256={sha256_file(audit_path)}\n",
        encoding="utf-8",
    )
    print(json.dumps({"status": verdict, "result": str(result_path), "audit_data": str(audit_path), "log": str(log_path)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
