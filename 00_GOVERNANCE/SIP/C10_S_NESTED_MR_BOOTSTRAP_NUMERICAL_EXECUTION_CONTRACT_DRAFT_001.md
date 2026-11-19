# C10-S — Nested M/R numerical validation execution contract

**ID:** C10S-NESTED-MR-EXECUTION-CONTRACT-001  
**Version:** 001  
**Date:** 2026-11-18  
**Status:** IMPLEMENTED_FOR_REVIEW / NOT_AUTHORIZED / NOT_EXECUTED  
**Governing protocol:** `C10S-NESTED-MR-BOOTSTRAP-VALIDATION-001`, version 002  
**Method:** `TGCV_NESTED_MR_BOOTSTRAP`, version 1.2  
**Repository line:** `research/c10-s-consolidation-draft`  
**Scope:** isolated scalar-fixture validation of the balanced, unpaired nested M/R estimator and bootstrap.

## 1. Purpose and separation

This contract binds the frozen protocol to a deterministic fixture generator, the existing nested M/R estimator, a cell-level evaluator, an execution controller and a fail-closed remote workflow.

It validates only the numerical method. It must not invoke or import the C10-S scientific Generator, Analyzer, Evaluator, DGP, calibration runner, calibration/evaluation banks, seed-bank builder, or scientific workflows. It creates no C10-S scientific evidence and cannot be consumed as Analyzer performance evidence.

The actual C10-S outer-world and conditional assignment sampling mechanisms are not validated by these synthetic fixture contracts.

## 2. Integrated implementation

| Component | Artifact | Responsibility |
|---|---|---|
| Fixture generator | `c10s_nested_mr_fixtures.py` | Six analytical fixture families, exact truths, deterministic independent seed namespaces and versioned M/R fixture contracts |
| Numerical estimator | `theta_a_nested_mc_precision.py` | Existing method 1.2, using bounded-memory vectorized batches for the same two-stage cluster-bootstrap law |
| Validation runner/evaluator | `run_c10s_nested_mr_validation.py` | Executes each frozen cell, reconciles estimates/intervals with independent analytical truths, computes coverage/Wilson/MCSE and diagnostics |
| Authorization validator | `validate_c10s_nested_mr_execution_authorization.py` | Requires a separate approved authorization commit, exact code parent, protocol hash, tier/K/B, branch and expiry |
| Software tests | `test_c10s_nested_mr_validation.py` plus existing nested precision tests | Checks fixture truth contracts, schedule determinism, cell counts, coverage adjudication and deterministic degeneracy guards |
| Remote controller | `.github/workflows/c10-s-nested-mr-numerical-validation.yml` | Runs only after a dedicated authorization-manifest commit; uploads immutable run artifacts |

The bootstrap implementation is vectorized in batches of 64 using explicitly pinned NumPy PCG64 child streams for outer-cluster and inner-R resampling. The fixture generator is version 1.1: its dataset seed is split through `SeedSequence.spawn(2)` into an outer-world stream and an inner stream; the inner stream is itself split into one independent R stream per world. The bootstrap seed is independently split into outer and inner bootstrap streams. The root dataset and bootstrap seeds remain separate SHA-256-derived namespaces. It retains all outer cluster draws, including all-same-source draws, and resamples R independently within every selected cluster copy. The estimator, raw component definitions, projection formula, legacy observed-MCSE reconciliation, 95% percentile interval and boundary abstention semantics remain those of method version 1.2. The optimization changes execution mechanics and deterministic stream implementation, not the frozen statistical resampling law. There are no prior numerical outputs whose seed stream would need migration.

## 3. Frozen fixture inventory

### 3.1 Tier A — regular-cell coverage

Eight cells, each with K=1,000 independent datasets and B=1,000 bootstrap draws per dataset:

| Family | Parameters | Designs | Cells |
|---|---|---|---:|
| F1 Gaussian | balanced (1,1), low-between (within 1, between .05), high-between (within .25, between 2) | (10,5), (30,20) | 6 |
| F5 beta-binomial | world probability Beta(2,2); within truth .20, between truth .05 | (10,5), (30,20) | 2 |

The component intervals are adjudicated separately for within and raw between. Projected MCSE coverage is reported separately, and cannot pass unless availability is at least 95%.

### 3.2 Tier B — boundary and support diagnostics

Twenty stochastic cells, each K=500 and B=500:

- F1 balanced and low-between at (3,2), (10,5), and the M=2 negative control (2,2): 6 cells.
- F2 exact-zero and near-zero between at (3,2) and (10,5): 4 cells.
- F3 within-zero at (3,2) and (10,5): 2 cells.
- F5 constant p=.5 and rare p=.01 at (3,2) and (10,5): 4 cells.
- F6 positive MSE scales 1 and 1e-8 at (3,2) and (10,5): 4 cells.

Four deterministic controls are evaluated once as direct invariants, outside K/B: F4 all-zero, F5 p=0, F5 p=1, and F6 exact-zero MSE. They must demonstrate explicit bootstrap degeneracy or the exact `RMSE_DELTA_NONREGULAR` guard and must not claim regular precision.

No additional cell, seed, K, B, interval level or acceptance threshold is permitted without a versioned amendment made before examining results.

## 4. Truth oracles and evaluator outputs

The fixture generator and evaluator keep analytical truth separate from the estimator output.

- Gaussian random-intercept fixtures: `Var(U)=sigma2_between`; `Var(E)=sigma2_within`.
- Beta-binomial Beta(2,2): `E[p(1-p)]=0.20`; `Var(p)=0.05`.
- Constant Bernoulli p: within `p(1-p)`; between 0.
- F3: within 0; between 1.
- F4: both components 0.
- F6 with squared Normal errors at scale s: MSE contribution mean s and within variance `2*s^2`; between 0. Exact-zero scale has both components 0.

For each dataset the runner records the analytical truths, component point estimates, raw between estimate, percentile intervals, projected MCSE interval/status, independently calculated legacy observed MCSE and its reconciliation, boundary fraction, B/valid-B counts, seeds, fixture identity, code commit and protocol hash.

Tier A cell adjudication follows protocol §9.5 exactly:
- empirical 95% coverage in [0.93, 0.97];
- 95% Wilson interval contains 0.95;
- both conditions must pass for each component separately;
- projected MCSE additionally requires at least 95% availability.

Tier B reports diagnostic counts, finite arithmetic, full B retention, raw-negative frequency, boundary frequency and correct M=2 abstention. It does not apply a nominal coverage pass.

No global average can rescue a failed cell.

## 5. Deterministic seed schedule

Seed schedule: `C10S_NESTED_MR_SEED_SCHEDULE_1.0`.

Each seed is the unsigned 64-bit integer represented by the first eight bytes of SHA-256 over:

`version | namespace | cell_id | replicate_index`

The two namespaces are exactly:
- `fixture_dataset`
- `bootstrap`

The seed is independent of iteration order, runner identity and workflow attempt. Both fixture and bootstrap draws use explicitly selected PCG64 child streams. Re-running a cell under the same code/protocol/schedule, fixture-generator version 1.1 and pinned NumPy dependency reproduces the same generated dataset and bootstrap stream. M and R are not paired across cells or N; no coupling is inferred from row order, IDs or coincident seeds.

## 6. Computational resource estimate

The estimator uses NumPy, already present in the hash-locked harness dependency file. Bootstrap draws are generated in batches of 64; the largest temporary nested-value block is 64×30×20 float64 values (approximately 0.30 MiB), plus index and summary arrays. This bounds working memory independently of K.

Exact scalar contribution-resampling workload implied by the frozen cells:

| Tier | Bootstrap replicates | Resampled q values | Outer cluster selections |
|---|---:|---:|---:|
| A | 8,000,000 | 2,600,000,000 | 160,000,000 |
| B | 5,000,000 | 128,000,000 | 30,250,000 |
| Total, if both tiers are separately authorized | 13,000,000 | 2,728,000,000 | 190,250,000 |

These are operation counts, not measured wall-clock estimates. No benchmark has been run. The remote job is bounded to one tier per run on `ubuntu-24.04`, CPython 3.12.10, with a hard 360-minute timeout. If the tier does not complete within the limit, it is BLOCKED; K/B, cells, seeds and acceptance criteria must not be reduced to make it pass. Any resource-driven change requires a prospective protocol amendment.

## 7. Remote execution and authorization gate

No authorization manifest currently exists. The workflow therefore has no route to execute the numerical tier at present.

A future execution requires a dedicated branch named:

`research/c10s-nested-mr-auth-<authorization-id>`

That branch must start at the exact reviewed code commit and contain exactly one new/changed file:

`00_GOVERNANCE/authorizations/C10S_NESTED_MR_NUMERICAL_EXECUTION_AUTHORIZATION.json`

The authorization record must include:
- schema `TGCV-C10S-NESTED-MR-EXECUTION-AUTH-001`;
- status `APPROVED` and non-empty authorization ID;
- approver and approval timestamp;
- expiry in UTC;
- exact protocol ID/version and SHA-256;
- exact approved code commit;
- method ID/version;
- tier A or B, exact K/B;
- seed-schedule version;
- exact authorization branch;
- optional prior workflow run ID for checkpoint resumption.

The validator requires the authorization commit's sole parent to equal `approved_code_commit`, verifies that only the authorization file changed, checks the exact protocol SHA-256 and rejects expired/mismatched authorization. The runner repeats the critical protocol/code/tier/K/B checks.

The workflow listens only for a push to a dedicated numerical-auth branch that changes the authorization manifest. Ordinary code commits, static-test workflows and PR updates cannot start numerical validation. Tier A and Tier B require separate authorization records and separate runs.

**The user's request to construct this component is not execution authorization.** No authorization record is being created by this contract.

## 8. Checkpoint, restart and artifact integrity

Each cell writes to a temporary JSONL file and is promoted atomically only after all K records are complete. After each completed cell, the runner atomically updates `checkpoint_index.json` with the cell identity, K/B, code commit, protocol hash, seed-schedule version, record SHA-256 and summary SHA-256. A completed cell can be reused only when:
- code commit and protocol SHA-256 match;
- cell identity, K and B match;
- record count equals K;
- record-file SHA-256 matches the cell summary.

A partial temporary cell is restarted from replicate index zero with the same deterministic seeds. For a new workflow attempt, the authorization may identify a previous run whose artifact is downloaded; completed cell files are reused only after the same integrity checks. Missing or mismatched checkpoints are not silently accepted.

Outputs:
- one JSONL record file per cell;
- one atomic `checkpoint_index.json` enabling verified cell-level restart;
- one JSON summary per cell;
- deterministic-guard report for Tier B;
- run manifest with source hashes, runtime, authorization, code commit and per-cell results;
- `SHA256SUMS.txt` covering every output except itself.

Artifacts are uploaded even on failure where the runner has produced partial outputs. The workflow must never convert timeout, missing artifact, invalid hash, incomplete cell or failed guard into PASS.

## 9. Software-only preflight and execution boundary

The existing static workflow is extended to compile and test the fixture generator, runner, authorization validator and estimator. This is software-contract validation only. It does not invoke the frozen Tier A/B runner.

The numerical workflow is not dispatched during implementation or static testing. No fixture dataset, K/B loop, numerical coverage study, calibration, scientific DGP, Generator, Analyzer, Evaluator or C10-S workflow is run as part of this construction.

## 10. Current disposition and next gate

**IMPLEMENTED_FOR_REVIEW / NOT_AUTHORIZED / NOT_EXECUTED.**

Before numerical execution:
1. review the integrated source and its static CI evidence;
2. review the exact resource and restart contract;
3. resolve any implementation/test discrepancy without changing protocol v002;
4. freeze the final code commit and protocol hash;
5. obtain explicit authorization for one tier;
6. create the separate authorization branch/manifest only after that authorization.

The result can establish bounded numerical-method evidence only. It cannot establish Analyzer causal recovery, C10 attribution, `Delta T_acc → Delta V`, Value causality, or confirmatory status.
