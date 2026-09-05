# N-R4A — Controlled Snapshot Generation Specification v0.1

**Program:** TGCV  
**Experiment:** EMP-1.1  
**Branch:** N — Controlled New Reconstruction  
**Status:** PROPOSED FOR PROSPECTIVE FREEZE  
**Date:** 2026-09-05

## 1. Purpose

N-R4A defines the controlled generation/reconstruction boundary for Branch N input snapshots before any learner fitting or confirmatory scientific execution.

This is a prospective reconstruction specification. It is **not** a recovery of the historical EMP-1.1 data generator.

## 2. Source-of-truth hierarchy

1. Frozen EMP-1.1 protocol parameters.
2. N-R1.2 Branch N transformation-system specification.
3. N-R1.3 v0.2 R encoding specification.
4. N-R2/N-R3 conformance-verified implementation.
5. Explicit Branch N reconstruction rules introduced by this specification.

Historical EMP-1.1 results are never an input to generation.

## 3. Snapshot schema

Each generated observation contains exactly the pre-outcome snapshot fields:

`episode_id, components, edges, resources, objective`

where:

- `components` are a non-empty subset of `A1..C2`, with size 3–5 for generated initial snapshots;
- `edges` form a simple directed graph over active components;
- `resources` contain exactly three integers in `{0,1,2,3}`;
- `objective` is one opaque label `O01..O12`.

The canonical Branch N `State` representation is the sole internal representation used to compute `T_acc` and `R`.

## 4. Initial-state generation

The generator must be deterministic under a recorded integer seed and must use a single explicit pseudo-random generator instance per dataset split.

For each episode:

1. draw component count uniformly from `{3,4,5}`;
2. sample that many distinct components uniformly without replacement from the six-component universe;
3. enumerate all possible directed non-self edges over the sampled components in canonical order;
4. draw the number of initial edges uniformly from `0..m`, where `m=n(n-1)`;
5. sample that many distinct edges uniformly without replacement;
6. draw each of the three resources independently and uniformly from `{0,1,2,3}`;
7. draw objective uniformly from `O01..O12`;
8. canonicalize the resulting state through the verified `State.make` representation.

These are **RECONSTRUCTED Branch N rules**, not historical generator claims.

## 5. Required dataset splits

The frozen EMP-1.1 protocol specifies:

- training episodes: `30,000`, seed `3,100,000`;
- locked test episodes: `10,000`, seed `4,100,000`.

N-R4A generation must preserve these counts and seeds. The test split must be generated independently from the training split and must not be used for any generation-rule selection.

The 20,000-episode pilot generation procedure remains OPEN because its historical implementation was not recovered. It must not be silently substituted with the confirmatory split.

## 6. Per-snapshot reconstruction

For each generated snapshot:

1. validate state invariants;
2. enumerate `T_acc` using the conformance-verified Branch N transformation universe;
3. encode `R` using the conformance-verified 58-feature encoder;
4. compute and record provenance metadata;
5. do not generate or attach future trajectory/outcome information in the snapshot artifact itself.

The reconstruction function must be pure with respect to the snapshot: same canonical snapshot plus same frozen implementation produces the same `T_acc` and `R`.

## 7. Provenance record

Every generated dataset artifact must record:

- generator specification identifier/version;
- generator implementation identifier and SHA-256;
- dataset split;
- seed;
- episode count;
- Branch N specification identifiers;
- implementation SHA-256;
- Python/runtime version;
- generation timestamp;
- output file SHA-256;
- schema version.

Generation timestamp is provenance metadata only and must not enter the scientific feature vector.

## 8. Sealing and reproducibility

Before scientific execution:

- generated files must be immutable/sealed by hash;
- generation must be repeated from the same specification and seed in a clean execution;
- byte-identical output is required for the deterministic snapshot corpus;
- any mismatch is FAIL/BLOCKED;
- no manual editing is permitted after generation;
- no live external registry, network state, ambient cache, or future data may enter generation.

## 9. Leakage boundary

The following are prohibited inputs to snapshot generation or R construction:

- future states;
- future transformations actually taken;
- downstream success;
- target/outcome labels;
- test-set performance;
- historical EMP-1.1 result values;
- learner predictions;
- any post-snapshot information.

Objective identity is allowed in the baseline `B`, but `R` must remain objective-exogenous as established by N-R3.

## 10. Scientific boundary

N-R4A does **not** define or validate the outcome process, transition dynamics after the snapshot, learner configuration, or confirmatory estimand beyond the already frozen EMP-1.1 protocol.

Consequently, passing N-R4A alone does not authorize model fitting or scientific claims.

## 11. Gate acceptance criteria

N-R4A can close only after a conformance runner demonstrates:

1. exact schema compliance;
2. component-count bounds 3–5;
3. component-universe compliance;
4. resource-domain compliance;
5. objective-domain compliance;
6. graph validity;
7. deterministic same-seed generation;
8. seed separation between train/test;
9. deterministic `S → T_acc → R` reconstruction;
10. recorded implementation/specification hashes;
11. byte-identical repeated corpus generation;
12. no scientific learner execution.

### Next gate

**N-R4B — Controlled Outcome/Trajectory Generation Specification.**

N-R4B must separately establish the prospective transition/outcome process required to construct the supervised scientific target. It must not be inferred from the historical numerical result.
