# EMP-1.1 — NEW CONTROLLED R OPERATIONALISATION SPECIFICATION v0.1

**Status:** PROPOSED FOR PROSPECTIVE FREEZE — CONTROLLED NEW RECONSTRUCTION  
**Date:** 2026-09-05  
**Branch:** N — Controlled New Reconstruction  
**Historical-recovery status:** CLOSED NEGATIVE; this specification does **not** claim recovery of the historical EMP-1.1 implementation.

## 1. Purpose and boundary

This document defines a new, explicit and prospective operationalisation of the TGCV representation `R` for a controlled reconstruction of EMP-1.1.

The reconstruction target is the mapping:

`S_snapshot -> T_acc -> R`

where `T_acc` is an accessibility structure induced by the frozen snapshot and a declared transition system. `R` is a finite, deterministic feature representation of that structure for the predictive comparison specified by the frozen EMP-1.1 protocol.

This specification is **not** a recovery of MVE-1.0, is **not** evidence that the historical EMP-1.1 result used these semantics, and does **not** use the historical numerical result as a tuning target.

The historical result remains an archival empirical record. It is not an input to any design, calibration, parameter selection, transformation selection, or model selection below.

## 2. Source-of-truth hierarchy

1. Frozen `Experimental_Protocol_v1_1.json`.
2. Frozen dataset/schema and sealed episode boundary used by the controlled reconstruction.
3. Existing TGCV Core decisions already established before this specification.
4. This document's explicit `RECONSTRUCTED` choices.
5. Implementation details derived mechanically from the above.

Where a choice is not determined by levels 1–3, it is labelled `RECONSTRUCTED` rather than presented as recovered fact.

## 3. Classification of specification elements

- **SPECIFIED:** directly imposed by a previously frozen artifact.
- **DERIVED:** follows without a free scientific choice from specified rules.
- **RECONSTRUCTED:** an explicit new operational choice introduced here.
- **VERIFIED:** subsequently demonstrated by an independent acceptance test.

No item labelled `RECONSTRUCTED` may later be relabelled `SPECIFIED` merely because the resulting empirical effect is desirable.

## 4. Snapshot state

### 4.1 State variables

For each episode at the frozen observation boundary:

`S_t = (V_t, E_t, x_t, q_t, o_t)`

where:

- `V_t`: finite set of component identifiers;
- `E_t ⊆ V_t × V_t`: directed relational edges;
- `x_t(v)`: declared scalar resource/component attributes available at the snapshot;
- `q_t`: three scalar resource values available to the baseline `B`;
- `o_t`: objective identity.

The exact concrete domains and episode schema must be taken from the sealed dataset. If a field required by this definition is absent, execution fails closed rather than imputing it.

`V_t`, `E_t`, `x_t`, `q_t`, and `o_t` are **SPECIFIED/DERIVED** from the frozen episode record. No future trajectory or outcome field may enter them.

### 4.2 Baseline representation

The frozen protocol defines `B` as:

- component count;
- three resource values;
- objective identity;
- deliberately excluding relational transformation structure.

This definition is **SPECIFIED** and is not altered here.

## 5. Transformation universe

The transformation universe is a finite, typed set of primitive operations over a snapshot. Exactly six transformation families are defined for the controlled reconstruction.

The six families are:

1. `ADD_COMPONENT`
2. `REMOVE_COMPONENT`
3. `ADD_EDGE`
4. `REMOVE_EDGE`
5. `REWIRE_EDGE`
6. `MODIFY_ATTRIBUTE`

The choice of these six families is **RECONSTRUCTED**. They are selected prospectively because together they represent node creation/deletion, relation creation/deletion, relational reconfiguration, and non-topological state modification while remaining finite and mechanically testable. Their selection is independent of the historical EMP-1.1 result.

### 5.1 ADD_COMPONENT

`ADD_COMPONENT(v*)` is admissible only when `v*` is not already in `V_t` and the generator's declared component-domain constraints permit creation.

### 5.2 REMOVE_COMPONENT

`REMOVE_COMPONENT(v)` is admissible only when `v ∈ V_t` and removal satisfies the declared structural validity constraints. Removal deletes all incident edges deterministically.

### 5.3 ADD_EDGE

`ADD_EDGE(u,v)` is admissible only when `u,v ∈ V_t`, `(u,v) ∉ E_t`, and the declared structural validity constraints permit the edge.

### 5.4 REMOVE_EDGE

`REMOVE_EDGE(u,v)` is admissible only when `(u,v) ∈ E_t`.

### 5.5 REWIRE_EDGE

`REWIRE_EDGE((u,v),(u,w))` is admissible only when `(u,v) ∈ E_t`, `w ∈ V_t`, `(u,w) ∉ E_t`, and the declared structural validity constraints permit the resulting graph. Equivalent source-preserving rewires may be canonicalised so that each resulting transformation has one identity.

### 5.6 MODIFY_ATTRIBUTE

`MODIFY_ATTRIBUTE(v,a,δ)` is admissible only for attributes explicitly included in the frozen snapshot schema and only for a value change permitted by the generator's declared attribute domain. The transformation identity records attribute name and discretised transition class, not an arbitrary future value.

The exact attribute domains and allowed modification classes are **RECONSTRUCTED** and must be frozen before any confirmatory fit.

## 6. Edge semantics

Edges are directed relational structure. An edge `(u,v)` means that the current state contains an observable directed relation from component `u` to component `v`.

No semantic label such as dependency, causality, cooperation, or influence may be inferred unless the frozen dataset explicitly defines it.

This is **RECONSTRUCTED** as a neutral graph interpretation and is deliberately narrower than a domain-specific causal interpretation.

The representation must preserve edge direction. Reversing `(u,v)` to `(v,u)` is a distinct structural operation.

## 7. Transition function

Each primitive transformation `τ` has a deterministic partial transition function:

`P_τ(S_t)=1  =>  S_{t+1}=τ(S_t)`

`P_τ(S_t)=0  =>  τ ∉ T_acc(S_t)`

A transition is admissible only when all family-specific preconditions and global validity constraints hold.

Global validity constraints are:

1. all component identifiers are unique;
2. all edges have endpoints in `V`;
3. no duplicate directed edges exist;
4. component and attribute domains remain valid;
5. transformations do not use information outside the frozen snapshot;
6. the operation terminates after one primitive step.

These rules are **RECONSTRUCTED** except where directly implied by the snapshot schema.

## 8. Accessibility rule

For the controlled reconstruction:

`T_acc(S_t) = { τ ∈ U(S_t) : P_τ(S_t)=1 }`

where `U(S_t)` is the finite universe of transformation instances constructible from the current snapshot and frozen domains.

Accessibility is therefore defined by **pre-state feasibility**, not by whether the transformation occurs in the observed future trajectory and not by whether it improves the eventual outcome.

This is a **DERIVED** consequence of the declared transition-system formulation plus a **RECONSTRUCTED** choice of finite primitive transformation universe and precondition set.

No closure over multiple steps is used in the primary `T_acc` definition. Multi-step reachability is a downstream analysis and must not be folded back into the one-step accessibility representation.

## 9. T_acc as a structure

`T_acc` is treated as a typed labelled structure, not as a scalar count.

Each accessible transformation instance has a canonical identity:

`(family, operands, attribute-class)`

and a deterministic resulting-state signature:

`sig(τ(S_t))`.

Canonical ordering is lexicographic over a stable serialization of transformation identity. This makes the representation invariant to input row order.

The transformation structure therefore retains:

- transformation family;
- structural operands;
- admissibility;
- resulting-state signature.

It must not include future outcome, future trajectory, or post-boundary observations.

## 10. R representation

`R` is a fixed-length deterministic encoding of `T_acc` consisting of four blocks:

### R1 — family availability vector

For each of the six families, record whether at least one accessible instance exists.

Dimension: 6.

### R2 — family cardinality vector

For each family, record the number of accessible instances, with a fixed pre-declared cap and overflow bin if required by the sealed dataset's maximum domain.

Dimension: 6 plus any explicitly frozen overflow indicators.

### R3 — relational reachability signature

For each component, compute deterministic structural summaries induced by the accessible transformation structure:

- number of accessible transformations incident to the component;
- number of distinct transformation families incident to the component;
- number of accessible transformations that add/remove/rewire an edge touching the component.

The component-level vector is aggregated using fixed order-independent statistics: mean, standard deviation, minimum, maximum, and quantiles at 25%, 50%, and 75% where the component set is non-empty.

### R4 — transition-result structural signature

For each accessible transformation, derive the delta in:

- component count;
- edge count;
- number of connected components under the undirected projection;
- mean in-degree;
- mean out-degree.

Aggregate each quantity by transformation family using mean and standard deviation, with deterministic zero/empty conventions.

The choice of R1–R4 and these aggregations is **RECONSTRUCTED**. It is deliberately structural and relation-sensitive while avoiding a direct copy of the raw graph.

## 11. Exclusion of outcome leakage

The following are prohibited inputs to `R`:

- observed future transitions;
- future states;
- trajectory length after the snapshot;
- success/failure outcome;
- any target label;
- any feature computed from the future trajectory;
- any variable whose value is assigned using the final historical result;
- any current/live external registry or database state not part of the sealed dataset.

This is **SPECIFIED/DERIVED** from the frozen no-retrofit rule and the snapshot-boundary requirement.

## 12. Empty and degenerate cases

If `T_acc = ∅`:

- all R1 entries are 0;
- all R2 entries are 0;
- R3 and R4 use a fixed zero vector;
- an explicit `R_EMPTY=1` indicator is added.

If a component-level aggregation has one component, standard deviation is defined as 0.

If a required numeric input is missing from the frozen snapshot, the episode is invalid for the reconstruction and must be reported separately; silent imputation is prohibited.

These conventions are **RECONSTRUCTED** and must be frozen before execution.

## 13. Encoding and normalization

All R features are numeric.

No target-dependent scaling is permitted.

If normalization is used, it must be fitted on the training partition only and applied unchanged to the test partition. The default controlled reconstruction is **no normalization**, because the R blocks are already defined as bounded or directly interpretable structural statistics.

Objective identity remains in `B` as a categorical variable using a deterministic one-hot encoding fit on training data only; unseen test categories must use a fixed unknown-category representation.

The encoding policy is **RECONSTRUCTED** where not imposed by the frozen protocol.

## 14. Data-generation boundary

The controlled reconstruction must not regenerate or alter the sealed historical EMP-1.1 confirmatory episodes if those episodes are the designated evaluation dataset.

For any new pilot or unit-test generator used to validate the implementation:

- generator version is frozen before inspection of confirmatory results;
- seed is recorded;
- generated snapshots are separate from confirmatory data;
- generator output is not used to tune R against the historical confirmatory effect.

The exact generator implementation, pilot seed, and fold construction remain separate reconstruction artefacts and must be specified before any confirmatory reproduction attempt.

## 15. Controls

The frozen protocol requires:

1. `R_count_only`;
2. `R_permuted_marginals`;
3. alternative learner `RandomForestClassifier`.

For `R_count_only`, retain only the six R2 family counts, with all other R blocks removed.

For `R_permuted_marginals`, independently permute each R feature across training episodes using a fixed pre-registered permutation seed while preserving each feature's marginal distribution; no permutation may cross the train/test boundary.

The exact permutation seed and model hyperparameters are not supplied by the frozen protocol and therefore remain `OPEN / RECONSTRUCTED` until separately frozen.

## 16. Learner and statistical test boundary

The frozen protocol remains authoritative for:

- primary metric: paired out-of-sample `Δ = LL_B - LL_B+R`;
- alpha = 0.05;
- minimum primary improvement `Δ >= 0.04`;
- 30,000 training episodes;
- 10,000 test episodes;
- HistGradientBoostingClassifier as the primary learner with identical fixed hyperparameters in both arms;
- paired Monte-Carlo sign-flip permutation test with 200,000 flips and seed 13579.

This document does not invent missing learner hyperparameters. They must be separately frozen before execution.

## 17. Independence and determinism requirements

The implementation is acceptable only if:

1. identical snapshot + identical frozen configuration produces byte-identical canonical R;
2. reordering input rows does not alter R;
3. future fields are unavailable to the R constructor;
4. train/test separation is respected;
5. no live external state is consulted;
6. all reconstruction choices are represented in a machine-readable configuration;
7. a second independent execution produces identical R hashes and identical evaluation inputs.

## 18. Prospective freeze rule

Once this specification is frozen for controlled execution:

- transformation families cannot be changed after test-set sealing;
- edge semantics cannot be changed after test-set sealing;
- accessibility predicates cannot be changed after test-set sealing;
- R aggregation/encoding cannot be changed after test-set sealing;
- generator and split rules cannot be changed after test-set sealing;
- learner hyperparameters cannot be selected using confirmatory results;
- the historical result `Δ=0.07942359585000518` is never a tuning objective.

Any later change creates a new reconstruction version.

## 19. Verification gates

Before a new confirmatory execution, the following gates must pass:

### Gate N-R1 — semantic completeness

Every transformation family, predicate, transition, aggregation, encoding, and degenerate-case rule has an explicit definition and classification.

### Gate N-R2 — implementation conformance

Unit tests demonstrate exact conformance to this specification, including row-order invariance, temporal/future-field exclusion, deterministic canonicalisation, empty-set handling, and invalid-input fail-closed behaviour.

### Gate N-R3 — leakage audit

Independent inspection demonstrates that R is computed exclusively from the frozen snapshot and declared static configuration.

### Gate N-R4 — sealed-data execution

The implementation processes the sealed dataset without modifying it and emits complete provenance manifests and hashes.

### Gate N-R5 — double execution

Two independent clean executions produce identical reconstruction outputs and compatible evaluation results.

### Gate N-R6 — confirmatory reproduction

Only after N-R1–N-R5 pass may the frozen EMP-1.1 predictive test be executed.

## 20. Scientific status

This specification establishes a **new controlled operationalisation**, not historical recovery.

If the subsequent experiment supports the hypothesis, the strongest justified claim is evidence for predictive utility of **this explicitly specified operationalisation of accessible-transformation structure** under the controlled experiment.

It does not by itself establish:

- historical equivalence to MVE-1.0;
- equivalence to Cargo or another external domain resolver;
- universal validity of TGCV;
- causal efficacy of any real-world interaction;
- literature novelty.

## 21. Current decision

**DECISION: PROPOSE NEW CONTROLLED R OPERATIONALISATION — NOT YET FROZEN FOR CONFIRMATORY EXECUTION.**

Blocking items that must be frozen in the next conformance specification include:

1. exact component/attribute domains from the sealed EMP-1.1 dataset;
2. exact admissibility predicates for each transformation family;
3. exact finite candidate universe and any size caps;
4. exact quantile convention and numerical precision;
5. exact categorical encoding;
6. exact `R_permuted_marginals` seed;
7. exact HistGradientBoostingClassifier hyperparameters;
8. exact RandomForestClassifier hyperparameters;
9. exact pilot generator and seed, if a pilot is used;
10. exact confirmatory split construction.

No confirmatory result may be generated until these items are separately frozen and N-R1 is marked PASS.
