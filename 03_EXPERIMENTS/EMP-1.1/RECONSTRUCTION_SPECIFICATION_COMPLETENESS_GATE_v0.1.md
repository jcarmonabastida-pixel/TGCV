# TGCV-EMP-1.1 — Reconstruction Specification Completeness Gate v0.1

**Date:** 2026-09-05  
**Status:** **BLOCKED — SPECIFICATION INCOMPLETE**  
**Purpose:** determine, before implementation, which elements of the historical EMP-1.1 operationalisation are recoverable without post-hoc scientific choices.

## 1. Scope and boundary

This gate audits only the reconstruction specification for EMP-1.1. It does **not** reopen TGCV Core, R* v0.2, the frozen EMP-1.1 protocol, or the historical numerical result.

The reconstruction target remains:

`S_snapshot -> T_acc -> R -> learner features`

The historical executable MVE-1.0 implementation remains unrecovered. Therefore a result of this gate cannot convert any reconstructed element into a historical artifact.

## 2. Source hierarchy inspected

The following repository artifacts were inspected:

1. `03_EXPERIMENTS/EMP-1.1/Experimental_Protocol_v1_1.json`
2. `03_EXPERIMENTS/EMP-1.1/EMP-1.1_RECONSTRUCTION_INPUTS.md`
3. `03_EXPERIMENTS/EMP-1.1/EMP-1.1_R_RECONSTRUCTION_SPEC_v0.1.md`
4. `03_EXPERIMENTS/EMP-1.1/EMP-1.1_RECONSTRUCTION_GATE_v0.2.md`
5. `03_EXPERIMENTS/EMP-1.1/EMP-1.1_REPRODUCIBILITY_RECONSTRUCTION_PLAN.md`

The protocol explicitly freezes the representation-level hypothesis, estimand, sample sizes, seeds, primary learner family, permutation test, controls, baseline B, and the statement that R is derived from accessible transformations at the frozen snapshot. The reconstruction inputs explicitly enumerate the still-missing executable details. The existing reconstruction specification independently lists the unresolved transformation/accessibility and encoding semantics.

## 3. Classification rule

- **SPECIFIED:** directly fixed by a frozen artifact.
- **DERIVED:** uniquely determined by specified artifacts with no remaining implementation choice.
- **RECONSTRUCTED:** requires a new explicit implementation choice, even if scientifically reasonable.
- **OPEN:** cannot be safely resolved from the current record without introducing an assumption that could affect the empirical result.

For this gate, an element is treated as closed only if it is `SPECIFIED` or `DERIVED`. `RECONSTRUCTED` elements require an explicit pre-implementation decision; `OPEN` elements block implementation.

## 4. Completeness matrix

| Element | Classification | Evidence / finding | Gate consequence |
|---|---|---|---|
| Representation-level hypothesis | SPECIFIED | Frozen protocol states that R adds reproducible out-of-sample predictive utility beyond B. | CLOSED |
| Primary estimand | SPECIFIED | `Delta = LL_B - LL_B+R`. | CLOSED |
| Alpha / historical delta threshold | SPECIFIED | alpha `0.05`; delta `0.04`. | CLOSED |
| Confirmatory train/test sizes | SPECIFIED | 30,000 train; 10,000 locked test. | CLOSED |
| Training/test seeds | SPECIFIED | 3,100,000 / 4,100,000. | CLOSED |
| Primary learner family | SPECIFIED | HistGradientBoostingClassifier, identical fixed hyperparameters in both arms. | CLOSED at family level; hyperparameter dictionary remains OPEN |
| Sign-flip test | SPECIFIED | 200,000 flips, seed 13,579, per-test-episode paired log-loss differences. | CLOSED |
| Controls | SPECIFIED | count-only R, permuted-marginals R, RandomForest alternative. | CLOSED at control identity level; RF configuration remains OPEN |
| Baseline B fields | SPECIFIED | component count + three resource values + objective identity; excludes relational edge structure. | CLOSED at semantic field level |
| Snapshot boundary | SPECIFIED | R is derived at the frozen snapshot; no-retrofit rule prohibits future trajectory/outcome leakage. | CLOSED conceptually; exact episode schema remains to be verified |
| Exact six transformation-family definitions | OPEN | Explicitly listed as missing in reconstruction inputs/spec. No frozen artifact inspected supplies the predicates. | **BLOCKING** |
| Exact edge semantics | OPEN | Existing record does not uniquely determine how directed edges participate in transformation predicates. | **BLOCKING** |
| Exact transition/update equations | OPEN | Historical executable transition implementation is explicitly unrecovered. | **BLOCKING** |
| Accessibility closure rule | OPEN | `T_acc` is named but the operational closure/feasibility rule is not frozen. | **BLOCKING** |
| Exact aggregation `T_acc -> R` | OPEN | R is described as accessible-transformation structure, but no complete encoding is specified. | **BLOCKING** |
| R feature ordering | OPEN | No frozen feature ordering found. | **BLOCKING** |
| Empty/degenerate T_acc handling | OPEN | No deterministic rule found. | **BLOCKING** |
| Normalisation / categorical encoding | OPEN | Not specified in the recovered record. | **BLOCKING** |
| Exact component/resource/objective domains | OPEN | Field identities are known, but exact domains/encodings are not. | **BLOCKING** |
| Exact HGB hyperparameters | OPEN | Protocol says fixed hyperparameters but does not record the dictionary. | **BLOCKING** |
| Exact RandomForest configuration | OPEN | Control identity is frozen; configuration is not. | **BLOCKING** |
| Data-generation implementation | OPEN | Generator source/complete executable procedure not recovered. | **BLOCKING** |
| Pilot generation procedure and seed | OPEN | Explicitly listed as missing. | **BLOCKING** for historical reconstruction; not needed if a new independent protocol is designed |
| 20,000-episode pilot fold construction | OPEN | Explicitly listed as missing. | **BLOCKING** for exact historical reconstruction |
| Integrity / no-retrofit rule | SPECIFIED | Frozen protocol and reconstruction plan prohibit tuning against final result. | CLOSED |
| Historical final result as acceptance criterion | SPECIFIED | May be compared only after independent construction; never used to resolve ambiguity. | CLOSED |

## 5. Determination

The specification is **not complete enough to implement the historical EMP-1.1 operationalisation without introducing material choices**.

The blocking items are not cosmetic. In particular, transformation predicates, transition equations, accessibility closure, and the mapping from `T_acc` to R jointly determine the representation whose predictive utility is being tested. Choosing them now would define a new operationalisation rather than recover the historical one.

The same applies to missing model hyperparameters, generator details, pilot construction, and encoding choices if the objective is exact reproduction of the historical computation.

## 6. What can already be frozen for a controlled reconstruction

The following may be inherited without reopening the scientific hypothesis:

- TGCV Core interpretation used by EMP-1.1;
- representation-level hypothesis and null;
- primary estimand and decision rule;
- sample sizes and seeds;
- baseline B semantic fields;
- control identities;
- no-retrofit rule;
- provenance distinction between HISTORICAL, SPECIFIED, DERIVED, RECONSTRUCTED and VERIFIED;
- the boundary that a reconstruction is **not** recovery of MVE-1.0.

These do not, by themselves, define the missing transformation/accessibility semantics.

## 7. Prohibited actions while blocked

Until the blocking specification items are resolved:

1. do not implement a canonical EMP-1.1 R reconstruction;
2. do not select transformation families by inspecting the recorded result;
3. do not tune hyperparameters to reproduce `Delta=0.07942359585`;
4. do not treat the historical numerical result as proof that any newly chosen R definition is the historical R;
5. do not modify R* v0.2;
6. do not rerun A/B/C as though this reconstruction were already validated.

## 8. Next admissible gate

The next step is a **RECONSTRUCTION SEMANTICS RECOVERY / NEW-OPERATIONALISATION DECISION** with two explicitly separated branches:

- **Branch H — historical recovery:** continue searching only for admissible frozen/historical artifacts that uniquely determine the missing semantics. If none are found, historical exact reproduction remains unavailable.
- **Branch N — controlled new reconstruction:** if the research program elects to proceed, define every missing semantic element prospectively, label it `RECONSTRUCTED`, freeze it before sealed-test evaluation, and treat the resulting experiment as a new controlled reconstruction rather than historical recovery.

No branch is selected by this gate itself.

## 9. Gate decision

**RECONSTRUCTION SPECIFICATION COMPLETENESS = FAIL / BLOCKED**

**Historical executable recovery = NOT ESTABLISHED**

**Controlled reconstruction = PERMITTED, but not yet specified completely**

**Canonical EMP-1.1 historical result = PRESERVED AS HISTORICAL RECORD**

**R* v0.2 = UNCHANGED**
