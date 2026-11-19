# DEC-C10-063 — Aceptación de Opción A para UG-SCH-10
**Fecha:** 2026-11-05  
**Estado:** ACCEPTED — decisión expresa del usuario  
**Ámbito:** C10-S / U_G / pertenencia a snapshot y referencias versionadas.

## Decisión

Se acepta Opción A como arquitectura de referencia para resolver la pertenencia de registros observacionales a snapshots y las referencias versionadas exactas.

La solución adoptada mantiene:
1. NODE, EDGE, ROUTE y PREDICATE como registros observacionales asociados al snapshot correspondiente.
2. Referencias exactas y versionadas entre extremos EDGE, PREDICATE y ROUTE.
3. ROUTE_STEP como relación normalizada para la secuencia ordenada de una ruta.
4. La distinción entre identidad semántica y revisión del registro observacional.
5. La integridad referencial como requisito; no se acepta resolver referencias por timestamp, última versión, orden de inserción o inferencia.

## Alcance y límites

La aceptación selecciona la arquitectura A frente a las alternativas comparadas en UG-SCH-10. No equivale a schema freeze ni demuestra que el motor relacional soporte el diseño. La resolución estructural detallada, incluida la circularidad SNAPSHOT↔NODE raíz, se desarrolla en DEC-C10-064. El pinning exacto de la revisión SNAPSHOT se completa mediante DEC-C10-065.

No autoriza DDL, parser, validadores, fixtures, inventario real, simulación ni ejecución científica. No modifica TGCV Core, RMA, Evidence→Claim Matrix, claims, estimandos, Outcome o Value.

**Estado resultante:** Opción A ACCEPTED AS DESIGN ARCHITECTURE; UG-SCH-10 permanece OPEN hasta reconciliación integral y validación técnica. scientific_execution=false; execution_authorized=false.
