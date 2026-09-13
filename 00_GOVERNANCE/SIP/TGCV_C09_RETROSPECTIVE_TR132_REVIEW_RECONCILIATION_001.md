# TGCV — C09 Retrospective TR-132 Review Reconciliation 001

**Status:** `COMPLETED — NO CANDIDATE ADMITTED FOR EXECUTION`
**Date:** 2026-09-13
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories
**Parent:** `TGCV_C09_DOMAIN_IDENTIFICATION_GATE_001.md`

## 1. Purpose

Close the current retrospective candidate-review batch by reconciling the candidate-specific preflight dispositions against the controlling C09 identification and TR-132 gates.

TR-132 requires bounded sufficiency for the declared causal contrast; it does not require complete system-wide `T_acc`. fileciteturn47file0L2-L2

## 2. Batch disposition

| Candidate | Current disposition | Decisive blocker |
|---|---|---|
| SWIM Reactive | `REJECTED FOR C09 CAUSAL EXECUTION` | no controlled accessibility intervention/counterfactual |
| Chicago Voucher Lottery | `CLOSED FOR C09 CAUSAL EXECUTION` | unit-level accessibility/outcome provenance not publicly reproducible |
| NYCHANS | `PRE-FLIGHT BLOCKED` | unit-level randomized linkage not publicly reproducible |
| King County Free Transit | `PRE-FLIGHT BLOCKED` | unit-level `T_acc,0/T_acc,1` not publicly reproducible |
| Naturalization Fee Voucher | `PRE-FLIGHT BLOCKED` | randomized unit-level longitudinal package not publicly reproducible |
| OHIE | `PRE-FLIGHT BLOCKED` | unit-level bounded accessibility representation not demonstrated |
| Charlotte-Mecklenburg School Choice | `PRE-FLIGHT BLOCKED` | underlying randomized student-level data not publicly reproducible |
| CHESS | `REJECTED FOR C09 EXECUTION` | intervention does not provide an ex-ante accessibility-space mapping |

The candidate-specific records explicitly reject substituting treatment assignment, realized behaviour, utilization, attendance or outcome variables for `T_acc`. 

## 3. Key finding

The retrospective review has not identified a candidate that simultaneously satisfies:

`independent accessibility intervention + defensible counterfactual + bounded TR-132 representation + unit-level reproducibility + direct-effect exclusion`.

The dominant failure mode is no longer simply “complete system-wide `T_acc` unavailable”. After adoption of TR-132, several candidates fail for the narrower and more decisive condition that the **bounded causal accessibility representation cannot be independently reconstructed from the admissible package**, or that the intervention itself does not instantiate an accessibility-space change.

## 4. Scientific interpretation

This batch does **not** falsify C09 and does not establish C09.

It establishes a methodological boundary: conventional randomized intervention studies can possess strong causal identification and rich longitudinal outcomes while still failing the TGCV-specific requirement to represent an ex-ante accessibility-space intervention at unit level.

This is methodological evidence about candidate admissibility, not evidence for the truth of C09.

## 5. Governance consequence

`EXECUTION AUTHORIZATION = NONE`

No dataset acquisition, restricted-data request, external intervention, SWIM rerun, AWS mutation, causal execution, matrix upgrade or Core modification follows from this reconciliation.

Historical candidate records remain immutable. The reconciliation only establishes their current routing under the controlling C09/TR-132 gates.

## 6. Next operation

The retrospective batch is closed. Before reopening another candidate family, perform a **C09 candidate-class decision gate**: determine whether the remaining candidate search should continue externally for a public operational dataset with an explicit rule/permission/access intervention, or whether C09 requires a new controlled synthetic/experimental domain specifically designed to satisfy the accessibility-intervention and TR-132 conditions.
