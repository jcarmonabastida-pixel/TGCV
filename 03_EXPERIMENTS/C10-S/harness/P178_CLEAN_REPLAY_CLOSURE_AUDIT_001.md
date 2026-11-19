# C10-S — P178 Analyzer Monte Carlo: clean replay closure audit 001

**Status:** CLOSED — COMPUTATIONAL REPRODUCIBILITY PASS / NON-CONFIRMATORY METHODOLOGICAL CALIBRATION  
**Primary run:** 43083651875  
**Clean replay run:** 43120303588  
**Primary source commit:** `689c8f0164e0625ca536a20b1805e555cd63d5fd`  
**Replay workflow commit:** `fc0839f53d3d09ae2764909bbf13a6ef896042a1`  
**Protocol:** `TGCV-C10-S-P178-ANALYZER-MC-001`

## 1. Scope

This audit closes the previously incomplete clean replay of the authorized, non-confirmatory P178 Analyzer Monte Carlo benchmark. It uses the exact primary-execution source commit and the existing primary artifact. No Analyzer code, DGP, grid, seed rule, dependency pin, estimator, acceptance criterion or scientific interpretation was changed.

The replay covers the same 27 cells (K = 2, 10, 50 × π0 = 0.2, 0.5, 0.8 × null/positive/negative), N = 700 balanced 350/350, R = 10,000 per cell: 270,000 Analyzer invocations.

## 2. Workflow and provenance

- GitHub Actions run: [43120303588](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/43120303588)
- Conclusion: `success`; job completed 2026-11-11 23:53:42 UTC.
- Job interval: 23:30:17–23:53:42 UTC; elapsed 23 min 25 s.
- Checkout: exact primary source commit `689c8f0164e0625ca536a20b1805e555cd63d5fd`.
- Pinned dependencies: Python 3.12.16, NumPy 2.3.5, SciPy 1.17.0.
- Contract tests: 17/17 PASS.
- Primary artifact integrity: PASS; downloaded primary artifact digest matched the declared SHA-256 `0218ac9303e588f8d134f43bd73627d51ec59f4281ecac02621a3f20726b288e`.
- Replay: all 27 cells completed; all 27 reference comparisons reported `reference_match=True`; 270,000 Analyzer invocations; stderr empty.
- Workflow steps 1–12 all succeeded, including clean-source archive construction, full replay, byte-level comparison, provenance recording and artifact upload.

## 3. Exact comparison

| File | Primary SHA-256 | Replay SHA-256 | Result |
|---|---|---|---|
| `p178_analyzer_monte_carlo.csv` | `e73a204b6ffc3ff4666c37d9a3e2d5ff4612a3d0602a25349cbb8bc12287914f` | `e73a204b6ffc3ff4666c37d9a3e2d5ff4612a3d0602a25349cbb8bc12287914f` | BYTE-IDENTICAL |
| `p178_analyzer_monte_carlo_manifest.json` | `72aed4c8bbe30a20cdb20e3b1c2d27f38e046687b100349f94b99aaed9f04294` | `72aed4c8bbe30a20cdb20e3b1c2d27f38e046687b100349f94b99aaed9f04294` | BYTE-IDENTICAL |

The workflow emitted `CLEAN_REPLAY_BYTE_IDENTICAL=PASS`. The replay artifact ZIP SHA-256 is `a72922ca51dc5afb713edcb35932dc1598d535f77abe9af6aaa8f3ed1b83e4de`; artifact ID `13901876197`, name `c10s-p178-analyzer-clean-replay-43083651875-43120303588-1`.

## 4. Acceptance result

The replay manifest preserves the primary acceptance status `PASS` and all registered criteria:

- 27 cells present and 10,000 replications per cell;
- reference metrics match within 1e-9;
- coverage deviation and Wilson-compatibility criteria pass;
- null rejection calibration and non-null power lower-bound criteria pass;
- bias/RMSE Monte Carlo error criteria pass;
- zero invalid replicates, zero classification errors and zero focal abstentions.

These are the frozen benchmark's acceptance criteria, not a new analysis or post-hoc recalibration.

## 5. Disposition

**P178 Analyzer Monte Carlo: COMPUTATIONAL REPRODUCIBILITY CLOSED — PASS.**

The exact clean replay reproduces both primary output files byte-for-byte. The prior incomplete replay attempts are superseded for closure purposes by this complete successful replay; their history is retained.

The result supports reproducibility of this bounded 27-cell methodological benchmark. It does not establish general Analyzer validity outside the evaluated grid, validate abstention under non-identification, cover direct paths/positivity failure/weak signals/degraded measurement/interference, establish confirmatory feasibility, or support the general TGCV causal/value claim.

No production Analyzer change is justified by this replay. The exact Student-t cache probe remains NO-GO; no performance optimization is adopted.

## 6. Governance boundary

This is a research-branch execution audit only. It does not modify `main`, RMA, Evidence→Claim Matrix, STATUS, TGCV Core, claims, or accepted scientific decisions. It does not authorize Design Freeze, confirmatory fixtures, new DGP cells, simulation expansion or further scientific execution.

**Next scientific work remains design/reconciliation of the material C10-S blockers.** P178 closure does not lift G-SCI/G-MAT/G-SCHEMA/G-ROLE/G-TEST/G-REPRO or G-AUTH blocks.
