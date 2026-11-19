"""Explicit command-line entry point for the C10-S F1 numerical stress gate.

This script executes the deterministic stress runners only when invoked as a
program. Importing this module has no execution side effects. Invocation must
be covered by a separate, current one-shot execution authorization.
"""
from __future__ import annotations

import argparse
import json

from c10s_f1_numerical_stress import (
    run_f1_observation_scale_ladder,
    run_polynomial_stress_grid,
    write_stress_evidence,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the deterministic C10-S F1 numerical stress gate."
    )
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--output-directory", required=True)
    args = parser.parse_args()

    polynomial_result = run_polynomial_stress_grid()
    f1_result = run_f1_observation_scale_ladder()
    evidence = write_stress_evidence(
        args.output_directory,
        polynomial_result=polynomial_result,
        f1_result=f1_result,
        source_commit=args.source_commit,
    )
    print(json.dumps(evidence, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
