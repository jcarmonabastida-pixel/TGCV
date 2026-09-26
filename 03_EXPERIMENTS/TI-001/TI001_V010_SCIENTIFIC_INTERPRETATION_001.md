# TI-001 V010 Scientific Interpretation 001

**Status:** CONTROLLED SCIENTIFIC INTERPRETATION — DESCRIPTIVE, NOT CAUSAL

## Scope

This interpretation concerns only the observed decision behaviour produced by the frozen TI-001 V010 fixture, decision interface, and runtime, as analyzed separately for Executor-1 and Executor-2.

It does not evaluate value, reward, utility, performance, task success, external outcomes, or the TGCV programme as a whole.

## Executor-1

Executor-1 produced 420 valid decisions.

The observed proportion selecting A was:
- control: 0.5857142857142857
- treatment: 0.5857142857142857
- null: 0.6285714285714286

The predefined indicators were:
- TI_DC = 0.0
- TI_NULL = 0.042857142857142816

Within this execution, the treatment and control A proportions are identical. The treatment-versus-control indicator therefore shows no observed difference in the predefined decision proportion for this execution.

The null condition has a higher observed A proportion than control by 0.042857142857142816.

## Executor-2

Executor-2 produced 420 valid decisions.

The observed proportion selecting A was:
- control: 0.7
- treatment: 0.6142857142857143
- null: 0.7214285714285714

The predefined indicators were:
- TI_DC = -0.08571428571428563
- TI_NULL = 0.021428571428571463

Within this execution, the treatment A proportion is lower than the control A proportion by 0.08571428571428563. The null A proportion is higher than the control A proportion by 0.021428571428571463.

## Cross-execution observation

The two independent executions do not produce identical decision distributions.

For TI_DC, Executor-1 gives 0.0 whereas Executor-2 gives -0.08571428571428563. For TI_NULL, Executor-1 gives 0.042857142857142816 whereas Executor-2 gives 0.021428571428571463.

These differences are retained as execution-level observations. They are not pooled, averaged, recoded, or resolved by selecting one executor.

Accordingly, the experiment provides two execution-specific observations rather than a single combined TI estimate.

## Presentation-stratified observation

Executor-1:
- I1_FIRST: A=210, B=0, q_A=1.0
- I2_FIRST: A=42, B=168, q_A=0.2
- pair agreement: 42/210 = 0.2

Executor-2:
- I1_FIRST: A=209, B=1, q_A=0.9952380952380953
- I2_FIRST: A=76, B=134, q_A=0.3619047619047619
- pair agreement: 77/210 = 0.36666666666666664

Both executions therefore exhibit a large descriptive difference in action distribution between the two presentation orientations. This is an observed presentation-stratified pattern. The present experiment does not establish why that pattern occurs and does not identify it as a causal effect.

## Scientific interpretation

Under the operational definition used by TI-001 V010, the experiment successfully generated valid A/B decisions and permits calculation of the predefined TI indicators.

The treatment-versus-control indicator is execution-dependent: it is 0.0 in Executor-1 and negative in Executor-2. Consequently, these executions do not provide a single stable treatment-control decision effect under the predefined indicator.

The null-versus-control indicator is positive in both executions, with different magnitudes. This is likewise an observed descriptive pattern and is not evidence of a value effect or a causal mechanism.

The strongest common descriptive feature across the two executions is the presentation-stratified difference between I1_FIRST and I2_FIRST. Because the experiment was not specified as a causal presentation-order study, this observation should be treated as a design-sensitive pattern requiring separate investigation rather than as an explanation of the treatment-control result.

## Scope and limitations

1. The experiment measures an A/B decision response, not value creation or external task performance.
2. The experiment does not establish that future structure causes a decision change.
3. The two executor runs are independent observations and must remain separate.
4. The observed execution-level difference means that a single pooled TI estimate would not be justified by the current analysis specification.
5. The presentation-stratified pattern is descriptive and may be relevant to subsequent interface or experimental-design work.
6. No general claim about model capability outside this fixture, interface, and runtime is warranted.

## Disposition

TI-001 V010 is **scientifically interpretable at the descriptive decision level** within its defined scope.

It does not, by itself, establish a causal effect, a value effect, or confirmation/falsification of TGCV.

**Interpretation status: CLOSED — DESCRIPTIVE SCIENTIFIC INTERPRETATION.**
