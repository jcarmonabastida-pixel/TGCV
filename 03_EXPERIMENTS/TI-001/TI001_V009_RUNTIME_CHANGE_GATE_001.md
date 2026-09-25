# TI-001 V009 — Runtime Change Gate 001

**Status:** CHANGE REQUIRED — NOT AUTHORIZED

## Trigger
TI-001 V008 completed processing 420 decision units but produced 0 valid A/B decisions. The Responses API marked the sampled response incomplete with reason max_output_tokens; the configured budget was exhausted by reasoning tokens.

## V008 preservation
V008 remains immutable and its execution is retained as non-valid scientific evidence:
- scientific_execution: PERFORMED
- valid A/B decisions: 0
- TI analysis: NOT_PERFORMED

## Required change
The runtime output budget must be increased sufficiently to permit completion of the required A/B response under the selected model/runtime.

This is a design/runtime change, not a retrospective correction of V008.

## Versioning rule
The changed runtime condition must be introduced as a new TI-001 version with:
1. new canonical runtime specification;
2. updated execution contract;
3. runtime compatibility preflight;
4. updated scientific executor binding if required;
5. renewed final pre-authorization gate;
6. explicit user authorization before execution.

No V009 scientific execution is authorized by this gate.

## Experimental invariant
The scientific object remains Transformational Intelligence. The change must not introduce value, reward, utility, performance, task success, external outcomes, causal-value analysis, retries, or recoding.

## Decision required
The next design action is to establish and validate the new runtime output budget for V009 before generating or executing any new scientific run.

**scientific_execution:** NOT_AUTHORIZED
