# TGCV — Domain A Source Selection and Fixture Extraction Audit 001

**Status:** PASS — DOMAIN A SOURCE SELECTED / FIXTURE EXTRACTION AUDITED
**Scientific execution:** NOT AUTHORIZED
**Date:** 2026-09-20

## 1. Source selection
Selected source family: **Rainbow self-adaptive system**, as specified in the Rainbow architecture and adaptation examples.

Rainbow is a self-adaptive software architecture framework with an explicit architectural model, monitored environment/system properties, adaptation strategies, and execution effects. The adaptation loop is represented independently of TGCV and provides a concrete source model for a self-adaptive-system fixture.

## 2. Fixture-selection principle
The fixture must use a concrete adaptation model in which:
- system/configuration state is explicitly represented;
- candidate adaptation actions/strategies are explicitly specified;
- applicability or strategy preconditions are available before realization;
- strategy effects define successor configurations;
- the adaptation decision is distinct from the resulting configuration.

The fixture must be extracted from the source model rather than invented from TGCV terminology.

## 3. Candidate formal representation
Let `S_t` contain the relevant monitored/configuration variables of the selected Rainbow adaptation model.

Let `A` be the source-defined set of adaptation strategies/actions.

For each action `a`, let `Pre(a)` be its independently specified applicability condition and `Eff(a)` its declared effect.

Derive:

`T_acc,t = { a ∈ A | Pre(a) holds in S_t }`

`T_real,t ∈ T_acc,t`

`S_(t+1) = Apply(S_t,T_real,t)`

This is deliberately the same semantic derivation rule used for Domain B.

## 4. Critical methodological condition
Rainbow must not be represented as a TGCV-specific transformation system by simply renaming adaptation strategies as transformations.

The source-native strategy/action semantics remain primary.

`T_acc` is only a derived analytical view over independently specified source facts.

## 5. Comparator
The baseline comparator is the source-native adaptation representation:

`S_t → adaptation strategy → S_(t+1)`.

The TGCV representation adds the explicit accessibility object:

`T_acc,t = applicable source-defined adaptation strategies`.

The underlying source facts are identical.

## 6. Cross-domain comparability
Domain A and Domain B now share the same semantic skeleton:

`state → independently specified admissible actions → realized action → successor state`.

Domain-specific meanings remain different:
- Domain A: software adaptation/configuration strategies;
- Domain B: robotic movement/planning actions.

The test therefore compares semantic roles, not domain labels.

## 7. Required source-to-fixture traceability
Before freezing, the fixture record must identify for every element:
- source model identifier;
- source state variable;
- source action/strategy;
- source precondition;
- source effect;
- derived `S_t` field;
- derived transformation identity;
- derived accessibility condition;
- derived successor-state rule.

## 8. Required negative/control structure
Domain A must include:
- a state with at least two admissible adaptation strategies;
- a state in which accessibility changes after a realized strategy;
- a null/control transition where the accessible strategy set is unchanged;
- an ambiguity condition in which the source model does not provide enough information and the representation test returns INCONCLUSIVE.

These cases must be derived from the source model, not manufactured after seeing the intended result.

## 9. Audit result
**PASS — DOMAIN A SOURCE BASIS ACCEPTABLE FOR FIXTURE CONSTRUCTION.**

The source family supplies the required self-adaptive-system semantics and supports the same pre-realization accessibility derivation used in Domain B.

However, this audit does not itself freeze a particular Rainbow configuration or authorize execution.

## 10. Remaining construction work
Before scientific execution, the exact source example/configuration, state variables, strategy set, preconditions, effects, fixture size, baseline comparator, equivalence relation and `ΔT_acc` operator must be fixed.

The final cross-domain package must also contain a null/control and ambiguity case and an independent reconstruction worksheet.

## 11. Governance
No frozen TR-131 artifact is modified.
No TGCV Core/RMA/Evidence→Claim Matrix change is authorized.
No scientific execution is authorized.

## 12. Next gate
**CROSS-DOMAIN REPRESENTATION PACKAGE CONSTRUCTION**

Now that both domains have passed source-selection/extraction audit, construct the minimal common representation package, including exact fixtures, source traceability, comparator, null/control, ambiguity case, equivalence relation, and `ΔT_acc` operator.