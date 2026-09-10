# IT-METH-I — Public Reproducible Fixture Evidence Category Rule 001

**Status:** `FROZEN — METHODOLOGICAL RULE / NO EXECUTION AUTHORIZATION`
**Date:** 2026-09-10

## Purpose

This rule formally distinguishes **public reproducible experimental fixtures** from **observed industrial cases**. The distinction is adopted following the FAA AMOC closure and the subsequent AWS-PatchAsgInstance candidate screening.

## 1. Evidence classes

### Class I — Observed industrial case

A bounded real-world operational case for which the relevant pre-decision state, transformations, accessibility conditions, temporal boundary, outcomes, comparator and evidence provenance can be independently frozen and audited.

Class I evidence may be considered for an industrial utility test subject to the full IT-METH-I admission sequence and IT-G1–IT-G5 gates.

### Class II — Public reproducible fixture

A deliberately bounded, publicly reproducible environment, workflow, dataset or reference configuration whose relevant variables can be instantiated or reconstructed independently, but which is **not itself evidence that an observed industrial organization or operation exhibited the represented state or outcome**.

Class II evidence may support:
- implementation feasibility;
- structural reconstruction;
- observability tests;
- reproducibility tests;
- controlled comparison of representations or procedures;
- falsifiable methodological experiments where the experimental claim is explicitly about the fixture.

Class II evidence may **not**, by itself, support:
- claims about observed industrial performance;
- claims that an industrial operator adopted or benefited from the mechanism;
- claims of industrial utility in an observed organization;
- financial/value realization claims in practice;
- causal claims about an industrial population.

## 2. Admission consequence

A Class II fixture does not automatically satisfy F1–F12 as though it were an industrial case.

Instead, each filter is evaluated against the **experimental object actually being tested**:

`fixture-level closure ≠ industrial-case closure`.

A fixture can therefore receive:
- `PASS` for reproducibility while industrial-case closure remains `NOT ESTABLISHED`;
- `PASS` for variable observability within the fixture while industrial pre-decision accessibility remains `NOT ESTABLISHED`;
- `PROMISING` for discriminative utility potential while industrial utility remains unproven.

## 3. No silent threshold relaxation

Introducing Class II does not relax the existing IT-METH-I industrial admission criteria. It creates a separate evidence class and requires the experimental claim to be scoped to that class.

No fixture may be promoted to Class I merely because it is publicly reproducible.

## 4. Application to AWS-PatchAsgInstance

The AWS-PatchAsgInstance material currently qualifies as a **Class II candidate fixture** at the reproducibility/structural level. It does not constitute a closed Class I industrial case.

Therefore the current disposition remains:

`CONDITIONAL — RETAIN FOR CONTROLLED FIXTURE EXPERIMENT / NOT ADMITTED TO IT-G1 AS INDUSTRIAL CASE`

No execution authorization is created by this rule.

## 5. Governance effect

This rule is methodological and does not alter TGCV Core, existing scientific claims, the FAA AMOC closure, or historical records.

Any future experiment using a Class II fixture must explicitly state:
1. the fixture identity and frozen version;
2. which variables are generated versus observed;
3. which claims are fixture-bounded;
4. which industrial claims remain outside the evidence boundary;
5. the comparator and metric before execution authorization, where applicable.
