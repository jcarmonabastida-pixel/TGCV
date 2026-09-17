"""Audit-only adapter manifest for frozen TSTC Fixture 001.

This script MUST NOT execute a TSTC trajectory and MUST NOT modify fixtures.
It classifies executable transition metadata as DERIVED,
EXPLICIT-IMPLEMENTATION, or MISSING and fails closed on MISSING semantics.
"""
from __future__ import annotations

import json
from pathlib import Path
from tstc_fixture_engine_v001 import fixtures, digest

VERSION = "TSTC_FIXTURE_001_ADAPTER_AUDIT_v001"

# Only mappings whose semantics are already explicit in Fixture 001 are listed.
# The C03 repo transition is deliberately absent: its semantics are missing.
EXPLICIT = {
    "c01.restrict_security": {
        "affected_variables": ["security"],
        "transition": "security: normal -> restricted",
        "traceability": "Fixture-001 FX-C01: restrict_security iff security=normal",
    },
    "c01.restore_security": {
        "affected_variables": ["security"],
        "transition": "security: restricted -> normal",
        "traceability": "Fixture-001 FX-C01: restore_security iff security=restricted",
    },
}


def classify(fixture, transformation_id):
    if transformation_id in EXPLICIT:
        return {
            "transformation_id": transformation_id,
            "status": "EXPLICIT-IMPLEMENTATION",
            **EXPLICIT[transformation_id],
        }

    # Fixture 001 explicitly specifies predicates but not an executable
    # transition operator for these transformations. Do not infer effects.
    if fixture.fixture_id == "FX-C03" and transformation_id in {
        "c03.query_db", "c03.inspect_repo", "c03.open_pr", "c03.complete_task"
    }:
        if transformation_id == "c03.inspect_repo":
            return {
                "transformation_id": transformation_id,
                "status": "MISSING",
                "reason": "No frozen transition semantics define repo: clean -> changed",
                "traceability": "Fixture-001 FX-C03 candidate transformation + cross-domain sequence",
            }
        return {
            "transformation_id": transformation_id,
            "status": "MISSING",
            "reason": "Frozen fixture does not specify executable transition semantics",
            "traceability": "Fixture-001 FX-C03 candidate transformation",
        }

    return {
        "transformation_id": transformation_id,
        "status": "MISSING",
        "reason": "Frozen fixture does not specify executable transition semantics",
        "traceability": f"Fixture-001 {fixture.fixture_id}",
    }


def build_manifest():
    rows = []
    for fixture in fixtures():
        for transformation in fixture.transformations:
            rows.append({
                "fixture_id": fixture.fixture_id,
                "fixture_version": fixture.fixture_version,
                "connector_id": fixture.connector_id,
                **classify(fixture, transformation.transformation_id),
            })

    return {
        "adapter_version": VERSION,
        "mode": "ADAPTER_AUDIT_ONLY",
        "fixture_versions": {f.fixture_id: f.fixture_version for f in fixtures()},
        "fixture_digest": digest({
            f.fixture_id: {
                "version": f.fixture_version,
                "state": f.state,
                "context": f.context,
                "transformations": [t.transformation_id for t in f.transformations],
            }
            for f in fixtures()
        }),
        "manifest": rows,
        "execution_performed": False,
        "trajectory_performed": False,
        "fixture_modified": False,
        "blocked": any(r["status"] == "MISSING" for r in rows),
        "non_claims": [
            "No TSTC trajectory execution",
            "No empirical causal claim",
            "No scientific validity claim",
            "No superiority claim",
            "No value claim",
        ],
    }


def main():
    result = build_manifest()
    print(json.dumps(result, sort_keys=True, indent=2))
    if result["blocked"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
