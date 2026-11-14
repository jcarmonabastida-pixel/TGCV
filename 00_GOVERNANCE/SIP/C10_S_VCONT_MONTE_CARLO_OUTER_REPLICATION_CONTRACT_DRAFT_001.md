# C10-S V_cont — Monte Carlo outer-replication implementation contract

**ID:** C10S-VCONT-MONTE-CARLO-OUTER-REPLICATION-001  
**Date:** 2026-11-13  
**Status:** DEFINED — IMPLEMENTATION OPEN  
**Branch:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)  
**Scope:** V_cont synthetic benchmark; no change to DGP truth, estimands, scenario matrix, identification assumptions or scientific acceptance thresholds.  
**Execution boundary:** no calibration, seed-bank generation, Monte Carlo, benchmark or scientific execution is authorized or performed by this contract.

## 1. Purpose and source inspection

This contract specifies the missing outer Monte Carlo dimension M and its relationship to the existing fixed-world repeated-assignment dimension R.

The reviewed implementation currently has:
- `SeedAssignment.replicate`, which identifies an assignment repetition;
- one fixed `world_seed` per scenario/version/N within a bank;
- varying Z and G assignment seeds across assignment repetitions;
- no explicit outer Monte Carlo replicate identity;
- no independent-world M aggregation identity.

Consequently, the existing seed-bank scaffold represents R within one world, not M independent outer worlds. The existing `required_replicates(calibration_sd, target_mcse)` remains an R-sizing helper and must not be reused or relabelled as M sizing.

## 2. Required hierarchy and identities

The hierarchy is:

`scenario/version/estimand/version/N → outer_replicate_id (m) → fixed world → {one RUN draw; R repeated joint assignments} → units (i)`.

The following identities are required:

| Identity | Meaning | Uniqueness scope |
|---|---|---|
| `outer_replicate_id` | Independent outer Monte Carlo world/sample draw m | Within bank × scenario/version × N |
| `world_id` | Fixed exogenous synthetic world for m | Within scenario/version × N × bank |
| `run_assignment_id` | One designated Z×G assignment used for RUN-level estimands in m | Exactly one per outer replicate and bank |
| `assignment_replicate_id` | One repeated joint Z×G assignment r within m | Within outer replicate |
| `run_id` | Unique generated dataset and execution | Globally within the benchmark artifact namespace |

The legacy `replicate_id` must not remain semantically ambiguous. During implementation it must either be migrated to the explicit `assignment_replicate_id` field with a compatibility rule, or be deprecated with a versioned schema change. It must never be interpreted as both R and M.

## 3. Generation contract

For each fixed scenario/version/N and each bank:

1. Generate M distinct outer replicate identities.
2. Derive a new independent world seed for every m. The world seed must not be held constant across m.
3. Hold that world fixed across the designated RUN assignment and all R repeated assignments belonging to m.
4. Generate exactly one designated RUN assignment per m, with its own Z and G assignment seeds. This is the Monte Carlo observation for RUN-level ITT-Z run-conditional and ITT-G(Z=0) performance.
5. Generate R additional joint Z×G assignments per m, with distinct assignment identities and seeds. These are used for mechanism-marginal and reference-regime repeated-assignment targets as authorized by the pair matrix.
6. Do not treat those R assignments as independent outer M replications.
7. Keep scenario version, DGP parameterization, N, estimand version and evaluation contract fixed across the M replicates within a declared benchmark cell.

The designated RUN draw is not selected after observing results. Its assignment-generation rule and its seed stream are fixed in the bank manifest before evaluation. The R repeated-assignment set is separately identified; it must not silently include or replace the designated RUN draw.

## 4. Random-stream and seed derivation contract

Seed derivation must be domain-separated by at least:

`(bank, namespace, scenario_id, scenario_version, N, outer_replicate_id, stream, assignment_replicate_id?)`.

Required stream roles:

- `world`: exogenous world/potential-outcome draw; varies across m and is fixed within m.
- `run_z`, `run_g`: designated RUN assignment streams; one pair per m.
- `repeat_z`, `repeat_g`: repeated-assignment streams; vary across r within m.
- Any future stochastic component not already deterministically derived from the world must receive its own named stream and schema version; it must not reuse a stream by convention.

Calibration and evaluation banks must remain disjoint across every seed role, including world, RUN assignment, repeated assignment and any future stochastic streams. The validator must reject collisions across roles and banks, duplicate identities, missing assignments, and violations of the fixed-world-within-m / independent-world-across-m rule.

The world definition includes the exogenous variables used to construct potential outcomes. If measurement-error randomness is generated from the same world stream, it is held fixed within m across assignments (common random numbers); if the scientific DGP later requires independent measurement-error draws by run, that must be introduced as a separately named stream and explicitly versioned. It must not change implicitly during implementation.

## 5. Manifest and provenance schema

Each bank manifest must declare:
- schema/version and bank label;
- benchmark namespace and code/configuration hashes;
- scenario ID/version and N;
- M and R counts and their indexing convention;
- outer replicate IDs and world IDs;
- one designated RUN assignment identity per m;
- the R repeated-assignment identities per m;
- seed values or protected seed references for every named stream;
- seed-bank fingerprint covering the complete ordered manifest;
- truth/DGP parameterization identity and estimand-matrix version;
- calibration/evaluation separation evidence.

Each generated RunManifest, TruthBundle and downstream record must carry enough provenance to recover:
`bank → scenario/version/N → outer_replicate_id → world_id → assignment_role → assignment_replicate_id → run_id`.

The outer replicate identity must survive Generator, Sealer, Analyzer, PairEvaluationRecord, temporal coverage manifest and benchmark aggregator without reconstruction from list position or run ordering.

## 6. Aggregation contract

The MONTE_CARLO level is a second-stage aggregation over exactly M independent outer-replicate contributions for a fixed aggregation key:

`K_MC = (scenario_id, scenario_version, estimand_id, estimand_version, temporal_level, metric_id, design_config_id)`.

Within each m:

- RUN metrics use the single designated RUN observation for that m. The RUN-conditional truth is the truth associated with that same run and realized assignment.
- REPEATED_ASSIGNMENT metrics first aggregate the R assignment records within that same fixed world m, using the matrix-approved aggregation and truth. This yields one repeated-level contribution per m.
- Status-only and non-identifiable pairs produce status contributions, not numeric errors or recovery values.
- Invalid or missing observations remain visible in coverage/validity denominators; they are not silently dropped or recoded as abstentions.

Across m, the aggregator computes benchmark performance summaries from the M per-m contributions. It must not flatten all R records across all M worlds and treat them as M×R independent Monte Carlo observations. For repeated-assignment metrics, R defines the within-world target estimate; M quantifies uncertainty/performance of that estimate across independent worlds.

If a per-m contribution cannot be produced, its missing/invalid state and reason remain in the M denominator and coverage report. Numeric summaries may use only eligible numeric contributions, with explicit eligible and total denominators. A required metric cannot receive PASS_PRECISION solely because invalid or missing m contributions were discarded.

## 7. Monte Carlo precision

For a scalar per-m metric contribution `psi_m`, report:
`MCSE(mean(psi)) = SD(psi_1,…,psi_M) / sqrt(M)`.

For a binary per-m outcome:
`MCSE(p_hat) = sqrt(p_hat * (1-p_hat) / M)`.

The M-sizing procedure, target MCSEs, calibration uncertainty treatment and any adaptive stopping rule remain governed by the Calibration and Seed-Bank Protocol. They must be explicitly specified before confirmatory evaluation. This contract defines the identity and aggregation unit; it does not approve numerical M values or precision targets.

## 8. Required validation and test obligations before implementation can be accepted

1. Different m values within the same scenario/version/N/bank have distinct world seeds and world IDs.
2. All assignments within one m share the declared world identity and world seed.
3. Every m has exactly one designated RUN assignment.
4. Every m has exactly R distinct repeated-assignment identities.
5. RUN and repeated-assignment stream roles cannot collide or be confused.
6. Calibration and evaluation seed banks have no seed overlap across any role.
7. Duplicate, missing, reordered, cross-world and cross-version identities fail closed.
8. Repeated-assignment aggregation occurs within m before Monte Carlo aggregation across m.
9. RUN-level aggregation uses one designated RUN contribution per m, not R as the M denominator.
10. Status-only, non-identifiable, invalid and missing outputs preserve their required denominators and never acquire numeric errors through coercion.
11. The complete 52-pair inventory and 65 existing temporal obligations remain intact; MONTE_CARLO is an aggregation level, not an extra scenario or estimand.
12. Replaying a manifest reproduces the same identities, seeds, hashes and aggregation membership.
13. MCSE is calculated across independent m contributions, never across the pooled R assignments.

## 9. Implementation sequence

Implementation should proceed in this order, without changing scientific targets:

1. Version the seed/manifest schema and disambiguate legacy `replicate_id`.
2. Add outer-replicate and assignment-role identities to seed assignments and manifests.
3. Implement domain-separated world, RUN and repeated-assignment seed derivation.
4. Extend seed-bank validation for independence across m and separation across banks/roles.
5. Propagate identity through Generator, TruthBundle, Sealer, Analyzer and PairEvaluationRecord.
6. Add per-m RUN and REPEATED_ASSIGNMENT contribution records.
7. Add MONTE_CARLO aggregation keyed by `K_MC`.
8. Add the fail-closed tests listed above and verify source-archive replay.
9. Reconcile the 52-pair inventory and all coverage/denominator reports against the implemented temporal manifest.

No calibration, seed-bank materialization, Monte Carlo sizing, benchmark or scientific execution is part of this implementation contract.

## 10. Gate 154 status

**GATE 154 — DEFINED AND PERSISTED; IMPLEMENTATION OPEN.**

This contract resolves the M/R identity and aggregation architecture. It does not freeze numeric N/R/M, precision thresholds, calibration stopping rules, or inferential procedures. No code or tests are changed by this document. No technical or scientific execution is recorded. `scientific_execution=false`; `execution_authorized=false`; `main` remains unchanged; PR #116 remains Draft.
