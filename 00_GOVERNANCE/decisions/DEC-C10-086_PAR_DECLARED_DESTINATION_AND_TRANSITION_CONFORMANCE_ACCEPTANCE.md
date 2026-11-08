# DEC-C10-086 — Aceptación de conformidad del destino declarado y de la transición F1/A1→F2/A2

**Fecha:** 2026-11-08  
**Estado:** ACCEPTED — DOCUMENTAL  
**Ámbito:** C10-S, rama `research/c10-s-consolidation-draft`

## 1. Decisión

Se acepta el contrato documental de la matriz abstracta de mapping §15.5 y su crosswalk IAM §10.15 para las comparaciones independientes:

- F: `F1_S2 → F2_DST_DECL`.
- A: `A1_S1 → A2_DST_DECL`.

La aceptación incluye la separación de dos dimensiones no compensables: conformidad semántica del destino declarado (`P-DECL`) y conformidad probatoria de la transición (`P-TRANS`).

## 2. P-DECL — conformidad semántica del destino declarado

Se evalúa por parámetro/regla y por ruta si F2/A2 declarada conserva el significado lógico de F1/A1. Incluye estado PAR, tipo/dominio/valor, preservación semántica de `RUL-SVC-ENABLE-PROFILE-01`, e identidad y alcance exactos.

Se aplican DEC-C10-068 y DEC-C10-084: BOOL con equivalencia exacta; ENUM mediante biyección total, inyectiva y versionada sobre STANDARD/READ_ONLY/DISABLED; regla con semántica REQUIRE y operandos/scope conservados mediante mapping aprobado. No se infiere equivalencia por igualdad nominal ni se aceptan coerciones implícitas.

## 3. P-TRANS — conformidad probatoria de la transición

Se exige evidencia íntegra y trazable que vincule la salida intermedia exacta con el artefacto destino declarado exacto y sustente que este es producto de la transición identificada. Deben poder resolverse entradas/salidas, proceso, mappings/versiones, procedencia, captura, integridad y cobertura.

La equivalencia entre artefactos no prueba que el proceso haya producido el destino. Una declaración o enlace sin evidencia del proceso no basta.

## 4. Unidad y adjudicación

F y A se adjudican independientemente. Cada resultado conserva su vector por parámetro, regla y predicado. No hay compensación entre rutas ni entre P-DECL y P-TRANS.

- `PASS`: equivalencia semántica o lineage demostrado, según dimensión, con identidad, mapping, observación, cobertura y evidencia suficientes.
- `FAIL`: diferencia semántica o contradicción de lineage demostrada con cobertura suficiente.
- `UNKNOWN`: artefacto, observación, cobertura, mapping, lineage o evidencia insuficientes.
- `NOT_COMPARABLE`: incompatibilidad de versiones/namespaces sin mapping aprobado.
- `NA`: inaplicabilidad ex ante justificada; no admisible para estos PAR/RUL en las rutas del contrato base.

La falta de registro no demuestra ABSENT ni que la transición no ocurrió. FAIL requiere contradicción o ausencia exhaustivamente demostrada dentro de universo/cobertura cerrados. La reconciliación SM/FP vigente evita predicados duplicados y doble contabilización.

## 5. Frontera con aplicación efectiva

F2/A2 declaradas no equivalen a F2/A2 aplicadas. Esta decisión no adjudica instalación, activación ni estado runtime. La aplicación/observación post-aplicación queda en FP-06/FP-07 y las etapas `F2_DST_APPLIED`/`A2_DST_APPLIED`.

## 6. Límites y no autorizaciones

Decisión documental. No define mappings físicos, codificaciones, tolerancias ni oráculo; no crea registros reales, fixtures, columnas o FK; no sella IAM; no autoriza parser, validator, implementación, Design Freeze ni ejecución científica. No modifica `main`, RMA, Evidence→Claim Matrix ni STATUS.

`scientific_execution=false`; `execution_authorized=false`.
