# C10-S — Gate 118: matriz integrada de decisiones causales y preparación para Design Freeze

**ID:** C10-S-GATE-118-CAUSAL-DESIGN-DECISION-MATRIX-001  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Estado:** HISTORICAL_CAUSAL_CONTRACTS_REUSED / ESTIMAND_SEPARATION_RECONCILED / DECISION_DEPENDENCIES_ORDERED / SCIENTIFIC_OWNER_CHOICES_OPEN / MATERIAL_AND_QUANTITATIVE_GATES_OPEN / NOT_DESIGN_FROZEN / NOT_IMPLEMENTATION_READY / NO_EXECUTION.

---

## 1. Pregunta y dictamen

¿Podemos convertir los Gates 109–117 y los contratos causales anteriores en una matriz finita que indique qué está realmente definido, qué puede cerrarse por reconstrucción documental, qué requiere decisión del responsable científico y qué necesita evidencia/materialización o parametrización?

**Dictamen:** sí, existe ya una base causal considerable y no debe reconstruirse desde cero. Los contratos históricos §§16.185–16.218 y los Gates 109–112 ya separan unidad, asignación, interferencia, soporte, resultados y estimandos. Gate 118 los integra con los hallazgos de identidad/roster de Gates 115–117 y ordena las dependencias.

La matriz no selecciona una arquitectura A/B/C/D, no aprueba roster A/B, no inventa un estimando residual ni convierte ITT en efecto de accesibilidad. El diseño sigue **NOT_DESIGN_FROZEN / NOT_IMPLEMENTATION_READY** porque las decisiones de población, asignación/interferencia, soporte y medición que condicionan la identificación no están resueltas ni materializadas.

**Hallazgo de eficiencia:** no necesitamos más gates de inventario general sobre los mismos conceptos. El siguiente trabajo debe ser una resolución científica concentrada de las decisiones P0 de esta matriz, seguida de una pasada de cierre contractual integrada. No abrir nuevas familias de IDs, tests o schemas.

## 2. Reconstrucción histórica reutilizada

| Fuente | Contenido que se reutiliza | Estado/límite |
|---|---|---|
| Plan maestro §§16.185–16.200 | Crosswalk causal de DGP, potenciales, observación, estimandos, población, soporte y rutas | Contratos estructurales; no freeze |
| Plan §§16.206–16.218 | DGP abstracto, truth/observed, V_cont, horizonte/medición S3, recuperación causal y abstención | Cierres estructurales; parámetros y aprobación pendientes |
| Gate 109 | UE, UA, cluster, U_G, instancia, versión, ruta y mappings no equivalentes por defecto | Mapping material incompleto |
| Gate 110 | Cuatro arquitecturas A–D y estimandos/condiciones diferenciados | Ninguna arquitectura seleccionada |
| Gate 111 | Reutilización de UNIT-01…14 y crosswalk de familias existentes | Cobertura contractual definida; no cobertura implementada/ejecutada |
| Gate 112 | Dependencias D1–D6, vacíos de asignación, interferencia, soporte, estimandos, outcomes y Analyzer | Dependencias confirmadas; no resueltas |
| Gates 115–117 | Campo lógico `ue_id`, roster/manifest propuesto, continuidad y alcance A/B abiertos | No roster aprobado/materializado; UE→U_G root UNKNOWN |
| DGP Temporal and Role Contract §§2–10 | Secuencia Z→B→W→S_install→C_dep→A_f→ΔT_acc→Reach→trajectory→Outcome→Value y roles | DRAFT / NO APPROVED / NO IMPLEMENTED |
| DEC-C10-095/096 y DEC-C10-066/067/099–102 | Need/cohorte, D2, separación de políticas y reglas V_cont | Decisiones y estipulaciones se preservan en su alcance; no amplían autorización |

Gate 118 es una reconciliación y ordenación. No reemplaza los contratos fuente ni crea un ledger paralelo.

## 3. Separación obligatoria de los objetos causales

| Objeto | Pregunta causal | Qué representa | No equivale a |
|---|---|---|---|
| ITT-D2((Y)) | ¿Qué efecto tiene asignar el paquete D2? | Efecto total de la política/paquete por resultado, población, unidad y régimen de interferencia | Efecto focal de accesibilidad |
| (	heta_A(q_X^*,r_{common};Y)) | ¿Qué cambia bajo intervenciones estocásticas sobre accesibilidad? | Contraste (g_{A1}) vs (g_{A0}) sobre el vector completo (Delta T_{acc}^*), con (q_X^*) común y régimen no focal (r_{common}) explícito | ITT-D2, cambio aislado de (A_f^*), o una coordenada de (Delta T_{acc}^*) |
| C4 | ¿Qué contribución se transmite por la vía mediadora bajo intervención longitudinal? | Estimando de mediación interventional con historia, orden temporal, confusión mediador–resultado, soporte secuencial y exposición definidos | ITT−(	heta_A), ajuste convencional por mediador o residual algebraico |
| LATE focal | ¿Cuál es el efecto local entre compliers bajo supuestos IV? | Estimando local condicionado a relevancia, independencia, exclusión, monotonicidad, consistencia, no interferencia y medición | ATE o (	heta_A) poblacional |
| Primeras etapas C2 | ¿Cómo cambia cada etapa bajo Z? | Contrastes separados sobre C_dep*, A_f*, D_f* y coordenadas de (Delta T_{acc}^*) | Outcome causal o prueba suficiente de mediación |

**Corrección de lenguaje sobre el residual:** las fuentes no autorizan definir un “efecto residual” como (ITT-	heta_A), ni como complemento automático de C4. Si el programa necesita cuantificar una vía directa/no mediada, deberá especificar un estimando directo interventional/controlled coherente con la misma población, intervención, historia y régimen de exposición. Hasta entonces se registran vías directas/colaterales en el DGP y se informa ITT como efecto de paquete; no se produce una cifra residual.

**Consecuencia central:** el objetivo científico de contribución de accesibilidad a Value sigue vigente, pero no se resuelve renombrando el ITT. La atribución exige identificación independiente de (	heta_A) y/o C4, con sus intervenciones y supuestos.

## 4. Matriz integrada de decisiones y dependencias

Estados:
- **REUSED / STRUCTURALLY DEFINED:** existe contrato suficiente en el alcance indicado; no implica aprobación global ni implementación.
- **OWNER DECISION OPEN:** requiere elección científica explícita; no puede decidirse por conveniencia documental.
- **MATERIAL EVIDENCE OPEN:** requiere roster, inventario, mapping, evidencia de aislamiento o artefactos concretos.
- **QUANTITATIVE SPECIFICATION OPEN:** requiere parámetros, soporte, precisión, potencia, umbrales o sensibilidad justificados.
- **DOWNSTREAM BLOCKED:** depende de una o varias filas anteriores.

| ID | Dominio/decisión | Estado recuperado | Cierre requerido | Clase | Dependencia/bloquea |
|---|---|---|---|---|---|
| M01 | Escenario focal | D2 es candidato primario; D1 secundario | Preservar precedencia DEC-C10-066/067; confirmar alcance en paquete final sin reabrir D1 por defecto | REUSED; aprobación global pendiente | Base del contraste D2 |
| M02 | Población primaria | (P^*_{\tau2}) candidata; (P^*_F) secundaria | Reconciliar universo con roster y elegibilidad pre-Z; no filtrar población primaria por alternativa secundaria | OWNER DECISION + MATERIAL | ITT, q_X*, soporte |
| M03 | Roster A/B | DEC-C10-096 deja separado vs conjunto abierto | Decidir si A/B son universos sintéticos distintos o políticas/escenarios sobre la misma población; justificar comparabilidad | OWNER DECISION OPEN | M02, UE continuity |
| M04 | Identidad UE | `ue_id` propuesto; roster_id/version/digest en PACKAGE_MANIFEST Draft | Definir alcance de unicidad, continuidad, replay, réplica y sucesión; aprobar contrato/roster antes de IDs | OWNER DECISION + CONTRACT | Cohorte, denominadores, reproducibilidad |
| M05 | UE–UA–cluster | Roles separados; UE=UA solo bajo aislamiento completo demostrado | Seleccionar/justificar arquitectura de asignación efectiva; declarar cardinalidades y nivel de aleatorización | OWNER DECISION + MATERIAL | Z, estimando, inferencia |
| M06 | Arquitectura de interferencia | Gate 110 A/B/C/D formalizadas; ninguna elegida | A: evidencia de aislamiento; B: cluster y spillover intercluster; C: mapa (G_i) y soporte; D: abstención/bounds. Elegir según DGP y evidencia, no por facilidad | OWNER DECISION + MATERIAL | Identificación ITT y efectos de exposición |
| M07 | Inventario de recursos compartidos | UNIT-02/03/04/05/06/07; DGP §§15/28 | Inventariar pools, dependencias, agentes, canales, estado compartido y carryover; separar correlación basal de spillover por Z | MATERIAL EVIDENCE OPEN | M06, suficiencia de G_i |
| M08 | Mecanismo Z | D2 asigna paquete; W_programmed distinto de Z y etapas posteriores | Cerrar UA, RNG/versionado, semilla, bloques/estratos, probabilidades, vector Z inmutable, provenance y mapping UA→Z | OWNER DECISION + CONTRACT + MATERIAL | Positividad y consistencia |
| M09 | Estimando ITT-D2 | Efecto total del paquete por resultado; Gate 110 | Instanciar (Y), población, unidad/ponderación, horizonte y régimen A/B/C; no condicionar post-Z | REUSED; instancia pendiente | M02, M05–M08, M12 |
| M10 | Target UE vs cluster | No intercambiables con tamaños de cluster desiguales | Elegir población/peso: promedio por UE o promedio por cluster; definir unidad de inferencia/varianza coherente | OWNER DECISION OPEN | M05, M09 |
| M11 | Mapa exposición (G_i) | Concepto y requisitos definidos; no especificado/materializado | Si arquitectura C, definir relaciones/versiones, suficiencia por resultado, probabilidades de exposición y soporte; sensibilidad a mapa misspecified/spillover residual | DOWNSTREAM BLOCKED / MATERIAL | M06–M08 |
| M12 | Soporte/positividad | QX y UNIT-09 existentes; soporte de Z, exposición, (g_A) y C4 separados | Definir historias (q_X^*), factibilidad de ambas políticas, soporte común y positividad por brazo/exposición/tiempo | QUANTITATIVE SPECIFICATION OPEN | M02, M06, M08, M11 |
| M13 | Consistencia/versiones/crossover | Separación asignada/recibida/aplicada y etapas establecida | Especificar desviaciones, versiones, contaminación, carryover y tratamiento de cambios; preservar ITT | CONTRACT + MATERIAL | M08, M09 |
| M14 | (	heta_A) sobre (Delta T_{acc}^*) | Estimando estructural existente; mapping D2→(g_A) no demostrado | Definir intervenciones factibles (g_{A1}/g_{A0}), (q_X^*), (r_{common}), unidad/exposición y soporte; demostrar no equivalencia automática con Z | OWNER DECISION + IDENTIFICATION OPEN | M06, M11, M12, M16 |
| M15 | C4 mediación interventional | Distinto de ITT y (	heta_A); confusión post-Z reconocida | Definir intervención mediadora longitudinal, historia, confusores inducidos por Z, positividad secuencial y exposición en cada etapa | DOWNSTREAM BLOCKED | M06, M11, M12, M16 |
| M16 | Vías directas/colaterales e interacciones | Deben permanecer explícitas; DGP/POL existentes | Declarar qué rutas puede activar D2; si se pretende efecto directo/residual, formular estimando interventional coherente; no usar resta algebraica | OWNER DECISION + DGP | Atribución focal |
| M17 | Outcome O-CONF | Unidad de adjudicación instancia×ruta | Cerrar mapping ruta/instancia→UE y regla de agregación solo si el estimando lo requiere; mantener O-CONF separado de Value | MATERIAL + CONTRACT | ITT por O-CONF |
| M18 | Value V_cont | Selección provisional DEC-C10-099; truth UE×K, ventana t0 y UNKNOWN→bounds según DEC-C10-100/101/102 | Cerrar soporte temporal numérico, K/Δ, medición S3, discriminación, calibración y aceptación; no convertir K en N | QUANTITATIVE + MATERIAL | ITT(V_cont), C4 |
| M19 | Observación/missingness | MEAS/MISS y S3 truth/observed separados | Especificar mecanismos diferenciales, cobertura, lag, pérdida, censura, dependencia y parámetros admisibles | QUANTITATIVE SPECIFICATION OPEN | Identificación/medición |
| M20 | Analyzer/Evaluator | Roles/firewall definidos en DGP/PE; PE contrato parcial | Cerrar serialización, schemas/enums, gates G-MAT/G-SCHEMA/G-ROLE/G-TEST/G-REPRO/G-AUTH y abstención por estimando | CONTRACT / DOWNSTREAM | Implementación |
| M21 | Sensibilidad y falsación | UNIT, P177–P183, S4R, POL, MEAS/MISS existentes | Especializar pruebas existentes sin nuevos IDs: falsa identificación, falsa atribución, abstención, G_i misspecification, spillover residual, medición diferencial | QUANTITATIVE + CONTRACT | Aceptación Analyzer |
| M22 | Precisión/potencia/umbrales | No se importan N/R/.80/.20/.80 históricos como parámetros confirmatorios | Definir MDE, α, potencia, cobertura, precisión, N/R, tasas máximas de falsa atribución/abstención y márgenes de equivalencia con justificación | QUANTITATIVE SPECIFICATION OPEN | Freeze cuantitativo |
| M23 | Mapping UE→U_G | UNKNOWN; no se deriva de B1 instance_id | Solo cerrar si la arquitectura PE requiere esa relación: mapping explícito y snapshot exacto, o justificar que no es requisito para el estimando/harness | MATERIAL / CONDITIONAL | Integridad PE |
| M24 | Aprobación paquete y roster | PACKAGE_MANIFEST/UNIT_BINDING Draft; NOT_APPROVED/NOT_MATERIALIZED | Aprobar contrato y roster versionado, digest, fuente autoritativa y censo pre-Z bajo DEC-C10-096 | OWNER DECISION + MATERIAL | Cualquier materialización |
| M25 | Design Freeze / implementación | No freeze; focal harness limitado a asignación individual con flag binario de no interferencia; B/C/D no implementados | Completar dependencias P0, contrato integrado, trazabilidad y revisión de autorización separada | DOWNSTREAM BLOCKED | Freeze y ejecución |

## 5. Orden causal de resolución (no orden de numeración)

No resolver los elementos según el orden del inventario. La secuencia que minimiza retrabajo es:

**P0 — decisiones que determinan el diseño**
1. M03 roster A/B y M02 población objetivo.
2. M05 UE–UA–cluster y M06 arquitectura A/B/C/D, sustentadas por M07 inventario de interferencia.
3. M10 target/peso UE vs cluster.
4. M08 mecanismo Z compatible con UA y arquitectura elegida.
5. M04 identidad/continuidad UE y M24 contrato/roster pre-Z.

**P1 — identificación de los efectos**
6. M11 mapa (G_i), si C; o prueba de aislamiento/cluster si A/B.
7. M12 soporte/positividad conjunta y consistencia/versiones M13.
8. M09 ITT-D2 por resultado.
9. M14 intervención (g_A) y M15 C4; M16 rutas directas/colaterales y cualquier estimando directo interventional requerido.

**P2 — medición y recuperación**
10. M17 mapping O-CONF y M18 V_cont.
11. M19 medición/missingness.
12. M20 firewall/schema PE y M21 sensibilidad/falsación.
13. M22 precisión/potencia/umbrales.

**P3 — integridad final**
14. M23 mapping UE→U_G solo si se demuestra necesario para la arquitectura seleccionada.
15. Integrar contrato, matriz de trazabilidad, criterios de freeze y autorización independiente.

El orden es parcialmente iterativo: el soporte puede obligar a restringir la población ex ante, pero no se permite cambiarla después de observar resultados.

## 6. Qué puede cerrarse documentalmente y qué no

### 6.1 Reutilizable sin nueva decisión

- No crear otra familia de tests de interferencia: UNIT-01…14 es la referencia primaria.
- No equiparar UE, UA, cluster, UO, U_G root, instancia CMP, EID, route, fixture o run.
- No asumir SUTVA ni ITT individual cuando interferencia no está resuelta.
- Mantener ITT-D2, (	heta_A), C4, LATE y primeras etapas como objetos distintos.
- No definir residual como ITT−(	heta_A) ni C4.
- Mantener O-CONF instancia×ruta y V_cont UE×K, truth separado de observed.
- Preservar Generator/Analyzer/Evaluator y abstención/bounds como salidas válidas.
- Reutilizar los contratos de población, soporte, Value, temporalidad y observación en su alcance vigente.

### 6.2 Requiere decisión científica explícita

- A/B separado vs conjunto y comparabilidad de población.
- Arquitectura efectiva de asignación/interferencia (A/B/C/D).
- Unidad/target de inferencia y ponderación UE vs cluster.
- Si el objetivo incluye un efecto directo/no mediado adicional y qué estimando lo representa.
- Intervenciones (g_A) y régimen (r_{common}) sustantivos cuando no estén fijados por contrato.
- Qué población/historias se excluyen por falta de factibilidad/soporte y con qué estimando restringido.

### 6.3 Requiere evidencia/materialización o parametrización posterior

- Roster aprobado/versionado, identidades y bindings.
- Inventario y prueba de aislamiento, o roster de clusters/mapa G_i.
- RNG, probabilidades, vector Z y provenance.
- Soporte y positividad efectivos.
- Mapping O-CONF ruta/instancia→UE, y mapping UE→U_G solo si requerido.
- Medición S3, horizonte y rejilla V_cont.
- MDE, potencia, precisión, sensibilidad y tasas de error/abstención.

## 7. Criterios mínimos para Design Freeze

No se propone congelar por completar un número de gates. Se podrá proponer Design Freeze únicamente cuando:

1. Población, roster y alcance A/B estén aprobados, versionados y con censo pre-Z reproducible.
2. UE, UA, cluster y UO tengan roles/cardinalidades definidos; mecanismo de asignación y unidad de inferencia sean coherentes.
3. Arquitectura de interferencia elegida con evidencia: aislamiento demostrado, o cluster/mapa suficiente y soporte; si no, el diseño se limita explícitamente a abstención/bounds.
4. ITT-D2 esté instanciado por resultado, población, unidad, ponderación, horizonte y política asignada.
5. (	heta_A) y C4 tengan intervención, población, historia, soporte y condiciones de identificación propias; la atribución residual/directa, si se desea, tenga estimando definido y no algebraico.
6. O-CONF y V_cont tengan mappings, verdad, observación y reglas temporales/medición cerradas en su alcance.
7. Confusión post-Z, vías directas/colaterales, consistencia/versiones, missingness y sensibilidad estén tratados.
8. Analyzer/Evaluator tenga interfaces, serialización, firewall, abstención y criterios de recuperación definidos.
9. Los contratos de pruebas existentes cubran los escenarios seleccionados y los falsadores sin duplicación.
10. MDE, potencia, precisión, cobertura, N/R y tolerancias estén justificados y aprobados.
11. El contrato integrado no contradiga DEC/RMA/Evidence→Claim ni las decisiones fuente.
12. Exista una autorización explícita separada para implementación; Design Freeze no autoriza por sí solo ejecución científica.

## 8. Criterios de readiness para implementación

Incluso después del freeze, la implementación debe ser por fases y bajo autorización:
- **Fase 0 — contrato:** paquete causal/PE aprobado, interfaces y schemas versionados, invariantes y test crosswalk fijados.
- **Fase 1 — infraestructura de diseño:** roster/configuración reproducible, Generator/Analyzer/Evaluator aislados, provenance y truth firewall.
- **Fase 2 — núcleo D2:** solo la arquitectura de asignación/interferencia aprobada; no implementar A/B/C/D completos por anticipado.
- **Fase 3 — outcomes/medición:** V_cont y O-CONF según unidad propia y reglas aprobadas.
- **Fase 4 — Analyzer:** ITT, identificación, bounds/abstención y, solo cuando identificables, (	heta_A)/C4.
- **Fase 5 — validación estática y tests autorizados:** sin generación/estimación científica hasta autorización específica.
- **Fase 6 — ejecución científica:** requiere autorización, preflight, provenance y workflow técnico completo.

No se implementa ni ejecuta en Gate 118.

## 9. Preguntas que sí requieren respuesta del responsable científico

La matriz reduce las decisiones irreducibles a cinco:

1. **Población A/B:** ¿A y B representan universos de unidades distintos o son políticas/escenarios comparables sobre una misma población sintética?
2. **Interferencia:** ¿Qué arquitectura pretende representar el DGP confirmatorio: A aislamiento individual, B asignación por cluster, C asignación individual con mapa de exposición, o D como mundo deliberadamente no identificable? La opción D puede ser adversarial, no necesariamente arquitectura principal.
3. **Unidad/target:** si hay cluster, ¿el target principal es promedio por UE o por cluster?
4. **Atribución focal:** además de ITT de paquete, ¿se exige estimar (	heta_A), C4 y un efecto directo interventional separado, o el objetivo confirmatorio se limita a ITT más evaluación separada de atribución cuando sea identificable?
5. **Continuidad UE:** ¿la identidad de UE debe persistir entre escenarios/versiones para comparación emparejada, o basta la identidad dentro del roster/paquete versionado con matching explícito solo cuando sea necesario?

No se solicita decidir RNG, semilla, N, K, p*, umbrales o claves técnicas ahora: son especificaciones posteriores dependientes de las decisiones P0 y de soporte.

## 10. Dictamen de Gate 118

**Resultado:** `GATE_118_CAUSAL_DECISION_MATRIX_RECONCILED / HISTORICAL_CONTRACTS_REUSED / ITT_THETA_A_C4_AND_DIRECT_EFFECT_SEPARATED / RESIDUAL_NOT_DEFINED_BY_SUBTRACTION / P0_OWNER_DECISIONS_OPEN / MATERIAL_AND_QUANTITATIVE_DEPENDENCIES_OPEN / DESIGN_FREEZE_NOT_READY / IMPLEMENTATION_NOT_READY / NO_NEW_TEST_IDS / NO_SCHEMA_CHANGE / NO_EXECUTION`.

La matriz muestra que el diseño no está a unas pocas tareas de programación: todavía depende de cinco decisiones científicas de arquitectura y de evidencias/parametrizaciones encadenadas. A la vez, la base conceptual está suficientemente reconstruida para evitar nuevos gates generales de inventario. El próximo paso debe resolver las decisiones P0 y convertir sus respuestas en un contrato integrado, sin reabrir lo ya establecido.

**Siguiente operación:** Gate 119 — decisión guiada de arquitectura causal D2. Preparar una comparación de las cinco preguntas del §9 contra la pregunta causal primaria, los mundos adversariales y el alcance confirmatorio; recomendar una combinación coherente sin convertirla en decisión aprobada. Si la evidencia no permite una recomendación, delimitar exactamente las opciones y sus consecuencias para identificación.

## 11. Gobernanza y autorización

- No se modifican DEC-C10-095/096 ni otras decisiones fuente; no se cambia C0, U_G, RMA, Evidence→Claim Matrix, STATUS ni main.
- No se crea roster, ID, cluster, mapa, schema, tabla, fixture o test ID.
- No se modifica el focal harness ni el contrato PE.
- No se ejecutan validadores, código, tests, workflows, simulaciones, estimaciones, calibraciones o experimentos.
- PR #116 permanece Draft.
- `scientific_execution=false`; `execution_authorized=false`.
