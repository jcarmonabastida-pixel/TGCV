# TR-131 — Gate A Cross-Domain Operationalisation — Domain Selection and Experimental Protocol v0.1

**Document ID:** TR131_GATE_A_CROSS_DOMAIN_OPERATIONALISATION_001  
**Status:** CANONICAL WORKING EXPERIMENTAL SPECIFICATION  
**Date:** 2026-09-23  
**Repository:** jcarmonabastida-pixel/TGCV

## 1. Purpose

Gate A tests whether the transformation-space instrumentation demonstrated in VisitAll can be operationalised in a materially different domain.

The Gate A question is:

> Can the analytical grammar
> `S_t → T_acc,t → T_real,t → S_(t+1) → T_acc,t+1`
> be instantiated, reconstructed and audited in a materially different domain without importing VisitAll-specific semantics?

Gate A is an operationalisation test. It does not test representational superiority, Transformational Intelligence, outcome linkage, value causality or ontology.

## 2. Frozen reference domain

VisitAll is the first-domain reference.

Its established role is:

- executable instrumentation of accessible transformations;
- explicit realization and successor-state reconstruction;
- observation of successive `T_acc`;
- observation of non-empty `ΔT_acc`;
- bounded independent reconstruction.

Its negative representational-gain result is retained and is not reopened.

## 3. Domain-selection criteria

The second domain must satisfy all of the following before scientific execution:

1. **Material domain difference:** its domain semantics must be materially different from grid navigation/planning.
2. **Explicit state:** a reproducible state representation must be available from a primary source.
3. **Identifiable transformations:** transformations must have domain-defined identity, not be invented solely for TGCV.
4. **Independent accessibility condition:** applicability/accessibility must be determined without using downstream outcomes.
5. **Realization:** realized transformations must be observable or reconstructible.
6. **Successor state:** transformation effects must permit reconstruction of the next state.
7. **Future-space observability:** subsequent accessible transformations must be derivable or explicitly available.
8. **Primary-source provenance:** the domain artifact must have stable provenance, version/DOI or equivalent identifier, and reproducible retrieval.
9. **Independent reconstruction:** two executors must be able to reconstruct the same operationalization from frozen inputs.
10. **Falsifiability:** the case must permit a PASS, PASS WITH BOUNDARY, or FAIL outcome.
11. **No semantic back-fitting:** the operational mapping must be fixed before inspecting the scientific result.
12. **No outcome contamination:** outcomes must not define accessibility.

## 4. Selected Gate A candidate

**Candidate domain:** healthcare treatment process / process execution.

**Primary source:** Mozafari Mehr, A. (2023), “Healthcare treatment process (logs and CPN model)”, 4TU.ResearchData.

**DOI:** 10.4121/8683fc1a-aca1-447b-aba4-8d7806a9977f.v1

**Source characteristics verified at selection stage:**

- the dataset contains event and data logs generated through simulation of a healthcare treatment process;
- the process model is a Colored Petri Net (CPN);
- the logs include treatment activities such as patient admission, doctor visits and test orders;
- the repository is 4TU.ResearchData;
- the dataset is CC0;
- the source provides a versioned DOI;
- nine experiment archives are published.

This domain is materially different from VisitAll at the semantic level: it concerns healthcare treatment/process execution rather than grid-navigation planning, while retaining a formal transition model capable of supporting reproducible state/transition analysis.

## 5. Why this candidate is suitable for Gate A

The CPN model provides a source-defined transition semantics from which an operational mapping can potentially be constructed:

`S_t` = relevant marking/data state of the treatment process;

`T_acc,t` = enabled source-defined treatment transitions under the frozen CPN semantics and current marking/data conditions;

`T_real,t` = observed transition/event executed in the trace;

`S_(t+1)` = successor marking/data state after that transition;

`T_acc,t+1` = subsequently enabled transition set.

The candidate is therefore promising because it can test whether the TGCV grammar survives a domain in which transformations correspond to healthcare-process activities rather than robot movement actions.

This is a **candidate selection**, not yet a scientific execution result.

## 6. Preflight required before execution

No scientific execution is authorized by this document alone.

The following must be frozen first:

- exact downloaded archive/file identifiers;
- exact CPN model artifact;
- exact experiment/log artifact selected;
- source hashes;
- CPN execution/interpretation semantics;
- definition of the operational state;
- transformation identity rule;
- accessibility/enabled-transition predicate;
- treatment of data-dependent guards;
- event-to-transformation mapping;
- state update rule;
- trajectory/case identity;
- executor scripts;
- comparison protocol;
- stop criteria;
- claim boundary.

A preflight failure is a valid Gate A result and must not be repaired by changing definitions after inspection of results.

## 7. Independent execution design

Gate A uses the established execution pattern:

`source → frozen fixture → operationalisation → Executor-1 → Executor-2 → comparison audit → scientific evaluation → canonical evidence propagation`

Executor-2 must reconstruct the operationalization independently from the frozen package and without using Executor-1 outputs as interpretive guidance.

## 8. Gate A evaluation dimensions

The scientific audit will evaluate at minimum:

### A1 — State operationalisation

Can a reproducible domain state `S_t` be defined without embedding future outcomes?

### A2 — Accessibility operationalisation

Can `T_acc,t` be reconstructed from source-defined transition semantics and the current state?

### A3 — Realization identity

Can `T_real,t` be identified independently of outcome?

### A4 — Successor-state reconstruction

Can `S_(t+1)` be reconstructed from `S_t` and `T_real,t`?

### A5 — Transformation-space evolution

Can `T_acc,t+1` be reconstructed and compared with `T_acc,t`?

### A6 — Independent reproducibility

Do Executor-1 and Executor-2 agree under frozen inputs?

### A7 — Domain-boundary disclosure

Which parts of the operationalization are domain-specific and which survive as common analytical structure?

## 9. Gate A decision states

**PASS — CROSS-DOMAIN OPERATIONALISATION**

All required dimensions are operationally reproducible with no unresolved material boundary that prevents the analytical grammar from being instantiated.

**PASS WITH BOUNDARY**

The grammar is operationalisable, but one or more constructs require an explicit domain-specific qualification that remains compatible with the cross-domain analytical layer.

**FAIL — OPERATIONALISATION**

A required element cannot be operationalised or independently reconstructed without importing an unsupported assumption, contaminating the result, or collapsing a distinction essential to the analytical grammar.

A failed Gate A does not imply failure of TGCV as a whole. It identifies a boundary of the current cross-domain formulation.

## 10. Scientific exclusions

Gate A does not test:

- representational superiority over the healthcare/process-mining baseline;
- causal `ΔT_acc → ΔValue`;
- Transformational Intelligence differentiation;
- practical usefulness;
- outcome linkage;
- value-guided navigation;
- ontological irreducibility;
- modification of TGCV Core.

Those questions remain assigned to later gates or Gate F.

## 11. Decision boundary

The candidate domain is selected because it offers a materially different semantic environment with an explicit formal process model and reproducible public provenance.

Selection does not imply that the candidate will pass Gate A.

The next action is therefore **preflight and fixture freezing**, not scientific execution.

## 12. Relation to the canonical sequence

Gate A precedes:

**Gate B — Cross-domain usefulness**  
**Gate C — Transformational Intelligence differentiation**  
**Gate D — Outcome linkage**  
**Gate E — Value-guided navigation**  
**Gate F — Scientific Core & Ontology Review**

The governing methodological rule remains:

> **Evidence first → conceptual differentiation second → ontological review third → Core modification only if warranted by accumulated evidence.**
