# TI-001 V011 E1-R Executor Identity and Compatibility Preflight Specification 001

**Status:** PREFLIGHT SPECIFICATION — SCIENTIFIC EXECUTION NOT AUTHORIZED

## Purpose

Verify that the E1-R executor implementation is exactly bound to the frozen V011 scientific fixture/interface and that the only intended execution-level change is an explicit no-reasoning request.

## Frozen bindings

- Executor blob SHA: `aa77be9715b00ea717cad24bc162b629e62fe919`
- Fixture SHA-256: `30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1`
- Interface blob SHA: `8667b0ff70f58283c688f24c76f10db142655d14`
- Generator blob SHA: `9170f767cac3fceccaba248747c6524c5f150e11`
- Schema blob SHA: `b2fef667f6eb33689ece5481957d3917a860dd3e`
- Model: `gpt-5.6-luna`
- Population: 420 units / 210 pairs.

## Required checks

The preflight must verify:
1. executor source exists, parses, and has the exact expected Git blob SHA;
2. frozen fixture/interface/generator/schema bindings are exact;
3. executor version is `TI001-V011-E1R-SCIENTIFIC-EXECUTOR-001`;
4. exactly one `client.responses.create` call site exists;
5. the request explicitly supplies `reasoning={"effort":"none"}`;
6. persisted generation configuration records the same reasoning setting;
7. model, top_p, max_output_tokens, tools, tool_choice, background and store remain frozen;
8. model-facing payload is still built from the canonical interface decision projection;
9. hidden provenance fields are not transmitted;
10. interface instruction and validator remain the canonical ones;
11. no retry, repair, inference, recoding or imputation logic is introduced;
12. no scientific outcome/value variables are introduced;
13. the executor does not execute unless the separate E1-R authorization record exists and is explicitly AUTHORIZED;
14. E1-R preflight itself performs no provider call.

## Outcome

PASS means E1-R is structurally compatible and ready for the final preauthorization gate. It does not authorize execution.
