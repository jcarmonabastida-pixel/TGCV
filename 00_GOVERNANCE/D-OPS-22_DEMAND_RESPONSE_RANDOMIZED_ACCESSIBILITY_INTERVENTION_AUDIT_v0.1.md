# D-OPS-22 — Demand Response Randomized Accessibility Intervention Audit v0.1

**Status:** `CLOSED — PROMISING C09 CANDIDATE / EXECUTION NOT ADMITTED`
**Date:** 2026-09-12
**Execution:** `NOT AUTHORIZED`

## 1. Candidate

Randomized electricity demand-response access interventions, with the strongest concrete evidence currently being the 2023–2019 emergency demand-response programme and the 2026 Spain demand-side-response RCT registration.

The 2019 southwestern-China EDR study randomly assigned permission to apply for an emergency demand-response trial. The final sample retained 205,129 households and used 15-minute smart-meter observations. The assignment created notification/eligibility groups and a control group; the study explicitly interprets the ITT as the causal effect of expanding access to EDR. citeturn1search6turn1search11

A 2026 Spanish RCT registration reports 108,163 residential customers randomly assigned across six groups during demand-response events, providing an unusually direct contemporary Spanish longitudinal intervention design. citeturn1search0

## 2. C09 screen

### Stable unit / longitudinal state

**PASS — bounded.**

Household identity and high-frequency electricity consumption provide a reconstructible state trajectory in the cited experimental designs. The China study uses 15-minute smart-meter measurements and a defined sequence of intervention events. citeturn1search6turn1search11

### Independently assigned accessibility intervention

**PASS — strongest result in current discovery.**

The China EDR experiment randomly assigned permission to apply for the programme. This is materially closer to the TGCV C09 requirement than the previously audited regulatory-rule changes because treatment assignment is randomized at the unit/cluster level. citeturn1search11

The intervention can be represented as changing access to an admissible demand-response transformation without assigning the downstream electricity trajectory itself.

### Formal rule layer

**CONDITIONAL PASS.**

The EDR programme has explicit eligibility, event, rebate and baseline rules. However, the current public evidence does not yet establish that these rules constitute an independently governed formal transition system equivalent to the stronger rule-layer requirement used for Ethereum or the electricity-system P.O. 7.5 audit.

Therefore the candidate is not yet admitted.

### Counterfactual

**PASS — experimental.**

Random assignment supplies a credible control/counterfactual structure. This is a major improvement over railway, Ethereum and the Spanish P.O. 7.5 candidate. The causal literature explicitly frames randomized access/assignment as an ITT estimand for expanding access to the intervention. citeturn1search6turn1search11

### No direct trajectory encoding

**PASS — preliminary.**

Assignment grants eligibility/access and incentive exposure; it does not specify the household's subsequent consumption path. The observed response therefore remains downstream of the intervention rather than being directly encoded by it. This must nevertheless be verified against the frozen intervention protocol before any execution.

## 3. Critical remaining gate

The unresolved issue is now sharply localized:

> Can the demand-response programme's eligibility/accessibility rule be formalized as an independently governed `P_tau` over a finite, pre-event transformation universe `U_tau`, while the randomized access assignment changes `T_acc` without changing the underlying transition law or directly defining the outcome trajectory?

If YES, this candidate could satisfy the full C09 architecture more closely than every candidate audited so far.

If NO, it remains a causal intervention reference but not a TGCV C09 execution domain.

## 4. Decision

**D-OPS-22 = CLOSED — PROMISING C09 CANDIDATE / EXECUTION NOT ADMITTED.**

This is the first discovery result in the current pass where the accessibility intervention itself is randomized at unit/cluster level while a longitudinal system state is directly observed. It therefore merits a dedicated formal-rule admissibility audit rather than immediate rejection.

No C09 claim upgrade follows.

## 5. Next controlled operation

Perform a **Demand-Response Formal Rule / U_tau / P_tau Admissibility Audit**, using only publicly documented intervention rules and preregistered design information. The audit must determine whether the access intervention can be represented as a change in transformation accessibility rather than merely as an ordinary behavioural treatment.

No execution, model fitting, data acquisition, AWS mutation, Rust rerun or SWIM rerun is authorized.
