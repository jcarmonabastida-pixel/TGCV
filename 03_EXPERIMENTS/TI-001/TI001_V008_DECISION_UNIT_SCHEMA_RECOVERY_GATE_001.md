# TI-001 V008 Decision Unit Schema Recovery Gate 001

**Status:** RECOVERY BLOCKED — CANONICAL SCHEMA NOT LOCATED
**Scientific execution:** NOT_PERFORMED
**Fixture generated:** false
**Generation authorized:** true

## Purpose

Record the unresolved dependency between V008 deterministic fixture generation and the exact canonical Decision Unit schema.

This gate prevents an inferred or newly invented schema from being treated as recovered prior design.

## Evidence reviewed

The current canonical V008 Generator Specification defines:

- 210 pairs;
- 70 control, 70 treatment, 70 null;
- 420 decision instances;
- 105 I1_FIRST and 105 I2_FIRST;
- actions A/B;
- treatment-only future structure;
- hidden condition, pair identity and variant;
- no successor realization before decision;
- no utility/reward/value/performance feedback.

It does not define the complete materialized Decision Unit record schema, field types, canonical record ordering, or exact serialization of the presented decision context.

The repository search performed for TI-001 Decision Units, V007 decision-unit fixtures, assignment fields, and the Decision Units Integrity Preflight did not locate an accessible canonical artifact containing those definitions.

## Recovery rule

No field, ordering rule, context representation, or serialization rule may be inferred from:

- the V008 generator implementation;
- previous assistant reasoning;
- an analogous experiment;
- an undocumented V007 reconstruction;
- generated output.

## Scientific boundary

This is a design-recovery/integrity activity only.

`scientific_execution = NOT_PERFORMED`

No model/API call or scientific execution is permitted.

## Gate decision

**BLOCKED.**

The V008 fixture cannot be generated reproducibly until the canonical Decision Unit schema is recovered or a new V008 schema is explicitly designed and assigned a new design identity.

## Next action

Perform a targeted canonical repository recovery for the original TI-001 Decision Unit specification and its associated preflight/fixture artifacts.

If no canonical schema is recoverable, stop recovery and open a separate V008 Decision Unit Schema Design Gate rather than silently inventing one.
