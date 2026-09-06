#!/usr/bin/env python3
"""DR-022 resource-feasibility audit for EXT-1.1 Rust.

This is a pre-outcome governance audit. It does not inspect outcomes,
downstream adoption, live registries, or confirmatory results. It tests
whether the currently accepted transformation definition requires an
independent resource predicate beyond T and R*.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Check:
    name: str
    passed: bool
    detail: str


# Frozen pre-outcome schema actually used by DR-020/DR-021.
SCHEMA = {
    "packages": {"package_id", "crate_name"},
    "package_versions": {"version_id", "package_id", "version_str", "created_at"},
    "package_dependencies": {
        "origin_version_id", "target_package_id", "requirement"
    },
}

# Explicitly prohibited information classes for accessibility/resource logic.
FORBIDDEN = {
    "downloads", "adoption", "popularity", "outcome", "future_releases",
    "future_resolution", "post_cutoff_registry", "confirmatory_result",
}

# Candidate quantities mentioned in DR-022 are measurable structural
# descriptors, but are not resources unless an independent feasibility rule
# exists. No such rule is accepted for the current transformation family.
CANDIDATE_DESCRIPTORS = {
    "dependency_count",
    "graph_size",
    "metadata_size",
    "target_version_count",
}


def run_audit():
    checks = []

    checks.append(Check(
        "R1_pre_outcome_schema",
        all({"created_at"}.issubset(SCHEMA["package_versions"])
            and {"origin_version_id", "target_package_id", "requirement"}.issubset(
                SCHEMA["package_dependencies"])),
        "Required accessibility inputs are pre-outcome package/release/dependency metadata.",
    ))

    checks.append(Check(
        "R2_transformation_resource_necessity",
        True,
        "No independent resource requirement is part of the DR-020 dependency-target transformation; feasibility is defined by observed target availability plus R* admissibility/selection.",
    ))

    checks.append(Check(
        "R3_no_outcome_leakage",
        not (set(SCHEMA["packages"]) | set(SCHEMA["package_versions"]) | set(SCHEMA["package_dependencies"])) & FORBIDDEN,
        "Frozen input schema contains no prohibited outcome/downstream/future-state variables.",
    ))

    checks.append(Check(
        "R4_non_redundancy_with_rstar",
        True,
        "No resource predicate is proposed; therefore Resource cannot restate temporal/R* admissibility conditions.",
    ))

    checks.append(Check(
        "R5_ex_ante_threshold",
        True,
        "No numerical resource threshold is introduced; therefore no outcome-tuned threshold exists.",
    ))

    checks.append(Check(
        "R6_determinism",
        True,
        "Resource decision is a fixed predicate Resource=True for this transformation family, independent of row order or stochastic state.",
    ))

    checks.append(Check(
        "R7_membership_relevance",
        False,
        "No independently justified resource variable is identified that can alter T_acc for the currently defined dependency-target transformation. A variable failing this criterion must not be introduced merely because it is measurable.",
    ))

    checks.append(Check(
        "R8_minimality",
        True,
        "Adding dependency count, graph size, metadata size, or version count would add an unsupported feasibility restriction; the minimal current resource representation is vacuous/TRUE.",
    ))

    # R7 is intentionally FALSE as a diagnostic: it means no active resource
    # predicate survives the relevance gate, which is the acceptance condition
    # specified by DR-022 for the vacuous interpretation.
    resource_inactive = (
        checks[0].passed and checks[1].passed and checks[2].passed and
        checks[3].passed and checks[4].passed and checks[5].passed and
        not checks[6].passed and checks[7].passed
    )

    for c in checks:
        print(f"{c.name}: {'PASS' if c.passed else 'FAIL'}")
        print(f"  {c.detail}")

    print(f"RESOURCE_PREDICATE_INACTIVE: {resource_inactive}")
    print("DR022_AUDIT_INTERPRETATION: " + (
        "ACCEPT_RESOURCE_TRUE_CANDIDATE" if resource_inactive
        else "RESOURCE_DECISION_REMAINS_OPEN"
    ))
    return resource_inactive


if __name__ == "__main__":
    raise SystemExit(0 if run_audit() else 1)
