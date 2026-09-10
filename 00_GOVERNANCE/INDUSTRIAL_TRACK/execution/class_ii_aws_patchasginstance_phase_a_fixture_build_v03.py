"""IT-METH-I Class II AWS-PatchAsgInstance — Phase A executor v0.3.

Repair wrapper over v0.2. Preserves the v0.2 non-empty PatchFilterGroup
repair, adds CAPABILITY_AUTO_EXPAND for the packaged SAM template, and makes
Patch Group App baseline registration idempotent after a prior failed Phase A
attempt has already registered a baseline.

No candidate/comparator transformation is enabled by this wrapper.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

V02 = Path(__file__).with_name("class_ii_aws_patchasginstance_phase_a_fixture_build_v02.py")


def load_v02():
    spec = importlib.util.spec_from_file_location("tgcv_phase_a_v02", V02)
    if spec is None or spec.loader is None:
        raise RuntimeError("V02_EXECUTOR_LOAD_FAILED")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_base_with_capability():
    """Load v0.1 and wrap its AWS command runner at the real module boundary."""
    v02 = load_v02()
    base = v02.load_base()
    original_run_aws = base.run_aws

    def run_aws(aws: str, args: list[str], region: str, *, timeout: int = 120) -> dict:
        call_args = list(args)
        if len(call_args) >= 2 and call_args[0] == "cloudformation" and call_args[1] == "create-stack":
            if "--capabilities" not in call_args:
                call_args.extend([
                    "--capabilities",
                    "CAPABILITY_IAM",
                    "CAPABILITY_NAMED_IAM",
                    "CAPABILITY_AUTO_EXPAND",
                ])
            else:
                i = call_args.index("--capabilities")
                j = i + 1
                while j < len(call_args) and not call_args[j].startswith("--"):
                    j += 1
                capabilities = call_args[i + 1:j]
                if "CAPABILITY_AUTO_EXPAND" not in capabilities:
                    capabilities.append("CAPABILITY_AUTO_EXPAND")
                    call_args[i + 1:j] = capabilities
        return original_run_aws(aws, call_args, region, timeout=timeout)

    base.run_aws = run_aws
    v02.load_base = lambda: base
    return v02


def make_idempotent_baseline_builder(v02):
    """Wrap v0.2 baseline creation so an existing App mapping is reused."""
    original_builder = v02.repaired_create_fixture_baseline

    def create_fixture_baseline(aws: str, region: str, name: str) -> dict:
        try:
            return original_builder(aws, region, name)
        except RuntimeError as exc:
            text = str(exc)
            if "AlreadyExistsException" not in text or "Patch Group App already has a baseline registered" not in text:
                raise
            base = v02.load_base()
            effective = base.run_aws(
                aws,
                ["ssm", "get-patch-baseline-for-patch-group", "--patch-group", base.PATCH_GROUP, "--operating-system", "AMAZON_LINUX_2"],
                region,
            )
            baseline_id = effective.get("BaselineId")
            if not baseline_id:
                raise RuntimeError("PATCH_GROUP_BASELINE_ID_MISSING_AFTER_ALREADY_EXISTS")
            details = base.run_aws(aws, ["ssm", "get-patch-baseline", "--baseline-id", baseline_id], region)
            return {
                "request": {"reuse_existing_registration": True, "patch_group": base.PATCH_GROUP, "operating_system": "AMAZON_LINUX_2"},
                "created": {"BaselineId": baseline_id, "reused": True},
                "registered": {"reused": True, "AlreadyExistsException": True},
                "effective_for_patch_group": effective,
                "details": details,
            }

    v02.repaired_create_fixture_baseline = create_fixture_baseline
    return v02


def main() -> int:
    v02 = load_base_with_capability()
    v02 = make_idempotent_baseline_builder(v02)
    return v02.main()


if __name__ == "__main__":
    raise SystemExit(main())
