# EXT-1.1 Rust — T_acc Counterfactual Fixture Evidence Dossier v0.1

**Status:** EXECUTION VERIFIED — pending final adversarial audit/freeze
**Fixture:** `EXT-1.1_TAcc_COUNTERFACTUAL_FIXTURE_v0.1`

## 1. Verification scope

The uploaded execution bundle was inspected after execution. The fixture is methodological evidence only; it is not evidence from the scientific Rust ecosystem dataset.

## 2. Execution result

The authoritative execution record reports `status = PASS` and `overall_pass = true`.

The fixture harness executed cases A, B and C twice using the captured Rust/Cargo environment and explicitly declared Cargo resolver 2.

## 3. Case verification

- **A:** `candidate_a 1.0.0` resolves successfully in both runs; lockfile SHA-256 is identical across runs (`64F1E3EE4D9DBF2596D2C84281E1A3B623D440E4AC399D2D2DA4D2E25D54A9B1`). Classification: `tau_a ∈ T_acc,t`. It is the accessible/unrealised fixture case.
- **B:** `candidate_b 1.0.0` fails in both runs with exit code 101 because `impossible =9.9.9` is absent from the frozen registry. No lockfile is created. Classification: `tau_b ∉ T_acc,t`.
- **C:** `candidate_c 1.0.0` resolves successfully in both runs; lockfile SHA-256 is identical across runs (`72483C9298C4A160A5FD7BC998A08C72486AB956774C721E52407BB9AC08D839`). Classification: `tau_c ∈ T_acc,t`.
- **C later:** `demo_pkg 1.1.0` resolves successfully and its generated lockfile was independently inspected to contain `candidate_c 1.0.0`. This establishes the intended later realization relation: `tau_c ∈ T_real,t+1` while prior accessibility was evaluated from `S_t,C_t,R`, not inferred from the later state.

## 4. Determinism

A/B/C repeated execution is deterministic under the canonical output criterion used by the harness. Raw Cargo/PowerShell logs are not treated as canonical deterministic output.

## 5. Integrity verification

`SHA256SUMS_FIXTURE.csv` contains 21 listed fixture inputs/results. All 21 listed paths were present in the uploaded bundle, and all recorded SHA-256 values and byte counts matched the uploaded bytes exactly.

The uploaded ZIP itself has SHA-256:

`EB1E290F9451B8B9ADB91662518687EC14EA9E3A978D30FB3B3A23D063BCA1DB`

## 6. Remaining qualification

The evidence now closes the previously identified C-later machine-check gap. The fixture is therefore execution-verified. Final scientific freeze still requires the adversarial audit to confirm that the evidence package is consistent with protocol v0.3 and resolver specification R v0.1, and that no hidden dependency on future information or ambient local state has entered the measurement.

**Scientific Rust dataset processing remains blocked until that final audit/freeze step passes.**
