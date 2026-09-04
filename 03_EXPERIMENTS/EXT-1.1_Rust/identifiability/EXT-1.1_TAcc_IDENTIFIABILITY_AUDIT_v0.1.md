# EXT-1.1 Rust — `T_acc` Identifiability Adversarial Audit v0.1

**Audited object:** `EXT-1.1_TAcc_IDENTIFIABILITY_PROTOCOL_v0.1.md`
**Status:** AUDIT COMPLETE — protocol v0.1 NOT FROZEN
**Decision:** CONDITIONAL FAIL / REVISION REQUIRED

## 1. Audit objective

Attack the proposed operationalization of `T_acc` before any scientific Rust dataset is processed. The audit asks whether the protocol can define a state-dependent transformational space that is non-circular, observable, reproducible, and empirically distinguishable from realised transitions.

## 2. A1 — Unit audit

**Verdict: PARTIAL PASS.**

The package-version unit is precise enough to be a candidate unit of observation, but `S_t` is underspecified because the relevant external registry state is not clearly separated from the package state. A package manifest alone does not determine which dependency transformations are feasible at a given historical time.

**Required correction:** represent the registry/package metadata snapshot as an explicit contextual/environmental input `C_t` (or equivalent), while keeping the package state `S_t` distinct.

## 3. A2 — Transformation audit

**Verdict: PARTIAL FAIL.**

The original candidate classes mix fundamentally different objects: edits to dependency declarations, changes in resolved versions, and publication of a new package version. The last of these is a realised release event rather than a clean counterfactual transformation primitive.

**Required correction:** define the primary transformation as a finite, machine-representable dependency-configuration change. Exclude package publication itself from the primitive `tau`; publication remains an observed trajectory event.

## 4. A3 — Accessibility audit

**Verdict: FAIL under v0.1 wording; recoverable.**

“Feasible transformation” is too broad. Whether an author could actually implement and publish a change depends on unobserved information (intent, source-code modifications, testing effort, maintainability, etc.). That would make accessibility partly unobservable.

A defensible Rust-specific construct is narrower: **registry-resolvable accessibility**. A candidate dependency transformation is accessible at `t` when, using only the package manifest state and the frozen registry metadata available at `t`, the candidate configuration is syntactically valid and admits a deterministic dependency-resolution solution under the frozen resolver rules.

This is deliberately a technical accessibility construct. It does not claim to measure whether an author would choose, implement, or publish the transformation.

## 5. A4 — Candidate-universe audit

**Verdict: FAIL under v0.1; recoverable.**

The statement that a finite `U_t` will be defined is insufficient. If `U_t` is derived from future observed transitions, `T_acc` becomes tautological.

**Required correction:** define `U_t` exclusively from information available at `t`. A principled candidate universe is generated from package/version identifiers present in the registry snapshot at `t`, combined with a pre-specified finite set of dependency-edit operators. Future releases and realised transitions must not enter `U_t`.

## 6. A5 — State sufficiency audit

**Verdict: FAIL under v0.1; recoverable.**

The package state alone is insufficient to determine dependency-resolution accessibility. The same manifest can face different accessible transformations under different registry snapshots.

**Required correction:** define the measurement function as `T_acc,t = F(S_t, C_t)` where `C_t` is an exogenous frozen registry/environment snapshot. This preserves the TGCV distinction between state and contextual conditions rather than silently embedding the environment in `S_t`.

## 7. A6 — Reproducibility audit

**Verdict: CONDITIONAL PASS.**

The protocol specifies determinism, machine-readable output, hashes, and a hand-verifiable fixture, which is adequate as a design requirement. Actual reproducibility cannot yet be demonstrated because the scientific dataset and the final resolver specification are not frozen.

C3 establishes useful infrastructure precedent: the historical Cargo lockfile records exact package versions and registry source/checksums, and the prepared environment successfully performed offline resolution. However, C3 is not evidence that the scientific `T_acc` construction is already reproducible.

## 8. A7 — Discriminability audit

**Verdict: PASS in principle, conditional on A3/A4 revision.**

`T_acc` can be analytically distinct from realised transitions if it is constructed counterfactually from all eligible candidate transformations available at `t`, rather than only from transformations observed to occur. The realised transition set is then an observed subset/trajectory, while `T_acc` is the pre-outcome accessible space.

The distinction collapses if candidate generation is based on future events or if accessibility is defined as occurrence.

## 9. Adversarial findings

### F1 — Feasibility versus authorship

The strongest threat is conflating technical resolvability with real-world ability or willingness to perform the transformation. The protocol must explicitly state which meaning is being measured.

### F2 — Infinite/ill-defined transformation space

Version constraints and arbitrary manifest edits can generate an ill-defined or effectively infinite candidate space. The experiment therefore needs a finite transformation representation and a pre-specified candidate-generation rule.

### F3 — Environment leakage

Registry contents change over time. Using the current registry to determine historical accessibility would leak future information. Historical `C_t` snapshots are therefore essential.

### F4 — Resolution is not implementation success

A Cargo-resolvable dependency configuration does not imply that the package source compiles or that the package author can successfully implement the intended feature. The protocol must not silently equate these.

### F5 — Lockfile leakage

A future `Cargo.lock` must never be used to define `T_acc,t`. A lockfile may document a realised resolution, but it cannot be the source of the counterfactual candidate universe.

### F6 — `T_acc` versus trajectory

The experimental distinction is strongest when `T_acc,t` contains transformations that did not occur. A sanity fixture must therefore include at least one accessible-but-unrealised candidate and one unrealised/inaccessible candidate.

## 10. Required revision before freeze

Protocol v0.2 must:

1. Separate `S_t` from historical registry/context `C_t`.
2. Replace broad “feasible transformation” language with an explicit technical accessibility predicate.
3. Remove package publication as a primitive transformation.
4. Define a finite `U_t` generated solely from information available at `t`.
5. Specify the dependency-resolution semantics used by the predicate.
6. Explicitly prohibit current/future registry information in historical `T_acc,t`.
7. Define the realised-transition set separately from `T_acc,t`.
8. Add a hand-verifiable fixture demonstrating accessible-but-unrealised transformations.
9. Preserve the distinction between technical accessibility and authorial/implementation feasibility.

## 11. Audit conclusion

`T_acc` is **not yet identified under v0.1**, but the failure is not a domain-level rejection. The core construct appears operationally recoverable if accessibility is deliberately narrowed to a historical, registry-resolvable transformation space and the candidate universe is generated counterfactually from contemporaneous information.

**Decision:** do not process the scientific dataset yet. Revise to protocol v0.2, then perform a second audit focused on the exact resolver semantics and the hand-verifiable counterfactual fixture.
