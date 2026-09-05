# EMP-1.1 — N-R1.1 HISTORICAL-TO-NEW SEMANTIC RECONCILIATION v0.1

**Date:** 2026-09-05  
**Branch:** N — Controlled New Reconstruction  
**Gate:** N-R1.1  
**Status:** CLOSED — RECONCILIATION COMPLETE; N-R1 REMAINS BLOCKED

## 1. Purpose

This gate reconciles the currently recoverable historical EMP-1.1/MVE artefacts with the new controlled operationalisation specified in `NEW_CONTROLLED_R_OPERATIONALISATION_SPECIFICATION_v0.1.md`.

The purpose is not historical code recovery. It is to determine which semantic elements can legitimately constrain the new reconstruction and which remain genuine new choices.

The historical numerical result is not used as evidence for, or as a tuning target for, any decision in this gate.

## 2. Evidence boundary

The reconciliation used the repository's frozen EMP-1.1 protocol/provenance/reconstruction documents and the recovered historical experiment artefacts. The historical recovery branch was previously closed negative: no complete historical executable semantics sufficient to recover the inequivalent choices was found.

Accordingly, absence of an artefact is recorded as `OPEN`, not converted into a historical claim.

## 3. Classification

- `RECOVERED`: explicitly supported by a retained historical artefact.
- `DERIVED`: follows mechanically from recovered/specification constraints.
- `RECONSTRUCTED`: new operational choice for Branch N.
- `OPEN`: insufficient evidence to choose without introducing a new decision.
- `REJECTED`: a previously proposed choice is removed because the available evidence does not justify it and it is not necessary to the controlled operationalisation.

## 4. Reconciled state representation

### 4.1 Components

Historical evidence supports a finite component universe of six named component identities: `A1, A2, B1, B2, C1, C2`, with experimental initial states containing 3–5 components.

**Classification: RECOVERED.**

Branch N therefore adopts this component universe rather than inventing a new domain.

### 4.2 Edges

Historical structural-intervention artefacts explicitly operate on component-edge structure and preserve edge count and degree-multiset controls while changing relational structure.

**Classification: RECOVERED.**

Direction is retained where represented by the computational graph. The neutral interpretation is: an edge is an observable directed relation in the experiment. No domain-specific causal/dependency semantics are inferred.

**Classification:** directed edge structure = RECOVERED; semantic interpretation as neutral relation = RECONSTRUCTED.

### 4.3 Resources

Historical artefacts identify three resource values and the frozen protocol identifies them as part of baseline `B`.

**Classification: RECOVERED / SPECIFIED.**

The exact value domain and transition/update equations are not sufficiently recoverable from the available artefacts.

**Classification: OPEN.**

Branch N must not invent resource dynamics unless they are required by the sealed generator and separately frozen.

### 4.4 Objectives

Historical protocol material identifies 12 objective identities.

**Classification: RECOVERED / SPECIFIED.**

Objective identity belongs to baseline `B`; it is not itself an accessible transformation.

### 4.5 Horizon

Historical protocol material identifies horizon `H=6`.

**Classification: RECOVERED / SPECIFIED.**

This belongs to outcome generation/evaluation and must not enter `R` through future trajectory information.

## 5. Transformation families

Historical evidence establishes that six transformation families existed in the prior experiment, but the currently recoverable artefacts do not provide a complete, auditable mapping from the six historical family identities to six exact predicates/transitions.

Therefore:

- number of families = **RECOVERED**;
- exact historical identities = **OPEN**;
- Branch N identities in v0.1 (`ADD_COMPONENT`, `REMOVE_COMPONENT`, `ADD_EDGE`, `REMOVE_EDGE`, `REWIRE_EDGE`, `MODIFY_ATTRIBUTE`) = **RECONSTRUCTED**, not recovered.

### 5.1 `MODIFY_ATTRIBUTE`

No sufficient evidence establishes that per-component attributes formed one of the six historical transformation families. The available evidence instead supports components, edges and three global/resource values.

**Decision: REJECTED from the default Branch N transformation universe.**

It may be reconsidered only as a separately justified new reconstruction version.

### 5.2 Resource transformation

Because three resource values are explicitly present in the experimental state, resource modification remains a candidate family for Branch N. Its exact semantics are not recovered.

**Classification: OPEN / candidate for RECONSTRUCTED family.**

### 5.3 Consequence

The six-family universe must be redesigned before N-R1 can pass. We must not force the historical count of six onto an unsupported list of operations.

## 6. Accessibility

The following abstract rule is retained:

`T_acc(S_t) = {τ ∈ U(S_t) : P_τ(S_t)=1}`

Accessibility is pre-state feasibility and does not depend on observed future occurrence or outcome.

**Classification:** formulation DERIVED; concrete candidate universe and predicates RECONSTRUCTED/OPEN.

No multi-step closure is included in primary `T_acc`.

## 7. Transition semantics

The generic deterministic partial transition form remains valid:

`P_τ(S_t)=1 => S_{t+1}=τ(S_t)`.

However, exact update equations for components, edges and resources are not fully recoverable.

**Classification:** generic form DERIVED; family-specific transition equations OPEN.

Fail-closed behaviour for undefined operations is a new methodological rule and therefore RECONSTRUCTED.

## 8. R representation

The earlier v0.1 proposal contained four blocks, including an attribute-dependent block. Following this reconciliation:

- family availability: RECONSTRUCTED candidate;
- family cardinalities: RECONSTRUCTED candidate;
- component-incidence structural summaries: RECONSTRUCTED candidate;
- transition-result signatures: RECONSTRUCTED candidate;
- per-component attribute contribution: REJECTED unless independently justified.

The exact dimensionality, caps, quantiles and numerical encoding remain OPEN.

## 9. Baseline B

The baseline definition is preserved from the frozen protocol:

- component count;
- three resource values;
- objective identity.

**Classification: SPECIFIED.**

Branch N must not add relational information to B merely to improve comparability.

## 10. Generator and data boundary

The historical artefacts support the existence of a finite synthetic experimental world and fixed objective/resource/component structure, but do not provide a complete recoverable generator implementation.

Therefore:

- historical generator identity = OPEN;
- Branch N generator = RECONSTRUCTED if new episodes are generated;
- historical final result = NEVER an input to generator design;
- sealed evaluation data, if retained, must remain immutable.

## 11. What is now closed

The reconciliation establishes the following without overclaiming:

1. Branch N should use the recovered six-component universe rather than inventing a new component domain.
2. Branch N should retain directed relational structure.
3. Branch N should retain the three resource values and 12 objective identities at the state/baseline level.
4. `H=6` belongs to the outcome horizon, not `R`.
5. `MODIFY_ATTRIBUTE` is removed from the default six-family proposal.
6. The six-family count is retained as a historical constraint, but exact family semantics remain open.
7. `T_acc` remains one-step, pre-state, feasibility-defined.
8. Historical EMP-1.1 numerical results remain archival and cannot resolve the missing semantics.

## 12. Remaining blockers for N-R1

The following must be resolved before semantic completeness can PASS:

1. exact six Branch N transformation families;
2. exact candidate universe for each family;
3. exact component-addition/removal semantics;
4. exact edge-addition/removal/rewire semantics;
5. exact resource transformation semantics, if applicable;
6. exact resource domains and admissible values;
7. exact state-validity predicates;
8. exact R dimensionality and feature ordering;
9. exact handling of empty/degenerate structures;
10. exact numerical aggregation conventions.

Model hyperparameters, permutation seed and confirmatory split are deliberately deferred to later gates and do not belong to N-R1 semantic completeness.

## 13. Gate decision

**N-R1.1 — PASS / CLOSED.**

This is a reconciliation gate, not the semantic-completeness gate itself.

**N-R1 — BLOCKED / NOT YET PASS.**

The correct next operation is to construct `N-R1.2 — Branch N Transformation-System Specification`, using the recovered six-component/three-resource/12-objective domain and explicitly resolving the six transformation families without consulting the historical result.

## 14. Scientific interpretation

This gate improves traceability but does not strengthen the historical EMP-1.1 result. It establishes a cleaner boundary between recovered experimental-domain facts and newly reconstructed semantics.

No confirmatory execution is authorized by this gate.
