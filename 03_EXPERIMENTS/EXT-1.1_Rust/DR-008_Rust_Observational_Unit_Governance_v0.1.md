# DR-008 — Rust observational-unit governance and freeze requirements

**Status:** ACCEPTED — GOVERNANCE SUBDECISION UNDER DR-007

## Decision

Adopt the following governance requirements for the already accepted EXT-1.1 observational unit `package@version` established by DR-007.

### Inclusion

A release is eligible for the eventual experimental universe only when its package identity, version, release timestamp and required dependency metadata are observable in the frozen dataset snapshot.

### Exclusion

Exclude records for which the pre-outcome state cannot be reconstructed reproducibly, including releases with missing mandatory metadata needed by the frozen representation or accessibility predicate.

### Temporal boundary

The state used to construct `B`, `T`, `T_acc` and `R` must be cut off at the release observation boundary. Information published or observable only after that boundary is forbidden in the pre-outcome representation.

### Dependency policy

Dependency information must be represented according to one deterministic, versioned resolution rule. The detailed dependency-resolution policy is governed separately by the dependency decision record and is not silently fixed here.

## Rationale

This record operationalises the governance consequences of DR-007 without redefining the observational unit. It establishes reproducibility and temporal-boundary requirements while preserving the separation between observational-unit choice and the later construction of the candidate universe `T`.

## Scope boundary

DR-008 does **not** decide:

- Rust component identity/domain semantics;
- the concrete candidate universe `T`;
- the accessibility predicate;
- resource thresholds;
- outcome or horizon;
- sampling;
- baseline `B` encoding;
- `R` serialization.

Those questions remain governed by their respective decision records.

## Consequence

This record is accepted as a governance subdecision supporting DR-007. It does not advance scientific execution and does not authorise dataset acquisition or confirmatory analysis.

## Provenance

This record preserves its original filename and version for traceability. Its role is explicitly clarified after the DR-007 acceptance to avoid conflating observational-unit governance with the separate component-identity decision in the master Decision Log.

This is a **NEW DECISION for EXT-1.1** and is not asserted as historical MVE/EMP-1.1 methodology.
