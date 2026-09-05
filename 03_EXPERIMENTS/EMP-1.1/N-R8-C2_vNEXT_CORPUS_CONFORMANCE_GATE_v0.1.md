# N-R8-C2 vNext — Corpus / Conformance Gate v0.1

**Status:** SPECIFIED — NOT YET EXECUTED

## 1. Purpose

This gate defines the controlled transition from the successful bounded identifiability result to prospective corpus construction. It is a conformance gate, not a scientific result and not the EXT-1.1 model execution.

The gate exists to ensure that the frozen C2-vNext key, the authoritative Branch N operationalisation, the transformation-organisation observable `O_T`, and the pair-construction procedure remain internally coherent before any 5,000-pair corpus is generated.

## 2. Preconditions

The following are already frozen or recorded and must not be altered by this gate:

1. `N-R8-C2_vNEXT_FREEZE_v0.1.md`.
2. `branch_n_r8c2_vnext_key_v01.py`.
3. `branch_n_r8_operationalisation_v01.py`.
4. `probe_n_r8c2_vnext_identifiability_v01.py`.
5. `N-R8-C2_vNEXT_IDENTIFIABILITY_RESULT_v0.1.md`.
6. EMP-1.1 frozen experimental protocol.

The bounded identifiability result is `IDENTIFIABLE / PASS`; corpus generation itself remains `NOT_PERFORMED`.

## 3. Conformance assertions

A conformance implementation must verify all of the following before accepting a corpus-generation run.

### C1 — Frozen-key conformance

For every candidate state:

`K_C2_vNext = B + degree-multiset(V)`

with:

`B = (|V|, q1, q2, q3, objective)`.

The key implementation must remain pure state-derived and must not call or inspect `tacc`, transformation enumeration/application, `R`, or `O_T`.

### C2 — State canonicalisation

Every generated state must pass the authoritative `canonical_state` validation. No duplicate edge, self-loop, absent endpoint, invalid resource, or invalid objective may enter the corpus.

### C3 — Pair equality

Every accepted pair `(A,B)` must satisfy:

`K_C2_vNext(A) == K_C2_vNext(B)`.

### C4 — Target inequality

Every accepted pair must satisfy:

`O_T(A) != O_T(B)`.

The target inequality is evaluated only after key equality has been established.

### C5 — Result-blind construction

Pair generation/bucketing may use only the frozen key. `O_T` may be used solely as the post hoc acceptance condition for a candidate equal-key pair. No generation parameter, sampling weight, seed, or key coordinate may be changed in response to observed `O_T` values.

### C6 — Determinism

Given identical source, configuration and seed, the generated corpus and all canonical state hashes must be byte-for-byte deterministic.

### C7 — Witness compatibility

The conformance implementation must be capable of representing the frozen four-component witness class used by the identifiability gate. This is a fixture adequacy check and must not be replaced by a new target-optimised fixture.

### C8 — Provenance separation

Generated corpus artifacts are `DERIVED` / `RECONSTRUCTED`, not `HISTORICAL`. The bounded identifiability result remains an immutable empirical record.

### C9 — No scientific execution

The conformance gate must not train models, consume the Rust dataset, evaluate the primary LogLoss estimand, or execute the confirmatory experiment.

## 4. Corpus construction boundary

Only after C1–C9 pass may the prospective matched-pair corpus be generated.

The intended corpus target remains **5,000 matched pairs**, but this document does not itself authorise execution of that generation. The generation command must be a separate explicit step after the conformance gate passes.

The conformance gate should first run on a small deterministic smoke corpus / fixture set. A passing smoke gate does not imply scientific validity; it only permits progression to the frozen corpus-generation stage.

## 5. Required output of the conformance gate

The gate must emit a machine-readable record containing at least:

- gate identifier and version;
- source commit SHA;
- key implementation SHA;
- operationalisation SHA;
- fixture/conformance seed(s);
- number of states checked;
- number of candidate equal-key pairs checked;
- number of accepted unequal-`O_T` pairs;
- canonical state hashes for accepted smoke pairs;
- deterministic rerun equality result;
- all assertion statuses C1–C9;
- overall `PASS` / `FAIL` / `BLOCKED_INFRASTRUCTURE` decision.

## 6. Fail-closed rules

- Any C1–C8 failure → `FAIL` and no corpus generation.
- Any implementation/import/runtime/invariant failure → `BLOCKED_INFRASTRUCTURE` and no corpus generation.
- A passing conformance gate does not authorize scientific execution.
- Any change to the frozen key, target observable, or authoritative transformation semantics invalidates this gate and requires a new versioned audit/freeze.

## 7. Explicit non-goals

This gate does not:

- establish global identifiability;
- prove that `O_T` is universally independent of the key;
- generate or inspect the Rust dataset;
- train or evaluate predictive models;
- alter N-R1.3;
- reopen the previous C2 derivability analysis.

## 8. Next operational step

Implement a small, deterministic **conformance/smoke probe** that executes C1–C9 only. Run that probe locally after `git pull`. If it returns `PASS`, freeze its output and only then proceed to the separately authorised 5,000-pair corpus-generation step.
