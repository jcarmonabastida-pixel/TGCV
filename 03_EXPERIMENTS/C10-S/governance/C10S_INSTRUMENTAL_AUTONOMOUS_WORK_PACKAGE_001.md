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
