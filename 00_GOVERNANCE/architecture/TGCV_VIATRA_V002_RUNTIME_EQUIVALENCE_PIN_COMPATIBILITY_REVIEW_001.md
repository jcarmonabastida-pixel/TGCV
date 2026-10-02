# TGCV VIATRA v002 Runtime Equivalence Pin Compatibility Review v001

**Status:** REVIEWED — current preflight pins are incompatible.

## Evidence

The current runtime-equivalence specification pins:

- VIATRA core: `ffa111dbb160c0bc55e89ea16430e97a38908662`
- VIATRA examples: `15f269dbf74000eac7b97cf7f92e256b8fb1fc1c`

The examples POM at the pinned examples revision declares:

`viatra.compiler.version = 2.9.0-SNAPSHOT`

The core revision currently pinned belongs to the 2.10 development line. The 2.10 version bump commit is:

`d217e0f8cec8fecea01690ef59185ee1cb985bb7`

Its direct parent is:

`6f7d2d7860ed901c33029700387d3535bd2553f1`

At that parent revision, the core parent is still 2.9.0-SNAPSHOT and includes the VIATRA Maven plugin reactor module.

## Decision

The compatible core candidate for the already frozen examples revision is:

`6f7d2d7860ed901c33029700387d3535bd2553f1`

This candidate must replace the current core pin in the runtime-equivalence preflight contract and workflow before another execution.

No runtime-equivalence PASS is claimed from the failed run.

## Required next action

Update the v001 specification and manual workflow to use the compatible core revision, preserving the examples revision and all other gates. Then commit the change and perform one controlled manual dispatch.

No scientific execution is authorized by this change.
