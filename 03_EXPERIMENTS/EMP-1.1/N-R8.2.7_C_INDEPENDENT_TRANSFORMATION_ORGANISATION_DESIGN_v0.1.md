# N-R8.2.7 — C Independent Transformation-Organisation Design v0.1

**Status:** PROPOSED — NOT FROZEN
**Date:** 2026-09-05
**Parent:** N-R8.2.6 C Minimal-Relaxation Analysis v0.1
**Design role:** replacement candidate for the blocked N-R8-C full-R inequality construction

## 1. Purpose

N-R8-C originally attempted to create a residual structural contrast by matching low-order summaries of `T_acc` and requiring inequality in the existing 58-dimensional R representation. N-R8.2.5 established that this is structurally impossible under the current Branch N semantics, and N-R8.2.6 rejected relaxing the matched R-derived quantities merely to make the fixture pass.

This document proposes a different construction: retain the low-order controls, but define the contrast using a **second-order organisation structure of `T_acc`** that is not one of the frozen R1–R4 coordinates.

The proposal is intentionally NOT FROZEN. Its first gate is identifiability, not corpus generation.

## 2. Scientific question

The revised C question is:

> When baseline state variables and specified low-order summaries of accessible transformations are held exactly fixed, does the organisation of the accessible transformations themselves contain an independently measurable structural distinction?

The experiment remains representation-qualified. It does not claim a universal or representation-independent notion of higher-order structure.

## 3. Core design principle

The contrast must be a property of the **organisation among accessible transformation instances**, not merely another aggregate count of those instances.

We therefore define a transformation-compatibility graph `G_T(S)` whose nodes are the canonical transformations in `T_acc(S)`.

The representation is based on pairwise compatibility/commutation of transformations and is deliberately distinct from the frozen R1–R4 feature blocks.

No learner, outcome, trajectory, historical result, or N-R7 result enters its construction.

## 4. Transformation-compatibility relation

For two distinct accessible transformations `tau, sigma in T_acc(S)`, define:

`tau ~ sigma`

iff all of the following hold:

1. `sigma` is applicable to the successor state `tau(S)`;
2. `tau` is applicable to the successor state `sigma(S)`;
3. the two ordered compositions produce the same canonical state:

`tau(sigma(S)) = sigma(tau(S))`.

The relation is symmetric by construction because conditions 1–3 are evaluated in both orders.

An undirected edge is placed between the two transformation nodes exactly when `tau ~ sigma`.

This is a second-order property: it depends on relationships between pairs of accessible transformations, rather than only on the marginal counts or component incidences of individual transformations.

## 5. Why this is preferable to modifying R

The frozen R representation is a prospective 58-dimensional representation of `T_acc` with family, incidence, and immediate successor summaries. Its current construction leaves no degree of freedom for the original C requirement once R1–R3 are matched.

The proposed `G_T` does not replace R and does not modify N-R1.3. It creates a separate structural object for the specific purpose of testing organisation among transformations.

Therefore:

- N-R1.2 remains unchanged;
- N-R1.3 remains unchanged;
- N-R7 remains unchanged;
- R remains the primary N-R8 representation;
- `G_T` is a C-specific structural contrast object.

## 6. Candidate scalar representation

To keep the C construction finite-dimensional and pre-specifiable, the initial candidate representation `O_T(S)` is the following fixed vector:

1. `n_nodes = |T_acc|`;
2. `n_edges` in `G_T`;
3. compatibility density `2*n_edges/(n_nodes*(n_nodes-1))`, defined as `0.0` when `n_nodes < 2`;
4. mean node degree;
5. population standard deviation of node degree;
6. number of connected components;
7. size of the largest connected component;
8. population mean local clustering coefficient;
9. number of triangles;
10. degree assortativity, defined as `0.0` when the denominator is zero.

This is a **candidate** vector only. The exact numerical treatment of degenerate cases and assortativity must be frozen only after the identifiability audit.

The vector is not intended to be a replacement learner representation at this stage. Its primary role is pair construction and structural contrast.

## 7. Matching key for revised C

The revised pair constructor retains the controls that were scientifically meaningful in the original design:

`K_C2(S) = (B(S), R_family_availability(S), R_family_cardinality(S), R_component_incidence(S), |T_acc(S)|, family_count(S), n_components(S), resources(S), objective(S))`

The graph edge count is not added separately because it is already determined by R2 family cardinality under the frozen transformation semantics.

A candidate pair A,B is accepted only if:

`K_C2(A) = K_C2(B)`

and

`O_T(A) != O_T(B)`.

The pair may additionally record the complete `G_T` graph hash and canonical graph statistics for provenance.

## 8. Important distinction from the failed C design

The failed design demanded:

`K_C2(A) = K_C2(B)` and `R(A) != R(B)`.

That condition is impossible because the matched quantities determine the current R vector.

The revised design instead demands:

`K_C2(A) = K_C2(B)` and `O_T(A) != O_T(B)`.

This does not assume that `O_T` is automatically independent of K. **Independence is an empirical/design identifiability condition that must be demonstrated before freezing.**

The first task is therefore to find a bounded fixture with equal `K_C2` and unequal `O_T` without consulting outcomes or results.

## 9. Identifiability gate — mandatory before implementation

The design cannot be frozen unless a deterministic bounded search produces at least one non-trivial pair satisfying:

1. exact equality of every component of `K_C2`;
2. exact equality of full R, where expected under the current structural determinism result;
3. exact inequality of `O_T`;
4. both states valid under N-R1.2;
5. identical resources and objective;
6. no outcome or trajectory data;
7. no N-R7 or N-R8 result data.

The fixture search must be deterministic and fail closed.

A useful first fixture family is the complete enumeration of directed-edge subsets for fixed 3- or 4-component sets, with fixed resources and objective. This is a **bounded identifiability search only**, not corpus generation.

If no fixture exists within a justified bounded search, the design remains BLOCKED and must not be promoted by increasing the search limit without a new scientific justification.

## 10. Independence audit

The audit must explicitly test whether each candidate `O_T` coordinate is a deterministic function of the matching key.

The audit shall classify each coordinate as:

- **IDENTIFIABLE:** a bounded counterexample exists with equal K and different coordinate;
- **DERIVED:** coordinate is mathematically determined by K;
- **UNRESOLVED:** bounded search is insufficient to establish either status.

Only coordinates classified IDENTIFIABLE may be retained in the final contrast vector.

This prevents selecting a statistic merely because it happens to differ in an unexamined fixture.

## 11. Scientific interpretation

A successful revised C experiment could support only the following narrow interpretation:

> Outcome/predictive differences remain associated with an independently measured organisation-level property of the accessible transformation space after the specified low-order summaries are matched.

It could NOT establish:

- a universal higher-order structure;
- a unique causal mechanism;
- representation-independent superiority of `G_T`;
- or that any particular graph statistic is the causal carrier.

Feature-level attribution remains exploratory.

N-R8-D retains its independent-representation role and is not replaced by this construction.

## 12. Computational constraints

The compatibility graph requires pairwise transformation checks. This may be substantially more expensive than the current R encoding.

Accordingly, no 5,000-pair target or implementation budget is inherited into this design until a bounded complexity analysis is completed.

The first implementation gate must operate on a microscopic fixture and record:

- number of transformations;
- number of transformation pairs examined;
- number of valid ordered compositions;
- number of compatibility edges;
- deterministic graph serialization hash;
- runtime and memory diagnostics.

These diagnostics do not enter the scientific representation unless explicitly frozen later.

## 13. Determinism requirements

The revised construction must use:

- canonical transformation ordering from N-R1.2;
- canonical state ordering from N-R1.2;
- deterministic pair enumeration;
- deterministic graph serialization;
- fixed numerical conventions;
- no hash-map iteration as a scientific ordering source;
- no ambient global RNG state.

Identical input state must produce byte-identical `G_T` and `O_T`.

## 14. Leakage and anti-retrofitting rules

Forbidden inputs include:

- Y;
- realized trajectory;
- terminal state;
- learner predictions;
- losses;
- p-values;
- N-R7 results;
- historical EMP-1.1 results;
- test-set performance;
- any result used to select or discard candidate graph statistics.

The candidate vector must be selected before the identifiability fixture search is interpreted as a success/failure criterion, and any revision requires a new version.

## 15. Relationship to N-R8-D

N-R8-D asks whether predictive utility persists under an independently specified 24-dimensional representation of `T_acc`.

Revised C asks a different question: whether a second-order organisation property of `T_acc` can be contrasted while the specified low-order R summaries are matched.

A later agreement between C and D would be convergent evidence. A disagreement would keep the interpretation representation-qualified.

Neither result may be used retrospectively to alter the other representation.

## 16. Gate status

**N-R8-C2 STATUS: PROPOSED — IDENTIFIABILITY PENDING.**

Current status:

- N-R8-C original full-R inequality: **BLOCKED / SUPERSEDED**;
- N-R8-C2 independent organisation design: **PROPOSED**;
- implementation: **NOT STARTED**;
- fixture search: **NOT STARTED**;
- 5,000-pair corpus: **NOT AUTHORIZED**;
- scientific execution: **NOT PERFORMED**;
- N-R7: **INTACT / UNMODIFIED**.

## 17. Next gate

The next action is **not** to modify the existing constructor. It is to implement a tiny, isolated identifiability probe for `G_T`/`O_T` on bounded fixtures only.

The probe must answer one question:

> Does there exist at least one pair with identical K and genuinely different transformation-organisation structure?

Only a PASS to that question authorizes a subsequent conformance design.
