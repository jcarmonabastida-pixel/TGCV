# TGCV — O4 Structural Connectivity Object Specification v0.1

**Status:** GOVERNANCE SPECIFICATION / PRE-EXPERIMENTAL / NO AUTHORIZATION
**Date:** 2026-10-01
**Decision:** ARCH-TRANS-001

## 1. Purpose

Convert O4 from an informal phrase (connectivity/topology/reconfiguration) into a candidate operational object that can be subjected to the inherited-architecture admissibility test.

This document does not claim that O4 is non-reducible, causally relevant, or part of a new Core.

## 2. Candidate object

Define the candidate structural object at observation time t as:

`G_t = (V_t, E_t)`

where V_t is the frozen set of transformation identities under observation and E_t is a binary relation indicating whether a pre-specified transformation-to-transformation structural adjacency exists at time t.

The relevant structural change is:

`Delta G_t = (Delta V_t, Delta E_t)`

with particular attention to cases where V_t remains constant while E_t changes.

## 3. Independence requirement

O4 is admissible as a candidate architectural object only if E_t is observed or measured independently of the future outcome used to test its explanatory relevance.

The edge relation must therefore be defined by a frozen measurement rule that does not use future trajectory success, future value or utility, the statistical outcome of the eventual test, or post-hoc edge selection.

## 4. A-reconstruction test

The decisive governance test is whether:

`E_t = f(S_t,C_t,L_t,T_acc,t,I_fixed)`

under the inherited admissibility rules.

Three outcomes are permitted:

### A-equivalent
Exact reconstruction is possible under the frozen A representation. Disposition: O4 remains an admissible derived descriptor; no architectural inference.

### Non-equivalent
Exact reconstruction is impossible under the frozen A representation and declared auxiliary vocabulary. Disposition: O4 becomes architecturally non-equivalent, but no scientific claim follows yet.

### Underdetermined
The available evidence does not establish either reconstruction or non-reconstructibility. Disposition: no architectural inference; additional evidence would be required.

## 5. Structural-change criterion

A candidate O4 instance is structurally informative only if there exists at least one matched observation pair satisfying:

`V_t^(1) = V_t^(2)`

and

`E_t^(1) != E_t^(2)`

without changing the inherited state/context representation in a way that simply encodes the edge difference.

This criterion is methodological, not an empirical finding.

## 6. Separation from T_acc

O4 must not be defined as a disguised accessibility set.

An edge cannot mean merely that both transformations are accessible; graph degree cannot be defined solely as a count of accessible transformations; and connectivity cannot be computed from T_acc using an arbitrary fixed pairing and then presented as an independent object.

If O4 is deterministically generated from T_acc by the measurement rule, it is A-equivalent by construction.

## 7. Separation from future outcome

The structural object must be frozen before the future trajectory is observed.

The eventual experimental outcome may test whether O4 carries explanatory information, but it may not define O4.

## 8. Current evidence status

The existing architectural transition assessment identifies MT5 and RUST-DYN-2 as relevant evidence streams for structural connectivity/reconfiguration, while explicitly noting that they do not yet establish non-reconstructibility from A.

Accordingly, O4 is a candidate object under admissibility review, not an established architectural primitive.

## 9. Deliberate exclusions

This specification does not define the concrete edge semantics, a domain or dataset, a fixture, sample size, effect size, statistical model, workflow, scientific execution, Core revision, or Matrix revision.

## 10. Next gate

The next governance task is a pre-experimental O4 reconstruction audit: determine whether the candidate edge relation can be independently defined and whether its information is already derivable from the inherited representation.

No experiment is authorized by this document.
