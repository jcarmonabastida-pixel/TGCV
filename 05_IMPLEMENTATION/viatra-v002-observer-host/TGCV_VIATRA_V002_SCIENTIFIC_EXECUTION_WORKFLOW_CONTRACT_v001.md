# TGCV VIATRA V002 — Scientific Execution Workflow Contract v001

**contract_status:** DRAFT_PENDING_PREFLIGHT  
**scientific_execution_authorized:** false

## Purpose

This contract defines the requirements for a future isolated scientific execution workflow for the frozen VIATRA V002 implementation and fixture. It does not authorize scientific execution.

## Frozen technical inputs

1. Canonical implementation commit: `8bef1d02c23b58dc5d5165b8aff51b264d4fd52f`
2. Fixture: `TGCV_VIATRA_MINIMAL_FIXTURE_v002`
3. Fixture freeze audit commit: `ebc46fe21f2ca1585e0fa169de240d64241726d6`
4. Fixture byte manifest blob: `83019cb86e41a3277dbd59b651c1bd5d2c810561`
5. PF-09 runtime-equivalence preflight: workflow run `37074926235`
6. Observer/Listener P3-P4 runtime preflight: workflow run `37665561065`

## Mandatory workflow properties

The future scientific execution workflow MUST:

- be manual-only (`workflow_dispatch`);
- verify the requested execution ref before any scientific execution;
- verify the frozen fixture bytes before any scientific execution;
- fail closed on any implementation, fixture, or package mismatch;
- resolve exactly `org.tgcv.viatra.v002.observer.V002SerialExecutor.execute()` as the scientific execution entry point;
- invoke that entry point only after separate explicit authorization;
- preserve raw execution outputs and cryptographic hashes;
- run the scientific firewall independently of the scientific result;
- publish no scientific interpretation as part of the execution workflow.

## Prohibited behavior

The workflow MUST NOT:

- modify source, fixture, target definition, or generated scientific inputs;
- silently regenerate or replace frozen fixture material;
- alter the primary protocol after execution starts;
- infer scientific authorization from technical PASS;
- perform scientific fitting or inference while the authorization gate remains pending.

## Required preflight evidence

Before explicit authorization, the package MUST establish:

- exact implementation and fixture identity checks;
- deterministic environment capture;
- exact scientific entry point, defined in `TGCV_VIATRA_V002_SCIENTIFIC_EXECUTION_ENTRY_POINT_v001.md`;
- explicit parameters and seed policy;
- expected artifact manifest;
- clean-workspace and contamination check;
- scientific firewall coverage;
- fail-closed behavior.

## Evidence required for every authorized run

Each authorized execution MUST persist:

- workflow run ID;
- canonical implementation commit SHA;
- workflow revision SHA;
- fixture manifest and hashes;
- execution parameters;
- seed(s), if applicable;
- runtime/environment metadata;
- raw outputs;
- output hashes;
- scientific firewall result;
- deviations, if any.

## Authorization boundary

Technical readiness does not constitute scientific authorization.

**This contract does not authorize scientific execution.**
