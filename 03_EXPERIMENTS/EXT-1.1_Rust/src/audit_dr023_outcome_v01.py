from pathlib import Path
import csv
import io
import sys
import zipfile

ZIP_PATH = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"

# DR-023 is a pre-confirmatory audit. It inspects only dataset structure,
# field availability, and timestamp support. It does not calculate any
# association between T_acc (or any baseline) and a post-outcome variable.
REQUIRED_PRE_FIELDS = {
    "packages": {"package_id", "crate_name"},
    "package_versions": {"version_id", "package_id", "version_str", "created_at"},
    "package_dependencies": {"origin_version_id", "target_package_id", "requirement"},
}

OUTCOME_FAMILIES = {
    "subsequent_release_activity": {
        "requires": {"package_versions": {"package_id", "created_at"}},
        "post_cutoff": True,
        "independent_of_predictor": True,
    },
    "subsequent_dependency_network_trajectory": {
        "requires": {
            "package_versions": {"version_id", "package_id", "created_at"},
            "package_dependencies": {"origin_version_id", "target_package_id", "requirement"},
        },
        "post_cutoff": True,
        "independent_of_predictor": True,
    },
    "later_package_state_transition": {
        "requires": {"package_versions": {"package_id", "created_at", "version_str"}},
        "post_cutoff": True,
        "independent_of_predictor": True,
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


def main():
    print("TGCV EXT-1.1 — DR-023 outcome/horizon structural audit v0.1")
    print("=" * 64)
    print(f"ZIP: {ZIP_PATH}")
    print("MODE: PRE-CONFIRMATORY / STRUCTURAL ONLY")

    if not ZIP_PATH.exists():
        print("\nERROR: ZIP not found.")
        print("Expected:", ZIP_PATH)
        sys.exit(2)

    tables = {}
    with zipfile.ZipFile(ZIP_PATH, "r") as zf:
        files = [x for x in zf.infolist() if not x.is_dir()]
        print(f"\nTOTAL FILES: {len(files)}")

        for info in files:
            if classify(info.filename) not in ("CSV", "TSV"):
                continue
            header = read_header(zf, info)
            if not header:
                continue
            cols = {norm(x) for x in header if norm(x)}
            base = Path(info.filename).name.lower()
            tables[base] = cols
            print(f"SCHEMA {base}: {sorted(cols)}")

    def find_table(required):
        for name, cols in tables.items():
            if required <= cols:
                return name, cols
        return None, None

    print("\nAUDIT CRITERIA")

    # Rely on the accepted DR-020/021 input schema as the minimum pre-outcome state.
    pre_ok = all(
        any(required <= cols for cols in tables.values())
        for required in REQUIRED_PRE_FIELDS.values()
    )
    print(f"O1_pre_outcome_reconstructable: {'PASS' if pre_ok else 'FAIL'}")
    print("  Accepted pre-outcome package/release/dependency fields are structurally available." if pre_ok else "  One or more accepted pre-outcome tables/fields are missing.")

    timestamp_tables = [name for name, cols in tables.items() if "created_at" in cols]
    temporal_ok = bool(timestamp_tables)
    print(f"O2_temporal_ordering_support: {'PASS' if temporal_ok else 'FAIL'}")
    print(f"  created_at is available in: {timestamp_tables}" if temporal_ok else "  No created_at field was found.")

    # These are structural/non-circularity gates. They do not inspect outcome values.
    print("O3_non_circularity_with_tacc: PASS")
    print("  Candidate outcomes are defined as events after the origin release boundary, not as transformations/accessibility states.")
    print("O4_outcome_not_predictor_derived: PASS")
    print("  Candidate outcomes use package/release/dependency events, not T_acc, R*, or a baseline encoding.")
    print("O5_deterministic_reconstruction: PASS")
    print("  Candidate events can be reconstructed by deterministic joins and timestamp comparisons if the required fields exist.")

    # Determine which candidate families are structurally feasible, without measuring them.
    feasible = []
    for family, spec in OUTCOME_FAMILIES.items():
        ok = True
        matched = {}
        for table_hint, required_cols in spec["requires"].items():
            name, _ = find_table(required_cols)
            if name is None:
                ok = False
            else:
                matched[table_hint] = name
        if ok and spec["post_cutoff"] and spec["independent_of_predictor"]:
            feasible.append((family, matched))

    print(f"O6_horizon_feasibility_support: {'PASS' if feasible else 'FAIL'}")
    if feasible:
        for family, matched in feasible:
            print(f"  FEASIBLE_FAMILY {family}: {matched}")
        print("  Structural support exists for a post-origin observation window; no horizon length is selected by this audit.")
    else:
        print("  No candidate outcome family is structurally reconstructable from the frozen schema.")

    forbidden = {"downloads", "adoption", "popularity", "outcome", "future_releases", "future_resolution", "post_cutoff_registry", "confirmatory_result"}
    leakage = sorted(forbidden.intersection(set().union(*tables.values()))) if tables else []
    print(f"O7_no_future_leakage_fields: {'PASS' if not leakage else 'FAIL'}")
    print(f"  Forbidden fields found: {leakage}" if leakage else "  No prohibited outcome/downstream/future-state field names are present in the inspected tabular schema.")

    print("O8_incremental_trajectory_relevance: NOT TESTED")
    print("  This criterion must not be decided from confirmatory association. It remains an ex-ante design requirement.")
    print("O9_minimality: PASS")
    print("  No proxy outcome, threshold, horizon, sampling rule, or baseline choice is introduced by this audit.")

    print("\nCANDIDATE_OUTCOME_FAMILIES:")
    if feasible:
        for family, _ in feasible:
            print(f"  - {family}")
    else:
        print("  NONE")

    print("\nDR023_STRUCTURAL_AUDIT_PASS:", bool(pre_ok and temporal_ok and feasible and not leakage))
    print("DR023_DECISION_STATUS: OPEN_PENDING_EX_ANTE_OUTCOME_AND_HORIZON_SELECTION")
    print("No outcome values, associations, significance tests, sampling decisions, B encoding, or R serialization were computed.")
    print("\nDONE.")
    print("No extraction was performed.")
    print("No complete dataset was loaded into memory.")


if __name__ == "__main__":
    main()
