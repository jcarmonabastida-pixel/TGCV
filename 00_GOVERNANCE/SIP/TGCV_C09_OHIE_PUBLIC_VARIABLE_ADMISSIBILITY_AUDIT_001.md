# TGCV C09 — OHIE Public Variable Admissibility Audit 001

**Status:** `COMPLETED — BLOCKED / NO C09 EXECUTION ADMISSION`
**Date:** 2026-09-13
**Parent:** `TGCV_C09_OHIE_OPERATIONAL_PREFLIGHT_001.md`
**Execution authorization:** `NONE`

## 1. Objective

Audit the public OHIE variables at variable level for construction of:

`U_tau → P_tau → T_acc,0 → T_acc,1`

while maintaining the C09 information firewall and excluding post-treatment leakage.

## 2. Public variable evidence

The published OHIE documentation confirms a stable person identifier and lottery-level variables including lottery selection, lottery draw, application status, and approval status. The ICPSR collection also documents administrative Medicaid enrollment histories and follow-up data. citeturn0search3turn0search0

A public-use data description identifies variables including `applied_app`, `draw_lottery`, `numhh_list`, `age`, `have_phone`, `English_list`, `female_list`, `pobox_list`, `self_list`, and `zip_msa_list`. citeturn0search22

The published experiment defines `LOTTERY` as selection status and interprets it as the effect of being able to apply for OHP Standard. citeturn0search0

## 3. Variable-level classification

| Variable / class | Pre-treatment admissibility | Allowed for `U_tau/P_tau` | Leakage risk | Decision |
|---|---|---|---|---|
| `person_id` / stable identifier | Yes | Identity only | None | PASS |
| `draw_lottery` / lottery draw | Yes | Treatment-boundary context | Low | PASS |
| `LOTTERY` / selection | At decision boundary | Defines `Z` | None if frozen before outcomes | PASS |
| `numhh_list` | Yes | Eligibility/treatment-probability conditioning | Low | PASS |
| lottery-list demographics (`age`, sex, language, PO box, phone, self-sign-up, ZIP/MSA, etc.) | Yes | Pre-state/context | Low | PASS |
| published OHP eligibility/application rules | Yes, external rule layer | Defines `P_tau` | None if version-frozen | PASS — bounded |
| `applied_app` | **Post-Z** | Outcome/take-up only | **HIGH** | EXCLUDE from `P_tau` / `T_acc` |
| application approval | **Post-Z** | Outcome/take-up only | **HIGH** | EXCLUDE |
| Medicaid enrollment history after lottery | **Post-Z** | Trajectory/outcome only | **HIGH** | EXCLUDE from accessibility construction |
| post-lottery health/insurance variables | Post-Z | `Y` only if frozen independently | **HIGH** | EXCLUDE from `T_acc` |
| pre-lottery administrative measures | Pre-Z where date verified | Baseline state only | Medium | CONDITIONAL |

The distinction is supported by the published design: application and approval occur after lottery selection, while lottery-list demographics are explicitly described as prerandomization information. citeturn0search0turn0search3

## 4. `U_tau` admissibility result

A finite `U_tau` can be specified at the **programme-action level**, for example:

`τ_insurance = initiate_OHP_Standard_application`

and, if separately justified by the frozen rule, the subsequent eligible enrollment transition.

However, the public dataset does not itself provide a pre-existing TGCV transformation taxonomy. Therefore `U_tau` is not an observed variable and must be an explicitly frozen research construct derived from the published programme rules.

**G3 = CONDITIONAL PASS, not execution-ready.**

## 5. `P_tau` admissibility result

`P_tau` can use:

- pre-lottery unit state;
- household/list composition;
- published OHP eligibility/application rules;
- lottery-selection permission at the treatment boundary.

It must not use:

- application submission;
- approval;
- enrollment;
- observed coverage duration;
- health outcomes;
- post-treatment behavior.

Therefore a bounded ex-ante predicate is feasible.

**G4 = PASS — BOUNDED.**

## 6. `T_acc,0` / `T_acc,1`

The critical construction is:

`T_acc,0 = {τ ∈ U_tau | P_tau(Z=0,S0,C0)=1}`

`T_acc,1 = {τ ∈ U_tau | P_tau(Z=1,S0,C0)=1}`

The public evidence supports the interpretation that lottery selection grants the opportunity to apply for OHP Standard. citeturn0search0turn0search3

But the exact unit-level transformation predicate is not contained as a TGCV-labelled variable in the public data. Consequently:

**`Z → ΔT_acc` remains CONDITIONAL, not demonstrated.**

This is the decisive blocker.

## 7. Information firewall

The following firewall is mandatory:

`Z → T_acc` may use only pre-treatment state and frozen programme rules.

`T_acc` must not be reconstructed from `applied_app`, approval, enrollment, coverage months, health care utilization, health outcomes, or later survey variables.

The published OHIE data structure confirms that application and approval are distinct downstream variables, making them unsuitable for defining the treatment-accessibility space. citeturn0search3turn0search22

## 8. Decision

**OHIE PUBLIC VARIABLE ADMISSIBILITY = BLOCKED FOR C09 EXECUTION.**

The audit establishes that the public data contain the ingredients required to define treatment, baseline state, and downstream trajectory, but they do **not** contain a sufficiently pre-specified TGCV transformation-space representation to demonstrate `Z → ΔT_acc` without introducing a researcher-defined transformation ontology.

This does not invalidate OHIE as a conventional randomized-access experiment. It prevents importing that conventional causal identification directly into C09.

**C09 claim remains H / no causal identification established.**

No execution authorization.
No data acquisition.
No model fitting.
No AWS/Rust/SWIM action.

### Disposition

`OHIE = CLOSED AS C09 EXECUTION CANDIDATE UNDER CURRENT PUBLIC-VARIABLE/FIREWALL STANDARD.`

Retain as methodological reference only unless a separately governed operational specification can justify `U_tau` independently of the realized insurance outcomes.
