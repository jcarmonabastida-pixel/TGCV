# TI-001 v005 Execution Data Specification 001

**Date:** 2026-09-25  
**Status:** FROZEN EXECUTION-DATA SPECIFICATION — SCIENTIFIC EXECUTION NOT STARTED

## 1. Scope

This specification fixes the replication and decision-unit construction for the already frozen TI-001 v005 scientific design. It does not modify the v005 fixture, treatment mapping, estimand, provider, or runtime.

The user-approved execution size is **32 matched pairs × 3 conditions = 96 decision units**.

## 2. Decision-unit structure

Each pair P001 through P032 contains exactly three decision units: pair_id + control, pair_id + treatment, and pair_id + null.

Total: 32 control, 32 treatment, 32 null, 96 decisions.

Within each pair, all three conditions share state S0, currently executable transformations [a,b,c], task TI001-TASK-001, and decision timing before successor realisation.

The treatment mapping is supplied only by the provider from the frozen v005 fixture.

## 3. Pair identifiers

Pair identifiers are deterministic labels P001 through P032. They carry no semantic information about condition, transformation, preference, outcome, or expected response.

## 4. Assignment

Each pair contains exactly one unit of each condition. The condition sequence is fixed as the neutral structural order: control, treatment, null. This ordering is an execution-data convention only; it is not presented to the decision agent and does not encode a prediction.

## 5. Replication boundary

The 32 pairs constitute the complete authorized v005 decision sample. No additional pairs may be added during execution. No v004 seed, pair count, randomization procedure, environment seed, successor generator, or successor table is inherited. No adaptive stopping, replacement, or selective repetition is permitted.

## 6. Decision-unit serialization

Each unit contains only pair_id and condition. The provider derives the actual decision input from the frozen v005 fixture and condition. The decision-unit artifact contains no duplicated future mapping and no successor information.

## 7. Integrity constraints

The execution-data artifact MUST satisfy: exactly 32 unique pair identifiers; exactly three units per pair; exactly one control, treatment, and null per pair; exactly 96 units; no duplicate pair/condition; no predetermined transformation; no selected transformation; no outcome, reward, value, utility, performance, or ranking field; no successor state/accessibility; no v004 execution parameter.

## 8. Scientific boundary

This specification fixes only sample/replication structure. It does not predict divergence, assign preferred transformations, score decisions, or define a composite TI measure. The primary observable remains matched_condition_difference_in_transformation_selection.

## 9. Authorization boundary

Scientific execution has been explicitly authorized by the user after the v005 compatibility gate PASS. This specification records the agreed execution sample but does not itself perform a scientific call. The provider --execute call remains the point at which scientific decisions are generated.

## 10. Traceability

This specification is subordinate to TI001_REDESIGN_PREFLIGHT_SPECIFICATION_002.md, TI001_v005_CANDIDATE_001.json, TI001_V005_EXECUTION_CONTRACT_001.md, TI001_DECISION_AGENT_SPECIFICATION_001.md, and TI001_DECISION_AGENT_RUNTIME_FREEZE_001.md. Historical v004 artifacts remain untouched and are not execution-data sources for v005.
