# C10-S — Autonomous instrumental readiness work package

**Status:** ACTIVE RESEARCH WORK PACKAGE  
**Date opened:** 2026-11-26  
**Branch:** `research/c10s-instrumental-autonomous-workpackage-20261126`  
**Parent audit:** `research/c10s-f1-f5-integrated-simplification-audit-20261126`  
**Parent commit:** `a4731d4b398d21eb0bcbd5b6b9e097f9263e685a`

## 1. Delegated objective

Autonomously take the C10-S statistical/inferential instrumentation from its current state to a documented, reproducible, scientifically defensible **Tier-A launch-readiness decision**. The project objective is to pass Tier-A and then Tier-B, so that the authorized causal C10-S experiment can be executed. Instrument development is subordinate to that objective.

The user delegates ordinary technical and methodological decisions within this work package. Do not return for routine choices, implementation details, or intermediate approvals. Return to the user only when:
- a new Tier-A confirmatory execution is genuinely ready to be launched; or
- a hard blocker, missing authority, unavailable evidence, or scientific impossibility prevents progress and cannot be resolved within this mandate.

## 2. Scope of autonomous work

Permitted within this research branch:
- inspect and reconcile the existing F1–F5 code, specifications, diagnostics, historical development data and test suites;
- review existing implementations before writing new ones;
- choose the simplest scientifically valid method supported by evidence;
- refactor, simplify, test, and document research-branch code;
- add deterministic tests and static mathematical/code reviews;
- run bounded development-only simulations and diagnostics using development data or newly generated development-only data, provided they are clearly separated from all confirmatory/holdout data and do not consume a Tier-A/Tier-B authorization;
- compare candidate methods on predeclared component-wise criteria;
- maintain a durable decision log, exact commits, reproducibility instructions and a launch-readiness checklist;
- prepare a prospective Tier-A protocol and execution package for review/launch, without launching it.

## 3. Prohibited without a separate explicit authorization

- Do not launch, dispatch, or otherwise initiate a new Tier-A confirmatory/holdout run.
- Do not launch Tier-B.
- Do not execute the scientific causal C10-S experiment.
- Do not consume, reuse, or manufacture authorization tokens.
- Do not change frozen Tier-A/Tier-B acceptance thresholds after observing results.
- Do not reuse any exposed, unblinded or previously adjudicated dataset as confirmatory evidence.
- Do not alter `main`, canonical governance, RMA, Evidence→Claim Matrix, STATUS, or canonical claims.
- Do not merge research branches or promote candidate methods to canonical status.
- Do not use G7 data to tune the method retrospectively.
- Do not introduce additional mathematical machinery unless a documented failure of a simpler candidate makes it necessary.

## 4. Scientific and engineering rules

1. Preserve the existing DGP truth and exact estimands. Keep estimation, interval construction, calibration, and numerical certification conceptually separate.
2. Select methods per estimand and declared DGP family; do not force a single estimator to solve different statistical problems.
3. Report component-wise coverage, Wilson intervals, emission/abstention, interval width, directional misses, numerical failure classes, runtime and Monte Carlo error. No pooling to rescue a failed cell.
4. Distinguish genuine non-identification/boundary states from optimizer termination flags and numerical precision warnings.
5. Every candidate must have deterministic unit/property tests, an independent numerical cross-check where applicable, and a bounded development comparison before it can enter the prospective protocol.
6. Prefer existing exact pivots, profile likelihood, finite-R oracles and validated components over new generic frameworks.
7. Keep F5 MCSE distinct from within/raw-between interval coverage.
8. Maintain exact provenance: branch, commit SHA, source-data identity, seed namespace, configuration, output hashes and test results.
9. Development evidence is not confirmatory evidence. A candidate selected using development results must be frozen before a fresh independent Tier-A holdout is generated.
10. No claim that Tier-A/Tier-B calibration establishes the causal effect `ΔT_acc → Value`.

## 5. Work sequence and exit gates

### Gate A — historical/code reconciliation
- Map the actual F1–F5 components, source files, contracts and current status.
- Identify which previous methods and datasets are development, exposed holdout, confirmatory, or unusable.
- Reconcile F1 exact within pivot and existing raw-between profile likelihood.
- Reconcile F5 production/analytic-gradient fits and the exact finite-R beta-binomial oracle.
- Establish whether the F5 global-MLE certificate is necessary for the selected inferential procedure, rather than assuming it is.

### Gate B — minimal candidate selection
- Choose the smallest candidate set that covers the frozen Tier-A estimands and DGP families.
- Diagnose F5 plug-in percentile bootstrap versus refitted parametric bootstrap and, only if warranted, component profile intervals.
- Do not increase bootstrap replication count without a demonstrated Monte Carlo error problem.
- Define explicit abstention/boundary handling and failure semantics.

### Gate C — development validation
- Run only bounded, non-confirmatory development experiments.
- Compare methods against the frozen component-wise acceptance targets and relevant diagnostics.
- Record negative results and stop expanding candidates when the evidence discriminates between them.
- If no method can meet the frozen gates, report the exact limitation and recommend a scientifically defensible scope restriction or a focused redesign; do not lower thresholds.

### Gate D — prospective freeze
- Freeze code, estimands, DGPs, thresholds, seed namespace policy, sample sizes, Monte Carlo precision, numerical tolerances, failure/abstention handling, resource profile, artifact contract and adjudicator.
- Verify that the confirmatory Tier-A data are fresh and independent of all development/exposed data.
- Verify the workflow and adjudication path end-to-end using non-confirmatory fixtures without consuming a Tier-A authorization.

### Gate E — return-to-user: Tier-A launch readiness
Return only when a concise evidence package establishes:
- candidate method and declared domain;
- why simpler alternatives were rejected or retained;
- deterministic tests and independent numerical checks PASS;
- development comparisons and uncertainty summaries;
- frozen prospective protocol and exact source commit;
- fresh confirmatory data/seed plan and sample-size/MCSE justification;
- workflow, artifact and final-adjudication dry-run PASS;
- explicit list of residual risks and assumptions;
- exact action required from the user to authorize Tier-A launch.

Passing Gate E means **READY_TO_LAUNCH_TIER_A**, not Tier-A PASS, not Tier-B authorization, and not permission to execute C10-S.

## 6. Reporting and focus control

- Work in this single research branch unless a technical dependency requires a clearly documented sub-branch.
- Keep a concise decision log and update this work package with links/SHAs as milestones complete.
- Do not create parallel conceptual architectures or broaden the scope to TGCV theory, web/playground, predictor, or unrelated governance work.
- Do not send routine progress requests or ask the user to choose among technical alternatives.
- When reporting, distinguish PASS, FAIL, SKIPPED and NOT_VERIFIABLE.
- If blocked by a tool limitation or a required external authorization, state the precise blocker; never imply background work is continuing when it is not.
- Preserve the previous audit as an immutable parent artifact; this document governs the delegated implementation/readiness phase.

## 7. Current initial state

- G7 Tier-A v1.1: `NOT_VALIDATED` (1/4 components passed); primary/replay integrity matched.
- Tier-B authorization: `false`.
- C10 scientific execution authorization: `false`.
- Previous integrated simplification audit: `C10S_F1_F5_INTEGRATED_SIMPLIFICATION_AUDIT_001.md`.
- No new confirmatory run is authorized by this work package.


## 8. Progress snapshot — 2026-11-26

**Current branch head after this progress record:** `5a6ef034bb71aaea067eb39b0088941bce89ecac`  
**Exact code commit covered by the latest static test run:** `3be47b6f86e5a625b23fda7e878651cc08731cdc`

### Gate A — historical/code reconciliation

- **F1 within:** retain the existing exact chi-square pivot. Its prior six-cell calibration evidence remains separate from the raw-between issue.
- **F1 raw-between:** the earlier static review has been reconciled against the current profile-likelihood source in `diagnostics/C10S_F1_PROFILE_LIKELIHOOD_RECONCILIATION_002.md`. The current path now enforces per-profile nuisance diagnostics, direct score-sign concordance, a unique nuisance maximum, and an explicit F1 family guard. The outer profile connectedness argument is documented. The LR cutoff remains uncalibrated; this candidate is not Tier-A ready.
- **F5:** the existing B1 analytic-gradient/Hessian diagnostics, production/analytic reconciliation, finite-R likelihood and exact beta-binomial oracle are retained. The historical B2/B3 raw-artifact reconciliation remains descriptive and does not change adjudication: M10/R5 has a near-binomial concentration ridge; M30/R20 has a distinct high-concentration plug-in undercoverage pattern.
- **F5 runner consistency:** two stale hard-coded references to method ID `F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0` were replaced with the engine's declared `IMPLEMENTED_METHODS["F5"][1]`. This aligns the development runner with the current method roster; it does not change the fit, interval construction, frozen thresholds, or historical data.
- **F5 functional P/A reconciliation:** a read-only derivation from the verified historical B2 artifact is recorded in `diagnostics/C10S_F5_B2_PA_FUNCTIONAL_RECONCILIATION_001.md` (artifact SHA-256 verified). Where both fit paths had parameters, W/B functional differences were very small at the 95th percentile, including M10/R5 despite parameter-level ridge diagnostics; missing analytic terminal parameters were 103/5,000 and 121/5,000 in M10/R5, while production fits remained 5,000/5,000 interior. This is descriptive historical evidence only: no threshold, selection, or tuning was derived from it. The fitted B point estimates still show downward bias, so this does not validate M1 or repair coverage.
- **Static CI:** the read-only comparator workflow was enabled for this research branch. Latest exact-code run `45816013597` completed **SUCCESS**: compilation PASS and 211 deterministic tests PASS. The G7 resource-profile compatibility steps were SKIPPED on this branch only; their historical manifest/artifact pair has a schema mismatch with the later resource validator and remains untouched. Those steps remain enabled on the original G7 research branch.
- An overstrict attempt to make the finite score-scan discordance flag an unconditional interval veto was reverted after the existing resolved repeated-root fixture demonstrated that the finite scan can report a false discordance. No such guard remains in the current source.

**Gate A disposition:** PASS for historical provenance and deterministic code/test reconciliation; CONDITIONAL for inferential candidate validity because F1 LR calibration and F5 method selection remain open.

### Gate B — minimal candidate selection

- F1 within remains unchanged.
- F1 raw-between profile likelihood is retained as the smallest existing candidate for the separate raw-between estimand; no cutoff selected.
- F5 fixed-parameter plug-in C5 remains the incumbent comparator and is not validated. C0 remains diagnostic only, not a fallback.
- **Provisional next F5 candidate to investigate:** M1-PCT, a refitted parametric bootstrap of the population functionals (W(\mu,\kappa)) and (B(\mu,\kappa)). M1-BASIC may remain a secondary diagnostic. This is not yet a method selection or freeze. The M2 profile-likelihood design is deferred unless the simpler M1 route cannot handle weak identification/boundary states or fails the frozen component gates.
- The exact global-MLE certificate is not assumed to be mandatory for every bootstrap refit; its boundary handling, numerical cost and necessity must be reconciled before the M1 fit contract is fixed.

**Gate B disposition:** OPEN — candidate roster narrowed, fit-state contract and method choice not frozen.

### Gates C–E

- **Gate C:** NOT STARTED. No new development bank or method-comparison simulation has been run in this work package. Historical B2/B3 and G7 data have not been reused for tuning.
- **Gate D:** NOT STARTED. No prospective Tier-A protocol, seed namespace, sample-size/MCSE plan, or final adjudication dry-run is frozen.
- **Gate E:** NOT READY. No Tier-A launch is being requested or authorized.

## 9. Next autonomous operations

1. Complete the bounded F5 fit-state/boundary reconciliation: determine the least costly admissible refit contract, distinguish finite-bound optimizer outcomes from the exact (\kappa\to0) and (\kappa\to\infty) likelihood limits, and document whether the exact global certificate is necessary for the proposed M1 functional bootstrap.
2. Define the minimal M1-PCT development implementation and its fail-closed replicate-state semantics, reusing the existing likelihood, finite-R oracle, data generator and provenance contracts. Do not change M0 or the frozen C5 specification.
3. Close F1 raw-between LR-cutoff development design, including common versus cell-specific cutoff choice, then use a fresh development-only seed namespace.
4. Run only bounded development comparisons permitted by this work package. Record all component-wise coverage, Wilson intervals, emission/abstention, width, directional misses, MCSE and resource use. If no candidate meets the frozen gates, stop and report the exact limitation rather than weakening criteria.
5. Freeze the smallest viable prospective Tier-A package only after Gates B–D pass. Do not dispatch it; return for the user's explicit Tier-A launch authorization.

No Tier-A/Tier-B authorization was created, consumed, or changed. No main-branch or canonical-governance file was modified.


## 10. M1-PCT development pilot result — 2026-11-26

**Result record:** `03_EXPERIMENTS/C10-S/diagnostics/C10S_F5_M1_PCT_DEVELOPMENT_PILOT_RESULT_001.md`  
**Workflow:** [45822945892](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45822945892) — SUCCESS  
**Code commit:** `ab32975c00b8c0c1764f3f455c11fa1092c9fe53`  
**Artifact SHA-256:** `142915b64fb819028f2db8c59b38d0b616c96b7d7d2e1f19b52effa597665806`

Gate C has now had its first bounded F5 development execution. The workflow, compilation, 9 deterministic tests, pilot execution, artifact upload and seed-collision audit all PASS as engineering/provenance checks. This is not a calibration PASS.

M1-PCT emission was 4% (2/50) in M10/R5 and 100% (50/50) in M30/R20. In M10/R5, 846/4,500 bootstrap refits were non-admissible, across four distinct fit states; the fail-closed contract therefore abstained on 43/45 originally admissible datasets. The M10/R5 emission result fails the inherited >=95% requirement decisively. M30/R20 descriptive coverage (98% within; 94% raw-between) is not confirmatory and has no formal coverage adjudication. 

**Gate B disposition:** M1-PCT is rejected as a Tier-A candidate under its current contract; it is not repaired by dropping failed replicates or weakening abstention.  
**Gate C disposition:** M1-PCT fails M10/R5 emission. The development result discriminates against this candidate; no further M1 tuning is authorized by the work package.  
**Next operation:** static design review of a minimal component-profile-likelihood candidate for F5 functionals W and B, reusing the existing likelihood/derivative and exact finite-R oracle assets. The existing MCSE profile implementation is not a W/B interval method. Boundary, weak-identification, non-unique nuisance, disconnected-set and LR-cutoff behaviour must be resolved before any new development simulation.  
**Tier-A/Tier-B/C10 execution:** not launched, not authorized. No thresholds changed; no canonical/main files modified.


## 11. F5 component-profile candidate — static design review opened

**Design draft:** \`03_EXPERIMENTS/C10-S/design/C10S_F5_COMPONENT_PROFILE_LIKELIHOOD_DESIGN_REVIEW_DRAFT_001.md\`

The design derives the constrained nuisance geometry for the two actual functionals W and B, retains both mean branches, and explicitly includes the \`kappa -> 0\` two-point and \`kappa -> infinity\` binomial likelihood limits. It reuses the existing analytic beta-binomial likelihood/derivatives, MCSE-profile numerical patterns (without mislabelling them as W/B intervals), and exact finite-R oracle.

The central unresolved issue is statistical, not just computational: no LR cutoff is currently justified for weak identification and boundary cases. A routine Wilks cutoff is not assumed. Before any M2 simulation, the profile maxima, branches, boundaries, topology, global-maximum reconciliation and grid convergence need deterministic tests, and a prospective development calibration/validation design must be defensible.

**M2 disposition:** DESIGN CANDIDATE ONLY — not implemented, calibrated or selected. No M2 simulation has been run. No Tier-A/Tier-B/C10 authorization has been created or consumed.


## 12. Repository-level F5 profile reuse audit completed

A direct source audit of the existing beta-binomial likelihood diagnostics, MCSE profile implementation and finite-R oracle is recorded in \`C10S_F5_COMPONENT_PROFILE_LIKELIHOOD_DESIGN_REVIEW_DRAFT_001.md\` §§10–12.

Key consequence: the existing MCSE profile is not a W/B interval implementation and must not be copied as if it were one. Its finite nuisance scan uses truncated log-concentration ranges and its own documentation disclaims certified global topology. The likelihood diagnostics also use bounded primary optimizer coordinates and do not certify the unrestricted global maximum. The exact finite-R oracle remains an independent truth/moment oracle only.

The M2 design now specifies compact nuisance coordinates for the W and B constrained profiles, with the two concentration limits evaluated analytically. This removes arbitrary mathematical tail truncation but does not confer numerical globality. Adaptive refinement, branch/maxima stability, independent likelihood checks and fail-closed unresolved states remain mandatory before coding or simulation.

**Current disposition unchanged:** M2 design-only; no M2 implementation/simulation, no LR cutoff selection, no Tier-A/Tier-B/C10 authorization.


## 13. F1 raw-between static verification path added

The existing F1 raw-between profile-likelihood implementation has been located and inspected. It is implemented (not merely a candidate sketch), F1-family guarded, and uses nuisance score-polynomial isolation plus optimizer/score cross-checks and root-based LR endpoint inversion. The cutoff is caller-supplied and has not been calibrated; no Tier-A inference follows.

A separate research-branch workflow \`.github/workflows/c10-s-f1-profile-static-tests.yml\` now runs only pinned-dependency compilation and deterministic unit tests for the F1 profile and its numerical dependencies. It does not execute a simulation or calibration. Its run result will be used to distinguish implementation/test integrity from the still-open cutoff calibration.

**F1 disposition:** implementation present; deterministic test run pending; LR cutoff calibration pending.  
**F5 disposition:** M1-PCT rejected for Tier-A; M2 component profile remains design-only.  
**Confirmatory execution:** none.


## 14. F1 profile deterministic workflow result — PASS

**Workflow run:** [45829318708](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45829318708)  
**Workflow commit:** \`aa735f9faa173376b4443b4444ee1e57880b51a6\`  
**Job:** \`f1-profile-deterministic-tests\` — SUCCESS

Verified steps:
- checkout exact commit: PASS;
- pinned Python 3.12.10 setup: PASS;
- hash-locked dependency installation: PASS;
- compile implementation and dependencies: PASS;
- F1 profile deterministic suite: **51/51 tests PASS**.

The test suite includes interval-path fixtures for all six frozen F1 cells, root/polynomial diagnostics, tangency and unresolved-root cases, scale equivariance, ordered finite interval endpoints, LR endpoint equation checks, and typed abstentions for unresolved nuisance searches.

This is deterministic software/numerical verification only. The six-cell fixture test uses one synthetic sample per cell and checks that the numerical path returns an ordered interval or typed abstention; it is not repeated-sampling coverage calibration. No LR cutoff is validated by this run.

**F1 disposition:** implementation and deterministic tests PASS; statistical cutoff calibration/validation remains open.


## 15. Integrated deterministic comparator suite — PASS

**Workflow run:** [45822945917](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45822945917)  
**Tested code commit:** \`ab32975c00b8c0c1764f3f455c11fa1092c9fe53\`  
**Job:** \`gaussian-oracle-static-tests\` — SUCCESS  
**Suite:** **220/220 tests PASS** in 44.259 s.

The suite compiled and exercised the existing Gaussian and beta-binomial variance oracles, comparison interface, F1 exact pivotal candidate, F5 fitted beta-binomial bootstrap, M1 functional-refit pilot contracts, F5 analytic likelihood/score/Hessian diagnostics, F1 profile-likelihood candidate, nested M/R comparison engine, resource-preflight contracts, authorization validators and G7 shard/resource controls.

The F5 likelihood-diagnostic tests specifically passed independent finite-difference checks of analytic score and Hessian, log-shape derivative checks near the boundary, exact finite-R oracle reconciliation, explicit \`kappa -> 0\` and \`kappa -> infinity\` likelihood-limit checks, and optimizer/profile diagnostic contracts.

The F1 profile's dedicated workflow separately passed 51/51 tests on commit \`aa735f9faa173376b4443b4444ee1e57880b51a6\`. The later commits changed documentation/workflow metadata only; no F1/F5 statistical implementation source changed after the 220-test run.

**Static gate disposition:** F1 profile deterministic implementation/tests PASS; F5 likelihood/optimizer/oracle deterministic implementation/tests PASS. These runs do not constitute repeated-sampling coverage calibration, resource preflight, or confirmatory evidence.


## 16. F5 M2 algebraic route refinement

Inspection of \`c10s_f5_rational_score_polynomials.py\` found reusable exact integer score numerators \`N_mu,N_kappa\`, Sturm/root-isolation machinery, rational likelihood enclosures, and \`beta_binomial_global_mle_certificate\`, which certifies the unrestricted likelihood winner or returns a typed unresolved/boundary state.

The preferred constrained W/B profile route is now to derive an exact univariate score polynomial after substituting:
- \`kappa_W(mu;w) = w / (mu*(1-mu)-w)\`;
- \`kappa_B(mu;b) = (mu*(1-mu)-b) / b\`.

The feasible mean interval is \`[(1-sqrt(1-4v))/2, (1+sqrt(1-4v))/2]\` for target \`v\in(0,1/4)\). Both mean branches are represented in one interval. The concentration-limit endpoints are binomial for W and two-point mixture for B. Complete root isolation plus rational likelihood enclosures could enumerate and order every constrained stationary candidate without a generic local optimizer.

This is a more promising and potentially simpler exact route than adapting the existing finite-grid MCSE profile. The derivation and reuse proposal are in design-review §§14–15. It remains a design candidate; no M2 code, numerical profile or simulation has been run.


## 17. F5 M2 constrained-score algebra prototype added

New research-only module:
\`03_EXPERIMENTS/C10-S/harness/c10s_f5_component_profile_score.py\`

It constructs an exact univariate integer score polynomial for a fixed within target W or raw-between target B by:
- reusing the existing exact bivariate beta-binomial score numerators;
- constructing the corresponding exact positive score denominators;
- substituting \`kappa_W(mu;w)=w/(mu*(1-mu)-w)\` or \`kappa_B(mu;b)=(mu*(1-mu)-b)/b\`;
- clearing denominators using exact rational arithmetic;
- removing factors belonging only to the analytic concentration-limit endpoints;
- square-free decomposing and Sturm-isolating candidate roots on \`mu in (0,1)\`;
- retaining only roots strictly inside the feasible \`mu*(1-mu)>target\` interval and returning an unresolved status if a root interval cannot be classified.

The paired tests compare the exact polynomial's sign against an independently evaluated analytic constrained score for W and B, and exercise exact root isolation. A dedicated pinned-dependency static workflow has been added. It does not generate synthetic datasets or perform coverage/calibration.

**M2 status:** algebraic score-polynomial prototype implemented; deterministic workflow run pending. It is not yet a profile-likelihood maximum certificate, likelihood-value ordering, LR confidence set, calibrated method or Tier-A candidate. Those remain separate gates.


## 18. F5 M2 constrained-score deterministic verification — PASS

**Workflow:** [45831295559](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45831295559) — SUCCESS  
**Tested commit:** \`2cb6db946ec1604865fc198969c36dfcd80c1f62\`  
**Tests:** **30/30 PASS** in 16.972 s.

The new exact constrained-score tests passed:
- sign agreement between the exact W/B score polynomials and independently evaluated analytic constrained likelihood derivatives;
- root isolation with all returned roots classified strictly inside the feasible \`mu*(1-mu)>target\` domain;
- deterministic polynomial construction and exact binary-rational target handling;
- invalid component/target fail-closed behaviour.

The test harness initially overflowed while converting very large exact integer polynomial coefficients to float. This was a test-evaluation defect, not an algorithm failure; the check now evaluates the polynomial with exact \`Fraction\` arithmetic. The first run had already shown that the Sturm root-isolation test itself passed. The bounded rerun then passed all 30 tests, including the F5 likelihood score/Hessian/boundary regression suite.

**M2 status:** exact constrained score numerator construction and complete one-dimensional root isolation now have deterministic test evidence. The code still does not evaluate/order constrained profile likelihood maxima, produce LR confidence sets, calibrate cutoffs or establish Tier-A eligibility.


## 19. F5 M2 constrained profile-maximum enclosure — PASS

**Workflow:** [45831943819](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45831943819) — SUCCESS  
**Tested commit:** \`2f9d185ac2353d60709015d527750de92b84b7b6\`  
**Tests:** **31/31 PASS** in 28.862 s.

The M2 module now extends exact score-polynomial construction/root isolation with a constrained profile-maximum enclosure:
- isolates the two algebraic feasible-domain endpoints \`mu*(1-mu)=target\`;
- evaluates W's \`kappa -> infinity\` binomial endpoint likelihood and B's \`kappa -> 0\` two-point endpoint likelihood with exact rational interval bounds;
- maps each interior stationary-root interval to a compactified \`(mu,t)\` box, where \`t=kappa/(1+kappa)\`;
- reuses the existing outward-rounded rational beta-binomial likelihood enclosure on every interior candidate;
- encloses the constrained profile maximum by taking the maximum of all stationary-candidate and analytic-endpoint lower/upper likelihood bounds.

The new test checks both W and B and verifies that the certified upper likelihood bound dominates an independent dense-grid evaluation along each constrained curve. The existing F5 score/Hessian/boundary regression tests also pass in the same workflow.

**M2 status:** deterministic constrained profile-maximum enclosure implemented and tested. This is not yet a likelihood-ratio statistic, confidence set, cutoff calibration, or Tier-A method. The unrestricted global likelihood maximum still needs to be bound/reconciled with the existing exact global-MLE certificate, and LR inversion/topology remains open.


## 20. F5 M2 likelihood-ratio statistic enclosure — PASS

**Workflow:** [45832387827](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45832387827) — SUCCESS  
**Tested commit:** \`6d2429387578339c23d293a8aa42a2ad56c375bd\`  
**Tests:** **33/33 PASS** in 55.284 s.

The M2 module now combines:
1. the existing exact unrestricted beta-binomial global-MLE certificate (interior winner, boundary supremum or certified co-maximizers);
2. the exact constrained W/B stationary-root census and endpoint likelihood enclosures;
3. rational likelihood-ratio bounds from the two likelihood enclosures;
4. a rational atanh-series logarithm enclosure with an explicit remainder bound, producing exact rational bounds for the LR statistic without floating-point log rounding.

The deterministic test constructs a nondegenerate M10/R5 histogram, obtains the existing exact global-MLE certificate, and successfully encloses the LR statistic for both W and B. The log-series test checks rational bounds for \(\log 2\) and \(\log(1/2)\).

**M2 status:** a fixed-target F5 LR-statistic enclosure is now implemented and deterministic-tested. The remaining major inferential component is LR confidence-set inversion over the full W/B target domain, including topology, endpoint inclusion and stable component enumeration. The LR cutoff still requires the frozen development calibration/validation design; no cutoff has been selected.


## 21. M2 exact LR layer — deterministic verification complete

The exact constrained W/B profile-maximum and LR-statistic layers are recorded in design-review §§16–17. The LR implementation reuses the existing exact unrestricted global-MLE certificate and produces rational likelihood-ratio/log-statistic enclosures. Both W and B pass the deterministic LR fixture.

The broader exact rational-score/global-MLE suite passed 130/130 tests on run \`45831286314\`; the M2 score/root/maximum suite passed 31/31 on \`45831943819\`; the M2 LR suite passed 33/33 on \`45832387827\`.

**Remaining M2 work:** integrate the four functional-domain endpoints into the profile/LR API; implement full target-domain LR confidence-set inversion while retaining all components and failing closed on unresolved topology; test disconnected/one-sided/empty sets and endpoint inclusion. Then assess resource cost. No calibration or numerical simulation has been run.


## 22. F5 closed-domain endpoints — PASS

**Workflow:** [45832976732](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45832976732) — SUCCESS  
**Tested commit:** \`09fa43914a4f407f545dd5ef017196a7c8c1e217\`  
**Tests:** **34/34 PASS** in 72.183 s.

The constrained profile maximum now supports the full closed functional domain:
- W=0 via the profiled two-point limit;
- B=0 via the profiled binomial limit;
- W=1/4 via the binomial limit at mu=1/2;
- B=1/4 via the two-point limit at mu=1/2.

Exact zero likelihood at a constrained endpoint is propagated as \`LR_STATISTIC_INFINITE\`, not as a numerical failure. Tests cover interior-count and endpoint-only histograms and verify the corresponding exact rational likelihoods. The same run re-exercised the LR statistic enclosure and F5 likelihood score/Hessian regressions.

**M2 status:** fixed-target LR-statistic enclosure now covers both interior and closed-domain endpoint targets. Full LR confidence-set inversion and topology remain unimplemented.


## 23. F5 closed-domain endpoint and infinite-LR tests — PASS

**Workflow:** [45832976732](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45832976732) — SUCCESS  
**Tested commit:** \`09fa43914a4f407f545dd5ef017196a7c8c1e217\`  
**Tests:** **34/34 PASS** in 72.183 s.

This run verifies all four W/B functional-domain endpoints, exact endpoint likelihoods for interior-count and endpoint-only histograms, and propagation of an exactly zero constrained profile likelihood as an infinite LR statistic. The LR-statistic enclosure and F5 analytic likelihood regression tests also pass.

**M2 status:** fixed-target LR calculation is now defined on the closed interval [0,1/4]. No full confidence-set inversion or coverage calibration has been performed.


## 24. F5 LR confidence-set grid inversion — implementation and deterministic logic tests

The M2 harness now includes \`f5_component_profile_confidence_set\`. It:
- obtains the global-MLE functional target (or targets for certified co-maximizers) from the exact global certificate;
- evaluates the exact fixed-target LR enclosure on a uniform target grid over the closed [0,1/4] domain, including the MLE target;
- classifies each target as definitely IN, definitely OUT, or unresolved against a caller-supplied cutoff;
- retains every grid-detected connected component;
- refines each detected IN/OUT crossing by exact-target LR evaluations and returns conservative outside brackets;
- fails closed when any target classification or crossing remains ambiguous.

The algorithm explicitly reports \`topology_certified=false\`: a component narrower than the scan spacing can be missed. Nested-grid convergence is still required as a separate diagnostic and does not by itself prove global topology.

**Logic tests:** 36/36 PASS in 70.276 s, workflow [45834076442](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45834076442). The tests use synthetic LR evaluator fixtures to verify preservation of two disconnected components, conservative crossing brackets, and fail-closed handling of an ambiguous cutoff classification. They do not execute the full statistical inversion on simulated data.

A separate single-fixture full-inversion smoke run is in progress to check the actual fixed-target LR pipeline end to end. No calibration or confirmatory run is involved.


## 25. F5 full LR inversion smoke — execution PASS, performance gate OPEN

**Workflow:** [45834226441](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45834226441) — SUCCESS  
**Tested commit:** \`c35d430b36ef519d2bbab93fc3b9cea49ad8b103\`  
**Job:** \`f5-profile-lr-inversion-smoke\` — SUCCESS  
**Single full-inversion test runtime:** 410.438 seconds (6 min 50.4 s).

The smoke test executed the end-to-end fixed-target LR pipeline for one synthetic M10/R5 histogram, W component, five scan-grid points and one bisection step. Pinned dependency installation, compilation and the test all passed. This establishes that the integrated path can complete for one bounded fixture.

**Important scope limitation:** the smoke test asserts only that the returned status is one of the three expected grid-scan statuses, that \`topology_certified\` is false, and that at least five target evaluations occurred. It does not assert the numerical confidence-set endpoints against a known answer, nor validate coverage, topology, or cutoff calibration. It is an execution smoke, not a statistical validation.

**Performance finding:** 410.4 seconds for one W-only fixture at a five-node grid is not a viable demonstrated throughput for a multi-cell, multi-component development calibration with nested-grid/topology diagnostics. The current implementation is therefore not ready for repeated-sampling development calibration. Do not expand grid size, run B, or multiply cells until profiling identifies the dominant costs and a bounded optimisation materially reduces runtime without weakening exactness or fail-closed behaviour.

**Next operation:** deterministic performance profiling of the single-target path, separating:
1. exact unrestricted global-MLE certificate construction (reused once per dataset);
2. constrained score-polynomial construction;
3. Sturm root isolation;
4. candidate likelihood enclosure and rational refinement;
5. LR logarithm enclosure;
6. repeated target evaluations and bisection.

Use a development-only microbenchmark on the existing fixture, report per-stage timings and exactness/status parity, and avoid any coverage simulation. Consider caching only mathematically identical immutable subresults (e.g. data-specific score numerators or the unrestricted certificate); never reuse a result across different target values where the target changes the constrained polynomial. If a substantial speedup cannot be achieved without compromising certification, report the candidate as computationally impractical and reconsider a simpler statistically defensible route.

**M2 disposition:** exact fixed-target profile/LR layers and grid inversion logic exist; deterministic logic tests pass (36/36) and one end-to-end smoke passes. The inversion remains numerically scanned with \`topology_certified=false\`, its end-to-end result assertions are minimal, and the measured runtime is a blocking performance concern. No coverage calibration or method selection has occurred. Tier-A/Tier-B/C10 execution remains not launched and not authorized.


## 26. Exact integer Sturm optimisation — runtime probe PASS

**Workflow:** [45839559807](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45839559807) — SUCCESS  
**Commit:** \`5dcd6a22da9da980825c5220371603ee4d6b0ae8\`  
**Job:** \`f5-lr-runtime-probe\` — SUCCESS

The full deterministic suite completed **102/102 tests PASS** (185.679 s). This includes:
- integer Sturm sign variations exactly matching the rational reference on the test grid;
- exact root-census/isolation parity on the irrational-root fixture;
- the pre-existing rational polynomial, boundary, global-MLE, resultant, Bernstein/Krawczyk and resource-abstention tests.

Bounded fixed-target benchmark, same M10/R5 histogram and target as the pre-optimisation probe:

| Stage | Before (s) | After (s) |
|---|---:|---:|
| Unrestricted global MLE certificate | 0.193 | 0.141 |
| W fixed-target LR statistic | 27.765 | 1.718 |
| B fixed-target LR statistic | 8.230 | 2.322 |
| W+B | 35.995 | 4.040 |

The observed speedups are approximately 16.2x for W, 3.5x for B, and 8.9x for W+B. Both components returned \`LR_STATISTIC_ENCLOSED\`, with profile status \`PROFILE_MAXIMUM_ENCLOSED\` and three candidates. The certificate returned \`GLOBAL_INTERIOR_MAXIMUM_CERTIFIED\`.

The dominant cost has shifted: the profile now spends most time constructing/substituting the exact component score polynomial (617k Fraction operations for W; ~1.05m for B). Root isolation is no longer dominant in this fixture (0.448 s W; ~0.203 s B). Thus the integer Sturm change addressed the measured root-count bottleneck, but it does not make the entire exact profile calculation free.

**Disposition:** accept this optimisation as a successful exact-arithmetic performance improvement for the tested fixture. Do not infer broad throughput, confidence-set topology, interval coverage, or calibration validity from this one fixture and deterministic tests.

**Next gate:** rerun the end-to-end fixed-target LR inversion smoke on the optimised commit and compare runtime/status/output structure with the pre-optimisation 410.4 s smoke. Then run a bounded set of independent synthetic fixtures (including M30/R20 and boundary/degenerate cases) for execution robustness and fail-closed behaviour only. No repeated-sampling coverage calibration yet. Keep Tier-A/Tier-B/C10 causal execution unlaunched and unauthorized.


## 27. Post-optimisation full LR inversion smoke — PASS

**Workflow:** [45840355272](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45840355272) — SUCCESS  
**Tested commit:** \`10678360fc456506cfd42b28cb7c748d77eb0f20\`  
**Job:** \`f5-profile-lr-inversion-smoke\` — SUCCESS  
**Environment:** Ubuntu 24.04, CPython 3.12.10, hash-locked dependencies.

The full bounded smoke completed successfully. The single test ran in 12.548 s (measured internal inversion time 12.356572 s), versus 410.4 s in the pre-optimisation smoke: approximately 33.2x faster.

Fixture: M10/R5 histogram \`{0:1, 1:2, 2:2, 3:2, 4:2, 5:1}\`, component W, LR cutoff 3.84, five scan-grid points and at most one bisection step. Result:
- status: \`GRID_DETECTED_SINGLE_COMPONENT_BRACKETED\`;
- target evaluations: 7;
- \`topology_certified=false\`.

This is a material execution/performance improvement. It does **not** certify the global topology or completeness of the confidence set, endpoint coverage, cutoff calibration, or inferential validity. A detected bracket on a finite numerical grid is not a topological certificate.

**Next operation:** run a small, predeclared robustness suite on independent synthetic fixtures, including an M30/R20 histogram, boundary/degenerate histograms and both W/B components where defined. The objective is computational robustness and fail-closed classification only; do not estimate coverage or tune any cutoff. Keep this suite small and bounded. Record fixture definitions, statuses, resource abstentions, and runtimes. If an exact global certificate or profile cannot be established, retain the unresolved status rather than silently dropping the fixture.

Tier-A/Tier-B and causal C10-S execution remain unlaunched and unauthorized.


## 28. M30/R20 independent robustness smoke — execution PASS, performance warning

**Workflow:** [45842033055](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45842033055) — SUCCESS  
**Commit:** \`c01ee7d3adbea272bd9bdc61c2a0da2966c3a0c6\`  
**Job:** \`m30r20-robustness\` — SUCCESS

The workflow first failed on commit \`7592bec36d2bb2a7506635e524e7d1fbdc78ce1f\` because its checkout expression had a literal backslash before \`\${{ github.sha }}\`; this was a workflow-only failure before Python setup or statistical execution. The expression was corrected and the rerun checked out the exact commit successfully.

The corrected run completed dependency installation, compilation, and both fixed-target component profiles. Fixture: M30/R20, \(n=30\), \(r=20\), histogram \`{0:1, 2:2, 5:4, 8:5, 10:6, 12:5, 15:4, 18:2, 20:1}\), target \(1/20\).

| Stage | Result | Runtime |
|---|---|---:|
| Global certificate | \`GLOBAL_INTERIOR_MAXIMUM_CERTIFIED\` | 33.365 s |
| W fixed-target LR | \`LR_STATISTIC_ENCLOSED\`; profile \`PROFILE_MAXIMUM_ENCLOSED\`; 3 candidates | 805.552 s |
| B fixed-target LR | \`LR_STATISTIC_ENCLOSED\`; profile \`PROFILE_MAXIMUM_ENCLOSED\`; 3 candidates | 246.418 s |
| W+B | both enclosed | 1,051.971 s |

**Interpretation:** execution robustness and fail-closed status are demonstrated for this single interior M30/R20 fixture. This is not a coverage or calibration result. The exact profile method is still computationally expensive at M30/R20: one target takes about 13.4 minutes for W and 4.1 minutes for B. The 9x overall speedup measured on M10/R5 does not generalise to this larger fixture in terms of acceptable throughput. The profile's candidate count and enclosed status do not certify confidence-set topology or endpoints over the target axis.

**Disposition:** retain the exact method as a viable correctness-oriented candidate, but mark M30/R20 throughput as an unresolved computational risk. Do not start repeated-sampling coverage work or Tier-A until this risk is bounded or a defensible resource policy is specified without relaxing inferential guarantees.

**Next bounded engineering step:** instrument a single M30/R20 W profile to separate time spent in score-polynomial construction/substitution, exact root isolation, profile candidate evaluation and LR enclosure. Reuse the already computed global certificate and fixed fixture; no repeated-sampling, no cutoff tuning, no coverage estimates. Then target only the dominant operation for optimisation. Preserve exact arithmetic and fail-closed abstention. Add a B profile only if the W instrumentation indicates a shared bottleneck. After that, run boundary/degenerate fixtures as status/abstention tests, not coverage calibration.

Tier-A/Tier-B and causal C10-S execution remain unlaunched and unauthorized.


## 29. M30/R20 W stage instrumentation — queued/running

**Profiler:** \`harness/profile_c10s_f5_m30r20_w_stages.py\`  
**Workflow:** [45848960349](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45848960349)  
**Code commit:** \`8be6d89505e63d93f7f3c28d9c2226c5aa0dadfd\`  
**Corrected workflow commit:** \`5526ddccf53126d5282778a31ef49261d4ad957e\`

The profiler reuses the same fixed M30/R20 histogram and exact global-MLE certificate, then runs one W fixed-target profile at target 1/20. It times disjoint production-stage boundaries:
- exact constrained score-polynomial construction/substitution;
- all Sturm root-isolation calls (including feasible-root and endpoint isolations);
- interior candidate likelihood enclosures;
- analytic boundary profile likelihoods;
- rational LR logarithm enclosure;
- total elapsed time and unattributed overhead.

It records call counts and the unchanged LR/profile status, candidate count and stationary-root count. This is a bounded development-only diagnostic; it does not estimate coverage, tune a cutoff, or alter the exact method.

**Workflow correction:** the first workflow revision (run 45848914002) failed at checkout because the generated YAML contained a literal backslash before \`\${{ github.sha }}\`; Python and the statistical script were skipped. The checkout expression was corrected and verified in the current workflow. The corrected run is [45848960349](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45848960349), currently queued/running. No statistical result is available until its job completes.


## 30. M30/R20 W stage instrumentation — PASS; root isolation is dominant

**Workflow:** [45848960349](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45848960349) — SUCCESS  
**Commit tested:** \`5526ddccf53126d5282778a31ef49261d4ad957e\`  
**Job:** \`m30r20-w-stage-profile\` — SUCCESS

The fixed M30/R20 W profile completed with the same exact fixture and target \(1/20\). Global certificate: \`GLOBAL_INTERIOR_MAXIMUM_CERTIFIED\` (36.937 s). Profile: \`LR_STATISTIC_ENCLOSED\`, \`PROFILE_MAXIMUM_ENCLOSED\`, 3 candidates, 1 interior stationary point.

Measured profile time: **925.034 s** (15 min 25 s), with 894.134 s accounted by the instrumented production stage boundaries:

| Stage | Time | Share of total |
|---|---:|---:|
| Exact Sturm root isolation | 825.760 s | 89.3% |
| Score-polynomial construction/substitution | 68.323 s | 7.4% |
| Candidate likelihood enclosure | 0.005 s | negligible |
| Boundary profiles | 0.002 s | negligible |
| LR logarithm enclosure | 0.043 s | negligible |
| Unattributed runtime | 30.900 s | 3.3% |

Call counts: score polynomial 1; root isolation 4; likelihood enclosure 1; boundary profiles 2; log enclosure 2. Root isolation consumes about 92.4% of the instrumented time. Therefore the next optimisation target is **not** likelihood evaluation or the score-polynomial builder: it is the exact Sturm isolation path. The earlier hypothesis that score construction dominated M30/R20 is superseded by this direct measurement.

**Important:** this is a successful computational diagnostic, not a coverage result. The output remains a fixed-target LR enclosure; it does not certify confidence-set topology across the target axis. Total runtime is somewhat higher than the earlier uninstrumented W run (805.6 s), as expected from the profiling wrapper and instrumentation overhead; the stage shares identify the bottleneck reliably enough to focus the next experiment.

**Next bounded step:** split the four root-isolation calls into per-call measurements (polynomial degree, Sturm sequence length, coefficient bit-size, processed intervals, isolated roots, unresolved intervals, and elapsed time). Then inspect exact sequence construction and sign-variation evaluation costs. Optimise only the dominant sub-operation, retaining exact arithmetic and fail-closed resource statuses. Do not start coverage calibration or Tier-A.


## 31. M30/R20 W per-call Sturm instrumentation — PASS; sign evaluation dominates

**Workflow:** [45853526656](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45853526656) — SUCCESS  
**Tested commit:** `2de26f48d29b02928ce5d38b0e7ce609246bc96e`  
**Job:** `m30r20-w-per-call-sturm-profile` — SUCCESS

The observational instrumentation completed the same M30/R20 W fixed-target profile. Global certificate: `GLOBAL_INTERIOR_MAXIMUM_CERTIFIED` (36.891 s). Profile: `LR_STATISTIC_ENCLOSED`, `PROFILE_MAXIMUM_ENCLOSED`, 3 candidates, 1 interior stationary point. Total profile time: **927.246 s**. All numerical return values were passed through unchanged.

Four root-isolation calls were observed:

| Call | Input degree | Elapsed | Processed intervals | Isolated roots | Unresolved |
|---|---:|---:|---:|---:|---:|
| 1 — stationary score factor | 179 | 829.485 s | 3,372 | 1 exact + 122 intervals | 0 |
| 2 — feasible-domain endpoints | 2 | 0.0013 s | 81 | 2 intervals | 0 |
| 3 — exact endpoint factor | 2 | 0.00008 s | 0 | 2 exact | 0 |
| 4 — second endpoint factor | 2 | 0.0013 s | 81 | 2 intervals | 0 |

The dominant call constructed two Sturm sequences, of lengths 180 and 179. Across those sequences:
- 32,400 rational coefficients;
- maximum numerator/denominator bit lengths of approximately 26,910/27,384 bits;
- sequence construction: 167.706 s total;
- conversion to primitive integer sequences: 0.917 s total;
- exact sign-variation evaluation: **651.150 s across 3,253 evaluations**;
- remaining isolation work: 9.711 s.

Thus sign-variation evaluation consumes approximately **78.5% of the dominant isolation call** and 70.2% of the full profile. The other three calls are negligible. The dominant polynomial input itself has degree 179, 180 coefficients, maximum numerator bit length 665 and denominator bit length 643. The call ended `ISOLATION_COMPLETE`, with no unresolved intervals.

**Interpretation:** the next optimisation target is the exact integer sign-variation evaluator, not polynomial construction, integer scaling, or interval queue management. The current evaluator uses homogeneous Horner arithmetic at rational dyadic subdivision points. A development-only alternative may exploit the exact power-of-two denominator structure (integer shifts rather than repeated denominator-power multiplication), but it must first pass exact sign-parity tests against the current implementation over endpoint, dyadic and adversarial polynomial fixtures. No floating-point sign decisions, approximate pruning, altered isolation widths, or relaxed resource limits are permitted.

**Next operation:** implement and benchmark a narrowly scoped exact dyadic sign-evaluation alternative, with deterministic parity tests and a bounded M30/R20 W comparison. Record per-call and end-to-end timings, unchanged root census/status, and exact parity. If the alternative does not materially improve runtime, retain the current implementation. No coverage simulation, LR-cutoff calibration, Tier-A, Tier-B, or causal C10-S execution is authorized by this step.


## 32. Certified fixed-point Sturm sign prototype — exact parity PASS; runtime improved

**Workflow:** [45856531585](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45856531585) — SUCCESS  
**Tested commit:** `0c049293c3909d2e0881f624b334c0137de4d1db`  
**Tests:** 3/3 exact sign-parity tests PASS (4.593 s).

A development-only sign evaluator was added without changing the production profile code. For dyadic points it uses integer fixed-point interval Horner evaluation at 128 and 256 bits; a sign is accepted only when the certified interval excludes zero. Ambiguous signs use exact homogeneous integer-Horner fallback. Non-dyadic points also use the exact fallback. No floating-point sign decision is made.

The deterministic parity tests cover large integer-coefficient polynomials, dyadic grids, exact dyadic roots, endpoints and non-dyadic fallback. They pass against the existing exact integer sign-variation implementation.

On the same M30/R20 W fixture, the bounded profile returned:
- global certificate: `GLOBAL_INTERIOR_MAXIMUM_CERTIFIED` (29.497 s);
- profile: `LR_STATISTIC_ENCLOSED`, `PROFILE_MAXIMUM_ENCLOSED`;
- 3 candidates, 1 interior stationary point;
- four root-isolation calls, with the dominant call still `ISOLATION_COMPLETE`, 3,372 processed intervals, 1 exact root, 122 isolating intervals and 0 unresolved intervals;
- total profile runtime: **732.843 s**, versus 927.246 s in the preceding per-call instrumentation run (approximately 21% lower).

For the dominant call, exact sign evaluation fell from 651.150 s to 522.910 s. Across 582,289 polynomial evaluations, 573,426 signs were certified at 128 bits, 8,685 at 256 bits, and only 178 required exact fallback. The sequence construction itself still took 123.164 s across the two large Sturm sequences. The optimisation is therefore a real but incomplete runtime improvement; the method remains expensive.

**Disposition:** retain the fixed-point interval evaluator as a research prototype. It is not yet promoted into the production implementation and does not establish profile topology, coverage, LR-cutoff calibration or Tier-A readiness.

**Next operation:** test a signed primitive-integer polynomial remainder sequence (PRS) to construct the Sturm sequence directly over integers. The sign of each remainder must be proven equivalent to the rational Euclidean remainder up to a strictly positive scale; a positive-content reduction is allowed, but arbitrary sign normalization is not. Add exact sign-variation parity tests against the current rational Sturm sequence over dyadic and adversarial fixtures, then benchmark the combined integer-PRS plus certified fixed-point evaluator on the same M30/R20 W fixture. Keep the existing rational implementation as the reference and fallback. No coverage simulation, LR-cutoff calibration, Tier-A, Tier-B, or causal C10-S execution is authorized by this step.


## 33. Signed primitive-integer Sturm PRS prototype — exact parity PASS; limited end-to-end gain

**Workflow:** [45858989479](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45858989479) — SUCCESS  
**Tested commit:** `91374956c702272fc2afc9ede4e4e54ea653bda4`  
**Tests:** 4/4 exact parity tests PASS (7.267 s).

A development-only signed primitive-integer pseudo-remainder sequence (PRS) was added. It constructs the Sturm chain directly over integer coefficients. Each pseudo-remainder is corrected for the sign of the divisor leading coefficient and reduced only by positive integer content, so each term is a strictly positive multiple of the corresponding rational Euclidean Sturm term. The existing rational Sturm sequence remains the reference implementation.

The deterministic tests compare sequence lengths and exact sign variations against the rational reference over dyadic grids, including polynomials with large coefficients and positive/negative leading coefficients. All four tests pass.

On the same M30/R20 W fixture, combined with the certified fixed-point sign evaluator:
- global certificate: `GLOBAL_INTERIOR_MAXIMUM_CERTIFIED` (33.274 s);
- profile: `LR_STATISTIC_ENCLOSED`, `PROFILE_MAXIMUM_ENCLOSED`;
- 3 candidates, 1 interior stationary point;
- dominant isolation: `ISOLATION_COMPLETE`, 3,372 processed intervals, 1 exact root, 122 isolating intervals, 0 unresolved;
- total profile runtime: **720.064 s**.

The two large Sturm sequence builds fell from 123.164 s in the fixed-point-only run to 47.123 s with integer PRS (about 62% lower). Integer conversion became effectively zero-cost. However, the measured sign-variation stage was 578.667 s in this run versus 522.910 s in the fixed-point-only run; this variation is not evidence that the new sign evaluator is intrinsically slower, but it prevents attributing the end-to-end improvement to sign evaluation. Overall runtime is only about 1.7% below the fixed-point-only run and 22.3% below the original per-call baseline. The prototype therefore establishes an exact alternative sequence construction and a material reduction in sequence-build time, but not a sufficient end-to-end performance solution.

**Disposition:** retain the signed integer PRS as a parity-tested development candidate, not yet as the production implementation. The combined profile remains computationally expensive and no coverage, topology, or cutoff-calibration claim follows.

**Next operation:** test whether a coarser *exact isolating interval width* can reduce subdivision/sign-evaluation cost while preserving complete root census, exact interval enclosure, and `LR_STATISTIC_ENCLOSED`. Start with a bounded M30/R20 W comparison at width (2^{-24}) against the current (2^{-40}) fixture. The width change must not alter any statistical acceptance threshold; if likelihood/LR enclosures become too wide or any root becomes unresolved, retain the tighter width. No coverage simulation, LR-cutoff calibration, Tier-A, Tier-B, or causal C10-S execution is authorized by this step.


## 34. Coarser exact root-isolation width — PASS; substantial runtime reduction

**Workflow:** [45862410768](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45862410768) — SUCCESS  
**Tested commit:** `be32e062aa4bce33fec5ef8ec6e72c55e1eca845`  
**Fixture:** same M30/R20 W histogram, target (1/20), signed integer PRS plus certified fixed-point sign evaluator.

The exact root-isolation width was changed from (2^{-40}) to (2^{-24}). This changes only the maximum width of rational isolating intervals; it does not approximate root counts, alter the LR cutoff, or weaken any statistical acceptance criterion. Likelihood and LR bounds continue to be computed by exact rational enclosures.

Result:
- profile: `LR_STATISTIC_ENCLOSED`, `PROFILE_MAXIMUM_ENCLOSED`;
- 3 candidates, 1 interior stationary point;
- dominant isolation: `ISOLATION_COMPLETE`, 1,420 processed intervals, 1 exact root, 122 isolating intervals, 0 unresolved;
- the other two nontrivial endpoint calls each processed 49 intervals and completed; the exact endpoint-factor call found 2 exact roots;
- total profile runtime: **342.267 s**, versus 720.064 s at (2^{-40}) with the same combined prototypes (about 52.5% lower), and 927.246 s in the original (2^{-40}) rational-sequence baseline (about 63% lower).

The dominant call took 242.616 s. Its two integer Sturm sequence builds took 48.701 s; certified sign evaluation took 190.902 s across 1,301 variation calls and 232,881 polynomial evaluations. Of these, 229,595 signs were certified at 128 bits, 3,197 at 256 bits, and 89 used exact fallback. No unresolved interval was introduced.

The LR statistic enclosure was approximately [68.60849784569649, 68.60849785926779]; the profile likelihood enclosure was approximately (2.322290881315881\times10^{-54}) at both displayed endpoints. The output retains exact rational bounds; the decimals above are diagnostic display only. The interval is finite and narrow for this fixture. No LR cutoff is selected or validated by this result.

**Disposition:** (2^{-24}) is a promising numerical-precision candidate for the M30/R20 W profile. It preserves complete root census and exact LR enclosure for this one fixture while materially reducing computation. It is not yet frozen for all cells, estimands or boundary cases.

**Next operation:** run a further bounded width-sensitivity comparison at (2^{-16}), using the same fixture and exact arithmetic, to determine whether additional speed is available without changing the root census or making the LR enclosure operationally ambiguous. If the wider intervals materially weaken the enclosure, retain (2^{-24}). Then test the selected width on M30/R20 B and boundary/degenerate fixtures before considering any broader development comparison. No coverage simulation, LR-cutoff calibration, Tier-A, Tier-B, or causal C10-S execution is authorized by this step.


## 35. Exact root-isolation width (2^{-16}) — PASS on M30/R20 W

**Workflow:** [45863571577](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45863571577) — SUCCESS  
**Tested commit:** `3e669d7addf8f9fbbb1f580ea74bce8700c2a402`  
**Fixture:** same M30/R20 W histogram and target (1/20), with signed integer PRS and certified fixed-point signs.

At exact isolating width (2^{-16}):
- profile: `LR_STATISTIC_ENCLOSED`, `PROFILE_MAXIMUM_ENCLOSED`;
- 3 candidates, 1 interior stationary point;
- dominant isolation: `ISOLATION_COMPLETE`, 528 processed intervals, 1 exact root, 122 isolating intervals, 0 unresolved;
- the two nontrivial endpoint calls each processed 33 intervals and completed; the exact endpoint-factor call found 2 exact roots;
- total profile runtime: **208.962 s**.

Relative to (2^{-24}), runtime fell by about 39%; relative to the (2^{-40}) combined-prototype run, it fell by about 71%. The dominant isolation call took 109.082 s, with 48.627 s in the two integer Sturm sequence builds and 59.636 s in 409 sign-variation evaluations (73,213 polynomial evaluations). There were 89 exact sign fallbacks; all isolation calls completed.

The displayed LR enclosure remains approximately [68.60849784569649, 68.60849785926779], and the profile-likelihood enclosure remains approximately (2.322290881315881\times10^{-54}) at both displayed endpoints. The displayed bounds match the (2^{-24}) run to the shown precision; exact rational bounds remain in the computation. This is a fixed-fixture numerical result, not a coverage or calibration result.

**Disposition:** retain (2^{-16}) as the leading numerical-width candidate for this M30/R20 W fixture. It is not yet a globally frozen tolerance: M30/R20 B, boundary/degenerate fixtures, other Tier-A cells and LR-inversion topology still require verification.

**Next operation:** run the same M30/R20 histogram for component B at (2^{-16}), then exercise explicit boundary/degenerate fixtures under the same signed integer PRS and certified sign evaluator. Preserve typed unresolved/abstention states; do not infer general validity from W alone. No coverage simulation, LR-cutoff calibration, Tier-A, Tier-B, or causal C10-S execution is authorized by this step.


## 36. M30/R20 B and boundary robustness at (2^{-16}) — PASS

**Workflow:** [45864483072](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45864483072) — SUCCESS  
**Tested commit:** `306ff8db11adfbf8dbc28d982d1a4ada63d9ff6f`  
**Fixtures:** original M30/R20 interior histogram and boundary-only histogram `{0:15, 20:15}), with exact signed integer PRS, certified fixed-point signs and root-isolation width (2^{-16}).

All three bounded profiles completed:

| Fixture | Component | Global certificate | LR / profile result | Dominant isolation |
|---|---|---|---|---|
| M30/R20 interior | B | `GLOBAL_INTERIOR_MAXIMUM_CERTIFIED` | `LR_STATISTIC_ENCLOSED` / `PROFILE_MAXIMUM_ENCLOSED` | degree 263; 34 processed; 1 exact root + 2 intervals; 0 unresolved |
| M30/R20 boundary-only | W | `GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED` | `LR_STATISTIC_ENCLOSED` / `PROFILE_MAXIMUM_ENCLOSED` | degree 177; 484 processed; 1 exact root + 106 intervals; 0 unresolved |
| M30/R20 boundary-only | B | `GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED` | `LR_STATISTIC_ENCLOSED` / `PROFILE_MAXIMUM_ENCLOSED` | degree 259; 1 processed; 1 exact root; 0 unresolved |

Profile runtimes were 253.396 s (interior B), 240.772 s (boundary-only W), and 240.788 s (boundary-only B). Each returned 3 candidates and 1 interior stationary point. The boundary-only fixture was therefore not silently treated as an ordinary interior-MLE case: the global certificate explicitly returned the boundary-supremum state, and both component profiles still completed with exact LR enclosures.

**Disposition:** the (2^{-16}) numerical-width candidate has now passed bounded M30/R20 W and B interior profiles and a boundary-only W/B fixture. This is computational/root-census robustness evidence only. It does not validate repeated-sampling coverage, LR cutoff calibration, confidence-set topology over the target axis, or any Tier-A cell.

**Next operation:** exercise the same implementation/width on the M10/R5 F5 fixture for both W and B, including an endpoint-only boundary histogram. Then reconcile resource use and the numerical tolerance across the two F5 Tier-A cells before designing any repeated-sampling development calibration. No coverage simulation, LR-cutoff calibration, Tier-A, Tier-B, or causal C10-S execution is authorized by this step.


## 37. M10/R5 W/B and endpoint-only boundary robustness at (2^{-16}) — PASS

**Workflow:** [45866730907](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/45866730907) — SUCCESS  
**Tested commit:** `04e7d4d5e098b017c13b3cf362be0bc6d0c162d4`  
**Fixtures:** M10/R5 interior histogram `{0:1, 1:2, 2:2, 3:2, 4:2, 5:1}` and endpoint-only histogram `{0:5, 5:5}); exact signed integer PRS, certified fixed-point signs and width (2^{-16}).

All four bounded profiles completed with `LR_STATISTIC_ENCLOSED` and `PROFILE_MAXIMUM_ENCLOSED`:
- interior W: 0.843 s; 3 candidates, 1 interior stationary point; dominant degree 35, 204 intervals processed, 1 exact root + 26 isolating intervals, 0 unresolved;
- interior B: 1.181 s; 3 candidates, 1 interior stationary point; dominant degree 53, 34 intervals processed, 1 exact root + 2 isolating intervals, 0 unresolved;
- endpoint-only W: 0.828 s; global certificate `GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED`; 3 candidates, 1 interior stationary point; dominant degree 33, 246 intervals processed, 1 exact root + 30 isolating intervals, 0 unresolved;
- endpoint-only B: 1.067 s; global certificate `GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED`; 5 candidates, 3 interior stationary points; dominant degree 49, 34 intervals processed, 1 exact root + 2 isolating intervals, 0 unresolved.

All auxiliary endpoint isolation calls also completed. No unresolved interval or silent boundary-to-interior recoding occurred.

**Disposition:** the (2^{-16}) implementation candidate has now completed M10/R5 W/B interior and endpoint-only boundary fixtures, and M30/R20 W/B interior and boundary-only fixtures. This supports computational portability across the two F5 Tier-A sample-size cells and both components, but it is still a small set of deterministic histogram fixtures. It does not validate repeated-sampling coverage, cutoff calibration, or confidence-set topology across the full target domain.

**Next operation:** assess whether a wider exact root-isolation width (initially (2^{-8})) further reduces M30/R20 W runtime without changing complete root census or producing materially wider likelihood/LR enclosures. If the width fails closed or widens the LR enclosure too much for useful classification, retain (2^{-16}). Then begin a bounded, explicitly development-only comparison of candidate F5 interval methods against known DGP truth, without using Tier-A confirmatory or exposed holdout data. No coverage simulation under frozen Tier-A criteria, LR-cutoff calibration, Tier-A, Tier-B, or causal C10-S execution is authorized by this step.
