# DEC-C10-096 — B1/Need_preZ validation cohort census and task boundary

**Date:** 2026-11-12  
**Status:** ACCEPTED WORKING DESIGN DECISION — NOT DESIGN FREEZE  
**Scope:** Validation cohort for B1/Need_preZ adjudication  
**Branch:** research/c10-s-consolidation-draft · PR #116 (Draft)

## 1. Decision

Following the user's explicit acceptance on 2026-11-12 of the proposed validation-cohort scope, adopt the following working design:

**The B1/Need_preZ validation cohort is the census of all experimental units (UE) in the approved, versioned DGP/package roster to which the B1/Need analytical package applies.** No convenience subcohort is selected.

Membership is determined ex ante from roster identity/version, UE identity and valid B1↔UE↔service-instance binding, before truth/evidence is opened and before Z. It is not determined by Need truth, evidence availability/coverage, adjudication outputs, treatment assignment/compliance or outcomes.

If A/B rosters remain separate, the applicable roster is the exact approved DGP/package roster for the B1/Need package. If a joint roster is approved, include every UE in that roster to which the package applies. This decision does not choose between separate and joint A/B rosters.

## 2. Evaluation task boundary

The cohort evaluates **E1 and E2 as independent adjudicators of observed Need_preZ**:
- both receive the same authorized observable case bundle;
- neither receives TRUTH_LEDGER, truth_basis_ref, reconstructive metadata or the other's output before sealing;
- each output is evaluated separately against Need_truth after both are sealed;
- inter-adjudicator agreement is reported separately from accuracy against DGP truth.

Analyzer PE is **not** a Need classifier and is outside this cohort's Need-classification denominators. Its PE outputs and evaluation against construct/estimand-specific DGP oracles remain separate. A PE estimand may consume an observed Need variable only if its own contract explicitly requires it; neither truth nor E1/E2 outputs are injected by default.

## 3. Census flow and denominators

All roster units remain visible in the flow. At minimum, report separately:
- N roster (all UE to which the package applies);
- N identity/binding/integrity evaluable;
- N truth 1, N truth 0 and N truth ?;
- N evidence coverage NONE/PARTIAL/COMPLETE by relevant claim dimension;
- E1 and E2 outputs available, 1/0/?/abstention/technical failure, separately;
- N binary-evaluable truth cases (1/0), with class-specific denominators;
- N blocked/non-evaluable, with reasons.

Identity, binding or truth-integrity failures are not recoded as truth=?, are not silently removed, and block declaration of completed census evaluation until resolved. Evidence absence or partial coverage does not remove a unit; it is an adjudication condition, normally yielding observed=? under the existing protocol when evidence is insufficient.

## 4. Binary support gate

The defined census must contain valid truth=1 and truth=0 cases to evaluate binary classification. If either class is absent, report SUPPORT_FAILURE / CONFIRMATORY_CLASSIFICATION_BLOCKED. No post-hoc cohort change, case addition, relabeling, rebalancing or prevalence assumption is permitted.

This support condition does not imply:
- balance or a target prevalence;
- support in every Z arm, stratum, P* population or ITT denominator;
- sufficient sample size, precision or power;
- positivity/identification for causal estimands;
- population representativeness or transportability.

Truth=? remains a separate semantic status and is reported separately, not imputed to 0/1.

## 5. Reused contracts and no expansion

This decision specializes:
- `C10_S_B1_PREZ_COHORT_SCOPE_AND_EVALUATION_DENOMINATORS_RECONCILIATION_DRAFT_001.md`;
- `C10_S_B1_PREZ_VALIDATION_COHORT_POPULATION_CROSSWALK_DRAFT_001.md`;
- `C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md`;
- `C10_S_B1_PREZ_OBSERVATION_MODEL_TO_PE_BUNDLE_RECONCILIATION_DRAFT_001.md`;
- `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`.

No seventh package artifact, new U_G target, Evidence→Claim claim, causal population or estimand is created. P*_{τ2}, P*_F, ITT, D2 and the Analyzer PE contract are unchanged.

## 6. Open gates

- approval and versioning of the actual DGP/package roster, including separate-vs-joint A/B scope;
- material identity and binding integrity;
- support 1/0 in the approved census;
- statistical adequacy, precision and power for E1/E2;
- complete observation-source/dependency specification and test crosswalk;
- technical implementation of the truth/evidence/adjudication firewall;
- any transportability claim beyond the validation census.

No roster, truth, evidence, adjudication, fixture, physical schema, code or execution is authorized by this decision.

## 7. Status and authorization

Accepted working design decision on the research branch; not Design Freeze, implementation approval or scientific execution authorization.

`scientific_execution=false`; `execution_authorized=false`.

## 8. Traceability

- User acceptance: 2026-11-12, response “Sí” to census of the complete applicable DGP/package B1 roster, with E1/E2 as Need adjudicators and Analyzer PE separate.
- Cohort/denominator reconciliation: `C10_S_B1_PREZ_COHORT_SCOPE_AND_EVALUATION_DENOMINATORS_RECONCILIATION_DRAFT_001.md`.
- Population crosswalk: `C10_S_B1_PREZ_VALIDATION_COHORT_POPULATION_CROSSWALK_DRAFT_001.md`.
- Observation and PE bundle boundary: `C10_S_B1_PREZ_OBSERVATION_MODEL_TO_PE_BUNDLE_RECONCILIATION_DRAFT_001.md`.
