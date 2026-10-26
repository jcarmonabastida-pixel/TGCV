# Graph-to-TGCV Transformation-Space Representation — Contract Review 001

**Status:** PROPOSED DESIGN REVIEW — NOT FROZEN  
**Branch:** `proposal/graph-tgcv-representation-contract-001`  
**Scope:** Architectural precondition for any integration of the trajectory selector into the interactive demonstrator.  
**Execution status:** Documentation-only review. No scientific execution, no engine/UI changes, no TGCV Core change, and no claim-status change are authorized by this artifact.

## 1. Decision to be resolved

The current collective-toy demonstrator represents a finite directed graph, enumerates state paths through eligible transitions, and records paths/results. Before connecting the heuristic trajectory selector or its recommendation audit to the UI, determine whether the graph and its execution trace instantiate TGCV's distinct semantic objects—or only a conventional state-transition model.

**Provisional conclusion:** the current graph is a useful operational substrate, but its present schema does not by itself establish a representation of the accessible transformation space (T_{acc}). Selector integration is therefore gated on a representation contract and a gap assessment.

## 2. Historical reconstruction

The following existing artifacts were inspected and reused; this review does not replace them:

1. `03_EXPERIMENTS/TR-131/execution/TR131_TRANSFORMATION_SPACE_DYNAMICS_FORMAL_SPEC_001.md` — defines (S_t), (C_t), (T_{acc,t}=A(S_t,C_t,R_t)), (T_{real,t}), trajectories, and the separation of accessibility, realization, trajectory, outcome and value. It explicitly requires transformation identity, admissibility/preconditions, state/context representation, an accessibility mapping, realization events, successor-state mapping, trajectory representation and a comparison operator for accessibility-space change.
2. `00_GOVERNANCE/SIP/TGCV_CROSS_DOMAIN_END_TO_END_ACCESSIBILITY_OUTCOME_VALUE_MAP_001.md` — states that domain-specific constructs must not be relabelled as TGCV constructs merely because they occupy similar positions in a sequence; the end-to-end chain is only partially evidenced and the downstream value linkage remains open.
3. `prototypes/collective_toy/collective_toy_engine_001.py` — the engine's module docstring explicitly says it does not implement TGCV (T_{acc}), value, causality or empirical inference. Its `Transition` record has `id`, `source`, `target`, and optional `condition`; these fields establish graph structure, not by themselves the domain semantics of a transformation.
4. `prototypes/collective_toy/test_collective_toy_engine_001.py` — current tests establish finite reachability/path enumeration and ensure transitions with unevaluated conditions are not explored. Those are valid engine contracts, but they do not establish an independently specified (T_{acc}).

Historical classification:
- **DEFINED:** TR-131 semantic distinction between accessible and realized transformations.
- **DEFINED / ANALYSIS:** independent cross-domain map and its limits.
- **IMPLEMENTED:** synthetic state/transition graph, bounded path exploration and temporal prerequisite handling.
- **TESTED at software-contract level:** deterministic graph traversal, reachability and rejection/exclusion of unevaluated conditional transitions.
- **OPEN:** explicit mapping from the graph model to (T_{acc}), transformation semantics, accessibility mapping and trace-level realization semantics.
- **NOT inferred:** no scientific, causal, predictive, value or general-validity conclusion follows from the existing software tests.

## 3. Semantic contract required before selector integration

### C1 — State is not transformation

A state (S_t) describes the system at a point in time. A graph node may encode a state, but a node identifier alone does not define the state's relevant variables, context or constraints. State/context fields must be explicit or refer to a documented domain schema.

### C2 — Edge identity is not sufficient transformation semantics

A graph edge must retain a stable identifier and source/target references. To count as a TGCV transformation, it must additionally have a declared transformation identity/meaning and a specified state-change or successor mapping. An edge label or ID must not be silently treated as proof of that meaning.

A graph transition and a transformation may be linked one-to-one, one-to-many, or through a domain-specific mapping, but that mapping must be explicit. The implementation must not assume one-to-one equivalence without evidence.

### C3 — Accessibility is specified independently of paths selected or realized

The model must define an accessibility mapping of the form (T_{acc,t}=A(S_t,C_t,R_t)), where the candidate transformation universe, context, and admissibility rules are declared. It must not define (T_{acc}) from the trajectories returned by exploration, from the selector's ranking, from an executed trace, or from outcomes/value.

A list of edges traversable in the current graph is only a graph-reachability result unless the mapping from those edges to the candidate transformation universe and the accessibility predicate is specified.

### C4 — Admissibility and evaluator capability are distinct

Known restrictions, temporal prerequisites and evaluated conditions may constrain whether a candidate transformation is admissible in a particular state/context. An unevaluated condition is not equivalent to a satisfied condition and must not silently become unconditional. The condition evaluator is one mechanism for evaluating specified predicates; it is not, by itself, the complete definition of (T_{acc}).

### C5 — Realization trace records transformations, not only graph traversal

A realized event must be reconstructable as at least:
- event/step identity and order;
- transformation identity;
- source state and resulting state;
- relevant context and evaluated admissibility evidence;
- evaluator/contract version and provenance sufficient to reproduce the decision.

A state sequence alone is insufficient to identify which transformation was realized when distinct transformations share endpoints or when a transition ID lacks semantic grounding.

### C6 — Trajectory preserves the alternating semantic sequence

The TGCV trajectory representation should distinguish states from realized transformations, e.g. (H_n=(S_0,T_{real,0},S_1,ldots,T_{real,n-1},S_n)). The current graph path format that interleaves a transition ID and the next state is structurally compatible with this idea, but compatibility is not semantic equivalence until C2 and C5 are satisfied.

### C7 — Transformation-space change is a separate comparison

If the demonstrator later compares (T_{acc,t}) with (T_{acc,t+1}), the comparison must operate on independently specified transformation-space representations and distinguish additions, removals, substitutions or structural changes where applicable. A change in reachable nodes/paths is not automatically (Delta T_{acc}).

No assumption is made that every realized transformation changes (T_{acc}), or that (Delta T_{acc}) entails a value change.

### C8 — Selector remains downstream and non-executing

The heuristic selector may rank only trajectories generated by a validated exploration contract. It must not define accessibility, add transformations, repair missing semantics, or execute the selected trajectory. A ranking remains a heuristic ranking, not a prediction or proof of value.

## 4. Initial gap assessment against the current synthetic engine

| Requirement | Current evidence | Assessment |
|---|---|---|
| Explicit state IDs and directed graph endpoints | Model states, transition source/target | Present at graph-structure level |
| Stable edge/transition ID | Transition `id` | Present; does not establish transformation semantics |
| Context (C_t) and declared accessibility mapping (A(S,C,R)) | Not part of the core model contract shown by the engine | Gap to assess |
| Candidate transformation universe distinct from explored paths | Engine explores graph transitions | Not established |
| Independently specified admissibility predicate | Disabled transitions, temporal prerequisites, optional condition metadata | Partial, scenario-specific; not a complete (T_{acc}) definition |
| Unevaluated conditions remain non-executable | Engine tests exclude conditional transitions without evaluator support | Present as a safety boundary |
| Transformation identity/meaning and successor mapping | Only graph transition ID and source/target | Not established |
| Realization trace identifies (T_{real}) separately from edge traversal | Current trajectory path records transition IDs and states | Structurally traceable, semantic mapping open |
| (Delta T_{acc}) comparison | Reachability/path deltas are computed | Not equivalent to (Delta T_{acc}); no such claim permitted |
| Outcome/value separation | UI displays results and perceived value as separate application fields | Presentation separation is useful; does not prove a TGCV value pathway |

This table is a source-level design assessment, not a runtime test result.

## 5. Minimal safe adaptation path

1. **Contract review:** resolve C1–C8 and document the domain meaning of transformations in the synthetic toy.
2. **Schema/gap decision:** decide whether to extend the existing graph schema with transformation/context/accessibility fields, add a separate TGCV semantic layer mapped onto the graph, or retain the graph explicitly as a non-TGCV substrate. Do not choose by convenience alone.
3. **Focused contract tests:** test semantic mapping, accessibility independence from selector/trace/outcome, rejection of missing or ambiguous transformation mappings, and preservation of unevaluated conditions. These are software contract tests, not scientific experiments.
4. **Trace adaptation:** only after the schema decision, ensure realized steps identify (T_{real}) and preserve source/result states and admissibility evidence.
5. **Selector and audit integration:** only then wire the selector into the demonstrator, recording the recommendation before execution and keeping selection separate from execution.
6. **Promotion:** review the branch diff and CI, then decide explicitly whether to open/revise a draft PR. Do not modify `main` or merge PR #99 as part of this review.

## 6. Acceptance gate

Do not integrate the selector into the interactive execution flow until all are true:

- [ ] C1–C8 have a documented resolution or explicit non-goal.
- [ ] The model states whether it represents (T_{acc}), a graph approximation, or only state-transition reachability.
- [ ] Transformation identity and semantics are not inferred from edge IDs alone.
- [ ] Accessibility is defined independently from exploration, ranking, realized trace, outcome and value.
- [ ] Trace semantics distinguish the realized transformation from the resulting state.
- [ ] Tests cover ambiguous/missing mappings and unevaluated conditions.
- [ ] UI wording does not overstate the model's TGCV status.
- [ ] No Core, RMA, Evidence→Claim Matrix, scientific execution or claim-status change is implied.

## 7. Governance boundary

This proposal is an implementation-design review derived from existing formal and analytical artifacts. It does not freeze a new TGCV ontology, amend TR-131, change the Core, or authorize scientific execution. If implementation would require changing a frozen semantic contract, stop and resolve that discrepancy through the appropriate governance decision before changing code.

**Disposition:** keep the selector disconnected from the demo execution flow until this representation gate is resolved.
