"""IT-METH-I Class II AWS-PatchAsgInstance — B0 permissions evidence audit v0.1.

Purpose:
  Read-only follow-up to the closed Phase-B0 accessibility preflight.
  Investigates only the two B0 unresolved dimensions:
    - iam_role_availability
    - operation_permission_availability

Strict boundary:
  - no AWS-PatchAsgInstance execution;
  - no AWS-RunPatchBaseline execution / ssm:SendCommand;
  - no Automation execution;
  - no resource, tag, IAM, baseline, or instance mutation;
  - no retrofit of missing Phase-A frozen role parameters;
  - no use of post-decision outcome data.

This audit is evidentiary only. It may resolve objective IAM facts, but it must
retain UNRESOLVED where effective transformation permission cannot be established
without changing the governed boundary or relying on execution behavior.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CANDIDATE = "AWS-PatchAsgInstance"
COMPARATOR = "DIRECT-AWS-SSM-RUNCOMMAND-PATCHBASELINE"
PROTOCOL = "IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_PHASE_B_ACCESSIBILITY_COMPARISON_PROTOCOL_001.md"
SCHEMA = "IT-METH-I-CLASS-II-AWS-PATCHASGINSTANCE-PHASE-B0-PERMISSIONS-AUDIT-1"


def canonical_json(value: dict[str, Any]) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run_aws(aws: str, args: list[str], region: str) -> tuple[int, Any, str]:
    cmd = [aws, *args, "--region", region, "--output", "json", "--no-cli-pager"]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    out = p.stdout.strip()
    if p.returncode != 0:
        return p.returncode, None, p.stderr.strip()
    try:
        return 0, json.loads(out or "{}"), ""
    except json.JSONDecodeError as exc:
        return 0, None, f"JSON_DECODE_ERROR:{exc}"


def first_nonempty(*values: Any) -> Any:
    for v in values:
        if v not in (None, "", {}, []):
            return v
    return None


def load_json(path: Path) -> dict[str, Any]:
    obj = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise ValueError(f"INVALID_OBJECT:{path}")
    return obj


def phase_a_state(phase_a: dict[str, Any]) -> dict[str, Any]:
    state = first_nonempty(
        phase_a.get("state_vector"),
        (phase_a.get("predecision_freeze") or {}).get("state_vector") if isinstance(phase_a.get("predecision_freeze"), dict) else None,
        (phase_a.get("predecision_state") or {}).get("state_vector") if isinstance(phase_a.get("predecision_state"), dict) else None,
    )
    if not isinstance(state, dict):
        raise ValueError("PHASE_A_STATE_VECTOR_MISSING")
    return state


def extract_ids(phase_a: dict[str, Any]) -> tuple[str, str]:
    state = phase_a_state(phase_a)
    instance_id = first_nonempty(state.get("target_instance_identity"), state.get("instance_id"), (phase_a.get("inputs") or {}).get("instance_id") if isinstance(phase_a.get("inputs"), dict) else None)
    asg = first_nonempty(state.get("asg_identity"), state.get("asg_name"), (phase_a.get("inputs") or {}).get("asg") if isinstance(phase_a.get("inputs"), dict) else None)
    if not instance_id or not asg:
        raise ValueError("PHASE_A_TARGET_OR_ASG_MISSING")
    return str(instance_id), str(asg)


def clean_policy(doc: Any) -> Any:
    if not isinstance(doc, dict):
        return doc
    # Keep policy evidence useful but bounded; the tool is not intended to export secrets.
    return {
        "Version": doc.get("Version"),
        "Statement": doc.get("Statement"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--region", required=True)
    ap.add_argument("--phase-a-record", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, required=True)
    ap.add_argument("--aws-cli", default="aws")
    args = ap.parse_args()

    phase_a = load_json(args.phase_a_record)
    instance_id, asg_name = extract_ids(phase_a)

    raw: dict[str, Any] = {}
    errors: dict[str, str] = {}

    def probe(name: str, cli_args: list[str]) -> Any:
        code, data, err = run_aws(args.aws_cli, cli_args, args.region)
        if code != 0 or data is None:
            errors[name] = err or f"returncode={code}"
            raw[name] = {"returncode": code, "stderr": err}
            return None
        raw[name] = data
        return data

    caller = probe("caller", ["sts", "get-caller-identity"])
    roles = probe("list_roles", ["iam", "list-roles"])
    ssm_doc = probe("describe_automation_document", ["ssm", "describe-document", "--name", CANDIDATE, "--document-format", "JSON"])
    ssm_doc_comp = probe("describe_comparator_document", ["ssm", "describe-document", "--name", "AWS-RunPatchBaseline", "--document-format", "JSON"])
    account_aliases = probe("list_account_aliases", ["iam", "list-account-aliases"])

    role_list = roles.get("Roles", []) if isinstance(roles, dict) else []
    likely_roles = [
        r for r in role_list
        if any(token.lower() in str(r.get("RoleName", "")).lower() for token in ("patch", "ssm", "automation", "lambda", "tgcv"))
    ]

    role_evidence: list[dict[str, Any]] = []
    for r in likely_roles:
        role_name = r.get("RoleName")
        if not role_name:
            continue
        attached = probe(f"attached_policies:{role_name}", ["iam", "list-attached-role-policies", "--role-name", role_name])
        inline = probe(f"inline_policies:{role_name}", ["iam", "list-role-policies", "--role-name", role_name])
        attached_arns = []
        if isinstance(attached, dict):
            for p in attached.get("AttachedPolicies", []) or []:
                attached_arns.append({"PolicyName": p.get("PolicyName"), "PolicyArn": p.get("PolicyArn")})
        inline_names = inline.get("PolicyNames", []) if isinstance(inline, dict) else []
        role_evidence.append({
            "role_name": role_name,
            "arn": r.get("Arn"),
            "path": r.get("Path"),
            "create_date": r.get("CreateDate"),
            "attached_policies": attached_arns,
            "inline_policy_names": inline_names,
        })

    # Explicitly do NOT select any discovered role as a candidate parameter.
    # Phase-A did not freeze role ARNs, so this remains a discovery observation only.
    candidate_roles_frozen = first_nonempty(
        phase_a.get("candidate_transformation"),
        phase_a.get("candidate"),
    )
    frozen_params = candidate_roles_frozen.get("parameters", {}) if isinstance(candidate_roles_frozen, dict) else {}
    frozen_automation_role = frozen_params.get("AutomationAssumeRole") if isinstance(frozen_params, dict) else None
    frozen_lambda_role = frozen_params.get("LambdaRoleArn") if isinstance(frozen_params, dict) else None

    iam_role_status = "PASS" if frozen_automation_role or frozen_lambda_role else "UNRESOLVED"
    iam_role_reason = (
        "One or more frozen candidate role ARNs are present in Phase-A evidence and were retained for objective existence inspection."
        if iam_role_status == "PASS"
        else "Phase-A freezes no candidate role ARN; discovered IAM roles are observational only and cannot be retrofitted into the frozen transformation parameters."
    )

    # Operation permission status remains unresolved by design. A read-only audit can expose
    # caller/document facts but cannot prove the effective service-role execution path without
    # either a frozen role principal, a formal IAM simulation anchor, or actual execution.
    operation_status = "UNRESOLVED"
    operation_reason = "Effective candidate/comparator execution permission remains unresolved under the B0 read-only boundary; no execution or postdecision behavior is used."

    # Determine whether an IAM simulation capability exists for the current caller, without using it
    # to fabricate a candidate role. This is only an availability observation.
    simulation_capability = probe("iam_simulation_self_check", ["iam", "simulate-principal-policy", "--policy-source-arn", "arn:aws:iam::000000000000:role/NONEXISTENT_TGCV_B0_PROBE_ROLE", "--action-names", "ssm:SendCommand", "--resource-arns", "arn:aws:ssm:*:*:document/AWS-RunPatchBaseline"])
    # A failure here is expected for the fake principal or missing permission; it is never interpreted
    # as proof of candidate permission.
    if isinstance(simulation_capability, dict):
        simulation_observation = "SIMULATION_API_RESPONDED"
    else:
        simulation_observation = "SIMULATION_NOT_AVAILABLE_OR_NOT_AUTHORIZED"

    result = {
        "schema": SCHEMA,
        "status": "B0_PERMISSIONS_AUDIT_CAPTURED",
        "protocol": PROTOCOL,
        "candidate": {"identity": CANDIDATE, "execution": "NOT_AUTHORIZED"},
        "comparator": {"identity": COMPARATOR, "execution": "NOT_AUTHORIZED"},
        "common_boundary": {
            "phase_a_record": str(args.phase_a_record),
            "target_instance_id": instance_id,
            "asg_name": asg_name,
            "postdecision_outcomes_used": False,
        },
        "frozen_candidate_parameters": {
            "AutomationAssumeRole": frozen_automation_role,
            "LambdaRoleArn": frozen_lambda_role,
            "retrofit_from_discovered_roles": False,
        },
        "permissions_audit": {
            "iam_role_availability": {
                "status": iam_role_status,
                "reason": iam_role_reason,
                "frozen_roles_inspected": {
                    "AutomationAssumeRole": frozen_automation_role,
                    "LambdaRoleArn": frozen_lambda_role,
                },
                "discovered_likely_roles": role_evidence,
            },
            "operation_permission_availability": {
                "status": operation_status,
                "reason": operation_reason,
                "iam_simulation_observation": simulation_observation,
            },
        },
        "document_observation": {
            "candidate_document_present": bool(isinstance(ssm_doc, dict) and ssm_doc.get("Document")),
            "candidate_document_status": (ssm_doc.get("Document") or {}).get("Status") if isinstance(ssm_doc, dict) else None,
            "candidate_document_arn": (ssm_doc.get("Document") or {}).get("Arn") if isinstance(ssm_doc, dict) else None,
            "comparator_document_present": bool(isinstance(ssm_doc_comp, dict) and ssm_doc_comp.get("Document")),
            "comparator_document_status": (ssm_doc_comp.get("Document") or {}).get("Status") if isinstance(ssm_doc_comp, dict) else None,
            "comparator_document_arn": (ssm_doc_comp.get("Document") or {}).get("Arn") if isinstance(ssm_doc_comp, dict) else None,
        },
        "caller_observation": caller,
        "account_observation": account_aliases,
        "raw_read_only_probes": raw,
        "probe_errors": errors,
        "guard": {
            "candidate_invoked": False,
            "comparator_invoked": False,
            "ssm_send_command_invoked": False,
            "automation_start_invoked": False,
            "iam_mutated": False,
            "fixture_mutated": False,
        },
        "interpretation": {
            "permission_equivalence_established": False,
            "accessibility_superiority_established": False,
            "industrial_utility_assessed": False,
            "class_ii_to_class_i_promotion": False,
        },
        "artifact": {"sha256": None, "sha256_basis": "canonical JSON with artifact.sha256=null"},
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out = args.output_dir / "IT-METH-I_CLASS_II_AWS_PATCHASGINSTANCE_PHASE_B0_PERMISSIONS_AUDIT_RESULT_001.json"
    out.write_bytes(canonical_json(result))
    sealed = json.loads(out.read_text(encoding="utf-8"))
    sealed["artifact"]["sha256"] = sha256_bytes(canonical_json(result))
    out.write_bytes(canonical_json(sealed))

    print(f"PERMISSIONS_AUDIT_STATUS={result['status']}")
    print(f"IAM_ROLE_AVAILABILITY={iam_role_status}")
    print(f"OPERATION_PERMISSION_AVAILABILITY={operation_status}")
    print(f"FROZEN_CANDIDATE_ROLE_ARN_PRESENT={bool(frozen_automation_role or frozen_lambda_role)}")
    print(f"DISCOVERED_LIKELY_IAM_ROLES={len(role_evidence)}")
    print(f"CANDIDATE_DOCUMENT_PRESENT={result['document_observation']['candidate_document_present']}")
    print(f"COMPARATOR_DOCUMENT_PRESENT={result['document_observation']['comparator_document_present']}")
    print(f"IAM_SIMULATION_OBSERVATION={simulation_observation}")
    print("CANDIDATE_EXECUTION=NOT_AUTHORIZED")
    print("COMPARATOR_EXECUTION=NOT_AUTHORIZED")
    print("READ_ONLY_GUARD=PASS")
    print(f"OUTPUT={out}")
    print(f"SHA256={sealed['artifact']['sha256']}")
    print("SHA256_MODE=CANONICAL_CONTENT_HASH_EXCLUDING_SELF_FIELD")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
