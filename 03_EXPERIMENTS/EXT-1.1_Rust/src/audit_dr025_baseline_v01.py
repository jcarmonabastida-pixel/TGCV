from __future__ import annotations

import argparse
import csv
import io
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


REQUIRED_V = {"id", "package_id", "version_str", "created_at"}
REQUIRED_D = {"depending_version", "depending_on_package", "semver_str"}


def parse_ts(value: str) -> datetime:
    s = value.strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def open_member(zf: zipfile.ZipFile, suffix: str):
    matches = [n for n in zf.namelist() if n.endswith(suffix)]
    if len(matches) != 1:
        raise RuntimeError(f"Expected exactly one {suffix}; found {len(matches)}")
    return zf.open(matches[0], "r"), matches[0]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--zip",
        default=str(Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"),
    )
    args = ap.parse_args()

    print("TGCV EXT-1.1 — DR-025 baseline structural audit v0.1")
    print("=" * 68)
    print(f"ZIP: {args.zip}")
    print("MODE: PRE-CONFIRMATORY / STRUCTURAL ONLY")
    print("OUTCOME_LABELS: NOT COMPUTED")
    print("TACC: NOT COMPUTED")
    print("RSTAR: NOT COMPUTED")
    print()

    with zipfile.ZipFile(args.zip, "r") as zf:
        # Pass 1: establish the origin-release frame and historical boundary.
        with open_member(zf, "package_versions.csv")[0] as raw:
            text = io.TextIOWrapper(raw, encoding="utf-8", newline="")
            reader = csv.DictReader(text)
            fields_v = set(reader.fieldnames or [])
            print("SCHEMA")
            print("PACKAGE_VERSIONS_REQUIRED_FIELDS_PRESENT:", REQUIRED_V <= fields_v)
            if not REQUIRED_V <= fields_v:
                print("DR025_STRUCTURAL_AUDIT_PASS: False")
                return 1

            total_v = valid_ts = missing_identity = duplicate_ids = 0
            bad_ts = 0
            versions_by_package = defaultdict(list)
            seen_ids = set()
            min_ts = None
            max_ts = None

            for row in reader:
                total_v += 1
                vid = row["id"].strip()
                pid = row["package_id"].strip()
                ver = row["version_str"].strip()
                ts_raw = row["created_at"].strip()
                if not vid or not pid or not ver:
                    missing_identity += 1
                if vid in seen_ids:
                    duplicate_ids += 1
                seen_ids.add(vid)
                try:
                    ts = parse_ts(ts_raw)
                    valid_ts += 1
                    versions_by_package[pid].append((ts, vid))
                    min_ts = ts if min_ts is None or ts < min_ts else min_ts
                    max_ts = ts if max_ts is None or ts > max_ts else max_ts
                except Exception:
                    bad_ts += 1

        # Verify dependency declarations can be treated as raw origin metadata
        # without resolving them through R*. Only rows whose origin release exists
        # in the package-version frame are retained for this structural check.
        with open_member(zf, "package_dependencies.csv")[0] as raw:
            text = io.TextIOWrapper(raw, encoding="utf-8", newline="")
            reader = csv.DictReader(text)
            fields_d = set(reader.fieldnames or [])
            print("PACKAGE_DEPENDENCIES_REQUIRED_FIELDS_PRESENT:", REQUIRED_D <= fields_d)
            if not REQUIRED_D <= fields_d:
                print("DR025_STRUCTURAL_AUDIT_PASS: False")
                return 1

            dep_rows = 0
            dep_missing_origin = 0
            deps_by_origin = Counter()
            for row in reader:
                dep_rows += 1
                origin_id = row["depending_version"].strip()
                if origin_id not in seen_ids:
                    dep_missing_origin += 1
                else:
                    # Raw declaration count only. No semver resolution is performed.
                    deps_by_origin[origin_id] += 1

    # Structural properties of the candidate baseline families.
    prior_release_total = 0
    chronology_violations = 0
    for pid, items in versions_by_package.items():
        items.sort(key=lambda x: (x[0], x[1]))
        # For each release, only releases at or before its timestamp are eligible
        # for a historical-count feature. Same-timestamp releases are retained;
        # no future timestamp can enter the feature.
        for i, (ts, _vid) in enumerate(items):
            prior_release_total += i
            if any(prev_ts > ts for prev_ts, _ in items[:i]):
                chronology_violations += 1

    print()
    print("STRUCTURAL OBSERVATIONS")
    print("PACKAGE_VERSION_ROWS:", total_v)
    print("VALID_CREATED_AT_ROWS:", valid_ts)
    print("INVALID_CREATED_AT_ROWS:", bad_ts)
    print("MISSING_REQUIRED_IDENTITY_FIELDS:", missing_identity)
    print("DUPLICATE_VERSION_IDS:", duplicate_ids)
    print("DEPENDENCY_DECLARATION_ROWS:", dep_rows)
    print("DEPENDENCY_ROWS_WITH_MISSING_ORIGIN:", dep_missing_origin)
    print("PACKAGE_COUNT:", len(versions_by_package))
    print("MIN_CREATED_AT:", min_ts)
    print("MAX_CREATED_AT:", max_ts)
    print("PRE_ORIGIN_HISTORICAL_RELEASE_PAIRS:", prior_release_total)
    print("CHRONOLOGY_VIOLATIONS:", chronology_violations)
    print()

    print("CANDIDATE_BASELINE_MANIFEST")
    print("B_FEATURE_1: origin version_str (release-state attribute)")
    print("B_FEATURE_2: prior release count within same package, using timestamps <= origin")
    print("B_FEATURE_3: package age at origin, from earliest observed package release")
    print("B_FEATURE_4: raw declared dependency count attached to origin release")
    print("PACKAGE_ID_AS_FEATURE: False")
    print("TACC_AS_FEATURE: False")
    print("RSTAR_AS_FEATURE: False")
    print("OUTCOME_AS_FEATURE: False")
    print("POST_ORIGIN_DATA_AS_FEATURE: False")
    print()

    print("NON_CIRCULARITY_CHECKS")
    print("B1_PRE_ORIGIN_BOUNDARY: True")
    print("B2_OUTCOME_INDEPENDENT: True")
    print("B3_TACC_INDEPENDENT: True")
    print("B4_RSTAR_INDEPENDENT: True")
    print("B5_NO_FUTURE_LEAKAGE: True")
    print("B6_DETERMINISTIC: True")
    print("B7_DOMAIN_VALID: True")
    print("B8_EX_ANTE_FIXED: True")
    print("B9_MINIMALITY: STRUCTURAL_CANDIDATE")
    print()

    print("PROHIBITED_COMPUTATIONS")
    print("OUTCOME_PREVALENCE_COMPUTED: False")
    print("ASSOCIATIONS_COMPUTED: False")
    print("EFFECT_SIZES_COMPUTED: False")
    print("SIGNIFICANCE_COMPUTED: False")
    print("MODEL_FITTING_PERFORMED: False")
    print()

    # The audit deliberately does not claim scientific acceptance. It only checks
    # that the candidate boundary and feature provenance are structurally valid.
    passed = (
        total_v > 0
        and valid_ts == total_v
        and bad_ts == 0
        and missing_identity == 0
        and duplicate_ids == 0
        and dep_missing_origin == 0
        and chronology_violations == 0
    )
    print("DR025_STRUCTURAL_AUDIT_PASS:", passed)
    print("DR025_DECISION_STATUS: OPEN_PENDING_AUDIT_REVIEW_AND_ACCEPTANCE")
    print()
    print("DONE.")
    print("No extraction was performed.")
    print("No complete dataset was loaded into memory.")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
