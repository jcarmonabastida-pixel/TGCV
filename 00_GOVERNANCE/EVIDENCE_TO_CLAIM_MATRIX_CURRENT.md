# TGCV — Evidence-to-Claim Matrix — Current v1.0

**Status:** GOVERNANCE CONTROL ARTIFACT — CURRENT  
**Date:** 2026-09-11  
**Predecessor:** v0.9  
**Current update:** Material evidence propagation for IUT-A-01 U2 FULL_PILOT 001 and IT-NOSD-010 IT-G2. No scientific claim status/level upgrade.

## Material evidence propagation rule
A material experimental result is propagated to this matrix when it adds, removes, qualifies, bounds, or otherwise changes the evidentiary basis or interpretation of a claim, even when no claim status/level changes. Claim upgrade is a separate decision and is never inferred merely from evidence propagation. Pure reruns with no new evidentiary content may remain outside the matrix.

**Operational rule:** A material experimental result is propagated to this matrix when it adds, removes, qualifies, bounds, or otherwise changes the evidentiary basis or interpretation of a claim. Claim upgrade is a separate decision. Evidence propagation does not imply claim upgrade.

| ID | Claim | Status | Current evidence / basis | Evidence impact / interpretation | Next requirement |
|---|---|---|---|---|---|
| C01 | TGCV represents system state/context/conditions and constraints/resources | E0 | Formal architecture + bounded cross-domain traces | IUT and IT-NOSD provide bounded experimental operational evidence, but no claim-level upgrade. | Further independent operational confirmation |
| C02 | Accessibility is represented by transformations satisfying an independently defined admissibility predicate | E0 | Formalization + Rust + C-01 A-C + I-01 Gate C + IT-NOSD-010 G0/G1/G2 | IT-NOSD independently reconstructs bounded accessibility and downstream separation for one frozen event; it does not close general T_acc. | Independent operationalization with closed accessible transformation space |
| C03 | T_acc is analytically distinct from downstream Reach in bounded Rust | E1 | Rust evidence | IT-NOSD adds bounded empirical separation of accessibility from downstream evidence, but does not alter the Rust claim level. | Independent replication |
| C04 | ΔT_acc can occur without ΔReach¹_pot | E1 | Rust ND-1 | No direct test by IUT or IT-NOSD. | Independent replication |
| C05 | ΔT_acc can occur with ΔReach¹_pot change | E1 | Rust ND-2 | No direct test by IUT or IT-NOSD. | Independent replication |
| C06 | Reach identity is not characterized by cardinality alone | E1 | Rust ND-4 | No direct impact. | Independent replication |
| C07 | Accessible transformation spaces change over time in Rust | E1 | Rust non-persistent pairs | IT-NOSD reconstructs one bounded state transition but does not establish the general Rust claim. | Independent closed operationalization |
| C08 | Accessibility changes modify reachable future trajectories | H | Formal chain + bounded Rust H=1 | IT-NOSD closes only bounded downstream separation/reconstructability for one event; it does not identify trajectory effects. | Valid trajectory test |
| C09 | Accessibility changes causally affect subsequent trajectories | H | No causal identification | IUT and IT-NOSD do not establish causality. | Causal design |
| C10 | Accessibility changes generate/predict value | H | No Value evidence | IUT M1/M2 is bounded decision-performance evidence and not value realization; IT-NOSD is bounded reconstructability evidence. | Value-linked test |
| C11 | TGCV is domain-independent / transversal | H | C-01 A-C + I-01 Gate C | IT-NOSD is one bounded 5G case and IUT is one frozen decision fixture; neither establishes transversal validity. | Independent operationalization across broader domains |
| C12 | TGCV provides superior explanatory representation | H | Comparative evidence absent | IUT M1 shows +40 pp bounded decision correctness in the frozen fixture, but M2 fails its predeclared timing criterion; the overall U2 result is U2-NULL. This is material comparative evidence but not superiority evidence. | Controlled differentiated comparison |
| C13 | TGCV contains no equivalent prior architecture | O | D-OPS-21 | No impact. | Comparative coverage |
| C14 | T_acc is an ontological primitive independent of S | F | TR-131 | No impact. | No restoration without contrary evidence |
| C15 | Rust demonstrates observed Cargo/runtime reachability | F | Rust evidence boundary | No impact. | Separate governed runtime test |
| C16 | TGCV provides a transversal analytical translation protocol preserving distinctions among state, candidate transformations, accessibility, Reach, Trajectory, Outcome and Value | H | D-OPS-22/23 + C-01 A-C + I-01 Gate C + IT-NOSD-010 G0/G1/G2 | IT-NOSD materially strengthens bounded state/accessibility/downstream-separation reconstruction methodology, without closing downstream trajectory/value boundaries. | Closed independent-domain operationalization / downstream test |

## Material methodological evidence — IUT-A-01 U2 FULL_PILOT 001

**Case:** `IUT-A-01`  
**Status:** `CLOSED — U2-NULL`  
**Evidence artifact:** `03_EXPERIMENTS/IUT-A-01/IUT_A01_U2_FULL_PILOT_RESULT_001.json`  
**Closure audit:** `03_EXPERIMENTS/IUT-A-01/IUT_A01_U2_FULL_PILOT_CLOSURE_AUDIT_001.md`

The frozen FULL_PILOT completed with execution integrity `PASS`. M1 decision correctness was `60.0%` control versus `100.0%` TGCV, a `+40.0` percentage-point difference, with the predeclared M1 gate passing. M2 used the declared single-invocation microbenchmark and failed its predeclared improvement threshold: control median `0.00155 ms`, TGCV median `0.00485 ms`. The overall classification is `U2-NULL`.

This is **material comparative methodological evidence** bounded to Fixture 002 and the executed criteria. It must be retained in the evidence base, but it does not upgrade C12 or any other claim. It does not establish explanatory superiority, general discriminatory superiority, industrial utility, financial/value realization, causal generalisation, validity across domains/populations, or TGCV Core modification.

## Material methodological evidence — IT-NOSD-010

**Case:** `IT-NOSD-010 — ETSI TS 23.502 / 3GPP 5GS`  
**Status:** `IT-G0 CLOSED — BOUNDED PRE-OUTCOME CASE-DEFINITION PASS`; `IT-G1 CLOSED — BOUNDED REPRODUCIBILITY / ADMISSION PASS`; `IT-G2 CLOSED — BOUNDED DOWNSTREAM-SEPARATION PASS`.

The independent G1 and G2 executions reproduced the frozen event, provenance, bounded pre-state, transformation identity, temporal boundary and downstream separation. G2 predicates G2-01 through G2-10 all passed. Accessibility was not reused as outcome evidence, outcome was not used to define post-state, and complete ex-ante enumeration of `T_acc(S_t)` was not required under TR-132-MOD-1.

This is **material bounded methodological evidence** for reconstruction and separation of accessibility from downstream evidence in one frozen 5G event. It does not establish complete `T_acc`, normative 3GPP admissibility, utility, causal effect, value effect, comparative superiority, transversal validity or scientific validation.

## Material methodological evidence — Class-II AWS-PatchAsgInstance

**Fixture:** `IT-METH-I-CLASS-II-AWS-PATCHASGINSTANCE`  
**Phase-A status:** `CLOSED — PREDECISION RECONSTRUCTION REPRODUCIBILITY PASS`  
**B0 accessibility preflight:** `CLOSED — NO ADMISSIBLE RESOLVED ACCESSIBILITY DIFFERENCE IDENTIFIED`  
**B0 permissions audit:** `CLOSED — PARTIAL / EFFECTIVE CANDIDATE PERMISSION UNRESOLVED`

The primary Phase-A predecision freeze and independently executed R002 reconstruction recovered the same governed target/ASG identity and exactly the same 21 compared reconstruction fields. All mandatory accessibility predicates passed in R002. The R002 artifact and governed comparison artifact were independently seal-verified.

The subsequent B0 read-only accessibility preflight found no admissible resolved predicate difference between candidate and comparator. The follow-up permissions audit established that the Phase-A fields `AutomationAssumeRole` and `LambdaRoleArn` were documented omissions (`OMITTED_UNLESS_FROZEN`), not concrete frozen IAM identities. Consequently no candidate role availability was established and effective candidate operation permission remains `UNRESOLVED`. The comparator caller's modeled `ssm:SendCommand` permission was observed as `allowed` through read-only IAM simulation, but this does not establish end-to-end transformation success.

This evidence is **Class-II fixture-level methodological evidence**. It supports reproducibility/readiness and documents the limits of the bounded predecision/accessibility evidence boundary. It is not an observed industrial-case result.

### Claim boundary

No C01–C16 status is upgraded by the material evidence recorded in v1.0. In particular, it does not establish general T_acc closure, utility, production benefit, financial/value realization, causality, predictive validity, superiority, transversal validity or Class-I industrial status.

## Invalidated intermediate tooling result

The earlier comparison artifact reporting 21 reconstruction disagreements is excluded from the evidence base because it resulted from a structural normalization defect in the comparison implementation. The corrected governed comparison reported `21 EXACT_AGREEMENT`, `0 RECONSTRUCTION_DISAGREEMENT`, `0 UNRESOLVED`.

## Gate state

- G1 Independent replication: OPEN at general scientific level; AWS fixture-level predecision reconstruction reproducibility CLOSED — PASS; IT-NOSD-010 bounded G1 CLOSED — PASS.
- G2 Cross-domain generalisation: BOUNDED / PARTIAL.
- G3 Trajectory sufficiency: OPEN.
- G4 Causal identification: OPEN.
- G5 Value linkage: OPEN.
- G6 Originality/comparative architecture: BOUNDED / PARTIAL; IUT U2-NULL does not close superiority.
- G7 Transversal translation protocol: C-01 A-C PASS + I-01 Gate C INDETERMINATE; IT-NOSD-010 provides bounded downstream-separation evidence only.

## Current methodological routing

- IUT-A-01 U2 FULL_PILOT 001: `CLOSED — U2-NULL`; no rerun.
- IT-NOSD-010: G0/G1/G2 closed for one bounded frozen event; industrial execution authorization `NONE`.
- Phase-A predecision reconstruction: `CLOSED — PASS`.
- Phase-B0 read-only accessibility preflight: `CLOSED — NO ADMISSIBLE RESOLVED DIFFERENCE`.
- Phase-B0 permissions audit: `CLOSED — PARTIAL / EFFECTIVE CANDIDATE PERMISSION UNRESOLVED`.
- Candidate transformation: `NOT AUTHORIZED`.
- Comparator transformation: `NOT AUTHORIZED`.
- Utility scoring: `NOT AUTHORIZED`.
- Industrial case admission: `NOT AUTHORIZED`.

## Current scientific position

The evidence base includes bounded comparative methodological evidence from IUT-A-01 U2 (`U2-NULL`), bounded downstream-separation/reconstructability evidence from IT-NOSD-010, and the closed Class-II AWS predecision reconstruction/accessibility/permissions evidence. These results are material evidence records but **do not alter the scientific Core or any C01–C16 claim status**.
