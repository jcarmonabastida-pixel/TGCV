"""IT-METH-I Class II AWS-PatchAsgInstance — Phase A fixture executor.

Phase A only: controlled fixture construction and pre-decision freeze.
Candidate/comparator transformations and utility scoring are forbidden.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

CANDIDATE = "AWS-PatchAsgInstance"
EVIDENCE_CLASS = "CLASS II — PUBLIC REPRODUCIBLE FIXTURE"
PHASE = "PHASE_A_FIXTURE_BUILD_AND_PREDECISION_FREEZE"
PATCH_GROUP = "App"
EXPECTED_SOURCE_SHA256 = {
    "ASG_TEMPLATE": "D10B323570774C9D4C07547A8035EB7D6B3D907E83CF0DDF95A8EDC73D02C339",
    "PATCH_TEMPLATE": "FD1C09C1FD200BC14A8039F00BF15AB3E894DE5DBA15315A07C375FD2ECEF5E2",
    "RUNBOOK": "EFC2F49FFA368EFF1BF768F71E74F7BC518C136EDE03ABAAB97D5B966DC3C4EB",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def run_aws(aws: str, args: list[str], region: str, *, timeout: int = 120) -> dict:
    cmd = [aws, *args, "--region", region, "--output", "json", "--no-cli-pager"]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if p.returncode != 0:
        raise RuntimeError(f"AWS command failed ({p.returncode}): {' '.join(cmd)}\n{p.stderr.strip()}")
    text = p.stdout.strip()
    return json.loads(text) if text else {}


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


def validate_packaging_manifest(manifest: Path, sources: dict) -> dict:
    if not manifest.is_file():
        raise RuntimeError("PACKAGING_MANIFEST_REQUIRED")
    data = json.loads(manifest.read_text(encoding="utf-8"))
    if data.get("schema") != "IT-METH-I-PACKAGING-MANIFEST-1" or data.get("status") != "FROZEN":
        raise RuntimeError("PACKAGING_MANIFEST_NOT_FROZEN")
    if data.get("source_sha256") != {k: v["sha256"] for k, v in sources.items()}:
        raise RuntimeError("PACKAGING_MANIFEST_SOURCE_HASH_MISMATCH")
    packaged = Path(data.get("packaged_template", ""))
    if not packaged.is_file():
        raise RuntimeError("PACKAGED_TEMPLATE_MISSING")
    actual = sha256_file(packaged)
    if actual != data.get("packaged_template_sha256"):
        raise RuntimeError("PACKAGED_TEMPLATE_HASH_MISMATCH")
    if not data.get("packaging_procedure_reference") or not data.get("composition_reference"):
        raise RuntimeError("PACKAGING_PROVENANCE_REFERENCE_MISSING")
    return data


def stack_name(prefix: str) -> str:
    safe = "".join(c if c.isalnum() or c == "-" else "-" for c in prefix)
    return safe[:90].rstrip("-")


def wait_stack(aws: str, region: str, name: str, timeout_s: int = 1800) -> None:
    start = time.time()
    while time.time() - start < timeout_s:
        data = run_aws(aws, ["cloudformation", "describe-stacks", "--stack-name", name], region)
        status = data["Stacks"][0]["StackStatus"]
        if status == "CREATE_COMPLETE":
            return
        if status in {"CREATE_FAILED", "ROLLBACK_FAILED", "ROLLBACK_COMPLETE"}:
            raise RuntimeError(f"STACK_BUILD_FAILED: {status}")
        time.sleep(10)
    raise RuntimeError("STACK_BUILD_TIMEOUT")


def get_stack_outputs(aws: str, region: str, name: str) -> dict[str, str]:
    data = run_aws(aws, ["cloudformation", "describe-stacks", "--stack-name", name], region)
    stack = data["Stacks"][0]
    return {x["OutputKey"]: x["OutputValue"] for x in stack.get("Outputs", [])}


def create_fixture_baseline(aws: str, region: str, name: str) -> dict:
    approval = {
        "PatchRules": [
            {"PatchFilterGroup": {"PatchFilters": [{"Key": "CLASSIFICATION", "Values": ["Security", "Bugfix"]}]}, "ApproveAfterDays": 0, "ComplianceLevel": "CRITICAL", "EnableNonSecurity": False},
            {"PatchFilterGroup": {"PatchFilters": []}, "ApproveAfterDays": 0, "ComplianceLevel": "MEDIUM", "EnableNonSecurity": True},
        ]
    }
    request = {
        "Name": name,
        "OperatingSystem": "AMAZON_LINUX_2",
        "ApprovalRules": approval,
        "ApprovedPatches": ["kernel*"],
        "ApprovedPatchesComplianceLevel": "CRITICAL",
        "ApprovedPatchesEnableNonSecurity": True,
        "Description": "TGCV IT-METH-I Class II disposable fixture baseline; composition of frozen AWS workshop semantics.",
        "Tags": [{"Key": "TGCV", "Value": "IT-METH-I"}, {"Key": "Fixture", "Value": "Class-II"}],
    }
    request_file = Path(tempfile.gettempdir()) / f"tgcv_{name}_patch_baseline.json"
    request_file.write_text(json.dumps(request), encoding="utf-8")
    try:
        created = run_aws(aws, ["ssm", "create-patch-baseline", "--cli-input-json", f"file://{request_file}"], region)
    finally:
        request_file.unlink(missing_ok=True)
    baseline_id = created.get("BaselineId")
    if not baseline_id:
        raise RuntimeError("PATCH_BASELINE_ID_MISSING")
    registered = run_aws(aws, ["ssm", "register-patch-baseline-for-patch-group", "--baseline-id", baseline_id, "--patch-group", PATCH_GROUP], region)
    effective = run_aws(aws, ["ssm", "get-patch-baseline-for-patch-group", "--patch-group", PATCH_GROUP, "--operating-system", "AMAZON_LINUX_2"], region)
    details = run_aws(aws, ["ssm", "get-patch-baseline", "--baseline-id", baseline_id], region)
    return {"request": request, "created": created, "registered": registered, "effective_for_patch_group": effective, "details": details}


def capture_state(aws: str, region: str, asg: str, instance_id: str, window_start: str) -> dict:
    observations: dict[str, dict] = {}
    def obs(name: str, value):
        observations[name] = {"captured_utc": utc_now(), "value": value}

    group = run_aws(aws, ["autoscaling", "describe-auto-scaling-groups", "--auto-scaling-group-names", asg], region)["AutoScalingGroups"][0]
    obs("asg", group)
    inst = run_aws(aws, ["ec2", "describe-instances", "--instance-ids", instance_id], region)["Reservations"][0]["Instances"][0]
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
    compliance_items = run_aws(aws, ["ssm", "list-compliance-items", "--resource-ids", instance_id, "--resource-types", "ManagedInstance"], region)
    obs("ssm_compliance_items", compliance_items)
    patch_state = run_aws(aws, ["ssm", "describe-instance-patch-states", "--instance-ids", instance_id], region)
    obs("instance_patch_state", patch_state)
    baseline = run_aws(aws, ["ssm", "get-patch-baseline-for-patch-group", "--patch-group", PATCH_GROUP, "--operating-system", "AMAZON_LINUX_2"], region)
    obs("effective_patch_baseline", baseline)
    baseline_details = run_aws(aws, ["ssm", "get-patch-baseline", "--baseline-id", baseline["BaselineId"]], region)
    obs("effective_patch_baseline_details", baseline_details)
    hooks = run_aws(aws, ["autoscaling", "describe-lifecycle-hooks", "--auto-scaling-group-name", asg], region)
    obs("lifecycle_hooks", hooks)
    termination = group.get("TerminationPolicy", [])
    obs("termination_policy", termination)
    health_cfg = {"health_check_type": group.get("HealthCheckType"), "health_check_grace_period": group.get("HealthCheckGracePeriod")}
    obs("health_check_configuration", health_cfg)
    ssm_info = managed.get("InstanceInformationList", [])
    ssm_os = ssm_info[0] if ssm_info else {}
    predicates = {
        "target_member_of_asg": any(x.get("InstanceId") == instance_id for x in group.get("Instances", [])),
        "instance_in_service": next((x.get("LifecycleState") == "InService" for x in group.get("Instances", []) if x.get("InstanceId") == instance_id), False),
        "ssm_registered": bool(ssm_info),
        "patch_group_app": any(t.get("Key") in {"Patch Group", "PatchGroup"} and t.get("Value") == PATCH_GROUP for t in tags.get("Tags", [])),
        "effective_baseline_resolved": bool(baseline.get("BaselineId")),
        "patch_state_resolved": bool(patch_state.get("InstancePatchStates")),
    }
    cutoff = utc_now()
    state = {
        "observation_window_start_utc": window_start,
        "observation_cutoff_utc": cutoff,
        "observations": observations,
        "accessibility_predicates": predicates,
        "state_vector": {
            "asg_identity": asg,
            "target_instance_identity": instance_id,
            "asg_capacity": {k: group.get(k) for k in ["MinSize", "MaxSize", "DesiredCapacity"]},
            "launch_template_identity_version": group.get("LaunchTemplate"),
            "effective_ami_id": inst.get("ImageId"),
            "os_identity": {"platform_details": inst.get("PlatformDetails"), "ssm_platform_type": ssm_os.get("PlatformType"), "ssm_platform_name": ssm_os.get("PlatformName"), "ssm_platform_version": ssm_os.get("PlatformVersion")},
            "instance_health": next((x.get("HealthStatus") for x in health.get("AutoScalingInstances", []) if x.get("InstanceId") == instance_id), None),
            "lifecycle_hooks": hooks,
            "health_check_type": group.get("HealthCheckType"),
            "replacement_termination_behavior": {"termination_policy": termination},
            "patch_group": PATCH_GROUP if predicates["patch_group_app"] else None,
            "effective_patch_baseline": {"assignment": baseline, "details": baseline_details},
            "predecision_patch_compliance": {"compliance_items": compliance_items, "patch_state": patch_state},
            "ssm_managed_instance_state": managed,
            "eligibility_predicates": predicates,
        },
    }
    for value in observations.values():
        if value["captured_utc"] > cutoff or value["captured_utc"] < window_start:
            raise RuntimeError("OBSERVATION_OUTSIDE_COMMON_WINDOW")
    if not all(predicates.values()):
        raise RuntimeError("PREDECISION_ACCESSIBILITY_GATE_FAILED")
    return state


def write_manifest(output_dir: Path, record_names: list[str]) -> dict:
    files = []
    for p in sorted(output_dir.glob("*")):
        if p.is_file() and p.name != "PHASE_A_EVIDENCE_MANIFEST_001.json":
            files.append({"path": p.name, "size": p.stat().st_size, "sha256": sha256_file(p)})
    manifest = {"schema": "IT-METH-I-PHASE-A-EVIDENCE-1", "records": record_names, "files": files}
    path = output_dir / "PHASE_A_EVIDENCE_MANIFEST_001.json"
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--region", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--stack-name", default="tgcv-it-meth-i-asg-fixture-001")
    parser.add_argument("--instance-id", default=None)
    parser.add_argument("--build-fixture", action="store_true")
    parser.add_argument("--packaging-manifest", type=Path, default=None)
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
    record = {
        "schema": "IT-METH-I-PHASE-A-EXECUTION-3",
        "phase": PHASE, "candidate": CANDIDATE, "evidence_class": EVIDENCE_CLASS,
        "region": args.region, "aws_identity_check": identity,
        "execution_boundary": {
            "fixture_build": "authorized", "predecision_freeze": "authorized",
            "candidate_transformation": "NOT_AUTHORIZED", "comparator_transformation": "NOT_AUTHORIZED",
            "utility_scoring": "NOT_AUTHORIZED", "industrial_execution": "NOT_AUTHORIZED",
        },
        "candidate": {
            "identity": CANDIDATE,
            "parameters": {"InstanceId": "FROZEN_AT_RUNTIME", "AutomationAssumeRole": "OMITTED_UNLESS_FROZEN", "LambdaRoleArn": "OMITTED_UNLESS_FROZEN", "WaitForInstance": "PT2M", "WaitForReboot": "PT5M"},
            "execution": "NOT_AUTHORIZED",
        },
        **static,
    }

    if not args.build_fixture and not args.instance_id:
        record["status"] = "PREFLIGHT_READY — FIXTURE BUILD NOT REQUESTED"
        out = args.output_dir / "PHASE_A_PREFLIGHT_RECORD_001.json"
        out.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        write_manifest(args.output_dir, [out.name])
        print("PHASE_A_STATUS=PREFLIGHT_READY")
        print(f"OUTPUT={out}")
        return 0

    stack = None
    baseline_id = None
    try:
        if args.build_fixture:
            if args.packaging_manifest is None:
                raise RuntimeError("PACKAGING_MANIFEST_REQUIRED")
            packaging = validate_packaging_manifest(args.packaging_manifest, static["source_hash_preflight"])
            template = Path(packaging["packaged_template"]).resolve()
            record["packaging"] = packaging
            baseline_name = f"tgcv-it-meth-i-al2-{int(time.time())}"
            baseline = create_fixture_baseline(aws, args.region, baseline_name)
            baseline_id = baseline["created"]["BaselineId"]
            record["patch_baseline_fixture"] = baseline
            stack = stack_name(args.stack_name)
            run_aws(aws, ["cloudformation", "create-stack", "--stack-name", stack, "--template-body", f"file://{template}", "--capabilities", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "--on-failure", "DO_NOTHING"], args.region, timeout=120)
            wait_stack(aws, args.region, stack)
            outputs = get_stack_outputs(aws, args.region, stack)
            record["fixture_build"] = {"stack_name": stack, "stack_outputs": outputs}
            asg = outputs.get("SampleAutoScalingGroup")
            if not asg:
                raise RuntimeError("STACK_OUTPUT_MISSING: SampleAutoScalingGroup")
            instances = run_aws(aws, ["autoscaling", "describe-auto-scaling-groups", "--auto-scaling-group-names", asg], args.region)["AutoScalingGroups"][0]["Instances"]
            if not instances:
                raise RuntimeError("TARGET_INSTANCE_NOT_AVAILABLE")
            instance_id = instances[0]["InstanceId"]
            run_aws(aws, ["ec2", "create-tags", "--resources", instance_id, "--tags", f"Key=Patch Group,Value={PATCH_GROUP}"], args.region)
            record["fixture_build"]["asg_name"] = asg
            record["fixture_build"]["target_instance_id"] = instance_id
        else:
            asg = run_aws(aws, ["autoscaling", "describe-auto-scaling-instances", "--instance-ids", args.instance_id], args.region)["AutoScalingInstances"][0]["AutoScalingGroupName"]
            instance_id = args.instance_id

        window_start = utc_now()
        state = capture_state(aws, args.region, asg, instance_id, window_start)
        record["predecision_freeze"] = state
        record["candidate"]["parameters"]["InstanceId"] = instance_id
        record["comparator"] = {
            "identity": "SSM-AWS-RunPatchBaseline on the same frozen target, Install operation, same baseline/group/evidence boundary",
            "procedure_reference": "AWS Systems Manager AWS-RunPatchBaseline; comparator execution explicitly not authorized in Phase A",
            "parameters": {"InstanceId": instance_id, "Operation": "Install", "WaitForReboot": "PT5M"},
            "eligibility_predicates": state["accessibility_predicates"],
            "execution": "NOT_AUTHORIZED",
        }
        record["effort"] = {"EFFORT_MEASURED": False, "convention": None}
        record["metric"] = {
            "name": "predecision_accessibility_vector_hamming_distance",
            "definition": "Hamming distance between normalized candidate/comparator accessibility predicate vectors at the common frozen cutoff; no post-decision outcomes permitted.",
            "comparison_rule": "0 = identical predicate vector; >0 = predecision accessibility distinction.",
        }
        record["independent_reconstruction"] = {"status": "REQUIRED", "package": "PHASE_A_INDEPENDENT_RECONSTRUCTION_PACKAGE_001.json", "automatic_second_reconstruction": False}
        record["status"] = "PHASE_A_PREDECISION_FREEZE_READY — INDEPENDENT RECONSTRUCTION REQUIRED BEFORE CLOSED"
        record["evidence_manifest_reference"] = {"path": "PHASE_A_EVIDENCE_MANIFEST_001.json", "status": "FROZEN_AFTER_RECORD_AND_RECONSTRUCTION_WRITE"}

        out = args.output_dir / "PHASE_A_PREDECISION_FREEZE_RECORD_001.json"
        recon = args.output_dir / "PHASE_A_INDEPENDENT_RECONSTRUCTION_PACKAGE_001.json"
        out.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        recon.write_text(json.dumps({"schema": "IT-METH-I-PHASE-A-RECON-1", "source_hash_preflight": static["source_hash_preflight"], "predecision_freeze": state, "candidate": record["candidate"], "comparator": record["comparator"], "metric": record["metric"], "effort": record["effort"]}, indent=2) + "\n", encoding="utf-8")
        write_manifest(args.output_dir, [out.name, recon.name])
        print("PHASE_A_STATUS=PREDECISION_FREEZE_READY")
        print(f"OUTPUT={out}")
        print("CLOSURE=BLOCKED_UNTIL_INDEPENDENT_RECONSTRUCTION")
        return 0
    except Exception as exc:
        failure = {"schema": "IT-METH-I-PHASE-A-FAILURE-1", "status": "BLOCKED_PHASE_A", "error": str(exc), "stack_name": stack, "baseline_id": baseline_id, "utc": utc_now(), "candidate_transformation": "NOT_AUTHORIZED", "comparator_transformation": "NOT_AUTHORIZED"}
        args.output_dir.mkdir(parents=True, exist_ok=True)
        (args.output_dir / "PHASE_A_FAILURE_RECORD_001.json").write_text(json.dumps(failure, indent=2) + "\n", encoding="utf-8")
        print("PHASE_A_STATUS=BLOCKED_PHASE_A")
        print(str(exc))
        return 7


if __name__ == "__main__":
    sys.exit(main())
