from pathlib import Path
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
    return match.group(1)


# 1. Resolve the stable canonical manifest. No scientific or historical version is hardcoded here.
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

# 2. Resolve the sole canonical RMA pointer and its current master dynamically.
rma_pointer = resolved.get("rma")
rma_pointer_text = read_text(rma_pointer, "RMA pointer") if rma_pointer else ""
rma_master_rel = extract(
    rma_pointer_text,
    r"^\*\*Current master:\*\*\s*`([^`]+)`",
    "RMA pointer current master",
)

rma_master = None
rma_version = None
if rma_master_rel:
    rma_master_name = Path(rma_master_rel).name
    rma_master = ROOT / "00_GOVERNANCE" / "rma" / rma_master_name
    require_file(rma_master, "resolved current RMA master")
    if rma_master_rel != rma_master_name:
        fail("RMA current master pointer resolves outside canonical RMA directory")
    version_match = re.search(r"_v(.+)\.md$", rma_master.name)
    if not version_match:
        fail("resolved current RMA master has no parseable version")
    else:
        rma_version = "v" + version_match.group(1)

if rma_master:
    rma_text = read_text(rma_master, "resolved current RMA master")
    if "**Status:** CURRENT / OPERATIVE" not in rma_text:
        fail("resolved current RMA master is not marked CURRENT / OPERATIVE")

# 3. Resolve the canonical Evidence→Claim Matrix dynamically.
matrix_pointer = resolved.get("claim_matrix_pointer")
matrix_pointer_text = read_text(matrix_pointer, "current claim matrix pointer") if matrix_pointer else ""
matrix_rel = extract(
    matrix_pointer_text,
    r"^\*\*Current matrix:\*\*\s*`([^`]+)`",
    "claim matrix pointer current matrix",
)
matrix_version = extract(
    matrix_pointer_text,
    r"^\*\*Current version:\*\*\s*(v[^\s]+)",
    "claim matrix pointer current version",
)

matrix = resolved.get("claim_matrix")
if matrix_rel:
    expected_matrix = ROOT / matrix_rel
    if matrix != expected_matrix:
        fail("canonical matrix manifest and matrix pointer disagree")
    require_file(expected_matrix, "resolved current claim matrix")

matrix_text = read_text(matrix, "current claim matrix") if matrix else ""
matrix_declared_version = extract(
    matrix_text,
    r"^# TGCV — Evidence-to-Claim Matrix — Current\s+(v[^\s]+)",
    "claim matrix declared current version",
)
if matrix_version and matrix_declared_version and matrix_version != matrix_declared_version:
    fail(f"claim matrix version mismatch: pointer {matrix_version} != artifact {matrix_declared_version}")

# 4. Cross-align RMA and matrix without encoding their versions in executable logic.
if rma_pointer_text and matrix_rel:
    declared_matrix_in_rma = extract(
        rma_pointer_text,
        r"^\*\*Current Evidence→Claim Matrix:\*\*\s*`([^`]+)`",
        "RMA pointer current matrix",
    )
    if declared_matrix_in_rma and declared_matrix_in_rma != matrix_rel:
        fail("RMA pointer and matrix pointer disagree")

# 5. Resolve traceability through its stable pointer, then require it to match the resolved RMA version.
trace_pointer = resolved.get("rma_traceability")
trace_pointer_text = read_text(trace_pointer, "current RMA traceability pointer") if trace_pointer else ""
trace_rel = extract(
    trace_pointer_text,
    r"^current_traceability=(.+)$",
    "traceability current target",
)
if trace_rel:
    trace = ROOT / trace_rel
    require_file(trace, "resolved current RMA traceability")
    if rma_version and trace.name != f"TGCV_RMA_traceability_{rma_version}.csv":
        fail("traceability target does not match resolved current RMA version")

# 6. STATUS must point to the same resolved current RMA and matrix.
status = resolved.get("status")
status_text = read_text(status, "STATUS") if status else ""
status_rma = extract(status_text, r"^\*\*Current RMA:\*\*\s*`([^`]+)`", "STATUS current RMA")
status_matrix = extract(status_text, r"^\*\*Current Evidence→Claim Matrix:\*\*\s*`([^`]+)`", "STATUS current matrix")
if rma_master and status_rma:
    expected_rma = rma_master.relative_to(ROOT).as_posix()
    if status_rma != expected_rma:
        fail("STATUS current RMA disagrees with resolved RMA master")
if matrix and status_matrix:
    expected_matrix = matrix.relative_to(ROOT).as_posix()
    if status_matrix != expected_matrix:
        fail("STATUS current matrix disagrees with resolved matrix")

# 7. Stable canonical locations are the sole current pointers.
canonical_current_rma = ROOT / "00_GOVERNANCE" / "rma" / "TGCV_RMA_current.md"
if rma_pointer != canonical_current_rma:
    fail("canonical RMA pointer location mismatch")
canonical_current_matrix = ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md"
if matrix != canonical_current_matrix:
    fail("canonical matrix location mismatch")

if errors:
    print("GOVERNANCE_CURRENT_STATE=FAIL")
    print("\n".join(errors))
    sys.exit(1)

print("GOVERNANCE_CURRENT_STATE=PASS")
print(
    "Canonical current-state pointers resolved and aligned: "
    f"RMA {rma_version or 'unresolved'}, matrix {matrix_declared_version or matrix_version or 'unresolved'}."
)
