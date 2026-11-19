# DEC-C10-082 — Aceptación del anclaje CMP↔NODE 1:1 por snapshot

**Fecha:** 2026-11-08  
**Estado:** ACEPTADA  
**Rama:** `research/c10-s-consolidation-draft`  
**Ámbito:** C10-S — correspondencia de identidad entre CMP contractual y NODE U_G.

## 1. Decisión

Se acepta la cardinalidad de anclaje **1:1 por CMP y snapshot** y el contrato de adjudicación definido en el crosswalk `C10_S_IAM_FIELD_TO_COLUMN_CROSSWALK_PROPOSAL_DRAFT_001.md`, §10.7, con su propagación en la matriz IAM §19.27.

La unidad de correspondencia es el par (identidad CMP contractual exacta, SNAPSHOT exacto):
- identidad CMP: `contract_id/version`, `instance_id/version`, `component_id`, `component_class`;
- snapshot: `snapshot_id + snapshot_object_record_id`;
- NODE anchor: `node_id + object_record_id`, perteneciente al snapshot exacto;
- mapping: `mapping_id/version`, con universe/scope, provenance, evidencia y adjudicación.

Reglas aceptadas:
1. Cada CMP declarado aplicable tiene exactamente un NODE anchor en cada snapshot aplicable.
2. Un NODE anchor no representa simultáneamente dos CMP distintos.
3. NODE subordinados no son CMP adicionales salvo identidad funcional propia declarada ex ante.
4. Un CMP no se duplica por etapa o ruta; `stage_key` y `route_id/scope` califican cobertura, no identidad del NODE.
5. Continuidad entre snapshots se establece mediante `component_id` contractual y mappings versionados separados; no se exige igualdad de `node_id` ni `object_record_id` entre snapshots.
6. La correspondencia es solo anclaje de identidad; no demuestra equivalencia de configuración, preservación transformacional, verdad PAR, pertenencia a rutas ni completitud del universo.

## 2. Adjudicación y estados

- Un NODE exacto y mapping íntegro, con unicidad bidireccional demostrada: candidato a `PASS` de correspondencia.
- Ningún NODE tras enumeración exhaustiva, siendo CMP aplicable: `FAIL`.
- Cardinalidad múltiple CMP→NODE o NODE→CMP: `FAIL`.
- Universo/snapshot/mapping/evidencia incompletos o no accesibles: `UNKNOWN`.
- Incompatibilidad contractual/semántica sin mapping de comparabilidad aprobado: `NOT_COMPARABLE`.
- No aplicabilidad declarada ex ante, con disparador y justificación: `NA`; nunca inferida de ausencia observada.

## 3. Límites

La aceptación es del contrato lógico documental. No:
- sella IAM ni completa el roster CMP;
- resuelve mappings P1, mappings de instancias reales o mappings PAR;
- crea registros de mapping, snapshots, NODE, columnas, FK, tablas o entidades;
- modifica U_G ni los contratos físicos;
- autoriza poblar IAM, fixtures, parser, validator, scripts, SQL, implementación, Design Freeze o validación técnica;
- autoriza ejecución del control, simulación o experimento científico;
- modifica TGCV Core, RMA, Evidence→Claim Matrix, STATUS o claims.

La evidencia y enumeración deben ser exhaustivas antes de declarar PASS/FAIL; si no, UNKNOWN. `scientific_execution=false`; `execution_authorized=false`.

**Aprobación:** aceptación explícita del responsable científico en la conversación del 2026-11-08.
