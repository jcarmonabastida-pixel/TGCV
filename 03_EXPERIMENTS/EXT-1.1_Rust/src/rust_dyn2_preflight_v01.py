#!/usr/bin/env python3
"""RUST-DYN-2 input/schema preflight; never executes the experiment."""
import argparse, hashlib, json, platform, sys, zipfile

DATASET_SHA256 = "823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224"
VERSIONS_MEMBER = "rust_repos_2022_09_07/dumps/postgresql/data/package_versions.csv"
DEPENDENCIES_MEMBER = "rust_repos_2022_09_07/dumps/postgresql/data/package_dependencies.csv"
VERSIONS_COLUMNS = {"id", "package_id", "version_str", "created_at"}
DEPENDENCIES_COLUMNS = {"depending_version", "depending_on_package", "semver_str"}
TEMPORAL_RULE_ID = "DR-035-v0.1-ADJACENT-CREATED-AT"
HORIZON = 1


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def header(zf, member):
    with zf.open(member) as f:
        line = f.readline().decode("utf-8-sig").rstrip("\r\n")
    return line.split(",")


def check_member(zf, member, expected):
    names = {n.replace("\\", "/") for n in zf.namelist()}
    present = member in names
    if not present:
        return {"member": member, "present": False, "schema_pass": False, "header": [], "missing_expected": sorted(expected), "duplicate_columns": []}
    cols = header(zf, member)
    return {"member": member, "present": True, "header": cols,
            "missing_expected": sorted(expected - set(cols)),
            "duplicate_columns": sorted({x for x in cols if cols.count(x) > 1}),
            "schema_pass": set(cols) == expected and len(cols) == len(set(cols))}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dataset", required=True)
    a = p.parse_args()
    digest = sha256(a.dataset)
    result = {
        "MODE": "RUST_DYN_2_REAL_DATA_PREFLIGHT_ONLY",
        "dataset_path": a.dataset,
        "dataset_sha256": digest,
        "expected_dataset_sha256": DATASET_SHA256,
        "temporal_rule_id": TEMPORAL_RULE_ID,
        "horizon": HORIZON,
        "python": sys.version,
        "platform": platform.platform(),
        "zip_opened": False,
        "package_versions": {}, "package_dependencies": {},
        "tacc_constructed": False, "delta_tacc_computed": False,
        "reach_computed": False, "trajectory_computed": False,
        "future_activity_read": False, "outcome_read": False,
        "predictive_metrics": False, "sampling": False,
        "real_dataset_execution": False,
        "execution_authorization": False,
    }
    try:
        with zipfile.ZipFile(a.dataset) as zf:
            result["zip_opened"] = True
            result["package_versions"] = check_member(zf, VERSIONS_MEMBER, VERSIONS_COLUMNS)
            result["package_dependencies"] = check_member(zf, DEPENDENCIES_MEMBER, DEPENDENCIES_COLUMNS)
    except Exception as e:
        result["error"] = f"{type(e).__name__}: {e}"
    result["pass"] = bool(
        result["zip_opened"] and digest == DATASET_SHA256 and
        result["package_versions"].get("schema_pass") is True and
        result["package_dependencies"].get("schema_pass") is True and
        not result["tacc_constructed"] and not result["delta_tacc_computed"] and
        not result["reach_computed"] and not result["trajectory_computed"] and
        not result["future_activity_read"] and not result["outcome_read"] and
        not result["predictive_metrics"] and not result["sampling"] and
        not result["real_dataset_execution"] and not result["execution_authorization"]
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["pass"] else 7

if __name__ == "__main__":
    raise SystemExit(main())
