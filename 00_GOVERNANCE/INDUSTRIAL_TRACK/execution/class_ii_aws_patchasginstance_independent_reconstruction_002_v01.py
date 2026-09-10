"""IT-METH-I Class II AWS-PatchAsgInstance — independent reconstruction executor v0.1.

Purpose: independently reconstruct the frozen pre-decision state of the Class II
fixture without importing or reading the primary reconstruction result.

Read-only against AWS. It does not execute AWS-PatchAsgInstance, the comparator,
patch installation, utility scoring, or any production/industrial action.

The implementation intentionally does not reuse the primary executor's
capture_state() function. It independently queries the AWS control plane and
constructs the state vector and accessibility predicates from raw observations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CANDIDATE = "AWS-PatchAsgInstance"
PATCH_GROUP = "App"
EVIDENCE_CLASS = "CLASS II — PUBLIC REPRODUCIBLE FIXTURE"
STACK_DEFAULT = "tgcv-it-meth-i-asg-fixture-001"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def run_aws(aws: str, args: list[str], region: str) -> dict[str, Any]:
    cmd = [aws, *args, "--region", region, "--output", "json", "--no-cli-pager"]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if p.returncode != 0:
        raise RuntimeError(f"AWS_COMMAND_FAILED:{p.returncode}:{p.stderr.strip()}")
    return json.loads(p.stdout or "{}")


def get_stack_outputs(aws: str, region: str, stack: str) -> dict[str, str]:
    data = run_aws(aws, ["cloudformation", "describe-stacks", "--stack-name", stack], region)
    stacks = data.get("Stacks", [])
    if not stacks:
        raise RuntimeError("STACK_NOT_FOUND")
    return {x["OutputKey"]: x["OutputValue"] for x in stacks[0].get("Outputs", [])}


def reconstruct(aws: str, region: str, asg: str, instance_id: str, evidence_dir: Path) -> dict[str, Any]:
    window_start = utc_now()
    observations: dict[str, Any] = {}
    captured: dict[str, str] = {}

    def observe(name: str, value: Any) -> None:
        observations[name] = value
        captured[name] = utc_now()

    group_data = run_aws(aws, ["autoscaling", "describe-auto-scaling-groups", "--auto-scaling-group-names", asg], region)
    groups = group_data.get("AutoScalingGroups", [])
    if not groups:
        raise RuntimeError("ASG_NOT_FOUND")
    group = groups[0]
    observe("asg", group)

    ec2_data = run_aws(aws, ["ec2", "describe-instances", "--instance-ids", instance_id], region)
    reservations = ec2_data.get("Reservations", [])
    if not reservations or not reservations[0].get("Instances"):
        raise RuntimeError("INSTANCE_NOT_FOUND")
    instance = reservations[0]["Instances"][0]
    observe("instance", instance)

    asg_instance = run_aws(aws, ["autoscaling", "describe-auto-scaling-instances", "--instance-ids", instance_id], region)
    observe("asg_instance", asg_instance)

    lt = group.get("LaunchTemplate") or {}
    lt_id = lt.get("LaunchTemplateId")
    lt_version = lt.get("Version")
    if not lt_id or not lt_version:
        raise RuntimeError("LAUNCH_TEMPLATE_ID_VERSION_MISSING")
    lt_data = run_aws(aws, ["ec2", "describe-launch-template-versions", "--launch-template-id", lt_id, "--versions", str(lt_version)], region)
    observe("launch_template", lt_data)

    tags = run_aws(aws, ["ec2", "describe-tags", "--filters", f"Name=resource-id,Values={instance_id}"], region)
    observe("instance_tags", tags)

    managed = run_aws(aws, ["ssm", "describe-instance-information", "--filters", f"Key=InstanceIds,Values={instance_id}"], region)
    observe("ssm_managed_instance", managed)

    compliance = run_aws(aws, ["ssm", "list-compliance-items", "--resource-ids", instance_id, "--resource-types", "ManagedInstance"], region)
    observe("ssm_compliance_items", compliance)

    patch_state = run_aws(aws, ["ssm", "describe-instance-patch-states", "--instance-ids", instance_id], region)
    observe("instance_patch_state", patch_state)

    baseline = run_aws(aws, ["ssm", "get-patch-baseline-for-patch-group", "--patch-group", PATCH_GROUP, "--operating-system", "AMAZON_LINUX_2"], region)
    observe("effective_patch_baseline", baseline)
    baseline_id = baseline.get("BaselineId")
    baseline_details = {}
    if baseline_id:
        baseline_details = run_aws(aws, ["ssm", "get-patch-baseline", "--baseline-id", baseline_id], region)
    observe("effective_patch_baseline_details", baseline_details)

    hooks = run_aws(aws, ["autoscaling", "describe-lifecycle-hooks", "--auto-scaling-group-name", asg], region)
    observe("lifecycle_hooks", hooks)

    policy = group.get("TerminationPolicy", [])
    observe("termination_policy", policy)

    health_cfg = {"health_check_type": group.get("HealthCheckType"), "health_check_grace_period": group.get("HealthCheckGracePeriod")}
    observe("health_check_configuration", health_cfg)

    ssm_info = managed.get("InstanceInformationList", [])
    ssm_os = ssm_info[0] if ssm_info else {}
    asg_instances = group.get("Instances", [])
    tag_items = tags.get("Tags", [])
    patch_state_items = patch_state.get("InstancePatchStates", [])

    predicates = {
        "target_member_of_asg": any(x.get("InstanceId") == instance_id for x in asg_instances),
        "instance_in_service": any(x.get("InstanceId") == instance_id and x.get("LifecycleState") == "InService" for x in asg_instances),
        "ssm_registered": bool(ssm_info),
        "patch_group_app": any(x.get("Key") in {"Patch Group", "PatchGroup"} and x.get("Value") == PATCH_GROUP for x in tag_items),
        "effective_baseline_resolved": bool(baseline_id),
        "patch_state_resolved": bool(patch_state_items),
    }

    state = {
        "schema": "IT-METH-I-CLASS-II-AWS-PATCHASGINSTANCE-INDEPENDENT-RECONSTRUCTION-1",
        "status": "RECONSTRUCTION_002_CAPTURED",
        "reconstruction": "002",
        "executor": "EXECUTOR-2-CONTROLLED",
        "candidate": CANDIDATE,
        "evidence_class": EVIDENCE_CLASS,
        "observation_window_start_utc": window_start,
        "observation_cutoff_utc": utc_now(),
        "inputs": {
            "region": region,
            "asg": asg,
            "instance_id": instance_id,
            "primary_reconstruction_loaded": False,
            "primary_reconstruction_reference": None,
            "comparison_loaded": False,
        },
        "observations": observations,
        "observation_timestamps_utc": captured,
        "accessibility_predicates": predicates,
        "state_vector": {
            "asg_identity": asg,
            "target_instance_identity": instance_id,
            "asg_capacity": {k: group.get(k) for k in ["MinSize", "MaxSize", "DesiredCapacity"]},
            "launch_template_identity_version": lt,
            "effective_ami_id": instance.get("ImageId"),
            "os_identity": {
                "platform_details": instance.get("PlatformDetails"),
                "ssm_platform_type": ssm_os.get("PlatformType"),
                "ssm_platform_name": ssm_os.get("PlatformName"),
                "ssm_platform_version": ssm_os.get("PlatformVersion"),
            },
            "instance_health": next((x.get("HealthStatus") for x in asg_instance.get("AutoScalingInstances", []) if x.get("InstanceId") == instance_id), None),
            "lifecycle_hooks": hooks,
            "health_check_type": group.get("HealthCheckType"),
            "replacement_termination_behavior": {"termination_policy": policy},
            "patch_group": PATCH_GROUP if predicates["patch_group_app"] else None,
            "effective_patch_baseline": {"assignment": baseline, "details": baseline_details},
            "predecision_patch_compliance": {"compliance_items": compliance, "patch_state": patch_state},
            "ssm_managed_instance_state": managed,
            "eligibility_predicates": predicates,
        },
        "candidate_transformation": {
            "identity": CANDIDATE,
            "execution": "NOT_AUTHORIZED",
        },
        "comparator_transformation": {
            "identity": "SSM-AWS-RunPatchBaseline/Install on the same frozen target",
            "execution": "NOT_AUTHORIZED",
        },
        "independence_control": {
            "primary_reconstruction_available_to_executor_2": False,
            "primary_answers_loaded": False,
            "comparison_results_loaded": False,
            "postdecision_outcomes_used_to_define_state": False,
        },
    }

    path = evidence_dir / "IT-METH-I_CLASS_II_AWS_PATCHASGINSTANCE_INDEPENDENT_RECONSTRUCTION_002_RESULT_001.json"
    path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    state["artifact"] = {"path": str(path), "sha256": sha256_file(path), "size": path.stat().st_size}
    path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    state["artifact"]["sha256"] = sha256_file(path)
    return state


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", required=True)
    parser.add_argument("--instance-id", required=True)
    parser.add_argument("--asg-name", default=None)
    parser.add_argument("--stack-name", default=STACK_DEFAULT)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    aws = shutil.which("aws")
    if aws is None:
        print("RECONSTRUCTION_002_STATUS=BLOCKED_INFRASTRUCTURE")
        print("REASON=AWS_CLI_NOT_FOUND")
        return 2

    try:
        run_aws(aws, ["sts", "get-caller-identity"], args.region)
    except Exception as exc:
        print("RECONSTRUCTION_002_STATUS=BLOCKED_INFRASTRUCTURE")
        print(f"REASON=AWS_IDENTITY_CHECK_FAILED:{exc}")
        return 3

    args.output_dir.mkdir(parents=True, exist_ok=True)
    try:
        asg = args.asg_name
        if not asg:
            info = run_aws(aws, ["autoscaling", "describe-auto-scaling-instances", "--instance-ids", args.instance_id], args.region)
            items = info.get("AutoScalingInstances", [])
            if not items:
                raise RuntimeError("ASG_NOT_RESOLVED_FROM_INSTANCE")
            asg = items[0]["AutoScalingGroupName"]
        state = reconstruct(aws, args.region, asg, args.instance_id, args.output_dir)
    except Exception as exc:
        print("RECONSTRUCTION_002_STATUS=BLOCKED_RECONSTRUCTION")
        print(str(exc))
        return 4

    all_pass = all(state["accessibility_predicates"].values())
    print("RECONSTRUCTION_002_STATUS=CAPTURED")
    print(f"ACCESSIBILITY_PREDICATES_ALL_PASS={all_pass}")
    print(f"OUTPUT={state['artifact']['path']}")
    print(f"SHA256={state['artifact']['sha256']}")
    print("CANDIDATE_EXECUTION=NOT_AUTHORIZED")
    print("COMPARATOR_EXECUTION=NOT_AUTHORIZED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
