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
- \(T\) is the finite set of transition records declared by this prototype. In schema `collective-toy-input-001`, each record has exactly `id`, `source`, and `target`, representing one directed graph edge. Separate applicability/effect functions and other transformation fields are not supported by this schema; they require a separately versioned extension.
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

Each transition record supported by the current schema has exactly:
- `id`: stable, unique transition identifier;
- `source`: declared source-state ID;
- `target`: declared target-state ID.

The current validator rejects additional transition fields. Enablement is determined by the selected rule profile and scenario-level disabled-transition IDs; relation records live in the top-level `relations` list. Per-transition descriptions, explicit effect functions, and embedded relation IDs are not part of schema v001.

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

A scenario is an explicit intervention over a common base model. In schema `collective-toy-input-001`, the only supported intervention is the `disabled_transitions` list of known transition IDs. Profile 2 may derive additional effective disablements from its declared relation guards, according to the documented guard rule.

Adding/removing arbitrary constraints, changing rule parameters, or changing the state inventory, transition definitions, or rule implementation is not supported by schema v001. Such capabilities require a separately versioned schema and contract rather than being implied by this draft.

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

### 5.1 Current executable conventions (draft; not a schema freeze)

The current implementation has the following observable conventions, which must be reviewed before freezing:

- Scenario results are processed and keyed by scenario ID in lexicographic order. Outgoing transitions are explored by transition ID in lexicographic order; the current trajectory enumerator is depth-first, with the stack arranged to emit that order. Reachable state IDs, enabled transition IDs, disabled transition IDs, and effective disabled transition IDs are returned sorted lexicographically.
- `max_depth` counts transition edges. At the depth boundary, the current path is retained; if an outgoing enabled transition remains, the result is marked `truncated: true`. A terminal path is retained without a depth-truncation warning when no outgoing enabled transition remains. `max_trajectories` is an output cap; if additional paths remain unexplored because the cap is reached, the result is marked truncated. Reachability is calculated separately from bounded trajectory enumeration. Exact-boundary rule: reaching `max_trajectories` alone does not mean truncation; `truncated` is true only if the traversal has evidence of an omitted continuation/path or a depth-boundary path with enabled outgoing transitions. Thus a single complete terminal path with a cap of one is not truncated, and a terminal path ending exactly at `max_depth` is not truncated.
- In profile 2, relation guards are evaluated independently against the scenario's explicit `disabled_transitions` set only. If any guard targeting a transition finds its prerequisite explicitly disabled, that guarded transition is added to the effective disabled set. An `APPLIED` guard does not cancel a different guard's `BLOCKED` effect. Guard-derived disablements are not recursively used as prerequisites for other guards; cycles between guard relations therefore do not trigger recursive propagation.
- The current validator rejects unknown keys on the top-level model, rule_profile, transition, scenario, exploration, and profile-2 relation objects. Profile-1 relation entries remain inert descriptive metadata and are not interpreted as a closed schema. Strict unknown-key rejection is a deliberate MVP choice to catch misspellings before execution; this rule remains part of the draft until the schema is formally frozen.
- The supported hash domain is restricted to JSON values whose numbers are finite safe integers (Python integral floats such as `1.0` normalize to the same representation as `1`), whose strings contain no unpaired Unicode surrogates, and whose object keys are sorted by Unicode code-point order. Fractional numbers and integers outside the JavaScript safe-integer range are rejected, including in profile-1 descriptive metadata. This is an MVP reproducibility constraint, not a general-purpose JSON canonicalization standard.

These conventions describe the present prototype and are not yet frozen normative rules. Any change to traversal, truncation, guard composition, unknown-key policy, or serialization must update both runtimes, tests, and this contract together.

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

### 8.1 Requirement-to-test coverage matrix (branch snapshot 2026-10-11; latest recorded CI for commit aafb7c3aa31d33616d3faad06a68436b00c152b0)

The following matrix maps the minimum acceptance criteria to tests present in the current prototype branch. For the commit named above, CI runs 38166544143 (synthetic engine tests), 38166544196 (browser/cross-runtime tests), and 38166544137 (governance consistency) all completed with success. “Covered” means an automated test exists and passed in that recorded CI snapshot; it does not imply exhaustive verification of all possible inputs.

| Contract criterion | Current evidence | Status / boundary |
|---|---|---|
| 1. Valid fixture produces expected results | test_diamond_fixture_matches_expected_reachability_and_paths; browser fixture diamond-reference | Covered for the hand-checkable diamond fixture |
| 2. Unknown state/transition references are rejected | test_unknown_state_reference_fails; browser invalid fixtures unknown-endpoint, unknown-relation-prerequisite, unknown-guarded-transition | Covered for these reference types; not every malformed schema shape |
| 3. Duplicate IDs are rejected | test_duplicate_state_id_fails, test_duplicate_transition_id_fails, test_relation_guarded_profile_rejects_duplicate_relation_ids; browser invalid fixtures | Covered for state, transition, and relation IDs |
| 4. Disabling a transition removes paths requiring it | test_diamond_fixture_matches_expected_reachability_and_paths; browser fixtures diamond-reference, multiple-interventions | Covered for tested deterministic graph cases |
| 5. An unrelated transition is unchanged by an intervention | test_intervention_does_not_change_unrelated_transition | Covered by the named unit test |
| 6. Cycles terminate under the exploration policy | test_cycle_terminates_and_marks_depth_truncation; browser fixtures cycle-depth-bound, relation-guarded-cycle-and-bounds | Covered with explicit bounds, not an unbounded enumeration claim |
| 7. Depth/trajectory caps set truncation explicitly | test_trajectory_limit_is_explicit; test_exact_trajectory_cap_does_not_mark_complete_enumeration_truncated; test_terminal_path_at_depth_boundary_is_not_truncated; browser fixtures depth-zero, trajectory-limit, exact-trajectory-cap-is-complete, terminal-at-depth-boundary-is-complete | Covered for tested boundary cases, including two exact boundaries; not a proof for all graphs |
| 8. Identical canonical input gives deterministic output | test_deterministic_result_hash; test_relation_guarded_profile_applies_multiple_guards_deterministically | Covered for tested fixtures and current engine version |
| 9. Canonical serialization and result hashes are stable | test_deterministic_result_hash; browser/Python checks compare input and result SHA-256 values across 27 valid fixtures after the added exact-cap and terminal-depth-boundary cases, including Unicode key-order and safe-integer metadata | Covered across the current cross-runtime fixture set; not a formal proof for all JSON values |
| 10. Export contains reproduction inputs and hashes | test_export_contains_reproduction_inputs_and_hashes; browser test downloads and parses exported run packages | Covered for package presence and tested export paths; long-term archival and independent replay workflow are not yet a separate acceptance gate |
| 11. Invalid input is rejected without a misleading partial PASS | Browser/Python test defines 71 named invalid fixtures to be rejected by both runtimes; all 71 were rejected in both runtimes in the latest successful cross-runtime CI run. Python includes a table-driven schema/resource-boundary test | Expanded coverage includes all seven required top-level fields, wrong container types for states/transitions/relations/rule_profile, duplicate disabled-transition IDs, duplicate scenario IDs, self-guards, and documented resource caps; nested-field coverage is still not exhaustive |

Current browser/Python fixture battery: 15 named hand-authored valid fixtures plus 12 deterministic generated graphs (27 valid fixtures total), and 71 named invalid fixtures. The latest 10-case schema extension covers missing/empty transition fields, fractional and boolean exploration limits, unsupported rule-profile type, and empty disabled-transition IDs. Two additional fixtures cover array/object initial_state values; the Python engine rejects these with ModelValidationError rather than leaking a TypeError, and the browser applies the same explicit string-ID rule. A further 14-case extension now covers relation fields, relation container/unknown-key handling, scenario fields, disabled-transition element types, and missing exploration bounds. The relation fixtures are constructed so referenced transitions exist, isolating the intended field-validation defect. The latest CI confirms 71 uniquely named invalid fixtures; the empty-scenario-ID case is included in that count. The UI test also checks relation add/remove, profile switching, profile-2 execution, profile-1 inertness, and visual attenuation of a relation-blocked transition. These counts describe the checked-in test definitions, not the number of every internal assertion.

Remaining explicit gaps before contract freeze:
- complete schema/type/range validation matrix for every nested field and boundary combination; the new 12-case extension systematically covers all seven required top-level fields and several container-type/duplicate-ID failures, but does not exhaust every nested field or boundary combination;
- no remaining dedicated gap for multiple guards on the same guarded transition or cycles among guard relations in the current fixture set; coverage is finite and does not exhaust arbitrary relation graphs;
- recursive guard evaluation remains explicitly out of scope: guards are evaluated only against the scenario's explicit disabled-transition set, not against disablements caused by other guards; the new tests cover same-target guards and a cyclic guard-reference fixture;
- the export-and-replay check is now confirmed passing in the recorded CI snapshot for the tested package paths; broader long-term archival and independent replay outside CI are not yet a separate acceptance gate;
- a review of deterministic ordering/serialization assumptions across supported Python/browser runtimes, including broader malformed-input fuzzing; numeric/Unicode edge cases now have explicit cross-runtime fixtures for code-point key ordering, integral-float normalization, fractional/unsafe-number rejection, and unpaired-surrogate rejection; strict rejection of unknown keys is implemented as the current draft policy, pending formal schema freeze;
- a formal decision on whether graph-level global availability guards remain the intended experimental semantics; the current OR-style blocking behavior for multiple guards is documented above but remains experimental.

The mapping to TGCV's system-level T_acc and schema freeze remain separate conceptual/contract gates; a passing coverage matrix does not settle them. Historical baseline snapshots are retained as chronology, not as current evidence: browser/Python run 38156848896 reported 24 valid fixtures matched and 25 invalid fixtures rejected; Python run 38156848887 reported 25 tests passed. The current checked-in battery defines 27 valid fixtures (15 named plus 12 deterministic generated graphs) and 71 named invalid fixtures, including required-field/type cases, nested relation/scenario/exploration fields, numeric type boundaries, exact-cap and terminal-depth-boundary cases, malformed initial-state containers, and empty scenario IDs. Latest CI for commit `5a5eb3ba98b36eaf770f0920e9917f3d505a47b7`: browser/cross-runtime run [38168736943](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38168736943), Python engine run [38168736951](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38168736951), and governance consistency run [38168736948](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38168736948), all passed. The browser log confirms 27 valid fixtures matched exactly and 71 invalid fixtures were rejected by both runtimes; the UI tests also passed relation-editor switching, add/remove, profile-2 execution, profile-1 inertness, and independent export replay. This evidence applies to tested fixtures only; it does not prove all-input correctness.

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
2. explicitly review the mapping between the engine's state-local enabled transitions and system-level `T_acc`; the proposed conceptual review is recorded in [TGCV_COLLECTIVE_TOY_TACC_MAPPING_REVIEW_001.md](TGCV_COLLECTIVE_TOY_TACC_MAPPING_REVIEW_001.md), with the field-by-field input/output crosswalk and proposed graph-demonstration scope in [TGCV_COLLECTIVE_TOY_FIELD_MAPPING_AND_MVP_SCOPE_001.md](TGCV_COLLECTIVE_TOY_FIELD_MAPPING_AND_MVP_SCOPE_001.md); both remain proposed and are not frozen;
3. freeze the input schema and deterministic exploration/truncation rules;
4. reconcile the acceptance tests in this contract with the implemented Python and browser test batteries, recording uncovered cases.

Keep development on a non-main branch. Do not treat software CI as scientific validation or run scientific workflows as part of this prototype step.

## 12. Decision status

- Mathematical/functional contract: **PROPOSED; NOT FROZEN**.
- Engineering freeze decision: **DEFERRED**. The latest CI is green, but green CI alone is insufficient: the complete schema/type/range matrix is not exhaustive; broader malformed-input/serialization robustness review remains open; the global availability-guard semantics (including multiple-guard composition) remain experimental; and the proposed mapping to system-level TGCV `T_acc` is not canonical and remains separate from this finite-graph MVP.
- MVP implementation: **PARTIALLY IMPLEMENTED on a development branch; contract remains draft**.
- Synthetic fixture: **implemented and covered by current CI for selected cases; full acceptance matrix pending**.
- \(U_t\) use: **NOT AUTHORIZED**.
- TGCV Core / Ω-primary canonical status: **UNCHANGED**.


### Latest exact-boundary coverage update

The development branch includes browser/Python parity fixtures and matching Python unit tests for exact exploration boundaries, nested relation/scenario/exploration fields, numeric type boundaries, malformed initial_state containers, and empty scenario IDs. The latest 71-fixture snapshot passed CI at browser/cross-runtime run [38168736943](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38168736943), Python engine run [38168736951](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38168736951), and governance consistency run [38168736948](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38168736948). The normative exploration interpretation is stated in §5.1. The contract remains proposed and the schema is not frozen.


### Latest CI reconciliation

As of commit `aafb7c3aa31d33616d3faad06a68436b00c152b0`, the three associated checks completed successfully: synthetic engine tests [38166544143](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38166544143), browser/cross-runtime tests [38166544196](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38166544196), and governance consistency [38166544137](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38166544137). This updates the evidence snapshot only; it does not freeze the contract, prove correctness for all inputs, or validate TGCV scientifically. Any subsequent commit requires its own CI check before its changes can be treated as passing.


### Deterministic malformed-input mutation matrix — PASS

The browser/Python invalid-input battery contains 90 named fixtures, including a 19-case fixed mutation catalogue covering container types, transition fields, scenario IDs and intervention elements, exploration bounds, relation containers/types/references, duplicate scenario IDs, and initial-state type. Python unit tests and the browser cross-runtime suite passed for commit `7ea6df46ad3135a789b579833fae29e972724ab2`: browser/cross-runtime [38169679974](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38169679974), Python engine [38169679950](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38169679950), and governance consistency [38169680046](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38169680046). All 90 invalid fixtures were rejected by both runtimes. The mutation catalogue is deterministic and targeted, not exhaustive property-based testing.


### Generated relation-guarded graph parity extension — PASS

The deterministic generated valid-fixture suite pairs each of 12 generated finite graphs with a profile-2 variant. Each variant adds a valid availability guard from the second chain transition to the first and tests both baseline and a scenario disabling that prerequisite. The browser/Python CI passed for commit `7ea6df46ad3135a789b579833fae29e972724ab2`: browser/cross-runtime [38169679974](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38169679974), Python engine [38169679950](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38169679950), and governance consistency [38169680046](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38169680046). All 39 valid fixtures matched exactly across scenario results, baseline comparisons, input hashes, and result hashes; the editor tests and independent export replay also passed. The 90 invalid fixtures were rejected by both runtimes. This is deterministic targeted coverage, not exhaustive graph coverage or scientific validation.


### Generated multi-guard composition extension — PASS

The generated browser/Python suite now adds 12 further deterministic fixtures (51 valid fixtures total). Each new graph variant places two valid availability guards on the same target transition and runs four scenarios: baseline, disabling prerequisite A, disabling prerequisite B, and disabling both. Under the current experimental semantics, each guard reads the scenario's explicitly disabled transition set; a blocked guard adds its target transition to the effective disabled set, and multiple guards are reported individually in stable relation-ID order. The suite checks exact browser/Python parity of results, baseline comparisons, and SHA-256 fingerprints, plus independent export replay. This tests composition of explicit guards, not recursive or temporal propagation. CI passed for the subsequent branch head `548d6987b7fae485dcbf8b8a13602686ad597933`: browser/cross-runtime [38177144060](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38177144060), Python engine [38177144068](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38177144068), and governance [38177144105](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38177144105).


### Generated cyclic relation-dependency extension — PASS

The deterministic generated suite now adds 12 further profile-2 fixtures (63 valid fixtures total). Each has two valid relations whose targets are each other's prerequisites, producing a cycle in the relation-dependency graph without a self-referential relation. Four scenarios cover baseline, disabling either member independently, and disabling both. This deliberately tests the current non-recursive rule: each guard consults only the scenario's explicit disabled-transition set, so a relation-induced disable is not recursively propagated through the cycle. Browser/Python scenario results, baseline comparisons, input/result SHA-256 values, and independent export replay are checked. The 90 invalid fixtures remain in the battery. This is bounded deterministic coverage, not exhaustive cycle analysis or scientific validation. The complete cycle battery passed in CI at branch head `548d6987b7fae485dcbf8b8a13602686ad597933`: browser/cross-runtime [38177144060](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38177144060), Python engine [38177144068](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38177144068), and governance [38177144105](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38177144105).


### Relation declaration-order invariance — PASS

The deterministic property that permuting the declaration order of valid relations must not change scenario results, comparisons to baseline, or result SHA-256 passed in Python and browser/Python cross-runtime CI. Relation effects are evaluated and reported in stable relation-ID order; the serialized input SHA-256 is expected to change because the input array order changes. The paired relation-cycle fixtures exercise this property while the 90 invalid fixtures remain in the battery. CI passed for commit `f15afcf91c18c6ef4dde424d28663552af983755`: browser/cross-runtime [38182219431](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38182219431), Python engine [38182219430](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38182219430), and governance consistency [38182219472](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38182219472). This establishes only the tested deterministic property, not exhaustive correctness or scientific validity.

### Direct intervention with a non-recursive guard chain — PASS

A targeted fixture combines three transitions in a chain with two availability guards: the middle transition requires the first transition to be explicitly enabled, and the final transition requires the middle transition to be explicitly enabled. Scenarios disable no transitions, the first transition, the middle transition, or the final transition directly. The expected distinction is that a transition disabled as a consequence of a guard is not treated as explicitly disabled when evaluating another guard; direct target disablement likewise does not change the explicit-prerequisite predicate. Python unit tests and the browser/Python cross-runtime suite include this case. CI passed for commit `f15afcf91c18c6ef4dde424d28663552af983755`: browser/cross-runtime [38182219431](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38182219431), Python engine [38182219430](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38182219430), and governance consistency [38182219472](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38182219472). This is bounded synthetic coverage of the current non-recursive semantics, not a claim that recursive or temporal propagation is defined.

### Disabled-transition declaration-order invariance — PASS

For the paired synthetic fixture, permuting the order of the same two IDs in a scenario's `disabled_transitions` list leaves scenario results, baseline comparisons, and the result SHA-256 unchanged, while changing the serialized input SHA-256. The Python unit test and browser/Python cross-runtime fixture both assert these expectations. The 90 invalid fixtures remain part of the cross-runtime battery. CI passed for commit `985188989ce7328a0bbbf1ee82218d3126fc0202`: browser/cross-runtime [38182683261](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38182683261), Python engine [38182683247](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38182683247), and governance consistency [38182683303](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38182683303). This establishes the property for the targeted fixture and current serialization/engine contract, not exhaustive permutation coverage or scientific validity.

### Scenario declaration-order invariance — PASS

A deterministic fixture compares a model with its scenario list in original and reversed order. The Python unit test and browser/Python cross-runtime suite assert equal scenario results, equal baseline comparisons, equal result SHA-256, and different input SHA-256 because the serialized scenario order changes. CI passed for commit `d002211e07f2a9c5c3102ff75b108d00cb057e05`: browser/cross-runtime [38182839369](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38182839369), Python engine [38182839273](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38182839273), and governance consistency [38182839306](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38182839306). This is evidence for the tested fixture and current engine/serialization contract, not exhaustive permutation coverage or scientific validity.

### Transition declaration-order invariance — PASS

A deterministic fixture compares the same transition graph with the `transitions` list in original and reversed order. Python and browser/Python cross-runtime tests assert identical scenario results, baseline comparisons, and result SHA-256, while input SHA-256 differs because serialized input order changes. All three CI checks passed for commit `80c61aa3f07adb5a9a8af0dac2a5fea24ef746dc`: browser/cross-runtime [38182983995](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38182983995), Python engine [38182983994](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38182983994), and governance consistency [38182984017](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38182984017). This establishes the property for the targeted fixture and current engine/serialization contract, not exhaustive permutation coverage or scientific validity.

### State declaration-order invariance — PASS

A deterministic fixture compares the same model with the `states` list in original and reversed order. Python and browser/Python cross-runtime tests assert identical scenario results, baseline comparisons, and result SHA-256, while input SHA-256 differs because serialized input order changes. All three CI checks passed for commit `6e135d7bfd210e306b4b28016cad09bea46ad585`: browser/cross-runtime [38183122426](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38183122426), Python engine [38183122429](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38183122429), and governance consistency [38183122457](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38183122457). This establishes the property for the targeted fixture and current engine/serialization contract, not exhaustive permutation coverage or scientific validity.

### Intervention reachability monotonicity — PASS

For the deterministic diamond fixture, the intervention that disables `t_ac` must not expand the set of reachable states or introduce trajectories absent from the baseline. Python and browser/cross-runtime assertions enforce both subset properties. All three CI checks passed for commit `55ed822763b9d04c6dc1bc6ae90c0aeab4a6f429`: Python engine [38183368693](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38183368693), browser/cross-runtime [38183368690](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38183368690), and governance consistency [38183368681](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38183368681). This evidence is limited to the tested fixture and current direct-transition disabling semantics; it does not establish a general TGCV scientific claim.

### Relation-guarded intervention reachability monotonicity — PASS

The deterministic relation-guarded graph fixture uses the supported profile `relation_guarded_graph` version `1`. With `t_ab` disabled, the scenario must not expand reachable states or introduce trajectories absent from baseline. All three CI checks passed on commit `badd9dfda53633fda7806cdfed5b2ea818054585`: Python engine [38183634825](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38183634825), browser/cross-runtime [38183634840](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38183634840), and governance consistency [38183634847](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38183634847). The preceding failure was a test-fixture profile-version mismatch (version `2` rather than supported version `1`), not evidence of a mathematical counterexample. Evidence is limited to this fixture and current engine semantics; no general TGCV scientific claim is implied.

### Relation-guarded scenario declaration-order invariance — PASS

For the deterministic relation-guarded fixture, reversing the scenario declaration order preserves per-scenario results, comparisons to baseline, and result SHA-256, while input SHA-256 changes due to serialization order. All three CI checks passed on commit `af19dff9b3942e08a12822508da6fb5ec27c90f1`: Python engine [38183783709](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38183783709), browser/cross-runtime [38183783679](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38183783679), and governance consistency [38183783687](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38183783687). The result is limited to the fixture and current serialization/runtime contract; it is not a general scientific validation of TGCV.

### Duplicate semantic guard invariance — PASS

Adding a second `requires_transition_enabled` relation with a distinct identifier but the same transition/prerequisite pair preserved each tested scenario's reachable states, trajectories, and effective disabled transitions. All three CI checks passed on commit `3feb8b6caec6c7533f6f82fcdb921463e657aa0e`: Python engine [38183904902](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38183904902), browser/cross-runtime [38183904904](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38183904904), and governance consistency [38183904903](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38183904903). The check compares graph outcomes only; relation-level audit records may differ because identifiers remain distinct. This is fixture-level software evidence, not a general scientific validation of TGCV.

### Relation-set addition monotonicity — PASS

Comparing a relation-guarded graph with a second model that adds one additional guard, all four deterministic scenarios (baseline, each prerequisite disabled separately, and both disabled) preserved the expected subset property: the extended model's reachable states and trajectories were subsets of those in the original model. All three CI checks passed on commit `c7fba8f755dad378c4ddc4f01cf89740c160c6c0`: Python engine [38184034960](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38184034960), browser/cross-runtime [38184035030](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38184035030), and governance consistency [38184035102](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38184035102). This supports only the tested deterministic fixture and current direct guard semantics, not a general TGCV scientific claim.

### Locality of relation-guard effects — PASS

In the deterministic graph fixture, disabling prerequisite transition `t_ab` caused the guard to disable its target transition `t_bd`, while the alternate path `A → C → D` remained available and `D` remained reachable. The corrected assertion reflects the engine's effective-disabled-transition semantics. All three CI checks passed on commit `383cc3dc70044bb45aac9bbc3278b6d960252518`: Python engine [38184259926](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38184259926), browser/cross-runtime [38184259923](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38184259923), and governance consistency [38184259934](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38184259934). Evidence is limited to this graph and the current direct guard semantics; it is not a general scientific validation of TGCV.

### Inactive relation-guard neutrality — PASS

The relation-free baseline and the relation-guarded baseline produced equal reachable states, trajectories, and effective-disabled-transition sets when the prerequisite was enabled. The initial assertions exposed a representation difference: the relation-free profile omits `effective_disabled_transitions`, whereas the guarded profile returns an empty list. Tests now normalize that absent optional field to an empty list for semantic comparison. The corrected revision `b7cd7eb8eaa87d552606ee9cc8a58ce1d302c7ea` passed Python [38184602776](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38184602776), browser/cross-runtime [38184602761](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38184602761), and governance [38184602796](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38184602796). This is fixture-level evidence under the current semantics, not scientific validation of TGCV.

### Scenario declaration-order isolation — PASS

The same relation-guarded model was evaluated with scenario declarations in forward and reverse order. Per-scenario outcomes and comparisons to baseline remained equal, while the serialized input SHA-256 changed as expected. All three CI checks passed on revision `8c5d460058e1427dc6ca03275f58a0cc72531405`: engine [38184751441](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38184751441), browser/cross-runtime [38184751468](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38184751468), and governance [38184751447](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38184751447). Evidence is limited to the deterministic fixture and current semantics; it does not establish scientific validity of TGCV.

### Disconnected-component invariance — PASS

Adding an isolated component with states `X`, `Y` and transition `t_xy` preserved reachable states, trajectories, and truncation status for every original scenario. The input SHA-256 changed as expected. All three CI checks passed on commit `2f242baecfefb51343f9bd7c360f5fb95e6cff6a`: Python engine [38184882608](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38184882608), browser/cross-runtime [38184882625](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38184882625), and governance [38184882613](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38184882613). Evidence is restricted to the tested fixture and current semantics, not scientific validation of TGCV.

### Combined-intervention monotonicity — corrected fixture PASS

The initial trajectory-subset assertion was too strong: disabling edges may create new terminal paths, so complete trajectory lists need not be subsets. The corrected test checks reachable-state subset monotonicity and that paths in the combined scenario do not use edges disabled in the compared single-intervention scenario. The cross-runtime test initially failed due to a JavaScript reference-scope error; this was corrected by reading relations from the active fixture model. All checks passed on `a4b2d5e06f6398a384d70b2a2cdd4934dd02ff4d`: browser/cross-runtime [38185424609](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38185424609), governance [38185424616](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38185424616), and Python engine [38185424629](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38185424629). This is implementation-level evidence for the defined fixtures and semantics, not scientific validation of TGCV.

### Disabled-transition order invariance — PASS

With the same `model_id`, reversing only the serialized order of the disabled transition IDs preserved scenario results, baseline comparisons, and result SHA-256 while changing input SHA-256 as expected. The corrected revision `edb5c0fbbeac2a04bc7adde28a0ad92250bac0e1` passed all three checks: Python [38185663866](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38185663866), browser/cross-runtime [38185663848](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38185663848), and governance [38185663757](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38185663757). This evidence applies to the defined fixture and current implementation only.

### Duplicate semantic relation — operational idempotence PASS

The same `requires_transition_enabled` relation was added a second time under a distinct relation ID. Python and browser/cross-runtime checks passed on `0417582ba951d0efffbad0f13e16b049c577c069`: Python [38185797856](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38185797856), browser/cross-runtime [38185797809](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38185797809), and governance [38185797821](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38185797821). The test compares operational fields (reachable states, trajectories, effective disabled transitions), not full output metadata; the serialized input hash is expected to change. This establishes idempotence only for this duplicate guard fixture and current rule profile, not a universal normalization rule.



### Conjunctive guards — relation declaration order invariance PASS

For the deterministic fixture with two `requires_transition_enabled` relations targeting the same transition (`t_bd`), reversing the serialized relation list preserved `reachable_states`, `trajectories`, and `effective_disabled_transitions` for each of four scenarios (baseline, prerequisite A disabled, prerequisite B disabled, both disabled). Python and browser/cross-runtime CI passed on `eac6bfa77bf658ce6b671a3b46486f5fe1a21c81`: Python [38186653531](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38186653531), browser/cross-runtime [38186653526](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38186653526), governance [38186653532](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38186653532). The serialized input SHA-256 is expected to differ because the input order differs. This establishes order invariance only for this fixture and current rule profile; it does not establish universal confluence or order-independence for all relation types.


### Direct-intervention reachability monotonicity — fixture-level PASS

For the deterministic `relation-guard-locality` fixture, the scenario disabling `t_ab` is checked against baseline. CI asserts that every reachable state and every trajectory remaining after the intervention was already present in baseline, while the alternative path `A → C → D` remains available and `A → B → D` is absent. Python and browser/cross-runtime tests passed on commit `07b0b26e0c977be328a29b12ebdd43b247f0563c`: engine [38186950514](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38186950514), browser/cross-runtime [38186950515](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38186950515), governance [38186950537](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38186950537). Scope is limited to this deterministic fixture and the current operational semantics; this is not a universal theorem for every model or relation type.


### Combined direct interventions — order of declaration and monotonicity scope

The current input schema represents interventions as an unordered set-like list of transition IDs within each scenario; it does not expose a sequential intervention executor. Accordingly, the tested order property is **permutation invariance of the serialized `disabled_transitions` list**, not temporal commutativity of two executed interventions. The cross-runtime fixture `disabled-transition-order` / `disabled-transition-order-reversed` compares scenario results, baseline comparisons, and result SHA-256 while expecting input SHA-256 to differ. Separately, `combined-disabling-interventions-monotonicity` checks that the combined scenario adds no reachable states relative to either single-intervention scenario and that combined trajectories do not use transitions disabled in either single-intervention case. The engine and browser/cross-runtime suites passed on code commit `07b0b26e0c977be328a29b12ebdd43b247f0563c`; governance, engine, and browser/cross-runtime workflows also passed on documentation commit `6997feac5321d2a5efc4976dc51e147ff38bc841`: engine [38187110289](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38187110289), browser/cross-runtime [38187110346](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38187110346), governance [38187110285](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38187110285). These are finite-fixture software properties, not a general theorem about intervention sequences or TGCV validity.


### Combined-intervention monotonicity — cross-runtime CI PASS

The explicit cross-runtime assertions for fixture `combined-disabling-interventions-monotonicity` are now active. With scenarios `disable_ab`, `disable_ac`, and `disable_both`, the test checks that the combined scenario introduces no reachable state absent from either single-intervention scenario, and that each transition used by a combined trajectory is available under each single-intervention comparison. Python engine [38187349750](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38187349750), governance [38187349753](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38187349753), and browser/cross-runtime [38187349783](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38187349783) all passed on code commit `b6a956bc11902c934583381d7f187b583f4af619`. This is a finite deterministic-fixture result under the current `relation_guarded_graph` semantics, not a universal theorem about intervention sequences or TGCV.


### Disconnected-component isolation — fixture-level CI PASS

The deterministic reference graph and its augmented variant (adding states `X`, `Y` and isolated transition `t_xy`) are compared scenario by scenario. The Python engine and browser/cross-runtime tests assert identical reachable states, trajectories, and truncation flags for the original component; the serialized input SHA-256 must differ. The existing assertions passed on code commit `a714220562ee975dc52f83dd46a6d29c2093e4dd`: engine [38187510955](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38187510955), browser/cross-runtime [38187510959](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38187510959), governance [38187510950](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38187510950). This supports isolation for the finite fixture and tested exploration settings only; it does not prove invariance under every resource limit or graph size.


### Disconnected-component isolation under a depth cap — CI PASS

A cyclic reference graph (including `t_ba`, with `max_depth=3`) is compared against the same graph augmented by disconnected states `X`, `Y` and transition `t_xy`. Python and browser/cross-runtime suites pass while asserting identical reachable states, trajectories, and `truncated` status across scenarios, with distinct input hashes. Evidence on code commit `21e4c6178b7a53f87e451494233f4198a379ab64`: engine [38187821777](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38187821777), browser/cross-runtime [38187821767](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38187821767), governance [38187821795](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38187821795). The earlier browser failure on `3d4381b` was resolved by the subsequent cross-runtime fixture adjustment; these results apply to the final code commit listed above. Scope remains the deterministic fixture and stated exploration bound, not all graph sizes or resource limits.


### Depth-boundary distinction — corrected fixture CI PASS

The depth-boundary fixture's Python expectation was corrected to match the engine's existing reachable-state semantics: with `A → B → C` and `max_depth=1`, the engine reports reachable states `A,B,C` while marking trajectory exploration truncated; with `max_depth=2`, it reports the same reachable states and no truncation. The cross-runtime suite and Python suite both pass on code commit `50d179470af4b8a38cd3e6b1bab4d92f379806c0`: Python [38188443602](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38188443602), browser/cross-runtime [38188443619](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38188443619), governance [38188443639](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38188443639). This records observed behavior and fixture-level consistency; it does not independently establish that reachability computation should or should not be bounded by the trajectory depth parameter.


### Combined depth and trajectory caps — CI PASS

The deterministic branching fixture was exercised under three configurations: (i) `max_depth=1, max_trajectories=1` (truncated), (ii) `max_depth=2, max_trajectories=1` (still truncated by the trajectory cap), and (iii) `max_depth=2, max_trajectories=2` (two trajectories, not truncated). Python, browser/cross-runtime, and governance checks all passed on code revision `e67b92151255d94b9bf9eb23cbf1373e6b9b6f76`: engine [38188583363](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38188583363), browser/cross-runtime [38188583393](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38188583393), governance [38188583276](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38188583276). This supports the tested fixture/configurations only; it is not a general proof for all graphs or cap combinations.
