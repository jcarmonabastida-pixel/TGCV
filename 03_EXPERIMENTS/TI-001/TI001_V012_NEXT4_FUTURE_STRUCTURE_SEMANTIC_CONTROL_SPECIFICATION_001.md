# TI-001 V012 NEXT4 — Future-Structure Semantic and Control Specification 001

**Status:** DESIGN-REVIEW DRAFT — NOT EXECUTION AUTHORIZED  
**Date:** 2026-09-30  
**Parent specification:** TI001_V012_NEXT4_EXPERIMENTAL_SPECIFICATION_001

## 1. Purpose

This specification defines the provisional semantic object `future_structure` before any NEXT4 fixture is generated.

The purpose is to ensure that the future-structure manipulation is a genuine, auditable explanatory-variable intervention and is not a disguised encoding of:

- action identity;
- reward;
- utility;
- value;
- success/performance;
- presentation;
- profile identity itself;
- or the observed decision.

The variable is intentionally **not** identified with `T_acc`, `Reach` or `Trajectory` at this stage.

## 2. Semantic definition

`future_structure` is defined as a finite, externally specified description of the **reachable transformation topology associated with a profile after the present decision point**, expressed only through structural relations among future states and candidate transformations.

It describes **what transformation possibilities and transition relations exist downstream**, not which option is preferable and not which action was selected.

A future structure therefore has:

1. a set of future states;
2. a set of admissible transformation identities between those states;
3. structural relations among those transformations;
4. a bounded horizon;
5. no outcome/value label.

The representation is a structural object, not a scalar score.

## 3. Provisional representation

Each future structure is represented by a canonical finite directed labelled graph:

`F = (V, E, L)`

where:

- `V` = anonymised future-state nodes;
- `E` = directed transformation edges;
- `L` = structural transformation labels.

The canonical representation must include only structural information required to reconstruct the graph.

No node or edge may contain:

- action names A/B/C/D;
- chosen/not-chosen status;
- reward;
- utility;
- value;
- performance;
- success/failure;
- probability of selection;
- model output;
- presentation coordinates.

## 4. What the representation means

The graph represents a **future transformation topology**, not a prediction.

Examples of admissible structural properties include:

- branching factor;
- path depth;
- convergence/divergence;
- transformation identity turnover;
- reachability relations;
- dependency structure;
- composition of transformations.

These properties may be derived descriptively from the graph, but no scalar composite is to be introduced as the experimental signal.

## 5. Horizon restriction

The future graph must use a fixed finite horizon chosen before fixture generation.

The horizon must be identical across all future structures.

No future structure may encode a longer horizon as a proxy for desirability, complexity or success.

## 6. Profile separation

A profile and a future structure are distinct objects.

The same structural profile identity must be capable of being paired with multiple future structures.

Conversely, the same future structure must be capable of being paired with multiple profiles.

The fixture generator must verify these cross-pairing possibilities before freeze.

This is essential: if each profile has a unique immutable future structure, future_structure cannot be experimentally separated from profile_id.

## 7. Action independence

Future structures are generated before action selection and independently of the model's eventual response.

The future-structure generator must not receive:

- model response;
- chosen action;
- action probabilities;
- action scores;
- decision latency;
- any post-decision variable.

The complete generation provenance must be frozen and auditable.

## 8. No value or preference channel

No edge, node or graph-level field may encode:

- reward;
- utility;
- economic value;
- task success;
- target achievement;
- preference;
- fitness;
- performance.

There must be no scalar `future_value`, `future_score` or equivalent.

If two future structures differ in structural complexity, that difference is permitted only as an independently defined structural property and must not be assigned an evaluative interpretation.

## 9. No presentation channel

Future-structure identity must be independently randomized with respect to:

- profile position;
- presentation order;
- orientation;
- format;
- permutation index.

The same future structure must occur under multiple presentation configurations.

A decoder audit must verify that presentation variables do not predict future-structure identity above the frozen design expectation.

## 10. No profile-identity leakage

The graph labels and canonical serialization must not encode `profile_id`.

The same future structure must appear with different profile identifiers across the fixture.

Profile→future mapping is an experimental factor, not an intrinsic property of either object.

## 11. Counterfactual reassignment

For every stable mapping, NEXT4 must construct matched reassigned mappings using a pre-specified permutation family.

The reassignment must preserve:

- the multiset of profiles;
- the multiset of future structures;
- the candidate actions;
- the presentation distribution;
- the domain;
- the operationalisation;
- the replicate structure.

Only the mapping

`profile_i → future_structure_j`

changes.

The permutation family must include non-identity mappings and must be balanced so that each profile is paired with each future structure equally often, subject to the finite fixture constraints.

## 12. Null condition

`UNINFORMATIVE_NULL` must contain no recoverable profile→future correspondence.

It must not simply replace future structures with random noise if doing so changes the perceptual or structural burden of the task.

The null must be matched on surface format and structural description length as closely as the frozen design permits while removing the informative correspondence.

The exact null construction must be frozen in the fixture specification and audited separately.

## 13. Surface control

`SURFACE_CONTROL` must manipulate presentation while preserving the underlying profile→future mapping.

This control is intended to separate future-structure sensitivity from order, position, orientation and formatting effects.

Surface controls must not alter the graph itself.

## 14. Structural equivalence requirements

Stable and reassigned conditions must use the same future-structure inventory.

For every graph `F`, the following must remain invariant under reassignment:

- node count;
- edge count;
- label vocabulary;
- horizon;
- topology;
- canonical graph identity.

Only its association with a profile may change.

## 15. Leakage audits

Before fixture freeze, the following deterministic audits are mandatory.

### L1 — Action leakage

Verify that future_structure generation and identity are independent of action identity.

### L2 — Choice leakage

Verify that no future-structure field is derived from chosen/not-chosen status.

### L3 — Value leakage

Verify absence of reward, utility, value, performance and preference fields.

### L4 — Presentation leakage

Verify balanced future-structure occurrence across presentation strata.

### L5 — Profile leakage

Verify that each future structure can occur with multiple profile identities.

### L6 — Domain leakage

Verify that future structures are not uniquely associated with domain.

### L7 — Operationalisation leakage

Verify that future structures are not uniquely associated with operationalisation.

### L8 — Mapping integrity

Verify that the declared stable/reassigned mapping is exactly the mapping represented in the frozen fixture.

## 16. Semantic audit criterion

The semantic gate passes only if an independent audit can reconstruct:

`profile → future_structure → future transformation topology`

from the fixture without using:

- observed action;
- outcome;
- value;
- reward;
- presentation metadata as the semantic source;
- post-decision information.

A failed semantic or leakage audit blocks fixture freeze.

## 17. Relation to TGCV constructs

At this stage:

- `future_structure` is an experimental construct;
- it is not automatically `T_acc`;
- its graph edges may later be mapped to candidate transformations;
- its reachable-state relations may later inform a bounded `Reach` representation;
- its multi-step structure may later support a `Trajectory` operationalisation.

Such mappings require a separate semantic equivalence/translation audit.

No TGCV Core modification follows from this specification.

## 18. Primary scientific role

The future-structure variable exists solely to test whether the NEXT3 Q5 action–profile reorganisation tracks an independently manipulated future transformation structure.

The critical scientific observation is therefore not:

> profiles contain more information.

It is:

> action–profile correspondence changes when the independently specified future transformation structure associated with the profile changes.

## 19. Required next gate

Before creating the NEXT4 fixture, the following must be produced and reviewed:

1. canonical graph schema;
2. finite graph inventory;
3. balanced profile↔future permutation plan;
4. exact null construction;
5. exact surface-control construction;
6. deterministic leakage tests L1–L8;
7. sample records showing stable and reassigned mappings;
8. a formal counterfactual audit proving that only the intended mapping changes.

No scientific execution is authorized by this artifact.
