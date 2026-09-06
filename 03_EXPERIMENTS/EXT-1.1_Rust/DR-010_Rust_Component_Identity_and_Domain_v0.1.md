# DR-010 — Rust component identity and domain

**Status:** ACCEPTED — NEW EXPERIMENTAL DECISION

## Decision question

Define the identity of the component whose accessible transformations are to be analysed in EXT-1.1, without using outcome information and without prematurely fixing the concrete candidate universe `T`.

## Decision

For EXT-1.1, the analytical component is the **Rust package identified by its canonical package name within a specific release observation**. The observational record is therefore `package@version`, as established by DR-007, while component identity is the package identity that remains invariant across its releases.

### Component identity

A component is identified by the canonical Rust package/crate name recorded in the frozen registry metadata. Version is an attribute of the observed state, not a distinct component identity.

Thus, for a package `p` and releases `v_t`, `v_{t+1}`, the observations are `p@v_t` and `p@v_{t+1}`, while the component remains `p`.

### Domain boundary

The component domain is the package-level Rust ecosystem represented by the frozen registry and its package metadata. The definition does not extend the component to an application, repository, downstream project, organisation, developer, or user population.

### Identity invariants

Component identity is determinable solely from pre-outcome metadata available at or before the release observation boundary. It does not depend on downloads, adoption, downstream success, future releases, or any outcome variable.

## Verification against the frozen dataset

The structural audit `AUDIT_DR-010_Component_Identity_v0.1.md`, executed against the frozen local dataset `rust_repos_2022_09_07.zip`, verified the following:

1. `source_id=3` is uniquely identified as `crates`.
2. There are 91,437 package rows and 91,437 unique package IDs; no package ID maps to conflicting name/source values and no duplicate `(source_id=3, name)` identity rows were observed.
3. There are 607,498 package-version rows and 607,498 unique version IDs; all are crate releases, all have valid package references, `(package_id, version_str)` is unique, timestamps are present, and no release timestamp precedes its package timestamp.
4. All 3,618,523 dependency rows have valid references to both package-version and package entities.
5. The observed literal `*` dependency constraint is a dataset fact only and does not modify the normative R* semantics established by DR-017.

These observations establish structural identifiability of the package component and reproducible reconstruction of `package@version` without requiring post-outcome or future-release information.

## Relation to `T`

This decision defines **what entity may own or expose a transformation**; it does not define which transformations constitute the candidate universe `T`. That remains a separate decision.

## Relation to `T_acc`

No accessibility condition is fixed by this decision. In particular, the existence of a package component does not imply that any specific transformation is accessible.

## Identifiability requirements

The decision satisfies:

1. **Observability:** canonical package identity is present in the package metadata used to reconstruct `package@version`.
2. **Temporal reproducibility:** identity can be reconstructed without information after the release observation boundary.
3. **Outcome independence:** identity does not require any success, adoption, or downstream-performance variable.
4. **Cross-release continuity:** the same package identity can be followed across releases while version remains a state attribute.
5. **Non-circularity:** identity is not defined by membership in `T`, `T_acc`, `B`, `R`, or by the outcome.

## Exclusions

This decision does not determine:

- the concrete transformation operator;
- the candidate universe `T`;
- the accessibility predicate;
- resource variables or thresholds;
- outcome or horizon;
- sampling/exclusion rules;
- baseline `B` encoding;
- `R` serialization;
- the exact registry snapshot or feature-resolution implementation parameters left open by DR-009.

## Authorization consequence

This decision closes the component-identity/domain question only. It does **not** authorize dataset sampling or confirmatory execution and does not resolve any subsequent OPEN decision.

The next scientific decision is the concrete instantiation of the candidate transformation universe `T`, which must be resolved without silently deciding accessibility, baseline, outcome, sampling, or other still-open parameters.

## Provenance

This is a **NEW DECISION for EXT-1.1**. It is not asserted as historical MVE/EMP-1.1 methodology.

## Evidence record

Audit record: `AUDIT_DR-010_Component_Identity_v0.1.md`

Audit implementation: `src/audit_rust_component_identity_v01.py`
