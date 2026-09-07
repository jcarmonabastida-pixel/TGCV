# DR-030 — TR-131 Real-Dataset Execution Authorization Gate v0.1

**Status:** ACCEPTED — EX-ANTE EXECUTION AUTHORIZATION
**Accepted:** 2026-09-07
**Scope:** EXT-1.1 Rust / TR-131 / DR-029
**Predecessors:** DR-029 v0.2; DR-029 Implementation / Pre-Execution Audit v0.1

## 1. Purpose

Authorize one deterministic exhaustive execution of the already frozen DR-029/TR-131 structural test against the frozen Rust dataset.

This decision authorizes execution only. It does not predetermine, imply, or anticipate the scientific result.

## 2. Authorization basis

The following prerequisites are satisfied:

1. DR-029 v0.2 is accepted as the ex-ante structural design.
2. The implementation/pre-execution protocol has been completed.
3. Synthetic conformance passed all reported tests:
   - same B + same T_acc → no witness;
   - same B + different T_acc → witness;
   - same-cardinality + different membership → witness;
   - different B → not comparable;
   - empty T_acc equality;
   - duplicate origin → fail closed;
   - missing/invalid B state → fail closed;
   - order permutation invariance;
   - prohibited outcome field not read;
   - deterministic repeatability.
4. The implementation audit was recorded as PASS in `AUDIT_DR-029_Implementation_PreExecution_Result_v0.1.md`.

## 3. Frozen execution inputs

### Dataset

The execution target is the already frozen Rust snapshot:

`rust_repos_2022_09_07.zip`

Expected local path:

`C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`

No replacement, refreshed, filtered, sampled, or modified dataset is authorized by this decision.

### Executor

`03_EXPERIMENTS/EXT-1.1_Rust/src/tr131_executor_v01.py`

The implementation currently frozen for execution is the version committed as:

`5c4208f6181af7fba30fa195a3e6a193bab55636`

### Structural definitions

- Conventional representation `B` is exactly DR-025A.
- `T_acc` is exactly the DR-021 / DR-026A construction using the frozen `R*` semantics.
- Equivalence is exact equality of the frozen B tuple.
- T_acc comparison is canonical set membership equality.

## 4. Authorized population

The TR-131 census is structural and independent of the DR-027 outcome horizon.

Therefore the executor shall evaluate all admissible origin observations in the frozen structural snapshot. The DR-027 H=180 complete-followup population of 507,279 is **not** a restriction for TR-131 and must not be used as an eligibility filter.

Terminal observations with valid structural state remain admissible. An empty `T_acc` is valid evidence; missing or failed structural reconstruction is not.

## 5. Information firewall

The execution must not read, load, derive, or use:

- Y_180;
- later release activity or any outcome field;
- downloads, adoption, popularity, success, or post-origin usage;
- predictive metrics or model outputs;
- DR-027/DR-028 results as selection inputs;
- Reach or any downstream substitute for T_acc;
- post-origin metadata;
- learned or target-derived features;
- package identity as an additional B-equivalence feature.

If any required computation would require such information, execution must fail closed rather than adapt the protocol.

## 6. Execution mode

The authorized mode is:

- exhaustive census;
- no sampling;
- no adaptive selection;
- deterministic ordering;
- canonical T_acc serialization;
- exact B equivalence;
- direct membership-set comparison;
- deterministic replay capable.

No exploratory or alternative analysis is authorized in the same run.

## 7. Exact authorized command

From `C:\Users\pedri\TGCV`:

```powershell
python .\03_EXPERIMENTS\EXT-1.1_Rust\src\tr131_executor_v01.py --dataset "C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip"
```

The output must be captured in full without manual editing.

## 8. Required execution evidence

The execution record must preserve at minimum:

- executor commit SHA;
- dataset filename and exact local path;
- dataset integrity/hash if available from the frozen dataset record;
- execution timestamp;
- Python/runtime version;
- origin count;
- B equivalence-class count;
- singleton and multi-member class counts;
- comparable class count;
- pair comparison count;
- differing class count;
- witness count;
- witness records, if any;
- canonical witness-result hash;
- firewall flags;
- sampling flag;
- deterministic/replay evidence where executed;
- complete stdout/stderr capture.

No scientific interpretation is to be added to the raw execution output.

## 9. Abort / invalidation conditions

Execution is invalid and must not be interpreted if any of the following occurs:

- dataset cannot be resolved exactly;
- required structural columns are absent or malformed;
- duplicate origin/version identifiers are silently collapsed;
- missing structural state is imputed or bypassed;
- a prohibited outcome/future field is read or used;
- an alternative resolver or T_acc definition is substituted;
- sampling or adaptive selection occurs;
- B is modified from DR-025A;
- T_acc is compared by cardinality alone;
- package identity is introduced into B equivalence;
- non-deterministic ordering/serialization prevents reproducible comparison;
- execution requires post-hoc changes to the frozen protocol.

## 10. Decision logic after execution

The result shall be classified exactly as DR-029 specifies:

- **TR-131 support for B:** at least one valid B-equivalent class contains two origin states with different canonical T_acc membership sets.
- **TR-131 non-support for B:** exhaustive evaluation finds identical canonical T_acc membership within every B-equivalent class.
- **Indeterminate:** reconstruction or firewall integrity fails.

No p-value, confidence interval, predictive metric, or causal claim is part of this decision.

## 11. Replay

After the primary execution, a replay should be run only if the primary output is successfully captured and the executor remains unchanged. The replay must use the same dataset and implementation and must reproduce the deterministic summary and witness hash exactly.

A mismatch invalidates deterministic replay and requires investigation before interpretation.

## 12. Boundary with prior results

DR-027C and DR-028 remain closed and unchanged. Their negative predictive result is neither a selection criterion nor an input to TR-131.

The present execution tests structural sufficiency of `B` for `T_acc`; it is not a predictive re-analysis.

## 13. Governance conclusion

**REAL-DATASET EXECUTION AUTHORIZED: YES — ONE DETERMINISTIC EXHAUSTIVE TR-131 RUN.**

This authorization is limited to the frozen protocol, frozen dataset, and frozen executor specified above. Any deviation requires a new governance decision before execution.

After execution, the next gate is the **TR-131 execution-result audit**, followed by scientific interpretation only after the execution evidence passes that audit.
