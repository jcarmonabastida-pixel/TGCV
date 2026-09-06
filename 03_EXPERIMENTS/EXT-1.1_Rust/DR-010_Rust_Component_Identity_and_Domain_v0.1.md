# DR-010 — Rust component identity and domain

**Status:** PROPOSED — NEW EXPERIMENTAL DECISION

## Decision question

Define the identity of the component whose accessible transformations are to be analysed in EXT-1.1, without using outcome information and without prematurely fixing the concrete candidate universe `T`.

## Proposed decision

For EXT-1.1, the analytical component is the **Rust package identified by its canonical package name within a specific release observation**. The observational record is therefore `package@version`, as established by DR-007, while component identity is the package identity that remains invariant across its releases.

### Component identity

A component is identified by the canonical Rust package/crate name recorded in the frozen registry metadata. Version is an attribute of the observed state, not a distinct component identity.

Thus, for a package `p` and releases `v_t`, `v_{t+1}`, the observations are `p@v_t` and `p@v_{t+1}`, while the component remains `p`.

### Domain boundary

The component domain is the package-level Rust ecosystem represented by the frozen registry and its package metadata. The definition does not extend the component to an application, repository, downstream project, organisation, developer, or user population.

### Identity invariants

Component identity must be determinable solely from pre-outcome metadata available at or before the release observation boundary. It must not depend on downloads, adoption, downstream success, future releases, or any outcome variable.

### Relation to `T`

This decision defines **what entity may own or expose a transformation**; it does not yet define which transformations constitute the candidate universe `T`. That remains a separate decision.

### Relation to `T_acc`

No accessibility condition is fixed by this decision. In particular, the existence of a package component does not imply that any specific transformation is accessible.

## Identifiability test

The proposed identity passes the following preliminary identifiability requirements:

1. **Observability:** canonical package identity is present in the package metadata used to reconstruct `package@version`.
2. **Temporal reproducibility:** the identity can be reconstructed without information after the release observation boundary.
3. **Outcome independence:** identity does not require any success, adoption, or downstream-performance variable.
4. **Cross-release continuity:** the same package identity can be followed across releases while version remains a state attribute.
5. **Non-circularity:** the identity is not defined by membership in `T`, `T_acc`, `B`, `R`, or by the outcome.

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

## Status rule

This record remains **PROPOSED** until the component identity can be verified against the actual frozen Rust dataset schema and the resulting representation is shown not to require any post-outcome or future-release information.

No dataset acquisition, sampling, or confirmatory execution is authorised by this proposal.

## Provenance

This is a **NEW DECISION for EXT-1.1**. It is not asserted as historical MVE/EMP-1.1 methodology.
