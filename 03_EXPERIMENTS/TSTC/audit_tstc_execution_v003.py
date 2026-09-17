"""Static conformance audit for the TGCV WP2 TSTC execution adapter v003.

This audit is pre-execution only. It reads the execution adapter as source text
and fails closed when mandatory execution-boundary elements are absent.
It does not import or execute the TSTC runner.
"""
from __future__ import annotations

import ast
from pathlib import Path

TARGET = Path(__file__).with_name("tstc_execution_v003.py")

REQUIRED_TEXT = {
    "fixture_version": 'FIXTURE_VERSION = "003"',
    "coupling_c01_c03": '"source_connector": "C01"',
    "coupling_c03_c05": '"source_connector": "C03"',
    "modify_repo": '"c03.modify_repo"',
    "negative_control": "_run_negative_control",
    "baseline": "_baseline_representation",
    "delta": "_delta",
    "cross_domain_a": "_cross_domain_scenario_c01_to_c03",
    "cross_domain_b": "_cross_domain_scenario_c03_to_c05",
    "execution_entrypoint": "def run_execution():",
    "non_claims": '"non_claims"',
}

FORBIDDEN_TEXT = {
    "real_data": "real datasets",
    "network": "network access",
    "causal_claim": "empirical causal inference",
    "value_analysis": "value analysis",
}

REQUIRED_OUTPUT_FIELDS = {
    "fixture_versions",
    "local_connector_results",
    "cross_domain_results",
    "baseline_comparison",
    "limitations",
    "non_claims",
    "execution_metadata",
}


def main():
    source = TARGET.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(TARGET))
    function_names = {n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}

    failures = []
    for name, text in REQUIRED_TEXT.items():
        if text not in source:
            failures.append(f"MISSING_REQUIRED:{name}")

    for name, text in FORBIDDEN_TEXT.items():
        # These phrases are intentionally present only as explicit boundary
        # restrictions in the module. Their presence is therefore required,
        # not a violation; the map documents the safety boundary.
        if text not in source:
            failures.append(f"MISSING_BOUNDARY_DECLARATION:{name}")

    if "run_execution" not in function_names:
        failures.append("MISSING_FUNCTION:run_execution")

    if "_cross_domain_scenario_c01_to_c03" not in function_names:
        failures.append("MISSING_FUNCTION:cross_domain_c01_to_c03")
    if "_cross_domain_scenario_c03_to_c05" not in function_names:
        failures.append("MISSING_FUNCTION:cross_domain_c03_to_c05")

    # Required reproducibility fields. These checks deliberately look for
    # explicit source_commit and output_hash semantics, not merely generic
    # metadata containers.
    if '"source_commit"' not in source and "source_commit" not in source:
        failures.append("MISSING_REPRODUCIBILITY:source_commit")
    if '"output_hash"' not in source:
        failures.append("MISSING_REPRODUCIBILITY:output_hash")
    if '"random_seed"' not in source:
        failures.append("MISSING_REPRODUCIBILITY:random_seed")
    if '"configuration_hash"' not in source:
        failures.append("MISSING_REPRODUCIBILITY:configuration_hash")

    # The execution specification requires a bounded trajectory, not merely
    # before/after T_acc sets.
    if "trajectory" not in source.lower():
        failures.append("MISSING_EXECUTION_BOUNDARY:trajectory")

    # Output-field contract must be visibly represented in the result object.
    for field in REQUIRED_OUTPUT_FIELDS:
        if f'"{field}"' not in source:
            failures.append(f"MISSING_OUTPUT_FIELD:{field}")

    if failures:
        print("TSTC_EXECUTION_V003_STATIC_AUDIT=BLOCKED")
        for failure in failures:
            print(failure)
        raise SystemExit(1)

    print("TSTC_EXECUTION_V003_STATIC_AUDIT=PASS")
    print("NO_TSTC_EXECUTION_PERFORMED=True")


if __name__ == "__main__":
    main()
