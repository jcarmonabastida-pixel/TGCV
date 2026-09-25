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


## Authoritative deterministic semantics

The following semantics are now binding for V008.

### PRNG

- PRNG: xorshift32.
- State width: exactly 32 bits.
- Arithmetic: unsigned 32-bit; every state is reduced modulo 2^32 after each left-shift/XOR stage.
- Transition, in order:
  1. `state ^= (state << 13) & 0xFFFFFFFF`
  2. `state ^= state >> 17`
  3. `state ^= (state << 5) & 0xFFFFFFFF`
  4. final state is masked with `0xFFFFFFFF`.
- Zero state is invalid and MUST terminate generation rather than being repaired.
- Seed: decimal integer `20260925`.
- Condition stream initial state: seed.
- Presentation stream initial state: `seed XOR 0x9E3779B9`, reduced to 32 bits.
- The two streams are independent and MUST NOT share consumed state.
- No warm-up draws.
- Each Fisher-Yates iteration consumes exactly one PRNG draw.

### Fisher-Yates

- Input sequence is indexed from 0.
- Iteration is descending: `i = n-1, n-2, ..., 1`.
- At each iteration, consume one PRNG state and calculate `j = state % (i+1)`.
- Swap positions `i` and `j`.
- No rejection sampling, floating-point conversion, or additional draw.
- Condition labels before shuffle: 70 `control`, followed by 70 `treatment`, followed by 70 `null`.
- Presentation labels before shuffle: 105 `I1_FIRST`, followed by 105 `I2_FIRST`.
- Pair IDs are assigned in fixed lexical order `P001` through `P210`; shuffled condition and presentation labels are then assigned by pair position.

### Canonical self-test vectors

For seed `1`, the first five xorshift32 outputs MUST be:

`270369, 67634689, 2647435461, 307599695, 2398689233`.

For condition-stream seed `20260925`, the first five outputs MUST be:

`577347236, 639621434, 2049311590, 4078523939, 3799384941`.

For presentation-stream initial state `20260925 XOR 0x9E3779B9 = 2667729284`, the first five outputs MUST be:

`1936054461, 3325135876, 27233372, 4070243990, 71659122`.

For a four-element test sequence `[a,b,c,d]` using the condition stream, the final sequence MUST be `[b,d,c,a]`; the consumed swaps are `(i,j)=(3,0),(2,2),(1,0)`.

For the same sequence using the presentation stream, the final sequence MUST be `[c,a,d,b]`; the consumed swaps are `(3,1),(2,1),(1,0)`.

These vectors are design-test fixtures, not scientific observations.

### Generation restriction

The generator source MUST implement exactly these semantics. V008 fixture generation remains blocked until the implementation passes every self-test vector and the generator preflight binds the implementation blob SHA.
