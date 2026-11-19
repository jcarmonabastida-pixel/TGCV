# C10-S F1 — Numerical Stress v002 primary execution result

**Primary execution:** PASS — command completed with exit code 0  
**Numerical robustness outcome:** MIXED — material topology loss and scale-dependent abstention observed  
**Final execution-result audit:** INDETERMINATE — replay was explicitly prohibited by authorization 004  
**Scientific C10-S execution:** NOT PERFORMED  
**Research branch:** `research/c10s-f1-integrated-correction-20261119`

## 1. Execution provenance

| Item | Value |
|---|---|
| Authorization | `C10S-F1-NUMERICAL-STRESS-20261119-004` |
| Authorization commit | `e743276c9658d2c7d16105a91d88a1c5d4ffaa88` |
| Workflow run | `44545538187` |
| Workflow attempt | 1 |
| Workflow conclusion | `success` |
| Frozen source commit | `a42351e374e3624a498b11199cea45cd0dc20c09` |
| Runtime | CPython 3.12.3 / NumPy 2.1.3 / SciPy 1.14.1 |
| Runner | ubuntu-24.04, x86_64 |
| Exact command | `python run_c10s_f1_numerical_stress_v2.py --source-commit a42351e374e3624a498b11199cea45cd0dc20c09 --output-directory "$RUNNER_TEMP/c10s-f1-numerical-stress-v2-evidence"` |
| Runner exit code | 0 |
| stderr | Empty |
| Record count | 152 |
| Artifact ID | `14541730681` |
| Artifact ZIP SHA-256 | `f8acbc8e5a18c148aaacc5589d831807c5c2b7eea7d5f45d5e0a57ab9a8cc648` |

The workflow passed authorization, source commit, source blob, manifest blob, runtime, command and scope preflight checks. It consumed authorization 004 immediately before the single numerical invocation. The authorization is not reusable.

## 2. Artifact integrity audit

All 152 JSONL lines parse as JSON. All 152 lines are unique. Lane denominators match the predeclared scope exactly:

| Lane | Expected | Observed |
|---|---:|---:|
| POLYNOMIAL_STURM_V2 | 131 | 131 |
| N3_COVARIANT_V2 | 7 | 7 |
| F1_N4_V2 | 14 | 14 |
| **Total** | **152** | **152** |

The artifact manifest's records and summary SHA-256 values independently match the extracted files:

- Records JSONL: `b350693e3e8f492ccb179631a703c45a6af45d661b21a033f280c0546fcc9a26`
- Summary JSON: `ac3837e0240a788fad3701543904dc699f5e40b5dee9d2e8b9b34355bac4faca`
- Manifest JSON: `60308d6162847616c826484c69776afc68cc9e3ae03ee2be70716c4338c8d726`

The records and summary hashes match the manifest. No malformed JSONL records, denominator drift, stderr output or nonzero runner exit were observed.

## 3. Numerical findings

### 3.1 Polynomial/Sturm lane — 131 records

Observed statuses:

- 70 `ROOTS_ISOLATED`;
- 57 `ROOTS_UNRESOLVED`;
- 2 `REPRESENTATION_UNRESOLVED`;
- 1 `NO_ROOTS_CONSTANT_POLYNOMIAL`;
- 1 `IDENTICALLY_ZERO_POLYNOMIAL_UNRESOLVED`.

Ideal-versus-binary64 topology comparison:

- 63 `PRESERVED`;
- 3 `CHANGED`;
- 65 `UNRESOLVED`.

The 16 dedicated near-double-root ULP records (`N2_NEAR_DOUBLE`, roots `-2`, `1`, and `1 + 2^-24`, with ±1/±2 ULP perturbations to each of four coefficients) all preserved the distinct-root count and ordered multiplicity structure: **16/16 PRESERVED**. This establishes topology preservation for this particular perturbation grid, not general ULP robustness.

A separate material topology-loss result appears in three configurations of `N5_CLOSE_PAIR_LARGE_MAGNITUDE`. The ideal polynomial has two distinct simple roots at (N) and (N+1), with (N=2^{120}). The exact rationalization of the binary64 coefficient vector instead has one double root at (N). The binary64 conversions are finite, but the coefficients are not exactly preserved: the (N(N+1)) and (-(2N+1)) coefficients round to (N^2) and (-2N). The represented polynomial therefore becomes ((x-N)^2).

The three `CHANGED` rows are the same underlying fixture at three requested isolation widths with depth 256; they are not three independent polynomial fixtures. This is a direct counterexample to topology preservation under finite binary64 conversion at extreme coefficient/root scale.

**Schema caveat:** the field `binary64_representable` means that conversion produced finite binary64 values; it does not mean the rational coefficients were exactly representable. Exact converted coefficients are separately recorded in `exact_binary64_coefficients`.

The 65 unresolved topology comparisons are not counted as preserved or changed. They remain in the denominator.

### 3.2 N3 covariant scale lane — 7 records

- 5/7 `ROOTS_ISOLATED`, topology `PRESERVED`, and inverse-mapped interval equivariance `PASS`;
- 2/7 `REPRESENTATION_UNRESOLVED` at exponents -500 and +500, because a finite binary64 coefficient vector could not be formed.

The two extreme-scale cases are explicit unresolved representation outcomes, not successful equivariance cases. No denominator reduction was applied.

### 3.3 F1 N4 observation-scale lane — 14 records

All 14 profile computations returned `PROFILE_LR_INTERVAL_ROOT_SOLVED`; all 14 score polynomials were isolated and retained degree 3 with one F1 root.

Independent Sturm/adjudication outcomes:

- 9/14 `ROOTS_ISOLATED` and `ROOTS_AGREE`;
- 5/14 `ROOTS_UNRESOLVED` and `ROOTS_UNRESOLVED` adjudication;
- 9/14 equivariance `PASS`;
- 5/14 equivariance `FAIL`.

The tested transition bracket is:

`36 < exponent_transition <= 40`

At exponent 36 the independent Sturm reference isolates the root and adjudication agrees. At exponent 40 and the higher tested exponents (44, 48, 50, 100), the independent Sturm reference abstains; the F1 profile/score solver still returns a root. Adjudication correctly refuses to claim agreement without the independent reference. The five cases remain failures of the strict equivariance/adjudication gate, not missing data.

The bracket is limited to the tested exponent grid; it is not a precise numerical threshold.

## 4. Interpretation and limits

This execution does **not** support a blanket statement that F1/Sturm is robust to adversarial numerical perturbations.

It demonstrates three distinct behaviors:

1. **ULP perturbation stability in the tested near-double fixture:** all 16 perturbations preserve the root topology.
2. **Finite-conversion topology failure at extreme coefficient scale:** the N5 fixture changes from two distinct simple roots to one double root after binary64 rounding.
3. **Scale-dependent loss of independent isolation:** N4 remains solvable by the profile/score path while the independent Sturm reference begins to abstain between exponents 36 and 40.

N3 additionally shows that sufficiently extreme covariant scaling can prevent finite binary64 representation altogether.

The proper conclusion is **MIXED / BOUNDED**, with an explicit counterexample and defined abstention regions. The 65 unresolved polynomial comparisons and five N4 adjudication failures must not be pooled into a PASS rate or silently excluded.

## 5. Gate disposition

| Gate | Result |
|---|---|
| Authorization and preflight | PASS |
| Frozen source identity | PASS |
| Single primary execution | PASS |
| Expected 152-record denominator | PASS |
| Artifact JSON/JSONL integrity | PASS |
| Artifact SHA-256 cross-check | PASS |
| Near-double ULP topology grid | 16/16 PRESERVED |
| N5 finite-conversion topology preservation | FAIL — 3 configurations CHANGED |
| N3 covariant equivariance | 5 PASS / 2 UNRESOLVED |
| N4 F1/Sturm equivariance | 9 PASS / 5 FAIL |
| Overall numerical robustness | MIXED / BOUNDED |
| Replay | NOT AUTHORIZED; NOT PERFORMED |
| Final execution-result audit | INDETERMINATE pending replay or an explicit governance decision that waives it |
| Monte Carlo calibration | NOT AUTHORIZED; NOT PERFORMED |
| Scientific C10-S / causal inference | NOT PERFORMED |

## 6. Evidence files

GitHub Actions run:  
`https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44545538187`

Artifact:  
`https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44545538187/artifacts/14541730681`

The artifact contains:
- `numerical_stress_v2_records.jsonl`
- `numerical_stress_v2_summary.json`
- `numerical_stress_v2_manifest.json`
- `workflow-preflight.txt`
- `runner.stdout`
- `runner.stderr`
- `runner-exit-code.txt`

## 7. Next research operation

Do not modify the frozen v002 source or rerun authorization 004.

The next design task is a v003 diagnostic/reconciliation, not a rerun:
- investigate the N5 coefficient-rounding counterexample and define an explicit exactness/conditioning diagnostic before any binary64 conversion;
- preserve the 16/16 ULP result as bounded fixture evidence, while assessing whether a closer-to-discriminant-boundary perturbation grid is scientifically justified;
- characterize the N4 Sturm abstention mechanism within the observed 36–40 bracket without post-outcome threshold tuning;
- keep unresolved and representation-lost outcomes in all denominators.

Any new execution requires a new frozen source, workflow and one-shot authorization. No replay, calibration or scientific C10-S execution is authorized by this record.
