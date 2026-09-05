# N-R8-C2 vNext — Derivability / Non-Circularity Audit v0.1

## Status

**AUDITED — CANDIDATE PASSES DESIGN-LEVEL AUDIT; PROBE NOT YET EXECUTED**

This audit evaluates the candidate defined in `N-R8-C2_vNEXT_DESIGN_v0.1.md`. It is a design audit only. It does not establish empirical identifiability and does not authorize corpus generation.

## 1. Candidate under audit

`K_C2_vNext = B + (|E|, degree-multiset(V))`

where `B = (|V|, q1, q2, q3, objective)` and the degree multiset is the sorted multiset of total directed incidences `in_degree + out_degree` for the current components.

## 2. Audit A — Direct dependence on R

**PASS.**

The candidate key is computed from the current `State` fields only:

- component set `V`;
- edge set `E`;
- resource vector `q`;
- objective.

It does not call or inspect:

- `enumerate_transformations`;
- `apply`;
- `tacc`;
- `encode_r`;
- `R1`, `R2`, `R3`, or `R4`;
- `O_T`.

Therefore no R coordinate is directly embedded in the key.

## 3. Audit B — Indirect dependence through transformation-derived statistics

**PASS, with one deliberate redundancy.**

`|E|` is a state property, not a statistic computed from `T_acc`. The degree multiset is likewise computed directly from `(V,E)`.

The fact that some transformation counts may be mathematically inferable from `|V|`, `|E|`, or the degree sequence does not make the key transformation-derived. The direction of construction remains state → key, not transformation universe → key.

The candidate therefore avoids the previous C2 failure mode, where R1–R3 were explicitly fixed and the remaining R coordinates became derivable.

## 4. Audit C — Separation from target observable

**PASS.**

`O_T` is defined downstream from the one-step transformation universe and its organisation. The candidate key is defined upstream from the current state snapshot.

Consequently the key does not inspect the target observable and cannot be tuned using target values.

This preserves result-blind construction.

## 5. Audit D — Existence of the intended matching class

**PASS at fixture-design level.**

A concrete four-component witness family exists under the frozen state representation.

Let all components be `{A1,A2,B1,B2}`, resources and objective be identical, and consider two directed graphs with four edges:

**Graph A — directed 4-cycle**

`A1→A2, A2→B1, B1→B2, B2→A1`

**Graph B — two directed 2-cycles**

`A1→A2, A2→A1, B1→B2, B2→B1`

Both states have:

- `|V| = 4`;
- `|E| = 4`;
- total-degree multiset `(2,2,2,2)`;
- identical resources;
- identical objective.

Hence they collide under `K_C2_vNext` while their edge arrangements are non-isomorphic. This establishes that the intended structural degree of freedom is non-empty without evaluating `T_acc` or `O_T`.

## 6. Audit E — Scientific independence of the degree of freedom

**PASS provisionally.**

The witness demonstrates that the key does not identify the full edge arrangement. The remaining arrangement information is therefore genuinely absent from the matching key.

Whether that omitted arrangement information changes `O_T` is an empirical question for the bounded probe. It must not be assumed from non-isomorphism alone.

## 7. Audit F — Result-blindness

**PASS.**

The key definition can be implemented as a pure function of `State`. The fixture can be generated before target evaluation. No collision selection criterion may reference `O_T` other than the final identifiability test.

## 8. Important qualification

The candidate contains `|E|`, while the degree multiset itself also determines `|E|` because the sum of total directed degrees equals `2|E|`. Thus `|E|` is redundant inside the key.

This redundancy is harmless for non-circularity, but it is unnecessary. For the frozen vNext implementation, the cleaner minimal form is therefore:

`K_C2_vNext,min = B + degree-multiset(V)`

with `B` already containing `|V|`, resources and objective.

This minimal form retains exactly the intended coarse graph constraint without duplicating an invariant.

## 9. Decision

**N-R8-C2 vNext design-level audit = PASS.**

The candidate is:

- state-derived;
- non-circular by construction;
- independent of `R` and `O_T` at construction time;
- capable of producing the required matching classes;
- compatible with a bounded exhaustive probe;
- free of any need to alter N-R1.3.

The canonical implementation candidate is now `K_C2_vNext,min = B + degree-multiset(V)`.

## 10. What remains unproven

This audit does **not** establish:

- `O_T` identifiability;
- non-derivability of `O_T` from the candidate key globally;
- existence of an equal-key / unequal-`O_T` pair in the actual operationalisation.

Those questions belong exclusively to the next bounded probe.

## 11. Execution gate

Before probe execution, freeze the minimal key definition and specify its pure implementation. Then construct the bounded exhaustive fixture using the witness class above and execute only the identifiability probe.

No 5,000-pair corpus, Rust dataset processing, or EXT-1.1 scientific execution is authorised until that probe passes.
