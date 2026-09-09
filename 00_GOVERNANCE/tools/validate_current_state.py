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
    if not path.exists(): errors.append(f"MISSING {label}: {path.as_posix()}")

def require_dir(path: Path, label: str):
    if not path.is_dir(): errors.append(f"MISSING {label}: {path.as_posix()}")

rma_current = RMA_DIR / "TGCV_RMA_current.md"
required = [
    (rma_current, "RMA current pointer"),
    (ROOT / "STATUS.md", "STATUS"),
    (ROOT / "CHANGELOG.md", "CHANGELOG"),
    (ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_POST_DOPS23_v0.1.md", "current claim matrix"),
    (RMA_DIR / "TGCV_RMA_v1.5.md", "historical RMA master v1.5"),
    (RMA_DIR / "TGCV_RMA_traceability_v1.5.csv", "historical RMA traceability v1.5"),
    (RMA_DIR / "TGCV_RMA_v1.6.md", "historical RMA master v1.6"),
    (RMA_DIR / "TGCV_RMA_traceability_v1.6.csv", "historical RMA traceability v1.6"),
    (RMA_DIR / "TGCV_RMA_v1.7.md", "current RMA master v1.7"),
    (RMA_DIR / "TGCV_RMA_traceability_v1.7.csv", "current RMA traceability v1.7"),
    (ROOT / "00_GOVERNANCE" / "workflows" / "CURRENT_STATE_PROPAGATION_AND_CONSISTENCY_WORKFLOW_v0.1.md", "propagation workflow"),
    (SCIENCE / "SCIENTIFIC_ASSET_REGISTRY_v0.1.md", "scientific asset registry"),
    (IMPACT_DIR / "D-OPS-24_CANDIDATE_POOL_EXPANSION_DISCOVERY_v0.2.md", "historical D-OPS-24 v0.2 protocol"),
    (IMPACT_DIR / "D-OPS-24_CANDIDATE_POOL_EXPANSION_DISCOVERY_v0.3.md", "historical D-OPS-24 v0.3 protocol"),
    (IMPACT_DIR / "D-OPS-24_CANDIDATE_POOL_EXPANSION_DISCOVERY_v0.4.md", "frozen D-OPS-24 v0.4 protocol"),
    (IMPACT_DIR / "D-OPS-24_PREFLIGHT_v0.4.md", "D-OPS-24 v0.4 preflight"),
    (IMPACT_DIR / "D-OPS-24_DISCOVERY_EXECUTION_LOG_v0.1.md", "historical D-OPS-24 execution log"),
    (IMPACT_DIR / "D-OPS-24_DISCOVERY_SEARCH_LOG_v0.3.md", "historical D-OPS-24 search log"),
    (IMPACT_DIR / "D-OPS-24_F1_Q3_GOVERNANCE_CORRECTION_v0.1.md", "D-OPS-24 F1-Q3 correction"),
    (IMPACT_DIR / "EXT-UPD-3.9_DOPS24_F1_Q3_GOVERNANCE_CORRECTION_v0.1.md", "EXT-UPD-3.9 governance correction"),
    (IMPACT_DIR / "EXT-UPD-4.0_DOPS24_CONTINUATION_DECISION_v0.1.md", "EXT-UPD-4.0 governance decision"),
    (IMPACT_DIR / "EXT-UPD-4.0_DOPS24_CONTINUATION_PROPAGATION_v0.1.md", "EXT-UPD-4.0 propagation"),
    (RMA_DIR / "EXT-UPD-4.0_CONSISTENCY_CLOSURE_v0.1.md", "EXT-UPD-4.0 consistency closure"),
]
for p, label in required: require_file(p, label)
for rel in ("TCP", "Vision_Paper", "Research_Prospectus", "ARM", "RII", "MOI"): require_dir(ASSETS / rel, f"canonical external asset family {rel}")

if rma_current.exists():
    text = rma_current.read_text(encoding="utf-8")
    checks = {
        "TGCV_RMA_v1.7.md": "RMA current pointer does not point to v1.7",
        "EXT-UPD-4.0": "RMA current does not declare EXT-UPD-4.0",
        "D-OPS-24": "RMA current does not declare D-OPS-24",
        "v0.4": "RMA current does not declare D-OPS-24 v0.4",
        "F2-first": "RMA current does not record F2-first continuation",
        "CLOSED / CONSISTENT": "RMA current does not record EXT-UPD-4.0 closure",
        "NOT AUTHORIZED": "RMA current does not record execution boundary",
        "from-scratch": "RMA current scientific reuse rule missing",
        "historical artifact": "RMA current scientific reuse rule missing historical-artifact condition",
    }
    for token, msg in checks.items():
        if token not in text: errors.append(msg)

trace = RMA_DIR / "TGCV_RMA_traceability_v1.7.csv"
if trace.exists():
    with trace.open(encoding="utf-8-sig", newline="") as f: rows = list(csv.DictReader(f))
    ids = {r.get("asset_id") for r in rows}
    required_ids = {"TGCV-CORE-001","TR-131","RUST-DYN-1","RUST-DYN-2","D-OPS-21","D-OPS-22","D-OPS-23","D-OPS-24","TGCV-EXT-TCP-001","TGCV-EXT-VP-001","TGCV-EXT-RP-001","TGCV-EXT-ARM-001","TGCV-EXT-RII-001","TGCV-EXT-MOI-001","SCIENTIFIC-ASSET-REGISTRY","EXT-UPD-3.6","EXT-UPD-3.7","EXT-UPD-3.8","DOPS24-DISCOVERY-PROTOCOL-v0.2","DOPS24-DISCOVERY-PROTOCOL-v0.3","DOPS24-DISCOVERY-PROTOCOL-v0.4","DOPS24-PREFLIGHT-v0.4","DOPS24-DISCOVERY-EXECUTION-v0.1","DOPS24-F1-Q3-CORRECTION","DOPS24-DISCOVERY-SEARCH-v0.3","DOPS24-F1-Q3-GOV-CORRECTION","DOPS24-EXT-UPD-4.0","EXT-UPD-4.0","DOPS24-EXT-UPD-4.0-CLOSURE","RMA-v1.5","RMA-v1.6","RMA-v1.7","RMA-current","STATUS","PROPAGATION-WORKFLOW","VALIDATOR"}
    missing = required_ids - ids
    if missing: errors.append("Traceability missing required assets: " + ", ".join(sorted(missing)))
    for asset_id, expected in {"RMA-v1.5":"HISTORICAL-SUPERSEDED","RMA-v1.6":"HISTORICAL-SUPERSEDED","RMA-v1.7":"CURRENT","DOPS24-DISCOVERY-PROTOCOL-v0.3":"FROZEN-HISTORICAL","DOPS24-DISCOVERY-PROTOCOL-v0.4":"FROZEN","DOPS24-PREFLIGHT-v0.4":"CLOSED","DOPS24-F1-Q3-CORRECTION":"CLOSED","DOPS24-DISCOVERY-SEARCH-v0.3":"STOPPED-GOVERNANCE-HOLD","EXT-UPD-3.8":"CLOSED-CONSISTENT","DOPS24-F1-Q3-GOV-CORRECTION":"CLOSED","DOPS24-EXT-UPD-4.0":"CLOSED","EXT-UPD-4.0":"CLOSED-CONSISTENT","DOPS24-EXT-UPD-4.0-CLOSURE":"CLOSED-CONSISTENT"}.items():
        matches = [r for r in rows if r.get("asset_id") == asset_id]
        if matches and matches[0].get("status") != expected: errors.append(f"Traceability status mismatch for {asset_id}")
    pointer = [r for r in rows if r.get("asset_id") == "RMA-current"]
    if pointer and pointer[0].get("depends_on") != "RMA-v1.7": errors.append("Traceability current pointer does not depend on RMA v1.7")

matrix = ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_POST_DOPS23_v0.1.md"
if matrix.exists():
    m = matrix.read_text(encoding="utf-8")
    for token in ("C03", "C07", "C11", "C13", "C16", "G7"):
        if token not in m: errors.append(f"Current claim matrix missing {token}")

registry = SCIENCE / "SCIENTIFIC_ASSET_REGISTRY_v0.1.md"
if registry.exists():
    s = registry.read_text(encoding="utf-8")
    for token in ("ESA-TGCV-001", "ESA-TGCV-007", "ESA-TGCV-014", "02_LITERATURE/", "from-scratch"):
        if token not in s: errors.append(f"Scientific registry missing required control token {token}")

if errors:
    print("GOVERNANCE_CURRENT_STATE=FAIL")
    for e in errors: print(e)
    sys.exit(1)
print("GOVERNANCE_CURRENT_STATE=PASS")
print("RMA v1.7, current pointer, traceability, STATUS, claim matrix, scientific registry, D-OPS-24 v0.4 frozen protocol/preflight and EXT-UPD-4.0 closure are structurally aligned.")
