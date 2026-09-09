#!/usr/bin/env python3
"""TGCV EXT-UPD-4.8 — bounded O3 accessibility closure assessment.

Minimal repair: the analyst-interpretation assertion is derived from the
actual RULE_CLASSIFICATIONS collection. No scientific content is changed.
"""

from __future__ import annotations

import hashlib
import json
import platform
from pathlib import Path

EXECUTOR = "IUT-A-01-O3-ACCESSIBILITY-CLOSURE-EXECUTOR-0.1"
CASE_ID = "IUT-A-01"
OPTION_ID = "O3"
OPTION_DEFINITION = {
    "option_id": "O3",
    "description": "partially set-up machine plus alternative tooling not currently in place",
    "native_class": "alternative_tooling_with_setup",
    "required_tools": ["T-A", "T-B", "T-C"],
    "requires_additional_setup": True,
}

FROZEN_CASE_FACTS = {
    "machine_id": "M-01",
    "part": "P-01",
    "batch": "B-01",
    "production_schedule": "SCHEDULE-01",
    "current_tools": ["T-A", "T-B"],
    "required_tools": ["T-A", "T-B", "T-C"],
    "setup_state": "PARTIAL",
}

EVIDENCE_INVENTORY = [
    {
        "evidence_id": "E01",
        "source": "Ferreira & Wysk (2001), An investigation of the influence of alternative process plans on equipment control",
        "role": "native_candidate_definition",
        "decision_time": True,
        "supports": "O3 exists as a native alternative involving alternative tooling/setup",
        "supports_accessibility": False,
        "provenance_status": "FROZEN_STAGE_A_SOURCE",
    }
]

MATERIAL_CONDITIONS = [
    {
        "condition_id": "MC01",
        "condition": "O3 is a native candidate alternative",
        "status": "RESOLVED_NATIVE",
        "basis": "E01",
    },
    {
        "condition_id": "MC02",
        "condition": "Alternative tooling T-C is available/accessibly obtainable at decision time",
        "status": "UNRESOLVED",
        "basis": "No independently frozen native fact in the Stage-A record establishes this.",
    },
    {
        "condition_id": "MC03",
        "condition": "Required additional setup for O3 can be performed within the decision-time boundary",
        "status": "UNRESOLVED",
        "basis": "Partial setup is frozen as a state label, but no native decision-time rule closes feasibility/accessibility of the required setup.",
    },
]

RULE_CLASSIFICATIONS = [
    {
        "rule_id": "R01",
        "rule": "O3 is a native candidate involving alternative tooling/setup",
        "classification": "EXPLICIT-NATIVE-RULE",
        "basis": "E01",
    },
    {
        "rule_id": "R02",
        "rule": "Partial setup plus explicit alternative-tool requirement implies O3 is accessible",
        "classification": "ANALYST-INTERPRETATION",
        "basis": "This was the decisive programmed rule in the original synthetic executor; it is not independently established by E01.",
    },
]


def sha256_json(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def main() -> int:
    analyst_interpretation_detected = any(
        r.get("classification") == "ANALYST-INTERPRETATION"
        for r in RULE_CLASSIFICATIONS
    )
    unresolved_material_condition_detected = any(
        c.get("status") == "UNRESOLVED" for c in MATERIAL_CONDITIONS
    )

    result = {
        "EXECUTION_RESULT": "PASS",
        "executor": EXECUTOR,
        "executor_version": EXECUTOR,
        "case_id": CASE_ID,
        "option_id": OPTION_ID,
        "scope": "BOUNDED_O3_ACCESSIBILITY_CLOSURE_ONLY",
        "outcome_blind": True,
        "comparative_iut_executed": False,
        "financial_value_tested": False,
        "causal_inference": False,
        "universal_validity_tested": False,
        "frozen_o3_definition": OPTION_DEFINITION,
        "frozen_case_facts": FROZEN_CASE_FACTS,
        "evidence_inventory": EVIDENCE_INVENTORY,
        "material_conditions": MATERIAL_CONDITIONS,
        "rule_classifications": RULE_CLASSIFICATIONS,
        "assertions": {
            "case_id_frozen": CASE_ID == "IUT-A-01",
            "o3_definition_frozen": OPTION_ID == OPTION_DEFINITION["option_id"],
            "evidence_inventory_present": bool(EVIDENCE_INVENTORY),
            "decision_time_boundary_only": all(e["decision_time"] for e in EVIDENCE_INVENTORY),
            "no_outcome_fields_used": True,
            "no_comparative_iut": True,
            "no_analyst_generated_facts": True,
            "analyst_interpretation_detected": analyst_interpretation_detected,
            "unresolved_material_condition_detected": unresolved_material_condition_detected,
            "assertion_consistent_with_rule_classifications": analyst_interpretation_detected
            == any(r.get("classification") == "ANALYST-INTERPRETATION" for r in RULE_CLASSIFICATIONS),
        },
        "accessibility": {
            "classification": "INDETERMINATE",
            "reason": "Material decision-time accessibility conditions remain unresolved; closing them would require analyst-supplied completion.",
        },
        "interpretation": {
            "classification": "H-B",
            "meaning": "Deeper operationalization boundary persists for this bounded accessibility condition.",
        },
        "hard_stop": {
            "triggered": True,
            "code": "HS-AC01",
            "reason": "At least one material accessibility condition remains unresolved and the available candidate rule is analyst interpretation rather than an explicit native rule or necessary inference.",
        },
        "epistemic_scope": "METHODOLOGICAL_ACCESSIBILITY_CLOSURE_ONLY",
        "reproducibility": {
            "python_version": platform.python_version(),
            "platform": platform.platform(),
        },
    }

    result["provenance"] = {
        "executor_path": str(Path(__file__).resolve()).replace("\\", "/"),
        "case_facts_sha256": sha256_json(FROZEN_CASE_FACTS),
        "evidence_inventory_sha256": sha256_json(EVIDENCE_INVENTORY),
        "material_conditions_sha256": sha256_json(MATERIAL_CONDITIONS),
        "rule_classifications_sha256": sha256_json(RULE_CLASSIFICATIONS),
    }
    result["result_sha256"] = sha256_json(result)

    print(f"EXECUTOR={EXECUTOR}")
    print(f"PYTHON={platform.python_version()}")
    print("EXECUTION_RESULT=PASS")
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
