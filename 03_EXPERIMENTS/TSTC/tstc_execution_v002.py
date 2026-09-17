"""TGCV WP2 TSTC bounded execution adapter v002.

This revision does not mutate the frozen Fixture 001 definitions. It adds an
explicit conformance/operationalisation layer and fails closed where the frozen
fixture does not yet provide enough executable transition information for the
required cross-domain sequence.

No real datasets, outcomes, sampling, network access, predictive metrics,
or value analysis are permitted.
"""
from __future__ import annotations

import json
from copy import deepcopy
from tstc_fixture_engine_v002 import fixtures, tacc, digest

EXECUTION_VERSION = "TSTC_EXECUTION_v002"

COUPLING_RULES = (
    {
        "source_connector": "C01",
        "source_condition": {"security": "restricted"},
        "transition": "propagate",
        "target_connector": "C03",
        "target_condition": {"permission_repo": "denied"},
    },
    {
        "source_connector": "C03",
        "source_condition": {"repo": "changed"},
        "transition": "propagate",
        "target_connector": "C05",
        "target_condition": {"mobility_requirement_A": "urgent"},
    },
)


def _fixture_by_id(items, fixture_id):
    return next(f for f in items if f.fixture_id == fixture_id)


def _transition_ids(fixture):
    return tuple(t.transformation_id for t in fixture.transformations)


def _find_transformation(fixture, transformation_id):
    for t in fixture.transformations:
        if t.transformation_id == transformation_id:
            return t
    raise AssertionError(f"unknown transformation: {transformation_id}")


def _check_declared_transition(fixture, transformation_id):
    t = _find_transformation(fixture, transformation_id)
    if not t.affected_variables:
        return {
            "status": "BLOCKED",
            "reason": "EMPTY_AFFECTED_VARIABLE_DECLARATION",
            "transformation_id": transformation_id,
        }
    return {"status": "PASS", "transformation_id": transformation_id}


def audit_operationalisation():
    fs = fixtures()
    c01 = _fixture_by_id(fs, "FX-C01")
    c03 = _fixture_by_id(fs, "FX-C03")
    c05 = _fixture_by_id(fs, "FX-C05")

    # The frozen cross-domain sequence explicitly requires a security
    # restriction followed by a C03 repository-state transition to changed.
    # We test whether the frozen transformation operators can represent it.
    checks = []

    checks.append(_check_declared_transition(c01, "c01.restrict_security"))

    c03_repo_transition = None
    for t in c03.transformations:
        if "repo" in t.transformation_id.lower() and "repo" in t.affected_variables:
            c03_repo_transition = t.transformation_id
            break

    if c03_repo_transition is None:
        checks.append({
            "status": "BLOCKED",
            "reason": "NO_DECLARED_C03_REPO_STATE_TRANSITION",
            "required_state_change": "repo: clean → changed",
        })
    else:
        checks.append(_check_declared_transition(c03, c03_repo_transition))

    # C05 coupling target is representable as context, but must not be
    # inferred as an empirical causal mechanism.
    if "mobility_requirement_A" not in c05.context:
        checks.append({
            "status": "BLOCKED",
            "reason": "MISSING_C05_TARGET_VARIABLE",
        })
    else:
        checks.append({"status": "PASS", "target": "mobility_requirement_A"})

    blocked = [c for c in checks if c.get("status") == "BLOCKED"]

    return {
        "execution_version": EXECUTION_VERSION,
        "mode": "TSTC_SYNTHETIC_EXECUTION_V002_CONFORMANCE",
        "status": "BLOCKED" if blocked else "READY_FOR_EXECUTION",
        "fixture_versions": {f.fixture_id: f.fixture_version for f in fs},
        "transformation_universes": {
            f.fixture_id: _transition_ids(f) for f in fs
        },
        "coupling_rules": COUPLING_RULES,
        "checks": checks,
        "blocked_reasons": blocked,
        "fixture_digest": digest({
            f.fixture_id: {
                "version": f.fixture_version,
                "state": f.state,
                "context": f.context,
                "U_tau": _transition_ids(f),
            }
            for f in fs
        }),
        "non_claims": [
            "No scientific validity claim",
            "No empirical causal claim",
            "No superiority claim",
            "No value claim",
        ],
    }


def run_execution():
    audit = audit_operationalisation()
    if audit["status"] != "READY_FOR_EXECUTION":
        return audit
    raise RuntimeError(
        "Execution path intentionally not enabled until the conformance audit "
        "passes all frozen trajectory and cross-domain requirements."
    )


if __name__ == "__main__":
    print(json.dumps(run_execution(), sort_keys=True, indent=2, default=list))
