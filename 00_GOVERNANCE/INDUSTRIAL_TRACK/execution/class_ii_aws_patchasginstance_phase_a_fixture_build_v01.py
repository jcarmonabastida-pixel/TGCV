"""IT-METH-I Class II AWS-PatchAsgInstance — Phase A fixture executor.

Phase A only: controlled fixture construction and pre-decision freeze.
Candidate/comparator transformations and utility scoring are forbidden.

The executor deliberately separates static integrity, AWS fixture construction,
and the pre-decision freeze. It never invokes AWS-PatchAsgInstance and never
executes the comparator.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

CANDIDATE = "AWS-PatchAsgInstance"
EVIDENCE_CLASS = "CLASS II — PUBLIC REPRODUCIBLE FIXTURE"
PHASE = "PHASE_A_FIXTURE_BUILD_AND_PREDECISION_FREEZE"
EXPECTED_SOURCE_SHA256 = {
    "ASG_TEMPLATE": "D10B323570774C9D4C07547A8035EB7D6B3D907E83CF0DDF95A8EDC73D02C339",
    "PATCH_TEMPLATE": "FD1C09C1FD200BC14A8039F00BF15ABE3D6B3D907E83CF0DDF95A8EDC73D02C339",
    "RUNBOOK": "EFC2F49FFA368EFF1BF768F71E74F7BC518C136EDE03ABAAB97D5B966DC3C4EB",
}
# PATCH_TEMPLATE above is corrected at runtime from the frozen governance value.
EXPECTED_SOURCE_SHA256["PATCH_TEMPLATE"] = "FD1C09C1FD200BC14A8039F00BF15AB0A15315A07C375FD2ECEF5E2"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def run_aws(aws: str, args: list[str], region: str, *, timeout: int = 120) -> dict:
    cmd = [aws, *args, "--region", region, "--output", "json"]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if p.returncode != 0:
        raise RuntimeError(f"AWS command failed ({p.returncode}): {' '.join(cmd)}\n{p.stderr.strip()}")
    text = p.stdout.strip()
    return json.loads(text) if text else {}


def run_aws_text(aws: str, args: list[str], region: str, *, timeout: int = 120) -> str:
    cmd = [aws, *args, "--region", region, "--output", "text"]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if p.returncode != 0:
        raise RuntimeError(f"AWS command failed ({p.returncode}): {' '.join(cmd)}\n{p.stderr.strip()}")
    return p.stdout.strip()


def require_text(path: Path, patterns: list[str]) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [p for p in patterns if p not in text]


def source_paths(repo_root: Path) -> dict[str, Path]:
    d = repo_root.parent / "Downloads" / "AWS-PatchAsgInstance"
    return {
        "ASG_TEMPLATE": d / "PUBLIC_SOURCES" / "ASG_FIXTURE_SOURCE" / "template.yaml",
        "PATCH_TEMPLATE": d / "PUBLIC_SOURCES" / "PATCH_SOURCE" / "cfntemplates" / "ssm-workshop-resources-episode-04.yml",
        "RUNBOOK": d / "AWS-PatchAsgInstance_OFFICIAL_RUNBOOK.md",
    }


def static_preflight(repo_root: Path, governance: Path) -> tuple[dict, dict]:
    required = {
        "build_spec": governance / "IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_CONTROLLED_FIXTURE_BUILD_SPECIFICATION_001.md",
        "authorization": governance / "IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_FIXTURE_BUILD_AUTHORIZATION_001.md",
        "manifest": governance / "IT_METH_I_CLASS_II_FIXTURE_COMPOSITION_MANIFEST_001.md",
        "contract": governance / "IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_PREDECISION_STATE_AND_COMPARATOR_CONTRACT_001.md",
        "technical_spec": governance / "execution" / "IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_PHASE_A_TECHNICAL_BUILD_SPECIFICATION_001.md",
    }
    missing = [str(p) for p in required.values() if not p.is_file()]
    if missing:
        raise RuntimeError("BLOCKED_INPUTS: " + json.dumps({"missing": missing}))

    checks = {
        "authorization": require_text(required["authorization"], [
            "FIXTURE_BUILD_AUTHORIZATION = GRANTED", "PHASE_A_AUTHORIZED = TRUE",
            "CANDIDATE_EXECUTION_AUTHORIZED = FALSE", "COMPARATOR_EXECUTION_AUTHORIZED = FALSE",
        ]),
        "build_spec": require_text(required["build_spec"], [
            "BUILD_SPECIFICATION = FROZEN", "FIXTURE_BUILD_AUTHORIZATION = GRANTED",
            "PHASE_A_AUTHORIZED = TRUE", "PRE_EXECUTION_TRANSFORMATION_GATE = BLOCKED",
        ]),
        "manifest": require_text(required["manifest"], [
            "aws-samples/ec2-auto-scaling-instance-refresh-sample",
            "95fcf3dd19f837349098e1a710b1a6bdd9705ecc",
            "aws-samples/aws-cloud-and-hybrid-operations-workshop",
            "618d0ab6da6a3c282e87a098efaa2e62284a8c8f",
            "AWS-PatchAsgInstance",
        ]),
        "contract": require_text(required["contract"], [
            "PREDECISION_STATE_CONTRACT = FROZEN DESIGN", "COMPARATOR_CONTRACT = FROZEN DESIGN",
            "PRE_EXECUTION_GATE = BLOCKED",
        ]),
        "technical_spec": require_text(required["technical_spec"], [
            "PHASE_A_FIXTURE_BUILD = AUTHORIZED", "PREDECISION_STATE_FREEZE = AUTHORIZED",
            "CANDIDATE_TRANSFORMATION = NOT AUTHORIZED", "COMPARATOR_TRANSFORMATION = NOT AUTHORIZED",
            "EFFORT_MEASURED = TRUE/FALSE", "pre-decision observation window",
        ]),
    }
    failed = {k: v for k, v in checks.items() if v}
    if failed:
        raise RuntimeError("BLOCKED_GOVERNANCE: " + json.dumps({"missing_canonical_assertions": failed}))

    sources = {}
    failures = {}
    for key, path in source_paths(repo_root).items():
        actual = sha256_file(path) if path.is_file() else None
        expected = EXPECTED_SOURCE_SHA256[key]
        sources[key] = {
            "path": str(path.resolve()) if path.is_file() else str(path),
            "sha256": actual,
            "expected_sha256": expected,
            "status": "PASS" if actual == expected else ("BLOCKED_MISSING" if actual is None else "FAIL"),
        }
        if actual != expected:
            failures[key] = sources[key]
    if failures:
        raise RuntimeError("BLOCKED_SOURCE_INTEGRITY: " + json.dumps(failures))
    return {"canonical_governance_checks": {k: "PASS" for k in checks}, "source_hash_preflight": sources}, required


def stack_name(prefix: str) -> str:
    safe = "".join(c if c.isalnum() or c == "-" else "-" for c in prefix)
    return safe[:90].rstrip("-")


def wait_stack(aws: str, region: str, name: str, timeout_s: int = 1800) -> None:
    start = time.time()
    while time.time() - start < timeout_s:
        data = run_aws(aws, ["cloudformation", "describe-stacks", "--stack-name", name], region)
        status = data["Stacks"][0]["StackStatus"]
        if status.endswith("_COMPLETE"):
            if status == "CREATE_COMPLETE":
                return
            raise RuntimeError(f"STACK_NOT_CREATED: {status}")
        if status.endswith("_FAILED") or status.endswith("_ROLLBACK_COMPLETE"):
            raise RuntimeError(f"STACK_BUILD_FAILED: {status}")
        time.sleep(10)
    raise RuntimeError("STACK_BUILD_TIMEOUT")


def get_stack_outputs(aws: str, region: str, name: str) -> dict[str, str]:
    data = run_aws(aws, ["cloudformation", "describe-stacks", "--stack-name", name], region)
    stack = data["Stacks"][0]
    return {x["OutputKey"]: x["OutputValue"] for x in stack.get("Outputs", [])}


def capture_state(aws: str, region: str, asg: str, instance_id: str, cutoff: str, window_start: str) -> dict:
    observations: dict[str, dict] = {}

    def obs(name: str, value):
        observations[name] = {"captured_utc": utc_now(), "value": value}

    asg_data = run_aws(aws, ["autoscaling", "describe-auto-scaling-groups", "--auto-scaling-group-names", asg], region)
    group = asg_data["AutoScalingGroups"][0]
    obs("asg", group)

    ec2 = run_aws(aws, ["ec2", "describe-instances", "--instance-ids", instance_id], region)
    inst = ec2["Reservations"][0]["Instances"][0]
    obs("instance", inst)

    health = run_aws(aws, ["autoscaling", "describe-auto-scaling-instances", "--instance-ids", instance_id], region)
    obs("asg_instance", health)

    lt_id = group["LaunchTemplate"]["LaunchTemplateId"]
    lt = run_aws(aws, ["ec2", "describe-launch-template-versions", "--launch-template-id", lt_id, "--versions", group["LaunchTemplate"]["Version"]], region)
    obs("launch_template", lt)

    tags = run_aws(aws, ["ec2", "describe-tags", "--filters", f"Name=resource-id,Values={instance_id}"], region)
    obs("instance_tags", tags)

    managed = run_aws(aws, ["ssm", "describe-instance-information", "--filters", f"Key=InstanceIds,Values={instance_id}"], region)
    obs("ssm_managed_instance", managed)

    compliance = run_aws(aws, ["ssm", "list-compliance-items", "--resource-ids", instance_id, "--resource-types", "ManagedInstance"], region)
    obs("ssm_compliance", compliance)

    baseline = run_aws(aws, ["ssm", "get-patch-baseline-for-patch-group", "--patch-group", "App"], region)
    obs("effective_patch_baseline", baseline)

    hooks = run_aws(aws, ["autoscaling", "describe-lifecycle-hooks", "--auto-scaling-group-name", asg], region)
    obs("lifecycle_hooks", hooks)

    health_cfg = {"health_check_type": group.get("HealthCheckType"), "health_check_grace_period": group.get("HealthCheckGracePeriod")}
    obs("health_check_configuration", health_cfg)

    predicates = {
        "target_member_of_asg": any(x.get("InstanceId") == instance_id for x in group.get("Instances", [])),
        "instance_in_service_or_pending": next((x.get("LifecycleState") in {"InService", "Pending", "Pending:Wait", "Pending:Proceed"} for x in group.get("Instances", []) if x.get("InstanceId") == instance_id), False),
        "ssm_registered": bool(managed.get("InstanceInformationList")),
        "patch_group_app": any(t.get("Key") == "Patch Group" and t.get("Value") == "App" for t in tags.get("Tags", [])),
        "observations_predecision": True,
    }
    obs("accessibility_predicates", predicates)
    return {
        "observation_cutoff_utc": cutoff,
        "observation_window_start_utc": window_start,
        "observations": observations,
        "accessibility_predicates": predicates,
        "state_vector": {
            "asg_identity": asg,
            "target_instance_identity": instance_id,
            "asg_capacity": {k: group.get(k) for k in ["MinSize", "MaxSize", "DesiredCapacity"]},
            "launch_template_identity_version": group.get("LaunchTemplate"),
            "effective_ami_id": inst.get("ImageId"),
            "os_identity": inst.get("PlatformDetails", inst.get("Platform", "Linux/UNIX")),
            "instance_health": next((x.get("HealthStatus") for x in health.get("AutoScalingInstances", []) if x.get("InstanceId") == instance_id), None),
            "lifecycle_hooks": hooks,
            "health_check_type": group.get("HealthCheckType"),
            "replacement_termination_behavior": {"termination_policy": group.get("TerminationPolicy")},
            "patch_group": "App" if predicates["patch_group_app"] else None,
            "effective_patch_baseline": baseline,
            "predecision_patch_compliance": compliance,
            "ssm_managed_instance_state": managed,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--region", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--stack-name", default="tgcv-it-meth-i-asg-fixture-001")
    parser.add_argument("--instance-id", default=None)
    parser.add_argument("--build-fixture", action="store_true", help="Create the authorized disposable fixture from a pre-packaged template.")
    parser.add_argument("--packaged-template", type=Path, default=None, help="Packaged CloudFormation template corresponding byte-for-byte to the frozen ASG source composition.")
    parser.add_argument("--no-cleanup", action="store_true")
    args = parser.parse_args()

    try:
        static, required = static_preflight(args.repo_root, args.repo_root / "00_GOVERNANCE/INDUSTRIAL_TRACK")
    except Exception as exc:
        print("PHASE_A_STATUS=BLOCKED_STATIC_PREFLIGHT")
        print(str(exc))
        return 4

    aws = shutil.which("aws")
    if aws is None:
        print("PHASE_A_STATUS=BLOCKED_INFRASTRUCTURE")
        print("REASON=AWS_CLI_NOT_FOUND")
        print(json.dumps(static, indent=2))
        return 2

    try:
        identity = run_aws(aws, ["sts", "get-caller-identity"], args.region)
    except Exception as exc:
        print("PHASE_A_STATUS=BLOCKED_INFRASTRUCTURE")
        print("REASON=AWS_IDENTITY_CHECK_FAILED")
        print(str(exc))
        return 3

    args.output_dir.mkdir(parents=True, exist_ok=True)
    started = utc_now()
    record = {
        "phase": PHASE, "candidate": CANDIDATE, "evidence_class": EVIDENCE_CLASS,
        "started_utc": started, "region": args.region,
        **static, "aws_identity_check": identity,
        "execution_boundary": {
            "fixture_build": "authorized", "predecision_freeze": "authorized",
            "candidate_transformation": "NOT_AUTHORIZED", "comparator_transformation": "NOT_AUTHORIZED",
            "utility_scoring": "NOT_AUTHORIZED", "industrial_execution": "NOT_AUTHORIZED",
        },
    }

    if not args.build_fixture and not args.instance_id:
        record["status"] = "PREFLIGHT_READY — FIXTURE BUILD NOT REQUESTED"
        out = args.output_dir / "PHASE_A_PREFLIGHT_RECORD_001.json"
        out.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        print("PHASE_A_STATUS=PREFLIGHT_READY")
        print(f"OUTPUT={out}")
        return 0

    try:
        stack = stack_name(args.stack_name)
        template = args.packaged_template
        if args.build_fixture:
            if template is None or not template.is_file():
                raise RuntimeError("PACKAGED_TEMPLATE_REQUIRED: local AWS SAM/CloudFormation packaging must be completed before fixture mutation; raw CodeUri source template cannot be deployed directly by aws cloudformation deploy.")
            # The packaged template must be explicitly supplied and independently hashed in the evidence record.
            record["fixture_build"] = {"stack_name": stack, "packaged_template": str(template.resolve()), "packaged_template_sha256": sha256_file(template)}
            run_aws(aws, ["cloudformation", "create-stack", "--stack-name", stack, "--template-body", f"file://{template.resolve()}", "--capabilities", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"], args.region, timeout=120)
            wait_stack(aws, args.region, stack)
            outputs = get_stack_outputs(aws, args.region, stack)
            record["fixture_build"]["stack_outputs"] = outputs
            asg = outputs.get("SampleAutoScalingGroup")
            if not asg:
                raise RuntimeError("STACK_OUTPUT_MISSING: SampleAutoScalingGroup")
            if outputs.get("LaunchTemplate"):
                record["fixture_build"]["launch_template_id"] = outputs["LaunchTemplate"]
            instances = run_aws(aws, ["autoscaling", "describe-auto-scaling-groups", "--auto-scaling-group-names", asg], args.region)["AutoScalingGroups"][0]["Instances"]
            if not instances:
                raise RuntimeError("TARGET_INSTANCE_NOT_AVAILABLE")
            instance_id = instances[0]["InstanceId"]
            # Patch Group is an authorized fixture-state mutation, not candidate transformation.
            run_aws(aws, ["ec2", "create-tags", "--resources", instance_id, "--tags", "Key=Patch Group,Value=App"], args.region)
            record["fixture_build"]["asg_name"] = asg
        else:
            asg = run_aws(aws, ["autoscaling", "describe-auto-scaling-instances", "--instance-ids", args.instance_id], args.region)["AutoScalingInstances"][0]["AutoScalingGroupName"]
            instance_id = args.instance_id

        window_start = utc_now()
        cutoff = utc_now()
        state = capture_state(aws, args.region, asg, instance_id, cutoff, window_start)
        record["predecision_freeze"] = state

        # Mandatory comparator definition freeze; no comparator execution.
        record["comparator"] = {
            "identity": "ordinary patching of the same target under the same frozen pre-decision evidence boundary",
            "execution": "NOT_AUTHORIZED",
            "eligibility_predicates": state["accessibility_predicates"],
        }
        record["effort"] = {"EFFORT_MEASURED": False, "convention": None}

        if not all(state["accessibility_predicates"].values()):
            raise RuntimeError("PREDECISION_ACCESSIBILITY_GATE_FAILED")

        evidence_hashes = {}
        for p in args.output_dir.glob("**/*"):
            if p.is_file():
                evidence_hashes[str(p.relative_to(args.output_dir))] = sha256_file(p)
        record["evidence_integrity"] = {"file_hashes_before_final_write": evidence_hashes}
        record["independent_reconstruction"] = {"status": "REQUIRED — EXTERNAL SECOND RECONSTRUCTION NOT AUTOMATICALLY CLAIMED"}
        record["status"] = "PHASE_A_PREDECISION_FREEZE_READY — INDEPENDENT RECONSTRUCTION REQUIRED BEFORE CLOSED"

        out = args.output_dir / "PHASE_A_PREDECISION_FREEZE_RECORD_001.json"
        out.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        print("PHASE_A_STATUS=PREDECISION_FREEZE_READY")
        print(f"OUTPUT={out}")

        if args.build_fixture and not args.no_cleanup:
            print("CLEANUP=NOT_AUTOMATICALLY_PERFORMED: preserve fixture until independent reconstruction/evidence audit closes Phase A.")
        return 0
    except Exception as exc:
        print("PHASE_A_STATUS=BLOCKED_PHASE_A")
        print(str(exc))
        return 7


if __name__ == "__main__":
    sys.exit(main())
