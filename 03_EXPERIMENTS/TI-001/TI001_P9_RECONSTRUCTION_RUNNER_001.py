#!/usr/bin/env python3
"""TI-001 P9 comparison runner.

Runs the independent Executor-2 reconstruction and compares its generated
fixture with the frozen canonical fixture. This runner is a gate/evidence
tool only and performs no scientific execution.

The Executor-2 process receives only an output path. The canonical fixture is
read only after reconstruction has completed, so it is an equivalence target,
not an Executor-2 construction input.
"""
import hashlib
import json
import os
import subprocess
import sys


def canonical_hash(fixture_without_hash):
    raw = json.dumps(
        fixture_without_hash,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def compare(expected, actual):
    differences = []

    expected_hash = expected.get("fixture_sha256")
    actual_hash = actual.get("fixture_sha256")

    expected_body = dict(expected)
    expected_body.pop("fixture_sha256", None)
    actual_body = dict(actual)
    actual_body.pop("fixture_sha256", None)

    if expected_body != actual_body:
        differences.append("record_or_structure_mismatch")

    if canonical_hash(expected_body) != expected_hash:
        differences.append("canonical_fixture_hash_invalid")

    if canonical_hash(actual_body) != actual_hash:
        differences.append("reconstructed_hash_invalid")

    if expected_hash != actual_hash:
        differences.append("fixture_sha256_mismatch")

    return differences


def main():
    if len(sys.argv) != 3:
        print(
            "usage: TI001_P9_RECONSTRUCTION_RUNNER_001.py "
            "<frozen_fixture.json> <executor2.py>",
            file=sys.stderr,
        )
        return 2

    canonical_path = os.path.abspath(sys.argv[1])
    executor_path = os.path.abspath(sys.argv[2])
    reconstructed_path = os.path.abspath(
        os.path.join(os.path.dirname(canonical_path), "TI001_EXECUTOR_2_RECONSTRUCTED_001.json")
    )

    completed = subprocess.run(
        [sys.executable, executor_path, reconstructed_path],
        capture_output=True,
        text=True,
        check=False,
    )

    if completed.returncode != 0:
        result = {
            "status": "P9_FAIL",
            "failure": "executor_2_nonzero_exit",
            "executor_returncode": completed.returncode,
            "scientific_execution": "NOT_PERFORMED",
        }
        print(json.dumps(result, indent=2, sort_keys=True))
        return 1

    expected = load_json(canonical_path)
    actual = load_json(reconstructed_path)
    differences = compare(expected, actual)

    result = {
        "status": "P9_PASS" if not differences else "P9_FAIL",
        "checks": {
            "executor_2_exit_zero": completed.returncode == 0,
            "canonical_structure_valid": "canonical_fixture_hash_invalid" not in differences,
            "reconstructed_structure_valid": "reconstructed_hash_invalid" not in differences,
            "observable_fixture_equivalence": "record_or_structure_mismatch" not in differences,
            "fixture_sha256_match": "fixture_sha256_mismatch" not in differences,
        },
        "canonical_fixture_sha256": expected.get("fixture_sha256"),
        "reconstructed_fixture_sha256": actual.get("fixture_sha256"),
        "differences": differences,
        "scientific_execution": "NOT_PERFORMED",
    }

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not differences else 1


if __name__ == "__main__":
    raise SystemExit(main())
