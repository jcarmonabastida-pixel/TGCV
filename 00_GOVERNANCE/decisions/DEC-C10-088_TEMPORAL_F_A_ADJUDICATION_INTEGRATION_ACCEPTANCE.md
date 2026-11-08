# DEC-C10-088 — Aceptación de integración temporal de adjudicaciones F/A

**Fecha:** 2026-11-08  
**Estado:** ACCEPTED — DOCUMENTAL  
**Ámbito:** C10-S, rama `research/c10-s-consolidation-draft`

## 1. Decisión

Se acepta la integración documental descrita en:
- `C10_S_PATH_PREDICATE_TEMPORAL_EVIDENCE_MATRIX_DRAFT_001.md` §14;
- `C10_S_ABSTRACT_PARAMETER_AND_SOURCE_DESTINATION_MAPPING_MATRIX_DRAFT_001.md` §15.9;
- `C10_S_IAM_FIELD_TO_COLUMN_CROSSWALK_PROPOSAL_DRAFT_001.md` §10.19.

La integración reutiliza las decisiones DEC-C10-071 y DEC-C10-083…087, las etapas y predicados vigentes, y las clases I/S/T/R/D/E. No crea un sistema de predicados paralelo.

## 2. Cadena integrada por ruta

Para cada ruta F y A, sin compensación entre ellas:

1. `C_SRC→F1_S2` / `C_SRC→A1_S1`: adjudicación de PAR, tipo/dominio/valor, RUL, identidad, binding y evidencia conforme a DEC-C10-085.
2. `F1_S2→F2_DST_DECL` / `A1_S1→A2_DST_DECL`: conformidad semántica `P-DECL` y lineage `P-TRANS` conforme a DEC-C10-086.
3. `F2_DST_DECL→F2_DST_APPLIED` / `A2_DST_DECL→A2_DST_APPLIED`: FP-06 aplicación efectiva, FP-07 post-check mediante FP-01…05 aplicables y FP-08 procedencia/identidad conforme a DEC-C10-087.

## 3. Ejes y trazabilidad

`stage_key`, reloj DGP `t0…t9`, `SNAPSHOT.phase` y paso hipotético `k=1…H` son ejes distintos. Cada registro debe enlazarlos explícitamente con snapshot/registro, ruta, unidad, mapping/versiones e instantes de generación/observación. No se infiere correspondencia por orden, nombre o timestamp.

La evidencia no se transfiere automáticamente entre etapas, rutas ni afirmaciones. Su reutilización exige que su contenido y alcance respalden cada afirmación por separado. Se conserva predicado primario y se evita doble contabilización del mismo defecto.

## 4. Estados y agregación

Se conservan `PASS`, `FAIL`, `UNKNOWN`, `NOT_COMPARABLE` y `NA` conforme a las decisiones previas. FAIL exige contradicción demostrada con cobertura suficiente; la falta de registro no demuestra ausencia ni no aplicación y conduce a UNKNOWN salvo evidencia autoritativa/exhaustiva o contradicción positiva. Un FAIL obligatorio permanece visible; sin FAIL, UNKNOWN impide PASS global. No se construye score compensatorio ni se mezclan resultados F/A.

COV/E_T conserva carácter epistémico: no modifica por sí mismo verdad DGP, accesibilidad o Reach. Conformidad de configuración/aplicación no acredita automáticamente ACC, APP, REL, DEP, Reach ni causalidad `ΔT_acc→Value`. FP-04 y FP-05 siguen diferenciadas; FP-06 no implica FP-07.

## 5. Límites y no autorizaciones

Esta aceptación consolida un crosswalk documental; no adjudica observaciones ni declara la cadena ejecutada o validada. Permanecen abiertos mappings físicos CMP/PAR/REF/RUL/MET↔U_G, route_id/ROUTE_STEP exhaustivos, universe_definition/version y C0, gramática del localizador PAR, mapping M, IAM completo, oráculo/protocolo de observación, cobertura y evidencia material.

No sella IAM, no declara Design Freeze y no autoriza fixtures, parser, validator, implementación, validación técnica ni ejecución del control o experimento científico.

`scientific_execution=false`; `execution_authorized=false`.
