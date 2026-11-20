# C10-S — F5 comparative interval-method design draft 001

**Status:** DESIGN DRAFT — NOT FROZEN / NOT IMPLEMENTED / NOT EXECUTED  
**Date:** 2026-11-20  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Scope:** coordinated statistical design for F5 within and raw-between interval estimation  
**Historical evidence:** B2/B3 run `44615173745`, artifact `14586221304`  
**Frozen development specification:** v1.0 unchanged  
**Execution authorization:** NONE  
**Decision:** no candidate method selected

---

## 1. Executive design decision

Compare three interval constructions without selecting a winner from historical B2/B3:

- **M0 — fixed-parameter plug-in parametric bootstrap:** current C5; alpha/beta estimated once and held fixed in all bootstrap draws.
- **M1 — refitted parametric bootstrap:** generate each nested dataset under the fitted beta-binomial law, refit alpha/beta in every replicate using the declared estimator, then recompute the target functional.
- **M2 — profile-likelihood inference:** construct likelihood-based confidence sets for the target functional by profiling nuisance parameter(s), with explicit treatment of boundaries and nonregularity.

C0 is retained only as a matched historical diagnostic comparator, not as a candidate or acceptance fallback. No method is selected, tuned, or promoted by this draft. M0 is the incumbent baseline; M1 and M2 are design candidates whose validity must be demonstrated prospectively.

The central scientific issue is not merely interval width. The method must represent uncertainty in the fitted concentration and its induced covariance with the target components, while remaining honest when concentration is weakly identified or the likelihood reaches a boundary.

## 2. Historical reconstruction and constraints

### 2.1 Relevant established work

- F5 B1 implementation and deterministic tests are complete; direct production P versus analytic-gradient reconciliation is implemented and statically validated.
- Historical B2/B3 are executed and audited, but C5 fails all eight frozen component gates; C0 also fails its complete frozen gates.
- The B2/B3 banks are development evidence only and cannot be reused to select, tune, or claim validation of M1/M2.
- The existing B2 artifact has four 5,000-row calibration/validation banks, immutable bank hashes and a verified artifact digest.
- Historical C5 bootstraps from one fitted alpha/beta pair and does not refit those parameters in each bootstrap replicate.
- M30/R20 top fitted-concentration decile exhibits severe conditional C5 undercoverage and directional misses. This is exploratory post-fit evidence, not a new acceptance stratum.
- M10/R5 has a separate weak-identification/near-binomial ridge problem. It must not be conflated with the M30/R20 interval-construction issue.
- MCSE interval construction is explicitly excluded and must remain an abstention.

### 2.2 Non-negotiable constraints

1. Frozen development specification v1.0, B2/B3 outputs, historical adjudications and acceptance gates remain unchanged.
2. No retrospective PASS, no post-hoc concentration cutoff, no selection based on the historical top decile, and no B2/B3 method tuning.
3. C5 production point-estimator semantics remain fixed for the comparison unless a separately versioned decision changes them.
4. C0 cannot be declared a valid fallback because its historical full gates failed.
5. No new simulation, bootstrap, calibration, preflight or scientific execution is authorized by this design.
6. Any prospective method comparison requires a separately authorized, fresh and disjoint development bank; confirmatory evidence requires another disjoint bank and its own authorization.

## 3. Estimands and statistical parameterization

Let the latent world probability be (p_jsimmathrm{Beta}(\alpha,\beta)), and conditional observations be (X_jmid p_jsimmathrm{Binomial}(R,p_j)). Define:

- (\mu=\alpha/(\alpha+\beta)), the mean world probability;
- (\kappa=\alpha+\beta), the concentration;
- (\operatorname{logit}(\mu)=\eta), (\log(\kappa)=\lambda).

The two F5 targets are the population variance components:

[
W(\mu,\kappa)=E[p(1-p)]
=\mu(1-\mu)\frac{\kappa}{\kappa+1},
]

[
B(\mu,\kappa)=\operatorname{Var}(p)
=\frac{\mu(1-\mu)}{\kappa+1}.
]

They satisfy (W+B=\mu(1-\mu)). The comparison must preserve the frozen mapping between these population targets and the actual within/raw-between estimators and reported coverage endpoints. The identities above are the model functionals; they do not authorize replacing the frozen estimators or redefining the raw-between target.

For every method, report intervals separately for W and B. Also retain the joint geometry of (W,B), because the shared ((\mu,\kappa)) estimate induces dependence and the two components are not independent. Marginal 95% intervals do not imply 95% simultaneous coverage of the pair.

### 3.1 Boundary geometry

- (\kappa\to0): the beta distribution approaches a two-point mixture at 0 and 1; W tends to 0 and B tends to (\mu(1-\mu)).
- (\kappa\to\infty): the beta-binomial approaches the binomial limit; W tends to (\mu(1-\mu)) and B tends to 0.
- (\mu\to0) or (1): both components approach 0 and ordinary interior asymptotics can fail.
- The transformation between ((\alpha,\beta)) and ((\eta,\lambda)) must be applied consistently, with explicit numerical handling of finite optimizer bounds versus theoretical limits.

A method must not return a deceptively narrow interval merely because an optimizer stopped at a finite numerical bound. The output must distinguish an estimated finite parameter, a boundary-supported likelihood, a numerically unresolved fit, and an interval whose endpoint is determined by the parameter-space boundary.

## 4. Candidate M0 — fixed-parameter plug-in bootstrap (incumbent)

### 4.1 Algorithm

1. Fit the frozen beta-binomial estimator once to the observed nested data, obtaining ((\hat\mu,\hat\kappa)) or ((\hat\alpha,\hat\beta)).
2. Hold this fitted pair fixed.
3. Generate latent world probabilities from the fitted beta law and nested binomial counts using the frozen data-generation hierarchy.
4. Recompute the frozen within and raw-between estimators for each replicate.
5. Construct the existing percentile intervals exactly as frozen C5 defines them.

### 4.2 Statistical meaning

M0 approximates the conditional sampling distribution of the nested estimators under one fitted latent law. It does not include the repeated-sampling distribution of the fitted concentration estimator because it does not refit alpha/beta within bootstrap replicates.

M0 remains necessary as the baseline and must be reproduced bit-for-bit or within the existing deterministic contract on a future disjoint bank. It is not currently validated and cannot be treated as a default accepted method.

### 4.3 Required diagnostics

Record the fixed parameter pair, boundary distances, optimizer states, bootstrap distribution of W/B estimators, interval widths and endpoint/miss directions. Separate conditional estimator variability from parameter-estimation variability; M0 contains only the former by construction.

## 5. Candidate M1 — refitted parametric bootstrap

### 5.1 Algorithm

For each observed dataset:

1. Fit the frozen beta-binomial likelihood once, using the frozen production estimator and start schedule, to obtain generating parameters (hat\theta=(\hat\mu,\hat\kappa)).
2. For each bootstrap replicate (b), generate a complete nested dataset under (hat\theta), preserving the original number of worlds, within-world replication, allocation, missingness/weighting rules if any, and all design features of the frozen DGP.
3. Refit the beta-binomial model to that replicate using the same estimator, parameterization, bounds, starts, convergence diagnostics and selection semantics as the observed-data fit.
4. Compute (W(\hat\theta_b^*)), (B(\hat\theta_b^*)), and any frozen sample-estimator targets required for direct comparability.
5. Construct marginal intervals using a single interval rule declared before the prospective bank. The initial design comparison should report percentile intervals for the refitted functionals and a clearly labelled centered/basic sensitivity analysis; the latter must not replace the primary interval after outcomes are seen.
6. Retain every replicate's raw fit state and all failed/ boundary/indeterminate outcomes. Never silently discard failed fits or replace them with successful draws.

### 5.2 What M1 adds and what it does not guarantee

M1 can propagate the sampling variability of alpha/beta estimation into W/B. It is a plausible response to the fixed-parameter omission identified in C5. It is not automatically valid under weak identification, nonregular boundaries, model misspecification, or frequent optimizer failure. A parametric bootstrap generated from a single unstable (hat\theta) can reproduce the wrong local regime and can fail to approximate the estimator's true sampling distribution.

### 5.3 Failure and boundary semantics

Every replicate must be assigned exactly one mutually exclusive terminal state, at minimum:

- `INTERIOR_FIT_SELECTED`;
- `BOUNDARY_LIMIT_SELECTED`;
- `MULTISTART_DISAGREEMENT`;
- `OPTIMIZER_TERMINATION_UNRESOLVED`;
- `NO_ADMISSIBLE_FIT`;
- `NUMERICAL_EXCEPTION`.

The exact state vocabulary must be reconciled with the implemented B1 typed diagnostics before implementation; this list is a proposed design schema, not a claim that the current code already emits these states.

The interval algorithm may not condition silently on only successful replicates. The design must prespecify whether any non-interior state causes dataset-level abstention, a boundary-aware set-valued contribution, or another mathematically justified treatment. Simple complete-case deletion is prohibited because it changes the bootstrap distribution in a data-dependent way. If a principled boundary contribution cannot be specified, the method must abstain and report the failure fraction and state counts.

### 5.4 Required diagnostics

For each original dataset and bootstrap bank retain:
- requested and completed replicate counts;
- counts by terminal state;
- distributions of (hat\mu^*), (hat\kappa^*), W*, B*;
- boundary-contact and optimizer-start concordance summaries;
- marginal interval endpoints and widths;
- whether endpoints are finite, boundary-determined or unresolved;
- Monte Carlo uncertainty of each endpoint and coverage estimate;
- computational cost, wall time and peak memory.

## 6. Candidate M2 — profile-likelihood intervals for W and B

### 6.1 Core construction

Let (ell(\theta)) be the frozen beta-binomial log-likelihood with (\theta=(\eta,\lambda)), and let (hat\theta) be the globally admissible maximum-likelihood estimate under the frozen parameter space.

For target (\psi(\theta)), where (\psi=W) or (B), define the profile log-likelihood:

[
\ell_p(\psi_0)=
\sup_{\theta:\,\psi(\theta)=\psi_0}\ell(\theta).
]

The likelihood-ratio statistic is:

[
D(\psi_0)=2\{\ell(\hat\theta)-\ell_p(\psi_0)\}.
]

An interval is obtained by inverting the accepted likelihood-ratio set over the feasible target range. The nuisance parameter is profiled, not fixed at its point estimate. The implementation must retain disconnected accepted sets if the profile is non-concave or multimodal; it must not force them into one interval without an explicit conservative hull rule.

### 6.2 Calibration

The usual chi-square cutoff is only a regular asymptotic reference. It cannot be assumed valid at the κ boundaries, near the binomial limit, under weak identification, or when the MLE is non-unique.

Therefore M2 has two separately labelled calibration variants:

- **M2a — asymptotic profile LR:** diagnostic/reference only, with its regularity assumptions explicitly reported.
- **M2b — calibrated profile LR:** calibrate the likelihood-ratio statistic under constrained null values using a parametric bootstrap with constrained and unconstrained refits. This is computationally more expensive and inherits the same refit/boundary failure obligations as M1.

M2b is not a free validation oracle: calibration must be prospective and prespecified. It must not be tuned on the B2/B3 observed coverage failures.

### 6.3 Boundary and numerical semantics

- Evaluate the theoretical κ→0 and κ→∞ likelihood limits explicitly where supported by the frozen likelihood contract.
- Distinguish a true boundary supremum from a finite optimizer bound.
- Retain profile branches and all nuisance optimizer outcomes at each target value.
- Do not interpolate across failed profile points as if they were valid likelihood values.
- Report disconnected sets, non-finite profile regions and unresolved target endpoints explicitly.
- If the global maximum cannot be established or the profile cannot be traced reliably, return an indeterminate/abstention state rather than a finite interval with false precision.

## 7. Coordinated comparison matrix

| Dimension | M0 fixed plug-in | M1 refitted parametric bootstrap | M2 profile likelihood |
|---|---|---|---|
| Re-estimates alpha/beta per replicate | No | Yes | Nuisance refit at each target value |
| Propagates fitted-parameter variability | No, conditional | Intended to | Through profile set |
| Weak-identification behaviour | Can be falsely narrow | May be unstable/nonregular | Exposes flat/disconnected profiles |
| Boundary handling | Fixed fitted pair; inherited fit issue | Must classify each replicate | Explicit feasible profile boundaries |
| Optimizer burden | One fit + cheap estimator replicates | One fit per replicate | Many constrained optimizations; M2b adds bootstrap calibration |
| Main risk | Understates parameter uncertainty | Bootstrap inconsistency / failed refits | Incorrect LR calibration / incomplete profile |
| Output on unresolved fit | Current frozen abstention | Prespecified abstention or valid boundary set | Indeterminate profile / abstention |
| Current evidence status | Implemented, historically failed gates | Design candidate only | Design candidate only |

C0 is not included as a fourth candidate. It may appear as a diagnostic comparator on the same future datasets, labelled non-candidate, until independently validated.

## 8. Prospective evaluation design — requirements before any new bank

### 8.1 Data partitioning

- Preserve historical B2/B3 as development evidence only.
- Create a new, disjoint method-development bank only after this design is reviewed, frozen and separately authorized.
- Reserve a second independent bank for confirmatory evaluation after method selection and freeze.
- Define DGP cells, parameter grid, seeds, sample sizes and exclusions before generating either bank.
- Stratify design coverage across interior concentration, near-binomial weak-identification, low-concentration/two-point-limit, mean-probability extremes, and the previously problematic M30/R20 regime. Strata are design factors defined before outcomes, not post-fit deciles.
- Keep calibration and validation banks disjoint at dataset/seed level and preserve exact hashes.

### 8.2 Primary performance outcomes

For W and B separately, and for every prespecified DGP cell/bank:
1. empirical marginal coverage at the frozen nominal level;
2. Wilson or other frozen binomial uncertainty interval for coverage;
3. median and distribution of interval width;
4. lower- and upper-tail miss rates, including directional imbalance;
5. interval endpoint bias and boundary frequency;
6. abstention and unresolved-fit rates;
7. Monte Carlo standard error for coverage and endpoint summaries;
8. computational cost per original dataset and per interval.

Do not pool cells or targets to rescue a failing component. Report the joint (W,B) coverage as a separate secondary outcome; do not substitute it for the frozen marginal component gates.

### 8.3 Acceptance and selection

- The frozen v1.0 component acceptance criteria remain controlling unless a separately approved decision explicitly supersedes them before prospective data generation.
- Apply the complete gate independently by cell, bank and target; no average/pooled PASS.
- Coverage alone is insufficient: report width and miss direction, but do not introduce an unapproved width optimum.
- Abstention is not silently counted as coverage or removed from the denominator. Report both unconditional operational success/abstention and conditional coverage among eligible intervals; the acceptance rule for each must be frozen in advance.
- Method selection must be based on the prespecified development bank only. The selected method and all tuning decisions are then frozen before the confirmatory bank is generated or opened.
- Confirmatory failure cannot be repaired by tuning on the confirmatory bank.

### 8.4 Monte Carlo precision

Choose the number of datasets per cell from a prospective precision calculation for the coverage estimate and its Wilson interval, not by copying B2/B3 sample sizes. Choose bootstrap replicates per dataset from an endpoint Monte Carlo error study performed in a separate deterministic/statistical pilot, not by increasing B after inspecting coverage.

For coverage (hat p) across (N) independent datasets, report (\sqrt{\hat p(1-\hat p)/N}) as a descriptive MCSE alongside the prespecified binomial interval. For bootstrap quantile endpoints, estimate Monte Carlo error using a declared quantile/endpoint procedure and retain convergence traces. The required precision targets are OPEN and must be numerically specified before bank generation.

### 8.5 Cost model

Before authorizing the prospective bank, estimate:
- M0 cost: approximately one model fit plus B estimator-only replicates per dataset;
- M1 cost: approximately one generating fit plus B model refits per dataset;
- M2a cost: number of profile target evaluations × nuisance optimizer starts per dataset;
- M2b cost: M2a plus null-bootstrap replicates × constrained/unconstrained fits.

Use measured static microbenchmarks on deterministic fixtures only after implementation; no benchmark is claimed by this design. Include worst-case boundary/abstention paths, not just median interior fits. Set a compute budget and stopping policy before numerical execution.

## 9. Required deterministic and analytical validation before implementation freeze

No Monte Carlo coverage run is required at this stage. The implementation design must first pass deterministic tests:

1. **Moment identities:** known W/B values for symmetric and asymmetric beta parameters; verify W+B=μ(1−μ).
2. **Boundary limits:** κ→0 and κ→∞; μ→0/1; continuity where mathematically expected and explicit nonregular states where not.
3. **Parameterization invariance:** equivalent alpha/beta and eta/lambda representations yield identical likelihood and target functionals.
4. **M0 reproduction:** current C5 output unchanged on fixed fixtures.
5. **M1 refit propagation:** constructed fixture where parameter uncertainty changes W/B spread; verify refitting occurs and is recorded for every replicate.
6. **M1 failures:** deterministic mocked optimizer outcomes for interior success, boundary selection, failed starts, disagreement and exception; verify no silent deletion.
7. **M2 profile correctness:** compare profile likelihood against analytically tractable or high-precision reference fixtures; verify constrained optimum never exceeds unconstrained global optimum beyond numerical tolerance.
8. **M2 topology:** disconnected profile sets, boundary endpoints and non-finite/failed profile points remain explicit.
9. **Coverage bookkeeping:** exact denominators, abstentions, directional misses and Wilson calculations on small deterministic fixtures.
10. **Serialization/provenance:** every dataset, replicate, optimizer result, method version and random stream is traceable.

Tolerances for deterministic numerical tests must be scale-aware and justified by the analytic fixture and floating-point error analysis. They are not statistical acceptance thresholds.

## 10. Implementation architecture and shared components

To avoid three disconnected implementations, use a shared frozen interface:

- `FitResult`: selected parameters, complete start roster, likelihood, gradient/Hessian diagnostics, boundary state and typed terminal status.
- `TargetFunctional`: W/B evaluation and feasible target range from a parameter vector.
- `NestedDataGenerator`: one canonical generator implementing the frozen hierarchy and deterministic stream identity.
- `IntervalMethod`: common input/output contract; method-specific implementation for M0, M1 and M2.
- `IntervalResult`: endpoints or set-valued region, target, method/version, terminal state, replicate/profile counts, failure/abstention reasons and MCSE.
- `MethodComparisonRecord`: same dataset ID and data hash across methods, paired output comparison, source/config hashes and provenance.

The existing C5 point estimator and historical M0 implementation must be wrapped, not silently rewritten. M1 must call the same frozen fit contract for each replicate. M2 must call the same likelihood and optimizer diagnostics while adding constrained profiling. Any required change to the fit contract is separately versioned.

## 11. Decision gates and work sequence

| Gate | Deliverable | Permitted disposition |
|---|---|---|
| D0 — design review | This draft reconciled with frozen v1.0, exact target semantics and governance | ACCEPT / REVISE / BLOCK |
| D1 — formal method specification | Fully specified M0/M1/M2 algorithms, failure semantics, interval rules, precision and cost targets | FREEZE or return to D0 |
| D2 — deterministic implementation | Shared interfaces, M1/M2 implementations, adversarial tests | PASS_STATIC / CONDITIONAL / NOT_VERIFIABLE |
| D3 — prospective development authorization | Separate one-use authorization, new disjoint development bank and resource budget | AUTHORIZE / BLOCK |
| D4 — development audit | Per-cell results, component gates, widths, misses, abstentions, cost | Select one method or no method |
| D5 — freeze and confirmatory authorization | Frozen selected method and independent confirmatory plan | AUTHORIZE / BLOCK |
| D6 — confirmatory audit | Independent results and complete gate disposition | ACCEPT / FAIL / INCONCLUSIVE |

No gate is implicitly passed by completion of a prior one. The current state is D0 draft.

## 12. Open design questions requiring resolution before D1

1. Does the frozen target require intervals for the population functionals W/B, the finite-sample raw estimators, or both as separate outputs? The frozen C5 estimator-to-target mapping must be quoted and reconciled, not inferred.
2. Should M1's primary interval be percentile on refitted W*/B*, or should a centered/basic construction be primary? The choice must be justified before data.
3. What is the mathematically defensible treatment of non-interior and failed bootstrap refits: dataset abstention, set-valued boundary contributions, or another method?
4. Should M2b use a bootstrap-calibrated likelihood-ratio cutoff for each target value, and how will Monte Carlo uncertainty in that cutoff be controlled?
5. Is a joint confidence region for (W,B) required as a formal secondary criterion, given W+B=μ(1−μ)?
6. What coverage precision and endpoint MCSE targets are required, and what computational ceiling is acceptable?
7. Which parameter-space boundaries are theoretical model boundaries versus finite optimizer safeguards in the frozen implementation?
8. How should method comparison treat DGP/model misspecification, given all three candidates are parametric or likelihood-based under the same beta-binomial family?

These are design questions, not requests to the user for immediate preference. They should be resolved from the frozen specification and statistical analysis, then recorded in a single integrated D1 specification.

## 13. Current disposition

- **M0:** IMPLEMENTED / HISTORICALLY EXECUTED / FAILED FROZEN C5 COMPONENT GATES.
- **M1:** DEFINED AT DESIGN LEVEL / NOT IMPLEMENTED / NOT EXECUTED.
- **M2a/M2b:** DEFINED AT DESIGN LEVEL / NOT IMPLEMENTED / NOT EXECUTED.
- **C0:** HISTORICAL DIAGNOSTIC COMPARATOR ONLY / NOT VALIDATED.
- **B2/B3:** HISTORICAL DEVELOPMENT EVIDENCE ONLY / NOT REUSABLE FOR METHOD SELECTION.
- **Design D0:** OPEN — review and reconcile target semantics and exact frozen acceptance language.
- **Execution:** NOT AUTHORIZED.

**Recommended next operation:** recover the exact frozen v1.0 specification and C5 estimator-target mapping from the canonical repository, resolve the open estimand/interval/failure semantics in this draft, and produce D1 as a single integrated, versioned method specification. Do not implement M1/M2 or generate any data until D1 is frozen and a separate execution authorization exists.
