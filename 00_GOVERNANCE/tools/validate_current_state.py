from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[2]
RMA_DIR = ROOT / "00_GOVERNANCE" / "rma"
IMPACT_DIR = ROOT / "00_GOVERNANCE" / "impact"
SCIENCE = ROOT / "02_EXTERNAL_SCIENCE"
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
require_file(RMA_DIR / "TGCV_RMA_v1.3.md", "current RMA master v1.3")
require_file(RMA_DIR / "TGCV_RMA_traceability_v1.3.csv", "current RMA traceability v1.3")
require_file(ROOT / "00_GOVERNANCE" / "workflows" / "CURRENT_STATE_PROPAGATION_AND_CONSISTENCY_WORKFLOW_v0.1.md", "propagation workflow")
for impact in ("EXT-UPD-1R.4_CONSISTENCY_PROPAGATION_v0.1.md", "EXT-UPD-3.1_RP_CONTROLLED_DRAFTING_AND_CONSISTENCY_v0.1.md", "EXT-UPD-3.2_TCP_PROPAGATION_v0.1.md", "EXT-UPD-3.3.5_VP_PROPAGATION_v0.1.md", "EXT-UPD-3.4_ARM_PROPAGATION_v0.1.md", "EXT-UPD-3.5_RII_PROPAGATION_v0.1.md", "EXT-UPD-3.6_SCIENTIFIC_ASSET_RECONCILIATION_v0.1.md", "EXT-UPD-3.6_POST_CLOSURE_RECONCILIATION_v0.1.md", "EXT-UPD-3.6_CONSISTENCY_CLOSURE_v0.1.md", "EXT-UPD-3.7_DOPS24_DISCOVERY_PROTOCOL_FREEZE_v0.1.md"):
    require_file(IMPACT_DIR / impact, f"impact {impact}")
require_file(IMPACT_DIR / "D-OPS-24_CANDIDATE_POOL_EXPANSION_DISCOVERY_v0.2.md", "frozen D-OPS-24 discovery protocol v0.2")
require_file(SCIENCE / "SCIENTIFIC_ASSET_REGISTRY_v0.1.md", "canonical scientific asset registry")
require_file(ASSETS / "ARM" / "TGCV-EXT-ARM-001_v0.1.md", "current ARM v0.1")
require_file(ASSETS / "RII" / "TGCV-EXT-RII-001_v0.1.md", "current RII v0.1")

for rel in ("TCP", "Vision_Paper", "Research_Prospectus", "ARM", "RII", "MOI"):
    require_dir(ASSETS / rel, f"canonical external asset family {rel}")

if rma_current.exists():
    text = rma_current.read_text(encoding="utf-8")
    if "TGCV_RMA_v1.3.md" not in text:
        errors.append("RMA current pointer does not point to v1.3")
    if "D-OPS-24" not in text or "DISCOVERY PROTOCOL" not in text:
        errors.append("RMA current does not declare the frozen D-OPS-24 discovery protocol")
    if "EXT-UPD-3.6 scientific asset reconciliation: CLOSED / CONSISTENT" not in text:
        errors.append("RMA current does not record EXT-UPD-3.6 closed/consistent state")
    if "EXT-UPD-3.7 D-OPS-24 discovery protocol freeze: CLOSED / CONSISTENT" not in text:
        errors.append("RMA current does not record EXT-UPD-3.7 closed/consistent state")
    if "from-scratch" not in text or "historical artifact" not in text:
        errors.append("RMA current scientific reuse rule missing")

matrix_path = ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_POST_DOPS23_v0.1.md"
if matrix_path.exists():
    matrix = matrix_path.read_text(encoding="utf-8")
    for token in ("C03", "C07", "C11", "C13", "C16", "G7"):
        if token not in matrix:
            errors.append(f"Current claim matrix missing {token}")

registry_path = SCIENCE / "SCIENTIFIC_ASSET_REGISTRY_v0.1.md"
if registry_path.exists():
    registry = registry_path.read_text(encoding="utf-8")
    for token in ("ESA-TGCV-001", "ESA-TGCV-007", "ESA-TGCV-014", "02_LITERATURE/", "from-scratch"):
        if token not in registry:
            errors.append(f"Scientific registry missing required control token {token}")

trace = RMA_DIR / "TGCV_RMA_traceability_v1.3.csv"
if trace.exists():
    with trace.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    required_assets = {
        "TGCV-CORE-001", "RUST-DYN-1", "RUST-DYN-2", "TR-131",
        "D-OPS-21", "D-OPS-22", "D-OPS-23", "D-OPS-24",
        "TGCV-EXT-TCP-001", "TGCV-EXT-VP-001", "TGCV-EXT-RP-001",
        "TGCV-EXT-ARM-001", "TGCV-EXT-RII-001", "TGCV-EXT-MOI-001",
        "SCIENTIFIC-ASSET-REGISTRY", "EXT-UPD-3.6", "EXT-UPD-3.7",
        "DOPS24-DISCOVERY-PROTOCOL", "RMA-v1.3", "RMA-current", "STATUS", "PROPAGATION-WORKFLOW", "HISTORICAL-RECONSTRUCTION-WORKFLOW", "VALIDATOR",
        "ESA-TGCV-001", "ESA-TGCV-007", "ESA-TGCV-014"
    }
    ids = {r.get("asset_id") for r in rows}
    missing = required_assets - ids
    if missing:
        errors.append("Traceability missing required assets: " + ", ".join(sorted(missing)))
    for asset_id, expected in {
        "TGCV-EXT-TCP-001": "05_ASSETS/TCP/",
        "TGCV-EXT-VP-001": "05_ASSETS/Vision_Paper/",
        "TGCV-EXT-RP-001": "05_ASSETS/Research_Prospectus/",
        "TGCV-EXT-ARM-001": "05_ASSETS/ARM/",
        "TGCV-EXT-RII-001": "05_ASSETS/RII/",
        "TGCV-EXT-MOI-001": "05_ASSETS/MOI/",
        "SCIENTIFIC-ASSET-REGISTRY": "02_EXTERNAL_SCIENCE/SCIENTIFIC_ASSET_REGISTRY_v0.1.md",
    }.items():
        matches = [r for r in rows if r.get("asset_id") == asset_id]
        if matches and matches[0].get("canonical_location") != expected:
            errors.append(f"Traceability canonical location mismatch for {asset_id}")
    ext = [r for r in rows if r.get("asset_id") == "EXT-UPD-3.6"]
    if ext and ext[0].get("status") != "CLOSED-CONSISTENT":
        errors.append("Traceability does not record EXT-UPD-3.6 closure")
    ext37 = [r for r in rows if r.get("asset_id") == "EXT-UPD-3.7"]
    if ext37 and ext37[0].get("status") != "CLOSED-CONSISTENT":
        errors.append("Traceability does not record EXT-UPD-3.7 closure")
    dops = [r for r in rows if r.get("asset_id") == "DOPS24-DISCOVERY-PROTOCOL"]
    if dops and dops[0].get("status") != "FROZEN":
        errors.append("Traceability does not record D-OPS-24 discovery protocol as frozen")
    rma = [r for r in rows if r.get("asset_id") == "RMA-v1.3"]
    if rma and rma[0].get("status") != "CURRENT":
        errors.append("Traceability does not record RMA v1.3 as current")
    pointer = [r for r in rows if r.get("asset_id") == "RMA-current"]
    if pointer and pointer[0].get("depends_on") != "RMA-v1.3":
        errors.append("Traceability current pointer does not depend on RMA v1.3")

if errors:
    print("GOVERNANCE_CURRENT_STATE=FAIL")
    for e in errors:
        print(e)
    sys.exit(1)

print("GOVERNANCE_CURRENT_STATE=PASS")
print("RMA v1.3, current pointer, traceability, STATUS, claim matrix, propagation impacts, scientific asset registry, D-OPS-24 frozen discovery protocol and canonical external asset structure are structurally aligned.")
