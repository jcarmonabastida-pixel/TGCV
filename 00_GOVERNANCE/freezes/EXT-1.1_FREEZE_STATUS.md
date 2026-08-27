# EXT-1.1 — Freeze Status Record

## State

**NOT FROZEN** as of 2026-08-27.

## Recovered continuity constraint

Before downloading or processing the Rust dataset, an identifiability/privacy audit must be performed. Only if that audit passes should EXT-1.1 be frozen and the exact dataset identified.

## Why this record exists

This file deliberately records the boundary between recovered research state and validated frozen state. It prevents an unverified dataset, execution, or result from being represented as an authoritative EXT-1.1 freeze.

## Freeze prerequisites

- [ ] Identifiability/privacy audit completed and passed.
- [ ] Exact Rust dataset identified and provenance recorded.
- [ ] Dataset integrity/hash recorded without committing the dataset itself.
- [ ] EXT-1.1 protocol and configuration fixed.
- [ ] Computational execution reproducibly recorded.
- [ ] Results and validation checks recorded.
- [ ] Immutable freeze manifest created.

## Integrity rule

Do not change this record to `FROZEN` merely to establish continuity. The freeze status must follow the evidence and reproducibility checks above.
