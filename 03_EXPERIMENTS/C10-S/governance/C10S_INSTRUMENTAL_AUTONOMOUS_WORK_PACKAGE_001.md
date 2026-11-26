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
