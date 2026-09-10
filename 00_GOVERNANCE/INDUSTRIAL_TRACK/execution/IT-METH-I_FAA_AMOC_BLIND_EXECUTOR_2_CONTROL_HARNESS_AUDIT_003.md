# IT-METH-I — FAA AMOC Blind Executor-2 Control Harness Audit 003

**Status:** `AUDIT COMPLETE — FAIL / REPAIR REQUIRED`

**Audited artifact:** `it_meth_i_faa_amoc_blind_executor_2_control_v01.py` v0.3, commit `c97db202d3a201125831bc769f15c166780327d6`

## Audit basis

Compared against:
- `IT-METH-I_FAA_AMOC_BLIND_EXECUTOR_2_SPEC_v0.1.md`
- `IT-METH-I_FAA_AMOC_BLIND_EXECUTOR_2_CONTROL_RECORD_001.md`
- Audit 001
- Audit 002

## Findings

### A3-1 — Critical: package manifest still self-derived

The harness computes `PACKAGE_MANIFEST_ENTRY` from the package file itself. This is useful provenance metadata but is not an independently supplied frozen declaration. The actual package integrity remains externally anchored by `--expected-package-sha256`, so H1 is repaired; however, the manifest should not be presented as an independent frozen manifest.

**Disposition:** minor semantic repair required: classify it explicitly as observed package metadata.

### A3-2 — Critical: evidence manifest does not itself prove information isolation

The externally supplied manifest is now genuinely external and its hashes are checked. This repairs the prior tautology. However, P1 still infers `RECONSTRUCTION_001_ACCESS_STATUS=PASS` from manifest validity plus absence of symlinks. A valid manifest establishes provenance of declared files; it cannot establish that the runtime has no access to other filesystem locations.

**Required repair:** rename/partition the control. Evidence-boundary integrity may PASS; actual access isolation must be either an independently enforced sandbox/container policy or explicitly `NOT_VERIFIED`. Do not conflate declared-input integrity with runtime access isolation.

### A3-3 — High: symlink control is not a complete filesystem isolation mechanism

`symlink_paths()` rejects symlinks under the evidence root, but the process can still read arbitrary paths because ordinary Python filesystem access is not sandboxed. The harness therefore cannot technically demonstrate “only declared roots readable”.

**Required repair:** for a defensible technical PASS, use an externally enforced execution boundary (e.g. OS/container sandbox) or change the claim to `DECLARED_INPUT_BOUNDARY_VERIFIED`, with runtime isolation remaining `NOT_VERIFIED`.

### A3-4 — High: comparison verification scans only configuration and manifest paths

This is better than the v0.2 self-assertion, but it does not prove that comparison material is absent from file contents, environment variables, current working directory, process arguments beyond the configured parser values, or other accessible locations.

**Required repair:** scope P9 narrowly to “no comparison target declared in controlled inputs” and do not call it “comparison absence” globally. Global absence requires external isolation evidence.

### A3-5 — Medium: output boundary is checked before output creation, but the seal probe itself creates the directory

The output root is checked for disjointness before creation, which is correct. The harness should additionally reject an existing symlink output path before `mkdir`, and should verify that the resolved output directory remains the same after creation.

**Required repair:** explicit output-root symlink/reparse-point rejection and post-creation path identity check.

### A3-6 — Medium: temporal sequence is technically observable but not yet a seal sequence

The ordering of `control_start`, `preseal_check`, and `seal_capability_probe_complete` is genuinely derived from timestamps. This repairs the hardcoded P7 problem. It should nevertheless be named `CONTROL_SEQUENCE_STATUS`; it cannot demonstrate the temporal ordering of a future reconstruction seal.

**Disposition:** semantic rename only.

### A3-7 — Low: dependency inventory remains correctly classified

The dependency inventory is now explicitly observational host metadata and is not part of the technical PASS vector. This finding is CLOSED.

## Finding closure matrix

| Prior finding | v0.3 disposition |
|---|---|
| H1 package hash mandatory | CLOSED |
| H2 filename-only P1 | SUBSTANTIVELY REPAIRED, but runtime isolation claim remains too broad |
| H3 output overlap | CLOSED subject to A3-5 hardening |
| H4 seal semantics | CLOSED |
| H5 hardcoded P7 | CLOSED subject to A3-6 naming |
| H6 hardcoded P9 | SUBSTANTIVELY REPAIRED, scope still too broad |
| H7 package-parent manifest | CLOSED |
| H8 dependency inventory | CLOSED |

## Gate decision

`HARNESS_AUDIT_003 = FAIL — REPAIR REQUIRED`

`DRY_RUN_EXECUTION = BLOCKED`

`RECONSTRUCTION_002 = NOT EXECUTED`

`EXECUTOR_2 = NOT ESTABLISHED`

`INDEPENDENCE_STATUS = NOT DEMONSTRATED`

`NEXT_GATE = v0.4 REPAIR + FINAL STATIC AUDIT`

No scientific, industrial utility, causal/value, or Core claim is changed by this audit.
