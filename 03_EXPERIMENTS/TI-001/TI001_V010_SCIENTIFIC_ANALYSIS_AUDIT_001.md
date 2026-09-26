# TI-001 V010 Scientific Analysis Audit 001

**Status:** CLOSED — SCIENTIFIC ANALYSIS STRUCTURALLY VALID

## Scope

Audit of the deterministic scientific analysis performed over the canonical Executor-1 and Executor-2 V010 results.

## Canonical bindings

- Analysis result: `TI001_V010_SCIENTIFIC_ANALYSIS_RESULT_001.json`
- Analysis result blob SHA: `5e4586be82fc8ade6331d0260d9d968468fffade`
- Analysis ID: `TI001-V010-SCIENTIFIC-ANALYSIS-001`
- Authorization: `TI001-V010-SCIENTIFIC-ANALYSIS-AUTHORIZATION-001`
- Fixture SHA: `dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9`
- Interface SHA: `e025d66e477de3afd79147986b716389d7d7be03d01a21d4380b384e17c8510c`
- Executor-1 result blob SHA: `5297b578f250a50e90043dab5806877e3c3eec1d`
- Executor-2 result blob SHA: `82b09712d1fa866dc25927c62ada1c7da1004665`

## Structural audit

Both executions contain 420 decision units, with 420 valid decisions and zero invalid decisions. Each has 140 decision units in control, treatment, and null conditions, and 210 units in each presentation orientation.

The analysis preserves Executor-1 and Executor-2 as independent executions and explicitly sets `pool_executions=false`. No pooling, averaging, majority vote, recoding, retry, imputation, or substitution is applied.

## Analysis outputs

Executor-1:
- Control: A=82, B=58, q_A=0.5857142857142857
- Treatment: A=82, B=58, q_A=0.5857142857142857
- Null: A=88, B=52, q_A=0.6285714285714286
- TI_DC=0.0
- TI_NULL=0.042857142857142816
- I1_FIRST: A=210, B=0, q_A=1.0
- I2_FIRST: A=42, B=168, q_A=0.2
- Pair agreement=42/210; disagreement=168/210; agreement_rate=0.2

Executor-2:
- Control: A=98, B=42, q_A=0.7
- Treatment: A=86, B=54, q_A=0.6142857142857143
- Null: A=101, B=39, q_A=0.7214285714285714
- TI_DC=-0.08571428571428563
- TI_NULL=0.021428571428571463
- I1_FIRST: A=209, B=1, q_A=0.9952380952380953
- I2_FIRST: A=76, B=134, q_A=0.3619047619047619
- Pair agreement=77/210; disagreement=133/210; agreement_rate=0.36666666666666664

## Disposition

The analysis is structurally valid and complete. The differences between Executor-1 and Executor-2 are retained as observed execution-level differences; they are not pooled away or treated as a defect.

This audit does not make a causal claim, does not infer value effects, and does not constitute confirmation or falsification of TGCV.

**Audit disposition: PASS — READY FOR SCIENTIFIC INTERPRETATION GATE.**
