# RUST-DYN-2 EXEC-1A — Synthetic Conformance Closure v0.2

**Date:** 2026-09-08  
**Status:** CLOSED — SYNTHETIC CONFORMANCE PASS / REAL EXECUTION NOT AUTHORIZED

## Executor

`03_EXPERIMENTS/EXT-1.1_Rust/src/rust_dyn2_executor_v02.py`

Implementation correction after execution: documentation escape warning removed without semantic change.

## User execution

Command:

```text
python .\03_EXPERIMENTS\EXT-1.1_Rust\src\rust_dyn2_executor_v02.py --synthetic
```

Result: `pass = true`.

## Conformance assertions

All 13 assertions passed:

- canonical_four_field_identity
- deterministic_canonicalization
- duplicate_fail_closed
- firewall_closed
- h_gt_1_not_claimed
- nd1_delta_t_reach_equal
- nd2_delta_t_reach_changed
- nd4_equal_cardinality_different_membership
- reach_is_configuration_set
- real_execution_blocked
- successor_is_not_tau
- trajectory_excludes_origin
- trajectory_h1_non_arbitrary

## Deterministic object hashes

- T_a: `c2e71c95f460d54a775bc903424e85fc757165f5e757dad9e934bd5ea95af782`
- T_b: `e012f76bd8e89360f9d15f24d44e6ba0d9e1b0503dc637dff1bd73c9fa1a00e9`
- R_a: `0906c0a5734ee4538bec21dca3fc70415ab18b91359999efdb1eb0c7a5bec3e7`
- R_b: `e4be19cf73fbcc21d7cc359f01ecf9d2a49c61668e6b5eba2ead6d9365dce766`
- G_a_H1: `0906c0a5734ee4538bec21dca3fc70415ab18b91359999efdb1eb0c7a5bec3e7`
- G_b_H1: `e4be19cf73fbcc21d7cc359f01ecf9d2a49c61668e6b5eba2ead6d9365dce766`

The equality of each H=1 trajectory hash with its corresponding Reach hash is expected under the bounded H=1 representation: trajectory introduces no additional semantic ordering among one-step alternatives.

## Interpretation

Synthetic conformance establishes that the implementation can represent the re-anchored Potential Reach semantics, exact set comparison, the selected non-redundancy witnesses, and the bounded H=1 trajectory representation without introducing an arbitrary path ordering.

It does **not** establish the empirical existence of ND-1/ND-2/ND-4 in the Rust dataset. Synthetic cases are implementation conformance fixtures only.

## Firewall

No real dataset was read. No T_acc, ΔT_acc, Reach, Trajectory, outcome, value, future activity, adoption, downloads, predictive metric, or runtime execution result was read or computed from the real dataset.

`real_rust_dyn2_execution_authorized = false`.

## Governance consequence

EXEC-1A synthetic conformance is closed PASS. The next controlled operation is the dedicated real-data preflight for RUST-DYN-2. A separate execution-authorization decision remains mandatory.
