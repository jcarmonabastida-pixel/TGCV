# N-R4B — Controlled Outcome/Trajectory Generation Specification v0.1

**Status:** PROPOSED FOR PROSPECTIVE FREEZE  
**Branch:** N — Controlled New Reconstruction  
**Date:** 2026-09-05  
**Scope:** post-snapshot outcome/trajectory generation only

## 1. Purpose

This specification defines the controlled Branch N process that maps a sealed initial snapshot into a finite post-snapshot trajectory and binary outcome for the prospective reconstruction of EMP-1.1.

It is a new controlled reconstruction specification. It is **not** a recovery of the historical EMP-1.1/MVE-1.0 generator.

No learner fitting or confirmatory execution is authorized by this specification alone.

## 2. Boundary conditions

The initial snapshot is the output of N-R4A and is treated as sealed input:

`S_0 = (V_0,E_0,q_0,o_0)`

The following are immutable during outcome generation:

- initial snapshot identity;
- initial component set;
- initial resource vector;
- initial objective;
- initial `T_acc(S_0)` and encoded `R(S_0)`;
- train/test split assignment;
- all frozen N-R1.2/N-R1.3 semantics.

Outcome generation may use the Branch N transformation universe and `apply_transformation`, but must not modify the definition or encoding of `T_acc` or `R`.

## 3. Horizon

The trajectory horizon is fixed at:

`H = 6`

There are at most six post-snapshot transition steps. `H` is an outcome/trajectory parameter and is not part of `R`.

## 4. Objective-conditioned goal

The objective label `O01..O12` is an exogenous target variable supplied by the initial snapshot.

For prospective Branch N reconstruction, each objective is represented by a deterministic goal predicate `G_o(S)` defined before execution. The predicate must depend only on the current state and the objective label, never on future states, learner outputs, or recorded historical results.

### Reconstruction rule

The twelve objective predicates are defined as a fixed deterministic family over the state representation. Each objective corresponds to a distinct target condition over the current component/edge/resource configuration.

**Important:** the exact twelve historical goal predicates were not recovered. Therefore their identities are explicitly classified as **RECONSTRUCTED**, not HISTORICAL.

## 5. Transition policy

At each step `h`:

1. evaluate the current state against the objective;
2. if the objective is satisfied, terminate successfully;
3. otherwise enumerate the currently accessible Branch N transformations using the frozen N-R1.2 universe and predicates;
4. choose one accessible transformation using a deterministic, objective-independent stochastic policy;
5. apply the transformation;
6. continue until success or `H` steps are exhausted.

The policy must not inspect the final outcome, learner predictions, test performance, or historical EMP-1.1 result.

## 6. Controlled stochastic policy

A single explicit pseudo-random generator instance is initialized from a registered episode-level trajectory seed.

At every non-terminal step, the policy selects uniformly from the canonical ordered list of currently accessible transformations.

This policy is a **RECONSTRUCTED Branch N rule**. It is not claimed to be the historical policy.

Canonical transformation ordering is inherited from N-R2:

1. family order fixed by N-R1.3;
2. parameter ordering fixed by N-R1.2 implementation;
3. no dependence on container/hash iteration order.

## 7. Initial-state information available to the trajectory process

The trajectory process may use:

- current state `S_h`;
- objective `o_0`;
- current accessible transformations `T_acc(S_h)`;
- trajectory step `h`;
- registered RNG state.

It may not use:

- any future trajectory state not yet generated;
- future transformation choices;
- outcome labels generated later in the same episode;
- `R(S_0)` as a policy input unless this is explicitly required by a later frozen specification;
- learner predictions;
- test-set metrics;
- the historical recorded EMP-1.1 result;
- external/live data.

## 8. Outcome definition

The binary outcome is:

`Y = 1` if and only if `G_o(S_h)=1` for some `h` in `{0,...,H}`.

Otherwise:

`Y = 0`.

The outcome is therefore generated strictly after the initial snapshot and is not an input feature of `B` or `R`.

## 9. Trajectory record

A trajectory record may contain:

- `episode_id`;
- initial snapshot identifier/hash;
- objective;
- `H`;
- stepwise state hashes;
- selected transformation identifiers;
- terminal step;
- terminal state hash;
- binary outcome `Y`;
- trajectory RNG seed;
- generator/specification identifiers;
- implementation/environment hashes.

For the learner input table, only the sealed initial snapshot and its derived `B` and `R` may be consumed. Trajectory internals and `Y` remain outcome-side data.

## 10. Separation of predictor and outcome

The causal/analytical boundary is:

`S_0 -> T_acc(S_0) -> R(S_0)`  [predictor-side]

and independently:

`S_0, objective, stochastic policy -> trajectory -> Y`  [outcome-side]

The outcome process must not feed information backward into construction of `R`.

The same initial snapshot may therefore be used to derive predictor features before trajectory simulation, while the resulting trajectory/outcome is generated independently afterward.

## 11. Determinism and reproducibility

Given identical:

- initial snapshot bytes;
- objective;
- trajectory seed;
- Branch N implementation;
- N-R1.2 specification;
- runtime;

trajectory generation must produce byte-identical canonical output.

A second clean execution must reproduce identical trajectory/output hashes. Any mismatch is FAIL/BLOCKED.

## 12. Train/test separation

The train/test split is inherited unchanged from N-R4A:

- train seed: `3,100,000`;
- test seed: `4,100,000`.

Trajectory generation must not use test outcomes to define or alter goal predicates, policy, transformation semantics, feature encoding, learner settings, or acceptance thresholds.

The locked test set remains untouched by model/rule selection.

## 13. Historical 20,000-episode pilot

The historical EMP-1.1 pilot procedure is not recovered and remains OPEN.

This specification does not silently replace the historical pilot with a newly generated 20,000-episode corpus. Any prospective pilot must be separately specified and frozen.

## 14. Scientific integrity constraints

The following are prohibited:

1. tuning goal predicates to reproduce the recorded historical effect;
2. changing transition policy after observing learner performance;
3. using outcome prevalence to redesign `R`;
4. selecting objective semantics from test-set results;
5. modifying H, outcome definition, or trajectory policy after confirmatory test sealing;
6. introducing external/live state;
7. treating the reconstructed generator as historical MVE-1.0 evidence.

## 15. Open items before N-R4B freeze

The following must be resolved prospectively before implementation:

1. exact reconstructed definitions of the twelve goal predicates;
2. exact trajectory RNG seeding scheme and seed derivation from episode identity;
3. exact canonical serialization of trajectory records;
4. exact handling if `T_acc(S_h)=∅` before `H` is reached;
5. exact policy behavior when multiple transformations lead to the same successor state;
6. explicit verification that the outcome process cannot leak into predictor construction;
7. implementation and conformance runner;
8. independent fixtures including success-at-0, success-before-H, failure-at-H, and empty-accessibility cases.

## 16. Acceptance gate

N-R4B can be frozen only when:

- all open items are resolved without reference to the recorded historical result as a tuning target;
- the twelve goal predicates are explicitly versioned and classified RECONSTRUCTED;
- trajectory policy is explicit and deterministic conditional on its registered RNG seed;
- outcome definition is executable and unambiguous;
- trajectory/predictor separation is verified;
- train/test seed separation is preserved;
- clean rerun is byte-identical;
- no learner fitting or confirmatory result is executed during the gate.

## 17. Scientific boundary

Passing N-R4B will establish only a controlled prospective outcome/trajectory generator for Branch N. It will not establish historical reproducibility, Cargo equivalence, MVE-1.0 recovery, causal validity, universal TGCV validity, or replication of the historical EMP-1.1 result.

**Next gate after freeze:** implementation-level N-R4B conformance, followed by the separately controlled pilot/confirmatory data-generation gate before any learner fitting.
