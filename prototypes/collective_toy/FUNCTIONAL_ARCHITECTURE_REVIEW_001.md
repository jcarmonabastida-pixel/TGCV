# Juguete Colectivo — functional architecture review 001

**Status:** design proposal for review; no implementation authorized by this document.
**Scope:** clarify what the demonstrator represents before deciding how conditions should be modeled.
**Scientific boundary:** this document does not change the TGCV Core, establish a causal relationship, or constitute scientific validation.

## 1. Decision to resolve

The demonstrator is intended to make TGCV's proposed object inspectable: interactions may modify the transformations accessible to a system, and those changes may relate to later trajectories. It must not accidentally present ordinary state-transition simulation as if it were the TGCV object itself.

The current prototype includes state-like nodes, directed transitions, scenarios, temporal prerequisites, trajectory exploration/execution, and value-oriented comparisons. The existing graph therefore appears to combine concepts that need an explicit semantic distinction. A graph edge being executable under a condition is not, by itself, evidence that the set of accessible transformations has changed.

**Recommendation:** use two explicitly distinguished layers, with the TGCV transformation-space layer primary and an optional domain/system execution layer secondary.

## 2. Proposed layers

### Layer A — TGCV transformation-space dynamics (primary)

This layer should help a user inspect and compare:

- **System/domain representation (S):** the declared subject and relevant representation, without assuming that every node is a system state.
- **Accessible transformations (T_acc):** which transformations are available in a specified representation/context.
- **Relations and mechanisms (R):** declared dependencies or interactions that relate transformations and may explain changes in accessibility.
- **Change in accessibility (ΔT_acc):** an explicit before/after or scenario comparison of the accessible transformation set.
- **Reachability and trajectories:** which transformation sequences are reachable under the declared model, distinguished from sequences actually executed in a simulation.
- **Provenance and uncertainty:** the assumptions, input data, scenario, and unresolved elements used to derive a displayed result.

The central question in this layer is not merely “which state comes next?” It is “which transformations are available, how does that availability change, and what consequences for reachability or trajectories follow under the declared representation?”

The implementation must not claim that a listed transformation is empirically accessible merely because it was drawn as an edge. Its status and basis must be explicit (for example: declared, derived by a stated rule, or observed in data).

### Layer B — optional system/domain execution (secondary)

This layer may simulate an application domain when doing so helps explain a concrete example:

- states or configurations of the modeled system;
- executable transitions between those states;
- explicit initial conditions and scenario facts;
- guards/conditions, temporal prerequisites, disabled transitions;
- step-by-step execution trace and resulting system state.

Conditions naturally belong here when they mean “this system transition may execute only when these facts hold.” A condition evaluator can improve the fidelity of this layer, but it does not by itself implement or demonstrate TGCV transformation-space dynamics.

This layer must be labeled as a domain simulation, not as the definition of TGCV. Its execution trace must not be presented as equivalent to a TGCV transformation-space trajectory unless the mapping between the two is explicitly defined.

## 3. Semantic separation rules

1. **Do not conflate nodes.** A node may denote a domain/system state, a transformation, a mechanism, or another model element. The UI and schema must identify which kind it is; visual shape alone is insufficient.
2. **Do not conflate edges.** A system transition, a transformation available to the system, and a relation that changes transformation accessibility are different semantic roles. If the interface uses a shared graph canvas, edge/node types and their legends must make those roles explicit.
3. **Do not equate a guard with accessibility change.** A guard controls execution in Layer B. It affects T_acc in Layer A only if an explicit, documented modeling rule says how the guard changes the set of accessible transformations.
4. **Separate possibility from execution.** A reachable candidate path, a path ruled out by model constraints, and an executed trace are distinct results. The UI must name them accordingly.
5. **Separate structural availability from contextual enablement.** If a transformation is structurally in the model but enabled only in a particular scenario, show the distinction between its declared status and its context-dependent applicability.
6. **No silent inference.** The system must not infer a TGCV mechanism, accessibility change, or condition truth from node/edge labels or free-form text without an explicit validated rule.
7. **Preserve traceability.** Results depend on a model version, scenario/context, and applicable rules. Any relevant edit invalidates stale derived results or marks them as belonging to the previous input version.
8. **No scientific overclaim.** Demonstrator output is a consequence of the supplied model and rules; it is not by itself evidence for TGCV's empirical validity or for value causality.

## 4. What this means for condition modeling

The question “should conditions be modeled?” has no single answer until their semantic role is declared.

- **Yes, in Layer B**, if the demonstrator is meant to execute domain transitions whose applicability depends on explicit facts.
- **Possibly in Layer A**, but only when a condition represents a declared constraint on transformation accessibility and the model specifies how it determines membership in T_acc. Such a condition is not merely an execution guard; it participates in a documented accessibility rule.
- **No as a substitute for Layer A.** Adding a typed evaluator (TRUE/FALSE/UNKNOWN) to state-transition edges would make execution more coherent, but would not by itself show how T_acc changes.

Therefore, pause implementation of the current condition-evaluator proposal and schema collective-toy-input-003 until the layer boundary and graph semantics are agreed. Do not discard the earlier proposal: retain it as a possible Layer B design input, subject to review.

## 5. Review questions before implementation

These questions should be resolved in the functional contract, not guessed in code:

1. What is the primary visual object: a graph of system states, a graph of transformations, or a typed representation that can show both without conflation?
2. How is T_acc represented: as transformation objects, as a set/list associated with a system/domain representation, or both?
3. What model element or rule records an interaction/mechanism that changes T_acc?
4. How are T_acc before and after an interaction compared, and how is ΔT_acc derived or supplied?
5. Which trajectories are TGCV-level transformation trajectories, and which are optional state-execution traces?
6. What is the minimum example that demonstrates a genuine change in transformation accessibility rather than only a state transition?
7. Does the existing value dashboard depend on system execution paths, TGCV-level trajectories, or a separate observer/context evaluation? Its meaning must be made explicit before retaining it as a TGCV result.
8. Which Layer B features are necessary for the first useful demonstration, and which can remain optional?

## 6. Recommended acceptance criteria for the revised functional contract

The revised contract should pass grouped review against these criteria:

- **Object clarity:** every displayed node, edge, set, and trajectory has an explicit semantic type.
- **TGCV-first demonstration:** a user can see at least one declared interaction/mechanism, the transformation accessibility before and after it, and the resulting difference in reachable transformation trajectories.
- **Derivation transparency:** each computed accessibility/reachability result identifies the rule and inputs used; supplied facts are not presented as derived results.
- **Possibility/execution distinction:** possible, blocked, and executed sequences are separately represented.
- **Optional simulation boundary:** conditions and state execution can be included without being confused with TGCV's primary object.
- **Reproducibility:** model, scenario, rule versions, and result provenance survive export/import without silent reinterpretation.
- **Stale-result safety:** edits to relevant inputs mark derived results stale until recomputed.
- **Scope honesty:** the interface explains that demonstration of a formal model is not empirical validation of TGCV.

Do not turn these grouped criteria into one test per sentence mechanically. Use a small number of end-to-end acceptance cases plus adversarial tests for semantic conflation, stale results, import/export, and misleading presentation.

## 7. Relationship to the condition-evaluator proposal

CONDITION_EVALUATOR_CONTRACT_PROPOSAL_001.md and CONDITION_EVALUATOR_IMPLEMENTATION_AUDIT_001.md are preliminary design/audit artifacts. Their proposed typed predicates and explicit scenario context may be useful for Layer B, but their proposed v003 migration is **not approved for implementation by this review**. Reassess them after the functional contract establishes the primary TGCV object and the optional simulation boundary.

## 8. Change boundary

This proposal changes documentation on a design branch only. It does not change main, executable code, schema validation, model artifacts, CI, or scientific execution. No implementation should start until the revised functional contract is reviewed and explicitly accepted.
