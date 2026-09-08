# DR-043 — RUST-DYN-2 Real Execution Authorization v0.1

**Status:** ACCEPTED — EX-ANTE REAL-DATASET EXECUTION AUTHORIZED
**Date:** 2026-09-08
**Scope:** EXT-1.1 Rust / RUST-DYN-2 / EXEC-1A

## 1. Authorization decision

Following historical reconciliation, semantic re-anchoring, configuration-multiplicity audit, corrected synthetic conformance and real-data preflight, this Decision Record authorizes **one primary real-dataset execution** of RUST-DYN-2.

**REAL-DATASET EXECUTION AUTHORIZED: YES — ONE PRIMARY RUN**

A deterministic replay is mandatory after a technically valid primary run.

No exploratory rerun, parameter change, sampling, filtering, alternative dataset, alternative executor or horizon change is authorized by this DR.

## 2. Preconditions satisfied

- D-OPS-1: PASS — Rust operational specification frozen.
- RUST-DYN-1: PASS — dynamic ΔT_acc / Reach / Trajectory design frozen.
- DR-033: ACCEPTED — dynamic design freeze.
- DR-035: ACCEPTED — temporal population freeze.
- DR-041: ACCEPTED — historical reconciliation and semantic re-anchoring.
- RUST-DYN-2 temporal population reconciliation: CLOSED — EXACT; 516,061 identical pairs; pair-set SHA-256 `1c7a29434675d5e7bbe5a1cfc3a44a809d8eae222d3467374177d8bd20048d8e`; zero timestamp ties.
- DR-042: ACCEPTED — RUST-DYN-2 design freeze / execution not authorized at that stage.
- Configuration multiplicity audit: CLOSED — LOSSLESS FOR CURRENT ASSIGNMENT REPRESENTATION; 3,618,523 dependency rows and 3,618,523 unique origin-target groups; maximum multiplicity 1.
- Corrected RUST-DYN-2 synthetic conformance: CLOSED PASS — 13/13 assertions.
- RUST-DYN-2 real-data preflight: CLOSED PASS — frozen dataset/schema/firewall checks passed.

## 3. Frozen dataset

Filename: `rust_repos_2022_09_07.zip`

Path: `C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`

SHA-256:

`823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`

Any mismatch blocks execution.

## 4. Frozen semantic boundary

Core ontology remains:

`Core_ontological = S`

For each origin `o`:

`T_acc(o) = {τ ∈ Uτ(o) | Pτ(o,C,L)=1}`

Potential depth-1 Reach is re-anchored to the historically frozen Rust structural semantics:

`Succ(C,τ) = C \ {(p_d,*)} ∪ {(p_d,v_d)}`

Reach is the exact canonical set of resulting structural configurations induced by accessible transformations.

Reach is not the transformation identity `τ`.

Trajectory is bounded to `H=1`; no additional semantic ordering among alternative one-step successors is invented. Where no independent ordering exists, the H=1 trajectory representation is the canonical unordered successor collection.

## 5. Frozen temporal population

Rule ID: `DR-035-v0.1-ADJACENT-CREATED-AT`

The primary population is exactly the reconciled population of 516,061 adjacent temporal pairs within package, ordered solely by `created_at`, with exact timestamp ties excluded.

No secondary ordering or non-adjacent pairing is permitted.

## 6. Required real-data computation

For each authorized temporal pair `(o_i,o_j)`:

1. reconstruct the frozen structural inputs;
2. construct `T_acc(o_i)` and `T_acc(o_j)` using frozen R* v0.2 semantics;
3. compute exact canonical `ΔT_acc` membership comparison;
4. construct depth-1 potential Reach from the frozen successor operator;
5. compare Reach sets exactly by canonical configuration membership;
6. construct the bounded H=1 trajectory representation without arbitrary ordering;
7. classify ΔT_acc as persistence, expansion, contraction or reconfiguration as specified by the frozen protocol;
8. report the required ND-1/ND-2/ND-4 contingency evidence.

Reach must not feed back into T_acc/Pτ construction.

## 7. Information firewall

The execution must not read or use:

- downloads, adoption, popularity or success measures;
- future outcome windows;
- predictive targets or predictive metrics;
- later release activity as an outcome signal;
- post-origin metadata;
- runtime/Cargo execution outcomes;
- lockfile results;
- sampling or convenience subsets;
- downstream outcome/value information to define upstream variables.

The experiment is structural and counterfactual-accessibility oriented only.

## 8. Mandatory pre-execution checks

Immediately before execution, the executor must verify and record:

1. exact dataset path;
2. dataset SHA-256 = `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`;
3. exact archive members;
4. R* v0.2 identity = `669d4f01131af518f32b1b4b3da27f676ae4ae55`;
5. RUST-DYN-2 executor identity matches the canonical GitHub version frozen for this authorization;
6. temporal rule ID = `DR-035-v0.1-ADJACENT-CREATED-AT`;
7. horizon = `1`;
8. no sampling;
9. no outcome/predictive access;
10. synthetic conformance = PASS;
11. output directory is clean and uniquely identified as the primary run;
12. configuration-multiplicity audit remains PASS.

Any failed check blocks execution.

## 9. Required command boundary

The final real-data executor must expose one explicit primary-run command and record that exact command in its execution manifest.

The executor must fail closed on dataset hash mismatch, implementation mismatch, temporal-rule mismatch, horizon mismatch, forbidden information access, unsupported duplicate canonical transformations, or any semantic deviation from this authorization.

No real-data execution may occur until the final executor and exact command are frozen in the repository.

## 10. Required outputs

The primary run must produce:

- machine-readable primary result;
- human-readable summary;
- complete stdout/stderr capture;
- execution manifest;
- dataset and implementation hashes;
- exact temporal population identity;
- eligible/excluded origin counts;
- temporal pair count;
- PERSISTENCE / EXPANSION / CONTRACTION / RECONFIGURATION counts;
- exact ΔT_acc evidence required by the frozen protocol;
- exact Reach-set comparison evidence;
- bounded H=1 trajectory evidence;
- ND-1 / ND-2 / ND-4 contingency counts and canonical witnesses where present;
- firewall flags;
- deterministic result hash;
- replay specification.

Raw machine output must contain execution facts, not scientific interpretation.

## 11. Scientific interpretation boundary

After technical PASS and deterministic replay, results may support only bounded statements about the authorized Rust structural population under the frozen operationalization.

The experiment can support or fail to support:

- ND-1: ΔT_acc without ΔReach;
- ND-2: ΔT_acc with ΔReach;
- ND-4: equal Reach cardinality with different Reach membership.

The experiment does not by itself establish universal TGCV validity, causality, predictive superiority, positive value, or originality.

TR-131 and DR-032 remain closed.

## 12. Replay

A deterministic replay is mandatory after a technically valid primary run.

Replay must use the same frozen dataset, executor, resolver semantics, temporal population, horizon and command. Canonical result hashes must reproduce exactly.

Any discrepancy blocks scientific closure and requires a new governance decision before further execution.

## 13. Stop conditions

Execution must stop immediately on:

- dataset hash mismatch;
- executor/semantic identity mismatch;
- archive-member mismatch;
- malformed required structural data;
- duplicate canonical transformation;
- arbitrary timestamp-tie ordering;
- non-adjacent or cross-package pair creation;
- sampling;
- forbidden future/outcome/predictive access;
- nondeterministic output;
- unsupported successor construction;
- any deviation from the frozen successor or Reach semantics.

## 14. Authorization scope

This authorization is intentionally narrow:

**ONE PRIMARY REAL-DATASET RUN, H=1, FOLLOWED BY ONE MANDATORY DETERMINISTIC REPLAY.**

It does not authorize exploratory reruns or modifications.

## 15. Governance conclusion

All identified pre-execution blockers have been cleared or formally bounded. The corrected implementation has passed synthetic conformance, the real dataset has passed the dedicated preflight, the historical temporal population has been exactly reconciled, and the configuration representation has been shown lossless for the frozen assignment representation.

**REAL-DATASET EXECUTION AUTHORIZED: YES — ONE PRIMARY RUN.**

Next controlled operation: freeze the final real-data executor and its exact command in GitHub, then execute the authorized primary run exactly once. After technical audit, perform the mandatory deterministic replay before scientific closure.
