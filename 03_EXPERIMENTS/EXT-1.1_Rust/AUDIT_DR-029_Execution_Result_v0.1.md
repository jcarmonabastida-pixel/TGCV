# AUDIT DR-029 — TR-131 Execution Result Audit v0.1

**Status:** INCOMPLETE — EMPIRICAL SIGNAL OBSERVED / INTEGRITY CLOSURE REQUIRED  
**Date:** 2026-09-07  
**Experiment:** EXT-1.1 Rust  
**Decision gate:** DR-030 — TR-131 Real Execution Authorization  
**Captured execution output:** `Pegado text.txt` (797,739 lines)

## 1. Purpose

Audit the captured real-dataset TR-131 execution against DR-029 v0.2 and DR-030. This audit does not replace the execution and does not authorize a scientific PASS until all integrity conditions are closed.

## 2. Captured execution result

The captured output identifies `MODE = REAL_DATASET` and reports:

- origin count: **607,498**
- equivalence classes: **521,282**
- singleton classes: **519,339**
- multi-member classes: **1,943**
- comparable classes: **1,943**
- pair comparisons: **86,216**
- differing classes: **1,760**
- witness count: **56,980**
- witness-list SHA-256: `283dc6cf7433e1a5f368ff9d46642d50e4447066029fb9298e5ddc18cba95c72`

The counts are internally coherent: singleton + multi-member classes = 521,282, and the reported origin count is 607,498.

## 3. Information-firewall audit

The captured output explicitly reports:

- `OUTCOME_READ = false`
- `POST_ORIGIN_ANALYSIS = false`
- `PREDICTIVE_METRICS = false`
- `REACH_READ = false`
- `SAMPLING = false`

Therefore the captured output provides direct evidence that the executor did not activate those prohibited analytical paths.

## 4. Scientific discriminating signal

The execution reports 1,760 B-equivalence classes containing differing canonical T_acc representations and 56,980 witness pairs. Multiple reported witnesses have equal B and equal T_acc cardinality but different T_acc hashes. For example, the captured output contains a witness with B = `(version_str=14.2.0, prior_release_count=0, package_age_days=0.0, dependency_count=7)` and two origins whose T_acc counts are both 7 but whose canonical T_acc hashes differ.

This is the required *type* of TR-131 counterexample: same frozen B, different T_acc membership, without relying on cardinality alone.

## 5. Integrity limitation requiring closure

The frozen executor at commit `5c4208f6181af7fba30fa195a3e6a193bab55636` defines canonicalization as:

`tuple(sorted(set(rows), ...))`

Consequently, an exact duplicate transformation row would be silently collapsed rather than causing the fail-closed integrity condition required by the DR-029 implementation protocol.

The captured output contains no explicit duplicate-transformation integrity field or assertion, nor does it contain an explicit dataset hash, runtime metadata block, or replay-equality result. Therefore the execution-result audit cannot close every DR-030 acceptance condition from the captured output alone.

A prior structural audit (DR-026A) reported zero duplicate canonical T_acc relations for the frozen Rust structural snapshot. That is relevant supporting evidence, but the TR-131 executor itself did not enforce this condition during the captured run. Accordingly, this audit records the issue rather than silently treating it as closed.

## 6. Decision

**TR-131 scientific PASS is NOT yet declared.**

The captured run establishes a strong empirical signal consistent with TR-131 support: there are many B-equivalent origins with different T_acc membership representations, including equal-cardinality/different-membership witnesses. However, the result remains **integrity-pending** until the duplicate-canonicalization condition and the missing execution provenance/replay requirements are explicitly closed.

## 7. Required next action

1. Patch the executor so duplicate canonical T_acc transformations fail closed rather than being silently collapsed.
2. Preserve the frozen B and T_acc definitions; no analytical redesign is permitted.
3. Run the synthetic conformance suite again.
4. Issue a new explicit execution authorization for the patched executor.
5. Re-execute the exhaustive real-dataset census and capture complete stdout/stderr plus provenance metadata.
6. If the rerun reproduces the same structural result, close TR-131 as **PASS — T_acc irreducibility supported relative to frozen B**, subject to the exact DR-029 decision wording.

## 8. Source evidence

The captured execution output is the user-supplied `Pegado text.txt`; its first lines identify REAL_DATASET mode, the firewall flags, and the complete aggregate counts, while its tail confirms the witness records continue through the end of the 797,739-line capture.

The executor source is frozen in GitHub at commit `5c4208f6181af7fba30fa195a3e6a193bab55636` and contains the canonicalization behavior described above.
