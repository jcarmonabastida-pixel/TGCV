# N-R5.1 — Predictor Representation Specification v0.1

**Experiment:** TGCV-EMP-1.1  
**Branch:** N — Controlled New Reconstruction  
**Status:** PROPOSED FOR PROSPECTIVE FREEZE  
**Date:** 2026-09-05  
**Parent:** N-R4B.4 frozen controlled corpus

## 1. Purpose

This specification defines the predictor-side representations required before any learner fitting:

- baseline representation `B`;
- TGCV representation `R`;
- concatenated representation `B+R`.

It is a prospective controlled reconstruction specification. It does **not** recover the historical EMP-1.1/MVE-1.0 feature-construction implementation.

No learner fitting, pilot inference, confirmatory inference, or result-driven tuning is authorized by this document.

## 2. Frozen predictor boundary

Predictor construction is a pure function of the sealed initial snapshot `S_0` and the registered representation specifications.

Allowed inputs:

- initial component set `V_0`;
- initial directed edge set `E_0`;
- initial resource vector `q_0`;
- initial objective `o_0`;
- frozen Branch N transformation semantics and `T_acc(S_0)`;
- frozen N-R1.3 v0.2 encoder for `R`.

Forbidden inputs:

- any trajectory step after `S_0`;
- any successor state;
- terminal reason;
- outcome `Y`;
- any test-set information during training representation construction;
- learner predictions or losses;
- historical EMP-1.1 result values.

## 3. Baseline B — specification status

The recovered EMP-1.1 protocol specifies baseline `B` as:

`component count + three resource values + objective identity`.

This semantic content is treated as **SPECIFIED**. The historical numerical encoding of objective identity is not recovered.

Therefore N-R5.1 does **not** silently claim historical encoding.

## 4. Prospective B encoding

For Branch N, `B` is reconstructed prospectively as a fixed numerical vector:

`B = [n_components, q_1, q_2, q_3, one_hot(o_0)]`

where:

- `n_components = |V_0|`;
- `q_1,q_2,q_3 ∈ {0,1,2,3}`;
- `one_hot(o_0)` is a 12-dimensional one-hot vector ordered `O01,...,O12`.

Thus:

`dim(B) = 1 + 3 + 12 = 16`.

The objective is encoded nominally rather than as an ordinal integer, avoiding an artificial metric ordering between objective labels.

This encoding is **RECONSTRUCTED / PROSPECTIVE**, not historical.

## 5. R representation

`R` is the frozen Branch N representation specified by N-R1.3 v0.2 and validated by N-R2/N-R3 conformance.

`dim(R) = 58`.

The canonical order is:

1. R1 — 6 family availability features;
2. R2 — 6 family cardinality features;
3. R3 — 30 component-incidence features;
4. R4 — 16 transition-result structural features.

Empty accessibility is encoded as exactly 58 zeros.

No trajectory or outcome information enters `R(S_0)`.

## 6. Combined representation

The primary combined predictor is the direct concatenation:

`B+R = [B || R]`.

Therefore:

`dim(B+R) = 16 + 58 = 74`.

No interaction terms, learned embeddings, normalization fitted on outcomes, dimensionality reduction, feature selection, or additional derived variables are introduced at this gate.

## 7. Canonical feature order

### B

1. `n_components`
2. `q_1`
3. `q_2`
4. `q_3`
5–16. `objective_O01` ... `objective_O12`

### R

The exact N-R1.3 v0.2 canonical order is normative.

### B+R

All 16 B features first, followed by all 58 R features in their normative order.

## 8. Normalization

No pre-R normalization is applied to the 58 R features, consistent with N-R1.3 v0.2.

For B, raw integer values are retained in the canonical representation. Any learner-specific preprocessing, if later required by a frozen learner implementation, must be specified separately and identically across B and B+R arms. It may not use outcome information.

## 9. Traceability

Every predictor row must be traceable to:

`episode_id → initial_snapshot_sha256 → B → R → B+R`.

The predictor dataset must not contain trajectory-derived fields or `Y`.

A separate outcome-side artifact retains trajectory and outcome information. The two sides may be joined only through the registered episode identifier plus initial snapshot hash for analysis.

## 10. Leakage tests required before freeze

The N-R5.1 implementation/conformance gate must verify at minimum:

1. B is invariant to replacement of the trajectory while S_0 is unchanged;
2. R is invariant to replacement of the trajectory while S_0 is unchanged;
3. B+R is invariant to replacement of the trajectory while S_0 is unchanged;
4. predictor construction does not read `Y`;
5. predictor construction does not read terminal reason or trajectory steps;
6. predictor rows preserve episode and snapshot identity;
7. objective one-hot ordering is deterministic;
8. B has exactly 16 features;
9. R has exactly 58 features;
10. B+R has exactly 74 features;
11. same snapshot produces byte-identical predictor representation;
12. no learner or network access is required;
13. train/test predictor rows are generated independently from their sealed snapshots;
14. historical result values are absent from predictor construction.

## 11. Provenance classification

- baseline semantic fields: **SPECIFIED**;
- baseline objective encoding: **RECONSTRUCTED / PROSPECTIVE**;
- B dimensionality: **DERIVED from the prospective encoding**;
- R semantics: **RECONSTRUCTED / PROSPECTIVE**, frozen by N-R1.3 v0.2;
- R dimensionality: **SPECIFIED / CONFORMANCE VERIFIED**;
- B+R concatenation: **DERIVED**;
- predictor/outcome separation: **DERIVED / SPECIFIED**.

## 12. Historical boundary

Nothing in this specification may be cited as evidence that the historical EMP-1.1/MVE-1.0 implementation used one-hot objective encoding, a 16-dimensional B vector, or a 74-dimensional B+R vector.

Those are Branch N prospective reconstruction decisions.

The historical EMP-1.1 result remains a frozen historical record and is not used to select or tune this representation.

## 13. Gate decision

**N-R5.1 STATUS: PROPOSED FOR PROSPECTIVE FREEZE.**

The specification is sufficiently explicit to implement and test the predictor-side representation while preserving the historical boundary.

No scientific learner execution is authorized at this stage.

### Next gate

**N-R5.2 — B/R implementation and leakage/conformance test.**
