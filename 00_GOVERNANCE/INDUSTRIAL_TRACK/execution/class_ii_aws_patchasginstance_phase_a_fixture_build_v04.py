"""IT-METH-I Class II AWS-PatchAsgInstance — Phase A executor v0.4.

Repair wrapper over v0.3.

Purpose of this repair:
- preserve v0.2 non-empty PatchFilterGroup repair;
- preserve v0.3 CAPABILITY_AUTO_EXPAND handling;
- preserve idempotent reuse of the existing Patch Group App baseline;
- remove unrelated EC2 Image Builder / SNS / Instance Refresh resources from
  the packaged public sample before CloudFormation fixture creation.

The public AWS sample is a broader Instance Refresh + Image Builder solution.
The TGCV Class II Phase A fixture only requires the reproducible ASG/VPC/EC2
state needed to freeze the predecision state for AWS-PatchAsgInstance and its
same-target comparator. Image Builder is therefore deliberately excluded from
fixture construction rather than granted additional IAM privileges.

No candidate/comparator transformation is enabled by this wrapper.
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path
from typing import Any

V03 = Path(__file__).with_name("class_ii_aws_patchasginstance_phase_a_fixture_build_v03.py")


REMOVED_LOGICAL_IDS = {
    "InstanceRefreshHandler",
    "InstanceRefreshHandlerLambdaRole",
    "SNSLambdaPermission",
}


def load_v03():
    spec = importlib.util.spec_from_file_location("tgcv_phase_a_v03", V03)
    if spec is None or spec.loader is None:
        raise RuntimeError("V03_EXECUTOR_LOAD_FAILED")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _is_removed_resource(logical_id: str) -> bool:
    return (
        logical_id.startswith("EC2ImageBuilder")
        or logical_id.startswith("ImageBuilder")
        or logical_id in REMOVED_LOGICAL_IDS
    )


def _references_removed(value: Any, removed: set[str], path: str = "") -> list[str]:
    hits: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else str(key)
            if key == "Ref" and isinstance(child, str) and child in removed:
                hits.append(f"{child_path}=Ref:{child}")
            elif key == "Fn::GetAtt" and isinstance(child, list) and child and child[0] in removed:
                hits.append(f"{child_path}=GetAtt:{child[0]}")
            else:
                hits.extend(_references_removed(child, removed, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            hits.extend(_references_removed(child, removed, f"{path}[{index}]"))
    elif isinstance(value, str):
        for logical_id in removed:
            if f"${{{logical_id}}}" in value:
                hits.append(f"{path}=Sub:{logical_id}")
    return hits


def build_pruned_template(source_template: Path, destination: Path) -> tuple[Path, list[str]]:
    try:
        import yaml
    except ImportError as exc:
        raise RuntimeError("PYTHON_YAML_REQUIRED_FOR_TEMPLATE_PRUNING") from exc

    document = yaml.safe_load(source_template.read_text(encoding="utf-8"))
    if not isinstance(document, dict) or not isinstance(document.get("Resources"), dict):
        raise RuntimeError("PACKAGED_TEMPLATE_RESOURCES_SECTION_INVALID")

    resources = document["Resources"]
    removed = {
        logical_id
        for logical_id in resources
        if _is_removed_resource(logical_id)
    }

    # Remove unrelated resources first.
    for logical_id in removed:
        resources.pop(logical_id, None)

    # Remove outputs that point exclusively at removed resources. Remaining
    # resource references are a hard failure: silent dependency changes would
    # invalidate the fixture composition.
    outputs = document.get("Outputs")
    if isinstance(outputs, dict):
        for output_id in list(outputs):
            if _references_removed(outputs[output_id], removed):
                outputs.pop(output_id)

    unresolved: list[str] = []
    for logical_id, resource in resources.items():
        unresolved.extend(
            f"Resources.{logical_id}:{hit}"
            for hit in _references_removed(resource, removed, f"Resources.{logical_id}")
        )

    if unresolved:
        raise RuntimeError(
            "PRUNED_TEMPLATE_HAS_UNRESOLVED_REMOVED_RESOURCE_REFERENCES: "
            + ";".join(unresolved)
        )

    # Retain all non-Image-Builder resources, parameters and mappings so that
    # the resulting fixture remains structurally derived from the public source.
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        yaml.safe_dump(document, sort_keys=False, default_flow_style=False),
        encoding="utf-8",
    )
    return destination, sorted(removed)


def load_base_with_pruning():
    v03 = load_v03()
    base = v03.load_base_with_capability()
    original_run_aws = base.run_aws
    generated_template: Path | None = None

    def run_aws(aws: str, args: list[str], region: str, *, timeout: int = 120) -> dict:
        nonlocal generated_template
        call_args = list(args)
        if len(call_args) >= 2 and call_args[0] == "cloudformation" and call_args[1] == "create-stack":
            if "--template-body" in call_args:
                i = call_args.index("--template-body")
                if i + 1 >= len(call_args):
                    raise RuntimeError("CREATE_STACK_TEMPLATE_BODY_ARGUMENT_MISSING")
                source = call_args[i + 1]
                if source.startswith("file://"):
                    source_template = Path(source[7:])
                else:
                    raise RuntimeError("CREATE_STACK_TEMPLATE_BODY_MUST_BE_FILE_URI")
                generated_template = source_template.with_name("phase_a_minimal_fixture_template.yaml")
                _, removed_ids = build_pruned_template(source_template, generated_template)
                call_args[i + 1] = f"file://{generated_template}"
                print("PHASE_A_TEMPLATE_PRUNED=" + str(generated_template))
                print("PHASE_A_REMOVED_UNRELATED_RESOURCES=" + ",".join(removed_ids))
        return original_run_aws(aws, call_args, region, timeout=timeout)

    base.run_aws = run_aws
    # v0.3's main resolves its executor through this hook.
    v03.load_base_with_capability = lambda: base
    v03.load_v02 = lambda: base
    return v03


def main() -> int:
    executor = load_base_with_pruning()
    return executor.main()


if __name__ == "__main__":
    raise SystemExit(main())
