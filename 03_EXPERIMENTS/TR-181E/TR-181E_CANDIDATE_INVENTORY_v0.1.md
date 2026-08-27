# TR-181E — Candidate Transformation Inventory v0.1

**Status:** PRE-REGISTRATION DRAFT — NOT FROZEN

## Purpose

Define a finite, auditable candidate universe `T` for TR-181E without using empirical outcomes to construct or prune candidates.

## Design rule

The inventory is deliberately minimal. A candidate is included only when its transformation semantics and pre-outcome realisation condition can be stated explicitly. The inventory is not intended to enumerate every conceivable transformation.

## Candidate families

### ACTIVATE
Introduce or activate a capability already represented as available in the system/context.

Operational precondition: target capability/component is present but inactive and the activation action is permitted.

### COMPOSE
Combine two or more existing compatible components into a new configuration.

Operational precondition: all declared components exist and the compatibility condition is satisfied.

### RECONFIGURE
Change the configuration of an existing component without introducing a new component.

Operational precondition: target component exists and the declared configuration change is permitted under the frozen resource/context constraints.

### ACQUIRE
Obtain a capability/resource not currently available from the baseline configuration, where acquisition is part of the declared candidate universe.

Operational precondition: the acquisition route is declared and its pre-outcome resource/constraint requirements are satisfied.

### LEARN
Acquire or update a system capability through a declared learning mechanism.

Operational precondition: the learning mechanism is available and its declared preconditions are satisfied.

### RECOMBINE
Re-use existing elements in a materially different arrangement or role without introducing a new primitive component.

Operational precondition: required elements exist and the declared recombination constraint is satisfied.

## Candidate schema

Each concrete candidate must instantiate:

`<id, class, target, pre, resource, eff>`

where `id` is unique, `class` is one of the six controlled labels above, `target` is explicit, `pre` contains only pre-outcome predicates, `resource` contains explicit requirements, and `eff` is descriptive metadata rather than an input to recursive accessibility computation.

## Inclusion/exclusion rule

Include a candidate only if:

1. its target is explicit;
2. its class is unambiguous;
3. every accessibility condition is evaluable from frozen pre-outcome information;
4. it can be represented without inspecting outcome or future trajectory;
5. its inclusion does not depend on empirical performance.

Exclude any candidate whose accessibility can only be established retrospectively or whose definition requires an observed result.

## Critical limitation

This document defines the candidate construction grammar and family-level inventory, not yet the final instance-level list. The final list must be generated from a frozen scenario/state schema and must be recorded before test evaluation.

## Decision

**Candidate-family inventory:** ACCEPTED FOR INSTANCE CONSTRUCTION

**Instance-level universe T:** NOT YET FROZEN

**R freeze:** NO-GO

**Experiment:** BLOCKED until instance-level candidates, predicates, thresholds and serialization are frozen.
