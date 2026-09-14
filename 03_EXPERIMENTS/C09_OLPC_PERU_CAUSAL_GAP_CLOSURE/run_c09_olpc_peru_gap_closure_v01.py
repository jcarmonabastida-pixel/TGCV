"""C09 OLPC Peru causal-gap closure executor v0.2.

Executes the frozen C09 gap-closure specification against openICPSR 113587 V2.
This is an evidence operation, not a TR-132 proof/reproduction exercise.

The R2 trajectory block is implemented according to the published input_r2.do:
P4_A/B1..5 -> yesterday-use duration; P5_A1..5 -> weekly use by place;
P6_A1..4 -> weekly use by activity; P7 -> weekly Internet use.
Raven scoring reproduces the published 36-item answer key from input_r2.do.
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
RAVEN_KEY = [4,5,1,2,6,3,6,2,1,3,4,5,4,5,1,6,2,1,3,4,6,3,5,2,2,6,1,2,1,3,5,6,4,3,4,5]


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


def resolve_col(df: pd.DataFrame, name: str) -> str:
    by_lower = {str(c).lower(): str(c) for c in df.columns}
    if name.lower() not in by_lower:
        raise RuntimeError(f"Required variable missing: {name}")
    return by_lower[name.lower()]


def binary_yes(x):
    s = pd.to_numeric(x, errors="coerce")
    return s.where(s.isin([1, 2])).map({1: 1, 2: 0})


def mean_diff(df, y, z):
    a = df.loc[df[z] == 1, y].dropna()
    b = df.loc[df[z] == 0, y].dropna()
    if len(a) == 0 or len(b) == 0:
        return {"n_z1": int(len(a)), "n_z0": int(len(b)), "mean_z1": None, "mean_z0": None, "diff": None}
    return {"n_z1": int(len(a)), "n_z0": int(len(b)), "mean_z1": float(a.mean()), "mean_z0": float(b.mean()), "diff": float(a.mean() - b.mean())}


def derive_trajectory(r2: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    d = r2.copy()
    # Published input_r2.do: when one duration component is missing while its pair is
    # observed, replace the missing component by zero; negative survey codes remain missing.
    duration_names = []
    for i in range(1, 6):
        a = resolve_col(d, f"P4_A{i}")
        b = resolve_col(d, f"P4_B{i}")
        av = pd.to_numeric(d[a], errors="coerce")
        bv = pd.to_numeric(d[b], errors="coerce")
        av = av.where(av >= 0)
        bv = bv.where(bv >= 0)
        av = av.mask(av.isna() & bv.notna(), 0)
        bv = bv.mask(bv.isna() & av.notna(), 0)
        d[f"trajectory_P4_duration_{i}_minutes"] = av * 60 + bv
        duration_names.append(f"trajectory_P4_duration_{i}_minutes")
    d["trajectory_P4_total_minutes"] = d[duration_names].sum(axis=1, min_count=1)
    d["trajectory_P4_used_yesterday"] = d["trajectory_P4_total_minutes"].gt(0).astype(float)
    d.loc[d[duration_names].notna().sum(axis=1).eq(0), "trajectory_P4_used_yesterday"] = np.nan

    weekly_names = []
    for i in range(1, 6):
        c = resolve_col(d, f"P5_A{i}")
        s = pd.to_numeric(d[c], errors="coerce")
        d[f"trajectory_P5_place_{i}"] = s.where(s.isin([1, 2])).map({1: 1, 2: 0})
        weekly_names.append(f"trajectory_P5_place_{i}")
    d["trajectory_P5_used_week"] = d[weekly_names].max(axis=1, skipna=True)
    d.loc[d[weekly_names].notna().sum(axis=1).eq(0), "trajectory_P5_used_week"] = np.nan

    activity_names = []
    for i in range(1, 5):
        c = resolve_col(d, f"P6_A{i}")
        s = pd.to_numeric(d[c], errors="coerce")
        d[f"trajectory_P6_activity_{i}"] = s.where(s.isin([1, 2])).map({1: 1, 2: 0})
        activity_names.append(f"trajectory_P6_activity_{i}")
    d["trajectory_P6_any_activity"] = d[activity_names].max(axis=1, skipna=True)
    d.loc[d[activity_names].notna().sum(axis=1).eq(0), "trajectory_P6_any_activity"] = np.nan

    p7 = pd.to_numeric(d[resolve_col(d, "P7")], errors="coerce")
    d["trajectory_P7_internet_use"] = p7.where(p7.isin([1, 2])).map({1: 1, 2: 0})
    return d, [
        "trajectory_P4_used_yesterday", "trajectory_P4_total_minutes",
        "trajectory_P5_used_week", "trajectory_P6_any_activity", "trajectory_P7_internet_use",
    ]


def build_raven(root: Path) -> tuple[pd.DataFrame | None, Path | None]:
    # Prefer a published derived file containing raven_r2.
    candidates = list(root.rglob("*.dta"))
    for path in candidates:
        try:
            tmp, _ = read_dta(path)
        except Exception:
            continue
        lower = {str(c).lower(): str(c) for c in tmp.columns}
        if "raven_r2" in lower and "codest" in lower:
            rr = tmp[[lower["codest"], lower["raven_r2"]]].copy()
            rr.columns = ["codest", "raven_r2"]
            return rr, path
    # Otherwise reproduce input_r2.do exactly from p1..p36 and its published key.
    for path in candidates:
        try:
            tmp, _ = read_dta(path)
        except Exception:
            continue
        lower = {str(c).lower(): str(c) for c in tmp.columns}
        if "codest" not in lower or not all(f"p{i}" in lower for i in range(1, 37)):
            continue
        cod = lower["codest"]
        items = [lower[f"p{i}"] for i in range(1, 37)]
        x = tmp[[cod] + items].copy()
        score = pd.Series(0.0, index=x.index)
        answered = pd.Series(0, index=x.index, dtype="int64")
        for i, key in enumerate(RAVEN_KEY, 1):
            v = pd.to_numeric(x[lower[f"p{i}"]], errors="coerce")
            valid = v.notna() & ~v.isin([-9, -8, -7])
            score = score + (v.eq(key) & valid).astype(float)
            answered = answered + valid.astype("int64")
        score = score.where(answered.gt(0))
        rr = pd.DataFrame({"codest": x[cod], "raven_r2": score})
        return rr, path
    return None, None


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

    p_lists = locate(root, "listas_final.dta")
    p_pairs = locate(root, "school_pairs_final.dta")
    p_r1 = locate(root, "cestudiante_g3-6_p2_r1.dta")
    p_r2 = locate(root, "cestudiante_g3-6_p2_r2.dta")
    files = [p_lists, p_pairs, p_r1, p_r2]
    inventory = [{"path": str(p), "sha256": sha256_file(p), "bytes": p.stat().st_size} for p in files]

    lists, _ = read_dta(p_lists)
    pairs, _ = read_dta(p_pairs)
    r1, _ = read_dta(p_r1)
    r2raw, _ = read_dta(p_r2)
    for c in ["codest", "participated_in_lottery", "won_lottery", "received_laptop", "treatment_school"]:
        resolve_col(lists, c)
    for c in ["pair", "treatment_school"]:
        resolve_col(pairs, c)

    # Canonicalise source keys case-insensitively.
    lists = lists.rename(columns={resolve_col(lists, "codest"): "codest"})
    r1 = r1.rename(columns={resolve_col(r1, "codest"): "codest"})
    r2raw = r2raw.rename(columns={resolve_col(r2raw, "codest"): "codest"})
    assignment_cols = ["codest", "participated_in_lottery", "won_lottery", "received_laptop", "treatment_school"]
    r1 = r1.merge(lists[assignment_cols], on="codest", how="left", validate="one_to_one")
    if r1["won_lottery"].isna().any():
        raise RuntimeError("ASSIGNMENT_LINK_FAIL")

    # Baseline T_acc,0.
    baseline_cols = ["P2", "P3", "P4"] + [f"P12_A{i}" for i in range(1, 9)]
    for c in baseline_cols:
        resolve_col(r1, c)
    for c, outc in [("P2", "Tacc0_resource_computer"), ("P3", "Tacc0_resource_internet"), ("P4", "Tacc0_resource_prior_use")]:
        r1[outc] = binary_yes(r1[c])
    cap_cols = []
    for i in range(1, 9):
        nc = f"Tacc0_cap_A{i}"
        r1[nc] = binary_yes(r1[f"P12_A{i}"])
        cap_cols.append(nc)
    r1["Tacc0_capacity_count"] = r1[cap_cols].sum(axis=1, min_count=1)

    # Post-treatment accessibility is strictly R2 P1-P3.
    for c in ["P1", "P2", "P3"]:
        resolve_col(r2raw, c)
    r2 = r2raw[["codest", "P1", "P2", "P3", "P7"] +
               [f"P4_A{i}" for i in range(1, 6)] + [f"P4_B{i}" for i in range(1, 6)] +
               [f"P5_A{i}" for i in range(1, 6)] + [f"P6_A{i}" for i in range(1, 5)]].copy()
    for c, outc in [("P1", "Tacc1_resource_computer"), ("P2", "Tacc1_resource_internet"), ("P3", "Tacc1_resource_prior_use")]:
        r2[outc] = binary_yes(r2[c])

    if r1["codest"].duplicated().any() or r2["codest"].duplicated().any():
        raise RuntimeError("NON_UNIQUE_STUDENT_KEY")
    d = r1.merge(r2, on="codest", how="inner", validate="one_to_one")
    for c in ["won_lottery", "received_laptop", "treatment_school"]:
        d[c] = pd.to_numeric(d[c], errors="coerce")
    d["Z"] = d["won_lottery"].where(d["won_lottery"].isin([0, 1]))
    d["delta_computer"] = d["Tacc1_resource_computer"] - d["Tacc0_resource_computer"]
    d["delta_internet"] = d["Tacc1_resource_internet"] - d["Tacc0_resource_internet"]
    d["delta_prior_use"] = d["Tacc1_resource_prior_use"] - d["Tacc0_resource_prior_use"]
    d["delta_resource_count"] = d[["Tacc1_resource_computer", "Tacc1_resource_internet", "Tacc1_resource_prior_use"]].sum(axis=1, min_count=1) - d[["Tacc0_resource_computer", "Tacc0_resource_internet", "Tacc0_resource_prior_use"]].sum(axis=1, min_count=1)

    # Published downstream transformation.
    traj, trajectory_variables = derive_trajectory(d)
    d = traj

    # Reconstruct the published Raven score, with no inference of answer keys.
    raven, raven_path = build_raven(root)
    if raven is None:
        raise RuntimeError("RAVEN_RECONSTRUCTION_INPUT_NOT_FOUND")
    if raven["codest"].duplicated().any():
        raise RuntimeError("RAVEN_NON_UNIQUE_STUDENT_KEY")
    d = d.merge(raven, on="codest", how="left", validate="one_to_one")
    if d["raven_r2"].dropna().empty:
        raise RuntimeError("RAVEN_RECONSTRUCTION_EMPTY")
    if not bool(d["raven_r2"].dropna().between(0, 36).all()):
        raise RuntimeError("RAVEN_OUT_OF_RANGE")

    contrasts = {
        "Z_to_delta_computer": mean_diff(d, "delta_computer", "Z"),
        "Z_to_delta_internet": mean_diff(d, "delta_internet", "Z"),
        "Z_to_delta_prior_use": mean_diff(d, "delta_prior_use", "Z"),
        "Z_to_delta_resource_count": mean_diff(d, "delta_resource_count", "Z"),
    }
    for c in trajectory_variables:
        contrasts[f"Z_to_{c}"] = mean_diff(d, c, "Z")
    contrasts["Z_to_raven_r2"] = mean_diff(d, "raven_r2", "Z")

    pair_col = resolve_col(pairs, "pair")
    treatment_col = resolve_col(pairs, "treatment_school")
    pair_counts = pairs.groupby(pair_col)[treatment_col].agg(["count", "sum"])
    pair_valid = bool((pair_counts["count"] == 2).all() and (pair_counts["sum"] == 1).all())
    identity = {
        "Z_definition": "won_lottery",
        "receipt_definition": "received_laptop",
        "school_condition_definition": "treatment_school",
        "Z_not_receipt": bool((d["Z"].fillna(-1) != d["received_laptop"].fillna(-2)).any()),
        "school_pair_structure_valid": pair_valid,
    }

    first_stage = any(v["diff"] is not None and abs(v["diff"]) > 0 for k, v in contrasts.items() if k.startswith("Z_to_delta_"))
    trajectory_present = any(v["diff"] is not None and abs(v["diff"]) > 0 for k, v in contrasts.items() if k.startswith("Z_to_trajectory_"))
    if not first_stage:
        verdict = "FAIL"
        note = "No measurable bounded accessibility change was reconstructed from Z in the tested indicators."
    else:
        verdict = "PARTIAL/INCONCLUSIVE"
        note = "The experiment reconstructs the bounded accessibility transition and downstream trajectory contrasts, but does not infer an accessibility-mediated causal effect without an explicit identification/exclusion argument."

    result = {
        "spec": SPEC,
        "status": verdict,
        "causal_note": note,
        "data_root": str(root),
        "inventory": inventory,
        "environment": {"python": sys.version, "platform": platform.platform(), "pandas": pd.__version__, "pyreadstat": getattr(pyreadstat, "__version__", "unknown")},
        "n": {"lists": int(len(lists)), "r1": int(len(r1)), "r2": int(len(r2)), "paired_r1_r2": int(len(d))},
        "identity": identity,
        "trajectory_variables": trajectory_variables,
        "trajectory_source_semantics": "Published input_r2.do transformations for P4/P5/P6/P7",
        "raven_source": str(raven_path),
        "raven_key": RAVEN_KEY,
        "raven_definition": "sum of 36 keyed item indicators; missing/nonresponse not counted; observed score constrained to [0,36]",
        "contrasts": contrasts,
        "first_stage_present": first_stage,
        "trajectory_contrast_present": trajectory_present,
        "output_schema": list(d.columns),
    }
    result_path = out / "C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_RESULT_001.json"
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    result["result_sha256"] = sha256_file(result_path)
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")

    export_cols = ["codest", "Z", "received_laptop", "treatment_school", "Tacc0_capacity_count", "Tacc0_resource_computer", "Tacc0_resource_internet", "Tacc0_resource_prior_use", "Tacc1_resource_computer", "Tacc1_resource_internet", "Tacc1_resource_prior_use", "delta_computer", "delta_internet", "delta_prior_use", "delta_resource_count"] + trajectory_variables + ["raven_r2"]
    audit_df = d[[c for c in export_cols if c in d.columns]].copy()
    audit_path = out / "C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_AUDIT_DATA_001.csv"
    audit_df.to_csv(audit_path, index=False)
    log_path = out / "C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_EXECUTION_LOG_001.txt"
    log_path.write_text(f"SPEC={SPEC}\nSTATUS={verdict}\nDATA_ROOT={root}\nRESULT={result_path}\nRESULT_SHA256={sha256_file(result_path)}\nAUDIT_DATA_SHA256={sha256_file(audit_path)}\n", encoding="utf-8")
    print(json.dumps({"status": verdict, "result": str(result_path), "audit_data": str(audit_path), "log": str(log_path)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
