# TI-001 V011 Experiment Specification 001

**Status:** SPECIFICATION — FIXTURE NOT GENERATED / EXECUTION NOT AUTHORIZED

## 1. Research question

Does the treatment-control difference in the probability of selecting A persist when presentation orientation is explicitly balanced and analyzed separately?

Secondary question: how does presentation orientation relate to the decision distribution within each condition?

## 2. Experimental object

V011 remains a decision-level Transformational Intelligence experiment.

Each decision unit presents:
- context;
- available_actions containing exactly A and B;
- future_structure.

The agent must select exactly one action, producing exactly A or B.

No value, reward, utility, performance, task success, successor realization, or external outcome is part of the experimental object.

## 3. Population and pair structure

The canonical candidate fixture shall contain:

- 210 unique pairs;
- 420 decision units;
- 70 pairs per condition: control, treatment, null;
- 35 pairs per condition × presentation cell;
- every pair contains exactly two decision units;
- each pair contains exactly one I1_FIRST unit and one I2_FIRST unit.

This produces an exactly balanced decision-unit factorial population:

| Condition | I1_FIRST | I2_FIRST | Total |
|---|---:|---:|---:|
| control | 70 | 70 | 140 |
| treatment | 70 | 70 | 140 |
| null | 70 | 70 | 140 |
| **Total** | **210** | **210** | **420** |

The pair-level allocation is also balanced:

| Condition | Pairs |
|---|---:|
| control | 70 |
| treatment | 70 |
| null | 70 |
| **Total** | **210** |

## 4. Pair semantics

Within each pair, the underlying decision scenario is held constant except for the presentation orientation defined by the fixture.

Each pair has:
- one I1_FIRST decision unit;
- one I2_FIRST decision unit;
- one condition identity.

Pair identity is hidden from the model and is used only for analysis.

## 5. Deterministic fixture generation

The fixture generator must use a fixed, explicitly recorded seed.

The seed must be bound into the fixture-generation specification and reproducibility manifest before fixture generation.

Generation must be deterministic: identical generator source, specification, and seed must reconstruct the identical fixture byte-for-byte.

No fixture may be generated before the corresponding pre-generation integrity gate is defined and passed.

## 6. Presentation balancing

Presentation orientation is not left to uncontrolled model interaction.

The canonical candidate fixture must contain exactly:
- 210 I1_FIRST decision units;
- 210 I2_FIRST decision units.

Within each condition:
- 70 I1_FIRST units;
- 70 I2_FIRST units.

The pair construction guarantees one unit of each orientation per pair.

## 7. Conditions

### Control

The future-structure information specified by the fixture is absent according to the frozen control definition.

### Treatment

The future-structure information specified by the fixture is available according to the frozen treatment definition.

### Null

The null condition follows the frozen null construction defined in the fixture specification.

The exact content of each condition must be frozen before fixture generation and may not be inferred or changed during analysis.

## 8. Primary estimands

For each execution independently:

### 8.1 Overall treatment-control contrast

`TI_DC = q_A(treatment) - q_A(control)`

where `q_A` is the proportion of valid decisions selecting A.

### 8.2 Presentation-stratified treatment-control contrasts

For each presentation orientation `p`:

`TI_DC(p) = q_A(treatment,p) - q_A(control,p)`

The two orientation-specific contrasts are primary diagnostic estimands for V011 because V010 showed a pronounced presentation-stratified pattern.

### 8.3 Presentation contrast within condition

For each condition `c`:

`P_D(c) = q_A(c,I1_FIRST) - q_A(c,I2_FIRST)`

These are descriptive estimands used to characterize presentation dependence.

### 8.4 Null-control contrast

Overall:

`TI_NULL = q_A(null) - q_A(control)`

And, descriptively, by presentation:

`TI_NULL(p) = q_A(null,p) - q_A(control,p)`

## 9. Required analysis outputs

For each independent execution:

1. valid/invalid/incomplete counts;
2. A/B counts and `q_A` overall by condition;
3. `TI_DC` and `TI_NULL`;
4. A/B counts and `q_A` by condition × presentation;
5. `TI_DC(I1_FIRST)` and `TI_DC(I2_FIRST)`;
6. presentation contrast within each condition;
7. pair agreement/disagreement;
8. missing response identifiers;
9. execution/runtime metadata and exact fixture/interface bindings.

Executor-1 and Executor-2 results must remain separate.

## 10. Reproducibility rule

Executor-1 and Executor-2 are independent executions.

V011 must not use:
- pooling;
- averaging across executors;
- majority vote;
- recoding;
- retry;
- imputation;
- post-hoc exclusion based on observed outputs.

Differences between independent executions are reported as execution-level observations.

Bit-for-bit equality is not a requirement unless a future design explicitly introduces deterministic response constraints.

## 11. Decision interface boundary

The model-facing interface must be frozen independently before execution.

The visible input shall contain only the fields explicitly authorized by the interface specification.

Hidden provenance fields must not be model-visible.

The output validator must accept exactly A or B after the predefined whitespace normalization rule and must not interpret, extract, repair, retry, or recode other output.

## 12. Scientific interpretation boundary

V011 can establish only decision-level observations within the frozen fixture/interface/runtime.

It cannot by itself establish:
- a causal effect of future structure;
- a value/reward/utility effect;
- a performance or task-success effect;
- a general capability beyond the tested configuration;
- a single pooled effect across independent executions.

## 13. Required pre-execution gates

Before any scientific execution:

1. fixture generator specification gate;
2. fixture generation and integrity gate;
3. decision-interface specification and compatibility preflight;
4. scientific execution contract;
5. Executor-1 identity preflight;
6. final preauthorization gate;
7. explicit scientific authorization;
8. Executor-1 primary audit;
9. Executor-2 replay gate and authorization;
10. replay audit/comparison;
11. scientific analysis specification and authorization;
12. deterministic analysis;
13. scientific analysis audit;
14. controlled interpretation;
15. scientific closure.

## 14. Current disposition

This specification freezes the proposed V011 experimental design at the conceptual level.

**No V011 fixture has been generated.**

**No V011 scientific execution is authorized.**

The next action is to define the deterministic fixture-generation specification and select/freeze its seed before any generator implementation or fixture creation.
