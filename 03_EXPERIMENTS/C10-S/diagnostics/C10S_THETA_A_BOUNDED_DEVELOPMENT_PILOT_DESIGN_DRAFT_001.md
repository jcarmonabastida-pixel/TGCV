# C10-S — Direct theta_A bounded development pilot design

**Record:** C10S-THETA-A-BOUNDED-DEVELOPMENT-PILOT-DESIGN-001  
**Version:** 0.1  
**Status:** SUPERSEDED DRAFT — SEE CORRECTION ADDENDUM AT END — NO EXECUTION AUTHORIZATION  
**Date:** 2026-11-27  
**Branch:** `research/c10s-m1-engine12-source-only-20261127`  
**Scope:** One bounded exploratory screen of the existing direct theta_A pipeline  
**Execution boundary:** No seeds generated, no DGP invoked, no tests or workflows run.

## 1. Purpose

Translate the accepted four-objective calibration plan into the smallest useful first development screen, reusing the existing direct pipeline:

`focal DGP → sealed evidence → direct theta_A Analyzer → independent Evaluator → calibration aggregator`.

The screen is intended to expose gross point-recovery, interval-availability, coverage-direction, and identification/abstention problems before any larger calibration design is considered. It is not a confirmatory experiment and cannot validate the interval, select final N/M/R, establish Monte Carlo precision, or support a causal claim.

This is the direct theta_A experiment. It is not the historical F1/F5 variance-component study, not the legacy 13×52 V_cont benchmark, and not P178 evidence transferred to a new estimand.

## 2. Reuse and historical constraints

Reuse, without rebuilding:
- the five-scenario roster from `build_theta_a_candidate_scenario_roster()`;
- the existing focal DGP and independent truth;
- the sealed evidence/observation harness;
- the direct theta_A Analyzer and independent Evaluator;
- the existing N×M×R seed-bank and aggregator contracts;
- the strict all-R denominator semantics and metric registry.

The five scenarios remain distinct:
1. positive focal truth (+0.5);
2. null focal truth (0);
3. negative focal truth (−0.5);
4. alternative active pathway with focal truth 0;
5. target-history support failure, expected NOT_IDENTIFIED.

Do not add stress scenarios, alter the estimand, or create another inference engine.

## 3. Proposed first screen

### 3.1 Candidate dimensions

| Dimension | Draft proposal | Status / interpretation |
|---|---:|---|
| N (units per world) | 700 | Candidate anchor only; previously explored in P178 as a diagnostic N, not calibrated for this direct theta_A pipeline |
| M (outer worlds) | 5 | Small descriptive outer sample; inadequate for a stable precision conclusion |
| R (joint assignment + S3 observation replicates per world) | 4 | Small within-world screen; no IID-within-R inference claimed |
| Scenarios | 5 existing scenarios | Full first-wave roster retained |
| Planned replicate records | 100 | 5 scenarios × 5 worlds × 4 R |
| Planned UE instances | 70,000 | 100 records × 700 UEs; a workload count, not an independence/effective-sample claim |

N=700 is deliberately not treated as an established optimum or as evidence transferred from P178. Its use is only to avoid inventing a new focal scale before observing direct-pipeline behaviour. If source history reveals a more appropriate already-frozen N for this exact direct theta_A DGP, that value takes precedence.

M=5 and R=4 are proposed only for a first directional screen. They do not support formal coverage acceptance or reliable MCSE estimation. In particular, M=5 is not a precision design, and the current within-world sampling mode remains UNVERIFIED.

### 3.2 Interpretation limits

For identified scenarios, report:
- point bias, MAE and RMSE using the exact planned M×R records and the existing fail-closed aggregation;
- inferential interval coverage and width only if every required R contribution is evaluable under the frozen all-R rule;
- interval availability over all planned R;
- identification and false-abstention rates over all planned R.

For the target-support-failure scenario, report correct abstention, wrong-cause abstention, partial identification and false identification, all over all planned R.

With only 20 R records per scenario, coverage is a coarse descriptive proportion. Show numerator, denominator and an uncertainty interval, but do not label it calibrated coverage or compare it against an acceptance band. Do not introduce a binary point-recovery rate until its tolerance is scientifically specified.

No type-I error or power metric is introduced: the current protocol does not define a hypothesis test.

## 4. Precision and sampling declarations

- Keep outer-world sampling mode `UNVERIFIED` unless a pre-existing, applicable, versioned outer-world contract is recovered and shown to match this DGP.
- Keep within-world R sampling mode `UNVERIFIED`. Each R varies both joint-policy randomization and S3 observation randomness. Distinct seeds establish stream separation/provenance, not an IID theorem.
- Consequently, no inferential MCSE or nested M/R projection is accepted from this screen. The nested module may be used descriptively only if its input and summary reconcile exactly and its status remains descriptive.
- The screen's across-M variation is descriptive. It is not a PASS_PRECISION result.

## 5. Staged execution envelope — proposal only

To control runtime and avoid another oversized run:

**Stage 0 — static authorization preflight (no scientific execution):**
- verify exact branch/commit, code and dependency identity;
- verify all five scenario contracts and their truths/support declarations;
- verify the proposed N/M/R design and seed-bank disjointness;
- verify the existing run path can execute one M-world block (R=4) without materializing duplicate cohorts;
- estimate resource cost from an explicitly authorized technical preflight only.

**Stage 1 — bounded screen:**
- one-use authorization required;
- use only a new development namespace;
- process one scenario × one outer-world block at a time (four R records per block), preserving the same world across those four R;
- persist checkpoint/provenance after each block;
- impose a hard 3-hour ceiling per workflow run, consistent with the project's run-time constraint; if a block cannot complete within that ceiling, stop and return measured resource evidence rather than silently splitting/reducing the scientific design;
- do not dispatch the next block automatically after a timeout or failure.

The 25 blocks (five scenarios × five M worlds) are a proposed sharding scheme, not an authorization to dispatch them. Before the full screen, the resource preflight must demonstrate that one block fits the ceiling.

If the workflow cannot safely checkpoint one M block or the resource preflight cannot establish its cost, the pilot remains BLOCKED; do not redesign the pipeline merely to force execution.

## 6. Development/evaluation bank separation

- Stage 1 uses a development-only namespace and may be inspected for design learning.
- No record, seed, world, S3 stream, or output from this screen may enter a later evaluation/holdout bank.
- Any later evaluation bank must be independently generated under a new namespace after the design, N/M/R, confidence level, metric targets, acceptance bands and stopping rule are frozen.
- The evaluation bank must remain unopened during development and tuning.

## 7. Numerical criteria intentionally not frozen

The following cannot be inherited from F5/Tier A defaults or test fixtures. They require explicit prospective decisions before any authorized calibration:
- inferential confidence level (0.95 is a candidate only, not adopted by this draft);
- point-recovery tolerance, if a binary recovery metric is desired;
- acceptable coverage interval and interval-availability floor;
- interval-width/informativeness criterion;
- MCSE target for each primary metric/scenario/N;
- outer-world sampling distribution/contract and within-world conditional sampling contract;
- development stopping rule and any expansion criteria beyond this first screen.

The historical F5 93–97% band, Wilson acceptance rule, 95% emission threshold and Tier A K/B values are not automatically transferable to direct theta_A.

## 8. Stop conditions

Stop the affected block and preserve the raw diagnostic state if:
- any planned R is missing, duplicated, mismatched to its seed assignment, or has inconsistent world/DGP/policy/support identity;
- Analyzer/Evaluator disagreement or evidence-integrity failure occurs;
- a nonidentified scenario is numerically identified or abstains for the wrong cause;
- an identified scenario produces unexpected abstention or unavailable inference;
- a world is not fixed across its R replicates;
- runtime exceeds three hours for one authorized workflow run;
- any code, dependency, seed namespace or canonical contract differs from the authorized manifest.

No automatic retries, sample-size reduction, scenario deletion, confidence/tolerance change or expansion are allowed.

## 9. Decision requested before authorization

This draft recommends the first screen at **N=700, M=5, R=4 across the existing five scenarios**, with 25 independently checkpointed scenario/world blocks and a three-hour per-run ceiling.

This recommendation is for an exploratory directional screen only. It is not a statistically adequate calibration design and does not resolve inferential sampling assumptions. The user must approve or revise the proposed dimensions and interpretation before a one-use execution authorization can be prepared.

`scientific_execution=false`  
`execution_authorized=false`


---

## 10. Correction after historical cross-check — 2026-11-27

**This section supersedes the proposed numerical dimensions and execution envelope in Sections 3 and 5 above.** The original N=700, M=5, R=4 and 25-block/3-hour proposal must not be treated as an adopted or recommended design.

The subsequent historical reconstruction identified a material gap in the original proposal:

1. The source-level review explicitly states that P178 and earlier Phase-A V_cont N/R values are not automatically transferable to direct theta_A. N=700 was borrowed as an anchor without evidence that it is appropriate for this direct focal DGP. It is therefore withdrawn as a recommendation.
2. M=5 and R=4 were proposed as convenient exploratory values, not derived from the existing nested precision contract or a measured pilot. They remain unsubstantiated candidates and are withdrawn as recommendations.
3. The 25-block decomposition and three-hour per-run ceiling were not verified against the actual runner's checkpoint semantics or a resource benchmark. They are not an execution-ready schedule.
4. The existing direct calibration protocol already requires a staged design: select an N grid against the four primary objectives, estimate within-world variability before selecting R, and justify M under an explicit outer-world target distribution. The design review also states that M<3 is insufficient for outer precision and M=2 is only a smoke/contract check. These requirements take precedence over the arbitrary values above.

### Corrected next operation

Do not freeze N/M/R yet. Reuse the existing direct pipeline and historical contracts to prepare a **dimension-selection note**, not a numerical execution plan:

- N: recover any already specified feasible N grid for this exact direct theta_A DGP; if none exists, identify a minimal candidate grid from the focal DGP's resource/estimand constraints, without importing P178 or F5 values as validated choices.
- M: retain UNVERIFIED outer-world sampling unless an applicable target distribution and independence basis are explicitly documented. A small M can be used only for descriptive development, not MCSE acceptance.
- R: retain the full assignment-plus-S3 observation interpretation. Choose R only after a bounded development sample provides an estimate of within-world variability; do not infer IID from distinct seeds.
- Resource budget: inspect the actual runner's checkpoint granularity and historical runtime evidence before proposing a shard count or ceiling. Preserve the user's <=3-hour preference as a planning constraint, not as evidence that each proposed block will fit.
- Stopping/acceptance: numerical confidence, coverage, availability, width and MCSE targets remain open and must be justified before any calibration.

### Status

The earlier numeric proposal is retained here only as an auditable superseded draft. No N/M/R design is frozen, no run schedule is approved, and no execution authorization is created.

`scientific_execution=false`  
`execution_authorized=false`


## 11. Runner and N-grid source audit — 2026-11-27

A further static inspection of the current direct theta_A source resolves what can and cannot be scheduled without implementation work:

- `ThetaACalibrationDesign.validate()` accepts any ascending positive-integer N grid. It enforces M>=2 and R>=2. It does not declare a recommended N grid, upper bound, or resource-derived values.
- `ThetaACalibrationDGPFactory.build_fixture()` defaults to N=32 only when no seed assignment/N is supplied. The calibration path passes N through the seed assignment. This default is a fixture convenience, not a scientifically selected calibration size.
- `build_theta_a_seed_bank()` materializes the complete N×M×R plan in memory. It does not invoke the DGP.
- `run_theta_a_calibration_replicates()` loops over every supplied assignment sequentially and calls the supplied world executor once per record. The function itself has no checkpoint/resume, sharding, concurrency, timeout, or partial-result persistence contract.
- No dedicated direct theta_A calibration GitHub Actions workflow was found in the research branch tree. Existing workflows are for F5/Tier A or static comparator work and cannot be treated as a direct theta_A execution route.

**Implications:** the earlier proposed 25-block sharding and three-hour per-run plan are not supported by the current runner. They would require a separately designed orchestration/checkpoint layer or an external executor with a verified contract. Do not build that layer merely to preserve the withdrawn proposal. First establish the actual per-replicate runtime/resource profile from existing complete-world execution evidence, if any; if none exists, the absence must remain explicit rather than be replaced with a speculative budget.

### Updated disposition

The direct theta_A statistical design is reusable and substantially implemented, but an execution-ready bounded pilot is **not yet specified**. The remaining minimum inputs are:
1. a scientifically justified candidate N grid for this DGP (N=32 is only the code default);
2. a defensible outer-world sampling target/contract if inferential MCSE is required;
3. a within-world sampling contract if R-based nested inference is required;
4. measured resource/runtime evidence and an execution route with checkpoint/recovery semantics;
5. prospective numeric coverage, availability, width and MCSE targets, plus a stopping rule.

Until these are supplied, the correct next state is **PILOT DESIGN BLOCKED — STATIC RECONCILIATION COMPLETE**, not a guessed N/M/R design. No new runner, workflow, checkpoint layer or seed bank is created by this audit.
