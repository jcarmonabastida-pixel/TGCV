# C10-S F5 — G7 prospective Tier-A calibration protocol 002

**Record:** C10S-F5-G7-TIERA-PROSPECTIVE-001  
**Version:** 1.1  
**Status:** DRAFT FOR DETERMINISTIC SOFTWARE VALIDATION — G7 HOLDOUT NOT AUTHORIZED  
**Scope:** F5 beta-binomial Tier-A relevance and coverage only  
**Parent:** F5 end-to-end closure dossier G7; frozen Tier-A comparability criteria  
**Research branch:** `research/c10s-f5-g7-canonical-mle-v1.1-20261122`

## 1. Purpose and non-change boundary

This is a versioned implementation successor to G7 prospective protocol v1.0. It corrects the observed primary/replay instability by making the exact global likelihood certificate authoritative for the fitted beta-binomial parameter and by separating scientific replay records from raw optimizer diagnostics.

This remains an instrumental F5 calibration gate. It is not the C10 causal experiment and is not evidence for `ΔT_acc → Value`.

The v1.0 prospective bank in run [44969714756](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44969714756) is consumed and unblinded. Its 2,000 records and all summaries remain immutable historical evidence. They are excluded from G7 v1.1 denominators, calibration, threshold selection and coverage adjudication. The v1.0 run may be used only to diagnose the software/replay defect already identified in the separate replay audit.

The following scientific design elements remain unchanged from v1.0:
- exactly the same two beta(2,2) target cells: M10/R5 and M30/R20;
- K=1,000 per cell;
- C0 B=1,000 and C5 B=1,000;
- the same C0 frozen v002 matched baseline;
- the same C5 beta-binomial parametric percentile interval construction;
- the same within and untruncated raw-between targets;
- the same 95% nominal level, conditional-coverage bounds [0.93, 0.97], two-sided 95% Wilson inclusion rule and minimum 95% interval-emission rate;
- the same complete accounting, finite/ordered endpoint and no-pooling requirements;
- the same PASS / NOT_VALIDATED / INDETERMINATE dispositions.

No coverage threshold, estimator, interval formula, target cell, denominator or adjudication rule is relaxed.

## 2. Exact-certificate-first fitted beta-binomial method

The v1.0 ordering was unsafe: three finite-difference L-BFGS-B starts ran before the exact global-MLE certificate. If all starts reported failure, the procedure returned `MLE_NONCONVERGENCE` without allowing the exact certificate to classify the likelihood winner. This caused seven status reversals in the consumed v1.0 bank.

The v1.1 ordering is:

1. Construct the exact count histogram from the observed M×R Bernoulli rows.
2. Run `beta_binomial_global_mle_certificate` on that histogram before any floating-point optimizer.
3. If the exact certificate proves a global boundary supremum, global co-maximizers, or an unresolved/incomplete ordering, emit the corresponding typed abstention. A numerical optimizer may not override or relabel that disposition.
4. If the certificate proves one global interior maximum, use the rational Krawczyk root enclosure in `winner.parameter_box`. The canonical fit is the exact rational midpoint of that enclosure in compactified coordinates `(mu, t)`, with `t=kappa/(1+kappa)`. Convert this one deterministic representative to floating point only when constructing the beta-binomial bootstrap generator parameters.
5. The production certificate call uses the frozen census budgets `max_refinements=3`, `max_lift_depth=24` and `max_mu_depth=12`. After global ordering, each winning/competing interior root enclosure is refined with up to 12 exact rational Newton steps followed by a final exact Krawczyk inclusion/contraction proof on a candidate box. The root enclosure must have width no greater than (2^{-32}) on each of the `mu` and `t` axes. If that precision cannot be established, abstain with `GLOBAL_MLE_ROOT_BOX_PRECISION_INSUFFICIENT`; do not fall back to an optimizer-selected fit.
6. Only after the certificate has established an interior global maximum, run the three-start finite-difference L-BFGS-B fit and the independent analytic-gradient optimizer audit as diagnostics. Their parameters, success flags, messages and numerical diagnostics are retained but cannot select, veto or alter the canonical fit.

The exact likelihood ordering remains based on the existing rational probability enclosures and complete interior stationary/boundary/corner census. The midpoint is a deterministic numerical representative of the certified root enclosure, not a claim that the midpoint itself is an exact algebraic root.

Newton steps are only a deterministic locator; they do not certify a root. The final Krawczyk proof is mandatory, and the candidate box must be contained in the original certified enclosure. If no candidate box of the declared width passes Krawczyk certification, the method abstains.

The candidate method identity is versioned as `F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.1`. The v1.0 candidate identity is preserved historically.

## 3. Diagnostic sidecar and replay integrity

The scientific comparison record contains the observed estimates, emitted intervals, typed abstention, analytical truth pairing, seed/data identity, row digest, fit parameters derived from the certified root enclosure, and exact-certificate status. It does not contain optimizer telemetry.

All `CandidateOutput.diagnostics`, including the raw three-start L-BFGS-B outcomes, analytic-gradient optimizer audit, production/analytic reconciliation and diagnostic errors, are preserved in the shard's `optimizer_diagnostics` sidecar. Each sidecar has its own canonical JSON SHA-256 digest and exact dataset/method roster.

The replay gate requires:
- exact equality of scientific records and their `records_digest`;
- exact equality of scientific data/seed/truth/row identities;
- independent validation of each primary and replay diagnostics-sidecar digest and roster;
- preservation of both original diagnostic sidecars, whether or not their numerical telemetry is identical.

Optimizer diagnostics are not required to be byte-identical across executions and do not enter the scientific-record digest. They are not discarded, rounded, normalized or represented as equal. A mismatch in scientific fields still blocks adjudication.

The already implemented same-runner primary/clean-source replay topology is retained: each primary shard is paired sequentially with a clean `git archive` replay on the same pinned Ubuntu runner, with the hash-locked Python environment and single-thread BLAS/OpenMP settings. Primary and replay remain separate immutable artifacts.

## 4. Target cells, replication and seeds

| Cell | M | R | K | Within truth | Raw-between truth |
|---|---:|---:|---:|---:|---:|
| F5 beta22 M10/R5 | 10 | 5 | 1,000 | 0.20 | 0.05 |
| F5 beta22 M30/R20 | 30 | 20 | 1,000 | 0.20 | 0.05 |

C0 uses the frozen v002 two-stage percentile bootstrap with B=1,000. C5 uses the v1.1 certified-root beta-binomial parametric percentile procedure with B=1,000. Both methods receive the same generated M×R dataset. Analytical truth is generated independently and is never passed to C5.

The consumed v1.0 seed schedule is not reused. v1.1 uses the same SHA-256 derivation structure but a new independent schedule and namespaces:
- holdout schedule: `C10S_F5_G7_TIERA_SEEDS_1.1`;
- holdout namespace: `c10s_f5_g7_holdout_v1_1`;
- resource-only namespace: `c10s_f5_g7_resource_v1_1`.

The validator checks collisions within the v1.1 bank and against the consumed G7 v1.0 namespace, the consumed comparative holdout and original v002 Tier-A seeds. The seed change prevents reuse of a consumed/unblinded bank; it does not change the DGP or scientific estimand.

## 5. Fresh resource-only preflight

The v1.0 resource profile (run 44926453920) is not reusable because the fitted-beta-binomial compute path has changed. A fresh resource-only profile is required from the final v1.1 compute snapshot before any new holdout authorization.

The resource profile uses K=100 per cell, C0/C5 B=1,000 and the disjoint v1.1 resource namespace. It is timing/scheduling evidence only:
- it may record per-dataset elapsed time, CPU/resource use and latency summaries;
- it must not inspect or retain certificate-status counts, interval-emission counts, abstention outcomes, coverage or method-selection results;
- it must not perform coverage adjudication;
- its datasets never enter the holdout denominator.

The profile uses schema `C10S-F5-G7-RESOURCE-PREFLIGHT-PARALLEL-PROFILE-002` and scope `RESOURCE_NAMESPACE_ONLY_K100_PER_CELL_TIMING_ONLY_NO_OUTCOME_INSPECTION_NO_COVERAGE_NO_HOLDOUT`. It is bound to the exact source commit and all performance-critical source-file hashes. Any change to the fitter, certificate, engine, fixtures, dependency lock, runner or profile script invalidates it. The v1.0 profile is retained historically but cannot satisfy this v1.1 gate.

## 6. Metrics and acceptance

For each cell × method × component, report:
- K and point/interval emission rates;
- conditional coverage and its two-sided 95% Wilson interval;
- unconditional cover rate;
- lower/upper miss rates;
- point bias, RMSE, median absolute error and mean interval width;
- typed abstentions and exact-certificate statuses;
- exact dataset/method/truth accounting and raw-between negative values;
- runtime/resource preflight and primary/replay identity.

A C5 component-cell passes only if:
1. conditional coverage is in [0.93, 0.97];
2. the two-sided 95% Wilson interval contains 0.95;
3. interval emission is at least 0.95;
4. all 1,000 datasets are accounted for exactly once with the expected C0/C5 roster and independent truth pairing;
5. all emitted endpoints are finite and ordered;
6. raw-between estimates and endpoints are untruncated.

G7 passes only if C5 passes all four component cells (two targets × two M/R cells). No pooling or averaging is permitted. C0 remains the matched baseline reference; its failure does not substitute for or rescue C5. If any C5 component fails, G7 is NOT_VALIDATED for that target regime. If integrity/resource/replay requirements prevent valid adjudication, G7 is INDETERMINATE.

## 7. Execution and authorization boundary

The v1.1 protocol and software are currently under deterministic implementation validation. No G7 v1.1 holdout bank is authorized or generated by this document.

Before any holdout execution:
- the implementation and adversarial tests must pass;
- the fresh v1.1 resource-only profile must be generated and independently hash-validated;
- the protocol, architecture, implementation, profile manifest, validator, workflow, tests and dependency lock must be frozen in one exact source snapshot;
- a new explicit one-use user authorization must bind to that snapshot and its complete hash set.

The consumed v1.0 authorization is not reusable. The current implementation authorization does not authorize resource-profile generation or G7 holdout execution.

Explicit exclusions remain: F1, Tier B, F2, B2/B3 development banks, consumed v1.0/v002 data, new stress cells, M1/M2 interval alternatives, F5 MCSE coverage, C10 Generator/Analyzer/Evaluator and any causal/Value claim.

## 8. Decision consequences

- **PASS:** F5's existing C5 within/raw-between percentile procedure is calibrated for the declared beta(2,2) M10/R5 and M30/R20 synthetic regimes, subject to v1.1 exact-fit and replay contracts.
- **NOT_VALIDATED:** one or more predeclared C5 coverage/emission criteria fail; preserve limiting evidence and do not retune on the G7 bank.
- **INDETERMINATE:** execution integrity, resource or replay requirements prevent valid adjudication.

No result automatically changes C10 claims, Core, RMA, Evidence→Claim Matrix, STATUS or main.
