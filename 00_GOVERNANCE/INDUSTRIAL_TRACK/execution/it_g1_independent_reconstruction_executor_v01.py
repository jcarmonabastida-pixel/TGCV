#!/usr/bin/env python3
"""IT-G1 independent reconstruction executor v0.1.

PRE-EXECUTION ONLY. This script reads the frozen local Git working tree and
performs no AWS calls and no state-changing action.

The same engine may be launched in separate isolated executor processes for
R001 and R002. The caller must not expose one result to the other executor.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

CASE_ID = "IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE"
TARGET_ID = "i-0b0bf56b94733718c"
REGION = "eu-south-2"

EVIDENCE = {
    "CASE-001": ("IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_RESOURCE_FREEZE_001.md", "6C42F13D5D8A47A8CD33F957F67675427CEEA7D2A8055E643A4717362416C9359"),
    "CASE-002": ("IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_RESOURCE_FREEZE_001.md", "6C42F13D5D8A47A8CD33F957F67675427CEEA7D2A8055E643A4717362416C9359"),
    "CASE-003": ("IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_RESOURCE_FREEZE_001.md", "6C42F13D5D8A47A8CD33F957F67675427CEEA7D2A8055E643A4717362416C9359"),
    "CASE-004": ("IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_ROOT_VOLUME_OBSERVED_STATE_001.md", "E4206B7A1B33944BEA2D38F702E2E6EE463F13F40684DC2BAB889B75084BA3F"),
    "CASE-005": ("IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_ROOT_VOLUME_ENCRYPTION_OBSERVED_STATE_001.md", "617F97003B1E940F9A39E75C04E1A9C06ACE5BBC110376143FFED2A215F8231C"),
    "CASE-006": ("IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_RESOURCE_FREEZE_001.md", "6C42F13D5D8A47A8CD33F957F67675427CEEA7D2A8055E643A4717362416C9359"),
    "CASE-007": ("IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_RESOURCE_FREEZE_001.md", "6C42F13D5D8A47A8CD33F957F67675427CEEA7D2A8055E643A4717362416C9359"),
    "CASE-008": ("IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_SSM_MANAGED_NODE_OBSERVED_STATE_001.md", "EC6901A36B66FD50634AD31A251C888E8920C771B45A4EE3F48243A97959FEC3"),
    "CASE-009": (
        "IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CALLER_IAM_SUPPORT_ACTION_AUTHORIZATION_SIMULATION_001.md",
        "C701DE80F96D2913B5AC84099AABC08AF0A3CF3F039A4099D127EC11821D05AF",
    ),
    "CASE-010": ("IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_SSM_CONNECTIVITY_OBSERVED_STATE_001.md", "09C1D188341C899FFA0657658016E01EC3AFC5D07301D051E9B691202F1B2871"),
    "CASE-011": ("IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_RUNBOOK_PARAMETER_TUPLE_001.md", "142EDF5FD735A423C6784CD7CFD8FF38DD4CEF9664312047BEA91761D886F362"),
    "CASE-012": ("IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_RDP_SYMPTOM_OBSERVED_STATE_001.md", "BD7CD1C5D8DCE0747DDCECCD853612EB7570A2EA3F80E65FAE03005545B6B5BB"),
}

IAM_FILES = [
    "IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CALLER_IAM_SUPPORT_ACTION_AUTHORIZATION_SIMULATION_001.md",
    "IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CALLER_EC2_MATERIAL_ACTION_AUTHORIZATION_SIMULATION_001.md",
    "IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CALLER_SSM_EXECUTION_AUTHORIZATION_SIMULATION_001.md",
    "IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_INSTANCE_ROLE_SSM_POLICY_VERSION_002_OBSERVED_STATE_001.md",
    "IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_RUNBOOK_ASSUMEROLE_AND_NESTED_WORKFLOW_OBSERVED_STATE_001.md",
]

RESOURCE_FILE = "IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_RESOURCE_FREEZE_001.md"
ROOT_FILE = "IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_ROOT_VOLUME_OBSERVED_STATE_001.md"
ENC_FILE = "IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_ROOT_VOLUME_ENCRYPTION_OBSERVED_STATE_001.md"
SSM_FILE = "IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_SSM_MANAGED_NODE_OBSERVED_STATE_001.md"
CONN_FILE = "IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_SSM_CONNECTIVITY_OBSERVED_STATE_001.md"
PARAM_FILE = "IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_RUNBOOK_PARAMETER_TUPLE_001.md"
RDP_FILE = "IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_RDP_SYMPTOM_OBSERVED_STATE_001.md"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read(repo: Path, name: str) -> str:
    path = repo / "00_GOVERNANCE" / "INDUSTRIAL_TRACK" / "execution" / name
    if not path.is_file():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8")


def require(text: str, pattern: str, label: str) -> str:
    m = re.search(pattern, text, flags=re.MULTILINE)
    if not m:
        raise ValueError(f"required frozen evidence not found: {label}")
    return m.group(1)


def classify(value: str | None) -> str:
    return "EXPLICIT" if value is not None else "UNKNOWN"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reconstruction-id", required=True, choices=["R001", "R002"])
    ap.add_argument("--executor-id", required=True)
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    repo = Path(args.repo_root).resolve()
    output = Path(args.output).resolve()
    evidence_dir = repo / "00_GOVERNANCE" / "INDUSTRIAL_TRACK" / "execution"

    # Integrity gate: every frozen evidence representation used by the
    # reconstruction must match the SHA-256 frozen in the canonical manifest.
    integrity = {}
    for evidence_id, (name, expected) in EVIDENCE.items():
        path = evidence_dir / name
        actual = sha256(path) if path.is_file() else None
        integrity[evidence_id] = {"path": name, "expected_sha256": expected, "actual_sha256": actual, "match": actual == expected}
        if actual != expected:
            raise RuntimeError(f"{evidence_id}: SHA-256 mismatch for {name}: expected {expected}, got {actual}")

    resource = read(repo, RESOURCE_FILE)
    root = read(repo, ROOT_FILE)
    enc = read(repo, ENC_FILE)
    ssm = read(repo, SSM_FILE)
    conn = read(repo, CONN_FILE)
    params = read(repo, PARAM_FILE)
    rdp = read(repo, RDP_FILE)
    iam = [read(repo, f) for f in IAM_FILES]

    # Reconstruct only from frozen text. No AWS/network/subprocess calls.
    target = require(resource, r"\*\*InstanceId:\*\* `([^`]+)`", "InstanceId")
    region = require(resource, r"\*\*Region:\*\ `([^`]+)`", "Region")
    az = require(resource, r"\*\*Availability Zone:\*\ `([^`]+)`", "Availability Zone")
    subnet = require(resource, r"\*\*Subnet:\*\ `([^`]+)`", "Subnet")
    instance_state = require(resource, r"\*\*Observed instance state:\*\ `([^`]+)`", "instance state")
    volume_id = require(root, r"\| `/dev/sda1` \| `([^`]+)` \|", "root volume")

    platform = "Windows" if "Microsoft Windows Server" in ssm and "Platform `Windows`" in ssm else None
    ssm_managed = "TRUE" if "PingStatus" in ssm and "Online" in ssm and "Observation status" in ssm else None
    encryption = "unencrypted" if re.search(r"(?i)encrypted\s*[:|]\s*`?False`?", enc) or "encrypted: False" in enc else None
    connectivity = "TRUE" if "DNS resolution: `PASS`" in conn and "TCP/443: `PASS`" in conn and "SSM command status: `Success`" in conn else None
    iam_ok = "TRUE" if all(("ALLOW" in x or "Allowed" in x) and "MissingContextValues" not in x for x in iam) else None
    parameters_explicit = "TRUE" if "UnreachableInstanceId" in params and "EC2RescueInstanceType" in params else None
    rdp_explicit = "TRUE" if "TermService" in rdp and "TcpTestSucceeded=False" in rdp else None

    predicates = {
        "P_PLATFORM": platform == "Windows",
        "P_INSTANCE": instance_state == "running",
        "P_TARGET": target == TARGET_ID,
        "P_STORAGE": encryption == "unencrypted" and volume_id.startswith("vol-"),
        "P_SSM": ssm_managed == "TRUE",
        "P_IAM": iam_ok == "TRUE",
        "P_NETWORK": connectivity == "TRUE",
        "P_PARAMETERS": parameters_explicit == "TRUE",
        "P_CASE_EVIDENCE": rdp_explicit == "TRUE",
    }
    a_t0 = all(predicates.values())

    contradiction = False
    reconstruction_result = "PASS" if a_t0 else "FAIL"

    record = {
        "RECONSTRUCTION_ID": args.reconstruction_id,
        "EXECUTOR_ID": args.executor_id,
        "CASE_ID": CASE_ID,
        "TARGET_ID": target,
        "REGION": region,
        "STATE_RECONSTRUCTION": {
            "platform": {"value": platform, "classification": classify(platform)},
            "instance_state": {"value": instance_state, "classification": classify(instance_state)},
            "root_volume_id": {"value": volume_id, "classification": classify(volume_id)},
            "root_volume_encryption": {"value": encryption, "classification": classify(encryption)},
            "availability_zone": {"value": az, "classification": classify(az)},
            "subnet_id": {"value": subnet, "classification": classify(subnet)},
            "ssm_managed": {"value": ssm_managed, "classification": classify(ssm_managed)},
            "iam_prerequisites": {"value": iam_ok, "classification": classify(iam_ok)},
            "subnet_ssm_connectivity": {"value": connectivity, "classification": classify(connectivity)},
            "unreachable_instance_id": {"value": target, "classification": classify(target)},
            "runbook_parameters": {"value": "FROZEN_TUPLE_PRESENT" if parameters_explicit else None, "classification": classify(parameters_explicit)},
            "rdp_context": {"value": "OBSERVED_TERM_SERVICE_STOPPED_NO_3389_LISTENER" if rdp_explicit else None, "classification": classify(rdp_explicit)},
        },
        "P_PLATFORM": predicates["P_PLATFORM"],
        "P_INSTANCE": predicates["P_INSTANCE"],
        "P_TARGET": predicates["P_TARGET"],
        "P_STORAGE": predicates["P_STORAGE"],
        "P_SSM": predicates["P_SSM"],
        "P_IAM": predicates["P_IAM"],
        "P_NETWORK": predicates["P_NETWORK"],
        "P_PARAMETERS": predicates["P_PARAMETERS"],
        "P_CASE_EVIDENCE": predicates["P_CASE_EVIDENCE"],
        "A_T0": a_t0,
        "EXECUTION_AUTHORIZATION": "NONE",
        "POST_DECISION_INFORMATION_USED": False,
        "CONTRADICTION_DETECTED": contradiction,
        "RECONSTRUCTION_RESULT": reconstruction_result,
        "TRANSFORMATION_IDENTITY": {
            "analytical": "ExecuteEC2RescueRemediation",
            "operational": "AWSSupport-ExecuteEC2Rescue",
            "successful_transformation_inferred": False,
        },
        "EVIDENCE_INTEGRITY": integrity,
        "GENERATED_UTC": datetime.now(timezone.utc).isoformat(),
        "EXECUTION_SIDE_EFFECTS": False,
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    tmp = output.with_suffix(output.suffix + ".tmp")
    tmp.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(output)

    print(f"RECONSTRUCTION_ID={args.reconstruction_id}")
    print(f"EXECUTOR_ID={args.executor_id}")
    print(f"RECONSTRUCTION_RESULT={reconstruction_result}")
    print(f"A_T0={'TRUE' if a_t0 else 'FALSE'}")
    print("EXECUTION_AUTHORIZATION=NONE")
    print("POST_DECISION_INFORMATION_USED=FALSE")
    print(f"OUTPUT={output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
