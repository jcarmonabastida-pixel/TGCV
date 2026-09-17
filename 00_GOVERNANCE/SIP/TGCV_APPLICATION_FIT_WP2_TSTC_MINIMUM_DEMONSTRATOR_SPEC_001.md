# TGCV — WP2 TSTC Minimum Demonstrator Specification 001

**Status:** FROZEN — MINIMUM APPLIED-DEMONSTRATION SPECIFICATION
**Date:** 2026-09-17
**Purpose:** controlled applicability test after WP2 cross-case synthesis C01/C03/C04/C05/C08
**Predecessor:** `TGCV_APPLICATION_FIT_WP2_CROSS_CASE_SYNTHESIS_C01_C03_C04_C05_C08_001.md`

## 1. Objective

Specify the smallest reproducible demonstrator capable of testing the WP2 hypothesis that a TGCV representation can make explicit, across heterogeneous domains, how a state/context transition changes the accessible transformation space and propagates consequences to a subsequent trajectory.

The demonstrator is an **applicability artefact**, not a scientific validation experiment.

It must be capable of producing a negative result:

> if a conventional domain representation reconstructs the same information with equivalent assumptions and granularity, no differential TGCV contribution is claimed.

## 2. Minimum question

The demonstrator answers one bounded question:

> Given a frozen decision-time state and context, can the system explicitly reconstruct `T_acc`, apply a controlled transition, reconstruct `T_acc'`, and trace the resulting cross-domain trajectory using a common representation?

A secondary comparison asks:

> Can the same transformation-space transition be reconstructed equivalently using the selected conventional baseline?

No prediction of value, market fit, deployment benefit, or scientific superiority is required.

## 3. Minimal formal model

For each domain connector:

`S_t` = domain/system state

`C_t` = relevant context/conditions

`L` = governing/admissibility rules

`Uτ` = finite candidate transformation universe

`Pτ(S_t,C_t,L)` = outcome-independent admissibility predicate

`T_acc,t = {τ ∈ Uτ | Pτ(S_t,C_t,L)=1}`

A controlled transition `g` produces:

`(S_t,C_t) → (S_t+1,C_t+1)`

and therefore:

`T_acc,t → T_acc,t+1`.

A trajectory is a finite sequence of selected or simulated admissible transformations and resulting state/context transitions.

## 4. Minimum architecture

The demonstrator contains:

1. a **TGCV core representation layer**;
2. at least three domain connectors;
3. a finite candidate-transformation registry;
4. explicit admissibility predicates;
5. a transition engine;
6. an accessible-transformation-space calculator;
7. a trajectory recorder;
8. one conventional baseline per connector or one sufficiently expressive common baseline;
9. a comparison/reporting layer;
10. deterministic fixture/version metadata.

### Recommended first three connectors

The minimum three-domain configuration should instantiate structurally distinct patterns rather than reproduce one architecture three times:

- **Technical orchestration** — C01 pattern;
- **Agent/tool/permission** — C03 pattern;
- **Resource/constraint coupling** — C05 pattern.

C04 and C08 remain extension connectors for later phases.

## 5. Why three connectors are sufficient for the first demonstrator

The purpose is to test cross-domain portability, not coverage of all five cases.

Three connectors permit a controlled demonstration of:

- technical configuration change;
- capability/permission change;
- resource/constraint change.

Adding C04 and C08 before the minimum architecture works would increase implementation surface without resolving the primary applicability question.

This is an implementation-scope decision, not a scientific ranking of candidates.

## 6. Connector contract

Every connector MUST expose the same abstract interface:

### 6.1 State

A serialisable finite state object `S`.

### 6.2 Context

A serialisable finite context object `C`.

### 6.3 Rules

A versioned rule set `L`.

### 6.4 Candidate transformations

A finite list `Uτ`, where each transformation has:

- identifier;
- domain;
- preconditions;
- affected state variables;
- expected transition operator;
- optional resource/cost metadata.

### 6.5 Admissibility

A deterministic function:

`Pτ(S,C,L) → {0,1}`.

The predicate MUST NOT inspect downstream outcomes or post-transition performance.

### 6.6 Transition

A deterministic or explicitly seeded operator:

`τ(S,C) → (S',C')`.

### 6.7 Trajectory

A serialisable sequence:

`[(S0,C0), τ1, (S1,C1), τ2, ...]`.

## 7. Cross-domain coupling contract

A connector may publish one or more effects that alter another connector's admissibility conditions.

Minimum form:

`state/context transition in A`
→ `cross-domain condition update`
→ `Pτ_B changes`
→ `T_acc,B changes`.

The cross-domain effect MUST be explicit and versioned.

It MUST NOT be inferred retrospectively from the downstream outcome.

## 8. Clean intervention library

The first fixture should implement four clean interventions, of which at least three must be used:

### I1 — Capability/permission opening

`permission/tool unavailable → permission/tool available`.

### I2 — Resource constraint change

`available capacity ≥ threshold → available capacity < threshold`.

### I3 — Technical configuration change

`service/network configuration A → configuration B`.

### I4 — Optional institutional/physical extension

Reserved for C04/C08 in a later connector extension.

For each intervention all non-target variables remain frozen.

## 9. Baseline comparison

The first demonstrator should use deliberately simple conventional baselines.

### C01 baseline

Finite-state orchestration / rule-based feasible-action model.

### C03 baseline

Capability/access-control matrix plus workflow state.

### C05 baseline

Finite constrained-feasibility / resource-allocation model.

The baseline is not required to reproduce an industrial system. It must be sufficient to represent the same bounded candidate actions and constraints.

## 10. TSTC comparison protocol

For each connector:

1. freeze fixture version;
2. freeze `S0,C0,L`;
3. enumerate bounded `Uτ`;
4. calculate `T_acc,0`;
5. record the conventional baseline representation;
6. apply exactly one clean intervention;
7. calculate `T_acc,1`;
8. record newly opened/closed transformations;
9. execute a bounded trajectory or trajectory simulation;
10. record downstream state/context changes;
11. reconstruct the same sequence using the baseline;
12. compare representational content.

The comparison dimensions are:

- transformation identities represented;
- admissibility conditions represented;
- state/context dependencies represented;
- transition causing accessibility change;
- cross-domain dependency represented;
- trajectory consequence represented;
- assumptions required;
- information omitted.

No single aggregate score is authorised.

## 11. Minimal output schema

Each run MUST produce machine-readable records containing at least:

```text
fixture_id
fixture_version
connector_id
intervention_id
S0
C0
L_version
U_tau
T_acc_0
transition
S1
C1
T_acc_1
Delta_T_acc
trajectory
baseline_model
baseline_representation
baseline_reconstruction
comparison_observations
limitations
non_claims
execution_metadata
```

## 12. Required invariants

The demonstrator MUST verify:

- deterministic admissibility for a fixed fixture;
- no downstream outcome access by `Pτ`;
- `Uτ` is unchanged by the intervention unless the fixture explicitly defines otherwise;
- all reported `T_acc` members belong to `Uτ`;
- every `T_acc` member satisfies `Pτ=1`;
- every excluded candidate satisfies `Pτ=0`;
- intervention changes only declared variables;
- trajectory uses only admissible transformations;
- cross-domain effects are explicitly logged;
- baseline comparison uses the same frozen information where possible.

## 13. Reproducibility requirements

The artefact MUST include:

- fixture identifier;
- semantic version;
- source commit;
- configuration hash;
- rule-set hash;
- transformation-universe hash;
- intervention identifier;
- random seed if randomness is used;
- execution environment;
- generated output hash.

The first demonstrator should avoid randomness unless it is necessary.

## 14. Negative-control / falsification behaviour

At least one fixture MUST include a transition that changes a state variable but does **not** alter any admissibility predicate.

Expected result:

`ΔT_acc = ∅`.

This prevents the mapper from mechanically converting every state change into a transformation-space change.

A second optional control should change a downstream outcome while leaving `T_acc` unchanged.

This tests separation between accessibility and outcome.

## 15. Cross-domain test

At least one fixture MUST demonstrate:

`ΔT_acc,A ≠ ∅`

followed by an explicitly declared dependency such that:

`ΔT_acc,B ≠ ∅`.

A second fixture SHOULD test the inverse direction where feasible.

The mapper must distinguish:

- direct local accessibility change;
- propagated cross-domain accessibility change;
- no accessibility change;
- outcome-only change.

## 16. Minimum success criteria for applicability

The demonstrator reaches **APPLICABILITY DEMONSTRATED — BOUNDED** only if it can reproducibly:

1. instantiate all required connector contracts;
2. calculate `T_acc` before and after controlled intervention;
3. identify exact opened/closed transformations;
4. execute the declared trajectory;
5. show at least one explicit cross-domain propagation;
6. pass the negative control;
7. produce reproducible machine-readable output;
8. reconstruct the same bounded case in the conventional baseline.

This status says only that the representation can be instantiated and exercised in the bounded demonstrator.

## 17. Differential explanatory result categories

The comparison MUST use qualitative dispositions rather than a score:

- **EQUIVALENT REPRESENTATION:** baseline reconstructs the same information with materially comparable assumptions;
- **TGCV ADDITIONAL STRUCTURE OBSERVED:** TGCV exposes a relation not represented in the baseline under the tested formulation;
- **BASELINE ADDITIONAL STRUCTURE OBSERVED:** baseline captures relevant structure not captured by the TGCV fixture;
- **INCONCLUSIVE:** comparison is insufficient or assumptions are not matched.

None of these categories is a scientific claim by itself.

## 18. Failure conditions

The demonstrator MUST be treated as failed or inconclusive if:

- admissibility depends on downstream outcome;
- candidate transformations are changed silently by the intervention;
- cross-domain effects are inferred rather than declared;
- the baseline receives materially different information without justification;
- negative control produces unexplained `ΔT_acc`;
- reproducibility metadata are incomplete;
- trajectory uses transformations not present in `T_acc`;
- results cannot be reproduced from the frozen fixture.

## 19. Scientific boundary

A successful demonstrator does **not** establish:

- TGCV scientific validity;
- causal validity;
- superiority over existing methods;
- generality across real-world systems;
- value creation;
- deployment readiness;
- industrial ROI;
- `ΔT_acc → ΔV`.

A failed demonstrator does not refute TGCV generally; it constrains the applicability hypothesis tested by this fixture.

## 20. Next execution gate

Before implementation, freeze:

1. connector schemas;
2. one synthetic fixture per first three connectors;
3. exact `Uτ` for each fixture;
4. exact `Pτ` predicates;
5. exact intervention definitions;
6. baseline schemas;
7. output schema;
8. invariant tests;
9. negative control;
10. reproducibility metadata.

Only after this specification is frozen should implementation begin.

**Governance disposition:** WP2 moves from exploration to controlled Applied Demonstration specification. No scientific evidence is admitted by this document. No Core/RMA/Matrix/STATUS change is authorised.
