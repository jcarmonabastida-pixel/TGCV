# TGCV — Immutable Artifact Pinning 001

**Status:** BLOCKED — PRIMARY ARTIFACTS IDENTIFIED, BUT THIS REVIEW DOES NOT YET ESTABLISH IMMUTABLE FIXTURE PINS
**Scientific execution:** NOT AUTHORIZED
**Date:** 2026-09-20

## 1. Source verification
The external verification confirms that Rainbow is maintained as `cmu-able/rainbow` and contains concrete target artifacts, including `targets/` and the ZNN target system. citeturn0search0

The external verification also confirms that `AI-Planning/pddl-generators` contains a `visitall` generator and that the generator collection has a citable Zenodo release (v1, DOI 10.5281/zenodo.6382174). citeturn0search1turn0search6

ACPBench independently confirms the relevant planning semantics: action applicability and progression are defined over formal planning states/actions. citeturn0search4

## 2. What can and cannot be pinned from the present evidence
The repository-level and release-level evidence is sufficient to identify the primary artifact families.

It is not sufficient, by itself, to establish the exact immutable content of the proposed fixtures.

An exact fixture pin requires, at minimum:
- immutable source revision;
- exact source path(s);
- exact source object identifiers;
- exact generated instance, if a generator is used;
- a reproducible mapping from source object to fixture element.

## 3. Domain B — preferred pinning route
The cleanest route is to use a released PDDL-generator artifact rather than an unpinned live generator.

Candidate immutable source: **PDDL Generators v1**, Zenodo DOI `10.5281/zenodo.6382174`. The associated repository explicitly contains `visitall`. citeturn0search1turn0search6

However, the exact VisitAll generated instance still has to be selected and its complete source bytes/hash recorded. The release alone is not the fixture.

## 4. Domain A — required pin
For Rainbow, the repository identifies `targets/` and `target-system/znn`, but the current canonical TGCV record still lacks a verified exact target path + source revision + extracted source object set.

The fixture therefore remains unpinned.

## 5. Decision
**BLOCKED — IMMUTABLE FIXTURE PIN NOT ESTABLISHED.**

This is not a failure of the representation hypothesis. It is a reproducibility gate.

No scientific execution.
No fixture freeze.
No inference about `T_acc` or `ΔT_acc`.
No Core/RMA/Evidence→Claim Matrix change.

## 6. Next gate
**EXACT SOURCE OBJECT EXTRACTION AND HASH RECORD**

Extract the exact source objects for one Rainbow fixture and one VisitAll fixture, compute their content hashes, record the immutable source revision/path, and create the source-to-fixture traceability record.

Only after that record passes audit should the candidate representation package be frozen.