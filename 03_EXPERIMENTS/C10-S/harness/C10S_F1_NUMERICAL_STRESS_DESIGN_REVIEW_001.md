# C10-S F1 — Numerical stress design review 001

**Status:** STATIC REVIEW COMPLETE — DESIGN AMENDMENT REQUIRED — NO EXECUTION  
**Research branch:** `research/c10s-f1-integrated-correction-20261119`  
**Reviewed result:** `C10S_F1_NUMERICAL_STRESS_RESULT_001.md`  
**Reviewed protocol:** `C10S_F1_NUMERICAL_STRESS_DESIGN_DRAFT_001.md`  
**Reviewed generator blob:** `cc047a3b112caf84533c94e77d1908c99a0c2bdf`  
**Reviewed isolator blob:** `3ac9ce31eb82421022fd8d2a65a0daee049322be`  
**Reviewed freeze manifest:** `C10S_F1_NUMERICAL_STRESS_FREEZE_MANIFEST_003.md`  
**Prior authorization 003:** CONSUMED AND CLOSED; NOT REUSABLE

## 1. Purpose and boundary

This review reconciles the 122-record deterministic stress execution with the existing generator, isolator and frozen protocol. It specifies the minimum next design increment. It does not run tests, invoke the stress runners, tune numerical parameters, alter the frozen source or authorize another execution.

The 73/73 integrated tests remain a historical software-test result. The 122-record stress run is a separate adversarial characterization with a mixed result. Neither is rewritten or retroactively upgraded.

## 2. Historical work retained

The following work is compatible and must be reused:
- integrated F1 implementation and its 73/73 deterministic test result;
- exact-rational Sturm isolator and its fail-closed `ROOTS_UNRESOLVED` contract;
- deterministic generator v001 and its 115 polynomial/Sturm plus 7 F1 scale records;
- result 001 and its artifact/provenance hashes;
- one-shot authorization 003 and its closed execution record.

No prior fixture roster or observed outcome is to be silently replaced. The next design is an explicit successor, not a rerun or reinterpretation of the 122 records.

## 3. Static findings in the current generator

### 3.1 Ideal and represented coefficient vectors are retained, but topology is not formally adjudicated

The generator records:
- exact ideal coefficients;
- exact pre-conversion coefficients after any declared perturbation;
- binary64 hexadecimal values;
- exact rationalizations of those binary64 values;
- ideal real roots.

It then invokes Sturm on the binary64 values. It does **not** invoke the same exact-rational isolator on the ideal coefficient vector and formally compare the ideal and represented root topologies. The result report therefore had to identify N1 E52/E54 and the N5 large-magnitude discrepancy by post-run inspection.

**Required amendment:** for each polynomial fixture, isolate both:
1. the ideal exact-rational polynomial; and
2. the exact rational polynomial represented by the actual binary64 coefficient vector.

Use the same declared domain for both. Record root count, multiplicity, interval endpoints, and comparison status. Add a separate topology comparison field with exactly:
- `PRESERVED`;
- `CHANGED`;
- `UNRESOLVED`.

Keep this separate from the existing solver status. A represented polynomial can be successfully isolated while its topology differs from the ideal polynomial. Conversely, failure to isolate either polynomial is unresolved, not proof of topology change.

Do not label this as F1/Sturm disagreement: the arbitrary-polynomial lane is a Sturm representation diagnostic; the F1 API still does not accept injected arbitrary polynomials.

### 3.2 ULP block is deliberately narrow

N2 perturbs each coefficient of one simple cubic by ±1 and ±2 ULP. It does not include a near-double or ill-conditioned base polynomial. Its 16/16 result is valid for that roster only.

**Required amendment:** preserve the existing 16 records unchanged. Add a separately identified near-double exact-rational base fixture and its independently perturbed coefficient records only if its coefficient/root geometry is specified before execution. Report ideal-vs-represented topology separately. Do not describe the original N2 result as a general ULP robustness envelope.

### 3.3 Variable-scale block confounds solver behavior with non-covariant test geometry

The current `_domain_for` sets a margin with a unit lower bound:
`max(1, |low|/10, |high|/10)`.
The current variable-scale records also retain an absolute `max_width=10^-12`. Neither setting transforms with the variable coordinate.

**Required amendment:** split N3 into two explicit lanes:
- **N3-FIXED:** retain the historical absolute domain margin and absolute width. This measures the existing fixed-absolute interface contract.
- **N3-COVARIANT:** derive the transformed domain by multiplying both base-domain endpoints by (2^k), and transform the requested interval width by (2^k). Keep depth fixed and declared. Map all returned intervals back by exact multiplication by (2^{-k}) before comparison.

For every scale, record the ideal and actual represented polynomial, transformed domain, transformed width, inverse-mapped intervals, coefficient representability and topology comparison. Do not combine the two lanes into one equivariance score.

Amplitude scaling remains a distinct control: roots and domain do not change; only coefficients scale.

### 3.4 N5 mixes root-magnitude and representational effects

The large-magnitude fixture ((2^{120},2^{120}+1)) is not merely a difficult interval-isolation case. Its binary64 coefficient representation may have a different topology from the ideal rational polynomial.

**Required amendment:** preserve the existing N5 width/depth grid and all 60 historical outcomes as v001. In the successor, report ideal-vs-represented topology first, then classify the width/depth outcome conditional on the represented polynomial. Keep the full 60-record denominator and all abstentions.

### 3.5 N4 identifies a failure bracket, not its transition location

The current predeclared ladder passes through exponent 20 and fails at 50 and 100. It does not locate the scale transition more precisely. The current record also needs a layer-by-layer comparison to prevent the final adjudication status from obscuring which stage first becomes unresolved.

**Required amendment:** preserve the existing seven scales and add the fixed, non-adaptive intermediate exponent set:
`{24, 28, 32, 36, 40, 44, 48}`.
This gives a 14-scale deterministic ladder:
`{-100, -50, -20, 0, 20, 24, 28, 32, 36, 40, 44, 48, 50, 100}`.

For each scale, record separately:
- profile result/status and analytically adjusted log-likelihood error;
- MLE and LR endpoint inverse-scale errors;
- score-polynomial construction and degree;
- polynomial solver status, root count and inverse-scaled locations;
- independent Sturm status and isolating intervals;
- adjudication status/reason.

The intermediate grid is fixed before any further result is observed. No adaptive insertion, tolerance change or parameter tuning is permitted after execution. The observed transition may be reported only as a bracket between adjacent predeclared exponents, not as a continuous threshold estimate.

## 4. Required successor evidence schema

Every polynomial record must retain:
- immutable fixture ID and generator version;
- ideal coefficients and exact ideal roots;
- actual pre-conversion coefficients;
- binary64 hexadecimal coefficient vector, or explicit representation failure;
- exact rationalization of the binary64 vector;
- common domain and width/depth configuration;
- ideal-polynomial isolation result;
- represented-polynomial isolation result;
- ideal-vs-represented topology status and reason;
- F1 arbitrary-polynomial status fixed to `NOT_APPLICABLE`;
- runtime/provenance fields supplied by the execution manifest.

Every N3 record additionally retains lane (`FIXED` or `COVARIANT`), transformed domain, transformed width, inverse-mapped intervals and base-scale comparison.

Every N4 record retains the separate stage statuses above and an explicit transition bracket derived from the fixed ladder.

Summary denominators must include planned, generated, representable, ideal-resolved, represented-resolved, topology-preserved, topology-changed, topology-unresolved, solver-resolved, solver-abstained, and each N4 stage status. Publish full denominators by block and by lane. Never compute a headline agreement rate only over resolved cases without also publishing the full denominator and abstention rate.

## 5. Acceptance and interpretation rules

1. `PRESERVED` requires equal distinct-root counts and equal multiplicity structure in the common domain, with a unique interval/root correspondence under a predeclared exact-rational comparison rule.
2. `CHANGED` requires both ideal and represented exact-rational isolations to be complete and a demonstrated difference in root count or multiplicity structure. Location differences alone must be reported separately and compared under a predeclared exact rational tolerance/mapping rule.
3. `UNRESOLVED` applies if either isolation is incomplete, representation is lost, or correspondence is ambiguous.
4. A represented-polynomial `ROOTS_ISOLATED` result is not evidence that ideal topology was preserved.
5. Fixed and covariant N3 lanes answer different questions and must never be pooled.
6. N4 transition localization is bounded by adjacent tested exponents; no interpolation or post-hoc threshold claim.
7. All prior 122 outcomes remain immutable and are reported as the historical v001 baseline.
8. No result in this workstream establishes C10 causal attribution, (Delta T_{acc}	oDelta V), Monte Carlo calibration, inferential coverage or a general TGCV claim.

## 6. Implementation and governance sequence

1. Approve this design review as the successor requirements baseline.
2. Implement a new generator/harness version on the research branch. Keep the v001 generator and frozen source unchanged.
3. Perform static review of the diff, fixture roster, denominators, domain/width transformations, status semantics and evidence schema.
4. Create a new freeze manifest with exact source/blob identities and runtime pins.
5. Prepare a new one-shot authorization. It must bind the new source snapshot, exact workflow identity, 14-scale N4 ladder, N3 lane definitions, record counts, command, runtime, timeout, outputs and prohibitions.
6. Obtain fresh explicit approval before any new numerical execution.

No tests, numerical runners, calibration or scientific experiment are authorized by this review. Authorization 003 remains consumed and closed.

## 7. Current disposition

| Gate | State |
|---|---|
| Historical 73/73 software tests | PASS — historical result |
| Deterministic stress run v001 | EXECUTED — 122 records |
| v001 execution integrity | PASS |
| v001 numerical robustness | MIXED / NOT ESTABLISHED |
| Ideal-vs-represented topology audit | OPEN |
| N3 fixed/covariant separation | OPEN |
| N4 transition localization | OPEN |
| Successor implementation | NOT STARTED |
| New freeze and authorization | NOT PREPARED |
| Further numerical execution | NOT AUTHORIZED |

**Next operation:** implement the successor generator/harness from these requirements, preserving the v001 source, records and results unchanged.
