# DEC-C10-064 — Aprobación de resolución estructural de Opción A para U_G

**Fecha:** 2026-11-05  
**Estado:** ACCEPTED DOCUMENTALLY / DESIGN APPROVED / NOT TECHNICALLY VALIDATED  
**Ámbito:** C10-S, UG-SCH-10, pertenencia a snapshot y referencias versionadas.

## Decisión

El usuario aprueba la resolución de detalle de Opción A documentada en `C10_S_UG_OPTION_A_STRUCTURAL_RESOLUTION_DRAFT_001.md`.

Quedan aprobados como contrato de diseño:
1. `object_version` identifica la revisión observacional secuencial por identidad semántica. Cada nueva captura genera registro/version nuevo aunque no haya cambio material.
2. SNAPSHOT↔NODE raíz conserva integridad referencial bidireccional, pinning exacto y pertenencia al mismo snapshot; la inserción requiere transacción atómica y constraints diferibles hasta COMMIT.
3. EDGE referencia NODE origen/destino mediante record IDs exactos y FKs compuestas que comprueban semantic ID y snapshot.
4. PREDICATE referencia la revisión exacta de ROUTE mediante FK compuesta de mismo snapshot.
5. ROUTE_STEP es la relación normalizada de secuencia, con destino exactamente tipado NODE/EDGE, referencias de mismo snapshot, índices únicos/contiguos y verificación de continuidad.
6. Los diffs separan cambio de observación, cambio estructural, cambio de evidencia (ΔE_T) y cambio de accesibilidad (ΔT_acc*).

## Aplicación

La plantilla U_G incorpora el contrato normativo en §13. Se deben reconciliar encabezados físicos de §§2–6, matriz de claves, dominios, crosswalk IAM/FP y contratos de identidad/referencias antes del cierre documental final.

## Condiciones y límites

- El motor relacional no está fijado. La compatibilidad con FKs diferibles/equivalentes es gate obligatorio. Si no se demuestra, implementación BLOCKED y reapertura arquitectónica; no se debilita integridad.
- La continuidad cross-row de ROUTE_STEP, constraints compuestas, secuencias, supersession, inmutabilidad, parser y pruebas negativas requieren validación técnica posterior.
- La aprobación no equivale a schema freeze, validación física, inventario real, truth, experimento ni autorización científica.
- No cambia TGCV Core, RMA, Evidence→Claim Matrix, estimandos, Outcome ni Value.
- `scientific_execution=false`; `execution_authorized=false`.

## Artefactos

- `C10_S_UG_OPTION_A_STRUCTURAL_RESOLUTION_DRAFT_001.md`
- `C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md` §13
- Plan integral C10-S §LXVI
- Auditoría U_G §14.8
- Maestro C10-S §118
