# TGCV — C09 EDR Bounded Causal Preflight 001

**Status:** `COMPLETED — BLOCKED BEFORE EXECUTION`
**Date:** 2026-09-13
**Candidate:** Southwestern-China EDR 2019
**Parent:** `TGCV_C09_EDR_BOUNDED_CAUSAL_OPERATIONAL_SPECIFICATION_001.md`
**Execution authorization:** `NONE`

## 1. Purpose

Assess whether the published EDR evidence is sufficient to freeze a bounded C09 causal execution package without acquiring or executing the underlying dataset.

## 2. Preflight results

| Gate | Result | Reason |
|---|---|---|
| Stable household/event unit | PASS | Household identity and event assignment are documented. |
| Temporal boundary | PASS | Six trials and a fixed 20:00–21:30 response window are documented. |
| Randomized assignment | PASS | Permission/access was randomized at community/region level and treatment/control groups are documented. |
| Longitudinal observation | PASS | 15-minute smart-meter observations and historical electricity-use data are documented. |
| Bounded `U_tau` | **OPEN / NOT DEMONSTRATED** | Publication reports consumption outcomes, but does not provide a frozen enumerable transformation-class universe corresponding to TGCV `U_tau`. |
| Ex-ante `P_tau` | **OPEN / NOT DEMONSTRATED** | Programme participation/eligibility is documented, but its mapping to a transformation-level accessibility predicate is not independently reconstructible from the published evidence alone. |
| `Z → ΔT_acc` | **FAIL — CRITICAL** | Random assignment changes access/notification/rebate exposure, but the evidence does not establish that the TGCV transformation space itself changes rather than only the incentive/payoff attached to available demand reduction. |
| No direct trajectory encoding | PASS — preliminary | Assignment does not prescribe a particular consumption sequence. |
| Counterfactual | PASS | Randomized design provides treatment/control comparison for the experimental policy. |
| Independent trajectory reconstruction | PASS — bounded | 15-minute consumption series permit downstream trajectory representation in principle. |
| Information firewall | PASS — designable | Pre-treatment assignment and event variables can be frozen; outcome variables can be excluded. |
| Provenance/integrity | OPEN | Source publication is identifiable, but a frozen machine-readable input package and hashes are not yet available. |

## 3. Critical finding

The existing publication establishes a strong randomized intervention on EDR **access/participation opportunity**, and it establishes causal effects on electricity use. It does **not yet establish the TGCV-specific manipulation condition**:

`Z → ΔT_acc`

The intervention may instead be represented as:

`Z → incentive/information/participation exposure → behavior → Y`

without demonstrating that the set/structure of admissible transformations `T_acc` changed.

The paper explicitly describes the intervention in terms of messages, confirmation, participation and monetary rebate, and estimates an ITT effect of the experimental EDR policy. citeturn0search0turn0search1

This distinction is decisive under the frozen TGCV C09 operational specification.

## 4. Decision

**C09 EDR BOUNDED PREFLIGHT = BLOCKED BEFORE EXECUTION.**

No dataset execution is authorized.

The candidate remains scientifically useful as a **causal-design reference**, but it is not yet an admissible TGCV C09 execution candidate.

## 5. Required next operation

Do not run the published dataset and do not reinterpret the existing causal result as C09 evidence.

The next controlled operation is a **bounded accessibility-mapping audit** asking whether the EDR protocol can support an independently specified transformation universe and accessibility predicate in which randomized access demonstrably changes `T_acc` while the trajectory outcome remains downstream and independently defined.

If this cannot be demonstrated from the protocol/data structure without post-hoc construction, the candidate must be rejected for C09 causal execution.

**No AWS mutation, Rust rerun, SWIM rerun, model fitting or external execution is authorized.**
