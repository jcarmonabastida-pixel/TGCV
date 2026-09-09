# TGCV — IT-G1 Case Identifiability Review — ICD-02

**Date:** 2026-09-09  
**Candidate:** `ICD-02 BPI-2015 Building-permit workflow`  
**Gate:** `IT-G1 Case Identifiability`  
**Decision:** **FAIL / NOT ADMITTED**  
**Execution:** NOT AUTHORIZED  
**Dataset execution:** NO  
**Scientific evidence introduced:** NO

## 1. Scope

This review tests whether ICD-02 can support an independently reconstructable industrial candidate of the form:

`(S_t, C_t) → candidate transformation → accessibility/admissibility conditions → (S_{t+1}, C_{t+1}) → observed outcome`.

The review is documentary only. No dataset was executed and no downstream utility or causal inference was attempted.

## 2. Documentary basis

The BPI 2015 collection contains building-permit applications from five Dutch municipalities over approximately four years. Event logs contain activities, timestamps, resources and cost information; the source documentation also states that procedures, rules and regulations changed over time and that implementation timing could differ between municipalities.

These properties provide a plausible case boundary and temporal structure, but they do not by themselves establish the complete set of alternatives admissible to an actor at each decision time.

## 3. IT-G1 assessment

| Requirement | Result | Finding |
|---|---|---|
| Concrete decision context | PASS-BOUND | Building-permit application handling is a concrete operational process. |
| System boundary S | PASS-BOUND | One application handled within one municipality/process slice can be bounded. |
| Unit of analysis | PASS | One building-permit application is explicitly represented as a case. |
| Temporal frame | PASS | Approximately four years with event timestamps; late 2010–early 2015 in the documented collection. |
| State/context reconstruction | CONDITIONAL | Event history, resources and case-level attributes support partial reconstruction; sufficiency for accessibility decisions is not established. |
| Transformation identity | PASS-CANDIDATE | Logged activities can be identified as realized process actions. |
| Decision-time accessibility/admissibility | **FAIL** | The public event log records realized activities/resources/context, but does not independently specify the full ex-ante set of admissible alternatives and their material/setup/temporal conditions at each decision point. |
| Independent evidence sufficiency | **FAIL** | Documentary evidence is sufficient for case identity but insufficient for independent accessibility closure. |
| Downstream separation | PASS-BOUND | Accessibility, outcomes and utility can remain conceptually separated. |

## 4. Decisive failure

The decisive problem is the same structural distinction that governed ICD-01:

`activity not observed ≠ transformation inaccessible`.

Likewise, observing an activity does not establish that all relevant alternatives were independently identified and admissible at that decision time. The dataset documentation explicitly acknowledges process/rule changes and differing implementation timing across municipalities, which increases the need for an ex-ante accessibility specification rather than supplying one.

Therefore the candidate cannot close IT-G1 under the current governance criteria.

## 5. Non-retroactivity

No TGCV Core definition, threshold, falsification criterion, claim status or epistemic state has been changed to accommodate this result. No downstream outcome or favorable process result has been used to rescue case admissibility.

## 6. Consequence

`ICD-02 = IT-G1 FAIL / NOT ADMITTED`.

It does not advance to IT-G2, dataset execution, utility assessment, causal analysis or value assessment. A future revision would require a separately grounded accessibility protocol capable of specifying ex ante admissible alternatives and their material/setup/temporal conditions, followed by a new governance review.

This is a **candidate-definition/evidence-closure failure, not a scientific failure of TGCV**.
