# IT-METH-I Class II AWS-PatchAsgInstance — Phase A Code Audit 004

**Status:** `CLOSED — PASS WITH REPAIR WRAPPER`

## Finding

Phase A execution reached AWS Systems Manager and failed at `CreatePatchBaseline` with:

`ValidationException: Filter Group within a Rule cannot be empty.`

The v0.1 executor contained a `PatchRule` whose `PatchFilterGroup.PatchFilters` was empty. This was an implementation defect in the fixture-builder request construction, not an AWS credential, governance, or scientific-result failure.

## Repair

Canonical repair executable:

`00_GOVERNANCE/INDUSTRIAL_TRACK/execution/class_ii_aws_patchasginstance_phase_a_fixture_build_v02.py`

Commit: `fdad5ca2672c472218c1987b9befc5088b02b72c`

The wrapper preserves the audited v0.1 executor and replaces only `create_fixture_baseline` at runtime. The repaired request contains two non-empty filter groups:

1. `CLASSIFICATION = Security, Bugfix` — Critical compliance, security/bugfix rule.
2. `SEVERITY = Critical, Important, Medium, Low` — Medium compliance, non-security enabled.

No candidate transformation, comparator transformation, utility scoring, or industrial execution is introduced.

## Static audit

PASS criteria:

- repair is isolated to PatchBaseline request construction;
- every generated PatchRule contains a non-empty `PatchFilterGroup.PatchFilters`;
- Amazon Linux 2 remains the operating-system target;
- Patch Group remains `App`;
- approved patch selector remains `kernel*`;
- candidate execution remains `NOT_AUTHORIZED`;
- comparator execution remains `NOT_AUTHORIZED`;
- Phase A remains fixture-build + predecision-freeze only;
- original v0.1 source and its frozen source hashes are not modified by the repair wrapper.

## Runtime status

The repair has **not** yet been executed against AWS. Therefore:

`AWS_RUNTIME_EXECUTION = NOT_YET_PERFORMED`

The previous failed attempt produced no valid fixture and cannot be treated as a Phase A result.

## Gate

`REPAIR_AUDIT = PASS`

Next authorized operation: pull the new canonical executable locally and run the same Phase A command using v0.2, with `AWS_PROFILE=tgcv`. Do not execute candidate or comparator transformations.
