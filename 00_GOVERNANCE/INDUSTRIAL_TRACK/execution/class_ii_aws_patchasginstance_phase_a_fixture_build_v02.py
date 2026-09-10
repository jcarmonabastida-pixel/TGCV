"""IT-METH-I Class II AWS-PatchAsgInstance — Phase A executor v0.2.

Repair wrapper over the audited v0.1 executor.
Only repairs the AWS PatchBaseline request construction: every PatchRule
must contain a non-empty PatchFilterGroup. No candidate/comparator
transformation is enabled by this wrapper.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

BASE = Path(__file__).with_name("class_ii_aws_patchasginstance_phase_a_fixture_build_v01.py")


def load_base():
    spec = importlib.util.spec_from_file_location("tgcv_phase_a_v01", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError("BASE_EXECUTOR_LOAD_FAILED")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def repaired_create_fixture_baseline(aws: str, region: str, name: str) -> dict:
    """Create the same bounded AL2 fixture baseline with valid non-empty rules."""
    module = load_base()
    approval = {
        "PatchRules": [
            {
                "PatchFilterGroup": {
                    "PatchFilters": [
                        {"Key": "CLASSIFICATION", "Values": ["Security", "Bugfix"]}
                    ]
                },
                "ApproveAfterDays": 0,
                "ComplianceLevel": "CRITICAL",
                "EnableNonSecurity": False,
            },
            {
                "PatchFilterGroup": {
                    "PatchFilters": [
                        {"Key": "SEVERITY", "Values": ["Critical", "Important", "Medium", "Low"]}
                    ]
                },
                "ApproveAfterDays": 0,
                "ComplianceLevel": "MEDIUM",
                "EnableNonSecurity": True,
            },
        ]
    }
    request = {
        "Name": name,
        "OperatingSystem": "AMAZON_LINUX_2",
        "ApprovalRules": approval,
        "ApprovedPatches": ["kernel*"],
        "ApprovedPatchesComplianceLevel": "CRITICAL",
        "ApprovedPatchesEnableNonSecurity": True,
        "Description": "TGCV IT-METH-I Class II disposable fixture baseline; repaired PatchFilterGroup construction.",
        "Tags": [{"Key": "TGCV", "Value": "IT-METH-I"}, {"Key": "Fixture", "Value": "Class-II"}],
    }
    request_file = module.Path(module.tempfile.gettempdir()) / f"tgcv_{name}_patch_baseline.json"
    request_file.write_text(json.dumps(request), encoding="utf-8")
    try:
        created = module.run_aws(aws, ["ssm", "create-patch-baseline", "--cli-input-json", f"file://{request_file}"], region)
    finally:
        request_file.unlink(missing_ok=True)
    baseline_id = created.get("BaselineId")
    if not baseline_id:
        raise RuntimeError("PATCH_BASELINE_ID_MISSING")
    registered = module.run_aws(
        aws,
        ["ssm", "register-patch-baseline-for-patch-group", "--baseline-id", baseline_id, "--patch-group", module.PATCH_GROUP],
        region,
    )
    effective = module.run_aws(
        aws,
        ["ssm", "get-patch-baseline-for-patch-group", "--patch-group", module.PATCH_GROUP, "--operating-system", "AMAZON_LINUX_2"],
        region,
    )
    details = module.run_aws(aws, ["ssm", "get-patch-baseline", "--baseline-id", baseline_id], region)
    return {"request": request, "created": created, "registered": registered, "effective_for_patch_group": effective, "details": details}


def main() -> int:
    base = load_base()
    base.create_fixture_baseline = repaired_create_fixture_baseline
    return base.main()


if __name__ == "__main__":
    raise SystemExit(main())
