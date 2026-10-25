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
| D1 | Duplicado exacto: misma transición y misma transformación repetidas | **PASS** dentro del fixture combinado | Probar aislado y combinado por pares |
| D2 | Una transición declara más de una transformación distinta | **PASS** dentro del fixture combinado | Probar aislado y combinado por pares |
| D3 | Varias transiciones declaran la misma transformación | **PASS** dentro del fixture combinado | Probar aislado y combinado por pares |

## Combinaciones no triviales que deben probarse de forma aislada

Las tres clases aparecen simultáneamente en el fixture existente. Eso demuestra detección conjunta, pero no demuestra por sí solo el comportamiento de cada subconjunto sin la tercera clase.

| ID | Combinación | Resultado esperado | Estado |
|---|---|---|---|
| C12 | D1 + D2 | Informar duplicado exacto y transición con varios destinos; no mutar el mapping | PENDIENTE |
| C13 | D1 + D3 | Informar duplicado exacto y destino compartido; no mutar el mapping | PENDIENTE |
| C23 | D2 + D3 | Informar ambos conflictos estructurales; no mutar el mapping | PENDIENTE |

El fixture conjunto actual sirve como evidencia de D1 + D2 + D3; se conserva como control de combinación triple. No se cuenta como sustituto de C12, C13 ni C23.

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
| Órdenes ejercitados hasta ahora (original y reverso) | 2, con aserciones parciales |
| Órdenes no ejercitados como permutación | 58 |
| Permutaciones con oráculo semántico normalizado acreditado | 0 de 60, según la evidencia localizada |

El test de inversión existente comprueba el número de conflictos y la no mutación, pero no compara una firma semántica normalizada completa. Por eso no se considera que haya cerrado ninguna de las 60 permutaciones bajo el criterio más estricto.

## Ejecución agrupada

No se requieren 63 ejecuciones de CI ni 63 tests independientes. El bloque se implementa como **una única suite agrupada** dentro del test integrado de navegador: primero ejecuta C12/C13/C23, después genera las 60 permutaciones únicas del fixture de cinco filas (incluidas la original y la inversa) y aplica las mismas aserciones a cada caso. La firma normalizada se compara por código y conjuntos de identificadores, no solo por el contador mostrado en UI.

La suite agrupada se ejecuta en los dos workflows obligatorios: **2 ejecuciones de CI** en total (una de Motor sintético y una de Navegador y concordancia). Si una ejecución falla y hay que corregir el código, se repetirán los workflows afectados; ese retrabajo no puede contabilizarse por adelantado.

## Conteo operativo

- **1 bloque automatizado agrupado** que contiene C12/C13/C23 y las 60 permutaciones.
- **2 ejecuciones de CI** previstas para validarlo (un workflow por motor).
- Las 60 permutaciones son iteraciones internas del mismo test, no ejecuciones independientes de CI.
- No incluye otras clases globales de conflicto, variantes de catálogo, ciclos de vida, persistencia nativa ni pruebas de validez científica.

## Criterio de cierre

El bloque solo pasa cuando la suite agrupada completa pasa en ambos workflows, con firma semántica normalizada, cero mutaciones no autorizadas y evidencia ligada al commit exacto. Hasta entonces, el gate contractual global permanece **PENDIENTE**.
