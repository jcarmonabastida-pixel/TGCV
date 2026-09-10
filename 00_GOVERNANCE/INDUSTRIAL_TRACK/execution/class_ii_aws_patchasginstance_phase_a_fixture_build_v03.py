"""IT-METH-I Class II AWS-PatchAsgInstance — Phase A executor v0.3.

Repair wrapper over v0.2. The previous v0.3 wrapper was structurally wrong:
v0.2 exposes its run_aws implementation only through the v0.1 module returned
by load_base(). This version layers the CloudFormation capability repair at
that actual module boundary.

Repair added: CAPABILITY_AUTO_EXPAND for the packaged SAM template's
CloudFormation create-stack request.

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
    # v0.2's repaired baseline builder calls its module-level load_base().
    # Replace that loader with the capability-repaired v0.1 module so both
    # repairs are applied in the same Phase A execution path.
    v02.load_base = lambda: base
    return v02


def main() -> int:
    v02 = load_base_with_capability()
    return v02.main()


if __name__ == "__main__":
    raise SystemExit(main())
