# TGCV — Realization / Selection Layer v0.1

**Status:** CONCEPTUAL DEVELOPMENT ARTIFACT — NOT YET EMPIRICAL EVIDENCE  
**Programme:** Teoría de Construcción de Valor de Sistemas Generativos (TGCV)  
**Version:** v0.1  
**Role:** Formal development preceding TR-131  
**Core impact:** NONE  
**Evidence Matrix impact:** NONE

---

## 1. Purpose

This document formalizes a provisional realization/selection layer between the space of accessible transformations and the transformations effectively realized by a system.

The layer is introduced following the bounded result of VSL Paired E1/E2 v001, where a modification of accessible transformation space was observed without a corresponding modification of realized trajectory or value under the tested synthetic construction.

The purpose is not to replace or weaken the transformational-space construct, but to distinguish:

1. transformations that are accessible;
2. transformations selected or realized;
3. resulting trajectories;
4. downstream outcomes and value.

The layer remains provisional until subjected to a dedicated irreducibility/sufficiency test.

---

## 2. Scope and status

This document does **not**:

- establish a new empirical phenomenon;
- establish a universal causal relation;
- modify the TGCV Core;
- establish `Π` as a primitive;
- upgrade any claim in the Evidence-to-Claim Matrix;
- establish general empirical validity outside the tested constructions.

It defines a candidate analytical layer whose necessity is itself testable.

---

## 3. Formal objects

Let:

- `S_t` = system state at time `t`;
- `C_t` = relevant conditions/context at time `t`;
- `T_acc,t` = transformations accessible under `(S_t,C_t)`;
- `Π_t` = selection/realization operator;
- `T_real,t` = transformation or set of transformations actually realized;
- `H` = realized trajectory;
- `O` = downstream outcome;
- `V` = value measure.

The existing transformational-space construct remains:

[
T_{acc,t}=F(S_t,C_t)
]

The candidate realization operator is:

[
Pi_t:(S_t,C_t,T_{acc,t},X_t)ightarrow T_{real,t}
]

where `X_t` denotes any additional information or decision conditions required by the realization mechanism.

The basic constraint is:

[
T_{real,t}subseteq T_{acc,t}
]

Thus accessibility does not imply realization.

---

## 4. Accessibility versus realization

TGCV distinguishes three analytically different objects:

[
T_{acc}
eq T_{real}
eq H
]

### 4.1 Accessible transformations

`T_acc` represents transformations that are available/admissible under the relevant system conditions.

A change:

[
Delta T_{acc}
eq0
]

means that the accessible transformational space has changed.

It does not, by itself, establish that the system will realize any newly accessible transformation.

### 4.2 Realized transformations

`T_real` represents transformations actually selected/executed.

Consequently:

[
T_{real}subseteq T_{acc}
]

is a constraint on realization, not an equivalence.

### 4.3 Trajectory

A realized trajectory is represented as:

[
H=(S_0,T_{real,0},S_1,T_{real,1},...,S_n)
]

with state transitions of the general form:

[
S_{t+1}=	au(S_t,C_t,T_{real,t})
]

The trajectory therefore depends on what is realized, rather than merely on what is accessible.

---

## 5. Provisional propagation chain

The resulting analytical chain is:

[
(S_t,C_t)
ightarrow
T_{acc,t}
ightarrow
Pi_t
ightarrow
T_{real,t}
ightarrow
S_{t+1}
ightarrow
H
ightarrow
O
ightarrow
V
]

This chain is a research construct, not a universal causal law.

In particular, the existence of the first transition does not entail the existence of every subsequent transition.

---

## 6. Non-implication established as a research constraint

The VSL result motivates the following distinction:

[
Delta T_{acc}
otRightarrowDelta H
]

in general.

A change in accessible transformational space can fail to propagate to the realized trajectory when the realization/selection process does not change.

A more specific mediated relation is therefore:

[
Delta T_{acc}
ightarrow
DeltaPi
ightarrow
Delta T_{real}
ightarrow
Delta H
]

where each arrow represents a condition requiring independent examination.

This formulation does not assert that the chain is universally present. It identifies the intermediate mechanisms whose role must be investigated.

---

## 7. VSL as boundary regime R0

The VSL Paired E1/E2 result is represented provisionally as:

[
Delta T_{acc}
eq0
]

while:

[
DeltaPi=0
]

and consequently:

[
Delta T_{real}=0
]

and:

[
Delta H=0
]

with the tested value measure also satisfying:

[
Delta V^*=0
]

This defines the provisional boundary regime:

### R0 — Accessible-Space Change / No Realization Change

[
oxed{
Delta T_{acc}
eq0,quad
DeltaPi=0,quad
Delta T_{real}=0,quad
Delta H=0
}
]

R0 is not a universal regime claim. It is the formal representation of the tested VSL boundary case.

---

## 8. Candidate propositions

### P1 — Accessibility/realization distinction

Accessible transformations and realized transformations are analytically distinct:

[
T_{real}subseteq T_{acc}
]

Equality is possible but is not assumed.

### P2 — Non-necessity of propagation

A modification of accessible transformation space does not necessarily modify realized trajectory:

[
Delta T_{acc}
eq0

otRightarrow
Delta H
eq0
]

The VSL result provides bounded synthetic support for this distinction under its frozen experimental definitions.

### P3 — Possible mediation by selection/realization

Under conditions in which the realization mechanism responds to a change in accessible transformations:

[
Delta T_{acc}
ightarrow
DeltaPi
ightarrow
Delta T_{real}
ightarrow
Delta H
]

may occur.

This is a candidate relationship requiring falsifiable testing.

### P4 — State/transformational-space sufficiency is testable

Whether `(S,T_acc)` is sufficient to explain realized trajectory is an empirical/formal question.

It must not be assumed either that:

[
(S,T_{acc})ightarrow H
]

is sufficient, or that an independent realization layer is necessarily irreducible.

---

## 9. TR-131 — State Sufficiency / Transformational-Space Irreducibility Test

### 9.1 Research question

Can the realized trajectory be explained from `(S,T_acc)` and already admitted contextual conditions without introducing an additional selection/realization variable or mechanism?

### 9.2 Sufficiency formulation

The sufficiency hypothesis can be represented as the existence of a function:

[
F_H(S,C,T_{acc})ightarrow H
]

such that the relevant trajectory is determined without an independent realization variable.

### 9.3 Irreducibility condition

A candidate counterexample consists of two controlled cases `A` and `B` satisfying:

[
(S,C,T_{acc})_A=(S,C,T_{acc})_B
]

while:

[
H_A
eq H_B
]

If this difference is reproducible under the frozen protocol, then `(S,C,T_acc)` is insufficient to determine the realized trajectory under that construction.

This would justify further examination of an independent realization/selection mechanism.

It would not, by itself, establish that `Π` must become part of the TGCV Core.

---

## 10. Minimal TR-131 experimental structure

The critical comparison should hold constant:

| Variable | Case A | Case B |
|---|---|---|
| Initial state `S₀` | identical | identical |
| Conditions `C` | identical | identical |
| Accessible space `T_acc` | identical | identical |
| Selection/realization mechanism | A | B |
| Realized transformation `T_real` | measured | measured |
| Trajectory `H` | measured | measured |

The central contrast is therefore:

[
(S,C,T_{acc})_A=(S,C,T_{acc})_B
]

with controlled variation in the candidate realization mechanism.

The critical outcome is:

[
H_A
eq H_B
]

under otherwise equivalent conditions.

---

## 11. Falsification conditions

The realization-layer hypothesis should not be treated as established if:

1. the two cases cannot be held equivalent with respect to `(S,C,T_acc)`;
2. the observed trajectory difference is attributable to an uncontrolled state or contextual difference;
3. the selection mechanism does not actually differ;
4. the difference disappears under independent reconstruction;
5. the trajectory difference cannot be operationally identified;
6. an equivalent explanatory representation using `(S,C,T_acc)` accounts for the result without the additional mechanism.

A negative result would therefore remain scientifically informative: it could support the sufficiency of the existing state/transformational-space representation under the tested construction.

---

## 12. Independence from downstream value

The realization layer is intentionally positioned before outcome and value:

[
T_{real}ightarrow Hightarrow Oightarrow V
]

TR-131 does not need to demonstrate a value effect.

The immediate question is narrower:

> Does an additional realization/selection mechanism become necessary to explain differences in realized trajectories?

This separation prevents the next experiment from conflating transformational accessibility with downstream value creation.

---

## 13. Relationship to the TGCV Core

The current TGCV Core remains unchanged.

In particular, this document does **not** establish:

[
Core=(S,T_{acc},Pi)
]

Instead:

[
Core_{current}=(S,T_{acc})
]

remains the working candidate representation, while `Π` is treated as a provisional auxiliary analytical construct pending TR-131.

Possible outcomes are therefore:

### Outcome A — sufficiency

`(S,T_acc)` is sufficient under the tested construction.

`Π` remains auxiliary or derivable.

### Outcome B — insufficiency

Controlled differences in realization/trajectory persist despite identical `(S,C,T_acc)`.

This provides evidence that the existing representation is insufficient and motivates a formal irreducibility assessment of `Π`.

### Outcome C — unresolved

The experiment cannot isolate the realization mechanism sufficiently.

No Core modification follows.

---

## 14. Governance status

At v0.1:

- **Core:** unchanged.
- **RMA:** unchanged.
- **Evidence-to-Claim Matrix:** unchanged.
- **C09:** unchanged.
- **VSL evidence:** unchanged.
- **TR-131:** not yet executed.
- **Empirical status of the realization layer:** unestablished.
- **`Π` as Core primitive:** unestablished.

This document is a conceptual and experimental-design artifact only.

---

## 15. Next scientific operation

The next operation is not another generic TGCV experiment.

It is the construction and audit of a frozen **TR-131 protocol** capable of distinguishing:

[
	ext{state/space sufficiency}
]

from:

[
	ext{irreducible realization/selection dependence}
]

Only after that protocol passes its own design and execution-integrity gates should TR-131 be executed.

The intended sequence is:

[
oxed{
	ext{Formalization}
ightarrow
	ext{Protocol}
ightarrow
	ext{Freeze}
ightarrow
	ext{Independent reconstruction}
ightarrow
	ext{Execution}
ightarrow
	ext{Interpretation}
}
]

No claim-level upgrade is implied at this stage.
