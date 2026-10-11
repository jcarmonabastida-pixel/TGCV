# Collective Toy — relation-aware execution profile proposal 001

**Status:** Experimental design proposal; not implemented, not canonical TGCV architecture, and not a scientific claim.  
**Scope:** Synthetic-only executable demonstrator. No Rust dataset or (U_t) processing is permitted or required.

## 1. Why a second profile

Profile 1 (`finite_deterministic_graph`, version `1`) treats `relations` as descriptive metadata. They do not affect transitions, reachability, trajectories, or result hashes. Preserve that behavior as the stable baseline.

This proposal defines a separate profile so that operational semantics are explicit and opt-in. Existing profile-1 inputs must not silently change meaning.

## 2. Proposed semantics: guarded transitions

Proposed profile identifier:

```json
{"type":"relation_guarded_graph","version":"1"}
```

A relation is an explicit guard that can enable or disable a named transition for a scenario. The initial minimal vocabulary is intentionally narrow:

```json
{
  "id": "r_guard_1",
  "type": "requires_state",
  "transition_id": "t_bd",
  "state_id": "B"
}
```

Interpretation: transition `t_bd` is enabled only when the current state is `B`. Since the transition itself already has a source, this example is redundant and is **not a useful first rule**. To avoid pretending a tautology adds semantics, implementation is blocked until the relation type is non-redundant and unambiguous.

The actual candidate for a minimal first rule is a scenario-level transition guard:

```json
{
  "id": "r_guard_1",
  "type": "requires_transition_enabled",
  "transition_id": "t_bd",
  "requires_transition_id": "t_ab"
}
```

Interpretation: `t_bd` may be used in a scenario only if `t_ab` is not disabled in that same scenario. This is a global scenario guard, not a state-local causal mechanism. It can alter the enabled transition set and therefore reachable states and trajectories. It must not be described as TGCV's `T_acc`.

## 3. Minimum normative rules if the candidate is approved

1. The profile must be explicitly selected; unknown profiles fail closed.
2. Profile 1 remains byte-for-byte semantically unchanged: relation metadata is inert.
3. Profile 2 must validate relation IDs for uniqueness, type, and referenced transition IDs.
4. A guard that references an unknown transition is invalid input, not a silently ignored relation.
5. The baseline and every intervention use the same relation set; interventions only alter the explicitly declared disabled transitions.
6. Guard evaluation order and result serialization must be deterministic.
7. Outputs must state the selected profile and the exact applied/blocked relation IDs.
8. Browser and Python implementations must match exactly for valid and invalid fixtures.
9. Exported packages retain the full input, engine/profile versions, output, and SHA-256 fingerprints.
10. No claim about value, causal effect, empirical validity, or TGCV Core follows from passing software tests.

## 4. Key design issue — do not implement yet

The candidate rule `requires_transition_enabled` means “the required transition is not disabled by this scenario,” not “the required transition occurs earlier in a trajectory.” Those meanings are different. A dependency between transition *availability* and transition *occurrence* would require a separate temporal/stateful semantics and additional tests.

Before implementation, decide whether this prototype needs:
- **A. Scenario-level availability dependency** (smallest demonstrator; the required transition is not listed as disabled); or
- **B. Trajectory-level prerequisite** (a transition can occur only after another transition has occurred earlier in that trajectory).

Recommendation for a minimal first executable: option A, named explicitly as a scenario-level availability dependency. Do not use terms like causal dependency, value creation, or system-level `T_acc` for this rule.

## 5. Required test plan

### Compatibility
- Profile 1 fixture with empty relations.
- Profile 1 fixture with arbitrary valid descriptive relation metadata: same scenario results and result hash; different input hash.
- Profile 1 continues to reject unsupported profile identifiers.

### Profile 2 valid cases
- Guarded transition enabled when its prerequisite transition is not disabled.
- Guarded transition blocked when its prerequisite transition is disabled.
- Two guards on distinct transitions.
- Multiple scenarios sharing the same relation set.
- Cycles and depth/trajectory caps under relation filtering.
- Stable outputs and hashes across repeated runs.

### Profile 2 invalid cases
- Duplicate relation IDs.
- Unknown relation type.
- Unknown guarded transition.
- Unknown prerequisite transition.
- Malformed or missing required relation fields.
- Duplicate scenario or transition IDs continue to fail as before.

### Cross-runtime
Every valid fixture must compare scenario results, baseline comparisons, input hashes, and result hashes between Python and Chromium. Every invalid fixture must be rejected by both runtimes with no partial successful result.

## 6. Gate to implementation

Do not implement this proposal until the semantics in section 4 are accepted and the test contract is reviewed. Implement on the existing prototype branch only; retain the current PR and profile 1 as the stable baseline. No merge to `main` is implied by this document.

## 7. Limits

This is a software semantics proposal for a synthetic demonstrator. It is not a formal TGCV definition, not a canonical architecture change, not an experiment on real-world data, and not evidence that transformation-space dynamics cause value.
