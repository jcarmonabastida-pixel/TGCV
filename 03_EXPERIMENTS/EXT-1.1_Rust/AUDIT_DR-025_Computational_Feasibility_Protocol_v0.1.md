# AUDIT DR-025 — Rust Computational Feasibility / Population Execution Gate v0.1

**Status:** PROTOCOL COMMITTED — EXECUTION PENDING  
**Date:** 2026-09-07  
**Scope:** EXT-1.1 Rust primary analytical population

## 1. Purpose

Determine, before any confirmatory outcome computation, whether the frozen EXT-1.1 Rust primary analytical population can be processed as a deterministic census of 507,279 complete-follow-up origins under the frozen protocol.

This gate is computational only. It must not use outcome prevalence, associations, effect sizes, statistical significance, T_acc, Reach, R*, B, or any predictor-derived quantity to decide feasibility or population size.

## 2. Frozen inputs

- Dataset: `C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`
- Primary horizon: `H = 180` elapsed days
- Primary population: 507,279 complete-follow-up origins
- Incomplete origins: 100,219; excluded as right-censored/ineligible, never coded as outcome = 0
- Primary outcome: `subsequent_release_activity`
- Candidate transformation universe and accessibility definitions remain governed by DR-020/DR-021 and subsequent accepted decisions.

## 3. Feasibility question

Can the primary population of 507,279 origins be processed deterministically on the intended local execution environment without requiring outcome-informed selection, adaptive sampling, or non-reproducible state?

## 4. Permitted measurements

The audit may measure:

- wall-clock execution time;
- CPU time where available;
- peak resident memory / process memory;
- temporary disk usage;
- number of origins processed;
- deterministic replay consistency;
- whether streaming/chunked processing is sufficient;
- whether the complete census can be completed without materializing the entire dataset in memory.

A bounded pilot may be used solely to estimate computational resource requirements, provided that the pilot subset is selected deterministically and independently of outcome, T_acc, Reach, R*, B, package popularity, or future activity.

## 5. Prohibited operations

The feasibility audit must not:

- compute or inspect outcome labels;
- compute outcome prevalence;
- compute associations, effect sizes, significance, or model performance;
- use `T_acc` or `Reach` to select the population or alter N;
- perform adaptive sampling;
- inspect downstream adoption, downloads, popularity, or future registry state;
- optimize the primary horizon;
- alter the frozen outcome or horizon;
- select cases manually on substantive package characteristics.

## 6. Decision rule

### PASS — census feasible

Return PASS if the complete deterministic population of 507,279 origins can be processed within the available execution environment using the repository-controlled implementation, with bounded resource use and deterministic replay.

Consequence: retain the full census; no sampling gate is required for computational reasons.

### FAIL — census not feasible

Return FAIL only if the complete census cannot be processed under the documented computational constraints.

Consequence: do **not** select a sample inside DR-025. A separate ex-ante sampling decision must define N, sampling frame, deterministic seed/mechanism, and inclusion procedure before confirmatory execution.

## 7. Determinism requirement

The same frozen inputs and same deterministic implementation must reproduce the same population count and feasibility result. Any computational pilot must not modify the frozen analytical population definition.

## 8. Required output

The implementation must report at minimum:

- environment/runtime information;
- frozen dataset identifier/path;
- target population N = 507,279;
- processing strategy;
- measured wall-clock time;
- peak memory;
- temporary disk usage if measured;
- processed origin count;
- PASS/FAIL for full-census feasibility;
- deterministic replay result where executed;
- explicit confirmation that outcome/predictor quantities were not used.

## 9. Governance boundary

DR-025 does not authorize confirmatory outcome analysis. It only decides whether the already frozen analytical population can be processed as a census. If a computational sample becomes necessary, sampling requires a separate ex-ante governance gate.

## 10. Expected execution

The implementation to be created under:

`03_EXPERIMENTS/EXT-1.1_Rust/src/audit_dr025_computational_feasibility_v01.py`

must be executed from the repository root with:

```text
python .\03_EXPERIMENTS\EXT-1.1_Rust\src\audit_dr025_computational_feasibility_v01.py
```

No confirmatory outcome computation is permitted during this audit.
