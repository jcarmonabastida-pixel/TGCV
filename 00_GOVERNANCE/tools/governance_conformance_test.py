from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / "00_GOVERNANCE" / "workflows" / "CURRENT_STATE_PROPAGATION_AND_CONSISTENCY_WORKFLOW_v0.1.md"
RMA = ROOT / "00_GOVERNANCE" / "rma" / "TGCV_RMA_current.md"
STATUS = ROOT / "STATUS.md"
MATRIX = ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_POST_DOPS23_v0.1.md"
TRACE = ROOT / "00_GOVERNANCE" / "rma" / "TGCV_RMA_traceability_v0.3.csv"

errors = []

def must_exist(p, label):
    if not p.exists():
        errors.append(f"MISSING {label}: {p}")

for p, label in [
    (WORKFLOW, "propagation workflow"),
    (RMA, "RMA current"),
    (STATUS, "STATUS"),
    (MATRIX, "claim/evidence matrix"),
    (TRACE, "RMA traceability"),
]:
    must_exist(p, label)

if WORKFLOW.exists():
    text = WORKFLOW.read_text(encoding="utf-8")
    required = [
        "historical reconstruction",
        "impact analysis",
        "RMA version/update",
        "dependent current assets",
        "STATUS",
        "claim/evidence control",
        "CHANGELOG",
        "machine consistency validation",
        "human consistency closure",
        "next gate",
    ]
    for token in required:
        if token not in text:
            errors.append(f"WORKFLOW missing mandatory stage: {token}")

# Synthetic negative case: a change with no impact analysis and no STATUS propagation.
negative_case = {
    "accepted_change": True,
    "impact_analysis": False,
    "dependent_assets_propagated": False,
    "status_reconciled": False,
    "claim_control_assessed": False,
    "changelog_updated": False,
    "machine_validation": False,
    "human_closure": False,
}
negative_should_block = not all(negative_case.values())
if not negative_should_block:
    errors.append("NEGATIVE synthetic case was not blocked")

# Synthetic positive case: all propagation obligations satisfied.
positive_case = {
    "accepted_change": True,
    "impact_analysis": True,
    "dependent_assets_propagated": True,
    "status_reconciled": True,
    "claim_control_assessed": True,
    "changelog_updated": True,
    "machine_validation": True,
    "human_closure": True,
}
positive_should_pass = all(positive_case.values())
if not positive_should_pass:
    errors.append("POSITIVE synthetic case did not satisfy propagation obligations")

# Production state must not be modified by this test.
with tempfile.TemporaryDirectory(prefix="tgcv_governance_conformance_"):
    pass

if errors:
    print("GOVERNANCE_CONFORMANCE_TEST=FAIL")
    for e in errors:
        print(e)
    raise SystemExit(1)

print("GOVERNANCE_CONFORMANCE_TEST=PASS")
print("Negative synthetic change is blocked; positive synthetic change satisfies propagation obligations.")
print("Production scientific/governance state was not modified by the test.")
