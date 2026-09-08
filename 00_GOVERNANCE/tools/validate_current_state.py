from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[2]
RMA_DIR = ROOT / "00_GOVERNANCE" / "rma"
ASSETS = ROOT / "05_ASSETS"

errors = []

def require_file(path: Path, label: str):
    if not path.exists():
        errors.append(f"MISSING {label}: {path.as_posix()}")

def require_dir(path: Path, label: str):
    if not path.is_dir():
        errors.append(f"MISSING {label}: {path.as_posix()}")

rma_current = RMA_DIR / "TGCV_RMA_current.md"
require_file(rma_current, "RMA current pointer")
require_file(ROOT / "STATUS.md", "STATUS")
require_file(ROOT / "CHANGELOG.md", "CHANGELOG")
require_file(ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_POST_DOPS23_v0.1.md", "current claim matrix")
require_file(RMA_DIR / "TGCV_RMA_v0.4.md", "current RMA master v0.4")
require_file(RMA_DIR / "TGCV_RMA_traceability_v0.4.csv", "current RMA traceability v0.4")
require_file(ROOT / "00_GOVERNANCE" / "workflows" / "CURRENT_STATE_PROPAGATION_AND_CONSISTENCY_WORKFLOW_v0.1.md", "propagation workflow")
require_file(ROOT / "00_GOVERNANCE" / "impact" / "EXT-UPD-1R.4_CONSISTENCY_PROPAGATION_v0.1.md", "external asset propagation impact")

for rel in ("TCP", "Vision_Paper", "Research_Prospectus", "ARM", "RII", "MOI"):
    require_dir(ASSETS / rel, f"canonical external asset family {rel}")

if rma_current.exists():
    text = rma_current.read_text(encoding="utf-8")
    if "TGCV_RMA_v0.4.md" not in text:
        errors.append("RMA current pointer does not point to v0.4")
    if "D-OPS-24" not in text or "NEXT" not in text:
        errors.append("RMA current does not declare D-OPS-24 as next controlled operation")
    if "accepted result/decision → impact analysis → RMA → dependent current assets → STATUS → claim/evidence control → consistency audit → next controlled operation" not in text:
        errors.append("RMA current propagation rule missing")

matrix_path = ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_POST_DOPS23_v0.1.md"
if matrix_path.exists():
    matrix = matrix_path.read_text(encoding="utf-8")
    for token in ("C03", "C07", "C11", "C13", "C16", "G7"):
        if token not in matrix:
            errors.append(f"Current claim matrix missing {token}")

trace = RMA_DIR / "TGCV_RMA_traceability_v0.4.csv"
if trace.exists():
    with trace.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    required_assets = {
        "TGCV-CORE-001", "TGCV-RUST-DYN2-001", "TGCV-DOPS23-001",
        "TGCV-DOPS24-001", "TGCV-DR044-001", "TGCV-RMA-001",
        "TGCV-EXT-VP-001", "TGCV-EXT-RP-001", "TGCV-EXT-ARM-001",
        "TGCV-EXT-RII-001", "TGCV-EXT-MOI-001"
    }
    ids = {r.get("asset_id") for r in rows}
    missing = required_assets - ids
    if missing:
        errors.append("Traceability missing required assets: " + ", ".join(sorted(missing)))
    for asset_id, expected in {
        "TGCV-EXT-VP-001": "05_ASSETS/Vision_Paper/",
        "TGCV-EXT-RP-001": "05_ASSETS/Research_Prospectus/",
        "TGCV-EXT-ARM-001": "05_ASSETS/ARM/",
        "TGCV-EXT-RII-001": "05_ASSETS/RII/",
        "TGCV-EXT-MOI-001": "05_ASSETS/MOI/",
    }.items():
        matches = [r for r in rows if r.get("asset_id") == asset_id]
        if matches and matches[0].get("canonical_location") != expected:
            errors.append(f"Traceability canonical location mismatch for {asset_id}")

if errors:
    print("GOVERNANCE_CURRENT_STATE=FAIL")
    for e in errors:
        print(e)
    sys.exit(1)

print("GOVERNANCE_CURRENT_STATE=PASS")
print("RMA v0.4, current pointer, traceability, STATUS, claim matrix, propagation record and canonical external asset structure are structurally aligned.")
