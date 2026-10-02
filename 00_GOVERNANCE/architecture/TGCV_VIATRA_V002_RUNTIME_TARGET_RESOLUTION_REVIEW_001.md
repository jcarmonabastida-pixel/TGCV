# TGCV VIATRA V002 Runtime Target Resolution Review 001

**Status:** RESOLVED — canonical runtime target identified  
**Date:** 2026-10-02  
**Core revision:** ffa111dbb160c0bc55e89ea16430e97a38908662  
**Examples revision:** 15f269dbf74000eac7b97cf7f92e256b8fb1fc1c

## Decision

The canonical runtime target for the v002 minimal fixture is the concrete event-driven CPS-to-Deployment transformation in the VIATRA examples repository, specifically the HostMapping rule in:

cps/transformations/org.eclipse.viatra.examples.cps.xform.m2m.incr.expl/src/org/eclipse/viatra/examples/cps/xform/m2m/incr/expl/rules/HostRules.xtend

The previously identified CPS2DeploymentTransformationViatra implementation in the ...incr.viatra package is not the target used to define the v002 fixture semantics.

## Evidence

The canonical v002 fixture specification explicitly names:

- transformation entry point: ...cps.xform.m2m.incr.expl/.../CPS2DeploymentTransformation.xtend;
- host rules: ...cps.xform.m2m.incr.expl/.../rules/HostRules.xtend;
- concrete rule: HostMapping;
- relevant query: unmappedHostInstance;
- expected activation: HostMapping(CREATED).

The specification also states that the complete transformation registers host, application, state-machine, state, transition and trigger rule groups, while the minimal fixture is constructed so that only the HostMapping CREATED activation is relevant.

## Resolution of apparent implementation ambiguity

The repository contains another VIATRA implementation under ...incr.viatra, including CPS2DeploymentTransformationViatra and its hostRule. That implementation is not silently substituted for the concrete example selected by the v002 fixture specification.

The runtime preflight must therefore instantiate the expl/event-driven HostMapping path selected by the fixture specification, not merely any implementation producing an observationally similar DeploymentHost.

## Consequence for the runner

The dedicated TGCV runtime adapter must:

1. load the three concrete metamodels;
2. load the frozen CPS, Deployment and CPSToDeployment XMI fixture;
3. instantiate the selected expl transformation path;
4. inspect the unmappedHostInstance activation before execution;
5. verify the single binding Rawsberry.PI / Aragorn;
6. execute the CREATED activation;
7. inspect the resulting DeploymentHost and CPS2DeploymentTrace;
8. compare the semantic post-state with the frozen expected projection;
9. emit the required JSON result;
10. fail closed on any target-path, activation-count, structural, semantic or contamination mismatch.

No scientific execution is authorized by this review.

## Status

**RESOLVED.**

The earlier implementation ambiguity is no longer a blocker. The next implementation step is the dedicated runtime adapter against the resolved HostMapping target.
