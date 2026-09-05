# N-R8-C2 vNext — Freeze v0.1

## Status

**FROZEN FOR BOUNDED IDENTIFIABILITY PROBE ONLY**

This freeze follows `N-R8-C2_vNEXT_DERIVABILITY_AUDIT_v0.1.md` and freezes the candidate key before any probe implementation or result inspection.

## 1. Frozen matching key

For `State(V,E,q,objective)`:

`K_C2_vNext = B + degree-multiset(V)`

where:

`B = (|V|, q1, q2, q3, objective)`

and `degree-multiset(V)` is the canonical sorted tuple of `in_degree(v) + out_degree(v)` over all components `v` in `V`.

`|E|` is deliberately excluded because it is redundant with the degree sum.

## 2. Frozen construction rule

The key MUST be computed directly from the current state representation.

The implementation MUST NOT call or inspect:

- `enumerate_transformations`;
- `apply` / `apply_transformation`;
- `tacc`;
- any `R` encoder or R coordinate;
- `O_T`;
- any target-derived statistic.

## 3. Frozen target

The target remains `O_T`, the transformation-organisation observable defined from the valid one-step transformation universe and its commutation structure.

The probe asks whether `O_T` can vary while `K_C2_vNext` remains fixed.

## 4. Frozen witness class

At minimum the fixture generator must be able to represent the following two states, with identical resources and objective:

A:
- components `{A1,A2,B1,B2}`
- edges `{A1→A2, A2→B1, B1→B2, B2→A1}`

B:
- components `{A1,A2,B1,B2}`
- edges `{A1→A2, A2→A1, B1→B2, B2→B1}`

Both have degree multiset `(2,2,2,2)` and therefore identical `K_C2_vNext`.

The witness is a fixture adequacy condition, not evidence that `O_T` differs.

## 5. Frozen probe decision rule

Search for `(A,B)` satisfying:

`K_C2_vNext(A) = K_C2_vNext(B)`

and

`O_T(A) != O_T(B)`.

Interpretation:

- found → `IDENTIFIABLE` within the bounded fixture;
- not found → `UNRESOLVED_OR_DERIVED`;
- implementation/invariant failure → `BLOCKED_INFRASTRUCTURE`.

No bounded non-result may be converted into a global derivability claim.

## 6. Frozen scope

The probe is bounded and exhaustive over its declared fixture family.

It does not authorize:

- 5,000-pair corpus generation;
- Rust dataset processing;
- EXT-1.1 scientific execution;
- changes to N-R1.3;
- retrospective alteration of the C2 key after observing probe results.

Any change to this key requires a new versioned design, audit and freeze.

## 7. Next action

Implement the probe as a new versioned artifact using this freeze as its sole key specification. Do not modify the frozen historical C2 implementation.
