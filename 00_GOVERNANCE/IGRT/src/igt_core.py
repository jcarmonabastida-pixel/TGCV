from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
GOV = ROOT / "00_GOVERNANCE"
MANIFEST = GOV / "CANONICAL_STATE.json"
VALIDATOR = GOV / "tools" / "validate_current_state.py"
STATE_DIR = GOV / "IGRT" / "state"
SESSION_STATE = STATE_DIR / "session_state.json"
CONTINUATION_STATE = STATE_DIR / "continuation_state.json"


@dataclass
class SessionState:
    runtime: str
    timestamp_utc: str
    phase: str
    governance_current_state: str
    rma_version: str | None
    matrix_version: str | None
    traceability_version: str | None
    validator_returncode: int
    validator_output: str
    governance_level: str
    material_change: bool
    active_work_item: str | None
    next_action: str


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_manifest() -> dict:
    if not MANIFEST.is_file():
        raise RuntimeError(f"MISSING canonical state manifest: {MANIFEST}")
    try:
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        raise RuntimeError(f"INVALID canonical state manifest: {exc}") from exc


def run_validator() -> tuple[int, str]:
    if not VALIDATOR.is_file():
        return 2, f"MISSING validator: {VALIDATOR}"
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR)],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    output = (proc.stdout + proc.stderr).strip()
    return proc.returncode, output


def current_versions(manifest: dict) -> tuple[str | None, str | None, str | None]:
    versions = manifest.get("current_versions", {})
    return versions.get("rma"), versions.get("claim_matrix"), versions.get("rma_traceability")


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def start_session(active_work_item: str | None = None) -> SessionState:
    manifest = load_manifest()
    rc, output = run_validator()
    rma, matrix, traceability = current_versions(manifest)
    governance_state = "PASS" if rc == 0 and output.startswith("GOVERNANCE_CURRENT_STATE=PASS") else "FAIL"
    state = SessionState(
        runtime="TGCV-IGRT-0.1",
        timestamp_utc=utc_now(),
        phase="SESSION_READY" if governance_state == "PASS" else "SESSION_BLOCKED",
        governance_current_state=governance_state,
        rma_version=rma,
        matrix_version=matrix,
        traceability_version=traceability,
        validator_returncode=rc,
        validator_output=output,
        governance_level="G0",
        material_change=False,
        active_work_item=active_work_item,
        next_action="CONTINUE" if governance_state == "PASS" else "REPAIR_CANONICAL_GOVERNANCE",
    )
    write_json(SESSION_STATE, asdict(state))
    return state


def close_session(material_change: bool = False, active_work_item: str | None = None, continuation_note: str = "") -> dict:
    payload = {
        "runtime": "TGCV-IGRT-0.1",
        "timestamp_utc": utc_now(),
        "phase": "SESSION_CLOSE",
        "material_change": material_change,
        "active_work_item": active_work_item,
        "continuation_note": continuation_note,
        "validator_required": material_change,
    }
    if material_change:
        rc, output = run_validator()
        payload["validator_returncode"] = rc
        payload["validator_output"] = output
        payload["governance_current_state"] = "PASS" if rc == 0 and output.startswith("GOVERNANCE_CURRENT_STATE=PASS") else "FAIL"
    else:
        payload["governance_current_state"] = "NOT_RECHECKED"
    write_json(CONTINUATION_STATE, payload)
    return payload
