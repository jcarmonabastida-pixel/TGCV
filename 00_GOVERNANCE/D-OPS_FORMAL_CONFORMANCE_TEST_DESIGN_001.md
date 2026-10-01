# TGCV — Transformational Dynamics Formal Conformance Test Design 001

**Status:** DESIGN DRAFT — NOT EXECUTED  
**Date:** 2026-10-01  
**Purpose:** define a minimal controlled conformance test for the v0.3 Transformational Dynamics formalization. This is formal/methodological validation, not empirical cross-domain validation.

## 1. Test boundary

The test instantiates Ω_T,t = (U_t, ≡_t, R_t) in a finite deterministic planning environment whose domain rules are frozen independently of generated trajectories.

PDDL is suitable for this controlled layer because domain files explicitly define predicates and actions, while formal planning work provides reproducible finite-state representations and explicit domain legality conditions. citeturn0search1turn0search2turn0search16

No real-world outcome, reward, utility, planner success, or downstream trajectory metric defines Ω_T.

## 2. Minimal formal environment

Use one frozen finite planning domain D0 with:

- finite typed objects;
- finite predicates;
- finite grounded action universe;
- explicit preconditions/effects;
- deterministic transitions;
- no numeric reward;
- no goal-dependent definition of transformation identity.

The canonical transformation identity is the grounded action operator, after parameter grounding and canonical normalization.

## 3. Primary object

For a frozen problem instance:

- U_t = canonical grounded action identities;
- ≡_t = alpha-renaming / canonical-grounding equivalence;
- R_t contains declared structural relations only.

Initial relation signature:

1. **Precondition-support:** action → predicate instances required for applicability.
2. **Effect-production:** action → predicate instances changed/produced.
3. **Action-interaction:** action → action when their declared effects/preconditions satisfy the frozen interaction rule.

No relation is inferred from observed execution frequency or plan success.

## 4. Controlled transformations

Construct four known states of the formal environment:

- **PERSISTENCE:** identical domain structure.
- **EXPANSION:** add one pre-specified valid action operator.
- **CONTRACTION:** remove one pre-specified valid action operator.
- **RECONFIGURATION:** preserve action identities but alter one pre-specified structural relation without changing action cardinality.

The expected descriptor is declared before execution.

## 5. Representation-invariance test

Create an admissible representation E' by applying only semantics-preserving transformations:

- rename symbols under the canonical mapping;
- reorder declarations;
- reorder conjuncts where semantically commutative;
- normalize equivalent syntactic forms.

The expected structural descriptor must remain unchanged.

A representation change that alters the descriptor is a FAIL for representation invariance. This is particularly important because planning research documents that alternative domain/problem representations can affect computational behaviour; therefore the test must distinguish representation artefact from structural semantics. citeturn0search15

## 6. Structural-null test

Construct paired representations with identical Ω_T structure but altered:

- object names;
- declaration order;
- initial state values;
- irrelevant state variables;
- planner/execution ordering.

The Ω_T descriptor must remain **PERSISTENCE** when the declared domain structure is unchanged.

This null is formal and controlled; it does not claim that an empirical null has been established.

## 7. State-reducibility test

Create paired instances where state variables change substantially while the domain-level Ω_T remains identical.

Then create a separate pair where the domain structure changes while a selected state snapshot is held constant.

The decision procedure must distinguish:

- state-only variation → no Ω_T change;
- structural variation → corresponding Ω_T change.

No post-hoc state variable selection is permitted.

## 8. Comparability test

Run:

A. same canonical universe and relation signature → comparable;
B. symbol-renamed equivalent universe under frozen correspondence κ → comparable;
C. incompatible transformation semantics → NON-COMPARABLE.

The test must not classify case C as expansion/contraction/reconfiguration.

## 9. Conditional-reorganization conformance

Use condition-indexed copies of the same formal environment.

Under H0, conditions alter only state values while Ω_T is invariant.

Under H1, a pre-specified condition changes a structural relation in Ω_T.

The detector must classify H0 as no structural change and H1 as conditional reorganization, without using outcomes.

## 10. Falsification matrix

| Test | Expected result | Failure meaning |
|---|---|---|
| Identity normalization | same identities | identity rule inadequate |
| Persistence | persistence | false positive dynamics |
| Expansion | expansion | missed structural addition |
| Contraction | contraction | missed structural removal |
| Reconfiguration | reconfiguration | relation semantics inadequate |
| Representation perturbation | invariant | representation-sensitive |
| Structural null | no change | null failure |
| State-only variation | no change | state-reducibility failure |
| Structural change at fixed state | change detected | insufficient structural sensitivity |
| Incomparable snapshots | NON-COMPARABLE | temporal gate failure |
| Conditional H0 | no reorganization | conditional false positive |
| Conditional H1 | reorganization | conditional sensitivity failure |

## 11. Execution boundary

This document authorizes **design only**.

Before execution, freeze:

1. exact PDDL domain/problem files;
2. SHA-256 hashes;
3. canonicalization algorithm;
4. relation-construction algorithm;
5. four structural perturbations;
6. representation perturbation set;
7. null cases;
8. state-only comparison cases;
9. expected classifications;
10. deterministic executor/version.

Execution must produce a machine-readable result and an independent audit artifact.

## 12. Decision

**READY FOR FREEZE-GATE REVIEW — NOT AUTHORIZED FOR EXECUTION.**

The design now provides a minimal controlled conformance test of v0.3 without treating formal trajectories as empirical evidence.

