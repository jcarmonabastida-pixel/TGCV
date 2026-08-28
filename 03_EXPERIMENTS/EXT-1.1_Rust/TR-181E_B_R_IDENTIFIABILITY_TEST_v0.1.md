# TGCV — TR-181E B/R Identifiability Test v0.1

**Date:** 2026-08-28
**Status:** ENGINE-LEVEL PASS / SCIENTIFIC GATE OPEN

## 1. Quota / execution condition

No quota-related blocker was detected for this test. The available computational path was sufficient to execute the engine-level structural check.

## 2. Inputs

Canonical B schema recovered in `EMP-1.1_RECONSTRUCTION_INPUTS.md`:

- component count;
- three resource values;
- objective identity.

Canonical R engine recovered from `03_EXPERIMENTS/TR-181E/r_engine.py`, whose current implementation returns `accessible_ids` and `cardinality` and evaluates only pre-outcome predicates. The implementation has SHA `7ff899b8bb691569d882ed7c13d333fb3d00662b`.

## 3. Executed structural check

Two synthetic snapshots were constructed with identical B-level summary values:

```text
B1 = B2
component count = 2
resources = (1, 2, 3)
objective = same objective identity
```

The component identities differed:

```text
S1 components = {A, C}
S2 components = {B, C}
```

A minimal candidate inventory containing pre-outcome component-existence predicates was evaluated by the current R engine.

Observed output:

```text
R1 = { accessible_ids: (A,), cardinality: 1 }
R2 = { accessible_ids: (B,), cardinality: 1 }
```

Therefore the engine produced:

```text
B1 = B2
R1 != R2
```

## 4. Interpretation

This is a **PASS for engine-level non-determinacy of B → R under the synthetic candidate construction**.

It demonstrates that the current R engine is capable of representing accessibility differences that are invisible to the B summary when component identity is not encoded by B.

It does **not yet constitute a scientific freeze-level proof**, because the exact admissible component domain and full frozen candidate instance inventory have not yet been recovered. The synthetic candidate inventory is therefore an implementation sanity check, not a claim about the final TR-181E experimental population.

## 5. Leakage check

The executed calculation used only snapshot components/resources and candidate preconditions. No outcome, trajectory or predictive score was used.

## 6. Gate decision

**Engine-level B/R identifiability:** PASS.

**Scientific B/R identifiability under final frozen T:** OPEN.

**Outcome leakage:** PASS for this check.

**TR-181E freeze:** BLOCKED pending recovery/freeze of the complete candidate instance universe and execution of the corresponding domain-level identifiability audit.

## 7. Next required step

Recover or explicitly freeze the admissible component/resource/objective domains and complete candidate inventory. Re-run this test over that final universe. No predictive fitting is required for this gate.
