# C09 OLPC Peru — Causal Gap Closure Evidence Record 001

Status: **PARTIAL/INCONCLUSIVE — SCIENTIFIC CLOSURE NOT AUTHORIZED**

## 1. Scope

This record documents the controlled scientific execution of C09 v0.7 for the OLPC Peru case and closes the causal-gap exercise at the level supported by the evidence. It records the distinction between evidence that the randomized assignment changes the bounded accessibility space and evidence sufficient to identify a causal pathway from accessibility change to subsequent trajectory.

This record does **not** upgrade TGCV Core, RMA, the Evidence Matrix, STATUS, or any other governance claim automatically.

## 2. Frozen specification

The execution was governed by the frozen artifact:

`00_GOVERNANCE/SIP/TGCV_C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_SPEC_001.md`

The frozen specification was not modified by the executor or the preflight.

## 3. Execution artifacts

Controlled executor:

`03_EXPERIMENTS/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE/run_c09_olpc_peru_gap_closure_v03.py`

Preflight:

`03_EXPERIMENTS/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE/output_v07/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_PREFLIGHT_003.json`

Scientific result:

`03_EXPERIMENTS/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE/output_v07/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE_RESULT_003.json`

Implementation audit:

`03_EXPERIMENTS/C09_OLPC_PERU_CAUSAL_GAP_CLOSURE/C09_OLPC_V07_EXECUTOR_IMPLEMENTATION_AUDIT_001.md`

## 4. Integrity hashes

### Scientific result

SHA256:

`2DBB053F9B025EA807671AD2820AA18945A5D48EABE39CB41127E55EBA5BBD4E`

### Preflight

SHA256:

`26D0A04AA6006867772C53DDD667909AC91B4E54637B1E0EAB7AE0EC3073D95B`

The hashes above are the locally computed SHA256 values of the executed artifacts.

## 5. Scientific execution result

Overall status:

**PARTIAL/INCONCLUSIVE**

Scientific closure authorized:

**FALSE**

The result is not an infrastructure failure. The controlled execution completed after a PASS preflight, and the remaining non-closure is methodological: the available evidence does not separately identify the accessibility-to-trajectory causal pathway from direct treatment or other alternative pathways.

## 6. Gate results

### G6.1 — Z → ΔT_acc

**PASS**

The corrected individual-lottery causal universe is preserved:

`participated_in_lottery == 1 AND treatment_school == 1`

with:

`Z = won_lottery`.

The execution provides measurable bounded accessibility contrasts, including the aggregate resource-count contrast used by the mediator diagnostic.

Interpretation: the randomized assignment provides evidence that the bounded transformational/accessibility space changes under the treatment assignment within the operationalized OLPC domain.

### G6.2 — ΔT_acc → subsequent trajectory

**PASS_DIAGNOSTIC_ONLY**

The executor uses `Z_to_delta_resource_count` as the specified aggregate ΔT_acc contrast and computes a bounded Wald/IV diagnostic using Z as instrument for downstream trajectory contrasts.

The result explicitly records:

`method = Wald/IV diagnostic using Z as instrument`

and:

`causal_interpretation_authorized = False`.

Therefore G6.2 is a diagnostic result only. It must **not** be interpreted as identified causal mediation.

### G6.3 — persistence under attrition sensitivity

**PASS**

The trajectory contrasts retain the required sign consistency across the complete-case and IPW sensitivity analyses implemented by G5.

This supports robustness of the observed trajectory contrast under the specified X0-only attrition sensitivity, but does not by itself establish the causal accessibility-to-trajectory bridge.

### G6.4 — alternative/direct pathways

**NOT_IDENTIFIED**

`alternative_paths_addressed = False`.

The available evidence does not separately identify or eliminate direct treatment pathways and other alternative channels that could generate subsequent trajectory differences without operating through the measured accessibility change.

### G6.5 — causal identification limit

**NOT_SATISFIED**

`causal_identification = False`.

No separate exclusion restriction, mediation identification strategy, or equivalent argument sufficient to attribute the downstream trajectory difference specifically to ΔT_acc was established.

## 7. C09 causal-gap questions

### 7.1 Does Z produce measurable bounded ΔT_acc?

**Yes, within the operationalized OLPC domain.** G6.1 PASS.

### 7.2 Does Z produce measurable subsequent trajectory differences?

**Yes.** The downstream trajectory contrasts are present and survive the specified G5 persistence sensitivity. This is compatible with the observed randomized-assignment effect on subsequent trajectory.

### 7.3 Is the trajectory difference attributable specifically to accessibility change?

**Not identified by this execution.** The bounded Wald/IV diagnostic in G6.2 is explicitly non-causal, and G6.4/G6.5 remain unresolved.

### 7.4 Does C09 satisfy its causal closure criterion?

**No. PARTIAL/INCONCLUSIVE.** The execution establishes the accessibility-change component and downstream trajectory differences, but does not separately identify the causal bridge `ΔT_acc → subsequent trajectory` against direct and alternative treatment pathways.

## 8. Scientific interpretation

The evidence supports the following bounded statement:

`Z → ΔT_acc` is empirically supported in the specified operational domain, and `Z` is also associated with measurable subsequent trajectory differences. However, the available evidence does not identify the stronger causal mediation claim that the trajectory change is caused specifically by the accessibility change rather than by direct treatment effects or other channels.

Accordingly, this C09 execution provides **partial evidence for the causal-gap bridge but does not close the causal gap**.

The result must not be promoted to a stronger TGCV causal claim.

## 9. Governance boundary

This evidence record does not automatically modify:

- TGCV Core;
- RMA;
- Evidence Matrix;
- STATUS;
- or any other canonical governance state.

Any later governance update must be a separate, explicitly authorized operation based on this evidence record.

## 10. Final disposition

**C09 v0.7 — PARTIAL/INCONCLUSIVE.**

Scientific execution completed. Implementation audit PASS. Preflight PASS. G6.1 PASS. G6.2 diagnostic-only. G6.3 PASS. G6.4 NOT_IDENTIFIED. G6.5 NOT_SATISFIED. Scientific closure remains unauthorized.
