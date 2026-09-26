import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

spec_path = ROOT / "03_EXPERIMENTS/TI-001/TI_SCIENTIFIC_DESIGN_READINESS_GATE_SPECIFICATION_001.md"
requirements_path = ROOT / "03_EXPERIMENTS/TI-001/TI_DISCRIMINATION_REQUIREMENTS_GATE_SPECIFICATION_001.md"

spec = spec_path.read_text(encoding="utf-8")
requirements_spec = requirements_path.read_text(encoding="utf-8")
v011 = read_json(ROOT / "03_EXPERIMENTS/TI-001/TI001_V011_SCIENTIFIC_CLOSURE_GATE_RESULT_001.json")
consolidation = read_json(ROOT / "03_EXPERIMENTS/TI-001/TI_EVIDENCE_CONSOLIDATION_GATE_RESULT_001.json")
oq = read_json(ROOT / "03_EXPERIMENTS/TI-001/TI_OPEN_QUESTIONS_AND_DISCRIMINATION_GATE_RESULT_001.json")
register = (ROOT / "03_EXPERIMENTS/TI-001/TI_DISCRIMINATION_REGISTER_001.md").read_text(encoding="utf-8")
register_integrity = read_json(ROOT / "03_EXPERIMENTS/TI-001/TI_DISCRIMINATION_REGISTER_INTEGRITY_GATE_RESULT_001.json")
requirements = read_json(ROOT / "03_EXPERIMENTS/TI-001/TI_DISCRIMINATION_REQUIREMENTS_GATE_RESULT_001.json")
closure = read_json(ROOT / "03_EXPERIMENTS/TI-001/TI_DISCRIMINATION_CLOSURE_GATE_RESULT_001.json")

checks = {
    "A1_SPEC_PRESENT": "## Purpose" in spec and "## Required readiness conditions" in spec,
    "A2_V011_CLOSED": v011.get("status") == "CLOSED_FOR_TI001_V011",
    "A3_EVIDENCE_CONSOLIDATED": consolidation.get("status") == "TI_EVIDENCE_CONSOLIDATED",
    "A4_OPEN_QUESTIONS_FORMALIZED": oq.get("status") == "TI_OPEN_QUESTIONS_FORMALIZED",
    "A5_REGISTER_INTEGRITY_PASS": register_integrity.get("status") == "PASS",
    "A6_REQUIREMENTS_PASS": requirements.get("status") == "PASS",
    "A7_CLOSURE_PASS": closure.get("status") == "PASS",
    "A8_SIX_QUESTIONS_PRESERVED": oq.get("details", {}).get("questions_formalized") == 6 and all(q in register for q in ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]),
    "A9_ALTERNATIVES_UNADJUDICATED": register_integrity.get("details", {}).get("alternatives_adjudicated") is False,
    "A10_OUTCOME_INDEPENDENT_OBSERVABLES": "the discriminating observation must be identifiable before inspecting the outcome." in requirements_spec.lower(),
    "A11_DECISION_TRANSFORMATION_VALUE_BOUNDARY": all(x in spec for x in ["decision-level evidence", "transformation-space evidence", "value evidence"]),
    "A12_TRACEABILITY_TO_OPEN_QUESTIONS": "traceable to one or more specific open questions" in spec,
    "A13_DISCRIMINATION_NOT_REPETITION": "rather than merely reproduce V011" in spec,
    "A14_INDEPENDENT_AUDITABILITY": all(x in spec for x in ["independent execution", "auditability", "reproducibility", "pre-specified analysis boundaries"]),
    "A15_NO_FUTURE_EXPERIMENT_DEFINED": "does not define, approve, or authorize a specific future experiment" in spec,
    "A16_NO_EXECUTION_AUTHORIZATION": "authorize scientific execution" in spec,
    "A17_NO_CLAIM_UPGRADE": "upgrade claims" in spec,
    "A18_CORE_UNCHANGED": "modify the TGCV Core" in spec,
    "A19_V011_IMMUTABLE": "mutate V011 scientific results" in spec,
    "A20_FINAL_DISPOSITION_PRESENT": "TI_SCIENTIFIC_DESIGN_READY" in spec,
}

status = "PASS" if all(checks.values()) else "FAIL"
result = {
    "gate_id": "TI-SCIENTIFIC-DESIGN-READINESS-GATE-001",
    "checks": checks,
    "details": {
        "questions_open": 6,
        "v011_closed": v011.get("status") == "CLOSED_FOR_TI001_V011",
        "evidence_consolidated": consolidation.get("status") == "TI_EVIDENCE_CONSOLIDATED",
        "register_integrity_pass": register_integrity.get("status") == "PASS",
        "requirements_pass": requirements.get("status") == "PASS",
        "v012_designed": False,
        "v012_authorized": False,
        "claim_statuses_upgraded": False,
        "core_modified": False,
        "v011_mutated": False,
    },
    "scientific_design_ready": status == "PASS",
    "status": status,
}
print(json.dumps(result, indent=2, ensure_ascii=False))
