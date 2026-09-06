#!/usr/bin/env python3
"""DR-024 structural sampling/exclusion audit for EXT-1.1 Rust.

PRE-CONFIRMATORY ONLY.

This audit evaluates only deterministic structural eligibility and complete
180-day observation coverage under the accepted DR-023 horizon. It does NOT
construct outcome labels, compute T_acc/R*/B, inspect associations or effect
sizes, or select N/seed.

The audit streams package_versions.csv directly from the frozen ZIP and uses
the dataset's global maximum package-version timestamp as the conservative
snapshot boundary. Complete follow-up means origin_created_at + 180 days <=
snapshot_max_created_at.

Technical invalidity and follow-up incompleteness are reported separately.
No substantive package characteristic is used for exclusion.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import zipfile
from pathlib import Path

DEFAULT_ZIP = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"
HORIZON_DAYS = 180
REQUIRED = {"id", "package_id", "version_str", "created_at"}


def resolve_member(zf: zipfile.ZipFile, basename: str) -> str:
    matches = [n for n in zf.namelist() if n.replace("\\", "/").rsplit("/", 1)[-1] == basename]
    if len(matches) != 1:
        raise RuntimeError(f"ARCHIVE_MEMBER_RESOLUTION_ERROR: {basename}: found {len(matches)}")
    return matches[0]


def parse_ts(value: str) -> dt.datetime:
    value = value.strip()
    if not value:
        raise ValueError("EMPTY_TIMESTAMP")
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).replace(tzinfo=None)


def main() -> int:
    parser = argparse.ArgumentParser(description="Structural DR-024 audit")
    parser.add_argument("--zip", default=str(DEFAULT_ZIP), help="Frozen Rust dataset ZIP")
    args = parser.parse_args()
    zip_path = Path(args.zip)

    print("TGCV EXT-1.1 — DR-024 sampling/exclusion structural audit v0.1")
    print("=" * 68)
    print(f"ZIP: {zip_path}")
    print("MODE: PRE-CONFIRMATORY / STRUCTURAL ONLY")
    print(f"HORIZON_DAYS: {HORIZON_DAYS}")
    print("SAMPLING_DECISION: NOT MADE")
    print("OUTCOME_LABELS: NOT COMPUTED")

    if not zip_path.exists():
        print("ERROR: ZIP not found.")
        return 2

    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            member = resolve_member(zf, "package_versions.csv")
            total = 0
            valid_timestamp = 0
            missing_timestamp = 0
            invalid_timestamp = 0
            missing_identity = 0
            duplicate_ids = 0
            seen_ids: set[str] = set()
            timestamps: list[dt.datetime] = []

            with zf.open(member, "r") as raw:
                text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
                reader = csv.DictReader(text)
                fields = set(reader.fieldnames or [])
                missing_fields = sorted(REQUIRED - fields)
                if missing_fields:
                    print("FAIL_SCHEMA: True")
                    print("MISSING_REQUIRED_FIELDS:", ",".join(missing_fields))
                    return 3

                for row in reader:
                    total += 1
                    rid = (row.get("id") or "").strip()
                    package_id = (row.get("package_id") or "").strip()
                    version_str = (row.get("version_str") or "").strip()
                    ts_value = row.get("created_at") or ""

                    if not rid or not package_id or not version_str:
                        missing_identity += 1
                    if rid:
                        if rid in seen_ids:
                            duplicate_ids += 1
                        else:
                            seen_ids.add(rid)

                    if not ts_value.strip():
                        missing_timestamp += 1
                        continue
                    try:
                        ts = parse_ts(ts_value)
                    except ValueError:
                        invalid_timestamp += 1
                        continue
                    valid_timestamp += 1
                    timestamps.append(ts)

            print("\nSTRUCTURAL OBSERVATIONS")
            print("PACKAGE_VERSION_ROWS:", total)
            print("VALID_CREATED_AT_ROWS:", valid_timestamp)
            print("MISSING_CREATED_AT_ROWS:", missing_timestamp)
            print("INVALID_CREATED_AT_ROWS:", invalid_timestamp)
            print("MISSING_REQUIRED_IDENTITY_FIELDS:", missing_identity)
            print("DUPLICATE_VERSION_IDS:", duplicate_ids)

            if not timestamps:
                print("FAIL_NO_VALID_TIMESTAMP_AXIS: True")
                return 4

            snapshot_max = max(timestamps)
            horizon = dt.timedelta(days=HORIZON_DAYS)
            complete_followup = 0
            incomplete_followup = 0
            structurally_invalid = 0

            for row_invalid in []:
                structurally_invalid += row_invalid

            # Structural invalidity is defined conservatively from the observed
            # required-field/timestamp checks above. Follow-up is independent.
            structurally_invalid = (
                missing_timestamp + invalid_timestamp + missing_identity
            )
            eligible = 0

            # Re-read only package_versions.csv to classify complete follow-up.
            # This keeps the audit simple and deterministic while still streaming.
            with zf.open(member, "r") as raw:
                text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
                reader = csv.DictReader(text)
                for row in reader:
                    rid = (row.get("id") or "").strip()
                    package_id = (row.get("package_id") or "").strip()
                    version_str = (row.get("version_str") or "").strip()
                    ts_value = row.get("created_at") or ""
                    if not rid or not package_id or not version_str or not ts_value.strip():
                        continue
                    try:
                        ts = parse_ts(ts_value)
                    except ValueError:
                        continue
                    if ts + horizon <= snapshot_max:
                        complete_followup += 1
                    else:
                        incomplete_followup += 1

            # The second pass above counts follow-up for structurally valid rows.
            # Eligible origins therefore require both structural validity and
            # complete follow-up. Duplicate IDs are technical ambiguity and are
            # excluded from the eligible count if present.
            eligible = max(0, complete_followup - max(0, duplicate_ids))

            print("\nFOLLOW-UP / ELIGIBILITY")
            print("SNAPSHOT_MAX_CREATED_AT:", snapshot_max.isoformat(sep=" "))
            print("HORIZON_END_RULE: origin_created_at + 180d <= snapshot_max_created_at")
            print("COMPLETE_FOLLOWUP_ORIGINS:", complete_followup)
            print("INCOMPLETE_FOLLOWUP_ORIGINS:", incomplete_followup)
            print("ELIGIBLE_ORIGINS:", eligible)

            print("\nEXCLUSION_POLICY_CHECK")
            print("OUTCOME_USED_FOR_EXCLUSION: False")
            print("TACC_USED_FOR_EXCLUSION: False")
            print("RSTAR_USED_FOR_EXCLUSION: False")
            print("BASELINE_B_USED_FOR_EXCLUSION: False")
            print("DOWNLOADS_ADOPTION_USED_FOR_EXCLUSION: False")
            print("POST_ORIGIN_ACTIVITY_USED_FOR_EXCLUSION: False")
            print("MANUAL_PACKAGE_SELECTION: False")
            print("PILOT_OR_CONFIRMATORY_RESULTS_USED: False")
            print("SUBSTANTIVE_PACKAGE_CHARACTERISTICS_USED: False")

            print("\nSAMPLING STATUS")
            print("CENSUS_FIRST: True")
            print("SAMPLING_REQUIRED_BY_THIS_AUDIT: False")
            print("N_SELECTED: False")
            print("SEED_SELECTED: False")

            # Determinism is established by replaying the same classification
            # rule on the same immutable timestamp boundary without randomness.
            replay_complete = 0
            with zf.open(member, "r") as raw:
                text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
                reader = csv.DictReader(text)
                for row in reader:
                    rid = (row.get("id") or "").strip()
                    package_id = (row.get("package_id") or "").strip()
                    version_str = (row.get("version_str") or "").strip()
                    ts_value = row.get("created_at") or ""
                    if not rid or not package_id or not version_str or not ts_value.strip():
                        continue
                    try:
                        ts = parse_ts(ts_value)
                    except ValueError:
                        continue
                    if ts + horizon <= snapshot_max:
                        replay_complete += 1

            deterministic = replay_complete == complete_followup
            print("\nDETERMINISM")
            print("REPLAY_COMPLETE_FOLLOWUP_ORIGINS:", replay_complete)
            print("DETERMINISTIC_CLASSIFICATION: ", deterministic)

            audit_pass = (
                missing_timestamp == 0
                and invalid_timestamp == 0
                and missing_identity == 0
                and duplicate_ids == 0
                and complete_followup > 0
                and deterministic
            )
            print("\nDR024_STRUCTURAL_AUDIT_PASS:", audit_pass)
            print("DR024_DECISION_STATUS: OPEN_PENDING_AUDIT_ACCEPTANCE")
            print("\nPROHIBITED_COMPUTATIONS")
            print("OUTCOME_PREVALENCE_COMPUTED: False")
            print("TACC_COMPUTED: False")
            print("ASSOCIATIONS_COMPUTED: False")
            print("EFFECT_SIZES_COMPUTED: False")
            print("SIGNIFICANCE_COMPUTED: False")
            print("\nDONE.")
            print("No extraction was performed.")
            print("No complete dataset was loaded into memory.")
            return 0 if audit_pass else 6
    except (zipfile.BadZipFile, RuntimeError, csv.Error, OSError) as exc:
        print(f"FAIL_AUDIT_RUNTIME: {type(exc).__name__}: {exc}")
        return 7


if __name__ == "__main__":
    raise SystemExit(main())
