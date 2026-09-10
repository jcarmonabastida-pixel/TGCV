# TGCV — Evidence-to-Claim Matrix — Current v0.9

**Status:** GOVERNANCE CONTROL ARTIFACT — CURRENT  
**Date:** 2026-09-11  
**Predecessor:** v0.8  
**Current update:** Class-II AWS-PatchAsgInstance B0 permissions-audit closure propagated. No scientific claim upgrade.

| ID | Claim | Status | Current evidence / basis | Evidence impact / interpretation | Next requirement |
|---|---|---|---|---|---|
| C01 | TGCV represents system state/context/conditions and constraints/resources | E0 | Formal architecture + bounded cross-domain traces | No scientific upgrade. AWS adds bounded fixture-state observability evidence only. | Further independent operational confirmation |
| C02 | Accessibility is represented by transformations satisfying an independently defined admissibility predicate | E0 | Formalization + Rust + C-01 A-C + I-01 Gate C | AWS demonstrates reconstruction of frozen accessibility predicates at fixture level; B0 permissions audit clarifies evidence-boundary limits. It does not close general T_acc. | Independent operationalization with closed accessible transformation space |
| C03 | T_acc is analytically distinct from downstream Reach in bounded Rust | E1 | Rust evidence | No impact. | Independent replication |
| C04 | ΔT_acc can occur without ΔReach¹_pot | E1 | Rust ND-1 | No impact. | Independent replication |
| C05 | ΔT_acc can occur with ΔReach¹_pot change | E1 | Rust ND-2 | No impact. | Independent replication |
| C06 | Reach identity is not characterized by cardinality alone | E1 | Rust ND-4 | No impact. | Independent replication |
| C07 | Accessible transformation spaces change over time in Rust | E1 | Rust non-persistent pairs | AWS Phase-A/B0 did not test transformation-induced change. | Independent closed operationalization |
| C08 | Accessibility changes modify reachable future trajectories | H | Formal chain + bounded Rust H=1 | AWS Phase-A/B0 stopped at predecision/read-only accessibility evidence and did not execute transformations or identify downstream Reach/Trajectory effects. | Valid trajectory test |
| C09 | Accessibility changes causally affect subsequent trajectories | H | No causal identification | No change. | Causal design |
| C10 | Accessibility changes generate/predict value | H | No Value evidence | No change. | Value-linked test |
| C11 | TGCV is domain-independent / transversal | H | C-01 A-C + I-01 Gate C | AWS is one bounded application/fixture and does not establish transversal conformance. | Independent operationalization across broader domains |
| C12 | TGCV provides superior explanatory representation | H | Comparative evidence absent | AWS reconstruction reproducibility and B0 permissions evidence are not a superiority comparison. | Controlled differentiated comparison |
| C13 | TGCV contains no equivalent prior architecture | O | D-OPS-21 | No impact. | Comparative coverage |
| C14 | T_acc is an ontological primitive independent of S | F | TR-131 | No impact. | No restoration without contrary evidence |
| C15 | Rust demonstrates observed Cargo/runtime reachability | F | Rust evidence boundary | No impact. | Separate governed runtime test |
| C16 | TGCV provides a transversal analytical translation protocol preserving distinctions among state, candidate transformations, accessibility, Reach, Trajectory, Outcome and Value | H | D-OPS-22/23 + C-01 A-C + I-01 Gate C | AWS Phase-A/B0 strengthens bounded state/accessibility reconstruction methodology only; downstream distinctions remain untested. | Closed independent-domain operationalization / downstream test |

## Material methodological evidence — Class-II AWS-PatchAsgInstance

**Fixture:** `IT-METH-I-CLASS-II-AWS-PATCHASGINSTANCE`  
**Phase-A status:** `CLOSED — PREDECISION RECONSTRUCTION REPRODUCIBILITY PASS`  
**B0 accessibility preflight:** `CLOSED — NO ADMISSIBLE RESOLVED ACCESSIBILITY DIFFERENCE IDENTIFIED`  
**B0 permissions audit:** `CLOSED — PARTIAL / EFFECTIVE CANDIDATE PERMISSION UNRESOLVED`

The primary Phase-A predecision freeze and independently executed R002 reconstruction recovered the same governed target/ASG identity and exactly the same 21 compared reconstruction fields. All mandatory accessibility predicates passed in R002. The R002 artifact and governed comparison artifact were independently seal-verified.

The subsequent B0 read-only accessibility preflight found no admissible resolved predicate difference between candidate and comparator. The follow-up permissions audit established that the Phase-A fields `AutomationAssumeRole` and `LambdaRoleArn` were documented omissions (`OMITTED_UNLESS_FROZEN`), not concrete frozen IAM identities. Consequently no candidate role availability was established and effective candidate operation permission remains `UNRESOLVED`. The comparator caller's modeled `ssm:SendCommand` permission was observed as `allowed` through read-only IAM simulation, but this does not establish end-to-end transformation success.

This evidence is **Class-II fixture-level methodological evidence**. It supports reproducibility/readiness and documents the limits of the bounded predecision/accessibility evidence boundary. It is not an observed industrial-case result.

### Claim boundary

No C01–C16 status is upgraded by this evidence. In particular, it does not establish general T_acc closure, utility, production benefit, financial/value realization, causality, predictive validity, superiority, transversal validity or Class-I industrial status.

## Invalidated intermediate tooling result

The earlier comparison artifact reporting 21 reconstruction disagreements is excluded from the evidence base because it resulted from a structural normalization defect in the comparison implementation. The corrected governed comparison reported `21 EXACT_AGREEMENT`, `0 RECONSTRUCTION_DISAGREEMENT`, `0 UNRESOLVED`.

## Gate state

- G1 Independent replication: OPEN at general scientific level; AWS fixture-level predecision reconstruction reproducibility CLOSED — PASS.
- G2 Cross-domain generalisation: BOUNDED / PARTIAL.
- G3 Trajectory sufficiency: OPEN.
- G4 Causal identification: OPEN.
- G5 Value linkage: OPEN.
- G6 Originality/comparative architecture: BOUNDED / PARTIAL.
- G7 Transversal translation protocol: C-01 A-C PASS + I-01 Gate C INDETERMINATE; AWS Phase-A/B0 does not close downstream boundary.

## Current methodological routing

- Phase-A predecision reconstruction: `CLOSED — PASS`.
- Phase-B0 read-only accessibility preflight: `CLOSED — NO ADMISSIBLE RESOLVED DIFFERENCE`.
- Phase-B0 permissions audit: `CLOSED — PARTIAL / EFFECTIVE CANDIDATE PERMISSION UNRESOLVED`.
- Candidate transformation: `NOT AUTHORIZED`.
- Comparator transformation: `NOT AUTHORIZED`.
- Utility scoring: `NOT AUTHORIZED`.
- Industrial case admission: `NOT AUTHORIZED`.

## Current scientific position

The evidence base includes a closed Class-II AWS predecision reconstruction reproducibility result and bounded B0 accessibility/permissions evidence. These are methodological fixture-level results and do not alter the scientific Core or any C01–C16 claim status.
