# IUT-A-01 — U2 Fixture Consistency Audit 001

**Date:** 2026-09-11  
**Status:** `AUDIT COMPLETE — FULL_PILOT NOT VALID FOR INFERENCE`  
**Case:** `IUT-A-01`  
**Utility layer:** `U2 — DECISION-PERFORMANCE UTILITY`

## 1. Audit trigger

The first `FULL_PILOT` executed successfully at infrastructure/protocol level, but produced a `NULL` result with a structurally anomalous M3 value. A fixture-consistency audit was therefore required before any scientific interpretation or rerun.

## 2. Audited frozen artifacts

- Execution manifest: `IUT_A01_U2_EXECUTION_MANIFEST_001.md`
- Fixture specification: `IUT_A01_U2_FIXTURE_SPECIFICATION_001.md`
- Executor source: `src/execute_iut_a01_u2_pilot_v02.py`
- Wrapper executor: `src/execute_iut_a01_u2_pilot_v021.py`
- Trial universe hash: `fcb2f7b6033249f4d326abb8e703cf8b353df6595e77fad2263c41a10206ca2b`
- Manifest Git blob SHA: `1506c548a0d1bee7a042c3e3395be9b54d3fb608`
- Fixture Git blob SHA: `5629db741dce63eee0e00314de6ecffaf1b82fc4`

## 3. Finding F-001 — objective/preference inconsistency

**Severity:** `MATERIAL`

The frozen executor defines option objective scores as:

- A = `80 + cycle`
- B = `85 + cycle`
- C = `99 + cycle`

The TGCV decision procedure selects the highest-objective option among options satisfying the frozen feasibility rules.

However, the frozen trial ground truth assigns preferred decisions of A or B in several classes while C remains feasible and has the highest objective score.

Therefore the decision rule implemented by `tgcv_decision()` and the scoring reference `preferred_option` are not semantically aligned.

This is directly visible in the frozen source: `tgcv_decision()` maximizes `objective_score` over feasible options, while `build_trial()` can designate A/B as preferred while C is feasible.

## 4. Observed manifestation in FULL_PILOT

The executed result shows:

- M1 control = `0.60`
- M1 TGCV = `0.25`
- M1 delta = `-35.0` percentage points
- M2 actual timing favors control
- M2 secondary proxy favors TGCV
- M3 control = `0.0`
- M3 TGCV = `1.875`
- M3 denominator = `16`
- classification = `NULL`

The repeated TGCV selection of `C` in DIRECT_FEASIBILITY, DEPENDENCY and ALTERNATIVE_SPACE trials is consistent with the frozen implementation's objective-maximization rule, rather than constituting independent evidence of poor TGCV decision performance.

## 5. Finding F-002 — M3 denominator/definition incompatibility

**Severity:** `MATERIAL`

The frozen implementation computes M3 as a rate over trials where the preferred option is viable and more than one viable option exists. It then counts every selected option outside the viable set as a missed viable alternative.

Because the TGCV procedure repeatedly selects C while C is not in the frozen `viable_options` tuple, the resulting TGCV M3 value can exceed 1.0 (`1.875`). This is not a valid conventional rate and demonstrates that the fixture/reference relationship is not suitable for inference in the current form.

## 6. Finding F-003 — control/TGCV asymmetry is not the primary defect

The control and TGCV procedures operate on the same generated trial objects and the integrity gate confirms the same universe for both arms. The present audit therefore does not identify unequal trial information as the cause of the anomalous result.

The primary defect is semantic alignment between the frozen decision objective, admissibility/reference rules, and scoring ground truth.

## 7. Disposition of FULL_PILOT

The `FULL_PILOT` execution remains an immutable historical execution record. Its infrastructure status is `PASS`, but its scored `NULL` result **must not be used as evidence for or against TGCV U2 utility** because the fixture has a material internal consistency defect.

No rerun is authorized against the current fixture 001.

No modification is made to fixture 001, manifest 001, or the historical execution result.

## 8. Required next action

Create a new explicitly versioned fixture revision (e.g. Fixture 002) only after defining a coherent decision objective/reference relation. The revision must be separately hashed and must pass a pre-execution consistency audit before any new FULL_PILOT.

The original fixture and execution remain preserved for provenance.

## 9. Interpretation boundary

This audit does **not** establish that TGCV is ineffective. It establishes only that the first U2 computational fixture is not internally coherent enough for inferential interpretation.
