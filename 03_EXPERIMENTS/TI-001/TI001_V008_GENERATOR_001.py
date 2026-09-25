#!/usr/bin/env python3
"""TI-001 V008 deterministic fixture generator."""

from __future__ import annotations

import argparse
import json

GENERATOR_ID = "TI001-V008-FIXTURE-GENERATOR-001"
SEED = 20260925
MASK32 = 0xFFFFFFFF
PRESENTATION_XOR = 0x9E3779B9

SEED1_VECTORS = [
    270369,
    67634689,
    2647435461,
    307599695,
    2398689233,
]
CONDITION_VECTORS = [
    577347236,
    639621434,
    2049311590,
    4078523939,
    3799384941,
]
PRESENTATION_VECTORS = [
    1936054461,
    3325135876,
    27233372,
    4070243990,
    71659122,
]


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
    checks["presentation_first5"] = (
        stream(presentation_seed, 5) == PRESENTATION_VECTORS
    )

    shuffled_condition, condition_swaps = fisher_yates(
        ["a", "b", "c", "d"], SEED
    )
    checks["condition_fisher_yates"] = (
        shuffled_condition == ["b", "d", "c", "a"]
        and condition_swaps == [(3, 0), (2, 2), (1, 0)]
    )

    shuffled_presentation, presentation_swaps = fisher_yates(
        ["a", "b", "c", "d"], presentation_seed
    )
    checks["presentation_fisher_yates"] = (
        shuffled_presentation == ["c", "a", "d", "b"]
        and presentation_swaps == [(3, 1), (2, 1), (1, 0)]
    )

    passed = all(checks.values())
    return {
        "generator_id": GENERATOR_ID,
        "status": "PASS" if passed else "FAIL",
        "scientific_execution": "NOT_PERFORMED",
        "checks": checks,
    }


def generate():
    raise RuntimeError(
        "BLOCKED: V008 fixture generation requires generator preflight "
        "and source hash binding."
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--generate", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        print(json.dumps(self_test(), sort_keys=True))
        return

    if args.generate:
        generate()
        return

    parser.print_help()


if __name__ == "__main__":
    main()
