"""IT-METH-I Class II AWS-PatchAsgInstance — governed reconstruction comparison v0.2.

Repair of comparison v0.1: R001 stores the reconstructed state under
`predecision_freeze`, while R002 stores it under `state_vector`. v0.1 therefore
compared R002 against null fields in R001 and produced false disagreements.

This version normalizes both artifact layouts to the frozen contract state before
comparison. Volatile raw observation payloads are not treated as contract-level
state values. R002 seal verification still occurs before R001 is loaded.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

STATE_FIELDS = [
    "asg_identity",
    "target_instance_identity",
    "asg_capacity",
    "launch_template_identity_version",
    "effective_ami_id",
    "os_identity",
    "instance_health",
    "lifecycle_hooks",
    "health_check_type",
    "replacement_termination_behavior",
    "patch_group",
    "effective_patch_baseline",
    "predecision_patch_compliance",
    "ssm_managed_instance_state",
    "eligibility_predicates",
]
PREDICATES = [
    "target_member_of_asg",
    "instance_in_service",
    "ssm_registered",
    "patch_group_app",
    "effective_baseline_resolved",
    "patch_state_resolved",
]


def canonical_json(data: dict[str, Any]) -> bytes:
    return (json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def verify_r002_seal(path: Path) -> tuple[bool, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    stored = data.get("artifact", {}).get("sha256")
    if not stored:
        return False, "R002_ARTIFACT_SHA256_MISSING"
    check = json.loads(json.dumps(data))
    check.setdefault("artifact", {})["sha256"] = None
    calculated = hashlib.sha256(canonical_json(check)).hexdigest()
    return calculated == stored, calculated


def extract_state(doc: dict[str, Any], label: str) -> dict[str, Any]:
    if label == "R001":
        state = doc.get("predecision_freeze")
        if not isinstance(state, dict):
            raise RuntimeError("R001_PREDECISION_FREEZE_MISSING")
        return state.get("state_vector", state)
    state = doc.get("state_vector")
    if not isinstance(state, dict):
        raise RuntimeError("R002_STATE_VECTOR_MISSING")
    return state


def extract_predicates(doc: dict[str, Any], label: str, state: dict[str, Any]) -> dict[str, Any]:
    if isinstance(state.get("eligibility_predicates"), dict):
        return state["eligibility_predicates"]
    if label == "R001":
        pf = doc.get("predecision_freeze", {})
        if isinstance(pf.get("accessibility_predicates"), dict):
            return pf["accessibility_predicates"]
    if isinstance(doc.get("accessibility_predicates"), dict):
        return doc["accessibility_predicates"]
    return {}


def norm(value: Any) -> Any:
    # Contract comparison is semantic for mappings representing AWS API identity
    # or configuration objects; list order is retained because it can be material
    # in some API structures. Volatile observation timestamps/raw payloads are not
    # compared as state fields.
    if isinstance(value, dict):
        return {k: norm(v) for k, v in sorted(value.items()) if k not in {"captured_utc", "LastPingDateTime", "RegistrationDate", "ResourceDataSyncStatus", "ComplianceItemEntry"}}
    if isinstance(value, list):
        return [norm(v) for v in value]
    return value


def classify(a: Any, b: Any, exact: bool = False) -> str:
    na, nb = norm(a), norm(b)
    if na == nb:
        return "EXACT_AGREEMENT"
    if not exact and isinstance(na, dict) and isinstance(nb, dict):
        # Stable semantic identity checks for nested AWS objects.
        keys = {"Id", "BaselineId", "InstanceId", "AutoScalingGroupName", "LaunchTemplateId", "Version", "ImageId", "OperatingSystem", "PatchGroup", "PlatformName", "PlatformVersion"}
        common = {k for k in na.keys() & nb.keys() if k in keys}
        if common and all(na.get(k) == nb.get(k) for k in common):
            return "SEMANTIC_AGREEMENT"
    return "RECONSTRUCTION_DISAGREEMENT"


def compare(primary: Path, independent: Path, output: Path) -> dict[str, Any]:
    sealed, calculated = verify_r002_seal(independent)
    if not sealed:
        raise RuntimeError(f"R002_SEAL_INVALID:RECALCULATED={calculated}")

    # Deliberate ordering: do not load R001 before R002 seal verification.
    r2 = json.loads(independent.read_text(encoding="utf-8"))
    r1 = json.loads(primary.read_text(encoding="utf-8"))

    s1 = extract_state(r1, "R001")
    s2 = extract_state(r2, "R002")
    p1 = extract_predicates(r1, "R001", s1)
    p2 = extract_predicates(r2, "R002", s2)

    rows: list[dict[str, Any]] = []
    for field in STATE_FIELDS:
        a, b = s1.get(field), s2.get(field)
        rows.append({"field": field, "classification": classify(a, b), "primary": a, "independent": b})
    for field in PREDICATES:
        a, b = p1.get(field), p2.get(field)
        rows.append({"field": f"accessibility_predicates.{field}", "classification": classify(a, b, exact=True), "primary": a, "independent": b})

    target1 = s1.get("target_instance_identity")
    target2 = s2.get("target_instance_identity")
    asg1 = s1.get("asg_identity")
    asg2 = s2.get("asg_identity")

    disagreements = sum(x["classification"] == "RECONSTRUCTION_DISAGREEMENT" for x in rows)
    semantic = sum(x["classification"] == "SEMANTIC_AGREEMENT" for x in rows)
    exact = sum(x["classification"] == "EXACT_AGREEMENT" for x in rows)
    unresolved = sum(x["classification"] == "UNRESOLVED" for x in rows)

    result: dict[str, Any] = {
        "schema": "IT-METH-I-CLASS-II-AWS-PATCHASGINSTANCE-RECONSTRUCTION-COMPARISON-2",
        "status": "COMPARISON_CAPTURED",
        "r001": {"path": str(primary), "layout": "predecision_freeze.state_vector"},
        "r002": {"path": str(independent), "layout": "state_vector", "seal_verified": True, "canonical_recalculated_sha256": calculated},
        "target_identity_agreement": target1 == target2,
        "asg_identity_agreement": asg1 == asg2,
        "field_results": rows,
        "summary": {"total_fields": len(rows), "exact_agreement": exact, "semantic_agreement": semantic, "reconstruction_disagreement": disagreements, "unresolved": unresolved},
        "independence_controls": {"r002_seal_verified_before_r001_load": True, "primary_used_to_construct_r002": False, "postdecision_outcomes_used": False},
        "scientific_boundary": {"candidate_execution": "NOT_AUTHORIZED", "comparator_execution": "NOT_AUTHORIZED", "utility_scoring": "NOT_AUTHORIZED", "industrial_claim": "NOT_ASSESSED"},
        "interpretation_guard": "This artifact classifies reconstruction agreement only. It does not by itself establish reproducibility, utility, superiority, causality, financial value, or industrial benefit.",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(canonical_json(result))
    digest = hashlib.sha256(canonical_json(result)).hexdigest()
    result["artifact_sha256"] = digest
    output.write_bytes(canonical_json(result))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--independent", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = compare(args.primary, args.independent, args.output)
    except Exception as exc:
        print("COMPARISON_STATUS=BLOCKED")
        print(f"REASON={exc}")
        return 4

    s = result["summary"]
    print("COMPARISON_STATUS=CAPTURED")
    print(f"TARGET_IDENTITY_AGREEMENT={result['target_identity_agreement']}")
    print(f"ASG_IDENTITY_AGREEMENT={result['asg_identity_agreement']}")
    print(f"EXACT_AGREEMENT={s['exact_agreement']}")
    print(f"SEMANTIC_AGREEMENT={s['semantic_agreement']}")
    print(f"RECONSTRUCTION_DISAGREEMENT={s['reconstruction_disagreement']}")
    print(f"UNRESOLVED={s['unresolved']}")
    print(f"OUTPUT={args.output}")
    print(f"ARTIFACT_SHA256={result['artifact_sha256']}")
    print("CANDIDATE_EXECUTION=NOT_AUTHORIZED")
    print("COMPARATOR_EXECUTION=NOT_AUTHORIZED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
