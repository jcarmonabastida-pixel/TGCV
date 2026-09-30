# TI-001 V012 NEXT4 — Data-Generating Process Specification 001

**Status:** DESIGN FREEZE CANDIDATE — NO EXECUTION AUTHORIZED  
**Date:** 2026-09-30  
**Purpose:** Freeze the synthetic data-generating process before power simulation.

## 1. Principle
The DGP is a calibration device for design sensitivity. It is not an empirical claim about the magnitude of the NEXT4 effect. No coefficient is imported from NEXT3 Q5.

## 2. Experimental unit
One experimental unit is one choice set containing one profile, one future structure, four candidate actions, and one observed categorical choice. The analysis representation expands each choice set into four action rows with a single chosen=1.

## 3. Factorial architecture
The simulator must preserve 24 complete profile→future permutations, 4 conditions, 3 domains, 2 operationalisations, 4 presentation strata, balanced allocation, and the candidate total N values specified by the power specification. For every candidate N, the same factorial proportions must be preserved.

## 4. Conditions
**STATIC_CONTROL:** identity profile→future mapping.
**FUTURE_REASSIGNED:** non-identity permutation from the complete 24-permutation family.
**SURFACE_CONTROL:** latent semantic mapping remains identity; only presentation is permuted by the frozen presentation-control operator.
**UNINFORMATIVE_NULL:** no informative profile→future correspondence; latent mapping signal is zero by construction. This is not implemented by silently substituting the identity mapping.

## 5. Mapping-alignment mechanism
For FUTURE_REASSIGNED, the DGP contains a pre-declared action preference increment for the action aligned with the imposed future structure. For STATIC_CONTROL the same mechanism operates relative to identity. SURFACE_CONTROL retains identity latent mapping. UNINFORMATIVE_NULL has mapping-alignment coefficient exactly zero.

## 6. Effect-size grid
- NULL = 0.00
- VERY_SMALL = 0.10
- SMALL = 0.25
- MODERATE = 0.50
- OPTIMISTIC = 0.80

These are simulation labels, not estimated NEXT4 effects.

## 7. Baseline coefficients
- action baseline: 0.05 × action_id
- profile interaction baseline: 0.04 × ((action_id + profile_id) mod 4)
- domain nuisance: 0.03 × domain_id
- operationalisation nuisance: 0.02 × operationalisation_id
- presentation nuisance: 0.00 in the primary DGP

## 8. Choice probabilities
For each choice set and action, latent logit is action baseline + profile-action baseline + domain nuisance + operationalisation nuisance + mapping-alignment effect, where mapping-alignment effect is beta × I(action = mapped_future_structure) for STATIC_CONTROL and FUTURE_REASSIGNED, and zero for UNINFORMATIVE_NULL and SURFACE_CONTROL. Choice probabilities are the four-action softmax.

## 9. Presentation control
Presentation remains in the dataset and analysis matrix, but its direct response coefficient is zero in the primary DGP.

## 10. Domain heterogeneity
Primary DGP uses common mapping-alignment beta across domains. A separate exploratory heterogeneity scenario may vary beta by domain, but cannot determine the primary sample-size decision unless separately frozen.

## 11. Randomness
Only the deterministic seed schedule may generate response randomness. No wall-clock seed, provider randomness or hidden state is permitted.

## 12. Required DGP audit
Verify exact factorial counts, balanced allocation, condition semantics, effect grid, baseline coefficients, NULL=0, identity STATIC_CONTROL mapping, non-identity FUTURE_REASSIGNED mapping, identity latent mapping plus surface-only SURFACE_CONTROL manipulation, zero mapping signal in UNINFORMATIVE_NULL, and deterministic replay.

## 13. Scientific boundary
The DGP is not evidence about the real system. It only evaluates sensitivity of the planned analysis under specified hypothetical effects. Simulation results are not NEXT4 scientific findings.

## 14. Next action
Implement this DGP as a versioned configuration and update the engine to consume it. Then audit factorial allocation and DGP before implementing the final numerical contrast and Monte Carlo loop.