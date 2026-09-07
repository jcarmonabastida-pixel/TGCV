#!/usr/bin/env python3
"""TGCV Rust Dataset Temporal Semantics Audit v0.1.

OUTCOME-BLIND / SCHEMA-ONLY / PRE-REDESIGN.

Purpose: inspect the retained Rust dataset for observable temporal and
state/condition fields that could legitimately support a time-varying
accessibility predicate. This script MUST NOT compute T_acc, Delta T_acc,
outcomes, models, or value.

It inventories CSV schemas and basic field-level temporal characteristics.
It does not interpret a field as an accessibility condition.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import zipfile
from collections import Counter
from pathlib import Path

DEFAULT_ZIP = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"
EXPECTED_CSVS = [
    "packages.csv",
    "package_versions.csv",
    "package_dependencies.csv",
]

TEMPORAL_NAME_TOKENS = (
    "created", "updated", "deleted", "yank", "time", "date", "timestamp",
    "published", "released", "valid", "start", "end", "from", "to",
)
STATE_NAME_TOKENS = (
    "status", "state", "active", "yanked", "deleted", "available", "valid",
    "enabled", "disabled", "deprecated", "removed",
)
OUTCOME_NAME_TOKENS = (
    "outcome", "success", "activity", "score", "value", "target", "label",
    "future", "subsequent",
)


def member_by_basename(zf: zipfile.ZipFile, basename: str) -> str:
    matches = [
        n for n in zf.namelist()
        if n.replace("\\", "/").rsplit("/", 1)[-1] == basename
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"ARCHIVE_MEMBER_RESOLUTION_ERROR: {basename}: found {len(matches)}"
        )
    return matches[0]


def parse_ts(value: str):
    value = value.strip()
    if not value:
        return None
    candidates = [value, value.replace("Z", "+00:00")]
    for candidate in candidates:
        try:
            return dt.datetime.fromisoformat(candidate).replace(tzinfo=None)
        except ValueError:
            pass
    return None


def read_header(zf: zipfile.ZipFile, basename: str) -> list[str]:
    member = member_by_basename(zf, basename)
    with zf.open(member, "r") as raw:
        text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
        reader = csv.reader(text)
        return next(reader, [])


def field_categories(name: str) -> list[str]:
    low = name.lower()
    categories = []
    if any(token in low for token in TEMPORAL_NAME_TOKENS):
        categories.append("TEMPORAL_CANDIDATE")
    if any(token in low for token in STATE_NAME_TOKENS):
        categories.append("STATE_CONDITION_CANDIDATE")
    if any(token in low for token in OUTCOME_NAME_TOKENS):
        categories.append("POTENTIAL_LEAKAGE_OR_OUTCOME_FIELD")
    return categories


def inspect_column(
    zf: zipfile.ZipFile,
    basename: str,
    field: str,
    max_rows: int,
) -> dict:
    member = member_by_basename(zf, basename)
    total = 0
    nonempty = 0
    distinct = set()
    temporal_valid = 0
    temporal_min = None
    temporal_max = None
    numeric = 0
    booleanish = 0
    samples = []

    with zf.open(member, "r") as raw:
        text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
        reader = csv.DictReader(text)
        for row in reader:
            total += 1
            value = (row.get(field) or "").strip()
            if value:
                nonempty += 1
                if len(distinct) < 50000:
                    distinct.add(value)
                if len(samples) < 5:
                    samples.append(value)
                if value.lower() in {"0", "1", "true", "false", "yes", "no"}:
                    booleanish += 1
                try:
                    float(value)
                    numeric += 1
                except ValueError:
                    pass
                parsed = parse_ts(value)
                if parsed is not None:
                    temporal_valid += 1
                    temporal_min = parsed if temporal_min is None else min(temporal_min, parsed)
                    temporal_max = parsed if temporal_max is None else max(temporal_max, parsed)
            if total >= max_rows:
                break

    return {
        "field": field,
        "categories": field_categories(field),
        "rows_inspected": total,
        "nonempty": nonempty,
        "distinct_values_capped": len(distinct),
        "numeric_like": numeric,
        "booleanish_like": booleanish,
        "parseable_iso_datetime": temporal_valid,
        "datetime_min": temporal_min.isoformat() if temporal_min else None,
        "datetime_max": temporal_max.isoformat() if temporal_max else None,
        "samples": samples,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="TGCV Rust dataset temporal semantics audit v0.1")
    ap.add_argument("--zip", default=str(DEFAULT_ZIP))
    ap.add_argument("--max-rows-per-field", type=int, default=200000)
    args = ap.parse_args()
    zip_path = Path(args.zip)

    print("TGCV — Rust Dataset Temporal Semantics Audit v0.1")
    print("=" * 78)
    print(f"ZIP: {zip_path}")
    print("MODE: OUTCOME-BLIND / SCHEMA-ONLY / PRE-REDESIGN")
    print("TACC_COMPUTED: False")
    print("DELTA_TACC_COMPUTED: False")
    print("OUTCOME_COMPUTED: False")
    print("MODEL_FITTED: False")
    print("VALUE_COMPUTED: False")
    print("\nFIELD INTERPRETATION RULE: name-based flags are candidates only; no field is accepted as semantic accessibility evidence by this audit.")

    if not zip_path.exists():
        print("FAIL_DATASET_NOT_FOUND: True")
        return 2

    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            names = zf.namelist()
            archive_sha = hashlib.sha256()
            for name in sorted(names):
                archive_sha.update(name.encode("utf-8") + b"\n")
            print(f"ARCHIVE_MEMBER_MANIFEST_SHA256: {archive_sha.hexdigest()}")

            basename_map = {}
            for basename in EXPECTED_CSVS:
                basename_map[basename] = member_by_basename(zf, basename)

            print("\nSCHEMA INVENTORY")
            report = {"zip": str(zip_path), "files": {}}
            for basename in EXPECTED_CSVS:
                header = read_header(zf, basename)
                report["files"][basename] = {"member": basename_map[basename], "fields": header}
                print(f"{basename}: {len(header)} fields")
                print("  " + ", ".join(header))

            print("\nFIELD-LEVEL TEMPORAL / STATE CANDIDATES")
            candidate_count = 0
            for basename in EXPECTED_CSVS:
                header = report["files"][basename]["fields"]
                for field in header:
                    categories = field_categories(field)
                    if not categories:
                        continue
                    candidate_count += 1
                    info = inspect_column(zf, basename, field, args.max_rows_per_field)
                    report["files"][basename].setdefault("field_profiles", []).append(info)
                    print(f"{basename}.{field}")
                    print(f"  CATEGORIES: {','.join(categories)}")
                    print(f"  ROWS_INSPECTED: {info['rows_inspected']}")
                    print(f"  NONEMPTY: {info['nonempty']}")
                    print(f"  ISO_DATETIME_PARSEABLE: {info['parseable_iso_datetime']}")
                    print(f"  DATETIME_MIN: {info['datetime_min']}")
                    print(f"  DATETIME_MAX: {info['datetime_max']}")
                    print(f"  SAMPLES: {info['samples']}")

            print("\nLEAKAGE SCREEN")
            leakage_fields = []
            for basename, data in report["files"].items():
                for info in data.get("field_profiles", []):
                    if "POTENTIAL_LEAKAGE_OR_OUTCOME_FIELD" in info["categories"]:
                        leakage_fields.append(f"{basename}.{info['field']}")
            print(f"POTENTIAL_LEAKAGE_OR_OUTCOME_FIELDS: {len(leakage_fields)}")
            for field in leakage_fields:
                print(f"  EXCLUDE_PENDING_SEMANTIC_REVIEW: {field}")

            print("\nAUDIT LIMITS")
            print("NO_ACCESSIBILITY_PREDICATE_INFERRED: True")
            print("NO_TEMPORAL_RULE_SELECTED: True")
            print("NO_RSTAR_CHANGE: True")
            print("NO_OUTCOME_OR_MODEL_INPUT: True")
            print("CANDIDATE_FIELDS_IDENTIFIED: ", candidate_count)

            payload = json.dumps(report, sort_keys=True, ensure_ascii=False, indent=2).encode("utf-8")
            print("REPORT_CANONICAL_SHA256:", hashlib.sha256(payload).hexdigest())
            print("\nRUNTIME_AUDIT_OK: True")
            print("DECISION_STATUS: OPEN_PENDING_HUMAN_REVIEW_AND_GITHUB_RECORD")
            print("NEXT_GATE: TEMPORAL_ACCESSIBILITY_CONDITION_SELECTION")
            return 0

    except (zipfile.BadZipFile, RuntimeError, OSError, csv.Error) as exc:
        print(f"FAIL_AUDIT_RUNTIME: {type(exc).__name__}: {exc}")
        return 7


if __name__ == "__main__":
    raise SystemExit(main())
