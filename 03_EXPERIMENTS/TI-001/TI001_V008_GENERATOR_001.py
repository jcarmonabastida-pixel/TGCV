#!/usr/bin/env python3
"""TI-001 V008 deterministic fixture generator."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

GENERATOR_ID = "TI001-V008-FIXTURE-GENERATOR-001"
SCHEMA_ID = "TI001-V008-DU-SCHEMA-001"
FIXTURE_ID = "TI001-V008-FIXTURE-001"
SEED = 20260925
MASK32 = 0xFFFFFFFF
PRESENTATION_XOR = 0x9E3779B9
SCHEMA_RELATIVE_PATH = "03_EXPERIMENTS/TI-001/TI001_V008_DECISION_UNIT_SCHEMA_SPECIFICATION_001.md"
GENERATOR_RELATIVE_PATH = "03_EXPERIMENTS/TI-001/TI001_V008_GENERATOR_001.py"

SEED1_VECTORS = [270369, 67634689, 2647435461, 307599695, 2398689233]
CONDITION_VECTORS = [577347236, 639621434, 2049311590, 4078523939, 3799384941]
PRESENTATION_VECTORS = [1936054461, 3325135876, 27233372, 4070243990, 71659122]


def xorshift32(state: int) -> int:
    state &= MASK32
    if state == 0:
        raise ValueError("xorshift32 zero state is invalid")
    state ^= (state << 13) & MASK32
    state &= MASK32
    state ^= state >> 17
    state &= MASK32
    state ^= (state << 5) & MASK32
    return state & MASK32


def stream(seed: int, count: int) -> list[int]:
    state = seed & MASK32
    if state == 0:
        raise ValueError("xorshift32 zero state is invalid")
    values = []
    for _ in range(count):
        state = xorshift32(state)
        values.append(state)
    return values


def fisher_yates(values: list[str], seed: int) -> tuple[list[str], list[tuple[int, int]]]:
    result = list(values)
    swaps = []
    state = seed & MASK32
    if state == 0:
        raise ValueError("xorshift32 zero state is invalid")
    for i in range(len(result) - 1, 0, -1):
        state = xorshift32(state)
        j = state % (i + 1)
        result[i], result[j] = result[j], result[i]
        swaps.append((i, j))
    return result, swaps


def self_test() -> dict:
    checks = {}
    checks["seed1_first5"] = stream(1, 5) == SEED1_VECTORS
    checks["condition_first5"] = stream(SEED, 5) == CONDITION_VECTORS
    presentation_seed = (SEED ^ PRESENTATION_XOR) & MASK32
    checks["presentation_seed"] = presentation_seed == 2667729284
    checks["presentation_first5"] = stream(presentation_seed, 5) == PRESENTATION_VECTORS
    shuffled_condition, condition_swaps = fisher_yates(["a", "b", "c", "d"], SEED)
    checks["condition_fisher_yates"] = shuffled_condition == ["b", "d", "c", "a"] and condition_swaps == [(3, 0), (2, 2), (1, 0)]
    shuffled_presentation, presentation_swaps = fisher_yates(["a", "b", "c", "d"], presentation_seed)
    checks["presentation_fisher_yates"] = shuffled_presentation == ["c", "a", "d", "b"] and presentation_swaps == [(3, 1), (2, 1), (1, 0)]
    passed = all(checks.values())
    return {"generator_id": GENERATOR_ID, "status": "PASS" if passed else "FAIL", "scientific_execution": "NOT_PERFORMED", "checks": checks}


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("utf-8")
    return hashlib.sha1(header + data).hexdigest()


def repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


def source_bindings() -> tuple[str, str]:
    root = repository_root()
    schema_sha = git_blob_sha1((root / SCHEMA_RELATIVE_PATH).read_bytes())
    generator_sha = git_blob_sha1((root / GENERATOR_RELATIVE_PATH).read_bytes())
    return schema_sha, generator_sha


def canonical_json_bytes(payload: dict) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=False) + "\n").encode("utf-8")


def materialize_records(condition_assignment: list[str], presentation_assignment: list[str]) -> list[dict]:
    records = []
    decision_number = 1
    for pair_number in range(1, 211):
        pair_id = f"P{pair_number:03d}"
        condition = condition_assignment[pair_number - 1]
        for presentation in ("I1_FIRST", "I2_FIRST"):
            decision_id = f"D{decision_number:03d}"
            if presentation == "I1_FIRST":
                items = [{"id": "I1", "action": "A"}, {"id": "I2", "action": "B"}]
            else:
                items = [{"id": "I2", "action": "B"}, {"id": "I1", "action": "A"}]
            record = {
                "decision_id": decision_id,
                "pair_id": pair_id,
                "condition": condition,
                "presentation": presentation,
                "context": {"items": items, "item_count": 2},
                "available_actions": ["A", "B"],
                "future_structure": {
                    "successor_realized": False,
                    "future_structure_available": condition == "treatment",
                },
            }
            records.append(record)
            decision_number += 1
    return records


def build_fixture() -> tuple[dict, str, str]:
    condition_labels = ["control"] * 70 + ["treatment"] * 70 + ["null"] * 70
    presentation_labels = ["I1_FIRST"] * 105 + ["I2_FIRST"] * 105
    condition_assignment, _ = fisher_yates(condition_labels, SEED)
    presentation_assignment, _ = fisher_yates(presentation_labels, (SEED ^ PRESENTATION_XOR) & MASK32)
    # Presentation is assigned per pair; the two records in each pair are always complementary.
    # The shuffled stream determines which pair positions receive the pair-level presentation orientation.
    records = []
    decision_number = 1
    for pair_number in range(1, 211):
        pair_id = f"P{pair_number:03d}"
        condition = condition_assignment[pair_number - 1]
        first = presentation_assignment[pair_number - 1]
        presentations = ("I1_FIRST", "I2_FIRST") if first == "I1_FIRST" else ("I2_FIRST", "I1_FIRST")
        for presentation in presentations:
            if presentation == "I1_FIRST":
                items = [{"id": "I1", "action": "A"}, {"id": "I2", "action": "B"}]
            else:
                items = [{"id": "I2", "action": "B"}, {"id": "I1", "action": "A"}]
            records.append({
                "decision_id": f"D{decision_number:03d}",
                "pair_id": pair_id,
                "condition": condition,
                "presentation": presentation,
                "context": {"items": items, "item_count": 2},
                "available_actions": ["A", "B"],
                "future_structure": {"successor_realized": False, "future_structure_available": condition == "treatment"},
            })
            decision_number += 1
    fixture = {"fixture_id": FIXTURE_ID, "schema_id": SCHEMA_ID, "generator_id": GENERATOR_ID, "seed": SEED, "decision_units": records}
    schema_sha, generator_sha = source_bindings()
    return fixture, schema_sha, generator_sha


def generate(binding_manifest: Path, output_dir: Path) -> dict:
    expected = json.loads(binding_manifest.read_text(encoding="utf-8"))
    schema_sha, generator_sha = source_bindings()
    if expected.get("schema_id") != SCHEMA_ID or expected.get("generator_id") != GENERATOR_ID or expected.get("schema_blob_sha1") != schema_sha or expected.get("generator_blob_sha1") != generator_sha:
        raise RuntimeError("BLOCKED: binding manifest does not match the current V008 schema and generator sources.")
    test = self_test()
    if test["status"] != "PASS":
        raise RuntimeError("BLOCKED: deterministic generator self-test failed.")
    fixture, schema_sha, generator_sha = build_fixture()
    fixture_bytes = canonical_json_bytes(fixture)
    fixture_sha256 = hashlib.sha256(fixture_bytes).hexdigest()
    output_dir.mkdir(parents=True, exist_ok=True)
    fixture_path = output_dir / "TI001_V008_FIXTURE_001.json"
    manifest_path = output_dir / "TI001_V008_FIXTURE_001_INTEGRITY_MANIFEST.json"
    fixture_path.write_bytes(fixture_bytes)
    manifest = {
        "fixture_id": FIXTURE_ID, "schema_id": SCHEMA_ID, "generator_id": GENERATOR_ID, "seed": SEED,
        "fixture_sha256": fixture_sha256, "schema_blob_sha1": schema_sha, "generator_blob_sha1": generator_sha,
        "generation_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "generation_environment": {"python": sys.version, "platform": platform.platform()},
        "scientific_execution": "NOT_PERFORMED",
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, separators=(",", ":"), sort_keys=False) + "\n", encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--generate", action="store_true")
    parser.add_argument("--binding-manifest", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("03_EXPERIMENTS/TI-001/generated/V008"))
    args = parser.parse_args()
    if args.self_test:
        print(json.dumps(self_test(), sort_keys=True))
        return
    if args.generate:
        if args.binding_manifest is None:
            raise SystemExit("BLOCKED: V008 fixture generation requires --binding-manifest.")
        print(json.dumps(generate(args.binding_manifest, args.output_dir), sort_keys=True))
        return
    parser.print_help()


if __name__ == "__main__":
    main()