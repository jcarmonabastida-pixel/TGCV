# TI-001 V009 — Runtime Diagnostic Specification 001

**Status:** READY FOR NON-SCIENTIFIC DIAGNOSTIC — SCIENTIFIC EXECUTION NOT AUTHORIZED

## Purpose
Determine whether the V009 runtime surface can complete the required A/B response when the output budget is increased from the V008 value of 16 to 64 tokens.

## Diagnostic configuration
- model: gpt-5.6-luna
- API: Responses API
- temperature: omitted
- top_p: 0.98
- max_output_tokens: 64
- tools: []
- tool_choice: auto
- background: false
- conversation: null
- previous_response_id: null
- reasoning: null
- store: false

## Diagnostic boundary
- No V008 fixture input.
- No scientific decision unit.
- No scientific execution.
- No scientific result.
- Diagnostic response must be recorded separately.
- The diagnostic must use the intended A/B response surface and establish that the response completes without max_output_tokens exhaustion.

## Pass criteria
1. response status is completed;
2. incomplete_details is null;
3. output_text is non-empty;
4. no max_output_tokens exhaustion;
5. diagnostic_only is true;
6. scientific_execution is NOT_PERFORMED.

A diagnostic PASS does not authorize V009 scientific execution.

**scientific_execution:** NOT_PERFORMED
