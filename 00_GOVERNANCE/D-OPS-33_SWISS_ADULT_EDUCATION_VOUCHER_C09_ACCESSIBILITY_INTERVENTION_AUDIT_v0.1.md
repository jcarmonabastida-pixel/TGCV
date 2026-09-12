# D-OPS-33 — Swiss Adult Education Voucher C09 Accessibility Intervention Audit v0.1

**Status:** `CLOSED — METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Execution:** `NOT AUTHORIZED`
**Candidate:** Swiss Adult Education Voucher randomized field experiment

## 1. Purpose

Apply the strengthened C09 filter to a randomized intervention that changes ex ante access to fee-based adult-education transformations.

## 2. Evidence

The Swiss experiment randomly issued adult-education vouchers to a representative sample drawn from the Swiss Labour Force Survey. The treatment group contained 1,422 individuals in the main labor-market analysis, compared with 9,099 controls; participants were followed through 2007 for earnings, employment and subsequent education. citeturn1search1turn1search10

The voucher could be redeemed for an adult-education course of the participant's choice. The experimental design therefore creates a direct intervention on the affordability/access condition for a class of fee-based education transformations. citeturn1search23turn1search27

## 3. C09 gate assessment

| Gate | Result | Finding |
|---|---|---|
| Stable unit | PASS | Individual SLFS respondent. |
| Independent intervention | PASS | Random voucher assignment. citeturn1search1 |
| `Z → ΔT_acc` | **PASS — strong design candidate** | Voucher changes ex ante affordability/access to eligible fee-based courses. |
| Counterfactual | PASS | Randomized no-voucher control. |
| Longitudinal trajectory | PASS — bounded | SLFS follow-up through 2007 observes subsequent education and labor-market outcomes. citeturn1search1 |
| Transition environment | PASS — bounded | Voucher changes financial accessibility; it does not itself redefine subsequent labor-market outcomes. |
| Bounded `U_tau` | CONDITIONAL PASS | A frozen universe of eligible fee-based course transformations can be defined for the intervention window. |
| Pre-execution `P_tau` | CONDITIONAL PASS | Voucher/course eligibility rules are documented, but full unit-level course universe is not publicly reconstructed. |
| Public unit-level inputs for `T_acc,0/T_acc,1` | **FAIL** | The experiment was embedded in SLFS respondent data and linked experimental/survey information; the sources located document the experiment but do not provide a complete public unit-level reconstruction package. The experiment also deliberately avoided releasing public information during the experimental period. citeturn1search27 |
| Public reproducibility | **FAIL** | No complete public unit-level package sufficient for independent reconstruction of treatment/control accessibility states was identified. |

## 4. TGCV boundary

The substantive mapping is clean:

`Z → voucher affordability → T_acc(Z) → course choice/participation → subsequent trajectory`

This is a direct accessibility intervention rather than a ranking, information-only or post-treatment incentive classification. However, the C09 firewall requires the transformation universe and accessibility predicate to be frozen independently of observed course uptake and outcomes.

## 5. Decision

**D-OPS-33 = CLOSED — METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED.**

Strengths:
- randomized intervention;
- direct affordability/access change;
- credible counterfactual;
- longitudinal follow-up;
- bounded transformation class.

Decisive blocker:
- no complete public unit-level reconstruction package for `T_acc,0/T_acc,1` was demonstrated.

No C09 claim upgrade.
No data acquisition.
No model fitting.
No execution authorization.
No AWS/Rust/SWIM action.

**Discovery implication:** adult-education vouchers remain a useful methodological reference. The search should now strongly favor public-use randomized datasets whose released variables themselves contain the complete pretreatment state and intervention rule needed to compute `T_acc`, rather than studies where the experiment is embedded in restricted survey infrastructure.
