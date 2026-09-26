# TI-001 V012 V002 Response Validation Procedure 001

For each scientific decision response:

1. Read the provider response without retrying or requesting clarification.
2. Extract the executor's designated output text.
3. Normalize only the transport-level representation required to identify the returned action; do not semantically rewrite the response.
4. Classify VALID only when the resulting action identifier is exactly one of: `a`, `b`, `c`.
5. Classify every other response as INVALID.
6. Never recode, substitute, infer, or retry an INVALID response.
7. Preserve the original response evidence and validity classification.
8. Scientific analysis must use the frozen classification; validation must not alter experimental observations.

Scientific execution remains unauthorized until the execution-package binding preflight and subsequent authorization conditions are satisfied.
