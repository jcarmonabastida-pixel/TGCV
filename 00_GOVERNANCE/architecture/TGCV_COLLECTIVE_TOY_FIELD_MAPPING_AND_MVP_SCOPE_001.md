# TGCV Collective Toy — Field Mapping and MVP Scope

**Status:** PROPOSED — NOT FROZEN  
**Applies to:** Synthetic Collective Toy input schema `collective-toy-input-001`, profiles 1 and 2  
**Scientific execution:** NOT AUTHORIZED  
**Architecture/Core change:** NONE

## 1. Decision to preserve scope

For the current MVP, retain the Collective Toy as a **finite-graph demonstration with explicitly state-local execution outputs**. Do not yet claim it is an operationalization of system-level TGCV `T_acc`.

This is the least-assumptive scope because the present input schema does not separately identify a complete candidate-transformation universe, transformation equivalence, or an independently justified structural relation system. Changing that would be a new modeling task and would require its own contract and governance review.

This recommendation is proposed, not frozen. It does not prevent a later versioned extension that explicitly operationalizes selected TGCV objects.

## 2. Field-by-field mapping

| Current input/output field | Current executable meaning | Possible TGCV relation | Boundary / requirement |
|---|---|---|---|
| `states` | Finite list of symbolic nodes/configurations admitted by the toy model | A finite model of selected states in `S` | Not proof that the list exhausts the real system's state space |
| `initial_state` | Node from which reachability and trajectory exploration start | Initial configuration `s_0in S` | A model initialization, not a general TGCV primitive by itself |
| `transitions[].id` | Stable identifier used for validation, disablement, sorting and output | Identifier for a modeled candidate transformation | IDs are not the transformation-equivalence relation `≡_T`; duplicate/alternative representations need separate semantics |
| `transitions[].source/target` | Directed edge from one declared state to another | Deterministic applicability/effect in this graph special case | The current edge inventory may omit possible but inaccessible transformations and cannot establish completeness of `U_t` |
| `relations` in profile 1 | Descriptive metadata; no effect on enablement | At most a record of annotations supplied to the toy | Not operational `R_t`; must not be described as causally active |
| Profile-2 relation guard | Blocks a named transition if its prerequisite ID is explicitly present in the scenario's disabled list | A toy-specific operational relation among transition records | Not temporal precedence, not recursive propagation, and not a canonical definition of `R_t` |
| `rule_profile` | Selects a versioned finite execution rule | Engineering proxy for part of the mechanism/rule layer `L` | Not the whole of TGCV's `L`; the selected semantics are local to this implementation |
| `scenarios[].disabled_transitions` | Explicit intervention on transition IDs; profile-2 guards derive additional disablements from this explicit set | A controlled model condition/intervention, potentially analogous to part of `C` | Does not yet provide a full system-level definition of `C`; derived guard disablements are not recursively treated as explicit inputs |
| `exploration.max_depth` | Bound on enumerated trajectory edge count | Computational observation/exploration bound | Not a system property or a TGCV accessibility condition |
| `exploration.max_trajectories` | Output cap for trajectory enumeration | Computational observation/exploration bound | Truncation must remain visible; omitted paths are unknown, not absent |
| `enabled_at_initial` | Modeled transitions sourced at the initial node that remain after scenario/profile filtering | State-local set `T_enabled(s_0mid M,q)` | Do not rename it `T_acc`; it is conditional on the declared graph and scenario |
| `reachable_states` | Declared nodes reachable from the initial node in the filtered graph | Toy graph reachability; illustrative analogue of derived Reach concepts | Not automatically system-level `Reach` or `ΔReach`; no temporal comparison is implied |
| `trajectories` | Finite paths enumerated under the stated traversal and bounds | Derived paths in the toy | Not automatically TGCV system trajectories; bounds and truncation qualify the result |
| Input/output hashes | SHA-256 of the documented canonical representation | Reproducibility/audit evidence | Hash equality proves byte-representation equality, not semantic or scientific equivalence |
| Scenario comparison | Difference between output sets for named scenarios on the same model | A controlled contrast of toy outputs | Not a causal estimate and not evidence of value construction |

## 3. The system-level distinction

The current working TGCV formulation includes:

`T_acc = F(S,C,L)`

and treats `(S,T_acc)` as the working Core candidate, with `C/L/Pτ` auxiliary and Reach/trajectories derived. The Ω-primary candidate additionally distinguishes a candidate transformation universe `U_t`, a transformation-equivalence rule `≡_T`, and typed relations `R_t`; accessibility is not identical to candidacy.

The current toy has a finite set of model-declared edges and calculates a state-local enabled set. It does not independently identify a complete `U_t`, define `≡_T`, or establish the system-level mapping `F`. Thus:

- `T_enabled(s | M,q)` is a valid toy output;
- it can be studied as a proxy for local availability under an explicit model;
- equality with system-level `T_acc` is **not established**;
- changes in toy reachability/trajectories are changes in the configured toy, not proof of real-system transformation-space dynamics.

## 4. Consequence for product/UI language

Until a separate mapping is approved, use these labels in UI, reports, and exports:

- “Modeled transitions”
- “Transitions enabled from the initial state”
- “Reachable states in the modeled graph”
- “Enumerated trajectories (bounded)”
- “Relation guard applied / blocked”
- “Scenario output difference”

Avoid unqualified labels such as “TGCV (T_{acc})”, “Ω-primary relation system”, “causal effect”, or “value created”.

## 5. If a future version is to operationalize (T_{acc})

A new, versioned design must specify before implementation:

1. the intended system boundary and state representation;
2. the candidate transformation universe, including candidates that are currently inaccessible;
3. the rule for transformation identity/equivalence (`≡_T`);
4. the explicit semantics and evidence status of `C`, `L`, and any operative relations;
5. the function that maps these inputs to system-level accessibility;
6. how observations at different times correspond, so `ΔReach` or transformation-space changes can be meaningfully defined;
7. validation fixtures that distinguish candidate-but-inaccessible transformations from nonexistent/unmodeled transformations;
8. separate governance approval before treating the extension as a TGCV architectural change.

Do not infer these primitives from existing graph field names or add them implicitly in the UI.

## 6. Recommended next implementation gate

1. Complete the current CI round after the documentation update.
2. Add a small UI/export terminology check ensuring the current output is described as state-local.
3. Verify that the editor preserves the selected rule profile and does not silently turn profile-1 descriptive metadata into operative guards.
4. Freeze neither this mapping nor the wider mathematical contract until schema and acceptance coverage are reconciled.

**Decision status:** retain graph-demonstration scope for the current MVP — proposed, not frozen. No change to TGCV Core, Evidence→Claim Matrix, RMA, or Ω-primary status. Scientific execution remains unauthorized.
