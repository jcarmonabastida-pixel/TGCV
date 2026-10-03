# TGCV VIATRA V002 Observer Host Build-Readiness Preflight Static Audit 001

Status: STATIC AUDIT COMPLETE — PREFLIGHT CONSTRUCTION NOT YET CLOSED

Date: 2026-10-03

## Purpose

This audit reviews the current `build-readiness-preflight.sh` itself before any further workflow execution.

The objective is to prevent the preflight from becoming a new reactive iteration loop in which:

1. the workflow is launched,
2. the preflight parser fails,
3. the preflight is patched,
4. the workflow is launched again.

That pattern is not considered construction-closed.

## Canonical inputs reviewed

- Branch: `main`
- Preflight: `05_IMPLEMENTATION/viatra-v002-observer-host/build-readiness-preflight.sh`
- Root POM: `05_IMPLEMENTATION/viatra-v002-observer-host/pom.xml`
- Target-definition POM: `target-definition/pom.xml`
- CPS-models POM: `cps-models/pom.xml`
- Observer POM: `observer/pom.xml`
- Target file: `target-definition/tgcv-viatra-v002-target.target`

## Audit result

The current preflight is **not yet construction-closed**.

The repository configuration it checks is internally coherent at the static level reviewed, but the preflight implementation is not sufficiently robust to serve as the final deterministic gate.

### Finding F-01 — shell pipelines can fail before an assertion is reached

The script uses:

- `set -euo pipefail`
- command substitutions containing `sed | head`
- command substitutions containing `grep | sed | tail`

Therefore a parsing pipeline can terminate the entire preflight before the script reaches the explicit `assert_eq` diagnostics.

This is exactly the failure mode observed in run `37121732697`: the log reached:

```
== Build closure audit ==
```

and exited before printing the calculated GAVs or a specific assertion failure.

Consequently, the preflight itself can currently be the source of an apparently structural failure.

**Disposition:** must be eliminated before the next workflow run.

### Finding F-02 — XML is being interpreted with text matching

The current build-closure audit derives Maven coordinates through `sed`, `grep`, and line-window assumptions.

This does not constitute a structural XML parse. It is vulnerable to harmless formatting changes, additional XML elements, or changes in ordering.

The preflight must validate the XML model semantically enough to distinguish:

- project coordinates,
- parent coordinates,
- module declarations,
- plugin declarations,
- target artifact coordinates,
- target-consumer configuration.

**Disposition:** replace coordinate extraction and structural POM checks with a deterministic XML parser, preferably Python's standard-library XML parser. The preflight must remain independent of Maven/Tycho.

### Finding F-03 — the current assertions do not construct a complete reactor model

The script checks selected strings, but it does not construct and validate the complete expected reactor graph.

The deterministic model to validate is:

- root:
  `org.tgcv:viatra-v002-observer-host:0.1.0-SNAPSHOT`
- target:
  `org.tgcv:tgcv-viatra-v002-target:0.1.0-SNAPSHOT`
- CPS aggregator:
  `org.tgcv:tgcv-viatra-v002-cps-models:0.1.0-SNAPSHOT`
- CPS children:
  `org.tgcv:org.eclipse.viatra.examples.cps.model:2.1.0-SNAPSHOT`
  `org.tgcv:org.eclipse.viatra.examples.cps.deployment:2.1.0-SNAPSHOT`
  `org.tgcv:org.eclipse.viatra.examples.cps.traceability:2.1.0-SNAPSHOT`
- observer:
  `org.tgcv:org.tgcv.viatra.v002.observer:0.1.0-SNAPSHOT`

The graph must also prove that each declared module path resolves to exactly the expected POM and that the parent relationship is the intended one.

**Disposition:** add to the redesigned static model audit.

### Finding F-04 — target-coordinate interpolation must be validated by context

The current repository correctly uses:

```
<version>${parent.version}</version>
```

inside the target artifact references of `cps-models` and `observer`.

The preflight should validate the actual XML context of that element, rather than merely asserting that the text occurs and that `${project.version}` does not occur.

This is important because a textual absence/presence test does not prove that the expected target artifact is the value associated with the expected target configuration.

**Disposition:** validate the `target/artifact` subtree structurally.

### Finding F-05 — target immutability is a genuine deterministic contract

The current SHA-256/blob-object identity check for the target file is appropriate as a deterministic pre-Maven check:

`7481dee30f1ae07d7dd9212d7891dc336f1e96ae`

The redesigned preflight should retain it.

### Finding F-06 — Tycho resolution remains outside static proof

No static preflight should claim to prove complete Tycho target-platform resolution.

The correct boundary is:

**Static preflight proves:**

- repository structure,
- pinned materialization contract,
- XML/POM structure,
- reactor coordinates and module graph,
- target artifact identity,
- target-consumer wiring,
- declared OSGi dependency closure,
- immutable target bytes,
- absence of forbidden scientific/runtime execution.

**Maven/Tycho `validate` proves dynamically:**

- Maven model construction as interpreted by Maven,
- Tycho extension loading,
- reactor resolution,
- target-platform resolution,
- actual dependency resolution against the target.

**Full `clean verify` proves later:**

- actual packaging/build execution after the resolution gate passes.

This separation prevents the preflight from trying to emulate Maven.

## Required redesign before next execution

The next implementation must be a single deterministic static audit with these stages:

1. Validate repository structure and materialization prerequisites.
2. Parse the relevant POMs as XML.
3. Build the expected reactor graph in memory.
4. Validate all coordinates and parent relationships.
5. Validate module paths and exact module membership.
6. Validate target-definition identity and filename.
7. Validate target-platform configuration only in the two intended consumers.
8. Validate the target artifact subtree as a structured GAV.
9. Validate historical OSGi manifests and declared provider relationships.
10. Validate target byte identity.
11. Explicitly reject Maven/build/runtime invocation from the preflight.
12. Emit one deterministic PASS/FAIL result with diagnostics tied to a named contract.

No workflow execution is required to validate this redesign.

## Important stale-document finding

The existing `TGCV_VIATRA_V002_OBSERVER_BUILD_CONSTRUCTION_REVIEW_001.md` states that the target reference uses:

```
org.tgcv:tgcv-viatra-v002-target:${project.version}
```

The canonical POMs now use `${parent.version}`.

Therefore that statement is stale and must not be treated as current construction evidence.

## Decision

**Do not launch another build workflow yet.**

The next action is to redesign and statically audit `build-readiness-preflight.sh` itself against this closure model. Only after that redesigned preflight is committed and reviewed should one workflow run be used as the first execution of the gate.

No Maven build, Tycho validation, or runtime execution was performed by this audit.
