# C10-S — P178 Student-t exact-cache probe 001

**Status:** PASS for numerical equivalence; NO-GO for performance adoption  
**Date:** 2026-11-12  
**Scope:** one-cell, non-confirmatory optimization probe on the frozen primary source. No production code was changed.

## Provenance

- Repository: `jcarmonabastida-pixel/TGCV`
- Source commit checked out: `689c8f0164e0625ca536a20b1805e555cd63d5fd`
- Probe workflow: `43119166570`
- Workflow commit: `51a721ca710e1114ab572b2a6f3aebc387d12c64`
- Workflow result: `completed / success`
- Artifact ID: `13898534919`
- Artifact SHA-256: `112f4910e5e42e143f18cf24dad3519891dd5d5c15b1523fc3cad4217358cf08`
- Environment: Python 3.12.16, NumPy 2.3.5, SciPy 1.17.0
- Frozen cell: K=10, pi0=0.5, positive, N=700, R=10,000, seed=20261495

## Comparison

| Variant | Wall time | CPU time |
|---|---:|---:|
| Original uncached function | 34.332 s | 34.278 s |
| Exact-float-key LRU cache | 34.006 s | 34.004 s |

Observed wall-time reduction: approximately 0.95%, not a material performance gain.

Cache statistics: 1 hit, 9,999 misses, maxsize 8,192, current size 8,192. The Welch/Satterthwaite degrees of freedom vary across replications, so exact-key memoization almost never reuses a critical value. The cache also retains entries that cannot be reused within this run.

## Numerical equivalence

**PASS.** All reported metrics were exactly equal between the baseline and cached variants (`metrics_identical=true`). The run also matched the frozen P178 reference for this cell (`reference_match=true`); 10,000 valid replications, zero invalid replications, zero classification errors, zero abstentions. Reference absolute differences were zero or floating-point roundoff at approximately 10^-17.

## Decision

**Do not adopt the exact-float-key LRU cache.** Although it preserves exact outputs in this cell, its 0.95% timing reduction is negligible and its 1/9,999 hit rate confirms the cache key has insufficient reuse. Keep the original Student-t critical-value calculation unchanged.

Do not round or bucket degrees of freedom merely to increase cache hits: that would change the numerical method and requires a separate error-bounded approximation study, independent of this exact-equivalence probe.

This is a one-cell performance probe only. It is not a 27-cell replay, not a full-run reproducibility audit, and not new scientific evidence for TGCV.

## Next technical direction

The profile's repeated Student-t quantile calculation remains a candidate bottleneck, but exact memoization is rejected. Any further optimization should first investigate whether a validated library quantile implementation or a numerically controlled approximation can reduce cost while meeting a predeclared equivalence/error bound against the current implementation across the full relevant degrees-of-freedom range. No replacement is authorized by this probe.
