# TGCV TR-131 — Formal Irreducibility Assessment Specification 001

**Status:** CANDIDATE — NOT EXECUTED
**Scientific execution:** NOT AUTHORIZED
**Date:** 2026-09-20

## 1. Purpose
Assess, separately from the frozen TR-131 execution, whether the realization dependence identified by TR-131 is irreducible with respect to an explicitly declared class of admissible pre-realization representations.

This assessment does not modify the frozen TR-131 package and does not itself establish that Pi is a TGCV Core primitive.

## 2. Starting evidence
The assessment inherits only the following closed scientific finding:
- (S,C,T_acc)_A = (S,C,T_acc)_B
- X_A != X_B
- H_A != H_B
- TR-131 disposition: POSITIVE — REPRESENTATION INSUFFICIENCY.

The assessment must not treat the observed TR-131 outcome as an input variable for constructing a candidate representation.

## 3. Object of assessment
Let the tested realization relation be Pi : (S,C,T_acc,X) -> T_real.

The assessment asks whether there exists an admissible representation R and deterministic realization rule F such that T_real = F(R,T_acc), where R is determined entirely from pre-realization system information and does not receive X, Pi, T_real, H, O, or V as a separate post hoc input.

A representation may be an expanded state/context pair R=(S',C') with S'=G_S(S,C,X) and C'=G_C(S,C,X), only where the mappings have independently declared semantics and are not merely aliases for X.

## 4. Scope of irreducibility
Irreducible is always relative to the declared representation class.

The assessment must specify: the source ontology of admissible pre-realization variables; allowed representation mappings; allowed deterministic realization functions; equivalence criteria; and prohibited encodings.

No conclusion may claim absolute or universal irreducibility beyond this declared class.

## 5. Admissible representation class
A candidate representation is admissible only if:
1. Every component has a pre-realization semantic interpretation.
2. Its value can be established before T_real.
3. Its semantics are specified independently of observed T_real, H, O and V.
4. It does not simply rename, serialize, index or copy X.
5. It does not encode the realized transformation or trajectory.
6. It is stable under the declared counterfactual transformations.
7. Its semantics are independently reproducible without seeing the assessment outcome.

## 6. Prohibited constructions
Invalid constructions include R=X, encode(X), label(X), R containing X as the unexplained operative determinant, R=T_real, R=H, R=O, R=V, or any mapping fitted after observing the assessment outcome.

An isomorphic relabelling is not absorption.

## 7. Elimination criterion
Pi is eliminable within the declared representation class only if a single deterministic rule exists: T_real = F(R,T_acc), reproducing all admissible realization behavior in the declared test domain without a separate X or Pi input.

The rule must be fixed before evaluation of target cases.

## 8. Irreducibility criterion
Pi is irreducible within the declared representation class only if:
1. the class is completely specified;
2. every admissible candidate is formally ruled out or shown insufficient;
3. no prohibited post hoc information is used;
4. the result is robust to declared counterfactuals;
5. the procedure is independently reproducible.

Failure to construct one representation is not sufficient by itself to establish irreducibility.

## 9. Completeness requirement
Because irreducibility is universal over a representation class, an open-ended search cannot establish formal irreducibility.

Route A: the admissible class is finite or otherwise exhaustively enumerable.

Route B: a formal impossibility argument rules out every admissible representation in the declared class.

If neither route is available, the only valid result is INCONCLUSIVE — REPRESENTATION CLASS NOT CLOSED.

## 10. Outcomes
PASS — IRREDUCIBLE WITHIN DECLARED CLASS: the class is closed and exhaustive or formally ruled out, while realization dependence survives.

FAIL — REDUCIBLE: at least one admissible non-tautological representation eliminates Pi.

INCONCLUSIVE — CLASS NOT CLOSED / IDENTIFICATION UNRESOLVED: the representation class, semantic basis or elimination procedure is incomplete.

## 11. Core boundary
Even PASS does not automatically modify TGCV Core. A separate governance decision must determine whether an irreducible realization layer is represented as a Core primitive, derived construct, auxiliary layer or another architectural element.

## 12. Independence
Executor-2 must independently reconstruct the assessment from the frozen assessment package and must not receive target results, interpretations, post hoc representation proposals, outcome-driven candidate definitions or coaching toward a desired classification.

## 13. Required package
Before authorization the repository must contain: this specification; formal representation-class definition; semantic-basis definitions; candidate mappings; prohibited-construction tests; elimination-rule definition; counterexample generator or proof procedure; counterfactual specification; output schema; integrity manifest; executor instructions; independent audit worksheet; environment specification; and explicit inference boundary.

## 14. Pre-execution gates
G1 — Representation-class closure.
G2 — Semantic independence.
G3 — Anti-tautology.
G4 — Elimination rule.
G5 — Counterexample / proof procedure.
G6 — Independent reconstruction.
G7 — Integrity.
G8 — Authorization.

Scientific execution is authorized only after G1-G7 pass.

## 15. Current disposition
TR-131 scientific finding: CLOSED — POSITIVE / REPRESENTATION INSUFFICIENCY.
Expanded-state operationalization from frozen semantics: BLOCKED.
Independent semantic basis currently identified in repository: NONE.
Formal irreducibility assessment: CANDIDATE — NOT EXECUTED.
Scientific authorization: NOT AUTHORIZED.

## 16. Immediate next gate
FORMAL IRREDUCIBILITY DESIGN AUDIT.

The next operation is to audit whether the declared representation class is actually closed enough to support a scientific irreducibility claim. If it is not closed, the assessment must stop at INCONCLUSIVE rather than manufacture completeness.