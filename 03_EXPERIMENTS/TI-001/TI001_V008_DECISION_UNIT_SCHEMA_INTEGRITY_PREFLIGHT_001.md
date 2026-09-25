# TI-001 V008 Decision Unit Schema Integrity Preflight 001

**Status:** READY — NOT EXECUTED
**Preflight ID:** TI001-V008-DU-SCHEMA-PREFLIGHT-001
**Schema ID:** TI001-V008-DU-SCHEMA-001
**Scientific execution:** NOT_PERFORMED
**Fixture generated:** false

## Purpose

Validate the V008 Decision Unit Schema Specification before any generator modification or fixture generation.

## Required checks

The preflight implementation MUST verify, from the canonical schema specification:

1. schema file exists;
2. schema identity is present and exact;
3. schema is explicitly identified as new V008 design;
4. exactly seven Decision Unit fields are defined;
5. field order is exact;
6. `decision_id` type and D001–D420 range are defined;
7. `pair_id` type and P001–P210 range are defined;
8. condition vocabulary is exactly control/treatment/null;
9. presentation vocabulary is exactly I1_FIRST/I2_FIRST;
10. context fields are exactly items/item_count;
11. context contains exactly two alternatives;
12. I1 maps to A and I2 maps to B;
13. available_actions is exactly A/B;
14. future_structure fields are exactly successor_realized/future_structure_available;
15. treatment-only future structure is defined;
16. successor_realized is false for all conditions;
17. agent-facing fields are exactly context/available_actions/future_structure;
18. hidden assignment fields are decision_id/pair_id/condition/presentation;
19. prohibited information list is present;
20. pair cardinality is 210;
21. decision-unit cardinality is 420;
22. two decision units per pair are defined;
23. each pair has I1_FIRST then I2_FIRST canonical order;
24. condition allocation is 70/70/70 pairs;
25. decision allocation is 140/140/140;
26. UTF-8 serialization is specified;
27. compact JSON serialization is specified;
28. exactly one final LF and no BOM are specified;
29. top-level field order is specified;
30. provenance fields are specified;
31. generator ID and seed are bound;
32. deterministic generator semantics are referenced without redefining them;
33. Executor-2 independence boundary is specified;
34. scientific execution remains NOT_PERFORMED;
35. generation remains prohibited pending preflight/gate completion.

## Binding checks

The executed preflight MUST calculate the Git blob SHA-1 of the exact canonical schema specification and report it.

Expected schema blob SHA MUST NOT be hard-coded until calculated from the committed artifact.

The preflight result MUST identify:

- `preflight_id`;
- `schema_id`;
- canonical schema path;
- schema blob SHA-1;
- all individual check results;
- aggregate status.

## Scientific boundary

The preflight MUST NOT invoke a model/API, generate a fixture, or consume scientific responses.

Expected state:

`scientific_execution = NOT_PERFORMED`

`fixture_generated = false`

## Failure semantics

Any failed check yields:

`status = FAIL`

No generator modification or fixture generation is authorized from a failed preflight.

## Exit condition

A PASS permits the next controlled action: reconcile the generator implementation with the approved schema, if necessary, and create the generator/schema binding preflight.

A PASS does not itself authorize fixture generation.
