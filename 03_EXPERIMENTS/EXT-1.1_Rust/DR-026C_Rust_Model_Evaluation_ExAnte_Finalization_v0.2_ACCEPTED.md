# DR-026C — EXT-1.1 Rust Model and Evaluation Ex-Ante Finalization v0.2

**Status:** ACCEPTED — NEW EXPERIMENTAL DECISION  
**Acceptance date:** 2026-09-06  
**Scope:** Primary predictive model and evaluation protocol for EXT-1.1 Rust  
**Depends on:** DR-023, DR-024, DR-025A, DR-026A

## Decision

The DR-026C candidate protocol is accepted following structural audit PASS v0.2.

The primary confirmatory comparison is frozen as follows:

- Outcome: DR-023 `Y_180`.
- Eligible population: DR-024 complete-follow-up origins; census-first.
- Baseline: DR-025A `B_num = encode(V_o) || prior_release_count_o || package_age_days_o || D_o`.
- Accessibility representation: DR-026A `TAcc_repr = (A_rel, A_count)`.
- Primary learner: scikit-learn `LogisticRegression`.
- Penalty: L2.
- Solver: `liblinear`.
- `C = 1.0`.
- `fit_intercept = True`.
- `max_iter = 1000`.
- `tol = 1e-8`.
- `class_weight = None`.
- `random_state = None`.
- Hash algorithm: BLAKE2b-256.
- Hash dimension: `2^20`.
- Hash input: exact UTF-8 token bytes.
- Hash index: first 8 digest bytes, unsigned big-endian, modulo `2^20`.
- Hash sign: ninth digest byte even → `+1`, odd → `-1`.
- Baseline version token: `BASE_VERSION::<version_str>`.
- T_acc relation token: `TACC_PAIR::<target_package_id>::<target_version_id>`.
- No learned vocabulary, frequency filtering, collision correction or post-hoc feature selection.
- Numeric features: `prior_release_count_o`, `package_age_days_o`, `D_o`, and `A_count`.
- Numeric transform: `log1p`, followed by training-only standardization.
- Zero training standard deviation: transformed value fixed to 0.
- Temporal split: first 80% of the elapsed eligible-origin timeline for training and final 20% for test, with boundary calculated mechanically as `min_eligible_created_at + 0.80 * elapsed_span`.
- Primary metric: mean test log loss.
- Primary comparison: `ΔLogLoss = LogLoss(B) - LogLoss(T_acc)`; positive favors T_acc.
- Secondary descriptive metrics: Brier score and ROC AUC only if both test classes are present.
- No class reweighting, oversampling, undersampling or threshold tuning.
- B and T_acc use exactly the same eligible frame, temporal split, learner, regularization, convergence configuration and primary metric.
- Unrepresentable observations fail closed; no silent repair or exclusion.

## Inference boundary

Package-aware inferential uncertainty is intentionally **not frozen or authorized** by DR-026C. No p-value or confidence interval may be added post hoc to the primary result without a separate ex-ante inference decision addressing repeated releases within packages.

The primary descriptive estimand is the paired test-origin mean difference in log loss.

## Acceptance basis

The structural audit `AUDIT_DR-026C_Model_Evaluation_v0.2.md` passed with:

- 607,498 package-version observations;
- 507,279 eligible origins;
- 333,244 training origins;
- 174,035 test origins;
- temporal boundary `2021-02-12 15:56:28.678095+00:00`;
- all prohibited-input checks false;
- all symmetry checks true;
- deterministic hash replay;
- no outcome construction;
- no model fitting;
- no predictions;
- no performance metrics;
- no significance testing.

The earlier v0.1 audit failure was identified as an implementation aggregation bug, corrected without changing the experimental protocol or inspecting any empirical outcome.

## Freeze boundary

After acceptance, the following cannot be changed on the basis of confirmatory observations: outcome, horizon, eligible population, baseline representation, T_acc representation, tokenization, hash algorithm/dimension, numeric preprocessing, temporal split rule, learner, solver, regularization, convergence settings, class handling, or primary metric.

Any necessary change requires a new ex-ante decision and corresponding audit.

**This acceptance freezes the primary predictive protocol but does not itself authorize confirmatory execution.**
