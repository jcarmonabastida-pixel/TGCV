# TGCV — Registro Maestro de Activos (RMA) v0.3

**Estado:** CURRENT / OPERATIVE  
**Fecha:** 2026-09-08  
**Predecesor:** `00_GOVERNANCE/rma/TGCV_RMA_v0.2.md`  
**Governance basis:** DR-044 + RMA Governance Reconciliation Audit v0.1  
**Purpose:** current master register of assets, dependencies, epistemic states, evidence and propagation obligations.

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

RUST-DYN-2 recorded 516,061 adjacent temporal pairs, 438,203 non-persistent pairs (~84.91%), ND-1=159,921, ND-2=278,282 and ND-4=266,201. Dataset SHA-256 is `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`; pair-evidence SHA-256 is `fdab99039990d0e0a5ab221e6b98e857349048e8a26bf3f6a7ffe6fcd179bad8`.

The mandatory replay was field-identical to the supplied primary result; no byte-level raw-JSON comparison is claimed.

Scientific boundary: no causality, prediction, value, universal validity, originality, H>1 trajectory sufficiency or runtime Cargo reachability.

## 3. Current claim/evidence control

Authoritative current matrix:
`00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_POST_DOPS23_v0.1.md`.

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

D-OPS-15 through D-OPS-20 are closed discovery/rejection/bridge audits. They establish that no execution-ready independent external domain has yet been identified under the current non-circular admissibility, longitudinal-state and public-reproducibility requirements.

No second-domain execution is authorized.

## 5. Contribution boundary

D-OPS-21 established high local redundancy with strong prior-art analogues. D-OPS-22 established bounded translational non-redundancy without proving superiority. D-OPS-23 froze the minimal transversal translation protocol and information-preservation invariants.

Current candidate contribution boundary:

> TGCV may provide a transversal analytical translation architecture for comparing how heterogeneous systems represent, change and relate accessible transformation spaces to downstream Reach, Trajectory, Outcome and context-dependent Value.

This remains a hypothesis and is not a claim of originality or superiority.

## 6. Current controlled operation

**D-OPS-24 is the next controlled operation and is UNBLOCKED FROM RMA GOVERNANCE CONSISTENCY PERSPECTIVE.**

It remains subject to its own historical reconstruction, design, preflight and explicit authorization requirements. No real-data execution is authorized by this RMA.

## 7. Master propagation rule

Every substantive accepted change must propagate through:

`Decision/Gate/Closure → Impact analysis → RMA current master → current dependent assets → STATUS → Evidence-to-Claim Matrix → consistency audit → next gate`.

An asset is not current merely because another document mentions the new state. If unaffected, that must be explicitly recorded in the impact analysis.

## 8. Mandatory impact propagation

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

## 9. State discipline

Document workflow state and epistemic evidence level are separate dimensions.

Workflow states:
`DRAFT → WORKING → REVIEW → FROZEN → SUPERSEDED`.

Historical descriptors may include:
`HISTORICAL / RECOVERED / UNVERIFIED`.

Evidence levels remain E0/E1/E2/H/O/F and are never upgraded by documentation propagation alone.

## 10. Immutability and versioning

- Historical RMA versions are immutable.
- Historical claim matrices are immutable.
- Closed Decision Records and experiment closures are immutable.
- Current pointers may move to a new version.
- Any substantive RMA change creates a new versioned file.
- A correction to a newly created current RMA is itself a new version; the prior version is not silently rewritten.

## 11. Governance invariants

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

## 12. Governance enforcement assets

- Propagation workflow: `00_GOVERNANCE/workflows/CURRENT_STATE_PROPAGATION_AND_CONSISTENCY_WORKFLOW_v0.1.md`
- Machine validator: `00_GOVERNANCE/tools/validate_current_state.py`
- CI workflow: `.github/workflows/governance-current-state.yml`
- Current traceability: `00_GOVERNANCE/rma/TGCV_RMA_traceability_v0.3.csv`

## 13. Current reconciliation status

**RMA v0.3 CURRENT / OPERATIVE.**

The RMA governance chain is considered current only when the validator passes and a consistency closure records the corresponding commit state.
