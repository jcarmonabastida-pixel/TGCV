# C10-S — Matriz de reconciliación P179/P182/P183 y núcleo mínimo Outcome/Value

**ID:** C10-S-VALUE-MIN-001  
**Versión:** Draft 001  
**Estado:** DRAFT / PROPUESTA DE RECONCILIACIÓN / NO ACEPTADA / NO CONGELADA  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116  
**Ámbito:** C10-S, paquete C-Value; no autoriza implementación ni ejecución.

## 1. Propósito y regla de precedencia

Esta matriz depura el contenido de P179, P182 y P183 frente al contrato histórico C-Value (§224), su especialización actual (§§264–265) y el crosswalk contra la instancia real `C10S-SVC-REQUEST-PROCESSOR v1.0.0` (§265; roster §232; DAG §233; superficies B-M01…15).

No crea una taxonomía adicional, no sustituye contratos fuente y no convierte dimensiones candidatas en variables obligatorias. La fuente normativa y sus decisiones aceptadas prevalecen; esta matriz es una propuesta de integración que debe cotejarse contra el texto íntegro de cada contrato antes de su aceptación.

Regla de no invención: ningún beneficiario, stakeholder, función de utilidad, indicador, escala, ponderación, umbral, horizonte ni estado terminal se presume por analogía. Un dato ausente se registra como OPEN/UNKNOWN, nunca como cero ni como evidencia de inexistencia.

## 2. Fuentes y alcance recuperado

| Fuente | Función que se reutiliza | Límite de esta reconciliación |
|---|---|---|
| P179 | Contrato de especificación/interpretación de Value y de sus reglas de agregación y sensibilidad, en el alcance que establezca su texto fuente | No se da por aprobada una fórmula escalar, vector concreto ni ponderación |
| P182-01…12 | Validez de constructo y sensibilidad de medidas: cobertura, circularidad, especificación O, separación O/V, reproducibilidad, acuerdo, error, invariancia, sensibilidad, firewall y trazabilidad | No crea dimensiones ni define por sí solo indicadores |
| P183-01…13 | Ausencia, selección, censura, missingness, cotas y dictamen separado por estimando | No transforma ausencia de observación en ausencia del constructo |
| C-Value §224 | Contrato histórico Outcome/Value que debe conservar precedencia en su alcance | Requiere cotejo literal de cada campo/decisión contra el maestro |
| C-Value §§264–265 | Candidatos y auditoría de correspondencia con roster de Opción A | El crosswalk recibido constata operacionalización incompleta |
| §232 / §233 / B-M01…15 | Roster, DAG y superficies observables de la instancia | Una superficie observable no es todavía indicador validado ni beneficiario |
| Registro de contratos de prueba, §§9 y 13 | POL-01…10; P182-01…12; P183-01…13 y reglas de adjudicación | Contratos propuestos; no fixtures implementados ni pruebas ejecutadas |

## 3. Matriz de depuración de dimensiones candidatas

Las cinco filas siguientes reproducen únicamente el conjunto candidato que se ha venido manejando en C-Value; no se declaran dimensiones aprobadas por P179. Su inclusión y definición literal deberán cotejarse con el contrato fuente antes de cerrar esta matriz.

| Dimensión candidata | Fundamento que puede conservarse | Riesgo de redundancia/circularidad | Dictamen propuesto | Condición para reconsiderarla |
|---|---|---|---|---|
| Eficiencia | Posible valoración de recursos/tiempo/esfuerzo para un beneficiario identificado | Recursos técnicos observados no equivalen a coste económico ni a esfuerzo; solapamiento parcial con carga operativa O | CONDITIONAL | Beneficiario, perspectiva, recurso valorado, unidad, coste/precio o proxy validado, ventana y regla de valoración |
| Calidad | Posible valoración de propiedades del servicio/resultado | Conformidad técnica no equivale automáticamente a calidad valorada; no reutilizar el mismo indicador como O y V sin justificación | CONDITIONAL | Criterio de calidad independiente, evaluador/fuente, escala, tolerancia, población y horizonte |
| Acceso de destinatarios | Posible valor de que destinatarios reales puedan obtener/usar el servicio | No confundir acceso del destinatario con T_acc transformacional; beneficiario/destinatario no identificado | CONDITIONAL | Identidad/rol del destinatario, unidad de acceso, necesidad, criterio de acceso y medida no derivada de T_acc |
| Robustez | Posible valor de estabilidad ante perturbaciones | Solapamiento potencial con continuidad, recuperación, disponibilidad y resiliencia como Outcomes | CONDITIONAL | Perturbación/historia, propiedad valorada, horizonte, tolerancia y demostración de que no duplica O |
| Sostenibilidad | Posible valoración intertemporal | Horizonte, sujeto de valoración y dimensión (económica, operativa, ambiental u otra) indeterminados | DEFER / CONDITIONAL | Dominio explícito, perspectiva, horizonte y criterio verificable; no incorporar como categoría genérica |

**Resultado:** ninguna dimensión de esta lista está actualmente habilitada como Value confirmatorio en la instancia Opción A. CONDITIONAL no significa rechazada: significa que la dimensión no entra en el núcleo confirmatorio hasta satisfacer su condición material.

## 4. Crosswalk de Outcome: no confundir evidencia superficial con operacionalización

| Outcome candidato de §264 | Hallazgo del crosswalk de §265 | Clasificación | Trabajo mínimo pendiente |
|---|---|---|---|
| O-MIG — migración | No existe campo de estado terminal | NOT_GROUNDED como medida actual | Definir evento terminal, unidad, criterio de éxito/fallo, fuente y snapshot |
| O-CONF — conformidad | Anclaje conceptual en F*/FP-01…08 | CONDITIONAL; mejor anclaje actual | Predicados, mapping, tolerancias, oráculo, snapshots, cobertura y adjudicación |
| O-SVC — continuidad | Superficies observables, sin indicador definido | NOT_GROUNDED como indicador actual | Definir continuidad, denominador, ventana, interrupciones admisibles y fuente |
| O-REC — recuperación | Referencias a rollback/estado persistente, sin medida de recuperación | NOT_GROUNDED como indicador actual | Definir evento adverso, estado de referencia, recuperación terminal, tiempo y criterio |
| O-BUR — carga operativa | Recursos/rendimiento disponibles, sin medición de esfuerzo/coste | NOT_GROUNDED como indicador actual | Definir actor, esfuerzo/coste, unidad, instrumento y ventana |

O-CONF puede mantenerse como candidato prioritario de Outcome para el trabajo de operacionalización, pero no debe etiquetarse como operacionalizado ni como Value. Los demás candidatos no se eliminan del historial; permanecen fuera del núcleo hasta que exista un contrato medible.

## 5. Separaciones semánticas obligatorias

1. **T_acc / ΔT_acc ≠ Outcome ≠ Value.** Accesibilidad, Reach y trayectoria pertenecen a la cadena transformacional/causal; no constituyen por sí mismas una valoración.
2. **Outcome ≠ Value.** Outcome describe un resultado operacional definido; Value requiere además perspectiva/beneficiario y criterio de valoración explícitos.
3. **CMP.owner ≠ beneficiario.** La propiedad/autoría del componente no identifica quién recibe o valora el servicio.
4. **Recurso consumido ≠ coste económico.** Hace falta perspectiva, precio/coste o proxy validado y regla de imputación.
5. **Disponibilidad de A1/A2 ≠ valor de portabilidad.** La existencia técnica de una ruta no prueba su utilidad ni valoración.
6. **No ejecución ≠ inaccesibilidad.** Se preservan los estados de accesibilidad, aplicabilidad, conocimiento/consideración, selección e implementación/ejecución.
7. **No observado ≠ cero; Value no definido ≠ Value no medido.** Aplicar P183 y la taxonomía de ausencia correspondiente.

## 6. Núcleo confirmatorio mínimo: especificación por capas

### 6.1 Núcleo metodológico que sí puede fijarse documentalmente

- A: medida independiente de accesibilidad/ΔT_acc*, con temporalidad, versión, unidad y evidencia; no depende de O ni V.
- O: como máximo un Outcome primario en el microdominio, seleccionado por justificación y operacionalizado antes de ejecución.
- V: una dimensión primaria (V_1) solo si se identifica beneficiario/perspectiva y una regla de valoración independiente y reproducible.
- Estimandos: adjudicación independiente para ITT de asignación/política, efecto focal solo si se sostienen sus condiciones de atribución, efecto interventional si se identifica y la pregunta general θ_A(q). No transferir conclusiones entre estimandos.
- Medición: P182 para validez, error, invariancia y trazabilidad.
- Ausencia/selección: P183 para missingness, censura, cotas y dictámenes.
- Evaluación: generador, analizador y evaluador separados; el analizador no recibe truth/potenciales ni Value potencial.

### 6.2 Núcleo material actualmente disponible

| Componente | Estado actual | ¿Confirmatorio ejecutable? |
|---|---|---|
| A / ΔT_acc* | Arquitectura y crosswalk semánticos parciales; inputs materiales, fuentes y medición pendientes | NO |
| O primario | O-CONF mejor anclado, pero sin predicados/mapping/tolerancias/oráculo/snapshots completos | NO |
| Beneficiario/perspectiva | No confirmado en roster | NO |
| V1 / regla de valoración | No operacionalizado; sin beneficiario ni criterio confirmado | NO |
| Función escalar/ponderaciones | No aceptadas; fórmula ilustrativa anterior no es decisión | NO |
| Missingness/selección | Contratos P183 disponibles; mecanismo y parámetros concretos pendientes | NO |
| Validez/error | Contratos P182 disponibles; instrumentos, tolerancias y validación pendientes | NO |

**Conclusión:** puede definirse un núcleo confirmatorio mínimo como arquitectura de diseño, pero no hay actualmente un núcleo material A–O–V completo ejecutable. La ausencia de V1 no debe ocultarse mediante un índice sustituto ni resolverse inventando beneficiarios.

## 7. Reglas de clasificación KEEP / REDUNDANT / CONDITIONAL / NOT_GROUNDED

| Objeto | Clasificación | Justificación |
|---|---|---|
| Separación A/O/V y no circularidad | KEEP | Requisito constitutivo de validez y atribución |
| P182 como contrato transversal de medición | KEEP | Complementa, no duplica, la definición de constructos |
| P183 como contrato transversal de ausencia/identificación | KEEP | Complementa, no crea dimensiones |
| P179 como contrato de Value y agregación/sensibilidad | KEEP, sujeto a precedencia literal | Evitar reemplazarlo por taxonomía nueva |
| Cinco dimensiones candidatas | CONDITIONAL | Mantener como catálogo histórico no obligatorio |
| Índice escalar y ponderaciones | NOT_GROUNDED | Sin decisión, beneficiario, escalas ni pesos justificados |
| O-CONF | CONDITIONAL | Anclaje conceptual existente, operacionalización incompleta |
| O-MIG/O-SVC/O-REC/O-BUR como medidas actuales | NOT_GROUNDED | El crosswalk no acredita indicadores completos |
| Recursos = coste | REDUNDANT / invalid inference | No es una dimensión independiente ni inferencia válida; requiere conversión/valoración |
| Continuidad + recuperación + robustez como un único indicador | REDUNDANT si se fusionan sin teoría | Mantener constructos separados hasta demostrar equivalencia |
| T_acc/Reach/trayectoria como Value | NOT_GROUNDED / circular | Son constructos de la cadena causal, no valoración |
| CMP.owner como beneficiario | NOT_GROUNDED | No existe equivalencia semántica acreditada |
| A1/A2 disponibles como valor de portabilidad | NOT_GROUNDED | Capacidad técnica no acredita utilidad/valor |

## 8. Bloqueos exactos para pasar de arquitectura a operacionalización

1. **B1 — Perspectiva/beneficiario:** identificar en el dominio quién recibe, usa o valora el servicio; distinguir owner, operador, usuario, cliente y beneficiario sin presumir equivalencia.
2. **B2 — Criterio V:** documentar qué resultado se valora, por quién, en qué dirección y bajo qué regla; justificar si V es vectorial o si se requiere agregación.
3. **B3 — Outcome primario:** decidir si O-CONF es el Outcome primario y completar predicados, mapping, tolerancias, oráculo, snapshots y cobertura.
4. **B4 — Independencia A/O/V:** demostrar fuentes, tiempos, evaluadores y reglas que impiden circularidad y leakage.
5. **B5 — Medición y error:** instrumentos, unidades, validez, fiabilidad, acuerdo, error y tolerancias ex ante conforme P182.
6. **B6 — Ausencia/censura:** taxonomía por variable y tiempo, mecanismo plausible, selección y sensibilidad/cotas conforme P183.
7. **B7 — Horizonte y versiones:** fijar ventana/horizonte, versiones del servicio y tratamiento de trade-offs sin agrupar versiones causalmente distintas.
8. **B8 — Estimando y adjudicación:** mantener separado ITT_Z, efecto de política/paquete, efecto focal y mediación; dictamen por estimando × Outcome/Value × población × horizonte × versión conforme MAP-07.
9. **B9 — Evidencia y reproducibilidad:** snapshots, fuentes, cobertura, oráculo, provenance y artefactos evaluables sin dar por implementada la separación Generator/Analyzer/Evaluator.

No se añaden bloqueos genéricos ni se convierten en requisitos de dimensión. Cada bloqueo debe cerrarse con evidencia concreta o declararse no identificable/no disponible.

## 9. Consecuencias para los paquetes C/D/E y gates

- **C / C-Value:** puede avanzar en reconciliación documental y definición de criterios; permanece OPEN materialmente mientras B1–B6 no se resuelvan.
- **D:** debe consumir la especificación mínima y los estados OPEN/UNKNOWN sin inventar schema, indicador o regla de valoración.
- **E:** no puede aceptar integración confirmatoria mientras A/O/V, sus contratos de datos y adjudicación no estén materialmente definidos.
- **MED-02 y MED-03:** no se declaran cerrados por esta matriz.
- **Design Freeze:** no procede.
- **Implementación/ejecución:** no autorizadas.

## 10. Decisiones propuestas para revisión

| Propuesta | Contenido | Estado |
|---|---|---|
| PROP-VALUE-01 | Mantener las cinco dimensiones como catálogo candidato, no como obligaciones confirmatorias | PROPUESTA |
| PROP-VALUE-02 | No definir índice escalar ni ponderaciones sin regla de valoración justificada | PROPUESTA |
| PROP-VALUE-03 | Mantener Outcome y Value separados; O-CONF es candidato prioritario, no cerrado | PROPUESTA |
| PROP-VALUE-04 | Exigir beneficiario/perspectiva explícitos antes de aceptar cualquier V_j confirmatorio | PROPUESTA |
| PROP-VALUE-05 | Permitir un solo V1 confirmatorio si y solo si tiene fundamento material suficiente; no exigir cinco dimensiones | PROPUESTA |
| PROP-VALUE-06 | Si no se operacionaliza V1, limitar las conclusiones sintéticas a los módulos/estimandos que sí puedan evaluarse y declarar no disponible la atribución a Value | PROPUESTA |

Estas propuestas no modifican DEC-C10 existentes ni constituyen aceptación por sí mismas. Requieren reconciliación con el texto íntegro de P179 y C-Value §224, comprobación de precedencia y registro explícito de aceptación antes de tratarlas como decisión.

## 11. Estado y siguiente gate

**Dictamen de esta matriz:** DOCUMENTARY RECONCILIATION PROPOSED / MATERIAL OUTCOME-VALUE OPEN.

Siguiente gate: cotejar fila por fila esta matriz con el texto íntegro de P179 y C-Value §224; resolver cualquier diferencia semántica/precedencia; después registrar aceptación o discrepancias. Solo entonces abordar B1–B3 (beneficiario, criterio V y Outcome primario) con evidencia del dominio, sin inferencias desde CMP.owner ni desde recursos técnicos.

No se ha modificado `main`; no se ha cerrado MED-02/MED-03; no hay Design Freeze, implementación ni ejecución científica.

`scientific_execution=false`  
`execution_authorized=false`
