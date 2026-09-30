# TI-001 V012 NEXT4 — Fixture Architecture and Analysis Specification 001

**Status:** DESIGN REVIEW — NOT EXECUTION AUTHORIZED  
**Date:** 2026-09-30  
**Purpose:** Close the quantitative architecture of NEXT4 sufficiently for implementation-equivalence review and fixture construction.

## 1. Experimental unit

One decision unit contains one domain, one operationalisation, four structural profiles, four candidate actions, four future structures, one profile→future mapping condition, one presentation configuration, and one model decision.

## 2. Primary conditions

1. STATIC_CONTROL
2. FUTURE_REASSIGNED
3. SURFACE_CONTROL
4. UNINFORMATIVE_NULL

STATIC_CONTROL and FUTURE_REASSIGNED are the principal semantic comparison. SURFACE_CONTROL and NULL are controls.

## 3. Permutation architecture

The complete 24-element permutation group of four future structures is used. One identity mapping is designated STATIC_CONTROL; the 23 non-identity permutations constitute FUTURE_REASSIGNED mappings. Permutation identity is balanced independently of presentation.

## 4. Replication architecture

The provisional minimum is 3 independent replicate units per permutation × domain × operationalisation × primary condition cell.

Planning grid: 24 permutations × 3 replicates × 4 conditions × 3 domains × 2 operationalisations = **1,728 decision units**.

This is a design planning value, not a power claim. A deterministic power/sensitivity analysis must be completed before fixture freeze. It may increase the unit count but may not decrease it because of an observed pilot result.

## 5. Domain architecture

Three domains are retained. Every permutation × condition × operationalisation cell occurs in every domain. Domain is included in the model and reported descriptively by domain. This controls the strong domain dependence observed in NEXT3; it does not establish transversal validity.

## 6. Operationalisation architecture

Two operationalisations are retained and crossed with domain, condition and permutation. Both use the same semantic future-structure inventory and permutation algebra.

## 7. Presentation architecture

Four presentation strata are retained: order, position, orientation and neutral format. Presentation is independently permuted and balanced against future-structure mapping.

## 8. Primary estimand

The primary estimand is the mapping-following reorganisation of action×profile association, not a generic condition effect.

Conceptually: action_identity × profile_id × future_mapping.

The critical contrast must test whether the action×profile association changes between matched stable and reassigned mappings in the direction specified by the known future permutation.

## 9. Candidate model

Candidate form: chosen ~ action_identity + profile_id + future_mapping + action_identity:profile_id + action_identity:profile_id:future_mapping + domain + operationalisation + presentation.

The exact coding and primary contrast must be frozen after rank diagnostics. If the full permutation factor is categorical, the primary contrast must be a pre-declared contrast over the mapping relation, not an omnibus permutation test alone.

## 10. Controls

SURFACE_CONTROL asks whether presentation manipulation alone can reproduce the reorganisation. NULL asks whether an informative profile→future correspondence is necessary for the mapping-sensitive effect.

## 11. Multiplicity

Default: Holm adjustment. The primary family should contain one primary discriminating contrast. Surface/null diagnostics should form a separate control family unless promoted before freeze. Exploratory domain and operationalisation analyses remain outside the primary family unless explicitly frozen otherwise.

## 12. Invalid-record policy

Invalidity is determined only from immutable design fields and fixture-binding integrity. It cannot depend on the observed action or statistical result. The result must report total, valid, invalid and invalidity categories.

## 13. Rank and singularity

Before execution, construct the exact primary design matrix, calculate rank, verify degrees of freedom, test structural aliasing and verify primary-contrast estimability. Failure blocks execution. No post-result term deletion is permitted.

## 14. Optimisation and covariance

The primary model must freeze fitting algorithm, covariance estimator, convergence criterion, maximum iterations, singularity criterion and Hessian/covariance checks.

Because NEXT3 Q5 used BFGS inverse-Hessian covariance and lacked a historical callback trace, NEXT4 must preserve optimisation diagnostics and callback/convergence trace in the result artifact. Missing trace is a binding-quality failure.

## 15. Execution budget

A real cost probe is mandatory before full execution. It must record model, reasoning setting, maximum output tokens, input/output/total tokens, estimated cost and latency. Output capacity must be set above expected response length so reasoning cannot consume the usable response budget.

## 16. Response contract

The decision interface returns only one bounded categorical response identifying one of four candidate actions. No free-form rationale is collected as a scientific variable.

## 17. Fixture contents

At minimum: experiment/version identifier, decision_unit_id, counterfactual_family_id, domain, operationalisation, condition, permutation_id, profile set, action set, future_structure set, profile→future mapping, presentation stratum, presentation permutation, replicate_id and immutable record hash.

Every stable/reassigned/null/surface-control relationship must be reconstructible from the fixture.

## 18. Sharding

The 1,728-unit planning size is suitable for an initial deterministic fixture audit. If sensitivity analysis requires scaling, the complete factorial architecture must be preserved. Shard boundaries must not make shard identity predictive of condition.

## 19. Pre-execution gates

1. semantic gate;
2. generator determinism;
3. graph schema;
4. null construction;
5. counterfactual mapping;
6. leakage L1–L8;
7. fixture balance;
8. power/sensitivity review;
9. rank/estimability;
10. implementation-equivalence;
11. provider/runtime compatibility;
12. cost probe;
13. fixture freeze;
14. explicit scientific authorization.

## 20. Interpretation boundary

Even a positive result would establish only that, under the frozen NEXT4 operationalisation, action×profile reorganisation tracks an independently imposed future-structure mapping.

It would not by itself establish Transformational Intelligence, a unique cognitive mechanism, future_structure = T_acc, causal value generation, transversal validity or generalisation outside the frozen population.

## 21. Next artifacts

Before fixture generation: deterministic generator implementation specification; exact null construction specification; power/sensitivity analysis; statistical analysis specification with frozen coding and contrast; implementation-equivalence gate.

**No scientific execution is authorized by this document.**