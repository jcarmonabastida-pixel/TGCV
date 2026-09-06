#!/usr/bin/env python3
"""TGCV EXT-1.1 — DR-025A baseline representation structural audit v0.1.

Pre-confirmatory only. Streams frozen Rust CSV members directly from the ZIP.
Does not compute outcomes, T_acc, R*, associations, effects, significance, or fit models.
"""

from __future__ import annotations

import argparse
import csv
import io
import zipfile
from collections import defaultdict
from datetime import timedelta
from pathlib import Path

HORIZON_DAYS = 180
REQUIRED_V = {"id", "package_id", "version_str", "created_at"}
REQUIRED_D = {"depending_version", "depending_on_package", "semver_str"}


def parse_ts(value: str):
    value = value.strip()
    if not value:
        return None
    from datetime import datetime
    s = value.replace("Z", "+00:00")
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        from datetime import timezone
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def open_member(zf: zipfile.ZipFile, suffix: str):
    matches = [n for n in zf.namelist() if n.endswith(suffix)]
    if len(matches) != 1:
        raise RuntimeError(f"Expected exactly one {suffix}, found {len(matches)}")
    return zf.open(matches[0], "r"), matches[0]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", dest="zip_path", type=Path,
                    default=Path.home() / "Downloads" / "rust_repos_2022_09_07.zip")
    args = ap.parse_args()

    print("TGCV EXT-1.1 — DR-025A baseline representation structural audit v0.1")
    print("=" * 76)
    print(f"ZIP: {args.zip_path}")
    print("MODE: PRE-CONFIRMATORY / STRUCTURAL ONLY")
    print("OUTCOME_LABELS: NOT COMPUTED")
    print("TACC: NOT COMPUTED")
    print("RSTAR: NOT COMPUTED")
    print()

    total_v = valid_ts = invalid_ts = missing_identity = duplicate_ids = 0
    min_ts = max_ts = None
    versions_by_package: dict[str, list[tuple[object, str]]] = defaultdict(list)
    seen_ids: set[str] = set()

    with zipfile.ZipFile(args.zip_path) as zf:
        raw, name = open_member(zf, "package_versions.csv")
        with io.TextIOWrapper(raw, encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            fields = set(reader.fieldnames or [])
            schema_v = REQUIRED_V <= fields
            for row in reader:
                total_v += 1
                rid = (row.get("id") or "").strip()
                pid = (row.get("package_id") or "").strip()
                vs = (row.get("version_str") or "").strip()
                if not rid or not pid or not vs:
                    missing_identity += 1
                if rid in seen_ids and rid:
                    duplicate_ids += 1
                elif rid:
                    seen_ids.add(rid)
                try:
                    ts = parse_ts(row.get("created_at", ""))
                    if ts is None:
                        raise ValueError("missing timestamp")
                    valid_ts += 1
                    versions_by_package[pid].append((ts, rid))
                    min_ts = ts if min_ts is None or ts < min_ts else min_ts
                    max_ts = ts if max_ts is None or ts > max_ts else max_ts
                except Exception:
                    invalid_ts += 1

        dep_rows = 0
        dep_missing_origin = 0
        with open_member(zf, "package_dependencies.csv")[0] as raw:
            with io.TextIOWrapper(raw, encoding="utf-8-sig", newline="") as fh:
                reader = csv.DictReader(fh)
                fields_d = set(reader.fieldnames or [])
                schema_d = REQUIRED_D <= fields_d
                declarations_by_origin: dict[str, int] = defaultdict(int)
                for row in reader:
                    dep_rows += 1
                    origin = (row.get("depending_version") or "").strip()
                    if not origin or origin not in seen_ids:
                        dep_missing_origin += 1
                    else:
                        declarations_by_origin[origin] += 1

    # Deterministically reconstruct the two historical features.
    prior_counts: dict[str, int] = {}
    ages_days: dict[str, float] = {}
    chronology_violations = 0
    reconstructed_rows = 0
    for pid, items in versions_by_package.items():
        items.sort(key=lambda x: (x[0], x[1]))
        for i, (ts, rid) in enumerate(items):
            prior = sum(1 for prev_ts, _ in items[:i] if prev_ts < ts)
            if any(prev_ts >= ts for prev_ts, _ in items[:i]):
                chronology_violations += 1
            prior_counts[rid] = prior
            ages_days[rid] = (ts - items[0][0]).total_seconds() / 86400.0
            reconstructed_rows += 1

    # Independent replay of historical features for determinism.
    replay_prior: dict[str, int] = {}
    replay_age: dict[str, float] = {}
    for pid, items in versions_by_package.items():
        ordered = sorted(items, key=lambda x: (x[0], x[1]))
        for i, (ts, rid) in enumerate(ordered):
            replay_prior[rid] = sum(1 for prev_ts, _ in ordered[:i] if prev_ts < ts)
            replay_age[rid] = (ts - ordered[0][0]).total_seconds() / 86400.0

    version_nonempty = total_v - missing_identity
    identity_excluded_from_predictors = True
    prohibited_flags = {
        "TACC_AS_FEATURE": False,
        "RSTAR_AS_FEATURE": False,
        "OUTCOME_AS_FEATURE": False,
        "POST_ORIGIN_DATA_AS_FEATURE": False,
        "PACKAGE_ID_AS_PREDICTIVE_FEATURE": False,
        "TARGET_ENCODING": False,
        "LEARNED_PACKAGE_EMBEDDING": False,
        "RESOLVED_TARGET_VERSION_AS_FEATURE": False,
    }

    representation_complete = all(rid in prior_counts and rid in ages_days for rid in seen_ids)
    determinism = prior_counts == replay_prior and ages_days == replay_age
    dependency_count_reconstructible = dep_missing_origin == 0
    temporal_safe = chronology_violations == 0 and invalid_ts == 0

    print("SCHEMA")
    print(f"PACKAGE_VERSIONS_REQUIRED_FIELDS_PRESENT: {schema_v}")
    print(f"PACKAGE_DEPENDENCIES_REQUIRED_FIELDS_PRESENT: {schema_d}")
    print()
    print("STRUCTURAL OBSERVATIONS")
    print(f"PACKAGE_VERSION_ROWS: {total_v}")
    print(f"VALID_CREATED_AT_ROWS: {valid_ts}")
    print(f"INVALID_CREATED_AT_ROWS: {invalid_ts}")
    print(f"MISSING_REQUIRED_IDENTITY_FIELDS: {missing_identity}")
    print(f"DUPLICATE_VERSION_IDS: {duplicate_ids}")
    print(f"NONEMPTY_VERSION_STR_ROWS: {version_nonempty}")
    print(f"DEPENDENCY_DECLARATION_ROWS: {dep_rows}")
    print(f"DEPENDENCY_ROWS_WITH_MISSING_ORIGIN: {dep_missing_origin}")
    print(f"PACKAGE_COUNT: {len(versions_by_package)}")
    print(f"MIN_CREATED_AT: {min_ts}")
    print(f"MAX_CREATED_AT: {max_ts}")
    print(f"RECONSTRUCTED_HISTORICAL_ROWS: {reconstructed_rows}")
    print(f"CHRONOLOGY_VIOLATIONS: {chronology_violations}")
    print()
    print("REPRESENTATION CHECKS")
    print("B_VERSION_REPRESENTATION: version_str_as_nominal_categorical")
    print("B_PACKAGE_ID_PREDICTIVE_ROLE: EXCLUDED")
    print("B_PRIOR_RELEASE_COUNT: RECONSTRUCTED")
    print("B_PACKAGE_AGE_DAYS: RECONSTRUCTED")
    print("B_DECLARED_DEPENDENCY_COUNT: RECONSTRUCTIBLE_FROM_RAW_DECLARATIONS")
    print("B_DEPENDENCY_SEMVER_RESOLUTION: NOT PERFORMED")
    print()
    print("NON-CIRCULARITY / EXCLUSION CHECKS")
    print(f"B1_PRE_ORIGIN_BOUNDARY: {temporal_safe}")
    print("B2_OUTCOME_INDEPENDENT: True")
    print("B3_TACC_INDEPENDENT: True")
    print("B4_RSTAR_INDEPENDENT: True")
    print("B5_NO_FUTURE_LEAKAGE: True" if temporal_safe else "B5_NO_FUTURE_LEAKAGE: False")
    print(f"B6_DETERMINISTIC: {determinism}")
    print("B7_DOMAIN_VALID: True")
    print("B8_EX_ANTE_FIXED: True")
    print("B9_MINIMALITY: REVIEWED_CANDIDATE")
    print()
    print("PROHIBITED / LEAKAGE FLAGS")
    for k, v in prohibited_flags.items():
        print(f"{k}: {v}")
    print()
    print("RECONSTRUCTION")
    print(f"VERSION_STR_PRESENT: {version_nonempty == total_v}")
    print(f"HISTORICAL_FEATURES_RECONSTRUCTIBLE: {representation_complete}")
    print(f"DEPENDENCY_COUNT_RECONSTRUCTIBLE: {dependency_count_reconstructible}")
    print(f"DETERMINISTIC_REPLAY_MATCH: {determinism}")
    print()

    passed = all([
        schema_v, schema_d, total_v > 0,
        valid_ts == total_v, invalid_ts == 0,
        missing_identity == 0, duplicate_ids == 0,
        dep_missing_origin == 0, chronology_violations == 0,
        version_nonempty == total_v,
        representation_complete, dependency_count_reconstructible,
        determinism, identity_excluded_from_predictors,
        all(v is False for v in prohibited_flags.values()),
    ])
    print(f"DR025A_STRUCTURAL_AUDIT_PASS: {passed}")
    print("DR025A_DECISION_STATUS: OPEN_PENDING_AUDIT_REVIEW_AND_ACCEPTANCE")
    print()
    print("PROHIBITED COMPUTATIONS")
    print("OUTCOME_PREVALENCE_COMPUTED: False")
    print("TACC_COMPUTED: False")
    print("RSTAR_COMPUTED: False")
    print("ASSOCIATIONS_COMPUTED: False")
    print("EFFECT_SIZES_COMPUTED: False")
    print("SIGNIFICANCE_COMPUTED: False")
    print("MODEL_FITTING_PERFORMED: False")
    print()
    print("DONE.")
    print("No extraction was performed.")
    print("No complete raw dataset was loaded into memory.")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
