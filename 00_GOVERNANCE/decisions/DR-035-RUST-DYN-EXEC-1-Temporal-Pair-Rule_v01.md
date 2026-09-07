# DR-035 — RUST-DYN-EXEC-1 Temporal Pair Construction Rule v0.1

**Status:** ACCEPTED — EX-ANTE TEMPORAL POPULATION FREEZE
**Date:** 2026-09-08
**Scope:** EXT-1.1 Rust / RUST-DYN-EXEC-1
**Predecessors:** D-OPS-1; DR-033; DR-034; RUST-DYN-STATE-1; RUST-DYN-ENGINE-2

## 1. Purpose

Freeze the exact population and construction rule for temporal comparisons before any real-dataset execution.

This record resolves the remaining ambiguity in the phrase “two package-version origins ordered by creation time” used by the preceding design records. It does not authorize real-data execution.

## 2. Primary observational population

An observational origin is:

`o = (version_id, package_id, version_str, created_at)`.

Only origins satisfying the frozen structural schema and integrity requirements of D-OPS-1 are eligible.

## 3. Temporal ordering

Within each `package_id`, eligible origins are ordered by `created_at`.

### Exact timestamp ties

If two or more origins of the same package have exactly the same `created_at` timestamp, they are **not ordered by version_id, lexical version string, database row order, file order, or any other secondary key**.

Such tied origins are excluded from temporal-pair construction unless a future governance decision defines and validates an independent temporal ordering rule.

This prevents an artificial temporal direction from being introduced by an arbitrary identifier.

## 4. Pair construction

The authorized temporal population consists exclusively of **adjacent consecutive origins within each package after the timestamp-tie exclusion**.

For an ordered package sequence:

`o_1, o_2, ..., o_n`

the admissible temporal pairs are:

`(o_1,o_2), (o_2,o_3), ..., (o_{n-1},o_n)`.

No non-adjacent pair `(o_i,o_j)` with `j > i+1` is included in the primary population.

The pair direction is always from the earlier origin to the later origin.

## 5. Rationale

The adjacent-pair rule is selected ex ante because the present gate tests **local temporal change** in the accessible transformation space. It avoids silently mixing short-step change with arbitrary long-range comparisons and prevents multiple temporal paths from overweighting a package through combinatorial all-pairs construction.

The rule is independent of whether the resulting dataset supports or fails H-R1, H-R3, or H-R4.

## 6. Frozen comparison semantics

For each admissible pair `(o_i,o_j)`:

`T_i = T_acc(o_i)`

`T_j = T_acc(o_j)`

and:

`ΔT_acc(i,j) ≠ 0 iff T_i ≠ T_j`.

The exact set differences are retained:

- expansion = `T_j \ T_i`;
- contraction = `T_i \ T_j`;
- persistence = `T_i ∩ T_j`.

Classification:

- `PERSISTENCE` iff `T_i = T_j`;
- `EXPANSION` iff `T_i ⊂ T_j`;
- `CONTRACTION` iff `T_j ⊂ T_i`;
- `RECONFIGURATION` otherwise.

Equal cardinality with different membership remains `RECONFIGURATION`.

## 7. Reach / Trajectory linkage

For each admissible origin, the downstream layer remains exactly the RUST-DYN-STATE-1 bounded representation:

- `Reach_H(o)` = finite-horizon successor set excluding the initial origin;
- `Trajectory_H(o)` = ordered finite-horizon successor sequences excluding the initial origin identity.

The first authorized execution uses `H=1`.

No Reach or Trajectory information is used to construct `T_acc` or `P_tau`.

## 8. Exclusions

The following are excluded from the temporal population or analysis:

- arbitrary secondary ordering of timestamp ties;
- non-adjacent temporal pairs in the primary population;
- duplicated origins;
- malformed structural records;
- sampled or convenience-selected pairs;
- pairs constructed using outcome, adoption, popularity, downloads or later activity;
- future outcome windows;
- predictive targets or metrics;
- post-origin metadata not admitted by D-OPS-1;
- any retrospective pair selection based on observed `ΔT_acc`, Reach, Trajectory or outcomes.

## 9. Required execution reporting

The real-data execution must report, at minimum:

- eligible origin count;
- timestamp-tie origin count;
- excluded-origin count due to ties;
- temporal pair count;
- pair count by package;
- zero-pair package count;
- exact pair-construction rule identifier: `DR-035-v0.1-ADJACENT-CREATED-AT`;
- dataset SHA-256;
- executor/adapter identity and hash;
- resolver identity and hash;
- horizon;
- firewall status;
- deterministic replay status.

These are execution facts and must be produced without scientific interpretation.

## 10. Falsifiers / integrity failures

Execution is invalid if:

1. a timestamp tie is ordered by an unapproved secondary key;
2. non-adjacent pairs enter the primary population;
3. pair membership depends on later outcomes or observed results;
4. the pair population is sampled without explicit authorization;
5. the reported pair count cannot be reconstructed from the frozen rule;
6. temporal ordering is not deterministic;
7. the implementation silently substitutes a different temporal rule.

## 11. Relationship to prior gates

This record does not modify:

- TGCV Core ontology;
- D-OPS-1 structural semantics;
- RUST-DYN-1 dynamic definitions;
- RUST-DYN-STATE-1 state normalization;
- RUST-DYN-ENGINE-2 synthetic conformance;
- TR-131 or DR-032 scientific closure.

It only makes the temporal population construction explicit for RUST-DYN-EXEC-1.

## 12. Decision

**DR-035 = ACCEPTED — TEMPORAL PAIR POPULATION FROZEN.**

The RUST-DYN-EXEC-1 temporal population is now fixed to adjacent consecutive package-version origins ordered by `created_at`, with exact timestamp ties excluded rather than arbitrarily ordered.

**REAL-DATASET EXECUTION AUTHORIZED: NO.**

## 13. Next controlled operation

**RUST-DYN-EXEC-1A — Real-Data Adapter Construction + Synthetic Conformance + Local Preflight.**

The adapter must implement this temporal rule exactly before any real-data execution authorization is considered.
