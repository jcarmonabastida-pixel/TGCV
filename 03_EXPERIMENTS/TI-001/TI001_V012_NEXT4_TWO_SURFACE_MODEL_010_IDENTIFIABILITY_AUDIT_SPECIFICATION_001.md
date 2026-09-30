# TI-001 V012 NEXT4 — Model 010 Identifiability Audit Specification 001

**Status:** DESIGN REVIEW — NOT EXECUTION AUTHORIZED
**Implementation:** `TI001_V012_NEXT4_TWO_SURFACE_MODEL_010.py`

## Gate
Audit only. No Monte Carlo and no scientific execution.

## Required properties
1. The reference-logit parameterisation estimates three within-profile action differences per surface/profile.
2. The primary contrast is a difference-in-differences of those within-profile differences.
3. Its coefficient sum is zero across actions separately within every surface/profile block in the underlying absolute-logit representation.
4. The contrast is estimable for every frozen candidate N.
5. Changing the reference action leaves the primary estimand unchanged.
6. Applying arbitrary additive kappa[s,p] shifts to absolute logits leaves the primary estimand unchanged.

## Scientific invariants
DGP, fixture, permutation group, candidate-N grid, seed schedule and scientific question are unchanged.

## Execution boundary
This audit must pass before any execution-specification revision or Monte Carlo launch. Engine 002 remains untouched.