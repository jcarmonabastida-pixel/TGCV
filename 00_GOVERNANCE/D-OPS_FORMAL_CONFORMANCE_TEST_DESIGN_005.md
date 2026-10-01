# TGCV — Transformational Dynamics Formal Conformance Test Design 005

**Status:** DESIGN DRAFT — NOT EXECUTED
**Date:** 2026-10-01
**Supersedes for development:** Design 004
**Purpose:** resolve the R3 contradiction identified in Freeze Package 001 Technical Consistency Audit 001.

## 1. Resolution

Design 005 adopts the independent-R3 model.

R3 is no longer derived from R1/R2 effects. It is an independently specified structural relation within the formal object:

Ω_T = (U, ≡, R1, R2, R3)

R1 and R2 retain their previous deterministic definitions. R3 has its own frozen relation manifest and comparison rules.

## 2. R3 definition

R3 is a directed structural relation over transformation identities.

A tuple (τ_i, τ_j) belongs to R3 iff it is explicitly present in the frozen R3 relation manifest for that fixture.

R3 construction therefore does not inspect action preconditions, action add effects, action delete effects, initial state, goals, execution traces, or outcomes.

The relation remains structural and ex ante.

## 3. Reconfiguration

A reconfiguration fixture preserves U exactly, ≡ exactly, R1 exactly, and R2 exactly, and changes exactly one R3 edge: one R3 edge is deleted and one different R3 edge is added.

The independent oracle verifies the complete canonical diff.

Expected descriptor: RECONFIGURATION_ONLY.

The previous impossible requirement that R3 be derived from unchanged R1/R2 is removed.

## 4. R3 manifest

The frozen fixture must contain an explicit canonical R3 edge list.

Canonical edge representation: [source_transformation_id, target_transformation_id]

Edges are directed, unweighted, unique, sorted canonically, and represented only between identities present in U.

A malformed edge referencing an identity outside U is a preflight failure.

## 5. Identity and relation comparison

The oracle computes independently ΔU, Δ≡, ΔR1, ΔR2, and ΔR3.

Descriptors:
- PERSISTENCE: all five diffs empty;
- EXPANSION: U gains at least one identity;
- CONTRACTION: U loses at least one identity;
- RECONFIGURATION_ONLY: ΔU=Δ≡=ΔR1=ΔR2=empty and ΔR3 consists of exactly one deletion plus one addition;
- OTHER_STRUCTURAL_CHANGE: any remaining non-empty structural diff;
- NON_COMPARABLE: canonical correspondence cannot be established.

## 6. Information firewall

R3 may not be reconstructed from outcomes, execution, planner behavior, reward, utility, or trajectory.

The R3 manifest is an ex ante structural input.

## 7. State-reducibility

The finite C_S and G_S definitions from Design 004 remain unchanged.

State-reducibility continues to test whether the structural-change decision can be reproduced from a frozen state-only representation without access to U or R.

## 8. Package implications

Freeze Package 001 must be regenerated from this specification.

The previous package is invalid and MUST NOT be treated as a freeze candidate.

No result from the invalid package may be used as evidence.

## 9. Execution boundary

NOT AUTHORIZED.

A new package must pass: package materialization audit; freeze preflight; explicit freeze decision.

No conformance execution is authorized before those gates pass.

## 10. Decision

DESIGN 005 — READY FOR DESIGN AUDIT.

No change to TGCV Core, RMA, Evidence-to-Claim Matrix, claim thresholds, or empirical evidence status.