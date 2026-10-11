# TGCV Collective Toy — Review of the Mapping to System-Level T_acc

**Status:** CONCEPTUAL MAPPING REVIEW — PROPOSED / NOT FROZEN  
**Scope:** Synthetic-only Collective Toy, profiles 1 and 2  
**Branch:** `prototype/collective-toy-relation-editor-001-20261011`  
**Scientific execution:** NOT AUTHORIZED  
**Core / Ω-primary status:** UNCHANGED

## 1. Purpose

Determine what the Collective Toy's executable outputs can legitimately represent in relation to TGCV's system-level accessible transformation set, without silently equating an implementation convenience with a TGCV primitive.

This is a representational review only. It does not establish that the toy instantiates TGCV empirically, prove the sufficiency of its state representation, or select a canonical architecture.

## 2. Relevant TGCV architectural distinction

The current candidate Ω-primary definition distinguishes:

- `U_t`: identifiable candidate transformations at time `t`, regardless of current accessibility;
- `≡_T`: a frozen rule for deciding when representations count as the same transformation;
- `R_t`: typed structural relations among transformations;
- `T_acc,t`: transformations accessible under the system's current state and conditions, derived from the structural space and admissibility conditions.

The governing candidate relation is:

`T_acc,t = F(Ω_T,t, S_t, C_t, L_t)`

and a transformation may belong to `U_t` without belonging to `T_acc,t`. See `TGCV_OMEGA_PRIMARY_DEFINITION_AND_ARCHITECTURAL_MEANING_001.md` and `TGCV_OMEGA_T_REPRESENTATION_BOUNDARY_v0.2.md`.

The inherited representation still uses `S` and `T_acc` with only admissible auxiliary mechanisms. A newly introduced relation cannot be silently declared a new primary object or an innocuous auxiliary; see `TGCV_ARCHITECTURAL_ADMISSIBILITY_BOUNDARY_v0.1.md`.

## 3. What the toy currently computes

The toy is a finite directed graph with declared state nodes and transition records. A transition `e` has an ID, source state and target state.

For a scenario `σ`, the engine:
1. starts with the explicitly disabled transition IDs;
2. in profile 2, evaluates each declared guard against that explicit disabled set;
3. adds a guarded transition to the disabled set when its declared prerequisite transition is explicitly disabled;
4. constructs the remaining graph and calculates graph reachability from the initial state;
5. enumerates bounded trajectories, marking truncation when an exploration cap is reached.

Profile 1 does not give relations execution semantics. Profile 2 implements the selected finite guard rule. Guard effects are evaluated against the scenario's explicit disabled set, not recursively against other guards' effects.

The engine reports `enabled_at_initial` as the transitions whose source is the initial node and which remain after scenario/guard filtering. This is explicitly state-local.

## 4. Safe mapping: an operational proxy, not an identity claim

For this toy only, define:

`E_model(x) = { e : source(e) = x }`

and for scenario `σ`, let `D_eff(model, σ)` be the effective disabled-transition set after the selected profile's rules have been applied.

Then define the toy's local enabled-transition set:

`A_toy(x | model, σ) = { e ∈ E_model(x) : id(e) ∉ D_eff(model, σ) }`

This set is a faithful description of what the current engine computes at node `x` for scenario `σ`.

It may be used as an **operational proxy for state-local transition availability inside the synthetic toy**. It must not be labelled simply `T_acc,t` without a separate mapping specification.

## 5. Why this is not yet TGCV's system-level T_acc

The current toy does not independently specify or identify all of the following:

- a candidate transformation universe `U_t` that includes transformations currently inaccessible;
- a transformation-type equivalence rule `≡_T` separate from record IDs;
- an independently evidenced, typed structural relation set `R_t`;
- explicit system-level semantics for `S_t`, `C_t`, and `L_t` and the rule `F` that maps them to accessibility;
- whether the graph's outgoing edges exhaust all transformations that are accessible in the relevant system, rather than only the actions represented in the toy model;
- a longitudinal correspondence rule for transformations across two observation intervals.

Consequently, the toy's graph edge set is model-declared, and its local enabled set is computed relative to that declared graph. It cannot establish that its edge inventory is an independently identified `U_t`, nor that the resulting enabled set equals TGCV's full system-level `T_acc,t`.

## 6. Profile 2 and relations

The profile-2 guard relation has a deliberately narrow semantics: a transition may be disabled when another transition is explicitly disabled in the scenario.

This demonstrates that a declared relation can alter the toy's effective local availability set and resulting graph reachability/trajectories. It does **not** demonstrate that:

- all structural relations have this form;
- the relation vocabulary is canonical;
- the guard relation is an independently evolving `R_t` in the Ω-primary sense;
- a change in local availability proves a change in the primary transformation universe;
- the relational profile is scientifically superior to profile 1 or to the inherited architecture.

The finite-graph result is a software behavior under an explicit rule, not a scientific effect estimate.

## 7. Interpretation of Reach and trajectories

Within the toy, reachability is graph reachability from the declared initial node after filtering disabled transitions. Trajectories are finite walks enumerated under explicit depth and trajectory caps.

These are well-defined toy outputs. They may serve as an illustrative analogue of derived reachability/path concepts, but they are not automatically equal to TGCV's system-level `Reach`, `ΔReach`, or trajectory objects. In particular, no longitudinal comparison between `t` and `t+1` is implemented by merely comparing two scenarios on one static graph.

A scenario contrast can establish that the configured toy rule changes the computed graph outputs. It cannot, by itself, establish a real system's transformation-space dynamics.

## 8. Recommendation

**Retain the mapping as a proxy and keep the boundary explicit.**

1. Keep the engine's output field `enabled_at_initial` state-local; do not rename it `T_acc`.
2. In user-facing UI and export, describe it as “transiciones habilitadas desde el estado inicial” or “local enabled transitions”.
3. Label profile 2 as an experimental guard semantics, not a general implementation of `R_t`.
4. If the toy is later extended to model `U_t`, `≡_T`, `R_t`, `S_t`, `C_t`, and `L_t` explicitly, introduce a versioned mapping specification and tests for each mapping; do not infer these objects from current output names.
5. Keep any architectural transition behind the existing governance/admissibility gate. Do not change Core, Evidence→Claim Matrix, RMA, or Ω-primary status as a consequence of these software tests.

## 9. Next contract work

Before freezing the toy contract:

- document the field-by-field distinction between model states, transition records, scenario interventions, guard relations, local enabled transitions, reachable states, and bounded trajectories;
- state whether the MVP intentionally remains a graph demonstration or is meant to become an explicit operationalization of `T_acc`;
- if the latter is chosen, specify the mapping from primitive inputs to `S,C,L` and from candidate transformations to `U_t` before implementation;
- align the contract's CI record with the latest successful runs and retain the explicit caveat that finite tests do not prove all-input correctness.

**Decision status:** mapping proposed; not frozen. The toy remains synthetic-only. No scientific execution is authorized.
