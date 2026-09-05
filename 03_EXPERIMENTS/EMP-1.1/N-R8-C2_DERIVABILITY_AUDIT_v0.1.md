# N-R8-C2 — Derivability Audit v0.1

## 1. Purpose

This document records the post-probe audit following the bounded N-R8-C2 identifiability probe.

The probe examined 4,160 bounded fixed-component directed-edge-subset states and 8,484 equal-key collision pairs. It found no pair with equal `K_C2` and unequal full `O_T`.

This audit determines whether that absence is plausibly explained by insufficient fixture diversity or by derivability of the current `O_T` representation from the current matching key.

## 2. Frozen artefacts audited

- `03_EXPERIMENTS/EMP-1.1/src/branch_n_r8_operationalisation_v01.py`
- `03_EXPERIMENTS/EMP-1.1/src/branch_n_r8b4_corpus_v01.py`
- `03_EXPERIMENTS/EMP-1.1/src/branch_n_r_v02.py`

The authoritative full `R` vector is the 58-dimensional N-R1.3 v0.2 encoding implemented by `encode_r`.

## 3. Current C2 matching key

The current `_c_match_key(state)` is:

`B || R1 || R2 || R3 || |T_acc| || n_families || |V| || resources || objective`

where the first 42 dimensions of the full R vector are `R1 + R2 + R3`.

## 4. Derivability audit

### 4.1 B

`B` contains:

- `|V|`;
- the three resource values;
- the one-hot objective.

These values are therefore already fixed explicitly by `K_C2`.

### 4.2 R1

`R1` is explicitly included in `K_C2`.

### 4.3 R2

`R2` is explicitly included in `K_C2`.

### 4.4 R3

`R3` is explicitly included in `K_C2`.

### 4.5 `|T_acc|`

`|T_acc|` is explicitly included in `K_C2`.

Moreover, under the authoritative Branch N semantics it is already the sum of the six R2 family cardinalities, so this coordinate is redundant but harmless.

### 4.6 Number of active families

The active-family count is the sum of the six R1 indicators. It is therefore derivable from R1.

### 4.7 R4 coordinates

The 16 R4 coordinates of the authoritative 58-vector are audited as follows.

1. `n_delta_components_add` = R2 count for `ADD_COMPONENT`.
2. `n_delta_components_remove` = R2 count for `REMOVE_COMPONENT`.
3. `n_delta_edges_add` = R2 count for `ADD_EDGE`.
4. `n_delta_edges_remove` = R2 count for `REMOVE_EDGE`.
5. `n_delta_edges_rewire` = R2 count for `REWIRE_EDGE`.
6. `n_delta_resources_up` = count of `MODIFY_RESOURCE` transformations with `d=+1`; this is derivable from the three current resource values and the R2 cardinality/Branch N transformation semantics.
7. `n_delta_resources_down` = analogous derivation for `d=-1`.
8. `n_noop` = 0 under the authoritative deterministic transformation semantics: every valid transformation changes at least one state coordinate.
9. `len(set(next_component_counts))` is determined by the presence/counts of ADD_COMPONENT and REMOVE_COMPONENT together with `|V|`.
10. `len(set(next_edge_counts))` is determined by ADD_EDGE, REMOVE_EDGE and REWIRE_EDGE effects, with the current edge count recoverable from R3 and `|V|`.
11. `len(set(next_resource_vectors))` is determined by the resource vector in B and the valid MODIFY_RESOURCE moves.
12. `len(set(next_states))` is determined by the deterministic one-step transformation semantics because distinct valid transformation instances produce distinct successors in this representation.
13. `max(next_component_counts)` is determined by `|V|` and whether ADD_COMPONENT is available.
14. `min(next_component_counts)` is determined by `|V|` and whether REMOVE_COMPONENT is available.
15. `max(next_edge_counts)` is determined by the current edge count and the available edge-changing families.
16. `min(next_edge_counts)` is determined analogously.

The current edge count is itself recoverable from R3. For example, the sum over components of the R3 `ADD_EDGE` incidence coordinate equals twice the number of currently absent directed edges. Given `|V|`, the total possible directed edges is `|V|(|V|-1)`, so the current edge count is determined.

## 5. Audit conclusion

The current C2 matching key contains the complete information required to reconstruct the current 58-dimensional `O_T`/full-R representation under the frozen Branch N semantics.

Therefore the bounded probe's failure is not adequately interpreted as merely a lack of fixture diversity. The current formulation of C2 is structurally incapable of producing the intended equal-key/unequal-O_T distinction, because `O_T` is derivable from the information already fixed by `K_C2`.

Decision:

`N-R8-C2 CURRENT FORMULATION = DERIVED / BLOCKED`

This is a methodological block, not a refutation of the broader N-R8 research question.

## 6. Consequences

1. Do not generate the planned 5,000-pair C2 corpus under the current key.
2. Do not expand the bounded fixture family merely to search for a counterexample to a derivability relation already implied by the representation.
3. Do not modify N-R1.3 retrospectively to manufacture non-derivability.
4. Preserve the original bounded-probe result as an auditable negative result.
5. Redesign the C2 operationalisation so that the candidate matching representation and the target observable contain a genuinely independent structural distinction, if such a distinction can be justified independently of the result.

## 7. Scientific status

- Scientific execution: `NOT_PERFORMED`
- Corpus generation: `NOT_PERFORMED`
- N-R7: `INTACT`
- Dataset processing: `NOT_PERFORMED`
- Rust dataset gate: remains blocked pending resolution of the relevant identifiability methodology.

## 8. Next gate

The next scientific task is **N-R8-C2 vNext design**, not corpus generation.

The redesign must specify, before any new search:

- the exact information retained by the new matching key;
- the exact target observable;
- the independent degree of freedom intended to separate them;
- why that degree of freedom is not derivable from the matching key;
- a bounded fixture family capable of varying that degree of freedom;
- a fail-closed decision rule.

No new empirical execution should be treated as scientific evidence until that specification is frozen.
