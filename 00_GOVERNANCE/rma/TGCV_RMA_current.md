# TGCV — RMA current state

**Date:** 2026-09-09  
**Status:** CURRENT / OPERATIVE  
**Current master:** `TGCV_RMA_v1.2.md`  
**Governance decision:** DR-044  
**Conformance closure:** DR-045  
**Structural/content propagation:** EXT-UPD-1R.4 + EXT-UPD-3.1 + EXT-UPD-3.2 + EXT-UPD-3.3.5 + EXT-UPD-3.4 + EXT-UPD-3.5 + EXT-UPD-3.6

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
- Cross-domain empirical generalisation: OPEN.
- Causal, predictive and value claims: OPEN.
- Originality: BOUNDED/PARTIAL, not established.
- Transversal translation protocol: FROZEN; D-OPS-24 is next controlled operation.

## External asset structure

`05_ASSETS/` is the canonical physical surface for external-facing deliverables:

- TCP → `05_ASSETS/TCP/` — current `TGCV-EXT-TCP-001_v0.3.md`
- Vision Paper → `05_ASSETS/Vision_Paper/` — current `TGCV-EXT-VP-001_v0.2.md`
- Research Prospectus → `05_ASSETS/Research_Prospectus/` — current `TGCV-EXT-RP-001_v0.1.md`
- ARM → `05_ASSETS/ARM/` — current `TGCV-EXT-ARM-001_v0.1.md`
- RII → `05_ASSETS/RII/` — current `TGCV-EXT-RII-001_v0.1.md`
- MOI → `05_ASSETS/MOI/` (reserved; substantive creation deferred)

The IE PhD Research Prospectus adaptation is subordinate to the generic RP and is located under `05_ASSETS/Research_Prospectus/adaptations/IE_PhD/`.

## Scientific-memory registry

Canonical reusable scientific-memory registry:
`02_EXTERNAL_SCIENCE/SCIENTIFIC_ASSET_REGISTRY_v0.1.md`.

`02_LITERATURE/` remains the historical SLR working/archive surface. Relevant historical scientific artifacts remain discoverable through the registry without requiring physical migration.

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

DR-044 established the RMA reconciliation and propagation control. DR-045 closed the governance conformance test. EXT-UPD-1R.4 regularised the external-asset structure. EXT-UPD-3.1 propagated RP v0.1. EXT-UPD-3.2 propagated TCP v0.3. EXT-UPD-3.3.5 propagated Vision Paper v0.2. EXT-UPD-3.4 propagated ARM v0.1. EXT-UPD-3.5 propagated RII v0.1 through RMA v1.0, current pointer and traceability without changing scientific claims, evidence levels or gate states. EXT-UPD-3.6 establishes the canonical scientific-memory registry and reuse control without changing scientific claims, evidence levels or gate states.

Propagation rule:

`accepted result/decision → impact analysis → RMA → dependent current assets → STATUS → claim/evidence control → consistency audit → next controlled operation`.

Scientific-memory reuse rule:

> The existence of a relevant historical artifact blocks a claim that a new operation starts “from scratch” (from-scratch), unless the operation explicitly records why the artifact is scientifically irrelevant.

**EXT-UPD-3.6 scientific asset reconciliation: CLOSED / CONSISTENT.**

**D-OPS-24 is the next controlled operation and is released to continue its controlled preflight sequence. Real-data execution remains NOT AUTHORIZED.**
