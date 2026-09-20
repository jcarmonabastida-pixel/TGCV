# TGCV — Primary Artifact Retrieval and Fixture Identification 001

**Status:** BLOCKED — SOURCE REPOSITORIES VERIFIED, EXACT FIXTURE EXTRACTION REQUIRES ARTIFACT-LEVEL PINNING
**Scientific execution:** NOT AUTHORIZED
**Date:** 2026-09-20

## 1. Retrieval result
Primary repositories/artifact families were located and verified:

- Rainbow: `cmu-able/rainbow`, public Carnegie Mellon repository. The repository identifies itself as Rainbow Self-Adaptive Framework Version Yellow - 3 and contains framework code, Stitch adaptation language, deployments, target definitions, testing infrastructure, and a ZNN target system. citeturn0search0
- ACPBench: `IBM/ACPBench`, public benchmark repository. It explicitly identifies action applicability, progression, reachability and state-transition reasoning as benchmark tasks and states that the benchmark spans thirteen planning domains. citeturn0search2

## 2. Domain A retrieval finding
The Rainbow repository provides concrete candidate artifacts, including:
- `targets/` example target definitions;
- `target-system/znn/` benchmark target system;
- deployment-specific model/strategy material;
- Stitch adaptation-language implementation.

The repository therefore resolves the previous uncertainty about the existence of concrete source artifacts.

However, the canonical construction record does not yet pin one exact target/model/example and its immutable revision. The fixture cannot be frozen until that selection is explicit.

## 3. Domain B retrieval finding
ACPBench provides the formal planning benchmark and its task/domain data. Its public repository confirms that action applicability and progression are first-class tasks over formal planning domains. citeturn0search2

However, the current canonical record still does not pin the exact VisitAll domain/problem artifact and immutable revision required for reproducible extraction.

## 4. Important correction
The previous gate was framed as if source discovery were the remaining uncertainty. It is now clear that the uncertainty is narrower:

**the source families are verified; the exact fixture artifacts are not yet pinned.**

This is an artifact-identification problem, not a theoretical problem.

## 5. Required immutable pin
For each domain, the next fixture record must contain:

### Domain A
- repository: `cmu-able/rainbow`;
- exact commit SHA;
- exact target/model/example path(s);
- exact adaptation strategy/operator identifiers;
- exact source snippets/objects used;
- source-to-fixture mapping.

### Domain B
- repository: `IBM/ACPBench`;
- exact commit SHA or immutable release;
- exact domain/problem path(s);
- exact action/predicate identifiers;
- exact source objects used;
- source-to-fixture mapping.

## 6. No inference from repository existence
Repository-level verification does not justify inventing a fixture from memory or from a secondary description.

The fixture must be extracted from the pinned artifact itself.

## 7. Decision
**BLOCKED — ARTIFACT-LEVEL PINNING REQUIRED.**

No freeze.
No scientific execution.
No result inference.
No TGCV Core/RMA/Evidence→Claim Matrix modification.

## 8. Next gate
**ARTIFACT-LEVEL SOURCE PINNING AND MINIMAL FIXTURE EXTRACTION**

Pin one exact Rainbow target/model and one exact ACPBench VisitAll domain/problem at immutable revisions, then extract the smallest source-faithful fixtures and their complete traceability records.