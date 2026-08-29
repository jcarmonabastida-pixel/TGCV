# DR-010 — EXT-1.1 Rust candidate universe T

**Status:** PROPOSED NEW EXPERIMENTAL DECISION

## Decision

Define the EXT-1.1 candidate universe `T` as the set of transformation instances that can be enumerated from the pre-outcome package-release snapshot using the six recovered transformation families and the canonical candidate schema:

`τ = <id, class, target, pre, resource, eff>`.

A candidate is included only when its identity, class, target, precondition, resource requirement and effect can be determined without observing the outcome.

## Operational instantiation

For a package-release snapshot `S_t`, enumerate candidates from observable package/component state and the frozen dependency/registry metadata:

- **ACTIVATE:** activate an already observable inactive component when its activation precondition is satisfied.
- **COMPOSE:** compose two observable compatible components when the compatibility predicate is satisfied.
- **RECONFIGURE:** alter an observable configuration along a predeclared admissible configuration transition.
- **ACQUIRE:** acquire a component/version that is available through the pre-cutoff registry/metadata and satisfies the predeclared acquisition condition.
- **LEARN:** apply a predeclared learning/update operation whose prerequisites are observable before the cutoff.
- **RECOMBINE:** construct a predeclared recombination of observable components when its compatibility/resource conditions are satisfied.

These are operational families, not claims that every package release instantiates every family.

## Inclusion rule

A candidate enters `T(S_t)` iff all fields required by the schema are computable from information available at or before the observational cutoff and the candidate is syntactically well-formed under the family-specific rule.

## Exclusion rule

Exclude any candidate whose accessibility depends on:

- future releases;
- downstream success;
- post-cutoff adoption;
- outcome values;
- future dependency resolution;
- any variable derived from the eventual trajectory.

## Important limitation

The family-level semantics are recovered, but Rust-specific predicates for compatibility, activation, reconfiguration, acquisition, learning and recombination remain partially open. This record therefore defines the **construction rule**, not yet a final frozen Rust instance list.

## Freeze requirement

Before data acquisition for confirmatory analysis, each family-specific predicate and resource threshold must be assigned a versioned decision record. The resulting explicit list/hash of candidate definitions becomes the `T` freeze manifest.

## Provenance

This is a **NEW DECISION for EXT-1.1**. It is not presented as a historical MVE/EMP-1.1 implementation.
