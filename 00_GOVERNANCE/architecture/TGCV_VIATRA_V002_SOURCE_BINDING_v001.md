# TGCV VIATRA V002 Source Binding v001

## Status

SOURCE BINDING — FROZEN FOR IMPLEMENTATION DESIGN.

## Purpose

Freeze the concrete VIATRA source artifact to which the V002 serial runtime observation implementation is bound.

## Source revision

Canonical VIATRA source revision:

`eb68158a3d74581f69ccb8bc4f47673b12abdf85`

Repository:

`eclipse-viatra/org.eclipse.viatra`

## Transformation binding

The concrete transformation rule is the VIATRA tutorial CPS-to-Deployment HostMapping rule identified as `hostRule`.

Its source-level precondition is:

`HostInstance.instance`

and the corresponding matcher form is:

`HostInstanceMatcher.querySpecification`

The rule action reads:

`HostInstance.nodeIp`

and creates the deployment-side `DeploymentHost` plus the trace association between the CPS source host and the deployment target.

## V002 semantic binding

The observer SHALL bind the concrete activation represented by the canonical V002 fixture:

- CPS source: one `HostInstance`;
- source attribute: `nodeIp = 152.66.102.6`;
- deployment target: one `DeploymentHost`;
- target attribute: `ip = 152.66.102.6`;
- trace: one `CPS2DeploymentTrace`;
- CPS trace reference: the source `HostInstance`;
- Deployment trace reference: the target `DeploymentHost`.

The V002 INITIAL and EXPECTED fixtures are the canonical state boundary for this binding. Their previously verified SHA-256 values remain authoritative.

## Observer boundary

The observer is bound to the activation of `hostRule`, not to an abstract or renamed rule.

It SHALL observe the transition without changing the rule, its precondition, its action semantics, or the canonical fixture artifacts.

## Provenance

The implementation SHALL retain:

- this source-binding revision;
- source repository and source commit;
- canonical V002 fixture revision;
- canonical fixture SHA-256 manifest revision;
- implementation revision;
- instrumentation revision.

Git blob identifiers SHALL NOT substitute for fixture-byte SHA-256 values.

## Scientific boundary

This binding contains no scientific outcome, accessibility, value, utility, reward, or performance variable.

It is an implementation/provenance binding only.

## Boundary

This document does not constitute runtime-equivalence evidence, scientific execution, or execution authorization.

The next gate is review of the concrete observer implementation against this frozen source binding and the V002 serial runtime observation implementation specification.
