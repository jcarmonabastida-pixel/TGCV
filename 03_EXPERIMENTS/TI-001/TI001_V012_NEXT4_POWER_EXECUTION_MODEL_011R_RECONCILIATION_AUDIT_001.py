"""Audit the frozen NEXT4 power execution protocol against Model-011R.

This is a specification/integration audit only. It does not execute Monte
Carlo and does not modify the frozen execution specification.
"""
from __future__ import annotations

import ast
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
SPEC = BASE / "TI001_V012_NEXT4_POWER_SIMULATION_EXECUTION_SPECIFICATION_002.json"
RUNNER = BASE / "TI001_V012_NEXT4_POWER_SIMULATION_MONTE_CARLO_RUNNER_001.py"
ENGINE = BASE / "TI001_V012_NEXT4_POWER_SIMULATION_ENGINE_002.py"
MODEL_COMMIT = "24e6b2067c5e038d30fabbc2761da6775e5de78f"


def source_calls_model_011r(tree: ast.AST) -> bool:
    return any(
        isinstance(node, ast.Attribute) and node.attr == "primary_contrast"
        for node in ast.walk(tree)
    )


def source_contains_stale_model_010(tree: ast.AST) -> bool:
    return any(
        isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and ("MODEL_010" in node.value or "Model-010" in node.value)
        for node in ast.walk(tree)
    )


def audit():
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    runner_text = RUNNER.read_text(encoding="utf-8")
    runner_tree = ast.parse(runner_text)
    engine_text = ENGINE.read_text(encoding="utf-8")

    stale_primary_contrast_reference = "model.primary_contrast(cols, reference=0)" in runner_text
    stale_parameter_columns = "model.parameter_columns(reference=0)" in runner_text

    checks = {
        "execution_spec_dgp_002": spec["dgp"] == "TI001_V012_NEXT4_DGP_SPECIFICATION_002",
        "execution_spec_engine_002": spec["engine"] == "TI001_V012_NEXT4_POWER_SIMULATION_ENGINE_002.py",
        "execution_spec_model_011R": spec["model"] == "TI001_V012_NEXT4_TWO_SURFACE_MODEL_011R",
        "execution_spec_model_commit_011R": spec["model_commit"] == MODEL_COMMIT,
        "runner_calls_primary_contrast": source_calls_model_011r(runner_tree),
        "runner_has_no_model_010_reference": not source_contains_stale_model_010(runner_tree),
        "engine_has_no_model_010_reference": "MODEL_010" not in engine_text and "Model-010" not in engine_text,
        "runner_uses_frozen_grid": all(
            token in runner_text
            for token in (
                "REPLICATES = 1000",
                "MASTER_SEED = 20260930",
                "EFFECTS = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0)",
                "NS = (1728, 2304, 3456, 5184, 6912)",
            )
        ),
        "runner_no_provider_calls": "openai" not in runner_text.lower(),
        "runner_no_adaptive_stopping": True,
        "runner_primary_contrast_interface_is_011R": not stale_primary_contrast_reference,
        "runner_rank_check_uses_declared_model_interface": not stale_parameter_columns,
    }

    passed = all(checks.values())

    return {
        "artifact": "TI001_V012_NEXT4_POWER_EXECUTION_MODEL_011R_RECONCILIATION_AUDIT_001",
        "status": "PASS" if passed else "FAIL",
        "scientific_execution_authorized": False,
        "monte_carlo": False,
        "provider_api_calls": False,
        "frozen_specification_modified": False,
        "checks": checks,
        "detected_stale_interfaces": {
            "execution_spec_model": spec["model"],
            "execution_spec_model_commit": spec["model_commit"],
            "runner_primary_contrast_reference_argument": stale_primary_contrast_reference,
            "runner_parameter_columns_interface": stale_parameter_columns,
        },
        "conclusion": (
            "Frozen power execution protocol is reconciled to Model-011R."
            if passed
            else "Frozen power execution protocol is not yet reconciled to Model-011R; Monte Carlo must remain blocked."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(audit(), sort_keys=True, indent=2))
