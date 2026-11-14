# DEC-C10-095 — B1 Need_preZ explicit stipulation and truth composition

**Date:** 2026-11-12  
**Status:** ACCEPTED WORKING DESIGN DECISION — NOT DESIGN FREEZE  
**Scope:** C10-S B1/UE baseline Need_preZ truth generation and validation-cohort support  
**Branch:** research/c10-s-consolidation-draft · PR #116 (Draft)

## 1. Decision and basis

Following the user's explicit acceptance of the comparison in `C10_S_B1_PREZ_STIPULATION_MECHANISM_COMPARISON_DRAFT_001.md`, adopt **explicit, versioned, reserved per-unit baseline stipulation** as the source of `Need_preZ` truth for each B1/UE.

A deterministic, transparent rule maps the stipulation to `need_truth_state`. No stochastic assignment/generation of Need is used in the current confirmatory nucleus.

This decision accepts a design mechanism. It does not approve a roster, a population prevalence, a sample size, a statistical distribution, a physical schema, implementation, execution or Design Freeze.

## 2. Normative rules

1. **Unit and time:** one stipulation per valid B1/UE/baseline/package version, referring to the versioned logical service binding and fixed at baseline t−1 before Z at t0.
2. **Explicit source:** the reserved stipulation is the sole semantic input to the derivation of Need truth. It is not a covariate, observed source, adjudication or causal mediator.
3. **Deterministic mapping:**
   - explicit focal inclusion → `need_truth_state=1`;
   - explicit focal exclusion within the already defined closed B1–service scope → `need_truth_state=0`;
   - genuine explicit semantic indeterminacy → `need_truth_state=?`.
4. **Integrity distinction:** missing/null/omitted stipulation, invalid binding, failed write, corrupt record or digest/version mismatch are integrity/materialization errors, not truth=? and never truth=0. Block the affected unit/package pending resolution.
5. **No stochastic Need generator:** no Bernoulli/categorical draw, probability, prevalence parameter or random seed assigns Need in the confirmatory design. This does not prohibit a separately specified stochastic observation/error model or the randomized assignment mechanism for Z.
6. **No proxy or post-treatment derivation:** do not derive or revise the stipulation from X/H/C/L, C_dep, A_f, T_acc, Reach, CMP/PAR/REF/RUL, ENABLED/PROFILE, installation, accessibility, requests, Z/D2, compliance, outcomes or Value.
7. **Truth/evidence firewall:** the stipulation and reconstructive metadata remain reserved. Observed evidence is generated separately; E1/E2 and Analyzer do not receive truth or its basis. Evaluators access truth only after the relevant output has been sealed.
8. **Roster/cohort order:** define the roster and validation cohort by identity, binding and population rules ex ante, without selecting membership based on Need, observability, adjudication or outcomes. The approved cohort is assessed as a whole. If a distinct subcohort is proposed, its selection rule must be justified independently of Need and approved before truth/evidence inspection.
9. **Binary support gate:** the pre-defined validation cohort must contain valid truth=1 and truth=0 cases for binary classification evaluation. If either class is absent, report `SUPPORT_FAILURE / DESIGN_BLOCKED`. Do not repair by post-hoc additions, relabeling, reweighting or cohort changes.
10. **No artificial prevalence claim:** no balance, proportion, prevalence, per-arm/per-stratum support or population representativeness is implied. The composition is a design-coverage property, not an estimate of natural prevalence. No class ratio is set by this decision.
11. **Truth=? handling:** preserve genuine semantic indeterminacy as a distinct status. It is not imputed into the binary classes and is reported separately. Whether it enters a separate confirmatory ternary estimand remains OPEN.
12. **No causal-scope expansion:** Need is not an ITT eligibility criterion, treatment assignment variable or substitute for P* populations/denominators. No causal identification or positivity claim follows from binary validation support.

## 3. Reused contracts and propagation

This decision specializes, without replacing:
- `C10_S_B1_PREZ_OBJECTIVE_SPECIFICATION_CONTRACT_DRAFT_001.md`;
- `C10_S_B1_PREZ_EXCLUSION_SCOPE_CONTRACT_DRAFT_001.md`;
- `C10_S_B1_PREZ_TRUTH_COMPOSITION_AND_SUPPORT_REVIEW_DRAFT_001.md`;
- `C10_S_B1_PREZ_VALIDATION_COHORT_POPULATION_CROSSWALK_DRAFT_001.md`;
- `C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md`;
- `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`.

The six existing package artifacts remain unchanged in number. The stipulation is the reserved basis referenced by the existing `TRUTH_LEDGER`; no seventh artifact, U_G target, Evidence→Claim claim or new causal construct is introduced.

## 4. Gates that remain OPEN

- final roster, B1/UE bindings, population and validation cohort;
- justification of the B1 scenario/domain coverage represented by the roster;
- sample size, precision, power and any class-conditional stability requirements;
- confirmatory treatment of truth=? beyond separate reporting;
- any justified statistical dependence of Need on baseline covariates (not implied here);
- observation-source mechanisms, error/capture/coverage dependencies and parameters;
- physical representation, storage, permissions, sealing and technical firewall;
- static test mapping and implementation contract.

No data, stipulations, truth records, sources, fixtures, parameters, seeds or executable artifacts are materialized by this decision.

## 5. Status and authorization

This is an accepted working design decision on the research branch. It is **not** a Design Freeze, implementation approval or scientific execution authorization. It does not alter `main`, RMA, Evidence→Claim Matrix, STATUS, P* populations, ITT estimands or D2.

`scientific_execution=false`; `execution_authorized=false`.

## 6. Traceability

- User acceptance: 2026-11-12, response “Sí” to the explicit-stipulation / deterministic-mapping / no-stochastic-Need recommendation.
- Comparison: `C10_S_B1_PREZ_STIPULATION_MECHANISM_COMPARISON_DRAFT_001.md`.
- Objective semantics: `C10_S_B1_PREZ_OBJECTIVE_SPECIFICATION_CONTRACT_DRAFT_001.md`.
- Exclusion scope: `C10_S_B1_PREZ_EXCLUSION_SCOPE_CONTRACT_DRAFT_001.md`.
- Validation cohort: `C10_S_B1_PREZ_VALIDATION_COHORT_POPULATION_CROSSWALK_DRAFT_001.md`.
