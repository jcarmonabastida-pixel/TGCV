# TGCV — Evidence-to-Claim Matrix — Current v0.4

**Status:** GOVERNANCE CONTROL ARTIFACT — CURRENT
**Date:** 2026-09-09
**Predecessor:** `EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md` v0.3
**Current update:** C-01 Gate D execution — EXT-UPD-4.4
**Governance basis:** EXT-UPD-4.3 + D-OPS-24_V05_C01_GATE_D_EXECUTION_RESULT_v0.1

## Current claim matrix

| ID | Claim | Status | Current evidence / basis | Evidence impact / interpretation | Next requirement |
|---|---|---|---|---|---|
| C01 | TGCV represents system state/context/conditions and constraints/resources | E0 | Formal TGCV architecture | C-01 provides bounded external instantiation of system state/context in aircraft control reconfiguration; Gate D execution does not change epistemic status. | Cross-domain operational confirmation |
| C02 | Accessibility is represented by transformations satisfying an independently defined admissibility predicate | E0 | Contribution formalization + Rust D-OPS-1 | C-01 A-C supports translation of accessibility as native feasibility-constrained transformation membership; Gate D does not upgrade general validity. | Independent operationalization |
| C03 | `T_acc` is analytically distinct from downstream Reach in bounded Rust | E1 | RUST-DYN-2 ND-1/ND-2 | C-01 preserves the distinction; D1 remains INDETERMINATE and does not replace the bounded Rust evidence. | Independent replication |
| C04 | `ΔT_acc` can occur without `ΔReach¹_pot` | E1 | ND-1 = 159,921 | C-01 Gate D does not empirically test this Rust proposition; no status change. | Independent replication |
| C05 | `ΔT_acc` can occur with `ΔReach¹_pot` change | E1 | ND-2 = 278,282 | C-01 Gate D does not quantitatively test this Rust proposition; no status change. | Independent replication |
| C06 | Reach identity is not characterized by cardinality alone | E1 | ND-4 = 266,201 | C-01 Gate D does not alter the Rust evidence; the extension audit reinforces the distinction but provides no upgrade. | Independent replication / broader semantics |
| C07 | Accessible transformation spaces change over time in Rust | E1 | 438,203 / 516,061 non-persistent pairs | C-01 supplies documentary evidence of changing feasible reconfiguration options; Gate D execution identifies a downstream extension boundary and does not upgrade the bounded Rust claim. | Independent domain replication |
| C08 | Accessibility changes modify reachable future trajectories | H | Formal chain + bounded H=1 Reach | C-01 Gate D is INDETERMINATE: D1 and D2 were not independently operationalized to the required constructive standard. No upgrade. | Valid trajectory test |
| C09 | Accessibility changes causally affect subsequent trajectories | H | No causal identification | C-01 Gate D contains no causal identification. Temporal ordering and engineering feasibility do not establish causality. | Intervention/quasi-experiment |
| C10 | Accessibility changes generate/predict value | H | Value excluded from Rust test | C-01 Gate D leaves Outcome→Value INDETERMINATE; engineering performance is not silently relabeled as TGCV Value. | Value-linked test |
| C11 | TGCV is domain-independent / transversal | H | Cross-domain reconstruction + D-OPS-22/23 + C-01 A-C | C-01 supports the bounded proposition that the Core can be translated to aircraft control-system reconfiguration while preserving essential semantic distinctions. Gate D execution does not establish full downstream transversal validity. | Independent cross-domain operationalization / broader domain evidence |
| C12 | TGCV provides superior explanatory representation | H | D-OPS-22/23 establish bounded translational non-redundancy, not superiority | C-01 Gate D provides no controlled comparison establishing superiority. No upgrade. | Controlled comparative explanatory test |
| C13 | TGCV contains no equivalent prior architecture | O | D-OPS-21: high local redundancy; adaptation-space drift near-direct analogue; full absorption not established | C-01 Gate D is not a comparative originality test. No upgrade. | Targeted comparative coverage |
| C14 | `T_acc` is an ontological primitive independent of `S` | F | TR-131 | C-01 Gate D does not contradict TR-131. | No restoration without contrary evidence |
| C15 | RUST-DYN-2 demonstrates observed Cargo/runtime reachability | F | Reach is potential structural Reach, not runtime execution | C-01 Gate D has no bearing on this Rust-specific false claim. | Separate governed runtime test |
| C16 | TGCV provides a transversal analytical translation protocol preserving distinctions among state, candidate transformations, accessibility, Reach, Trajectory, Outcome and Value | H | D-OPS-22 bounded non-redundancy + D-OPS-23 frozen minimal protocol + C-01 A-C | C-01 supports the Core portion of the protocol. Gate D execution now provides explicit evidence that the downstream extension remains an operational boundary in this domain; no full protocol-conformance claim. | New controlled design/operationalization or independent domain evidence |

## C-01 evidence record

**Evidence item:** C-01 — NASA-CR-172489, *Automatic Control Design Procedures for Restructurable Aircraft Control* (1985).

**Evidence class:** documentary / primary-source translational evidence plus controlled Gate-D operationalization execution.

**Gate A:** PASS — Minimum Translation Eligibility.

**Gate B:** PASS — Translation Readiness.

**Gate C:** PASS — bounded/partial Translation Trace; C1-C5 PASS.

**Gate D:** **INDETERMINATE — extension boundary identified.**

**D1:** INDETERMINATE — constructive Reach/ΔReach could not be established to the required independent standard without relying on the observed redesign case.

**D2:** INDETERMINATE — an independently generated admissible trajectory set could not be established from Reach without promoting observed historical sequence to the trajectory set.

**D3:** PARTIAL SUPPORT — downstream engineering performance/outcome-like observations exist, but the complete preceding trajectory construction is not established; no causal inference.

**D4:** INDETERMINATE — no independent native valuation criterion sufficient to establish Outcome→Value while preserving the Outcome/Value distinction.

**Scientific interpretation:** C-01 continues to support a bounded translation of the TGCV Core analytical distinctions. Gate-D execution shows that the full chain `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value` cannot be claimed from the present source without importing observed transitions, observed trajectories or engineering performance into upstream/value constructs.

## D-OPS-23 consequence

D-OPS-23 does not upgrade any empirical claim. It freezes the minimal translation protocol and establishes explicit information-preservation invariants and anti-renaming criteria.

The protocol requires traceable mappings for `S`, `C`, `L`, `U_tau`, `tau`, `P_tau`, `T_acc`, `Delta T_acc`, `Reach`, `Trajectory`, `Outcome`, and `Value`, while preserving the distinctions:

- state vs transformation;
- candidate universe vs accessible subset;
- accessibility vs execution;
- accessibility vs Reach;
- Reach vs Trajectory;
- Outcome vs Value.

## Gate state

- G1 Independent replication: OPEN.
- G2 Cross-domain generalisation: OPEN.
- G3 Trajectory sufficiency: OPEN.
- G4 Causal identification: OPEN.
- G5 Value linkage: OPEN.
- G6 Originality/comparative architecture: BOUNDED / PARTIAL.
- G7 Transversal translation protocol: **C-01 A-C PASS / Gate D INDETERMINATE — extension boundary identified.**

## Current scientific position

E1 evidence exists for the bounded Rust distinction between changing accessible transformations and changing potential Reach. D-OPS-21 through D-OPS-23 narrow the candidate contribution toward a transversal translation protocol. C-01 adds bounded documentary evidence that the TGCV Core distinctions can be translated to an external aircraft control-system reconfiguration domain while preserving their essential semantic roles. The Gate-D execution identifies a concrete extension boundary: the downstream Reach/Trajectory/Outcome/Value chain is not established under the current independent operationalization criteria. Superiority, originality, empirical cross-domain generalisation, causality, prediction and value creation remain unestablished.

## Next controlled operation

**New explicit governance decision required before any further attempt to resolve the C-01 Gate-D extension boundary or to open an independent-domain test.**

No second-domain search, new D-OPS QF, causal inference, value optimization or external-asset update is authorized by this matrix.
