# Inventario finito de conflictos declarados y permutaciones — 001

## Propósito y límite

Este plan convierte en un conjunto finito y contable la cobertura de **mapping declarado ↔ mapping declarado** en el derivador de correspondencias. No declara cerrada la matriz global del derivador: las interacciones declarada↔derivada, derivada↔derivada, efectiva y persistencia pertenecen a otros bloques.

Fuente de verdad del fixture actual: `prototypes/collective_toy/web/cross_runtime_test.cjs`, bloque `Declared↔declared pairwise conflicts`.

## Fixture acotado

El fixture contiene cinco filas de mapping:

| Símbolo | `system_transition_id` | `tgcv_transformation_id` | Multiplicidad |
|---|---|---|---:|
| A1 | `t_declared_ab_1` | `T_SHARED_AB` | 2 filas idénticas |
| A2 | `t_declared_ab_2` | `T_SHARED_AB` | 1 |
| B1 | `t_declared_ac` | `T_AC_1` | 1 |
| B2 | `t_declared_ac` | `T_AC_2` | 1 |

Las cinco filas son A1, A1, A2, B1, B2. Por tanto, el número de órdenes distintos es:

`5! / 2! = 60`

La división por `2!` elimina el doble conteo causado por las dos filas A1 idénticas.

## Clases de conflicto

| Código | Regla | Evidencia actual | Pendiente |
|---|---|---|---|
| D1 | Duplicado exacto: misma transición y misma transformación repetidas | **PASS** dentro del fixture y las combinaciones agrupadas | No pendiente en este bloque |
| D2 | Una transición declara más de una transformación distinta | **PASS** dentro del fixture y las combinaciones agrupadas | No pendiente en este bloque |
| D3 | Varias transiciones declaran la misma transformación | **PASS** dentro del fixture y las combinaciones agrupadas | No pendiente en este bloque |

## Combinaciones no triviales

C12, C13 y C23 están cubiertas por la suite agrupada aprobada en ambos workflows. No se reabren ni se cuentan como ejecuciones pendientes.

| ID | Combinación | Estado verificado |
|---|---|---|
| C12 | D1 + D2 | **PASS** en la suite agrupada |
| C13 | D1 + D3 | **PASS** en la suite agrupada |
| C23 | D2 + D3 | **PASS** en la suite agrupada |

El fixture combinado D1 + D2 + D3 se conserva como control adicional. No genera ejecuciones independientes de CI.

## Permutaciones

Las 60 permutaciones únicas deben producir la misma **firma semántica normalizada** de conflictos para el mismo conjunto de filas. La firma no debe depender del orden de entrada. La lista original de declaraciones sí debe conservar exactamente el orden recibido; no se exige reordenar ni mutar el modelo.

Aserciones obligatorias por permutación:

1. Firma normalizada de conflictos igual a la referencia, comparando códigos y conjuntos de identificadores, no solo el número total.
2. Cero propuestas derivadas originadas para resolver mappings declarados.
3. Mapping declarado conservado exactamente, incluido el orden de entrada.
4. Sin materialización ni cambios en mappings efectivos.
5. Mensaje de UI coherente con la firma detectada.

| Estado de permutaciones | Cantidad |
|---|---:|
| Permutaciones únicas del fixture | 60 |
| Órdenes ejercitados por suite agrupada | 60 de 60 |
| Órdenes no ejercitados como permutación | 0 |
| Permutaciones con oráculo semántico normalizado acreditado | 60 de 60 — PASS en ambos workflows |

La suite agrupada del commit `2ae4829273f81ab27209a52640c4fd3a3489d271` ejecutó las 60 permutaciones con firma semántica normalizada, conservación exacta del orden y cero propuestas. Ambos workflows finalizaron PASS: [Motor sintético, run 40195539421](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40195539421) y [Navegador y concordancia, run 40195539418](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40195539418).

## Ejecución agrupada

No se requieren 63 ejecuciones de CI ni 63 tests independientes. El bloque de permutaciones ya está implementado y cerrado; no se vuelve a ejecutar para el cierre global. El pendiente global se concentra en una suite agrupada de integración cruzada dentro del test integrado existente. La firma normalizada se compara por código y conjuntos de identificadores, no solo por el contador mostrado en UI.

La suite agrupada se ejecuta en los dos workflows obligatorios: **2 ejecuciones de CI** en total (una de Motor sintético y una de Navegador y concordancia). Si una ejecución falla y hay que corregir el código, se repetirán los workflows afectados; ese retrabajo no puede contabilizarse por adelantado.

## Conteo operativo

- **1 bloque automatizado agrupado — PASS**: C12/C13/C23 y las 60 permutaciones.
- **2 ejecuciones de CI completadas — PASS** (un workflow por motor), sobre el commit `2ae4829273f81ab27209a52640c4fd3a3489d271`.
- Las 60 permutaciones son iteraciones internas del mismo test, no ejecuciones independientes de CI.
- No incluye otras clases globales de conflicto, variantes de catálogo, ciclos de vida, persistencia nativa ni pruebas de validez científica.

## Criterio de cierre

El bloque declarado↔declarado queda **PASS** para el fixture y el contrato comprobados. El gate contractual global permanece **PENDIENTE** por la integración cruzada entre clases de conflicto y las invariantes conjuntas de ciclo de vida.


## Minimización del cierre global pendiente

No se abrirán suites individuales por cada combinación ni se repetirán las 60 permutaciones. El pendiente global identificado en `CONDITION_INPUT_PATH_COVERAGE_MATRIX_001.md` se ejecutará como **un único bloque de integración cruzada**, reutilizando los fixtures y helpers existentes para cubrir, en una sola secuencia controlada, las interacciones entre clases declarada↔derivada, derivada↔derivada y efectiva, con las aserciones comunes de decisión explícita, mapping declarado/effective, `T_acc`, ejecución, alcanzabilidad, trayectorias y recarga.

**Presupuesto mínimo planificado: 2 ejecuciones de CI**, una de Motor sintético y una de Navegador y concordancia, sobre el mismo commit. Las variantes de fixture se ejecutan dentro de la suite agrupada; no se lanzan como workflows separados. Si el bloque falla, solo se repiten los workflows afectados por la corrección, no se programa por adelantado ninguna batería adicional.

La persistencia de borrador tras recarga ya tiene PASS sin reinyección manual; no se repite como test aislado. Los límites de perfil/origen o almacenamiento borrado quedan fuera salvo que el contrato del producto los exija explícitamente.


## Evidencia posterior: colisión declarada ↔ derivada agrupada

**PASS en ambos workflows** sobre `17ac9e28f182dee6707eeb6cb31cb1bfd23de858`:

- [Navegador y concordancia](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40198397842)
- [Motor sintético](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40198397820)

El test verifica que una candidata derivada no reclame una transformación ya asignada por el mapping declarado, que la exclusión quede explícita, que una propuesta no conflictiva pueda hacerse efectiva y que el mapping fuente declarado se restaure tras recarga nativa sin reinyección manual.

Este caso cierra únicamente esta colisión declarada↔derivada. No se ejecuta el grafo de fixture con transiciones duplicadas, por lo que no atribuye a este caso cobertura de ejecución/alcanzabilidad/trayectorias; esas propiedades se mantienen en el fixture de ciclo de vida integrado separado.

**Gate contractual global: PENDIENTE.** No se consideran cerradas todas las interacciones cruzadas ni se reabren las 60 permutaciones declarada↔declarada.


## Gate final consolidado (fuente de verdad operativa)

No se reabren las 60 permutaciones declarada↔declarada ni se crean tests/workflows individuales por estado. La única brecha global a consolidar es una secuencia de un mismo fixture que compara el baseline contra: propuestas pendientes, decisión rechazada, mapping aplicado y posteriormente obsoleto por cambio de ámbito, y recarga/reaplicación.

En cada fase deben compararse por separado: (1) mappings declarados y overlay efectivo con procedencia/decisiones; (2) `T_acc` operacional estructurado frente a las transformaciones de las trayectorias; (3) grafo TGCV; (4) resultado por escenario; (5) estados alcanzables; y (6) trayectorias normalizadas. La propuesta pendiente o rechazada no puede alterar resultados; el mapping `STALE` debe dejar de ser activo y no resucitar tras restaurar el ámbito; aplicar dos veces debe ser idempotente.

**Mínimo planificado: un bloque de test agrupado, dos ejecuciones CI** (Navegador y concordancia y Motor sintético) en el mismo commit. La suite de 60 permutaciones queda cerrada y fuera de este bloque. Este gate permanece **PENDIENTE** hasta que el test agrupado se implemente y ambos workflows pasen; no basta con sumar PASS de fixtures independientes.


## Resultado del bloque agrupado — 2026-10-25

El bloque implementado en `d12bb02f40ac0ec841ae33bfc0fa3c445ade8aa0` pasa en ambos workflows:

- [Navegador y concordancia — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40199349994)
- [Motor sintético — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40199350007)

Cubre snapshots baseline/propuestas pendientes, invalidación por cambio de catálogo, historial `STALE`, consistencia operacional posterior a la invalidación y no reactivación automática al restaurar el catálogo.

**Límite:** este PASS no demuestra por sí solo que una decisión rechazada se haya comparado explícitamente con el baseline ni que la reaplicación idempotente se haya verificado dentro del mismo bloque. La cobertura global queda pendiente hasta enlazar evidencia existente para ambas propiedades o incorporarlas al bloque agrupado. No se reabren las 60 permutaciones declarada↔declarada.


## Dos aserciones residuales añadidas al bloque agrupado

En `520b82d43506cf141c880787b6713d835b897913` se añaden al mismo fixture:

- **Rechazo frente al baseline:** rechazo explícito de `t_ab`, comparación exacta de snapshot operacional (mapping declarado/overlay efectivo, `T_acc`, grafo, alcanzabilidad y trayectorias) y persistencia de `REJECTED`.
- **Idempotencia:** aceptación explícita de `t_cd`, aplicación duplicada y comparación exacta de conjunto efectivo y almacenamiento persistido; el rechazo previo debe conservarse.

La implementación no abre workflows adicionales ni reejecuta las 60 permutaciones declarada↔declarada. **Pendiente de CI**: el gate solo se considera cerrado cuando ambos workflows pasan en este commit.


## Rechazo e idempotencia — PASS confirmado

Commit: `6b5ee82bb9935a051a312ea12b4bc3233c27e943`.

- [Navegador y concordancia — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40203256337)
- [Motor sintético — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40203256339)

La prueba agrupada compara el snapshot operacional antes/después de rechazar `t_ab`, comprueba que `REJECTED` se persiste, y verifica que la segunda aplicación de la correspondencia aceptada `t_cd` no cambia ni el conjunto efectivo ni el almacenamiento persistido. Ambos workflows pasan.

**Estado del bloque:** cerrado con evidencia de CI. No se reabren las 60 permutaciones declarada↔declarada. La PR #95 permanece en borrador y `main` intacta.


## Fuente de verdad reconciliada — 2026-10-25

Esta sección prevalece sobre los estados históricos de “pendiente de CI” anteriores; describen commits y fases anteriores.

**Último bloque ejecutado:** inversión del orden del catálogo en la colisión declarada↔derivada, commit `f12bf81214f90807cb8d6ce0a5f743a096ce424f`.

- [Navegador y concordancia — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40204075921)
- [Motor sintético — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40204075929)

La prueba confirma invariancia del mapping declarado, conjunto normalizado de candidatas/conflictos, exclusión explícita y ausencia de mappings efectivos antes de aceptación. Rechazo sin efecto operacional e idempotencia ya tienen PASS independiente en el commit `6b5ee82bb9935a051a312ea12b4bc3233c27e943`.

### Recuento reconciliado

Para **cerrar el gate de integración cruzada definido en este plan**, queda **1 bloque automatizado integrado**, ejecutado mediante **2 workflows CI** sobre el mismo commit: Navegador y concordancia + Motor sintético. No quedan 60 permutaciones por repetir; esas permutaciones declarada↔declarada no se reabren.

El bloque pendiente debe consolidar en **una sola secuencia** la evidencia hoy repartida en fixtures: baseline → propuesta pendiente → rechazo explícito → mapping aplicado → cambio de catálogo e invalidación `STALE` → restauración/recarga → reaplicación idempotente. En cada fase se comparan por separado mapping declarado/overlay efectivo y procedencia, `T_acc`, grafo TGCV, resultados por escenario, alcanzabilidad y trayectorias normalizadas. El PASS del test de orden de catálogo no sustituye esta secuencia integrada.

**Límite del número:** `1 bloque / 2 workflows` es el recuento exacto para este gate, no una cifra de todas las pruebas pendientes del contrato completo. El §10.6 del contrato mantiene aparte: (a) restauración tras reinicio de las decisiones de resolución de conflicto y (b) un flujo general de resolución para todos los tipos `CONFLICT_NEEDS_REVIEW`, ambos sin verificar; la derivación sigue siendo exact-boundary, sin reclamar inferencia semántica general. Además, los gates de entrada de condiciones (JSON/texto y la cobertura agrupada de las tres vías) tienen su propio estado parcial. No hay base en estos artefactos para convertir todos esos ámbitos distintos en un número global único de ejecuciones.

PR #95 permanece abierta y en borrador. `main` no se modifica; no hay autorización de promoción ni de ejecución científica.
