# TGCV Application Fit WP2 — TSTC Synthetic Fixture 002 Specification 002

**Status:** `SPECIFICATION RESTORED — NOT FROZEN`
**Version:** `002`
**Predecessor:** Fixture-002 design specification / transition-semantics design and correction gates
**Fixture 001:** unchanged and immutable
**TSTC execution:** not authorized by this document

## 1. Purpose

Fixture 002 defines a controlled synthetic extension of Fixture 001 in which executable transition semantics are explicit enough to support a bounded TSTC demonstrator without inventing missing predicates at runtime.

This specification records only decisions already established by the preceding Fixture-002 design, conformance and predicate gates. It does not retroactively alter Fixture 001.

## 2. Inheritance boundary

The following are inherited from Fixture 001 unless explicitly overridden below:

- connectors C01, C03 and C05;
- initial states and contexts;
- existing transformation identities and admissibility predicates;
- positive interventions and negative controls;
- coupling relations;
- baseline comparison boundary;
- synthetic/deterministic scope;
- non-claim boundary.

Fixture 002 adds explicit executable transition semantics where those semantics were deliberately defined in the Fixture-002 design process.

No implementation behavior may be promoted to frozen fixture semantics merely because it exists in code.

## 3. Executable transformation universe

### 3.1 C01 — technical orchestration

Executable transformations:

- `c01.deploy_A`
  - precondition: inherited Fixture-001 predicate;
  - affected variables: `[service, compute_A]`;
  - transition: `service: absent → deployed; compute_A: free → occupied`.
- `c01.deploy_B`
  - precondition: inherited Fixture-001 predicate;
  - affected variables: `[service, compute_B]`;
  - transition: `service: absent → deployed; compute_B: free → occupied`.
- `c01.route_A_to_B`
  - precondition: inherited Fixture-001 predicate;
  - affected variables: `[routing]`;
  - transition: `routing: A → B`.
- `c01.route_B_to_A`
  - precondition: inherited Fixture-001 predicate;
  - affected variables: `[routing]`;
  - transition: `routing: B → A`.
- `c01.restrict_security`
  - precondition: `security = normal`;
  - affected variables: `[security]`;
  - transition: `security: normal → restricted`.
- `c01.restore_security`
  - precondition: `security = restricted`;
  - affected variables: `[security]`;
  - transition: `security: restricted → normal`.

### 3.2 C03 — agent/tool/permission

Executable transformations:

- `c03.query_db`
  - precondition: inherited Fixture-001 predicate;
  - affected variables: `[]`;
  - identity-preserving with respect to the represented fixture state.
- `c03.inspect_repo`
  - precondition: inherited Fixture-001 predicate;
  - affected variables: `[]`;
  - identity-preserving with respect to the represented fixture state.
- `c03.open_pr`
  - precondition: inherited Fixture-001 predicate;
  - affected variables: `[]`;
  - identity-preserving with respect to the represented fixture state.
- `c03.modify_repo`
  - **new explicit Fixture-002 transformation**;
  - precondition: `repo = clean AND permission_repo = granted`;
  - affected variables: `[repo]`;
  - transition: `repo: clean → changed`;
  - postcondition: `repo = changed`;
  - semantic provenance: explicitly added in Fixture 002; not inferred from implementation.

The inherited transformation `c03.complete_task` is retained for traceability only and is **not executable** in Fixture 002.

### 3.3 C03 complete_task exclusion

`c03.complete_task`:

- status: `TRACEABILITY_ONLY / NON-EXECUTABLE`;
- reason: `INHERITED_PREDICATE_UNDER_SPECIFIED`;
- excluded from executable `Uτ` for the minimum demonstrator;
- no trajectory eligibility;
- no runtime inference of missing task preconditions is permitted;
- its exclusion is an explicit fixture-definition decision, not an implementation convenience.

The absence of executable preconditions is therefore treated as a bounded limitation rather than filled by assumption.

### 3.4 C05 — resource/constraint

Executable transformations:

- `c05.start_A`
  - precondition: inherited Fixture-001 predicate;
  - affected variables: `[ev_A]`;
  - transition: `ev_A: waiting → charging`.
- `c05.start_B`
  - precondition: inherited Fixture-001 predicate;
  - affected variables: `[ev_B]`;
  - transition: `ev_B: waiting → charging`.
- `c05.defer_A`
  - precondition: inherited Fixture-001 predicate;
  - affected variables: `[]`;
  - identity-preserving in the represented state.
- `c05.defer_B`
  - precondition: inherited Fixture-001 predicate;
  - affected variables: `[]`;
  - identity-preserving in the represented state.
- `c05.redirect_A_to_B`
  - precondition: inherited Fixture-001 predicate;
  - affected variables: `[]`;
  - identity-preserving in the represented state;
  - limitation: Fixture 002 contains no destination/location state variable, so the represented transition cannot encode an explicit destination change. No hidden destination mutation is permitted.
- `c05.reduce_power_A`
  - precondition: inherited Fixture-001 predicate;
  - affected variables: `[]`;
  - identity-preserving in the represented state;
  - limitation: Fixture 002 contains no power-level state variable. No hidden `grid_capacity` mutation or other unrepresented power-state mutation is permitted.

## 4. Executable Uτ boundary

For Fixture 002 minimum execution:

- C01 executable set = all six C01 transformations listed above.
- C03 executable set = `query_db`, `inspect_repo`, `open_pr`, `modify_repo`.
- `complete_task` is excluded from executable `Uτ` but remains in the traceability record.
- C05 executable set = all six C05 transformations listed above.

The exclusion of `complete_task` must be represented explicitly in fixture metadata. It must not be silently filtered by the engine.

## 5. Interventions

The Fixture-001 positive interventions remain unchanged:

- C01: `trust_B: trusted → untrusted`.
- C03: `permission_repo: granted → denied`.
- C05: `grid_capacity: high → low`.

Negative controls remain unchanged:

- C01: `routing: A → B` under a state where no frozen initial predicate depends on routing; expected `ΔT_acc = ∅`.
- C03: identity-preserving `tool_query: available → available`; expected `ΔT_acc = ∅`.
- C05: identity-preserving `mobility_requirement_A: normal → normal`; expected `ΔT_acc = ∅`.

No intervention may be changed merely to force a desired cross-domain trajectory.

## 6. Cross-domain coupling

Two explicit coupling rules are retained:

1. `C01.security = restricted → C03.permission_repo = denied`.
2. `C03.repo = changed → C05.mobility_requirement_A = urgent`.

Local state mutation and propagated cross-domain effect must be logged separately.

## 7. Composed scenarios

The earlier design inconsistency is resolved by treating the two propagation paths as separate composed scenarios.

### Scenario A — C01 → C03

1. Start from the frozen initial states/contexts.
2. Apply `c01.restrict_security` where admissible.
3. Record the local C01 transition.
4. Propagate `security = restricted` to `permission_repo = denied` in C03.
5. Recalculate C03 accessibility.
6. Record the transformations closed by the propagated permission change, including `c03.modify_repo`.

This scenario does not require `c03.modify_repo` to execute after the permission has been denied.

### Scenario B — C03 → C05

1. Use an independent C03 scenario with `permission_repo = granted`.
2. Execute `c03.modify_repo` from `repo = clean` to `repo = changed`.
3. Record the local C03 transition.
4. Propagate `repo = changed` to `mobility_requirement_A = urgent` in C05.
5. Recalculate C05 accessibility.

A single executable C01 → C03 → C05 trajectory is **not claimed** by Fixture 002.

## 8. Determinism and admissibility

- Predicates must be deterministic and outcome-independent.
- `T_acc` must remain a subset of the declared executable `Uτ`.
- No downstream outcome, future activity or observed success may enter an admissibility predicate.
- No transformation outside executable `Uτ` may enter a trajectory.
- No undeclared state/context mutation is permitted.
- No hidden destination, power, task-precondition or other variable may be inferred.

## 9. Baseline and reproducibility boundary

The conventional baseline must receive the same frozen information available to the TSTC representation. No superiority score or aggregate ranking is permitted.

Execution, when separately authorized, must record the implementation-specification reproducibility metadata, including fixture identity/version, source commit, ruleset/universe/configuration hashes, environment, random seed where applicable, and output hash.

A byte-equivalence rerun remains a required conformance check.

## 10. Limitations

Fixture 002 deliberately leaves the following limitations explicit:

- `c03.complete_task` cannot be executed because its inherited predicate is under-specified.
- `c05.redirect_A_to_B` cannot represent an explicit destination variable because none exists in the frozen state model.
- `c05.reduce_power_A` cannot represent a power-level change because none exists in the frozen state model.
- The two cross-domain paths are separate scenarios rather than one full chain.

These limitations are not to be repaired through implementation inference.

## 11. Non-claims

Fixture 002 does not establish:

- TGCV scientific validity;
- empirical causality;
- superiority over conventional baselines;
- generality across domains;
- industrial deployment suitability;
- ROI or economic value;
- `ΔT_acc → ΔV`.

## 12. Freeze status

This file restores the canonical Fixture-002 specification required for the final freeze gate, but it is **not itself the freeze decision**.

The next gate is a whole-fixture conformance review against the frozen TSTC implementation specification and the preceding Fixture-002 audits. Only a PASS at that gate may convert Fixture 002 into a frozen scientific fixture.

Fixture 001 remains unchanged and immutable.
