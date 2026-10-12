# Collective Toy — current baseline fixture 001

**Fixture class:** Current baseline (not historical).  
**Purpose:** Preserve a named, reviewable baseline for the current synthetic diamond model before any future compatibility adapter is proposed.  
**Captured from source commit:** `2a3dc6f1e68d5221199590bb2d64ce8c630d70d5`.  
**Source of expected invariants:** `prototypes/collective_toy/test_collective_toy_engine_001.py`, test `test_diamond_fixture_matches_expected_reachability_and_paths`.  
**Runtime scope:** Current Python engine and current browser/Python cross-runtime suite only.

## 1. Provenance and limits

This is a source-pinned current baseline record, not a preserved export from a prior release. It must not be described as a historical fixture or evidence of cross-version compatibility.

The source commit and expected invariants below are recorded explicitly. This document does not claim a package SHA-256 or result SHA-256: the exact serialized export bytes and their hashes have not been captured as immutable fixture artifacts in this record. Do not derive or invent such hashes from source identifiers.

## 2. Expected semantic invariants

For the current `demo_model()` diamond fixture:

- Baseline reachable states: `["A", "B", "C", "D"]`.
- `block_ac` reachable states: `["A", "B", "D"]`.
- Baseline trajectories ending at `D`: `("A", "B", "D")` and `("A", "C", "D")`.
- `block_ac` trajectories ending at `D`: `("A", "B", "D")`.
- Both scenarios report `truncated == false`.
- Repeated runs on the same input must preserve input and result fingerprints.
- Browser/Python tests compare scenario results and each runtime's own package contract; the browser and Python envelopes are not assumed to have identical schemas.

These are software-level invariants of the synthetic fixture, not measurements of an empirical system and not evidence for TGCV's scientific hypotheses.

## 3. Admission status

| Evidence item | Status |
|---|---|
| Source commit identified | Recorded |
| Semantic invariants defined in tests | Recorded |
| Exact exported package bytes preserved separately | Not yet recorded |
| Package SHA-256 of preserved export | Not yet recorded |
| Result SHA-256 independently frozen as golden value | Not yet recorded |
| Historical engine/schema compatibility | Untested |

## 4. Next capture step

A future fixture-capture change should export the baseline package using the supported deterministic path, preserve the exact bytes as a versioned fixture, and record SHA-256 values calculated from those exact bytes in CI. The expected output fingerprints should be reviewed and frozen separately from the code that generates them. Until that capture is reviewed, this file remains a semantic baseline register only.

No compatibility adapter, promotion to `main`, empirical-data execution, or scientific authorization is implied.
