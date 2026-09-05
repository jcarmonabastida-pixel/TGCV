# N-R8.4 — Controlled Corpus Construction and Integrity Freeze Specification v0.1

**Status:** PROPOSED — NOT FROZEN  
**Date:** 2026-09-05  
**Parent:** N-R8.3 Conformance Gate Result v0.1

## 1. Purpose and gate position

N-R8.4 defines the construction, validation, provenance, and integrity-freeze requirements for the prospective corpora required by N-R8.

This specification authorizes **construction and conformance work only**. It does not authorize N-R8 scientific execution. Scientific execution remains blocked until N-R8.4 is PASS/CLOSED and N-R8.5 explicitly authorizes execution.

No N-R7 artifact or result may be regenerated, modified, tuned against, or substituted.

## 2. Immutable inherited objects

N-R8.4 reuses without modification:

- Branch N state and transformation semantics from N-R1.2;
- N-R3 R1 representation (58 dimensions);
- N-R4A G1 generator as the reference distribution;
- N-R4B.2 trajectory/outcome mechanism;
- N-R4B.4 controlled-corpus serialization and outcome semantics;
- N-R5.1 v0.2 semantic state hashing;
- N-R6 learner/statistical conventions where later execution requires them;
- reconciled N-R8.2 operationalisation, including integrated N-R8.2.1 R2 semantics;
- N-R8.3 conformance-validated implementation.

Any change to an inherited object requires a new specification and invalidates the corresponding downstream freeze.

## 3. Corpus architecture

N-R8.4 consists of four logically separate prospective objects:

1. **G2 state corpus** — training and test initial states generated from the frozen G2 distribution;
2. **N-R8-B matched-pair corpus** — pairs with exactly equal B and unequal `T_acc`;
3. **N-R8-C structural-confounding pair corpus** — pairs matched on all specified low-order structural controls while having unequal R1;
4. **R2 predictor corpus** — R2 vectors deterministically derived from initial states, using the frozen N-R8.3 implementation.

Where the same G2 initial states are reused for R1 and R2, the state corpus is generated once and referenced by immutable hash. R2 is never used to alter state selection.

Each object must have independent provenance and a complete manifest of source specifications, implementation hashes, seeds, counts, schemas, and output SHA-256 hashes.

## 4. G2 state corpus

### 4.1 Required sizes

- Training: **30,000** initial snapshots.
- Test: **10,000** initial snapshots.

### 4.2 Generator

Use the reconciled N-R8.2 G2 generator:

- component count probabilities `{3:0.10, 4:0.30, 5:0.60}`;
- edge-density mixture `{0.20:0.50, 0.50:0.30, 0.80:0.20}`;
- deterministic round-half-up edge-count rule;
- uniform sampling of distinct directed edges at the selected count;
- resource probabilities `{0:0.10, 1:0.20, 2:0.30, 3:0.40}`;
- objective probabilities `O01..O06 = 0.10` each and `O07..O12 = 1/15` each;
- uniform component-subset sampling conditional on component count;
- canonicalization before emission.

Seed: **5,100,000**. Training and test are generated as deterministic, non-overlapping streams derived from this frozen seed under the frozen generator implementation; the exact derivation rule must be recorded in the implementation/provenance and verified by the integrity runner.

### 4.3 State-only requirements

Every snapshot must contain exactly the N-R4B-compatible semantic state fields:

`components`, `edges`, `resources`, `objective`.

`episode_id` is permitted only in trajectory/predictor records and must not enter semantic state hashing.

Semantic state hash is the N-R5.1 v0.2 hash of the state-only object:

`{"components":...,"edges":...,"objective":...,"resources":...}`

with sorted keys, compact separators, ASCII-safe JSON, UTF-8, and no trailing newline.

## 5. N-R8-B matched-pair corpus

### 5.1 Required condition

Every pair `(A,B)` must satisfy:

`B(A) = B(B)` exactly;

`T_acc(A) != T_acc(B)` exactly.

The equality and inequality are evaluated from the frozen initial-state and transformation semantics, before trajectory generation.

### 5.2 Construction constraints

- Pair seed: **5,200,000**.
- Pair generation uses only initial-state information.
- No Y, trajectory, learner prediction, loss, N-R7 result, or N-R8 result may be observed.
- Candidate search is deterministic.
- A pair is emitted only after both conditions and all Branch N invariants pass.
- The exact pair-generation search budget and exhaustion/fail-closed rule must be frozen before construction.

### 5.3 Required provenance

For each pair retain:

- pair_id;
- canonical state A and state B or immutable references to them;
- semantic state hashes;
- B representation for both states;
- R1 hashes/representations sufficient to verify `T_acc` inequality;
- generator seed and deterministic candidate-search metadata;
- implementation/specification hashes.

No outcome field is permitted in the pair-generation artifact.

## 6. N-R8-C structural-confounding corpus

### 6.1 Required condition

Every pair `(A,B)` must satisfy exact equality for:

- B (16 dimensions);
- R1 family availability;
- R2 family cardinality;
- R3 component-incidence features;
- `|T_acc|`;
- number of accessible transformation families;
- component count;
- edge count;
- resource tuple;
- objective.

And simultaneously:

`R1(A) != R1(B)`.

### 6.2 Construction

- Pair seed: **5,300,000**.
- Target: **5,000 valid pairs**.
- Pair search is deterministic and uses initial-state information only.
- No outcome, trajectory, learner prediction, loss, N-R7 result, or N-R8 result may be used.
- If the frozen search budget cannot produce 5,000 valid pairs, construction must fail closed and no partial corpus may be promoted to frozen status.

### 6.3 Verification

The integrity runner must recompute all equality constraints independently from the emitted states and verify R1 inequality independently. Self-reported match flags are insufficient.

## 7. R2 corpus construction

R2 is computed from each initial state using the conformance-validated N-R8.3 implementation.

Required properties:

- exactly 24 dimensions;
- exact N-R8.2 feature order;
- empty `T_acc` produces 24 zero values;
- finite IEEE-754 double values only;
- deterministic byte representation;
- no learner, outcome, trajectory, post-state, or N-R7 artifact dependency.

The R2 artifact must preserve `episode_id` and `initial_snapshot_sha256` as the join key, but `episode_id` must not enter the semantic state hash.

## 8. Trajectory/outcome generation

After initial-state corpus construction and integrity checks, trajectories/outcomes may be generated using the frozen N-R4B.2 mechanism.

Trajectory generation is a downstream operation and must not influence state construction, matching, R1/R2 computation, or pair selection.

For each generated outcome record:

- preserve the exact `(episode_id, initial_snapshot_sha256)` join key;
- preserve the minimum N-R4B.4 provenance fields;
- retain binary Y exactly as generated;
- verify one-to-one join integrity.

Outcome artifacts must remain physically/logically separate from predictor-construction artifacts until the join stage defined by the later execution specification.

## 9. Predictor construction and separation

Predictor artifacts must be constructed from initial states only:

- B from the initial snapshot;
- R1 from `T_acc` of the initial snapshot;
- R2 from the initial snapshot via the frozen N-R8.3 implementation.

No predictor row may contain:

- Y;
- trajectory steps;
- terminal state;
- terminal reason;
- future releases or post-snapshot information;
- learner predictions or losses;
- N-R7 or N-R8 result literals;
- fields derived from outcome generation.

The integrity runner must perform an explicit dependency/firewall scan in addition to schema checks.

## 10. Determinism and seed separation

Every independent generation process must instantiate a fresh deterministic RNG from its frozen seed.

The following seeds are reserved:

| Object | Seed |
|---|---:|
| G2 state generation | 5,100,000 |
| N-R8-B pair generation | 5,200,000 |
| N-R8-C pair generation | 5,300,000 |
| Sign-flip inference | 13,579 unless explicitly superseded before execution |

No ambient/global RNG state may affect corpus construction.

A deterministic regeneration test must reproduce byte-identical artifacts before freeze.

## 11. Integrity checks required before freeze

N-R8.4 may be declared PASS/CLOSED only if all applicable checks pass:

1. frozen specification hashes verified;
2. N-R8.3 implementation hash verified;
3. G2 train/test counts exact;
4. G2 schemas exact;
5. semantic state hashes recomputed and exact;
6. train/test episode IDs unique and complete where applicable;
7. G2 deterministic regeneration byte-identical;
8. G2 distribution properties conform to frozen probabilities/rules;
9. N-R8-B matching conditions independently verified for every pair;
10. N-R8-B deterministic regeneration verified;
11. N-R8-C all low-order equality constraints independently verified;
12. N-R8-C R1 inequality independently verified;
13. N-R8-C target pair count exactly 5,000;
14. N-R8-C deterministic regeneration verified;
15. R2 dimension/order/value rules verified;
16. R2 byte determinism verified;
17. no outcome/trajectory/learner dependency in predictor construction;
18. no N-R7 result/artifact dependency;
19. one-to-one join integrity for downstream outcome records;
20. seed separation verified;
21. complete provenance manifests present;
22. SHA-256 hashes of all frozen artifacts recorded;
23. no partial or failed construction artifact promoted to frozen status.

Any failed check is blocking.

## 12. Freeze artifacts

The N-R8.4 freeze package must contain, at minimum:

- G2 train snapshots;
- G2 test snapshots;
- N-R8-B matched pairs;
- N-R8-C matched pairs;
- R2 predictor artifacts, if separately emitted;
- trajectory/outcome artifacts required for the later execution stage;
- a master manifest;
- per-artifact SHA-256 hashes;
- complete provenance records;
- integrity/conformance execution report;
- exact implementation and specification hashes.

Historical, superseded, aborted, or failed artifacts must be retained separately and clearly marked; they must not be silently overwritten.

## 13. Fail-closed rules

Construction must abort and the corpus must not be frozen if any of the following occurs:

- hash mismatch;
- schema mismatch;
- duplicate semantic state hash where uniqueness is required;
- duplicate join key;
- missing join key;
- state-hash mismatch;
- matching-condition violation;
- insufficient N-R8-C pairs within the frozen search budget;
- non-deterministic regeneration;
- non-finite R2;
- implementation/specification hash mismatch;
- dependency on outcomes, trajectories, learner results, or historical N-R7 artifacts;
- result-dependent filtering or selection;
- incomplete provenance.

## 14. Status and next gate

**Status:** PROPOSED — NOT FROZEN.

N-R8.4 becomes PASS/CLOSED only after the construction implementation and integrity runner have been independently conformance-tested and the complete corpus has been generated and verified.

The next gate after N-R8.4 is **N-R8.5 — Scientific Execution Authorization**.

**Decision:** N-R8.4 CORPUS CONSTRUCTION SPECIFICATION PROPOSED; SCIENTIFIC EXECUTION REMAINS BLOCKED.
