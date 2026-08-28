# DR-007 — Rust observational unit

**Status:** PROPOSED NEW EXPERIMENTAL DECISION

## Decision

Use the **Rust package release** as the primary observational unit for EXT-1.1, with a package-version snapshot defining the pre-outcome state.

## Rationale

A package release is an observable, versioned unit that permits reconstruction of dependency structure and temporal evolution without defining accessibility from the outcome itself. It also provides a natural temporal boundary for pre/post transformation states.

## Non-circularity constraint

All features used to construct `S`, `C`, `B`, `T`, `T_acc` and `R` must be computable from information available no later than the release observation boundary. Future releases, future dependency adoption, downstream success, and outcome-derived variables are excluded from accessibility.

## Open implementation details

- exact package-release inclusion criteria;
- treatment of yanked/deprecated releases;
- dependency resolution policy;
- registry snapshot/date;
- handling of optional/dev/build dependencies;
- exact outcome and horizon.

These remain separate decisions and must be frozen before confirmatory analysis.

## Consequence

This decision does not claim that package release was the historical MVE unit. It is explicitly a **NEW DECISION for EXT-1.1**.
