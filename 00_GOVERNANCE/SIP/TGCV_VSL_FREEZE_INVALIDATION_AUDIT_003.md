# TGCV — VSL Freeze Invalidation Audit 003

**Date:** 2026-09-19
**Status:** BLOCKED — FREEZE 002 INVALIDATED

## Finding

The technical freeze recorded in `TGCV_VSL_FINAL_FREEZE_AUDIT_002.md` cannot be accepted as a valid Git-anchored freeze.

The local capture record states that checkout `9f5b9e72d5354582c2963837ec148071bdb7f602` contained six execution-package byte hashes. The current verification calculated SHA-256 directly from the bytes stored by Git at that exact commit and obtained different values for all six files.

Therefore the captured byte hashes do not describe the bytes stored in the declared frozen commit.

This is distinct from the Git blob SHA versus file SHA-256 distinction: the comparison here is SHA-256(file bytes) against SHA-256(file bytes), with the latter obtained by `git show <commit>:<path>`.

## Verified discrepancy

### A

| File | Captured SHA-256 | SHA-256 of bytes stored at commit 9f5b9e72 |
|---|---|---|
| EXECUTION_SPEC.md | 6926E14E8B735172A21C727AD1BD4E9B6F4AF8DB9F0D3813741A18CCEB8ABDBE | 7336D3F3F54BB893BE4067C59885EABB786010B6D30EE5B01D9A5DFE22A2B15C |
| execute.py | 1AD2A3C34CC03723A9D6E739077B58E049DD5B2CBF116D67AF8E103C951D0F08 | B1DBDD7B470E8731E48AC9ACAD54EDAAB5E7B0AFD2847409A7F526A315DDF0DD |
| EXECUTOR_2_RECONSTRUCTION_SPEC.md | 4427717B1C374F41BF9E2D9DF375C93B8B32B640B56696149C3E773454E18440 | 62E90C68789CE7A6F6AA41A00879AFA2D51C6702AF56D1CF7CDEA8AB985CD754 |

### B

| File | Captured SHA-256 | SHA-256 of bytes stored at commit 9f5b9e72 |
|---|---|---|
| EXECUTION_SPEC.md | 87D1C5A4A463D283F605AFFC3352ABB50291A2197E40ACE3637151A6DF178445 | 2EA9911ADF91FE9BCB24204A6690277AFDFF435E6E176A7CF950A598AF835D3B |
| execute.py | D5DE28BBD97D344FE5DF29C5F69B9387B75639F375893A55D81BC28D89B09371 | 5531D36B00715CB294C3311983173A79497D99F348672EFCAD8E68172C509ED3 |
| EXECUTOR_2_RECONSTRUCTION_SPEC.md | 74197CFD2939550B01A9FF09390A6937966700905682726E2960D134BBA79CB9 | A99A6E67E31FA13162C1F0B330452EE8F45567650E8A9A3E2B25834971C90B11 |

## Consequence for the A/B execution just performed

The A/B result files were generated while `HEAD` was `9f5b9e72...`, but the declared technical freeze record does not describe the bytes actually present in that commit.

Accordingly:

- `A_EXECUTION_RESULT_001.json` = **NON-EVIDENCE / INVALIDATED BY FREEZE INTEGRITY FAILURE**
- `B_EXECUTION_RESULT_001.json` = **NON-EVIDENCE / INVALIDATED BY FREEZE INTEGRITY FAILURE**
- No result values may be interpreted.
- No Executor-2 reconstruction may be started from the invalidated freeze.
- The result files must be preserved, not deleted or edited, as an audit trail.

## Governance decision

`VSL_FINAL_FREEZE_002 = INVALIDATED`

`A = EXECUTION_BLOCKED`

`B = EXECUTION_BLOCKED`

`EXECUTOR_2 = NOT_AUTHORIZED`

No changes are made to TGCV Core, C09, RMA, Evidence-to-Claim Matrix, VSL-SPEC-01 or VSL-EXP-01.

## Corrective action

A new technical freeze must be constructed from a commit whose stored bytes are exactly the intended A/B execution package. The new freeze must:

1. identify the exact commit;
2. compute SHA-256 directly from `git show <commit>:<path>`;
3. record those byte hashes;
4. verify the Executor-2 boundary against the same commit;
5. only then authorize a new A/B execution.

The invalidated freeze record and the two non-evidence execution outputs remain historical audit artifacts.
