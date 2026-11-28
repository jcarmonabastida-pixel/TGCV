# DEC-C10-089 — Identidad de unidad lógica raíz y relación con CMP

**Fecha:** 2026-11-08  
**Estado:** ACCEPTED — DOCUMENTAL  
**Ámbito:** C10-S, rama `research/c10-s-consolidation-draft`

## 1. Decisión

Se acepta que el NODE raíz `LOGICAL_SERVICE_UNIT` represente la identidad de la unidad lógica de servicio objeto del estudio, separada conceptualmente del host/entorno anfitrión y del estado basal S0.

La relación entre ese NODE raíz y el CMP contractual `CMP-SERVICE-LOGIC-001` queda **sin adjudicar**. No se presume que sean la misma entidad de dominio ni que sean entidades distintas. Cualquier correspondencia deberá declararse mediante mapping explícito, versionado y sustentado, compatible con DEC-C10-082.

## 2. Reglas

1. La unidad lógica de servicio es la raíz semántica estable; no absorbe host, runtime, infraestructura ni recursos.
2. Host/entorno/runtime se modelan como contexto P1 y NODE separados únicamente cuando satisfagan el criterio de granularidad y exista identidad/versión suficiente.
3. S0 es un estado temporal basal representado por SNAPSHOT, con pinning exacto de la revisión de la unidad raíz; no es un CMP ni un host.
4. La raíz NODE y el CMP pueden corresponder al mismo objeto de dominio o a objetos distintos. La decisión queda abierta hasta mapping explícito y evidencia; no se fuerzan uno o dos NODE.
5. DEC-C10-082 conserva su alcance: un NODE anchor por CMP aplicable y snapshot exacto, unicidad bidireccional. Esta decisión no redefine esa cardinalidad ni convierte automáticamente el NODE raíz en el anchor del CMP.
6. La clasificación boundary_class sigue DEC-C10-059. La raíz puede usar NA cuando actúe solo como contenedor de identidad; el entorno técnico aplicable se clasifica según evidencia, no por inferencia nominal.

## 3. Estado y límites

Queda aceptada la distinción conceptual de N01 y la regla de no inferencia de identidad CMP↔raíz. Permanecen OPEN: identidad concreta del NODE raíz, existencia y composición del host/entorno, mapping CMP↔raíz, snapshots y evidencia observacional.

No se asignan IDs ni se crean registros U_G/IAM. No se sella IAM, no se declara roster CMP exhaustivo ni cobertura. No autoriza acceso técnico, captura de snapshots, parser, validator, fixtures, implementación, Design Freeze ni ejecución científica.

`scientific_execution=false`; `execution_authorized=false`.
