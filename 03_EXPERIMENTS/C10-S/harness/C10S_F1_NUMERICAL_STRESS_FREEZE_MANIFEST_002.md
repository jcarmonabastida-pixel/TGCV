# C10-S F1 — Numerical Stress Freeze Manifest 002

**Status:** SOURCE SNAPSHOT FROZEN — EXECUTION NOT AUTHORIZED  
**Research branch:** research/c10s-f1-integrated-correction-20261119  
**Frozen source commit:** f19ae92bed172f502cceb89fd26e86b5e37c5227  
**Supersedes:** Numerical Stress Freeze Manifest 001 (its source commit predates the final provenance dependency inventory)  
**Validated F1 baseline:** d65686beb2b242c0acb8ffbbcfe8ff55437f6c8b  
**Scope:** deterministic adversarial numerical characterization of the independent Sturm isolator and the existing data-derived F1 → Sturm → adjudication pipeline.

## 1. Freeze rule

The source snapshot is the exact commit above. Any future validation must check out this commit in detached mode and verify every Git blob identity in §3 before importing or invoking the harness.

This manifest freezes software and protocol identity only. It does **not** authorize execution, tests, calibration, DGP work or scientific C10-S execution. Any source/protocol change requires a new freeze snapshot and a new one-shot authorization.

Manifest 001 is retained as historical evidence. Manifest 002 supersedes it because the evidence writer's source-hash inventory was expanded to include the transitive F1 observed-data interface module.

## 2. Frozen design and denominators

### Polynomial/Sturm lane

- N1: 20 fixtures — progressive root separation, close pair plus negative root, double-plus-simple and triple-root cases.
- N2: 16 fixtures — each of four nonzero coefficients independently perturbed by ±1 and ±2 ULP.
- N3: 14 fixtures — amplitude and variable scaling at exponents −500, −200, −50, 0, 50, 200 and 500.
- N5: 4 fixtures × 3 widths × 5 depths = 60 records — unit-scale, near-zero, large-magnitude and exact finite upper-endpoint cases.
- N6: 5 fixtures — zero and endpoint roots, degree-one, nonzero constant and identically-zero cases.

**Total:** 59 base fixtures and 115 planned polynomial/Sturm records.

### F1 end-to-end lane

Seven predeclared observation-scale factors 2^k, where k ∈ {−100,−50,−20,0,20,50,100}. Variance coordinates, including nuisance-score roots, are mapped back using 2^(−2k).

Predeclared equivariance tolerances, compared with the k=0 baseline:
- profile log-likelihood absolute error: 10⁻⁷;
- MLE in base variance units: 10⁻¹⁰;
- each LR endpoint in base variance units: 10⁻⁸;
- maximum relative location error for inverse-scaled polynomial roots: 10⁻⁷.

The F1 baseline must itself have status POLYNOMIAL_ROOTS_ISOLATED and adjudication ROOTS_AGREE; otherwise scale equivariance is classified UNRESOLVED_BASELINE, never PASS.

### Explicit interface boundary

The existing F1 API does not accept arbitrary polynomial coefficient vectors. Therefore N1–N3 and N5–N6 characterize exact-rational Sturm behavior and coefficient representation, not generic F1/Sturm concordance. N4 is the data-derived F1 end-to-end lane. No arbitrary-polynomial F1 agreement rate is claimed.

## 3. Frozen Git blob inventory

Git blob SHAs:

| Role | Path | Git blob SHA |
|---|---|---|
| Stress fixture generator, runners and evidence writer | 03_EXPERIMENTS/C10-S/harness/c10s_f1_numerical_stress.py | 80ff414e076b06de14ea1190dd9e877b6045b88f |
| Explicit CLI runner | 03_EXPERIMENTS/C10-S/harness/run_c10s_f1_numerical_stress.py | b08ee28a1423b7a6c598db69c0ef15dff5f0ac22 |
| F1 solver | 03_EXPERIMENTS/C10-S/harness/c10s_f1_between_profile_likelihood.py | 39f1732e1571f9d0705378d924b58b9475277e7a |
| Independent exact-rational Sturm isolator | 03_EXPERIMENTS/C10-S/harness/c10s_f1_independent_root_isolator.py | 3ac9ce31eb82421022fd8d2a65a0daee049322be |
| F1/Sturm adjudicator | 03_EXPERIMENTS/C10-S/harness/c10s_f1_root_adjudication.py | 9fa1cb21cd47e32030db8a00420e7dacfdc77321 |
| Transitive observed-data interface | 03_EXPERIMENTS/C10-S/harness/c10s_variance_comparison_interface.py | 6d193798e792dd5129fbfb0c312286763791d463 |

The evidence writer hashes all five Python source modules listed above. The CLI is separately frozen and hash-checked by the workflow.

The three validated F1/Sturm/adjudication modules and the observed-data interface are byte-identical to the corresponding source blobs in frozen validation commit d65686be....

## 4. Runtime proposal

Reuse the exact successful integrated-validation runtime to minimize avoidable environmental differences:

- GitHub-hosted ubuntu-24.04;
- CPython 3.12.3;
- NumPy 2.1.3;
- SciPy 1.14.1;
- isolated virtual environment;
- only the pinned NumPy and SciPy binary wheels, installed with --no-deps.

This is a proposed execution environment, not evidence that the stress harness has run there. The actual workflow must verify all versions and source hashes before execution.

## 5. Exact intended command

Working directory: 03_EXPERIMENTS/C10-S/harness

    python run_c10s_f1_numerical_stress.py \
      --source-commit f19ae92bed172f502cceb89fd26e86b5e37c5227 \
      --output-directory "$RUNNER_TEMP/c10s-f1-numerical-stress-evidence"

The CLI invokes each deterministic runner once and passes the returned records to the explicit evidence writer. Importing either module does not execute the runners.

The evidence writer produces:
- numerical_stress_records.jsonl — one canonical JSON record per fixture/scale;
- numerical_stress_summary.json — planned/generated/representable/resolved/unresolved and equivariance denominators;
- numerical_stress_manifest.json — source-file SHA-256 values, runtime versions, and hashes of the records and summary.

The writer rejects non-finite JSON values and requires a full 40-character source commit identity. Workflow-level stdout/stderr, exit code, artifact identity and GitHub run provenance must be captured separately.

## 6. Execution limits and exclusions

Proposed resource boundary for a future authorization:
- one primary execution only;
- 115 polynomial/Sturm records and 7 F1 scale records;
- no random fixtures or adaptive post-outcome parameter changes;
- GitHub-hosted job timeout: 15 minutes;
- no replay unless separately authorized after the primary integrity audit.

Explicit exclusions:
- no unit tests or broad test suite;
- no Monte Carlo calibration;
- no DGP experiment or inferential coverage study;
- no parameter tuning;
- no external dataset;
- no modification of the frozen source during execution;
- no scientific C10-S execution or causal/value claim.

The exact runner command and environment above are proposed for authorization. They are not permission to execute.

## 7. Current gate status

| Gate | State |
|---|---|
| Historical integrated deterministic tests | PASS — 73/73 on the separate frozen baseline |
| Adversarial protocol | DEFINED |
| Generator and harness | IMPLEMENTED |
| N4 equivariance checks | IMPLEMENTED — NOT EXECUTED |
| N5 magnitude/depth ladder | IMPLEMENTED — NOT EXECUTED |
| JSONL/summary/hash writer | IMPLEMENTED — NOT EXECUTED |
| Frozen source and blob identities | FROZEN |
| Execution workflow for this stress gate | NOT YET CREATED |
| One-shot numerical stress authorization | NOT APPROVED |
| Numerical stress execution | NOT AUTHORIZED |
| Monte Carlo / scientific C10-S execution | NOT AUTHORIZED |

**Next operation:** create a manual GitHub Actions workflow that checks this exact freeze and fails closed unless a separate one-shot authorization matches the frozen commit, blob identities, command, runtime and limits. The workflow must not be dispatched until that authorization is explicitly approved.
