# DEC-C10-076 — Aceptación del contrato de referencias tipadas e identidad de registro

- **Estado:** ACEPTADA
- **Fecha:** 2026-11-07
- **Ámbito:** C10-S / UDG-04 / identidad y resolución de referencias
- **Autoridad:** aceptación explícita del usuario

## Decisión

Se acepta UDG-04 como contrato documental para distinguir identidad lógica e identidad exacta de registro, tipar referencias por rol y target, resolverlas contra un registry/manifiesto versionado con scope explícito, y clasificar los resultados de resolución sin confundir inexistencia, inaccesibilidad e incompatibilidad.

## Identidades aceptadas

- Identidad lógica: `(object_class, object_id)`.
- Identidad de registro: `(object_class, object_id, object_record_id)`, inmutable y referida a una materialización/versionado exacto.
- Una misma identidad lógica con distinto `object_record_id` no equivale automáticamente al mismo miembro. La continuidad semántica entre registros requiere mapping de versión explícito y aprobado.

## Referencia tipada aceptada

`(ref_role, target_object_class, target_object_id, target_object_record_id)`.

El rol describe la relación desde el origen, sin cambiar la identidad del target. Los roles MEMBER/OWNER/SOURCE/INCLUSION_RULE/EXCLUSION_RULE/DEPENDENCY/PROVENANCE son ilustrativos y deben reconciliarse con el catálogo REF; esta decisión no los convierte en enum físico cerrado. Cada campo declara REQUIRED/OPTIONAL y cardinalidad conforme al contrato de su clase.

## Resolución aceptada

Resolución exacta contra registry/manifiesto versionado y scope explícito; no se permite latest implícito ni fallback por nombre visible, valor, posición o hash aislado. Comprobar forma, record_id exacto, clase e identidad lógica, integridad/inmutabilidad, compatibilidad de versiones/schema/contract, acceso a fuente y cardinalidad.

## Estados aceptados

- Referencia requerida ausente, dangling tras búsqueda exhaustiva en registry cerrado, conflicto de clase/identidad o record_id mutable: FAIL.
- Registry inaccesible/incompleto o cobertura no exhaustiva: UNKNOWN; no inferir inexistencia.
- Versión/schema/contract incompatible sin mapping aprobado: NOT_COMPARABLE.
- Referencia opcional ausente: NOT_APPLICABLE para esa relación.
- Más de un candidato sin record_id exacto: UNKNOWN; NOT_COMPARABLE si se comparan objetos no fijados.

## Ciclos, cardinalidad y propagación

Ciclos y cardinalidad se evalúan por tipo de relación y contrato de clase; no se presupone DAG universal. DEPENDENCY solo exige DAG cuando el contrato lo declara; ciclos admitidos requieren semántica explícita. No eliminar aristas ni escoger nodos arbitrariamente. UNKNOWN en dependencia requerida propaga UNKNOWN a conclusiones dependientes; FAIL invalida la relación afectada y conclusiones que dependan de ella; NOT_COMPARABLE no se convierte en DIFFERENT. No propagar fallos a objetos sin dependencia demostrada.

Resolver una referencia no demuestra pertenencia al universo, aplicabilidad, preservación semántica ni ejecución.

## Límites

Aceptación documental. No cierra el catálogo REF ni fija schema físico, API, registry concreto, algoritmo/resolver, parser, validator, comparator, fixtures o implementación. No cierra el mapping CMP/PAR/RUL entre F1/A1 y F2/A2. No autoriza Design Freeze ni ejecución científica.

`scientific_execution=false`; `execution_authorized=false`.

## Propagación

Protocolo de evidencia §20.17; plantilla U_G §18.22; matriz de mapping §20.19; maestro C10-S §196; plan de cierre §16.51; matriz de control §69; Decision Log §75.
