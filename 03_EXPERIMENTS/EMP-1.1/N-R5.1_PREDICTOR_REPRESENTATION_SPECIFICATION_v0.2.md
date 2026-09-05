# N-R5.1 — Predictor Representation Specification v0.2

**Experiment:** TGCV-EMP-1.1  
**Branch:** N — Controlled New Reconstruction  
**Status:** FROZEN FOR PROSPECTIVE USE  
**Date:** 2026-09-05  
**Supersedes:** N-R5.1 v0.1  
**Parent:** N-R4B.4 frozen controlled corpus

## 1. Purpose

This specification defines the predictor-side representations required before learner fitting: `B`, `R`, and direct concatenation `B+R`.

This v0.2 additionally makes normative the canonical semantic identity used by `initial_snapshot_sha256`, resolving the cross-artifact identity defect detected at N-R7 Run 01.

This is a prospective controlled reconstruction specification. It does **not** recover the historical EMP-1.1/MVE-1.0 feature-construction implementation.

## 2. Predictor boundary

Predictor construction is a pure function of the sealed initial state `S_0` and the registered representation specifications.

Allowed state inputs:

- initial component set `V_0`;
- initial directed edge set `E_0`;
- initial resource vector `q_0`;
- initial objective `o_0`;
- frozen Branch N transformation semantics and `T_acc(S_0)`;
- frozen N-R1.3 v0.2 encoder for `R`.

Forbidden predictor inputs:

- trajectory steps after `S_0`;
- successor/post-transition states;
- terminal reason;
- outcome `Y`;
- test-set information during training representation construction;
- learner predictions or losses;
- historical EMP-1.1 result values.

## 3. Canonical initial-state identity — normative

`initial_snapshot_sha256` is the SHA-256 digest of the semantic initial state only.

The canonical object is exactly:

```text
{
  "components": <components>,
  "edges": <edges>,
  "objective": <objective>,
  "resources": <resources>
}
```

Canonical serialization rules:

1. keys sorted lexicographically;
2. compact JSON separators `(',', ':')`;
3. ASCII-safe JSON (`ensure_ascii=True`);
4. UTF-8 encoded bytes;
5. **no trailing newline**;
6. `episode_id` is excluded;
7. any trajectory, outcome, terminal, or post-snapshot field is excluded.

The semantic identity therefore represents `S_0`, not the episode container or record identity.

This convention is identical to the N-R4B.4 initial-state identity convention and is required for the registered N-R7 join:

`episode_id + initial_snapshot_sha256`.

Changing `episode_id` while holding `S_0` fixed MUST NOT change `initial_snapshot_sha256`.

## 4. Baseline B

`B = [n_components, q_1, q_2, q_3, one_hot(o_0)]`

with objective one-hot order `O01,...,O12`.

`dim(B)=16`.

This encoding is reconstructed/prospective, not historical.

## 5. R representation

`R` is the frozen Branch N representation specified by N-R1.3 v0.2 and validated by N-R2/N-R3 conformance.

`dim(R)=58`, in normative R1/R2/R3/R4 order.

Empty accessibility is encoded as exactly 58 zeros.

## 6. Combined representation

`B+R = [B || R]`, with `dim(B+R)=74`.

No interaction terms, embeddings, dimensionality reduction, feature selection, outcome-derived normalization, or additional derived variables are permitted.

## 7. Traceability

Every predictor row must be traceable as:

`episode_id → initial_snapshot_sha256 → B → R → B+R`.

The predictor dataset contains no trajectory-derived fields and no `Y`.

The outcome-side artifact remains separate and may be joined only through the registered episode identifier plus semantic initial-state hash.

## 8. Required conformance checks

In addition to the prior N-R5.2 checks, conformance MUST verify:

1. identical `S_0` with different `episode_id` gives identical `initial_snapshot_sha256`;
2. adding forbidden post-snapshot fields does not alter the hash;
3. canonical bytes contain only the four semantic state fields;
4. canonical bytes have no trailing newline;
5. the hash is byte-compatible with the N-R4B.4 semantic initial-state convention;
6. no trajectory/outcome/learner/network dependency exists.

## 9. Provenance and supersession

N-R5.1 v0.1 remains preserved as historical development provenance. Its prior hash convention is **superseded** and must not be used for future N-R5.3 regeneration or N-R7 execution.

The v0.2 correction is an integration-consistency repair discovered before any learner fit. It does not use scientific results, does not tune any learner, and does not alter B, R, B+R, seeds, train/test partition, labels, controls, or learner parameters.

Because the frozen N-R5.3 predictor files contain the superseded hash convention, they MUST be regenerated from the unchanged frozen N-R4B.4 snapshots before further N-R7 execution.

## 10. Gate decision

**N-R5.1 v0.2 STATUS: FROZEN FOR PROSPECTIVE USE.**

**Scientific execution remains blocked until N-R5.2 conformance and N-R5.3 predictor-dataset regeneration/integrity freeze are PASS/CLOSED.**
