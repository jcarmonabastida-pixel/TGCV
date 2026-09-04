# EXT-1.1 Rust — `T_acc` Identifiability Protocol v0.2

**Status:** DRAFT — revision after adversarial audit; not frozen
**Purpose:** Define a non-circular, observable, reproducible operationalization of the TGCV construct `T_acc` in the Rust package ecosystem, before scientific dataset processing.

## 1. Scientific question

Can the accessible transformational space of a Rust package at time `t`, `T_acc,t`, be reconstructed from information available at `t`, such that it is distinguishable from the transformations that actually occurred?

A negative result remains scientifically admissible. If the operationalization fails audit, EXT-1.1 must record the failure rather than force a positive result.

## 2. State and context

The package state is `S_t`: the exact published package version, including its manifest-level dependency declarations and other frozen package attributes required by the transformation model.

The contemporaneous external context is `C_t`: the historical Rust registry/index state and other explicitly frozen environmental information used to evaluate dependency-resolution accessibility at `t`.

The measurement function is therefore:

`T_acc,t = F(S_t, C_t)`.

`C_t` is not permitted to contain information first becoming available after `t`.

## 3. Primary transformation `tau`

The primary transformation is a finite, machine-representable change to the package dependency configuration. The experimental primitive is a dependency-configuration transformation, not the act of publication itself.

Candidate operators, fixed before analysis, are:

1. add a dependency declaration;
2. remove a dependency declaration;
3. replace a declared dependency requirement;
4. change a declared dependency requirement to another pre-specified valid requirement form.

A package release is an observed state transition in the trajectory, not itself a member of the transformation ontology.

## 4. Finite candidate universe `U_t`

`U_t` is generated exclusively from information available in `(S_t, C_t)` and from the frozen transformation operators.

For dependency transformations, candidate dependency identities and versions MUST come from the historical registry snapshot `C_t`; future package releases cannot enter `U_t`.

The candidate universe is finite because the protocol operates over the finite package/version records represented in the frozen historical registry snapshot and a finite, pre-specified set of operators.

Observed future transitions may be used later to classify realised versus unrealised candidates, but never to generate `U_t` or define accessibility.

## 5. Technical accessibility predicate

A candidate `tau ∈ U_t` is **registry-resolvably accessible** at `t` iff all of the following hold using only `(S_t, C_t)`:

1. the resulting dependency configuration is syntactically valid under the frozen manifest rules;
2. every referenced package/version requirement is represented in `C_t`;
3. the resulting dependency graph admits a deterministic Cargo dependency-resolution solution under the frozen resolver semantics;
4. no information from a future registry snapshot, future package version, realised transition, adoption/success outcome, or later state is required to establish the above.

This is intentionally a **technical accessibility** construct. It does not claim that a developer intended, implemented, tested, or published the transformation.

## 6. Construction of `T_acc,t`

`T_acc,t = { tau ∈ U_t | Accessible(tau | S_t, C_t) }`.

The construction must be deterministic. Identical frozen inputs and rules must produce identical `T_acc,t`.

The protocol must record the exact resolver version/semantics and all configuration relevant to the accessibility decision.

## 7. Realised trajectory

The realised transformation set is defined separately as `T_real,t`, derived only after the state sequence has been reconstructed.

`T_real,t` records transformations actually observed between successive package states.

No member of `T_real,t` is automatically promoted to `T_acc,t`. Conversely, an accessible transformation may remain unrealised.

This separation is essential to avoid defining accessibility by occurrence.

## 8. Change in transformational space

For adjacent states:

`Delta T_acc,t+ = T_acc,t+1 - T_acc,t`

`Delta T_acc,t- = T_acc,t - T_acc,t+1`

Primary identity test:

`T_acc,t != T_acc,t+1`.

Realised transitions are analysed separately and cannot be substituted for `Delta T_acc`.

## 9. Temporal non-leakage rule

For every historical time `t`, construction of `S_t`, `C_t`, `U_t`, and `T_acc,t` must exclude information whose first availability is later than `t`.

In particular, the current crates.io index, future registry snapshots, future package releases, future lockfiles, adoption/download measures, survival outcomes, and observed next states are prohibited inputs to historical accessibility decisions.

Historical registry snapshots are therefore a required experimental input, not an optional convenience.

## 10. Non-circularity audit

The operationalization passes only if accessibility can be computed before observing the target future transition and without using any outcome variable the experiment seeks to explain.

A transformation being observed is evidence for trajectory, not evidence that defines its prior accessibility.

## 11. State sufficiency

`S_t` is sufficient only relative to `C_t` and the frozen measurement function `F`. The protocol does not claim that package metadata alone determine the transformational space.

The minimum frozen input is therefore the pair `(S_t, C_t)` plus the fixed rules of `F`.

## 12. Reproducibility requirements

An independent researcher must be able to reconstruct the same `T_acc,t` from:

- exact dataset identity/version;
- exact historical context snapshot `C_t`;
- exact package state `S_t`;
- frozen transformation operators;
- frozen candidate-generation algorithm;
- frozen Cargo resolver semantics/version;
- machine-readable `T_acc` output;
- cryptographic hashes of frozen input artifacts;
- hand-verifiable test fixtures.

## 13. Required counterfactual fixture

Before freeze, the implementation must demonstrate at least three manually verifiable cases:

1. **Accessible + unrealised:** a candidate belongs to `T_acc,t` but is absent from `T_real,t`.
2. **Inaccessible + unrealised:** a candidate does not belong to `T_acc,t` and is absent from `T_real,t`.
3. **Realised:** a candidate belongs to `T_real,t`; its prior accessibility must be evaluated independently rather than inferred from occurrence.

The first case is especially important because it demonstrates that `T_acc` is not merely a relabelling of the observed trajectory.

## 14. Identifiability failure conditions

EXT-1.1 identifiability fails if:

1. accessibility requires future or outcome information;
2. `U_t` depends on realised future transitions;
3. historical `C_t` cannot be reconstructed reproducibly;
4. equivalent `(S_t,C_t)` inputs can yield different `T_acc,t` because of hidden analyst choices;
5. `T_acc,t` is definitionally identical to `T_real,t`;
6. resolver semantics cannot be frozen sufficiently to make the predicate deterministic;
7. the candidate universe is not finite and explicitly bounded by the protocol.

## 15. Pre-freeze audit A1–A7

- **A1 — Unit:** Is `S_t` precisely specified?
- **A2 — Transformation:** Is `tau` a finite, observable dependency-configuration operation?
- **A3 — Accessibility:** Is registry-resolvable accessibility decidable using only `(S_t,C_t)`?
- **A4 — Candidate universe:** Is `U_t` generated without future transitions or outcomes?
- **A5 — State/context sufficiency:** Does `(S_t,C_t)` contain all information required by `F`?
- **A6 — Reproducibility:** Can an independent implementation reproduce `T_acc,t`?
- **A7 — Discriminability:** Can accessible-but-unrealised transformations be represented?

All seven must pass for the protocol to be frozen.

## 16. Decision rule

**PASS / IDENTIFIABLE:** A1–A7 pass, the counterfactual fixture passes, and no failure condition is triggered.

**FAIL / NOT IDENTIFIABLE:** Any required criterion fails. Scientific dataset processing under this operationalization is blocked.

A PASS authorises the next phase: exact scientific Rust dataset selection, acquisition, and processing.

## 17. Relation to TR-131

The protocol provides the empirical operationalization needed to test whether `T_acc` is a state/context-dependent object rather than a relabelling of realised transitions.

It does not by itself establish TR-131. TR-131 requires the resulting empirical construction to survive the identifiability and state-sufficiency tests.

## 18. Freeze discipline

This document remains a draft until the second adversarial audit is complete and the protocol is frozen under a distinct version/hash. No scientific Rust dataset may be processed for hypothesis testing before that freeze.
