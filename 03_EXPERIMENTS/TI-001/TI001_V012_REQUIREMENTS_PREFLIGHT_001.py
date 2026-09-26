#!/usr/bin/env python3
"""TI-001 V012 requirements preflight. No fixture generation or scientific execution."""
import json
from pathlib import Path

SPEC=Path("03_EXPERIMENTS/TI-001/TI001_V012_EXPERIMENTAL_DESIGN_SPECIFICATION_001.md")

def main():
    c=SPEC.read_text(encoding="utf-8")
    checks={
      "R1_Q1_CONSTRUCT":"## 8. Q1 — Construct validity" in c and "null condition" in c and "mechanism perturbation" in c,
      "R2_Q2_PRESENTATION":"## 9. Q2 — Presentation dependence" in c and "P1" in c and "P2" in c,
      "R3_Q3_NULL":"## 10. Q3 — Null/control behaviour" in c and "NULL" in c,
      "R4_Q4_ROBUSTNESS":"## 11. Q4 — Robustness" in c and all(x in c for x in ("O1","O2","O3")),
      "R5_Q5_MECHANISM":"## 12. Q5 — Mechanism" in c and all(x in c for x in ("INTACT","SCRAMBLED","derangement")),
      "R6_Q6_TACC_BRIDGE":"## 13. Q6 — Decision-to-T_acc bridge" in c and "S_t → selected transformation → S_t+1 → T_acc,t+1" in c,
      "R7_PRESENTATION_CLOSED":"two semantically equivalent encodings" in c and "randomized at the decision-unit level" in c,
      "R8_MECHANISM_CLOSED":"descriptor multiset" in c and "derangement for the three-action case" in c and "no action retains its original descriptor" in c,
      "R9_OPERATIONALISATIONS_CLOSED":"three" in c and "72 instances total" in c,
      "R10_RANDOMIZATION_CLOSED":"582031" in c and "balanced allocation" in c,
      "R11_NO_VALUE_PRIMARY":"No ΔV endpoint is part of primary V012 inference." in c,
      "R12_NO_COMPOSITE_SCORE":"No composite TI score is defined." in c,
      "R13_V011_IMMUTABLE":"V011 remains immutable and closed." in c,
      "R14_NO_FIXTURE_YET":"V012 fixture: NOT GENERATED." in c,
      "R15_NO_EXECUTION":"V012 scientific execution: NOT AUTHORIZED." in c
    }
    passed=all(checks.values())
    result={"gate_id":"TI001-V012-REQUIREMENTS-PREFLIGHT-001","checks":checks,"reasons":{} if passed else {k:"required specification element missing" for k,v in checks.items() if not v},"overall_requirements_preflight_pass":passed,"fixture_generation_authorized":False,"scientific_execution_authorized":False,"status":"PASS" if passed else "BLOCKED"}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=="__main__": main()
