# TGCV — C09 Retrospective TR-132 Candidate Review 001

**Status:** `COMPLETED — TR-132 REOPENS SCREENING OF SELECTED HISTORICAL REFERENCES / EXECUTION NOT ADMITTED`
**Date:** 2026-09-13
**Parent gate:** `TGCV_C09_TR132_SUFFICIENCY_GATE_001.md`
**Domain gate:** `TGCV_C09_DOMAIN_IDENTIFICATION_GATE_001.md`
**Execution authorization:** `NONE`

## 1. Purpose

Reassess the strongest previously rejected C09 candidates under the newly adopted TR-132 bounded-sufficiency criterion.

This review does not reopen or rewrite the historical audits. It determines which candidates deserve a new, dedicated TR-132 operational sufficiency audit.

## 2. Revised screening principle

The previous blocker:

`complete public system-wide T_acc reconstruction`

is no longer mandatory.

The current requirement is:

`bounded U* + frozen P_tau + identifiable T_acc,0/T_acc,1 within U* + independent trajectory endpoint + credible counterfactual + TR-132 sufficiency`

The candidate remains inadmissible if the causal intervention itself is deficient, if the intervention does not change accessibility in the TGCV sense, if trajectory is not independently reconstructible, or if omitted transformations can alter the causal conclusion.

## 3. Candidate reassessment

### A — MTO Randomized Housing Accessibility

Historical disposition: `CLOSED — STRONG METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED`.

TR-132 reassessment: `REOPEN FOR DEDICATED SUFFICIENCY AUDIT`.

Reason: MTO has randomized LPV/TRV/control assignment, an explicit low-poverty-tract access rule, a credible counterfactual, and long-horizon follow-up. The historical blocker was primarily granularity/provenance for full unit-level T_acc reconstruction, not causal assignment. A bounded U* may be sufficient if it is restricted to the residential transformation class directly affected by the LPV rule and the trajectory endpoint can be independently reconstructed without restricted residential-history data.

Decision: **HIGH PRIORITY TR-132 AUDIT**.

### B — Chicago Voucher Lottery

Historical disposition: `CLOSED — STRONG METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED`.

TR-132 reassessment: `REOPEN FOR DEDICATED SUFFICIENCY AUDIT`.

Reason: randomized voucher allocation directly changes access to a concrete class of housing transformations and provides a counterfactual. The historical blocker was public unit-level reconstruction. TR-132 may allow a bounded housing-transformation profile rather than a complete system-wide housing space, provided the 1997 lottery/access rule and subsequent trajectory can be reconstructed independently.

Decision: **HIGH PRIORITY TR-132 AUDIT**.

### C — NYCHANS Affordable Housing

Historical disposition: `CLOSED — STRONG METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED`.

TR-132 reassessment: `REOPEN FOR DEDICATED SUFFICIENCY AUDIT`.

Reason: randomized affordable-housing offer changes access to a concrete residential transformation; counterfactual and multi-year follow-up are strong. The former complete-public-input blocker may be narrower than necessary if the causal question is bounded to the offered-development transformation class and a sufficient pre-treatment profile can be reconstructed.

Decision: **HIGH PRIORITY TR-132 AUDIT**.

### D — King County Free Transit

Historical disposition: `CLOSED — PROMISING METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED`.

TR-132 reassessment: `REOPEN FOR DEDICATED SUFFICIENCY AUDIT`.

Reason: randomized free-transit access directly changes the affordability predicate for a bounded class of transit transformations while leaving the network environment largely fixed. The previous blocker was incomplete public unit-level data, not treatment assignment. TR-132 can test whether a frozen route/journey profile is sufficient without reconstructing every possible trip in the network.

Decision: **MEDIUM-HIGH PRIORITY TR-132 AUDIT**.

### E — Naturalization Fee Voucher

Historical disposition: `CLOSED — PROMISING METHODOLOGICAL REFERENCE / EXECUTION NOT ADMITTED`.

TR-132 reassessment: `REOPEN FOR DEDICATED SUFFICIENCY AUDIT`.

Reason: exceptionally clean randomized intervention removing a fee barrier to initiating a defined transformation. The prior blocker was incomplete public unit-level data. A bounded U* containing the application-initiation transformation may be sufficient if the trajectory endpoint can be independently reconstructed and omitted transformations cannot alter the declared causal contrast.

Decision: **MEDIUM-HIGH PRIORITY TR-132 AUDIT**.

### F — Oregon Health Insurance Experiment (OHIE)

Historical disposition: `CLOSED AS C09 EXECUTION CANDIDATE UNDER CURRENT PUBLIC-VARIABLE/FIREWALL STANDARD`.

TR-132 reassessment: `REOPEN FOR DEDICATED SUFFICIENCY AUDIT — CONDITIONAL`.

Reason: the former blocker was not merely missing system-wide data; it was the need to construct a TGCV transformation taxonomy independently of realized enrollment. TR-132 permits a programme-action-level U* if that bounded profile is demonstrably sufficient for the declared causal contrast. The audit must therefore prove that `initiate_OHP_Standard_application` (and any necessary bounded successor action) is a sufficient transformation profile rather than an ad-hoc relabelling of conventional insurance take-up.

Decision: **MEDIUM PRIORITY TR-132 AUDIT**.

### G — Charlotte-Mecklenburg School-Choice Lottery

Historical disposition: `CLOSED — PROMISING REFERENCE / EXECUTION NOT ADMITTED`.

TR-132 reassessment: `REOPEN FOR DEDICATED SUFFICIENCY AUDIT — CONDITIONAL`.

Reason: randomized lottery access to concrete school-enrollment alternatives is strong, but the previous audit identified a conceptual distinction between formal eligibility, realizable allocation and realized enrollment. TR-132 can only reopen this candidate if a bounded U* cleanly represents the accessibility distinction without conflating these layers.

Decision: **MEDIUM PRIORITY TR-132 AUDIT**.

### H — EDR demand-response

Historical disposition: `CLOSED — CANDIDATE REJECTED FOR C09 CAUSAL EXECUTION`.

TR-132 reassessment: `DO NOT REOPEN`.

Reason: the decisive blocker was not completeness of T_acc but failure of the required causal mapping `Z → ΔT_acc`. The intervention evidence supports access/notification/incentive exposure followed by behaviour, not a demonstrated transformation-space change. TR-132 cannot repair this identification mismatch.

### I — eBay search-ranking experiment

Historical disposition: `CLOSED — CANDIDATE NOT ADMITTED FOR C09 CAUSAL EXECUTION`.

TR-132 reassessment: `DO NOT REOPEN`.

Reason: the critical failure is conceptual: ranking/visibility changed, not demonstrably the underlying transformation accessibility space. Public-data availability is a secondary blocker. TR-132 does not permit redefining visibility as T_acc post hoc.

### J — Ethereum protocol interventions

Historical disposition: `CLOSED — NO ETHEREUM INTERVENTION ADMITTED FOR C09 CAUSAL EXECUTION`.

TR-132 reassessment: `DO NOT REOPEN`.

Reason: the critical intervention failure is lack of isolated accessibility treatment: protocol upgrades alter the transition environment and multiple execution rules. TR-132 cannot isolate the causal pathway.

### K — Railway/RINF historical path

Historical disposition: `BLOCKED under public-only longitudinal replication`.

TR-132 reassessment: `DO NOT REOPEN AT THIS STAGE`.

Reason: the blocker is historical state recovery itself. Without an independently reproducible pre/post state archive, a bounded sufficiency argument cannot be grounded in the required evidence. This does not justify reopening D-OPS-10–14.

## 4. Ranked output

| Rank | Candidate | TR-132 disposition | Main remaining question |
|---|---|---|---|
| 1 | MTO | Reopen | Can a bounded residential U* + public outcome/trajectory representation suffice? |
| 2 | Chicago voucher lottery | Reopen | Can the lottery/access rule define a sufficient bounded housing U*? |
| 3 | NYCHANS | Reopen | Can offered-development transformations form a sufficient U* with independent trajectory? |
| 4 | King County free transit | Reopen | Can a bounded transit journey profile suffice without restricted tap data? |
| 5 | Naturalization fee voucher | Reopen | Is application-initiation U* sufficient for the declared trajectory contrast? |
| 6 | OHIE | Conditional reopen | Can programme-action U* be justified without ad-hoc ontology? |
| 7 | School-choice lottery | Conditional reopen | Can eligibility, realizability and realization be separated within U*? |
| — | EDR | Do not reopen | `Z → ΔT_acc` not demonstrated |
| — | eBay | Do not reopen | intervention changes visibility, not demonstrated T_acc |
| — | Ethereum | Do not reopen | intervention not isolated from transition environment |
| — | Railway/RINF | Do not reopen | historical state recovery blocker |

## 5. Decision

**TR-132 retrospective review = PASS AS SCREENING REASSESSMENT.**

The new gate materially changes the candidate landscape: at least seven previously rejected methodological references are no longer rejectable solely because they lack complete system-wide/public `T_acc` reconstruction.

This does **not** mean that any of the seven is a C09 execution candidate. Each requires a dedicated TR-132 audit, and execution authorization remains `NONE`.

The highest-information next operation is a dedicated **MTO TR-132 Sufficiency Audit**, followed by Chicago voucher lottery if MTO fails.

No claim-matrix upgrade.
No C09 causal result.
No data acquisition.
No model fitting.
No AWS/Rust/SWIM execution.
