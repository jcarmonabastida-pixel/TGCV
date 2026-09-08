# TGCV — RMA current state

**Date:** 2026-09-08  
**Status:** CURRENT / OPERATIVE  
**Current master:** `TGCV_RMA_v0.5.md`  
**Governance decision:** DR-044  
**Conformance closure:** DR-045  
**Structural propagation:** EXT-UPD-1R.4 + EXT-UPD-3.1 + EXT-UPD-3.2

This file is the current RMA pointer. It is not a historical record. Historical RMA versions remain immutable.

## Current state

- Core ontology: `S`
- Analytical object: `T_acc = F(S,C,L)`
- Central phenomenon: `ΔT_acc`
- Downstream chain: `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`
- `I`: explanatory mechanism, not Core primitive.

## Evidence state

- TR-131: CLOSED.
- RUST-DYN-1: CLOSED.
- RUST-DYN-2 / EXEC-1A: CLOSED — bounded structural empirical pass.
- Independent replication: OPEN.
- Cross-domain empirical generalisation: OPEN; no execution-ready external domain currently identified.
- Causal, predictive and value claims: OPEN.
- Originality: BOUNDED/PARTIAL, not established.
- Transversal translation protocol: FROZEN; D-OPS-24 is next controlled operation.

## External asset structure

`05_ASSETS/` is the canonical physical surface for external-facing deliverables:

- TCP → `05_ASSETS/TCP/` — current `TGCV-EXT-TCP-001_v0.3.md`
- Vision Paper → `05_ASSETS/Vision_Paper/`
- Research Prospectus → `05_ASSETS/Research_Prospectus/` — current `TGCV-EXT-RP-001_v0.1.md`
- ARM → `05_ASSETS/ARM/`
- RII → `05_ASSETS/RII/`
- MOI → `05_ASSETS/MOI/` (reserved; substantive creation deferred)

The IE PhD Research Prospectus adaptation is subordinate to the generic RP and is located under `05_ASSETS/Research_Prospectus/adaptations/IE_PhD/`.

## Current claim control

Authoritative matrix:
`00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_POST_DOPS23_v0.1.md`.

C01–C02 = E0; C03–C07 = E1 within frozen Rust; C08–C12 = H; C13 = O; C14–C15 = F within scope; C16 = H.

## Current gate state

- G1 Independent replication: OPEN
- G2 Cross-domain generalisation: OPEN
- G3 Trajectory sufficiency: OPEN
- G4 Causal identification: OPEN
- G5 Value linkage: OPEN
- G6 Originality/comparative architecture: BOUNDED/PARTIAL
- G7 Transversal translation protocol: FROZEN / D-OPS-24 NEXT

## Governance state

DR-044 established the RMA reconciliation and propagation control. DR-045 closed the governance conformance test with PASS. EXT-UPD-1R.4 propagated the external-asset structural regularisation. EXT-UPD-3.1 propagated the current RP v0.1. EXT-UPD-3.2 propagates the current TCP v0.3.

Propagation rule:

`accepted result/decision → impact analysis → RMA → dependent current assets → STATUS → claim/evidence control → consistency audit → next controlled operation`.

**D-OPS-24 is unblocked by governance consistency and remains subject to its own historical reconstruction, design and preflight.**
