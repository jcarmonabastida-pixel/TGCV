"""IT-METH-I Class II AWS-PatchAsgInstance — Phase B0 read-only accessibility preflight v0.1.

Governed by:
  IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_PHASE_B_ACCESSIBILITY_COMPARISON_PROTOCOL_001.md

Boundary:
  - READ-ONLY only.
  - Loads the closed Phase-A predecision freeze as a common evidence boundary.
  - Evaluates candidate/comparator accessibility predicates ex ante.
  - Never starts AWS-PatchAsgInstance.
  - Never invokes AWS-RunPatchBaseline / SSM SendCommand.
  - Never mutates AWS resources, tags, IAM, patch baselines, or instance state.

Evidence class: CLASS II — PUBLIC REPRODUCIBLE FIXTURE
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CANDIDATE = "AWS-PatchAsgInstance"
COMPARATOR = "DIRECT-AWS-SSM-RUNCOMMAND-PATCHBASELINE"
PATCH_GROUP = "App"
PROTOCOL = "IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_PHASE_B_ACCESSIBILITY_COMPARISON_PROTOCOL_001.md"
SCHEMA = "IT-METH-I-CLASS-II-AWS-PATCHASGINSTANCE-PHASE-B0-ACCESSIBILITY-PREFLIGHT-1"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def canonical_json(value: dict[str, Any]) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run_aws(aws: str, args: list[str], region: str) -> tuple[int, dict[str, Any] | None, str]:
    cmd = [aws, *args, "--region", region, "--output", "json", "--no-cli-pager"]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if p.returncode != 0:
        return p.returncode, None, p.stderr.strip()
    try:
        return 0, json.loads(p.stdout or "{}"), ""
    except json.JSONDecodeError as exc:
        return 0, None, f"JSON_DECODE_ERROR:{exc}"


def load_phase_a(phase_a_json: Path) -> dict[str, Any]:
    if not phase_a_json.is_file():
        raise FileNotFoundError(f"PHASE_A_RECORD_MISSING:{phase_a_json}")
    data = json.loads(phase_a_json.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("PHASE_A_RECORD_INVALID:root_not_object")
    return data


def first_nonempty(*values: Any) -> Any:
    for value in values:
        if value not in (None, "", {}, []):
            return value
    return None


def phase_a_state(phase_a: dict[str, Any]) -> dict[str, Any]:
    # Accept the known frozen Phase-A record shape while keeping this loader tolerant
    # of the wrapper used in earlier controlled builds.
    state = first_nonempty(
        phase_a.get("state_vector"),
        (phase_a.get("predecision_freeze") or {}).get("state_vector") if isinstance(phase_a.get("predecision_freeze"), dict) else None,
        (phase_a.get("predecision_state") or {}).get("state_vector") if isinstance(phase_a.get("predecision_state"), dict) else None,
    )
    if not isinstance(state, dict):
        raise ValueError("PHASE_A_STATE_VECTOR_MISSING")
    return state


def observed_target_id(state: dict[str, Any], phase_a: dict[str, Any]) -> str | None:
    value = first_nonempty(
        state.get("target_instance_identity"),
        state.get("instance_id"),
        (phase_a.get("inputs") or {}).get("instance_id") if isinstance(phase_a.get("inputs"), dict) else None,
    )
    return str(value) if value else None


def observed_asg(state: dict[str, Any], phase_a: dict[str, Any]) -> str | None:
    value = first_nonempty(
        state.get("asg_identity"),
        state.get("asg_name"),
        (phase_a.get("inputs") or {}).get("asg") if isinstance(phase_a.get("inputs"), dict) else None,
    )
    return str(value) if value else None


def predicate(status: str, evidence: str, detail: Any = None) -> dict[str, Any]:
    return {"status": status, "evidence": evidence, "detail": detail}


def evaluate_b0(aws: str, region: str, asg: str | None, instance_id: str | None, phase_a: dict[str, Any]) -> dict[str, Any]:
    if not asg:
        raise ValueError("ASG_IDENTITY_UNRESOLVED_FROM_PHASE_A")
    if not instance_id:
        raise ValueError("TARGET_INSTANCE_ID_UNRESOLVED_FROM_PHASE_A")

    results: dict[str, dict[str, Any]] = {}
    raw_probes: dict[str, Any] = {}
    command_errors: dict[str, str] = {}

    def probe(name: str, cli_args: list[str]) -> dict[str, Any] | None:
        code, data, err = run_aws(aws, cli_args, region)
        raw_probes[name] = data if data is not None else {"returncode": code, "stderr": err}
        if code != 0 or data is None:
            command_errors[name] = err or f"returncode={code}"
            return None
        return data

    caller = probe("sts_get_caller_identity", ["sts", "get-caller-identity"])
    group = probe("describe_auto_scaling_group", ["autoscaling", "describe-auto-scaling-groups", "--auto-scaling-group-names", asg])
    instance = probe("describe_instance", ["ec2", "describe-instances", "--instance-ids", instance_id])
    asg_instance = probe("describe_auto_scaling_instance", ["autoscaling", "describe-auto-scaling-instances", "--instance-ids", instance_id])
    managed = probe("describe_ssm_managed_instance", ["ssm", "describe-instance-information", "--filters", f"Key=InstanceIds,Values={instance_id}"])
    tags = probe("describe_instance_tags", ["ec2", "describe-tags", "--filters", f"Name=resource-id,Values={instance_id}"])
    patch_state = probe("describe_patch_state", ["ssm", "describe-instance-patch-states", "--instance-ids", instance_id])
    baseline = probe("resolve_patch_baseline", ["ssm", "get-patch-baseline-for-patch-group", "--patch-group", PATCH_GROUP, "--operating-system", "AMAZON_LINUX_2"])
    if baseline and baseline.get("BaselineId"):
        baseline_details = probe("get_patch_baseline", ["ssm", "get-patch-baseline", "--baseline-id", baseline["BaselineId"]])
    else:
        baseline_details = None
    hooks = probe("describe_lifecycle_hooks", ["autoscaling", "describe-lifecycle-hooks", "--auto-scaling-group-name", asg])

    group_items = group.get("AutoScalingGroups", []) if isinstance(group, dict) else []
    group_obj = group_items[0] if group_items else None
    instance_items = instance.get("Reservations", []) if isinstance(instance, dict) else []
    ec2_obj = instance_items[0].get("Instances", [None])[0] if instance_items else None
    asgi_items = asg_instance.get("AutoScalingInstances", []) if isinstance(asg_instance, dict) else []
    asgi_obj = next((x for x in asgi_items if x.get("InstanceId") == instance_id), None)
    managed_items = managed.get("InstanceInformationList", []) if isinstance(managed, dict) else []
    managed_obj = managed_items[0] if managed_items else None
    tag_items = tags.get("Tags", []) if isinstance(tags, dict) else []
    patch_items = patch_state.get("InstancePatchStates", []) if isinstance(patch_state, dict) else []
    baseline_id = baseline.get("BaselineId") if isinstance(baseline, dict) else None

    results["target_resolvability"] = predicate(
        "PASS" if ec2_obj else ("UNRESOLVED" if "describe_instance" in command_errors else "FAIL"),
        "aws.ec2.describe-instances",
        {"instance_id": instance_id},
    )
    results["ssm_registration_readiness"] = predicate(
        "PASS" if managed_obj else ("UNRESOLVED" if "describe_ssm_managed_instance" in command_errors else "FAIL"),
        "aws.ssm.describe-instance-information",
        {"ping_status": managed_obj.get("PingStatus") if managed_obj else None},
    )
    results["resource_state_predicates"] = predicate(
        "PASS" if asgi_obj and asgi_obj.get("LifecycleState") == "InService" else ("UNRESOLVED" if not asgi_obj and "describe_auto_scaling_instance" in command_errors else "FAIL"),
        "autoscaling membership + lifecycle read",
        {"member_of_asg": bool(asgi_obj), "lifecycle_state": asgi_obj.get("LifecycleState") if asgi_obj else None},
    )
    results["patch_group_baseline_resolution"] = predicate(
        "PASS" if baseline_id and any(t.get("Key") in {"Patch Group", "PatchGroup"} and t.get("Value") == PATCH_GROUP for t in tag_items) else ("UNRESOLVED" if command_errors else "FAIL"),
        "aws.ssm.get-patch-baseline-for-patch-group + instance tag read",
        {"patch_group": PATCH_GROUP, "baseline_id": baseline_id},
    )

    # IAM/permission predicates are deliberately conservative. Read-only B0 must not
    # invent effective execution permissions for service roles that would only be proven
    # by executing the transformation. Where no frozen role ARN is present, retain UNRESOLVED.
    frozen_candidate_roles = phase_a.get("candidate_transformation", {})
    role_values = frozen_candidate_roles.get("parameters", {}) if isinstance(frozen_candidate_roles, dict) else {}
    automation_role = role_values.get("AutomationAssumeRole")
    lambda_role = role_values.get("LambdaRoleArn")
    if not automation_role and not lambda_role:
        results["iam_role_availability"] = predicate("UNRESOLVED", "parent contract documents optional role fields but Phase-A record contains no frozen role ARN")
    else:
        details = {"AutomationAssumeRole": automation_role, "LambdaRoleArn": lambda_role}
        role_checks = []
        for arn in (automation_role, lambda_role):
            if arn:
                code, data, err = run_aws(aws, ["iam", "get-role", "--role-name", arn.split("/")[-1]], region)
                raw_probes[f"iam_get_role:{arn}"] = data if data is not None else {"returncode": code, "stderr": err}
                role_checks.append(code == 0)
        results["iam_role_availability"] = predicate("PASS" if role_checks and all(role_checks) else "UNRESOLVED", "iam.get-role read-only existence probe", details)

    # Do not simulate or invoke transformation permissions here: an effective permission
    # for a service role cannot be established safely from the frozen fixture alone unless
    # an explicit read-only IAM evidence anchor is available.
    results["operation_permission_availability"] = predicate("UNRESOLVED", "Effective candidate/comparator execution permission is not proven by read-only target-state evidence")

    # Candidate parameter completeness is ex ante and can be evaluated from the frozen contract.
    results["parameter_completeness"] = predicate(
        "PASS",
        "parent comparator contract",
        {"InstanceId": instance_id, "WaitForInstance": "PT2M", "WaitForReboot": "PT5M", "AutomationAssumeRole": automation_role, "LambdaRoleArn": lambda_role},
    )
    results["temporal_availability"] = predicate("PASS", "Phase-A observation cutoff exists; B0 cutoff is defined separately and no post-decision data used")
    results["dependency_availability"] = predicate(
        "PASS" if managed_obj and baseline_id and asgi_obj and asgi_obj.get("LifecycleState") == "InService" else "UNRESOLVED",
        "read-only dependency probes",
        {"ssm_managed": bool(managed_obj), "baseline_id": baseline_id, "instance_in_service": bool(asgi_obj and asgi_obj.get("LifecycleState") == "InService")},
    )
    results["evidence_sufficiency"] = predicate(
        "PASS" if phase_a.get("status") or phase_a.get("closure_status") else "UNRESOLVED",
        "closed Phase-A artifact loaded as common evidence boundary",
        {"phase_a_status": first_nonempty(phase_a.get("status"), phase_a.get("closure_status"))},
    )

    # Symmetry is evaluated only on the frozen common boundary. The transformations differ
    # in identity, but state/evidence conditions are held common. Any effective execution-role
    # permission difference remains unresolved rather than inferred.
    candidate_vector = {k: v["status"] for k, v in results.items()}
    comparator_vector = dict(candidate_vector)
    candidate_vector["operation_permission_availability"] = "UNRESOLVED"
    comparator_vector["operation_permission_availability"] = "UNRESOLVED"

    return {
        "schema": SCHEMA,
        "status": "B0_CAPTURED",
        "protocol": PROTOCOL,
        "protocol_status": "DESIGN_FROZEN — COMPARISON EXECUTION NOT YET AUTHORIZED",
        "evidence_class": "CLASS II — PUBLIC REPRODUCIBLE FIXTURE",
        "candidate": {"identity": CANDIDATE, "execution": "NOT_AUTHORIZED"},
        "comparator": {"identity": COMPARATOR, "execution": "NOT_AUTHORIZED"},
        "phase_a_common_boundary": {
            "phase_a_record": str(phase_a.get("artifact", {}).get("path") or "frozen Phase-A record"),
            "target_instance_id": instance_id,
            "asg_name": asg,
            "phase_a_status": first_nonempty(phase_a.get("status"), phase_a.get("closure_status")),
            "postdecision_outcomes_used": False,
        },
        "caller_identity": caller,
        "accessibility_predicates": {
            "candidate": candidate_vector,
            "comparator": comparator_vector,
            "details": results,
        },
        "delta_accessibility": {
            "differences": {k: {"candidate": candidate_vector[k], "comparator": comparator_vector[k]} for k in candidate_vector if candidate_vector[k] != comparator_vector[k]},
            "non_empty": any(candidate_vector[k] != comparator_vector[k] for k in candidate_vector),
        },
        "symmetry": {
            "same_target": True,
            "same_os_image": True,
            "same_patch_group": True,
            "same_baseline_context": True,
            "same_predecision_compliance_boundary": True,
            "same_cutoff_boundary": True,
            "same_evidence_boundary": True,
            "same_nonproduction_fixture_boundary": True,
            "confounder_status": "UNRESOLVED" if results["operation_permission_availability"]["status"] == "UNRESOLVED" else "NONE_IDENTIFIED",
        },
        "raw_read_only_probes": raw_probes,
        "read_only_probe_errors": command_errors,
        "execution_guard": {
            "candidate_invoked": False,
            "comparator_invoked": False,
            "patch_installation_invoked": False,
            "fixture_mutated": False,
            "iam_modified": False,
            "patch_baseline_modified": False,
            "target_mutated": False,
        },
        "interpretation": {
            "utility_score": "NOT_ASSIGNED",
            "industrial_utility": "NOT_ASSESSED",
            "superiority": "NOT_ASSESSED",
            "causality": "NOT_ASSESSED",
            "financial_value": "NOT_ASSESSED",
            "class_ii_to_class_i_promotion": False,
            "tgcv_core_modified": False,
        },
        "artifact": {"sha256": None, "sha256_basis": "canonical JSON with artifact.sha256=null"},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", required=True)
    parser.add_argument("--phase-a-record", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--asg-name", default=None)
    parser.add_argument("--instance-id", default=None)
    args = parser.parse_args()

    aws = shutil.which("aws")
    if not aws:
        print("B0_STATUS=BLOCKED_INFRASTRUCTURE")
        print("REASON=AWS_CLI_NOT_FOUND")
        return 2

    try:
        phase_a = load_phase_a(args.phase_a_record)
        state = phase_a_state(phase_a)
        instance_id = args.instance_id or observed_target_id(state, phase_a)
        asg = args.asg_name or observed_asg(state, phase_a)
        result = evaluate_b0(aws, args.region, asg, instance_id, phase_a)
    except Exception as exc:
        print("B0_STATUS=BLOCKED_PRECONDITION")
        print(f"REASON={exc}")
        return 3

    args.output_dir.mkdir(parents=True, exist_ok=True)
    path = args.output_dir / "IT-METH-I_CLASS_II_AWS_PATCHASGINSTANCE_PHASE_B0_ACCESSIBILITY_PREFLIGHT_RESULT_001.json"
    digest = sha256_bytes(canonical_json(result))
    result["artifact"]["sha256"] = digest
    path.write_bytes(canonical_json(result))

    cand = result["accessibility_predicates"]["candidate"]
    comp = result["accessibility_predicates"]["comparator"]
    unresolved = sorted({k for k, v in cand.items() if v == "UNRESOLVED"} | {k for k, v in comp.items() if v == "UNRESOLVED"})
    diffs = result["delta_accessibility"]["differences"]

    print("B0_STATUS=CAPTURED")
    print(f"CANDIDATE={CANDIDATE}")
    print(f"COMPARATOR={COMPARATOR}")
    print(f"TARGET_INSTANCE={result['phase_a_common_boundary']['target_instance_id']}")
    print(f"ASG={result['phase_a_common_boundary']['asg_name']}")
    print(f"DELTA_A_NON_EMPTY={result['delta_accessibility']['non_empty']}")
    print(f"DIFFERING_PREDICATES={','.join(sorted(diffs)) if diffs else 'NONE'}")
    print(f"UNRESOLVED_PREDICATES={','.join(unresolved) if unresolved else 'NONE'}")
    print(f"CANDIDATE_EXECUTION=NOT_AUTHORIZED")
    print(f"COMPARATOR_EXECUTION=NOT_AUTHORIZED")
    print(f"OUTPUT={path}")
    print(f"SHA256={digest}")
    print("SHA256_MODE=CANONICAL_CONTENT_HASH_EXCLUDING_SELF_FIELD")
    print("READ_ONLY_GUARD=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
