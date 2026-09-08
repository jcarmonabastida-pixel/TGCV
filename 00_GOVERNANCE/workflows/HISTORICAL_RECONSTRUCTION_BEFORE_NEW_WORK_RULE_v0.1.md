# TGCV — Historical Reconstruction Before New Work Rule v0.1

**Status:** ACCEPTED — GOVERNANCE PROCESS RULE

## Purpose

Prevent redundant reimplementation, duplicated experiments, and accidental reset of previously established TGCV work.

## Canonical principle

GitHub is the canonical continuity and provenance surface of TGCV. Before initiating a new gate, specification, implementation, audit, execution, or Decision Record, the current and relevant historical GitHub state must be reconstructed.

## Mandatory pre-operation historical reconstruction

Before any new controlled operation, the operator must inspect the relevant historical artifacts and establish:

1. what was previously defined;
2. what was frozen;
3. what was implemented;
4. what was executed;
5. what result was obtained;
6. what was formally accepted;
7. what remains OPEN, CONDITIONAL, BLOCKED, or unresolved;
8. whether the apparently new problem was already solved or partially solved;
9. whether an existing frozen artifact is compatible with the proposed operation;
10. whether a proposed new requirement is genuinely necessary or is an unnecessary strengthening that would invalidate/recreate prior work.

## Reuse-before-recreation rule

If compatible prior work exists, it must be reused rather than recreated.

A new definition, implementation, audit, or experiment may be introduced only when the historical reconstruction identifies a real unresolved discrepancy, a changed scientific question, an explicit limitation of the prior work, or a formally justified need for stronger evidence.

## No silent semantic replacement

A later artifact must not silently replace or redefine an earlier frozen semantic contract.

If a new design introduces a stronger or different requirement that conflicts with prior frozen work, the discrepancy must be explicitly documented in a new Decision Record or design-review artifact before implementation or execution.

Historical artifacts must not be rewritten merely to conceal or erase such divergence.

## Evidence-state classification

Every reconstructed line of work should be classified, as applicable, as:

- DEFINED / FROZEN
- IMPLEMENTED
- EXECUTED
- AUDITED
- ACCEPTED
- CONDITIONAL
- OPEN
- BLOCKED
- SUPERSEDED BY EXPLICIT DECISION

The distinction between these states must be preserved. In particular, a design PASS does not imply empirical execution, and an execution PASS does not imply causal, predictive, universal, value, or originality claims.

## Minimum reconciliation record

Before proceeding when prior work is found, the coordination record should identify:

- historical artifact(s);
- their status and scope;
- the proposed new operation;
- requirements already satisfied by historical work;
- genuinely new requirements still open;
- any conflict between historical and current designs;
- the minimum corrective action required.

## Experiment restart prohibition

No experiment may be restarted from zero solely because a newer workstream does not initially reference earlier artifacts.

Before writing new code, the historical implementation and its provenance must be checked. Before rerunning data, prior execution and authorization records must be checked. Before defining a new semantic object, prior semantic gates and accepted operationalizations must be checked.

## Relationship to execution governance

This rule is a precondition to the existing technical execution workflow. It does not authorize execution by itself.

The normal sequence remains:

historical reconstruction → design/reconciliation → preflight → explicit authorization → primary execution → audit → replay → scientific closure.

## Current project interpretation

This rule is particularly mandatory for EXT-1.1 Rust and subsequent TGCV empirical work because the project contains multiple historical semantic gates, operational specifications, audits, and accepted Decision Records. The existence of an apparently new implementation problem must therefore be treated as a hypothesis to verify against GitHub history, not as an assumption.

## Governance intent

The objective is to preserve scientific continuity, minimize unnecessary retracing of already established work, maintain provenance, and prevent the project from repeatedly solving the same problem under slightly different terminology.
