#!/usr/bin/env python3
"""TI-001 V008 deterministic fixture generator.

Design/preflight artifact only. This module never performs scientific execution.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import List


SEED = 20260925
WORD_MASK = 0xFFFFFFFF
SHIFT_A = 13
SHIFT_B = 17
SHIFT_C = 5
GENERATOR_ID = "TI001-V008-FIXTURE-GENERATOR-001"
SELF_TEST_SEED = 1
SELF_TEST_EXPECTED_STATE = None


def xorshift32(state: int) -> int:
    """Marsaglia xorshift32: <<13, >>17, <<5, unsigned 32-bit arithmetic."""
    state &= WORD_MASK
    if state == 0:
        raise ValueError("xorshift32 zero state is not permitted")
    state ^= (state << SHIFT_A) & WORD_MASK
    state ^= state >> SHIFT_B
    state ^= (state << SHIFT_C) & WORD_MASK
    return state & WORD_MASK


def fisher_yates(values: List[str], state: int):
    """In-place descending Fisher-Yates using modulo index mapping."""
    values = list(values)
    for i in range(len(values) - 1, 0, -1):
        state = xorshift32(state)
        j = state % (i + 1)
        values[i], values[j] = values[j], values[i]
    return values, state


def condition_assignment(seed: int, pair_ids: List[str]):
    labels = ["control", "treatment", "null"]
    expanded = []
    for label in labels:
        expanded.extend([label] * 70)
    state = seed
    shuffled, state = fisher_yates(expanded, state)
    return shuffled, state


def presentation_assignment(seed: int, pair_ids: List[str]):
    labels = ["I1_FIRST"] * 105 + ["I2_FIRST"] * 105
    state = seed
    shuffled, state = fisher_yates(labels, state)
    return shuffled, state


def canonical_sha256(value) -> str:
    payload = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def build_assignments(seed: int = SEED):
    pair_ids = [f"P{i:03d}" for i in range(1, 211)]
    conditions, _ = condition_assignment(seed, pair_ids)
    presentations, _ = presentation_assignment(seed, pair_ids)
    return [
        {
            "pair_id": pair_id,
            "condition": condition,
            "presentation_order": presentation,
        }
        for pair_id, condition, presentation in zip(
            pair_ids, conditions, presentations
        )
    ]


def self_test() -> dict:
    if SELF_TEST_EXPECTED_STATE is None:
        return {
            "status": "BLOCKED",
            "reason": "SELF_TEST_EXPECTED_STATE_NOT_BOUND",
            "scientific_execution": "NOT_PERFORMED",
        }
    observed = xorshift32(SELF_TEST_SEED)
    return {
        "status": "PASS" if observed == SELF_TEST_EXPECTED_STATE else "FAIL",
        "seed": SELF_TEST_SEED,
        "observed_state": observed,
        "expected_state": SELF_TEST_EXPECTED_STATE,
        "scientific_execution": "NOT_PERFORMED",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--print-generator-metadata", action="store_true")
    parser.add_argument("--generate", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        print(json.dumps(self_test(), sort_keys=True))
        return

    if args.print_generator_metadata:
        print(
            json.dumps(
                {
                    "generator_id": GENERATOR_ID,
                    "seed": SEED,
                    "word_width": 32,
                    "unsigned_arithmetic": True,
                    "xorshift_shifts": [SHIFT_A, SHIFT_B, SHIFT_C],
                    "zero_state": "rejected",
                    "fisher_yates": "descending",
                    "index_mapping": "state_modulo_(i+1)",
                    "streams": "not_yet_bound",
                    "scientific_execution": "NOT_PERFORMED",
                },
                sort_keys=True,
            )
        )
        return

    if args.generate:
        raise SystemExit(
            "BLOCKED: V008 fixture generation requires completed generator "
            "specification, bound self-test vectors, stream semantics, and "
            "generator preflight."
        )

    parser.print_help()


if __name__ == "__main__":
    main()
