"""IT-METH-I Class II AWS-PatchAsgInstance — Phase A executor v0.3.

Repair wrapper over v0.2. Preserves the v0.2 non-empty PatchFilterGroup
repair and adds the CloudFormation capability required by the packaged
AWS SAM template: CAPABILITY_AUTO_EXPAND.

No candidate/comparator transformation is enabled by this wrapper.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

BASE = Path(__file__).with_name("class_ii_aws_patchasginstance_phase_a_fixture_build_v02.py")


def load_base():
    spec = importlib.util.spec_from_file_location("tgcv_phase_a_v02", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError("BASE_EXECUTOR_LOAD_FAILED")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def repaired_run_aws(aws: str, args: list[str], region: str, *, timeout: int = 120) -> dict:
    """Preserve v0.2 behavior and add the required SAM expansion capability."""
    module = repaired_run_aws.module
    call_args = list(args)
    if len(call_args) >= 2 and call_args[0] == "cloudformation" and call_args[1] == "create-stack":
        if "--capabilities" not in call_args:
            call_args.extend(["--capabilities", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"])
        else:
            i = call_args.index("--capabilities")
            j = i + 1
            while j < len(call_args) and not call_args[j].startswith("--"):
                j += 1
            capabilities = call_args[i + 1:j]
            if "CAPABILITY_AUTO_EXPAND" not in capabilities:
                capabilities.append("CAPABILITY_AUTO_EXPAND")
                call_args[i + 1:j] = capabilities
    return module.original_run_aws(aws, call_args, region, timeout=timeout)


def main() -> int:
    module = load_base()
    repaired_run_aws.module = module
    module.original_run_aws = module.run_aws
    module.run_aws = repaired_run_aws
    return module.main()


if __name__ == "__main__":
    raise SystemExit(main())
