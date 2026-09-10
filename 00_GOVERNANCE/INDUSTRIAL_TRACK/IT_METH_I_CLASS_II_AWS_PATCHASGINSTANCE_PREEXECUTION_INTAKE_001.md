# IT-METH-I — Class II AWS-PatchAsgInstance Pre-Execution Intake 001

**Status:** `BLOCKED — PRE-EXECUTION INTAKE NOT CLOSED`
**Date:** 2026-09-10
**Evidence class:** `CLASS II — PUBLIC REPRODUCIBLE FIXTURE`
**Candidate:** `AWS-PatchAsgInstance`

## Purpose

Determine whether the public AWS fixture can be frozen sufficiently to permit a controlled Class II experiment without silently substituting documentation examples for observed case data.

## Intake checklist

| Requirement | Current disposition | Reason |
|---|---|---|
| Fixture identity/version | CONDITIONAL | Public AWS material identified; exact frozen package still required |
| Infrastructure definition | CONDITIONAL | Reconstructible, but exact package/version must be frozen |
| ASG identity | NOT CLOSED | Documentation examples do not establish one frozen experimental ASG |
| Instance identity | NOT CLOSED | A concrete fixture instance must be instantiated/frozen |
| Lifecycle/replacement configuration | NOT CLOSED | Must be frozen before decision point |
| OS/image | NOT CLOSED | Must be frozen explicitly |
| Patch group/baseline | NOT CLOSED | Must be frozen explicitly |
| Pre-decision compliance state | NOT CLOSED | Must be captured before candidate invocation |
| Runbook identifier/version | CONDITIONAL | Runbook identity documented; execution package must freeze reference |
| Runbook parameters | NOT CLOSED | Exact values must be frozen |
| Comparator | NOT CLOSED | Ordinary patch path must be operationalized before execution |
| Accessibility predicates | NOT CLOSED | Must be expressed from pre-decision observables |
| Temporal cutoff | NOT CLOSED | Must be frozen before execution |
| Evidence provenance | CONDITIONAL | First-party documentation identified; instantiated fixture evidence not yet packaged |
| Two independent reconstructions | NOT CLOSED | Required before execution |
| Metric | NOT CLOSED | Discriminative metric must be frozen ex ante |
| Effort convention | NOT CLOSED | Required if effort is reported |

## Gate decision

`PRE_EXECUTION_GATE = BLOCKED`

The fixture is **not executable yet**.

The blocking condition is not lack of a documented runbook. The blocking condition is that the experimental fixture has not yet been instantiated and frozen at the level required to define a common pre-decision state for candidate and comparator.

## Required next operation

Construct the fixture intake package locally from the public AWS material, freeze its infrastructure/configuration identifiers and pre-decision state, and produce a manifest containing byte hashes and all mandatory variables.

The local package may be generated and tested locally; GitHub remains the authoritative record of the resulting manifest and gate decision.

No AWS production account, real industrial organization, or production system is implied or required by this Class II design.

## Prohibitions

Until the gate is closed:

- do not invoke `AWS-PatchAsgInstance` as an experimental treatment;
- do not score utility;
- do not claim industrial evidence;
- do not infer accessibility from post-decision outcomes;
- do not alter TGCV Core;
- do not open IT-G1;
- do not issue IT-G5 authorization.
