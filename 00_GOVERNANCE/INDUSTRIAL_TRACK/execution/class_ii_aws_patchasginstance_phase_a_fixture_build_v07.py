"""IT-METH-I Class II AWS-PatchAsgInstance — Phase A executor v0.7.

Repair wrapper over v0.5 with a robust, structure-aware SSM identity patch.

v0.6 identified the correct repair concept but assumed an exact textual
LaunchTemplateData shape. The packaged template can vary after SAM/package
processing, so v0.6 could fail before CloudFormation with
SAMPLE_LAUNCH_TEMPLATE_DATA_SHAPE_UNEXPECTED.

v0.7 fixes only that implementation defect:
- reuses v0.5 stdlib-only pruning;
- preserves removal of unrelated Image Builder / SNS / Instance Refresh
  resources;
- adds a dedicated Phase-A EC2 IAM role/profile carrying only
  AmazonSSMManagedInstanceCore;
- attaches the profile to SampleLaunchTemplate by locating the structural
  SecurityGroupIds line inside that logical resource rather than matching an
  exact rendered text block;
- validates that the profile reference and role/profile resources are present;
- leaves candidate/comparator transformations unauthorized.

This is a fixture-construction repair only. It does not authorize candidate
execution, comparator execution, industrial execution, utility measurement,
or any TGCV Core change.
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

V05 = Path(__file__).with_name("class_ii_aws_patchasginstance_phase_a_fixture_build_v05.py")

PHASE_A_ROLE_ID = "PhaseAInstanceRole"
PHASE_A_PROFILE_ID = "PhaseAInstanceProfile"


def load_v05():
    spec = importlib.util.spec_from_file_location("tgcv_phase_a_v05", V05)
    if spec is None or spec.loader is None:
        raise RuntimeError("V05_EXECUTOR_LOAD_FAILED")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _logical_block_bounds(lines: list[str], logical_id: str) -> tuple[int, int]:
    logical_re = re.compile(r"^  ([A-Za-z][A-Za-z0-9]*):\s*$")
    start = None
    for i, line in enumerate(lines):
        if line.rstrip("\r\n") == f"  {logical_id}:":
            start = i
            break
    if start is None:
        raise RuntimeError(f"LOGICAL_RESOURCE_NOT_FOUND:{logical_id}")
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if logical_re.match(lines[i].rstrip("\r\n")):
            end = i
            break
    return start, end


def patch_launch_template_and_add_ssm_identity(text: str) -> str:
    """Patch the minimal fixture structurally, without assuming rendered values."""
    lines = text.splitlines(keepends=True)
    start, end = _logical_block_bounds(lines, "SampleLaunchTemplate")

    security_group_idx = None
    launch_data_seen = False
    profile_seen = False
    for i in range(start + 1, end):
        stripped = lines[i].rstrip("\r\n")
        if stripped == "      LaunchTemplateData:":
            launch_data_seen = True
        elif launch_data_seen and stripped.startswith("        IamInstanceProfile:"):
            profile_seen = True
        elif launch_data_seen and stripped == "        SecurityGroupIds:":
            security_group_idx = i
            break

    if profile_seen:
        raise RuntimeError("PHASE_A_SSM_IDENTITY_ALREADY_PRESENT")
    if not launch_data_seen:
        raise RuntimeError("SAMPLE_LAUNCH_TEMPLATE_DATA_SECTION_NOT_FOUND")
    if security_group_idx is None:
        raise RuntimeError("SAMPLE_LAUNCH_TEMPLATE_SECURITY_GROUPS_NOT_FOUND")

    lines.insert(
        security_group_idx,
        "        IamInstanceProfile:\n"
        "          Name: !Ref PhaseAInstanceProfile\n",
    )

    # Recompute insertion point after the line insertion and add the dedicated
    # role/profile at the beginning of Resources. This deliberately retains no
    # Image Builder policy.
    resources_idx = None
    for i, line in enumerate(lines):
        if line.rstrip("\r\n") == "Resources:":
            resources_idx = i
            break
    if resources_idx is None:
        raise RuntimeError("RESOURCES_SECTION_MISSING")

    role_profile = [
        "  PhaseAInstanceRole:\n",
        "    Type: AWS::IAM::Role\n",
        "    Properties:\n",
        "      AssumeRolePolicyDocument:\n",
        "        Version: \"2012-10-17\"\n",
        "        Statement:\n",
        "          - Effect: Allow\n",
        "            Principal:\n",
        "              Service:\n",
        "                - ec2.amazonaws.com\n",
        "            Action:\n",
        "              - sts:AssumeRole\n",
        "      ManagedPolicyArns:\n",
        "        - arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore\n",
        "\n",
        "  PhaseAInstanceProfile:\n",
        "    Type: AWS::IAM::InstanceProfile\n",
        "    Properties:\n",
        "      Roles:\n",
        "        - !Ref PhaseAInstanceRole\n",
        "\n",
    ]
    lines[resources_idx + 1:resources_idx + 1] = role_profile

    final_text = "".join(lines)

    # Hard assertions prevent a silent malformed repair.
    if "!Ref PhaseAInstanceProfile" not in final_text:
        raise RuntimeError("PHASE_A_SSM_PROFILE_REFERENCE_MISSING")
    if "PhaseAInstanceRole:\n    Type: AWS::IAM::Role" not in final_text:
        raise RuntimeError("PHASE_A_SSM_ROLE_MISSING")
    if "PhaseAInstanceProfile:\n    Type: AWS::IAM::InstanceProfile" not in final_text:
        raise RuntimeError("PHASE_A_SSM_PROFILE_MISSING")
    if "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore" not in final_text:
        raise RuntimeError("PHASE_A_SSM_POLICY_MISSING")
    return final_text


def build_pruned_template(source_template: Path, destination: Path) -> tuple[Path, list[str]]:
    v05 = load_v05()
    pruned_path, removed = v05.build_pruned_template(source_template, destination)
    text = pruned_path.read_text(encoding="utf-8")
    patched = patch_launch_template_and_add_ssm_identity(text)
    pruned_path.write_text(patched, encoding="utf-8")
    return pruned_path, sorted(set(removed))


def build_executor():
    v05 = load_v05()
    v03 = v05.load_v03()
    v02 = v03.load_base_with_capability()
    base = v02.load_base()
    original_run_aws = base.run_aws

    def run_aws(aws: str, args: list[str], region: str, *, timeout: int = 120) -> dict:
        call_args = list(args)
        if len(call_args) >= 2 and call_args[0] == "cloudformation" and call_args[1] == "create-stack":
            if "--template-body" not in call_args:
                raise RuntimeError("CREATE_STACK_TEMPLATE_BODY_ARGUMENT_MISSING")
            idx = call_args.index("--template-body")
            if idx + 1 >= len(call_args):
                raise RuntimeError("CREATE_STACK_TEMPLATE_BODY_ARGUMENT_MISSING")
            source = call_args[idx + 1]
            if not source.startswith("file://"):
                raise RuntimeError("CREATE_STACK_TEMPLATE_BODY_MUST_BE_FILE_URI")
            source_template = Path(source[7:])
            destination = source_template.with_name("phase_a_minimal_fixture_template_v07.yaml")
            _, removed = build_pruned_template(source_template, destination)
            call_args[idx + 1] = f"file://{destination}"
            print("PHASE_A_TEMPLATE_PRUNED=" + str(destination))
            print("PHASE_A_REMOVED_UNRELATED_RESOURCES=" + ",".join(removed))
            print("PHASE_A_SSM_IDENTITY_ADDED=PhaseAInstanceProfile")
        return original_run_aws(aws, call_args, region, timeout=timeout)

    base.run_aws = run_aws
    v02.load_base = lambda: base
    v03.load_base_with_capability = lambda: v02
    v05.load_v03 = lambda: v03
    return v05


def main() -> int:
    return build_executor().main()


if __name__ == "__main__":
    raise SystemExit(main())
