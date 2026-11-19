# C10-S F1 — Numerical stress v003 execution result

**Status:** EXECUTION COMPLETED — TECHNICAL RESULT MIXED — F1 VALIDATION OPEN  
**Workflow run:** 44550116151 (attempt 1)  
**Workflow URL:** https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44550116151  
**Authorization:** C10S-F1-NUMERICAL-STRESS-20261119-005 (CONSUMED)  
**Authorization commit:** 65cad11a5ff6039b5a6fca68e8c166be4babb123  
**Frozen source:** e526acb04e1d2c2421fa2663a43e31b537985522  
**Artifact:** c10s-f1-numerical-stress-v3-44550116151 (ID 14543050995)  
**Artifact SHA-256:** 13a131429004433d6006dce234325529a604e5ed56f3e89a7aa59d42c2fa9d74  
**Records SHA-256:** 37db928f3d09bbe6688d554649229b5693708e830871b752eb3016746f42e9cf  
**Summary SHA-256:** 2c7dbda7af42d58380f989bc449aa8f2e7b7d18a3b18abc2677e26cae8e456e7  
**Runtime:** CPython 3.12.3 / ubuntu-24.04  
**Exit code:** 0

## 1. Execution integrity

The dedicated v003 job completed successfully. Authorization preflight, frozen source and transitive blob verification, one-shot consumption, diagnostic invocation and artifact upload all completed successfully. Exactly 79 records were emitted: 64 N2, 14 N4 and 1 N5.

The authorization is consumed and execution_authorized=false. No retry or replay was performed. No tests, compilation, Monte Carlo calibration, DGP experiment or scientific C10 execution took place.

## 2. N2 — ULP perturbations near the discriminant boundary

Across 64 records:
- Ideal discriminant sign: POSITIVE in 64/64.
- Represented discriminant sign: POSITIVE in 40/64 and NEGATIVE in 24/64.
- Topology comparison: PRESERVED 30, CHANGED 18, UNRESOLVED 16.
- By gap exponent 28, 32 and 36: each has 10 PRESERVED and 6 CHANGED.
- At gap exponent 40: all 16 are UNRESOLVED.

**Critical limitation:** all 64 records have f1_root_result=NOT_EVALUATED_ARBITRARY_POLYNOMIAL_API_UNAVAILABLE. The results characterize exact-rational Sturm topology of ideal versus binary64-represented coefficients; they do not validate the production F1 reconstruction on arbitrary polynomials. Thus N2 is a representation/topology diagnostic, not an end-to-end F1 success rate.

## 3. N5 — exact binary64 rounding cells

The ideal polynomial has discriminant +1 and two simple real roots. The represented binary64 polynomial has discriminant zero and one double root. Both exact Sturm analyses isolate their respective roots. The discriminant enclosure over the coefficient rounding cells spans negative and positive values, so the rounding-cell topology is classified TOPOLOGY_UNCERTAIN_AT_ROUNDING_RESOLUTION.

This demonstrates that the rounded coefficient tuple alone does not preserve the ideal polynomial's root topology in this constructed case. The enclosure does not establish a unique topology over the full rounding cell.

## 4. N4 — Cauchy versus Fujiwara

Fujiwara/Sturm isolated one root in all 14 cases. Compared with the frozen v002 Cauchy result:
- BOTH_RESOLVED: 9/14.
- RESOLVED_AFTER_TIGHTER_BOUND: 5/14, at exponents 40, 44, 48, 50 and 100.
- The five corresponding v002 Cauchy results were ROOTS_UNRESOLVED.

This is positive comparative evidence that the tighter Fujiwara bound improves resolution under the frozen isolator and depth limit for the five high-scale cases.

**Causal-mechanistic limit:** the recorded midpoint_depth_estimate is explicitly marked APPROXIMATE_BUDGET_NOT_ACTUAL_SUBDIVISION_TRACE. It estimates 280, 304, 328, 340 and 640 levels for the five rescued cases, but the run did not record actual subdivision counts or an exhaustion trace. Therefore the experiment supports the excessive-initial-bound hypothesis but does not prove that actual depth consumption from the Cauchy starting bound was the mechanism. The Cauchy/Fujiwara bound ratios also vary substantially by scale.

## 5. Overall adjudication

- Execution integrity: PASS.
- Record count and artifact generation: PASS (79/79).
- N4 comparative outcome: POSITIVE, 5 previously unresolved cases resolved by Fujiwara.
- N5 rounding-cell diagnostic: INDETERMINATE topology at rounding-cell resolution, with ideal/represented topology divergence.
- N2 topology diagnostic: MIXED; 18 changed, 30 preserved, 16 unresolved.
- End-to-end F1 arbitrary-polynomial reconstruction validation: NOT ESTABLISHED (API unavailable for all N2 records).
- Actual N4 subdivision-depth mechanism: NOT ESTABLISHED (no actual subdivision trace).
- Global numerical robustness of F1: NOT ESTABLISHED.
- Scientific C10-S / causal contribution of ΔT_acc to Value: NOT EXECUTED and NOT ADDRESSED.

## 6. Required follow-up before claiming F1 closure

1. Add or expose a production-compatible arbitrary-polynomial F1 entry point for N2, without changing the frozen diagnostic result; then design a separately authorized validation.
2. For N4, instrument actual subdivision depth, interval counts and stopping reason, or otherwise obtain a direct trace from the same frozen isolator. Do not infer actual depth consumption from midpoint estimates.
3. Audit the legacy per-record generator_version field in N2 records: the aggregate manifest identifies generator v003, while individual N2 rows report a v001 helper version. Establish whether this is intentional provenance for the reused helper or a misleading record-level label before downstream reuse.
4. Keep N2/N4/N5 findings scoped to these deterministic fixtures. No broad claim of global F1 robustness follows.

**Conclusion:** v003 is a successful deterministic diagnostic execution with a meaningful N4 improvement, but it is not a validation closure. F1 remains open, and C10-S causal execution remains separate and unauthorized.
