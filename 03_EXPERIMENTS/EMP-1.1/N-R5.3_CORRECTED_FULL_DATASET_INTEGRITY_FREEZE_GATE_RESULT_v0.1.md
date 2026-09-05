# N-R5.3 Corrected Full Dataset Integrity Freeze Gate — Result v0.1

**Date:** 2026-09-05  
**Status:** PASS / CLOSED  
**Scientific execution:** NOT PERFORMED  
**Learner execution:** NOT PERFORMED  
**Confirmatory inference:** NOT PERFORMED

## Decision

The corrected prospective N-R5.3 predictor dataset passes the full-data integrity gate and is frozen for the subsequent N-R7 integration step.

This gate supersedes the historical N-R5.3 freeze record based on the superseded hash convention. The prior artifacts remain preserved as historical development provenance and MUST NOT be supplied to N-R7.

## Frozen specification

- `N-R5.3_PREDICTOR_DATASET_CONSTRUCTION_AND_FREEZE_SPECIFICATION_v0.2.md`
- Corrected semantic S0 hash convention from N-R5.2 v0.2 / N-R4B.4.

## Frozen inputs

- Train snapshots SHA-256: `b49c4da6187d015b9eb8a930a729ebbb874f17586f18c3ddddf65ed505145ef9`
- Test snapshots SHA-256: `18a67b22523f3d17183b14f7611ebc58451754bbfa104bc08ce26a512665ade1`
- Train count: 30,000
- Test count: 10,000
- Train seed: 3,100,000
- Test seed: 4,100,000

## Frozen outputs

- Train predictors SHA-256: `6559e31c7ef369c3d93f00d4c4dd0dfc481f7a001c4d89896994051872749bb9`
- Test predictors SHA-256: `6c2bebff931aaeae4b542ef9846645c0d88b07c86ad6962d19c166ed0a59cd98`

## Integrity checks

All 21 full-dataset checks reported PASS:

1. train_snapshot_hash
2. train_count
3. train_episode_ids
4. train_unique_ids
5. train_schema
6. train_dimensions
7. train_BR_concatenation
8. train_semantic_state_hash_consistency
9. train_traceability
10. test_snapshot_hash
11. test_count
12. test_episode_ids
13. test_unique_ids
14. test_schema
15. test_dimensions
16. test_BR_concatenation
17. test_semantic_state_hash_consistency
18. test_traceability
19. train_test_seed_separation
20. no_learner_or_inference
21. historical_recovery

## Implementation provenance

- Predictor implementation SHA-256: `d26c89fc9e194149d9fc722aa012858b8d265787e9b422e85df20b12c37a15dd`
- Constructor implementation SHA-256: `5187771c24e8f435f7cd04c22004f0507c03d79885e9fb95ee5e5797c8ec9474`
- Python: 3.14.7 CPython
- Platform: Windows 11 `10.0.26200-SP0`

## Scientific boundary

This gate establishes dataset integrity, traceability, deterministic construction, semantic-hash compatibility with N-R4B.4, and absence of learner/inference execution. It does not establish predictive performance or any scientific hypothesis result.

## Next authorized gate

Update the N-R7 integration artifacts to reference these corrected predictor hashes, then run the N-R7 preflight. No learner or confirmatory inference is authorized until the updated preflight passes.
