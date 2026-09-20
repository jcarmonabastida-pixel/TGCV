# TGCV TR-131 — RE-FREEZE PACKAGE DELTA AUDIT 001

**Status: BLOCKED — SCIENTIFIC CANDIDATE STILL USES SYNTHETIC BASELINE**

## 1. Purpose

Determine the minimum package change required to replace the previous synthetic scientific fixture with the newly verified exact-source VisitAll/Rainbow fixture before any new Freeze Audit or G8 authorization.

## 2. Canonical evidence inspected

The current candidate manifest declares:

- `TR-131_FREEZE_CANDIDATE_MANIFEST_v02.json`
- `tr131_scientific_runner_v02.py`
- `scientific_policy_definitions.json`
- `scientific_execution_config_v01.json`

The exact-source fixture and PREFLIGHT records are already PASS.

## 3. Blocking mismatch

The current scientific runner still defines its baseline internally:

- `S0 = {node: S0, resources: 1, status: ready}`
- `C = {context: frozen, version: 1}`
- `T_acc = {tau_accept, tau_defer}`

and its policy definitions select:

- `tau_accept`
- `tau_defer`

These are not the exact VisitAll or Rainbow source transformations established by the new source lock.

Therefore the current scientific runner is **not the exact-source fixture**.

The candidate manifest's baseline hashes:

- S0: `f172e9a705a27d73b864f6ce34e0c6b6cdf9f18bf1e61a646f2d81efdd40ec0a`
- C: `0aefc336bb0509d6403b51449c07f75a08b83d69137823e4653437a63164af43`
- T_acc: `0b5d8211831f6f2701578dc4a91d82ce63a4192422f66fee7aae856e9ba539b9`

are consequently hashes of the synthetic scientific baseline, not of the exact-source fixture.

## 4. Consequence

A new freeze cannot legitimately be created merely by adding the exact-source PREFLIGHT report to the existing package.

Doing so would produce a package in which:

**PREFLIGHT fixture ≠ scientific runner baseline**

and would therefore break the required traceability from the authorized fixture to the executed scientific object.

## 5. Minimum required change

The scientific runner must be replaced or refactored so that its executable scientific baseline is derived exclusively from the exact source-lock fixture.

At minimum:

1. eliminate the internally invented `S0/C/T_acc` baseline;
2. load the exact source-lock record;
3. derive the VisitAll and Rainbow source states and accessible transformations from that locked representation;
4. define the scientific realization policy over the resulting source-defined transformation space;
5. ensure the selected `T_real` is an actual member of the corresponding `T_acc`;
6. update trace and hash construction accordingly;
7. regenerate candidate hashes;
8. independently reconstruct the resulting package with Executor-2;
9. only then perform the new Freeze Audit and G8 authorization.

## 6. Important methodological boundary

The current source lock establishes **structural fixture equivalence**, not a ready-made causal realization policy.

It does not authorize us to invent mappings such as:

`tau_accept = TIncDimmer`

or

`tau_defer = TRemoveServer`

without an explicit methodological justification.

Such a mapping would alter the scientific fixture and therefore must be specified and frozen before execution.

## 7. Gate disposition

**RE-FREEZE PACKAGE DELTA AUDIT: BLOCKED**

The blocker is precise and local:

**the scientific runner still executes a synthetic baseline that is different from the exact-source fixture whose PREFLIGHT has passed.**

No scientific execution is authorized.

No G8 record is created or modified.

## 8. Next gate

**EXACT-SOURCE SCIENTIFIC RUNNER RECONSTRUCTION DESIGN**

Before implementation, define the minimal domain-preserving realization interface that permits X to select a source-defined transformation without inventing cross-domain semantics.

