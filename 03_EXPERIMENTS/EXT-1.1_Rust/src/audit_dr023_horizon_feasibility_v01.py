#!/usr/bin/env python3
"""DR-023 horizon-feasibility audit for EXT-1.1 Rust.

PRE-CONFIRMATORY ONLY.

The audit evaluates only whether pre-declared candidate elapsed-time horizons
are structurally observable in the frozen snapshot. It does NOT construct
outcome labels, inspect outcome prevalence, compute T_acc, B, R, associations,
effect sizes, significance, or sampling decisions.

A candidate horizon is reported as structurally feasible when the frozen
package_versions timestamp axis contains complete global follow-up through
that elapsed-time window for an origin release. This is a conservative
measurement-coverage criterion: incomplete follow-up is never converted into
a negative outcome.

The candidate horizon grid is explicitly a DESIGN GRID, not a selected primary
horizon. No member of the grid is privileged by this script.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import sys
import zipfile
from pathlib import Path

ZIP_PATH = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"
DEFAULT_HORIZONS_DAYS = (30, 90, 180, 365)


def archive_member(zf: zipfile.ZipFile, basename: str) -> str:
    matches = [
        n for n in zf.namelist()
        if n.replace("\\", "/").rsplit("/", 1)[-1] == basename
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"ARCHIVE_MEMBER_RESOLUTION_ERROR: {basename!r}: found {len(matches)} matches"
        )
    return matches[0]


def parse_timestamp(value: str) -> dt.datetime:
    value = value.strip()
    if not value:
        raise ValueError("EMPTY_TIMESTAMP")
    # The frozen dump uses ISO-like timestamps with microseconds and no offset.
    # Treat them as naive UTC-like dataset timestamps for elapsed-time arithmetic;
    # no external clock or timezone conversion is introduced.
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).replace(tzinfo=None)


def percentile(sorted_values, fraction):
    if not sorted_values:
        return None
    index = int(round((len(sorted_values) - 1) * fraction))
    return sorted_values[index]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Pre-confirmatory structural feasibility audit for DR-023 horizons."
    )
    parser.add_argument(
        "--horizons",
        nargs="+",
        type=int,
        default=list(DEFAULT_HORIZONS_DAYS),
        help="Explicit design-grid horizons in elapsed days; no horizon is selected by this script.",
    )
    args = parser.parse_args()

    horizons = tuple(sorted(set(args.horizons)))
    if not horizons or any(h <= 0 for h in horizons):
        print("ERROR: horizons must be positive integers.")
        return 2

    print("TGCV EXT-1.1 — DR-023 horizon feasibility audit v0.1")
    print("=" * 64)
    print(f"ZIP: {ZIP_PATH}")
    print("MODE: PRE-CONFIRMATORY / STRUCTURAL ONLY")
    print("HORIZON_GRID_DAYS:", ",".join(str(h) for h in horizons))
    print("GRID_STATUS: DESIGN CANDIDATES ONLY — NO PRIMARY HORIZON SELECTED")

    if not ZIP_PATH.exists():
        print("ERROR: ZIP not found.")
        print("Expected:", ZIP_PATH)
        return 2

    try:
        with zipfile.ZipFile(ZIP_PATH, "r") as zf:
            member = archive_member(zf, "package_versions.csv")

            timestamps = []
            missing_timestamp = 0
            row_count = 0
            with zf.open(member, "r") as raw:
                text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
                reader = csv.DictReader(text)
                required = {"id", "package_id", "created_at"}
                header = set(reader.fieldnames or [])
                if not required.issubset(header):
                    print("FAIL_SCHEMA_PACKAGE_VERSIONS: True")
                    print("  Missing required fields:", sorted(required - header))
                    return 3

                for row in reader:
                    row_count += 1
                    value = row.get("created_at", "")
                    if not value.strip():
                        missing_timestamp += 1
                        continue
                    try:
                        timestamps.append(parse_timestamp(value))
                    except ValueError as exc:
                        print("FAIL_TIMESTAMP_PARSE:", exc)
                        return 4

            if not timestamps:
                print("FAIL_NO_TIMESTAMP_AXIS: True")
                return 5

            timestamps.sort()
            min_ts = timestamps[0]
            max_ts = timestamps[-1]
            span = max_ts - min_ts

            print("\nDATASET TEMPORAL COVERAGE")
            print("PACKAGE_VERSION_ROWS:", row_count)
            print("VALID_CREATED_AT_ROWS:", len(timestamps))
            print("MISSING_CREATED_AT_ROWS:", missing_timestamp)
            print("MIN_CREATED_AT:", min_ts.isoformat(sep=" "))
            print("MAX_CREATED_AT:", max_ts.isoformat(sep=" "))
            print("OBSERVED_SPAN_DAYS:", span.total_seconds() / 86400.0)

            # This audit deliberately does not construct Y_H. It counts only
            # origins for which the global snapshot boundary permits complete
            # observation through H. It uses timestamps only.
            print("\nHORIZON COVERAGE")
            print("NOTE: counts below are observation-coverage counts, NOT outcome counts.")
            print("NOTE: no later-release event is searched for or labelled.")

            total_origins = len(timestamps)
            results = []
            for h in horizons:
                cutoff = max_ts - dt.timedelta(days=h)
                # Number of origin timestamps for which origin + H <= snapshot end.
                eligible = 0
                for ts in timestamps:
                    if ts <= cutoff:
                        eligible += 1
                    else:
                        break
                censored = total_origins - eligible
                coverage = eligible / total_origins if total_origins else 0.0
                results.append((h, eligible, censored, coverage))
                print(
                    f"H={h}d: COMPLETE_FOLLOWUP_ORIGINS={eligible} "
                    f"INCOMPLETE_FOLLOWUP_ORIGINS={censored} "
                    f"COVERAGE={coverage:.6f}"
                )

            # Structural gate: each candidate must have a non-empty complete-
            # follow-up population and the dataset span must exceed H. This does
            # not choose the best horizon and does not rank candidates.
            print("\nSTRUCTURAL FEASIBILITY")
            feasible = []
            for h, eligible, censored, coverage in results:
                ok = eligible > 0 and span >= dt.timedelta(days=h)
                print(f"H={h}d: {'PASS' if ok else 'FAIL'}")
                if ok:
                    feasible.append(h)

            print("\nDESIGN INTERPRETATION")
            print("FEASIBLE_HORIZONS:", ",".join(str(h) for h in feasible) if feasible else "NONE")
            print("PRIMARY_HORIZON_SELECTED: False")
            print("OUTCOME_LABELS_COMPUTED: False")
            print("OUTCOME_PREVALENCE_COMPUTED: False")
            print("TACC_COMPUTED: False")
            print("ASSOCIATIONS_COMPUTED: False")
            print("EFFECT_SIZES_COMPUTED: False")
            print("SAMPLING_DECISION_COMPUTED: False")
            print("BASELINE_B_COMPUTED: False")
            print("R_SERIALIZATION_COMPUTED: False")
            print("HORIZON_SELECTION_BY_STATISTICAL_CRITERION: False")

            audit_pass = bool(feasible)
            print("\nDR023_HORIZON_FEASIBILITY_AUDIT_PASS:", audit_pass)
            print("DR023_DECISION_STATUS: OPEN_PENDING_EX_ANTE_HORIZON_SELECTION")
            print("\nDONE.")
            print("No extraction was performed.")
            print("No complete dataset was loaded into memory.")
            return 0 if audit_pass else 6

    except (zipfile.BadZipFile, KeyError, ValueError, RuntimeError, csv.Error) as exc:
        print(f"FAIL_AUDIT_RUNTIME: {type(exc).__name__}: {exc}")
        return 7


if __name__ == "__main__":
    raise SystemExit(main())
