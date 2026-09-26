# TI-001 V011 E1 Configuration Deviation Reconciliation Gate Specification 001

**Status:** GATE SPECIFICATION — SCIENTIFIC ANALYSIS BLOCKED PENDING RECONCILIATION

## Purpose

Determine the evidentiary status of Executor-1 (E1) after the primary execution audit identified an observed runtime-generation deviation.

## Fixed facts

- E1 attempted exactly 420 decision units.
- The canonical fixture binding is intact.
- 245 responses are valid A/B decisions and 175 are invalid.
- The declared generation configuration contains `reasoning: null`.
- Runtime usage records show non-zero `reasoning_tokens` in 300 of 420 records, totaling 16,613 observed reasoning tokens.
- The E1 result is preserved without modification.

## Reconciliation questions

1. Does the recorded `reasoning: null` configuration have a documented runtime/API meaning that permits non-zero reasoning-token usage?
2. If so, does that meaning satisfy the frozen V011 execution contract, or does the contract require an explicit no-reasoning guarantee?
3. If the runtime behavior is a configuration deviation, what evidentiary status follows for E1?
4. Are the 245 valid decisions still usable as descriptive execution observations without silently treating E1 as fully conformant?
5. Does any resolution require repeating E1? No repeat is authorized by this gate; any future execution requires a separately approved design decision.

## Prohibitions

This gate must not alter E1 records, remove invalid responses, reinterpret reasoning tokens as zero, recode decisions, or calculate TI-001 estimands.

## Required outcome

The gate must record:
- observed deviation;
- documented runtime semantics;
- contract conformity determination;
- evidentiary status of E1;
- whether scientific analysis may proceed;
- whether a new execution design is required.

Until PASS/RESOLVED status is established, scientific analysis remains blocked.
