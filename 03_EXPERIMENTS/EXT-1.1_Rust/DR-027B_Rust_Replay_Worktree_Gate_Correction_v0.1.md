# DR-027B — Rust Replay Worktree Gate Correction v0.1

**Status:** ACCEPTED — LIMITED OPERATIONAL CORRECTION
**Date:** 2026-09-07
**Scope:** EXT-1.1 Rust confirmatory execution only

## 1. Trigger

The authorized `primary` execution completed successfully and produced its two confirmatory output files under `execution/CONFIRMATORY_PRIMARY_v01/`. The subsequent `replay` invocation stopped before scientific computation because the runner's worktree-hygiene check incorrectly compared Git's repository-relative status paths against absolute filesystem prefixes.

Observed Git status:

`?? 03_EXPERIMENTS/EXT-1.1_Rust/execution/CONFIRMATORY_PRIMARY_v01/`

The primary output directory is an explicitly authorized execution-output location and must be permitted by the runner. No scientific computation occurred during the failed replay invocation.

## 2. Authorized correction

Correct only the implementation of `git_clean_for_execution()` so that the allowlist is expressed in the same repository-relative path space returned by `git status --porcelain`.

The correction must continue to reject every dirty path outside:

- `03_EXPERIMENTS/EXT-1.1_Rust/execution/CONFIRMATORY_PRIMARY_v01/`
- `03_EXPERIMENTS/EXT-1.1_Rust/execution/CONFIRMATORY_REPLAY_v01/`

No output is deleted, modified, interpreted, or used for scientific selection by this correction.

## 3. Explicit invariants

Unchanged and binding:

- Dataset SHA-256: `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`
- Python: `3.14.7`
- scikit-learn: `1.9.0`
- NumPy: `2.5.2`
- SciPy: `1.18.1`
- Machine: `AMD64`
- `random_state=0`
- Resolver blob SHA: `669d4f01131af518f32b1b4b3da27f676ae4ae55`
- Solver: `liblinear`
- L2 penalty, `C=1.0`, `tol=1e-8`, `max_iter=1000`, `fit_intercept=True`, `class_weight=None`
- Hash dimension: `2**20`
- DR-023 through DR-026D scientific protocol
- DR-027 primary/replay sequence
- Primary result already generated is preserved as-is

## 4. Governance interpretation

This is an infrastructure-level conformance repair. It was discovered after primary completion but before any replay scientific computation and is not informed by the primary outcome. The scientific protocol, population, outcome, representation, resolver, model, split, metric, and seed remain unchanged.

Because the executable runner changes, the DR-027 structural audit must be rerun locally and return `DR027_STRUCTURAL_AUDIT_PASS: True` with all prohibited-computation flags false before replay is attempted.

**Decision:** ACCEPTED as a limited operational correction; replay remains blocked pending updated structural audit.