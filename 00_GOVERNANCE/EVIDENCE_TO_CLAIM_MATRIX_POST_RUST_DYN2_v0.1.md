# TGCV — Evidence-to-Claim Matrix Post-RUST-DYN-2 v0.2

**Status:** GOVERNANCE CONTROL ARTIFACT — CURRENT
**Date:** 2026-09-08
**Predecessor:** `00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_POST_RUST_DYN2_v0.1.md`
**Purpose:** Reconcile the current TGCV scientific claims with the evidence actually established after RUST-DYN-2 and the subsequent comparative architectural audits, without inflating scope.

## 1. Governing rule

Every substantive scientific claim must be traceable to a definition, an explicit inference, an empirical result, or a hypothesis. No downstream asset may silently upgrade a bounded structural result into a causal, predictive, value, universal or originality claim.

Historical matrices remain immutable. This document supersedes v0.1 only as the current evidence-to-claim control state.

## 2. Evidence levels

- **E0 — Defined:** semantic/model definition; not an empirical claim.
- **E1 — Empirically supported:** directly supported within the frozen operationalization and tested population.
- **E2 — Replication-supported:** independently reproduced under a separately specified operationalization.
- **H — Hypothesis:** requires further empirical testing.
- **O — Open:** insufficiently established or not currently demonstrated.
- **F — Falsified:** contradicted by valid evidence under the relevant scope.

## 3. Current claim matrix

| ID | Claim | Status | Current evidence / basis | Remaining requirement / next gate |
|---|---|---|---|---|
| C01 | TGCV can represent a system through state/context/conditions and constraints/resources at the analytical level | E0 | Formalized TGCV architecture | Cross-domain empirical/operational confirmation |
| C02 | Accessibility can be represented as a set of transformations satisfying an independently defined admissibility predicate | E0 | Contribution formalization + Rust D-OPS-1 | Independent operationalization in another domain |
| C03 | `T_acc` is analytically distinct from downstream Reach in the bounded Rust representation | E1 | RUST-DYN-2 ND-1/ND-2 | External-domain replication |
| C04 | `ΔT_acc` can occur without `ΔReach¹_pot` | E1 | ND-1 = 159,921 temporal pairs | Independent replication |
| C05 | `ΔT_acc` can occur together with `ΔReach¹_pot` change | E1 | ND-2 = 278,282 temporal pairs | Independent replication |
| C06 | Reach identity cannot be characterized by cardinality alone | E1 | ND-4 = 266,201 pairs with equal cardinality but different membership | Independent replication / broader Reach semantics |
| C07 | Accessible transformation spaces can change over time in a real generative/technical ecosystem | E1 | 438,203 non-persistent of 516,061 adjacent Rust pairs (~84.91%) | External-domain replication |
| C08 | Changes in accessibility modify reachable future trajectories | H | Formal architecture + bounded H=1 Reach evidence | Valid trajectory test; H>1 only if independently justified |
| C09 | Accessibility changes causally affect subsequent trajectories | H | No intervention/causal identification | Causal identification / intervention |
| C10 | Accessibility changes can systematically generate or predict value | H | Programme objective; outcome/value excluded from RUST-DYN-2 | Value-linked empirical test |
| C11 | TGCV is domain-independent / transversal | H | Cross-domain structural reconstruction and translational analysis only; no independent empirical generalisation | Independent cross-domain operationalization |
| C12 | TGCV provides a superior explanatory representation relative to relevant alternatives | H | D-OPS-22 establishes bounded translational non-redundancy, not superiority | Controlled comparative explanatory test |
| C13 | TGCV contains no equivalent prior architecture | O | D-OPS-21 found high local redundancy and a near-direct analogue in adaptation-space drift; full architectural absorption still not established | Further targeted comparative coverage; no absolute novelty claim |
| C14 | `T_acc` is an ontological primitive independent of `S` | F | TR-131 establishes analytical indispensability but not ontological independence | No restoration unless future evidence overturns TR-131 |
| C15 | RUST-DYN-2 demonstrates observed Cargo/runtime reachability | F | Experiment explicitly uses `Reach¹_pot`, not runtime execution | Requires a separately governed execution/outcome design |
| C16 | TGCV provides a transversal analytical translation protocol that preserves distinctions among state, candidate transformations, accessibility, Reach, Trajectory, Outcome and Value across heterogeneous domain constructs | H | D-OPS-22 bounded translational non-redundancy analysis | D-OPS-23 minimal protocol + information-preservation/falsification test |

## 4. Empirical evidence now accepted

RUST-DYN-2 / EXEC-1A is closed as a bounded structural empirical test. Frozen dataset SHA-256:

`823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`

Frozen temporal rule:

`DR-035-v0.1-ADJACENT-CREATED-AT`

Horizon:

`H=1`

Temporal population:

`516,061` adjacent package-version pairs.

Classification:

- PERSISTENCE: 77,858
- EXPANSION: 8,295
- CONTRACTION: 3,786
- RECONFIGURATION: 426,122

Non-persistence:

`438,203 / 516,061 ≈ 84.91%`

Downstream distinction:

- ND-1: `159,921` pairs with `ΔT_acc ≠ 0` and `ΔReach¹_pot = 0`.
- ND-2: `278,282` pairs with `ΔT_acc ≠ 0` and `ΔReach¹_pot ≠ 0`.
- ND-4: `266,201` pairs with equal Reach cardinality but different Reach membership.

Primary/replay structured outputs were field-identical; the closure explicitly does not claim byte-level raw-file comparison because independent raw JSON artifacts were not supplied during coordination. The experiment's firewall reports no sampling, outcome/value/future/predictive/Cargo-runtime/lockfile access.

## 5. Scientific interpretation rule

The current strongest empirical claim is **bounded structural distinguishability between `ΔT_acc` and `ΔReach¹_pot` in the frozen Rust representation**.

The result may support C03–C07 only within the stated operational scope. It must not be rewritten as evidence for:

- causality;
- predictive superiority;
- positive value creation;
- universal domain independence;
- complete prior-art absence;
- observed runtime/Cargo reachability;
- H>1 trajectory sufficiency.

## 6. Comparative architectural evidence now accepted

D-OPS-21 established a high-redundancy prior-art environment around the central accessibility construction, especially self-adaptive adaptation-space drift. It did **not** establish full architectural absorption. Therefore C13 remains open, with a materially higher burden for any originality claim. The defensible residual is the possible transversal synthesis/translation architecture, not invention of changing accessible spaces themselves.

D-OPS-22 established **bounded translational non-redundancy**: the common TGCV mapping is not merely a one-to-one renaming because it preserves explicit typed distinctions among state, transformation universe, accessibility, execution, Reach, Trajectory, Outcome and Value. This is architectural/formal evidence only; it does not establish empirical usefulness, explanatory superiority, originality, causality, prediction or value creation.

## 7. Architecture consequence

The stabilized architecture remains unchanged:

`Core_ontological = S`

`T_acc,t = {τ ∈ Uτ | Pτ(S_t,C_t,L)=1}`

`ΔT_acc(t,t+1) = T_acc,t+1 ≄ T_acc,t`

`mechanism → (S_t,C_t) → (S_t+1,C_t+1) → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

`T_acc` remains a derived analytical structure. `ΔT_acc` remains the central comparative object. `Reach¹_pot` is downstream and bounded; it is not an ontological primitive.

## 8. Evidence gates and current state

### G1 — Independent replication

**OPEN.** Test whether the bounded distinction between `ΔT_acc` and downstream Reach survives a separately specified operationalization and dataset.

### G2 — Cross-domain generalisation

**OPEN.** Test the same analytical architecture in an external domain without importing Rust-specific semantics. Current external-domain search is closed because no execution-ready candidate has been identified.

### G3 — Trajectory sufficiency

**OPEN.** Test whether Reach differences translate into non-redundant trajectory differences, with explicit treatment of H=1 versus any justified H>1 extension.

### G4 — Causal identification

**OPEN.** Determine whether accessibility changes can be identified as causes of downstream trajectory or outcome changes under an intervention or valid quasi-experimental design.

### G5 — Value linkage

**OPEN.** Determine whether accessibility/trajectory changes translate into measurable context-dependent outcomes or value; do not use value retrospectively to define accessibility.

### G6 — Originality / comparative architecture

**BOUNDED / PARTIAL.** D-OPS-21 materially weakens the broad novelty narrative; D-OPS-22 identifies bounded translational non-redundancy as the narrower surviving candidate contribution.

### G7 — Transversal translation protocol

**OPEN / NEXT.** Freeze the minimum common translation protocol and define machine-checkable or traceable falsifiers for semantic loss, hidden assumptions and trivial renaming.

## 9. Priority rule for next work

The next operation must be selected by scientific information gain, not by extending the existing Rust execution merely because data and code are available.

Before any new gate, perform historical-state reconstruction and verify whether the proposed question is already answered by an existing formal or empirical artifact.

Current priority: **D-OPS-23 — Minimal Transversal Translation Protocol & Information-Preservation Gate.**

## 10. Current scientific position

**Bounded positive empirical evidence exists for the analytical distinction between changing accessible transformations and changing bounded potential Reach in the Rust operationalization. Comparative architectural analysis now supports a narrower candidate contribution—bounded translational non-redundancy—but does not establish superiority, originality, cross-domain empirical validity, causality, prediction or value creation.**

The external-domain discovery programme is closed for the current evidence base. A second empirical domain may only be reopened if an independently governed rule/constraint system, finite transformation universe, non-circular accessibility predicate and public longitudinal state archive become available and pass the corresponding gates.
