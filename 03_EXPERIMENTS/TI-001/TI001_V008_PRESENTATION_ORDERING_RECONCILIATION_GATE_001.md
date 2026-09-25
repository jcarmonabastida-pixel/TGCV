# TI-001 V008 Presentation Ordering Reconciliation Gate 001

**Status:** PROPOSAL — APPROVAL REQUIRED
**Scientific execution:** NOT_PERFORMED
**Fixture generated:** false

## Existing contracts

The approved V008 generator specification assigns a shuffled presentation label to each pair position and requires each pair to contain one `I1_FIRST` and one `I2_FIRST`. The current generator materializes the pair in the order determined by that pair-level presentation assignment.

The current Decision Unit Schema instead states that every pair must be serialized `I1_FIRST` then `I2_FIRST`.

These rules are incompatible.

## Proposed reconciliation

Preserve the already specified deterministic presentation stream and the current generator semantics, and amend the schema's canonical ordering rule to:

1. pair IDs in lexical order `P001` → `P210`;
2. for each pair, the first decision uses the pair's shuffled presentation assignment;
3. the second decision uses the complementary presentation;
4. therefore each pair contains exactly one `I1_FIRST` and one `I2_FIRST`, while pair-level orientation is deterministically randomized.

This makes the presentation stream operational rather than redundant and preserves the generator specification's stated assignment semantics.

## Consequences

- `D001`/`D002` remain the two decisions of `P001`, but their presentation order is determined by the presentation stream.
- Every pair remains complementary.
- The total allocation remains exactly 105 `I1_FIRST` and 105 `I2_FIRST`.
- Condition allocation remains 70/70/70 at pair level.
- No agent-facing information changes.
- No model/API call is involved.
- Fixture generation remains blocked until the reconciliation is approved and the schema and preflights are updated.

## Approval boundary

This artifact is a design reconciliation proposal only. It does not modify the schema, generator, or fixture and does not authorize generation.

`scientific_execution = NOT_PERFORMED`.