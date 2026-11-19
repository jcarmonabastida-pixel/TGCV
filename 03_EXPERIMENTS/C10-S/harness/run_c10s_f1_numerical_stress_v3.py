"""CLI and canonical evidence writer for C10-S F1 diagnostic v003."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path
import sys

from c10s_f1_numerical_stress_v3 import GENERATOR_VERSION, run_stress_v3


EXPECTED_COUNTS = {
    "N2_DISCRIMINANT_ULP_V3": 64,
    "N5_ROUNDING_CELL_V3": 1,
    "N4_FUJIWARA_BOUND_V3": 14,
}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--output-directory", required=True)
    parser.add_argument("--frozen-inputs", default=None)
    args = parser.parse_args()

    source_commit = args.source_commit
    if len(source_commit) != 40 or any(c not in "0123456789abcdef" for c in source_commit):
        parser.error("--source-commit must be a full lowercase Git commit SHA")

    output = Path(args.output_directory)
    output.mkdir(parents=True, exist_ok=True)
    frozen_inputs = (
        Path(args.frozen_inputs)
        if args.frozen_inputs
        else Path(__file__).with_name("C10S_F1_N4_V002_FROZEN_INPUTS_001.json")
    )

    result = run_stress_v3(frozen_inputs)
    records = result.pop("records")
    if len(records) != 79:
        raise SystemExit("V003_TOTAL_RECORD_COUNT_MISMATCH")
    observed = {
        lane: sum(record.get("lane") == lane for record in records)
        for lane in EXPECTED_COUNTS
    }
    if observed != EXPECTED_COUNTS:
        raise SystemExit(f"V003_LANE_DENOMINATOR_MISMATCH:{observed}")

    records_path = output / "numerical_stress_v3_records.jsonl"
    summary_path = output / "numerical_stress_v3_summary.json"
    manifest_path = output / "numerical_stress_v3_manifest.json"
    with records_path.open("w", encoding="utf-8", newline="\n") as stream:
        for record in records:
            stream.write(json.dumps(record, sort_keys=True, ensure_ascii=False) + "\n")
    _write_json(summary_path, result)

    harness_path = Path(__file__).with_name("c10s_f1_numerical_stress_v3.py")
    frozen_input_path = frozen_inputs.resolve()
    transitive_names = (
        "c10s_f1_numerical_stress.py",
        "c10s_f1_numerical_stress_v2.py",
        "c10s_f1_independent_root_isolator.py",
    )
    transitive = {
        name: _sha256(harness_path.with_name(name))
        for name in transitive_names
    }
    manifest = {
        "schema": "C10S-F1-NUMERICAL-STRESS-MANIFEST-003",
        "generator_version": GENERATOR_VERSION,
        "source_commit": source_commit,
        "runtime": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "frozen_inputs": {
            "path": frozen_input_path.name,
            "sha256": _sha256(frozen_input_path),
            "record_count": 14,
        },
        "source_sha256": {
            "runner": _sha256(Path(__file__)),
            "generator": _sha256(harness_path),
            **transitive,
        },
        "lane_counts": observed,
        "record_count": len(records),
        "records_sha256": _sha256(records_path),
        "summary_sha256": _sha256(summary_path),
        "scientific_execution": False,
        "dgp_execution": False,
        "monte_carlo_calibration": False,
    }
    _write_json(manifest_path, manifest)

    print(f"GENERATOR_VERSION={GENERATOR_VERSION}")
    print(f"SOURCE_COMMIT={source_commit}")
    print(f"LANE_COUNTS={json.dumps(observed, sort_keys=True)}")
    print(f"RECORD_COUNT={len(records)}")
    print(f"RECORDS_SHA256={manifest['records_sha256']}")
    print(f"SUMMARY_SHA256={manifest['summary_sha256']}")
    print(f"MANIFEST_SHA256={_sha256(manifest_path)}")
    print("SCIENTIFIC_EXECUTION=false")
    print("DGP_EXECUTION=false")
    print("MONTE_CARLO_CALIBRATION=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
