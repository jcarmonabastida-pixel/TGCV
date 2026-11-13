# C10-S V_cont — Calibration and Seed-Bank Protocol

**Status:** IMPLEMENTED PROTOCOL SCAFFOLD — NUMERIC PRECISION TARGETS OPEN  
**Branch:** `research/c10-s-consolidation-draft`  
**Scope:** Phase A synthetic V_cont benchmark only  
**Scientific execution:** NOT AUTHORIZED

## 1. Purpose and boundary

This protocol defines how calibration outputs may select candidate sample size N and assignment-replicate count R before an independent evaluation bank is opened.

It does not change the C1 estimands, DGP scenario definitions, Analyzer identification rules, or the distinction between ITT-Z, ITT-G and theta_A. It does not establish real-world causal identification or the TGCV `ΔT_acc → ΔValue` claim.

## 2. Two disjoint banks

### Calibration bank

Used only to:
- estimate scenario- and estimand-specific dispersion at candidate N values;
- calculate the calibration SD used for R dimensioning;
- select the smallest candidate N meeting all predeclared Monte Carlo precision targets;
- identify numerical instability and feasibility constraints.

### Evaluation bank

Used only after N, R, estimands, metrics and acceptance rules are frozen. It must not be used to tune N, R, tolerances, scenarios or analysis choices.

The banks use deterministic, domain-separated seed derivation with distinct bank labels. Within each scenario/N:
- the world seed is fixed across assignment replicates;
- Z assignment seeds vary by replicate;
- G assignment seeds vary independently by replicate;
- world, Z and G streams are distinct within each run;
- calibration and evaluation seed sets must be disjoint.

The implementation is in `vcont_benchmark_protocol.py`: `build_seed_bank` and `validate_seed_banks`.

## 3. Candidate N selection

The N grid is an explicit protocol input, not silently inferred from the harness default. Each candidate must satisfy the Generator constraints (N >= 16 and divisible by four).

For every candidate N, calibration must report precision separately for each predeclared scenario and estimand. The selection rule is the smallest N for which every required scenario-specific MCSE is no greater than its predeclared target:

`N* = min{N : MCSE_cal(s, e, N) <= target_MCSE(s, e) for every required (s,e)}`.

If no candidate qualifies, the result is `NO_CANDIDATE_N_MEETS_ALL_PREDECLARED_MCSE_TARGETS`; no extrapolation beyond the tested grid is permitted without a protocol amendment.

Implementation: `select_minimum_n`.

## 4. Assignment replicate count R

For each selected scenario/N/estimand, calibration estimates the across-assignment-replicate SD, `SD_cal`. The minimum R is:

`R = max(2, ceil((SD_cal / target_MCSE)^2))`.

Implementation: `required_replicates`.

This formula controls Monte Carlo precision of the simulated mean estimate, not sampling uncertainty of a real-world causal estimand. If the calibration SD is estimated imprecisely, the protocol must conservatively account for that uncertainty before freezing R; a plug-in point estimate alone is not an automatic guarantee.

## 5. Required calibration outputs

For each scenario and estimand:
- number of calibration assignment replicates;
- fixed world identity and scenario/N configuration hash;
- SD across assignment replicates;
- resulting MCSE for the planned R;
- selected N and R, with the exact target used;
- counts of identified, not-identified and indeterminate Analyzer results;
- abstention and invalid-run counts;
- seed-bank fingerprint and code/configuration hashes.

Do not pool scenarios to conceal a scenario-specific precision failure. Do not discard abstentions from denominators; report rates and denominators explicitly.

## 6. Metrics and inference boundary

Continuous recovery metrics: bias, MAE, RMSE, SD and MCSE.  
Adjudication metrics: identification, non-identification, indeterminacy and abstention rates.

Coverage, type-I error and power remain `NOT_EVALUATED` unless an inferential procedure with valid per-replicate interval/test outputs has been separately specified and implemented. The current Analyzer standard errors do not establish those properties. Wilson intervals in the protocol module quantify Monte Carlo uncertainty in simulated binary rates; they are not confidence intervals for causal effects.

## 7. Numeric decisions deliberately left open

The following values cannot be responsibly inferred from software defaults or unit-test fixtures and must be explicitly approved before the calibration bank is run:

1. Candidate N grid.
2. Minimum scientifically relevant effect / precision scale for each primary estimand, or an independently justified absolute target MCSE.
3. Target MCSE by scenario and estimand.
4. Calibration replicate budget or adaptive stopping rule for estimating `SD_cal` with adequate precision.
5. The required scenario/estimand set for N and R selection.
6. Any scientific recovery tolerance. The existing test tolerance 0.10 is not promoted to a scientific criterion.

If a target is expressed relative to a minimum relevant effect `δ_min`, its ratio must also be approved explicitly; no ratio is assumed by this protocol.

## 8. Freeze and authorization sequence

1. Approve the numeric decisions in §7.
2. Freeze the N grid, targets, scenario/estimand set and calibration stopping rule.
3. Generate calibration bank only; persist its manifest and outputs.
4. Select N and R using the predeclared rules; record all failures and feasibility limits.
5. Freeze the evaluation-bank seed plan, N, R, metrics and acceptance criteria.
6. Conduct a separate authorization gate before generating the evaluation bank.

This document and its software are protocol preparation only. No calibration run, benchmark execution, or scientific execution is authorized by this record.
