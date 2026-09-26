# TI-001 V011 E1-R / E2-R Independent Execution Concordance Audit Specification 001

**Status:** GATE SPECIFICATION — SCIENTIFIC ANALYSIS NOT YET AUTHORIZED

## Purpose

Verify that E1-R and E2-R are two separately executed, independently identified observations of the same frozen V011 decision fixture and that neither execution was contaminated by the other.

This gate does not calculate or report TI-DC, TI-NULL, presentation effects, pooled estimates, or any other scientific estimand.

## Canonical bindings

Both executions must bind exactly to:

- Fixture ID: `TI001-V011-FIXTURE-001`
- Fixture SHA-256: `30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1`
- Interface Git blob SHA: `8667b0ff70f58283c688f24c76f10db142655d14`
- Generator Git blob SHA: `9170f767cac3fceccaba248747c6524c5f150e11`
- Schema Git blob SHA: `b2fef667f6eb33689ece5481957d3917a860dd3e`
- Model: `gpt-5.6-luna`
- Reasoning: `{"effort":"none"}`

## Required checks

The audit must verify:

1. E1-R primary execution audit exists and is PASS.
2. E2-R primary execution audit exists and is PASS.
3. E1-R and E2-R have distinct executor identities.
4. E1-R and E2-R results are distinct files and independently executed.
5. Both bind exactly to the same frozen fixture/interface/generator/schema.
6. Each execution contains 420 decision records.
7. Decision IDs match the same fixture in canonical serialized order within each execution.
8. Each execution has 140 units per condition and 210 per presentation.
9. Each execution has 420 valid A/B decisions and zero invalid decisions.
10. Each execution has zero observed reasoning tokens.
11. Each execution has 420 unique response identifiers.
12. E1-R result contains no reference to E2-R result or pooled result.
13. E2-R result contains no reference to E1-R result or pooled result.
14. No result contains an observed output field from the other execution.
15. E1-R and E2-R response IDs are disjoint.
16. Runtime metadata are separately recorded.
17. Neither execution contains retry, recoding, repair, imputation, or response-dependent input mutation markers.
18. No scientific estimands or outcome/value variables are computed inside either execution result.
19. Any response-level agreement/disagreement is treated as an observation for later analysis, not as an execution-validity criterion.
20. The gate itself performs no scientific estimation.

## Independence interpretation

Different A/B responses between E1-R and E2-R do not by themselves indicate an execution defect. Bit-for-bit equality is not required.

Concordance is established only at the fixture/protocol/traceability level. Response agreement is a later empirical quantity.

## Outcome

**PASS** means the two independent executions are jointly eligible for the subsequent scientific-analysis gate.

**FAIL** blocks scientific analysis and requires resolution of the identified execution-level defect.

No pooling is performed by this gate.
