# TGCV Application Fit WP2 — TSTC Fixture-001 Transition Semantics Provenance Audit 001

**Status:** `CLOSED — FROZEN FIXTURE DOES NOT CONTAIN COMPLETE EXECUTABLE TRANSITION SEMANTICS`

## 1. Purpose

This audit resolves a specific ambiguity exposed by the Fixture-001 adapter audit: whether transition semantics present in the current Python engine may legitimately be treated as semantics frozen in Fixture 001.

They may not.

Fixture 001 is the frozen scientific fixture specification. The Python engine is an implementation artifact. An implementation operator cannot retroactively become part of the frozen fixture merely because it currently performs a plausible state change.

## 2. Provenance rule

For an executable transition to be admitted into a Fixture-001 adapter without a new fixture version, its affected variables and transition effect must be traceable to the frozen fixture definition itself.

The following are therefore distinct:

1. **Frozen fixture semantics** — explicitly specified in Fixture 001.
2. **Implementation semantics** — behaviour currently encoded in `tstc_fixture_engine_v001.py`.
3. **Adapter inference** — a mapping supplied by the adapter without explicit frozen support.

Only category 1 is automatically admissible for the frozen adapter. Categories 2 and 3 cannot silently upgrade the scientific fixture.

## 3. Audit finding

The current engine defines executable operators for all transformations, but the frozen Fixture 001 definitions specify predicates, transformation identities, interventions, negative controls and cross-domain coupling. They do not independently specify complete state/context transition operators for the transformation universe.

Consequently, the presence of operators in the implementation does not establish that their semantics were frozen as part of Fixture 001.

## 4. Consequence for the previous adapter result

The two previous `EXPLICIT-IMPLEMENTATION` mappings for:

- `c01.restrict_security`
- `c01.restore_security`

are implementation-supported mappings, not independently demonstrated frozen-fixture transition semantics.

Under the provenance rule above, they must therefore be treated as **IMPLEMENTATION-AVAILABLE / FROZEN-SEMANTICS-UNVERIFIED**, rather than as frozen executable semantics.

This does not invalidate the engine implementation. It establishes that the implementation and the frozen scientific fixture have different provenance boundaries.

## 5. Transformation classes

### FX-C01

- `c01.deploy_A`: implementation operator exists; frozen executable transition semantics not independently specified.
- `c01.deploy_B`: same.
- `c01.route_A_to_B`: same.
- `c01.route_B_to_A`: same.
- `c01.restrict_security`: implementation operator exists; frozen transition effect is not independently specified beyond the predicate/identity.
- `c01.restore_security`: same.

### FX-C03

All four transformations have implementation operators that are currently `_noop`.

More importantly, no frozen transformation semantics establish `repo: clean -> changed`.

Therefore the C03→C05 coupling path remains non-executable from Fixture 001.

### FX-C05

The implementation currently provides `_noop` operators for the transformation universe. Frozen executable transition effects are not independently specified.

## 6. Critical distinction

The fact that the v001 execution previously produced accessibility differences under interventions is not equivalent to having executed the corresponding transformation trajectories. Those results were accessibility calculations before/after declared interventions and did not establish the missing transformation transition contract.

Therefore no previous TSTC result is upgraded by this audit.

## 7. Decision

Fixture 001 cannot currently support a complete trajectory execution adapter solely from its frozen scientific definition.

The correct next choice is between:

- **Fixture version 002:** explicitly freeze executable transition semantics and the C03 `repo -> changed` transition required by the cross-domain sequence; or
- **bounded non-execution:** retain Fixture 001 unchanged and close the TSTC demonstrator path as incomplete because the required transition semantics are absent.

No semantics will be invented in the adapter.

## 8. Governance impact

None.

This audit does not alter TGCV Core, RMA, Evidence→Claim Matrix, C09, C10, scientific claim status, or industrial authorization.

## 9. Non-claims

No scientific validity, empirical causality, superiority, generality, value, deployment, or industrial applicability claim is established.
