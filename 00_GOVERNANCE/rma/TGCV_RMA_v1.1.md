# TGCV — Registro Maestro de Activos (RMA) v1.1

**Estado:** CURRENT / OPERATIVE  
**Fecha:** 2026-09-09  
**Predecesor:** `00_GOVERNANCE/rma/TGCV_RMA_v1.0.md`  
**Governance basis:** DR-044 + DR-045 + EXT-UPD-1R.4 + EXT-UPD-3.1 + EXT-UPD-3.2 + EXT-UPD-3.3.5 + EXT-UPD-3.4 + EXT-UPD-3.5 + EXT-UPD-3.6  
**Purpose:** current master register of assets, dependencies, epistemic states, evidence and propagation obligations, including canonical scientific-memory/reuse control.

## 1. Canonical current state

GitHub is the canonical continuity/provenance surface of TGCV.

Current conceptual architecture:

- `Core_ontological = S`
- `T_acc,t = {τ ∈ Uτ | Pτ(S_t,C_t,L)=1}`
- `ΔT_acc(t,t+1) = T_acc,t+1 ≄ T_acc,t`
- `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`
- `I` = explanatory mechanism, not Core primitive.

TR-131 is closed. RUST-DYN-1 is closed. RUST-DYN-2 / EXEC-1A is closed as bounded structural empirical evidence. No result has reopened or altered the Core.

## 2. Current empirical evidence state

- EXT-1.0 / CollegeMsg: historical negative result, retained unchanged.
- TGCV-EMP-1.1: historical computational programme, frozen and distinct from EXT-1.1.
- EXT-1.1 Rust / RUST-DYN-1: closed bounded dynamic evidence.
- EXT-1.1 Rust / RUST-DYN-2 / EXEC-1A: closed bounded structural empirical evidence.

RUST-DYN-2 recorded 516,061 adjacent temporal pairs, 438,203 non-persistent pairs (~84.91%), ND-1=159,921, ND-2=278,282 and ND-4=266,201. Dataset SHA-256 is `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`; pair-evidence SHA-256 is `fdab99039990d0a5ab221e6b98e857349048e8a26bf3f6a7ffe6fcd179bad8`.

Scientific boundary: no causality, prediction, value, universal validity, originality, H>1 trajectory sufficiency or runtime Cargo reachability.

## 3. Current claim/evidence control

Authoritative current matrix: `00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_POST_DOPS23_v0.1.md`.

- C01–C02: E0;
- C03–C07: E1 within frozen Rust operationalization;
- C08–C12: H;
- C13: O;
- C14–C15: F within scope;
- C16: H.

Gate state:

- G1 independent replication: OPEN;
- G2 cross-domain generalisation: OPEN; no execution-ready external domain currently identified;
- G3 trajectory sufficiency: OPEN;
- G4 causal identification: OPEN;
- G5 value linkage: OPEN;
- G6 originality/comparative architecture: BOUNDED/PARTIAL;
- G7 transversal translation protocol: FROZEN / D-OPS-24 NEXT.

## 4. External-domain discovery state

D-OPS-15 through D-OPS-20 are closed discovery/rejection/bridge audits. No execution-ready independent external domain has been identified under the current strict admissibility requirements.

No second-domain execution is authorized.

## 5. Contribution boundary

D-OPS-21 established high local redundancy with strong prior-art analogues. D-OPS-22 established bounded translational non-redundancy without proving superiority. D-OPS-23 froze the minimal transversal translation protocol and information-preservation invariants.

Current candidate contribution boundary:

> TGCV may provide a transversal analytical translation architecture for comparing how heterogeneous systems represent, change and relate accessible transformation spaces to downstream Reach, Trajectory, Outcome and context-dependent Value.

This remains a hypothesis and is not a claim of originality or superiority.

## 6. Current controlled operation

**D-OPS-24 is the next controlled operation.**

It remains subject to its own historical reconstruction, design, preflight and explicit authorization requirements. No real-data execution is authorized by this RMA.

## 7. Canonical external-asset surface

`05_ASSETS/` is the single canonical physical surface for external-facing deliverable families.

- `TGCV-EXT-TCP-001` → `05_ASSETS/TCP/` — current `TGCV-EXT-TCP-001_v0.3.md`
- `TGCV-EXT-VP-001` → `05_ASSETS/Vision_Paper/` — current `TGCV-EXT-VP-001_v0.2.md`
- `TGCV-EXT-RP-001` → `05_ASSETS/Research_Prospectus/` — current `TGCV-EXT-RP-001_v0.1.md`
- `TGCV-EXT-ARM-001` → `05_ASSETS/ARM/` — current `TGCV-EXT-ARM-001_v0.1.md`
- `TGCV-EXT-RII-001` → `05_ASSETS/RII/` — current `TGCV-EXT-RII-001_v0.1.md`
- `TGCV-EXT-MOI-001` → `05_ASSETS/MOI/` — RESERVED; substantive creation deferred

## 8. Canonical scientific-memory surface

`02_EXTERNAL_SCIENCE/` is the canonical registry/integration surface for reusable research-bearing scientific artifacts.

Current registry:

`02_EXTERNAL_SCIENCE/SCIENTIFIC_ASSET_REGISTRY_v0.1.md`

`02_LITERATURE/` remains the historical SLR working/archive surface. Historical scientific gates, audits and operational specifications may remain physically there while being discoverable through the registry.

The current registry records fourteen substantive historical `TGCV_*` artifacts from `02_LITERATURE/` whose prior reasoning may materially affect future work.

## 9. Scientific reuse / anti-redundancy rule

Before any new scientific gate, audit, experiment, domain selection, dataset search, operationalisation, cross-domain translation or technical feasibility study, the investigator must consult:

1. current and relevant historical `00_GOVERNANCE/` control surfaces;
2. `02_EXTERNAL_SCIENCE/SCIENTIFIC_ASSET_REGISTRY_v0.1.md`;
3. `02_LITERATURE/` when indicated by the registry or research question.

Normative rule:

> The existence of a relevant historical artifact blocks a claim that a new operation starts “from scratch”, unless the operation explicitly records why that artifact is scientifically irrelevant.

If a prior artifact is reconstructed, refined, replaced or independently revalidated, that relationship must be stated explicitly rather than treating the prior artifact as nonexistent.

Registration does not upgrade evidence, claim strength, closure state or epistemic level.

## 10. Master propagation rule

Every substantive accepted change must propagate through:

`Decision/Gate/Closure → Impact analysis → RMA current master → current dependent assets → STATUS → Evidence-to-Claim Matrix → consistency audit → next gate`.

For scientific-memory changes, the sequence additionally requires registry reconciliation before final consistency closure.

## 11. Mandatory impact propagation

For every accepted substantive Decision, Gate or Closure:

1. reconstruct relevant historical state;
2. identify changed scientific/governance propositions;
3. create an impact analysis against the RMA dependency graph;
4. update or explicitly exempt every affected current asset;
5. update the RMA master and current pointer;
6. update STATUS;
7. update claim/evidence control when claim evidence or epistemic status changes;
8. record the change in CHANGELOG;
9. run the machine consistency validator;
10. create a consistency closure before opening the next gate.

## 12. State discipline

Document workflow state and epistemic evidence level are separate dimensions.

Workflow states: `DRAFT → WORKING → REVIEW → FROZEN → SUPERSEDED`.

Evidence levels remain E0/E1/E2/H/O/F and are never upgraded by documentation propagation alone.

## 13. Immutability and versioning

- Historical RMA versions are immutable.
- Historical claim matrices are immutable.
- Closed Decision Records and experiment closures are immutable.
- Current pointers may move to a new version.
- Any substantive RMA change creates a new versioned file.
- A correction to a newly created current RMA is itself a new version.

## 14. Governance invariants

1. GitHub is canonical.
2. Historical reconstruction precedes new work.
3. Reuse precedes recreation.
4. No silent semantic replacement.
5. Evidence state is never inflated by document propagation alone.
6. Experimental results cannot retrospectively redefine the Core.
7. Application material cannot redefine scientific ontology.
8. Current control surfaces must agree with the latest accepted state.
9. A new gate is blocked while the current-state chain is inconsistent.
10. A gate becomes open only after consistency closure.
11. The machine validator is a control aid, not a substitute for scientific judgement.
12. External deliverable identity is determined by `TGCV-EXT-*` identity and canonical location, not historical filename.
13. Relevant historical scientific artifacts must be discoverable through the canonical scientific registry before new scientific work.
14. A “from-scratch” claim requires explicit prior-art/reuse review.
15. Registry inclusion does not constitute scientific validation or epistemic upgrade.

## 15. Governance enforcement assets

- Propagation workflow: `00_GOVERNANCE/workflows/CURRENT_STATE_PROPAGATION_AND_CONSISTENCY_WORKFLOW_v0.1.md`
- Historical reconstruction workflow: `00_GOVERNANCE/workflows/HISTORICAL_RECONSTRUCTION_BEFORE_NEW_WORK_RULE_v0.1.md`
- Scientific registry: `02_EXTERNAL_SCIENCE/SCIENTIFIC_ASSET_REGISTRY_v0.1.md`
- Machine validator: `00_GOVERNANCE/tools/validate_current_state.py`
- CI workflow: `.github/workflows/governance-current-state.yml`
- Current traceability: `00_GOVERNANCE/rma/TGCV_RMA_traceability_v1.1.csv`

## 16. Current reconciliation status

**RMA v1.1 CURRENT / OPERATIVE — EXT-UPD-3.6 scientific asset reconciliation recorded; final consistency closure pending.**

EXT-UPD-3.6 introduces no scientific claim, evidence-level or gate-state change. It regularises scientific memory and reuse control after discovery of substantive historical `TGCV_*` artifacts in the SLR archive.

D-OPS-24 remains held until EXT-UPD-3.6 propagation and consistency closure are complete.
