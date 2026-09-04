# EXT-1.1 Rust — `T_acc` Counterfactual Micro-Fixture v0.1

**Status:** FROZEN — PASS
**Purpose:** Demonstrate that the operationalized `T_acc` is not definitionally identical to realised trajectory `T_real`.

## 1. Fixture principle

The fixture is deliberately independent of the scientific Rust dataset. It uses a tiny **synthetic but fully frozen registry context** and package states for which candidate dependency-edge insertions can be checked by the real Cargo resolver.

The fixture was evaluated using the canonical ontology and resolver boundary defined for EXT-1.1. It is methodological evidence only; it is not evidence about the empirical Rust ecosystem.

## 2. Fixed package state

`S_t = demo_pkg 1.0.0`, with resolver 2 and fixed normal dependency `base = "=1.0.0"`.

## 3. Frozen fixture registry context

The in-scope package/version records are exactly:

- `base 1.0.0`
- `candidate_a 1.0.0`
- `candidate_b 1.0.0`
- `candidate_c 1.0.0`

`candidate_a` has no additional dependency and resolves. `candidate_b` requires absent `impossible =9.9.9` and therefore cannot resolve. `candidate_c` is present at `t` but is introduced into the observed package state only at `t+1`.

## 4. Candidate universe

`U_t = {tau_a, tau_b, tau_c}` with each transformation represented canonically as `(package_name, version, requirement)`.

The universe is constructed from the frozen registry context and not from realised future transitions.

## 5. Verified cases

### A — accessible + unrealised

`tau_a ∈ T_acc,t` and `tau_a ∉ T_real,t`.

Observed twice with exit code `0`; canonical lockfile SHA-256 was identical in both runs:
`64F1E3EE4D9DBF2596D2C84281E1A3B623D440E4AC399D2D2DA4D2E25D54A9B1`.

### B — inaccessible + unrealised

`tau_b ∉ T_acc,t` and `tau_b ∉ T_real,t`.

Observed twice with exit code `101`, no lockfile, and the expected missing-package resolution failure.

### C — accessible at t, realised later

Prior accessibility:
`tau_c ∈ T_acc,t`.

Observed twice with exit code `0`; canonical lockfile SHA-256 was identical in both runs:
`72483C9298C4A160A5FD7BC998A08C72486AB956774C721E52407BB9AC08D839`.

Later state `S_t+1 = demo_pkg 1.1.0` generated successfully, and its lockfile was independently verified to contain `candidate_c 1.0.0`, establishing `tau_c ∈ T_real,t+1`.

## 6. Determinism and integrity

The execution harness reports overall PASS and deterministic A/B/C classifications. The uploaded fixture checksum inventory contains 21 entries; all 21 listed files were present and their SHA-256 values and byte counts matched exactly.

Uploaded execution bundle SHA-256:
`EB1E290F9451B8B9ADB91662518687EC14EA9E3A978D30FB3B3A23D063BCA1DB`.

## 7. Freeze decision

The counterfactual fixture passes the v0.3 adversarial identifiability gate. It is now **FROZEN** as methodological evidence for the separation of accessible and realised transformations.

This freeze does not constitute empirical evidence from the scientific Rust dataset and does not authorize use of future observations to define historical accessibility.
