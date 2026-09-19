# TGCV — TR-131 Protocol v0.1

**Status:** PROTOCOL DRAFT — NOT FROZEN  
**Programme:** Teoría de Construcción de Valor de Sistemas Generativos (TGCV)  
**Test:** TR-131 — State Sufficiency / Transformational-Space Irreducibility Test  
**Precondition:** TGCV Realization / Selection Layer v0.1  
**Core impact:** NONE  
**Evidence Matrix impact:** NONE  
**Execution status:** NOT AUTHORIZED

---

## 1. Purpose

TR-131 tests whether the current candidate representation based on system state and accessible transformational space is sufficient to explain realized trajectory, or whether a distinct realization/selection mechanism is required.

The test is motivated by VSL Paired E1/E2 v001, which showed a bounded synthetic boundary case in which:

\[
\Delta T_{acc}\neq0,\quad \Delta H=0,\quad \Delta V^*=0
\]

The present test addresses a different question.

It does not test whether accessible transformation space can change.

It tests whether, when S, C, and T_acc are held constant, differences in a controlled realization/selection mechanism can produce differences in realized trajectory.

---

## 2. Scientific question

The primary question is:

> Is (S,C,T_acc) sufficient to explain the realized trajectory under a controlled construction, or is an additional realization/selection mechanism required?

The test is deliberately narrower than a test of value creation.

No value effect is required for TR-131.

---

## 3. Competing hypotheses

### H0 — State/space sufficiency

Under the frozen construction, realized trajectory is determined by the admissible state, conditions, and accessible transformational space:

\[
H=F_H(S,C,T_{acc})
\]

Therefore, when:

\[
(S,C,T_{acc})_A=(S,C,T_{acc})_B
\]

equivalent realizational conditions should not produce systematically different trajectories unless an already represented variable differs.

### H1 — Additional realization dependence

There exists a controlled realization/selection condition not reducible to (S,C,T_acc) such that:

\[
(S,C,T_{acc})_A=(S,C,T_{acc})_B
\]

while:

\[
H_A\neq H_B
\]

and the trajectory difference is attributable to the controlled realization/selection condition.

H1 is evidence of insufficiency of the current representation under the tested construction. It is not, by itself, proof that Π is a universal primitive or that it belongs in the TGCV Core.

---

## 4. Candidate realization operator

The provisional realization layer is:

\[
\Pi:(S,C,T_{acc},X)\rightarrow T_{real}
\]

with:

\[
T_{real}\subseteq T_{acc}
\]

X represents candidate realization/selection information or mechanism.

TR-131 must operationalize X independently from the variables whose sufficiency is being tested.

---

## 5. Critical invariants

The following must remain frozen and identical across the principal comparison:

- initial state S₀;
- contextual conditions C;
- accessible transformation space T_acc;
- transformation definitions;
- admissibility rules;
- transition function;
- trajectory definition;
- observation window;
- measurement procedure;
- dataset generation procedure;
- random seed policy, where applicable;
- software/environment specification;
- output schema;
- analysis code;
- exclusion rules.

Only the designated realization/selection condition may vary.

If any critical invariant differs unintentionally, the comparison is invalid for the primary TR-131 inference.

---

## 6. Experimental contrast

The minimal paired design is:

| Element | Case A | Case B |
|---|---|---|
| S₀ | frozen | identical |
| C | frozen | identical |
| T_acc | frozen | identical |
| transformation/admissibility rules | frozen | identical |
| transition function τ | frozen | identical |
| realization/selection condition X | X_A | X_B |
| T_real | observed | observed |
| trajectory H | observed | observed |

The controlled contrast is therefore:

\[
X_A\neq X_B
\]

subject to:

\[
(S_0,C,T_{acc})_A=(S_0,C,T_{acc})_B
\]

---

## 7. Operationalization requirements

Before freeze, the protocol must specify:

### 7.1 State

A finite, machine-readable representation of S₀.

### 7.2 Conditions

A complete representation of C sufficient to reproduce the test.

### 7.3 Accessible transformational space

An explicit enumeration or deterministic generator for T_acc.

The protocol must permit independent verification that:

\[
T_{acc,A}=T_{acc,B}
\]

### 7.4 Realization/selection condition

X_A and X_B must differ in a precisely specified way.

The difference must not silently modify S, C, T_acc, admissibility, or transition rules.

### 7.5 Realized transformation

T_real must be observable from the execution trace rather than inferred retrospectively from the final state.

### 7.6 Trajectory

H must have a deterministic representation from the sequence of states and realized transformations.

---

## 8. Primary outcome

The primary outcome is trajectory difference.

Define:

\[
D_H(H_A,H_B)
\]

as a pre-specified trajectory distance or equality predicate.

The primary binary outcome is:

\[
Y_H=
\begin{cases}
1 & \text{if }D_H(H_A,H_B)>0\\
0 & \text{otherwise}
\end{cases}
\]

The exact metric must be frozen before execution.

No post hoc trajectory metric selection is permitted.

---

## 9. Secondary outcomes

The protocol may record:

- T_real,A versus T_real,B;
- first divergence time;
- number of divergent transitions;
- terminal state difference;
- trajectory distance;
- downstream outcome O, if defined;
- value V, if defined.

These are secondary to the TR-131 question.

A downstream value difference must not be used to rescue an otherwise null trajectory result.

---

## 10. Identification condition

A positive TR-131 result requires all of the following:

1. S₀ equivalence is verified;
2. C equivalence is verified;
3. T_acc equivalence is verified;
4. all non-target rules are frozen and identical;
5. X_A and X_B are demonstrably different;
6. T_real is measured;
7. H is measured using the frozen definition;
8. H_A ≠ H_B under the pre-specified criterion;
9. the result survives independent reconstruction;
10. no identified invariant violation explains the difference.

If any of these conditions fails, the primary irreducibility inference is not established.

---

## 11. Negative-result interpretation

If:

\[
(S,C,T_{acc})_A=(S,C,T_{acc})_B
\]

and:

\[
H_A=H_B
\]

under the controlled realization contrast, the test does not establish irreducibility of Π.

It may support sufficiency of the tested representation, subject to the scope and limitations of the construction.

It does not prove universal sufficiency.

---

## 12. Positive-result interpretation

If the identification conditions are satisfied and:

\[
H_A\neq H_B
\]

then the result provides evidence that the current (S,C,T_acc) representation is insufficient to determine realized trajectory under the tested construction.

The appropriate conclusion is:

\[
(S,C,T_{acc})\not\Rightarrow H
\]

under the tested conditions.

The next step would be an irreducibility assessment of the candidate realization mechanism.

No automatic Core modification follows.

---

## 13. Falsification and invalidation rules

The primary result must be classified as invalid, unresolved, or non-informative for TR-131 if:

- T_acc differs between cases;
- hidden state differs;
- context differs;
- transition/admissibility rules differ;
- realization contrast is not isolated;
- trajectory metric was selected after observing outcomes;
- execution trace is incomplete;
- independent reconstruction fails;
- the apparent trajectory difference is attributable to an uncontrolled factor;
- the result depends on undocumented manual intervention.

---

## 14. Independence requirement

TR-131 requires an independent Executor-2 reconstruction.

Executor-2 must reconstruct from the frozen package without access to:

- Executor-1 results;
- Executor-1 interpretation;
- post-execution trajectory data;
- post-execution tuning;
- unfreezed implementation changes;
- coaching intended to reproduce a desired result.

The independent executor must independently verify:

\[
S_0,\ C,\ T_{acc},\ X_A,\ X_B,\ T_{real},\ H
\]

before comparison.

---

## 15. Required frozen package

Before authorization, the repository must contain a complete operational bundle containing at minimum:

1. protocol specification;
2. fixture or fixture-generation procedure;
3. operational definitions;
4. exact S₀ representation;
5. exact C representation;
6. exact T_acc construction;
7. exact X_A and X_B definitions;
8. transition function;
9. admissibility rules;
10. trajectory metric;
11. randomization/seed policy, if applicable;
12. null/control conditions, if applicable;
13. execution commands;
14. environment specification;
15. expected output schema;
16. integrity hashes;
17. independent reconstruction instructions;
18. audit worksheet.

The package must be executable by an independent executor without interpretive completion of missing scientific definitions.

---

## 16. Pre-execution gates

No scientific execution is authorized until the following gates pass:

### G1 — Conceptual consistency

The protocol is consistent with the Realization/Selection Layer v0.1.

### G2 — Operational completeness

All variables and outcome measures are operationally defined.

### G3 — Invariance completeness

The frozen invariants can be independently checked.

### G4 — Isolation of realization condition

X is the only intended experimental difference.

### G5 — Identifiability

The protocol can distinguish:

\[
T_{acc}
\]

from:

\[
T_{real}
\]

and both from:

\[
H
\]

### G6 — Executor-2 reproducibility

An independent executor can reconstruct the complete package.

### G7 — Integrity

Hashes, version identifiers, environment and execution instructions are frozen.

### G8 — Authorization

Only after G1-G7 pass may TR-131 scientific execution be authorized.

---

## 17. Governance boundaries

This protocol does not authorize:

- modification of the TGCV Core;
- changes to the Evidence-to-Claim Matrix;
- reopening of completed TGCV tests;
- reinterpretation of VSL beyond its closed bounded result;
- claim of empirical causality from a synthetic execution;
- generalization beyond the tested construction.

Any such change requires a separate governance decision after results are available.

---

## 18. Decision table

| Result | Interpretation | TGCV consequence |
|---|---|---|
| H_A = H_B, valid execution | No irreducibility demonstrated | Π remains auxiliary |
| H_A ≠ H_B, valid execution | Current representation insufficient under construction | Formal irreducibility assessment of Π |
| Invariant failure | Test invalid/unresolved | No scientific inference |
| Executor-2 failure | Execution not independently verified | No scientific inference |
| Ambiguous trajectory metric | Protocol failure | No primary inference |

---

## 19. Status and next action

**Current status:** DRAFT — NOT FROZEN  
**Scientific execution:** NOT AUTHORIZED  
**Core:** unchanged  
**RMA:** unchanged  
**Evidence Matrix:** unchanged

The next operation after this protocol draft is **not execution**.

It is a protocol audit focused on whether the proposed contrast is scientifically identifiable and whether X can genuinely be varied without changing S, C, or T_acc.

Only after that audit should the operational fixture and frozen execution bundle be constructed.
