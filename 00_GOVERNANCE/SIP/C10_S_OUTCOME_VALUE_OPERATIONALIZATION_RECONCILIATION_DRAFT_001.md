# C10-S — Reconciliación integrada de operacionalización confirmatoria de Outcome y Value

**ID:** C10-S-OV-OPERATIONALIZATION-001  
**Fecha:** 2026-11-11  
**Estado:** MEASUREMENT_ARCHITECTURE_RECONCILED / O-CONF_CANDIDATE_NOT_FROZEN / VALUE_VECTOR_PRESERVED_NOT_INSTANTIATED / NO_CONFIRMATORY_Y / NOT_DESIGN_FROZEN  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Objeto, precedencia y reutilización

Este ciclo integra la operacionalización confirmatoria de Outcome y Value. Reutiliza, sin duplicar ni reemplazar:
- maestro C10-S §§222–225, 232–233, 253–266 y 273–275;
- C10_S_B2_B3_BENEFICIARY_OUTCOME_VALUE_RECONCILIATION_DRAFT_001.md;
- C10_S_FSTAR_OPERATIONAL_PROPERTY_AND_ADJUDICATION_MATRIX_DRAFT_001.md y fichas Opción A;
- C-Value §264 y crosswalk de roster/eventos §265;
- PA/C1, PB/PB-MAT, PC/C3-C4, PD/DGP, PE/roles y el ciclo D2 de asignación/población/soporte;
- contratos existentes P179-01…08, P182-01…12, P183-01…13, §224 y familias MEAS/MISS existentes.

No crea Decision Record, dimensiones, instrumentos, campos, eventos, escalas, pesos, umbrales, ventanas, parámetros, N/R ni fixtures. No reabre B1, D2, P*τ2/P*_F ni decisiones aceptadas.

## 2. Regla central: tres objetos distintos

Se mantienen tres capas no intercambiables:

1. **Criterio funcional F*:** especificación técnica versionada que define cuándo una ruta completa satisface los requisitos funcionales obligatorios aplicables. FP-01…FP-07 describen propiedades funcionales; FP-08 es gate probatorio independiente.
2. **Outcome O-CONF:** resultado adjudicado del estado de conformidad funcional del destino en la instancia/horizonte evaluados. El criterio F* y el resultado O-CONF no son dos resultados técnicos independientes. O-CONF puede usar la adjudicación F* como su anclaje de medida, sin duplicar F* como otro endpoint, covariable o mediador.
3. **Value V:** valoración contextual de una o más consecuencias para B1 respecto de Need_preZ, bajo perspectiva, autoridad y criterio de valoración estipulados ex ante. No es el resultado técnico ni la evidencia usada para medirlo.

La especificación objetivo, la verdad generada, la observación y la adjudicación deben seguir separadas. Un F*=1/O-CONF favorable no implica Value positivo; un fallo funcional no determina por sí solo el valor contextual.

## 3. O-CONF: candidato prioritario, no selección confirmatoria

### 3.1 Constructo y unidad

Se conserva O-CONF —conformidad funcional del destino— como candidato con mejor anclaje conceptual entre los Outcomes históricos. Su objeto es el estado realmente aplicado en el destino, evaluado frente a la especificación funcional versionada y al contrato F* común. No mide intento, recepción, instalación, C_dep*, A_f*, D_f*, ΔT_acc*, Reach, selección, ejecución ni satisfacción de B1.

La unidad de medida debe ser la instancia lógica de servicio/UE y su estado terminal evaluable en una ventana común. No se ha aceptado aún la identidad material/roster, el evento terminal, H, la ventana ni la granularidad definitiva; por tanto, esta unidad es una condición de la ficha, no un mapping físico ya establecido.

### 3.2 Regla de resultado sin inventar escala

La regla vigente de F* es no compensatoria y trivalente sobre FP-01…FP-07 aplicables:
- 1: todos los requisitos funcionales obligatorios aplicables están demostrados;
- 0: al menos una violación obligatoria está demostrada;
- ?: no hay violación demostrada, pero al menos un requisito pertinente permanece desconocido/contradictorio.

FP-08 determina validez probatoria, procedencia y reproducibilidad; no es propiedad funcional ni se suma a F*. Si la evidencia FP-08 no permite aceptar la adjudicación, O-CONF observado debe conservar estado no válido/indeterminado según el contrato de evidencia, sin cambiar la verdad funcional del DGP.

No se convierte ? en 0, ni NA en ausencia, ni se inventa puntuación continua/porcentual. No se presupone ordinalidad entre 0/1/? ni se define un modelo estadístico para esas categorías en este ciclo. Si en el futuro se desea una magnitud graduada de conformidad, deberá justificarse como constructo/indicador adicional, con unidades, reglas y validez; no se deriva de sumar FP ni de tolerancias arbitrarias.

### 3.3 Ficha O-CONF — campos exigidos y estado

| Campo §224 | Requisito para cierre | Estado |
|---|---|---|
| ID/versión/constructo/frontera | Identidad versionada de O-CONF y relación explícita con F* | Candidato conceptual; ficha no congelada |
| Unidad/población | UE/instancia de servicio, relación con P*τ2 y asignación | Unidad lógica aceptada; roster/materialización OPEN |
| Especificación de referencia | F* y contrato fuente/destino versionados, propiedades obligatorias/condicionales/NA | Familias FP aceptadas; predicados/IAM no cerrados |
| Mapping | C_src→M→C_dst_decl→C_dst_applied y predicados atómicos | OPEN |
| Evento/estado terminal | Snapshot de destino aplicado y punto de adjudicación común | OPEN; sin event_id/snapshot material |
| Fuente primaria/corroboración | Evidencia E_T independiente, trazable y con cobertura suficiente | Arquitectura definida; fuente/oráculo no implementados ni validados |
| Regla de cálculo/dirección | Adjudicación no compensatoria 1/0/?; FP-08 separado | Lógica documental disponible; instancia no evaluable |
| Baseline/comparabilidad | C0 pre-Z, misma versión de F*, G y contexto comparable | C0/G/H y snapshots OPEN |
| Ventana/horizonte | Ancla y H común preespecificado | OPEN; AB-TIME-01/02 |
| Validez/error/reproducibilidad | Falsos positivos/negativos, acuerdo, error, invariancia y validación del oráculo | OPEN; P182 y MEAS reutilizables |
| Ausencia/censura | Estados observacionales diferenciados y mecanismos por brazo/historia | Contrato P183/MISS definido; parámetros y aplicación OPEN |
| Cegamiento/provenance | Adjudicador ciego a Z/B y downstream cuando sea viable; versionado inmutable | Requisito definido; no demostrado |

**Dictamen O-CONF:** candidato prioritario de Outcome técnico; no está operacionalizado ni puede incorporarse todavía como Y confirmatorio completo. No se seleccionan O-MIG/O-SVC/O-REC/O-BUR: sus vacíos históricos permanecen, sin reabrirlos ni promoverlos.

## 4. Value: admisibilidad de dimensiones, sin selección artificial

### 4.1 Referente y criterio de admisibilidad

B1 es la entidad sintética solicitante-beneficiaria estipulada, una por UE. Need_preZ es el objetivo/necesidad focal existente en truth antes de Z; no se infiere de Request_event, procesamiento, uso o resultado. El contenido de Need_preZ y su evidencia/medición material permanecen OPEN.

Una dimensión V_j solo es admisible si:
1. expresa una consecuencia identificable para B1 respecto de Need_preZ;
2. declara perspectiva y autoridad de valoración ex ante, coherentes con el mundo sintético y representativas del interés de B1;
3. define criterio y frontera semántica frente a Outcome, accesibilidad, trayectoria, ejecución, recursos y otras V_k;
4. puede medirse independientemente con fuente/instrumento, unidad/escala y baseline/post/horizonte definidos;
5. conserva dirección, interpretación, ausencia, error, validez y regla de adjudicación;
6. declara si es compensable/no compensable y sus trade-offs con otras dimensiones, sin ponderación por defecto.

El Evaluator aplica una regla de valoración estipulada; no se convierte en beneficiario ni valida preferencias reales. La regla no se infiere de CMP.owner, operador, mantenedor, ejecutor, disponibilidad de recursos o telemetría.

### 4.2 Perspectiva y autoridad

La perspectiva primaria es la de B1 por estipulación del modelo. La autoridad que define el criterio valorativo debe quedar expresamente incorporada a truth_dgp, con identidad, versión, justificación y simetría entre brazos. Esto es una regla normativa interna del DGP, no una afirmación de preferencia empírica real.

No se inventa un representante humano, usuario, propietario de servicio ni encuesta. Si se introduce más de una perspectiva legítima, se conserva la pluralidad o se justifica una regla de representación; no se promedian valoraciones heterogéneas por defecto.

### 4.3 Vector y dimensiones no seleccionadas

Se preserva P179: Value se mantiene como vector (V=(V_1,ldots,V_k)) durante identificación. k, la selección de dimensiones y sus indicadores siguen OPEN. Las cinco dimensiones históricas (eficiencia, calidad, acceso de destinatarios, robustez y sostenibilidad) son candidatas de referencia, no un roster aprobado ni exhaustivo.

En particular:
- ΔT_acc*, A_f*, Reach y trayectoria no son Value ni proxies automáticos de V_j.
- Una dimensión de acceso/posibilidad solo podría incorporarse si mide una consecuencia valorada para B1, distinta de la accesibilidad estructural del sistema y justificada en el DGP.
- Consumo de CPU/RAM, capacidad disponible, logs, costes monetarios o esfuerzo humano no se convierten en valor sin fuente, unidad, perspectiva y criterio propios.
- El Outcome técnico no se reutiliza como Value sin una justificación de constructo y medición que evite circularidad.
- No se fija índice escalar, peso, normalización, compensabilidad ni regla de trade-off global.

### 4.4 Ficha V_j — campos exigidos y estado

| Campo §224 | Requisito para cierre | Estado |
|---|---|---|
| Identidad/definición | value_dimension_id, constructo y frontera | No existe V_j seleccionada |
| Beneficiario/contexto | B1, UE, Need_preZ y contexto versionados | Tipo/relación aceptados; instancia/Need OPEN |
| Perspectiva/autoridad | Regla ex ante y legitimidad interna del DGP | Perspectiva B1 como base; autoridad concreta OPEN |
| Criterio de valoración | Relación entre consecuencia y objetivo basal | OPEN |
| Indicador/fuente/instrumento | Medición directa o proxy validado, provenance | OPEN |
| Unidad/escala/dirección | Rango, anclas y significado | OPEN |
| Baseline/post/horizonte | Medida basal y ventana común preespecificada | Need_preZ conceptual; medición/tiempo OPEN |
| Procedimiento/adjudicador | Aplicación simétrica, ciega a Z cuando viable | OPEN |
| Validez/fiabilidad/error | P182, acuerdo, invariancia y sensibilidad | Contratos existentes; evidencia/parámetros OPEN |
| Ausencia/censura/desacuerdo | P183 y estados separados | Contratos existentes; mecanismos/valores OPEN |
| Trade-offs | Compensable/no compensable y relaciones V_j | OPEN; sin pesos |
| Selección confirmatoria | Antes de generar/observar resultados y versionada | No realizada |

**Dictamen Value:** arquitectura vectorial y reglas de admisibilidad reconciliadas; ninguna dimensión, escala, instrumento, regla valorativa o endpoint V_j está instanciado. No existe todavía un resultado Value confirmatorio.

## 5. Separación causal y consecuencias para C1–C4

El DGP debe representar por separado las rutas:
- Z/política → proceso técnico → O-CONF;
- Z/política → ΔT_acc*/Reach/trayectoria/ejecución → consecuencia B1 → V_j;
- Z/política → vías directas/colaterales → consecuencia B1 → V_j;
- O-CONF → consecuencia B1 → V_j, solo si el DGP lo estipula y lo identifica como mecanismo.

Estas rutas son posibilidades del diseño, no flechas empíricas aprobadas. Outcome no es causa exclusiva por definición y Value no es función mecánica de Outcome.

Para cada población, versión, dimensión y horizonte:
- ITT_Z^D2(O-CONF) y ITT_Z^D2(V_j) son estimandos separados.
- La identificación del ITT de Outcome no se transfiere a Value, ni entre dimensiones.
- C3/θ_A o θ_Af sobre V_j requiere intervención de accesibilidad, mapping, soporte, régimen común y control/identificación de vías colaterales.
- C4 requiere intervención mediadora, orden temporal, tratamiento de confusión mediador–resultado inducida por Z y soporte longitudinal.
- Un efecto de paquete puede ser identificable sin atribución exclusiva a accesibilidad.
- Si las rutas causales o medición no permiten identificación puntual, la salida correcta es CONDITIONAL, BOUNDS (solo con restricciones justificadas), NOT_IDENTIFIED o INDETERMINATE_MEASUREMENT.

No se calcula efecto directo/residual por resta entre estimandos incompatibles. No se promueve un resultado técnico favorable a afirmación de creación de Value.

## 6. Verdad, observación y evaluación

- **truth_dgp:** Need_preZ, perspectiva/autoridad, criterio valorativo, consecuencias potenciales, O-CONF verdadero, V_j verdadero, mecanismos, interacciones y versiones.
- **observed_evidence:** snapshots, logs, instrumentos, fuentes, adjudicaciones y medidas permitidas al Analyzer, con cobertura, error, missingness y provenance. No contiene contrafactuales ni truth reservado.
- **evaluation/adjudication:** el Evaluator compara la salida sellada del Analyzer con truth después de congelar esa salida. No corrige retrospectivamente observaciones ni revela truth al Analyzer.

P182/P183 y las familias MEAS/MISS existentes se reutilizan por constructo y dimensión. No se crean nuevos IDs de prueba. Las tolerancias, umbrales de error, criterios de abstención y parámetros de sensibilidad siguen OPEN hasta su justificación.

## 7. Crosswalk de contratos existentes y cobertura

| Requisito | Contrato existente | Resultado de esta reconciliación |
|---|---|---|
| Separación A/O/V | P179-01…03 | Semántica reconciliada; fichas materiales OPEN |
| Vector y resultados por dimensión | P179-02 | Regla preservada; dimensiones no seleccionadas |
| Perspectiva/contexto | P179-04 | B1 como referente; autoridad/criterio OPEN |
| Baseline | P179-05 | Need_preZ conceptual; medidas basales OPEN |
| Trade-offs | P179-06 | No agregación prematura; regla por dimensión OPEN |
| ITT/estimación por dimensión | P179-07 | No estimable hasta diseño, medida y soporte |
| Agregación | P179-08 | Sin índice/pesos por defecto |
| Validez/error/cegamiento/invariancia | P182-01…12; MEAS-01…14 | Reutilizados; no ejecutados ni materializados |
| Ausencia/selección/censura/bounds | P183-01…13; MISS-01…15 | Reutilizados; mecanismos y parámetros OPEN |
| Ficha de Outcome | §224.2 | O-CONF candidato; ficha incompleta |
| Ficha Value | §224.3 | Ninguna V_j instanciada |
| Adjudicación/canales | §224.4 y PD/PE | Arquitectura definida; separación computacional no validada |

No se duplican pruebas. La presencia de un ID en el registro no implica fixture, implementación, ejecución ni PASS.

## 8. Dictamen integrado

| Elemento | Estado |
|---|---|
| Distinción F* / O-CONF / Value | RECONCILED DOCUMENTALLY |
| O-CONF | PRIORITY CANDIDATE / NOT CONFIRMATORY / NOT OPERATIONALIZED |
| FP-01…07 | Familias aceptadas; predicados/IAM/oráculo incompletos |
| FP-08 | Gate probatorio separado; evidencia material no disponible |
| B1/Need_preZ | Base semántica aceptada; contenido/medida material OPEN |
| Perspectiva B1 | Base aceptada |
| Autoridad y criterio de valoración | OPEN |
| Vector P179 | PRESERVED |
| Dimensiones V_j / k | NOT SELECTED / OPEN |
| Indicadores, instrumentos, escalas, baseline, horizonte | OPEN |
| P182/P183 | Contratos existentes reutilizados; evidencia/parámetros no cerrados |
| ITT por O/V | Familias separadas; no confirmatorias ni identificadas actualmente |
| C3/C4 por O/V | NOT IDENTIFIED IN CURRENT MATERIAL DESIGN |
| Design Freeze / implementation / execution | BLOCKED / NOT AUTHORIZED |

## 9. Condiciones para cerrar la medición y el Design Freeze

Antes de cerrar G-SCI/G-MAT/G-TEST deben existir:
1. DGP/instancia y roster B1/UE versionados, con Need_preZ y evidencia basal;
2. F* con predicados atómicos, mapping, IAM, obligatoriedad/NA, C0/G/H y snapshots;
3. O-CONF con evento terminal, fuente/oráculo independiente validado, regla, error, cobertura, cegamiento y ficha §224 completa;
4. decisión justificada de si O-CONF es el único Outcome confirmatorio o si otro O_k tiene una razón científica independiente; no se añade por disponibilidad de datos;
5. criterio de Value y autoridad de valoración estipulados en truth_dgp;
6. selección ex ante y justificada de al menos el conjunto de dimensiones V_j que se pretenda estudiar; cada ficha §224 completa;
7. fuentes/instrumentos y validación P182, missingness/censura P183 y regla de trade-offs;
8. DAG y estimandos por resultado/dimensión/horizonte, con vías colaterales e interacciones;
9. asignación D2, población, soporte, unidad/interferencia y horizonte reconciliados con el ciclo previo;
10. separación efectiva Generator/Analyzer/Evaluator y criterios de recuperación/abstención P177/P178.

Si estos requisitos no pueden satisfacerse, se reduce explícitamente el alcance confirmatorio o se mantiene NOT_IDENTIFIED/INDETERMINATE; no se completa con supuestos favorables.

## 10. Autorización y no-regresión

Este documento cierra la reconciliación de arquitectura de medición y de criterios de admisibilidad; no operacionaliza O-CONF ni instancia Value. No crea decisión científica, no cambia DEC-C10-095, D2, población, B1, Opción A, TGCV Core, RMA, Evidence→Claim Matrix, STATUS o claims.

No se autoriza schema físico, captura material, fixtures, código, implementación, generación de datos, simulación, estimación o ejecución científica.

`scientific_execution=false`; `execution_authorized=false`.

## 12. Caso de valoración B1 — dependencia contextual pendiente (2026-11-11)

El caso semántico se documenta en `C10_S_B1_VALUATION_CASE_RECONCILIATION_DRAFT_001.md`. El microdominio de migración está aceptado; B1 por UE, servicio por UE y una oportunidad estandarizada por UE se reutilizan. El probe no representa demanda natural ni Value. La formulación candidata de Need_preZ exige un objetivo operativo basal relacionado con sostener una operación de servicio predeclarada en destino; el contenido concreto de esa operación no está aceptado/instanciado. La consecuencia B1 permanece separada de procesamiento, respuesta, F*, O-CONF y accesibilidad. Se describen clases de consecuencia solo como envolvente, no dimensiones aprobadas. No se seleccionan V_j, autoridad, criterio, escala, instrumento u horizonte.


## 14. Dependencia de Need_preZ tras aceptación de la clase de propósito B1 (2026-11-11)

Se acepta como base semántica que B1 pretende mantener operativa una función de servicio dependiente de la configuración migrada al entorno destino. La operación concreta permanece OPEN; por tanto, esta aceptación no completa el constructo ni la truth por UE. La ficha de cualquier V_j deberá referir la consecuencia al objetivo basal concreto una vez nombrado/versionado, no a una formulación genérica ni al éxito técnico de la migración.

La clase aceptada no autoriza asignar `Need_preZ=1` a todas las unidades. Se conserva 1/0/? pre-Z, con unknown distinto de ausencia y truth_dgp distinto de observed_evidence. Request_event, procesamiento, O-CONF, accesibilidad, Reach y ejecución no adjudican Need_preZ ni permiten selección post-Z de la población ITT. La consecuencia B1 sigue siendo un objeto separado de F*/O-CONF y de la valoración V_j. No cambia el estado: O-CONF candidato no congelado; Value vectorial preservado pero no instanciado; sin Y confirmatorio completo ni Design Freeze.


## 16. DEC-C10-099 — Selección provisional de V_cont (2026-11-12)

Se actualiza el estado histórico NO_VJ_SELECTED / VALUE_NOT_INSTANTIATED: tras la aceptación expresa del usuario registrada en §16.174 y formalizada en DEC-C10-099, V_cont es la única dimensión mínima provisional de Value para el núcleo confirmatorio candidato de la extensión sintética B. La selección no implica que Value esté materialmente instanciado ni que exista un endpoint ya operacionalizado. Continúan abiertos el criterio normativo, truth temporal, indicador/fuente, baseline, ventana/horizonte, resolución, escala, regla de agregación, observación independiente, error/cobertura, adjudicación, validez discriminante frente a O-CONF/F* e identificación. Si no se superan los gates, V_cont no será confirmatorio/identificable. P179 permanece vectorial y no se introducen pesos ni otras dimensiones. DEC-C10-095 se complementa dentro del alcance B; no se altera A. No Design Freeze, implementación o ejecución.


## 17. Contrato de medición sintética V_cont — crosswalk y límites (2026-11-12)

El contrato integrado queda desarrollado en el plan C10-S §16.182. Se fija una distinción entre (i) truth temporal latente (A^{B1}_{ik}), definida por el Generator conforme al contrato funcional B1 y al modo ENABLED/PROFILE, y (ii) vector de evidencia S3 observado, imperfecto y potencialmente incompleto. S3 es un canal pasivo candidato; sus señales de proceso/módulo, listener/socket, dependencias, capacidad y perfil runtime no prueban individualmente ni en conjunción automática la admisión funcional. No se crea una regla AND/OR, índice o umbral no justificado.

La agregación (V^{truth}_{cont}=K^{-1}sum A^{B1}_{ik}) sigue siendo candidata y requiere K definido, ventana/rejilla común y aceptación normativa del peso igual por intervalo. El Analyzer solo puede estimar puntualmente si el canal es identificable con calibración accesible bajo el protocolo; sin ello debe emitir bounds o NOT_IDENTIFIED/INDETERMINATE_MEASUREMENT. No se admite usar la media bruta de señales o casos completos como sustituto.

S6 y la oportunidad estandarizada única no se reutilizan como monitor temporal ni se añaden peticiones. O-CONF/F* sigue sin ficha terminal validada; la discriminación V_cont/O-CONF queda CONDITIONAL/NOT_VERIFIABLE. Esta especificación sintética no es validación empírica de señales S3 reales ni instancia Value completa. No altera P179, DEC-C10-095 ni la decisión específica DEC-C10-099; no autoriza implementación/ejecución.


## 18. Reconciliación de la frontera B1–F*–O-CONF–V_cont (2026-11-12)

El contrato funcional B1 §2 define la función de servicio: admitir solicitudes según ENABLED y exponer PROFILE. Las referencias históricas a una operación concreta pendiente se interpretan como ausencia de payload/perfil material, no como ausencia de definición funcional. V_cont mide cumplimiento temporal de esa función; O-CONF adjudica conformidad terminal de la ruta frente a F*. F* no contiene actualmente una regla de continuidad temporal durante toda la ventana.

Se documentan en el plan §16.183 dos contrastes DGP candidatos: terminal conforme tras interrupciones temporales recuperadas; y servicio parcialmente operativo durante la ventana pese a fallo terminal de una propiedad F* independiente. Su admisibilidad depende del cierre de predicados F*, alcance de la verificación y oráculo terminal. No se declaran generados ni validados. O-CONF permanece candidato no operacionalizado; discriminación final CONDITIONAL/NOT_VERIFIABLE.



## 19. Ficha §224 de O-CONF — operacionalización parcial (2026-11-12)

La reconciliación integrada del plan §16.184 y la matriz F* §22 completa la frontera conceptual sin declarar O-CONF operacionalizado.

- **Constructo:** adjudicación terminal de conformidad de una ruta completa de migración frente al criterio funcional F* versionado. F* es el criterio, O-CONF su resultado; no son dos Outcomes distintos.
- **Unidad:** instancia exacta de configuración × ruta (F1→F2 o A1→A2), con binding a UE/B1 cuando el DGP B lo requiera. Los resultados por ruta no se promedian ni se transfieren.
- **Escala:** 1/0/? y SCOPE_ERROR/NOT_EVALUABLE separado. FP-08 es gate probatorio separado, no dimensión funcional compensable.
- **Regla:** todos los predicados obligatorios aplicables FP-01…07 deben ser 1 para O-CONF=1; un 0 obligatorio demostrado da O-CONF=0; ausencia de fallo confirmado con algún obligatorio desconocido da ?; conjunto vacío/cardinalidad constitutiva incumplida bloquea como SCOPE_ERROR. NA solo por IAM ex ante. FP-08 inválido puede dejar O_CONF_obs no evaluable, pero no transforma la truth funcional en 0.
- **Ancla:** post-aplicación/post-check en F2_DST_APPLIED o A2_DST_APPLIED, conforme DEC-C10-071/087. Snapshot, evento y timestamp exactos permanecen OPEN.
- **Fuente:** oráculo independiente/versionado que aplica criterios y mappings a evidencia de fuente, destino, mapping, aplicación y snapshot. Su arquitectura está definida; implementación, versión/hash, error y validación no existen todavía.
- **Contexto/baseline:** C_src y snapshot basal del destino vinculados bajo C0. DEC-C10-070 acepta C0 como binding lógico de cobertura, no fija valores del entorno ni resuelve integridad física.
- **Horizonte:** ruta completa hasta aplicación y verificación dentro de H; H y su relación con el reloj DGP no están fijados.
- **Cobertura/error/acuerdo:** se reutilizan P182/P183; error, falsos positivos/negativos, fiabilidad, acuerdo, missingness, censura, sensibilidad y criterios de abstención siguen abiertos y sin resultados.
- **Cegamiento/provenance:** Generator conserva truth; Analyzer no recibe truth/potenciales/semillas; su salida se sella antes de Evaluator. Los requisitos son documentales; firewall, custodia y ACL no están probados materialmente.

**Dictamen §224:** O_CONF_FICHE_PARTIAL / NOT_OPERATIONALIZED / NOT_CONFIRMATORY / ORACLE_NOT_IMPLEMENTED_NOT_VALIDATED. No se selecciona O-CONF como Outcome confirmatorio final por mera disponibilidad de su anclaje. La decisión de su papel confirmatorio requiere ficha completa y justificación científica, no solo completar campos.



## 20. E+F — precisión de V_cont, P178 y estado confirmatorio (2026-11-12)

La precedencia de medición es el plan §16.182 y su integración §16.186. La verdad V_cont es la secuencia latente A_B1(i,k) por UE e intervalo, estipulada por el Generator conforme a ENABLED/PROFILE. S3 es un vector pasivo de señales imperfectas; no es verificador directo, no se reduce por AND/OR/score arbitrario y su media/proporción observada no sustituye a la verdad. El Analyzer no recibe la secuencia latente ni parámetros reservados. Sin modelo de medición identificable con información permitida, la salida es bounds justificadas o NOT_IDENTIFIED/INDETERMINATE_MEASUREMENT.

La agregación no ponderada K^-1 sum A_B1(i,k) sigue CANDIDATE/OPEN y solo sería interpretable como fracción temporal si los intervalos tienen igual duración y la ventana/rejilla es común y ex ante. K, frecuencia, baseline, inicio/fin y transitorios permanecen OPEN. La decisión provisional de V_cont como dimensión no equivale a aceptar esta escala/indicador.

El P178 clean replay audit 001 cierra la reproducibilidad computacional de un benchmark metodológico acotado (27 celdas, N=700, R=10.000/celda, 270.000 invocaciones, 17/17 tests, artefactos primario/replay byte-idénticos). No es el DGP confirmatorio C10-S, no es validación general del Analyzer y no cubre medición adversarial/no-identificación/interferencia/soporte fallido/rutas directas. Sus N, ratio, R y parámetros no se transfieren. No se repite el replay.

O-CONF permanece ficha §224 parcial, oráculo no implementado/no validado y selección confirmatoria no resuelta. La discriminación V_cont/O-CONF no está verificada. No se declara Outcome ni Value confirmatorio; no Design Freeze, implementación o ejecución.



## 22. DEC-C10-100 — aceptación provisional de escala temporal V_cont (2026-11-12)

Tras DEC-C10-099 (selección de dimensión), se acepta expresamente la regla inicial de agregación de la truth sintética: V_cont_truth(i)=(1/K)Σ_k A_B1(i,k), con K intervalos de igual duración en una rejilla/ventana post-Z común preespecificada. A_B1(i,k)=1/0 por estipulación funcional positiva; ? permanece desconocido. Con intervalos ?, Evaluator conserva bounds [n1/K,(n1+n?)/K], sin imputación a cero ni eliminación del denominador.

La decisión cierra la regla de agregación, no K, frecuencia, duración, inicio/fin, transitorios, baseline, MDE ni canal. El estimando es nivel post-Z; baseline no se resta automáticamente. S3 permanece vector de señales imperfectas y no se promedia para sustituir truth. Estimación puntual exige modelo de medición identificable con información permitida al Analyzer; en otro caso, bounds/abstención.

DEC-C10-100 está registrada en 00_GOVERNANCE/decisions/DEC-C10-100_V_CONT_EQUAL_INTERVAL_TEMPORAL_AGGREGATION_ACCEPTANCE.md. La validez de medición, discriminación O-CONF/F*, identificación y calibración continúan abiertas. No se declara V_cont endpoint confirmatorio validado ni Design Freeze. No autoriza implementación, generación, simulación o ejecución.


## 23. DEC-C10-101/102 — cierre semántico temporal de V_cont (2026-11-12)

Esta sección actualiza la lectura temporal de §§20 y 22 conforme a las decisiones posteriores DEC-C10-100, DEC-C10-101 y DEC-C10-102. No reabre la selección de V_cont ni su regla de agregación.

- La ventana post-Z empieza inmediatamente después de Z en t0 e incluye provisión e instalación; no se condiciona a recepción, instalación, C_dep, accesibilidad, Reach, selección o ejecución.
- La truth por intervalo es estricta: A_B1(i,k)=1 solo si ENABLED/PROFILE se cumple durante todo el intervalo; A_B1(i,k)=0 si ocurre un incumplimiento funcional confirmado en cualquier instante; A_B1(i,k)=? solo si el Generator no determina la truth. No existe periodo de gracia ni tolerancia implícita.
- Se mantiene V_cont_truth=(1/K)Σ A_B1(i,k) con intervalos de igual duración; UNKNOWN se propaga a bounds y no se imputa ni se elimina del denominador.
- S3 sigue siendo un vector pasivo e imperfecto. Falta, pérdida, lag o cobertura insuficiente son estados observacionales, no truth. Sin identificación del canal, Analyzer produce bounds o abstención.
- T* deberá cubrir el periodo de provisión/instalación y el seguimiento hasta el último evento causal que pueda modificar el cumplimiento B1 dentro del estimando. El orden t0…t9 no fija duración física ni determina T*.
- Se recomienda un reloj explícito de tiempo transcurrido, unidad normalizada declarada, eventos fechados y rejilla regular. K=(T*−t0)/Δ con Δ constante y divisibilidad exacta. No se admiten intervalos residuales desiguales.

**Permanecen OPEN:** unidad y anclaje de tiempo normalizado; catálogo de eventos funcionalmente relevantes; mínima duración representable; T*, Δ, K; regla de cierre; frontera exacta; resolución, cobertura, error y calibración S3; validez y discriminación frente a O-CONF. Por tanto, DEC-C10-101/102 cierran inicio y semántica de intervalo, no la parametrización temporal ni el gate confirmatorio.

**Estado:** WINDOW_START_ACCEPTED / STRICT_INTERVAL_TRUTH_ACCEPTED / EQUAL_INTERVAL_AGGREGATION_ACCEPTED / NUMERIC_GRID_OPEN / MEASUREMENT_VALIDITY_OPEN / NOT_DESIGN_FROZEN.

## 24. Corrección de interpretación matemática de V_cont tras DEC-C10-102 (2026-11-12)

Esta sección aclara una consecuencia necesaria de combinar la agregación igualitaria DEC-C10-100 con la continuidad estricta por intervalo DEC-C10-102. No altera ni revoca ninguna de las dos decisiones.

Se mantiene V_cont_truth(i)=(1/K)Σ_k A_B1(i,k), y A_B1(i,k)=1 solo si ENABLED/PROFILE cumple durante todo el intervalo; cualquier incumplimiento funcional confirmado en cualquier instante produce 0 para ese intervalo.

Por ello, V_cont es la **proporción de intervalos completamente conformes**. No es matemáticamente la fracción exacta de tiempo transcurrido en uptime ni una integral de disponibilidad. Un episodio breve confirmado convierte en 0 el intervalo entero afectado; el valor depende de Δ y de la alineación de la rejilla. La expresión anterior “fracción temporal de cumplimiento” debe entenderse en el sentido de proporción de bloques temporales plenamente conformes, no como porcentaje exacto de uptime.

La falta de determinación de truth sigue propagándose a bounds conforme a DEC-C10-100; ausencia/pérdida/lag S3 es incertidumbre observacional y no se recodifica como truth=?/0/1.

Si el objetivo científico exigiera medir el porcentaje exacto de uptime, habría que sustituir la regla binaria estricta por una medida basada en duración de estados (integral/tiempo ponderado), con una decisión nueva. No se adopta esa alternativa ni se reabre ahora la escala aceptada.

**Estado:** EQUAL_INTERVAL_AGGREGATION_PRESERVED / STRICT_BLOCK_COMPLIANCE_SHARE / NOT_EXACT_UPTIME / Δ_AND_GRID_ALIGNMENT_MATERIALLY_DEFINE_SCALE / NO_DESIGN_FREEZE.

## 25. Consecuencia de DEC-C10-102: dominio de medición separado de truth funcional (2026-11-12)

V_cont conserva la proporción de intervalos completamente conformes. No hay periodo de gracia ni duración mínima funcional: un incumplimiento confirmado, por breve que sea, hace A_B1=0 en cada intervalo afectado.

La detectabilidad de S3 es un problema separado. δ_det designa el dominio mínimo de duración para el que el canal pasivo, una vez especificado y calibrado, puede demostrar capacidad de detección bajo sus condiciones de captura/cobertura. No es una tolerancia funcional, no cambia A_B1 y no permite recodificar episodios más breves como conformes. Si un episodio puede afectar truth pero no es observable con fiabilidad, Analyzer debe producir bounds o abstenerse.

Δ de la rejilla V_cont, resolución/cadencia/cobertura S3 y δ_det no son equivalentes. No se afirma recuperación puntual de V_cont sin demostrar que el canal cubre los eventos que determinan cada bloque. Se mantienen separados truth, observación y evaluación.

**Estado:** STRICT_TRUTH_PRESERVED / S3_DETECTION_DOMAIN_NOT_CALIBRATED / V_CONT_RECOVERY_CONDITIONAL / NO_DESIGN_FREEZE.


## 26. Reloj normalizado y límite de interpretación de V_cont (2026-11-12)

V_cont mantiene la proporción de intervalos completamente conformes; no es fracción exacta de uptime. Se representa el tiempo mediante W_c, tramo común de soporte causal desde t0 hasta t_c,max, y x=(t−t0)/W_c, sin unidad física ni conversión a segundos/horas. El horizonte común es T*=1+ρ_follow, con ρ_follow=τ_follow/W_c pendiente.

Las duraciones d_e=δ_event/W_c, la cadencia/resolución S3 c_j/W_c, la anchura Δ y la cola ρ_follow son distintas. El canal S3 se contrasta en modos snapshots/métricas, logs/trazas/eventos e híbrido, sin asumir periodicidad, completitud o independencia. δ_det se informa inicialmente como curva conjunta de detección por duración, fase, familia y versión; un valor puntual requiere umbral p* aprobado.

d_min,DGP limita solo el soporte del benchmark sintético, nunca introduce una tolerancia o periodo de gracia. Cualquier incumplimiento confirmado sigue afectando cada intervalo intersectado. Si S3 no identifica la truth puntual, se reportan bounds o abstención.

**Estado:** V_CONT_SCALE_SEMANTICS_PRESERVED / NORMALIZED_CLOCK_ONLY / DETECTION_THRESHOLD_OPEN / NO_DESIGN_FREEZE.


## 27. Crosswalk temporal de V_cont con P182/P183 (2026-11-12)

La recuperación de V_cont reutiliza los escenarios temporales del plan §16.196 y P182/P183/MEAS/MISS; no crea una prueba ni un estimando nuevo. Los errores de S3 se evalúan con P182-07/08; la separación Analyzer–truth y trazabilidad con P182-11/12; ausencia y mecanismo con P183-01/02; no observado≠cero con P183-04; pérdida diferencial/selección con P183-07/10 y MEAS/MISS existentes; censura y bounds con P183-09/11; discriminación temporal-terminal con P182-04/10.

V_cont_truth sigue siendo la proporción de intervalos completamente conformes bajo DEC-C10-100/102. Las variantes snapshot/métrica, logs/trazas y híbrida son mecanismos dentro de S3, no Outcomes ni fuentes nuevas. Una señal S3 no demuestra por sí sola capacidad B1; si la curva conjunta de observación no identifica la secuencia, se informan bounds o NOT_IDENTIFIED. O-CONF/F* permanece como adjudicación terminal independiente. No se infiere Value contextual ni se eleva ningún claim.

**Estado:** V_CONT_MEASUREMENT_TEST_CROSSWALK_DEFINED / CHANNEL_VALIDITY_OPEN / O_CONF_DISCRIMINATION_NOT_VERIFIED / NO_DESIGN_FREEZE.


## 28. Corrección semántica y límite de interpretación de V_cont (2026-11-12)

DEC-C10-100/102 operacionalizan V_cont_truth como la proporción de intervalos completamente conformes. Dado que cualquier incumplimiento confirmado pone a cero el intervalo completo, esta medida no equivale a la fracción exacta de tiempo disponible ni a uptime integral; depende de Δ y de la alineación de la rejilla. Se conserva la regla aceptada y no se modifica la fórmula. Las salidas no podrán describirse como porcentaje exacto de tiempo en servicio.

Se mantiene separada la validez de la medición S3: el Generator estipula A_B1; Analyzer solo recupera lo identificable desde evidencia sellada; de otro modo produce bounds/abstención. O-CONF sigue siendo un Outcome terminal independiente. La interpretación de V_cont como medida de intervalos completos debe preservarse en estimandos, informes y claims, sin extrapolar a continuidad temporal exacta.
