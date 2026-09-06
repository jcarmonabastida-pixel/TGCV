# DR-027 — EXT-1.1 Rust Confirmatory Execution Authorization v0.2

**Status:** ACCEPTED — CONFIRMATORY EXECUTION AUTHORIZED  
**Acceptance date:** 2026-09-07  
**Scope:** Sole authorization gate for confirmatory execution of EXT-1.1 Rust  
**Depends on:** DR-023, DR-024, DR-025A, DR-026A, DR-026C, DR-026D

## Decision

DR-027 is accepted following the dedicated structural audit v0.2 with `DR027_STRUCTURAL_AUDIT_PASS: True`.

The acceptance authorizes execution of the already frozen EXT-1.1 Rust confirmatory protocol exactly as specified by DR-023 through DR-026D. It authorizes no methodological modification, exploratory comparison, post-hoc optimization, or inferential procedure not separately frozen ex ante.

## Acceptance evidence

The pre-authorization structural audit was executed against the local frozen environment and returned:

- dataset SHA-256 matched: `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`;
- Python 3.14.7;
- scikit-learn 1.9.0;
- NumPy 2.5.2;
- SciPy 1.18.1;
- `random_state=0`;
- hash dimension `2^20`;
- solver `liblinear`, `C=1.0`, `tol=1e-8`, `max_iter=1000`;
- all prerequisite decisions present;
- normative resolver present and exact SHA matched;
- confirmatory runner present and exact SHA matched;
- runner commit present in current Git history;
- Git worktree clean;
- all prohibited pre-authorization computations false.

Audit execution HEAD: `105c642e8766e3cef0beb1a1422f2dea9721207d`.

Audit script blob SHA: `afa0774caa0e86780df8c1f8604d140449adc214`.

## Frozen execution identities

### Dataset

`rust_repos_2022_09_07.zip`  
SHA-256: `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`  
Size: `6,047,715,996` bytes

### Runtime

- Python 3.14.7 CPython
- Windows 11 `10.0.26200-SP0`
- AMD64
- scikit-learn 1.9.0
- NumPy 2.5.2
- SciPy 1.18.1
- `random_state=0`

### Normative resolver

Path: `03_EXPERIMENTS/EXT-1.1_Rust/src/rstar_v02.py`  
SHA-256/blob identity: `669d4f01131af518f32b1b4b3da27f676ae4ae55`

### Confirmatory runner

Path: `03_EXPERIMENTS/EXT-1.1_Rust/src/run_ext11_confirmatory_v01.py`  
SHA-256/blob identity: `dbf4aa11aee9848e5c6466e63bd8fb772cfe772c`  
Introducing commit: `e24f6365fd942053704026ecfa4861fc05c469bf`

The runner imports the normative resolver rather than reimplementing R* semantics.

## Authorized execution sequence

1. **Primary:** execute `run_ext11_confirmatory_v01.py --mode primary`.
2. Preserve the primary execution evidence without outcome-based alteration.
3. **Replay:** execute the identical runner with `--mode replay`.
4. Compare primary and replay under the reproducibility requirements of DR-027.
5. If replay disagrees beyond the frozen numerical tolerance or any hard-stop condition occurs, mark the confirmatory result invalid pending investigation under a new ex-ante gate.

The primary result must not be selected, modified, or interpreted preferentially on the basis of the replay.

## Frozen scientific protocol

The execution must use, without modification:

- DR-024 eligible population and census-first rule;
- DR-023 `Y_180` and 180-day horizon;
- DR-025A baseline `B_num`;
- DR-020/DR-021/DR-022 candidate, resolver and resource semantics;
- DR-026A `TAcc_repr=(A_rel,A_count)`;
- DR-026C BLAKE2b-256 tokenization, `2^20` hashing, numeric `log1p` plus training-only standardization, chronological 80/20 elapsed-time split, and logistic regression;
- DR-026D deterministic runtime and `random_state=0`.

Primary metric:

`ΔLogLoss = LogLoss(B) − LogLoss(T_acc)`

Positive values favor `T_acc`.

No package-aware p-value, confidence interval, or other inferential claim is authorized by DR-027.

## Hard stops

Any mismatch in dataset, runtime, normative resolver, runner identity, accepted protocol, population, outcome construction, temporal split, preprocessing, learner, or reproducibility invalidates execution under this gate.

Any adaptive methodological choice after outcome construction is prohibited.

## Acceptance boundary

This acceptance authorizes one primary confirmatory execution followed by one identical reproducibility replay. It does not authorize a third exploratory run, alternate seed, alternate model, alternate horizon, alternate baseline, alternate T_acc representation, post-hoc feature selection, or unapproved inferential analysis.

**DR-027 ACCEPTED. CONFIRMATORY EXECUTION IS NOW AUTHORIZED.**
