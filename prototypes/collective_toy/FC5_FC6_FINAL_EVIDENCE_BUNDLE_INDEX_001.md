# FC-5 / FC-6 Final Evidence Bundle Index

Status: clean-promotion candidate evidence map. Required grouped contract coverage is accepted from the prior candidate; this branch must independently pass the five-workflow exact-HEAD gate before promotion. This index does not claim scientific validity.

## Artifact inventory by package stage

The browser contract suite enumerates four stages (EXPLORATION, EXECUTION, OUTCOME, ASSESSMENT) against all eight presence combinations of `concrete_execution_trace`, `outcome_record`, and `value_assessment` (32 rows). The declared stage is expected to match the furthest present artifact:

| Stage | Required artifact presence | Key contract checks |
|---|---|---|
| EXPLORATION | no trace, outcome, or assessment | stage and absence/dependency consistency; `value_assessment_status=NOT_ASSESSED` |
| EXECUTION | trace present; no outcome or assessment | trace object/type and structural semantics; package stage consistency |
| OUTCOME | trace and outcome present; no assessment | outcome references the concrete execution and trace digest; stage consistency |
| ASSESSMENT | trace, outcome, and assessment present | assessment links to outcome; outcome links to execution and trace digest; assessment outcome digest; package digest and replay |

These are the four valid rows asserted by the GT-04 matrix. The other 28 combinations are rejection adversaries, not valid artifacts.

## Evidence and permitted claims

| Evidence | Permitted claim | Explicit non-claim |
|---|---|---|
| Governance workflow | repository/process contract checks passed on the tested commit | no scientific or causal validity |
| Synthetic engine workflow | deterministic software-contract behavior passed for covered synthetic cases | no empirical finding, generalization, or TGCV theory validation |
| Browser and cross-runtime workflow | UI/package checks and cross-runtime agreement passed for covered cases | no exhaustive correctness claim outside tested predicates |
| Engine benchmark | measured runtime for the named benchmark workload | no universal performance claim |
| Browser benchmark | measured browser behavior for the named benchmark workload | no general UX/performance guarantee |
| GT-04 stage/presence matrix | 4 valid stage rows and rejection of the other 28 presence combinations in the tested matrix | not exhaustive schema validation |
| GT-05 full-chain replay | tested synthetic path preserves ordered transitions, execution/outcome/assessment links, export/import and replay verification | not empirical evidence or scientific execution |

## Link integrity inspected by GT-05

The grouped end-to-end tests assert:
- exported package stage is `ASSESSMENT`;
- concrete trace is completed and preserves the submitted transition sequence;
- outcome execution ID matches trace execution ID;
- outcome trace SHA-256 matches the trace digest;
- assessment outcome ID matches the outcome ID;
- imported package reaches `replay-verified` independently.

The temporal-profile path repeats export/import/replay checks for its ordered transition sequence.

## Final-gate rule

All five required workflows must pass on one exact candidate HEAD after the final documentation and test changes. Older successful runs are historical evidence only and cannot be represented as the final gate for a later SHA. Recheck PR #70 is still draft and `main` is unchanged before any promotion.

## Deferred limitation

Compatibility with authentic historical packages remains separate until authentic artifacts, provenance, and applicable licensing are verified. Synthetic fixtures do not substitute for historical evidence.
