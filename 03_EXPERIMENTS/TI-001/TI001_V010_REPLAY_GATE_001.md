# TI-001 V010 — Replay Gate 001

**Status:** PASS — EXECUTOR-2 REPLAY REQUIRED BEFORE SCIENTIFIC ANALYSIS

## Purpose

Establish an independent reconstruction boundary for TI-001 V010 before any scientific interpretation or indicator calculation.

## Primary execution preserved

The V010 primary execution result remains the canonical scientific execution record:

- Result: `03_EXPERIMENTS/TI-001/TI001_V010_SCIENTIFIC_EXECUTOR_1_RESULT_001.json`
- Canonical result blob: `5297b578f250a50e90043dab5806877e3c3eec1d`
- Canonicalization commit: `a30112a660ad30fdcad97dc945fdc0031e8821e0`

The primary result MUST NOT be modified, reclassified, recoded, or replaced by the replay.

## Replay decision

- Executor-2 required: **YES**
- Scientific analysis authorized: **NO**
- Executor-2 scientific execution authorized: **NO**
- Replay purpose: independent reproducibility / implementation reconstruction
- Replay is not a correction or rerun of Executor-1.

## Independence boundary

Executor-2 MUST:

1. independently implement the reconstruction;
2. consume only the frozen V010 contract, canonical fixture specification/fixture, decision-interface specification, required runtime contract, and its own source;
3. not import, call, execute, parse, or consume Executor-1 source or implementation;
4. not consume Executor-1 outputs to generate its own decisions;
5. apply the same exact A/B validity rule;
6. preserve the 420 decision-unit population;
7. preserve the frozen condition and presentation assignments;
8. record its own execution metadata and result.

## Scientific invariants

The replay MUST preserve:

- fixture: `TI001-V008-FIXTURE-001`
- fixture SHA-256: `dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9`
- interface: `TI001-V010-DECISION-INTERFACE-001`
- interface SHA-256: `e025d66e477de3afd79147986b716389d7d7be03d01a21d4380b384e17c8510c`
- decision units: 420
- valid outputs: exactly `A` or `B`
- no retry
- no recode
- no value/reward/utility/performance metric
- no successor realization
- no scientific analysis during replay.

## Gate disposition

**PASS — READY TO FORMALIZE EXECUTOR-2 RECONSTRUCTION CONTRACT.**

No scientific replay execution is authorized by this gate.
