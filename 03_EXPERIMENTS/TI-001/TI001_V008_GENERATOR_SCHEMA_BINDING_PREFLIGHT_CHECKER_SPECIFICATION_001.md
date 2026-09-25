# TI-001 V008 Generator–Schema Binding Preflight Checker 001

**Status:** READY — NOT EXECUTED
**Scientific execution:** NOT_PERFORMED
**Fixture generated:** false

## Purpose

Validate the committed V008 generator implementation against the approved Decision Unit Schema before any fixture generation.

## Canonical bindings

- Schema ID: `TI001-V008-DU-SCHEMA-001`
- Schema blob SHA-1: `e0da4352f74a518f7e1bc7c9532a171bf5167735`
- Generator ID: `TI001-V008-FIXTURE-GENERATOR-001`
- Generator implementation commit: `ec83e8bea30717b5f084d2c3f0411a5743ffdce4`
- Generator blob SHA-1: `f345c41371a189c43b69b707b49b7eb17d140f55`

## Required checks

The executable checker MUST verify the Git blob SHA-1 of both source artifacts and verify:

1. generator identity;
2. approved schema identity and SHA binding;
3. generator source commit/blob binding;
4. deterministic self-test PASS;
5. 210 pair / 420 Decision Unit materialization;
6. 70/70/70 condition allocation;
7. complementary I1_FIRST/I2_FIRST presentation within every pair;
8. exact seven Decision Unit fields and nested field order;
9. treatment/control/null future-structure mapping;
10. exact top-level fixture field order;
11. compact UTF-8 JSON and single final LF;
12. fixture SHA-256 calculation;
13. external integrity manifest binding;
14. generation remains blocked unless an explicit binding manifest is supplied;
15. Executor-2 reconstruction independence;
16. scientific execution remains `NOT_PERFORMED`.

## Gate rule

PASS means the implementation is conformant and bound to the approved schema. PASS does not itself authorize fixture generation; the separate Fixture Generation Gate remains required.