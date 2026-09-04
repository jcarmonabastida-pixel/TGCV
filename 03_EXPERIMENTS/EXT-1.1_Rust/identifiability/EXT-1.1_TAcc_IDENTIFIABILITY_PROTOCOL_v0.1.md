# EXT-1.1 Rust — `T_acc` Identifiability Protocol v0.1

**Status:** DRAFT — pre-audit, not frozen
**Purpose:** Establish whether the TGCV construct `T_acc` (set of accessible transformations) can be identified in the Rust ecosystem in a non-circular, observable, and reproducible way before scientific dataset processing.

## 1. Scientific question

Can the set of transformations accessible to a Rust package at time `t`, `T_acc,t`, be reconstructed from observable data without defining accessibility by reference to the outcome that the experiment is intended to explain?

A negative result is scientifically admissible: if no non-circular operationalization survives audit, EXT-1.1 must record an identifiability failure rather than force a positive construction.

## 2. Observed system `S`

The primary unit of observation is a **published Rust package version** identified by its package name and exact version.

For each observation, the system state is represented by externally observable package metadata and source/build-relevant declarations available in the frozen experimental data. At minimum this includes the package identity/version, declared dependencies and their version constraints, and the registry/package metadata required to reconstruct candidate transformations.

The experimental unit must be fixed before data analysis; it must not be changed after inspecting results in order to improve identifiability.

## 3. Transformation `tau`

A transformation is an externally observable change that results in a distinct package-version state or in a changed set of feasible package-level dependency configurations.

Candidate transformation classes to audit:

1. **Dependency acquisition:** adding a dependency that was not previously declared.
2. **Dependency substitution/version change:** changing a declared dependency constraint or resolved dependency version.
3. **Dependency removal:** removing a declared dependency.
4. **Package release:** publishing a new package version that changes the package's declared dependency configuration.

The final transformation ontology must select only transformations that are both observable in the dataset and operationally decidable without using the later outcome as the definition of accessibility.

## 4. Accessibility criterion

A candidate transformation `tau` is **accessible** for state `S_t` iff the frozen observable data provide sufficient evidence, using only information available at or before `t`, that `tau` is a feasible transformation under the predefined rules.

Accessibility must not be defined as:

- a transformation that actually occurred;
- a transformation that led to package success, adoption, survival, or any other outcome;
- a transformation selected because it predicts the observed next state;
- a transformation whose feasibility is inferred from the post-transformation state itself.

Occurrence is therefore evidence about realised trajectory, not by itself the definition of accessibility.

## 5. Construction of `T_acc,t`

For each package state `S_t`, construct:

`T_acc,t = { tau | tau satisfies the frozen transformation definition and the frozen accessibility criterion at t }`.

The construction must be deterministic: the same frozen input data and rules must yield the same set.

Where complete enumeration of all mathematically possible transformations is infeasible, the protocol must define a finite observable candidate universe `U_t` before analysis and establish that `T_acc,t` is the subset of `U_t` satisfying the accessibility predicate. Any limitation introduced by `U_t` must be treated as part of the measurement model, not hidden as a scientific result.

## 6. Change in transformational space

A change is recorded when the reconstructed sets differ:

`Delta T_acc,t = T_acc,t+1 - T_acc,t` and
`Delta T_acc,t^- = T_acc,t - T_acc,t+1`.

The primary binary test is:

`T_acc,t != T_acc,t+1`.

Secondary measures may include additions, removals, and normalized set distance, but these are not substitutes for the identity test.

## 7. Non-circularity audit

The protocol passes the non-circularity criterion only if accessibility can be decided without using:

- future package versions;
- realised future transformations;
- adoption/download/success outcomes;
- survival or disappearance outcomes;
- any variable derived from the target phenomenon being explained.

If any component of the accessibility predicate requires future or outcome information, that component must be removed or explicitly classified as post hoc/explanatory rather than part of `T_acc`.

## 8. Observability and reproducibility audit

An independent researcher must be able to reconstruct `T_acc,t` and `T_acc,t+1` from the frozen dataset, frozen candidate universe, and frozen rules.

The protocol therefore requires:

- exact dataset identity and version;
- exact observation timestamps/version ordering;
- deterministic transformation-generation rules;
- deterministic accessibility predicate;
- machine-readable output for `T_acc`;
- cryptographic hashes for frozen input artifacts where applicable;
- a test fixture with at least one hand-verifiable example.

## 9. Identifiability failure conditions

EXT-1.1 identifiability fails if any of the following holds after audit:

1. Accessibility cannot be decided without using the realised outcome.
2. The candidate transformation universe is defined from observed future transitions in a way that makes `T_acc` tautological.
3. Equivalent observed states can receive different `T_acc` solely because of hidden analyst choices not represented in the frozen state/data.
4. The required inputs cannot be reconstructed reproducibly by an independent researcher.
5. `T_acc` collapses into the realised-transition set, making the construct empirically indistinguishable from observed trajectory by definition.

## 10. Required pre-freeze audit

Before downloading/processing the scientific Rust dataset, perform and record:

- **A1 — Unit audit:** Is the package-version state `S_t` precisely specified?
- **A2 — Transformation audit:** Is `tau` externally observable and decidable?
- **A3 — Accessibility audit:** Can accessibility be determined without future/outcome information?
- **A4 — Candidate-universe audit:** Is `U_t` fixed independently of observed future transitions?
- **A5 — State sufficiency audit:** Does the frozen state contain enough information to determine `T_acc,t` under the rules?
- **A6 — Reproducibility audit:** Can a second implementation reproduce the same `T_acc` from the frozen inputs?
- **A7 — Discriminability audit:** Is `T_acc` analytically distinguishable from the realised transition set?

## 11. Decision rule

The protocol is **PASS / IDENTIFIABLE** only if A1–A7 pass and no identifiability failure condition is triggered.

Otherwise the result is **FAIL / NOT IDENTIFIABLE**, with the failed criterion(s) recorded.

A PASS authorises the next phase: exact scientific Rust dataset selection, acquisition, and processing.

A FAIL blocks scientific dataset processing under the current operationalization and triggers protocol revision or abandonment of the Rust domain for this test.

## 12. Relation to TR-131

This protocol operationalizes the empirical side of TR-131: whether `T_acc` can be reconstructed as a state-dependent object rather than being merely a relabelling of observed transitions.

TR-131 is not considered passed merely because a computable set can be produced. The set must satisfy identifiability, non-circularity, state sufficiency, and reproducibility requirements.

## 13. Freeze discipline

This document is a draft. No scientific Rust dataset should be processed for hypothesis testing until the protocol has been audited, revised if necessary, and frozen under a distinct version/hash.
