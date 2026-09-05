# N-R8-C2 vNext — Prospective 5,000-Pair Corpus Generation Contract v0.1

**Status:** FROZEN — GENERATION NOT PERFORMED

## 1. Purpose

This document freezes the prospective corpus-generation contract following the successful N-R8-C2 vNext bounded identifiability result and deterministic C1–C9 smoke conformance gate.

It is an execution contract, not a scientific result. It authorises implementation of a deterministic corpus generator, but **does not authorise its execution in this step** and does not authorise scientific execution of EXT-1.1.

## 2. Frozen inputs

The generator must use, without modification:

1. `branch_n_r8_operationalisation_v01.py` — authoritative Branch N operationalisation.
2. `branch_n_r8c2_vnext_key_v01.py` — frozen key `K_C2_vNext = B + degree-multiset(V)`.
3. `probe_n_r8c2_vnext_identifiability_v01.py` — authoritative `O_T` construction/observable.
4. `N-R8-C2_vNEXT_FREEZE_v0.1.md`.
5. `N-R8-C2_vNEXT_IDENTIFIABILITY_RESULT_v0.1.md`.
6. `N-R8-C2_vNEXT_CORPUS_CONFORMANCE_GATE_v0.1.md` — smoke gate PASS.
7. EMP-1.1 frozen experimental protocol.

Any change to these scientific inputs requires a new versioned audit/freeze and invalidates this contract.

## 3. Corpus target

- Target: **5,000 matched pairs**.
- Each pair consists of two canonical states `(A,B)`.
- Required pair condition: `K_C2_vNext(A) == K_C2_vNext(B)` and `O_T(A) != O_T(B)`.
- The corpus is prospective/derived/reconstructed. It must not be represented as historical observations.

## 4. Sampling space

The default generation space is the bounded Branch N state space used for the frozen witness family, generalized only within the already-authorised Branch N state representation.

The generator must construct states exclusively through the authoritative `canonical_state(...)` interface and must obey all authoritative state invariants.

No state may enter the corpus if it contains:

- duplicate edges;
- self-loops;
- absent edge endpoints;
- invalid resource values;
- invalid objective values;
- non-canonical component/edge ordering.

The generator must not inspect the Rust dataset during corpus construction.

## 5. Result-blind pair construction

Pair construction is a two-stage process:

### Stage A — key-only candidate generation

1. Generate or enumerate candidate canonical states using only the frozen state representation and deterministic configuration.
2. Compute `K_C2_vNext` for each candidate.
3. Bucket candidates by exact key equality.
4. Construct candidate pairs only within equal-key buckets.

`O_T` must not be used for state generation, candidate weighting, bucket formation, seed adaptation, or any other sampling decision.

### Stage B — post hoc target acceptance

For each equal-key candidate pair, compute `O_T(A)` and `O_T(B)` only after key equality has been established.

Accept the pair iff:

`O_T(A) != O_T(B)`.

Rejected equal-key/equal-`O_T` pairs may be recorded in generation diagnostics but must not be represented as accepted corpus pairs.

No sampling parameter may be changed in response to observed `O_T` values.

## 6. Determinism

The generation configuration must include a single explicit integer seed recorded in the run manifest.

Given identical:

- source commit;
- generator version;
- frozen scientific-input SHAs;
- configuration;
- seed;
- runtime-relevant generation parameters;

the accepted pair sequence, canonical state serialisations, and SHA-256 hashes must be byte-for-byte reproducible.

The generator must fail closed if required frozen inputs cannot be resolved or if their recorded hashes differ from the expected manifest.

## 7. Pair identity and deduplication

Each state is identified by its canonical SHA-256 digest.

Each accepted pair must have a deterministic pair identifier derived from the ordered canonical state hashes. The generator must define and apply one fixed pair ordering rule before hashing.

The accepted corpus must contain no duplicate pair identifiers.

The same unordered pair must not appear twice under reversed ordering.

## 8. Corpus output schema

The generated corpus must provide, at minimum, one machine-readable record per accepted pair containing:

- `pair_id`;
- `state_a` canonical representation;
- `state_b` canonical representation;
- `state_a_sha256`;
- `state_b_sha256`;
- `key_sha256` or canonical serialisation of `K_C2_vNext`;
- `o_t_a` canonical signature;
- `o_t_b` canonical signature;
- `provenance_class` = `DERIVED_RECONSTRUCTED`;
- generator version;
- source/input manifest identifier.

A separate run manifest must contain:

- corpus contract version;
- generator version;
- seed;
- target pair count;
- accepted pair count;
- candidate pair count;
- rejected equal-key/equal-`O_T` count;
- all frozen input SHAs;
- generator SHA;
- deterministic rerun result;
- start/end execution metadata;
- final corpus SHA-256;
- final manifest SHA-256;
- execution status.

## 9. Provenance and scientific boundary

The corpus is a constructed experimental instrument. It is **not historical data** and must be labelled `DERIVED_RECONSTRUCTED` throughout the repository.

The corpus generator must not:

- consume or transform the Rust dataset;
- train a model;
- evaluate the primary LogLoss estimand;
- run the confirmatory EXT-1.1 experiment;
- alter N-R7;
- alter the frozen key or `O_T`.

## 10. Fail-closed rules

Generation must terminate without producing an accepted corpus if any of the following occurs:

1. Frozen-input SHA mismatch.
2. Canonical-state invariant failure.
3. Key equality failure for a proposed pair.
4. Target inequality cannot be established.
5. Determinism check fails.
6. Duplicate pair identity detected.
7. Provenance classification is missing or invalid.
8. Runtime/import/infrastructure failure.
9. Any attempt is detected to use `O_T` before key equality during candidate construction.

A failure must produce a machine-readable status and must not be silently repaired by changing the frozen contract.

## 11. Execution boundary

**This contract freezes preparation only. The 5,000-pair corpus is NOT generated by this commit.**

Before execution, the generator implementation must itself pass a dedicated preflight against this contract, including:

- schema validation;
- frozen-input SHA validation;
- deterministic seed/configuration validation;
- result-blind static inspection;
- small dry-run without corpus acceptance;
- reproducibility check.

Only after that preflight passes should the explicit corpus-generation command be run.

## 12. Status

**FROZEN — READY FOR GENERATOR IMPLEMENTATION / PREFLIGHT**

Scientific execution remains **NOT PERFORMED**.
