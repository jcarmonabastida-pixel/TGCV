# IT-METH-I — FAA AMOC Blind Executor-2 Control Harness Audit 008

**Status:** `AUDIT COMPLETE — PASS FOR DRY-RUN CONTROL ONLY`

**Audited harness:** `it_meth_i_faa_amoc_blind_executor_2_control_v01.py`

**Audited harness commit:** `622bc6d0c797c7812556617656418a7ac8904806`

**Audited harness version:** `v0.7`

## 1. Trigger for repair

Technical DRY_RUN_CONTROL on repository commit `759d3956073027bc15ae87b9507c761fa552ee49` returned `BLOCKED` because:

1. the local Windows checkout produced a different byte-level Git-blob calculation for the package (`9bcfd952...`) than the canonical repository blob (`722e9150...`); and
2. the documentary manifest contained an invalid 41-character `git_blob_sha` for the G2 record.

The observed discrepancy is consistent with checkout-level line-ending normalization and therefore must not be interpreted as corruption of the canonical GitHub record.

## 2. Repair assessed

v0.7 changes repository-integrity verification from hashing the normalized working-tree bytes to resolving the canonical Git blob object stored at `HEAD:<repo_path>` through Git.

The package and each manifest entry are therefore checked against the repository object actually identified by the frozen GitHub path and SHA, independently of local checkout line endings.

The local SHA-256 and local byte-level Git-blob calculation remain observational metadata only unless an explicit SHA-256 is supplied in the manifest.

The G2 manifest anchor was corrected to a valid 40-character Git blob SHA field.

## 3. Audit findings

| Control | Result |
|---|---|
| Canonical package Git blob anchor retained | PASS |
| Checkout line-ending normalization handled without false integrity failure | PASS |
| Package path resolved relative to repository root | PASS |
| Canonical `HEAD:<path>` blob verification implemented | PASS |
| Manifest Git blob format validation | PASS |
| G2 manifest schema defect repaired | PASS |
| Evidence paths constrained to repository/evidence roots | PASS |
| Symlink rejection retained | PASS |
| Runtime filesystem isolation claim | NOT VERIFIED — correctly retained |
| Reconstruction-001 access claim | NOT VERIFIED — correctly retained |
| Output boundary | PASS |
| Seal capability probe | PASS |
| Control sequence / temporal ordering | PASS |
| Pre-seal comparison control | PASS |
| EXECUTION mode hard block | PASS |
| Governance non-promotion | PASS |

## 4. Boundary

This audit authorizes only the next technical `DRY_RUN_CONTROL`.

It does **not**:

- authorize reconstruction 002;
- establish EXECUTOR-2;
- establish independent execution;
- establish runtime filesystem isolation;
- establish industrial utility;
- establish causal or value claims;
- modify the TGCV Core;
- upgrade any scientific or industrial claim.

## 5. Gate decision

`HARNESS_AUDIT_008 = PASS`

`DRY_RUN_CONTROL = PERMITTED`

`RECONSTRUCTION_002 = BLOCKED`

`EXECUTOR_2 = NOT ESTABLISHED`

`INDEPENDENCE_STATUS = NOT DEMONSTRATED`

`GOVERNANCE_AUTHORIZATION_STATUS = NOT AUTHORIZED`

## 6. Next operation

Synchronize the local checkout to the exact audited commit and rerun the existing one-shot launcher in `DRY_RUN_CONTROL` mode. No other operation is admitted at this gate.
