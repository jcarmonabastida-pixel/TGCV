# C10-S V_cont — Gate 156: MONTE_CARLO Matrix Coverage and Temporal Manifest Contract

**Status:** IMPLEMENTED / TECHNICALLY VERIFIED THROUGH GATE 157 — TARGETED CLASSIFICATION REGRESSION CONDITIONAL  
**Branch:** `research/c10-s-consolidation-draft`  
**Scope:** C10-S synthetic V_cont benchmark; matrix coverage and MONTE_CARLO reporting  
**Scientific execution:** NOT AUTHORIZED  
**Calibration / seed-bank generation:** NOT EXECUTED

## 1. Purpose and historical reconciliation

Gate 155 implemented the outer M identity, one designated RUN per outer world, R repeated assignments within that world, and a per-scenario Evaluator aggregation over M.

The historical reconstruction identifies a remaining integration boundary rather than a need to replace that work:

- `build_scenario_estimand_matrix()` defines the authoritative 52 scenario–estimand pairs (13 scenarios × 4 estimands).
- `evaluate_monte_carlo()` currently selects and summarizes the four pairs for one scenario/version at a time.
- Its returned coverage count is therefore per-scenario (four pairs), not a complete 52-pair benchmark manifest.
- The current per-scenario result does not itself provide a single canonical, keyed contribution ledger for all 52 pairs.
- The current entry point does not require a declared common R count for every M within a scenario.
- Status summaries must be adjudicated against each matrix pair's temporal classification and expected identification/abstention state; a boolean derived from an Analyzer status is not by itself a matrix-complete status record.

Gate 156 adds a benchmark-level integration contract. It does not replace Gate 154's M/R identity contract or Gate 155's tested per-scenario aggregation.

## 2. Canonical identities

### 2.1 Matrix pair

The authoritative base key remains:

`K = (scenario_id, scenario_version, estimand_id, estimand_version)`.

For MONTE_CARLO aggregation:

`K_MC = (scenario_id, scenario_version, estimand_id, estimand_version, temporal_level=MONTE_CARLO)`.

Metric identity is an additional field, not a substitute for `K_MC`. A metric target must therefore be keyed by the full pair identity and metric name; generic labels such as `run_conditional.mae` are insufficient in a 52-pair report.

### 2.2 Temporal manifest row

Each generated contribution must be traceable by:

`(scenario_id, scenario_version, N, outer_replicate_id=M, assignment_role, replicate=R-index)`.

Required provenance fields:

- `world_id` and `world_seed`;
- Z and G assignment seeds;
- `run_id`;
- scenario/version and N;
- assignment role and R index;
- seed-bank identity/fingerprint and bank label;
- executable/code commit and configuration identity.

The manifest must preserve the explicit distinction:
- one `RUN` row per M, with `replicate=-1`;
- exactly R `REPEATED_ASSIGNMENT` rows per M, with R indices `0..R-1`.

## 3. M/R/N completeness rules

For each scenario/version/N evaluation block:

1. Exactly the predeclared M outer identities must be present; no duplicate or missing M identity is permitted.
2. Every M contains exactly one designated RUN.
3. Every M contains exactly the same predeclared R repeated assignments.
4. R indices are unique and complete from 0 through R−1.
5. RUN and R rows within one M share exactly one world identity and world seed.
6. Different M identities have different world identities and world seeds.
7. Z/G assignment seeds remain distinct by stream and assignment; calibration and evaluation banks remain disjoint.
8. Scenario/version and N are fixed within a block. No aggregation may pool different scenario versions or N values.
9. The observed M and R counts must equal the declared design; observed counts must never silently redefine the expected design.

The contract does not choose numeric M, R or N. Those values remain open until the governed calibration/design decision.

## 4. Full 52-pair benchmark coverage

A benchmark-level aggregation receives one per-scenario M block for each of the 13 scenario IDs in the authoritative matrix.

Acceptance requires:

- exactly 13 required scenario IDs;
- exactly four unique estimand keys per scenario;
- exactly 52 unique `K` keys, with versions matching the authoritative matrix;
- exactly one MONTE_CARLO summary/contribution series for each `K_MC`;
- exactly M outer contributions per pair at its matrix-authorized temporal level;
- no extra, duplicated, omitted, version-mismatched or unrecognized pair.

A complete report has a 52-row pair ledger. It must not report only a scalar `required_pairs=52` count without the actual keys and their individual dispositions.

The per-scenario evaluator remains responsible for the within-scenario M calculations. The benchmark-level aggregator composes and validates those outputs; it does not recompute or silently reinterpret DGP truth or Analyzer outputs.

## 5. Matrix-authoritative temporal contribution

For every pair, the matrix's `run_evaluation_class` and `repeated_evaluation_class` determine which temporal source contributes:

| Estimand | Per-M source | MONTE_CARLO contribution |
|---|---|---|
| ITT-Z run-conditional | One designated RUN | Run-level estimate/error/status |
| ITT-G, Z=0 | One designated RUN | Run-level estimate/error/status |
| ITT-Z mechanism-marginal | R assignments aggregated within M | One within-M marginal estimate/error/status |
| ITT-Z reference-regime | R assignments aggregated within M for numeric recovery; designated RUN remains status-only | One within-M reference estimate/error/status where matrix permits it |

No R assignment may substitute for a RUN contribution. No RUN estimate may substitute for the within-M marginal estimands.

For `EVALUABLE` temporal pairs, numeric contribution is required for a complete numeric metric series. If an Analyzer abstains or fails to produce a finite estimate, the record remains present as a failed/invalid contribution; it is not dropped or converted to zero. The corresponding numeric summary is `NOT_EVALUABLE`/incomplete rather than calculated on a selectively reduced M denominator.

For `STATUS_ONLY` and `NOT_IDENTIFIABLE` pairs:
- numeric truth comparison, error, MAE, RMSE and numeric recovery are prohibited;
- status contribution is mandatory for every M;
- the observed identification and abstention state is adjudicated against the exact matrix expectation.

For all classes, preserve the distinction among identified, not identified, indeterminate, abstained, invalid output and missing record. Missing is not abstention; invalid is not non-identification.

## 6. Per-pair MONTE_CARLO metrics and denominators

Each of the 52 pair-ledger rows reports, as applicable:

- expected M and observed M;
- temporal source (RUN or REPEATED_ASSIGNMENT);
- matrix evaluation class and truth status;
- numeric contribution count / expected M;
- status contribution count / expected M;
- missing, invalid and abstention counts separately;
- bias, MAE and RMSE plus their M-level MCSE and predeclared target, only for a complete numeric EVALUABLE series;
- recovery, identification, non-identification, indeterminacy and abstention rates with explicit denominator M, where applicable;
- precision status: `PASS_PRECISION`, `FAIL_PRECISION` or `NOT_EVALUABLE`;
- pair-level disposition and reasons.

Binary-rate MCSE/Wilson intervals describe Monte Carlo uncertainty in benchmark rates only. They are not confidence intervals for causal effects.

Metric target identity is:

`(K_MC, metric_name) → target_mcse`.

The supplied target set must equal the exact set of numeric metrics required by the matrix for the 52 pairs. Targets are not inferred from defaults or copied across scenarios merely because the estimand label is the same. Status-rate targets, if used as acceptance criteria, must be separately predeclared and keyed in the same way.

## 7. Benchmark-level report and reconstruction

The canonical MONTE_CARLO report must include:

1. **Design header:** scenario versions, N, M, R, seed-bank label/fingerprint, executable commit, matrix identity/hash, configuration hash and metric-target manifest.
2. **Temporal manifest:** all expected M × (1 RUN + R assignments) identities per scenario, with observed provenance.
3. **Pair ledger:** all 52 `K_MC` rows, their temporal source, classes, denominators, metrics and dispositions.
4. **Coverage summary:** 52/52 pair identities; per-pair M coverage; per-scenario M/R completeness; numeric and status denominators.
5. **Contribution ledger:** one immutable per-M contribution for every pair at its authorized temporal level, including non-numeric status contributions.
6. **Reconstruction integrity:** stable fingerprints/hashes allowing every summary to be recomputed from the contribution ledger and the declared matrix/targets.

Aggregate-only output without per-M contributions is insufficient for audit. The report must not erase scenario-level failures behind pooled metrics.

## 8. Acceptance tests required for implementation

The implementation must test at least:

- exact 13 × 4 = 52 key coverage;
- omitted scenario, omitted estimand, duplicate key and extra key rejection;
- scenario-version and estimand-version mismatch rejection;
- exact declared M and R counts; missing/duplicate M, RUN or R index rejection;
- distinct world identity/seed across M and fixed world identity/seed within M;
- RUN versus repeated temporal-source enforcement for all four estimands;
- matrix-authoritative EVALUABLE / STATUS_ONLY / NOT_IDENTIFIABLE handling;
- no numeric metrics for non-numeric classes;
- abstention, invalid output and missing contribution kept distinct;
- an incomplete numeric series yields no deceptively complete M metric;
- per-pair metric targets require full K_MC identity and reject missing/extra targets;
- reconstruction of each aggregate from the retained per-M contribution ledger;
- no cross-scenario, cross-version, cross-N or cross-level pooling.

Tests must use deterministic fixtures only. They must not generate calibration/evaluation seed banks or perform benchmark, calibration, sizing or scientific execution.

## 9. Implementation sequence — Gate 157

1. Add a declared design object carrying expected scenario/version set, N, M, R, matrix identity and pair-keyed metric targets.
2. Validate each per-scenario M block against exact M/R completeness before aggregation.
3. Preserve a per-M, per-pair contribution ledger from the existing Evaluator.
4. Add a benchmark-level aggregator composing all 13 scenario blocks and validating all 52 matrix keys.
5. Apply matrix-authoritative status adjudication and denominator accounting per pair.
6. Emit a reconstructable report manifest and fingerprints.
7. Add the fail-closed acceptance tests in §8.
8. Run only the deterministic technical test workflow after implementation; no calibration or scientific execution.

## 10. State and authorization

**Gate 156: IMPLEMENTED / TECHNICALLY VERIFIED through Gate 157.**

- Gate 154: M/R identity and temporal separation contract — DEFINED / PERSISTED.
- Gate 155: M/R seed identity and per-scenario aggregation — IMPLEMENTED / TECHNICALLY VERIFIED at the recorded commit/run.
- Gate 156: benchmark-level 52-pair coverage, per-pair denominators and reconstructable contribution ledger — IMPLEMENTED / TECHNICALLY VERIFIED; implementation record: `C10_S_VCONT_MONTE_CARLO_BENCHMARK_AGGREGATION_IMPLEMENTATION_GATE_157_DRAFT_001.md`.
- Numeric N/R/M, MCSE targets, calibration budget and scientific acceptance thresholds remain OPEN.
- `scientific_execution=false`; `execution_authorized=false`.
- No calibration/evaluation seed bank, Monte Carlo sizing, benchmark or scientific execution is authorized or recorded.
- `main` is unchanged; PR #116 remains Draft on its existing base branch.
