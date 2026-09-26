#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = ROOT / "03_EXPERIMENTS/TI-001/TI_OPEN_QUESTIONS_AND_DISCRIMINATION_GATE_SPECIFICATION_001.md"
CLOSURE = ROOT / "03_EXPERIMENTS/TI-001/TI001_V011_SCIENTIFIC_CLOSURE_GATE_RESULT_001.json"
CONSOLIDATION = ROOT / "03_EXPERIMENTS/TI-001/TI_EVIDENCE_CONSOLIDATION_GATE_RESULT_001.json"
MATRIX = ROOT / "00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md"

def load_json(p):
    raw = p.read_text(encoding="utf-8")
    if raw.endswith("\\n"):
        raw = raw[:-2]
    return json.loads(raw)

spec = SPEC.read_text(encoding="utf-8")
matrix = MATRIX.read_text(encoding="utf-8")
closure = load_json(CLOSURE)
consolidation = load_json(CONSOLIDATION)

checks = {
    "A1_SPEC_PRESENT": SPEC.exists(),
    "A2_V011_CLOSED": closure.get("status") == "CLOSED_FOR_TI001_V011",
    "A3_V011_ANALYSIS_PERFORMED": closure.get("scientific_analysis") == "PERFORMED",
    "A4_CONSOLIDATION_PRESENT": CONSOLIDATION.exists(),
    "A5_EVIDENCE_CONSOLIDATED": consolidation.get("status") == "TI_EVIDENCE_CONSOLIDATED",
    "A6_MATRIX_V135_PRESENT": "Evidence-to-Claim Matrix — Current v1.35" in matrix,
    "A7_V011_MATERIAL_SECTION_PRESENT": "Material experimental evidence — TI-001 V011 Transformational Intelligence" in matrix,
    "A8_ESTABLISHED_VS_NONCLAIM_BOUNDARY": "V011 does not establish" in spec,
    "A9_Q1_CONSTRUCT_VALIDITY": "### Q1 — Construct validity" in spec,
    "A10_Q2_PRESENTATION": "### Q2 — Presentation dependence" in spec,
    "A11_Q3_NULL_CONTROL": "### Q3 — Null/control behaviour" in spec,
    "A12_Q4_ROBUSTNESS": "### Q4 — Robustness" in spec,
    "A13_Q5_MECHANISM": "### Q5 — Mechanism" in spec,
    "A14_Q6_TGCV_RELATION": "### Q6 — Relation to TGCV" in spec,
    "A15_DISCRIMINATION_REQUIREMENTS_PRESENT": spec.count("**Discrimination requirement:**") == 6,
    "A16_NO_V012_DESIGN": "create a V012 specification" in spec and "does not:" in spec,
    "A17_NO_EXECUTION_AUTHORIZATION": "authorize scientific execution" in spec,
    "A18_NO_CLAIM_UPGRADE": "upgrade C01–C16" in spec,
    "A19_NO_CORE_MODIFICATION": "modify the TGCV Core" in spec,
    "A20_FINAL_DISPOSITION_DEFINED": "TI_OPEN_QUESTIONS_FORMALIZED" in spec,
}

result = {
    "gate_id": "TI-OPEN-QUESTIONS-AND-DISCRIMINATION-GATE-001",
    "checks": checks,
    "details": {
        "v011_status": closure.get("status"),
        "consolidation_status": consolidation.get("status"),
        "matrix_version": "v1.35" if "Current v1.35" in matrix else None,
        "questions_formalized": 6,
        "discrimination_requirements": 6,
        "v012_authorized": False,
        "claim_statuses_upgraded": False,
        "core_modified": False,
    },
    "status": "TI_OPEN_QUESTIONS_FORMALIZED" if all(checks.values()) else "BLOCKED",
}

out = ROOT / "03_EXPERIMENTS/TI-001/TI_OPEN_QUESTIONS_AND_DISCRIMINATION_GATE_RESULT_001.json"
out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2, ensure_ascii=False))
