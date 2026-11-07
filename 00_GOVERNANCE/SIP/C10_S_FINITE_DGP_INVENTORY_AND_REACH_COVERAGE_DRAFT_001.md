# C10-S — Inventario finito candidato del DGP y mapa de cobertura Reach

**ID:** C10-S-DGP-INV-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-04  
**Estado:** PROPUESTA DE ESPECIFICACIÓN / NO APROBADA / NO CONGELADA.  
**Ámbito:** Bloque 3 — conversión de los contratos de identidad, snapshots y Reach en un universo sintético finito auditable.  
**Restricciones:** No autoriza implementación, generación de datos, simulación, ejecución, preregistro ni freeze.

## 1. Propósito y reconstrucción histórica

Este documento convierte las reglas existentes de accesibilidad, identidad, snapshots y Reach en un inventario finito candidato. La reconstrucción del DGP y del PR #116 encontró que:

- El contrato DGP temporal fija el reloj t0–t9 y separa accesibilidad, Reach, selección, ejecución, Outcome y Value.
- El DGP contiene políticas candidatas B_g0/B_g1 y escenarios D1/D2; actor, versiones, recepción, reintentos y rollback siguen abiertos.
- El historial menciona G0/G1, H=3 y evaluación de ramas dinámicas, pero no constituye por sí solo un catálogo canónico completo ni resuelve la precedencia D1/D2.
- El contrato Reach exige G/H, estados, objetivos, catálogo, relaciones, recursos, ciclos y cobertura exhaustiva antes de afirmar Reach=0.

Por tanto, lo que sigue es un fixture conceptual finito candidato, no la recuperación de una especificación aprobada. No sustituye los contratos previos ni elige estimando o comparador primario.

## 2. Frontera y granularidad candidatas

**Unidad:** una instancia sintética aislada (UE=UA candidata), con una asignación y una versión de política durante el horizonte. La ausencia de interferencia solo se sostiene si cada instancia tiene estado, agentes, recursos, información, infraestructura y canales independientes.

**Frontera:** estado de la instancia; catálogo de transformaciones; relaciones de composición; precondiciones; autorizaciones basales; dependencias técnicas; recursos reservados; bloqueos; reloj y snapshots. Los servicios externos se incluyen si pueden bloquear o habilitar una transformación; en otro caso se declaran constantes externas y no diferenciales por brazo.

**Granularidad G:** transformación atómica como unidad de catálogo; las rutas son secuencias ordenadas de transformaciones atómicas. Un compuesto solo se introduce como TID independiente si es irreducible en G y se preserva mapping a sus componentes. No se cuentan estados ni eventos como transformaciones.

**Horizonte H candidato:** tres pasos transformacionales (H=3), cada paso ocupa una unidad discreta de tiempo; evaluación antes y después de cada paso. Esta propuesta recupera el H=3 citado en el historial, pero requiere ratificación frente a duración real, ventanas y sensibilidad a H. H=3 define el horizonte científico, no un límite computacional accidental.

**Ciclos:** prohibidos en el fixture base. Una repetición/ciclo solo se admite en escenario adversarial separado, con regla de visita, coste temporal y terminación explícitos.

## 3. Estados y objetivos candidatos

Se usa un alfabeto abstracto; no son estados de un dominio real.

| ID | Descripción estructural | Papel |
|---|---|---|
| S0 | Instancia en configuración basal elegible; τ2 focal no accesible en baseline | Estado inicial |
| S1 | Estado intermedio alcanzado por ruta funcional alternativa | Intermedio alternativo |
| S2 | Estado intermedio alcanzado mediante τ2 focal | Intermedio focal |
| SF | Estado objetivo sintético que satisface el predicado funcional F* | Objetivo |

El predicado GOAL_F(SF)=1 por definición del fixture. No se define usando Outcome ni Value. La definición operacional de F*, tolerancias y criterios de aceptación continúa abierta; SF es un marcador formal, no un constructo funcional validado.

El objetivo de Reach se calcula desde S0 hacia SF dentro de H y bajo el snapshot/régimen declarado.

## 4. Catálogo finito candidato

Los identificadores siguientes son aliases locales del fixture, no TID canónicas aprobadas.

| Alias | TID candidata | Transición | Papel | Condición principal |
|---|---|---|---|---|
| F1 | TID-F1 | S0 → S2 | Paso focal τ2 | A_f*(τ2)=1 y App*(τ2,S0)=1 |
| F2 | TID-F2 | S2 → SF | Continuación posterior | F2 accesible y aplicable desde S2 |
| A1 | TID-A1 | S0 → S1 | Primera transformación alternativa | Ruta alternativa disponible |
| A2 | TID-A2 | S1 → SF | Cierre de ruta alternativa | A2 accesible y aplicable desde S1 |

**Relaciones permitidas:** F1→F2 y A1→A2. No se permiten otras aristas en el fixture base. No hay auto-bucles ni composición cruzada F1→A2 o A1→F2.

Este catálogo de cuatro transformaciones es el mínimo fixture propuesto para distinguir apertura focal, alcanzabilidad y sustituibilidad. La sensibilidad deberá añadir transformaciones no focales que no conducen a SF, cambios relacionales sin alta de TID, versiones y mappings split/merge; no amplían el camino al objetivo salvo declaración expresa.

## 5. Escenarios de rutas y relación con las poblaciones

| Escenario | F1→F2 | A1→A2 | Papel analítico |
|---|---|---|---|
| R0 — focal exclusiva | Cerrada en baseline; puede abrirse post-B | Ausente respaldada | Candidato a P*_F, si F* y cobertura se validan |
| R1 — alternativa basal | Cerrada en baseline; puede abrirse post-B | Disponible basal y no afectada por B | P*_τ2 con alternativa; apertura focal no equivale a apertura funcional |
| R2 — alternativa afectada | Cerrada en baseline; puede abrirse post-B | B puede modificar/activar/bloquear A1/A2 | Vía colateral; alerta de exclusión/efecto paquete |
| R3 — provisión fallida | Intento B sin apertura de F1 | Según R0/R1 | Noncompliance/fallo; no imputar accesibilidad por asignación |

R0–R3 son escenarios sintéticos separados. No se mezclan sus ITT ni se presupone que sus poblaciones de cumplidores coincidan. R1 y R2 no pertenecen automáticamente a P*_F. R2 no se interpreta como instrumento focal exclusivo si B afecta la ruta alternativa.

## 6. Matriz ruta × predicados × tiempo × evidencia × cobertura

Leyenda: **1** = estipulado verdadero en truth del fixture; **0** = estipulado falso; **?** = desconocido/no cubierto; **NA** = no aplica. La tabla define requisitos del evaluador, no observaciones empíricas.

| Ruta | t0 baseline | Post provisión/verificación | Predicados constitutivos | App / composición | Recursos/autorización/bloqueos | Evidencia y cobertura requerida |
|---|---|---|---|---|---|---|
| F1→F2 | F1: Acc=0 en elegibilidad; F2 evaluada desde S2 | R0/R1: F1 puede pasar a Acc=1; F2 se evalúa separadamente | ID/version, REL, COND, AUTH, RES, DEP, ¬BLOCK por paso | App(F1,S0); App(F2,S2); F1→F2=1 | Reserva por paso; C_auth basal fijo; sin doble consumo | Catálogo completo, contratos/versiones, verificación de cuatro componentes, recursos y snapshots t0/t3/t4 |
| A1→A2 | R0: ambas 0/ausentes con cobertura; R1: ruta 1; R2: estado basal fijado | R0 permanece 0; R1 estable; R2 puede cambiar bajo B | Mismos predicados para A1/A2 | App(A1,S0); App(A2,S1); A1→A2=1 | Recursos alternativos y permisos no compartidos salvo modelado | Inventario de alternativas, criterio F*, fuentes E1–E4, adjudicación ciega y cobertura basal/post |
| F1 sola | Basal 0 | Post depende de B y predicados | Predicados de F1 | No alcanza SF por sí sola | Según provisión | Evidencia técnica y de accesibilidad; no contar como Reach(SF) |
| A1 sola | Según R0/R1/R2 | Según escenario | Predicados de A1 | No alcanza SF por sí sola | Según escenario | Evidencia de A1 y ausencia/presencia de A2 |
| Rutas omitidas | No clasificable | No clasificable | Universo/cobertura no cerrados | ? | ? | Si catálogo o búsqueda no es exhaustiva, Reach=0 queda prohibido |

La matriz deberá implementarse como registros por unidad, ruta, paso, predicado, tiempo, truth, observación, fuente, cobertura, versión, adjudicación y motivo de indeterminación. No se rellenan evidencias con Outcome/Value.

## 7. Recursos, condiciones, autorización y bloqueos

### 7.1 Condiciones basales

- C_auth_base se fija y verifica antes de Z en el diseño focal aislado.
- C_domain se define por compatibilidad del objeto/clase, no por el estado concreto S0.
- C_resource distingue stock instalado, pool disponible, reserva por unidad y consumo en ejecución.
- C_capacity distingue capacidad nominal, slots disponibles por tiempo y precondiciones puntuales.
- C_info separa configuración técnica que habilita invocación de mensajes/conocimiento al agente.
- C_other no se admite como comodín: cada condición debe tener identidad, nivel, momento, fuente y rol causal.

### 7.2 Recursos del fixture

Cada instancia recibe recursos no compartidos R_i, con reserva temporal por transformación. F1/F2 y A1/A2 no se consideran simultáneamente ejecutables si consumen un mismo recurso limitante no duplicable. La reserva se evalúa para alcanzabilidad planificada; el consumo real se registra solo en ejecución.

### 7.3 Bloqueos

Cada transformación tiene BLOCK(τ,t) con estados 1/0/? y causa tipada: incompatibilidad, integridad, autorización, recurso, ventana temporal, dependencia externa, precondición o retirada. Un bloqueo confirmado de un predicado necesario refuta esa ruta concreta. Un bloqueo desconocido mantiene la ruta indeterminada.

## 8. Cobertura y exhaustividad

La cobertura se registra por dimensión:

1. Catálogo: todas las TID/SID/RID dentro de frontera y G.
2. Relaciones: todas las composiciones permitidas y prohibidas.
3. Condiciones: todos los predicados constitutivos y sus dependencias.
4. Alternativas: universo funcional F*, rutas candidatas y criterio Sub(π,F*,G,H,C0).
5. Recursos: disponibilidad temporal, reservas, exclusividad y concurrencia.
6. Tiempo: todos los pasos y ventanas dentro de H.
7. Identidad/versiones: matching y mapping resueltos para cada paso.
8. Observación: fuente, cobertura, validez, procedencia y adjudicación por predicado.

Cobertura exhaustiva solo puede declararse si las ocho dimensiones están cerradas y no hay rutas omitidas dentro de la frontera. La cobertura de enumeración computacional se informa aparte de la cobertura del universo semántico.

Resultado por estado objetivo:
- REACH=1: al menos una ruta completa confirmada.
- REACH=0: universo exhaustivo y todas las rutas refutadas.
- REACH=?: ruta potencial no resuelta o cualquier dimensión de cobertura insuficiente.
- OUT_OF_SCOPE / NOT_COMPARABLE: frontera, G o mapping incompatibles.

No encontrar A1/A2 no prueba su ausencia: R0 solo puede clasificarse sin alternativa si catálogo y búsqueda funcional están exhaustivamente cubiertos y adjudicados.

## 9. Códigos de evidencia y registro

Cada predicado deberá tener truth_dgp (solo generador/evaluador independiente), observed_state ∈ {1,0,?}, evidence_id, fuente, timestamp y versión; cobertura de catálogo/relación/alternativa; actor/adjudicador y cegamiento; regla/tolerancia aplicada; motivo de ?/OUT_OF_SCOPE/NOT_COMPARABLE.

El analizador no recibe truth_dgp. El evaluador independiente accede a la verdad solo después de sellar la clasificación observada.

## 10. Auditoría de coherencia y límites

1. Se preserva la separación entre accesibilidad, aplicabilidad, Reach, selección y ejecución.
2. Abrir F1 no implica Reach(SF)=1: F2 debe ser accesible, aplicable y componible.
3. A1→A2 puede mantener Reach(SF)=1 aunque F1 se abra; D_f* no equivale a cambio funcional exclusivo.
4. En R2, si B altera A1/A2, el contraste incluye una vía no focal y no se interpreta automáticamente como θ_Af ni LATE_f.
5. En R3, Z/W_attempt no implican C_dep, A_f* ni D_f*.
6. Ausencia de ruta exige cobertura exhaustiva; búsqueda truncada produce ?.
7. Outcome y Value no intervienen en estado, arista, accesibilidad ni Reach.
8. H=3 y topología de cuatro transformaciones son candidatos de fixture, no parámetros confirmatorios.

## 11. Pendientes antes de cerrar el inventario

- Aprobar frontera, G, H=3 y duración/ventanas.
- Definir F* y GOAL_F con criterios/tolerancias ex ante.
- Ratificar identidad contractual de τ2 y mappings de versiones.
- Decidir escenarios R0–R3 del DGP confirmatorio y contraste primario D1/D2.
- Completar predicados, fuentes E1–E4, cobertura de alternativas y adjudicación.
- Cerrar recursos, autorización, dependencias externas, reintentos y rollback.
- Definir snapshots dentro de H y relación con reloj t0–t9.
- Construir fixtures/oráculos para combinaciones relevantes 1/0/? y auditar errores.
- Revisión causal y transformacional independiente.

## 12. Dictamen

**Avance:** existe una topología finita candidata y un mapa de cobertura que permite operacionalizar las reglas de Reach sin confundir apertura focal con alcanzabilidad funcional.

**No cerrado:** catálogo, F*, G, H, recursos, comparador, escenario primario y cobertura de alternativas no están aprobados. La matriz es documental; no contiene datos ni fixtures ejecutables.

AUD-005 y AUD-007 permanecen abiertos. También siguen abiertos AUD-004, OPEN-C10-001/003/005/007 y XSYNC-138-03/06 según sus contratos.

No se ha implementado, generado datos, simulado, ejecutado, congelado ni autorizado el experimento.
