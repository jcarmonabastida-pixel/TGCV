# TGCV C09 — FOS Statistical Estimator Specification 001

**Status:** `PRE-FLIGHT SPECIFICATION — EXECUTION NOT AUTHORIZED`

**Candidate:** Family Options Study (FOS), SUB vs UC comparison  
**Purpose:** Freeze the statistical estimator and inference procedure before any causal estimate is produced.

## 1. Target estimand

Primary estimand: causal effect of assignment to the FOS Supplemental Utility Allowance (SUB) intervention versus assignment to usual care (UC) on the determinately observed 37-month adult endpoint `p37_composite_hl`.

Treatment is defined by randomized assignment:
- Treatment: `i_ra_result = SUB`
- Control: `i_ra_result = UC`

Assignment is not replaced by programme take-up, programme use, compliance, housing status, or any post-assignment variable.

## 2. Frozen outcome

Primary outcome variable: `p37_composite_hl`.

Only determinately observed values `0` and `1` enter the primary outcome calculation. The single SUB/UC-linked observation coded `D` is excluded from the estimand calculation without imputation or inference from component variables.

Frozen estimation sample: **895** determinately observed SUB/UC-linked outcomes.

The excluded observation and its valid `w_nr_p37_su` weight remain in the audit trail.

## 3. Frozen weighting

Use the FOS 37-month adult non-response weight specifically defined for the SUB-versus-UC comparison:

`w_nr_p37_su`

No other pairwise weight is substituted.

## 4. Primary estimator

Estimate the weighted intention-to-treat difference in the probability of `p37_composite_hl = 1`:

`ITT = weighted_mean(Y | SUB) - weighted_mean(Y | UC)`

where each unit contributes `w_nr_p37_su` and treatment/control membership is determined by randomized assignment.

No regression adjustment, matching, propensity-score procedure, treatment-on-the-treated estimate, or post-assignment adjustment is part of the primary estimator.

## 5. Inference

Primary inference will use a design-consistent weighted variance calculation for the randomized SUB/UC comparison, preserving the randomization structure represented by the reconstructed FOS assignment cells.

The final executable implementation must report:
- weighted SUB mean;
- weighted UC mean;
- weighted ITT difference;
- standard error;
- 95% confidence interval;
- effective sample information used by the variance calculation;
- exact number of included and excluded observations.

If the executable variance procedure cannot be implemented reproducibly from the public-use files and frozen design information, the causal estimate is **NOT REPORTABLE**.

## 6. Exclusion and sensitivity

The `D` observation is not imputed.

A sensitivity analysis may bound or separately report the effect of assigning the excluded observation the two possible binary endpoint values, but such bounds must not replace the primary estimand or convert the observation into an observed outcome.

## 7. Reproducibility and stopping rule

Execution is permitted only after the C09 gate explicitly authorizes estimation.

The executable reconstruction must freeze:
- input file identity and SHA-256 values;
- variable names and coding rules;
- treatment/control universe;
- assignment-cell reconstruction;
- endpoint inclusion/exclusion rule;
- `w_nr_p37_su` weighting rule;
- estimator and variance algorithm;
- software/runtime environment;
- output schema and result hash.

Any mismatch, missing required input, non-reproducible variance calculation, or evidence of future leakage stops the execution and yields `BLOCKED` or `NOT REPORTABLE` rather than an estimated effect.

## 8. Scientific status

This specification freezes an estimation procedure only. It does **not** constitute a causal result, does not authorize execution by itself, and does not alter TGCV Core or the claim matrix.

**Next gate:** explicit C09 execution authorization after statistical implementation preflight.