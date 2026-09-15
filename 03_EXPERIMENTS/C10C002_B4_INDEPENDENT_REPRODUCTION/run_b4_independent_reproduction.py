"""C10C-002 B4 independent reproduction verifier.

This script performs deterministic reconstruction checks only. It does NOT run
causal estimation and must not consume historical T17 results.

Usage:
  python run_b4_independent_reproduction.py <extracted_V1_directory> <output_json>
"""
from __future__ import annotations

import hashlib
import json
import platform
import sys
from pathlib import Path

import pandas as pd

ZIP_SHA256 = "D481DF2CCD6D677E81D1F0CD80AF27F24A111515BB6D1E9844D1DE6483A1DFC8"
B4_SPEC_GIT_BLOB_SHA = "90d9795666031ed1afeca1a68ab6157216fee2fd"
REQUIRED = {
    "Encuestas-2012.docx": "CD3947BAE112CEBE83783C241B18C06783FE31D0101D2C50C155761A512EC1A6",
    "Habitat_Household_Analysis_Replication_170830.do": "9C2F010725DCD60B090438137D155C8AC629D9AC185E3F22430C43DF46E4F3AF",
    "Habitat_Household_Data_for_Replication.dta": "B080612908BDD45BD8B44B2A42F94E92CCAFCF776DE5379BD6DAB2B054469C55",
    "Habitat_Household_Data_for_Replication.xlsx": "6E2E72DA1386F76DA7750CC0DCCCC73D9F74E0FF416C3178D85ABF9463E62B84",
    "Habitat_Real_Estate_Replication_170830.do": "383531C1C9CC64D4AC772E4518E35B5DC66429369974A4CD1E23B0B08702B67D",
    "ReadMe.txt": "AA2053E1745DE8CF1C04A6A49EECF7C642BA75468F24CDB3AA7FBB024CF8A443",
    "real_estate_polygon_level.dta": "428560B2976FBBFB77CD7669F476262FA9AF9F6CD1B7C578D45E95456884B494",
    "real_estate_polygon_level.xlsx": "5F962319AD9C22814C9C342E87237F5BFE5C191C38BD6D82451C5D1C82D58BEF",
}
DIMS = ["Disp_Agua", "Disp_Drenaje", "Disp_Luz", "Disp_Guarniciones", "Disp_Banquetas", "Disp_Pavimento"]
FORBIDDEN = ["sat", "sat_treat", "r2", "treat_r2"]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def clean(v):
    try:
        if pd.isna(v):
            return None
        return int(v)
    except Exception:
        return None


def collapse_polygon_round(g, dimensions):
    """Conservatively collapse repeated household rows to polygon x round.

    A structural value is admitted only when all non-missing observations
    within a polygon-round agree on the same binary state. No arbitrary row,
    treatment value, or outcome value is selected.
    """
    state = {}
    conflicts = {}
    for d in dimensions:
        vals = sorted({clean(v) for v in g[d].tolist() if clean(v) is not None})
        invalid = [v for v in vals if v not in (0, 1)]
        if invalid:
            conflicts[d] = {"reason": "non_binary", "values": vals}
        elif len(vals) > 1:
            conflicts[d] = {"reason": "intra_polygon_round_conflict", "values": vals}
        else:
            state[d] = vals[0] if vals else None
    return state, conflicts


def main(root: Path, out: Path) -> int:
    script_path = Path(__file__).resolve()
    result = {
        "status": "B4_INDEPENDENT_REPRODUCTION",
        "causal_estimation": "NOT_PERFORMED",
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "pandas": pd.__version__,
        },
        "governance_hashes": {
            "source_zip_sha256": ZIP_SHA256,
            "b4_specification_git_blob_sha": B4_SPEC_GIT_BLOB_SHA,
            "verifier_script_sha256": sha256(script_path),
        },
        "checks": {},
    }

    hashes = {}
    hash_ok = True
    for name, expected in REQUIRED.items():
        p = root / name
        if not p.exists():
            hashes[name] = {"exists": False, "expected": expected}
            hash_ok = False
            continue
        actual = sha256(p)
        hashes[name] = {"exists": True, "actual": actual, "expected": expected, "match": actual == expected}
        hash_ok &= actual == expected
    result["checks"]["input_hashes"] = {"pass": hash_ok, "files": hashes}
    if not hash_ok:
        result["status"] = "B4_BLOCKED_INPUT_HASH_MISMATCH"
        out.write_text(json.dumps(result, indent=2), encoding="utf-8")
        return 2

    dta = root / "Habitat_Household_Data_for_Replication.dta"
    re_dta = root / "real_estate_polygon_level.dta"
    df = pd.read_stata(dta, convert_categoricals=False)
    re = pd.read_stata(re_dta, convert_categoricals=False)

    required_cols = ["N_POLIGONO", "round", "sample_PANEL", "treat", "cve_mun", *DIMS]
    missing = [c for c in required_cols if c not in df.columns]
    result["checks"]["household_required_columns"] = {"pass": not missing, "missing": missing}
    if missing:
        result["status"] = "B4_BLOCKED_MISSING_REQUIRED_COLUMNS"
        out.write_text(json.dumps(result, indent=2), encoding="utf-8")
        return 3

    panel = df.loc[df["sample_PANEL"] == 1].copy()
    panel_ids = set(panel["N_POLIGONO"].dropna().astype(str))
    re_ids = set(re["N_POLIGONO"].dropna().astype(str))
    linkage_ok = len(panel_ids) == 342 and len(re_ids) == 342 and panel_ids == re_ids
    result["checks"]["panel_linkage"] = {
        "pass": linkage_ok,
        "panel_polygons": len(panel_ids),
        "real_estate_polygons": len(re_ids),
        "intersection": len(panel_ids & re_ids),
    }

    panel["N_POLIGONO_STR"] = panel["N_POLIGONO"].astype(str)
    rounds = sorted(panel["round"].dropna().unique().tolist())
    if len(rounds) < 2:
        result["checks"]["rounds"] = {"pass": False, "rounds": rounds}
        result["status"] = "B4_BLOCKED_ROUND_RECONSTRUCTION"
        out.write_text(json.dumps(result, indent=2), encoding="utf-8")
        return 4
    r0, r1 = rounds[0], rounds[-1]

    states = {}
    conflicts = {}
    delta_counts = {"opening": 0, "closing": 0, "nonempty_delta": 0}
    for pid, g in panel.groupby("N_POLIGONO_STR"):
        g0 = g.loc[g["round"] == r0]
        g1 = g.loc[g["round"] == r1]
        if g0.empty or g1.empty:
            continue
        s0, c0 = collapse_polygon_round(g0, DIMS)
        s1, c1 = collapse_polygon_round(g1, DIMS)
        if c0 or c1:
            conflicts[pid] = {"round_0": c0, "round_1": c1}
            continue
        t0 = {f"{d}+" for d in DIMS if s0[d] is not None and s0[d] < 1}
        t0 |= {f"{d}-" for d in DIMS if s0[d] is not None and s0[d] > 0}
        t1 = {f"{d}+" for d in DIMS if s1[d] is not None and s1[d] < 1}
        t1 |= {f"{d}-" for d in DIMS if s1[d] is not None and s1[d] > 0}
        op = t1 - t0
        cl = t0 - t1
        delta_counts["opening"] += len(op)
        delta_counts["closing"] += len(cl)
        if op or cl:
            delta_counts["nonempty_delta"] += 1
        states[pid] = {"T_acc_0": sorted(t0), "T_acc_1": sorted(t1), "Delta_open": sorted(op), "Delta_close": sorted(cl)}

    structural_pass = len(states) == 342 and not conflicts and all(
        len(v["T_acc_0"]) <= 12 and len(v["T_acc_1"]) <= 12 for v in states.values()
    )
    result["checks"]["bounded_structural_reconstruction"] = {
        "pass": structural_pass,
        "polygons_reconstructed": len(states),
        "dimensions": DIMS,
        "transformation_count": 12,
        "aggregation_rule": "polygon x round; retain a structural value only when all non-missing observations agree on the same binary state; conflicting groups are excluded, never resolved arbitrarily",
        "conflicting_polygon_rounds": len(conflicts),
        "delta_counts": delta_counts,
        "rounds": [r0, r1],
    }
    if conflicts:
        result["checks"]["bounded_structural_reconstruction"]["conflict_examples"] = dict(list(conflicts.items())[:10])

    treatment_ok = "treat" in panel.columns and set(pd.to_numeric(panel["treat"], errors="coerce").dropna().unique()).issubset({0, 1})
    result["checks"]["treatment_state_separation"] = {"pass": treatment_ok, "treat_counts": panel["treat"].value_counts(dropna=False).to_dict()}

    endpoint_ok = "precios_diferencia_usd" in re.columns and "any_precio" in re.columns
    coverage = int((re["any_precio"] == 1).sum()) if endpoint_ok else None
    result["checks"]["endpoint_linkage"] = {"pass": endpoint_ok and coverage == 138, "observed": coverage, "universe": len(re)}

    forbidden_present = {c: c in panel.columns for c in FORBIDDEN}
    result["checks"]["forbidden_saturation_exclusion"] = {"pass": True, "fields_present_but_not_used_in_predicates": forbidden_present}

    result["checks"]["causal_estimation"] = {"pass": True, "performed": False, "reason": "B4 is reproduction only; no regression is executed."}
    result["reconstruction_digest"] = hashlib.sha256(json.dumps(states, sort_keys=True).encode()).hexdigest()

    all_pass = all(
        v.get("pass", False)
        for k, v in result["checks"].items()
        if isinstance(v, dict) and "pass" in v and k != "causal_estimation"
    )
    result["overall"] = "PASS_B4_REPRODUCTION_CHECKS" if all_pass else "B4_REPRODUCTION_CHECKS_REQUIRE_REVIEW"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0 if all_pass else 5


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python run_b4_independent_reproduction.py <V1_DIR> <OUTPUT_JSON>")
        raise SystemExit(1)
    raise SystemExit(main(Path(sys.argv[1]), Path(sys.argv[2])))
