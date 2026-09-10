# IT-METH-I — FAA AMOC Blind Executor-2 Control Harness Audit 002

**Status:** `AUDIT COMPLETE — REPAIR REQUIRED BEFORE DRY-RUN`

**Audited artifact:** `it_meth_i_faa_amoc_blind_executor_2_control_v01.py` at repair commit `e6817600a2ba081b2b86a58a993bc2a801a9adee`  
**Reference:** `IT-METH-I_FAA_AMOC_BLIND_EXECUTOR_2_SPEC_v0.1.md` and Audit 001

## 1. Overall result

The v0.2 repair addresses several Audit-001 findings, especially mandatory package hashing, output-root handling, real seal probing, and environment inventory. However, the harness still contains control assertions that are not sufficiently grounded in observable facts for a governance-quality dry-run.

Therefore the dry-run remains blocked.

## 2. Findings

### H1 — P3 declared-input boundary remains incomplete

`DECLARED_INPUTS` records package and evidence roots, but `INPUT_BOUNDARY_STATUS` only checks that those paths exist and that no detected symlink escapes exist. It does not establish that the process is unable to read undeclared paths, nor does it verify a closed allowlist of files actually consumed.

**Required repair:** define an explicit allowlist/manifest boundary and make the harness reject any configured input outside that allowlist. The dry-run should operate only on declared package/evidence paths and report the exact allowed roots/files.

### H2 — P1 still relies partly on filename heuristics

The harness now adds symlink checks, but `RECONSTRUCTION_001_ACCESS_STATUS` remains a combination of forbidden filename detection and symlink detection. A forbidden artifact with a neutral filename remains undetectable.

**Required repair:** make boundary isolation the primary P1 control. Filename scanning may remain supplementary. The harness must not imply that absence of forbidden names proves absence of reconstruction-001 information.

### H3 — Output boundary is too permissive

`OUTPUT_BOUNDARY_STATUS` rejects only equality with `package.parent` or `evidence`. An output directory nested inside the package parent can therefore pass even though the package parent is scanned as a broader tree and may contain other governance/control material.

**Required repair:** require the output root to be disjoint from every input root and from their descendants/ancestors, except for the explicitly designated output root itself.

### H4 — P6 seal is still only a temporary hash probe

The probe demonstrates hashing capability, but it does not exercise sealing of the actual execution artifact. That is acceptable only if the result is explicitly labelled `SEAL_MECHANISM_CAPABILITY`, not `SEAL_STATUS`.

**Required repair:** rename the field semantics to capability and keep actual artifact sealing as a later execution-stage operation. Do not represent capability as completed sealing.

### H5 — P7 remains hardcoded

`TEMPORAL_ORDERING_STATUS` is still assigned `PASS` based on a constant `PRESEAL_CONTROL_RECORDED=True`. This is not an independent observation of the required temporal sequence.

**Required repair:** record explicit control events (`control_start`, `preseal_check`, and, when applicable, `seal`) and derive temporal status from their ordering. In pure dry-run, the result should be `TECHNICAL_SEQUENCE_VERIFIED`, not a claim about an actual reconstruction seal.

### H6 — P9 is configuration-derived rather than environment-derived

`COMPARISON_TARGET_CONFIGURED=False` is set by the harness itself and then converted into `COMPARISON_PRESEAL_STATUS=PASS`. This verifies only the harness's own configuration.

**Required repair:** verify that no comparison target, comparison result, or reconstruction-001 reference is present in the declared input manifest/configuration. If this cannot be independently established, return `NOT_VERIFIED` and block.

### H7 — Manifest scope includes package parent rather than exact package artifact

`INPUT_MANIFEST["package"]` hashes every file in `package.parent`, not just the frozen package. This weakens provenance because unrelated sibling files become part of the declared package evidence without explicit authorization.

**Required repair:** manifest the exact package file separately and the exact evidence root separately. Do not silently broaden the frozen package boundary to its containing directory.

### H8 — Python dependency inventory is non-deterministically broad

The full installed-distribution inventory depends on the host environment and can contain unrelated packages. This is useful as an environment observation but should not be treated as a reproducibility fingerprint unless normalized and explicitly classified as host metadata.

**Required repair:** classify it as observational environment metadata and include a stable runtime identifier; do not use it as a pass/fail criterion.

## 3. Safety conclusion

No reconstruction has been executed and no independence claim has been made. Nevertheless, a governance-quality dry-run should not return PASS from controls that are partly self-asserted or based on filename heuristics.

## 4. Gate decision

`HARNESS_AUDIT = FAIL — REPAIR REQUIRED`

`DRY_RUN_EXECUTION = BLOCKED`

`RECONSTRUCTION_002 = NOT EXECUTED`

`EXECUTOR_2 = NOT ESTABLISHED`

`INDEPENDENCE_STATUS = NOT DEMONSTRATED`

`NEXT_GATE = REPAIRED_HARNESS_STATIC_AUDIT_003`
