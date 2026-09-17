# TGCV — VSL Synthetic Minimum v0.1
## Executable Fixture Runtime Audit 001

**Status:** RUNTIME VALIDATION — PASS  
**Scope:** Fixture validation only; no experimental causal execution  
**Fixture:** `03_EXPERIMENTS/VSL_SYNTHETIC_MIN_V001/vsl_synthetic_min_fixture_v01.py`  
**Fixture commit:** `1b2990e067fdc7ae862c84c58be04848dde339d3`

## 1. Runtime observation

The fixture validation entry point completed and emitted all six required cases:

T1, T2, T3, T4, NC1, NC2.

No assertion failure was reported.

## 2. Observed outputs

| Case | accessibility_changed | O0 | O1 | ΔO | V0 | V1 | ΔV* | exogenous_factor |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| T1 | False | 15.0 | 15.0 | 0.0 | 15.0 | 15.0 | 0.0 | 0 |
| T2 | True | 15.0 | 15.0 | 0.0 | 15.0 | 15.0 | 0.0 | 0 |
| T3 | True | 15.0 | 19.0 | +4.0 | 15.0 | 19.0 | +4.0 | 0 |
| T4 | False | 15.0 | 17.0 | +2.0 | 15.0 | 17.0 | +2.0 | 2 |
| NC1 | False | 15.0 | 15.0 | 0.0 | 15.0 | 15.0 | 0.0 | 0 |
| NC2 | True | 15.0 | 15.0 | 0.0 | 15.0 | 15.0 | 0.0 | 0 |

## 3. Runtime controls

**T2 control:** observed accessibility change with zero outcome/value change. **PASS.**

**T3 specified linkage:** observed accessibility change with +4 outcome/value change. **PASS as fixture behavior.** This is not yet causal evidence because no experimental runner or treatment-generation mechanism has been executed.

**T4 non-circularity control:** observed no accessibility change with +2 outcome/value change; exogenous factor = 2. **PASS as fixture behavior.**

**NC1:** zero outcome/value change. **PASS.**

**NC2:** accessibility change with zero outcome/value change. **PASS.**

## 4. Numerical integrity

Baseline:

`S0=(10,10)`

`O0=10+0.5(10)=15`

T3:

`S1=(14,10)`

`O1=19`

`ΔO=+4`

T4:

`S1=(12,10)`

`O1=17`

`ΔO=+2`

All observed values conform to the frozen outcome definition.

## 5. What this runtime validates

The runtime establishes that the executable fixture correctly implements the frozen numerical contract and produces the required discriminating patterns.

It validates:

- deterministic outcome calculation from final `q,r`;
- deterministic `V*=O` mapping;
- accessibility/value separation at fixture level;
- required T2/T3/T4/NC patterns.

## 6. What this runtime does NOT validate

This execution does not establish:

- causal validity;
- an executed transformation mechanism;
- empirical Value;
- generalization;
- independence of an experimental runner;
- independent executor reconstruction;
- absence of leakage in a future runner;
- any real-world Value claim.

## 7. Governance disposition

**Fixture runtime validation:** PASS  
**Frozen contract conformance:** PASS  
**Experimental runner:** NOT YET BUILT  
**Experimental execution:** NOT PERFORMED  
**Causal claim:** NONE  
**Evidence-to-Claim Matrix propagation:** NONE

The fixture is now eligible to serve as the frozen executable input to construction of the experimental runner.
