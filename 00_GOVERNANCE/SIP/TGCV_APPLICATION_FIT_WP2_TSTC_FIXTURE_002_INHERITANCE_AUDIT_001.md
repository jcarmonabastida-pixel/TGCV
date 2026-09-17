# TGCV Application Fit WP2 — TSTC Fixture-002 Inheritance Audit 001

**Status:** `CLOSED — FIXTURE 002 REQUIRES EXPLICIT TRANSITION ADDITIONS; FIXTURE 001 REMAINS IMMUTABLE`

## 1. Audit basis

Compared the proposed Fixture-002 specification against frozen Fixture 001.

Fixture 001 freezes states, contexts, candidate transformation identities, admissibility predicates, interventions, negative controls, coupling rules and baseline boundaries, but does not independently provide a complete executable transition operator for every transformation. fileciteturn174file0

## 2. Elements that can be inherited unchanged

The following can be inherited from Fixture 001 without scientific reinterpretation:

- connectors C01, C03 and C05;
- initial state spaces and initial values;
- transformation identities currently present in Fixture 001;
- admissibility predicates;
- positive interventions;
- negative controls;
- coupling rules;
- baseline information boundary;
- comparison-unit requirements;
- synthetic/non-empirical scope.

## 3. Elements requiring explicit Fixture-002 additions

The following cannot be inherited as complete executable semantics merely from Fixture 001:

- affected-variable declarations for every trajectory transformation;
- deterministic transition operators;
- transition postconditions;
- semantic provenance of each operator;
- complete trajectory eligibility;
- an executable transition producing `repo: clean -> changed` if the C03→C05 path is retained.

## 4. Critical C03 finding

The frozen C03 transformation universe contains `c03.query_db`, `c03.inspect_repo`, `c03.open_pr`, and `c03.complete_task`, while the cross-domain fixture requires a transition from `repo=clean` to `repo=changed`. Fixture 001 does not specify which of those transformations produces that state change. fileciteturn174file0

Therefore Fixture 002 must not silently assign that effect to an existing C03 transformation.

The cleanest representation is to introduce a **new explicitly named repository-changing transformation** only if the synthetic scenario genuinely requires it. That new identity must be treated as a real Fixture-002 scientific-definition change and documented as such.

## 5. Recommended Fixture-002 delta

Minimum delta:

1. Preserve all Fixture-001 state/context variables.
2. Preserve all existing transformation identities and predicates.
3. Add explicit transition metadata to transformations used in trajectories.
4. Add one explicit repository-changing transformation for the C03→C05 coupling only if required by the intended synthetic scenario.
5. Add explicit deterministic operators for the C05 trajectory transformations required by the sequence.
6. Preserve the existing positive and negative controls.
7. Preserve the coupling rules and baseline information boundary.

No additional domains, outcomes, value variables or empirical data should be introduced.

## 6. Freeze condition

Fixture 002 should **not** be frozen yet.

Before freezing, the proposed new C03 transformation and all transition operators must be reviewed to ensure they represent the intended synthetic scenario rather than implementation convenience.

## 7. Execution status

- Fixture 001: `FROZEN / UNCHANGED`
- Fixture 002 specification: `DRAFT SPECIFICATION`
- Fixture 002 freeze: `NOT AUTHORIZED`
- Fixture 002 execution: `NOT AUTHORIZED`
- TSTC scientific result: `NONE`

## 8. Governance boundary

No change to TGCV Core, RMA, Evidence→Claim Matrix, C09, C10, or industrial execution authorization.
