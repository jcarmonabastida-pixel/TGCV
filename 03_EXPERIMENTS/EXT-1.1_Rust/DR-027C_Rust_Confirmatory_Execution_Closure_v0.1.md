# DR-027C — EXT-1.1 Rust Confirmatory Execution Closure v0.1

**Status:** CLOSED — PRIMARY/REPLAY VERIFIED  
**Closure date:** 2026-09-07  
**Scope:** Formal closure of the DR-027 confirmatory execution sequence  
**Governing decisions:** DR-023, DR-024, DR-025A, DR-026A, DR-026C, DR-026D, DR-027, DR-027A, DR-027B

## 1. Closure decision

The EXT-1.1 Rust confirmatory execution authorized by DR-027 is formally closed.

The authorized sequence was completed as:

1. primary confirmatory execution;
2. preservation of primary evidence;
3. replay confirmatory execution;
4. structural Primary/Replay identity verification.

The Primary/Replay verifier v0.2 returned:

`DR027_PRIMARY_REPLAY_IDENTITY_PASS: True`

`DR027_PRIMARY_REPLAY_IDENTITY_STATUS: VERIFIED`

No additional confirmatory execution is authorized under DR-027.

## 2. Primary/Replay identity criterion

Literal manifest identity is not the governing reproducibility criterion because execution-instance metadata may legitimately differ between the two runs.

The accepted criterion is **protocol identity plus exact critical-result identity**.

The verifier established:

- `RESULTS_IDENTITY: True`;
- `PROTOCOL_MANIFEST_IDENTITY: True`;
- `DATASET_IDENTITY: True`;
- `RUNTIME_IDENTITY: True`;
- `RESOLVER_IDENTITY: True`;
- `MODEL_IDENTITY: True`;
- `SPLIT_IDENTITY: True`;
- `METRIC_IDENTITY: True`;
- `INFERENCE_PROHIBITION_IDENTITY: True`;
- `CRITICAL_RESULTS_EXACTLY_EQUAL: True`;
- `RUNNER_DIFFERENCE_EXPLAINED: True`;
- `GIT_HEAD_DIFFERENCE_ALLOWED_AS_EXECUTION_METADATA: True`;
- `PROHIBITED_POST_HOC_ACTIONS_FALSE: True`.

## 3. Execution-instance differences

The following differences are preserved as execution metadata and are not treated as scientific protocol differences:

- Primary Git HEAD: `16511d9366003d9d0f1ae96aa7b75f5950727112`;
- Replay Git HEAD: `8af247bb8424d6e5aebe5eb15915a47fd2210683`;
- Primary runner blob SHA: `0bf11ea54e33082900f49a73de276342e61c83a1`;
- Replay runner blob SHA: `762320fcc6fe81dad7aadb43b33e52c8a60100ad`.

The runner difference is explained by DR-027B, an infrastructure-level worktree-gate correction required before replay. DR-027B did not alter the scientific protocol, dataset, resolver semantics, model, split, metric, or execution order.

The original primary and replay manifests remain preserved without retroactive normalization.

## 4. Exact confirmatory results

Both executions reported exactly the same critical values:

- eligible origins: `507279`;
- train origins: `280760`;
- test origins: `226519`;
- resolved T_acc relations: `2509886`;
- unresolved dependency edges: `355475`;
- `LogLoss(B)`: `0.40512255638027656`;
- `LogLoss(T_acc)`: `0.41124528865339655`;
- `ΔLogLoss = LogLoss(B) − LogLoss(T_acc)`: `-0.006122732273119991`.

The replay reproduced the primary critical results exactly.

## 5. Descriptive result boundary

Under the frozen DR-026C convention, positive `ΔLogLoss` favors `T_acc` and negative values favor `B`.

Therefore the observed confirmatory result is descriptively in favor of the baseline representation `B`, with:

`ΔLogLoss = -0.006122732273119991`.

This statement is descriptive only. DR-026C and DR-027 did not authorize package-aware inferential analysis. Consequently this closure does **not** assert a p-value, confidence interval, population-level effect, causal effect, or statistical significance.

## 6. Post-execution prohibition check

The identity verifier explicitly confirmed that the following were not performed during verification:

- outcome recomputation;
- T_acc recomputation;
- model fitting;
- prediction generation;
- performance recomputation;
- significance testing;
- outcome-based selection or modification;
- post-hoc methodological optimization.

The verifier was structural/comparative only.

## 7. Evidence preservation

The following execution evidence is preserved in GitHub:

- `execution/CONFIRMATORY_PRIMARY_v01/EXECUTION_MANIFEST.json`;
- `execution/CONFIRMATORY_PRIMARY_v01/RESULTS.json`;
- `execution/CONFIRMATORY_REPLAY_v01/EXECUTION_MANIFEST.json`;
- `execution/CONFIRMATORY_REPLAY_v01/RESULTS.json`;
- `src/verify_dr027_primary_replay_identity_v01.py`.

The dataset itself is not committed to the repository. Its frozen SHA-256 remains:

`823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`

## 8. Governance conclusion

DR-027 has fulfilled its role as the sole confirmatory execution authorization gate. DR-027A and DR-027B are recorded as limited infrastructure/conformance corrections and do not constitute scientific redesign.

The Primary/Replay sequence is reproducible under the frozen protocol, and the evidence is sufficient to close the execution phase.

Any subsequent statistical inference, robustness analysis, alternative model, alternative horizon, alternative baseline, alternative T_acc representation, or further empirical test requires a new ex-ante decision/gate and must not be presented as part of the already closed DR-027 confirmatory execution.

**DR-027C CLOSED. PRIMARY/REPLAY VERIFICATION PASSED.**
