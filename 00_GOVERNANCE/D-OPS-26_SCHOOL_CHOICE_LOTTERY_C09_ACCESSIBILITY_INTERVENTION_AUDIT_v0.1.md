# D-OPS-26 — School-Choice Lottery C09 Accessibility Intervention Audit v0.1

**Status:** `CLOSED — PROMISING REFERENCE / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Execution:** `NOT AUTHORIZED`
**Candidate:** Charlotte-Mecklenburg public-school choice lottery

## 1. Purpose

Assess whether randomized school admission can satisfy the strengthened C09 requirement: an independently assigned intervention must change a bounded transformation-accessibility space `T_acc`, with a credible counterfactual trajectory and reproducible provenance.

## 2. Evidence

Charlotte-Mecklenburg's 2002 school-choice system required families to rank schools; students were guaranteed a neighborhood-school place, while oversubscribed schools allocated remaining places through a lottery. The documented mechanism used priority groups and lottery numbers. citeturn4search6turn4search8

Longitudinal causal studies used lottery assignment to estimate effects on school outcomes and postsecondary attainment. One study follows students through 2009; another links administrative school records to National Student Clearinghouse outcomes. citeturn4search8turn4search4

A replication package is publicly registered at OpenICPSR, but the listed materials are code and documentation rather than the underlying restricted administrative microdata. citeturn4search10

## 3. Gate assessment

| Gate | Result | Finding |
|---|---|---|
| Stable unit/state | PASS — bounded | Student identity, school assignment and longitudinal outcomes are reconstructible in the original administrative environment. |
| Formal rule layer | PASS — bounded | Priority groups, capacity constraints and lottery assignment are explicitly documented. |
| Independently assigned intervention | PASS | Lottery number determines admission among applicants within the relevant priority/capacity structure. |
| Bounded `U_tau` | CONDITIONAL PASS | Candidate transformations can be defined as admissible school-enrollment choices for a frozen admissions round. |
| Pre-execution `P_tau` | PASS — bounded | Eligibility, priority and capacity rules precede the realized lottery outcome. |
| `Z → ΔT_acc` | **CONDITIONAL / NOT YET DEMONSTRATED** | Winning the lottery changes the student's realized admission opportunity, but the experiment does not directly define `T_acc` as a transformation space and does not independently enumerate all admissible enrollment transformations. |
| Counterfactual | PASS | Random lottery supplies a credible within-applicant counterfactual. |
| Subsequent trajectory | PASS — bounded | Longitudinal educational outcomes are documented through multiple years. |
| Transition environment | CONDITIONAL | School environment and assignment rules can evolve across years; the C09 unit/horizon would need to freeze the relevant admissions round and subsequent trajectory window. |
| Public reproducibility | **FAIL for direct execution** | Underlying administrative microdata are restricted; the public replication package does not supply the raw student-level data. |

## 4. Critical C09 distinction

The candidate is stronger than eBay because the lottery changes **admission/access to a concrete alternative transformation** rather than merely changing information ordering.

A bounded representation is plausible:

`S_t,C_t → U_tau → P_tau → T_acc,t`

where candidate transformations include enrollment in schools for which the student is eligible to apply, and lottery assignment changes which requested enrollment transformation becomes accessible.

However, the decisive unresolved issue is whether this can be specified without conflating:

- the set of transformations the student is formally eligible to request;
- the set of transformations the allocation mechanism makes realizable; and
- the single transformation actually realized after admission.

C09 requires an ex-ante, independently defined accessibility space, not an accessibility definition inferred from the observed lottery winner's subsequent enrollment.

## 5. Reproducibility constraint

The causal design is strong, but direct TGCV execution is not currently reproducible from the public record because the underlying administrative microdata remain restricted. The publicly registered replication package contains analysis materials rather than the source microdata. citeturn4search10

Therefore the candidate cannot presently pass the execution-level provenance gate.

## 6. Decision

**D-OPS-26 = CLOSED — PROMISING REFERENCE / EXECUTION NOT ADMITTED.**

The school-choice lottery is retained as a high-value methodological reference because it combines:

1. explicit allocation/admission rules;
2. randomized access to a concrete alternative;
3. long-horizon downstream outcomes; and
4. documented counterfactual identification.

But it is **not admitted as C09 execution evidence** because `Z → ΔT_acc` still requires a non-ad-hoc operationalization and the underlying longitudinal microdata are not publicly reproducible.

No C09 claim upgrade follows.

## 7. Discovery implication

The strongest remaining search class is now narrower:

`formal allocation/admission rule + randomized or quasi-exogenous unit-level access + explicit transformation-level accessibility + public/reproducible longitudinal state data`.

Candidates failing the final public-data/provenance condition should remain references rather than being promoted to execution candidates.

No data acquisition, model fitting, execution, AWS mutation, Rust rerun or SWIM rerun is authorized.
