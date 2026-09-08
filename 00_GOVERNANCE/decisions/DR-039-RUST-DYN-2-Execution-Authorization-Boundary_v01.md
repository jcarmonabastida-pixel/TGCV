# DR-039 — RUST-DYN-2 Execution Authorization Boundary v0.1

## Status

**ACCEPTED — PRE-AUTHORIZATION BOUNDARY CONFIRMED / REAL EXECUTION NOT AUTHORIZED**

Date: 2026-09-08

## Basis

RUST-DYN-2 synthetic conformance and real-data input preflight both passed.

However, the currently frozen `rust_dyn2_executor_v01.py` remains a synthetic-first executor whose real-dataset path is explicitly fail-closed. Therefore it cannot itself be used as the authorized real-data executor.

This boundary is intentional and prevents authorization of an executable whose real-data implementation has not independently passed the required conformance and integrity checks.

## Accepted evidence

### Synthetic conformance

Artifact:
`03_EXPERIMENTS/EXT-1.1_Rust/execution/RUST-DYN-2_EXEC-1A_SYNTHETIC_CONFORMANCE_CLOSURE_v01.md`

Result: PASS.

ND-1 through ND-5 passed, including:

- `ΔT_acc != 0` with `ΔReach = 0`;
- `ΔT_acc != 0` with `ΔReach != 0`;
- equal Reach cardinality with different membership;
- same Reach with different trajectory ordering;
- independent four-field transformation identity.

### Real-data preflight

Artifact:
`03_EXPERIMENTS/EXT-1.1_Rust/execution/RUST-DYN-2_EXEC-1A_REAL_DATA_PREFLIGHT_CLOSURE_v01.md`

Result: PASS.

Frozen dataset SHA-256:
`823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`

Temporal rule:
`DR-035-v0.1-ADJACENT-CREATED-AT`

Horizon:
`H=1`

Required dataset members and schemas passed preflight.

## Authorization boundary

**REAL-DATASET EXECUTION AUTHORIZED: NO.**

No real-data run may be performed under this decision.

The authorization gate remains open until a dedicated real-data RUST-DYN-2 executor/adapter has been constructed and frozen.

## Mandatory real-data implementation requirements

The future executor must:

1. load only the frozen dataset and exact frozen archive members;
2. use the frozen four-field transformation identity;
3. construct `T_acc` independently of Reach and Trajectory;
4. construct bounded `Reach_H` independently of `T_acc`;
5. construct ordered `Trajectory_H` independently of `T_acc`;
6. use DR-035 adjacent temporal pairs only;
7. exclude exact timestamp ties without arbitrary secondary ordering;
8. compare sets/sequences by exact membership/order, not cardinality alone;
9. compute the pre-registered contingency cells `(D_T,D_R,D_G)`;
10. identify valid ND-1 through ND-5 observations where present;
11. fail closed on duplicates, malformed structural records and ambiguous identities;
12. enforce the existing information firewall;
13. perform no sampling or retrospective outcome-based selection;
14. produce deterministic canonical output suitable for byte-identical replay;
15. expose dataset, executor, resolver and output hashes;
16. support exactly one primary run followed by one mandatory replay after authorization.

## Scientific boundary

A future PASS may support bounded structural evidence for the RUST-DYN-2 hypotheses. It will not by itself establish causality, predictive superiority, universal validity, positive value, or originality.

RUST-DYN-EXEC-1 remains scientifically closed and its result must not be reused as RUST-DYN-2 evidence.

## Next controlled operation

**RUST-DYN-2-EXEC-1B — Real-Data Executor Construction + Synthetic Conformance.**

After that implementation passes synthetic conformance, a new real-data authorization review will freeze the executable and permit the actual primary run.

No dataset execution is authorized by this Decision Record.
