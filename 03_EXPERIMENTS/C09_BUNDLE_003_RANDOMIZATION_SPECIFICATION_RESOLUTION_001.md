# C09 Bundle 003 — Randomization Specification Resolution 001

**Status:** `RESOLUTION REQUIRED — BUNDLE 003 REMAINS FROZEN`

## Purpose

This artifact records a specification gap identified before independent Executor-2 execution. It does not modify Bundle 003 and does not authorize execution.

## Finding

Bundle 003 declares the randomization algorithm as `SHA256-Fisher-Yates` with seed `130917`, but does not freeze the exact byte/string construction used to derive each Fisher-Yates index.

A Fisher-Yates procedure requires, at minimum, an exact deterministic mapping from `(seed, i)` to the integer used to select `j` at each descending index. The Bundle 003 text does not specify that mapping.

## Historical implementation observed

An earlier C09 executor uses the following construction:

```text
SHA256(f"{seed}:{i}")
```

followed by conversion of the first eight digest bytes to a big-endian integer and reduction modulo `i + 1`.

This historical implementation is evidence of a prior implementation choice only. It is **not adopted as an implicit definition of Bundle 003** because doing so after the freeze would silently convert an Executor-1 implementation detail into a frozen experimental definition.

## Independence consequence

Executor-2 must not resolve this ambiguity by importing, calling, or copying the historical Executor-1 implementation as its source of truth. Such reuse would compromise the intended independent reconstruction boundary.

## Current authorization state

- Bundle 003: remains immutable.
- Bundle 003 scientific execution: `NOT AUTHORIZED`.
- Executor-2: `BLOCKED PENDING SPECIFICATION RESOLUTION`.
- No treatment effect estimate is authorized from the current Executor-2 path.

## Required resolution

Before execution, the canonical experimental contract must explicitly freeze the deterministic SHA256-Fisher-Yates derivation, including:

1. the exact input encoding for `(seed, i)`;
2. the exact digest-to-integer conversion;
3. the exact range-reduction rule;
4. the resulting assignment definition.

The resolution must be recorded as a new, versioned specification artifact or successor bundle definition. Bundle 003 itself must not be edited retroactively.

## Non-retroactivity rule

No result produced under an implementation chosen after this finding may be attributed to the currently frozen Bundle 003 unless the missing randomization definition is formally resolved as part of the canonical successor specification before execution.
