# TGCV — C09 Naturalization Fee Voucher TR-132 Operational Preflight 001

**Status:** `COMPLETED — PRE-FLIGHT BLOCKED / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Candidate:** NaturalizeNY naturalization-fee voucher lottery
**Parent:** `TGCV_C09_RETROSPECTIVE_TR132_CANDIDATE_REVIEW_001.md`
**Execution authorization:** `NONE`

## 1. Candidate definition

NaturalizeNY randomized low-income lawful permanent residents into an offer of a voucher covering the naturalization application fee versus no voucher. The 2016 voucher-lottery sample contained 863 registrants, with 336 winners and 527 non-winners; later cohorts expanded the programme. The intervention materially increased naturalization applications. citeturn1search1turn1search0

## 2. Proposed bounded C09 representation

`U* = naturalization-application transformation available to an eligible registrant during the frozen application window.`

`P0(τ) = application transformation requires payment of the applicable naturalization fee.`

`P1(τ) = same application transformation is financially admissible because the randomized voucher covers the applicable fee.`

The causal intervention is the randomized voucher offer, not actual application or citizenship attainment.

## 3. Operational gates

### P1 — Randomized intervention

**PASS.**

The voucher was assigned by lottery among eligible registrants, creating a clean treatment/control contrast. citeturn1search1turn1search0

### P2 — Decision-time unit and pre-treatment state

**PASS — DESIGN LEVEL.**

The registration process collected individual demographic and socioeconomic information before randomization, including income, employment, education and green-card history. The randomization block was also defined before treatment. citeturn1search0

### P3 — Accessibility intervention

**PASS — CONCEPTUAL / BOUNDED.**

This is unusually clean for TR-132: the intervention removes a specified financial barrier to one clearly defined transformation — submitting a naturalization application. The voucher could only be used to pay that application fee. citeturn1search1

### P4 — Unit-level `T_acc,0/T_acc,1`

**CONDITIONAL PASS — CONCEPTUAL, NOT PUBLICLY RECONSTRUCTIBLE.**

At the rule level, the transformation and accessibility contrast are explicit: the same eligible application is financially inaccessible under the full-fee condition for the targeted low-income group and accessible with the voucher. However, a unit-level TGCV representation still requires the admissible package to identify the relevant pre-treatment eligibility state and frozen transformation universe for each randomized unit.

The published 2026 study states that its analysis combines individual-level programme registration data, follow-up surveys and matched administrative credit-bureau records; it does not establish a public-use household/registrant microdata release containing the randomized lottery data and unit-level longitudinal outcomes. citeturn1search0

### P5 — Independent trajectory endpoint

**CONDITIONAL PASS — DATA ACCESS BLOCKER.**

The study has longitudinal outcomes including income, credit scores, financial distress, credit access and broader integration measures for periods before and after the lottery. The causal contrast is well defined, but the required unit-level outcome data are part of the study's linked research data rather than an established unrestricted public-use package. citeturn1search0turn1search20

### P6 — Public reproducibility

**FAIL / NOT ESTABLISHED.**

The available public documentation describes confidential programme information and follow-up surveys, while the 2026 analysis explicitly uses matched administrative credit-bureau data. Public descriptions of NaturalizeNY also state that participant survey information was confidential. citeturn2search6turn1search0

No public replication package was identified that provides the randomized registrant-level assignment, frozen unit-level accessibility representation and admissible longitudinal endpoint required for a TGCV C09 reconstruction.

### P7 — TR-132 omitted-path sufficiency

**NOT ADMITTED.**

The rule-level accessibility contrast is sufficiently clear, but operational sufficiency cannot be demonstrated without an admissible unit-level data package. Treatment assignment cannot substitute for `T_acc`, and published aggregate treatment effects cannot reconstruct the missing unit-level representation.

## 4. Decision

**NATURALIZATION FEE VOUCHER = PRE-FLIGHT BLOCKED / EXECUTION NOT ADMITTED.**

This candidate is scientifically attractive for C09 because the intervention directly removes a clearly defined financial accessibility barrier to a bounded transformation. It nevertheless fails the current reproducibility gate because the required randomized unit-level data and independent longitudinal endpoint are not established as publicly reproducible.

No inference from lottery assignment to `T_acc`.
No substitution of naturalization/application status for accessibility.
No use of confidential or restricted participant data.
No restricted-data request.
No causal execution.
No matrix upgrade.
No Core change.
No execution authorization.

## 5. Candidate disposition

Retain as a **strong methodological reference** and as a particularly clean conceptual example of an accessibility intervention. Do not reopen for execution unless a legitimately accessible unit-level package satisfying TR-132 becomes available.

**Next operation:** evaluate **OHIE (Oregon Health Insurance Experiment)** under the controlled TR-132 operational-preflight gate.
