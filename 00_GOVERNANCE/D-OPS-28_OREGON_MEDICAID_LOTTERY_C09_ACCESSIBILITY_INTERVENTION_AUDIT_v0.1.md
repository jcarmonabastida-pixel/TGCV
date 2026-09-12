# D-OPS-28 — Oregon Medicaid Lottery C09 Accessibility Intervention Audit v0.1

**Status:** `CLOSED — PROMISING C09 CANDIDATE / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Execution:** `NOT AUTHORIZED`
**Candidate:** Oregon Health Insurance Experiment (OHIE), 2008 Medicaid lottery

## 1. Purpose

Audit whether the OHIE provides the required combination of randomized unit-level access, ex-ante transformation accessibility, longitudinal state/trajectory data and public reproducibility for C09.

## 2. Evidence

Oregon used lottery selection to allocate scarce openings in a previously closed Medicaid programme. Selected individuals received the opportunity to apply; unselected individuals could not apply during the initial lottery period. The lottery was conducted in eight draws from March through September 2008. citeturn1search0turn1search6

The ICPSR collection contains the lottery sign-up list, lottery draw and selection information, application/approval information, Medicaid enrollment records and multiple follow-up sources for 2007–2010. Public-use files are available. citeturn1search2turn1search8

## 3. Gate assessment

| Gate | Result | Finding |
|---|---|---|
| Stable unit/state | PASS — bounded | Individual/household lottery unit and pre-lottery variables are documented. |
| Formal rule layer | PASS — bounded | Eligibility and OHP Standard application/enrollment rules are explicitly specified. |
| Independent intervention | PASS | Lottery selection was randomized. |
| Bounded `U_tau` | **CONDITIONAL PASS** | A bounded transformation universe can be defined as insurance-state transitions permitted to an eligible lottery participant during the frozen study window. |
| Pre-execution `P_tau` | PASS — bounded | Eligibility and programme constraints precede realized coverage and downstream outcomes. |
| `Z → ΔT_acc` | **PASS — BOUNDED DESIGN CANDIDATE** | Lottery selection changes whether the individual is permitted to apply for OHP Standard, thereby changing the admissible insurance-enrollment transformation space relative to controls. The mapping must be frozen before outcome inspection. |
| Counterfactual | PASS | Randomized lottery supplies the control condition. |
| Longitudinal trajectory | PASS — bounded | Enrollment and follow-up outcomes extend from pre-lottery periods through 2009/2010. citeturn1search0turn1search5 |
| Transition environment | CONDITIONAL PASS | The Medicaid programme rules are fixed for the initial lottery window, but later lottery waves affect longer follow-up; C09 must freeze an initial cohort and observation horizon before the later re-lottery. |
| Public reproducibility | **PASS — BOUNDED** | ICPSR and NBER provide public-use data and replication materials; restricted files also exist, so the admissible C09 profile must rely only on public variables. citeturn1search2turn1search3turn1search8 |

## 4. Critical TGCV mapping

A bounded operational mapping is plausible:

`S_0,C_0 → U_tau → P_tau(Z) → T_acc(Z) → S_1,C_1 → trajectory`

Here the transformation universe is not “health outcomes”. It is the set of eligible insurance-enrollment transitions defined for the frozen Medicaid programme and observation window. Lottery selection changes the pre-outcome permission to initiate the Medicaid-enrollment transformation.

This is materially different from eBay ranking and from EDR information/incentive exposure: the intervention changes a **formal permission to execute a concrete state transition**.

## 5. Critical remaining issue

The main unresolved issue is **unit-level construction of `U_tau` and `P_tau` from the public-use variables without importing post-treatment enrollment or outcome information**.

A C09 execution package must therefore demonstrate, before execution:

1. a finite frozen insurance-transformation profile;
2. ex-ante eligibility predicates;
3. `T_acc,0` for selected and unselected units using only pre-lottery information and the formal programme rule;
4. `T_acc,1` under lottery permission without defining it from realized enrollment;
5. an observation horizon ending before the later re-lottery contaminates the original control condition;
6. an independently defined trajectory `Y` distinct from treatment/accessibility;
7. reproducibility using only public-use data and published rule documentation.

## 6. Decision

**D-OPS-28 = CLOSED — PROMISING C09 CANDIDATE / EXECUTION NOT ADMITTED.**

OHIE is retained as the **highest-priority candidate for a dedicated C09 operational preflight** because, unlike previous candidates, the public evidence supports all major structural ingredients simultaneously:

- randomized unit-level access;
- explicit formal eligibility/application rules;
- a direct permission change affecting a concrete transformation;
- a credible counterfactual;
- longitudinal administrative/follow-up data; and
- public-use data sufficient for a bounded feasibility reconstruction.

This is a **screening result only**, not causal TGCV evidence. The next operation, if pursued, is a dedicated C09 OHIE operational preflight focused exclusively on proving `Z → ΔT_acc` from public variables without leakage or post-hoc redefinition.

No C09 claim upgrade follows from this audit.

No data acquisition, model fitting, execution, AWS mutation, Rust rerun or SWIM rerun is authorized.
