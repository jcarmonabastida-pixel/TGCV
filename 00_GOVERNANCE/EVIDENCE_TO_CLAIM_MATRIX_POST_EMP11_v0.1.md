# TGCV — Evidence-to-Claim Matrix Post-EMP-1.1 v0.1

**Status:** Governance control artifact
**Purpose:** Prevent scientific claims in downstream assets from exceeding the evidence currently available.

## 1. Governing rule

Every substantive scientific claim must be traceable to evidence, an explicit inference, or an identified hypothesis. No downstream document may silently upgrade a hypothesis into an empirical fact.

## 2. Claim classes

- **E0 — Defined:** semantic/model definition; not an empirical claim.
- **E1 — Supported:** directly supported by current empirical evidence within its tested scope.
- **E2 — Indirectly supported:** consistent with evidence but not directly tested.
- **H — Hypothesis:** requires further empirical testing.
- **O — Open:** insufficiently specified or currently untestable.
- **F — Falsified:** contradicted by valid evidence under the relevant scope.

## 3. Core claims

| ID | Claim | Status | Current evidence / basis | Next gate |
|---|---|---|---|---|
| C01 | Systems may be represented in terms of state, context and constraints/resources | E0 | Model definition | Cross-domain justification |
| C02 | Accessibility can be represented as a set/structure of accessible transformations | E0 | Formal definition + EMP-1.1 operationalisation | Independent operationalisation |
| C03 | The tested relational accessibility representation contains predictive information beyond the tested baseline | E1 | EMP-1.1 | Independent replication |
| C04 | The observed effect is not adequately explained by accessibility cardinality alone | E1 | Count-only control | Independent replication |
| C05 | Arbitrary permutation of the tested relational accessibility structure does not reproduce the observed advantage | E1 | Permutation control | Independent replication |
| C06 | Changes in accessibility modify reachable future trajectories | H | Core theoretical relation | Direct trajectory test |
| C07 | Accessibility changes causally affect subsequent trajectories | H | Not directly established by EMP-1.1 | Causal identification / intervention |
| C08 | Accessibility changes can systematically generate or predict value | H | Programme objective, not tested | Value-linked empirical test |
| C09 | TGCV is domain-independent | H | No cross-domain evidence yet | External replication/generalisation |
| C10 | TGCV provides a superior explanatory representation across relevant alternatives | H | Not established globally | Comparative tests |

## 4. Evidence interpretation

The strongest current empirical statement is C03. It should not be expanded in public or internal documents into C06–C10 without new evidence.

EMP-1.1 is evidence about its **sealed operationalisation and tested environment**. It is not evidence that every semantic or causal layer of TGCV has been validated.

## 5. Asset mapping

| Asset | Claims permitted without additional evidence |
|---|---|
| Scientific State | C01–C05, with scope explicitly bounded |
| Research Prospectus | C01–C10, provided statuses are explicit |
| Vision Paper | C03 as bounded first empirical evidence; C06–C10 as open programme questions |
| Core & Ontology | C01–C02; C06–C10 remain provisional/open |
| Formal Model | Formal definitions plus explicit hypotheses; no unsupported theorem claims |
| Reference Architecture | Architecture semantics; only C03 marked empirically supported |
| Methodology | Current workflow as provisional programme output; not a validated universal methodology |
| Impact Roadmap | Impact hypotheses only; no unvalidated benefit claims |

## 6. Evidence gates

### Gate G1 — Replication
Independent operationalisation reproduces or challenges C03 under pre-specified conditions.

### Gate G2 — Generalisation
Evidence across an external domain/dataset establishes the scope of the accessibility effect.

### Gate G3 — Trajectory
A valid design tests whether accessibility changes alter reachable or realised trajectories.

### Gate G4 — Value
A valid design tests whether trajectory/accessibility changes translate into measurable practical value.

### Gate G5 — Methodological generalisation
Repeated research cycles establish whether the Programme's methodology itself is reproducible and transferable.

## 7. Anti-inflation rule

If a document contains a stronger claim than the matrix permits, the document must be revised or the claim must be linked to new evidence and a new matrix version.

## 8. Update rule

The matrix is updated after each material empirical result, not after each editorial revision. Historical versions remain immutable and traceable.

## 9. Current scientific position

**Positive evidence exists. General validation does not.**

The scientific task is therefore to increase evidential scope, test boundary conditions, and determine which parts of the theoretical chain survive independent scrutiny.
