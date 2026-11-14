# DEC-C10-081 — Aceptación del protocolo de control independiente del binding probatorio PAR

**Fecha:** 2026-11-08  
**Estado:** ACEPTADA  
**Rama:** `research/c10-s-consolidation-draft`  
**Ámbito:** C10-S — gobernanza documental del binding probatorio PAR.

## 1. Decisión

Se acepta expresamente el protocolo documental descrito en el §20.18 de `C10_S_UG_EVIDENCE_PROVENANCE_AND_ADJUDICATION_PROTOCOL_DRAFT_001.md` como contrato lógico de control independiente del binding probatorio PAR vinculado a DEC-C10-080.

La aceptación comprende:
- no duplicar C0: reutilizar el control de §19;
- mantener cinco capas separadas: `C0_SCOPE`, `PAR_ROW_BINDING`, `EVIDENCE_LINK_INTEGRITY`, `EVIDENCE_RELEVANCE` y `COVERAGE_COMPLETENESS`;
- adoptar las entradas mínimas y la secuencia P0–P11;
- aplicar identidad lógica, revisión y supersession conforme a DEC-C10-079;
- preservar los resultados por capa `PASS`, `FAIL`, `UNKNOWN`, `NOT_COMPARABLE` y `NA`, con la precedencia especificada;
- mantener separados integridad del vínculo, pertinencia sustantiva de la evidencia y completitud de cobertura;
- conservar los 18 casos adversariales documentales y los requisitos de informe como especificaciones futuras.

## 2. Límites explícitos

La aceptación es exclusivamente del contrato lógico documental. No:
- amplía U_G ni añade columnas, FK, target_type, tablas, puentes o entidades PAR;
- cierra gramática, escaping, canonicalización o vocabulario de predicate del localizador;
- cierra mappings físicos/semánticos IAM↔U_G de `stage_key`, clase o ruta;
- crea registros, scopes, manifiestos, fixtures o evidencia observada;
- autoriza parser, validator, scripts, SQL, implementación, Design Freeze, validación técnica ni ejecución del control;
- autoriza simulación o experimento científico, ni modifica TGCV Core, RMA, Evidence→Claim Matrix, STATUS o claims.

Los mappings no inequívocos siguen produciendo `UNKNOWN`; no se permite inferencia heurística ni PASS por defecto.

## 3. Consecuencia y estado

El §20.18 pasa de propuesta pendiente a contrato documental aceptado. Su implementación y ejecución permanecen separadas y requieren gates y autorización específicos.

`scientific_execution=false`  
`execution_authorized=false`

**Aprobación:** aceptación explícita del responsable científico en la conversación del 2026-11-08.
