# C10-S V_cont — Gate 205: static workflow follow-up audit and corrective patch record

**Status:** STATIC STRUCTURAL REVIEW PASS WITH CORRECTIONS / TARGETED SHELL-FRAGMENT SYNTAX PASS / FULL WORKFLOW YAML VALIDATION OPEN / EXECUTION NOT AUTHORIZED  
**Branch:** `research/c10-s-consolidation-draft`  
**Parent:** Gate 204 — coordinated EP-01/EP-02/EP-03 workflow implementation  
**Audit target HEAD before this record:** `513a724380357739d64afc722b508ce7ec5ec48c`  
**Scope:** follow-up static audit of the three Gate 204 workflows, correction of concrete shell-quoting defects and EP-03 evidence-retention omission, and re-check of profile path/manifest alignment. No workflow dispatch, test, compile, package writer, producer, calibration, Monte Carlo or scientific execution is performed.

## 1. Canonical and historical context

The canonical governance entry point was re-read from GitHub `main`:
- `00_GOVERNANCE/README.md`
- `00_GOVERNANCE/CHATGPT_BOOTSTRAP.md`
- `00_GOVERNANCE/CANONICAL_STATE.json`
- `STATUS.md`
- `00_GOVERNANCE/workflows/HISTORICAL_RECONSTRUCTION_BEFORE_NEW_WORK_RULE_v0.1.md`
- `00_GOVERNANCE/workflows/TECHNICAL_EXECUTION_WORKFLOW_v0.1.md`
- current RMA pointer/master, current Matrix pointer/alias/versioned artifact, current traceability alias/versioned artifact, governance operating principles, scientific asset registry and both read-only validators.

Canonical declarations cross-check manually:
- RMA v3.38: canonical manifest, STATUS and stable RMA pointer agree.
- Evidence→Claim Matrix v1.47: canonical manifest, STATUS and matrix pointer agree.
- RMA traceability v3.38: canonical manifest, STATUS and current traceability alias/versioned file resolve consistently.
- Stable Matrix v1.47 alias and versioned artifact have the same Git blob SHA `5fccfc99af7172b6a2777c93bdbeddd8d4997de8`.
- Current traceability alias and versioned v3.38 file have the same Git blob SHA `448b422b1e30160a161f0068dca3cd842593217b`.
- IGRT remains `NOT_ESTABLISHED / NOT_REQUIRED_BY_CURRENT_CANONICAL_SCHEMA`.
- The current Matrix keeps C10 at `H` and explicitly OPEN; no C10 value or causal-value claim is established.

The two canonical read-only validators were inspected but not executed: this runtime has no TGCV checkout, and external GitHub network access is unavailable from the local shell. This is not recorded as a validator PASS or FAIL. Manual pointer/version cross-check is not a substitute for the required local validator run.

Historical reconstruction confirmed that Gate 203 authorized no implementation by itself and required a separate explicit approval. That approval was supplied in the conversation preceding Gate 204. Gate 204 implemented the approved infrastructure-only scope. Gate 205 is a follow-up static correction, not a new scientific gate and not an execution authorization.

## 2. Findings and corrections

### 2.1 Duplicated shell grouping escapes — corrected

The post-Gate-204 review found duplicated backslashes in the `find` grouping expression used by the final bytecode-cache assertions:
- EP-01 replay assertion;
- EP-02 replay assertion;
- EP-03 post-test assertion.

The affected expression contained two literal backslashes before `(` and `)`. Bash parses that form as an invalid grouping expression and returns a syntax error. A targeted `bash -n` check reproduced the failure for the doubled form and passed for the single-backslash form.

All three workflows have now been corrected to use the valid shell expression:
`\( ... \)`

Correction commits:
- EP-01: `0f7fb6ddb9a3aec5a1da7702b0db6c9b915518e9`
- EP-02: `6a0c2349dca202116a0a6e09f6f3dd195adb5a81`
- EP-03: `9932e964e7c983166e12dd21e12ad1310ca910da`

The exact corrected `find` assertion forms were checked with Bash syntax parsing:
**TARGETED_FIND_ASSERTION_BASH_SYNTAX = PASS.**

This targeted check does not validate every shell command or every workflow YAML expression.

### 2.2 EP-03 output/log retention — corrected

The EP-03 pure-test workflow previously uploaded runtime identity files as its payload but omitted the captured test stdout/stderr files. The manifest calculated their hashes, but the corresponding raw logs were not included in the payload artifact.

The payload upload now includes:
- `c10s-pure-tests-stdout.txt`
- `c10s-pure-tests-stderr.txt`
- the existing runtime identity directory.

Correction commit:
`513a724380357739d64afc722b508ce7ec5ec48c`

The manifest remains a separate artifact. No test scope, source allowlist, dependency lock, or producer boundary changed.

## 3. Rechecked profile boundaries

The three workflow files were retrieved again from the current research branch and checked structurally.

| Control | EP-01 | EP-02 | EP-03 |
|---|---:|---:|---:|
| Manual dispatch only | PASS | PASS | PASS |
| No push/schedule/PR trigger | PASS | PASS | PASS |
| Exact research-branch restriction | PASS | PASS | PASS |
| Explicit test module allowlist | 3 modules | 8 modules | 3 modules |
| Archive source paths | 8 | 18 | 9 |
| Manifest input paths | 8 | 18 | 9 |
| Archive/manifest path order and identity | PASS | PASS | PASS |
| Immutable action commit SHAs | PASS | PASS | PASS |
| `ubuntu-24.04` runner label | PASS | PASS | PASS |
| CPython `3.12.10` selector | PASS | PASS | PASS |
| x86-64 assertion | PASS | PASS | PASS |
| Doubled shell grouping escapes | 0 | 0 | 0 |
| Runtime/source materialization manifest | PASS | PASS | PASS |

The allowlists remain:
- EP-01: `test_focal_harness`, `test_p178_analyzer_bridge`, `test_p178_analyzer_monte_carlo`.
- EP-02: the preceding three plus `test_vcont_integrated_harness`, `test_vcont_benchmark_protocol`, `test_vcont_capture_v2`, `test_vcont_package_v2_serialization`, `test_vcont_package_v2_verifier`.
- EP-03: `test_vcont_capture_v2`, `test_vcont_package_v2_serialization`, `test_vcont_package_v2_verifier`.

The exact archive path arrays and corresponding manifest path arrays were compared in order. They match at 8/8, 18/18 and 9/9 paths respectively.

Static import inspection of the allowlisted tests and their declared local modules confirms the dependency partition:
- EP-01 requires NumPy and SciPy.
- EP-02 requires NumPy, SciPy and RFC 8785/JCS.
- EP-03 requires the existing RFC 8785/JCS lock.
No additional third-party import was found in the inspected allowlisted source/test closure.

The existing dependency lockfiles and their published wheel SHA-256 entries were re-read. This audit did not download or independently re-hash wheel bytes.

## 4. Remaining validation gap — workflow parser/actionlint

**Full workflow YAML/action validation remains OPEN.**

The current local runtime does not contain `actionlint` or `shellcheck`. The repository is not cloned/materialized in this runtime, and GitHub cannot be reached from the local shell to obtain it. Consequently:
- `actionlint` was not run;
- a complete YAML parser pass over the three exact workflow files was not run;
- all embedded Bash and Python blocks have not been independently parsed as complete scripts;
- no GitHub workflow validation or CI run was triggered.

Do not convert the targeted Bash grouping check or structural source review into a global workflow syntax PASS. The corrected workflow contents still require a complete non-executing YAML/action validator pass.

## 5. Runtime and evidence limitations retained

The Gate 204 runtime qualification remains unchanged:
- CPython 3.12.10 is the selected binary-supported patch for the pinned CPython 3.12 wheel profile.
- The later 3.12 security-only source release is not selected by these workflows.
- This is a documented runtime limitation, not a claim that 3.12.10 is the latest security patch.
- PyPI-published wheel hashes remain recorded; independent local wheel-byte hashing has not occurred.
- Hosted runner image labels remain mutable; manifests capture available actual image/OS/libc identity at run time.

No dependency migration or runtime-policy decision is made in Gate 205.

## 6. Repository and PR integrity

At the start of this follow-up audit:
- canonical `main` HEAD: `a8b83f4b3955bcb602f97adf0c4dc716a5123f8d`;
- research branch HEAD before Gate 205 record: `513a724380357739d64afc722b508ce7ec5ec48c`;
- PR #116: OPEN / DRAFT;
- PR base: `research/c10-d1-protocol-draft`;
- PR head: `research/c10-s-consolidation-draft`.

All corrections in this gate were committed only to the research branch. `main` was not modified. The six-file implementation delta recorded by Gate 204 remains the workflow/lockfile implementation set; Gate 205 adds its own audit record. No scientific source, DGP, estimand, seed, statistical criterion, calibration input, package schema, 14-file inventory or 28-component fingerprint was modified.

## 7. Execution boundary

- Workflow dispatch: NOT PERFORMED.
- YAML/actionlint validation: NOT PERFORMED.
- Complete workflow shell validation: NOT PERFORMED.
- Unit tests: NOT PERFORMED.
- Compilation: NOT PERFORMED.
- Monte Carlo: NOT PERFORMED.
- Producer/package writer: NOT PERFORMED.
- Scientific execution: NOT PERFORMED.
- `scientific_execution=false`.
- `execution_authorized=false`.

## 8. Disposition and next operation

**Gate 205: STATIC STRUCTURAL REVIEW PASS WITH CORRECTIONS / TARGETED FIND-ASSERTION BASH SYNTAX PASS / FULL WORKFLOW YAML VALIDATION OPEN / EXECUTION NOT AUTHORIZED.**

The concrete defects found in the three bytecode assertions have been corrected, and EP-03 now retains its raw test logs alongside runtime identity. Profile allowlists and manifest source inventories remain aligned.

**Next operation:** obtain a complete non-executing workflow YAML/action validation for all three exact files (preferably `actionlint`), plus full embedded-shell syntax validation. Resolve every finding, then update the implementation record. Do not dispatch a workflow, run tests, or perform scientific execution as part of that validation.
