from pathlib import Path
import csv
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "00_GOVERNANCE" / "CANONICAL_STATE.json"
errors = []


def fail(message):
    errors.append(message)


def require_file(path, label):
    if not path.is_file():
        fail(f"MISSING {label}: {path.as_posix()}")


def read_text(path, label):
    if not path.is_file():
        fail(f"MISSING {label}: {path.as_posix()}")
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:
        fail(f"UNREADABLE {label}: {exc}")
        return ""


def extract(text, pattern, label):
    match = re.search(pattern, text, flags=re.MULTILINE)
    if not match:
        fail(f"{label} declaration missing")
        return None
    return match.group(1).strip()


# 1. Stable manifest: only canonical roles and locations are structural invariants.
require_file(MANIFEST, "canonical state manifest")
if errors:
    print("GOVERNANCE_CURRENT_STATE=FAIL")
    print("\n".join(errors))
    sys.exit(1)
try:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
except Exception as exc:
    fail(f"INVALID canonical state manifest: {exc}")
    manifest = {}

if manifest.get("schema") != "TGCV-CANONICAL-STATE-1":
    fail("canonical state manifest schema mismatch")
if manifest.get("status") != "CURRENT":
    fail("canonical state manifest is not CURRENT")

pointers = manifest.get("pointers")
if not isinstance(pointers, dict):
    fail("canonical state manifest pointers missing or invalid")
    pointers = {}

required_roles = {
    "rma": "RMA pointer",
    "claim_matrix": "current claim matrix",
    "claim_matrix_pointer": "current claim matrix pointer",
    "rma_traceability": "current RMA traceability pointer",
    "status": "STATUS",
    "changelog": "CHANGELOG",
    "scientific_registry": "scientific registry",
    "validator": "validator",
}

resolved = {}
for role, label in required_roles.items():
    value = pointers.get(role)
    if not isinstance(value, str) or not value.strip():
        fail(f"canonical pointer missing {role}")
        continue
    path = ROOT / value
    require_file(path, label)
    resolved[role] = path

canonical_current_rma = ROOT / "00_GOVERNANCE" / "rma" / "TGCV_RMA_current.md"
canonical_current_matrix = ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md"
canonical_traceability_pointer = ROOT / "00_GOVERNANCE" / "rma" / "TGCV_RMA_traceability_current.csv"
if resolved.get("rma") != canonical_current_rma:
    fail("canonical RMA pointer location mismatch")
if resolved.get("claim_matrix") != canonical_current_matrix:
    fail("canonical matrix location mismatch")
if resolved.get("rma_traceability") != canonical_traceability_pointer:
    fail("canonical traceability pointer location mismatch")

# 2. Resolve current RMA dynamically from the stable RMA pointer.
rma_pointer = resolved.get("rma")
rma_pointer_text = read_text(rma_pointer, "RMA pointer") if rma_pointer else ""
rma_master_rel = extract(rma_pointer_text, r"^\*\*Current master:\*\*\s*`([^`]+)`", "RMA pointer current master")
rma_master = None
rma_version = None
if rma_master_rel:
    rma_master_name = Path(rma_master_rel).name
    rma_master = ROOT / "00_GOVERNANCE" / "rma" / rma_master_name
    require_file(rma_master, "resolved current RMA master")
    if rma_master_rel != rma_master_name:
        fail("RMA current master pointer resolves outside canonical RMA directory")
    # Accept semantic versions vN, vN.N, vN.N.N, etc.; never hardcode the current version.
    version_match = re.fullmatch(r"TGCV_RMA_(v\d+(?:\.\d+)*)\.md", rma_master.name)
    if not version_match:
        fail("resolved current RMA master has no parseable semantic version")
    else:
        rma_version = version_match.group(1)
if rma_master:
    rma_text = read_text(rma_master, "resolved current RMA master")
    if "**Status:** CURRENT / OPERATIVE" not in rma_text:
        fail("resolved current RMA master is not marked CURRENT / OPERATIVE")

# 3. Resolve current Evidence→Claim Matrix dynamically.
matrix_pointer = resolved.get("claim_matrix_pointer")
matrix_pointer_text = read_text(matrix_pointer, "current claim matrix pointer") if matrix_pointer else ""
matrix_rel = extract(matrix_pointer_text, r"^\*\*Current matrix:\*\*\s*`([^`]+)`", "claim matrix pointer current matrix")
matrix_version = extract(matrix_pointer_text, r"^\*\*Current version:\*\*\s*(v[^\s]+)", "claim matrix pointer current version")
matrix = resolved.get("claim_matrix")
if matrix_rel:
    expected_matrix = ROOT / matrix_rel
    if matrix != expected_matrix:
        fail("canonical matrix manifest and matrix pointer disagree")
    require_file(expected_matrix, "resolved current claim matrix")
matrix_text = read_text(matrix, "current claim matrix") if matrix else ""
matrix_declared_version = extract(matrix_text, r"^# TGCV — Evidence-to-Claim Matrix — Current\s+(v[^\s]+)", "claim matrix declared current version")
if matrix_version and matrix_declared_version and matrix_version != matrix_declared_version:
    fail(f"claim matrix version mismatch: pointer {matrix_version} != artifact {matrix_declared_version}")
if rma_pointer_text and matrix_rel:
    declared_matrix_in_rma = extract(rma_pointer_text, r"^\*\*Current Evidence→Claim Matrix:\*\*\s*`([^`]+)`", "RMA pointer current matrix")
    if declared_matrix_in_rma and declared_matrix_in_rma != matrix_rel:
        fail("RMA pointer and matrix pointer disagree")

# 4. Traceability is a CSV data asset, not a key/value pointer file.
trace_pointer = resolved.get("rma_traceability")
trace_text = read_text(trace_pointer, "current RMA traceability") if trace_pointer else ""
trace_rows = []
if trace_text:
    try:
        reader = csv.DictReader(trace_text.splitlines())
        expected_fields = {"asset_id", "asset_type", "status", "canonical_location", "depends_on", "notes"}
        if reader.fieldnames is None:
            fail("current RMA traceability CSV header missing")
        else:
            missing = expected_fields - set(reader.fieldnames)
            if missing:
                fail("current RMA traceability CSV missing columns: " + ", ".join(sorted(missing)))
            trace_rows = list(reader)
            if not trace_rows:
                fail("current RMA traceability CSV contains no data rows")
            ids = [row.get("asset_id", "").strip() for row in trace_rows]
            if any(not asset_id for asset_id in ids):
                fail("current RMA traceability contains blank asset_id")
            duplicates = sorted({x for x in ids if ids.count(x) > 1})
            if duplicates:
                fail("current RMA traceability contains duplicate asset_id: " + ", ".join(duplicates))
    except csv.Error as exc:
        fail(f"INVALID current RMA traceability CSV: {exc}")

by_id = {row.get("asset_id", "").strip(): row for row in trace_rows}
for asset_id in ("RMA-current", "TRACEABILITY-current"):
    if asset_id not in by_id:
        fail(f"current RMA traceability missing required row: {asset_id}")

if "RMA-current" in by_id:
    row = by_id["RMA-current"]
    if row.get("status", "").strip() != "CURRENT":
        fail("RMA-current traceability row is not CURRENT")
    if row.get("canonical_location", "").strip() != "00_GOVERNANCE/rma/TGCV_RMA_current.md":
        fail("RMA-current traceability location mismatch")
    # Traceability uses semantic asset identity (RMA-v3.7), while the master uses its filename.
    expected_rma_asset = f"RMA-{rma_version}" if rma_version else None
    dependencies = {item.strip() for item in row.get("depends_on", "").split(";") if item.strip()}
    if expected_rma_asset and expected_rma_asset not in dependencies:
        fail("RMA-current traceability does not resolve to the current RMA master")

if "TRACEABILITY-current" in by_id:
    row = by_id["TRACEABILITY-current"]
    if row.get("status", "").strip() != "CURRENT":
        fail("TRACEABILITY-current traceability row is not CURRENT")
    if row.get("canonical_location", "").strip() != "00_GOVERNANCE/rma/TGCV_RMA_traceability_current.csv":
        fail("TRACEABILITY-current canonical location mismatch")
    if row.get("depends_on", "").strip() != "RMA-current":
        fail("TRACEABILITY-current must depend on RMA-current")

if rma_version:
    versioned_trace = ROOT / "00_GOVERNANCE" / "rma" / f"TGCV_RMA_traceability_{rma_version}.csv"
    require_file(versioned_trace, "versioned current RMA traceability")

# 5. STATUS aligns with stable canonical locations and the resolved matrix.
status = resolved.get("status")
status_text = read_text(status, "STATUS") if status else ""
status_rma = extract(status_text, r"^\*\*Current RMA:\*\*\s*`([^`]+)`", "STATUS current RMA")
status_matrix = extract(status_text, r"^\*\*Current Evidence→Claim Matrix:\*\*\s*`([^`]+)`", "STATUS current matrix")
if status_rma and status_rma != canonical_current_rma.relative_to(ROOT).as_posix():
    fail("STATUS current RMA must reference the stable canonical RMA pointer")
if matrix and status_matrix and status_matrix != matrix.relative_to(ROOT).as_posix():
    fail("STATUS current matrix disagrees with resolved matrix")

# 6. Canonical validator location is itself stable.
validator = resolved.get("validator")
if validator and validator != ROOT / "00_GOVERNANCE" / "tools" / "validate_current_state.py":
    fail("canonical validator location mismatch")

if errors:
    print("GOVERNANCE_CURRENT_STATE=FAIL")
    print("\n".join(errors))
    sys.exit(1)

print("GOVERNANCE_CURRENT_STATE=PASS")
print(
    "Canonical current-state pointers resolved and aligned: "
    f"RMA {rma_version or 'unresolved'}, matrix {matrix_declared_version or matrix_version or 'unresolved'}, "
    "traceability CSV structurally and semantically aligned."
)
