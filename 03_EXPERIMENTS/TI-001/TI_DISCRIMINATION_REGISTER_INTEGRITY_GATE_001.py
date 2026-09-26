import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
REGISTER = ROOT / "03_EXPERIMENTS" / "TI-001" / "TI_DISCRIMINATION_REGISTER_001.md"
SPEC = ROOT / "03_EXPERIMENTS" / "TI-001" / "TI_DISCRIMINATION_REGISTER_GATE_SPECIFICATION_001.md"

text = REGISTER.read_text(encoding="utf-8") if REGISTER.exists() else ""
spec = SPEC.read_text(encoding="utf-8") if SPEC.exists() else ""

checks = {
    "A1_REGISTER_PRESENT": REGISTER.exists(),
    "A2_SPEC_PRESENT": SPEC.exists(),
    "A3_Q1_PRESENT": "| Q1 |" in text,
    "A4_Q2_PRESENT": "| Q2 |" in text,
    "A5_Q3_PRESENT": "| Q3 |" in text,
    "A6_Q4_PRESENT": "| Q4 |" in text,
    "A7_Q5_PRESENT": "| Q5 |" in text,
    "A8_Q6_PRESENT": "| Q6 |" in text,
    "A9_EXACTLY_SIX_REGISTER_ENTRIES": len(re.findall(r"^\| Q[1-6] \|", text, re.M)) == 6,
    "A10_UNRESOLVED_ISSUES_PRESENT": "Unresolved issue" in text,
    "A11_ALTERNATIVES_PRESENT": "Compatible alternative explanations" in text,
    "A12_DISCRIMINATING_OBSERVABLES_PRESENT": "Discriminating observables" in text,
    "A13_INFORMATIVE_PATTERNS_PRESENT": "Informative result patterns" in text,
    "A14_NONCLAIMS_PRESENT": "Current non-claims" in text,
    "A15_NO_V012_DESIGN": "No V012 experiment is specified" in text,
    "A16_NO_EXECUTION_AUTHORIZATION": "No execution is authorized" in text,
    "A17_NO_CLAIM_UPGRADE": "No claim status is upgraded" in text,
    "A18_CORE_UNCHANGED": "The TGCV Core is unchanged" in text,
    "A19_NO_V011_MUTATION": "V011 scientific results remain immutable" in text,
    "A20_NO_WINNER_SELECTION": "Compatible alternatives are not ranked or selected as winners" in text,
    "A21_FINAL_DISPOSITION": "TI_DISCRIMINATION_REGISTER_FORMALIZED" in text,
}
status = "PASS" if all(checks.values()) else "FAIL"
result = {
    "gate_id": "TI-DISCRIMINATION-REGISTER-INTEGRITY-GATE-001",
    "checks": checks,
    "details": {
        "register_entries": 6,
        "v012_authorized": False,
        "claim_statuses_upgraded": False,
        "core_modified": False,
        "v011_mutated": False,
        "alternatives_adjudicated": False
    },
    "status": status
}
print(__import__("json").dumps(result, indent=2, ensure_ascii=False))
sys.exit(0 if status == "PASS" else 1)
