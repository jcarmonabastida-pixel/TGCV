# Dual-graph first increment — CI verification 001

**Initial reviewed commit:** `02be572d1aa730171119b40264c4825bc40e3b58`  
**Latest reviewed commit:** `31dea771e4dfed30dfa138d616fcf80e2790fc4b`  
**Pull request:** [#91 — Load integrated system and TGCV graph example together](https://github.com/jcarmonabastida-pixel/TGCV/pull/91)  
**Review date:** 2026-10-21  
**Scope:** engineering/UI verification only. No scientific execution or TGCV theory validation.

## Workflow results at the initial reviewed commit

| Check | Run | Result |
|---|---:|---|
| Browser and cross-runtime tests | [39676233457](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39676233457) | PASS |
| Browser performance benchmark | [39676233839](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39676233839) | PASS |
| Governance current-state consistency | [39676233683](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39676233683) | PASS |
| Synthetic engine tests | [39676233704](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39676233704) | PASS |

The browser/cross-runtime job reports passing the profile-3-only browser/Python contract and the grouped UI contract tests, including integrated graph loading and the stale-mapping warning. The engine job also replayed its suites from a clean source archive.

## Latest correction and fresh CI results

The initial implementation exposed a semantic inconsistency: it treated a transition as available whenever it was not explicitly disabled, even if its source state could not be reached in that scenario. Commit `31dea771e4dfed30dfa138d616fcf80e2790fc4b` corrects this for the integrated example: a mapped TGCV transformation is included in a scenario's `T_acc` only when its system transition occurs in at least one trajectory enumerated by the existing system engine for that scenario. In the fixture, blocking `A→C` also excludes downstream `C→D`; opening that branch adds both mapped transformations to `ΔT_acc`.

Fresh CI on the corrected commit completed successfully:

| Check | Run | Result |
|---|---:|---|
| Browser and cross-runtime tests | [39677288840](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39677288840) | PASS |
| Browser performance benchmark | [39677289217](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39677289217) | PASS |
| Governance current-state consistency | [39677288941](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39677288941) | PASS |
| Synthetic engine tests | [39677288932](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39677288932) | PASS |

The corrected benchmark artifact is [collective-toy-browser-performance](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39677289217/artifacts/12382067569). The workflow reports validation and upload success. These are software/engineering checks, not scientific validation.

## Scope review against `main`

GitHub comparison from `main` at `988d92636e8f77b9accebbd4affefdcfb3efe837` to the latest implementation commit reports 14 commits ahead, 0 behind, and exactly three changed files: `prototypes/collective_toy/web/index.html`, `prototypes/collective_toy/web/ui_contract_test.cjs`, and `prototypes/collective_toy/web/cross_runtime_test.cjs`. No production core, schema, persistence, condition evaluator, or scientific execution file is changed in this diff.

## Performance evidence (initial passing run)

The benchmark run reports browser button-to-completed timings for synthetic graph fixtures:

| Graph fixture | States / transitions | Median | p95 |
|---|---:|---:|---:|
| Chain | 500 / 499 | 113.213 ms | 125.268 ms |
| Branching DAG | 500 / 2000 | 234.207 ms | 248.720 ms |
| Cyclic branching | 500 / 2000 | 229.655 ms | 241.695 ms |

These are engineering measurements for the existing synthetic workload, not a performance guarantee for every user model or device. The benchmark reports engine medians of 1.0 ms, 2.8 ms, and 2.7 ms respectively for these same cases; the remainder of the button-to-completed time is outside the measured engine calculation.

Artifact: [collective-toy-browser-performance](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39676233839/artifacts/12381039836).

## Relevant qualification

The clean-room browser job emitted an npm audit warning reporting one high-severity dependency vulnerability during `npm install`; this did not fail the tests and was not investigated or changed in this scoped increment. It should not be confused with a failing TGCV behavior test.

## Acceptance status

**CI gate: PASS for the latest implementation commit `31dea771e4dfed30dfa138d616fcf80e2790fc4b`.**

This does not by itself authorize merge or promotion. Before acceptance, the remaining gate is review of the actual rendered interaction in the PR. Confirm that:
- both graphs are blank on first load;
- one `Cargar ejemplo` action loads the integrated case into both;
- the TGCV mapping remains explicitly illustrative and fixture-specific;
- editing the system model marks the previous TGCV correspondence stale;
- no unrelated condition-evaluator, schema, persistence, value-causality, or TGCV Core changes have entered the PR.

`main` remains untouched. This record is engineering evidence only; it is not scientific validation.
