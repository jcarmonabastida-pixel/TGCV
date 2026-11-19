# DEC-C10-085 — Aceptación de predicados de adjudicación PAR en rutas F1 y A1

**Fecha:** 2026-11-08  
**Estado:** ACCEPTED — DOCUMENTAL  
**Ámbito:** C10-S, rama research `research/c10-s-consolidation-draft`

## 1. Decisión

Se acepta el contrato documental de predicados de adjudicación para las transiciones `C_SRC → F1_S2` y `C_SRC → A1_S1`, tal como se especifica en la matriz abstracta de parámetros §15.3, con la precisión obligatoria de reconciliar las familias de comprobación con el catálogo SM/FP aceptado y evitar duplicidad o doble contabilización.

## 2. Unidad y separación de adjudicación

La adjudicación se realiza independientemente por ruta y por parámetro/regla, fijando contrato e instancia/versiones, CMP owner, snapshots y registros exactos, `stage_key`, `route_id/route_record_id`, `coverage_scope_id`, clave PAR o regla y `mapping_id/version`.

F1 y A1 no se compensan ni se imputan mutuamente. Un resultado agregado no puede ocultar el vector de estados por predicado.

## 3. Familias reconciliadas con SM/FP

Se aceptan como familias organizadoras, no como nuevos predicados confirmatorios duplicados:

1. Estado PAR.
2. Valor, tipo y dominio PAR.
3. Preservación semántica RUL.
4. Binding de identidad y alcance.
5. Procedencia y suficiencia probatoria.

La asignación de primacía y la descomposición se rigen por la reconciliación SM/FP aceptada en DEC-C10-055 y los artefactos vigentes: cobertura de claves/componentes no sustituye equivalencia semántica; esquema/tipo y significado se mantienen diferenciados; FP-06 verifica aplicación y FP-07 observa el estado aplicado. No se suman varias familias como si fueran fallos confirmatorios independientes cuando representan una misma discrepancia subyacente.

## 4. Reglas sustantivas

- `PAR-SVC-ENABLED`: equivalencia lógica BOOL exacta.
- `PAR-SVC-PROFILE`: resolución semántica mediante biyección total, inyectiva y versionada sobre STANDARD/READ_ONLY/DISABLED.
- Estado VALUE debe observarse en origen y salida para estos parámetros. Falta de fila no demuestra ABSENT.
- `RUL-SVC-ENABLE-PROFILE-01` se comprueba como preservación FP-03; no demuestra aplicación runtime.
- El CMP owner se resuelve al NODE anchor exacto conforme a DEC-C10-082.
- La evidencia de una ruta no cubre la otra.

## 5. Adjudicación

- `PASS`: requisitos observados, cobertura suficiente, identidad y mapping exactos, evidencia pertinente e íntegra.
- `FAIL`: contradicción sustantiva demostrada con cobertura suficiente.
- `UNKNOWN`: observación, snapshot, cobertura, evidencia, mapping o resolución insuficientes.
- `NOT_COMPARABLE`: incompatibilidad de contratos/versiones/namespaces sin mapping aprobado.
- `NA`: inaplicabilidad ex ante justificada; no admisible para los dos PAR ni la regla en las dos rutas del contrato base.

El resultado por ruta es un vector de estados. Cualquier FAIL permanece visible; en ausencia de FAIL, UNKNOWN impide declarar PASS global. NOT_COMPARABLE se conserva explícitamente.

## 6. Límites y no autorizaciones

Esta decisión acepta criterios documentales, no observaciones ni mappings físicos. No define codificaciones, tolerancias u oráculo técnico; no completa IAM ni sella el manifiesto; no autoriza fixtures, parser, validator, implementación, Design Freeze ni ejecución científica. No modifica U_G, RMA, Evidence→Claim Matrix, STATUS ni main.

`scientific_execution=false`; `execution_authorized=false`.
