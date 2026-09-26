#!/usr/bin/env python3
"""TI-001 V012 design audit against the persisted Q1-Q6 mapping. No fixture generation or scientific execution."""
import json
from pathlib import Path

SPEC = Path("03_EXPERIMENTS/TI-001/TI001_V012_EXPERIMENTAL_DESIGN_SPECIFICATION_001.md")
MAPPING = Path("03_EXPERIMENTS/TI-001/TI001_V012_DISCRIMINATION_MAPPING_001.md")

def has(text, *terms):
    return all(term in text for term in terms)

def main():
    spec = SPEC.read_text(encoding="utf-8")
    mapping = MAPPING.read_text(encoding="utf-8")

    checks = {
        "A1_SPEC_PRESENT": SPEC.exists(),
        "A2_MAPPING_PRESENT": MAPPING.exists(),
        "A3_Q1_TRACEABLE": has(mapping, "Q1 Construct validity") and has(spec, "## 8. Q1 — Construct validity"),
        "A4_Q2_TRACEABLE": has(mapping, "Q2 Presentation dependence") and has(spec, "## 9. Q2 — Presentation dependence"),
        "A5_Q3_TRACEABLE": has(mapping, "Q3 Null/control behaviour") and has(spec, "## 10. Q3 — Null/control behaviour"),
        "A6_Q4_TRACEABLE": has(mapping, "Q4 Robustness") and has(spec, "## 11. Q4 — Robustness"),
        "A7_Q5_TRACEABLE": has(mapping, "Q5 Mechanism") and has(spec, "## 12. Q5 — Mechanism"),
        "A8_Q6_TRACEABLE": has(mapping, "Q6 Relation to TGCV") and has(spec, "## 13. Q6 — Decision-to-T_acc bridge"),
        "A9_V011_IMMUTABLE": "V011 remains immutable and closed" in spec,
        "A10_NO_V011_POOLING": "pool V011 with V012 observations" in spec,
        "A11_NO_PRIMARY_VALUE_ENDPOINT": "No ΔV endpoint is part of primary V012 inference." in spec,
        "A12_NO_COMPOSITE_TI_SCORE": "No composite TI score is defined." in spec,
        "A13_INDEPENDENT_RECONSTRUCTION": "Executor-2 must reconstruct" in spec,
        "A14_V005_EXCLUDED_AS_IDENTITY": "they are not V012 by identity" in spec,
        "A15_EXECUTION_NOT_AUTHORIZED": "V012 scientific execution: NOT AUTHORIZED." in spec,
        "A16_FIXTURE_NOT_GENERATED": "V012 fixture: NOT GENERATED." in spec,
        "A17_PRESENTATION_FACTOR_DEFINED": has(spec, "### F2 — Presentation", "At least two independently specified"),
        "A18_NULL_DEFINED": has(spec, "### F3 — Null", "excluding future-space information"),
        "A19_MECHANISM_FACTOR_DEFINED": has(spec, "### F4 — Mechanism perturbation", "removed or independently scrambled"),
        "A20_ROBUSTNESS_FACTOR_DEFINED": has(spec, "### F5 — Independent operationalisation", "multiple independently specified"),
        "A21_PRIMARY_ESTIMAND_DEFINED": "Primary behavioural estimand:" in spec,
        "A22_BLOCKING_CRITERIA_DEFINED": "## 15. Blocking and falsification criteria" in spec,
    }

    conditions = [
        "Exact presentation encodings/order scheme are not yet frozen.",
        "Exact mechanism-perturbation construction is not yet frozen.",
        "Exact independent environment/transition instances are not yet specified.",
        "Sample size/randomization details are not yet specified.",
    ]

    passed = all(checks.values())
    result = {
        "gate_id": "TI001-V012-DESIGN-AUDIT-001",
        "checks": checks,
        "reasons": {} if passed else {k: "failed" for k,v in checks.items() if not v},
        "conditions": conditions,
        "overall_design_audit_pass": passed,
        "status": "PASS_WITH_CONDITIONS" if passed else "BLOCKED",
        "fixture_generation_authorized_by_this_audit": False,
        "scientific_execution_authorized": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
