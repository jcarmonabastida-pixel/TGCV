# N-R8.2 — Operationalisation Specification v0.1

**Status:** PROPOSED — NOT FROZEN
**Date:** 2026-09-05
**Parent:** N-R8.1 Robustness & Mechanism Discrimination Specification v0.1
**Clarification:** N-R8.2.1 resolves and is incorporated into this parent specification; where the earlier draft wording differed, the reconciled definitions below are normative for N-R8.3.

## 1. Purpose and gate position

This document converts N-R8.1 into executable operational definitions. It is still **PROPOSED**. No N-R8 execution is authorized until N-R8.1 and N-R8.2 are reviewed, implemented, conformance-tested, and frozen.

No N-R7 artifact or result is regenerated or modified.

## 2. Immutable inherited objects

N-R8 reuses without modification:

- Branch N semantic state and transformation definitions from N-R1.2;
- N-R3 R semantics (58 features) for the primary R representation;
- N-R4B.2 trajectory/outcome semantics;
- N-R4B.4 controlled corpus as the G1 reference corpus;
- N-R5.1 v0.2 semantic state hashing;
- N-R6 learner configuration and statistical conventions unless explicitly superseded below;
- N-R7 claim boundary.

Any change to an inherited object creates a new specification and is not an N-R8 operational parameter.

## 3. Common state and baseline definitions

For every initial state S:

`B(S) = [n_components, q1, q2, q3, one_hot(objective)]`, dimension 16.

`R1(S)` is the frozen 58-dimensional N-R3 representation of `T_acc(S)`.

`BR1(S) = B(S) || R1(S)`, dimension 74.

The outcome Y is generated only by the frozen N-R4B trajectory mechanism after the initial snapshot has been constructed. Y is never used to construct, select, match, filter, or rank predictor states.

## 4. N-R8-A — G2 generator distribution

### 4.1 Objective

Test whether the N-R7 predictive signal persists under a materially different state-generation distribution while retaining identical Branch N transformation and outcome semantics.

### 4.2 G1 reference

G1 is exactly the N-R4A generator:

- `n_components ~ Uniform{3,4,5}`;
- component subset sampled from the six-component universe;
- number of possible directed edges `m = n(n-1)`;
- `n_edges ~ Uniform{0,...,m}`;
- distinct directed edges sampled uniformly;
- each resource independently uniform on `{0,1,2,3}`;
- objective uniform on `{O01,...,O12}`;
- canonicalization applied before emission.

### 4.3 G2

G2 is defined prospectively as follows:

- `n_components` distribution: `{3: 0.10, 4: 0.30, 5: 0.60}`;
- conditional on n components, edge density `d = n_edges/m` is sampled from a discrete mixture:
  - probability 0.50: `d = 0.20` rounded to an admissible integer edge count;
  - probability 0.30: `d = 0.50` rounded to an admissible integer edge count;
  - probability 0.20: `d = 0.80` rounded to an admissible integer edge count;
- directed edges are then sampled uniformly without replacement at the selected edge count;
- resources are sampled independently with probabilities `{0:0.10, 1:0.20, 2:0.30, 3:0.40}`;
- objective is sampled with probabilities `{O01..O06:0.10 each, O07..O12:0.0666666666666667 each}`;
- the component subset is sampled uniformly among subsets of the selected cardinality;
- canonicalization is identical to G1.

For edge-density rounding, `n_edges = round_half_up(d*m)` and is clipped only to `[0,m]`; the exact integer rule must be implemented deterministically and recorded.

G2 must use an independent seed from all G1/N-R4A generation seeds. Proposed seed: `5_100_000`.

### 4.4 G2 evaluation

Generate 30,000 G2 training snapshots and 10,000 G2 test snapshots. Generate trajectories/outcomes with the frozen N-R4B mechanism using trajectory seed `dataset_seed + episode_id`.

The same predictor representation R1 and the frozen primary learner are evaluated on G2. The G1 N-R7 result is not recomputed; it remains the reference result.

Primary G2 comparison:

`logloss(B+R1) - logloss(B)`.

The sign convention is identical to N-R7: positive delta means improvement in log loss.

## 5. N-R8-B — matched T_acc intervention

### 5.1 Objective

Test whether differences in accessible-transformation structure can predict different outcomes when the baseline representation is held exactly fixed.

### 5.2 Matching unit

A matched pair consists of two independently constructed initial states A and B satisfying:

`B(A) = B(B)` exactly,

and

`T_acc(A) != T_acc(B)`.

Matching is performed before trajectory generation and without observing Y, predictions, losses, or any N-R8 result.

### 5.3 Construction

For each pair:

1. Sample one baseline tuple B from the admissible Branch N baseline space.
2. Construct two distinct canonical initial states with exactly that same B.
3. Require distinct accessible-transformation structures.
4. Reject pairs violating Branch N invariants.
5. Generate trajectories independently from the two states using independently derived deterministic episode seeds.

The pair generator may search over candidate states until the structural condition is satisfied, but search must use only initial-state information and frozen transformation semantics.

Proposed pair seed: `5_200_000`.

### 5.4 Outcome comparison

For each pair, compute Y_A and Y_B. The primary descriptive quantity is the paired outcome difference `Y_A - Y_B`.

A secondary predictive analysis compares:

`P(Y | B,R1)` across the two matched states.

Because B is identical within pair, any systematic prediction difference is attributable to R1 rather than to B as encoded in N-R5.1.

This is an intervention-style synthetic test. It does not establish real-world causality.

## 6. N-R8-C — structural-confounding attack

### 6.1 Objective

Test whether the N-R7 signal survives when low-order structural summaries are matched exactly while higher-order organization of T_acc differs.

### 6.2 Matching constraints

A valid pair must satisfy exact equality for:

- B (all 16 baseline variables);
- R1 family availability R1;
- R2 family cardinality R2;
- R3 component-incidence features;
- total number of accessible transformations `|T_acc|`;
- total number of accessible transformation families;
- component count;
- graph edge count;
- resource tuple;
- objective.

The pair must nevertheless satisfy:

`R1(A) != R1(B)`.

This deliberately creates a high-order structural contrast while controlling the low-order summaries already identified as plausible confounders.

### 6.3 Pair generation

Pairs are generated from initial states only. No outcome, trajectory, learner prediction, N-R7 result, or post-state information may be used.

Proposed seed: `5_300_000`.

Target: 5,000 valid pairs, with deterministic candidate search and fail-closed rejection if the target cannot be reached under the frozen search budget.

### 6.4 Interpretation

If predictive/outcome differences persist, simple cardinality and incidence explanations are weakened. If they disappear, H1-N must be narrowed accordingly.

## 7. N-R8-D — independent representation R2

### 7.1 Objective

Test whether predictive information persists under a semantically equivalent but independently specified representation of T_acc.

### 7.2 R2 definition

R2 is a fixed 24-dimensional structural summary of the canonical accessible-transformation set.

For each state, enumerate canonical transformations in frozen transformation order. For every transformation τ, compute:

- family id `f(τ)`;
- canonical source component set `src(τ)`;
- canonical target component set `dst(τ)` where applicable;
- successor-state structural delta `Δτ` relative to S.

The transformation-incidence mapping is frozen as follows:

| Transformation | `src(τ)` | `dst(τ)` |
|---|---|---|
| `ADD_COMPONENT(v)` | `∅` | `{v}` |
| `REMOVE_COMPONENT(v)` | `{v}` | `∅` |
| `ADD_EDGE(u,v)` | `{u}` | `{v}` |
| `REMOVE_EDGE(u,v)` | `{u}` | `{v}` |
| `REWIRE_EDGE(u,v,w)` | `{u}` | `{w}` |
| `MODIFY_RESOURCE(i,d)` | `∅` | `∅` |

For `REWIRE_EDGE(u,v,w)`, `v` is the removed edge target and is not included in `dst`; the resulting relation is from `u` to `w`.

`MODIFY_RESOURCE(i,d)` is restricted to `d ∈ {-1,+1}` and is accessible only when the resulting resource remains in `{0,1,2,3}`. No arbitrary resource jumps are represented.

R2 consists of the following deterministic statistics, in this exact order:

1. total `|T_acc|`;
2. number of non-empty families;
3. Shannon entropy of family proportions, using natural logarithm;
4. Herfindahl concentration of family proportions;
5. mean number of source components;
6. mean number of target components;
7. mean absolute resource delta;
8. mean component-count delta `ΔV`;
9. mean edge-count delta `ΔE`;
10. mean positive edge-count change `max(ΔE,0)`;
11. mean edge-count decrease `-min(ΔE,0)`;
12. fraction of transformations in `ADD_COMPONENT`;
13. fraction of transformations in `REMOVE_COMPONENT`;
14. fraction of transformations in `MODIFY_RESOURCE`;
15. fraction of edge-transform families (`ADD_EDGE`, `REMOVE_EDGE`, `REWIRE_EDGE`);
16. fraction of component-transform families (`ADD_COMPONENT`, `REMOVE_COMPONENT`);
17. fraction preserving component count;
18. fraction preserving edge count;
19. fraction modifying resources;
20. fraction modifying edges;
21. mean Jaccard similarity between original and successor component sets;
22. mean Jaccard similarity between original and successor edge sets;
23. population standard deviation of successor edge-count change;
24. population standard deviation of successor component-count change.

This exact 24-feature order supersedes the earlier draft ordering in this document. The clarification is incorporated here rather than treated as a parallel specification.

All statistics are computed from the initial state's accessible transformations and their deterministic successors only. No trajectory is executed to compute R2. No Y, terminal state, or post-snapshot field enters R2.

Empty `T_acc` handling is frozen as follows: all 24 R2 features are exactly `0.0`.

Jaccard similarity is defined as `|A∩B|/|A∪B|`, with value `1.0` when both sets are empty. Standard deviations are population standard deviations. Floating-point computation must use deterministic IEEE-754 double precision and a single documented implementation. Canonical serialization of R2 must use JSON sorted keys, compact separators, UTF-8, ASCII-safe output, and no trailing newline when hashing artifacts.

### 7.3 R2 evaluation

R2 is evaluated as a separate predictor family against the same B and outcomes:

`P(Y | B,R2)` versus `P(Y | B)`.

R2 is not selected, transformed, or reduced after seeing results.

## 8. Statistical hierarchy

N-R8 is divided into:

### Confirmatory tier

- **C1:** G2 primary predictive comparison using B+R1 vs B.
- **C2:** matched T_acc intervention paired outcome comparison.
- **C3:** structural-confounding matched comparison.
- **C4:** R2 semantic-representation predictive comparison.

### Exploratory tier

Feature-level attribution, subgroup analyses, alternative learners, and additional descriptive analyses are exploratory only and cannot modify the confirmatory claim.

### Alpha

Family-wise confirmatory alpha is proposed as `0.05`, using Holm correction across C1–C4 for inferential p-values. Practical significance must be assessed separately using the same minimum practical delta used in N-R7 unless N-R8.3 freezes a justified alternative before execution.

No N-R8 result may be used to choose the correction method or threshold.

## 9. Reproducibility and seeds

Proposed seeds:

| Object | Seed |
|---|---:|
| G2 train/test generation | 5,100,000 |
| N-R8-B matched pairs | 5,200,000 |
| N-R8-C structural pairs | 5,300,000 |
| R2 evaluation corpus | inherited G2 corpus unless a separate corpus is explicitly frozen |
| sign-flip inference | 13,579 inherited unless a distinct paired test requires a separate frozen seed |

Each independently generated corpus must use a fresh deterministic RNG instance. No global ambient RNG state is permitted.

## 10. Required artifact schemas

Every generated state corpus must preserve the N-R4B-compatible canonical state fields:

`components`, `edges`, `resources`, `objective`.

Every predictor row must contain:

`episode_id`, `initial_snapshot_sha256`, predictor vector(s).

Every outcome row must contain the exact join key and Y plus the minimum provenance fields required by N-R4B.4.

All joins must be one-to-one and exact on `(episode_id, initial_snapshot_sha256)`.

## 11. Fail-closed conditions

Execution must abort before fitting if any of the following occurs:

- frozen input hash mismatch;
- schema mismatch;
- predictor dimension mismatch;
- duplicate join key;
- missing join key;
- semantic state hash mismatch;
- outcome leakage into predictors;
- non-deterministic pair generation;
- matching condition violated;
- R2 non-finite value;
- R2 implementation hash mismatch;
- result-dependent filtering detected.

## 12. Required conformance tests

Before corpus generation, implementation must demonstrate:

1. G2 deterministic regeneration;
2. G2 differs from G1 according to frozen distribution tests;
3. exact B matching for N-R8-B;
4. exact T_acc inequality for N-R8-B;
5. exact low-order matching for N-R8-C;
6. exact R1 inequality for N-R8-C;
7. R2 dimension = 24;
8. R2 empty-T_acc all-zero rule;
9. R2 byte determinism;
10. R2 no Y/trajectory dependency;
11. predictor/outcome separation;
12. one-to-one join integrity;
13. seed separation;
14. no N-R7 result literals or artifact reads in generation code;
15. no learner invocation during corpus construction;
16. complete provenance and artifact hashes.

## 13. Execution status

**BLOCKED.** This document authorizes implementation/conformance work only.

Required next gates:

- N-R8.3 implementation and conformance;
- N-R8.4 corpus construction and integrity freeze;
- N-R8.5 execution authorization.

**Decision:** N-R8.2 OPERATIONALISATION PROPOSED; SCIENTIFIC EXECUTION NOT AUTHORIZED.
