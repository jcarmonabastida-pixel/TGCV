# TGCV — VSL Synthetic Minimum v0.1
## Exact Downstream Outcome Definition

**Status:** CANDIDATE ADDENDUM — FREEZE BLOCKED UNTIL REVIEW  
**Scope:** Synthetic demonstrator only  
**Parent specification:** `TGCV_VSL_SYNTHETIC_MIN_v0.1_SPECIFICATION.md`

## 1. Purpose

This addendum converts the previously conceptual `performance_final` outcome into an exact deterministic downstream outcome function.

The outcome is deliberately defined from final-state performance variables and does not inspect transformation accessibility.

## 2. Synthetic State

Each system state is represented as:

`S = (q, r)`

where:

- `q` = operational capability level;
- `r` = operational resource level.

Both variables are non-negative integers.

The state does not contain `T_acc`.

Transformation accessibility is maintained as a separate object.

## 3. Baseline State

The frozen baseline is:

`S0 = (q=10, r=10)`

The baseline outcome is therefore:

`O(S0) = 10`

## 4. Exact Outcome Function

The downstream operational outcome is defined as:

`O(S) = q + 0.5r`

No other variable enters the outcome function.

Therefore:

`O(S1) - O(S0) = (q1-q0) + 0.5(r1-r0)`

The outcome function is deterministic and scalar.

## 5. Independence Constraint

The outcome function MUST NOT receive or inspect:

- `T_acc`;
- `ΔT_acc`;
- `Pτ`;
- treatment assignment;
- selected transformation identity;
- accessibility-change flags;
- Value variables;
- experimental case labels.

The outcome is calculated only from the final values of `q` and `r`.

## 6. Value Mapping

The parent VSL remains unchanged:

`V*(S) = O(S)`

and:

`ΔV* = ΔO`

No accessibility information enters the Value mapping.

## 7. Required Transition Behaviour

The synthetic fixture shall implement the following state effects independently from the accessibility mechanism.

### T1 — Baseline

`S1 = (10,10)`

Therefore:

`ΔO = 0`

and:

`ΔV* = 0`

### T2 — Accessibility-only

Accessibility changes, but selected trajectory A leaves the state unchanged:

`S1 = (10,10)`

Therefore:

`ΔT_acc ≠ 0`

while:

`ΔO = 0,quad ΔV* = 0`

This is the principal control against interpreting accessibility change itself as Value.

### T3 — Value-linkage

Accessibility changes and trajectory B produces a downstream capability improvement:

`S1 = (14,10)`

Therefore:

`ΔO = 4
`

and:

`ΔV* = 4
`

The intended pathway is:

`ΔT_acc → trajectory B → Δq → ΔO → ΔV*`

### T4 — Outcome control

Accessibility remains unchanged.

An exogenous downstream state factor changes capability:

`S1 = (12,10)`

Therefore:

`ΔT_acc = 0
`

while:

`ΔO = 2,quad ΔV* = 2
`

The change to `q` MUST be generated independently of accessibility.

T4 must not directly manipulate `O` or `V*`.

### NC1 — Irrelevant control

A representation-only change occurs.

The final state remains:

`S1 = (10,10)`

Therefore:

`ΔO = 0,quad ΔV* = 0
`

### NC2 — Accessible but not selected

Accessibility changes, but the selected trajectory A leaves the state unchanged:

`S1 = (10,10)`

Therefore:

`ΔT_acc ≠ 0
`

while:

`ΔO = 0,quad ΔV* = 0
`

## 8. Required Identifiability Pattern

The frozen fixture must preserve the following distinguishable states:

| Case | ΔT_acc | ΔO | ΔV* |
|---|---:|---:|---:|
| T1 | 0 | 0 | 0 |
| T2 | ≠0 | 0 | 0 |
| T3 | ≠0 | +4 | +4 |
| T4 | 0 | +2 | +2 |
| NC1 | 0 | 0 | 0 |
| NC2 | ≠0 | 0 | 0 |

The demonstrator therefore contains both:

- accessibility change without Value change; and
- Value change without accessibility change.

These are required to prevent the VSL from collapsing into an accessibility measure.

## 9. Operational Separation Requirement

The implementation must maintain two independent computational paths:

### Accessibility path

`state/context → T_acc`

### Outcome path

`final state (q,r) → O`

The outcome path must not call the accessibility path.

The Value path is:

`O → V*`

The following architecture is prohibited:

`T_acc → O → V*`

## 10. Freeze Condition

This addendum may become frozen only after the circularity/identifiability review confirms:

1. `q` and `r` are genuine downstream state variables;
2. `q` and `r` are not aliases for accessibility;
3. the transition effects above are implemented exactly;
4. T4 changes `q` independently of accessibility;
5. the outcome runner cannot access `T_acc`;
6. an independent executor can calculate `O` from `S1` alone.

Until then:

`OUTCOME_DEFINITION_v0.1 = CANDIDATE`

## 11. Claim Boundary

This definition does not constitute experimental evidence.

It does not establish that operational performance is Value in any real-world domain.

It exists solely to make the synthetic VSL experimentally identifiable.

No C09 inference, Core change, RMA change, Evidence-to-Claim Matrix change, or causal claim is authorized by this artifact alone.
