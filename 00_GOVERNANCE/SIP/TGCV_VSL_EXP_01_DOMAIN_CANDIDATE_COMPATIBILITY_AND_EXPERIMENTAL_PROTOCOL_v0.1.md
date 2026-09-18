# TGCV — VSL-EXP-01
## Domain Candidate Compatibility and Experimental Protocol

**Status:** DRAFT / CANDIDATE FOR FREEZE  
**Version:** v0.1  
**Precondition:** VSL-SPEC-01 is FROZEN  
**Scope:** Candidate-domain compatibility and pre-experimental protocol  
**Role:** Determine whether a candidate domain can instantiate a VSL without retrospectively redefining Value

---

## 1. Purpose

VSL-EXP-01 defines the procedure for evaluating candidate domains against the frozen requirements of VSL-SPEC-01.

Its purpose is not to select a preferred domain.

Its purpose is to determine, for each candidate domain, whether the domain can support an independently specified, reproducible and pre-execution identification of Value.

The protocol therefore permits:

- compatibility;
- partial compatibility;
- methodological incompatibility.

A candidate domain must not be altered merely to obtain compatibility.

---

## 2. Frozen precondition

VSL-EXP-01 depends on the frozen artifact:

`00_GOVERNANCE/SIP/TGCV_VSL_SPEC_01_DOMAIN_INDEPENDENT_VALUE_IDENTIFICATION_v0.1.md`

Frozen specification blob:

`595afd1af16b856f33d4360d30e91be66680ecd1`

The requirements of VSL-SPEC-01 are normative for this protocol.

VSL-EXP-01 may not weaken, reinterpret or selectively omit them.

---

## 3. Scope

This protocol covers:

1. candidate-domain identification;
2. domain evidence inventory;
3. Value-identification compatibility assessment;
4. construction-readiness assessment for a domain-specific VSL;
5. pre-execution freezing of domain-specific Value rules;
6. classification of the candidate;
7. authorization or blocking of subsequent experimental protocol construction.

This protocol does not execute the experiment.

---

## 4. Candidate-domain neutrality

Candidate domains must be evaluated independently.

The protocol must not:

- rank candidates;
- assign a global score;
- declare a preferred candidate;
- infer experimental success from compatibility;
- choose a candidate because it produces a convenient Value definition.

If multiple candidates satisfy the frozen requirements, their later selection remains a separate research decision.

---

## 5. Candidate-domain dossier

Each candidate must have a pre-execution dossier containing, at minimum:

- domain identity;
- scope and population;
- unit of analysis;
- available observable/reconstructable outcomes;
- potential evaluative perspective(s);
- candidate reference frame;
- temporal scope;
- relevant costs/benefits/trade-offs;
- known uncertainty and missingness;
- provenance of domain evidence;
- limitations affecting Value identification.

The dossier must be assembled before the domain-specific VSL is frozen.

---

## 6. Compatibility assessment

For each candidate, assess the following requirements from VSL-SPEC-01.

| ID | Requirement | Result |
|---|---|---|
| C01 | Unit of analysis can be fixed | PASS / PARTIAL / FAIL |
| C02 | Evaluative perspective can be fixed | PASS / PARTIAL / FAIL |
| C03 | Outcome can be specified independently of Value | PASS / PARTIAL / FAIL |
| C04 | Reference can be fixed before result inspection | PASS / PARTIAL / FAIL |
| C05 | Outcome → Value mapping can be pre-specified | PASS / PARTIAL / FAIL |
| C06 | Directionality can be fixed | PASS / PARTIAL / FAIL |
| C07 | Time horizon can be fixed | PASS / PARTIAL / FAIL |
| C08 | Costs/benefits/trade-offs can be specified | PASS / PARTIAL / FAIL / N/A |
| C09 | Aggregation can be specified where required | PASS / PARTIAL / FAIL / N/A |
| C10 | Uncertainty/missingness can be specified | PASS / PARTIAL / FAIL |
| C11 | Independence from TGCV transformation/accessibility variables can be preserved | PASS / FAIL |
| C12 | All essential rules can be frozen before execution | PASS / FAIL |

The table is an assessment structure, not a scoring system.

---

## 7. Essential versus conditional requirements

C01-C07, C10, C11 and C12 are essential unless a domain-specific justification establishes that a particular requirement is genuinely not applicable under VSL-SPEC-01.

C08 and C09 may be marked N/A only where the domain structure demonstrably contains no relevant multidimensional cost/benefit or aggregation requirement.

N/A must be justified explicitly.

A missing rule is not equivalent to N/A.

---

## 8. Candidate classification

The compatibility assessment must produce one of the following methodological dispositions.

### VALUE_IDENTIFIED_READY

All essential Value-identification requirements can be specified and frozen before execution, and a domain-specific VSL can therefore be constructed without violating VSL-SPEC-01.

This status is a readiness classification, not evidence that Value has been observed or empirically validated.

### VALUE_PARTIALLY_IDENTIFIED_READY

Some Value dimensions or perspectives can be specified and frozen, but the complete declared Value construct cannot yet be identified reproducibly.

Subsequent work must preserve the partial boundary rather than silently expanding it.

### VALUE_NOT_IDENTIFIED_BLOCKED

One or more essential requirements cannot be satisfied independently and pre-execution.

The candidate is blocked from proceeding to a Value experiment under the current specification.

### INSUFFICIENT_DOMAIN_INFORMATION

The available domain information is insufficient to perform the compatibility assessment.

This is distinct from VALUE_NOT_IDENTIFIED_BLOCKED: the former indicates insufficient evidence for assessment; the latter indicates a substantive methodological incompatibility established by the available evidence.

---

## 9. Prohibited selection effects

The candidate assessment must not use experimental results to decide:

- which Outcome is Value;
- which reference is preferable;
- which direction is favorable;
- which time horizon produces the desired result;
- which costs or benefits may be ignored;
- which aggregation rule gives the desired classification.

No candidate may be made compatible by post hoc specification.

---

## 10. Domain-specific VSL construction gate

A candidate may proceed to construction of a domain-specific VSL only after:

1. its dossier is complete enough for compatibility assessment;
2. all essential compatibility requirements are PASS;
3. all applicable conditional requirements are PASS;
4. every N/A determination is justified;
5. the Value-identification rules can be frozen before execution;
6. no rule depends on future experimental results;
7. the independence boundary from TGCV variables is preserved.

The resulting domain-specific VSL must then be frozen separately.

---

## 11. Separation of candidate compatibility and experiment

VSL-EXP-01 does not itself establish:

- Value;
- a Value outcome;
- a causal effect;
- a relationship between accessibility and Value;
- experimental validity;
- predictive validity.

Its output is a compatibility/readiness disposition.

The subsequent experiment requires its own:

- domain-specific VSL;
- execution protocol;
- frozen inputs;
- runtime integrity checks;
- evidence audit.

---

## 12. Candidate comparison

If multiple candidate domains are assessed, results must be reported independently.

The protocol permits a comparison of documented compatibility conditions, but does not prescribe an ordering, score or winner.

Any later selection among compatible candidates is outside the evidentiary claim of this protocol.

---

## 13. Evidence and provenance

Every PASS, PARTIAL, FAIL or N/A determination must be traceable to the candidate-domain dossier and its underlying evidence.

The protocol must distinguish:

- observed domain fact;
- reconstructed domain fact;
- methodological inference;
- unresolved issue;
- non-claim.

No compatibility status may be supported solely by an assertion that a suitable Value measure “should exist”.

---

## 14. Freeze and change control

Before candidate assessment begins, VSL-EXP-01 itself must be frozen.

After freeze, substantive changes to:

- compatibility requirements;
- essential/conditional status;
- classification states;
- candidate selection rules;
- evidence requirements;

require a new protocol version.

A protocol revision may not silently replace the protocol under which a candidate was assessed.

---

## 15. Relationship to Synthetic Minimum v0.1

VSL-EXP-01 does not replace, modify or reinterpret the frozen Synthetic Minimum v0.1.

The synthetic demonstrator remains a separate methodological implementation with its own frozen contract and evidence boundary.

No Synthetic Minimum execution result is required to establish candidate-domain compatibility under VSL-EXP-01.

---

## 16. Governance boundaries

Creation or freeze of VSL-EXP-01 does not modify:

- TGCV Core;
- RMA;
- C09;
- Evidence-to-Claim Matrix;
- existing claim statuses.

Candidate compatibility is methodological preparation, not experimental evidence.

If later candidate execution generates material evidence routed into the cumulative matrix, GL-07 applies to that evidence expediente.

---

## 17. Freeze gate

VSL-EXP-01 may be frozen only after review confirms:

1. it faithfully operationalizes frozen VSL-SPEC-01 requirements;
2. it does not rank or score candidates;
3. it distinguishes compatibility from experimental evidence;
4. it distinguishes insufficient information from methodological incompatibility;
5. it preserves retrospective-specification protections;
6. it preserves the independence boundary from TGCV variables;
7. it does not import C09 assumptions;
8. it does not modify the frozen Synthetic Minimum;
9. it does not create a claim upgrade;
10. candidate-domain selection remains downstream of the frozen methodological requirements.

---

## 18. Next artifact

After VSL-EXP-01 is frozen, the next artifact is a candidate-domain dossier and compatibility assessment for one or more domains.

Only after a candidate passes the compatibility gate should a domain-specific VSL and experimental execution protocol be constructed.

---

## 19. Governance disposition

This artifact is a candidate protocol specification.

**Current status:** DRAFT / CANDIDATE FOR FREEZE
