# TGCV — Rust Ω-Primary U Implementation Test Fixture Review v0.1

**Status:** CLOSED — SYNTHETIC TEST FIXTURE CONTRACT FROZEN / REAL DATA EXCLUDED
**Date:** 2026-10-02
**Gate:** RUST_OMEGA_PRIMARY_U_IMPLEMENTATION_TEST_FIXTURE_REVIEW

## 1. Fixture boundary

No existing canonical Ω-primary fixtures were found in the repository. A dedicated synthetic fixture set is therefore required.

Fixtures must be entirely artificial and must not be derived from, sampled from, or copied from the retained Rust snapshot.

## 2. Minimal fixture universe

The fixture set must contain a deliberately small universe with:

- two origin releases;
- at least two target packages;
- at least two target releases;
- one valid transformation;
- one duplicate representation of the same transformation;
- one missing transformation-defining identifier;
- one ambiguous/missing timestamp;
- one complete-absence case;
- one UNKNOWN_MISSING coverage case;
- one out-of-scope record;
- at least one dependency relation candidate.

All identifiers must be synthetic.

## 3. Expected behaviors

### F1 — valid transformation
`(o1, p1, v1)` produces one canonical τ.

### F2 — duplicate
Two identical canonical τ records collapse to one U identity while retaining source provenance in diagnostics.

### F3 — missing identity
A record lacking any transformation-defining identifier becomes unresolved/FAIL-CLOSED and cannot enter U_t.

### F4 — temporal ambiguity
A record whose timestamp cannot be placed unambiguously under DR-035-v0.1-ADJACENT-CREATED-AT is unresolved and excluded from U_t.

### F5 — complete absence
An explicitly complete absence may support a descriptive absence state, but must not manufacture a transformation.

### F6 — unknown coverage
UNKNOWN_MISSING must remain unknown and cannot be interpreted as removal.

### F7 — out-of-scope
OUT_OF_SCOPE is retained as a coverage/provenance state and cannot be silently treated as absence.

### F8 — relation candidate
A synthetic dependency record can generate a candidate relation endpoint only through the separately frozen relation vocabulary and endpoint rules.

## 4. Negative firewall fixtures

At least one test must inject synthetic prohibited fields representing accessibility, Reach, outcome, value or future trajectory.

Changing those prohibited fields while holding primitive Ω inputs constant must leave U_t byte-identical.

This is a software firewall test, not a scientific independence result.

## 5. Determinism fixture

The same fixture supplied in different input row orders must produce identical canonical output and identical declared output hash.

## 6. Fixture integrity

The fixture manifest must record:

- fixture version;
- synthetic origin;
- expected case labels;
- expected U identities;
- expected unresolved/coverage states;
- serialization version;
- expected output hash once the implementation exists.

The expected output hash cannot be frozen until the implementation and serialization are actually built; therefore this gate freezes the fixture semantics, not a future hash.

## 7. Decision

**FIXTURE SEMANTICS:** FROZEN.
**REAL DATA:** EXCLUDED.
**EXPECTED BEHAVIOR:** FROZEN.
**IMPLEMENTATION EXECUTION:** NOT PERFORMED.
**SCIENTIFIC EXECUTION:** NOT AUTHORIZED.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 8. Next gate

`RUST_OMEGA_PRIMARY_U_IMPLEMENTATION_SYNTHETIC_TEST_BUILD_REVIEW`