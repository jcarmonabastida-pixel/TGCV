# C10-S — Coverage-first execution focus 001

**Status:** ACTIVE RESEARCH DIRECTION — DESIGN/RECOVERY ONLY PENDING CANONICAL ROUTING AND AUTHORIZATION  
**Date:** 2026-11-27  
**Branch:** `research/c10s-coverage-first-focus-20261127`  
**Parent:** `research/c10s-instrumental-autonomous-workpackage-20261126`  
**Purpose:** prevent further drift into mathematical/instrumental perfectionism and direct all remaining work at the observed Tier-A interval-coverage and interval-emission deficits.

## 1. Governing objective

The sole technical objective of this workstream is to obtain defensible interval procedures that meet the already-frozen Tier-A component-wise criteria on the declared F1/F5 data-generating families:

- conditional coverage in [0.93, 0.97];
- two-sided 95% Wilson interval containing 0.95;
- interval emission >=0.95;
- exact dataset/method/truth accounting;
- finite, ordered endpoints;
- correct untruncated raw-between treatment;
- no unresolved numerical state;
- no pooling or averaging across cells/components.

The objective is **not** to certify every mathematical operation, build a general-purpose inference framework, or maximise numerical exactness. Statistical coverage and honest interval availability are the decision criteria.

No frozen threshold, estimand, DGP, acceptance rule or historical adjudication may be weakened or retrospectively changed.

## 2. Historical evidence that fixes the priorities

The following findings are the baseline; do not rerun their banks or use their exposed data as a holdout.

| Target | Existing evidence | Disposition |
|---|---|---|
| F1 within, six Gaussian cells | Exact chi-square pivot: 94.9–95.5% in independent comparative holdout; Wilson gates and 100% emission passed | CLOSED for declared F1 Gaussian scope; preserve unchanged |
| F1 raw-between | Conservative joint-pivot projection: 96.7–99.4%, above the frozen upper limit; existing profile-likelihood implementation has deterministic tests but no calibrated LR cutoff | OPEN — coverage too high; calibrate/review existing method only |
| F5 M10/R5 within | G7 v1.1: 98.644% conditional coverage, 88.5% emission | OPEN — overcoverage and insufficient emission |
| F5 M10/R5 raw-between | G7 v1.1: 99.661% conditional coverage, 88.5% emission | OPEN — overcoverage and insufficient emission |
| F5 M30/R20 within | G7 v1.1: 94.260%, 99.3% emission; this was the only G7 component PASS | CLOSED provisionally for the exact declared G7 method/DGP scope only; do not disturb absent contrary evidence |
| F5 M30/R20 raw-between | G7 v1.1: 93.353%, 99.3% emission; Wilson gate failed | OPEN — marginal undercoverage |

Original C0 percentile bootstrap failed multiple components and is a comparator, not a fallback. F5 C5 fixed-parameter plug-in percentile bootstrap remains unvalidated. F5 M1-PCT refitted bootstrap pilot is rejected under its current contract: M10/R5 emitted 2/50 (4%), with 846/4,500 non-admissible refits. Do not drop failed replicates or relax abstention to improve emission.

The exact global-MLE certificate improved fit classification/provenance but did not solve coverage. This is direct evidence against treating more exact fit certification as the remedy.

## 3. Work scope — only the deficits

### Closed diagnostic blocker — F5 M10/R5: no supported candidate

The historical diagnosis is complete and persisted in `C10S_F5_M10R5_COVERAGE_EMISSION_RECONCILIATION_001.md` and `C10S_F5_M10R5_MINIMUM_METHOD_DECISION_001.md`. Disposition: `NO_SUPPORTED_F5_M10R5_CANDIDATE`. C5 B2/B3 has adequate emission but overcovers; G7 v1.1 has 88.5% emission and overcoverage; M1-PCT emits only 4% under its strict refit contract. No defensible candidate is currently supported. Do not reopen M10/R5 or relax refit/abstention rules unless new evidence identifies a specific correctable mechanism. M2 profile likelihood remains uncalibrated and is not the default route.

### Current next coverage target — F5 M30/R20 raw-between: isolated undercoverage

Do not conflate this with M10/R5 weak-identification/emission failure.

1. Reuse the existing F5 likelihood and finite-R oracle.
2. Determine whether the observed 93.353% result is attributable to a systematic interval-construction defect, finite-bootstrap endpoint noise, or a specific concentration/parameter stratum.
3. Use a bounded development-only diagnostic with predeclared strata and metrics; no broad parameter sweep.
4. Change only the component interval construction if a mechanism is identified. Preserve the passing M30/R20 within method.
5. Require a disjoint development validation before prospective freeze.

### Priority 3 — F1 raw-between: excessive coverage

1. Preserve F1 within unchanged.
2. Review the existing raw-between profile-likelihood implementation and its 51/51 deterministic test result.
3. Select/calibrate an LR cutoff only from development evidence, with the frozen coverage/emission criteria as target. Do not assume a generic Wilks cutoff.
4. Use a bounded development-only comparison against the conservative joint-pivot reference, measuring coverage, Wilson, width, directional misses, emission and runtime.
5. Do not implement another F1 interval engine.

## 4. Explicitly out of scope / anti-drift rules

Until a specific coverage result proves otherwise, the following are prohibited within this workstream:

- further Sturm, subresultant, rational-arithmetic or arbitrary-precision optimisation;
- increasing root-isolation depth/precision, topology certification or global-MLE certification for its own sake;
- building generic confidence-set, interval, optimizer or certification frameworks;
- extending the F5 M2 profile-likelihood inversion or calibrating its cutoff as the default path;
- developing F5 MCSE intervals as a proxy for within/raw-between coverage;
- increasing bootstrap B merely to make the run larger;
- repeating original Tier-A, B2/B3, comparative holdout or G7 banks;
- selecting methods on exposed/unblinded results;
- changing acceptance thresholds, dropping failed replicates, conditioning coverage on successful fits, truncating raw-between values, or pooling cells.

A mathematical/numerical refinement is permitted only when all three conditions hold:
1. a specific observed coverage or emission failure is documented;
2. the proposed refinement addresses its identified cause directly;
3. a simpler alternative cannot address it adequately.

The deliverable for any such refinement must be an observable improvement in coverage/emission or a necessary integrity condition for measuring them. Mathematical elegance or a standalone exactness PASS is not sufficient.

## 5. Development experiment discipline

- Development runs must use fresh, disjoint development-only seeds and remain clearly separated from every historical/holdout/confirmatory namespace.
- **Hard runtime budget for every new development run: 30 minutes maximum.** A run that cannot complete a useful diagnostic within 30 minutes must be redesigned as smaller staged probes; do not simply raise the timeout. The current K=400/B=100 M30/R20 run 45976887796 is a one-off legacy exception already in progress; do not duplicate or expand it. No further run may use its runtime as precedent.
- Prefer K=25–50 diagnostic probes and B=25–50 when sufficient to expose gross emission/fit-state problems; report that such probes cannot certify coverage. Increase K/B only with an explicit MCSE/power justification and a demonstrated runtime fit within 30 minutes.
- Every run must emit per-dataset progress/checkpoints (or at least stage-level progress) so a long silent compute step is not repeated blindly.
- No parallel duplicate runs. Inspect an existing run before considering another.
- A pilot may reject a candidate; it cannot establish Tier-A PASS.
- Report each component/cell separately: K, emission, conditional coverage, Wilson 95%, unconditional cover, interval width, lower/upper misses, abstention classes, runtime and endpoint Monte Carlo error.
- Do not use a result with an emission rate below 95% to claim calibrated conditional coverage, even if the conditional percentage lies in range.
- If the candidate cannot meet the frozen gates, stop and report the exact failure rather than escalating mathematical machinery by default.

## 6. Work sequence and exit conditions

1. **Historical coverage ledger:** complete; do not rerun historical banks.
2. **F5 M10/R5:** diagnosis complete; `NO_SUPPORTED_F5_M10R5_CANDIDATE`. Keep blocked unless a new, specific, defensible interval contract emerges.
3. **F5 M30/R20 raw-between:** current target. The K=400/B=100 run `45976887796` was cancelled and produced no statistical result. The next proposed screen is K=30/B=25, one cell, existing M1-PCT contract, fresh disjoint development seeds, per-dataset checkpoints, hard 30-minute cap. This remains a proposal, not a dispatched run.
4. **Canonical C10 recovery gate:** before any new empirical run, reconcile the canonical C10 methodological state required by `main` bootstrap and confirm applicable execution authority. The bootstrap currently routes to design/recovery only; no new run may be dispatched until this is resolved.
5. **F1 raw-between:** afterwards, review/calibrate the existing implementation only; no new solver.
6. **Prospective freeze:** only after all required components have adequate disjoint development evidence, freeze methods, seed plan, K/B and MCSE justification, workflow and adjudicator.
7. Tier-A confirmatory, Tier-B and causal C10-S execution each remain subject to their separate explicit authorization.

F1 within and F5 M30/R20 within are not reopened unless new evidence directly contradicts their bounded existing PASS evidence.

## 7. Governance and authorization

- This document and all work remain on this research branch.
- The autonomous work-package permission for ordinary static review, code simplification, deterministic tests and bounded development-only experiments continues to apply.
- No Tier-A confirmatory run, Tier-B run or C10 causal execution is authorized.
- No changes to `main`, RMA, Evidence→Claim Matrix, STATUS, canonical claims, frozen thresholds or scientific authorization.
- No PR merge or promotion to canonical status.
- This focus document narrows the active work package; it does not rewrite historical results or the original work-package history.

## 8. Required reporting discipline

Every update must start with the coverage question:

**Which frozen Tier-A cell/component coverage or emission deficit does this action address, and what observable result will tell us whether it improved?**

If that question has no concrete answer, do not perform the action.

The historical coverage ledger is recorded in `03_EXPERIMENTS/C10-S/diagnostics/C10S_TIER_A_COVERAGE_LEDGER_001.md`. M10/R5 is blocked as `NO_SUPPORTED_F5_M10R5_CANDIDATE`. The single M30/R20 raw-between M1-PCT screen (run `45976887796`) was cancelled by the user; GitHub confirms the calculation step was cancelled and no artifact/statistical result was produced. Do not rerun it. The proposed K=30/B=25 screen is not dispatchable until canonical C10 recovery and applicable authorization are resolved. All future development runs, if authorized, must fit the 30-minute cap.
