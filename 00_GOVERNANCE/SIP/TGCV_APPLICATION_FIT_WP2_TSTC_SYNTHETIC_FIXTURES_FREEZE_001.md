# TGCV — WP2 TSTC Synthetic Fixtures Freeze 001

**Status:** FROZEN — SYNTHETIC FIXTURES DEFINED; EXECUTION NOT STARTED
**Date:** 2026-09-17
**Specification:** `TGCV_APPLICATION_FIT_WP2_TSTC_MINIMUM_DEMONSTRATOR_SPEC_001.md`
**Purpose:** freeze the minimum deterministic fixtures before implementation/execution

## 1. Freeze boundary

This document freezes the first three synthetic connectors for the TSTC demonstrator:

- `FX-C01` — technical orchestration;
- `FX-C03` — agent/tool/permission;
- `FX-C05` — resource/constraint.

No execution result is contained here. All states, transformations, predicates, interventions and baselines are fixture definitions only.

## 2. Common fixture rules

All fixtures use:

- finite state spaces;
- finite transformation universes;
- deterministic predicates;
- no downstream outcome in admissibility;
- deterministic transitions;
- explicit cross-domain dependencies;
- one positive accessibility intervention;
- one negative control.

The initial implementation SHOULD use no randomness.

## 3. FX-C01 — Technical orchestration

### State

```text
service = {absent, deployed}
compute_A = {free, occupied}
compute_B = {free, occupied}
routing = {A, B}
security = {normal, restricted}
```

Initial state:

```text
service=absent
compute_A=free
compute_B=free
routing=A
security=normal
```

### Context

```text
sla = {standard, strict}
policy_deploy = {allowed, denied}
trust_B = {trusted, untrusted}
```

Initial context:

```text
sla=standard
policy_deploy=allowed
trust_B=trusted
```

### Candidate transformations

```text
c01.deploy_A
c01.deploy_B
c01.route_A_to_B
c01.route_B_to_A
c01.restrict_security
c01.restore_security
```

### Admissibility

`deploy_A` iff service absent AND compute_A free AND policy_deploy allowed AND security normal.

`deploy_B` iff service absent AND compute_B free AND policy_deploy allowed AND trust_B trusted AND security normal.

`route_A_to_B` iff service deployed AND routing=A AND compute_B free AND trust_B trusted AND security normal.

`route_B_to_A` iff service deployed AND routing=B AND compute_A free AND security normal.

`restrict_security` iff security=normal.

`restore_security` iff security=restricted.

### Positive intervention I-C01

Change:

`trust_B: trusted → untrusted`.

Expected effect:

`c01.deploy_B` and `c01.route_A_to_B` become inaccessible, while other admissibility conditions remain frozen.

This is a **declared fixture expectation**, not an execution result.

### Negative control N-C01

Change:

`routing: A → B` while service=absent.

No predicate may depend on routing for the declared initial transformations.

Expected:

`ΔT_acc = ∅`.

## 4. FX-C03 — Agent/tool/permission

### State

```text
task = {pending, completed}
db = {available, unavailable}
repo = {clean, changed}
```

Initial state:

```text
task=pending
db=available
repo=clean
```

### Context

```text
permission_db = {granted, denied}
permission_repo = {granted, denied}
tool_query = {available, unavailable}
tool_pr = {available, unavailable}
```

Initial context:

```text
permission_db=granted
permission_repo=granted
tool_query=available
tool_pr=available
```

### Candidate transformations

```text
c03.query_db
c03.inspect_repo
c03.open_pr
c03.complete_task
```

### Admissibility

`query_db` iff db available AND permission_db granted AND tool_query available.

`inspect_repo` iff repo clean/changed AND permission_repo granted.

`open_pr` iff permission_repo granted AND tool_pr available AND repo clean/changed.

`complete_task` iff task pending AND required declared task preconditions are satisfied.

### Positive intervention I-C03

Change:

`permission_repo: granted → denied`.

Expected effect:

`inspect_repo` and `open_pr` become inaccessible; `query_db` remains accessible.

### Negative control N-C03

Change:

`task: pending → pending` is prohibited as a state mutation; instead use a declared metadata-only context change:

`tool_query: available → available`.

Expected:

`ΔT_acc = ∅`.

The negative control is intentionally identity-preserving and tests that the implementation does not manufacture accessibility changes from no substantive change.

## 5. FX-C05 — Resource/constraint coupling

### State

```text
grid_capacity = {high, low}
site_A = {available, unavailable}
site_B = {available, unavailable}
ev_A = {waiting, charging}
ev_B = {waiting, charging}
```

Initial state:

```text
grid_capacity=high
site_A=available
site_B=available
ev_A=waiting
ev_B=waiting
```

### Context

```text
mobility_requirement_A = {normal, urgent}
mobility_requirement_B = {normal, urgent}
charger_A = {V1G, V2G}
charger_B = {V1G, V2G}
```

Initial context:

```text
mobility_requirement_A=normal
mobility_requirement_B=normal
charger_A=V1G
charger_B=V1G
```

### Candidate transformations

```text
c05.start_A
c05.start_B
c05.defer_A
c05.defer_B
c05.redirect_A_to_B
c05.reduce_power_A
```

### Admissibility

`start_A` iff site_A available AND grid_capacity high AND ev_A waiting.

`start_B` iff site_B available AND grid_capacity high AND ev_B waiting.

`defer_A` iff ev_A waiting.

`defer_B` iff ev_B waiting.

`redirect_A_to_B` iff ev_A waiting AND site_B available AND mobility_requirement_A not urgent.

`reduce_power_A` iff ev_A charging AND charger_A in {V1G,V2G}.

### Positive intervention I-C05

Change:

`grid_capacity: high → low`.

Expected effect:

`start_A` and `start_B` become inaccessible; defer transformations remain accessible; redirect remains accessible if its independent conditions hold.

### Negative control N-C05

Change:

`mobility_requirement_A: normal → normal`.

Expected:

`ΔT_acc = ∅`.

## 6. Cross-domain coupling fixture

A minimal coupling scenario links the three connectors without introducing a fourth domain model.

### Coupling rule 1

`FX-C01 security=restricted`
→ `FX-C03 permission_repo=denied`.

Interpretation: a security restriction propagated from technical orchestration changes agent/tool admissibility.

### Coupling rule 2

`FX-C03 repo=changed`
→ `FX-C05 mobility_requirement_A=urgent`.

Interpretation: a declared engineering-state transition changes a resource-allocation requirement.

These are synthetic dependencies deliberately created for the demonstrator. They are **not empirical claims about the real C01/C03/C05 systems**.

## 7. Cross-domain test sequence

The minimum composed fixture is:

```text
Initial
  ↓
FX-C01 intervention
  ↓
security restriction
  ↓
FX-C03 accessibility update
  ↓
agent repository action becomes inaccessible
  ↓
FX-C03 state transition
  ↓
FX-C05 mobility requirement update
  ↓
FX-C05 accessibility update
```

The implementation must record each transition separately so that local accessibility effects are distinguishable from propagated effects.

## 8. Baseline definitions

### C01 baseline

Finite-state rule-based orchestration graph with the same state variables and action preconditions.

### C03 baseline

Capability matrix:

`actor × permission × tool`

plus a finite workflow state.

### C05 baseline

Finite constrained-feasibility model:

`candidate action + resource capacity + mobility constraint → feasible/infeasible`.

### Cross-domain baseline

A directed dependency graph carrying the same explicitly declared coupling edges.

This is intentionally strong enough to expose the possibility that the TGCV representation is merely a relabelling of conventional feasible-action/dependency representations.

## 9. Frozen comparison unit

For every intervention, comparison must use the same:

- state variables;
- context variables;
- candidate transformation identities;
- admissibility conditions;
- transition definition;
- declared cross-domain dependencies.

The baseline is not allowed to receive additional information that the TGCV representation does not receive, and TGCV is not allowed to use information unavailable to the baseline.

## 10. Expected fixture-level observations

These are **expected properties of the fixture**, not results:

1. C01 positive intervention changes `T_acc`.
2. C03 positive intervention changes `T_acc`.
3. C05 positive intervention changes `T_acc`.
4. Each negative control produces `ΔT_acc=∅`.
5. At least one C01 transition propagates to C03.
6. At least one C03 transition propagates to C05.
7. The baseline representations can encode the same bounded feasible-action changes.

The last point is deliberate: it creates the required discrimination challenge rather than presupposing TGCV advantage.

## 11. Implementation gate

Implementation may begin only against these frozen definitions.

Any change to:

- state variables;
- context variables;
- transformation identities;
- admissibility predicates;
- interventions;
- coupling rules;
- baseline information

requires a new fixture version and must not silently modify this frozen version.

## 12. Governance boundary

This fixture freeze does not alter:

- TGCV Core;
- RMA v3.35;
- Evidence→Claim Matrix v1.12;
- scientific evidence status;
- C09/C10 conclusions;
- VSL-44;
- industrial execution authorization.

**Next controlled step:** implement the deterministic fixture engine and run invariant/preflight tests only. No TSTC execution or interpretive result should be generated until the fixture-engine preflight passes.
