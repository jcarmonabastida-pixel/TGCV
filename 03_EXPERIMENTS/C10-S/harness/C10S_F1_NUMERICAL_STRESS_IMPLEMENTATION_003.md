# C10-S F1 — Numerical Stress v003 implementation and static review

**Status:** IMPLEMENTED — STATIC REVIEW ONLY — NOT EXECUTED  
**Design:** `C10S_F1_NUMERICAL_STRESS_DESIGN_003.md`  
**Research branch:** `research/c10s-f1-integrated-correction-20261119`

## 1. Implemented artifacts

| Artifact | Role |
|---|---|
| `C10S_F1_N4_V002_FROZEN_INPUTS_001.json` | Immutable 14-record N4 input subset extracted from v002 artifact |
| `c10s_f1_numerical_stress_v3.py` | Three deterministic diagnostic lanes |
| `run_c10s_f1_numerical_stress_v3.py` | CLI, denominator enforcement, JSONL/summary/manifest writer |

Frozen historical sources are imported read-only:
- v001 fixture generator and exact-rational isolator;
- v002 topology annotation and exact root-product helper;
- independent exact-rational Sturm isolator.

No v001/v002 source, result, manifest or artifact was modified.

## 2. Frozen N4 input provenance

The N4 fixture file contains exactly the 14 records selected from the v002 primary artifact:

- v002 source commit: `a42351e374e3624a498b11199cea45cd0dc20c09`;
- workflow run: `44545538187`;
- artifact ID: `14541730681`;
- source file: `numerical_stress_v2_records.jsonl`;
- source JSONL SHA-256: `b350693e3e8f492ccb179631a703c45a6af45d661b21a033f280c0546fcc9a26`.

Only the recorded exponent, exact binary64 coefficient hex vector, F1 root estimate in base variance units and v002 Sturm/adjudication statuses are retained. No profile likelihood, score polynomial or v002 root-isolation computation is rerun by the N4 lane.

## 3. Static implementation review

### N2 discriminant-proximity ULP lane

- Four predeclared gaps: (2^{-28},2^{-32},2^{-36},2^{-40}).
- Four coefficients perturbed independently by (-2,-1,+1,+2) binary64 steps.
- Fixed denominator: 64.
- Exact ideal and represented cubic discriminants are recorded.
- Existing v002 exact-rational topology annotator is reused.
- No random sampling or adaptive fixture selection.

### N5 coefficient-rounding-cell lane

- Reconstructs the existing (N=2^{120}) quadratic and its binary64 vector.
- Derives exact adjacent-float midpoints and ties-to-even endpoint closure.
- Computes a conservative rational interval enclosure of (b^2-4ac).
- Records exact ideal/represented discriminants, coefficient errors, root counts and multiplicities.
- The interval classifier is deliberately conservative: if the enclosure contains zero, it reports uncertainty; it does not claim that both topologies have been attained.

### N4 Fujiwara-bound lane

- Reads exactly 14 frozen v002 inputs.
- Reconstructs each coefficient exactly from its stored binary64 hexadecimal representation.
- Computes the existing exact Cauchy bound and an outward-rounded integer Fujiwara bound using rational/integer arithmetic.
- Computes an explicitly labelled approximate midpoint depth budget; this is not misrepresented as an actual subdivision trace.
- Invokes the unchanged exact-rational isolator with the same coefficients, width (10^{-12}), depth 256 and explicit Fujiwara upper endpoint.
- Compares that result with the already-recorded v002 Cauchy-domain status; it does not rerun the Cauchy baseline.

### CLI and evidence contract

- Requires a full lowercase 40-character source commit.
- Enforces 64 + 1 + 14 = 79 records.
- Writes JSONL, summary and a manifest with source/input/output SHA-256 values and runtime provenance.
- No random source, network access, external dataset, Monte Carlo, DGP or inferential-coverage operation is present in the authored implementation.

## 4. Static-review findings and limitations

**Static disposition: CONDITIONAL — SOURCE REVIEW RECORDED, NOT VALIDATED.**

1. The implementation imports private helpers from frozen v001/v002 modules. Their exact blob identities must be pinned in the future freeze manifest; any upstream change invalidates that freeze.
2. The N5 interval enclosure is conservative and may return UNCERTAIN when the exact rounding-cell set has a narrower topology range. This is a safe loss of power, not a false certification.
3. The N4 midpoint-depth estimate is a scale diagnostic only. It does not establish that max-depth exhaustion caused the v002 abstention. The explicit Fujiwara-bound isolation comparison is the discriminating operation.
4. No test, import, compilation, CLI invocation, numerical function, or scientific experiment has been executed for v003.
5. Because the implementation has not been run, syntax/runtime compatibility, record generation, exact denominator completion and numerical outcomes remain UNVERIFIED.

## 5. Operational provenance note

The first attempt to create the v003 generator omitted the explicit research-branch argument and briefly placed a commit on `main`. The branch pointer was immediately restored with an expected-head lease to its exact prior SHA `e22928eb79adb5bc74295967a45b9c440b78f849`. The final `main` pointer was re-read and matched that SHA; the v003 file is present only on the research branch. No net change to canonical `main` remains.

## 6. Execution boundary

- v003 design: DEFINED.
- v003 implementation: IMPLEMENTED.
- source-level review: CONDITIONAL.
- imports/compilation/tests: NOT EXECUTED.
- numerical diagnostic: NOT EXECUTED.
- source freeze: PENDING.
- workflow and one-shot authorization: PENDING.
- fresh explicit approval: REQUIRED before any numerical execution.
- replay, Monte Carlo calibration and scientific C10-S execution: NOT AUTHORIZED.

The next operation is a complete source-level reconciliation, then a freeze manifest and a dedicated workflow/authorization draft. No execution is implied by this implementation record.
