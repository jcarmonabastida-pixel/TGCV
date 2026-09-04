# EXT-1.1 Rust — `T_acc` Identifiability Protocol v0.3

**Status:** DRAFT — pre-freeze revision after second adversarial audit
**Purpose:** Define a finite, canonical, non-circular, observable and reproducible operationalization of TGCV `T_acc` in the Rust package ecosystem before scientific dataset processing.

## 1. Scientific question

Can the accessible transformational space of a Rust package at historical time `t`, `T_acc,t`, be reconstructed from contemporaneous information and frozen resolution rules, while remaining distinguishable from transformations actually realised?

A negative result is scientifically admissible. If the operationalization fails the final audit, EXT-1.1 must record the failure and must not force a positive result.

## 2. Explicit input model

The measurement function is:

`T_acc,t = F(S_t, C_t, R)`

where:

- `S_t` = package-local state;
- `C_t` = historical contemporaneous registry/context snapshot;
- `R` = frozen resolver and measurement specification.

All three inputs MUST be versioned or cryptographically hashed before scientific analysis.

### 2.1 Package state `S_t`

For the minimal confirmatory experiment, `S_t` is exactly the following machine-readable record:

1. package name and version;
2. complete normal dependency declarations relevant to the experiment;
3. dependency requirement strings for those declarations;
4. dependency kind, restricted to normal registry dependencies;
5. target/platform condition, restricted to unconditional dependencies;
6. optional flag, restricted to `false`;
7. feature activation, restricted to the fixed experiment policy;
8. Rust edition and resolver declaration where relevant to `R`.

Build-dependencies, dev-dependencies, path dependencies, git dependencies, local patches, workspace inheritance, target-specific dependencies, optional dependencies and feature-dependent dependency activation are excluded from the minimal confirmatory domain unless explicitly represented in a later protocol revision.

The package state is therefore closed under a fixed schema rather than an open-ended phrase such as "other relevant attributes".

## 3. Historical context `C_t`

`C_t` is the exact historical registry snapshot available at `t` for the package/version universe used by the experiment.

For the minimal confirmatory experiment, `C_t` contains only registry metadata necessary to establish the existence, version identity, checksum and dependency metadata of eligible registry package versions.

The current live registry MUST NOT be queried while constructing historical `T_acc,t`.

A historical snapshot is an input artifact with a cryptographic hash and provenance record.

## 4. Frozen resolver specification `R`

`R` is an immutable machine-readable specification containing at minimum:

1. exact Cargo toolchain/version used for resolution;
2. Cargo resolver generation;
3. registry source and snapshot identity;
4. target/platform fixed for the experiment;
5. feature policy fixed for the experiment;
6. yanked-version handling;
7. source replacement/configuration policy;
8. lockfile-generation procedure;
9. command-line/configuration flags affecting resolution;
10. deterministic invocation environment required by the experiment.

The exact values are to be frozen in a separate resolver specification artifact before final protocol freeze.

## 5. Canonical primary transformation `tau`

The minimal confirmatory transformation is a **single normal registry dependency-edge insertion**.

It is represented canonically as:

`tau = (package_name, package_version, requirement)`

subject to the fixed experiment parameter domain:

- registry source = the historical registry represented by `C_t`;
- dependency kind = normal;
- target condition = unconditional;
- optional = false;
- feature set = fixed empty set for the candidate edge;
- requirement representation = one canonical requirement generated from the exact candidate version.

For candidate package version `p@v`, the canonical requirement is the exact-version requirement `=v`.

Thus each eligible package version contributes at most one candidate dependency edge.

Removal and replacement operations are deliberately excluded from the minimal confirmatory ontology. They may be evaluated in later extensions only after the minimal construct passes identifiability.

## 6. Finite candidate universe `U_t`

Define:

`EligibleVersions(C_t) = { (p,v) | p@v is represented in C_t and satisfies the fixed eligibility rules }`.

The candidate universe is:

`U_t = { tau(p,v) | (p,v) ∈ EligibleVersions(C_t) }`

with `tau(p,v) = (p,v,=v)`.

Because the historical registry snapshot is finite and the operator and parameter domains are fixed and finite, `U_t` is finite.

No candidate may be added because it was observed later in the package trajectory.

No future package release may enter `U_t`.

No analyst-selected candidate subset may be introduced after inspection of realised transitions or outcomes.

## 7. Technical accessibility predicate

For `tau ∈ U_t`, construct the counterfactual package manifest obtained by adding the canonical dependency edge represented by `tau` to `S_t`.

`Accessible(tau | S_t,C_t,R) = 1` iff and only if:

1. the counterfactual manifest conforms to the fixed manifest schema;
2. the candidate package/version exists in `C_t`;
3. dependency resolution succeeds under exactly the frozen rules in `R` and historical context `C_t`;
4. no future registry information, future package release, observed next state, adoption/success measure, survival outcome, or future lockfile is used;
5. the resolution result is deterministic under repeated execution with identical `(S_t,C_t,R,tau)` inputs.

This construct measures **registry-resolvable technical accessibility** only. It does not measure authorial intention, coding effort, implementation success, testing success, adoption, popularity or survival.

## 8. Construction of `T_acc,t`

`T_acc,t = { tau ∈ U_t | Accessible(tau | S_t,C_t,R) = 1 }`.

The output MUST be a canonical, machine-readable set sorted by the canonical tuple ordering.

The algorithm MUST record inclusion/exclusion and the reason for every candidate, not only successful candidates.

## 9. Realised transformation set `T_real,t`

`T_real,t` is reconstructed separately from observed package states.

For the minimal dependency-edge ontology, a realised transformation is a dependency edge insertion that can be identified from successive published package manifests and that conforms to the same canonical representation.

`T_real,t` is never used to construct `U_t` or evaluate prior accessibility.

For an observed transformation, its prior accessibility is evaluated from the preceding `(S_t,C_t,R)` only.

## 10. Change in transformational space

For adjacent historical states:

`Delta T_acc,t+ = T_acc,t+1 - T_acc,t`

`Delta T_acc,t- = T_acc,t - T_acc,t+1`

and the primary identity comparison is:

`T_acc,t != T_acc,t+1`.

Realised transitions remain analytically separate from changes in accessible space.

## 11. Temporal non-leakage

For every historical `t`, all inputs used to construct `T_acc,t` MUST have been available no later than `t`.

The following are prohibited inputs to historical accessibility decisions:

- current live registry state;
- future registry snapshots;
- future package versions;
- future package manifests;
- future lockfiles;
- adoption/download measures;
- survival outcomes;
- observed next states;
- any outcome variable used later in hypothesis testing.

The historical snapshot `C_t` must be immutable and hashed before use.

## 12. Counterfactual fixture

Before final freeze, a synthetic or historical micro-registry fixture MUST demonstrate all three cases:

### Case A — accessible + unrealised

A candidate `tau_A` satisfies:

`tau_A ∈ T_acc,t` and `tau_A ∉ T_real,t`.

### Case B — inaccessible + unrealised

A candidate `tau_B` satisfies:

`tau_B ∉ T_acc,t` and `tau_B ∉ T_real,t`.

### Case C — realised

A candidate `tau_C` satisfies:

`tau_C ∈ T_real,t` and its prior accessibility is independently evaluated from `(S_t,C_t,R)`.

The fixture MUST be small enough for manual verification and MUST NOT depend on the scientific dataset.

## 13. Determinism and reproducibility

An independent researcher must be able to reproduce the same result from:

- the exact `S_t` record;
- the exact historical `C_t` snapshot;
- the exact resolver specification `R`;
- the frozen candidate-generation algorithm;
- the frozen canonical transformation grammar;
- the exact software/toolchain versions;
- machine-readable expected output;
- cryptographic hashes of all frozen inputs;
- the hand-verifiable counterfactual fixture.

Repeated execution with identical frozen inputs MUST produce byte-identical canonical output.

## 14. Identifiability failure conditions

EXT-1.1 identifiability fails if:

1. accessibility requires information first available after `t`;
2. `U_t` depends on realised future transitions or outcomes;
3. `S_t`, `C_t` or `R` are not closed and machine-reproducible;
4. equivalent frozen inputs permit hidden analyst choices that change `T_acc,t`;
5. `T_acc,t` is definitionally identical to `T_real,t`;
6. resolver semantics are not sufficiently frozen for deterministic evaluation;
7. `U_t` is not finite under the frozen grammar;
8. the counterfactual fixture cannot produce an accessible-but-unrealised candidate.

## 15. Final audit A1–A7

- **A1 — Unit:** Is `S_t` explicitly closed and machine-readable?
- **A2 — Transformation:** Is `tau` canonical, finite and observable?
- **A3 — Accessibility:** Is the predicate decidable using only `(S_t,C_t,R)`?
- **A4 — Candidate universe:** Is `U_t` finite and generated without future information?
- **A5 — State/context/rules sufficiency:** Are `S_t`, `C_t` and `R` jointly sufficient for `F`?
- **A6 — Reproducibility:** Can an independent implementation reproduce byte-identical output?
- **A7 — Discriminability:** Does the fixture demonstrate accessible-but-unrealised transformations?

All seven must pass, together with the counterfactual fixture, for freeze.

## 16. Decision rule

**PASS / IDENTIFIABLE:** A1–A7 pass, the fixture passes, no failure condition is triggered, and the resolver specification is frozen and hashed.

**FAIL / NOT IDENTIFIABLE:** Any required criterion fails. Scientific dataset processing is blocked.

A PASS authorises exact scientific Rust dataset selection, acquisition and processing.

## 17. Relation to TR-131

This protocol operationalises the empirical construction required to test whether `T_acc` is a state/context/rules-dependent transformational object rather than a relabelling of realised transitions.

It does not itself establish TR-131. TR-131 remains the higher-level state-sufficiency/transformational-space irreducibility test.

## 18. Freeze discipline

This v0.3 document remains a draft until:

1. the resolver specification `R` is created and hashed;
2. the micro-fixture is executed and independently verified;
3. the final adversarial audit passes A1–A7;
4. a distinct frozen protocol version and hash are committed.

No scientific Rust dataset may be processed for hypothesis testing before that freeze.
