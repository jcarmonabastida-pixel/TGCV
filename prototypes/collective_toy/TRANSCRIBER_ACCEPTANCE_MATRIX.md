# Transcriber acceptance matrix

Current evidence snapshot: commit `fab9954707081b9f61b82ae9194406a511c6ce83`.
The initial acceptance probe failed because the parser did not produce the expected graph; that failure is retained as discovery evidence:
https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39626485661.
The test was then changed to characterize the current limitation without changing parser behavior. The resulting suite passed all five workflows:
https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39627345707
https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39627345719
https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39627345734
https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39627345736
https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39627345920.

This matrix records what the current browser contract test explicitly checks.
A passing test establishes the tested examples, not general Spanish-language
understanding. “Partial” means the requirement is demonstrated only for
bounded examples or has not been tested as a systematic class.

| Requirement group | Existing acceptance evidence in `web/ui_contract_test.cjs` | Status | Limitation / next evidence needed |
|---|---|---|---|
| Directed source and target | Checks explicit `source` and `target`; includes destination-before-source wording and passive “Desde reposo se pasa a ejecución” | Verified for examples; bounded | Other grammatical constructions are not assumed equivalent without evidence |
| Passive construction “es seguido por” | Characterization test records that “El estado de reposo es seguido por el estado de ejecución” remains pending clarification and does not add an edge | Known limitation | Supporting this construction requires a separate, scoped parser change and new acceptance evidence |
| Normalized graph equivalence | Compares normalized edges for “El proceso pasa a ejecución desde reposo” and “Desde reposo se pasa a ejecución”; compares source, target and condition | Verified for this pair | Does not establish equivalence across other constructions or domains |
| Multiple and sequential relations | Checks two explicit sequential edges plus an independent third edge | Verified for example | Broader clause ordering and coordination remain unproven |
| Branches and return edges | Checks evaluation to approved/rejected and rejected back to evaluation | Verified for example | Not exhaustive for arbitrary graph topology |
| Initial-state declaration | Checks “El sistema comienza en reposo/espera” and resulting `initial_state` | Verified for examples | Broader initial-state paraphrases are not systematically covered |
| Conditions preserved as metadata | Checks condition text and schema v002 for conditional transitions | Verified for examples | Recognition grammar remains bounded |
| Unassessed conditions blocked | Checks that prose conditions remain unevaluated and do not enable traversal | Verified for examples | Does not prove correctness for arbitrary condition language |
| Supported condition evaluator | Tests a supported true condition permits execution and a false condition blocks it | Verified for tested predicates | Only tested evaluator expressions are covered |
| Negated transition vs. negated condition | Checks that a negated transition does not create an affirmative edge, while negation inside a condition is preserved and not evaluated by the bounded evaluator | Verified for examples | Other negation scope/word order remains unproven |
| Ambiguous / incomplete clauses | Checks unresolved sentences remain pending for clarification; clarified text can add an explicit edge | Verified for examples | Does not establish exhaustive ambiguity detection |
| Cross-domain transfer | Includes irrigation and access-control examples | Partial | Two domains are not evidence of domain-independent parsing |
| Robustness against invented edges | Checks selected negated, incomplete, sequential and multi-relation examples for expected edge counts and labels | Partial | Adversarial coverage is selected, not exhaustive |
| General Spanish understanding | No test suite can establish unrestricted language understanding from these examples | Not established | Keep claims bounded to tested constructions; add targeted evidence only for explicit requirements |

## Grouped adversarial contract: clarification lifecycle

The existing `web/ui_contract_test.cjs` already exercises a bounded clarification lifecycle; do not duplicate these cases as separate phrase-level tests unless a regression exposes a gap:

| Invariant | Existing evidence | Assessment |
|---|---|---|
| No invented edge from unresolved text | Unsupported `es seguido por` stays pending and does not add a transition; vague text yields no transitions | Verified for these examples |
| Preserve previously recognized edges | After partial clarification, the two already recognized transitions remain in the model | Verified for this flow |
| Keep unresolved clauses pending after partial clarification | After replacing one pending clause, the remaining `Cuando se recupera, continúa.` stays visible for clarification | Verified for this flow |
| Add only explicitly recognized relations after clarification | Final clarified graph has three transitions, including the explicitly clarified return and recovery edges | Verified for this flow |

These assertions cover the lifecycle as a grouped contract, but they do not establish robustness for arbitrary ambiguous or adversarial Spanish input. Keep the broader “Robustness against invented edges” status **Partial** until a named requirement or reproducible discrepancy justifies additional tests.

## Acceptance rule

- **Verified for examples**: an explicit assertion checks the expected graph or behavior.
- **Partial**: evidence exists, but the broader capability is not established.
- **Not established**: current evidence does not justify the claim.
- A green CI is evidence that the automated suite passed for the referenced commit; it is not, by itself, proof of scientific validity or general language competence.

## Scope guard

This is documentation of existing acceptance evidence. It does not change the parser,
execution engine, condition evaluator, scientific core, or `main`. New tests should be
added only when tied to a named requirement or a reproducible discrepancy.
