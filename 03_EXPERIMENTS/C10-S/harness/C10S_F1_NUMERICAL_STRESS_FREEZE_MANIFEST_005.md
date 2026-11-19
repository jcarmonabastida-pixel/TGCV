# C10-S F1 — Numerical Stress Freeze Manifest 005

**Status:** V003 SOURCE SNAPSHOT FROZEN — EXECUTION NOT AUTHORIZED  
**Research branch:** `research/c10s-f1-integrated-correction-20261119`  
**Frozen source commit:** `e526acb04e1d2c2421fa2663a43e31b537985522`  
**Generator:** `C10S_F1_NUMERICAL_STRESS_GENERATOR_003`  
**Predecessors:** v001/v002 remain immutable; this is a diagnostic successor, not a replacement.

## 1. Freeze boundary

This manifest pins the v003 diagnostic source and frozen N4 input subset. It does not authorize imports, compilation, tests, CLI execution, numerical diagnostics, calibration or scientific C10-S execution.

Any change to source, frozen inputs, runtime, command, scope or workflow after this snapshot requires a new manifest and one-shot authorization.

## 2. Frozen source and input inventory

All blobs below are resolved at source commit `e526acb04e1d2c2421fa2663a43e31b537985522`.

| Role | Path | Git blob SHA |
|---|---|---|
| v003 diagnostic design | `03_EXPERIMENTS/C10-S/harness/C10S_F1_NUMERICAL_STRESS_DESIGN_003.md` | `ee2c6a8e16c63a0cd636e34ab9d63ad7e4e968b3` |
| v003 frozen N4 inputs | `03_EXPERIMENTS/C10-S/harness/C10S_F1_N4_V002_FROZEN_INPUTS_001.json` | `413e96c5478381ac615f3d44dd8a30a41d88513f` |
| v003 generator | `03_EXPERIMENTS/C10-S/harness/c10s_f1_numerical_stress_v3.py` | `fe43d0252f4a56d93b187091680fa16bca21a13d` |
| v003 CLI/evidence writer | `03_EXPERIMENTS/C10-S/harness/run_c10s_f1_numerical_stress_v3.py` | `177838e6fc6baaacca004f0d2179fd50c1ddd7a1` |
| v003 implementation/static review | `03_EXPERIMENTS/C10-S/harness/C10S_F1_NUMERICAL_STRESS_IMPLEMENTATION_003.md` | `0b475553effcd4adcb3124bdf107e2db93a6ad86` |
| v001 fixture generator (read-only) | `03_EXPERIMENTS/C10-S/harness/c10s_f1_numerical_stress.py` | `cc047a3b112caf84533c94e77d1908c99a0c2bdf` |
| v002 diagnostic helpers (read-only) | `03_EXPERIMENTS/C10-S/harness/c10s_f1_numerical_stress_v2.py` | `a4f7a79bf36385cd6174567a4acf3e260d971ac7` |
| exact-rational Sturm isolator (read-only) | `03_EXPERIMENTS/C10-S/harness/c10s_f1_independent_root_isolator.py` | `3ac9ce31eb82421022fd8d2a65a0daee049322be` |

The N4 frozen input subset is derived from v002 artifact `14541730681`, workflow run `44545538187`, using the v002 records JSONL SHA-256:

`b350693e3e8f492ccb179631a703c45a6af45d661b21a033f280c0546fcc9a26`.

It contains the 14 predeclared N4 exponents and their recorded coefficient hex vectors, F1 base-variance candidate and v002 Sturm/adjudication statuses. The v003 runner checks the source commit, run/artifact identifiers, JSONL source hash and exact exponent roster before using these inputs.

## 3. Frozen scope

| Lane | Planned records | Frozen construction |
|---|---:|---|
| N2 discriminant-proximity ULP | 64 | Gaps (2^{-28},2^{-32},2^{-36},2^{-40}), four independent coefficients, four ULP steps |
| N5 coefficient rounding cells | 1 | Existing (N=2^{120}) quadratic, exact binary64 preimage cells and discriminant enclosure |
| N4 Fujiwara bound comparison | 14 | Existing v002 N4 coefficient vectors, exact Cauchy/Fujiwara bounds and explicit Fujiwara-domain isolation |
| **Total** | **79** | Fixed deterministic roster |

No v002 record is regenerated or reclassified. No Monte Carlo, random fixture selection or adaptive exponent insertion is included.

## 4. Runtime and command proposal

- Runner: GitHub-hosted `ubuntu-24.04`.
- Python: CPython `3.12.3`.
- External Python dependencies: none; standard library only.
- Working directory: `03_EXPERIMENTS/C10-S/harness`.
- One primary execution; zero retries; no replay.
- Timeout: 15 minutes.
- Proposed command:

```bash
python run_c10s_f1_numerical_stress_v3.py \
  --source-commit e526acb04e1d2c2421fa2663a43e31b537985522 \
  --output-directory "$RUNNER_TEMP/c10s-f1-numerical-stress-v3-evidence"
```

Expected outputs:
- `numerical_stress_v3_records.jsonl`;
- `numerical_stress_v3_summary.json`;
- `numerical_stress_v3_manifest.json`;
- workflow preflight/provenance;
- complete stdout/stderr and runner exit code.

The CLI must fail closed unless lane counts are exactly 64 + 1 + 14 = 79. It hashes the generator, CLI, frozen N4 input, and all transitive numerical source modules.

## 5. Prohibitions

- no unit-test suite;
- no bytecode compilation or compile check;
- no Monte Carlo calibration;
- no DGP experiment or inferential coverage study;
- no parameter tuning or post-outcome changes;
- no external dataset;
- no modification of frozen v001/v002 sources;
- no source modification during execution;
- no scientific C10-S execution or causal/value claim;
- no replay or automatic retry.

## 6. Gate state

| Gate | State |
|---|---|
| v003 design | DEFINED |
| v003 implementation | IMPLEMENTED |
| source-level review | CONDITIONAL — NOT EXECUTED |
| N4 frozen input provenance | RECORDED |
| source snapshot | FROZEN at commit above |
| workflow v003 | PENDING |
| authorization v003 | PENDING |
| numerical execution | NOT AUTHORIZED |
| Monte Carlo calibration | NOT AUTHORIZED |
| scientific C10-S execution | NOT AUTHORIZED |

**Execution boundary:** the snapshot is frozen for review and possible future execution only. A dedicated workflow and one-shot authorization must pin this manifest's exact blob and workflow blob. Fresh explicit user approval is required before any numerical execution.
