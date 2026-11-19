# C10-S — Nested M/R calibration comparison design

**Record:** C10S-NESTED-MR-CALIBRATION-COMPARISON-DESIGN-001  
**Status:** RESEARCH DESIGN — NON-CANONICAL / F1 C1 + F5 C5 CONNECTED THROUGH COMMON COMPARISON ENGINE / STATIC CI PASS 36 OF 36 / NO COVERAGE EXECUTION  
**Date:** 2026-11-19  
**Predecessor diagnosis:** `C10S_NESTED_MR_TIER_A_CALIBRATION_INVESTIGATION_001`  
**Frozen baseline:** protocol `C10S-NESTED-MR-BOOTSTRAP-VALIDATION-001` v002; method `TGCV_NESTED_MR_BOOTSTRAP` 1.2  
**Source Tier A run:** `44449787220`; artifact `14495695421`; code commit `6bcb5a2827d810896315f66042083a5be7dda308`

## 1. Decision and boundary

The next operation is a controlled comparison of interval procedures on common synthetic datasets, not another Tier A/Tier B run and not a change to the frozen estimator. The purpose is to identify which inferential procedure, if any, has defensible finite-sample coverage for the two variance components and their MCSE functional across the declared fixture families.

Protocol v002 and its Tier A result remain immutable. Current percentile intervals remain the baseline. This document neither selects a winner nor authorizes implementation execution, Tier B, or C10 scientific execution.

## 2. Statistical target and invariants

For balanced nested observations:
`q_{mr}=\mu+U_m+\epsilon_{mr}`, with independent outer effects and conditional inner errors in F1.

The unbiased ANOVA component estimators remain:
`MSW = SSW/[M(R-1)]`,
`MSB = R S^u_{\bar q}`,
`\hat\sigma^2_w=MSW`,
`\hat\sigma^2_{b,raw}=(MSB-MSW)/R=S^u_{\bar q}-MSW/R`.

The raw between estimate is the scored inferential object. A nonnegative convenience estimate may be reported separately but must never replace or truncate `between_raw` in bias, RMSE, coverage, likelihood, or bootstrap records.

The target projection is:
`g(\sigma_b^2,\sigma_w^2)=\operatorname{MCSE}(M^*,R^*)=\sqrt{\sigma_b^2/M^*+\sigma_w^2/(M^*R^*)}`.

Every candidate must preserve the same dataset, truth, M/R structure, target projection and coverage denominator. No method-specific deletion of negative raw draws is allowed without an explicitly defined constrained inferential construction.

## 3. Candidate method families

### C0 — Frozen baseline: two-stage nonparametric percentile bootstrap

- Exact protocol-v002 resampling law: resample M complete clusters, then R contributions within each selected cluster copy.
- Retain all B draws, including all-same-source cluster samples and negative raw-between values.
- Report percentile intervals for raw within, raw between and any declared regular projection.
- This is the comparison baseline, not a presumed acceptable procedure.

### C1 — Gaussian exact / finite-sample pivot benchmark (F1 only)

Under the balanced Gaussian random-intercept fixture:

`\nu_w=M(R-1)`,
`\nu_b=M-1`,
`\nu_w MSW/\sigma_w^2\sim\chi^2_{\nu_w}`,
`\nu_b S^2_{\bar q}/\tau^2\sim\chi^2_{\nu_b}`,
where `\tau^2=\sigma_b^2+\sigma_w^2/R`. The two pivots are independent.

Within interval at level 1−α:
`[\nu_w MSW/\chi^2_{1-\alpha/2,\nu_w},\ \nu_w MSW/\chi^2_{\alpha/2,\nu_w}]`.

Between raw inference must retain the constraint `\sigma_b^2=\tau^2-\sigma_w^2/R\geq0`. Include:
1. a conservative Bonferroni interval formed from independent `\tau^2` and `\sigma_w^2` intervals, explicitly labelled conservative;
2. a constrained profile-likelihood interval for `\sigma_b^2`, with nuisance `\sigma_w^2` profiled over the admissible parameter space.

Do not label the conservative interval efficient. C1 is an oracle/reference for F1 only and is not a general-purpose solution for F5 or real C10 metrics.

### C2 — Parametric bootstrap under the declared DGP

- F1: generate parametric bootstrap datasets from the fitted Gaussian random-intercept model; refit both variance components on each dataset; retain negative raw between estimates.
- F5: fit a declared beta-binomial random-effects model to world-level Bernoulli contributions; use the exact fixture parameterization as a separate oracle-known upper-bound diagnostic, not as the deployable fitted procedure.
- Refit the complete estimator in each parametric replicate. Do not bootstrap only a derived formula while holding nuisance estimates fixed.
- Report sensitivity to boundary estimates, optimizer failures, convergence, parameter constraints and fit misspecification.

Oracle-known F5 parameters are not a fair estimate of real-world calibration and must be labelled as an oracle benchmark.

### C3 — BCa hierarchical cluster bootstrap

- Preserve M as the outer resampling unit and R as the conditional inner unit.
- Bias correction must be computed from the same target statistic and same raw (untruncated) estimand.
- Acceleration must use a delete-one-outer-cluster jackknife as the primary cluster-level influence calculation. Inner-level jackknife is not interchangeable with outer-level acceleration.
- If a stable acceleration cannot be computed (ties, degenerate jackknife, insufficient outer support), return a typed abstention, not a percentile fallback.
- Report acceleration, bias-correction constant, adjusted quantiles and failure rate.

BCa is a candidate only; it may not be presumed to fix a non-smooth/boundary variance estimator.

### C4 — Studentized nested bootstrap

- Define the studentized statistic for each component before implementation.
- The standard error inside each bootstrap replicate must be computed from a valid nested variance-estimator approximation, not borrowed from the original sample.
- Outer-cluster jackknife or a predeclared analytic standard error may be evaluated as studentizer candidates.
- Report studentizer stability, tail quantiles, failures and computational multiplier.
- No studentized interval is admissible if the replicate-level standard error is zero, undefined or based on an unsupported M/R contract.

C4 is likely expensive; benchmark a small development subset before considering confirmatory K.

### C5 — Boundary-aware joint inference for the MCSE functional

This is a separate inferential target, not a side-effect of separately calibrated marginal component intervals.

For F1, use the independent sufficient statistics:
- `X=MSW`, with `\nu_w X/\sigma_w^2\sim\chi^2_{\nu_w}`;
- `Y=S^2_{\bar q}`, with `\nu_b Y/(\sigma_b^2+\sigma_w^2/R)\sim\chi^2_{\nu_b}`.

Define the constrained parameter space:
`\Theta=\{(\sigma_b^2,\sigma_w^2):\sigma_b^2\geq0,\sigma_w^2\geq0\}`.

Construct a profile likelihood for the scalar target `g(\sigma_b^2,\sigma_w^2)` by maximizing the likelihood over all nuisance combinations satisfying a fixed g, then invert a predeclared likelihood-ratio cutoff. Calibrate the cutoff by exact/simulation-based finite-sample coverage over the F1 grid; do not assume Wilks' chi-square cutoff is valid at a boundary. A generalized-pivotal alternative may be compared on the same joint target.

The procedure must:
- include boundary mass rather than discard negative raw bootstrap estimates;
- return a numeric MCSE interval whenever the inversion is defined, including when the MLE is on the boundary;
- distinguish a legitimate unbounded/one-sided interval from computational failure;
- report boundary estimate frequency, likelihood-ratio calibration, interval width and coverage;
- be invariant to B because B is not part of this analytic inferential procedure.

For F5, no Gaussian pivot may be reused. Candidate MCSE inference must be calibrated against the beta-binomial oracle and the fitted beta-binomial parametric procedure separately.

## 4. Matched comparison protocol

All candidate procedures are evaluated on identical datasets and identical target parameters. The comparison must not use the original Tier A datasets as final acceptance evidence after method selection.

### Development stage

Use existing Tier A records only to debug and understand failure modes. New development simulations use a separate seed namespace and are labelled exploratory. Method selection criteria and code are recorded before inspecting any holdout result.

### Independent holdout stage

After freezing the candidate list, implementation, tuning rules and protocol:
- create a new seed namespace/version and fresh K datasets per cell;
- retain the eight Tier A cells and add predeclared F2 near/exact boundary cells and F5 sparse/constant controls as appropriate;
- use enough K for the Monte Carlo uncertainty of coverage to discriminate the [93%,97%] gate; K must be justified prospectively;
- use B sufficient for stable bootstrap quantiles, with Monte Carlo error of interval endpoints assessed separately from sampling coverage;
- do not increase B/K or change acceptance limits after seeing coverage outcomes.

Use independent seed namespaces for dataset generation, each bootstrap method, parametric simulation and any inner numerical calibration. Common datasets provide paired method comparison; independent random streams prevent method-specific RNG coupling.

## 5. Required outcomes and diagnostics

For each cell × method × target:
- empirical coverage and 95% Wilson interval;
- Monte Carlo standard error of coverage;
- lower-tail and upper-tail miss rates separately;
- bias, RMSE and median absolute error of component point estimates;
- mean, median and quantiles of interval width;
- interval endpoint Monte Carlo error for bootstrap methods;
- raw negative-between frequency and bootstrap boundary fraction;
- abstention / non-convergence / non-finite rates with typed reasons;
- BCa acceleration and bias correction, or studentizer diagnostics where relevant;
- computational cost and peak-memory estimate;
- coverage conditional on emission **and** unconditional usable-interval rate.

A conditional coverage result cannot pass if the method abstains too often. Report the joint operational performance: probability of emitting a valid interval and probability that the emitted interval covers, with a prespecified minimum emission rate. Do not conceal abstentions by reporting conditional coverage alone.

For a family-level disposition, every required cell must pass its predeclared criterion. No averaging across cells, components or methods can rescue a failed cell.

## 6. F5-specific caution

F5's current beta22 generator has `p_m~Beta(2,2)`, then `q_{mr}|p_m~Bernoulli(p_m)`. Its marginal moments are:
`E[p_m]=1/2`,
`E[p_m(1-p_m)]=1/5`,
`Var(p_m)=1/20`.

The conditional within and between variance targets are therefore not the same as a Gaussian variance-components likelihood. The fitted beta-binomial procedure must estimate the hyperparameters from the M world clusters and preserve finite R information. The oracle-known parameter procedure is only a best-case reference. Include sensitivity to sparse p, overdispersion and misspecified mixing distributions before generalizing.

## 7. Implementation sequence — one integrated work package

1. **Independent formula/oracle module:** implement F1 exact chi-square pivots, constrained Gaussian likelihood and F5 moment/likelihood oracles in a module separate from the production analyzer.
2. **Common comparison interface:** each candidate accepts one immutable dataset and returns typed estimates, intervals, boundary diagnostics, abstention reason and provenance. No candidate may mutate or filter input rows.
3. **Candidate implementations:** C1 first; then C2; then C3/C4 only if the required acceleration/studentizer is mathematically and computationally defensible; C5 built as a joint functional procedure.
4. **Adversarial unit tests:** negative raw between values, exact zero components, M=2, M=3, tied data, all-same-cluster bootstrap draws, BCa undefined acceleration, studentizer zero, boundary MLE, unbounded profile interval, F5 all-zero/all-one and sparse outcomes.
5. **Deterministic micro-simulation:** verify formula correctness and method determinism on small K/B only. These tests are software/oracle tests, not coverage validation.
6. **Resource benchmark:** estimate full holdout runtime/memory before fixing K/B.
7. **New protocol version and authorization:** only after design review and successful static/micro tests. The new version must explicitly supersede neither protocol v002 nor its historical result; it defines a new method-comparison validation.

## 8. Acceptance and selection rule

A candidate is eligible for selection only if:
- all algebraic/oracle invariants pass;
- no silent truncation, positive-only conditioning or untyped abstention occurs;
- each regular holdout cell meets the predeclared coverage and Wilson criterion;
- boundary cells meet their separately predeclared coverage/abstention/interval-existence requirements;
- operational emission rate is adequate and declared in advance;
- interval width is not unacceptably conservative relative to the Gaussian reference;
- the procedure is robust to the declared F5 discrete model and specified misspecification tests;
- reproducibility and runtime requirements pass.

If no candidate meets all conditions, the correct outcome is no validated general-purpose method. A model-specific Gaussian procedure may be reported as bounded F1-only evidence but cannot be generalized to arbitrary C10-S metrics.

## 9. Current state and next operation

| Item | State |
|---|---|
| Protocol v002 baseline | FROZEN; historical result NOT_VALIDATED |
| Tier A artifact | EXECUTED; integrity checked; not a holdout |
| F1 exact within pivot | ORACLE + ADDITIVE C1 CANDIDATE IMPLEMENTED; NEW C1 TESTS NOT RUN |
| F1 conservative between pivot | ORACLE + ADDITIVE C1 CANDIDATE IMPLEMENTED; RAW INTERVAL NOT CLIPPED |
| Gaussian profile/joint MCSE | PROFILE FUNCTION EXISTS; ADDITIVE C1 USES BONFERRONI JOINT-SET PROJECTION; NEITHER HAS CALIBRATED CUTOFF |
| Parametric / BCa / studentized comparison | DEFINED HERE; NOT IMPLEMENTED |
| F5 fitted beta-binomial inference | OPEN |
| New holdout protocol | OPEN |
| Tier B | NOT AUTHORIZED |
| C10 scientific execution | NOT AUTHORIZED |

**Progress recorded (2026-11-19):** additive F1 candidate `c10s_f1_exact_pivotal_candidate.py` and its deterministic contract tests `test_c10s_f1_exact_pivotal_candidate.py` were added. The tests have NOT been run. The candidate consumes the existing immutable comparison interface, preserves raw between estimates/intervals, rejects non-F1 family labels, and projects the Bonferroni joint confidence region to target MCSE by checking its polygon vertices. No new coverage simulation, technical test run, or workflow dispatch was performed. Independent F1 oracle module `c10s_gaussian_variance_oracles.py` and seven adversarial tests were added on the research branch. GitHub Actions run `44451657996` completed SUCCESS; compile passed and all 7 tests passed. The tests cover exact/joint-pivot interval construction, preservation of a negative raw lower endpoint, constrained MLE at the zero-between boundary, interior MLE reconciliation, finite profile MCSE likelihood-ratio output and fail-closed invalid support. This is static/formula-contract evidence only; it is not coverage calibration, method validation, or a numerical Monte Carlo run. The profile-likelihood implementation currently returns a profile LR statistic; its cutoff calibration and interval inversion remain OPEN.\n\n**Next operation (updated 2026-11-19):** connect the common result contract to the first candidate interval methods, beginning with the F1 exact/pivotal reference and a fitted (not oracle-known) F5 beta-binomial parametric-bootstrap implementation. Add fit convergence, boundary and failure diagnostics; retain the oracle-known F5 moments solely as an upper-bound reference. In parallel, complete the F1 profile-likelihood interval-inversion design without selecting a cutoff. Any cutoff calibration, coverage simulation, holdout execution or Tier B work remains blocked pending explicit numerical-calibration authorization and a separately frozen execution contract. Keep all work on a research branch. Do not alter the production Analyzer, protocol v002, canonical main, RMA, Evidence→Claim Matrix or scientific authorization state.


**Follow-up formula audit (2026-11-19):** review of the C1 Bonferroni construction found that the `within` interval had been computed at 95% marginal confidence while the `tau` interval used 97.5%. Their joint coverage was therefore not guaranteed to reach the declared 95% level by the stated Bonferroni argument. Corrected both marginal intervals to error `alpha/2` (two-sided tail `alpha/4`), preserving the untruncated raw-between combination. Added a regression test checking the exact chi-square quantiles. Added a separate deterministic dense-feasible-grid comparison for the MCSE profile likelihood with `R*≠R`. GitHub Actions run `44452473062` completed SUCCESS on commit `3b0858b87ac36f3e20d63856136fd27e0d7992bf`; compilation and all 9 comparator tests passed. This is formula/software verification only; no Monte Carlo calibration, cutoff selection, interval coverage simulation, Tier B or scientific C10 execution was performed. Calibration remains unauthorized under the C10-S mission contract.


**F5 beta-binomial oracle implementation (2026-11-19):** added `c10s_beta_binomial_variance_oracles.py`, an independent finite-sample oracle for the frozen F5 hierarchy (p_m\sim Beta(\alpha,\beta)), (X_m\mid p_m\sim Binomial(R,p_m)), (q_m=X_m/R). It computes the exact beta-binomial PMF on (X=0,\ldots,R), the population components (\sigma_w^2=\alpha\beta/[s(s+1)]) and (\sigma_b^2=\alpha\beta/[s^2(s+1)]), observed world-mean variance (\sigma_b^2+\sigma_w^2/R), target MCSE, and finite-M variances/covariance for the within estimator, observed world-mean sample variance and untruncated raw between estimator. Five deterministic tests include beta22 reconciliation (0.20/0.05; observed world-mean variance 0.09 at R=5), PMF normalization, exhaustive enumeration of all count configurations for M=3/R=2 against the analytic estimator moments, asymmetric beta parameters and fail-closed invalid support. The isolated static workflow compiles and runs both F1 and F5 oracle suites. GitHub Actions run `44452812636` completed SUCCESS on commit `9b81ac49ac51699af0c0d9426cbc0873c1354901`; compilation passed and all 14 tests passed (9 F1 + 5 F5). The F5 exhaustive-enumeration test matched the analytic finite-M estimator moments and covariance.

This oracle supplies exact moments and a finite-sample count law, not F5 confidence intervals, profile likelihood, cutoff calibration, bootstrap coverage or method selection. In particular, F5 inference must not reuse Gaussian pivots. No calibration or scientific execution is authorized or performed.


**Common comparison interface implementation (2026-11-19):** added `c10s_variance_comparison_interface.py` with a frozen typed result contract for common observed-data estimates, optional candidate intervals, boundary flags, typed abstention and provenance. The shared adapter computes within, observed world-mean variance and the untruncated raw between estimate from one rectangular immutable M×R dataset; optional MCSE projection returns `NONPOSITIVE_PROJECTED_VARIANCE` rather than clipping a negative value. Five adversarial tests cover hand calculation, negative raw between/abstention, input immutability, exact degeneracy and invalid shapes/values. Isolated workflow run `44452995537` completed SUCCESS on commit `f007310f85c6f4ab0b69f70c0472478f47ba78b4`; compilation passed and all 19 tests passed (9 Gaussian oracle + 5 beta-binomial oracle + 5 common-interface tests). This remains deterministic software/formula verification only.


**F5 fitted beta-binomial parametric-bootstrap candidate (2026-11-19):** implemented `c10s_fitted_beta_binomial_bootstrap.py`. It fits the two-parameter beta-binomial random-effects law by multi-start maximum likelihood in mean-logit/log-concentration coordinates, with fail-closed treatment for all-zero/all-one samples, no between-cluster count variation, optimizer non-convergence and numerical-boundary solutions. The fitted model generates independent world probabilities and R Bernoulli observations for each parametric replicate; the complete raw nested M/R component estimator is recomputed for every replicate. Raw between draws are retained without truncation. Percentile intervals for within and raw between are returned alongside an MCSE interval only when the predeclared minimum valid projected-draw rate is met; otherwise the MCSE interval is withheld with a typed abstention. Fit parameters, likelihood, seed, PCG64, replicate count, valid-draw rate and interval method are carried in provenance.

Five initial deterministic tests passed in GitHub Actions run `44453532266` (24 total comparator tests) on commit `eaab7c95c174d7d12a5222d6c9639ee541bcb6d4`. Subsequent hardening explicitly abstains when every world has the same non-boundary count and selects the best successful finite optimizer result among three starts; an additional regression test was added. The post-hardening run `44453677594` completed SUCCESS on commit `52d93b5ab9b4ded9dd49b3cea5da1318204a523d`; compilation passed and all 25 tests passed. This is deterministic software/formula verification only.

This candidate is a fitted-model exploratory percentile bootstrap, not calibrated inference. The finite B used in deterministic tests checks reproducibility and plumbing only. It does not establish interval coverage, alpha/beta estimator quality, robustness under misspecified mixing distributions, adequate emission rate, or suitability for C10-S dimensioning. Oracle-known F5 parameters remain a separate best-case reference and are not used to fit this candidate. No calibration, holdout, Tier B or scientific C10 execution was performed.

**Progress update (2026-11-19):** implemented the unified orchestrator `c10s_nested_mr_comparative_inference_engine.py` and deterministic contract suite `test_c10s_nested_mr_comparative_inference_engine.py`. The engine dispatches F1 to C1 and independently reconciles its raw-between interval against `gaussian_f1_reference`; dispatches F5 to the fitted beta-binomial candidate only when explicit B and seed are supplied; and always retains C0 as the point-only common baseline. C2-C4 are explicitly marked unavailable. Its adjudicator reports point bias/RMSE/emission, interval emission, conditional coverage, unconditional usable-and-covering rate, tail miss rates, interval width, typed non-emissions, coverage MCSE and Wilson 95% limits. It rejects mixed-family batches, mismatched target designs and invalid truth targets. Six deterministic engine tests were executed as part of the 36-test GitHub Actions static suite and passed. Run 15 (`44456441892`) on commit `478ee8033828ac5cdd773cb3cd6f397162fc11bb` completed SUCCESS: pinned dependencies installed, compilation passed, and all 36 tests passed. The first run exposed an incorrect expectation in the F1 negative-between boundary test; inspection confirmed the candidate's empty feasible joint confidence set and MCSE abstention were correct, so the test was corrected to assert that typed abstention. The rerun passed. This remains static/deterministic software evidence only; it is not coverage calibration or empirical inference validation. No calibration, holdout, Tier B, scientific C10 execution or main promotion was performed.

**Next operation:** design the numerical calibration/holdout protocol for C1 and C5, including DGP-specific operating characteristics, emission/abstention criteria and independent truth generation. This requires a separate explicit authorization; no Monte Carlo, calibration, Tier B, scientific execution or main promotion is authorized by the static-test approval. The authorization state in the mission record remains controlling: technical test execution, workflow dispatch, calibration, scientific execution and main promotion remain unauthorized.


**Comparative readiness audit and implementation (2026-11-19):** `C10S_COMPARATIVE_CALIBRATION_READINESS_AUDIT_001.md` identified six readiness issues. The integrated engine is now version 1.1: C0 calls the frozen v002 `analyze_nested_precision` implementation through a thin adapter, reconciles its within/raw-between/world-variance point targets against the common interface, and emits its original component/projection intervals; C5 no longer emits a positive-projection-conditioned MCSE interval and returns a typed abstention; the adjudicator reports separate B/K quantities and Wilson intervals for point emission, interval emission, conditional coverage and unconditional cover; and it enforces dataset/truth IDs, exact family-specific method roster, candidate identity and consistent input/target designs. GitHub Actions run 24 (`44457516440`) on commit `932ac429e85897430b9a42901533cb61cba6ac11` completed SUCCESS: compilation and all 39 deterministic tests passed. This remains static/formula-contract evidence, not coverage calibration.

**F5 MCSE next-method design (2026-11-19):** `C10S_F5_MCSE_PROFILE_LIKELIHOOD_DESIGN_001.md` specifies a candidate beta-binomial profile-likelihood interval for the scalar MCSE functional. The parameterization `(mu,kappa)` yields a one-dimensional profile reduction with both mean branches, explicit `kappa→0` and `kappa→infinity` limits, and finite-sample least-favourable LR cutoff calibration. The method is FORMULA-SPECIFIED only: no code, cutoff calibration, Monte Carlo or execution has occurred. A finite nuisance grid alone will not be described as uniform continuous-parameter coverage.

**Current disposition:** matched component comparator IMPLEMENTED / STATIC CI PASS 39/39. F1 MCSE can be compared C0-v002 vs C1. F5 within and raw-between can be compared C0-v002 vs C5. F5 MCSE remains NOT_IMPLEMENTED until the profile candidate is implemented, adversarially tested and calibrated. The original v002 Tier A result remains NOT_VALIDATED and is not a holdout. No numerical calibration, holdout, Tier B or scientific C10 execution is authorized by the static-test approval.


## 10. Comparative Tier A holdout protocol v1.0

**Status:** HOLDOUT DESIGN FROZEN FOR IMPLEMENTATION / NOT EXECUTED / NOT AUTHORIZED.  
**Purpose:** evaluate the corrected C1/C5 candidates against the unchanged C0-v002 baseline on fresh independent datasets. This is the successor evaluation to the failed original Tier A, not a rerun of protocol v002.

### 10.1 Frozen scope

The confirmatory comparison is restricted to the eight regular Tier A cells already defined in protocol v002:

- F1 Gaussian random-intercept: balanced `(sigma2_within,sigma2_between)=(1,1)`, low-between `(1,0.05)`, and high-between `(0.25,2)`, each at input designs `(M,R)=(10,5)` and `(30,20)`.
- F5 beta-binomial: `alpha=2, beta=2`, at the same two input designs.

No Tier B cells, added stress cells, C2-C4 methods, cross-family pooling, or C10 Generator/Analyzer/Evaluator execution are included.

The target design is `(M*,R*)=(M,R)` for each cell. Adjudication is performed separately for every cell; no pooling across cells, families, targets or methods is allowed.

### 10.2 Fixed method roster

- **C0:** exact frozen protocol-v002 two-stage percentile bootstrap, unchanged, with `B=1,000`.
- **C1 (F1 only):** exact Gaussian within pivot and conservative joint-pivot raw-between interval; its MCSE projection is retained as a model-specific F1 result. No Gaussian method is applied to F5.
- **C5 (F5 only):** fitted beta-binomial parametric bootstrap for within and raw-between components, with `B=1,000`. The fitted model is estimated from each observed dataset; oracle parameters are used only for independent truth, never for fitting.
- **F5 MCSE:** C5 emits the existing typed abstention `F5_MCSE_JOINT_BOUNDARY_METHOD_NOT_IMPLEMENTED`. This target is excluded from candidate acceptance and is not repaired by conditioning on positive projected draws. C0 F5 MCSE is reported descriptively with its emission/abstention rate only.
- **Profile-likelihood diagnostics:** F1/F5 profile evaluators and root/optimizer diagnostics are not candidate interval methods in this holdout. They are not run for every holdout dataset and do not enter coverage adjudication. Their implementation can remain available for separate, explicitly scoped diagnostics; no LR cutoff is selected here.

### 10.3 Replication and seed separation

- Independent datasets: `K=1,000` per cell.
- C0 bootstrap: `B=1,000` per dataset, exactly as frozen in v002.
- C5 parametric bootstrap: `B=1,000` per F5 dataset.
- Confidence level: 95%.
- Holdout seed namespace: cell IDs are prefixed `COMPARATIVE_HOLDOUT_V1__`; this changes the deterministic SHA-256 seed inputs and makes every dataset independent of the original Tier A development bank. Bootstrap streams are separately derived with method-specific cell suffixes `__C0` and `__C5`.
- The existing PCG64 generator and seed derivation are reused; no source Tier A dataset, seed, or bootstrap stream is reused. The exact seed schedule, code commit and all generated seeds are recorded in the run manifest.

**K rationale:** at nominal coverage 0.95 and K=1,000, the binomial Monte Carlo standard error is approximately 0.0069 (0.69 percentage points); the 95% Wilson half-width is approximately 1.35 percentage points. This is adequate to adjudicate the pre-existing 93%-97% coverage band without treating small deviations as exact.

**B rationale:** C0 retains B=1,000 because changing B would no longer reproduce the frozen v002 baseline. C5 also uses B=1,000 to keep its bootstrap Monte Carlo budget aligned with C0. For every percentile endpoint, the report additionally records the exact binomial order-statistic rank band for the 2.5% and 97.5% quantiles and the corresponding observed endpoint-value band. This endpoint Monte Carlo uncertainty is reported separately from sampling coverage; B is not increased or tuned after inspecting holdout outcomes.

### 10.4 Truth and adjudication

Truth is generated independently of the interval candidates:

- F1: `sigma2_within` and `sigma2_between` are the declared Gaussian DGP parameters.
- F5: for `Beta(2,2)`, `sigma2_within=0.20` and `sigma2_between=0.05`, from the independent beta-binomial oracle.
- For each cell, `MCSE(M*,R*)=sqrt(sigma2_between/M* + sigma2_within/(M*R*))`.

For every method × cell × target, retain point bias/RMSE, interval-emission rate, conditional coverage, unconditional usable-and-covering rate, lower/upper miss rates, interval width, Wilson 95% intervals, coverage MCSE, fit/convergence failures, typed abstentions, endpoint Monte Carlo uncertainty, runtime and complete provenance.

### 10.5 Prospective acceptance

- C0, C5, and C1-F1 within: empirical coverage must be in `[0.93,0.97]`, its 95% Wilson interval must contain 0.95, and interval emission must be at least 0.95 of K. Otherwise the cell is `NOT_VALIDATED`; conditional coverage cannot rescue low availability.
- C1-F1 raw-between and its MCSE projection are deliberately conservative joint-pivot results. They are adjudicated as **at-least-nominal conservative procedures**: the 95% Wilson lower bound must be at least 0.93, interval emission must be at least 0.95, and width/overcoverage are reported explicitly. They are not required to fall below 97%, and no efficiency claim is made.
- F5-C5 MCSE remains `NOT_IMPLEMENTED / ABSTAINED`; it receives no coverage pass or fail and cannot be represented as a calibrated MCSE interval.
- Each cell and target is adjudicated independently. A failed cell is not rescued by averaging, and no method is selected by a pooled score.

### 10.6 Interpretation and stopping rule

The original Tier A v002 run remains immutable development evidence and remains `NOT_VALIDATED`; it is not part of the holdout denominator. This holdout tests the new candidates on fresh data and does not rewrite protocol v002.

No tuning, candidate replacement, cutoff selection, K/B change, seed change, or tolerance adjustment is permitted after holdout outcomes are inspected. If no candidate meets its declared criteria, the result is `NO_VALIDATED_METHOD_FOR_THAT_SCOPE`; any subsequent method change requires a new prospective protocol and a new independent seed namespace.

This holdout is numerical-method calibration only. It does not execute C10-S Generator/Analyzer/Evaluator, does not validate the actual C10-S M/R sampling assumptions, and does not establish the causal contribution of `Delta T_acc` to Value. Tier B and scientific C10 execution remain separately unauthorized.

**Next operation:** implement the bounded holdout runner and its fail-closed authorization/workflow by reusing the existing fixture generator, comparison engine and adjudicator. Do not rerun Tier A v002. Do not execute this holdout until its exact code/protocol hashes are frozen and a separate one-shot authorization is explicitly granted.
