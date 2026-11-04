# C10-S — Matriz operacional de predicados por paso, rama y tiempo

**ID:** C10-S-PRED-MATRIX-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** propuesta operacional documental; no aprobada ni ejecutable.  
**Dependencias:** inventario finito §74, reconciliación temporal §75, contrato DGP §§33–34, contrato Reach §73 y contrato de identidad/versionado.  
**Restricciones:** no implementa ni ejecuta fixtures; no genera datos; no autoriza simulación, experimento, preregistro o freeze.

## 1. Objetivo y dictamen

Se convierte el inventario abstracto S0/S1/S2/SF y F1/F2/A1/A2 en una matriz de evaluación por paso. La matriz distingue: (1) accesibilidad estructural de la transformación; (2) aplicabilidad desde el estado concreto de entrada; (3) composición e identidad/versionado; (4) factibilidad conjunta —autorización, recursos, dependencias, ventanas y bloqueos—; y (5) evidencia observada y cobertura, separadas de la verdad estructural del DGP.

Reach se evalúa en t4 sobre el snapshot postintervención sellado en t3. El inventario base no contiene reglas de transformación que modifiquen el catálogo de accesibilidad durante la ruta. Por ello, en el fixture base propuesto, T_acc y las condiciones estructurales del snapshot t3 se mantienen fijas a lo largo de las ramas hipotéticas. Los estados de entrada cambian según F1/F2/A1/A2, por lo que App debe evaluarse paso a paso. Recursos, ventanas o autorizaciones solo cambian dentro de una rama si el DGP incorpora explícitamente una regla de consumo, caducidad, renovación o modificación; no se presupone ninguna.

## 2. Convención temporal y de rama

- t0: baseline/elegibilidad antes de Z.
- t1: asignación/oferta/recepción B y W_attempt.
- t2: verificación técnica y condiciones.
- t3: snapshot postintervención S_T(i,t3) y clasificación observada.
- t4: cálculo de Reach_H sobre snapshot t3 y reglas de rama declaradas.
- t5–t9: conocimiento, selección, ejecución, Outcome y Value; no alimentan retroactivamente Reach_H.

Índice de paso k=1…H; s0=S0. Ramas candidatas:
- πF=(F1,F2): S0→S2→SF.
- πA=(A1,A2): S0→S1→SF.

H=3 continúa siendo profundidad máxima candidata; ambas rutas enumeradas tienen longitud 2. No se añade un tercer paso artificial.

## 3. Ficha de predicado por paso

Cada evaluación se almacena con clave mínima:
(unit_id, scenario_id, branch_id, step_k, TID_alias, SID, RID, input_state, snapshot_id, predicate_id, t_eval, branch_time, truth_dgp, observed_state, evidence_id, coverage_id, source_version, adjudicator, reason_unknown).

| Código | Predicado | Pregunta operacional | Nivel/tiempo de referencia | ¿Puede variar dentro de la rama? |
|---|---|---|---|---|
| ID | Identidad/continuidad | ¿Es la transformación semánticamente la misma y su versión compatible? | TID/SID/RID; fijado en t3 | No en fixture base; solo con evento/versionado explícito |
| ACC | Accesibilidad | ¿Está la transformación en T_acc de la unidad bajo snapshot t3? | unidad×transformación×t3 | No en fixture base; requiere regla explícita de cambio de T_acc |
| APP | Aplicabilidad | ¿Se satisfacen precondiciones desde el estado de entrada s(k−1)? | transformación×estado hipotético×paso | Sí, porque cambia el estado de entrada |
| REL | Composición | ¿Está permitida la relación entre paso anterior y actual? | arista ordenada×versión | No en fixture base; solo por rewire/regla explícita |
| COND | Condiciones constitutivas | ¿Se cumplen las condiciones necesarias de la transformación en su contexto? | unidad/sistema o paso según ficha | Solo si son state-dependent o temporales y existe regla |
| AUTH | Autorización | ¿La autorización cubre actor, objeto, unidad y ventana del paso? | basal o unidad×paso×ventana | No si autorización basal constante; sí con caducidad/revocación explícita |
| RES | Recursos | ¿Hay recursos reservables para completar el paso y la ruta sin doble asignación? | sistema/unidad/rama×ventana | Sí solo con regla de reserva/consumo/liberación; no inferir consumo real |
| DEP | Dependencia técnica | ¿Se satisfacen instalación, integridad, compatibilidad y operación de la dependencia requerida? | unidad×dependencia×snapshot t3 | No en fixture base; cambio solo por intervención/evento explícito |
| BLOCK | Bloqueo | ¿Existe bloqueo que impide el paso? | transformación×unidad×ventana | Puede variar si causa state-dependent/temporal; exige regla y evidencia |
| WIN | Ventana/duración | ¿El paso y la ruta caben en ventanas, precedencias y caducidades? | paso/ruta×θ | Sí por programación temporal; H no define duración |
| COV | Cobertura/evidencia | ¿El universo, fuente y observación son suficientes para clasificar el predicado? | predicado×ruta×unidad×tiempo | Puede mejorar como conocimiento; no cambia truth estructural |

COV no es una condición causal constitutiva: no entra en la conjunción truth de accesibilidad ni en la verdad de Reach. Sí determina si el observador puede clasificar 1/0/? y si puede afirmar exhaustividad.

## 4. Matriz por ruta y paso

| Rama/paso | Entrada→salida | ACC en t3 | APP | REL | COND/AUTH/RES/DEP/BLOCK/WIN |
|---|---|---|---|---|---|
| F1, k=1 | S0→S2 | ACC(F1,t3) | APP(F1,S0) | Inicio de ruta; no requiere arista previa | Evaluar para F1 y ventana de k=1 |
| F2, k=2 | S2→SF | ACC(F2,t3) | APP(F2,S2) | REL(F1,F2) | Evaluar para F2 y ruta acumulada |
| A1, k=1 | S0→S1 | ACC(A1,t3) | APP(A1,S0) | Inicio de ruta; no requiere arista previa | Evaluar para A1 y ventana de k=1 |
| A2, k=2 | S1→SF | ACC(A2,t3) | APP(A2,S1) | REL(A1,A2) | Evaluar para A2 y ruta acumulada |

La accesibilidad de F2/A2 no se infiere de la de F1/A1. La aplicabilidad se evalúa desde S2/S1, no desde S0. La admisibilidad de ruta es una conjunción de los predicados necesarios de ambos pasos, la relación y las restricciones conjuntas de ruta.

## 5. Invariancia y dinámica: regla de clasificación

Antes de construir un fixture, cada variable debe clasificarse en una clase:

- **I — Invariante de rama:** queda fijada en t3 y no puede cambiar durante el recorrido hipotético (p. ej., identidad/versiones, catálogo, T_acc en el fixture base).
- **S — Dependiente del estado:** se vuelve a evaluar desde s(k−1) (p. ej., APP y cualquier COND expresamente state-dependent).
- **T — Dependiente del tiempo/ventana:** se evalúa para el intervalo asignado al paso (p. ej., WIN y AUTH con caducidad).
- **R — Dependiente de recursos de ruta:** requiere una regla de reserva, concurrencia, consumo/liberación (p. ej., RES).
- **D — Dinámica explícita:** solo cambia por una regla de transición versionada del DGP; crea snapshot hipotético de rama inmutable.
- **E — Epistémica:** evidencia/cobertura/adjudicación; puede cambiar la clasificación observada, nunca por sí sola la verdad estructural.

Regla por defecto: si no existe regla DGP explícita, el predicado se mantiene fijo conforme al snapshot t3 o queda indeterminado; no se inventa una transición. Un predicado no puede clasificarse simultáneamente como invariante y dinámico para la misma versión de fixture.

## 6. Evaluación por escenario

| Escenario | Rama focal F1→F2 | Rama alternativa A1→A2 | Precaución |
|---|---|---|---|
| R0 / S4R-A | F1 puede abrirse tras B; F2 requiere evaluación propia | Ausencia de A1/A2 solo si cobertura funcional exhaustiva | No asumir Reach=0 basal sin descartar ambas rutas; no asumir F* por alias |
| R1 / S4R-B | Evaluación ordinaria de F1 y F2 | Ruta basal estable puede mantener Reach=1 | Apertura focal no implica cambio de Reach |
| R2 / S4R-C | Evaluar efecto de B sobre F1/F2 | Revaluar A1/A2 si B puede modificarlas | Vía colateral; efecto paquete salvo identificación adicional |
| R3 / S4R-D | El intento fallido puede dejar ACC(F1)=0 o ? según evidencia | Según escenario basal subyacente | Z/W_attempt no determinan ACC, DEP o Reach |

No se asignan valores 1/0 a predicados concretos por escenario en este documento: esos valores pertenecen a la especificación del DGP y deben justificarse por mecanismo y evidencia, no rellenarse para obtener un resultado deseado.

## 7. Lógica de composición y propagación

Para una ruta π, los predicados necesarios incluyen por paso ID, ACC, APP, COND, AUTH, RES, DEP, ausencia de BLOCK y WIN, además de REL entre pasos. En verdad DGP:
- ruta=1 si todos los predicados necesarios son 1;
- ruta=0 si al menos uno necesario es 0;
- ruta=? si no hay 0 y al menos uno es ?.

Entre rutas alternativas:
- Reach=1 si alguna ruta completa es 1;
- Reach=0 solo si todas las rutas del universo relevante son 0 y la cobertura es exhaustiva;
- Reach=? en los demás casos.

La evidencia/cobertura no se introduce como una conjunción causal. Para el observador, cada predicado se clasifica 1/0/? según evidencia, y Reach_obs aplica las mismas reglas más la condición de cobertura para declarar 0.

## 8. Reservas, recursos y no interferencia

En el fixture aislado se propone asignar pools no compartidos por unidad. Sin embargo, la factibilidad de una ruta no se puede derivar de “hay recursos” sin especificar: tipo/cantidad de recurso; demanda de cada transformación; simultaneidad o secuencialidad; regla de reserva y liberación; capacidad por ventana; posibilidad de compartir entre ramas contrafactuales.

Las ramas F y A son alternativas potenciales de la misma unidad, no dos ejecuciones concurrentes. No deben consumir simultáneamente un mismo recurso por el mero hecho de enumerarse. La evaluación pregunta si cada ruta, considerada por separado bajo la política de reserva declarada, es factible. Si el diseño introduce competición real entre unidades, se abandona la independencia simple y se modela clúster/interferencia antes de calcular estimandos.

## 9. Evidencia, cobertura y adjudicación

Para cada predicado y ruta registrar evidencia directa/indirecta y fuente; instante de generación y observación; versión del contrato y del sistema; universo/catálogo al que se refiere; cobertura y límites de búsqueda; observador/adjudicador, cegamiento respecto de Z/B/O/V; estado observado 1/0/? y motivo; desacuerdo, contradicción o no comparabilidad.

La ausencia de evidencia no equivale a evidencia de ausencia. Una mejora de cobertura entre t0 y t3 puede descubrir una ruta preexistente: se registra como cambio epistémico, no como ADD estructural. No se usa Outcome/Value para adjudicar F*, alternativa, App, Reach ni cobertura.

## 10. Contratos adversariales documentales

| ID | Caso | Resultado requerido |
|---|---|---|
| PM-01 | F1 ACC=1, F2 ACC=0 | Ruta focal=0 |
| PM-02 | F1 ACC=1, F2 APP(S2)=? | Ruta focal=? salvo otro predicado necesario 0 |
| PM-03 | F1/F2 accesibles y aplicables, REL(F1,F2)=0 | Ruta focal=0 |
| PM-04 | F2 accesible pero APP(F2,S2)=0 | Ruta focal=0 |
| PM-05 | Todos los predicados estructurales 1, cobertura epistémica incompleta | Truth ruta=1; Reach_obs puede ser ? |
| PM-06 | Ruta A confirmada, ruta F desconocida | Reach truth/obs=1 si A observada y validada |
| PM-07 | A1/A2 no halladas, cobertura incompleta | Ruta alternativa=?; no declarar Reach=0 |
| PM-08 | Mejora de cobertura descubre A1 preexistente | ΔE_T≠0; no ADD estructural |
| PM-09 | Recurso compartido entre unidades sin modelo | No asumir no interferencia |
| PM-10 | F y A son ramas contrafactuales alternativas | No sumar sus consumos como simultáneos |
| PM-11 | AUTH caduca entre pasos | Aplicar regla temporal explícita; sin ella, ? |
| PM-12 | COND depende de estado intermedio | Reevaluar desde el estado de entrada de cada paso |
| PM-13 | Cambio de T_acc dentro de la rama sin regla DGP | Rechazar actualización inventada; mantener snapshot o ? |
| PM-14 | B modifica A1/A2 en R2 | Registrar vía colateral y revisar estimando/exclusión |
| PM-15 | W_attempt=1, dependencia técnica fallida | No inferir ACC=1 |
| PM-16 | No existe regla de reserva/consumo | RES=?; no afirmar ruta factible |
| PM-17 | Outcome/Value conocido antes de adjudicación | Cegamiento/independencia comprometidos; no usar para Reach |
| PM-18 | Catálogo truncado por límite computacional | No declarar exhaustividad semántica |

Son contratos de diseño; no se han implementado ni ejecutado.

## 11. Decisiones y dependencias aún abiertas

No se fija todavía: valor verdadero u observado de cada predicado por escenario; definición operacional de F* y criterio GOAL_F; universo funcional de alternativas y cobertura; G y H confirmatorios; duración, ventanas y caducidad; regla de reservas, demanda y recursos por transformación; qué condiciones constitutivas son invariantes o state-dependent en el dominio sustantivo; si existe dinámica dentro de la trayectoria o si el fixture base es estático; elección D1/D2, q_X*, estimandos y unidad/interferencia; fuentes E1–E4, adjudicación y matriz de error.

No se cierran AUD-004/005/007/010/011 ni OPEN-C10-001/003/005/007. La matriz es una especificación candidata, no un DGP completo.

## 12. Dictamen

Se dispone ahora de una matriz operacional que identifica qué se evalúa por transformación, estado de entrada, paso, rama y tiempo. El default del fixture base es snapshot estructural fijo en t3, aplicabilidad por estado hipotético, factibilidad por ruta y ausencia de dinámica no declarada. Cualquier cambio intrarrama exige regla DGP explícita y snapshot inmutable.

**Siguiente bloqueo:** definir el catálogo de predicados constitutivos y su ficha sustantiva para F1/F2/A1/A2, incluyendo qué es realmente state-dependent, temporal, recurso-dependiente o invariante. Después podrá fijarse el vector de evidencia y el oráculo de clasificación sin inventar valores.

No se han generado datos, implementado fixtures, simulado ni ejecutado el experimento.
