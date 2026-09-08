# Changelog

## 2026-09-09

- Reconciled a post-closure governance inconsistency identified after EXT-UPD-3.6: immutable RMA v1.1 and dependent current-control surfaces still contained pre-closure wording.
- Created `00_GOVERNANCE/impact/EXT-UPD-3.6_POST_CLOSURE_RECONCILIATION_v0.1.md` documenting the discrepancy and corrective decision.
- Created immutable `00_GOVERNANCE/rma/TGCV_RMA_v1.2.md` as the corrected current RMA; v1.1 remains historical and immutable.
- Created `00_GOVERNANCE/rma/TGCV_RMA_traceability_v1.2.csv` and moved the current dependency map to v1.2.
- Moved `TGCV_RMA_current.md` to v1.2 and synchronized `STATUS.md` with the closed/consistent EXT-UPD-3.6 state.
- D-OPS-24 is released to continue its controlled preflight sequence; real-data execution remains NOT AUTHORIZED.
- No scientific claims, evidence levels, empirical results, Core propositions or gate closures changed through this reconciliation.

- Opened `EXT-UPD-3.3.5_VP_PROPAGATION_v0.1.md` and accepted Vision Paper v0.2 propagation into the current canonical external-asset state.
- Created `00_GOVERNANCE/rma/TGCV_RMA_v0.6.md` as the new immutable current RMA master; v0.5 remains historical.
- Created `00_GOVERNANCE/rma/TGCV_RMA_traceability_v0.6.csv` and moved the current dependency map to v0.6.
- Moved `TGCV_RMA_current.md` to v0.6 and synchronized the current pointer with Vision Paper v0.2.
- Updated `STATUS.md` to record Vision Paper v0.2 as the current controlled draft and EXT-UPD-3.3.5 as the current propagation.
- Updated `validate_current_state.py` to validate RMA v0.6, traceability v0.6 and the Vision Paper propagation impact.
- Closed EXT-UPD-3.3.5 consistency without fabricating a CI PASS where no status check was observable.
- Created `EXT-UPD-3.4_ARM_HISTORICAL_RECONSTRUCTION_v0.1.md`; no substantive historical ARM artifact was found.
- Created `TGCV-EXT-ARM-001_v0.1.md` as the first substantive canonical ARM controlled draft.
- Opened `EXT-UPD-3.4_ARM_PROPAGATION_v0.1.md` and propagated ARM v0.1 through the current governance surfaces.
- Created RMA v0.7 and traceability v0.7, then finalized the propagation in immutable RMA v0.8 and traceability v0.8.
- Moved the RMA current pointer to v0.8 and synchronized STATUS with ARM v0.1 and EXT-UPD-3.4.
- Updated `validate_current_state.py` to validate RMA v0.8, traceability v0.8, ARM v0.1 and the ARM propagation impact.
- No scientific claims, evidence levels, gate states or historical scientific artefacts were changed by ARM creation/propagation.
- Created `EXT-UPD-3.5_RII_HISTORICAL_RECONSTRUCTION_v0.1.md`; historical/preparatory impact-roadmap material was identified and retained without promotion.
- Created `TGCV-EXT-RII-001_v0.1.md` as the first substantive canonical RII controlled draft, excluding obsolete EMP-1.1 predictive/readiness framing.
- Opened `EXT-UPD-3.5_RII_PROPAGATION_v0.1.md` and advanced the current RMA through v0.9 to final immutable v1.0 and traceability v1.0.
- Moved the RMA current pointer to v1.0 and synchronized STATUS with RII v0.1 and EXT-UPD-3.5.
- Updated `validate_current_state.py` to validate RMA v1.0 and traceability v1.0.
- GitHub Actions governance-current-state run 81 for the pre-finalization propagation commit completed successfully; the final-state commits subsequently completed the same canonical propagation chain.
- No scientific claims, evidence levels, gate states or historical scientific artefacts were changed by RII creation/propagation.
- EXT-UPD-3.5 RII propagation is CLOSED / CONSISTENT. D-OPS-24 remains the next controlled operation and is not an execution authorization.
- EXT-UPD-3.6 identified a scientific-memory/reuse-control gap: substantive historical `TGCV_*` scientific artifacts were present in `02_LITERATURE/` and were not surfaced through a canonical reusable-science registry before later work.
- Created `02_EXTERNAL_SCIENCE/SCIENTIFIC_ASSET_REGISTRY_v0.1.md` as the canonical registry/integration surface; fourteen substantive historical `TGCV_*` artifacts are initially registered without physical migration or epistemic upgrade.
- Created `00_GOVERNANCE/impact/EXT-UPD-3.6_SCIENTIFIC_ASSET_RECONCILIATION_v0.1.md` documenting the finding, reconciliation decision and propagation obligations.
- Advanced the immutable RMA to v1.1 and traceability to v1.1; current pointer and STATUS now identify EXT-UPD-3.6 and the scientific-memory registry.
- Established the normative reuse rule: a relevant historical artifact blocks a “from-scratch” claim unless its scientific irrelevance is explicitly justified.
- No scientific claims, evidence levels or gate states changed through EXT-UPD-3.6; D-OPS-24 is held pending consistency closure.

## 2026-09-08

- Confirmed GitHub canonical continuity is operational through direct repository reads/writes.
- Completed RMA Governance Reconciliation Audit v0.1 and accepted the current-state propagation workflow.
- Accepted DR-045 closing governance conformance and establishing the propagation chain as operational.
- Advanced the current RMA to `00_GOVERNANCE/rma/TGCV_RMA_v0.4.md`; `TGCV_RMA_current.md` now points to v0.4 and `TGCV_RMA_traceability_v0.4.csv` is the current dependency map.
- Synchronized the external-asset surface and normalised the IE PhD Research Prospectus adaptation.
- Created `TGCV-EXT-RP-001_v0.1.md` as the current generic Research Prospectus controlled draft under `05_ASSETS/Research_Prospectus/`.
- Recorded EXT-UPD-3.1 controlled drafting and consistency review.
- Propagated RP v0.1 into the then-current RMA v0.4, traceability and STATUS; this historical propagation is preserved and is not rewritten.
- Opened EXT-UPD-3.2 and created `TGCV-EXT-TCP-001_v0.3.md` as the current controlled TCP draft.
- Identified a versioning defect in the prior RP propagation: a substantive RMA change had been applied to v0.4 instead of creating a new version. The correction is represented by new RMA v0.5; v0.4 history is preserved.
- Created `00_GOVERNANCE/rma/TGCV_RMA_v0.5.md` as the correctly versioned current RMA master and `TGCV_RMA_traceability_v0.5.csv` as its dependency map.
- Moved `TGCV_RMA_current.md` to v0.5 and synchronized `STATUS.md` with RMA v0.5 and TCP v0.3.
- Opened `EXT-UPD-3.2_TCP_PROPAGATION_v0.1.md` for TCP propagation control.
- No scientific claims, evidence levels, gate states or historical scientific artefacts were changed by this propagation/correction.
- D-OPS-24 remains the next controlled operation and is not an execution authorization.

## 2026-08-27

- Bootstrapped the canonical TGCV repository structure.
- Added governance, core, literature, experiments, RMA, assets, applications, code and data-manifest areas.
- Recorded the EXT-1.1 identifiability/privacy gate.
- Marked EXT-1.1 as not frozen until the gate and exact-dataset verification are completed.
