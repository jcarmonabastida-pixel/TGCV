# TGCV — RMA current state

**Date:** 2026-08-27  
**Status:** WORKING / OPERATIVE

This current RMA pointer supersedes neither historical RMA v0.1 nor frozen experiment records. It integrates their traceability with the current empirical state.

## Canonical Core

`S` → `T_acc = F(S,C,L)` → `ΔT_acc` → `ΔReach → ΔTrajectory` → downstream `Outcome → Value`.

`I` is mechanism, not Core primitive.

## Empirical evidence

- Historical `TGCV-EXT-1.0 / CollegeMsg`: FAIL / NO SUPPORT under locked `ΔLogLoss >= 0.04` criterion; observed `ΔLogLoss=0.008717`.
- `TGCV-EMP-1.1`: PRIMARY TEST PASS under frozen computational operationalization; `ΔLogLoss=0.07942`, `δ=0.04`, paired sign-flip `p<0.000005`.
- Structural intervention: 5,000 matched pairs, paired mean difference `-0.0078`, `p≈0.037`.

These results are not universal validation. They support the specified operationalization and motivate independent replication/domain validation.

## Asset states

| Asset | Current state |
|---|---|
| Core | FOUNDATIONAL / STABILIZED |
| MVE-1.0 | FROZEN historical state |
| TGCV-EMP-1.1 protocol | FROZEN |
| TGCV-EMP-1.1 results | EMPIRICALLY TESTED / PRIMARY TEST PASS |
| Vision Paper v0.1 | WORKING / CONDITIONAL historical version |
| TCP v0.2 | WORKING / CONDITIONAL historical version |
| IE Research Prospectus application version | APPLICATION HISTORY |
| Orange v5.1 note/emails | APPLICATION/INDUSTRIAL CONTEXT |
| UAM track | MATERIALS NOT RECOVERED as a distinct canonical UAM set |
| SLR-1 | OPEN prior-art absorption gate |

## Rules

1. Experimental evidence is propagated through the RMA before changing external claims.
2. Negative and positive experiments are both retained.
3. No result is used to rewrite the Core retrospectively.
4. Application material cannot redefine the scientific Core.
5. Every substantive change gets a new version/commit.
6. Frozen records are immutable.
