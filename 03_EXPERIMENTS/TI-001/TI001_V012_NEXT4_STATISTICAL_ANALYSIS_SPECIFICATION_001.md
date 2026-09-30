# TI-001 V012 NEXT4 — Statistical Analysis Specification 001

**Status:** DESIGN REVIEW — NOT EXECUTION AUTHORIZED  
**Date:** 2026-09-30  
**Parent:** NEXT4 Fixture Architecture and Analysis Specification 001

## 1. Primary scientific question

Does an independently imposed profile→future-structure mapping reorganise the action×profile correspondence in a way that follows the known permutation, beyond generic condition differences and presentation effects?

## 2. Response

The response is a categorical choice among four candidate actions. No value, reward, utility, performance or free-form rationale is part of the response variable.

## 3. Primary model

The primary analysis uses a multinomial choice formulation equivalent to action-specific logits with a fixed reference action. Conceptual formula:

`chosen ~ action_identity + profile_id + mapping_signal + action_identity:profile_id + action_identity:profile_id:mapping_signal + domain + operationalisation + presentation`

The implementation must encode mapping_signal from the frozen profile→future permutation without using the observed choice.

## 4. Mapping signal

For each candidate action/profile pair, define a deterministic indicator derived only from the frozen future mapping and immutable action/profile labels. It must be deterministic, response-independent, reconstructible from the fixture, and identical in simulation and scientific analysis.

## 5. Primary contrast

The primary contrast is the difference in mapping-aligned action×profile association between STATIC_CONTROL and FUTURE_REASSIGNED, evaluated in the direction predicted by the imposed permutation.

The contrast is constructed directly from the immutable permutation table. A generic STATIC_CONTROL vs FUTURE_REASSIGNED coefficient is not the primary estimand.

One scalar primary contrast is tested at two-sided alpha 0.05.

## 6. Hypotheses

H0: the action×profile association does not reorganise in the direction specified by the independently imposed future mapping.

H1: the action×profile association shows the pre-specified mapping-aligned reorganisation.

## 7. Controls

SURFACE_CONTROL tests whether the mapping-alignment contrast appears when semantic mapping is held constant and only presentation is permuted. UNINFORMATIVE_NULL tests whether the mapping-alignment contrast is absent under an uninformative profile→future mapping.

These are control analyses, not substitutes for the primary test.

## 8. Domain, operationalisation and presentation

Domain and operationalisation are nuisance/design factors. Domain-specific estimates are descriptive secondary outputs because NEXT3 showed strong domain dependence. Presentation stratum is included as a nuisance/design factor across order, position, orientation and neutral strata.

## 9. Multiplicity

Primary family: exactly one primary mapping-alignment contrast.

Secondary control family: surface-control and null-control contrasts, with Holm correction within that family. Domain and operationalisation moderation remain exploratory unless separately frozen before execution.

## 10. Estimability and rank

Before execution, the exact fixture must generate the primary design matrix and verify expected rank, actual rank, primary contrast estimability, absence of structural aliasing and sufficient observations in every declared cell. Failure blocks execution.

## 11. Optimisation and covariance

The exact fitting algorithm, covariance estimator, convergence tolerance, iteration limit and singularity criteria must be frozen in the implementation-equivalence specification. The result must retain convergence status, optimisation method, covariance method, Hessian/information diagnostics, callback/convergence trace, rank, coefficients and covariance matrix.

The NEXT3 Q5 limitation concerning absent historical callback trace is explicitly closed by this requirement.

## 12. Simulation identity

The power simulator must use the same model formula, coding, primary contrast and covariance/convergence rules as the scientific analysis. No simulator-specific simplification of the primary estimand is permitted.

## 13. Invalid records

Invalidity is determined only by immutable fixture integrity and response-schema validity. Observed choice may not determine exclusion. The analysis must report total, valid, invalid, invalidity categories and analysis population.

## 14. Reporting

The primary result must report contrast estimate, standard error, confidence interval, test statistic, degrees of freedom where applicable, raw p-value, adjusted p-value where applicable, model rank, covariance method and convergence status. No composite score is produced.

## 15. Scientific boundary

A positive result would show that observed action×profile reorganisation follows the imposed future-structure mapping under the frozen experimental construct. It would not by itself establish Transformational Intelligence, a unique cognitive mechanism, equivalence of future_structure to T_acc, causal value generation, or generalisation outside the frozen design.

## 16. Freeze rule

This specification must be hash-bound to the power/sensitivity specification, fixture architecture, future-structure generator/control specification and implementation source. Any change to model, coding, contrast or multiplicity after simulation results are inspected requires a new specification version and a new sensitivity analysis.

## 17. Next action

Implement the exact mapping signal and primary contrast from this specification, then run the statistical implementation-equivalence audit.

**No Monte Carlo execution and no scientific execution are authorized until that audit passes.**
