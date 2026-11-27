# C10-S — F5 M1-PCT candidate integration specification

**Status:** DRAFT — DESIGN ONLY / REVIEW REQUIRED  
**Research branch:** research/c10s-coverage-first-focus-20261127  
**Related audit:** C10S_F5_M1_PCT_TIERA_CONTRACT_CROSSWALK_AUDIT_DRAFT_001.md  
**Execution:** NONE  
**Authorization:** This specification authorizes no tests, CI, benchmark, calibration, holdout, simulation or scientific execution.

## 1. Decision

Treat M1-PCT as an **interval-only challenger** in the F5 nested M/R comparison, not as a replacement for the common point estimator and not as a relabelled C5 implementation.

The common point-estimation contract remains \`observed_nested_mr_result\`:
- \`within_estimate\` is the mean unbiased within-world sample variance;
- \`between_estimate_raw\` is the untruncated sample variance of world means minus \`within/R\`;
- the common raw point estimates remain the basis for cross-method point bias/RMSE.

M1's fitted beta-binomial \`point_within\` and \`point_between\` remain candidate-specific model outputs. They must be preserved in M1 diagnostics/provenance, but are not substituted into the common comparison point fields and are not scored as though they were the common raw estimator.

M1's percentile intervals remain its own inferential outputs and are adjudicated against the independent F5 truth. The fact that the point metric is common does not imply that the interval is centered on that common estimator.

## 2. Why a versioned integration is required

The existing \`C10S_NESTED_MR_COMPARATIVE_INFERENCE_ENGINE_1.1\` declares the exact F5 roster:
- \`C0_FROZEN_V002_NESTED_PERCENTILE_1.2\`
- \`F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.1\`

Its adjudicator rejects any incomplete or unexpected roster. Its typed \`VarianceComparisonResult\` also requires finite point fields, so it cannot represent M1's original-fit abstention as a missing candidate-specific point estimate.

Do not modify or reinterpret engine 1.1, the existing C0/C5 records, or previously accepted C5 evidence. Introduce a separately versioned challenger comparison path (proposed engine ID \`C10S_NESTED_MR_COMPARATIVE_INFERENCE_ENGINE_1.2_M1_CHALLENGER\`) with an explicit three-method F5 roster:
- frozen C0 baseline;
- existing C5 candidate, unchanged;
- new M1-PCT interval challenger.

The new path may reuse the existing independent matched-dataset truth join and coverage/emission calculations, but must version its roster and record schema. It must not claim that the existing engine 1.1 already accepts M1.

## 3. Typed adapter contract

For every generated dataset, the adapter receives:
1. the immutable rectangular M×R binary dataset;
2. the common result from \`observed_nested_mr_result\`;
3. the M1 result, including method ID, fit ID, \`point_within\`, \`point_between\`, interval outputs, bootstrap replicate counts, fit status and typed failure reason;
4. the dataset ID and explicit design identity.

For a valid M1 interval result, the adapter creates a candidate record with:
- \`method_id = F5_M1_FUNCTIONAL_REFIT_PARAMETRIC_BOOTSTRAP_PCT_1.0\`;
- common \`within_estimate\` and \`between_estimate_raw\` copied unchanged from \`observed_nested_mr_result\`;
- \`within_interval\` and \`between_interval\` copied unchanged from M1;
- \`mcse\` fields explicitly unavailable/not evaluated unless a separate M1 MCSE procedure is specified;
- M1 fit and bootstrap provenance retained without lossy renaming.

M1 \`point_within\` and \`point_between\` must be preserved in a namespaced diagnostic payload (\`m1_model_point_within\`, \`m1_model_point_between\`) and never overwrite common point fields.

For an M1 original-fit or bootstrap failure:
- do not construct a valid M1 interval;
- preserve a typed dataset-level abstention reason and failed-replicate counts;
- count the dataset in the full emission denominator;
- do not drop the dataset, failed replicates or truth row;
- do not synthesize a finite point estimate from an inadmissible fit.

The challenger record must make clear that common point emission and M1 interval emission are different output channels. No metric may silently treat the model-based M1 point estimate as the common point estimator.

## 4. Independent truth, unit and denominators

Reuse the F5 fixture's independently generated truth record, keyed by unique \`dataset_id\`. Truth must be generated from the DGP parameters and never from M1 fitted outputs.

The coverage unit is one complete generated M×R dataset paired with one independent truth record. Worlds and within-world Bernoulli observations are nested sampling units, not independent coverage adjudication units.

For each method and component:
- point bias/RMSE denominator: datasets with a valid common point estimate, reported with point emission;
- interval emission denominator: all generated datasets in the adjudication batch;
- conditional coverage denominator: datasets for which that method emitted a valid interval;
- unconditional cover rate denominator: all generated datasets;
- abstention count: all datasets without a valid interval, including fit/bootstrap failures and invalid intervals.

Preserve interval-level coverage and point-level emission as separate metrics. Do not pool across input/target designs, F5 DGP cells, components or methods. Report the full dataset count, interval-emitted count, abstention count/reasons, conditional coverage, Wilson interval and unconditional cover rate.

The M1 development pilot (\`K=50\`, \`B=100\`) remains development-only and cannot be relabelled as Tier-A adjudication.

## 5. Frozen C5 and protocol firewall

- C5 implementation, method ID, fit contract, output records and accepted historical evidence remain unchanged.
- M1 is never labelled C5 and C5 coverage is never transferred to M1.
- Existing frozen C0/C5 Tier-A results remain valid only for their declared methods and protocol.
- The new M1 challenger path is a prospective, separately versioned comparison; it is not retroactive amendment of the old holdout.
- Any confirmatory M1 claim requires a separate protocol, independent validation data, fresh one-use authorization and a disjoint seed namespace.
- The current F5 frozen holdout (including its declared K and M/R cells) is not silently expanded or reused as an M1 validation set.

## 6. Seed separation and prospective resource design

Before any execution, specify and review:
- a development seed namespace used only for method debugging and bounded screening;
- a disjoint validation/holdout seed namespace inaccessible during method tuning;
- deterministic seed derivation and per-dataset provenance;
- the number of datasets and bootstrap refits per design cell;
- an explicit runtime budget and stop condition;
- the statistical precision/power rationale for any proposed K;
- a rule for whether a bounded screen is exploratory only or can trigger a later confirmatory protocol.

No K/B values are authorized by this specification. In particular, do not launch K=30/B=25, K=50/B=100, K=1,000 or any other batch on the strength of this document.

## 7. Required tests before any authorized bounded development run

Source-level test definitions must cover at least:
1. exact method roster and unique method IDs;
2. C0 and C5 records unchanged under the new versioned path;
3. M1 interval values copied without rounding, clipping or transformation;
4. common point fields remain byte/value-identical to \`observed_nested_mr_result\`;
5. M1 model point estimates remain separately preserved;
6. original-fit abstention and bootstrap-refit failure abstain at dataset level;
7. failed bootstrap replicates are not removed to manufacture a complete-case interval;
8. dataset/truth ID mismatch, duplicate IDs and missing truth fail closed;
9. interval emission uses all datasets as denominator;
10. conditional coverage uses emitted intervals only;
11. unconditional cover rate uses all datasets;
12. no pooling across designs, components or DGP cells;
13. deterministic output and fresh-seed namespace separation;
14. no M1 field can overwrite C5 identity, fit provenance or interval outputs.

These are proposed test definitions only. They must not be executed until separately authorized.

## 8. Scientific and inferential limits

An M1 pass on F5 beta22 would establish only bounded performance for the declared beta-binomial DGP and specified M/R designs. It would not establish robustness to model misspecification, general nested variance decomposition, causal identification of \`theta_A\`, validity of the C10-S \`V_cont\` Analyzer/Evaluator, or any \`Delta T_acc -> Delta V\` claim.

The F5 Raw-between Tier-A workstream is statistically distinct from the C10-S causal estimand. No M1 result transfers to \`theta_A(q_X*, r_common; V_cont)\` or to the integrated causal architecture.

## 9. Review disposition and next gate

**Proposed design decision:** \`M1_INTERVAL_ONLY_CHALLENGER / COMMON_RAW_POINT_METRICS / VERSIONED_THREE_METHOD_ROSTER\`.

Before implementation:
1. review and accept this candidate role and its reporting semantics;
2. confirm whether the separate engine 1.2 path is the minimum acceptable version boundary;
3. approve a source-only implementation scope and test definitions;
4. separately decide whether/when to authorize a bounded development screen.

Until those decisions are made, the implementation remains OPEN and all empirical execution remains unauthorized.
