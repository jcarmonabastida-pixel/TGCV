# DEC-C10-075 — Aceptación del contrato de comparación semántica de universos

- **Estado:** ACEPTADA
- **Fecha:** 2026-11-07
- **Ámbito:** C10-S / UDG-03 / comparación de universos U1 versionados
- **Autoridad:** aceptación explícita del usuario

## Decisión

Se acepta UDG-03 como contrato documental de comparación semántica por dimensiones, con siete niveles y resultados controlados. No se colapsan en un único booleano.

## Siete niveles aceptados

1. Identidad del artefacto fuente (bytes originales).
2. Igualdad de representación canónica (mismo perfil y hash canónico recalculado).
3. Identidad del universo (universe_id), sin inferir igualdad de revisión/contenido.
4. Identidad de revisión (universe_id + universe_revision), verificando inmutabilidad y ausencia de conflicto.
5. Igualdad extensional de miembros: conjunto completo de identidades tipadas/versionadas en scope y snapshot comparables.
6. Equivalencia definicional: condiciones de inclusión/exclusión, reglas/AST, dominios, dependencias y semántica de pertenencia equivalentes.
7. Compatibilidad dirigida entre revisiones (p. ej. SAME_MEMBERS, STRICT_SUPERSET, STRICT_SUBSET, REDEFINED, INCOMPARABLE), demostrada y no inferida del número de revisión o cardinalidad.

## Proyecciones y precondiciones

La comparación mantiene Projection-ID (identidad/revisión/schema/contract/instance/C0/stage_key/route/route_record/snapshot/perfil) y Projection-SEM (membership mode, refs tipadas/versionadas, inclusión/exclusión, reglas/AST/dependencias, fuentes/cobertura y cardinalidad). Provenance, timestamp y hashes son trazabilidad/integridad, no miembros; C0, stage, ruta, snapshot, contrato/instancia y versión de objeto condicionan la comparabilidad.

Igualdad extensional exige ambos universos completos/exhaustivos, referencias resueltas y scope/snapshot compatibles. Equivalencia definicional exige además evidencia de equivalencia de las reglas, dominios y dependencias. Un resultado EXPLICIT y otro RULE_DEFINED con los mismos miembros en un snapshot no acredita equivalencia definicional. Diferentes scopes/snapshots/contratos sin mapping explícito = NOT_COMPARABLE. Evidencia faltante = UNKNOWN. Contradicción de integridad = FAIL.

## Resultados controlados

- `EQUAL`: igualdad demostrada en la dimensión indicada.
- `DIFFERENT`: diferencia demostrada con evidencia completa y comparabilidad.
- `UNKNOWN`: evidencia insuficiente o referencias no resueltas.
- `NOT_COMPARABLE`: objetos válidos, pero scopes/contratos/snapshots/perfiles no armonizables con mapping explícito.
- `FAIL`: incumplimiento de integridad/contrato; no es clase de igualdad.

Cada resultado debe identificar dimensión, reason_code, evidencia, versiones/perfiles y scope comparado. No elevar UNKNOWN/NOT_COMPARABLE a PASS ni declarar equivalencia global si una dimensión crítica está abierta.

## Alcance y límites

Esta decisión acepta el contrato documental, no un algoritmo automático completo. No crea fingerprint semántico, comparator ejecutable, regla de migración, fixtures, parser/validator ni schema change. No autoriza Design Freeze, implementación o ejecución científica. La comparación efectiva de equivalencia definicional requiere evidencia y adjudicación; no se deriva del hash, nombre, ID o cardinalidad.

`scientific_execution=false`; `execution_authorized=false`.

## Propagación

Protocolo de evidencia §20.15; plantilla U_G §18.20; matriz de mapping §20.17; maestro C10-S §194; plan de cierre §16.49; matriz de control §67; Decision Log §73.
