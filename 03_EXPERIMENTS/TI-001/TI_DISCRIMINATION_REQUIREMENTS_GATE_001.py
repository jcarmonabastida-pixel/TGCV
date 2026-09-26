import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SPEC = ROOT / "03_EXPERIMENTS" / "TI-001" / "TI_DISCRIMINATION_REQUIREMENTS_GATE_SPECIFICATION_001.md"

text = SPEC.read_text(encoding="utf-8") if SPEC.exists() else ""

checks = {
    "A1_SPEC_PRESENT": SPEC.exists(),
    "A2_Q1_REQUIREMENT_PRESENT": bool(re.search(r"\| Q1 \|.*\|", text)),
    "A3_Q2_REQUIREMENT_PRESENT": bool(re.search(r"\| Q2 \|.*\|", text)),
    "A4_Q3_REQUIREMENT_PRESENT": bool(re.search(r"\| Q3 \|.*\|", text)),
    "A5_Q4_REQUIREMENT_PRESENT": bool(re.search(r"\| Q4 \|.*\|", text)),
    "A6_Q5_REQUIREMENT_PRESENT": bool(re.search(r"\| Q5 \|.*\|", text)),
    "A7_Q6_REQUIREMENT_PRESENT": bool(re.search(r"\| Q6 \|.*\|", text)),
    "A8_EXACTLY_SIX_Q_REQUIREMENTS": len(re.findall(r"^\| Q[1-6] \|", text, re.M)) == 6,
    "A9_PRE_OUTCOME_IDENTIFIABILITY": "identifiable before inspecting the outcome" in text,
    "A10_ALTERNATIVES_REMAIN_EXPLICIT": "remain explicitly represented until evidence discriminates them" in text,
    "A11_REPRODUCIBILITY_NOT_DISCRIMINATION": "reproducibility and construct validity are distinct" in text,
    "A12_DECISION_TRANSFORMATION_VALUE_DISTINCTION": "present decision, future transformation structure, transformation-space consequences, and value endpoints" in text,
    "A13_NO_RETROSPECTIVE_V011_RESOLUTION": "No single result from V011 is to be retrospectively reclassified" in text,
    "A14_NO_V012_DESIGN": "specify V012" in text,
    "A15_NO_EXECUTION_AUTHORIZATION": "authorize scientific execution" in text,
    "A16_NO_CLAIM_UPGRADE": "upgrade claims" in text,
    "A17_NO_CORE_MODIFICATION": "modify the TGCV Core" in text,
    "A18_NO_V011_MUTATION": "mutate V011 scientific results" in text,
    "A19_NO_PREFERRED_ALTERNATIVE": "select a preferred alternative explanation" in text,
    "A20_FINAL_DISPOSITION": "TI_DISCRIMINATION_REQUIREMENTS_FORMALIZED" in text,
}

status = "PASS" if all(checks.values()) else "FAIL"
result = {
    "gate_id": "TI-DISCRIMINATION-REQUIREMENTS-GATE-001",
    "checks": checks,
    "details": {
        "questions_with_requirements": 6,
        "cross_cutting_requirements": 6,
        "v012_designed": False,
        "v012_authorized": False,
        "claim_statuses_upgraded": False,
        "core_modified": False,
        "v011_mutated": False,
        "preferred_alternative_selected": False
    },
    "status": status
}
print(json.dumps(result, indent=2, ensure_ascii=False))
sys.exit(0 if status == "PASS" else 1)
