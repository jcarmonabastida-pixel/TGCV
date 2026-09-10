# IT-METH-I Post-Filter Case Data Reproducibility — AWS-PatchAsgInstance

**Status:** `CLOSED — PUBLIC REPRODUCIBLE FIXTURE AVAILABLE / INDUSTRIAL CASE STILL NOT CLOSED`
**Date:** 2026-09-10
**Candidate:** `AWS-PatchAsgInstance`

## Finding

A first-party AWS workshop provides a reproducible Patch Manager environment: prerequisite resources are created with CloudFormation, a patch baseline is created and assigned to a patch group, instances are scanned, compliance is reviewed, and missing updates are installed. The workshop explicitly uses four test instances and documents the pre-install compliance state as `Never reported`. citeturn0search11

A separate public example shows `AWS-PatchAsgInstance` being invoked automatically from an EC2 state-change event, passing the concrete instance identifier as `InstanceId`. citeturn0search0

AWS's first-party runbook reference confirms the runbook's ASG boundary, parameters and execution-control semantics. citeturn0search1

## Interpretation

This closes **reproducibility of a public experimental fixture** substantially better than the previous screening. It does **not** establish a real industrial decision case: the workshop resources are sample/test infrastructure and must not be represented as observed industrial evidence.

Therefore the candidate can support a controlled methodological experiment if the governance track explicitly admits a generated/public fixture as the case substrate, but it cannot yet be admitted as an industrial utility case under the current industrial-case specification without an explicit decision that such a fixture is acceptable.

## Gate impact

- F1 Documentary closure: PASS
- F2 System/state identifiability: PASS for fixture construction; CONDITIONAL for an industrial case
- F3 Transformation identity: PASS
- F4 Accessibility observability: PASS for fixture construction; CONDITIONAL for industrial interpretation
- F5 Temporal closure: PASS for the documented fixture procedure; CONDITIONAL for industrial case
- F6 Evidence integrity: PASS at source-document level
- F7 Metric observability: PASS/CONDITIONAL
- F8 Effort readiness: CONDITIONAL
- F9 Reproducibility readiness: PASS for public fixture construction
- F10 Discriminative utility potential: PROMISING
- F11 Comparator validity: CONDITIONAL-PASS
- F12 Downstream separation: PASS/CONDITIONAL

## Decision

**PUBLIC_FIXTURE_REPRODUCIBILITY = PASS**
**INDUSTRIAL_CASE_CLOSURE = NOT ESTABLISHED**
**IT-G1_ADMISSION = NOT GRANTED**
**EXECUTION_AUTHORIZATION = NONE**
**TGCV_CORE_CHANGE = NO**

## Next permissible decision

The methodological question is now explicit and bounded: **does the Industrial Track permit a public/generated reproducible fixture as the case substrate, or must the case be an observed industrial instance?**

No further generic AWS search is justified until that methodological boundary is decided. If public fixtures are admissible, this candidate has enough structure to prepare a concrete IT-G1 package. If they are not, the candidate should be closed and the search should pivot to a domain with naturally public real-world decision-time state.
