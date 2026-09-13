# C09 Executor-2 Independent Reconstruction 001

**Status:** `PREPARED — NOT EXECUTED`
**Scope:** independent reconstruction for C09 Operational Execution Bundle 003.

## Independence boundary

Executor-2 is a separately implemented reconstruction. It must not import, call, execute, parse, or consume any Executor-1 output or implementation artifact. It may read only the frozen Bundle 003 specification, fixture and hash manifest, plus its own source.

The reconstruction must independently implement:

1. the 256-unit universe and frozen baseline state;
2. the deterministic SHA256-Fisher-Yates assignment with seed `130917`;
3. control/treatment accessibility;
4. the fixed-score policy without a treatment-flag argument;
5. the one-step transition and endpoint;
6. the predeclared null run;
7. the required integrity checks;
8. the primary and null contrasts as reconstruction outputs.

## Frozen inputs

Bundle 003 remains immutable. Executor-2 does not modify its three frozen components or its manifest.

Declared Bundle 003 component hashes:

- `fixture.json` SHA-256 `3E3AC9601F893B7E01F75813499BB3F539D7B192AE18F0332DC6365AAA5EBD49`
- `EXECUTION_SPEC.md` SHA-256 `D1621DBBCB9DD840828D0F3C431949D7DDA2B73F3E4B43EA86F35FC07A87E10B`
- `execute_c09_bundle_003.py` SHA-256 `94534CC29FA31E86A9936DE8615D8B0114D44F183942C2126E817E507BF62AC3`

## Authorization boundary

Preparation of Executor-2 is not scientific execution authorization. The reconstruction must first be reviewed for independence and then executed as a separate control path. Any integrity failure is `BLOCKED` and no scientific estimate is authorized.

## Prohibited inputs

- Executor-1 result files;
- Executor-1 runtime output;
- post-execution treatment-effect results from any prior run;
- external datasets or services;
- modifications to Bundle 003.

## Acceptance condition

Executor-2 is acceptable only if its independently produced assignment, accessibility sets, selected transformations, endpoint values and integrity status conform to the frozen specification. Agreement with Executor-1, if later observed, is a result of independent reconstruction and not an input to it.
