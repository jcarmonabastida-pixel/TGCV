# TI-001 V012 NEXT4 — Primary Estimand / Identifiable Model 010 Specification 001

**Status:** DESIGN REVIEW — NOT EXECUTION AUTHORIZED  
**Date:** 2026-09-30  
**Parent:** TI001_V012_NEXT4_TWO_SURFACE_MODEL_009_IDENTIFIABILITY_AUDIT_001

## 1. Purpose
Resolve the model-009 identifiability block without changing the scientific question, frozen DGP, candidate-N grid, seed schedule, or scientific construct.

## 2. Scientific question retained
Does the independently imposed profile→future-structure mapping reorganise the action×profile correspondence in FUTURE_REASSIGNED relative to STATIC_CONTROL, specifically in the direction prescribed by the frozen permutation?

No value, reward, utility, performance, rationale, or external outcome enters the estimand.

## 3. Identification problem
For each surface s and profile p, categorical choice probabilities are unchanged by

    eta[s,p,a] -> eta[s,p,a] + kappa[s,p]

for every action a. Therefore absolute action×profile surface levels are not identified.

## 4. Corrected primitive estimand
Let eta_F(p,a) and eta_S(p,a) denote the action logits for profile p under FUTURE_REASSIGNED and STATIC_CONTROL, respectively.

For permutation pi and profile p, define:

    d(pi,p) = [eta_F(p,pi(p)) - eta_F(p,p)] - [eta_S(p,pi(p)) - eta_S(p,p)]

The primary estimand is:

    theta = (1 / (24*4)) * sum_pi sum_p d(pi,p)

where the sum is over the 24 frozen permutations and the four profiles. If pi(p) = p, that term is identically zero.

## 5. Identification proof requirement
Under eta_s(p,a) -> eta_s(p,a) + kappa[s,p], each bracket is unchanged because its two action coefficients sum to zero within the same surface/profile block. Therefore theta is invariant and is a legitimate estimand of the observed categorical choice distribution.

## 6. Equivalent identifiable parameterisation
The implementation may use either:

1. within-profile reference logits: three action-logit differences per surface/profile relative to one fixed action reference; or
2. within-profile sum-to-zero logits: impose sum_a eta[s,p,a] = 0 for every surface/profile block.

The primary contrast must be algebraically identical under either parameterisation. Reference-action choice must not alter theta.

## 7. Required contrast coding
For every surface/profile block, the primary contrast must use coefficients that sum to zero across actions. Equivalently, for each permutation/profile contribution:

- +1 on eta_F(p,pi(p));
- -1 on eta_F(p,p);
- -1 on eta_S(p,pi(p));
- +1 on eta_S(p,p);
- all multiplied by 1/(24*4).

No absolute surface-cell coefficient may appear in the primary contrast.

## 8. Nuisance/design factors
Domain, operationalisation and presentation remain nuisance/design factors exactly as previously specified. Control conditions remain part of the experimental design and are not used merely to repair identifiability.

No empirical result, NEXT3 estimate, value signal, or reward/performance measure is imported.

## 9. Required audit before simulation
A new implementation-equivalence/identifiability audit must demonstrate, for every frozen candidate N:

1. expected parameterisation;
2. numerical rank;
3. likelihood null-space dimension;
4. primary-contrast estimability;
5. invariance under generated kappa[s,p] transformations;
6. reference-action invariance if reference logits are used;
7. algebraic equivalence of reference-logit and sum-to-zero formulations;
8. exact primary-contrast construction over the 24 frozen permutations and four profiles;
9. no change to the frozen DGP or seed schedule.

The audit must precede Monte Carlo execution.

## 10. Engine boundary
TI001_V012_NEXT4_POWER_SIMULATION_ENGINE_002.py is not to be modified at this stage.

The frozen execution specification remains an historical frozen artifact. A new execution-specification version is required only after the corrected model passes independent implementation-equivalence and identifiability gates.

## 11. Decision gate
- Model-009 primary estimand: BLOCKED.
- Corrected Model-010 estimand: DESIGN PROPOSED.
- Monte Carlo: NOT AUTHORIZED.
- Scientific execution: NOT AUTHORIZED.
- DGP: UNCHANGED / FROZEN.
- Seed schedule: UNCHANGED / FROZEN.

## 12. Next technical action
Implement the corrected estimand as a standalone model-010 implementation, without changing Engine 002, and run its identifiability/reference-invariance audit.

Only a PASS on that audit permits drafting the next execution-specification revision.