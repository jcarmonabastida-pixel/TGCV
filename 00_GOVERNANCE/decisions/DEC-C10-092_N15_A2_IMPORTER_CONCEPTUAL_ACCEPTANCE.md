# DEC-C10-092 — Aceptación conceptual de N15: importador A2

**Estado:** ACCEPTED — DOCUMENTAL. **Fecha:** 2026-11-08.
**Ámbito:** C10-S; rama de investigación research/c10-s-consolidation-draft.

## Decisión
Se acepta la descomposición conceptual N15 propuesta en el crosswalk IAM↔U_G §10.29: capacidad/contrato A2, implementación concreta y ejecución temporal son planos distintos; recepción efectiva, parseo, validación estructural/semántica, resolución M, aplicación FP-06, verificación FP-07 y procedencia FP-08 son hitos distintos. N15 no se presume CMP autónomo; requiere identidad contractual, lifecycle y frontera autónomos para serlo.

Se reutilizan DEC-C10-071/086/087/088, los siete stage_key y FP-01…08. No se crean nuevos predicados confirmatorios. F/A se adjudican independientemente; la evidencia no se hereda entre etapas/rutas. La ausencia de registro no demuestra ausencia de evento.

## Alcance y límites
La aceptación cierra solo la descomposición conceptual. Permanecen abiertos protocolo/implementación A2, formato/parser, reglas de validación, mapping físico, destino, eventos reales, snapshots, cobertura y evidencia. No crea IDs, registros ni columnas; no adjudica CMP N15, no sella IAM y no autoriza captura, pruebas, parser, validator, implementación, Design Freeze o ejecución.

## Propagación
Crosswalk IAM↔U_G §10.30; Closure Control Matrix §98; Plan de cierre §16.80; Decision Log.

scientific_execution=false; execution_authorized=false.
