# TGCV — VSL Synthetic Minimum v0.1
## Circularity and Identifiability Review 001

**Date:** 2026-09-18  
**Specification under review:** `TGCV_VSL_SYNTHETIC_MIN_v0.1_SPECIFICATION.md`  
**Specification status at review:** `CANDIDATE SPECIFICATION — TO BE FROZEN BEFORE EXECUTION`  
**Review status:** `REVIEW COMPLETE — FREEZE BLOCKED BY IDENTIFIABILITY DEFECT`  
**Scope:** Synthetic demonstrator only

## 1. Review purpose

This review evaluates whether the candidate VSL is sufficiently external, non-circular, operationally separable and identifiable to justify freezing the specification and proceeding to fixture/runner construction.

The review is deliberately prior to execution.

No experimental result is used to assess the specification.

No C09 evidence is used as an input to the synthetic VSL.

## 2. Canonical specification

Reviewed artifact:

`00_GOVERNANCE/SIP/TGCV_VSL_SYNTHETIC_MIN_v0.1_SPECIFICATION.md`

The specification defines the intended chain:

`ΔT_acc → trajectory → ΔO → ΔV*`

with the VSL restricted to:

`O → V*`

and explicitly excludes `T_acc`, `ΔT_acc`, treatment assignment, selected transformation and Value-derived variables from the VSL.

## 3. Review criteria

### R1 — Externality

**Result: PASS**

The specification explicitly places the VSL downstream of outcome measurement and outside construction of `T_acc`, `ΔT_acc`, `Pτ`, treatment assignment and trajectory selection.

### R2 — Direct accessibility-to-Value prohibition

**Result: PASS**

The specification explicitly prohibits:

`T_acc → V*`

and:

`ΔT_acc → V*`

The VSL therefore does not encode the target relationship as its valuation rule.

### R3 — Treatment/trajectory independence

**Result: PASS**

The specification prohibits treatment assignment, selected transformation and trajectory identity from entering the VSL.

### R4 — Outcome independence from accessibility

**Result: PASS IN PRINCIPLE**

The specification explicitly prohibits the outcome from using:

- `T_acc`;
- `ΔT_acc`;
- treatment assignment;
- selected transformation identity;
- the fact that a transformation was made accessible;
- Value variables.

This is an adequate architectural constraint.

### R5 — Outcome operational identifiability

**Result: FAIL**

The current specification defines:

`O = performance_final`

but does not yet define the exact state variable or deterministic function that constitutes `performance_final`.

Consequently, two independent executors could agree with the specification while selecting different downstream state variables or calculations.

This violates the intended independent-reproducibility requirement.

The defect is methodological, not empirical.

### R6 — Value mapping reproducibility

**Result: PASS**

Once `O` is fixed, the mapping:

`V*(S) = O(S)`

and:

`ΔV* = ΔO`

is deterministic and reproducible.

The mapping itself therefore introduces no additional ambiguity.

### R7 — T2 identifiability

**Result: CONDITIONALLY PASS**

The specification requires a case with:

`ΔT_acc ≠ 0`

and:

`ΔV* = 0`

This is a valid discriminating requirement.

However, it cannot be demonstrated until the outcome function is operationally frozen.

### R8 — T4 non-circularity control

**Result: CONDITIONALLY PASS**

The specification requires:

`ΔT_acc = 0`

while:

`ΔV* > 0`

through an exogenous synthetic state factor unrelated to accessibility.

This is an effective non-circularity control in principle.

The exact exogenous factor and its relation to the downstream outcome remain to be specified in the fixture.

### R9 — Identity-collapse prevention

**Result: FAIL PENDING FIX**

The specification correctly prohibits generating `ΔT_acc`, `ΔO` and `ΔV*` from one common function.

However, because the exact `O` function is not frozen, the review cannot yet establish that the planned implementation will operationally separate accessibility from outcome.

### R10 — Domain boundedness

**Result: PASS**

The specification explicitly restricts interpretation to the synthetic demonstrator and excludes C09, KGFS, financial wellbeing, economic Value, industrial Value, monetary ROI, social Value, organizational Value and universal Value claims.

### R11 — Version/provenance separation

**Result: PASS**

The specification establishes independent versioning and prohibits silent substantive modification.

### R12 — Execution readiness

**Result: BLOCKED**

Execution is not authorized from the current specification.

The specification must first be amended or supplemented with an exact, deterministic and accessibility-independent operational definition of `O`.

## 4. Main finding

The VSL architecture is sufficiently separated from the transformational mechanism, but the current candidate contains one material under-specification:

> `performance_final` is a concept, not yet an operational variable.

This matters because the central scientific purpose of the demonstrator is to distinguish:

`ΔT_acc`

from:

`ΔO`

and then from:

`ΔV*`.

Without a frozen outcome function, that distinction is not yet auditable.

## 5. Required correction

Before freezing `VSL_SYNTHETIC_MIN_v0.1`, the implementation must define a downstream synthetic performance variable satisfying all of the following:

1. It is computed from final state variables.
2. Its exact formula is deterministic.
3. Its inputs are listed explicitly.
4. None of its inputs is `T_acc`, `ΔT_acc`, treatment assignment, selected transformation identity or Value.
5. Its baseline value is reproducible.
6. Its change can be positive, zero or negative under the planned synthetic transitions.
7. T2 can produce `ΔT_acc ≠ 0` with `ΔO = 0`.
8. T3 can produce `ΔT_acc ≠ 0` with `ΔO > 0`.
9. T4 can produce `ΔT_acc = 0` with `ΔO > 0` through an exogenous downstream state factor.
10. The same final state must always yield the same `O`.

## 6. Governance consequence

Current disposition:

`VSL_SYNTHETIC_MIN_v0.1 = CANDIDATE`

Freeze is **not authorized**.

Runner construction is **not authorized**.

Execution is **not authorized**.

No Evidence-to-Claim Matrix change is authorized.

No C09 status, Core, RMA or Value claim changes.

## 7. Authorized next operation

The next operation is narrowly bounded:

**Define the exact synthetic downstream outcome function and update the candidate VSL specification without changing its externality, non-circularity, domain or claim boundaries.**

After that correction, this review must be rerun before the specification can be frozen.

## 8. Review conclusion

The review does **not** reject the VSL architecture.

It establishes that the architecture passes the principal circularity constraints but is not yet operationally identifiable because the outcome variable remains underspecified.

Therefore:

**CIRCULARITY ARCHITECTURE: PASS**

**OPERATIONAL IDENTIFIABILITY: BLOCKED**

**SPECIFICATION FREEZE: NOT AUTHORIZED**

**EXPERIMENTAL EXECUTION: NOT AUTHORIZED**
