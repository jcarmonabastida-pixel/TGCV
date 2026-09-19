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

variation in a candidate external realization variable X should not be necessary to predict H if (S,C,T_acc) is sufficient.

### H1 — Additional realization dependence

There exists a controlled realization/selection condition not represented by (S,C,T_acc) such that:

\[
(S,C,T_{acc})_A=(S,C,T_{acc})_B
\]

while:

\[
H_A\neq H_B
\]

and the trajectory difference is attributable to the controlled realization/selection condition.

H1 is evidence of **representation insufficiency under the tested construction**. It is not, by itself, proof that Π is a universal primitive or that it belongs in the TGCV Core.

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

A positive result must not be labelled “Π irreducible” without a subsequent irreducibility assessment.

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

Only the designated realization/selection condition X may vary.

The protocol must explicitly verify that the intended variation in X does not alter the candidate explanatory representation before realization:

\[
X\not\rightarrow S
\]

\[
X\not\rightarrow C
\]

\[
X\not\rightarrow T_{acc}
\]

except through the explicitly intended downstream realization operation.

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

The paired design is interpretable only if equality of the non-target representation is independently verified rather than inferred from identical configuration or fixture files.

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

Equality must be checked using a canonical transformation representation, deterministic ordering/canonicalization, cardinality, and a reproducible set/hash procedure.

### 7.4 Realization/selection condition

X_A and X_B must differ in a precisely specified way.

The protocol must declare X before execution, specify its admissible values, instantiate it deterministically or according to a frozen randomization procedure, and record it in the execution trace before realization occurs.

The difference must not silently modify S, C, T_acc, admissibility, or transition rules.

### 7.5 Realized transformation

T_real must be observable from the execution trace rather than inferred retrospectively from the final state.

### 7.6 Trajectory

H must have a deterministic representation derived from the sequence of states and realized transformations.

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

The exact metric or equality predicate must be frozen before fixture generation and execution.

It must be deterministic, computable from the frozen transition trace, insensitive to irrelevant serialization differences, and independently executable.

Where the representation permits exact comparison, exact trajectory equality should be preferred to a discretionary distance threshold. If a non-zero threshold is used, its value and justification must be frozen before execution.

No post hoc trajectory metric selection is permitted.

---

## 9. Required transition trace

The operational bundle must produce a transition-level trace exposing, for every relevant transition at minimum:

\[
(S_t,C_t,T_{acc,t},X_t,T_{real,t},S_{t+1})
\]

The trajectory H must be derived from this trace using the frozen trajectory definition.

The final state alone is insufficient to establish the realized transformation sequence.

The trace must make it possible to independently verify:

1. X_A ≠ X_B;
2. S_A = S_B at the relevant comparison points;
3. C_A = C_B;
4. T_acc,A = T_acc,B;
5. T_real,A and T_real,B;
6. H_A and H_B.

---

## 10. Secondary outcomes

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

## 11. Identification condition

A positive TR-131 result requires all of the following:

1. S₀ equivalence is verified;
2. C equivalence is verified;
3. T_acc equivalence is verified;
4. equality of transformation/admissibility/transition definitions is verified;
5. X_A and X_B are demonstrably different;
6. T_real is measured from the execution trace;
7. H is derived using the frozen definition;
8. H_A ≠ H_B under the pre-specified criterion;
9. the result survives independent reconstruction;
10. no identified invariant violation or uncontrolled factor explains the difference.

If any of these conditions fails, the primary **representation-insufficiency** inference is not established.

---

## 12. Negative-result interpretation

If:

\[
(S,C,T_{acc})_A=(S,C,T_{acc})_B
\]

and:

\[
H_A=H_B
\]

under the controlled realization contrast, the test does not establish representation insufficiency or irreducibility of Π.

It may support sufficiency of the tested representation, subject to the scope and limitations of the construction.

It does not prove universal sufficiency.

---

## 13. Positive-result interpretation

If the identification conditions are satisfied and:

\[
H_A\neq H_B
\]

then the result is classified:

**TR-131 POSITIVE — REPRESENTATION INSUFFICIENCY**

The result provides evidence that the current (S,C,T_acc) representation is insufficient to determine realized trajectory under the tested construction:

\[
(S,C,T_{acc})\not\Rightarrow H
\]

under the tested conditions.

This is not yet a finding that Π is irreducible.

The next step is a separate **irreducibility assessment** asking whether X can be incorporated into an expanded state/context representation without making the explanation tautological or destroying the intended explanatory distinction.

No automatic Core modification follows.

---

## 14. Falsification and invalidation rules

The primary result must be classified as invalid, unresolved, or non-informative for TR-131 if:

- T_acc differs between cases;
- hidden state differs;
- context differs;
- transition/admissibility rules differ;
- realization contrast is not isolated;
- X is defined retrospectively from observed outcomes;
- trajectory metric was selected after observing outcomes;
- execution trace is incomplete;
- independent reconstruction fails;
- the apparent trajectory difference is attributable to an uncontrolled factor;
- the result depends on undocumented manual intervention.

---

## 15. Independence requirement

TR-131 requires an independent Executor-2 reconstruction.

Executor-2 must reconstruct from the frozen package without access to:

- Executor-1 results;
- Executor-1 interpretation;
- post-execution trajectory data;
- post-execution tuning;
- unfrozen implementation changes;
- coaching intended to reproduce a desired result.

The independent executor must independently verify:

\[
S_0,\ C,\ T_{acc},\ X_A,\ X_B,\ T_{real},\ H
\]

before comparison.

---

## 16. Required frozen package

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
10. trajectory metric or exact equality predicate;
11. canonical T_acc representation and hash/equality procedure;
12. transition-trace schema;
13. randomization/seed policy, if applicable;
14. null/control conditions, if applicable;
15. execution commands;
16. environment specification;
17. expected output schema;
18. integrity hashes;
19. independent reconstruction instructions;
20. audit worksheet;
21. explicit non-target invariance checklist.

The package must be executable by an independent executor without interpretive completion of missing scientific definitions.

---

## 17. Pre-execution gates

No scientific execution is authorized until the following gates pass:

### G1 — Conceptual consistency

The protocol is consistent with the Realization/Selection Layer v0.1.

### G2 — Operational completeness

All variables and outcome measures are operationally defined.

### G3 — Invariance completeness

The frozen invariants can be independently checked, including:

\[
S_A=S_B
\]

\[
C_A=C_B
\]

\[
T_{acc,A}=T_{acc,B}
\]

and equality of transition/admissibility definitions.

### G4 — Isolation of realization condition

X is the only intended experimental difference and the protocol demonstrates that X does not alter S, C, or T_acc except through the intended downstream realization operation.

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

## 18. Governance boundaries

This protocol does not authorize:

- modification of the TGCV Core;
- changes to the Evidence-to-Claim Matrix;
- reopening of completed TGCV tests;
- reinterpretation of VSL beyond its closed bounded result;
- claim of empirical causality from a synthetic execution;
- generalization beyond the tested construction.

Any such change requires a separate governance decision after results are available.

A TR-131 positive result does not automatically alter the Core. It first triggers a separate irreducibility assessment.

---

## 19. Decision table

| Result | Interpretation | TGCV consequence |
|---|---|---|
| H_A = H_B, valid execution | No representation insufficiency demonstrated | Π remains auxiliary |
| H_A ≠ H_B, valid execution | Representation insufficiency under construction | Separate irreducibility assessment of Π |
| Invariant failure | Test invalid/unresolved | No scientific inference |
| Executor-2 failure | Execution not independently verified | No scientific inference |
| Ambiguous trajectory metric | Protocol failure | No primary inference |

---

## 20. Explicit non-target invariance audit

Before freeze and before each scientific execution, the operational audit must produce machine-checkable results for:

### A1 — State invariance

\[
S_A=S_B
\]

with a canonical state representation and reproducible equality/hash result.

### A2 — Context invariance

\[
C_A=C_B
\]

with a canonical representation and reproducible equality/hash result.

### A3 — T_acc invariance

\[
T_{acc,A}=T_{acc,B}
\]

with canonical transformation representation, cardinality, and set/hash result.

### A4 — Rule invariance

Transformation definitions, admissibility rules, transition function, observation window, measurement procedure, and analysis code must be identical or explicitly hash-equivalent.

The audit must fail closed if any required equality cannot be established.

---

## 21. X declaration and trace audit

Before execution, an X declaration record must specify:

- X definition;
- admissible values;
- X_A;
- X_B;
- instantiation procedure;
- randomization procedure, if any;
- expected location in the trace;
- verification that X is present before realization;
- verification that X does not alter S, C, T_acc, admissibility, or transition rules except through the intended realization operation.

The declaration record is frozen with the protocol.

X must never be defined as a function of H, O, V, T_real, or any post-execution result.

---

## 22. Expanded-state challenge

A TR-131 positive result establishes representation insufficiency, not formal irreducibility.

Before considering any Core modification, the candidate realization information X must be subjected to an expanded-state challenge.

The challenge asks whether an equivalent representation can be constructed:

\[
S' = G(S,C,X)
\]

or, where appropriate:

\[
C' = G(C,X)
\]

such that the observed trajectory can be represented without a separate Π while preserving the intended explanatory distinction.

The challenge must avoid tautological constructions in which the entire outcome or trajectory is simply encoded into the expanded state.

A positive TR-131 result followed by successful expanded-state representation would therefore not justify declaring Π irreducible.

Only if the additional realization dependence survives this challenge does a formal irreducibility assessment become warranted.

---

## 23. Status and next action

**Current status:** DRAFT — NOT FROZEN  
**Scientific execution:** NOT AUTHORIZED  
**Core:** unchanged  
**RMA:** unchanged  
**Evidence Matrix:** unchanged

The protocol has incorporated the six design-audit requirements A1-A6:

- A1 — explicit non-target invariance audit;
- A2 — canonical T_acc representation;
- A3 — X declaration record;
- A4 — transition-level trace schema;
- A5 — positive-result classification as representation insufficiency;
- A6 — expanded-state challenge.

The next operation is a **second protocol audit** of this amended version.

Only after that audit passes should the operational fixture and frozen execution bundle be constructed.
