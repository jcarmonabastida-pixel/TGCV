# VSL A Executable Bundle — Post-Correction Integrity Audit 001

**Date:** 2026-09-28  
**Audited canonical commit:** 2a67cf21165ba66d4986e03ce36bb243005d7a8  
**Status:** AUDIT COMPLETE — COHERENCE BLOCKED BY STALE EMBEDDED COMMIT REFERENCES

## Scope

Audit of the canonical contents of VSL_EXP_A_EXECUTABLE_BUNDLE_001 after correction of the integrity-manifest structure.

## Verified Git blob identities

| File | Git blob SHA |
|---|---|
| EXECUTION_SPEC.md | 63e27ced5606c8e60606c695ea6d95610c59439b |
| EXECUTOR_2_RECONSTRUCTION_SPEC.md | b87b3911e322d6d35b89fdabf0d806372c102eea |
| FREEZE_MANIFEST_001.md | a5844317787a2ec07dd4db51ab1ded29972e9bd3 |
| MANIFEST_SHA256.md | daf63489bdc016366cea0bd2cf21f727a824d272 |
| execute.py | 4165bf5a112187e312cbd2c9c2728927fdefa888 |
| Frozen A VSL reference | b4e97d5441c45ab43da879986816803e590f055e |

## Verified byte-level SHA-256 values

| File | SHA-256 |
|---|---|
| EXECUTION_SPEC.md | 7336d3f3f54bb893be4067c59885eabb786010b6d30ee5b01d9a5dfe22a2b15c |
| EXECUTOR_2_RECONSTRUCTION_SPEC.md | 62e90c68789ce7a6f6aa41a00879afa2d51c6702af56d1cf7cdea8ab985cd754 |
| FREEZE_MANIFEST_001.md | d6389344e26db5554094e22858e72790dace82bd89da6c0ae909172f0dfca6be |
| execute.py | b1dbdd7b470e8731e48ac9acad54edaab5e7b0afd2847409a7f526a315ddf0dd |
| MANIFEST_SHA256.md | f3a9e88708a84a1001eb60e788c166991c8edbb59a671cc9443f48a908a51d8c |

## Checks

- Executable bundle component identities: PASS
- Frozen A VSL reference identity: PASS
- Byte-level hashes recorded for all non-self-referential components: PASS
- Manifest self-reference exclusion: PASS
- Execution authorization remains NO: PASS
- Bundle remains NOT FROZEN: PASS
- Embedded canonical checkout reference consistency: FAIL

## Identified inconsistency

FREEZE_MANIFEST_001.md embeds commit 9411188cbf366c68fc0dd46ab8fdf344ac4076e8.

MANIFEST_SHA256.md embeds commit f74119e7de2e57dbb269dee300f72df43787a15c.

The audited checkout is 2a67cf21165ba66d4986e03ce36bb243005d7a8a.

These embedded commit references are therefore historical and do not identify the audited checkout.

## Disposition

The integrity data themselves are internally recorded and the executable components are unchanged, but the bundle is NOT yet eligible for final freeze.

No scientific execution is authorized.

## Required corrective action

Replace the historical embedded checkout references with a non-self-referential canonical identification convention, then recompute the affected byte-level SHA-256 values and perform one final integrity audit.

**Execution authorization: NO**
