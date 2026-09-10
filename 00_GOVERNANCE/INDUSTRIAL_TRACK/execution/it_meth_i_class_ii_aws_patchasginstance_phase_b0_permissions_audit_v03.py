"""IT-METH-I Class II AWS-PatchAsgInstance — B0 permissions evidence audit v0.3.

Correction over v0.2:
  The Phase-A sentinel ``OMITTED_UNLESS_FROZEN`` is not a frozen ARN.
  It is treated as absent evidence for role identity and availability.

Boundary remains strictly read-only: no transformation execution, no SSM
SendCommand, no Automation execution, no AWS resource/IAM mutation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

CANDIDATE = "AWS-PatchAsgInstance"
COMPARATOR = "DIRECT-AWS-SSM-RUNCOMMAND-PATCHBASELINE"
PROTOCOL = "IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_PHASE_B_ACCESSIBILITY_COMPARISON_PROTOCOL_001.md"
SCHEMA = "IT-METH-I-CLASS-II-AWS-PATCHASGINSTANCE-PHASE-B0-PERMISSIONS-AUDIT-3"
OMITTED_SENTINEL = "OMITTED_UNLESS_FROZEN"


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
    instance_id = first_nonempty(
        state.get("target_instance_identity"),
        state.get("instance_id"),
        (phase_a.get("inputs") or {}).get("instance_id") if isinstance(phase_a.get("inputs"), dict) else None,
    )
    asg = first_nonempty(
        state.get("asg_identity"),
        state.get("asg_name"),
        (phase_a.get("inputs") or {}).get("asg") if isinstance(phase_a.get("inputs"), dict) else None,
    )
    if not instance_id or not asg:
        raise ValueError("PHASE_A_TARGET_OR_ASG_MISSING")
    return str(instance_id), str(asg)


def normalize_frozen_role_arn(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text or text.upper() == OMITTED_SENTINEL:
        return None
    return text


def role_name_from_arn(arn: str | None) -> str | None:
    if not arn or ":role/" not in arn:
        return None
    return arn.split(":role/", 1)[1]


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
        raw[name] = data if data is not None else {"returncode": code, "stderr": err}
        if code != 0 or data is None:
            errors[name] = err or f"returncode={code}"
            return None
        return data

    phase_a_candidate = first_nonempty(phase_a.get("candidate_transformation"), phase_a.get("candidate"))
    frozen_params = phase_a_candidate.get("parameters", {}) if isinstance(phase_a_candidate, dict) else {}

    raw_automation_role = frozen_params.get("AutomationAssumeRole") if isinstance(frozen_params, dict) else None
    raw_lambda_role = frozen_params.get("LambdaRoleArn") if isinstance(frozen_params, dict) else None
    frozen_automation_role = normalize_frozen_role_arn(raw_automation_role)
    frozen_lambda_role = normalize_frozen_role_arn(raw_lambda_role)

    caller = probe("caller", ["sts", "get-caller-identity"])
    roles = probe("list_roles", ["iam", "list-roles"])
    account_aliases = probe("list_account_aliases", ["iam", "list-account-aliases"])

    frozen_roles = {
        "AutomationAssumeRole": {
            "arn": frozen_automation_role,
            "raw_value": raw_automation_role,
            "role_name": role_name_from_arn(frozen_automation_role),
            "status": "UNRESOLVED",
        },
        "LambdaRoleArn": {
            "arn": frozen_lambda_role,
            "raw_value": raw_lambda_role,
            "role_name": role_name_from_arn(frozen_lambda_role),
            "status": "UNRESOLVED",
        },
    }
    any_frozen_role = False
    role_resolution_errors: dict[str, str] = {}

    for label, info in frozen_roles.items():
        arn = info["arn"]
        role_name = info["role_name"]
        if not arn or not role_name:
            continue
        any_frozen_role = True
        data = probe(f"get_role:{role_name}", ["iam", "get-role", "--role-name", role_name])
        if isinstance(data, dict) and isinstance(data.get("Role"), dict):
            role = data["Role"]
            arn_match = role.get("Arn") == arn
            info["status"] = "PASS" if arn_match else "UNRESOLVED"
            info["arn_match"] = arn_match
            info["role_path"] = role.get("Path")
            info["create_date"] = role.get("CreateDate")
            if not arn_match:
                role_resolution_errors[label] = "IAM_ROLE_ARN_MISMATCH"
        else:
            info["status"] = "UNRESOLVED"
            role_resolution_errors[label] = errors.get(f"get_role:{role_name}", "GET_ROLE_UNRESOLVED")

    if any_frozen_role and all(info["status"] == "PASS" for info in frozen_roles.values() if info["arn"]):
        iam_role_status = "PASS"
        iam_role_reason = "All frozen candidate role ARNs were positively resolved by IAM GetRole with matching ARN identity."
    elif any_frozen_role:
        iam_role_status = "UNRESOLVED"
        iam_role_reason = "At least one frozen candidate role could not be positively resolved or matched; no discovery result was substituted."
    else:
        iam_role_status = "UNRESOLVED"
        iam_role_reason = "No frozen candidate role ARN is available in Phase-A evidence; the omitted-role sentinel is not an identity."

    resolved_role_policies: dict[str, Any] = {}
    for label, info in frozen_roles.items():
        role_name = info["role_name"]
        if info["status"] != "PASS" or not role_name:
            continue
        attached = probe(f"attached_policies_frozen:{role_name}", ["iam", "list-attached-role-policies", "--role-name", role_name])
        inline = probe(f"inline_policies_frozen:{role_name}", ["iam", "list-role-policies", "--role-name", role_name])
        resolved_role_policies[label] = {
            "role_name": role_name,
            "attached_policies": (attached or {}).get("AttachedPolicies", []) if isinstance(attached, dict) else None,
            "inline_policy_names": (inline or {}).get("PolicyNames", []) if isinstance(inline, dict) else None,
        }

    comparator_simulation = None
    caller_arn = caller.get("Arn") if isinstance(caller, dict) else None
    if caller_arn:
        comparator_simulation = probe(
            "simulate_comparator_sendcommand",
            ["iam", "simulate-principal-policy", "--policy-source-arn", caller_arn, "--action-names", "ssm:SendCommand"],
        )

    candidate_role_simulations: dict[str, Any] = {}
    for label, info in frozen_roles.items():
        arn = info["arn"]
        if not arn or info["status"] != "PASS":
            continue
        sim = probe(
            f"simulate_candidate_role:{label}",
            ["iam", "simulate-principal-policy", "--policy-source-arn", arn, "--action-names", "ssm:SendCommand,ssm:StartAutomationExecution,iam:PassRole"],
        )
        candidate_role_simulations[label] = sim

    operation_status = "UNRESOLVED"
    operation_reason = "Effective transformation permission remains unresolved because B0 cannot execute the candidate/comparator; simulation is informative only and may be unavailable or incomplete for service-role paths."

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
            "raw_AutomationAssumeRole": raw_automation_role,
            "raw_LambdaRoleArn": raw_lambda_role,
            "omitted_role_sentinel_treated_as_identity": False,
            "retrofit_from_discovered_roles": False,
        },
        "permissions_audit": {
            "iam_role_availability": {
                "status": iam_role_status,
                "reason": iam_role_reason,
                "frozen_roles": frozen_roles,
                "resolution_errors": role_resolution_errors,
                "resolved_role_policies": resolved_role_policies,
            },
            "operation_permission_availability": {
                "status": operation_status,
                "reason": operation_reason,
                "caller_arn": caller_arn,
                "comparator_simulation": comparator_simulation,
                "candidate_role_simulations": candidate_role_simulations,
            },
        },
        "caller_observation": caller,
        "account_observation": account_aliases,
        "role_inventory_observation": {
            "list_roles_succeeded": isinstance(roles, dict),
            "matching_role_names_seen": [
                r.get("RoleName")
                for r in (roles or {}).get("Roles", [])
                if isinstance(r, dict)
                and r.get("RoleName")
                and any(tok in r.get("RoleName", "").lower() for tok in ("patch", "ssm", "automation", "lambda", "tgcv"))
            ],
        },
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
        "artifact": {
            "sha256": None,
            "sha256_basis": "canonical JSON with artifact.sha256=null",
        },
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out = args.output_dir / "IT-METH-I_CLASS_II_AWS_PATCHASGINSTANCE_PHASE_B0_PERMISSIONS_AUDIT_RESULT_003.json"
    canonical = canonical_json(result)
    result["artifact"]["sha256"] = sha256_bytes(canonical)
    out.write_bytes(canonical_json(result))

    print(f"PERMISSIONS_AUDIT_STATUS={result['status']}")
    print(f"IAM_ROLE_AVAILABILITY={iam_role_status}")
    print(f"OPERATION_PERMISSION_AVAILABILITY={operation_status}")
    print(f"FROZEN_CANDIDATE_ROLE_ARN_PRESENT={bool(frozen_automation_role or frozen_lambda_role)}")
    print(f"RAW_ROLE_SENTINEL_PRESENT={bool(raw_automation_role == OMITTED_SENTINEL or raw_lambda_role == OMITTED_SENTINEL)}")
    print(f"FROZEN_AUTOMATION_ROLE_STATUS={frozen_roles['AutomationAssumeRole']['status']}")
    print(f"FROZEN_LAMBDA_ROLE_STATUS={frozen_roles['LambdaRoleArn']['status']}")
    print(f"CALLER_ARN_PRESENT={bool(caller_arn)}")
    print(f"COMPARATOR_SIMULATION_RESPONSE={isinstance(comparator_simulation, dict)}")
    print(f"CANDIDATE_ROLE_SIMULATION_RESPONSES={len(candidate_role_simulations)}")
    print("CANDIDATE_EXECUTION=NOT_AUTHORIZED")
    print("COMPARATOR_EXECUTION=NOT_AUTHORIZED")
    print("READ_ONLY_GUARD=PASS")
    print(f"OUTPUT={out}")
    print(f"SHA256={result['artifact']['sha256']}")
    print("SHA256_MODE=CANONICAL_CONTENT_HASH_EXCLUDING_SELF_FIELD")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
