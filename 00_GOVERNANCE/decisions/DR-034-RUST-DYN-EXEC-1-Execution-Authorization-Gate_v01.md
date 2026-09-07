# DR-034 — RUST-DYN-EXEC-1 Execution Authorization Gate v0.1

**Status:** ACCEPTED — EX-ANTE EXECUTION GATE PREPARED / NOT YET AUTHORIZED
**Date:** 2026-09-08
**Scope:** EXT-1.1 Rust / RUST-DYN-1 / RUST-DYN-STATE-1 / RUST-DYN-ENGINE-2
**Predecessors:** D-OPS-1; DR-033; RUST-DYN-ENGINE-2 synthetic conformance

## 1. Purpose

Freeze the exact conditions required for the first real-dataset execution of RUST-DYN-EXEC-1.

This document is an authorization gate, not a scientific result and not an authorization to execute by itself. Real-dataset execution remains blocked until all mandatory pre-execution integrity fields are verified locally and this gate is explicitly accepted as **AUTHORIZED**.

## 2. Scientific boundary

The execution tests the operationalized dynamic structural layer defined by RUST-DYN-1:

- exact temporal comparison of `T_acc` membership sets;
- classification as PERSISTENCE, EXPANSION, CONTRACTION, or RECONFIGURATION;
- bounded downstream `Reach_H` and `Trajectory_H` representations;
- separation of accessibility from execution and outcome.

It does **not** test or establish universal TGCV validity, causality, predictive superiority, positive value, or originality.

## 3. Frozen implementation

### Executor

Canonical executor:

`03_EXPERIMENTS/EXT-1.1_Rust/src/rust_dyn_engine_v02.py`

Expected blob SHA:

`a2e925b1af18d25dd9f9ff695afecc50090336f6`

The synthetic conformance result for this executor is PASS: 11/11 tests true. The executor explicitly refuses real-dataset execution at v0.2. Therefore a real-data adapter/executor must be created and frozen as a separate implementation before this gate can become executable.

### Design

`03_EXPERIMENTS/EXT-1.1_Rust/RUST-DYN-1_DYNAMIC_DELTA_TACC_REACH_TRAJECTORY_OPERATIONAL_GATE_v0.1.md`

### State normalization

`03_EXPERIMENTS/EXT-1.1_Rust/RUST-DYN-STATE-1_REACH_STATE_SUFFICIENCY_GATE_v0.1.md`

No semantic change to the frozen design is authorized during adapter implementation.

## 4. Frozen dataset

Dataset filename:

`rust_repos_2022_09_07.zip`

Expected local path:

`C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`

Dataset SHA-256: **MUST BE COMPUTED AND RECORDED IN THE PRE-EXECUTION PREFLIGHT.**

No replacement, refreshed, filtered, sampled, decompressed-and-modified, or otherwise altered dataset is authorized.

## 5. Frozen temporal design

For each package, temporal comparison uses two package-version origins ordered by `created_at`.

- Exact timestamp ties are not arbitrarily ordered.
- `T_i = T_acc(o_i)` and `T_j = T_acc(o_j)`.
- Compare canonical membership sets exactly.
- `T_j \ T_i` = expansion component.
- `T_i \ T_j` = contraction component.
- `T_i ∩ T_j` = persistence component.
- Equal cardinality with different membership is a genuine RECONFIGURATION, not persistence.

The engine must not replace set identity with cardinality-only comparison.

## 6. Frozen downstream semantics

`Reach_H(o)` is the finite-horizon successor space generated from accessible transformations, excluding the initial origin node.

`Trajectory_H(o)` is the ordered finite-horizon successor sequence space, excluding the initial origin identity while preserving path order.

The accepted bounded-state interpretation is the RUST-DYN-STATE-1 convention: package `version_id` is a bounded successor-state identifier within the frozen package-version structural graph, not a claim of complete Rust ecosystem state.

Horizon must be an explicit fixed parameter of the run and recorded in the output. The first authorized real execution should use **H=1**, unless a new governance decision explicitly changes the horizon.

## 7. Information firewall

The execution must not read, derive, or use:

- later release activity outside the frozen origin-local structural reconstruction;
- downloads, adoption, popularity, success, or other outcome proxies;
- future outcome windows;
- predictive targets or predictive metrics;
- Reach/Trajectory information during the construction of the accessibility predicate;
- post-origin metadata;
- sampling or convenience subsets;
- package identity as an additional substitute for the frozen analytical representation;
- any result from later stages to construct an earlier-stage variable.

Outcome and value remain downstream and are not accessed by this gate.

## 8. Required pre-execution integrity gate

Before any real-data execution, a local preflight MUST record:

1. exact dataset path;
2. dataset SHA-256;
3. exact executor file SHA-256/blob identity;
4. exact resolver `R* v0.2` identity/hash;
5. Python version/runtime;
6. operating environment;
7. exact command;
8. horizon;
9. canonical transformation identity;
10. temporal ordering rule;
11. duplicate handling;
12. missing-data rule;
13. information-firewall status;
14. output artifact names/paths;
15. no-sampling confirmation;
16. no-outcome/no-predictive-access confirmation.

If any mandatory field cannot be established, execution is blocked.

## 9. Required real-data adapter

Because `rust_dyn_engine_v02.py` is synthetic-only and explicitly refuses `--dataset`, a separate real-data adapter/executor must be created before authorization.

The adapter MUST:

- load only the frozen dataset;
- implement exactly the D-OPS-1 frozen `S,C,L,Uτ,Pτ,T_acc` semantics;
- preserve the RUST-DYN-1 temporal and downstream definitions;
- fail closed on duplicate canonical transformations;
- fail closed on malformed required structural records;
- never silently sample;
- never access outcome/predictive fields;
- emit complete machine-readable deterministic output;
- expose executor version/hash in the output;
- preserve complete stdout/stderr.

The adapter must first pass a synthetic conformance suite equivalent to RUST-DYN-ENGINE-2 before real execution is authorized.

## 10. Required output artifacts

At minimum:

- primary machine-readable execution result;
- human-readable execution summary;
- complete stdout capture;
- complete stderr capture;
- execution manifest containing dataset hash, executor identity, resolver identity, runtime, command, horizon, timestamp and firewall flags;
- primary-result SHA-256;
- deterministic replay result;
- replay comparison/audit;
- final execution-result closure.

Raw primary output must contain execution facts only and no scientific interpretation.

## 11. PASS / FAIL criteria

### Technical PASS

All of the following must hold:

- dataset resolves exactly to the frozen file;
- dataset hash is recorded;
- executor identity is frozen and matches the authorized adapter;
- resolver identity matches frozen `R* v0.2`;
- no sampling occurs;
- required structural reconstruction is valid;
- duplicate transformations fail closed;
- canonicalization is deterministic;
- temporal ordering is deterministic;
- exact set comparison is used;
- Reach/Trajectory exclude the initial origin as specified;
- firewall flags are closed;
- output is complete and machine-readable;
- replay reproduces the deterministic summary/result hash exactly.

### Scientific result categories

After technical PASS only:

- **H-R1 supported:** at least one valid temporal pair exhibits non-trivial `ΔT_acc`.
- **H-R1 not supported:** no valid temporal pair exhibits non-trivial `ΔT_acc`.
- **H-R3 supported:** an admissible case exhibits a bounded structural association between `ΔT_acc` and `ΔReach` and/or `ΔTrajectory` under the frozen definitions.
- **H-R3 not supported:** no such case is observed in the authorized population.
- **H-R4 supported:** accessible alternatives are represented without requiring execution/outcome access in the authorized structural construction.
- **Indeterminate:** integrity, firewall, reconstruction, or replay requirements fail.

Observed support is bounded to the frozen dataset and operational definitions.

## 12. Replay gate

A deterministic replay is mandatory after a technically valid primary execution.

Replay must use the same dataset, adapter/executor version, resolver, command, horizon and environment constraints. Any difference in deterministic summary or canonical result hash invalidates reproducibility until explained and resolved under a new governance decision.

## 13. Authorization boundary

**REAL-DATASET EXECUTION AUTHORIZED: NO — PRE-EXECUTION GATE ONLY.**

Authorization can be changed to YES only after:

1. the real-data adapter is created;
2. the adapter passes synthetic conformance;
3. the local preflight records all mandatory integrity fields, including dataset SHA-256;
4. the exact executable/hash and command are frozen;
5. no semantic deviation from D-OPS-1, RUST-DYN-1, or RUST-DYN-STATE-1 is identified;
6. a new explicit governance acceptance authorizes the real run.

## 14. Next controlled operation

**RUST-DYN-EXEC-1A — Real-Data Adapter + Preflight.**

No real dataset execution is permitted before RUST-DYN-EXEC-1A is completed and a subsequent authorization decision is recorded.

## 15. Governance conclusion

This gate is **PASS as a pre-execution authorization specification** and **NOT an execution authorization**.

The project therefore advances to adapter construction and integrity preflight without executing the real Rust dataset.