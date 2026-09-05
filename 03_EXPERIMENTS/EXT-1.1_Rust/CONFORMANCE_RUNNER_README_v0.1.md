# R* v0.2 — SQLite Conformance Runner v0.1

## Purpose

This runner checks implementation conformance of the frozen **R* v0.2** resolver against the actual EXT-1.1 Rust SQLite export and performs one bounded integration smoke test.

It is a **conformance gate**, not the scientific experiment. A `PASS` does not establish historical Cargo equivalence, causal effects, universality, or literature novelty.

## Inputs

Required local input:

- `rust_repos_2022_09_07_export.db`

The database is opened read-only and `PRAGMA query_only=ON` is set. The runner does not require uploading the large database to GitHub or ChatGPT.

## Windows / PowerShell execution

From the EXT-1.1_Rust directory:

```powershell
python .\tools\run_rstar_conformance.py `
  --db "C:\Users\pedri\Downloads\TGCV_Rust_Audit\rust_repos_2022_09_07_export.db" `
  --output ".\CONFORMANCE_RESULT.json"
```

If the database hash is intentionally omitted for a diagnostic run:

```powershell
python .\tools\run_rstar_conformance.py `
  --db "C:\Users\pedri\Downloads\TGCV_Rust_Audit\rust_repos_2022_09_07_export.db" `
  --output ".\CONFORMANCE_RESULT.json" `
  --skip-hash
```

## What is checked

1. R* v0.2 implementation-level checks:
   - exact constraint;
   - supported caret constraint `^1.0`;
   - unsupported constraint is fail-closed and distinct from an empty candidate set;
   - temporal cutoff;
   - maximum semantic version selection;
   - row-order independence;
   - duplicate version-ID ambiguity fails closed.
2. Required SQLite schema and row counts.
3. A bounded real-data smoke test using the known `solana-tokens@1.10.38 -> serde ^1.0` path, if present in the frozen export.
4. Runtime and database provenance, including Python version, SQLite version, platform, local Git HEAD when available, and database SHA-256 unless `--skip-hash` is used.

## Status interpretation

- `PASS`: implementation checks, schema check, and bounded smoke test passed.
- `FAIL`: an implementation or execution check failed.
- `BLOCKED`: required input/schema/path was unavailable, or the smoke test could not be executed without guessing.
- `NOT_EXECUTED`: reserved for an invocation that did not reach execution.

## Scientific boundary

The runner must not be used to claim that R* reproduces Cargo's historical resolver. The frozen specification explicitly defines R* as a restricted, deterministic empirical construction over retained dataset fields. Unsupported Cargo semantics remain excluded and are not negative evidence.

A conformance `PASS` authorizes the next experimental gate: controlled **A/B/C execution plus double-run reproducibility**. It does not itself constitute an A/B/C result.

## Reproducibility

Keep `CONFORMANCE_RESULT.json` with the experiment records. Do not commit the large SQLite database. Commit only compact provenance, code, specifications, manifests, logs, and derived results that are appropriate for repository storage.
