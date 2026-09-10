# IT-METH-I Class II AWS-PatchAsgInstance — Phase A Code Audit 005

**Status:** `CLOSED — PASS WITH REPAIR WRAPPER / RUNTIME RETRY BLOCKED UNTIL PREFLIGHT`

**Date:** 2026-09-10

## Trigger

Authorized Phase A execution using v0.3 reached CloudFormation `CREATE_FAILED`.
The primary resource failure was `AWS::ImageBuilder::ImageRecipe` because the
execution identity lacked `imagebuilder:CreateImageRecipe`.

The remaining reported failures (`VPC`, `InternetGateway`,
`EC2ImageBuilderIAMRole`, `InstanceRefreshHandlerLambdaRole`) were cancellation
cascade events, not primary causes.

## Repair decision

Do **not** expand the IAM permissions of `tgcv-experiment` merely to reproduce
an unrelated Image Builder component of the public AWS sample.

The Class II Phase A fixture requires the ASG/VPC/EC2 state needed to freeze the
predecision state for `AWS-PatchAsgInstance` and the same-target comparator.
Image Builder, its pipeline, infrastructure/distribution configuration,
Image Builder IAM instance profile/role, notification topic, and instance-refresh
Lambda resources are outside that minimum boundary.

v0.4 therefore prunes those unrelated resources from the packaged public sample
at the CloudFormation create-stack boundary, while preserving the source
composition and failing closed if any remaining resource references a removed
logical resource.

## Preserved repairs

- v0.2 non-empty `PatchFilterGroup` repair.
- v0.3 `CAPABILITY_AUTO_EXPAND` handling.
- v0.3 idempotent reuse of the existing `Patch Group App` baseline.
- Candidate/comparator transformation remains unauthorized.

## Integrity requirement

The v0.4 wrapper must pass local/static preflight before any AWS fixture retry.
No scientific result, utility result, industrial claim, or TGCV Core change is
inferred from the failed v0.3 execution.

## Next gate

`V04_PREFLIGHT_REQUIRED = TRUE`
`PHASE_A_TRANSFORMATION = NOT_AUTHORIZED`
