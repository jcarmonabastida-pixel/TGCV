# TI-001 V010 Scientific Closure 001

**Status:** CLOSED — DESCRIPTIVE RESULT, NO CAUSAL OR VALUE CLAIM

## Closure basis

TI-001 V010 completed the authorized workflow:

1. Frozen fixture and decision interface were preflighted.
2. Executor-1 scientific execution was authorized and completed.
3. Executor-1 primary execution audit closed as structurally valid.
4. Executor-2 independent replay was authorized and completed.
5. Replay governance deviation was reconciled without modifying the replay result.
6. Replay comparison gate passed.
7. Scientific analysis was preflighted and explicitly authorized.
8. Deterministic scientific analysis was completed and canonicalized.
9. Scientific analysis audit closed as structurally valid.
10. Controlled scientific interpretation was completed and canonicalized.

## Canonical evidence

- Fixture SHA-256: `dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9`
- Decision interface SHA-256: `e025d66e477de3afd79147986b716389d7d7be03d01a21d4380b384e17c8510c`
- Executor-1 result blob: `5297b578f250a50e90043dab5806877e3c3eec1d`
- Executor-2 result blob: `82b09712d1fa866dc25927c62ada1c7da1004665`
- Scientific analysis result blob: `5e4586be82fc8ade6331d0260d9d968468fffade`
- Analysis audit commit: `b67d952d4fc8f2fb6d0f902aa222b183b3dcaee8`
- Interpretation commit: `5d8b0f234d435da03ffe170ca3ba897b58f5491c`

## Scientific result

Both independent executions produced 420/420 valid A/B decisions.

Executor-1:
- TI_DC = 0.0
- TI_NULL = 0.042857142857142816

Executor-2:
- TI_DC = -0.08571428571428563
- TI_NULL = 0.021428571428571463

The predefined treatment-control indicator therefore differs across the two executions. No pooled or averaged indicator is adopted.

Both executions also show a pronounced descriptive difference between I1_FIRST and I2_FIRST. This pattern is recorded as presentation-stratified observation only.

## What is established

The experiment established that the specified decision interface can obtain valid A/B responses from the configured model/runtime under the frozen fixture and that the predefined descriptive indicators can be computed independently for two executions.

The experiment also establishes that the observed treatment-control decision pattern is not identical across the two executions.

## What is not established

The experiment does not establish:

- a causal effect of future structure on decisions;
- a value, reward, utility, performance, or task-success effect;
- a general model capability beyond the specified fixture/interface/runtime;
- a stable single TI effect across independent executions;
- confirmation or falsification of TGCV as a whole.

## Follow-up implications

The strong presentation-stratified pattern is a concrete design finding. A future experiment may investigate presentation/order effects separately, but such work requires its own preregistered design and authorization.

The observed execution-level difference should likewise inform future reproducibility and robustness design rather than being removed through post-hoc pooling or recoding.

## Final disposition

**TI-001 V010: CLOSED.**

Scientific status: **DESCRIPTIVE RESULT — VALID EXECUTION AND ANALYSIS; NO CAUSAL OR VALUE CLAIM.**

No further scientific execution is authorized by this closure document.
