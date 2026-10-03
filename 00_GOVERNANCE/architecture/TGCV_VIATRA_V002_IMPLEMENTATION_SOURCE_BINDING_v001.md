# TGCV VIATRA V002 Implementation Source Binding v001

## Status

SOURCE BINDING — FROZEN.

## Canonical source

Repository: `eclipse-viatra/org.eclipse.viatra`

Revision: `ffa111dbb160c0bc55e89ea16430e97a38908662`

Source artifact:

`documentation/org.eclipse.viatra.documentation.help/src/main/asciidoc/tutorial/batch-transformations.adoc`

## Concrete rule

The implementation target is the tutorial CPS-to-Deployment batch transformation rule:

`hostRule`

Its concrete construction is:

`createRule(HostInstance.instance).action[ ... ].build`

The action obtains the matched source object through:

`it.hostInstance`

and reads:

`cpsHostInstance.nodeIp`

## Concrete state mutation

The reference action performs the following semantic operations, in order:

1. creates a `DeploymentHost` under the deployment model;
2. sets `DeploymentHost.ip` to the source `HostInstance.nodeIp`;
3. creates a `CPS2DeploymentTrace`;
4. adds the matched CPS `HostInstance` to `CPS2DeploymentTrace.cpsElements`;
5. adds the created `DeploymentHost` to `CPS2DeploymentTrace.deploymentElements`.

For V002, the canonical fixture binds this activation to:

`nodeIp = 152.66.102.6`

and therefore to:

`DeploymentHost.ip = 152.66.102.6`.

## Activation boundary

The observer implementation SHALL regard one firing of `hostRule` as one activation instance.

The observation lifecycle SHALL be conceptually:

`TRANSFORMATION_BEGIN → hostRule activation → TRANSFORMATION_END`

The observer SHALL capture the pre-state before the rule action mutates the model and the post-state after the action has completed.

The observer SHALL NOT alter rule scheduling, matching, action semantics, or fixture content.

## Execution reference

The tutorial executes the rule through:

`hostRule.fireAllCurrent`

The V002 minimal observer MUST remain scoped to the single intended `HostInstance` activation and MUST NOT aggregate multiple rule firings.

## Required implementation evidence

A concrete observer implementation derived from this binding SHALL demonstrate:

- unique identification of the selected `hostRule` activation;
- deterministic PRE-state capture;
- deterministic POST-state capture;
- event ordering;
- canonical state digests;
- activation identity;
- fixture/source provenance;
- instrumentation provenance.

## Canonical fixture binding

The implementation is bound to the V002 canonical fixture set:

- CPS;
- Deployment INITIAL;
- Deployment EXPECTED;
- Traceability INITIAL;
- Traceability EXPECTED.

The independently verified SHA-256 manifest for these artifacts remains authoritative.

## Scientific firewall

The source binding and observer SHALL not introduce:

- U_t;
- T_acc;
- accessibility labels;
- future assignment;
- utility;
- reward;
- value;
- scientific performance metrics.

## Boundary

This document freezes the implementation source boundary only.

It does not constitute runtime-equivalence evidence, scientific execution, or execution authorization.

The next gate is implementation review/preflight against this frozen source binding and the V002 Serial Runtime Observation Implementation Specification.
