# TR-131 — Deterministic Analysis Runner Construction and Unit-Test Freeze 001

**Status:** CONSTRUCTED — UNIT TESTS DEFINED / SCIENTIFIC EXECUTION NOT AUTHORIZED  
**Date:** 2026-09-23  
**Canonical source:** GitHub `origin/main`

## Runner
`TR131_CROSS_DOMAIN_COMPARISON_RUNNER_001.py`

The runner is deliberately a **secondary analysis layer**. It does not reconstruct VisitAll or PRISM semantics and does not execute either domain.

Input is a frozen normalized evidence package governed by:
`TR131_CROSS_DOMAIN_COMPARISON_PROTOCOL_FREEZE_001`.

## Deterministic stages

1. Validate protocol identifier.
2. Validate required analytical fields.
3. Normalize transformation identities within each domain.
4. Derive `A,G,L,P,R,D` mechanically.
5. classify FPE structurally.
6. produce domain-local summaries.
7. emit provenance trace hashes and a deterministic output hash.

No outcome, VSL, value, TI label, or utility judgement is read by the runner.

## Minimum unit-test freeze

The test suite is:
`TR131_CROSS_DOMAIN_COMPARISON_RUNNER_001_TEST.py`

Frozen cases:

1. unchanged accessibility;
2. pure addition;
3. pure loss;
4. simultaneous addition/loss;
5. insufficient trajectory continuation;
6. duplicate identity rejection;
7. missing required field rejection;
8. two-domain comparison without raw identity pooling;
9. deterministic output hash.

Expected behaviour is encoded in the test assertions.

## Important boundary

The runner does **not** implement scientific trajectory-divergence inference. That endpoint requires a multi-transition trajectory dataset and a separately frozen trajectory procedure. A single transition is therefore **not testable**, rather than being treated as “no divergence”.

Likewise, the runner does not assign positive/negative meaning to expansion, contraction, persistence, or turnover.

## Construction decision

**PASS — RUNNER CONSTRUCTED AND MINIMUM UNIT-TEST SET FROZEN.**

This is a construction result only.

**Scientific execution remains NOT AUTHORIZED.**

## Next gate

**ANALYSIS IMPLEMENTATION TRACEABILITY AUDIT — ACTUAL RUNNER**

The actual Python implementation and test source must now be audited against the prior traceability specification. Only after that audit passes may the runner be used on the frozen VisitAll + PRISM evidence package.
