# TGCV — VSL Execution Gate 001

**Date:** 2026-09-19
**Status:** READY — LOCAL FROZEN CHECKOUT REQUIRED

## Freeze integrity note

The published technical-freeze record captures byte-level SHA-256 values from the local Windows checkout. GitHub-rendered file content uses repository-normalized text representation and therefore must not be used to recompute those byte hashes. The authoritative byte-level values are those captured locally in `VSL_TECHNICAL_FREEZE_CAPTURE_RESULT_001.json`.

## Execution boundary

Execute only from checkout commit:
`9f5b9e72d5354582c2963837ec148071bdb7f602`

Environment:
- Python 3.8.10
- Windows 11 Pro build 26200
- network prohibited

No source file may be edited after the freeze capture.

## Required execution outputs

A:
`03_EXPERIMENTS/VSL/A_EXECUTION_RESULT_001.json`

B:
`03_EXPERIMENTS/VSL/B_EXECUTION_RESULT_001.json`

Each output must preserve:
- N=100;
- both control/treatment conditions per fixture;
- T_acc,0/T_acc,1;
- ΔT_acc;
- trajectories;
- O and V*;
- ΔV*;
- dataset hash.

## Stop conditions

STOP if:
- HEAD differs from the frozen checkout;
- any frozen file hash differs;
- Python/platform differs;
- network is available;
- any bundle file is modified.

No result is evidence until Executor-2 independently reconstructs it.

## Current authorization

`A/B EXECUTION = AUTHORIZED ONLY WITHIN THIS FROZEN BOUNDARY`
`CLAIM INTERPRETATION = NOT AUTHORIZED`
