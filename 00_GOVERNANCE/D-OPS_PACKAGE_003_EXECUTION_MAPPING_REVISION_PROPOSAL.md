# D-OPS Package 003 — Execution Mapping Revision Proposal

**Status:** PROPOSED — NOT FROZEN / NOT EXECUTED
**Date:** 2026-10-01
**Parent:** D-OPS_FREEZE_PACKAGE_002
**Reason:** Package 002 contains expected-result labels without a frozen case-to-execution mapping for all labels.

## Purpose

Define the missing case-to-execution mapping explicitly without modifying Package 002.

## Mapping supported directly by the frozen package

| expected key | frozen construction | oracle/result |
|---|---|---|
| persistence | D0 unchanged | PERSISTENCE |
| expansion | perturbations.expansion(D0) | EXPANSION |
| contraction | perturbations.contraction(D0) | CONTRACTION |
| reconfiguration | reconfiguration_r3(R3) | RECONFIGURATION_ONLY |
| mixed_identity_change | mixed_identity(D0) | OTHER_STRUCTURAL_CHANGE |
| representation | representation-only operations | INVARIANT |
| state_only_variation | non-structural initial-state view | NO_OMEGA_CHANGE |
| incomparable | explicit incomparable input | NON_COMPARABLE |

## Unmapped frozen labels

The following labels in expected_results.json have no corresponding frozen construction or oracle classification:

- structural_null -> NO_OMEGA_CHANGE
- structural_change_fixed_state -> OTHER_STRUCTURAL_CHANGE
- conditional_H0 -> CONDITIONAL_H0
- conditional_H1 -> CONDITIONAL_H1

They MUST NOT be assigned a construction by inference.

## Governance decision required

Package 002 remains immutable and valid.

A future Package 003 may either:

1. explicitly define these four cases and their deterministic constructions, or
2. remove them through a governed package revision if they are confirmed to be non-operative expected-result entries.

Until that decision is frozen, the governed executor must remain fail-closed.

No execution or scientific interpretation is authorized by this proposal.