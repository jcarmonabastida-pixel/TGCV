# TI-001 V010 Decision-Interface Compatibility Preflight 001

**Status:** READY FOR EXECUTION — SCIENTIFIC EXECUTION NOT AUTHORIZED

## Bound implementation

`TI001_V010_DECISION_INTERFACE_001.py`

Expected implementation properties:

1. Explicit model-facing decision instruction is present.
2. Instruction requires exactly one `A` or `B`.
3. Visible input is restricted to `context`, `available_actions`, `future_structure`.
4. Hidden provenance fields are not transmitted.
5. Output validation accepts only exact atomic `A` or `B` after transport whitespace normalization.
6. JSON extraction is not performed.
7. Natural-language interpretation is not performed.
8. Multiple-action outputs are rejected.
9. No retry or recoding is implemented.
10. Scientific execution is not performed by the interface component.

## Frozen bindings

- V008 fixture remains unchanged.
- Scientific object remains Transformational Intelligence.
- Valid output domain remains A/B.
- No value/reward/utility/performance/task-success input.
- No successor realization.
- No scientific analysis during preflight.

## Gate

This preflight must be executed against the canonical implementation before the V010 execution contract and final pre-authorization gate.

**Scientific execution: NOT AUTHORIZED**
