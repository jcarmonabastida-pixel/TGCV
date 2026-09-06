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

## DR-019 — Rust component identity and domain

**Status:** ACCEPTED — NEW EXPERIMENTAL DECISION

The analytical component for EXT-1.1 is the Rust package identified by its canonical package/crate name. The primary observational record remains `package@version` under DR-007; version is a state attribute, not a distinct component identity.

The domain boundary is the package-level Rust ecosystem represented by the frozen registry and package metadata. Identity is defined from pre-outcome metadata and does not depend on downloads, adoption, downstream success, future releases, or outcomes.

The structural audit `AUDIT_DR-010_Component_Identity_v0.1.md` verified the decision against the frozen local dataset: unique `crates` source identification; 91,437 unique package IDs with no package identity conflicts or duplicate crate names; 607,498 unique package-version observations with valid package references, unique `(package_id, version_str)` keys and valid temporal ordering; and valid foreign-key references across 3,618,523 dependency rows.

This decision closes component identity/domain only. It does not decide `T`, accessibility/`T_acc`, resources, outcome, sampling, `B`, `R`, or the exact dependency-resolution implementation parameters left open by DR-009. No confirmatory execution is authorised.

## DR-020 — Rust transformation candidate universe T

**Status:** ACCEPTED — NEW EXPERIMENTAL DECISION

The candidate universe `T` for EXT-1.1 is defined for each observed dependency edge `e=(v_o,p_d,q)` as the set of candidate target releases `τ(v_o,p_d,v_d)` where `v_d` is a release of the referenced target package `p_d` and `created_at(v_d) <= created_at(v_o)`.

Canonical candidate identity is `(origin_version_id, target_package_id, target_version_id)`. The dependency constraint `q` is retained as provenance but does not determine membership in `T`; accessibility is evaluated later by the frozen `R*`/`T_acc` layer. Thus `T_acc ⊆ T` remains explicit and non-circular.

Acceptance is supported by `AUDIT_DR-020_Candidate_Universe_T_v0.1.md`. The corrected auditor was executed twice against the same frozen dataset and reproduced the complete result exactly: 91,437 packages; 607,498 versions; 3,618,523 dependency edges; 194,371,905 candidates; zero duplicate candidate keys; zero temporal violations within `T`; 62,706,824 future target releases explicitly excluded; zero missing origin versions or target packages; zero target-package identity mismatches; `q` not used for membership; deterministic construction PASS; and structural T gate PASS.

This acceptance closes candidate-universe `T` only. It does not close accessibility/`T_acc`, resources, outcome, sampling, baseline `B`, `R` serialization, or remaining exact dependency-resolution implementation parameters. No confirmatory execution is authorised by DR-020.

## DR-021 — Rust accessibility operationalization

**Status:** ACCEPTED — NEW EXPERIMENTAL DECISION

The accessibility layer for EXT-1.1 is operationalized as a strict separation between candidate existence (`T`) and admissibility/selection under the frozen R* operator. For each observable dependency edge `e=(v_o,p_d,q)`, eligible target releases are those in `T(e)` that satisfy the frozen temporal cutoff and supported R* constraint semantics. If eligible candidates exist, R* selects the greatest eligible semantic version. The resulting selected edges constitute `T_acc^(R*)`.

The normative implementation is `src/rstar_v02.py`. Unsupported SemVer forms fail closed. Resource terms are not silently instantiated by this decision and remain separately governed.

Acceptance is supported by `AUDIT_DR-021_RStar_Conformance_v0.1.md`. The local synthetic conformance audit passed all fourteen predicates: exact grammar, caret grammar, bare stable caret grammar, unsupported wildcard/tilde/compound handling, temporal cutoff, maximal selection, exact selection, fail-closed unsupported input, no future target selection, row-order invariance, duplicate-version-ID fail-closed behavior, and distinction of empty candidate sets. The final result was `DR021_CONFORMANCE_PASS: True`.

The audit is dataset-independent and establishes conformance of the normative R* implementation to the tested DR-021 operational contract; it does not establish empirical accessibility results for the Rust dataset.

This decision closes the accessibility operationalization question only. It does not close resource variables/thresholds, outcome definition/horizon, sampling/exclusion, pilot N/seed, baseline `B`, or `R` serialization. No confirmatory execution is authorised by DR-021.

## DR-022 — Rust resource feasibility / threshold operationalization

**Status:** ACCEPTED — NEW EXPERIMENTAL DECISION

The DR-022 resource-feasibility audit was executed locally against the accepted pre-outcome schema and returned `RESOURCE_PREDICATE_INACTIVE: True` with interpretation `ACCEPT_RESOURCE_TRUE_CANDIDATE`.

The audit passed R1 (pre-outcome schema), R2 (transformation resource necessity), R3 (no outcome leakage), R4 (non-redundancy with R*), R5 (ex-ante threshold), R6 (determinism), and R8 (minimality). R7 (membership relevance) intentionally returned `FAIL`, because no independently justified resource variable was identified that can alter `T_acc` for the currently defined dependency-target transformation. Under the explicit DR-022 acceptance rule, this diagnostic failure supports the inactive/vacuous resource interpretation rather than an active resource constraint.

Accordingly, for the current EXT-1.1 dependency-target transformation family only:

`Resource_τ(S_t,C_t,L_t) = TRUE`

and therefore:

`T_acc^(R*) = T_acc^(R*,Resource=TRUE)`.

No Rust resource variable or numerical threshold is authorised. Measurable descriptors such as dependency count, graph size, metadata size, or target-version count are not promoted to feasibility restrictions merely because they are observable.

This decision is scope-limited. It does not claim that Rust software has no computational, build, runtime, acquisition, or other resource requirements, and it does not instantiate Resource for other transformation families. It also does not decide outcome, sampling, baseline `B`, or representation `R`.

Evidence record: `AUDIT_DR-022_Resource_Feasibility_v0.1.md`.

No confirmatory execution is authorised by DR-022 itself.

## OPEN DECISIONS

- Outcome definition and horizon: OPEN.
- Sampling/exclusion rules: OPEN.
- Pilot N and seed: OPEN.
- Baseline `B` encoding in Rust: OPEN.
- `R` serialization: OPEN.

No OPEN decision may be silently resolved in code.
