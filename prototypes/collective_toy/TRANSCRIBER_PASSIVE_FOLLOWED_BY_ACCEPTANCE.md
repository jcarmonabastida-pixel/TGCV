# Transcriber acceptance note: scoped passive construction

## Change
The browser natural-language transcriber recognizes the bounded singular pattern:

> El estado de A es seguido por el estado de B.

The recognized relation is directed from A to B.

## Acceptance evidence
The browser contract suite asserts:
- exactly two named states and one transition for the standalone example;
- source `reposo` and target `ejecución`;
- no reverse transition;
- no unresolved-clause notice for this supported example;
- preservation of a prior `inicio → reposo` transition when the passive sentence adds `reposo → ejecución`;
- adversarial multi-destination wording (`El estado de reposo es seguido por el estado de ejecución y después por el estado de resultado.`) is not swallowed into one destination label and is surfaced for human clarification.

The adversarial test initially failed on the incorrect destination label, reproducing the issue. After the scoped parser guard and test-message alignment, all four required CI workflows passed on commit `ed272e939924f958746b32ec39cafc3a9240246d`: governance consistency, synthetic engine tests, browser performance benchmark, and browser/cross-runtime tests.

## Limits
This does not claim support for all Spanish passive constructions, gender/number variants, arbitrary passive clauses, or general Spanish understanding. Unsupported input must continue to follow the existing clarification behavior.

## Scope
This change is isolated from the condition evaluator, graph execution engine, scientific core, and graph-based demonstrator flow. It is based directly on `main` and does not include unrelated commits from the broader prototype PR.
