# C10-S — Addendum al plan de cierre, Gate 137: docket UNKNOWN/frontera

**Fecha:** 2026-11-16  
**Registro:** C10_S_UNKNOWN_AND_INTERVAL_BOUNDARY_DECISION_DOCKET_GATE_137_DRAFT_001.md  
**Rama:** research/c10-s-consolidation-draft · PR #116 Draft  
**Estado:** DECISION_DOCKET / USER_ACCEPTANCE_PENDING / NO_CODE_CHANGE / NO_EXECUTION.

La reconstrucción de DEC-C10-100…102, Decision Log hasta DEC-C10-103, DGP §§48–55 y plan §§16.193–198 no encuentra una causa intrínseca ya aceptada para generar UNKNOWN funcional de A_B1. P182/P183/MEAS/MISS describen missingness/error/lag/censura del canal de observación y no autorizan convertirlos en UNKNOWN de truth. Se recomienda no emitir ? por defecto en historias sintéticas completas y deterministas; conservar la semántica tri-valuada y permitir ? únicamente tras estipulación DGP explícita, con condición semántica y provenance reservada. No se inventa aquí esa condición.

La convención semiabierta [b_{k−1},b_k) para intervalos internos y cierre inclusivo de T* aparece de forma consistente como recomendación en DGP §49 y plan §§16.193.4, 16.195, 16.198.2. DEC-C10-102 exige una asignación determinista, única y versionada, pero no adopta esa convención. No se localiza aceptación posterior hasta DEC-C10-103. Se propone su aceptación expresa, sin fijar parámetros temporales.

No se crea DEC-C10-104 hasta recibir aceptación; no se cambia el Decision Log ni se implementa nada. Siguiente tras la decisión: crosswalk de conformidad hacia Generator/TruthBundle/Sealer/Analyzer/Evaluator.

scientific_execution=false; execution_authorized=false.


## Acceptance outcome — 2026-11-16

The user explicitly accepted both proposals. DEC-C10-104 now records the semi-open interval convention and the conservative Generator UNKNOWN rule as accepted working design decisions. Internal-boundary events belong to the interval beginning at that boundary; T* belongs to the final interval. Functional ? is not emitted in complete determinate histories and cannot arise from S3 missingness, incomplete DGP/harness representation or implementation defects. It requires a future explicit DGP contract defining intrinsic A_B1 indeterminacy.

The tri-valued state space and bounds in DEC-C10-100 remain unchanged. No numerical temporal parameters are fixed. This does not authorize implementation, schema/test changes, materialization or execution; no Design Freeze.
