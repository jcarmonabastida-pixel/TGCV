# TI-001 V011 Experiment Design Derivation 001

**Status:** DESIGN PROPOSAL — NO FIXTURE, PREFLIGHT, OR EXECUTION AUTHORIZED

## Purpose

Derive the next falsifiable experiment from the two concrete findings retained from TI-001 V010:

1. a pronounced presentation-stratified difference between `I1_FIRST` and `I2_FIRST`;
2. variation in the treatment-control indicator across independent executions.

The purpose is to separate these two sources of variation before making any stronger claim about transformational intelligence.

## Design question

The primary design question is:

> Does the observed treatment-control decision difference persist when presentation orientation is explicitly balanced and independently controlled?

A secondary methodological question is:

> How much of the observed decision variation is attributable to presentation orientation versus independent execution variation?

## Proposed experimental structure

V011 should use a factorial structure with:

- condition: control / treatment / null;
- presentation orientation: I1_FIRST / I2_FIRST;
- independent execution: Executor-1 / Executor-2;
- identical frozen decision fixture across executors;
- identical model-facing decision interface across executors.

The analysis must preserve all factors rather than collapse them into a single pooled estimate.

## Primary estimands

For each execution separately:

1. treatment-control difference in q_A within `I1_FIRST`;
2. treatment-control difference in q_A within `I2_FIRST`;
3. overall treatment-control difference;
4. presentation difference within each experimental condition.

The primary interpretation should focus on whether the treatment-control contrast remains directionally and materially present after presentation stratification.

## Reproducibility requirement

Executor-1 and Executor-2 remain independent.

No averaging, pooling, majority vote, recoding, retry, or post-hoc selection is permitted.

The design should define in advance how execution-level discrepancies are reported. It must not require bit-for-bit equality unless a deterministic response protocol is explicitly part of the new design.

## Scope boundary

V011 remains a decision-level experiment.

It does not introduce value, reward, utility, performance, task-success, or external outcome measures unless a separate design gate explicitly authorizes such an extension.

It does not claim to test `delta_tacc -> value`.

## Required design gates before fixture generation

Before any V011 fixture is generated, the following must be formalized and separately gated:

1. exact factorial population and pair structure;
2. presentation randomization/balancing rule;
3. decision interface and visible-field contract;
4. executor independence boundary;
5. runtime configuration;
6. predefined estimands and analysis rules;
7. reproducibility/reporting rule;
8. canonical fixture identity and hash binding;
9. preflight criteria;
10. explicit scientific authorization.

## Current disposition

This document is a design derivation only.

**No V011 fixture exists.**

**No V011 scientific execution is authorized.**

The next action is to formalize the V011 experimental design specification, including exact population counts and randomization rules, before implementation.
