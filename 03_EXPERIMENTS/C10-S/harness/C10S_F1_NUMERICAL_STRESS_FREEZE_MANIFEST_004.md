# C10-S F1 — Numerical Stress Freeze Manifest 004

**Status:** V002 SOURCE SNAPSHOT FROZEN — EXECUTION NOT AUTHORIZED  
**Research branch:** `research/c10s-f1-integrated-correction-20261119`  
**Frozen source commit:** `a42351e374e3624a498b11199cea45cd0dc20c09`  
**Supersedes:** Freeze Manifest 003 for future v002 work only; manifest 003 and result 001 remain immutable  
**Generator:** `C10S_F1_NUMERICAL_STRESS_GENERATOR_002`

## 1. Freeze boundary

This manifest pins the v002 source snapshot and its exact Git blob identities. It does not authorize imports, tests, compilation, numerical runners, calibration or scientific C10-S execution.

The v001 source, CLI, execution result, artifact and authorization 003 remain unchanged. V002 is a separate successor implementation.

Any source, fixture, parameter, command, runtime or workflow change after this freeze requires a new manifest and one-shot authorization.

## 2. Frozen v002 roster and command

Predeclared records:
- 131 polynomial/Sturm records: v001 115-record roster plus 16 near-double ULP perturbations;
- 7 N3 covariant variable-scale records;
- 14 N4 observation-scale records at exponents `{-100,-50,-20,0,20,24,28,32,36,40,44,48,50,100}`;
- total 152 records.

N3 fixed-absolute lane remains embedded in the 131 polynomial/Sturm records and is not pooled with the 7-record N3 covariant lane.

Working directory: `03_EXPERIMENTS/C10-S/harness`

Exact command:
```bash
python run_c10s_f1_numerical_stress_v2.py \
  --source-commit a42351e374e3624a498b11199cea45cd0dc20c09 \
  --output-directory "$RUNNER_TEMP/c10s-f1-numerical-stress-v2-evidence"
```

## 3. Frozen Git blob inventory

| Role | Path | Git blob SHA |
|---|---|---|
| v002 deterministic runners and diagnostics | `03_EXPERIMENTS/C10-S/harness/c10s_f1_numerical_stress_v2.py` | `a4f7a79bf36385cd6174567a4acf3e260d971ac7` |
| v002 CLI and evidence writer | `03_EXPERIMENTS/C10-S/harness/run_c10s_f1_numerical_stress_v2.py` | `c184861614437aeb07da6fa568ebac9a6fad71ac` |
| v002 design | `03_EXPERIMENTS/C10-S/harness/C10S_F1_NUMERICAL_STRESS_DESIGN_002.md` | `119467917d974471486e2d29f0b2e583948de889` |
| v002 implementation/static-review record | `03_EXPERIMENTS/C10-S/harness/C10S_F1_NUMERICAL_STRESS_IMPLEMENTATION_002.md` | `a5dbfb46ed1905564bdb5397b85ca321581c8df7` |
| v001 fixture generator reused read-only | `03_EXPERIMENTS/C10-S/harness/c10s_f1_numerical_stress.py` | `cc047a3b112caf84533c94e77d1908c99a0c2bdf` |
| F1 score/profile implementation | `03_EXPERIMENTS/C10-S/harness/c10s_f1_between_profile_likelihood.py` | `39f1732e1571f9d0705378d924b58b9475277e7a` |
| exact-rational Sturm isolator | `03_EXPERIMENTS/C10-S/harness/c10s_f1_independent_root_isolator.py` | `3ac9ce31eb82421022fd8d2a65a0daee049322be` |
| F1/Sturm adjudicator | `03_EXPERIMENTS/C10-S/harness/c10s_f1_root_adjudication.py` | `9fa1cb21cd47e32030db8a00420e7dacfdc77321` |
| observed-data interface | `03_EXPERIMENTS/C10-S/harness/c10s_variance_comparison_interface.py` | `6d193798e792dd5129fbfb0c312286763791d463` |

The implementation record blob is pinned above. The workflow and authorization blobs are separate governance artifacts and are pinned by the authorization. Workflow and authorization blobs are separate governance artifacts and are pinned by the authorization.

## 4. Runtime

- GitHub-hosted `ubuntu-24.04`;
- CPython `3.12.3`;
- NumPy `2.1.3`;
- SciPy `1.14.1`;
- isolated virtual environment;
- pinned binary wheels installed with `--no-deps`;
- 15-minute job timeout.

## 5. Evidence outputs

- `numerical_stress_v2_records.jsonl`;
- `numerical_stress_v2_summary.json`;
- `numerical_stress_v2_manifest.json`;
- workflow preflight/provenance;
- complete runner stdout/stderr and exit code;
- GitHub run and artifact identity/digest.

The CLI must fail closed unless its generated lane counts are exactly 131 + 7 + 14 = 152. The evidence manifest records SHA-256 values for the v002 runner, CLI and transitive numerical source modules, plus runtime versions and canonical records/summary hashes.

## 6. Limits and prohibitions

- one primary execution;
- zero automatic retries;
- no replay;
- no unit-test suite or bytecode/compile check under this authorization;
- no Monte Carlo calibration;
- no DGP experiment or inferential coverage study;
- no parameter tuning or adaptive post-outcome fixture changes;
- no external dataset;
- no source modification during the run;
- no scientific C10-S execution and no causal/value claim.

## 7. Gate state

| Gate | State |
|---|---|
| v001 adversarial run | EXECUTED — 122 records, mixed result |
| v002 design | DEFINED |
| v002 implementation | IMPLEMENTED |
| source-level review | RECORDED; no import/compile/tests |
| v002 snapshot | FROZEN at source commit above |
| workflow v2 | PENDING |
| authorization v2 | PENDING |
| numerical execution | NOT AUTHORIZED |

**Execution boundary:** this manifest freezes the v002 source only. A separate workflow and one-shot authorization must pin this manifest's exact Git blob and workflow blob. Fresh explicit user approval is required before execution.
