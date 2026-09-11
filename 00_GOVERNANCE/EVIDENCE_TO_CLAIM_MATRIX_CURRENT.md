# TGCV — Evidence-to-Claim Matrix — Current v1.1

**Status:** GOVERNANCE CONTROL ARTIFACT — CURRENT  
**Date:** 2026-09-11  
**Predecessor:** v1.0  
**Current update:** Material evidence propagation for IUT-A-01 U2 FULL_PILOT 001, IT-NOSD-010 IT-G2, and EXT-UPD-4.8 O3 accessibility-closure reassessment. No scientific claim status/level upgrade.

## Material evidence propagation rule
A material experimental result is propagated to this matrix when it adds, removes, qualifies, bounds, or otherwise changes the evidentiary basis or interpretation of a claim, even when no claim status/level changes. Claim upgrade is a separate decision and is never inferred merely from evidence propagation.

**Operational rule:** A material experimental result is propagated to this matrix when it adds, removes, qualifies, bounds, or otherwise changes the evidentiary basis or interpretation of a claim. Claim upgrade is a separate decision. Evidence propagation does not imply claim upgrade.

| ID | Claim | Status | Current evidence / basis | Evidence impact / interpretation | Next requirement |
|---|---|---|---|---|---|
| C01 | TGCV represents system state/context/conditions and constraints/resources | E0 | Formal architecture + bounded cross-domain traces | IUT, IT-NOSD and EXT-UPD-4.8 provide bounded methodological evidence, but no claim-level upgrade. | Further independent operational confirmation |
| C02 | Accessibility is represented by transformations satisfying an independently defined admissibility predicate | E0 | Formalization + Rust + C-01 A-C + I-01 Gate C + IT-NOSD-010 G0/G1/G2 + EXT-UPD-4.8 | IT-NOSD closes bounded accessibility reconstruction for one event; EXT-UPD-4.8 additionally demonstrates that a native candidate definition does not by itself close decision-time accessibility when material conditions remain unresolved. General T_acc remains unclosed. | Independent operationalization with closed accessible transformation space |
| C03 | T_acc is analytically distinct from downstream Reach in bounded Rust | E1 | Rust evidence | IT-NOSD adds bounded empirical separation of accessibility from downstream evidence; EXT-UPD-4.8 does not alter the Rust claim level. | Independent replication |
| C04 | ΔT_acc can occur without ΔReach¹_pot | E1 | Rust ND-1 | No direct test by IUT, IT-NOSD or EXT-UPD-4.8. | Independent replication |
| C05 | ΔT_acc can occur with ΔReach¹_pot change | E1 | Rust ND-2 | No direct test by IUT, IT-NOSD or EXT-UPD-4.8. | Independent replication |
| C06 | Reach identity is not characterized by cardinality alone | E1 | Rust ND-4 | No direct impact. | Independent replication |
| C07 | Accessible transformation spaces change over time in Rust | E1 | Rust non-persistent pairs | IT-NOSD reconstructs one bounded state transition; EXT-UPD-4.8 does not establish the general Rust claim. | Independent closed operationalization |
| C08 | Accessibility changes modify reachable future trajectories | H | Formal chain + bounded Rust H=1 | IT-NOSD closes bounded downstream separation/reconstructability for one event; EXT-UPD-4.8 identifies an accessibility-closure boundary but does not identify trajectory effects. | Valid trajectory test |
| C09 | Accessibility changes causally affect subsequent trajectories | H | No causal identification | IUT, IT-NOSD and EXT-UPD-4.8 do not establish causality. | Causal design |
| C10 | Accessibility changes generate/predict value | H | No Value evidence | IUT is bounded decision-performance evidence; IT-NOSD is bounded reconstructability evidence; EXT-UPD-4.8 is bounded accessibility-closure evidence. None establishes value realization. | Value-linked test |
| C11 | TGCV is domain-independent / transversal | H | C-01 A-C + I-01 Gate C | One bounded 5G case, one frozen decision fixture and one bounded O3 accessibility case do not establish transversal validity. | Independent operationalization across broader domains |
| C12 | TGCV provides superior explanatory representation | H | Comparative evidence absent | IUT M1 shows +40 pp bounded decision correctness in the frozen fixture, but M2 fails; U2-NULL. EXT-UPD-4.8 is non-comparative and does not establish superiority. | Controlled differentiated comparison |
| C13 | TGCV contains no equivalent prior architecture | O | D-OPS-21 | No impact. | Comparative coverage |
| C14 | T_acc is an ontological primitive independent of S | F | TR-131 | No impact. | No restoration without contrary evidence |
| C15 | Rust demonstrates observed Cargo/runtime reachability | F | Rust evidence boundary | No impact. | Separate governed runtime test |
| C16 | TGCV provides a transversal analytical translation protocol preserving distinctions among state, candidate transformations, accessibility, Reach, Trajectory, Outcome and Value | H | D-OPS-22/23 + C-01 A-C + I-01 Gate C + IT-NOSD-010 G0/G1/G2 + EXT-UPD-4.8 | EXT-UPD-4.8 materially qualifies the accessibility-closure boundary: native candidate identification is insufficient where decision-time material conditions are unresolved. It does not close downstream trajectory/value boundaries. | Closed independent-domain operationalization / downstream test |

## Material methodological evidence — IUT-A-01 U2 FULL_PILOT 001

**Case:** `IUT-A-01`  
**Status:** `CLOSED — U2-NULL`

The frozen FULL_PILOT completed with execution integrity `PASS`. M1 decision correctness was `60.0%` control versus `100.0%` TGCV, a `+40.0` percentage-point difference, while M2 failed its predeclared improvement threshold. The overall classification is `U2-NULL`. This is material comparative methodological evidence bounded to Fixture 002 and the executed criteria; it does not upgrade C12 or any other claim.

## Material methodological evidence — IT-NOSD-010

**Case:** `IT-NOSD-010 — ETSI TS 23.502 / 3GPP 5GS`  
**Status:** `IT-G0 CLOSED — BOUNDED PRE-OUTCOME CASE-DEFINITION PASS`; `IT-G1 CLOSED — BOUNDED REPRODUCIBILITY / ADMISSION PASS`; `IT-G2 CLOSED — BOUNDED DOWNSTREAM-SEPARATION PASS`.

The independent G1 and G2 executions reproduced the frozen event, provenance, bounded pre-state, transformation identity, temporal boundary and downstream separation. Accessibility was not reused as outcome evidence, outcome was not used to define post-state, and complete ex-ante enumeration of `T_acc(S_t)` was not required under TR-132-MOD-1. This is material bounded methodological evidence and does not establish complete `T_acc`, utility, causality, value, superiority, transversal validity or scientific validation.

## Material methodological evidence — EXT-UPD-4.8 O3 accessibility closure reassessment

**Case:** `IUT-A-01`; **Option:** `O3`  
**Status:** `CLOSED — INDETERMINATE / H-B — HS-AC01`  
**Execution artifact:** `03_EXPERIMENTS/IUT-A-01/IUT_A01_O3_ACCESSIBILITY_CLOSURE_RESULT_001.json`  
**Governance closure:** `00_GOVERNANCE/D-OPS-24_EXT-UPD-4.8_STAGE_B_ACCESSIBILITY_CLOSURE_REASSESSMENT_EXECUTION_RESULT_v0.1.md`

The bounded corrective assessment executed with integrity `PASS`; RF-AC01 through RF-AC04 all passed. O3 was confirmed as a native candidate alternative, but MC02 (availability/accessibility of T-C at decision time) and MC03 (ability to perform required setup within the decision-time boundary) remained unresolved. The rule that partial setup plus an explicit alternative-tool requirement implies accessibility was correctly classified as `ANALYST-INTERPRETATION`, triggering `HS-AC01`.

The result is `INDETERMINATE / H-B`: a bounded deeper operationalization boundary persists. It is material methodological evidence because it qualifies the evidence boundary for accessibility closure. It does not establish complete `T_acc`, utility, superiority, causality, value, transversal validity or any Core modification. No additional constructive attempt or comparative IUT is authorized by this closure.

## Material methodological evidence — Class-II AWS-PatchAsgInstance

**Fixture:** `IT-METH-I-CLASS-II-AWS-PATCHASGINSTANCE`  
**Phase-A:** `CLOSED — PREDECISION RECONSTRUCTION REPRODUCIBILITY PASS`  
**B0 accessibility:** `CLOSED — NO ADMISSIBLE RESOLVED ACCESSIBILITY DIFFERENCE IDENTIFIED`  
**B0 permissions:** `CLOSED — PARTIAL / EFFECTIVE CANDIDATE PERMISSION UNRESOLVED`

The primary Phase-A freeze and independent R002 reconstruction recovered the same governed identity and 21/21 exact compared fields. B0 found no admissible resolved accessibility difference and the permissions audit left effective candidate permission unresolved. This remains Class-II fixture-level methodological evidence.

### Claim boundary

No C01–C16 status is upgraded by the material evidence recorded in v1.1. EXT-UPD-4.8 does not establish general T_acc closure, utility, production benefit, financial/value realization, causality, predictive validity, superiority, transversal validity or Class-I industrial status.

## Gate state

- G1 Independent replication: OPEN at general scientific level; bounded fixture/event closures remain separately recorded.
- G2 Cross-domain generalisation: BOUNDED / PARTIAL.
- G3 Trajectory sufficiency: OPEN.
- G4 Causal identification: OPEN.
- G5 Value linkage: OPEN.
- G6 Originality/comparative architecture: BOUNDED / PARTIAL.
- G7 Transversal translation protocol: C-01 A-C PASS + I-01 Gate C INDETERMINATE; IT-NOSD-010 provides bounded downstream-separation evidence; EXT-UPD-4.8 provides bounded accessibility-closure boundary evidence.

## Current methodological routing

- IUT-A-01 U2 FULL_PILOT 001: `CLOSED — U2-NULL`; no rerun.
- IT-NOSD-010: G0/G1/G2 closed for one bounded frozen event; industrial execution authorization `NONE`.
- EXT-UPD-4.8 O3 accessibility closure: `CLOSED — INDETERMINATE / H-B / HS-AC01`; no reopening or additional attempt under this closure.
- AWS Phase-A/B0 work remains fixture-level and no candidate/comparator transformation is authorized.
- Utility scoring and industrial case admission: `NOT AUTHORIZED`.

## Current scientific position

The evidence base includes bounded comparative methodological evidence from IUT-A-01 U2, bounded downstream-separation/reconstructability evidence from IT-NOSD-010, bounded accessibility-closure boundary evidence from EXT-UPD-4.8, and Class-II AWS fixture evidence. These results are material evidence records but do not alter the scientific Core or any C01–C16 claim status.
