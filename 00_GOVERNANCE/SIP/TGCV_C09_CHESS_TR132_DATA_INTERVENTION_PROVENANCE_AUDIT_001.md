# TGCV — C09 CHESS TR-132 Data / Intervention Provenance Audit 001

**Status:** `COMPLETED — CANDIDATE REJECTED FOR C09 EXECUTION / INTERVENTION-ACCESSIBILITY MAPPING FAIL`
**Date:** 2026-09-13
**Candidate:** CHESS (Comprehensive intelligent Hypertension managEment SyStem) RCT
**Execution authorization:** `NONE`

## 1. Scope

Assess whether the public CHESS dataset and trial protocol jointly support an ex-ante, bounded representation of `T_acc,0/T_acc,1` rather than merely treatment assignment and health outcomes.

The public Dryad record contains 1,666 individual-level records with treatment assignment, baseline characteristics and follow-up outcomes. citeturn0search0

## 2. Findings

### P1 — Randomized intervention

**PASS.**

CHESS is a cluster-randomized trial: primary-care sites were randomized to usual care or the CHESS intervention. The protocol reports 41 sites and more than 1,600 patients followed for 12 months. citeturn0search4turn0search8

### P2 — Decision-time state

**PASS.**

The public dataset includes baseline clinical, demographic and behavioural variables measured before follow-up, and the protocol defines the intervention from the randomized site assignment. citeturn0search0turn0search4

### P3 — Accessibility intervention

**FAIL — CONSTRUCT MISFIT.**

CHESS is a multifaceted management intervention rather than a rule that directly changes which transformations are admissible to the patient. It provides home blood-pressure monitoring, automated reminders/alerts, physician decision support and provider quality feedback. The intervention is explicitly designed to change management behaviour and clinical decision processes. citeturn0search4turn0search3

Those components may change behaviour, information, treatment decisions and subsequent states, but the protocol does not define an ex-ante transformation universe whose membership changes from `T_acc,0` to `T_acc,1` as a direct consequence of the intervention.

### P4 — Unit-level `T_acc,0/T_acc,1`

**FAIL.**

The public CSV provides a `group` treatment indicator and clinical/outcome variables, but no operational representation of a bounded transformation universe or accessibility predicates. citeturn0search0

Defining `T_acc,1` as "all actions enabled by CHESS" would be post-hoc and underspecified; defining it as medication adherence, BP monitoring, clinical visits or observed behaviours would replace accessibility with realized behaviour.

### P5 — Independent trajectory endpoint

**PASS.**

The protocol fixes a 12-month endpoint, with primary outcome mean change in 24-hour ambulatory systolic BP from baseline to 12 months. The public dataset contains follow-up measurements including ambulatory BP indicators. citeturn0search0turn0search4

### P6 — Public reproducibility

**PASS — DATA AVAILABILITY ONLY.**

The individual-level dataset is publicly available and explicitly documents treatment assignment and variables. citeturn0search0

This resolves the provenance problem but does not resolve the TGCV construct problem.

### P7 — TR-132 sufficiency

**FAIL.**

The omitted-path argument cannot be completed because no intervention-defined bounded transformation universe and accessibility predicates are specified. Public data availability cannot compensate for a construct-level failure.

## 3. Decision

**CHESS = REJECTED FOR C09 EXECUTION.**

The candidate demonstrates an important distinction: **public unit-level data are necessary but not sufficient for C09**. The intervention must itself support an ex-ante accessibility-space representation.

No treatment indicator as `T_acc`.
No observed behaviour as `T_acc`.
No clinical outcome as accessibility.
No restricted-data request.
No causal execution.
No matrix upgrade.
No Core change.
No execution authorization.

## 4. Search implication

The discovery criterion is refined again: prioritize interventions that modify an explicit **rule, permission, eligibility condition, capacity, route, option set or admissible action set**, where the changed accessibility state can be represented before outcomes are observed. Pure behavioural, informational or management interventions are excluded unless their intervention specification explicitly changes such a rule or option set.

**Next operation:** targeted discovery of a public operational dataset with an explicit randomized rule/permission/access intervention.
