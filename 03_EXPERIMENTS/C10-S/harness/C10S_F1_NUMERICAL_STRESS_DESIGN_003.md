# C10-S F1 — Numerical Stress Diagnostic Design v003

**Status:** DESIGN DEFINED — IMPLEMENTED IN SEPARATE V003 FILES — STATIC REVIEW CONDITIONAL — EXECUTION NOT AUTHORIZED  
**Predecessor:** v002 primary execution, result 002  
**Research branch:** `research/c10s-f1-integrated-correction-20261119`  
**Purpose:** discriminate coefficient-rounding uncertainty from root-isolation domain inefficiency and characterize the next ULP-to-discriminant boundary without repeating v002.

## 1. Decision and historical reconciliation

V003 is a diagnostic successor, not a rerun or a repair of the frozen v002 source.

The following v002 evidence is retained unchanged:

| Finding | Existing result | V003 treatment |
|---|---|---|
| Near-double ULP family at gap (2^{-24}) | 16/16 topology PRESERVED | Retain as historical bounded evidence; do not regenerate |
| N5 large-magnitude pair | 3 width configurations CHANGED, all one underlying polynomial | Reuse exact coefficients and binary64 hex; add one coefficient-rounding-cell diagnostic |
| N4 observation ladder | 9/14 Sturm isolated; 5/14 unresolved; observed bracket 36–40 | Reuse all 14 recorded score-polynomial coefficient vectors; compare root bounds |
| N3 covariant lane | 5 PASS / 2 representation UNRESOLVED | No repetition in v003 |
| Other v002 polynomial records | 65 topology comparisons UNRESOLVED | Preserve denominator and historical classification; no retest |

The 73 deterministic unit tests and the v002 152-record numerical stress execution are different evidence classes. Neither is repeated by this design. The v002 primary run passed its execution/integrity checks, while the numerical robustness outcome remains MIXED / BOUNDED and the final execution-result audit remains INDETERMINATE because replay was prohibited.

## 2. V003 scope and denominators

The proposed deterministic roster contains **79 new diagnostic records**:

| Lane | Records | Purpose |
|---|---:|---|
| N2 discriminant-proximity ULP family | 64 | Four new root-gap levels × four independently perturbed coefficients × four ULP directions |
| N5 rounding-cell topology diagnostic | 1 | Exact coefficient rounding cells and discriminant enclosure for the existing counterexample |
| N4 root-bound comparison | 14 | Existing observation-scale ladder, with an alternative exact positive-root bound |
| **Total** | **79** | Fixed before implementation; no random or adaptive additions |

No v002 record is overwritten, reclassified or removed. The N2 v002 16/16 result remains a separate historical denominator.

## 3. N5 — coefficient rounding cells and topology uncertainty

### 3.1 Exact counterexample retained

The existing fixture is the quadratic with ascending coefficients:

[
(a,b,c)=left(N(N+1),-(2N+1),1ight),qquad N=2^{120}.
]

Its ideal discriminant is:

[
Delta_{mathrm{ideal}}=b^2-4ac=1,
]

so the ideal polynomial has two distinct real roots (N) and (N+1).

The recorded binary64 coefficient vector is:

[
(a_f,b_f,c_f)=(N^2,-2N,1),
]

whose exact rationalized polynomial has:

[
Delta_{mathrm{represented}}=0,
]

and one double root at (N). The finite conversion therefore changes topology. The three v002 CHANGED records are three isolation-width settings for this one coefficient vector, not three independent fixtures.

### 3.2 New diagnostic

For each rounded coefficient (f_i), derive its exact round-to-nearest-even preimage cell from the adjacent finite binary64 values:

[
I_i=[m(f_i^-,f_i),m(f_i,f_i^+)]
]

with endpoint inclusion/exclusion determined by the ties-to-even significand rule. Midpoints and all calculations are rational; no decimal approximations are used.

Construct the coefficient box (I_a	imes I_b	imes I_c). Evaluate a conservative exact-rational interval enclosure of:

[
Delta=b^2-4ac.
]

Classify:

- `ROBUST_TWO_REAL`: the entire discriminant enclosure is strictly positive;
- `ROBUST_NO_REAL_PAIR`: the entire enclosure is strictly negative;
- `TOPOLOGY_UNCERTAIN_AT_ROUNDING_RESOLUTION`: the enclosure contains zero;
- `DIAGNOSTIC_UNRESOLVED`: a coefficient cell or interval calculation cannot be represented under the declared exact rules.

The interval enclosure may be conservative: containing zero means the diagnostic cannot certify topology over the rounding cell, not that both signs have necessarily been attained. No sign conclusion may be inferred from the represented discriminant alone.

Also record, coefficient by coefficient:
- ideal rational value;
- rounded binary64 hexadecimal value and exact rationalization;
- exact rounding error;
- exact lower/upper rounding-cell boundaries and endpoint closure;
- whether the ideal coefficient is exactly representable;
- exact ideal and represented discriminants;
- exact interval enclosure and its classification.

This diagnostic distinguishes “finite binary64 conversion” from “exact coefficient preservation” and from “topology certified over the coefficient uncertainty cell”.

## 4. N2 — closer-to-discriminant-boundary ULP family

The v002 family at gap (2^{-24}) is retained and not repeated.

V003 adds four predeclared cubic root-gap levels:

[
kin{28,32,36,40},qquad
(r_1,r_2,r_3)=(1,1+2^{-k},-2).
]

For each level, independently perturb each of the four ascending coefficients by (-2,-1,+1,+2) adjacent binary64 steps. This yields:

[
4	ext{ levels}	imes4	ext{ coefficients}	imes4	ext{ steps}=64
]

records. There is no combinatorial cross-product and no post-outcome selection.

For every record retain the exact ideal coefficient vector, the actual binary64 vector, its exact rationalization, exact discriminants of the ideal and represented cubic, ideal/represented exact-rational root counts and multiplicities, and the perturbation identity.

The discriminant is computed from the ascending coefficient tuple ((a,b,c,d)) using the exact cubic formula:

[
Delta=c^2b^2-4db^3-4c^3a-27d^2a^2+18dcba.
]

Report the sign transition as a topology change only when both exact-rational root isolations complete. If either side is unresolved, classify the comparison as UNRESOLVED and retain it in the denominator. No “robustness percentage” may discard unresolved records.

The purpose is to measure where the existing coefficient-ULP perturbation protocol ceases to preserve topology as the ideal discriminant approaches zero. It is not intended to demonstrate a predetermined failure.

## 5. N4 — diagnose Cauchy-bound depth consumption

### 5.1 Hypothesis to test, not a result to assume

The v002 independent isolator is called on the positive half-line with no explicit upper endpoint. Its implementation obtains a generic Cauchy bound:

[
B_C=leftlceil1+max_{i<n}|a_i/a_n|ightceil.
]

The score polynomial coefficients recorded in N4 have a strongly separated scale pattern. The F1 positive-root estimate, mapped back to the observation-scale variance coordinate, is of order (2^{2e}), while the constant coefficient and generic Cauchy bound grow approximately as (2^{6e}). This can spend many subdivision levels reducing the initial upper endpoint before the interval reaches the root's scale.

A midpoint-budget approximation suggests why the observed transition may occur near the max-depth limit:

[
d_{mathrm{coarse}}approxleftlceillog_2(B_C/r_{F1})ightceil,qquad
d_{mathrm{local}}approxleftlceillog_2(r_{F1}/w)ightceil,
]

where (r_{F1}) is only the recorded binary64 candidate mapped to the current scale and (w=10^{-12}). Their sum is a diagnostic estimate, not a proof of the actual branch depth. The v002 isolator does not expose its subdivision trace, and v002's generic `ROOTS_UNRESOLVED` status alone does not prove that max depth was the cause.

### 5.2 Alternative exact positive-root bound

For each recorded cubic

[
p(x)=a_3x^3+a_2x^2+a_1x+a_0,
]

derive an exact-rational Fujiwara bound:

[
B_F=2maxleft{
left|a_0/a_3ight|^{1/3},
left|a_1/a_3ight|^{1/2},
left|a_2/a_3ight|
ight}.
]

Round the bound outward to an integer using exact integer arithmetic (exact ceiling of rational square/cube roots); do not use floating-point roots to construct the bound.

For each of the same 14 N4 records:
1. Reconstruct the exact rational coefficient tuple from the stored binary64 hexadecimal values in v002.
2. Record the exact Cauchy bound and exact Fujiwara bound.
3. Record (B_C/B_F), the mapped F1 candidate, the exact rational width (10^{-12}), and the two-part midpoint-depth estimate.
4. Call the existing frozen exact-rational isolator with the same coefficients, lower endpoint 0, width (10^{-12}), and max depth 256, but supply (B_F) as the explicit upper endpoint.
5. Record the result and compare it with the already-recorded v002 Cauchy-domain status. Do not rerun the Cauchy-domain baseline.

This changes only the finite search-domain bound supplied to the existing isolator. It does not change the isolator implementation, coefficient vector, width, depth, F1 profile, score polynomial or adjudication tolerances.

Interpretation:
- If Fujiwara-bound isolation resolves cases that were unresolved under the Cauchy bound, this supports the hypothesis that generic-bound overhead consumed the depth budget.
- If it remains unresolved, the cause is not established by this comparison; a separate instrumented subdivision trace would be needed before proposing any solver change.
- If either bound cannot be constructed exactly, classify the record as UNRESOLVED.

The 14 records remain the full N4 denominator. No adaptive exponents are inserted around 36–40.

## 6. Prohibited interpretation and scope boundaries

- Do not claim that v002's N4 failure was caused by max-depth exhaustion until the alternative-bound comparison supports that diagnosis.
- Do not describe a tighter bound as a general solver correction or as validated beyond this frozen N4 ladder.
- Do not call a rounding-cell interval that contains zero a demonstrated two-topology realization; it is a conservative uncertainty classification.
- Do not infer general ULP robustness from either the v002 16/16 family or the proposed v003 grid.
- Do not change tolerances, max depth, isolation width, root-matching rules, fixtures or exponents after observing v003 outputs.
- Do not change the frozen v001/v002 source, result records or artifacts.
- No unit-test suite, Monte Carlo calibration, DGP experiment, inferential coverage study, parameter tuning or scientific C10-S execution is included.
- No replay is authorized by this design. The v002 final execution-result audit remains INDETERMINATE; this design does not waive or rewrite that status.

## 7. Proposed implementation and execution boundary

Implementation, if separately authorized as design work, must live in new v003 files and import the frozen v001/v002 source read-only. It must not modify the existing isolator, F1 modules, v001 generator or v002 generator.

Before any numerical execution, create:
- v003 implementation/static-review record;
- exact source and dependency blob manifest;
- dedicated workflow with immutable source checkout and exact runtime;
- one-shot authorization pinning the source, workflow, command, 79-record roster, outputs, timeout and prohibitions;
- explicit approval for that exact authorization.

A future v003 execution would be a new diagnostic numerical operation. It is not authorized by the approval or consumed authorization 004.

## 8. Current gate state

| Gate | State |
|---|---|
| v002 source and result | FROZEN / EXECUTED / PRIMARY INTEGRITY AUDITED |
| v002 numerical robustness | MIXED / BOUNDED |
| v002 final execution-result audit | INDETERMINATE — replay prohibited |
| N5 rounding-cell diagnostic | DEFINED — NOT IMPLEMENTED |
| N2 closer discriminant-boundary grid | DEFINED — NOT IMPLEMENTED |
| N4 alternative-bound comparison | DEFINED — NOT IMPLEMENTED |
| v003 implementation | IMPLEMENTED — STATIC REVIEW CONDITIONAL |
| v003 execution | NOT AUTHORIZED |
| Monte Carlo calibration | NOT AUTHORIZED |
| Scientific C10-S execution | NOT AUTHORIZED |

**Next operation:** obtain fresh explicit approval for authorization 005 if and only if the user wants the single 79-record numerical diagnostic. Numerical execution remains unauthorized until that approval is applied to the exact draft.
