# Dual-graph first increment — CI verification 001

**Reviewed implementation commit:** `02be572d1aa730171119b40264c4825bc40e3b58`  
**Pull request:** [#91 — Load integrated system and TGCV graph example together](https://github.com/jcarmonabastida-pixel/TGCV/pull/91)  
**Review date:** 2026-10-21  
**Scope:** engineering/UI verification only. No scientific execution or TGCV theory validation.

## Workflow results at the reviewed commit

| Check | Run | Result |
|---|---:|---|
| Browser and cross-runtime tests | [39676233457](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39676233457) | PASS |
| Browser performance benchmark | [39676233839](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39676233839) | PASS |
| Governance current-state consistency | [39676233683](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39676233683) | PASS |
| Synthetic engine tests | [39676233704](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39676233704) | PASS |

The browser/cross-runtime job reports passing the profile-3-only browser/Python contract and the grouped UI contract tests, including integrated graph loading and the stale-mapping warning. The engine job also replayed its suites from a clean source archive.

## Performance evidence

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

**CI gate: PASS for this exact implementation commit.**

This does not by itself authorize merge or promotion. Before acceptance, review the actual rendered interaction in the PR and confirm that:
- both graphs are blank on first load;
- one `Cargar ejemplo` action loads the integrated case into both;
- the TGCV mapping remains explicitly illustrative and fixture-specific;
- editing the system model marks the previous TGCV correspondence stale;
- no unrelated condition-evaluator, schema, persistence, value-causality, or TGCV Core changes have entered the PR.

`main` remains untouched. This record is engineering evidence only; it is not scientific validation.
