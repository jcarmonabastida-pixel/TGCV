# TI-001 V010 — Scientific Analysis Specification 001

**Status:** SPECIFICATION — ANALYSIS NOT AUTHORIZED

## Purpose

Define, before calculation, the deterministic analysis of the two canonical TI-001 V010 executions.

The analysis is descriptive and operational. It measures the predefined decision-level Transformational Intelligence indicators. It does not establish a value effect, causal effect, or general theory confirmation.

## Analysis population

Each execution is analyzed independently over its 420 valid decision units:

- control: 140
- treatment: 140
- null: 140

The two executions MUST NOT be pooled, averaged, majority-voted, or substituted for one another.

## Primary observable

For each execution and condition:

`q_A(condition) = count(A) / count(valid decision units in condition)`

The primary observable is the proportion of decisions selecting action A.

## Predefined indicators

For each execution independently:

`TI_DC = q_A(treatment) - q_A(control)`

`TI_NULL = q_A(null) - q_A(control)`

Where:

- `TI_DC` is the treatment-control decision contrast;
- `TI_NULL` is the predefined null-control contrast.

No individual response receives a value, reward, utility, performance, or quality score.

## Required descriptive outputs

For Executor-1 and Executor-2 separately, calculate:

1. total valid decisions;
2. valid decisions by condition;
3. A count and B count by condition;
4. `q_A` by condition;
5. `TI_DC`;
6. `TI_NULL`;
7. presentation-stratified A/B counts and proportions;
8. pair-level agreement/disagreement between the two decision units of each pair, where applicable;
9. missing/invalid/incomplete counts;
10. execution metadata and binding identifiers.

## Cross-executor comparison

Executor-1 and Executor-2 may be compared descriptively on:

- condition-level A proportions;
- `TI_DC`;
- `TI_NULL`;
- presentation-stratified proportions;
- pair-level agreement/disagreement summaries.

Cross-executor differences are descriptive observations. They MUST NOT be averaged into a single scientific estimate unless a separately authorized analysis design explicitly defines such an estimator.

## Presentation stratification

Results MUST be reported separately for:

- `I1_FIRST`
- `I2_FIRST`

Presentation stratification is descriptive and must not be used post hoc to select a preferred subset.

## Pair-level analysis

Each canonical pair contains exactly two decision units, one `I1_FIRST` and one `I2_FIRST`.

For each execution, pair-level agreement is:

`agreement = number of pairs with identical A/B selections / 210`

Disagreement is the complement.

Pair-level analysis is descriptive and does not replace the decision-level indicators.

## Missingness and validity

No recoding, retry, imputation, exclusion after inspection, or reinterpretation is permitted.

The analysis MUST operate on the canonical execution validity field.

If any non-VALID record is discovered, the analysis must report it and stop before silently altering the denominator.

## Interpretation constraints

The analysis MUST NOT claim:

- causal impact of future structure on value;
- improvement in value, reward, utility, performance, or task success;
- superiority of treatment or null conditions;
- deterministic model behavior;
- confirmation or falsification of TGCV as a theory.

The permitted conclusion is limited to the observed decision-selection contrasts defined above.

## Reproducibility

The analysis implementation MUST be deterministic and consume only:

1. the canonical Executor-1 result;
2. the canonical Executor-2 replay result;
3. this analysis specification;
4. its own source.

It MUST NOT modify either execution result.

## Authorization boundary

This specification authorizes no calculation by itself.

A dedicated analysis preflight MUST verify the canonical result bindings, formulas, denominators, no-pooling rule, and prohibition of recoding/retry before explicit scientific analysis authorization.

**Disposition:** READY FOR ANALYSIS PREFLIGHT; SCIENTIFIC ANALYSIS NOT AUTHORIZED.
