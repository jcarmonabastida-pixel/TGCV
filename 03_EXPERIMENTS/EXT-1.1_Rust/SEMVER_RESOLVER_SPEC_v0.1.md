# EXT-1.1 Rust — Historical semver resolver specification v0.1

## Objective

Provide a deterministic, historical-only resolver sufficient to derive the candidate accessible version set from a frozen crates.io index state.

## Inputs

- Historical index snapshot/commit.
- Package name and historical version records.
- Dependency requirement strings (`req`).
- Version metadata required by the resolver.
- Explicit cutoff timestamp.

## Excluded inputs

- Download counts.
- Current crates.io API responses.
- Versions first appearing after the cutoff.
- Future package metadata.
- Any empirical success/failure outcome.

## Resolver semantics

For each dependency edge at time t, candidate versions are restricted to versions observable in the frozen historical index state and satisfying the declared semver requirement. Yanked versions are excluded according to the declared resolution policy unless the policy explicitly models lockfile-specific exceptions; EXT-1.1 uses the default registry-resolution interpretation and records yanked status as an input feature.

The resolver must be deterministic: identical historical input and parameters produce identical candidate sets.

## T_acc construction

For a package-version state s at t, define:

`T_acc(s,t) = { candidate version configurations satisfying all declared structural accessibility constraints at t }`.

The implementation must retain the identity and provenance of each candidate transformation so that additions/removals can be audited rather than represented only as a cardinality.

## Required synthetic resolver cases

1. Exact version requirement.
2. Compatible caret requirement.
3. Upper-bounded requirement.
4. Range with no satisfying version.
5. Multiple satisfying versions.
6. Yanked satisfying version.
7. Version appearing only after cutoff.
8. Malformed/unsupported requirement: fail closed and record an error.

## Failure rule

If a requirement cannot be interpreted deterministically under the pinned semver implementation, the record is not silently coerced. It is flagged and excluded from confirmatory calculations until resolved.

## Status

Specification for implementation. No real-data result is implied by this document.
