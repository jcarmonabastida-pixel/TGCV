# TGCV — EXT-UPD-4.8 — Stage A Case Specification Execution Result v0.1

**Status:** CLOSED / STAGE A PASS — CONTROLLED CASE SPECIFICATION ESTABLISHED
**Date:** 2026-09-09
**Authorization:** `EXT-UPD-4.8_TGCV_SCIENTIFIC_AND_INDUSTRIAL_APPLICABILITY_REASSESSMENT_EXECUTION_AUTHORIZATION_v0.1.md`

## 1. Stage-A objective

Determine whether a concrete industrial decision episode can be specified, with a frozen pre-decision boundary, a credible incumbent baseline, a native candidate-option universe and a TGCV-specific analytical output, without observing or using the target outcome to construct the case.

Stage A does not establish industrial utility and does not authorize Stage B.

## 2. Selected industrial case

**Case ID:** IUT-A-01

**Domain:** Manufacturing — machine-level alternative process-plan / tooling decision.

**Native decision episode:** A manufacturing system is preparing to process a new batch/part while the production schedule and available cutting-tool set may differ from the previous state. The decision concerns which process-plan/configuration strategy can be used under the tooling/setup state available at decision time.

The case is selected because the documented industrial literature explicitly distinguishes alternative process plans and machine-level alternatives and frames them as a means of enabling faster decisions. The source describes three decision alternatives at machine level:

1. retain/use a static optimal local process plan;
2. use the current tooling already available on the machine for the new batch;
3. partially set up the machine and use alternative tools not yet in place to accomplish the part.

No performance/result values from the published experiment are used in this Stage-A specification.

## 3. Source provenance

Primary documentary source used for case definition:

Ferreira, J. C. E. & Wysk, R. A. (2001), *An investigation of the influence of alternative process plans on equipment control*, Journal of Manufacturing Systems, 19(6), 393–406. DOI: `10.1016/S0278-6125(01)80011-X`.

Source URL:
`https://www.sciencedirect.com/science/article/pii/S027861250180011X`

The source states that fixed/linear process plans are common in manufacturing and studies machine-specific process-plan alternatives under changing parts, production schedule and dynamic tooling conditions.

## 4. Native state representation

For Stage A the relevant native state is bounded to:

`S_D = (M, Tool, Plan, Setup)`

where:

- `M` = machine/equipment identity and relevant machine capabilities;
- `Tool` = tooling currently available/in place;
- `Plan` = currently defined process-plan state;
- `Setup` = machine setup/configuration state relevant to the decision.

The decision context is:

`C_D = (Part, Batch, ProductionSchedule, ToolRequirements)`

where the components are restricted to information available before the decision.

This representation is intentionally bounded. It is not claimed to be a complete TGCV representation of manufacturing systems.

## 5. Candidate transformation / option universe

The candidate universe is frozen from the native operation classes explicitly exposed by the source:

`Uτ,D = {O1, O2, O3}`

- `O1`: use the static/local process-plan alternative;
- `O2`: execute using tooling currently available on the machine;
- `O3`: partially reconfigure/setup the machine and introduce alternative tooling not currently in place.

No additional transformation class is introduced by TGCV.

Therefore RF-01 is satisfied at the Stage-A specification level: the inclusion universe is the source-defined three-option universe, the inclusion rule is **include exactly the native machine-level alternatives explicitly identified by the source**, and no option is selected because of an observed result.

## 6. Decision-time information boundary

The controlled information boundary is frozen as:

- machine/equipment state;
- tooling currently available;
- current setup state;
- part/batch requirements;
- production schedule relevant to the decision;
- tool requirements known before the decision.

Excluded from construction of the pre-decision representation:

- achieved production performance;
- observed cycle time after the decision;
- achieved quality;
- realized tardiness/throughput;
- any result reported by the source experiment;
- any post-decision information.

## 7. Baseline

**Baseline class:** conventional fixed/linear process-plan representation / incumbent process-plan decision.

This baseline is credible for the case because the source explicitly characterizes fixed linear process plans as the conventional manufacturing practice against which alternative process plans are motivated.

The baseline is frozen before any comparative outcome is considered.

## 8. TGCV-specific output

The first TGCV-specific output to be tested, if Stage B is later authorized, is not the selected production outcome itself. It is:

> **Decision-time identification of which native process-plan/configuration alternatives are accessible under the current state/context, together with the structural state/configuration differences that make each alternative accessible or inaccessible.**

The corresponding local transformation-space representation is:

`T_acc,D(S_t,C_t) ⊆ Uτ,D`

with the explicit understanding that Stage A has established the finite candidate universe but has **not yet empirically closed the native accessibility predicate for every instance**.

## 9. Why this is industrially relevant

The case is a genuine production decision concerning machine configuration, tooling and process-plan alternatives. The documented industrial problem is not an abstract theoretical example: alternative process plans are explicitly motivated as a mechanism for enabling faster and more efficient manufacturing decisions.

The later IUT question would therefore be whether TGCV can identify decision-relevant option-space differences that are not equivalently exposed by the fixed/linear baseline.

## 10. Stage-A comparison metrics frozen for any later Stage B

If Stage B is separately authorized, the comparison boundary must use predefined metrics such as:

- number of decision-relevant native alternatives identified;
- missed-option rate;
- false-option rate;
- time/lead-time to identify an option-space difference, where measurable;
- explanation of configuration/tooling conditions associated with accessibility;
- reproducibility of the analytical classification.

These metrics are capability measures only. They are not financial-value measures.

## 11. Stage-A result

**PASS — CONTROLLED CASE SPECIFICATION ESTABLISHED.**

Reason:

- a concrete industrial decision episode exists;
- native state/context variables can be bounded;
- the candidate option universe is finite and explicitly source-defined;
- RF-01 can be satisfied without outcome-aware selection;
- a credible incumbent baseline can be frozen;
- a distinct TGCV-specific output can be stated;
- the pre-decision information boundary can be frozen;
- the case can proceed to a later comparative test without requiring exhaustive global `T_acc` reconstruction.

## 12. Important limitation

Stage A does **not** establish that `Pτ,D` can be completely evaluated from the source documentation, nor that TGCV outperforms the baseline. Those questions belong to a separately authorized Stage B.

If Stage B requires analyst-supplied feasibility rules, arbitrary discretization, post-outcome information, or unsupported completion of the native model, the case must be classified INDETERMINATE and stopped under the existing hard-stop controls.

## 13. Governance decision boundary

This PASS authorizes only preparation of the next governance decision for Stage B.

It does not authorize:

- comparative IUT measurement;
- data acquisition or processing;
- industrial partner engagement;
- causal inference;
- value linkage;
- superiority claims;
- universal generalization;
- external asset refresh.

**Stage A conclusion: PASS. Stage B: NOT YET AUTHORIZED.**
