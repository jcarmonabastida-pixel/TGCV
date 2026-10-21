# TGCV-first demonstration case 001 — illustrative transformation-space change

**Status:** proposed functional acceptance case; not implemented or scientifically validated.
**Purpose:** give the functional architecture review one small, explicit example that distinguishes TGCV transformation-space dynamics from ordinary state-transition simulation.

## 1. Scope and interpretation

This is a deliberately artificial, domain-neutral example. Its rules are stipulated for demonstrating representation and derivation, not inferred from empirical data. It makes no claim about real systems or value causality.

The demonstration is successful only if a user can inspect:
1. a declared accessible-transformation set before an interaction;
2. a declared interaction/mechanism and the rule it applies;
3. the accessible-transformation set after the interaction;
4. the resulting change in reachable transformation sequences;
5. the inputs/rules that justify those results.

## 2. Minimal declared model

Use three transformations:

- `a`: prepare
- `b`: inspect
- `c`: repair

These labels are placeholders. They represent transformations, not system states.

### Before the interaction

Declared accessible transformations:

`T_acc_before = {a, b}`

Declared compatibility relation between consecutive transformations:

`R_before = {(a, b)}`

For this example, a trajectory is a non-empty sequence of accessible transformations in which every adjacent pair is permitted by the declared compatibility relation. This is a demonstration-specific rule, not a universal TGCV definition.

Under that rule, the two-step sequence `[a, b]` is reachable. `c` cannot occur because it is not in the declared accessible set.

### Interaction/mechanism

Declare an interaction `m` with this explicit model rule:

> Applying `m` adds transformation `c` to the accessible set and adds the compatibility relation `(b, c)`.

This is stipulated input, not a discovered mechanism. The model must display the rule itself; it must not infer it from the name or description of `m`.

### After the interaction

The declared rule yields:

`T_acc_after = {a, b, c}`

`R_after = {(a, b), (b, c)}`

Therefore:

`ΔT_acc = T_acc_after − T_acc_before = {c}`

The two-step sequence `[a, b]` remains reachable, and `[a, b, c]` becomes reachable under the stipulated trajectory rule. The display should distinguish the newly available transformation `c` and newly reachable sequence `[a, b, c]` from the sequence that was already reachable.

No state-machine execution is required to establish this representational result.

## 3. Required interface behavior

- Render transformations as transformation objects, not unlabeled state nodes.
- Show `T_acc_before`, the interaction rule, `T_acc_after`, and `ΔT_acc` side by side or in a clear before/after view.
- Show `R_before` and `R_after` as typed compatibility relations.
- Show at least one previously reachable sequence and one newly reachable sequence.
- Selecting `m` reveals its stipulated rule and provenance (“user-declared demonstration rule”).
- Clearly label all values as declared or derived. `T_acc_after`, `ΔT_acc`, and the new reachable sequence may be marked derived only if the interface actually applies the displayed rule.
- If the user edits the initial set, interaction rule, or relation set, mark the derived sets and sequences stale until recomputed.
- Do not calculate a value score or claim value creation in this case. The case demonstrates only a change in accessibility and reachability.

## 4. Acceptance checks (grouped)

1. **Before/after correctness:** the UI reports exactly the sets and relations stated above.
2. **Derivation transparency:** it identifies `c` as the sole member of `ΔT_acc` and points to the declared rule that introduced it.
3. **Trajectory distinction:** `[a, b]` is shown as reachable before and after; `[a, b, c]` is shown as newly reachable after applying `m`; no sequence containing `c` is presented as reachable before.
4. **Semantic typing:** `a`, `b`, and `c` are identified as transformations; `m` as an interaction/mechanism; `R` as a compatibility relation. None is silently treated as a system state or execution guard.
5. **Edit/provenance safety:** editing the rule invalidates derived results; export/import preserves the declarations and the distinction between declared and derived data.
6. **No overclaim:** the UI states that the example is artificial and provides no empirical validation of TGCV.

Do not create one unit test per bullet mechanically. Prefer one end-to-end acceptance test for the full before/after case, plus adversarial tests for stale results, invalid relation endpoints, and mislabeling a transformation as a system state.

## 5. What this case does not specify

This case does not settle:
- a universal ontology or final schema for all TGCV models;
- empirical criteria for determining whether a transformation is truly accessible;
- whether `R` should be a general relation set, a typed family of relations, or multiple relation layers;
- the role of conditions in system execution;
- observer/context value evaluation;
- how accessibility changes are inferred from real-world evidence.

Those are separate design or research questions and must not be silently answered by this toy example.
