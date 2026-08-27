# TGCV-EXT-1.0 — Final External Replication Report

**Decision:** FAIL / NO SUPPORT under the locked historical EXT-1.0 rule.

This result is a failure to obtain the pre-specified magnitude of incremental predictive information under that operationalisation. It is not interpreted as a falsification of the TGCV Core.

## Dataset

- Source: SNAP CollegeMsg
- File: `CollegeMsg.txt.gz`
- SHA-256: `50ae2d98ed3bad9ddb18dbd495a89e5e10cfb8f7e86932827db29fc41b41f9fa`
- Records: 59,835

## Operationalisation

`Core_ontological = S`  
`T_acc = F(S,C,L)`  
`ΔT_acc → ΔReach → ΔTrajectory`

The operational representation R uses change in accessible-transformation features between consecutive weekly snapshots; baseline B contains network/activity descriptors. Outcome Y is formation of at least one new directed interaction in the following weekly forecast window. Features are restricted to information available at the snapshot cutoff and evaluation is chronological.

## Fixed external holdout

- training snapshots: 18
- test snapshots: 7
- test observations: 13,012

| Model | LogLoss | AUC |
|---|---:|---:|
| B | 0.145701 | 0.843711 |
| B + ΔR | 0.136984 | 0.842770 |

`ΔLogLoss = 0.008717`  
`paired sign-flip p = 0.00019996`

The p-value is small, but the locked effect-size requirement was `ΔLogLoss >= 0.04`; the observed improvement is substantially smaller.

## Controls

- cardinality-only: LogLoss 0.139330; AUC 0.850256
- permuted-R: LogLoss 0.140314; AUC 0.825993

Expanding walk-forward analysis was directionally positive but remained below the locked 0.04 criterion.

## Scientific interpretation

`TGCV-EXT-1.0` does not provide sufficient external empirical support for the pre-specified predictive claim under this operationalisation.

It does not justify changing the Core or the locked decision criterion retrospectively. The result must remain visible in the RMA and experimental history.
