# DR-031 — TR-131 Real-Dataset Execution Authorization Gate v0.2

**Status:** ACCEPTED — EX-ANTE EXECUTION AUTHORIZATION
**Accepted:** 2026-09-07
**Scope:** EXT-1.1 Rust / TR-131 / DR-029
**Predecessors:** DR-029 v0.2; DR-030; DR-029 execution audit v0.1

## 1. Purpose

Authorize one deterministic exhaustive execution of TR-131 using the patched executor after the prior execution was classified incomplete for integrity closure.

This decision authorizes execution only and does not predetermine the scientific result.

## 2. Authorization basis

The following prerequisites are satisfied:

1. DR-029 v0.2 remains the frozen structural design.
2. The prior real execution exposed an implementation-integrity gap: duplicate T_acc transformations could be silently collapsed by `set(rows)`.
3. The executor has been patched so duplicate canonical T_acc transformations fail closed.
4. The patched executor passed the synthetic conformance suite (`pass: true`).
5. No change has been made to B, T_acc, R*, equivalence, comparison logic, or the information firewall.

## 3. Frozen execution inputs

### Dataset

`rust_repos_2022_09_07.zip`

Expected local path:

`C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`

No replacement, refreshed, filtered, sampled, or modified dataset is authorized.

### Executor

`03_EXPERIMENTS/EXT-1.1_Rust/src/tr131_executor_v02.py`

Patched execution version committed at:

`2034aa309e8d756a6292f0d3e8e21dfba5130a23`

The v0.1 executor remains frozen as historical evidence and is not authorized for this run.

## 4. Frozen structural definitions

- Conventional representation `B`: exactly DR-025A.
- `T_acc`: exactly DR-021 / DR-026A using frozen `R* v0.2` semantics.
- Equivalence: exact equality of the frozen B tuple.
- Comparison: canonical T_acc membership equality, not cardinality alone.
- Duplicate canonical T_acc transformation: integrity failure; execution must fail closed.

## 5. Authorized population

Evaluate all admissible origin observations in the frozen structural snapshot. The DR-027 H=180 complete-followup population of 507,279 is not an eligibility restriction.

Empty T_acc is valid evidence. Missing or failed structural reconstruction is invalid.

## 6. Information firewall

The execution must not read, load, derive, or use Y_180, later release activity, downloads/adoption/popularity/success, predictive metrics, DR-027/DR-028 results, Reach, post-origin metadata, learned/target-derived features, or package identity as an additional B-equivalence feature.

## 7. Exact authorized command

From `C:\Users\pedri\TGCV`:

```powershell
python .\03_EXPERIMENTS\EXT-1.1_Rust\src\tr131_executor_v02.py --dataset "C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip"
```

Capture stdout and stderr in full without manual editing.

## 8. Required execution evidence

Preserve at minimum:

- executor commit SHA;
- dataset filename and exact local path;
- dataset integrity/hash where available;
- execution timestamp;
- Python/runtime version;
- origin count;
- B equivalence-class count;
- singleton and multi-member class counts;
- comparable class count;
- pair comparison count;
- differing class count;
- witness count;
- witness records;
- canonical witness-result SHA-256;
- firewall flags;
- sampling flag;
- duplicate-T_acc integrity status;
- deterministic replay evidence if executed;
- complete stdout/stderr capture.

Raw execution output must not contain scientific interpretation.

## 9. Abort / invalidation conditions

Invalidate the run if dataset resolution fails, required structural columns are malformed, duplicate origins or T_acc transformations are silently collapsed, missing state is bypassed, prohibited information is read, an alternative resolver/definition is substituted, sampling occurs, B/T_acc are modified, cardinality replaces membership comparison, package identity is added to B, or deterministic comparison cannot be reproduced.

## 10. Replay

If the primary output is captured successfully and the executor remains unchanged, perform one deterministic replay with the same dataset and executor. The deterministic summary and witness hash must match exactly.

## 11. Decision logic

- **TR-131 support for B:** at least one valid B-equivalent class contains different canonical T_acc membership sets.
- **TR-131 non-support for B:** every B-equivalent class has identical canonical T_acc membership.
- **Indeterminate:** reconstruction or firewall integrity fails.

No p-value, predictive metric, or causal claim is part of this decision.

## 12. Governance conclusion

**REAL-DATASET EXECUTION AUTHORIZED: YES — ONE DETERMINISTIC EXHAUSTIVE RUN USING EXECUTOR v0.2.**

Any deviation requires a new governance decision before execution.

The next gate after execution is the TR-131 execution-result audit. Scientific interpretation is deferred until execution integrity is established.
