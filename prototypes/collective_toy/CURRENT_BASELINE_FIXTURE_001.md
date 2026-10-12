# Collective Toy — current baseline fixture 001

**Record status:** SUPERSEDED for frozen package fingerprints by `CURRENT_BASELINE_FIXTURE_002.md`.  
**Fixture class:** Original semantic baseline register (not historical).  
**Purpose:** Preserve a named, reviewable baseline for the current synthetic diamond model before any future compatibility adapter is proposed.  
**Captured from source commit:** `2a3dc6f1e68d5221199590bb2d64ce8c630d70d5`.  
**Source of expected invariants:** `prototypes/collective_toy/test_collective_toy_engine_001.py`, test `test_diamond_fixture_matches_expected_reachability_and_paths`.  
**Runtime scope:** Current Python engine and current browser/Python cross-runtime suite only.

## 1. Provenance and limits

This is the earlier source-pinned semantic baseline register, not a preserved export from a prior release. It must not be described as a historical fixture or evidence of cross-version compatibility. Its statements that exact export bytes and package/result fingerprints were not yet recorded describe the state of this record at that revision only.

The later `CURRENT_BASELINE_FIXTURE_002.md` records the separately preserved package bytes and frozen file/package/input/result fingerprints. Use fixture 002 as the authoritative record for those artifacts and fingerprints; retain this file for provenance and semantic-baseline history. Do not infer that fixture 001 and fixture 002 are separate incompatible models merely because their provenance commits differ.

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

## 3. Admission status at the time of fixture 001

| Evidence item | Status |
|---|---|
| Source commit identified | Recorded |
| Semantic invariants defined in tests | Recorded |
| Exact exported package bytes preserved separately | Not yet recorded |
| Package SHA-256 of preserved export | Not yet recorded |
| Result SHA-256 independently frozen as golden value | Not yet recorded |
| Historical engine/schema compatibility | Untested |

## 4. Subsequent capture and current authority

The capture step described in the original record was subsequently completed and documented in `CURRENT_BASELINE_FIXTURE_002.md`, including the exact fixture-file SHA-256 and the canonical package, input, and result fingerprints. The current CI suite checks those frozen values and independently replays the package. Do not overwrite those values silently; any future change requires a new versioned fixture and reviewed expected fingerprints.

This record remains useful for the original semantic invariants and provenance, but it is not the authority for frozen package fingerprints. No compatibility adapter, empirical-data execution, or scientific authorization is implied.
