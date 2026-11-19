# C10-S F1 — Numerical Stress Harness Static Design Review 001

**Status:** DESIGN REVIEW RECORDED — IMPLEMENTED SOURCE AMENDED — NOT EXECUTED  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Reviewed baseline:** `d65686beb2b242c0acb8ffbbcfe8ff55437f6c8b`  
**Scope:** static reconciliation of the adversarial design, harness implementation and existing frozen F1/Sturm contracts.

## 1. Executive disposition

The first implementation was directionally correct but did not yet fully operationalise its stated objectives. Four material issues were found and corrected additively in the harness:

1. the N4 inverse scale for nuisance-variance roots was wrong by one power of the observation scale;
2. N4 recorded equivariance quantities but did not adjudicate them against a baseline or a predeclared tolerance set;
3. N5 used only one order-one root fixture, despite the design requiring near-zero, endpoint and large-magnitude cases;
4. the implementation note's fixture count needed updating after N5 expansion.

The corrected harness remains separate from and does not modify the frozen F1, Sturm or adjudication source modules. No test, compilation, smoke test, fixture runner or scientific execution was performed.

## 2. Finding A — N4 variance-coordinate mapping

For an observation transformation (y' = c y), all variance coordinates transform as (	au' = c^2	au). The positive roots of the F1 nuisance-variance score polynomial are also in a variance coordinate and therefore transform by (c^2).

The initial harness divided those roots by (c), which was dimensionally incorrect. It now maps them back using (c^{-2}), consistently with the MLE and LR interval endpoints.

This correction changes only the new harness.

## 3. Finding B — N4 requires an actual equivariance adjudication

The existing frozen tests establish reference tolerances for the same fixture family:

- profile log-likelihood scale relation: absolute agreement to 7 decimal places;
- MLE after inverse variance scaling: absolute delta (10^{-10});
- LR endpoints after inverse variance scaling: absolute delta (10^{-8}).

The harness now records the expected profile log-likelihood shift
[
ell(cy;c^2	au)=ell(y;	au)-rac{df_w+df_b}{2}log(c^2)
]
and checks it against an absolute tolerance of (10^{-7}).

It also checks:
- inverse-scaled MLE (absolute tolerance (10^{-10}));
- inverse-scaled lower and upper LR endpoints (absolute tolerance (10^{-8}));
- number and locations of inverse-scaled F1 nuisance-score roots (maximum relative location error (10^{-7}));
- invariance of the F1 polynomial and root-adjudication status.

These are software-characterization tolerances, grounded in the existing frozen test contract. They are not inferential or scientific acceptance thresholds. If the k=0 baseline itself cannot be produced, the scale comparison is unavailable; the harness must not fabricate a baseline.

## 4. Finding C — N5 root-magnitude and endpoint coverage

N5 now uses four deterministic fixtures, each crossed with the existing three width settings and five depth settings:

1. order-one close pair;
2. close pair near zero;
3. close pair at large root magnitude (2^{120});
4. close pair whose larger root is exactly the finite upper-domain endpoint.

This yields 4 × 3 × 5 = 60 N5 records. Combined with the other 55 base fixtures, the polynomial/Sturm lane contains 115 planned records.

The absolute-width contract remains unchanged. Consequently, a large-magnitude fixture may require more bisection depth than a small-magnitude fixture. `ROOTS_UNRESOLVED` under an intentionally insufficient depth is an expected fail-closed observation, not a solver failure and not a PASS for root-location accuracy. The results must preserve width, depth and fixture identity.

The exact endpoint fixture checks singleton endpoint representation through the existing isolator contract. No new endpoint semantics are introduced.

## 5. Finding D — Ideal versus perturbed coefficient provenance

N2 retains both:
- the ideal polynomial coefficients and their ideal roots;
- the actual coefficient vector after deterministic ULP perturbation.

The exact binary64 values and their rationalisation are separately recorded. This avoids incorrectly attributing the root geometry of the ideal polynomial to the perturbed polynomial. The reference root set for any future comparison must be computed from the actual binary64 vector.

## 6. F1-versus-Sturm interface decision

The current F1 implementation has no public pure-polynomial solver entry point. Its critical-point reconstruction depends on model-derived sufficient statistics. The existing adjudicator takes observed rows and reconstructs that polynomial internally.

**Decision for this gate:** retain two lanes; do not introduce a new pure-polynomial F1 solver API into the frozen baseline.

- N1–N3 and N5–N6 characterize the exact-rational Sturm reference, coefficient representation and isolation limits.
- N4 exercises the actual data-derived F1 → Sturm → adjudication path.
- The harness must not report F1/Sturm agreement, false-agreement or false-discrepancy rates for arbitrary polynomial fixtures, because F1 is not evaluated on those fixtures.

A generic polynomial solver interface could be a separately justified future engineering task, but it is not required to test the present F1 implementation end-to-end and would enlarge the frozen software surface. It is therefore deferred rather than smuggled into this stress gate.

## 7. Evidence schema and reproducibility boundary

The callable runners return deterministic in-memory Python records. A separate writer persists supplied records; it does not initiate or repeat execution. This is acceptable for static implementation, but not yet a complete governed evidence pipeline.

Before authorization, the execution package must specify:
- canonical JSON serialization (UTF-8, sorted keys, fixed separators, no NaN/Infinity);
- one JSONL record per fixture/scale × resolution configuration;
- a summary JSON with planned, generated, representable, resolved, unresolved and fail-closed denominators;
- SHA-256 of raw JSONL, summary JSON, source snapshot and environment manifest;
- exact runtime and dependency versions;
- stdout/stderr capture and a one-shot run identity.

The harness now includes an explicit `write_stress_evidence()` function that accepts already-produced result objects and writes canonical JSONL, summary JSON and a SHA-256 manifest containing source-file hashes and runtime versions, including the observed-data interface module used transitively by F1. It does not invoke the runners. This writer has not been executed; its behavior remains statically reviewed only. Full stdout/stderr capture and workflow-level run identity remain responsibilities of the governed execution workflow.

## 8. Revised scope and counts

- Polynomial/Sturm lane: 59 base fixtures, 115 records after N5 expansion.
- F1 end-to-end scale lane: 7 predeclared observation scales.
- ULP perturbations: independent ±1/±2 ULP steps per nonzero coefficient of the selected base cubic.
- No random generation.
- No arbitrary-polynomial F1 comparison.
- No Monte Carlo calibration, DGP experiment, inferential coverage study or scientific C10 execution.

These are planned counts only. No runner was invoked.

## 9. Remaining pre-authorization gates

1. Static review of the amended source and exact blob identities.
2. Statically verify the JSONL/summary writer, source hashes and output manifest contract.
3. Define the runtime/workflow and resource/time limits.
4. Freeze the complete source/protocol snapshot.
5. Prepare a new one-shot authorization for only the numerical stress harness.

The prior authorization for the 73-test validation is consumed and cannot authorize this new stress execution.

## 10. Current status

| Layer | Status |
|---|---|
| Historical 73-test integrated validation | PASS — historical frozen snapshot |
| Adversarial design | DEFINED |
| Deterministic fixture generator | IMPLEMENTED — static review only |
| N4 equivariance metrics | IMPLEMENTED — not executed |
| N5 root-magnitude/depth ladder | IMPLEMENTED — not executed |
| F1 arbitrary-polynomial comparison | NOT AVAILABLE — explicitly excluded |
| Persistent evidence serialization/audit | IMPLEMENTED — NOT EXECUTED; workflow stdout/stderr capture specified |
| Numerical stress execution workflow | IMPLEMENTED — FAIL-CLOSED; authorization remains DRAFT |\n| Numerical stress execution | NOT AUTHORIZED |
| Monte Carlo / scientific C10-S execution | NOT AUTHORIZED |

**Next operation:** await explicit user approval of the exact one-shot authorization. Approval must be recorded in the authorization file and in a commit carrying the workflow's approval marker; that commit triggers one execution and consumes the authorization. No runner or writer execution is authorized before that approval.
