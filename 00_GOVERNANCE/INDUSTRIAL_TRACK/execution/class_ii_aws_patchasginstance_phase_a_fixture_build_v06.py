"""IT-METH-I Class II AWS-PatchAsgInstance — Phase A executor v0.6.

Repair wrapper over v0.5.

v0.5 correctly removed unrelated Image Builder / SNS / Instance Refresh
resources, but also removed the Image Builder IAM role/profile that happened
to carry AmazonSSMManagedInstanceCore and therefore left the ASG instances
without the IAM instance profile required for SSM registration.

v0.6 fixes that fixture-construction defect without restoring Image Builder:
- preserves v0.2 non-empty PatchFilterGroup repair;
- preserves v0.3 CAPABILITY_AUTO_EXPAND handling;
- preserves v0.3 idempotent Patch Group App baseline reuse;
- preserves v0.5 removal of unrelated Image Builder / SNS / Instance Refresh
  resources;
- adds a dedicated Phase-A EC2 IAM role/profile carrying only
  AmazonSSMManagedInstanceCore;
- attaches that dedicated instance profile to SampleLaunchTemplate;
- leaves candidate/comparator transformations unauthorized.

This is a fixture repair only. It does not authorize candidate execution,
comparator execution, industrial execution, utility measurement, or any TGCV
Core change.
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

V05 = Path(__file__).with_name("class_ii_aws_patchasginstance_phase_a_fixture_build_v05.py")

REMOVED_LOGICAL_IDS = {
    "InstanceRefreshHandler",
    "InstanceRefreshHandlerLambdaRole",
    "ImageBuilderSNSTopic",
    "SNSLambdaPermission",
    "EC2ImageBuilderRecipe",
    "EC2ImageBuilderPipeline",
    "EC2ImageBuilderInfrastructureConfiguration",
    "EC2ImageBuilderDistributionConfiguration",
    "EC2ImageBuilderIAMRole",
    "EC2ImageBuilderIAMInstanceProfile",
}

PHASE_A_ROLE_ID = "PhaseAInstanceRole"
PHASE_A_PROFILE_ID = "PhaseAInstanceProfile"


def load_v05():
    spec = importlib.util.spec_from_file_location("tgcv_phase_a_v05", V05)
    if spec is None or spec.loader is None:
        raise RuntimeError("V05_EXECUTOR_LOAD_FAILED")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def patch_launch_template_and_add_ssm_identity(text: str) -> str:
    """Add a minimal SSM identity to the already-pruned fixture template.

    The source sample's Image Builder role/profile are deliberately removed by
    v0.5. v0.6 replaces only the SSM capability that Phase A actually requires
    with a dedicated, fixture-scoped role/profile. No Image Builder permission
    is retained.
    """
    if PHASE_A_ROLE_ID in text or PHASE_A_PROFILE_ID in text:
        raise RuntimeError("PHASE_A_SSM_IDENTITY_ALREADY_PRESENT")

    launch_marker = "  SampleLaunchTemplate:\n    Type: AWS::EC2::LaunchTemplate\n"
    if launch_marker not in text:
        raise RuntimeError("SAMPLE_LAUNCH_TEMPLATE_BLOCK_NOT_FOUND")

    data_marker = "    Properties:\n      LaunchTemplateData:\n        ImageId: !Ref AmazonLinux2LatestAmiId\n        InstanceType: !Ref SampleAutoScalingGroupInstanceType\n        SecurityGroupIds:\n          - !GetAtt VPC.DefaultSecurityGroup\n"
    if data_marker not in text:
        raise RuntimeError("SAMPLE_LAUNCH_TEMPLATE_DATA_SHAPE_UNEXPECTED")

    replacement = "    Properties:\n      LaunchTemplateData:\n        ImageId: !Ref AmazonLinux2LatestAmiId\n        InstanceType: !Ref SampleAutoScalingGroupInstanceType\n        IamInstanceProfile:\n          Name: !Ref PhaseAInstanceProfile\n        SecurityGroupIds:\n          - !GetAtt VPC.DefaultSecurityGroup\n"
    patched = text.replace(data_marker, replacement, 1)

    role_profile = """\n  PhaseAInstanceRole:\n    Type: AWS::IAM::Role\n    Properties:\n      AssumeRolePolicyDocument:\n        Version: \"2012-10-17\"\n        Statement:\n          - Effect: Allow\n            Principal:\n              Service:\n                - ec2.amazonaws.com\n            Action:\n              - sts:AssumeRole\n      ManagedPolicyArns:\n        - arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore\n\n  PhaseAInstanceProfile:\n    Type: AWS::IAM::InstanceProfile\n    Properties:\n      Roles:\n        - !Ref PhaseAInstanceRole\n"""

    resources_marker = "Resources:\n"
    if resources_marker not in patched:
        raise RuntimeError("RESOURCES_SECTION_MISSING")
    patched = patched.replace(resources_marker, resources_marker + role_profile, 1)
    return patched


def build_pruned_template(source_template: Path, destination: Path) -> tuple[Path, list[str]]:
    """Reuse v0.5 pruning, then restore only the SSM identity required by Phase A."""
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
            destination = source_template.with_name("phase_a_minimal_fixture_template_v06.yaml")
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
