# TI-001 V011 E1-R Replacement Execution Design Specification 001

**Status:** DESIGN — NOT AUTHORIZED

## 1. Purpose

Define the replacement Executor-1 execution for TI-001 V011 after E1 was found non-conformant because the runtime observed non-zero reasoning tokens while the execution package did not explicitly request a no-reasoning configuration.

E1 remains immutable evidence. E1-R is a new execution and requires its own identity/compatibility preflight, final preauthorization gate, and explicit user authorization.

## 2. Scientific continuity

E1-R preserves unchanged:
- Fixture ID: `TI001-V011-FIXTURE-001`
- Fixture SHA-256: `30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1`
- Generator Git blob SHA: `9170f767cac3fceccaba248747c6524c5f150e11`
- Schema Git blob SHA: `b2fef667f6eb33689ece5481957d3917a860dd3e`
- Decision-interface Git blob SHA: `8667b0ff70f58283c688f24c76f10db142655d14`
- Seed: `20260926`
- 420 decision units / 210 pairs
- Model: `gpt-5.6-luna`
- `top_p = 0.98`
- `max_output_tokens = 64`
- no tools
- `tool_choice = "auto"`
- `background = false`
- `store = false`
- same visible payload, instruction, validator, ordering, no retry/recode/repair/imputation rules.

## 3. Controlled configuration change

The only intended execution-level configuration change relative to E1 is to make the no-reasoning setting explicit in the Responses API request:

`reasoning={"effort": "none"}`

The same setting must be recorded in the persisted generation configuration as:

`"reasoning": {"effort": "none"}`

The replacement executor must not merely record this metadata; it must transmit the explicit parameter in the provider request.

Current OpenAI model documentation lists GPT-5.6 Luna as supporting reasoning values including `none`. citeturn202254search0

## 4. Runtime acceptance criterion

For E1-R, the execution-level audit must verify:
1. every request contains `reasoning.effort = "none"`;
2. persisted configuration exactly records the same setting;
3. observed `reasoning_tokens` are zero or otherwise semantically consistent with the documented `none` setting;
4. any non-zero reasoning-token observation is treated as a new deviation and blocks confirmatory analysis;
5. no request is retried or modified after an invalid response.

## 5. Scientific invariants

No change is made to:
- treatment/control/null definitions;
- future-structure content;
- presentation randomization;
- decision instruction;
- A/B validator;
- primary estimands;
- interpretation boundary.

No value, reward, utility, performance, task-success, successor-realization, or external-outcome variables are introduced.

## 6. Evidence separation

E1 and E1-R remain separately identifiable.

E1:
- remains preserved exactly;
- is not repaired or re-run;
- is excluded from confirmatory analysis unless a later formal methodological decision explicitly permits a descriptive-only use.

E1-R:
- is a new execution;
- receives a new result filename and execution identity;
- is not pooled with E1;
- must pass its own primary execution audit before scientific analysis.

## 7. Authorization boundary

This design does not authorize execution.

Required sequence:
1. canonicalize replacement executor implementation;
2. run replacement executor identity/compatibility preflight;
3. run final preauthorization gate for E1-R;
4. obtain explicit user authorization;
5. execute E1-R;
6. run primary execution audit;
7. only then consider scientific analysis.

## 8. Non-retroactivity

No E1 field, response, validity status, reasoning observation, or timestamp may be changed to make E1 conformant with E1-R.

## 9. Required next artifact

The next artifact is the canonical E1-R executor specification/implementation binding `reasoning.effort = "none"` explicitly in the provider request and its persisted runtime configuration.
