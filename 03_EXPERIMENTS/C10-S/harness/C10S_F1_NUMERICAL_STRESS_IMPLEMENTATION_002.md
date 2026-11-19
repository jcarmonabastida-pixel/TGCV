# C10-S F1 — Numerical stress v002 implementation record

**Status:** IMPLEMENTED — SOURCE-LEVEL STATIC REVIEW RECORDED — NOT EXECUTED — NOT FROZEN  
**Research branch:** `research/c10s-f1-integrated-correction-20261119`  
**Implementation snapshot:** `be13fe1a227517d0d7fe48ec26315caa8a09dc1d`  
**Design:** `C10S_F1_NUMERICAL_STRESS_DESIGN_002.md`  
**Design review:** `C10S_F1_NUMERICAL_STRESS_DESIGN_REVIEW_001.md`

## 1. Implemented files

| Role | Path | Git blob |
|---|---|---|
| v002 stress orchestration and deterministic lanes | `03_EXPERIMENTS/C10-S/harness/c10s_f1_numerical_stress_v2.py` | `a4f7a79bf36385cd6174567a4acf3e260d971ac7` |
| v002 CLI and evidence writer | `03_EXPERIMENTS/C10-S/harness/run_c10s_f1_numerical_stress_v2.py` | `c184861614437aeb07da6fa568ebac9a6fad71ac` |
| v002 design | `03_EXPERIMENTS/C10-S/harness/C10S_F1_NUMERICAL_STRESS_DESIGN_002.md` | `119467917d974471486e2d29f0b2e583948de889` |

## 2. Implemented design increments

- Reuses the historical v001 115-record polynomial/Sturm grid without modifying its generator or CLI.
- Adds 16 near-double ULP perturbation records using exact-rational roots `(1, 1 + 2^-24, -2)`.
- For each polynomial record, isolates the ideal exact-rational polynomial and the exact rationalization of the actual binary64 coefficient vector on the same domain/width/depth. Records `PRESERVED`, `CHANGED` or `UNRESOLVED` independently of represented-polynomial solver status.
- Adds a seven-record N3 covariant variable-scale lane. Domain endpoints and requested interval width transform by (2^k); intervals are inverse-mapped exactly and compared with the base represented-polynomial isolators.
- Retains the historical N3 fixed-absolute lane in the 131 polynomial records.
- Adds the fixed 14-scale N4 observation ladder `{-100,-50,-20,0,20,24,28,32,36,40,44,48,50,100}`.
- Records F1 profile status, MLE/LR endpoint errors, score-polynomial degree/coefficients/roots, exact-rational Sturm intervals, boundary roots, root counts, matched counts, multiplicity review, adjudication and fixed-grid transition brackets.
- Requires a resolved N4 baseline before any scale record can be classified as PASS.
- The CLI enforces the predeclared denominators: 131 polynomial/Sturm + 7 N3 covariant + 14 N4 = 152 records.
- Writes canonical JSONL, summary and manifest with source SHA-256 inventory and runtime versions.

## 3. Source-level static review

Reviewed the v002 module and CLI directly from GitHub. The following issues identified during source inspection were corrected before this record:
- the v1 fixture roster does not contain the unscaled N3 base fixture; v002 now constructs that exact base fixture explicitly;
- exact rational width parsing uses the single-string `Fraction` form;
- added near-double records are included in the full polynomial/Sturm status denominators;
- N3 representation loss is explicitly counted as base-equivariance UNRESOLVED;
- N4 transition brackets do not bridge over fail-closed records;
- N4 PASS requires a resolved baseline and checks profile status, score degree/root count/location, Sturm status/intervals, adjudication counts, multiplicity review and boundary roots;
- CLI refuses to write evidence if the 131/7/14 record denominator changes.

This is a source-level review only. No Python import, bytecode compilation, unit test, CLI invocation, numerical runner, calibration or scientific experiment has been executed. Therefore syntax/runtime behavior, actual record counts and numerical outcomes remain unverified. No PASS is claimed for v002.

## 4. Frozen v001 assets confirmed unchanged

| Asset | Git blob |
|---|---|
| v001 generator | `cc047a3b112caf84533c94e77d1908c99a0c2bdf` |
| v001 CLI | `b08ee28a1423b7a6c598db69c0ef15dff5f0ac22` |
| independent exact-rational Sturm isolator | `3ac9ce31eb82421022fd8d2a65a0daee049322be` |
| F1 profile/score implementation | `39f1732e1571f9d0705378d924b58b9475277e7a` |
| F1/Sturm adjudicator | `9fa1cb21cd47e32030db8a00420e7dacfdc77321` |
| observed-data interface | `6d193798e792dd5129fbfb0c312286763791d463` |
| v001 result record | `2eb24f5b050f8c40194365dc41e7ac9f45cd3c6d` |
| authorization 003 | `b37a18b8cf774d6528ba48cab3c731299656585d` |

The v001 122-record result remains the only executed adversarial stress evidence. Authorization 003 remains consumed and closed. No authorization from v001 is reusable.

## 5. Gate status and next operation

| Gate | State |
|---|---|
| v001 execution and result | EXECUTED — MIXED |
| v002 design | DEFINED |
| v002 implementation | IMPLEMENTED |
| v002 source-level static review | COMPLETED WITH LIMITATION |
| v002 import/compile/unit tests | NOT RUN |
| v002 numerical execution | NOT RUN |
| v002 source freeze | PENDING |
| v002 workflow | PENDING |
| v002 one-shot authorization | PENDING |
| scientific C10-S / Monte Carlo | NOT AUTHORIZED |

**Next operation:** create a new source freeze manifest and dedicated workflow/authorization for v002. Before any primary execution, obtain fresh explicit approval. The v002 CLI must not be invoked before that authorization.
