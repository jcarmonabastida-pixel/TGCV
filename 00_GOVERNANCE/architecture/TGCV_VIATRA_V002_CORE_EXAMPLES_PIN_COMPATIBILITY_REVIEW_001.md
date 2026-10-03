# TGCV VIATRA V002 Core/Examples Pin Compatibility Review 001

## Status

**SUPERSEDED — HISTORICAL RUNTIME-EQUIVALENCE PIN REVIEW**

This blocked review belongs to the earlier runtime-equivalence chain using core `ffa111db...` and examples `15f269db...`. It is retained as execution history and does not describe the current Observer Host build chain.

## Observed execution

Workflow run: 37026491901

Pinned revisions:
- VIATRA core: `ffa111dbb160c0bc55e89ea16430e97a38908662`
- VIATRA examples: `15f269dbf74000eac7b97cf7f92e256b8fb1fc1c`

The build reached the Maven build stage successfully. Java 11 toolchain resolution also passed.

The failure was:

`org.eclipse.viatra:viatra-maven-plugin:2.9.0-SNAPSHOT` could not be resolved from the configured VIATRA Maven repository.

## Root cause

The pinned examples revision is a 2.9.0-SNAPSHOT CPS demonstrator. Its `cps/pom.xml` declares:

`<viatra.compiler.version>2.9.0-SNAPSHOT</viatra.compiler.version>`

The pinned core revision is from the 2.10.0 development line. Its core parent POM declares version 2.10.0-SNAPSHOT, while the previous core commit immediately before the 2.10.0 version bump is:

`6f7d2d7860ed901c33029700387d3535bd2553f1`

At that revision, `org.eclipse.viatra.parent.core` declares version 2.9.0-SNAPSHOT and includes the VIATRA Maven plugin module.

The 2.10.0 version bump commit is `d217e0f8cec8fecea01690ef59185ee1cb985bb7`, whose parent is `6f7d2d7860ed901c33029700387d3535bd2553f1`.

Therefore the current pair is not a reproducibly compatible core/examples pair for this build path.

## Evidence

- Examples revision `15f269dbf74000eac7b97cf7f92e256b8fb1fc1c`: CPS parent version 2.9.0-SNAPSHOT and VIATRA compiler version 2.9.0-SNAPSHOT.
- Core revision `6f7d2d7860ed901c33029700387d3535bd2553f1`: core parent version 2.9.0-SNAPSHOT and Maven plugin included in the core reactor.
- Core revision `ffa111dbb160c0bc55e89ea16430e97a38908662`: 2.10.0 development line.
- Workflow run `37026491901`: build failure caused by unresolved `viatra-maven-plugin:2.9.0-SNAPSHOT`.

## Decision boundary

Do not execute the dedicated runtime adapter until a compatible core/examples pair is frozen.

Candidate compatible core revision identified by this review:
`6f7d2d7860ed901c33029700387d3535bd2553f1`

This candidate must be explicitly incorporated into the runtime-equivalence preflight contract before execution.

## Scientific status

No scientific execution occurred. The runtime adapter was skipped because the pinned implementation could not be built.
