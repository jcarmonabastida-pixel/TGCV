# DEC-C10-073 — Aceptación de la arquitectura envelope de universe_definition

- **Estado:** ACEPTADA
- **Fecha:** 2026-11-07
- **Ámbito:** C10-S / COVERAGE_REGISTER / universe_definition
- **Autoridad:** aceptación explícita del usuario

## Decisión

Se acepta U1: un envelope JSON autocontenido y versionado como arquitectura documental de `universe_definition`, con los campos, cardinalidades y separación conceptual definidos en UDG-01 (§20.10 del protocolo de evidencia).

## Estructura aceptada

El envelope comprende:

- `schema_id` (1), literal propuesto `TGCV-C10S-UNIVERSE`;
- `schema_version` (1), independiente de contrato/instancia;
- `universe_id` (1) y `universe_revision` (1, entero positivo);
- `scope` (1), réplica exacta de la tupla C0 de nueve componentes;
- `membership_mode` (1): `EXPLICIT` o `RULE_DEFINED`;
- `member_refs` (0..N), requeridas para EXPLICIT;
- `inclusion_rule_ref` (0..1), requerida para RULE_DEFINED;
- `exclusion_rule_refs` (0..N);
- `source_manifest_refs` (1..N);
- `declared_member_count` (1, entero no negativo);
- `provenance_ref` (1).

La tupla scope conserva los nueve componentes C0; `dimension` permanece como atributo independiente de COVERAGE_REGISTER. El scope interno debe coincidir exactamente con la tupla C0 externa.

## Invariantes aceptados

1. EXPLICIT representa el denominador mediante referencias tipadas y resolubles; duplicados exactos son FAIL.
2. RULE_DEFINED requiere regla, versión y dependencias identificadas; no se declara exhaustiva sin resultado reproducible.
3. La cardinalidad declarada coincide con el conjunto deduplicado; no se corrige automáticamente.
4. Un universo vacío exige evidencia exhaustiva; una lista vacía aislada no basta.
5. Identidad no se infiere solo por nombre, valor, hash o posición.
6. Referencia requerida no resoluble/información insuficiente = UNKNOWN; contradicción demostrada = FAIL; PASS exige invariantes aplicables y exhaustividad.
7. Route-specific resuelve route_id a route_record_id exacto; scope global usa el token aceptado DEC-C10-072.

## Límites explícitos de la aceptación

Esta decisión acepta la arquitectura y el contrato documental de campos/cardinalidades de U1. **No acepta ni congela**:

- la política concreta de canonicalización (UTF-8/NFC, orden de claves/arrays);
- el algoritmo/hash SHA-256 como requisito normativo;
- la autoridad normativa de RFC/JCS u otra especificación externa;
- detalles finales de serialización física, gramática ejecutable o compatibilidad de schema;
- mapping físico CMP/PAR/REF/RUL/MET ni el control independiente C0 implementado/auditado.

La propuesta de semver para `schema_version` y revisión monotónica/inmutable de `universe_revision` se acepta como separación conceptual de versionado, no como especificación final de reglas de incremento/compatibilidad.

No se autoriza crear parser, validator, fixtures, snapshots/scopes, modificar schema, realizar Design Freeze, implementar ni ejecutar científicamente. `scientific_execution=false`; `execution_authorized=false`.

## Propagación

Actualizar protocolo §20.11, plantilla U_G §18.16, matriz mapping §20.13, maestro §190, plan §16.45, matriz de control §63 y Decision Log §69. UDG-01 pasa a ACCEPTED para arquitectura y estructura; canonicalización/hash y ejecución permanecen OPEN.
