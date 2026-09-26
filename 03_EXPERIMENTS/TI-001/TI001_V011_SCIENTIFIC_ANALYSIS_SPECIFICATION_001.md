# TI-001 V011 Scientific Analysis Specification 001

**Status:** ANALYSIS SPECIFICATION — NOT AUTHORIZED

## 1. Scope
This specification defines the deterministic analysis of the already audited E1-R and E2-R execution results. It does not modify either execution result and does not perform any new provider call.
The two executions remain separate throughout the primary analysis.

## 2. Frozen inputs
The analysis consumes only the canonical V011 fixture, E1-R and E2-R scientific execution results, their primary execution audits, and the E1-R/E2-R independent execution concordance audit.
The fixture binding is SHA-256 `30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1`.
Only records marked valid by the audited execution results are eligible. Both audited executions currently contain 420 valid decisions.

## 3. Primary unit
The decision unit is the analysis unit for overall and presentation-stratified proportions. Pair identity is used only for descriptive agreement analysis.

## 4. Primary estimands
For each execution e in {E1-R, E2-R} and condition c: q_A(e,c) = N_A(e,c) / N_valid(e,c).
TI_DC(e) = q_A(e,treatment) - q_A(e,control).
TI_DC(e,I1_FIRST) and TI_DC(e,I2_FIRST) are the presentation-stratified treatment-control contrasts.
TI_NULL(e) = q_A(e,null) - q_A(e,control).
TI_NULL(e,I1_FIRST) and TI_NULL(e,I2_FIRST) are descriptive null-control contrasts by presentation.

## 5. Presentation dependence
For each execution and condition: P_D(e,c) = q_A(e,c,I1_FIRST) - q_A(e,c,I2_FIRST). These are descriptive presentation contrasts, not causal effects.

## 6. Cross-execution comparison
E1-R and E2-R estimands are reported side-by-side. The analysis may calculate absolute differences, direction agreement/disagreement, response-level A/B agreement across matching decision IDs, and pair-level agreement/disagreement within each execution.
These are execution-level comparison quantities and must not be interpreted as pooled estimates or causal effects.

## 7. Explicit non-pooling rule
The analysis MUST NOT pool E1-R and E2-R decisions, average their proportions, majority-vote their outputs, concatenate their records into a single sample, use one execution to repair or recode the other, or exclude observations because E1-R and E2-R disagree.
Any disagreement is retained as an execution-level observation.

## 8. Required output
For each execution separately: valid/invalid counts; A/B counts and q_A by condition; TI_DC; TI_NULL; A/B counts and q_A by condition x presentation; TI_DC by presentation; TI_NULL by presentation; P_D for control, treatment and null; pair agreement/disagreement; and response-level agreement across E1-R/E2-R matching decision IDs.
Cross-execution output: side-by-side estimates, absolute differences, and direction agreement/disagreement.

## 9. Determinism
All calculations must be deterministic from the canonical JSON inputs. No randomization, model call, retry, imputation, recoding, filtering based on observed outcomes, or external data is permitted.
Counts must be reconstructed directly from validated_decision after the execution audit has established its consistency with raw output.

## 10. Interpretation boundary
The analysis describes decision distributions within the frozen V011 configuration. It does not by itself establish a causal effect of future structure, a value/reward/utility effect, performance or task-success effects, general Transformational Intelligence outside the tested configuration, or a pooled effect across independent executions.

## 11. Authorization
This document defines the analysis protocol only.
Scientific analysis remains NOT AUTHORIZED until the corresponding analysis preauthorization gate passes and explicit authorization is recorded.