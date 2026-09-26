import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASE = ROOT / "03_EXPERIMENTS" / "TI-001"

SPEC = BASE / "TI_DISCRIMINATION_CLOSURE_GATE_SPECIFICATION_001.md"
REGISTER = BASE / "TI_DISCRIMINATION_REGISTER_001.md"
REG_INTEGRITY = BASE / "TI_DISCRIMINATION_REGISTER_INTEGRITY_GATE_RESULT_001.json"
REQ_GATE = BASE / "TI_DISCRIMINATION_REQUIREMENTS_GATE_RESULT_001.json"
OPEN_GATE = BASE / "TI_OPEN_QUESTIONS_AND_DISCRIMINATION_GATE_RESULT_001.json"
CONSOLIDATION = BASE / "TI_EVIDENCE_CONSOLIDATION_GATE_RESULT_001.json"
V011_CLOSURE = BASE / "TI001_V011_SCIENTIFIC_CLOSURE_GATE_RESULT_001.json"

def read(p):
    return p.read_text(encoding="utf-8") if p.exists() else ""

def load(p):
    return json.loads(read(p)) if p.exists() else {}

spec = read(SPEC)
register = read(REGISTER)
reg_integrity = load(REG_INTEGRITY)
req_gate = load(REQ_GATE)
open_gate = load(OPEN_GATE)
consolidation = load(CONSOLIDATION)
v011_closure = load(V011_CLOSURE)

checks = {
    "A1_SPEC_PRESENT": SPEC.exists(),
    "A2_V011_CLOSED": v011_closure.get("status") == "CLOSED_FOR_TI001_V011",
    "A3_EVIDENCE_CONSOLIDATED": consolidation.get("status") == "TI_EVIDENCE_CONSOLIDATED",
    "A4_REGISTER_PRESENT": REGISTER.exists(),
    "A5_EXACTLY_SIX_REGISTER_ENTRIES": len(re.findall(r"^\| Q[1-6] \|", register, re.M)) == 6,
    "A6_REQUIREMENTS_PASS": req_gate.get("status") == "PASS",
    "A7_REGISTER_INTEGRITY_PASS": reg_integrity.get("status") == "PASS",
    "A8_OPEN_QUESTIONS_GATE_PASS": open_gate.get("status") == "TI_OPEN_QUESTIONS_FORMALIZED",
    "A9_ALTERNATIVES_NOT_ADJUDICATED": "not ranked or selected as winners" in register,
    "A10_NO_Q_RESOLVED": "No Q1–Q6 is declared scientifically resolved by V011" in spec,
    "A11_NO_CLAIM_UPGRADE": "No claim status has been upgraded" in spec,
    "A12_CORE_UNCHANGED": "The TGCV Core remains unchanged" in spec,
    "A13_V012_NOT_DESIGNED": "V012 has not been designed or authorized" in spec,
    "A14_V011_IMMUTABLE": "V011 scientific results remain immutable" in spec,
    "A15_NO_EXECUTION_AUTHORIZATION": "authorize scientific execution" in spec,
    "A16_FINAL_DISPOSITION": "TI_DISCRIMINATION_PHASE_CLOSED_FOR_DESIGN" in spec,
}

status = "PASS" if all(checks.values()) else "FAIL"
result = {
    "gate_id": "TI-DISCRIMINATION-CLOSURE-GATE-001",
    "checks": checks,
    "details": {
        "questions_open": 6,
        "v011_closed": checks["A2_V011_CLOSED"],
        "evidence_consolidated": checks["A3_EVIDENCE_CONSOLIDATED"],
        "v012_designed": False,
        "v012_authorized": False,
        "claim_statuses_upgraded": False,
        "core_modified": False,
        "v011_mutated": False,
        "alternatives_adjudicated": False
    },
    "scientific_design_ready": status == "PASS",
    "status": status
}
print(json.dumps(result, indent=2, ensure_ascii=False))
sys.exit(0 if status == "PASS" else 1)
