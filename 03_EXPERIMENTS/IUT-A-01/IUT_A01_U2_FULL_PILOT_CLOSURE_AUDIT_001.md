# IUT-A-01 U2 — FULL PILOT 001 Closure Audit

**Status:** CLOSED — U2-NULL
**Case:** IUT-A-01
**Executor:** IUT-A-01-U2-PILOT-EXECUTOR-0.3
**Mode:** FULL_PILOT
**Trial universe hash:** `4a993f428144fc955c4060bc0299c23357f663929ecf05bfa3cb9cade30b8ec5`
**Frozen result artifact:** `IUT_A01_U2_FULL_PILOT_RESULT_001.json`
**Result SHA256 declared by execution:** `7ecf987db3a274e50aa540e6934dc3932254940c3bff23bad8298e42cc03ff70`

## 1. Closure determination

The FULL_PILOT execution completed with `EXECUTION_RESULT=PASS`. The frozen result artifact is present in canonical GitHub `main` and identifies the executor, execution mode, PASS status, trial-universe hash and declared result SHA256.

Execution integrity is accepted as PASS on the basis of the frozen execution record and the previously completed pre-execution alignment gate. No experiment rerun is authorized or required for closure.

## 2. M1 — primary decision correctness

- Control arm: **60.0% (24/40)**
- TGCV arm: **100.0% (40/40)**
- Difference: **+40.0 percentage points** in favor of TGCV.
- Predeclared degradation limit: **−5 percentage points**.
- Gate: **PASS**.

The result is consistent with the frozen Fixture 002 semantics. The control arm misses the dependency and alternative-space cases in which option B is the preferred admissible option; the TGCV arm selects the frozen preferred option across all 40 trials.

## 3. M2 — secondary elapsed decision time

Timing basis: `perf_counter_ns_single_decision_invocation`.

- Control median: **0.00155 ms**
- TGCV median: **0.00485 ms**
- Relative reduction: **−212.9%** (i.e. TGCV is slower under this timing basis).
- Predeclared threshold: **+10% relative reduction**.
- Gate: **FAIL**.

The timing result is retained as executed. It must not be rerun or replaced to obtain a favorable outcome.

This M2 measurement is a microbenchmark of the decision functions, at microsecond-scale elapsed times. It is not evidence about human decision time, end-to-end workflow duration, or industrial operational performance.

## 4. M3 status

M3 is retired for the current U2 pilot. It was not an active scoring criterion and cannot be used to rescue, reinterpret, or overturn the M1/M2 classification.

## 5. Final frozen classification

`U2-NULL`

Reason:

1. M1 passes its degradation gate.
2. M2 fails its predeclared threshold.
3. No execution-integrity violation is identified.
4. M3 is retired and unavailable for post-hoc rescue.

The result is therefore **not U2-POSITIVE** and **not U2-MIXED**.

## 6. Documentation / methodological note

The execution manifest states that tool/runtime overhead would be captured separately. Executor v0.3 does not expose a separate overhead field in the frozen result structure. This is recorded as a documentation/methodological discrepancy and is **non-blocking for closure of the executed pilot**. It does not justify altering the observed M2 result or rerunning the pilot.

## 7. Bounded scientific interpretation

The experiment supports only the bounded statement that, within the frozen IUT-A-01 Fixture 002 and under the predeclared M1 criterion, the TGCV decision arm achieved higher decision correctness than the control arm.

Because the overall U2-positive criterion requires both preservation of M1 and a qualifying M2 improvement, the pilot does **not** establish U2-positive decision-performance utility.

This closure does not establish:

- explanatory superiority of TGCV;
- general discriminatory superiority;
- industrial utility;
- financial or value realization;
- causal generalisation beyond the frozen experiment;
- validity across other domains or populations;
- modification or confirmation of TGCV Core.

## 8. Integrity and continuity disposition

- FULL_PILOT rerun: **PROHIBITED / NOT REQUIRED**.
- Fixture 002: **UNCHANGED**.
- Metric Design Revision 001: **UNCHANGED**.
- Execution Manifest 002: **UNCHANGED**.
- Executor v0.3: **UNCHANGED**.
- Historical Fixture 001: **IMMUTABLE**.
- Canonical evidence source: **GitHub `main`**.

**Closure status:** `CLOSED — U2-NULL`
