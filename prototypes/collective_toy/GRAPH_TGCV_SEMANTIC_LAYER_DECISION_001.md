# Graph ↔ TGCV Semantic Layer — Design Decision Proposal 001

**Status:** PROPOSED — requires review; not frozen  
**Branch:** `proposal/graph-tgcv-representation-contract-001`  
**Decision scope:** choose the least disruptive representation approach before selector/UI integration.  
**Execution boundary:** design-only. No scientific execution, no motor/UI changes, no Core/RMA/Evidence→Claim Matrix changes, and no claim-status changes.

## 1. Decision question

How should the existing synthetic temporal-prerequisite graph be related to TGCV's distinct semantic objects (S_t), (C_t), (T_{acc,t}), (T_{real,t}) and (H_t), without silently treating ordinary graph reachability as transformation-space accessibility?

## 2. Existing implementation constraints

The current engine has explicit state IDs and transition IDs with source/target states, optional condition text, scenario-level disabled transitions and temporal prerequisite relations. It enumerates graph trajectories. The selector consumes these enumerated trajectories and ranks them heuristically; it explicitly does not enumerate paths, evaluate conditions, execute paths, or predict outcomes.

The engine's own module contract states that it does not implement (T_{acc}). TR-131 requires an independently specified accessibility mapping and distinguishes accessibility, realization, trajectory, outcome and value. Thus neither the graph nor the selector may be relabelled as a complete TGCV representation without an explicit semantic mapping.

## 3. Options considered

| Option | Advantages | Risks / cost | Disposition |
|---|---|---|---|
| A. Treat each graph edge as a TGCV transformation by default | Lowest code cost | Assumes edge identity and semantics are equivalent; cannot represent ambiguous/multiple mappings; accessibility becomes graph reachability by implication | Reject |
| B. Replace the graph engine with a TGCV-specific model | Direct representation possible | High regression surface; risks changing the accepted synthetic engine and UI before a gap is proven; couples exploration and semantic interpretation | Defer |
| C. Add a separate, versioned semantic layer that explicitly maps the existing graph to TGCV objects | Preserves current graph engine and UI; makes mapping inspectable and testable; allows explicit “not specified” status | Requires a new contract and mapping fixture; does not itself prove that the domain semantics are scientifically adequate | **Recommend for prototype evaluation** |
| D. Keep the graph explicitly as a conventional graph and do not claim TGCV representation | Safest if no defensible semantic mapping can be specified | Selector remains a generic graph-path heuristic and cannot be presented as operating on (T_{acc}) | Fallback if C cannot be completed |

## 4. Proposed decision

Adopt **Option C as a prototype design direction only**, subject to the contract tests below. Preserve the existing engine's graph semantics and API. Add a sidecar semantic artifact (not implicit engine defaults) that explicitly declares the mapping. If the toy domain cannot give a defensible meaning to a transformation or accessibility predicate, use Option D and label the result as graph-path ranking, not TGCV trajectory recommendation.

This decision is not a declaration that the current demonstrator implements (T_{acc}). It is not an ontology freeze or a change to TR-131.

## 5. Candidate sidecar contract (proposal only)

A candidate sidecar should contain:

- `schema_version` and `semantic_model_id`;
- `state_contexts`: each graph state ID maps to an explicit state description and context reference; no ungrounded inference from a label like “B”;
- `transformation_universe`: stable transformation IDs with domain meaning and declared preconditions/admissibility rule references;
- `graph_transition_mapping`: each graph transition ID maps explicitly to zero, one or multiple transformation IDs, with a declared mapping type; missing/ambiguous mappings are not silently resolved;
- `accessibility_rule_set`: versioned rule references defining the candidate universe and (A(S_t,C_t,R_t)), independent of enumerated paths, selector ranking, execution trace, outcome and value;
- `successor_mapping`: declared mapping from a realized transformation and applicable state/context to the resulting state; no inference from endpoints alone where more than one mapping is possible;
- `realization_trace_contract`: required fields for realized transformation ID, source/result state, order, relevant context, evaluated admissibility evidence, evaluator/contract version and provenance;
- `accessibility_comparison_contract`: declared representation/equivalence and (D(T_{acc,t},T_{acc,t+1})) where comparison is used; no assumption that reachable-node/path differences equal (Delta T_{acc});
- `scope_status`: explicitly distinguish `TGCV_SEMANTIC_MAPPING_SPECIFIED`, `GRAPH_ONLY`, and `MAPPING_INCOMPLETE`.

This is a minimum review checklist, not yet a production JSON schema. It must not be implemented until its fields and semantics have been reviewed.

## 6. Contract tests to implement after the sidecar schema is approved

| ID | Test / adversarial case | Required result |
|---|---|---|
| SL-01 | All graph state references in sidecar exist | Valid mapping; unknown state rejected |
| SL-02 | All referenced graph transition IDs exist | Valid mapping; unknown transition rejected |
| SL-03 | Transition maps to no transformation | Allowed only with explicit declared reason/status; never silently treated as a TGCV transformation |
| SL-04 | Transition maps to multiple transformations | Valid only when mapping type and disambiguation/successor rules are explicit |
| SL-05 | Two transformations share the same source/target | Both identities preserved; trace identifies the realized transformation |
| SL-06 | A graph edge has no semantic mapping | Overall status is `MAPPING_INCOMPLETE` or `GRAPH_ONLY`; no TGCV claim |
| SL-07 | Accessibility is computed before/without selector output | (T_{acc}) unchanged when selector ranking changes |
| SL-08 | Accessibility is computed without execution trace/outcome/value | No dependence on realization, outcome or value fields |
| SL-09 | A condition is unevaluated or unknown | Transformation not marked admissible; no traversal as if condition were true |
| SL-10 | A temporal prerequisite is unsatisfied | Corresponding transition remains unavailable under that scenario |
| SL-11 | Realization trace contains only state sequence, no transformation ID | Reject as insufficient for TGCV (T_{real}) trace |
| SL-12 | Same accessibility set but different realized transformations | Representation permits distinct traces while preserving same (T_{acc}) |
| SL-13 | Reachable nodes or paths differ between scenarios | Do not emit (Delta T_{acc}) unless the independent accessibility comparison contract supports it |
| SL-14 | Semantic mapping/version changes | Hash/provenance identifies the exact mapping version used for ranking/execution |
| SL-15 | Sidecar absent or malformed | Preserve graph-engine behavior, but label output graph-only; do not call it TGCV accessibility/trajectory |
| SL-16 | Selector returns a ranking | Ranking cannot mutate the semantic layer or add/remove accessible transformations |

These are software-contract tests for representation integrity, not scientific experiments or evidence of TGCV validity.

## 7. Acceptance and stop rules

Before code changes:
1. Review the candidate fields against TR-131 and the existing engine/selector interfaces.
2. Specify a tiny domain example in which transformation meaning and accessibility rules can be stated independently of the resulting trajectory/outcome.
3. Confirm that the example does not make every edge automatically accessible and does not define (T_{acc}) from the path list.
4. Approve a versioned schema and fixture.

If these cannot be met without inventing semantics for the toy domain, choose Option D and retain the graph as a graph-only demonstrator. Do not broaden claims to preserve the planned selector feature.

## 8. Governance boundary

The proposal does not authorize scientific execution or a runtime test run. It does not alter the current engine, the interactive demonstrator, PR #99, TGCV Core, RMA, Evidence→Claim Matrix, or any claim status.

**Proposed disposition:** evaluate a separate semantic sidecar first; keep selector/UI integration gated until the mapping passes contract tests.
