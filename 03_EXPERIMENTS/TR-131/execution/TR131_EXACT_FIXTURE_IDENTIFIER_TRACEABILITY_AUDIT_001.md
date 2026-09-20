# TGCV — Exact Fixture Identifier and Traceability Audit 001

**Status:** BLOCKED — EXACT PRIMARY FIXTURE IDENTIFIERS NOT VERIFIED IN THE CANONICAL SOURCE RECORD
**Scientific execution:** NOT AUTHORIZED
**Date:** 2026-09-20

## 1. Audit purpose
Verify the exact source-level identifiers required to make the cross-domain representation package reproducible and freezeable.

## 2. Domain B — ACPBench / VisitAll
The previous package identified ACPBench and VisitAll as the intended source family/domain.

Before freeze, the canonical fixture record must contain the exact:
- ACPBench release/version;
- source repository or benchmark artifact identifier;
- PDDL domain filename/path;
- PDDL problem filename/path;
- action identifiers;
- predicate identifiers used in the selected state;
- exact initial state;
- exact applicable-action set at each tested step;
- exact successor-state effects.

The current package record does not yet contain those exact source artifact identifiers.

Therefore Domain B is not yet freeze-ready.

## 3. Domain A — Rainbow
The primary-source verification established Rainbow as an independently specified self-adaptation framework, including architecture models, adaptation strategies/operators, applicability conditions and effects.

However, the current package still lacks the exact executable example/model artifact from which a finite fixture can be reconstructed without researcher interpretation.

The following must be identified:
- exact Rainbow example or model;
- exact configuration/architecture state;
- exact adaptation strategies/operators;
- exact applicability conditions;
- exact effects;
- exact pre-realization information available to the adaptation mechanism.

Therefore Domain A is not yet freeze-ready.

## 4. Why the blocker must remain
The purpose of the representation test is precisely to determine whether TGCV contributes something beyond existing formal representations.

If the exact source fixture is not frozen, a later constructor could unconsciously choose states/actions that favor `T_acc` as an explicit object.

That would undermine the null hypothesis:
`T_acc ≡ source-defined applicable actions/operators`.

## 5. Traceability schema
For every fixture element, the final audit must provide:

`source_artifact → source_element → fixture_element → TGCV_role`.

Required TGCV roles:
- `S_t`;
- `T_acc,t`;
- `T_real,t`;
- `S_(t+1)`;
- `T_acc,t+1`;
- `ΔT_acc,t`.

No fixture element may have an untraced semantic origin.

## 6. Construction rule
The smallest reproducible fixture must be extracted mechanically from the source artifacts wherever possible.

Where interpretation is unavoidable, the interpretation must be:
1. declared before execution;
2. applied symmetrically across the two representations;
3. independently auditable;
4. incapable of using observed outcomes.

## 7. Decision
**BLOCKED — EXACT FIXTURE IDENTIFIER AND TRACEABILITY AUDIT NOT YET PASSED.**

No freeze.
No scientific execution.
No result inference.
No Core/RMA/Evidence→Claim Matrix modification.

## 8. Next gate
**PRIMARY ARTIFACT RETRIEVAL AND FIXTURE IDENTIFICATION**

Retrieve the exact primary artifacts for both domains and record their immutable identifiers and relevant source elements. Only then construct the final candidate fixtures.