# TGCV — WP2 TSTC Execution Result 001

**Status:** CLOSED — BOUNDED ACCESSIBILITY EXECUTION PARTIAL; DEMONSTRATOR COMPLETION BLOCKED
**Date:** 2026-09-17
**Fixture:** TSTC synthetic fixture freeze 001
**Execution:** `TSTC_EXECUTION_v001`
**Environment:** Windows-11-10.0.26200-SP0; Python 3.14.7; deterministic (`random_seed=null`)

## 1. Evidence provenance

The execution output was supplied from the authorized local run of:

`03_EXPERIMENTS/TSTC/tstc_execution_v001.py`

The reported mode was:

`TSTC_SYNTHETIC_EXECUTION`

## 2. Observed structural results

### FX-C01

`T_acc,0` contained:

- `c01.deploy_A`
- `c01.deploy_B`
- `c01.restrict_security`

After `I-C01` (`trust_B: trusted → untrusted`), `c01.deploy_B` closed while `c01.deploy_A` and `c01.restrict_security` persisted.

Observed:

`ΔT_acc = closed {c01.deploy_B}; opened ∅`

The negative control changed `routing` and produced an empty accessibility delta.

### FX-C03

`T_acc,0` contained four transformations.

After `I-C03` (`permission_repo: granted → denied`), `c03.inspect_repo` and `c03.open_pr` closed while `c03.query_db` and `c03.complete_task` persisted.

Observed:

`ΔT_acc = closed {c03.inspect_repo, c03.open_pr}; opened ∅`

The negative control produced an empty accessibility delta.

### FX-C05

`T_acc,0` contained five transformations.

After `I-C05` (`grid_capacity: high → low`), `c05.start_A` and `c05.start_B` closed while `c05.defer_A`, `c05.defer_B` and `c05.redirect_A_to_B` persisted.

Observed:

`ΔT_acc = closed {c05.start_A, c05.start_B}; opened ∅`

The negative control produced an empty accessibility delta.

## 3. What this execution establishes

Within the frozen synthetic representation, the three declared positive interventions produced deterministic, rule-derived changes in `T_acc`, and all three negative controls preserved `T_acc`.

This is a bounded execution observation of the synthetic demonstrator machinery.

It is not empirical evidence about an external system.

## 4. Completion gap detected

The execution runner returned an empty trajectory for every fixture and did not yet execute the frozen cross-domain propagation sequence or reconstruct/report the conventional baselines.

Therefore the complete TSTC minimum demonstrator contract has **not** been executed.

Specifically, the current output does not yet establish:

- admissible trajectory recording;
- C01 → C03 propagation;
- C03 → C05 propagation;
- local versus propagated accessibility effects;
- baseline reconstruction and representational comparison;
- complete frozen output schema for the full demonstrator.

## 5. Disposition

The result is therefore classified:

**`CLOSED — BOUNDED ACCESSIBILITY EXECUTION PARTIAL; DEMONSTRATOR COMPLETION BLOCKED`**

The positive `ΔT_acc` observations are retained as execution evidence for the implemented synthetic accessibility component, but they MUST NOT be promoted to a complete TSTC applicability result.

## 6. Required next implementation step

Extend the execution runner, without changing fixture definitions, to implement:

1. trajectory recording using only transformations admissible at each decision point;
2. explicit C01 → C03 propagation;
3. explicit C03 → C05 propagation;
4. separation of local and propagated effects;
5. conventional baseline reconstruction with identical frozen information;
6. comparison observations without aggregate scoring;
7. complete reproducibility/output metadata;
8. fail-closed validation against the frozen execution authorization gate.

Only after those components execute successfully may a final bounded applicability disposition be considered.

## 7. Non-claims

This record does not establish:

- TGCV scientific validity;
- causal validity beyond the synthetic fixture's declared rules;
- superiority over conventional representations;
- generality;
- value creation;
- `ΔT_acc → ΔV`;
- deployment readiness;
- industrial authorization.

No Core/RMA/Matrix/C09/C10/VSL-44 scientific status change is made by this record.
