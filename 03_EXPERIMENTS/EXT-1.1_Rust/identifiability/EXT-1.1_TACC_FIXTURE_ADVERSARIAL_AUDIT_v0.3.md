# EXT-1.1 Rust — T_acc Fixture Adversarial Audit v0.3

**Result: PASS**
**Fixture:** `EXT-1.1_TAcc_COUNTERFACTUAL_FIXTURE_v0.1`

## Audit outcome

The executed fixture satisfies the v0.3 identifiability gate for the confirmatory micro-fixture.

1. **Closed state:** the fixture uses the explicitly defined `demo_pkg` package states and in-scope dependency declarations.
2. **Canonical transformation:** each candidate is a single normal registry dependency-edge insertion represented as `(package_name, version, requirement)`.
3. **Finite candidate universe:** `U_t = {tau_a, tau_b, tau_c}` is explicitly fixed by the frozen fixture registry records and does not depend on later package transitions.
4. **Explicit resolver:** Cargo 1.98.1, rustc 1.98.1, Windows MSVC target, resolver 2, explicit fixture Cargo configuration and isolated Cargo home are used.
5. **No future leakage in accessibility classification:** A/B/C accessibility is evaluated from the prior fixture state and frozen registry context; the later C state is used only for the separate realization check.
6. **A/B/C separation:** A is accessible; B is inaccessible because its dependency is absent; C is accessible and is later realized.
7. **Determinism:** repeated canonical lockfile outputs are byte-identical for successful A and C runs; B deterministically fails with exit code 101 and no lockfile.
8. **Temporal separation:** `case_C_later/Cargo.lock` was independently verified to contain `candidate_c 1.0.0`, closing the prior evidence-packaging gap.
9. **Integrity:** all 21 entries listed in `SHA256SUMS_FIXTURE.csv` were present and their SHA-256 values and byte counts matched the uploaded bundle exactly.
10. **Scope control:** the fixture is methodological evidence only and is not treated as empirical evidence from the scientific Rust dataset.

## Decision

**PASS — FREEZE AUTHORIZED for the counterfactual identifiability fixture v0.1.**

This pass does **not** imply that the scientific Rust dataset has yet been identified or processed. The next experiment may proceed only under the frozen v0.3 ontology and resolver boundary, with a separately frozen historical dataset/context and reproducible acquisition record.
