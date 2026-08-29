# DR-009 — Rust dependency-resolution policy

**Status:** PROPOSED NEW EXPERIMENTAL DECISION

## Decision

For EXT-1.1, reconstruct the dependency graph from the package manifest and the frozen registry snapshot using a deterministic resolver. Record direct declared dependencies as the primary observable relation; resolve version constraints against the frozen registry snapshot without using information first appearing after the observational cutoff.

### Dependency classes

- **Normal/runtime dependencies:** included in the primary dependency graph.
- **Optional dependencies:** represented explicitly as optional edges; they are not treated as active runtime dependencies unless the frozen package metadata declares the corresponding feature as enabled under the pre-outcome state.
- **Development dependencies:** excluded from the primary runtime transformation graph, but retained in raw provenance so that the exclusion is reproducible.
- **Build dependencies:** retained as a separate dependency class and excluded from the primary runtime graph unless the final candidate definition explicitly requires build-environment composition.

## Rationale

This separates the observable package dependency structure from environment-specific build/test configuration and prevents future registry information from entering the pre-outcome state. The policy is deterministic and auditable.

## Non-circularity

The resolver may use only package metadata and registry state available at or before the release cutoff. It must not use download counts, downstream adoption, future releases, future dependency resolution outcomes, or any post-release success measure.

## Open parameters

The exact registry snapshot mechanism, feature-resolution semantics, treatment of yanked versions, and lockfile availability remain to be specified and frozen in subsequent decision records.

## Provenance

This is a **NEW DECISION for EXT-1.1**. It is not asserted as historical MVE/EMP-1.1 methodology.
