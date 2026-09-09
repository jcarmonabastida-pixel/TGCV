from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "00_GOVERNANCE" / "rma"
I = ROOT / "00_GOVERNANCE" / "impact"
S = ROOT / "02_EXTERNAL_SCIENCE"
A = ROOT / "05_ASSETS"
errors = []


def require_file(path, label):
    if not path.exists():
        errors.append(f"MISSING {label}: {path.as_posix()}")


def require_dir(path, label):
    if not path.is_dir():
        errors.append(f"MISSING {label}: {path.as_posix()}")


def require_text(path, label, tokens):
    if not path.exists():
        errors.append(f"MISSING {label}: {path.as_posix()}")
        return
    text = path.read_text(encoding="utf-8")
    for token in tokens:
        if token not in text:
            errors.append(f"{label} missing {token}")

# Canonical current-state artifacts.
for path, label in [
    (R / "TGCV_RMA_current.md", "RMA pointer"),
    (R / "TGCV_RMA_v2.6.md", "RMA v2.6"),
    (R / "TGCV_RMA_traceability_v2.6.csv", "traceability v2.6"),
    (ROOT / "STATUS.md", "STATUS"),
    (ROOT / "CHANGELOG.md", "CHANGELOG"),
    (ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md", "current claim matrix"),
    (ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT_POINTER.md", "current claim matrix pointer"),
    (S / "SCIENTIFIC_ASSET_REGISTRY_v0.1.md", "scientific registry"),
]:
    require_file(path, label)

# Current EXT-UPD-4.6 / 4.7 / 4.8 control chain.
for path, label in [
    (I / "EXT-UPD-4.6_I01_GATE_C_EVIDENCE_CLAIM_IMPACT_ASSESSMENT_v0.1.md", "EXT-UPD-4.6 impact"),
    (I / "EXT-UPD-4.6_I01_PROPAGATION_v0.1.md", "EXT-UPD-4.6 propagation"),
    (I / "EXT-UPD-4.6_I01_CONSISTENCY_CLOSURE_v0.1.md", "EXT-UPD-4.6 closure"),
    (ROOT / "00_GOVERNANCE" / "EXT-UPD-4.8_TGCV_SCIENTIFIC_AND_INDUSTRIAL_APPLICABILITY_REASSESSMENT_DECISION_v0.1.md", "EXT-UPD-4.8 decision"),
    (ROOT / "00_GOVERNANCE" / "D-OPS-24_EXT-UPD-4.8_TGCV_SCIENTIFIC_AND_INDUSTRIAL_APPLICABILITY_REASSESSMENT_DESIGN_v0.1.md", "EXT-UPD-4.8 design"),
    (ROOT / "00_GOVERNANCE" / "D-OPS-24_EXT-UPD-4.8_TGCV_SCIENTIFIC_AND_INDUSTRIAL_APPLICABILITY_REASSESSMENT_DESIGN_AUDIT_v0.1.md", "EXT-UPD-4.8 design audit"),
    (ROOT / "00_GOVERNANCE" / "D-OPS-24_EXT-UPD-4.8_TGCV_SCIENTIFIC_AND_INDUSTRIAL_APPLICABILITY_REASSESSMENT_PREFLIGHT_v0.1.md", "EXT-UPD-4.8 preflight"),
]:
    require_file(path, label)

for family in ("TCP", "Vision_Paper", "Research_Prospectus", "ARM", "RII", "MOI"):
    require_dir(A / family, f"asset family {family}")

# Current RMA pointer must identify the actual current master and current matrix.
require_text(
    R / "TGCV_RMA_current.md",
    "RMA pointer",
    ("TGCV_RMA_v2.6.md", "v0.6", "EXT-UPD-4.6", "I-01", "machine consistency validation"),
)

# Current matrix pointer must agree with matrix v0.6.
require_text(
    ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT_POINTER.md",
    "claim matrix pointer",
    ("EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md", "v0.6", "EXT-UPD-4.6"),
)

matrix = ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md"
require_text(matrix, "claim matrix", ("Current v0.6", "C11", "C16", "I-01"))

# Traceability is versioned with the current RMA; historical v2.5 remains immutable.
trace = R / "TGCV_RMA_traceability_v2.6.csv"
if trace.exists():
    with trace.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    by_id = {row.get("asset_id"): row for row in rows}
    required = {
        "RMA-v2.4": "HISTORICAL-SUPERSEDED",
        "RMA-v2.5": "HISTORICAL-SUPERSEDED",
        "RMA-v2.6": "CURRENT",
        "RMA-current": "CURRENT",
        "CLAIM-MATRIX": "CURRENT",
        "STATUS": "CURRENT",
        "VALIDATOR": "CURRENT",
        "EXT-UPD-4.6-I01-IMPACT": "CLOSED",
        "EXT-UPD-4.6-I01-PROPAGATION": "CLOSED-PROPAGATED",
        "EXT-UPD-4.6-I01-CLOSURE": "CLOSED-CONSISTENT",
    }
    for asset_id, expected in required.items():
        row = by_id.get(asset_id)
        if row is None:
            errors.append(f"Traceability missing {asset_id}")
        elif row.get("status") != expected:
            errors.append(f"Traceability status mismatch {asset_id}: {row.get('status')} != {expected}")
    if by_id.get("RMA-current", {}).get("depends_on") != "RMA-v2.6":
        errors.append("Traceability current pointer mismatch")
    if by_id.get("CLAIM-MATRIX", {}).get("canonical_location") != "00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md":
        errors.append("Traceability claim matrix location mismatch")
    if by_id.get("RMA-v2.6", {}).get("canonical_location") != "00_GOVERNANCE/rma/TGCV_RMA_v2.6.md":
        errors.append("Traceability RMA v2.6 location mismatch")

if errors:
    print("GOVERNANCE_CURRENT_STATE=FAIL")
    print("\n".join(errors))
    sys.exit(1)

print("GOVERNANCE_CURRENT_STATE=PASS")
print("Current RMA v2.6, matrix v0.6, v2.6 traceability, STATUS, validator and EXT-UPD-4.6/4.8 control chain aligned.")
