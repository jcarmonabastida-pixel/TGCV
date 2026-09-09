# TGCV — Evidence-to-Claim Matrix — Current v0.3

**Status:** GOVERNANCE CONTROL ARTIFACT — CURRENT
**Date:** 2026-09-09
**Predecessor:** `EVIDENCE_TO_CLAIM_MATRIX_POST_DOPS23_v0.1.md`
**Current update:** C-01 — EXT-UPD-4.3
**Governance basis:** `EXT-UPD-4.3_EVIDENCE_CLAIM_PROPAGATION_GOVERNANCE_CORRECTION_v0.1.md`

## Current claim matrix

| ID | Claim | Status | Current evidence / basis | Evidence impact / interpretation | Next requirement |
|---|---|---|---|---|---|
| C01 | TGCV represents system state/context/conditions and constraints/resources | E0 | Formal TGCV architecture | C-01 provides a bounded external instantiation of system state/context in aircraft control reconfiguration; no change to epistemic status. | Cross-domain operational confirmation |
| C02 | Accessibility is represented by transformations satisfying an independently defined admissibility predicate | E0 | Contribution formalization + Rust D-OPS-1 | C-01 Gate A/B/C independently supports translation of accessibility as native feasibility-constrained transformation membership; no upgrade of general validity. | Independent operationalization |
| C03 | `T_acc` is analytically distinct from downstream Reach in bounded Rust | E1 | RUST-DYN-2 ND-1/ND-2 | C-01 preserves the same analytical distinction in a second native representation at documentary level; it does not replace or extend the bounded Rust empirical evidence. | Independent replication |
| C04 | `ΔT_acc` can occur without `ΔReach¹_pot` | E1 | ND-1 = 159,921 | C-01 is not an empirical test of this Rust proposition; no status change. Its Gate C trace nevertheless preserves the distinction needed for future cross-domain testing. | Independent replication |
| C05 | `ΔT_acc` can occur with `ΔReach¹_pot` change | E1 | ND-2 = 278,282 | C-01 does not quantitatively test this Rust proposition; no status change. | Independent replication |
| C06 | Reach identity is not characterized by cardinality alone | E1 | ND-4 = 266,201 | C-01 does not alter the Rust evidence; its translation trace explicitly avoids identifying accessibility with downstream reachable-set cardinality. | Independent replication / broader semantics |
| C07 | Accessible transformation spaces change over time in Rust | E1 | 438,203 / 516,061 non-persistent pairs | C-01 supplies documentary evidence of changing feasible reconfiguration options across ordered engineering configurations, but does not upgrade the bounded Rust claim or establish cross-domain generalisation. | Independent domain replication |
| C08 | Accessibility changes modify reachable future trajectories | H | Formal chain + bounded H=1 Reach | C-01 Gate D is INDETERMINATE: Reach and Trajectory links were not independently operationalized. No upgrade. | Valid trajectory test |
| C09 | Accessibility changes causally affect subsequent trajectories | H | No causal identification | C-01 contains no causal identification. Temporal ordering and engineering feasibility do not establish causality. | Intervention/quasi-experiment |
| C10 | Accessibility changes generate/predict value | H | Value excluded from Rust test | C-01 documents engineering objectives/performance but does not establish a distinct TGCV Value construct or an auditable Outcome→Value mapping. | Value-linked test |
| C11 | TGCV is domain-independent / transversal | H | Cross-domain reconstruction + D-OPS-22/23 architectural translation evidence; C-01 Gates A-C PASS as bounded documentary translation evidence | **C-01 supports the bounded proposition that the TGCV Core can be translated to an external domain of aircraft control-system reconfiguration while preserving the essential semantic distinctions among system state, candidate transformations, accessibility and change in accessible transformation membership.** This is translational support, not empirical cross-domain generalisation. | Independent cross-domain operationalization / broader domain evidence |
| C12 | TGCV provides superior explanatory representation | H | D-OPS-22/23 establish bounded translational non-redundancy, explicitly not superiority | C-01 demonstrates a bounded translation trace but provides no controlled comparison establishing superiority. No upgrade. | Controlled comparative explanatory test |
| C13 | TGCV contains no equivalent prior architecture | O | D-OPS-21: high local redundancy; adaptation-space drift near-direct analogue; full absorption not established | C-01 is a translation evidence item, not a comparative originality test. No upgrade. | Targeted comparative coverage |
| C14 | `T_acc` is an ontological primitive independent of `S` | F | TR-131 | C-01 does not contradict TR-131; its translation instead treats accessibility as analytically dependent on native system/context constraints. | No restoration without contrary evidence |
| C15 | RUST-DYN-2 demonstrates observed Cargo/runtime reachability | F | Reach is potential structural Reach, not runtime execution | C-01 has no bearing on this Rust-specific false claim. | Separate governed runtime test |
| C16 | TGCV provides a transversal analytical translation protocol preserving distinctions among state, candidate transformations, accessibility, Reach, Trajectory, Outcome and Value | H | D-OPS-22 bounded non-redundancy + D-OPS-23 frozen minimal protocol + C-01 Gates A-C PASS | **C-01 provides bounded documentary support for the Core portion of the protocol: state, candidate transformation universe, accessibility and `ΔT_acc` can be mapped into aircraft control reconfiguration without collapsing the semantic distinctions. Gate D remains INDETERMINATE because the downstream chain through Reach, Trajectory, Outcome and Value is not yet established.** | D-OPS-24 C-01 Gate-D operationalization test |

## C-01 evidence record

**Evidence item:** C-01 — NASA-CR-172489, *Automatic Control Design Procedures for Restructurable Aircraft Control* (1985).

**Evidence class:** documentary / primary-source translational evidence.

**Gate A:** PASS — Minimum Translation Eligibility.

**Gate B:** PASS — Translation Readiness.

**Gate C:** PASS — bounded/partial Translation Trace; C1-C5 PASS.

**Gate D:** INDETERMINATE — downstream extension not established.

**Scientific interpretation:** The source provides a native engineering domain in which aircraft/control-system states, candidate restructuring/reconfiguration operations, native feasibility constraints, and resulting feasible configuration options can be distinguished without defining accessibility by downstream performance. C-01 therefore supports a bounded translation of the TGCV Core analytical distinctions. It does not establish that the full chain `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value` has been operationalized.

## D-OPS-23 consequence

D-OPS-23 does not upgrade any empirical claim. It freezes the minimal translation protocol and establishes explicit information-preservation invariants and anti-renaming criteria.

The protocol requires traceable mappings for `S`, `C`, `L`, `U_tau`, `tau`, `P_tau`, `T_acc`, `Delta T_acc`, `Reach`, `Trajectory`, `Outcome`, and `Value`, while preserving the distinctions:

- state vs transformation;
- candidate universe vs accessible subset;
- accessibility vs execution;
- accessibility vs Reach;
- Reach vs Trajectory;
- Outcome vs Value.

The mandatory translation trace is:

`native_construct -> TGCV_object -> semantic_definition -> evidence_source -> assumptions -> admissibility_rule -> canonical_identity -> transformation_membership -> downstream_mapping -> unresolved_items`

## Gate state

- G1 Independent replication: OPEN.
- G2 Cross-domain generalisation: OPEN.
- G3 Trajectory sufficiency: OPEN.
- G4 Causal identification: OPEN.
- G5 Value linkage: OPEN.
- G6 Originality/comparative architecture: BOUNDED / PARTIAL.
- G7 Transversal translation protocol: **C-01 A-C PASS / Gate D INDETERMINATE — Gate-D operationalization next.**

## Current scientific position

E1 evidence exists for the bounded Rust distinction between changing accessible transformations and changing potential Reach. D-OPS-21 through D-OPS-23 narrow the candidate contribution toward a transversal translation protocol. C-01 adds bounded documentary evidence that the TGCV Core distinctions can be translated to an external aircraft control-system reconfiguration domain while preserving their essential semantic roles. The downstream chain through Reach, Trajectory, Outcome and Value remains indeterminate. Superiority, originality, empirical cross-domain generalisation, causality, prediction and value creation remain unestablished.

## Next controlled operation

**D-OPS-24 / C-01 Gate-D operationalization design audit and preflight.**

No empirical execution, second-domain search, causal inference or value test is authorized by this matrix.
