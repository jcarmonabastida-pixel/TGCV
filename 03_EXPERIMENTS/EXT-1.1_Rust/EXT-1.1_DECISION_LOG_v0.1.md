# EXT-1.1 Rust — Decision Log v0.1

**Status:** ACTIVE / APPEND-ONLY GOVERNANCE RECORD

## DR-001 — Current Experimental Baseline

**Status:** ACCEPTED

The executable experiment is governed by `EXT-1.1_CURRENT_EXPERIMENTAL_BASELINE_v0.1.md`. Historical MVE records remain preserved as provenance and are not silently treated as the current executable specification.

## DR-002 — Rust as external domain

**Status:** ACCEPTED

Rust ecosystem is the selected external domain for EXT-1.1. This is an experimental domain-selection decision, not a claim that Rust was part of the historical MVE validation.

## DR-003 — No historical-code reconstruction claim

**Status:** ACCEPTED

The TR-181E implementation is a new implementation of the recoverable MVE semantics. It must not be described as recovered historical code unless a historical executable artefact is independently recovered and verified.

## DR-004 — R representation boundary

**Status:** ACCEPTED

For the current implementation candidate, R contains accessible transformation identifiers and accessible-set cardinality. Additional derived statistics are excluded unless a new decision explicitly justifies them before freeze.

## DR-005 — B/R identifiability gate

**Status:** ACCEPTED

The engine-level test has passed using synthetic states with identical B and different R. This opens, but does not close, the final-domain identifiability gate. The final test must use the frozen Rust candidate universe.

## DR-006 — Fail-closed rule

**Status:** ACCEPTED

Any unresolved executable-path parameter remains OPEN and blocks scientific execution. Missing historical information may be replaced by a new experimental decision only when necessary, explicitly labelled NEW DECISION, justified and versioned.

## DR-017 — R* SemVer normative implementation boundary

**Status:** ACCEPTED

The frozen `EXT-1.1_RESOLVER_SPEC_R_v0.2.md` is the sole normative SemVer/accessibility specification for EXT-1.1. Its supported grammar is intentionally restricted to the tested exact and caret forms defined there; unsupported forms must fail closed and must not be broadened by auxiliary code.

`rstar_v02.py` is the normative resolver implementation. `semver_reference.py` is retained only as a fixture/test helper and must implement the same restricted grammar; it must not introduce wildcard, inequality, tilde, compound, prerelease, or other unsupported semantics.

`tacc_pipeline.py` is not itself the normative R* resolver and must not be used as evidence of R* conformance unless its semantics are separately reconciled with the frozen R* selection operator. In particular, the R* definition selects the maximal eligible target per observable edge; a helper that merely returns all satisfying versions is not equivalent to R*.

No expansion of the R* grammar or substitution of an alternative SemVer semantics may occur silently. Any substantive change requires a new specification/decision before scientific execution.

## OPEN DECISIONS

- DR-007: Rust observational unit
- DR-008: Rust component identity/domain
- DR-009: concrete T instantiation
- DR-010: Rust accessibility predicate
- DR-011: resource variables/thresholds
- DR-012: outcome definition and horizon
- DR-013: sampling/exclusion rules
- DR-014: pilot N and seed
- DR-015: baseline B encoding in Rust
- DR-016: R serialization

No OPEN decision may be silently resolved in code.
