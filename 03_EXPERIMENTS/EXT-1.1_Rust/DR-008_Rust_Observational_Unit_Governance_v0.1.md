# DR-008 — Rust observational-unit governance and freeze requirements

**Status:** PROPOSED NEW EXPERIMENTAL DECISION

## Decision

Adopt the Rust package release as the observational unit for EXT-1.1, subject to the following operational freeze requirements.

### Inclusion

A release is eligible only when its package identity, version, release timestamp and dependency metadata are observable in the frozen dataset snapshot.

### Exclusion

Exclude records for which the pre-outcome state cannot be reconstructed reproducibly, including releases with missing mandatory metadata needed by the frozen representation or accessibility predicate.

### Temporal boundary

The state used to construct `B`, `T`, `T_acc` and `R` must be cut off at the release observation boundary. Information published or observable only after that boundary is forbidden in the pre-outcome representation.

### Dependency policy

Dependency information must be represented according to one deterministic, versioned resolution rule. Optional/dev/build dependency treatment remains an explicit open parameter until DR-009.

## Rationale

The purpose is not to claim that package releases are the only valid Rust unit. It is to choose a reproducible unit that supports temporal reconstruction while preserving the pre-outcome constraint.

## Status of this decision

This is a NEW DECISION for EXT-1.1. It becomes binding only when the baseline freeze manifest records the accepted version and the remaining dependency-resolution choices are frozen.
