# DR-036 — RUST-DYN-EXEC-1 Real Execution Authorization v0.1

**Status:** ACCEPTED — EX-ANTE REAL-DATASET EXECUTION AUTHORIZED
**Date:** 2026-09-08
**Scope:** EXT-1.1 Rust / RUST-DYN-1 / RUST-DYN-STATE-1 / RUST-DYN-EXEC-1

## 1. Authorization decision

Following completion of the required design, implementation, conformance and preflight gates, this Decision Record authorizes **one primary real-dataset execution** of RUST-DYN-EXEC-1.

**REAL-DATASET EXECUTION AUTHORIZED: YES — ONE PRIMARY RUN**

A deterministic replay is separately mandatory after a technically valid primary run.

No additional rerun, parameter change, sampling, filtering, alternative executor, alternative dataset, or horizon change is authorized by this DR.

## 2. Preconditions satisfied

- D-OPS-1: PASS — Rust structural operational specification frozen.
- RUST-DYN-1: PASS — dynamic ΔT_acc / Reach / Trajectory design frozen.
- RUST-DYN-STATE-1: PASS CONDITIONAL — bounded successor-state representation accepted subject to normalization.
- RUST-DYN-ENGINE-2: PASS — synthetic conformance 11/11.
- DR-033: ACCEPTED — ex-ante dynamic design freeze.
- DR-035: ACCEPTED — ex-ante temporal population freeze.
- RUST-DYN-EXEC-1A dataset/schema preflight: PASS and CLOSED.
- RUST-DYN-EXEC-1A adapter conformance: PASS, 7/7.
- RUST-DYN-EXEC-1A adapter integrity closure: PASS.

## 3. Frozen dataset

Filename: `rust_repos_2022_09_07.zip`

Path: `C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`

SHA-256:

`823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`

Any hash mismatch blocks execution.

## 4. Frozen implementation

Primary structural adapter:

`03_EXPERIMENTS/EXT-1.1_Rust/src/rust_dyn_adapter_v01.py`

The adapter must be the post-integrity-hardening version committed after RUST-DYN-EXEC-1A. Its current GitHub content SHA is:

`539b38ccbf1798f015c06c9cb6a0319328018afa`

Authorization requires the local executable to match the GitHub canonical content before execution.

Downstream engine semantics are frozen to:

`03_EXPERIMENTS/EXT-1.1_Rust/src/rust_dyn_engine_v02.py`

Blob SHA:

`a2e925b1af18d25dd9f9ff695afecc50090336f6`

Resolver:

`03_EXPERIMENTS/EXT-1.1_Rust/src/rstar_v02.py`

Blob SHA:

`669d4f01131af518f32b1b4b3da27f676ae4ae55`

The real executor must combine these frozen semantics without modifying D-OPS-1, RUST-DYN-1, RUST-DYN-STATE-1 or DR-035.

## 5. Frozen temporal population

Rule ID: `DR-035-v0.1-ADJACENT-CREATED-AT`

For each package, eligible origins are ordered solely by `created_at`. Exact timestamp ties are excluded. The primary population consists exclusively of adjacent consecutive origins after tie exclusion.

No secondary ordering, non-adjacent pairing, cross-package pairing, outcome-based selection or retrospective pair selection is permitted.

## 6. Frozen dynamic semantics

For each authorized temporal pair:

- `T_i = T_acc(o_i)`
- `T_j = T_acc(o_j)`
- exact canonical set comparison is mandatory;
- expansion = `T_j \ T_i`;
- contraction = `T_i \ T_j`;
- persistence = `T_i ∩ T_j`;
- equal cardinality with different membership is RECONFIGURATION;
- `Reach_H` and `Trajectory_H` use the RUST-DYN-STATE-1 bounded successor-state convention;
- initial origin identity is excluded from Reach and Trajectory;
- `H = 1`.

## 7. Information firewall

The run must not read or use:

- later release activity as an outcome signal;
- downloads, adoption, popularity or success measures;
- future outcome windows;
- predictive targets or predictive metrics;
- post-origin metadata;
- sampling or convenience subsets;
- Reach/Trajectory information while constructing `T_acc`;
- downstream outcome/value information to define upstream variables.

The execution is structural and counterfactual-accessibility oriented only.

## 8. Mandatory pre-execution local checks

Immediately before the primary run, the local executor must verify and record:

1. exact dataset path;
2. dataset SHA-256 = frozen value;
3. adapter content/hash matches canonical GitHub version;
4. R* v0.2 identity matches frozen value;
5. Python/runtime and operating environment;
6. exact command;
7. `H=1`;
8. DR-035 temporal rule ID;
9. no sampling;
10. no outcome/predictive access;
11. frozen archive members exist exactly;
12. synthetic conformance remains PASS;
13. output directory is clean and uniquely identified for this primary run.

Any failed check blocks execution.

## 9. Required command boundary

The command must be recorded exactly in the primary execution manifest after the final real-data executor has been frozen. No alternative command is authorized under this DR.

The executable must fail closed if the dataset hash, implementation identity, horizon or authorization state does not match the frozen specification.

## 10. Required outputs

The primary run must produce:

- machine-readable primary result;
- human-readable summary;
- complete stdout;
- complete stderr;
- execution manifest;
- primary result SHA-256;
- counts of eligible origins, timestamp ties, excluded origins, temporal pairs and zero-pair packages;
- counts/classification of PERSISTENCE, EXPANSION, CONTRACTION and RECONFIGURATION;
- exact structural `ΔT_acc` evidence required by the frozen protocol;
- bounded Reach/Trajectory results required by RUST-DYN-1;
- firewall flags;
- deterministic replay input specification.

Raw machine output must contain execution facts, not scientific interpretation.

## 11. Scientific interpretation boundary

After technical PASS, the result may support only bounded statements about the authorized Rust structural population and frozen operational definitions.

Potential result categories:

- H-R1 supported / not supported;
- H-R3 supported / not supported;
- H-R4 supported / not supported;
- indeterminate if technical integrity or replay fails.

The run does not by itself establish universal TGCV validity, causality, predictive superiority, positive value, or originality.

TR-131 and DR-032 remain closed.

## 12. Replay

A deterministic replay is mandatory after primary technical PASS.

Replay must use the same frozen dataset, executor/adapter, resolver, temporal rule, horizon and command. The deterministic summary and canonical result hash must reproduce exactly.

Any discrepancy blocks scientific closure and requires a new governance decision before further execution.

## 13. Stop conditions

Execution must stop immediately on:

- dataset hash mismatch;
- executable/hash mismatch;
- resolver mismatch;
- archive-member mismatch;
- malformed required structural data;
- duplicate canonical transformation;
- arbitrary timestamp-tie ordering;
- non-adjacent or cross-package pair creation;
- sampling;
- outcome/predictive access;
- nondeterministic output;
- any semantic deviation from the frozen definitions.

## 14. Authorization scope

This authorization is intentionally narrow:

**ONE PRIMARY REAL-DATASET RUN, H=1, FOLLOWED BY ONE MANDATORY DETERMINISTIC REPLAY.**

It does not authorize exploratory reruns or modifications.

## 15. Governance conclusion

All required ex-ante conditions are satisfied. The project may now proceed from design/preflight into the controlled real-data execution phase.

**REAL-DATASET EXECUTION AUTHORIZED: YES — ONE PRIMARY RUN.**

Next controlled operation: construct/freeze the final real-data executor and execute the authorized primary run exactly once. Then perform the mandatory replay gate before scientific closure.
