import csv
import ctypes
import io
import json
import os
import platform
import time
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

DATASET = Path(r"C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip")
TARGET_N = 507_279
H_DAYS = 180


def parse_dt(value: str) -> datetime:
    value = value.strip()
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        return dt
    return dt.astimezone(timezone.utc).replace(tzinfo=None)


def rss_bytes() -> int | None:
    if os.name != "nt":
        return None
    class PROCESS_MEMORY_COUNTERS(ctypes.Structure):
        _fields_ = [
            ("cb", ctypes.c_ulong),
            ("PageFaultCount", ctypes.c_ulong),
            ("PeakWorkingSetSize", ctypes.c_size_t),
            ("WorkingSetSize", ctypes.c_size_t),
            ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
            ("QuotaPagedPoolUsage", ctypes.c_size_t),
            ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
            ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
            ("PagefileUsage", ctypes.c_size_t),
            ("PeakPagefileUsage", ctypes.c_size_t),
        ]
    counters = PROCESS_MEMORY_COUNTERS()
    counters.cb = ctypes.sizeof(counters)
    handle = ctypes.windll.kernel32.GetCurrentProcess()
    ok = ctypes.windll.psapi.GetProcessMemoryInfo(
        handle, ctypes.byref(counters), ctypes.sizeof(counters)
    )
    return int(counters.PeakWorkingSetSize) if ok else None


def locate_versions_member(zf: zipfile.ZipFile) -> str:
    candidates = [
        n for n in zf.namelist()
        if n.lower().endswith("package_versions.csv")
    ]
    if not candidates:
        candidates = [n for n in zf.namelist() if Path(n).name.lower() == "versions.csv"]
    if not candidates:
        raise RuntimeError("Could not locate package_versions.csv or versions.csv inside ZIP")
    if len(candidates) > 1:
        raise RuntimeError(f"Ambiguous version CSV members: {candidates}")
    return candidates[0]


def open_reader(zf: zipfile.ZipFile, member: str):
    raw = zf.open(member, "r")
    text = io.TextIOWrapper(raw, encoding="utf-8-sig", newline="")
    return raw, text, csv.DictReader(text)


def main() -> None:
    started = time.perf_counter()
    if not DATASET.is_file():
        raise FileNotFoundError(f"Dataset not found: {DATASET}")

    with zipfile.ZipFile(DATASET, "r") as zf:
        member = locate_versions_member(zf)
        info = zf.getinfo(member)

        # Pass 1: determine the immutable observation endpoint from created_at only.
        raw, text, reader = open_reader(zf, member)
        required = {"created_at"}
        if not required.issubset(set(reader.fieldnames or [])):
            raise RuntimeError(f"Missing required columns. Headers: {reader.fieldnames}")
        max_created = None
        rows = 0
        invalid = 0
        for row in reader:
            rows += 1
            try:
                dt = parse_dt(row["created_at"])
            except Exception:
                invalid += 1
                continue
            if max_created is None or dt > max_created:
                max_created = dt
        text.close()
        raw.close()

        if max_created is None or invalid:
            raise RuntimeError(f"Invalid created_at state: max={max_created}, invalid={invalid}")

        cutoff = max_created - timedelta(days=H_DAYS)

        # Pass 2: deterministic census count of complete-follow-up origins.
        raw, text, reader = open_reader(zf, member)
        complete = 0
        incomplete = 0
        invalid_second = 0
        for row in reader:
            try:
                dt = parse_dt(row["created_at"])
            except Exception:
                invalid_second += 1
                continue
            if dt <= cutoff:
                complete += 1
            else:
                incomplete += 1
        text.close()
        raw.close()

    elapsed = time.perf_counter() - started
    peak = rss_bytes()
    pass_population = complete == TARGET_N and incomplete == (rows - TARGET_N)

    result = {
        "audit": "DR-025",
        "status": "PASS" if pass_population else "FAIL",
        "mode": "COMPUTATIONAL_FEASIBILITY_STRUCTURAL_ONLY",
        "dataset": str(DATASET),
        "dataset_member": member,
        "dataset_member_compressed_bytes": info.compress_size,
        "dataset_member_uncompressed_bytes": info.file_size,
        "python": platform.python_version(),
        "platform": platform.platform(),
        "h_days": H_DAYS,
        "snapshot_max_created_at": max_created.isoformat(sep=" "),
        "complete_followup_cutoff": cutoff.isoformat(sep=" "),
        "package_version_rows": rows,
        "invalid_created_at_pass1": invalid,
        "invalid_created_at_pass2": invalid_second,
        "complete_followup_origins": complete,
        "incomplete_right_censored_origins": incomplete,
        "target_complete_followup_origins": TARGET_N,
        "population_count_matches_frozen_target": pass_population,
        "wall_clock_seconds": round(elapsed, 6),
        "peak_working_set_bytes": peak,
        "peak_working_set_mib": round(peak / (1024 ** 2), 3) if peak is not None else None,
        "full_dataset_materialized_in_memory": False,
        "outcome_computed": False,
        "outcome_prevalence_computed": False,
        "association_computed": False,
        "effect_size_computed": False,
        "tacc_used_for_selection": False,
        "reach_used_for_selection": False,
        "rstar_used_for_selection": False,
        "b_used_for_selection": False,
        "adaptive_sampling": False,
        "sampling_performed": False,
        "confirmatory_analysis": False,
        "deterministic_census": True,
        "resource_feasibility_result": "CENSUS_ENUMERATION_FEASIBLE" if pass_population else "CENSUS_ENUMERATION_TARGET_MISMATCH",
    }

    print("EXECUTION_RESULT=" + result["status"])
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
