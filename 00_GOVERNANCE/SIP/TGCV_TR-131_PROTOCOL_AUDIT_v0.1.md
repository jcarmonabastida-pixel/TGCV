# TGCV — TR-131 Protocol Audit v0.1

**Status:** DESIGN AUDIT — NOT FROZEN  
**Protocol audited:** TGCV_TR-131_PROTOCOL_v0.1.md  
**Audit scope:** Identifiability of the proposed realization/selection contrast  
**Core impact:** NONE  
**Evidence Matrix impact:** NONE  
**Execution status:** NOT AUTHORIZED

---

## 1. Audit objective

This audit examines whether TR-131 v0.1 can isolate a realization/selection condition X while keeping the candidate explanatory representation (S,C,T_acc) invariant.

The audit is a design-integrity step. It does not execute TR-131 and does not establish evidence for or against the realization layer.

---

## 2. Critical finding

The protocol's central contrast is scientifically meaningful but requires one additional distinction before freeze.

The mere observation that:

\[
(S,C,T_{acc})_A=(S,C,T_{acc})_B
\]

while:

\[
X_A\neq X_B
\]

and:

\[
H_A\neq H_B
\]

does not, by itself, establish that X is an irreducible TGCV primitive.

It establishes, at most, that the current representation (S,C,T_acc) does not encode the controlled difference X sufficiently to predict the observed trajectory under the tested construction.

Therefore TR-131 must distinguish:

1. representation insufficiency;
2. formal irreducibility of the candidate realization mechanism.

The protocol already states that no automatic Core modification follows. This audit makes the distinction explicit.

---

## 3. Required causal isolation

The primary contrast must be:

\[
(S,C,T_{acc})_A=(S,C,T_{acc})_B
\]

with:

\[
X_A\neq X_B
\]

and all other operational variables invariant.

The protocol must additionally demonstrate:

\[
X\not\rightarrow S
\]

before the comparison,

\[
X\not\rightarrow C
\]

and:

\[
X\not\rightarrow T_{acc}
\]

except through an explicitly intended downstream realization operation.

Otherwise a change attributed to selection could actually be a hidden change in state, context, or accessible transformational space.

---

## 4. T_acc equality is necessary but not sufficient

A hash or equality check of the enumerated T_acc sets is required.

However, equality must be established at the operational representation level, not merely by asserting identical configuration files.

The audit therefore requires the frozen bundle to expose:

- canonical representation of each transformation;
- deterministic ordering or canonicalization;
- set/hash construction procedure;
- cardinality;
- equality/hash result for A and B.

The acceptance condition is:

\[
T_{acc,A}=T_{acc,B}
\]

under the canonical representation.

---

## 5. X must be independently observable

X cannot be defined retrospectively from the observed trajectory.

The bundle must specify:

- what X is;
- its admissible values;
- how it is instantiated;
- how its difference is verified;
- why it does not modify S, C, T_acc, admissibility, or transition rules.

The execution trace must record X before realization occurs.

---

## 6. Realized transformation must precede trajectory inference

The protocol correctly requires T_real to be observable.

This requirement is critical.

The execution trace should therefore expose, at minimum:

\[
(S_t,C_t,T_{acc,t},X_t,T_{real,t},S_{t+1})
\]

for every relevant transition.

H must then be derived from this trace using the frozen trajectory definition.

The final state alone is insufficient to establish the realized transformation sequence.

---

## 7. The trajectory metric must be fixed before execution

The current protocol correctly prohibits post hoc trajectory-metric selection.

The audit adds that the metric must be:

- deterministic;
- computable from the frozen trace;
- insensitive to irrelevant serialization differences;
- specified before fixture generation;
- independently executable.

For a first TR-131 construction, exact trajectory equality may be preferable to a discretionary distance threshold if the state and transformation representations permit it.

If a non-zero threshold is used, that threshold must itself be justified and frozen.

---

## 8. H0 requires refinement

The current H0 formulation says that equivalent realizational conditions should not produce systematically different trajectories unless an already represented variable differs.

Because TR-131 deliberately varies X, this wording can create a circularity.

The refined null is:

> Once all information represented by (S,C,T_acc) is held constant, variation in an external candidate variable X should not be required to predict H if (S,C,T_acc) is sufficient.

Operationally, the test is not whether X has an effect. It is whether the effect of X survives after demonstrating equality of all variables in the candidate representation.

Thus the inferential sequence should be:

\[
X_A\neq X_B
\]

then verify:

\[
(S,C,T_{acc})_A=(S,C,T_{acc})_B
\]

then observe:

\[
H_A\neq H_B
\]

and finally exclude known represented or uncontrolled explanations.

---

## 9. Irreducibility requires a second analytical step

A positive paired result should be labelled:

**REPRESENTATION INSUFFICIENCY — TR-131 POSITIVE**

rather than immediately:

**Π IRREDUCIBLE**

The latter requires an additional analysis asking whether X can itself be represented as part of an expanded state/context description without destroying the intended explanatory distinction.

The logical sequence is therefore:

\[
\text{paired divergence}
\rightarrow
\text{representation insufficiency}
\rightarrow
\text{irreducibility assessment}
\]

not:

\[
\text{paired divergence}
\rightarrow
\Pi\text{ is Core}
\]

This preserves the current Core boundary.

---

## 10. Required additions before protocol freeze

The following additions are mandatory:

### A1 — Explicit non-target invariance audit

Add an executable checklist verifying:

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

### A2 — Canonical T_acc representation

Specify canonicalization, cardinality, and hash/equality procedure.

### A3 — X declaration record

Define X before execution and record its values independently of outcomes.

### A4 — Trace schema

Freeze a transition-level trace containing:

\[
S_t,C_t,T_{acc,t},X_t,T_{real,t},S_{t+1}
\]

### A5 — Positive-result classification

Replace any direct implication of irreducibility with:

**TR-131 POSITIVE — REPRESENTATION INSUFFICIENCY**, pending separate irreducibility assessment.

### A6 — Expanded-state challenge

After a positive result, test whether X can be incorporated into an expanded state/context representation without making the explanation tautological or destroying the distinction being investigated.

---

## 11. Recommended decision rule after audit

TR-131 should produce one of four primary statuses:

| Status | Meaning |
|---|---|
| NEGATIVE_VALID | No trajectory divergence under valid controlled contrast |
| POSITIVE_REPRESENTATION_INSUFFICIENCY | Divergence survives all invariance checks |
| INVALID_INVARIANCE | S, C, T_acc or another frozen invariant differs |
| UNVERIFIED_INDEPENDENCE | Executor-2 cannot independently reproduce the comparison |

Only the second status should trigger a subsequent irreducibility assessment.

---

## 12. Governance consequence

This audit does not authorize execution.

It does not alter:

- TGCV Core;
- RMA;
- Evidence-to-Claim Matrix;
- VSL interpretation;
- C09;
- completed tests.

The protocol remains:

**DRAFT — NOT FROZEN**

until the six required additions are incorporated and audited.

---

## 13. Next operation

The next operation is to revise TGCV_TR-131_PROTOCOL_v0.1.md in GitHub, incorporating A1-A6.

After that revision, a second audit should verify the amended protocol before any fixture or execution bundle is created.
