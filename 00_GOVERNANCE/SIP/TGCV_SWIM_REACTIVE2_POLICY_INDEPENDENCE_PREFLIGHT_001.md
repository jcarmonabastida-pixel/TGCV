# TGCV — SWIM Reactive2 Policy-Independence Preflight 001

**Date:** 2026-09-11

**Status:** `PREPARED — LOCAL PREFLIGHT REQUIRED`

**Gate:** `TGCV_SWIM_REACTIVE2_POLICY_INDEPENDENCE_GATE_001.md`

## Purpose

Prepare the controlled Reactive2 execution without executing it. This preflight verifies that the already-governed SWIM infrastructure can support the policy-independence gate using the same frozen inputs as Reactive-0.

## Continuity / governance checks

- Canonical GitHub state: current.
- IGRT governance reconciliation: PASS.
- Evidence→Claim Matrix: v1.2 CURRENT.
- Reactive-0 operationalization: CLOSED — BOUNDED TGCV OPERATIONALIZATION RESULT.
- Reactive2 policy-independence gate: PREPARED — NOT EXECUTED.
- No closed experiment is reopened.
- No new dataset is authorized.
- No claim-level upgrade is authorized by this preflight.

## Required local preflight checks

Run locally from `C:\Users\pedri\TGCV` and record PASS/FAIL before execution:

1. `swim_sa.ini` contains the `Reactive2` configuration mapped to `ReactiveAdaptationManager2`.
2. The frozen SWIM input manifest and the three frozen input SHA256 values remain unchanged.
3. The previously validated OMNeT++ 5.4.1 execution image/binary remains available.
4. The Reactive2 result directory is separate from Reactive-0 results and contains no prior outcome data that could contaminate the reconstruction.
5. No new dataset, trace, configuration, or source modification is introduced.
6. The execution command is the controlled Reactive2 equivalent of Reactive-0 run 0:

```powershell
cd C:\Users\pedri\TGCV; docker run --rm -v "C:\Users\pedri\TGCV\03_EXPERIMENTS\SWIM\dataset\config:/root/seams-swim/swim/simulations/swim_sa:ro" -v "C:\Users\pedri\TGCV\03_EXPERIMENTS\SWIM\dataset\traces:/root/seams-swim/swim/simulations/swim_sa/traces:ro" -v "C:\Users\pedri\TGCV\03_EXPERIMENTS\SWIM\dataset\results\SWIM_SA_REACTIVE2:/root/seams-swim/swim/results:rw" -w /root/seams-swim/swim/simulations/swim_sa swim-tgcv-omnetpp541:latest /root/seams-swim/swim/src/swim swim_sa.ini -u Cmdenv -c Reactive2 -r 0 -n ..:/root/seams-swim/swim/src:/root/seams-swim/queueinglib:/root/seams-swim/swim/src -lqueueinglib
```

**Important:** the command above is an execution template, not an execution record. Do not run it until the gate's execution authorization is explicitly recorded.

## Execution boundary

This preflight does not authorize execution. The gate remains:

`EXECUTION = NOT AUTHORIZED BY THIS RECORD`

A successful local preflight is necessary but not sufficient. The subsequent execution must produce a separately governed result record containing execution integrity, frozen-input provenance, run identity, result artifact hashes, reconstructable pre-decision points, accessibility reconstruction, policy selection, and claim-boundary disposition.

## Scientific stop condition

If any frozen-input, configuration, executable, isolation, or provenance check fails, stop. Do not repair by silently changing the frozen experimental surface; create a bounded governance repair record instead.

## Expected next state

`LOCAL PREFLIGHT PASS` → explicit execution authorization → Reactive2 run 0 → bounded reconstruction → gate disposition.

No Evidence→Claim Matrix update is required at preflight stage because no new empirical evidence has yet been produced.
