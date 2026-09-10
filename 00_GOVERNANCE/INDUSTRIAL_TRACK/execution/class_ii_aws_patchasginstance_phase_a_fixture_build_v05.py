"""IT-METH-I Class II AWS-PatchAsgInstance — Phase A executor v0.5.

Repair wrapper over v0.3. This version removes the unrelated Image Builder /
Instance Refresh resources from the packaged CloudFormation template using a
stdlib-only YAML block pruner, avoiding an undeclared PyYAML dependency.

Preserves:
- v0.2 non-empty PatchFilterGroup repair;
- v0.3 CAPABILITY_AUTO_EXPAND handling;
- v0.3 idempotent reuse of the pre-existing Patch Group App baseline.

The fixture remains limited to the ASG/VPC/EC2 state required for Phase A
predecision-state capture. Candidate and comparator transformations remain
unauthorized.
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

V03 = Path(__file__).with_name("class_ii_aws_patchasginstance_phase_a_fixture_build_v03.py")

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


def load_v03():
    spec = importlib.util.spec_from_file_location("tgcv_phase_a_v03", V03)
    if spec is None or spec.loader is None:
        raise RuntimeError("V03_EXECUTOR_LOAD_FAILED")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def prune_top_level_yaml_section(text: str, section: str) -> tuple[str, list[str]]:
    """Remove selected two-space logical-id blocks from a top-level YAML map.

    This deliberately handles only the CloudFormation structure used by the
    frozen packaged template: logical resource/output IDs are exactly two-space
    indented and their block ends at the next line with the same indentation.
    No YAML parser or semantic rewriting is performed.
    """
    lines = text.splitlines(keepends=True)
    section_re = re.compile(rf"^{re.escape(section)}:\s*$")
    logical_re = re.compile(r"^  ([A-Za-z][A-Za-z0-9]*):\s*$")
    section_start = None
    for idx, line in enumerate(lines):
        if section_re.match(line.rstrip("\r\n")):
            section_start = idx
            break
    if section_start is None:
        raise RuntimeError(f"PACKAGED_TEMPLATE_SECTION_MISSING:{section}")

    # Locate the next top-level (zero-space) section after the selected map.
    section_end = len(lines)
    for idx in range(section_start + 1, len(lines)):
        if lines[idx] and not lines[idx].startswith((" ", "\t", "\n", "\r")) and lines[idx].rstrip("\r\n").endswith(":"):
            section_end = idx
            break

    output: list[str] = lines[:section_start + 1]
    removed: list[str] = []
    i = section_start + 1
    while i < section_end:
        match = logical_re.match(lines[i].rstrip("\r\n"))
        if match and match.group(1) in REMOVED_LOGICAL_IDS:
            logical_id = match.group(1)
            removed.append(logical_id)
            i += 1
            while i < section_end:
                next_match = logical_re.match(lines[i].rstrip("\r\n"))
                if next_match:
                    break
                i += 1
            continue
        output.append(lines[i])
        i += 1

    output.extend(lines[section_end:])
    return "".join(output), removed


def build_pruned_template(source_template: Path, destination: Path) -> tuple[Path, list[str]]:
    text = source_template.read_text(encoding="utf-8")
    pruned, removed_resources = prune_top_level_yaml_section(text, "Resources")

    # Outputs referring to removed resources must also disappear. Since the
    # selected sample outputs are one logical-id block each, remove only those
    # output blocks whose bodies contain a direct Ref to a removed logical ID.
    lines = pruned.splitlines(keepends=True)
    output_start = None
    for idx, line in enumerate(lines):
        if line.rstrip("\r\n") == "Outputs:":
            output_start = idx
            break
    if output_start is None:
        raise RuntimeError("PACKAGED_TEMPLATE_SECTION_MISSING:Outputs")

    logical_re = re.compile(r"^  ([A-Za-z][A-Za-z0-9]*):\s*$")
    next_top = len(lines)
    for idx in range(output_start + 1, len(lines)):
        if lines[idx] and not lines[idx].startswith((" ", "\t", "\n", "\r")) and lines[idx].rstrip("\r\n").endswith(":"):
            next_top = idx
            break

    out: list[str] = lines[:output_start + 1]
    removed_outputs: list[str] = []
    i = output_start + 1
    while i < next_top:
        m = logical_re.match(lines[i].rstrip("\r\n"))
        if not m:
            out.append(lines[i])
            i += 1
            continue
        output_id = m.group(1)
        j = i + 1
        block = [lines[i]]
        while j < next_top and not logical_re.match(lines[j].rstrip("\r\n")):
            block.append(lines[j])
            j += 1
        block_text = "".join(block)
        if any(re.search(rf"\b{re.escape(logical_id)}\b", block_text) for logical_id in removed_resources):
            removed_outputs.append(output_id)
        else:
            out.extend(block)
        i = j
    out.extend(lines[next_top:])

    # Hard integrity check: no remaining direct Ref/GetAtt/Sub references to
    # removed logical IDs. This prevents a silent partial dependency rewrite.
    final_text = "".join(out)
    unresolved: list[str] = []
    for logical_id in removed_resources:
        if re.search(rf"\bRef:\s*{re.escape(logical_id)}\b", final_text):
            unresolved.append(f"Ref:{logical_id}")
        if re.search(rf"\b{re.escape(logical_id)}\b", final_text) and re.search(rf"\b(?:GetAtt|Sub).*{re.escape(logical_id)}\b", final_text):
            unresolved.append(f"Dependency:{logical_id}")
    if unresolved:
        raise RuntimeError("PRUNED_TEMPLATE_HAS_UNRESOLVED_REMOVED_RESOURCE_REFERENCES:" + ";".join(sorted(set(unresolved))))

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(final_text, encoding="utf-8")
    return destination, sorted(set(removed_resources + removed_outputs))


def build_executor():
    v03 = load_v03()
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
            destination = source_template.with_name("phase_a_minimal_fixture_template.yaml")
            _, removed = build_pruned_template(source_template, destination)
            call_args[idx + 1] = f"file://{destination}"
            print("PHASE_A_TEMPLATE_PRUNED=" + str(destination))
            print("PHASE_A_REMOVED_UNRELATED_RESOURCES=" + ",".join(removed))
        return original_run_aws(aws, call_args, region, timeout=timeout)

    base.run_aws = run_aws
    v02.load_base = lambda: base
    v03.load_base_with_capability = lambda: v02
    return v03


def main() -> int:
    return build_executor().main()


if __name__ == "__main__":
    raise SystemExit(main())
