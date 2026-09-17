# TGCV — VSL Synthetic Minimum v0.1
## Runner Source/Runtime Integrity Audit 001

**Status:** PASS — BOUNDED METHODOLOGICAL EVIDENCE  
**Runner:** `03_EXPERIMENTS/VSL_SYNTHETIC_MIN_V001/vsl_synthetic_min_runner_v01.py`  
**Runner blob:** `eebade9075aa286f22249015443397fb83d069bf`  
**Prior runtime audit:** `TGCV_VSL_SYNTHETIC_MIN_RUNNER_RUNTIME_AUDIT_001.md`

## 1. Source-level separation

Inspection confirms:

- `outcome(state)` accepts only `State(q,r)`.
- `value(outcome_value)` accepts only the outcome.
- Neither function receives `case_id`, accessibility status, selected transform, exogenous factor, or transformation identity.
- Accessibility is generated upstream by `accessible_transforms()`.
- Selection is generated upstream by `select_transform()`.
- State transition is generated upstream by `TRANSFORMS` or the isolated T4 exogenous function.

**Result: PASS.**

## 2. T4 exogeneity

T4 explicitly sets `exogenous_factor=2` and computes:

`final_state = apply_exogenous_factor(S0, exogenous_factor)`.

The validation routine additionally asserts that the T4 final state equals the result of applying that factor.

**Result: PASS.**

## 3. Runtime correspondence

The supplied runtime output matches the expected source behavior for all six cases:

- T1: 0
- T2: 0
- T3: +4
- T4: +2
- NC1: 0
- NC2: 0

The reported selected transforms and accessibility flags also correspond to the source logic.

**Result: PASS.**

## 4. Identity/circularity boundary

The source supports the following bounded statement:

`final state -> outcome -> value`

is computationally separated from:

`accessibility -> selection -> transition`.

This is a methodological property of the synthetic implementation.

It does not establish that accessibility causes Value in any empirical system.

## 5. Evidence classification

**Class:** synthetic methodological evidence / implementation demonstration.

Supported:

- executable separation of transformation/accessibility and valuation paths;
- operational reproducibility of the frozen synthetic VSL mapping;
- explicit non-circular outcome/value interface;
- controlled contrast patterns T2/T3/T4/NC1/NC2.

Not supported:

- empirical causal effect;
- universal valuation function;
- real-world Value;
- cross-domain validity;
- superiority;
- deployment readiness.

## 6. Governance disposition

**Source integrity:** PASS  
**Runtime correspondence:** PASS  
**T4 exogeneity:** PASS  
**Non-circular outcome/value interface:** PASS  
**Scientific causal claim:** NONE  
**Matrix propagation:** bounded methodological routing may now be considered; no Core or C09 change is implied.
