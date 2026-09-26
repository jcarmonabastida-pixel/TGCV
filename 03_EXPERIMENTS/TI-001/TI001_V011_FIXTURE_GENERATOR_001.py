#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path

SEED = 20260926
MASK = 0xFFFFFFFF
PRESENTATION_XOR = 0x9E3779B9
GENERATOR_ID = "TI001-V011-FIXTURE-GENERATOR-001"
FIXTURE_ID = "TI001-V011-FIXTURE-001"
SCHEMA_ID = "TI001-V011-DU-SCHEMA-001"
CONDITIONS = ("control", "treatment", "null")
PRESENTATIONS = ("I1_FIRST", "I2_FIRST")


class XorShift32:
    def __init__(self, seed):
        seed &= MASK
        if seed == 0:
            raise ValueError("zero seed is invalid")
        self.state = seed

    def next(self):
        x = self.state
        x ^= (x << 13) & MASK
        x ^= x >> 17
        x ^= (x << 5) & MASK
        self.state = x & MASK
        if self.state == 0:
            raise RuntimeError("xorshift32 reached forbidden zero state")
        return self.state


def fisher_yates(values, prng):
    values = list(values)
    for i in range(len(values) - 1, 0, -1):
        j = prng.next() % (i + 1)
        values[i], values[j] = values[j], values[i]
    return values


def build_fixture():
    condition_labels = (
        ["control"] * 70
        + ["treatment"] * 70
        + ["null"] * 70
    )
    presentation_labels = (
        ["I1_FIRST"] * 105
        + ["I2_FIRST"] * 105
    )

    condition_assignment = fisher_yates(
        condition_labels, XorShift32(SEED)
    )
    first_presentation = fisher_yates(
        presentation_labels,
        XorShift32((SEED ^ PRESENTATION_XOR) & MASK),
    )

    decision_units = []
    for pair_index in range(210):
        pair_id = f"P{pair_index + 1:03d}"
        condition = condition_assignment[pair_index]
        first = first_presentation[pair_index]
        second = "I2_FIRST" if first == "I1_FIRST" else "I1_FIRST"
        for offset, presentation in enumerate((first, second)):
            decision_id = f"D{pair_index * 2 + offset + 1:03d}"
            if presentation == "I1_FIRST":
                items = [
                    {"id": "I1", "action": "A"},
                    {"id": "I2", "action": "B"},
                ]
            else:
                items = [
                    {"id": "I2", "action": "B"},
                    {"id": "I1", "action": "A"},
                ]
            decision_units.append(
                {
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
            )

    return {
        "fixture_id": FIXTURE_ID,
        "schema_id": SCHEMA_ID,
        "generator_id": GENERATOR_ID,
        "seed": SEED,
        "decision_units": decision_units,
    }


def validate(fixture):
    units = fixture["decision_units"]
    assert len(units) == 420
    assert len({u["decision_id"] for u in units}) == 420
    assert len({u["pair_id"] for u in units}) == 210

    by_pair = {}
    for unit in units:
        by_pair.setdefault(unit["pair_id"], []).append(unit)

    assert all(len(v) == 2 for v in by_pair.values())
    assert all(
        {v[0]["presentation"], v[1]["presentation"]}
        == {"I1_FIRST", "I2_FIRST"}
        for v in by_pair.values()
    )

    condition_pairs = {c: 0 for c in CONDITIONS}
    first_counts = {c: {"I1_FIRST": 0, "I2_FIRST": 0} for c in CONDITIONS}
    unit_counts = {c: 0 for c in CONDITIONS}
    presentation_counts = {"I1_FIRST": 0, "I2_FIRST": 0}

    for pair_id, pair in by_pair.items():
        condition = pair[0]["condition"]
        assert condition in CONDITIONS
        assert pair[1]["condition"] == condition
        condition_pairs[condition] += 1
        unit_counts[condition] += 2
        first_counts[condition][pair[0]["presentation"]] += 1
        presentation_counts[pair[0]["presentation"]] += 1
        presentation_counts[pair[1]["presentation"]] += 1

    assert condition_pairs == {"control": 70, "treatment": 70, "null": 70}
    assert unit_counts == {"control": 140, "treatment": 140, "null": 140}
    assert presentation_counts == {"I1_FIRST": 210, "I2_FIRST": 210}
    assert all(
        first_counts[c] == {"I1_FIRST": 35, "I2_FIRST": 35}
        for c in CONDITIONS
    )

    expected_keys = [
        "decision_id",
        "pair_id",
        "condition",
        "presentation",
        "context",
        "available_actions",
        "future_structure",
    ]
    for unit in units:
        assert list(unit.keys()) == expected_keys
        assert list(unit["context"].keys()) == ["items", "item_count"]
        assert unit["context"]["item_count"] == 2
        assert unit["available_actions"] == ["A", "B"]
        assert list(unit["future_structure"].keys()) == [
            "successor_realized",
            "future_structure_available",
        ]
        assert unit["future_structure"]["successor_realized"] is False
        assert unit["future_structure"]["future_structure_available"] is (
            unit["condition"] == "treatment"
        )


def serialize(fixture):
    return (
        json.dumps(fixture, ensure_ascii=False, separators=(",", ":"))
        + "\n"
    ).encode("utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    fixture = build_fixture()
    validate(fixture)
    data = serialize(fixture)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(data)

    print(
        json.dumps(
            {
                "generator_id": GENERATOR_ID,
                "fixture_id": FIXTURE_ID,
                "seed": SEED,
                "decision_count": len(fixture["decision_units"]),
                "sha256": hashlib.sha256(data).hexdigest(),
                "scientific_execution": "NOT_PERFORMED",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
