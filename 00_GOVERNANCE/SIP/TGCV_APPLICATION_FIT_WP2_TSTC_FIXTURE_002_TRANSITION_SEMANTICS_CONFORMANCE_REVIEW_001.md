# TGCV Application Fit WP2 — TSTC Fixture 002 Transition Semantics Conformance Review 001

**Status:** `BLOCKED — DESIGN REQUIRES CORRECTIONS BEFORE FREEZE`
**Date:** 2026-09-17
**Review basis:**
- `TGCV_APPLICATION_FIT_WP2_TSTC_ENGINE_IMPLEMENTATION_SPEC_001.md` — frozen implementation contract;
- `TGCV_APPLICATION_FIT_WP2_TSTC_SYNTHETIC_FIXTURES_FREEZE_001.md` — frozen Fixture 001;
- `TGCV_APPLICATION_FIT_WP2_TSTC_FIXTURE_002_INHERITANCE_AUDIT_001.md`;
- `TGCV_APPLICATION_FIT_WP2_TSTC_FIXTURE_002_TRANSITION_SEMANTICS_DESIGN_001.md`.

## 1. Purpose

Confront the proposed Fixture-002 transition operators with the frozen TSTC implementation contract and the frozen Fixture-001 predicates before any Fixture-002 freeze or execution.

This review is a design/conformance gate only. It does not execute TSTC and does not modify Fixture 001.

## 2. Implementation-contract checks

The TSTC Implementation Spec requires every transformation used by the engine to have:

- `transformation_id`;
- `domain`;
- `preconditions`;
- `affected_variables`;
- `transition_operator`.

It also requires declared-variable-only transitions, explicit coupling, valid trajectories, negative-control invariants, baseline parity and deterministic reproducibility.

The proposed Fixture-002 design supplies explicit affected variables and deterministic operators for the proposed transition set. The new `c03.modify_repo` is correctly identified as a genuine Fixture-002 transformation-universe change rather than an implementation repair to Fixture 001.

## 3. Operator-by-operator review

### C01

| Transformation | Review | Finding |
|---|---|---|
| `c01.deploy_A` | `CONFORMANT_WITH_EXPLICIT_FIXTURE_002_CHANGE` | `service absent → deployed` and `compute_A free → occupied` are compatible with the frozen predicate. No routing mutation is introduced. |
| `c01.deploy_B` | `CONFORMANT_WITH_EXPLICIT_FIXTURE_002_CHANGE` | `service absent → deployed` and `compute_B free → occupied` are compatible with the frozen predicate. No hidden routing mutation is introduced. |
| `c01.route_A_to_B` | `CONFORMANT_WITH_EXPLICIT_FIXTURE_002_CHANGE` | `routing A → B` is exactly representable by the frozen state and compatible with its predicate. |
| `c01.route_B_to_A` | `CONFORMANT_WITH_EXPLICIT_FIXTURE_002_CHANGE` | `routing B → A` is exactly representable by the frozen state and compatible with its predicate. |
| `c01.restrict_security` | `CONFORMANT_WITH_EXPLICIT_FIXTURE_002_CHANGE` | `security normal → restricted` is directly compatible with the frozen predicate. |
| `c01.restore_security` | `CONFORMANT_WITH_EXPLICIT_FIXTURE_002_CHANGE` | `security restricted → normal` is directly compatible with the frozen predicate. |

No C01 operator is internally inconsistent with the frozen state/predicate definitions.

### C03

| Transformation | Review | Finding |
|---|---|---|
| `c03.query_db` | `CONFORMANT_WITH_EXPLICIT_FIXTURE_002_CHANGE` | Identity-preserving is representable because the fixture has no query-result state variable. |
| `c03.inspect_repo` | `CONFORMANT_WITH_EXPLICIT_FIXTURE_002_CHANGE` | Identity-preserving is representable. It must not be assigned `repo clean → changed`. |
| `c03.open_pr` | `CONFORMANT_WITH_EXPLICIT_FIXTURE_002_CHANGE` | Identity-preserving is representable because PR existence is not represented in the frozen state. |
| `c03.complete_task` | `BLOCKED` | The frozen predicate says `task pending AND required declared task preconditions are satisfied`, but those required preconditions are not explicitly enumerated. A deterministic executable predicate/trace cannot be validated without inventing missing conditions. |
| `c03.modify_repo` | `CONFORMANT_WITH_EXPLICIT_FIXTURE_002_CHANGE` | The proposed new transformation has a coherent explicit predicate and operator: `repo clean AND permission_repo granted` → `repo changed`. It is a deliberate Fixture-002 universe change. |

### C05

| Transformation | Review | Finding |
|---|---|---|
| `c05.start_A` | `CONFORMANT_WITH_EXPLICIT_FIXTURE_002_CHANGE` | `ev_A waiting → charging` is compatible with the frozen predicate. |
| `c05.start_B` | `CONFORMANT_WITH_EXPLICIT_FIXTURE_002_CHANGE` | `ev_B waiting → charging` is compatible with the frozen predicate. |
| `c05.defer_A` | `CONFORMANT_WITH_EXPLICIT_FIXTURE_002_CHANGE` | Identity-preserving is representable because no deferral state is represented. |
| `c05.defer_B` | `CONFORMANT_WITH_EXPLICIT_FIXTURE_002_CHANGE` | Identity-preserving is representable because no deferral state is represented. |
| `c05.redirect_A_to_B` | `BLOCKED` | The proposed operator `ev_A waiting → charging` does not represent a redirection to B. Fixture 001 has no vehicle-location/destination variable. The design correctly avoids inventing one, but the proposed non-identity operator nevertheless gives the transformation a state effect that does not encode its named semantic effect. This requires an explicit Fixture-002 design decision. |
| `c05.reduce_power_A` | `CONFORMANT_WITH_EXPLICIT_FIXTURE_002_CHANGE_WITH_LIMITATION` | Identity-preserving is technically representable because no power variable exists. The fixture must explicitly state that power reduction is not represented in the frozen state and must not be interpreted as a hidden grid-capacity mutation. |

## 4. Critical cross-domain inconsistency

The proposed cross-domain sequence is not executable as currently designed.

The design proposes:

1. `C01 restrict_security` → `security=restricted`;
2. coupling → `C03 permission_repo=denied`;
3. C03 accessibility recalculation;
4. `C03 modify_repo` → `repo=changed`;
5. coupling → `C05 mobility_requirement_A=urgent`.

However, the proposed `c03.modify_repo` predicate explicitly requires:

`repo=clean AND permission_repo=granted`.

After step 2, `permission_repo=denied`, therefore `c03.modify_repo` is inaccessible. Consequently the stated sequence cannot reach `repo=changed` and cannot trigger the C03→C05 coupling edge.

This is a genuine design inconsistency, not an implementation defect.

The design document already correctly states that the C03 positive intervention must not be altered merely to preserve the cross-domain path. The same logic applies here: the C01→C03 propagation must not be weakened merely to make the composed sequence executable.

A separate composed scenario/order or a revised explicitly frozen transformation predicate is required. No such revision may be inferred by the implementation.

## 5. Negative controls

The proposed negative controls remain compatible with the implementation contract:

- C01 routing A → B while service absent should not alter admissibility because no frozen C01 initial predicate depends on routing;
- C03 `tool_query available → available` is identity-preserving;
- C05 `mobility_requirement_A normal → normal` is identity-preserving.

The implementation must still execute and verify `ΔT_acc=∅` for each control during preflight.

## 6. Baseline parity

Adding `c03.modify_repo` changes the Fixture-002 transformation universe. Therefore the same frozen information must be made available to the C03 baseline representation. The baseline must not silently omit the new transformation or receive additional information about its effects.

No baseline superiority conclusion is permitted.

## 7. Freeze decision

Fixture 002 **MUST NOT be frozen** on the basis of the current design.

Required corrections before freeze:

1. resolve the under-specified frozen `complete_task` predicate without inventing hidden conditions;
2. resolve the semantic mismatch for `redirect_A_to_B` without silently adding a destination variable;
3. redesign the composed C01→C03→C05 sequence so that its declared predicates actually permit the required transitions, without weakening the C01→C03 coupling merely for execution convenience;
4. explicitly preserve the limitation that identity-preserving transformations do not represent unmodeled real-world side effects;
5. re-run this conformance review after the design corrections.

## 8. Execution boundary

- Fixture 001: `FROZEN / UNCHANGED`.
- Fixture 002: `NOT FROZEN`.
- TSTC execution: `NOT AUTHORIZED / NOT PERFORMED`.
- No empirical claim generated.
- No TGCV Core change.
- No RMA or Evidence→Claim Matrix change.
- No C09/C10 change.
- No industrial execution authorization change.

**Next controlled action:** revise the Fixture-002 transition-semantics design to resolve the three blockers above, then perform a second conformance review before any freeze decision.
