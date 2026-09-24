# TI-001 Decision Agent Specification 001

**Status:** FROZEN DECISION MECHANISM — SCIENTIFIC EXECUTION AUTHORIZED, NOT STARTED

## 1. Decision mechanism

TI-001 uses a general-purpose LLM agent as the decision mechanism. The same model and the same base decision protocol are used for Control and Treatment. The experimental manipulation is restricted to the condition-specific information defined by the frozen fixture.

The mechanism must not contain a hand-coded rule that maps the treatment signal to a preferred transformation.

## 2. Symmetry

Control and Treatment use the same:

- model;
- base prompt;
- output format;
- deterministic generation configuration;
- tool restrictions;
- decision timing;
- validation procedure.

Treatment differs only by receiving the structured future transformation-space information specified by the frozen fixture.

## 3. Information isolation

The agent has no access to:

- web or external search;
- external files other than the explicitly supplied pre-decision input;
- successor state;
- successor accessibility;
- reward, utility, payoff, value, or outcome;
- decisions made by other instances;
- post-decision feedback.

## 4. Decision output

The agent must return exactly one executable transformation: `a`, `b`, or `c`.

No preferred-action field, confidence score, intelligence score, reward estimate, value estimate, or outcome prediction is part of the primary decision output.

## 5. Determinism

The generation configuration must be deterministic or otherwise have its complete stochastic configuration recorded. The exact model identifier/version, runtime identifier/version, generation parameters, and system/base prompt hash must be frozen before scientific execution.

## 6. Model/runtime freeze requirement

The mechanism is conceptually frozen by this specification, but the following fields must be populated in the execution package before the first scientific run:

- `model_id`
- `model_version`
- `runtime_id`
- `runtime_version`
- `generation_configuration`
- `base_prompt_sha256`

Changing any of these after the first scientific observation constitutes a protocol deviation unless explicitly defined as a separate authorized experiment.

## 7. Separation from execution

The decision agent produces the transformation choice only. `TI001_SCIENTIFIC_EXECUTOR_001.py` remains responsible for validating the choice and applying the frozen transition after the decision.

## 8. Governance boundary

This specification freezes the decision-mechanism class and experimental symmetry. It does not claim scientific evidence for Transformational Intelligence and does not itself create scientific observations.

**Scientific execution remains AUTHORIZED but NOT STARTED.**
