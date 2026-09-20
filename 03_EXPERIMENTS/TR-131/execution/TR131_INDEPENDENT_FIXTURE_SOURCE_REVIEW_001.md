# TGCV — Independent Fixture Source Review 001

**Status:** CLOSED — SOURCE BASIS SUFFICIENT FOR CONSTRUCTION, WITH EXPLICIT BOUNDARIES
**Scientific execution:** NOT AUTHORIZED
**Date:** 2026-09-20

## 1. Purpose
Identify independently specified domain mechanisms from which the Transformation-Space Dynamics Representation Test can derive fixtures without inventing TGCV-specific semantics.

## 2. Source-selection rule
A source is admissible only if it specifies domain mechanisms independently of TGCV, including enough information to identify states/routines, possible actions or transformations, realization mechanisms, and changes over time.

The source is not treated as evidence that TGCV is correct. It is used only as a fixture source.

## 3. Candidate source A — self-adaptive systems
Gil de la Iglesia and Weyns (2015), MAPE-K Formal Templates to Rigorously Design Behaviors for Self-Adaptive Systems, ACM Transactions on Autonomous and Adaptive Systems, DOI 10.1145/2724719.

The work provides formal templates for designing self-adaptive behavior around MAPE-K and is therefore suitable as an independent source for a software/system adaptation fixture.

Relevant independently specified semantics include monitoring, analysis, planning and execution of adaptation behavior, with knowledge supporting the loop.

This source is appropriate for Domain A because the adaptation mechanism exists independently of TGCV.

## 4. Candidate source B — organizational routine transformation
Chen, Ouyang and Pan (2013), The role of feedback in changing organizational routine: A case study of Haier, China, Information & Management 50(6), 971–974, DOI 10.1016/j.ijinfomgt.2013.09.002.

The case specifies an organizational routine, its action pattern, feedback, and subsequent routine change during organizational transformation.

The study reports that feedback from performing a routine contributed to changes in routine patterns and organizational transformation.

This is suitable as an independent source for Domain B because the transformation mechanism and temporal change are documented independently of TGCV.

## 5. Supporting source B2 — routine reconfiguration and trajectory
Chen, Guo and Zhao (2021), Cross-fertilization for routine reconfiguration in IT-enabled organizational transformation, Information & Management 58(2), 103414, DOI 10.1016/j.im.2020.103414.

The study explicitly examines routine reconfiguration and reports changes involving trajectory components during IT-enabled organizational transformation.

This source can be used as a supporting source when the fixture requires a richer trajectory representation.

## 6. Supporting affordance source — not selected as primary fixture
Dremel, Herterich, Wulf and vom Brocke (2020), Actualizing big data analytics affordances: A revelatory case study, Information & Management 57(1), 103121, DOI 10.1016/j.im.2018.10.007.

The study identifies affordances and actualization mechanisms in an automotive manufacturing setting.

It is useful as a comparator/anti-circularity source because it demonstrates that action possibilities and their actualization are already independently theorized.

It should not be used as the primary source for the TGCV fixture if doing so would make the fixture definition effectively an affordance-theory translation into TGCV notation.

## 7. Source adequacy decision
The review finds sufficient independent source material to construct candidate fixtures:
- Domain A: self-adaptive software/system adaptation using MAPE-K semantics;
- Domain B: organizational routine transformation using documented routine-change and feedback mechanisms.

The sources provide independent domain semantics from which cases can be derived.

## 8. Critical limitation
The sources do not independently define T_acc.

Therefore the fixture construction must derive T_acc from source-defined admissibility/action conditions rather than import the term or its meaning from the literature.

The derivation rule must be declared before the test and applied identically at the semantic level to both domains.

If a source does not contain enough information to derive accessibility independently, that case must be marked INCONCLUSIVE rather than supplemented with TGCV-specific assumptions.

## 9. Anti-circularity rule
The fixture constructor may use:
- source-defined preconditions;
- source-defined available actions/routine changes;
- source-defined system configuration constraints;
- source-defined adaptation policies or mechanisms;
- information explicitly available before realization.

The constructor may not use:
- observed realized transformation to define prior accessibility;
- future state;
- outcome/value;
- trajectory success;
- post-hoc classification;
- TGCV's desired result.

## 10. Comparator rule
The baseline representation and TGCV representation must derive from the same source facts.

The TGCV representation may expose T_acc explicitly, but it may not receive additional domain information unavailable to the comparator.

## 11. Construction consequence
The source review therefore removes the previous BLOCKED condition concerning absence of independent domain mechanisms.

It does not authorize scientific execution.

The next construction task is to build candidate fixtures from these sources and perform a fixture-level semantic audit before freezing them.

## 12. Next gate
**FIXTURE CONSTRUCTION AND SEMANTIC AUDIT**

Required outputs:
1. Domain A fixture;
2. Domain B fixture;
3. source-to-fixture traceability;
4. pre-realization information inventory;
5. T_acc derivation rule;
6. baseline comparator;
7. null/control case;
8. ambiguity case;
9. independent reconstruction worksheet.

No scientific execution is authorized.