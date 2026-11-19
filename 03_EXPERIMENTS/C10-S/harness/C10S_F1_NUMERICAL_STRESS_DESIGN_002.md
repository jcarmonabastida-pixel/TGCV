# C10-S F1 — Deterministic numerical stress design 002

**Status:** IMPLEMENTED DESIGN — STATIC AUDIT PENDING — NOT FROZEN — EXECUTION NOT AUTHORIZED  
**Supersedes for future work:** design draft 001 only after explicit approval; result 001 remains immutable historical evidence  
**Generator:** `C10S_F1_NUMERICAL_STRESS_GENERATOR_002`  
**Research branch:** `research/c10s-f1-integrated-correction-20261119`

## 1. Objective

The v002 design separates three effects that v001 could not fully distinguish:

1. change in the mathematical root topology caused by converting ideal rational coefficients to binary64;
2. change in resolution caused by isolation width/depth and the choice of fixed versus scale-covariant domains;
3. loss of end-to-end F1 → Sturm → adjudication equivariance at extreme observation scales.

This remains a bounded deterministic numerical-characterization exercise. It does not establish arbitrary-polynomial F1 concordance, statistical calibration, inferential coverage, C10 causal attribution or a value claim.

## 2. Historical baseline retained

All 122 v001 records, the v001 source, result record, artifact and closed authorization 003 remain unchanged. The v002 generator reuses the v001 115-record polynomial/Sturm roster and adds separate diagnostics. No v001 result is overwritten or re-labelled.

## 3. Frozen v002 record roster

| Lane | Records | Construction |
|---|---:|---|
| Polynomial/Sturm | 131 | Historical 115 plus 16 near-double ULP records |
| N3 covariant | 7 | Variable-scale transformations with covariant domain and width |
| F1 N4 | 14 | Historical seven observation scales plus seven fixed intermediate exponents |
| **Total** | **152** | Deterministic; no random fixtures |

The 131 polynomial records retain the v001 N3 fixed-absolute lane. The additional seven N3 records are a separate covariant lane and must not be pooled with it.

### N2 near-double ULP family

Use the exact-rational roots:
`(1, 1 + 2^-24, -2)`.

For each nonzero coefficient of the resulting cubic, independently apply `-2, -1, +1, +2` adjacent binary64 representable steps using `math.nextafter`. This produces 16 additional records. The original N2 simple-cubic 16 records remain unchanged.

For each record preserve ideal coefficients, actual pre-conversion coefficients, binary64 hexadecimal values, exact rationalization, ideal and represented root isolations, and topology comparison. Perturbations are independent, not a combinatorial cross-product.

### Ideal-versus-represented topology

For each polynomial record, isolate:
- the ideal exact-rational coefficient vector; and
- the exact rationalization of the actual binary64 vector supplied to the isolator.

Use the same domain, width and depth. Report both root lists, intervals and multiplicities. The independent field `topology_comparison_status` is:
- `PRESERVED`: both isolations complete and ordered root count/multiplicity structure matches;
- `CHANGED`: both isolations complete and root count or multiplicity structure differs;
- `UNRESOLVED`: either isolation is incomplete or representation is lost.

This comparison is not F1-vs-Sturm adjudication. The F1 API does not accept arbitrary injected polynomials.

### N3 fixed and covariant lanes

- **N3 fixed:** the historical v001 absolute domain-margin and absolute-width configuration is retained in the 131-record polynomial roster.
- **N3 covariant:** for each (k\in\{-500,-200,-50,0,50,200,500\}), transform both domain endpoints and the requested isolation width by (2^k), keep depth 256, and inverse-map all returned intervals by exact (2^{-k}). Compare mapped intervals, root counts and multiplicities against the base-scale represented polynomial.

The N3 covariant records separately retain ideal and represented coefficients, binary64 representation, exact rationalization, transformed domain/width, ideal and represented Sturm roots, topology status, inverse-mapped intervals and base-equivalence status. Representation loss or incomplete isolation is unresolved, never PASS.

Amplitude scaling remains in the historical N3 fixed roster and is not combined with variable scaling.

### N4 fixed 14-scale observation ladder

Use the ordered, predeclared exponent set:
`{-100, -50, -20, 0, 20, 24, 28, 32, 36, 40, 44, 48, 50, 100}`.

For each exponent, record:
- profile status and maximum log-likelihood;
- MLE and LR endpoints inverse-mapped to base variance units;
- score-polynomial status, degree, binary64 coefficient hex values and exact rationalized coefficients;
- score roots inverse-mapped to base variance units;
- independent Sturm status, intervals, boundary roots and root count;
- F1 root count, matched root count and multiplicity-review flag;
- adjudication status and reason;
- each predeclared equivariance error and status.

Report a transition only as a bracket between adjacent tested exponents where both records returned and the relevant stage status changed. Do not bridge over a fail-closed record, interpolate a continuous threshold or adaptively insert exponents after observing results.

## 4. Acceptance and denominator rules

- Keep all 152 records, including representation failures, unresolved isolations and fail-closed F1 records.
- Publish planned/generated counts and representability, ideal-resolved, represented-resolved, topology-preserved/changed/unresolved, and Sturm-status denominators by lane.
- For N3 publish fixed and covariant lanes separately, including base-equivalence PASS/FAIL/UNRESOLVED.
- For N4 publish profile, score-polynomial, Sturm, adjudication, root-count and matched-root denominators; publish transition brackets and all unresolved exponents.
- Never interpret `ROOTS_ISOLATED` for the represented polynomial as proof that ideal topology was preserved.
- Never treat an abstention as a successful root recovery or discard it from the denominator.
- No threshold, tolerance, domain rule, fixture, scale exponent or root-matching rule may be changed after results are observed. Any amendment requires a new version, freeze and authorization.

## 5. Execution contract proposal

- Runner: GitHub-hosted `ubuntu-24.04`.
- Python: `3.12.3`.
- NumPy: `2.1.3`.
- SciPy: `1.14.1`.
- One primary execution; zero automatic retries; no replay.
- Timeout: 15 minutes.
- Exact CLI:
```bash
python run_c10s_f1_numerical_stress_v2.py \
  --source-commit <full-frozen-commit-sha> \
  --output-directory "$RUNNER_TEMP/c10s-f1-numerical-stress-v2-evidence"
```
- Outputs: `numerical_stress_v2_records.jsonl`, `numerical_stress_v2_summary.json`, `numerical_stress_v2_manifest.json`, plus workflow stdout/stderr, exit code and provenance.
- Explicit exclusions: no unit-test suite, Monte Carlo calibration, DGP experiment, inferential coverage study, parameter tuning, external dataset or scientific C10-S execution.

The runtime, command and scope are design proposals until pinned to the new freeze manifest and authorization.

## 6. Current gate state

| Gate | State |
|---|---|
| v001 historical result | EXECUTED — 122 records; mixed numerical result |
| v001 authorization 003 | CONSUMED AND CLOSED |
| v002 generator and CLI | IMPLEMENTED |
| v002 static code audit | PENDING |
| v002 deterministic fixture execution | NOT RUN |
| v002 software tests | NOT RUN |
| v002 freeze manifest | NOT PREPARED |
| v002 workflow | NOT PREPARED |
| v002 one-shot authorization | NOT PREPARED |
| v002 numerical execution | NOT AUTHORIZED |
| Monte Carlo / scientific C10-S | NOT AUTHORIZED |

**Next operation:** complete the static audit of the v002 source and evidence contract. After audit, freeze exact blobs, prepare a dedicated workflow and one-shot authorization, and request fresh explicit approval. Do not invoke the CLI before that approval.
