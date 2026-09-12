# TGCV C09 — OHIE Operational Preflight 001

**Status:** `COMPLETED — BLOCKED BEFORE EXECUTION`
**Date:** 2026-09-13
**Candidate:** Oregon Health Insurance Experiment (OHIE), 2008 Medicaid lottery
**Parent audit:** `D-OPS-28_OREGON_MEDICAID_LOTTERY_C09_ACCESSIBILITY_INTERVENTION_AUDIT_v0.1.md`
**Execution authorization:** `NONE`

## 1. Objective

Test the minimum operational condition for C09:

`Z → ΔT_acc → Y`

without defining `T_acc` from realized enrollment, treatment take-up, health outcomes, or other post-treatment variables.

## 2. Frozen candidate design

**Unit:** individual registered in the 2008 Oregon Medicaid lottery.

**Decision time:** the individual's lottery-selection notification boundary.

**Treatment:** `Z=1` lottery selected / permitted to apply for OHP Standard.

**Control:** `Z=0` lottery not selected during the frozen initial opportunity window.

**State/context:** only information available before lottery selection plus the published OHP Standard eligibility/application rules.

**Trajectory outcome:** independently specified post-selection insurance/health trajectory over a frozen horizon; outcome definition must not be used to construct accessibility.

The public ICPSR collection contains lottery selection, application and approval variables, the initial lottery list, Medicaid enrollment records and follow-up survey/administrative data for 2007–2010. Public-use files are explicitly available, although some collection components are restricted. citeturn0search2turn0search11

## 3. Accessibility construction

A candidate bounded transformation universe is:

`U_tau = {τ_insurance : eligible lottery participant → OHP Standard application/enrollment state}`

with `P_tau(Z)` determined only from the frozen programme rules and pre-treatment state.

The critical distinction is:

- **Allowed:** lottery selection changes the formal opportunity to initiate the OHP Standard application/enrollment transition.
- **Forbidden:** defining accessibility as “actually enrolled”, “months covered”, “insurance observed”, or any variable downstream of lottery selection.

The underlying experiment explicitly describes selection as giving individuals the chance to apply, with enrollment conditional on eligibility/application. citeturn0search0turn0search5

## 4. Preflight gates

| Gate | Result | Reason |
|---|---|---|
| G1 Stable unit | PASS | Individual lottery records are identifiable within the study universe. |
| G2 Pre-treatment state | PASS — bounded | Lottery sign-up and eligibility variables are documented. citeturn0search1 |
| G3 Frozen `U_tau` | **OPEN** | A defensible finite profile of insurance transformations must be specified explicitly rather than assumed from the programme label. |
| G4 Ex-ante `P_tau` | PASS — bounded | Published eligibility/application rules can be fixed before observing outcomes. citeturn0search4 |
| G5 `Z → ΔT_acc` | **BLOCKED** | The design plausibly changes formal application access, but the public data documentation does not by itself provide an already-defined TGCV transformation universe/predicate. |
| G6 Counterfactual | PASS | Lottery provides randomized selected/unselected comparison. citeturn0search0turn0search5 |
| G7 Independent trajectory | PASS — candidate | Longitudinal follow-up exists, but the final Y must be frozen independently. citeturn0search2 |
| G8 No post-treatment leakage | OPEN | Requires executable variable-level specification before any data inspection. |
| G9 Public reproducibility | PASS — bounded | Public-use data and replication materials exist; restricted components cannot be used in the controlled profile. citeturn0search2turn0search3 |
| G10 Stable transition environment | CONDITIONAL | The initial lottery opportunity is bounded in time; later coverage/re-lottery processes must be excluded from the frozen intervention window. |

## 5. Blocking finding

The decisive result is **not** that OHIE lacks causal identification. It has strong randomized causal identification for conventional Medicaid outcomes. The problem is narrower and TGCV-specific: the public documentation does not yet establish an executable, independently frozen `U_tau/P_tau` representation whose treatment contrast is demonstrably a change in the transformation space rather than merely a change in realized insurance coverage.

Therefore the causal result cannot be imported into C09 by relabelling Medicaid coverage as `T_acc`.

## 6. Decision

**C09 OHIE operational preflight = BLOCKED BEFORE EXECUTION.**

OHIE remains the strongest methodological reference identified in this discovery branch, but it is **not yet an admitted C09 execution candidate**.

No C09 claim upgrade.
No data acquisition.
No model fitting.
No execution authorization.
No AWS/Rust/SWIM action.

**Required next operation:** if continuing this branch, perform a variable-level public-data admissibility audit restricted to `U_tau`, `P_tau`, `T_acc,0`, `T_acc,1` and leakage. Do not reopen D-OPS-28 or broaden the discovery search before that audit is completed.
