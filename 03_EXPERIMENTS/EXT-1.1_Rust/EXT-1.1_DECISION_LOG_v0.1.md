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

## DR-007 — Rust observational unit

**Status:** ACCEPTED — NEW DECISION

`package@version` (Rust package release) is the primary observational unit for EXT-1.1. The package-version snapshot defines the pre-outcome state. This closes the observational-unit question only; it does not close the definitions of `T`, `T_acc`, `B`, `R`, or outcome, and does not treat any particular version transition as the scientific baseline `B`.

The decision preserves the pre-outcome/non-circularity constraint: features entering the pre-outcome representation must be computable from information available no later than the release observation boundary. Detailed release inclusion/exclusion, component identity, dependency resolution, candidate-universe instantiation, accessibility, and outcome remain governed by subsequent decision records.

## DR-018 — Decision-numbering reconciliation for EXT-1.1

**Status:** ACCEPTED — GOVERNANCE RECONCILIATION / NEW DECISION

A review of the versioned decision files identified a bookkeeping mismatch between the historical OPEN list above and the substantive contents of the files named `DR-008` and `DR-009`. The mismatch is resolved here without deleting, renaming, or silently rewriting historical decision identities.

### Authoritative substantive mapping

- **DR-007** — observational unit: `package@version`.
- **DR-008** — observational-unit governance and freeze requirements, as defined in `DR-008_Rust_Observational_Unit_Governance_v0.1.md`.
- **DR-009** — dependency-resolution policy, as defined in `DR-009_Rust_Dependency_Resolution_Policy_v0.1.md`.

The prior OPEN labels that described DR-008 as “Rust component identity/domain” and DR-009 as “concrete T instantiation” are therefore treated as stale bookkeeping labels and are superseded by this reconciliation. The underlying scientific questions remain OPEN and are not thereby decided.

### Scope of reconciliation

This decision changes **only the governance mapping of decision identifiers to their existing versioned records**. It does not decide component identity, candidate universe `T`, accessibility, resources, outcome, sampling, `B`, or `R`.

No dataset acquisition, sampling, outcome measurement, or confirmatory execution is authorised by this reconciliation.

### Next decision identifiers

The unresolved component-identity question will receive a new decision identifier after this reconciliation, and the concrete candidate-universe `T` question will likewise receive a new decision identifier. Existing numbered records are not repurposed retroactively.

This preserves traceability and fail-closed execution while avoiding a destructive renumbering of versioned experimental artefacts.

## OPEN DECISIONS

- Component identity/domain: OPEN — new decision record to be assigned after DR-018 reconciliation.
- Candidate universe `T` instantiation: OPEN — new decision record to be assigned after component identity is resolved.
- DR-010: Rust accessibility predicate
- DR-011: resource variables/thresholds
- DR-012: outcome definition and horizon
- DR-013: sampling/exclusion rules
- DR-014: pilot N and seed
- DR-015: baseline B encoding in Rust
- DR-016: R serialization

No OPEN decision may be silently resolved in code.
