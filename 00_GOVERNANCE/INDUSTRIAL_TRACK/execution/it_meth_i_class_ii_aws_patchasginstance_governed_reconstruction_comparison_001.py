"""IT-METH-I Class II AWS-PatchAsgInstance — governed R001/R002 comparison v0.1.

This script is a downstream comparison operation. It must NOT be used to construct
R002 or repair either reconstruction. It first verifies the canonical R002 seal,
then (and only then) loads R001 and classifies agreement.

No AWS mutations are performed. No candidate/comparator transformation is run.
No utility, superiority, causal, financial, or industrial claim is produced.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

PREDICATES = [
    "target_member_of_asg",
    "instance_in_service",
    "ssm_registered",
    "patch_group_app",
    "effective_baseline_resolved",
    "patch_state_resolved",
]

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


def canonical_json(data: dict[str, Any]) -> bytes:
    return (json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def verify_r002_seal(path: Path) -> tuple[bool, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    artifact = data.get("artifact", {})
    stored = artifact.get("sha256")
    if not stored:
        return False, "R002_ARTIFACT_SHA256_MISSING"
    check = json.loads(json.dumps(data))
    check.setdefault("artifact", {})["sha256"] = None
    calculated = hashlib.sha256(canonical_json(check)).hexdigest()
    return calculated == stored, calculated


def nested_field(data: dict[str, Any], field: str) -> Any:
    return data.get("state_vector", {}).get(field)


def classify(r1: Any, r2: Any, exact: bool = False) -> str:
    if r1 == r2:
        return "EXACT_AGREEMENT"
    if not exact and isinstance(r1, dict) and isinstance(r2, dict):
        if r1.get("identity") == r2.get("identity"):
            return "SEMANTIC_AGREEMENT"
    return "RECONSTRUCTION_DISAGREEMENT"


def compare(primary: Path, independent: Path, out: Path) -> dict[str, Any]:
    sealed, calculated = verify_r002_seal(independent)
    if not sealed:
        raise RuntimeError(f"R002_SEAL_INVALID:RECALCULATED={calculated}")

    # R001 is intentionally loaded only after R002 seal verification.
    r1 = json.loads(primary.read_text(encoding="utf-8"))
    r2 = json.loads(independent.read_text(encoding="utf-8"))

    rows: list[dict[str, Any]] = []
    for field in STATE_FIELDS:
        a = nested_field(r1, field)
        b = nested_field(r2, field)
        rows.append({"field": field, "classification": classify(a, b), "primary": a, "independent": b})

    for field in PREDICATES:
        a = r1.get("accessibility_predicates", {}).get(field)
        b = r2.get("accessibility_predicates", {}).get(field)
        rows.append({"field": f"accessibility_predicates.{field}", "classification": classify(a, b, exact=True), "primary": a, "independent": b})

    target_match = r1.get("inputs", {}).get("instance_id") == r2.get("inputs", {}).get("instance_id")
    asg_match = r1.get("inputs", {}).get("asg") == r2.get("inputs", {}).get("asg")

    material = [x for x in rows if x["classification"] == "RECONSTRUCTION_DISAGREEMENT"]
    semantic = [x for x in rows if x["classification"] == "SEMANTIC_AGREEMENT"]

    result = {
        "schema": "IT-METH-I-CLASS-II-AWS-PATCHASGINSTANCE-RECONSTRUCTION-COMPARISON-1",
        "status": "COMPARISON_CAPTURED",
        "r001": {"path": str(primary)},
        "r002": {"path": str(independent), "seal_verified": True, "canonical_recalculated_sha256": calculated},
        "target_identity_agreement": target_match,
        "asg_identity_agreement": asg_match,
        "field_results": rows,
        "summary": {
            "total_fields": len(rows),
            "exact_agreement": sum(x["classification"] == "EXACT_AGREEMENT" for x in rows),
            "semantic_agreement": len(semantic),
            "reconstruction_disagreement": len(material),
            "unresolved": sum(x["classification"] == "UNRESOLVED" for x in rows),
        },
        "independence_controls": {
            "r002_seal_verified_before_r001_load": True,
            "primary_used_to_construct_r002": False,
            "postdecision_outcomes_used": False,
        },
        "scientific_boundary": {
            "candidate_execution": "NOT_AUTHORIZED",
            "comparator_execution": "NOT_AUTHORIZED",
            "utility_scoring": "NOT_AUTHORIZED",
            "industrial_claim": "NOT_ASSESSED",
        },
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(canonical_json(result))
    result["artifact_sha256"] = hashlib.sha256(canonical_json(result)).hexdigest()
    out.write_bytes(canonical_json(result))
    return result


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--primary", type=Path, required=True)
    p.add_argument("--independent", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
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
    print(f"OUTPUT={args.output}")
    print(f"ARTIFACT_SHA256={result['artifact_sha256']}")
    print("CANDIDATE_EXECUTION=NOT_AUTHORIZED")
    print("COMPARATOR_EXECUTION=NOT_AUTHORIZED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
