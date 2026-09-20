# TGCV — Artifact-Level Source Pinning and Minimal Fixture Extraction 001

**Status:** BLOCKED — ARTIFACT FAMILIES VERIFIED; IMMUTABLE FIXTURE PINS NOT YET ESTABLISHED
**Scientific execution:** NOT AUTHORIZED
**Date:** 2026-09-20

## 1. Verification performed
The primary repositories were rechecked directly:

- Rainbow: `cmu-able/rainbow`, current public default branch `master`. The repository documents the `targets` directory as example target definitions and identifies `target-system/znn` as a benchmark target system. citeturn0search0turn0view0
- ACPBench: `IBM/ACPBench`, current public repository. The repository explicitly defines Action Applicability and Progression over formal planning states/actions. citeturn0search1turn0view1

## 2. Important finding
The repository-level evidence is sufficient to establish the source families, but not sufficient to claim an immutable fixture pin.

GitHub's rendered repository pages expose the branches and artifact families, but the exact source objects needed for the proposed fixtures still have to be pinned at artifact level.

Therefore the prior blocker remains valid.

## 3. Domain B correction
The previous plan treated `VisitAll` as if ACPBench itself necessarily contained the canonical VisitAll PDDL artifact.

The current source evidence instead shows ACPBench as a benchmark/data repository whose tasks are generated from formal planning domains. A separate formal PDDL source can provide the VisitAll domain, but it must be explicitly declared as the fixture's primary source.

A suitable independent source family exists: `AI-Planning/pddl-generators`, whose repository explicitly contains a `visitall` generator. citeturn0search2

However, that generator is not yet pinned to an exact revision and generated problem instance. Therefore it cannot yet be treated as the frozen fixture.

## 4. Domain A correction
Rainbow provides concrete example target definitions and the ZNN benchmark target system. citeturn0view0

Nevertheless, the exact target/configuration/strategy artifact and immutable commit required for the fixture have not yet been pinned.

## 5. Decision
**BLOCKED — DO NOT FREEZE OR EXECUTE.**

The theoretical construction remains viable, but artifact-level reproducibility has not yet been established.

## 6. Next gate
**IMMUTABLE ARTIFACT PINNING**

For Domain A, pin one exact Rainbow target/example and its commit SHA.

For Domain B, choose one exact formal VisitAll PDDL source (or an exact ACPBench instance if the repository itself contains the required domain/problem artifact), pin its commit SHA, and record the exact domain/problem paths.

Only after those pins are recorded should the minimal fixtures be extracted and audited.