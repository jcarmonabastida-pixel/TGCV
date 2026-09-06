# DR-027A — Rust Runtime Identity Correction v0.1

**Status:** ACCEPTED — LIMITED OPERATIONAL CORRECTION
**Date:** 2026-09-07
**Scope:** EXT-1.1 Rust confirmatory execution only

## 1. Trigger

The first invocation of the authorized confirmatory runner (`--mode primary`) terminated before any scientific computation because the runner compared the runtime string produced by `platform.platform()` against an over-specific literal containing `SP0`.

Observed runtime identity:

`Windows-11-10.0.26200`

Frozen runtime identity in DR-026D/DR-027:

`Windows 11 10.0.26200-SP0`

The discrepancy is representational only. The invocation terminated at the OS gate; no `Y_180`, `T_acc`, model fit, prediction, performance metric, or inferential quantity was computed.

## 2. Authorized correction

The runner's OS identity literal is corrected from:

`Windows-11-10.0.26200-SP0`

to the actual frozen platform identity emitted by the execution environment:

`Windows-11-10.0.26200`

This correction changes **only the runtime identity validation string**. It does not alter any scientific quantity, transformation, resolver rule, population rule, outcome definition, feature representation, hashing rule, split, learner, hyperparameter, metric, seed, exclusion rule, or inference policy.

## 3. Explicit invariants

The following remain unchanged and binding:

- Dataset SHA-256: `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`
- Python: `3.14.7`
- scikit-learn: `1.9.0`
- NumPy: `2.5.2`
- SciPy: `1.18.1`
- Machine: `AMD64`
- `random_state=0`
- Resolver SHA-256/Git blob SHA: `669d4f01131af518f32b1b4b3da27f676ae4ae55`
- Solver: `liblinear`
- L2 penalty, `C=1.0`, `tol=1e-8`, `max_iter=1000`, `fit_intercept=True`, `class_weight=None`
- Hash dimension: `2**20`
- DR-023 outcome and 180-day horizon
- DR-024 population/exclusion policy
- DR-025A baseline representation
- DR-026A T_acc representation
- DR-026C model/evaluation protocol
- DR-026D deterministic runtime protocol
- DR-027 confirmatory execution sequence: primary followed by identical replay

## 4. Execution authorization effect

DR-027 remains the governing confirmatory authorization. DR-027A supersedes only the defective runner identity literal and the corresponding runner identity binding in the structural audit.

Because the executable runner changed, confirmatory execution remains **stopped** until the updated DR-027 structural audit is run locally and returns `DR027_STRUCTURAL_AUDIT_PASS: True` with all prohibited-computation flags false.

No scientific execution is authorized from the failed invocation, and its failure is not an experimental result.

## 5. Governance interpretation

This correction is classified as an infrastructure-level conformance repair discovered before scientific computation. It is not a data-driven protocol change and is not informed by any experimental outcome.

**Decision:** ACCEPTED as a limited ex-ante operational correction, with revalidation of the DR-027 structural gate required before primary execution.
