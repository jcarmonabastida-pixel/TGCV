from pathlib import Path
import csv
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
RMA_DIR = ROOT / "00_GOVERNANCE" / "rma"

errors = []

def require_file(path: Path, label: str):
    if not path.exists():
        errors.append(f"MISSING {label}: {path.as_posix()}")

rma_current = RMA_DIR / "TGCV_RMA_current.md"
require_file(rma_current, "RMA current pointer")
require_file(ROOT / "STATUS.md", "STATUS")
require_file(ROOT / "CHANGELOG.md", "CHANGELOG")
require_file(ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_POST_DOPS23_v0.1.md", "current claim matrix")
require_file(RMA_DIR / "TGCV_RMA_v0.3.md", "current RMA master v0.3")
require_file(RMA_DIR / "TGCV_RMA_traceability_v0.3.csv", "current RMA traceability")
require_file(ROOT / "00_GOVERNANCE" / "workflows" / "CURRENT_STATE_PROPAGATION_AND_CONSISTENCY_WORKFLOW_v0.1.md", "propagation workflow")

if rma_current.exists():
    text = rma_current.read_text(encoding="utf-8")
    if "TGCV_RMA_v0.3.md" not in text:
        errors.append("RMA current pointer does not point to v0.3")
    if "D-OPS-24" not in text or "NEXT" not in text:
        errors.append("RMA current does not declare D-OPS-24 as next controlled operation")
    if "accepted result/decision → impact analysis → RMA → dependent current assets → STATUS → claim/evidence control → consistency audit → next controlled operation" not in text:
        errors.append("RMA current propagation rule missing")

if (ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_POST_DOPS23_v0.1.md").exists():
    matrix = (ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_POST_DOPS23_v0.1.md").read_text(encoding="utf-8")
    for token in ("C03", "C07", "C11", "C13", "C16", "G7"):
        if token not in matrix:
            errors.append(f"Current claim matrix missing {token}")

trace = RMA_DIR / "TGCV_RMA_traceability_v0.3.csv"
if trace.exists():
    with trace.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    required_assets = {"TGCV-CORE-001", "TGCV-RUST-DYN2-001", "TGCV-DOPS23-001", "TGCV-DOPS24-001", "TGCV-DR044-001"}
    ids = {r.get("asset_id") for r in rows}
    missing = required_assets - ids
    if missing:
        errors.append("Traceability missing required assets: " + ", ".join(sorted(missing)))

if errors:
    print("GOVERNANCE_CURRENT_STATE=FAIL")
    for e in errors:
        print(e)
    sys.exit(1)

print("GOVERNANCE_CURRENT_STATE=PASS")
print("RMA current pointer, current RMA, traceability, STATUS, claim matrix and propagation workflow are structurally present and aligned.")
