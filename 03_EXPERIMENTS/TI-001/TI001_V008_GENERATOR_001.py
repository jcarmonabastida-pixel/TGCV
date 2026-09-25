#!/usr/bin/env python3
"""TI-001 V008 generator scaffold.

This file deliberately contains no authoritative PRNG implementation yet.
It exists to reserve the generator identity while the complete deterministic
semantics are formalized. It cannot generate a V008 fixture.
"""

from __future__ import annotations

import argparse
import json


GENERATOR_ID = "TI001-V008-FIXTURE-GENERATOR-001"
SEED = 20260925


def generate():
    raise RuntimeError(
        "BLOCKED: authoritative V008 PRNG/Fisher-Yates semantics and "
        "self-test vectors are not yet bound."
    )


def self_test() -> dict:
    return {
        "status": "BLOCKED",
        "reason": "AUTHORITATIVE_GENERATOR_SEMANTICS_NOT_BOUND",
        "scientific_execution": "NOT_PERFORMED",
    }


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
