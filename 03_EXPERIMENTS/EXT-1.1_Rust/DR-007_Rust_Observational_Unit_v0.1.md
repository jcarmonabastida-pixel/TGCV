# DR-007 — Rust observational unit

**Status:** ACCEPTED
**Decision class:** NEW DECISION for EXT-1.1

## Decision

Use the **Rust package release (`package@version`)** as the primary observational unit for EXT-1.1, with the package-version snapshot defining the pre-outcome state.

A package release is therefore the atomic observational record at which the pre-outcome representation is reconstructed. This decision does **not** assert that package release was the historical MVE/EMP-1.1 observational unit.

## Rationale

A package release is an observable, versioned unit that permits reconstruction of dependency structure and temporal evolution without defining accessibility from the outcome itself. It provides a reproducible temporal boundary for pre/post transformation states.

The choice also permits the experiment to distinguish the observational unit (`package@version`) from the later scientific construction of the candidate universe `T` and its accessible subset `T_acc`.

## Non-circularity constraint

All features used to construct `S`, `C`, `B`, `T`, `T_acc` and `R` must be computable from information available no later than the release observation boundary. Future releases, future dependency adoption, downstream success, and outcome-derived variables are excluded from the pre-outcome representation.

## Operational boundary

For EXT-1.1, the observational record is identified by at least:

- package identity;
- package version;
- release timestamp;
- dependency metadata available at the release observation boundary.

The exact inclusion/exclusion rules and dependency-resolution semantics are deliberately delegated to subsequent decision records and are not silently fixed by this decision.

## Deferred decisions

The following remain separate decisions:

- release inclusion/exclusion criteria;
- treatment of yanked/deprecated releases;
- package/component identity details;
- dependency resolution policy;
- registry snapshot/date;
- handling of optional/dev/build dependencies;
- exact candidate-universe instantiation;
- accessibility predicate;
- outcome and horizon.

These must be frozen before confirmatory analysis.

## Consequence

DR-007 closes the **observational-unit** question only. It does not close the definition of `T`, `T_acc`, `B`, `R`, or outcome, and it does not turn any particular version transition (including `^1.0 → ^1.1`) into the scientific baseline `B`.

## Provenance

This is a **NEW DECISION for EXT-1.1**. It is not asserted as historical MVE/EMP-1.1 methodology.
