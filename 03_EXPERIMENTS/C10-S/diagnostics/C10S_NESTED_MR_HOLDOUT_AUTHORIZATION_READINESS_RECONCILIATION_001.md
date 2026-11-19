# C10-S — Tier A comparative holdout authorization readiness reconciliation

**Record:** C10S-NESTED-MR-HOLDOUT-AUTHORIZATION-READINESS-RECONCILIATION-001  
**Date:** 2026-11-19  
**Status:** STATIC GATE PASS / HOLDOUT NOT AUTHORIZED / EXECUTION NOT STARTED  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Research branch HEAD at preparation:** `ecdf06d52d07b6541a1474e0781aece382867e25`

## 1. Purpose and boundary

This record reconciles the frozen Tier A comparative holdout protocol, its implemented runner, the completed resource-only preflight and the one-use authorization path. It prepares exact authorization identities without granting authorization or starting the numerical holdout.

The operation remains the bounded methodological comparison required by C10-S: C0 versus C1 in F1 and C0 versus C5 in F5, on fresh independent Tier A datasets. It is not the C10 causal experiment and makes no claim about \(\Delta T_{acc}\to Value\).

## 2. Frozen scientific workload

The existing protocol v1.0 remains unchanged:

- Eight frozen cells: six F1 Gaussian cells and two F5 beta-binomial cells.
- K=1,000 fresh datasets per cell; total 8,000 datasets.
- C0 v002 baseline B=1,000 for every dataset.
- C1 exact pivotal candidate in F1 (analytic; no bootstrap B).
- C5 fitted beta-binomial candidate in F5, B=1,000.
- Confirmatory components: within variance and untruncated raw between variance.
- MCSE is not a confirmatory coverage target; F5 MCSE retains its typed abstention.
- Profile/root diagnostics disabled; no Tier B, no post-hoc cells, no C10 Generator/Analyzer/Evaluator execution.
- Primary run followed by a clean-source replay; record and summary hashes must match exactly.
- No pooling across cells and no post-result changes to K/B or acceptance criteria.

The original Tier A v002 run remains immutable development evidence and is not reused as holdout.

## 3. Exact code and protocol identity

The resource preflight authorization 005 was bound to code commit:

`ec2754659d7237839a487fd855f26c4d4b551782`.

The resource preflight was performed against the earlier code commit `ec2754659d7237839a487fd855f26c4d4b551782`. The validator correction and its regression test have now been incorporated and the static suite has passed on the new exact code commit `e191f3589ba3061eb7dcb9f0fc30ea7f0b60c459`. The preflight evidence remains valid for capacity planning because the change is limited to authorization-output serialization and its test; it does not change the runner, generator, statistical engine, protocol, dependency lock or holdout workflow. The holdout authorization must bind to `e191f3589ba3061eb7dcb9f0fc30ea7f0b60c459`, not to the earlier preflight code commit or a later documentation-only branch HEAD.

### Frozen SHA-256 inventory at the approved code commit

| Component | SHA-256 |
|---|---|
| Protocol v1.0 | `1916d8c1aa5100672bd201281b2fa3c4b4a4a0240ef03b42d8c6ec49d16e1e2a` |
| Comparative runner | `983d46e7874187747662da167e5d71704b586878efe31670786968d7d3f2608c` |
| Comparative inference engine | `3b13cea92eff966c60cd4782dcdea88e9d25254703cf37fbe70fd5430004c54e` |
| Fixture generator | `bd0704c0353f2e32defe627c9f14743999349baff48e05d64b2810d8d732d6bf` |
| Dependency lock | `4bdd6993cd8add430dab560f2e6eabb73028b4693e7f73e73999ecda4b2a30a9` |
| Holdout workflow | `8e6532c6410bf247422a9212179da631754a69edc4d7ac5d983100af27670e6b` |
| Holdout executor | `d9d6756021a07e0368910e472ef74e14bcc777c08eecec7d767517bdfe9372c2` |
| Holdout authorization validator | `e5fa516786d3601496563aba9af205f2707ea5d0d93be8e945dedf13a1b4aaf3` |

The protocol SHA-256 is computed over the exact GitHub file content at the approved code commit. The eight source identities above are the inputs expected by the existing authorization validator/executor.

## 4. Resource preflight evidence

- Run: `44566299402` — SUCCESS.
- Authorization: `C10S-RES-PREFLIGHT-20261119-005` — consumed; not reusable.
- Approved code commit: `ec2754659d7237839a487fd855f26c4d4b551782`.
- Two representative cells, 1,000 datasets each; 2,000 datasets total.
- F1 M=30/R=20: 18.283 s; peak RSS 116.7 MiB.
- F5 M=30/R=20: 229.321 s; peak RSS 119.0 MiB.
- Coverage adjudication was not called; no holdout coverage result was generated.

Disposition recorded by the implementation record: resource readiness PASS for proceeding to the separately authorized 8-cell holdout. The estimate is a capacity-planning result, not a measured full-run duration or a coverage result.

## 5. Authorization payload design

Draft identifier: `C10S-HOLDOUT-20261119-001`.

Dedicated authorization branch, to be created only after the validator gate below passes:

`research/c10s-nested-mr-comparative-auth-C10S-HOLDOUT-20261119-001`

Required authorization properties:
- schema `TGCV-C10S-COMPARATIVE-HOLDOUT-AUTH-001`;
- scope `C10S_NESTED_MR_COMPARATIVE_HOLDOUT_ONLY`;
- exact approved code commit and SHA-256 inventory in §3;
- exact eight-cell roster and K/B values in §2;
- profile diagnostics disabled; Tier B false;
- primary/replay required;
- C10 scientific execution explicitly false;
- one-use approval, short UTC validity window, and authorization commit whose sole parent is the approved code commit;
- authorization commit changes only `00_GOVERNANCE/authorizations/C10S_NESTED_MR_COMPARATIVE_HOLDOUT_AUTHORIZATION.json`;
- commit message must match the holdout workflow's explicit authorization marker.

The authorization draft is stored separately from the workflow-triggering authorization path and is not an APPROVED authorization. No authorization branch or workflow run is created by this record.

## 6. Blocking validator defect found before approval

Static inspection of `validate_c10s_nested_mr_comparative_holdout_authorization.py` found that its CLI writes the validated JSON using a literal escaped backslash-n suffix (`"\\\\n"`) rather than a newline character (`"\\n"`). The resulting output is not valid JSON for the subsequent `json.loads` step in the workflow.

This is a pre-execution orchestration defect. It is not a failure of the runner, not a resource-preflight failure, and not a statistical result.

Required minimum correction:
1. change the CLI suffix to a real newline character;
2. add a deterministic test that invokes the validator CLI with `validate` mocked and verifies that the emitted file parses with `json.loads`;
3. rerun the existing static comparator/runner/authorization suite on the resulting exact code commit;
4. recompute and freeze the source hashes and code commit;
5. only then prepare an APPROVED one-use authorization and its dedicated branch.

No holdout authorization is to be approved or pushed until this gate passes. The prior 60-test PASS on Run `44563560279` does not cover a correction that has not yet been made.

## 7. Current disposition

| Gate | State |
|---|---|
| Scientific protocol and eight-cell roster | FROZEN |
| Comparative engine and runner | IMPLEMENTED |
| Deterministic suite at prior code state | TECHNICALLY TESTED — 60/60 PASS (Run `44563560279`) |
| Corrected full static suite | TECHNICALLY TESTED — 61/61 PASS (Run `44569992586`, commit `e191f3589ba3061eb7dcb9f0fc30ea7f0b60c459`) |
| Resource-only preflight | EXECUTED — PASS (Run `44566299402`) |
| Exact code identity for preflight | RECONCILED |
| Holdout authorization validator CLI | CORRECTED; CLI JSON serialization regression test PASS |
| Full numerical holdout authorization | NOT GRANTED |
| 8,000-dataset holdout | NOT EXECUTED |
| Primary/replay audit | NOT EXECUTED |
| Tier B / C10 scientific execution | OUT OF SCOPE / NOT AUTHORIZED |

**Next minimum action:** the validator correction and static regression gate are complete. The authorization draft has been refreshed to the tested code identity. The remaining step is the separate explicit one-use authorization for the 8,000-dataset Tier A holdout. Do not expand F1/F5 methodology, add cells, or reopen the frozen scientific protocol.


## 8. Amendment — validator correction and static gate PASS (2026-11-19)

The authorization validator CLI had serialized a literal backslash-n sequence instead of a real newline, making the workflow's subsequent JSON parse fail. This was corrected in commit `4996a20dd24c181aeb690c7f03acba8b12a4f4c9`.

A dedicated regression test was added in commit `e993a57d4140a01e93654234e67a768b6134bfa8`. The existing static workflow was extended to compile and execute this test in commit `e191f3589ba3061eb7dcb9f0fc30ea7f0b60c459`.

GitHub Actions run `44569992586` completed **SUCCESS** on that exact commit:
- pinned Python 3.12.10;
- hash-locked dependencies installed successfully;
- compile step passed;
- complete comparator/static test command passed: **61 tests, OK**;
- the new test `test_cli_output_is_valid_json_with_real_newline` passed.

### Final code identity for the upcoming holdout authorization

| Component | SHA-256 at `e191f3589ba3061eb7dcb9f0fc30ea7f0b60c459` |
|---|---|
| Protocol v1.0 | `1916d8c1aa5100672bd201281b2fa3c4b4a4a0240ef03b42d8c6ec49d16e1e2a` |
| Comparative runner | `983d46e7874187747662da167e5d71704b586878efe31670786968d7d3f2608c` |
| Comparative inference engine | `3b13cea92eff966c60cd4782dcdea88e9d25254703cf37fbe70fd5430004c54e` |
| Fixture generator | `bd0704c0353f2e32defe627c9f14743999349baff48e05d64b2810d8d732d6bf` |
| Dependency lock | `4bdd6993cd8add430dab560f2e6eabb73028b4693e7f73e73999ecda4b2a30a9` |
| Holdout workflow | `8e6532c6410bf247422a9212179da631754a69edc4d7ac5d983100af27670e6b` |
| Holdout executor | `d9d6756021a07e0368910e472ef74e14bcc777c08eecec7d767517bdfe9372c2` |
| Authorization validator | `2bdca5bf6a40673a69028b98db726aa8c4b857b5daed49a448aac55ac6038473` |

The authorization draft JSON has been refreshed with this commit and validator hash. It remains `DRAFT_NOT_APPROVED_READY_FOR_EXPLICIT_HOLDOUT_AUTHORIZATION`; no authorization branch was created and no holdout workflow was triggered.

The successful static gate establishes technical readiness of the validator/runner contract, not coverage, calibration, or scientific C10 evidence.
