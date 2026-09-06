from pathlib import Path
import csv
import io
import zipfile
import sys
from collections import Counter, defaultdict

ZIP_PATH = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"
ROOT = "rust_repos_2022_09_07/"
SOURCES = ROOT + "dumps/postgresql/data/sources.csv"
PACKAGES = ROOT + "dumps/postgresql/data/packages.csv"
VERSIONS = ROOT + "dumps/postgresql/data/package_versions.csv"
DEPS = ROOT + "dumps/postgresql/data/package_dependencies.csv"


def rows_from_zip(zf, member):
    with zf.open(member, "r") as raw:
        text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
        yield from csv.DictReader(text)


def parse_dt(value):
    if not value:
        return None
    # Dataset timestamps are ISO-like; lexical comparison is safe after
    # normalising the date/time separator and retaining microseconds.
    return value.strip()


def main():
    print("TGCV EXT-1.1 — Rust component identity audit v0.1")
    print("=" * 64)
    print(f"ZIP: {ZIP_PATH}")

    if not ZIP_PATH.exists():
        print("ERROR: ZIP not found.")
        sys.exit(2)

    with zipfile.ZipFile(ZIP_PATH, "r") as zf:
        names = set(zf.namelist())
        required = [SOURCES, PACKAGES, VERSIONS, DEPS]
        missing = [x for x in required if x not in names]
        if missing:
            print("ERROR: required dataset members missing:")
            for x in missing:
                print("  -", x)
            sys.exit(3)

        # ------------------------------------------------------------
        # 1. Source/domain identity
        # ------------------------------------------------------------
        source_rows = list(rows_from_zip(zf, SOURCES))
        crates = [r for r in source_rows if r.get("id") == "3"]
        print("\n[1] SOURCE DOMAIN")
        print("source_id=3 rows:", len(crates))
        for r in crates:
            print("  id=3 name=%r url_root=%r" % (r.get("name"), r.get("url_root")))
        print("PASS_SOURCE_CRATES:", len(crates) == 1 and crates[0].get("name") == "crates")

        # ------------------------------------------------------------
        # 2. Package identity: id -> source/name
        # ------------------------------------------------------------
        package_by_id = {}
        package_name_pairs = Counter()
        package_name_conflicts = []
        package_source_conflicts = []
        package_rows = 0
        crate_packages = 0

        for r in rows_from_zip(zf, PACKAGES):
            package_rows += 1
            pid = r.get("id", "")
            key = (r.get("source_id", ""), r.get("name", ""))
            package_name_pairs[key] += 1
            if pid in package_by_id:
                prev = package_by_id[pid]
                if (prev.get("name"), prev.get("source_id")) != (r.get("name"), r.get("source_id")):
                    package_name_conflicts.append((pid, prev, r))
            else:
                package_by_id[pid] = r
            if r.get("source_id") == "3":
                crate_packages += 1

        duplicate_package_names = [k for k, n in package_name_pairs.items() if n > 1 and k[0] == "3"]
        print("\n[2] PACKAGE IDENTITY")
        print("package rows:", package_rows)
        print("unique package ids:", len(package_by_id))
        print("crate packages:", crate_packages)
        print("package id -> name/source conflicts:", len(package_name_conflicts))
        print("duplicate (source_id=3, name) rows:", sum(package_name_pairs[k] - 1 for k in duplicate_package_names))
        print("PASS_PACKAGE_ID_STABLE:", len(package_name_conflicts) == 0)

        if package_name_conflicts:
            for pid, a, b in package_name_conflicts[:10]:
                print("  CONFLICT", pid, a, b)

        # ------------------------------------------------------------
        # 3. Version observation: (package_id, version_str) -> version id
        # ------------------------------------------------------------
        version_by_id = {}
        version_key_to_ids = defaultdict(list)
        version_rows = 0
        version_package_missing = 0
        version_time_before_package = 0
        version_time_missing = 0
        non_crate_versions = 0
        crate_version_rows = 0

        for r in rows_from_zip(zf, VERSIONS):
            version_rows += 1
            vid = r.get("id", "")
            pid = r.get("package_id", "")
            vstr = r.get("version_str", "")
            version_by_id[vid] = r
            version_key_to_ids[(pid, vstr)].append(vid)

            pkg = package_by_id.get(pid)
            if pkg is None:
                version_package_missing += 1
            else:
                if pkg.get("source_id") == "3":
                    crate_version_rows += 1
                else:
                    non_crate_versions += 1
                pdt = parse_dt(pkg.get("created_at", ""))
                vdt = parse_dt(r.get("created_at", ""))
                if not pdt or not vdt:
                    version_time_missing += 1
                elif vdt < pdt:
                    version_time_before_package += 1

        duplicate_version_keys = {k: ids for k, ids in version_key_to_ids.items() if len(ids) > 1}
        print("\n[3] RELEASE OBSERVATION")
        print("package_version rows:", version_rows)
        print("unique version ids:", len(version_by_id))
        print("crate release rows:", crate_version_rows)
        print("non-crate release rows:", non_crate_versions)
        print("version rows with missing package_id:", version_package_missing)
        print("duplicate (package_id, version_str) keys:", len(duplicate_version_keys))
        print("rows with version.created_at < package.created_at:", version_time_before_package)
        print("rows with missing package/version timestamp:", version_time_missing)
        print("PASS_VERSION_KEY_UNIQUE:", len(duplicate_version_keys) == 0)
        print("PASS_VERSION_PACKAGE_FK:", version_package_missing == 0)
        print("PASS_VERSION_TEMPORAL_ORDER:", version_time_before_package == 0)

        if duplicate_version_keys:
            for k, ids in list(duplicate_version_keys.items())[:10]:
                print("  DUPLICATE_VERSION_KEY", k, ids[:10])

        # ------------------------------------------------------------
        # 4. Dependency reference integrity and post-outcome exposure
        # ------------------------------------------------------------
        dep_rows = 0
        dep_version_missing = 0
        dep_package_missing = 0
        semver_counter = Counter()
        dependency_dates = []

        for r in rows_from_zip(zf, DEPS):
            dep_rows += 1
            dv = r.get("depending_version", "")
            dp = r.get("depending_on_package", "")
            semver_counter[r.get("semver_str", "")] += 1
            if dv not in version_by_id:
                dep_version_missing += 1
            if dp not in package_by_id:
                dep_package_missing += 1

        print("\n[4] DEPENDENCY REFERENCE INTEGRITY")
        print("dependency rows:", dep_rows)
        print("depending_version ids missing from package_versions:", dep_version_missing)
        print("depending_on_package ids missing from packages:", dep_package_missing)
        print("distinct semver strings:", len(semver_counter))
        print("literal '*' semver rows:", semver_counter.get("*", 0))
        print("PASS_DEP_VERSION_FK:", dep_version_missing == 0)
        print("PASS_DEP_PACKAGE_FK:", dep_package_missing == 0)

        # ------------------------------------------------------------
        # 5. Audit conclusion. This is deliberately conservative:
        #    a PASS here means only that the proposed identity is
        #    structurally identifiable from these four frozen tables.
        # ------------------------------------------------------------
        audit_pass = (
            len(crates) == 1
            and crates[0].get("name") == "crates"
            and len(package_name_conflicts) == 0
            and version_package_missing == 0
            and version_time_before_package == 0
            and len(duplicate_version_keys) == 0
            and dep_version_missing == 0
            and dep_package_missing == 0
        )

        print("\nAUDIT CONCLUSION")
        print("PASS_STRUCTURAL_COMPONENT_IDENTITY:", audit_pass)
        print("NOTE: This audit does not define T, T_acc, B, R, resources, outcome, sampling, or the exact dependency-resolution semantics.")
        print("NOTE: No dataset extraction was performed; CSV members were streamed directly from the ZIP.")
        print("NOTE: No confirmatory experiment was executed.")

        if not audit_pass:
            sys.exit(4)


if __name__ == "__main__":
    main()
