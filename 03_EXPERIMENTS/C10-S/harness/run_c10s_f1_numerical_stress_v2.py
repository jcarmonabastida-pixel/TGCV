"""Explicit CLI for the v002 F1 numerical stress design.

This command performs numerical work. It must only be invoked under a fresh,
exact one-shot authorization. Importing this file does not execute the suite.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from pathlib import Path

from c10s_f1_numerical_stress_v2 import GENERATOR_VERSION, run_stress_v2


def canonical_bytes(value: object) -> bytes:
    return (
        json.dumps(
            value, sort_keys=True, separators=(",", ":"),
            ensure_ascii=False, allow_nan=False,
        ) + "\n"
    ).encode("utf-8")


def package_version(name: str) -> str:
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return "NOT_INSTALLED"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the deterministic C10-S F1 numerical stress v002."
    )
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--output-directory", required=True)
    args = parser.parse_args()
    if (
        len(args.source_commit) != 40
        or any(c not in "0123456789abcdef" for c in args.source_commit.lower())
    ):
        parser.error("--source-commit must be a full 40-character Git SHA")

    result = run_stress_v2()
    if result.get("generator_version") != GENERATOR_VERSION:
        raise SystemExit("GENERATOR_VERSION_MISMATCH")

    records = []
    for lane, payload in (
        ("POLYNOMIAL_STURM_V2", result["polynomial"]),
        ("N3_COVARIANT_V2", result["n3_covariant"]),
        ("F1_N4_V2", result["f1_n4"]),
    ):
        for record in payload["records"]:
            records.append({"lane": lane, "record": record})
    records_bytes = b"".join(canonical_bytes(item) for item in records)

    def counts(records_for_lane, field):
        output = {}
        for item in records_for_lane:
            value = item.get(field)
            if value is not None:
                key = str(value)
                output[key] = output.get(key, 0) + 1
        return output

    summary = {
        "schema": "C10S-F1-NUMERICAL-STRESS-SUMMARY-002",
        "generator_version": GENERATOR_VERSION,
        "source_commit": args.source_commit,
        "polynomial_sturm_v2": {
            "record_count": len(result["polynomial"]["records"]),
            "topology_comparison_counts": result["polynomial"]["topology_comparison_counts"],
            "sturm_status_counts": result["polynomial"]["sturm_status_counts"],
        },
        "n3_covariant_v2": {
            "record_count": len(result["n3_covariant"]["records"]),
            "sturm_status_counts": counts(result["n3_covariant"]["records"], "sturm_status"),
            "topology_comparison_counts": counts(result["n3_covariant"]["records"], "topology_comparison_status"),
            "base_equivariance_counts": counts(result["n3_covariant"]["records"], "base_equivariance_status"),
        },
        "f1_n4_v2": {
            "record_count": len(result["f1_n4"]["records"]),
            "returned_count": result["f1_n4"]["returned_count"],
            "equivariance_counts": result["f1_n4"]["equivariance_counts"],
            "scale_exponents": result["f1_n4"]["scale_exponents"],
            "sturm_status_transition_brackets": result["f1_n4"]["sturm_status_transition_brackets"],
            "adjudication_status_transition_brackets": result["f1_n4"]["adjudication_status_transition_brackets"],
            "unresolved_exponents": result["f1_n4"]["unresolved_exponents"],
            "profile_status_counts": counts(result["f1_n4"]["records"], "profile_status"),
            "score_polynomial_status_counts": counts(result["f1_n4"]["records"], "score_polynomial_status"),
            "sturm_status_counts": counts(result["f1_n4"]["records"], "sturm_status"),
            "adjudication_status_counts": counts(result["f1_n4"]["records"], "adjudication_status"),
            "f1_root_count_total": sum(
                int(item.get("f1_root_count", 0))
                for item in result["f1_n4"]["records"]
            ),
            "sturm_root_count_total": sum(
                int(item.get("sturm_root_count", 0))
                for item in result["f1_n4"]["records"]
            ),
            "matched_root_count_total": sum(
                int(item.get("matched_root_count", 0))
                for item in result["f1_n4"]["records"]
            ),
            "multiplicity_review_required_count": sum(
                item.get("multiplicity_review_required") is True
                for item in result["f1_n4"]["records"]
            ),
        },
        "combined_record_count": len(records),
        "scientific_execution": False,
        "monte_carlo_calibration": False,
        "dgp_execution": False,
    }
    summary_bytes = canonical_bytes(summary)

    module_dir = Path(__file__).resolve().parent
    source_names = (
        "c10s_f1_numerical_stress_v2.py",
        "run_c10s_f1_numerical_stress_v2.py",
        "c10s_f1_numerical_stress.py",
        "c10s_f1_between_profile_likelihood.py",
        "c10s_f1_independent_root_isolator.py",
        "c10s_f1_root_adjudication.py",
        "c10s_variance_comparison_interface.py",
    )
    source_hashes = {
        name: hashlib.sha256((module_dir / name).read_bytes()).hexdigest()
        for name in source_names
    }
    manifest = {
        "schema": "C10S-F1-NUMERICAL-STRESS-MANIFEST-002",
        "generator_version": GENERATOR_VERSION,
        "source_commit": args.source_commit,
        "source_sha256": source_hashes,
        "runtime": {
            "python": sys.version,
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "numpy": package_version("numpy"),
            "scipy": package_version("scipy"),
        },
        "records_file": "numerical_stress_v2_records.jsonl",
        "records_sha256": hashlib.sha256(records_bytes).hexdigest(),
        "summary_file": "numerical_stress_v2_summary.json",
        "summary_sha256": hashlib.sha256(summary_bytes).hexdigest(),
        "record_encoding": "UTF-8 canonical JSON, sorted keys, compact separators, LF",
        "nan_and_infinity": "REJECTED",
    }
    manifest_bytes = canonical_bytes(manifest)

    output = Path(args.output_directory)
    output.mkdir(parents=True, exist_ok=True)
    payloads = {
        "numerical_stress_v2_records.jsonl": records_bytes,
        "numerical_stress_v2_summary.json": summary_bytes,
        "numerical_stress_v2_manifest.json": canonical_bytes(manifest),
    }
    for filename, payload in payloads.items():
        temporary = output / (filename + ".tmp")
        temporary.write_bytes(payload)
        temporary.replace(output / filename)
    print(json.dumps({
        "source_commit": args.source_commit,
        "record_count": len(records),
        "files_sha256": {
            name: hashlib.sha256(payload).hexdigest()
            for name, payload in payloads.items()
        },
    }, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
