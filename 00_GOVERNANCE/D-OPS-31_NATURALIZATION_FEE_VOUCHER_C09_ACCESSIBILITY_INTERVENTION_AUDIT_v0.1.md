# D-OPS-31 — Naturalization Fee Voucher C09 Accessibility Intervention Audit v0.1

**Status:** `CLOSED — PROMISING METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Execution:** `NOT AUTHORIZED`
**Candidate:** New York naturalization fee-voucher randomized intervention

## 1. Purpose

Apply the strengthened C09 filter to a randomized intervention that directly removes an ex ante financial barrier to a concrete transformation: initiating a naturalization application.

## 2. Evidence

The 2016–2018 New York programme randomly assigned eligible registrants to receive a voucher covering the naturalization application fee. The 2026 study reports 2,802 randomized registrants (1,442 treatment; 1,360 control) and longitudinal follow-up for up to five years for some cohorts. The voucher increased naturalization by about 36 percentage points. citeturn0search0turn1search1

The intervention is tightly specified: the voucher could only be used to pay the naturalization application fee, and randomization occurred after registration within geographic/fee blocks. citeturn0search0

## 3. C09 gate assessment

| Gate | Result | Finding |
|---|---|---|
| Stable unit | PASS | Individual registrant with pretreatment registration record. |
| Bounded `U_tau` | CONDITIONAL PASS | A frozen universe can be defined as application-initiation transformations under the declared naturalization programme/window. |
| Pre-execution `P_tau` | PASS — bounded | Eligibility and fee-payment conditions are specified before realized application/naturalization outcomes. |
| Independent intervention | PASS | Individual random lottery assignment. citeturn0search0 |
| `Z → ΔT_acc` | **PASS — strong design candidate** | Voucher assignment removes the fee barrier for initiating the naturalization application, changing ex ante affordability/access without defining access from realized application behaviour. |
| Counterfactual | PASS | Randomized no-voucher control. |
| Longitudinal trajectory | PASS — bounded | Follow-up measures application/naturalization and other outcomes over multiple years. citeturn0search0 |
| Transition environment | PASS — bounded | Voucher changes fee accessibility; it does not itself alter the naturalization legal decision rule. |
| Public unit-level inputs for `T_acc,0/T_acc,1` | **FAIL / NOT DEMONSTRATED** | The published study uses programme registration data, follow-up surveys and matched credit-bureau records; some survey data are only available in coarsened form upon request, and credit-bureau data cannot be shared. citeturn0search0turn1search12 |
| Public reproducibility | **FAIL** | The complete unit-level package required for an independent reconstruction of both treatment/control accessibility states is not publicly available. |

## 4. TGCV boundary

The substantive accessibility mapping is unusually clean:

`Z → fee-access condition → T_acc(Z) → application initiation → subsequent trajectory`

This is stronger than interventions affecting only ranking, information, notification or realized participation. The voucher changes an ex ante condition for initiating a defined transformation.

However, the TGCV execution firewall requires `T_acc` to be reconstructed from pretreatment/public inputs independently of realized applications, citizenship, credit outcomes or later trajectory. The current data-access statement prevents claiming that this complete unit-level reconstruction is publicly reproducible. citeturn0search0

## 5. Decision

**D-OPS-31 = CLOSED — PROMISING METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED.**

Strengths:
- randomized individual intervention;
- unusually direct `Z → ΔT_acc` mechanism;
- explicit pre-treatment programme/eligibility rules;
- credible randomized counterfactual;
- multi-year trajectory observation;
- no need to infer accessibility from realized outcomes.

Decisive blocker:
- incomplete public unit-level data for independent reconstruction of `T_acc,0` and `T_acc,1`.

No C09 claim upgrade.
No data acquisition.
No model fitting.
No execution authorization.
No AWS/Rust/SWIM action.

**Discovery implication:** naturalization is retained as a high-quality methodological reference. Future candidates must satisfy the same direct-accessibility test while additionally providing a complete public unit-level pretreatment package sufficient to compute treatment/control `T_acc` without restricted administrative or survey data.
