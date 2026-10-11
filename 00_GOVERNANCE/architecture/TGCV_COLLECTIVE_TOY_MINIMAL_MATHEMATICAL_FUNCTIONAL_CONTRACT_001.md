# TGCV Collective Toy — Minimal Mathematical and Functional Contract 001

- **Status:** PROPOSAL / ENGINEERING CONTRACT DRAFT
- **Date:** 2026-10-11
- **Scope:** Synthetic-only minimum executable demonstrator
- **Canonical effect:** None. This document does not amend TGCV Core, make Ω-primary canonical, or settle the architectural transition question.
- **Scientific execution:** Not authorized by this document. No real dataset, including the existing Rust-derived \(U_t\), is an input to this MVP.

## 1. Purpose

Specify the smallest executable contract for the TGCV “Collective Toy”: an interactive tool in which a developer or scientist can define a test system, inspect its accessible transformations and relations, intervene through controlled scenarios, compare resulting trajectories, and reproduce/audit the computation.

The MVP demonstrates what the implemented model computes under explicit rules. It does not, by itself, validate TGCV as a theory or establish claims about value, intelligence, causality, or empirical systems.

## 2. Design principles

1. **Inspectable:** inputs, rules, and intermediate/output objects are visible.
2. **Deterministic by default:** identical canonical inputs and engine version yield identical canonical outputs.
3. **Small and finite:** the initial engine operates on a finite declared state space and bounded exploration.
4. **Explicit semantics:** a transformation is not treated as available merely because it is drawn on screen; availability follows the model's declared rules.
5. **Scenario comparison:** each scenario is an explicit intervention against a shared baseline model.
6. **Reproducible:** every run can be exported with all inputs needed to repeat it.
7. **No scientific overclaim:** software conformance, model behavior, and empirical/theoretical evidence are reported separately.
8. **Synthetic-only boundary:** MVP fixtures are authored/artificial. No connection to \(U_t\) or other real-data processing is implemented in this phase.

## 3. Representation boundary

### 3.1 Engineering representation for MVP

The MVP uses a finite transition system as a deliberately limited computational representation:

\[
M = (S, T, R, C, L, s_0)
\]

where:

- \(S\) is a finite set of explicitly defined system configurations/states.
- \(T\) is a finite set of candidate transformations. Each transformation has a stable identifier and declared source/target configuration or a deterministic applicability/effect rule.
- \(R\) is the set of declared relations among transformations and/or system elements that the selected MVP rule profile actually uses.
- \(C\) is the set of explicit scenario conditions/constraints.
- \(L\) is the declared rule/mechanism profile used to evaluate availability and transition effects.
- \(s_0\in S\) is the initial configuration.

For the first fixture, a state may be represented by a node label and a transformation by a directed edge. This is a special case of the finite transition-system interface, not a claim that all TGCV systems reduce ontologically to graphs.

### 3.2 Relationship to the current TGCV working representation

The current working TGCV formulation includes \(T_{acc}=F(S,C,L)\), with \((S,T_{acc})\) as the working Core candidate and \(C/L/P_\tau\) as auxiliary elements; Reach and trajectories are derived/analytical structures. The MVP must not silently equate its state-local enabled transitions with the system-level TGCV object \(T_{acc}\), nor revise or canonize that formulation.

For implementation, define a **state-local enabled-transition set** separately from the TGCV working object \(T_{acc}\):

\[
T_{enabled}(s\mid M,q)=\{t\in T : enabled(t,s,M,q)=\mathrm{true}\}.
\]

This local set is an MVP operational term, not a claim that the canonical/working TGCV \(T_{acc}\) is itself state-indexed. The mapping between the state-local enabled sets produced by the engine and the system-level \(T_{acc}=F(S,C,L)\) must be explicitly reviewed before the contract is frozen. The engine must not use the same symbol for these objects until that mapping is settled.

For MVP profile 1, relations are recorded as descriptive metadata only and do not change transition enablement or effects. The experimental profile 2 (`relation_guarded_graph`, version `1`) adds a narrowly scoped scenario-level guard: a named transition is blocked if its `requires_transition_id` is explicitly disabled in that scenario. This is a prototype-specific global availability rule, not a temporal prerequisite and not a definition of TGCV's system-level `T_acc`. Its implementation is experimental and does not change canonical TGCV architecture.

## 4. Core concepts and outputs

### 4.1 State/configuration

A state is a uniquely identified configuration admitted by the finite model. Its identity and fields are explicit in the input. The initial MVP may use symbolic states. Continuous-valued or unbounded state spaces are out of scope.

### 4.2 Transformation

Each transformation has:
- stable ID;
- source/applicability specification;
- target/effect specification;
- enabled/disabled status or an explicit enablement rule;
- optional declared relation IDs;
- optional human-readable description.

The MVP begins with deterministic transitions. Nondeterministic or probabilistic effects are out of scope until separately specified.

### 4.3 Accessibility

A transition is **enabled at a state** if it is in \(T_{enabled}(s\mid M,q)\) under the frozen scenario and rule profile. This engine-level term is not interchangeable with TGCV's system-level \(T_{acc}\). A state is **reachable** from \(s_0\) if at least one permitted finite sequence of enabled transitions leads from \(s_0\) to that state.

The engine must report separately:
- transitions enabled at the current state under the MVP rule profile;
- reachable states under the exploration policy;
- trajectories discovered within the declared bounds.

These are related but non-interchangeable outputs.

### 4.4 Trajectory

A trajectory is an ordered finite sequence of states and the transformations connecting consecutive states:

\[
\tau=(s_0,t_1,s_1,\ldots,t_n,s_n).
\]

Every transition in a reported trajectory must satisfy the scenario's enablement and effect rules. The MVP reports finite trajectories only. If cycles exist, enumeration requires explicit maximum depth and/or a declared cycle policy.

### 4.5 Scenario

A scenario is a versioned, explicit intervention over a common base model. MVP interventions may:
- enable or disable specified transformation IDs;
- add/remove a declared constraint;
- change a declared rule parameter within its permitted domain.

A scenario may not silently alter the state inventory, transformation definitions, or rule implementation. Such edits create a new model version and must be recorded as such.

### 4.6 Comparison

Compare a named baseline scenario with one or more intervention scenarios under the same model version, exploration bounds, and engine version.

Minimum comparison outputs:
- differences in state-local enabled-transition sets at the specified comparison state(s);
- differences in reachable-state sets;
- trajectory-set differences under the same enumeration bound;
- explicit indication of truncation, cycles, or unexplored space;
- the exact intervention that distinguishes each scenario.

A count difference alone is not an explanation or a scientific conclusion.

## 5. Engine behavior

For a valid model/scenario pair, the engine shall:

1. validate schema, unique IDs, references, initial state, and rule parameters;
2. calculate state-local enabled transitions under the declared MVP rule profile;
3. explore reachable states with a deterministic, documented traversal order;
4. enumerate trajectories only within explicit depth/count bounds;
5. compute scenario differences from canonicalized result sets;
6. emit a structured result and audit record;
7. return explicit validation errors or truncation warnings rather than silently dropping invalid elements.

The first engine must use a stable traversal order (for example, lexicographic ordering by stable IDs) so output ordering is reproducible. The choice of order is an implementation detail that must be versioned, not a theoretical property.

## 6. Canonical input schema (conceptual)

The JSON shape below documents the current prototype input shape; the contract remains a draft and schema-freeze review is still pending:

~~~json
{
  "schema_version": "collective-toy-input-001",
  "model_id": "toy-diamond-001",
  "initial_state": "A",
  "states": ["A", "B", "C", "D"],
  "transitions": [
    {"id": "t_ab", "source": "A", "target": "B"},
    {"id": "t_ac", "source": "A", "target": "C"},
    {"id": "t_bd", "source": "B", "target": "D"},
    {"id": "t_cd", "source": "C", "target": "D"}
  ],
  "relations": [],
  "rule_profile": {"type": "finite_deterministic_graph", "version": "1"},
  "scenarios": [
    {"id": "baseline", "disabled_transitions": []},
    {"id": "block_ac", "disabled_transitions": ["t_ac"]}
  ],
  "exploration": {"max_depth": 4, "max_trajectories": 1000}
}
~~~

This schema is a proposal for the MVP only. If relations or constraints are present, their semantics must be defined by the selected rule profile; arbitrary relation metadata must not be presented as causally operative.

## 7. Hand-checkable acceptance fixture

Base model: states \(A,B,C,D\), initial state \(A\), transitions \(A\to B\), \(A\to C\), \(B\to D\), \(C\to D\).

- Baseline scenario: all four transitions enabled.
- Intervention scenario: disable only \(A\to C\).

Expected outcomes under the finite deterministic graph rule profile:
- Baseline reachable states: \(\{A,B,C,D\}\).
- Intervention reachable states: \(\{A,B,D\}\).
- Baseline complete paths from \(A\) to \(D\): \(A\to B\to D\) and \(A\to C\to D\).
- Intervention complete paths from \(A\) to \(D\): \(A\to B\to D\).
- \(D\) remains reachable after the intervention.
- The engine reports the disabled transition and the resulting differences explicitly.

These are expected outputs from a synthetic fixture, not observed scientific findings.

## 8. Minimum acceptance tests

The implementation is not accepted until automated tests cover:

1. valid input produces the expected fixture results;
2. unknown state/transition references fail validation;
3. duplicate IDs fail validation;
4. disabling a transition removes paths that require it;
5. an unrelated transition is not changed by an intervention;
6. cycles terminate under the declared exploration policy;
7. depth/trajectory limits produce an explicit truncation flag;
8. same canonical input + same engine version produces the same canonical result;
9. canonical serialization and result hashes are stable for identical results;
10. exported run package contains enough information to reproduce the result;
11. invalid input yields a clear error and does not produce a misleading partial PASS.

### 8.1 Requirement-to-test coverage matrix (branch snapshot 2026-10-11)

The following matrix maps the minimum acceptance criteria to tests present in the current prototype branch. “Covered” means an automated test exists and passed in the recorded CI snapshot; it does not imply exhaustive verification of all possible inputs.

| Contract criterion | Current evidence | Status / boundary |
|---|---|---|
| 1. Valid fixture produces expected results | test_diamond_fixture_matches_expected_reachability_and_paths; browser fixture diamond-reference | Covered for the hand-checkable diamond fixture |
| 2. Unknown state/transition references are rejected | test_unknown_state_reference_fails; browser invalid fixtures unknown-endpoint, unknown-relation-prerequisite, unknown-guarded-transition | Covered for these reference types; not every malformed schema shape |
| 3. Duplicate IDs are rejected | test_duplicate_state_id_fails, test_duplicate_transition_id_fails, test_relation_guarded_profile_rejects_duplicate_relation_ids; browser invalid fixtures | Covered for state, transition, and relation IDs |
| 4. Disabling a transition removes paths requiring it | test_diamond_fixture_matches_expected_reachability_and_paths; browser fixtures diamond-reference, multiple-interventions | Covered for tested deterministic graph cases |
| 5. An unrelated transition is unchanged by an intervention | test_intervention_does_not_change_unrelated_transition | Covered by the named unit test |
| 6. Cycles terminate under the exploration policy | test_cycle_terminates_and_marks_depth_truncation; browser fixtures cycle-depth-bound, relation-guarded-cycle-and-bounds | Covered with explicit bounds, not an unbounded enumeration claim |
| 7. Depth/trajectory caps set truncation explicitly | test_trajectory_limit_is_explicit; browser fixtures depth-zero, trajectory-limit | Covered for tested boundary cases |
| 8. Identical canonical input gives deterministic output | test_deterministic_result_hash; test_relation_guarded_profile_applies_multiple_guards_deterministically | Covered for tested fixtures and current engine version |
| 9. Canonical serialization and result hashes are stable | test_deterministic_result_hash; browser/Python checks compare input and result SHA-256 values across 21 valid fixtures | Covered across the current cross-runtime fixture set; not a formal proof for all JSON values |
| 10. Export contains reproduction inputs and hashes | test_export_contains_reproduction_inputs_and_hashes; browser test downloads and parses exported run packages | Covered for package presence and tested export paths; long-term archival and independent replay workflow are not yet a separate acceptance gate |
| 11. Invalid input is rejected without a misleading partial PASS | Browser/Python test checks 25 named invalid fixtures are rejected by both runtimes; Python includes a table-driven schema/resource-boundary test | Expanded coverage for required fields, types, duplicate scenario IDs, self-guards, and documented resource caps; not exhaustive schema fuzzing |

Current browser/Python fixture battery: 9 named hand-authored valid fixtures plus 12 deterministic generated graphs (21 valid fixtures total), and 25 named invalid fixtures. The UI test also checks relation add/remove, profile switching, profile-2 execution, profile-1 inertness, and visual attenuation of a relation-blocked transition. These counts describe the checked-in test definitions, not the number of every internal assertion.

Remaining explicit gaps before contract freeze:
- complete schema/type/range validation matrix for every field and all malformed nested shapes; current fixtures broaden coverage but are not exhaustive;
- combinations of multiple guards that refer to the same guarded transition, and cycles among guard relations;
- a documented policy for whether guard relations are evaluated against explicit interventions only (current implementation) or recursively against other relation-derived disablements;
- an independent export-and-replay test that recomputes all hashes from the exported package and verifies the same canonical result (implemented in tests; confirm the latest CI run before marking the gate closed);
- a review of deterministic ordering/serialization assumptions across supported Python/browser runtimes;
- a formal decision on whether graph-level global availability guards remain the intended experimental semantics.

The mapping to TGCV's system-level T_acc and schema freeze remain separate conceptual/contract gates; a passing coverage matrix does not settle them.

## 9. Audit and reproduction record

Every run shall record at least:
- run ID and timestamp (timestamp is metadata, not part of deterministic result identity);
- input schema version and canonical input;
- model and scenario IDs;
- rule-profile and engine versions;
- exploration bounds and traversal/cycle policy;
- validation result;
- canonical outputs and comparison report;
- truncation/error status;
- code revision identifier, when available;
- cryptographic hashes of canonical input, output, and exported package.

The implementation must define canonical serialization before treating hashes as comparable. A hash proves byte identity for the hashed representation, not scientific validity or model correctness.

## 10. Out of scope for MVP

- processing or importing the real Rust-derived \(U_t\);
- claims of privacy clearance or scientific data admission;
- probabilistic/continuous/unbounded systems;
- automatic inference of relations or causal mechanisms;
- value, reward, utility, outcome, intelligence, or causal-effect calculations;
- declaring Ω-primary or another candidate architecture canonical;
- proof that the implementation's abstractions adequately represent any particular real system.

These may be considered later only with separate specifications and gates.

## 11. Remaining contract gate

A synthetic finite-graph engine and two experimental relation profiles now exist on the development branch. The following contract work remains before freezing this document:
1. review the contract against current canonical/working TGCV definitions and the architectural admissibility boundary;
2. explicitly review the mapping between the engine's state-local enabled transitions and system-level `T_acc`;
3. freeze the input schema and deterministic exploration/truncation rules;
4. reconcile the acceptance tests in this contract with the implemented Python and browser test batteries, recording uncovered cases.

Keep development on a non-main branch. Do not treat software CI as scientific validation or run scientific workflows as part of this prototype step.

## 12. Decision status

- Mathematical/functional contract: **PROPOSED; NOT FROZEN**.
- MVP implementation: **PARTIALLY IMPLEMENTED on a development branch; contract remains draft**.
- Synthetic fixture: **implemented and covered by current CI for selected cases; full acceptance matrix pending**.
- \(U_t\) use: **NOT AUTHORIZED**.
- TGCV Core / Ω-primary canonical status: **UNCHANGED**.
