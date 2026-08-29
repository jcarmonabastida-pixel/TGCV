# EXT-1.1 Rust — Synthetic fixtures v0.1

These fixtures test the operational definition before any real outcome data are inspected.

| Fixture | Structural change | Expected ΔT_acc | Purpose |
|---|---|---:|---|
| F1 | New version satisfying existing constraints | Addition | Positive accessibility-space change |
| F2 | New version, but outside all relevant constraints | Empty | State change without T_acc change |
| F3 | Existing version becomes yanked | Removal, subject to resolver rules | Negative accessibility-space change |
| F4 | Dependency requirement narrows and excludes a previously admissible version | Removal | Constraint-induced contraction |
| F5 | Dependency requirement broadens and admits a previously inaccessible version | Addition | Constraint-induced expansion |
| F6 | Metadata field changes without affecting resolution | Empty | Non-redundancy / invariance |
| F7 | Candidate requires a future version | Empty at t | Temporal leakage test |
| F8 | Download count changes while structural state is identical | Empty | Outcome-independence test |
| F9 | Same structural input processed twice | Identical | Determinism test |
| F10 | Version identity reused ambiguously | Reject | Identity-integrity test |

## Acceptance criteria

- F1/F3/F4/F5 must produce the expected set difference.
- F2/F6/F8 must leave T_acc unchanged.
- F7 must not admit future information.
- F9 must be bitwise/logically deterministic at the derived-set level.
- F10 must fail closed rather than infer identity.

## Interpretation

Passing these fixtures establishes implementation readiness, not empirical support for TGCV. The fixtures test whether the operational representation behaves as specified before exposure to real data.
