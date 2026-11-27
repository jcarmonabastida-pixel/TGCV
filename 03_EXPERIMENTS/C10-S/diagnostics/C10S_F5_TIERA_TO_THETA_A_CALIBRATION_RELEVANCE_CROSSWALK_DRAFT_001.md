# C10-S — F5 Tier-A / M1-PCT relevance crosswalk to direct theta_A calibration

**Date:** 2026-11-27  
**Status:** STATIC RECONCILIATION COMPLETE / M1 F5-SCOPED / NO DIRECT TRANSFER TO THETA_A / NO EXECUTION  
**Branch:** `research/c10s-m1-engine12-source-only-20261127`  
**Scope:** F5 M1-PCT Raw-between evidence versus the direct-g_A theta_A Analyzer/Evaluator and its N×M×R calibration protocol  
**Authorization:** No tests, seed-bank generation, calibration, simulation, benchmark, holdout, workflow or scientific execution.

## 1. Executive finding

M1-PCT is a candidate interval procedure for the F5 beta-binomial between-world variance functional. It is **not** the inferential procedure for the direct causal estimand

`theta_A(q_X^*, g_{A0}, g_{A1}; r_{common}, V_{cont})`.

The direct theta_A Analyzer uses a history-standardized two-arm Horvitz–Thompson contrast and, when eligible, the `HOEFFDING_TWO_STAGE_BOUNDED_HT_V1` interval. Its calibration scaffold is separate: `theta_a_calibration_protocol.py` captures the actual Analyzer/Evaluator result over N units, M outer worlds and R repeated direct-`g_A` assignments within each fixed world.

There is a limited algebraic analogy: for a binary per-R calibration metric, the per-world success probability can be written as `p_m`, and the between-world component is `Var(p_m)`. That does not make the F5 M1 interval transferable. The distribution of `p_m`, the target population, the unit, the meaning of R, the abstention event and the coverage denominator must all match. They do not currently match by contract or evidence.

**Disposition:** retain the M1 adapter as an isolated F5 research challenger only. Do not connect it to theta_A, do not treat F5 Tier-A evidence as theta_A calibration, and do not launch the M30/R20 M1 screen on the basis of this crosswalk.

## 2. F5 M1-PCT statistical object

The F5 beta22 fixture declares independent world probabilities

`p_i ~ Beta(2,2)`, with `Y_ij | p_i ~ Bernoulli(p_i)`.

Its component targets are:

- `W = E[p_i(1-p_i)] = 0.20`;
- `B = Var(p_i) = 0.05`.

M1-PCT refits the beta-binomial likelihood and constructs percentile-bootstrap intervals for W and B. The F5 comparative engine's common point estimator for between variance remains the untruncated raw estimator `S²(world means) - within/R`; M1's fitted Beta-binomial point functional is an auxiliary model estimate, not a replacement for that common point metric.

The M1 F5 pilot remains development-only:
- M10/R5: 50 datasets, 2 emitted, 4% emission; 100% descriptive coverage among only 2 emitted; 846/4,500 bootstrap refits non-admissible.
- M30/R20: 50 datasets, 50 emitted, 100% emission; descriptive coverage 98% within and 94% raw-between; no formal Tier-A adjudication.

M1 was not selected for Tier-A under its existing fail-closed contract. Dropping failed refits or weakening abstention is not an acceptable repair.

## 3. Direct theta_A statistical object

The direct path is defined by the following source contracts:

- `theta_a_analyzer.py`: history-standardized contrast over target `q_X^*), joint policies `g_A0/g_A1`, fixed `r_common`, with history-specific assignment probabilities. The optional inferential interval requires a declared confidence level, assignment probabilities and explicit unit-independence certification.
- `theta_a_evaluator.py`: independently reconstructs the bounded two-stage HT interval from sealed evidence and the analysis contract; separately evaluates logical identification bounds and inferential-interval coverage against reserved theta_A truth.
- `theta_a_calibration_protocol.py`: records one actual Analyzer/Evaluator result per `(scenario, N, outer_world_id, assignment_replicate)`; validates source/target population bindings and seed provenance; summarizes R within each fixed M, then aggregates M.
- `theta_a_calibration_dgp.py`: materializes the declared focal DGP variants through the complete-world pipeline.

The inferential interval and logical identification bounds are distinct outputs. The Evaluator's `truth_within_bounds` is not a substitute for `inference_truth_covered`; the focal calibration record captures both separately.

## 4. N/M/R and population/unit crosswalk

| Dimension | F5 M1-PCT | Direct theta_A calibration |
|---|---|---|
| N | Not a dimension in the F5 M×R fixture | Number of experimental units (UEs) in one synthetic world |
| M | Independent latent-probability worlds within one F5 dataset | Independent outer synthetic worlds |
| R | Bernoulli observations within each F5 world | Repeated randomized direct-`g_A` assignments within one fixed outer world |
| Per-R observation | Binary `Y_ij` generated from latent `p_i` | A complete assigned-policy run and its Analyzer/Evaluator outcome |
| Target population | F5 beta22 mixing population | Baseline histories with target masses `q_X^*), one positive mass per UE/history |
| Unit | F5 world for the latent probability; complete M×R dataset for coverage | UE for assignment/inference; complete run for one R replicate |
| Between component | `Var(p_i)` under the F5 Beta mixing model | `between_raw = MSB/R - MSW/R` for the supplied per-R metric contributions; its population depends on the theta_A scenario and metric |

The direct synthetic-world contract binds q_X* exactly once to every generated baseline history and requires one positive target mass per unit, summing to one. The policy-assignment bundle requires exactly one assignment per q_X* history/unit. This is the correct population/unit binding for the direct theta_A pipeline.

The F5 M1 pilot's F5 world is not a UE, and its Beta(2,2) mixing population is not q_X*. Equal-looking M and R labels do not establish population or sampling-unit equivalence.

## 5. Raw-between: limited algebraic correspondence, not estimator transfer

The generic direct theta_A nested precision module, `theta_a_nested_mc_precision.py`, consumes already-adjudicated per-R scalar metric contributions `q_mr). It computes:

- within-world mean square `MSW`;
- between-world mean square `MSB`;
- untruncated `between_raw = (MSB - MSW)/R`;
- observed variance of outer-world means;
- bootstrap intervals and projected MCSEs, subject to declared within- and outer-world sampling contracts.

For a binary metric such as interval coverage or interval availability, the per-R contributions are 0/1. If, additionally, the induced per-world success probabilities `p_m) followed a Beta distribution, then the population decomposition would have the same form `W=E[p_m(1-p_m)]), `B=Var(p_m)`. This is a conditional mathematical analogy only.

It does **not** establish that the theta_A metric-specific `p_m) distribution is Beta(2,2), or even Beta. The distribution is induced by the actual DGP, q_X*, g_A assignment mechanism, r_common, N, scenario and metric. F5 M1's known Beta22 oracle is therefore not an independent oracle for theta_A calibration.

M1 is also not a general replacement for the direct nested precision module:
- its beta-binomial likelihood is suitable only for binary per-R contributions under an adequately justified Beta-mixing model;
- theta_A calibration also includes continuous contributions such as point bias, MAE, squared error/RMSE and interval width;
- the direct precision module's bootstrap operates on the actual supplied metric contributions and preserves the untruncated raw-between component and its boundary behaviour.

No M1 integration into `theta_a_nested_mc_precision.py` is specified or justified.

## 6. Abstention and coverage denominators

| Contract dimension | F5 Tier-A / M1 | Direct theta_A calibration |
|---|---|---|
| Abstention event | Original beta-binomial fit inadmissible, or any bootstrap refit inadmissible; whole dataset abstains | Analyzer identification/support/measurement disposition: IDENTIFIED, NOT_IDENTIFIED, INDETERMINATE or PARTIALLY_IDENTIFIED, with expected and observed causes |
| Emission denominator | All K complete datasets | All planned R assignments within each fixed M |
| Conditional/usable coverage | Among emitted intervals; reported separately from emission | `interval_coverage` is evaluable only when every planned R in each M has an inferential interval; otherwise the M contribution is NOT_EVALUABLE |
| Availability | Dataset interval-emission rate over all K | `interval_availability_rate` over all planned R |
| Aggregation | Matched dataset-level adjudication | R within fixed M, then equal-weight aggregation across M |
| Abstention metrics | Dataset-level fit/bootstrap reason counts | Identification, abstention, false-abstention, correct/wrong-cause abstention, partial-identification and false-identification rates |

The theta_A protocol deliberately does not silently compute coverage from only the emitted subset. It records interval availability over all R and marks interval coverage/width NOT_EVALUABLE when any required R interval is absent within an M. This is not the same estimand/denominator as M1's conditional coverage among emitted F5 datasets.

The F5 M1 bootstrap-failure abstention is a method-fit event. It must not be relabelled as a causal Analyzer non-identification or measurement abstention.

## 7. Statistical precision and calibration status

The direct theta_A scaffold already declares a 16-metric registry, including:
- identification, abstention and interval availability;
- Evaluator truth-within-bounds and correct-adjudication rates;
- false abstention;
- point bias, MAE, RMSE and point recovery;
- inferential interval coverage and width;
- correct/wrong-cause abstention, partial identification and false identification.

It requires a versioned metric-target manifest for any nonempty MCSE targets. The outer-world sampling contract defaults to `UNVERIFIED`; inferential MCSE and precision verdicts are suppressed unless the sampling mode and supporting contract are explicitly declared. Type-I error and power remain undefined until a separate hypothesis-test procedure exists.

The calibration/evaluation seed-bank validator is already designed to require complete N×M×R banks and disjoint world, assignment, S3 and run streams. The runner requires an explicit `execution_authorized=True` and a complete-world executor. No bank, N/M/R design, metric-target manifest or numerical calibration is authorized or materialized by this audit. The five-scenario roster remains a candidate roster, not a frozen design.

Historical EP-02 deterministic contract-test evidence is software evidence only; it is not N×M×R calibration, interval-coverage evidence or scientific execution.

## 8. Decision

1. **F5 M1-PCT:** remains F5-only. Its current adapter can compare M1 intervals against F5 independent truth under the F5 roster, if later tests are authorized. It does not alter C0/C5 and does not change any causal Analyzer/Evaluator contract.
2. **Direct theta_A inference:** use the existing `theta_a_analyzer.py` / `theta_a_evaluator.py` interval contract as the object whose coverage must be calibrated.
3. **Nested MC precision:** use the existing `theta_a_calibration_protocol.py` and `theta_a_nested_mc_precision.py` as the direct path's existing calibration/precision scaffold. Do not replace it with M1 by analogy.
4. **No threshold transfer:** F5 Tier-A's 93–97% conditional coverage band, Wilson rule and >=95% emission threshold are not automatically theta_A acceptance rules. The theta_A metric-target manifest and precision/coverage acceptance criteria require their own prospective justification.
5. **No new M1 workstream:** do not launch M30/R20 M1 screening or add more interval-engine instrumentation from this crosswalk.

## 9. Minimum next operation

The next useful task is a **single static design review of the existing direct theta_A calibration scaffold**, not another implementation:

- verify the exact relationship between the HT/Hoeffding inferential interval and the calibration `interval_coverage` metric;
- confirm the all-R emission/coverage denominator and equal-M aggregation are the intended target;
- identify which of the existing 16 metrics are necessary to distinguish interval calibration, point recovery, identification and abstention;
- identify the still-unselected N/M/R, outer-world sampling contract and metric-target/MCSE manifest inputs;
- keep the independent evaluation bank disjoint and unused until the calibration design is prospectively frozen.

No values for N/M/R, metric targets, MCSE tolerances, power, type-I error, confidence level or new scenarios are selected here. No code change, tests, seed-bank generation, CI, benchmark, simulation or scientific execution is authorized.

