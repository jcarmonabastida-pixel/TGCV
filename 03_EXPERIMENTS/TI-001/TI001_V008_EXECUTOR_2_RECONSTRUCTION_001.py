#!/usr/bin/env python3
"""Independent TI-001 V008 Executor-2 deterministic reconstruction.

This implementation is intentionally independent of Executor-1 and the
scientific provider. It reconstructs the canonical fixture from the frozen
V008 design rules only. It never reads the generated fixture.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

FIXTURE_ID = "TI001-V008-FIXTURE-001"
SCHEMA_ID = "TI001-V008-DU-SCHEMA-001"
GENERATOR_ID = "TI001-V008-FIXTURE-GENERATOR-001"
SEED = 20260925
MASK = 0xFFFFFFFF
PRESENTATION_SEED = (SEED ^ 0x9E3779B9) & MASK
EXPECTED_SHA256 = "dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"


def next_state(value: int) -> int:
    value &= MASK
    if value == 0:
        raise ValueError("invalid zero xorshift32 state")
    value = (value ^ ((value << 13) & MASK)) & MASK
    value = (value ^ (value >> 17)) & MASK
    value = (value ^ ((value << 5) & MASK)) & MASK
    if value == 0:
        raise ValueError("xorshift32 reached invalid zero state")
    return value


def shuffle(sequence: list[str], initial_state: int) -> list[str]:
    result = sequence[:]
    state = initial_state & MASK
    if state == 0:
        raise ValueError("invalid zero shuffle seed")
    for index in range(len(result) - 1, 0, -1):
        state = next_state(state)
        other = state % (index + 1)
        result[index], result[other] = result[other], result[index]
    return result


def make_fixture() -> dict:
    conditions = shuffle(["control"] * 70 + ["treatment"] * 70 + ["null"] * 70, SEED)
    orientations = shuffle(["I1_FIRST"] * 105 + ["I2_FIRST"] * 105, PRESENTATION_SEED)

    units = []
    number = 1
    for pair_index in range(210):
        pair_id = f"P{pair_index + 1:03d}"
        condition = conditions[pair_index]
        first = orientations[pair_index]
        order = ("I1_FIRST", "I2_FIRST") if first == "I1_FIRST" else ("I2_FIRST", "I1_FIRST")
        for presentation in order:
            if presentation == "I1_FIRST":
                items = [{"id": "I1", "action": "A"}, {"id": "I2", "action": "B"}]
            else:
                items = [{"id": "I2", "action": "B"}, {"id": "I1", "action": "A"}]
            units.append({
                "decision_id": f"D{number:03d}",
                "pair_id": pair_id,
                "condition": condition,
                "presentation": presentation,
                "context": {"items": items, "item_count": 2},
                "available_actions": ["A", "B"],
                "future_structure": {
                    "successor_realized": False,
                    "future_structure_available": condition == "treatment",
                },
            })
            number += 1

    return {
        "fixture_id": FIXTURE_ID,
        "schema_id": SCHEMA_ID,
        "generator_id": GENERATOR_ID,
        "seed": SEED,
        "decision_units": units,
    }


def canonical_bytes(value: dict) -> bytes:
    return (json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=False) + "\n").encode("utf-8")


def validate(fixture: dict, raw: bytes) -> dict:
    units = fixture["decision_units"]
    pairs = {}
    for unit in units:
        pairs.setdefault(unit["pair_id"], []).append(unit)

    condition_pairs = {name: 0 for name in ("control", "treatment", "null")}
    presentations = {name: 0 for name in ("I1_FIRST", "I2_FIRST")}
    hidden_ok = True
    structure_ok = True
    for pair_id, pair_units in pairs.items():
        if len(pair_units) != 2:
            structure_ok = False
        if pair_units and pair_units[0]["condition"] in condition_pairs:
            condition_pairs[pair_units[0]["condition"]] += 1
        seen = {u["presentation"] for u in pair_units}
        if seen != {"I1_FIRST", "I2_FIRST"}:
            structure_ok = False
    for unit in units:
        presentations[unit["presentation"]] += 1
        visible = set(unit["context"].keys()) | {"available_actions", "future_structure"}
        if any(key in visible for key in ("decision_id", "pair_id", "condition", "presentation")):
            hidden_ok = False
        if unit["future_structure"]["successor_realized"] is not False:
            structure_ok = False

    digest = hashlib.sha256(raw).hexdigest()
    checks = {
        "fixture_identity": fixture.get("fixture_id") == FIXTURE_ID,
        "schema_identity": fixture.get("schema_id") == SCHEMA_ID,
        "generator_identity": fixture.get("generator_id") == GENERATOR_ID,
        "seed_identity": fixture.get("seed") == SEED,
        "pair_count": len(pairs) == 210,
        "decision_count": len(units) == 420,
        "condition_allocation": condition_pairs == {"control": 70, "treatment": 70, "null": 70},
        "presentation_allocation": presentations == {"I1_FIRST": 105, "I2_FIRST": 105},
        "two_units_per_pair": all(len(v) == 2 for v in pairs.values()),
        "complementary_presentation": structure_ok,
        "future_structure_mapping": all(
            u["future_structure"]["future_structure_available"] == (u["condition"] == "treatment")
            for u in units
        ),
        "no_successor_realization": all(not u["future_structure"]["successor_realized"] for u in units),
        "hidden_field_isolation": hidden_ok,
        "action_representation": all(u["available_actions"] == ["A", "B"] for u in units),
        "canonical_ordering": all(
            units[i]["decision_id"] == f"D{i + 1:03d}" and units[i]["pair_id"] == f"P{i // 2 + 1:03d}"
            for i in range(len(units))
        ),
        "canonical_serialization": raw.endswith(b"\n") and not raw.startswith(b"\xef\xbb\xbf"),
        "canonical_sha256": digest == EXPECTED_SHA256,
    }
    return {
        "reconstruction_id": "TI001-V008-EXECUTOR-2-RECONSTRUCTION-001",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "scientific_execution": "NOT_PERFORMED",
        "checks": checks,
        "reconstructed_sha256": digest,
        "expected_sha256": EXPECTED_SHA256,
        "pair_count": len(pairs),
        "decision_count": len(units),
        "condition_pair_counts": condition_pairs,
        "presentation_counts": presentations,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    fixture = make_fixture()
    raw = canonical_bytes(fixture)
    result = validate(fixture, raw)
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
