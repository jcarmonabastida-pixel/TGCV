# N-R4B.1 — Outcome Semantic Resolution v0.1

**Status:** PROPOSED FOR PROSPECTIVE FREEZE  
**Branch:** N — Controlled New Reconstruction  
**Date:** 2026-09-05  
**Parent:** N-R4B v0.1

## 1. Purpose

N-R4B.1 resolves the previously open semantic choices required before implementation of the Branch N outcome/trajectory generator.

This document is a **prospective reconstruction decision record**. It does not recover the historical EMP-1.1/MVE-1.0 generator.

The recovered constraints that must be preserved are: six potential components `A1..C2`, three discrete resources, twelve objectives, horizon `H=6`, and stochastic execution independent of objective. The exact historical objective predicates and trajectory policy were not recovered. They are therefore not presented as historical facts. memcite

## 2. Objective codebook

The twelve objective labels remain `O01..O12`.

For Branch N, the objective codebook is fixed prospectively as follows.

### Component-presence objectives

- `O01`: `A1 ∈ V`
- `O02`: `A2 ∈ V`
- `O03`: `B1 ∈ V`
- `O04`: `B2 ∈ V`
- `O05`: `C1 ∈ V`
- `O06`: `C2 ∈ V`

### Resource-maximisation objectives

- `O07`: `q_1 = 3`
- `O08`: `q_2 = 3`
- `O09`: `q_3 = 3`

### Resource-minimisation objectives

- `O10`: `q_1 = 0`
- `O11`: `q_2 = 0`
- `O12`: `q_3 = 0`

The predicates are deterministic, mutually interpretable, and depend only on the current state and registered objective. No predicate uses edges as a hidden outcome channel, future states, trajectory history, learner output, or recorded EMP-1.1 results.

These twelve mappings are **RECONSTRUCTED / PROSPECTIVE**, not historical.

## 3. Why this codebook is fixed before execution

The codebook is deliberately chosen from the already frozen state vocabulary:

- six named components;
- three named resource coordinates;
- four discrete resource values.

No new latent variable is introduced. No objective predicate is selected using the historical result, pilot prevalence, test performance, or expected effect size.

The codebook is therefore a pre-registered Branch N modeling choice. Its purpose is operational completeness, not historical recovery.

## 4. Trajectory RNG

Each episode receives one trajectory seed derived deterministically from the registered dataset seed and episode identifier:

`trajectory_seed = dataset_seed + episode_id`

where `episode_id` is the canonical zero-based integer assigned by N-R4A.

For each episode, a fresh `random.Random(trajectory_seed)` instance is created. No global RNG state is used.

Train and test therefore use disjoint seed ranges because their dataset seeds differ by `1,000,000`.

The trajectory RNG is used only for transformation selection. State generation remains governed by N-R4A.

## 5. Empty accessibility

If `T_acc(S_h) = ∅` and `G_o(S_h)=0`, trajectory generation terminates immediately with:

- terminal step = `h`;
- terminal reason = `NO_ACCESSIBLE_TRANSFORMATION`;
- outcome `Y=0`.

No artificial no-op transformation is introduced.

If `G_o(S_h)=1`, success is recorded before accessibility is evaluated.

## 6. Multiple transformations with identical successor states

The trajectory policy samples from the **transformation list**, not from the set of distinct successor states.

Therefore two distinct transformations that happen to produce the same canonical successor state remain two equally weighted selectable transformations.

This preserves the frozen transformation-universe semantics and avoids silently replacing the registered action space by a quotient over successor states.

The successor state itself is canonicalized after application.

## 7. Exact trajectory algorithm

For each episode:

1. initialize `S_0` from the sealed N-R4A snapshot;
2. initialize the episode RNG from `dataset_seed + episode_id`;
3. for `h = 0,...,H`:
   - evaluate `G_o(S_h)`;
   - if true, terminate with `Y=1`;
   - if `h = H`, terminate with `Y=0` and `HORIZON_EXHAUSTED`;
   - compute `T_acc(S_h)` using the frozen N-R1.2 semantics;
   - if empty, terminate with `Y=0` and `NO_ACCESSIBLE_TRANSFORMATION`;
   - otherwise sample one transformation uniformly from the canonical ordered transformation list;
   - apply it using the frozen Branch N transition function;
   - continue to `h+1`.

Thus at most six transformations are applied.

## 8. Objective-independent execution

The transformation-selection distribution is uniform over `T_acc(S_h)` and does **not** depend on `o_0`.

The objective affects only the success predicate `G_o(S_h)`.

Consequently, for a fixed state and accessible transformation set, changing the objective changes the evaluation of success but does not alter the transition-selection distribution.

## 9. Trajectory serialization

Trajectory records are serialized as canonical UTF-8 JSON with:

- sorted object keys;
- compact separators `(',', ':')`;
- ASCII-safe JSON encoding;
- one record per line;
- newline terminated output;
- deterministic list ordering.

Canonical record fields:

`episode_id, dataset_split, dataset_seed, trajectory_seed, initial_snapshot_sha256, objective, horizon, steps, terminal_step, terminal_reason, outcome`

`steps` is an ordered list of objects containing:

`step, state_sha256_before, transformation_id, state_sha256_after`

No predictor feature vector is stored inside the trajectory record.

## 10. State hashing

The state hash is SHA-256 over the canonical UTF-8 JSON representation of:

`components, edges, resources, objective`

with sorted keys and compact separators.

This hash is a provenance identifier only. It is not a learner feature and does not influence transition selection.

## 11. Predictor/outcome separation

The learner-side dataset contains only:

- the sealed initial snapshot;
- baseline `B` as defined by the frozen EMP-1.1 protocol;
- `R(S_0)` as defined by N-R1.3 v0.2.

The outcome-side dataset contains the trajectory and `Y`.

The join key is `episode_id` plus the initial snapshot hash. No trajectory field is permitted to enter `B` or `R`.

## 12. Required conformance fixtures

Before any pilot or confirmatory generation, the implementation runner must test at least:

1. success at `h=0`;
2. success after one or more transformations and before `H`;
3. failure after exactly `H` transitions;
4. failure caused by empty `T_acc` before `H`;
5. objective-independence of the transformation-selection distribution;
6. duplicate-successor transformations remain separately selectable;
7. same snapshot + same trajectory seed gives byte-identical trajectory;
8. changing only trajectory seed can change the sampled trajectory while leaving the initial snapshot unchanged;
9. no outcome field is consumed by predictor construction;
10. no learner is executed.

## 13. Provenance labels

- `H=6`: RECOVERED / SPECIFIED
- six components: RECOVERED / SPECIFIED
- three resources: RECOVERED / SPECIFIED
- twelve objectives: RECOVERED / SPECIFIED
- objective predicates: RECONSTRUCTED
- trajectory policy: RECONSTRUCTED
- trajectory seed derivation: RECONSTRUCTED
- empty-accessibility rule: RECONSTRUCTED
- duplicate-successor policy: RECONSTRUCTED
- trajectory serialization: RECONSTRUCTED
- outcome separation: DERIVED / SPECIFIED

## 14. Historical boundary

Nothing in this document may be cited as evidence that the historical EMP-1.1/MVE-1.0 generator used these objective predicates, seed derivation, uniform action policy, empty-accessibility rule, or serialization format.

The historical executable semantics remain unrecovered.

## 15. Freeze decision

N-R4B.1 is ready for **prospective freeze** subject to implementation conformance. No scientific corpus has been generated from these decisions and no historical result has been used as a tuning target.

The next action is implementation of the generator and an independent N-R4B conformance runner. The implementation must not begin learner fitting or full scientific execution.

**Scientific execution:** NOT PERFORMED.
