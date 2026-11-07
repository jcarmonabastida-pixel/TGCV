# DEC-C10-072 — Aceptación del token reservado de scope global C10-S

- **Estado:** ACEPTADA
- **Fecha:** 2026-11-07
- **Ámbito:** C10-S, binding C0 de scopes de cobertura
- **Autoridad:** aceptación explícita del usuario en esta conversación

## Decisión

Se acepta G1 y el literal reservado exacto `C10S_SCOPE_GLOBAL` para ocupar el slot `route_id` de la tupla C0 cuando el scope no está restringido a una ruta concreta.

## Semántica normativa

1. El token significa exclusivamente **“sin restricción a una ruta concreta”**.
2. No significa que no existan rutas, que el objeto no pertenezca a ninguna ruta, ni que la clase sea `NA`.
3. El literal queda reservado en el namespace C10-S y no puede asignarse como `route_id` semántico real. Una colisión observada es un conflicto de identidad y produce FAIL en C0.
4. No se usa `NULL`, cadena vacía, `NONE`, `F` ni `A` como sustituto del token global.
5. El scope global enumera los objetos elegibles de la clase/etapa/snapshot y cuenta cada identidad una sola vez, aunque pertenezca a varias rutas. Los scopes route-specific conservan denominadores separados.
6. La pertenencia route-specific sigue requiriendo route_id real, route_record_id y snapshot exactos, con evidencia conforme al protocolo C10-S. El token global no prueba ni niega pertenencia individual a rutas.

## Límites

Esta decisión acepta el literal y su semántica, pero **no** aprueba la gramática completa ni el esquema serializado de `universe_definition/version`, mappings físicos CMP/PAR/REF/RUL/MET, fixtures, parser, validador o control C0 implementado. Tampoco modifica el schema U_G, crea snapshots/scopes ni constituye Design Freeze.

C1/C2 y la alternativa G2 no quedan aceptadas. No hay autorización de implementación, simulación ni ejecución científica. `scientific_execution=false`; `execution_authorized=false`.

## Propagación requerida

Actualizar protocolo de evidencia §20.8, matriz de mapping §20.10, plantilla U_G §18.13, maestro §188, plan §16.43, matriz de control §61 y Decision Log §67. Marcar G1/token como ACCEPTED; conservar la gramática y el control independiente C0 como OPEN/CONDITIONAL.
