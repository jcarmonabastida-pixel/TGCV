# DEC-C10-097 — B1/Need_preZ observation and coverage model acceptance

**Date:** 2026-11-12  
**Status:** ACCEPTED WORKING DESIGN DECISION — NOT DESIGN FREEZE  
**Scope:** Pre-Z observable evidence generation, source admissibility, adjudication input and coverage accounting for B1/Need_preZ  
**Branch:** research/c10-s-consolidation-draft · PR #116 (Draft)

## 1. Decision

The user explicitly accepted the operational observation and coverage rules in `C10_S_B1_PREZ_OBSERVATION_MECHANISM_AND_COVERAGE_RULES_RECONCILIATION_DRAFT_001.md` on 2026-11-12.

Accept those rules as the working design for the B1/Need_preZ package, subject to the existing higher-precedence B1 contracts and DEC-C10-095/096. The accepted model keeps distinct:

1. the ex-ante source/opportunity frame and its enumeration rule;
2. source declaration/emission;
3. capture/retention/loss;
4. semantic content and its relation to the focal objective;
5. authority, scope and validity;
6. identity, version, temporal and integrity checks;
7. adjudicator examination and admissibility;
8. coverage by UE × claim dimension;
9. E1 and E2 independent adjudication;
10. post-seal comparison against reserved DGP truth.

These are distinct logical mechanisms and states. No conditional independence is assumed and no rates, probabilities, prevalence, source counts, parameter values or dependence structure are fixed by this decision.

## 2. Binding semantic rules

- Absence, non-emission, loss, failed search, missing field or no request is not an affirmative exclusion and never establishes observed=0.
- observed=1 requires admissible, authoritative, semantically aligned, correctly bound, pre-Z affirmative evidence of the focal B1 objective.
- observed=0 requires an affirmative focal exclusion, valid for the B1/UE/service scope and version, with sufficient authority, temporal integrity and coverage to adjudicate it. In accordance with DEC-C10-095, the focal exclusion is the minimum sufficient truth=0 stipulation; exhaustive enumeration of every possible B1 objective is not required. The relevant B1–service scope must nevertheless be closed and identifiable.
- observed=? is retained for absence/insufficiency, ambiguity, unresolved conflict, opaque or incomplete coverage, and non-admissible evidence that does not constitute a technical identity/integrity block.
- Identity, binding, schema, digest or truth-integrity defects that prevent valid evaluation remain explicit package/unit blocks; they are not silently recoded as observed=? or removed from the census.
- Coverage COMPLETE requires an ex-ante enumerable and closed expected-source universe for the relevant UE × dimension and examination of all in-scope surfaces under the versioned rule. COMPLETE alone does not imply observed=0.
- Event time must be pre-Z. Later capture is admissible only when an immutable, integrity-verifiable pre-Z record is demonstrated.
- The observation generator may create truth-dependent authentic content/availability only through the declared observation mechanism; it must not expose the truth label, truth basis reference or reserved metadata to E1/E2. Observation and adjudication mechanisms must not depend on Z, D2, post-Z accessibility, Reach, trajectory, execution, Outcome, Value or adjudicator outputs.
- No source independence, MCAR, MAR, MNAR, sensitivity, specificity, missingness rate or error rate is presumed. Such mechanisms remain to be specified and justified in the DGP and sensitivity design.

## 3. Cohort and task boundary inherited

DEC-C10-096 remains binding: the Need validation cohort is the census of all UE in the approved, versioned DGP/package roster to which B1/Need applies. E1 and E2 are the only Need adjudicators in this validation task. Analyzer PE remains outside the Need classification task and its denominators.

The cohort rule does not create a causal population, alter P*_{τ2}, P*_F, ITT, D2 or any estimand. Truth=1/0 support is a classification validation gate only; it does not imply arm-specific support, balance, power, positivity or causal identification.

## 4. Reuse of existing test contracts — no new IDs

The accepted rules specialize existing contracts; they do not create a new test family or duplicate IDs.

| Accepted requirement | Existing contract(s) to reuse |
|---|---|
| Truth/evidence separation, no truth leakage, pre-Z temporal integrity | PKG-02, PKG-05, PKG-06, PKG-07; P182-11/12 |
| Omission/non-emission/loss is not observed=0 | PKG-08; P183-01/03/04 |
| Affirmative focal exclusion and sufficient closed-scope coverage for observed=0 | PKG-09; P182-01/03/05; P183-13 |
| Technical service/configuration evidence does not prove B1 objective | PKG-10; P182-01/02 |
| Ambiguity, conflict, identity, version, temporal and integrity failures | PKG-11, PKG-14; P182-05/12; P183-09/13 |
| E1/E2 independence, preserved disagreement, seal-before-evaluation | PKG-12, PKG-13; P182-06/11/12 |
| Source emission/capture loss, differential observation and missingness | P183-01/02/07/09/10/11; MEAS-13; MISS-05/10/13/15, where applicable |
| Coverage and support reporting without overclaiming transportability/identification | PKG-04, PKG-09; P182-03/05/07; P183-07/12/13 |

This crosswalk does not assert that any test is implemented or executed. Existing test wording may require a versioned clarification if it cannot express the accepted B1-specific rule; do not silently alter a test contract or reuse an ID for a materially different assertion.

## 5. Package and artifact boundary

Reuse the six logical artifacts already specified in the analytical package:
`PACKAGE_MANIFEST`, `UNIT_BINDING`, `TRUTH_LEDGER`, `EVIDENCE_LEDGER`, `ADJUDICATION_LEDGER`, `EVALUATION_LEDGER`.

Source scope and coverage remain represented within the manifest/evidence scope records as already proposed. Do not create a seventh logical artifact, a new U_G target, a new Evidence→Claim claim, a new causal population or an Analyzer Need output.

## 6. Remaining open gates

- define the minimum source classes actually needed for the B1 microdomain; inventory candidates are not automatically present sources;
- define the ex-ante expected-source universe and enumeration/closure rule per UE × dimension;
- specify the observation dependency graph and support without inventing independence or rates;
- reconcile each accepted rule to the detailed PKG/P182/P183/MEAS/MISS contracts and test wording;
- justify statistical adequacy, precision, power and sensitivity analysis;
- approve the material roster and identity/binding;
- technically verify the truth/evidence/adjudication firewall and side-channel controls;
- approve implementation and scientific execution separately.

No roster, truth, evidence, adjudication, source record, fixture, physical schema, code or execution is authorized by this decision.

## 7. Status and authorization

Accepted working design decision on the research branch; not Design Freeze, implementation approval or scientific execution authorization.

`scientific_execution=false`; `execution_authorized=false`.

## 8. Traceability

- User acceptance: 2026-11-12, response “Sí” to the operational observation/coverage rules.
- Observation/coverage reconciliation: `C10_S_B1_PREZ_OBSERVATION_MECHANISM_AND_COVERAGE_RULES_RECONCILIATION_DRAFT_001.md`.
- Analytical package: `C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md`.
- Source inventory/audit: `C10_S_B1_PREZ_EVIDENCE_SOURCE_INVENTORY_AND_COVERAGE_AUDIT_DRAFT_001.md`.
- Adjudication contract: `C10_S_B1_PREZ_ADJUDICATION_AND_CONSEQUENCE_RECONCILIATION_DRAFT_001.md`.
- Cohort acceptance: DEC-C10-096.
- Truth composition/exclusion acceptance: DEC-C10-095 and the B1/Need exclusion decision record.



## 9. Specialization by DEC-C10-098 — expected S7 opportunity frame

DEC-C10-098 subsequently closes the second open gate in §6 for the focal B1/Need_preZ semantic declaration: the expected-source universe contains one logical S7 opportunity per UE in the approved B1/Need validation census. The opportunity is enumerated and sealed ex ante; its existence is not conditional on truth, Z/D2, evidence discovery, emission, capture or adjudication.

This specialization does not close the observation dependency graph, emission/content/capture parameters, scenario support, statistical adequacy, physical source format or implementation gates. It does not alter any rule in §§1–8. All source-opportunity, evidence, coverage and adjudication semantics remain subject to DEC-C10-097.
