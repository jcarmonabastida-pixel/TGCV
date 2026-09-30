# TI-001 V012 NEXT4 — Future-Structure Schema and Permutation Plan 001

**Status:** DESIGN REVIEW — NOT EXECUTION AUTHORIZED  
**Date:** 2026-09-30  
**Parent:** TI001_V012_NEXT4_FUTURE_STRUCTURE_SEMANTIC_CONTROL_SPECIFICATION_001

## 1. Objective

Define the canonical finite representation of `future_structure` and the balanced counterfactual permutation plan required before fixture generation.

This artifact defines the representation and design algebra only. It does not create the scientific fixture and does not authorize execution.

## 2. Canonical graph schema

Each future structure is a directed labelled graph:

`F = (V,E,L,H)`

where:

- `V`: anonymised future-state nodes;
- `E`: directed transformation edges;
- `L`: transformation-type labels;
- `H`: fixed finite horizon.

Each node record contains only:

- `node_id`: canonical local identifier;
- `depth`: integer in `[0,H]`.

Each edge record contains only:

- `source`;
- `target`;
- `transform_id`;
- `transform_type`.

No node or edge may contain action, choice, reward, value, utility, performance, presentation or profile identifiers.

## 3. Canonical serialization

Graph identity is determined by canonical serialization:

1. nodes sorted by depth then node_id;
2. edges sorted by source, target, transform_id;
3. labels represented by an immutable vocabulary;
4. no presentation metadata included;
5. no profile or action metadata included.

The canonical serialized representation is hashed. The hash identifies the future structure independently of where it is assigned.

## 4. Structural inventory

The initial inventory shall contain a balanced finite set of graph topologies rather than a single graph.

The inventory must include structural variation sufficient to distinguish:

- linear progression;
- branching;
- convergence;
- mixed branching/convergence;
- multi-step composition.

Each topology must have a matched structural complexity class so that graph size itself cannot become an unintended condition signal.

The exact graph inventory is to be generated deterministically from a frozen generator specification after this design review. No inventory is considered scientifically frozen by this document alone.

## 5. Structural matching

Every inventory class must be balanced on:

- node count;
- edge count;
- horizon;
- label vocabulary size.

Where exact equality is impossible, the difference must be explicitly declared and included in the pre-execution audit rather than hidden by post-hoc normalisation.

No scalar complexity score is used as the scientific signal.

## 6. Profile namespace

Profiles and future structures use independent namespaces.

Example:

- profiles: `P01...P04`;
- future structures: `F01...FN`.

No identifier may contain information about the other namespace.

The same profile must occur with multiple future structures, and the same future structure must occur with multiple profiles.

## 7. Core permutation family

For a four-profile unit, define a balanced permutation family over the four future structures.

The minimum family is the full set of 24 permutations of four elements.

For each base mapping:

`M0 = [F1,F2,F3,F4]`

the reassignment condition may use:

`Mπ = π(M0)`

with `π` drawn from the frozen permutation family.

The 24 permutations provide:

- identity mapping;
- all non-identity reassignment patterns;
- balanced exposure of every profile to every future structure.

The final fixture must specify whether all 24 permutations are used and how replicates are allocated. This allocation must be frozen before fixture generation.

## 8. Counterfactual pair construction

Each stable mapping must have one or more reassigned counterparts.

A matched pair is valid only if:

- profiles are identical;
- candidate actions are identical;
- future-structure multiset is identical;
- domain is identical;
- operationalisation is identical;
- presentation distribution is identical;
- only profile→future mapping differs.

The pair identifier must be immutable and independent of model output.

## 9. Presentation orthogonality

Permutation index must be independently balanced against:

- order;
- position;
- orientation;
- format.

For every future-structure permutation, the fixture must contain multiple presentation configurations.

A deterministic audit must reject any design in which future-structure identity can be reconstructed from presentation metadata alone.

## 10. Domain orthogonality

The same future-structure inventory and permutation family must be used across all domains.

For every domain:

- stable mappings occur;
- non-identity mappings occur;
- each future structure is exposed across multiple profiles;
- presentation permutations remain balanced.

No future structure may become a domain marker.

## 11. Operationalisation orthogonality

The same future-structure semantics must be used across operationalisations.

Operationalisation may alter the external rendering only if the semantic audit proves equivalence.

No operationalisation may receive a unique subset of future structures.

## 12. Null design

The null condition must preserve the surface burden of the informative conditions while eliminating recoverable profile→future correspondence.

The null construction is deliberately left as a separate frozen sub-specification because its validity cannot be established merely by choosing random labels.

The null must pass the same leakage and presentation audits as informative conditions.

## 13. Surface-control design

Surface control uses the same future-structure mapping as its paired informative condition but applies a pre-specified presentation permutation.

The graph identity and profile→future mapping remain invariant.

This permits separation of semantic reassignment from presentation changes.

## 14. Design invariants

Before fixture freeze, deterministic checks must verify:

`profiles(stable) = profiles(reassigned)`

`actions(stable) = actions(reassigned)`

`future_structures(stable) = future_structures(reassigned)`

`domain(stable) = domain(reassigned)`

`operationalisation(stable) = operationalisation(reassigned)`

`presentation_distribution(stable) ≈ presentation_distribution(reassigned)`

and:

`mapping(stable) != mapping(reassigned)`

for every non-identity counterfactual pair.

## 15. Identification matrix

The final design must identify independently:

| Variable | Independent variation required |
|---|---|
| profile_id | Yes |
| action_identity | Yes |
| future_structure_id | Yes |
| profile→future mapping | Yes |
| condition | Yes |
| presentation | Yes |
| domain | Yes |
| operationalisation | Yes |
| replicate | Yes |

The design is invalid if any declared primary interaction is structurally aliased.

## 16. Required deterministic audits

Before fixture freeze:

- **S1 Schema audit:** every graph conforms to the canonical schema.
- **S2 Serialization audit:** identical graphs have identical hashes.
- **S3 Namespace audit:** profile/action/future identifiers are disjoint.
- **S4 Cross-pair audit:** profiles and future structures are independently reusable.
- **S5 Permutation audit:** permutation family is complete/balanced as declared.
- **S6 Counterfactual audit:** stable/reassigned pairs differ only in mapping.
- **S7 Presentation audit:** no future mapping is recoverable from presentation.
- **S8 Domain audit:** no future structure is a domain marker.
- **S9 Operationalisation audit:** no future structure is an operationalisation marker.
- **S10 Null audit:** null removes recoverable semantic correspondence without introducing an unmatched surface burden.

Any failed audit blocks fixture freeze.

## 17. Deliberate non-commitments

This document does not yet freeze:

- the exact graph inventory;
- the final number of decision units;
- the null encoding;
- the model formula;
- the multiplicity family;
- the API prompt;
- token budget;
- execution seed.

Those belong to later specifications and gates.

## 18. Next required artifact

The next artifact must be the **deterministic future-structure generator and null/control construction specification**.

Only after that specification passes semantic review should a fixture be generated.

No scientific execution is authorized.
