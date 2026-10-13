# Collective Toy — current baseline fixture 002

**Fixture class:** Current baseline; explicitly not historical.  
**Status:** Exact exported package bytes preserved and fingerprint-locked by CI.  
**Synthetic source model:** `toy-diamond-001`.  
**Engine version:** `collective-toy-engine-001`.  
**Input schema:** `collective-toy-input-001`.  
**Package schema:** `collective-toy-run-package-001`.

## 1. Provenance

- Engine/model source commit used for the baseline semantics: `9bf78ae6ea770475f5d803a862395311ff3dd829`.
- Capture test commit: `d232128e6c32d8e0e074fd2ef74c9e6379104fb9`.
- Capture workflow run: [38253411320](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/38253411320).
- Preserved package path: `prototypes/collective_toy/fixtures/current_baseline_package_001.json`.
- Package fixture was emitted by `export_run(demo_model())` and stored as canonical compact JSON without a trailing newline.

This is a baseline for the current synthetic engine contract, not an export from a previous release. It must not be cited as evidence of historical compatibility.

## 2. Frozen fingerprints

| Fingerprint | Value | What it covers |
|---|---|---|
| Exact fixture file SHA-256 | `cda406ad711caef3e0d6fb87a429bf329ae99ca35254747166c5b6c61056ab19` | Exact 2,359-byte file, including the package's embedded hash field |
| Package SHA-256 | `4f56aa1618d9a9aadbb68ee5f456950dfaf4898c94bbf7672be3d9d0bba9c9b8` | Canonical package object excluding `package_sha256`, per package contract |
| Result SHA-256 | `bb937763a3e8bd3e5aa9ae4b461f10ae2d6b655f17a9f735f5ae8f930ad93a84` | Canonical result payload excluding `input_sha256` and `result_sha256`, per engine contract |
| Input SHA-256 | `0ffab89f1b35a4ffbe30c1a6150d7e17c2fb01bc7f96d6049156c2f8fe70ae27` | Canonical input model |

The file hash and embedded package/result hashes cover different byte representations and must not be substituted for one another.

## 3. Expected semantic invariants

- Baseline reachable states: `["A", "B", "C", "D"]`.
- `block_ac` reachable states: `["A", "B", "D"]`.
- Baseline paths ending at `D`: `A → B → D` and `A → C → D`.
- `block_ac` path ending at `D`: `A → B → D`.
- Both scenarios are not truncated.
- The current engine must independently replay the frozen package and return `replay-verified`.

## 4. CI contract

The engine unit test loads the committed fixture and verifies:

1. The exact file SHA-256.
2. The file bytes are canonical JSON with no trailing newline.
3. The package, input, and result fingerprints.
4. Independent replay against the current engine.
5. The expected reachability results for both scenarios.

Browser/Python tests continue to compare shared semantic outputs without assuming identical package-envelope schemas.

## 5. Limits and next gate

- This is a synthetic software fixture, not empirical evidence and not a TGCV scientific-validity claim.
- No prior-version artifact has been identified; historical compatibility remains untested.
- The fixture does not authorize a compatibility adapter or promotion to `main`.
- Future fixture changes require a new versioned fixture and a reviewed change to expected fingerprints; do not silently overwrite these values.
