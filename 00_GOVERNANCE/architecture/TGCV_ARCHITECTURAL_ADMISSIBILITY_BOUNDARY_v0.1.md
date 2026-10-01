# TGCV — Architectural Admissibility Boundary v0.1

**Status:** CURRENT GOVERNANCE / ARCHITECTURAL REDESIGN REQUIRED BEFORE NEW DISCRIMINATOR  
**Date:** 2026-10-01  
**Decision:** ARCH-TRANS-001 / ARCH-DISC-001

## 1. Purpose

The D1 reconstruction audit exposed a deeper governance issue: if the inherited architecture permits any additional relational or transition mechanism to be appended as an auxiliary variable, then an experimental result cannot by itself distinguish a genuinely different architectural object from an extension of A.

This document therefore defines the boundary between:

- an admissible auxiliary representation within the inherited architecture; and
- a modification of the architecture's primary explanatory object.

No experiment is authorized by this document.

## 2. Problem exposed by D1

The current formulation of A permits `S`, `T_acc` and auxiliary mechanisms. D1 introduced `E_tau` as a mechanism controlling future transitions.

Because A can absorb `E_tau` as an auxiliary mechanism, the observed future difference does not establish that transformation-space structure is a distinct primary object.

The problem is therefore not merely fixture design. It is an **architectural admissibility problem**.

## 3. Proposed admissibility boundary

An auxiliary variable may remain inside A only if it satisfies all of the following:

1. **Derivability:** it is derivable from the current A-level objects and declared inputs under a fixed rule;
2. **Non-constitutiveness:** introducing it does not change what A treats as the primary object of explanation;
3. **No new ontology:** it does not introduce a new primitive relational structure whose independent evolution is itself the phenomenon being explained;
4. **No unrestricted escape hatch:** it cannot be added post hoc solely because A failed to represent an observed regularity;
5. **Versioned admissibility:** its inclusion is specified before the discriminating test.

An object that fails these conditions cannot be silently absorbed as an 'auxiliary' variable. Its introduction requires architectural review.

## 4. Consequence for TSDI

Under this boundary, the question becomes more precise:

> Is there an independently observable, dynamically evolving structural object over transformation possibilities whose explanatory role cannot be reduced to a derivable descriptor or auxiliary mechanism of the inherited `S + T_acc` representation without changing the ontology of the primary object?

This is stronger than asking whether relational variables improve prediction.

## 5. Consequence for D1

D1 is **not reopened** by this document.

The current D1 construction remains NON-DISCRIMINATING because its `E_tau` can be treated as an auxiliary transition mechanism.

Any future discriminator must first specify which candidate structural object crosses the admissibility boundary and why.

## 6. Required architectural test before new experiment design

Before selecting another experimental discriminator, governance must establish:

- the complete admissible auxiliary vocabulary of the inherited architecture for the intended test;
- which candidate structural objects are derivable within that vocabulary;
- which candidate objects would constitute an ontological extension;
- a pre-specified rule preventing post-hoc migration of failed A variables into 'auxiliaries'.

Only then can an experiment meaningfully test whether the candidate TSDI object is empirically necessary.

## 7. Current gate

**ARCHITECTURAL DISCRIMINATION GATE: CLOSED — ADMISSIBILITY BOUNDARY REQUIRED.**

Do not design a new fixture, choose N, perform power analysis, select a statistical model or execute a workflow until this boundary is formalized.

## 8. Next governed task

Construct the **Inherited Architecture Admissibility Specification**, including the exact Core definition, allowed auxiliary objects, derivation rules and conditions under which an apparent extension constitutes a Core revision rather than an auxiliary addition.