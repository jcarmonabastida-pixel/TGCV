# D-OPS-32 — NYCHANS Affordable-Housing C09 Accessibility Intervention Audit v0.1

**Status:** `CLOSED — STRONG METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Execution:** `NOT AUTHORIZED`
**Candidate:** New York City Housing and Neighborhood Study (NYCHANS)

## 1. Purpose

Apply the strengthened C09 filter to a randomized housing-access intervention with a concrete unit-level change in the set of housing transformations available to treatment households.

## 2. Evidence

NYCHANS is a randomized control trial of newly constructed affordable housing. Approximately 2,600 households were randomly assigned either to receive an affordable housing unit at one of thirteen developments or to remain in private-market housing without assistance; follow-up interviews occurred four to seven years later. citeturn2search0turn3search1

The study used the existing New York City housing-lottery mechanism. Administrative application/screening data include household characteristics, eligibility, originating address and group assignment; group assignment data were available for the full sample. citeturn3search12

## 3. C09 gate assessment

| Gate | Result | Finding |
|---|---|---|
| Stable unit | PASS | Household/application unit identified through the housing lottery. |
| Independent intervention | PASS | Housing offers were determined through randomized lottery assignment. citeturn3search12 |
| `Z → ΔT_acc` | **PASS — strong design candidate** | An affordable-housing offer changes ex ante access to a concrete class of residential transformations: occupying the offered subsidized unit/development. |
| Counterfactual | PASS | Eligible but non-offered households form the randomized comparison. |
| Longitudinal trajectory | PASS — bounded | Follow-up extends four to seven years and covers housing, neighborhood, financial and health trajectories. citeturn2search0 |
| Transition environment | PASS — bounded | The intervention is an offer of an existing housing unit rather than a modification of the downstream outcome definition. |
| Bounded `U_tau` | CONDITIONAL PASS | A frozen universe can be defined over eligible housing-occupation transitions at the participating developments. |
| Pre-treatment `P_tau` | PASS — bounded | Lottery eligibility and unit-specific programme conditions are defined before realized outcomes. |
| Public unit-level reconstruction of `T_acc` | **FAIL / NOT DEMONSTRATED** | The required application/screening files and Housing Connect/administrative records were used by the research team; current public HPD pages do not establish a complete public NYCHANS unit-level package. citeturn3search12turn3search0 |
| Public reproducibility | **FAIL** | NYCHANS research data are not demonstrated as a complete public reconstruction package; disclosure-avoidance constraints are documented for study-site information. citeturn3search13 |

## 4. TGCV boundary

The candidate provides a particularly clean accessibility mechanism:

`Z → housing-offer availability → T_acc(Z) → residential transition → subsequent trajectory`

This is closer to the required C09 mechanism than ranking, information, notification or incentive-only interventions. The treatment changes the ex ante availability of a concrete residential transformation.

The analysis must not infer `T_acc` from the observed move. The transformation universe and admissibility predicate must be frozen from the housing programme, participating developments, eligibility rules and pretreatment application state before examining take-up or subsequent outcomes.

## 5. Decision

**D-OPS-32 = CLOSED — STRONG METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED.**

Strengths:
- randomized unit-level housing access;
- direct and concrete `Z → ΔT_acc` mechanism;
- credible counterfactual;
- multi-year trajectory;
- documented pretreatment administrative state;
- stable treatment mechanism.

Decisive blocker:
- complete public unit-level pretreatment data required for independent reconstruction of treatment/control `T_acc` are not demonstrated.

No C09 claim upgrade.
No data acquisition.
No model fitting.
No execution authorization.
No AWS/Rust/SWIM action.

**Discovery implication:** NYCHANS becomes a strong methodological reference for the exact intervention mechanism sought by C09, but the public-reconstructibility gate remains decisive. Future search should prioritize experiments where the lottery/eligibility state and all transformation-relevant unit inputs are released publicly, not merely the randomized assignment and outcomes.
