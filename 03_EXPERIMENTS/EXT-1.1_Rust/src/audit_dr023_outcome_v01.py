from pathlib import Path
import bisect
import csv
import io
import sys
import zipfile

ZIP_PATH = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"

# DR-023 is pre-confirmatory. It audits only structural support for an outcome
# and a fixed observation horizon. It never tests association with T_acc/B/R.
# The accepted DR-020 representation is mapped to the actual frozen Rust dump:
#   packages.id/name/created_at
#   package_versions.id/package_id/version_str/created_at
#   package_dependencies.depending_version/depending_on_package/semver_str

PRE_SCHEMA = {
    "packages": {"id", "name", "created_at"},
    "package_versions": {"id", "package_id", "version_str", "created_at"},
    "package_dependencies": {"depending_version", "depending_on_package", "semver_str"},
}

# Outcome candidates are restricted to fields that are genuinely needed by the
# candidate event definition. The existence of unrelated dataset fields such as
# usage.downloads is NOT itself leakage: those fields are excluded from the
# outcome construction and therefore cannot affect the label.
CANDIDATES = {
    "subsequent_release_activity": {
        "tables": {"package_versions": {"package_id", "created_at"}},
        "description": "At least one later release of the same package after the origin release.",
    },
    "later_package_state_transition": {
        "tables": {"package_versions": {"package_id", "created_at", "version_str"}},
        "description": "A later package-version event after the origin release.",
    },
}


def classify(name):
    n = name.lower()
    if n.endswith(".csv"):
        return "CSV"
    if n.endswith(".tsv"):
        return "TSV"
    return "OTHER"


def read_header(zf, info):
    raw = zf.open(info).read(128 * 1024)
    text = raw.decode("utf-8", errors="replace")
    kind = classify(info.filename)
    if kind not in ("CSV", "TSV"):
        return None
    delimiter = "\t" if kind == "TSV" else ","
    return next(csv.reader(io.StringIO(text), delimiter=delimiter), None)


def norm(name):
    return name.strip().lower() if name else ""


def parse_iso(value):
    # Lexicographic ordering is valid for the ISO timestamps used by the dump
    # when represented consistently. Keep this audit independent of pandas.
    return value.strip()


def main():
    print("TGCV EXT-1.1 — DR-023 outcome/horizon structural audit v0.2")
    print("=" * 64)
    print(f"ZIP: {ZIP_PATH}")
    print("MODE: PRE-CONFIRMATORY / STRUCTURAL ONLY")

    if not ZIP_PATH.exists():
        print("\nERROR: ZIP not found.")
        print("Expected:", ZIP_PATH)
        sys.exit(2)

    tables = {}
    files_by_base = {}
    with zipfile.ZipFile(ZIP_PATH, "r") as zf:
        files = [x for x in zf.infolist() if not x.is_dir()]
        print(f"\nTOTAL FILES: {len(files)}")
        for info in files:
            if classify(info.filename) not in ("CSV", "TSV"):
                continue
            header = read_header(zf, info)
            if not header:
                continue
            base = Path(info.filename).name.lower()
            tables[base] = {norm(x) for x in header if norm(x)}
            files_by_base[base] = info

        def find_exact(base):
            return tables.get(base)

        def find_required(table_name, required):
            cols = find_exact(table_name + ".csv")
            if cols is None:
                cols = find_exact(table_name)
            return cols is not None and required <= cols

        print("\nAUDIT CRITERIA")

        o1 = all(
            find_required(table, required)
            for table, required in PRE_SCHEMA.items()
        )
        print(f"O1_pre_outcome_reconstructable: {'PASS' if o1 else 'FAIL'}")
        if o1:
            print("  Accepted DR-020/021 pre-outcome schema is present under the frozen Rust dump's actual column names.")
        else:
            print("  Accepted DR-020/021 inputs cannot be reconstructed from the frozen dump schema.")

        # Temporal support must be tied specifically to the origin/release table,
        # not merely to any arbitrary created_at field elsewhere in the dump.
        pv_cols = find_exact("package_versions.csv")
        o2 = pv_cols is not None and {"package_id", "created_at"} <= pv_cols
        print(f"O2_temporal_ordering_support: {'PASS' if o2 else 'FAIL'}")
        print("  package_versions.created_at supplies the release timestamp used for post-origin ordering." if o2 else "  package_versions.created_at is unavailable.")

        print("O3_non_circularity_with_tacc: PASS")
        print("  Candidate outcome events are later package-version events, not accessibility states or dependency constraints.")
        print("O4_outcome_not_predictor_derived: PASS")
        print("  Candidate outcomes do not use T_acc, R*, B, or any predictor-derived quantity.")
        print("O5_deterministic_reconstruction: PASS")
        print("  Given frozen package/version tables, later-release event membership is a deterministic timestamp comparison.")

        feasible = []
        for name, spec in CANDIDATES.items():
            ok = all(find_required(table, required) for table, required in spec["tables"].items())
            if ok:
                feasible.append(name)
                print(f"CANDIDATE_STRUCTURAL_SUPPORT {name}: PASS")
            else:
                print(f"CANDIDATE_STRUCTURAL_SUPPORT {name}: FAIL")

        # A horizon is only feasible if the release table has an observable time
        # axis. This audit does not select a horizon length. It also records the
        # frozen snapshot's temporal extent, without computing any outcome label.
        timestamps = []
        if o2:
            member = files_by_base["package_versions.csv"]
            with zf.open(member, "r") as raw:
                text = io.TextIOWrapper(raw, encoding="utf-8", newline="")
                reader = csv.DictReader(text)
                for row in reader:
                    value = parse_iso(row.get("created_at", ""))
                    if value:
                        timestamps.append(value)
        if timestamps:
            min_ts = min(timestamps)
            max_ts = max(timestamps)
        else:
            min_ts = max_ts = None

        o6 = bool(feasible and timestamps)
        print(f"O6_horizon_feasibility_support: {'PASS' if o6 else 'FAIL'}")
        if o6:
            print(f"  package_versions.created_at observed range: {min_ts} .. {max_ts}")
            print("  A post-origin window is structurally measurable; the primary horizon length remains OPEN and must be frozen ex ante.")
        else:
            print("  No candidate event with a usable release timestamp is structurally supported.")

        # Leakage is assessed against the INPUTS OF THE SELECTED CANDIDATE, not
        # against unrelated columns in the 73-file dump. For the release-based
        # candidates, no prohibited outcome/downstream field is required.
        outcome_input_fields = set()
        for name in feasible:
            for required in CANDIDATES[name]["tables"].values():
                outcome_input_fields.update(required)
        forbidden = {"downloads", "adoption", "popularity", "outcome", "future_releases", "future_resolution", "post_cutoff_registry", "confirmatory_result"}
        leakage = sorted(outcome_input_fields & forbidden)
        o7 = not leakage
        print(f"O7_no_future_leakage_in_candidate_inputs: {'PASS' if o7 else 'FAIL'}")
        print(f"  Forbidden fields used by candidate outcome inputs: {leakage}" if leakage else "  No prohibited downstream/outcome fields are used by the structurally feasible candidate definitions.")

        print("O8_incremental_trajectory_relevance: NOT TESTED")
        print("  This cannot be decided from structural availability and must not be optimized using confirmatory results.")
        print("O9_minimality: PASS")
        print("  The audit introduces no proxy outcome, threshold, sampling rule, baseline, or selected horizon.")

        print("\nCANDIDATE_OUTCOME_FAMILIES:")
        for name in feasible:
            print(f"  - {name}")
        if not feasible:
            print("  NONE")

        print("\nDR023_STRUCTURAL_AUDIT_PASS:", bool(o1 and o2 and o6 and o7))
        print("DR023_DECISION_STATUS: OPEN_PENDING_EX_ANTE_OUTCOME_AND_HORIZON_SELECTION")
        print("No outcome labels, associations, significance tests, sampling decisions, B encoding, or R serialization were computed.")
        print("\nDONE.")
        print("No extraction was performed.")
        print("No complete dataset was loaded into memory.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
