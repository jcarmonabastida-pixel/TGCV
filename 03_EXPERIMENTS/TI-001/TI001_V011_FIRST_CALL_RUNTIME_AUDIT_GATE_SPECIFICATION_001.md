# TI-001 V011 — First-Call Runtime Audit Gate Specification

Status: GATE SPECIFICATION — SCIENTIFIC EXECUTION NOT STARTED

## Purpose
Audit the canonical Executor-1 implementation immediately before the first provider call. This gate verifies that the executable path preserves the frozen V011 input boundary and execution controls. It does not execute the scientific provider calls and does not authorize execution.

## Required bindings
- Executor version: `TI001-V011-SCIENTIFIC-EXECUTOR-001`
- Executor blob SHA: `578294aa7d2698ffa181ecbf1d1acbfe882087f9`
- Fixture SHA-256: `30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1`
- Interface blob SHA: `8667b0ff70f58283c688f24c76f10db142655d14`
- Generator blob SHA: `9170f767cac3fceccaba248747c6524c5f150e11`
- Schema blob SHA: `b2fef667f6eb33689ece5481957d3917a860dd3e`

## Gate checks
A1 executor exists
A2 executor blob SHA exact
A3 frozen fixture SHA exact
A4 frozen interface blob SHA exact
A5 frozen generator blob SHA exact
A6 frozen schema blob SHA exact
A7 executor version exact
A8 model exact (`gpt-5.6-luna`)
A9 generation configuration exact (top_p=0.98, max_output_tokens=64, tools=[], tool_choice=auto, background=false, store=false, reasoning=None)
A10 exactly one Responses API call site
A11 no retry mechanism in executor
A12 no recode/repair/inference/imputation path in executor
A13 payload is constructed from `model_input["decision"]`
A14 payload excludes hidden provenance fields
A15 payload visible fields are exactly context, available_actions, future_structure
A16 instruction comes from the canonical interface
A17 output validation comes from the canonical interface
A18 no scientific outcome/value/reward/performance fields are transmitted
A19 authorization file remains AUTHORIZED / AUTHORIZED_NOT_STARTED before execution
A20 executor contains no scientific execution before the `--execute` branch
A21 scientific execution result is not created by this gate

## Pass condition
All A1-A21 must be true. PASS means the implementation is cleared for the first-call execution step under the already granted authorization. It does not itself perform provider calls.

## Scientific boundary
This gate does not inspect or alter fixture contents, does not modify the contract, and does not reinterpret V011 estimands.
