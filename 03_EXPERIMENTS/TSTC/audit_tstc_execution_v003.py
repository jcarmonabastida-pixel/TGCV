"""Static conformance audit for the TGCV WP2 TSTC execution adapter v003.

Pre-execution only. This audit reads source text and AST structure; it never
imports or executes the TSTC runner.
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
    "trajectory": "_bounded_trajectory",
    "cross_domain_a": "_cross_domain_scenario_c01_to_c03",
    "cross_domain_b": "_cross_domain_scenario_c03_to_c05",
    "execution_entrypoint": "def run_execution():",
    "source_commit": "def _source_commit():",
    "non_claims": '"non_claims"',
}

BOUNDARY_TEXT = {
    "real_data": "No real datasets",
    "network": "network access",
    "causal_claim": "empirical causal inference",
    "value_analysis": "value analysis",
}

EXPECTED_UNIVERSE_IDS = (
    "c01.deploy_A", "c01.deploy_B", "c01.route_A_to_B",
    "c01.route_B_to_A", "c01.restrict_security", "c01.restore_security",
    "c03.query_db", "c03.inspect_repo", "c03.open_pr",
    "c03.complete_task", "c03.modify_repo",
    "c05.start_A", "c05.start_B", "c05.defer_A", "c05.defer_B",
    "c05.redirect_A_to_B", "c05.reduce_power_A",
)

REQUIRED_OUTPUT_FIELDS = {
    "fixture_versions",
    "local_connector_results",
    "cross_domain_results",
    "baseline_comparison",
    "limitations",
    "non_claims",
    "execution_metadata",
}

REQUIRED_METADATA_FIELDS = {
    "source_commit",
    "fixture_manifest_hash",
    "ruleset_hash",
    "transformation_universe_hash",
    "configuration_hash",
    "random_seed",
    "output_hash",
}


def main():
    source = TARGET.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(TARGET))
    function_names = {
        n.name for n in ast.walk(tree)
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
    }

    failures = []
    for name, text in REQUIRED_TEXT.items():
        if text not in source:
            failures.append(f"MISSING_REQUIRED:{name}")

    for name, text in BOUNDARY_TEXT.items():
        if text not in source:
            failures.append(f"MISSING_BOUNDARY_DECLARATION:{name}")

    if "run_execution" not in function_names:
        failures.append("MISSING_FUNCTION:run_execution")

    for function_name in (
        "_cross_domain_scenario_c01_to_c03",
        "_cross_domain_scenario_c03_to_c05",
        "_bounded_trajectory",
    ):
        if function_name not in function_names:
            failures.append(f"MISSING_FUNCTION:{function_name}")

    for transformation_id in EXPECTED_UNIVERSE_IDS:
        if transformation_id not in source:
            failures.append(f"MISSING_U_TAU_ID:{transformation_id}")

    for field in REQUIRED_OUTPUT_FIELDS:
        if f'"{field}"' not in source:
            failures.append(f"MISSING_OUTPUT_FIELD:{field}")

    for field in REQUIRED_METADATA_FIELDS:
        if f'"{field}"' not in source:
            failures.append(f"MISSING_METADATA_FIELD:{field}")

    if "It does not execute C03.modify_repo" not in source:
        failures.append("MISSING_GUARD:C01_C03_does_not_execute_modify_repo")
    if "independent from Scenario A" not in source and "independent" not in source:
        failures.append("MISSING_GUARD:independent_cross_domain_scenarios")

    if failures:
        print("TSTC_EXECUTION_V003_STATIC_AUDIT=BLOCKED")
        for failure in failures:
            print(failure)
        raise SystemExit(1)

    print("TSTC_EXECUTION_V003_STATIC_AUDIT=PASS")
    print("NO_TSTC_EXECUTION_PERFORMED=True")


if __name__ == "__main__":
    main()
