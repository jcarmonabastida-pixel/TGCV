# TI-001 V008 Generator Specification 001

**Status:** DESIGN — NOT GENERATED  
**Scientific execution:** NOT_PERFORMED

## Purpose

Define a deterministic, independently reproducible fixture generator before any V008 fixture is generated.

V008 is a new design identity. It does not modify or replace V007.

## Design inheritance

V008 preserves the validated V007 experimental structure unless a later design record explicitly changes it:

- 210 pairs;
- 70 control, 70 treatment, 70 null;
- 420 decision instances;
- 105 I1_FIRST and 105 I2_FIRST;
- decision actions A/B;
- treatment-only future structure;
- condition, pair identity and variant hidden from the agent;
- no successor realization before decision;
- no utility/reward/value/performance feedback.

Any deviation from these properties requires explicit design documentation and a new preflight.

## Deterministic generator requirements

The generator MUST define, in source and in this specification:

1. seed value and accepted representation;
2. PRNG word width;
3. unsigned integer arithmetic semantics;
4. initial state derivation from the seed;
5. exact state-transition equations;
6. exact shift constants;
7. shift operation semantics;
8. zero-state handling;
9. number and order of PRNG streams;
10. stream initialization;
11. Fisher-Yates iteration direction;
12. exact random draw consumed at each position;
13. random-value-to-index mapping;
14. bounded-index/rejection semantics, if applicable;
15. condition-label ordering;
16. presentation-order-label ordering;
17. pair-ID assignment order;
18. serialization/canonical JSON rules;
19. generator source identity and canonical Git blob binding.

## Independence requirement

Executor-2 MUST be able to reproduce the V008 fixture from this specification, the frozen generator source, and the declared seed without reading:

- the generated V008 fixture;
- Executor-1 output;
- model/API responses;
- scientific execution results.

The generated fixture is an output to be independently reconstructed, not an input used to infer the algorithm.

## Generation gate

No V008 fixture may be generated until:

- this specification is complete;
- the generator implementation is committed;
- the generator source is hash-bound;
- a deterministic self-test vector is recorded;
- an independent reconstruction can be implemented from the specification;
- generator preflight passes.

## Scientific boundary

Generator development and deterministic reconstruction are design/preflight activities.

They MUST retain:

`scientific_execution = NOT_PERFORMED`

No model/API call is permitted as part of generator validation.
